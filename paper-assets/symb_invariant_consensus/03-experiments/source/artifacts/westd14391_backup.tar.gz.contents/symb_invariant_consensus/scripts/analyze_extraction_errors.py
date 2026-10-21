"""
Extraction Error Taxonomy for SICA self-extraction.
Analyzes exp033 (Mistral-7B self-extracted) constraint quality,
cross-references with exp031 (Qwen-14B oracle FOL) as ceiling.
"""
import json
import os
import glob
import numpy as np
from collections import defaultdict

BASE = "/root/symb_invariant_consensus"
EXP033_DIR = os.path.join(BASE, "results/exp033_mistral_7b_folio204")
EXP031_FILE = os.path.join(BASE, "results/oracle_folio_regen/exp031_results.json")
OUTPUT_FILE = os.path.join(BASE, "results/extraction_error_taxonomy.json")


def load_exp033():
    with open(os.path.join(EXP033_DIR, "exp033_results.json")) as f:
        results = json.load(f)
    intermediates = {}
    for fpath in sorted(glob.glob(os.path.join(EXP033_DIR, "intermediates", "folio_*.json"))):
        with open(fpath) as f:
            data = json.load(f)
        intermediates[data["problem"]["id"]] = data
    return results, intermediates


def load_exp031():
    with open(EXP031_FILE) as f:
        data = json.load(f)
    return data, {r["problem_id"]: r for r in data["results"]}


def constraint_quality_metrics(sica_result, k=12):
    cs = sica_result["constraints_stats"]
    ms = sica_result["maxsat_stats"]

    total_ext = cs["total_extracted"]
    traces_ok = cs["traces_with_constraints"]
    unique = cs["unique_after_dedup"]
    satisfied = ms["satisfied"]
    excluded = ms["excluded"]
    total_weight = ms["total_weight"]

    scores = sica_result.get("scores", {})
    score_vals = list(scores.values())
    ac = sica_result.get("answer_counts", {})
    total_votes = sum(ac.values())

    if total_votes > 0:
        probs = [v / total_votes for v in ac.values()]
        entropy = -sum(p * np.log2(p) for p in probs if p > 0)
    else:
        entropy = 0.0

    return {
        "extraction_coverage": traces_ok / k if k > 0 else 0,
        "constraint_density": total_ext / traces_ok if traces_ok > 0 else 0,
        "total_extracted": total_ext,
        "unique_after_dedup": unique,
        "dedup_ratio": unique / total_ext if total_ext > 0 else 0,
        "satisfied": satisfied,
        "excluded": excluded,
        "excluded_ratio": excluded / unique if unique > 0 else 0,
        "sat_ratio": satisfied / unique if unique > 0 else 0,
        "avg_weight": total_weight / satisfied if satisfied > 0 else 0,
        "total_weight": total_weight,
        "score_range": (max(score_vals) - min(score_vals)) if len(score_vals) >= 2 else 0,
        "score_std": float(np.std(score_vals)) if len(score_vals) >= 2 else 0,
        "n_candidates": len(score_vals),
        "majority_frac": max(ac.values()) / total_votes if total_votes > 0 else 0,
        "n_answer_types": len(ac),
        "entropy": entropy,
    }


def classify_issues(m):
    issues = []
    if m["extraction_coverage"] < 1.0:
        issues.append("incomplete_extraction")
    if m["unique_after_dedup"] < 10:
        issues.append("low_constraint_count")
    if m["dedup_ratio"] < 0.5:
        issues.append("high_redundancy")
    if m["excluded_ratio"] > 0.10:
        issues.append("high_contradiction")
    if m["score_range"] < 5 and m["n_candidates"] >= 2:
        issues.append("low_discrimination")
    if m["sat_ratio"] > 0.98 and m["unique_after_dedup"] > 5:
        issues.append("trivially_satisfied")
    if m["avg_weight"] < 1.15 and m["satisfied"] > 5:
        issues.append("low_consensus")
    return issues


def fmt(x, decimals=3):
    if isinstance(x, (np.floating, float)):
        return round(float(x), decimals)
    return x


def main():
    exp033_results, exp033_inter = load_exp033()
    exp031_data, exp031_by_id = load_exp031()
    res_by_id = {r["problem_id"]: r for r in exp033_results["results"]}

    problems = []
    for pid in sorted(exp033_inter.keys()):
        idata = exp033_inter[pid]
        rdata = res_by_id.get(pid, {})
        oracle = exp031_by_id.get(pid, {})
        sica = idata["sica_result"]

        gt = rdata.get("ground_truth", idata["problem"]["answer"])
        sica_ans = sica["answer"]
        ac = sica["answer_counts"]
        sc_ans = rdata.get("sc_answer", max(ac, key=ac.get) if ac else "")
        sica_ok = sica_ans == gt
        sc_ok = sc_ans == gt

        if sica_ok and sc_ok:
            group = "both_correct"
        elif sica_ok and not sc_ok:
            group = "sica_wins"
        elif not sica_ok and sc_ok:
            group = "sc_wins"
        else:
            group = "both_wrong"

        overrides_sc = sica_ans != sc_ans

        metrics = constraint_quality_metrics(sica)
        issues = classify_issues(metrics)

        n_premises = len(idata["problem"].get("premises_fol", []))

        problems.append({
            "pid": pid,
            "ground_truth": gt,
            "sica_answer": sica_ans,
            "sc_answer": sc_ans,
            "sica_correct": sica_ok,
            "sc_correct": sc_ok,
            "group": group,
            "overrides_sc": overrides_sc,
            "oracle_correct": oracle.get("oracle_correct"),
            "oracle_answer": oracle.get("oracle_answer"),
            "n_premises_fol": n_premises,
            "metrics": metrics,
            "issues": issues,
        })

    # --- 1. Outcome distribution ---
    groups = defaultdict(list)
    for p in problems:
        groups[p["group"]].append(p)

    outcome_dist = {g: len(ps) for g, ps in groups.items()}

    # --- 2. Error taxonomy ---
    issue_counts = defaultdict(int)
    issue_by_group = defaultdict(lambda: defaultdict(int))
    for p in problems:
        for iss in p["issues"]:
            issue_counts[iss] += 1
            issue_by_group[p["group"]][iss] += 1

    # --- 3. Per-group constraint quality ---
    metric_keys = [
        "extraction_coverage", "constraint_density", "unique_after_dedup",
        "excluded_ratio", "sat_ratio", "dedup_ratio", "avg_weight",
        "score_range", "score_std", "entropy", "majority_frac", "total_weight",
    ]
    group_quality = {}
    for gname in ["sica_wins", "sc_wins", "both_correct", "both_wrong"]:
        gps = groups.get(gname, [])
        if not gps:
            group_quality[gname] = {"n": 0}
            continue
        mlist = [p["metrics"] for p in gps]
        stats = {"n": len(gps)}
        for mk in metric_keys:
            vals = [m[mk] for m in mlist]
            stats[f"avg_{mk}"] = fmt(np.mean(vals))
            stats[f"std_{mk}"] = fmt(np.std(vals))
        stats["issue_distribution"] = dict(issue_by_group.get(gname, {}))
        group_quality[gname] = stats

    # --- 4. Oracle gap analysis ---
    oracle_gap = {
        "oracle_correct_self_wrong": 0,
        "oracle_wrong_self_correct": 0,
        "both_correct": 0,
        "both_wrong": 0,
    }
    oracle_gap_problems = []
    for p in problems:
        oc = p["oracle_correct"]
        if oc is None:
            continue
        sc = p["sica_correct"]
        if oc and sc:
            oracle_gap["both_correct"] += 1
        elif oc and not sc:
            oracle_gap["oracle_correct_self_wrong"] += 1
            oracle_gap_problems.append(p["pid"])
        elif not oc and sc:
            oracle_gap["oracle_wrong_self_correct"] += 1
        else:
            oracle_gap["both_wrong"] += 1

    # Constraint quality for oracle_correct_self_wrong vs rest
    gap_problems = [p for p in problems if p["oracle_correct"] and not p["sica_correct"]]
    nongap = [p for p in problems if p["sica_correct"]]
    gap_quality = {}
    for mk in metric_keys:
        gap_vals = [p["metrics"][mk] for p in gap_problems] if gap_problems else [0]
        nongap_vals = [p["metrics"][mk] for p in nongap] if nongap else [0]
        gap_quality[mk] = {
            "oracle_correct_self_wrong": fmt(np.mean(gap_vals)),
            "self_correct": fmt(np.mean(nongap_vals)),
        }

    # --- 5. Error impact analysis ---
    issue_impact = {}
    for iss, total in issue_counts.items():
        sc_w = issue_by_group.get("sc_wins", {}).get(iss, 0)
        bw = issue_by_group.get("both_wrong", {}).get(iss, 0)
        sw = issue_by_group.get("sica_wins", {}).get(iss, 0)
        bc = issue_by_group.get("both_correct", {}).get(iss, 0)
        harmful = sc_w + bw
        issue_impact[iss] = {
            "total_problems": total,
            "prevalence_pct": fmt(total / len(problems) * 100, 1),
            "in_sica_wins": sw,
            "in_sc_wins": sc_w,
            "in_both_correct": bc,
            "in_both_wrong": bw,
            "harmful_rate": fmt(harmful / total if total > 0 else 0),
        }
    issue_impact_sorted = dict(
        sorted(issue_impact.items(), key=lambda x: -x[1]["harmful_rate"])
    )

    # --- 6. Override analysis ---
    override_correct = sum(1 for p in problems if p["overrides_sc"] and p["sica_correct"] and not p["sc_correct"])
    override_wrong = sum(1 for p in problems if p["overrides_sc"] and not p["sica_correct"] and p["sc_correct"])
    override_both_ok = sum(1 for p in problems if p["overrides_sc"] and p["sica_correct"] and p["sc_correct"])
    override_both_bad = sum(1 for p in problems if p["overrides_sc"] and not p["sica_correct"] and not p["sc_correct"])
    total_overrides = sum(1 for p in problems if p["overrides_sc"])

    # --- 7. Per-answer-type analysis ---
    answer_type_stats = defaultdict(lambda: {
        "n": 0, "sica_correct": 0, "sc_correct": 0,
        "avg_excluded_ratio": [], "avg_score_range": [],
        "avg_unique_constraints": [], "avg_entropy": [],
    })
    for p in problems:
        gt = p["ground_truth"]
        s = answer_type_stats[gt]
        s["n"] += 1
        if p["sica_correct"]:
            s["sica_correct"] += 1
        if p["sc_correct"]:
            s["sc_correct"] += 1
        s["avg_excluded_ratio"].append(p["metrics"]["excluded_ratio"])
        s["avg_score_range"].append(p["metrics"]["score_range"])
        s["avg_unique_constraints"].append(p["metrics"]["unique_after_dedup"])
        s["avg_entropy"].append(p["metrics"]["entropy"])

    answer_type_out = {}
    for atype, s in answer_type_stats.items():
        answer_type_out[atype] = {
            "n": s["n"],
            "sica_acc": fmt(s["sica_correct"] / s["n"]),
            "sc_acc": fmt(s["sc_correct"] / s["n"]),
            "delta_pp": fmt((s["sica_correct"] - s["sc_correct"]) / s["n"] * 100, 1),
            "avg_excluded_ratio": fmt(np.mean(s["avg_excluded_ratio"])),
            "avg_score_range": fmt(np.mean(s["avg_score_range"])),
            "avg_unique_constraints": fmt(np.mean(s["avg_unique_constraints"])),
            "avg_entropy": fmt(np.mean(s["avg_entropy"])),
        }

    # --- 8. FOL complexity vs quality ---
    complexity_buckets = {"simple (<=4)": [], "medium (5-6)": [], "complex (7+)": []}
    for p in problems:
        n = p["n_premises_fol"]
        if n <= 4:
            complexity_buckets["simple (<=4)"].append(p)
        elif n <= 6:
            complexity_buckets["medium (5-6)"].append(p)
        else:
            complexity_buckets["complex (7+)"].append(p)

    complexity_analysis = {}
    for bname, bps in complexity_buckets.items():
        if not bps:
            continue
        complexity_analysis[bname] = {
            "n": len(bps),
            "sica_acc": fmt(sum(p["sica_correct"] for p in bps) / len(bps)),
            "sc_acc": fmt(sum(p["sc_correct"] for p in bps) / len(bps)),
            "avg_excluded_ratio": fmt(np.mean([p["metrics"]["excluded_ratio"] for p in bps])),
            "avg_unique_constraints": fmt(np.mean([p["metrics"]["unique_after_dedup"] for p in bps])),
            "avg_score_range": fmt(np.mean([p["metrics"]["score_range"] for p in bps])),
        }

    # === Build output ===
    output = {
        "summary": {
            "n_problems": len(problems),
            "exp033_sica_acc": fmt(exp033_results["summary"]["sica_accuracy"]),
            "exp033_sc_acc": fmt(exp033_results["summary"]["sc_accuracy"]),
            "exp033_extraction_rate": fmt(exp033_results["summary"]["extraction_rate"]),
            "exp031_oracle_acc": fmt(exp031_data["summary"]["oracle_sica_accuracy"]),
            "exp031_sc_acc": fmt(exp031_data["summary"]["sc_accuracy"]),
            "exp031_self_acc": fmt(exp031_data["summary"]["sica_self_accuracy"]),
        },
        "outcome_distribution": outcome_dist,
        "error_taxonomy_counts": dict(issue_counts),
        "error_impact_analysis": issue_impact_sorted,
        "per_group_constraint_quality": {k: {kk: fmt(vv) if isinstance(vv, (float, np.floating)) else vv for kk, vv in v.items()} for k, v in group_quality.items()},
        "oracle_gap_analysis": oracle_gap,
        "oracle_gap_constraint_quality": gap_quality,
        "override_analysis": {
            "total_overrides": total_overrides,
            "override_rate_pct": fmt(total_overrides / len(problems) * 100, 1),
            "correct_overrides": override_correct,
            "wrong_overrides": override_wrong,
            "both_ok_overrides": override_both_ok,
            "both_bad_overrides": override_both_bad,
            "override_precision": fmt(override_correct / (override_correct + override_wrong) if (override_correct + override_wrong) > 0 else 0),
        },
        "per_answer_type": answer_type_out,
        "fol_complexity_analysis": complexity_analysis,
    }

    with open(OUTPUT_FILE, "w") as f:
        json.dump(output, f, indent=2, default=lambda x: fmt(x) if isinstance(x, (np.floating, np.integer)) else str(x))

    # === Print report ===
    print("=" * 70)
    print("  EXTRACTION ERROR TAXONOMY - exp033 (Mistral-7B, FOLIO-204)")
    print("=" * 70)

    print(f"\n--- Baselines ---")
    print(f"exp033 SICA: {exp033_results['summary']['sica_accuracy']:.1%} | SC: {exp033_results['summary']['sc_accuracy']:.1%}")
    print(f"exp031 Oracle SICA: {exp031_data['summary']['oracle_sica_accuracy']:.1%} | SC: {exp031_data['summary']['sc_accuracy']:.1%}")
    print(f"Oracle ceiling gap: {(exp031_data['summary']['oracle_sica_accuracy'] - exp033_results['summary']['sica_accuracy'])*100:.1f}pp")

    print(f"\n--- Outcome Distribution (n={len(problems)}) ---")
    for g in ["both_correct", "sica_wins", "sc_wins", "both_wrong"]:
        n = outcome_dist.get(g, 0)
        print(f"  {g:15s}: {n:3d} ({n/len(problems)*100:.1f}%)")

    print(f"\n--- Error Taxonomy Distribution ---")
    for iss, cnt in sorted(issue_counts.items(), key=lambda x: -x[1]):
        print(f"  {iss:25s}: {cnt:3d} ({cnt/len(problems)*100:.1f}%)")

    print(f"\n--- Error Impact (sorted by harmful_rate) ---")
    print(f"  {'Issue':<25s} {'Total':>5s} {'Harmful%':>8s} {'SICA+':>5s} {'SC+':>5s} {'BothOK':>6s} {'BothX':>5s}")
    for iss, imp in issue_impact_sorted.items():
        print(f"  {iss:<25s} {imp['total_problems']:5d} {imp['harmful_rate']*100:7.1f}% {imp['in_sica_wins']:5d} {imp['in_sc_wins']:5d} {imp['in_both_correct']:6d} {imp['in_both_wrong']:5d}")

    print(f"\n--- Per-Group Constraint Quality ---")
    print(f"  {'Group':<15s} {'N':>3s} {'Uniq':>6s} {'Excl%':>6s} {'ScRng':>6s} {'AvgW':>6s} {'Entr':>5s}")
    for g in ["sica_wins", "sc_wins", "both_correct", "both_wrong"]:
        gq = group_quality.get(g, {"n": 0})
        if gq["n"] == 0:
            continue
        print(f"  {g:<15s} {gq['n']:3d} "
              f"{gq.get('avg_unique_after_dedup', 0):6.1f} "
              f"{gq.get('avg_excluded_ratio', 0):6.3f} "
              f"{gq.get('avg_score_range', 0):6.1f} "
              f"{gq.get('avg_avg_weight', 0):6.2f} "
              f"{gq.get('avg_entropy', 0):5.2f}")

    print(f"\n--- Oracle Gap (exp031 oracle vs exp033 self-extracted) ---")
    for k, v in oracle_gap.items():
        print(f"  {k:30s}: {v}")

    print(f"\n--- Override Analysis ---")
    oa = output["override_analysis"]
    print(f"  Total overrides: {oa['total_overrides']} ({oa['override_rate_pct']}%)")
    print(f"  Correct: {oa['correct_overrides']}, Wrong: {oa['wrong_overrides']}, Precision: {oa['override_precision']:.1%}")

    print(f"\n--- Per Answer Type ---")
    for at in ["True", "False", "Unknown"]:
        if at in answer_type_out:
            a = answer_type_out[at]
            print(f"  {at:8s}: n={a['n']}, SICA={a['sica_acc']:.1%}, SC={a['sc_acc']:.1%}, delta={a['delta_pp']:+.1f}pp, excl_ratio={a['avg_excluded_ratio']:.3f}")

    print(f"\n--- FOL Complexity ---")
    for bname, bdata in complexity_analysis.items():
        print(f"  {bname:15s}: n={bdata['n']}, SICA={bdata['sica_acc']:.1%}, SC={bdata['sc_acc']:.1%}, excl={bdata['avg_excluded_ratio']:.3f}, uniq={bdata['avg_unique_constraints']:.1f}")

    print(f"\nResults saved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
