"""exp-015: FPR analysis — determine if text baseline's high lead time comes from false positives."""

import sys
import json
import warnings
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from sklearn.linear_model import LogisticRegression

sys.path.insert(0, 'DATA_DIR')
from src.data_loader import prepare_dataset, split_data
from src.config import TRAIN_RATIO, VAL_RATIO, SEED, DETECTION_WINDOW, LAYERS, HIDDEN_DIM
from src.eval.evaluate import first_crossing_point, detection_lead_time, step_accuracy

warnings.filterwarnings("ignore")

HS_DIR = Path("DATA_DIR/artifacts/hidden_states")
OUT_DIR = Path("DATA_DIR/artifacts/exp_015_fpr")
OUT_DIR.mkdir(parents=True, exist_ok=True)

WINDOW = 15
LAYER_IDX = 2  # Layer 14 = LAYERS[2]
GRU_HIDDEN = 256
GRU_EPOCHS = 20
GRU_PATIENCE = 5
GRU_LR = 1e-3
MULTI_LAYER_INDICES = [0, 2, 4, 6, 8, 10, 12]  # layers 12,14,16,18,20,22,24


# ============================================================
# Feature builders
# ============================================================

def build_text_static_features(trace, st_model):
    embs = trace["text_embeddings"]  # [T, 384]
    return embs

def build_text_temporal_features(trace, st_model, window=WINDOW):
    embs = trace["text_embeddings"]  # [T, 384]
    T = len(embs)
    features = []
    for i in range(T):
        start = max(0, i - window + 1)
        window_embs = embs[start:i+1]
        if len(window_embs) < window:
            pad = np.zeros((window - len(window_embs), embs.shape[1]))
            window_embs = np.vstack([pad, window_embs])
        features.append(window_embs.flatten())
    return np.array(features)

def load_hs(trace, layer_idx=LAYER_IDX):
    pt_path = HS_DIR / f"{trace['trace_id']}.pt"
    if not pt_path.exists():
        return None
    pt = torch.load(pt_path, map_location="cpu", weights_only=False)
    return pt["hidden_states"][:, layer_idx, :].numpy()

def load_hs_multi7l(trace):
    pt_path = HS_DIR / f"{trace['trace_id']}.pt"
    if not pt_path.exists():
        return None
    pt = torch.load(pt_path, map_location="cpu", weights_only=False)
    hs = pt["hidden_states"][:, MULTI_LAYER_INDICES, :].mean(dim=1).numpy()
    return hs

def build_hs_static_features(trace):
    return load_hs(trace)

def build_hs_temporal_features(trace, window=WINDOW):
    hs = load_hs(trace)
    if hs is None:
        return None
    T = len(hs)
    features = []
    for i in range(T):
        start = max(0, i - window + 1)
        w = hs[start:i+1]
        if len(w) < window:
            pad = np.zeros((window - len(w), hs.shape[1]))
            w = np.vstack([pad, w])
        features.append(w.flatten())
    return np.array(features)


# ============================================================
# FPR metrics
# ============================================================

def safe_trace_fpr(predict_fn, safe_traces, build_fn, **kwargs):
    total_steps = 0
    false_positives = 0
    n_evaluated = 0
    for t in safe_traces:
        features = build_fn(t, **kwargs)
        if features is None:
            continue
        probs = predict_fn(features)
        preds = (probs > 0.5).astype(int)
        total_steps += len(preds)
        false_positives += preds.sum()
        n_evaluated += 1
    fpr = false_positives / total_steps if total_steps > 0 else 0
    return fpr, n_evaluated

def pre_commitment_fpr(predict_fn, test_traces, build_fn, **kwargs):
    total_pre = 0
    fp_pre = 0
    for t in test_traces:
        cp = t["commitment_point"]
        if cp is None or cp == 0:
            continue
        features = build_fn(t, **kwargs)
        if features is None:
            continue
        probs = predict_fn(features)
        preds = (probs > 0.5).astype(int)
        pre_preds = preds[:cp]
        total_pre += len(pre_preds)
        fp_pre += pre_preds.sum()
    return fp_pre / total_pre if total_pre > 0 else 0

def compute_precision(predict_fn, test_traces, build_fn, **kwargs):
    tp = 0
    fp = 0
    for t in test_traces:
        cp = t["commitment_point"]
        if cp is None:
            continue
        features = build_fn(t, **kwargs)
        if features is None:
            continue
        probs = predict_fn(features)
        preds = (probs > 0.5).astype(int)
        labels = np.array(t["step_labels"])
        tp += int(((preds == 1) & (labels == 1)).sum())
        fp += int(((preds == 1) & (labels == 0)).sum())
    return tp / (tp + fp) if (tp + fp) > 0 else 0

def compute_coverage_and_lead(predict_fn, test_traces, build_fn, **kwargs):
    leads = []
    n_crossing = 0
    n_valid = 0
    accs = []
    for t in test_traces:
        cp = t["commitment_point"]
        if cp is None:
            continue
        features = build_fn(t, **kwargs)
        if features is None:
            continue
        n_valid += 1
        probs = predict_fn(features)
        preds = (probs > 0.5).astype(int)
        labels = np.array(t["step_labels"])
        accs.append(step_accuracy(preds, labels))
        fcp = first_crossing_point(probs, threshold=0.5, consecutive_k=DETECTION_WINDOW)
        if fcp is not None:
            n_crossing += 1
            lead = detection_lead_time(fcp, cp)
            leads.append(lead)
    coverage = n_crossing / n_valid if n_valid > 0 else 0
    mean_lead = float(np.mean(leads)) if leads else None
    mean_acc = float(np.mean(accs)) if accs else None
    return coverage, mean_lead, mean_acc


# ============================================================
# GRU Probe
# ============================================================

class GRUProbe(nn.Module):
    def __init__(self, input_dim=HIDDEN_DIM, hidden_dim=GRU_HIDDEN, dropout=0.3):
        super().__init__()
        self.gru = nn.GRU(input_dim, hidden_dim, num_layers=1, batch_first=True, dropout=0)
        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(hidden_dim, 1)

    def forward(self, x):
        out, _ = self.gru(x)
        out = self.dropout(out)
        logits = self.fc(out).squeeze(-1)
        return logits


def train_gru(train_traces, val_traces):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = GRUProbe().to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=GRU_LR)

    # Compute pos_weight from training data
    n_pos = sum(sum(t["step_labels"]) for t in train_traces if t["step_labels"])
    n_neg = sum(len(t["step_labels"]) - sum(t["step_labels"]) for t in train_traces if t["step_labels"])
    pos_weight = torch.tensor([n_neg / max(n_pos, 1)], device=device)
    criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)

    # Load all training hidden states
    train_data = []
    for t in train_traces:
        hs = load_hs_multi7l(t)
        if hs is None:
            continue
        labels = np.array(t["step_labels"], dtype=np.float32)
        train_data.append((hs, labels))

    val_data = []
    for t in val_traces:
        hs = load_hs_multi7l(t)
        if hs is None:
            continue
        labels = np.array(t["step_labels"], dtype=np.float32)
        val_data.append((hs, labels))

    best_val_loss = float('inf')
    patience_counter = 0
    best_state = None

    for epoch in range(GRU_EPOCHS):
        model.train()
        epoch_loss = 0
        np.random.shuffle(train_data)
        for hs, labels in train_data:
            x = torch.tensor(hs, dtype=torch.float32).unsqueeze(0).to(device)
            y = torch.tensor(labels, dtype=torch.float32).unsqueeze(0).to(device)
            optimizer.zero_grad()
            logits = model(x)
            loss = criterion(logits, y)
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()

        # Validation
        model.eval()
        val_loss = 0
        with torch.no_grad():
            for hs, labels in val_data:
                x = torch.tensor(hs, dtype=torch.float32).unsqueeze(0).to(device)
                y = torch.tensor(labels, dtype=torch.float32).unsqueeze(0).to(device)
                logits = model(x)
                val_loss += criterion(logits, y).item()

        val_loss /= max(len(val_data), 1)
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            patience_counter = 0
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
        else:
            patience_counter += 1
            if patience_counter >= GRU_PATIENCE:
                break

    model.load_state_dict(best_state)
    model.eval()
    return model


def gru_predict(model, trace):
    device = next(model.parameters()).device
    hs = load_hs_multi7l(trace)
    if hs is None:
        return None
    with torch.no_grad():
        x = torch.tensor(hs, dtype=torch.float32).unsqueeze(0).to(device)
        logits = model(x)
        probs = torch.sigmoid(logits).squeeze(0).cpu().numpy()
    return probs


# ============================================================
# Main
# ============================================================

def main():
    print("Loading data...")
    data = prepare_dataset("r1-8b")
    jb_traces = data["jailbreak_with_commitment"]
    safe_traces = data["safe"]
    train_jb, val_jb, test_jb = split_data(jb_traces, TRAIN_RATIO, VAL_RATIO, SEED)
    print(f"Train: {len(train_jb)}, Val: {len(val_jb)}, Test: {len(test_jb)}, Safe: {len(safe_traces)}")

    # Embed all text
    print("Loading sentence-transformers...")
    from sentence_transformers import SentenceTransformer
    st_model = SentenceTransformer('all-MiniLM-L6-v2')

    print("Embedding text...")
    all_traces = train_jb + val_jb + test_jb + safe_traces
    for t in all_traces:
        t["text_embeddings"] = st_model.encode(t["sentences"], batch_size=64, show_progress_bar=False)

    # Check safe traces HS availability
    safe_with_hs = [t for t in safe_traces if (HS_DIR / f"{t['trace_id']}.pt").exists()]
    print(f"Safe traces with hidden states: {len(safe_with_hs)}/{len(safe_traces)}")

    results = {}

    # ============================================================
    # Method 1: text_static — LR on single-step embedding [384]
    # ============================================================
    print("\n--- Method 1: text_static ---")
    X_train, y_train = [], []
    for t in train_jb:
        embs = t["text_embeddings"]
        labels = t["step_labels"]
        X_train.append(embs)
        y_train.extend(labels)
    X_train = np.vstack(X_train)
    y_train = np.array(y_train)

    lr_text_static = LogisticRegression(C=1.0, class_weight='balanced', max_iter=1000, solver='lbfgs')
    lr_text_static.fit(X_train, y_train)

    def predict_text_static(features):
        return lr_text_static.predict_proba(features)[:, 1]

    fpr1, n_eval = safe_trace_fpr(predict_text_static, safe_traces, lambda t, **kw: build_text_static_features(t, st_model))
    fpr2 = pre_commitment_fpr(predict_text_static, test_jb, lambda t, **kw: build_text_static_features(t, st_model))
    prec = compute_precision(predict_text_static, test_jb, lambda t, **kw: build_text_static_features(t, st_model))
    cov, lead, acc = compute_coverage_and_lead(predict_text_static, test_jb, lambda t, **kw: build_text_static_features(t, st_model))
    results["text_static"] = {"safe_fpr": fpr1, "pre_commitment_fpr": fpr2, "precision": prec,
                              "coverage": cov, "lead_time_mean": lead, "step_accuracy": acc, "n_safe_evaluated": n_eval}
    print(f"  Safe FPR: {fpr1:.4f} ({n_eval} traces), Pre-CP FPR: {fpr2:.4f}, Precision: {prec:.4f}")

    # ============================================================
    # Method 2: text_temporal W=15 — LR on windowed embedding [5760]
    # ============================================================
    print("\n--- Method 2: text_temporal W=15 ---")
    X_train_t, y_train_t = [], []
    for t in train_jb:
        feats = build_text_temporal_features(t, st_model, window=WINDOW)
        X_train_t.append(feats)
        y_train_t.extend(t["step_labels"])
    X_train_t = np.vstack(X_train_t)
    y_train_t = np.array(y_train_t)

    lr_text_temporal = LogisticRegression(C=1.0, class_weight='balanced', max_iter=1000, solver='lbfgs')
    lr_text_temporal.fit(X_train_t, y_train_t)

    def predict_text_temporal(features):
        return lr_text_temporal.predict_proba(features)[:, 1]

    fpr1, n_eval = safe_trace_fpr(predict_text_temporal, safe_traces, lambda t, **kw: build_text_temporal_features(t, st_model, window=WINDOW))
    fpr2 = pre_commitment_fpr(predict_text_temporal, test_jb, lambda t, **kw: build_text_temporal_features(t, st_model, window=WINDOW))
    prec = compute_precision(predict_text_temporal, test_jb, lambda t, **kw: build_text_temporal_features(t, st_model, window=WINDOW))
    cov, lead, acc = compute_coverage_and_lead(predict_text_temporal, test_jb, lambda t, **kw: build_text_temporal_features(t, st_model, window=WINDOW))
    results["text_temporal_w15"] = {"safe_fpr": fpr1, "pre_commitment_fpr": fpr2, "precision": prec,
                                    "coverage": cov, "lead_time_mean": lead, "step_accuracy": acc, "n_safe_evaluated": n_eval}
    print(f"  Safe FPR: {fpr1:.4f} ({n_eval} traces), Pre-CP FPR: {fpr2:.4f}, Precision: {prec:.4f}")

    # ============================================================
    # Method 3: HS_static LR L14
    # ============================================================
    print("\n--- Method 3: HS_static LR L14 ---")
    X_train_hs, y_train_hs = [], []
    for t in train_jb:
        hs = load_hs(t)
        if hs is None:
            continue
        X_train_hs.append(hs)
        y_train_hs.extend(t["step_labels"])
    X_train_hs = np.vstack(X_train_hs)
    y_train_hs = np.array(y_train_hs)

    lr_hs_static = LogisticRegression(C=1.0, class_weight='balanced', max_iter=1000, solver='lbfgs')
    lr_hs_static.fit(X_train_hs, y_train_hs)

    def predict_hs_static(features):
        return lr_hs_static.predict_proba(features)[:, 1]

    fpr1, n_eval = safe_trace_fpr(predict_hs_static, safe_traces, lambda t, **kw: build_hs_static_features(t))
    fpr2 = pre_commitment_fpr(predict_hs_static, test_jb, lambda t, **kw: build_hs_static_features(t))
    prec = compute_precision(predict_hs_static, test_jb, lambda t, **kw: build_hs_static_features(t))
    cov, lead, acc = compute_coverage_and_lead(predict_hs_static, test_jb, lambda t, **kw: build_hs_static_features(t))
    results["hs_static_lr_l14"] = {"safe_fpr": fpr1, "pre_commitment_fpr": fpr2, "precision": prec,
                                   "coverage": cov, "lead_time_mean": lead, "step_accuracy": acc, "n_safe_evaluated": n_eval}
    print(f"  Safe FPR: {fpr1:.4f} ({n_eval} traces), Pre-CP FPR: {fpr2:.4f}, Precision: {prec:.4f}")

    # ============================================================
    # Method 4: HS_temporal LR W=15 L14
    # ============================================================
    print("\n--- Method 4: HS_temporal LR W=15 L14 ---")
    X_train_hst, y_train_hst = [], []
    for t in train_jb:
        feats = build_hs_temporal_features(t, window=WINDOW)
        if feats is None:
            continue
        X_train_hst.append(feats)
        y_train_hst.extend(t["step_labels"])
    X_train_hst = np.vstack(X_train_hst)
    y_train_hst = np.array(y_train_hst)

    lr_hs_temporal = LogisticRegression(C=1.0, class_weight='balanced', max_iter=1000, solver='lbfgs')
    lr_hs_temporal.fit(X_train_hst, y_train_hst)

    def predict_hs_temporal(features):
        return lr_hs_temporal.predict_proba(features)[:, 1]

    fpr1, n_eval = safe_trace_fpr(predict_hs_temporal, safe_traces, lambda t, **kw: build_hs_temporal_features(t, window=WINDOW))
    fpr2 = pre_commitment_fpr(predict_hs_temporal, test_jb, lambda t, **kw: build_hs_temporal_features(t, window=WINDOW))
    prec = compute_precision(predict_hs_temporal, test_jb, lambda t, **kw: build_hs_temporal_features(t, window=WINDOW))
    cov, lead, acc = compute_coverage_and_lead(predict_hs_temporal, test_jb, lambda t, **kw: build_hs_temporal_features(t, window=WINDOW))
    results["hs_temporal_lr_w15_l14"] = {"safe_fpr": fpr1, "pre_commitment_fpr": fpr2, "precision": prec,
                                         "coverage": cov, "lead_time_mean": lead, "step_accuracy": acc, "n_safe_evaluated": n_eval}
    print(f"  Safe FPR: {fpr1:.4f} ({n_eval} traces), Pre-CP FPR: {fpr2:.4f}, Precision: {prec:.4f}")

    # ============================================================
    # Method 5: GRU multi-7L h=256
    # ============================================================
    print("\n--- Method 5: GRU multi-7L h=256 ---")
    print("  Training GRU...")
    gru_model = train_gru(train_jb, val_jb)

    def predict_gru(features_trace):
        # features_trace is actually the trace dict for GRU
        return features_trace

    # GRU needs special handling since it takes raw traces
    def gru_safe_fpr(safe_traces):
        total_steps = 0
        false_positives = 0
        n_evaluated = 0
        for t in safe_traces:
            probs = gru_predict(gru_model, t)
            if probs is None:
                continue
            preds = (probs > 0.5).astype(int)
            total_steps += len(preds)
            false_positives += preds.sum()
            n_evaluated += 1
        return (false_positives / total_steps if total_steps > 0 else 0), n_evaluated

    def gru_pre_commitment_fpr(test_traces):
        total_pre = 0
        fp_pre = 0
        for t in test_traces:
            cp = t["commitment_point"]
            if cp is None or cp == 0:
                continue
            probs = gru_predict(gru_model, t)
            if probs is None:
                continue
            preds = (probs > 0.5).astype(int)
            pre_preds = preds[:cp]
            total_pre += len(pre_preds)
            fp_pre += pre_preds.sum()
        return fp_pre / total_pre if total_pre > 0 else 0

    def gru_precision(test_traces):
        tp = 0
        fp = 0
        for t in test_traces:
            cp = t["commitment_point"]
            if cp is None:
                continue
            probs = gru_predict(gru_model, t)
            if probs is None:
                continue
            preds = (probs > 0.5).astype(int)
            labels = np.array(t["step_labels"])
            tp += int(((preds == 1) & (labels == 1)).sum())
            fp += int(((preds == 1) & (labels == 0)).sum())
        return tp / (tp + fp) if (tp + fp) > 0 else 0

    def gru_coverage_lead(test_traces):
        leads = []
        n_crossing = 0
        n_valid = 0
        accs = []
        for t in test_traces:
            cp = t["commitment_point"]
            if cp is None:
                continue
            probs = gru_predict(gru_model, t)
            if probs is None:
                continue
            n_valid += 1
            preds = (probs > 0.5).astype(int)
            labels = np.array(t["step_labels"])
            accs.append(step_accuracy(preds, labels))
            fcp = first_crossing_point(probs, threshold=0.5, consecutive_k=DETECTION_WINDOW)
            if fcp is not None:
                n_crossing += 1
                lead = detection_lead_time(fcp, cp)
                leads.append(lead)
        coverage = n_crossing / n_valid if n_valid > 0 else 0
        mean_lead = float(np.mean(leads)) if leads else None
        mean_acc = float(np.mean(accs)) if accs else None
        return coverage, mean_lead, mean_acc

    fpr1, n_eval = gru_safe_fpr(safe_traces)
    fpr2 = gru_pre_commitment_fpr(test_jb)
    prec = gru_precision(test_jb)
    cov, lead, acc = gru_coverage_lead(test_jb)
    results["gru_multi7l_h256"] = {"safe_fpr": fpr1, "pre_commitment_fpr": fpr2, "precision": prec,
                                   "coverage": cov, "lead_time_mean": lead, "step_accuracy": acc, "n_safe_evaluated": n_eval}
    print(f"  Safe FPR: {fpr1:.4f} ({n_eval} traces), Pre-CP FPR: {fpr2:.4f}, Precision: {prec:.4f}")

    # ============================================================
    # Summary table
    # ============================================================
    print("\n" + "="*100)
    print(f"{'Method':<22} {'Safe FPR':>10} {'Pre-CP FPR':>12} {'Precision':>10} {'Coverage':>10} {'Lead Time':>10} {'Step Acc':>10}")
    print("-"*100)
    method_names = {
        "text_static": "text_static",
        "text_temporal_w15": "text_temporal W=15",
        "hs_static_lr_l14": "HS_static LR L14",
        "hs_temporal_lr_w15_l14": "HS_temporal LR W=15",
        "gru_multi7l_h256": "GRU multi-7L h=256",
    }
    for key, name in method_names.items():
        r = results[key]
        lead_str = f"{r['lead_time_mean']:+.1f}" if r['lead_time_mean'] is not None else "N/A"
        print(f"{name:<22} {r['safe_fpr']:>10.4f} {r['pre_commitment_fpr']:>12.4f} {r['precision']:>10.4f} "
              f"{r['coverage']:>9.1%} {lead_str:>10} {r['step_accuracy']:>10.4f}")
    print("="*100)

    # Save results
    output = {
        "methods": results,
        "n_safe_traces": len(safe_traces),
        "n_test_jb_traces": len(test_jb),
        "n_safe_with_hs": len(safe_with_hs),
    }
    with open(OUT_DIR / "fpr_results.json", "w") as f:
        json.dump(output, f, indent=2, default=lambda x: float(x) if isinstance(x, (np.floating, np.integer)) else x)

    print(f"\nResults saved to {OUT_DIR / 'fpr_results.json'}")


if __name__ == "__main__":
    main()
