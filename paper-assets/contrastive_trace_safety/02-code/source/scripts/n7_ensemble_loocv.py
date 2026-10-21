#!/usr/bin/env python3
"""N7: 5-fold stratified CV validation of multi-metric ensemble layer selection.

For R1-8B (n=209), runs 5-fold stratified CV where layer selection
(precision-best, BA-best, FPR-best) happens INSIDE each fold via an
inner 80/20 split, preventing information leakage.
Compares ensemble vs single-metric layer selection under the same CV.

Output: artifacts/ensemble_cv_results.json
"""

import os, sys, json, warnings, time
from collections import Counter

os.environ["TOKENIZERS_PARALLELISM"] = "false"
warnings.filterwarnings("ignore")
sys.stdout.reconfigure(line_buffering=True)

import numpy as np
import torch
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import balanced_accuracy_score
from sklearn.model_selection import StratifiedKFold

PROJECT = Path("/root/autodl-tmp/contrastive_trace_safety")
ARTIFACTS = PROJECT / "artifacts"
OUT_FILE = ARTIFACTS / "ensemble_cv_results.json"

SEED = 42
N_FOLDS = 5

MODEL_CONFIGS = {
    "R1-8B": {
        "hs_dir": ARTIFACTS / "hidden_states_r1_8b_full",
        "layer_offset": 12,
        "n_stored_layers": 13,
        "hidden_dim": 4096,
        "window": 15,
        "sweep_step": 1,
    },
}


def load_traces(hs_dir):
    traces = []
    for pt_file in sorted(hs_dir.glob("*.pt")):
        data = torch.load(pt_file, map_location="cpu", weights_only=False)
        if data.get("step_labels") is None or data.get("commitment_point") is None:
            continue
        traces.append(data)
    return traces


def get_labels(t):
    sl = t["step_labels"]
    if isinstance(sl, torch.Tensor):
        return sl.tolist()
    return list(sl)


def get_cp(t):
    cp = t["commitment_point"]
    if isinstance(cp, torch.Tensor):
        return int(cp.item())
    return int(cp)


def moving_avg(hs, window):
    if window <= 1:
        return hs
    T, D = hs.shape
    out = np.zeros_like(hs)
    cumsum = np.zeros((T + 1, D), dtype=hs.dtype)
    for i in range(T):
        cumsum[i + 1] = cumsum[i] + hs[i]
    for i in range(T):
        start = max(0, i - window + 1)
        out[i] = (cumsum[i + 1] - cumsum[start]) / (i - start + 1)
    return out


def extract_features(trace, layer_idx, window):
    hs = trace["hidden_states"][:, layer_idx, :]
    if isinstance(hs, torch.Tensor):
        hs = hs.float().numpy()
    return moving_avg(hs.astype(np.float32), window)


def collect_data(traces, layer_idx, window):
    X_parts, y_parts = [], []
    for t in traces:
        feats = extract_features(t, layer_idx, window)
        labels = get_labels(t)
        n = min(len(feats), len(labels))
        X_parts.append(feats[:n])
        y_parts.extend(labels[:n])
    return np.vstack(X_parts), np.array(y_parts)


def train_probe(X, y):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    clf = LogisticRegression(C=1.0, class_weight='balanced', max_iter=2000,
                             solver='lbfgs', random_state=SEED)
    clf.fit(X_scaled, y)
    return clf, scaler


def predict_trace(clf, scaler, trace, layer_idx, window):
    feats = extract_features(trace, layer_idx, window)
    labels = get_labels(trace)
    n = min(len(feats), len(labels))
    X_scaled = scaler.transform(feats[:n])
    if len(clf.classes_) == 1:
        probs = np.full(n, 0.5)
    else:
        probs = clf.predict_proba(X_scaled)[:, 1]
    return probs, np.array(labels[:n]), get_cp(trace)


def compute_aggregate_metrics(all_probs, all_labels, all_cps):
    all_p, all_l = [], []
    pre_fp, pre_total = 0, 0
    for probs, labels, cp in zip(all_probs, all_labels, all_cps):
        preds = (probs > 0.5).astype(int)
        all_p.extend(preds)
        all_l.extend(labels)
        if cp and 0 < cp < len(preds):
            pre_fp += int(preds[:cp].sum())
            pre_total += cp

    all_p = np.array(all_p)
    all_l = np.array(all_l)
    ba = balanced_accuracy_score(all_l, all_p)
    tp = int(((all_p == 1) & (all_l == 1)).sum())
    fp = int(((all_p == 1) & (all_l == 0)).sum())
    prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    fpr = pre_fp / pre_total if pre_total > 0 else 0.0
    return {"bal_acc": round(ba, 4), "precision": round(prec, 4), "fpr": round(fpr, 4)}


def compute_trace_metrics(probs, labels, cp):
    preds = (probs > 0.5).astype(int)
    if len(set(labels)) < 2:
        ba = float((preds == labels).mean())
    else:
        ba = balanced_accuracy_score(labels, preds)
    tp = int(((preds == 1) & (labels == 1)).sum())
    fp = int(((preds == 1) & (labels == 0)).sum())
    prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    if cp and 0 < cp < len(preds):
        fpr = float(preds[:cp].sum()) / cp
    else:
        fpr = 0.0
    return {"bal_acc": ba, "precision": prec, "fpr": fpr}


def sweep_layers(train_traces, val_traces, n_layers, window, step=1):
    layer_metrics = {}
    for si in range(0, n_layers, step):
        try:
            X_tr, y_tr = collect_data(train_traces, si, window)
            if len(set(y_tr)) < 2:
                continue
            clf, scaler = train_probe(X_tr, y_tr)
            all_probs, all_labels, all_cps = [], [], []
            for t in val_traces:
                probs, labels, cp = predict_trace(clf, scaler, t, si, window)
                all_probs.append(probs)
                all_labels.append(labels)
                all_cps.append(cp)
            metrics = compute_aggregate_metrics(all_probs, all_labels, all_cps)
            layer_metrics[si] = metrics
        except Exception:
            continue
    return layer_metrics


def select_layers(layer_metrics):
    if not layer_metrics:
        return None, None, None
    prec_layer = max(layer_metrics, key=lambda l: layer_metrics[l]["precision"])
    ba_layer = max(layer_metrics, key=lambda l: layer_metrics[l]["bal_acc"])
    fpr_layer = min(layer_metrics, key=lambda l: layer_metrics[l]["fpr"])
    return prec_layer, ba_layer, fpr_layer


def kfold_cv(model_name, cfg):
    print(f"\n{'='*60}")
    print(f"5-Fold Stratified CV: {model_name}")
    print(f"{'='*60}")

    traces = load_traces(cfg["hs_dir"])
    N = len(traces)
    print(f"  Loaded {N} traces")

    n_layers = cfg["n_stored_layers"]
    offset = cfg["layer_offset"]
    window = cfg["window"]
    step = cfg.get("sweep_step", 1)

    # Stratification label: CP position relative to median
    cps = [get_cp(t) for t in traces]
    median_cp = float(np.median(cps))
    strat_labels = np.array([1 if cp >= median_cp else 0 for cp in cps])
    print(f"  Median CP={median_cp:.0f}, strat balance: {Counter(strat_labels)}")

    skf = StratifiedKFold(n_splits=N_FOLDS, shuffle=True, random_state=SEED)

    ens_probs_all, ens_labels_all, ens_cps_all = [], [], []
    single_prec_probs_all = []
    single_ba_probs_all = []
    single_fpr_probs_all = []
    single_labels_all, single_cps_all = [], []

    fold_details = []
    t_start = time.time()

    for fold_i, (train_idx, test_idx) in enumerate(skf.split(np.arange(N), strat_labels)):
        fold_start = time.time()
        print(f"  Fold {fold_i+1}/{N_FOLDS}: train={len(train_idx)}, test={len(test_idx)}")

        train_traces = [traces[j] for j in train_idx]
        test_traces = [traces[j] for j in test_idx]

        # Inner 80/20 split of train for layer selection
        rng = np.random.default_rng(SEED + fold_i)
        inner_idx = rng.permutation(len(train_traces))
        n_inner_train = int(len(train_traces) * 0.8)
        inner_train = [train_traces[k] for k in inner_idx[:n_inner_train]]
        inner_val = [train_traces[k] for k in inner_idx[n_inner_train:]]

        print(f"    Inner split: train={len(inner_train)}, val={len(inner_val)}")

        layer_metrics = sweep_layers(inner_train, inner_val, n_layers, window, step)
        prec_li, ba_li, fpr_li = select_layers(layer_metrics)

        if prec_li is None:
            print(f"    WARNING: no valid layers, skipping fold")
            continue

        unique_layers = list(dict.fromkeys([prec_li, ba_li, fpr_li]))
        print(f"    Selected layers: prec=L{prec_li+offset}, ba=L{ba_li+offset}, fpr=L{fpr_li+offset} ({len(unique_layers)} unique)")

        # Train probes on ALL train traces at selected layers
        trained = {}
        for li in unique_layers:
            X_tr, y_tr = collect_data(train_traces, li, window)
            trained[li] = train_probe(X_tr, y_tr)

        # Predict each test trace at all selected layers
        for t in test_traces:
            preds_by_layer = {}
            last_labels, last_cp = None, None
            for li in unique_layers:
                clf, scaler = trained[li]
                probs, labels, cp = predict_trace(clf, scaler, t, li, window)
                preds_by_layer[li] = probs
                last_labels, last_cp = labels, cp

            single_prec_probs_all.append(preds_by_layer[prec_li])
            single_ba_probs_all.append(preds_by_layer[ba_li])
            single_fpr_probs_all.append(preds_by_layer[fpr_li])
            single_labels_all.append(last_labels)
            single_cps_all.append(last_cp)

            # Ensemble: average probabilities across layers
            min_len = min(len(preds_by_layer[li]) for li in unique_layers)
            ens_prob = np.mean([preds_by_layer[li][:min_len] for li in unique_layers], axis=0)
            ens_probs_all.append(ens_prob)
            ens_labels_all.append(last_labels[:min_len])
            ens_cps_all.append(last_cp)

        fold_elapsed = time.time() - fold_start
        print(f"    Fold {fold_i+1} done in {fold_elapsed:.1f}s")

        fold_details.append({
            "fold": fold_i,
            "n_train": len(train_idx),
            "n_test": len(test_idx),
            "selected_layers": {
                "precision": int(prec_li + offset),
                "ba": int(ba_li + offset),
                "fpr": int(fpr_li + offset),
            },
            "n_unique_layers": len(unique_layers),
            "elapsed_seconds": round(fold_elapsed, 1),
        })

    # Aggregate CV metrics
    ens_metrics = compute_aggregate_metrics(ens_probs_all, ens_labels_all, ens_cps_all)
    prec_metrics = compute_aggregate_metrics(single_prec_probs_all, single_labels_all, single_cps_all)
    ba_metrics = compute_aggregate_metrics(single_ba_probs_all, single_labels_all, single_cps_all)
    fpr_metrics = compute_aggregate_metrics(single_fpr_probs_all, single_labels_all, single_cps_all)

    # Per-trace stats
    ens_per_trace = [compute_trace_metrics(p, l, c)
                     for p, l, c in zip(ens_probs_all, ens_labels_all, ens_cps_all)]

    def trace_stats(per_trace, key):
        vals = [t[key] for t in per_trace]
        return {"mean": round(float(np.mean(vals)), 4), "std": round(float(np.std(vals)), 4),
                "min": round(float(np.min(vals)), 4), "max": round(float(np.max(vals)), 4)}

    # Layer selection stability across folds
    prec_layers = [f["selected_layers"]["precision"] for f in fold_details]
    ba_layers = [f["selected_layers"]["ba"] for f in fold_details]
    fpr_layers = [f["selected_layers"]["fpr"] for f in fold_details]

    total_elapsed = time.time() - t_start

    result = {
        "model": model_name,
        "n_traces": N,
        "n_folds": len(fold_details),
        "cv_type": "5-fold_stratified",
        "window": window,
        "layer_offset": offset,
        "metrics": {
            "ensemble_cv": ens_metrics,
            "single_precision_cv": prec_metrics,
            "single_ba_cv": ba_metrics,
            "single_fpr_cv": fpr_metrics,
        },
        "per_trace_stats": {
            "ensemble_ba": trace_stats(ens_per_trace, "bal_acc"),
            "ensemble_precision": trace_stats(ens_per_trace, "precision"),
            "ensemble_fpr": trace_stats(ens_per_trace, "fpr"),
        },
        "layer_selection_stability": {
            "precision_layers": prec_layers,
            "ba_layers": ba_layers,
            "fpr_layers": fpr_layers,
            "precision_counts": dict(Counter(prec_layers).most_common()),
            "ba_counts": dict(Counter(ba_layers).most_common()),
            "fpr_counts": dict(Counter(fpr_layers).most_common()),
        },
        "fold_details": fold_details,
        "elapsed_seconds": round(total_elapsed, 1),
    }

    print(f"\n  Results ({model_name}):")
    print(f"    {'Method':<25} {'BA':>7} {'Prec':>7} {'FPR':>7}")
    print(f"    {'-'*46}")
    print(f"    {'Ensemble CV':<25} {ens_metrics['bal_acc']:>7.4f} {ens_metrics['precision']:>7.4f} {ens_metrics['fpr']:>7.4f}")
    print(f"    {'Single-prec CV':<25} {prec_metrics['bal_acc']:>7.4f} {prec_metrics['precision']:>7.4f} {prec_metrics['fpr']:>7.4f}")
    print(f"    {'Single-BA CV':<25} {ba_metrics['bal_acc']:>7.4f} {ba_metrics['precision']:>7.4f} {ba_metrics['fpr']:>7.4f}")
    print(f"    {'Single-FPR CV':<25} {fpr_metrics['bal_acc']:>7.4f} {fpr_metrics['precision']:>7.4f} {fpr_metrics['fpr']:>7.4f}")
    print(f"    Layer stability: prec={prec_layers}, ba={ba_layers}, fpr={fpr_layers}")
    print(f"    Total time: {total_elapsed:.1f}s")

    return result


def main():
    t0 = time.time()
    results = {}

    for model_name in ["R1-8B"]:
        cfg = MODEL_CONFIGS[model_name]
        try:
            results[model_name] = kfold_cv(model_name, cfg)
        except Exception as e:
            import traceback
            traceback.print_exc()
            results[model_name] = {"error": str(e)}

    elapsed = time.time() - t0
    results["_meta"] = {
        "script": "n7_ensemble_loocv.py",
        "elapsed_seconds": round(elapsed, 1),
        "seed": SEED,
        "n_folds": N_FOLDS,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "description": "5-fold stratified CV validation of multi-metric ensemble layer selection. "
                       "Layer selection happens INSIDE each fold (inner 80/20 split of training set). "
                       "R1-8B only.",
    }

    def json_default(x):
        if isinstance(x, (np.floating, np.integer)):
            return float(x)
        if isinstance(x, np.ndarray):
            return x.tolist()
        return None

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_FILE, "w") as f:
        json.dump(results, f, indent=2, default=json_default)

    print(f"\n{'='*60}")
    print(f"Total runtime: {elapsed:.0f}s")
    print(f"Saved: {OUT_FILE}")


if __name__ == "__main__":
    main()
