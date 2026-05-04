#!/usr/bin/env python3
"""
Elyria Certified Execution Validator
Built by Elyria Systems — VA

Public-safe validator for consequence-bearing AI execution certification.

This validator does not expose private runtime law, protected enforcement internals,
private certification methodology, customer reports, or production deployment logic.
It demonstrates the public C0-C5 certification surface only.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from hashlib import sha256
import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Tuple


REQUIRED_RECEIPT_FIELDS = [
    "receipt_id",
    "system_id",
    "action_id",
    "consequence_type",
    "boundary_time",
    "decision",
    "state_hash",
    "authority_hash",
    "standing_hash",
    "corridor_hash",
    "law_bundle_hash",
    "rule_trace_hash",
    "outcome_hash",
    "fail_closed_outcome",
    "replay_token",
]

REQUIRED_PROOFS = [
    "standing_proof",
    "authority_proof",
    "receipt_integrity_proof",
    "replay_verification_proof",
    "fail_closed_proof",
]

CROSS_BOUNDARY_PROOFS = [
    "corridor_proof",
]


@dataclass(frozen=True)
class CertificationResult:
    certification_level: str
    level_name: str
    passed: bool
    reasons: List[str]
    missing_fields: List[str]
    missing_proofs: List[str]
    decision_hash: str
    certification_hash: str


def stable_hash(obj: Any) -> str:
    encoded = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return sha256(encoded).hexdigest()


def load_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def proof_true(receipt: Dict[str, Any], proof_name: str) -> bool:
    proof = receipt.get("proofs", {}).get(proof_name)
    return isinstance(proof, dict) and proof.get("status") == "PASS"


def classify(receipt: Dict[str, Any]) -> Tuple[str, str, List[str], List[str], List[str]]:
    reasons: List[str] = []
    missing_fields = [field for field in REQUIRED_RECEIPT_FIELDS if field not in receipt]
    missing_proofs = [proof for proof in REQUIRED_PROOFS if not proof_true(receipt, proof)]

    if not receipt:
        return "C0", "Claim Only", ["empty or unreadable receipt"], REQUIRED_RECEIPT_FIELDS, REQUIRED_PROOFS

    if missing_fields:
        reasons.append("receipt lacks required structured fields")
        return "C1", "Logged Execution", reasons, missing_fields, missing_proofs

    if receipt.get("decision") not in {"ADMIT", "NARROW", "ESCALATE", "REFUSE", "HALT", "QUARANTINE", "REBOUND"}:
        reasons.append("decision is not an admitted certified-execution outcome")
        return "C1", "Logged Execution", reasons, missing_fields, missing_proofs

    if missing_proofs:
        reasons.append("receipt exists but required proof classes are incomplete")
        return "C2", "Receipt-Bearing Execution", reasons, missing_fields, missing_proofs

    if not receipt.get("replay_token") or not proof_true(receipt, "replay_verification_proof"):
        reasons.append("receipt is not replay-verifiable")
        return "C2", "Receipt-Bearing Execution", reasons, missing_fields, missing_proofs

    if not proof_true(receipt, "standing_proof") or not proof_true(receipt, "authority_proof"):
        reasons.append("standing or authority proof is incomplete")
        return "C3", "Replay-Verifiable Execution", reasons, missing_fields, missing_proofs

    if receipt.get("boundary_enforced") is not True:
        reasons.append("action is replay-verifiable but not proven boundary-enforced")
        return "C3", "Replay-Verifiable Execution", reasons, missing_fields, missing_proofs

    if receipt.get("cross_boundary") is True:
        corridor_missing = [proof for proof in CROSS_BOUNDARY_PROOFS if not proof_true(receipt, proof)]
        if corridor_missing:
            reasons.append("cross-boundary execution lacks corridor proof")
            return "C4", "Boundary-Enforced Execution", reasons, missing_fields, corridor_missing
        reasons.append("cross-boundary consequence is standing-, authority-, corridor-, receipt-, replay-, and fail-closed certified")
        return "C5", "Cross-Boundary Certified Execution", reasons, missing_fields, []

    reasons.append("execution is boundary-enforced, receipt-bearing, replay-verifiable, and fail-closed")
    return "C4", "Boundary-Enforced Execution", reasons, missing_fields, []


def certify(receipt: Dict[str, Any]) -> CertificationResult:
    level, name, reasons, missing_fields, missing_proofs = classify(receipt)
    decision_hash = stable_hash(receipt)
    result_payload = {
        "level": level,
        "name": name,
        "passed": level in {"C4", "C5"},
        "reasons": reasons,
        "missing_fields": missing_fields,
        "missing_proofs": missing_proofs,
        "decision_hash": decision_hash,
    }
    return CertificationResult(
        certification_level=level,
        level_name=name,
        passed=level in {"C4", "C5"},
        reasons=reasons,
        missing_fields=missing_fields,
        missing_proofs=missing_proofs,
        decision_hash=decision_hash,
        certification_hash=stable_hash(result_payload),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a public-safe Elyria Certified Execution receipt.")
    parser.add_argument("receipt", type=Path, help="Path to a JSON receipt file.")
    parser.add_argument("--compact", action="store_true", help="Emit compact JSON.")
    args = parser.parse_args()

    receipt = load_json(args.receipt)
    result = certify(receipt)
    payload = asdict(result)
    if args.compact:
        print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
    else:
        print(json.dumps(payload, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
