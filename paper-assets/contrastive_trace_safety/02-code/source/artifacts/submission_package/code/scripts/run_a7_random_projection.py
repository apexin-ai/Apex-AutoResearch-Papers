"""A7: Random Gaussian projection to 384d baseline.

Tests whether HS advantage over text depends on PCA's variance-preserving
property by replacing PCA with random Gaussian projection.
"""

import os, sys, json, glob, warnings, time
os.environ["TOKENIZERS_PARALLELISM"] = "false"
# os.environ["HF_DATASETS_OFFLINE"] = "1"  # uncomment for offline mode
# os.environ["HF_HUB_OFFLINE"] = "1"  # uncomment for offline mode
# os.environ["HF_ENDPOINT"] = "..."  # set HF mirror if needed
warnings.filterwarnings("ignore")

import numpy as np
import torch
from pathlib import Path
from collections import defaultdict
from sklearn.linear_model import LogisticRegression
from sklearn.random_projection import GaussianRandomProjection
from sklearn.metrics import (
    balanced_accuracy_score, precision_score,
    roc_auc_score, confusion_matrix
)
from sentence_transformers import SentenceTransformer

PROJECT = Path("DATA_DIR")
OUT_DIR = PROJECT / "artifacts" / "r14_a7_random_projection"
OUT_DIR.mkdir(parents=True, exist_ok=True)

SEED = 42
RP_SEEDS = [42, 123, 456]
N_COMPONENTS = 384
N_BOOTSTRAP = 1000

MODEL_CONFIGS = {
    "R1-8B": {
        "hs_dir": PROJECT / "artifacts" / "hidden_states",
        "layer_idx": 2,
        "hidden_dim": 4096,
        "window": 15,
        "hf_model_name": "r1-8b",
    },
    "OT-7B": {
        "hs_dir": PROJECT / "artifacts" / "hidden_states_ot7b",
        "layer_idx": 16,
        "hidden_dim": 3584,
        "window": 3,
        "hf_model_name": "ot-7b",
    },
    "R1-32B": {
        "hs_dir": PROJECT / "artifacts" / "hidden_states_r1_32b",
        "layer_idx": 63,
        "hidden_dim": 5120,
        "window": 1,
        "hf_model_name": "r1-32b",
    },
    "QwQ-32B": {
        "hs_dir": PROJECT / "artifacts" / "hidden_states_qwq_32b",
        "layer_idx": 60,
        "hidden_dim": 5120,
        "window": 5,
        "hf_model_name": "QwQ",
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
        sl = d["step_labels"]
        if isinstance(sl, torch.Tensor):
            sl = sl.tolist()
        else:
            sl = list(sl)
        n_steps = len(sl)
        sentences = sentences_map[trace_id]
        if len(sentences) < n_steps:
            continue
        hs = d["hidden_states"][:n_steps, layer_idx, :].float().numpy().astype(np.float32)
        traces.append({
            "trace_id": trace_id,
            "hidden_states": hs,
            "step_labels": sl,
            "sentences": sentences[:n_steps],
            "commitment_point": int(d["commitment_point"]),
        })
    return traces


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


def apply_window(feats, window):
    if window <= 1:
        return feats
    n, dim = feats.shape
    half_w = window // 2
    padded = np.zeros((n + window - 1, dim), dtype=np.float32)
    padded[half_w:half_w + n] = feats
    return np.array([padded[i:i + window].flatten() for i in range(n)])


def build_hs_features(traces, window):
    X_list, y_list = [], []
    for t in traces:
        hs = t["hidden_states"]
        labels = np.array(t["step_labels"])
        n = min(len(hs), len(labels))
        feat = apply_window(hs[:n], window)
        X_list.append(feat)
        y_list.append(labels[:n])
    return np.concatenate(X_list), np.concatenate(y_list)


def build_text_features(traces, st_model):
    X_list, y_list = [], []
    for t in traces:
        embs = st_model.encode(t["sentences"], batch_size=64, show_progress_bar=False)
        labels = np.array(t["step_labels"])
        n = min(len(embs), len(labels))
        X_list.append(embs[:n].astype(np.float32))
        y_list.append(labels[:n])
    return np.concatenate(X_list), np.concatenate(y_list)


def compute_metrics(y_true, y_pred, y_prob):
    prec = precision_score(y_true, y_pred, zero_division=0)
    ba = balanced_accuracy_score(y_true, y_pred)
    tn, fp, fn, tp = confusion_matrix(y_true, y_pred, labels=[0, 1]).ravel()
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0.0
    try:
        auroc = roc_auc_score(y_true, y_prob)
    except ValueError:
        auroc = float("nan")
    return {"precision": prec, "bal_acc": ba, "fpr": fpr, "auroc": auroc}


def bootstrap_compare(y_true, y_pred_a, y_prob_a, y_pred_b, y_prob_b, n_boot=N_BOOTSTRAP):
    rng = np.random.default_rng(SEED)
    n = len(y_true)
    delta_prec, delta_ba, delta_fpr, delta_auroc = [], [], [], []
    for _ in range(n_boot):
        idx = rng.integers(0, n, size=n)
        yt = y_true[idx]
        if len(np.unique(yt)) < 2:
            continue
        ma = compute_metrics(yt, y_pred_a[idx], y_prob_a[idx])
        mb = compute_metrics(yt, y_pred_b[idx], y_prob_b[idx])
        delta_prec.append(ma["precision"] - mb["precision"])
        delta_ba.append(ma["bal_acc"] - mb["bal_acc"])
        delta_fpr.append(ma["fpr"] - mb["fpr"])
        delta_auroc.append(ma["auroc"] - mb["auroc"])

    def ci(arr):
        arr = np.array(arr)
        return {
            "mean": float(np.mean(arr)),
            "ci_lo": float(np.percentile(arr, 2.5)),
            "ci_hi": float(np.percentile(arr, 97.5)),
            "p_positive": float(np.mean(arr > 0)),
        }
    return {
        "delta_prec": ci(delta_prec),
        "delta_ba": ci(delta_ba),
        "delta_fpr": ci(delta_fpr),
        "delta_auroc": ci(delta_auroc),
    }


def run_model(model_name, cfg, st_model):
    print(f"\n{'='*60}")
    print(f"Model: {model_name}")
    print(f"{'='*60}")
    t0 = time.time()

    print("Loading sentences from HF...")
    sentences_map = load_sentences_from_hf(cfg["hf_model_name"])
    print(f"  {len(sentences_map)} traces with sentences")

    print("Loading hidden states...")
    traces = load_traces(cfg["hs_dir"], sentences_map, cfg["layer_idx"])
    print(f"  {len(traces)} traces loaded")

    train, val, test = split_traces(traces)
    print(f"  Split: train={len(train)}, val={len(val)}, test={len(test)}")

    window = cfg["window"]
    orig_dim = cfg["hidden_dim"] * window
    print(f"  Window={window}, original_dim={orig_dim}")

    X_train_hs, y_train_hs = build_hs_features(train, window)
    X_val_hs, y_val_hs = build_hs_features(val, window)
    X_test_hs, y_test_hs = build_hs_features(test, window)
    print(f"  HS shapes: train={X_train_hs.shape}, val={X_val_hs.shape}, test={X_test_hs.shape}")

    print("Building text features...")
    X_train_txt, y_train_txt = build_text_features(train, st_model)
    X_val_txt, y_val_txt = build_text_features(val, st_model)
    X_test_txt, y_test_txt = build_text_features(test, st_model)

    print("Training text LR...")
    clf_txt = LogisticRegression(
        solver="lbfgs", C=1.0, class_weight="balanced",
        max_iter=2000, random_state=SEED
    )
    clf_txt.fit(X_train_txt, y_train_txt)
    txt_pred = clf_txt.predict(X_test_txt)
    txt_prob = clf_txt.predict_proba(X_test_txt)[:, 1]
    txt_metrics = compute_metrics(y_test_txt, txt_pred, txt_prob)
    print(f"  Text: prec={txt_metrics['precision']:.4f}, ba={txt_metrics['bal_acc']:.4f}, "
          f"fpr={txt_metrics['fpr']:.4f}, auroc={txt_metrics['auroc']:.4f}")

    rp_results = []
    for rp_seed in RP_SEEDS:
        print(f"  RP seed={rp_seed}...")
        rp = GaussianRandomProjection(n_components=N_COMPONENTS, random_state=rp_seed)
        X_train_rp = rp.fit_transform(X_train_hs)
        X_val_rp = rp.transform(X_val_hs)
        X_test_rp = rp.transform(X_test_hs)

        clf_rp = LogisticRegression(
            solver="lbfgs", C=1.0, class_weight="balanced",
            max_iter=2000, random_state=SEED
        )
        clf_rp.fit(X_train_rp, y_train_hs)
        rp_pred = clf_rp.predict(X_test_rp)
        rp_prob = clf_rp.predict_proba(X_test_rp)[:, 1]
        rp_met = compute_metrics(y_test_hs, rp_pred, rp_prob)
        print(f"    prec={rp_met['precision']:.4f}, ba={rp_met['bal_acc']:.4f}, "
              f"fpr={rp_met['fpr']:.4f}, auroc={rp_met['auroc']:.4f}")
        rp_results.append({"seed": rp_seed, "metrics": rp_met, "pred": rp_pred, "prob": rp_prob})

    rp_mean = {}
    rp_std = {}
    for k in ["precision", "bal_acc", "fpr", "auroc"]:
        vals = [r["metrics"][k] for r in rp_results]
        rp_mean[k] = float(np.mean(vals))
        rp_std[k] = float(np.std(vals))

    print(f"  RP mean: prec={rp_mean['precision']:.4f}+-{rp_std['precision']:.4f}, "
          f"ba={rp_mean['bal_acc']:.4f}+-{rp_std['bal_acc']:.4f}")

    best_rp = max(rp_results, key=lambda r: r["metrics"]["bal_acc"])
    boot = bootstrap_compare(
        y_test_hs, best_rp["pred"], best_rp["prob"],
        txt_pred, txt_prob
    )

    elapsed = time.time() - t0
    print(f"  Done in {elapsed:.1f}s")

    return {
        "model": model_name,
        "n_traces": len(traces),
        "split": {"train": len(train), "val": len(val), "test": len(test)},
        "window": window,
        "orig_dim": orig_dim,
        "text_metrics": txt_metrics,
        "rp_mean": rp_mean,
        "rp_std": rp_std,
        "rp_per_seed": [{"seed": r["seed"], "metrics": r["metrics"]} for r in rp_results],
        "bootstrap_rp_vs_text": boot,
    }


def main():
    print("Loading all-MiniLM-L6-v2...")
    st_model = SentenceTransformer("all-MiniLM-L6-v2")

    all_results = {}
    for model_name, cfg in MODEL_CONFIGS.items():
        if not cfg["hs_dir"].exists():
            print(f"Skipping {model_name}: {cfg['hs_dir']} not found")
            continue
        result = run_model(model_name, cfg, st_model)
        all_results[model_name] = result

    with open(OUT_DIR / "a7_results.json", "w") as f:
        json.dump(all_results, f, indent=2)

    print("\n" + "=" * 80)
    print("SUMMARY TABLE")
    print("=" * 80)
    header = (
        f"{'Model':<10} | {'RP-384 Prec':>14} | {'Txt Prec':>8} | {'dPrec':>8} | "
        f"{'RP-384 BA':>12} | {'Txt BA':>8} | {'dBA':>8} | "
        f"{'RP-384 FPR':>12} | {'Txt FPR':>8} | {'dFPR':>8} | "
        f"{'RP-384 AUC':>12} | {'Txt AUC':>8}"
    )
    print(header)
    print("-" * len(header))

    for model_name, r in all_results.items():
        rp = r["rp_mean"]
        rs = r["rp_std"]
        tx = r["text_metrics"]
        print(
            f"{model_name:<10} | "
            f"{rp['precision']:.3f}+-{rs['precision']:.3f} | "
            f"{tx['precision']:.3f}   | "
            f"{rp['precision'] - tx['precision']:+.3f}  | "
            f"{rp['bal_acc']:.3f}+-{rs['bal_acc']:.3f} | "
            f"{tx['bal_acc']:.3f}   | "
            f"{rp['bal_acc'] - tx['bal_acc']:+.3f}  | "
            f"{rp['fpr']:.3f}+-{rs['fpr']:.3f} | "
            f"{tx['fpr']:.3f}   | "
            f"{rp['fpr'] - tx['fpr']:+.3f}  | "
            f"{rp['auroc']:.3f}+-{rs['auroc']:.3f} | "
            f"{tx['auroc']:.3f}"
        )

    print("\nBootstrap RP-vs-Text (best RP seed):")
    for model_name, r in all_results.items():
        b = r["bootstrap_rp_vs_text"]
        print(f"  {model_name}:")
        for k in ["delta_prec", "delta_ba", "delta_fpr", "delta_auroc"]:
            d = b[k]
            print(f"    {k}: {d['mean']:+.4f} [{d['ci_lo']:+.4f}, {d['ci_hi']:+.4f}] p(>0)={d['p_positive']:.3f}")

    print(f"\nResults saved to {OUT_DIR}/a7_results.json")


if __name__ == "__main__":
    main()
