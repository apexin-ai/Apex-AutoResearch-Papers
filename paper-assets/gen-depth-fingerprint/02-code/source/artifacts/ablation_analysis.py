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
    n_folds = min(5, min_class_n)
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

    pairs = [('full', 'reference_only'), ('full', 'surface_only'), ('reference_only', 'surface_only')]
    t_tests = {}
    for a, b in pairs:
        t_stat, p_val = sp_stats.ttest_rel(fold_scores[a], fold_scores[b])
        t_tests[f'{a}_vs_{b}'] = {'t_stat': float(t_stat), 'p_value': float(p_val)}

    results['paired_t_tests'] = t_tests
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
    print("\nPaired t-tests:")
    for key, val in t_tests.items():
        sig = "***" if val['p_value'] < 0.001 else "**" if val['p_value'] < 0.01 else "*" if val['p_value'] < 0.05 else "ns"
        print(f"  {key}: t={val['t_stat']:.4f}, p={val['p_value']:.4f} {sig}")

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
        slope, intercept, r_value, p_value, std_err = sp_stats.linregress(x, y)
        r_sq = r_value ** 2

        if r_sq > 0.8 and p_value < 0.05:
            interpretation = f"divergence (H2, {'increasing' if slope > 0 else 'decreasing'})"
        elif r_sq < 0.3 or p_value >= 0.05:
            interpretation = 'attractor (H1)'
        else:
            interpretation = 'moderate trend'

        trend_results[feat] = {
            'slope': float(slope),
            'intercept': float(intercept),
            'r_squared': float(r_sq),
            'p_value': float(p_value),
            'std_err': float(std_err),
            'interpretation': interpretation,
        }

    print("\n=== Part B: H1/H2 Trend Analysis ===")
    print(f"Samples: {len(df)}")
    print(f"\n{'Feature':<15} {'Slope':>10} {'R²':>8} {'p-value':>10} {'Interpretation'}")
    print("-" * 72)
    for feat in FEATURES_ALL:
        r = trend_results[feat]
        print(f"{feat:<15} {r['slope']:>10.6f} {r['r_squared']:>8.4f} {r['p_value']:>10.2e} {r['interpretation']}")

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
        ax.set_title(f"{feat}\nslope={r['slope']:.4f}, R²={r['r_squared']:.4f}", fontsize=10)
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
