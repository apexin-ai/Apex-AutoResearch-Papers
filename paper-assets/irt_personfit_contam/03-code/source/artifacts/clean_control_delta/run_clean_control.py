"""Clean-vs-Clean Δlz* validation experiment."""

import sys
sys.path.insert(0, '/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/src')

import numpy as np
import pandas as pd
import json
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from person_fit import (
    generate_response, estimate_theta_mle, compute_lz_star,
    _estimate_theta_mle_batch
)

PARAMS_DIR = '/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/psn_irt_params'
OUT_DIR = '/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/clean_control_delta'

BENCHMARKS = ['mmlu', 'hellaswag', 'gsm8k', 'arc_c', 'humaneval']
N_SUBJECTS = 500
CONTAM_PCT = 0.25
SEED_BASE = 42


def load_params(benchmark):
    df = pd.read_csv(f'{PARAMS_DIR}/{benchmark}_params.csv')
    return (
        df['a_discrimination'].values,
        df['b_difficulty'].values,
        df['c_guessing'].values,
        df['d_feasibility'].values,
    )


def run_clean_vs_clean(thetas, a, b, c, d, seed_a, seed_b):
    rng_a = np.random.default_rng(seed_a)
    rng_b = np.random.default_rng(seed_b)

    X_a = generate_response(thetas, a, b, c, d, rng=rng_a)
    X_b = generate_response(thetas, a, b, c, d, rng=rng_b)

    theta_hat_a = _estimate_theta_mle_batch(X_a, a, b, c, d)
    theta_hat_b = _estimate_theta_mle_batch(X_b, a, b, c, d)

    lz_a = compute_lz_star(X_a, theta_hat_a[:, None], a, b, c, d)
    lz_b = compute_lz_star(X_b, theta_hat_b[:, None], a, b, c, d)

    return lz_a - lz_b


def run_clean_vs_contam(thetas, a, b, c, d, contam_pct, seed):
    rng = np.random.default_rng(seed)
    J = len(a)
    n_contam = int(J * contam_pct)

    X_clean = generate_response(thetas, a, b, c, d, rng=rng)
    theta_hat_clean = _estimate_theta_mle_batch(X_clean, a, b, c, d)
    lz_clean = compute_lz_star(X_clean, theta_hat_clean[:, None], a, b, c, d)

    rng_contam = np.random.default_rng(seed + 10000)
    X_contam = X_clean.copy()
    for i in range(len(thetas)):
        contam_idx = rng_contam.choice(J, size=n_contam, replace=False)
        X_contam[i, contam_idx] = 1

    theta_hat_contam = _estimate_theta_mle_batch(X_contam, a, b, c, d)
    lz_contam = compute_lz_star(X_contam, theta_hat_contam[:, None], a, b, c, d)

    return lz_clean - lz_contam


def compute_stats(delta, label, benchmark):
    n = len(delta)
    mean = np.mean(delta)
    std = np.std(delta, ddof=1)
    se = std / np.sqrt(n)
    ci_lo = mean - 1.96 * se
    ci_hi = mean + 1.96 * se
    t_stat, p_value = stats.ttest_1samp(delta, 0)
    return {
        'benchmark': benchmark,
        'condition': label,
        'n': n,
        'mean': mean,
        'std': std,
        'ci_lo': ci_lo,
        'ci_hi': ci_hi,
        't_stat': t_stat,
        'p_value': p_value,
    }


def main():
    rng_theta = np.random.default_rng(SEED_BASE)
    thetas = rng_theta.standard_normal(N_SUBJECTS)

    all_results = []
    all_deltas = {}

    for bm in BENCHMARKS:
        print(f'Processing {bm}...')
        a, b, c, d = load_params(bm)
        print(f'  Items: {len(a)}')

        delta_cc = run_clean_vs_clean(thetas, a, b, c, d,
                                       seed_a=SEED_BASE + 1, seed_b=SEED_BASE + 2)
        stats_cc = compute_stats(delta_cc, 'clean_vs_clean', bm)
        all_results.append(stats_cc)

        delta_ct = run_clean_vs_contam(thetas, a, b, c, d,
                                        contam_pct=CONTAM_PCT, seed=SEED_BASE + 3)
        stats_ct = compute_stats(delta_ct, 'clean_vs_contam', bm)
        all_results.append(stats_ct)

        # two-sample t-test
        t2, p2 = stats.ttest_ind(delta_cc, delta_ct, equal_var=False)
        pooled_std = np.sqrt((stats_cc['std']**2 + stats_ct['std']**2) / 2)
        cohens_d = (stats_cc['mean'] - stats_ct['mean']) / pooled_std

        stats_cc['two_sample_t'] = t2
        stats_cc['two_sample_p'] = p2
        stats_cc['cohens_d'] = cohens_d
        stats_ct['two_sample_t'] = t2
        stats_ct['two_sample_p'] = p2
        stats_ct['cohens_d'] = cohens_d

        all_deltas[bm] = {'clean_vs_clean': delta_cc, 'clean_vs_contam': delta_ct}

        print(f'  Clean-vs-Clean:  mean={stats_cc["mean"]:.4f}, std={stats_cc["std"]:.4f}, p={stats_cc["p_value"]:.4f}')
        print(f'  Clean-vs-Contam: mean={stats_ct["mean"]:.4f}, std={stats_ct["std"]:.4f}, p={stats_ct["p_value"]:.4f}')
        print(f'  Cohen\'s d: {cohens_d:.4f}')

    # Save CSV
    df = pd.DataFrame(all_results)
    df.to_csv(f'{OUT_DIR}/delta_lz_results.csv', index=False)

    # Save JSON summary
    summary = {}
    for bm in BENCHMARKS:
        cc_row = [r for r in all_results if r['benchmark'] == bm and r['condition'] == 'clean_vs_clean'][0]
        ct_row = [r for r in all_results if r['benchmark'] == bm and r['condition'] == 'clean_vs_contam'][0]
        summary[bm] = {
            'clean_vs_clean': {
                'mean': round(cc_row['mean'], 6),
                'std': round(cc_row['std'], 6),
                'ci': [round(cc_row['ci_lo'], 6), round(cc_row['ci_hi'], 6)],
                'p_value': round(cc_row['p_value'], 6),
            },
            'clean_vs_contam': {
                'mean': round(ct_row['mean'], 6),
                'std': round(ct_row['std'], 6),
                'p_value': round(ct_row['p_value'], 6),
            },
            'two_sample_t': round(cc_row.get('two_sample_t', 0), 6),
            'two_sample_p': round(cc_row.get('two_sample_p', 0), 6),
            'cohens_d': round(cc_row.get('cohens_d', 0), 6),
        }
    with open(f'{OUT_DIR}/delta_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)

    # Plot
    fig, axes = plt.subplots(len(BENCHMARKS), 2, figsize=(12, 3 * len(BENCHMARKS)))
    for i, bm in enumerate(BENCHMARKS):
        delta_cc = all_deltas[bm]['clean_vs_clean']
        delta_ct = all_deltas[bm]['clean_vs_contam']

        x_min = min(delta_cc.min(), delta_ct.min())
        x_max = max(delta_cc.max(), delta_ct.max())
        bins = np.linspace(x_min, x_max, 50)

        ax_cc = axes[i, 0]
        ax_cc.hist(delta_cc, bins=bins, color='steelblue', alpha=0.8, edgecolor='white')
        ax_cc.axvline(0, color='red', linestyle='--', linewidth=1)
        ax_cc.axvline(np.mean(delta_cc), color='black', linestyle='-', linewidth=1.5)
        ax_cc.set_title(f'{bm} — Clean vs Clean')
        ax_cc.set_xlabel('Δlz*')
        cc_row = [r for r in all_results if r['benchmark'] == bm and r['condition'] == 'clean_vs_clean'][0]
        ax_cc.text(0.97, 0.95, f"μ={cc_row['mean']:.3f}\nσ={cc_row['std']:.3f}\np={cc_row['p_value']:.3f}",
                   transform=ax_cc.transAxes, ha='right', va='top', fontsize=8,
                   bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

        ax_ct = axes[i, 1]
        ax_ct.hist(delta_ct, bins=bins, color='coral', alpha=0.8, edgecolor='white')
        ax_ct.axvline(0, color='red', linestyle='--', linewidth=1)
        ax_ct.axvline(np.mean(delta_ct), color='black', linestyle='-', linewidth=1.5)
        ax_ct.set_title(f'{bm} — Clean vs Contaminated (25%)')
        ax_ct.set_xlabel('Δlz*')
        ct_row = [r for r in all_results if r['benchmark'] == bm and r['condition'] == 'clean_vs_contam'][0]
        ax_ct.text(0.97, 0.95, f"μ={ct_row['mean']:.3f}\nσ={ct_row['std']:.3f}\np={ct_row['p_value']:.3f}",
                   transform=ax_ct.transAxes, ha='right', va='top', fontsize=8,
                   bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.tight_layout()
    plt.savefig(f'{OUT_DIR}/delta_distributions.png', dpi=150)
    plt.close()
    print(f'\nPlot saved to {OUT_DIR}/delta_distributions.png')

    # Generate report
    report_lines = ['# Clean-vs-Clean Δlz* Validation Report\n']
    report_lines.append(f'N subjects: {N_SUBJECTS}, Contamination: {int(CONTAM_PCT*100)}%\n')
    report_lines.append('## Results by Benchmark\n')

    for bm in BENCHMARKS:
        cc_row = [r for r in all_results if r['benchmark'] == bm and r['condition'] == 'clean_vs_clean'][0]
        ct_row = [r for r in all_results if r['benchmark'] == bm and r['condition'] == 'clean_vs_contam'][0]
        report_lines.append(f'### {bm}\n')
        report_lines.append(f'| Metric | Clean-vs-Clean | Clean-vs-Contam |')
        report_lines.append(f'|--------|---------------|-----------------|')
        report_lines.append(f'| Mean Δlz* | {cc_row["mean"]:.4f} | {ct_row["mean"]:.4f} |')
        report_lines.append(f'| Std Δlz* | {cc_row["std"]:.4f} | {ct_row["std"]:.4f} |')
        report_lines.append(f'| 95% CI | [{cc_row["ci_lo"]:.4f}, {cc_row["ci_hi"]:.4f}] | [{ct_row["ci_lo"]:.4f}, {ct_row["ci_hi"]:.4f}] |')
        report_lines.append(f'| t-stat (H0: μ=0) | {cc_row["t_stat"]:.4f} | {ct_row["t_stat"]:.4f} |')
        report_lines.append(f'| p-value | {cc_row["p_value"]:.6f} | {ct_row["p_value"]:.6f} |')
        report_lines.append(f'| Cohen\'s d (between groups) | {cc_row.get("cohens_d", 0):.4f} |')
        report_lines.append(f'| Two-sample p | {cc_row.get("two_sample_p", 0):.6f} |')
        report_lines.append('')

    report_lines.append('## Validation Criteria\n')
    all_pass = True
    for bm in BENCHMARKS:
        cc_row = [r for r in all_results if r['benchmark'] == bm and r['condition'] == 'clean_vs_clean'][0]
        ct_row = [r for r in all_results if r['benchmark'] == bm and r['condition'] == 'clean_vs_contam'][0]
        cc_ok = abs(cc_row['mean']) < 0.2
        ct_ok = ct_row['p_value'] < 0.05
        cd_ok = abs(cc_row.get('cohens_d', 0)) > 0.5
        status = 'PASS' if (cc_ok and ct_ok and cd_ok) else 'FAIL'
        if status == 'FAIL':
            all_pass = False
        report_lines.append(f'- **{bm}**: |mean_cc|<0.2: {"✓" if cc_ok else "✗"} ({cc_row["mean"]:.4f}), '
                          f'contam p<0.05: {"✓" if ct_ok else "✗"} ({ct_row["p_value"]:.6f}), '
                          f'|d|>0.5: {"✓" if cd_ok else "✗"} ({abs(cc_row.get("cohens_d", 0)):.4f}) → **{status}**')

    report_lines.append(f'\n## Conclusion\n')
    if all_pass:
        report_lines.append('All benchmarks pass validation. Δlz* between clean response vectors has E≈0, '
                          'confirming that non-zero Δlz* in contamination experiments reflects genuine contamination signal.')
    else:
        report_lines.append('Some benchmarks did not meet all criteria. See details above.')

    with open(f'{OUT_DIR}/delta_report.md', 'w') as f:
        f.write('\n'.join(report_lines))

    print('\nAll outputs saved.')


if __name__ == '__main__':
    main()
