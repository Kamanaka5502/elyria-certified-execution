# Certification Matrix

Built by **Elyria Systems — VA**.

Copyright (c) 2026 **Samantha Revita** and **Terry Snyder**. All rights reserved.

This matrix is public-safe. It defines the visible certification ladder without exposing private runtime law, protected enforcement internals, private certification methodology, or customer-specific certification reports.

## Level Matrix

| Level | Name | What It Proves | What It Does Not Prove | Public Example |
|---|---|---|---|---|
| C0 | Claim Only | Governance is asserted. | No enforceable proof. | Empty / unsupported claim. |
| C1 | Logged Execution | Actions are recorded after they occur. | No pre-effect admissibility, receipt integrity, or replay. | Missing required structured fields. |
| C2 | Receipt-Bearing Execution | Structured receipt exists. | Proof classes may be incomplete. Boundary enforcement not proven. | `examples/c2_receipt_bearing_receipt.json` |
| C3 | Replay-Verifiable Execution | Receipt can be replayed under identical state/law/input conditions. | Boundary enforcement may still be absent. | Reserved for future public example. |
| C4 | Boundary-Enforced Execution | Action is admitted/refused before consequence binds inside one boundary. | Cross-boundary corridor standing is not proven. | `examples/c4_boundary_enforced_receipt.json` |
| C5 | Cross-Boundary Certified Execution | Execution remains admissible across organizations, agents, data corridors, authority domains, and transfer relations. | Does not disclose private certification methods or customer reports. | `examples/c5_cross_boundary_receipt.json` |

## Proof Class Matrix

| Proof Class | C0 | C1 | C2 | C3 | C4 | C5 |
|---|---:|---:|---:|---:|---:|---:|
| Structured receipt fields | No | Partial | Yes | Yes | Yes | Yes |
| Standing proof | No | No | Optional / incomplete | Yes | Yes | Yes |
| Authority proof | No | No | Optional / incomplete | Yes | Yes | Yes |
| Receipt integrity proof | No | No | Yes | Yes | Yes | Yes |
| Replay verification proof | No | No | Optional / incomplete | Yes | Yes | Yes |
| Boundary enforcement proof | No | No | No | Optional / incomplete | Yes | Yes |
| Corridor proof | No | No | No | No | No / not required | Yes |
| Fail-closed proof | No | No | Optional / incomplete | Yes | Yes | Yes |

## Outcome Semantics

Certified execution recognizes these public outcomes:

```text
ADMIT
NARROW
ESCALATE
REFUSE
HALT
QUARANTINE
REBOUND
```

A system that silently continues after standing fails cannot certify beyond claim or logging behavior.

## Boundary Distinction

```text
C2 proves evidence exists.
C3 proves evidence can replay.
C4 proves consequence is controlled before binding.
C5 proves the boundary relation itself remains admissible across domains.
```

## Reviewer Rule

A reviewer should not ask only:

```text
Did the system log what happened?
```

The certification question is:

```text
Could the system prove the consequence was admissible before it bound?
```

For C5, the stronger question is:

```text
Could the system prove the transfer relation itself had standing across the boundary?
```

## Protected Boundary

This matrix does not disclose:

```text
private runtime law
protected enforcement internals
private certification methodology
customer-specific certification reports
private law bundles
production deployment architecture
NDA-bound formal proofs
commercial pilot terms
```
