#!/usr/bin/env python3
"""
Dirichlet Prior Subspace Analysis for IV Wald Estimator
========================================================

Companion to mvp_exposure_dirichlet_subspace.py. Stratifies the IV Wald
sign-flip / amplification / violation rates by minimum diagonal of C.

Subspaces:
  - Full space (no diagonal constraint, equiv. Dirichlet(1,1,1) per column)
  - min(diag(C)) >= 0.5
  - min(diag(C)) >= 0.7  (realistic LLM accuracy)
  - min(diag(C)) >= 0.9  (high-accuracy LLM)

IV plim (Wald estimator) under misclassification:
    tau_biased(C) = RF / (C @ FS)[1]
where RF = Cov(Z, Y)/Var(Z), FS_k = Cov(Z, D_k)/Var(Z) precomputed via
2M-sample Monte Carlo from gen_iv() with DEFAULT_PARAMS["iv"].

Definitions (scalar tau):
  - sign_flip:    tau_biased * tau_true < 0
  - amplification: |tau_biased| > |tau_true| AND tau_biased*tau_true > 0
  - violation:    sign_flip OR amplification
  - severity:    |tau_biased / tau_true|
"""

import json
import time
import sys
from pathlib import Path

import numpy as np

PROJ = Path("/home/ubuntu/.agent-ml-research-prod_0510/projects/causal_annot_error_attrib")
sys.path.insert(0, str(PROJ))

from annot_sensitivity.bias import _precompute
from annot_sensitivity.dgp import DEFAULT_PARAMS

K = 3
DIAG_THRESHOLDS = [0.0, 0.5, 0.7, 0.9]
N_SAMPLES = 100_000
SEED = 42


def sample_C_batch(n, K, diag_thresh, rng):
    """Sample n column-stochastic K x K matrices with min(diag) >= diag_thresh.

    Per column: diagonal d ~ truncated Beta(1, K-1) on [diag_thresh, 1]; the
    K-1 off-diagonal entries split the remaining mass (1-d) by a Dirichlet(1,...,1)
    on the (K-2)-simplex (i.e. uniform).
    """
    C = np.empty((n, K, K))
    for col in range(K):
        # Truncated Beta(1, K-1): density propto (1-d)^(K-2), inverse CDF:
        # d = 1 - (1 - diag_thresh) * U^{1/(K-1)} where U ~ Uniform(0,1).
        U = rng.uniform(size=n)
        d = 1.0 - (1.0 - diag_thresh) * U ** (1.0 / (K - 1))
        rem = 1.0 - d
        # Uniform split of `rem` across the K-1 off-diagonal slots.
        if K == 2:
            off_alpha = np.ones((n, 1))
        else:
            off_alpha = rng.dirichlet(np.ones(K - 1), size=n)
        off_rows = [r for r in range(K) if r != col]
        C[:, col, col] = d
        for j, r in enumerate(off_rows):
            C[:, r, col] = rem * off_alpha[:, j]
    return C


def analyze(C_batch, FS, RF, tau_true):
    """Compute Wald plim for a batch of confusion matrices and tally events."""
    # (C @ FS)[1] for each C: shape (n,)
    FS_star = C_batch @ FS         # (n, K)
    denom = FS_star[:, 1]          # (n,)

    valid = np.abs(denom) > 1e-15
    n_valid = int(valid.sum())

    tau_biased = np.full(C_batch.shape[0], np.nan)
    tau_biased[valid] = RF / denom[valid]

    sign_flip = valid & (tau_biased * tau_true < 0)
    amp = valid & (np.abs(tau_biased) > np.abs(tau_true)) & (tau_biased * tau_true > 0)
    violation = sign_flip | amp

    sev = np.full(C_batch.shape[0], 0.0)
    sev[valid] = np.abs(tau_biased[valid] / tau_true)
    worst_idx = int(np.argmax(sev * violation))    # zero severity if not violating
    worst_sev = float(sev[worst_idx]) if violation[worst_idx] else 0.0
    worst_C = C_batch[worst_idx].copy() if violation[worst_idx] else None
    worst_tau = float(tau_biased[worst_idx]) if violation[worst_idx] else float("nan")

    return {
        "n_valid": n_valid,
        "n_sign_flip": int(sign_flip.sum()),
        "n_amp": int(amp.sum()),
        "n_violation": int(violation.sum()),
        "sign_flip_rate": float(sign_flip.sum() / n_valid) if n_valid else 0.0,
        "amplification_rate": float(amp.sum() / n_valid) if n_valid else 0.0,
        "violation_rate": float(violation.sum() / n_valid) if n_valid else 0.0,
        "worst_severity": worst_sev,
        "worst_C": worst_C.tolist() if worst_C is not None else None,
        "worst_tau_biased": worst_tau,
    }


def main():
    t0 = time.time()
    rng = np.random.default_rng(SEED)

    print("=" * 85)
    print("Dirichlet Subspace Analysis: IV Wald Estimator Sign-Flip / Amplification")
    print("=" * 85)

    params = DEFAULT_PARAMS["iv"]
    stats = _precompute("iv", params, K)
    FS = stats["FS"]
    RF = stats["RF"]
    tau_true = float(RF / FS[1])

    print(f"DGP: gen_iv() with DEFAULT_PARAMS['iv'] (Z~N(0,1), U~N(0,1), K={K})")
    print(f"  dZ = {params['dZ']}")
    print(f"  dU = {params['dU']}")
    print(f"  beta = {params['beta']}")
    print(f"Precomputed (N=2,000,000):")
    print(f"  RF = {RF:.6f}")
    print(f"  FS = {FS}")
    print(f"  tau_true (Wald, C=I) = {tau_true:.6f}")
    print(f"Samples per subspace: {N_SAMPLES:,}\n")

    header = f"{'Subspace':>12} {'N_valid':>8} {'Viol%':>8} {'SignFlip%':>10} {'Amp%':>8} {'WorstSev':>9} {'Time':>7}"
    print(header)
    print("-" * len(header))

    out = {
        "topology": "iv",
        "K": K,
        "n_samples_per_threshold": N_SAMPLES,
        "seed": SEED,
        "dgp": {
            "dZ": list(map(float, params["dZ"])),
            "dU": list(map(float, params["dU"])),
            "beta": list(map(float, params["beta"])),
            "g": list(map(float, params["g"])),
            "lam": float(params["lam"]),
        },
        "precomputed": {
            "RF": float(RF),
            "FS": list(map(float, FS)),
            "tau_true": tau_true,
        },
        "thresholds": {},
    }

    for thresh in DIAG_THRESHOLDS:
        ts = time.time()
        C_batch = sample_C_batch(N_SAMPLES, K, thresh, rng)
        res = analyze(C_batch, FS, RF, tau_true)
        dt = time.time() - ts
        label = f"diag>={thresh:.1f}" if thresh > 0 else "full"
        print(f"{label:>12} {res['n_valid']:>8,} "
              f"{100*res['violation_rate']:>7.2f}% "
              f"{100*res['sign_flip_rate']:>9.2f}% "
              f"{100*res['amplification_rate']:>7.2f}% "
              f"{res['worst_severity']:>9.2f} {dt:>6.1f}s")
        out["thresholds"][f"{thresh:.1f}"] = res

    # Worst-case display
    print("\n" + "=" * 85)
    print("Worst-case C per subspace (max |tau_biased / tau_true|, conditional on violation)")
    print("=" * 85)
    for thresh in DIAG_THRESHOLDS:
        res = out["thresholds"][f"{thresh:.1f}"]
        label = f"diag>={thresh:.1f}" if thresh > 0 else "full"
        if res["worst_C"] is None:
            print(f"\n{label}: no violations found")
            continue
        C_w = np.array(res["worst_C"])
        print(f"\n{label}: severity={res['worst_severity']:.3f}, "
              f"tau_biased={res['worst_tau_biased']:.4f} (tau_true={tau_true:.4f})")
        for row in C_w:
            print("  [" + "  ".join(f"{v:.3f}" for v in row) + "]")

    elapsed = time.time() - t0
    print(f"\nTotal runtime: {elapsed:.1f}s")

    out_path = PROJ / "artifacts" / "iv_dirichlet_subspace_results.json"
    out_path.write_text(json.dumps(out, indent=2))
    print(f"\nWrote: {out_path}")


if __name__ == "__main__":
    main()
