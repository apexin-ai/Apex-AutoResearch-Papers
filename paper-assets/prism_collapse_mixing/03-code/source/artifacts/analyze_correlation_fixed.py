"""
analyze_correlation.py — Analyze per-example signal correlations across generations.
Reads signals_gen{i}_seed{s}.json files, prints rho trend tables, outputs Pass/Fail verdict.
"""

import os
import json
import glob
import argparse
import numpy as np


def main():
    parser = argparse.ArgumentParser(description="Analyze per-example signal correlations and Pass/Fail")
    parser.add_argument("--results_dir", default="/root/prism_collapse_mixing/results", help="Dir with signal JSONs")
    parser.add_argument("--seeds", type=str, default="42,137", help="Comma-separated seeds")
    args = parser.parse_args()

    seeds = [int(s) for s in args.seeds.split(",")]

    # Load all signal files
    data = {}
    for s in seeds:
        data[s] = {}
        for p in sorted(glob.glob(os.path.join(args.results_dir, f"signals_gen*_seed{s}.json"))):
            with open(p) as f:
                d = json.load(f)
            data[s][d["gen"]] = d

    if not data[seeds[0]]:
        print("No signal files found.")
        return

    gens = sorted(data[seeds[0]].keys())
    analysis = {"seeds": {}, "verdict": None}

    # Per-seed rho trend tables
    for s in seeds:
        print(f"\nSeed {s}:")
        header = f"{'Signal':<20}" + "".join(f"{'Gen'+str(g)+'_rho':>12}" for g in gens) + f"{'Trend':>18}"
        print(header)
        print("-" * len(header))

        seed_result = {"gens": gens, "signals": {}}

        for sig_name, rho_key in [
            ("entropy", "rho_loss_entropy"),
            ("spectral_rank", "rho_loss_spectral_rank"),
        ]:
            rhos = []
            for g in gens:
                r = data[s].get(g, {}).get("correlations", {}).get(rho_key, float("nan"))
                rhos.append(r)

            if len(rhos) >= 2 and abs(rhos[-1]) < abs(rhos[0]):
                trend = "↓ decoupling"
            elif len(rhos) >= 2 and abs(rhos[-1]) > abs(rhos[0]):
                trend = "↑ coupling"
            else:
                trend = "→ stable"

            rho_str = "".join(f"{r:>12.4f}" for r in rhos)
            print(f"{sig_name:<20}{rho_str}{trend:>18}")

            seed_result["signals"][sig_name] = {
                "rhos": {f"gen{g}": round(r, 4) for g, r in zip(gens, rhos)},
                "trend": trend,
            }

        # Corpus-level signals table
        print(f"\n  Corpus-level:")
        for key in ["sigma_spectral_rank", "distinct_1", "distinct_2", "distinct_3"]:
            vals = [data[s].get(g, {}).get("corpus_level", {}).get(key, float("nan")) for g in gens]
            val_str = "".join(f"{v:>12.4f}" for v in vals)
            print(f"    {key:<24}{val_str}")
            seed_result["signals"][key] = {f"gen{g}": round(v, 4) for g, v in zip(gens, vals)}

        # Aggregated means table
        print(f"\n  Aggregated means:")
        for key in ["loss_mean", "entropy_mean", "spectral_rank_mean"]:
            vals = [data[s].get(g, {}).get("aggregated", {}).get(key, float("nan")) for g in gens]
            val_str = "".join(f"{v:>12.4f}" for v in vals)
            print(f"    {key:<24}{val_str}")
            seed_result["signals"][key] = {f"gen{g}": round(v, 4) for g, v in zip(gens, vals)}

        analysis["seeds"][str(s)] = seed_result

    # === Pass/Fail Judgment ===
    print(f"\n{'=' * 60}")
    print("=== PASS/FAIL JUDGMENT ===")
    print(f"{'=' * 60}")

    seed_passes = {}
    for s in seeds:
        passes = []
        for sig_name, rho_key in [
            ("entropy", "rho_loss_entropy"),
            ("spectral_rank", "rho_loss_spectral_rank"),
        ]:
            rhos = [data[s].get(g, {}).get("correlations", {}).get(rho_key, float("nan")) for g in gens]

            # Condition 1: last gen |rho| < 0.5 AND (gen0 or gen1) |rho| > 0.7
            cond1 = False
            if len(gens) >= 2:
                last_rho = abs(rhos[-1]) if not np.isnan(rhos[-1]) else 1.0
                early_rhos = [abs(rhos[i]) for i in range(min(2, len(rhos))) if not np.isnan(rhos[i])]
                early_max = max(early_rhos) if early_rhos else 0.0
                cond1 = last_rho < 0.5 and early_max > 0.7

            # Condition 2: |ρ| monotonically decreases, drop >= 15%
            cond2 = False
            abs_rhos = [abs(r) for r in rhos if not np.isnan(r)]
            if len(abs_rhos) >= 2 and abs_rhos[0] != 0:
                monotonic_decrease = all(abs_rhos[i] >= abs_rhos[i + 1] for i in range(len(abs_rhos) - 1))
                drop_frac = (abs_rhos[0] - abs_rhos[-1]) / abs_rhos[0]
                cond2 = monotonic_decrease and drop_frac >= 0.15

            sig_pass = cond1 and cond2
            passes.append(sig_pass)
            c1_mark = "Y" if cond1 else "N"
            c2_mark = "Y" if cond2 else "N"
            verdict_mark = "PASS" if sig_pass else "FAIL"
            print(f"  Seed {s}, {sig_name}: cond1_rho_drop={c1_mark}, cond2_abs_rho_decay={c2_mark} -> {verdict_mark}")

        seed_passes[s] = any(passes)
        print(f"  Seed {s} overall: {'PASS' if seed_passes[s] else 'FAIL'}")

    all_pass = all(seed_passes.values())
    any_pass = any(seed_passes.values())

    if all_pass:
        verdict = "PASS"
    elif any_pass:
        verdict = "WEAK_PASS"
    else:
        verdict = "FAIL"

    print(f"\n  >>> VERDICT: {verdict} <<<")
    analysis["verdict"] = verdict
    analysis["seed_passes"] = {str(s): v for s, v in seed_passes.items()}

    out_path = os.path.join(args.results_dir, "correlation_analysis.json")
    with open(out_path, "w") as f:
        json.dump(analysis, f, indent=2)
    print(f"\nAnalysis saved to {out_path}")


if __name__ == "__main__":
    main()
