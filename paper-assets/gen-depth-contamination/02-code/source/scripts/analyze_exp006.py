"""exp006 graduated filtering — results analysis with statistical tests.

Reads outputs/exp006/*/eval_results.json (6 strategies × 5 seeds × {MMLU, HellaSwag}).
Produces: terminal summary, LaTeX table, exp006_summary.json.

Usage:
    python analyze_exp006.py --results_dir /path/to/outputs/exp006 [--output_dir artifacts/exp006]
"""

import argparse
import json
import os
import re
import sys
import warnings
from collections import defaultdict
from glob import glob

import numpy as np
from scipy import stats

STRATEGIES = [
    "no-filter", "binary-ours", "binary-drayson",
    "graduated", "surprisal", "dsir",
]
SEEDS = [42, 123, 456, 789, 1024]
ALPHAS = [0.1, 0.3, 0.5, 0.7, 0.9]

DISPLAY_NAMES = {
    "no-filter": "No filter",
    "binary-ours": "Binary (ours)",
    "binary-drayson": "Binary (Drayson)",
    "graduated": "Graduated",
    "surprisal": "Surprisal",
    "dsir": "DSIR",
    "base_model": "Base model",
}

BONFERRONI_COMPARISONS = [
    ("graduated", "binary-ours"),
    ("graduated", "binary-drayson"),
    ("graduated", "no-filter"),
    ("graduated", "surprisal"),
    ("graduated", "dsir"),
    ("binary-ours", "no-filter"),
]


def parse_tag(dirname):
    base = os.path.basename(dirname)
    if base == "base_model":
        return "base_model", None, None
    m = re.match(r"(graduated)_a([\d.]+)_s(\d+)$", base)
    if m:
        return m.group(1), float(m.group(2)), int(m.group(3))
    m = re.match(r"(.+)_s(\d+)$", base)
    if m:
        return m.group(1), None, int(m.group(2))
    return None, None, None


def extract_scores(result):
    scores = result.get("scores", {})
    mmlu = hs = None
    for task, metrics in scores.items():
        if "mmlu" in task.lower():
            mmlu = metrics.get("acc,none", metrics.get("acc_norm,none"))
        if "hellaswag" in task.lower():
            hs = metrics.get("acc_norm,none", metrics.get("acc,none"))
    return mmlu, hs


def cohens_d(a, b):
    diff = np.array(a) - np.array(b)
    return float(np.mean(diff) / np.std(diff, ddof=1)) if np.std(diff, ddof=1) > 0 else 0.0


def paired_test(a_scores, b_scores, a_seeds, b_seeds):
    common = sorted(set(a_seeds) & set(b_seeds))
    if len(common) < 3:
        return {"n": len(common), "t": None, "p_t": None, "w": None, "p_w": None, "d": None}
    a = [a_scores[a_seeds.index(s)] for s in common]
    b = [b_scores[b_seeds.index(s)] for s in common]
    t_stat, t_p = stats.ttest_rel(a, b)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        try:
            w_stat, w_p = stats.wilcoxon(a, b)
        except ValueError:
            w_stat, w_p = None, None
    d = cohens_d(a, b)
    return {
        "n": len(common),
        "t": float(t_stat), "p_t": float(t_p),
        "w": float(w_stat) if w_stat is not None else None,
        "p_w": float(w_p) if w_p is not None else None,
        "d": d,
    }


def sig_marker(p, corrected_alpha=0.05):
    if p is None:
        return ""
    if p < corrected_alpha / 10:
        return "**"
    if p < corrected_alpha:
        return "*"
    return ""


def latex_val(mean, std, bold=False):
    s = f"{mean:.2f} {{\\scriptsize $\\pm$ {std:.2f}}}"
    return f"\\textbf{{{s}}}" if bold else s


def main():
    parser = argparse.ArgumentParser(description="exp006 graduated filtering analysis")
    parser.add_argument("--results_dir", default="/root/autodl-tmp/gen-depth-contamination/outputs/exp006")
    parser.add_argument("--output_dir", default="artifacts/exp006")
    parser.add_argument("--alpha_metric", default="avg", choices=["mmlu", "hellaswag", "avg"],
                        help="metric for selecting best graduated alpha")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    result_files = sorted(glob(os.path.join(args.results_dir, "*/eval_results.json")))
    if not result_files:
        print(f"ERROR: no results in {args.results_dir}", file=sys.stderr)
        sys.exit(1)

    # ── Collect ──
    base_model = {"mmlu": None, "hellaswag": None}
    data = defaultdict(lambda: {"seeds": [], "mmlu": [], "hellaswag": []})
    alpha_data = defaultdict(lambda: {"seeds": [], "mmlu": [], "hellaswag": []})
    missing = []

    for fpath in result_files:
        dirname = os.path.dirname(fpath)
        strategy, alpha, seed = parse_tag(dirname)

        with open(fpath) as f:
            result = json.load(f)
        mmlu, hs = extract_scores(result)

        if strategy == "base_model":
            base_model["mmlu"] = mmlu
            base_model["hellaswag"] = hs
            continue
        if strategy is None:
            print(f"  WARN: unrecognized dir {dirname}", file=sys.stderr)
            continue
        if mmlu is None or hs is None:
            print(f"  WARN: incomplete scores in {fpath}", file=sys.stderr)
            missing.append(os.path.basename(dirname))
            continue

        if strategy == "graduated" and alpha is not None:
            alpha_data[alpha]["seeds"].append(seed)
            alpha_data[alpha]["mmlu"].append(mmlu)
            alpha_data[alpha]["hellaswag"].append(hs)
        else:
            data[strategy]["seeds"].append(seed)
            data[strategy]["mmlu"].append(mmlu)
            data[strategy]["hellaswag"].append(hs)

    # Check missing runs
    for strat in STRATEGIES:
        if strat == "graduated":
            for a in ALPHAS:
                for s in SEEDS:
                    if s not in alpha_data.get(a, {}).get("seeds", []):
                        missing.append(f"graduated_a{a}_s{s}")
        else:
            for s in SEEDS:
                if s not in data.get(strat, {}).get("seeds", []):
                    missing.append(f"{strat}_s{s}")

    if missing:
        print(f"  WARN: {len(missing)} missing runs: {missing[:10]}{'...' if len(missing) > 10 else ''}", file=sys.stderr)

    # ── Best alpha ──
    best_alpha = None
    if alpha_data:
        best_score = -1
        for a, d in sorted(alpha_data.items()):
            if not d["mmlu"]:
                continue
            if args.alpha_metric == "mmlu":
                val = np.mean(d["mmlu"])
            elif args.alpha_metric == "hellaswag":
                val = np.mean(d["hellaswag"])
            else:
                val = np.mean([(m + h) / 2 for m, h in zip(d["mmlu"], d["hellaswag"])])
            if val > best_score:
                best_score = val
                best_alpha = a
        if best_alpha is not None:
            data["graduated"] = alpha_data[best_alpha]

    # ── Summary stats ──
    summary = {}
    if base_model["mmlu"] is not None:
        summary["base_model"] = {
            "n": 1,
            "mmlu_mean": base_model["mmlu"], "mmlu_std": 0.0,
            "hellaswag_mean": base_model["hellaswag"], "hellaswag_std": 0.0,
        }

    for strat in STRATEGIES:
        d = data.get(strat)
        if not d or not d["mmlu"]:
            continue
        arr_m = np.array(d["mmlu"])
        arr_h = np.array(d["hellaswag"])
        summary[strat] = {
            "n": len(d["seeds"]),
            "mmlu_mean": float(np.mean(arr_m)),
            "mmlu_std": float(np.std(arr_m, ddof=1)) if len(arr_m) > 1 else 0.0,
            "hellaswag_mean": float(np.mean(arr_h)),
            "hellaswag_std": float(np.std(arr_h, ddof=1)) if len(arr_h) > 1 else 0.0,
            "seeds": d["seeds"],
            "mmlu_scores": [float(x) for x in d["mmlu"]],
            "hellaswag_scores": [float(x) for x in d["hellaswag"]],
        }
        if strat == "graduated" and best_alpha is not None:
            summary[strat]["best_alpha"] = best_alpha

    # ── Alpha sensitivity ──
    alpha_summary = {}
    for a in sorted(alpha_data.keys()):
        d = alpha_data[a]
        if not d["mmlu"]:
            continue
        alpha_summary[str(a)] = {
            "n": len(d["seeds"]),
            "mmlu_mean": float(np.mean(d["mmlu"])),
            "mmlu_std": float(np.std(d["mmlu"], ddof=1)) if len(d["mmlu"]) > 1 else 0.0,
            "hellaswag_mean": float(np.mean(d["hellaswag"])),
            "hellaswag_std": float(np.std(d["hellaswag"], ddof=1)) if len(d["hellaswag"]) > 1 else 0.0,
        }

    # ── Statistical tests with Bonferroni correction ──
    n_comparisons = len(BONFERRONI_COMPARISONS) * 2  # ×2 metrics
    corrected_alpha = 0.05 / n_comparisons

    stat_tests = {}
    for sa, sb in BONFERRONI_COMPARISONS:
        da, db = data.get(sa), data.get(sb)
        if not da or not db:
            continue
        for metric in ["mmlu", "hellaswag"]:
            key = f"{sa}_vs_{sb}_{metric}"
            result = paired_test(da[metric], db[metric], da["seeds"], db["seeds"])
            result["bonferroni_alpha"] = corrected_alpha
            result["significant"] = (result["p_t"] is not None and result["p_t"] < corrected_alpha)
            stat_tests[key] = result

    # ── Contingency judgment ──
    grad_vs_binary_keys = [
        f"graduated_vs_binary-ours_{m}" for m in ["mmlu", "hellaswag"]
    ]
    grad_wins = all(
        stat_tests.get(k, {}).get("significant", False)
        and stat_tests.get(k, {}).get("t", 0) is not None
        and stat_tests.get(k, {}).get("t", 0) > 0
        for k in grad_vs_binary_keys
        if k in stat_tests
    )
    any_grad_result = any(k in stat_tests for k in grad_vs_binary_keys)

    if not any_grad_result:
        contingency = "UNDETERMINED"
        contingency_reason = "Insufficient data for graduated vs binary-ours comparison."
    elif grad_wins:
        contingency = "VERSION_A"
        contingency_reason = (
            "Graduated filtering significantly outperforms binary-ours on both MMLU and HellaSwag "
            f"(p < {corrected_alpha:.4f} after Bonferroni correction)."
        )
    else:
        contingency = "VERSION_B"
        reasons = []
        for k in grad_vs_binary_keys:
            r = stat_tests.get(k)
            if r is None:
                reasons.append(f"{k}: no data")
            elif not r["significant"]:
                reasons.append(f"{k}: p={r['p_t']:.4f} (not significant after correction)")
            elif r["t"] is not None and r["t"] <= 0:
                reasons.append(f"{k}: graduated is not better (t={r['t']:.3f})")
        contingency_reason = "Graduated does not significantly outperform binary-ours. " + "; ".join(reasons)

    # ── Print terminal summary ──
    print("=" * 90)
    print(f"exp006 Results  |  graduated best α={best_alpha}  |  Bonferroni α={corrected_alpha:.4f} ({n_comparisons} tests)")
    print("=" * 90)

    print(f"\n{'Strategy':<20} {'N':>3}  {'MMLU (acc)':>20}  {'HellaSwag (acc_norm)':>20}")
    print("-" * 70)
    if "base_model" in summary:
        s = summary["base_model"]
        print(f"{'base_model':<20} {s['n']:>3}  {s['mmlu_mean']:>20.4f}  {s['hellaswag_mean']:>20.4f}")
        print("-" * 70)
    for strat in STRATEGIES:
        s = summary.get(strat)
        if not s:
            print(f"{strat:<20}  --")
            continue
        m_str = f"{s['mmlu_mean']:.4f} ± {s['mmlu_std']:.4f}"
        h_str = f"{s['hellaswag_mean']:.4f} ± {s['hellaswag_std']:.4f}"
        print(f"{strat:<20} {s['n']:>3}  {m_str:>20}  {h_str:>20}")

    # Statistical tests
    print(f"\nStatistical tests (paired t-test, Bonferroni α={corrected_alpha:.4f})")
    print("-" * 90)
    for sa, sb in BONFERRONI_COMPARISONS:
        for metric in ["mmlu", "hellaswag"]:
            key = f"{sa}_vs_{sb}_{metric}"
            r = stat_tests.get(key)
            if not r:
                continue
            if r["t"] is not None:
                mark = sig_marker(r["p_t"], corrected_alpha)
                d_str = f"d={r['d']:.3f}" if r["d"] is not None else ""
                w_str = f"W p={r['p_w']:.4f}" if r["p_w"] is not None else ""
                print(f"  {sa} vs {sb} [{metric}]: t={r['t']:.3f}  p={r['p_t']:.4f}{mark}  {d_str}  {w_str}  (n={r['n']})")
            else:
                print(f"  {sa} vs {sb} [{metric}]: insufficient data (n={r['n']})")

    # Alpha sensitivity
    if alpha_summary:
        print(f"\nAlpha sensitivity (graduated)")
        print("-" * 70)
        print(f"  {'α':>5}  {'N':>3}  {'MMLU':>18}  {'HellaSwag':>18}")
        for a in sorted(alpha_summary.keys(), key=float):
            d = alpha_summary[a]
            marker = " <--" if best_alpha is not None and float(a) == best_alpha else ""
            print(f"  {a:>5}  {d['n']:>3}  {d['mmlu_mean']:.4f} ± {d['mmlu_std']:.4f}  "
                  f"{d['hellaswag_mean']:.4f} ± {d['hellaswag_std']:.4f}{marker}")

    # Contingency
    print(f"\n{'=' * 90}")
    print(f"CONTINGENCY: {contingency}")
    print(f"  {contingency_reason}")
    print(f"{'=' * 90}")

    # ── LaTeX table ──
    tex_path = os.path.join(args.output_dir, "exp006_table.tex")
    with open(tex_path, "w") as f:
        f.write("% Auto-generated by analyze_exp006.py\n")
        f.write("\\begin{table}[t]\n\\centering\n")
        f.write("\\caption{Downstream performance under six filtering strategies")
        if best_alpha is not None:
            f.write(f" (graduated $\\alpha={best_alpha}$)")
        f.write(". Bold = best among filtering strategies.}\n")
        f.write("\\label{tab:exp006}\n")
        f.write("\\begin{tabular}{lccc}\n\\toprule\n")
        f.write("Strategy & MMLU (mean$\\pm$std) & HellaSwag (mean$\\pm$std) & vs binary-ours ($p$) \\\\\n")
        f.write("\\midrule\n")

        if "base_model" in summary:
            s = summary["base_model"]
            f.write(f"Base model & {s['mmlu_mean']*100:.2f} & {s['hellaswag_mean']*100:.2f} & --- \\\\\n")
            f.write("\\midrule\n")

        best_mmlu = max((summary[s]["mmlu_mean"] for s in STRATEGIES if s in summary), default=0)
        best_hs = max((summary[s]["hellaswag_mean"] for s in STRATEGIES if s in summary), default=0)

        for strat in STRATEGIES:
            s = summary.get(strat)
            if not s:
                continue
            name = DISPLAY_NAMES.get(strat, strat)
            if strat == "graduated" and best_alpha is not None:
                name = f"Graduated ($\\alpha$={best_alpha})"
            m_bold = abs(s["mmlu_mean"] - best_mmlu) < 1e-8
            h_bold = abs(s["hellaswag_mean"] - best_hs) < 1e-8
            m_str = latex_val(s["mmlu_mean"] * 100, s["mmlu_std"] * 100, bold=m_bold)
            h_str = latex_val(s["hellaswag_mean"] * 100, s["hellaswag_std"] * 100, bold=h_bold)

            # p-value vs binary-ours (use avg of MMLU and HellaSwag p-values — show both)
            if strat == "binary-ours":
                p_str = "---"
            else:
                p_parts = []
                for metric in ["mmlu", "hellaswag"]:
                    r = stat_tests.get(f"{strat}_vs_binary-ours_{metric}")
                    if r and r["p_t"] is not None:
                        mark = sig_marker(r["p_t"], corrected_alpha)
                        p_parts.append(f"{r['p_t']:.3f}{mark}")
                p_str = " / ".join(p_parts) if p_parts else "---"

            f.write(f"{name} & {m_str} & {h_str} & {p_str} \\\\\n")

        f.write("\\bottomrule\n\\end{tabular}\n\\end{table}\n")
    print(f"\nSaved: {tex_path}")

    # ── JSON summary ──
    output = {
        "experiment": "exp006_graduated_filtering",
        "best_alpha": best_alpha,
        "alpha_metric": args.alpha_metric,
        "bonferroni_alpha": corrected_alpha,
        "n_comparisons": n_comparisons,
        "contingency": contingency,
        "contingency_reason": contingency_reason,
        "summary": summary,
        "alpha_sensitivity": alpha_summary,
        "stat_tests": stat_tests,
        "base_model": base_model,
        "missing_runs": missing,
    }
    json_path = os.path.join(args.output_dir, "exp006_summary.json")
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"Saved: {json_path}")


if __name__ == "__main__":
    main()
