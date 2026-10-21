#!/usr/bin/env python3
"""Backup 3: Distillation-based Verifier — supervised entity-level binary classifier.

Trains LR / RF / MLP to predict whether a candidate entity is in the gold set,
using 6 lightweight features (LP score, agreement ratio, degeneracy flag,
span length, type consistency, N). Classifier probabilities replace MV
frequency voting for weighted entity construction.

Input:  samples.jsonl files from SCS experiments (N=8, T=1.0)
Output: JSON with per-fold AUROC + downstream F1 (weighted MV vs standard MV)

Dependencies: numpy, scikit-learn (no GPU needed)
"""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler

# ── Default data paths (on autodl-5090) ──────────────────────────────────────
BASE = Path("/root/autodl-tmp/struct_self_consist_ie")
DEFAULT_PATHS = {
    "scierc": BASE / "output" / "exp_026_t10_seed42" / "samples.jsonl",
    "conll":  BASE / "output" / "exp_002_conll_n16" / "samples.jsonl",
    "fewnerd": BASE / "output" / "exp_021_inference" / "samples.jsonl",
}
# CoNLL file has N=16; we subsample to first 8.
SUBSAMPLE_N = {"conll": 8}


# ── Entity helpers ───────────────────────────────────────────────────────────

def entity_key(e):
    """Canonical entity identity: (start, end, type)."""
    return (e["start"], e["end"], e["type"])


def entity_set(entities):
    return frozenset(entity_key(e) for e in entities)


def compute_f1_sets(pred_set, gold_set):
    if not pred_set and not gold_set:
        return 1.0, 1.0, 1.0
    if not pred_set or not gold_set:
        return 0.0, 0.0, 0.0
    tp = len(pred_set & gold_set)
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    f1 = 2 * p * r / (p + r) if (p + r) > 0 else 0.0
    return p, r, f1


# ── Feature extraction ──────────────────────────────────────────────────────

def extract_entity_features(instance, target_n=None):
    """Extract per-entity feature vectors and labels from one instance.

    Returns list of (feature_vector, label, entity_key) tuples.
    """
    gold_ents = entity_set(instance["gold"]["entities"])
    samples = instance.get("samples", [])
    if target_n and len(samples) > target_n:
        samples = samples[:target_n]
    N = len(samples)
    if N < 2:
        return []

    sample_entity_sets = [entity_set(s["entities"]) for s in samples]
    sample_lps = [s.get("mean_logprob", 0.0) for s in samples]

    # Degeneracy: are all sample entity sets identical?
    degeneracy_flag = 1.0 if len(set(sample_entity_sets)) == 1 else 0.0

    # Collect all unique entities across samples
    all_entities = set()
    for s_set in sample_entity_sets:
        all_entities |= s_set

    # For type consistency: group by (start, end) span
    span_type_counts = {}  # (start, end) -> Counter of types
    for s in samples:
        for e in s["entities"]:
            span = (e["start"], e["end"])
            if span not in span_type_counts:
                span_type_counts[span] = Counter()
            span_type_counts[span][e["type"]] += 1

    results = []
    for ek in all_entities:
        start, end, etype = ek

        # Feature 1: LP score — mean of sample-level mean_logprob for samples containing this entity
        containing_indices = [i for i, s_set in enumerate(sample_entity_sets) if ek in s_set]
        lp_score = float(np.mean([sample_lps[i] for i in containing_indices]))

        # Feature 2: agreement ratio
        vote_count = len(containing_indices)
        agreement_ratio = vote_count / N

        # Feature 3: degeneracy flag (instance-level)
        # already computed above

        # Feature 4: span length (characters)
        span_length = end - start

        # Feature 5: type consistency — fraction of times this (start,end) gets this type
        span = (start, end)
        if span in span_type_counts:
            total_at_span = sum(span_type_counts[span].values())
            type_consistency = span_type_counts[span].get(etype, 0) / total_at_span
        else:
            type_consistency = 1.0

        # Feature 6: N
        n_samples = float(N)

        features = np.array([
            lp_score,
            agreement_ratio,
            degeneracy_flag,
            span_length,
            type_consistency,
            n_samples,
        ])

        label = 1 if ek in gold_ents else 0
        results.append((features, label, ek))

    return results


# ── Data loading ─────────────────────────────────────────────────────────────

def load_dataset(path, dataset_name, max_instances=None):
    """Load samples.jsonl and extract entity-level features.

    Returns:
        features: np.ndarray of shape (n_entities, 6)
        labels:   np.ndarray of shape (n_entities,)
        instance_meta: list of (instance_id, entity_keys, n_entities) for reconstruction
    """
    target_n = SUBSAMPLE_N.get(dataset_name)
    all_features = []
    all_labels = []
    instance_meta = []

    with open(path) as f:
        for i, line in enumerate(f):
            if max_instances and i >= max_instances:
                break
            inst = json.loads(line)
            entity_data = extract_entity_features(inst, target_n=target_n)
            if not entity_data:
                instance_meta.append((inst["id"], [], 0))
                continue
            feats, labs, ekeys = zip(*entity_data)
            start_idx = len(all_features)
            all_features.extend(feats)
            all_labels.extend(labs)
            instance_meta.append((inst["id"], list(ekeys), len(feats)))

    if not all_features:
        return np.zeros((0, 6)), np.zeros(0), instance_meta

    return np.array(all_features), np.array(all_labels), instance_meta


def load_all_data(data_dir, datasets=("scierc", "conll", "fewnerd"), max_instances=None):
    """Load all datasets. Returns dict keyed by dataset name."""
    result = {}
    for ds in datasets:
        path = data_dir / DEFAULT_PATHS[ds].name if data_dir != BASE else DEFAULT_PATHS[ds]
        if not path.exists():
            path = DEFAULT_PATHS[ds]
        print(f"Loading {ds} from {path} ...", flush=True)
        features, labels, meta = load_dataset(path, ds, max_instances=max_instances)
        result[ds] = {
            "features": features,
            "labels": labels,
            "meta": meta,
            "n_entities": len(labels),
            "n_positive": int(labels.sum()) if len(labels) > 0 else 0,
            "n_instances": sum(1 for _, _, n in meta if n > 0),
        }
        print(f"  {ds}: {result[ds]['n_instances']} instances, "
              f"{result[ds]['n_entities']} entities, "
              f"{result[ds]['n_positive']} positive ({result[ds]['n_positive']/max(result[ds]['n_entities'],1)*100:.1f}%)",
              flush=True)
    return result


# ── Instance-level reconstruction for downstream F1 ─────────────────────────

def load_instances_raw(path, dataset_name, max_instances=None):
    """Load raw instances for F1 evaluation."""
    target_n = SUBSAMPLE_N.get(dataset_name)
    instances = []
    with open(path) as f:
        for i, line in enumerate(f):
            if max_instances and i >= max_instances:
                break
            inst = json.loads(line)
            samples = inst.get("samples", [])
            if target_n and len(samples) > target_n:
                inst["samples"] = samples[:target_n]
            instances.append(inst)
    return instances


def evaluate_weighted_mv(instances, classifier, scaler, dataset_name,
                         threshold=0.5, sweep_thresholds=None):
    """Evaluate weighted MV vs standard MV on a list of instances.

    Returns dict with standard_mv_f1, weighted_mv_f1, and optionally best_threshold results.
    """
    target_n = SUBSAMPLE_N.get(dataset_name)
    total_tp_std = total_fp_std = total_fn_std = 0
    total_tp_w = total_fp_w = total_fn_w = 0

    # For threshold sweep
    if sweep_thresholds is None:
        sweep_thresholds = [0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7]
    sweep_counts = {t: {"tp": 0, "fp": 0, "fn": 0} for t in sweep_thresholds}

    for inst in instances:
        gold_ents = entity_set(inst["gold"]["entities"])
        entity_data = extract_entity_features(inst, target_n=target_n)
        if not entity_data:
            total_fn_std += len(gold_ents)
            total_fn_w += len(gold_ents)
            for t in sweep_thresholds:
                sweep_counts[t]["fn"] += len(gold_ents)
            continue

        feats, _, ekeys = zip(*entity_data)
        feats_arr = np.array(feats)
        feats_scaled = scaler.transform(feats_arr)

        # Agreement ratios (feature index 1)
        agreement_ratios = feats_arr[:, 1]

        # Standard MV: entities with agreement >= 0.5
        std_mv_set = frozenset(ek for ek, ar in zip(ekeys, agreement_ratios) if ar >= 0.5)

        # Classifier probabilities
        probs = classifier.predict_proba(feats_scaled)[:, 1]

        # Weighted MV: classifier_prob as score, threshold = 0.5
        weighted_set = frozenset(ek for ek, p in zip(ekeys, probs) if p >= threshold)

        # Standard MV counts
        tp = len(std_mv_set & gold_ents)
        total_tp_std += tp
        total_fp_std += len(std_mv_set - gold_ents)
        total_fn_std += len(gold_ents - std_mv_set)

        # Weighted MV counts
        tp_w = len(weighted_set & gold_ents)
        total_tp_w += tp_w
        total_fp_w += len(weighted_set - gold_ents)
        total_fn_w += len(gold_ents - weighted_set)

        # Threshold sweep
        for t in sweep_thresholds:
            t_set = frozenset(ek for ek, p in zip(ekeys, probs) if p >= t)
            sweep_counts[t]["tp"] += len(t_set & gold_ents)
            sweep_counts[t]["fp"] += len(t_set - gold_ents)
            sweep_counts[t]["fn"] += len(gold_ents - t_set)

    def f1_from_counts(tp, fp, fn):
        p = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        r = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        return 2 * p * r / (p + r) if (p + r) > 0 else 0.0

    std_f1 = f1_from_counts(total_tp_std, total_fp_std, total_fn_std)
    weighted_f1 = f1_from_counts(total_tp_w, total_fp_w, total_fn_w)

    sweep_f1s = {}
    for t in sweep_thresholds:
        sweep_f1s[str(t)] = f1_from_counts(
            sweep_counts[t]["tp"], sweep_counts[t]["fp"], sweep_counts[t]["fn"]
        )
    best_t = max(sweep_f1s, key=sweep_f1s.get)
    best_sweep_f1 = sweep_f1s[best_t]

    return {
        "standard_mv_f1": std_f1,
        "weighted_mv_f1_at_0.5": weighted_f1,
        "best_threshold": float(best_t),
        "best_weighted_f1": best_sweep_f1,
        "threshold_sweep": sweep_f1s,
        "delta_best_vs_std": best_sweep_f1 - std_f1,
    }


# ── Classifiers ──────────────────────────────────────────────────────────────

def get_classifiers(seed):
    return {
        "LogisticRegression": LogisticRegression(
            max_iter=1000, class_weight="balanced", random_state=seed, C=1.0
        ),
        "RandomForest": RandomForestClassifier(
            n_estimators=100, class_weight="balanced", random_state=seed, max_depth=8
        ),
        "MLP": MLPClassifier(
            hidden_layer_sizes=(64, 32), max_iter=500, random_state=seed,
            early_stopping=True, validation_fraction=0.1
        ),
    }

FEATURE_NAMES = [
    "lp_score", "agreement_ratio", "degeneracy_flag",
    "span_length", "type_consistency", "n_samples"
]


# ── Leave-one-dataset-out CV ────────────────────────────────────────────────

def leave_one_dataset_out_cv(data, seed, max_instances_eval=None):
    """3-fold leave-one-dataset-out cross-validation.

    For each fold: train on 2 datasets, test on the held-out dataset.
    Report entity-level AUROC and downstream F1.
    """
    datasets = list(data.keys())
    results = {}

    for held_out in datasets:
        print(f"\n{'='*60}")
        print(f"Fold: held-out = {held_out}")
        print(f"{'='*60}")

        # Combine training data
        train_feats = []
        train_labels = []
        for ds in datasets:
            if ds == held_out:
                continue
            train_feats.append(data[ds]["features"])
            train_labels.append(data[ds]["labels"])

        X_train = np.concatenate(train_feats)
        y_train = np.concatenate(train_labels)
        X_test = data[held_out]["features"]
        y_test = data[held_out]["labels"]

        print(f"  Train: {len(X_train)} entities ({int(y_train.sum())} pos, "
              f"{len(y_train)-int(y_train.sum())} neg)")
        print(f"  Test:  {len(X_test)} entities ({int(y_test.sum())} pos, "
              f"{len(y_test)-int(y_test.sum())} neg)")

        if len(X_test) == 0 or len(np.unique(y_test)) < 2:
            print(f"  SKIP: insufficient test data")
            results[held_out] = {"skip": True}
            continue

        # Scale features
        scaler = StandardScaler()
        X_train_s = scaler.fit_transform(X_train)
        X_test_s = scaler.transform(X_test)

        fold_results = {"n_train": len(X_train), "n_test": len(X_test)}
        classifiers = get_classifiers(seed)

        for clf_name, clf in classifiers.items():
            print(f"\n  Training {clf_name} ...")
            clf.fit(X_train_s, y_train)

            # Entity-level AUROC
            if hasattr(clf, "predict_proba"):
                probs = clf.predict_proba(X_test_s)[:, 1]
            else:
                probs = clf.decision_function(X_test_s)

            try:
                auroc = roc_auc_score(y_test, probs)
            except ValueError:
                auroc = float("nan")

            print(f"    AUROC: {auroc:.4f}")

            # Downstream F1 evaluation
            test_instances = load_instances_raw(
                DEFAULT_PATHS[held_out], held_out,
                max_instances=max_instances_eval
            )
            f1_results = evaluate_weighted_mv(
                test_instances, clf, scaler, held_out
            )
            print(f"    Standard MV F1:    {f1_results['standard_mv_f1']:.4f}")
            print(f"    Weighted MV F1:    {f1_results['weighted_mv_f1_at_0.5']:.4f}")
            print(f"    Best weighted F1:  {f1_results['best_weighted_f1']:.4f} (θ={f1_results['best_threshold']})")
            print(f"    Δ(best - std):     {f1_results['delta_best_vs_std']:+.4f}")

            fold_results[clf_name] = {
                "auroc": auroc,
                **f1_results,
            }

            # Feature importance (for interpretability)
            if clf_name == "LogisticRegression":
                coefs = dict(zip(FEATURE_NAMES, clf.coef_[0].tolist()))
                fold_results[clf_name]["coefficients"] = coefs
                print(f"    Coefficients: {coefs}")
            elif clf_name == "RandomForest":
                importances = dict(zip(FEATURE_NAMES, clf.feature_importances_.tolist()))
                fold_results[clf_name]["feature_importances"] = importances
                print(f"    Feature importances: {importances}")

        results[held_out] = fold_results

    return results


# ── Main ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Backup 3: Distillation-based Verifier — entity-level supervised classifier"
    )
    parser.add_argument("--data_dir", type=str, default=str(BASE),
                        help="Base directory for data files")
    parser.add_argument("--output_dir", type=str,
                        default=str(BASE / "output" / "distill_verifier"),
                        help="Output directory for results")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--max_instances", type=int, default=None,
                        help="Max instances per dataset (for debugging)")
    args = parser.parse_args()

    np.random.seed(args.seed)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load data
    print("=" * 60)
    print("Loading data ...")
    print("=" * 60)
    data = load_all_data(
        Path(args.data_dir),
        max_instances=args.max_instances,
    )

    # Summary
    total_entities = sum(d["n_entities"] for d in data.values())
    total_positive = sum(d["n_positive"] for d in data.values())
    print(f"\nTotal: {total_entities} entities, {total_positive} positive "
          f"({total_positive/max(total_entities,1)*100:.1f}%)")

    # Leave-one-dataset-out CV
    print("\n" + "=" * 60)
    print("Leave-one-dataset-out cross-validation")
    print("=" * 60)
    cv_results = leave_one_dataset_out_cv(
        data, args.seed,
        max_instances_eval=args.max_instances,
    )

    # Aggregate summary
    summary = {
        "experiment": "backup3_distill_verifier",
        "seed": args.seed,
        "data_summary": {
            ds: {
                "n_instances": d["n_instances"],
                "n_entities": d["n_entities"],
                "n_positive": d["n_positive"],
                "positive_rate": d["n_positive"] / max(d["n_entities"], 1),
            }
            for ds, d in data.items()
        },
        "cv_results": cv_results,
        "aggregate": {},
    }

    # Compute mean AUROC and F1 delta across folds per classifier
    clf_names = ["LogisticRegression", "RandomForest", "MLP"]
    for clf_name in clf_names:
        aurocs = []
        deltas = []
        for ds in cv_results:
            if "skip" in cv_results[ds]:
                continue
            if clf_name in cv_results[ds]:
                a = cv_results[ds][clf_name].get("auroc", float("nan"))
                if not np.isnan(a):
                    aurocs.append(a)
                d = cv_results[ds][clf_name].get("delta_best_vs_std", 0)
                deltas.append(d)
        summary["aggregate"][clf_name] = {
            "mean_auroc": float(np.mean(aurocs)) if aurocs else None,
            "std_auroc": float(np.std(aurocs)) if aurocs else None,
            "mean_delta_f1": float(np.mean(deltas)) if deltas else None,
            "per_fold_auroc": aurocs,
            "per_fold_delta_f1": deltas,
        }

    # Save
    out_path = output_dir / "distill_verifier_results.json"
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2, default=str)
    print(f"\nResults saved to {out_path}")

    # Print aggregate
    print("\n" + "=" * 60)
    print("AGGREGATE RESULTS")
    print("=" * 60)
    for clf_name in clf_names:
        agg = summary["aggregate"][clf_name]
        print(f"\n{clf_name}:")
        print(f"  Mean AUROC:    {agg['mean_auroc']:.4f} ± {agg['std_auroc']:.4f}" if agg["mean_auroc"] else "  Mean AUROC: N/A")
        print(f"  Mean Δ F1:     {agg['mean_delta_f1']:+.4f}" if agg["mean_delta_f1"] is not None else "  Mean Δ F1: N/A")


if __name__ == "__main__":
    main()
