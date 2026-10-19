"""Threshold sensitivity analysis for QwQ-32B and R1-32B.

Sweeps classification threshold in [0.3, 0.4, 0.5, 0.6, 0.7] and
K-consecutive in [3, 5, 7, 10] to verify detection robustness.
Evaluates both HS probe and Text (BGE-large) probe.
"""

import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
# os.environ["HF_ENDPOINT"] = "..."  # set HF mirror if needed

import sys
import json
import warnings
import time
import numpy as np
import torch
from pathlib import Path
from collections import defaultdict
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score
from sklearn.preprocessing import StandardScaler

sys.path.insert(0, "DATA_DIR")
warnings.filterwarnings("ignore")

BASE = Path("DATA_DIR")
OUT_DIR = BASE / "artifacts/exp_r9_threshold_sensitivity"
OUT_DIR.mkdir(parents=True, exist_ok=True)

BGE_MODEL_PATH = str(BASE / "models/bge-large-en-v1.5")
BGE_DIM = 1024
SEED = 42
THRESHOLDS = [0.3, 0.4, 0.5, 0.6, 0.7]
K_VALUES = [3, 5, 7, 10]

MODEL_CONFIGS = {
    "qwq_32b": {
        "model_name_hf": "QwQ",
        "hs_dir": BASE / "artifacts/hidden_states_qwq_32b",
        "layer_idx": 60,
        "hidden_dim": 5120,
        "window": 3,
    },
    "r1_32b": {
        "model_name_hf": "r1-32b",
        "hs_dir": BASE / "artifacts/hidden_states_r1_32b",
        "layer_idx": 63,
        "hidden_dim": 5120,
        "window": 10,
    },
}


def load_sentences_from_hf(model_name_hf):
    from datasets import load_dataset
    ds = load_dataset("ishitakakkar-10/HarmThoughts", split="train")
    traces = defaultdict(list)
    for row in ds:
        if row["model_name"] != model_name_hf:
            continue
        sid = row["sentence_id"]
        parts = sid.rsplit("-", 1)
        trace_id = parts[0]
        step_idx = int(parts[1]) - 1
        traces[trace_id].append((step_idx, row["sentence"]))
    for tid in traces:
        traces[tid].sort(key=lambda x: x[0])
        traces[tid] = [s for _, s in traces[tid]]
    return dict(traces)


def load_traces(hs_dir, sentences_map, layer_idx):
    traces = []
    for pt_file in sorted(hs_dir.glob("*.pt")):
        d = torch.load(pt_file, map_location="cpu", weights_only=False)
        if d.get("step_labels") is None or d.get("commitment_point") is None:
            continue
        trace_id = d["trace_id"]
        if trace_id not in sentences_map:
            continue
        sentences = sentences_map[trace_id]
        sl = d["step_labels"]
        if isinstance(sl, torch.Tensor):
            sl = sl.tolist()
        else:
            sl = list(sl)
        n_steps = len(sl)
        if len(sentences) < n_steps:
            continue
        hs = d["hidden_states"][:n_steps, layer_idx, :].float().numpy()
        traces.append({
            "trace_id": trace_id,
            "hidden_states": hs.astype(np.float32),
            "step_labels": sl,
            "sentences": sentences[:n_steps],
            "commitment_point": int(d["commitment_point"]),
        })
    return traces


def split_traces(traces, seed=SEED):
    rng = np.random.default_rng(seed)
    indices = rng.permutation(len(traces))
    n_train = int(len(traces) * 0.6)
    n_val = int(len(traces) * 0.2)
    return (
        [traces[i] for i in indices[:n_train]],
        [traces[i] for i in indices[n_train:n_train + n_val]],
        [traces[i] for i in indices[n_train + n_val:]],
    )


def compute_windowed_average(features, window):
    n_steps = features.shape[0]
    cumsum = np.cumsum(features, axis=0)
    X = np.zeros_like(features)
    for t in range(n_steps):
        start = max(0, t - window + 1)
        if start == 0:
            X[t] = cumsum[t] / (t + 1)
        else:
            X[t] = (cumsum[t] - cumsum[start - 1]) / (t - start + 1)
    return X


def build_hs_features(traces, window):
    X_list, y_list = [], []
    for t in traces:
        hs = t["hidden_states"]
        labels = np.array(t["step_labels"], dtype=np.int32)
        n = min(hs.shape[0], len(labels))
        windowed = compute_windowed_average(hs[:n], window)
        X_list.append(windowed)
        y_list.append(labels[:n])
    return np.concatenate(X_list, axis=0), np.concatenate(y_list)


def build_text_features(traces, st_model, window):
    X_list, y_list = [], []
    for t in traces:
        sentences = t["sentences"]
        labels = np.array(t["step_labels"], dtype=np.int32)
        n = min(len(sentences), len(labels))
        embeddings = st_model.encode(sentences[:n], show_progress_bar=False,
                                     normalize_embeddings=True)
        windowed = compute_windowed_average(embeddings, window)
        X_list.append(windowed)
        y_list.append(labels[:n])
    return np.concatenate(X_list, axis=0), np.concatenate(y_list)


def train_lr(X_train, y_train):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_train)
    lr = LogisticRegression(
        C=1.0, class_weight="balanced", solver="lbfgs",
        max_iter=2000, random_state=SEED
    )
    lr.fit(X_scaled, y_train)
    return lr, scaler


def predict_per_trace(lr, scaler, traces, feature_fn):
    results = []
    for t in traces:
        X = feature_fn(t)
        X_scaled = scaler.transform(X)
        probs = lr.predict_proba(X_scaled)[:, 1]
        labels = np.array(t["step_labels"], dtype=np.int32)
        n = min(len(probs), len(labels))
        results.append({
            "probs": probs[:n],
            "labels": labels[:n],
            "cp": t["commitment_point"],
        })
    return results


def step_level_metrics(trace_results, threshold):
    all_preds, all_labels = [], []
    all_pre_cp_preds, all_pre_cp_labels = [], []
    for tr in trace_results:
        preds = (tr["probs"] > threshold).astype(int)
        labels = tr["labels"]
        n = min(len(preds), len(labels))
        all_preds.append(preds[:n])
        all_labels.append(labels[:n])
        cp = tr["cp"]
        if cp > 0 and cp <= n:
            all_pre_cp_preds.append(preds[:cp])
            all_pre_cp_labels.append(labels[:cp])

    preds = np.concatenate(all_preds)
    labels = np.concatenate(all_labels)

    tp = int(((preds == 1) & (labels == 1)).sum())
    fp = int(((preds == 1) & (labels == 0)).sum())
    tn = int(((preds == 0) & (labels == 0)).sum())
    fn = int(((preds == 0) & (labels == 1)).sum())

    tpr = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    tnr = tn / (tn + fp) if (tn + fp) > 0 else 0.0
    bal_acc = (tpr + tnr) / 2
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tpr
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0.0

    return {
        "bal_acc": round(bal_acc, 4),
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "fpr": round(fpr, 4),
    }


def k_consecutive_detection(probs, k, threshold):
    above = probs > threshold
    count = 0
    for a in above:
        if a:
            count += 1
            if count >= k:
                return True
        else:
            count = 0
    return False


def trace_level_detection_rate(trace_results, k, threshold):
    detected = sum(
        1 for tr in trace_results
        if k_consecutive_detection(tr["probs"], k, threshold)
    )
    return round(detected / len(trace_results), 4) if trace_results else 0.0


def run_model(model_key, cfg, st_model):
    print(f"\n{'='*60}", flush=True)
    print(f"  {model_key}: Layer {cfg['layer_idx']}, W={cfg['window']}", flush=True)
    print(f"{'='*60}", flush=True)

    print("Loading sentences from HF...", flush=True)
    sentences_map = load_sentences_from_hf(cfg["model_name_hf"])
    print(f"  Found {len(sentences_map)} traces in HF dataset", flush=True)

    print("Loading .pt traces...", flush=True)
    traces = load_traces(cfg["hs_dir"], sentences_map, cfg["layer_idx"])
    print(f"  Loaded {len(traces)} traces with HS + sentences", flush=True)

    train, val, test = split_traces(traces)
    print(f"  Split: train={len(train)}, val={len(val)}, test={len(test)}", flush=True)
    train_val = train + val

    # --- HS probe ---
    print("Training HS probe...", flush=True)
    X_tr_hs, y_tr_hs = build_hs_features(train_val, cfg["window"])
    lr_hs, scaler_hs = train_lr(X_tr_hs, y_tr_hs)

    def hs_feat_fn(t):
        hs = t["hidden_states"]
        labels = np.array(t["step_labels"])
        n = min(hs.shape[0], len(labels))
        return compute_windowed_average(hs[:n], cfg["window"])

    hs_results = predict_per_trace(lr_hs, scaler_hs, test, hs_feat_fn)

    # --- Text probe ---
    print("Training Text probe (BGE-large)...", flush=True)
    X_tr_text, y_tr_text = build_text_features(train_val, st_model, cfg["window"])
    lr_text, scaler_text = train_lr(X_tr_text, y_tr_text)

    def text_feat_fn(t):
        sentences = t["sentences"]
        labels = np.array(t["step_labels"])
        n = min(len(sentences), len(labels))
        emb = st_model.encode(sentences[:n], show_progress_bar=False,
                              normalize_embeddings=True)
        return compute_windowed_average(emb, cfg["window"])

    text_results = predict_per_trace(lr_text, scaler_text, test, text_feat_fn)

    # --- Threshold sweep ---
    print("\nThreshold sweep (step-level):", flush=True)
    hs_metrics = {k: [] for k in ["bal_acc", "precision", "recall", "fpr"]}
    text_metrics = {k: [] for k in ["bal_acc", "precision", "recall", "fpr"]}
    delta_metrics = {k: [] for k in ["bal_acc", "precision", "fpr"]}
    hs_det_k5 = []
    text_det_k5 = []

    for thr in THRESHOLDS:
        hs_m = step_level_metrics(hs_results, thr)
        text_m = step_level_metrics(text_results, thr)
        for k in hs_metrics:
            hs_metrics[k].append(hs_m[k])
            text_metrics[k].append(text_m[k])
        for k in delta_metrics:
            delta_metrics[k].append(round(hs_m[k] - text_m[k], 4))

        hs_dr = trace_level_detection_rate(hs_results, 5, thr)
        text_dr = trace_level_detection_rate(text_results, 5, thr)
        hs_det_k5.append(hs_dr)
        text_det_k5.append(text_dr)

        print(f"  thr={thr}: HS bal_acc={hs_m['bal_acc']:.4f} prec={hs_m['precision']:.4f} "
              f"fpr={hs_m['fpr']:.4f} det_K5={hs_dr:.4f} | "
              f"Text bal_acc={text_m['bal_acc']:.4f} prec={text_m['precision']:.4f} "
              f"fpr={text_m['fpr']:.4f} det_K5={text_dr:.4f}", flush=True)

    hs_metrics["detection_rate_K5"] = hs_det_k5
    text_metrics["detection_rate_K5"] = text_det_k5

    # --- K sweep at multiple thresholds ---
    print("\nK sweep (trace-level detection rate):", flush=True)
    k_sweep = {}
    for thr in THRESHOLDS:
        key = f"threshold_{thr}"
        hs_drs = [trace_level_detection_rate(hs_results, k, thr) for k in K_VALUES]
        text_drs = [trace_level_detection_rate(text_results, k, thr) for k in K_VALUES]
        k_sweep[key] = {"K": K_VALUES, "hs_det_rate": hs_drs, "text_det_rate": text_drs}
        print(f"  thr={thr}: K={K_VALUES}", flush=True)
        print(f"    HS   det_rate={hs_drs}", flush=True)
        print(f"    Text det_rate={text_drs}", flush=True)

    return {
        "thresholds": THRESHOLDS,
        "hs": hs_metrics,
        "text": text_metrics,
        "delta": delta_metrics,
        "k_sweep": k_sweep,
        "n_train": len(train_val),
        "n_test": len(test),
    }


def print_summary_table(results):
    print("\n" + "=" * 80, flush=True)
    print("SUMMARY: Threshold Sensitivity Analysis", flush=True)
    print("=" * 80, flush=True)

    for model_key, res in results.items():
        print(f"\n--- {model_key} (n_test={res['n_test']}) ---", flush=True)

        print(f"\n  {'Threshold':<12} {'HS bal_acc':<12} {'Text bal_acc':<13} {'Delta':<10} "
              f"{'HS FPR':<10} {'Text FPR':<10} {'HS det_K5':<11} {'Text det_K5':<12}", flush=True)
        print("  " + "-" * 90, flush=True)
        for i, thr in enumerate(res["thresholds"]):
            print(f"  {thr:<12.1f} {res['hs']['bal_acc'][i]:<12.4f} "
                  f"{res['text']['bal_acc'][i]:<13.4f} {res['delta']['bal_acc'][i]:<10.4f} "
                  f"{res['hs']['fpr'][i]:<10.4f} {res['text']['fpr'][i]:<10.4f} "
                  f"{res['hs']['detection_rate_K5'][i]:<11.4f} "
                  f"{res['text']['detection_rate_K5'][i]:<12.4f}", flush=True)

        print(f"\n  K sweep at threshold=0.5:", flush=True)
        ks = res["k_sweep"]["threshold_0.5"]
        print(f"    K:         {ks['K']}", flush=True)
        print(f"    HS det:    {ks['hs_det_rate']}", flush=True)
        print(f"    Text det:  {ks['text_det_rate']}", flush=True)

        ba_range = max(res["hs"]["bal_acc"]) - min(res["hs"]["bal_acc"])
        fpr_range = max(res["hs"]["fpr"]) - min(res["hs"]["fpr"])
        print(f"\n  HS bal_acc range across thresholds: {ba_range:.4f}", flush=True)
        print(f"  HS FPR range across thresholds: {fpr_range:.4f}", flush=True)
        delta_ba = res["delta"]["bal_acc"]
        print(f"  Delta(HS-Text) bal_acc: min={min(delta_ba):.4f} max={max(delta_ba):.4f}", flush=True)


def main():
    t0 = time.time()

    print("Loading BGE-large model...", flush=True)
    from sentence_transformers import SentenceTransformer
    st_model = SentenceTransformer(BGE_MODEL_PATH)
    print(f"  BGE-large loaded in {time.time()-t0:.1f}s", flush=True)

    results = {}
    for model_key, cfg in MODEL_CONFIGS.items():
        results[model_key] = run_model(model_key, cfg, st_model)

    out_path = OUT_DIR / "results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}", flush=True)

    print_summary_table(results)

    print(f"\nTotal time: {time.time()-t0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
