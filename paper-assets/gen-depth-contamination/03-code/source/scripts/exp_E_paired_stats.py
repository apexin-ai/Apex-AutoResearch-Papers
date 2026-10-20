"""EXP-E: Pairwise paired t-tests for 6 strategies × 5 seeds (MMLU & HellaSwag)."""

import json
import os
import sys
from itertools import combinations
import numpy as np
from scipy import stats

BASE_DIR = "/root/autodl-tmp/gen-depth-contamination/outputs/exp006"
OUT_PATH = "/root/autodl-tmp/gen-depth-contamination/artifacts/exp_E_paired_stats.json"

MAIN_STRATEGIES = ["binary-ours", "binary-drayson", "surprisal", "graduated_a0.9", "dsir", "no-filter"]
GRADUATED_ALPHAS = ["graduated_a0.1", "graduated_a0.3", "graduated_a0.5", "graduated_a0.7"]
ALL_STRATEGIES = MAIN_STRATEGIES + GRADUATED_ALPHAS
SEEDS = [42, 123, 456, 789, 1024]


def load_scores():
    data = {}
    for strat in ALL_STRATEGIES:
        data[strat] = {"mmlu": [], "hellaswag": []}
        for seed in SEEDS:
            path = os.path.join(BASE_DIR, f"{strat}_s{seed}", "eval_results.json")
            with open(path) as f:
                res = json.load(f)
            data[strat]["mmlu"].append(res["scores"]["mmlu"]["acc,none"])
            data[strat]["hellaswag"].append(res["scores"]["hellaswag"]["acc_norm,none"])
    return data


def cohens_d_paired(x, y):
    x, y = np.array(x), np.array(y)
    pooled_sd = np.sqrt((np.var(x, ddof=1) + np.var(y, ddof=1)) / 2)
    return float(np.mean(x - y) / pooled_sd) if pooled_sd > 0 else 0.0


def holm_bonferroni(p_values):
    n = len(p_values)
    indexed = sorted(enumerate(p_values), key=lambda x: x[1])
    corrected = [None] * n
    cummax = 0.0
    for rank, (orig_idx, p) in enumerate(indexed):
        adjusted = p * (n - rank)
        adjusted = max(adjusted, cummax)
        adjusted = min(adjusted, 1.0)
        cummax = adjusted
        corrected[orig_idx] = adjusted
    return corrected


def run_pairwise(data, metric, strategies):
    pairs = list(combinations(strategies, 2))
    raw_ps = []
    results = []

    for s1, s2 in pairs:
        x = np.array(data[s1][metric])
        y = np.array(data[s2][metric])
        t_stat, p_val = stats.ttest_rel(x, y)
        d = cohens_d_paired(x, y)
        raw_ps.append(p_val)
        results.append({
            "pair": [s1, s2],
            "mean_diff": float(np.mean(x - y)),
            "t_stat": float(t_stat),
            "raw_p": float(p_val),
            "cohens_d": float(d),
        })

    corrected = holm_bonferroni(raw_ps)
    for i, r in enumerate(results):
        r["corrected_p"] = float(corrected[i])
        r["significant"] = bool(corrected[i] < 0.05)

    results.sort(key=lambda r: r["raw_p"])
    return results


def summarize(mmlu_res, hswag_res):
    sig_mmlu = [r for r in mmlu_res if r["significant"]]
    sig_hswag = [r for r in hswag_res if r["significant"]]
    lines = []
    lines.append(f"MMLU: {len(sig_mmlu)}/{len(mmlu_res)} pairs significant after Holm-Bonferroni correction.")
    lines.append(f"HellaSwag: {len(sig_hswag)}/{len(hswag_res)} pairs significant after Holm-Bonferroni correction.")

    top_mmlu = sorted(mmlu_res, key=lambda r: abs(r["cohens_d"]), reverse=True)[:3]
    lines.append("Largest MMLU effect sizes: " + "; ".join(
        f"{r['pair'][0]} vs {r['pair'][1]} (d={r['cohens_d']:.2f}, p_corr={r['corrected_p']:.4f})"
        for r in top_mmlu
    ))
    top_hswag = sorted(hswag_res, key=lambda r: abs(r["cohens_d"]), reverse=True)[:3]
    lines.append("Largest HellaSwag effect sizes: " + "; ".join(
        f"{r['pair'][0]} vs {r['pair'][1]} (d={r['cohens_d']:.2f}, p_corr={r['corrected_p']:.4f})"
        for r in top_hswag
    ))
    return " ".join(lines)


def main():
    data = load_scores()

    # Print per-strategy means for verification
    print("=== Per-strategy means ===")
    for strat in ALL_STRATEGIES:
        mmlu_mean = np.mean(data[strat]["mmlu"])
        hswag_mean = np.mean(data[strat]["hellaswag"])
        print(f"  {strat:25s}  MMLU={mmlu_mean:.4f}  HellaSwag={hswag_mean:.4f}")

    # Main 6-strategy pairwise (C(6,2)=15 comparisons)
    mmlu_main = run_pairwise(data, "mmlu", MAIN_STRATEGIES)
    hswag_main = run_pairwise(data, "hellaswag", MAIN_STRATEGIES)

    # All 10 strategies pairwise (C(10,2)=45 comparisons) for graduated alpha sweep
    mmlu_all = run_pairwise(data, "mmlu", ALL_STRATEGIES)
    hswag_all = run_pairwise(data, "hellaswag", ALL_STRATEGIES)

    output = {
        "mmlu": {
            "pairwise_comparisons": mmlu_main,
            "correction_method": "Holm-Bonferroni",
            "n_comparisons": len(mmlu_main),
            "n_seeds": len(SEEDS),
            "alpha": 0.05,
        },
        "hellaswag": {
            "pairwise_comparisons": hswag_main,
            "correction_method": "Holm-Bonferroni",
            "n_comparisons": len(hswag_main),
            "n_seeds": len(SEEDS),
            "alpha": 0.05,
        },
        "per_seed_data": {
            strat: {
                "mmlu": data[strat]["mmlu"],
                "hellaswag": data[strat]["hellaswag"],
                "seeds": SEEDS,
            }
            for strat in ALL_STRATEGIES
        },
        "graduated_alpha_sweep": {
            "mmlu": {
                "pairwise_comparisons": [r for r in mmlu_all if any(
                    s.startswith("graduated") for s in r["pair"]
                )],
                "correction_method": "Holm-Bonferroni",
                "n_comparisons": len(mmlu_all),
            },
            "hellaswag": {
                "pairwise_comparisons": [r for r in hswag_all if any(
                    s.startswith("graduated") for s in r["pair"]
                )],
                "correction_method": "Holm-Bonferroni",
                "n_comparisons": len(hswag_all),
            },
        },
        "key_findings": summarize(mmlu_main, hswag_main),
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {OUT_PATH}")

    # Print main comparison table
    print("\n=== MMLU Pairwise (6 main strategies, Holm-Bonferroni corrected) ===")
    print(f"{'Pair':50s} {'mean_diff':>10s} {'t':>8s} {'p_raw':>10s} {'p_corr':>10s} {'d':>8s} {'sig':>5s}")
    for r in mmlu_main:
        pair_str = f"{r['pair'][0]} vs {r['pair'][1]}"
        sig = "*" if r["significant"] else ""
        print(f"{pair_str:50s} {r['mean_diff']:>10.5f} {r['t_stat']:>8.3f} {r['raw_p']:>10.4f} {r['corrected_p']:>10.4f} {r['cohens_d']:>8.3f} {sig:>5s}")

    print("\n=== HellaSwag Pairwise (6 main strategies, Holm-Bonferroni corrected) ===")
    print(f"{'Pair':50s} {'mean_diff':>10s} {'t':>8s} {'p_raw':>10s} {'p_corr':>10s} {'d':>8s} {'sig':>5s}")
    for r in hswag_main:
        pair_str = f"{r['pair'][0]} vs {r['pair'][1]}"
        sig = "*" if r["significant"] else ""
        print(f"{pair_str:50s} {r['mean_diff']:>10.5f} {r['t_stat']:>8.3f} {r['raw_p']:>10.4f} {r['corrected_p']:>10.4f} {r['cohens_d']:>8.3f} {sig:>5s}")


if __name__ == "__main__":
    main()
