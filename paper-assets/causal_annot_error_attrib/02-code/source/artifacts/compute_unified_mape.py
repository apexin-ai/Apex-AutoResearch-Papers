#!/usr/bin/env python3
"""
Recompute Theory-Empirical MAPE using all 23 configs from updated_empirical_results.json.
Unifies the dataset with the Empirical Validation section (same 23 configs).
"""
import json
import sys
import time
import numpy as np
from pathlib import Path
from collections import defaultdict

PROJ = Path("/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib")
sys.path.insert(0, str(PROJ))

import importlib.util
spec = importlib.util.spec_from_file_location(
    "plan_006", str(PROJ / "plan_006_asv_empirical.py"))
plan_006 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plan_006)

TOPOLOGIES = ['confounding', 'mediation', 'collider', 'exposure',
              'mbias', 'iv', 'frontdoor']

def main():
    t0 = time.time()

    with open(PROJ / "artifacts/updated_empirical_results.json") as f:
        emp = json.load(f)

    all_cms = {k: np.array(v) for k, v in emp["confusion_matrices"].items()}
    print(f"Loaded {len(all_cms)} confusion matrices from updated_empirical_results.json")

    config_meta = {}
    for k, C in all_cms.items():
        if k.startswith("civil_comments_"):
            dataset = "civil_comments"
        elif k.startswith("vast_"):
            dataset = "vast"
        else:
            dataset = "humaid"
        K = C.shape[0]
        config_meta[k] = {
            "dataset": dataset,
            "K": K,
            "min_diag": float(np.min(np.diag(C))),
            "trace": float(np.trace(C)),
            "macro_recall": float(np.trace(C) / K),
        }

    N_MC = 200
    N_SAMPLES = 10_000

    Ks_used = sorted(set(m["K"] for m in config_meta.values()))
    params_by_K = {K: plan_006.make_dgp_params(K) for K in Ks_used}
    suff_stats = {}
    tau_true_cache = {}

    for K in Ks_used:
        for topo in TOPOLOGIES:
            st = plan_006.precompute_suff_stats(K, topo, params_by_K[K][topo])
            suff_stats[(K, topo)] = st
            plim_I = plan_006.compute_plim(np.eye(K), st, K)
            tau_true_cache[(K, topo)] = plan_006.extract_tau(plim_I, topo)
            print(f"  K={K:>2} {topo:<12} tau_true={tau_true_cache[(K, topo)]:.6f}")

    per_config = {}
    per_topology = defaultdict(list)
    grand_records = []

    for config_key, C in sorted(all_cms.items()):
        meta = config_meta[config_key]
        K = meta["K"]
        params = params_by_K[K]
        per_config[config_key] = {}
        print(f"\n[{config_key}] K={K}, min_diag={meta['min_diag']:.4f}")

        for topo in TOPOLOGIES:
            tau_true = tau_true_cache[(K, topo)]
            st = suff_stats[(K, topo)]

            plim_C = plan_006.compute_plim(C, st, K)
            tau_biased = plan_006.extract_tau(plim_C, topo)
            if not np.isfinite(tau_biased) or not np.isfinite(tau_true):
                continue
            theory_bias = tau_biased - tau_true

            tau_hats = []
            for mc_i in range(N_MC):
                seed = (hash(config_key + topo) & 0xFFFFFFFF) + mc_i * 7919
                try:
                    rng = np.random.default_rng(seed)
                    first_var, Y, A = plan_006.GEN_FNS[topo](K, N_SAMPLES,
                                                              params[topo], rng)
                    A_star = plan_006.generate_Astar(A, C, rng)

                    if topo == 'iv':
                        Z = first_var
                        W, _ = plan_006.wald_estimator(Z, Y, A_star, k=1)
                        if np.isfinite(W):
                            tau_hats.append(float(W))
                    elif topo == 'exposure':
                        beta, _ = plan_006.ols_no_T(Y, A_star, K)
                        if len(beta) > 1 and np.isfinite(beta[1]):
                            tau_hats.append(float(beta[1]))
                    else:
                        T = first_var
                        beta, _ = plan_006.ols_with_dummies(Y, T, A_star, K)
                        if np.isfinite(beta[1]):
                            tau_hats.append(float(beta[1]))
                except Exception:
                    continue

            if len(tau_hats) < N_MC // 2:
                print(f"  {topo:<12} MC FAILED ({len(tau_hats)}/{N_MC})")
                continue

            tau_mean = float(np.mean(tau_hats))
            tau_se = float(np.std(tau_hats, ddof=1) / np.sqrt(len(tau_hats)))
            mc_bias = tau_mean - tau_true

            if abs(theory_bias) > 1e-12:
                ape = abs(theory_bias - mc_bias) / abs(theory_bias)
            else:
                ape = float('nan')

            entry = {
                'theory_bias': float(theory_bias),
                'mc_bias': float(mc_bias),
                'mc_tau_mean': tau_mean,
                'mc_tau_se': tau_se,
                'tau_true': float(tau_true),
                'tau_biased_plim': float(tau_biased),
                'abs_pct_error': float(ape) if np.isfinite(ape) else None,
                'n_mc_used': len(tau_hats),
            }
            per_config[config_key][topo] = entry
            if np.isfinite(ape):
                per_topology[topo].append(ape)
                grand_records.append(ape)
            print(f"  {topo:<12} theory={theory_bias:+.5f}  MC={mc_bias:+.5f}  "
                  f"APE={ape:.3%}")

    per_topology_summary = {}
    for topo in TOPOLOGIES:
        apes = per_topology.get(topo, [])
        finite = [a for a in apes if np.isfinite(a)]
        per_topology_summary[topo] = {
            'mape': float(np.mean(finite)) if finite else None,
            'median_ape': float(np.median(finite)) if finite else None,
            'max_ape': float(np.max(finite)) if finite else None,
            'n': len(finite),
        }

    grand_mape = float(np.mean(grand_records)) if grand_records else None

    output = {
        'meta': {
            'n_mc': N_MC,
            'n_samples': N_SAMPLES,
            'scope': f'All {len(all_cms)} configs from updated_empirical_results.json (K=2,3,10)',
            'n_valid_configs': len(all_cms),
            'n_scenarios_total': len(grand_records),
            'topologies': TOPOLOGIES,
            'note': 'Unified with Empirical Validation section (same 23 configs).',
        },
        'grand_mape': grand_mape,
        'per_topology': per_topology_summary,
        'per_config': per_config,
    }

    out_path = PROJ / "artifacts/theory_empirical_mape.json"
    out_path.write_text(json.dumps(output, indent=2))
    print(f"\n{'='*60}")
    print(f"DONE in {time.time()-t0:.1f}s")
    print(f"Grand MAPE: {grand_mape:.4%}" if grand_mape else "Grand MAPE: N/A")
    print(f"Configs: {len(all_cms)}, Scenarios: {len(grand_records)}")
    print(f"Written: {out_path}")

    print(f"\nPer-topology MAPE:")
    for topo in TOPOLOGIES:
        s = per_topology_summary[topo]
        if s['mape'] is not None:
            print(f"  {topo:<12} MAPE={100*s['mape']:.2f}%  median={100*s['median_ape']:.2f}%  "
                  f"max={100*s['max_ape']:.2f}%  n={s['n']}")

    high_ape = [(k, t, e['abs_pct_error'])
                for k, topos in per_config.items()
                for t, e in topos.items()
                if e.get('abs_pct_error') is not None and e['abs_pct_error'] > 0.10]
    if high_ape:
        print(f"\n⚠️ Configs with APE > 10%:")
        for k, t, ape in sorted(high_ape, key=lambda x: -x[2]):
            print(f"  {k} / {t}: {100*ape:.1f}%")


if __name__ == "__main__":
    main()
