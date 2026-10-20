"""Fitting methods for the G-MFRM synthetic recovery experiment.

Four methods of increasing sophistication:
  1. Raw average — naive mean of responses.
  2. MFRM-only — standard 3-facet Rasch via NumPyro MCMC.
  3. Sequential — MFRM then OLS residual regression on exposure.
  4. Joint G-MFRM — full model with contamination term, NumPyro MCMC.

Dependencies: numpy, jax, numpyro, arviz, scipy
"""

import warnings

import arviz as az
import jax
import jax.numpy as jnp
import numpy as np
import numpyro
import numpyro.distributions as dist
from numpyro.infer import MCMC, NUTS
from scipy.special import expit

numpyro.set_host_device_count(2)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _mcmc_diagnostics(mcmc: MCMC) -> tuple[float, float]:
    """Return (max R-hat, min ESS) across all parameters."""
    summary = az.summary(az.from_numpyro(mcmc))
    max_rhat = summary["r_hat"].max()
    min_ess = summary["ess_bulk"].min()
    return float(max_rhat), float(min_ess)


# ---------------------------------------------------------------------------
# Method 1: Raw average
# ---------------------------------------------------------------------------

def fit_raw_average(data: dict) -> dict:
    """Estimate theta as mean response rate per model.

    Args:
        data: Output of generate_gated_mfrm_data().

    Returns:
        Dict with theta_hat (N,), r_hat=NaN, ess=NaN.
    """
    Y = data["responses"].astype(np.float64)
    theta_hat = Y.mean(axis=(1, 2))
    # Center to match identification constraint of MCMC methods
    theta_hat = theta_hat - theta_hat.mean()
    return {"theta_hat": theta_hat, "r_hat": float("nan"), "ess": float("nan")}


# ---------------------------------------------------------------------------
# Method 2: Standard MFRM (no contamination term)
# ---------------------------------------------------------------------------

def _mfrm_model(Y: jnp.ndarray, N: int, I: int, J: int) -> None:
    theta_raw = numpyro.sample("theta_raw", dist.Normal(0, 1).expand([N]))
    theta = numpyro.deterministic("theta", theta_raw - theta_raw.mean())
    b = numpyro.sample("b", dist.Normal(0, 1).expand([I]))
    d = numpyro.sample("d", dist.Normal(0, 0.5).expand([J]))

    logits = theta[:, None, None] - b[None, :, None] - d[None, None, :]
    numpyro.sample("obs", dist.Bernoulli(logits=logits), obs=Y)


def fit_mfrm_only(data: dict) -> dict:
    """Fit standard 3-facet MFRM via NUTS.

    Args:
        data: Output of generate_gated_mfrm_data().

    Returns:
        Dict with theta_hat (N,), r_hat (float), ess (float).
    """
    cfg = data["config"]
    Y = jnp.array(data["responses"], dtype=jnp.float32)

    kernel = NUTS(_mfrm_model)
    mcmc = MCMC(kernel, num_warmup=1000, num_samples=2000, num_chains=2, progress_bar=False)
    mcmc.run(jax.random.PRNGKey(cfg["seed"]), Y=Y, N=cfg["N"], I=cfg["I"], J=cfg["J"])

    samples = mcmc.get_samples()
    theta_hat = np.array(samples["theta"].mean(axis=0))
    max_rhat, min_ess = _mcmc_diagnostics(mcmc)

    return {"theta_hat": theta_hat, "r_hat": max_rhat, "ess": min_ess}


# ---------------------------------------------------------------------------
# Method 3: Sequential (MFRM then OLS residual correction)
# ---------------------------------------------------------------------------

def fit_sequential(data: dict, e_values: np.ndarray) -> dict:
    """Two-step approach: fit MFRM, then regress residuals on exposure.

    Args:
        data: Output of generate_gated_mfrm_data().
        e_values: True item exposure values, shape (I,).

    Returns:
        Dict with theta_hat (N,), r_hat (float), ess (float).
    """
    cfg = data["config"]
    N, I, J = cfg["N"], cfg["I"], cfg["J"]
    Y = data["responses"].astype(np.float64)

    # Step A: single MFRM MCMC — extract theta, b, d from one run
    Y_jnp = jnp.array(data["responses"], dtype=jnp.float32)
    kernel = NUTS(_mfrm_model)
    mcmc = MCMC(kernel, num_warmup=1000, num_samples=2000, num_chains=2, progress_bar=False)
    mcmc.run(jax.random.PRNGKey(cfg["seed"]), Y=Y_jnp, N=N, I=I, J=J)
    samples = mcmc.get_samples()
    theta_mfrm = np.array(samples["theta"].mean(axis=0))
    b_hat = np.array(samples["b"].mean(axis=0))
    d_hat = np.array(samples["d"].mean(axis=0))
    max_rhat, min_ess = _mcmc_diagnostics(mcmc)

    # Step B: residuals
    logits_hat = theta_mfrm[:, None, None] - b_hat[None, :, None] - d_hat[None, None, :]
    pred = expit(logits_hat)
    residuals = Y - pred  # (N, I, J)
    r_ni = residuals.mean(axis=2)  # (N, I) — average over judges

    # Step C: OLS per model — regress r_ni on e_i to get c_hat_n
    c_hat = np.zeros(N)
    e_centered = e_values - e_values.mean()
    e_var = (e_centered**2).sum()
    if e_var > 1e-10:
        for n in range(N):
            c_hat[n] = (r_ni[n] * e_centered).sum() / e_var

    # Step D: adjust theta
    mean_e = e_values.mean()
    theta_seq = theta_mfrm - c_hat * mean_e
    theta_seq = theta_seq - theta_seq.mean()

    return {
        "theta_hat": theta_seq,
        "r_hat": max_rhat,
        "ess": min_ess,
    }


# ---------------------------------------------------------------------------
# Method 4: Joint G-MFRM
# ---------------------------------------------------------------------------

def _gmfrm_model(Y: jnp.ndarray, e: jnp.ndarray, N: int, I: int, J: int) -> None:
    theta_raw = numpyro.sample("theta_raw", dist.Normal(0, 1).expand([N]))
    theta = numpyro.deterministic("theta", theta_raw - theta_raw.mean())
    b = numpyro.sample("b", dist.Normal(0, 1).expand([I]))
    d = numpyro.sample("d", dist.Normal(0, 0.5).expand([J]))
    c = numpyro.sample("c", dist.HalfNormal(0.5).expand([N]))

    logits = (
        theta[:, None, None]
        - b[None, :, None]
        - d[None, None, :]
        + c[:, None, None] * e[None, :, None]
    )
    numpyro.sample("obs", dist.Bernoulli(logits=logits), obs=Y)


def fit_joint_gmfrm(data: dict, e_values: np.ndarray) -> dict:
    """Fit full G-MFRM with contamination term via NUTS.

    Args:
        data: Output of generate_gated_mfrm_data().
        e_values: True item exposure values, shape (I,).

    Returns:
        Dict with theta_hat (N,), c_hat (N,), r_hat (float), ess (float).
    """
    cfg = data["config"]
    Y = jnp.array(data["responses"], dtype=jnp.float32)
    e = jnp.array(e_values, dtype=jnp.float32)

    kernel = NUTS(_gmfrm_model)
    mcmc = MCMC(kernel, num_warmup=1000, num_samples=2000, num_chains=2, progress_bar=False)
    mcmc.run(jax.random.PRNGKey(cfg["seed"]), Y=Y, e=e, N=cfg["N"], I=cfg["I"], J=cfg["J"])

    samples = mcmc.get_samples()
    theta_hat = np.array(samples["theta"].mean(axis=0))
    c_hat = np.array(samples["c"].mean(axis=0))
    max_rhat, min_ess = _mcmc_diagnostics(mcmc)

    return {"theta_hat": theta_hat, "c_hat": c_hat, "r_hat": max_rhat, "ess": min_ess}
