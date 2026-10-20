#!/usr/bin/env python3
"""exp-019: Trained Verifier Baseline (Logistic Regression on 5 confidence signals).

Sample-level LR verifier with LOO-CV to close the oracle gap.
Compares supervised selection F1 with unsupervised single-signal baselines.
"""

import json
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import LeaveOneOut, StratifiedKFold, cross_val_predict
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')
from consistency import (
    _ner_soft_jaccard_pair,
    _extract_surface_keys,
    structural_consistency_soft_jaccard,
    fleiss_kappa_surface,
)
from evaluation import per_instance_f1

BASE = "/root/autodl-tmp/struct_self_consist_ie"
OUT_DIR = Path(f"{BASE}/output/exp_019_trained_verifier")
OUT_DIR.mkdir(parents=True, exist_ok=True)

SEEDS = [42, 123, 789]
SEED_PATHS = {
    42: f"{BASE}/output/exp_012_rerun_1024/samples.jsonl",
    123: f"{BASE}/output/exp_018_qwen_scierc_seed123/samples.jsonl",
    789: f"{BASE}/output/exp_022_seed789/samples.jsonl",
}
SUBTASK = "ner"
SIGNALS = ["SJ", "FK", "LP", "EM", "VC"]


def load_data(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


# ── Per-sample signal computations (reused from analyze_3seed.py) ──

def compute_sample_sj_scores(instance):
    samples = instance["samples"]
    N = len(samples)
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            s = _ner_soft_jaccard_pair(
                samples[i].get("entities", []),
                samples[j].get("entities", []),
            )
            matrix[i][j] = s
            matrix[j][i] = s
    np.fill_diagonal(matrix, 1.0)
    return [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]


def compute_sample_surface_scores(instance):
    samples = instance["samples"]
    N = len(samples)
    key_sets = [frozenset(_extract_surface_keys(s, SUBTASK)) for s in samples]
    matrix = np.zeros((N, N))
    for i in range(N):
        for j in range(i + 1, N):
            union = len(key_sets[i] | key_sets[j])
            inter = len(key_sets[i] & key_sets[j])
            s = inter / union if union > 0 else 1.0
            matrix[i][j] = s
            matrix[j][i] = s
    np.fill_diagonal(matrix, 1.0)
    fk_scores = [float(np.mean([matrix[k][j] for j in range(N) if j != k])) for k in range(N)]
    return fk_scores, key_sets


def compute_sample_voting_conf(key_sets, N):
    all_keys = set()
    for ks in key_sets:
        all_keys |= ks
    if not all_keys:
        return [1.0] * N
    key_freq = {}
    for k in all_keys:
        key_freq[k] = sum(1 for ks in key_sets if k in ks) / N
    scores = []
    for ks in key_sets:
        if not ks:
            scores.append(0.0)
        else:
            scores.append(float(np.mean([key_freq[k] for k in ks])))
    return scores


def compute_sample_em_scores(key_sets):
    counter = Counter(key_sets)
    return [counter[ks] / len(key_sets) for ks in key_sets]


def compute_sample_logprobs(instance):
    lps = []
    for s in instance["samples"]:
        lp = s.get("mean_logprob")
        if lp is None:
            lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
        lps.append(lp)
    return lps


def compute_instance_signals(instance):
    samples = instance["samples"]
    N = len(samples)
    sj = structural_consistency_soft_jaccard(samples, subtask=SUBTASK)
    fk = fleiss_kappa_surface(samples, subtask=SUBTASK)

    counter = Counter()
    for s in samples:
        for e in s.get("entities", []):
            counter[(e["text"], e["type"])] += 1
    rates = [v / N for v in counter.values()] if counter else [0.0]
    vc = float(np.mean(rates))

    keys = [frozenset((e["text"], e["type"]) for e in s.get("entities", [])) for s in samples]
    c = Counter(keys)
    em = c.most_common(1)[0][1] / N if keys else 0.0

    logprobs = [s.get("mean_logprob") for s in samples if s.get("mean_logprob") is not None]
    logprobs = [lp for lp in logprobs if np.isfinite(lp)]
    lp = float(np.mean(logprobs)) if logprobs else float("nan")

    return {"SJ": sj, "FK": fk, "VC": vc, "EM": em, "LP": lp}


# ── Core analysis for one seed ──

def analyze_seed(seed):
    print(f"\n{'='*60}")
    print(f"Seed {seed}")
    print(f"{'='*60}")

    path = SEED_PATHS[seed]
    data = load_data(path)
    instances = [d for d in data if len(d["gold"].get("entities", [])) > 0]
    N_samples = len(instances[0]["samples"])
    print(f"  {len(instances)} instances, N={N_samples}")

    # ── Compute per-sample features and F1s ──
    all_sample_features = []  # list of (n_instances, N_samples, 5)
    all_sample_f1s = []       # list of (n_instances, N_samples)
    greedy_f1s = []
    oracle_f1s = []

    # Per-instance signals for instance-level AUROC
    instance_signals = []

    t0 = time.time()
    for idx, inst in enumerate(instances):
        samples = inst["samples"]
        gold = inst["gold"]
        greedy = inst.get("greedy", samples[0])
        N = len(samples)

        g_f1 = per_instance_f1(greedy, gold, subtask=SUBTASK)
        greedy_f1s.append(g_f1)

        sample_f1s = [per_instance_f1(s, gold, subtask=SUBTASK) for s in samples]
        oracle_f1s.append(max(sample_f1s))
        all_sample_f1s.append(sample_f1s)

        # Per-sample signals
        sj_scores = compute_sample_sj_scores(inst)
        fk_scores, key_sets = compute_sample_surface_scores(inst)
        vc_scores = compute_sample_voting_conf(key_sets, N)
        em_scores = compute_sample_em_scores(key_sets)
        lp_scores = compute_sample_logprobs(inst)

        features = np.array([
            [sj_scores[k], fk_scores[k], lp_scores[k], em_scores[k], vc_scores[k]]
            for k in range(N)
        ])
        all_sample_features.append(features)

        inst_sig = compute_instance_signals(inst)
        instance_signals.append(inst_sig)

    elapsed = time.time() - t0
    print(f"  Signal computation: {elapsed:.1f}s")

    n_inst = len(instances)
    greedy_f1_mean = float(np.mean(greedy_f1s))
    oracle_f1_mean = float(np.mean(oracle_f1s))

    # ── Unsupervised baselines (single-signal selection) ──
    unsup_selection_f1 = {}
    for sig_idx, sig in enumerate(SIGNALS):
        sel_f1s = []
        for i in range(n_inst):
            best_idx = int(np.argmax(all_sample_features[i][:, sig_idx]))
            sel_f1s.append(all_sample_f1s[i][best_idx])
        unsup_selection_f1[sig] = float(np.mean(sel_f1s))

    print(f"\n  Greedy F1:  {greedy_f1_mean:.4f}")
    print(f"  Oracle F1:  {oracle_f1_mean:.4f}")
    for sig in SIGNALS:
        print(f"  {sig} sel F1: {unsup_selection_f1[sig]:.4f}")

    # ── Sample-level supervised verifier (LOO-CV at instance level) ──
    # Flatten: each sample is a training example
    # X: [SJ, FK, LP, EM, VC], y: sample F1
    # For selection: train on all other instances, predict on held-out instance,
    #   pick sample with highest predicted probability of being "good"

    print("\n  Training sample-level LR verifier (LOO-CV)...")
    t0 = time.time()

    X_all = np.vstack(all_sample_features)  # (n_inst * N, 5)
    y_f1_all = np.concatenate(all_sample_f1s)  # (n_inst * N,)

    # Binary label: sample F1 > median across ALL samples
    median_f1 = np.median(y_f1_all)
    y_bin_all = (y_f1_all > median_f1).astype(int)

    N = N_samples
    lr_sel_f1s = []

    for i in range(n_inst):
        # Train indices: all samples except instance i
        train_mask = np.ones(n_inst * N, dtype=bool)
        train_mask[i * N : (i + 1) * N] = False
        X_train = X_all[train_mask]
        y_train = y_bin_all[train_mask]

        X_test = X_all[i * N : (i + 1) * N]

        scaler = StandardScaler()
        X_train_s = scaler.fit_transform(X_train)
        X_test_s = scaler.transform(X_test)

        # Handle edge case: if all train labels are same class
        if len(np.unique(y_train)) < 2:
            best_idx = 0
        else:
            lr = LogisticRegression(max_iter=1000, random_state=42)
            lr.fit(X_train_s, y_train)
            probs = lr.predict_proba(X_test_s)[:, 1]
            best_idx = int(np.argmax(probs))

        lr_sel_f1s.append(all_sample_f1s[i][best_idx])

    lr_selection_f1 = float(np.mean(lr_sel_f1s))
    elapsed = time.time() - t0
    print(f"  LOO-CV done: {elapsed:.1f}s")
    print(f"  LR Selection F1: {lr_selection_f1:.4f}")

    # ── Also try 5-fold CV for selection (faster, as sanity check) ──
    print("  Training sample-level LR verifier (5-fold CV)...")
    from sklearn.model_selection import KFold
    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    lr_sel_f1s_5fold = [0.0] * n_inst

    for train_idx, test_idx in kf.split(range(n_inst)):
        train_mask = np.zeros(n_inst * N, dtype=bool)
        for ti in train_idx:
            train_mask[ti * N : (ti + 1) * N] = True
        X_train = X_all[train_mask]
        y_train = y_bin_all[train_mask]

        scaler = StandardScaler()
        X_train_s = scaler.fit_transform(X_train)

        lr = LogisticRegression(max_iter=1000, random_state=42)
        if len(np.unique(y_train)) < 2:
            for ti in test_idx:
                lr_sel_f1s_5fold[ti] = all_sample_f1s[ti][0]
            continue
        lr.fit(X_train_s, y_train)

        for ti in test_idx:
            X_test = X_all[ti * N : (ti + 1) * N]
            X_test_s = scaler.transform(X_test)
            probs = lr.predict_proba(X_test_s)[:, 1]
            best_idx = int(np.argmax(probs))
            lr_sel_f1s_5fold[ti] = all_sample_f1s[ti][best_idx]

    lr_selection_f1_5fold = float(np.mean(lr_sel_f1s_5fold))
    print(f"  LR Selection F1 (5-fold): {lr_selection_f1_5fold:.4f}")

    # ── Instance-level AUROC (LOO-CV) ──
    print("\n  Instance-level LR AUROC (LOO-CV)...")
    X_inst = np.array([[instance_signals[i][sig] for sig in SIGNALS] for i in range(n_inst)])
    # Handle NaN in LP
    nan_mask = np.isnan(X_inst)
    if nan_mask.any():
        col_means = np.nanmean(X_inst, axis=0)
        for c in range(X_inst.shape[1]):
            X_inst[np.isnan(X_inst[:, c]), c] = col_means[c]

    y_inst_binary = (np.array(greedy_f1s) > np.median(greedy_f1s)).astype(int)

    scaler_inst = StandardScaler()
    X_inst_s = scaler_inst.fit_transform(X_inst)

    loo = LeaveOneOut()
    lr_inst = LogisticRegression(max_iter=1000, random_state=42)
    y_prob_loo = cross_val_predict(lr_inst, X_inst_s, y_inst_binary, cv=loo, method='predict_proba')[:, 1]
    auroc_loo = roc_auc_score(y_inst_binary, y_prob_loo)

    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    y_prob_5fold = cross_val_predict(lr_inst, X_inst_s, y_inst_binary, cv=skf, method='predict_proba')[:, 1]
    auroc_5fold = roc_auc_score(y_inst_binary, y_prob_5fold)

    # Single-signal AUROCs for comparison
    single_aurocs = {}
    for sig_idx, sig in enumerate(SIGNALS):
        try:
            single_aurocs[sig] = roc_auc_score(y_inst_binary, X_inst[:, sig_idx])
        except ValueError:
            single_aurocs[sig] = float("nan")

    print(f"  LR AUROC (LOO): {auroc_loo:.4f}")
    print(f"  LR AUROC (5-fold): {auroc_5fold:.4f}")
    for sig in SIGNALS:
        print(f"  {sig} AUROC: {single_aurocs[sig]:.4f}")

    # ── Feature importance ──
    lr_full = LogisticRegression(max_iter=1000, random_state=42)
    lr_full.fit(X_inst_s, y_inst_binary)
    importance = {sig: round(float(lr_full.coef_[0][i]), 4) for i, sig in enumerate(SIGNALS)}
    print(f"\n  Feature importance (coefs): {importance}")

    # ── Ablation: leave-one-signal-out ──
    print("\n  Ablation (leave-one-signal-out AUROC)...")
    ablation = {}
    for drop_idx, drop_sig in enumerate(SIGNALS):
        keep_idx = [j for j in range(5) if j != drop_idx]
        X_abl = X_inst_s[:, keep_idx]
        lr_abl = LogisticRegression(max_iter=1000, random_state=42)
        y_prob_abl = cross_val_predict(lr_abl, X_abl, y_inst_binary, cv=loo, method='predict_proba')[:, 1]
        auroc_abl = roc_auc_score(y_inst_binary, y_prob_abl)
        drop_val = auroc_loo - auroc_abl
        ablation[drop_sig] = {"auroc_without": round(auroc_abl, 4), "delta": round(drop_val, 4)}
        print(f"    w/o {drop_sig}: AUROC={auroc_abl:.4f} (Δ={drop_val:+.4f})")

    # ── Learning curve ──
    print("\n  Learning curve...")
    fractions = [0.1, 0.25, 0.5, 0.75, 1.0]
    learning_curve = {}
    rng = np.random.RandomState(42)
    for frac in fractions:
        n_train = max(int(n_inst * frac), 10)
        n_repeats = 10 if frac < 1.0 else 1
        aurocs_rep = []
        for rep in range(n_repeats):
            if frac < 1.0:
                idx_sub = rng.choice(n_inst, n_train, replace=False)
            else:
                idx_sub = np.arange(n_inst)
            X_sub = X_inst_s[idx_sub]
            y_sub = y_inst_binary[idx_sub]
            if len(np.unique(y_sub)) < 2:
                continue
            lr_lc = LogisticRegression(max_iter=1000, random_state=42)
            if frac < 1.0:
                cv_lc = StratifiedKFold(n_splits=min(5, n_train), shuffle=True, random_state=rep)
            else:
                cv_lc = loo
            try:
                y_prob_lc = cross_val_predict(lr_lc, X_sub, y_sub, cv=cv_lc, method='predict_proba')[:, 1]
                aurocs_rep.append(roc_auc_score(y_sub, y_prob_lc))
            except ValueError:
                pass
        if aurocs_rep:
            learning_curve[str(frac)] = {
                "mean_auroc": round(float(np.mean(aurocs_rep)), 4),
                "std_auroc": round(float(np.std(aurocs_rep)), 4),
                "n_train": n_train,
            }
            print(f"    {frac*100:.0f}% ({n_train}): AUROC={np.mean(aurocs_rep):.4f}±{np.std(aurocs_rep):.4f}")

    return {
        "n_instances": n_inst,
        "n_samples": N_samples,
        "greedy_f1": round(greedy_f1_mean, 4),
        "oracle_f1": round(oracle_f1_mean, 4),
        "unsup_selection_f1": {k: round(v, 4) for k, v in unsup_selection_f1.items()},
        "lr_selection_f1_loo": round(lr_selection_f1, 4),
        "lr_selection_f1_5fold": round(lr_selection_f1_5fold, 4),
        "lr_auroc_loo": round(auroc_loo, 4),
        "lr_auroc_5fold": round(auroc_5fold, 4),
        "single_signal_aurocs": {k: round(v, 4) for k, v in single_aurocs.items()},
        "feature_importance": importance,
        "ablation": ablation,
        "learning_curve": learning_curve,
    }


def main():
    print("=" * 60)
    print("exp-019: Trained Verifier Baseline (Logistic Regression)")
    print("=" * 60)

    all_results = {}
    for seed in SEEDS:
        all_results[seed] = analyze_seed(seed)

    # ── Aggregated across seeds ──
    print(f"\n{'='*60}")
    print("AGGREGATED (3-seed mean ± std)")
    print(f"{'='*60}")

    agg = {}

    # Selection F1
    lr_sel_vals = [all_results[s]["lr_selection_f1_loo"] for s in SEEDS]
    greedy_vals = [all_results[s]["greedy_f1"] for s in SEEDS]
    oracle_vals = [all_results[s]["oracle_f1"] for s in SEEDS]

    agg["lr_selection_f1_loo"] = {
        "mean": round(float(np.mean(lr_sel_vals)), 4),
        "std": round(float(np.std(lr_sel_vals, ddof=1)), 4),
        "per_seed": {s: all_results[s]["lr_selection_f1_loo"] for s in SEEDS},
    }
    agg["greedy_f1"] = {
        "mean": round(float(np.mean(greedy_vals)), 4),
        "std": round(float(np.std(greedy_vals, ddof=1)), 4),
    }
    agg["oracle_f1"] = {
        "mean": round(float(np.mean(oracle_vals)), 4),
        "std": round(float(np.std(oracle_vals, ddof=1)), 4),
    }

    # Gap closure
    greedy_mean = np.mean(greedy_vals)
    oracle_mean = np.mean(oracle_vals)
    lr_sel_mean = np.mean(lr_sel_vals)
    gap = oracle_mean - greedy_mean
    lr_gain = lr_sel_mean - greedy_mean
    gap_closure = lr_gain / gap * 100 if gap > 0 else 0
    agg["gap_closure_pct"] = round(gap_closure, 1)
    agg["oracle_gap"] = round(float(gap), 4)
    agg["lr_gain_over_greedy"] = round(float(lr_gain), 4)

    # Unsup selection F1
    for sig in SIGNALS:
        vals = [all_results[s]["unsup_selection_f1"][sig] for s in SEEDS]
        agg[f"unsup_{sig}_selection_f1"] = {
            "mean": round(float(np.mean(vals)), 4),
            "std": round(float(np.std(vals, ddof=1)), 4),
        }

    # Best unsupervised
    best_unsup_sig = max(SIGNALS, key=lambda sig: np.mean([all_results[s]["unsup_selection_f1"][sig] for s in SEEDS]))
    best_unsup_f1 = np.mean([all_results[s]["unsup_selection_f1"][best_unsup_sig] for s in SEEDS])
    agg["best_unsup_signal"] = best_unsup_sig
    agg["best_unsup_selection_f1"] = round(float(best_unsup_f1), 4)
    agg["lr_vs_best_unsup"] = round(float(lr_sel_mean - best_unsup_f1), 4)

    # AUROC
    lr_auroc_vals = [all_results[s]["lr_auroc_loo"] for s in SEEDS]
    agg["lr_auroc_loo"] = {
        "mean": round(float(np.mean(lr_auroc_vals)), 4),
        "std": round(float(np.std(lr_auroc_vals, ddof=1)), 4),
    }
    for sig in SIGNALS:
        vals = [all_results[s]["single_signal_aurocs"][sig] for s in SEEDS]
        agg[f"single_{sig}_auroc"] = {
            "mean": round(float(np.mean(vals)), 4),
            "std": round(float(np.std(vals, ddof=1)), 4),
        }

    best_auroc_sig = max(SIGNALS, key=lambda sig: np.mean([all_results[s]["single_signal_aurocs"][sig] for s in SEEDS]))
    best_auroc_val = np.mean([all_results[s]["single_signal_aurocs"][best_auroc_sig] for s in SEEDS])
    agg["best_single_auroc_signal"] = best_auroc_sig
    agg["best_single_auroc"] = round(float(best_auroc_val), 4)
    agg["lr_auroc_vs_best_single"] = round(float(np.mean(lr_auroc_vals) - best_auroc_val), 4)

    # Print summary
    print(f"\n  Greedy F1:         {agg['greedy_f1']['mean']:.4f} ± {agg['greedy_f1']['std']:.4f}")
    print(f"  Oracle F1:         {agg['oracle_f1']['mean']:.4f} ± {agg['oracle_f1']['std']:.4f}")
    print(f"  Oracle gap:        {agg['oracle_gap']:.4f}")
    print(f"\n  Selection F1:")
    for sig in SIGNALS:
        v = agg[f"unsup_{sig}_selection_f1"]
        print(f"    {sig} (unsup):    {v['mean']:.4f} ± {v['std']:.4f}")
    print(f"    Best unsup ({best_unsup_sig}): {agg['best_unsup_selection_f1']:.4f}")
    print(f"    LR (supervised):  {agg['lr_selection_f1_loo']['mean']:.4f} ± {agg['lr_selection_f1_loo']['std']:.4f}")
    print(f"    LR vs best unsup: {agg['lr_vs_best_unsup']:+.4f}")
    print(f"    Gap closure:      {agg['gap_closure_pct']:.1f}%")

    print(f"\n  Instance-level AUROC:")
    for sig in SIGNALS:
        v = agg[f"single_{sig}_auroc"]
        print(f"    {sig}:             {v['mean']:.4f} ± {v['std']:.4f}")
    print(f"    Best single ({best_auroc_sig}): {agg['best_single_auroc']:.4f}")
    print(f"    LR:               {agg['lr_auroc_loo']['mean']:.4f} ± {agg['lr_auroc_loo']['std']:.4f}")
    print(f"    LR vs best:       {agg['lr_auroc_vs_best_single']:+.4f}")

    # ── Save results ──
    full_results = {
        "per_seed": {str(s): all_results[s] for s in SEEDS},
        "aggregated": agg,
    }
    results_path = OUT_DIR / "results.json"
    with open(results_path, "w") as f:
        json.dump(full_results, f, indent=2)
    print(f"\nSaved: {results_path}")

    # ── Feature importance ──
    fi = {}
    for sig in SIGNALS:
        vals = [all_results[s]["feature_importance"][sig] for s in SEEDS]
        fi[sig] = {"mean": round(float(np.mean(vals)), 4), "std": round(float(np.std(vals, ddof=1)), 4),
                    "per_seed": {str(s): all_results[s]["feature_importance"][sig] for s in SEEDS}}
    fi_path = OUT_DIR / "feature_importance.json"
    with open(fi_path, "w") as f:
        json.dump(fi, f, indent=2)
    print(f"Saved: {fi_path}")

    # ── Generate report.md ──
    lines = []
    lines.append("# exp-019: Trained Verifier Baseline (Logistic Regression)")
    lines.append("")
    lines.append(f"Seeds: {SEEDS}, Dataset: SciERC NER, N=8, Qwen2.5-7B-Instruct")
    lines.append("")

    lines.append("## 1. Selection F1 Comparison")
    lines.append("")
    lines.append("| Method | seed42 | seed123 | seed789 | Mean ± σ |")
    lines.append("|--------|--------|---------|---------|----------|")
    lines.append(f"| Greedy | {all_results[42]['greedy_f1']:.4f} | {all_results[123]['greedy_f1']:.4f} | {all_results[789]['greedy_f1']:.4f} | {agg['greedy_f1']['mean']:.4f} ± {agg['greedy_f1']['std']:.4f} |")
    for sig in SIGNALS:
        vals = [all_results[s]["unsup_selection_f1"][sig] for s in SEEDS]
        m = agg[f"unsup_{sig}_selection_f1"]
        lines.append(f"| {sig} (unsup) | {vals[0]:.4f} | {vals[1]:.4f} | {vals[2]:.4f} | {m['mean']:.4f} ± {m['std']:.4f} |")
    lr_vals = [all_results[s]["lr_selection_f1_loo"] for s in SEEDS]
    lines.append(f"| **LR (supervised)** | {lr_vals[0]:.4f} | {lr_vals[1]:.4f} | {lr_vals[2]:.4f} | **{agg['lr_selection_f1_loo']['mean']:.4f} ± {agg['lr_selection_f1_loo']['std']:.4f}** |")
    lines.append(f"| Oracle | {all_results[42]['oracle_f1']:.4f} | {all_results[123]['oracle_f1']:.4f} | {all_results[789]['oracle_f1']:.4f} | {agg['oracle_f1']['mean']:.4f} ± {agg['oracle_f1']['std']:.4f} |")
    lines.append("")
    lines.append(f"Oracle gap: {agg['oracle_gap']:.4f}")
    lines.append(f"LR gain over greedy: {agg['lr_gain_over_greedy']:+.4f}")
    lines.append(f"LR vs best unsupervised ({best_unsup_sig}): {agg['lr_vs_best_unsup']:+.4f}")
    lines.append(f"Gap closure: {agg['gap_closure_pct']:.1f}%")
    lines.append("")

    lines.append("## 2. Instance-level AUROC")
    lines.append("")
    lines.append("| Method | seed42 | seed123 | seed789 | Mean ± σ |")
    lines.append("|--------|--------|---------|---------|----------|")
    for sig in SIGNALS:
        vals = [all_results[s]["single_signal_aurocs"][sig] for s in SEEDS]
        m = agg[f"single_{sig}_auroc"]
        lines.append(f"| {sig} | {vals[0]:.4f} | {vals[1]:.4f} | {vals[2]:.4f} | {m['mean']:.4f} ± {m['std']:.4f} |")
    auroc_vals = [all_results[s]["lr_auroc_loo"] for s in SEEDS]
    lines.append(f"| **LR (5 signals)** | {auroc_vals[0]:.4f} | {auroc_vals[1]:.4f} | {auroc_vals[2]:.4f} | **{agg['lr_auroc_loo']['mean']:.4f} ± {agg['lr_auroc_loo']['std']:.4f}** |")
    lines.append("")
    lines.append(f"LR vs best single signal ({best_auroc_sig}): {agg['lr_auroc_vs_best_single']:+.4f}")
    lines.append("")

    lines.append("## 3. Feature Importance (LR Coefficients)")
    lines.append("")
    lines.append("| Signal | seed42 | seed123 | seed789 | Mean ± σ |")
    lines.append("|--------|--------|---------|---------|----------|")
    for sig in SIGNALS:
        f_vals = [all_results[s]["feature_importance"][sig] for s in SEEDS]
        lines.append(f"| {sig} | {f_vals[0]:.4f} | {f_vals[1]:.4f} | {f_vals[2]:.4f} | {fi[sig]['mean']:.4f} ± {fi[sig]['std']:.4f} |")
    lines.append("")

    lines.append("## 4. Ablation (Leave-One-Signal-Out AUROC)")
    lines.append("")
    lines.append("| Dropped | seed42 AUROC | seed123 AUROC | seed789 AUROC | Mean Δ |")
    lines.append("|---------|-------------|---------------|---------------|--------|")
    for sig in SIGNALS:
        abl_vals = [all_results[s]["ablation"][sig]["auroc_without"] for s in SEEDS]
        delta_vals = [all_results[s]["ablation"][sig]["delta"] for s in SEEDS]
        mean_delta = np.mean(delta_vals)
        lines.append(f"| w/o {sig} | {abl_vals[0]:.4f} | {abl_vals[1]:.4f} | {abl_vals[2]:.4f} | {mean_delta:+.4f} |")
    lines.append(f"| All 5 | {auroc_vals[0]:.4f} | {auroc_vals[1]:.4f} | {auroc_vals[2]:.4f} | — |")
    lines.append("")

    lines.append("## 5. Learning Curve (Instance-level AUROC)")
    lines.append("")
    lines.append("| % Data | Mean AUROC ± σ |")
    lines.append("|--------|----------------|")
    for frac_str in ["0.1", "0.25", "0.5", "0.75", "1.0"]:
        vals_per_seed = []
        for s in SEEDS:
            lc = all_results[s].get("learning_curve", {}).get(frac_str)
            if lc:
                vals_per_seed.append(lc["mean_auroc"])
        if vals_per_seed:
            lines.append(f"| {float(frac_str)*100:.0f}% | {np.mean(vals_per_seed):.4f} ± {np.std(vals_per_seed, ddof=1) if len(vals_per_seed) > 1 else 0:.4f} |")
    lines.append("")

    lines.append("## 6. Interpretation")
    lines.append("")
    if agg["lr_auroc_vs_best_single"] > 0.01:
        lines.append("- LR AUROC significantly exceeds best single signal → signals carry complementary information.")
    elif agg["lr_auroc_vs_best_single"] > 0:
        lines.append("- LR AUROC marginally exceeds best single signal → limited complementary information in current signals.")
    else:
        lines.append("- LR AUROC does NOT exceed best single signal → signals are largely redundant.")
    lines.append("")
    if agg["lr_vs_best_unsup"] > 0.005:
        lines.append(f"- Supervised LR selection F1 exceeds best unsupervised by {agg['lr_vs_best_unsup']:+.4f} → supervision helps.")
    elif agg["lr_vs_best_unsup"] > 0:
        lines.append(f"- Supervised LR selection F1 marginally exceeds best unsupervised by {agg['lr_vs_best_unsup']:+.4f}.")
    else:
        lines.append(f"- Supervised LR selection F1 does NOT exceed best unsupervised → simple heuristics suffice.")
    lines.append("")
    lines.append(f"- Gap closure: {agg['gap_closure_pct']:.1f}% of the oracle gap closed by supervised LR.")
    lines.append("")

    report_path = OUT_DIR / "report.md"
    with open(report_path, "w") as f:
        f.write("\n".join(lines))
    print(f"Saved: {report_path}")


if __name__ == "__main__":
    main()
