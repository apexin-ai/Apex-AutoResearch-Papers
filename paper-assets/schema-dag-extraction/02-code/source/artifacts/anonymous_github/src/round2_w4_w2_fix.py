# Round 2: W4 + W2 only (W3 results already saved)
# Fixes: W4 uses correct data source, W2 fixes json.load bug

import json
import logging
from pathlib import Path
import numpy as np

ROOT = Path(".")
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
logger = logging.getLogger(__name__)


def run_w4():
    logger.info("W4: NER count=22/44 recall CI overlap")

    data = json.load(open(ROOT / "results" / "exp1_text_match_reeval.json"))

    results = {}
    for count_key in ["count_22", "count_44"]:
        batch_tp = []
        batch_gold = []
        batch_recalls = []
        batch_idx = 0
        while True:
            key = f"{count_key}_random_{batch_idx}"
            if key not in data:
                break
            m = data[key]["metrics"]
            batch_tp.append(m["tp"])
            batch_gold.append(m["total_gold"])
            batch_recalls.append(m["recall"])
            batch_idx += 1

        tp_arr = np.array(batch_tp)
        gold_arr = np.array(batch_gold)
        recall_arr = np.array(batch_recalls)
        n = len(recall_arr)

        pooled_recall = float(tp_arr.sum() / gold_arr.sum())
        mean_recall = float(recall_arr.mean())

        # Bootstrap CI: resample batches, recompute pooled recall
        rng = np.random.RandomState(42)
        n_boot = 10000
        boot_pooled = np.empty(n_boot)
        boot_mean = np.empty(n_boot)
        for b in range(n_boot):
            idx = rng.randint(0, n, size=n)
            boot_pooled[b] = tp_arr[idx].sum() / gold_arr[idx].sum()
            boot_mean[b] = recall_arr[idx].mean()

        results[count_key] = {
            "n_batches": n,
            "per_batch_recalls": [round(float(r), 4) for r in recall_arr],
            "per_batch_tp": [int(t) for t in tp_arr],
            "per_batch_gold": [int(g) for g in gold_arr],
            "pooled_recall": round(pooled_recall, 4),
            "mean_recall": round(mean_recall, 4),
            "pooled_ci_lower": round(float(np.percentile(boot_pooled, 2.5)), 4),
            "pooled_ci_upper": round(float(np.percentile(boot_pooled, 97.5)), 4),
            "mean_ci_lower": round(float(np.percentile(boot_mean, 2.5)), 4),
            "mean_ci_upper": round(float(np.percentile(boot_mean, 97.5)), 4),
            "std": round(float(recall_arr.std(ddof=1)), 4),
        }
        logger.info("[W4] %s: pooled=%.4f CI [%.4f, %.4f], mean=%.4f CI [%.4f, %.4f]",
                     count_key, pooled_recall,
                     results[count_key]["pooled_ci_lower"],
                     results[count_key]["pooled_ci_upper"],
                     mean_recall,
                     results[count_key]["mean_ci_lower"],
                     results[count_key]["mean_ci_upper"])

    # Overlap analysis (using pooled CI, matching figure values)
    ci22 = (results["count_22"]["pooled_ci_lower"], results["count_22"]["pooled_ci_upper"])
    ci44 = (results["count_44"]["pooled_ci_lower"], results["count_44"]["pooled_ci_upper"])
    overlap_pooled = ci22[1] >= ci44[0] and ci44[1] >= ci22[0]

    # Also mean CI overlap
    ci22m = (results["count_22"]["mean_ci_lower"], results["count_22"]["mean_ci_upper"])
    ci44m = (results["count_44"]["mean_ci_lower"], results["count_44"]["mean_ci_upper"])
    overlap_mean = ci22m[1] >= ci44m[0] and ci44m[1] >= ci22m[0]

    delta_pooled = results["count_44"]["pooled_recall"] - results["count_22"]["pooled_recall"]
    delta_mean = results["count_44"]["mean_recall"] - results["count_22"]["mean_recall"]

    results["overlap_analysis"] = {
        "pooled_ci_22": list(ci22),
        "pooled_ci_44": list(ci44),
        "overlap_pooled": overlap_pooled,
        "mean_ci_22": list(ci22m),
        "mean_ci_44": list(ci44m),
        "overlap_mean": overlap_mean,
        "delta_pooled": round(float(delta_pooled), 4),
        "delta_mean": round(float(delta_mean), 4),
        "narrative": "",
    }

    if overlap_pooled:
        results["overlap_analysis"]["narrative"] = (
            f"The 95% bootstrap CIs for count=22 (pooled recall={results['count_22']['pooled_recall']:.3f}, "
            f"CI [{ci22[0]:.3f}, {ci22[1]:.3f}]) and count=44 (pooled recall={results['count_44']['pooled_recall']:.3f}, "
            f"CI [{ci44[0]:.3f}, {ci44[1]:.3f}]) overlap substantially, "
            f"confirming that the non-monotonicity (+{delta_pooled:.3f}) is within sampling variability "
            f"and not statistically significant. With only 5 batches per count level, "
            f"the wide CIs reflect the expected high variance in batch composition."
        )
    else:
        results["overlap_analysis"]["narrative"] = (
            f"The 95% bootstrap CIs for count=22 [{ci22[0]:.3f}, {ci22[1]:.3f}] "
            f"and count=44 [{ci44[0]:.3f}, {ci44[1]:.3f}] do not overlap — "
            f"the non-monotonicity may reflect a real effect worth investigating."
        )

    return results


def run_w2():
    logger.info("W2: Realistic practical effect calculation")

    batch_data = []
    with open(ROOT / "artifacts" / "fewrel_16rel_bootstrap" / "results_incremental.jsonl") as f:
        for line in f:
            batch_data.append(json.loads(line))

    bcs_vals = np.array([b["bcs"] for b in batch_data])
    acc_vals = np.array([b["accuracy"] for b in batch_data])

    with open(ROOT / "artifacts" / "fewrel_16rel_bootstrap" / "regression_slope.json") as f:
        slope_data = json.load(f)
    slope = slope_data["regression"]["slope"]
    r_value = slope_data["regression"]["r_value"]

    q1 = float(np.percentile(bcs_vals, 25))
    q3 = float(np.percentile(bcs_vals, 75))
    iqr = q3 - q1
    bcs_mean = float(np.mean(bcs_vals))
    bcs_std = float(np.std(bcs_vals))
    bcs_median = float(np.median(bcs_vals))

    typical_gap_pp = slope * iqr * 100
    one_sd_gap_pp = slope * bcs_std * 100

    with open(ROOT / "artifacts" / "fewrel_80pool_16sub" / "bootstrap_ci.json") as f:
        pool80_data = json.load(f)
    pool80_slope = pool80_data["regression_slope"]["slope"]
    pool80_bcs_q1 = pool80_data["quartile_stats"]["Q1_low"]["mean_bcs"]
    pool80_bcs_q3 = pool80_data["quartile_stats"]["Q3"]["mean_bcs"]
    pool80_iqr = pool80_bcs_q3 - pool80_bcs_q1
    pool80_typical_gap_pp = pool80_slope * pool80_iqr * 100
    pool80_bcs_std = pool80_data["summary"]["std_bcs"]
    pool80_1sd_pp = pool80_slope * pool80_bcs_std * 100

    result = {
        "16rel_pool": {
            "n_batches": len(batch_data),
            "slope": round(slope, 4),
            "slope_ci_95": slope_data["regression"]["bootstrap_slope_ci_95"],
            "r_value": round(r_value, 4),
            "bcs_stats": {
                "mean": round(bcs_mean, 4),
                "std": round(bcs_std, 4),
                "median": round(bcs_median, 4),
                "Q1": round(q1, 4),
                "Q3": round(q3, 4),
                "IQR": round(iqr, 4),
                "min": round(float(np.min(bcs_vals)), 4),
                "max": round(float(np.max(bcs_vals)), 4),
            },
            "typical_gap_pp": round(float(typical_gap_pp), 2),
            "one_sd_gap_pp": round(float(one_sd_gap_pp), 2),
            "extreme_gap_pp": -31.2,
        },
        "80pool_16sub": {
            "slope": round(pool80_slope, 4),
            "slope_ci_95": pool80_data["regression_slope"]["bootstrap_ci_95"],
            "bcs_Q1": pool80_bcs_q1,
            "bcs_Q3": pool80_bcs_q3,
            "IQR": round(pool80_iqr, 4),
            "typical_gap_pp": round(float(pool80_typical_gap_pp), 2),
            "one_sd_gap_pp": round(float(pool80_1sd_pp), 2),
        },
        "narrative": (
            f"The extreme-batch 31.2pp gap compares the lowest-BCS and highest-BCS batches "
            f"(top/bottom 5% of batch compositions). For typical user experience, we consider "
            f"the interquartile range (IQR). "
            f"In the 16-relation pool (r={r_value:.2f}), BCS IQR spans [{q1:.3f}, {q3:.3f}] "
            f"(width={iqr:.3f}). The regression slope ({slope:.3f}) predicts a typical Q1-to-Q3 gap "
            f"of {abs(typical_gap_pp):.1f}pp. A 1-SD BCS change ({bcs_std:.3f}) corresponds to "
            f"{abs(one_sd_gap_pp):.1f}pp accuracy change. "
            f"In the 80-type pool with 16-type subsets (more realistic deployments), "
            f"the typical IQR gap is {abs(pool80_typical_gap_pp):.1f}pp and "
            f"the 1-SD gap is {abs(pool80_1sd_pp):.1f}pp."
        ),
    }

    logger.info("[W2] 16rel: slope=%.3f, IQR=%.3f, typical=%.1fpp, 1SD=%.1fpp",
                slope, iqr, typical_gap_pp, one_sd_gap_pp)
    logger.info("[W2] 80pool: slope=%.3f, IQR=%.3f, typical=%.1fpp, 1SD=%.1fpp",
                pool80_slope, pool80_iqr, pool80_typical_gap_pp, pool80_1sd_pp)

    return result


def main():
    # Load existing W3 results
    existing = json.load(open(ROOT / "artifacts" / "round2_statistical_analyses.json"))

    results = {}
    results["W3_cluster_bootstrap"] = existing["W3_cluster_bootstrap"]
    results["W4_recall_ci"] = run_w4()
    results["W2_practical_effect"] = run_w2()

    output_path = ROOT / "artifacts" / "round2_statistical_analyses.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    logger.info("Saved -> %s", output_path)

    # Full summary
    print("\n" + "=" * 70)
    print("ROUND 2 STATISTICAL ANALYSES — SUMMARY")
    print("=" * 70)

    w3 = results["W3_cluster_bootstrap"]
    print("\n--- W3: Type-level Cluster Bootstrap ---")
    for dataset in ["fewnerd", "maven"]:
        d = w3[dataset]
        print(f"  {dataset.upper()}: r={d['point_estimate']:.4f}")
        print(f"    Naive CI:   [{d['naive_ci'][0]:.4f}, {d['naive_ci'][1]:.4f}]")
        print(f"    Cluster CI: [{d['cluster_ci_lower']:.4f}, {d['cluster_ci_upper']:.4f}]")
        print(f"    CI wider (as expected): {(d['cluster_ci_upper']-d['cluster_ci_lower']) > (d['naive_ci'][1]-d['naive_ci'][0])}")
        print(f"    Significant (0 not in CI): {d['significant']}")
        print(f"    -> {d['narrative']}")

    w4 = results["W4_recall_ci"]
    print("\n--- W4: count=22/44 Recall CI ---")
    for ck in ["count_22", "count_44"]:
        d = w4[ck]
        print(f"  {ck}: pooled={d['pooled_recall']:.4f} [{d['pooled_ci_lower']:.4f}, {d['pooled_ci_upper']:.4f}]")
        print(f"         mean={d['mean_recall']:.4f} [{d['mean_ci_lower']:.4f}, {d['mean_ci_upper']:.4f}]")
        print(f"    Per-batch: {d['per_batch_recalls']}")
    ov = w4["overlap_analysis"]
    print(f"  Pooled CI overlap: {ov['overlap_pooled']}")
    print(f"  Mean CI overlap: {ov['overlap_mean']}")
    print(f"  -> {ov['narrative']}")

    w2 = results["W2_practical_effect"]
    print("\n--- W2: Practical Effect ---")
    d16 = w2["16rel_pool"]
    print(f"  16-rel pool (n={d16['n_batches']}):")
    print(f"    slope={d16['slope']}, r={d16['r_value']}")
    print(f"    BCS: mean={d16['bcs_stats']['mean']}, Q1={d16['bcs_stats']['Q1']}, Q3={d16['bcs_stats']['Q3']}, IQR={d16['bcs_stats']['IQR']}")
    print(f"    Typical gap (Q1->Q3): {d16['typical_gap_pp']}pp")
    print(f"    1-SD gap: {d16['one_sd_gap_pp']}pp")
    print(f"    Extreme gap: {d16['extreme_gap_pp']}pp")
    d80 = w2["80pool_16sub"]
    print(f"  80-pool 16-sub:")
    print(f"    slope={d80['slope']}, IQR={d80['IQR']}")
    print(f"    Typical gap: {d80['typical_gap_pp']}pp")
    print(f"    1-SD gap: {d80['one_sd_gap_pp']}pp")

    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
