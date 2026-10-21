"""Random-CP control experiment for QwQ-32B.

Replaces real CP with uniform-random CP [0.2, 0.8]*T for each trace,
retrains LR probes at every layer, measures 5 layer-selection metrics.
Tests whether the metric disagreement pattern (CR-composite -> L2 shallow,
threshold-based -> L63 deep) is CP-quality-dependent or a geometry artifact.

Also runs real-CP baseline to confirm the L2 vs L63 disagreement.
10 random-CP repeats with seeds 42-51. Uses PCA to 100d for tractability.
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
N_REPEATS = 10
SEED_BASE = 42
W = 5
HIDDEN_DIM = 5120
N_LAYERS = 64
MAX_ITER = 2000
K_CROSSING = 5
CROSSING_THRESHOLD = 0.5
PCA_DIM = 100
SHALLOW_THRESHOLD = 10
DEEP_THRESHOLD = 50

BASE = Path("DATA_DIR")
HS_DIR = BASE / "artifacts/hidden_states_qwq_32b"
OUTPUT_DIR = BASE / "artifacts/random_cp_control/qwq_32b"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def ts():
    return time.strftime("[%H:%M:%S]")


def load_traces():
    files = sorted([f for f in os.listdir(HS_DIR) if f.endswith(".pt")])
    traces = []
    for i, fname in enumerate(files):
        d = torch.load(HS_DIR / fname, map_location="cpu", weights_only=True)
        tid = d["trace_id"]
        cp = d.get("commitment_point")
        sl = d.get("step_labels")
        if cp is None or sl is None:
            continue
        hs = d["hidden_states"].float().numpy()
        if isinstance(sl, torch.Tensor):
            sl = sl.tolist()
        T = min(hs.shape[0], len(sl))
        traces.append(dict(
            trace_id=tid,
            hs=hs[:T],
            real_cp=int(cp),
            real_labels=sl[:T],
            num_steps=T,
        ))
        if (i + 1) % 20 == 0:
            print(f"  loaded {i+1}/{len(files)} files", flush=True)
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


def assign_random_cp(traces, rng):
    for t in traces:
        T = t["num_steps"]
        cp = int(rng.uniform(0.2, 0.8) * T)
        cp = max(1, min(T - 1, cp))
        t["random_cp"] = cp
        t["random_labels"] = [0 if i < cp else 1 for i in range(T)]


def build_windowed_features(traces, layer_idx):
    X_list = []
    n_per_trace = []
    for t in traces:
        hs_layer = t["hs"][:, layer_idx, :]
        T = hs_layer.shape[0]
        padded = np.concatenate([np.repeat(hs_layer[:1], W - 1, axis=0), hs_layer], axis=0)
        windows = np.empty((T, W * HIDDEN_DIM), dtype=hs_layer.dtype)
        for w_i in range(W):
            windows[:, w_i * HIDDEN_DIM:(w_i + 1) * HIDDEN_DIM] = padded[w_i:w_i + T]
        X_list.append(windows)
        n_per_trace.append(T)
    return np.vstack(X_list), n_per_trace


def get_labels(traces, label_key):
    y = []
    for t in traces:
        y.extend(t[label_key])
    return np.array(y, dtype=np.int32)


def first_crossing(probs, threshold=CROSSING_THRESHOLD, k=K_CROSSING):
    for i in range(len(probs) - k + 1):
        if all(p > threshold for p in probs[i:i + k]):
            return i
    return None


def run_layer_sweep(layer_data, train, test, label_key, cp_key):
    y_train = get_labels(train, label_key)

    layer_metrics = {}
    for layer_idx in range(N_LAYERS):
        ld = layer_data[layer_idx]
        X_tr = ld["X_train_pca"]

        scaler = StandardScaler()
        X_tr_scaled = scaler.fit_transform(X_tr)

        if len(np.unique(y_train)) < 2:
            layer_metrics[layer_idx] = None
            continue

        clf = LogisticRegression(
            solver="lbfgs", C=1.0, class_weight="balanced",
            max_iter=MAX_ITER, random_state=SEED,
        )
        clf.fit(X_tr_scaled, y_train)

        X_te_scaled = scaler.transform(ld["X_test_pca"])
        y_test = get_labels(test, label_key)
        y_pred = clf.predict(X_te_scaled)
        y_proba = clf.predict_proba(X_te_scaled)[:, 1]

        ba = balanced_accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred, zero_division=0)

        fprs_list = []
        n_crossings = 0
        offset = 0
        for i, t in enumerate(test):
            T = ld["n_test"][i]
            cp = t[cp_key]
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
        crossing_rate = n_crossings / len(test) if len(test) > 0 else 0.0

        layer_metrics[layer_idx] = {
            "bal_acc": round(ba, 4),
            "precision": round(prec, 4),
            "pre_cp_fpr": round(pre_cp_fpr, 4),
            "crossing_rate": round(crossing_rate, 4),
            "cr_composite": round(ba * crossing_rate, 4),
        }

    valid = {l: m for l, m in layer_metrics.items() if m is not None}
    best_layers = {
        "bal_acc": max(valid, key=lambda l: valid[l]["bal_acc"]),
        "precision": max(valid, key=lambda l: valid[l]["precision"]),
        "pre_cp_fpr": min(valid, key=lambda l: valid[l]["pre_cp_fpr"]),
        "crossing_rate": max(valid, key=lambda l: valid[l]["crossing_rate"]),
        "cr_composite": max(valid, key=lambda l: valid[l]["cr_composite"]),
    }

    return layer_metrics, best_layers


def main():
    t_start = time.time()
    print(f"{ts()} Loading QwQ-32B traces...", flush=True)
    traces = load_traces()
    print(f"  Loaded {len(traces)} traces", flush=True)

    train, val, test = split_60_20_20(traces)
    print(f"  Split: train={len(train)}, val={len(val)}, test={len(test)}", flush=True)

    print(f"{ts()} Pre-extracting windowed features and fitting PCA per layer...", flush=True)
    train_val = train + val
    layer_data = {}
    for layer_idx in range(N_LAYERS):
        X_train_raw, n_train = build_windowed_features(train, layer_idx)
        X_val_raw, _ = build_windowed_features(val, layer_idx)
        X_test_raw, n_test = build_windowed_features(test, layer_idx)

        X_fit_raw = np.vstack([X_train_raw, X_val_raw])
        del X_val_raw

        pca = PCA(n_components=PCA_DIM, random_state=SEED)
        pca.fit(X_fit_raw)
        del X_fit_raw

        X_train_pca = pca.transform(X_train_raw)
        del X_train_raw
        X_test_pca = pca.transform(X_test_raw)
        del X_test_raw

        layer_data[layer_idx] = {
            "X_train_pca": X_train_pca,
            "X_test_pca": X_test_pca,
            "n_test": n_test,
        }
        if layer_idx % 16 == 0:
            ev = pca.explained_variance_ratio_.sum()
            print(f"  L{layer_idx:2d}: PCA {PCA_DIM}d explains {ev:.3f} variance", flush=True)

    for t in traces:
        del t["hs"]
    gc.collect()
    print(f"{ts()} Feature extraction done ({time.time()-t_start:.0f}s)", flush=True)

    # Real-CP baseline
    print(f"\n{ts()} === Real-CP Baseline ===", flush=True)
    t_real = time.time()
    real_layer_metrics, real_best_layers = run_layer_sweep(
        layer_data, train, test, "real_labels", "real_cp"
    )
    elapsed_real = time.time() - t_real
    print(f"  Best: ba->L{real_best_layers['bal_acc']} "
          f"prec->L{real_best_layers['precision']} "
          f"fpr->L{real_best_layers['pre_cp_fpr']} "
          f"cr->L{real_best_layers['crossing_rate']} "
          f"cr_comp->L{real_best_layers['cr_composite']} ({elapsed_real:.0f}s)", flush=True)

    # Random-CP repeats
    all_repeats = []
    for rep in range(N_REPEATS):
        rep_seed = SEED_BASE + rep
        rng = np.random.default_rng(rep_seed)
        t_rep = time.time()
        print(f"\n{ts()} === Random-CP Repeat {rep} (seed={rep_seed}) ===", flush=True)

        assign_random_cp(train, rng)
        assign_random_cp(val, rng)
        assign_random_cp(test, rng)

        layer_metrics, best_layers = run_layer_sweep(
            layer_data, train, test, "random_labels", "random_cp"
        )

        elapsed_rep = time.time() - t_rep
        print(f"  Best: ba->L{best_layers['bal_acc']} "
              f"prec->L{best_layers['precision']} "
              f"fpr->L{best_layers['pre_cp_fpr']} "
              f"cr->L{best_layers['crossing_rate']} "
              f"cr_comp->L{best_layers['cr_composite']} ({elapsed_rep:.0f}s)", flush=True)

        all_repeats.append({
            "repeat": rep,
            "seed": rep_seed,
            "best_layers": best_layers,
            "all_layer_metrics": {str(l): m for l, m in layer_metrics.items() if m is not None},
        })

    # Aggregate
    print(f"\n{ts()} === AGGREGATION ===", flush=True)

    metric_names = ["bal_acc", "precision", "pre_cp_fpr", "crossing_rate", "cr_composite"]
    selected_layers = {m: [] for m in metric_names}
    for r in all_repeats:
        for m in metric_names:
            selected_layers[m].append(r["best_layers"][m])

    summary = {}
    for m in metric_names:
        layers = selected_layers[m]
        mean_l = np.mean(layers)
        std_l = np.std(layers)
        shallow_freq = sum(1 for l in layers if l <= SHALLOW_THRESHOLD) / len(layers)
        deep_freq = sum(1 for l in layers if l >= DEEP_THRESHOLD) / len(layers)
        summary[m] = {
            "mean_layer": round(float(mean_l), 1),
            "std_layer": round(float(std_l), 1),
            "selected_layers": layers,
            "shallow_freq": round(shallow_freq, 2),
            "deep_freq": round(deep_freq, 2),
        }
        print(f"  {m:16s}: mean_L={mean_l:5.1f} +/- {std_l:4.1f} "
              f"shallow={shallow_freq:.0%} deep={deep_freq:.0%} "
              f"layers={layers}", flush=True)

    cr_composite_selects_shallow = summary["cr_composite"]["shallow_freq"]
    threshold_prec_deep = summary["precision"]["deep_freq"]
    threshold_fpr_deep = summary["pre_cp_fpr"]["deep_freq"]
    threshold_selects_deep = (threshold_prec_deep + threshold_fpr_deep) / 2

    real_cr_comp_layer = real_best_layers["cr_composite"]
    real_prec_layer = real_best_layers["precision"]
    real_fpr_layer = real_best_layers["pre_cp_fpr"]
    real_gap = abs(real_prec_layer - real_cr_comp_layer)

    print(f"\n  Real-CP: CR-composite->L{real_cr_comp_layer}, Precision->L{real_prec_layer}, "
          f"FPR->L{real_fpr_layer}, gap={real_gap}", flush=True)
    print(f"  Random-CP: CR-composite shallow freq={cr_composite_selects_shallow:.0%}", flush=True)
    print(f"  Random-CP: Precision deep freq={threshold_prec_deep:.0%}", flush=True)
    print(f"  Random-CP: FPR deep freq={threshold_fpr_deep:.0%}", flush=True)

    disagreement_replicates = (cr_composite_selects_shallow >= 0.6 and
                               threshold_selects_deep >= 0.6)
    print(f"  Metric disagreement replicates: {disagreement_replicates}", flush=True)

    # Save
    result = {
        "model": "QwQ-32B",
        "n_traces": len(traces),
        "n_layers": N_LAYERS,
        "window": W,
        "pca_dim": PCA_DIM,
        "n_repeats": N_REPEATS,
        "seed_base": SEED_BASE,
        "max_iter": MAX_ITER,
        "crossing_k": K_CROSSING,
        "crossing_threshold": CROSSING_THRESHOLD,
        "split": {"train": len(train), "val": len(val), "test": len(test)},
        "real_cp": {
            "best_layers": real_best_layers,
            "all_layer_metrics": {str(l): m for l, m in real_layer_metrics.items() if m is not None},
        },
        "random_cp_repeats": all_repeats,
    }
    with open(OUTPUT_DIR / "random_cp_layer_selection.json", "w") as f:
        json.dump(result, f, indent=2)

    summary_out = {
        "model": "QwQ-32B",
        "n_layers": N_LAYERS,
        "n_traces": len(traces),
        "n_repeats": N_REPEATS,
        "real_cp_disagreement": {
            "cr_composite_layer": real_cr_comp_layer,
            "precision_layer": real_prec_layer,
            "fpr_layer": real_fpr_layer,
            "gap": real_gap,
        },
        "random_cp_cr_composite_mean_layer": summary["cr_composite"]["mean_layer"],
        "random_cp_cr_composite_std_layer": summary["cr_composite"]["std_layer"],
        "random_cp_precision_mean_layer": summary["precision"]["mean_layer"],
        "random_cp_precision_std_layer": summary["precision"]["std_layer"],
        "cr_composite_selects_shallow_freq": cr_composite_selects_shallow,
        "precision_selects_deep_freq": threshold_prec_deep,
        "fpr_selects_deep_freq": threshold_fpr_deep,
        "threshold_based_selects_deep_freq": threshold_selects_deep,
        "metric_disagreement_replicates": disagreement_replicates,
        "per_metric_summary": summary,
        "pca_dim": PCA_DIM,
        "elapsed_s": round(time.time() - t_start, 1),
    }
    with open(OUTPUT_DIR / "random_cp_summary.json", "w") as f:
        json.dump(summary_out, f, indent=2)

    # Human-readable report
    lines = [
        "Random-CP Control Experiment: QwQ-32B",
        "=" * 55,
        f"Traces: {len(traces)}, Layers: {N_LAYERS}, Window: {W}, PCA: {PCA_DIM}d",
        f"Repeats: {N_REPEATS} (seeds {SEED_BASE}-{SEED_BASE+N_REPEATS-1})",
        f"Split: {len(train)}/{len(val)}/{len(test)}",
        "",
        "Real-CP Baseline:",
        f"  CR-composite -> L{real_cr_comp_layer}",
        f"  Precision    -> L{real_prec_layer}",
        f"  FPR          -> L{real_fpr_layer}",
        f"  BA           -> L{real_best_layers['bal_acc']}",
        f"  Crossing     -> L{real_best_layers['crossing_rate']}",
        f"  Disagreement gap: {real_gap} layers",
        "",
        f"Random-CP Layer Selection (across {N_REPEATS} repeats):",
        f"  {'Metric':16s} {'Mean L':>7s} {'Std':>5s} {'Shallow%':>9s} {'Deep%':>6s} {'Layers'}",
        "-" * 80,
    ]
    for m in metric_names:
        s = summary[m]
        lines.append(
            f"  {m:16s} {s['mean_layer']:7.1f} {s['std_layer']:5.1f} "
            f"{s['shallow_freq']:9.0%} {s['deep_freq']:6.0%} {s['selected_layers']}"
        )
    lines += [
        "",
        "Key findings:",
        f"  Real-CP: CR-composite->L{real_cr_comp_layer} (shallow), "
        f"Precision->L{real_prec_layer}, FPR->L{real_fpr_layer} (deep)",
        f"  Random-CP: CR-composite selects shallow (L<={SHALLOW_THRESHOLD}) "
        f"in {cr_composite_selects_shallow:.0%} of repeats",
        f"  Random-CP: Precision selects deep (L>={DEEP_THRESHOLD}) "
        f"in {threshold_prec_deep:.0%} of repeats",
        f"  Random-CP: FPR selects deep (L>={DEEP_THRESHOLD}) "
        f"in {threshold_fpr_deep:.0%} of repeats",
        f"  Metric disagreement replicates with random CP: {disagreement_replicates}",
        "",
        "Interpretation:",
    ]
    if disagreement_replicates:
        lines.append("  The metric disagreement pattern persists with random CPs,")
        lines.append("  suggesting it may reflect model geometry rather than CP quality.")
    else:
        lines.append("  The metric disagreement pattern does NOT replicate with random CPs,")
        lines.append("  supporting that the L2 vs L63 disagreement requires real CP labels")
        lines.append("  and reflects genuine model behavioral structure.")
    lines.append(f"\nTotal time: {time.time() - t_start:.0f}s")

    report = "\n".join(lines)
    with open(OUTPUT_DIR / "report.txt", "w") as f:
        f.write(report)
    print(f"\n{report}", flush=True)
    print(f"\n{ts()} DONE. Saved to {OUTPUT_DIR}", flush=True)


if __name__ == "__main__":
    main()
