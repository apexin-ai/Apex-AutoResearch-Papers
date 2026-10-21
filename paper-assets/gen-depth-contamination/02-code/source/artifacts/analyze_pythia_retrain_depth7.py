#!/usr/bin/env python3
"""Analyze Pythia retrain-chain depth 7 results and compare with Qwen."""
import json
import math
import sys
from pathlib import Path

RESULTS_ROOT = Path("/root/autodl-tmp/gen-depth-contamination/results")
PYTHIA_DIR = RESULTS_ROOT / "exp_pythia_retrain_depth7"
QWEN_DIR = RESULTS_ROOT / "exp_qwen_retrain_chain_ext"
THETA = 0.60
N_FOLDS = 5
OUT_DIR = RESULTS_ROOT / "analysis_pythia_retrain_depth7"


def load_experiment(exp_dir: Path) -> dict:
    auc_path = exp_dir / "pairwise_auc.json"
    jsd_path = exp_dir / "jsd.json"
    summary_path = exp_dir / "summary.json"

    with open(auc_path) as f:
        auc_data = json.load(f)
    with open(jsd_path) as f:
        jsd_data = json.load(f)

    summary = None
    if summary_path.exists():
        with open(summary_path) as f:
            summary = json.load(f)

    pairs = list(auc_data["mean"].keys())
    result = {"pairs": pairs, "auc_mean": {}, "per_fold": {}, "ci": {}, "jsd": {}}

    for p in pairs:
        result["auc_mean"][p] = auc_data["mean"][p]
        result["jsd"][p] = jsd_data.get(p)

        if "per_fold" in auc_data and p in auc_data["per_fold"]:
            folds = auc_data["per_fold"][p]
            result["per_fold"][p] = folds
            n = len(folds)
            mean = sum(folds) / n
            std = math.sqrt(sum((x - mean) ** 2 for x in folds) / (n - 1))
            margin = 1.96 * std / math.sqrt(n)
            result["ci"][p] = {
                "mean": round(mean, 4),
                "std": round(std, 4),
                "ci_lo": round(mean - margin, 4),
                "ci_hi": round(mean + margin, 4),
            }
        elif "ci" in auc_data and p in auc_data["ci"]:
            ci = auc_data["ci"][p]
            result["ci"][p] = {
                "mean": ci["mean"],
                "std": ci["std"],
                "ci_lo": ci["ci_95"][0],
                "ci_hi": ci["ci_95"][1],
            }

    return result


def determine_kstar(exp: dict, theta: float) -> int:
    k = 0
    for p in exp["pairs"]:
        ci = exp["ci"].get(p, {})
        ci_lo = ci.get("ci_lo", exp["auc_mean"][p])
        if ci_lo > theta:
            k += 1
        else:
            break
    return k


def determine_kstar_mean(exp: dict, theta: float) -> int:
    k = 0
    for p in exp["pairs"]:
        if exp["auc_mean"][p] > theta:
            k += 1
        else:
            break
    return k


def print_summary(name: str, exp: dict, kstar: int, kstar_mean: int):
    print(f"\n{'=' * 60}")
    print(f"  {name}")
    print(f"{'=' * 60}")
    print(f"  {'Pair':<8} {'AUC':>7} {'95% CI':>17} {'JSD':>9}")
    print(f"  {'-' * 50}")
    for p in exp["pairs"]:
        ci = exp["ci"].get(p, {})
        ci_str = f"[{ci.get('ci_lo', '?'):.4f}, {ci.get('ci_hi', '?'):.4f}]"
        jsd_val = exp["jsd"].get(p)
        jsd_str = f"{jsd_val:.6f}" if jsd_val is not None else "N/A"
        marker = " *" if exp["auc_mean"][p] <= THETA else ""
        print(f"  {p:<8} {exp['auc_mean'][p]:>7.4f} {ci_str:>17} {jsd_str:>9}{marker}")
    print(f"\n  K* (mean > {THETA}):    {kstar_mean}")
    print(f"  K* (CI_lo > {THETA}):   {kstar}")
    print(f"  (* = below theta)")


def build_comparison_table(pythia: dict, qwen: dict) -> str:
    all_pairs = list(dict.fromkeys(pythia["pairs"] + qwen["pairs"]))
    lines = []
    lines.append(f"\n{'=' * 72}")
    lines.append(f"  Side-by-side Comparison: Pythia-1.4B vs Qwen2.5-1.5B")
    lines.append(f"{'=' * 72}")
    header = f"  {'Pair':<8} {'Pythia AUC':>11} {'Pythia CI':>17} {'Qwen AUC':>10} {'Qwen CI':>17}"
    lines.append(header)
    lines.append(f"  {'-' * 66}")
    for p in all_pairs:
        p_auc = pythia["auc_mean"].get(p)
        q_auc = qwen["auc_mean"].get(p)
        p_ci = pythia["ci"].get(p, {})
        q_ci = qwen["ci"].get(p, {})
        p_auc_str = f"{p_auc:.4f}" if p_auc is not None else "N/A"
        q_auc_str = f"{q_auc:.4f}" if q_auc is not None else "N/A"
        p_ci_str = f"[{p_ci['ci_lo']:.4f},{p_ci['ci_hi']:.4f}]" if p_ci else "N/A"
        q_ci_str = f"[{q_ci['ci_lo']:.4f},{q_ci['ci_hi']:.4f}]" if q_ci else "N/A"
        lines.append(f"  {p:<8} {p_auc_str:>11} {p_ci_str:>17} {q_auc_str:>10} {q_ci_str:>17}")
    return "\n".join(lines)


def generate_latex(pythia: dict, qwen: dict, pythia_kstar: int, qwen_kstar: int) -> str:
    all_pairs = list(dict.fromkeys(pythia["pairs"] + qwen["pairs"]))
    lines = []
    lines.append(r"\begin{table}[t]")
    lines.append(r"\centering")
    lines.append(r"\caption{Retrain-chain pairwise AUC: Pythia-1.4B vs Qwen2.5-1.5B (depth 0--7, $\theta=0.60$).}")
    lines.append(r"\label{tab:retrain-pythia-qwen}")
    lines.append(r"\small")
    lines.append(r"\begin{tabular}{l cc cc}")
    lines.append(r"\toprule")
    lines.append(r"& \multicolumn{2}{c}{\textbf{Pythia-1.4B}} & \multicolumn{2}{c}{\textbf{Qwen2.5-1.5B}} \\")
    lines.append(r"\cmidrule(lr){2-3} \cmidrule(lr){4-5}")
    lines.append(r"Depth Pair & AUC & 95\% CI & AUC & 95\% CI \\")
    lines.append(r"\midrule")

    for p in all_pairs:
        p_auc = pythia["auc_mean"].get(p)
        q_auc = qwen["auc_mean"].get(p)
        p_ci = pythia["ci"].get(p, {})
        q_ci = qwen["ci"].get(p, {})

        label = p.replace("v", " vs ")

        p_auc_str = f"{p_auc:.4f}" if p_auc is not None else "--"
        q_auc_str = f"{q_auc:.4f}" if q_auc is not None else "--"
        p_ci_str = f"[{p_ci['ci_lo']:.4f}, {p_ci['ci_hi']:.4f}]" if p_ci else "--"
        q_ci_str = f"[{q_ci['ci_lo']:.4f}, {q_ci['ci_hi']:.4f}]" if q_ci else "--"

        lines.append(f"{label} & {p_auc_str} & {p_ci_str} & {q_auc_str} & {q_ci_str} \\\\")

    lines.append(r"\midrule")
    lines.append(f"$K^*$ (mean $> \\theta$) & \\multicolumn{{2}}{{c}}{{{pythia_kstar}}} & \\multicolumn{{2}}{{c}}{{{qwen_kstar}}} \\\\")
    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    return "\n".join(lines)


def build_output_json(pythia: dict, qwen: dict, pythia_ks: dict, qwen_ks: dict) -> dict:
    return {
        "experiment": "retrain_depth7_cross_model_comparison",
        "theta": THETA,
        "pythia": {
            "model": "EleutherAI/pythia-1.4b",
            "k_star_mean": pythia_ks["mean"],
            "k_star_ci": pythia_ks["ci"],
            "pairwise_auc": pythia["auc_mean"],
            "pairwise_ci": pythia["ci"],
            "pairwise_jsd": pythia["jsd"],
        },
        "qwen": {
            "model": "Qwen2.5-1.5B",
            "k_star_mean": qwen_ks["mean"],
            "k_star_ci": qwen_ks["ci"],
            "pairwise_auc": qwen["auc_mean"],
            "pairwise_ci": qwen["ci"],
            "pairwise_jsd": qwen["jsd"],
        },
        "cross_model_consistent": pythia_ks["mean"] == qwen_ks["mean"],
        "conclusion": (
            f"Both models achieve K*={pythia_ks['mean']} (mean-based), "
            f"confirming retrain K* >> prompt K* is model-agnostic."
            if pythia_ks["mean"] == qwen_ks["mean"]
            else f"Pythia K*={pythia_ks['mean']} vs Qwen K*={qwen_ks['mean']} (mean-based). "
            f"Difference may reflect model-specific decay rates."
        ),
    }


def main():
    if not PYTHIA_DIR.exists():
        print(f"ERROR: Pythia results not found at {PYTHIA_DIR}")
        sys.exit(1)
    if not QWEN_DIR.exists():
        print(f"ERROR: Qwen results not found at {QWEN_DIR}")
        sys.exit(1)

    pythia = load_experiment(PYTHIA_DIR)
    qwen = load_experiment(QWEN_DIR)

    pythia_kstar_ci = determine_kstar(pythia, THETA)
    pythia_kstar_mean = determine_kstar_mean(pythia, THETA)
    qwen_kstar_ci = determine_kstar(qwen, THETA)
    qwen_kstar_mean = determine_kstar_mean(qwen, THETA)

    print_summary("Pythia-1.4B retrain-chain (depth 0-7)", pythia, pythia_kstar_ci, pythia_kstar_mean)
    print_summary("Qwen2.5-1.5B retrain-chain (depth 0-7)", qwen, qwen_kstar_ci, qwen_kstar_mean)

    comparison = build_comparison_table(pythia, qwen)
    print(comparison)

    print(f"\n{'=' * 72}")
    print(f"  K* Summary (theta={THETA})")
    print(f"{'=' * 72}")
    print(f"  Pythia-1.4B:   K*={pythia_kstar_mean} (mean), K*={pythia_kstar_ci} (CI-conservative)")
    print(f"  Qwen2.5-1.5B:  K*={qwen_kstar_mean} (mean), K*={qwen_kstar_ci} (CI-conservative)")
    consistent = pythia_kstar_mean == qwen_kstar_mean
    print(f"  Cross-model consistent (mean): {'YES' if consistent else 'NO'}")
    if not consistent:
        print(f"  Delta: {abs(pythia_kstar_mean - qwen_kstar_mean)}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    out_json = build_output_json(
        pythia, qwen,
        {"mean": pythia_kstar_mean, "ci": pythia_kstar_ci},
        {"mean": qwen_kstar_mean, "ci": qwen_kstar_ci},
    )
    json_path = OUT_DIR / "comparison.json"
    with open(json_path, "w") as f:
        json.dump(out_json, f, indent=2)
    print(f"\n  JSON saved: {json_path}")

    latex = generate_latex(pythia, qwen, pythia_kstar_mean, qwen_kstar_mean)
    latex_path = OUT_DIR / "table_retrain_comparison.tex"
    with open(latex_path, "w") as f:
        f.write(latex)
    print(f"  LaTeX saved: {latex_path}")

    print(f"\n{'=' * 72}")
    print(f"  CONCLUSION")
    print(f"{'=' * 72}")
    print(f"  {out_json['conclusion']}")
    print()


if __name__ == "__main__":
    main()
