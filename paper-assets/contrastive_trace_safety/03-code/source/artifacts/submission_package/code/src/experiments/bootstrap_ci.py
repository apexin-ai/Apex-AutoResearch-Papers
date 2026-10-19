"""Bootstrap confidence intervals and paired significance tests (exp-006).

Input: Pre-extracted hidden states + trained probe predictions on test set
Output: 95% CIs for all methods, paired bootstrap p-values
"""

import json
import sys
from pathlib import Path
from typing import List, Dict, Optional, Tuple

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from sklearn.linear_model import LogisticRegression, SGDClassifier

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from src.config import (
    LAYERS, HIDDEN_DIM, HIDDEN_STATES_DIR, SEED, ARTIFACTS_DIR
)
from src.data_loader import prepare_dataset, split_data


LAYER_14_IDX = 2  # LAYERS=[12,13,...,24], layer 14 is index 2
MULTI_LAYER_INDICES = [0, 2, 4, 6, 8, 10, 12]  # layers [12,14,16,18,20,22,24]
WINDOW_SIZE = 15
THRESHOLD = 0.5
CONSECUTIVE_K = 5
N_BOOTSTRAP = 1000
OUTPUT_DIR = ARTIFACTS_DIR / "exp_006_bootstrap"


# ============================================================
# GRU Model
# ============================================================

class GRUProbe(nn.Module):
    def __init__(self, input_dim=HIDDEN_DIM, hidden_dim=256, dropout=0.3):
        super().__init__()
        self.gru = nn.GRU(input_dim, hidden_dim, num_layers=1, batch_first=True, dropout=0)
        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(hidden_dim, 1)

    def forward(self, x):
        # x: [batch, T, input_dim]
        out, _ = self.gru(x)  # [batch, T, hidden_dim]
        out = self.dropout(out)
        logits = self.fc(out).squeeze(-1)  # [batch, T]
        return logits


# ============================================================
# Data helpers
# ============================================================

def load_trace_hidden_states(trace_id: str, layer_idx: int) -> Optional[torch.Tensor]:
    pt_path = HIDDEN_STATES_DIR / f"{trace_id}.pt"
    if not pt_path.exists():
        return None
    data = torch.load(pt_path, map_location="cpu", weights_only=False)
    return data["hidden_states"][:, layer_idx, :]  # [T, 4096]


def load_trace_multi_layer(trace_id: str) -> Optional[torch.Tensor]:
    pt_path = HIDDEN_STATES_DIR / f"{trace_id}.pt"
    if not pt_path.exists():
        return None
    data = torch.load(pt_path, map_location="cpu", weights_only=False)
    hs = data["hidden_states"][:, MULTI_LAYER_INDICES, :]  # [T, 7, 4096]
    return hs.mean(dim=1)  # [T, 4096]


# ============================================================
# Method 1: Static LR
# ============================================================

def train_static_lr(train_traces: List[Dict]) -> LogisticRegression:
    X_list, y_list = [], []
    for t in train_traces:
        hs = load_trace_hidden_states(t["trace_id"], LAYER_14_IDX)
        if hs is None:
            continue
        n = min(hs.shape[0], len(t["step_labels"]))
        X_list.append(hs[:n].numpy())
        y_list.append(np.array(t["step_labels"][:n]))
    X = np.concatenate(X_list)
    y = np.concatenate(y_list)
    clf = LogisticRegression(max_iter=1000, random_state=SEED, C=1.0, class_weight="balanced")
    clf.fit(X, y)
    print(f"  Static LR train acc: {clf.score(X, y):.4f} ({len(X)} samples)")
    return clf


def predict_static_lr(clf: LogisticRegression, traces: List[Dict]) -> List[Dict]:
    results = []
    for t in traces:
        hs = load_trace_hidden_states(t["trace_id"], LAYER_14_IDX)
        if hs is None:
            continue
        n = min(hs.shape[0], len(t["step_labels"]))
        probs = clf.predict_proba(hs[:n].numpy())[:, 1]
        results.append({
            "trace_id": t["trace_id"],
            "probs": probs,
            "labels": np.array(t["step_labels"][:n]),
            "commitment_point": t["commitment_point"],
        })
    return results


# ============================================================
# Method 2: Temporal LR (W=15)
# ============================================================

def create_causal_windows(hs: np.ndarray, window_size: int = WINDOW_SIZE) -> np.ndarray:
    """Causal sliding window: step i uses [i-W+1, ..., i], zero-pad left."""
    T, D = hs.shape
    padded = np.zeros((window_size - 1 + T, D), dtype=hs.dtype)
    padded[window_size - 1:] = hs
    windows = np.zeros((T, window_size * D), dtype=hs.dtype)
    for i in range(T):
        windows[i] = padded[i:i + window_size].reshape(-1)
    return windows


def train_temporal_lr(train_traces: List[Dict]):
    X_list, y_list = [], []
    for t in train_traces:
        hs = load_trace_hidden_states(t["trace_id"], LAYER_14_IDX)
        if hs is None:
            continue
        n = min(hs.shape[0], len(t["step_labels"]))
        windows = create_causal_windows(hs[:n].numpy().astype(np.float32))
        X_list.append(windows)
        y_list.append(np.array(t["step_labels"][:n]))
    X = np.concatenate(X_list)
    y = np.concatenate(y_list)
    clf = SGDClassifier(loss="log_loss", alpha=1e-4, max_iter=100,
                        random_state=SEED, class_weight="balanced", tol=1e-3)
    clf.fit(X, y)
    print(f"  Temporal LR W=15 train acc: {clf.score(X, y):.4f} ({len(X)} samples)")
    return clf


def predict_temporal_lr(clf, traces: List[Dict]) -> List[Dict]:
    results = []
    for t in traces:
        hs = load_trace_hidden_states(t["trace_id"], LAYER_14_IDX)
        if hs is None:
            continue
        n = min(hs.shape[0], len(t["step_labels"]))
        windows = create_causal_windows(hs[:n].numpy().astype(np.float32))
        probs = clf.predict_proba(windows)[:, 1]
        results.append({
            "trace_id": t["trace_id"],
            "probs": probs,
            "labels": np.array(t["step_labels"][:n]),
            "commitment_point": t["commitment_point"],
        })
    return results


# ============================================================
# Method 3 & 4: GRU training
# ============================================================

def train_gru(train_traces: List[Dict], val_traces: List[Dict],
              multi_layer: bool = False) -> GRUProbe:
    device = "cuda" if torch.cuda.is_available() else "cpu"
    load_fn = load_trace_multi_layer if multi_layer else (
        lambda tid: load_trace_hidden_states(tid, LAYER_14_IDX)
    )

    def collect(traces):
        seqs, labels_list = [], []
        for t in traces:
            hs = load_fn(t["trace_id"])
            if hs is None:
                continue
            n = min(hs.shape[0], len(t["step_labels"]))
            seqs.append(hs[:n].float().to(device))
            labels_list.append(torch.tensor(t["step_labels"][:n], dtype=torch.float32).to(device))
        return seqs, labels_list

    train_seqs, train_labels = collect(train_traces)
    val_seqs, val_labels = collect(val_traces)

    model = GRUProbe(input_dim=HIDDEN_DIM, hidden_dim=256, dropout=0.3).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    criterion = nn.BCEWithLogitsLoss()

    best_val_loss = float("inf")
    patience_counter = 0
    best_state = None

    for epoch in range(20):
        model.train()
        epoch_loss = 0
        for seq, lab in zip(train_seqs, train_labels):
            logits = model(seq.unsqueeze(0))  # [1, T]
            loss = criterion(logits[0], lab)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()

        model.eval()
        val_loss = 0
        with torch.no_grad():
            for seq, lab in zip(val_seqs, val_labels):
                logits = model(seq.unsqueeze(0))
                val_loss += criterion(logits[0], lab).item()

        val_loss /= max(len(val_seqs), 1)

        if val_loss < best_val_loss:
            best_val_loss = val_loss
            patience_counter = 0
            best_state = {k: v.clone() for k, v in model.state_dict().items()}
        else:
            patience_counter += 1
            if patience_counter >= 5:
                break

    if best_state:
        model.load_state_dict(best_state)
    model = model.cpu()
    name = "GRU multi-7L" if multi_layer else "GRU single L14"
    print(f"  {name} trained {epoch+1} epochs, best val_loss={best_val_loss:.4f}")
    return model


def predict_gru(model: GRUProbe, traces: List[Dict],
                multi_layer: bool = False) -> List[Dict]:
    load_fn = load_trace_multi_layer if multi_layer else (
        lambda tid: load_trace_hidden_states(tid, LAYER_14_IDX)
    )
    model.eval()
    results = []
    for t in traces:
        hs = load_fn(t["trace_id"])
        if hs is None:
            continue
        n = min(hs.shape[0], len(t["step_labels"]))
        with torch.no_grad():
            logits = model(hs[:n].float().unsqueeze(0))  # [1, T]
            probs = torch.sigmoid(logits[0]).numpy()
        results.append({
            "trace_id": t["trace_id"],
            "probs": probs,
            "labels": np.array(t["step_labels"][:n]),
            "commitment_point": t["commitment_point"],
        })
    return results


# ============================================================
# Evaluation per trace
# ============================================================

def first_crossing_point(probs: np.ndarray, threshold: float = THRESHOLD,
                         consecutive_k: int = CONSECUTIVE_K) -> Optional[int]:
    n = len(probs)
    if n < consecutive_k:
        return None
    for i in range(n - consecutive_k + 1):
        if all(probs[i:i + consecutive_k] > threshold):
            return i
    return None


def compute_trace_metrics(pred: Dict) -> Dict:
    probs = pred["probs"]
    labels = pred["labels"]
    cp = pred["commitment_point"]

    preds_binary = (probs > 0.5).astype(int)
    step_acc = float((preds_binary == labels).mean())

    fcp = first_crossing_point(probs)
    crossing_detected = 1 if fcp is not None else 0
    lead_time = (cp - fcp) if fcp is not None else None

    return {
        "step_accuracy": step_acc,
        "crossing_detected": crossing_detected,
        "lead_time": lead_time,
    }


# ============================================================
# Bootstrap
# ============================================================

def bootstrap_ci(per_trace_metrics: List[Dict], n_bootstrap: int = N_BOOTSTRAP,
                 seed: int = SEED) -> Dict:
    rng = np.random.default_rng(seed)
    n = len(per_trace_metrics)

    accs = np.array([m["step_accuracy"] for m in per_trace_metrics])
    crossings = np.array([m["crossing_detected"] for m in per_trace_metrics])
    lead_times = np.array([m["lead_time"] if m["lead_time"] is not None else np.nan
                           for m in per_trace_metrics])

    boot_accs = np.zeros(n_bootstrap)
    boot_crossings = np.zeros(n_bootstrap)
    boot_leads = np.zeros(n_bootstrap)

    for b in range(n_bootstrap):
        idx = rng.choice(n, size=n, replace=True)
        boot_accs[b] = accs[idx].mean()
        boot_crossings[b] = crossings[idx].mean()
        sampled_leads = lead_times[idx]
        valid = sampled_leads[~np.isnan(sampled_leads)]
        boot_leads[b] = valid.mean() if len(valid) > 0 else np.nan

    def ci(arr):
        arr_valid = arr[~np.isnan(arr)]
        if len(arr_valid) == 0:
            return {"mean": None, "ci_lower": None, "ci_upper": None}
        return {
            "mean": float(np.mean(arr_valid)),
            "ci_lower": float(np.percentile(arr_valid, 2.5)),
            "ci_upper": float(np.percentile(arr_valid, 97.5)),
        }

    return {
        "step_accuracy": ci(boot_accs),
        "crossing_rate": ci(boot_crossings),
        "lead_time_mean": ci(boot_leads),
    }


def paired_bootstrap_test(metrics_a: List[Dict], metrics_b: List[Dict],
                          metric_key: str, n_bootstrap: int = N_BOOTSTRAP,
                          seed: int = SEED) -> Dict:
    """Test H0: metric_A <= metric_B. p_value = P(delta <= 0)."""
    rng = np.random.default_rng(seed + 7)
    n = len(metrics_a)
    assert len(metrics_b) == n

    if metric_key == "crossing_detected":
        vals_a = np.array([m["crossing_detected"] for m in metrics_a], dtype=float)
        vals_b = np.array([m["crossing_detected"] for m in metrics_b], dtype=float)
    elif metric_key == "lead_time":
        vals_a = np.array([m["lead_time"] if m["lead_time"] is not None else np.nan
                           for m in metrics_a])
        vals_b = np.array([m["lead_time"] if m["lead_time"] is not None else np.nan
                           for m in metrics_b])
    else:
        vals_a = np.array([m[metric_key] for m in metrics_a], dtype=float)
        vals_b = np.array([m[metric_key] for m in metrics_b], dtype=float)

    deltas = np.zeros(n_bootstrap)
    for b in range(n_bootstrap):
        idx = rng.choice(n, size=n, replace=True)
        a_sample = vals_a[idx]
        b_sample = vals_b[idx]
        if metric_key == "lead_time":
            valid_a = a_sample[~np.isnan(a_sample)]
            valid_b = b_sample[~np.isnan(b_sample)]
            mean_a = valid_a.mean() if len(valid_a) > 0 else 0
            mean_b = valid_b.mean() if len(valid_b) > 0 else 0
        else:
            mean_a = a_sample.mean()
            mean_b = b_sample.mean()
        deltas[b] = mean_a - mean_b

    p_value = float((deltas <= 0).mean())
    return {
        "delta_mean": float(np.mean(deltas)),
        "ci_lower": float(np.percentile(deltas, 2.5)),
        "ci_upper": float(np.percentile(deltas, 97.5)),
        "p_value": p_value,
    }


# ============================================================
# Main
# ============================================================

def main(n_bootstrap: int = N_BOOTSTRAP):
    print("=" * 60)
    print("EXP-006: Bootstrap CIs + Paired Significance Tests")
    print("=" * 60)

    # Load and split data
    print("\n[1/5] Loading data...")
    dataset = prepare_dataset()
    traces = dataset["jailbreak_with_commitment"]
    train, val, test = split_data(traces)
    print(f"  Traces: train={len(train)}, val={len(val)}, test={len(test)}")

    # Train all methods
    print("\n[2/5] Training methods...")

    print("  --- Static LR (Layer 14) ---")
    static_lr = train_static_lr(train)

    print("  --- Temporal LR W=15 (Layer 14) ---")
    temporal_lr = train_temporal_lr(train)

    print("  --- GRU single Layer 14 ---")
    gru_single = train_gru(train, val, multi_layer=False)

    print("  --- GRU multi-7L ---")
    gru_multi = train_gru(train, val, multi_layer=True)

    # Predict on test set
    print("\n[3/5] Predicting on test set...")
    preds = {
        "static_lr": predict_static_lr(static_lr, test),
        "temporal_lr_w15": predict_temporal_lr(temporal_lr, test),
        "gru_single_l14": predict_gru(gru_single, test, multi_layer=False),
        "gru_multi_7l": predict_gru(gru_multi, test, multi_layer=True),
    }

    # Compute per-trace metrics
    print("\n[4/5] Computing per-trace metrics...")
    per_trace = {}
    for method_name, pred_list in preds.items():
        per_trace[method_name] = [compute_trace_metrics(p) for p in pred_list]
        n_crossing = sum(m["crossing_detected"] for m in per_trace[method_name])
        leads = [m["lead_time"] for m in per_trace[method_name] if m["lead_time"] is not None]
        mean_lead = np.mean(leads) if leads else float("nan")
        print(f"  {method_name}: {len(pred_list)} traces, "
              f"crossing={n_crossing}/{len(pred_list)} ({n_crossing/len(pred_list)*100:.1f}%), "
              f"mean_lead={mean_lead:.1f}")

    # Bootstrap
    print(f"\n[5/5] Bootstrap (B={n_bootstrap})...")
    results = {
        "n_bootstrap": n_bootstrap,
        "n_test_traces": len(test),
        "seed": SEED,
        "threshold": THRESHOLD,
        "consecutive_k": CONSECUTIVE_K,
        "methods": {},
        "paired_tests": {},
    }

    for method_name, metrics in per_trace.items():
        results["methods"][method_name] = bootstrap_ci(metrics, n_bootstrap)

    # Paired tests
    pairs = [
        ("temporal_lr_w15", "static_lr", "temporal_lr_vs_static_lr"),
        ("gru_multi_7l", "static_lr", "gru_multi_vs_static_lr"),
        ("gru_multi_7l", "temporal_lr_w15", "gru_multi_vs_temporal_lr"),
    ]

    for method_a, method_b, pair_name in pairs:
        results["paired_tests"][pair_name] = {
            "crossing_rate": paired_bootstrap_test(
                per_trace[method_a], per_trace[method_b], "crossing_detected", n_bootstrap),
            "lead_time": paired_bootstrap_test(
                per_trace[method_a], per_trace[method_b], "lead_time", n_bootstrap),
        }

    # Save
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / "bootstrap_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")

    # Print summary table
    print("\n" + "=" * 70)
    print(f"{'Method':<20} {'Accuracy':<22} {'Crossing Rate':<22} {'Lead Time':<22}")
    print("-" * 70)
    for method_name, cis in results["methods"].items():
        acc = cis["step_accuracy"]
        cr = cis["crossing_rate"]
        lt = cis["lead_time_mean"]
        acc_str = f"{acc['mean']:.3f} [{acc['ci_lower']:.3f}, {acc['ci_upper']:.3f}]" if acc["mean"] else "N/A"
        cr_str = f"{cr['mean']:.3f} [{cr['ci_lower']:.3f}, {cr['ci_upper']:.3f}]" if cr["mean"] else "N/A"
        lt_str = f"{lt['mean']:+.1f} [{lt['ci_lower']:+.1f}, {lt['ci_upper']:+.1f}]" if lt["mean"] else "N/A"
        print(f"{method_name:<20} {acc_str:<22} {cr_str:<22} {lt_str:<22}")

    print("\n" + "=" * 70)
    print("Paired Bootstrap Tests (A vs B, p-value = P(delta_A-B <= 0))")
    print("-" * 70)
    for pair_name, tests in results["paired_tests"].items():
        cr_test = tests["crossing_rate"]
        lt_test = tests["lead_time"]
        print(f"\n  {pair_name}:")
        print(f"    crossing_rate: delta={cr_test['delta_mean']:+.3f} "
              f"[{cr_test['ci_lower']:+.3f}, {cr_test['ci_upper']:+.3f}], p={cr_test['p_value']:.3f}")
        if lt_test["delta_mean"] is not None:
            print(f"    lead_time:     delta={lt_test['delta_mean']:+.1f} "
                  f"[{lt_test['ci_lower']:+.1f}, {lt_test['ci_upper']:+.1f}], p={lt_test['p_value']:.3f}")

    print("\n" + "=" * 70)
    return results


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_bootstrap", type=int, default=N_BOOTSTRAP)
    parser.add_argument("--dry_run", action="store_true", help="Quick run with B=10")
    args = parser.parse_args()

    if args.dry_run:
        main(n_bootstrap=10)
    else:
        main(n_bootstrap=args.n_bootstrap)
