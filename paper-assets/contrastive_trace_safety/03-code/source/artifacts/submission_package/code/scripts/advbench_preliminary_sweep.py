"""AdvBench preliminary layer sweep with pseudo-CP labels.

Runs 5-metric layer sweep across 25 layers × 4 windows using
heuristic CP annotations from pseudo_cp_annotations.json.
Bootstrap 1000 for CI on best layers.
"""
import os, json, time, gc, warnings
os.environ["TOKENIZERS_PARALLELISM"] = "false"
warnings.filterwarnings("ignore")

import numpy as np
import torch
from pathlib import Path
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score, precision_score
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

SEED = 42
N_LAYERS = 25
HIDDEN_DIM = 4096
WINDOWS = [1, 3, 5, 15]
MAX_ITER = 2000
K_CROSSING = 5
CROSSING_THRESHOLD = 0.5
PCA_DIM = 100
N_BOOTSTRAP = 1000

BASE = Path("DATA_DIR")
HS_DIR = BASE / "artifacts/hidden_states_advbench"
CP_PATH = BASE / "artifacts/advbench_preliminary/pseudo_cp_annotations.json"
OUTPUT_DIR = BASE / "artifacts/advbench_preliminary/pseudo_cp_layer_sweep"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def ts():
    return time.strftime("[%H:%M:%S]")


def load_traces():
    with open(CP_PATH) as f:
        cp_data = json.load(f)
    annotations = cp_data["annotations"]
    print(f"  {len(annotations)} annotated traces in pseudo_cp_annotations.json", flush=True)

    traces = []
    for tid, ann in sorted(annotations.items()):
        pt_path = HS_DIR / f"{tid}.pt"
        if not pt_path.exists():
            continue
        d = torch.load(pt_path, map_location="cpu", weights_only=False)
        hs = d["hidden_states"].float().numpy()
        cp = ann["commitment_point"]
        T = min(hs.shape[0], ann["total_steps"])
        if cp < 1 or cp >= T:
            continue
        step_labels = [0 if i < cp else 1 for i in range(T)]
        traces.append(dict(
            trace_id=tid,
            hs=hs[:T],
            cp=cp,
            step_labels=step_labels,
            num_steps=T,
        ))
    return traces


def split_60_20_20(traces, seed=SEED):
    rng = np.random.default_rng(seed)
    n = len(traces)
    idx = rng.permutation(n)
    n_train = int(n * 0.6)
    n_val = int(n * 0.2)
    train = [traces[i] for i in idx[:n_train]]
    val = [traces[i] for i in idx[n_train:n_train + n_val]]
    test = [traces[i] for i in idx[n_train + n_val:]]
    return train, val, test


def build_windowed_features(traces, layer_idx, window):
    X_list = []
    n_per_trace = []
    for t in traces:
        hs_layer = t["hs"][:, layer_idx, :]
        T = hs_layer.shape[0]
        padded = np.concatenate([np.repeat(hs_layer[:1], window - 1, axis=0), hs_layer], axis=0)
        windows = np.empty((T, window * HIDDEN_DIM), dtype=hs_layer.dtype)
        for w_i in range(window):
            windows[:, w_i * HIDDEN_DIM:(w_i + 1) * HIDDEN_DIM] = padded[w_i:w_i + T]
        X_list.append(windows)
        n_per_trace.append(T)
    return np.vstack(X_list), n_per_trace


def get_labels(traces):
    y = []
    for t in traces:
        y.extend(t["step_labels"])
    return np.array(y, dtype=np.int32)


def first_crossing(probs, threshold=CROSSING_THRESHOLD, k=K_CROSSING):
    for i in range(len(probs) - k + 1):
        if all(p > threshold for p in probs[i:i + k]):
            return i
    return None


def evaluate_layer_window(X_train, y_train, X_test, y_test, test_traces, n_test):
    if len(np.unique(y_train)) < 2:
        return None

    scaler = StandardScaler()
    X_tr = scaler.fit_transform(X_train)
    X_te = scaler.transform(X_test)

    clf = LogisticRegression(
        solver="lbfgs", C=1.0, class_weight="balanced",
        max_iter=MAX_ITER, random_state=SEED,
    )
    clf.fit(X_tr, y_train)

    y_pred = clf.predict(X_te)
    y_proba = clf.predict_proba(X_te)[:, 1]

    ba = balanced_accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, zero_division=0)

    fprs_list = []
    n_crossings = 0
    offset = 0
    for i, t in enumerate(test_traces):
        T = n_test[i]
        cp = t["cp"]
        preds_t = y_pred[offset:offset + T]
        probs_t = y_proba[offset:offset + T]

        if cp > 0:
            pre_cp_preds = preds_t[:min(T, cp)]
            if len(pre_cp_preds) > 0:
                fprs_list.append(float(pre_cp_preds.mean()))

        fc = first_crossing(probs_t.tolist())
        if fc is not None and fc < cp:
            n_crossings += 1
        offset += T

    pre_cp_fpr = float(np.mean(fprs_list)) if fprs_list else 0.0
    crossing_rate = n_crossings / len(test_traces) if len(test_traces) > 0 else 0.0

    return {
        "bal_acc": round(ba, 4),
        "precision": round(prec, 4),
        "fpr": round(pre_cp_fpr, 4),
        "crossing_rate": round(crossing_rate, 4),
        "composite": round(ba * crossing_rate, 4),
    }


def bootstrap_ci(traces_pool, layer_idx, window, n_boot=N_BOOTSTRAP):
    """Bootstrap CI by resampling traces. PCA fitted once on all data."""
    rng = np.random.default_rng(SEED + 999)
    n = len(traces_pool)
    metrics_boot = {m: [] for m in ["bal_acc", "precision", "fpr", "crossing_rate", "composite"]}

    X_all, n_per_trace = build_windowed_features(traces_pool, layer_idx, window)
    pca_dim = min(PCA_DIM, X_all.shape[1], X_all.shape[0])
    pca = PCA(n_components=pca_dim, random_state=SEED)
    X_all_pca = pca.fit_transform(X_all)
    del X_all

    per_trace_X = []
    offset = 0
    for nt in n_per_trace:
        per_trace_X.append(X_all_pca[offset:offset + nt])
        offset += nt
    del X_all_pca

    for b in range(n_boot):
        idx = rng.choice(n, size=n, replace=True)
        perm = rng.permutation(len(idx))
        n_train = int(len(idx) * 0.6)
        n_val = int(len(idx) * 0.2)
        tr_idx = idx[perm[:n_train + n_val]]
        te_idx = idx[perm[n_train + n_val:]]

        X_train_pca = np.vstack([per_trace_X[i] for i in tr_idx])
        X_test_pca = np.vstack([per_trace_X[i] for i in te_idx])
        y_train = np.concatenate([np.array(traces_pool[i]["step_labels"]) for i in tr_idx])
        y_test_arr = np.concatenate([np.array(traces_pool[i]["step_labels"]) for i in te_idx])
        test_traces = [traces_pool[i] for i in te_idx]
        n_test = [per_trace_X[i].shape[0] for i in te_idx]

        result = evaluate_layer_window(X_train_pca, y_train, X_test_pca, y_test_arr, test_traces, n_test)
        if result is None:
            continue
        for m in metrics_boot:
            metrics_boot[m].append(result[m])

        if (b + 1) % 200 == 0:
            print(f" [{b+1}/{n_boot}]", end="", flush=True)

    ci = {}
    for m, vals in metrics_boot.items():
        if len(vals) < 10:
            ci[m] = {"mean": None, "ci_lo": None, "ci_hi": None, "n_valid": len(vals)}
            continue
        ci[m] = {
            "mean": round(float(np.mean(vals)), 4),
            "ci_lo": round(float(np.percentile(vals, 2.5)), 4),
            "ci_hi": round(float(np.percentile(vals, 97.5)), 4),
            "n_valid": len(vals),
        }
    return ci


def main():
    t_start = time.time()

    # --- Dry run flag ---
    dry_run = os.environ.get("DRY_RUN", "0") == "1"
    if dry_run:
        print(f"{ts()} *** DRY RUN: 1 layer, 1 window ***", flush=True)
        layers_to_sweep = [12]
        windows_to_sweep = [3]
    else:
        layers_to_sweep = list(range(N_LAYERS))
        windows_to_sweep = WINDOWS

    print(f"{ts()} Loading traces...", flush=True)
    traces = load_traces()
    print(f"  Loaded {len(traces)} traces with pseudo-CP", flush=True)

    train, val, test = split_60_20_20(traces)
    train_val = train + val
    print(f"  Split: train={len(train)}, val={len(val)}, test={len(test)}", flush=True)

    # --- Main sweep ---
    all_results = {}
    metric_names = ["bal_acc", "precision", "fpr", "crossing_rate", "composite"]
    n_combos = len(layers_to_sweep) * len(windows_to_sweep)
    combo_idx = 0

    for layer_idx in layers_to_sweep:
        all_results[layer_idx] = {}

        for window in windows_to_sweep:
            combo_idx += 1
            t_combo = time.time()

            X_train_raw, _ = build_windowed_features(train_val, layer_idx, window)
            X_test_raw, n_test = build_windowed_features(test, layer_idx, window)
            y_train = get_labels(train_val)
            y_test = get_labels(test)

            pca_dim = min(PCA_DIM, X_train_raw.shape[1], X_train_raw.shape[0])
            pca = PCA(n_components=pca_dim, random_state=SEED)
            X_train_pca = pca.fit_transform(X_train_raw)
            X_test_pca = pca.transform(X_test_raw)
            ev = pca.explained_variance_ratio_.sum()

            del X_train_raw, X_test_raw

            result = evaluate_layer_window(X_train_pca, y_train, X_test_pca, y_test, test, n_test)
            all_results[layer_idx][window] = result

            elapsed = time.time() - t_combo
            if result:
                print(f"  [{combo_idx}/{n_combos}] L{layer_idx:2d} W{window:2d}: "
                      f"ba={result['bal_acc']:.3f} prec={result['precision']:.3f} "
                      f"fpr={result['fpr']:.3f} cr={result['crossing_rate']:.3f} "
                      f"comp={result['composite']:.3f} (PCA {ev:.2f}, {elapsed:.1f}s)",
                      flush=True)
            else:
                print(f"  [{combo_idx}/{n_combos}] L{layer_idx:2d} W{window:2d}: SKIPPED", flush=True)

    # Free HS memory
    for t in traces:
        del t["hs"]
    gc.collect()

    # --- Find best layers ---
    print(f"\n{ts()} Finding best layers per metric...", flush=True)
    best_layers = {}
    for m in metric_names:
        best_val = -1e9 if m != "fpr" else 1e9
        best_key = None
        for layer_idx in layers_to_sweep:
            for window in windows_to_sweep:
                r = all_results[layer_idx].get(window)
                if r is None:
                    continue
                metric_val = r[m]
                if m == "fpr":
                    if metric_val < best_val:
                        best_val = metric_val
                        best_key = (layer_idx, window)
                else:
                    if metric_val > best_val:
                        best_val = metric_val
                        best_key = (layer_idx, window)
        best_layers[m] = {"layer": best_key[0], "window": best_key[1], "value": best_val}

    # Per-window best
    best_per_window = {}
    for m in metric_names:
        best_per_window[m] = {}
        for window in windows_to_sweep:
            best_val = -1e9 if m != "fpr" else 1e9
            best_l = None
            for layer_idx in layers_to_sweep:
                r = all_results[layer_idx].get(window)
                if r is None:
                    continue
                metric_val = r[m]
                if m == "fpr":
                    if metric_val < best_val:
                        best_val = metric_val
                        best_l = layer_idx
                else:
                    if metric_val > best_val:
                        best_val = metric_val
                        best_l = layer_idx
            best_per_window[m][f"W{window}"] = {
                "layer": f"L{best_l}",
                "value": round(best_val, 4),
            }

    # --- Print summary table ---
    print(f"\n{'='*70}", flush=True)
    print(f"Best layers per metric × window (AdvBench, pseudo-CP):", flush=True)
    print(f"{'Metric':16s}", end="")
    for w in windows_to_sweep:
        print(f" {'W='+str(w):>8s}", end="")
    print()
    print("-" * (16 + 9 * len(windows_to_sweep)))
    for m in metric_names:
        print(f"{m:16s}", end="")
        for w in windows_to_sweep:
            info = best_per_window[m][f"W{w}"]
            print(f" {info['layer']:>8s}", end="")
        print()
    print(f"{'='*70}", flush=True)

    # --- Bootstrap CI for best layers ---
    if not dry_run:
        print(f"\n{ts()} Bootstrap {N_BOOTSTRAP}x for best layers...", flush=True)
        # Reload traces with HS for bootstrap
        traces_reload = load_traces()
        bootstrap_results = {}
        for m in metric_names:
            bl = best_layers[m]
            key = f"L{bl['layer']}_W{bl['window']}"
            if key in bootstrap_results:
                bootstrap_results[f"{m}_best"] = bootstrap_results[key]
                continue
            print(f"  {m}: L{bl['layer']} W{bl['window']}...", end="", flush=True)
            t_boot = time.time()
            ci = bootstrap_ci(traces_reload, bl["layer"], bl["window"])
            bootstrap_results[key] = ci
            bootstrap_results[f"{m}_best"] = ci
            print(f" done ({time.time()-t_boot:.0f}s)", flush=True)
            for mm, vals in ci.items():
                if vals["mean"] is not None:
                    print(f"    {mm}: {vals['mean']:.3f} [{vals['ci_lo']:.3f}, {vals['ci_hi']:.3f}]",
                          flush=True)
        del traces_reload
    else:
        bootstrap_results = {}

    # --- Full table ---
    full_table = {}
    for m in metric_names:
        full_table[m] = {}
        for layer_idx in layers_to_sweep:
            full_table[m][f"L{layer_idx}"] = {}
            for window in windows_to_sweep:
                r = all_results[layer_idx].get(window)
                full_table[m][f"L{layer_idx}"][f"W{window}"] = r[m] if r else None

    # --- Save ---
    elapsed = time.time() - t_start
    output = {
        "experiment": "advbench_preliminary_pseudo_cp_sweep",
        "model": "DeepSeek-R1-Distill-Qwen-8B",
        "dataset": "AdvBench (B-class, pseudo-CP)",
        "method": "heuristic_max_cosine_dist",
        "n_traces": len(traces),
        "split": {"train": len(train), "val": len(val), "test": len(test)},
        "seed": SEED,
        "layers": len(layers_to_sweep),
        "layer_range": f"L{layers_to_sweep[0]}-L{layers_to_sweep[-1]}",
        "windows": windows_to_sweep,
        "metrics": metric_names,
        "pca_dim": PCA_DIM,
        "max_iter": MAX_ITER,
        "crossing_k": K_CROSSING,
        "crossing_threshold": CROSSING_THRESHOLD,
        "n_bootstrap": N_BOOTSTRAP if not dry_run else 0,
        "runtime_seconds": round(elapsed, 1),
        "best_layers_overall": {m: best_layers[m] for m in metric_names},
        "best_layers_per_window": best_per_window,
        "full_table": full_table,
        "bootstrap_ci": bootstrap_results,
    }

    out_path = OUTPUT_DIR / "sweep_results.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\n{ts()} Saved to {out_path}", flush=True)

    # --- Human-readable report ---
    lines = [
        f"AdvBench Preliminary Layer Sweep (pseudo-CP)",
        "=" * 55,
        f"Traces: {len(traces)} (B-class compliance, heuristic CP)",
        f"Layers: {len(layers_to_sweep)}, Windows: {windows_to_sweep}",
        f"Split: {len(train)}/{len(val)}/{len(test)}, Seed: {SEED}",
        f"PCA: {PCA_DIM}d, LR: C=1.0 balanced max_iter={MAX_ITER}",
        f"Bootstrap: {N_BOOTSTRAP if not dry_run else 0}",
        "",
        f"{'Metric':16s}",
    ]
    header = f"{'Metric':16s}"
    for w in windows_to_sweep:
        header += f" {'W='+str(w):>8s}"
    lines.append(header)
    lines.append("-" * (16 + 9 * len(windows_to_sweep)))
    for m in metric_names:
        row = f"{m:16s}"
        for w in windows_to_sweep:
            info = best_per_window[m][f"W{w}"]
            row += f" {info['layer']:>8s}"
        lines.append(row)

    lines.append("")
    lines.append("Best layers with values:")
    for m in metric_names:
        bl = best_layers[m]
        lines.append(f"  {m}: L{bl['layer']} W{bl['window']} = {bl['value']:.4f}")

    if bootstrap_results:
        lines.append("")
        lines.append("Bootstrap 95% CI (best layer per metric):")
        for m in metric_names:
            ci = bootstrap_results.get(f"{m}_best", {}).get(m, {})
            if ci and ci.get("mean") is not None:
                lines.append(f"  {m}: {ci['mean']:.3f} [{ci['ci_lo']:.3f}, {ci['ci_hi']:.3f}]")

    lines.append(f"\nTotal time: {elapsed:.0f}s")
    report = "\n".join(lines)

    with open(OUTPUT_DIR / "report.txt", "w") as f:
        f.write(report)
    print(f"\n{report}", flush=True)
    print(f"\n{ts()} DONE.", flush=True)


if __name__ == "__main__":
    main()
