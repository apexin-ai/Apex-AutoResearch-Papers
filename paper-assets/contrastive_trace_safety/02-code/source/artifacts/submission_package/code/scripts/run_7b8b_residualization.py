"""E-R11-1: Position residualization for R1-8B and OT-7B.
Replicates QwQ E-R9-4 protocol on 7-8B models.
"""

import sys, json, time, warnings, os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
# os.environ["HF_DATASETS_OFFLINE"] = "1"  # uncomment for offline mode
# os.environ["HF_HUB_OFFLINE"] = "1"  # uncomment for offline mode
# os.environ["HF_ENDPOINT"] = "..."  # set HF mirror if needed

import numpy as np
import torch
from pathlib import Path
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.decomposition import PCA
from scipy.stats import binom, wilcoxon
from sentence_transformers import SentenceTransformer

warnings.filterwarnings("ignore")

PROJECT = Path("DATA_DIR")
OUT_DIR = PROJECT / "artifacts" / "exp_r11_position_residualization"
OUT_DIR.mkdir(parents=True, exist_ok=True)

SEED = 42
WINDOW = 3

MODEL_CONFIGS = {
    "R1-8B": {
        "hs_dir": PROJECT / "artifacts" / "hidden_states",
        "layer_idx": 2,      # L14 = index 2 in stored layers 12-24
        "actual_layer": 14,
        "hidden_dim": 4096,
        "hf_model_name": "r1-8b",
    },
    "OT-7B": {
        "hs_dir": PROJECT / "artifacts" / "hidden_states_ot7b",
        "layer_idx": 16,     # L16 = index 16 (all 28 layers stored)
        "actual_layer": 16,
        "hidden_dim": 3584,
        "hf_model_name": "ot-7b",
    },
}

ST_MODEL_PATH = "MODEL_DIR/bge-large-en-v1.5/snapshots"
TEXT_DIM = 1024


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


def split(traces, seed=SEED):
    rng = np.random.default_rng(seed)
    idx = rng.permutation(len(traces))
    n_tr = int(len(traces) * 0.6)
    n_va = int(len(traces) * 0.2)
    return (
        [traces[i] for i in idx[:n_tr]],
        [traces[i] for i in idx[n_tr:n_tr + n_va]],
        [traces[i] for i in idx[n_tr + n_va:]],
    )


def apply_window(feats, window=WINDOW):
    n, dim = feats.shape
    half_w = window // 2
    padded = np.zeros((n + window - 1, dim), dtype=np.float32)
    padded[half_w:half_w + n] = feats
    return np.array([padded[i:i + window].flatten() for i in range(n)])


def extract_hs(trace, layer_idx):
    hs = trace["hidden_states"][:, layer_idx, :].float().numpy()
    labels = np.array(get_labels(trace))
    n = min(hs.shape[0], len(labels))
    return hs[:n].astype(np.float32), labels[:n]


def residualize(features):
    T = len(features)
    norm_pos = np.arange(T, dtype=np.float32).reshape(-1, 1) / T
    reg = LinearRegression().fit(norm_pos, features)
    return features - reg.predict(norm_pos)


def per_trace_ba(preds, labels):
    preds = np.asarray(preds)
    labels = np.asarray(labels)
    tp = int(((preds == 1) & (labels == 1)).sum())
    fp = int(((preds == 1) & (labels == 0)).sum())
    tn = int(((preds == 0) & (labels == 0)).sum())
    fn = int(((preds == 0) & (labels == 1)).sum())
    tpr = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    tnr = tn / (tn + fp) if (tn + fp) > 0 else 0.0
    return (tpr + tnr) / 2


def build_features(traces, layer_idx, do_residualize=False, position_only=False):
    X_list, y_list = [], []
    for t in traces:
        hs, labels = extract_hs(t, layer_idx)
        T = len(hs)
        if position_only:
            feat = np.arange(T, dtype=np.float32).reshape(-1, 1) / T
        elif do_residualize:
            feat = apply_window(residualize(hs))
        else:
            feat = apply_window(hs)
        X_list.append(feat)
        y_list.append(labels)
    return X_list, y_list


def load_sentence_map(hf_model_name):
    from datasets import load_dataset
    ds = load_dataset("ishitakakkar-10/HarmThoughts", split="train")
    from collections import defaultdict
    trace_sents = defaultdict(list)
    for row in ds:
        if row["model_name"] != hf_model_name:
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


def build_text_features(traces, st_model, sentence_map, do_residualize=False):
    X_list, y_list = [], []
    for t in traces:
        tid = t["trace_id"]
        labels = np.array(get_labels(t))
        sents = sentence_map.get(tid)
        if sents is None:
            continue
        n = min(len(sents), len(labels))
        embs = st_model.encode(sents[:n], normalize_embeddings=True, show_progress_bar=False)
        embs = embs.astype(np.float32)
        if do_residualize:
            feat = apply_window(residualize(embs))
        else:
            feat = apply_window(embs)
        X_list.append(feat)
        y_list.append(labels[:n])
    return X_list, y_list


def train_and_eval(X_train_list, y_train_list, X_test_list, y_test_list, n_pca=50):
    X_tr = np.concatenate(X_train_list)
    y_tr = np.concatenate(y_train_list)
    n_comp = min(n_pca, X_tr.shape[0], X_tr.shape[1])

    if X_tr.shape[1] > 1:
        pca = PCA(n_components=n_comp, random_state=SEED)
        X_tr_pca = pca.fit_transform(X_tr)
    else:
        pca = None
        X_tr_pca = X_tr

    clf = LogisticRegression(C=1.0, class_weight="balanced", solver="lbfgs",
                             max_iter=2000, random_state=SEED)
    clf.fit(X_tr_pca, y_tr)

    per_trace_bas = []
    all_preds, all_labels = [], []
    for X_te, y_te in zip(X_test_list, y_test_list):
        if pca is not None:
            X_te_pca = pca.transform(X_te)
        else:
            X_te_pca = X_te
        preds = clf.predict(X_te_pca)
        per_trace_bas.append(per_trace_ba(preds, y_te))
        all_preds.append(preds)
        all_labels.append(y_te)

    all_preds = np.concatenate(all_preds)
    all_labels = np.concatenate(all_labels)
    from sklearn.metrics import balanced_accuracy_score
    pooled_ba = float(balanced_accuracy_score(all_labels, all_preds))

    return pooled_ba, np.array(per_trace_bas)


def binomial_test_vs_chance(pooled_ba, n_test_steps):
    n_correct = int(round(pooled_ba * n_test_steps))
    p_val = float(binom.sf(n_correct - 1, n_test_steps, 0.5))
    return p_val


def run_model(model_name, cfg, st_model, sentence_map):
    print(f"\n{'='*60}", flush=True)
    print(f"{model_name} (L{cfg['actual_layer']}, W={WINDOW})", flush=True)
    print(f"{'='*60}", flush=True)

    traces = load_traces(cfg["hs_dir"])
    train, val, test = split(traces)
    train_val = train + val
    print(f"Traces: {len(traces)} total, train+val={len(train_val)}, test={len(test)}", flush=True)

    layer_idx = cfg["layer_idx"]

    # 1) Original HS
    X_tr, y_tr = build_features(train_val, layer_idx, do_residualize=False)
    X_te, y_te = build_features(test, layer_idx, do_residualize=False)
    orig_ba, orig_per_trace = train_and_eval(X_tr, y_tr, X_te, y_te)
    print(f"Original HS BA (pooled): {orig_ba:.4f}", flush=True)

    # 2) Residualized HS
    X_tr_r, y_tr_r = build_features(train_val, layer_idx, do_residualize=True)
    X_te_r, y_te_r = build_features(test, layer_idx, do_residualize=True)
    resid_ba, resid_per_trace = train_and_eval(X_tr_r, y_tr_r, X_te_r, y_te_r)

    n_test_steps = sum(len(y) for y in y_te_r)
    resid_p_binom = binomial_test_vs_chance(resid_ba, n_test_steps)

    resid_per_trace_shifted = resid_per_trace - 0.5
    nonzero = resid_per_trace_shifted[resid_per_trace_shifted != 0]
    if len(nonzero) >= 10:
        w_stat, w_p = wilcoxon(nonzero, alternative="greater")
    else:
        w_stat, w_p = float("nan"), float("nan")

    print(f"Residualized HS BA (pooled): {resid_ba:.4f} (drop: {(orig_ba - resid_ba)*100:.1f}pp)", flush=True)
    print(f"Residualized HS p-val (binomial): {resid_p_binom:.6f}", flush=True)
    print(f"Residualized HS p-val (Wilcoxon): {w_p:.6f}", flush=True)

    # 3) Position-only
    X_tr_p, y_tr_p = build_features(train_val, layer_idx, position_only=True)
    X_te_p, y_te_p = build_features(test, layer_idx, position_only=True)
    pos_ba, pos_per_trace = train_and_eval(X_tr_p, y_tr_p, X_te_p, y_te_p, n_pca=1)
    print(f"Position-only BA (pooled): {pos_ba:.4f}", flush=True)

    # 4) Original Text
    X_tr_t, y_tr_t = build_text_features(train_val, st_model, sentence_map, do_residualize=False)
    X_te_t, y_te_t = build_text_features(test, st_model, sentence_map, do_residualize=False)
    if len(X_tr_t) > 0 and len(X_te_t) > 0:
        orig_text_ba, _ = train_and_eval(X_tr_t, y_tr_t, X_te_t, y_te_t)
        print(f"Original Text BA (pooled): {orig_text_ba:.4f}", flush=True)
    else:
        orig_text_ba = float("nan")
        print("Text: no matching traces", flush=True)

    # 5) Residualized Text
    X_tr_tr, y_tr_tr = build_text_features(train_val, st_model, sentence_map, do_residualize=True)
    X_te_tr, y_te_tr = build_text_features(test, st_model, sentence_map, do_residualize=True)
    if len(X_tr_tr) > 0 and len(X_te_tr) > 0:
        resid_text_ba, _ = train_and_eval(X_tr_tr, y_tr_tr, X_te_tr, y_te_tr)
        print(f"Residualized Text BA (pooled): {resid_text_ba:.4f}", flush=True)
    else:
        resid_text_ba = float("nan")

    return {
        "model": model_name,
        "layer": cfg["actual_layer"],
        "window": WINDOW,
        "n_test_traces": len(test),
        "n_test_steps": n_test_steps,
        "original_hs_ba": round(orig_ba, 4),
        "residualized_hs_ba": round(resid_ba, 4),
        "drop_pp": round((orig_ba - resid_ba) * 100, 1),
        "residualized_hs_p_binomial": round(resid_p_binom, 6),
        "residualized_hs_p_wilcoxon": round(w_p, 6),
        "per_trace_bas_residualized": [round(float(b), 4) for b in resid_per_trace],
        "position_only_ba": round(pos_ba, 4),
        "original_text_ba": round(orig_text_ba, 4) if not np.isnan(orig_text_ba) else None,
        "residualized_text_ba": round(resid_text_ba, 4) if not np.isnan(resid_text_ba) else None,
    }


def main():
    t_start = time.time()

    # Load sentence transformer for text features
    import glob
    snap_dirs = sorted(glob.glob(ST_MODEL_PATH + "/*"))
    if snap_dirs:
        st_path = snap_dirs[-1]
    else:
        st_path = "BAAI/bge-large-en-v1.5"
    print(f"Loading ST model from {st_path}...", flush=True)
    st_model = SentenceTransformer(st_path)
    print("ST model loaded.", flush=True)

    results = {}
    for model_name, cfg in MODEL_CONFIGS.items():
        # Load sentence map for this model
        print(f"\nLoading sentence map for {cfg['hf_model_name']}...", flush=True)
        sentence_map = load_sentence_map(cfg["hf_model_name"])
        print(f"  {len(sentence_map)} traces with sentences", flush=True)

        r = run_model(model_name, cfg, st_model, sentence_map)
        results[model_name] = r

    # Print cross-model comparison
    qwq_ref = {
        "model": "QwQ-32B (ref)",
        "original_hs_ba": 0.735,
        "residualized_hs_ba": 0.612,
        "drop_pp": 12.3,
        "residualized_hs_p_binomial": 0.0024,
        "position_only_ba": 0.519,
    }

    print(f"\n{'='*80}", flush=True)
    print("Cross-model comparison", flush=True)
    print(f"{'='*80}", flush=True)
    header = f"{'Model':<15} {'Orig BA':>8} {'Resid BA':>9} {'Drop':>6} {'Resid p':>10} {'Pos-only':>9}"
    print(header, flush=True)
    print("-" * 60, flush=True)
    for r in list(results.values()) + [qwq_ref]:
        p_str = f"{r['residualized_hs_p_binomial']:.4f}" if r['residualized_hs_p_binomial'] is not None else "N/A"
        print(f"{r['model']:<15} {r['original_hs_ba']:>8.3f} {r['residualized_hs_ba']:>9.3f} {r['drop_pp']:>5.1f}pp {p_str:>10} {r['position_only_ba']:>9.3f}", flush=True)

    # Print detailed per-model results
    for model_name, r in results.items():
        n_test = r["n_test_traces"]
        print(f"\n=== {model_name} (L{r['layer']}, W={WINDOW}, n_test={n_test}) ===", flush=True)
        print(f"Original HS BA:        {r['original_hs_ba']:.3f}", flush=True)
        print(f"Residualized HS BA:    {r['residualized_hs_ba']:.3f} (drop: {r['drop_pp']:.1f}pp)", flush=True)
        print(f"Residualized HS p-val: {r['residualized_hs_p_binomial']:.6f} (binomial vs 0.5)", flush=True)
        print(f"Residualized HS p-val: {r['residualized_hs_p_wilcoxon']:.6f} (Wilcoxon vs 0.5)", flush=True)
        print(f"Position-only BA:      {r['position_only_ba']:.3f}", flush=True)
        if r.get("original_text_ba") is not None:
            print(f"Original Text BA:      {r['original_text_ba']:.3f}", flush=True)
        if r.get("residualized_text_ba") is not None:
            print(f"Residualized Text BA:  {r['residualized_text_ba']:.3f}", flush=True)

    elapsed = time.time() - t_start

    out = {
        "experiment": "exp_r11_position_residualization",
        "seed": SEED,
        "window": WINDOW,
        "results": results,
        "qwq_reference": qwq_ref,
        "elapsed_seconds": round(elapsed, 1),
    }
    out_path = OUT_DIR / "results.json"
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nSaved to {out_path} ({elapsed:.0f}s)", flush=True)


if __name__ == "__main__":
    main()
