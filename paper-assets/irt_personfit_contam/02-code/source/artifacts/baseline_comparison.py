"""
Baseline comparison: Tier 1 + Tier 2 methods vs IRT lz* for contamination detection.

Model-level: accuracy z-score, lz*, HT, U3, Guttman errors
Item-level: lz* contribution, gain score, LR/RF cross-model
"""

import json
import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, precision_score
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────
QWEN_DIR = "/root/autodl-tmp/ctrl_contam_pilot"
LLAMA_DIR = "/root/autodl-tmp/ctrl_contam_llama"
OUT_DIR = "/root/autodl-tmp/baseline_comparison/results"
os.makedirs(OUT_DIR, exist_ok=True)

# ── Load data ──────────────────────────────────────────────────────────
def load_results(base_dir, conditions):
    data = {}
    for cond in conditions:
        path = f"{base_dir}/results/{cond}_results.json"
        with open(path) as f:
            d = json.load(f)
        data[cond] = {
            "response_vector": np.array(d["response_vector"], dtype=np.int8),
            "theta_mle": d["theta_mle"],
            "lz_star": d["lz_star"],
            "accuracy": d["accuracy_overall"],
        }
    return data

def load_seen_items(base_dir, pct):
    with open(f"{base_dir}/data/seen_items_{pct}pct.json") as f:
        return set(json.load(f))

params = pd.read_csv(f"{QWEN_DIR}/mmlu_params.csv")
a = params["a_discrimination"].values
b = params["b_difficulty"].values
c = params["c_guessing"].values
d_param = params["d_feasibility"].values
n_items = len(a)

qwen_conds = ["clean_s1", "clean_s2", "clean_s3", "contam_15", "contam_50"]
llama_conds_raw = ["clean", "clean_s2", "clean_s3", "contam_15", "contam_50"]
qwen = load_results(QWEN_DIR, qwen_conds)
llama = load_results(LLAMA_DIR, llama_conds_raw)

qwen_seen_15 = load_seen_items(QWEN_DIR, 15)
qwen_seen_50 = load_seen_items(QWEN_DIR, 50)
llama_seen_15 = load_seen_items(LLAMA_DIR, 15)
llama_seen_50 = load_seen_items(LLAMA_DIR, 50)

qwen_clean_keys = ["clean_s1", "clean_s2", "clean_s3"]
llama_clean_keys = ["clean", "clean_s2", "clean_s3"]

# ── IRT 4PL probability ────────────────────────────────────────────────
def irt_prob(theta, a, b, c, d_param):
    z = a * (theta - b)
    z = np.clip(z, -30, 30)
    p = c + (d_param - c) / (1.0 + np.exp(-z))
    return np.clip(p, 1e-10, 1 - 1e-10)

# ══════════════════════════════════════════════════════════════════════
# MODEL-LEVEL METRICS
# ══════════════════════════════════════════════════════════════════════

# ── 1. Accuracy z-score ────────────────────────────────────────────────
def acc_zscore(model_data, clean_keys, contam_key):
    clean_accs = np.array([model_data[k]["accuracy"] for k in clean_keys])
    contam_acc = model_data[contam_key]["accuracy"]
    mu = clean_accs.mean()
    sigma = clean_accs.std(ddof=1)
    z = (contam_acc - mu) / sigma if sigma > 0 else 0.0
    return {"value": float(z), "contam_acc": float(contam_acc),
            "clean_mean": float(mu), "clean_std": float(sigma)}

# ── 2. Person-fit statistics ───────────────────────────────────────────
def person_fit_stats(response_vector, b_difficulty):
    sort_idx = np.argsort(b_difficulty)
    x = response_vector[sort_idx]
    n = len(x)
    n_correct = int(x.sum())
    n_incorrect = n - n_correct

    # Guttman errors: pairs (i,j) i<j where x_i=0 and x_j=1
    # = for each j where x_j=1, count zeros before j
    zeros_cumsum = np.cumsum(1 - x)
    guttman_errors = int(np.sum(zeros_cumsum[x == 1]) - np.sum(x[x == 1]))
    # Fix: zeros_cumsum[j] includes position j itself if x_j=0, but x_j=1 here
    # zeros_cumsum[j] = number of zeros in positions 0..j
    # Since x_j=1, zeros before j = zeros_cumsum[j] (no zero at j itself)
    # Wait, zeros_cumsum[j] = sum of (1-x[0..j]) = number of zeros in 0..j
    # If x[j]=1, then (1-x[j])=0, so zeros_cumsum[j] = zeros in 0..j-1 + 0 = zeros before j ✓
    # If x[j]=0, zeros_cumsum[j] = zeros in 0..j-1 + 1
    # We only look at positions where x[j]=1, so zeros_cumsum[j] = number of zeros in 0..j-1. Correct.

    ones_positions = np.where(x == 1)[0]
    guttman_errors = int(np.sum(zeros_cumsum[ones_positions]))

    total_pairs = n * (n - 1) // 2
    max_guttman = n_correct * n_incorrect

    ht = guttman_errors / max_guttman if max_guttman > 0 else 0.0
    u3 = guttman_errors / total_pairs if total_pairs > 0 else 0.0

    return {
        "ht_statistic": float(ht),
        "u3_statistic": float(u3),
        "guttman_errors": int(guttman_errors),
        "max_guttman": int(max_guttman),
        "total_pairs": int(total_pairs),
        "n_correct": n_correct,
        "n_incorrect": n_incorrect,
    }

# ── 3. lz* (already computed, collect) ────────────────────────────────
def collect_lz_star(model_data, clean_keys, contam_key):
    clean_vals = np.array([model_data[k]["lz_star"] for k in clean_keys])
    contam_val = model_data[contam_key]["lz_star"]
    mu = clean_vals.mean()
    sigma = clean_vals.std(ddof=1)
    cohens_d = (contam_val - mu) / sigma if sigma > 0 else 0.0
    return {"value": float(contam_val), "cohens_d": float(cohens_d),
            "clean_mean": float(mu), "clean_std": float(sigma)}

# ── Compute model-level for all conditions ─────────────────────────────
def compute_model_level(model_name, model_data, clean_keys, contam_conditions):
    results = {}
    # Clean baselines
    for ck in clean_keys:
        pf = person_fit_stats(model_data[ck]["response_vector"], b)
        results[ck] = {
            "accuracy": float(model_data[ck]["accuracy"]),
            "lz_star": float(model_data[ck]["lz_star"]),
            "theta_mle": float(model_data[ck]["theta_mle"]),
            **{k: pf[k] for k in ["ht_statistic", "u3_statistic", "guttman_errors"]},
        }

    for contam_key in contam_conditions:
        pf = person_fit_stats(model_data[contam_key]["response_vector"], b)
        az = acc_zscore(model_data, clean_keys, contam_key)
        lz = collect_lz_star(model_data, clean_keys, contam_key)

        # Person-fit Cohen's d against clean seeds
        clean_ht = [person_fit_stats(model_data[k]["response_vector"], b)["ht_statistic"] for k in clean_keys]
        clean_u3 = [person_fit_stats(model_data[k]["response_vector"], b)["u3_statistic"] for k in clean_keys]
        clean_ge = [person_fit_stats(model_data[k]["response_vector"], b)["guttman_errors"] for k in clean_keys]

        def cohens_d(val, clean_vals):
            mu = np.mean(clean_vals)
            sigma = np.std(clean_vals, ddof=1)
            return float((val - mu) / sigma) if sigma > 0 else 0.0

        results[contam_key] = {
            "accuracy": float(model_data[contam_key]["accuracy"]),
            "acc_zscore": az,
            "lz_star": lz,
            "ht_statistic": {"value": pf["ht_statistic"],
                             "cohens_d": cohens_d(pf["ht_statistic"], clean_ht)},
            "u3_statistic": {"value": pf["u3_statistic"],
                             "cohens_d": cohens_d(pf["u3_statistic"], clean_u3)},
            "guttman_errors": {"value": pf["guttman_errors"],
                               "cohens_d": cohens_d(pf["guttman_errors"], clean_ge)},
            "theta_mle": float(model_data[contam_key]["theta_mle"]),
        }
    return results


# ══════════════════════════════════════════════════════════════════════
# ITEM-LEVEL METRICS
# ══════════════════════════════════════════════════════════════════════

def make_seen_labels(seen_set, n_items):
    labels = np.zeros(n_items, dtype=int)
    for idx in seen_set:
        labels[idx] = 1
    return labels

def precision_at_k(scores, labels, k):
    top_k_idx = np.argsort(-scores)[:k]
    return float(labels[top_k_idx].mean())

# ── Item-level lz* contribution ────────────────────────────────────────
def lz_item_scores(response_vector, theta):
    p = irt_prob(theta, a, b, c, d_param)
    x = response_vector.astype(float)
    log_p = np.log(p)
    log_1mp = np.log(1.0 - p)
    l_j = x * log_p + (1.0 - x) * log_1mp
    E_j = p * log_p + (1.0 - p) * log_1mp
    score = l_j - E_j  # positive = overperforming
    return score

# ── Simple gain score ──────────────────────────────────────────────────
def gain_scores(contam_rv, clean_rvs):
    mean_clean = np.mean(clean_rvs, axis=0)
    return contam_rv.astype(float) - mean_clean

# ── Item-level evaluation ─────────────────────────────────────────────
def eval_item_level(scores, labels, n_seen):
    auroc = roc_auc_score(labels, scores)
    p_at_k = precision_at_k(scores, labels, n_seen)
    return {"auroc": float(auroc), "precision_at_k": float(p_at_k), "k": int(n_seen)}

# ── ML cross-model features ───────────────────────────────────────────
def build_features(model_data, clean_keys, contam_key, theta_contam):
    clean_rvs = np.stack([model_data[k]["response_vector"].astype(float) for k in clean_keys])
    contam_rv = model_data[contam_key]["response_vector"].astype(float)
    mean_clean = clean_rvs.mean(axis=0)

    p_contam = irt_prob(theta_contam, a, b, c, d_param)
    residual = contam_rv - p_contam
    gain = contam_rv - mean_clean
    lz_score = lz_item_scores(model_data[contam_key]["response_vector"], theta_contam)

    # Features per item: [contam_response, mean_clean, gain, residual, a, b, c, d, P, lz_contrib]
    X = np.column_stack([
        contam_rv,
        mean_clean,
        gain,
        residual,
        lz_score,
        a, b, c, d_param,
        p_contam,
    ])
    return X

def run_ml_cross_model(train_data, train_clean_keys, train_contam_key, train_seen,
                        test_data, test_clean_keys, test_contam_key, test_seen):
    train_theta = train_data[train_contam_key]["theta_mle"]
    test_theta = test_data[test_contam_key]["theta_mle"]

    X_train = build_features(train_data, train_clean_keys, train_contam_key, train_theta)
    X_test = build_features(test_data, test_clean_keys, test_contam_key, test_theta)

    y_train = make_seen_labels(train_seen, n_items)
    y_test = make_seen_labels(test_seen, n_items)
    n_seen_test = int(y_test.sum())

    results = {}

    # Logistic Regression
    lr = LogisticRegression(max_iter=1000, random_state=42, class_weight="balanced")
    lr.fit(X_train, y_train)
    lr_proba = lr.predict_proba(X_test)[:, 1]
    results["lr"] = eval_item_level(lr_proba, y_test, n_seen_test)

    # Random Forest
    rf = RandomForestClassifier(n_estimators=100, random_state=42, class_weight="balanced", n_jobs=-1)
    rf.fit(X_train, y_train)
    rf_proba = rf.predict_proba(X_test)[:, 1]
    results["rf"] = eval_item_level(rf_proba, y_test, n_seen_test)

    # Feature importances from RF
    feat_names = ["contam_resp", "mean_clean", "gain", "residual", "lz_contrib",
                  "a_disc", "b_diff", "c_guess", "d_feas", "P_theta"]
    importances = dict(zip(feat_names, rf.feature_importances_.tolist()))
    results["rf_feature_importances"] = importances

    return results

# ── Within-model ML (train/test on same model, different contam levels) ──
def run_ml_within_model(model_data, clean_keys, train_contam, train_seen,
                         test_contam, test_seen):
    train_theta = model_data[train_contam]["theta_mle"]
    test_theta = model_data[test_contam]["theta_mle"]

    X_train = build_features(model_data, clean_keys, train_contam, train_theta)
    X_test = build_features(model_data, clean_keys, test_contam, test_theta)

    y_train = make_seen_labels(train_seen, n_items)
    y_test = make_seen_labels(test_seen, n_items)
    n_seen_test = int(y_test.sum())

    results = {}
    for name, clf in [("lr", LogisticRegression(max_iter=1000, random_state=42, class_weight="balanced")),
                      ("rf", RandomForestClassifier(n_estimators=100, random_state=42, class_weight="balanced", n_jobs=-1))]:
        clf.fit(X_train, y_train)
        proba = clf.predict_proba(X_test)[:, 1]
        results[name] = eval_item_level(proba, y_test, n_seen_test)
    return results


# ══════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════

print("Computing model-level metrics...")
qwen_model = compute_model_level("qwen", qwen, qwen_clean_keys, ["contam_15", "contam_50"])
llama_model = compute_model_level("llama", llama, llama_clean_keys, ["contam_15", "contam_50"])

print("Computing item-level metrics...")

item_results = {}

for model_name, model_data, clean_keys, seen_map in [
    ("qwen", qwen, qwen_clean_keys, {"contam_15": qwen_seen_15, "contam_50": qwen_seen_50}),
    ("llama", llama, llama_clean_keys, {"contam_15": llama_seen_15, "contam_50": llama_seen_50}),
]:
    for contam_key, seen_set in seen_map.items():
        key = f"{model_name}_{contam_key}"
        labels = make_seen_labels(seen_set, n_items)
        n_seen = int(labels.sum())
        theta = model_data[contam_key]["theta_mle"]

        # lz* item-level
        lz_scores = lz_item_scores(model_data[contam_key]["response_vector"], theta)
        lz_eval = eval_item_level(lz_scores, labels, n_seen)

        # Gain score
        clean_rvs = np.stack([model_data[k]["response_vector"].astype(float) for k in clean_keys])
        g_scores = gain_scores(model_data[contam_key]["response_vector"], clean_rvs)
        gain_eval = eval_item_level(g_scores, labels, n_seen)

        # IRT residual
        p = irt_prob(theta, a, b, c, d_param)
        residual = model_data[contam_key]["response_vector"].astype(float) - p
        resid_eval = eval_item_level(residual, labels, n_seen)

        item_results[key] = {
            "lz_star_itemwise": lz_eval,
            "gain_score": gain_eval,
            "irt_residual": resid_eval,
            "random": {"auroc": 0.5, "precision_at_k": float(n_seen / n_items), "k": n_seen},
        }
        print(f"  {key}: lz*_auroc={lz_eval['auroc']:.4f}, gain_auroc={gain_eval['auroc']:.4f}, resid_auroc={resid_eval['auroc']:.4f}")

# ── Cross-model ML ─────────────────────────────────────────────────────
print("Running cross-model ML (Qwen→Llama)...")
for contam_pct, q_seen, l_seen in [("15", qwen_seen_15, llama_seen_15),
                                     ("50", qwen_seen_50, llama_seen_50)]:
    contam_key = f"contam_{contam_pct}"
    ml_results = run_ml_cross_model(
        qwen, qwen_clean_keys, contam_key, q_seen,
        llama, llama_clean_keys, contam_key, l_seen
    )
    item_results[f"llama_{contam_key}"]["lr_cross_model_qwen2llama"] = ml_results["lr"]
    item_results[f"llama_{contam_key}"]["rf_cross_model_qwen2llama"] = ml_results["rf"]
    item_results[f"llama_{contam_key}"]["rf_feature_importances"] = ml_results["rf_feature_importances"]
    print(f"  Qwen→Llama {contam_key}: LR_auroc={ml_results['lr']['auroc']:.4f}, RF_auroc={ml_results['rf']['auroc']:.4f}")

print("Running cross-model ML (Llama→Qwen)...")
for contam_pct, q_seen, l_seen in [("15", qwen_seen_15, llama_seen_15),
                                     ("50", qwen_seen_50, llama_seen_50)]:
    contam_key = f"contam_{contam_pct}"
    ml_results = run_ml_cross_model(
        llama, llama_clean_keys, contam_key, l_seen,
        qwen, qwen_clean_keys, contam_key, q_seen
    )
    item_results[f"qwen_{contam_key}"]["lr_cross_model_llama2qwen"] = ml_results["lr"]
    item_results[f"qwen_{contam_key}"]["rf_cross_model_llama2qwen"] = ml_results["rf"]
    item_results[f"qwen_{contam_key}"]["rf_feature_importances"] = ml_results["rf_feature_importances"]
    print(f"  Llama→Qwen {contam_key}: LR_auroc={ml_results['lr']['auroc']:.4f}, RF_auroc={ml_results['rf']['auroc']:.4f}")

# ── Within-model ML (train on contam_15, test on contam_50 and vice versa) ──
print("Running within-model ML...")
for model_name, model_data, clean_keys, seen_15, seen_50 in [
    ("qwen", qwen, qwen_clean_keys, qwen_seen_15, qwen_seen_50),
    ("llama", llama, llama_clean_keys, llama_seen_15, llama_seen_50),
]:
    ml_15to50 = run_ml_within_model(model_data, clean_keys, "contam_15", seen_15, "contam_50", seen_50)
    item_results[f"{model_name}_contam_50"]["lr_within_15to50"] = ml_15to50["lr"]
    item_results[f"{model_name}_contam_50"]["rf_within_15to50"] = ml_15to50["rf"]
    print(f"  {model_name} 15→50: LR={ml_15to50['lr']['auroc']:.4f}, RF={ml_15to50['rf']['auroc']:.4f}")

# ── Assemble final output ──────────────────────────────────────────────
output = {
    "metadata": {
        "n_items": n_items,
        "qwen_seen_15": len(qwen_seen_15),
        "qwen_seen_50": len(qwen_seen_50),
        "llama_seen_15": len(llama_seen_15),
        "llama_seen_50": len(llama_seen_50),
        "seen_overlap_15pct": len(qwen_seen_15 & llama_seen_15),
        "seen_overlap_50pct": len(qwen_seen_50 & llama_seen_50),
    },
    "model_level": {
        "qwen": qwen_model,
        "llama": llama_model,
    },
    "item_level": item_results,
    "method_descriptions": {
        "lz_star": "IRT-based person-fit (unsupervised, uses IRT params + response vector)",
        "acc_zscore": "Accuracy z-score vs clean seeds (unsupervised, no IRT)",
        "ht_statistic": "HT person-fit: Guttman errors / (n_correct * n_incorrect) (unsupervised, uses item difficulty ordering)",
        "u3_statistic": "U3 person-fit: Guttman errors / total_pairs (unsupervised, uses item difficulty ordering)",
        "guttman_errors": "Raw Guttman error count (unsupervised, uses item difficulty ordering)",
        "lz_star_itemwise": "Per-item lz* log-likelihood contribution (unsupervised item-level)",
        "gain_score": "Item response gain: contam - mean(clean) (unsupervised item-level, no IRT)",
        "irt_residual": "IRT residual: observed - P(theta) (unsupervised item-level)",
        "lr_cross_model": "Logistic Regression trained on other model (supervised oracle, cross-model)",
        "rf_cross_model": "Random Forest trained on other model (supervised oracle, cross-model)",
        "random": "Random baseline (AUROC=0.5)",
    },
}

out_path = f"{OUT_DIR}/comparison_results.json"
with open(out_path, "w") as f:
    json.dump(output, f, indent=2)
print(f"\nResults saved to {out_path}")

# ── Print summary table ───────────────────────────────────────────────
print("\n" + "="*80)
print("MODEL-LEVEL SUMMARY")
print("="*80)
for model_name, model_res in [("Qwen", qwen_model), ("Llama", llama_model)]:
    for cond in ["contam_15", "contam_50"]:
        r = model_res[cond]
        print(f"\n{model_name} {cond}:")
        print(f"  Accuracy z-score:  {r['acc_zscore']['value']:+.2f}")
        print(f"  lz* (free θ):      {r['lz_star']['value']:.4f}  (Cohen's d = {r['lz_star']['cohens_d']:.2f})")
        print(f"  HT statistic:      {r['ht_statistic']['value']:.6f}  (Cohen's d = {r['ht_statistic']['cohens_d']:.2f})")
        print(f"  U3 statistic:      {r['u3_statistic']['value']:.6f}  (Cohen's d = {r['u3_statistic']['cohens_d']:.2f})")
        print(f"  Guttman errors:    {r['guttman_errors']['value']}  (Cohen's d = {r['guttman_errors']['cohens_d']:.2f})")

print("\n" + "="*80)
print("ITEM-LEVEL SUMMARY (AUROC / P@K)")
print("="*80)
for key in sorted(item_results.keys()):
    ir = item_results[key]
    print(f"\n{key}:")
    for method in ["lz_star_itemwise", "gain_score", "irt_residual", "random"]:
        if method in ir:
            print(f"  {method:30s}  AUROC={ir[method]['auroc']:.4f}  P@K={ir[method]['precision_at_k']:.4f}")
    for method in ir:
        if "cross_model" in method or "within" in method:
            print(f"  {method:30s}  AUROC={ir[method]['auroc']:.4f}  P@K={ir[method]['precision_at_k']:.4f}")
