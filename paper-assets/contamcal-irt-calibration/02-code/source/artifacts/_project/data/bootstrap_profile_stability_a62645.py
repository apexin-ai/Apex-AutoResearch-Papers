#!/usr/bin/env python3
"""Bootstrap item-level analysis for dose-response profile stability.

Analyses:
1. Profile classification stability — how often does bootstrap resampling
   of evaluation items reproduce the observed dose-response pattern?
2. Benefit/harm threshold CI — 95% confidence interval for the baseline
   accuracy separating contamination-benefiting from -harmed models.

Data layout:
    {data_dir}/{model}_{dosage}[{suffix}]/correctness_matrix.json
    or  .../item_responses.json

Usage:
    python bootstrap_profile_stability.py \
        --data-dir /root/autodl-tmp/exp001/eval_results_v2/ \
        --benchmark mmlu --n-bootstrap 10000
"""

import argparse
import json
import os
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np

# ── Registry ────────────────────────────────────────────────────────

MODELS = {
    'phi4':    'Phi-4 14.7B',
    'qwen14b': 'Qwen2.5-14B',
    'qwen7b':  'Qwen2.5-7B',
    'gemma2':  'Gemma-2 9B',
    'olmo2':   'OLMo-2 7B',
}

DOSAGES = ['d000', 'd005', 'd025', 'd050', 'd100']
DOSE_LABELS = ['0%', '5%', '25%', '50%', '100%']

# ── Data loading ────────────────────────────────────────────────────

def load_responses(data_dir, model, dosage, benchmark, suffix=''):
    """Load boolean correctness array for one model x dosage x benchmark.

    Tries correctness_matrix.json first (compact), falls back to
    item_responses.json.
    """
    base = Path(data_dir) / f'{model}_{dosage}{suffix}'

    # Fast path: correctness_matrix.json
    cm = base / 'correctness_matrix.json'
    if cm.exists():
        with open(cm) as f:
            data = json.load(f)
        if benchmark in data:
            return np.array(data[benchmark], dtype=np.int8)

    # Fallback: item_responses.json
    ir = base / 'item_responses.json'
    if ir.exists():
        with open(ir) as f:
            items = json.load(f)
        arr = [it['correct'] for it in items if it['benchmark'] == benchmark]
        if arr:
            return np.array(arr, dtype=np.int8)

    return None


def load_all(data_dir, benchmark, suffix, model_keys):
    """Load data for all models, return dict of model -> {dosage -> array}."""
    data = {}
    for model in model_keys:
        arrays = {}
        ok = True
        for dose in DOSAGES:
            arr = load_responses(data_dir, model, dose, benchmark, suffix)
            if arr is None:
                print(f'  [SKIP] {model}_{dose}{suffix}: not found')
                ok = False
                break
            arrays[dose] = arr
        if not ok:
            continue
        lens = {d: len(a) for d, a in arrays.items()}
        if len(set(lens.values())) != 1:
            print(f'  [SKIP] {model}: inconsistent item counts {lens}')
            continue
        data[model] = arrays
        n = lens['d000']
        print(f'  {MODELS.get(model, model):.<22s} {n:>6d} items')
    return data

# ── Pattern classification ──────────────────────────────────────────

PATTERN_NAMES = ['Immune', 'U-collapse', 'V-recovery', 'Benefit', 'Benefit-sat']


def classify_vec(accs):
    """Vectorized pattern classification.

    Args:
        accs: dict dosage -> ndarray shape (B,), accuracy in percentage points.
    Returns:
        ndarray shape (B,) of pattern name strings.

    Rules:
        |delta| <= 1pp                          -> Immune
        delta <= -5pp                           -> U-collapse
        -5 < delta < -1, mid dips below both    -> V-recovery
        -5 < delta < -1, no V dip               -> U-collapse
        delta > 1, late gain saturates           -> Benefit-sat
        delta > 1, otherwise                    -> Benefit
    """
    B = len(accs['d000'])
    delta = accs['d100'] - accs['d000']
    mid = np.column_stack([accs['d005'], accs['d025'], accs['d050']])
    mid_min = mid.min(axis=1)

    pat = np.full(B, '', dtype='U15')

    # Immune
    immune = np.abs(delta) <= 1.0
    pat[immune] = 'Immune'

    # Negative delta
    neg = delta < -1.0
    severe = neg & (delta <= -5.0)
    v_dip = neg & ~severe & (mid_min < accs['d100']) & (mid_min < accs['d000'])
    pat[severe] = 'U-collapse'
    pat[v_dip] = 'V-recovery'
    pat[neg & ~severe & ~v_dip] = 'U-collapse'

    # Positive delta
    pos = delta > 1.0
    first_half = accs['d025'] - accs['d000']
    second_half = accs['d100'] - accs['d025']
    late = accs['d100'] - accs['d050']
    sat = pos & (((first_half > 0) & (second_half < first_half * 0.3)) | (late < 0.5))
    pat[pos & ~sat] = 'Benefit'
    pat[sat] = 'Benefit-sat'

    return pat

# ── Bootstrap ───────────────────────────────────────────────────────

def run_bootstrap(all_data, B, rng):
    """Paired item-level bootstrap across all models.

    Same resampled item indices are used for every model and dosage,
    preserving cross-model correlations (they evaluate the same items).
    """
    models = list(all_data.keys())
    n_items = len(all_data[models[0]]['d000'])
    idx = rng.integers(0, n_items, size=(B, n_items))

    results = {}
    for model in models:
        t0 = time.time()
        boot_accs = {}
        for dose in DOSAGES:
            boot_accs[dose] = all_data[model][dose][idx].mean(axis=1) * 100.0

        patterns = classify_vec(boot_accs)
        deltas = boot_accs['d100'] - boot_accs['d000']

        obs = {d: float(all_data[model][d].mean() * 100.0) for d in DOSAGES}
        obs_pat = classify_vec({d: np.array([obs[d]]) for d in DOSAGES})[0]

        counts = Counter(patterns)
        stability = counts[obs_pat] / B * 100.0

        results[model] = dict(
            observed_pattern=str(obs_pat),
            observed_delta=round(obs['d100'] - obs['d000'], 4),
            observed_accs={d: round(v, 4) for d, v in obs.items()},
            stability_pct=round(stability, 2),
            pattern_distribution={
                str(k): round(v / B * 100, 2) for k, v in counts.most_common()
            },
            delta_mean=round(float(np.mean(deltas)), 4),
            delta_std=round(float(np.std(deltas)), 4),
            delta_ci95=[
                round(float(np.percentile(deltas, 2.5)), 4),
                round(float(np.percentile(deltas, 97.5)), 4),
            ],
            _baselines=boot_accs['d000'],
            _deltas=deltas,
            _boot_accs=boot_accs,
        )
        dt = time.time() - t0
        print(f'  {MODELS.get(model, model):.<22s} '
              f'{obs_pat:<15s} stability={stability:5.1f}%  ({dt:.1f}s)')

    return results

# ── Threshold ───────────────────────────────────────────────────────

def compute_threshold(results, B):
    """Find 95% CI for baseline accuracy where delta crosses zero.

    For each bootstrap sample, sort models by their resampled baseline,
    then linearly interpolate the crossing from positive to negative delta.
    """
    models = list(results.keys())
    thresholds = []

    for i in range(B):
        pts = sorted(
            (results[m]['_baselines'][i], results[m]['_deltas'][i])
            for m in models
        )
        for j in range(len(pts) - 1):
            b1, d1 = pts[j]
            b2, d2 = pts[j + 1]
            if d1 > 0 and d2 < 0:
                thresholds.append(b1 + (b2 - b1) * d1 / (d1 - d2))
                break
            if d1 > 1.0 and abs(d2) <= 1.0:
                thresholds.append((b1 + b2) / 2.0)
                break

    if not thresholds:
        return None

    arr = np.array(thresholds)
    return dict(
        mean=round(float(np.mean(arr)), 2),
        median=round(float(np.median(arr)), 2),
        ci95=[round(float(np.percentile(arr, 2.5)), 2),
              round(float(np.percentile(arr, 97.5)), 2)],
        std=round(float(np.std(arr)), 2),
        n_valid=len(thresholds),
        n_total=B,
        _values=arr,
    )

# ── Plotting ────────────────────────────────────────────────────────

def make_plots(results, threshold, out_dir, benchmark):
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
    except ImportError:
        print('[WARN] matplotlib unavailable, skipping plots')
        return

    sorted_m = sorted(results, key=lambda m: results[m]['observed_accs']['d000'],
                      reverse=True)
    colors = {
        'phi4': '#1f77b4', 'qwen14b': '#ff7f0e', 'qwen7b': '#2ca02c',
        'gemma2': '#d62728', 'olmo2': '#9467bd',
    }

    # --- Figure 1: delta distributions ---
    n_models = len(sorted_m)
    ncols = min(3, n_models + 1)
    nrows = (n_models + 1 + ncols - 1) // ncols
    fig, axes = plt.subplots(nrows, ncols, figsize=(5.5 * ncols, 4.5 * nrows))
    if nrows == 1 and ncols == 1:
        axes = np.array([[axes]])
    elif nrows == 1:
        axes = axes[np.newaxis, :]
    elif ncols == 1:
        axes = axes[:, np.newaxis]
    fig.suptitle(
        f'Bootstrap Δ(d000→d100) Distributions — {benchmark.upper()} '
        f'(B={len(results[sorted_m[0]]["_deltas"])})',
        fontsize=13, fontweight='bold', y=1.01,
    )

    for i, model in enumerate(sorted_m):
        ax = axes[i // ncols][i % ncols]
        r = results[model]
        ax.hist(r['_deltas'], bins=80, density=True, alpha=0.7,
                color=colors.get(model, 'steelblue'), edgecolor='none')
        ax.axvline(r['observed_delta'], color='crimson', lw=2,
                   label=f'Obs: {r["observed_delta"]:+.2f}pp')
        ax.axvline(0, color='black', lw=0.8, ls='--')
        for bnd in (-1, 1, -5):
            ax.axvline(bnd, color='gray', lw=0.5, ls=':')
        name = MODELS.get(model, model)
        ax.set_title(f'{name}  (base {r["observed_accs"]["d000"]:.1f}%)\n'
                     f'{r["observed_pattern"]}  — {r["stability_pct"]:.1f}% stable',
                     fontsize=10)
        ax.set_xlabel('Δ [pp]')
        ax.legend(fontsize=8)

    # Threshold subplot
    idx_t = n_models
    ax_t = axes[idx_t // ncols][idx_t % ncols]
    if threshold and threshold['n_valid'] > 100:
        ax_t.hist(threshold['_values'], bins=60, density=True, alpha=0.7,
                  color='darkorange', edgecolor='none')
        ax_t.axvline(threshold['median'], color='crimson', lw=2,
                     label=f'Median: {threshold["median"]:.1f}%')
        ci = threshold['ci95']
        ax_t.axvspan(ci[0], ci[1], alpha=0.2, color='crimson',
                     label=f'95% CI: [{ci[0]:.1f}, {ci[1]:.1f}]')
        ax_t.set_xlabel('Baseline accuracy (%)')
        ax_t.set_title('Benefit/Harm Threshold', fontsize=10)
        ax_t.legend(fontsize=8)
    else:
        msg = 'Threshold\nnot estimable' if threshold is None \
              else f'Too few crossings\n({threshold["n_valid"]}/{threshold["n_total"]})'
        ax_t.text(0.5, 0.5, msg, transform=ax_t.transAxes,
                  ha='center', va='center', fontsize=11)
        ax_t.set_title('Benefit/Harm Threshold', fontsize=10)

    # Hide unused axes
    total_slots = nrows * ncols
    for k in range(n_models + 1, total_slots):
        axes[k // ncols][k % ncols].set_visible(False)

    plt.tight_layout()
    p1 = Path(out_dir) / f'bootstrap_delta_{benchmark}.png'
    plt.savefig(p1, dpi=150, bbox_inches='tight')
    plt.close()
    print(f'[INFO] Plot saved: {p1}')

    # --- Figure 2: dose-response with CI bands ---
    fig2, ax2 = plt.subplots(figsize=(10, 7))
    x = np.arange(len(DOSAGES))
    for model in sorted_m:
        r = results[model]
        means = np.array([r['_boot_accs'][d].mean() for d in DOSAGES])
        lo = np.array([np.percentile(r['_boot_accs'][d], 2.5) for d in DOSAGES])
        hi = np.array([np.percentile(r['_boot_accs'][d], 97.5) for d in DOSAGES])
        c = colors.get(model, 'gray')
        name = MODELS.get(model, model)
        ax2.plot(x, means, 'o-', color=c, lw=2,
                 label=f'{name} ({r["observed_pattern"]})')
        ax2.fill_between(x, lo, hi, alpha=0.15, color=c)

    ax2.set_xticks(x)
    ax2.set_xticklabels(DOSE_LABELS)
    ax2.set_xlabel('Contamination dose', fontsize=12)
    ax2.set_ylabel('Accuracy (%)', fontsize=12)
    ax2.set_title(f'Dose-Response with 95% Bootstrap CI — {benchmark.upper()}',
                  fontsize=13, fontweight='bold')
    ax2.legend(fontsize=9, loc='best')
    ax2.grid(True, alpha=0.3)
    plt.tight_layout()
    p2 = Path(out_dir) / f'bootstrap_dose_response_{benchmark}.png'
    plt.savefig(p2, dpi=150, bbox_inches='tight')
    plt.close()
    print(f'[INFO] Plot saved: {p2}')

# ── Main ────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(
        description='Bootstrap profile classification stability analysis')
    ap.add_argument('--data-dir', required=True,
                    help='Root dir with {model}_{dosage}/ subdirs')
    ap.add_argument('--benchmark', default='mmlu',
                    choices=['mmlu', 'arc_challenge'])
    ap.add_argument('--n-bootstrap', type=int, default=10000)
    ap.add_argument('--seed', type=int, default=42,
                    help='RNG seed for bootstrap')
    ap.add_argument('--seed-suffix', default='',
                    help='Dir name suffix, e.g. "_s123"')
    ap.add_argument('--output-dir', default='.',
                    help='Where to write JSON + plots')
    ap.add_argument('--models', nargs='*', default=None,
                    help='Subset of model keys (default: all 5)')
    ap.add_argument('--no-plot', action='store_true')
    args = ap.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    rng = np.random.default_rng(args.seed)
    model_keys = args.models or list(MODELS.keys())

    print(f'=== Bootstrap Profile Stability ===')
    print(f'Benchmark: {args.benchmark}   B={args.n_bootstrap}   '
          f'rng_seed={args.seed}')
    print(f'Data: {args.data_dir}   suffix="{args.seed_suffix}"')
    print()

    all_data = load_all(args.data_dir, args.benchmark, args.seed_suffix,
                        model_keys)
    if not all_data:
        print('[ERROR] No valid data found')
        sys.exit(1)

    n_items_set = {len(all_data[m]['d000']) for m in all_data}
    if len(n_items_set) == 1:
        print(f'\nPaired bootstrap on {n_items_set.pop()} shared items')
    else:
        print(f'\n[WARN] Item counts differ: {n_items_set} — '
              f'bootstrap uses smallest common count')

    print()
    t0 = time.time()
    results = run_bootstrap(all_data, args.n_bootstrap, rng)
    elapsed = time.time() - t0
    print(f'\nBootstrap done in {elapsed:.1f}s')

    threshold = None
    if len(results) >= 3:
        threshold = compute_threshold(results, args.n_bootstrap)

    # ── Summary table ──
    print()
    hdr = (f'{"Model":<18} {"Baseline":>8} {"Delta":>10} '
           f'{"Pattern":<15} {"Stability":>10} {"Delta 95% CI":>22}')
    sep = '-' * len(hdr)
    print('=' * len(hdr))
    print(hdr)
    print(sep)
    for m in sorted(results, key=lambda m: results[m]['observed_accs']['d000'],
                    reverse=True):
        r = results[m]
        ci = r['delta_ci95']
        print(f'{MODELS.get(m,m):<18} {r["observed_accs"]["d000"]:>7.2f}% '
              f'{r["observed_delta"]:>+9.2f}pp '
              f'{r["observed_pattern"]:<15} {r["stability_pct"]:>9.1f}% '
              f'[{ci[0]:>+7.2f}, {ci[1]:>+7.2f}]')
    print('=' * len(hdr))

    if threshold:
        ci = threshold['ci95']
        print(f'\nBenefit/Harm Threshold: {threshold["median"]:.1f}% '
              f'(95% CI: [{ci[0]:.1f}, {ci[1]:.1f}])')
        print(f'  Valid crossings: {threshold["n_valid"]}/{threshold["n_total"]} '
              f'({threshold["n_valid"]/threshold["n_total"]*100:.1f}%)')

    # ── Plots ──
    if not args.no_plot:
        make_plots(results, threshold, args.output_dir, args.benchmark)

    # ── JSON output ──
    output = {
        'config': {
            'benchmark': args.benchmark,
            'n_bootstrap': args.n_bootstrap,
            'seed': args.seed,
            'data_dir': str(args.data_dir),
        },
        'models': {},
        'threshold': (
            {k: v for k, v in threshold.items() if not k.startswith('_')}
            if threshold else None
        ),
    }
    for m, r in results.items():
        output['models'][m] = {
            'display_name': MODELS.get(m, m),
            'observed_pattern': r['observed_pattern'],
            'observed_delta_pp': r['observed_delta'],
            'observed_accs': r['observed_accs'],
            'stability_pct': r['stability_pct'],
            'pattern_distribution': r['pattern_distribution'],
            'delta_mean': r['delta_mean'],
            'delta_std': r['delta_std'],
            'delta_ci95': r['delta_ci95'],
        }

    jp = Path(args.output_dir) / f'bootstrap_results_{args.benchmark}.json'
    with open(jp, 'w') as f:
        json.dump(output, f, indent=2)
    print(f'\n[INFO] Results saved: {jp}')


if __name__ == '__main__':
    main()
