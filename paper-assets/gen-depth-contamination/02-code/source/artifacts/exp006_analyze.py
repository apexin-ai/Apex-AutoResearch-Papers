"""exp006 Analysis — aggregate results, paired t-tests, alpha sensitivity.

Input:  outputs/exp006/*/eval_results.json
Output: summary JSON + formatted tables to stdout

Dependencies: numpy, scipy, json, glob
"""

import argparse
import json
import os
import re
from collections import defaultdict
from glob import glob

import numpy as np
from scipy import stats


def parse_tag(dirname):
    """Extract (strategy, alpha, seed) from directory name like 'graduated_a0.5_s42'."""
    base = os.path.basename(dirname)
    m_grad = re.match(r"(graduated)_a([\d.]+)_s(\d+)", base)
    if m_grad:
        return m_grad.group(1), float(m_grad.group(2)), int(m_grad.group(3))
    m_other = re.match(r"(.+)_s(\d+)", base)
    if m_other:
        return m_other.group(1), None, int(m_other.group(2))
    return None, None, None


def extract_scores(result):
    """Pull MMLU acc and HellaSwag acc_norm from lm-eval result JSON."""
    scores = result.get("scores", {})
    mmlu = None
    hellaswag = None

    for task_name, metrics in scores.items():
        if "mmlu" in task_name.lower():
            mmlu = metrics.get("acc,none", metrics.get("acc_norm,none"))
        if "hellaswag" in task_name.lower():
            hellaswag = metrics.get("acc_norm,none", metrics.get("acc,none"))

    return mmlu, hellaswag


def paired_ttest(scores_a, scores_b, seeds_a, seeds_b):
    """Paired t-test on matched seeds. Returns (t_stat, p_value, n_pairs)."""
    common = sorted(set(seeds_a) & set(seeds_b))
    if len(common) < 2:
        return None, None, len(common)
    a = [scores_a[seeds_a.index(s)] for s in common]
    b = [scores_b[seeds_b.index(s)] for s in common]
    t, p = stats.ttest_rel(a, b)
    return float(t), float(p), len(common)


def main():
    parser = argparse.ArgumentParser(description="exp006 analysis")
    parser.add_argument("--results-dir", type=str, default="outputs/exp006")
    parser.add_argument("--output", type=str, default=None,
                        help="Save summary JSON")
    parser.add_argument("--best-alpha-metric", type=str, default="mmlu",
                        choices=["mmlu", "hellaswag", "avg"])
    args = parser.parse_args()

    # --- Collect results ---
    result_files = sorted(glob(os.path.join(args.results_dir, "*/eval_results.json")))
    if not result_files:
        print(f"No results found in {args.results_dir}")
        return

    # strategy -> {seeds: [], mmlu: [], hellaswag: []}
    data = defaultdict(lambda: {"seeds": [], "mmlu": [], "hellaswag": []})
    # graduated alpha sweep: (alpha,) -> same structure
    alpha_data = defaultdict(lambda: {"seeds": [], "mmlu": [], "hellaswag": []})

    for fpath in result_files:
        dirname = os.path.dirname(fpath)
        strategy, alpha, seed = parse_tag(dirname)
        if strategy is None:
            continue

        with open(fpath) as f:
            result = json.load(f)
        mmlu, hellaswag = extract_scores(result)

        if mmlu is None and hellaswag is None:
            print(f"  WARN: no scores in {fpath}")
            continue

        if strategy == "graduated" and alpha is not None:
            alpha_data[alpha]["seeds"].append(seed)
            alpha_data[alpha]["mmlu"].append(mmlu)
            alpha_data[alpha]["hellaswag"].append(hellaswag)
        else:
            data[strategy]["seeds"].append(seed)
            data[strategy]["mmlu"].append(mmlu)
            data[strategy]["hellaswag"].append(hellaswag)

    # For graduated, pick best alpha and add to main data
    best_alpha = None
    if alpha_data:
        best_score = -1
        for a, d in sorted(alpha_data.items()):
            vals = d["mmlu"] if args.best_alpha_metric == "mmlu" else d["hellaswag"]
            if args.best_alpha_metric == "avg":
                vals = [(m + h) / 2 for m, h in zip(d["mmlu"], d["hellaswag"])]
            mean_val = np.mean(vals) if vals else 0
            if mean_val > best_score:
                best_score = mean_val
                best_alpha = a
        data["graduated"] = alpha_data[best_alpha]

    # --- Summary table ---
    print("=" * 80)
    print(f"exp006 Results Summary (graduated best_alpha={best_alpha})")
    print("=" * 80)
    print(f"{'Strategy':<20} {'N':>3}  {'MMLU':>18}  {'HellaSwag':>18}")
    print("-" * 80)

    summary = {}
    for strategy in ["no-filter", "binary-ours", "binary-drayson",
                     "graduated", "surprisal", "dsir"]:
        d = data.get(strategy)
        if not d or not d["mmlu"]:
            print(f"{strategy:<20}  -   {'N/A':>18}  {'N/A':>18}")
            continue
        n = len(d["seeds"])
        mmlu_m, mmlu_s = np.mean(d["mmlu"]), np.std(d["mmlu"])
        hs_m, hs_s = np.mean(d["hellaswag"]), np.std(d["hellaswag"])
        print(f"{strategy:<20} {n:>3}  {mmlu_m:.4f} +/- {mmlu_s:.4f}  "
              f"{hs_m:.4f} +/- {hs_s:.4f}")
        summary[strategy] = {
            "n": n,
            "mmlu_mean": float(mmlu_m), "mmlu_std": float(mmlu_s),
            "hellaswag_mean": float(hs_m), "hellaswag_std": float(hs_s),
            "seeds": d["seeds"],
            "mmlu_scores": d["mmlu"],
            "hellaswag_scores": d["hellaswag"],
        }
        if strategy == "graduated":
            summary[strategy]["best_alpha"] = best_alpha

    # --- Paired t-tests ---
    print()
    print("Paired t-tests")
    print("-" * 80)
    comparisons = [
        ("graduated", "binary-ours"),
        ("graduated", "no-filter"),
        ("binary-ours", "no-filter"),
        ("graduated", "binary-drayson"),
        ("graduated", "dsir"),
        ("graduated", "surprisal"),
    ]

    ttests = {}
    for sa, sb in comparisons:
        da, db = data.get(sa), data.get(sb)
        if not da or not db:
            continue
        for metric in ["mmlu", "hellaswag"]:
            t, p, n = paired_ttest(
                da[metric], db[metric], da["seeds"], db["seeds"]
            )
            key = f"{sa}_vs_{sb}_{metric}"
            sig = ""
            if p is not None:
                if p < 0.01:
                    sig = " **"
                elif p < 0.05:
                    sig = " *"
            result_str = f"t={t:.3f}, p={p:.4f}, n={n}{sig}" if t is not None else "insufficient data"
            print(f"  {sa} vs {sb} ({metric}): {result_str}")
            ttests[key] = {"t": t, "p": p, "n": n}

    # --- Alpha sensitivity ---
    if alpha_data:
        print()
        print("Alpha sensitivity (graduated)")
        print("-" * 80)
        print(f"{'alpha':>6}  {'N':>3}  {'MMLU':>18}  {'HellaSwag':>18}")
        alpha_summary = {}
        for a in sorted(alpha_data.keys()):
            d = alpha_data[a]
            n = len(d["seeds"])
            mmlu_m, mmlu_s = np.mean(d["mmlu"]), np.std(d["mmlu"])
            hs_m, hs_s = np.mean(d["hellaswag"]), np.std(d["hellaswag"])
            marker = " <-- best" if a == best_alpha else ""
            print(f"{a:>6.1f}  {n:>3}  {mmlu_m:.4f} +/- {mmlu_s:.4f}  "
                  f"{hs_m:.4f} +/- {hs_s:.4f}{marker}")
            alpha_summary[str(a)] = {
                "n": n,
                "mmlu_mean": float(mmlu_m), "mmlu_std": float(mmlu_s),
                "hellaswag_mean": float(hs_m), "hellaswag_std": float(hs_s),
            }

    # --- Output ---
    output = {
        "summary": summary,
        "paired_ttests": ttests,
        "alpha_sensitivity": alpha_summary if alpha_data else {},
        "best_alpha": best_alpha,
        "best_alpha_metric": args.best_alpha_metric,
    }

    if args.output:
        os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
        with open(args.output, "w") as f:
            json.dump(output, f, indent=2)
        print(f"\nSummary saved to {args.output}")
    else:
        print(f"\nJSON output (use --output to save):")
        print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
