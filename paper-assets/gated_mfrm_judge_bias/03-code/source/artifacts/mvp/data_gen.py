"""Synthetic data generation for Gated Multi-Facet Rasch Model (G-MFRM).

Generates binary response tensors Y[n,i,j] from the model:
    logit(P_nij) = theta_n - b_i - d_j + c_n * e_i * (1 + s_j)

Two confounding mechanisms controlled by rho:
  A) Item-level: e_i correlated with -b_i (easy items get high exposure).
  B) Judge-level: s_j (contamination sensitivity) correlated with -d_j
     (strict judges dampen contamination signal), so d̂_j absorbs part of
     the c_n·e_i effect when contamination is unmodeled.

Dependencies: numpy, scipy
"""

import numpy as np
from scipy.special import expit


def generate_gated_mfrm_data(
    N: int = 20,
    I: int = 100,
    J: int = 5,
    rho: float = 0.3,
    seed: int = 42,
) -> dict:
    """Generate synthetic G-MFRM data with item-level and judge-level confounding.

    Args:
        N: Number of models (examinees).
        I: Number of items.
        J: Number of judges.
        rho: Controls both confounding strengths: (A) corr(e_i, -b_i) for
             item-level and (B) corr(s_j, -d_j) for judge-level.
        seed: Random seed for reproducibility.

    Returns:
        Dict with keys:
            responses: (N, I, J) binary numpy array.
            true_params: dict of theta (N,), b (I,), d (J,), c (N,), e (I,), s (J,).
            config: dict of N, I, J, rho, seed.
    """
    rng = np.random.default_rng(seed)

    theta = rng.standard_normal(N)
    b = rng.standard_normal(I)
    d = rng.normal(0, 0.5, size=J)
    c = np.abs(rng.normal(0, 0.5, size=N))

    # Confounding A (item-level): e_i correlated with -b_i (easy items get high exposure)
    b_std = b.std()
    if b_std < 1e-8:
        b_std = 1.0
    z = rng.standard_normal(I)
    e_raw = rho * (-b / b_std) + np.sqrt(1 - rho**2) * z
    e = expit(e_raw)  # map to [0, 1]

    # Confounding B (judge-level): s_j correlated with -d_j
    # Strict judges (high d_j) get negative s_j → dampen contamination signal
    d_std = d.std()
    if d_std < 1e-8:
        d_std = 1.0
    z_s = rng.standard_normal(J)
    s = 0.3 * (-rho * (d / d_std) + np.sqrt(1 - rho**2) * z_s)

    # logit(P_nij) = theta_n - b_i - d_j + c_n * e_i * (1 + s_j)
    contamination = c[:, None, None] * e[None, :, None] * (1.0 + s[None, None, :])
    logits = (
        theta[:, None, None]
        - b[None, :, None]
        - d[None, None, :]
        + contamination
    )
    probs = expit(logits)
    responses = rng.binomial(1, probs).astype(np.int8)

    return {
        "responses": responses,
        "true_params": {
            "theta": theta,
            "b": b,
            "d": d,
            "c": c,
            "e": e,
            "s": s,
        },
        "config": {"N": N, "I": I, "J": J, "rho": rho, "seed": seed},
    }
