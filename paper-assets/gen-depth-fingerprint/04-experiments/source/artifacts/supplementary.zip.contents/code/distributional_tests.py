"""Location Shift distributional tests: KS (pairwise) + Levene (3-group) on 3-class depth grouping."""

import json
import numpy as np
import pandas as pd
from scipy import stats
from pathlib import Path

DATA_PATH = Path("../data/features_all_models.csv")
OUT_PATH = Path("results/distributional_tests.json")
OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

FEATURES = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max", "tail_decay", "ttr", "hapax_ratio"]
PAIRS = [("gen0", "gen1"), ("gen0", "gen2plus"), ("gen1", "gen2plus")]
N_KS_TESTS = len(FEATURES) * len(PAIRS)
ALPHA = 0.05

df = pd.read_csv(DATA_PATH)

groups = {
    "gen0": df[df["depth"] == 0],
    "gen1": df[df["depth"] == 1],
    "gen2plus": df[df["depth"] >= 2],
}

n_samples = {k: len(v) for k, v in groups.items()}

ks_results = {}
for feat in FEATURES:
    ks_results[feat] = {}
    for g1, g2 in PAIRS:
        stat, p = stats.ks_2samp(groups[g1][feat].dropna(), groups[g2][feat].dropna())
        p_corr = min(p * N_KS_TESTS, 1.0)
        ks_results[feat][f"{g1}_vs_{g2}"] = {
            "statistic": round(stat, 6),
            "p_value": float(f"{p:.6e}"),
            "p_corrected": float(f"{p_corr:.6e}"),
            "significant": bool(p_corr < ALPHA),
        }

levene_results = {}
for feat in FEATURES:
    stat, p = stats.levene(
        groups["gen0"][feat].dropna(),
        groups["gen1"][feat].dropna(),
        groups["gen2plus"][feat].dropna(),
    )
    levene_results[feat] = {
        "statistic": round(stat, 6),
        "p_value": float(f"{p:.6e}"),
        "significant": bool(p < ALPHA),
    }

location_shift_shape_preserved = []
location_shift_shape_shift = []
no_shift = []

for feat in FEATURES:
    any_ks_sig = any(ks_results[feat][f"{g1}_vs_{g2}"]["significant"] for g1, g2 in PAIRS)
    levene_sig = levene_results[feat]["significant"]

    if any_ks_sig and not levene_sig:
        location_shift_shape_preserved.append(feat)
    elif any_ks_sig and levene_sig:
        location_shift_shape_shift.append(feat)
    else:
        no_shift.append(feat)

output = {
    "experiment": "distributional_tests",
    "n_samples": n_samples,
    "ks_tests": ks_results,
    "levene_tests": levene_results,
    "summary": {
        "location_shift_shape_preserved": location_shift_shape_preserved,
        "location_shift_shape_shift": location_shift_shape_shift,
        "no_shift": no_shift,
    },
}

with open(OUT_PATH, "w") as f:
    json.dump(output, f, indent=2)

print(f"N samples: gen0={n_samples['gen0']}, gen1={n_samples['gen1']}, gen2plus={n_samples['gen2plus']}")
print(f"\nBonferroni correction: {N_KS_TESTS} tests, alpha={ALPHA}")
print("\n=== KS Tests (pairwise, corrected p) ===")
for feat in FEATURES:
    sigs = []
    for g1, g2 in PAIRS:
        r = ks_results[feat][f"{g1}_vs_{g2}"]
        marker = "*" if r["significant"] else " "
        sigs.append(f"  {g1} vs {g2}: D={r['statistic']:.4f}, p_corr={r['p_corrected']:.2e} {marker}")
    print(f"\n{feat}:")
    for s in sigs:
        print(s)

print("\n=== Levene's Tests (3-group) ===")
for feat in FEATURES:
    r = levene_results[feat]
    marker = "*" if r["significant"] else " "
    print(f"  {feat}: W={r['statistic']:.4f}, p={r['p_value']:.2e} {marker}")

print("\n=== Summary Classification ===")
print(f"  Location shift + shape preserved: {location_shift_shape_preserved}")
print(f"  Location shift + shape shift:     {location_shift_shape_shift}")
print(f"  No shift:                         {no_shift}")
print(f"\nResults saved to {OUT_PATH}")
