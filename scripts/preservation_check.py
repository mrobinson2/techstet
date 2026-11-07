#!/usr/bin/env python3
"""Preservation gate: diff an edited document against its source for the invariants
technical prose cannot lose. Prints a markdown report; exits 1 if anything is flagged.

usage: preservation_check.py ORIGINAL EDITED [--terms terms.txt] [--genre policy|adr|runbook|design-doc|incident|readme|brief|book-chapter|blog]

terms.txt: one term per line; '#' comments; 'term|variant|variant' to catch known drifts.
"""
import argparse, difflib, re, sys
from collections import Counter

MODALS = ["may", "might", "must", "shall", "should", "can", "cannot", "could", "will", "would",
          "only", "unless", "never", "always", "before", "after", "not"]
HEDGES = ["i think", "probably", "perhaps", "in most cases", "where relevant", "roughly", "approximately", "typically", "in general"]
LEAKS = {"contraction": r"\b\w+(?:'|’)(?:t|s|re|ve|ll|d)\b", "second person": r"\b[Yy]ou(?:r|rs)?\b",
         "however": r"\bHowever\b", "here": r"\bhere\b", "actually": r"\bactually\b", "just": r"\bjust\b",
         "em/en dash": r"[—–]|\s--\s"}
NEUTRAL = {"policy", "adr", "design-doc", "incident", "brief"}

def paras(t):
    return [p.strip() for p in re.split(r"\n\s*\n", t) if p.strip()]

def sents(t):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", t) if s.strip()]

def words(t):
    return re.findall(r"\b[\w'’-]+\b", t)

def figures(t):
    return Counter(re.findall(r"\b\d[\d,.:/%-]*\w*\b", t))

def headings(t):
    return [l.rstrip() for l in t.split("\n") if re.match(r"^#{1,6}\s", l)]

def labels(t):
    out = []
    for l in t.split("\n"):
        m = re.match(r"^\s*(?:[-*]|\d+\.)\s+\*\*([^*]+)\*\*", l)
        if m: out.append(m.group(1).strip().rstrip(":."))
    return out

def fragments(t):
    """bullets / table cells without a terminal period"""
    out = []
    for l in t.split("\n"):
        if re.match(r"^\s*(?:[-*]|\d+\.)\s+", l) and not re.search(r"[.!?]\s*$", l):
            out.append(re.sub(r"^\s*(?:[-*]|\d+\.)\s+", "", l).strip())
    return out

def proper_nouns(t):
    """capitalized tokens that follow a lowercase word in running prose (skips sentence starts,
    table cells, bold labels, list markers); plus camelCase and ALLCAPS anywhere"""
    out = set()
    for s in sents(t):
        toks = re.findall(r"[^\s]+", s)
        for i, w in enumerate(toks):
            core = re.sub(r"^[^\w]+|[^\w]+$", "", w)
            if not core: continue
            if re.match(r"^[a-z]+[A-Z]\w+$", core) or re.match(r"^[A-Z]{2,}$", core): out.add(core); continue
            if i == 0: continue
            prev = re.sub(r"^[^\w]+|[^\w]+$", "", toks[i-1])
            if not re.match(r"^[a-z][a-z'’-]*$", prev): continue
            if re.search(r"[|*:]", toks[i-1]): continue
            if re.match(r"^[A-Z][a-zA-Z]+$", core) and len(core) > 2: out.add(core)
    return out

def passives(t):
    return len(re.findall(r"\b(?:is|are|was|were|be|been|being)\s+(?:\w+ly\s+)?(?:\w+ed|made|met|set|done|named|held|kept|sent|put|seen|given|taken|known|shown|written)\b", t))

def count(p, t):
    return len(re.findall(p, t))

def align(a, b, cutoff=0.45):
    """pair paragraphs by similarity; return list of (i, j|None)"""
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    pairs, used = [], set()
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1): pairs.append((i1 + k, j1 + k)); used.add(j1 + k)
        else:
            for i in range(i1, i2):
                best, bj = 0, None
                for j in range(j1, j2):
                    if j in used: continue
                    r = difflib.SequenceMatcher(None, a[i], b[j], autojunk=False).ratio()
                    if r > best: best, bj = r, j
                if bj is not None and best >= cutoff: pairs.append((i, bj)); used.add(bj)
                else: pairs.append((i, None))
    return pairs, used

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("original"); ap.add_argument("edited")
    ap.add_argument("--terms"); ap.add_argument("--genre", default="policy")
    a = ap.parse_args()
    A = open(a.original, encoding="utf-8").read(); B = open(a.edited, encoding="utf-8").read()
    flags, rows = [], []
    def row(name, status, detail=""):
        rows.append((name, status, detail));
        if status == "FLAG": flags.append(name)

    # terms
    terms = []
    if a.terms:
        for l in open(a.terms, encoding="utf-8"):
            l = l.split("#")[0].strip()
            if l: parts = [p.strip() for p in l.split("|")]; terms.append((parts[0], parts[1:]))
    tdet = []
    for t, variants in terms:
        ca, cb = count(r"\b" + re.escape(t) + r"\b", A), count(r"\b" + re.escape(t) + r"\b", B)
        if cb < ca: tdet.append(f"'{t}' {ca}→{cb}")
        for v in variants:
            cv = count(r"\b" + re.escape(v) + r"\b", B) - count(r"\b" + re.escape(v) + r"\b", A)
            if cv > 0: tdet.append(f"variant '{v}' +{cv} (for '{t}')")
    row("Terms", "FLAG" if tdet else "pass", "; ".join(tdet) if terms else "no term list supplied")

    # paragraph alignment
    PA, PB = paras(A), paras(B)
    pairs, used = align(PA, PB)
    deleted = [PA[i][:80] for i, j in pairs if j is None]
    added = [PB[j][:80] for j in range(len(PB)) if j not in used]
    row("Paragraphs", "FLAG" if deleted or added else "pass",
        (f"{len(deleted)} source paragraph(s) with no counterpart: " + " | ".join(deleted) if deleted else "") +
        (f" || {len(added)} new paragraph(s): " + " | ".join(added) if added else ""))

    # modals per aligned pair
    mdet = []
    for i, j in pairs:
        if j is None: continue
        ma = Counter(w.lower() for w in words(PA[i]) if w.lower() in MODALS)
        mb = Counter(w.lower() for w in words(PB[j]) if w.lower() in MODALS)
        if ma != mb:
            d = {k: (ma[k], mb[k]) for k in set(ma) | set(mb) if ma[k] != mb[k]}
            mdet.append(f"¶{i+1} " + ", ".join(f"{k} {x}→{y}" for k, (x, y) in sorted(d.items())))
    row("Modals", "FLAG" if mdet else "pass", "; ".join(mdet[:12]) + (" …" if len(mdet) > 12 else ""))

    # figures
    fa, fb = figures(A), figures(B)
    miss = [f for f in fa if fb[f] < fa[f]]; new = [f for f in fb if fa[f] < fb[f]]
    row("Figures", "FLAG" if miss or new else "pass",
        (f"missing: {', '.join(miss)}" if miss else "") + (f" new: {', '.join(new)}" if new else ""))

    # headings
    ha, hb = headings(A), headings(B)
    hd = [l for l in difflib.unified_diff(ha, hb, lineterm="", n=0) if l[:1] in "+-" and l[:3] not in ("+++", "---")]
    row("Headings", "FLAG" if hd else "pass", " | ".join(hd[:10]))

    # labels
    la, lb = labels(A), labels(B)
    ld = set(la) ^ set(lb)
    row("Labels", "FLAG" if ld else "pass", ", ".join(sorted(ld))[:300])

    # fragments turned into sentences
    fr_a = fragments(A); fr_b = set(fragments(B))
    expanded = []
    for f in fr_a:
        if f in fr_b: continue
        best = max((difflib.SequenceMatcher(None, f, x).ratio(), x) for x in sents(B)) if sents(B) else (0, "")
        if best[0] > 0.6 and len(best[1]) > len(f) * 1.3: expanded.append(f[:60])
    row("Fragments", "FLAG" if expanded else "pass", " | ".join(expanded[:8]))

    # length
    wa, wb = len(words(A)), len(words(B)); ratio = wb / wa if wa else 1
    pl = [f"¶{i+1} {len(words(PB[j]))/max(1,len(words(PA[i]))):.2f}" for i, j in pairs if j is not None and not 0.7 <= len(words(PB[j]))/max(1,len(words(PA[i]))) <= 1.4]
    row("Length", "FLAG" if not 0.85 <= ratio <= 1.15 or pl else "pass", f"overall {ratio:.3f} ({wa}→{wb} words)" + (f"; out of band: {', '.join(pl[:10])}" if pl else ""))

    # code / formatting
    fmt = []
    for name, p in [("backticks", r"`"), ("code blocks", r"^```"), ("bold", r"\*\*"), ("italic", r"(?<!\*)\*(?!\*)"), ("table rows", r"^\|"), ("list items", r"^\s*(?:[-*]|\d+\.)\s"), ("links/paths", r"https?://\S+|(?:/[\w.-]+){2,}")]:
        ca, cb = count(p if not p.startswith("^") else "(?m)" + p, A), count(p if not p.startswith("^") else "(?m)" + p, B)
        if ca != cb: fmt.append(f"{name} {ca}→{cb}")
    row("Code & formatting", "FLAG" if fmt else "pass", "; ".join(fmt))

    # proper nouns added
    pn = sorted(proper_nouns(B) - proper_nouns(A))
    row("Proper nouns added", "FLAG" if pn else "pass", ", ".join(pn)[:300])

    # register leaks
    leaks = []
    for name, p in LEAKS.items():
        ca, cb = count(p, A), count(p, B)
        if cb > ca and (a.genre in NEUTRAL or name == "em/en dash"): leaks.append(f"{name} {ca}→{cb}")
    row("Register leaks", "FLAG" if leaks else "pass", "; ".join(leaks))

    # passives
    pa_, pb_ = passives(A), passives(B)
    row("Passives", "FLAG" if pb_ > pa_ else "pass", f"{pa_}→{pb_}")

    # hedges
    hdg = [h for h in HEDGES if count(r"\b" + h + r"\b", A.lower()) > count(r"\b" + h + r"\b", B.lower())]
    row("Hedges removed", "FLAG" if hdg else "pass", ", ".join(hdg))

    print(f"# Preservation gate: {a.edited} vs {a.original}\n")
    print("| Check | Result | Detail |\n|---|---|---|")
    for n, s, d in rows: print(f"| {n} | {'**FLAG**' if s == 'FLAG' else 'pass'} | {d} |")
    print(f"\n{len(flags)} flag(s): {', '.join(flags) if flags else 'none'}. Resolve each by revert, justify, or ask before delivery.")
    sys.exit(1 if flags else 0)

if __name__ == "__main__":
    main()
