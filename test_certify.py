#!/usr/bin/env python3
"""
Elyria Certified Execution Tests
Built by Elyria Systems — VA

Public-safe tests for the C0-C5 certification validator.
"""
from __future__ import annotations

from pathlib import Path

from certify import certify, load_json


EXAMPLE_C2 = Path("examples/c2_receipt_bearing_receipt.json")
EXAMPLE_C4 = Path("examples/c4_boundary_enforced_receipt.json")
EXAMPLE_C5 = Path("examples/c5_cross_boundary_receipt.json")


def test_c5_cross_boundary_receipt_certifies():
    receipt = load_json(EXAMPLE_C5)
    result = certify(receipt)

    assert result.passed is True
    assert result.certification_level == "C5"
    assert result.level_name == "Cross-Boundary Certified Execution"
    assert result.missing_fields == []
    assert result.missing_proofs == []
    assert result.decision_hash
    assert result.certification_hash


def test_c4_boundary_enforced_receipt_certifies():
    receipt = load_json(EXAMPLE_C4)
    result = certify(receipt)

    assert result.passed is True
    assert result.certification_level == "C4"
    assert result.level_name == "Boundary-Enforced Execution"
    assert result.missing_fields == []
    assert result.missing_proofs == []
    assert result.decision_hash
    assert result.certification_hash


def test_c2_receipt_bearing_example_classifies_as_c2():
    receipt = load_json(EXAMPLE_C2)
    result = certify(receipt)

    assert result.passed is False
    assert result.certification_level == "C2"
    assert result.level_name == "Receipt-Bearing Execution"
    assert result.missing_fields == []
    assert "standing_proof" in result.missing_proofs
    assert "authority_proof" in result.missing_proofs
    assert "replay_verification_proof" in result.missing_proofs
    assert "fail_closed_proof" in result.missing_proofs


def test_empty_receipt_is_c0():
    result = certify({})

    assert result.passed is False
    assert result.certification_level == "C0"
    assert result.level_name == "Claim Only"


def test_logged_execution_without_required_fields_is_c1():
    result = certify({"decision": "ADMIT"})

    assert result.passed is False
    assert result.certification_level == "C1"
    assert result.level_name == "Logged Execution"
    assert result.missing_fields


def test_receipt_without_proofs_is_c2():
    receipt = load_json(EXAMPLE_C5)
    receipt["proofs"] = {}

    result = certify(receipt)

    assert result.passed is False
    assert result.certification_level == "C2"
    assert result.level_name == "Receipt-Bearing Execution"
    assert result.missing_proofs


def test_cross_boundary_without_corridor_proof_does_not_reach_c5():
    receipt = load_json(EXAMPLE_C5)
    receipt["proofs"]["corridor_proof"]["status"] = "FAIL"

    result = certify(receipt)

    assert result.passed is True
    assert result.certification_level == "C4"
    assert result.level_name == "Boundary-Enforced Execution"
    assert "corridor_proof" in result.missing_proofs


if __name__ == "__main__":
    import pytest
    raise SystemExit(pytest.main([__file__, "-q"]))
