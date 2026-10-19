"""SF3: Nonlinear (Quadratic) Position Residualization.

Compares linear [t/T] vs quadratic [t/T, (t/T)^2] residualization
of HS and Text features across 4 models. For R19 review revision.
"""

import os, sys, json, time, warnings, pickle
os.environ["TOKENIZERS_PARALLELISM"] = "false"
warnings.filterwarnings("ignore")

import numpy as np
import torch
from pathlib import Path
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.decomposition import PCA
from sklearn.metrics import balanced_accuracy_score

PROJECT = Path("DATA_DIR")
ARTIFACTS = PROJECT / "artifacts"
OUT_DIR = ARTIFACTS / "sf3_quadratic_residual"
OUT_DIR.mkdir(parents=True, exist_ok=True)

SEED = 42
N_PCA = 50
N_BOOTSTRAP = 10000

MODEL_CONFIGS = {
    "R1-8B": {
        "hs_dir": ARTIFACTS / "hidden_states",
        "layer_idx": 2,
        "hidden_dim": 4096,
        "window": 3,
        "text_emb_pkl": ARTIFACTS / "r12_5seed_hb" / "r1_8b_text_emb.pkl",
    },
    "OT-7B": {
        "hs_dir": ARTIFACTS / "hidden_states_ot7b",
        "layer_idx": 16,
        "hidden_dim": 3584,
        "window": 3,
        "text_emb_pkl": ARTIFACTS / "ot7b_text_embeddings.pkl",
    },
    "R1-32B": {
        "hs_dir": ARTIFACTS / "hidden_states_r1_32b",
        "layer_idx": 63,
        "hidden_dim": 5120,
        "window": 1,
        "text_emb_pkl": ARTIFACTS / "r12_5seed_hb" / "r1_32b_text_emb.pkl",
    },
    "QwQ-32B": {
        "hs_dir": ARTIFACTS / "hidden_states_qwq_32b",
        "layer_idx": 63,
        "hidden_dim": 5120,
        "window": 5,
        "text_emb_pkl": ARTIFACTS / "r12_5seed_hb" / "qwq_text_emb.pkl",
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
    return sl.tolist() if isinstance(sl, torch.Tensor) else list(sl)


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
    if window == 1:
        return feats
    n, dim = feats.shape
    half_w = window // 2
    padded = np.zeros((n + window - 1, dim), dtype=np.float32)
    padded[half_w:half_w + n] = feats
    return np.array([padded[i:i + window].flatten() for i in range(n)])


def residualize_linear(features):
    T = len(features)
    t_norm = np.arange(T, dtype=np.float64) / T
    X_reg = t_norm.reshape(-1, 1)
    reg = LinearRegression().fit(X_reg, features)
    return (features - reg.predict(X_reg)).astype(np.float32)


def residualize_quadratic(features):
    T = len(features)
    t_norm = np.arange(T, dtype=np.float64) / T
    X_reg = np.column_stack([t_norm, t_norm ** 2])
    reg = LinearRegression().fit(X_reg, features)
    return (features - reg.predict(X_reg)).astype(np.float32)


def extract_hs(trace, layer_idx):
    hs = trace["hidden_states"][:, layer_idx, :].float().numpy()
    labels = np.array(get_labels(trace))
    n = min(hs.shape[0], len(labels))
    return hs[:n].astype(np.float32), labels[:n]


def per_trace_ba(preds, labels):
    preds, labels = np.asarray(preds), np.asarray(labels)
    tp = ((preds == 1) & (labels == 1)).sum()
    fp = ((preds == 1) & (labels == 0)).sum()
    tn = ((preds == 0) & (labels == 0)).sum()
    fn = ((preds == 0) & (labels == 1)).sum()
    tpr = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    tnr = tn / (tn + fp) if (tn + fp) > 0 else 0.0
    return (tpr + tnr) / 2


def build_hs_features(traces, layer_idx, window, resid_fn):
    X_list, y_list = [], []
    for t in traces:
        hs, labels = extract_hs(t, layer_idx)
        feat = apply_window(resid_fn(hs), window)
        X_list.append(feat)
        y_list.append(labels)
    return X_list, y_list


def build_text_features(traces, text_emb_dict, window, resid_fn):
    X_list, y_list = [], []
    for t in traces:
        tid = t["trace_id"]
        emb = text_emb_dict.get(tid)
        if emb is None:
            continue
        labels = np.array(get_labels(t))
        emb = np.array(emb, dtype=np.float32)
        n = min(len(emb), len(labels))
        emb, labels = emb[:n], labels[:n]
        feat = apply_window(resid_fn(emb), window)
        X_list.append(feat)
        y_list.append(labels)
    return X_list, y_list


def train_probe(X_train_list, y_train_list, X_test_list, y_test_list):
    X_tr = np.concatenate(X_train_list)
    y_tr = np.concatenate(y_train_list)
    n_comp = min(N_PCA, X_tr.shape[0], X_tr.shape[1])

    if X_tr.shape[1] > 1:
        pca = PCA(n_components=n_comp, random_state=SEED)
        X_tr_pca = pca.fit_transform(X_tr)
    else:
        pca = None
        X_tr_pca = X_tr

    clf = LogisticRegression(
        C=1.0, class_weight="balanced", solver="lbfgs",
        max_iter=2000, random_state=SEED
    )
    clf.fit(X_tr_pca, y_tr)

    per_trace_bas = []
    all_preds, all_labels = [], []
    for X_te, y_te in zip(X_test_list, y_test_list):
        X_te_pca = pca.transform(X_te) if pca is not None else X_te
        preds = clf.predict(X_te_pca)
        per_trace_bas.append(float(per_trace_ba(preds, y_te)))
        all_preds.append(preds)
        all_labels.append(y_te)

    pooled_ba = float(balanced_accuracy_score(
        np.concatenate(all_labels), np.concatenate(all_preds)
    ))
    return pooled_ba, np.array(per_trace_bas)


def paired_permutation_test(ba_hs, ba_text, n_perm=N_BOOTSTRAP, seed=SEED):
    """One-sided paired permutation test. H0: mean(HS_BA) <= mean(Text_BA)."""
    gaps = ba_hs - ba_text
    observed = float(gaps.mean())
    rng = np.random.default_rng(seed + 77)
    count = 0
    for _ in range(n_perm):
        signs = rng.choice([-1, 1], size=len(gaps))
        if (signs * gaps).mean() >= observed:
            count += 1
    p_value = count / n_perm
    return observed, p_value


def holm_bonferroni(p_values, alpha=0.05):
    """Holm-Bonferroni correction. Returns dict of model -> {adjusted_p, reject}."""
    n = len(p_values)
    items = sorted(p_values.items(), key=lambda x: x[1])
    results = {}
    for rank, (model, p) in enumerate(items):
        adjusted_alpha = alpha / (n - rank)
        reject = p <= adjusted_alpha
        adjusted_p = min(p * (n - rank), 1.0)
        results[model] = {"raw_p": p, "adjusted_p": round(adjusted_p, 6), "reject": reject}
    return results


def run_model(model_name, cfg, text_emb_dict):
    print(f"\n{'='*60}")
    print(f"{model_name} (L{cfg['layer_idx'] if model_name not in ['R1-8B'] else 14}, W={cfg['window']})")
    print(f"{'='*60}")

    traces = load_traces(cfg["hs_dir"])
    # Filter to traces with text embeddings
    traces = [t for t in traces if t["trace_id"] in text_emb_dict]
    print(f"Traces with both HS + text: {len(traces)}")

    train, val, test = split_traces(traces)
    train_val = train + val
    print(f"Split: train+val={len(train_val)}, test={len(test)}")

    layer_idx = cfg["layer_idx"]
    window = cfg["window"]
    results = {}

    for method_name, resid_fn in [("linear", residualize_linear), ("quadratic", residualize_quadratic)]:
        # HS features
        X_tr_hs, y_tr_hs = build_hs_features(train_val, layer_idx, window, resid_fn)
        X_te_hs, y_te_hs = build_hs_features(test, layer_idx, window, resid_fn)
        hs_pooled, hs_per_trace = train_probe(X_tr_hs, y_tr_hs, X_te_hs, y_te_hs)

        # Text features
        X_tr_txt, y_tr_txt = build_text_features(train_val, text_emb_dict, window, resid_fn)
        X_te_txt, y_te_txt = build_text_features(test, text_emb_dict, window, resid_fn)
        txt_pooled, txt_per_trace = train_probe(X_tr_txt, y_tr_txt, X_te_txt, y_te_txt)

        # Ensure same number of test traces for paired comparison
        n_test = min(len(hs_per_trace), len(txt_per_trace))
        hs_ba = hs_per_trace[:n_test]
        txt_ba = txt_per_trace[:n_test]

        gap, p_value = paired_permutation_test(hs_ba, txt_ba)

        hs_mean = float(hs_ba.mean())
        txt_mean = float(txt_ba.mean())

        results[method_name] = {
            "hs_ba_pooled": round(hs_pooled, 4),
            "text_ba_pooled": round(txt_pooled, 4),
            "hs_ba_mean_per_trace": round(hs_mean, 4),
            "text_ba_mean_per_trace": round(txt_mean, 4),
            "ba_gap": round(gap, 4),
            "ba_gap_pp": round(gap * 100, 1),
            "p_value": round(p_value, 6),
            "n_test_traces": n_test,
            "per_trace_hs_ba": [round(float(b), 4) for b in hs_ba],
            "per_trace_text_ba": [round(float(b), 4) for b in txt_ba],
        }
        print(f"  {method_name}: HS={hs_mean:.4f}, Text={txt_mean:.4f}, "
              f"gap={gap*100:.1f}pp, p={p_value:.4f}")

    return results


def main():
    t_start = time.time()

    all_results = {}

    for model_name, cfg in MODEL_CONFIGS.items():
        print(f"\nLoading text embeddings for {model_name}...")
        text_emb_dict = pickle.load(open(cfg["text_emb_pkl"], "rb"))
        print(f"  {len(text_emb_dict)} text traces loaded")

        r = run_model(model_name, cfg, text_emb_dict)
        all_results[model_name] = r

    # Holm-Bonferroni for linear
    linear_pvals = {m: r["linear"]["p_value"] for m, r in all_results.items()}
    hb_linear = holm_bonferroni(linear_pvals)
    for m in all_results:
        all_results[m]["linear"]["hb_reject"] = hb_linear[m]["reject"]
        all_results[m]["linear"]["hb_adjusted_p"] = hb_linear[m]["adjusted_p"]

    # Holm-Bonferroni for quadratic
    quad_pvals = {m: r["quadratic"]["p_value"] for m, r in all_results.items()}
    hb_quad = holm_bonferroni(quad_pvals)
    for m in all_results:
        all_results[m]["quadratic"]["hb_reject"] = hb_quad[m]["reject"]
        all_results[m]["quadratic"]["hb_adjusted_p"] = hb_quad[m]["adjusted_p"]

    elapsed = time.time() - t_start

    # Save results.json
    out = {
        "experiment": "sf3_quadratic_residual",
        "seed": SEED,
        "n_pca": N_PCA,
        "n_bootstrap": N_BOOTSTRAP,
        "lr_params": {"C": 1.0, "class_weight": "balanced", "max_iter": 2000},
        "split": "60/20/20 trace-level",
        "models": all_results,
        "holm_bonferroni_linear": hb_linear,
        "holm_bonferroni_quadratic": hb_quad,
        "elapsed_seconds": round(elapsed, 1),
    }
    with open(OUT_DIR / "results.json", "w") as f:
        json.dump(out, f, indent=2)

    # Save comparison_table.csv
    import csv
    with open(OUT_DIR / "comparison_table.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Model", "Method", "HS_BA_mean", "Text_BA_mean", "HS_BA_pooled", "Text_BA_pooled",
                    "Gap_pp", "p_value", "HB_adjusted_p", "HB_reject"])
        for m in MODEL_CONFIGS:
            for method in ["linear", "quadratic"]:
                r = all_results[m][method]
                w.writerow([
                    m, method,
                    r["hs_ba_mean_per_trace"], r["text_ba_mean_per_trace"],
                    r["hs_ba_pooled"], r["text_ba_pooled"],
                    r["ba_gap_pp"], r["p_value"],
                    r["hb_adjusted_p"], r["hb_reject"],
                ])

    # Save report.txt
    lines = [
        "SF3: Nonlinear (Quadratic) Position Residualization",
        "=" * 55,
        f"Seed: {SEED}, PCA: {N_PCA}, Bootstrap: {N_BOOTSTRAP}",
        f"Probe: LogReg(C=1.0, balanced, max_iter=2000)",
        f"Split: 60/20/20 trace-level, train+val for training",
        "",
        "Per-trace mean balanced accuracy (gap = mean per-trace difference):",
        "",
        f"{'Model':<10} {'Method':<12} {'HS BA':>7} {'Txt BA':>7} {'Gap':>7} {'p':>8} {'HB p':>8} {'Pass':>5}",
        "-" * 67,
    ]
    for m in MODEL_CONFIGS:
        for method in ["linear", "quadratic"]:
            r = all_results[m][method]
            lines.append(
                f"{m:<10} {method:<12} {r['hs_ba_mean_per_trace']:>7.4f} {r['text_ba_mean_per_trace']:>7.4f} "
                f"{r['ba_gap_pp']:>6.1f}pp {r['p_value']:>8.4f} {r['hb_adjusted_p']:>8.4f} "
                f"{'Y' if r['hb_reject'] else 'N':>5}"
            )
        lines.append("")

    lines.append("")
    lines.append("Key: HS/Txt BA = mean of per-trace balanced accuracies")
    lines.append("     Gap = mean(HS_BA_i - Txt_BA_i), positive = HS advantage")
    lines.append("     p = paired permutation test (10K, one-sided, H0: HS <= Text)")
    lines.append("     HB p = Holm-Bonferroni adjusted (across 4 models, alpha=0.05)")
    lines.append(f"\nElapsed: {elapsed:.0f}s")

    with open(OUT_DIR / "report.txt", "w") as f:
        f.write("\n".join(lines))

    print(f"\n{'='*65}")
    print("\n".join(lines))
    print(f"\nSaved to {OUT_DIR}")


if __name__ == "__main__":
    main()
