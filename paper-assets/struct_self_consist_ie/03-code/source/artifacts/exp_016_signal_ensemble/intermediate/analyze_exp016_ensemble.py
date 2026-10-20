#!/usr/bin/env python3
"""exp-016: Signal Ensemble & Combination Analysis (CPU-only).

Four-part analysis:
  Part 1: SJ + logprob instance-level correlation (Pearson/Spearman)
  Part 2: Linear combination grid search (α sweep)
  Part 3: 5-signal logistic regression ensemble (5-fold CV AUROC)
  Part 4: Best-of-N selection F1 comparison

Usage:
    cd /root/autodl-tmp/struct_self_consist_ie
    pip install scikit-learn  # if not installed
    python code/analyze_exp016_ensemble.py \
        --pilot_dir output/mvp_pilot_004 \
        --logprob_dir output/exp_012_logprob \
        --output_dir output/exp016_signal_ensemble
"""

from __future__ import annotations

import argparse
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
    fleiss_kappa_surface,
    structural_consistency_soft_jaccard,
)
from evaluation import per_instance_f1


# ---------------------------------------------------------------------------
# Data loading (reused from exp-015)
# ---------------------------------------------------------------------------

def load_samples(path: str) -> list[dict]:
    instances = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                instances.append(json.loads(line))
    return instances


def load_logprob_instances(logprob_dir: str) -> list[dict] | None:
    """Load instances with per-sample logprob from samples_with_logprobs.jsonl."""
    if not logprob_dir or not os.path.isdir(logprob_dir):
        return None
    path = os.path.join(logprob_dir, "samples_with_logprobs.jsonl")
    if not os.path.exists(path):
        return None
    instances = load_samples(path)
    if instances and "samples" in instances[0]:
        s0 = instances[0]["samples"][0]
        if "mean_logprob" in s0:
            return instances
    return None


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
    """Mean of per-sample mean_logprob for an instance."""
    lps = []
    for s in inst.get("samples", []):
        lp = s.get("mean_logprob")
        if lp is not None:
            lps.append(lp)
    return float(np.mean(lps)) if lps else 0.0


def compute_all_signals(
    instances: list[dict],
    subtask: str,
) -> tuple[list[dict], list[float], dict[str, list[float]]]:
    """Compute all 5 signals + F1 for filtered (gold-nonempty) instances.

    Returns: (filtered_instances, filtered_f1, signals_dict)
    """
    n_total = len(instances)
    f1_values = [per_instance_f1(inst["greedy"], inst["gold"], subtask=subtask) for inst in instances]

    if subtask == "ner":
        nonempty_mask = [len(inst["gold"].get("entities", [])) > 0 for inst in instances]
    elif subtask == "re":
        nonempty_mask = [len(inst["gold"].get("relations", [])) > 0 for inst in instances]
    else:
        nonempty_mask = [True] * n_total

    filtered_instances = [inst for inst, m in zip(instances, nonempty_mask) if m]
    filtered_f1 = [f for f, m in zip(f1_values, nonempty_mask) if m]
    n_filtered = len(filtered_f1)

    consistency = compute_all_consistency_scores(filtered_instances, subtask=subtask)
    signals: dict[str, list[float]] = {
        "soft_jaccard": list(consistency["soft_jaccard"]),
        "fleiss_kappa": list(consistency["fleiss_kappa"]),
        "exact_match": compute_exact_match_rate(filtered_instances, subtask),
        "voting_confidence": compute_voting_confidence(filtered_instances, subtask),
    }

    has_logprob = any(
        s.get("mean_logprob") is not None
        for inst in filtered_instances
        for s in inst.get("samples", [])[:1]
    )
    if has_logprob:
        signals["logprob"] = [compute_instance_logprob(inst) for inst in filtered_instances]
    else:
        print(f"  WARNING: logprob unavailable for {subtask}, using zeros")
        signals["logprob"] = [0.0] * n_filtered

    return filtered_instances, filtered_f1, signals


# ---------------------------------------------------------------------------
# Part 1: Pairwise signal correlation
# ---------------------------------------------------------------------------

def part1_signal_correlation(
    signals: dict[str, list[float]],
    f1_values: list[float],
    subtask: str,
) -> dict:
    sig_names = ["soft_jaccard", "fleiss_kappa", "logprob", "exact_match", "voting_confidence"]
    available = [s for s in sig_names if s in signals]

    pairwise = {}
    for i, a in enumerate(available):
        for b in available[i + 1:]:
            sa, sb = np.array(signals[a]), np.array(signals[b])
            pr, pp = pearsonr(sa, sb)
            sr, sp = spearmanr(sa, sb)
            pairwise[f"{a}_vs_{b}"] = {
                "pearson_r": round(float(pr), 4),
                "pearson_p": float(pp),
                "spearman_rho": round(float(sr), 4),
                "spearman_p": float(sp),
            }

    signal_vs_f1 = {}
    for s in available:
        sa = np.array(signals[s])
        fa = np.array(f1_values)
        pr, pp = pearsonr(sa, fa)
        sr, sp = spearmanr(sa, fa)
        signal_vs_f1[s] = {
            "pearson_r": round(float(pr), 4),
            "pearson_p": float(pp),
            "spearman_rho": round(float(sr), 4),
            "spearman_p": float(sp),
        }

    scatter_data = {
        "soft_jaccard": [round(v, 4) for v in signals.get("soft_jaccard", [])],
        "logprob": [round(v, 4) for v in signals.get("logprob", [])],
        "f1": [round(v, 4) for v in f1_values],
    }

    return {
        "subtask": subtask,
        "n": len(f1_values),
        "pairwise_correlations": pairwise,
        "signal_vs_f1": signal_vs_f1,
        "scatter_data_sj_logprob": scatter_data,
    }


# ---------------------------------------------------------------------------
# Part 2: Linear combination grid search
# ---------------------------------------------------------------------------

def part2_linear_combo_grid(
    signals: dict[str, list[float]],
    f1_values: list[float],
    subtask: str,
) -> dict:
    alphas = [round(a * 0.1, 1) for a in range(11)]
    combos = [
        ("soft_jaccard", "logprob"),
        ("voting_confidence", "logprob"),
        ("soft_jaccard", "voting_confidence"),
    ]

    results = {}
    f1_arr = np.array(f1_values)

    for sig_a_name, sig_b_name in combos:
        if sig_a_name not in signals or sig_b_name not in signals:
            continue
        sa = np.array(signals[sig_a_name])
        sb = np.array(signals[sig_b_name])

        # Normalize to [0, 1] for fair combination
        sa_min, sa_max = sa.min(), sa.max()
        sb_min, sb_max = sb.min(), sb.max()
        sa_norm = (sa - sa_min) / (sa_max - sa_min + 1e-12)
        sb_norm = (sb - sb_min) / (sb_max - sb_min + 1e-12)

        grid = []
        best_alpha, best_rho = None, -999
        for alpha in alphas:
            combined = alpha * sa_norm + (1 - alpha) * sb_norm
            rho, p = spearmanr(combined, f1_arr)
            rho_val = round(float(rho), 4)
            grid.append({"alpha": alpha, "spearman_rho": rho_val, "p_value": float(p)})
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
            "single_a_rho": grid[-1]["spearman_rho"],  # alpha=1.0
            "single_b_rho": grid[0]["spearman_rho"],   # alpha=0.0
        }

    return {"subtask": subtask, "n": len(f1_values), "combinations": results}


# ---------------------------------------------------------------------------
# Part 3: Logistic regression ensemble
# ---------------------------------------------------------------------------

def part3_logistic_ensemble(
    signals: dict[str, list[float]],
    f1_values: list[float],
    subtask: str,
) -> dict:
    try:
        from sklearn.linear_model import LogisticRegression
        from sklearn.model_selection import StratifiedKFold
        from sklearn.preprocessing import StandardScaler
        from sklearn.metrics import roc_auc_score
    except ImportError:
        return {"error": "scikit-learn not installed", "subtask": subtask}

    feature_names = ["soft_jaccard", "fleiss_kappa", "logprob", "exact_match", "voting_confidence"]
    available = [f for f in feature_names if f in signals]

    f1_arr = np.array(f1_values)
    median_f1 = float(np.median(f1_arr))
    y = (f1_arr > median_f1).astype(int)

    if len(set(y)) < 2:
        return {"error": "cannot binarize F1 (all same class)", "subtask": subtask}

    X = np.column_stack([signals[f] for f in available])
    n, d = X.shape

    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    scaler = StandardScaler()

    # Ensemble CV
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

    # Single-signal AUROCs
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

    # Average coefficients
    mean_coefs = np.mean(all_coefs, axis=0)
    coef_dict = {f: round(float(c), 4) for f, c in zip(available, mean_coefs)}

    # Fit final model on all data for ensemble scores (used in Part 4)
    X_all_s = scaler.fit_transform(X)
    clf_all = LogisticRegression(max_iter=1000, random_state=42)
    clf_all.fit(X_all_s, y)
    ensemble_scores = clf_all.predict_proba(X_all_s)[:, 1].tolist()

    return {
        "subtask": subtask,
        "n": n,
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

def part4_best_of_n_selection(
    filtered_instances: list[dict],
    f1_values: list[float],
    signals: dict[str, list[float]],
    ensemble_scores: list[float] | None,
    subtask: str,
) -> dict:
    n_instances = len(filtered_instances)

    # Per-sample F1 for each instance
    per_sample_f1s = []
    for inst in filtered_instances:
        sample_f1s = [per_instance_f1(s, inst["gold"], subtask=subtask) for s in inst["samples"]]
        per_sample_f1s.append(sample_f1s)

    # Greedy F1
    greedy_f1s = [per_instance_f1(inst["greedy"], inst["gold"], subtask=subtask) for inst in filtered_instances]
    greedy_mean = float(np.mean(greedy_f1s))

    # Random (average over all samples)
    random_f1s = [float(np.mean(sf)) if sf else 0.0 for sf in per_sample_f1s]
    random_mean = float(np.mean(random_f1s))

    # Oracle (true best)
    oracle_f1s = [max(sf) if sf else 0.0 for sf in per_sample_f1s]
    oracle_mean = float(np.mean(oracle_f1s))

    # Signal-based selection: pick the sample with highest signal value
    def select_by_per_sample_signal(sig_name: str) -> list[float]:
        """For signals computed per-sample (logprob), select best sample."""
        # Most signals are instance-level, not per-sample
        # For instance-level signals, we can't do per-sample selection
        # Fall back to using the signal as a quality indicator for the instance
        return None

    def select_by_instance_signal_rerank(
        sig_values: list[float],
        per_sample_f1s_: list[list[float]],
        instances_: list[dict],
        subtask_: str,
    ) -> list[float]:
        """Use instance-level signal to select: pick the sample that maximizes
        the consistency signal when other samples are held fixed.

        For efficiency, we use a simpler heuristic:
        pick the sample whose individual contribution to the consistency score is highest.
        Specifically, for each sample k, compute SJ between sample k and all others,
        then pick the sample with highest mean pairwise SJ.
        """
        selected_f1s = []
        for idx, inst in enumerate(instances_):
            samples = inst["samples"]
            n = len(samples)
            if n == 0:
                selected_f1s.append(0.0)
                continue
            if n == 1:
                selected_f1s.append(per_sample_f1s_[idx][0] if per_sample_f1s_[idx] else 0.0)
                continue

            # For each sample, compute mean pairwise consistency with all others
            field = "entities" if subtask_ == "ner" else "relations"
            sample_scores = []
            for k in range(n):
                pairwise_sims = []
                for j in range(n):
                    if j == k:
                        continue
                    if subtask_ == "ner":
                        from consistency import _ner_soft_jaccard_pair
                        sim = _ner_soft_jaccard_pair(
                            samples[k].get("entities", []),
                            samples[j].get("entities", []),
                        )
                    else:
                        from consistency import _re_soft_jaccard_pair
                        sim = _re_soft_jaccard_pair(
                            samples[k].get("relations", []),
                            samples[j].get("relations", []),
                        )
                    pairwise_sims.append(sim)
                sample_scores.append(float(np.mean(pairwise_sims)) if pairwise_sims else 0.0)

            best_k = int(np.argmax(sample_scores))
            selected_f1s.append(per_sample_f1s_[idx][best_k])
        return selected_f1s

    # SJ-best: select sample with highest mean pairwise SJ
    print(f"  Computing SJ-best selection for {subtask}...")
    sj_selected = select_by_instance_signal_rerank(
        signals.get("soft_jaccard", []), per_sample_f1s, filtered_instances, subtask
    )
    sj_mean = float(np.mean(sj_selected))

    # Voting-conf-best: select sample closest to majority vote
    print(f"  Computing voting-conf-best selection for {subtask}...")
    vc_selected = []
    for idx, inst in enumerate(filtered_instances):
        samples = inst["samples"]
        n = len(samples)
        if n == 0:
            vc_selected.append(0.0)
            continue

        # Build majority vote set
        counter: Counter = Counter()
        for s in samples:
            if subtask == "ner":
                for e in s.get("entities", []):
                    counter[(e.get("text", ""), e.get("type", ""))] += 1
            else:
                for r in s.get("relations", []):
                    counter[(r.get("head", ""), r.get("tail", ""), r.get("type", ""))] += 1

        majority_set = {k for k, v in counter.items() if v > n / 2}

        # Score each sample by overlap with majority
        best_k, best_overlap = 0, -1
        for k, s in enumerate(samples):
            if subtask == "ner":
                s_keys = {(e.get("text", ""), e.get("type", "")) for e in s.get("entities", [])}
            else:
                s_keys = {(r.get("head", ""), r.get("tail", ""), r.get("type", "")) for r in s.get("relations", [])}
            overlap = len(s_keys & majority_set)
            penalty = len(s_keys - majority_set)
            score = overlap - 0.5 * penalty
            if score > best_overlap:
                best_overlap = score
                best_k = k
        vc_selected.append(per_sample_f1s[idx][best_k])
    vc_mean = float(np.mean(vc_selected))

    # Logprob-best: if we have per-sample logprobs, use them
    # Otherwise, logprob is instance-level and can't do per-sample selection
    # Try to load per-sample logprobs from the instances
    lp_selected = []
    has_per_sample_lp = False
    for inst in filtered_instances:
        for s in inst["samples"]:
            if "mean_logprob" in s or "logprob" in s:
                has_per_sample_lp = True
                break
        break

    if has_per_sample_lp:
        print(f"  Computing logprob-best selection for {subtask} (per-sample logprobs available)...")
        for idx, inst in enumerate(filtered_instances):
            samples = inst["samples"]
            if not samples:
                lp_selected.append(0.0)
                continue
            lp_scores = [s.get("mean_logprob", s.get("logprob", 0.0)) for s in samples]
            best_k = int(np.argmax(lp_scores))
            lp_selected.append(per_sample_f1s[idx][best_k])
    else:
        print(f"  No per-sample logprobs; logprob-best = greedy")
        lp_selected = list(greedy_f1s)
    lp_mean = float(np.mean(lp_selected))

    # Ensemble-best: use logistic regression score per sample
    # We need per-sample features to score each sample
    # Build per-sample features and score with ensemble
    ens_selected = []
    if ensemble_scores is not None:
        print(f"  Computing ensemble-best selection for {subtask}...")
        try:
            from sklearn.linear_model import LogisticRegression
            from sklearn.preprocessing import StandardScaler

            feature_names = ["soft_jaccard", "fleiss_kappa", "logprob", "exact_match", "voting_confidence"]
            available_feats = [f for f in feature_names if f in signals]
            f1_arr = np.array(f1_values)
            median_f1 = float(np.median(f1_arr))
            y = (f1_arr > median_f1).astype(int)
            X = np.column_stack([signals[f] for f in available_feats])
            scaler = StandardScaler()
            X_s = scaler.fit_transform(X)
            clf = LogisticRegression(max_iter=1000, random_state=42)
            clf.fit(X_s, y)

            for idx, inst in enumerate(filtered_instances):
                samples = inst["samples"]
                n = len(samples)
                if n == 0:
                    ens_selected.append(0.0)
                    continue
                if n == 1:
                    ens_selected.append(per_sample_f1s[idx][0])
                    continue

                # For each sample, compute "leave-this-sample-in" features
                # Use the sample's pairwise SJ as a proxy for per-sample signal
                # Simpler approach: score each sample by its mean pairwise consistency
                sample_ens_scores = []
                for k in range(n):
                    # Compute per-sample SJ
                    pairwise_sjs = []
                    for j in range(n):
                        if j == k:
                            continue
                        if subtask == "ner":
                            from consistency import _ner_soft_jaccard_pair
                            sim = _ner_soft_jaccard_pair(
                                samples[k].get("entities", []),
                                samples[j].get("entities", []),
                            )
                        else:
                            from consistency import _re_soft_jaccard_pair
                            sim = _re_soft_jaccard_pair(
                                samples[k].get("relations", []),
                                samples[j].get("relations", []),
                            )
                        pairwise_sjs.append(sim)
                    sj_k = float(np.mean(pairwise_sjs)) if pairwise_sjs else 0.0

                    # Use instance-level features with per-sample SJ
                    feat_vec = []
                    for f in available_feats:
                        if f == "soft_jaccard":
                            feat_vec.append(sj_k)
                        else:
                            feat_vec.append(signals[f][idx])
                    feat_arr = scaler.transform([feat_vec])
                    score = clf.predict_proba(feat_arr)[0, 1]
                    sample_ens_scores.append(score)

                best_k = int(np.argmax(sample_ens_scores))
                ens_selected.append(per_sample_f1s[idx][best_k])
        except Exception as e:
            print(f"  Ensemble selection failed: {e}")
            ens_selected = list(greedy_f1s)
    else:
        ens_selected = list(greedy_f1s)
    ens_mean = float(np.mean(ens_selected))

    methods = {
        "greedy": {"mean_f1": round(greedy_mean, 4), "per_instance": [round(v, 4) for v in greedy_f1s]},
        "random_avg": {"mean_f1": round(random_mean, 4), "per_instance": [round(v, 4) for v in random_f1s]},
        "sj_best": {"mean_f1": round(sj_mean, 4), "per_instance": [round(v, 4) for v in sj_selected]},
        "voting_conf_best": {"mean_f1": round(vc_mean, 4), "per_instance": [round(v, 4) for v in vc_selected]},
        "logprob_best": {"mean_f1": round(lp_mean, 4), "per_instance": [round(v, 4) for v in lp_selected]},
        "ensemble_best": {"mean_f1": round(ens_mean, 4), "per_instance": [round(v, 4) for v in ens_selected]},
        "oracle": {"mean_f1": round(oracle_mean, 4), "per_instance": [round(v, 4) for v in oracle_f1s]},
    }

    summary_table = {k: v["mean_f1"] for k, v in methods.items()}

    return {
        "subtask": subtask,
        "n": n_instances,
        "methods": methods,
        "summary": summary_table,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="exp-016: Signal ensemble analysis")
    parser.add_argument("--pilot_dir", default="/root/autodl-tmp/struct_self_consist_ie/output/mvp_pilot_004")
    parser.add_argument("--logprob_dir", default="/root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob")
    parser.add_argument("--output_dir", default="/root/autodl-tmp/struct_self_consist_ie/output/exp016_signal_ensemble")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    np.random.seed(42)

    # Prefer samples_with_logprobs.jsonl (has per-sample logprob fields)
    lp_instances = load_logprob_instances(args.logprob_dir)
    if lp_instances is not None:
        instances = lp_instances
        print(f"Loaded {len(instances)} instances from {args.logprob_dir}/samples_with_logprobs.jsonl (with logprobs)")
    else:
        samples_path = os.path.join(args.pilot_dir, "samples.jsonl")
        print(f"Loading samples from {samples_path}...")
        instances = load_samples(samples_path)
        print(f"Loaded {len(instances)} instances (no per-sample logprobs)")

    def save_json(data, filename):
        path = os.path.join(args.output_dir, filename)
        with open(path, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"  Saved {path}")

    all_results = {}

    for subtask in ["ner", "re"]:
        print(f"\n{'='*70}")
        print(f"  {subtask.upper()} Analysis")
        print(f"{'='*70}")

        filtered_insts, filtered_f1, signals = compute_all_signals(instances, subtask)
        n = len(filtered_f1)
        print(f"  {n} gold-nonempty instances")

        # Part 1
        print(f"\n  --- Part 1: Signal Correlation ---")
        corr = part1_signal_correlation(signals, filtered_f1, subtask)
        for pair, vals in corr["pairwise_correlations"].items():
            print(f"    {pair}: pearson={vals['pearson_r']:+.4f}, spearman={vals['spearman_rho']:+.4f}")

        # Part 2
        print(f"\n  --- Part 2: Linear Combo Grid Search ---")
        grid = part2_linear_combo_grid(signals, filtered_f1, subtask)
        for combo_key, combo_val in grid["combinations"].items():
            print(f"    {combo_key}: best_α={combo_val['best_alpha']}, best_ρ={combo_val['best_rho']:+.4f} "
                  f"(vs a={combo_val['single_a_rho']:+.4f}, b={combo_val['single_b_rho']:+.4f})")

        # Part 3
        print(f"\n  --- Part 3: Logistic Regression Ensemble ---")
        ens = part3_logistic_ensemble(signals, filtered_f1, subtask)
        if "error" not in ens:
            print(f"    Ensemble AUROC: {ens['ensemble_mean_auroc']:.4f} ± {ens['ensemble_std_auroc']:.4f}")
            for sig, auc_info in ens["single_signal_aurocs"].items():
                print(f"    {sig:25s} AUROC: {auc_info['mean_auroc']:.4f} ± {auc_info['std_auroc']:.4f}")
            print(f"    Coefficients: {ens['mean_coefficients']}")
            ensemble_scores = ens.get("ensemble_scores")
        else:
            print(f"    ERROR: {ens['error']}")
            ensemble_scores = None

        # Part 4
        print(f"\n  --- Part 4: Best-of-N Selection F1 ---")
        sel = part4_best_of_n_selection(filtered_insts, filtered_f1, signals, ensemble_scores, subtask)
        for method, f1_val in sel["summary"].items():
            print(f"    {method:25s} mean_F1={f1_val:.4f}")

        all_results[subtask] = {
            "correlation": corr,
            "linear_combo": grid,
            "logistic_ensemble": ens,
            "selection_f1": sel,
        }

    # Save outputs
    print(f"\n{'='*70}")
    print("  Saving outputs...")
    print(f"{'='*70}")

    save_json({
        "ner": all_results["ner"]["correlation"],
        "re": all_results["re"]["correlation"],
    }, "correlation_matrix.json")

    save_json({
        "ner": all_results["ner"]["linear_combo"],
        "re": all_results["re"]["linear_combo"],
    }, "linear_combo_grid.json")

    save_json({
        "ner": all_results["ner"]["logistic_ensemble"],
        "re": all_results["re"]["logistic_ensemble"],
    }, "logistic_ensemble.json")

    # Selection F1 — remove per_instance arrays for summary
    sel_summary = {}
    for st in ["ner", "re"]:
        sel_data = all_results[st]["selection_f1"]
        sel_summary[st] = {
            "subtask": st,
            "n": sel_data["n"],
            "summary": sel_data["summary"],
        }
    save_json(sel_summary, "selection_f1_comparison.json")

    # Full selection data with per-instance
    save_json({
        "ner": all_results["ner"]["selection_f1"],
        "re": all_results["re"]["selection_f1"],
    }, "selection_f1_full.json")

    # Summary markdown
    summary_lines = ["# exp-016: Signal Ensemble Analysis\n"]
    for st in ["ner", "re"]:
        r = all_results[st]
        summary_lines.append(f"\n## {st.upper()}\n")

        summary_lines.append("### Part 1: Signal Correlation (SJ vs logprob)")
        sj_lp_key = "soft_jaccard_vs_logprob"
        if sj_lp_key in r["correlation"]["pairwise_correlations"]:
            c = r["correlation"]["pairwise_correlations"][sj_lp_key]
            summary_lines.append(f"- Pearson r = {c['pearson_r']}, Spearman ρ = {c['spearman_rho']}")

        summary_lines.append("\n### Part 2: Linear Combo Grid (best α)")
        for combo_key, combo_val in r["linear_combo"]["combinations"].items():
            summary_lines.append(
                f"- {combo_val['formula']}: best α={combo_val['best_alpha']}, "
                f"ρ={combo_val['best_rho']} (single: {combo_val['single_a_rho']}, {combo_val['single_b_rho']})"
            )

        summary_lines.append("\n### Part 3: Logistic Ensemble")
        ens = r["logistic_ensemble"]
        if "error" not in ens:
            summary_lines.append(f"- Ensemble AUROC: {ens['ensemble_mean_auroc']} ± {ens['ensemble_std_auroc']}")
            for sig, auc_info in ens["single_signal_aurocs"].items():
                summary_lines.append(f"  - {sig}: {auc_info['mean_auroc']} ± {auc_info['std_auroc']}")
            summary_lines.append(f"- Coefficients: {ens['mean_coefficients']}")

        summary_lines.append("\n### Part 4: Best-of-N Selection F1")
        summary_lines.append("| Method | Mean F1 |")
        summary_lines.append("|--------|---------|")
        for method, f1_val in r["selection_f1"]["summary"].items():
            summary_lines.append(f"| {method} | {f1_val:.4f} |")
        summary_lines.append("")

    summary_md = "\n".join(summary_lines)
    summary_path = os.path.join(args.output_dir, "summary.md")
    with open(summary_path, "w") as f:
        f.write(summary_md)
    print(f"  Saved {summary_path}")

    print("\nDone.")


if __name__ == "__main__":
    main()
