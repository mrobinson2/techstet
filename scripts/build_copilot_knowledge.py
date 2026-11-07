#!/usr/bin/env python3
"""Merge the reference files into one .docx for M365 Copilot knowledge upload.
Uses pandoc if present, otherwise a small markdown-to-HTML pass plus macOS `textutil`.
usage: build_copilot_knowledge.py [skill_dir]"""
import html, os, re, shutil, subprocess, sys, tempfile
root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
refs = [os.path.join(root, "references", f) for f in ["tells.md", "engagement.md", "genres.md", "preservation-gate.md", "long-form.md"]]
out = os.path.join(root, "copilot", "knowledge", "techstet-reference.docx")
os.makedirs(os.path.dirname(out), exist_ok=True)
if shutil.which("pandoc"):
    subprocess.run(["pandoc", *refs, "-o", out], check=True); print("wrote", out, "(pandoc)"); sys.exit()

def inline(s):
    s = html.escape(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", s)
    return s

def md2html(text):
    o, lines, i, inlist, intable = [], text.split("\n"), 0, False, False
    def close():
        nonlocal inlist, intable
        if inlist: o.append("</ul>"); inlist = False
        if intable: o.append("</table>"); intable = False
    while i < len(lines):
        l = lines[i]
        if l.startswith("|"):
            cells = [c.strip() for c in l.strip().strip("|").split("|")]
            if re.match(r"^\|\s*-{3,}", l): i += 1; continue
            if not intable: close(); o.append("<table border='1' cellpadding='4'>"); intable = True; tag = "th"
            else: tag = "td"
            o.append("<tr>" + "".join(f"<{tag}>{inline(c)}</{tag}>" for c in cells) + "</tr>"); i += 1; continue
        if intable: close()
        m = re.match(r"^(#{1,6})\s+(.*)", l)
        if m: close(); o.append(f"<h{len(m.group(1))}>{inline(m.group(2))}</h{len(m.group(1))}>"); i += 1; continue
        if l.startswith("```"):
            close(); buf = []; i += 1
            while i < len(lines) and not lines[i].startswith("```"): buf.append(html.escape(lines[i])); i += 1
            o.append("<pre>" + "\n".join(buf) + "</pre>"); i += 1; continue
        m = re.match(r"^\s*[-*]\s+(.*)", l)
        if m:
            if not inlist: close(); o.append("<ul>"); inlist = True
            o.append(f"<li>{inline(m.group(1))}</li>"); i += 1; continue
        if not l.strip(): close(); i += 1; continue
        close(); o.append(f"<p>{inline(l)}</p>"); i += 1
    close(); return "\n".join(o)

body = "<h1>techstet: reference</h1>" + "".join(md2html(open(f, encoding="utf-8").read()) for f in refs)
tmp = tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8")
tmp.write(f"<html><head><meta charset='utf-8'></head><body>{body}</body></html>"); tmp.close()
subprocess.run(["textutil", "-convert", "docx", tmp.name, "-output", out], check=True)
os.unlink(tmp.name); print("wrote", out, "(textutil)")
