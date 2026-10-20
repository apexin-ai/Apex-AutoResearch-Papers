"""exp006 graduated filtering — full results analysis.

Scans outputs/exp006/*/eval_results.json, produces summary tables,
statistical tests, and LaTeX output.

Dependencies: numpy, scipy (stdlib: json, csv, os, re, argparse, glob)
"""

import argparse
import csv
import json
import os
import re
import sys
from collections import defaultdict
from glob import glob

import numpy as np
from scipy import stats

STRATEGIES_ORDER = [
    "no-filter", "binary-ours", "binary-drayson",
    "graduated", "surprisal", "dsir",
]
SEEDS = [42, 123, 456, 789, 1024]
ALPHAS = [0.1, 0.3, 0.5, 0.7, 0.9]


def parse_tag(dirname):
    base = os.path.basename(dirname)
    if base == "base_model":
        return "base_model", None, None
    m_grad = re.match(r"(graduated)_a([\d.]+)_s(\d+)$", base)
    if m_grad:
        return m_grad.group(1), float(m_grad.group(2)), int(m_grad.group(3))
    m_other = re.match(r"(.+)_s(\d+)$", base)
    if m_other:
        return m_other.group(1), None, int(m_other.group(2))
    return None, None, None


def extract_scores(result):
    scores = result.get("scores", {})
    mmlu = scores.get("mmlu", {}).get("acc,none")
    hellaswag = scores.get("hellaswag", {}).get("acc_norm,none")
    return mmlu, hellaswag


def paired_test(a_scores, b_scores, a_seeds, b_seeds):
    common = sorted(set(a_seeds) & set(b_seeds))
    if len(common) < 3:
        return {"n": len(common), "t": None, "t_p": None, "w": None, "w_p": None}
    a = np.array([a_scores[a_seeds.index(s)] for s in common])
    b = np.array([b_scores[b_seeds.index(s)] for s in common])
    t_stat, t_p = stats.ttest_rel(a, b)
    try:
        w_stat, w_p = stats.wilcoxon(a, b)
    except ValueError:
        w_stat, w_p = None, None
    return {
        "n": len(common),
        "t": float(t_stat), "t_p": float(t_p),
        "w": float(w_stat) if w_stat is not None else None,
        "w_p": float(w_p) if w_p is not None else None,
    }


def sig_marker(p):
    if p is None:
        return ""
    if p < 0.01:
        return "**"
    if p < 0.05:
        return "*"
    return ""


def latex_val(mean, std, bold=False):
    s = f"{mean:.2f} {{\\scriptsize $\\pm$ {std:.2f}}}"
    if bold:
        s = f"\\textbf{{{s}}}"
    return s


def main():
    parser = argparse.ArgumentParser(description="exp006 graduated filtering analysis")
    parser.add_argument("--results-dir", default="/root/autodl-tmp/gen-depth-contamination/outputs/exp006")
    parser.add_argument("--output-dir", default="artifacts/exp006_results")
    parser.add_argument("--alpha-metric", default="avg", choices=["mmlu", "hellaswag", "avg"],
                        help="Metric for selecting best graduated alpha")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    result_files = sorted(glob(os.path.join(args.results_dir, "*/eval_results.json")))
    if not result_files:
        print(f"ERROR: No results in {args.results_dir}", file=sys.stderr)
        sys.exit(1)

    # ---- Collect ----
    base_model = {"mmlu": None, "hellaswag": None}
    data = defaultdict(lambda: {"seeds": [], "mmlu": [], "hellaswag": []})
    alpha_data = defaultdict(lambda: {"seeds": [], "mmlu": [], "hellaswag": []})
    missing = []

    for fpath in result_files:
        dirname = os.path.dirname(fpath)
        strategy, alpha, seed = parse_tag(dirname)

        with open(fpath) as f:
            result = json.load(f)
        mmlu, hellaswag = extract_scores(result)

        if strategy == "base_model":
            base_model["mmlu"] = mmlu
            base_model["hellaswag"] = hellaswag
            continue

        if strategy is None:
            print(f"  WARN: unrecognized dir {dirname}", file=sys.stderr)
            continue

        if mmlu is None or hellaswag is None:
            print(f"  WARN: incomplete scores in {fpath}", file=sys.stderr)
            missing.append(os.path.basename(dirname))
            continue

        if strategy == "graduated" and alpha is not None:
            alpha_data[alpha]["seeds"].append(seed)
            alpha_data[alpha]["mmlu"].append(mmlu)
            alpha_data[alpha]["hellaswag"].append(hellaswag)
        else:
            data[strategy]["seeds"].append(seed)
            data[strategy]["mmlu"].append(mmlu)
            data[strategy]["hellaswag"].append(hellaswag)

    # Check expected runs
    for strat in STRATEGIES_ORDER:
        if strat == "graduated":
            for alpha in ALPHAS:
                for seed in SEEDS:
                    tag = f"graduated_a{alpha}_s{seed}"
                    if seed not in alpha_data.get(alpha, {}).get("seeds", []):
                        missing.append(tag)
        else:
            for seed in SEEDS:
                if seed not in data.get(strat, {}).get("seeds", []):
                    missing.append(f"{strat}_s{seed}")

    if missing:
        print(f"  WARN: {len(missing)} missing runs: {missing[:10]}{'...' if len(missing) > 10 else ''}", file=sys.stderr)

    # ---- Best alpha for graduated ----
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

    # ---- Summary stats ----
    summary = {}
    if base_model["mmlu"] is not None:
        summary["base_model"] = {
            "n": 1,
            "mmlu_mean": base_model["mmlu"], "mmlu_std": 0.0,
            "hellaswag_mean": base_model["hellaswag"], "hellaswag_std": 0.0,
            "seeds": [], "mmlu_scores": [base_model["mmlu"]], "hellaswag_scores": [base_model["hellaswag"]],
        }

    for strat in STRATEGIES_ORDER:
        d = data.get(strat)
        if not d or not d["mmlu"]:
            continue
        mmlu_arr = np.array(d["mmlu"])
        hs_arr = np.array(d["hellaswag"])
        summary[strat] = {
            "n": len(d["seeds"]),
            "mmlu_mean": float(np.mean(mmlu_arr)), "mmlu_std": float(np.std(mmlu_arr, ddof=1)) if len(mmlu_arr) > 1 else 0.0,
            "hellaswag_mean": float(np.mean(hs_arr)), "hellaswag_std": float(np.std(hs_arr, ddof=1)) if len(hs_arr) > 1 else 0.0,
            "seeds": d["seeds"],
            "mmlu_scores": [float(x) for x in d["mmlu"]],
            "hellaswag_scores": [float(x) for x in d["hellaswag"]],
        }
        if strat == "graduated" and best_alpha is not None:
            summary[strat]["best_alpha"] = best_alpha

    # ---- Relative improvements ----
    improvements = {}
    for ref_name in ["base_model", "no-filter"]:
        ref = summary.get(ref_name)
        if not ref:
            continue
        for strat in STRATEGIES_ORDER:
            s = summary.get(strat)
            if not s or strat == ref_name:
                continue
            key = f"{strat}_vs_{ref_name}"
            improvements[key] = {
                "mmlu_delta": s["mmlu_mean"] - ref["mmlu_mean"],
                "mmlu_rel_pct": (s["mmlu_mean"] - ref["mmlu_mean"]) / ref["mmlu_mean"] * 100 if ref["mmlu_mean"] else None,
                "hellaswag_delta": s["hellaswag_mean"] - ref["hellaswag_mean"],
                "hellaswag_rel_pct": (s["hellaswag_mean"] - ref["hellaswag_mean"]) / ref["hellaswag_mean"] * 100 if ref["hellaswag_mean"] else None,
            }

    # ---- Statistical tests ----
    comparisons = [
        ("graduated", "binary-ours"),
        ("graduated", "binary-drayson"),
        ("graduated", "no-filter"),
        ("graduated", "surprisal"),
        ("graduated", "dsir"),
        ("binary-ours", "no-filter"),
        ("binary-drayson", "no-filter"),
        ("surprisal", "no-filter"),
        ("dsir", "no-filter"),
    ]

    stat_tests = {}
    for sa, sb in comparisons:
        da, db = data.get(sa), data.get(sb)
        if not da or not db:
            continue
        for metric in ["mmlu", "hellaswag"]:
            key = f"{sa}_vs_{sb}_{metric}"
            stat_tests[key] = paired_test(
                da[metric], db[metric], da["seeds"], db["seeds"]
            )

    # ---- Alpha sensitivity ----
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
            "seeds": d["seeds"],
        }

    # ---- Print ----
    print("=" * 90)
    print(f"exp006 Results (graduated best α={best_alpha}, selected by {args.alpha_metric})")
    print("=" * 90)

    header = f"{'Strategy':<20} {'N':>3}  {'MMLU (acc)':>20}  {'HellaSwag (acc_norm)':>20}"
    print(header)
    print("-" * 90)

    if "base_model" in summary:
        s = summary["base_model"]
        print(f"{'base_model':<20} {s['n']:>3}  {s['mmlu_mean']:>20.4f}  {s['hellaswag_mean']:>20.4f}")
        print("-" * 90)

    for strat in STRATEGIES_ORDER:
        s = summary.get(strat)
        if not s:
            print(f"{strat:<20}  --  {'N/A':>20}  {'N/A':>20}")
            continue
        mmlu_str = f"{s['mmlu_mean']:.4f} ± {s['mmlu_std']:.4f}"
        hs_str = f"{s['hellaswag_mean']:.4f} ± {s['hellaswag_std']:.4f}"
        print(f"{strat:<20} {s['n']:>3}  {mmlu_str:>20}  {hs_str:>20}")

    # Improvements
    print()
    print("Relative improvements (pp)")
    print("-" * 90)
    for ref_name in ["base_model", "no-filter"]:
        for strat in STRATEGIES_ORDER:
            key = f"{strat}_vs_{ref_name}"
            imp = improvements.get(key)
            if not imp:
                continue
            md = imp["mmlu_delta"] * 100
            hd = imp["hellaswag_delta"] * 100
            print(f"  {strat} vs {ref_name}: MMLU {md:+.2f}pp  HellaSwag {hd:+.2f}pp")

    # Statistical tests
    print()
    print("Statistical tests (paired t-test / Wilcoxon signed-rank)")
    print("-" * 90)
    for sa, sb in comparisons:
        for metric in ["mmlu", "hellaswag"]:
            key = f"{sa}_vs_{sb}_{metric}"
            r = stat_tests.get(key)
            if not r:
                continue
            if r["t"] is not None:
                t_sig = sig_marker(r["t_p"])
                w_part = f", W={r['w']:.1f} p={r['w_p']:.4f}{sig_marker(r['w_p'])}" if r["w"] is not None else ""
                print(f"  {sa} vs {sb} [{metric}]: t={r['t']:.3f} p={r['t_p']:.4f}{t_sig}{w_part} (n={r['n']})")
            else:
                print(f"  {sa} vs {sb} [{metric}]: insufficient data (n={r['n']})")

    # Alpha sensitivity
    if alpha_summary:
        print()
        print("Alpha sensitivity (graduated)")
        print("-" * 90)
        print(f"  {'α':>5}  {'N':>3}  {'MMLU':>18}  {'HellaSwag':>18}")
        for a in sorted(alpha_summary.keys(), key=float):
            d = alpha_summary[a]
            marker = " <--" if best_alpha is not None and float(a) == best_alpha else ""
            print(f"  {a:>5}  {d['n']:>3}  {d['mmlu_mean']:.4f} ± {d['mmlu_std']:.4f}  "
                  f"{d['hellaswag_mean']:.4f} ± {d['hellaswag_std']:.4f}{marker}")

    # ---- Seed × Strategy matrix (CSV-friendly) ----
    print()
    print("Seed × Strategy matrix (MMLU)")
    print("-" * 90)
    seed_header = "Strategy," + ",".join(str(s) for s in SEEDS) + ",Mean,Std"
    print(f"  {seed_header}")
    for strat in STRATEGIES_ORDER:
        d = data.get(strat)
        if not d:
            continue
        vals = []
        for s in SEEDS:
            if s in d["seeds"]:
                vals.append(f"{d['mmlu'][d['seeds'].index(s)]:.4f}")
            else:
                vals.append("-")
        s = summary.get(strat, {})
        vals.append(f"{s.get('mmlu_mean', 0):.4f}")
        vals.append(f"{s.get('mmlu_std', 0):.4f}")
        print(f"  {strat},{','.join(vals)}")

    # ---- Save JSON ----
    output = {
        "base_model": base_model,
        "summary": summary,
        "improvements": improvements,
        "stat_tests": stat_tests,
        "alpha_sensitivity": alpha_summary,
        "best_alpha": best_alpha,
        "alpha_metric": args.alpha_metric,
        "missing_runs": missing,
    }
    json_path = os.path.join(args.output_dir, "summary.json")
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved: {json_path}")

    # ---- Save CSV ----
    csv_path = os.path.join(args.output_dir, "summary.csv")
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["strategy", "n", "mmlu_mean", "mmlu_std",
                         "hellaswag_mean", "hellaswag_std",
                         "mmlu_delta_vs_base", "hellaswag_delta_vs_base",
                         "mmlu_delta_vs_nofilter", "hellaswag_delta_vs_nofilter"])
        for strat in ["base_model"] + STRATEGIES_ORDER:
            s = summary.get(strat)
            if not s:
                continue
            imp_base = improvements.get(f"{strat}_vs_base_model", {})
            imp_nf = improvements.get(f"{strat}_vs_no-filter", {})
            writer.writerow([
                strat, s["n"],
                f"{s['mmlu_mean']:.6f}", f"{s['mmlu_std']:.6f}",
                f"{s['hellaswag_mean']:.6f}", f"{s['hellaswag_std']:.6f}",
                f"{imp_base.get('mmlu_delta', 0):.6f}" if imp_base else "",
                f"{imp_base.get('hellaswag_delta', 0):.6f}" if imp_base else "",
                f"{imp_nf.get('mmlu_delta', 0):.6f}" if imp_nf else "",
                f"{imp_nf.get('hellaswag_delta', 0):.6f}" if imp_nf else "",
            ])
    print(f"Saved: {csv_path}")

    # ---- LaTeX table ----
    tex_path = os.path.join(args.output_dir, "latex_table.tex")
    with open(tex_path, "w") as f:
        f.write("% Auto-generated by exp006_analyze_results.py\n")
        f.write("\\begin{table}[t]\n")
        f.write("\\centering\n")
        f.write("\\caption{Downstream performance under six filtering strategies. ")
        if best_alpha is not None:
            f.write(f"Graduated uses $\\alpha={best_alpha}$ (best by {args.alpha_metric}). ")
        f.write("Bold = best among filtering strategies.}\n")
        f.write("\\label{tab:exp006_filtering}\n")
        f.write("\\begin{tabular}{lcc}\n")
        f.write("\\toprule\n")
        f.write("Strategy & MMLU (0-shot) & HellaSwag (0-shot) \\\\\n")
        f.write("\\midrule\n")

        # Find best values (excluding base_model)
        best_mmlu = max((summary[s]["mmlu_mean"] for s in STRATEGIES_ORDER if s in summary), default=0)
        best_hs = max((summary[s]["hellaswag_mean"] for s in STRATEGIES_ORDER if s in summary), default=0)

        # Base model row
        if "base_model" in summary:
            s = summary["base_model"]
            f.write(f"Base model (no training) & {s['mmlu_mean']*100:.2f} & {s['hellaswag_mean']*100:.2f} \\\\\n")
            f.write("\\midrule\n")

        display_names = {
            "no-filter": "No filter",
            "binary-ours": "Binary (ours)",
            "binary-drayson": "Binary (Drayson)",
            "graduated": f"Graduated ($\\alpha$={best_alpha})" if best_alpha else "Graduated",
            "surprisal": "Surprisal threshold",
            "dsir": "DSIR",
        }
        for strat in STRATEGIES_ORDER:
            s = summary.get(strat)
            if not s:
                continue
            name = display_names.get(strat, strat)
            mmlu_bold = abs(s["mmlu_mean"] - best_mmlu) < 1e-8
            hs_bold = abs(s["hellaswag_mean"] - best_hs) < 1e-8
            mmlu_str = latex_val(s["mmlu_mean"] * 100, s["mmlu_std"] * 100, bold=mmlu_bold)
            hs_str = latex_val(s["hellaswag_mean"] * 100, s["hellaswag_std"] * 100, bold=hs_bold)
            f.write(f"{name} & {mmlu_str} & {hs_str} \\\\\n")

        f.write("\\bottomrule\n")
        f.write("\\end{tabular}\n")
        f.write("\\end{table}\n")

        # Alpha sensitivity sub-table
        if alpha_summary:
            f.write("\n% Alpha sensitivity\n")
            f.write("\\begin{table}[t]\n")
            f.write("\\centering\n")
            f.write("\\caption{Graduated filtering: sensitivity to decay parameter $\\alpha$.}\n")
            f.write("\\label{tab:exp006_alpha}\n")
            f.write("\\begin{tabular}{ccc}\n")
            f.write("\\toprule\n")
            f.write("$\\alpha$ & MMLU (0-shot) & HellaSwag (0-shot) \\\\\n")
            f.write("\\midrule\n")
            best_a_mmlu = max((alpha_summary[a]["mmlu_mean"] for a in alpha_summary), default=0)
            best_a_hs = max((alpha_summary[a]["hellaswag_mean"] for a in alpha_summary), default=0)
            for a in sorted(alpha_summary.keys(), key=float):
                d = alpha_summary[a]
                m_bold = abs(d["mmlu_mean"] - best_a_mmlu) < 1e-8
                h_bold = abs(d["hellaswag_mean"] - best_a_hs) < 1e-8
                m_str = latex_val(d["mmlu_mean"] * 100, d["mmlu_std"] * 100, bold=m_bold)
                h_str = latex_val(d["hellaswag_mean"] * 100, d["hellaswag_std"] * 100, bold=h_bold)
                f.write(f"{a} & {m_str} & {h_str} \\\\\n")
            f.write("\\bottomrule\n")
            f.write("\\end{tabular}\n")
            f.write("\\end{table}\n")

    print(f"Saved: {tex_path}")


if __name__ == "__main__":
    main()
