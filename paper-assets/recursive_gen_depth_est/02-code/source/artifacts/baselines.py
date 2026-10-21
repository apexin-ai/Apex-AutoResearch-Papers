"""
Baseline battery for recursive generation depth estimation.

Baselines (feature-based, 19-dim input):
  1. PPLRegressionBaseline  -- OLS regression on mean_ppl (single) or all 19 features (multi)
  2. CEClassificationBaseline -- MLP with cross-entropy loss (DCOL ablation, no contrastive loss)
  3. CORALBaseline -- Ordinal regression with K-1 binary classifiers (Cao et al., 2020)
  4. DivEyeBaseline -- Surprisal diversity features + XGBoost (Basani & Chen, TMLR 2026)
  5. RandomForestBaseline -- sklearn RF on 19-dim features
  6. LogisticRegressionBaseline -- sklearn LR on 19-dim features

Baselines (text-based, raw text input):
  7. ZeroShotLLMBaseline -- Prompt an LLM (Claude/OpenAI) to classify depth directly

Usage:
  python src/baselines.py --method ppl_reg --features_path data/features_all.jsonl
  python src/baselines.py --method ce_mlp  --features_path data/features_all.jsonl --epochs 50
  python src/baselines.py --method coral   --features_path data/features_all.jsonl --epochs 50
  python src/baselines.py --method diveye  --features_path data/features_all.jsonl
  python src/baselines.py --method rf      --features_path data/features_all.jsonl
  python src/baselines.py --method lr      --features_path data/features_all.jsonl
  python src/baselines.py --method zeroshot --data_dirs data/ --provider claude --max_eval_samples 200
  python src/baselines.py --method all     --features_path data/features_all.jsonl --epochs 50
"""

import argparse
import json
import os
import re
import sys
import time
import numpy as np
from collections import Counter

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, confusion_matrix, classification_report, roc_auc_score,
)

# -- Feature schema (must match extract_features.py / dcol_dataset.py) --

FEATURE_NAMES = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]
NUM_FEATURES = len(FEATURE_NAMES)
NUM_DEPTHS = 4
DEPTH_LABELS = list(range(NUM_DEPTHS))

# -- Data loading --

def load_features(path):
    """Load JSONL features file -> (X [n, 19], y [n])."""
    records = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    X = np.array([[r[k] for k in FEATURE_NAMES] for r in records], dtype=np.float64)
    y = np.array([r["depth"] for r in records], dtype=np.int64)
    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
    return X, y


def load_jsonl_texts(data_dirs, max_samples=0, seed=42):
    """Load raw text + depth labels from depth_*.jsonl files across directories."""
    import glob as glob_mod
    texts, labels = [], []
    for data_dir in data_dirs:
        for d in range(NUM_DEPTHS):
            fpath = os.path.join(data_dir, f"depth_{d}.jsonl")
            if not os.path.exists(fpath):
                matches = glob_mod.glob(os.path.join(data_dir, f"*depth_{d}*.jsonl"))
                fpath = matches[0] if matches else None
            if fpath is None or not os.path.exists(fpath):
                continue
            with open(fpath) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    rec = json.loads(line)
                    texts.append(rec["text"])
                    labels.append(rec.get("depth", d))
    labels = np.array(labels, dtype=np.int64)
    if max_samples > 0 and len(texts) > max_samples:
        rng = np.random.RandomState(seed)
        idx = sorted(rng.choice(len(texts), max_samples, replace=False))
        texts = [texts[i] for i in idx]
        labels = labels[idx]
    print(f"Loaded {len(texts)} text samples. Depth distribution: {dict(Counter(labels))}")
    return texts, labels


def prepare_splits(X, y, test_size=0.15, val_size=0.15, seed=42):
    idx = np.arange(len(y))
    train_val_idx, test_idx = train_test_split(
        idx, test_size=test_size, stratify=y, random_state=seed
    )
    rel_val = val_size / (1 - test_size)
    train_idx, val_idx = train_test_split(
        train_val_idx, test_size=rel_val,
        stratify=y[train_val_idx], random_state=seed
    )
    return (
        X[train_idx], y[train_idx],
        X[val_idx], y[val_idx],
        X[test_idx], y[test_idx],
    )

# -- Evaluation metrics --

def pairwise_auc(y_true, y_prob, d1, d2):
    mask = np.isin(y_true, [d1, d2])
    if mask.sum() < 2:
        return None
    yt = (y_true[mask] == d2).astype(int)
    if len(np.unique(yt)) < 2:
        return None
    yp = y_prob[mask, d2]
    return float(roc_auc_score(yt, yp))


def compute_all_pairwise_auc(y_true, y_prob):
    result = {}
    for i, d1 in enumerate(DEPTH_LABELS):
        for d2 in DEPTH_LABELS[i + 1:]:
            auc = pairwise_auc(y_true, y_prob, d1, d2)
            result[f"d{d1}_vs_d{d2}"] = round(auc, 4) if auc is not None else None
    return result


def bootstrap_ci(y_true, y_pred, metric_fn=accuracy_score, n_boot=1000, seed=42):
    rng = np.random.RandomState(seed)
    scores = []
    n = len(y_true)
    for _ in range(n_boot):
        idx = rng.choice(n, n, replace=True)
        scores.append(metric_fn(y_true[idx], y_pred[idx]))
    lo = float(np.percentile(scores, 2.5))
    hi = float(np.percentile(scores, 97.5))
    return lo, hi


def evaluate(name, y_true, y_pred, y_prob=None):
    """Print and return evaluation metrics."""
    acc4 = accuracy_score(y_true, y_pred)
    ci_lo, ci_hi = bootstrap_ci(y_true, y_pred)

    mask_13 = y_true >= 1
    acc3 = accuracy_score(y_true[mask_13], y_pred[mask_13]) if mask_13.sum() > 0 else 0.0

    mae = float(np.mean(np.abs(y_true - y_pred)))

    cm = confusion_matrix(y_true, y_pred, labels=DEPTH_LABELS)
    per_class_recall = cm.diagonal() / cm.sum(axis=1).clip(min=1)

    pair_aucs = {}
    if y_prob is not None:
        pair_aucs = compute_all_pairwise_auc(y_true, y_prob)

    print(f"\n{'='*60}")
    print(f"  {name}")
    print(f"{'='*60}")
    print(f"  4-class accuracy : {acc4:.4f}  (95% CI: [{ci_lo:.4f}, {ci_hi:.4f}])")
    print(f"  3-class accuracy : {acc3:.4f}  (d1-d3 only)")
    print(f"  MAE              : {mae:.4f}")
    print(f"  Per-class recall : {dict(zip([f'd{d}' for d in DEPTH_LABELS], [round(r,4) for r in per_class_recall]))}")
    if pair_aucs:
        print(f"  Pairwise AUC     : {pair_aucs}")
    print(f"\n  Confusion matrix:")
    print(f"  {'':>8s}", " ".join(f"pred-{d}" for d in DEPTH_LABELS))
    for i, d in enumerate(DEPTH_LABELS):
        print(f"  true-{d}  ", " ".join(f"{cm[i,j]:6d}" for j in range(NUM_DEPTHS)))

    cr = classification_report(
        y_true, y_pred,
        target_names=[f"depth-{d}" for d in DEPTH_LABELS],
        zero_division=0,
    )
    print(f"\n{cr}")

    return {
        "method": name,
        "acc_4class": round(acc4, 4),
        "acc_4class_ci": [round(ci_lo, 4), round(ci_hi, 4)],
        "acc_3class": round(acc3, 4),
        "mae": round(mae, 4),
        "per_class_recall": {f"d{d}": round(r, 4) for d, r in zip(DEPTH_LABELS, per_class_recall)},
        "pairwise_auc": pair_aucs,
    }


# ===================================================================
#  Baseline 1: PPL Regression
# ===================================================================

class PPLRegressionBaseline:
    """
    Linear regression -> round to nearest depth.
    Single-feature mode: depth = a * mean_ppl + b
    Multi-feature mode:  depth = X @ w + b  (19-dim OLS)
    """

    def __init__(self, mode="multi"):
        self.mode = mode
        self.scaler = StandardScaler()
        self.model = LinearRegression()

    def _select(self, X):
        if self.mode == "single":
            idx = FEATURE_NAMES.index("mean_ppl")
            return X[:, idx:idx+1]
        return X

    def fit(self, X_train, y_train, **kwargs):
        Xs = self._select(X_train)
        Xs = self.scaler.fit_transform(Xs)
        self.model.fit(Xs, y_train.astype(np.float64))

    def predict(self, X_test):
        Xs = self._select(X_test)
        Xs = self.scaler.transform(Xs)
        raw = self.model.predict(Xs)
        return np.clip(np.round(raw).astype(int), 0, NUM_DEPTHS - 1)

    def predict_proba(self, X_test):
        preds = self.predict(X_test)
        prob = np.zeros((len(preds), NUM_DEPTHS))
        for i, p in enumerate(preds):
            prob[i, p] = 1.0
        return prob


# ===================================================================
#  Baseline 2: Cross-Entropy MLP (DCOL ablation)
# ===================================================================

class _CEMLP(nn.Module):
    """19 -> 128 -> 64 -> 4  with ReLU + dropout."""

    def __init__(self, input_dim=NUM_FEATURES, hidden1=128, hidden2=64,
                 num_classes=NUM_DEPTHS, dropout=0.3):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden1),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden1, hidden2),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden2, num_classes),
        )

    def forward(self, x):
        return self.net(x)


class CEClassificationBaseline:
    """
    Standard multi-class MLP with cross-entropy loss.
    Architecture identical to DCOL's feature classifier head (19->128->64->4)
    but uses only CE loss -- no contrastive learning.
    Key ablation: if CE-MLP matches DCOL, the contrastive loss adds no value.
    """

    def __init__(self, lr=1e-3, epochs=100, batch_size=256, patience=10,
                 device=None, seed=42):
        self.lr = lr
        self.epochs = epochs
        self.batch_size = batch_size
        self.patience = patience
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.seed = seed
        self.scaler = StandardScaler()
        self.model = None

    def fit(self, X_train, y_train, X_val=None, y_val=None, **kwargs):
        torch.manual_seed(self.seed)
        np.random.seed(self.seed)

        X_s = self.scaler.fit_transform(X_train).astype(np.float32)
        Xt = torch.tensor(X_s, device=self.device)
        yt = torch.tensor(y_train, dtype=torch.long, device=self.device)
        ds = TensorDataset(Xt, yt)
        loader = DataLoader(ds, batch_size=self.batch_size, shuffle=True)

        self.model = _CEMLP().to(self.device)
        optimizer = optim.Adam(self.model.parameters(), lr=self.lr, weight_decay=1e-4)
        criterion = nn.CrossEntropyLoss()

        best_loss = float("inf")
        wait = 0
        best_state = None

        has_val = X_val is not None and y_val is not None
        if has_val:
            Xv = torch.tensor(self.scaler.transform(X_val).astype(np.float32),
                              device=self.device)
            yv = torch.tensor(y_val, dtype=torch.long, device=self.device)

        for epoch in range(self.epochs):
            self.model.train()
            epoch_loss = 0.0
            for xb, yb in loader:
                optimizer.zero_grad()
                logits = self.model(xb)
                loss = criterion(logits, yb)
                loss.backward()
                optimizer.step()
                epoch_loss += loss.item() * len(xb)
            epoch_loss /= len(ds)

            if has_val:
                self.model.eval()
                with torch.no_grad():
                    val_logits = self.model(Xv)
                    val_loss = criterion(val_logits, yv).item()
            else:
                val_loss = epoch_loss

            if val_loss < best_loss - 1e-4:
                best_loss = val_loss
                best_state = {k: v.clone() for k, v in self.model.state_dict().items()}
                wait = 0
            else:
                wait += 1
                if wait >= self.patience:
                    break

        if best_state is not None:
            self.model.load_state_dict(best_state)

    def predict(self, X_test):
        self.model.eval()
        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),
                           device=self.device)
        with torch.no_grad():
            logits = self.model(X_s)
        return logits.argmax(dim=-1).cpu().numpy()

    def predict_proba(self, X_test):
        self.model.eval()
        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),
                           device=self.device)
        with torch.no_grad():
            logits = self.model(X_s)
            probs = torch.softmax(logits, dim=-1)
        return probs.cpu().numpy()


# ===================================================================
#  Baseline 3: CORAL Ordinal Regression
# ===================================================================

class _CORALNet(nn.Module):
    """
    CORAL ordinal regression (Cao et al., 2020).
    19 -> 128 -> 64 -> shared representation, then K-1=3 sigmoid heads.
    Each head k: P(depth > k). Prediction: depth = sum_k I[P(depth > k) > 0.5].
    Loss: sum_{k=0}^{K-2} BCE(sigmoid(w^T h + b_k), I[y > k])
    """

    def __init__(self, input_dim=NUM_FEATURES, hidden1=128, hidden2=64,
                 num_classes=NUM_DEPTHS, dropout=0.3):
        super().__init__()
        self.num_classes = num_classes
        self.backbone = nn.Sequential(
            nn.Linear(input_dim, hidden1),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden1, hidden2),
            nn.ReLU(),
            nn.Dropout(dropout),
        )
        self.fc = nn.Linear(hidden2, 1, bias=False)
        self.biases = nn.Parameter(torch.zeros(num_classes - 1))

    def forward(self, x):
        h = self.backbone(x)
        logit_base = self.fc(h)
        logits = logit_base + self.biases
        return logits


class CORALBaseline:
    """
    CORAL ordinal regression for depth estimation.
    Ref: Cao, Mirjalili & Raschka (2020). "Rank consistent ordinal regression
    for neural networks with consistent confidence sets." Pattern Recognition.
    """

    def __init__(self, lr=1e-3, epochs=100, batch_size=256, patience=10,
                 device=None, seed=42):
        self.lr = lr
        self.epochs = epochs
        self.batch_size = batch_size
        self.patience = patience
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.seed = seed
        self.scaler = StandardScaler()
        self.model = None

    @staticmethod
    def _encode_ordinal(y, num_classes):
        n = len(y)
        targets = np.zeros((n, num_classes - 1), dtype=np.float32)
        for k in range(num_classes - 1):
            targets[:, k] = (y > k).astype(np.float32)
        return targets

    def fit(self, X_train, y_train, X_val=None, y_val=None, **kwargs):
        torch.manual_seed(self.seed)
        np.random.seed(self.seed)

        X_s = self.scaler.fit_transform(X_train).astype(np.float32)
        ord_targets = self._encode_ordinal(y_train, NUM_DEPTHS)

        Xt = torch.tensor(X_s, device=self.device)
        ot = torch.tensor(ord_targets, device=self.device)
        ds = TensorDataset(Xt, ot)
        loader = DataLoader(ds, batch_size=self.batch_size, shuffle=True)

        self.model = _CORALNet().to(self.device)
        optimizer = optim.Adam(self.model.parameters(), lr=self.lr, weight_decay=1e-4)
        criterion = nn.BCEWithLogitsLoss()

        best_loss = float("inf")
        wait = 0
        best_state = None

        has_val = X_val is not None and y_val is not None
        if has_val:
            Xv = torch.tensor(self.scaler.transform(X_val).astype(np.float32),
                              device=self.device)
            ov = torch.tensor(self._encode_ordinal(y_val, NUM_DEPTHS),
                              device=self.device)

        for epoch in range(self.epochs):
            self.model.train()
            epoch_loss = 0.0
            for xb, ob in loader:
                optimizer.zero_grad()
                logits = self.model(xb)
                loss = criterion(logits, ob)
                loss.backward()
                optimizer.step()
                epoch_loss += loss.item() * len(xb)
            epoch_loss /= len(ds)

            if has_val:
                self.model.eval()
                with torch.no_grad():
                    val_logits = self.model(Xv)
                    val_loss = criterion(val_logits, ov).item()
            else:
                val_loss = epoch_loss

            if val_loss < best_loss - 1e-4:
                best_loss = val_loss
                best_state = {k: v.clone() for k, v in self.model.state_dict().items()}
                wait = 0
            else:
                wait += 1
                if wait >= self.patience:
                    break

        if best_state is not None:
            self.model.load_state_dict(best_state)

    def predict(self, X_test):
        self.model.eval()
        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),
                           device=self.device)
        with torch.no_grad():
            logits = self.model(X_s)
            probs = torch.sigmoid(logits)
        preds = (probs > 0.5).sum(dim=-1).cpu().numpy().astype(int)
        return preds

    def predict_proba(self, X_test):
        self.model.eval()
        X_s = torch.tensor(self.scaler.transform(X_test).astype(np.float32),
                           device=self.device)
        with torch.no_grad():
            logits = self.model(X_s)
            cum_probs = torch.sigmoid(logits).cpu().numpy()

        n = len(X_test)
        probs = np.zeros((n, NUM_DEPTHS))
        probs[:, 0] = 1.0 - cum_probs[:, 0]
        for k in range(1, NUM_DEPTHS - 1):
            probs[:, k] = cum_probs[:, k - 1] - cum_probs[:, k]
        probs[:, NUM_DEPTHS - 1] = cum_probs[:, NUM_DEPTHS - 2]
        probs = np.clip(probs, 0, 1)
        row_sums = probs.sum(axis=1, keepdims=True)
        probs = probs / np.where(row_sums > 0, row_sums, 1.0)
        return probs


# ===================================================================
#  Baseline 4: DivEye (Surprisal Diversity + XGBoost)
# ===================================================================
#
# DivEye feature groups mapped to our 19 features:
#   Distributional: mean_ppl, var_ppl, skewness_ppl, kurtosis_ppl
#   Surprisal:      mean_surprisal, var_surprisal, entropy_of_surprisal
#   Lexical diversity: type_token_ratio, hapax_ratio, bigram_entropy, trigram_entropy
#   Repetition:     rep_2gram, rep_3gram, rep_4gram
#
# Note: DivEye's temporal features (first-order dS and second-order d2S)
# are not available in our pre-computed features.

DIVEYE_FEATURE_INDICES = [
    FEATURE_NAMES.index(f) for f in [
        "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
        "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
        "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
        "rep_2gram", "rep_3gram", "rep_4gram",
    ]
]


class DivEyeBaseline:
    """
    DivEye-style detection adapted for depth estimation.
    Ref: Basani & Chen (2026). "Diversity Boosts AI-Generated Text Detection." TMLR.
    XGBoost on surprisal-related feature subset (14 of 19 features).
    """

    def __init__(self, seed=42):
        self.seed = seed
        self.model = None

    def fit(self, X_train, y_train, **kwargs):
        try:
            from xgboost import XGBClassifier
        except ImportError:
            print("[ERROR] xgboost not installed. Run: pip install xgboost")
            sys.exit(1)

        Xd = X_train[:, DIVEYE_FEATURE_INDICES]
        self.model = XGBClassifier(
            n_estimators=200,
            max_depth=6,
            learning_rate=0.1,
            subsample=0.8,
            colsample_bytree=0.8,
            random_state=self.seed,
            use_label_encoder=False,
            eval_metric="mlogloss",
            verbosity=0,
        )
        self.model.fit(Xd, y_train)

    def predict(self, X_test):
        Xd = X_test[:, DIVEYE_FEATURE_INDICES]
        return self.model.predict(Xd)

    def predict_proba(self, X_test):
        Xd = X_test[:, DIVEYE_FEATURE_INDICES]
        probs = self.model.predict_proba(Xd)
        if probs.shape[1] < NUM_DEPTHS:
            full = np.zeros((probs.shape[0], NUM_DEPTHS))
            for i, c in enumerate(self.model.classes_):
                full[:, c] = probs[:, i]
            return full
        return probs


# ===================================================================
#  Baseline 5: Random Forest
# ===================================================================

class RandomForestBaseline:

    def __init__(self, n_estimators=100, seed=42):
        self.seed = seed
        self.n_estimators = n_estimators
        self.scaler = StandardScaler()
        self.model = None

    def fit(self, X_train, y_train, **kwargs):
        from sklearn.ensemble import RandomForestClassifier
        X_s = self.scaler.fit_transform(X_train)
        self.model = RandomForestClassifier(
            n_estimators=self.n_estimators,
            random_state=self.seed,
            n_jobs=-1,
        )
        self.model.fit(X_s, y_train)

    def predict(self, X_test):
        X_s = self.scaler.transform(X_test)
        return self.model.predict(X_s)

    def predict_proba(self, X_test):
        X_s = self.scaler.transform(X_test)
        probs = self.model.predict_proba(X_s)
        if probs.shape[1] < NUM_DEPTHS:
            full = np.zeros((probs.shape[0], NUM_DEPTHS))
            for i, c in enumerate(self.model.classes_):
                full[:, c] = probs[:, i]
            return full
        return probs


# ===================================================================
#  Baseline 6: Logistic Regression
# ===================================================================

class LogisticRegressionBaseline:

    def __init__(self, max_iter=1000, seed=42):
        self.seed = seed
        self.max_iter = max_iter
        self.scaler = StandardScaler()
        self.model = None

    def fit(self, X_train, y_train, **kwargs):
        from sklearn.linear_model import LogisticRegression as _LR
        X_s = self.scaler.fit_transform(X_train)
        self.model = _LR(
            max_iter=self.max_iter,
            random_state=self.seed,
            solver="lbfgs",
        )
        self.model.fit(X_s, y_train)

    def predict(self, X_test):
        X_s = self.scaler.transform(X_test)
        return self.model.predict(X_s)

    def predict_proba(self, X_test):
        X_s = self.scaler.transform(X_test)
        probs = self.model.predict_proba(X_s)
        if probs.shape[1] < NUM_DEPTHS:
            full = np.zeros((probs.shape[0], NUM_DEPTHS))
            for i, c in enumerate(self.model.classes_):
                full[:, c] = probs[:, i]
            return full
        return probs


# ===================================================================
#  Baseline 7: Zero-shot LLM Prompting
# ===================================================================

ZEROSHOT_SYSTEM_PROMPT = """You are an expert at detecting AI-generated text and estimating its generation depth.

"Recursive generation depth" refers to how many times a text has been through an LLM generation cycle:
- Depth 0: Original human-written text (e.g., Wikipedia, StackExchange, academic papers)
- Depth 1: Text generated by an LLM given human-written text as a prompt/seed
- Depth 2: Text generated by an LLM given depth-1 text as input
- Depth 3: Text generated by an LLM given depth-2 text as input

Key patterns by depth:
- Depth 0 (human): Rich vocabulary, domain-specific terminology, natural topic shifts, occasional typos/informal phrasing
- Depth 1 (first-gen): Fluent but slightly generic, may have formulaic transitions, maintains topic coherence
- Depth 2 (second-gen): More repetitive phrasing, narrower vocabulary, increasingly generic content, possible topic drift
- Depth 3 (third-gen): Noticeable repetition, formulaic structure, may contain subtle incoherence or circular reasoning, very generic language"""

ZEROSHOT_USER_TEMPLATE = """Analyze the following text and estimate its recursive generation depth (0, 1, 2, or 3).

TEXT:
{text}

Respond with ONLY a JSON object in this exact format:
{{"depth": <integer 0-3>, "confidence": <float 0-1>, "reasoning": "<brief one-sentence explanation>"}}"""


def _parse_llm_response(response_text):
    """Extract depth prediction from LLM response."""
    json_match = re.search(r'\{[^{}]*"depth"\s*:\s*(\d)[^{}]*\}', response_text)
    if json_match:
        try:
            obj = json.loads(json_match.group(0))
            depth = int(obj.get("depth", -1))
            confidence = float(obj.get("confidence", 0.5))
            if 0 <= depth <= 3:
                return depth, confidence
        except (json.JSONDecodeError, ValueError):
            pass
    digit_match = re.search(r'\b([0-3])\b', response_text)
    if digit_match:
        return int(digit_match.group(1)), 0.5
    return 0, 0.0


def _call_claude(text, model, max_tokens=256):
    import anthropic
    client = anthropic.Anthropic()
    message = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=ZEROSHOT_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": ZEROSHOT_USER_TEMPLATE.format(text=text)}],
    )
    return message.content[0].text


def _call_openai(text, model, max_tokens=256):
    import openai
    client = openai.OpenAI()
    response = client.chat.completions.create(
        model=model,
        max_tokens=max_tokens,
        messages=[
            {"role": "system", "content": ZEROSHOT_SYSTEM_PROMPT},
            {"role": "user", "content": ZEROSHOT_USER_TEMPLATE.format(text=text)},
        ],
    )
    return response.choices[0].message.content


class ZeroShotLLMBaseline:
    """
    Zero-shot LLM prompting for depth estimation.
    No training -- uses in-context prompting to classify text depth.
    Supports Claude (Anthropic) and OpenAI APIs.
    """

    def __init__(self, provider="claude", model=None, max_seq_len=512,
                 rate_limit_delay=0.5):
        self.provider = provider
        self.model = model
        if self.model is None:
            self.model = "claude-sonnet-4-20250514" if provider == "claude" else "gpt-4o"
        self.max_seq_len = max_seq_len
        self.rate_limit_delay = rate_limit_delay
        self._call_fn = _call_claude if provider == "claude" else _call_openai

    def _truncate(self, text):
        words = text.split()
        approx_tokens = int(self.max_seq_len * 0.75)
        if len(words) > approx_tokens:
            words = words[:approx_tokens]
        return " ".join(words)

    def fit(self, X_train, y_train, **kwargs):
        pass

    def predict_texts(self, texts):
        """Predict depth for raw text inputs."""
        y_preds, y_probs = [], []
        errors = 0
        for i, text in enumerate(texts):
            truncated = self._truncate(text)
            try:
                response = self._call_fn(truncated, self.model)
                depth, confidence = _parse_llm_response(response)
                y_preds.append(depth)
                prob = np.zeros(NUM_DEPTHS)
                prob[depth] = confidence
                remaining = (1.0 - confidence) / max(NUM_DEPTHS - 1, 1)
                for d in range(NUM_DEPTHS):
                    if d != depth:
                        prob[d] = remaining
                y_probs.append(prob)
            except Exception as e:
                print(f"  [{i}] API error: {e}")
                y_preds.append(0)
                y_probs.append(np.ones(NUM_DEPTHS) / NUM_DEPTHS)
                errors += 1

            if (i + 1) % 20 == 0:
                print(f"  Progress: {i+1}/{len(texts)}")
            if self.rate_limit_delay > 0:
                time.sleep(self.rate_limit_delay)

        if errors > 0:
            print(f"  {errors}/{len(texts)} API errors.")
        return np.array(y_preds), np.array(y_probs)

    def predict(self, X_test):
        raise NotImplementedError("ZeroShotLLMBaseline requires raw text. Use predict_texts().")

    def predict_proba(self, X_test):
        raise NotImplementedError("ZeroShotLLMBaseline requires raw text. Use predict_texts().")


# ===================================================================
#  Unified Runner
# ===================================================================

FEATURE_BASED_METHODS = ["ppl_reg_single", "ppl_reg", "ce_mlp", "coral", "diveye", "rf", "lr"]
TEXT_BASED_METHODS = ["zeroshot"]

BASELINE_REGISTRY = {
    "ppl_reg_single": "PPL Regression (single: mean_ppl)",
    "ppl_reg":        "PPL Regression (multi: 19-dim OLS)",
    "ce_mlp":         "CE-MLP (DCOL ablation)",
    "coral":          "CORAL Ordinal Regression",
    "diveye":         "DivEye (XGBoost)",
    "rf":             "Random Forest",
    "lr":             "Logistic Regression",
    "zeroshot":       "Zero-shot LLM",
}

ALL_METHODS = FEATURE_BASED_METHODS + TEXT_BASED_METHODS


def _make_baseline(method, args):
    if method == "ppl_reg_single":
        return PPLRegressionBaseline(mode="single")
    elif method == "ppl_reg":
        return PPLRegressionBaseline(mode="multi")
    elif method == "ce_mlp":
        return CEClassificationBaseline(
            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,
            patience=args.patience, seed=args.seed,
        )
    elif method == "coral":
        return CORALBaseline(
            lr=args.lr, epochs=args.epochs, batch_size=args.batch_size,
            patience=args.patience, seed=args.seed,
        )
    elif method == "diveye":
        return DivEyeBaseline(seed=args.seed)
    elif method == "rf":
        return RandomForestBaseline(n_estimators=100, seed=args.seed)
    elif method == "lr":
        return LogisticRegressionBaseline(max_iter=1000, seed=args.seed)
    elif method == "zeroshot":
        return ZeroShotLLMBaseline(
            provider=args.provider,
            model=args.llm_model,
            max_seq_len=args.max_seq_len,
            rate_limit_delay=args.rate_limit_delay,
        )
    return None


def run_feature_baseline(method, X_train, y_train, X_val, y_val, X_test, y_test, args):
    bl = _make_baseline(method, args)
    if bl is None:
        print(f"Unknown method: {method}")
        return None
    bl.fit(X_train, y_train, X_val=X_val, y_val=y_val)
    y_pred = bl.predict(X_test)
    y_prob = bl.predict_proba(X_test)
    return evaluate(BASELINE_REGISTRY[method], y_test, y_pred, y_prob)


def run_zeroshot_baseline(texts, labels, args):
    bl = _make_baseline("zeroshot", args)
    _, eval_idx = train_test_split(
        np.arange(len(labels)), test_size=args.eval_split,
        stratify=labels, random_state=args.seed,
    )
    eval_texts = [texts[i] for i in eval_idx]
    eval_labels = labels[eval_idx]

    if len(eval_texts) > args.max_eval_samples:
        rng = np.random.RandomState(args.seed)
        sample_idx = sorted(rng.choice(len(eval_texts), args.max_eval_samples, replace=False))
        eval_texts = [eval_texts[i] for i in sample_idx]
        eval_labels = eval_labels[sample_idx]

    print(f"Zero-shot: evaluating {len(eval_texts)} samples with {args.provider}/{bl.model}")
    print(f"  Label distribution: {dict(Counter(eval_labels))}")

    y_pred, y_prob = bl.predict_texts(eval_texts)
    return evaluate(BASELINE_REGISTRY["zeroshot"], eval_labels, y_pred, y_prob)


def parse_args():
    p = argparse.ArgumentParser(description="Baseline battery for depth estimation.")
    p.add_argument("--method", default="all",
                   choices=ALL_METHODS + ["all", "all_features"])
    p.add_argument("--features_path", "--data_path", default="data/features_all.jsonl",
                   dest="features_path")
    p.add_argument("--data_dirs", nargs="+", default=["data/"],
                   help="Directories containing depth_*.jsonl (for zero-shot)")
    p.add_argument("--output_dir", default="results/baselines/")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--test_size", type=float, default=0.15)
    p.add_argument("--val_size", type=float, default=0.15)
    p.add_argument("--eval_split", type=float, default=0.15)
    p.add_argument("--epochs", type=int, default=100)
    p.add_argument("--batch_size", type=int, default=256)
    p.add_argument("--lr", type=float, default=1e-3)
    p.add_argument("--patience", type=int, default=10)
    p.add_argument("--max_seq_len", type=int, default=512)
    # Zero-shot LLM args
    p.add_argument("--provider", choices=["claude", "openai"], default="claude")
    p.add_argument("--llm_model", default=None,
                   help="LLM model name (default: claude-sonnet-4-20250514 / gpt-4o)")
    p.add_argument("--max_eval_samples", type=int, default=200,
                   help="Max samples for zero-shot eval (API cost control)")
    p.add_argument("--rate_limit_delay", type=float, default=0.5)
    return p.parse_args()


def main():
    args = parse_args()

    if args.method == "all":
        methods = FEATURE_BASED_METHODS
        print("Running all feature-based baselines (use --method zeroshot for LLM baseline)")
    elif args.method == "all_features":
        methods = FEATURE_BASED_METHODS
    else:
        methods = [args.method]

    all_results = {}

    feature_methods = [m for m in methods if m in FEATURE_BASED_METHODS]
    text_methods = [m for m in methods if m in TEXT_BASED_METHODS]

    if feature_methods:
        print(f"Loading features from {args.features_path} ...")
        X, y = load_features(args.features_path)
        print(f"  {X.shape[0]} samples, {X.shape[1]} features")
        print(f"  Depth distribution: {dict(Counter(y))}")

        X_train, y_train, X_val, y_val, X_test, y_test = prepare_splits(
            X, y, test_size=args.test_size, val_size=args.val_size, seed=args.seed
        )
        print(f"  Train: {len(y_train)}, Val: {len(y_val)}, Test: {len(y_test)}")

        for m in feature_methods:
            result = run_feature_baseline(
                m, X_train, y_train, X_val, y_val, X_test, y_test, args
            )
            if result is not None:
                all_results[m] = result

    if text_methods:
        if "zeroshot" in text_methods:
            texts, labels = load_jsonl_texts(
                args.data_dirs, max_samples=0, seed=args.seed
            )
            result = run_zeroshot_baseline(texts, labels, args)
            if result is not None:
                all_results["zeroshot"] = result

    if len(all_results) > 1:
        print(f"\n{'='*60}")
        print(f"  SUMMARY")
        print(f"{'='*60}")
        print(f"  {'Method':<35s} {'4-cls':>6s} {'3-cls':>6s} {'MAE':>6s}")
        print(f"  {'-'*35} {'-'*6} {'-'*6} {'-'*6}")
        for m, r in all_results.items():
            print(f"  {r['method']:<35s} {r['acc_4class']:6.4f} {r['acc_3class']:6.4f} {r['mae']:6.4f}")

    os.makedirs(args.output_dir, exist_ok=True)
    out_path = os.path.join(args.output_dir, "baseline_results.json")
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2, default=str)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
