"""
Compare Uniform vs Non-uniform DIF models (Reviewer W11).

Uniform DIF:     P(y=1) = sigma(a_i * (theta_j - b_i) + gamma * e_ij)
Non-uniform DIF: P(y=1) = sigma(a_i * (theta_j - b_i + gamma * e_ij))

Data: MMLU, J=16 (<=3B models), I=300 (stratified subsample).
MCMC: CmdStanPy, 4 chains, 1000 warmup + 1000 sampling, adapt_delta=0.95.
"""

import os
import sys
import time
import json
import numpy as np
import pandas as pd
import arviz as az
from cmdstanpy import CmdStanModel
from scipy.special import expit

PROJ = "/root/contamcal-irt-calibration"
DATA = os.path.join(PROJ, "analysis/irt_data/mmlu")
STAN = os.path.join(PROJ, "stan_models")
OUT  = os.path.join(PROJ, "analysis/dif_comparison")

SEED = 42
N_ITEMS = 300
N_CHAINS = 4
N_WARMUP = 1000
N_SAMPLING = 1000
ADAPT_DELTA = 0.95


def load_data():
    resp = pd.read_csv(os.path.join(DATA, "response_matrix.csv"))
    expo = pd.read_csv(os.path.join(DATA, "exposure_scores.csv"))
    meta = pd.read_csv(os.path.join(DATA, "item_metadata.csv"))

    mask = ~resp["respondent"].str.contains("7B")
    resp = resp[mask].reset_index(drop=True)
    expo = expo[expo["respondent"].isin(resp["respondent"])].reset_index(drop=True)

    names = resp["respondent"].values
    Y = resp.drop(columns=["respondent"]).values.astype(int)
    e = expo.set_index("respondent").loc[names, "exposure"].values
    J, I_all = Y.shape

    rng = np.random.default_rng(SEED)
    doms = meta["domain"].values
    udoms = np.unique(doms)
    per_d = max(1, N_ITEMS // len(udoms))
    idx = []
    for d in udoms:
        di = np.where(doms == d)[0]
        idx.append(rng.choice(di, size=min(per_d, len(di)), replace=False))
    idx = np.concatenate(idx)
    if len(idx) < N_ITEMS:
        rem = np.setdiff1d(np.arange(I_all), idx)
        idx = np.concatenate([idx, rng.choice(rem, size=N_ITEMS - len(idx), replace=False)])
    elif len(idx) > N_ITEMS:
        idx = rng.choice(idx, size=N_ITEMS, replace=False)
    idx = np.sort(idx)

    Y = Y[:, idx]
    print(f"Data: J={J} respondents, I={Y.shape[1]} items (from {I_all})", flush=True)
    print(f"Exposure range: [{e.min():.2f}, {e.max():.2f}]", flush=True)
    print(f"Respondents: {list(names)}", flush=True)
    return Y, e, names


def fit_model(stan_file, Y, exposure, label):
    J, I = Y.shape
    E = np.tile(exposure[:, None], (1, I))
    data = {"N_models": J, "N_items": I, "y": Y.tolist(), "exposure": E.tolist()}

    print(f"\n{'='*60}", flush=True)
    print(f"Fitting: {label}", flush=True)
    print(f"Stan file: {stan_file}", flush=True)
    print(f"{'='*60}", flush=True)

    t0 = time.time()
    model = CmdStanModel(stan_file=stan_file)
    ct = time.time() - t0
    print(f"Compiled in {ct:.0f}s", flush=True)

    t0 = time.time()
    f = model.sample(
        data=data,
        chains=N_CHAINS,
        iter_warmup=N_WARMUP,
        iter_sampling=N_SAMPLING,
        adapt_delta=ADAPT_DELTA,
        seed=SEED,
        show_progress=True,
    )
    st = time.time() - t0
    print(f"Sampled in {st:.0f}s ({st/60:.1f} min)", flush=True)
    return f, ct, st


def compute_ppp(fit_obj, Y, exposure, model_type):
    J, I = Y.shape
    E = np.tile(exposure[:, None], (1, I))
    T_obs = float(Y.sum())

    th = fit_obj.stan_variable("theta")
    a  = fit_obj.stan_variable("a")
    b  = fit_obj.stan_variable("b")
    g  = fit_obj.stan_variable("gamma")
    S = th.shape[0]
    rng = np.random.default_rng(SEED + 1)

    count = 0
    for s in range(S):
        if model_type == "uniform_dif":
            eta = a[s][None, :] * (th[s][:, None] - b[s][None, :]) + g[s] * E
        else:
            eta = a[s][None, :] * (th[s][:, None] - b[s][None, :] + g[s] * E)
        y_rep = rng.binomial(1, expit(eta))
        if y_rep.sum() >= T_obs:
            count += 1
    return count / S


def sf(v):
    if v is None:
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def main():
    os.makedirs(OUT, exist_ok=True)
    total_t0 = time.time()

    print("=" * 60, flush=True)
    print("DIF Model Comparison: Uniform vs Non-uniform", flush=True)
    print(f"Config: I={N_ITEMS}, chains={N_CHAINS}, "
          f"warmup={N_WARMUP}, sampling={N_SAMPLING}, "
          f"adapt_delta={ADAPT_DELTA}", flush=True)
    print("=" * 60, flush=True)

    Y, exposure, names = load_data()
    J, I = Y.shape

    models = [
        ("uniform_dif", os.path.join(STAN, "contam_irt_2pl_gamma.stan")),
        ("nonuniform_dif",    os.path.join(STAN, "contam_irt_2pl_gamma_uniform.stan")),
    ]

    results = {}
    idatas = {}

    for mtype, sfile in models:
        f, ct, st = fit_model(sfile, Y, exposure, f"{mtype} DIF")

        summ = f.summary()
        gr = summ.loc["gamma"]

        try:
            ndiv = int(f.method_variables()["divergent__"].sum())
        except Exception:
            ndiv = -1

        r = {
            "gamma_mean":   sf(gr["Mean"]),
            "gamma_sd":     sf(gr["StdDev"]),
            "gamma_q5":     sf(gr["5%"]),
            "gamma_q95":    sf(gr["95%"]),
            "gamma_rhat":   sf(gr["R_hat"]),
            "gamma_ess_bulk": sf(gr["ESS_bulk"]),
            "gamma_ess_tail": sf(gr["ESS_tail"]),
            "max_rhat":     sf(summ["R_hat"].dropna().max()),
            "min_ess_bulk": sf(summ["ESS_bulk"].dropna().min()),
            "n_divergent":  ndiv,
            "compile_s":    round(ct, 1),
            "sample_s":     round(st, 1),
        }

        print(f"\n  gamma = {r['gamma_mean']:.4f} +/- {r['gamma_sd']:.4f} "
              f"  90%CI: [{r['gamma_q5']:.4f}, {r['gamma_q95']:.4f}]", flush=True)
        print(f"  Rhat(gamma)={r['gamma_rhat']:.4f}  "
              f"ESS_bulk(gamma)={r['gamma_ess_bulk']:.0f}  "
              f"ESS_tail(gamma)={r['gamma_ess_tail']:.0f}", flush=True)
        print(f"  Max Rhat={r['max_rhat']:.4f}  Min ESS_bulk={r['min_ess_bulk']:.0f}", flush=True)
        print(f"  Divergences: {ndiv}", flush=True)

        print("  Computing PPP...", flush=True)
        r["ppp"] = compute_ppp(f, Y, exposure, mtype)
        print(f"  PPP = {r['ppp']:.3f}", flush=True)

        print("  Computing LOO...", flush=True)
        try:
            idata = az.from_cmdstanpy(posterior=f, log_likelihood="log_lik")
            idatas[mtype] = idata

            l = az.loo(idata)
            r["loo_elpd"]  = sf(l.elpd)
            r["loo_se"]    = sf(l.se)
            r["p_loo"]     = sf(l.p)
            try:
                kvals = np.asarray(l.pareto_k)
                r["loo_k_gt07"] = int((kvals > 0.7).sum())
            except Exception:
                r["loo_k_gt07"] = None
            print(f"  LOO elpd={r['loo_elpd']:.1f} +/- {r['loo_se']:.1f}  "
                  f"p_loo={r['p_loo']:.1f}  k>0.7={r['loo_k_gt07']}", flush=True)
        except Exception as e:
            print(f"  LOO failed: {type(e).__name__}: {e}", flush=True)
            r["loo_elpd"] = r["loo_se"] = r["p_loo"] = r["loo_k_gt07"] = None

        results[mtype] = r

    # --- Model Comparison ---
    print("\n" + "=" * 60, flush=True)
    print("MODEL COMPARISON", flush=True)
    print("=" * 60, flush=True)

    if len(idatas) == 2:
        try:
            comp_df = az.compare(idatas)
            print("\nArViZ LOO Comparison:", flush=True)
            print(comp_df.to_string(), flush=True)
        except Exception as e:
            print(f"az.compare failed: {type(e).__name__}: {e}", flush=True)

    u  = results["uniform_dif"]
    nu = results["nonuniform_dif"]

    print(f"\n{'Metric':<25} {'Uniform':>15} {'Non-uniform':>15}", flush=True)
    print("-" * 55, flush=True)

    def prow(label, key, fmt):
        v1, v2 = u[key], nu[key]
        print(f"{label:<25} {v1:>15{fmt}} {v2:>15{fmt}}", flush=True)

    prow("gamma mean",      "gamma_mean",     ".4f")
    prow("gamma SD",        "gamma_sd",       ".4f")
    prow("gamma Rhat",      "gamma_rhat",     ".4f")
    prow("gamma ESS_bulk",  "gamma_ess_bulk", ".0f")
    prow("gamma ESS_tail",  "gamma_ess_tail", ".0f")
    prow("Max Rhat (all)",  "max_rhat",       ".4f")
    prow("Min ESS_bulk",    "min_ess_bulk",   ".0f")
    prow("Divergences",     "n_divergent",    "d")
    prow("PPP",             "ppp",            ".3f")

    print(f"{'gamma 90% CI':<25} [{u['gamma_q5']:.3f}, {u['gamma_q95']:.3f}]"
          f"     [{nu['gamma_q5']:.3f}, {nu['gamma_q95']:.3f}]", flush=True)

    if u.get("loo_elpd") is not None and nu.get("loo_elpd") is not None:
        dl = nu["loo_elpd"] - u["loo_elpd"]
        print(f"{'LOO elpd':<25} {u['loo_elpd']:>15.1f} {nu['loo_elpd']:>15.1f}  delta={dl:+.1f}", flush=True)
        print(f"{'LOO SE':<25} {u['loo_se']:>15.1f} {nu['loo_se']:>15.1f}", flush=True)
        print(f"{'p_loo':<25} {u['p_loo']:>15.1f} {nu['p_loo']:>15.1f}", flush=True)
        if u.get("loo_k_gt07") is not None and nu.get("loo_k_gt07") is not None:
            print(f"{'LOO k>0.7':<25} {u['loo_k_gt07']:>15d} {nu['loo_k_gt07']:>15d}", flush=True)

    # Save JSON
    jpath = os.path.join(OUT, "results.json")
    with open(jpath, "w") as fp:
        json.dump(results, fp, indent=2, default=float)
    print(f"\nSaved: {jpath}", flush=True)

    total_elapsed = time.time() - total_t0
    print(f"\nTotal time: {total_elapsed:.0f}s ({total_elapsed/60:.1f} min)", flush=True)
    print("Done.", flush=True)


if __name__ == "__main__":
    main()
