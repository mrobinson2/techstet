# ADR-014: Adopt Azure Key Vault as the default secrets store

**Status:** Proposed

## Context

In today's rapidly evolving cloud landscape, secrets management has emerged as a pivotal concern for our platform teams. Currently, secrets are managed in a variety of ways across the organization — some teams leverage HashiCorp Vault, others utilize platform-specific solutions, and a few still embed credentials in pipeline variables. This fragmentation isn't just an operational inconvenience; it's a security risk.

It's important to note that industry best practices increasingly point toward centralized, cloud-native secrets management. Experts agree that a single source of truth for secrets significantly reduces the attack surface.

## Decision

We will adopt Azure Key Vault as the default secrets management capability for all new Azure-hosted applications, ensuring consistency, enhancing security posture, and streamlining developer workflows.

Teams may request an exception through the architecture review board, which should be granted only where a documented technical constraint exists.

## Options considered

- **Option A: Azure Key Vault.** Native integration, managed identity support, and seamless alignment with our Azure-first strategy.
- **Option B: HashiCorp Vault.** A robust, battle-tested solution, but one that requires us to operate and scale the infrastructure ourselves.
- **Option C: Status quo.** Continue with the current fragmented approach.

One might be tempted to choose Option B given its flexibility. However, the operational overhead is not insignificant.

## Consequences

This decision marks a significant step forward in our security journey. Applications will benefit from automatic rotation, audit logging, and workload identity integration. Teams currently on HashiCorp Vault must migrate within 12 months of this ADR being accepted.

The real question is whether teams will embrace the change. At its core, this is about building a culture of security. The future looks bright.
