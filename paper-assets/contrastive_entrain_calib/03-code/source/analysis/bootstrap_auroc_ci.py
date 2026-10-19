#!/usr/bin/env python3
"""Bootstrap 95% CI for d_syc AUROC metrics.

Computes bootstrap CIs for:
1. Qwen3-8B 5-fold CV AUROC (style-controlled data, 181 pairs)
2. Qwen3-8B per-strength AUROC (weak/medium/strong)
3. Llama-3-8B 5-fold CV AUROC
4. d_syc vs random baseline AUROC difference
"""

import json
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
import torch
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import StratifiedKFold

N_BOOTSTRAP = 10000
N_FOLDS = 5
SEED = 42


# ── Data loading ──────────────────────────────────────────────────────

def load_pairs(path, act_key="activations"):
    records = torch.load(path, map_location="cpu", weights_only=False)
    pairs = defaultdict(dict)
    for s in records:
        pairs[s["pair_id"]][s["condition"]] = s
    return {
        pid: conds
        for pid, conds in pairs.items()
        if "valid_correction" in conds and "invalid_pressure" in conds
    }


def prepare_arrays(pairs, act_key="activations", pos=None):
    """Pre-extract activations as numpy arrays for speed.

    Returns:
        syc: (n_pairs, n_layers, hidden_dim)
        wr:  (n_pairs, n_layers, hidden_dim)
        domains: list[str]
        strengths: list[str]
        pair_ids: list[str]
    """
    pair_ids = sorted(pairs.keys())
    syc_list, wr_list, domains, strengths = [], [], [], []

    for pid in pair_ids:
        s_act = pairs[pid]["invalid_pressure"][act_key]
        w_act = pairs[pid]["valid_correction"][act_key]
        if pos is not None:
            s_act = s_act[:, pos, :]
            w_act = w_act[:, pos, :]
        syc_list.append(s_act)
        wr_list.append(w_act)
        domains.append(pairs[pid]["valid_correction"]["domain"])
        strengths.append(pairs[pid]["valid_correction"]["evidence_strength"])

    syc = torch.stack(syc_list).numpy().astype(np.float32)
    wr = torch.stack(wr_list).numpy().astype(np.float32)
    return syc, wr, domains, strengths, pair_ids


# ── Core CV + AUROC ──────────────────────────────────────────────────

def cv_auroc(syc, wr, domains_arr, n_folds=N_FOLDS, seed=SEED,
             layer_lo=0, layer_hi=None, return_oof=False):
    """Run stratified 5-fold CV and return mean AUROC (and optionally OOF scores).

    For each fold: compute d_syc from train, search best layer on test, record AUROC.
    """
    n_pairs = syc.shape[0]
    if layer_hi is None:
        layer_hi = syc.shape[1]

    skf = StratifiedKFold(n_splits=n_folds, shuffle=True, random_state=seed)
    fold_aurocs = []
    oof_scores = np.zeros(n_pairs)  # syc_score - wr_score per pair (for OOF)
    oof_syc = np.zeros(n_pairs)
    oof_wr = np.zeros(n_pairs)

    for train_idx, test_idx in skf.split(np.arange(n_pairs), domains_arr):
        d = syc[train_idx].mean(axis=0) - wr[train_idx].mean(axis=0)
        norms = np.linalg.norm(d, axis=-1, keepdims=True)
        d = d / np.maximum(norms, 1e-8)

        # Vectorized scoring: (n_test, n_layers)
        s_test = (syc[test_idx] * d).sum(axis=-1)
        w_test = (wr[test_idx] * d).sum(axis=-1)

        best_auroc = -1.0
        best_layer = layer_lo
        for layer in range(layer_lo, layer_hi):
            scores = np.concatenate([s_test[:, layer], w_test[:, layer]])
            labels = np.concatenate([np.ones(len(test_idx)), np.zeros(len(test_idx))])
            try:
                auroc = roc_auc_score(labels, scores)
                if auroc > best_auroc:
                    best_auroc = auroc
                    best_layer = layer
            except ValueError:
                pass

        fold_aurocs.append(best_auroc)
        oof_syc[test_idx] = s_test[:, best_layer]
        oof_wr[test_idx] = w_test[:, best_layer]

    mean_auroc = float(np.mean(fold_aurocs))

    if return_oof:
        return mean_auroc, fold_aurocs, oof_syc, oof_wr
    return mean_auroc, fold_aurocs


# ── Bootstrap routines ───────────────────────────────────────────────

def bootstrap_cv_auroc(syc, wr, domains_arr, n_bootstrap=N_BOOTSTRAP,
                       seed=SEED, layer_lo=0, layer_hi=None):
    """Bootstrap the 5-fold CV AUROC by resampling pairs."""
    rng = np.random.RandomState(seed)
    n_pairs = syc.shape[0]
    aurocs = []

    for b in range(n_bootstrap):
        boot_idx = rng.choice(n_pairs, size=n_pairs, replace=True)
        boot_domains = domains_arr[boot_idx]

        # Ensure at least 2 unique domain values for stratification
        if len(np.unique(boot_domains)) < N_FOLDS:
            boot_domains = np.arange(n_pairs) % N_FOLDS

        try:
            mean_auc, _ = cv_auroc(
                syc[boot_idx], wr[boot_idx], boot_domains,
                seed=b, layer_lo=layer_lo, layer_hi=layer_hi,
            )
            aurocs.append(mean_auc)
        except Exception:
            pass

        if (b + 1) % 1000 == 0:
            print(f"  bootstrap {b+1}/{n_bootstrap}...", flush=True)

    aurocs = np.array(aurocs)
    return {
        "mean": float(np.mean(aurocs)),
        "std": float(np.std(aurocs)),
        "ci_95_lower": float(np.percentile(aurocs, 2.5)),
        "ci_95_upper": float(np.percentile(aurocs, 97.5)),
        "n_valid": len(aurocs),
    }


def bootstrap_oof_auroc(oof_syc, oof_wr, mask=None,
                         n_bootstrap=N_BOOTSTRAP, seed=SEED):
    """Bootstrap AUROC from OOF predictions by resampling pairs."""
    if mask is not None:
        oof_syc = oof_syc[mask]
        oof_wr = oof_wr[mask]

    n = len(oof_syc)
    if n < 4:
        return None

    rng = np.random.RandomState(seed)
    aurocs = []

    for _ in range(n_bootstrap):
        idx = rng.choice(n, size=n, replace=True)
        scores = np.concatenate([oof_syc[idx], oof_wr[idx]])
        labels = np.concatenate([np.ones(len(idx)), np.zeros(len(idx))])
        try:
            aurocs.append(roc_auc_score(labels, scores))
        except ValueError:
            pass

    aurocs = np.array(aurocs)
    # Point estimate from full data
    full_scores = np.concatenate([oof_syc, oof_wr])
    full_labels = np.concatenate([np.ones(n), np.zeros(n)])
    point_auroc = float(roc_auc_score(full_labels, full_scores))

    return {
        "point_auroc": point_auroc,
        "bootstrap_mean": float(np.mean(aurocs)),
        "std": float(np.std(aurocs)),
        "ci_95_lower": float(np.percentile(aurocs, 2.5)),
        "ci_95_upper": float(np.percentile(aurocs, 97.5)),
        "n_pairs": n,
        "n_valid": len(aurocs),
    }


def bootstrap_auroc_difference(oof_syc_d, oof_wr_d, oof_syc_r, oof_wr_r,
                                n_bootstrap=N_BOOTSTRAP, seed=SEED):
    """Bootstrap CI for AUROC(d_syc) - AUROC(random)."""
    n = len(oof_syc_d)
    rng = np.random.RandomState(seed)
    diffs = []

    for _ in range(n_bootstrap):
        idx = rng.choice(n, size=n, replace=True)
        scores_d = np.concatenate([oof_syc_d[idx], oof_wr_d[idx]])
        scores_r = np.concatenate([oof_syc_r[idx], oof_wr_r[idx]])
        labels = np.concatenate([np.ones(len(idx)), np.zeros(len(idx))])
        try:
            a_d = roc_auc_score(labels, scores_d)
            a_r = roc_auc_score(labels, scores_r)
            diffs.append(a_d - a_r)
        except ValueError:
            pass

    diffs = np.array(diffs)
    return {
        "mean_diff": float(np.mean(diffs)),
        "ci_95_lower": float(np.percentile(diffs, 2.5)),
        "ci_95_upper": float(np.percentile(diffs, 97.5)),
        "p_greater_zero": float(np.mean(diffs > 0)),
        "n_valid": len(diffs),
    }


def random_direction_oof(syc, wr, domains_arr, n_random=200, seed=SEED,
                          layer_lo=0, layer_hi=None):
    """Compute mean AUROC of random directions (matched procedure to d_syc)."""
    rng = np.random.RandomState(seed)
    n_pairs, n_layers, hidden = syc.shape
    if layer_hi is None:
        layer_hi = n_layers

    skf = StratifiedKFold(n_splits=N_FOLDS, shuffle=True, random_state=seed)
    folds = list(skf.split(np.arange(n_pairs), domains_arr))

    random_aurocs = []
    best_oof_syc = np.zeros(n_pairs)
    best_oof_wr = np.zeros(n_pairs)
    best_overall = -1.0

    for r in range(n_random):
        d_rand = rng.randn(n_layers, hidden).astype(np.float32)
        norms = np.linalg.norm(d_rand, axis=-1, keepdims=True)
        d_rand = d_rand / np.maximum(norms, 1e-8)

        fold_aurocs = []
        tmp_syc = np.zeros(n_pairs)
        tmp_wr = np.zeros(n_pairs)

        for train_idx, test_idx in folds:
            s_test = (syc[test_idx] * d_rand).sum(axis=-1)
            w_test = (wr[test_idx] * d_rand).sum(axis=-1)

            best_a = -1.0
            best_l = layer_lo
            for layer in range(layer_lo, layer_hi):
                scores = np.concatenate([s_test[:, layer], w_test[:, layer]])
                labels = np.concatenate([np.ones(len(test_idx)), np.zeros(len(test_idx))])
                try:
                    a = roc_auc_score(labels, scores)
                    if a > best_a:
                        best_a = a
                        best_l = layer
                except ValueError:
                    pass

            fold_aurocs.append(best_a)
            tmp_syc[test_idx] = s_test[:, best_l]
            tmp_wr[test_idx] = w_test[:, best_l]

        mean_a = np.mean(fold_aurocs)
        random_aurocs.append(mean_a)
        if mean_a > best_overall:
            best_overall = mean_a
            best_oof_syc = tmp_syc.copy()
            best_oof_wr = tmp_wr.copy()

    return {
        "mean_auroc": float(np.mean(random_aurocs)),
        "std": float(np.std(random_aurocs)),
        "max_auroc": float(np.max(random_aurocs)),
        "n_random": n_random,
    }, best_oof_syc, best_oof_wr


# ── Main ──────────────────────────────────────────────────────────────

def main():
    t0 = time.time()
    results = {}

    # ── Qwen3-8B (exp001, 181 pairs, style-controlled) ────────────
    print("Loading Qwen3-8B data (181 pairs)...")
    qwen_pairs = load_pairs(
        "/root/contrastive_entrain_calib/results/exp001/activations.pt",
        act_key="activations",
    )
    syc_q, wr_q, domains_q, strengths_q, pids_q = prepare_arrays(
        qwen_pairs, act_key="activations", pos=1,  # asst_first
    )
    domains_q_arr = np.array(domains_q)
    strengths_q_arr = np.array(strengths_q)
    print(f"  {syc_q.shape[0]} pairs, {syc_q.shape[1]} layers, {syc_q.shape[2]} dim")

    # Point estimate: 5-fold CV
    print("Running Qwen 5-fold CV (point estimate)...")
    q_mean, q_folds, q_oof_syc, q_oof_wr = cv_auroc(
        syc_q, wr_q, domains_q_arr, return_oof=True,
    )
    print(f"  Mean CV AUROC = {q_mean:.4f}, folds = {[round(x, 4) for x in q_folds]}")

    results["qwen_cv"] = {
        "point_estimate": q_mean,
        "fold_aurocs": [round(x, 6) for x in q_folds],
        "fold_std": float(np.std(q_folds)),
        "n_pairs": int(syc_q.shape[0]),
    }

    # Bootstrap CI via OOF predictions (fast)
    print("Bootstrapping Qwen OOF AUROC (n=10000)...")
    q_oof_ci = bootstrap_oof_auroc(q_oof_syc, q_oof_wr, seed=SEED)
    results["qwen_cv"]["oof_bootstrap"] = q_oof_ci
    print(f"  OOF AUROC = {q_oof_ci['point_auroc']:.4f} "
          f"[{q_oof_ci['ci_95_lower']:.4f}, {q_oof_ci['ci_95_upper']:.4f}]")

    # Per-strength breakdown
    print("Bootstrapping Qwen per-strength AUROC...")
    results["qwen_per_strength"] = {}
    for strength in ["weak", "medium", "strong"]:
        mask = strengths_q_arr == strength
        ci = bootstrap_oof_auroc(q_oof_syc, q_oof_wr, mask=mask, seed=SEED)
        if ci:
            results["qwen_per_strength"][strength] = ci
            print(f"  {strength}: AUROC = {ci['point_auroc']:.4f} "
                  f"[{ci['ci_95_lower']:.4f}, {ci['ci_95_upper']:.4f}] "
                  f"(n={ci['n_pairs']})")

    # Full bootstrap-of-CV (slower but more rigorous)
    print("Bootstrapping Qwen full CV (n=10000, this takes a while)...")
    q_full_ci = bootstrap_cv_auroc(syc_q, wr_q, domains_q_arr, seed=SEED)
    results["qwen_cv"]["full_cv_bootstrap"] = q_full_ci
    print(f"  Full CV bootstrap: {q_full_ci['mean']:.4f} "
          f"[{q_full_ci['ci_95_lower']:.4f}, {q_full_ci['ci_95_upper']:.4f}]")
    print(f"  Elapsed: {time.time() - t0:.1f}s")

    # ── Llama-3-8B (exp012, 181 pairs) ────────────────────────────
    print("\nLoading Llama-3-8B data (181 pairs)...")
    llama_pairs = load_pairs(
        "/root/contrastive_entrain_calib/results/exp012_llama_direction/activations.pt",
        act_key="activation",
    )
    syc_l, wr_l, domains_l, strengths_l, pids_l = prepare_arrays(
        llama_pairs, act_key="activation", pos=None,  # no position dim
    )
    domains_l_arr = np.array(domains_l)
    strengths_l_arr = np.array(strengths_l)
    print(f"  {syc_l.shape[0]} pairs, {syc_l.shape[1]} layers, {syc_l.shape[2]} dim")

    # Point estimate
    print("Running Llama 5-fold CV...")
    l_mean, l_folds, l_oof_syc, l_oof_wr = cv_auroc(
        syc_l, wr_l, domains_l_arr, return_oof=True,
    )
    print(f"  Mean CV AUROC = {l_mean:.4f}, folds = {[round(x, 4) for x in l_folds]}")

    results["llama_cv"] = {
        "point_estimate": l_mean,
        "fold_aurocs": [round(x, 6) for x in l_folds],
        "fold_std": float(np.std(l_folds)),
        "n_pairs": int(syc_l.shape[0]),
    }

    # Bootstrap OOF
    print("Bootstrapping Llama OOF AUROC (n=10000)...")
    l_oof_ci = bootstrap_oof_auroc(l_oof_syc, l_oof_wr, seed=SEED)
    results["llama_cv"]["oof_bootstrap"] = l_oof_ci
    print(f"  OOF AUROC = {l_oof_ci['point_auroc']:.4f} "
          f"[{l_oof_ci['ci_95_lower']:.4f}, {l_oof_ci['ci_95_upper']:.4f}]")

    # Llama per-strength
    print("Bootstrapping Llama per-strength AUROC...")
    results["llama_per_strength"] = {}
    for strength in ["weak", "medium", "strong"]:
        mask = strengths_l_arr == strength
        ci = bootstrap_oof_auroc(l_oof_syc, l_oof_wr, mask=mask, seed=SEED)
        if ci:
            results["llama_per_strength"][strength] = ci
            print(f"  {strength}: AUROC = {ci['point_auroc']:.4f} "
                  f"[{ci['ci_95_lower']:.4f}, {ci['ci_95_upper']:.4f}] "
                  f"(n={ci['n_pairs']})")

    # Full CV bootstrap for Llama
    print("Bootstrapping Llama full CV (n=10000)...")
    l_full_ci = bootstrap_cv_auroc(syc_l, wr_l, domains_l_arr, seed=SEED)
    results["llama_cv"]["full_cv_bootstrap"] = l_full_ci
    print(f"  Full CV bootstrap: {l_full_ci['mean']:.4f} "
          f"[{l_full_ci['ci_95_lower']:.4f}, {l_full_ci['ci_95_upper']:.4f}]")

    # ── d_syc vs random baseline (Qwen) ──────────────────────────
    print("\nComputing random baseline (200 random directions)...")
    rand_stats, rand_oof_syc, rand_oof_wr = random_direction_oof(
        syc_q, wr_q, domains_q_arr, n_random=200, seed=SEED,
    )
    results["random_baseline_qwen"] = rand_stats
    print(f"  Random AUROC: mean={rand_stats['mean_auroc']:.4f}, "
          f"max={rand_stats['max_auroc']:.4f}")

    # Bootstrap difference CI
    print("Bootstrapping d_syc vs random AUROC difference...")
    diff_ci = bootstrap_auroc_difference(
        q_oof_syc, q_oof_wr, rand_oof_syc, rand_oof_wr, seed=SEED,
    )
    results["dsyc_vs_random_qwen"] = {
        "dsyc_auroc": q_oof_ci["point_auroc"],
        "random_auroc": rand_stats["mean_auroc"],
        "difference_ci": diff_ci,
    }
    print(f"  AUROC diff = {diff_ci['mean_diff']:.4f} "
          f"[{diff_ci['ci_95_lower']:.4f}, {diff_ci['ci_95_upper']:.4f}], "
          f"P(diff>0) = {diff_ci['p_greater_zero']:.4f}")

    # ── Save results ──────────────────────────────────────────────
    out_dir = Path("/root/contrastive_entrain_calib/artifacts")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "bootstrap_auroc_ci.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to {out_path}")

    # ── Human-readable summary ────────────────────────────────────
    print("\n" + "=" * 70)
    print("BOOTSTRAP 95% CI SUMMARY (n_bootstrap=10000)")
    print("=" * 70)

    print("\n┌─ Qwen3-8B (style-controlled, 181 pairs) ─────────────────────────┐")
    print(f"│ 5-fold CV AUROC = {q_mean:.4f} (std={np.std(q_folds):.4f})")
    print(f"│ OOF bootstrap:  {q_oof_ci['point_auroc']:.4f} "
          f"[{q_oof_ci['ci_95_lower']:.4f}, {q_oof_ci['ci_95_upper']:.4f}]")
    print(f"│ Full CV bootstrap: {q_full_ci['mean']:.4f} "
          f"[{q_full_ci['ci_95_lower']:.4f}, {q_full_ci['ci_95_upper']:.4f}]")
    print("│")
    print("│ Per-strength (OOF):")
    for s in ["weak", "medium", "strong"]:
        ci = results["qwen_per_strength"].get(s)
        if ci:
            print(f"│   {s:8s}: {ci['point_auroc']:.4f} "
                  f"[{ci['ci_95_lower']:.4f}, {ci['ci_95_upper']:.4f}] (n={ci['n_pairs']})")
    print("└──────────────────────────────────────────────────────────────────┘")

    print("\n┌─ Llama-3-8B (style-controlled, 181 pairs) ────────────────────────┐")
    print(f"│ 5-fold CV AUROC = {l_mean:.4f} (std={np.std(l_folds):.4f})")
    print(f"│ OOF bootstrap:  {l_oof_ci['point_auroc']:.4f} "
          f"[{l_oof_ci['ci_95_lower']:.4f}, {l_oof_ci['ci_95_upper']:.4f}]")
    print(f"│ Full CV bootstrap: {l_full_ci['mean']:.4f} "
          f"[{l_full_ci['ci_95_lower']:.4f}, {l_full_ci['ci_95_upper']:.4f}]")
    print("│")
    print("│ Per-strength (OOF):")
    for s in ["weak", "medium", "strong"]:
        ci = results["llama_per_strength"].get(s)
        if ci:
            print(f"│   {s:8s}: {ci['point_auroc']:.4f} "
                  f"[{ci['ci_95_lower']:.4f}, {ci['ci_95_upper']:.4f}] (n={ci['n_pairs']})")
    print("└──────────────────────────────────────────────────────────────────┘")

    print(f"\n┌─ d_syc vs random baseline (Qwen) ───────────────────────────────┐")
    print(f"│ d_syc AUROC:  {q_oof_ci['point_auroc']:.4f}")
    print(f"│ Random AUROC: {rand_stats['mean_auroc']:.4f} (mean of {rand_stats['n_random']} random dirs)")
    print(f"│ Δ(d_syc - random) = {diff_ci['mean_diff']:.4f} "
          f"[{diff_ci['ci_95_lower']:.4f}, {diff_ci['ci_95_upper']:.4f}]")
    print(f"│ P(d_syc > random) = {diff_ci['p_greater_zero']:.4f}")
    print("└──────────────────────────────────────────────────────────────────┘")

    elapsed = time.time() - t0
    print(f"\nTotal time: {elapsed:.1f}s")


if __name__ == "__main__":
    main()
