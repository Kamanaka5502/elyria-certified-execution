# Run the Elyria Certified Execution Proof

Built by **Elyria Systems — VA**.

Copyright (c) 2026 **Samantha Revita** and **Terry Snyder**. All rights reserved.

This repository is a protected public proof surface for consequence-bearing AI execution certification.

## Clone

```bash
git clone https://github.com/Kamanaka5502/elyria-certified-execution.git
cd elyria-certified-execution
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run the C5 certification proof

```bash
python certify.py examples/c5_cross_boundary_receipt.json
```

Compact output:

```bash
python certify.py examples/c5_cross_boundary_receipt.json --compact
```

Expected certification level:

```text
C5 — Cross-Boundary Certified Execution
```

## Run tests

```bash
python test_certify.py
```

The tests verify:

```text
C5 cross-boundary receipt certifies
empty receipt falls to C0
missing fields falls to C1
missing proofs falls to C2
cross-boundary receipt without corridor proof does not reach C5
```

## GitHub Actions

The repository includes a proof workflow:

```text
.github/workflows/proof.yml
```

It runs the public validator, compact validator output, and test suite on push, pull request, and manual dispatch.

## Proof principle

A system is not certified because it has policies, logs, controls, or approvals.

A system is certified only if consequence-bearing actions are admitted, bounded, receipt-bearing, replayable, and fail-closed at the boundary where they bind.

## Protected scope

This repository does not expose private runtime law, protected enforcement internals, private certification methodology, customer-specific certification reports, private law bundles, production deployment architecture, NDA-bound formal proofs, or deployment-sensitive architecture.

See `PROTECTED_SCOPE.md`.
