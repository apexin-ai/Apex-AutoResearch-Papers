import json, numpy as np
from pathlib import Path

np.random.seed(2026)

BASE = Path("/root/autodl-tmp/gen-depth-fingerprint/experiments/downstream")
VARIANTS = ["all", "size_matched", "depth01", "binary_filtered", "depth0_only"]
SEEDS = [42, 123, 456]

data = {}
for v in VARIANTS:
    data[v] = {}
    for s in SEEDS:
        with open(BASE / f"{v}_seed{s}" / "results.json") as f:
            data[v][s] = json.load(f)["eval_perplexity"]

lines = []
def log(s=""):
    print(s)
    lines.append(s)

log("=" * 70)
log("Plan-004-v2 Downstream Perplexity Analysis")
log("=" * 70)

# 1. Ranking + bootstrap CI
log("\n1. PERPLEXITY RANKING WITH 95% BOOTSTRAP CI")
log("-" * 50)

vstats = {}
for v in VARIANTS:
    vals = np.array([data[v][s] for s in SEEDS])
    boot = [np.random.choice(vals, size=3, replace=True).mean() for _ in range(1000)]
    boot = np.array(boot)
    vstats[v] = {"mean": vals.mean(), "ci_lo": np.percentile(boot, 2.5),
                 "ci_hi": np.percentile(boot, 97.5), "vals": vals}

ranked = sorted(vstats.items(), key=lambda x: x[1]["mean"])
log(f"{'Rank':<5} {'Variant':<20} {'Mean PPL':<12} {'95% CI':<24} {'Seeds (per-seed PPL)'}")
log("-" * 90)
for i, (v, st) in enumerate(ranked, 1):
    seeds_str = ", ".join(f"{x:.4f}" for x in st["vals"])
    log(f"{i:<5} {v:<20} {st['mean']:<12.4f} [{st['ci_lo']:.4f}, {st['ci_hi']:.4f}]     {seeds_str}")

log("\nSample sizes per variant:")
for v in VARIANTS:
    with open(BASE / f"{v}_seed42" / "results.json") as f:
        n = json.load(f)["train_samples"]
    log(f"  {v}: {n}")

# 2. Paired bootstrap
log("\n\n2. PAIRED BOOTSTRAP SIGNIFICANCE TESTS")
log("-" * 50)
log("Method: paired bootstrap on per-seed PPL differences (1000 resamples)")
log("Convention: diff = A - B. Negative diff means A has lower (better) PPL.")
log("n=3 seeds → only 2^3=8 distinct bootstrap patterns; CIs are coarse.\n")

comparisons = [
    ("size_matched", "depth01", "Random vs depth-aware (same N=3951)"),
    ("size_matched", "binary_filtered", "Random vs detector-based (same N=3951)"),
    ("depth01", "binary_filtered", "Depth-aware vs detector-based"),
    ("all", "size_matched", "Full data (12299) vs size-matched (3951)"),
]

cresults = {}
for v1, v2, desc in comparisons:
    diffs = np.array([data[v1][s] - data[v2][s] for s in SEEDS])
    obs = diffs.mean()
    boot = [np.random.choice(diffs, size=3, replace=True).mean() for _ in range(1000)]
    boot = np.array(boot)
    ci_lo, ci_hi = np.percentile(boot, 2.5), np.percentile(boot, 97.5)
    # two-sided p
    if obs > 0:
        p = 2 * (boot <= 0).mean()
    else:
        p = 2 * (boot >= 0).mean()
    p = min(p, 1.0)
    sig = ci_lo > 0 or ci_hi < 0
    cresults[(v1,v2)] = dict(obs=obs, ci_lo=ci_lo, ci_hi=ci_hi, p=p, sig=sig, diffs=diffs)

    # direction interpretation (lower PPL = better)
    if obs < 0:
        winner = v1
        interp = f"{v1} is BETTER (lower PPL) by {abs(obs):.4f}"
    else:
        winner = v2
        interp = f"{v2} is BETTER (lower PPL) by {abs(obs):.4f}"

    log(f"  {desc}")
    log(f"    {v1} − {v2}")
    log(f"    Per-seed diffs: {', '.join(f'{d:+.4f}' for d in diffs)}")
    log(f"    Mean diff: {obs:+.4f}")
    log(f"    95% CI: [{ci_lo:+.4f}, {ci_hi:+.4f}]")
    log(f"    p-value: {p:.3f}  |  CI excludes 0: {'YES' if sig else 'NO'}")
    log(f"    → {interp}")
    log()

# 3. Effect sizes
log("\n3. EFFECT SIZES (PAIRED COHEN'S d / HEDGES' g)")
log("-" * 50)
log("With n=3, these are unstable. Reported for completeness.\n")
log(f"{'Comparison':<42} {'d':<10} {'g':<10} {'Size'}")
log("-" * 75)
for v1, v2, desc in comparisons:
    diffs = np.array([data[v1][s] - data[v2][s] for s in SEEDS])
    sd = diffs.std(ddof=1)
    d = diffs.mean() / sd if sd > 0 else float('inf')
    g = d * (1 - 3/(4*(3-1)-1))  # Hedges correction
    sz = "negligible" if abs(g)<0.2 else "small" if abs(g)<0.5 else "medium" if abs(g)<0.8 else "large"
    log(f"  {v1} vs {v2:<22} {d:>+8.2f}   {g:>+8.2f}   {sz}")
log("\nNote: extremely large d values reflect very low seed-to-seed variance,")
log("NOT large practical effects. The actual PPL differences are 0.002–0.032.")

# 4. Conclusions
log("\n\n4. CONCLUSIONS")
log("=" * 70)

log("""
IMPORTANT CAVEATS:
- n=3 seeds. Bootstrap with 3 observations has only 8 distinct patterns.
  CIs appear tight because per-seed PPL variance is very low (seeds differ
  by <0.001 within each variant), NOT because we have strong evidence.
- The tight CIs reflect low seed noise, not high confidence in the ranking.
- Practically, all size-matched variants differ by ≤0.022 PPL.
""")

sm, d01, bf = vstats["size_matched"]["mean"], vstats["depth01"]["mean"], vstats["binary_filtered"]["mean"]

log(f"Q1: Does depth-aware filtering (depth01) beat random sampling (size_matched)?")
log(f"    size_matched: {sm:.4f}  vs  depth01: {d01:.4f}")
log(f"    → NO. Random sampling is BETTER by {d01-sm:.4f} PPL.")
log(f"    → Depth-aware curation does NOT help; it slightly hurts.")
log()
log(f"Q2: Does detector-based filtering (binary_filtered) beat random sampling?")
log(f"    size_matched: {sm:.4f}  vs  binary_filtered: {bf:.4f}")
log(f"    → NO. Random sampling is BETTER by {bf-sm:.4f} PPL.")
log()
log(f"Q3: Depth-aware vs detector-based filtering?")
log(f"    depth01: {d01:.4f}  vs  binary_filtered: {bf:.4f}")
log(f"    → Practically identical (diff = {abs(d01-bf):.4f} PPL).")
log()
log(f"Q4: Does more data help?")
log(f"    all (12299): {vstats['all']['mean']:.4f}  vs  size_matched (3951): {sm:.4f}")
log(f"    → YES. 3x more data gives {sm - vstats['all']['mean']:.4f} PPL improvement.")
log(f"    → This is the largest and most meaningful effect in the experiment.")
log()
log("OVERALL VERDICT:")
log("  The 'depth-aware curation helps' claim is NOT supported.")
log("  Both filtering strategies (depth01, binary_filtered) produce slightly")
log(f"  WORSE perplexity than random sampling at the same data size.")
log(f"  The dominant factor is data QUANTITY, not filtering QUALITY.")
log(f"  Going from 3951→12299 samples gives a {sm - vstats['all']['mean']:.3f} PPL gain,")
log(f"  while the best filtering method differs from random by only {d01-sm:.3f} PPL")
log(f"  (and in the wrong direction).")

out = "/root/gen-depth-fingerprint/artifacts/plan-004-v2/downstream_analysis.txt"
with open(out, "w") as f:
    f.write("\n".join(lines))
log(f"\nSaved to {out}")
