#!/usr/bin/env python3
"""Falcon3-7B-Base item-level paired bootstrap for Table 1 CIs.

Computes 95% BCa CI for Δ(d100-d000) and pattern stability.
B=10,000 bootstrap replicates.
"""

import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy import stats as sp_stats

DATA_DIR = Path('/root/autodl-tmp/exp001/eval_results')
DOSAGES = ['d000', 'd005', 'd025', 'd050', 'd100']
BENCHMARKS = ['mmlu', 'arc_challenge']


def load_data(benchmark):
    arrays = {}
    for dose in DOSAGES:
        path = DATA_DIR / f'Falcon3-7B-Base_{dose}_s42_aligned' / 'correctness_matrix.json'
        with open(path) as f:
            data = json.load(f)
        arrays[dose] = np.array(data[benchmark], dtype=np.int8)
    lens = {d: len(a) for d, a in arrays.items()}
    assert len(set(lens.values())) == 1, f"Item count mismatch: {lens}"
    return arrays


def bca_ci(boot_stat, obs_stat, jackknife_stats, alpha=0.05):
    """BCa confidence interval."""
    B = len(boot_stat)
    z0 = sp_stats.norm.ppf(np.mean(boot_stat < obs_stat))

    jack_mean = np.mean(jackknife_stats)
    diff = jack_mean - jackknife_stats
    a_hat = np.sum(diff**3) / (6.0 * (np.sum(diff**2))**1.5 + 1e-12)

    z_alpha_lo = sp_stats.norm.ppf(alpha / 2)
    z_alpha_hi = sp_stats.norm.ppf(1 - alpha / 2)

    def adj(z_a):
        num = z0 + z_a
        return sp_stats.norm.cdf(z0 + num / (1 - a_hat * num))

    p_lo = adj(z_alpha_lo)
    p_hi = adj(z_alpha_hi)

    p_lo = np.clip(p_lo, 0.5 / B, 1 - 0.5 / B)
    p_hi = np.clip(p_hi, 0.5 / B, 1 - 0.5 / B)

    sorted_boot = np.sort(boot_stat)
    ci_lo = sorted_boot[int(p_lo * B)]
    ci_hi = sorted_boot[min(int(p_hi * B), B - 1)]
    return ci_lo, ci_hi


def classify_pattern(accs):
    """Classify dose-response pattern from dict of dosage -> scalar accuracy."""
    delta = accs['d100'] - accs['d000']
    mid_vals = [accs['d005'], accs['d025'], accs['d050']]
    mid_min = min(mid_vals)

    if abs(delta) <= 1.0:
        return 'Immune'
    if delta <= -5.0:
        return 'U-collapse'
    if delta < -1.0:
        if mid_min < accs['d100'] and mid_min < accs['d000']:
            return 'V-recovery'
        return 'U-collapse'
    # delta > 1.0
    first_half = accs['d025'] - accs['d000']
    second_half = accs['d100'] - accs['d025']
    late = accs['d100'] - accs['d050']
    if (first_half > 0 and second_half < first_half * 0.3) or late < 0.5:
        return 'Benefit-sat'
    return 'Benefit'


def classify_vec(accs_dict):
    """Vectorized pattern classification for bootstrap samples."""
    B = len(accs_dict['d000'])
    delta = accs_dict['d100'] - accs_dict['d000']
    mid = np.column_stack([accs_dict['d005'], accs_dict['d025'], accs_dict['d050']])
    mid_min = mid.min(axis=1)

    pat = np.full(B, '', dtype='U15')
    immune = np.abs(delta) <= 1.0
    pat[immune] = 'Immune'
    neg = delta < -1.0
    severe = neg & (delta <= -5.0)
    v_dip = neg & ~severe & (mid_min < accs_dict['d100']) & (mid_min < accs_dict['d000'])
    pat[severe] = 'U-collapse'
    pat[v_dip] = 'V-recovery'
    pat[neg & ~severe & ~v_dip] = 'U-collapse'
    pos = delta > 1.0
    first_half = accs_dict['d025'] - accs_dict['d000']
    second_half = accs_dict['d100'] - accs_dict['d025']
    late = accs_dict['d100'] - accs_dict['d050']
    sat = pos & (((first_half > 0) & (second_half < first_half * 0.3)) | (late < 0.5))
    pat[pos & ~sat] = 'Benefit'
    pat[sat] = 'Benefit-sat'
    return pat


def run_bootstrap(arrays, benchmark, B=10000, seed=42):
    n_items = len(arrays['d000'])
    rng = np.random.default_rng(seed)

    obs_accs = {d: float(arrays[d].mean() * 100.0) for d in DOSAGES}
    obs_delta = obs_accs['d100'] - obs_accs['d000']
    obs_pattern = classify_pattern(obs_accs)

    print(f"\n{'='*60}")
    print(f"Benchmark: {benchmark}  |  N={n_items} items  |  B={B}")
    print(f"Observed accs: " + ", ".join(f"{d}={obs_accs[d]:.2f}%" for d in DOSAGES))
    print(f"Observed Δ(d100-d000) = {obs_delta:+.2f}pp")
    print(f"Observed pattern: {obs_pattern}")
    print(f"{'='*60}")

    idx = rng.integers(0, n_items, size=(B, n_items))

    boot_accs = {}
    for dose in DOSAGES:
        boot_accs[dose] = arrays[dose][idx].mean(axis=1) * 100.0

    boot_deltas = boot_accs['d100'] - boot_accs['d000']

    # Jackknife for BCa
    jack_deltas = np.zeros(n_items)
    for i in range(n_items):
        mask = np.ones(n_items, dtype=bool)
        mask[i] = False
        jack_deltas[i] = (arrays['d100'][mask].mean() - arrays['d000'][mask].mean()) * 100.0

    ci_lo, ci_hi = bca_ci(boot_deltas, obs_delta, jack_deltas)

    # Per-dosage CIs
    dosage_cis = {}
    for dose in DOSAGES:
        boot_d = boot_accs[dose]
        pct_lo = np.percentile(boot_d, 2.5)
        pct_hi = np.percentile(boot_d, 97.5)
        dosage_cis[dose] = (pct_lo, pct_hi)

    # Pattern stability
    boot_patterns = classify_vec(boot_accs)
    from collections import Counter
    pat_counts = Counter(boot_patterns)
    stability = pat_counts[obs_pattern] / B * 100.0

    print(f"\nResults:")
    print(f"  Δ = {obs_delta:+.2f}pp  95% BCa CI: [{ci_lo:+.2f}, {ci_hi:+.2f}]")
    print(f"  Percentile CI: [{np.percentile(boot_deltas, 2.5):+.2f}, {np.percentile(boot_deltas, 97.5):+.2f}]")
    print(f"  Bootstrap Δ mean: {boot_deltas.mean():+.4f}, std: {boot_deltas.std():.4f}")
    print(f"  Pattern stability: {stability:.1f}% ({obs_pattern})")
    print(f"  Pattern distribution: {dict(pat_counts.most_common())}")
    print(f"\n  Per-dosage 95% CIs:")
    for dose in DOSAGES:
        lo, hi = dosage_cis[dose]
        print(f"    {dose}: {obs_accs[dose]:.2f}% [{lo:.2f}, {hi:.2f}]")

    return {
        'benchmark': benchmark,
        'n_items': n_items,
        'B': B,
        'observed_accs': obs_accs,
        'observed_delta': round(obs_delta, 4),
        'observed_pattern': obs_pattern,
        'delta_bca_ci95': [round(ci_lo, 4), round(ci_hi, 4)],
        'delta_pct_ci95': [round(float(np.percentile(boot_deltas, 2.5)), 4),
                           round(float(np.percentile(boot_deltas, 97.5)), 4)],
        'delta_mean': round(float(boot_deltas.mean()), 4),
        'delta_std': round(float(boot_deltas.std()), 4),
        'stability_pct': round(stability, 2),
        'pattern_distribution': {str(k): round(v/B*100, 2) for k, v in pat_counts.most_common()},
        'dosage_ci95': {d: [round(lo, 4), round(hi, 4)] for d, (lo, hi) in dosage_cis.items()},
    }


def main():
    results = {}
    for bench in BENCHMARKS:
        arrays = load_data(bench)
        results[bench] = run_bootstrap(arrays, bench, B=10000, seed=42)

    # Summary for Table 1
    print("\n" + "="*60)
    print("TABLE 1 SUMMARY — Falcon3-7B-Base")
    print("="*60)
    for bench in BENCHMARKS:
        r = results[bench]
        ci = r['delta_bca_ci95']
        print(f"  {bench.upper():20s}: Δ = {r['observed_delta']:+.2f}pp  "
              f"95% CI [{ci[0]:+.2f}, {ci[1]:+.2f}]  "
              f"Pattern: {r['observed_pattern']} ({r['stability_pct']:.1f}% stable)")

    out_path = '/root/contamcal-irt-calibration/artifacts/falcon3_bootstrap_results.json'
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nJSON saved: {out_path}")


if __name__ == '__main__':
    main()
