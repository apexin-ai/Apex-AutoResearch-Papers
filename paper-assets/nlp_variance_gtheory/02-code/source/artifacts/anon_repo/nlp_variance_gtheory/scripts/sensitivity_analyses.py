#!/usr/bin/env python3
"""Sensitivity analyses for exp-001 G-study (4-model bf16).

(k) Fixed vs Random facet sensitivity
(d) REML vs Henderson Method I
(i) Power analysis for interaction detection

Output: results/exp001_analysis/sensitivity_analyses.json
"""

import json
import time
from itertools import combinations
from math import prod
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import optimize, stats

FACETS = ["model", "temperature", "prompt_template", "seed", "ordering", "item_id"]


def _ikey(a, b):
    """Canonical interaction key in FACETS order."""
    return f"{a}:{b}" if FACETS.index(a) < FACETS.index(b) else f"{b}:{a}"


def compute_henderson_i(df, response="correct"):
    """Henderson Method I variance component estimation."""
    gm = df[response].mean()
    N = len(df)
    nl = {f: df[f].nunique() for f in FACETS}
    anova = {}

    # Main effects
    for f in FACETS:
        means = df.groupby(f, observed=True)[response].mean()
        n_per = N // nl[f]
        ss = float(n_per * ((means - gm) ** 2).sum())
        dof = nl[f] - 1
        anova[f] = {"ss": ss, "df": dof, "ms": ss / dof if dof > 0 else 0.0}

    # Two-way interactions (vectorized)
    for fi, fj in combinations(FACETS, 2):
        cell = df.groupby([fi, fj], observed=True)[response].mean()
        mi = df.groupby(fi, observed=True)[response].mean()
        mj = df.groupby(fj, observed=True)[response].mean()
        cdf = cell.reset_index(name="cm")
        cdf["interaction"] = (cdf["cm"]
                              - cdf[fi].map(mi)
                              - cdf[fj].map(mj)
                              + gm)
        n_per = N // (nl[fi] * nl[fj])
        ss = float(n_per * (cdf["interaction"] ** 2).sum())
        dof = (nl[fi] - 1) * (nl[fj] - 1)
        anova[f"{fi}:{fj}"] = {"ss": ss, "df": dof, "ms": ss / dof if dof > 0 else 0.0}

    # Residual
    ss_tot = float(((df[response] - gm) ** 2).sum())
    ss_exp = sum(e["ss"] for e in anova.values())
    ss_res = max(0.0, ss_tot - ss_exp)
    df_res = N - 1 - sum(e["df"] for e in anova.values())
    anova["residual"] = {"ss": ss_res, "df": max(1, df_res),
                         "ms": ss_res / max(1, df_res)}

    ms_res = anova["residual"]["ms"]
    vc, vc_raw = {}, {}

    # Two-way interaction VCs
    for fi, fj in combinations(FACETS, 2):
        key = f"{fi}:{fj}"
        coeff = prod(nl[f] for f in FACETS if f not in (fi, fj))
        raw = (anova[key]["ms"] - ms_res) / coeff if coeff > 0 else 0.0
        vc_raw[key] = raw
        vc[key] = max(0.0, raw)

    # Main effect VCs (using clamped interactions)
    for fi in FACETS:
        cm = prod(nl[f] for f in FACETS if f != fi)
        ic = sum(prod(nl[f] for f in FACETS if f not in (fi, fj))
                 * vc[_ikey(fi, fj)]
                 for fj in FACETS if fj != fi)
        raw = (anova[fi]["ms"] - ic - ms_res) / cm if cm > 0 else 0.0
        vc_raw[fi] = raw
        vc[fi] = max(0.0, raw)

    vc["residual"] = ms_res
    vc_raw["residual"] = ms_res
    return vc, nl, anova, vc_raw


def compute_g_item(vc, nl, fixed=None):
    """G coefficient with item_id as measurement object.

    tau = sigma2(item_id)
    delta = sum(sigma2(facet:item_id) / n_facet for random non-item facets)
          + sigma2(residual) / prod(n_random_non_item_facets)
    Fixed facets: their item-interactions excluded from delta;
    residual divided only by random non-item facet levels.
    """
    fixed = set(fixed or [])
    tau = vc.get("item_id", 0)
    rni = [f for f in FACETS if f != "item_id" and f not in fixed]
    delta = 0.0
    terms = {}

    for key, est in vc.items():
        if key == "item_id" or est <= 0:
            continue
        parts = key.split(":")
        if "item_id" in parts:
            other = [p for p in parts if p != "item_id"]
            if any(f in fixed for f in other):
                continue
            d = prod(nl[f] for f in other) if other else 1
            terms[key] = {"est": est, "divisor": d, "contribution": est / d}
            delta += est / d
        elif key == "residual":
            d = prod(nl[f] for f in rni) if rni else 1
            terms["residual"] = {"est": est, "divisor": d, "contribution": est / d}
            delta += est / d

    g = tau / (tau + delta) if (tau + delta) > 0 else 0
    return round(g, 6), round(tau, 8), round(delta, 8), terms


# === (k) Fixed vs Random ================================================

def analysis_fixed_vs_random(vc, nl):
    tv = sum(vc.values())
    g_a, t_a, d_a, tr_a = compute_g_item(vc, nl)
    g_f, t_f, d_f, tr_f = compute_g_item(vc, nl, fixed={"temperature", "ordering"})

    return {
        "all_random": {
            "G_item": g_a, "tau": t_a, "delta": d_a,
            "item_id_pct": round(vc["item_id"] / tv * 100, 2),
            "delta_terms": {k: round(v["contribution"], 8) for k, v in tr_a.items()},
        },
        "temp_ordering_fixed": {
            "G_item": g_f, "tau": t_f, "delta": d_f,
            "item_id_pct": round(vc["item_id"] / tv * 100, 2),
            "excluded_from_delta": ["temperature:item_id", "ordering:item_id"],
            "delta_terms": {k: round(v["contribution"], 8) for k, v in tr_f.items()},
        },
        "difference": {
            "G_item_diff": round(g_f - g_a, 6),
            "G_item_diff_pct_points": round((g_f - g_a) * 100, 2),
            "delta_reduction_pct": round((1 - d_f / d_a) * 100, 2) if d_a > 0 else 0,
        },
        "variance_pct_excluded": {
            "temperature:item_id_pct": round(vc.get("temperature:item_id", 0) / tv * 100, 4),
            "ordering:item_id_pct": round(vc.get("ordering:item_id", 0) / tv * 100, 4),
        },
    }


# === (d) REML vs Henderson ==============================================

def build_ems_matrix(nl):
    """Build EMS coefficient matrix for balanced crossed design.

    E[MS_A] = sigma2_res + coeff_A * sigma2_A + sum coeff_AB * sigma2_AB
    E[MS_AB] = sigma2_res + coeff_AB * sigma2_AB
    E[MS_res] = sigma2_res
    """
    comps = (list(FACETS)
             + [f"{a}:{b}" for a, b in combinations(FACETS, 2)]
             + ["residual"])
    nc = len(comps)
    C = np.zeros((nc, nc))
    ri = comps.index("residual")

    for i, term in enumerate(comps):
        if term == "residual":
            C[i, ri] = 1.0
        elif ":" in term:
            a, b = term.split(":")
            C[i, i] = prod(nl[f] for f in FACETS if f not in (a, b))
            C[i, ri] = 1.0
        else:
            fi = term
            C[i, i] = prod(nl[f] for f in FACETS if f != fi)
            C[i, ri] = 1.0
            for fj in FACETS:
                if fj == fi:
                    continue
                ik = _ikey(fi, fj)
                j = comps.index(ik)
                C[i, j] = prod(nl[f] for f in FACETS if f not in (fi, fj))

    return C, comps


def reml_nll(theta, ms_vec, df_vec, C):
    """Negative REML log-likelihood for balanced design."""
    ems = C @ theta
    if np.any(ems <= 1e-20):
        return 1e20
    return 0.5 * np.sum(df_vec * (np.log(ems) + ms_vec / ems))


def analysis_reml_vs_henderson(vc, vc_raw, nl, anova):
    C, comps = build_ems_matrix(nl)
    ms_vec = np.array([anova[c]["ms"] for c in comps])
    df_vec = np.array([anova[c]["df"] for c in comps])
    hend = np.array([vc.get(c, 0) for c in comps])

    # Constrained REML via L-BFGS-B
    x0 = np.maximum(hend, 1e-12)
    bounds = [(1e-15, None)] * len(comps)
    res = optimize.minimize(reml_nll, x0, args=(ms_vec, df_vec, C),
                            method="L-BFGS-B", bounds=bounds,
                            options={"maxiter": 10000, "ftol": 1e-15})
    reml = res.x

    out = {}
    for i, c in enumerate(comps):
        h, r = float(hend[i]), float(reml[i])
        if h > 1e-10:
            dp = round((r - h) / h * 100, 4)
        else:
            dp = 0.0 if r < 1e-8 else "N/A"
        out[c] = {"henderson": round(h, 10), "reml": round(r, 10), "diff_pct": dp}

    pos = [c for c in comps if vc.get(c, 0) > 1e-10]
    md = max((abs(out[c]["reml"] - out[c]["henderson"]) / out[c]["henderson"]
              for c in pos), default=0) * 100

    return {
        "components": out,
        "reml_converged": res.success,
        "reml_nit": int(res.nit),
        "max_relative_diff_pct": round(md, 4),
        "n_boundary_components": sum(1 for v in vc_raw.values() if v < -1e-10),
        "boundary_components": [c for c, v in vc_raw.items() if v < -1e-10],
    }


# === (i) Power Analysis ==================================================

def analysis_power(vc, nl, anova):
    """Power for detecting model:item_id interaction via F-test.

    For random effects ANOVA:
      F = MS_AB / MS_res
      Under H1: F_obs / (1 + n_cell * sigma2_AB / sigma2_res) ~ F(df_AB, df_res)
      Power = P(F > F_crit | H1) = 1 - F_cdf(F_crit / scale, df_AB, df_res)
    """
    tv = sum(vc.values())
    ms_res = vc["residual"]
    mi_key = "model:item_id"
    n_cell = prod(nl[f] for f in FACETS if f not in ("model", "item_id"))
    df_mi = (nl["model"] - 1) * (nl["item_id"] - 1)
    df_res = anova["residual"]["df"]
    alpha = 0.05
    f_crit = stats.f.ppf(1 - alpha, df_mi, df_res)
    f_obs = anova[mi_key]["ms"] / ms_res

    curve = []
    for pct in [1, 2, 5, 10]:
        s2 = tv * pct / 100
        scale = 1 + n_cell * s2 / ms_res
        pw = float(1 - stats.f.cdf(f_crit / scale, df_mi, df_res))
        curve.append({
            "effect_size_pct": pct,
            "sigma2_effect": round(s2, 8),
            "noncentrality_scale": round(scale, 4),
            "power": round(pw, 6),
        })

    return {
        "design": {
            "models": int(nl["model"]),
            "conditions_per_model_item": int(n_cell),
            "items": int(nl["item_id"]),
            "total_observations": int(prod(nl[f] for f in FACETS)),
        },
        "test_details": {
            "target": mi_key,
            "df_numerator": int(df_mi),
            "df_denominator": int(df_res),
            "f_critical_alpha05": round(float(f_crit), 6),
            "ms_residual": round(float(ms_res), 8),
            "total_variance": round(float(tv), 8),
        },
        "observed": {
            "f_statistic": round(float(f_obs), 4),
            "sigma2_model_item": round(float(vc.get(mi_key, 0)), 8),
            "pct_of_total": round(float(vc.get(mi_key, 0) / tv * 100), 2),
            "p_value": round(float(1 - stats.f.cdf(f_obs, df_mi, df_res)), 10),
        },
        "power_curve": curve,
    }


# === Main =================================================================

def main():
    t0 = time.time()
    csv = "./results/analysis/cross_model_4way_bf16.csv"
    print(f"Loading {csv}...")
    df = pd.read_csv(csv, low_memory=False)
    print(f"  {len(df)} rows")
    for f in FACETS:
        df[f] = df[f].astype(str)

    print("Henderson Method I...", flush=True)
    vc, nl, anova, vc_raw = compute_henderson_i(df)
    tv = sum(vc.values())
    g0, _, _, _ = compute_g_item(vc, nl)
    print(f"  n_levels: { {k: int(v) for k, v in nl.items()} }")
    print(f"  G_item={g0}, total_var={tv:.6f}")
    print(f"  item_id={vc['item_id']/tv*100:.2f}%  model:item={vc.get('model:item_id',0)/tv*100:.2f}%  residual={vc['residual']/tv*100:.2f}%")

    print("\n[k] Fixed vs Random...", flush=True)
    rk = analysis_fixed_vs_random(vc, nl)
    print(f"  all-random G={rk['all_random']['G_item']}  fixed G={rk['temp_ordering_fixed']['G_item']}  diff={rk['difference']['G_item_diff']}")

    print("\n[d] REML vs Henderson...", flush=True)
    rd = analysis_reml_vs_henderson(vc, vc_raw, nl, anova)
    print(f"  converged={rd['reml_converged']}  max_diff={rd['max_relative_diff_pct']}%  boundary={rd['boundary_components']}")

    print("\n[i] Power analysis...", flush=True)
    ri = analysis_power(vc, nl, anova)
    print(f"  F_obs={ri['observed']['f_statistic']}  p={ri['observed']['p_value']}")
    for p in ri["power_curve"]:
        print(f"    {p['effect_size_pct']}% effect -> power={p['power']}")

    output = {
        "fixed_vs_random": rk,
        "reml_vs_henderson": rd,
        "power_analysis": ri,
        "baseline": {
            "G_item": g0,
            "n_levels": {k: int(v) for k, v in nl.items()},
            "n_observations": len(df),
            "variance_components": {
                k: {"estimate": round(v, 10), "pct": round(v / tv * 100, 4)}
                for k, v in sorted(vc.items(), key=lambda x: -x[1])
            },
        },
        "elapsed_seconds": round(time.time() - t0, 1),
    }

    out = Path("./results/exp001_analysis/sensitivity_analyses.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(str(out), "w") as fp:
        json.dump(output, fp, indent=2, default=str)
    print(f"\nDone in {time.time()-t0:.1f}s -> {out}")


if __name__ == "__main__":
    main()
