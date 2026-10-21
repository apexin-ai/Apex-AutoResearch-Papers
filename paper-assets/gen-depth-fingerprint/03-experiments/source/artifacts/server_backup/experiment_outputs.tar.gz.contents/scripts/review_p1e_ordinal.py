# P1-E: Ordinal regression vs multiclass XGBoost for depth classification
# Compares: XGBoost multiclass, CORAL ordinal (PyTorch), Frank-Hall ordinal decomposition

import json
import numpy as np
import pandas as pd
import torch
import torch.nn as nn
from pathlib import Path
from sklearn.metrics import f1_score
from xgboost import XGBClassifier
from coral_pytorch.losses import corn_loss
from coral_pytorch.dataset import corn_label_from_logits

ROOT = Path("/root/gen-depth-fingerprint")
SEED = 42
N_BOOT = 1000
MODELS = ["olmo-2-1b", "pythia-1b", "pythia-2.8b", "qwen3-0.6b", "qwen3-1.7b", "qwen3-8b"]
FEAT_7 = ["entropy_mean", "entropy_std", "entropy_min", "entropy_max",
           "tail_decay", "ttr", "hapax_ratio"]
DEVICE = "cuda:3"


def load_data():
    feat = pd.read_csv(ROOT / "data" / "features_all_models.csv")
    feat["label"] = feat["depth"].clip(upper=2)
    return feat


def downsample(df, rng):
    min_n = df["label"].value_counts().min()
    parts = [df[df["label"] == lbl].sample(n=min_n, random_state=rng, replace=False)
             for lbl in sorted(df["label"].unique())]
    return pd.concat(parts, ignore_index=True)


def bootstrap_f1(y_true, y_pred, n_boot=N_BOOT, seed=SEED):
    rng = np.random.RandomState(seed)
    n = len(y_true)
    n_classes = len(np.unique(y_true))
    scores = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        if len(np.unique(y_true[idx])) < n_classes:
            continue
        scores.append(f1_score(y_true[idx], y_pred[idx], average="macro"))
    arr = np.array(scores)
    return {"mean": round(float(np.mean(arr)), 4),
            "ci_lo": round(float(np.percentile(arr, 2.5)), 4),
            "ci_hi": round(float(np.percentile(arr, 97.5)), 4)}


# --- Method 1: Multiclass XGBoost ---

def xgb_logo(df, features, n_class, xgb_params):
    y_true_all, y_pred_all = [], []
    per_gen = {}
    rng_ds = np.random.RandomState(SEED)
    for hold in MODELS:
        tr_df = downsample(df[df["model_name"] != hold], rng_ds)
        te_df = df[df["model_name"] == hold]
        X_tr, y_tr = tr_df[features].values, tr_df["label"].values
        X_te, y_te = te_df[features].values, te_df["label"].values
        clf = XGBClassifier(**xgb_params)
        clf.fit(X_tr, y_tr)
        y_p = clf.predict(X_te)
        y_true_all.extend(y_te)
        y_pred_all.extend(y_p)
        per_gen[hold] = round(float(f1_score(y_te, y_p, average="macro")), 4)
    y_true_all = np.array(y_true_all)
    y_pred_all = np.array(y_pred_all)
    macro_f1 = round(float(f1_score(y_true_all, y_pred_all, average="macro")), 4)
    ci = bootstrap_f1(y_true_all, y_pred_all)
    return {"f1": macro_f1, "ci": ci, "per_gen": per_gen}, y_true_all, y_pred_all


# --- Method 2: CORAL/CORN ordinal regression ---

class OrdinalNet(nn.Module):
    def __init__(self, n_features, n_classes, hidden=64):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(n_features, hidden),
            nn.ReLU(),
            nn.BatchNorm1d(hidden),
            nn.Dropout(0.2),
            nn.Linear(hidden, hidden),
            nn.ReLU(),
            nn.BatchNorm1d(hidden),
            nn.Dropout(0.2),
            nn.Linear(hidden, n_classes - 1),
        )

    def forward(self, x):
        return self.net(x)


def train_coral_model(X_tr, y_tr, X_te, n_classes, device, epochs=150, lr=1e-3):
    torch.manual_seed(SEED)
    n_feat = X_tr.shape[1]
    model = OrdinalNet(n_feat, n_classes).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=epochs)

    X_tr_t = torch.tensor(X_tr, dtype=torch.float32).to(device)
    y_tr_t = torch.tensor(y_tr, dtype=torch.long).to(device)
    X_te_t = torch.tensor(X_te, dtype=torch.float32).to(device)

    dataset = torch.utils.data.TensorDataset(X_tr_t, y_tr_t)
    loader = torch.utils.data.DataLoader(dataset, batch_size=256, shuffle=True)

    model.train()
    for _ in range(epochs):
        for xb, yb in loader:
            logits = model(xb)
            loss = corn_loss(logits, yb, num_classes=n_classes)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        scheduler.step()

    model.eval()
    with torch.no_grad():
        logits_te = model(X_te_t)
        preds = corn_label_from_logits(logits_te).cpu().numpy()
    return preds


def coral_logo(df, features, n_class, device):
    y_true_all, y_pred_all = [], []
    per_gen = {}
    rng_ds = np.random.RandomState(SEED)

    # Standardize features globally for neural net
    mu = df[features].mean()
    std = df[features].std().replace(0, 1)

    for hold in MODELS:
        tr_df = downsample(df[df["model_name"] != hold], rng_ds)
        te_df = df[df["model_name"] == hold]
        X_tr = ((tr_df[features] - mu) / std).values
        y_tr = tr_df["label"].values
        X_te = ((te_df[features] - mu) / std).values
        y_te = te_df["label"].values
        y_p = train_coral_model(X_tr, y_tr, X_te, n_class, device)
        y_true_all.extend(y_te)
        y_pred_all.extend(y_p)
        per_gen[hold] = round(float(f1_score(y_te, y_p, average="macro")), 4)
    y_true_all = np.array(y_true_all)
    y_pred_all = np.array(y_pred_all)
    macro_f1 = round(float(f1_score(y_true_all, y_pred_all, average="macro")), 4)
    ci = bootstrap_f1(y_true_all, y_pred_all)
    return {"f1": macro_f1, "ci": ci, "per_gen": per_gen}, y_true_all, y_pred_all


# --- Method 3: Frank-Hall ordinal decomposition ---

def frank_hall_logo(df, features, xgb_params_bin):
    """Frank & Hall (2001): K-1 binary classifiers for K ordinal classes."""
    y_true_all, y_pred_all = [], []
    per_gen = {}
    rng_ds = np.random.RandomState(SEED)
    for hold in MODELS:
        tr_df = downsample(df[df["model_name"] != hold], rng_ds)
        te_df = df[df["model_name"] == hold]
        X_tr, y_tr = tr_df[features].values, tr_df["label"].values
        X_te, y_te = te_df[features].values, te_df["label"].values

        # Binary classifier 1: P(class > 0) i.e. gen-0 vs gen-1+
        y_bin1 = (y_tr > 0).astype(int)
        clf1 = XGBClassifier(**xgb_params_bin)
        clf1.fit(X_tr, y_bin1)
        p1 = clf1.predict_proba(X_te)[:, 1]  # P(class > 0)

        # Binary classifier 2: P(class > 1) i.e. gen-01 vs gen-2+
        y_bin2 = (y_tr > 1).astype(int)
        clf2 = XGBClassifier(**xgb_params_bin)
        clf2.fit(X_tr, y_bin2)
        p2 = clf2.predict_proba(X_te)[:, 1]  # P(class > 1)

        # Combine: P(class=0) = 1 - P(>0), P(class=1) = P(>0) - P(>1), P(class=2) = P(>1)
        prob_0 = 1 - p1
        prob_1 = np.clip(p1 - p2, 0, 1)
        prob_2 = p2
        probs = np.column_stack([prob_0, prob_1, prob_2])
        # Renormalize
        probs = probs / probs.sum(axis=1, keepdims=True)
        y_p = probs.argmax(axis=1)

        y_true_all.extend(y_te)
        y_pred_all.extend(y_p)
        per_gen[hold] = round(float(f1_score(y_te, y_p, average="macro")), 4)
    y_true_all = np.array(y_true_all)
    y_pred_all = np.array(y_pred_all)
    macro_f1 = round(float(f1_score(y_true_all, y_pred_all, average="macro")), 4)
    ci = bootstrap_f1(y_true_all, y_pred_all)
    return {"f1": macro_f1, "ci": ci, "per_gen": per_gen}, y_true_all, y_pred_all


# --- Ordinal consistency check ---

def ordinal_consistency(y_true, y_pred):
    """Check if ordinal structure is preserved: for samples with true ordering,
    does the model predict in the correct ordinal direction?"""
    # For each pair of samples with different true labels, check if predicted order matches
    n = len(y_true)
    rng = np.random.RandomState(SEED)
    n_pairs = min(50000, n * (n - 1) // 2)
    concordant = 0
    discordant = 0
    tied = 0
    for _ in range(n_pairs):
        i, j = rng.randint(0, n, size=2)
        if y_true[i] == y_true[j]:
            continue
        true_order = np.sign(y_true[i] - y_true[j])
        pred_order = np.sign(y_pred[i] - y_pred[j])
        if pred_order == 0:
            tied += 1
        elif pred_order == true_order:
            concordant += 1
        else:
            discordant += 1
    total = concordant + discordant + tied
    if total == 0:
        return 0.0
    return round(float(concordant / total), 4)


def main():
    print("=" * 70)
    print("P1-E: Ordinal Regression vs Multiclass XGBoost")
    print("=" * 70)

    df = load_data()
    print(f"Data: {len(df)} samples, {df['model_name'].nunique()} generators, 3-class")

    xgb_3class = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                       objective="multi:softmax", num_class=3,
                       eval_metric="mlogloss", verbosity=0, random_state=SEED)
    xgb_binary = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                       objective="binary:logistic",
                       eval_metric="logloss", verbosity=0, random_state=SEED)

    results = {"3class_logo": {}, "binary_logo": {}, "ordinal_consistency": {}}

    # ========== 3-CLASS EXPERIMENTS ==========
    print("\n--- 3-class LOGO ---")

    print("  [1/3] XGBoost multiclass...")
    res_xgb, yt_xgb, yp_xgb = xgb_logo(df, FEAT_7, 3, xgb_3class)
    print(f"        F1={res_xgb['f1']}  CI=[{res_xgb['ci']['ci_lo']}, {res_xgb['ci']['ci_hi']}]")
    results["3class_logo"]["xgboost_multiclass"] = res_xgb

    print("  [2/3] CORAL ordinal (PyTorch)...")
    res_coral, yt_coral, yp_coral = coral_logo(df, FEAT_7, 3, DEVICE)
    print(f"        F1={res_coral['f1']}  CI=[{res_coral['ci']['ci_lo']}, {res_coral['ci']['ci_hi']}]")
    results["3class_logo"]["coral_ordinal"] = res_coral

    print("  [3/3] Frank-Hall ordinal decomposition...")
    res_fh, yt_fh, yp_fh = frank_hall_logo(df, FEAT_7, xgb_binary)
    print(f"        F1={res_fh['f1']}  CI=[{res_fh['ci']['ci_lo']}, {res_fh['ci']['ci_hi']}]")
    results["3class_logo"]["frank_hall_ordinal"] = res_fh

    # Ordinal consistency
    print("\n  Ordinal consistency (concordance rate):")
    for name, yt, yp in [("xgboost", yt_xgb, yp_xgb), ("coral", yt_coral, yp_coral),
                          ("frank_hall", yt_fh, yp_fh)]:
        oc = ordinal_consistency(yt, yp)
        results["ordinal_consistency"][name] = oc
        print(f"    {name}: {oc}")

    # ========== BINARY EXPERIMENTS (gen-1 vs gen-2+, exclude gen-0) ==========
    print("\n--- Binary LOGO (gen-1 vs gen-2+, exclude gen-0) ---")
    df_bin = df[df["label"] > 0].copy()
    df_bin["label"] = df_bin["label"] - 1  # remap: 1->0, 2->1

    xgb_bin_cls = dict(n_estimators=200, max_depth=6, learning_rate=0.1,
                        objective="binary:logistic",
                        eval_metric="logloss", verbosity=0, random_state=SEED)

    print("  [1/2] XGBoost binary...")
    res_xgb_bin, _, _ = xgb_logo(df_bin, FEAT_7, 2, xgb_bin_cls)
    print(f"        F1={res_xgb_bin['f1']}")
    results["binary_logo"]["xgboost_binary"] = res_xgb_bin

    print("  [2/2] CORAL binary...")
    res_coral_bin, _, _ = coral_logo(df_bin, FEAT_7, 2, DEVICE)
    print(f"        F1={res_coral_bin['f1']}")
    results["binary_logo"]["coral_binary"] = res_coral_bin

    # ========== CONCLUSION ==========
    xgb_f1 = res_xgb["f1"]
    coral_f1 = res_coral["f1"]
    fh_f1 = res_fh["f1"]
    diff_coral = abs(xgb_f1 - coral_f1)
    diff_fh = abs(xgb_f1 - fh_f1)

    if diff_coral < 0.02 and diff_fh < 0.02:
        conclusion = (f"Ordinal methods (CORAL F1={coral_f1}, Frank-Hall F1={fh_f1}) perform "
                      f"comparably to multiclass XGBoost (F1={xgb_f1}). With only 3 ordinal "
                      f"levels, the ordinal structure provides minimal additional benefit.")
    elif coral_f1 > xgb_f1 or fh_f1 > xgb_f1:
        best = "CORAL" if coral_f1 > fh_f1 else "Frank-Hall"
        conclusion = f"Ordinal method ({best}) outperforms multiclass XGBoost, suggesting ordinal structure helps."
    else:
        conclusion = (f"Multiclass XGBoost (F1={xgb_f1}) outperforms ordinal methods "
                      f"(CORAL F1={coral_f1}, Frank-Hall F1={fh_f1}).")
    results["conclusion"] = conclusion

    print(f"\n{'='*70}")
    print(f"CONCLUSION: {conclusion}")
    print(f"{'='*70}")

    # Save
    out_dir = ROOT / "results"
    out_dir.mkdir(exist_ok=True)
    out_path = out_dir / "review_p1e_ordinal.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out_path}")


if __name__ == "__main__":
    main()
