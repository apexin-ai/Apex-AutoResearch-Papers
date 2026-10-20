"""Crash test for Z3 subprocess sandbox.

Verifies:
1. Normal validation works
2. Crash test: worker dies, parent survives, worker restarts
3. Post-crash validation still works
"""

import logging
import sys

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

from z3_sandbox import Z3Sandbox

def main():
    sandbox = Z3Sandbox()

    vocab = {
        "predicates": {"Green": {"arity": 1}, "Big": {"arity": 1}, "Likes": {"arity": 2}},
        "constants": {"cat": {"sort": "entity"}, "dog": {"sort": "entity"}},
    }

    print("=== Test 1: Normal validation ===")
    valid, err = sandbox.validate("ForAll([x], Implies(Green(x), Big(x)))", vocab)
    assert valid and err is None, f"Expected valid, got {valid}, {err}"
    print(f"  PASS: valid={valid}, err={err}")

    valid, err = sandbox.validate("Green(cat)", vocab)
    assert valid and err is None, f"Expected valid, got {valid}, {err}"
    print(f"  PASS: valid={valid}, err={err}")

    valid, err = sandbox.validate("Likes(cat, dog)", vocab)
    assert valid and err is None, f"Expected valid, got {valid}, {err}"
    print(f"  PASS: valid={valid}, err={err}")

    valid, err = sandbox.validate("INVALID SYNTAX !!!", vocab)
    assert not valid, f"Expected invalid, got {valid}"
    print(f"  PASS: valid={valid}, err={err}")

    print("\n=== Test 2: IC check ===")
    fols = ["Green(cat)", "Big(cat)", "ForAll([x], Implies(Green(x), Big(x)))"]
    is_sat, ic_score, mcs_size = sandbox.check_ic(fols, vocab, total_claims=3)
    print(f"  Consistent set: is_sat={is_sat}, ic_score={ic_score:.2f}, mcs={mcs_size}")
    assert is_sat, "Expected SAT for consistent set"

    fols_incon = ["Green(cat)", "Not(Green(cat))"]
    is_sat, ic_score, mcs_size = sandbox.check_ic(fols_incon, vocab, total_claims=2)
    print(f"  Inconsistent set: is_sat={is_sat}, ic_score={ic_score:.2f}, mcs={mcs_size}")
    assert not is_sat, "Expected UNSAT for inconsistent set"
    assert mcs_size == 1, f"Expected MCS=1, got {mcs_size}"

    print("\n=== Test 3: Crash test (os.abort in worker) ===")
    crashed = sandbox.crash_test()
    assert crashed, "Expected crash_test to return True (worker died)"
    print("  PASS: Worker crashed, parent survived")

    print("\n=== Test 4: Post-crash validation ===")
    valid, err = sandbox.validate("Green(cat)", vocab)
    assert valid and err is None, f"Post-crash validation failed: {valid}, {err}"
    print(f"  PASS: valid={valid}, err={err} (worker restarted)")

    valid, err = sandbox.validate("ForAll([x], Implies(Green(x), Big(x)))", vocab)
    assert valid and err is None, f"Post-crash validation failed: {valid}, {err}"
    print(f"  PASS: valid={valid}, err={err}")

    print("\n=== Test 5: Entailment check ===")
    entails, status = sandbox.check_entailment(
        claim_fol_strs=["Green(cat)"],
        vocab=vocab,
        premise_fols=["ForAll([x], Implies(Green(x), Big(x)))"],
        conclusion_fol="Big(cat)",
    )
    print(f"  Entailment: entails={entails}, status={status}")
    assert entails and status == "entails", f"Expected entails, got {entails}, {status}"

    sandbox.shutdown()
    print("\n=== ALL TESTS PASSED ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
