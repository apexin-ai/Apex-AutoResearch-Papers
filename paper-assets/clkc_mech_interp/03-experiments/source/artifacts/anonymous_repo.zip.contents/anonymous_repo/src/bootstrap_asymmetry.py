"""Bootstrap CI for cross-lingual transfer asymmetry."""

import argparse
import json
import numpy as np
import torch
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score
from sklearn.preprocessing import StandardScaler


def load_activations(path):
    d = torch.load(path, map_location='cpu', weights_only=True)
    n_train = d['split_sizes']['train']
    act = d['activations'].float().numpy()
    labels = d['labels'].numpy()
    return act[:n_train], act[n_train:], labels[:n_train], labels[n_train:]


def bootstrap_asymmetry(en_path, zh_path, zh_en_layer, en_zh_layer, n_bootstrap=1000, seed=42):
    en_train, en_test, en_train_y, en_test_y = load_activations(en_path)
    zh_train, zh_test, zh_train_y, zh_test_y = load_activations(zh_path)

    scaler_zh_en = StandardScaler()
    X_train_zh_en = scaler_zh_en.fit_transform(zh_train[:, zh_en_layer, :])
    X_test_zh_en = scaler_zh_en.transform(en_test[:, zh_en_layer, :])
    clf_zh_en = LogisticRegression(max_iter=1000, class_weight='balanced', random_state=seed)
    clf_zh_en.fit(X_train_zh_en, zh_train_y)

    scaler_en_zh = StandardScaler()
    X_train_en_zh = scaler_en_zh.fit_transform(en_train[:, en_zh_layer, :])
    X_test_en_zh = scaler_en_zh.transform(zh_test[:, en_zh_layer, :])
    clf_en_zh = LogisticRegression(max_iter=1000, class_weight='balanced', random_state=seed)
    clf_en_zh.fit(X_train_en_zh, en_train_y)

    pred_zh_en = clf_zh_en.predict(X_test_zh_en)
    pred_en_zh = clf_en_zh.predict(X_test_en_zh)
    obs_zh_en = balanced_accuracy_score(en_test_y, pred_zh_en)
    obs_en_zh = balanced_accuracy_score(zh_test_y, pred_en_zh)

    rng = np.random.RandomState(seed)
    diffs = []
    for _ in range(n_bootstrap):
        idx_en = rng.choice(len(en_test_y), len(en_test_y), replace=True)
        idx_zh = rng.choice(len(zh_test_y), len(zh_test_y), replace=True)
        acc_zh_en = balanced_accuracy_score(en_test_y[idx_en], pred_zh_en[idx_en])
        acc_en_zh = balanced_accuracy_score(zh_test_y[idx_zh], pred_en_zh[idx_zh])
        diffs.append(acc_zh_en - acc_en_zh)

    diffs = np.array(diffs)
    ci_low, ci_high = np.percentile(diffs, [2.5, 97.5])
    return {
        'zh_en_balanced_acc': round(float(obs_zh_en), 4),
        'en_zh_balanced_acc': round(float(obs_en_zh), 4),
        'observed_diff': round(float(obs_zh_en - obs_en_zh), 4),
        'bootstrap_mean_diff': round(float(diffs.mean()), 4),
        'ci_95_low': round(float(ci_low), 4),
        'ci_95_high': round(float(ci_high), 4),
        'ci_excludes_zero': bool(ci_low > 0 or ci_high < 0),
        'n_bootstrap': n_bootstrap,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--activation_dir', required=True)
    parser.add_argument('--zh_en_layer', type=int, required=True)
    parser.add_argument('--en_zh_layer', type=int, required=True)
    parser.add_argument('--n_bootstrap', type=int, default=1000)
    parser.add_argument('--output', default=None)
    args = parser.parse_args()

    result = bootstrap_asymmetry(
        f'{args.activation_dir}/en_activations.pt',
        f'{args.activation_dir}/zh_activations.pt',
        args.zh_en_layer, args.en_zh_layer, args.n_bootstrap
    )
    print(json.dumps(result, indent=2))
    if args.output:
        from pathlib import Path
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, 'w') as f:
            json.dump(result, f, indent=2)
        print(f'Saved to {args.output}')
