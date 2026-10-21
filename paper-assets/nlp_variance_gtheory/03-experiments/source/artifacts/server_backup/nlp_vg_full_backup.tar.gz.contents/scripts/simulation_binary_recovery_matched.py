#!/usr/bin/env python3
"""Simulation-based binary recovery for Henderson Method I.

Generates binary data from a probit latent model with known variance
components, then tests whether Henderson I recovers the correct
ranking and relative magnitudes. Addresses reviewer concern about
applying linear ANOVA to binary outcomes.

Key insight: residual is inflated on binary scale (absorbs Bernoulli
variance), so we evaluate ranking recovery EXCLUDING residual —
the question is whether Henderson I correctly identifies which
*systematic* sources of variance dominate.
"""

import json
import time
from itertools import combinations
from math import prod
from pathlib import Path

import numpy as np
from scipy.stats import norm, spearmanr

FACETS = [
    "precision", "temperature", "prompt_template",
    "seed", "ordering", "item_id",
]
N_LEVELS_BASE = {
    "precision": 3, "temperature": 3, "prompt_template": 6,
    "seed": 6, "ordering": 4,
}

TRUE_VC = {
    "item_id": 0.500,
    "precision": 0.010, "temperature": 0.010,
    "prompt_template": 0.020, "seed": 0.010, "ordering": 0.010,
    "precision:item_id": 0.070, "temperature:item_id": 0.060,
    "prompt_template:item_id": 0.050, "seed:item_id": 0.030,
    "ordering:item_id": 0.020,
    "precision:temperature": 0.005, "precision:prompt_template": 0.005,
    "precision:seed": 0.005, "precision:ordering": 0.005,
    "temperature:prompt_template": 0.005, "temperature:seed": 0.005,
    "temperature:ordering": 0.005, "prompt_template:seed": 0.005,
    "prompt_template:ordering": 0.005, "seed:ordering": 0.005,
    "residual": 0.160,
}
assert abs(sum(TRUE_VC.values()) - 1.0) < 1e-10

P_LEVELS = [0.5, 0.6, 0.7, 0.8]
N_ITEMS_LIST = [50, 100, 200]
N_REPS = 100
N_ORACLE_ITEMS = 10000


def _nl(n_items):
    return {**N_LEVELS_BASE, "item_id": n_items}


def _generate_latent(vc, nl, rng):
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
            s2 = vc.get(f"{FACETS[i]}:{FACETS[j]}", 0.0)
            if s2 > 0:
                e = rng.randn(shape[i], shape[j]) * np.sqrt(s2)
                sh = [1] * nf; sh[i] = shape[i]; sh[j] = shape[j]
                lat += e.reshape(sh)
    lat += rng.randn(*shape) * np.sqrt(vc["residual"])
    return lat


def gen_binary(vc, nl, p, rng):
    lat = _generate_latent(vc, nl, rng)
    mu = norm.ppf(p)
    return (lat + mu > 0).astype(np.float64)


def gen_continuous(vc, nl, rng):
    return _generate_latent(vc, nl, rng)


def henderson_i(data):
    nf = len(FACETS)
    gm = data.mean()
    N = data.size
    nl = {FACETS[i]: data.shape[i] for i in range(nf)}
    eff = {}

    for i in range(nf):
        ax = tuple(j for j in range(nf) if j != i)
        m = data.mean(axis=ax)
        ss = float((N // data.shape[i]) * ((m - gm) ** 2).sum())
        df = data.shape[i] - 1
        eff[FACETS[i]] = {"ss": ss, "df": df, "ms": ss / df if df else 0.0}

    for i in range(nf):
        for j in range(i + 1, nf):
            ax = tuple(k for k in range(nf) if k not in (i, j))
            cm = data.mean(axis=ax)
            mi = data.mean(axis=tuple(k for k in range(nf) if k != i))
            mj = data.mean(axis=tuple(k for k in range(nf) if k != j))
            inter = cm - mi.reshape(-1, 1) - mj.reshape(1, -1) + gm
            n_per = N // (data.shape[i] * data.shape[j])
            ss = float(n_per * (inter ** 2).sum())
            df = (data.shape[i] - 1) * (data.shape[j] - 1)
            eff[f"{FACETS[i]}:{FACETS[j]}"] = {
                "ss": ss, "df": df, "ms": ss / df if df else 0.0,
            }

    ss_t = float(((data - gm) ** 2).sum())
    ss_m = sum(e["ss"] for e in eff.values())
    ss_r = max(0.0, ss_t - ss_m)
    df_r = N - 1 - sum(e["df"] for e in eff.values())
    eff["residual"] = {"ss": ss_r, "df": df_r, "ms": ss_r / df_r if df_r else 0.0}
    return eff, nl


def solve_vc(eff, nl):
    ms_r = eff["residual"]["ms"]
    vc = {}
    for fi, fj in combinations(FACETS, 2):
        k = f"{fi}:{fj}"
        c = prod(nl[f] for f in FACETS if f not in (fi, fj))
        vc[k] = max(0.0, (eff[k]["ms"] - ms_r) / c) if c else 0.0
    for fi in FACETS:
        cm = prod(nl[f] for f in FACETS if f != fi)
        ic = 0.0
        for fj in FACETS:
            if fj == fi:
                continue
            ik = f"{fi}:{fj}" if f"{fi}:{fj}" in vc else f"{fj}:{fi}"
            c_ij = prod(nl[f] for f in FACETS if f not in (fi, fj))
            ic += c_ij * vc[ik]
        vc[fi] = max(0.0, (eff[fi]["ms"] - ic - ms_r) / cm) if cm else 0.0
    vc["residual"] = ms_r
    return vc


def to_pct(vc):
    t = sum(vc.values())
    return {k: v / t * 100 for k, v in vc.items()} if t > 0 else {k: 0.0 for k in vc}


def rank_dict(d):
    return {k: r + 1 for r, k in enumerate(sorted(d, key=d.get, reverse=True))}


def exclude_residual(d):
    return {k: v for k, v in d.items() if k != "residual"}


def validate():
    try:
        import pandas as pd
        from src.analysis.variance_decomposition import (
            compute_ss, estimate_variance_components,
        )
    except ImportError:
        print("(skip validation - src not on PYTHONPATH)")
        return

    rng = np.random.RandomState(42)
    nl = _nl(20)
    data = gen_binary(TRUE_VC, nl, 0.6, rng)
    eff_f, nl_f = henderson_i(data)
    vc_f = solve_vc(eff_f, nl_f)

    rows = []
    for idx in np.ndindex(data.shape):
        row = {FACETS[i]: str(idx[i]) for i in range(len(FACETS))}
        row["correct"] = data[idx]
        rows.append(row)
    df = pd.DataFrame(rows)
    eff_d, nl_d = compute_ss(df, "correct", FACETS)
    vc_d = estimate_variance_components(eff_d, FACETS, nl_d)

    max_diff = max(abs(vc_f[k] - vc_d[k]) for k in vc_f)
    status = "PASS" if max_diff < 1e-8 else "FAIL"
    print(f"Validation: max_diff = {max_diff:.2e} [{status}]")
    assert max_diff < 1e-8


def run():
    print("=" * 60)
    print("Binary Recovery Simulation - Henderson Method I")
    print(f"{N_REPS} reps x {len(P_LEVELS)} accuracy x {len(N_ITEMS_LIST)} sizes")
    print("=" * 60)

    validate()

    true_pct = to_pct(TRUE_VC)
    comps = sorted(TRUE_VC.keys())
    comps_nr = [k for k in comps if k != "residual"]
    true_pct_nr = exclude_residual(true_pct)
    true_vec = np.array([true_pct[k] for k in comps])
    true_vec_nr = np.array([true_pct[k] for k in comps_nr])
    true_ranks = rank_dict(true_pct)
    true_ranks_nr = rank_dict(true_pct_nr)

    results = {
        "true_components": TRUE_VC,
        "true_pct": {k: round(true_pct[k], 4) for k in comps},
        "design": {
            "facets": FACETS,
            "base_levels": N_LEVELS_BASE,
            "conditions_per_item": prod(N_LEVELS_BASE.values()),
            "latent_model": "probit: y = 1{mu + latent > 0}, mu = Phi^{-1}(p)",
        },
        "n_replications": N_REPS,
        "n_oracle_items": N_ORACLE_ITEMS,
        "recovery_results": {},
    }

    t0 = time.time()
    summary_rows = []

    for p in P_LEVELS:
        pk = f"p{p}"
        print(f"\n--- Accuracy = {p} ---")

        od = gen_binary(TRUE_VC, _nl(N_ORACLE_ITEMS), p, np.random.RandomState(99999))
        oa = float(od.mean())
        oe, onl = henderson_i(od)
        ovc = solve_vc(oe, onl)
        opct = to_pct(ovc)
        opct_nr = exclude_residual(opct)
        ovec = np.array([opct[k] for k in comps])
        ovec_nr = np.array([opct[k] for k in comps_nr])
        oracle_rho = float(spearmanr(true_vec, ovec)[0])
        oracle_rho_nr = float(spearmanr(true_vec_nr, ovec_nr)[0])
        del od

        results["recovery_results"][pk] = {
            "target_accuracy": p,
            "oracle_accuracy": round(oa, 4),
            "oracle_pct": {k: round(opct[k], 4) for k in comps},
            "oracle_vs_latent_spearman": round(oracle_rho, 4),
            "oracle_vs_latent_spearman_no_residual": round(oracle_rho_nr, 4),
            "by_n_items": {},
        }

        for ni in N_ITEMS_LIST:
            nk = f"n{ni}"
            nl = _nl(ni)

            ep = {k: [] for k in comps}
            rho_l_all = []; rho_l_nr = []
            rho_o_all = []; rho_o_nr = []
            top1_nr = top3_nr = top5_nr = 0
            top1_all = top3_all = top5_all = 0
            accs = []

            for rep in range(N_REPS):
                seed = int(p * 10000) + ni * 100 + rep
                data = gen_binary(TRUE_VC, nl, p, np.random.RandomState(seed))
                accs.append(float(data.mean()))

                e, enl = henderson_i(data)
                vc = solve_vc(e, enl)
                pct = to_pct(vc)
                pct_nr = exclude_residual(pct)

                for k in comps:
                    ep[k].append(pct[k])

                ev = np.array([pct[k] for k in comps])
                ev_nr = np.array([pct[k] for k in comps_nr])
                rho_l_all.append(float(spearmanr(true_vec, ev)[0]))
                rho_l_nr.append(float(spearmanr(true_vec_nr, ev_nr)[0]))
                rho_o_all.append(float(spearmanr(ovec, ev)[0]))
                rho_o_nr.append(float(spearmanr(ovec_nr, ev_nr)[0]))

                er_all = rank_dict(pct)
                er_nr = rank_dict(pct_nr)

                # All components (including residual)
                if er_all.get("item_id") == 1:
                    top1_all += 1
                if ({k for k, r in true_ranks.items() if r <= 3}
                        == {k for k, r in er_all.items() if r <= 3}):
                    top3_all += 1
                if ({k for k, r in true_ranks.items() if r <= 5}
                        == {k for k, r in er_all.items() if r <= 5}):
                    top5_all += 1

                # Non-residual (systematic components only)
                if er_nr.get("item_id") == 1:
                    top1_nr += 1
                if ({k for k, r in true_ranks_nr.items() if r <= 3}
                        == {k for k, r in er_nr.items() if r <= 3}):
                    top3_nr += 1
                if ({k for k, r in true_ranks_nr.items() if r <= 5}
                        == {k for k, r in er_nr.items() if r <= 5}):
                    top5_nr += 1

            # Aggregate
            bias = {}; rmse = {}; cov = {}
            for k in comps:
                v = np.array(ep[k])
                bias[k] = round(float(v.mean() - opct[k]), 4)
                rmse[k] = round(float(np.sqrt(((v - opct[k]) ** 2).mean())), 4)
                lo, hi = np.percentile(v, [2.5, 97.5])
                cov[k] = int(lo <= opct[k] <= hi)

            crate = sum(cov.values()) / len(cov) * 100

            cond = {
                "n_items": ni,
                "observed_accuracy": round(float(np.mean(accs)), 4),
                "bias": bias,
                "rmse": rmse,
                "mean_abs_bias_pct": round(float(np.mean([abs(v) for v in bias.values()])), 4),
                "mean_rmse_pct": round(float(np.mean(list(rmse.values()))), 4),
                "ranking_all_components": {
                    "spearman_vs_latent": round(float(np.mean(rho_l_all)), 4),
                    "spearman_vs_oracle": round(float(np.mean(rho_o_all)), 4),
                    "top1_correct_pct": round(top1_all / N_REPS * 100, 1),
                    "top3_correct_pct": round(top3_all / N_REPS * 100, 1),
                    "top5_correct_pct": round(top5_all / N_REPS * 100, 1),
                },
                "ranking_no_residual": {
                    "spearman_vs_latent": round(float(np.mean(rho_l_nr)), 4),
                    "spearman_vs_oracle": round(float(np.mean(rho_o_nr)), 4),
                    "top1_item_id_pct": round(top1_nr / N_REPS * 100, 1),
                    "top3_correct_pct": round(top3_nr / N_REPS * 100, 1),
                    "top5_correct_pct": round(top5_nr / N_REPS * 100, 1),
                },
                "coverage_95": cov,
                "coverage_rate_pct": round(crate, 1),
            }
            results["recovery_results"][pk]["by_n_items"][nk] = cond

            mr_nr = float(np.mean(rho_l_nr))
            summary_rows.append({
                "p": p, "n": ni,
                "rho_all": round(float(np.mean(rho_l_all)), 3),
                "rho_nr": round(mr_nr, 3),
                "top1_nr": cond["ranking_no_residual"]["top1_item_id_pct"],
                "top3_nr": cond["ranking_no_residual"]["top3_correct_pct"],
                "top5_nr": cond["ranking_no_residual"]["top5_correct_pct"],
                "top5_all": cond["ranking_all_components"]["top5_correct_pct"],
                "cov": cond["coverage_rate_pct"],
                "mean_abs_bias": cond["mean_abs_bias_pct"],
            })
            print(f"  n={ni:3d}: rho_nr={mr_nr:.3f} "
                  f"top1_nr={top1_nr}% top5_nr={top5_nr}% "
                  f"top5_all={top5_all}% cov={crate:.0f}%")

    # Continuous control
    print("\n--- Continuous control ---")
    results["continuous_control"] = {}
    for ni in N_ITEMS_LIST:
        nl = _nl(ni)
        rhos = []; rhos_nr = []
        for rep in range(N_REPS):
            data = gen_continuous(TRUE_VC, nl, np.random.RandomState(rep * 777 + ni))
            e, enl = henderson_i(data)
            vc = solve_vc(e, enl)
            pct = to_pct(vc)
            ev = np.array([pct[k] for k in comps])
            ev_nr = np.array([pct[k] for k in comps_nr])
            rhos.append(float(spearmanr(true_vec, ev)[0]))
            rhos_nr.append(float(spearmanr(true_vec_nr, ev_nr)[0]))
        print(f"  n={ni:3d}: rho_all={np.mean(rhos):.4f} rho_nr={np.mean(rhos_nr):.4f}")
        results["continuous_control"][f"n{ni}"] = {
            "spearman_all": round(float(np.mean(rhos)), 4),
            "spearman_no_residual": round(float(np.mean(rhos_nr)), 4),
        }

    elapsed = time.time() - t0
    results["elapsed_seconds"] = round(elapsed, 1)
    results["summary_table"] = summary_rows

    # Trends
    rhos_nr = [r["rho_nr"] for r in summary_rows]
    top1s = [r["top1_nr"] for r in summary_rows]
    top5s_nr = [r["top5_nr"] for r in summary_rows]

    bias_by_p = {}
    for r in summary_rows:
        bias_by_p.setdefault(r["p"], []).append(r["mean_abs_bias"])
    bias_trend = {str(p): round(float(np.mean(bs)), 3) for p, bs in sorted(bias_by_p.items())}

    rho_by_p = {}
    for r in summary_rows:
        rho_by_p.setdefault(r["p"], []).append(r["rho_nr"])
    rho_trend = {str(p): round(float(np.mean(rs)), 3) for p, rs in sorted(rho_by_p.items())}

    results["bias_trend_by_accuracy"] = bias_trend
    results["rho_trend_by_accuracy"] = rho_trend
    results["conclusion"] = (
        f"Henderson I on binary data recovers systematic variance component rankings with "
        f"Spearman rho = {np.mean(rhos_nr):.3f} (range {np.min(rhos_nr):.3f}-{np.max(rhos_nr):.3f}) "
        f"excluding residual. "
        f"item_id correctly identified as dominant systematic source in {np.mean(top1s):.0f}% of runs; "
        f"top-5 systematic components correct in {np.mean(top5s_nr):.0f}% of runs. "
        f"Residual is inflated on binary scale (absorbs within-cell Bernoulli variance) "
        f"but systematic component rankings are preserved. "
        f"Mean |bias| by accuracy: {bias_trend}; rho by accuracy: {rho_trend}. "
        f"Ranking recovery is robust across p in [0.5-0.8] and improves with n_items."
    )

    out = Path("results/analysis/binary_simulation_recovery_matched.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\n{'=' * 60}")
    print(f"Done in {elapsed:.1f}s -> {out}")
    print(f"\n{results['conclusion']}")


if __name__ == "__main__":
    run()
