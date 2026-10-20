"""
analyze_decoding_strategy.py — Cohen's d, Spearman rho, silhouette for decoding strategy comparison.
Compares nucleus (existing) vs greedy vs top-k for 3 generators.
"""
import pandas as pd
import numpy as np
from scipy.stats import spearmanr
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
import json, os, sys

FEATURES = ['entropy_mean', 'entropy_std', 'entropy_min', 'entropy_max',
            'tail_decay', 'ttr', 'hapax_ratio']
SHAPE_FEATURES = ['entropy_max', 'entropy_min', 'tail_decay']
MODELS = ['pythia-2.8b', 'olmo-2-1b', 'qwen3-1.7b']
STRATEGIES = ['nucleus', 'greedy', 'topk']

DATA_DIR = '/root/gen-depth-fingerprint/data'

FEATURE_FILES = {
    ('pythia-2.8b', 'nucleus'): f'{DATA_DIR}/features_pythia-2.8b.csv',
    ('olmo-2-1b', 'nucleus'): f'{DATA_DIR}/features_olmo-2-1b.csv',
    ('qwen3-1.7b', 'nucleus'): f'{DATA_DIR}/features_qwen3-1.7b.csv',
    ('pythia-2.8b', 'greedy'): f'{DATA_DIR}/features_pythia-2.8b-greedy.csv',
    ('pythia-2.8b', 'topk'): f'{DATA_DIR}/features_pythia-2.8b-topk.csv',
    ('olmo-2-1b', 'greedy'): f'{DATA_DIR}/features_olmo-2-1b-greedy.csv',
    ('olmo-2-1b', 'topk'): f'{DATA_DIR}/features_olmo-2-1b-topk.csv',
    ('qwen3-1.7b', 'greedy'): f'{DATA_DIR}/features_qwen3-1.7b-greedy.csv',
    ('qwen3-1.7b', 'topk'): f'{DATA_DIR}/features_qwen3-1.7b-topk.csv',
}


def compute_cohens_d(df, feat):
    g1 = df[df['depth'] == 1][feat].dropna()
    g2 = df[df['depth'] >= 2][feat].dropna()
    if len(g1) == 0 or len(g2) == 0:
        return float('nan')
    pooled_std = np.sqrt((g1.std()**2 + g2.std()**2) / 2)
    if pooled_std == 0:
        return 0.0
    return abs(g1.mean() - g2.mean()) / pooled_std


def compute_spearman_rho(df, feat):
    rho, _ = spearmanr(df['depth'], df[feat])
    return abs(rho)


def compute_metrics(df):
    metrics = {}
    for feat in FEATURES:
        d = compute_cohens_d(df, feat)
        rho = compute_spearman_rho(df, feat)
        metrics[feat] = {'d': d, 'abs_rho': rho}
    return metrics


def compute_silhouette_k2(metrics):
    X = np.array([[metrics[f]['abs_rho'], metrics[f]['d']] for f in FEATURES])
    X_scaled = StandardScaler().fit_transform(X)
    labels = np.array([0, 1, 1, 1, 1, 0, 0])
    return silhouette_score(X_scaled, labels)


def main():
    results = {}
    all_metrics = {}

    for model in MODELS:
        for strategy in STRATEGIES:
            key = (model, strategy)
            path = FEATURE_FILES[key]
            if not os.path.exists(path):
                print(f"MISSING: {path}")
                continue

            df = pd.read_csv(path)
            print(f"Loaded {key}: {len(df)} rows, depths={sorted(df['depth'].unique())}")
            metrics = compute_metrics(df)
            sil = compute_silhouette_k2(metrics)
            all_metrics[key] = metrics

            results[f"{model}/{strategy}"] = {
                'n_rows': len(df),
                'silhouette_k2': round(sil, 4),
                'features': {f: {'d': round(metrics[f]['d'], 4), 'abs_rho': round(metrics[f]['abs_rho'], 4)} for f in FEATURES},
            }

    # Print summary table
    print("\n" + "="*90)
    print("COHEN'S d  (gen-1 vs gen-2+)  — shape features highlighted")
    print("="*90)
    header = f"{'Model':<15} {'Strategy':<10}"
    for f in FEATURES:
        tag = " *" if f in SHAPE_FEATURES else ""
        header += f" {f[:12]+tag:>14}"
    print(header)
    print("-"*90)

    for model in MODELS:
        for strategy in STRATEGIES:
            key = f"{model}/{strategy}"
            if key not in results:
                continue
            row = f"{model:<15} {strategy:<10}"
            for f in FEATURES:
                d = results[key]['features'][f]['d']
                marker = "<<" if f in SHAPE_FEATURES and d < 0.15 else ""
                row += f" {d:>12.4f}{marker:>2}"
            print(row)
        print()

    print("\n" + "="*90)
    print("|Spearman rho| (pooled)")
    print("="*90)
    header = f"{'Model':<15} {'Strategy':<10}"
    for f in FEATURES:
        header += f" {f[:14]:>14}"
    print(header)
    print("-"*90)

    for model in MODELS:
        for strategy in STRATEGIES:
            key = f"{model}/{strategy}"
            if key not in results:
                continue
            row = f"{model:<15} {strategy:<10}"
            for f in FEATURES:
                rho = results[key]['features'][f]['abs_rho']
                row += f" {rho:>14.4f}"
            print(row)
        print()

    print("\n" + "="*50)
    print("Silhouette (k=2, drifting vs near-stationary)")
    print("="*50)
    for model in MODELS:
        for strategy in STRATEGIES:
            key = f"{model}/{strategy}"
            if key not in results:
                continue
            print(f"  {model:<15} {strategy:<10} sil={results[key]['silhouette_k2']:.4f}")
        print()

    # Shape stability verdict
    print("\n" + "="*50)
    print("SHAPE STABILITY VERDICT (d < 0.15 threshold)")
    print("="*50)
    for model in MODELS:
        for strategy in STRATEGIES:
            key = f"{model}/{strategy}"
            if key not in results:
                continue
            shape_ds = [results[key]['features'][f]['d'] for f in SHAPE_FEATURES]
            all_stable = all(d < 0.15 for d in shape_ds)
            max_d = max(shape_ds)
            status = "PASS" if all_stable else "FAIL"
            print(f"  {model:<15} {strategy:<10} {status}  max_shape_d={max_d:.4f}  ({', '.join(f'{f}={d:.4f}' for f, d in zip(SHAPE_FEATURES, shape_ds))})")

    # Save JSON
    out_path = '/root/gen-depth-fingerprint/results/decoding_strategy_results.json'
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
