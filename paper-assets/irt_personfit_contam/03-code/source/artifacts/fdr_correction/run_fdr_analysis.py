"""BH-FDR multiple testing correction for cross-benchmark person-fit analysis."""

import json
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.stats.multitest import multipletests
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BASE = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts"
OUT = f"{BASE}/fdr_correction"

# =============================================================================
# Part A: Real data FDR correction (60 cells)
# =============================================================================

matrix = pd.read_csv(f"{BASE}/phase_b_two_sided_v2/personfit_matrix_v2.csv")
null_bias = pd.read_csv(f"{BASE}/empirical_null_analysis/null_bias_table.csv")
null_bias = null_bias[~null_bias['model'].str.startswith('[')]

real = matrix[['model_name', 'benchmark', 'lz_star']].rename(columns={'model_name': 'model'})

real = real.merge(
    null_bias[['model', 'benchmark', 'null_mean', 'null_std']],
    on=['model', 'benchmark'], how='left'
)

# Method 1: Standard normal p-values (theoretical null)
real['p_theoretical'] = 2 * stats.norm.sf(np.abs(real['lz_star']))

# Method 2: Empirical null-corrected p-values
real['z_corrected'] = (real['lz_star'] - real['null_mean']) / real['null_std']
real['p_empirical'] = 2 * stats.norm.sf(np.abs(real['z_corrected']))

# Global BH-FDR and Bonferroni across all 60 cells
for p_col, prefix in [('p_theoretical', 'theo'), ('p_empirical', 'emp')]:
    pvals = real[p_col].values

    # BH-FDR
    reject_bh, padj_bh, _, _ = multipletests(pvals, alpha=0.05, method='fdr_bh')
    real[f'{prefix}_bh_p'] = padj_bh
    real[f'{prefix}_bh_flag'] = reject_bh

    # Bonferroni
    reject_bonf, padj_bonf, _, _ = multipletests(pvals, alpha=0.05, method='bonferroni')
    real[f'{prefix}_bonf_p'] = padj_bonf
    real[f'{prefix}_bonf_flag'] = reject_bonf

# Uncorrected flags at alpha=0.05
real['theo_raw_flag'] = real['p_theoretical'] < 0.05
real['emp_raw_flag'] = real['p_empirical'] < 0.05

real.to_csv(f"{OUT}/fdr_real_data.csv", index=False)

# Summary stats
def count_flags(col):
    return int(real[col].sum())

summary = {
    "total_cells": 60,
    "theoretical_null": {
        "uncorrected_flagged": count_flags('theo_raw_flag'),
        "bh_fdr_flagged": count_flags('theo_bh_flag'),
        "bonferroni_flagged": count_flags('theo_bonf_flag'),
    },
    "empirical_null": {
        "uncorrected_flagged": count_flags('emp_raw_flag'),
        "bh_fdr_flagged": count_flags('emp_bh_flag'),
        "bonferroni_flagged": count_flags('emp_bonf_flag'),
    },
    "cells_lost_bh_theoretical": count_flags('theo_raw_flag') - count_flags('theo_bh_flag'),
    "cells_lost_bh_empirical": count_flags('emp_raw_flag') - count_flags('emp_bh_flag'),
    "cells_lost_bonf_theoretical": count_flags('theo_raw_flag') - count_flags('theo_bonf_flag'),
    "cells_lost_bonf_empirical": count_flags('emp_raw_flag') - count_flags('emp_bonf_flag'),
}

# Cells that flip under BH
flipped_bh_emp = real[real['emp_raw_flag'] & ~real['emp_bh_flag']][['model', 'benchmark', 'lz_star', 'p_empirical', 'emp_bh_p']]
summary["flipped_cells_bh_empirical"] = flipped_bh_emp.to_dict('records') if len(flipped_bh_emp) > 0 else []

flipped_bonf_emp = real[real['emp_raw_flag'] & ~real['emp_bonf_flag']][['model', 'benchmark', 'lz_star', 'p_empirical', 'emp_bonf_p']]
summary["flipped_cells_bonf_empirical"] = flipped_bonf_emp.to_dict('records') if len(flipped_bonf_emp) > 0 else []

# Min/max p-values for context
summary["p_value_range"] = {
    "empirical_raw_min": float(real['p_empirical'].min()),
    "empirical_raw_max": float(real['p_empirical'].max()),
    "empirical_raw_median": float(real['p_empirical'].median()),
    "empirical_bh_max": float(real['emp_bh_p'].max()),
}

print("=== Part A: Real Data FDR Correction ===")
print(f"Theoretical null: uncorrected={summary['theoretical_null']['uncorrected_flagged']}, "
      f"BH={summary['theoretical_null']['bh_fdr_flagged']}, "
      f"Bonferroni={summary['theoretical_null']['bonferroni_flagged']}")
print(f"Empirical null:   uncorrected={summary['empirical_null']['uncorrected_flagged']}, "
      f"BH={summary['empirical_null']['bh_fdr_flagged']}, "
      f"Bonferroni={summary['empirical_null']['bonferroni_flagged']}")

# =============================================================================
# Part B: Simulation FDR correction
# =============================================================================

sim = pd.read_csv(f"{BASE}/extended_simulation/simulation_detailed.csv")

benchmarks = sim['benchmark'].unique()
contam_levels = sorted(sim['contamination_pct'].unique())

sim_results = []

for contam in contam_levels:
    sub = sim[sim['contamination_pct'] == contam].copy()

    # p-values from theoretical null (two-sided)
    sub['p_raw'] = 2 * stats.norm.sf(np.abs(sub['lz_star']))

    # Within each contamination level, group by sim_idx and apply BH across benchmarks
    # Each sim_idx has 5 benchmark values -> family of 5 tests
    # But more natural: for each (benchmark, contam_pct), pool all 200 sims
    # The reviewer concern is about 60 cells (model × benchmark), so for simulation
    # we correct across benchmarks within each sim run

    for bench in benchmarks:
        bsub = sub[sub['benchmark'] == bench]
        n_total = len(bsub)
        if n_total == 0:
            continue

        pvals = bsub['p_raw'].values

        # Uncorrected rejection rate
        raw_reject_rate = np.mean(pvals < 0.05)

        # BH-FDR within this (benchmark, contam) group
        if len(pvals) > 0:
            reject_bh, padj_bh, _, _ = multipletests(pvals, alpha=0.05, method='fdr_bh')
            bh_reject_rate = np.mean(reject_bh)

            reject_bonf, padj_bonf, _, _ = multipletests(pvals, alpha=0.05, method='bonferroni')
            bonf_reject_rate = np.mean(reject_bonf)
        else:
            bh_reject_rate = bonf_reject_rate = 0

        sim_results.append({
            'benchmark': bench,
            'contamination_pct': contam,
            'n_sims': n_total,
            'raw_reject_rate': raw_reject_rate,
            'bh_reject_rate': bh_reject_rate,
            'bonf_reject_rate': bonf_reject_rate,
        })

    # Also: cross-benchmark correction per sim run
    for sidx in sub['sim_idx'].unique():
        ssub = sub[sub['sim_idx'] == sidx]
        if len(ssub) < 2:
            continue
        pvals_cross = 2 * stats.norm.sf(np.abs(ssub['lz_star'].values))
        reject_bh_cross, _, _, _ = multipletests(pvals_cross, alpha=0.05, method='fdr_bh')
        reject_bonf_cross, _, _, _ = multipletests(pvals_cross, alpha=0.05, method='bonferroni')

        for i, (_, row) in enumerate(ssub.iterrows()):
            p_raw = 2 * stats.norm.sf(np.abs(row['lz_star']))
            # Store per-observation cross-benchmark corrected results
            # (used for aggregation below)

sim_fdr = pd.DataFrame(sim_results)
sim_fdr.to_csv(f"{OUT}/fdr_simulation.csv", index=False)

# Cross-benchmark correction: for each sim run, correct across 5 benchmarks
cross_results = []
for contam in contam_levels:
    sub = sim[sim['contamination_pct'] == contam].copy()
    sub['p_raw'] = 2 * stats.norm.sf(np.abs(sub['lz_star']))

    raw_by_bench = {}
    bh_by_bench = {}
    bonf_by_bench = {}
    for bench in benchmarks:
        raw_by_bench[bench] = []
        bh_by_bench[bench] = []
        bonf_by_bench[bench] = []

    for sidx in sub['sim_idx'].unique():
        ssub = sub[sub['sim_idx'] == sidx].sort_values('benchmark')
        if len(ssub) != len(benchmarks):
            continue
        pvals = ssub['p_raw'].values
        reject_bh, _, _, _ = multipletests(pvals, alpha=0.05, method='fdr_bh')
        reject_bonf, _, _, _ = multipletests(pvals, alpha=0.05, method='bonferroni')

        for j, bench in enumerate(ssub['benchmark'].values):
            raw_by_bench[bench].append(pvals[j] < 0.05)
            bh_by_bench[bench].append(reject_bh[j])
            bonf_by_bench[bench].append(reject_bonf[j])

    for bench in benchmarks:
        if len(raw_by_bench[bench]) > 0:
            cross_results.append({
                'benchmark': bench,
                'contamination_pct': contam,
                'n_sims': len(raw_by_bench[bench]),
                'raw_reject_rate': np.mean(raw_by_bench[bench]),
                'bh_cross_reject_rate': np.mean(bh_by_bench[bench]),
                'bonf_cross_reject_rate': np.mean(bonf_by_bench[bench]),
            })

cross_fdr = pd.DataFrame(cross_results)
cross_fdr.to_csv(f"{OUT}/fdr_simulation_cross_benchmark.csv", index=False)

print("\n=== Part B: Simulation FDR (contam=0, Type I error) ===")
type1 = sim_fdr[sim_fdr['contamination_pct'] == 0]
print(type1[['benchmark', 'raw_reject_rate', 'bh_reject_rate', 'bonf_reject_rate']].to_string(index=False))

summary["simulation_type1_error"] = {}
for _, row in type1.iterrows():
    summary["simulation_type1_error"][row['benchmark']] = {
        "raw": round(row['raw_reject_rate'], 4),
        "bh_fdr": round(row['bh_reject_rate'], 4),
        "bonferroni": round(row['bonf_reject_rate'], 4),
    }

# Cross-benchmark type I error
cross_type1 = cross_fdr[cross_fdr['contamination_pct'] == 0]
print("\n=== Part B: Cross-benchmark correction (contam=0, Type I) ===")
print(cross_type1[['benchmark', 'raw_reject_rate', 'bh_cross_reject_rate', 'bonf_cross_reject_rate']].to_string(index=False))

summary["simulation_cross_benchmark_type1"] = {}
for _, row in cross_type1.iterrows():
    summary["simulation_cross_benchmark_type1"][row['benchmark']] = {
        "raw": round(row['raw_reject_rate'], 4),
        "bh_cross": round(row['bh_cross_reject_rate'], 4),
        "bonf_cross": round(row['bonf_cross_reject_rate'], 4),
    }

# =============================================================================
# Part C: Power comparison figure
# =============================================================================

fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

# Panel 1: Within-benchmark correction power curves (averaged across benchmarks)
avg_power = sim_fdr.groupby('contamination_pct')[['raw_reject_rate', 'bh_reject_rate', 'bonf_reject_rate']].mean().reset_index()

ax = axes[0]
ax.plot(avg_power['contamination_pct'], avg_power['raw_reject_rate'], 'o-', label='Uncorrected', color='#2196F3', linewidth=2)
ax.plot(avg_power['contamination_pct'], avg_power['bh_reject_rate'], 's-', label='BH-FDR', color='#FF9800', linewidth=2)
ax.plot(avg_power['contamination_pct'], avg_power['bonf_reject_rate'], '^-', label='Bonferroni', color='#F44336', linewidth=2)
ax.axhline(0.05, ls='--', color='gray', alpha=0.5, label='α = 0.05')
ax.set_xlabel('Contamination %', fontsize=12)
ax.set_ylabel('Rejection Rate', fontsize=12)
ax.set_title('(a) Within-Benchmark Correction\n(averaged across 5 benchmarks)', fontsize=12)
ax.legend(fontsize=10)
ax.set_ylim(-0.02, 1.05)
ax.grid(alpha=0.3)

# Panel 2: Cross-benchmark correction power curves (averaged across benchmarks)
avg_cross = cross_fdr.groupby('contamination_pct')[['raw_reject_rate', 'bh_cross_reject_rate', 'bonf_cross_reject_rate']].mean().reset_index()

ax = axes[1]
ax.plot(avg_cross['contamination_pct'], avg_cross['raw_reject_rate'], 'o-', label='Uncorrected', color='#2196F3', linewidth=2)
ax.plot(avg_cross['contamination_pct'], avg_cross['bh_cross_reject_rate'], 's-', label='BH-FDR (cross-bench)', color='#FF9800', linewidth=2)
ax.plot(avg_cross['contamination_pct'], avg_cross['bonf_cross_reject_rate'], '^-', label='Bonferroni (cross-bench)', color='#F44336', linewidth=2)
ax.axhline(0.05, ls='--', color='gray', alpha=0.5, label='α = 0.05')
ax.set_xlabel('Contamination %', fontsize=12)
ax.set_ylabel('Rejection Rate', fontsize=12)
ax.set_title('(b) Cross-Benchmark Correction\n(5-test family per simulation run)', fontsize=12)
ax.legend(fontsize=10)
ax.set_ylim(-0.02, 1.05)
ax.grid(alpha=0.3)

plt.tight_layout()
plt.savefig(f"{OUT}/fdr_power_comparison.png", dpi=200, bbox_inches='tight')
plt.close()
print(f"\nSaved power comparison figure.")

# =============================================================================
# Additional figure: per-benchmark power curves
# =============================================================================

fig, axes = plt.subplots(1, 5, figsize=(22, 4.5), sharey=True)
for i, bench in enumerate(sorted(benchmarks)):
    bdf = sim_fdr[sim_fdr['benchmark'] == bench].sort_values('contamination_pct')
    ax = axes[i]
    ax.plot(bdf['contamination_pct'], bdf['raw_reject_rate'], 'o-', label='Uncorrected', color='#2196F3', linewidth=1.5, markersize=4)
    ax.plot(bdf['contamination_pct'], bdf['bh_reject_rate'], 's-', label='BH-FDR', color='#FF9800', linewidth=1.5, markersize=4)
    ax.plot(bdf['contamination_pct'], bdf['bonf_reject_rate'], '^-', label='Bonferroni', color='#F44336', linewidth=1.5, markersize=4)
    ax.axhline(0.05, ls='--', color='gray', alpha=0.5)
    ax.set_title(bench, fontsize=11, fontweight='bold')
    ax.set_xlabel('Contamination %', fontsize=9)
    if i == 0:
        ax.set_ylabel('Rejection Rate', fontsize=10)
        ax.legend(fontsize=7, loc='lower right')
    ax.set_ylim(-0.02, 1.05)
    ax.grid(alpha=0.3)

plt.suptitle('FDR Correction Impact on Detection Power (per benchmark)', fontsize=13, y=1.02)
plt.tight_layout()
plt.savefig(f"{OUT}/fdr_power_per_benchmark.png", dpi=200, bbox_inches='tight')
plt.close()
print("Saved per-benchmark power figure.")

# =============================================================================
# Save summary
# =============================================================================

# Add flagging rates
for key in ['theoretical_null', 'empirical_null']:
    for subkey in summary[key]:
        summary[key][f"{subkey}_rate"] = round(summary[key][subkey] / 60 * 100, 1)

with open(f"{OUT}/fdr_summary.json", 'w') as f:
    json.dump(summary, f, indent=2, default=str)

print(f"\nAll outputs saved to {OUT}/")
print(f"\nKey result: empirical null BH-FDR flagging = {summary['empirical_null']['bh_fdr_flagged']}/60 "
      f"({summary['empirical_null']['bh_fdr_flagged']/60*100:.1f}%)")
