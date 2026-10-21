#!/usr/bin/env python3
"""Robustness analysis for DeiT-S confirmatory correlation."""
import csv
import json
import re
import numpy as np
from scipy import stats

SCAN_CSV = "results/gradient_geometry_deit_small.csv"
SWAP_CSV = "results/deit_weight_swap.csv"
OUTPUT = "results/robustness_analysis.json"
PRIMARY_EPOCH = 5

def load_scan(path):
    data = {}
    with open(path) as f:
        for row in csv.DictReader(f):
            data[(int(row["epoch"]), row["layer_name"])] = {
                "R": float(row["R"]),
                "sr_X": float(row["sr_X"]),
                "delta_grishina": float(row["delta_grishina"]),
            }
    return data

def load_swap(path):
    data = {}
    with open(path) as f:
        for row in csv.DictReader(f):
            if row["group_type"] == "component":
                data[row["group_name"]] = float(row["muon_drop_pp"])
    return data

def scan_to_swap(name):
    m = re.match(r"blocks\.(\d+)\.(.*)", name)
    return f"block_{m.group(1)}.{m.group(2)}" if m else name

def build_matched(scan, swap, epoch):
    layers, margins, drops = [], [], []
    scan_layers = sorted(set(l for _, l in scan.keys()))
    for sl in scan_layers:
        sw = scan_to_swap(sl)
        if sw in swap and (epoch, sl) in scan:
            row = scan[(epoch, sl)]
            margin = row["R"] / (row["delta_grishina"] ** 2 * row["sr_X"])
            layers.append(sw)
            margins.append(margin)
            drops.append(swap[sw])
    return layers, np.array(margins), np.array(drops)

def corr(x, y):
    sr, sp = stats.spearmanr(x, y)
    pr, pp = stats.pearsonr(x, y)
    return {"spearman_rho": round(float(sr), 4), "spearman_p": round(float(sp), 6),
            "pearson_r": round(float(pr), 4), "pearson_p": round(float(pp), 6), "n": len(x)}

def main():
    import os
    os.chdir("/root/spectral_optim_vision_geometry")
    scan = load_scan(SCAN_CSV)
    swap = load_swap(SWAP_CSV)
    layers, margins, drops = build_matched(scan, swap, PRIMARY_EPOCH)
    n = len(layers)
    print(f"Matched layers: {n}")

    full = corr(margins, drops)
    print(f"\nFull correlation (n={n}):")
    print(f"  Spearman rho={full['spearman_rho']}, p={full['spearman_p']}")
    print(f"  Pearson  r={full['pearson_r']}, p={full['pearson_p']}")

    # (a) Check if any patch_embed layer exists in matched set
    patch_idx = [i for i, l in enumerate(layers) if "patch_embed" in l]
    if patch_idx:
        mask = np.ones(n, dtype=bool)
        for i in patch_idx:
            mask[i] = False
        no_patch = corr(margins[mask], drops[mask])
        print(f"\nWithout patch_embed (n={no_patch['n']}):")
        print(f"  Spearman rho={no_patch['spearman_rho']}, p={no_patch['spearman_p']}")
    else:
        no_patch = None
        print("\npatch_embed.proj already excluded from matched set (not a component layer)")

    # (b) Leave-one-out
    print("\n--- Leave-one-out analysis ---")
    loo_results = []
    for i in range(n):
        mask = np.ones(n, dtype=bool)
        mask[i] = False
        sr, _ = stats.spearmanr(margins[mask], drops[mask])
        delta = full["spearman_rho"] - sr
        loo_results.append({
            "layer": layers[i],
            "rho_without": round(float(sr), 4),
            "delta_rho": round(float(delta), 4),
            "margin": round(float(margins[i]), 4),
            "muon_drop_pp": round(float(drops[i]), 4),
        })

    loo_sorted = sorted(loo_results, key=lambda x: abs(x["delta_rho"]), reverse=True)
    print("\nTop-10 most influential layers (|Δρ|):")
    for r in loo_sorted[:10]:
        print(f"  {r['layer']:30s}  Δρ={r['delta_rho']:+.4f}  ρ_without={r['rho_without']:.4f}  "
              f"margin={r['margin']:.2f}  drop={r['muon_drop_pp']:.2f}")

    max_delta = max(abs(r["delta_rho"]) for r in loo_results)
    print(f"\nMax |Δρ| = {max_delta:.4f}")
    rho_range = [min(r["rho_without"] for r in loo_results),
                 max(r["rho_without"] for r in loo_results)]
    print(f"ρ range across LOO: [{rho_range[0]:.4f}, {rho_range[1]:.4f}]")
    print(f"All LOO ρ significant (p<0.05)? ", end="")
    all_sig = all(
        stats.spearmanr(
            np.delete(margins, i), np.delete(drops, i)
        ).pvalue < 0.05
        for i in range(n)
    )
    print("YES" if all_sig else "NO")

    # (c) Bootstrap CI
    print("\n--- Bootstrap confidence interval ---")
    np.random.seed(42)
    n_boot = 10000
    boot_rhos = np.empty(n_boot)
    for b in range(n_boot):
        idx = np.random.randint(0, n, size=n)
        sr, _ = stats.spearmanr(margins[idx], drops[idx])
        boot_rhos[b] = sr
    ci_low, ci_high = np.percentile(boot_rhos, [2.5, 97.5])
    boot_mean = np.mean(boot_rhos)
    boot_std = np.std(boot_rhos)
    print(f"Bootstrap Spearman ρ: mean={boot_mean:.4f}, std={boot_std:.4f}")
    print(f"95% CI: [{ci_low:.4f}, {ci_high:.4f}]")
    print(f"CI includes 0? {'YES' if ci_low <= 0 <= ci_high else 'NO'}")

    # Also bootstrap Pearson
    boot_pearson = np.empty(n_boot)
    for b in range(n_boot):
        idx = np.random.randint(0, n, size=n)
        pr, _ = stats.pearsonr(margins[idx], drops[idx])
        boot_pearson[b] = pr
    pci_low, pci_high = np.percentile(boot_pearson, [2.5, 97.5])
    print(f"\nBootstrap Pearson r: mean={np.mean(boot_pearson):.4f}, std={np.std(boot_pearson):.4f}")
    print(f"95% CI: [{pci_low:.4f}, {pci_high:.4f}]")
    print(f"CI includes 0? {'YES' if pci_low <= 0 <= pci_high else 'NO'}")

    # Save
    output = {
        "analysis": "patch_embed_robustness_check",
        "n_matched_layers": n,
        "full_correlation": full,
        "patch_embed_in_matched_set": bool(patch_idx),
        "without_patch_embed": no_patch,
        "leave_one_out": {
            "max_abs_delta_rho": round(float(max_delta), 4),
            "rho_range": [round(rho_range[0], 4), round(rho_range[1], 4)],
            "all_loo_significant_p05": all_sig,
            "top5_influential": loo_sorted[:5],
            "full_results": loo_sorted,
        },
        "bootstrap": {
            "n_bootstrap": n_boot,
            "seed": 42,
            "spearman": {
                "mean": round(float(boot_mean), 4),
                "std": round(float(boot_std), 4),
                "ci_95_low": round(float(ci_low), 4),
                "ci_95_high": round(float(ci_high), 4),
                "ci_includes_zero": bool(ci_low <= 0 <= ci_high),
            },
            "pearson": {
                "mean": round(float(np.mean(boot_pearson)), 4),
                "std": round(float(np.std(boot_pearson)), 4),
                "ci_95_low": round(float(pci_low), 4),
                "ci_95_high": round(float(pci_high), 4),
                "ci_includes_zero": bool(pci_low <= 0 <= pci_high),
            },
        },
        "conclusion": "",
    }

    # Write conclusion
    robust = (
        not output["patch_embed_in_matched_set"]
        and all_sig
        and max_delta < 0.10
        and not output["bootstrap"]["spearman"]["ci_includes_zero"]
    )
    if robust:
        output["conclusion"] = (
            f"ROBUST. patch_embed.proj was already excluded from the 48-layer matched set "
            f"(it maps to 'special' type, not 'component'). "
            f"LOO: max|Δρ|={max_delta:.4f}, all {n} subsets significant at p<0.05. "
            f"Bootstrap 95% CI for Spearman ρ: [{ci_low:.4f}, {ci_high:.4f}], excludes 0. "
            f"The correlation ρ={full['spearman_rho']} is not driven by any single outlier."
        )
    else:
        reasons = []
        if output["patch_embed_in_matched_set"]:
            reasons.append("patch_embed in matched set")
        if not all_sig:
            reasons.append("some LOO subsets not significant")
        if max_delta >= 0.10:
            reasons.append(f"max|Δρ|={max_delta:.4f} >= 0.10")
        if output["bootstrap"]["spearman"]["ci_includes_zero"]:
            reasons.append("bootstrap CI includes 0")
        output["conclusion"] = f"NOT FULLY ROBUST: {'; '.join(reasons)}"

    print(f"\n=== CONCLUSION ===\n{output['conclusion']}")

    with open(OUTPUT, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved to {OUTPUT}")

if __name__ == "__main__":
    main()
