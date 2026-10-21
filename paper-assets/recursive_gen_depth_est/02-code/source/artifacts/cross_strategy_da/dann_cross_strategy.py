#!/usr/bin/env python3
"""DANN cross-strategy domain adaptation for recursive generation depth estimation."""

import json
import sys
import os
import math
import warnings

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, balanced_accuracy_score, mean_absolute_error,
    cohen_kappa_score,
)

warnings.filterwarnings("ignore")

FEATURE_COLS = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]

BASE = "/root/autodl-tmp/recursive_gen_depth_est"
DATA_PATHS = {
    "pythia": {
        "nucleus": f"{BASE}/data/features_all.jsonl",
        "temp": f"{BASE}/data/pythia_temp09/features.jsonl",
        "topk": f"{BASE}/results/pythia_topk50/features.jsonl",
    },
    "olmo": {
        "nucleus": f"{BASE}/data/olmo/features.jsonl",
        "temp": f"{BASE}/results/olmo_temp09/features.jsonl",
        "topk": f"{BASE}/results/olmo_topk50/features.jsonl",
    },
    "gpt2xl": {
        "nucleus": f"{BASE}/data/gpt2xl/features.jsonl",
        "temp": f"{BASE}/results/gpt2xl_temp09/features.jsonl",
        "topk": f"{BASE}/results/gpt2xl_topk50/features.jsonl",
    },
}

STRATEGIES = ["nucleus", "temp", "topk"]
STRATEGY_TO_IDX = {s: i for i, s in enumerate(STRATEGIES)}
SEED = 42


def load_features(path):
    X, y = [], []
    with open(path) as f:
        for line in f:
            row = json.loads(line)
            X.append([row[c] for c in FEATURE_COLS])
            y.append(row["depth"])
    X = np.array(X, dtype=np.float64)
    X = np.clip(X, -1e15, 1e15)
    X = np.where(np.isfinite(X), X, np.nan)
    col_medians = np.nanmedian(X, axis=0)
    for col in range(X.shape[1]):
        mask = np.isnan(X[:, col])
        if mask.any():
            X[mask, col] = col_medians[col]
    return X.astype(np.float32), np.array(y, dtype=np.int64)


def load_model_data(model_name):
    data = {}
    for strat, path in DATA_PATHS[model_name].items():
        X, y = load_features(path)
        data[strat] = (X, y)
    return data


# ===================== DANN Model =====================

class GradientReversalFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x, lambda_):
        ctx.lambda_ = lambda_
        return x.clone()

    @staticmethod
    def backward(ctx, grad_output):
        return -ctx.lambda_ * grad_output, None


class GRL(nn.Module):
    def __init__(self):
        super().__init__()
        self.lambda_ = 0.0

    def set_lambda(self, val):
        self.lambda_ = val

    def forward(self, x):
        return GradientReversalFunction.apply(x, self.lambda_)


class FeatureEncoder(nn.Module):
    def __init__(self, in_dim=19, hidden=128, out_dim=64, dropout=0.3):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, hidden), nn.ReLU(), nn.Dropout(dropout),
            nn.Linear(hidden, out_dim), nn.ReLU(), nn.Dropout(dropout),
        )

    def forward(self, x):
        return self.net(x)


class DepthClassifier(nn.Module):
    def __init__(self, in_dim=64, hidden=32, num_classes=4):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, hidden), nn.ReLU(),
            nn.Linear(hidden, num_classes),
        )

    def forward(self, x):
        return self.net(x)


class StrategyDiscriminator(nn.Module):
    def __init__(self, in_dim=64, hidden=32, num_classes=3):
        super().__init__()
        self.grl = GRL()
        self.net = nn.Sequential(
            nn.Linear(in_dim, hidden), nn.ReLU(),
            nn.Linear(hidden, num_classes),
        )

    def set_lambda(self, val):
        self.grl.set_lambda(val)

    def forward(self, x):
        return self.net(self.grl(x))


class DANN(nn.Module):
    def __init__(self):
        super().__init__()
        self.encoder = FeatureEncoder()
        self.depth_clf = DepthClassifier()
        self.strategy_disc = StrategyDiscriminator()

    def set_lambda(self, val):
        self.strategy_disc.set_lambda(val)

    def forward(self, x):
        feat = self.encoder(x)
        return self.depth_clf(feat), self.strategy_disc(feat)

    def predict_depth(self, x):
        return self.depth_clf(self.encoder(x))


# ===================== Training =====================

def ganin_lambda(epoch, max_epochs):
    p = epoch / max_epochs
    return 2.0 / (1.0 + math.exp(-10.0 * p)) - 1.0


def train_dann(source_X, source_y, source_strat_labels,
               target_X, target_strat_idx,
               max_epochs=200, patience=20, batch_size=256,
               lr=1e-3, weight_decay=1e-4, seed=SEED):
    torch.manual_seed(seed)
    np.random.seed(seed)

    n_src = len(source_X)
    perm = np.random.permutation(n_src)
    split = int(0.8 * n_src)
    train_idx, val_idx = perm[:split], perm[split:]

    train_X = torch.tensor(source_X[train_idx])
    train_y = torch.tensor(source_y[train_idx])
    train_strat = torch.tensor(source_strat_labels[train_idx])
    val_X = torch.tensor(source_X[val_idx])
    val_y = torch.tensor(source_y[val_idx])
    target_X_t = torch.tensor(target_X)
    target_strat_t = torch.full((len(target_X),), target_strat_idx, dtype=torch.long)

    model = DANN()
    optimizer = optim.Adam(model.parameters(), lr=lr, weight_decay=weight_decay)
    depth_ce = nn.CrossEntropyLoss()
    strat_ce = nn.CrossEntropyLoss()

    best_val_acc = 0.0
    best_state = None
    no_improve = 0

    for epoch in range(max_epochs):
        model.train()
        lam = ganin_lambda(epoch, max_epochs)
        model.set_lambda(lam)

        src_perm = torch.randperm(len(train_X))
        train_X_s = train_X[src_perm]
        train_y_s = train_y[src_perm]
        train_strat_s = train_strat[src_perm]

        tgt_perm = torch.randperm(len(target_X_t))
        target_X_s = target_X_t[tgt_perm]
        target_strat_s = target_strat_t[tgt_perm]

        n_batches = max(len(train_X_s), len(target_X_s)) // batch_size + 1

        for i in range(n_batches):
            si = (i * batch_size) % len(train_X_s)
            ti = (i * batch_size) % len(target_X_s)

            src_batch_X = train_X_s[si:si+batch_size]
            src_batch_y = train_y_s[si:si+batch_size]
            src_batch_strat = train_strat_s[si:si+batch_size]

            tgt_batch_X = target_X_s[ti:ti+batch_size]
            tgt_batch_strat = target_strat_s[ti:ti+batch_size]

            src_depth_logits, src_strat_logits = model(src_batch_X)
            tgt_strat_logits = model.strategy_disc(model.encoder(tgt_batch_X))

            loss_depth = depth_ce(src_depth_logits, src_batch_y)
            loss_strat = strat_ce(
                torch.cat([src_strat_logits, tgt_strat_logits]),
                torch.cat([src_batch_strat, tgt_batch_strat]),
            )

            loss = loss_depth + loss_strat
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        model.eval()
        with torch.no_grad():
            val_preds = model.predict_depth(val_X).argmax(dim=1).numpy()
            val_acc = accuracy_score(val_y.numpy(), val_preds)

        if val_acc > best_val_acc:
            best_val_acc = val_acc
            best_state = {k: v.clone() for k, v in model.state_dict().items()}
            no_improve = 0
        else:
            no_improve += 1

        if no_improve >= patience:
            break

    model.load_state_dict(best_state)
    return model


def train_naive_dnn(source_X, source_y, max_epochs=200, patience=20,
                    batch_size=256, lr=1e-3, weight_decay=1e-4, seed=SEED):
    torch.manual_seed(seed)
    np.random.seed(seed)

    n = len(source_X)
    perm = np.random.permutation(n)
    split = int(0.8 * n)
    train_idx, val_idx = perm[:split], perm[split:]

    train_X = torch.tensor(source_X[train_idx])
    train_y = torch.tensor(source_y[train_idx])
    val_X = torch.tensor(source_X[val_idx])
    val_y = torch.tensor(source_y[val_idx])

    encoder = FeatureEncoder()
    classifier = DepthClassifier()
    params = list(encoder.parameters()) + list(classifier.parameters())
    optimizer = optim.Adam(params, lr=lr, weight_decay=weight_decay)
    criterion = nn.CrossEntropyLoss()

    best_val_acc = 0.0
    best_enc = None
    best_clf = None
    no_improve = 0

    for epoch in range(max_epochs):
        encoder.train(); classifier.train()
        ep = torch.randperm(len(train_X))
        tXs, tYs = train_X[ep], train_y[ep]

        for i in range(0, len(tXs), batch_size):
            bX, bY = tXs[i:i+batch_size], tYs[i:i+batch_size]
            loss = criterion(classifier(encoder(bX)), bY)
            optimizer.zero_grad(); loss.backward(); optimizer.step()

        encoder.eval(); classifier.eval()
        with torch.no_grad():
            val_acc = accuracy_score(
                val_y.numpy(),
                classifier(encoder(val_X)).argmax(dim=1).numpy()
            )

        if val_acc > best_val_acc:
            best_val_acc = val_acc
            best_enc = {k: v.clone() for k, v in encoder.state_dict().items()}
            best_clf = {k: v.clone() for k, v in classifier.state_dict().items()}
            no_improve = 0
        else:
            no_improve += 1
        if no_improve >= patience:
            break

    encoder.load_state_dict(best_enc)
    classifier.load_state_dict(best_clf)
    return encoder, classifier


# ===================== Evaluation =====================

def compute_metrics(y_true, y_pred):
    mask = y_true >= 1
    return {
        "accuracy_4class": float(accuracy_score(y_true, y_pred)),
        "balanced_accuracy_d1d3": float(
            balanced_accuracy_score(y_true[mask], y_pred[mask])
        ) if mask.sum() > 0 else 0.0,
        "mae": float(mean_absolute_error(y_true, y_pred)),
        "cohen_kappa_weighted": float(
            cohen_kappa_score(y_true, y_pred, weights="quadratic")
        ),
    }


def fmt(m):
    return (f"acc={m['accuracy_4class']:.4f}  "
            f"bal_d1d3={m['balanced_accuracy_d1d3']:.4f}  "
            f"mae={m['mae']:.4f}  kappa={m['cohen_kappa_weighted']:.4f}")


# ===================== LOSO Evaluation =====================

def run_loso_for_model(model_name, verbose=True):
    if verbose:
        print(f"\n{'='*60}\nModel: {model_name}\n{'='*60}")

    data = load_model_data(model_name)
    results = {"model": model_name, "folds": {}, "methods": {}}
    fold_results = {"rf": [], "dnn": [], "dann": []}

    for held_out in STRATEGIES:
        source_strats = [s for s in STRATEGIES if s != held_out]
        if verbose:
            print(f"\n--- Hold out {held_out}, train on {source_strats} ---")

        src_Xs, src_ys, src_strats = [], [], []
        for s in source_strats:
            X, y = data[s]
            src_Xs.append(X)
            src_ys.append(y)
            src_strats.append(np.full(len(X), STRATEGY_TO_IDX[s], dtype=np.int64))

        source_X = np.concatenate(src_Xs)
        source_y = np.concatenate(src_ys)
        source_strat = np.concatenate(src_strats)
        target_X, target_y = data[held_out]

        scaler = StandardScaler()
        sX = scaler.fit_transform(source_X).astype(np.float32)
        tX = scaler.transform(target_X).astype(np.float32)

        fk = f"held_out_{held_out}"
        results["folds"][fk] = {}

        # RF
        rf = RandomForestClassifier(n_estimators=200, random_state=SEED, n_jobs=-1)
        rf.fit(sX, source_y)
        rf_m = compute_metrics(target_y, rf.predict(tX))
        results["folds"][fk]["rf"] = rf_m
        fold_results["rf"].append(rf_m)
        if verbose:
            print(f"  RF:   {fmt(rf_m)}")

        # Naive DNN
        enc, clf = train_naive_dnn(sX, source_y)
        enc.eval(); clf.eval()
        with torch.no_grad():
            dnn_pred = clf(enc(torch.tensor(tX))).argmax(1).numpy()
        dnn_m = compute_metrics(target_y, dnn_pred)
        results["folds"][fk]["dnn"] = dnn_m
        fold_results["dnn"].append(dnn_m)
        if verbose:
            print(f"  DNN:  {fmt(dnn_m)}")

        # DANN
        dann = train_dann(sX, source_y, source_strat, tX, STRATEGY_TO_IDX[held_out])
        dann.eval()
        with torch.no_grad():
            dann_pred = dann.predict_depth(torch.tensor(tX)).argmax(1).numpy()
        dann_m = compute_metrics(target_y, dann_pred)
        results["folds"][fk]["dann"] = dann_m
        fold_results["dann"].append(dann_m)
        if verbose:
            print(f"  DANN: {fmt(dann_m)}")

    for method in ["rf", "dnn", "dann"]:
        avg = {}
        for k in fold_results[method][0]:
            vals = [f[k] for f in fold_results[method]]
            avg[k] = float(np.mean(vals))
            avg[f"{k}_std"] = float(np.std(vals))
        results["methods"][method] = avg

    if verbose:
        print(f"\n--- {model_name} LOSO Average ---")
        for method in ["rf", "dnn", "dann"]:
            m = results["methods"][method]
            print(f"  {method.upper():5s}: acc={m['accuracy_4class']:.4f}+-"
                  f"{m['accuracy_4class_std']:.4f}  "
                  f"bal_d1d3={m['balanced_accuracy_d1d3']:.4f}  "
                  f"mae={m['mae']:.4f}  kappa={m['cohen_kappa_weighted']:.4f}")

    return results


def main():
    models_to_run = sys.argv[1:] if len(sys.argv) > 1 else ["pythia"]
    all_results = {}

    for model_name in models_to_run:
        if model_name not in DATA_PATHS:
            print(f"Unknown model: {model_name}, skipping")
            continue
        all_results[model_name] = run_loso_for_model(model_name)

    output_path = os.environ.get(
        "DANN_OUTPUT",
        "/root/autodl-tmp/recursive_gen_depth_est/results/dann_results.json"
    )
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    main()
