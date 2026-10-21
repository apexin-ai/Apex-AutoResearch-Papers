#!/usr/bin/env python3
"""Round 8 supplementary analyses: N1 (bootstrap cluster), N2 (auth scope ranking), W5 (clause variance)."""

import csv
import json
import os
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy.cluster.hierarchy import linkage, fcluster
from scipy.spatial.distance import pdist

# ─── Config ───
BASE = Path("/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts")
SUMMARY_CSV = BASE / "full_study" / "analysis" / "per_clause_summary.csv"
OUTPUT_DIR = BASE / "round8_supplementary"
OUTPUT_JSON = OUTPUT_DIR / "round8_supplementary_analyses.json"
SEED = 42
B_CLUSTER = 10000  # bootstrap iterations for N1
B_RANKING = 10000  # bootstrap iterations for N2

MODELS = ["gpt-5.4", "gpt-4.1", "claude-sonnet-4-6", "qwen3-235b", "deepseek-v3"]
TYPES_ORDERED = ["incompleteness", "lexical", "authorization_scope", "scopal", "conditional_precedence", "coreferential"]

# GPT-5.4 judges these models (cross-judge design)
GPT54_JUDGED_MODELS = ["claude-sonnet-4-6", "gpt-4.1", "qwen3-235b"]


def load_data():
    """Load per-clause summary CSV into structured dicts."""
    with open(SUMMARY_CSV) as f:
        rows = list(csv.DictReader(f))

    # Build: type -> clause_id -> model -> violation_rate (ambiguous only)
    ambig_data = defaultdict(lambda: defaultdict(dict))
    # Also raw: type -> model -> list of violation_rates
    type_model_viol = defaultdict(lambda: defaultdict(list))

    for r in rows:
        if r["condition"] != "ambiguous":
            continue
        t = r["ambiguity_type"]
        c = r["clause_id"]
        m = r["model"]
        v = float(r["violation_rate"])
        ambig_data[t][c][m] = v
        type_model_viol[t][m].append(v)

    return ambig_data, type_model_viol


def compute_clause_level_rates(ambig_data):
    """For each type, compute per-clause mean violation rate (averaged across models)."""
    # type -> list of (clause_id, mean_rate)
    clause_rates = {}
    for t in TYPES_ORDERED:
        rates = []
        for c_id, model_dict in sorted(ambig_data[t].items()):
            vals = [model_dict[m] for m in MODELS if m in model_dict]
            mean_rate = np.mean(vals) if vals else 0.0
            rates.append((c_id, mean_rate))
        clause_rates[t] = rates
    return clause_rates


# ════════════════════════════════════════════════════════════════
# Analysis 1: Bootstrap Cluster Analysis (N1)
# ════════════════════════════════════════════════════════════════

def analysis_n1(ambig_data, clause_rates):
    """Hierarchical clustering on type-level violation rates with bootstrap stability."""
    rng = np.random.RandomState(SEED)

    # Observed type-level rates
    obs_rates = {}
    for t in TYPES_ORDERED:
        rates = [r for _, r in clause_rates[t]]
        obs_rates[t] = np.mean(rates)

    # Ward's clustering on 6 type means
    rate_vector = np.array([obs_rates[t] for t in TYPES_ORDERED]).reshape(-1, 1)
    Z = linkage(rate_vector, method="ward")

    clusters_k2 = fcluster(Z, t=2, criterion="maxclust")
    clusters_k3 = fcluster(Z, t=3, criterion="maxclust")

    k2_membership = {t: int(clusters_k2[i]) for i, t in enumerate(TYPES_ORDERED)}
    k3_membership = {t: int(clusters_k3[i]) for i, t in enumerate(TYPES_ORDERED)}

    # Identify which cluster incompleteness belongs to at k=2
    inc_cluster_obs = k2_membership["incompleteness"]
    # Check if incompleteness is a singleton at k=2
    inc_singleton_obs = sum(1 for v in k2_membership.values() if v == inc_cluster_obs) == 1

    # Bootstrap: resample clauses within each type, recompute type rates, re-cluster
    inc_singleton_count = 0
    same_k2_count = 0

    # Pre-extract clause rates as arrays for fast resampling
    clause_rate_arrays = {}
    for t in TYPES_ORDERED:
        clause_rate_arrays[t] = np.array([r for _, r in clause_rates[t]])

    for b in range(B_CLUSTER):
        boot_rates = []
        for t in TYPES_ORDERED:
            arr = clause_rate_arrays[t]
            n = len(arr)
            idx = rng.randint(0, n, size=n)
            boot_rates.append(np.mean(arr[idx]))

        boot_vec = np.array(boot_rates).reshape(-1, 1)
        try:
            Z_boot = linkage(boot_vec, method="ward")
            boot_k2 = fcluster(Z_boot, t=2, criterion="maxclust")
        except Exception:
            continue

        # Check if incompleteness is singleton at k=2
        inc_idx = 0  # incompleteness is first in TYPES_ORDERED
        inc_clust = boot_k2[inc_idx]
        if sum(1 for c in boot_k2 if c == inc_clust) == 1:
            inc_singleton_count += 1

        # Check if same 2-cluster structure holds
        # Map observed cluster labels to bootstrap labels
        obs_groups = defaultdict(set)
        for i, t in enumerate(TYPES_ORDERED):
            obs_groups[clusters_k2[i]].add(i)
        boot_groups = defaultdict(set)
        for i, t in enumerate(TYPES_ORDERED):
            boot_groups[boot_k2[i]].add(i)
        if set(frozenset(v) for v in obs_groups.values()) == set(frozenset(v) for v in boot_groups.values()):
            same_k2_count += 1

    # Approximately Unbiased (AU) p-values via multiscale bootstrap (simplified)
    # We compute AU p-values using different resample sizes
    au_results = {}
    scales = [0.5, 0.7, 1.0, 1.4, 2.0]
    for scale in scales:
        n_singleton = 0
        for b in range(2000):
            boot_rates = []
            for t in TYPES_ORDERED:
                arr = clause_rate_arrays[t]
                n = len(arr)
                n_resample = max(2, int(n * scale))
                idx = rng.randint(0, n, size=n_resample)
                boot_rates.append(np.mean(arr[idx]))
            boot_vec = np.array(boot_rates).reshape(-1, 1)
            try:
                Z_b = linkage(boot_vec, method="ward")
                bk2 = fcluster(Z_b, t=2, criterion="maxclust")
                inc_clust = bk2[0]
                if sum(1 for c in bk2 if c == inc_clust) == 1:
                    n_singleton += 1
            except Exception:
                pass
        au_results[scale] = n_singleton / 2000

    # Simple AU p-value estimate: extrapolate from multiscale
    # Use the proportion at scale=1.0 as bootstrap probability (BP)
    bp = inc_singleton_count / B_CLUSTER
    # AU approximation: use scale=2.0 result as better estimate
    au_pvalue = au_results.get(2.0, bp)

    result = {
        "observed_type_rates": {t: round(obs_rates[t], 4) for t in TYPES_ORDERED},
        "k2_cluster_membership": k2_membership,
        "k3_cluster_membership": k3_membership,
        "incompleteness_singleton_at_k2": inc_singleton_obs,
        "bootstrap": {
            "B": B_CLUSTER,
            "incompleteness_singleton_pct": round(inc_singleton_count / B_CLUSTER * 100, 2),
            "same_k2_structure_pct": round(same_k2_count / B_CLUSTER * 100, 2),
        },
        "multiscale_bootstrap": {str(s): round(v, 4) for s, v in au_results.items()},
        "au_pvalue_approx": round(au_pvalue, 4),
        "bp_value": round(bp, 4),
    }
    return result


# ════════════════════════════════════════════════════════════════
# Analysis 2: Bootstrap Model Ranking CI for Auth Scope (N2)
# ════════════════════════════════════════════════════════════════

def analysis_n2(ambig_data):
    """Bootstrap ranking stability for authorization_scope within GPT-5.4 judge subset."""
    rng = np.random.RandomState(SEED + 1)

    # Get per-clause binary violations for auth_scope, ambiguous, per model
    # Each clause has exactly 1 episode per model -> violation is 0 or 1
    auth_data = ambig_data["authorization_scope"]

    model_clause_violations = {m: [] for m in GPT54_JUDGED_MODELS}
    clause_ids = sorted(auth_data.keys())

    for c_id in clause_ids:
        for m in GPT54_JUDGED_MODELS:
            if m in auth_data[c_id]:
                model_clause_violations[m].append(auth_data[c_id][m])

    # Observed rates
    obs_rates = {}
    for m in GPT54_JUDGED_MODELS:
        vals = model_clause_violations[m]
        obs_rates[m] = np.mean(vals)

    # Observed ranking (ascending violation rate)
    obs_ranking = sorted(GPT54_JUDGED_MODELS, key=lambda m: obs_rates[m])

    # Bootstrap: resample 50 clauses with replacement, recompute per-model rates
    ranking_preserved_count = 0
    boot_rates_collection = {m: [] for m in GPT54_JUDGED_MODELS}

    n_clauses = len(clause_ids)
    # Pre-build arrays indexed by clause position
    model_arrays = {}
    for m in GPT54_JUDGED_MODELS:
        arr = []
        for c_id in clause_ids:
            arr.append(auth_data[c_id].get(m, 0.0))
        model_arrays[m] = np.array(arr)

    for b in range(B_RANKING):
        idx = rng.randint(0, n_clauses, size=n_clauses)
        boot_model_rates = {}
        for m in GPT54_JUDGED_MODELS:
            boot_model_rates[m] = np.mean(model_arrays[m][idx])
            boot_rates_collection[m].append(boot_model_rates[m])

        # Check if ranking preserved
        boot_ranking = sorted(GPT54_JUDGED_MODELS, key=lambda m: boot_model_rates[m])
        if boot_ranking == obs_ranking:
            ranking_preserved_count += 1

    # 95% CIs
    cis = {}
    for m in GPT54_JUDGED_MODELS:
        arr = np.array(boot_rates_collection[m])
        ci_lo = np.percentile(arr, 2.5)
        ci_hi = np.percentile(arr, 97.5)
        cis[m] = {
            "observed_rate": round(obs_rates[m], 4),
            "ci_95_lower": round(ci_lo, 4),
            "ci_95_upper": round(ci_hi, 4),
            "bootstrap_mean": round(np.mean(arr), 4),
            "bootstrap_sd": round(np.std(arr), 4),
        }

    # Also check pairwise ordering stability
    pairwise = {}
    for i, m1 in enumerate(obs_ranking):
        for m2 in obs_ranking[i + 1:]:
            arr1 = np.array(boot_rates_collection[m1])
            arr2 = np.array(boot_rates_collection[m2])
            pct = np.mean(arr1 < arr2) * 100
            pairwise[f"{m1} < {m2}"] = round(pct, 2)

    result = {
        "judge_subset": "gpt-5.4",
        "models_tested": GPT54_JUDGED_MODELS,
        "observed_ranking": obs_ranking,
        "observed_rates": {m: round(obs_rates[m], 4) for m in GPT54_JUDGED_MODELS},
        "bootstrap": {
            "B": B_RANKING,
            "ranking_preserved_pct": round(ranking_preserved_count / B_RANKING * 100, 2),
        },
        "per_model_95ci": cis,
        "pairwise_ordering_stability": pairwise,
    }
    return result


# ════════════════════════════════════════════════════════════════
# Analysis 3: Clause-level Variance (W5)
# ════════════════════════════════════════════════════════════════

def analysis_w5(clause_rates):
    """Within-type clause-level heterogeneity and leave-one-out sensitivity."""
    result = {}

    for t in TYPES_ORDERED:
        rates = np.array([r for _, r in clause_rates[t]])
        n = len(rates)
        mean = np.mean(rates)
        sd = np.std(rates, ddof=1) if n > 1 else 0.0
        cv = sd / mean if mean > 0 else float("inf")

        # Leave-one-out
        loo_estimates = []
        for i in range(n):
            remaining = np.delete(rates, i)
            loo_estimates.append(np.mean(remaining))
        loo_estimates = np.array(loo_estimates)
        loo_range = float(np.max(loo_estimates) - np.min(loo_estimates))

        # Identify influential clauses (those whose removal changes rate the most)
        loo_diffs = np.abs(loo_estimates - mean)
        top_influential_idx = np.argsort(-loo_diffs)[:3]
        influential_clauses = []
        for idx in top_influential_idx:
            c_id, c_rate = clause_rates[t][idx]
            influential_clauses.append({
                "clause_id": c_id,
                "clause_rate": round(c_rate, 4),
                "loo_type_rate": round(loo_estimates[idx], 4),
                "shift": round(loo_estimates[idx] - mean, 4),
            })

        result[t] = {
            "n_clauses": n,
            "mean": round(mean, 4),
            "sd": round(sd, 4),
            "min": round(float(np.min(rates)), 4),
            "max": round(float(np.max(rates)), 4),
            "cv": round(cv, 4),
            "variance": round(float(np.var(rates, ddof=1)), 4),
            "loo": {
                "min_estimate": round(float(np.min(loo_estimates)), 4),
                "max_estimate": round(float(np.max(loo_estimates)), 4),
                "range": round(loo_range, 4),
            },
            "top_influential_clauses": influential_clauses,
        }

    return result


# ════════════════════════════════════════════════════════════════
# Main
# ════════════════════════════════════════════════════════════════

def print_summary(n1, n2, w5):
    """Print human-readable summary of all three analyses."""
    print("=" * 72)
    print("SUPPLEMENTARY ANALYSES — ROUND 8")
    print("=" * 72)

    print("\n─── Analysis N1: Bootstrap Cluster Analysis ───")
    print(f"\nObserved per-type ambiguous violation rates:")
    for t in TYPES_ORDERED:
        print(f"  {t:30s} {n1['observed_type_rates'][t]:.1%}")

    print(f"\nWard's hierarchical clustering:")
    print(f"  k=2 clusters:")
    for k in sorted(set(n1["k2_cluster_membership"].values())):
        members = [t for t, v in n1["k2_cluster_membership"].items() if v == k]
        print(f"    Cluster {k}: {', '.join(members)}")
    print(f"  k=3 clusters:")
    for k in sorted(set(n1["k3_cluster_membership"].values())):
        members = [t for t, v in n1["k3_cluster_membership"].items() if v == k]
        print(f"    Cluster {k}: {', '.join(members)}")

    print(f"\n  Incompleteness is singleton at k=2: {n1['incompleteness_singleton_at_k2']}")
    bs = n1["bootstrap"]
    print(f"  Bootstrap (B={bs['B']:,}):")
    print(f"    Incompleteness singleton:  {bs['incompleteness_singleton_pct']:.1f}%")
    print(f"    Same k=2 structure:        {bs['same_k2_structure_pct']:.1f}%")
    print(f"  AU p-value (approx):         {n1['au_pvalue_approx']:.4f}")
    print(f"  BP value:                    {n1['bp_value']:.4f}")
    ms = n1["multiscale_bootstrap"]
    print(f"  Multiscale bootstrap (singleton rate by scale):")
    for s, v in sorted(ms.items(), key=lambda x: float(x[0])):
        print(f"    scale={s}: {v:.4f}")

    print("\n─── Analysis N2: Bootstrap Model Ranking CI (Auth Scope) ───")
    print(f"\n  Judge subset: {n2['judge_subset']}")
    print(f"  Observed ranking (ascending violation rate): {' < '.join(n2['observed_ranking'])}")
    print(f"  Observed rates:")
    for m in n2["observed_ranking"]:
        r = n2["observed_rates"][m]
        ci = n2["per_model_95ci"][m]
        print(f"    {m:25s} {r:.1%}  95% CI [{ci['ci_95_lower']:.1%}, {ci['ci_95_upper']:.1%}]")
    print(f"\n  Bootstrap (B={n2['bootstrap']['B']:,}):")
    print(f"    Full ranking preserved: {n2['bootstrap']['ranking_preserved_pct']:.1f}%")
    print(f"  Pairwise ordering stability:")
    for pair, pct in n2["pairwise_ordering_stability"].items():
        print(f"    {pair}: {pct:.1f}%")

    print("\n─── Analysis W5: Clause-level Variance ───")
    print(f"\n  {'Type':30s} {'Mean':>6s} {'SD':>6s} {'CV':>6s} {'Min':>6s} {'Max':>6s} {'LOO range':>10s}")
    print(f"  {'-'*30} {'-'*6} {'-'*6} {'-'*6} {'-'*6} {'-'*6} {'-'*10}")
    for t in TYPES_ORDERED:
        d = w5[t]
        print(f"  {t:30s} {d['mean']:6.3f} {d['sd']:6.3f} {d['cv']:6.3f} {d['min']:6.3f} {d['max']:6.3f} {d['loo']['range']:10.4f}")

    print(f"\n  Top influential clauses per type:")
    for t in TYPES_ORDERED:
        print(f"    {t}:")
        for ic in w5[t]["top_influential_clauses"]:
            print(f"      {ic['clause_id']}: rate={ic['clause_rate']:.2f}, LOO shift={ic['shift']:+.4f}")

    print("\n" + "=" * 72)
    print(f"Results saved to: {OUTPUT_JSON}")
    print("=" * 72)


def main():
    print("Loading data...")
    ambig_data, type_model_viol = load_data()

    print("Computing clause-level rates...")
    clause_rates = compute_clause_level_rates(ambig_data)

    print(f"Running Analysis N1: Bootstrap Cluster Analysis (B={B_CLUSTER:,})...")
    n1 = analysis_n1(ambig_data, clause_rates)

    print(f"Running Analysis N2: Bootstrap Model Ranking CI (B={B_RANKING:,})...")
    n2 = analysis_n2(ambig_data)

    print("Running Analysis W5: Clause-level Variance...")
    w5 = analysis_w5(clause_rates)

    # Save results
    results = {
        "N1_bootstrap_cluster": n1,
        "N2_auth_scope_ranking": n2,
        "W5_clause_variance": w5,
    }

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_JSON, "w") as f:
        json.dump(results, f, indent=2)

    print_summary(n1, n2, w5)


if __name__ == "__main__":
    main()
