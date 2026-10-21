#!/usr/bin/env python3
"""Verification: BGE 1024d comparison (Task 4) + Ensemble holdout (Task 5) for R1-8B."""

import os, sys, json, time, warnings
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["HF_HUB_DISABLE_XET"] = "1"
warnings.filterwarnings("ignore")

import numpy as np
import torch
from pathlib import Path
from collections import defaultdict
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import balanced_accuracy_score

PROJECT = Path("/root/autodl-tmp/contrastive_trace_safety")
ARTIFACTS = PROJECT / "artifacts"
HS_DIR = ARTIFACTS / "hidden_states_r1_8b_full"
BGE_PATH = PROJECT / "models" / "bge-large-en-v1.5"
OUT_DIR = ARTIFACTS / "verification"
OUT_DIR.mkdir(parents=True, exist_ok=True)

SEED = 42
HF_MODEL_NAME = "r1-8b"


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
    return sl.tolist() if isinstance(sl, torch.Tensor) else list(sl)


def get_cp(t):
    cp = t["commitment_point"]
    return int(cp.item()) if isinstance(cp, torch.Tensor) else int(cp)


def split_60_20_20(traces, seed=SEED):
    rng = np.random.default_rng(seed)
    idx = rng.permutation(len(traces))
    n_tr = int(len(traces) * 0.6)
    n_va = int(len(traces) * 0.2)
    return (
        [traces[i] for i in idx[:n_tr]],
        [traces[i] for i in idx[n_tr:n_tr + n_va]],
        [traces[i] for i in idx[n_tr + n_va:]],
    )


def load_sentence_map():
    from datasets import load_dataset
    ds = load_dataset("ishitakakkar-10/HarmThoughts", split="train")
    trace_sents = defaultdict(list)
    for row in ds:
        if row["model_name"] != HF_MODEL_NAME:
            continue
        sid = row["sentence_id"]
        parts = sid.rsplit("-", 1)
        trace_id = parts[0]
        step_idx = int(parts[1]) - 1
        trace_sents[trace_id].append((step_idx, row["sentence"]))
    result = {}
    for tid, steps in trace_sents.items():
        steps.sort(key=lambda x: x[0])
        result[tid] = [s[1] for s in steps]
    return result


# ============================================================
# Task 4: BGE 1024d ΔPrec (table3 approach)
# ============================================================

def apply_window_concat(feats, window=3):
    n, dim = feats.shape
    half_w = window // 2
    padded = np.zeros((n + window - 1, dim), dtype=np.float32)
    padded[half_w:half_w + n] = feats
    return np.array([padded[i:i + window].flatten() for i in range(n)])


def build_hs_table3(traces, layer_idx, window=3):
    X_list, y_list = [], []
    for t in traces:
        hs = t["hidden_states"][:, layer_idx, :]
        if isinstance(hs, torch.Tensor):
            hs = hs.float().numpy()
        labels = np.array(get_labels(t))
        n = min(hs.shape[0], len(labels))
        feat = apply_window_concat(hs[:n].astype(np.float32), window)
        X_list.append(feat)
        y_list.append(labels[:n])
    return X_list, y_list


def build_text_table3(traces, sentence_map, st_model, window=3):
    X_list, y_list = [], []
    for t in traces:
        tid = str(t.get("trace_id", ""))
        sents = sentence_map.get(tid)
        if sents is None:
            continue
        labels = np.array(get_labels(t))
        n = min(len(sents), len(labels))
        embs = st_model.encode(sents[:n], normalize_embeddings=True, show_progress_bar=False)
        feat = apply_window_concat(embs.astype(np.float32), window)
        X_list.append(feat)
        y_list.append(labels[:n])
    return X_list, y_list


def train_eval_with_pca(X_train_list, y_train_list, X_test_list, y_test_list, n_pca=100):
    X_tr = np.concatenate(X_train_list)
    y_tr = np.concatenate(y_train_list)
    n_comp = min(n_pca, X_tr.shape[0], X_tr.shape[1])
    pca = PCA(n_components=n_comp, random_state=SEED)
    X_tr_pca = pca.fit_transform(X_tr)
    clf = LogisticRegression(C=1.0, class_weight="balanced", solver="lbfgs",
                             max_iter=2000, random_state=SEED)
    clf.fit(X_tr_pca, y_tr)

    all_preds, all_labels = [], []
    per_trace_precs = []
    for X_te, y_te in zip(X_test_list, y_test_list):
        X_te_pca = pca.transform(X_te)
        preds = clf.predict(X_te_pca)
        all_preds.append(preds)
        all_labels.append(y_te)
        tp = int(((preds == 1) & (y_te == 1)).sum())
        fp = int(((preds == 1) & (y_te == 0)).sum())
        per_trace_precs.append(tp / (tp + fp) if (tp + fp) > 0 else 0.0)

    all_preds = np.concatenate(all_preds)
    all_labels = np.concatenate(all_labels)
    tp = int(((all_preds == 1) & (all_labels == 1)).sum())
    fp = int(((all_preds == 1) & (all_labels == 0)).sum())
    pooled_prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    pooled_ba = float(balanced_accuracy_score(all_labels, all_preds))
    return pooled_prec, pooled_ba, np.array(per_trace_precs), len(all_preds)


def bootstrap_delta(precs_a, precs_b, n_boot=10000, seed=SEED):
    rng = np.random.default_rng(seed)
    n = len(precs_a)
    observed = float(precs_a.mean() - precs_b.mean())
    count = 0
    for _ in range(n_boot):
        idx = rng.choice(n, size=n, replace=True)
        if precs_a[idx].mean() - precs_b[idx].mean() <= 0:
            count += 1
    return observed, count / n_boot


def run_task4(traces, train, val, test, sentence_map, st_model):
    print("\n" + "=" * 60)
    print("Task 4: BGE 1024d ΔPrec at L14")
    print("=" * 60)

    layer_idx = 14
    window = 3
    train_val = train + val

    X_hs_tr, y_hs_tr = build_hs_table3(train_val, layer_idx, window)
    X_hs_te, y_hs_te = build_hs_table3(test, layer_idx, window)
    hs_prec, hs_ba, hs_per_trace, n_steps = train_eval_with_pca(
        X_hs_tr, y_hs_tr, X_hs_te, y_hs_te, n_pca=100)
    print(f"  HS probe: prec={hs_prec:.4f}, BA={hs_ba:.4f}, n_test_steps={n_steps}")

    X_txt_tr, y_txt_tr = build_text_table3(train_val, sentence_map, st_model, window)
    X_txt_te, y_txt_te = build_text_table3(test, sentence_map, st_model, window)
    txt_prec, txt_ba, txt_per_trace, _ = train_eval_with_pca(
        X_txt_tr, y_txt_tr, X_txt_te, y_txt_te, n_pca=100)
    print(f"  Text probe (BGE 1024d): prec={txt_prec:.4f}, BA={txt_ba:.4f}")

    delta_prec = (hs_prec - txt_prec) * 100
    print(f"  ΔPrec: {delta_prec:+.1f}pp (paper: +5.8pp)")

    n_common = min(len(hs_per_trace), len(txt_per_trace))
    gap, p_val = bootstrap_delta(hs_per_trace[:n_common], txt_per_trace[:n_common])

    return {
        "layer": 14,
        "hs_prec": round(hs_prec, 4),
        "text_1024d_prec": round(txt_prec, 4),
        "delta_prec": round(delta_prec, 1),
        "paper_value": 5.8,
        "hs_ba": round(hs_ba, 4),
        "txt_ba": round(txt_ba, 4),
        "n_test_steps": n_steps,
        "n_test_traces": len(test),
        "bootstrap_gap": round(gap, 4),
        "bootstrap_p": round(p_val, 4),
        "window": window,
        "pca_dim": 100,
    }


# ============================================================
# Task 5: Ensemble holdout (n6 approach)
# ============================================================

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


def extract_hs_features(trace, layer_idx, window):
    hs = trace["hidden_states"][:, layer_idx, :]
    if isinstance(hs, torch.Tensor):
        hs = hs.float().numpy()
    return moving_avg(hs.astype(np.float32), window)


def collect_hs_data(traces, layer_idx, window):
    X_parts, y_parts = [], []
    for t in traces:
        feats = extract_hs_features(t, layer_idx, window)
        labels = get_labels(t)
        n = min(len(feats), len(labels))
        X_parts.append(feats[:n])
        y_parts.extend(labels[:n])
    return np.vstack(X_parts), np.array(y_parts)


def train_probe_scaler(X, y):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    clf = LogisticRegression(C=1.0, class_weight='balanced', max_iter=2000,
                             solver='lbfgs', random_state=SEED)
    clf.fit(X_scaled, y)
    return clf, scaler


def predict_traces_proba(clf, scaler, traces, layer_idx, window):
    results = []
    for t in traces:
        feats = extract_hs_features(t, layer_idx, window)
        labels = get_labels(t)
        n = min(len(feats), len(labels))
        X_scaled = scaler.transform(feats[:n])
        if len(clf.classes_) == 1:
            probs = np.full(n, 0.5)
        else:
            probs = clf.predict_proba(X_scaled)[:, 1]
        results.append({
            "trace_id": str(t.get("trace_id", "")),
            "probs": probs,
            "labels": np.array(labels[:n]),
            "commitment_point": get_cp(t),
        })
    return results


def compute_metrics(trace_results):
    all_preds, all_labels = [], []
    pre_fp, pre_total = 0, 0
    for tr in trace_results:
        preds = (tr["probs"] > 0.5).astype(int)
        all_preds.extend(preds)
        all_labels.extend(tr["labels"])
        cp = tr["commitment_point"]
        if cp is not None and cp > 0 and cp < len(preds):
            pre_fp += int(preds[:cp].sum())
            pre_total += cp
    all_preds = np.array(all_preds)
    all_labels = np.array(all_labels)
    ba = balanced_accuracy_score(all_labels, all_preds)
    tp = int(((all_preds == 1) & (all_labels == 1)).sum())
    fp = int(((all_preds == 1) & (all_labels == 0)).sum())
    prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    fpr = pre_fp / pre_total if pre_total > 0 else 0.0
    return {"bal_acc": round(ba, 4), "precision": round(prec, 4), "fpr": round(fpr, 4)}


def per_trace_precision(trace_results):
    vals = []
    for tr in trace_results:
        preds = (tr["probs"] > 0.5).astype(int)
        labels = tr["labels"]
        tp = int(((preds == 1) & (labels == 1)).sum())
        fp = int(((preds == 1) & (labels == 0)).sum())
        vals.append(tp / (tp + fp) if (tp + fp) > 0 else 0.0)
    return np.array(vals)


def ensemble_results(results_list):
    by_id = {}
    for results in results_list:
        for tr in results:
            tid = tr["trace_id"]
            if tid not in by_id:
                by_id[tid] = {"probs_list": [], "labels": tr["labels"],
                              "commitment_point": tr["commitment_point"]}
            by_id[tid]["probs_list"].append(tr["probs"])
    ensembled = []
    for tid in sorted(by_id):
        data = by_id[tid]
        if len(data["probs_list"]) < len(results_list):
            continue
        min_len = min(len(p) for p in data["probs_list"])
        avg_probs = np.mean([p[:min_len] for p in data["probs_list"]], axis=0)
        ensembled.append({
            "trace_id": tid,
            "probs": avg_probs,
            "labels": data["labels"][:min_len],
            "commitment_point": data["commitment_point"],
        })
    return ensembled


def sweep_layers_for_fpr(train, val, n_layers, window, exclude_layers, step=1):
    best_fpr = 1.0
    best_layer = None
    for li in range(0, n_layers, step):
        if li in exclude_layers:
            continue
        try:
            X_tr, y_tr = collect_hs_data(train, li, window)
            if len(set(y_tr)) < 2:
                continue
            clf, scaler = train_probe_scaler(X_tr, y_tr)
            val_res = predict_traces_proba(clf, scaler, val, li, window)
            m = compute_metrics(val_res)
            if m["fpr"] < best_fpr:
                best_fpr = m["fpr"]
                best_layer = li
        except Exception:
            continue
    return best_layer


def run_task5(traces, train, val, test, sentence_map, st_model):
    print("\n" + "=" * 60)
    print("Task 5: Ensemble holdout (3-metric)")
    print("=" * 60)

    window = 15
    prec_layer = 14
    ba_layer = 12
    n_layers = 25

    print(f"  Finding FPR-best layer (sweep L0-L24, exclude L{prec_layer},L{ba_layer})...")
    fpr_layer = sweep_layers_for_fpr(train, val, n_layers, window,
                                      {prec_layer, ba_layer}, step=1)
    if fpr_layer is None:
        fpr_layer = 13
    print(f"  Layers: precision=L{prec_layer}, BA=L{ba_layer}, FPR=L{fpr_layer}")

    unique_layers = list(dict.fromkeys([prec_layer, ba_layer, fpr_layer]))
    print(f"  Unique layers: {len(unique_layers)} — {unique_layers}")

    layer_results = {}
    for li in unique_layers:
        print(f"  Training L{li} probe (W={window})...")
        X_tr, y_tr = collect_hs_data(train, li, window)
        clf, scaler = train_probe_scaler(X_tr, y_tr)
        test_res = predict_traces_proba(clf, scaler, test, li, window)
        layer_results[li] = test_res
        m = compute_metrics(test_res)
        print(f"    BA={m['bal_acc']:.4f}  Prec={m['precision']:.4f}  FPR={m['fpr']:.4f}")

    ens_res = ensemble_results([layer_results[li] for li in unique_layers])
    ens_m = compute_metrics(ens_res)
    print(f"  Ensemble: BA={ens_m['bal_acc']:.4f}  Prec={ens_m['precision']:.4f}  FPR={ens_m['fpr']:.4f}")
    print(f"  Paper Ens Prec: 0.565")

    print("  Training text probe for ensemble comparison...")
    X_txt_parts, y_txt_parts = [], []
    for t in train:
        tid = str(t.get("trace_id", ""))
        sents = sentence_map.get(tid)
        if sents is None:
            continue
        labels = get_labels(t)
        n = min(len(sents), len(labels))
        embs = st_model.encode(sents[:n], normalize_embeddings=True, show_progress_bar=False)
        feat = moving_avg(embs.astype(np.float32), window)
        X_txt_parts.append(feat[:n])
        y_txt_parts.extend(labels[:n])

    text_metrics = {"bal_acc": None, "precision": None, "fpr": None}
    ens_text_delta = None
    bootstrap_p = None
    if X_txt_parts:
        X_txt = np.vstack(X_txt_parts)
        y_txt = np.array(y_txt_parts)
        txt_clf, txt_scaler = train_probe_scaler(X_txt, y_txt)

        txt_test_results = []
        for t in test:
            tid = str(t.get("trace_id", ""))
            sents = sentence_map.get(tid)
            if sents is None:
                continue
            labels = get_labels(t)
            n = min(len(sents), len(labels))
            embs = st_model.encode(sents[:n], normalize_embeddings=True, show_progress_bar=False)
            feat = moving_avg(embs.astype(np.float32), window)
            X_scaled = txt_scaler.transform(feat[:n])
            probs = txt_clf.predict_proba(X_scaled)[:, 1]
            txt_test_results.append({
                "trace_id": tid,
                "probs": probs,
                "labels": np.array(labels[:n]),
                "commitment_point": get_cp(t),
            })

        text_metrics = compute_metrics(txt_test_results)
        print(f"  Text:  BA={text_metrics['bal_acc']:.4f}  Prec={text_metrics['precision']:.4f}")

        ens_text_delta = (ens_m["precision"] - text_metrics["precision"]) * 100
        print(f"  Ens-Text: {ens_text_delta:+.1f}pp (paper: +19.3pp)")

        ens_per = per_trace_precision(ens_res)
        txt_per = per_trace_precision(txt_test_results)
        n_common = min(len(ens_per), len(txt_per))
        if n_common > 0:
            gap, bootstrap_p = bootstrap_delta(ens_per[:n_common], txt_per[:n_common])
    else:
        print("  Text: NO MATCHING EMBEDDINGS")

    return {
        "layers": {"precision": prec_layer, "ba": ba_layer, "fpr": fpr_layer},
        "n_unique_layers": len(unique_layers),
        "window": window,
        "ens_precision": ens_m["precision"],
        "ens_ba": ens_m["bal_acc"],
        "ens_fpr": ens_m["fpr"],
        "text_precision": text_metrics["precision"],
        "ens_text_delta_pp": round(ens_text_delta, 1) if ens_text_delta is not None else None,
        "bootstrap_p": round(bootstrap_p, 4) if bootstrap_p is not None else None,
        "paper_ens_prec": 0.565,
        "paper_ens_text_delta": 19.3,
        "n_test_traces": len(test),
        "per_layer_metrics": {
            f"L{li}": compute_metrics(layer_results[li]) for li in unique_layers
        },
    }


# ============================================================
# Main
# ============================================================

def main():
    t0 = time.time()
    print("Loading traces...", flush=True)
    traces = load_traces(HS_DIR)
    print(f"  Loaded {len(traces)} traces", flush=True)

    train, val, test = split_60_20_20(traces)
    print(f"  Split: train={len(train)}, val={len(val)}, test={len(test)}", flush=True)

    print("Loading HarmThoughts sentences...", flush=True)
    sentence_map = load_sentence_map()
    matched = sum(1 for t in traces if str(t.get("trace_id", "")) in sentence_map)
    print(f"  Matched {matched}/{len(traces)} traces to text", flush=True)

    print("Loading BGE-large-en-v1.5...", flush=True)
    from sentence_transformers import SentenceTransformer
    if BGE_PATH.exists():
        st_model = SentenceTransformer(str(BGE_PATH))
    else:
        st_model = SentenceTransformer("BAAI/bge-large-en-v1.5")
    emb = st_model.encode(["test"])
    print(f"  BGE dim={emb.shape[1]}", flush=True)

    task4_result = run_task4(traces, train, val, test, sentence_map, st_model)
    task5_result = run_task5(traces, train, val, test, sentence_map, st_model)

    elapsed = time.time() - t0

    bge_output = {
        "task": "bge_1024d_verification",
        "models": {
            "r1_8b": task4_result,
        },
        "missing_models": ["ot_7b", "qwq_32b", "r1_32b"],
        "missing_reason": "Hidden states for OT-7B, QwQ-32B, R1-32B not available on this server",
        "text_encoder": "BAAI/bge-large-en-v1.5",
        "text_dim": 1024,
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "elapsed_seconds": round(elapsed, 1),
    }

    ensemble_output = {
        "task": "ensemble_holdout_verification",
        "models": {
            "r1_8b": task5_result,
        },
        "missing_models": ["ot_7b", "qwq_32b", "r1_32b"],
        "missing_reason": "Hidden states for OT-7B, QwQ-32B, R1-32B not available on this server",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "elapsed_seconds": round(elapsed, 1),
    }

    def json_default(x):
        if isinstance(x, (np.floating, np.integer)):
            return float(x)
        if isinstance(x, np.ndarray):
            return x.tolist()
        return None

    with open(OUT_DIR / "bge_1024d_verification.json", "w") as f:
        json.dump(bge_output, f, indent=2, default=json_default)
    print(f"\nSaved: {OUT_DIR / 'bge_1024d_verification.json'}")

    with open(OUT_DIR / "ensemble_holdout_verification.json", "w") as f:
        json.dump(ensemble_output, f, indent=2, default=json_default)
    print(f"Saved: {OUT_DIR / 'ensemble_holdout_verification.json'}")

    print(f"\nTotal time: {elapsed:.0f}s")

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Task 4 — BGE 1024d ΔPrec (R1-8B L14):")
    print(f"  HS Prec:   {task4_result['hs_prec']:.4f}")
    print(f"  Text Prec: {task4_result['text_1024d_prec']:.4f}")
    print(f"  ΔPrec:     {task4_result['delta_prec']:+.1f}pp  (paper: +5.8pp)")
    print(f"\nTask 5 — Ensemble holdout (R1-8B):")
    print(f"  Ens Prec:      {task5_result['ens_precision']:.4f}  (paper: 0.565)")
    if task5_result.get('ens_text_delta_pp') is not None:
        print(f"  Ens-Text:      {task5_result['ens_text_delta_pp']:+.1f}pp  (paper: +19.3pp)")
    if task5_result.get('bootstrap_p') is not None:
        print(f"  Bootstrap p:   {task5_result['bootstrap_p']:.4f}")


if __name__ == "__main__":
    main()
