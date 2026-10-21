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


def bootstrap_ci(scores, n_bootstrap=1000, ci=0.95):
    rng = np.random.RandomState(42)
    means = []
    for _ in range(n_bootstrap):
        idx = rng.randint(0, len(scores), size=len(scores))
        means.append(np.mean(scores[idx]))
    lower = np.percentile(means, (1 - ci) / 2 * 100)
    upper = np.percentile(means, (1 + ci) / 2 * 100)
    return float(lower), float(upper)


def cohens_d(group1, group2):
    n1, n2 = len(group1), len(group2)
    if n1 < 2 or n2 < 2:
        return float('nan')
    var1, var2 = group1.var(ddof=1), group2.var(ddof=1)
    pooled_std = np.sqrt(((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2))
    if pooled_std == 0:
        return 0.0
    return float((group1.mean() - group2.mean()) / pooled_std)


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

        ci_lower, ci_upper = bootstrap_ci(macro_f1s)
        results[name] = {
            'macro_f1_mean': float(macro_f1s.mean()),
            'macro_f1_std': float(macro_f1s.std()),
            'bootstrap_ci_95': [ci_lower, ci_upper],
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
    print(f"{'Feature Set':<20} {'Macro-F1':>14} {'95% CI':>16} {'gen-0':>8} {'gen-1':>8} {'gen-2+':>8}")
    print("-" * 80)
    for name in ['reference_only', 'surface_only', 'full']:
        r = results[name]
        ci = r['bootstrap_ci_95']
        print(f"{name:<20} {r['macro_f1_mean']:.4f}+/-{r['macro_f1_std']:.4f}"
              f"   [{ci[0]:.4f},{ci[1]:.4f}]"
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

    depth_groups = {}
    for d in depths:
        depth_groups[int(d)] = df[df['depth'] == d]

    depth_stats = {}
    for d in depths:
        sub = depth_groups[int(d)]
        depth_stats[int(d)] = {
            feat: {'mean': float(sub[feat].mean()), 'std': float(sub[feat].std())}
            for feat in FEATURES_ALL
        }

    trend_results = {}
    for feat in FEATURES_ALL:
        x = df['depth'].values.astype(float)
        y = df[feat].values.astype(float)
        rho, p_value = spearmanr(x, y)

        effect_sizes = {}
        for idx in range(len(depths) - 1):
            d_curr = int(depths[idx])
            d_next = int(depths[idx + 1])
            g1 = depth_groups[d_curr][feat].values
            g2 = depth_groups[d_next][feat].values
            key = f"d_{d_curr}{d_next}"
            effect_sizes[key] = cohens_d(g1, g2)

        es_vals = [abs(v) for v in effect_sizes.values() if not np.isnan(v)]
        es_decreasing = all(es_vals[i] > es_vals[i + 1] for i in range(len(es_vals) - 1)) if len(es_vals) >= 2 else False

        if abs(rho) > 0.5 and p_value < 0.05:
            label = "H2 (drift)"
        else:
            label = "H1 (near-stationary)"

        depth_means = [float(depth_stats[int(d)][feat]['mean']) for d in depths]
        depth_stds = [float(depth_stats[int(d)][feat]['std']) for d in depths]

        trend_results[feat] = {
            'spearman_rho': float(rho),
            'spearman_p': float(p_value),
            'label': label,
            'depth_means': depth_means,
            'depth_stds': depth_stds,
            'effect_sizes': effect_sizes,
            'effect_size_decreasing': es_decreasing,
        }

    print("\n=== Part B: H1/H2 Trend Analysis (Spearman) ===")
    print(f"Samples: {len(df)}")
    print(f"\n{'Feature':<15} {'rho':>8} {'p-value':>10} {'Label':<22} {'ES decreasing'}")
    print("-" * 75)
    for feat in FEATURES_ALL:
        r = trend_results[feat]
        print(f"{feat:<15} {r['spearman_rho']:>8.4f} {r['spearman_p']:>10.2e} {r['label']:<22} {r['effect_size_decreasing']}")

    print(f"\nEffect sizes (Cohen's d between adjacent depths):")
    es_keys = list(trend_results[FEATURES_ALL[0]]['effect_sizes'].keys())
    header = f"{'Feature':<15}" + "".join(f" {k:>8}" for k in es_keys)
    print(header)
    for feat in FEATURES_ALL:
        row = f"{feat:<15}" + "".join(f" {trend_results[feat]['effect_sizes'][k]:>8.4f}" for k in es_keys)
        print(row)

    print(f"\nPer-depth means:")
    header = f"{'Feature':<15}" + "".join(f" {'d=' + str(d):>12}" for d in depths)
    print(header)
    for feat in FEATURES_ALL:
        row = f"{feat:<15}" + "".join(f" {depth_stats[int(d)][feat]['mean']:>12.4f}" for d in depths)
        print(row)

    n_cols = 4
    n_rows = 2
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(20, 10))
    axes = axes.flatten()
    for i, feat in enumerate(FEATURES_ALL):
        ax = axes[i]
        means = trend_results[feat]['depth_means']
        stds = trend_results[feat]['depth_stds']
        n_per_depth = [len(depth_groups[int(d)]) for d in depths]
        std_errs = [s / np.sqrt(n) for s, n in zip(stds, n_per_depth)]

        ax.errorbar(depths, means, yerr=std_errs, fmt='o-', capsize=5, capthick=1.5,
                     linewidth=1.5, markersize=6, color='#1f77b4')

        r = trend_results[feat]
        sig_marker = "*" if r['spearman_p'] < 0.05 else ""
        ax.set_xlabel('Depth', fontsize=11)
        ax.set_ylabel(feat, fontsize=11)
        ax.set_title(f"{feat}\n$\\rho$={r['spearman_rho']:.4f}, p={r['spearman_p']:.2e} {sig_marker}\n{r['label']}", fontsize=10)
        ax.set_xticks(depths)

    for j in range(len(FEATURES_ALL), len(axes)):
        axes[j].set_visible(False)

    plt.tight_layout()
    png_path = os.path.join(output_dir, 'depth_trends.png')
    plt.savefig(png_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"\nSaved: {png_path}")

    output = {'trend_results': trend_results, 'n_samples': len(df)}
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
    texts_by_id = {}
    with torch.no_grad():
        for i, rec in enumerate(records):
            text = rec['text']
            inputs = tokenizer(text, return_tensors='pt', truncation=True, max_length=512)
            input_ids = inputs['input_ids'].to(device)

            if input_ids.shape[1] < 2:
                perplexities.append({'id': rec['id'], 'depth': rec['depth'], 'perplexity': float('nan'), 'n_tokens': input_ids.shape[1]})
                texts_by_id[rec['id']] = text
                continue

            outputs = model(input_ids, labels=input_ids)
            ppl = float(np.exp(outputs.loss.item()))
            n_tokens = input_ids.shape[1]
            perplexities.append({'id': rec['id'], 'depth': rec['depth'], 'perplexity': ppl, 'n_tokens': n_tokens})
            texts_by_id[rec['id']] = text

            if (i + 1) % 200 == 0 or (i + 1) == len(records):
                print(f"  Processed {i+1}/{len(records)}")

    depth_ppls = {}
    for p in perplexities:
        if not np.isnan(p['perplexity']):
            depth_ppls.setdefault(p['depth'], []).append(p)

    def is_degenerate(text, tokenizer_ref):
        tokens = tokenizer_ref.encode(text)
        if len(tokens) < 20:
            return True
        repeat_count = sum(1 for a, b in zip(tokens[:-1], tokens[1:]) if a == b)
        if repeat_count / max(len(tokens) - 1, 1) > 0.5:
            return True
        return False

    degenerate_examples = []
    per_depth = {}
    for d in sorted(depth_ppls.keys()):
        entries = depth_ppls[d]
        ppl_vals = np.array([e['perplexity'] for e in entries])
        high_ppl_mask = ppl_vals > 100
        high_ppl_ratio = float(high_ppl_mask.sum() / len(ppl_vals))

        clean_ppls = []
        for e in entries:
            text = texts_by_id[e['id']]
            if e['perplexity'] > 100 and is_degenerate(text, tokenizer):
                degenerate_examples.append({
                    'depth': int(d),
                    'ppl': float(e['perplexity']),
                    'text_preview': text[:200],
                })
            else:
                clean_ppls.append(e['perplexity'])

        clean_ppls = np.array(clean_ppls) if clean_ppls else np.array([])

        per_depth[str(int(d))] = {
            'mean': float(np.mean(ppl_vals)),
            'median': float(np.median(ppl_vals)),
            'std': float(np.std(ppl_vals)),
            'n': len(ppl_vals),
            'high_ppl_ratio': high_ppl_ratio,
            'clean_mean': float(np.mean(clean_ppls)) if len(clean_ppls) > 0 else float('nan'),
            'clean_median': float(np.median(clean_ppls)) if len(clean_ppls) > 0 else float('nan'),
            'clean_n': len(clean_ppls),
        }

    groups_all = [np.array([e['perplexity'] for e in depth_ppls[d]]) for d in sorted(depth_ppls.keys())]
    if len(groups_all) >= 2 and all(len(g) >= 1 for g in groups_all):
        kw_stat, kw_p = sp_stats.kruskal(*groups_all)
    else:
        kw_stat, kw_p = float('nan'), float('nan')

    clean_groups = []
    for d in sorted(depth_ppls.keys()):
        entries = depth_ppls[d]
        cg = [e['perplexity'] for e in entries
              if not (e['perplexity'] > 100 and is_degenerate(texts_by_id[e['id']], tokenizer))]
        clean_groups.append(np.array(cg) if cg else np.array([]))

    if len(clean_groups) >= 2 and all(len(g) >= 1 for g in clean_groups):
        kw_clean_stat, kw_clean_p = sp_stats.kruskal(*clean_groups)
    else:
        kw_clean_stat, kw_clean_p = float('nan'), float('nan')

    print(f"\n{'Depth':>6} {'Mean':>10} {'Median':>10} {'Std':>10} {'N':>6} {'HighPPL%':>9} {'CleanMean':>10} {'CleanMed':>10} {'CleanN':>7}")
    print("-" * 84)
    for d_str in sorted(per_depth.keys(), key=int):
        s = per_depth[d_str]
        cm = f"{s['clean_mean']:.2f}" if not np.isnan(s['clean_mean']) else "N/A"
        cmd = f"{s['clean_median']:.2f}" if not np.isnan(s['clean_median']) else "N/A"
        print(f"{d_str:>6} {s['mean']:>10.2f} {s['median']:>10.2f} {s['std']:>10.2f} {s['n']:>6} {s['high_ppl_ratio']:>8.2%} {cm:>10} {cmd:>10} {s['clean_n']:>7}")
    print(f"\nKruskal-Wallis (all):   H={kw_stat:.4f}, p={kw_p:.4e}")
    print(f"Kruskal-Wallis (clean): H={kw_clean_stat:.4f}, p={kw_clean_p:.4e}")

    if degenerate_examples:
        print(f"\nDegenerate samples (PPL>100, top 5):")
        for ex in degenerate_examples[:5]:
            print(f"  depth={ex['depth']}, ppl={ex['ppl']:.1f}: {ex['text_preview'][:120]}...")

    output = {
        'per_depth': per_depth,
        'kruskal_wallis': {'H': float(kw_stat), 'p': float(kw_p)},
        'kruskal_wallis_clean': {'H': float(kw_clean_stat), 'p': float(kw_clean_p)},
        'degenerate_examples': degenerate_examples[:20],
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
