#!/usr/bin/env python3
"""
correction_k_sensitivity.py — Correction Method Ranking Stability across K

Tests whether the correction method ranking from Table 4 (K=3) is stable
at K=5 and K=10.  For each K, samples 5 random Dirichlet confusion matrices
(diagonal >= 0.6), runs 100 MC reps per {topology x C} combination across
all 5 correction methods, and compares method rankings via Spearman rho.

Output: artifacts/correction_k_sensitivity_results.json

Dependencies: numpy, scipy (for Spearman), annot_sensitivity (local package)
"""

import sys
import os
import json
import time
import numpy as np
from scipy import stats

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

from annot_sensitivity.correction import (
    correct_ppi, correct_naive_plugin, correct_dsl, correct_mcsimex, correct_mla
)
from annot_sensitivity.utils import misclassify, make_dummies, ols

# ── Import K-flexible DGP infrastructure from compute_ppi_empirical ──
# We reuse the DGP generators and make_dgp_params from that file.
from artifacts.compute_ppi_empirical import (
    make_dgp_params, make_p_A,
    gen_confounding, gen_mediation, gen_collider, gen_exposure,
    gen_mbias, gen_iv, gen_frontdoor,
    GEN_FNS, HAS_TREATMENT,
    compute_tau_true,
    ppi_wald, mcsimex_wald, wald_est,
)

# ── Configuration ──────────────────────────────────────────────────

K_VALUES = [3, 5, 10]
N_SAMPLES = 5000
N_REPS = 100
N_CONFUSION = 5          # random confusion matrices per K
GOLD_FRACTION = 0.10
SEED = 2026

TOPOLOGIES = ['confounding', 'mediation', 'collider', 'exposure',
              'mbias', 'iv', 'frontdoor']
METHODS = ['ppi', 'naive_plugin', 'dsl', 'mcsimex', 'mla']


# ── Random Confusion Matrix ───────────────────────────────────────

def random_confusion_matrix(K, min_diag=0.6, rng=None):
    """Sample a column-stochastic confusion matrix with diagonal >= min_diag.

    Uses Dirichlet sampling with concentration toward the diagonal,
    then rejects/resamples any column whose diagonal < min_diag.

    Args:
        K: number of categories
        min_diag: minimum diagonal element per column
        rng: numpy random Generator

    Returns:
        (K, K) column-stochastic matrix with all diag >= min_diag
    """
    if rng is None:
        rng = np.random.default_rng()
    C = np.zeros((K, K))
    for k in range(K):
        while True:
            # Dirichlet with high concentration on diagonal
            alphas = np.full(K, 0.5)
            alphas[k] = max(K * 2.0, 5.0)  # strong diagonal
            col = rng.dirichlet(alphas)
            if col[k] >= min_diag:
                C[:, k] = col
                break
    return C


# ── Oracle tau computation ─────────────────────────────────────────

def compute_oracle_tau(K, topology, params, N_large=500_000, seed=99):
    """Compute true tau by running estimator on very large uncontaminated sample."""
    rng = np.random.default_rng(seed)
    first_var, Y, A = GEN_FNS[topology](K, N_large, params[topology], rng)

    if topology == 'iv':
        return wald_est(first_var, Y, A, k=1)
    elif topology == 'exposure':
        D = make_dummies(A, K)
        X = np.column_stack([np.ones(N_large), D])
        beta = np.linalg.lstsq(X, Y, rcond=None)[0]
        return float(beta[1])
    else:
        T = first_var
        D = make_dummies(A, K)
        X = np.column_stack([np.ones(N_large), T, D])
        beta = np.linalg.lstsq(X, Y, rcond=None)[0]
        return float(beta[1])


# ── Single MC replication ──────────────────────────────────────────

def run_single_rep(K, topology, params, C, tau_true, rng):
    """Run one MC replication: generate data, misclassify, apply corrections.

    Returns dict mapping method_name -> tau_hat (or None if failed).
    Also returns 'naive' (uncorrected) estimate.
    """
    N = N_SAMPLES
    first_var, Y, A = GEN_FNS[topology](K, N, params[topology], rng)
    Astar = misclassify(A, C, rng)

    n_gold = max(int(N * GOLD_FRACTION), 50)
    gold_idx = rng.choice(N, size=n_gold, replace=False)
    gold_mask = np.zeros(N, dtype=bool)
    gold_mask[gold_idx] = True

    results = {}

    if topology == 'iv':
        Z = first_var
        # Naive (uncorrected Wald)
        tau_naive = wald_est(Z, Y, Astar, k=1)
        results['naive'] = float(tau_naive) if np.isfinite(tau_naive) else None

        # PPI++ Wald
        tau_ppi, ok = ppi_wald(Z, Y, A, Astar, gold_mask, k=1, rng=rng)
        results['ppi'] = float(tau_ppi) if ok and np.isfinite(tau_ppi) else None

        # MC-SIMEX Wald
        tau_sim, ok = mcsimex_wald(Z, Y, Astar, C, k=1, rng=rng)
        results['mcsimex'] = float(tau_sim) if ok and np.isfinite(tau_sim) else None

        # naive_plugin, dsl, mla not applicable for IV Wald
        results['naive_plugin'] = None
        results['dsl'] = None
        results['mla'] = None

    elif topology == 'exposure':
        # No T variable: Y = beta_0 + D @ beta[1:] + eps
        X_other = np.ones((N, 1))
        D_star = make_dummies(Astar, K)
        X_full = np.column_stack([X_other, D_star])
        try:
            beta_naive = np.linalg.lstsq(X_full, Y, rcond=None)[0]
            tau_naive = float(beta_naive[1])
        except Exception:
            tau_naive = np.nan
        results['naive'] = float(tau_naive) if np.isfinite(tau_naive) else None

        for method in METHODS:
            try:
                if method == 'ppi':
                    tau, se, ok = correct_ppi(X_other, Y, Astar, A,
                                              gold_mask, tau_idx=1, rng=rng)
                elif method == 'naive_plugin':
                    tau, se, ok = correct_naive_plugin(X_other, Y, Astar,
                                                       C, tau_idx=1)
                elif method == 'dsl':
                    tau, se, ok = correct_dsl(X_other, Y, Astar, A,
                                              gold_mask, tau_idx=1)
                elif method == 'mcsimex':
                    tau, se, ok = correct_mcsimex(X_other, Y, Astar,
                                                   C, tau_idx=1, rng=rng)
                elif method == 'mla':
                    tau, se, ok = correct_mla(X_other, Y, Astar,
                                               C, tau_idx=1)
                else:
                    continue
                results[method] = float(tau) if ok and np.isfinite(tau) else None
            except Exception:
                results[method] = None

    else:
        # Standard topologies with T variable
        T = first_var
        X_other = np.column_stack([np.ones(N), T])
        D_star = make_dummies(Astar, K)
        X_full = np.column_stack([X_other, D_star])
        try:
            beta_naive = np.linalg.lstsq(X_full, Y, rcond=None)[0]
            tau_naive = float(beta_naive[1])
        except Exception:
            tau_naive = np.nan
        results['naive'] = float(tau_naive) if np.isfinite(tau_naive) else None

        for method in METHODS:
            try:
                if method == 'ppi':
                    tau, se, ok = correct_ppi(X_other, Y, Astar, A,
                                              gold_mask, tau_idx=1, rng=rng)
                elif method == 'naive_plugin':
                    tau, se, ok = correct_naive_plugin(X_other, Y, Astar,
                                                       C, tau_idx=1)
                elif method == 'dsl':
                    tau, se, ok = correct_dsl(X_other, Y, Astar, A,
                                              gold_mask, tau_idx=1)
                elif method == 'mcsimex':
                    tau, se, ok = correct_mcsimex(X_other, Y, Astar,
                                                   C, tau_idx=1, rng=rng)
                elif method == 'mla':
                    tau, se, ok = correct_mla(X_other, Y, Astar,
                                               C, tau_idx=1)
                else:
                    continue
                results[method] = float(tau) if ok and np.isfinite(tau) else None
            except Exception:
                results[method] = None

    return results


# ── Main ───────────────────────────────────────────────────────────

def main():
    t_start = time.time()
    print("=" * 70)
    print("Correction Method Ranking Stability: K=3 vs K=5 vs K=10")
    print("=" * 70)
    print(f"N_SAMPLES={N_SAMPLES}, N_REPS={N_REPS}, N_CONFUSION={N_CONFUSION}")
    print(f"GOLD_FRACTION={GOLD_FRACTION}, SEED={SEED}")
    print(f"Topologies: {TOPOLOGIES}")
    print(f"Methods: {METHODS}")
    print()

    rng_master = np.random.default_rng(SEED)

    # Storage: results[K_label][topology][method] = bias_reduction_pct
    all_results = {}

    for K in K_VALUES:
        K_label = f"K={K}"
        print(f"\n{'='*60}")
        print(f"  K = {K}")
        print(f"{'='*60}")

        params = make_dgp_params(K)

        # Compute oracle tau for each topology
        print("  Computing tau_true (N=500k)...")
        tau_true = {}
        for topo in TOPOLOGIES:
            tau_true[topo] = compute_oracle_tau(K, topo, params)
            print(f"    {topo}: tau_true = {tau_true[topo]:.6f}")

        # Sample confusion matrices
        print(f"  Sampling {N_CONFUSION} random confusion matrices...")
        confusion_matrices = []
        for ci in range(N_CONFUSION):
            C = random_confusion_matrix(K, min_diag=0.6,
                                         rng=np.random.default_rng(
                                             rng_master.integers(0, 2**31)))
            confusion_matrices.append(C)
            print(f"    C[{ci}]: diag_min={np.diag(C).min():.3f}, "
                  f"diag_mean={np.diag(C).mean():.3f}")

        # Run MC for each topology x confusion matrix
        topo_results = {}
        total_combos = len(TOPOLOGIES) * N_CONFUSION
        combo_i = 0

        for topo in TOPOLOGIES:
            method_biases = {m: [] for m in METHODS}  # accumulate across all C's
            naive_biases_all = []

            for ci, C in enumerate(confusion_matrices):
                combo_i += 1
                t_combo = time.time()
                print(f"  [{combo_i}/{total_combos}] K={K} / {topo} / C[{ci}]",
                      end="", flush=True)

                rep_results = []
                for rep in range(N_REPS):
                    seed_rep = rng_master.integers(0, 2**31)
                    rng_rep = np.random.default_rng(seed_rep)
                    res = run_single_rep(K, topo, params, C,
                                         tau_true[topo], rng_rep)
                    rep_results.append(res)

                # Compute biases
                tt = tau_true[topo]
                for res in rep_results:
                    if res['naive'] is not None:
                        naive_biases_all.append(abs(res['naive'] - tt))
                    for m in METHODS:
                        if res.get(m) is not None:
                            method_biases[m].append(abs(res[m] - tt))

                elapsed = time.time() - t_combo
                print(f"  [{elapsed:.1f}s]")

            # Compute mean bias reduction per method for this topology
            avg_naive_bias = np.mean(naive_biases_all) if naive_biases_all else None
            topo_method_results = {}

            for m in METHODS:
                biases = method_biases[m]
                if biases and avg_naive_bias and avg_naive_bias > 1e-8:
                    avg_method_bias = np.mean(biases)
                    reduction = 1.0 - avg_method_bias / avg_naive_bias
                    topo_method_results[m] = round(float(reduction) * 100, 2)
                else:
                    topo_method_results[m] = None

            topo_results[topo] = topo_method_results
            print(f"    {topo}: ", end="")
            for m in METHODS:
                v = topo_method_results[m]
                print(f"{m}={v}%  " if v is not None else f"{m}=N/A  ", end="")
            print()

        all_results[K_label] = topo_results

    # ── Rank stability analysis ────────────────────────────────────
    print("\n" + "=" * 70)
    print("RANK STABILITY ANALYSIS")
    print("=" * 70)

    def get_ranking_vector(results_dict):
        """Convert per-topology method results to a flat ranking vector.

        For each topology, rank methods by bias reduction (higher = better).
        Return the flat vector of ranks across all topologies.
        """
        all_ranks = []
        for topo in TOPOLOGIES:
            topo_res = results_dict.get(topo, {})
            # Get method values (None -> -inf for ranking)
            vals = []
            for m in METHODS:
                v = topo_res.get(m)
                vals.append(v if v is not None else -9999)
            # Rank: higher reduction = rank 1
            order = np.argsort(vals)[::-1]
            ranks = np.zeros(len(METHODS))
            for rank_pos, idx in enumerate(order):
                ranks[idx] = rank_pos + 1
            all_ranks.extend(ranks)
        return np.array(all_ranks)

    rank_k3 = get_ranking_vector(all_results["K=3"])
    rank_k5 = get_ranking_vector(all_results["K=5"])
    rank_k10 = get_ranking_vector(all_results["K=10"])

    rho_3v5, pval_3v5 = stats.spearmanr(rank_k3, rank_k5)
    rho_3v10, pval_3v10 = stats.spearmanr(rank_k3, rank_k10)
    rho_5v10, pval_5v10 = stats.spearmanr(rank_k5, rank_k10)

    print(f"\nSpearman rank correlation (across {len(TOPOLOGIES)} topologies "
          f"x {len(METHODS)} methods = {len(rank_k3)} pairs):")
    print(f"  K=3 vs K=5:  rho = {rho_3v5:.4f}  (p = {pval_3v5:.4e})")
    print(f"  K=3 vs K=10: rho = {rho_3v10:.4f}  (p = {pval_3v10:.4e})")
    print(f"  K=5 vs K=10: rho = {rho_5v10:.4f}  (p = {pval_5v10:.4e})")

    # Per-topology Spearman (methods only, not flattened)
    per_topo_spearman = {}
    for topo in TOPOLOGIES:
        vals_3 = [all_results["K=3"].get(topo, {}).get(m, -9999) or -9999
                  for m in METHODS]
        vals_5 = [all_results["K=5"].get(topo, {}).get(m, -9999) or -9999
                  for m in METHODS]
        vals_10 = [all_results["K=10"].get(topo, {}).get(m, -9999) or -9999
                   for m in METHODS]

        rho_35, _ = stats.spearmanr(vals_3, vals_5)
        rho_310, _ = stats.spearmanr(vals_3, vals_10)
        per_topo_spearman[topo] = {
            "K3_vs_K5": round(float(rho_35), 4) if np.isfinite(rho_35) else None,
            "K3_vs_K10": round(float(rho_310), 4) if np.isfinite(rho_310) else None,
        }
        print(f"  {topo:14s}: K3vsK5={rho_35:.3f}  K3vsK10={rho_310:.3f}")

    # Determine stability: stable if all global rho > 0.7
    stable = (rho_3v5 > 0.7) and (rho_3v10 > 0.7) and (rho_5v10 > 0.7)
    print(f"\nStability verdict: {'STABLE' if stable else 'UNSTABLE'} "
          f"(threshold: rho > 0.7)")

    # ── Per-topology best method consistency ───────────────────────
    print("\n" + "-" * 50)
    print("Best method per topology across K values:")
    print(f"{'Topology':14s}  {'K=3':14s}  {'K=5':14s}  {'K=10':14s}  Consistent?")
    print("-" * 70)
    best_consistent = 0
    for topo in TOPOLOGIES:
        bests = []
        for K_label in ["K=3", "K=5", "K=10"]:
            topo_res = all_results[K_label].get(topo, {})
            valid = {m: v for m, v in topo_res.items() if v is not None}
            if valid:
                best_m = max(valid, key=valid.get)
            else:
                best_m = "N/A"
            bests.append(best_m)
        consistent = len(set(bests)) == 1
        if consistent:
            best_consistent += 1
        mark = "YES" if consistent else "NO"
        print(f"{topo:14s}  {bests[0]:14s}  {bests[1]:14s}  {bests[2]:14s}  {mark}")
    print(f"\nConsistent: {best_consistent}/{len(TOPOLOGIES)} topologies")

    # ── Save results ───────────────────────────────────────────────
    output = {
        "meta": {
            "description": "Correction method ranking stability across K values",
            "k_values": K_VALUES,
            "n_samples": N_SAMPLES,
            "n_reps": N_REPS,
            "n_confusion_matrices": N_CONFUSION,
            "gold_fraction": GOLD_FRACTION,
            "seed": SEED,
            "topologies": TOPOLOGIES,
            "methods": METHODS,
        },
        "k_values": K_VALUES,
        "results": all_results,
        "rank_stability": {
            "K3_vs_K5_spearman": round(float(rho_3v5), 4),
            "K3_vs_K5_pvalue": float(pval_3v5),
            "K3_vs_K10_spearman": round(float(rho_3v10), 4),
            "K3_vs_K10_pvalue": float(pval_3v10),
            "K5_vs_K10_spearman": round(float(rho_5v10), 4),
            "K5_vs_K10_pvalue": float(pval_5v10),
            "per_topology": per_topo_spearman,
            "stable": stable,
        },
    }

    out_path = os.path.join(PROJECT_ROOT, 'artifacts',
                            'correction_k_sensitivity_results.json')
    with open(out_path, 'w') as f:
        json.dump(output, f, indent=2)

    elapsed = time.time() - t_start
    print(f"\nResults saved to: {out_path}")
    print(f"Total runtime: {elapsed:.1f}s ({elapsed/60:.1f} min)")


if __name__ == '__main__':
    main()
