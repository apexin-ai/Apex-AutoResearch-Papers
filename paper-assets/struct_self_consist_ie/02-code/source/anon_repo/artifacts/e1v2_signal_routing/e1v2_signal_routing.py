#!/usr/bin/env python3
"""E1v2 Adaptive Signal Routing: deployment-available features only.

Removes oracle_headroom and all ground-truth-dependent features from E1.
Uses only deployment-available signals: model_size, regime, degeneracy_rate,
lp_variance, vc_variance + interaction terms.
Trains GradientBoosting and RandomForest classifiers with 5-fold CV and LOO.
"""

import json
import os
import sys
from collections import Counter, defaultdict

import numpy as np
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, LeaveOneOut
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report

BASE = "/root/autodl-tmp/struct_self_consist_ie"
OUT = os.path.join(BASE, "output")
RESULTS_DIR = os.path.join(BASE, "artifacts", "e1v2_signal_routing")

# ============================================================
# E1 config data (from routing_results.json)
# ============================================================
E1_CONFIGS = [
    {"config_id": "Qwen3_8B_ft_scierc_s456", "model_size": 8, "regime": "ft", "dataset": "scierc",
     "degeneracy_rate": 0.1928, "greedy_f1": 0.6453, "oracle_f1": 0.7726,
     "construction_deltas_pp": {"lp_selection": -0.3, "majority_vote": -2.04, "consensus_theta2n": 0.4, "consensus_lp_weighted": -0.35}},
    {"config_id": "Qwen3_8B_ft_scierc_s789", "model_size": 8, "regime": "ft", "dataset": "scierc",
     "degeneracy_rate": 0.2136, "greedy_f1": 0.6428, "oracle_f1": 0.7767,
     "construction_deltas_pp": {"lp_selection": 0.86, "majority_vote": -4.01, "consensus_theta2n": 1.12, "consensus_lp_weighted": 0.4}},
    {"config_id": "Qwen3_8B_ft_conll_s123", "model_size": 8, "regime": "ft", "dataset": "conll",
     "degeneracy_rate": 0.6295, "greedy_f1": 0.9074, "oracle_f1": 0.9477,
     "construction_deltas_pp": {"lp_selection": -0.6, "majority_vote": -1.29, "consensus_theta2n": -1.01, "consensus_lp_weighted": -0.42}},
    {"config_id": "Qwen3_8B_ft_conll_s456", "model_size": 8, "regime": "ft", "dataset": "conll",
     "degeneracy_rate": 0.6303, "greedy_f1": 0.9076, "oracle_f1": 0.9443,
     "construction_deltas_pp": {"lp_selection": -0.77, "majority_vote": -1.46, "consensus_theta2n": -1.17, "consensus_lp_weighted": -0.42}},
    {"config_id": "Qwen3_8B_ft_fewnerd_s123", "model_size": 8, "regime": "ft", "dataset": "fewnerd",
     "degeneracy_rate": 0.1307, "greedy_f1": 0.7482, "oracle_f1": 0.8771,
     "construction_deltas_pp": {"lp_selection": 1.37, "majority_vote": -7.78, "consensus_theta2n": 1.56, "consensus_lp_weighted": -0.06}},
    {"config_id": "Qwen3_8B_ft_fewnerd_s456", "model_size": 8, "regime": "ft", "dataset": "fewnerd",
     "degeneracy_rate": 0.12, "greedy_f1": 0.7483, "oracle_f1": 0.8755,
     "construction_deltas_pp": {"lp_selection": 1.37, "majority_vote": -5.9, "consensus_theta2n": 0.91, "consensus_lp_weighted": 0.06}},
    {"config_id": "Qwen3_8B_ft_fewnerd_s789", "model_size": 8, "regime": "ft", "dataset": "fewnerd",
     "degeneracy_rate": 0.1177, "greedy_f1": 0.7483, "oracle_f1": 0.8716,
     "construction_deltas_pp": {"lp_selection": 1.35, "majority_vote": -13.97, "consensus_theta2n": 0.19, "consensus_lp_weighted": -1.24}},
    {"config_id": "Qwen2.5_72B_zs_scierc_sNone", "model_size": 72, "regime": "zs", "dataset": "scierc",
     "degeneracy_rate": 0.2098, "greedy_f1": 0.3993, "oracle_f1": 0.5489,
     "construction_deltas_pp": {"lp_selection": -0.1, "majority_vote": 1.39, "consensus_theta2n": -0.52, "consensus_lp_weighted": 1.53}},
    {"config_id": "Qwen2.5_72B_zs_conll_sNone", "model_size": 72, "regime": "zs", "dataset": "conll",
     "degeneracy_rate": 0.6771, "greedy_f1": 0.712, "oracle_f1": 0.7651,
     "construction_deltas_pp": {"lp_selection": -0.39, "majority_vote": -0.85, "consensus_theta2n": -0.92, "consensus_lp_weighted": -0.37}},
    {"config_id": "Qwen2.5_72B_zs_fewnerd_sNone", "model_size": 72, "regime": "zs", "dataset": "fewnerd",
     "degeneracy_rate": 0.4622, "greedy_f1": 0.6281, "oracle_f1": 0.7072,
     "construction_deltas_pp": {"lp_selection": -0.4, "majority_vote": -0.19, "consensus_theta2n": -1.7, "consensus_lp_weighted": -0.2}},
    {"config_id": "Qwen2.5_72B_fs_scierc_sNone", "model_size": 72, "regime": "fs", "dataset": "scierc",
     "degeneracy_rate": 0.1664, "greedy_f1": 0.4615, "oracle_f1": 0.6044,
     "construction_deltas_pp": {"lp_selection": -1.36, "majority_vote": -0.62, "consensus_theta2n": -1.4, "consensus_lp_weighted": -0.08}},
    {"config_id": "Qwen2.5_72B_fs_conll_sNone", "model_size": 72, "regime": "fs", "dataset": "conll",
     "degeneracy_rate": 0.7003, "greedy_f1": 0.745, "oracle_f1": 0.7958,
     "construction_deltas_pp": {"lp_selection": 0.24, "majority_vote": -0.22, "consensus_theta2n": -0.5, "consensus_lp_weighted": 0.03}},
    {"config_id": "Qwen2.5_72B_fs_fewnerd_sNone", "model_size": 72, "regime": "fs", "dataset": "fewnerd",
     "degeneracy_rate": 0.452, "greedy_f1": 0.6189, "oracle_f1": 0.7017,
     "construction_deltas_pp": {"lp_selection": -0.14, "majority_vote": 0.06, "consensus_theta2n": -1.42, "consensus_lp_weighted": 0.02}},
    {"config_id": "Qwen2.5_7B_ft_fewnerd_s42", "model_size": 7, "regime": "ft", "dataset": "fewnerd",
     "degeneracy_rate": 0.3109, "greedy_f1": 0.7851, "oracle_f1": 0.8718,
     "construction_deltas_pp": {"lp_selection": 0.39, "majority_vote": -2.67, "consensus_theta2n": -0.06, "consensus_lp_weighted": -0.4}},
    {"config_id": "Qwen2.5_7B_ft_fewnerd_s123", "model_size": 7, "regime": "ft", "dataset": "fewnerd",
     "degeneracy_rate": 0.3276, "greedy_f1": 0.785, "oracle_f1": 0.8777,
     "construction_deltas_pp": {"lp_selection": 0.38, "majority_vote": -2.13, "consensus_theta2n": 0.29, "consensus_lp_weighted": -0.03}},
    {"config_id": "Qwen2.5_7B_ft_fewnerd_s456", "model_size": 7, "regime": "ft", "dataset": "fewnerd",
     "degeneracy_rate": 0.3129, "greedy_f1": 0.7825, "oracle_f1": 0.8771,
     "construction_deltas_pp": {"lp_selection": 0.52, "majority_vote": -1.77, "consensus_theta2n": 0.14, "consensus_lp_weighted": 0.09}},
]

# Best-match mapping: config_id → samples.jsonl path (relative to BASE)
# For FT 8B Qwen3 configs, matching by dataset+seed
# For 72B/7B configs, no raw samples available
SAMPLES_MAP = {
    "Qwen3_8B_ft_scierc_s456":  "output/exp_001_seed456_v2_ner/samples.jsonl",
    "Qwen3_8B_ft_scierc_s789":  "output/exp_001_seed123_v2/samples.jsonl",  # proxy: same model/dataset, different seed
    "Qwen3_8B_ft_conll_s123":   "output/exp_002_conll_n8_seed123/samples.jsonl",
    "Qwen3_8B_ft_conll_s456":   "output/exp_002_conll_n8_seed456/samples.jsonl",
    "Qwen3_8B_ft_fewnerd_s123": "output/exp_021_fewnerd_n8_seed123/samples.jsonl",
    "Qwen3_8B_ft_fewnerd_s456": "output/exp_021_fewnerd_n8_seed456/samples.jsonl",
    "Qwen3_8B_ft_fewnerd_s789": "output/fewnerd_seed789_merged/samples.jsonl",
}


class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (np.integer,)): return int(obj)
        if isinstance(obj, (np.floating,)): return float(obj)
        if isinstance(obj, (np.bool_,)): return bool(obj)
        if isinstance(obj, np.ndarray): return obj.tolist()
        return super().default(obj)


def compute_variance_from_samples(samples_path, max_instances=5000):
    """Compute lp_variance and vc_variance from a samples.jsonl file.

    lp_variance: mean across instances of var(mean_logprob across N samples)
    vc_variance: mean across instances of var(normalized_vote_count across N samples)
    """
    lp_vars = []
    vc_vars = []
    n_processed = 0

    with open(samples_path) as f:
        for line in f:
            if n_processed >= max_instances:
                break
            try:
                inst = json.loads(line)
            except json.JSONDecodeError:
                continue

            samples = inst.get("samples", [])
            N = len(samples)
            if N < 2:
                continue

            # LP variance: variance of mean_logprob across N samples
            logprobs = []
            for s in samples:
                lp = s.get("mean_logprob")
                if lp is None:
                    lp = s.get("cumulative_logprob", 0) / max(s.get("n_tokens", 1), 1)
                logprobs.append(lp)
            lp_vars.append(float(np.var(logprobs)))

            # VC variance: for each sample, compute its "vote count"
            # (fraction of other samples producing the same entity set)
            entity_sets = []
            for s in samples:
                es = frozenset(
                    (e.get("start", 0), e.get("end", 0), e.get("type", ""))
                    for e in s.get("entities", [])
                )
                entity_sets.append(es)

            vote_counts = [
                sum(1 for j in range(N) if entity_sets[j] == entity_sets[i]) / N
                for i in range(N)
            ]
            vc_vars.append(float(np.var(vote_counts)))
            n_processed += 1

    if not lp_vars:
        return None, None

    return float(np.mean(lp_vars)), float(np.mean(vc_vars))


def get_label(config):
    """Get best construction method label from delta_pp values."""
    deltas = config["construction_deltas_pp"]
    if not deltas:
        return "none"
    best_method = max(deltas, key=deltas.get)
    best_delta = deltas[best_method]
    return "none" if best_delta <= 0 else best_method


def build_feature_vector(config, lp_var, vc_var):
    """Build 8-dim feature vector: 5 base + 3 interactions."""
    regime_map = {"zs": 0, "fs": 1, "ft": 2}
    ms = config["model_size"]
    reg = regime_map[config["regime"]]
    deg = config["degeneracy_rate"]

    return [
        ms,           # model_size
        reg,          # regime
        deg,          # degeneracy_rate_estimate
        lp_var,       # lp_variance
        vc_var,       # vc_variance
        ms * reg,     # interaction: model_size × regime
        reg * deg,    # interaction: regime × degeneracy
        ms * deg,     # interaction: model_size × degeneracy
    ]


FEATURE_NAMES = [
    "model_size", "regime", "degeneracy_rate", "lp_variance", "vc_variance",
    "model_size×regime", "regime×degeneracy", "model_size×degeneracy"
]


def resolve_router_delta(predicted, deltas_pp):
    """Get the F1 delta for a predicted method."""
    if predicted == "none":
        return 0.0
    return deltas_pp.get(predicted, 0.0)


def run_classification(X, y, labels_text, le, configs, model_name, model_cls, model_kwargs):
    """Run both 5-fold CV and LOO evaluation."""
    n = len(y)
    class_names = [str(c) for c in le.classes_]

    results = {}

    # --- LOO (for direct comparison with E1) ---
    loo = LeaveOneOut()
    loo_preds = []
    loo_pred_labels = []

    for train_idx, test_idx in loo.split(X):
        scaler = StandardScaler()
        X_tr = scaler.fit_transform(X[train_idx])
        X_te = scaler.transform(X[test_idx])
        model = model_cls(**model_kwargs)
        model.fit(X_tr, y[train_idx])
        pred = model.predict(X_te)[0]
        loo_preds.append(pred)
        loo_pred_labels.append(str(le.inverse_transform([pred])[0]))

    loo_acc = float(np.mean(np.array(loo_preds) == y))

    # Router delta F1
    router_delta_sum = oracle_delta_sum = lp_delta_sum = 0.0
    for i, c in enumerate(configs):
        deltas = c["construction_deltas_pp"]
        router_delta_sum += resolve_router_delta(loo_pred_labels[i], deltas)
        oracle_delta_sum += max(max(deltas.values()), 0) if deltas else 0
        lp_delta_sum += deltas.get("lp_selection", 0)

    # Confusion matrix
    cm = confusion_matrix(y, loo_preds, labels=range(len(class_names)))

    # Feature importance from full model
    scaler_full = StandardScaler()
    X_full = scaler_full.fit_transform(X)
    full_model = model_cls(**model_kwargs)
    full_model.fit(X_full, y)

    if hasattr(full_model, "feature_importances_"):
        imp = full_model.feature_importances_
    elif hasattr(full_model, "coef_"):
        imp = np.abs(full_model.coef_).mean(axis=0) if full_model.coef_.ndim > 1 else np.abs(full_model.coef_)
    else:
        imp = np.zeros(X.shape[1])

    feature_imp = sorted(
        {FEATURE_NAMES[i]: round(float(imp[i]), 4) for i in range(len(FEATURE_NAMES))}.items(),
        key=lambda x: -x[1]
    )

    # Per-config LOO predictions
    per_config_loo = []
    for i, c in enumerate(configs):
        deltas = c["construction_deltas_pp"]
        pd_ = resolve_router_delta(loo_pred_labels[i], deltas)
        per_config_loo.append({
            "config_id": c["config_id"],
            "actual": labels_text[i],
            "predicted": loo_pred_labels[i],
            "correct": labels_text[i] == loo_pred_labels[i],
            "predicted_delta_pp": round(pd_, 2),
        })

    results["loo"] = {
        "accuracy": round(loo_acc, 4),
        "n_correct": int(loo_acc * n),
        "n_total": n,
        "router_avg_delta_pp": round(router_delta_sum / n, 2),
        "always_lp_avg_delta_pp": round(lp_delta_sum / n, 2),
        "oracle_avg_delta_pp": round(oracle_delta_sum / n, 2),
        "feature_importance": dict(feature_imp),
        "confusion_matrix": {"classes": class_names, "matrix": cm.tolist()},
        "per_config_predictions": per_config_loo,
    }

    # --- 5-fold CV ---
    n_splits = min(5, n)
    if len(set(y)) < 2:
        results["cv5"] = {"error": "insufficient class diversity"}
        return results

    # Use stratified if possible, else regular KFold
    try:
        skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
        folds = list(skf.split(X, y))
    except ValueError:
        from sklearn.model_selection import KFold
        kf = KFold(n_splits=n_splits, shuffle=True, random_state=42)
        folds = list(kf.split(X))

    fold_accs = []
    all_cv_preds = np.zeros(n, dtype=int)
    all_cv_pred_labels = [""] * n

    for train_idx, test_idx in folds:
        scaler = StandardScaler()
        X_tr = scaler.fit_transform(X[train_idx])
        X_te = scaler.transform(X[test_idx])
        model = model_cls(**model_kwargs)
        model.fit(X_tr, y[train_idx])
        preds = model.predict(X_te)
        fold_accs.append(float(np.mean(preds == y[test_idx])))
        for j, idx in enumerate(test_idx):
            all_cv_preds[idx] = preds[j]
            all_cv_pred_labels[idx] = str(le.inverse_transform([preds[j]])[0])

    cv_mean = float(np.mean(fold_accs))
    cv_std = float(np.std(fold_accs))
    cv_overall_acc = float(np.mean(all_cv_preds == y))

    # Router delta for CV
    cv_router_delta = sum(
        resolve_router_delta(all_cv_pred_labels[i], configs[i]["construction_deltas_pp"])
        for i in range(n)
    ) / n

    results["cv5"] = {
        "mean_accuracy": round(cv_mean, 4),
        "std_accuracy": round(cv_std, 4),
        "overall_accuracy": round(cv_overall_acc, 4),
        "fold_accuracies": [round(a, 4) for a in fold_accs],
        "router_avg_delta_pp": round(cv_router_delta, 2),
    }

    return results


def main():
    os.makedirs(RESULTS_DIR, exist_ok=True)

    print("=" * 70)
    print("E1v2: Signal Routing with Deployment-Available Features")
    print("=" * 70)

    # Step 1: Compute variance features from available samples
    print("\n--- Phase 1: Computing variance features from samples.jsonl ---")
    variance_data = {}

    for config_id, rel_path in SAMPLES_MAP.items():
        full_path = os.path.join(BASE, rel_path)
        if not os.path.exists(full_path):
            print(f"  {config_id}: MISSING ({rel_path})")
            continue

        print(f"  {config_id}: processing {rel_path}...", end="", flush=True)
        lp_var, vc_var = compute_variance_from_samples(full_path)
        if lp_var is not None:
            variance_data[config_id] = {"lp_variance": lp_var, "vc_variance": vc_var}
            print(f" lp_var={lp_var:.6f}, vc_var={vc_var:.6f}")
        else:
            print(" FAILED (no valid instances)")

    print(f"\n  Computed variance for {len(variance_data)}/{len(E1_CONFIGS)} configs")

    # Step 2: Impute missing variance using regime-group means
    # Group available data by regime
    regime_vars = defaultdict(lambda: {"lp": [], "vc": []})
    for config_id, vd in variance_data.items():
        cfg = next(c for c in E1_CONFIGS if c["config_id"] == config_id)
        regime_vars[cfg["regime"]]["lp"].append(vd["lp_variance"])
        regime_vars[cfg["regime"]]["vc"].append(vd["vc_variance"])

    # Compute regime means (fallback: global mean of all available)
    all_lp = [vd["lp_variance"] for vd in variance_data.values()]
    all_vc = [vd["vc_variance"] for vd in variance_data.values()]
    global_lp_mean = float(np.mean(all_lp)) if all_lp else 0.001
    global_vc_mean = float(np.mean(all_vc)) if all_vc else 0.01

    regime_means = {}
    for regime in ["ft", "zs", "fs"]:
        rv = regime_vars[regime]
        regime_means[regime] = {
            "lp": float(np.mean(rv["lp"])) if rv["lp"] else global_lp_mean,
            "vc": float(np.mean(rv["vc"])) if rv["vc"] else global_vc_mean,
        }

    print(f"\n  Regime means for imputation:")
    for r, m in regime_means.items():
        print(f"    {r}: lp_var={m['lp']:.6f}, vc_var={m['vc']:.6f}")

    # Step 3: Build feature matrix
    print("\n--- Phase 2: Building feature matrix ---")
    labels_text = []
    feature_matrix = []
    imputed_flags = []

    for c in E1_CONFIGS:
        label = get_label(c)
        labels_text.append(label)

        cid = c["config_id"]
        if cid in variance_data:
            lp_var = variance_data[cid]["lp_variance"]
            vc_var = variance_data[cid]["vc_variance"]
            imputed = False
        else:
            lp_var = regime_means[c["regime"]]["lp"]
            vc_var = regime_means[c["regime"]]["vc"]
            imputed = True

        fv = build_feature_vector(c, lp_var, vc_var)
        feature_matrix.append(fv)
        imputed_flags.append(imputed)

        print(f"  {cid:40s} label={label:25s} imputed={'Y' if imputed else 'N'}")

    X = np.array(feature_matrix)
    label_counts = Counter(labels_text)
    print(f"\n  Label distribution: {dict(label_counts)}")
    print(f"  Imputed: {sum(imputed_flags)}/{len(imputed_flags)} configs")

    le = LabelEncoder()
    y = le.fit_transform(labels_text)

    # Step 4: Train classifiers
    print("\n--- Phase 3: Classification ---")

    models = [
        ("GradientBoosting", GradientBoostingClassifier,
         {"n_estimators": 200, "max_depth": 4, "random_state": 42, "learning_rate": 0.1}),
        ("RandomForest", RandomForestClassifier,
         {"n_estimators": 200, "max_depth": 4, "random_state": 42}),
    ]

    all_results = {}
    for model_name, model_cls, model_kwargs in models:
        print(f"\n  {'=' * 60}")
        print(f"  {model_name}")
        print(f"  {'=' * 60}")

        res = run_classification(X, y, labels_text, le, E1_CONFIGS,
                                 model_name, model_cls, model_kwargs)

        loo = res["loo"]
        print(f"  LOO Accuracy:     {loo['accuracy']:.1%} ({loo['n_correct']}/{loo['n_total']})")
        print(f"  Router avg dF1:   {loo['router_avg_delta_pp']:+.2f} pp")
        print(f"  Always-LP dF1:    {loo['always_lp_avg_delta_pp']:+.2f} pp")
        print(f"  Oracle dF1:       {loo['oracle_avg_delta_pp']:+.2f} pp")
        print(f"  Top features: {list(loo['feature_importance'].items())[:5]}")

        cm = loo["confusion_matrix"]
        print(f"\n  Confusion matrix (classes: {cm['classes']}):")
        for ri, row in enumerate(cm["matrix"]):
            print(f"    {cm['classes'][ri]:25s}: {row}")

        print(f"\n  Per-config LOO predictions:")
        for p in loo["per_config_predictions"]:
            ok = "OK" if p["correct"] else "XX"
            print(f"    {p['config_id']:40s} true={p['actual']:25s} pred={p['predicted']:25s} [{ok}]")

        if "cv5" in res and "error" not in res["cv5"]:
            cv = res["cv5"]
            print(f"\n  5-fold CV:  {cv['mean_accuracy']:.1%} ± {cv['std_accuracy']:.1%}")
            print(f"  CV Router dF1: {cv['router_avg_delta_pp']:+.2f} pp")

        all_results[model_name] = res

    # Step 5: Comparison with E1
    print("\n\n" + "=" * 70)
    print("COMPARISON: E1 (with oracle) vs E1v2 (deployment-only)")
    print("=" * 70)

    e1_reference = {
        "LogisticRegression_LOO": {"accuracy": 0.5000, "router_delta_pp": 0.29},
        "RandomForest_LOO": {"accuracy": 0.5625, "router_delta_pp": 0.39},
    }

    print(f"\n  {'Model':<25s} {'E1 Acc':>8s} {'E1v2 Acc':>9s} {'E1 dF1':>8s} {'E1v2 dF1':>9s}")
    print(f"  {'-'*60}")

    for model_name in ["GradientBoosting", "RandomForest"]:
        e1v2_loo = all_results[model_name]["loo"]
        e1_key = "RandomForest_LOO"  # Compare both with E1's RF (best E1 model)
        e1_ref = e1_reference[e1_key]
        print(f"  {model_name:<25s} {e1_ref['accuracy']:>7.1%} {e1v2_loo['accuracy']:>8.1%} "
              f"{e1_ref['router_delta_pp']:>+7.2f} {e1v2_loo['router_avg_delta_pp']:>+8.2f}")

    print(f"\n  E1 best (RF LOO): accuracy=56.2%, top features: oracle_headroom, base_f1, degeneracy_rate")
    print(f"  E1 used 12 features including oracle_headroom, base_f1, rho_* (all require ground truth)")
    print(f"  E1v2 uses 8 features: 5 deployment-available + 3 interaction terms")

    # Step 6: Regime-specific analysis
    print("\n\n--- Regime-Specific Patterns ---")
    regime_configs = defaultdict(list)
    for i, c in enumerate(E1_CONFIGS):
        regime_configs[c["regime"]].append((i, c, labels_text[i]))

    for regime in ["ft", "zs", "fs"]:
        items = regime_configs[regime]
        print(f"\n  {regime.upper()} ({len(items)} configs):")
        method_counts = Counter(label for _, _, label in items)
        print(f"    Labels: {dict(method_counts)}")
        if len(set(label for _, _, label in items)) == 1:
            print(f"    → Single dominant method: {items[0][2]}")

    # Step 7: Save results
    output = {
        "experiment": "E1v2_signal_routing_deployment_features",
        "n_configs": len(E1_CONFIGS),
        "n_variance_computed": len(variance_data),
        "n_variance_imputed": sum(imputed_flags),
        "features_used": FEATURE_NAMES,
        "label_distribution": dict(label_counts),
        "variance_data": {k: {kk: round(vv, 6) for kk, vv in v.items()} for k, v in variance_data.items()},
        "regime_imputation_means": {k: {kk: round(vv, 6) for kk, vv in v.items()} for k, v in regime_means.items()},
        "models": all_results,
        "e1_comparison": {
            "e1_best_accuracy": 0.5625,
            "e1_best_model": "RandomForest_LOO",
            "e1_best_router_delta_pp": 0.39,
            "e1_features": ["model_size", "model_family", "dataset", "regime", "base_f1",
                           "degeneracy_rate", "oracle_headroom", "rho_SJ", "rho_FK",
                           "rho_LP", "rho_EM", "rho_VC"],
            "e1v2_features": FEATURE_NAMES,
            "key_removals": ["oracle_headroom", "base_f1", "rho_SJ", "rho_FK", "rho_LP", "rho_EM", "rho_VC"],
            "key_additions": ["lp_variance", "vc_variance", "model_size×regime",
                             "regime×degeneracy", "model_size×degeneracy"],
        },
    }

    results_path = os.path.join(RESULTS_DIR, "results.json")
    with open(results_path, "w") as f:
        json.dump(output, f, indent=2, cls=NumpyEncoder)
    print(f"\n\nResults saved to {results_path}")

    # Generate summary.md
    gb_loo = all_results["GradientBoosting"]["loo"]
    rf_loo = all_results["RandomForest"]["loo"]
    gb_cv = all_results["GradientBoosting"].get("cv5", {})
    rf_cv = all_results["RandomForest"].get("cv5", {})

    summary = f"""# E1v2: Signal Routing with Deployment-Available Features

## Key Change
Removed all ground-truth-dependent features (oracle_headroom, base_f1, rho_*).
Replaced with deployment-available features: lp_variance, vc_variance + interactions.

## Features (8 total)
- **Base (5)**: model_size, regime, degeneracy_rate, lp_variance, vc_variance
- **Interactions (3)**: model_size×regime, regime×degeneracy, model_size×degeneracy

## Results

| Model | LOO Acc | 5-fold CV | Router dF1 | Always-LP dF1 | Oracle dF1 |
|-------|---------|-----------|------------|---------------|------------|
| GradientBoosting | {gb_loo['accuracy']:.1%} ({gb_loo['n_correct']}/{gb_loo['n_total']}) | {gb_cv.get('mean_accuracy', 0):.1%} ± {gb_cv.get('std_accuracy', 0):.1%} | {gb_loo['router_avg_delta_pp']:+.2f}pp | {gb_loo['always_lp_avg_delta_pp']:+.2f}pp | {gb_loo['oracle_avg_delta_pp']:+.2f}pp |
| RandomForest | {rf_loo['accuracy']:.1%} ({rf_loo['n_correct']}/{rf_loo['n_total']}) | {rf_cv.get('mean_accuracy', 0):.1%} ± {rf_cv.get('std_accuracy', 0):.1%} | {rf_loo['router_avg_delta_pp']:+.2f}pp | {rf_loo['always_lp_avg_delta_pp']:+.2f}pp | {rf_loo['oracle_avg_delta_pp']:+.2f}pp |

## E1 vs E1v2 Comparison

| Metric | E1 (RF, LOO) | E1v2 GB (LOO) | E1v2 RF (LOO) |
|--------|-------------|---------------|---------------|
| Accuracy | 56.2% | {gb_loo['accuracy']:.1%} | {rf_loo['accuracy']:.1%} |
| Router dF1 | +0.39pp | {gb_loo['router_avg_delta_pp']:+.2f}pp | {rf_loo['router_avg_delta_pp']:+.2f}pp |
| Features | 12 (incl. oracle) | 8 (deploy-only) | 8 (deploy-only) |

## Top Features (GradientBoosting)
{chr(10).join(f"- {k}: {v:.4f}" for k, v in list(gb_loo['feature_importance'].items())[:5])}

## Top Features (RandomForest)
{chr(10).join(f"- {k}: {v:.4f}" for k, v in list(rf_loo['feature_importance'].items())[:5])}

## Data Notes
- {len(variance_data)}/{len(E1_CONFIGS)} configs had raw samples.jsonl available for variance computation
- {sum(imputed_flags)} configs used regime-group mean imputation for lp_variance/vc_variance
- Only FT 8B Qwen3 configs had raw samples; 72B (ZS/FS) and 7B configs were imputed

## Regime Patterns
"""
    for regime in ["ft", "zs", "fs"]:
        items = regime_configs[regime]
        method_counts = Counter(label for _, _, label in items)
        summary += f"- **{regime.upper()}** ({len(items)} configs): {dict(method_counts)}\n"

    summary_path = os.path.join(RESULTS_DIR, "summary.md")
    with open(summary_path, "w") as f:
        f.write(summary)
    print(f"Summary saved to {summary_path}")


if __name__ == "__main__":
    main()
