import argparse
import json
import numpy as np
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description="Bootstrap CI & effect size analysis for downstream experiments.")
    parser.add_argument("--seeds", type=int, nargs="+", default=[42, 123, 456])
    parser.add_argument("--base-dir", default="/root/autodl-tmp/gen-depth-fingerprint/experiments/downstream")
    parser.add_argument("--n-boot", type=int, default=10000)
    parser.add_argument("--random-seed", type=int, default=2026)
    return parser.parse_args()


args = parse_args()
np.random.seed(args.random_seed)
N_BOOT = args.n_boot

BASE = Path(args.base_dir)
VARIANTS = {
    "all":              args.seeds,
    "size_matched":     args.seeds,
    "depth01":          args.seeds,
    "binary_filtered":  args.seeds,
    "depth0_only":      args.seeds,
}

# Load all PPL values
data = {}
for v, seeds in VARIANTS.items():
    data[v] = {}
    for s in seeds:
        with open(BASE / f"{v}_seed{s}" / "results.json") as f:
            r = json.load(f)
            data[v][s] = r["eval_perplexity"]

print("=" * 70)
print("DOWNSTREAM BOOTSTRAP CI & EFFECT SIZE ANALYSIS")
print("=" * 70)

# 1. Per-variant stats with bootstrap CI
print("\n1. PER-VARIANT BOOTSTRAP 95% CI (seed-level, n=3)")
print("-" * 60)
print(f"{'Variant':<20} {'Mean':>8} {'Std':>8} {'Boot 95% CI':>22}  Seeds")
print("-" * 70)

vstats = {}
for v in ["all", "size_matched", "depth01", "binary_filtered", "depth0_only"]:
    vals = np.array([data[v][s] for s in VARIANTS[v]])
    mean = vals.mean()
    std = vals.std(ddof=1)
    # Bootstrap CI on the mean
    boot_means = np.array([
        np.random.choice(vals, size=len(vals), replace=True).mean()
        for _ in range(N_BOOT)
    ])
    ci_lo, ci_hi = np.percentile(boot_means, [2.5, 97.5])
    vstats[v] = dict(mean=mean, std=std, ci_lo=ci_lo, ci_hi=ci_hi, vals=vals)
    seeds_str = ", ".join(f"{x:.4f}" for x in vals)
    print(f"{v:<20} {mean:>8.4f} {std:>8.5f} [{ci_lo:.4f}, {ci_hi:.4f}]  {seeds_str}")

print(f"\nNote: with n=3, bootstrap resamples have only 10 distinct mean values.")
print(f"CIs appear narrow because cross-seed variance is <0.001, not because n is large.")

# 2. Paired comparisons: bootstrap CI on differences + effect sizes
print("\n\n2. PAIRED BOOTSTRAP TESTS & EFFECT SIZES")
print("-" * 60)

comparisons = [
    ("size_matched", "depth01",          "Size-matched vs Depth 0-1"),
    ("size_matched", "binary_filtered",  "Size-matched vs Binary-filtered"),
    ("depth01",      "binary_filtered",  "Depth 0-1 vs Binary-filtered"),
    ("all",          "size_matched",     "All data vs Size-matched"),
]

results_out = {}
for v1, v2, desc in comparisons:
    vals1 = np.array([data[v1][s] for s in args.seeds])
    vals2 = np.array([data[v2][s] for s in args.seeds])
    diffs = vals1 - vals2  # negative = v1 better (lower PPL)
    
    mean_diff = diffs.mean()
    sd_diff = diffs.std(ddof=1)
    
    # Bootstrap CI on paired differences
    boot_diffs = np.array([
        np.random.choice(diffs, size=len(diffs), replace=True).mean()
        for _ in range(N_BOOT)
    ])
    ci_lo, ci_hi = np.percentile(boot_diffs, [2.5, 97.5])
    
    # Two-sided bootstrap p-value
    if mean_diff > 0:
        p = 2 * (boot_diffs <= 0).mean()
    else:
        p = 2 * (boot_diffs >= 0).mean()
    p = min(p, 1.0)
    
    # Cohen's d (paired)
    d = mean_diff / sd_diff if sd_diff > 0 else float('inf')
    
    # Hedges' g correction for small samples
    # g = d * (1 - 3/(4*df - 1)) where df = n-1
    df = len(diffs) - 1
    g = d * (1 - 3 / (4 * df - 1))
    
    # CI excludes 0?
    sig = ci_lo > 0 or ci_hi < 0
    
    winner = v1 if mean_diff < 0 else v2
    
    results_out[(v1, v2)] = dict(
        mean_diff=mean_diff, sd_diff=sd_diff, 
        ci_lo=ci_lo, ci_hi=ci_hi, p=p, d=d, g=g, sig=sig
    )
    
    print(f"\n  {desc}")
    print(f"    Per-seed diffs ({v1} - {v2}): {', '.join(f'{x:+.4f}' for x in diffs)}")
    print(f"    Mean diff:    {mean_diff:+.4f}")
    print(f"    SD(diff):     {sd_diff:.5f}")
    print(f"    Boot 95% CI:  [{ci_lo:+.5f}, {ci_hi:+.5f}]")
    print(f"    Boot p-value: {p:.3f}")
    print(f"    CI excludes 0: {'YES' if sig else 'NO'}")
    print(f"    Cohen's d:    {d:+.1f}")
    print(f"    Hedges' g:    {g:+.1f}")
    print(f"    → {winner} has lower PPL by {abs(mean_diff):.4f}")

# 3. Summary for paper
print("\n\n3. NUMBERS FOR PAPER")
print("=" * 70)

sm = vstats["size_matched"]
d01 = vstats["depth01"]
bf = vstats["binary_filtered"]
r = results_out[("size_matched", "depth01")]

print(f"\nSize-matched: {sm['mean']:.3f} (95% boot CI [{sm['ci_lo']:.3f}, {sm['ci_hi']:.3f}])")
print(f"Depth 0-1:    {d01['mean']:.3f} (95% boot CI [{d01['ci_lo']:.3f}, {d01['ci_hi']:.3f}])")
print(f"Binary-filt:  {bf['mean']:.3f} (95% boot CI [{bf['ci_lo']:.3f}, {bf['ci_hi']:.3f}])")
print(f"\nPaired diff (size_matched - depth01): {r['mean_diff']:+.4f}")
print(f"  95% boot CI: [{r['ci_lo']:+.5f}, {r['ci_hi']:+.5f}]")
print(f"  Cohen's d = {r['d']:+.1f}, Hedges' g = {r['g']:+.1f}")
print(f"  (Large d reflects near-zero seed variance, not large practical effect)")
print(f"\nLimitation: n=3 seeds → only 10 distinct bootstrap means.")
print(f"Document-level bootstrap not possible (no per-sample losses saved).")

