#!/usr/bin/env python3
"""Adaptive Sample Budget (ASB) for structured self-consistency IE.

CPU-only experiment. No GPU or model forward pass required.
Subsamples existing N=16 inference data to N∈{2,4,8,16}, computes instance-level
features from cheap (N=2) subsamples, trains a predictor for optimal per-instance
sample count, and evaluates adaptive allocation under a fixed total budget.
"""

import argparse
import json
import os
import sys
import time
import warnings
from collections import defaultdict
from itertools import combinations

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import f1_score, classification_report
from sklearn.preprocessing import StandardScaler

warnings.filterwarnings("ignore", category=UserWarning)

N_VALUES = [2, 4, 8, 16]


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_samples(path, max_instances=0):
    data = []
    with open(path) as f:
        for line in f:
            if line.strip():
                data.append(json.loads(line))
                if 0 < max_instances <= len(data):
                    break
    return data


# ---------------------------------------------------------------------------
# Entity helpers
# ---------------------------------------------------------------------------

def entity_set(entities):
    return {(e["start"], e["end"], e["type"]) for e in entities}


def compute_prf(pred, gold):
    if not gold and not pred:
        return 1.0, 1.0, 1.0
    if not pred or not gold:
        return 0.0, 0.0, 0.0
    tp = len(pred & gold)
    if tp == 0:
        return 0.0, 0.0, 0.0
    p = tp / len(pred)
    r = tp / len(gold)
    return p, r, 2 * p * r / (p + r)


def majority_vote(samples, threshold=0.5):
    counts = defaultdict(int)
    N = len(samples)
    for s in samples:
        for e in s.get("entities", []):
            counts[(e["start"], e["end"], e["type"])] += 1
    return {k for k, c in counts.items() if c / N >= threshold}


# ---------------------------------------------------------------------------
# Phase 1: Subsampling
# ---------------------------------------------------------------------------

def subsample_f1(instance, n, n_subsamples, rng, gold):
    """Compute mean construction F1 over random subsets of size n."""
    all_samples = instance["samples"]
    max_n = len(all_samples)
    if n >= max_n:
        pred = majority_vote(all_samples)
        return compute_prf(pred, gold)[2]

    f1s = []
    for _ in range(n_subsamples):
        idx = rng.choice(max_n, size=n, replace=False)
        subset = [all_samples[i] for i in idx]
        pred = majority_vote(subset)
        f1s.append(compute_prf(pred, gold)[2])
    return float(np.mean(f1s))


def subsample_oracle_f1(instance, n, n_subsamples, rng, gold):
    """Mean oracle F1 (best single sample) over random subsets of size n."""
    all_samples = instance["samples"]
    max_n = len(all_samples)
    if n >= max_n:
        return max(
            compute_prf(entity_set(s.get("entities", [])), gold)[2]
            for s in all_samples
        )

    oracles = []
    for _ in range(n_subsamples):
        idx = rng.choice(max_n, size=n, replace=False)
        subset = [all_samples[i] for i in idx]
        oracles.append(max(
            compute_prf(entity_set(s.get("entities", [])), gold)[2]
            for s in subset
        ))
    return float(np.mean(oracles))


def compute_degeneracy(samples):
    """Fraction of sample pairs that are identical entity sets."""
    esets = [frozenset((e["start"], e["end"], e["type"]) for e in s.get("entities", []))
             for s in samples]
    n = len(esets)
    if n < 2:
        return 0.0
    n_same = sum(1 for i, j in combinations(range(n), 2) if esets[i] == esets[j])
    return n_same / (n * (n - 1) / 2)


def compute_lp_variance(samples):
    """Variance of mean_logprob across samples."""
    lps = []
    for s in samples:
        lp = s.get("mean_logprob")
        if lp is None:
            lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
        lps.append(lp)
    if len(lps) < 2:
        return 0.0
    return float(np.var(lps))


def compute_agreement(samples):
    """Average pairwise Jaccard similarity of entity sets."""
    esets = [frozenset((e["start"], e["end"], e["type"]) for e in s.get("entities", []))
             for s in samples]
    n = len(esets)
    if n < 2:
        return 1.0
    jaccards = []
    for i, j in combinations(range(n), 2):
        a, b = esets[i], esets[j]
        if not a and not b:
            jaccards.append(1.0)
        elif not a or not b:
            jaccards.append(0.0)
        else:
            jaccards.append(len(a & b) / len(a | b))
    return float(np.mean(jaccards))


def compute_entity_count(samples):
    """Average entity count across samples."""
    return float(np.mean([len(s.get("entities", [])) for s in samples]))


# ---------------------------------------------------------------------------
# Phase 2: Instance features (from N=2 cheap subsamples)
# ---------------------------------------------------------------------------

def compute_instance_features(instance, n_subsamples, rng):
    """Compute cheap features from small subsamples."""
    all_samples = instance["samples"]
    max_n = len(all_samples)
    n_feat = min(2, max_n)

    degen_vals = []
    lp_var_vals = []
    agree_vals = []
    ent_count_vals = []

    n_trials = n_subsamples if n_feat < max_n else 1
    for _ in range(n_trials):
        if n_feat < max_n:
            idx = rng.choice(max_n, size=n_feat, replace=False)
            subset = [all_samples[i] for i in idx]
        else:
            subset = all_samples[:n_feat]
        degen_vals.append(compute_degeneracy(subset))
        lp_var_vals.append(compute_lp_variance(subset))
        agree_vals.append(compute_agreement(subset))
        ent_count_vals.append(compute_entity_count(subset))

    text_length = len(instance.get("text", ""))

    features = {
        "degen_rate_n2": float(np.mean(degen_vals)),
        "lp_variance_n2": float(np.mean(lp_var_vals)),
        "agreement_n2": float(np.mean(agree_vals)),
        "entity_count_n2": float(np.mean(ent_count_vals)),
        "text_length": text_length,
    }

    if "greedy" in instance and "gold" in instance:
        greedy_ents = entity_set(instance["greedy"].get("entities", []))
        gold_ents = entity_set(instance["gold"]["entities"])
        features["greedy_f1"] = compute_prf(greedy_ents, gold_ents)[2]

    return features


# ---------------------------------------------------------------------------
# Phase 3: Optimal N labels
# ---------------------------------------------------------------------------

def find_optimal_n(f1_by_n, gain_ratio=0.95):
    """Find smallest N achieving ≥ gain_ratio of max F1 gain over N=2."""
    f1_min_n = min(N_VALUES)
    f1_at_min = f1_by_n.get(f1_min_n, 0.0)
    max_f1 = max(f1_by_n.values())
    max_gain = max_f1 - f1_at_min

    if max_gain <= 1e-6:
        return f1_min_n

    target = f1_at_min + gain_ratio * max_gain
    for n in sorted(N_VALUES):
        if f1_by_n.get(n, 0.0) >= target - 1e-9:
            return n
    return max(N_VALUES)


# ---------------------------------------------------------------------------
# Phase 4: Predictor training
# ---------------------------------------------------------------------------

def train_and_evaluate(X, y, seed=42):
    """5-fold CV for multiple classifiers. Returns dict of results."""
    models = {
        "LogisticRegression": LogisticRegression(
            max_iter=1000, random_state=seed,
        ),
        "RandomForest": RandomForestClassifier(
            n_estimators=100, max_depth=5, random_state=seed,
        ),
        "MLP": MLPClassifier(
            hidden_layer_sizes=(64, 32), max_iter=500, random_state=seed,
        ),
    }

    unique_classes = np.unique(y)
    if len(unique_classes) < 2:
        return {name: {"macro_f1": 0.0, "note": "single class"} for name in models}

    n_splits = min(5, min(np.bincount(y)[np.bincount(y) > 0]))
    if n_splits < 2:
        n_splits = 2

    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=seed)
    results = {}

    for name, model in models.items():
        fold_f1s = []
        all_preds = np.zeros_like(y)
        all_true = np.zeros_like(y)

        for fold_i, (train_idx, test_idx) in enumerate(skf.split(X, y)):
            X_train, X_test = X[train_idx], X[test_idx]
            y_train, y_test = y[train_idx], y[test_idx]

            scaler = StandardScaler()
            X_train_s = scaler.fit_transform(X_train)
            X_test_s = scaler.transform(X_test)

            model_copy = type(model)(**model.get_params())
            model_copy.fit(X_train_s, y_train)
            preds = model_copy.predict(X_test_s)

            fold_f1 = f1_score(y_test, preds, average="macro", zero_division=0)
            fold_f1s.append(fold_f1)
            all_preds[test_idx] = preds
            all_true[test_idx] = y_test

        overall_f1 = f1_score(all_true, all_preds, average="macro", zero_division=0)
        results[name] = {
            "macro_f1": round(float(overall_f1), 4),
            "fold_f1s": [round(f, 4) for f in fold_f1s],
            "mean_fold_f1": round(float(np.mean(fold_f1s)), 4),
            "std_fold_f1": round(float(np.std(fold_f1s)), 4),
        }

    return results


def train_best_model(X, y, best_name, seed=42):
    """Train the best model on all data, return fitted model + scaler."""
    constructors = {
        "LogisticRegression": lambda: LogisticRegression(
            max_iter=1000, random_state=seed,
        ),
        "RandomForest": lambda: RandomForestClassifier(
            n_estimators=100, max_depth=5, random_state=seed,
        ),
        "MLP": lambda: MLPClassifier(
            hidden_layer_sizes=(64, 32), max_iter=500, random_state=seed,
        ),
    }
    scaler = StandardScaler()
    X_s = scaler.fit_transform(X)
    model = constructors[best_name]()
    model.fit(X_s, y)
    return model, scaler


# ---------------------------------------------------------------------------
# Phase 5: Budget-constrained evaluation
# ---------------------------------------------------------------------------

def adaptive_allocation(predicted_ns, budget_per_instance, n_instances):
    """Adjust predicted N values to meet total budget constraint."""
    total_budget = budget_per_instance * n_instances
    alloc = np.array(predicted_ns, dtype=float)

    current_total = alloc.sum()

    if current_total > total_budget:
        # trim: repeatedly reduce the largest allocations
        while alloc.sum() > total_budget:
            excess = alloc.sum() - total_budget
            max_idx = np.where(alloc == alloc.max())[0]
            reduce_each = min(excess / len(max_idx), 2.0)
            for idx in max_idx:
                alloc[idx] = max(2, alloc[idx] - reduce_each)
                if alloc.sum() <= total_budget:
                    break

    elif current_total < total_budget:
        # distribute surplus to instances with highest predicted N (most uncertain)
        surplus = total_budget - current_total
        uncertainty_order = np.argsort(-np.array(predicted_ns))
        for idx in uncertainty_order:
            if surplus <= 0:
                break
            add = min(surplus, 16 - alloc[idx])
            alloc[idx] += add
            surplus -= add

    # snap to valid N values
    valid = np.array(N_VALUES)
    snapped = []
    for a in alloc:
        snapped.append(int(valid[np.argmin(np.abs(valid - a))]))
    return snapped


def evaluate_allocation(instances, allocations, n_subsamples, rng):
    """Evaluate construction F1 under given per-instance N allocations."""
    f1s = []
    for inst, n_alloc in zip(instances, allocations):
        gold = entity_set(inst["gold"]["entities"])
        f1 = subsample_f1(inst, n_alloc, n_subsamples, rng, gold)
        f1s.append(f1)
    return float(np.mean(f1s))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(
        description="Adaptive Sample Budget (ASB) — CPU-only experiment"
    )
    ap.add_argument("--data_paths", type=str, required=True,
                    help="Comma-separated N≥16 inference JSONL paths")
    ap.add_argument("--dataset_names", type=str, required=True,
                    help="Comma-separated dataset names (same order as data_paths)")
    ap.add_argument("--output_dir", type=str, required=True)
    ap.add_argument("--n_subsamples", type=int, default=10,
                    help="Random subsets per N value (default: 10)")
    ap.add_argument("--budget_per_instance", type=int, default=8,
                    help="Average budget per instance (default: 8)")
    ap.add_argument("--max_instances", type=int, default=0,
                    help="Cap instances per dataset for debugging (0=all)")
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    rng = np.random.RandomState(args.seed)

    data_paths = [p.strip() for p in args.data_paths.split(",")]
    dataset_names = [n.strip() for n in args.dataset_names.split(",")]
    assert len(data_paths) == len(dataset_names), \
        f"Mismatch: {len(data_paths)} paths vs {len(dataset_names)} names"

    all_results = {}

    for dpath, dname in zip(data_paths, dataset_names):
        print(f"\n{'='*70}")
        print(f"  Dataset: {dname}")
        print(f"  Path: {dpath}")
        print(f"{'='*70}")

        if not os.path.exists(dpath):
            print(f"  SKIP: file not found")
            continue

        t0 = time.time()
        instances = load_samples(dpath, args.max_instances)
        # filter to instances with gold
        instances = [inst for inst in instances if inst.get("gold", {}).get("entities")]
        max_n = len(instances[0]["samples"]) if instances else 0
        print(f"  Loaded {len(instances)} instances (with gold), max_n={max_n}")

        if max_n < max(N_VALUES):
            valid_ns = [n for n in N_VALUES if n <= max_n]
            print(f"  Warning: max_n={max_n} < 16, using N_VALUES={valid_ns}")
        else:
            valid_ns = N_VALUES

        # ---- Phase 1: Compute F1 at each N for every instance ----
        print("\n  Phase 1: Subsampling F1 at each N ...")
        inst_f1_by_n = []
        for i, inst in enumerate(instances):
            gold = entity_set(inst["gold"]["entities"])
            f1_dict = {}
            for n in valid_ns:
                f1_dict[n] = subsample_f1(inst, n, args.n_subsamples, rng, gold)
            inst_f1_by_n.append(f1_dict)
            if (i + 1) % 500 == 0:
                print(f"    {i+1}/{len(instances)} instances processed")

        # aggregate F1 by N
        mean_f1_by_n = {}
        for n in valid_ns:
            mean_f1_by_n[n] = float(np.mean([d[n] for d in inst_f1_by_n]))
        print(f"  Mean F1 by N: { {n: f'{v:.4f}' for n, v in mean_f1_by_n.items()} }")

        # ---- Phase 2: Instance features ----
        print("\n  Phase 2: Computing instance features (from N=2) ...")
        features_list = []
        for i, inst in enumerate(instances):
            feat = compute_instance_features(inst, args.n_subsamples, rng)
            features_list.append(feat)

        feature_names = sorted(features_list[0].keys())
        X = np.array([[f[k] for k in feature_names] for f in features_list])
        print(f"  Features: {feature_names}")
        print(f"  Feature matrix: {X.shape}")

        # ---- Phase 3: Optimal N labels ----
        print("\n  Phase 3: Computing optimal N labels ...")
        optimal_ns = []
        for f1_dict in inst_f1_by_n:
            optimal_ns.append(find_optimal_n(f1_dict, gain_ratio=0.95))
        optimal_ns_arr = np.array(optimal_ns)

        # map to class indices for sklearn
        n_to_class = {n: i for i, n in enumerate(valid_ns)}
        y = np.array([n_to_class[n] for n in optimal_ns])

        dist = {n: int((optimal_ns_arr == n).sum()) for n in valid_ns}
        print(f"  Optimal N distribution: {dist}")
        print(f"  Mean optimal N: {optimal_ns_arr.mean():.2f}")

        # ---- Phase 4: Predictor training ----
        print("\n  Phase 4: Training predictors (5-fold CV) ...")
        cv_results = train_and_evaluate(X, y, seed=args.seed)

        best_model_name = max(cv_results, key=lambda k: cv_results[k]["macro_f1"])
        print(f"  CV Results:")
        for name, res in cv_results.items():
            marker = " <-- best" if name == best_model_name else ""
            print(f"    {name}: macro_F1={res['macro_f1']:.4f} "
                  f"(±{res.get('std_fold_f1', 0):.4f}){marker}")

        # train final model on all data
        model, scaler = train_best_model(X, y, best_model_name, seed=args.seed)
        predicted_classes = model.predict(scaler.transform(X))
        class_to_n = {i: n for n, i in n_to_class.items()}
        predicted_ns = [class_to_n[c] for c in predicted_classes]

        # ---- Phase 5: Budget-constrained evaluation ----
        print(f"\n  Phase 5: Budget-constrained evaluation (avg budget={args.budget_per_instance}) ...")

        # adaptive allocation
        adapted_ns = adaptive_allocation(
            predicted_ns, args.budget_per_instance, len(instances)
        )
        adaptive_f1 = evaluate_allocation(
            instances, adapted_ns, args.n_subsamples, rng
        )
        adaptive_total = sum(adapted_ns)
        adaptive_avg_n = adaptive_total / len(instances)

        # uniform baseline
        uniform_n = args.budget_per_instance
        uniform_ns = [uniform_n] * len(instances)
        uniform_f1 = evaluate_allocation(
            instances, uniform_ns, args.n_subsamples, rng
        )

        # oracle adaptive (uses true optimal N, then adjusts to budget)
        oracle_adapted = adaptive_allocation(
            optimal_ns, args.budget_per_instance, len(instances)
        )
        oracle_f1 = evaluate_allocation(
            instances, oracle_adapted, args.n_subsamples, rng
        )
        oracle_avg_n = sum(oracle_adapted) / len(instances)

        # greedy baseline
        greedy_f1s = []
        for inst in instances:
            gold = entity_set(inst["gold"]["entities"])
            g_ents = entity_set(inst.get("greedy", inst["samples"][0]).get("entities", []))
            greedy_f1s.append(compute_prf(g_ents, gold)[2])
        greedy_f1 = float(np.mean(greedy_f1s))

        # N=16 (all samples) baseline
        full_f1 = mean_f1_by_n.get(max(valid_ns), 0.0)

        print(f"\n  Results:")
        print(f"    Greedy (N=1):         F1={greedy_f1:.4f}")
        print(f"    Uniform N={uniform_n}:         F1={uniform_f1:.4f}")
        print(f"    Adaptive (predicted): F1={adaptive_f1:.4f}  avg_N={adaptive_avg_n:.2f}")
        print(f"    Oracle adaptive:      F1={oracle_f1:.4f}  avg_N={oracle_avg_n:.2f}")
        print(f"    Full N={max(valid_ns)}:           F1={full_f1:.4f}")
        print(f"    Δ(adaptive - uniform): {adaptive_f1 - uniform_f1:+.4f}")
        print(f"    Δ(oracle - uniform):   {oracle_f1 - uniform_f1:+.4f}")

        # allocation distribution
        adapted_dist = {n: int(sum(1 for a in adapted_ns if a == n)) for n in valid_ns}
        print(f"    Adaptive allocation dist: {adapted_dist}")
        print(f"    Adaptive total budget: {adaptive_total} "
              f"(target: {args.budget_per_instance * len(instances)})")

        # feature importance (from RF)
        if best_model_name == "RandomForest":
            importances = model.feature_importances_
        else:
            # train RF just for feature importance
            rf_temp = RandomForestClassifier(
                n_estimators=100, max_depth=5, random_state=args.seed
            )
            rf_temp.fit(scaler.transform(X), y)
            importances = rf_temp.feature_importances_

        feat_imp = sorted(zip(feature_names, importances), key=lambda x: -x[1])
        print(f"\n  Feature importance (RF):")
        for fname, imp in feat_imp:
            print(f"    {fname}: {imp:.4f}")

        elapsed = time.time() - t0

        # ---- Build dataset result ----
        ds_result = {
            "dataset": dname,
            "data_path": dpath,
            "n_instances": len(instances),
            "max_n": max_n,
            "n_subsamples": args.n_subsamples,
            "budget_per_instance": args.budget_per_instance,
            "seed": args.seed,
            "elapsed_seconds": round(elapsed, 1),
            "mean_f1_by_n": {str(n): round(v, 4) for n, v in mean_f1_by_n.items()},
            "optimal_n_distribution": {str(n): int(c) for n, c in dist.items()},
            "mean_optimal_n": round(float(optimal_ns_arr.mean()), 2),
            "cv_results": cv_results,
            "best_model": best_model_name,
            "feature_importance": {fn: round(float(imp), 4) for fn, imp in feat_imp},
            "evaluation": {
                "greedy_f1": round(greedy_f1, 4),
                "uniform_f1": round(uniform_f1, 4),
                "adaptive_f1": round(adaptive_f1, 4),
                "oracle_adaptive_f1": round(oracle_f1, 4),
                "full_n_f1": round(full_f1, 4),
                "delta_adaptive_vs_uniform": round(adaptive_f1 - uniform_f1, 4),
                "delta_oracle_vs_uniform": round(oracle_f1 - uniform_f1, 4),
                "adaptive_avg_n": round(adaptive_avg_n, 2),
                "oracle_avg_n": round(oracle_avg_n, 2),
                "adaptive_allocation_dist": {str(n): int(c) for n, c in adapted_dist.items()},
                "adaptive_total_budget": adaptive_total,
            },
        }
        all_results[dname] = ds_result

        # save per-instance details
        per_instance = []
        for i, inst in enumerate(instances):
            per_instance.append({
                "text": inst.get("text", "")[:100],
                "features": features_list[i],
                "f1_by_n": {str(n): round(inst_f1_by_n[i][n], 4) for n in valid_ns},
                "optimal_n": optimal_ns[i],
                "predicted_n": predicted_ns[i],
                "adapted_n": adapted_ns[i],
            })

        detail_path = os.path.join(args.output_dir, f"instance_details_{dname}.jsonl")
        with open(detail_path, "w") as f:
            for item in per_instance:
                f.write(json.dumps(item, ensure_ascii=False) + "\n")
        print(f"\n  Saved instance details: {detail_path}")

    # ---- Save aggregate results ----
    out_path = os.path.join(args.output_dir, "asb_results.json")
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    print(f"\nSaved: {out_path}")

    # ---- Print summary ----
    print(f"\n{'='*70}")
    print("ASB Adaptive Sample Budget — Summary")
    print(f"{'='*70}")
    for dname, res in all_results.items():
        ev = res["evaluation"]
        print(f"\n  {dname}:")
        print(f"    Instances: {res['n_instances']}")
        print(f"    Uniform N={args.budget_per_instance}: F1={ev['uniform_f1']:.4f}")
        print(f"    Adaptive:         F1={ev['adaptive_f1']:.4f} (Δ={ev['delta_adaptive_vs_uniform']:+.4f})")
        print(f"    Oracle:           F1={ev['oracle_adaptive_f1']:.4f} (Δ={ev['delta_oracle_vs_uniform']:+.4f})")
        print(f"    Best predictor: {res['best_model']} (macro_F1={res['cv_results'][res['best_model']]['macro_f1']:.4f})")
        print(f"    Optimal N dist: {res['optimal_n_distribution']}")

    print(f"\n  NOTE: This is a CPU-only experiment. No GPU required.")
    print("DONE")


if __name__ == "__main__":
    main()
