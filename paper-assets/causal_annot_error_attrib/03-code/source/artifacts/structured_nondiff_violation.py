#!/usr/bin/env python3
"""
Structured Non-Differential Violation Experiment (K=3, 7 topologies)

Tests sensitivity of naive estimators across 7 causal topologies when the
confusion matrix C varies systematically with the outcome Y.

Mechanism:
  - Baseline C0: diag=0.7, off-diag=0.15 (uniform)
  - Per-rep random Δ: off-diagonal ~ Uniform(-1,1) / L1, col sums = 0
  - C(Y > median) = renormalize(C0 + ε·Δ)
  - C(Y ≤ median) = renormalize(C0 - ε·Δ)
  - Bias measured relative to oracle (same estimator with true A)

For each topology: 500 reps × N=50,000, shared across all ε levels.

Outputs: JSON results + LaTeX table.
"""

import os
import sys
import json
import time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from annot_sensitivity.dgp import GEN_FUNCS, HAS_TREATMENT
from annot_sensitivity.utils import make_dummies

# ─── Config ──────────────────────────────────────────────────
K = 3
TOPOLOGIES = ["confounding", "mediation", "collider", "exposure",
              "mbias", "iv", "frontdoor"]
EPSILONS = [0.01, 0.02, 0.05, 0.10]
N_SAMPLES = 50_000
N_REPS = 500
SEED = 42

DIAG = 0.7
OFF_DIAG = (1.0 - DIAG) / (K - 1)


# ─── Confusion matrix utilities ─────────────────────────────
def make_C0(K, diag=DIAG):
    C = np.full((K, K), (1.0 - diag) / (K - 1))
    np.fill_diagonal(C, diag)
    return C


def make_perturbation_matrix(K, rng):
    """Generate Δ s.t. each column sums to 0."""
    Delta = np.zeros((K, K))
    for col in range(K):
        off_idx = [r for r in range(K) if r != col]
        off = rng.uniform(-1.0, 1.0, size=len(off_idx))
        s = np.abs(off).sum()
        if s > 0:
            off = off / s
        for idx, j in enumerate(off_idx):
            Delta[j, col] = off[idx]
        Delta[col, col] = -off.sum()
    return Delta


def renormalize_stochastic(C):
    Cn = np.maximum(C, 0.0)
    col_sums = Cn.sum(axis=0)
    col_sums = np.where(col_sums > 0, col_sums, 1.0)
    return Cn / col_sums


# ─── Misclassification ──────────────────────────────────────
def misclassify(A_true, C, rng):
    A_star = np.empty_like(A_true)
    for k in range(K):
        mask = (A_true == k)
        n_k = int(mask.sum())
        if n_k > 0:
            A_star[mask] = rng.choice(K, size=n_k, p=C[:, k])
    return A_star


def misclassify_y_dependent(A_true, Y, C_high, C_low, rng):
    med = np.median(Y)
    high = Y > med
    A_star = np.empty_like(A_true)
    for k in range(K):
        m_h = high & (A_true == k)
        m_l = (~high) & (A_true == k)
        if m_h.sum() > 0:
            A_star[m_h] = rng.choice(K, size=int(m_h.sum()), p=C_high[:, k])
        if m_l.sum() > 0:
            A_star[m_l] = rng.choice(K, size=int(m_l.sum()), p=C_low[:, k])
    return A_star


# ─── Naive estimators ───────────────────────────────────────
def estimate_naive(topology, data, A_obs):
    """Returns target coefficient using (possibly misclassified) A_obs."""
    Y = data["Y"]
    N = len(Y)
    D = make_dummies(A_obs, K)

    if topology == "iv":
        Z = data["Z"]
        Zc = Z - Z.mean()
        var_Z = float((Zc ** 2).mean())
        if var_Z < 1e-12:
            return np.nan
        D1c = D[:, 0] - D[:, 0].mean()
        FS = float((Zc * D1c).mean()) / var_Z
        if abs(FS) < 1e-8:
            return np.nan
        RF = float((Zc * (Y - Y.mean())).mean()) / var_Z
        return RF / FS

    if topology == "exposure":
        X = np.column_stack([np.ones(N), D])
    else:
        X = np.column_stack([np.ones(N), data["T"], D])

    try:
        coefs = np.linalg.lstsq(X, Y, rcond=None)[0]
    except np.linalg.LinAlgError:
        return np.nan
    return float(coefs[1])


# ─── Main experiment ────────────────────────────────────────
def run_experiment(n_samples, n_reps):
    rng = np.random.default_rng(SEED)
    C0 = make_C0(K)

    all_results = []

    for topo in TOPOLOGIES:
        print(f"\n{'='*60}")
        print(f"  {topo}")
        print(f"{'='*60}")
        t0 = time.time()

        nondiff_biases = []
        diff_biases = {eps: [] for eps in EPSILONS}
        nondiff_sf = 0
        diff_sf = {eps: 0 for eps in EPSILONS}
        n_valid = 0

        for rep in range(n_reps):
            if n_reps >= 100 and (rep + 1) % 100 == 0:
                print(f"  rep {rep + 1}/{n_reps}")

            # 1. Generate data (shared across nondiff and all diff)
            data = GEN_FUNCS[topo](n_samples, rng=rng)
            A_true = data["A"]
            Y = data["Y"]

            # 2. Oracle estimate
            tau_oracle = estimate_naive(topo, data, A_true)
            if not np.isfinite(tau_oracle):
                continue

            # 3. Non-differential baseline (C0 uniform)
            A_star_nd = misclassify(A_true, C0, rng)
            tau_nd = estimate_naive(topo, data, A_star_nd)
            if not np.isfinite(tau_nd):
                continue

            n_valid += 1
            bias_nd = tau_nd - tau_oracle
            nondiff_biases.append(bias_nd)
            if tau_nd * tau_oracle < 0:
                nondiff_sf += 1

            # 4. Generate per-rep perturbation matrix
            Delta = make_perturbation_matrix(K, rng)

            # 5. Differential for each ε (shared data + Δ)
            for eps in EPSILONS:
                C_high = renormalize_stochastic(C0 + eps * Delta)
                C_low = renormalize_stochastic(C0 - eps * Delta)
                A_star_d = misclassify_y_dependent(A_true, Y, C_high, C_low, rng)
                tau_d = estimate_naive(topo, data, A_star_d)
                if np.isfinite(tau_d):
                    diff_biases[eps].append(tau_d - tau_oracle)
                    if tau_d * tau_oracle < 0:
                        diff_sf[eps] += 1

        elapsed = time.time() - t0
        nd_arr = np.array(nondiff_biases)
        nd_mean = float(nd_arr.mean()) if nd_arr.size else float("nan")
        nd_std = float(nd_arr.std()) if nd_arr.size else float("nan")
        nd_sf_rate = nondiff_sf / max(n_valid, 1)

        print(f"  nondiff: bias={nd_mean:.6f}±{nd_std:.6f}, "
              f"sf={100*nd_sf_rate:.2f}%, n_valid={n_valid}")

        for eps in EPSILONS:
            d_arr = np.array(diff_biases[eps])
            d_mean = float(d_arr.mean()) if d_arr.size else float("nan")
            d_std = float(d_arr.std()) if d_arr.size else float("nan")
            n_d = len(diff_biases[eps])
            d_sf_rate = diff_sf[eps] / max(n_d, 1)

            if abs(nd_mean) > 1e-10 and np.isfinite(nd_mean) and np.isfinite(d_mean):
                rel_dev = abs(d_mean - nd_mean) / abs(nd_mean) * 100
            else:
                rel_dev = float("nan")

            all_results.append({
                "topology": topo,
                "epsilon": eps,
                "bias_nondiff_mean": round(nd_mean, 6),
                "bias_nondiff_std": round(nd_std, 6),
                "bias_diff_mean": round(d_mean, 6),
                "bias_diff_std": round(d_std, 6),
                "relative_deviation_pct": round(rel_dev, 2) if np.isfinite(rel_dev) else None,
                "sign_flip_nondiff": round(nd_sf_rate, 4),
                "sign_flip_diff": round(d_sf_rate, 4),
            })

            print(f"  ε={eps:.2f}: bias_diff={d_mean:.6f}±{d_std:.6f}, "
                  f"dev={rel_dev:.1f}%, sf={100*d_sf_rate:.2f}%")

        print(f"  [{elapsed:.1f}s]")

    return all_results


# ─── Sensitivity ranking ───────────────────────────────────
def compute_ranking(results):
    topo_devs = {}
    for r in results:
        t = r["topology"]
        dev = r["relative_deviation_pct"]
        if dev is not None:
            topo_devs.setdefault(t, []).append(dev)
    avg = {t: float(np.mean(ds)) for t, ds in topo_devs.items()}
    return sorted(avg, key=lambda t: avg[t], reverse=True), avg


# ─── LaTeX table ────────────────────────────────────────────
TOPO_LABELS = {
    "confounding": "Confounding", "mediation": "Mediation",
    "collider": "Collider", "exposure": "Exposure",
    "mbias": "M-bias", "iv": "IV", "frontdoor": "Front-door",
}


def write_latex_table(results, ranking, out_path, n_samples, n_reps):
    n_eps = len(EPSILONS)
    lines = [
        r"\begin{table*}[t]",
        r"\centering",
        r"\small",
        r"\setlength{\tabcolsep}{4pt}",
        (r"\caption{Sensitivity of 7 DAG topologies to structured Y-dependent "
         r"misclassification ($K{=}3$, $\mathrm{diag}(C_0){=}0.70$, "
         "$N{=}" + f"{n_samples:,}$".replace(",", r"{,}") +
         f", ${n_reps}$ reps). "
         r"Bias is relative to oracle (no misclassification). "
         r"Dev.\ $= |\bar{b}_{\mathrm{diff}} - \bar{b}_{\mathrm{nd}}|"
         r"/|\bar{b}_{\mathrm{nd}}|$.}"),
        r"\label{tab:structured_nondiff}",
        r"\begin{tabular}{l" + "rrr" * n_eps + r"}",
        r"\toprule",
    ]

    h1 = "Topology"
    for e in EPSILONS:
        h1 += rf" & \multicolumn{{3}}{{c}}{{$\varepsilon={e}$}}"
    lines.append(h1 + r" \\")

    clines = " ".join(
        rf"\cmidrule(lr){{{2+3*i}-{4+3*i}}}" for i in range(n_eps)
    )
    lines.append(clines)

    h2 = ""
    for _ in EPSILONS:
        h2 += (r" & {\scriptsize $\bar{b}_{\mathrm{d}}$}"
               r" & {\scriptsize Dev\%}"
               r" & {\scriptsize SF\%}")
    lines.append(h2 + r" \\")
    lines.append(r"\midrule")

    for topo in TOPOLOGIES:
        row = TOPO_LABELS[topo]
        for eps in EPSILONS:
            r = next(x for x in results
                     if x["topology"] == topo and x["epsilon"] == eps)
            b = r["bias_diff_mean"]
            rd = r["relative_deviation_pct"]
            sf = 100.0 * r["sign_flip_diff"]
            b_s = f"{b:.4f}" if np.isfinite(b) else "--"
            rd_s = f"{rd:.1f}" if rd is not None else "--"
            sf_s = f"{sf:.1f}" if np.isfinite(sf) else "--"
            row += f" & {b_s} & {rd_s} & {sf_s}"
        lines.append(row + r" \\")

    lines += [r"\bottomrule", r"\end{tabular}"]

    # Ranking footnote
    top3 = ", ".join(TOPO_LABELS[t] for t in ranking[:3])
    lines.append(
        r"\par\smallskip\noindent\textit{Sensitivity ranking (top 3): "
        + top3 + r".}")
    lines += [r"\end{table*}"]

    with open(out_path, "w") as f:
        f.write("\n".join(lines) + "\n")


# ─── NaN-safe JSON serializer ──────────────────────────────
def clean_for_json(o):
    if isinstance(o, (float, np.floating)):
        v = float(o)
        return None if (np.isnan(v) or np.isinf(v)) else v
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    if isinstance(o, dict):
        return {k: clean_for_json(v) for k, v in o.items()}
    if isinstance(o, list):
        return [clean_for_json(v) for v in o]
    return o


# ─── Main ───────────────────────────────────────────────────
def main():
    t_start = time.time()
    out_dir = os.path.dirname(os.path.abspath(__file__))

    dry_run = "--dry-run" in sys.argv
    n_samples = 10_000 if dry_run else N_SAMPLES
    n_reps = 50 if dry_run else N_REPS

    print("=" * 70)
    print("Structured Non-Differential Violation Experiment")
    print("=" * 70)
    if dry_run:
        print("*** DRY-RUN MODE ***")
    print(f"K={K}, N={n_samples:,}, reps={n_reps}, seed={SEED}")
    print(f"Topologies: {TOPOLOGIES}")
    print(f"ε levels: {EPSILONS}")
    print(f"C₀: diag={DIAG}, off-diag={OFF_DIAG:.3f}")

    results = run_experiment(n_samples, n_reps)
    ranking, avg_devs = compute_ranking(results)

    print(f"\n{'='*70}")
    print("SENSITIVITY RANKING (mean relative deviation across ε)")
    print("=" * 70)
    for i, t in enumerate(ranking):
        print(f"  {i+1}. {t:<12} {avg_devs[t]:.1f}%")

    top3 = ranking[:3]
    summary = (
        f"Most sensitive: {', '.join(top3[:3])}. "
        f"Least sensitive: {ranking[-1]}. "
        f"Max single-cell deviation: "
        f"{max(r['relative_deviation_pct'] for r in results if r['relative_deviation_pct'] is not None):.1f}%."
    )

    output = {
        "experiment": "structured_nondiff_violation",
        "K": K,
        "N": n_samples,
        "n_reps": n_reps,
        "epsilons": EPSILONS,
        "C0_diag": DIAG,
        "C0_offdiag": OFF_DIAG,
        "mechanism": (
            "Y-dependent: C_high=renorm(C0+ε·Δ) for Y>median, "
            "C_low=renorm(C0-ε·Δ) for Y≤median; "
            "Δ: per-rep random, off-diag ~ U(-1,1)/L1, col sums=0"),
        "seed": SEED,
        "results": results,
        "sensitivity_ranking": ranking,
        "topology_avg_deviation_pct": avg_devs,
        "summary": summary,
    }

    json_path = os.path.join(out_dir, "structured_nondiff_violation_results.json")
    with open(json_path, "w") as f:
        json.dump(clean_for_json(output), f, indent=2)
    print(f"\nJSON saved to: {json_path}")

    tex_path = os.path.join(out_dir, "structured_nondiff_violation_table.tex")
    write_latex_table(results, ranking, tex_path, n_samples, n_reps)
    print(f"LaTeX saved to: {tex_path}")

    total = time.time() - t_start
    print(f"\nTotal: {total:.1f}s ({total/60:.1f} min)")
    print(f"\n{summary}")


if __name__ == "__main__":
    main()
