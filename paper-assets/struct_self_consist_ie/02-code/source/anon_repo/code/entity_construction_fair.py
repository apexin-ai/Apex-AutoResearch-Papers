"""Fair evaluation of entity-level majority vote construction for NER and RE.

Fixes methodological bug: original find_best_threshold() swept theta on test set.
This script uses:
  1. 5-fold CV on test set for theta optimization
  2. Fixed theta=0.5 (majority vote, no tuning)
  3. Fixed theta=2/N (confirmation threshold, no tuning)
  + paired bootstrap significance tests for all comparisons
  + adaptive LP+construction combination
"""

import json
import math
import os
import sys
import numpy as np
from collections import defaultdict
from sklearn.model_selection import KFold

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

DATASETS = {
    "scierc": "/root/autodl-tmp/struct_self_consist_ie/output/exp_001_seed42_v2/samples.jsonl",
    "conll": "/root/autodl-tmp/struct_self_consist_ie/output/exp_002_conll_n16/samples.jsonl",
    "fewnerd": "/root/autodl-tmp/struct_self_consist_ie/output/exp_027_fewnerd_n16/samples.jsonl",
}

OUTPUT_DIR = "/root/autodl-tmp/struct_self_consist_ie/output/entity_construction_fair"
THRESHOLDS = [0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.7, 0.8, 0.9]

# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------

def compute_prf(pred_set, gold_set):
    if not gold_set and not pred_set:
        return 1.0, 1.0, 1.0
    if not pred_set:
        return 0.0, 0.0, 0.0
    if not gold_set:
        return 0.0, 0.0, 0.0
    tp = len(pred_set & gold_set)
    if tp == 0:
        return 0.0, 0.0, 0.0
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    f = 2 * p * r / (p + r)
    return p, r, f


def entity_set(entities):
    return {(e["start"], e["end"], e["type"]) for e in entities}


def relation_set(relations):
    return {(r["head_start"], r["head_end"], r["tail_start"], r["tail_end"], r["type"])
            for r in relations}


# ---------------------------------------------------------------------------
# Construction
# ---------------------------------------------------------------------------

def entity_majority_vote(samples, threshold, weights=None):
    entity_counts = defaultdict(float)
    N = len(samples)
    for i, sample in enumerate(samples):
        w = weights[i] if weights is not None else 1.0
        for e in sample.get("entities", []):
            key = (e["start"], e["end"], e["type"])
            entity_counts[key] += w
    total_weight = sum(weights) if weights is not None else N
    constructed = set()
    for key, count in entity_counts.items():
        if count / total_weight >= threshold:
            constructed.add(key)
    return constructed


def relation_majority_vote(samples, threshold, weights=None):
    rel_counts = defaultdict(float)
    N = len(samples)
    for i, sample in enumerate(samples):
        w = weights[i] if weights is not None else 1.0
        for r in sample.get("relations", []):
            key = (r["head_start"], r["head_end"], r["tail_start"], r["tail_end"], r["type"])
            rel_counts[key] += w
    total_weight = sum(weights) if weights is not None else N
    constructed = set()
    for key, count in rel_counts.items():
        if count / total_weight >= threshold:
            constructed.add(key)
    return constructed


# ---------------------------------------------------------------------------
# Data loading & weight helpers
# ---------------------------------------------------------------------------

def load_data(path, gold_filter=True):
    instances = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            obj = json.loads(line)
            if gold_filter and not obj["gold"].get("entities", []):
                continue
            instances.append(obj)
    return instances


def get_lp_weights(inst):
    samples = inst["samples"]
    logprobs = inst.get("logprobs", None)
    lps = []
    for i, s in enumerate(samples):
        lp = s.get("mean_logprob", None)
        if lp is None and logprobs is not None and i < len(logprobs):
            lp = logprobs[i]
        if lp is None or not math.isfinite(lp):
            lp = -100.0
        lps.append(lp)
    max_lp = max(lps)
    ws = [math.exp(lp - max_lp) for lp in lps]
    total = sum(ws)
    return [w / total for w in ws]


def get_sj_weights(inst):
    samples = inst["samples"]
    lps = []
    for s in samples:
        lp = s.get("cumulative_logprob", None)
        if lp is None or not math.isfinite(lp):
            lp = -1e6
        lps.append(lp)
    max_lp = max(lps)
    ws = [math.exp(lp - max_lp) for lp in lps]
    total = sum(ws)
    return [w / total for w in ws]


def best_of_n_by_key(inst, key="mean_logprob"):
    samples = inst["samples"]
    logprobs = inst.get("logprobs", None)
    best_idx, best_val = 0, -float("inf")
    for i, s in enumerate(samples):
        val = s.get(key, None)
        if val is None and key == "mean_logprob" and logprobs is not None and i < len(logprobs):
            val = logprobs[i]
        if val is not None and math.isfinite(val) and val > best_val:
            best_val = val
            best_idx = i
    return best_idx


def best_of_n_sj(inst):
    best_idx, best_val = 0, -float("inf")
    for i, s in enumerate(inst["samples"]):
        val = s.get("cumulative_logprob", None)
        if val is not None and math.isfinite(val) and val > best_val:
            best_val = val
            best_idx = i
    return best_idx


# ---------------------------------------------------------------------------
# Per-instance F1 computation
# ---------------------------------------------------------------------------

def compute_per_instance_f1s(data, method_fn):
    f1s = []
    for inst in data:
        gold = entity_set(inst["gold"]["entities"])
        pred = method_fn(inst)
        _, _, f = compute_prf(pred, gold)
        f1s.append(f)
    return np.array(f1s)


def compute_per_instance_re_f1s(data, method_fn):
    f1s = []
    for inst in data:
        gold = relation_set(inst["gold"].get("relations", []))
        pred = method_fn(inst)
        _, _, f = compute_prf(pred, gold)
        f1s.append(f)
    return np.array(f1s)


# ---------------------------------------------------------------------------
# Bootstrap significance test
# ---------------------------------------------------------------------------

def bootstrap_test(f1_method, f1_baseline, B=10000, seed=42):
    rng = np.random.RandomState(seed)
    n = len(f1_method)
    diffs = f1_method - f1_baseline
    observed_diff = diffs.mean()

    boot_diffs = []
    for _ in range(B):
        idx = rng.randint(0, n, n)
        boot_diffs.append(diffs[idx].mean())

    boot_diffs = np.array(boot_diffs)
    ci_low = float(np.percentile(boot_diffs, 2.5))
    ci_high = float(np.percentile(boot_diffs, 97.5))
    p_value = float((boot_diffs <= 0).mean())

    return float(observed_diff), (ci_low, ci_high), p_value


# ---------------------------------------------------------------------------
# Method functions
# ---------------------------------------------------------------------------

def make_greedy_fn():
    def fn(inst):
        greedy = inst.get("greedy", inst["samples"][0])
        return entity_set(greedy.get("entities", []))
    return fn

def make_lp_selection_fn():
    def fn(inst):
        idx = best_of_n_by_key(inst, "mean_logprob")
        return entity_set(inst["samples"][idx].get("entities", []))
    return fn

def make_sj_selection_fn():
    def fn(inst):
        idx = best_of_n_sj(inst)
        return entity_set(inst["samples"][idx].get("entities", []))
    return fn

def make_oracle_fn():
    def fn(inst):
        gold = entity_set(inst["gold"]["entities"])
        best_set, best_f = set(), 0.0
        for s in inst["samples"]:
            pred = entity_set(s.get("entities", []))
            _, _, f = compute_prf(pred, gold)
            if f > best_f:
                best_f = f
                best_set = pred
        return best_set
    return fn

def make_random_fn():
    def fn(inst):
        idx = np.random.randint(0, len(inst["samples"]))
        return entity_set(inst["samples"][idx].get("entities", []))
    return fn

def make_construction_fn(threshold, variant="uniform"):
    def fn(inst):
        if variant == "uniform":
            return entity_majority_vote(inst["samples"], threshold)
        else:
            ws = get_lp_weights(inst)
            return entity_majority_vote(inst["samples"], threshold, weights=ws)
    return fn

def make_greedy_re_fn():
    def fn(inst):
        greedy = inst.get("greedy", inst["samples"][0])
        return relation_set(greedy.get("relations", []))
    return fn

def make_lp_selection_re_fn():
    def fn(inst):
        idx = best_of_n_by_key(inst, "mean_logprob")
        return relation_set(inst["samples"][idx].get("relations", []))
    return fn

def make_oracle_re_fn():
    def fn(inst):
        gold = relation_set(inst["gold"].get("relations", []))
        best_set, best_f = set(), 0.0
        for s in inst["samples"]:
            pred = relation_set(s.get("relations", []))
            _, _, f = compute_prf(pred, gold)
            if f > best_f:
                best_f = f
                best_set = pred
        return best_set
    return fn

def make_construction_re_fn(threshold, variant="uniform"):
    def fn(inst):
        if variant == "uniform":
            return relation_majority_vote(inst["samples"], threshold)
        else:
            ws = get_lp_weights(inst)
            return relation_majority_vote(inst["samples"], threshold, weights=ws)
    return fn


# ---------------------------------------------------------------------------
# 5-fold CV for threshold selection
# ---------------------------------------------------------------------------

def cv_threshold_selection(data, variant="uniform", n_splits=5, seed=42, task="ner"):
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=seed)
    indices = np.arange(len(data))

    fold_f1s = []
    fold_thetas = []
    per_instance_f1s = np.zeros(len(data))

    for fold_idx, (train_idx, test_idx) in enumerate(kf.split(indices)):
        train_data = [data[i] for i in train_idx]
        test_data = [data[i] for i in test_idx]

        best_train_f1, best_t = 0.0, 0.5
        for t in THRESHOLDS:
            if task == "ner":
                fn = make_construction_fn(t, variant)
                f1s = compute_per_instance_f1s(train_data, fn)
            else:
                fn = make_construction_re_fn(t, variant)
                f1s = compute_per_instance_re_f1s(train_data, fn)
            mean_f1 = f1s.mean()
            if mean_f1 > best_train_f1:
                best_train_f1 = mean_f1
                best_t = t

        if task == "ner":
            fn = make_construction_fn(best_t, variant)
            test_f1s = compute_per_instance_f1s(test_data, fn)
        else:
            fn = make_construction_re_fn(best_t, variant)
            test_f1s = compute_per_instance_re_f1s(test_data, fn)

        fold_f1s.append(float(test_f1s.mean()))
        fold_thetas.append(best_t)

        for i, idx in enumerate(test_idx):
            per_instance_f1s[idx] = test_f1s[i]

    return {
        "mean_f1": float(np.mean(fold_f1s)),
        "std_f1": float(np.std(fold_f1s)),
        "fold_f1s": fold_f1s,
        "fold_thetas": fold_thetas,
        "per_instance_f1s": per_instance_f1s,
    }


# ---------------------------------------------------------------------------
# Adaptive combination
# ---------------------------------------------------------------------------

def compute_lp_alignment(inst):
    gold = entity_set(inst["gold"]["entities"])
    samples = inst["samples"]
    logprobs = inst.get("logprobs", None)

    lps = []
    f1s = []
    for i, s in enumerate(samples):
        lp = s.get("mean_logprob", None)
        if lp is None and logprobs is not None and i < len(logprobs):
            lp = logprobs[i]
        if lp is None or not math.isfinite(lp):
            lp = -100.0
        lps.append(lp)
        pred = entity_set(s.get("entities", []))
        _, _, f = compute_prf(pred, gold)
        f1s.append(f)

    if len(set(lps)) <= 1 or len(set(f1s)) <= 1:
        return 0.0

    from scipy.stats import spearmanr
    rho, _ = spearmanr(lps, f1s)
    if not math.isfinite(rho):
        return 0.0
    return rho


def adaptive_combination_cv(data, n_splits=5, seed=42, variant="uniform"):
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=seed)
    indices = np.arange(len(data))

    alignments = np.array([compute_lp_alignment(inst) for inst in data])
    lp_f1s = compute_per_instance_f1s(data, make_lp_selection_fn())

    gating_thresholds = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]

    fold_f1s = []
    fold_params = []
    per_instance_f1s = np.zeros(len(data))

    for fold_idx, (train_idx, test_idx) in enumerate(kf.split(indices)):
        best_train_f1 = 0.0
        best_gate_t = 0.0
        best_constr_t = 0.5

        for gate_t in gating_thresholds:
            for constr_t in THRESHOLDS:
                train_f1_sum = 0.0
                for i in train_idx:
                    if alignments[i] > gate_t:
                        train_f1_sum += lp_f1s[i]
                    else:
                        fn = make_construction_fn(constr_t, variant)
                        gold = entity_set(data[i]["gold"]["entities"])
                        pred = fn(data[i])
                        _, _, f = compute_prf(pred, gold)
                        train_f1_sum += f
                mean_f1 = train_f1_sum / len(train_idx)
                if mean_f1 > best_train_f1:
                    best_train_f1 = mean_f1
                    best_gate_t = gate_t
                    best_constr_t = constr_t

        test_f1_list = []
        for i in test_idx:
            if alignments[i] > best_gate_t:
                f = lp_f1s[i]
            else:
                fn = make_construction_fn(best_constr_t, variant)
                gold = entity_set(data[i]["gold"]["entities"])
                pred = fn(data[i])
                _, _, f = compute_prf(pred, gold)
            per_instance_f1s[i] = f
            test_f1_list.append(f)

        fold_f1s.append(float(np.mean(test_f1_list)))
        fold_params.append({"gate_threshold": best_gate_t, "construction_theta": best_constr_t})

    return {
        "mean_f1": float(np.mean(fold_f1s)),
        "std_f1": float(np.std(fold_f1s)),
        "fold_f1s": fold_f1s,
        "fold_params": fold_params,
        "per_instance_f1s": per_instance_f1s,
    }


def dataset_level_gating_recommendation(data, name):
    alignments = [compute_lp_alignment(inst) for inst in data]
    mean_align = float(np.mean(alignments))
    median_align = float(np.median(alignments))
    frac_positive = float(np.mean(np.array(alignments) > 0))
    return {
        "dataset": name,
        "mean_alignment": mean_align,
        "median_alignment": median_align,
        "frac_positive": frac_positive,
        "recommendation": "LP selection" if mean_align > 0.2 else "construction",
    }


# ---------------------------------------------------------------------------
# Main evaluation
# ---------------------------------------------------------------------------

def evaluate_dataset(name, path):
    print(f"\n{'='*70}")
    print(f"Dataset: {name}")
    print(f"{'='*70}")

    data = load_data(path, gold_filter=True)
    n_instances = len(data)
    n_samples = len(data[0]["samples"])
    has_relations = name == "scierc"
    print(f"Instances: {n_instances}, Samples/instance: {n_samples}, Has RE: {has_relations}")

    results = {}

    # --- Baselines ---
    greedy_f1s = compute_per_instance_f1s(data, make_greedy_fn())
    lp_f1s = compute_per_instance_f1s(data, make_lp_selection_fn())
    sj_f1s = compute_per_instance_f1s(data, make_sj_selection_fn())
    oracle_f1s = compute_per_instance_f1s(data, make_oracle_fn())

    np.random.seed(42)
    random_f1s_runs = []
    for _ in range(50):
        random_f1s_runs.append(compute_per_instance_f1s(data, make_random_fn()))
    random_f1s = np.mean(random_f1s_runs, axis=0)

    results["greedy"] = {"F1": float(greedy_f1s.mean()), "std": float(greedy_f1s.std())}
    results["lp_selection"] = {"F1": float(lp_f1s.mean()), "std": float(lp_f1s.std())}
    results["sj_selection"] = {"F1": float(sj_f1s.mean()), "std": float(sj_f1s.std())}
    results["oracle"] = {"F1": float(oracle_f1s.mean()), "std": float(oracle_f1s.std())}
    results["random"] = {"F1": float(random_f1s.mean()), "std": float(random_f1s.std())}

    print(f"\n  Greedy:       {greedy_f1s.mean():.4f}")
    print(f"  LP Selection: {lp_f1s.mean():.4f}")
    print(f"  SJ Selection: {sj_f1s.mean():.4f}")
    print(f"  Random:       {random_f1s.mean():.4f}")
    print(f"  Oracle:       {oracle_f1s.mean():.4f}")

    # --- Fixed theta methods ---
    theta_majority = 0.5
    theta_confirm = 2.0 / n_samples

    for variant in ["uniform", "lp_weighted"]:
        fn_maj = make_construction_fn(theta_majority, variant)
        maj_f1s = compute_per_instance_f1s(data, fn_maj)
        key_maj = f"construction_{variant}_majority"
        results[key_maj] = {
            "F1": float(maj_f1s.mean()),
            "std": float(maj_f1s.std()),
            "theta": theta_majority,
        }

        fn_conf = make_construction_fn(theta_confirm, variant)
        conf_f1s = compute_per_instance_f1s(data, fn_conf)
        key_conf = f"construction_{variant}_confirm"
        results[key_conf] = {
            "F1": float(conf_f1s.mean()),
            "std": float(conf_f1s.std()),
            "theta": theta_confirm,
        }

        print(f"\n  Running 5-fold CV for {variant}...")
        cv_result = cv_threshold_selection(data, variant=variant, n_splits=5, seed=42, task="ner")
        key_cv = f"construction_{variant}_cv"
        results[key_cv] = {
            "F1": cv_result["mean_f1"],
            "std": cv_result["std_f1"],
            "fold_f1s": cv_result["fold_f1s"],
            "fold_thetas": cv_result["fold_thetas"],
        }

        print(f"    {variant} majority(t=0.5):  F1={maj_f1s.mean():.4f}")
        print(f"    {variant} confirm(t={theta_confirm:.3f}): F1={conf_f1s.mean():.4f}")
        print(f"    {variant} CV:               F1={cv_result['mean_f1']:.4f} +/- {cv_result['std_f1']:.4f}")
        print(f"      fold thetas: {cv_result['fold_thetas']}")
        print(f"      fold F1s:    {[f'{f:.4f}' for f in cv_result['fold_f1s']]}")

        for method_name, method_f1s in [
            (key_maj, maj_f1s),
            (key_conf, conf_f1s),
            (key_cv, cv_result["per_instance_f1s"]),
        ]:
            diff, ci, pval = bootstrap_test(method_f1s, greedy_f1s)
            results[f"bootstrap_{method_name}_vs_greedy"] = {
                "mean_diff": diff,
                "ci_95": list(ci),
                "p_value": pval,
                "significant": pval < 0.05,
            }

        diff, ci, pval = bootstrap_test(lp_f1s, greedy_f1s)
        results["bootstrap_lp_selection_vs_greedy"] = {
            "mean_diff": diff, "ci_95": list(ci), "p_value": pval, "significant": pval < 0.05,
        }

    # --- Adaptive combination ---
    print(f"\n  Running adaptive combination CV...")
    adaptive_result = adaptive_combination_cv(data, n_splits=5, seed=42, variant="uniform")
    results["adaptive_uniform"] = {
        "F1": adaptive_result["mean_f1"],
        "std": adaptive_result["std_f1"],
        "fold_f1s": adaptive_result["fold_f1s"],
        "fold_params": [
            {"gate_threshold": p["gate_threshold"], "construction_theta": p["construction_theta"]}
            for p in adaptive_result["fold_params"]
        ],
    }
    diff, ci, pval = bootstrap_test(adaptive_result["per_instance_f1s"], greedy_f1s)
    results["bootstrap_adaptive_uniform_vs_greedy"] = {
        "mean_diff": diff, "ci_95": list(ci), "p_value": pval, "significant": pval < 0.05,
    }
    print(f"    Adaptive uniform: F1={adaptive_result['mean_f1']:.4f} +/- {adaptive_result['std_f1']:.4f}")

    gating = dataset_level_gating_recommendation(data, name)
    results["lp_alignment_gating"] = gating
    print(f"    LP alignment: mean={gating['mean_alignment']:.3f}, recommendation={gating['recommendation']}")

    # --- Full threshold sweep (reference only) ---
    for variant in ["uniform", "lp_weighted"]:
        print(f"\n  Full theta sweep ({variant}):")
        for t in THRESHOLDS:
            fn = make_construction_fn(t, variant)
            f1s = compute_per_instance_f1s(data, fn)
            key = f"sweep_{variant}_t{t}"
            results[key] = {"F1": float(f1s.mean()), "theta": t}
            delta = (f1s.mean() - greedy_f1s.mean()) * 100
            print(f"    t={t:.2f}  F1={f1s.mean():.4f}  d={delta:+.2f}pp")

    # --- RE (SciERC only) ---
    if has_relations:
        print(f"\n  --- Relation Extraction ---")
        re_greedy_f1s = compute_per_instance_re_f1s(data, make_greedy_re_fn())
        re_lp_f1s = compute_per_instance_re_f1s(data, make_lp_selection_re_fn())
        re_oracle_f1s = compute_per_instance_re_f1s(data, make_oracle_re_fn())

        results["re_greedy"] = {"F1": float(re_greedy_f1s.mean())}
        results["re_lp_selection"] = {"F1": float(re_lp_f1s.mean())}
        results["re_oracle"] = {"F1": float(re_oracle_f1s.mean())}

        print(f"  RE Greedy:       {re_greedy_f1s.mean():.4f}")
        print(f"  RE LP Selection: {re_lp_f1s.mean():.4f}")
        print(f"  RE Oracle:       {re_oracle_f1s.mean():.4f}")

        for variant in ["uniform", "lp_weighted"]:
            fn_maj = make_construction_re_fn(theta_majority, variant)
            re_maj_f1s = compute_per_instance_re_f1s(data, fn_maj)
            results[f"re_{variant}_majority"] = {"F1": float(re_maj_f1s.mean()), "theta": theta_majority}

            fn_conf = make_construction_re_fn(theta_confirm, variant)
            re_conf_f1s = compute_per_instance_re_f1s(data, fn_conf)
            results[f"re_{variant}_confirm"] = {"F1": float(re_conf_f1s.mean()), "theta": theta_confirm}

            re_cv = cv_threshold_selection(data, variant=variant, n_splits=5, seed=42, task="re")
            results[f"re_{variant}_cv"] = {
                "F1": re_cv["mean_f1"],
                "std": re_cv["std_f1"],
                "fold_thetas": re_cv["fold_thetas"],
            }

            print(f"    RE {variant} majority(t=0.5): {re_maj_f1s.mean():.4f}")
            print(f"    RE {variant} confirm(t={theta_confirm:.3f}): {re_conf_f1s.mean():.4f}")
            print(f"    RE {variant} CV: {re_cv['mean_f1']:.4f} +/- {re_cv['std_f1']:.4f} (thetas={re_cv['fold_thetas']})")

            for label, f1arr in [("majority", re_maj_f1s), ("confirm", re_conf_f1s), ("cv", re_cv["per_instance_f1s"])]:
                diff, ci, pval = bootstrap_test(f1arr, re_greedy_f1s)
                results[f"re_bootstrap_{variant}_{label}_vs_greedy"] = {
                    "mean_diff": diff, "ci_95": list(ci), "p_value": pval, "significant": pval < 0.05,
                }

    return results, data, greedy_f1s


# ---------------------------------------------------------------------------
# LaTeX table
# ---------------------------------------------------------------------------

def print_latex_table(all_results):
    print("\n" + "=" * 90)
    print("LaTeX TABLE: Fair Entity Construction Evaluation")
    print("=" * 90)

    datasets = ["scierc", "conll", "fewnerd"]
    dataset_labels = {"scierc": "SciERC", "conll": "CoNLL", "fewnerd": "FewNERD"}

    print(r"\begin{table}[t]")
    print(r"\centering")
    print(r"\small")
    print(r"\begin{tabular}{l" + "c" * len(datasets) + "}")
    print(r"\toprule")
    header = "Method & " + " & ".join([dataset_labels[d] for d in datasets]) + r" \\"
    print(header)
    print(r"\midrule")

    methods = [
        ("Greedy", "greedy"),
        ("Random", "random"),
        ("LP Selection", "lp_selection"),
        ("SJ Selection", "sj_selection"),
        ("Oracle", "oracle"),
    ]

    construction_methods = [
        ("Construction (majority, $\\theta$=0.5)", "construction_uniform_majority"),
        ("Construction (confirm, $\\theta$=2/N)", "construction_uniform_confirm"),
        ("Construction (5-fold CV)", "construction_uniform_cv"),
        ("Construction+LP (majority)", "construction_lp_weighted_majority"),
        ("Construction+LP (confirm)", "construction_lp_weighted_confirm"),
        ("Construction+LP (5-fold CV)", "construction_lp_weighted_cv"),
        ("Adaptive (LP+Construction)", "adaptive_uniform"),
    ]

    best_f1 = {}
    for d in datasets:
        if d not in all_results:
            continue
        res = all_results[d]
        best = 0
        for _, key in methods[:-1]:
            if key in res:
                best = max(best, res[key]["F1"])
        for _, key in construction_methods:
            if key in res:
                best = max(best, res[key]["F1"])
        best_f1[d] = best

    def fmt(d, key, all_res):
        if d not in all_res or key not in all_res[d]:
            return "--"
        f1 = all_res[d][key]["F1"]
        boot_key = f"bootstrap_{key}_vs_greedy"
        sig = ""
        if boot_key in all_res[d]:
            if all_res[d][boot_key]["significant"] and all_res[d][boot_key]["mean_diff"] > 0:
                sig = "$^{*}$"
        s = f"{f1*100:.1f}{sig}"
        if d in best_f1 and abs(f1 - best_f1[d]) < 1e-4:
            s = r"\textbf{" + s + "}"
        return s

    for label, key in methods:
        cells = [fmt(d, key, all_results) for d in datasets]
        print(f"{label} & " + " & ".join(cells) + r" \\")

    print(r"\midrule")

    for label, key in construction_methods:
        cells = [fmt(d, key, all_results) for d in datasets]
        print(f"{label} & " + " & ".join(cells) + r" \\")

    print(r"\bottomrule")
    print(r"\end{tabular}")
    print(r"\caption{Fair evaluation of entity construction methods (Entity F1). $^{*}$: significantly better than Greedy ($p<0.05$, paired bootstrap).}")
    print(r"\end{table}")

    # Significance summary
    print("\n" + "=" * 90)
    print("SIGNIFICANCE TESTS vs Greedy")
    print("=" * 90)
    print(f"{'Dataset':<10} {'Method':<40} {'d F1':>8} {'95% CI':>20} {'p-value':>10} {'Sig?':>5}")
    print("-" * 93)
    for d in datasets:
        if d not in all_results:
            continue
        res = all_results[d]
        for key in sorted(res.keys()):
            if key.startswith("bootstrap_") and key.endswith("_vs_greedy") and not key.startswith("re_"):
                method_name = key.replace("bootstrap_", "").replace("_vs_greedy", "")
                b = res[key]
                ci_str = f"[{b['ci_95'][0]*100:+.2f}, {b['ci_95'][1]*100:+.2f}]"
                sig_str = "YES" if b["significant"] else "no"
                print(f"{d:<10} {method_name:<40} {b['mean_diff']*100:+.2f}pp {ci_str:>20} {b['p_value']:>10.4f} {sig_str:>5}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    all_results = {}

    for name, path in DATASETS.items():
        if not os.path.exists(path):
            print(f"SKIP {name}: {path} not found")
            continue
        results, data, greedy_f1s = evaluate_dataset(name, path)
        all_results[name] = results

    with open(os.path.join(OUTPUT_DIR, "fair_results.json"), "w") as f:
        json.dump(all_results, f, indent=2, default=str)

    bootstrap_tests = {}
    for name, res in all_results.items():
        bootstrap_tests[name] = {k: v for k, v in res.items() if k.startswith("bootstrap_") or k.startswith("re_bootstrap_")}
    with open(os.path.join(OUTPUT_DIR, "bootstrap_tests.json"), "w") as f:
        json.dump(bootstrap_tests, f, indent=2)

    adaptive_results = {}
    for name, res in all_results.items():
        adaptive_results[name] = {k: v for k, v in res.items() if "adaptive" in k or "gating" in k}
    with open(os.path.join(OUTPUT_DIR, "adaptive_combination.json"), "w") as f:
        json.dump(adaptive_results, f, indent=2, default=str)

    print_latex_table(all_results)

    print("\n" + "=" * 70)
    print("VALIDATION CHECKS")
    print("=" * 70)
    for name, res in all_results.items():
        print(f"\n{name}:")
        for variant in ["uniform", "lp_weighted"]:
            cv_key = f"construction_{variant}_cv"
            maj_key = f"construction_{variant}_majority"
            if cv_key in res:
                cv_f1 = res[cv_key]["F1"]
                best_sweep = max(
                    (res[k]["F1"] for k in res if k.startswith(f"sweep_{variant}_t")),
                    default=0
                )
                check = "YES (expected)" if cv_f1 <= best_sweep + 1e-6 else "NO (unexpected!)"
                print(f"  {variant}: CV F1={cv_f1:.4f} <= test-optimized F1={best_sweep:.4f}? {check}")
                if maj_key in res:
                    print(f"  {variant}: majority F1={res[maj_key]['F1']:.4f} (no tuning)")

    print("\nResults saved to:", OUTPUT_DIR)


if __name__ == "__main__":
    main()
