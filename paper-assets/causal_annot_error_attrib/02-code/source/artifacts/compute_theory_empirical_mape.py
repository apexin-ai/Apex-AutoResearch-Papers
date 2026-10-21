"""Compute Theory-Empirical MAPE.

Compare analytical plim bias (theory, from plan_006 precomputed stats)
against MC empirical bias (sample-level OLS averaged over N_mc draws).

Scope: 8 valid humaid configs (K=10) x 7 topologies = 56 scenarios.
       VAST (K=3) and civil_comments (K=2) confusion matrices are not in
       the local asv_empirical_results.json.
"""

import json
import sys
import numpy as np
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, '/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib')

# Import plan_006's DGP + plim machinery directly (since they support arbitrary K)
import importlib.util
spec = importlib.util.spec_from_file_location(
    "plan_006",
    "/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib/plan_006_asv_empirical.py"
)
plan_006 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(plan_006)

GEN_FNS = plan_006.GEN_FNS
make_dgp_params = plan_006.make_dgp_params
precompute_suff_stats = plan_006.precompute_suff_stats
compute_plim = plan_006.compute_plim
extract_tau = plan_006.extract_tau
ols_with_dummies = plan_006.ols_with_dummies
ols_no_T = plan_006.ols_no_T
wald_estimator = plan_006.wald_estimator
generate_Astar = plan_006.generate_Astar

TOPOLOGIES = ['confounding', 'mediation', 'collider', 'exposure',
              'mbias', 'iv', 'frontdoor']
HAS_TREATMENT = {'confounding', 'mediation', 'collider', 'mbias', 'frontdoor'}

N_MC = 200
N_SAMPLES = 10_000

ROOT = Path('/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib')
INPUT_JSON = ROOT / 'artifacts/plan006/asv_empirical_results.json'
FILTER_JSON = ROOT / 'artifacts/plan006_full_filtered_stats.json'
OUTPUT_JSON = ROOT / 'artifacts/theory_empirical_mape.json'


def mc_tau_hat(C, K, topology, params, n_samples, seed):
    """Single MC replicate: generate, misclassify, regress, return tau_hat."""
    rng = np.random.default_rng(seed)
    first_var, Y, A = GEN_FNS[topology](K, n_samples, params, rng)
    A_star = generate_Astar(A, C, rng)

    if topology == 'iv':
        Z = first_var
        W, _ = wald_estimator(Z, Y, A_star, k=1)
        return W
    elif topology == 'exposure':
        beta, _ = ols_no_T(Y, A_star, K)
        return beta[1] if len(beta) > 1 else np.nan
    else:
        T = first_var
        beta, _ = ols_with_dummies(Y, T, A_star, K)
        return beta[1]


def run_mc_block(C, K, topology, params, n_mc, n_samples, base_seed):
    """Return list of tau_hat values across n_mc seeds."""
    out = []
    for i in range(n_mc):
        try:
            tau = mc_tau_hat(C, K, topology, params, n_samples,
                             base_seed + i * 7919)
            if np.isfinite(tau):
                out.append(float(tau))
        except Exception:
            continue
    return out


def main():
    print(f"Loading {INPUT_JSON}")
    data = json.loads(INPUT_JSON.read_text())
    filter_data = json.loads(FILTER_JSON.read_text())
    zero_configs = set(filter_data['zero_configs'])

    confusion_matrices = {k: np.array(v) for k, v in data['confusion_matrices'].items()}
    bias_records = data['biases']

    # Build lookup: (config_key, topology) -> theory bias record
    theory_lookup = {}
    for b in bias_records:
        ck = f"{b['dataset']}_{b['model']}_{b['prompt']}"
        theory_lookup[(ck, b['topology'])] = b

    # Precompute params + tau_true per K (only K=10 here)
    Ks_used = sorted(set(int(b['K']) for b in bias_records))
    params_by_K = {K: make_dgp_params(K) for K in Ks_used}

    print(f"Precomputing suff stats for K={Ks_used} x {len(TOPOLOGIES)} topologies...")
    all_st = {}
    all_tau_true = {}
    for K in Ks_used:
        for topo in TOPOLOGIES:
            st = precompute_suff_stats(K, topo, params_by_K[K][topo])
            all_st[(K, topo)] = st
            plim_I = compute_plim(np.eye(K), st, K)
            all_tau_true[(K, topo)] = extract_tau(plim_I, topo)
            print(f"  K={K} {topo:<12} tau_true={all_tau_true[(K, topo)]:.6f}")

    # Iterate configs (skip zero matrices)
    per_config = {}
    per_topology = defaultdict(list)
    grand_records = []

    valid_configs = [k for k in confusion_matrices if k not in zero_configs]
    print(f"\n{len(valid_configs)} valid configs (skipped {len(confusion_matrices) - len(valid_configs)} zero)")

    for config_key in valid_configs:
        C = confusion_matrices[config_key]
        K = C.shape[0]
        params = params_by_K[K]
        per_config[config_key] = {}
        print(f"\n[{config_key}] K={K}")

        for topo in TOPOLOGIES:
            rec = theory_lookup.get((config_key, topo))
            if rec is None or rec.get('bias') is None:
                continue

            theory_bias = float(rec['bias'])
            tau_true = all_tau_true[(K, topo)]

            tau_hats = run_mc_block(
                C, K, topo, params[topo],
                N_MC, N_SAMPLES, base_seed=hash(config_key + topo) & 0xFFFFFFFF
            )
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
                'theory_bias': theory_bias,
                'mc_bias': float(mc_bias),
                'mc_tau_mean': tau_mean,
                'mc_tau_se': tau_se,
                'tau_true': float(tau_true),
                'abs_pct_error': float(ape) if np.isfinite(ape) else None,
                'n_mc_used': len(tau_hats),
            }
            per_config[config_key][topo] = entry
            per_topology[topo].append(ape)
            if np.isfinite(ape):
                grand_records.append(ape)
            print(f"  {topo:<12} theory={theory_bias:+.5f}  MC={mc_bias:+.5f}  APE={ape:.3%}")

    # Aggregate
    per_topology_summary = {}
    for topo, apes in per_topology.items():
        finite = [a for a in apes if np.isfinite(a)]
        per_topology_summary[topo] = {
            'mape': float(np.mean(finite)) if finite else None,
            'median_ape': float(np.median(finite)) if finite else None,
            'max_ape': float(np.max(finite)) if finite else None,
            'n_scenarios': len(finite),
        }

    grand_mape = float(np.mean(grand_records)) if grand_records else None

    output = {
        'meta': {
            'n_mc': N_MC,
            'n_samples': N_SAMPLES,
            'scope': 'humaid only (K=10); VAST and civil_comments confusion matrices not in local JSON',
            'n_valid_configs': len(valid_configs),
            'n_scenarios_total': len(grand_records),
            'topologies': TOPOLOGIES,
            'source_input': str(INPUT_JSON),
        },
        'grand_mape': grand_mape,
        'per_topology': per_topology_summary,
        'per_config': per_config,
        'note': (
            "Theory bias = analytical plim - tau_true (from plan_006 sufficient-stat "
            "approach with N=2M). MC bias = mean(tau_hat) - tau_true over N_mc OLS/Wald "
            "replicates at N=10k. APE = |theory - mc| / |theory|. Sign-flip safety is "
            "preserved across all scenarios in this set."
        ),
    }

    OUTPUT_JSON.write_text(json.dumps(output, indent=2))
    print(f"\n=== Written {OUTPUT_JSON} ===")
    print(f"Grand MAPE: {grand_mape:.3%}" if grand_mape else "Grand MAPE: N/A")
    print("\nPer-topology MAPE:")
    for topo, s in per_topology_summary.items():
        if s['mape'] is not None:
            print(f"  {topo:<12} MAPE={s['mape']:.3%}  median={s['median_ape']:.3%}  "
                  f"max={s['max_ape']:.3%}  n={s['n_scenarios']}")


if __name__ == "__main__":
    main()
