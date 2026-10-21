#!/usr/bin/env python3
"""Classification sensitivity sweep with mid-trajectory volatility check.

Sweeps over τ (noise threshold) and σ (collapse threshold) to evaluate
classification robustness across 30 parameter combinations.

v2: Adds volatility check within the Immune branch — if intermediate
dosages deviate beyond τ from baseline, reclassify as V-recovery.
"""

import json
import os
from itertools import product

import numpy as np

# ── Parameters ──────────────────────────────────────────────────────

TAU_VALUES = [0.5, 0.75, 1.0, 1.25, 1.5, 2.0]
SIGMA_VALUES = [3.0, 4.0, 5.0, 6.0, 7.0]

# ── Classifier v2 (with volatility check) ──────────────────────────

def classify_profile(accs, tau=1.0, sigma=5.0):
    """Classify a single dose-response profile.

    Args:
        accs: dict d000..d100 -> float accuracy (percentage points)
        tau: noise threshold (pp) for Immune boundary
        sigma: collapse threshold (pp) for severe U-collapse
    Returns:
        str: Immune | U-collapse | V-recovery | Benefit | Benefit-sat
    """
    acc_d000 = accs['d000']
    acc_d100 = accs['d100']
    delta = acc_d100 - acc_d000

    intermediate_accs = [accs['d005'], accs['d025'], accs['d050']]

    if abs(delta) <= tau:
        # v2: mid-trajectory volatility check
        max_deviation = max(abs(a - acc_d000) for a in intermediate_accs)
        if max_deviation <= tau:
            return 'Immune'
        else:
            min_intermediate = min(intermediate_accs)
            if min_intermediate < acc_d000 - tau:
                return 'V-recovery'
            else:
                return 'Immune'

    if delta <= -sigma:
        return 'U-collapse'

    if delta < -tau:
        mid_min = min(intermediate_accs)
        if mid_min < acc_d100 and mid_min < acc_d000:
            return 'V-recovery'
        else:
            return 'U-collapse'

    # delta > tau: positive
    first_half = accs['d025'] - acc_d000
    second_half = acc_d100 - accs['d025']
    late = acc_d100 - accs['d050']

    if (first_half > 0 and second_half < first_half * 0.3) or late < 0.5:
        return 'Benefit-sat'

    return 'Benefit'


# ── Classifier v1 (without volatility check, for comparison) ───────

def classify_profile_v1(accs, tau=1.0, sigma=5.0):
    """Original classifier without volatility check."""
    acc_d000 = accs['d000']
    acc_d100 = accs['d100']
    delta = acc_d100 - acc_d000

    intermediate_accs = [accs['d005'], accs['d025'], accs['d050']]

    if abs(delta) <= tau:
        return 'Immune'

    if delta <= -sigma:
        return 'U-collapse'

    if delta < -tau:
        mid_min = min(intermediate_accs)
        if mid_min < acc_d100 and mid_min < acc_d000:
            return 'V-recovery'
        else:
            return 'U-collapse'

    first_half = accs['d025'] - acc_d000
    second_half = acc_d100 - accs['d025']
    late = acc_d100 - accs['d050']

    if (first_half > 0 and second_half < first_half * 0.3) or late < 0.5:
        return 'Benefit-sat'

    return 'Benefit'


# ── Test cases ──────────────────────────────────────────────────────

TEST_CASES = [
    {
        'name': 'Phi-4 s42',
        'accs': {'d000': 76.44, 'd005': 76.28, 'd025': 76.50,
                 'd050': 76.10, 'd100': 76.27},
        'expected': 'Immune',
    },
    {
        'name': 'Qwen-14B s42',
        'accs': {'d000': 69.44, 'd005': 63.76, 'd025': 62.51,
                 'd050': 61.34, 'd100': 60.07},
        'expected': 'U-collapse',
    },
    {
        'name': 'Qwen-7B s42',
        'accs': {'d000': 66.11, 'd005': 63.42, 'd025': 63.15,
                 'd050': 63.59, 'd100': 64.33},
        'expected': 'V-recovery',
    },
    {
        'name': 'Gemma-2 s42',
        'accs': {'d000': 61.86, 'd005': 63.56, 'd025': 64.19,
                 'd050': 64.73, 'd100': 65.62},
        'expected': 'Benefit',
    },
    {
        'name': 'OLMo-2 s42',
        'accs': {'d000': 53.79, 'd005': 55.17, 'd025': 56.06,
                 'd050': 56.53, 'd100': 57.00},
        'expected': 'Benefit-sat',
    },
    {
        'name': 'Qwen-7B s123',
        'accs': {'d000': 66.59, 'd005': 63.37, 'd025': 64.82,
                 'd050': 65.00, 'd100': 66.59},
        'expected': 'V-recovery',
    },
]


def run_verification(tau=1.0, sigma=5.0):
    print(f"\n{'='*70}")
    print(f"  Verification (tau={tau}, sigma={sigma})")
    print(f"{'='*70}")

    all_pass = True
    for tc in TEST_CASES:
        result = classify_profile(tc['accs'], tau=tau, sigma=sigma)
        ok = result == tc['expected']
        if not ok:
            all_pass = False
        mark = 'PASS' if ok else 'FAIL'
        print(f"  [{mark}] {tc['name']:<20s}  got={result:<15s}  expected={tc['expected']}")

    print(f"\n  {'ALL 6/6 PASSED' if all_pass else 'SOME FAILED'}")
    return all_pass


# ── Sensitivity Sweep ───────────────────────────────────────────────

def run_sweep():
    results = {}
    for tau, sigma in product(TAU_VALUES, SIGMA_VALUES):
        key = f"tau={tau}_sigma={sigma}"
        results[key] = {'tau': tau, 'sigma': sigma, 'classifications': {}}

        for tc in TEST_CASES:
            v2 = classify_profile(tc['accs'], tau=tau, sigma=sigma)
            v1 = classify_profile_v1(tc['accs'], tau=tau, sigma=sigma)
            results[key]['classifications'][tc['name']] = {
                'v2': v2, 'v1': v1,
                'expected': tc['expected'],
                'v2_correct': v2 == tc['expected'],
                'v1_correct': v1 == tc['expected'],
                'changed': v1 != v2,
            }
    return results


def print_sweep_table(results):
    print(f"\n{'='*120}")
    print("  SENSITIVITY SWEEP RESULTS (30 combinations)")
    print(f"{'='*120}")

    names = [tc['name'] for tc in TEST_CASES]
    print(f"\n  {'tau':>5s} {'sigma':>5s} | ", end='')
    for n in names:
        print(f"{n:>16s}", end=' ')
    print(f"| {'Match':>5s}")
    print(f"  {'-'*5} {'-'*5}-+-" + '-' * (17 * len(names)) + f"+-{'-'*5}")

    for tau in TAU_VALUES:
        for sigma in SIGMA_VALUES:
            key = f"tau={tau}_sigma={sigma}"
            r = results[key]
            n_correct = sum(1 for c in r['classifications'].values()
                           if c['v2_correct'])

            print(f"  {tau:>5.2f} {sigma:>5.1f} | ", end='')
            for tc in TEST_CASES:
                cls = r['classifications'][tc['name']]
                marker = '' if cls['v2_correct'] else '*'
                label = cls['v2'] + marker
                print(f"{label:>16s}", end=' ')
            print(f"| {n_correct}/{len(TEST_CASES)}")
        print()


def print_change_summary(results):
    print(f"\n{'='*80}")
    print("  V1 -> V2 CHANGES (volatility check impact)")
    print(f"{'='*80}")

    changes = []
    for key, r in results.items():
        for name, cls in r['classifications'].items():
            if cls['changed']:
                changes.append({
                    'tau': r['tau'], 'sigma': r['sigma'],
                    'name': name, 'v1': cls['v1'], 'v2': cls['v2'],
                    'correct': cls['v2_correct'],
                })

    if not changes:
        print("  No changes between v1 and v2.")
        return

    print(f"\n  {'tau':>5s} {'sigma':>5s} | {'Family':<20s} | "
          f"{'v1':<15s} -> {'v2':<15s} | Correct?")
    print(f"  {'-'*5} {'-'*5}-+-{'-'*20}-+-"
          f"{'-'*15}----{'-'*15}-+-{'-'*8}")

    for c in sorted(changes, key=lambda x: (x['name'], x['tau'], x['sigma'])):
        mark = 'YES' if c['correct'] else 'NO'
        print(f"  {c['tau']:>5.2f} {c['sigma']:>5.1f} | {c['name']:<20s} | "
              f"{c['v1']:<15s} -> {c['v2']:<15s} | {mark}")

    n_improved = sum(1 for c in changes if c['correct'])
    n_regressed = sum(1 for c in changes if not c['correct'])
    print(f"\n  Total changes: {len(changes)}")
    print(f"  Improvements (v2 correct, v1 wrong): {n_improved}")
    print(f"  Regressions  (v2 wrong, v1 correct): {n_regressed}")


def qwen7b_s123_analysis(results):
    print(f"\n{'='*70}")
    print("  Qwen-7B s123 Classification Across All Combinations")
    print(f"{'='*70}")

    print(f"\n  {'tau':>5s} |", end='')
    for sigma in SIGMA_VALUES:
        print(f" sigma={sigma:<4.1f}   ", end='')
    print()
    print(f"  {'-'*5}-+" + '-' * (14 * len(SIGMA_VALUES)))

    v2_correct = 0
    v1_correct = 0
    total = 0

    for tau in TAU_VALUES:
        print(f"  {tau:>5.2f} |", end='')
        for sigma in SIGMA_VALUES:
            key = f"tau={tau}_sigma={sigma}"
            cls = results[key]['classifications']['Qwen-7B s123']
            mark = ' ok' if cls['v2_correct'] else '  X'
            print(f" {cls['v2']:<10s}{mark}", end='')
            total += 1
            if cls['v2_correct']:
                v2_correct += 1
            if cls['v1_correct']:
                v1_correct += 1
        print()

    print(f"\n  v2 correct: {v2_correct}/{total}  "
          f"(v1 correct: {v1_correct}/{total})")


def make_heatmaps(results, output_dir):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    n_families = len(TEST_CASES)

    agree_v2 = np.zeros((len(TAU_VALUES), len(SIGMA_VALUES)))
    agree_v1 = np.zeros((len(TAU_VALUES), len(SIGMA_VALUES)))

    for i, tau in enumerate(TAU_VALUES):
        for j, sigma in enumerate(SIGMA_VALUES):
            key = f"tau={tau}_sigma={sigma}"
            r = results[key]
            agree_v2[i, j] = sum(
                1 for c in r['classifications'].values() if c['v2_correct'])
            agree_v1[i, j] = sum(
                1 for c in r['classifications'].values() if c['v1_correct'])

    # --- Figure 1: v1 vs v2 vs diff ---
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    for ax_idx, (mat, title) in enumerate([
        (agree_v2, 'v2 (with volatility check)'),
        (agree_v1, 'v1 (without volatility check)'),
    ]):
        ax = axes[ax_idx]
        im = ax.imshow(mat, cmap='RdYlGn', vmin=0, vmax=n_families,
                        aspect='auto')
        ax.set_xticks(range(len(SIGMA_VALUES)))
        ax.set_xticklabels([f'{s:.0f}' for s in SIGMA_VALUES])
        ax.set_yticks(range(len(TAU_VALUES)))
        ax.set_yticklabels([f'{t:.2f}' for t in TAU_VALUES])
        ax.set_xlabel(r'$\sigma$ (collapse threshold, pp)')
        ax.set_ylabel(r'$\tau$ (noise threshold, pp)')
        ax.set_title(title)
        for ii in range(len(TAU_VALUES)):
            for jj in range(len(SIGMA_VALUES)):
                ax.text(jj, ii, f'{int(mat[ii, jj])}/{n_families}',
                        ha='center', va='center', fontsize=10,
                        fontweight='bold')
        plt.colorbar(im, ax=ax, label='Correct classifications')

    # Diff heatmap
    diff = agree_v2 - agree_v1
    vmax_diff = max(abs(diff.min()), abs(diff.max()), 1)
    ax = axes[2]
    im = ax.imshow(diff, cmap='RdBu', vmin=-vmax_diff, vmax=vmax_diff,
                    aspect='auto')
    ax.set_xticks(range(len(SIGMA_VALUES)))
    ax.set_xticklabels([f'{s:.0f}' for s in SIGMA_VALUES])
    ax.set_yticks(range(len(TAU_VALUES)))
    ax.set_yticklabels([f'{t:.2f}' for t in TAU_VALUES])
    ax.set_xlabel(r'$\sigma$ (collapse threshold, pp)')
    ax.set_ylabel(r'$\tau$ (noise threshold, pp)')
    ax.set_title(r'v2 $-$ v1 (improvement)')
    for ii in range(len(TAU_VALUES)):
        for jj in range(len(SIGMA_VALUES)):
            val = int(diff[ii, jj])
            ax.text(jj, ii, f'{val:+d}' if val != 0 else '0',
                    ha='center', va='center', fontsize=10, fontweight='bold')
    plt.colorbar(im, ax=ax, label=r'$\Delta$ correct')

    plt.suptitle('Classification Sensitivity Sweep: Agreement with Expected Labels',
                 fontsize=13)
    plt.tight_layout()
    p1 = os.path.join(output_dir, 'sensitivity_heatmap_v2.png')
    plt.savefig(p1, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\n  [INFO] Heatmap saved: {p1}")

    # --- Figure 2: per-family breakdown ---
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    axes_flat = axes.flatten()

    for f_idx, tc in enumerate(TEST_CASES):
        ax = axes_flat[f_idx]
        correct_mat = np.zeros((len(TAU_VALUES), len(SIGMA_VALUES)))
        label_mat = np.empty((len(TAU_VALUES), len(SIGMA_VALUES)), dtype='U15')

        for i, tau in enumerate(TAU_VALUES):
            for j, sigma in enumerate(SIGMA_VALUES):
                key = f"tau={tau}_sigma={sigma}"
                cls = results[key]['classifications'][tc['name']]
                correct_mat[i, j] = 1.0 if cls['v2_correct'] else 0.0
                label_mat[i, j] = cls['v2']

        im = ax.imshow(correct_mat, cmap='RdYlGn', vmin=0, vmax=1,
                        aspect='auto')
        ax.set_xticks(range(len(SIGMA_VALUES)))
        ax.set_xticklabels([f'{s:.0f}' for s in SIGMA_VALUES])
        ax.set_yticks(range(len(TAU_VALUES)))
        ax.set_yticklabels([f'{t:.2f}' for t in TAU_VALUES])
        ax.set_xlabel(r'$\sigma$')
        ax.set_ylabel(r'$\tau$')
        ax.set_title(f'{tc["name"]} (expected: {tc["expected"]})')

        for i in range(len(TAU_VALUES)):
            for j in range(len(SIGMA_VALUES)):
                color = 'black' if correct_mat[i, j] > 0.5 else 'white'
                ax.text(j, i, label_mat[i, j][:8],
                        ha='center', va='center', fontsize=7, color=color)

    for idx in range(len(TEST_CASES), len(axes_flat)):
        axes_flat[idx].set_visible(False)

    plt.suptitle('Per-Family Classification (green=correct, red=incorrect)',
                 fontsize=13)
    plt.tight_layout()
    p2 = os.path.join(output_dir, 'sensitivity_per_family_v2.png')
    plt.savefig(p2, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  [INFO] Per-family heatmap saved: {p2}")


# ── Main ────────────────────────────────────────────────────────────

def main():
    output_dir = '/root/contamcal-irt-calibration/analysis/results/sensitivity_v2'
    os.makedirs(output_dir, exist_ok=True)

    # Step 1: verification at default params
    passed = run_verification(tau=1.0, sigma=5.0)
    if not passed:
        print("\n  [ERROR] Verification failed, aborting sweep.")
        return

    # Step 2: 30-combo sweep
    print(f"\n{'='*70}")
    print("  Running 30-combination sensitivity sweep...")
    print(f"{'='*70}")

    results = run_sweep()
    print_sweep_table(results)
    print_change_summary(results)
    qwen7b_s123_analysis(results)

    # Phi-4 robustness
    print(f"\n{'='*70}")
    print("  Phi-4 Immune Stability")
    print(f"{'='*70}")
    phi4_immune = sum(
        1 for r in results.values()
        if r['classifications']['Phi-4 s42']['v2'] == 'Immune')
    print(f"  Phi-4 classified as Immune in {phi4_immune}/{len(results)} "
          f"combinations")

    # Per-family robustness
    print(f"\n{'='*70}")
    print("  Per-Family Robustness (correct in N/30 combos)")
    print(f"{'='*70}")
    for tc in TEST_CASES:
        n_v2 = sum(1 for r in results.values()
                   if r['classifications'][tc['name']]['v2_correct'])
        n_v1 = sum(1 for r in results.values()
                   if r['classifications'][tc['name']]['v1_correct'])
        delta = n_v2 - n_v1
        delta_str = f" ({delta:+d})" if delta != 0 else ""
        print(f"  {tc['name']:<20s}  v2: {n_v2:>2d}/30  "
              f"v1: {n_v1:>2d}/30{delta_str}")

    # Heatmaps
    make_heatmaps(results, output_dir)

    # JSON output
    json_out = {}
    for key, r in results.items():
        json_out[key] = {
            'tau': r['tau'], 'sigma': r['sigma'],
            'classifications': r['classifications'],
        }

    json_path = os.path.join(output_dir, 'sweep_results.json')
    with open(json_path, 'w') as f:
        json.dump(json_out, f, indent=2)
    print(f"\n  [INFO] JSON results saved: {json_path}")


if __name__ == '__main__':
    main()
