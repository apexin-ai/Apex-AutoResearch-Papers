"""Data generation processes for 7 DAG topologies.

Each topology generates synthetic data with a known causal structure.
The variable A (or M for frontdoor) is the one subject to misclassification.
"""

import numpy as np
from .utils import softmax_sample, make_dummies

DEFAULT_PARAMS = {
    "confounding": dict(
        p_A=np.array([0.40, 0.35, 0.25]),
        alpha=np.array([1.5, -1.0]),
        beta_A=np.array([1.0, -0.5]),
        beta_T=2.0, sigma_T=1.0),
    "mediation": dict(
        tau=0.5,
        gamma=np.array([0.0, 0.5, -0.3]),
        delta=np.array([0.0, 0.8, -0.6]),
        beta=np.array([0.0, 1.0, -0.5])),
    "collider": dict(
        tau=1.0,
        g=np.array([0.0, 0.0, 0.0]),
        dT=np.array([0.0, 0.5, -0.3]),
        dY=np.array([0.0, 0.8, 0.6])),
    "exposure": dict(
        beta=np.array([0.0, 1.0, -0.5]),
        p_A=np.array([0.40, 0.35, 0.25])),
    "mbias": dict(
        tau=1.0, delta_coef=1.0, lam=1.0,
        g=np.array([0.0, 0.0, 0.0]),
        a1=np.array([0.0, 0.8, -0.5]),
        a2=np.array([0.0, 0.6, 0.9])),
    "iv": dict(
        lam=1.0,
        g=np.array([0.0, 0.0, 0.0]),
        dZ=np.array([0.0, 1.0, -0.5]),
        dU=np.array([0.0, 0.8, 0.6]),
        beta=np.array([0.0, 1.0, -0.5])),
    "frontdoor": dict(
        alpha_U=1.0, lam_U=1.0,
        gamma=np.array([0.0, 0.5, -0.3]),
        delta=np.array([0.0, 1.0, -0.8]),
        beta=np.array([0.0, 1.0, -0.5])),
}

TOPOLOGIES = list(DEFAULT_PARAMS.keys())

HAS_TREATMENT = {"confounding", "mediation", "collider", "mbias", "frontdoor"}
NO_TREATMENT = {"exposure", "iv"}


def _get_rng(rng, seed):
    if rng is not None:
        return rng
    return np.random.default_rng(seed)


def _get_params(topology, params):
    p = dict(DEFAULT_PARAMS[topology])
    if params is not None:
        p.update(params)
    return p


def gen_confounding(N, params=None, rng=None, seed=None):
    """A->T, A->Y, T->Y. Researcher controls for A*.

    Returns:
        dict with keys T, Y, A
    """
    rng = _get_rng(rng, seed)
    p = _get_params("confounding", params)
    K = len(p["p_A"])
    A = rng.choice(K, size=N, p=p["p_A"])
    D = make_dummies(A, K)
    T = D @ p["alpha"] + rng.normal(0, p["sigma_T"], N)
    Y = p["beta_T"] * T + D @ p["beta_A"] + rng.normal(0, 1, N)
    return {"T": T, "Y": Y, "A": A}


def gen_mediation(N, params=None, rng=None, seed=None):
    """T->A->Y. A mediates; researcher controls for A*.

    Returns:
        dict with keys T, Y, A
    """
    rng = _get_rng(rng, seed)
    p = _get_params("mediation", params)
    T = rng.binomial(1, 0.5, N).astype(float)
    K = len(p["gamma"])
    logits = p["gamma"][None, :] + p["delta"][None, :] * T[:, None]
    A = softmax_sample(logits, rng)
    D = make_dummies(A, K)
    Y = p["beta"][0] + D @ p["beta"][1:] + p["tau"] * T + rng.normal(0, 1, N)
    return {"T": T, "Y": Y, "A": A}


def gen_collider(N, params=None, rng=None, seed=None):
    """T->A<-Y. Researcher wrongly controls for A*.

    Returns:
        dict with keys T, Y, A
    """
    rng = _get_rng(rng, seed)
    p = _get_params("collider", params)
    T = rng.normal(0, 1, N)
    Y = p["tau"] * T + rng.normal(0, 1, N)
    logits = (p["g"][None, :] + p["dT"][None, :] * T[:, None]
              + p["dY"][None, :] * Y[:, None])
    A = softmax_sample(logits, rng)
    return {"T": T, "Y": Y, "A": A}


def gen_exposure(N, params=None, rng=None, seed=None):
    """A->Y (direct exposure, no treatment T).

    Returns:
        dict with keys Y, A
    """
    rng = _get_rng(rng, seed)
    p = _get_params("exposure", params)
    K = len(p["p_A"])
    A = rng.choice(K, size=N, p=p["p_A"])
    D = make_dummies(A, K)
    Y = p["beta"][0] + D @ p["beta"][1:] + rng.normal(0, 1, N)
    return {"Y": Y, "A": A}


def gen_mbias(N, params=None, rng=None, seed=None):
    """U1->{A,T}, U2->{A,Y}, T->Y. Conditioning on A* induces M-bias.

    Returns:
        dict with keys T, Y, A
    """
    rng = _get_rng(rng, seed)
    p = _get_params("mbias", params)
    N_out = N
    U1, U2 = rng.normal(0, 1, N_out), rng.normal(0, 1, N_out)
    T = p["delta_coef"] * U1 + rng.normal(0, 1, N_out)
    logits = (p["g"][None, :] + p["a1"][None, :] * U1[:, None]
              + p["a2"][None, :] * U2[:, None])
    A = softmax_sample(logits, rng)
    Y = p["tau"] * T + p["lam"] * U2 + rng.normal(0, 1, N_out)
    return {"T": T, "Y": Y, "A": A}


def gen_iv(N, params=None, rng=None, seed=None):
    """Z->A->Y, U->{A,Y}. IV topology with endogenous A.

    Returns:
        dict with keys Z, Y, A
    """
    rng = _get_rng(rng, seed)
    p = _get_params("iv", params)
    K = len(p["g"])
    Z = rng.normal(0, 1, N)
    U = rng.normal(0, 1, N)
    logits = (p["g"][None, :] + p["dZ"][None, :] * Z[:, None]
              + p["dU"][None, :] * U[:, None])
    A = softmax_sample(logits, rng)
    D = make_dummies(A, K)
    Y = p["beta"][0] + D @ p["beta"][1:] + p["lam"] * U + rng.normal(0, 1, N)
    return {"Z": Z, "Y": Y, "A": A}


def gen_frontdoor(N, params=None, rng=None, seed=None):
    """T->M->Y, U->{T,Y}. Misclassified variable is M (mediator, stored as A).

    Returns:
        dict with keys T, Y, A (A is the mediator M)
    """
    rng = _get_rng(rng, seed)
    p = _get_params("frontdoor", params)
    U = rng.normal(0, 1, N)
    T = p["alpha_U"] * U + rng.normal(0, 1, N)
    K = len(p["gamma"])
    logits = p["gamma"][None, :] + p["delta"][None, :] * T[:, None]
    A = softmax_sample(logits, rng)
    D = make_dummies(A, K)
    Y = p["beta"][0] + D @ p["beta"][1:] + p["lam_U"] * U + rng.normal(0, 1, N)
    return {"T": T, "Y": Y, "A": A}


GEN_FUNCS = {
    "confounding": gen_confounding,
    "mediation": gen_mediation,
    "collider": gen_collider,
    "exposure": gen_exposure,
    "mbias": gen_mbias,
    "iv": gen_iv,
    "frontdoor": gen_frontdoor,
}


def generate_data(topology, N, params=None, rng=None, seed=None):
    """Generate synthetic data for a given topology.

    Args:
        topology: one of "confounding", "mediation", "collider", "exposure",
                  "mbias", "iv", "frontdoor"
        N: sample size
        params: optional DGP parameter overrides
        rng: numpy random Generator
        seed: random seed (used if rng is None)

    Returns:
        dict with generated variables (topology-dependent keys)
    """
    if topology not in GEN_FUNCS:
        raise ValueError(f"Unknown topology: {topology}. Choose from {TOPOLOGIES}")
    return GEN_FUNCS[topology](N, params=params, rng=rng, seed=seed)
