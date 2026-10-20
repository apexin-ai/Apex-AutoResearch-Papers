# fit_irt_dose_response.py — IRT 2PL dose-response fitting for contamination calibration
# Fits 2PL IRT per benchmark, estimates theta per (family, dosage),
# fits dose-response curves, and runs TOST equivalence tests.

import argparse
import json
import os
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.special import expit
from scipy import stats

FAMILIES = ["qwen7b", "qwen14b", "gemma2", "phi4", "olmo2"]
DOSAGES = ["d000", "d005", "d025", "d050", "d100"]
DOSAGE_VALUES = {"d000": 0.0, "d005": 0.05, "d025": 0.25, "d050": 0.50, "d100": 1.0}
BENCHMARKS = ["mmlu", "arc_challenge"]


def log(msg):
    print(msg, flush=True)


def load_correctness_matrix(base_dir, family, dosage):
    path = Path(base_dir) / f"{family}_{dosage}" / "correctness_matrix.json"
    if not path.exists():
        alt = Path(base_dir) / f"{family}_{dosage}" / "eval_results.json"
        if not alt.exists():
            return None
        with open(alt) as f:
            data = json.load(f)
        result = {}
        for bm in BENCHMARKS:
            if bm in data.get("benchmarks", {}):
                items = data["benchmarks"][bm].get("per_item", [])
                result[bm] = [item["correct"] for item in items]
        return result if result else None
    with open(path) as f:
        return json.load(f)


def build_response_matrix(base_dir, benchmark):
    respondents = []
    labels = []
    for family in FAMILIES:
        for dosage in DOSAGES:
            cm = load_correctness_matrix(base_dir, family, dosage)
            if cm is None or benchmark not in cm:
                continue
            vec = cm[benchmark]
            respondents.append(np.array(vec, dtype=np.float64))
            labels.append((family, dosage))
    if not respondents:
        return None, None, 0
    n_items = len(respondents[0])
    valid = [r for r in respondents if len(r) == n_items]
    if len(valid) < len(respondents):
        log(f"  WARNING: dropped {len(respondents)-len(valid)} respondents with mismatched item count")
        labels = [labels[i] for i, r in enumerate(respondents) if len(r) == n_items]
    return np.array(valid), labels, n_items


# ── 2PL IRT with analytic gradients ────────────────────────────────────────

def fit_2pl(X, max_iter=30, tol=1e-4, verbose=False, reg_a=0.05):
    """
    2PL IRT via alternating optimization with analytic gradients.
    X: (J, I) binary response matrix (J respondents, I items).
    reg_a: L2 regularization on discrimination toward 1.0
    """
    J, I = X.shape
    log(f"  Matrix: {J} respondents x {I} items")

    prop_j = X.mean(axis=1).clip(0.01, 0.99)
    theta = stats.norm.ppf(prop_j)

    prop_i = X.mean(axis=0).clip(0.01, 0.99)
    b = -stats.norm.ppf(prop_i)
    a = np.ones(I)

    prev_nll = np.inf

    for iteration in range(max_iter):
        # E-step: optimize each theta_j given fixed (a, b)
        a_fixed, b_fixed = a.copy(), b.copy()
        for j in range(J):
            xj = X[j]
            def _theta_obj(t, _xj=xj, _a=a_fixed, _b=b_fixed):
                z = _a * (t[0] - _b)
                p = expit(z)
                pc = np.clip(p, 1e-10, 1 - 1e-10)
                nll = -((_xj * np.log(pc) + (1 - _xj) * np.log(1 - pc)).sum())
                grad = -((_xj - p) * _a).sum()
                return nll, np.array([grad])
            res = minimize(_theta_obj, [theta[j]], jac=True,
                          method='L-BFGS-B', bounds=[(-4.0, 4.0)])
            theta[j] = res.x[0]

        # M-step: optimize (a, b) jointly given fixed theta
        theta_fixed = theta.copy()

        def _items_obj(params):
            av = params[:I]
            bv = params[I:]
            Z = av[None, :] * (theta_fixed[:, None] - bv[None, :])
            P = expit(Z)
            Pc = np.clip(P, 1e-10, 1 - 1e-10)
            nll = -(X * np.log(Pc) + (1 - X) * np.log(1 - Pc)).sum()
            nll += reg_a * np.sum((av - 1.0) ** 2)

            R = X - P
            diff = theta_fixed[:, None] - bv[None, :]
            ga = -(R * diff).sum(axis=0) + 2 * reg_a * (av - 1.0)
            gb = av * R.sum(axis=0)
            return nll, np.concatenate([ga, gb])

        x0 = np.concatenate([a, b])
        bounds_items = [(0.1, 5.0)] * I + [(-5.0, 5.0)] * I
        res = minimize(_items_obj, x0, jac=True, method='L-BFGS-B',
                      bounds=bounds_items, options={'maxiter': 200, 'ftol': 1e-10})
        a = np.clip(res.x[:I], 0.1, 5.0)
        b = res.x[I:]

        # Convergence check
        Z = a[None, :] * (theta[:, None] - b[None, :])
        P = expit(Z)
        Pc = np.clip(P, 1e-10, 1 - 1e-10)
        nll = -(X * np.log(Pc) + (1 - X) * np.log(1 - Pc)).sum()

        if verbose:
            log(f"  Iter {iteration+1}: NLL={nll:.2f}, a mean={a.mean():.3f} std={a.std():.3f}")

        if abs(nll - prev_nll) / (abs(prev_nll) + 1) < tol:
            if verbose:
                log(f"  Converged at iteration {iteration+1}")
            break
        prev_nll = nll

    # Center theta for identifiability
    tm = theta.mean()
    theta -= tm
    b -= tm

    return theta, a, b


# ── Dose-response ──────────────────────────────────────────────────────────

def fit_dose_response_linear(dosage_vals, theta_vals):
    if len(dosage_vals) < 3:
        return np.nan, np.nan, np.nan, np.nan
    slope, intercept, r_value, p_value, std_err = stats.linregress(dosage_vals, theta_vals)
    return intercept, slope, r_value ** 2, p_value


def tost_equivalence(group1, group2, delta):
    if len(group1) < 2 or len(group2) < 2:
        return np.nan, np.nan
    n1, n2 = len(group1), len(group2)
    m1, m2 = np.mean(group1), np.mean(group2)
    s1, s2 = np.var(group1, ddof=1), np.var(group2, ddof=1)
    se = np.sqrt(s1 / n1 + s2 / n2)
    if se < 1e-12:
        se = 1e-12
    diff = m1 - m2
    denom1 = (s1 / n1) ** 2 / max(n1 - 1, 1) + (s2 / n2) ** 2 / max(n2 - 1, 1) + 1e-30
    df = max(((s1 / n1 + s2 / n2) ** 2) / denom1, 1.0)
    t_lower = (diff + delta) / se
    t_upper = (diff - delta) / se
    p_lower = 1.0 - stats.t.cdf(t_lower, df)
    p_upper = stats.t.cdf(t_upper, df)
    return max(p_lower, p_upper), diff


# ── Plotting ───────────────────────────────────────────────────────────────

def plot_dose_response(results, benchmark, out_path):
    fig, ax = plt.subplots(figsize=(8, 5))
    markers = ["o", "s", "^", "D", "v"]
    colors = plt.cm.tab10.colors
    for i, family in enumerate(FAMILIES):
        fdata = [(d, t) for (fam, d, t) in results if fam == family]
        if not fdata:
            continue
        fdata.sort()
        ds, ts = zip(*fdata)
        ax.plot(ds, ts, marker=markers[i % 5], color=colors[i % 10],
                label=family, linewidth=2, markersize=7)
    ax.set_xlabel("Contamination Dosage", fontsize=12)
    ax.set_ylabel(r"IRT Ability ($\theta$)", fontsize=12)
    ax.set_title(f"IRT Dose-Response: {benchmark}", fontsize=14)
    ax.legend(fontsize=10)
    ax.set_xticks([0, 0.05, 0.25, 0.5, 1.0])
    ax.set_xticklabels(["0%", "5%", "25%", "50%", "100%"])
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    log(f"  Plot saved: {out_path}")


# ── Main ───────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="IRT 2PL dose-response fitting")
    parser.add_argument("--base-dir", default="/root/autodl-tmp/exp001/eval_results_v2")
    parser.add_argument("--out-dir", default=None)
    parser.add_argument("--max-iter", type=int, default=30)
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    out_dir = args.out_dir or args.base_dir

    if args.dry_run:
        log("=== DRY RUN: checking data availability ===")
        for benchmark in BENCHMARKS:
            mat, labels, n_items = build_response_matrix(args.base_dir, benchmark)
            if mat is None:
                log(f"  {benchmark}: NO DATA")
                continue
            log(f"  {benchmark}: {mat.shape[0]} respondents x {n_items} items")
            for fam, dos in labels:
                log(f"    {fam}_{dos}")
        return

    all_rows = []

    for benchmark in BENCHMARKS:
        log(f"\n{'='*60}")
        log(f"Benchmark: {benchmark}")
        log(f"{'='*60}")

        mat, labels, n_items = build_response_matrix(args.base_dir, benchmark)
        if mat is None:
            log(f"  MISSING: no data for {benchmark}")
            continue

        log(f"  Fitting 2PL IRT...")
        theta, a, b = fit_2pl(mat, max_iter=args.max_iter, verbose=args.verbose)

        log(f"  Item params: a mean={a.mean():.3f} std={a.std():.3f}, b mean={b.mean():.3f} std={b.std():.3f}")

        theta_map = {}
        dose_data = []
        for idx, (family, dosage) in enumerate(labels):
            dval = DOSAGE_VALUES[dosage]
            theta_map[(family, dosage)] = theta[idx]
            dose_data.append((family, dval, theta[idx]))
            log(f"  {family}_{dosage}: theta = {theta[idx]:.4f}")

        log(f"\n  Linear dose-response (theta = alpha + beta * dosage):")
        family_betas = {}
        for family in FAMILIES:
            fdata = [(DOSAGE_VALUES[d], theta_map[(family, d)])
                     for d in DOSAGES if (family, d) in theta_map]
            if len(fdata) < 3:
                log(f"    {family}: MISSING (< 3 dosage levels)")
                for d in DOSAGES:
                    if (family, d) in theta_map:
                        all_rows.append(dict(
                            benchmark=benchmark, family=family, dosage=d,
                            dosage_val=DOSAGE_VALUES[d], theta=theta_map[(family, d)],
                            beta=np.nan, r2=np.nan, beta_pval=np.nan,
                            tost_p=np.nan, tost_diff=np.nan))
                continue
            ds, ts = zip(*fdata)
            alpha, beta, r2, p_val = fit_dose_response_linear(np.array(ds), np.array(ts))
            family_betas[family] = beta
            log(f"    {family}: beta={beta:.4f} (p={p_val:.4g}), R2={r2:.4f}")

            for d in DOSAGES:
                if (family, d) in theta_map:
                    all_rows.append(dict(
                        benchmark=benchmark, family=family, dosage=d,
                        dosage_val=DOSAGE_VALUES[d], theta=theta_map[(family, d)],
                        beta=beta, r2=r2, beta_pval=p_val,
                        tost_p=np.nan, tost_diff=np.nan))

        # TOST: d000 vs d005 cross-family
        log(f"\n  TOST equivalence (d000 vs d005, cross-family):")
        t_d000 = [theta_map[(f, "d000")] for f in FAMILIES if (f, "d000") in theta_map]
        t_d005 = [theta_map[(f, "d005")] for f in FAMILIES if (f, "d005") in theta_map]
        if len(t_d000) >= 2 and len(t_d005) >= 2:
            pooled_std = np.std(t_d000 + t_d005, ddof=1)
            delta = 0.1 * pooled_std if pooled_std > 0 else 0.01
            tost_p, tost_diff = tost_equivalence(np.array(t_d000), np.array(t_d005), delta)
            log(f"    N_d000={len(t_d000)}, N_d005={len(t_d005)}")
            log(f"    mean_diff={tost_diff:.4f}, delta={delta:.4f}")
            log(f"    TOST p={tost_p:.4g} {'(equivalent)' if tost_p < 0.05 else '(NOT equivalent)'}")
            for row in all_rows:
                if row["benchmark"] == benchmark and row["dosage"] in ("d000", "d005"):
                    row["tost_p"] = tost_p
                    row["tost_diff"] = tost_diff
        else:
            log(f"    SKIP: need >= 2 families with both d000 and d005")

        plot_path = os.path.join(out_dir, f"irt_{benchmark}_dose_response.pdf")
        plot_dose_response(dose_data, benchmark, plot_path)

    # CSV output
    csv_path = os.path.join(out_dir, "irt_dose_response.csv")
    if all_rows:
        header = ["benchmark", "family", "dosage", "dosage_val", "theta",
                  "beta", "r2", "beta_pval", "tost_p", "tost_diff"]
        with open(csv_path, "w") as f:
            f.write(",".join(header) + "\n")
            for row in all_rows:
                f.write(",".join(str(row.get(h, "")) for h in header) + "\n")
        log(f"\nCSV saved: {csv_path}")

    log("\nDone.")


if __name__ == "__main__":
    main()
