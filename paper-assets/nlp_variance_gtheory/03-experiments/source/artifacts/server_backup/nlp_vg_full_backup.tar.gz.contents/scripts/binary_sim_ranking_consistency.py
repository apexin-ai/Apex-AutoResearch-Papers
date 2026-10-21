#!/usr/bin/env python3
"""Binary simulation: top-3 ranking consistency for 8-model MMLU design.

Generates binary data from a probit latent model with variance components
matching the observed MMLU 8-model G-study, then checks how often
Henderson I recovers the observed top-3 ranking.

Key finding: residual is inflated on binary scale (absorbs Bernoulli noise),
so we also evaluate ranking excluding residual.
"""

import json
import numpy as np
from itertools import combinations
from math import prod
from scipy.stats import norm, kendalltau
from pathlib import Path

FACETS = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id"]
N_LEVELS = {
    "model": 8, "temperature": 2, "prompt_template": 6,
    "seed": 6, "ordering": 4, "item_id": 200,
}

OBSERVED_PCT = {
    "item_id": 37.8812,
    "model:item_id": 30.2095,
    "residual": 25.0065,
    "model": 2.8326,
    "model:prompt_template": 1.5944,
    "prompt_template:item_id": 0.9456,
    "temperature:item_id": 0.5568,
    "seed:item_id": 0.5252,
    "ordering:item_id": 0.3122,
    "model:temperature": 0.0438,
    "model:seed": 0.0299,
    "model:ordering": 0.0278,
    "temperature": 0.0203,
    "prompt_template:ordering": 0.0070,
    "temperature:seed": 0.0059,
    "ordering": 0.0007,
    "temperature:prompt_template": 0.0007,
    "temperature:ordering": 0.0,
    "prompt_template:seed": 0.0,
    "seed:ordering": 0.0,
    "prompt_template": 0.0,
    "seed": 0.0,
}

TRUE_VC = {k: v / 100.0 for k, v in OBSERVED_PCT.items()}
s = sum(TRUE_VC.values())
TRUE_VC = {k: v / s for k, v in TRUE_VC.items()}

OBSERVED_TOP3 = ["item_id", "model:item_id", "residual"]
GRAND_MEAN_ACC = 0.645736
N_REPS = 100


def generate_binary(vc, nl, p, rng):
    shape = tuple(nl[f] for f in FACETS)
    nf = len(FACETS)
    lat = np.zeros(shape)
    for i, fi in enumerate(FACETS):
        s2 = vc.get(fi, 0.0)
        if s2 > 0:
            e = rng.randn(shape[i]) * np.sqrt(s2)
            sh = [1] * nf; sh[i] = shape[i]
            lat += e.reshape(sh)
    for i in range(nf):
        for j in range(i + 1, nf):
            key = f"{FACETS[i]}:{FACETS[j]}"
            s2 = vc.get(key, 0.0)
            if s2 > 0:
                e = rng.randn(shape[i], shape[j]) * np.sqrt(s2)
                sh = [1] * nf; sh[i] = shape[i]; sh[j] = shape[j]
                lat += e.reshape(sh)
    lat += rng.randn(*shape) * np.sqrt(vc.get("residual", 0.0))
    mu = norm.ppf(p)
    return (lat + mu > 0).astype(np.float64)


def compute_ss_array(data):
    nf = len(FACETS)
    gm = data.mean()
    N = data.size
    nl = {FACETS[i]: data.shape[i] for i in range(nf)}
    effects = {}
    for i in range(nf):
        ax = tuple(j for j in range(nf) if j != i)
        m = data.mean(axis=ax)
        n_per = N // data.shape[i]
        ss = float(n_per * ((m - gm) ** 2).sum())
        df_eff = data.shape[i] - 1
        effects[FACETS[i]] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff else 0.0}
    for i in range(nf):
        for j in range(i + 1, nf):
            ax = tuple(k for k in range(nf) if k not in (i, j))
            cm = data.mean(axis=ax)
            mi = data.mean(axis=tuple(k for k in range(nf) if k != i))
            mj = data.mean(axis=tuple(k for k in range(nf) if k != j))
            inter = cm - mi[:, None] - mj[None, :] + gm
            n_per = N // (data.shape[i] * data.shape[j])
            ss = float(n_per * (inter ** 2).sum())
            df_eff = (data.shape[i] - 1) * (data.shape[j] - 1)
            effects[f"{FACETS[i]}:{FACETS[j]}"] = {"ss": ss, "df": df_eff, "ms": ss / df_eff if df_eff else 0.0}
    ss_t = float(((data - gm) ** 2).sum())
    ss_m = sum(e["ss"] for e in effects.values())
    ss_r = max(0.0, ss_t - ss_m)
    df_r = N - 1 - sum(e["df"] for e in effects.values())
    effects["residual"] = {"ss": ss_r, "df": df_r, "ms": ss_r / df_r if df_r else 0.0}
    return effects, nl


def estimate_vc(effects, nl):
    ms_res = effects["residual"]["ms"]
    vc = {}
    for fi, fj in combinations(FACETS, 2):
        key = f"{fi}:{fj}"
        coeff = prod(nl[f] for f in FACETS if f not in (fi, fj))
        raw = (effects[key]["ms"] - ms_res) / coeff if coeff > 0 else 0.0
        vc[key] = max(0.0, raw)
    for fi in FACETS:
        coeff_main = prod(nl[f] for f in FACETS if f != fi)
        interaction_contrib = 0.0
        for fj in FACETS:
            if fj == fi:
                continue
            int_key = f"{fi}:{fj}" if f"{fi}:{fj}" in vc else f"{fj}:{fi}"
            coeff_ij = prod(nl[f] for f in FACETS if f not in (fi, fj))
            interaction_contrib += coeff_ij * vc[int_key]
        raw = (effects[fi]["ms"] - interaction_contrib - ms_res) / coeff_main if coeff_main > 0 else 0.0
        vc[fi] = max(0.0, raw)
    vc["residual"] = ms_res
    return vc


def to_pct(vc):
    total = sum(vc.values())
    if total == 0:
        return {k: 0.0 for k in vc}
    return {k: round(v / total * 100, 4) for k, v in vc.items()}


def get_ranking(pct_dict):
    return sorted(pct_dict.keys(), key=lambda k: pct_dict[k], reverse=True)


def run():
    observed_ranking = get_ranking(OBSERVED_PCT)
    observed_top3 = observed_ranking[:3]
    observed_top3_set = set(observed_top3)

    # Observed ranking excluding residual
    obs_no_res = {k: v for k, v in OBSERVED_PCT.items() if k != "residual"}
    observed_top2_no_res = get_ranking(obs_no_res)[:2]

    print(f"Observed top-3: {observed_top3}")
    print(f"Observed top-2 (no residual): {observed_top2_no_res}")
    print(f"Running {N_REPS} binary simulations with p={GRAND_MEAN_ACC:.4f}...")

    per_rep_rankings = []
    per_rep_pcts = []
    top1_match = 0
    top3_exact_match = 0
    top3_set_match = 0
    top2_no_res_exact_match = 0
    top1_no_res_match = 0

    all_comps = list(set(list(OBSERVED_PCT.keys()) + ["residual"]))
    top3_freq = {c: {"rank1": 0, "rank2": 0, "rank3": 0} for c in all_comps}
    top2_no_res_freq = {c: {"rank1": 0, "rank2": 0} for c in all_comps if c != "residual"}

    for rep in range(N_REPS):
        rng = np.random.RandomState(42 + rep)
        data = generate_binary(TRUE_VC, N_LEVELS, GRAND_MEAN_ACC, rng)
        effects, nl = compute_ss_array(data)
        vc = estimate_vc(effects, nl)
        pct = to_pct(vc)

        ranking = get_ranking(pct)
        top3 = ranking[:3]
        per_rep_rankings.append(top3)
        per_rep_pcts.append(pct)

        # Top-3 metrics (including residual)
        if top3[0] == observed_top3[0]:
            top1_match += 1
        if top3 == observed_top3:
            top3_exact_match += 1
        if set(top3) == observed_top3_set:
            top3_set_match += 1

        for rank_idx, comp in enumerate(top3):
            if comp in top3_freq:
                top3_freq[comp][f"rank{rank_idx + 1}"] += 1

        # Non-residual metrics
        pct_no_res = {k: v for k, v in pct.items() if k != "residual"}
        ranking_no_res = get_ranking(pct_no_res)
        top2_nr = ranking_no_res[:2]
        if top2_nr[0] == observed_top2_no_res[0]:
            top1_no_res_match += 1
        if top2_nr == observed_top2_no_res:
            top2_no_res_exact_match += 1
        for rank_idx, comp in enumerate(top2_nr):
            if comp in top2_no_res_freq:
                top2_no_res_freq[comp][f"rank{rank_idx + 1}"] += 1

        if (rep + 1) % 20 == 0:
            print(f"  Rep {rep+1}/{N_REPS}: top3={top3}, "
                  f"top2_nr={top2_nr}, "
                  f"pct=[{pct.get(top3[0],0):.1f}, {pct.get(top3[1],0):.1f}, {pct.get(top3[2],0):.1f}]")

    # Kendall's tau (full ranking)
    obs_rank_order = {c: i for i, c in enumerate(observed_ranking)}
    taus_full = []
    taus_no_res = []
    obs_no_res_ranking = get_ranking(obs_no_res)
    obs_nr_order = {c: i for i, c in enumerate(obs_no_res_ranking)}
    for pct in per_rep_pcts:
        sim_ranking = get_ranking(pct)
        sim_order = {c: i for i, c in enumerate(sim_ranking)}
        shared = [c for c in obs_rank_order if c in sim_order]
        tau, _ = kendalltau([obs_rank_order[c] for c in shared],
                            [sim_order[c] for c in shared])
        taus_full.append(tau)

        pct_nr = {k: v for k, v in pct.items() if k != "residual"}
        sim_nr_ranking = get_ranking(pct_nr)
        sim_nr_order = {c: i for i, c in enumerate(sim_nr_ranking)}
        shared_nr = [c for c in obs_nr_order if c in sim_nr_order]
        tau_nr, _ = kendalltau([obs_nr_order[c] for c in shared_nr],
                               [sim_nr_order[c] for c in shared_nr])
        taus_no_res.append(tau_nr)

    active_top3 = {k: v for k, v in top3_freq.items()
                   if v["rank1"] + v["rank2"] + v["rank3"] > 0}
    active_top2_nr = {k: v for k, v in top2_no_res_freq.items()
                      if v["rank1"] + v["rank2"] > 0}

    # Mean pct across reps
    mean_pcts = {}
    for comp in per_rep_pcts[0]:
        vals = [p[comp] for p in per_rep_pcts]
        mean_pcts[comp] = {
            "mean": round(float(np.mean(vals)), 2),
            "std": round(float(np.std(vals)), 2),
        }

    results = {
        "observed_top3": observed_top3,
        "observed_top3_pct": [round(OBSERVED_PCT[c], 2) for c in observed_top3],
        "n_simulations": N_REPS,
        "grand_mean_accuracy": GRAND_MEAN_ACC,
        "design": N_LEVELS,
        "with_residual": {
            "exact_top3_match_pct": round(top3_exact_match / N_REPS * 100, 1),
            "top3_set_match_pct": round(top3_set_match / N_REPS * 100, 1),
            "top1_match_pct": round(top1_match / N_REPS * 100, 1),
            "kendall_tau_mean": round(float(np.mean(taus_full)), 4),
            "kendall_tau_std": round(float(np.std(taus_full)), 4),
            "note": "Residual inflated on binary scale (absorbs Bernoulli within-cell noise)"
        },
        "excluding_residual": {
            "observed_top2": observed_top2_no_res,
            "exact_top2_match_pct": round(top2_no_res_exact_match / N_REPS * 100, 1),
            "top1_match_pct": round(top1_no_res_match / N_REPS * 100, 1),
            "kendall_tau_mean": round(float(np.mean(taus_no_res)), 4),
            "kendall_tau_std": round(float(np.std(taus_no_res)), 4),
            "note": "Systematic component ranking (excluding Bernoulli-inflated residual)"
        },
        "top3_components_frequency": active_top3,
        "top2_no_residual_frequency": active_top2_nr,
        "mean_pct_across_sims": {k: v for k, v in sorted(mean_pcts.items(), key=lambda x: -x[1]["mean"])},
        "per_rep_top3": per_rep_rankings,
    }

    out = Path("results/exp004_8model_analysis/binary_sim_ranking_consistency.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n{'='*60}")
    print(f"=== With residual ===")
    print(f"  Top-1 match: {results['with_residual']['top1_match_pct']}%")
    print(f"  Exact top-3 match: {results['with_residual']['exact_top3_match_pct']}%")
    print(f"  Top-3 set match: {results['with_residual']['top3_set_match_pct']}%")
    print(f"  Kendall tau: {results['with_residual']['kendall_tau_mean']:.4f} +/- {results['with_residual']['kendall_tau_std']:.4f}")
    print(f"\n=== Excluding residual ===")
    print(f"  Top-1 (no res) match: {results['excluding_residual']['top1_match_pct']}%")
    print(f"  Exact top-2 (no res) match: {results['excluding_residual']['exact_top2_match_pct']}%")
    print(f"  Kendall tau (no res): {results['excluding_residual']['kendall_tau_mean']:.4f} +/- {results['excluding_residual']['kendall_tau_std']:.4f}")
    print(f"\nTop-3 frequency (with residual):")
    for comp, freq in sorted(active_top3.items(), key=lambda x: -(x[1]["rank1"]+x[1]["rank2"]+x[1]["rank3"])):
        total = freq["rank1"] + freq["rank2"] + freq["rank3"]
        print(f"  {comp:25s}: R1={freq['rank1']:3d}  R2={freq['rank2']:3d}  R3={freq['rank3']:3d}  (total={total})")
    print(f"\nTop-2 frequency (no residual):")
    for comp, freq in sorted(active_top2_nr.items(), key=lambda x: -(x[1]["rank1"]+x[1]["rank2"])):
        total = freq["rank1"] + freq["rank2"]
        print(f"  {comp:25s}: R1={freq['rank1']:3d}  R2={freq['rank2']:3d}  (total={total})")
    print(f"\nMean pct (top-5):")
    for comp, v in sorted(mean_pcts.items(), key=lambda x: -x[1]["mean"])[:5]:
        obs = OBSERVED_PCT.get(comp, 0)
        print(f"  {comp:25s}: sim={v['mean']:5.1f}% +/- {v['std']:4.1f}%   obs={obs:.1f}%")
    print(f"\nSaved to {out}")


if __name__ == "__main__":
    run()
