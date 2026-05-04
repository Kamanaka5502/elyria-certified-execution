# Reviewer Brief

Built by **Elyria Systems — VA**.

Copyright (c) 2026 **Samantha Revita** and **Terry Snyder**. All rights reserved.

## One-minute read

Elyria Certified Execution is a protected public proof surface for certification of consequence-bearing AI execution.

It defines what must be proven before an AI action, agent action, tool call, transfer, recommendation, or automated consequence can be treated as governed execution.

The core rule:

```text
A system is not certified because it has policies, logs, controls, or approvals.

A system is certified only if consequence-bearing actions are admitted, bounded, receipt-bearing, replayable, and fail-closed at the boundary where they bind.
```

## What reviewers should look for

Reviewers should distinguish between systems that merely describe governance and systems that prove admissible execution.

The key question is:

```text
Can the system prove that consequence was admissible at the moment it bound?
```

If the answer depends only on policy documents, logs, dashboards, manual review, authentication, or inferred continuity, the system is not certified execution.

## Certification levels

```text
C0 — Claim Only
Governance is asserted but not proven.

C1 — Logged Execution
Actions are recorded after they occur.

C2 — Receipt-Bearing Execution
Structured receipts exist for decisions/actions.

C3 — Replay-Verifiable Execution
Receipts can be replayed under identical state/law/input conditions.

C4 — Boundary-Enforced Execution
Actions are admitted or refused before consequence binds.

C5 — Cross-Boundary Certified Execution
Execution remains admissible across organizations, agents, data corridors, authority domains, and transfer relations.
```

## Required proof classes

```text
Standing Proof
Authority Proof
Corridor Proof
Receipt Integrity Proof
Replay Verification Proof
Fail-Closed Proof
```

## Current public proof

The current public proof includes:

```text
certify.py
examples/c5_cross_boundary_receipt.json
test_certify.py
.github/workflows/proof.yml
```

Run:

```bash
python certify.py examples/c5_cross_boundary_receipt.json
python certify.py examples/c5_cross_boundary_receipt.json --compact
python test_certify.py
```

Expected result:

```text
C5 — Cross-Boundary Certified Execution
```

## What this is not

This repository is not:

```text
production certification engine
customer audit package
regulated certification grant
open-source project
commercial license grant
private law-bundle disclosure
production deployment architecture
```

## Protected boundary

This repository intentionally excludes:

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

## Reviewer conclusion

A reviewer should leave with one conclusion:

```text
Certification is not trust language.
Certification is replayable proof that consequence was admissible when it bound.
```
