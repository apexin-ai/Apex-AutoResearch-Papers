"""Per-type F1 vs BCS analysis, controlling for type frequency.

For each entity type:
  - F1: averaged across all batches containing that type (text_match eval)
  - mean_BCS: mean cosine similarity with all other types (from embeddings)
  - frequency: gold entity count in test set

Then: Pearson, Spearman, partial correlation (controlling freq), quartile comparison.
"""
import json
import sys
import logging
from pathlib import Path
from collections import defaultdict

import numpy as np
import torch
from scipy import stats

sys.path.insert(0, str(Path(__file__).parent))
from few_nerd_utils import load_few_nerd

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

ROOT = Path(".")


def text_match(pred, gold, source_text=""):
    if pred.get("type") != gold["type"]:
        return False
    pt = pred.get("text", "").strip()
    gt = gold.get("text", "").strip()
    if not pt or not gt:
        return False
    if source_text and pt.lower() not in source_text.lower():
        return False
    pl, gl = pt.lower(), gt.lower()
    return pl == gl or pl in gl or gl in pl


def compute_per_type_metrics(predictions, samples, batch_types):
    """Compute TP/FP/FN per type for a single batch."""
    type_stats = {t: {"tp": 0, "fp": 0, "fn": 0} for t in batch_types}

    pred_by_sample = defaultdict(list)
    for p in predictions:
        pred_by_sample[p["sample_id"]].append(p)

    for sid, pred_entries in pred_by_sample.items():
        if sid >= len(samples):
            continue
        sample = samples[sid]
        source_text = sample.get("text", "")
        gold_entities = [e for e in sample["entities"] if e["type"] in batch_types]
        pred_entities = pred_entries[0].get("predictions", [])
        pred_entities = [p for p in pred_entities if p.get("type") in batch_types]

        matched_gold = set()
        matched_pred = set()
        for pi, pred in enumerate(pred_entities):
            for gi, gold in enumerate(gold_entities):
                if gi not in matched_gold and text_match(pred, gold, source_text):
                    matched_gold.add(gi)
                    matched_pred.add(pi)
                    t = gold["type"]
                    type_stats[t]["tp"] += 1
                    break

        for pi, pred in enumerate(pred_entities):
            if pi not in matched_pred:
                t = pred.get("type")
                if t in type_stats:
                    type_stats[t]["fp"] += 1

        for gi, gold in enumerate(gold_entities):
            if gi not in matched_gold:
                type_stats[gold["type"]]["fn"] += 1

    result = {}
    for t, s in type_stats.items():
        tp, fp, fn = s["tp"], s["fp"], s["fn"]
        p = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        r = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
        result[t] = {"precision": p, "recall": r, "f1": f1, "tp": tp, "fp": fp, "fn": fn,
                      "gold_count": tp + fn}
    return result


def compute_mean_bcs(embeddings):
    """For each type, compute mean cosine similarity with all other types."""
    types = list(embeddings.keys())
    embs = torch.stack([embeddings[t].float() for t in types])
    embs_norm = embs / embs.norm(dim=1, keepdim=True)
    sim = embs_norm @ embs_norm.T
    n = len(types)
    mean_bcs = {}
    for i, t in enumerate(types):
        sims = [sim[i, j].item() for j in range(n) if j != i]
        mean_bcs[t] = np.mean(sims)
    return mean_bcs


def partial_corr(x, y, z):
    """Partial Pearson correlation of x and y, controlling for z."""
    x, y, z = np.array(x), np.array(y), np.array(z)
    rx = stats.pearsonr(x, z)[0]
    ry = stats.pearsonr(y, z)[0]
    res_x = x - rx * z / np.std(z) * np.std(x) if np.std(z) > 0 else x
    res_y = y - ry * z / np.std(z) * np.std(y) if np.std(z) > 0 else y
    # Proper partial correlation
    from numpy.linalg import lstsq
    Z = np.column_stack([z, np.ones(len(z))])
    res_x = x - Z @ lstsq(Z, x, rcond=None)[0]
    res_y = y - Z @ lstsq(Z, y, rcond=None)[0]
    r, p = stats.pearsonr(res_x, res_y)
    return r, p


def main():
    logger.info("Loading predictions...")
    with open(ROOT / "artifacts" / "predictions_exp2.json") as f:
        raw_preds = json.load(f)

    logger.info("Loading Few-NERD test set...")
    samples = load_few_nerd(split="test")

    logger.info("Loading type embeddings...")
    embeddings = torch.load(ROOT / "artifacts" / "type_embeddings.pt", weights_only=False)

    # Group predictions by batch
    batches = defaultdict(list)
    batch_meta = {}
    for p in raw_preds:
        bid = p["batch_id"]
        batches[bid].append(p)
        if bid not in batch_meta:
            batch_meta[bid] = {
                "batch_types": set(p["batch_types"]),
                "batch_bcs": p.get("batch_bcs", 0.0),
            }

    # Compute per-type F1 within each batch
    logger.info("Computing per-type metrics across %d batches...", len(batches))
    type_f1_across_batches = defaultdict(list)
    type_tp_total = defaultdict(int)
    type_fp_total = defaultdict(int)
    type_fn_total = defaultdict(int)

    for bid, preds in batches.items():
        bt = batch_meta[bid]["batch_types"]
        per_type = compute_per_type_metrics(preds, samples, bt)
        for t, m in per_type.items():
            type_f1_across_batches[t].append(m["f1"])
            type_tp_total[t] += m["tp"]
            type_fp_total[t] += m["fp"]
            type_fn_total[t] += m["fn"]

    # Compute global per-type frequency (gold count in test set)
    type_freq = defaultdict(int)
    for sample in samples:
        for e in sample["entities"]:
            type_freq[e["type"]] += 1

    # Compute mean BCS
    mean_bcs = compute_mean_bcs(embeddings)

    # Build analysis table
    rows = []
    for t in sorted(type_f1_across_batches.keys()):
        if t not in mean_bcs:
            continue
        tp = type_tp_total[t]
        fp = type_fp_total[t]
        fn = type_fn_total[t]
        micro_p = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        micro_r = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        micro_f1 = 2 * micro_p * micro_r / (micro_p + micro_r) if (micro_p + micro_r) > 0 else 0.0
        freq = type_freq.get(t, 0)
        rows.append({
            "type": t,
            "mean_bcs": mean_bcs[t],
            "micro_f1": micro_f1,
            "mean_f1": np.mean(type_f1_across_batches[t]),
            "frequency": freq,
            "num_batches": len(type_f1_across_batches[t]),
            "tp": tp, "fp": fp, "fn": fn,
        })

    # Filter: gold count >= 5
    rows_filtered = [r for r in rows if r["frequency"] >= 5]
    logger.info("Types total: %d, after freq>=5 filter: %d", len(rows), len(rows_filtered))

    # Print table
    print(f"\n{'Type':<35} {'mean_BCS':>8} {'micro_F1':>8} {'mean_F1':>8} {'freq':>6} {'batches':>7}")
    print("-" * 80)
    for r in sorted(rows_filtered, key=lambda x: x["mean_bcs"], reverse=True):
        print(f"{r['type']:<35} {r['mean_bcs']:8.4f} {r['micro_f1']:8.4f} {r['mean_f1']:8.4f} {r['frequency']:6d} {r['num_batches']:7d}")

    # Extract arrays for correlation
    bcs_arr = np.array([r["mean_bcs"] for r in rows_filtered])
    f1_arr = np.array([r["micro_f1"] for r in rows_filtered])
    freq_arr = np.array([r["frequency"] for r in rows_filtered])
    log_freq = np.log1p(freq_arr)

    # Correlations
    pearson_r, pearson_p = stats.pearsonr(bcs_arr, f1_arr)
    spearman_r, spearman_p = stats.spearmanr(bcs_arr, f1_arr)
    partial_r, partial_p = partial_corr(bcs_arr, f1_arr, log_freq)

    # Also with mean_f1
    mean_f1_arr = np.array([r["mean_f1"] for r in rows_filtered])
    pearson_r2, pearson_p2 = stats.pearsonr(bcs_arr, mean_f1_arr)
    spearman_r2, spearman_p2 = stats.spearmanr(bcs_arr, mean_f1_arr)
    partial_r2, partial_p2 = partial_corr(bcs_arr, mean_f1_arr, log_freq)

    # Quartile comparison
    q25 = np.percentile(bcs_arr, 25)
    q75 = np.percentile(bcs_arr, 75)
    low_bcs = [r for r in rows_filtered if r["mean_bcs"] <= q25]
    high_bcs = [r for r in rows_filtered if r["mean_bcs"] >= q75]
    low_avg_f1 = np.mean([r["micro_f1"] for r in low_bcs])
    high_avg_f1 = np.mean([r["micro_f1"] for r in high_bcs])
    low_avg_freq = np.mean([r["frequency"] for r in low_bcs])
    high_avg_freq = np.mean([r["frequency"] for r in high_bcs])

    print("\n" + "=" * 60)
    print("CORRELATION RESULTS (micro_F1)")
    print(f"  Pearson  r={pearson_r:.4f}, p={pearson_p:.4f}")
    print(f"  Spearman ρ={spearman_r:.4f}, p={spearman_p:.4f}")
    print(f"  Partial  r={partial_r:.4f}, p={partial_p:.4f} (controlling log-freq)")
    print()
    print("CORRELATION RESULTS (mean_F1)")
    print(f"  Pearson  r={pearson_r2:.4f}, p={pearson_p2:.4f}")
    print(f"  Spearman ρ={spearman_r2:.4f}, p={spearman_p2:.4f}")
    print(f"  Partial  r={partial_r2:.4f}, p={partial_p2:.4f} (controlling log-freq)")
    print()
    print("QUARTILE COMPARISON")
    print(f"  Low BCS  (≤{q25:.4f}): n={len(low_bcs)}, avg_F1={low_avg_f1:.4f}, avg_freq={low_avg_freq:.1f}")
    print(f"  High BCS (≥{q75:.4f}): n={len(high_bcs)}, avg_F1={high_avg_f1:.4f}, avg_freq={high_avg_freq:.1f}")
    print(f"  Δ F1 (high-low) = {high_avg_f1 - low_avg_f1:.4f}")

    # Freq-BCS correlation (to show confound)
    freq_bcs_r, freq_bcs_p = stats.pearsonr(bcs_arr, log_freq)
    freq_f1_r, freq_f1_p = stats.pearsonr(log_freq, f1_arr)
    print()
    print("CONFOUND CHECK")
    print(f"  r(mean_BCS, log_freq) = {freq_bcs_r:.4f}, p={freq_bcs_p:.4f}")
    print(f"  r(log_freq, micro_F1) = {freq_f1_r:.4f}, p={freq_f1_p:.4f}")

    # Scatter plot
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # Panel 1: BCS vs F1 colored by freq
    sc = axes[0].scatter(bcs_arr, f1_arr, c=log_freq, cmap="viridis", s=40, alpha=0.8)
    plt.colorbar(sc, ax=axes[0], label="log(freq+1)")
    axes[0].set_xlabel("Mean BCS")
    axes[0].set_ylabel("Micro F1")
    axes[0].set_title(f"Per-type BCS vs F1\nr={pearson_r:.3f}, p={pearson_p:.3f}")
    z = np.polyfit(bcs_arr, f1_arr, 1)
    x_line = np.linspace(bcs_arr.min(), bcs_arr.max(), 100)
    axes[0].plot(x_line, np.polyval(z, x_line), "r--", alpha=0.5)

    # Panel 2: BCS vs F1 (mean_F1)
    sc2 = axes[1].scatter(bcs_arr, mean_f1_arr, c=log_freq, cmap="viridis", s=40, alpha=0.8)
    plt.colorbar(sc2, ax=axes[1], label="log(freq+1)")
    axes[1].set_xlabel("Mean BCS")
    axes[1].set_ylabel("Mean F1 (across batches)")
    axes[1].set_title(f"Per-type BCS vs Mean F1\nr={pearson_r2:.3f}, p={pearson_p2:.3f}")
    z2 = np.polyfit(bcs_arr, mean_f1_arr, 1)
    axes[1].plot(x_line, np.polyval(z2, x_line), "r--", alpha=0.5)

    # Panel 3: Residuals after controlling for freq
    from numpy.linalg import lstsq as np_lstsq
    Z = np.column_stack([log_freq, np.ones(len(log_freq))])
    res_bcs = bcs_arr - Z @ np_lstsq(Z, bcs_arr, rcond=None)[0]
    res_f1 = f1_arr - Z @ np_lstsq(Z, f1_arr, rcond=None)[0]
    axes[2].scatter(res_bcs, res_f1, c="steelblue", s=40, alpha=0.8)
    axes[2].set_xlabel("BCS residual (freq removed)")
    axes[2].set_ylabel("F1 residual (freq removed)")
    axes[2].set_title(f"Partial correlation\nr={partial_r:.3f}, p={partial_p:.3f}")
    z3 = np.polyfit(res_bcs, res_f1, 1)
    x3 = np.linspace(res_bcs.min(), res_bcs.max(), 100)
    axes[2].plot(x3, np.polyval(z3, x3), "r--", alpha=0.5)

    plt.tight_layout()
    out_fig = ROOT / "results" / "per_type_bcs_f1_scatter.png"
    plt.savefig(out_fig, dpi=150, bbox_inches="tight")
    logger.info("Saved figure to %s", out_fig)

    # Save JSON
    output = {
        "n_types_total": len(rows),
        "n_types_filtered": len(rows_filtered),
        "min_freq_threshold": 5,
        "correlations": {
            "micro_f1": {
                "pearson": {"r": pearson_r, "p": pearson_p},
                "spearman": {"rho": spearman_r, "p": spearman_p},
                "partial_controlling_log_freq": {"r": partial_r, "p": partial_p},
            },
            "mean_f1": {
                "pearson": {"r": pearson_r2, "p": pearson_p2},
                "spearman": {"rho": spearman_r2, "p": spearman_p2},
                "partial_controlling_log_freq": {"r": partial_r2, "p": partial_p2},
            },
        },
        "quartile_comparison": {
            "low_bcs_threshold": q25,
            "high_bcs_threshold": q75,
            "low_bcs": {"n": len(low_bcs), "avg_f1": low_avg_f1, "avg_freq": low_avg_freq},
            "high_bcs": {"n": len(high_bcs), "avg_f1": high_avg_f1, "avg_freq": high_avg_freq},
            "delta_f1": high_avg_f1 - low_avg_f1,
        },
        "confound_check": {
            "r_bcs_logfreq": {"r": freq_bcs_r, "p": freq_bcs_p},
            "r_logfreq_f1": {"r": freq_f1_r, "p": freq_f1_p},
        },
        "per_type_table": [{k: (float(v) if isinstance(v, (np.floating, float)) else v) for k, v in r.items()} for r in sorted(rows_filtered, key=lambda x: x["mean_bcs"], reverse=True)],
    }
    out_json = ROOT / "results" / "per_type_analysis.json"
    with open(out_json, "w") as f:
        json.dump(output, f, indent=2)
    logger.info("Saved JSON to %s", out_json)


if __name__ == "__main__":
    main()
