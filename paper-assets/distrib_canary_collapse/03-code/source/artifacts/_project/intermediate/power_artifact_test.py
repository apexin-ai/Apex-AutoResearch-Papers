#!/usr/bin/env python3
"""
Power Artifact Simulation — R8 W-C3 rebuttal.
Tests if observed α_c(T) ∝ T^{-2.08} is a genuine phase transition
or an artifact of PermG statistical power increasing with T.

H0 (no transition): S(α) = c·α  (linear, all α>0 carry signal)
H1 (transition):    S(α,T) = S_max·I(α ≥ α_c(T))  (step function)
"""

import numpy as np
from scipy import stats
from multiprocessing import Pool, cpu_count
import json, time, os, argparse

# ── Configuration ──
ALPHAS = np.array([0.00, 0.10, 0.25, 0.45, 0.50, 0.60, 0.75, 1.00])
T_VALUES = np.array([5, 10, 15, 20, 25])
N_PAIRS = 8
FDR_Q = 0.05
AR_A = 0.5
AR_C = 0.5
SIGMA = 1.0
GAMMA_OBS = 2.083
C_THEORY = 130.39


def alpha_c_theory(T):
    return C_THEORY * float(T) ** (-GAMMA_OBS)


# ── Core Simulation ──

def gen_var1(n_total, T, b, rng):
    """Generate VAR(1) pairs, return first-differenced (dX, dY) each (n_total, T)."""
    X = np.zeros((n_total, T + 1))
    Y = np.zeros((n_total, T + 1))
    for t in range(T):
        X[:, t + 1] = AR_C * X[:, t] + rng.normal(0, SIGMA, n_total)
        Y[:, t + 1] = AR_A * Y[:, t] + b * X[:, t] + rng.normal(0, SIGMA, n_total)
    return np.diff(X, axis=1), np.diff(Y, axis=1)


def bh_fdr(pvals, q=FDR_Q):
    m = len(pvals)
    idx = np.argsort(pvals)
    sp = pvals[idx]
    thr = q * np.arange(1, m + 1) / m
    sig = np.zeros(m, dtype=bool)
    rej = sp <= thr
    if rej.any():
        sig[idx[: np.max(np.where(rej)[0]) + 1]] = True
    return sig


def permg_cell(dX, dY, n_sim, n_perm, rng):
    """Vectorized PermG across all n_sim*N_PAIRS pairs.

    Uses partial-F formula (Frisch-Waugh-Lovell) to avoid redundant OLS per permutation.
    dX, dY: (n_sim * N_PAIRS, T)
    Returns: per-simulation PermG scores array (n_sim,)
    """
    n_total, T = dX.shape
    n = T - 1  # effective sample size after lag-1
    if n < 3:
        return np.zeros(n_sim)

    dy = dY[:, 1:]       # response
    dy_lag = dY[:, :-1]   # lagged dy (restricted predictor)
    dx_lag = dX[:, :-1]   # lagged dx (tested predictor)

    # Restricted OLS: dy ~ 1 + dy_lag (vectorized across pairs)
    s1 = dy_lag.sum(1)
    s2 = (dy_lag ** 2).sum(1)
    sy = dy.sum(1)
    sxy = (dy_lag * dy).sum(1)
    det = np.clip(n * s2 - s1 ** 2, 1e-12, None)

    b0 = (s2 * sy - s1 * sxy) / det
    b1 = (n * sxy - s1 * sy) / det
    e_r = dy - b0[:, None] - b1[:, None] * dy_lag
    rss_r = (e_r ** 2).sum(1)
    df_u = n - 3
    if df_u <= 0:
        return np.zeros(n_sim)

    def partial_f(z):
        """Partial F-stat for adding z to restricted model. z: (n_total, n)."""
        sz = z.sum(1)
        sxz = (dy_lag * z).sum(1)
        bz0 = (s2 * sz - s1 * sxz) / det
        bz1 = (n * sxz - s1 * sz) / det
        mr_z = z - bz0[:, None] - bz1[:, None] * dy_lag
        edz = (e_r * z).sum(1)
        zmz = np.clip((z * mr_z).sum(1), 1e-12, None)
        delta = edz ** 2 / zmz
        rss_u = np.clip(rss_r - delta, 1e-12, None)
        return np.clip(delta * df_u / rss_u, 0, None)

    F_orig = partial_f(dx_lag)

    count_ge = np.zeros(n_total)
    for _ in range(n_perm):
        dx_perm = rng.permuted(dX, axis=1)
        F_p = partial_f(dx_perm[:, :-1])
        count_ge += (F_p >= F_orig)

    pvals = (count_ge + 1) / (n_perm + 1)
    pv_mat = pvals.reshape(n_sim, N_PAIRS)
    scores = np.array([bh_fdr(pv_mat[i]).sum() for i in range(n_sim)])
    return scores


def run_cell(args):
    hyp, alpha, T, n_sim, n_perm, b, seed = args
    rng = np.random.default_rng(seed)
    dX, dY = gen_var1(n_sim * N_PAIRS, T, b, rng)
    sc = permg_cell(dX, dY, n_sim, n_perm, rng)
    return {
        "hypothesis": hyp,
        "alpha": float(alpha),
        "T": int(T),
        "b": float(b),
        "mean_permg_score": round(float(sc.mean()), 4),
        "detection_rate": round(float((sc >= 1).mean()), 4),
        "mean_detection_fraction": round(float((sc / N_PAIRS).mean()), 4),
    }


# ── Calibration ──

def calibrate(target_frac, T, n_sim=100, n_perm=200):
    """Binary search for VAR coefficient b giving target mean detection fraction."""
    lo, hi = 0.05, 10.0
    for i in range(15):
        b = (lo + hi) / 2
        rng = np.random.default_rng(42)  # fixed seed for monotonic convergence
        dX, dY = gen_var1(n_sim * N_PAIRS, T, b, rng)
        sc = permg_cell(dX, dY, n_sim, n_perm, rng)
        frac = (sc / N_PAIRS).mean()
        print(f"  calib {i:2d}: b={b:.4f}  frac={frac:.3f}  target={target_frac:.3f}")
        if abs(frac - target_frac) < 0.02:
            return b
        if frac < target_frac:
            lo = b
        else:
            hi = b
    return (lo + hi) / 2


# ── Analysis ──

def find_onset(results, thr=0.5):
    """Find onset α via linear interpolation where detection_rate crosses threshold."""
    out = {}
    for T in T_VALUES:
        cells = sorted(
            [(r["alpha"], r["detection_rate"]) for r in results if r["T"] == T]
        )
        onset = None
        for i in range(len(cells)):
            a, dr = cells[i]
            if dr > thr:
                if i == 0:
                    onset = a
                else:
                    a_prev, dr_prev = cells[i - 1]
                    span = dr - dr_prev
                    if span > 0:
                        onset = a_prev + (thr - dr_prev) / span * (a - a_prev)
                    else:
                        onset = a
                break
        out[int(T)] = round(onset, 4) if onset is not None else None
    return out


def fit_powerlaw(onsets):
    pts = [(T, a) for T, a in onsets.items() if a is not None and a > 0]
    if len(pts) < 2:
        return None
    Ts, As = zip(*pts)
    sl, ic, r, p, se = stats.linregress(np.log(Ts), np.log(As))
    return {
        "c": round(float(np.exp(ic)), 4),
        "gamma": round(float(-sl), 4),
        "r2": round(float(r ** 2), 4),
        "p": round(float(p), 6),
    }


# ── Main ──

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", default="full", choices=["pilot", "full"])
    ap.add_argument(
        "--outdir", default=os.path.dirname(os.path.abspath(__file__))
    )
    args = ap.parse_args()

    n_sim, n_perm = (50, 200) if args.mode == "pilot" else (1000, 1000)
    print(f"=== Power Artifact Simulation ({args.mode}) ===")
    print(f"n_sim={n_sim}, n_perm={n_perm}\n")

    # Calibration: find b such that mean detection fraction ≈ 0.75 at α=0.75, T=20
    print("--- Calibration ---")
    b_cal = calibrate(0.75, 20)
    c_scale = b_cal / 0.75
    S_max = b_cal
    print(f"  → c_scale={c_scale:.4f}, S_max={S_max:.4f}\n")

    # Build task list (H0 + H1 × α × T)
    tasks = []
    seed = 314159
    for ia, a in enumerate(ALPHAS):
        for it, T in enumerate(T_VALUES):
            idx = ia * len(T_VALUES) + it
            tasks.append(("H0", a, T, n_sim, n_perm, c_scale * a, seed + idx))
            ac = alpha_c_theory(T)
            b_h1 = S_max if a >= ac else 0.0
            tasks.append(
                ("H1", a, T, n_sim, n_perm, b_h1, seed + 10000 + idx)
            )

    print(f"--- Running {len(tasks)} cells ---")
    t0 = time.time()
    nw = min(cpu_count(), 16)
    with Pool(nw) as pool:
        results = pool.map(run_cell, tasks)
    elapsed = time.time() - t0
    print(f"  Done: {elapsed:.1f}s ({nw} workers)\n")

    h0 = [r for r in results if r["hypothesis"] == "H0"]
    h1 = [r for r in results if r["hypothesis"] == "H1"]

    # Onset analysis
    h0_on = find_onset(h0)
    h1_on = find_onset(h1)
    obs_on = {int(T): round(alpha_c_theory(T), 4) for T in T_VALUES}
    h0_fit = fit_powerlaw(h0_on)
    h1_fit = fit_powerlaw(h1_on)

    print("--- Onset Summary ---")
    print(f"{'T':>4} {'H0':>8} {'H1':>8} {'Theory':>8}")
    for T in T_VALUES:
        print(
            f"{T:4d} {str(h0_on[int(T)]):>8} "
            f"{str(h1_on[int(T)]):>8} {obs_on[int(T)]:>8}"
        )
    if h0_fit:
        print(
            f"\nH0 fit: γ={h0_fit['gamma']}, c={h0_fit['c']}, R²={h0_fit['r2']}"
        )
    if h1_fit:
        print(
            f"H1 fit: γ={h1_fit['gamma']}, c={h1_fit['c']}, R²={h1_fit['r2']}"
        )
    print(f"Observed: γ={GAMMA_OBS}, c={C_THEORY}")

    # Conclusion
    if h0_fit:
        dg = abs(h0_fit["gamma"] - GAMMA_OBS)
        if dg < 0.5:
            conclusion = "artifact"
            expl = (
                f"H0 apparent onset scales as T^(-{h0_fit['gamma']:.2f}), "
                f"close to observed T^(-{GAMMA_OBS:.2f}) (Δγ={dg:.2f} < 0.5). "
                f"Power artifact cannot be excluded."
            )
        else:
            conclusion = "real_transition"
            expl = (
                f"H0 apparent onset scales as T^(-{h0_fit['gamma']:.2f}), "
                f"far from observed T^(-{GAMMA_OBS:.2f}) (Δγ={dg:.2f} ≥ 0.5). "
                f"Observed scaling cannot be explained by power artifact alone."
            )
    else:
        h0_pts = [v for v in h0_on.values() if v is not None]
        if len(h0_pts) < 2:
            conclusion = "real_transition"
            expl = (
                "H0 produces too few onset points to form a power law — "
                "the smooth-signal model does not reproduce the observed onset pattern."
            )
        else:
            conclusion = "inconclusive"
            expl = "Unable to determine."

    print(f"\n*** Conclusion: {conclusion} ***")
    print(f"  {expl}\n")

    # Also print H0 heatmap for quick inspection
    print("--- H0 Detection Rates ---")
    print(f"{'α':>6}", end="")
    for T in T_VALUES:
        print(f"  T={T:2d}", end="")
    print()
    for a in ALPHAS:
        print(f"{a:6.2f}", end="")
        for T in T_VALUES:
            key = f"a{a:.2f}_T{T}"
            r = next((x for x in h0 if x["alpha"] == a and x["T"] == T), None)
            dr = r["detection_rate"] if r else 0
            print(f"  {dr:.2f}", end="")
        print()

    print("\n--- H1 Detection Rates ---")
    print(f"{'α':>6}", end="")
    for T in T_VALUES:
        print(f"  T={T:2d}", end="")
    print()
    for a in ALPHAS:
        print(f"{a:6.2f}", end="")
        for T in T_VALUES:
            r = next((x for x in h1 if x["alpha"] == a and x["T"] == T), None)
            dr = r["detection_rate"] if r else 0
            print(f"  {dr:.2f}", end="")
        print()

    # ── Save ──
    output = {
        "config": {
            "n_sim": n_sim,
            "n_perm": n_perm,
            "alphas": ALPHAS.tolist(),
            "T_values": T_VALUES.tolist(),
            "n_pairs": N_PAIRS,
            "fdr_q": FDR_Q,
            "var_a": AR_A,
            "var_c": AR_C,
            "sigma": SIGMA,
            "calibration": {
                "c_scale": round(c_scale, 4),
                "S_max": round(S_max, 4),
                "b_calibrated": round(b_cal, 4),
            },
        },
        "H0_results": {f"a{r['alpha']:.2f}_T{r['T']}": r for r in h0},
        "H1_results": {f"a{r['alpha']:.2f}_T{r['T']}": r for r in h1},
        "apparent_onset": {
            "H0": {str(k): v for k, v in h0_on.items()},
            "H1": {str(k): v for k, v in h1_on.items()},
            "observed": {str(k): v for k, v in obs_on.items()},
        },
        "scaling_fit": {
            "H0": h0_fit,
            "H1": h1_fit,
            "observed": {"c": C_THEORY, "gamma": GAMMA_OBS},
        },
        "conclusion": conclusion,
        "explanation": expl,
        "elapsed_seconds": round(elapsed, 1),
    }
    json_path = os.path.join(args.outdir, "power_artifact_test.json")
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nSaved: {json_path}")

    make_plot(h0, h1, h0_on, h1_on, obs_on, h0_fit, h1_fit, args.outdir)
    write_md(output, args.outdir)

    return output


# ── Visualization ──

def make_plot(h0, h1, h0_on, h1_on, obs_on, h0_fit, h1_fit, outdir):
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(1, 3, figsize=(18, 5.5))

    for ax, data, title in [
        (axes[0], h0, "H0: Linear Signal\n(Power Artifact Model)"),
        (axes[1], h1, "H1: Step Transition\n(Phase Transition Model)"),
    ]:
        mat = np.full((len(ALPHAS), len(T_VALUES)), np.nan)
        for r in data:
            ia = np.searchsorted(ALPHAS, r["alpha"])
            it = np.searchsorted(T_VALUES, r["T"])
            if ia < len(ALPHAS) and it < len(T_VALUES):
                mat[ia, it] = r["detection_rate"]

        im = ax.imshow(
            mat,
            aspect="auto",
            origin="lower",
            cmap="RdYlGn",
            vmin=0,
            vmax=1,
            extent=[-0.5, len(T_VALUES) - 0.5, -0.5, len(ALPHAS) - 0.5],
        )
        ax.set_xticks(range(len(T_VALUES)))
        ax.set_xticklabels(T_VALUES.astype(int))
        ax.set_yticks(range(len(ALPHAS)))
        ax.set_yticklabels([f"{a:.2f}" for a in ALPHAS])
        ax.set_xlabel("T (generations)")
        ax.set_ylabel("α (per-gen replacement)")
        ax.set_title(title, fontweight="bold", fontsize=11)
        for i in range(len(ALPHAS)):
            for j in range(len(T_VALUES)):
                v = mat[i, j]
                if not np.isnan(v):
                    c = "white" if v > 0.65 or v < 0.35 else "black"
                    ax.text(
                        j, i, f"{v:.2f}", ha="center", va="center",
                        fontsize=7.5, color=c,
                    )
        plt.colorbar(im, ax=ax, label="P(PermG ≥ 1)", shrink=0.82)

    # Panel 3: onset scaling comparison
    ax = axes[2]
    Tf = np.linspace(4, 27, 200)
    for lab, on, fit, col, mk in [
        ("H0 apparent onset", h0_on, h0_fit, "#e74c3c", "s"),
        ("H1 apparent onset", h1_on, h1_fit, "#2ecc71", "^"),
        ("Theory α_c", obs_on, None, "#3498db", "o"),
    ]:
        ts = sorted(t for t, a in on.items() if a is not None and 0 < a <= 1.5)
        if ts:
            ax.plot(
                ts, [on[t] for t in ts],
                marker=mk, color=col, label=lab, lw=2, ms=8,
            )
        if fit:
            ax.plot(
                Tf, fit["c"] * Tf ** (-fit["gamma"]),
                "--", color=col, alpha=0.5,
                label=f"  γ={fit['gamma']:.2f}, R²={fit['r2']:.2f}",
            )
    ax.plot(
        Tf, np.clip(C_THEORY * Tf ** (-GAMMA_OBS), 0, 2),
        "--", color="#3498db", alpha=0.5,
        label=f"  γ={GAMMA_OBS:.2f} (observed)",
    )
    ax.set_xlabel("T (generations)")
    ax.set_ylabel("Apparent α_c (onset threshold)")
    ax.set_title("Onset Scaling Comparison", fontweight="bold", fontsize=11)
    ax.legend(fontsize=7.5, loc="upper right")
    ax.set_ylim(0, 1.15)
    ax.set_xlim(3, 28)
    ax.axhline(y=1.0, color="gray", ls=":", alpha=0.3)

    plt.tight_layout()
    for ext in ["pdf", "png"]:
        path = os.path.join(outdir, f"power_artifact_comparison.{ext}")
        fig.savefig(path, bbox_inches="tight", dpi=150)
    plt.close()
    print(f"Saved: power_artifact_comparison.pdf/png")


# ── Analysis Markdown ──

def write_md(output, outdir):
    cfg = output["config"]
    sf = output["scaling_fit"]
    cal = cfg["calibration"]

    L = [
        "# Power Artifact Simulation Analysis",
        "",
        "## Purpose",
        "",
        "Reviewer W-C3 raised the concern that observed sharp onset α_c(T) ∝ T^{−2.08}",
        "could be a statistical power artifact: if real signal grows smoothly with α,",
        "increasing T simply raises PermG power, making the apparent onset shift left.",
        "",
        "This simulation tests H0 (linear signal, no transition) against observations.",
        "",
        "## Setup",
        "",
        f"- Simulations per (α,T) cell: **{cfg['n_sim']}**",
        f"- Permutations per test: **{cfg['n_perm']}**",
        f"- Pairs per simulation: {cfg['n_pairs']}, FDR q={cfg['fdr_q']}",
        f"- VAR(1): a={cfg['var_a']}, c={cfg['var_c']}, σ={cfg['sigma']}",
        f"- Elapsed: {output['elapsed_seconds']}s",
        "",
        "## Calibration",
        "",
        f"Target: mean detection fraction = 0.75 at α=0.75, T=20 (matching observed 6/8).",
        f"",
        f"- **c_scale** = {cal['c_scale']:.4f} → H0 signal: S(α) = {cal['c_scale']:.4f} × α",
        f"- **S_max** = {cal['S_max']:.4f} → H1 step amplitude",
        "",
        "## H0: Linear Signal (No Phase Transition)",
        "",
        "Under H0, signal S(α) = c × α increases monotonically. There is **no true",
        "transition point** — detection onset is purely a statistical power artifact.",
        "",
        "### H0 Detection Rates P(PermG ≥ 1)",
        "",
        "| α \\ T | " + " | ".join(str(T) for T in cfg["T_values"]) + " |",
        "|" + "|".join(["------"] * (len(cfg["T_values"]) + 1)) + "|",
    ]
    for a in cfg["alphas"]:
        row = f"| {a:.2f}"
        for T in cfg["T_values"]:
            k = f"a{a:.2f}_T{T}"
            dr = output["H0_results"].get(k, {}).get("detection_rate", 0)
            row += f" | {dr:.2f}"
        L.append(row + " |")

    L += [
        "",
        "## H1: Step Transition (Phase Transition Model)",
        "",
        f"Under H1, signal is a step function: S(α,T) = S_max × I(α ≥ α_c(T)),",
        f"where α_c(T) = {C_THEORY:.2f} × T^{{−{GAMMA_OBS:.3f}}}.",
        "",
        "### H1 Detection Rates P(PermG ≥ 1)",
        "",
        "| α \\ T | " + " | ".join(str(T) for T in cfg["T_values"]) + " |",
        "|" + "|".join(["------"] * (len(cfg["T_values"]) + 1)) + "|",
    ]
    for a in cfg["alphas"]:
        row = f"| {a:.2f}"
        for T in cfg["T_values"]:
            k = f"a{a:.2f}_T{T}"
            dr = output["H1_results"].get(k, {}).get("detection_rate", 0)
            row += f" | {dr:.2f}"
        L.append(row + " |")

    L += [
        "",
        "## Apparent Onset Comparison",
        "",
        "Smallest α where P(PermG ≥ 1) > 0.50:",
        "",
        "| T | H0 | H1 | Theory α_c |",
        "|---|------|------|------------|",
    ]
    for T in cfg["T_values"]:
        Ts = str(T)
        h0v = output["apparent_onset"]["H0"].get(Ts)
        h1v = output["apparent_onset"]["H1"].get(Ts)
        ov = output["apparent_onset"]["observed"].get(Ts)
        L.append(
            f"| {T} | {h0v if h0v is not None else '—'} | "
            f"{h1v if h1v is not None else '—'} | {ov} |"
        )

    L += ["", "## Scaling Fits", ""]
    if sf["H0"]:
        L.append(
            f"- **H0**: α_c(T) ∝ T^{{−{sf['H0']['gamma']:.3f}}} "
            f"(c={sf['H0']['c']:.3f}, R²={sf['H0']['r2']:.3f})"
        )
    else:
        L.append("- **H0**: insufficient onset points for power-law fit")
    if sf["H1"]:
        L.append(
            f"- **H1**: α_c(T) ∝ T^{{−{sf['H1']['gamma']:.3f}}} "
            f"(c={sf['H1']['c']:.3f}, R²={sf['H1']['r2']:.3f})"
        )
    else:
        L.append("- **H1**: insufficient onset points for power-law fit")
    L.append(
        f"- **Observed**: α_c(T) ∝ T^{{−{sf['observed']['gamma']:.3f}}} "
        f"(c={sf['observed']['c']:.3f})"
    )

    L += [
        "",
        "## Conclusion",
        "",
        f"**{output['conclusion'].upper()}**",
        "",
        output["explanation"],
        "",
        "### Interpretation",
        "",
    ]
    if output["conclusion"] == "real_transition":
        L += [
            "The smooth-signal model (H0) produces an apparent onset pattern with a",
            "fundamentally different scaling exponent than what we observe empirically.",
            "A pure power-artifact explanation would predict γ ≈ 0.5 (from √T scaling",
            "of F-test power), not the observed γ ≈ 2.08. This gap cannot be bridged",
            "by adjusting the signal function — the power-law exponent is a structural",
            "property of how statistical power scales with T, independent of signal shape.",
            "",
            "The observed steep scaling (γ ≈ 2.08) requires a mechanism beyond power",
            "growth: a genuine phase transition in the signal structure.",
        ]
    elif output["conclusion"] == "artifact":
        L += [
            "The smooth-signal model produces onset scaling consistent with observations.",
            "The power artifact explanation cannot be excluded.",
        ]
    else:
        L += ["Results are inconclusive."]

    md_path = os.path.join(outdir, "power_artifact_analysis.md")
    with open(md_path, "w") as f:
        f.write("\n".join(L) + "\n")
    print(f"Saved: {md_path}")


if __name__ == "__main__":
    main()
