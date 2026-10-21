#!/usr/bin/env python3
"""exp-011 convergence analysis: cross-architecture std vs attention ratio."""

import json
import os
import sys
import numpy as np
import pandas as pd
from itertools import permutations
from scipy.stats import spearmanr

RESULT_DIR = "/root/entrainment_gated_ft/lm_eval_clean/exp011"
OUTPUT_DIR = "/root/entrainment_gated_ft/analysis"

ARCHITECTURES = ["GatedDeltaNet", "RetNet", "HGRN2"]
ARCH_SHORT = {"GatedDeltaNet": "GDN", "RetNet": "RetNet", "HGRN2": "HGRN2"}

VARIANTS = {
    "pure": 0.0,
    "hybrid-24-1": 1 / 25,
    "hybrid-12-1": 1 / 13,
    "hybrid-6-1": 1 / 7,
    "hybrid-3-1": 1 / 4,
}

BENCHMARKS = ["boolq", "copa", "piqa", "sciq"]
MAIN_BENCHMARKS = ["boolq", "piqa", "sciq"]

# exp-008 prior results (6 benchmarks)
PRIOR_RESULTS = {
    "lambada_openai": {"rho": -1.0, "raw_p": 0.0167},
    "hellaswag":      {"rho": 0.3,  "raw_p": 0.6833},
    "winogrande":     {"rho": 0.1,  "raw_p": 0.95},
    "arc_easy":       {"rho": -0.7, "raw_p": 0.2333},
    "arc_challenge":  {"rho": 0.6,  "raw_p": 0.35},
    "mmlu":           {"rho": -0.7, "raw_p": 0.2333},
}


def exact_spearman_p(x, y):
    rho_obs = spearmanr(x, y).statistic
    n = len(x)
    all_perms = list(permutations(range(n)))
    count = sum(
        1 for perm in all_perms
        if abs(spearmanr(x, [y[i] for i in perm]).statistic) >= abs(rho_obs)
    )
    return rho_obs, count / len(all_perms)


def load_results():
    rows = []
    for arch in ARCHITECTURES:
        for variant, ratio in VARIANTS.items():
            fname = f"1.3B-100B-{arch}-{variant}.json"
            fpath = os.path.join(RESULT_DIR, fname)
            with open(fpath) as f:
                data = json.load(f)
            for bm in BENCHMARKS:
                acc = data["results"][bm]["acc,none"]
                rows.append({
                    "architecture": arch,
                    "arch_short": ARCH_SHORT[arch],
                    "variant": variant,
                    "attention_ratio": ratio,
                    "benchmark": bm,
                    "accuracy": acc,
                })

    # Transformer baseline
    tpath = os.path.join(RESULT_DIR, "transformer_1.3B_baseline.json")
    with open(tpath) as f:
        tdata = json.load(f)
    for bm in BENCHMARKS:
        acc = tdata["results"][bm]["acc,none"]
        rows.append({
            "architecture": "Transformer",
            "arch_short": "Transformer",
            "variant": "baseline",
            "attention_ratio": 1.0,
            "benchmark": bm,
            "accuracy": acc,
        })

    return pd.DataFrame(rows)


def compute_cross_arch_std(df):
    """Compute cross-architecture std at each attention ratio for each benchmark."""
    results = []
    for bm in BENCHMARKS:
        for variant, ratio in VARIANTS.items():
            sub = df[(df["benchmark"] == bm) & (df["variant"] == variant) & (df["architecture"] != "Transformer")]
            accs = {}
            for _, row in sub.iterrows():
                accs[row["arch_short"]] = row["accuracy"]
            std_val = np.std(list(accs.values()), ddof=0)

            # Transformer acc
            t_row = df[(df["benchmark"] == bm) & (df["architecture"] == "Transformer")]
            t_acc = t_row["accuracy"].values[0] if len(t_row) > 0 else None

            results.append({
                "benchmark": bm,
                "attention_ratio": round(ratio, 4),
                "GDN_acc": accs.get("GDN"),
                "RetNet_acc": accs.get("RetNet"),
                "HGRN2_acc": accs.get("HGRN2"),
                "cross_arch_std": round(std_val, 6),
                "Transformer_acc": t_acc,
            })
    return pd.DataFrame(results)


def bh_fdr(pvals):
    """Benjamini-Hochberg FDR correction."""
    n = len(pvals)
    sorted_idx = np.argsort(pvals)
    sorted_p = np.array(pvals)[sorted_idx]
    adjusted = np.zeros(n)
    for i in range(n - 1, -1, -1):
        rank = i + 1
        if i == n - 1:
            adjusted[sorted_idx[i]] = sorted_p[i]
        else:
            adjusted[sorted_idx[i]] = min(adjusted[sorted_idx[i + 1]], sorted_p[i] * n / rank)
    return adjusted.tolist()


def main():
    df = load_results()

    # CSV output
    csv_df = compute_cross_arch_std(df)
    csv_path = os.path.join(OUTPUT_DIR, "exp011_convergence_results.csv")
    csv_df.to_csv(csv_path, index=False)
    print(f"CSV saved: {csv_path}")

    # Spearman analysis per benchmark
    new_results = {}
    for bm in BENCHMARKS:
        bm_csv = csv_df[csv_df["benchmark"] == bm].sort_values("attention_ratio")
        ratios = bm_csv["attention_ratio"].values
        stds = bm_csv["cross_arch_std"].values

        rho, p_exact = exact_spearman_p(ratios.tolist(), stds.tolist())

        std_pure = float(stds[ratios == 0.0][0])
        std_h3_1 = float(stds[np.isclose(ratios, 0.25)][0])
        convergence_ratio = std_pure / std_h3_1 if std_h3_1 > 0 else float("inf")

        new_results[bm] = {
            "rho": round(rho, 4),
            "raw_p": round(p_exact, 4),
            "std_at_pure": round(std_pure, 6),
            "std_at_h3_1": round(std_h3_1, 6),
            "convergence_ratio": round(convergence_ratio, 4),
            "is_copa_supplementary": bm == "copa",
        }

    # Combined multiple comparison correction
    # Main benchmarks: 6 prior + 3 new (boolq, piqa, sciq) = 9
    main_benchmark_names = list(PRIOR_RESULTS.keys()) + MAIN_BENCHMARKS
    main_raw_ps = [PRIOR_RESULTS[b]["raw_p"] for b in PRIOR_RESULTS] + [new_results[b]["raw_p"] for b in MAIN_BENCHMARKS]
    n_main = len(main_raw_ps)  # 9

    # Bonferroni for main
    main_bonf = [min(p * n_main, 1.0) for p in main_raw_ps]
    # BH-FDR for main
    main_bh = bh_fdr(main_raw_ps)

    # Build combined results
    combined = {}
    for i, bname in enumerate(main_benchmark_names):
        if bname in PRIOR_RESULTS:
            combined[bname] = {
                "rho": PRIOR_RESULTS[bname]["rho"],
                "raw_p": PRIOR_RESULTS[bname]["raw_p"],
                "bonferroni_adj_p": round(main_bonf[i], 4),
                "bh_fdr_adj_p": round(main_bh[i], 4),
                "source": "exp-008",
            }
        else:
            combined[bname] = {
                "rho": new_results[bname]["rho"],
                "raw_p": new_results[bname]["raw_p"],
                "bonferroni_adj_p": round(main_bonf[i], 4),
                "bh_fdr_adj_p": round(main_bh[i], 4),
                "std_at_pure": new_results[bname]["std_at_pure"],
                "std_at_h3_1": new_results[bname]["std_at_h3_1"],
                "convergence_ratio": new_results[bname]["convergence_ratio"],
                "source": "exp-011",
            }

    # COPA separate
    copa_result = {
        "rho": new_results["copa"]["rho"],
        "raw_p": new_results["copa"]["raw_p"],
        "bonferroni_adj_p": min(new_results["copa"]["raw_p"] * 1, 1.0),  # only 1 supplementary test
        "std_at_pure": new_results["copa"]["std_at_pure"],
        "std_at_h3_1": new_results["copa"]["std_at_h3_1"],
        "convergence_ratio": new_results["copa"]["convergence_ratio"],
        "is_supplementary": True,
        "note": "n=100, not included in main Bonferroni correction",
        "source": "exp-011",
    }

    # JSON summary
    summary = {
        "n_main_benchmarks": n_main,
        "benchmarks_new": {bm: new_results[bm] for bm in BENCHMARKS},
        "combined_correction": combined,
        "copa_supplementary": copa_result,
    }

    json_path = os.path.join(OUTPUT_DIR, "exp011_convergence_summary.json")
    with open(json_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"JSON saved: {json_path}")

    # Human-readable summary
    print("\n" + "=" * 70)
    print("EXP-011 CONVERGENCE ANALYSIS SUMMARY")
    print("=" * 70)

    print("\n--- New Benchmarks (exp-011) ---")
    for bm in BENCHMARKS:
        r = new_results[bm]
        tag = " [SUPPLEMENTARY, n=100]" if bm == "copa" else ""
        print(f"  {bm:10s}: ρ={r['rho']:+.4f}, exact_p={r['raw_p']:.4f}, "
              f"std_pure={r['std_at_pure']:.6f}, std_h3-1={r['std_at_h3_1']:.6f}, "
              f"conv_ratio={r['convergence_ratio']:.2f}{tag}")

    print(f"\n--- Combined {n_main}-Benchmark Correction (Bonferroni & BH-FDR) ---")
    print(f"  {'benchmark':20s} {'ρ':>7s} {'raw_p':>8s} {'bonf_p':>8s} {'bh_fdr_p':>8s} {'sig?':>5s}")
    sig_count = 0
    for bname in main_benchmark_names:
        c = combined[bname]
        sig = "YES" if c["bonferroni_adj_p"] < 0.05 else "no"
        if c["bonferroni_adj_p"] < 0.05:
            sig_count += 1
        print(f"  {bname:20s} {c['rho']:+7.4f} {c['raw_p']:8.4f} {c['bonferroni_adj_p']:8.4f} {c['bh_fdr_adj_p']:8.4f} {sig:>5s}")

    print(f"\n  COPA (supplementary): ρ={copa_result['rho']:+.4f}, raw_p={copa_result['raw_p']:.4f} "
          f"(not in main correction, n=100)")

    print(f"\n--- Key Finding ---")
    sig_names = [b for b in main_benchmark_names if combined[b]["bonferroni_adj_p"] < 0.05]
    if len(sig_names) >= 2:
        print(f"  FOUND {len(sig_names)} significant anchors after Bonferroni: {sig_names}")
    elif len(sig_names) == 1:
        print(f"  Only 1 significant anchor after Bonferroni: {sig_names}")
        print(f"  No second significant anchor found.")
    else:
        print(f"  No benchmarks significant after Bonferroni correction (α=0.05).")

    # Check BH-FDR
    bh_sig = [b for b in main_benchmark_names if combined[b]["bh_fdr_adj_p"] < 0.05]
    if len(bh_sig) != len(sig_names):
        print(f"  Under BH-FDR: {len(bh_sig)} significant: {bh_sig}")

    print("\nTransformer baseline (excluded from Spearman):")
    for bm in BENCHMARKS:
        t_row = csv_df[(csv_df["benchmark"] == bm)]
        t_acc = df[(df["architecture"] == "Transformer") & (df["benchmark"] == bm)]["accuracy"].values[0]
        print(f"  {bm:10s}: {t_acc:.4f}")


if __name__ == "__main__":
    main()
