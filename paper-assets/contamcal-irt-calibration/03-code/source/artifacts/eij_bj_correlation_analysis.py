"""Compute correlation between per-item RRF exposure (tau_j) and item difficulty (b_j)."""

import json
import csv
import numpy as np
from scipy import stats

BENCHMARKS = ["mmlu", "arc_challenge", "gsm8k"]
RRF_AGG = "/root/autodl-tmp/exp003/rrf_full_3scales/exposure_aggregated.json"
IRT_DATA = "/root/contamcal-irt-calibration/analysis/irt_data"

with open(RRF_AGG) as f:
    rrf_agg = json.load(f)

results = {}

for bench in BENCHMARKS:
    meta_path = f"{IRT_DATA}/{bench}/item_metadata.csv"
    try:
        with open(meta_path) as f:
            reader = csv.DictReader(f)
            meta = list(reader)
    except FileNotFoundError:
        print(f"SKIP {bench}: no item_metadata.csv")
        continue

    diff_baseline = np.array([float(row["difficulty_baseline"]) for row in meta])
    n_items_meta = len(diff_baseline)

    if bench not in rrf_agg:
        print(f"SKIP {bench}: not in RRF aggregated")
        continue
    tau = np.array(rrf_agg[bench])
    n_items_rrf = len(tau)

    n = min(n_items_meta, n_items_rrf)
    tau_n = tau[:n]
    diff_n = diff_baseline[:n]

    p_clipped = np.clip(diff_n, 0.01, 0.99)
    b_proxy = -np.log(p_clipped / (1 - p_clipped))

    print(f"\n{'='*60}")
    print(f"Benchmark: {bench}")
    print(f"  N_items (matched): {n}")
    print(f"  tau range: [{tau_n.min():.4f}, {tau_n.max():.4f}], mean={tau_n.mean():.4f}, std={tau_n.std():.4f}")
    print(f"  diff_baseline range: [{diff_n.min():.4f}, {diff_n.max():.4f}], mean={diff_n.mean():.4f}")
    print(f"  b_proxy range: [{b_proxy.min():.4f}, {b_proxy.max():.4f}], mean={b_proxy.mean():.4f}")

    r_pearson, p_pearson = stats.pearsonr(tau_n, diff_n)
    r_spearman, p_spearman = stats.spearmanr(tau_n, diff_n)
    r_pearson_b, p_pearson_b = stats.pearsonr(tau_n, b_proxy)
    r_spearman_b, p_spearman_b = stats.spearmanr(tau_n, b_proxy)

    print(f"\n  [ALL {n} items] tau vs p(correct):")
    print(f"    Pearson  r={r_pearson:.4f}, p={p_pearson:.2e}")
    print(f"    Spearman rho={r_spearman:.4f}, p={p_spearman:.2e}")
    print(f"  [ALL {n} items] tau vs b_proxy (-logit(p)):")
    print(f"    Pearson  r={r_pearson_b:.4f}, p={p_pearson_b:.2e}")
    print(f"    Spearman rho={r_spearman_b:.4f}, p={p_spearman_b:.2e}")

    top300_idx = np.argsort(tau_n)[-300:]
    tau_300 = tau_n[top300_idx]
    diff_300 = diff_n[top300_idx]
    b_300 = b_proxy[top300_idx]

    r_p300, p_p300 = stats.pearsonr(tau_300, diff_300)
    r_s300, p_s300 = stats.spearmanr(tau_300, diff_300)
    r_pb300, p_pb300 = stats.pearsonr(tau_300, b_300)
    r_sb300, p_sb300 = stats.spearmanr(tau_300, b_300)

    print(f"\n  [TOP-300 RRF items] tau vs p(correct):")
    print(f"    Pearson  r={r_p300:.4f}, p={p_p300:.2e}")
    print(f"    Spearman rho={r_s300:.4f}, p={p_s300:.2e}")
    print(f"  [TOP-300 RRF items] tau vs b_proxy (-logit(p)):")
    print(f"    Pearson  r={r_pb300:.4f}, p={p_pb300:.2e}")
    print(f"    Spearman rho={r_sb300:.4f}, p={p_sb300:.2e}")

    print(f"\n  [TOP-300] p(correct) mean={diff_300.mean():.4f} vs ALL mean={diff_n.mean():.4f}")
    print(f"  [TOP-300] b_proxy mean={b_300.mean():.4f} vs ALL mean={b_proxy.mean():.4f}")

    results[bench] = {
        "n_all": int(n),
        "n_top300": 300,
        "all_items": {
            "tau_vs_p": {"pearson_r": round(r_pearson, 4), "pearson_p": f"{p_pearson:.2e}",
                         "spearman_rho": round(r_spearman, 4), "spearman_p": f"{p_spearman:.2e}"},
            "tau_vs_b": {"pearson_r": round(r_pearson_b, 4), "pearson_p": f"{p_pearson_b:.2e}",
                         "spearman_rho": round(r_spearman_b, 4), "spearman_p": f"{p_spearman_b:.2e}"},
        },
        "top300_rrf": {
            "tau_vs_p": {"pearson_r": round(r_p300, 4), "pearson_p": f"{p_p300:.2e}",
                         "spearman_rho": round(r_s300, 4), "spearman_p": f"{p_s300:.2e}"},
            "tau_vs_b": {"pearson_r": round(r_pb300, 4), "pearson_p": f"{p_pb300:.2e}",
                         "spearman_rho": round(r_sb300, 4), "spearman_p": f"{p_sb300:.2e}"},
            "p_correct_mean_top300": round(float(diff_300.mean()), 4),
            "p_correct_mean_all": round(float(diff_n.mean()), 4),
        },
    }

# Per-model RRF exposure variation
print(f"\n\n{'='*60}")
print("ADDITIONAL: Per-model RRF exposure variation check")

rrf_permodel = "/root/autodl-tmp/exp003/rrf_full_3scales/exposure_scores.json"
with open(rrf_permodel) as f:
    rrf_pm = json.load(f)

for bench in BENCHMARKS:
    model_taus = {}
    for model_name, model_data in rrf_pm.items():
        if bench in model_data:
            scores = model_data[bench]
            if isinstance(scores, dict) and "exposure_scores" in scores:
                scores = scores["exposure_scores"]
            model_taus[model_name] = np.array(scores)

    if not model_taus:
        continue

    models = list(model_taus.keys())
    n_items = min(len(v) for v in model_taus.values())
    tau_matrix = np.vstack([model_taus[m][:n_items] for m in models])

    cross_model_corrs = []
    for i in range(len(models)):
        for j in range(i + 1, len(models)):
            r, _ = stats.pearsonr(tau_matrix[i], tau_matrix[j])
            cross_model_corrs.append(r)

    print(f"\n  {bench}: {len(models)} base models, {n_items} items")
    print(f"    Cross-model tau corr: mean={np.mean(cross_model_corrs):.4f}, min={np.min(cross_model_corrs):.4f}, max={np.max(cross_model_corrs):.4f}")

    tau_mean = tau_matrix.mean(axis=0)
    tau_std = tau_matrix.std(axis=0)
    print(f"    Mean tau: mean={tau_mean.mean():.4f}, std={tau_mean.std():.4f}")
    print(f"    Within-item tau std (across models): mean={tau_std.mean():.4f}")

    # Correlation of per-model mean tau with difficulty
    meta_path = f"{IRT_DATA}/{bench}/item_metadata.csv"
    try:
        with open(meta_path) as f:
            reader = csv.DictReader(f)
            meta = list(reader)
        diff_baseline = np.array([float(row["difficulty_baseline"]) for row in meta])
        n_match = min(n_items, len(diff_baseline))
        r, p = stats.spearmanr(tau_mean[:n_match], diff_baseline[:n_match])
        print(f"    Mean tau vs diff_baseline: Spearman rho={r:.4f}, p={p:.2e}")
    except Exception:
        pass

print("\n\nDone.")

with open("/tmp/eij_bj_corr_results.json", "w") as f:
    json.dump(results, f, indent=2)
print("Results saved to /tmp/eij_bj_corr_results.json")
