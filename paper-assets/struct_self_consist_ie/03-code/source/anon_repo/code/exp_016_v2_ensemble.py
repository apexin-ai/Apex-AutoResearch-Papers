#!/usr/bin/env python3
"""exp-016 v2: Signal Ensemble Analysis on v2 unified inference data.

Uses v2 data: N=16, T=1.0, all 551 instances.
NER: merged samples from seed42 + seed123 (N=32 effective).
RE: exp_008_re_n16_v2 (N=16).

4 configurations: NER full, NER conditional, RE full, RE conditional.

Parts:
  1. Signal correlation matrix (Pearson + Spearman, all 5 signals + F1)
  2. Linear combination grid search (all 10 pairs, step 0.05)
  3. Logistic regression ensemble (10-fold CV)
  4. Best-of-N selection F1

Usage:
    cd /root/autodl-tmp/struct_self_consist_ie
    python code/exp_016_v2_ensemble.py
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import sys
from collections import Counter
from itertools import combinations

import numpy as np
from scipy.stats import spearmanr, pearsonr

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(__file__))

from consistency import (
    compute_all_consistency_scores,
    _ner_soft_jaccard_pair,
    _re_soft_jaccard_pair,
)
from evaluation import per_instance_f1


SIGNAL_NAMES = ["soft_jaccard", "fleiss_kappa", "logprob", "exact_match", "voting_confidence"]


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_samples(path: str) -> list[dict]:
    instances = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                instances.append(json.loads(line))
    return instances


def merge_ner_seeds(seed42_path: str, seed123_path: str) -> list[dict]:
    """Merge NER samples from two seeds. Pool samples (N=32) per instance."""
    insts_42 = load_samples(seed42_path)
    insts_123 = load_samples(seed123_path)
    assert len(insts_42) == len(insts_123), f"Seed count mismatch: {len(insts_42)} vs {len(insts_123)}"

    merged = []
    for i42, i123 in zip(insts_42, insts_123):
        assert i42["id"] == i123["id"], f"ID mismatch: {i42['id']} vs {i123['id']}"
        inst = {
            "id": i42["id"],
            "text": i42["text"],
            "gold": i42["gold"],
            "samples": i42["samples"] + i123["samples"],
            "greedy": i42["greedy"],
        }
        merged.append(inst)
    return merged


# ---------------------------------------------------------------------------
# Signal computation
# ---------------------------------------------------------------------------

def compute_exact_match_rate(instances: list[dict], subtask: str) -> list[float]:
    rates = []
    for inst in instances:
        samples = inst["samples"]
        n = len(samples)
        if n < 2:
            rates.append(1.0)
            continue
        sample_keys = []
        for s in samples:
            if subtask == "ner":
                keys = frozenset((e.get("text", ""), e.get("type", "")) for e in s.get("entities", []))
            elif subtask == "re":
                keys = frozenset((r.get("head", ""), r.get("tail", ""), r.get("type", "")) for r in s.get("relations", []))
            else:
                keys = frozenset()
            sample_keys.append(keys)
        match_count = sum(1 for i in range(n) for j in range(i + 1, n) if sample_keys[i] == sample_keys[j])
        total_pairs = n * (n - 1) // 2
        rates.append(match_count / total_pairs if total_pairs > 0 else 1.0)
    return rates


def compute_voting_confidence(instances: list[dict], subtask: str) -> list[float]:
    confidences = []
    for inst in instances:
        samples = inst["samples"]
        n = len(samples)
        counter: Counter = Counter()
        for s in samples:
            if subtask == "ner":
                for e in s.get("entities", []):
                    counter[(e.get("text", ""), e.get("type", ""))] += 1
            elif subtask == "re":
                for r in s.get("relations", []):
                    counter[(r.get("head", ""), r.get("tail", ""), r.get("type", ""))] += 1
        majority_votes = [v / n for v in counter.values() if v > n / 2]
        confidences.append(float(np.mean(majority_votes)) if majority_votes else 0.0)
    return confidences


def compute_instance_logprob(inst: dict) -> float:
    lps = [s["mean_logprob"] for s in inst.get("samples", []) if "mean_logprob" in s]
    return float(np.mean(lps)) if lps else 0.0


def compute_all_signals(
    instances: list[dict],
    subtask: str,
    mode: str = "conditional",
) -> tuple[list[dict], list[float], dict[str, list[float]]]:
    """Compute all 5 signals + greedy F1.

    mode: "full" (all instances) or "conditional" (gold-nonempty only).
    """
    if mode == "conditional":
        if subtask == "ner":
            mask = [len(inst["gold"].get("entities", [])) > 0 for inst in instances]
        else:
            mask = [len(inst["gold"].get("relations", [])) > 0 for inst in instances]
        filtered = [inst for inst, m in zip(instances, mask) if m]
    else:
        filtered = list(instances)

    f1_values = [per_instance_f1(inst["greedy"], inst["gold"], subtask=subtask) for inst in filtered]

    consistency = compute_all_consistency_scores(filtered, subtask=subtask)
    signals: dict[str, list[float]] = {
        "soft_jaccard": list(consistency["soft_jaccard"]),
        "fleiss_kappa": list(consistency["fleiss_kappa"]),
        "exact_match": compute_exact_match_rate(filtered, subtask),
        "voting_confidence": compute_voting_confidence(filtered, subtask),
    }

    has_logprob = any(
        "mean_logprob" in s
        for inst in filtered[:5]
        for s in inst.get("samples", [])[:1]
    )
    if has_logprob:
        signals["logprob"] = [compute_instance_logprob(inst) for inst in filtered]
    else:
        print(f"  WARNING: logprob unavailable for {subtask}, using zeros")
        signals["logprob"] = [0.0] * len(filtered)

    return filtered, f1_values, signals


# ---------------------------------------------------------------------------
# Part 1: Pairwise signal correlation
# ---------------------------------------------------------------------------

def part1_signal_correlation(
    signals: dict[str, list[float]],
    f1_values: list[float],
    label: str,
) -> dict:
    available = [s for s in SIGNAL_NAMES if s in signals]

    pairwise = {}
    for i, a in enumerate(available):
        for b in available[i + 1:]:
            sa, sb = np.array(signals[a]), np.array(signals[b])
            if np.std(sa) < 1e-12 or np.std(sb) < 1e-12:
                pairwise[f"{a}_vs_{b}"] = {
                    "pearson_r": 0.0, "pearson_p": 1.0,
                    "spearman_rho": 0.0, "spearman_p": 1.0,
                }
                continue
            pr, pp = pearsonr(sa, sb)
            sr, sp = spearmanr(sa, sb)
            pairwise[f"{a}_vs_{b}"] = {
                "pearson_r": round(float(pr), 4),
                "pearson_p": float(pp),
                "spearman_rho": round(float(sr), 4),
                "spearman_p": float(sp),
            }

    signal_vs_f1 = {}
    fa = np.array(f1_values)
    for s in available:
        sa = np.array(signals[s])
        if np.std(sa) < 1e-12 or np.std(fa) < 1e-12:
            signal_vs_f1[s] = {
                "pearson_r": 0.0, "pearson_p": 1.0,
                "spearman_rho": 0.0, "spearman_p": 1.0,
            }
            continue
        pr, pp = pearsonr(sa, fa)
        sr, sp = spearmanr(sa, fa)
        signal_vs_f1[s] = {
            "pearson_r": round(float(pr), 4),
            "pearson_p": float(pp),
            "spearman_rho": round(float(sr), 4),
            "spearman_p": float(sp),
        }

    return {
        "label": label,
        "n": len(f1_values),
        "pairwise_correlations": pairwise,
        "signal_vs_f1": signal_vs_f1,
    }


# ---------------------------------------------------------------------------
# Part 2: Linear combination grid search (all pairs, step 0.05)
# ---------------------------------------------------------------------------

def part2_linear_combo_grid(
    signals: dict[str, list[float]],
    f1_values: list[float],
    label: str,
) -> dict:
    available = [s for s in SIGNAL_NAMES if s in signals]
    alphas = [round(a * 0.05, 2) for a in range(21)]
    f1_arr = np.array(f1_values)

    results = {}
    for sig_a_name, sig_b_name in combinations(available, 2):
        sa = np.array(signals[sig_a_name])
        sb = np.array(signals[sig_b_name])

        sa_range = sa.max() - sa.min()
        sb_range = sb.max() - sb.min()
        sa_norm = (sa - sa.min()) / (sa_range + 1e-12) if sa_range > 1e-12 else np.zeros_like(sa)
        sb_norm = (sb - sb.min()) / (sb_range + 1e-12) if sb_range > 1e-12 else np.zeros_like(sb)

        grid = []
        best_alpha, best_rho = None, -999.0
        for alpha in alphas:
            combined = alpha * sa_norm + (1 - alpha) * sb_norm
            if np.std(combined) < 1e-12:
                rho_val, p_val = 0.0, 1.0
            else:
                rho, p = spearmanr(combined, f1_arr)
                rho_val = round(float(rho), 4)
                p_val = float(p)
            grid.append({"alpha": alpha, "spearman_rho": rho_val, "p_value": p_val})
            if rho_val > best_rho:
                best_rho = rho_val
                best_alpha = alpha

        combo_key = f"{sig_a_name}_vs_{sig_b_name}"
        results[combo_key] = {
            "signal_a": sig_a_name,
            "signal_b": sig_b_name,
            "formula": f"alpha*{sig_a_name} + (1-alpha)*{sig_b_name}",
            "grid": grid,
            "best_alpha": best_alpha,
            "best_rho": best_rho,
            "single_a_rho": grid[-1]["spearman_rho"],
            "single_b_rho": grid[0]["spearman_rho"],
        }

    return {"label": label, "n": len(f1_values), "combinations": results}


# ---------------------------------------------------------------------------
# Part 3: Logistic regression ensemble (10-fold CV)
# ---------------------------------------------------------------------------

def part3_logistic_ensemble(
    signals: dict[str, list[float]],
    f1_values: list[float],
    label: str,
) -> dict:
    from sklearn.linear_model import LogisticRegression
    from sklearn.model_selection import StratifiedKFold
    from sklearn.preprocessing import StandardScaler
    from sklearn.metrics import roc_auc_score

    available = [f for f in SIGNAL_NAMES if f in signals]
    f1_arr = np.array(f1_values)
    median_f1 = float(np.median(f1_arr))
    y = (f1_arr > median_f1).astype(int)

    if len(set(y)) < 2:
        return {"error": "cannot binarize F1", "label": label}

    X = np.column_stack([signals[f] for f in available])
    n, d = X.shape
    n_splits = min(10, n)

    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    scaler = StandardScaler()

    ensemble_aucs = []
    all_coefs = []
    for train_idx, test_idx in skf.split(X, y):
        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]
        X_train_s = scaler.fit_transform(X_train)
        X_test_s = scaler.transform(X_test)
        clf = LogisticRegression(max_iter=1000, random_state=42)
        clf.fit(X_train_s, y_train)
        proba = clf.predict_proba(X_test_s)[:, 1]
        if len(set(y_test)) >= 2:
            ensemble_aucs.append(roc_auc_score(y_test, proba))
        all_coefs.append(clf.coef_[0].tolist())

    single_aucs = {}
    for i, f in enumerate(available):
        sig_aucs = []
        for train_idx, test_idx in skf.split(X, y):
            x_train = X[train_idx, i:i+1]
            x_test = X[test_idx, i:i+1]
            y_train, y_test = y[train_idx], y[test_idx]
            x_train_s = scaler.fit_transform(x_train)
            x_test_s = scaler.transform(x_test)
            clf_s = LogisticRegression(max_iter=1000, random_state=42)
            clf_s.fit(x_train_s, y_train)
            proba_s = clf_s.predict_proba(x_test_s)[:, 1]
            if len(set(y_test)) >= 2:
                sig_aucs.append(roc_auc_score(y_test, proba_s))
        single_aucs[f] = {
            "mean_auroc": round(float(np.mean(sig_aucs)), 4) if sig_aucs else None,
            "std_auroc": round(float(np.std(sig_aucs)), 4) if sig_aucs else None,
        }

    mean_coefs = np.mean(all_coefs, axis=0)
    coef_dict = {f: round(float(c), 4) for f, c in zip(available, mean_coefs)}

    X_all_s = scaler.fit_transform(X)
    clf_all = LogisticRegression(max_iter=1000, random_state=42)
    clf_all.fit(X_all_s, y)
    ensemble_scores = clf_all.predict_proba(X_all_s)[:, 1].tolist()

    return {
        "label": label,
        "n": n,
        "n_splits": n_splits,
        "median_f1_threshold": round(median_f1, 4),
        "features_used": available,
        "ensemble_mean_auroc": round(float(np.mean(ensemble_aucs)), 4) if ensemble_aucs else None,
        "ensemble_std_auroc": round(float(np.std(ensemble_aucs)), 4) if ensemble_aucs else None,
        "single_signal_aurocs": single_aucs,
        "mean_coefficients": coef_dict,
        "ensemble_scores": [round(v, 4) for v in ensemble_scores],
    }


# ---------------------------------------------------------------------------
# Part 4: Best-of-N selection F1
# ---------------------------------------------------------------------------

def _select_sj_best(filtered_instances, per_sample_f1s, subtask):
    selected = []
    for idx, inst in enumerate(filtered_instances):
        samples = inst["samples"]
        n = len(samples)
        if n <= 1:
            selected.append(per_sample_f1s[idx][0] if n == 1 else 0.0)
            continue
        sample_scores = []
        for k in range(n):
            sims = []
            for j in range(n):
                if j == k:
                    continue
                if subtask == "ner":
                    sim = _ner_soft_jaccard_pair(samples[k].get("entities", []), samples[j].get("entities", []))
                else:
                    sim = _re_soft_jaccard_pair(samples[k].get("relations", []), samples[j].get("relations", []))
                sims.append(sim)
            sample_scores.append(float(np.mean(sims)))
        best_k = int(np.argmax(sample_scores))
        selected.append(per_sample_f1s[idx][best_k])
    return selected


def _select_vc_best(filtered_instances, per_sample_f1s, subtask):
    selected = []
    for idx, inst in enumerate(filtered_instances):
        samples = inst["samples"]
        n = len(samples)
        if n == 0:
            selected.append(0.0)
            continue
        counter: Counter = Counter()
        for s in samples:
            if subtask == "ner":
                for e in s.get("entities", []):
                    counter[(e.get("text", ""), e.get("type", ""))] += 1
            else:
                for r in s.get("relations", []):
                    counter[(r.get("head", ""), r.get("tail", ""), r.get("type", ""))] += 1
        majority_set = {k for k, v in counter.items() if v > n / 2}
        best_k, best_score = 0, -1
        for k, s in enumerate(samples):
            if subtask == "ner":
                s_keys = {(e.get("text", ""), e.get("type", "")) for e in s.get("entities", [])}
            else:
                s_keys = {(r.get("head", ""), r.get("tail", ""), r.get("type", "")) for r in s.get("relations", [])}
            overlap = len(s_keys & majority_set)
            penalty = len(s_keys - majority_set)
            score = overlap - 0.5 * penalty
            if score > best_score:
                best_score = score
                best_k = k
        selected.append(per_sample_f1s[idx][best_k])
    return selected


def _select_lp_best(filtered_instances, per_sample_f1s):
    selected = []
    for idx, inst in enumerate(filtered_instances):
        samples = inst["samples"]
        if not samples:
            selected.append(0.0)
            continue
        lp_scores = [s.get("mean_logprob", -999) for s in samples]
        best_k = int(np.argmax(lp_scores))
        selected.append(per_sample_f1s[idx][best_k])
    return selected


def _select_ensemble_best(filtered_instances, per_sample_f1s, signals, f1_values, subtask):
    from sklearn.linear_model import LogisticRegression
    from sklearn.preprocessing import StandardScaler

    available = [f for f in SIGNAL_NAMES if f in signals]
    f1_arr = np.array(f1_values)
    median_f1 = float(np.median(f1_arr))
    y = (f1_arr > median_f1).astype(int)

    if len(set(y)) < 2:
        return [per_instance_f1(inst["greedy"], inst["gold"], subtask=subtask) for inst in filtered_instances]

    X = np.column_stack([signals[f] for f in available])
    scaler = StandardScaler()
    X_s = scaler.fit_transform(X)
    clf = LogisticRegression(max_iter=1000, random_state=42)
    clf.fit(X_s, y)

    selected = []
    for idx, inst in enumerate(filtered_instances):
        samples = inst["samples"]
        n = len(samples)
        if n <= 1:
            selected.append(per_sample_f1s[idx][0] if n == 1 else 0.0)
            continue

        sample_ens_scores = []
        for k in range(n):
            sjs = []
            for j in range(n):
                if j == k:
                    continue
                if subtask == "ner":
                    sim = _ner_soft_jaccard_pair(samples[k].get("entities", []), samples[j].get("entities", []))
                else:
                    sim = _re_soft_jaccard_pair(samples[k].get("relations", []), samples[j].get("relations", []))
                sjs.append(sim)
            sj_k = float(np.mean(sjs))

            feat_vec = []
            for f in available:
                if f == "soft_jaccard":
                    feat_vec.append(sj_k)
                elif f == "logprob":
                    feat_vec.append(samples[k].get("mean_logprob", signals["logprob"][idx]))
                else:
                    feat_vec.append(signals[f][idx])
            score = clf.predict_proba(scaler.transform([feat_vec]))[0, 1]
            sample_ens_scores.append(score)

        best_k = int(np.argmax(sample_ens_scores))
        selected.append(per_sample_f1s[idx][best_k])
    return selected


def part4_best_of_n_selection(
    filtered_instances: list[dict],
    f1_values: list[float],
    signals: dict[str, list[float]],
    ensemble_scores: list[float] | None,
    label: str,
    subtask: str,
) -> dict:
    n_instances = len(filtered_instances)
    n_samples = len(filtered_instances[0]["samples"]) if filtered_instances else 0

    per_sample_f1s = []
    for inst in filtered_instances:
        sample_f1s = [per_instance_f1(s, inst["gold"], subtask=subtask) for s in inst["samples"]]
        per_sample_f1s.append(sample_f1s)

    greedy_f1s = [per_instance_f1(inst["greedy"], inst["gold"], subtask=subtask) for inst in filtered_instances]
    random_f1s = [float(np.mean(sf)) if sf else 0.0 for sf in per_sample_f1s]
    oracle_f1s = [max(sf) if sf else 0.0 for sf in per_sample_f1s]

    print(f"    SJ-best...")
    sj_selected = _select_sj_best(filtered_instances, per_sample_f1s, subtask)

    print(f"    voting-conf-best...")
    vc_selected = _select_vc_best(filtered_instances, per_sample_f1s, subtask)

    print(f"    logprob-best...")
    lp_selected = _select_lp_best(filtered_instances, per_sample_f1s)

    print(f"    ensemble-best...")
    if ensemble_scores is not None:
        ens_selected = _select_ensemble_best(filtered_instances, per_sample_f1s, signals, f1_values, subtask)
    else:
        ens_selected = list(greedy_f1s)

    methods = {
        "greedy": round(float(np.mean(greedy_f1s)), 4),
        "random_avg": round(float(np.mean(random_f1s)), 4),
        "sj_best": round(float(np.mean(sj_selected)), 4),
        "voting_conf_best": round(float(np.mean(vc_selected)), 4),
        "logprob_best": round(float(np.mean(lp_selected)), 4),
        "ensemble_best": round(float(np.mean(ens_selected)), 4),
        "oracle": round(float(np.mean(oracle_f1s)), 4),
    }

    return {
        "label": label,
        "n": n_instances,
        "n_samples_per_instance": n_samples,
        "summary": methods,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="exp-016 v2: Signal ensemble analysis")
    parser.add_argument("--ner_seed42_dir", default="/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2")
    parser.add_argument("--ner_seed123_dir", default="/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed123_v2")
    parser.add_argument("--re_dir", default="/root/autodl-tmp/struct_self_consist_ie/output/exp_008_re_n16_v2")
    parser.add_argument("--output_dir", default="/root/autodl-tmp/struct_self_consist_ie/output/exp_016_v2")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    np.random.seed(42)

    print("Loading NER data (merging seed42 + seed123, N=32)...")
    ner_instances = merge_ner_seeds(
        os.path.join(args.ner_seed42_dir, "samples.jsonl"),
        os.path.join(args.ner_seed123_dir, "samples.jsonl"),
    )
    print(f"  {len(ner_instances)} NER instances, {len(ner_instances[0]['samples'])} samples/instance")

    print("Loading RE data (N=16)...")
    re_instances = load_samples(os.path.join(args.re_dir, "samples.jsonl"))
    print(f"  {len(re_instances)} RE instances, {len(re_instances[0]['samples'])} samples/instance")

    def save_json(data, filename):
        path = os.path.join(args.output_dir, filename)
        with open(path, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"  Saved {path}")

    configs = [
        (ner_instances, "ner", "full", "ner_full"),
        (ner_instances, "ner", "conditional", "ner_conditional"),
        (re_instances, "re", "full", "re_full"),
        (re_instances, "re", "conditional", "re_conditional"),
    ]

    all_results = {}

    for data, subtask, mode, label in configs:
        print(f"\n{'='*70}")
        print(f"  {label.upper()} ({subtask}, {mode})")
        print(f"{'='*70}")

        filtered_insts, filtered_f1, signals = compute_all_signals(data, subtask, mode)
        n = len(filtered_f1)
        print(f"  {n} instances")

        # Part 1
        print(f"\n  --- Part 1: Signal Correlation ---")
        corr = part1_signal_correlation(signals, filtered_f1, label)
        print(f"  Signal vs F1 (Spearman rho):")
        for sig, vals in corr["signal_vs_f1"].items():
            print(f"    {sig:25s}: rho={vals['spearman_rho']:+.4f}")

        # Part 2
        print(f"\n  --- Part 2: Linear Combo Grid Search ---")
        grid = part2_linear_combo_grid(signals, filtered_f1, label)
        sorted_combos = sorted(grid["combinations"].items(), key=lambda x: x[1]["best_rho"], reverse=True)
        for combo_key, combo_val in sorted_combos[:5]:
            print(f"    {combo_key}: best_a={combo_val['best_alpha']:.2f}, best_rho={combo_val['best_rho']:+.4f} "
                  f"(single: {combo_val['single_a_rho']:+.4f}, {combo_val['single_b_rho']:+.4f})")

        # Part 3
        print(f"\n  --- Part 3: Logistic Regression Ensemble ({min(10, n)}-fold CV) ---")
        ens = part3_logistic_ensemble(signals, filtered_f1, label)
        if "error" not in ens:
            print(f"    Ensemble AUROC: {ens['ensemble_mean_auroc']:.4f} +/- {ens['ensemble_std_auroc']:.4f}")
            for sig, auc_info in ens["single_signal_aurocs"].items():
                if auc_info["mean_auroc"] is not None:
                    print(f"    {sig:25s} AUROC: {auc_info['mean_auroc']:.4f} +/- {auc_info['std_auroc']:.4f}")
            print(f"    Coefficients: {ens['mean_coefficients']}")
            ensemble_scores = ens.get("ensemble_scores")
        else:
            print(f"    ERROR: {ens['error']}")
            ensemble_scores = None

        # Part 4
        print(f"\n  --- Part 4: Best-of-N Selection F1 ---")
        sel = part4_best_of_n_selection(filtered_insts, filtered_f1, signals, ensemble_scores, label, subtask)
        for method, f1_val in sel["summary"].items():
            print(f"    {method:25s} mean_F1={f1_val:.4f}")

        all_results[label] = {
            "correlation": corr,
            "linear_combo": grid,
            "logistic_ensemble": ens,
            "selection_f1": sel,
        }

    # Save outputs
    print(f"\n{'='*70}")
    print("  Saving outputs...")
    print(f"{'='*70}")

    save_json({k: v["correlation"] for k, v in all_results.items()}, "correlation_matrix.json")
    save_json({k: v["linear_combo"] for k, v in all_results.items()}, "linear_combo_grid.json")

    ens_output = {}
    for k, v in all_results.items():
        ens_data = dict(v["logistic_ensemble"])
        ens_data.pop("ensemble_scores", None)
        ens_output[k] = ens_data
    save_json(ens_output, "logistic_ensemble.json")

    save_json({k: v["selection_f1"] for k, v in all_results.items()}, "selection_f1_comparison.json")

    # CSV summary
    csv_path = os.path.join(args.output_dir, "summary.csv")
    labels = list(all_results.keys())
    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(["=== Selection F1 ==="])
        sel_methods = ["greedy", "random_avg", "sj_best", "voting_conf_best", "logprob_best", "ensemble_best", "oracle"]
        writer.writerow(["method"] + labels)
        for m in sel_methods:
            writer.writerow([m] + [all_results[lb]["selection_f1"]["summary"].get(m, "") for lb in labels])

        writer.writerow([])
        writer.writerow(["=== Ensemble AUROC ==="])
        writer.writerow(["signal"] + labels)
        for sig in SIGNAL_NAMES + ["ensemble_5sig"]:
            row = [sig]
            for lb in labels:
                ens = all_results[lb]["logistic_ensemble"]
                if "error" in ens:
                    row.append("N/A")
                elif sig == "ensemble_5sig":
                    row.append(f"{ens['ensemble_mean_auroc']:.4f}+/-{ens['ensemble_std_auroc']:.4f}")
                else:
                    ai = ens.get("single_signal_aurocs", {}).get(sig, {})
                    if ai.get("mean_auroc") is not None:
                        row.append(f"{ai['mean_auroc']:.4f}+/-{ai['std_auroc']:.4f}")
                    else:
                        row.append("N/A")
            writer.writerow(row)

        writer.writerow([])
        writer.writerow(["=== Best Linear Combo (top 3 per config) ==="])
        writer.writerow(["config", "pair", "best_alpha", "best_rho", "single_a_rho", "single_b_rho"])
        for lb in labels:
            combos = all_results[lb]["linear_combo"]["combinations"]
            sc = sorted(combos.items(), key=lambda x: x[1]["best_rho"], reverse=True)
            for ck, cv in sc[:3]:
                writer.writerow([lb, ck, cv["best_alpha"], cv["best_rho"], cv["single_a_rho"], cv["single_b_rho"]])

        writer.writerow([])
        writer.writerow(["=== Signal vs F1 Spearman ==="])
        writer.writerow(["signal"] + labels)
        for sig in SIGNAL_NAMES:
            row = [sig]
            for lb in labels:
                sv = all_results[lb]["correlation"]["signal_vs_f1"].get(sig, {})
                row.append(sv.get("spearman_rho", "N/A"))
            writer.writerow(row)

    print(f"  Saved {csv_path}")
    print("\nDone.")


if __name__ == "__main__":
    main()
