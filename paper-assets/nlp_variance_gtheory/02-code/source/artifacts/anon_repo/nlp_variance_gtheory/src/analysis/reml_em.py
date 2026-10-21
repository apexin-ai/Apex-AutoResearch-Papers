"""REML variance component estimation via EM algorithm.

Uses Henderson MME with Cholesky factorization. Set OPENBLAS_NUM_THREADS=2
for optimal performance on this server (multi-thread OpenBLAS has contention issues).
"""

import argparse
import json
import time
from itertools import combinations
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import sparse
from scipy.linalg import cho_factor, cho_solve


ALL_FACETS = [
    "model", "precision", "temperature",
    "prompt_template", "seed", "ordering", "item_id",
]


def _encode_factor(series):
    codes, uniques = pd.factorize(series, sort=True)
    return codes, len(uniques)


def _build_z_sparse(codes, n_levels, n_obs):
    return sparse.csc_matrix(
        (np.ones(n_obs, dtype=np.float64), (np.arange(n_obs), codes)),
        shape=(n_obs, n_levels),
    )


def reml_em(df, response, facets, max_iter=500, tol=1e-8, verbose=True):
    t0 = time.time()
    n_obs = len(df)
    y = df[response].values.astype(np.float64)
    p = 1

    factor_codes = {}
    factor_nlevels = {}
    for f in facets:
        codes, nl = _encode_factor(df[f])
        factor_codes[f] = codes
        factor_nlevels[f] = nl

    re_names = []
    Z_list = []
    q_list = []

    for f in facets:
        Z = _build_z_sparse(factor_codes[f], factor_nlevels[f], n_obs)
        re_names.append(f)
        Z_list.append(Z)
        q_list.append(factor_nlevels[f])

    for fi, fj in combinations(facets, 2):
        int_codes = factor_codes[fi] * factor_nlevels[fj] + factor_codes[fj]
        observed = np.unique(int_codes)
        n_obs_levels = len(observed)
        remap = np.empty(factor_nlevels[fi] * factor_nlevels[fj], dtype=np.int32)
        remap[observed] = np.arange(n_obs_levels)
        Z = _build_z_sparse(remap[int_codes], n_obs_levels, n_obs)
        re_names.append(f"{fi}:{fj}")
        Z_list.append(Z)
        q_list.append(n_obs_levels)

    K = len(re_names)
    q_arr = np.array(q_list)
    q_total = int(q_arr.sum())
    dim = p + q_total
    q_offsets = np.zeros(K + 1, dtype=int)
    q_offsets[1:] = np.cumsum(q_arr)

    if verbose:
        print(f"REML-EM: {n_obs} obs, {K} RE terms, q={q_total}, dim={dim}")

    Z_full = sparse.hstack(Z_list, format="csc")
    ZtZ = (Z_full.T @ Z_full).toarray()
    Zty = np.asarray(Z_full.T @ y).ravel()
    ones = np.ones(n_obs, dtype=np.float64)
    ZtX = np.asarray(Z_full.T @ ones).ravel()
    XtX = float(n_obs)
    Xty = float(ones @ y)
    yty = float(y @ y)
    del Z_full, Z_list

    if verbose:
        print(f"  Precomp: {time.time()-t0:.1f}s")

    from variance_decomposition import compute_ss, estimate_variance_components
    effects_init, n_levels_init = compute_ss(df, response, facets)
    vc_init = estimate_variance_components(effects_init, facets, n_levels_init)

    sigma2 = np.zeros(K + 1, dtype=np.float64)
    for i, name in enumerate(re_names):
        sigma2[i] = max(vc_init.get(name, 0.0), 1e-10)
    sigma2[K] = max(vc_init.get("residual", 0.01), 1e-10)

    if verbose:
        print(f"  Henderson I init: total={sigma2.sum():.6f}")

    C_base = np.zeros((dim, dim), dtype=np.float64)
    C_base[0, 0] = XtX
    C_base[0, 1:] = ZtX
    C_base[1:, 0] = ZtX
    C_base[1:, 1:] = ZtZ

    rhs = np.zeros(dim, dtype=np.float64)
    rhs[0] = Xty
    rhs[1:] = Zty

    converged = False
    sigma2_history = []

    for iteration in range(max_iter):
        t_iter = time.time()
        sigma2_old = sigma2.copy()
        sig2e = sigma2[K]

        C = C_base.copy()
        for i in range(K):
            lam_i = sig2e / sigma2[i]
            s = p + q_offsets[i]
            e = p + q_offsets[i + 1]
            np.fill_diagonal(C[s:e, s:e], C[s:e, s:e].diagonal() + lam_i)

        # Cholesky solve
        cho = cho_factor(C, lower=False, check_finite=False)
        sol = cho_solve(cho, rhs, check_finite=False)
        beta_hat = sol[0]
        u_hat = sol[1:]

        # Diagonal of C_inv via Cholesky: solve C * X = I column by column
        # Only need trace per block, so compute just needed diag elements
        C_inv_diag = np.zeros(dim)
        eye_cols = np.eye(dim, dtype=np.float64)
        C_inv_full = cho_solve(cho, eye_cols, check_finite=False)
        C_inv_diag = np.diag(C_inv_full)

        rss = yty - float(sol @ rhs)

        trace_lam_sum = 0.0
        for i in range(K):
            s = q_offsets[i]
            e = q_offsets[i + 1]
            qi = q_arr[i]
            u_k = u_hat[s:e]
            tr_Cinv_kk = C_inv_diag[p+s:p+e].sum()

            sigma2[i] = max(1e-12, (u_k @ u_k + sig2e * tr_Cinv_kk) / qi)
            lam_k = sig2e / sigma2_old[i]
            trace_lam_sum += lam_k * tr_Cinv_kk

        sigma2[K] = max(1e-12, (rss + sig2e * (q_total - trace_lam_sum)) / (n_obs - p))

        rel_change = np.max(np.abs(sigma2 - sigma2_old) / (np.abs(sigma2_old) + 1e-15))
        dt = time.time() - t_iter

        if verbose and (iteration < 10 or iteration % 20 == 0):
            print(f"  iter {iteration}: Δ={rel_change:.2e} "
                  f"sig2e={sigma2[K]:.6f} total={sigma2.sum():.6f} ({dt:.1f}s)")

        sigma2_history.append(sigma2.copy())

        if rel_change < tol:
            converged = True
            if verbose:
                print(f"  Converged at iter {iteration} (Δ={rel_change:.2e})")
            break

    elapsed = time.time() - t0

    vc_dict = {}
    total_var = float(sigma2.sum())
    for i, name in enumerate(re_names):
        vc_dict[name] = {"estimate": float(sigma2[i]),
                         "pct": float(sigma2[i] / total_var * 100)}
    vc_dict["residual"] = {"estimate": float(sigma2[K]),
                           "pct": float(sigma2[K] / total_var * 100)}

    result = {
        "variance_components": vc_dict,
        "total_variance": total_var,
        "n_observations": n_obs,
        "method": "REML-EM (Henderson MME)",
        "elapsed_seconds": elapsed,
        "converged": converged,
        "n_iterations": iteration + 1,
        "n_levels": {f: factor_nlevels[f] for f in facets},
        "fixed_intercept": float(beta_hat),
        "n_random_effects": K,
        "q_total": q_total,
        "all_facets": facets,
    }

    if verbose:
        print(f"\n=== REML Variance Components ({elapsed:.1f}s, {iteration+1} iters) ===")
        print(f"{'Component':<30} {'Estimate':>12} {'%':>8}")
        print("-" * 52)
        for name, info in sorted(vc_dict.items(), key=lambda x: -x[1]["estimate"]):
            print(f"{name:<30} {info['estimate']:>12.6f} {info['pct']:>7.2f}%")
        print(f"\nTotal: {total_var:.6f}, Grand mean: {float(beta_hat):.4f}")

    return result


if __name__ == "__main__":
    import os
    os.environ.setdefault("OPENBLAS_NUM_THREADS", "2")

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", default="results/analysis/cross_model_reml.json")
    parser.add_argument("--response-var", default="correct")
    parser.add_argument("--max-iter", type=int, default=500)
    args = parser.parse_args()

    df = pd.read_json(args.input, lines=True)
    for f in ALL_FACETS:
        df[f] = df[f].astype(str)

    if args.response_var == "correct":
        if "binary_correct" in df.columns:
            resp = "binary_correct"
        else:
            df["binary_correct"] = df["correct"]
            resp = "binary_correct"
    else:
        resp = args.response_var

    result = reml_em(df, resp, ALL_FACETS, max_iter=args.max_iter)

    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(result, f, indent=2)
    print(f"\n-> {args.output}")
