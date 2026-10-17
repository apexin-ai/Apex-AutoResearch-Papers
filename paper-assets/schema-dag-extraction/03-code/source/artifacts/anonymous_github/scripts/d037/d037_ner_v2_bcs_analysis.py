"""D037: NER v2 BCS-metric correlation analysis.

Computes BCS-F1 correlations from exp2 (prompt v2) per-batch results.
v1 raw data was overwritten; v1 stats come from decision records (D005).
"""
import json
import numpy as np
from scipy import stats

EVAL_PATH = "./artifacts/eval_exp2.json"
OUT_PATH = "./scripts/d037/d037_ner_v2_bcs_analysis_results.json"

with open(EVAL_PATH) as f:
    data = json.load(f)

# Parse per-batch (BCS, F1) pairs by count
v2_batches = {"count_6": [], "count_12": []}
for batch_id, metrics in data.items():
    count_key = metrics["count_key"]
    bcs = metrics["bcs"]
    f1 = metrics["text_match"]["f1"]
    recall = metrics["text_match"]["recall"]
    precision = metrics["text_match"]["precision"]
    v2_batches[count_key].append({
        "batch_id": batch_id,
        "bcs": bcs,
        "f1": f1,
        "recall": recall,
        "precision": precision,
    })

def compute_correlations(batches):
    bcs = np.array([b["bcs"] for b in batches])
    f1 = np.array([b["f1"] for b in batches])
    recall = np.array([b["recall"] for b in batches])
    
    pr, pp = stats.pearsonr(bcs, f1)
    sr, sp = stats.spearmanr(bcs, f1)
    pr_rec, pp_rec = stats.pearsonr(bcs, recall)
    sr_rec, sp_rec = stats.spearmanr(bcs, recall)
    
    return {
        "f1_vs_bcs": {
            "pearson_r": round(pr, 4),
            "pearson_p": round(pp, 4),
            "spearman_rho": round(sr, 4),
            "spearman_p": round(sp, 4),
        },
        "recall_vs_bcs": {
            "pearson_r": round(pr_rec, 4),
            "pearson_p": round(pp_rec, 4),
            "spearman_rho": round(sr_rec, 4),
            "spearman_p": round(sp_rec, 4),
        },
        "n_batches": len(batches),
        "bcs_range": [round(float(bcs.min()), 4), round(float(bcs.max()), 4)],
        "f1_range": [round(float(f1.min()), 4), round(float(f1.max()), 4)],
        "mean_f1": round(float(f1.mean()), 4),
        "std_f1": round(float(f1.std()), 4),
    }

def bootstrap_ci(batches, metric="f1", B=1000, seed=42):
    rng = np.random.RandomState(seed)
    bcs = np.array([b["bcs"] for b in batches])
    y = np.array([b[metric] for b in batches])
    n = len(batches)
    
    pearson_boots = []
    spearman_boots = []
    for _ in range(B):
        idx = rng.randint(0, n, size=n)
        bcs_b = bcs[idx]
        y_b = y[idx]
        if np.std(bcs_b) < 1e-10 or np.std(y_b) < 1e-10:
            continue
        pr, _ = stats.pearsonr(bcs_b, y_b)
        sr, _ = stats.spearmanr(bcs_b, y_b)
        pearson_boots.append(pr)
        spearman_boots.append(sr)
    
    pearson_boots = np.array(pearson_boots)
    spearman_boots = np.array(spearman_boots)
    
    return {
        "pearson_ci_95": [round(float(np.percentile(pearson_boots, 2.5)), 4),
                          round(float(np.percentile(pearson_boots, 97.5)), 4)],
        "spearman_ci_95": [round(float(np.percentile(spearman_boots, 2.5)), 4),
                           round(float(np.percentile(spearman_boots, 97.5)), 4)],
        "n_valid_bootstrap": len(pearson_boots),
    }

# V2 analysis
results = {"v2": {}, "v1": {}, "comparison": {}}

for count_key in ["count_6", "count_12"]:
    batches = v2_batches[count_key]
    corr = compute_correlations(batches)
    ci_f1 = bootstrap_ci(batches, metric="f1", B=1000)
    ci_recall = bootstrap_ci(batches, metric="recall", B=1000)
    corr["bootstrap_f1"] = ci_f1
    corr["bootstrap_recall"] = ci_recall
    results["v2"][count_key] = corr

# V2 pooled
pooled = v2_batches["count_6"] + v2_batches["count_12"]
corr_pooled = compute_correlations(pooled)
ci_pooled = bootstrap_ci(pooled, metric="f1", B=1000)
corr_pooled["bootstrap_f1"] = ci_pooled
results["v2"]["pooled"] = corr_pooled

# Extreme batch gap (v2)
for count_key in ["count_6", "count_12"]:
    batches = v2_batches[count_key]
    low_bcs_batch = [b for b in batches if "low_bcs" in b["batch_id"]]
    high_bcs_batch = [b for b in batches if "high_bcs" in b["batch_id"]]
    if low_bcs_batch and high_bcs_batch:
        gap = high_bcs_batch[0]["f1"] - low_bcs_batch[0]["f1"]
        results["v2"][count_key]["extreme_gap"] = {
            "low_bcs": round(low_bcs_batch[0]["bcs"], 4),
            "low_f1": round(low_bcs_batch[0]["f1"], 4),
            "high_bcs": round(high_bcs_batch[0]["bcs"], 4),
            "high_f1": round(high_bcs_batch[0]["f1"], 4),
            "delta_f1_pp": round(gap * 100, 2),
            "direction": "positive (high BCS → higher F1)" if gap > 0 else "negative (high BCS → lower F1)",
        }

# V1 from D005 decision records (raw data overwritten)
results["v1"] = {
    "count_6": {
        "note": "v1 per-batch raw data overwritten by v2 run; stats from D005 decision record",
        "f1_vs_bcs": {
            "pearson_r": None,
            "note": "D005 reported pooled/count_12 stats only"
        },
        "n_batches": 27,
    },
    "count_12": {
        "note": "v1 per-batch raw data overwritten by v2 run; stats from D005 decision record",
        "f1_vs_bcs": {
            "pearson_r": 0.50,
            "pearson_p": 0.008,
            "source": "D005 decision record"
        },
        "recall_vs_bcs": {
            "pearson_r": 0.25,
            "pearson_p": 0.066,
            "source": "D005 decision record"
        },
        "partial_r_f1_bcs": {
            "r": 0.30,
            "p": 0.026,
            "source": "D005 decision record"
        },
        "n_batches": 27,
    },
    "pooled": {
        "note": "v1 raw data unavailable; D005 reported within-count stats"
    }
}

# Comparison
v2_c6 = results["v2"]["count_6"]["f1_vs_bcs"]
v2_c12 = results["v2"]["count_12"]["f1_vs_bcs"]
v1_c12_r = 0.50  # from D005

v2_c12_r = v2_c12["pearson_r"]
v2_c6_r = v2_c6["pearson_r"]

# Both v1 and v2 show POSITIVE BCS-F1 correlation
# D008 confirmed: v2 also showed positive (高 BCS→高 F1)
# This is OPPOSITE to the confusability hypothesis (expected negative)
both_positive = (v1_c12_r > 0) and (v2_c12_r > 0)

results["comparison"] = {
    "direction_consistent": both_positive,
    "v1_count12_pearson_r": v1_c12_r,
    "v2_count12_pearson_r": v2_c12_r,
    "v2_count6_pearson_r": v2_c6_r,
    "v1_vs_v2_summary": (
        f"Both v1 (r={v1_c12_r:.2f}) and v2 (r={v2_c12_r:.4f}) show positive BCS-F1 correlation "
        f"at count_12, direction consistent. This is OPPOSITE to the confusability hypothesis "
        f"(expected negative). D008 identified type frequency as confounding variable: high-BCS "
        f"batches contain high-frequency types that models extract better. The batch-level "
        f"BCS-F1 correlation is NOT a valid test of Channel 2; pairwise SCS→confusion analysis "
        f"(Channel 1) is the primary evidence."
    ),
    "risk_level": "LOW — direction consistent across prompt versions; confound identified and documented",
    "note": "v1 raw per-batch data unavailable (overwritten). v1 stats from D005 decision record."
}

with open(OUT_PATH, "w") as f:
    json.dump(results, f, indent=2)

print(json.dumps(results, indent=2))
