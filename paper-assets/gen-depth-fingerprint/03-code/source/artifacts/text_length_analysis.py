"""
text_length_analysis.py — plan-013 文本长度混淆控制
输入: data/*/generations.jsonl (原始文本) + data/features_all_models.csv (特征)
输出: data/text_length_analysis.json, data/text_length_boxplot.png
分析: 长度分布/相关性/归一化特征/长度匹配分类/dropout分析
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import json, os, sys
import numpy as np
import pandas as pd
from collections import Counter
from scipy.stats import spearmanr
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import f1_score
import xgboost as xgb

BASE = '/root/gen-depth-fingerprint'

MODEL_PATHS = {
    'pythia-2.8b': f'{BASE}/data/generations.jsonl',
    'pythia-1b':   f'{BASE}/data/pythia-1b/generations.jsonl',
    'olmo-2-1b':   f'{BASE}/data/olmo-2-1b/generations.jsonl',
    'qwen3-0.6b':  f'{BASE}/data/qwen3-0.6b/generations.jsonl',
    'qwen3-1.7b':  f'{BASE}/data/qwen3-1.7b/generations.jsonl',
}

MODEL_ORDER = ['pythia-2.8b', 'pythia-1b', 'olmo-2-1b', 'qwen3-0.6b', 'qwen3-1.7b']

def load_generations():
    rows = []
    for model, path in MODEL_PATHS.items():
        with open(path) as f:
            for line in f:
                d = json.loads(line)
                text = d['text']
                words = text.split()
                rows.append({
                    'model': model,
                    'seed_id': d['seed_id'],
                    'depth': d['depth'],
                    'text': text,
                    'char_count': len(text),
                    'word_count': len(words),
                    'token_count': d.get('token_count', None),
                })
    return pd.DataFrame(rows)

def load_features():
    return pd.read_csv(f'{BASE}/data/features_all_models.csv')

# ── 1. 长度分布 ──
def analyze_length_distribution(df):
    print('='*60)
    print('1. LENGTH DISTRIBUTION (mean ± std)')
    print('='*60)
    results = {}
    for model in MODEL_ORDER:
        mdf = df[df['model'] == model]
        print(f'\n  {model}:')
        model_res = {}
        for d in sorted(mdf['depth'].unique()):
            sub = mdf[mdf['depth'] == d]
            cm, cs = sub['char_count'].mean(), sub['char_count'].std()
            wm, ws = sub['word_count'].mean(), sub['word_count'].std()
            print(f'    depth {d}: chars={cm:.0f}±{cs:.0f}  words={wm:.1f}±{ws:.1f}  n={len(sub)}')
            model_res[int(d)] = {'n': len(sub), 'char_mean': round(cm,1), 'char_std': round(cs,1),
                                  'word_mean': round(wm,1), 'word_std': round(ws,1)}
        results[model] = model_res
    return results

def plot_boxplot(df):
    fig, axes = plt.subplots(1, 5, figsize=(20, 4), sharey=True)
    fig.subplots_adjust(wspace=0.08)
    for i, model in enumerate(MODEL_ORDER):
        ax = axes[i]
        mdf = df[df['model'] == model]
        depths = sorted(mdf['depth'].unique())
        data = [mdf[mdf['depth'] == d]['word_count'].values for d in depths]
        bp = ax.boxplot(data, labels=[str(d) for d in depths], widths=0.6,
                        patch_artist=True, medianprops=dict(color='black', linewidth=1.5))
        colors = plt.cm.Blues(np.linspace(0.3, 0.85, len(depths)))
        for patch, c in zip(bp['boxes'], colors):
            patch.set_facecolor(c)
        ax.set_xlabel('Generation Depth', fontsize=11)
        ax.set_title(model, fontsize=12, fontweight='bold')
        if i == 0:
            ax.set_ylabel('Word Count', fontsize=11)
        ax.tick_params(labelsize=10)
        ax.grid(axis='y', alpha=0.3)
    fig.suptitle('Text Length Distribution by Generation Depth', fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    out = f'{BASE}/data/text_length_boxplot.png'
    plt.savefig(out, dpi=150, bbox_inches='tight')
    print(f'\n  Box plot saved: {out}')

# ── 2. 长度与深度相关性 ──
def analyze_correlation(df):
    print('\n' + '='*60)
    print('2. SPEARMAN CORRELATION (word_count vs depth)')
    print('='*60)
    results = {}
    print(f'  {"Model":<15} {"ρ":>8} {"p-value":>12} {"Significant":>12}')
    print(f'  {"-"*47}')
    for model in MODEL_ORDER:
        mdf = df[df['model'] == model]
        rho, pval = spearmanr(mdf['word_count'], mdf['depth'])
        sig = 'Yes' if pval < 0.05 else 'No'
        print(f'  {model:<15} {rho:>8.4f} {pval:>12.2e} {sig:>12}')
        results[model] = {'rho': round(rho, 4), 'p_value': float(f'{pval:.4e}'), 'significant': pval < 0.05}
    return results

# ── 3. 长度归一化特征 ──
def normalized_ttr(text, window=200):
    words = text.split()[:window]
    if len(words) < 10:
        return None
    return len(set(words)) / len(words)

def normalized_hapax(text, window=200):
    words = text.split()[:window]
    if len(words) < 10:
        return None
    freq = Counter(words)
    return sum(1 for w, c in freq.items() if c == 1) / len(set(words))

def analyze_normalized_features(df, feat_df):
    print('\n' + '='*60)
    print('3. LENGTH-NORMALIZED FEATURES (window=200 words)')
    print('='*60)

    df = df.copy()
    df['norm_ttr'] = df['text'].apply(lambda t: normalized_ttr(t, 200))
    df['norm_hapax'] = df['text'].apply(lambda t: normalized_hapax(t, 200))

    results = {}
    for model in MODEL_ORDER:
        mdf = df[df['model'] == model].dropna(subset=['norm_ttr', 'norm_hapax'])
        fdf = feat_df[feat_df['model_name'] == model]

        print(f'\n  {model}:')
        print(f'    {"Depth":<8} {"TTR_orig":>10} {"TTR_norm":>10} {"Δ":>8} {"Hapax_orig":>12} {"Hapax_norm":>12} {"Δ":>8}')
        model_res = {}
        for d in sorted(mdf['depth'].unique()):
            orig_ttr = fdf[fdf['depth'] == d]['ttr'].mean()
            norm_ttr_val = mdf[mdf['depth'] == d]['norm_ttr'].mean()
            orig_hap = fdf[fdf['depth'] == d]['hapax_ratio'].mean()
            norm_hap_val = mdf[mdf['depth'] == d]['norm_hapax'].mean()
            d_ttr = norm_ttr_val - orig_ttr
            d_hap = norm_hap_val - orig_hap
            print(f'    {d:<8} {orig_ttr:>10.4f} {norm_ttr_val:>10.4f} {d_ttr:>+8.4f} {orig_hap:>12.4f} {norm_hap_val:>12.4f} {d_hap:>+8.4f}')
            model_res[int(d)] = {
                'ttr_orig': round(orig_ttr, 4), 'ttr_norm': round(norm_ttr_val, 4),
                'hapax_orig': round(orig_hap, 4), 'hapax_norm': round(norm_hap_val, 4),
            }
        results[model] = model_res

        # Spearman on normalized
        rho_ttr, p_ttr = spearmanr(mdf['depth'], mdf['norm_ttr'])
        rho_hap, p_hap = spearmanr(mdf['depth'], mdf['norm_hapax'])
        print(f'    Spearman norm_ttr~depth: ρ={rho_ttr:.4f}, p={p_ttr:.2e}')
        print(f'    Spearman norm_hapax~depth: ρ={rho_hap:.4f}, p={p_hap:.2e}')
        results[model]['spearman_norm_ttr'] = {'rho': round(rho_ttr, 4), 'p': float(f'{p_ttr:.4e}')}
        results[model]['spearman_norm_hapax'] = {'rho': round(rho_hap, 4), 'p': float(f'{p_hap:.4e}')}

    # Compare original vs normalized Spearman across models
    print('\n  CONCLUSION:')
    for model in MODEL_ORDER:
        fdf = feat_df[feat_df['model_name'] == model]
        mdf = df[df['model'] == model].dropna(subset=['norm_ttr'])
        rho_orig, _ = spearmanr(fdf['depth'], fdf['ttr'])
        rho_norm = results[model]['spearman_norm_ttr']['rho']
        verdict = 'trend preserved' if abs(rho_norm) > 0.05 and results[model]['spearman_norm_ttr']['p'] < 0.05 else 'trend weakened/gone'
        print(f'    {model}: orig_ρ={rho_orig:.4f} → norm_ρ={rho_norm:.4f}  ({verdict})')

    return results

# ── 4. 长度匹配分类器 ──
def length_matched_classifier(df, feat_df):
    print('\n' + '='*60)
    print('4. LENGTH-MATCHED CLASSIFIER (XGBoost 3-class)')
    print('='*60)

    feat_df = feat_df.copy()
    feat_df['depth_class'] = feat_df['depth'].apply(lambda d: min(d, 2))
    feature_cols = ['entropy_mean', 'entropy_std', 'entropy_min', 'entropy_max', 'tail_decay', 'ttr', 'hapax_ratio']

    # Merge word_count into features
    wc = df.groupby(['model', 'seed_id', 'depth'])['word_count'].first().reset_index()
    wc.columns = ['model_name', 'seed_id', 'depth', 'word_count']
    feat_merged = feat_df.merge(wc, on=['model_name', 'seed_id', 'depth'], how='left')

    results = {}

    for model in MODEL_ORDER:
        mdf = feat_merged[feat_merged['model_name'] == model].dropna(subset=['word_count']).copy()

        # Original (unmatched) CV
        X = mdf[feature_cols].values
        y = mdf['depth_class'].values
        f1_orig = _cv_f1(X, y)

        # Length-matched subsample
        n_bins = 10
        mdf['wc_bin'] = pd.qcut(mdf['word_count'], q=n_bins, labels=False, duplicates='drop')
        matched_idx = []
        for b in mdf['wc_bin'].unique():
            bin_df = mdf[mdf['wc_bin'] == b]
            counts_per_class = bin_df.groupby('depth_class').size()
            if len(counts_per_class) < 3:
                continue
            min_count = counts_per_class.min()
            if min_count == 0:
                continue
            for cls in counts_per_class.index:
                cls_rows = bin_df[bin_df['depth_class'] == cls]
                matched_idx.extend(cls_rows.sample(n=min_count, random_state=42).index.tolist())
        matched = mdf.loc[matched_idx]

        if len(matched) < 30:
            print(f'  {model}: insufficient matched samples ({len(matched)}), skipping')
            results[model] = {'original_f1': round(f1_orig, 4), 'matched_f1': None, 'delta': None, 'matched_n': len(matched)}
            continue

        X_m = matched[feature_cols].values
        y_m = matched['depth_class'].values
        f1_matched = _cv_f1(X_m, y_m)

        delta = f1_matched - f1_orig
        print(f'  {model}: orig_F1={f1_orig:.4f}  matched_F1={f1_matched:.4f}  Δ={delta:+.4f}  (n_orig={len(mdf)}, n_matched={len(matched)})')
        results[model] = {
            'original_f1': round(f1_orig, 4), 'matched_f1': round(f1_matched, 4),
            'delta': round(delta, 4), 'original_n': len(mdf), 'matched_n': len(matched),
        }

    deltas = [v['delta'] for v in results.values() if v['delta'] is not None]
    avg_delta = np.mean(deltas) if deltas else 0
    print(f'\n  Average Δ F1: {avg_delta:+.4f}')
    if abs(avg_delta) < 0.05:
        print('  CONCLUSION: Length is NOT a major confound (|avg Δ| < 0.05)')
    else:
        print('  CONCLUSION: Length may be a confound (|avg Δ| >= 0.05)')
    results['avg_delta'] = round(avg_delta, 4)
    return results

def _cv_f1(X, y, n_splits=5):
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    scores = []
    for tr, te in skf.split(X, y):
        clf = xgb.XGBClassifier(n_estimators=200, max_depth=6, learning_rate=0.1,
                                 random_state=42, eval_metric='mlogloss',
                                 use_label_encoder=False, verbosity=0)
        clf.fit(X[tr], y[tr])
        pred = clf.predict(X[te])
        scores.append(f1_score(y[te], pred, average='macro'))
    return np.mean(scores)

# ── 5. Dropout 分析 ──
def analyze_dropout(df):
    print('\n' + '='*60)
    print('5. DROPOUT ANALYSIS')
    print('='*60)

    results = {}
    for model in MODEL_ORDER:
        mdf = df[df['model'] == model]
        depths = sorted(mdf['depth'].unique())
        print(f'\n  {model}:')
        model_res = {}
        for i in range(len(depths) - 1):
            d, d1 = depths[i], depths[i+1]
            seeds_d = set(mdf[mdf['depth'] == d]['seed_id'])
            seeds_d1 = set(mdf[mdf['depth'] == d1]['seed_id'])
            dropped = seeds_d - seeds_d1
            dropout_rate = len(dropped) / len(seeds_d) if len(seeds_d) > 0 else 0

            # Length comparison
            kept = mdf[(mdf['depth'] == d) & (mdf['seed_id'].isin(seeds_d1))]
            lost = mdf[(mdf['depth'] == d) & (mdf['seed_id'].isin(dropped))]
            kept_wc = kept['word_count'].mean() if len(kept) > 0 else 0
            lost_wc = lost['word_count'].mean() if len(lost) > 0 else 0

            print(f'    {d}→{d1}: dropout={len(dropped)}/{len(seeds_d)} ({dropout_rate:.1%}), '
                  f'lost_avg_wc={lost_wc:.0f}, kept_avg_wc={kept_wc:.0f}')
            model_res[f'{d}->{d1}'] = {
                'dropped': len(dropped), 'total': len(seeds_d),
                'dropout_rate': round(dropout_rate, 4),
                'lost_avg_wordcount': round(lost_wc, 1),
                'kept_avg_wordcount': round(kept_wc, 1),
            }
        results[model] = model_res

    # Summary: are shorter texts more likely to dropout?
    print('\n  CONCLUSION:')
    shorter_dropout_count = 0
    total_transitions = 0
    for model, transitions in results.items():
        for t, v in transitions.items():
            if v['dropped'] > 0:
                total_transitions += 1
                if v['lost_avg_wordcount'] < v['kept_avg_wordcount']:
                    shorter_dropout_count += 1
    if total_transitions > 0:
        frac = shorter_dropout_count / total_transitions
        if frac > 0.7:
            print(f'    Shorter texts dropout more often ({shorter_dropout_count}/{total_transitions} transitions)')
        elif frac < 0.3:
            print(f'    Longer texts dropout more often ({total_transitions - shorter_dropout_count}/{total_transitions} transitions)')
        else:
            print(f'    No clear length-dropout pattern ({shorter_dropout_count}/{total_transitions} shorter-dropout)')

    return results

# ── Main ──
if __name__ == '__main__':
    print('Loading data...')
    df = load_generations()
    feat_df = load_features()
    print(f'  Generations: {len(df)} rows, Features: {len(feat_df)} rows')

    all_results = {}

    all_results['length_distribution'] = analyze_length_distribution(df)
    plot_boxplot(df)
    all_results['correlation'] = analyze_correlation(df)
    all_results['normalized_features'] = analyze_normalized_features(df, feat_df)
    all_results['length_matched_classifier'] = length_matched_classifier(df, feat_df)
    all_results['dropout'] = analyze_dropout(df)

    out_path = f'{BASE}/data/text_length_analysis.json'
    with open(out_path, 'w') as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    print(f'\nResults saved: {out_path}')
