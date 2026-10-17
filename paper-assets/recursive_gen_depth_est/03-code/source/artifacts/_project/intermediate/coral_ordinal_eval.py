"""CORAL Ordinal Regression vs RF — 9-cell systematic evaluation."""
import os
os.environ["OMP_NUM_THREADS"] = "4"
os.environ["MKL_NUM_THREADS"] = "4"
os.environ["OPENBLAS_NUM_THREADS"] = "4"

import json
import time
import numpy as np
import torch
import torch.nn as nn
from pathlib import Path
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, balanced_accuracy_score, cohen_kappa_score

torch.set_num_threads(4)
DEVICE = torch.device("cpu")

FEATURE_NAMES = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio",
    "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]

CELLS = {
    "pythia_nucleus":  "/root/autodl-tmp/recursive_gen_depth_est/data/features_all.jsonl",
    "pythia_temp09":   "/root/autodl-tmp/recursive_gen_depth_est/data/pythia_temp09/features.jsonl",
    "pythia_topk50":   "/root/autodl-tmp/recursive_gen_depth_est/results/pythia_topk50/features.jsonl",
    "olmo_nucleus":    "/root/autodl-tmp/recursive_gen_depth_est/data/olmo/features.jsonl",
    "olmo_temp09":     "/root/autodl-tmp/recursive_gen_depth_est/results/olmo_temp09/features.jsonl",
    "olmo_topk50":     "/root/autodl-tmp/recursive_gen_depth_est/results/olmo_topk50/features.jsonl",
    "gpt2xl_nucleus":  "/root/autodl-tmp/recursive_gen_depth_est/data/gpt2xl/features.jsonl",
    "gpt2xl_temp09":   "/root/autodl-tmp/recursive_gen_depth_est/results/gpt2xl_temp09/features.jsonl",
    "gpt2xl_topk50":   "/root/autodl-tmp/recursive_gen_depth_est/results/gpt2xl_topk50/features.jsonl",
}

NUM_CLASSES = 4
NUM_FOLDS = 5
SEED = 42
EPOCHS = 100
PATIENCE = 10
BATCH_SIZE = 256
LR = 1e-3


def load_features(path):
    X, y = [], []
    with open(path) as f:
        for line in f:
            rec = json.loads(line)
            X.append([rec[fn] for fn in FEATURE_NAMES])
            y.append(rec["depth"])
    X = np.array(X, dtype=np.float64)
    y = np.array(y, dtype=np.int64)
    inf_mask = ~np.isfinite(X)
    if inf_mask.any():
        n_inf = inf_mask.sum()
        print(f"  WARNING: {n_inf} inf/nan values found, clipping", flush=True)
        for col in range(X.shape[1]):
            col_data = X[:, col]
            finite_vals = col_data[np.isfinite(col_data)]
            if len(finite_vals) > 0:
                col_max = np.max(np.abs(finite_vals))
                col_data[~np.isfinite(col_data)] = col_max
            else:
                col_data[~np.isfinite(col_data)] = 0.0
    X = X.astype(np.float32)
    X = np.nan_to_num(X, nan=0.0, posinf=np.finfo(np.float32).max * 0.9, neginf=-np.finfo(np.float32).max * 0.9)
    return X, y


class CoralDNN(nn.Module):
    def __init__(self, n_features, n_classes):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(n_features, 64),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(64, 32),
            nn.ReLU(),
            nn.Dropout(0.3),
        )
        self.coral_weight = nn.Linear(32, 1, bias=False)
        self.coral_bias = nn.Parameter(torch.zeros(n_classes - 1))

    def forward(self, x):
        h = self.fc(x)
        logits = self.coral_weight(h) + self.coral_bias
        return logits


def coral_loss(logits, labels, n_classes):
    levels = torch.zeros(labels.size(0), n_classes - 1, device=logits.device)
    for k in range(n_classes - 1):
        levels[:, k] = (labels > k).float()
    return nn.functional.binary_cross_entropy_with_logits(logits, levels)


def coral_predict(logits):
    probs = torch.sigmoid(logits)
    return (probs > 0.5).sum(dim=1).long()


def train_coral(X_train, y_train, X_val, y_val):
    n_features = X_train.shape[1]
    model = CoralDNN(n_features, NUM_CLASSES).to(DEVICE)
    optimizer = torch.optim.Adam(model.parameters(), lr=LR)

    X_tr = torch.tensor(X_train, device=DEVICE)
    y_tr = torch.tensor(y_train, device=DEVICE)
    X_v = torch.tensor(X_val, device=DEVICE)
    y_v = torch.tensor(y_val, device=DEVICE)

    best_val_loss = float("inf")
    best_state = None
    patience_counter = 0

    for epoch in range(EPOCHS):
        model.train()
        perm = torch.randperm(len(X_tr))
        for i in range(0, len(X_tr), BATCH_SIZE):
            idx = perm[i:i + BATCH_SIZE]
            logits = model(X_tr[idx])
            loss = coral_loss(logits, y_tr[idx], NUM_CLASSES)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        model.eval()
        with torch.no_grad():
            val_logits = model(X_v)
            val_loss = coral_loss(val_logits, y_v, NUM_CLASSES).item()

        if val_loss < best_val_loss:
            best_val_loss = val_loss
            best_state = {k: v.clone() for k, v in model.state_dict().items()}
            patience_counter = 0
        else:
            patience_counter += 1
            if patience_counter >= PATIENCE:
                break

    model.load_state_dict(best_state)
    return model


def ordinal_consistency_sampled(y_true, y_pred, max_n=2000):
    n = len(y_true)
    if n > max_n:
        rng = np.random.RandomState(42)
        idx = rng.choice(n, max_n, replace=False)
        y_true = y_true[idx]
        y_pred = y_pred[idx]

    yt = y_true.astype(np.int16)[:, None]
    yp = y_pred.astype(np.int16)[:, None]
    true_lt = yt < yt.T
    true_gt = yt > yt.T
    pred_le = yp <= yp.T
    pred_ge = yp >= yp.T

    concordant = np.sum(true_lt & pred_le) + np.sum(true_gt & pred_ge)
    total = np.sum(true_lt) + np.sum(true_gt)
    return concordant / total if total > 0 else 1.0


def evaluate_predictions(y_true, y_pred):
    acc_4class = accuracy_score(y_true, y_pred)
    mask = y_true > 0
    if mask.sum() > 0:
        y_t_sub = y_true[mask]
        y_p_sub = y_pred[mask]
        correct_per_class = {}
        count_per_class = {}
        for yt, yp in zip(y_t_sub, y_p_sub):
            count_per_class[yt] = count_per_class.get(yt, 0) + 1
            if yt == yp:
                correct_per_class[yt] = correct_per_class.get(yt, 0) + 1
        recalls = []
        for c in sorted(count_per_class.keys()):
            recalls.append(correct_per_class.get(c, 0) / count_per_class[c])
        d1d3_bal_acc = float(np.mean(recalls))
    else:
        d1d3_bal_acc = 0.0

    mae = float(np.mean(np.abs(y_true - y_pred)))
    qwk = float(cohen_kappa_score(y_true, y_pred, weights="quadratic"))
    oc = ordinal_consistency_sampled(y_true, y_pred)
    return {
        "4class_acc": round(acc_4class, 4),
        "d1d3_bal_acc": round(d1d3_bal_acc, 4),
        "mae": round(mae, 4),
        "qwk": round(qwk, 4),
        "ordinal_consistency": round(float(oc), 4),
    }


def run_cell(cell_name, features_path):
    t0 = time.time()
    X, y = load_features(features_path)
    print(f"[{cell_name}] loaded {len(X)} samples", flush=True)

    skf = StratifiedKFold(n_splits=NUM_FOLDS, shuffle=True, random_state=SEED)
    coral_fold_metrics, rf_fold_metrics = [], []

    for fold_i, (train_idx, test_idx) in enumerate(skf.split(X, y)):
        ft0 = time.time()
        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]

        scaler = StandardScaler().fit(X_train)
        X_train_s = scaler.transform(X_train).astype(np.float32)
        X_test_s = scaler.transform(X_test).astype(np.float32)

        torch.manual_seed(SEED + fold_i)
        np.random.seed(SEED + fold_i)

        val_size = int(0.15 * len(X_train_s))
        perm = np.random.permutation(len(X_train_s))
        val_idx = perm[:val_size]
        tr_idx = perm[val_size:]

        model = train_coral(
            X_train_s[tr_idx], y_train[tr_idx],
            X_train_s[val_idx], y_train[val_idx],
        )
        model.eval()
        with torch.no_grad():
            test_logits = model(torch.tensor(X_test_s, device=DEVICE))
            coral_pred = coral_predict(test_logits).numpy()

        rf = RandomForestClassifier(n_estimators=200, random_state=SEED + fold_i, n_jobs=4)
        rf.fit(X_train, y_train)
        rf_pred = rf.predict(X_test)

        coral_fold_metrics.append(evaluate_predictions(y_test, coral_pred))
        rf_fold_metrics.append(evaluate_predictions(y_test, rf_pred))

        ft1 = time.time()
        print(f"  fold{fold_i}: CORAL={coral_fold_metrics[-1]['4class_acc']:.4f} RF={rf_fold_metrics[-1]['4class_acc']:.4f} ({ft1-ft0:.1f}s)", flush=True)

    def avg_m(fl):
        return {k: round(float(np.mean([f[k] for f in fl])), 4) for k in fl[0]}

    coral_avg = avg_m(coral_fold_metrics)
    rf_avg = avg_m(rf_fold_metrics)
    coral_std = {k + "_std": round(float(np.std([f[k] for f in coral_fold_metrics])), 4) for k in coral_avg}
    rf_std = {k + "_std": round(float(np.std([f[k] for f in rf_fold_metrics])), 4) for k in rf_avg}
    delta = {k: round(coral_avg[k] - rf_avg[k], 4) for k in coral_avg}

    elapsed = time.time() - t0
    print(f"  => CORAL acc={coral_avg['4class_acc']:.4f} RF acc={rf_avg['4class_acc']:.4f} delta={delta['4class_acc']:+.4f} [{elapsed:.0f}s]", flush=True)

    return {"coral": {**coral_avg, **coral_std}, "rf": {**rf_avg, **rf_std}, "delta": delta}


def main():
    print(f"Starting CORAL 9-cell evaluation (threads=4, seed={SEED})", flush=True)
    results = {"per_cell": {}, "average": {}}
    cell_order = [
        "pythia_nucleus", "pythia_temp09", "pythia_topk50",
        "olmo_nucleus", "olmo_temp09", "olmo_topk50",
        "gpt2xl_nucleus", "gpt2xl_temp09", "gpt2xl_topk50",
    ]

    for cell in cell_order:
        path = CELLS[cell]
        if not Path(path).exists():
            print(f"SKIP {cell}: {path} not found", flush=True)
            continue
        results["per_cell"][cell] = run_cell(cell, path)

    if results["per_cell"]:
        metric_keys = ["4class_acc", "d1d3_bal_acc", "mae", "qwk", "ordinal_consistency"]
        avg_coral, avg_rf, avg_delta = {}, {}, {}
        for k in metric_keys:
            avg_coral[k] = round(float(np.mean([v["coral"][k] for v in results["per_cell"].values()])), 4)
            avg_rf[k] = round(float(np.mean([v["rf"][k] for v in results["per_cell"].values()])), 4)
            avg_delta[k] = round(avg_coral[k] - avg_rf[k], 4)
        results["average"] = {"coral": avg_coral, "rf": avg_rf, "delta": avg_delta}

    output_path = "/root/autodl-tmp/recursive_gen_depth_est/results/coral_9cell_results.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {output_path}", flush=True)

    print("\n===JSON_RESULTS_START===")
    print(json.dumps(results, indent=2))
    print("===JSON_RESULTS_END===")


if __name__ == "__main__":
    main()
