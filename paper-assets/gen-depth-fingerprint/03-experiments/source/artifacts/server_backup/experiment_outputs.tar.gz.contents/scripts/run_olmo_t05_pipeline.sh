#!/bin/bash
set -e
export CUDA_VISIBLE_DEVICES=0
cd /root/gen-depth-fingerprint
PYTHON=/root/miniconda3/bin/python

echo "=== Step A: Feature extraction (OLMo t=0.5) ==="
echo "Start: $(date)"
$PYTHON extract_features.py \
    --input data/olmo-2-1b-t05/generations_shard0.jsonl \
    --output data/features_olmo-2-1b-t05.csv \
    --device cuda:0 \
    --batch-size 16
echo "Feature extraction done: $(date)"

echo "=== Step B: LOGO classification ==="
$PYTHON -c "
import json, os, sys
import numpy as np
import pandas as pd
from scipy.stats import spearmanr
from xgboost import XGBClassifier
from sklearn.metrics import f1_score

FEATURES = ['entropy_mean', 'entropy_std', 'entropy_min', 'entropy_max',
            'tail_decay', 'ttr', 'hapax_ratio']
RESULTS_DIR = '/root/gen-depth-fingerprint/results'
features_csv = 'data/features_olmo-2-1b-t05.csv'
result_json = os.path.join(RESULTS_DIR, 'temp_olmo-2-1b_t0.5_eval.json')

df = pd.read_csv(features_csv)
print(f'Loaded {len(df)} rows from {features_csv}')
print(f'Columns: {list(df.columns)}')
print(f'Depth distribution: {df[\"depth\"].value_counts().to_dict()}')

# Train/test split by seed
unique_seeds = sorted(df['seed_id'].unique())
n_train = int(len(unique_seeds) * 0.8)
train_seeds = set(unique_seeds[:n_train])
test_seeds = set(unique_seeds[n_train:])
train_df = df[df['seed_id'].isin(train_seeds)]
test_df = df[df['seed_id'].isin(test_seeds)]
print(f'Train: {len(train_df)} rows ({len(train_seeds)} seeds), Test: {len(test_df)} rows ({len(test_seeds)} seeds)')

results = {'model': 'olmo-2-1b', 'temperature': 0.5, 'n_seeds': len(unique_seeds),
           'n_train': len(train_df), 'n_test': len(test_df)}

# Bootstrap CI
def bootstrap_ci(y_true, y_pred, n_boot=1000, ci=0.95, metric='f1'):
    rng = np.random.default_rng(42)
    scores = []
    for _ in range(n_boot):
        idx = rng.choice(len(y_true), size=len(y_true), replace=True)
        yt, yp = np.array(y_true)[idx], np.array(y_pred)[idx]
        if len(set(yt)) < 2:
            continue
        if metric == 'f1':
            avg = 'macro' if len(set(yt)) > 2 else 'binary'
            scores.append(f1_score(yt, yp, average=avg, zero_division=0))
    alpha = (1 - ci) / 2
    return (np.percentile(scores, alpha * 100), np.percentile(scores, (1 - alpha) * 100))

XGB_PARAMS = {'n_estimators': 200, 'max_depth': 4, 'learning_rate': 0.1,
              'subsample': 0.8, 'colsample_bytree': 0.8, 'random_state': 42,
              'eval_metric': 'logloss', 'use_label_encoder': False}

# Binary: depth=0 vs depth>0
train_bin = train_df.copy()
train_bin['label'] = (train_bin['depth'] > 0).astype(int)
test_bin = test_df.copy()
test_bin['label'] = (test_bin['depth'] > 0).astype(int)

params_bin = dict(XGB_PARAMS)
params_bin['objective'] = 'binary:logistic'
clf_bin = XGBClassifier(**params_bin)
clf_bin.fit(train_bin[FEATURES].values, train_bin['label'].values)
y_pred_bin = clf_bin.predict(test_bin[FEATURES].values)
y_test_bin = test_bin['label'].values
bin_f1 = float(f1_score(y_test_bin, y_pred_bin, average='binary'))
bin_ci = bootstrap_ci(y_test_bin, y_pred_bin)
results['binary_f1'] = round(bin_f1, 4)
results['binary_ci_95'] = [round(bin_ci[0], 4), round(bin_ci[1], 4)]
results['binary_n_test'] = int(len(test_bin))

# 3-class: depth 0 vs 1 vs 2+
train_ds3 = train_df.copy()
train_ds3['label'] = train_ds3['depth'].clip(upper=2)
test_3c = test_df.copy()
test_3c['label'] = test_3c['depth'].clip(upper=2)

params3 = dict(XGB_PARAMS)
params3['num_class'] = 3
params3['objective'] = 'multi:softmax'
clf3 = XGBClassifier(**params3)
clf3.fit(train_ds3[FEATURES].values, train_ds3['label'].values)
y_pred3 = clf3.predict(test_3c[FEATURES].values)
y_test3 = test_3c['label'].values
three_f1 = float(f1_score(y_test3, y_pred3, average='macro'))
three_ci = bootstrap_ci(y_test3, y_pred3)
results['three_class_f1'] = round(three_f1, 4)
results['three_class_ci_95'] = [round(three_ci[0], 4), round(three_ci[1], 4)]
results['three_class_n_test'] = int(len(test_3c))

# Spearman rho for entropy_mean vs depth
rho, pval = spearmanr(test_df['entropy_mean'], test_df['depth'])
results['entropy_mean_spearman_rho'] = round(float(rho), 4)
results['entropy_mean_spearman_p'] = float(pval)

# Per-feature Spearman
per_feat_rho = {}
for feat in FEATURES:
    r, p = spearmanr(test_df[feat], test_df['depth'])
    per_feat_rho[feat] = round(float(r), 4)
results['per_feature_spearman'] = per_feat_rho

os.makedirs(RESULTS_DIR, exist_ok=True)
with open(result_json, 'w') as f:
    json.dump(results, f, indent=2)

print(f'Binary F1: {bin_f1:.4f}  CI: [{bin_ci[0]:.4f}, {bin_ci[1]:.4f}]')
print(f'3-class F1: {three_f1:.4f}  CI: [{three_ci[0]:.4f}, {three_ci[1]:.4f}]')
print(f'entropy_mean Spearman rho: {rho:.4f} (p={pval:.2e})')
print(f'Results saved to: {result_json}')
"
echo "=== Pipeline complete: $(date) ==="
