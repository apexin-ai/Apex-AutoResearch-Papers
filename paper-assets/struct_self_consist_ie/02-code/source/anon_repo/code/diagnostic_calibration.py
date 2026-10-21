#!/root/miniconda3/bin/python3.12
"""Diagnostic-Calibrated Deployment Framework evaluation.

Computes 3 diagnostic indicators + LP selection delta for each dataset-model
combination, then fits a linear regression to predict deployment benefit.
"""

import json
import os
import sys
import numpy as np
from scipy.stats import spearmanr
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, "/root/autodl-tmp/struct_self_consist_ie/code")
from unified_metrics import compute_entity_f1, compute_degeneracy

BASE = "/root/autodl-tmp/struct_self_consist_ie/output"
OUT_DIR = os.path.join(BASE, "diagnostic_calibration")
os.makedirs(OUT_DIR, exist_ok=True)

COMBOS = {
    "SciERC-Qwen8B": {
        "path": f"{BASE}/exp_012_rerun_1024/samples.jsonl",
        "dataset": "SciERC", "model": "Qwen3-8B", "subtask": "ner",
    },
    "CoNLL-Qwen8B": {
        "path": f"{BASE}/exp_002_conll_n16_r1024/samples.jsonl",
        "dataset": "CoNLL", "model": "Qwen3-8B", "subtask": "ner",
    },
    "FewNERD-Qwen8B": {
        "path": f"{BASE}/exp_021_inference/samples.jsonl",
        "dataset": "Few-NERD", "model": "Qwen3-8B", "subtask": "ner",
    },
    "CoNLL-LLaMA": {
        "path": f"{BASE}/exp_017_llama_conll_n16_r1024/samples.jsonl",
        "dataset": "CoNLL", "model": "LLaMA3.1-8B", "subtask": "ner",
    },
    "SciERC-LLaMA": {
        "path": f"{BASE}/exp_007_llama_n16_r1024/samples.jsonl",
        "dataset": "SciERC", "model": "LLaMA3.1-8B", "subtask": "ner",
    },
    "SciERC-Qwen4B": {
        "path": f"{BASE}/exp_qwen3_4b_scierc_scs_inference/samples.jsonl",
        "dataset": "SciERC", "model": "Qwen3-4B", "subtask": "ner",
    },
    "CoNLL-Qwen4B": {
        "path": f"{BASE}/exp_qwen3_4b_conll_scs_inference_v2/samples.jsonl",
        "dataset": "CoNLL", "model": "Qwen3-4B", "subtask": "ner",
    },
}


def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def compute_diagnostics(data, subtask="ner"):
    """Compute 3 diagnostic indicators + LP selection delta (macro-averaged F1)."""
    gold_filtered = [inst for inst in data if len(inst["gold"].get("entities", [])) > 0]
    n = len(gold_filtered)

    greedy_f1s = []
    lp_sel_f1s = []
    n_constant_f1 = 0
    within_rhos = []
    lp_ranges = []

    for inst in gold_filtered:
        samples = inst["samples"]
        gold = inst["gold"]
        greedy = inst.get("greedy", samples[0])
        logprobs = inst.get("logprobs", [s.get("mean_logprob", 0) for s in samples])

        sample_f1s = [compute_entity_f1(s.get("entities", []), gold.get("entities", [])) for s in samples]
        greedy_f1 = compute_entity_f1(greedy.get("entities", []), gold.get("entities", []))
        greedy_f1s.append(greedy_f1)

        best_idx = int(np.argmax(logprobs))
        lp_sel_f1s.append(sample_f1s[best_idx])

        if compute_degeneracy(sample_f1s):
            n_constant_f1 += 1

        if (not compute_degeneracy(sample_f1s) and
                len(set(round(lp, 10) for lp in logprobs)) > 1):
            rho, _ = spearmanr(logprobs, sample_f1s)
            if not np.isnan(rho):
                within_rhos.append(rho)

        lp_range = max(logprobs) - min(logprobs)
        lp_ranges.append(lp_range)

    g_f1 = float(np.mean(greedy_f1s))
    lp_f1 = float(np.mean(lp_sel_f1s))

    return {
        "n_instances": n,
        "n_samples": len(gold_filtered[0]["samples"]) if gold_filtered else 0,
        "degeneracy_rate": n_constant_f1 / n * 100 if n > 0 else 0,
        "within_instance_lp_f1_rho": float(np.mean(within_rhos)) if within_rhos else 0.0,
        "n_rho_computable": len(within_rhos),
        "lp_range_median": float(np.median(lp_ranges)) if lp_ranges else 0.0,
        "lp_range_mean": float(np.mean(lp_ranges)) if lp_ranges else 0.0,
        "greedy_f1": g_f1,
        "lp_sel_f1": lp_f1,
        "lp_delta_pp": (lp_f1 - g_f1) * 100,
    }


def run_analysis():
    results = {}
    print("=" * 70)
    print("Diagnostic-Calibrated Deployment Framework")
    print("=" * 70)

    for name, cfg in COMBOS.items():
        path = cfg["path"]
        if not os.path.exists(path):
            print(f"  SKIP {name}: {path} not found")
            continue
        print(f"\n  Processing {name}...", end=" ", flush=True)
        data = load_data(path)
        diag = compute_diagnostics(data, subtask=cfg["subtask"])
        diag["dataset"] = cfg["dataset"]
        diag["model"] = cfg["model"]
        results[name] = diag
        print(f"n={diag['n_instances']}, degen={diag['degeneracy_rate']:.1f}%, "
              f"rho={diag['within_instance_lp_f1_rho']:.3f}, "
              f"lp_range={diag['lp_range_median']:.4f}, "
              f"delta={diag['lp_delta_pp']:+.3f}pp")

    print(f"\n{'=' * 70}")
    print(f"Total data points: {len(results)}")

    names = list(results.keys())
    X = np.array([[results[n]["degeneracy_rate"],
                    results[n]["within_instance_lp_f1_rho"],
                    results[n]["lp_range_median"]] for n in names])
    y = np.array([results[n]["lp_delta_pp"] for n in names])

    feature_names = ["degeneracy_rate", "within_lp_f1_rho", "lp_range_median"]

    reg = LinearRegression().fit(X, y)
    y_pred = reg.predict(X)
    r2 = r2_score(y, y_pred)
    mae = mean_absolute_error(y, y_pred)
    print(f"\n--- 3-indicator Linear Regression ---")
    print(f"  R² = {r2:.4f}, MAE = {mae:.4f} pp")
    for fn, c in zip(feature_names, reg.coef_):
        print(f"  coef({fn}) = {c:.4f}")
    print(f"  intercept = {reg.intercept_:.4f}")

    loo_preds = []
    loo_actual = []
    loo_names = []
    for i in range(len(names)):
        X_train = np.delete(X, i, axis=0)
        y_train = np.delete(y, i)
        reg_loo = LinearRegression().fit(X_train, y_train)
        pred_i = reg_loo.predict(X[i:i+1])[0]
        loo_preds.append(pred_i)
        loo_actual.append(y[i])
        loo_names.append(names[i])

    loo_preds = np.array(loo_preds)
    loo_actual = np.array(loo_actual)
    loo_mae = mean_absolute_error(loo_actual, loo_preds)
    loo_ss_res = np.sum((loo_actual - loo_preds) ** 2)
    loo_ss_tot = np.sum((loo_actual - np.mean(loo_actual)) ** 2)
    loo_r2 = 1 - loo_ss_res / loo_ss_tot if loo_ss_tot > 0 else float("nan")
    sign_match = sum(1 for a, p in zip(loo_actual, loo_preds) if (a > 0) == (p > 0))
    print(f"\n--- LOO Cross-Validation ---")
    print(f"  LOO R² = {loo_r2:.4f}, LOO MAE = {loo_mae:.4f} pp")
    print(f"  Sign accuracy = {sign_match}/{len(names)} ({sign_match/len(names):.1%})")
    for n, a, p in zip(loo_names, loo_actual, loo_preds):
        sign = "ok" if (a > 0) == (p > 0) else "MISS"
        print(f"  {n:20s}: actual={a:+.3f}, pred={p:+.3f} [{sign}]")

    # --- Individual indicator correlations ---
    print(f"\n--- Individual Indicator Correlations ---")
    for j, fn in enumerate(feature_names):
        rho_val, p_val = spearmanr(X[:, j], y)
        print(f"  Spearman({fn}, delta): rho={rho_val:+.3f}, p={p_val:.4f}")

    # --- Threshold rule exploration ---
    print(f"\n--- Threshold Rule Exploration ---")
    threshold_combos = [
        (20, 0.2, "degen<20% & rho>0.2"),
        (20, 0.3, "degen<20% & rho>0.3"),
        (30, 0.2, "degen<30% & rho>0.2"),
        (30, 0.3, "degen<30% & rho>0.3"),
        (50, 0.1, "degen<50% & rho>0.1"),
        (50, 0.2, "degen<50% & rho>0.2"),
        (50, 0.3, "degen<50% & rho>0.3"),
        (20, 0.15, "degen<20% & rho>0.15"),
    ]

    best_rule = None
    best_accuracy = 0
    threshold_results = []

    for degen_thresh, rho_thresh, label in threshold_combos:
        correct = 0
        total = len(names)
        tp = fp = tn = fn_ = 0
        for n in names:
            r = results[n]
            pred_positive = (r["degeneracy_rate"] < degen_thresh and
                           r["within_instance_lp_f1_rho"] > rho_thresh)
            actual_positive = r["lp_delta_pp"] > 0
            if pred_positive == actual_positive:
                correct += 1
            if pred_positive and actual_positive:
                tp += 1
            elif pred_positive and not actual_positive:
                fp += 1
            elif not pred_positive and actual_positive:
                fn_ += 1
            else:
                tn += 1
        acc = correct / total
        rule_result = {
            "rule": label,
            "accuracy": acc,
            "tp": tp, "fp": fp, "tn": tn, "fn": fn_,
        }
        threshold_results.append(rule_result)
        print(f"  {label:30s}: acc={acc:.1%} (TP={tp} FP={fp} TN={tn} FN={fn_})")
        if acc > best_accuracy:
            best_accuracy = acc
            best_rule = label

    print(f"  Best rule: {best_rule} ({best_accuracy:.1%})")

    # --- Scatter plots ---
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))

    marker_map = {"Qwen3-8B": "o", "LLaMA3.1-8B": "s", "Qwen3-4B": "^"}
    color_map = {"SciERC": "#e41a1c", "CoNLL": "#377eb8", "Few-NERD": "#4daf4a"}

    def plot_scatter(ax, x_vals, y_vals, xlabel, title):
        for i, n in enumerate(names):
            r = results[n]
            ax.scatter(x_vals[i], y_vals[i],
                      marker=marker_map.get(r["model"], "o"),
                      c=color_map.get(r["dataset"], "gray"),
                      s=100, zorder=5, edgecolors="black", linewidth=0.5)
            ax.annotate(n, (x_vals[i], y_vals[i]),
                       fontsize=6, ha="center", va="bottom",
                       xytext=(0, 6), textcoords="offset points",
                       rotation=15)
        ax.axhline(0, color="gray", linestyle="--", alpha=0.5)
        ax.set_xlabel(xlabel, fontsize=10)
        ax.set_ylabel("LP Selection Delta (pp)", fontsize=10)
        ax.set_title(title, fontsize=11)

    x_degen = [results[n]["degeneracy_rate"] for n in names]
    x_rho = [results[n]["within_instance_lp_f1_rho"] for n in names]
    x_lp = [results[n]["lp_range_median"] for n in names]
    y_vals = [results[n]["lp_delta_pp"] for n in names]

    plot_scatter(axes[0, 0], x_degen, y_vals,
                "Degeneracy Rate (%)", "Degeneracy vs LP Delta")
    plot_scatter(axes[0, 1], x_rho, y_vals,
                "Within-Instance LP-F1 rho (mean)", "LP-F1 Correlation vs LP Delta")
    plot_scatter(axes[0, 2], x_lp, y_vals,
                "LP Range (median)", "LP Range vs LP Delta")

    axes[1, 0].scatter(y_pred, y, c="steelblue", s=80, edgecolors="black", linewidth=0.5)
    for i, n in enumerate(names):
        axes[1, 0].annotate(n, (y_pred[i], y[i]), fontsize=6,
                           ha="center", va="bottom", xytext=(0, 5),
                           textcoords="offset points", rotation=15)
    lims = [min(min(y_pred), min(y)) - 0.3, max(max(y_pred), max(y)) + 0.3]
    axes[1, 0].plot(lims, lims, "k--", alpha=0.4)
    axes[1, 0].set_xlabel("Predicted Delta (pp)", fontsize=10)
    axes[1, 0].set_ylabel("Actual Delta (pp)", fontsize=10)
    axes[1, 0].set_title(f"Regression Fit (R²={r2:.3f})", fontsize=11)

    axes[1, 1].scatter(loo_preds, loo_actual, c="darkorange", s=80,
                       edgecolors="black", linewidth=0.5)
    for i, n in enumerate(loo_names):
        axes[1, 1].annotate(n, (loo_preds[i], loo_actual[i]), fontsize=6,
                           ha="center", va="bottom", xytext=(0, 5),
                           textcoords="offset points", rotation=15)
    lims2 = [min(min(loo_preds), min(loo_actual)) - 0.3,
             max(max(loo_preds), max(loo_actual)) + 0.3]
    axes[1, 1].plot(lims2, lims2, "k--", alpha=0.4)
    axes[1, 1].set_xlabel("LOO Predicted Delta (pp)", fontsize=10)
    axes[1, 1].set_ylabel("Actual Delta (pp)", fontsize=10)
    axes[1, 1].set_title(f"LOO CV (R²={loo_r2:.3f}, MAE={loo_mae:.3f})", fontsize=11)

    from matplotlib.lines import Line2D
    legend_elements = []
    for ds, c in color_map.items():
        legend_elements.append(Line2D([0], [0], marker="o", color="w",
                                      markerfacecolor=c, markersize=8, label=ds))
    for model, m in marker_map.items():
        legend_elements.append(Line2D([0], [0], marker=m, color="w",
                                      markerfacecolor="gray", markersize=8, label=model))
    axes[1, 2].legend(handles=legend_elements, loc="center", fontsize=10)
    axes[1, 2].axis("off")
    axes[1, 2].set_title("Legend", fontsize=11)

    plt.tight_layout()
    fig_path = os.path.join(OUT_DIR, "diagnostic_calibration_scatter.png")
    plt.savefig(fig_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"\n  Saved scatter plots to {fig_path}")

    # --- Save results JSON ---
    output = {
        "data_points": results,
        "regression": {
            "features": feature_names,
            "coefficients": reg.coef_.tolist(),
            "intercept": float(reg.intercept_),
            "r2": r2,
            "mae": mae,
        },
        "loo_cv": {
            "r2": loo_r2,
            "mae": loo_mae,
            "sign_accuracy": sign_match / len(names),
            "predictions": {n: {"actual": float(a), "predicted": float(p)}
                           for n, a, p in zip(loo_names, loo_actual, loo_preds)},
        },
        "individual_correlations": {},
        "threshold_rules": threshold_results,
        "best_threshold_rule": best_rule,
    }

    for j, fn in enumerate(feature_names):
        rho_val, p_val = spearmanr(X[:, j], y)
        output["individual_correlations"][fn] = {
            "spearman_rho": float(rho_val), "p_value": float(p_val)}

    json_path = os.path.join(BASE, "diagnostic_calibration_results.json")
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"  Saved results JSON to {json_path}")

    # --- Markdown report ---
    md_lines = [
        "# Diagnostic-Calibrated Deployment Framework",
        "",
        "## Data Points (macro-averaged F1, gold-filtered, span-based)",
        "",
        "| Combination | Dataset | Model | N_inst | N_samp | Degen% | rho(LP,F1) | LP Range | Greedy F1 | LP Sel F1 | Delta (pp) |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for n in names:
        r = results[n]
        md_lines.append(
            f"| {n} | {r['dataset']} | {r['model']} | {r['n_instances']} | "
            f"{r['n_samples']} | {r['degeneracy_rate']:.1f} | "
            f"{r['within_instance_lp_f1_rho']:.3f} | "
            f"{r['lp_range_median']:.4f} | {r['greedy_f1']:.4f} | "
            f"{r['lp_sel_f1']:.4f} | {r['lp_delta_pp']:+.3f} |"
        )

    md_lines += [
        "",
        "## Individual Indicator Correlations with LP Delta",
        "",
        "| Indicator | Spearman rho | p-value |",
        "|---|---|---|",
    ]
    for j, fn in enumerate(feature_names):
        rho_val, p_val = spearmanr(X[:, j], y)
        md_lines.append(f"| {fn} | {rho_val:+.3f} | {p_val:.4f} |")

    md_lines += [
        "",
        "## 3-Indicator Linear Regression",
        "",
        f"- **R²** = {r2:.4f}",
        f"- **MAE** = {mae:.4f} pp",
        f"- Coefficients: degen={reg.coef_[0]:.4f}, rho={reg.coef_[1]:.4f}, lp_range={reg.coef_[2]:.4f}",
        f"- Intercept: {reg.intercept_:.4f}",
        "",
        "## LOO Cross-Validation",
        "",
        f"- **LOO R²** = {loo_r2:.4f}",
        f"- **LOO MAE** = {loo_mae:.4f} pp",
        f"- **Sign accuracy** = {sign_match}/{len(names)} ({sign_match/len(names):.1%})",
        "",
        "| Combination | Actual Delta | LOO Predicted | Sign Match |",
        "|---|---|---|---|",
    ]
    for n, a, p in zip(loo_names, loo_actual, loo_preds):
        sign = "Yes" if (a > 0) == (p > 0) else "No"
        md_lines.append(f"| {n} | {a:+.3f} | {p:+.3f} | {sign} |")

    md_lines += [
        "",
        "## Threshold Rules",
        "",
        "| Rule | Accuracy | TP | FP | TN | FN |",
        "|---|---|---|---|---|---|",
    ]
    for tr in threshold_results:
        md_lines.append(
            f"| {tr['rule']} | {tr['accuracy']:.1%} | "
            f"{tr['tp']} | {tr['fp']} | {tr['tn']} | {tr['fn']} |"
        )
    md_lines.append(f"\n**Best rule**: {best_rule} ({best_accuracy:.1%})")

    md_lines += [
        "",
        "## Statistical Limitations",
        "",
        f"Only {len(results)} data points. The 3-feature regression is likely overfit "
        "(7 points, 4 parameters). LOO CV R² and sign accuracy are more reliable "
        "indicators of predictive power than in-sample R².",
    ]

    md_path = os.path.join(OUT_DIR, "diagnostic_calibration_report.md")
    with open(md_path, "w") as f:
        f.write("\n".join(md_lines) + "\n")
    print(f"  Saved markdown report to {md_path}")

    return output


if __name__ == "__main__":
    run_analysis()
