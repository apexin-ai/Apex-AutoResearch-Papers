"""
CKA analysis for cross-lingual calibration probing (plan_011).

Computes Linear CKA (Kornblith et al., 2019) between English and target-language
activations, then runs four statistical analyses:
  (a) Same-layer cross-language Spearman ρ(CKA, transfer_degradation)
  (b) Partial Spearman controlling for normalized depth
  (c) Per-language Spearman across layers
  (d) Subspace angle between EN and target correctness probe directions

Input:  Cached activations from extract_activations.py (npy format)
        activations/{model_name}/L{layer}/{lang}_{eval}.npy
        Probe metrics from train_probes.py
Output: CKA matrix, correlation tables, bootstrap CIs, human-readable report

Dependencies: numpy, scipy, sklearn, pandas
"""
import argparse
import json
import os
import pickle
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import spearmanr, rankdata


# ---------------------------------------------------------------------------
# Linear CKA (Kornblith et al., 2019)
# CKA(X, Y) = ||Y^T X||_F^2 / (||X^T X||_F * ||Y^T Y||_F)
# ---------------------------------------------------------------------------

def linear_cka(X, Y):
    """Linear CKA between activation matrices X (n, d_x) and Y (n, d_y).
    Both must have the same n (parallel samples). Returns scalar in [0, 1]."""
    X = X - X.mean(axis=0)
    Y = Y - Y.mean(axis=0)
    XTX = X.T @ X
    YTY = Y.T @ Y
    YTX = Y.T @ X
    num = np.linalg.norm(YTX, 'fro') ** 2
    den = np.linalg.norm(XTX, 'fro') * np.linalg.norm(YTY, 'fro')
    if den == 0:
        return 0.0
    return float(num / den)


# ---------------------------------------------------------------------------
# Activation loading (npy format from extract_activations.py)
# ---------------------------------------------------------------------------

def detect_format(act_dir):
    p = Path(act_dir)
    if list(p.glob("L*/en_eval.npy")):
        return "npy"
    if list(p.glob("layer*_en.pt")):
        return "pt_flat"
    raise FileNotFoundError(f"No activations found in {act_dir}")


def discover_layers(act_dir, fmt):
    p = Path(act_dir)
    if fmt == "npy":
        return sorted(int(d.name[1:]) for d in p.glob("L*")
                       if (d / "en_eval.npy").exists())
    else:
        return sorted({int(f.stem.split("_")[0].replace("layer", ""))
                       for f in p.glob("layer*_en.pt")})


def discover_languages(act_dir, fmt, layers):
    p = Path(act_dir)
    langs = set()
    if fmt == "npy":
        layer_dir = p / f"L{layers[0]}"
        for f in layer_dir.glob("*_eval.npy"):
            lang = f.stem.replace("_eval", "")
            if lang != "en":
                langs.add(lang)
    else:
        for f in p.glob(f"layer{layers[0]}_*.pt"):
            parts = f.stem.split("_")
            lang = parts[1] if len(parts) >= 2 else None
            if lang and lang != "en":
                langs.add(lang)
    return sorted(langs)


def load_eval_activations(act_dir, fmt, layer, lang):
    """Load eval-split activations for a language at a layer."""
    p = Path(act_dir)
    if fmt == "npy":
        path = p / f"L{layer}" / f"{lang}_eval.npy"
        if not path.exists():
            return None
        return np.load(path)
    else:
        import torch
        path = p / f"layer{layer}_{lang}.pt"
        if not path.exists():
            return None
        data = torch.load(path, weights_only=True)
        acts = data["activations"].numpy() if hasattr(data["activations"], 'numpy') else data["activations"]
        n = len(acts)
        split = int(n * 0.7)
        return acts[split:]


# ---------------------------------------------------------------------------
# Metrics loading
# ---------------------------------------------------------------------------

def load_metrics(metrics_dir, model_name):
    """Load EN AUROC and ZS AUROC from train_probes.py output.
    Returns: en_auroc[layer], zs_auroc[(layer, lang)]
    """
    en_auroc = {}
    zs_auroc = {}

    # Try new format: results/{model_name}/metrics/transfer_matrix.json
    new_tm = Path(metrics_dir) / model_name / "metrics" / "transfer_matrix.json"
    new_summary = Path(metrics_dir) / model_name / "metrics" / "summary.json"
    if new_tm.exists():
        with open(new_tm) as f:
            tm = json.load(f)
        with open(new_summary) as f:
            summary = json.load(f)
        for key, m in summary.get("en_eval", {}).items():
            # key like "lr_L0"
            parts = key.split("_L")
            if len(parts) == 2:
                layer = int(parts[1])
                en_auroc[layer] = m["auroc"]
        for pt in tm:
            for lang in tm[pt]:
                for layer_str in tm[pt][lang]:
                    layer = int(layer_str)
                    zs = tm[pt][lang][layer_str].get("zero_shot")
                    if zs:
                        zs_auroc[(layer, lang)] = zs["auroc"]
        return en_auroc, zs_auroc

    # Fallback: old format CSV files
    train_csv = Path(metrics_dir) / "train_metrics.csv"
    transfer_csv = Path(metrics_dir) / "transfer_results.csv"
    if train_csv.exists() and transfer_csv.exists():
        df_train = pd.read_csv(train_csv)
        for _, row in df_train.iterrows():
            en_auroc[int(row["layer"])] = row["auroc"]
        df_transfer = pd.read_csv(transfer_csv)
        df_zs = df_transfer[df_transfer["method"] == "zero_shot"].dropna(subset=["auroc"])
        for _, row in df_zs.iterrows():
            zs_auroc[(int(row["layer"]), row["language"])] = row["auroc"]
        return en_auroc, zs_auroc

    # Try probes_dir/train_metrics.csv
    probes_csv = Path(metrics_dir).parent / "probes" / "train_metrics.csv"
    if probes_csv.exists():
        df = pd.read_csv(probes_csv)
        for _, row in df.iterrows():
            en_auroc[int(row["layer"])] = row["auroc"]

    return en_auroc, zs_auroc


def load_probe_weights(probes_dir, model_name, layer):
    """Load LR probe weight vector for subspace angle analysis.
    Returns: (d,) weight vector or None.
    """
    # New format
    pkl_path = Path(probes_dir) / model_name / "probes" / f"L{layer}" / "en_lr_probe.pkl"
    if pkl_path.exists():
        with open(pkl_path, "rb") as f:
            data = pickle.load(f)
        model = data["model"]
        if hasattr(model, "coef_"):
            return model.coef_.flatten()
        return None

    # Old format
    pkl_path = Path(probes_dir) / f"probe_layer{layer}.pkl"
    if pkl_path.exists():
        with open(pkl_path, "rb") as f:
            data = pickle.load(f)
        model = data["model"]
        if hasattr(model, "coef_"):
            return model.coef_.flatten()
    return None


# ---------------------------------------------------------------------------
# Bootstrap CI
# ---------------------------------------------------------------------------

def bootstrap_ci(values, stat_fn=np.mean, n_boot=1000, ci=0.95, seed=42):
    """Bootstrap CI for a statistic. values: array or tuple of arrays for corr."""
    rng = np.random.RandomState(seed)
    n = len(values) if isinstance(values, np.ndarray) else len(values[0])
    stats = []
    for _ in range(n_boot):
        idx = rng.randint(0, n, size=n)
        if isinstance(values, tuple):
            s = stat_fn(values[0][idx], values[1][idx])
        else:
            s = stat_fn(values[idx])
        if s is not None and np.isfinite(s):
            stats.append(s)
    if len(stats) < 10:
        return float('nan'), float('nan')
    alpha = (1 - ci) / 2
    return float(np.percentile(stats, 100 * alpha)), float(np.percentile(stats, 100 * (1 - alpha)))


def spearman_stat(x, y):
    if len(x) < 3:
        return float('nan')
    rho, _ = spearmanr(x, y)
    return rho


# ---------------------------------------------------------------------------
# Partial Spearman correlation (rank-based, no pingouin dependency)
# ---------------------------------------------------------------------------

def partial_spearman(x, y, z):
    """Partial Spearman ρ(x, y | z). All inputs: 1-D arrays of same length.
    Computes rank-based partial correlation by regressing out z from ranks of x, y.
    Returns (partial_rho, p_value).
    """
    n = len(x)
    if n < 4:
        return float('nan'), float('nan')

    rx = rankdata(x)
    ry = rankdata(y)
    rz = rankdata(z)

    # Spearman correlations between pairs
    rho_xy, _ = spearmanr(x, y)
    rho_xz, _ = spearmanr(x, z)
    rho_yz, _ = spearmanr(y, z)

    # Partial correlation formula: ρ_xy.z = (ρ_xy - ρ_xz * ρ_yz) / sqrt((1-ρ_xz²)(1-ρ_yz²))
    num = rho_xy - rho_xz * rho_yz
    den = np.sqrt(max(0, (1 - rho_xz**2) * (1 - rho_yz**2)))
    if den < 1e-10:
        return float('nan'), float('nan')

    partial_rho = num / den

    # t-test for significance (df = n - 3 for one control variable)
    from scipy.stats import t as t_dist
    df = n - 3
    if df < 1:
        return partial_rho, float('nan')
    t_stat = partial_rho * np.sqrt(df / max(1e-10, 1 - partial_rho**2))
    p_value = 2 * t_dist.sf(abs(t_stat), df)

    return float(partial_rho), float(p_value)


# ---------------------------------------------------------------------------
# Subspace angle: train target-language probe, compare weight direction
# ---------------------------------------------------------------------------

def train_lr_probe(X, y, seed=42):
    """Train a logistic regression probe. Returns weight vector (d,)."""
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import StandardScaler
    scaler = StandardScaler()
    X_s = scaler.fit_transform(X)
    lr = LogisticRegression(max_iter=2000, C=1.0, random_state=seed, solver="lbfgs")
    lr.fit(X_s, y)
    return lr.coef_.flatten()


def cosine_similarity(w1, w2):
    """Cosine similarity between two vectors."""
    n1 = np.linalg.norm(w1)
    n2 = np.linalg.norm(w2)
    if n1 < 1e-10 or n2 < 1e-10:
        return 0.0
    return float(np.dot(w1, w2) / (n1 * n2))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def parse_args():
    p = argparse.ArgumentParser(
        description="CKA analysis for cross-lingual calibration probing (plan_011)")
    p.add_argument("--activation_dir", required=True,
                   help="Activation root (e.g. activations/qwen3_235b_int4)")
    p.add_argument("--model_name", required=True,
                   help="Model short name (e.g. qwen3_235b_int4)")
    p.add_argument("--metrics_dir", default="results",
                   help="Directory containing probe metrics (train_probes.py output)")
    p.add_argument("--probes_dir", default=None,
                   help="Directory containing saved probes (for subspace angles). "
                        "Default: same as metrics_dir")
    p.add_argument("--output_dir", default=None,
                   help="Output dir. Default: results/{model_name}/cka/")
    p.add_argument("--n_bootstrap", type=int, default=1000)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--languages", nargs="+", default=None,
                   help="Language list. Default: auto-discover from activations")
    p.add_argument("--layers", nargs="+", type=int, default=None,
                   help="Layer list. Default: auto-discover from activations")
    p.add_argument("--skip_subspace", action="store_true",
                   help="Skip subspace angle analysis (requires training probes)")
    return p.parse_args()


def main():
    args = parse_args()
    t0 = time.time()

    if args.probes_dir is None:
        args.probes_dir = args.metrics_dir
    if args.output_dir is None:
        args.output_dir = os.path.join("results", args.model_name, "cka")

    os.makedirs(args.output_dir, exist_ok=True)

    # ---- Discover structure ----
    fmt = detect_format(args.activation_dir)
    layers = args.layers or discover_layers(args.activation_dir, fmt)
    languages = args.languages or discover_languages(args.activation_dir, fmt, layers)

    print(f"Format: {fmt}")
    print(f"Layers ({len(layers)}): {layers}")
    print(f"Languages ({len(languages)}): {languages}")

    # ---- Load metrics ----
    en_auroc, zs_auroc = load_metrics(args.metrics_dir, args.model_name)
    has_metrics = bool(en_auroc and zs_auroc)
    if has_metrics:
        print(f"Loaded metrics: {len(en_auroc)} EN layers, {len(zs_auroc)} ZS entries")
    else:
        print("WARNING: No probe metrics found. Correlation analyses will be skipped.")

    num_layers_total = max(layers) + 1

    # ==================================================================
    # 1. CKA matrix
    # ==================================================================
    print(f"\n{'='*60}")
    print("Computing CKA matrix")
    print(f"{'='*60}")

    cka_matrix = {}  # (layer, lang) -> cka_value
    cka_boot_cis = {}

    header = f"{'Layer':>5s}" + "".join(f" {l:>7s}" for l in languages)
    print(header)
    print("-" * len(header))

    for layer in layers:
        X_en = load_eval_activations(args.activation_dir, fmt, layer, "en")
        if X_en is None:
            print(f"{layer:>5d}  [EN missing]")
            continue

        row_str = f"{layer:>5d}"
        for lang in languages:
            X_tgt = load_eval_activations(args.activation_dir, fmt, layer, lang)
            if X_tgt is None:
                row_str += f" {'N/A':>7s}"
                continue
            n = min(len(X_en), len(X_tgt))
            cka_val = linear_cka(X_en[:n], X_tgt[:n])
            cka_matrix[(layer, lang)] = cka_val
            row_str += f" {cka_val:>7.4f}"

            # Bootstrap CI for CKA
            def cka_boot(idx):
                return linear_cka(X_en[:n][idx], X_tgt[:n][idx])

            rng = np.random.RandomState(args.seed)
            boot_vals = []
            for _ in range(args.n_bootstrap):
                idx = rng.randint(0, n, size=n)
                boot_vals.append(linear_cka(X_en[:n][idx], X_tgt[:n][idx]))
            ci_lo = float(np.percentile(boot_vals, 2.5))
            ci_hi = float(np.percentile(boot_vals, 97.5))
            cka_boot_cis[(layer, lang)] = (ci_lo, ci_hi)

        print(row_str)

    # ==================================================================
    # 2a. Same-layer cross-language correlation
    # ==================================================================
    same_layer_corr = {}
    if has_metrics:
        print(f"\n{'='*60}")
        print("Analysis (a): Same-layer cross-language Spearman")
        print(f"{'='*60}")
        print(f"{'Layer':>5s} {'n':>3s} {'ρ(CKA,deg)':>11s} {'p':>8s} {'ρ(CKA,ZS)':>10s} {'p':>8s}")
        print("-" * 52)

        for layer in layers:
            cka_vals = []
            deg_vals = []
            zs_vals = []
            langs_used = []

            en_auc = en_auroc.get(layer)
            if en_auc is None:
                continue

            for lang in languages:
                cka_val = cka_matrix.get((layer, lang))
                zs_auc = zs_auroc.get((layer, lang))
                if cka_val is None or zs_auc is None:
                    continue
                degradation = (en_auc - zs_auc) / en_auc if en_auc > 0 else 0
                cka_vals.append(cka_val)
                deg_vals.append(degradation)
                zs_vals.append(zs_auc)
                langs_used.append(lang)

            n_pts = len(cka_vals)
            if n_pts < 4:
                continue

            cka_arr = np.array(cka_vals)
            deg_arr = np.array(deg_vals)
            zs_arr = np.array(zs_vals)

            rho_deg, p_deg = spearmanr(cka_arr, deg_arr)
            rho_zs, p_zs = spearmanr(cka_arr, zs_arr)

            # Bootstrap CIs
            ci_deg = bootstrap_ci((cka_arr, deg_arr), spearman_stat,
                                  args.n_bootstrap, seed=args.seed)
            ci_zs = bootstrap_ci((cka_arr, zs_arr), spearman_stat,
                                 args.n_bootstrap, seed=args.seed)

            sig_deg = "*" if p_deg < 0.05 else ""
            sig_zs = "*" if p_zs < 0.05 else ""
            print(f"{layer:>5d} {n_pts:>3d} {rho_deg:>+10.4f}{sig_deg} {p_deg:>8.4f} "
                  f"{rho_zs:>+9.4f}{sig_zs} {p_zs:>8.4f}")

            same_layer_corr[layer] = {
                "n": n_pts,
                "rho_cka_degradation": float(rho_deg),
                "p_cka_degradation": float(p_deg),
                "ci_cka_degradation": list(ci_deg),
                "rho_cka_zs_auroc": float(rho_zs),
                "p_cka_zs_auroc": float(p_zs),
                "ci_cka_zs_auroc": list(ci_zs),
                "languages": langs_used,
            }

    # ==================================================================
    # 2b. Partial Spearman controlling for normalized depth
    # ==================================================================
    partial_corr_results = {}
    if has_metrics:
        print(f"\n{'='*60}")
        print("Analysis (b): Partial Spearman ρ(CKA, degradation | depth)")
        print(f"{'='*60}")

        all_cka = []
        all_deg = []
        all_depth = []

        for layer in layers:
            en_auc = en_auroc.get(layer)
            if en_auc is None:
                continue
            norm_depth = layer / num_layers_total
            for lang in languages:
                cka_val = cka_matrix.get((layer, lang))
                zs_auc = zs_auroc.get((layer, lang))
                if cka_val is None or zs_auc is None:
                    continue
                degradation = (en_auc - zs_auc) / en_auc if en_auc > 0 else 0
                all_cka.append(cka_val)
                all_deg.append(degradation)
                all_depth.append(norm_depth)

        if len(all_cka) >= 10:
            cka_arr = np.array(all_cka)
            deg_arr = np.array(all_deg)
            depth_arr = np.array(all_depth)

            # Full Spearman (no control)
            rho_full, p_full = spearmanr(cka_arr, deg_arr)

            # Partial Spearman controlling for depth
            rho_partial, p_partial = partial_spearman(cka_arr, deg_arr, depth_arr)

            # Also: Spearman of CKA vs depth, degradation vs depth
            rho_cka_depth, p_cka_depth = spearmanr(cka_arr, depth_arr)
            rho_deg_depth, p_deg_depth = spearmanr(deg_arr, depth_arr)

            # Bootstrap CI for partial rho
            rng = np.random.RandomState(args.seed)
            boot_partial = []
            n_pts = len(cka_arr)
            for _ in range(args.n_bootstrap):
                idx = rng.randint(0, n_pts, size=n_pts)
                pr, _ = partial_spearman(cka_arr[idx], deg_arr[idx], depth_arr[idx])
                if np.isfinite(pr):
                    boot_partial.append(pr)
            ci_partial = (float(np.percentile(boot_partial, 2.5)),
                          float(np.percentile(boot_partial, 97.5))) if boot_partial else (float('nan'), float('nan'))

            partial_corr_results = {
                "n_observations": n_pts,
                "full_spearman_rho": float(rho_full),
                "full_spearman_p": float(p_full),
                "partial_spearman_rho": float(rho_partial),
                "partial_spearman_p": float(p_partial),
                "partial_spearman_ci": list(ci_partial),
                "rho_cka_depth": float(rho_cka_depth),
                "p_cka_depth": float(p_cka_depth),
                "rho_degradation_depth": float(rho_deg_depth),
                "p_degradation_depth": float(p_deg_depth),
            }

            print(f"  N observations: {n_pts}")
            print(f"  Full ρ(CKA, degradation):    {rho_full:+.4f} (p={p_full:.4f})")
            print(f"  Partial ρ(CKA, deg | depth): {rho_partial:+.4f} (p={p_partial:.4f})"
                  f"  CI=[{ci_partial[0]:.4f}, {ci_partial[1]:.4f}]")
            print(f"  ρ(CKA, depth):               {rho_cka_depth:+.4f} (p={p_cka_depth:.4f})")
            print(f"  ρ(degradation, depth):        {rho_deg_depth:+.4f} (p={p_deg_depth:.4f})")

            if p_partial < 0.05:
                print("  => CKA has independent explanatory power beyond depth")
            else:
                print("  => CKA may be a proxy for depth (partial ρ not significant)")
        else:
            print(f"  Insufficient data ({len(all_cka)} observations, need ≥10)")

    # ==================================================================
    # 2c. Per-language Spearman across layers
    # ==================================================================
    per_lang_corr = {}
    if has_metrics:
        print(f"\n{'='*60}")
        print("Analysis (c): Per-language Spearman (CKA vs ZS AUROC across layers)")
        print(f"{'='*60}")
        print(f"{'Lang':>6s} {'n':>3s} {'ρ':>7s} {'p':>8s} {'CI_lo':>7s} {'CI_hi':>7s}")
        print("-" * 42)

        for lang in languages:
            cka_vals = []
            zs_vals = []
            for layer in layers:
                cka_val = cka_matrix.get((layer, lang))
                zs_auc = zs_auroc.get((layer, lang))
                if cka_val is not None and zs_auc is not None:
                    cka_vals.append(cka_val)
                    zs_vals.append(zs_auc)

            n_pts = len(cka_vals)
            if n_pts < 4:
                print(f"{lang:>6s} {n_pts:>3d}  insufficient data")
                continue

            cka_arr = np.array(cka_vals)
            zs_arr = np.array(zs_vals)
            rho, p = spearmanr(cka_arr, zs_arr)
            ci = bootstrap_ci((cka_arr, zs_arr), spearman_stat,
                              args.n_bootstrap, seed=args.seed)
            sig = "*" if p < 0.05 else ""
            print(f"{lang:>6s} {n_pts:>3d} {rho:>+7.4f} {p:>8.4f}{sig} {ci[0]:>7.4f} {ci[1]:>7.4f}")

            per_lang_corr[lang] = {
                "n_layers": n_pts,
                "rho": float(rho),
                "p_value": float(p),
                "ci": list(ci),
            }

    # ==================================================================
    # 2d. Subspace angle analysis
    # ==================================================================
    subspace_angles = {}
    if not args.skip_subspace:
        print(f"\n{'='*60}")
        print("Analysis (d): Subspace angle (EN vs target correctness direction)")
        print(f"{'='*60}")

        # Try to load pre-trained EN probe weights first
        en_weights = {}
        for layer in layers:
            w = load_probe_weights(args.probes_dir, args.model_name, layer)
            if w is not None:
                en_weights[layer] = w

        if en_weights:
            print(f"Loaded EN probe weights for {len(en_weights)} layers")
        else:
            print("No pre-trained EN probes found. Training EN probes from activations...")
            for layer in layers:
                en_train_path = Path(args.activation_dir) / f"L{layer}" / "en_train.npy"
                en_labels_path = Path(args.activation_dir) / f"L{layer}" / "en_train_labels.npy"
                if en_train_path.exists() and en_labels_path.exists():
                    X = np.load(en_train_path)
                    y = np.load(en_labels_path)
                    if len(np.unique(y)) >= 2:
                        en_weights[layer] = train_lr_probe(X, y, args.seed)
            print(f"Trained EN probes for {len(en_weights)} layers")

        if en_weights:
            header = f"{'Layer':>5s}" + "".join(f" {l:>7s}" for l in languages)
            print(header)
            print("-" * len(header))

            for layer in layers:
                w_en = en_weights.get(layer)
                if w_en is None:
                    continue

                row_str = f"{layer:>5d}"
                for lang in languages:
                    # Train target-language probe
                    if fmt == "npy":
                        train_path = Path(args.activation_dir) / f"L{layer}" / f"{lang}_train.npy"
                        labels_path = Path(args.activation_dir) / f"L{layer}" / f"{lang}_train_labels.npy"
                        if not (train_path.exists() and labels_path.exists()):
                            row_str += f" {'N/A':>7s}"
                            continue
                        X_tgt = np.load(train_path)
                        y_tgt = np.load(labels_path)
                    else:
                        row_str += f" {'N/A':>7s}"
                        continue

                    if len(np.unique(y_tgt)) < 2:
                        row_str += f" {'N/A':>7s}"
                        continue

                    w_tgt = train_lr_probe(X_tgt, y_tgt, args.seed)
                    cos_sim = cosine_similarity(w_en, w_tgt)
                    angle_deg = float(np.degrees(np.arccos(np.clip(abs(cos_sim), -1, 1))))
                    subspace_angles[(layer, lang)] = {
                        "cosine_similarity": cos_sim,
                        "angle_degrees": angle_deg,
                    }
                    row_str += f" {cos_sim:>7.4f}"

                print(row_str)
        else:
            print("No activations available for training probes. Skipping.")

    # ==================================================================
    # Save outputs
    # ==================================================================
    out = Path(args.output_dir)

    # CKA matrix
    cka_matrix_dict = {}
    for (layer, lang), val in sorted(cka_matrix.items()):
        cka_matrix_dict.setdefault(str(layer), {})[lang] = val
    with open(out / "cka_matrix.json", "w") as f:
        json.dump(cka_matrix_dict, f, indent=2)

    # CKA matrix CSV
    with open(out / "cka_matrix.csv", "w") as f:
        f.write("layer," + ",".join(languages) + "\n")
        for layer in layers:
            vals = [str(cka_matrix.get((layer, l), "")) for l in languages]
            f.write(f"{layer}," + ",".join(vals) + "\n")

    # Same-layer correlation
    with open(out / "same_layer_corr.json", "w") as f:
        json.dump({str(k): v for k, v in same_layer_corr.items()}, f, indent=2)

    # Partial correlation
    with open(out / "partial_corr.json", "w") as f:
        json.dump(partial_corr_results, f, indent=2)

    # Per-language correlation
    with open(out / "per_lang_corr.json", "w") as f:
        json.dump(per_lang_corr, f, indent=2)

    # Subspace angles
    sa_dict = {}
    for (layer, lang), val in sorted(subspace_angles.items()):
        sa_dict.setdefault(str(layer), {})[lang] = val
    with open(out / "subspace_angles.json", "w") as f:
        json.dump(sa_dict, f, indent=2)

    # Subspace angles CSV
    if subspace_angles:
        with open(out / "subspace_angles.csv", "w") as f:
            f.write("layer," + ",".join(languages) + "\n")
            for layer in layers:
                vals = []
                for l in languages:
                    sa = subspace_angles.get((layer, l))
                    vals.append(f"{sa['cosine_similarity']:.6f}" if sa else "")
                f.write(f"{layer}," + ",".join(vals) + "\n")

    # Bootstrap CIs
    boot_dict = {
        "cka": {f"{layer}_{lang}": list(ci) for (layer, lang), ci in cka_boot_cis.items()},
        "same_layer_corr": {str(l): {
            "ci_cka_degradation": v["ci_cka_degradation"],
            "ci_cka_zs_auroc": v["ci_cka_zs_auroc"],
        } for l, v in same_layer_corr.items()},
        "partial_corr": partial_corr_results.get("partial_spearman_ci", []),
        "per_lang_corr": {l: v["ci"] for l, v in per_lang_corr.items()},
    }
    with open(out / "bootstrap_cis.json", "w") as f:
        json.dump(boot_dict, f, indent=2)

    # Human-readable report
    elapsed = time.time() - t0
    lines = [
        f"CKA Analysis Report — {args.model_name}",
        f"Elapsed: {elapsed:.1f}s",
        f"Layers: {layers}",
        f"Languages: {languages}",
        f"Bootstrap: {args.n_bootstrap} resamples",
        "",
    ]

    lines.append("--- CKA Matrix ---")
    lines.append(f"{'Layer':>5s}" + "".join(f" {l:>7s}" for l in languages))
    for layer in layers:
        row = f"{layer:>5d}"
        for l in languages:
            v = cka_matrix.get((layer, l))
            row += f" {v:>7.4f}" if v is not None else f" {'':>7s}"
        lines.append(row)
    lines.append("")

    if same_layer_corr:
        lines.append("--- Same-layer cross-language Spearman ---")
        lines.append(f"{'Layer':>5s} {'n':>3s} {'ρ(CKA,deg)':>11s} {'p':>8s}")
        for layer, v in sorted(same_layer_corr.items()):
            sig = "*" if v["p_cka_degradation"] < 0.05 else ""
            lines.append(f"{layer:>5d} {v['n']:>3d} {v['rho_cka_degradation']:>+10.4f}{sig}"
                         f" {v['p_cka_degradation']:>8.4f}")
        lines.append("")

    if partial_corr_results:
        lines.append("--- Partial Spearman ρ(CKA, degradation | depth) ---")
        lines.append(f"  N = {partial_corr_results['n_observations']}")
        lines.append(f"  Full ρ:    {partial_corr_results['full_spearman_rho']:+.4f}"
                     f" (p={partial_corr_results['full_spearman_p']:.4f})")
        lines.append(f"  Partial ρ: {partial_corr_results['partial_spearman_rho']:+.4f}"
                     f" (p={partial_corr_results['partial_spearman_p']:.4f})"
                     f"  CI={partial_corr_results['partial_spearman_ci']}")
        if partial_corr_results["partial_spearman_p"] < 0.05:
            lines.append("  => CKA has independent explanatory power beyond depth")
        else:
            lines.append("  => Partial ρ not significant; CKA may be a proxy for depth")
        lines.append("")

    if per_lang_corr:
        lines.append("--- Per-language Spearman (CKA vs ZS AUROC) ---")
        lines.append(f"{'Lang':>6s} {'n':>3s} {'ρ':>7s} {'p':>8s}")
        for lang, v in sorted(per_lang_corr.items()):
            sig = "*" if v["p_value"] < 0.05 else ""
            lines.append(f"{lang:>6s} {v['n_layers']:>3d} {v['rho']:>+7.4f} {v['p_value']:>8.4f}{sig}")
        lines.append("")

    if subspace_angles:
        lines.append("--- Subspace angles (cosine similarity) ---")
        lines.append(f"{'Layer':>5s}" + "".join(f" {l:>7s}" for l in languages))
        for layer in layers:
            row = f"{layer:>5d}"
            for l in languages:
                sa = subspace_angles.get((layer, l))
                row += f" {sa['cosine_similarity']:>7.4f}" if sa else f" {'':>7s}"
            lines.append(row)
        lines.append("")

    with open(out / "report.txt", "w") as f:
        f.write("\n".join(lines))

    print(f"\nResults saved to {args.output_dir}/")
    print(f"Total elapsed: {elapsed:.1f}s")


if __name__ == "__main__":
    main()
