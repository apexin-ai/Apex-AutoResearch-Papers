"""
Item-level residual variance analysis for FF vs MC benchmarks.
Decomposes residual variance and regresses on item features.
"""
import json
import os
import re
import sys
import warnings
from collections import defaultdict

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import statsmodels.api as sm

warnings.filterwarnings('ignore')

# ── Config ──────────────────────────────────────────────────────────────
EXP_DIR = '/root/nlp_variance_gtheory/results/exp002/'
ITEM_DIR = '/root/nlp_variance_gtheory/data/'
OUT_DIR = '/tmp/ff_residual_output/'
os.makedirs(OUT_DIR, exist_ok=True)

MODELS = ['gemma', 'llama', 'mistral', 'qwen', 'deepseek', 'internlm', 'olmo', 'yi']
BENCHMARKS = ['gsm8k', 'math', 'mmlu', 'arc', 'hellaswag']
FF_BENCHMARKS = ['gsm8k', 'math']
MC_BENCHMARKS = ['mmlu', 'arc', 'hellaswag']

# Wong 2011 color-blind-safe palette
WONG_COLORS = {
    'gsm8k': '#E69F00',    # orange
    'math': '#56B4E9',     # sky blue
    'mmlu': '#009E73',     # green
    'arc': '#F0E442',      # yellow
    'hellaswag': '#0072B2', # blue
}

FACETS = ['model', 'temperature', 'prompt_template', 'seed', 'ordering']


def load_jsonl(path):
    rows = []
    with open(path) as f:
        for line in f:
            rows.append(json.loads(line))
    return rows


def load_benchmark_data(benchmark):
    """Load all model data for a benchmark."""
    all_rows = []
    for model in MODELS:
        path = os.path.join(EXP_DIR, f'{model}_{benchmark}.jsonl')
        if not os.path.exists(path):
            continue
        rows = load_jsonl(path)
        all_rows.extend(rows)
    return all_rows


def load_item_metadata(benchmark):
    """Load item metadata from item files."""
    path = os.path.join(ITEM_DIR, f'{benchmark}_items_exp002.json')
    if not os.path.exists(path):
        path = os.path.join(ITEM_DIR, f'{benchmark}_items.json')
    if not os.path.exists(path):
        return {}
    with open(path) as f:
        items = json.load(f)
    return {item['item_id']: item for item in items}


def count_gsm8k_steps(raw_answer):
    """Count reasoning steps from GSM8K raw answer using <<...>> markers."""
    if not raw_answer:
        return 0
    return len(re.findall(r'<<[^>]+>>', raw_answer))


def compute_item_stats(all_rows, benchmark):
    """Compute per-item variance decomposition."""
    # Group by item
    item_data = defaultdict(list)
    for row in all_rows:
        item_data[row['item_id']].append(row)

    item_stats = {}
    for item_id, rows in item_data.items():
        corrects = np.array([r['correct'] for r in rows], dtype=float)
        n_obs = len(corrects)
        p_i = corrects.mean()
        var_total = corrects.var(ddof=1) if n_obs > 1 else 0.0

        # Per-model means
        model_means = defaultdict(list)
        for r in rows:
            model_means[r['model']].append(r['correct'])
        model_mean_vals = np.array([np.mean(v) for v in model_means.values()])
        var_between_model = model_mean_vals.var(ddof=1) if len(model_mean_vals) > 1 else 0.0

        # Per-temperature means
        temp_means = defaultdict(list)
        for r in rows:
            temp_means[r['temperature']].append(r['correct'])
        temp_mean_vals = np.array([np.mean(v) for v in temp_means.values()])
        var_between_temp = temp_mean_vals.var(ddof=1) if len(temp_mean_vals) > 1 else 0.0

        # Per-prompt means
        prompt_means = defaultdict(list)
        for r in rows:
            prompt_means[r['prompt_template']].append(r['correct'])
        prompt_mean_vals = np.array([np.mean(v) for v in prompt_means.values()])
        var_between_prompt = prompt_mean_vals.var(ddof=1) if len(prompt_mean_vals) > 1 else 0.0

        # Per-seed means
        seed_means = defaultdict(list)
        for r in rows:
            seed_means[r['seed']].append(r['correct'])
        seed_mean_vals = np.array([np.mean(v) for v in seed_means.values()])
        var_between_seed = seed_mean_vals.var(ddof=1) if len(seed_mean_vals) > 1 else 0.0

        # Per-ordering means
        order_means = defaultdict(list)
        for r in rows:
            order_means[r['ordering']].append(r['correct'])
        order_mean_vals = np.array([np.mean(v) for v in order_means.values()])
        var_between_order = order_mean_vals.var(ddof=1) if len(order_mean_vals) > 1 else 0.0

        # Residual: total minus all between-facet components
        var_explained = var_between_model + var_between_temp + var_between_prompt + var_between_seed + var_between_order
        var_residual = max(0.0, var_total - var_explained)

        item_stats[item_id] = {
            'item_id': item_id,
            'n_obs': n_obs,
            'p_i': float(p_i),
            'var_total': float(var_total),
            'var_between_model': float(var_between_model),
            'var_between_temp': float(var_between_temp),
            'var_between_prompt': float(var_between_prompt),
            'var_between_seed': float(var_between_seed),
            'var_between_order': float(var_between_order),
            'var_explained': float(var_explained),
            'var_residual': float(var_residual),
            'residual_pct': float(var_residual / var_total * 100) if var_total > 0 else 0.0,
        }
    return item_stats


def extract_features_gsm8k(item_stats, item_meta):
    """Extract item features for GSM8K."""
    features = {}
    for item_id, stats in item_stats.items():
        meta = item_meta.get(item_id, {})
        metadata = meta.get('metadata', {})
        raw_answer = metadata.get('raw_answer', '')

        n_steps = metadata.get('n_steps', count_gsm8k_steps(raw_answer))
        answer_len = len(str(meta.get('answer', '')))
        question_len = len(meta.get('question', ''))

        features[item_id] = {
            'difficulty': stats['p_i'],
            'difficulty_sq': stats['p_i'] ** 2,
            'n_steps': n_steps,
            'answer_length': answer_len,
            'question_length': question_len,
        }
    return features


def extract_features_math(item_stats, item_meta):
    """Extract item features for MATH."""
    features = {}
    for item_id, stats in item_stats.items():
        meta = item_meta.get(item_id, {})
        metadata = meta.get('metadata', {})

        problem_level = metadata.get('difficulty', 0)
        subject = metadata.get('subject', 'Unknown')
        solution = metadata.get('solution', '')
        answer_len = len(str(meta.get('answer', '')))
        solution_len = len(solution)

        features[item_id] = {
            'difficulty': stats['p_i'],
            'difficulty_sq': stats['p_i'] ** 2,
            'problem_level': int(problem_level),
            'answer_length': answer_len,
            'solution_length': solution_len,
            'subject': subject,
        }
    return features


def extract_features_mc(item_stats, item_meta, benchmark):
    """Extract item features for MC benchmarks."""
    features = {}
    for item_id, stats in item_stats.items():
        meta = item_meta.get(item_id, {})
        metadata = meta.get('metadata', {})

        n_choices = metadata.get('n_choices', len(meta.get('choices', [])))
        question_len = len(meta.get('question', ''))

        feat = {
            'difficulty': stats['p_i'],
            'difficulty_sq': stats['p_i'] ** 2,
            'n_choices': n_choices,
            'question_length': question_len,
        }

        if benchmark == 'mmlu':
            feat['subject'] = meta.get('subject', metadata.get('subject', 'unknown'))

        features[item_id] = feat
    return features


def run_regression(item_stats, features, benchmark):
    """Run OLS regression: residual_var ~ item features."""
    item_ids = sorted(set(item_stats.keys()) & set(features.keys()))

    y = np.array([item_stats[iid]['var_residual'] for iid in item_ids])

    # Determine numeric features (exclude categorical)
    sample_feat = features[item_ids[0]]
    numeric_cols = [k for k, v in sample_feat.items() if isinstance(v, (int, float))]
    categorical_cols = [k for k, v in sample_feat.items() if isinstance(v, str)]

    # Build X matrix
    X_data = {}
    for col in numeric_cols:
        X_data[col] = np.array([features[iid][col] for iid in item_ids], dtype=float)

    # One-hot encode categoricals (drop first)
    for col in categorical_cols:
        vals = [features[iid][col] for iid in item_ids]
        unique_vals = sorted(set(vals))
        if len(unique_vals) > 1:
            for uv in unique_vals[1:]:  # drop first
                X_data[f'{col}_{uv}'] = np.array([1.0 if v == uv else 0.0 for v in vals])

    feature_names = list(X_data.keys())
    X = np.column_stack([X_data[fn] for fn in feature_names])
    X = sm.add_constant(X)

    # Fit OLS
    model = sm.OLS(y, X).fit()

    # Also fit difficulty-only model for comparison
    X_diff = sm.add_constant(np.column_stack([
        X_data['difficulty'],
        X_data['difficulty_sq'],
    ]))
    model_diff = sm.OLS(y, X_diff).fit()

    coefficients = {}
    p_values = {}
    for i, name in enumerate(['const'] + feature_names):
        coefficients[name] = float(model.params[i])
        p_values[name] = float(model.pvalues[i])

    result = {
        'n_items': len(item_ids),
        'features_used': feature_names,
        'R2': float(model.rsquared),
        'adj_R2': float(model.rsquared_adj),
        'coefficients': coefficients,
        'p_values': p_values,
        'F_statistic': float(model.fvalue),
        'F_p_value': float(model.f_pvalue),
        'difficulty_only_R2': float(model_diff.rsquared),
        'difficulty_only_adj_R2': float(model_diff.rsquared_adj),
        'residual_var_mean': float(y.mean()),
        'residual_var_std': float(y.std()),
        'ols_summary': model.summary().as_text(),
    }

    return result, item_ids, y, X_data


def make_scatter_plot(item_ids, item_stats, features, benchmark, out_dir):
    """Scatter: difficulty vs residual variance with regression fit."""
    difficulty = np.array([features[iid]['difficulty'] for iid in item_ids])
    residual_var = np.array([item_stats[iid]['var_residual'] for iid in item_ids])

    fig, ax = plt.subplots(figsize=(5, 4))

    color = WONG_COLORS.get(benchmark, '#333333')
    ax.scatter(difficulty, residual_var, c=color, alpha=0.6, s=30, edgecolors='white', linewidth=0.5)

    # Quadratic fit
    mask = ~(np.isnan(difficulty) | np.isnan(residual_var))
    d = difficulty[mask]
    rv = residual_var[mask]
    if len(d) > 3:
        coeffs = np.polyfit(d, rv, 2)
        d_sorted = np.linspace(d.min(), d.max(), 100)
        rv_fit = np.polyval(coeffs, d_sorted)
        ax.plot(d_sorted, rv_fit, color='#CC79A7', linewidth=2, linestyle='-')

        # R² for quadratic
        X_q = sm.add_constant(np.column_stack([d, d**2]))
        mod = sm.OLS(rv, X_q).fit()
        r2 = mod.rsquared

        ax.text(0.05, 0.95, f'$R^2$ = {r2:.3f} (quadratic)',
                transform=ax.transAxes, fontsize=9, verticalalignment='top',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))

    bm_labels = {
        'gsm8k': 'GSM8K', 'math': 'MATH', 'mmlu': 'MMLU',
        'arc': 'ARC-Challenge', 'hellaswag': 'HellaSwag'
    }
    ax.set_xlabel('Item Difficulty ($p_i$)', fontsize=11)
    ax.set_ylabel('Residual Variance', fontsize=11)
    ax.set_title(f'{bm_labels.get(benchmark, benchmark)}', fontsize=12, fontweight='bold')
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(bottom=-0.005)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.tick_params(labelsize=9)

    plt.tight_layout()
    pdf_path = os.path.join(out_dir, f'difficulty_vs_residual_{benchmark}.pdf')
    fig.savefig(pdf_path, dpi=300, bbox_inches='tight')
    png_path = os.path.join(out_dir, f'difficulty_vs_residual_{benchmark}.png')
    fig.savefig(png_path, dpi=150, bbox_inches='tight')
    plt.close(fig)
    return pdf_path


def main():
    all_results = {'benchmarks': {}}
    all_item_features = {}

    for benchmark in BENCHMARKS:
        print(f'\n{"="*60}')
        print(f'Processing {benchmark.upper()}...')
        print(f'{"="*60}')

        # Load data
        rows = load_benchmark_data(benchmark)
        if not rows:
            print(f'  No data for {benchmark}, skipping.')
            continue

        n_models = len(set(r['model'] for r in rows))
        print(f'  Loaded {len(rows)} rows from {n_models} models')

        # Load item metadata
        item_meta = load_item_metadata(benchmark)
        print(f'  Item metadata: {len(item_meta)} items')

        # Compute item stats
        item_stats = compute_item_stats(rows, benchmark)
        print(f'  Computed stats for {len(item_stats)} items')

        # Summary stats
        residual_pcts = [s['residual_pct'] for s in item_stats.values()]
        var_residuals = [s['var_residual'] for s in item_stats.values()]
        difficulties = [s['p_i'] for s in item_stats.values()]
        print(f'  Mean difficulty: {np.mean(difficulties):.3f} (range {np.min(difficulties):.3f}-{np.max(difficulties):.3f})')
        print(f'  Mean residual var: {np.mean(var_residuals):.4f} (std {np.std(var_residuals):.4f})')
        print(f'  Mean residual %: {np.mean(residual_pcts):.1f}% (range {np.min(residual_pcts):.1f}%-{np.max(residual_pcts):.1f}%)')

        # Extract features
        if benchmark == 'gsm8k':
            features = extract_features_gsm8k(item_stats, item_meta)
        elif benchmark == 'math':
            features = extract_features_math(item_stats, item_meta)
        else:
            features = extract_features_mc(item_stats, item_meta, benchmark)

        # Run regression
        reg_result, item_ids, y, X_data = run_regression(item_stats, features, benchmark)
        print(f'\n  Regression R²: {reg_result["R2"]:.4f} (adj {reg_result["adj_R2"]:.4f})')
        print(f'  Difficulty-only R²: {reg_result["difficulty_only_R2"]:.4f}')
        print(f'  F-stat: {reg_result["F_statistic"]:.2f} (p={reg_result["F_p_value"]:.2e})')

        sig_features = {k: v for k, v in reg_result['p_values'].items() if v < 0.05 and k != 'const'}
        print(f'  Significant features (p<0.05): {list(sig_features.keys())}')

        # Compute overall residual % for this benchmark
        total_var_sum = sum(s['var_total'] for s in item_stats.values())
        residual_var_sum = sum(s['var_residual'] for s in item_stats.values())
        overall_residual_pct = residual_var_sum / total_var_sum * 100 if total_var_sum > 0 else 0

        # Build interpretation
        is_ff = benchmark in FF_BENCHMARKS
        if reg_result['R2'] > 0.3:
            interp = f"Item features explain {reg_result['R2']*100:.1f}% of residual variance, indicating substantial systematic structure."
        elif reg_result['R2'] > 0.1:
            interp = f"Item features explain {reg_result['R2']*100:.1f}% of residual variance, indicating moderate systematic structure."
        else:
            interp = f"Item features explain only {reg_result['R2']*100:.1f}% of residual variance, suggesting the residual is predominantly random/stochastic."

        if is_ff:
            interp += f" As a free-form benchmark, the large residual ({overall_residual_pct:.1f}%) reflects inherent generation stochasticity."
        else:
            interp += f" As a multiple-choice benchmark, the residual ({overall_residual_pct:.1f}%) is relatively constrained."

        # Store result (without the lengthy OLS summary for the JSON)
        ols_summary = reg_result.pop('ols_summary')
        reg_result['overall_residual_pct'] = float(overall_residual_pct)
        reg_result['interpretation'] = interp
        reg_result['benchmark_type'] = 'free-form' if is_ff else 'multiple-choice'
        all_results['benchmarks'][benchmark] = reg_result

        # Print full OLS summary
        print(f'\n  OLS Summary:\n{ols_summary}')

        # Store item features
        for iid in item_ids:
            feat = features[iid].copy()
            feat.update(item_stats[iid])
            all_item_features.setdefault(benchmark, {})[iid] = feat

        # Scatter plot
        pdf_path = make_scatter_plot(item_ids, item_stats, features, benchmark, OUT_DIR)
        print(f'  Saved scatter plot: {pdf_path}')

    # ── Cross-benchmark comparison ──────────────────────────────────────
    print(f'\n{"="*60}')
    print('Cross-benchmark comparison: FF vs MC')
    print(f'{"="*60}')

    ff_r2s = [all_results['benchmarks'][b]['R2'] for b in FF_BENCHMARKS if b in all_results['benchmarks']]
    mc_r2s = [all_results['benchmarks'][b]['R2'] for b in MC_BENCHMARKS if b in all_results['benchmarks']]

    all_results['comparison'] = {
        'ff_mean_R2': float(np.mean(ff_r2s)) if ff_r2s else None,
        'mc_mean_R2': float(np.mean(mc_r2s)) if mc_r2s else None,
        'ff_benchmarks': FF_BENCHMARKS,
        'mc_benchmarks': MC_BENCHMARKS,
        'finding': (
            f"FF benchmarks have mean R²={np.mean(ff_r2s):.4f} vs MC mean R²={np.mean(mc_r2s):.4f}. "
            f"{'FF residuals are more systematic (item features explain more)' if np.mean(ff_r2s) > np.mean(mc_r2s) else 'MC residuals are more systematic'}."
        ) if ff_r2s and mc_r2s else 'Insufficient data for comparison',
    }
    print(f'  FF mean R²: {np.mean(ff_r2s):.4f}')
    print(f'  MC mean R²: {np.mean(mc_r2s):.4f}')

    # ── Save outputs ────────────────────────────────────────────────────
    with open(os.path.join(OUT_DIR, 'ff_residual_regression.json'), 'w') as f:
        json.dump(all_results, f, indent=2)
    print(f'\nSaved regression results to {OUT_DIR}ff_residual_regression.json')

    with open(os.path.join(OUT_DIR, 'item_features.json'), 'w') as f:
        json.dump(all_item_features, f, indent=2, default=str)
    print(f'Saved item features to {OUT_DIR}item_features.json')

    print('\nDone.')


if __name__ == '__main__':
    main()
