"""N6: Multi-Metric Layer Ensemble Proof-of-Concept.

For each of 4 models, train probes at 3 candidate layers (precision-best,
BA-best, FPR-best), ensemble their per-step probabilities, and compare
against single-layer and text baselines. Bootstrap significance tests
on ensemble vs text and ensemble vs best-single-layer.
"""

import os, sys, json, pickle, warnings, time
os.environ["TOKENIZERS_PARALLELISM"] = "false"
warnings.filterwarnings("ignore")

import numpy as np
import torch
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import balanced_accuracy_score

PROJECT = Path("DATA_DIR")
ARTIFACTS = PROJECT / "artifacts"
OUT_DIR = ARTIFACTS / "n6_multi_metric_ensemble"
OUT_DIR.mkdir(parents=True, exist_ok=True)

SEED = 42
N_BOOTSTRAP = 10000

MODEL_CONFIGS = {
    "R1-8B": {
        "hs_dir": ARTIFACTS / "hidden_states",
        "layer_offset": 12,
        "n_stored_layers": 13,
        "hidden_dim": 4096,
        "window": 15,
        "precision_layer": 14,
        "ba_layer": 12,
        "text_emb_pkl": ARTIFACTS / "r12_5seed_hb" / "r1_8b_text_emb.pkl",
        "sweep_step": 1,
    },
    "OT-7B": {
        "hs_dir": ARTIFACTS / "hidden_states_ot7b",
        "layer_offset": 0,
        "n_stored_layers": 28,
        "hidden_dim": 3584,
        "window": 3,
        "precision_layer": 16,
        "ba_layer": 9,
        "fpr_layer_hint": 18,
        "text_emb_pkl": ARTIFACTS / "ot7b_text_embeddings.pkl",
        "sweep_step": 1,
    },
    "QwQ-32B": {
        "hs_dir": ARTIFACTS / "hidden_states_qwq_32b",
        "layer_offset": 0,
        "n_stored_layers": 64,
        "hidden_dim": 5120,
        "window": 3,
        "precision_layer": 60,
        "ba_layer": 30,
        "fpr_layer_hint": 63,
        "text_emb_pkl": ARTIFACTS / "r12_5seed_hb" / "qwq_text_emb.pkl",
        "sweep_step": 4,
    },
    "R1-32B": {
        "hs_dir": ARTIFACTS / "hidden_states_r1_32b",
        "layer_offset": 0,
        "n_stored_layers": 64,
        "hidden_dim": 5120,
        "window": 1,
        "precision_layer": 63,
        "ba_layer": 47,
        "text_emb_pkl": ARTIFACTS / "r12_5seed_hb" / "r1_32b_text_emb.pkl",
        "sweep_step": 4,
    },
}


# ============================================================
# Data loading
# ============================================================

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


def split_traces(traces, seed=SEED):
    rng = np.random.default_rng(seed)
    idx = rng.permutation(len(traces))
    n_tr = int(len(traces) * 0.6)
    n_va = int(len(traces) * 0.2)
    return (
        [traces[i] for i in idx[:n_tr]],
        [traces[i] for i in idx[n_tr:n_tr + n_va]],
        [traces[i] for i in idx[n_tr + n_va:]],
    )


# ============================================================
# Feature extraction
# ============================================================

def moving_avg(hs, window):
    """Causal moving average: step i = mean(hs[max(0, i-W+1) : i+1])."""
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


def extract_text_features(text_emb_dict, trace_id, window):
    emb = text_emb_dict.get(trace_id)
    if emb is None:
        return None
    if isinstance(emb, torch.Tensor):
        emb = emb.numpy()
    return moving_avg(emb.astype(np.float32), window)


# ============================================================
# Probe training and prediction
# ============================================================

def collect_hs_data(traces, layer_idx, window):
    X_parts, y_parts = [], []
    for t in traces:
        feats = extract_hs_features(t, layer_idx, window)
        labels = get_labels(t)
        n = min(len(feats), len(labels))
        X_parts.append(feats[:n])
        y_parts.extend(labels[:n])
    return np.vstack(X_parts), np.array(y_parts)


def train_probe(X_train, y_train):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_train)
    clf = LogisticRegression(C=1.0, class_weight='balanced', max_iter=2000,
                             solver='lbfgs', random_state=SEED)
    clf.fit(X_scaled, y_train)
    return clf, scaler


def predict_hs_traces(clf, scaler, traces, layer_idx, window):
    results = []
    for t in traces:
        feats = extract_hs_features(t, layer_idx, window)
        labels = get_labels(t)
        n = min(len(feats), len(labels))
        probs = clf.predict_proba(scaler.transform(feats[:n]))[:, 1]
        results.append({
            "trace_id": str(t.get("trace_id", "")),
            "probs": probs,
            "labels": np.array(labels[:n]),
            "commitment_point": get_cp(t),
        })
    return results


def predict_text_traces(clf, scaler, traces, text_emb_dict, window):
    results = []
    for t in traces:
        tid = str(t.get("trace_id", ""))
        emb = extract_text_features(text_emb_dict, tid, window)
        if emb is None:
            continue
        labels = get_labels(t)
        n = min(len(emb), len(labels))
        probs = clf.predict_proba(scaler.transform(emb[:n]))[:, 1]
        results.append({
            "trace_id": tid,
            "probs": probs,
            "labels": np.array(labels[:n]),
            "commitment_point": get_cp(t),
        })
    return results


# ============================================================
# Metrics
# ============================================================

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


def per_trace_metric(trace_results, key):
    vals = []
    for tr in trace_results:
        preds = (tr["probs"] > 0.5).astype(int)
        labels = tr["labels"]
        if key == "bal_acc":
            if len(set(labels)) < 2:
                vals.append(float((preds == labels).mean()))
            else:
                vals.append(balanced_accuracy_score(labels, preds))
        elif key == "precision":
            tp = int(((preds == 1) & (labels == 1)).sum())
            fp = int(((preds == 1) & (labels == 0)).sum())
            vals.append(tp / (tp + fp) if (tp + fp) > 0 else 0.0)
        elif key == "fpr":
            cp = tr["commitment_point"]
            if cp and 0 < cp < len(preds):
                vals.append(float(preds[:cp].sum()) / cp)
            else:
                vals.append(0.0)
    return np.array(vals)


# ============================================================
# Ensemble
# ============================================================

def ensemble_trace_results(results_list):
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


# ============================================================
# Bootstrap
# ============================================================

def bootstrap_gap(results_a, results_b, metric_key, n_boot=N_BOOTSTRAP):
    id_a = {tr["trace_id"]: tr for tr in results_a}
    id_b = {tr["trace_id"]: tr for tr in results_b}
    common = sorted(set(id_a) & set(id_b))
    if len(common) < 3:
        return None, None

    a_aligned = [id_a[tid] for tid in common]
    b_aligned = [id_b[tid] for tid in common]
    va = per_trace_metric(a_aligned, metric_key)
    vb = per_trace_metric(b_aligned, metric_key)
    observed_gap = float(va.mean() - vb.mean())

    rng = np.random.default_rng(SEED)
    n = len(common)
    count = 0
    for _ in range(n_boot):
        idx = rng.choice(n, size=n, replace=True)
        boot_gap = va[idx].mean() - vb[idx].mean()
        if metric_key == "fpr":
            if boot_gap >= 0:
                count += 1
        else:
            if boot_gap <= 0:
                count += 1

    return round(observed_gap, 4), round(count / n_boot, 4)


# ============================================================
# 3rd layer selection
# ============================================================

def find_third_layer(train, val, cfg):
    offset = cfg["layer_offset"]
    n_layers = cfg["n_stored_layers"]
    window = cfg["window"]
    prec_layer = cfg["precision_layer"]
    ba_layer = cfg["ba_layer"]
    step = cfg.get("sweep_step", 1)
    exclude = {prec_layer, ba_layer}

    hint = cfg.get("fpr_layer_hint")
    if hint is not None and hint not in exclude:
        return hint

    best_fpr = 1.0
    best_layer = None
    for si in range(0, n_layers, step):
        actual = si + offset
        if actual in exclude:
            continue
        try:
            X_tr, y_tr = collect_hs_data(train, si, window)
            clf, scaler = train_probe(X_tr, y_tr)
            val_res = predict_hs_traces(clf, scaler, val, si, window)
            m = compute_metrics(val_res)
            if m["fpr"] < best_fpr:
                best_fpr = m["fpr"]
                best_layer = actual
        except Exception:
            continue

    if best_layer is None or best_layer in exclude:
        best_layer = (prec_layer + ba_layer) // 2
        while best_layer in exclude:
            best_layer += 1

    return best_layer


# ============================================================
# Per-model processing
# ============================================================

def process_model(model_name, cfg):
    print(f"\n{'='*60}")
    print(f"Model: {model_name}")
    print(f"{'='*60}")

    traces = load_traces(cfg["hs_dir"])
    print(f"  Loaded {len(traces)} traces with commitment points")

    train, val, test = split_traces(traces)
    print(f"  Split: train={len(train)}, val={len(val)}, test={len(test)}")

    offset = cfg["layer_offset"]
    window = cfg["window"]
    prec_layer = cfg["precision_layer"]
    ba_layer = cfg["ba_layer"]

    # Find 3rd layer
    print("  Finding 3rd candidate layer...")
    third_layer = find_third_layer(train, val, cfg)
    print(f"  Layers: precision=L{prec_layer}, BA=L{ba_layer}, 3rd=L{third_layer}")

    # Deduplicate layers
    layer_map = {}
    for name, lnum in [("precision", prec_layer), ("ba", ba_layer), ("third", third_layer)]:
        if lnum not in [v for v in layer_map.values()]:
            layer_map[name] = lnum
    n_ens = len(layer_map)
    print(f"  Unique layers: {n_ens} — {dict(layer_map)}")

    # Train per-layer probes and get test predictions
    layer_results = {}
    for name, lnum in layer_map.items():
        lidx = lnum - offset
        print(f"  Training L{lnum} probe (idx={lidx}, W={window})...")
        X_tr, y_tr = collect_hs_data(train, lidx, window)
        clf, scaler = train_probe(X_tr, y_tr)
        test_res = predict_hs_traces(clf, scaler, test, lidx, window)
        layer_results[name] = {"layer": lnum, "results": test_res}
        m = compute_metrics(test_res)
        print(f"    BA={m['bal_acc']:.4f}  Prec={m['precision']:.4f}  FPR={m['fpr']:.4f}")

    # Ensemble
    ens_results = ensemble_trace_results([lr["results"] for lr in layer_results.values()])
    ens_metrics = compute_metrics(ens_results)
    print(f"  Ensemble ({n_ens}L): BA={ens_metrics['bal_acc']:.4f}  "
          f"Prec={ens_metrics['precision']:.4f}  FPR={ens_metrics['fpr']:.4f}")

    # Text probe
    print("  Training text probe...")
    text_emb_dict = pickle.load(open(cfg["text_emb_pkl"], "rb"))

    X_txt_parts, y_txt_parts = [], []
    for t in train:
        tid = str(t.get("trace_id", ""))
        emb = extract_text_features(text_emb_dict, tid, window)
        if emb is None:
            continue
        labels = get_labels(t)
        n = min(len(emb), len(labels))
        X_txt_parts.append(emb[:n])
        y_txt_parts.extend(labels[:n])

    text_metrics = {"bal_acc": None, "precision": None, "fpr": None}
    text_test_results = []
    if X_txt_parts:
        X_txt = np.vstack(X_txt_parts)
        y_txt = np.array(y_txt_parts)
        txt_clf, txt_scaler = train_probe(X_txt, y_txt)
        text_test_results = predict_text_traces(txt_clf, txt_scaler, test,
                                                text_emb_dict, window)
        text_metrics = compute_metrics(text_test_results)
        print(f"  Text:  BA={text_metrics['bal_acc']:.4f}  "
              f"Prec={text_metrics['precision']:.4f}  FPR={text_metrics['fpr']:.4f}")
    else:
        print("  Text: NO MATCHING EMBEDDINGS")

    # Bootstrap tests
    print("  Bootstrap (10000 resamples)...")
    bootstrap = {}

    # Ensemble vs Text
    if text_test_results:
        for mk in ["bal_acc", "precision", "fpr"]:
            gap, pval = bootstrap_gap(ens_results, text_test_results, mk)
            bootstrap[f"ens_vs_text_{mk}"] = {"gap": gap, "p": pval}
            print(f"    ens vs text {mk}: gap={gap}, p={pval}")

    # Ensemble vs best single layer (by precision)
    best_name = max(layer_results, key=lambda k: compute_metrics(layer_results[k]["results"])["precision"])
    best_single = layer_results[best_name]["results"]
    for mk in ["bal_acc", "precision", "fpr"]:
        gap, pval = bootstrap_gap(ens_results, best_single, mk)
        bootstrap[f"ens_vs_best_single_{mk}"] = {"gap": gap, "p": pval}
        print(f"    ens vs best_single({best_name} L{layer_results[best_name]['layer']}) {mk}: gap={gap}, p={pval}")

    # Ensemble vs worst single layer (to show improvement)
    worst_name = min(layer_results, key=lambda k: compute_metrics(layer_results[k]["results"])["precision"])
    worst_single = layer_results[worst_name]["results"]
    for mk in ["bal_acc", "precision", "fpr"]:
        gap, pval = bootstrap_gap(ens_results, worst_single, mk)
        bootstrap[f"ens_vs_worst_single_{mk}"] = {"gap": gap, "p": pval}

    # Compile
    metrics_out = {}
    for name, lr in layer_results.items():
        metrics_out[f"single_{name}_L{lr['layer']}"] = compute_metrics(lr["results"])
    metrics_out["ensemble"] = ens_metrics
    metrics_out["text"] = text_metrics

    return {
        "model": model_name,
        "n_traces": {"total": len(traces), "train": len(train),
                     "val": len(val), "test": len(test)},
        "window": window,
        "layers": {name: lr["layer"] for name, lr in layer_results.items()},
        "n_ensemble_layers": n_ens,
        "metrics": metrics_out,
        "bootstrap": bootstrap,
    }


# ============================================================
# Main
# ============================================================

def main():
    t0 = time.time()
    all_results = {}

    for model_name, cfg in MODEL_CONFIGS.items():
        try:
            result = process_model(model_name, cfg)
            all_results[model_name] = result
        except Exception as e:
            import traceback
            traceback.print_exc()
            all_results[model_name] = {"error": str(e)}

    elapsed = time.time() - t0

    # Save JSON
    def json_default(x):
        if isinstance(x, (np.floating, np.integer)):
            return float(x)
        if isinstance(x, np.ndarray):
            return x.tolist()
        return None

    with open(OUT_DIR / "results.json", "w") as f:
        json.dump(all_results, f, indent=2, default=json_default)

    # Generate report
    lines = [
        "N6: Multi-Metric Layer Ensemble — Results",
        "=" * 60,
        f"Date: {time.strftime('%Y-%m-%d %H:%M')}",
        f"Total runtime: {elapsed:.0f}s",
        "",
    ]

    for model_name, res in all_results.items():
        if "error" in res:
            lines.append(f"{model_name}: ERROR — {res['error']}\n")
            continue

        lines.append(f"{model_name}  (W={res['window']}, test={res['n_traces']['test']}, "
                     f"ensemble={res['n_ensemble_layers']}L)")
        lines.append(f"  Layers: {res['layers']}")
        lines.append(f"  {'Method':<35} {'BA':>7} {'Prec':>7} {'FPR':>7}")
        lines.append(f"  {'-'*56}")
        for mk, mv in res["metrics"].items():
            if mv.get("bal_acc") is not None:
                lines.append(f"  {mk:<35} {mv['bal_acc']:>7.4f} {mv['precision']:>7.4f} {mv['fpr']:>7.4f}")
        lines.append("")

        if res.get("bootstrap"):
            lines.append("  Bootstrap (n=10000):")
            for bk, bv in res["bootstrap"].items():
                sig = "*" if bv.get("p") is not None and bv["p"] < 0.05 else ""
                lines.append(f"    {bk}: gap={bv['gap']}, p={bv['p']}{sig}")
            lines.append("")

    # Summary table
    lines.append("=" * 60)
    lines.append("SUMMARY: Does ensemble mitigate layer sensitivity?")
    lines.append(f"{'Model':<10} {'Best-Single Prec':>16} {'Ensemble Prec':>14} {'Delta':>7} {'Text Prec':>10} {'Ens-Text Gap':>12}")
    lines.append("-" * 70)
    for model_name, res in all_results.items():
        if "error" in res:
            continue
        m = res["metrics"]
        single_precs = [v["precision"] for k, v in m.items()
                        if k.startswith("single_") and v.get("precision") is not None]
        best_single = max(single_precs) if single_precs else 0
        worst_single = min(single_precs) if single_precs else 0
        ens_prec = m["ensemble"]["precision"]
        txt_prec = m["text"]["precision"] if m["text"]["precision"] is not None else 0
        delta = ens_prec - best_single
        gap = ens_prec - txt_prec
        lines.append(f"{model_name:<10} {best_single:>16.4f} {ens_prec:>14.4f} {delta:>+7.4f} {txt_prec:>10.4f} {gap:>+12.4f}")

    lines.append("")
    lines.append("Sensitivity reduction (ensemble precision range vs single-layer range):")
    for model_name, res in all_results.items():
        if "error" in res:
            continue
        m = res["metrics"]
        single_precs = [v["precision"] for k, v in m.items()
                        if k.startswith("single_") and v.get("precision") is not None]
        if len(single_precs) >= 2:
            single_range = max(single_precs) - min(single_precs)
            ens_prec = m["ensemble"]["precision"]
            lines.append(f"  {model_name}: single-layer range={single_range:.4f}, "
                         f"ensemble={ens_prec:.4f} "
                         f"(within {abs(ens_prec - np.mean(single_precs)):.4f} of mean)")

    report = "\n".join(lines)
    with open(OUT_DIR / "report.txt", "w") as f:
        f.write(report)

    print(f"\n{'='*60}")
    print(report)
    print(f"\nResults: {OUT_DIR / 'results.json'}")
    print(f"Report:  {OUT_DIR / 'report.txt'}")


if __name__ == "__main__":
    main()
