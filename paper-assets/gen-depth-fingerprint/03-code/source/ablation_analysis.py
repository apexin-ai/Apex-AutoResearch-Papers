# ablation_analysis.py — Feature ablation, trend analysis, perplexity pre-validation
# Input:  data/features.csv (4609 rows), data/generations.jsonl (4609 rows)
# Output: results/ablation_results.json, results/trend_analysis.json,
#         results/depth_trends.png, results/perplexity_by_depth.json
# Deps:   xgboost, scikit-learn, scipy, matplotlib, numpy, pandas, torch, transformers

import matplotlib
matplotlib.use('Agg')

import argparse
import json
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats as sp_stats
from scipy.stats import spearmanr
from pathlib import Path


FEATURES_REF = ['entropy_mean', 'entropy_std', 'entropy_min', 'entropy_max', 'tail_decay']
FEATURES_SURF = ['ttr', 'hapax_ratio']
FEATURES_ALL = FEATURES_REF + FEATURES_SURF

MODEL_PATHS = [
    '/root/autodl-tmp/.hf_cache/EleutherAI/pythia-410m',
    '/root/autodl-tmp/models/pythia-410m/models--EleutherAI--pythia-410m/snapshots/9879c9b5f8bea9051dcb0e68dff21493d67e9d4f',
]


def _stratified_sample(df, n_per_depth, seed=42):
    parts = []
    for d in sorted(df['depth'].unique()):
        sub = df[df['depth'] == d]
        parts.append(sub.sample(min(n_per_depth, len(sub)), random_state=seed))
    return pd.concat(parts).reset_index(drop=True)


def bootstrap_compare(scores_a, scores_b, n_bootstrap=1000, alpha=0.05):
    """Bootstrap paired comparison: resample fold-level scores, return mean diff, 95% CI, two-sided p."""
    np.random.seed(42)
    n = len(scores_a)
    diffs = []
    for _ in range(n_bootstrap):
        idx = np.random.choice(n, size=n, replace=True)
        diff = np.mean(scores_a[idx]) - np.mean(scores_b[idx])
        diffs.append(diff)
    diffs = np.array(diffs)
    ci_lower = float(np.percentile(diffs, 100 * alpha / 2))
    ci_upper = float(np.percentile(diffs, 100 * (1 - alpha / 2)))
    p_value = float(min(np.mean(diffs <= 0), np.mean(diffs >= 0)) * 2)
    return float(np.mean(diffs)), ci_lower, ci_upper, p_value


def part_a(input_path, output_dir, dry_run=False):
    from sklearn.model_selection import StratifiedKFold
    from sklearn.metrics import f1_score
    from xgboost import XGBClassifier

    df = pd.read_csv(input_path)

    if dry_run:
        df = _stratified_sample(df, 20)

    df['label'] = df['depth'].apply(lambda d: 0 if d == 0 else (1 if d == 1 else 2))

    if not dry_run:
        gen0 = df[df['label'] == 0]
        gen1 = df[df['label'] == 1]
        gen2p = df[df['label'] == 2]
        gen2p_sampled = pd.concat([
            gen2p[gen2p['depth'] == d].sample(333, random_state=42) for d in [2, 3, 4]
        ])
        target_n = min(len(gen0), len(gen1), len(gen2p_sampled))
        df = pd.concat([
            gen0.sample(target_n, random_state=42),
            gen1.sample(target_n, random_state=42),
            gen2p_sampled.sample(target_n, random_state=42),
        ]).reset_index(drop=True)

    y = df['label'].values
    min_class_n = int(np.bincount(y).min())
    n_folds = min(10, min_class_n)
    n_folds = max(2, n_folds)

    feature_sets = {
        'reference_only': FEATURES_REF,
        'surface_only': FEATURES_SURF,
        'full': FEATURES_ALL,
    }

    results = {}
    fold_scores = {}

    for name, feats in feature_sets.items():
        X = df[feats].values
        skf = StratifiedKFold(n_splits=n_folds, shuffle=True, random_state=42)
        macro_f1s, per_class_f1s = [], []

        for train_idx, test_idx in skf.split(X, y):
            clf = XGBClassifier(
                n_estimators=100, max_depth=6, learning_rate=0.1,
                random_state=42, verbosity=0, eval_metric='mlogloss',
            )
            clf.fit(X[train_idx], y[train_idx])
            pred = clf.predict(X[test_idx])
            macro_f1s.append(f1_score(y[test_idx], pred, average='macro', zero_division=0))
            per_class_f1s.append(f1_score(y[test_idx], pred, average=None, labels=[0, 1, 2], zero_division=0))

        macro_f1s = np.array(macro_f1s)
        per_class_f1s = np.array(per_class_f1s)
        fold_scores[name] = macro_f1s

        results[name] = {
            'macro_f1_mean': float(macro_f1s.mean()),
            'macro_f1_std': float(macro_f1s.std()),
            'per_class_f1': {
                'gen-0': float(per_class_f1s[:, 0].mean()),
                'gen-1': float(per_class_f1s[:, 1].mean()),
                'gen-2+': float(per_class_f1s[:, 2].mean()),
            },
        }

    # Bootstrap pairwise comparisons with Bonferroni correction (3 comparisons, alpha=0.05/3)
    pairs = [('full', 'reference_only'), ('full', 'surface_only'), ('reference_only', 'surface_only')]
    bonferroni_alpha = 0.05 / len(pairs)
    bootstrap_results = {}
    for a, b in pairs:
        mean_diff, ci_lower, ci_upper, p_val = bootstrap_compare(fold_scores[a], fold_scores[b])
        bootstrap_results[f'{a}_vs_{b}'] = {
            'mean_diff': mean_diff,
            'ci_lower': ci_lower,
            'ci_upper': ci_upper,
            'p_value': p_val,
            'significant_bonferroni': p_val < bonferroni_alpha,
        }

    results['bootstrap_comparisons'] = bootstrap_results
    results['bonferroni_alpha'] = bonferroni_alpha
    results['n_samples'] = len(df)
    results['n_folds'] = n_folds

    print("\n=== Part A: Feature Ablation ===")
    print(f"Samples: {len(df)} (balanced 1:1:1), Folds: {n_folds}")
    print(f"{'Feature Set':<20} {'Macro-F1':>14} {'gen-0':>8} {'gen-1':>8} {'gen-2+':>8}")
    print("-" * 62)
    for name in ['reference_only', 'surface_only', 'full']:
        r = results[name]
        print(f"{name:<20} {r['macro_f1_mean']:.4f}±{r['macro_f1_std']:.4f}"
              f"   {r['per_class_f1']['gen-0']:.4f}   {r['per_class_f1']['gen-1']:.4f}   {r['per_class_f1']['gen-2+']:.4f}")
    print(f"\nBootstrap pairwise comparisons (n_bootstrap=1000, Bonferroni α={bonferroni_alpha:.4f}):")
    for key, val in bootstrap_results.items():
        sig = "significant (Bonferroni corrected)" if val['significant_bonferroni'] else "ns"
        print(f"  {key}: diff={val['mean_diff']:+.4f} [{val['ci_lower']:.4f}, {val['ci_upper']:.4f}], p={val['p_value']:.4f} → {sig}")

    out_path = os.path.join(output_dir, 'ablation_results.json')
    with open(out_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out_path}")
    return results


def part_b(input_path, output_dir, dry_run=False):
    df = pd.read_csv(input_path)

    if dry_run:
        df = _stratified_sample(df, 20)

    depths = sorted(df['depth'].unique())

    depth_stats = {}
    for d in depths:
        sub = df[df['depth'] == d]
        depth_stats[int(d)] = {
            feat: {'mean': float(sub[feat].mean()), 'std': float(sub[feat].std())}
            for feat in FEATURES_ALL
        }

    trend_results = {}
    for feat in FEATURES_ALL:
        x = df['depth'].values.astype(float)
        y = df[feat].values.astype(float)

        # Linear regression kept for trend-line plotting only
        slope, intercept, r_value, p_value_lr, std_err = sp_stats.linregress(x, y)

        # Spearman rank correlation — primary monotonic-trend test
        rho, p_value = spearmanr(x, y)

        # Cohen's d between adjacent depths: measures if per-step shift shrinks (H1) or persists (H2)
        effect_sizes = []
        for i in range(len(depths) - 1):
            group_i = df.loc[df['depth'] == depths[i], feat].values
            group_next = df.loc[df['depth'] == depths[i + 1], feat].values
            pooled_std = np.sqrt((np.std(group_i)**2 + np.std(group_next)**2) / 2)
            cohen_d = abs(np.mean(group_i) - np.mean(group_next)) / pooled_std if pooled_std > 0 else 0.0
            effect_sizes.append(float(cohen_d))

        # Effect-size trend: negative rho means effect sizes decrease with depth (convergence)
        if len(effect_sizes) >= 3:
            es_trend_rho, es_trend_p = spearmanr(list(range(len(effect_sizes))), effect_sizes)
        else:
            es_trend_rho, es_trend_p = float('nan'), float('nan')

        # H1: effect sizes decrease (es_trend_rho < 0, p < 0.05) — converging to attractor
        # H2: strong monotonic trend (|rho| > 0.5, p < 0.05) AND effect sizes don't decrease — persistent drift
        # Otherwise: inconclusive
        if not np.isnan(es_trend_rho) and es_trend_rho < 0 and es_trend_p < 0.05:
            interpretation = 'attractor (H1)'
        elif abs(rho) > 0.5 and p_value < 0.05 and (np.isnan(es_trend_rho) or es_trend_rho >= 0):
            direction = 'increasing' if rho > 0 else 'decreasing'
            interpretation = f'divergence (H2, {direction})'
        else:
            interpretation = 'inconclusive'

        trend_results[feat] = {
            'spearman_rho': float(rho),
            'spearman_p': float(p_value),
            'effect_sizes': effect_sizes,
            'es_trend_rho': float(es_trend_rho) if not np.isnan(es_trend_rho) else None,
            'es_trend_p': float(es_trend_p) if not np.isnan(es_trend_p) else None,
            'slope': float(slope),
            'intercept': float(intercept),
            'interpretation': interpretation,
        }

    print("\n=== Part B: H1/H2 Trend Analysis ===")
    print(f"Samples: {len(df)}")
    print(f"\n{'Feature':<15} {'Spearman ρ':>12} {'p-value':>10} {'Effect sizes (adj.)':>30} {'Interpretation'}")
    print("-" * 90)
    for feat in FEATURES_ALL:
        r = trend_results[feat]
        es_str = ', '.join(f'{e:.3f}' for e in r['effect_sizes'])
        print(f"{feat:<15} {r['spearman_rho']:>12.4f} {r['spearman_p']:>10.2e} {es_str:>30} {r['interpretation']}")

    if any(r['es_trend_rho'] is not None for r in trend_results.values()):
        print(f"\nEffect-size trend (Spearman of |d_i| vs position):")
        for feat in FEATURES_ALL:
            r = trend_results[feat]
            if r['es_trend_rho'] is not None:
                print(f"  {feat}: ρ={r['es_trend_rho']:.4f}, p={r['es_trend_p']:.4f}")

    print(f"\nPer-depth means:")
    header = f"{'Feature':<15}" + "".join(f" {'d=' + str(d):>12}" for d in depths)
    print(header)
    for feat in FEATURES_ALL:
        row = f"{feat:<15}" + "".join(f" {depth_stats[d][feat]['mean']:>12.4f}" for d in depths)
        print(row)

    fig, axes = plt.subplots(2, 4, figsize=(20, 10))
    axes = axes.flatten()
    for i, feat in enumerate(FEATURES_ALL):
        ax = axes[i]
        means = [depth_stats[d][feat]['mean'] for d in depths]
        stds = [depth_stats[d][feat]['std'] for d in depths]

        ax.errorbar(depths, means, yerr=stds, fmt='o-', capsize=5, capthick=1.5,
                     linewidth=1.5, markersize=6, color='#1f77b4')

        r = trend_results[feat]
        x_line = np.linspace(min(depths), max(depths), 100)
        y_line = r['slope'] * x_line + r['intercept']
        ax.plot(x_line, y_line, '--', color='red', alpha=0.7, linewidth=1.5)

        ax.set_xlabel('Depth', fontsize=11)
        ax.set_ylabel(feat, fontsize=11)
        ax.set_title(f"{feat}\nρ={r['spearman_rho']:.4f}, p={r['spearman_p']:.2e}", fontsize=10)
        ax.set_xticks(depths)

    for j in range(len(FEATURES_ALL), len(axes)):
        axes[j].set_visible(False)

    plt.tight_layout()
    png_path = os.path.join(output_dir, 'depth_trends.png')
    plt.savefig(png_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"\nSaved: {png_path}")

    output = {'depth_stats': depth_stats, 'trend_results': trend_results, 'n_samples': len(df)}
    json_path = os.path.join(output_dir, 'trend_analysis.json')
    with open(json_path, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"Saved: {json_path}")
    return output


def part_c(generations_path, output_dir, device='cuda:0', dry_run=False):
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    records = []
    with open(generations_path) as f:
        for line in f:
            records.append(json.loads(line))

    if dry_run:
        by_depth = {}
        for r in records:
            by_depth.setdefault(r['depth'], []).append(r)
        sampled = []
        for d in sorted(by_depth.keys()):
            sampled.extend(by_depth[d][:4])
        records = sampled

    print(f"\n=== Part C: Perplexity Pre-validation ===")
    print(f"Records: {len(records)}")

    model_path = None
    for p in MODEL_PATHS:
        if os.path.isdir(p):
            model_path = p
            break
    if model_path is None:
        raise FileNotFoundError(f"Pythia-410M not found at any of: {MODEL_PATHS}")

    print(f"Loading model from {model_path} ...")
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path, dtype=torch.float16).to(device)
    model.eval()

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    perplexities = []
    with torch.no_grad():
        for i, rec in enumerate(records):
            inputs = tokenizer(rec['text'], return_tensors='pt', truncation=True, max_length=512)
            input_ids = inputs['input_ids'].to(device)

            if input_ids.shape[1] < 2:
                perplexities.append({'id': rec['id'], 'depth': rec['depth'], 'perplexity': float('nan')})
                continue

            outputs = model(input_ids, labels=input_ids)
            ppl = float(np.exp(outputs.loss.item()))
            perplexities.append({'id': rec['id'], 'depth': rec['depth'], 'perplexity': ppl})

            if (i + 1) % 200 == 0 or (i + 1) == len(records):
                print(f"  Processed {i+1}/{len(records)}")

    depth_ppls = {}
    for p in perplexities:
        if not np.isnan(p['perplexity']):
            depth_ppls.setdefault(p['depth'], []).append(p['perplexity'])

    depth_summary = {}
    for d in sorted(depth_ppls.keys()):
        vals = depth_ppls[d]
        depth_summary[int(d)] = {
            'mean': float(np.mean(vals)),
            'std': float(np.std(vals)),
            'count': len(vals),
        }

    groups = [depth_ppls[d] for d in sorted(depth_ppls.keys())]
    if len(groups) >= 2 and all(len(g) >= 1 for g in groups):
        kw_stat, kw_p = sp_stats.kruskal(*groups)
    else:
        kw_stat, kw_p = float('nan'), float('nan')

    print(f"\n{'Depth':>6} {'Mean PPL':>12} {'Std':>10} {'Count':>6}")
    print("-" * 38)
    for d in sorted(depth_summary.keys()):
        s = depth_summary[d]
        print(f"{d:>6} {s['mean']:>12.2f} {s['std']:>10.2f} {s['count']:>6}")
    print(f"\nKruskal-Wallis: H={kw_stat:.4f}, p={kw_p:.4e}")

    output = {
        'depth_summary': depth_summary,
        'kruskal_wallis': {'H_stat': float(kw_stat), 'p_value': float(kw_p)},
        'n_records': len(records),
    }
    out_path = os.path.join(output_dir, 'perplexity_by_depth.json')
    with open(out_path, 'w') as f:
        json.dump(output, f, indent=2)
    print(f"Saved: {out_path}")
    return output


def main():
    parser = argparse.ArgumentParser(description='Ablation analysis for gen-depth-fingerprint')
    parser.add_argument('--parts', nargs='+', default=['A', 'B', 'C'], choices=['A', 'B', 'C'])
    parser.add_argument('--input', default='data/features.csv')
    parser.add_argument('--generations', default='data/generations.jsonl')
    parser.add_argument('--output-dir', default='results/')
    parser.add_argument('--device', default='cuda:0')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    if args.dry_run:
        print("[DRY-RUN MODE]")

    if 'A' in args.parts:
        part_a(args.input, args.output_dir, dry_run=args.dry_run)
    if 'B' in args.parts:
        part_b(args.input, args.output_dir, dry_run=args.dry_run)
    if 'C' in args.parts:
        part_c(args.generations, args.output_dir, device=args.device, dry_run=args.dry_run)

    print("\nDone.")


if __name__ == '__main__':
    main()
