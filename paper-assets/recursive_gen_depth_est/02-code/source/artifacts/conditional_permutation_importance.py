#!/usr/bin/env python3
"""
N4: Conditional Permutation Importance + Bootstrap Rank Stability.

For each of 9 cells (3 model x 3 strategy):
  1. Train RF (200 trees, seed=42)
  2. Permutation importance (n_repeats=30, seed=42, scoring='accuracy')
  3. Bootstrap rank stability (1000 resamples, RF 100 trees, PI n_repeats=10)

Output -> results/conditional_pi/
"""

import json
import os
import sys
import time
import numpy as np
from collections import OrderedDict
from sklearn.ensemble import RandomForestClassifier
from sklearn.inspection import permutation_importance

BASE_DIR = '/root/autodl-tmp/recursive_gen_depth_est'
OUT_DIR = os.path.join(BASE_DIR, 'results', 'conditional_pi')
os.makedirs(OUT_DIR, exist_ok=True)

LOG_FILE = os.path.join(OUT_DIR, 'progress.log')

FEATURE_NAMES = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]

CELLS = OrderedDict({
    'pythia_nucleus':  'data/features_all.jsonl',
    'pythia_temp09':   'data/pythia_temp09/features.jsonl',
    'pythia_topk50':   'results/pythia_topk50/features.jsonl',
    'olmo_nucleus':    'data/olmo/features.jsonl',
    'olmo_temp09':     'results/olmo_temp09/features.jsonl',
    'olmo_topk50':     'results/olmo_topk50/features.jsonl',
    'gpt2xl_nucleus':  'data/gpt2xl/features.jsonl',
    'gpt2xl_temp09':   'results/gpt2xl_temp09/features.jsonl',
    'gpt2xl_topk50':   'results/gpt2xl_topk50/features.jsonl',
})

FEATURE_CATEGORIES = OrderedDict({
    "perplexity": ["mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
                   "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl"],
    "surprisal":  ["mean_surprisal", "var_surprisal", "entropy_of_surprisal"],
    "lexical":    ["type_token_ratio", "hapax_ratio"],
    "ngram_entropy": ["bigram_entropy", "trigram_entropy"],
    "repetition": ["rep_2gram", "rep_3gram", "rep_4gram"],
})

SEED = 42
N_TREES_MAIN = 200
N_REPEATS_MAIN = 30
N_TREES_BOOT = 100
N_REPEATS_BOOT = 10
N_BOOTSTRAP = 1000


def log(msg):
    ts = time.strftime('%Y-%m-%d %H:%M:%S')
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    with open(LOG_FILE, 'a') as f:
        f.write(line + '\n')


def load_features(path):
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)
    y = np.array([r["depth"] for r in records], dtype=np.int64)
    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
    return X, y


def compute_ranks(importances):
    order = np.argsort(importances)[::-1]
    ranks = np.empty_like(order)
    ranks[order] = np.arange(len(order))
    return ranks + 1  # 1-indexed


def compute_pi(X, y, n_trees=N_TREES_MAIN, n_repeats=N_REPEATS_MAIN, seed=SEED):
    rf = RandomForestClassifier(n_estimators=n_trees, random_state=seed, n_jobs=-1)
    rf.fit(X, y)
    result = permutation_importance(
        rf, X, y, n_repeats=n_repeats, random_state=seed,
        scoring='accuracy', n_jobs=-1
    )
    return result.importances_mean, result.importances_std


def bootstrap_rank_stability(X, y, n_bootstrap=N_BOOTSTRAP, seed=SEED):
    rng = np.random.RandomState(seed)
    n_features = X.shape[1]
    all_ranks = np.zeros((n_bootstrap, n_features), dtype=np.int32)

    for b in range(n_bootstrap):
        if b % 100 == 0:
            log(f"    bootstrap {b}/{n_bootstrap}")
        idx = rng.choice(len(X), size=len(X), replace=True)
        X_b, y_b = X[idx], y[idx]

        if len(np.unique(y_b)) < 2:
            all_ranks[b] = np.arange(n_features) + 1
            continue

        rf = RandomForestClassifier(
            n_estimators=N_TREES_BOOT, random_state=seed + b, n_jobs=-1
        )
        rf.fit(X_b, y_b)
        result = permutation_importance(
            rf, X_b, y_b, n_repeats=N_REPEATS_BOOT,
            random_state=seed + b, scoring='accuracy', n_jobs=-1
        )
        all_ranks[b] = compute_ranks(result.importances_mean)

    return all_ranks


def generate_latex_table(per_cell, bootstrap, avg_ranks, avg_pi, family_imp, sorted_fams):
    sorted_features = sorted(FEATURE_NAMES, key=lambda f: avg_ranks[f])
    feat_to_family = {}
    for fam, feats in FEATURE_CATEGORIES.items():
        for f in feats:
            feat_to_family[f] = fam

    lines = []
    lines.append(r'\begin{table*}[t]')
    lines.append(r'\centering')
    lines.append(r'\caption{Permutation importance (PI) across 9 cells (3 models $\times$ 3 strategies).')
    lines.append(r'Bootstrap 95\% CI from 1{,}000 resamples.}')
    lines.append(r'\label{tab:conditional_pi}')
    lines.append(r'\small')
    lines.append(r'\setlength{\tabcolsep}{3pt}')
    lines.append(r'\begin{tabular}{llcccc}')
    lines.append(r'\toprule')
    lines.append(r'Feature & Family & Avg PI & Avg Rank & Boot.\ Median & 95\% CI \\')
    lines.append(r'\midrule')

    for fname in sorted_features:
        median_ranks = [bootstrap[c][fname]['median_rank'] for c in CELLS]
        ci_lows = [bootstrap[c][fname]['rank_ci_low'] for c in CELLS]
        ci_highs = [bootstrap[c][fname]['rank_ci_high'] for c in CELLS]
        avg_med = np.mean(median_ranks)
        avg_lo = np.mean(ci_lows)
        avg_hi = np.mean(ci_highs)

        family = feat_to_family.get(fname, '?')
        fname_tex = fname.replace('_', r'\_')
        family_tex = family.replace('_', r'\_')

        lines.append(
            f'  {fname_tex} & {family_tex} & {avg_pi[fname]:.4f} & '
            f'{avg_ranks[fname]:.1f} & {avg_med:.1f} & '
            f'[{avg_lo:.1f}, {avg_hi:.1f}] \\\\'
        )

    lines.append(r'\midrule')
    lines.append(r'\multicolumn{6}{l}{\textit{Family-level summary:}} \\')
    for fam in sorted_fams:
        fam_tex = fam.replace('_', r'\_')
        fi = family_imp[fam]
        lines.append(
            f'  \\textbf{{{fam_tex}}} & -- & {fi["avg_pi"]:.4f} & '
            f'{fi["avg_rank"]:.1f} & -- & -- \\\\'
        )

    lines.append(r'\bottomrule')
    lines.append(r'\end{tabular}')
    lines.append(r'\end{table*}')
    return '\n'.join(lines)


def main():
    t0 = time.time()
    log("=== N4: Conditional PI + Bootstrap Rank Stability ===")

    per_cell_results = {}
    bootstrap_results = {}

    for cell_name, rel_path in CELLS.items():
        tc = time.time()
        path = os.path.join(BASE_DIR, rel_path)
        log(f"Cell: {cell_name} ({path})")

        X, y = load_features(path)
        classes = np.unique(y)
        log(f"  samples={len(y)}, classes={classes.tolist()}")

        # Main PI
        log("  Computing permutation importance (main)...")
        pi_mean, pi_std = compute_pi(X, y)

        ranks = compute_ranks(pi_mean)
        cell_pi = {}
        for i, fname in enumerate(FEATURE_NAMES):
            cell_pi[fname] = {
                'importance_mean': float(pi_mean[i]),
                'importance_std': float(pi_std[i]),
                'rank': int(ranks[i]),
            }
        per_cell_results[cell_name] = cell_pi

        # Bootstrap
        log(f"  Bootstrap rank stability ({N_BOOTSTRAP} resamples)...")
        all_ranks = bootstrap_rank_stability(X, y)

        cell_boot = {}
        for i, fname in enumerate(FEATURE_NAMES):
            fr = all_ranks[:, i].astype(float)
            cell_boot[fname] = {
                'median_rank': float(np.median(fr)),
                'mean_rank': float(np.mean(fr)),
                'rank_ci_low': float(np.percentile(fr, 2.5)),
                'rank_ci_high': float(np.percentile(fr, 97.5)),
                'rank_std': float(np.std(fr)),
            }
        bootstrap_results[cell_name] = cell_boot

        top5 = sorted(FEATURE_NAMES, key=lambda f: cell_pi[f]['rank'])[:5]
        log(f"  Top 5: {top5}")
        log(f"  Cell done in {time.time()-tc:.0f}s")

        # Save intermediate
        with open(os.path.join(OUT_DIR, 'per_cell_pi.json'), 'w') as f:
            json.dump(per_cell_results, f, indent=2)
        with open(os.path.join(OUT_DIR, 'bootstrap_ranks.json'), 'w') as f:
            json.dump(bootstrap_results, f, indent=2)

    # Cross-cell aggregation
    log("Computing cross-cell summary...")
    avg_ranks = {}
    avg_pi = {}
    for fname in FEATURE_NAMES:
        r = [per_cell_results[c][fname]['rank'] for c in CELLS]
        p = [per_cell_results[c][fname]['importance_mean'] for c in CELLS]
        avg_ranks[fname] = float(np.mean(r))
        avg_pi[fname] = float(np.mean(p))

    sorted_features = sorted(FEATURE_NAMES, key=lambda f: avg_ranks[f])

    # Family importance
    family_importance = {}
    for family, features in FEATURE_CATEGORIES.items():
        fam_pi = float(np.mean([avg_pi[f] for f in features]))
        fam_rank = float(np.mean([avg_ranks[f] for f in features]))
        family_importance[family] = {
            'avg_pi': fam_pi,
            'avg_rank': fam_rank,
            'features': features,
            'feature_ranks': {f: avg_ranks[f] for f in features},
        }

    sorted_families = sorted(
        family_importance.keys(),
        key=lambda f: family_importance[f]['avg_pi'],
        reverse=True
    )

    # Cross-cell bootstrap stability
    cross_boot = {}
    for fname in FEATURE_NAMES:
        meds = [bootstrap_results[c][fname]['median_rank'] for c in CELLS]
        lows = [bootstrap_results[c][fname]['rank_ci_low'] for c in CELLS]
        highs = [bootstrap_results[c][fname]['rank_ci_high'] for c in CELLS]
        cross_boot[fname] = {
            'avg_median_rank': float(np.mean(meds)),
            'avg_ci_low': float(np.mean(lows)),
            'avg_ci_high': float(np.mean(highs)),
            'ci_width': float(np.mean([h - l for h, l in zip(highs, lows)])),
        }

    summary = {
        'cross_cell_avg_rank': {f: avg_ranks[f] for f in sorted_features},
        'cross_cell_avg_pi': {f: avg_pi[f] for f in sorted_features},
        'family_importance_ranked': [
            {'family': f, **family_importance[f]} for f in sorted_families
        ],
        'top_family': sorted_families[0],
        'perplexity_is_top_family': sorted_families[0] == 'perplexity',
        'bootstrap_stability': {f: cross_boot[f] for f in sorted_features},
        'n_cells': len(CELLS),
        'n_bootstrap': N_BOOTSTRAP,
        'n_trees_main': N_TREES_MAIN,
        'n_repeats_main': N_REPEATS_MAIN,
        'n_trees_boot': N_TREES_BOOT,
        'n_repeats_boot': N_REPEATS_BOOT,
        'seed': SEED,
    }

    with open(os.path.join(OUT_DIR, 'summary.json'), 'w') as f:
        json.dump(summary, f, indent=2)

    # LaTeX table
    latex = generate_latex_table(
        per_cell_results, bootstrap_results,
        avg_ranks, avg_pi, family_importance, sorted_families
    )
    with open(os.path.join(OUT_DIR, 'latex_table.tex'), 'w') as f:
        f.write(latex)

    elapsed = time.time() - t0
    log(f"\n{'='*60}")
    log("SUMMARY")
    log(f"{'='*60}")
    log(f"Family ranking by avg PI:")
    for i, fam in enumerate(sorted_families):
        fi = family_importance[fam]
        log(f"  {i+1}. {fam}: avg_pi={fi['avg_pi']:.4f}, avg_rank={fi['avg_rank']:.1f}")
    log(f"Perplexity is top family: {summary['perplexity_is_top_family']}")
    log(f"Top 5 features by cross-cell avg rank:")
    for f in sorted_features[:5]:
        bs = cross_boot[f]
        log(f"  {f}: rank={avg_ranks[f]:.1f}, pi={avg_pi[f]:.4f}, "
            f"boot_med={bs['avg_median_rank']:.1f} [{bs['avg_ci_low']:.1f},{bs['avg_ci_high']:.1f}]")
    log(f"Total time: {elapsed:.0f}s ({elapsed/60:.1f}min)")
    log("DONE")


if __name__ == '__main__':
    main()
