"""W4: Bootstrap CI for Few-NERD count=22 and count=44 recall.

Input: Per-batch recall data from exp1_reeval_results_v1.json
Output: Bootstrap CIs showing whether count_22 vs count_44 non-monotonicity is within sampling variability
Method: (1) Batch-level bootstrap (B=10,000), (2) Entity-level binomial CI
"""

import json
import logging
from pathlib import Path

import numpy as np
from scipy import stats

ROOT = Path(".")
OUTPUT = ROOT / "scripts" / "d037" / "w4_count_recall_ci_results.json"
B = 10_000
SEED = 42

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
logger = logging.getLogger(__name__)


def load_per_batch_data():
    """Load per-batch recall/tp/gold for count_22 and count_44."""
    with open(ROOT / "results" / "exp1_reeval_results_v1.json") as f:
        data = json.load(f)

    result = {}
    for ck in ["count_22", "count_44"]:
        entries = [(k, v) for k, v in data.items() if v.get("count_key") == ck]
        recalls = [v["text_match"]["recall"] for _, v in entries]
        tps = [v["text_match"]["tp"] for _, v in entries]
        golds = [v["text_match"]["total_gold"] for _, v in entries]
        result[ck] = {
            "recalls": recalls,
            "tps": tps,
            "golds": golds,
            "micro_recall": sum(tps) / sum(golds),
        }
    return result


def batch_bootstrap_ci(recalls, n_boot, seed):
    """Bootstrap CI by resampling batch-level recalls."""
    rng = np.random.RandomState(seed)
    n = len(recalls)
    arr = np.array(recalls)
    boot_means = np.empty(n_boot)
    for i in range(n_boot):
        idx = rng.randint(0, n, size=n)
        boot_means[i] = np.mean(arr[idx])
    return {
        "mean": round(float(np.mean(arr)), 6),
        "ci_lower": round(float(np.percentile(boot_means, 2.5)), 6),
        "ci_upper": round(float(np.percentile(boot_means, 97.5)), 6),
        "std": round(float(np.std(arr, ddof=1)), 6),
        "n_batches": n,
    }


def entity_bootstrap_ci(tps, golds, n_boot, seed):
    """Bootstrap CI by resampling entity-level binary outcomes."""
    rng = np.random.RandomState(seed)
    total_tp = sum(tps)
    total_gold = sum(golds)
    micro_recall = total_tp / total_gold

    outcomes = np.zeros(total_gold)
    outcomes[:total_tp] = 1.0

    boot_recalls = np.empty(n_boot)
    for i in range(n_boot):
        idx = rng.randint(0, total_gold, size=total_gold)
        boot_recalls[i] = np.mean(outcomes[idx])

    return {
        "micro_recall": round(float(micro_recall), 6),
        "ci_lower": round(float(np.percentile(boot_recalls, 2.5)), 6),
        "ci_upper": round(float(np.percentile(boot_recalls, 97.5)), 6),
        "total_tp": int(total_tp),
        "total_gold": int(total_gold),
    }


def wilson_ci(tp, n, alpha=0.05):
    """Wilson score interval for binomial proportion."""
    p = tp / n
    z = stats.norm.ppf(1 - alpha / 2)
    denom = 1 + z**2 / n
    center = (p + z**2 / (2 * n)) / denom
    margin = z * np.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / denom
    return {
        "point": round(float(p), 6),
        "ci_lower": round(float(center - margin), 6),
        "ci_upper": round(float(center + margin), 6),
    }


def main():
    data = load_per_batch_data()
    results = {}

    for ck in ["count_22", "count_44"]:
        d = data[ck]
        logger.info("%s: per-batch recalls=%s", ck, [round(r, 4) for r in d["recalls"]])

        batch_ci = batch_bootstrap_ci(d["recalls"], B, SEED)
        entity_ci = entity_bootstrap_ci(d["tps"], d["golds"], B, SEED)
        wilson = wilson_ci(sum(d["tps"]), sum(d["golds"]))

        results[ck] = {
            "per_batch_recalls": [round(r, 4) for r in d["recalls"]],
            "micro_recall": round(d["micro_recall"], 4),
            "batch_bootstrap_ci": batch_ci,
            "entity_bootstrap_ci": entity_ci,
            "wilson_ci": wilson,
        }
        logger.info("%s: micro=%.4f, batch CI [%.4f, %.4f], entity CI [%.4f, %.4f]",
                    ck, d["micro_recall"],
                    batch_ci["ci_lower"], batch_ci["ci_upper"],
                    entity_ci["ci_lower"], entity_ci["ci_upper"])

    # Overlap analysis
    c22_batch = results["count_22"]["batch_bootstrap_ci"]
    c44_batch = results["count_44"]["batch_bootstrap_ci"]
    c22_entity = results["count_22"]["entity_bootstrap_ci"]
    c44_entity = results["count_44"]["entity_bootstrap_ci"]

    batch_overlap = max(0, min(c22_batch["ci_upper"], c44_batch["ci_upper"]) -
                        max(c22_batch["ci_lower"], c44_batch["ci_lower"]))
    entity_overlap = max(0, min(c22_entity["ci_upper"], c44_entity["ci_upper"]) -
                         max(c22_entity["ci_lower"], c44_entity["ci_lower"]))

    # Permutation test on batch-level means
    rng = np.random.RandomState(SEED)
    r22 = np.array(data["count_22"]["recalls"])
    r44 = np.array(data["count_44"]["recalls"])
    obs_diff = np.mean(r44) - np.mean(r22)
    pooled = np.concatenate([r22, r44])
    n22 = len(r22)
    perm_diffs = np.empty(B)
    for i in range(B):
        rng.shuffle(pooled)
        perm_diffs[i] = np.mean(pooled[n22:]) - np.mean(pooled[:n22])
    p_value = float(np.mean(np.abs(perm_diffs) >= np.abs(obs_diff)))

    results["comparison"] = {
        "count_44_minus_count_22_micro": round(float(data["count_44"]["micro_recall"] - data["count_22"]["micro_recall"]), 4),
        "count_44_minus_count_22_batch_mean": round(float(obs_diff), 4),
        "batch_ci_overlap_width": round(batch_overlap, 4),
        "entity_ci_overlap_width": round(entity_overlap, 4),
        "permutation_test_p_value": round(p_value, 4),
        "batch_cis_overlap": batch_overlap > 0,
        "entity_cis_overlap": entity_overlap > 0,
    }

    with open(OUTPUT, "w") as f:
        json.dump(results, f, indent=2)
    logger.info("Saved -> %s", OUTPUT)

    print("\n" + "=" * 70)
    print("W4: COUNT RECALL CI RESULTS (B=%d)" % B)
    print("=" * 70)
    for ck in ["count_22", "count_44"]:
        r = results[ck]
        bc = r["batch_bootstrap_ci"]
        ec = r["entity_bootstrap_ci"]
        wc = r["wilson_ci"]
        print(f"\n{ck}:")
        print(f"  micro recall = {r['micro_recall']:.4f}")
        print(f"  per-batch recalls: {r['per_batch_recalls']}")
        print(f"  Batch bootstrap CI:  [{bc['ci_lower']:.4f}, {bc['ci_upper']:.4f}]")
        print(f"  Entity bootstrap CI: [{ec['ci_lower']:.4f}, {ec['ci_upper']:.4f}]")
        print(f"  Wilson CI:           [{wc['ci_lower']:.4f}, {wc['ci_upper']:.4f}]")
    comp = results["comparison"]
    print(f"\nDifference (count_44 - count_22):")
    print(f"  Micro: {comp['count_44_minus_count_22_micro']:.4f}")
    print(f"  Batch mean: {comp['count_44_minus_count_22_batch_mean']:.4f}")
    print(f"  Batch CIs overlap: {comp['batch_cis_overlap']} (width={comp['batch_ci_overlap_width']:.4f})")
    print(f"  Entity CIs overlap: {comp['entity_cis_overlap']} (width={comp['entity_ci_overlap_width']:.4f})")
    print(f"  Permutation test p-value: {comp['permutation_test_p_value']:.4f}")
    print("=" * 70)


if __name__ == "__main__":
    main()
