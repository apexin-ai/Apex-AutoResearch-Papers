#!/usr/bin/env python3
"""
Ĉ Estimation Robustness Experiment.

Question: With a finite K-class gold-labelled set used to estimate C, does
the safe/fragile topology partition (5 vs 2) hold under multinomial bootstrap
of Ĉ?

For each empirical column-stochastic K=3 confusion matrix C (LLM truth),
draw B bootstrap replicates Ĉ ~ multinomial(C[:,k] · n_gold) / n_gold for
each class k. For each Ĉ, recompute the magnitude ASV δ* for the 7
topologies (confounding, mediation, collider, exposure, mbias, IV,
frontdoor) and report:

  • Partition stability rate vs n_gold: fraction of bootstraps where the
    two lowest-ASV topologies equal {exposure, IV}.
  • Spearman ρ vs n_gold: rank correlation between ASV ranking from Ĉ and
    from true C (averaged over bootstraps and source matrices).

Empirical Cs come from artifacts/updated_empirical_results.json (23 LLM
matrices; 8 are K=3 vast/stance — the K=3 framework subset).

Output: c_estimation_robustness_results.json next to this script.
"""

import json
import os
import sys
import time
from collections import defaultdict

import numpy as np
from scipy.stats import rankdata, spearmanr

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ranking_stability import (  # noqa: E402
    ALL_TOPOS, COMPUTE_SS, DGP_PARAMS, K, N_DELTA, DELTAS, ASV_EPSILON,
    PROTECTIVE, get_tau_true, process_batch_iv, process_batch_exposure,
    process_batch_with_T,
)

# ──────────────────────────────────────────────────────────────────────────
EMP_PATH = '/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/artifacts/updated_empirical_results.json'
OUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUT_PATH = os.path.join(OUT_DIR, 'c_estimation_robustness_results.json')

N_GOLD_GRID = [50, 100, 200, 500]
B_BOOT = 200
SEED = 20260523
SAFE = {'confounding', 'mediation', 'collider', 'frontdoor', 'mbias'}
FRAGILE = {'exposure', 'iv'}
RANK_TOPOS = ['confounding', 'mediation', 'collider', 'exposure',
              'mbias', 'iv', 'frontdoor']
TOPO_IDX = {t: i for i, t in enumerate(RANK_TOPOS)}


def load_k3_matrices():
    with open(EMP_PATH) as f:
        d = json.load(f)
    out = {}
    for name, cm in d['confusion_matrices'].items():
        arr = np.asarray(cm, dtype=float)
        if arr.shape == (K, K):
            # Re-normalise columns just in case
            cs = arr.sum(axis=0, keepdims=True)
            cs = np.where(cs < 1e-12, 1.0, cs)
            out[name] = arr / cs
    return out


def bootstrap_chats(C_true, n_gold, B, rng):
    """Multinomial bootstrap of Ĉ.

    For each class k, draw n_gold predictions from C_true[:, k] then
    normalise. Returns (B, K, K) array of column-stochastic matrices.
    """
    out = np.empty((B, K, K))
    for k in range(K):
        # rng.multinomial returns (B, K) with each row summing to n_gold
        counts = rng.multinomial(n_gold, C_true[:, k], size=B)
        out[:, :, k] = counts / float(n_gold)
    return out


def compute_asv_for_matrices(C0_batch, all_ss, all_tau_true):
    """Compute magnitude ASV per topology for a batch of C0 matrices.

    Returns asv: (M, n_topo) ndarray. Collider/M-bias get +inf (protective).
    """
    M = C0_batch.shape[0]
    n_topo = len(RANK_TOPOS)
    asv = np.full((M, n_topo), np.nan)
    # Protective topologies: always inf
    asv[:, TOPO_IDX['collider']] = np.inf
    asv[:, TOPO_IDX['mbias']] = np.inf

    for topo in RANK_TOPOS:
        if topo in PROTECTIVE:
            continue
        ss = all_ss[topo]
        tau_true = all_tau_true[topo]
        if topo == 'iv':
            vals = process_batch_iv(C0_batch, ss, tau_true)
        elif topo == 'exposure':
            vals, _ = process_batch_exposure(C0_batch, ss, tau_true)
        else:
            vals, _ = process_batch_with_T(C0_batch, ss, tau_true, topo)
        asv[:, TOPO_IDX[topo]] = vals
    return asv


def partition_from_asv(asv_row):
    """Bottom-2 topologies (smallest ASV) form the fragile set."""
    order = np.argsort(asv_row, kind='stable')
    return frozenset(RANK_TOPOS[i] for i in order[:2])


def spearman_versus_truth(asv_boot, asv_true):
    """Spearman rho between bootstrap ASV ranking and truth ranking."""
    # Handle infinities: replace +inf with large finite via rank ordering.
    # scipy.spearmanr is OK with finite inputs; rankdata handles infinities.
    r_true = rankdata(asv_true)
    r_boot = rankdata(asv_boot)
    # If all values are identical (or all inf), correlation undefined → NaN
    if np.all(r_true == r_true[0]) or np.all(r_boot == r_boot[0]):
        return np.nan
    rho, _ = spearmanr(r_true, r_boot)
    return rho


def main():
    t_total = time.time()
    print('Ĉ Estimation Robustness Experiment')
    print(f'  K={K}, B={B_BOOT}, n_gold ∈ {N_GOLD_GRID}')
    print(f'  Topologies: {RANK_TOPOS}')
    print(f'  ASV threshold (magnitude): {ASV_EPSILON}')
    print(f'  n_delta = {N_DELTA}')
    print('=' * 70)
    sys.stdout.flush()

    # Precompute analytic sufficient statistics + tau_true
    print('\nPrecomputing sufficient statistics & tau_true...')
    all_ss = {}
    all_tau_true = {}
    for topo in ALL_TOPOS:
        ss = COMPUTE_SS[topo](DGP_PARAMS[topo])
        all_ss[topo] = ss
        all_tau_true[topo] = get_tau_true(topo, ss)
        print(f'  {topo:<12} tau_true = {all_tau_true[topo]:.6f}')
    sys.stdout.flush()

    # Load empirical K=3 matrices
    print('\nLoading empirical K=3 confusion matrices...')
    Cs = load_k3_matrices()
    print(f'  Loaded {len(Cs)} K=3 matrices')
    for name in Cs:
        print(f'    {name}  diag={np.diag(Cs[name]).round(3).tolist()}')
    sys.stdout.flush()

    # Truth ASV per source C
    print('\nComputing ASV for the truth Cs...')
    truth_C_batch = np.stack(list(Cs.values()))
    truth_asv = compute_asv_for_matrices(truth_C_batch, all_ss, all_tau_true)
    truth_partition = {}
    truth_asv_dict = {}
    for i, name in enumerate(Cs):
        truth_partition[name] = partition_from_asv(truth_asv[i])
        truth_asv_dict[name] = {
            RANK_TOPOS[j]: (None if np.isinf(truth_asv[i, j])
                            else float(truth_asv[i, j]))
            for j in range(len(RANK_TOPOS))
        }
        eq = 'YES' if truth_partition[name] == FRAGILE else 'NO'
        print(f'  {name}  fragile-set={sorted(truth_partition[name])}  '
              f'matches canonical: {eq}')
    sys.stdout.flush()

    # Bootstrap loop
    print(f'\nBootstrapping (B={B_BOOT})...')
    rng = np.random.default_rng(SEED)

    results_per_n = {}
    for n_gold in N_GOLD_GRID:
        t0 = time.time()
        partition_match_total = 0   # vs canonical {exposure,iv}
        partition_match_truth = 0   # vs source-C truth partition
        n_bootstraps_total = 0
        rho_values_vs_truth = []
        rho_values_vs_theoretical_safe = []

        # Per-source-C aggregates
        per_C = {}

        for name, C_true in Cs.items():
            boot = bootstrap_chats(C_true, n_gold, B_BOOT, rng)
            asv_boot = compute_asv_for_matrices(
                boot, all_ss, all_tau_true)  # (B, n_topo)

            truth_row = truth_asv[list(Cs).index(name)]

            n_match_canon = 0
            n_match_truth = 0
            rho_vs_truth = []
            for b in range(B_BOOT):
                part = partition_from_asv(asv_boot[b])
                if part == FRAGILE:
                    n_match_canon += 1
                if part == truth_partition[name]:
                    n_match_truth += 1
                rho_vs_truth.append(
                    spearman_versus_truth(asv_boot[b], truth_row))

            rho_vs_truth = np.array(rho_vs_truth, dtype=float)
            rho_clean = rho_vs_truth[~np.isnan(rho_vs_truth)]

            per_C[name] = {
                'partition_match_canonical': n_match_canon / B_BOOT,
                'partition_match_truth_C': n_match_truth / B_BOOT,
                'spearman_rho_mean_vs_truth':
                    float(rho_clean.mean()) if rho_clean.size else float('nan'),
                'spearman_rho_median_vs_truth':
                    float(np.median(rho_clean)) if rho_clean.size else float('nan'),
                'spearman_rho_q25_vs_truth':
                    float(np.quantile(rho_clean, 0.25)) if rho_clean.size else float('nan'),
                'truth_partition_matches_canonical':
                    truth_partition[name] == FRAGILE,
            }

            partition_match_total += n_match_canon
            partition_match_truth += n_match_truth
            n_bootstraps_total += B_BOOT
            rho_values_vs_truth.extend(rho_clean.tolist())

        results_per_n[n_gold] = {
            'n_bootstraps_total': n_bootstraps_total,
            'partition_stability_rate_vs_canonical':
                partition_match_total / n_bootstraps_total,
            'partition_stability_rate_vs_truth_C':
                partition_match_truth / n_bootstraps_total,
            'spearman_rho_mean':
                float(np.mean(rho_values_vs_truth)) if rho_values_vs_truth
                else float('nan'),
            'spearman_rho_median':
                float(np.median(rho_values_vs_truth)) if rho_values_vs_truth
                else float('nan'),
            'spearman_rho_q25':
                float(np.quantile(rho_values_vs_truth, 0.25))
                if rho_values_vs_truth else float('nan'),
            'spearman_rho_q75':
                float(np.quantile(rho_values_vs_truth, 0.75))
                if rho_values_vs_truth else float('nan'),
            'per_source_C': per_C,
        }
        elapsed = time.time() - t0
        r = results_per_n[n_gold]
        print(f'  n_gold={n_gold:<4}  '
              f'partition_rate_canonical={r["partition_stability_rate_vs_canonical"]:.4f}  '
              f'partition_rate_truth={r["partition_stability_rate_vs_truth_C"]:.4f}  '
              f'rho_mean={r["spearman_rho_mean"]:.4f}  '
              f'({elapsed:.1f}s)')
        sys.stdout.flush()

    # Summary
    print('\n' + '=' * 70)
    print('Summary')
    print('=' * 70)
    print(f'{"n_gold":<8}{"part_canon":<14}{"part_truth":<14}'
          f'{"rho_mean":<12}{"rho_median":<12}')
    for n_gold in N_GOLD_GRID:
        r = results_per_n[n_gold]
        print(f'{n_gold:<8}'
              f'{r["partition_stability_rate_vs_canonical"]:<14.4f}'
              f'{r["partition_stability_rate_vs_truth_C"]:<14.4f}'
              f'{r["spearman_rho_mean"]:<12.4f}'
              f'{r["spearman_rho_median"]:<12.4f}')

    # Save
    total_time = time.time() - t_total
    out = {
        'description': ('Ĉ estimation robustness under multinomial bootstrap'
                        ' from finite gold set'),
        'config': {
            'K': K,
            'n_gold_grid': N_GOLD_GRID,
            'B_bootstrap': B_BOOT,
            'seed': SEED,
            'asv_threshold': ASV_EPSILON,
            'n_delta': N_DELTA,
            'topologies': RANK_TOPOS,
            'canonical_safe': sorted(SAFE),
            'canonical_fragile': sorted(FRAGILE),
            'empirical_path': EMP_PATH,
        },
        'source_matrices': {
            name: {
                'C': Cs[name].tolist(),
                'diag': np.diag(Cs[name]).tolist(),
                'truth_asv': truth_asv_dict[name],
                'truth_fragile_set': sorted(truth_partition[name]),
                'truth_matches_canonical':
                    truth_partition[name] == FRAGILE,
            }
            for name in Cs
        },
        'results_per_n_gold': {
            str(n): results_per_n[n] for n in N_GOLD_GRID
        },
        'total_time_seconds': total_time,
    }
    with open(OUT_PATH, 'w') as f:
        json.dump(out, f, indent=2)
    print(f'\nJSON saved: {OUT_PATH}')
    print(f'Total: {total_time:.1f}s')


if __name__ == '__main__':
    main()
