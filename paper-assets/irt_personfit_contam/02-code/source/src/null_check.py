# Null distribution sanity check for lz* under PSN-IRT estimated 4PL parameters.
# Verifies that lz* ~ N(0,1) when responses are generated from the model.

import json
import os
import sys
import time

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from person_fit import (
    prob_4pl, generate_response, compute_lz_star,
    _estimate_theta_mle_batch, filter_valid_items,
)

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARAMS_DIR = os.path.join(PROJECT_ROOT, 'artifacts', 'psn_irt_params')
OUTPUT_DIR = os.path.join(PROJECT_ROOT, 'artifacts', 'null_check_results')
BENCHMARKS = ['mmlu', 'hellaswag', 'gsm8k', 'arc_c', 'humaneval']
N_SIM = 2_000
SEED = 42


def load_params(benchmark):
    path = os.path.join(PARAMS_DIR, f'{benchmark}_params.csv')
    df = pd.read_csv(path)
    return (
        df['a_discrimination'].values,
        df['b_difficulty'].values,
        df['c_guessing'].values,
        df['d_feasibility'].values,
    )


def run_benchmark(benchmark, n_sim=N_SIM, seed=SEED):
    print(f'\n{"="*60}')
    print(f'Benchmark: {benchmark}')
    print(f'{"="*60}')

    a, b, c, d = load_params(benchmark)
    n_original = len(a)
    print(f'  Items loaded: {n_original}')

    mask = filter_valid_items(a, b, c, d, min_a=0.0)
    a, b, c, d = a[mask], b[mask], c[mask], d[mask]
    n_filtered = len(a)
    n_removed = n_original - n_filtered
    print(f'  Items after filtering (a > 0): {n_filtered} (removed {n_removed})')

    rng = np.random.default_rng(seed)
    theta_true = rng.standard_normal(n_sim)

    print(f'  Generating {n_sim} response vectors ({n_sim} x {n_filtered})...')
    t0 = time.time()
    X = generate_response(theta_true, a, b, c, d, rng=rng)
    print(f'    Done in {time.time()-t0:.1f}s')

    print(f'  Estimating theta_hat for {n_sim} vectors...')
    t0 = time.time()
    theta_hat = _estimate_theta_mle_batch(X, a, b, c, d)
    print(f'    Done in {time.time()-t0:.1f}s')

    print(f'  Computing lz* ...')
    t0 = time.time()
    lz_star = compute_lz_star(X, theta_hat[:, None], a, b, c, d)
    print(f'    Done in {time.time()-t0:.1f}s')

    lz_star = np.asarray(lz_star).ravel()
    finite_mask = np.isfinite(lz_star)
    n_nonfinite = (~finite_mask).sum()
    if n_nonfinite > 0:
        print(f'  WARNING: {n_nonfinite} non-finite lz* values removed')
    lz_star = lz_star[finite_mask]

    mean = float(np.mean(lz_star))
    std = float(np.std(lz_star, ddof=1))
    skew = float(stats.skew(lz_star))
    kurt = float(stats.kurtosis(lz_star, fisher=False))  # excess=False -> raw kurtosis

    ks_stat, ks_p = stats.kstest(lz_star, 'norm')
    n_shapiro = min(5000, len(lz_star))
    shapiro_stat, shapiro_p = stats.shapiro(lz_star[:n_shapiro])
    ad_result = stats.anderson(lz_star, 'norm')
    ad_crit_5 = float(ad_result.critical_values[2])  # 5% significance level

    is_large = benchmark in ('mmlu', 'hellaswag', 'gsm8k')
    flag = ''
    passed = True
    if is_large and ks_p < 0.01:
        flag = 'KS p < 0.01 on large benchmark — recalibration may be needed'
        passed = False

    print(f'  Results: mean={mean:.4f}, std={std:.4f}, skew={skew:.4f}, kurtosis={kurt:.4f}')
    print(f'  KS: stat={ks_stat:.4f}, p={ks_p:.4f}')
    print(f'  Shapiro (n={n_shapiro}): stat={shapiro_stat:.4f}, p={shapiro_p:.4f}')
    print(f'  Anderson: stat={ad_result.statistic:.4f}, crit_5%={ad_crit_5:.4f}')
    if flag:
        print(f'  FLAG: {flag}')

    plot_diagnostics(benchmark, lz_star, n_filtered, ks_p)

    return {
        'n_items_original': int(n_original),
        'n_items_filtered': int(n_filtered),
        'n_items_removed': int(n_removed),
        'n_simulations': int(len(lz_star)),
        'lz_star_mean': round(mean, 4),
        'lz_star_std': round(std, 4),
        'lz_star_skewness': round(skew, 4),
        'lz_star_kurtosis': round(kurt, 4),
        'ks_statistic': round(float(ks_stat), 4),
        'ks_pvalue': round(float(ks_p), 4),
        'shapiro_statistic': round(float(shapiro_stat), 4),
        'shapiro_pvalue': round(float(shapiro_p), 4),
        'anderson_statistic': round(float(ad_result.statistic), 4),
        'anderson_critical_5pct': round(ad_crit_5, 4),
        'pass': passed,
        'flag': flag,
    }


def plot_diagnostics(benchmark, lz_star, n_items, ks_p):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.hist(lz_star, bins=100, density=True, alpha=0.7, color='steelblue',
             edgecolor='white', linewidth=0.3, label='lz* empirical')
    x_grid = np.linspace(-5, 5, 300)
    ax1.plot(x_grid, stats.norm.pdf(x_grid), 'r--', lw=2, label='N(0,1)')
    ax1.set_xlabel('lz*')
    ax1.set_ylabel('Density')
    ax1.set_title(f'{benchmark} | n_items={n_items} | KS p={ks_p:.4f}')
    ax1.legend(fontsize=9)
    ax1.set_xlim(-5, 5)

    osm = stats.probplot(lz_star, dist='norm', fit=False)
    ax2.scatter(osm[0], osm[1], s=1, alpha=0.3, color='steelblue')
    lims = [-4, 4]
    ax2.plot(lims, lims, 'r--', lw=1.5)
    ax2.set_xlabel('Theoretical quantiles')
    ax2.set_ylabel('Observed quantiles')
    ax2.set_title(f'{benchmark} QQ-plot')
    ax2.set_xlim(lims)
    ax2.set_ylim(lims)
    ax2.set_aspect('equal')

    fig.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, f'{benchmark}_lz_star_hist.png')
    fig.savefig(out_path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f'  Saved: {out_path}')


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Dry-run: 100 simulations on smallest benchmark to validate correctness
    print('DRY RUN: 100 sims on humaneval...')
    dry = run_benchmark('humaneval', n_sim=100, seed=0)
    print(f'  Dry run lz* mean={dry["lz_star_mean"]}, std={dry["lz_star_std"]}')
    if abs(dry['lz_star_mean']) > 1.0 or dry['lz_star_std'] < 0.3:
        print('ERROR: Dry run looks wrong, aborting.')
        sys.exit(1)
    print('Dry run OK, proceeding with full runs.\n')

    results = {}
    for bm in BENCHMARKS:
        results[bm] = run_benchmark(bm, n_sim=N_SIM, seed=SEED)

    summary_path = os.path.join(OUTPUT_DIR, 'null_check_summary.json')
    with open(summary_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f'\nSummary saved: {summary_path}')

    print('\n' + '='*60)
    print('SUMMARY')
    print('='*60)
    for bm, r in results.items():
        status = 'PASS' if r['pass'] else 'FAIL'
        flag_str = f'  {r["flag"]}' if r['flag'] else ''
        print(f'  {bm:12s}: mean={r["lz_star_mean"]:+.4f} std={r["lz_star_std"]:.4f} '
              f'KS_p={r["ks_pvalue"]:.4f} [{status}]{flag_str}')


if __name__ == '__main__':
    main()
