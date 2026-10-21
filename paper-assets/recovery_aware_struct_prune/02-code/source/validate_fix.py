"""Validate eval_math500.py bug fixes by comparing v2 (OLD) and v3 (NEW) results."""

import json
import math
import re


def normalize_answer_fixed(ans):
    if ans is None:
        return ""
    ans = str(ans).strip()
    ans = ans.rstrip(".")
    ans = re.sub(r"\\text\{([^}]*)\}", r"\1", ans)
    ans = re.sub(r"\\(mathrm|mathbf|textbf|operatorname)\{([^}]*)\}", r"\2", ans)
    ans = re.sub(r"\\(left|right|displaystyle)", "", ans)
    ans = ans.replace("\\!", "").replace("\\,", "").replace("\\;", "").replace("\\ ", "")
    ans = ans.replace("\\$", "").replace("$", "")
    ans = ans.replace("\\%", "%")
    ans = re.sub(r"\\dfrac", r"\\frac", ans)
    ans = re.sub(r"\\tfrac", r"\\frac", ans)
    ans = ans.replace("{", "").replace("}", "")
    ans = re.sub(r",\s+", ",", ans)
    ans = re.sub(r"\(\s+", "(", ans)
    ans = re.sub(r"\s+\)", ")", ans)
    ans = re.sub(r"(\w)\s*([+-])\s*(\w)", r"\1\2\3", ans)
    ans = re.sub(r"\s+", " ", ans).strip()
    ans = ans.lower()
    if re.match(r'^\([a-zA-Z0-9]\)$', ans):
        ans = ans[1:-1]
    return ans


def normalize_answer_buggy(ans):
    if ans is None:
        return ""
    ans = str(ans).strip()
    ans = ans.rstrip(".")
    ans = re.sub(r"\\text\{([^}]*)\}", r"\1", ans)
    ans = re.sub(r"\\(mathrm|mathbf|textbf|operatorname)\{([^}]*)\}", r"\2", ans)
    ans = re.sub(r"\\(left|right|displaystyle)", "", ans)
    ans = ans.replace("\\!", "").replace("\\,", "").replace("\\;", "").replace("\\ ", "")
    ans = ans.replace("\\$", "").replace("$", "")
    ans = ans.replace("\\%", "%")
    ans = re.sub(r"\\dfrac", r"\\frac", ans)
    ans = re.sub(r"\\tfrac", r"\\frac", ans)
    ans = ans.replace("{", "").replace("}", "")
    ans = re.sub(r"\s+", " ", ans).strip()
    ans = ans.lower()
    return ans


def answers_match_impl(pred, gold, normalize_fn):
    if pred is None:
        return False
    pred_n = normalize_fn(pred)
    gold_n = normalize_fn(gold)
    if not pred_n:
        return False
    if pred_n == gold_n:
        return True
    try:
        def eval_numeric(s):
            s = s.replace("\\frac", "").replace("\\pi", str(math.pi))
            s = re.sub(r"(\d+)\s*(\d+)/(\d+)", lambda m: str(int(m.group(1)) + int(m.group(2))/int(m.group(3))), s)
            s = re.sub(r"(\d+)/(\d+)", lambda m: str(int(m.group(1))/int(m.group(2))), s)
            s = s.replace(",", "").strip()
            return float(s)
        pv = eval_numeric(pred_n)
        gv = eval_numeric(gold_n)
        return abs(pv - gv) < 1e-5
    except (ValueError, OverflowError, ZeroDivisionError):
        pass
    return False


def main():
    v2 = json.load(open("/root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_standard_20_2048_v2.json"))
    v3 = json.load(open("/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_20_2048_v3.json"))
    v2e = v2["examples"]
    v3e = v3["examples"]

    print(f"v2 (OLD): {v2['n_correct']}/{v2['n_total']} = {v2['accuracy']:.4f}")
    print(f"v3 (NEW): {v3['n_correct']}/{v3['n_total']} = {v3['accuracy']:.4f}")
    print()

    diffs = []
    for i, (a, b) in enumerate(zip(v2e, v3e)):
        if a["correct"] != b["correct"]:
            gold = a["gold"]
            v2p = a["pred"]
            v3p = b["pred_answer"]
            diffs.append((i, a["correct"], b["correct"], gold, v2p, v3p))

    v2_plus = [(i, v2c, v3c, g, v2p, v3p) for i, v2c, v3c, g, v2p, v3p in diffs if v2c]
    v3_plus = [(i, v2c, v3c, g, v2p, v3p) for i, v2c, v3c, g, v2p, v3p in diffs if v3c]

    print(f"v2+ (OLD correct, NEW wrong): {len(v2_plus)}")
    print(f"v3+ (OLD wrong, NEW correct): {len(v3_plus)}")
    print()

    # Classify Bug A vs Bug B
    bug_a = [(i, g, v2p, v3p) for i, v2c, v3c, g, v2p, v3p in v2_plus if v2p != v3p]
    bug_b = [(i, g, v2p, v3p) for i, v2c, v3c, g, v2p, v3p in v2_plus if v2p == v3p]

    print(f"Bug A (extraction differs): {len(bug_a)} samples")
    print(f"Bug B (same pred, matching fails): {len(bug_b)} samples")
    print()

    # Test Bug B: fixed matching on v3_pred (same as v2_pred)
    print("=" * 100)
    print("BUG B VERIFICATION (same pred, matching should now work)")
    print("=" * 100)
    hdr = f"{'idx':>4} | {'gold':>30} | {'pred':>30} | {'buggy':>6} | {'fixed':>6}"
    print(hdr)
    print("-" * len(hdr))
    bug_b_fixed = 0
    for i, gold, v2p, v3p in bug_b:
        buggy = answers_match_impl(v3p, gold, normalize_answer_buggy)
        fixed = answers_match_impl(v3p, gold, normalize_answer_fixed)
        status = "FIXED" if fixed and not buggy else ("OK" if fixed else "FAIL")
        if fixed:
            bug_b_fixed += 1
        print(f"{i:4d} | {gold:>30} | {v3p:>30} | {str(buggy):>6} | {str(fixed):>6}  {status}")
    print(f"\nBug B: {bug_b_fixed}/{len(bug_b)} fixed by normalization")

    # Test Bug A: fixed matching on v2_pred (correct extraction from OLD)
    print()
    print("=" * 100)
    print("BUG A VERIFICATION (using v2_pred as proxy for correct extraction)")
    print("=" * 100)
    hdr = f"{'idx':>4} | {'gold':>30} | {'v2_pred':>30} | {'v3_pred':>15} | {'buggy_v2':>8} | {'fixed_v2':>8}"
    print(hdr)
    print("-" * len(hdr))
    bug_a_fixed = 0
    for i, gold, v2p, v3p in bug_a:
        v2p_str = str(v2p)[:30] if v2p else "None"
        v3p_str = str(v3p)[:15] if v3p else "None"
        buggy_v2 = answers_match_impl(v2p, gold, normalize_answer_buggy)
        fixed_v2 = answers_match_impl(v2p, gold, normalize_answer_fixed)
        status = "FIXED" if fixed_v2 and not buggy_v2 else ("OK" if fixed_v2 else "NEEDS_EXTRACT")
        if fixed_v2:
            bug_a_fixed += 1
        gold_n = normalize_answer_fixed(gold)
        v2p_n = normalize_answer_fixed(v2p)
        print(f"{i:4d} | {gold:>30} | {v2p_str:>30} | {v3p_str:>15} | {str(buggy_v2):>8} | {str(fixed_v2):>8}  {status}")
        if not fixed_v2:
            print(f"      gold_norm={gold_n!r}  v2_pred_norm={v2p_n!r}")
    print(f"\nBug A: {bug_a_fixed}/{len(bug_a)} would match with correct extraction + fixed normalization")

    # Test v3+ cases: ensure no regression
    print()
    print("=" * 100)
    print("V3+ REGRESSION CHECK (must stay correct)")
    print("=" * 100)
    hdr = f"{'idx':>4} | {'gold':>20} | {'v3_pred':>20} | {'buggy':>6} | {'fixed':>6}"
    print(hdr)
    print("-" * len(hdr))
    regressions = 0
    for i, v2c, v3c, gold, v2p, v3p in v3_plus:
        buggy = answers_match_impl(v3p, gold, normalize_answer_buggy)
        fixed = answers_match_impl(v3p, gold, normalize_answer_fixed)
        status = "OK" if fixed else "REGRESSION!"
        if not fixed:
            regressions += 1
        print(f"{i:4d} | {gold:>20} | {v3p:>20} | {str(buggy):>6} | {str(fixed):>6}  {status}")
    print(f"\nRegressions: {regressions}/{len(v3_plus)}")

    # Summary
    print()
    print("=" * 100)
    print("SUMMARY")
    print("=" * 100)
    print(f"Bug B (normalization only): {bug_b_fixed}/{len(bug_b)} fixed")
    print(f"Bug A (extraction + normalization): {bug_a_fixed}/{len(bug_a)} would match if extraction fixed")
    print(f"v3+ regressions: {regressions}/{len(v3_plus)}")
    total_fixable = bug_b_fixed + bug_a_fixed
    print(f"Projected accuracy after fix: ({v3['n_correct']} + {total_fixable}) / {v3['n_total']} = {(v3['n_correct'] + total_fixable) / v3['n_total']:.4f}")


if __name__ == "__main__":
    main()
