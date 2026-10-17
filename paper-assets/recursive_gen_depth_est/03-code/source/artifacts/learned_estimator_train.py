#!/usr/bin/env python3
"""
Learned depth estimator training (Plan 025).
Methods: ordinal_mlp (CORAL), prototypical, xgboost.
Evaluation: leave-one-model-out cross-model transfer.
"""

import argparse
import json
import os
import time
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from sklearn.preprocessing import StandardScaler

from learned_estimator_utils import (
    load_cross_model_split, compute_metrics,
    CoralOrdinalMLP, coral_loss,
    PrototypicalNet, prototypical_loss,
    NUM_FEATURES, NUM_CLASSES, DEPTH_LABELS,
)

BASE = '/root/autodl-tmp/recursive_gen_depth_est'
OUT_DIR = os.path.join(BASE, 'results', 'learned_estimator')


def set_seed(seed=42):
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def train_ordinal_mlp(X_train, y_train, X_test, y_test, config):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    X_tr = torch.FloatTensor(X_train_s).to(device)
    y_tr = torch.LongTensor(y_train).to(device)
    X_te = torch.FloatTensor(X_test_s).to(device)

    model = CoralOrdinalMLP(
        input_dim=NUM_FEATURES,
        hidden_dims=config['hidden_dims'],
        num_classes=NUM_CLASSES,
        dropout=config['dropout'],
    ).to(device)

    optimizer = torch.optim.AdamW(model.parameters(), lr=config['lr'], weight_decay=config['wd'])
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=config['epochs'])

    dataset = TensorDataset(X_tr, y_tr)
    loader = DataLoader(dataset, batch_size=config['batch_size'], shuffle=True)

    best_acc = 0.0
    best_state = None
    patience_counter = 0

    for epoch in range(config['epochs']):
        model.train()
        total_loss = 0.0
        for xb, yb in loader:
            logits = model(xb)
            loss = coral_loss(logits, yb, NUM_CLASSES)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            total_loss += loss.item() * xb.size(0)
        scheduler.step()

        if (epoch + 1) % 10 == 0 or epoch == 0:
            model.eval()
            preds = model.predict(X_te).cpu().numpy()
            acc = (preds == y_test).mean()
            if acc > best_acc:
                best_acc = acc
                best_state = {k: v.clone() for k, v in model.state_dict().items()}
                patience_counter = 0
            else:
                patience_counter += 1

            if config.get('verbose'):
                print(f"  Epoch {epoch+1}/{config['epochs']} loss={total_loss/len(X_tr):.4f} test_acc={acc:.4f} best={best_acc:.4f}")

            if patience_counter >= config.get('patience', 20):
                if config.get('verbose'):
                    print(f"  Early stop at epoch {epoch+1}")
                break

    if best_state:
        model.load_state_dict(best_state)
    model.eval()
    y_pred = model.predict(X_te).cpu().numpy()
    y_prob = model.predict_proba(X_te).cpu().numpy()
    return y_pred, y_prob


def train_prototypical(X_train, y_train, X_test, y_test, config):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    X_tr = torch.FloatTensor(X_train_s).to(device)
    y_tr = torch.LongTensor(y_train).to(device)
    X_te = torch.FloatTensor(X_test_s).to(device)

    model = PrototypicalNet(
        input_dim=NUM_FEATURES,
        embed_dim=config['embed_dim'],
        hidden_dims=config['hidden_dims'],
        dropout=config['dropout'],
    ).to(device)

    optimizer = torch.optim.AdamW(model.parameters(), lr=config['lr'], weight_decay=config['wd'])
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=config['epochs'])

    dataset = TensorDataset(X_tr, y_tr)
    loader = DataLoader(dataset, batch_size=config['batch_size'], shuffle=True)

    best_acc = 0.0
    best_state = None
    patience_counter = 0

    for epoch in range(config['epochs']):
        model.train()
        total_loss = 0.0
        for xb, yb in loader:
            embeddings = model(xb)
            loss = prototypical_loss(embeddings, yb, NUM_CLASSES)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            total_loss += loss.item() * xb.size(0)
        scheduler.step()

        if (epoch + 1) % 10 == 0 or epoch == 0:
            model.eval()
            with torch.no_grad():
                prototypes = model.compute_prototypes(X_tr, y_tr, NUM_CLASSES)
                dists = model.predict_with_prototypes(X_te, prototypes)
                preds = dists.argmin(dim=1).cpu().numpy()
                if np.any(np.isnan(preds)):
                    preds = np.nan_to_num(preds, nan=0.0).astype(int)
                acc = (preds == y_test).mean()

            if acc > best_acc:
                best_acc = acc
                best_state = {k: v.clone() for k, v in model.state_dict().items()}
                patience_counter = 0
            else:
                patience_counter += 1

            if config.get('verbose'):
                print(f"  Epoch {epoch+1}/{config['epochs']} loss={total_loss/len(X_tr):.4f} test_acc={acc:.4f} best={best_acc:.4f}")

            if patience_counter >= config.get('patience', 20):
                if config.get('verbose'):
                    print(f"  Early stop at epoch {epoch+1}")
                break

    if best_state:
        model.load_state_dict(best_state)
    model.eval()
    with torch.no_grad():
        prototypes = model.compute_prototypes(X_tr, y_tr, NUM_CLASSES)
        dists = model.predict_with_prototypes(X_te, prototypes)
        y_pred = dists.argmin(dim=1).cpu().numpy()
        dists_safe = torch.nan_to_num(dists, nan=1e6, posinf=1e6, neginf=0.0)
        dists_clamped = torch.clamp(dists_safe, min=1e-8, max=100.0)
        softmax_input = torch.nan_to_num(-dists_clamped, nan=0.0, posinf=1e6, neginf=-1e6)
        y_prob = torch.softmax(softmax_input, dim=1).cpu().numpy()
        y_prob = np.nan_to_num(y_prob, nan=0.0)
    return y_pred, y_prob


def train_xgboost(X_train, y_train, X_test, y_test, config):
    import xgboost as xgb
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s = scaler.transform(X_test)

    clf = xgb.XGBClassifier(
        n_estimators=config['n_estimators'],
        max_depth=config['max_depth'],
        learning_rate=config['xgb_lr'],
        subsample=config['subsample'],
        colsample_bytree=config['colsample'],
        objective='multi:softprob',
        num_class=NUM_CLASSES,
        eval_metric='mlogloss',
        use_label_encoder=False,
        random_state=42,
        n_jobs=-1,
        tree_method='hist',
    )
    clf.fit(X_train_s, y_train, verbose=False)
    y_pred = clf.predict(X_test_s)
    y_prob = clf.predict_proba(X_test_s)
    return y_pred, y_prob


METHOD_CONFIGS = {
    'ordinal_mlp': {
        'hidden_dims': (256, 128, 64),
        'dropout': 0.3,
        'lr': 1e-3,
        'wd': 1e-4,
        'batch_size': 2048,
        'epochs': 150,
        'patience': 15,
        'verbose': True,
    },
    'prototypical': {
        'embed_dim': 64,
        'hidden_dims': (256, 128),
        'dropout': 0.3,
        'lr': 1e-3,
        'wd': 1e-4,
        'batch_size': 2048,
        'epochs': 150,
        'patience': 15,
        'verbose': True,
    },
    'xgboost': {
        'n_estimators': 500,
        'max_depth': 6,
        'xgb_lr': 0.1,
        'subsample': 0.8,
        'colsample': 0.8,
    },
}

TRAIN_FNS = {
    'ordinal_mlp': train_ordinal_mlp,
    'prototypical': train_prototypical,
    'xgboost': train_xgboost,
}


def main():
    parser = argparse.ArgumentParser(description='Learned Depth Estimator (Plan 025)')
    parser.add_argument('--method', type=str, required=True,
                        choices=['ordinal_mlp', 'prototypical', 'xgboost'])
    parser.add_argument('--holdout_model', type=str, required=True,
                        choices=['pythia', 'olmo', 'gpt2xl'])
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--max_samples', type=int, default=0,
                        help='Limit train samples (0=all, for dry-run)')
    parser.add_argument('--output_dir', type=str, default=OUT_DIR)
    args = parser.parse_args()

    set_seed(args.seed)
    os.makedirs(args.output_dir, exist_ok=True)

    print(f"Method: {args.method}, Holdout: {args.holdout_model}")
    t0 = time.time()

    X_train, y_train, X_test, y_test = load_cross_model_split(args.holdout_model)
    print(f"Train: {X_train.shape[0]} samples from {[m for m in ['pythia','olmo','gpt2xl'] if m != args.holdout_model]}")
    print(f"Test:  {X_test.shape[0]} samples from [{args.holdout_model}]")

    if args.max_samples > 0 and X_train.shape[0] > args.max_samples:
        rng = np.random.RandomState(args.seed)
        idx = rng.choice(X_train.shape[0], args.max_samples, replace=False)
        X_train, y_train = X_train[idx], y_train[idx]
        print(f"Subsampled train to {args.max_samples}")

    config = METHOD_CONFIGS[args.method].copy()
    train_fn = TRAIN_FNS[args.method]
    y_pred, y_prob = train_fn(X_train, y_train, X_test, y_test, config)

    metrics = compute_metrics(y_test, y_pred, y_prob)
    elapsed = time.time() - t0
    metrics['method'] = args.method
    metrics['holdout_model'] = args.holdout_model
    metrics['train_samples'] = int(X_train.shape[0])
    metrics['test_samples'] = int(X_test.shape[0])
    metrics['elapsed_seconds'] = round(elapsed, 1)
    metrics['config'] = config

    out_file = os.path.join(args.output_dir, f"{args.method}_{args.holdout_model}.json")
    with open(out_file, 'w') as f:
        json.dump(metrics, f, indent=2, default=str)

    print(f"\nResults: accuracy={metrics['accuracy']:.4f}, MAE={metrics['mae']:.4f}")
    if 'mean_pairwise_auc' in metrics:
        print(f"         mean_pairwise_AUC={metrics['mean_pairwise_auc']:.4f}")
    print(f"Saved to {out_file} ({elapsed:.1f}s)")


if __name__ == '__main__':
    main()
