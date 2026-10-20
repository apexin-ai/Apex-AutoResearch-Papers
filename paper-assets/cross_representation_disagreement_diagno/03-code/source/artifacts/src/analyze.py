"""
结果分析：分歧率、诊断信息量、错误类型分布、定向修复 vs 盲目重生成对比。
对照 ROADMAP 中的 MVP 通过标准 (C1-C5)。
"""

import json
import argparse
from collections import Counter
from pathlib import Path
from typing import List

from config import RESULTS_DIR


def load_results(path: str) -> List[dict]:
    with open(path) as f:
        return json.load(f)


def analyze(results: List[dict]) -> dict:
    total = len(results)
    errored = [r for r in results if "pipeline_error" in r]
    valid = [r for r in results if "disagreement" in r]

    if not valid:
        return {"error": "no valid results", "total": total, "errored": len(errored)}

    n = len(valid)

    # --- agreement distribution ---
    type_cnt = Counter(r["disagreement"]["agreement_type"] for r in valid)

    disagree_n = type_cnt.get("disagree", 0)
    disagree_rate = disagree_n / n

    # --- diagnostic rate: one-side-correct among disagreements ---
    dis_samples = [r for r in valid if r["disagreement"]["agreement_type"] == "disagree"]
    one_correct = sum(
        1 for r in dis_samples
        if bool(r["disagreement"]["fol_correct"]) != bool(r["disagreement"]["code_correct"])
    )
    diagnostic_rate = one_correct / len(dis_samples) if dis_samples else 0

    fol_right_in_dis = sum(1 for r in dis_samples if r["disagreement"]["fol_correct"])
    code_right_in_dis = sum(1 for r in dis_samples if r["disagreement"]["code_correct"])

    # --- error types ---
    etypes = Counter()
    for r in valid:
        et = r["disagreement"].get("error_type")
        if et:
            etypes[et] += 1

    # --- repair comparison ---
    tgt_att = tgt_ok = bld_att = bld_ok = 0
    for r in valid:
        rep = r.get("repair", {})
        for key in ("fol_targeted", "code_targeted"):
            rounds = rep.get(key, [])
            if rounds:
                tgt_att += 1
                if any(rd["success"] for rd in rounds):
                    tgt_ok += 1
        for key in ("fol_blind", "code_blind"):
            rounds = rep.get(key, [])
            if rounds:
                bld_att += 1
                if any(rd["success"] for rd in rounds):
                    bld_ok += 1

    tgt_rate = tgt_ok / tgt_att if tgt_att else 0
    bld_rate = bld_ok / bld_att if bld_att else 0

    # --- effective disagree rate (both sides executed successfully) ---
    both_exec = [
        r for r in valid
        if r.get("fol_exec", {}).get("verdict") not in ("Error", None)
        and r.get("code_exec", {}).get("verdict") not in ("Error", None)
    ]
    both_exec_n = len(both_exec)
    eff_disagree = sum(
        1 for r in both_exec
        if r.get("fol_exec", {}).get("verdict") != r.get("code_exec", {}).get("verdict")
    )
    eff_disagree_rate = eff_disagree / both_exec_n if both_exec_n else 0

    # --- overall accuracy ---
    fol_acc = sum(
        1 for r in valid if r.get("fol_exec", {}).get("verdict") == r["ground_truth"]
    ) / n
    code_acc = sum(
        1 for r in valid if r.get("code_exec", {}).get("verdict") == r["ground_truth"]
    ) / n
    oracle_acc = sum(
        1 for r in valid
        if r.get("fol_exec", {}).get("verdict") == r["ground_truth"]
        or r.get("code_exec", {}).get("verdict") == r["ground_truth"]
    ) / n

    # --- C5: ground-truth-free localization accuracy ---
    loc_correct = 0
    loc_total = 0
    loc_l1_correct = 0
    loc_l1_total = 0
    loc_l2_correct = 0
    loc_l2_total = 0

    for r in valid:
        at = r["disagreement"]["agreement_type"]
        if at == "agree_correct":
            continue
        loc_total += 1
        actual_side = r["disagreement"].get("error_side")

        if at == "single_error":
            loc_l1_total += 1
            predicted = r["disagreement"].get("error_side")  # crashed side
            fol_c = r["disagreement"].get("fol_correct")
            code_c = r["disagreement"].get("code_correct")
            if fol_c is True or code_c is True:
                loc_l1_correct += 1
                loc_correct += 1

        elif at == "disagree":
            loc_l2_total += 1
            stab = r.get("stability", {})
            predicted = stab.get("predicted_error_side")
            if predicted and predicted != "ambiguous" and predicted == actual_side:
                loc_l2_correct += 1
                loc_correct += 1

    loc_accuracy = loc_correct / loc_total if loc_total else 0

    # --- API cost summary ---
    total_calls = 0
    total_input_tok = 0
    total_output_tok = 0
    total_cost = 0.0
    for r in valid:
        u = r.get("api_usage", {})
        total_calls += u.get("calls", 0)
        total_input_tok += u.get("input_tokens", 0)
        total_output_tok += u.get("output_tokens", 0)
        total_cost += u.get("cost_usd", 0.0)

    return {
        "total": total,
        "pipeline_errors": len(errored),
        "valid": n,
        "agreement_distribution": dict(type_cnt),
        "disagree_rate": round(disagree_rate, 4),
        "disagree_count": disagree_n,
        "effective_disagree": {
            "both_executed": both_exec_n,
            "disagree_count": eff_disagree,
            "rate": round(eff_disagree_rate, 4),
        },
        "diagnostic_rate": round(diagnostic_rate, 4),
        "one_side_correct": one_correct,
        "fol_correct_in_disagree": fol_right_in_dis,
        "code_correct_in_disagree": code_right_in_dis,
        "error_types": dict(etypes),
        "distinct_error_types": len(etypes),
        "repair": {
            "targeted": {"attempts": tgt_att, "successes": tgt_ok, "rate": round(tgt_rate, 4)},
            "blind":    {"attempts": bld_att, "successes": bld_ok, "rate": round(bld_rate, 4)},
            "delta_pp": round((tgt_rate - bld_rate) * 100, 2),
        },
        "accuracy": {
            "fol": round(fol_acc, 4),
            "code": round(code_acc, 4),
            "oracle": round(oracle_acc, 4),
        },
        "localization": {
            "total": loc_total,
            "correct": loc_correct,
            "accuracy": round(loc_accuracy, 4),
            "layer1": {"total": loc_l1_total, "correct": loc_l1_correct},
            "layer2": {"total": loc_l2_total, "correct": loc_l2_correct},
        },
        "api_cost": {
            "total_calls": total_calls,
            "input_tokens": total_input_tok,
            "output_tokens": total_output_tok,
            "total_cost_usd": round(total_cost, 4),
        },
        "mvp": {
            "C1_disagree_ge_10pct": disagree_rate >= 0.10,
            "C2_diagnostic_ge_40pct": diagnostic_rate >= 0.40,
            "C3_error_types_ge_2": len(etypes) >= 2,
            "C4_targeted_advantage_ge_5pp": (tgt_rate - bld_rate) * 100 >= 5,
            "C5_localization_ge_60pct": loc_accuracy >= 0.60,
        },
    }


def print_report(s: dict):
    n = s["valid"]
    print("=" * 65)
    print("Cross-Representation Disagreement Diagnosis  —  MVP Report")
    print("=" * 65)

    print(f"\nDataset: {n} valid / {s['total']} total", end="")
    if s["pipeline_errors"]:
        print(f"  ({s['pipeline_errors']} pipeline errors)")
    else:
        print()

    print("\n— Agreement Distribution —")
    for k, v in s["agreement_distribution"].items():
        print(f"  {k:20s}  {v:4d}  ({v/n*100:5.1f}%)")

    a = s["accuracy"]
    print("\n— Accuracy —")
    print(f"  FOL (Z3)     {a['fol']*100:5.1f}%")
    print(f"  Python code  {a['code']*100:5.1f}%")
    print(f"  Oracle       {a['oracle']*100:5.1f}%")

    print("\n— Disagreement —")
    print(f"  Rate: {s['disagree_rate']*100:.1f}%  ({s['disagree_count']}/{n})")
    ed = s.get("effective_disagree", {})
    print(f"  Effective (both executed): {ed.get('rate',0)*100:.1f}%  ({ed.get('disagree_count',0)}/{ed.get('both_executed',0)})")
    print(f"  Diagnostic (one-side-correct): {s['diagnostic_rate']*100:.1f}%  ({s['one_side_correct']}/{s['disagree_count']})")
    print(f"    FOL correct: {s['fol_correct_in_disagree']}  |  Code correct: {s['code_correct_in_disagree']}")

    print(f"\n— Error Types ({s['distinct_error_types']}) —")
    for k, v in s["error_types"].items():
        print(f"  {k:25s}  {v}")

    r = s["repair"]
    print("\n— Repair —")
    print(f"  Targeted  {r['targeted']['successes']}/{r['targeted']['attempts']}  = {r['targeted']['rate']*100:.1f}%")
    print(f"  Blind     {r['blind']['successes']}/{r['blind']['attempts']}  = {r['blind']['rate']*100:.1f}%")
    print(f"  Delta     {r['delta_pp']:+.1f} pp")

    loc = s.get("localization", {})
    print(f"\n— Localization (ground-truth-free) —")
    print(f"  Overall   {loc.get('correct',0)}/{loc.get('total',0)}  = {loc.get('accuracy',0)*100:.1f}%")
    l1 = loc.get("layer1", {})
    l2 = loc.get("layer2", {})
    print(f"  Layer 1 (exec error)    {l1.get('correct',0)}/{l1.get('total',0)}")
    print(f"  Layer 2 (stability)     {l2.get('correct',0)}/{l2.get('total',0)}")

    c = s.get("api_cost", {})
    print(f"\n— API Cost —")
    print(f"  Calls: {c.get('total_calls', 0)}")
    print(f"  Tokens: {c.get('input_tokens',0):,} in / {c.get('output_tokens',0):,} out")
    print(f"  Cost:  ${c.get('total_cost_usd', 0):.4f}")

    print("\n— MVP Criteria —")
    for k, v in s["mvp"].items():
        print(f"  {k}:  {'PASS' if v else 'FAIL'}")

    passed = all(s["mvp"].values())
    print(f"\n{'MVP PASSED' if passed else 'MVP NOT PASSED'}")
    print("=" * 65)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("results_file", help="path to results JSON")
    ap.add_argument("--save", type=str, default=None)
    args = ap.parse_args()

    data = load_results(args.results_file)
    summary = analyze(data)
    print_report(summary)

    out = args.save or str(RESULTS_DIR / "summary.json")
    with open(out, "w") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    print(f"\nSummary → {out}")
