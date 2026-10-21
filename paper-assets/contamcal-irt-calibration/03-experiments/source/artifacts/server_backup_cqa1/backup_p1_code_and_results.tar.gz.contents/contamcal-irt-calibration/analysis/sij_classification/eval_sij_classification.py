"""
s_ij Exposure Score Classification Performance Evaluation [SF4]

Evaluates how well RRF exposure scores and individual signals
distinguish treated (injected) vs untreated items.
Ground truth: known injection membership from prepare_sft_data.py.

Output: CSV, JSON, ROC curve PDF per benchmark.
"""

import json
import os
import re
import csv
import numpy as np
from pathlib import Path

try:
    from sklearn.metrics import roc_auc_score, average_precision_score, roc_curve
except ImportError:
    raise ImportError("scikit-learn required: pip install scikit-learn")

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ── Config ──────────────────────────────────────────────
SIGNALS_DIR = "/root/autodl-tmp/exp002/signals"
LABELS_DIR = "/root/autodl-tmp/exp001/sft_data"
BENCHMARKS = ["mmlu", "arc_challenge", "gsm8k"]
ACTIVE_SIGNALS = ["s1_embedding", "s2_minkpp", "s4_selfcritique"]
NEGATE = {"s1_embedding": False, "s2_minkpp": True, "s4_selfcritique": False}
RRF_K = 60
SKIP_PATTERNS = ["DEPRECATED", "old_alpha16", "Instruct"]
EVAL_DOSAGES = [5, 25]

OUTPUT_DIR = Path("/root/contamcal-irt-calibration/analysis/sij_classification")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SIGNAL_DISPLAY = {
    "s1_embedding": "Embedding",
    "s2_minkpp": "Min-K++",
    "s4_selfcritique": "Self-Critique",
    "rrf": "RRF (fused)",
}


def parse_model_info(dirname):
    m_dose = re.search(r'_d(\d{3})', dirname)
    m_seed = re.search(r'_s(\d+)', dirname)
    if not m_dose:
        return None
    dosage = int(m_dose.group(1))
    seed = int(m_seed.group(1)) if m_seed else None
    if dirname.startswith("Llama-3.2-3B"):
        family = "Llama-3.2-3B"
    elif dirname.startswith("Qwen2.5-0.5B"):
        family = "Qwen2.5-0.5B"
    elif dirname.startswith("Qwen2.5-1.5B"):
        family = "Qwen2.5-1.5B"
    elif dirname.startswith("Qwen2.5-3B"):
        family = "Qwen2.5-3B"
    else:
        family = dirname.split("_d")[0]
    is_a32 = "a32" in dirname or "_v3" in dirname
    return {"family": family, "dosage": dosage, "seed": seed, "a32": is_a32, "dirname": dirname}


def should_skip(dirname):
    return any(p in dirname for p in SKIP_PATTERNS)


def select_best_3b(models_3b):
    by_key = {}
    for m in models_3b:
        key = (m["dosage"], m["seed"])
        existing = by_key.get(key)
        if existing is None:
            by_key[key] = m
        elif m["a32"] and not existing["a32"]:
            by_key[key] = m
    return list(by_key.values())


def load_labels(benchmark, dosage):
    fpath = os.path.join(LABELS_DIR, f"contamination_labels_{benchmark}_d{dosage:03d}.json")
    if not os.path.exists(fpath):
        return None
    with open(fpath) as f:
        return json.load(f)


def load_signals(model_dir, benchmark):
    fpath = os.path.join(model_dir, f"signals_merged_{benchmark}.json")
    if not os.path.exists(fpath):
        return None
    with open(fpath) as f:
        return json.load(f)


def get_item_indices(items, benchmark):
    """Extract label-array indices from items, handling both formats."""
    if "item_id" in items[0]:
        prefix = benchmark + "_"
        return [int(it["item_id"][len(prefix):]) if it["item_id"].startswith(prefix)
                else int(it["item_id"].rsplit("_", 1)[-1])
                for it in items]
    elif "index" in items[0]:
        return [it["index"] for it in items]
    else:
        return list(range(len(items)))


def compute_rrf(items):
    n = len(items)
    rrf = np.zeros(n)
    for sig in ACTIVE_SIGNALS:
        v = np.array([it.get(sig, 0.0) or 0.0 for it in items], dtype=float)
        if NEGATE.get(sig, False):
            v = -v
        order = np.argsort(-v)
        ranks = np.empty_like(order, dtype=float)
        ranks[order] = np.arange(1, n + 1)
        rrf += 1.0 / (RRF_K + ranks)
    mn, mx = rrf.min(), rrf.max()
    if mx > mn:
        rrf = (rrf - mn) / (mx - mn)
    return rrf


def oriented_signal(items, sig):
    v = np.array([it.get(sig, 0.0) or 0.0 for it in items], dtype=float)
    if NEGATE.get(sig, False):
        v = -v
    return v


def precision_at_k(y_true, y_scores, k):
    if k <= 0:
        return 0.0
    k = min(k, len(y_true))
    top_k_idx = np.argsort(y_scores)[-k:]
    return float(np.mean(y_true[top_k_idx]))


def evaluate_scores(y_true, y_scores):
    n_pos = int(np.sum(y_true))
    n_total = len(y_true)
    if n_pos == 0 or n_pos == n_total:
        return None
    roc = roc_auc_score(y_true, y_scores)
    pr = average_precision_score(y_true, y_scores)
    p_at_npos = precision_at_k(y_true, y_scores, n_pos)
    return {
        "roc_auc": round(float(roc), 4),
        "pr_auc": round(float(pr), 4),
        "p_at_npos": round(float(p_at_npos), 4),
        "n_pos": n_pos,
        "n_total": n_total,
        "base_rate": round(n_pos / n_total, 4),
    }


def discover_models():
    all_models = []
    for name in sorted(os.listdir(SIGNALS_DIR)):
        dirpath = os.path.join(SIGNALS_DIR, name)
        if not os.path.isdir(dirpath) or should_skip(name):
            continue
        info = parse_model_info(name)
        if info is None or info["dosage"] not in EVAL_DOSAGES:
            continue
        info["path"] = dirpath
        avail = [b for b in BENCHMARKS
                 if os.path.exists(os.path.join(dirpath, f"signals_merged_{b}.json"))]
        if avail:
            info["benchmarks"] = avail
            all_models.append(info)

    non_3b = [m for m in all_models if m["family"] != "Qwen2.5-3B"]
    only_3b = [m for m in all_models if m["family"] == "Qwen2.5-3B"]
    best_3b = select_best_3b(only_3b)
    return non_3b + best_3b


def run_evaluation():
    models = discover_models()
    print(f"Evaluating {len(models)} models")
    for m in models:
        print(f"  {m['dirname']:45s} d={m['dosage']:3d} s={m['seed']} family={m['family']}")

    all_results = []
    roc_data = {}

    for model in models:
        for bench in model["benchmarks"]:
            items = load_signals(model["path"], bench)
            label_data = load_labels(bench, model["dosage"])
            if items is None or label_data is None:
                continue

            labels_arr = label_data["labels"]
            indices = get_item_indices(items, bench)
            y_true = np.array([labels_arr[i] for i in indices], dtype=float)

            n_pos = int(y_true.sum())
            if n_pos == 0 or n_pos == len(y_true):
                continue

            rrf_scores = compute_rrf(items)
            rrf_metrics = evaluate_scores(y_true, rrf_scores)

            row_base = {
                "model": model["dirname"],
                "family": model["family"],
                "dosage": model["dosage"],
                "seed": model["seed"],
                "benchmark": bench,
            }

            if rrf_metrics:
                row = {**row_base, "signal": "rrf", **rrf_metrics}
                all_results.append(row)
                key = (bench, model["dosage"])
                fpr, tpr, _ = roc_curve(y_true, rrf_scores)
                roc_data.setdefault(key, []).append(
                    (model["dirname"], fpr, tpr, rrf_metrics["roc_auc"]))

            for sig in ACTIVE_SIGNALS:
                scores = oriented_signal(items, sig)
                metrics = evaluate_scores(y_true, scores)
                if metrics:
                    row = {**row_base, "signal": sig, **metrics}
                    all_results.append(row)

    return all_results, roc_data


def aggregate_results(all_results):
    from collections import defaultdict
    groups = defaultdict(list)
    for r in all_results:
        key = (r["dosage"], r["benchmark"], r["signal"])
        groups[key].append(r)

    agg = []
    for (dose, bench, sig), rows in sorted(groups.items()):
        roc_aucs = [r["roc_auc"] for r in rows]
        pr_aucs = [r["pr_auc"] for r in rows]
        p_vals = [r["p_at_npos"] for r in rows]
        agg.append({
            "dosage": dose,
            "benchmark": bench,
            "signal": sig,
            "signal_display": SIGNAL_DISPLAY.get(sig, sig),
            "n_models": len(rows),
            "roc_auc_mean": round(float(np.mean(roc_aucs)), 4),
            "roc_auc_std": round(float(np.std(roc_aucs)), 4),
            "pr_auc_mean": round(float(np.mean(pr_aucs)), 4),
            "pr_auc_std": round(float(np.std(pr_aucs)), 4),
            "p_at_npos_mean": round(float(np.mean(p_vals)), 4),
            "p_at_npos_std": round(float(np.std(p_vals)), 4),
            "base_rate": rows[0]["base_rate"],
            "models": [r["model"] for r in rows],
        })
    return agg


def write_csv(agg, path):
    fields = ["dosage", "benchmark", "signal", "signal_display",
              "n_models", "roc_auc_mean", "roc_auc_std",
              "pr_auc_mean", "pr_auc_std",
              "p_at_npos_mean", "p_at_npos_std", "base_rate"]
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for row in agg:
            writer.writerow(row)
    print(f"CSV saved: {path}")


def plot_roc_curves(roc_data):
    for bench in BENCHMARKS:
        doses_with_data = sorted(set(d for (b, d) in roc_data if b == bench))
        if not doses_with_data:
            continue

        fig, axes = plt.subplots(1, len(doses_with_data),
                                 figsize=(5 * len(doses_with_data), 4.5),
                                 squeeze=False)
        fig.suptitle(f"ROC Curves — {bench}", fontsize=13, y=1.02)

        for col, dose in enumerate(doses_with_data):
            ax = axes[0, col]
            key = (bench, dose)
            curves = sorted(roc_data.get(key, []), key=lambda x: -x[3])

            for model_name, fpr, tpr, auc_val in curves:
                short = model_name.replace("Qwen2.5-", "Q").replace("Llama-3.2-", "L")
                ax.plot(fpr, tpr, label=f"{short} ({auc_val:.3f})", alpha=0.8)

            ax.plot([0, 1], [0, 1], 'k--', alpha=0.3)
            ax.set_xlabel("FPR")
            ax.set_ylabel("TPR")
            ax.set_title(f"d={dose:03d}")
            ax.legend(fontsize=6, loc="lower right")
            ax.set_xlim(-0.02, 1.02)
            ax.set_ylim(-0.02, 1.02)
            ax.set_aspect("equal")

        fig.tight_layout()
        outpath = OUTPUT_DIR / f"roc_{bench}.pdf"
        fig.savefig(outpath, bbox_inches="tight", dpi=150)
        plt.close(fig)
        print(f"ROC plot saved: {outpath}")


def main():
    all_results, roc_data = run_evaluation()
    agg = aggregate_results(all_results)

    write_csv(agg, OUTPUT_DIR / "sij_classification_results.csv")

    output = {
        "per_model": all_results,
        "aggregated": agg,
        "config": {
            "signals_dir": SIGNALS_DIR,
            "labels_dir": LABELS_DIR,
            "rrf_k": RRF_K,
            "active_signals": ACTIVE_SIGNALS,
            "negate": NEGATE,
            "eval_dosages": EVAL_DOSAGES,
        }
    }
    json_path = OUTPUT_DIR / "sij_classification_results.json"
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"JSON saved: {json_path}")

    plot_roc_curves(roc_data)

    print("\n" + "=" * 90)
    print("AGGREGATED RESULTS (mean +/- std across models)")
    print("=" * 90)
    print(f"{'Dose':>4s} {'Benchmark':>15s} {'Signal':>16s} {'N':>3s} {'ROC-AUC':>14s} {'PR-AUC':>14s} {'P@Npos':>14s} {'Base':>6s}")
    print("-" * 90)
    for r in agg:
        roc_s = f"{r['roc_auc_mean']:.4f}+/-{r['roc_auc_std']:.4f}"
        pr_s = f"{r['pr_auc_mean']:.4f}+/-{r['pr_auc_std']:.4f}"
        p_s = f"{r['p_at_npos_mean']:.4f}+/-{r['p_at_npos_std']:.4f}"
        print(f"{r['dosage']:>4d} {r['benchmark']:>15s} {r['signal_display']:>16s} {r['n_models']:>3d} {roc_s:>14s} {pr_s:>14s} {p_s:>14s} {r['base_rate']:>6.3f}")


if __name__ == "__main__":
    main()
