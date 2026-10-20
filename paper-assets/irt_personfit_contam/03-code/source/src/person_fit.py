# Person-fit statistics for 4PL IRT models with PSN-IRT estimated parameters.

import numpy as np
from scipy.optimize import minimize_scalar


def prob_4pl(theta, a, b, c, d):
    """4PL IRT model probability: P(X=1|theta) = c + (d-c) / (1 + exp(-a*(theta-b))).

    Parameters
    ----------
    theta : float or array
        Ability parameter(s).
    a, b, c, d : array-like
        Item discrimination, difficulty, guessing, and feasibility parameters.

    Returns
    -------
    P : ndarray
        Response probabilities, clipped to [1e-15, 1-1e-15].
    """
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    c = np.asarray(c, dtype=np.float64)
    d = np.asarray(d, dtype=np.float64)
    z = a * (np.asarray(theta, dtype=np.float64) - b)
    sigmoid = 1.0 / (1.0 + np.exp(-np.clip(z, -30, 30)))
    P = c + (d - c) * sigmoid
    return np.clip(P, 1e-15, 1 - 1e-15)


def generate_response(theta, a, b, c, d, rng=None):
    """Generate binary response vector via Bernoulli sampling from 4PL probabilities.

    Parameters
    ----------
    theta : float or 1-d array
        If 1-d array of shape (N,), a, b, c, d must be 1-d of shape (J,),
        and output is (N, J).
    a, b, c, d : 1-d array of shape (J,)
        Item parameters.
    rng : numpy.random.Generator or None

    Returns
    -------
    x : ndarray, int8
        Binary responses, shape (J,) if theta is scalar, else (N, J).
    """
    if rng is None:
        rng = np.random.default_rng()
    theta = np.asarray(theta, dtype=np.float64)
    if theta.ndim == 1:
        P = prob_4pl(theta[:, None], a[None, :], b[None, :], c[None, :], d[None, :])
    else:
        P = prob_4pl(theta, a, b, c, d)
    u = rng.random(P.shape)
    return (u < P).astype(np.int8)


def log_likelihood(x, theta, a, b, c, d):
    """Log-likelihood of response vector x at ability theta under 4PL.

    Parameters
    ----------
    x : array-like, shape (..., J)
    theta : float or array broadcastable with x
    a, b, c, d : array-like, shape (J,)

    Returns
    -------
    ll : float or ndarray
    """
    P = prob_4pl(theta, a, b, c, d)
    x = np.asarray(x, dtype=np.float64)
    return np.sum(x * np.log(P) + (1 - x) * np.log(1 - P), axis=-1)


def estimate_theta_mle(x, a, b, c, d, theta_init=0.0, bounds=(-4, 4)):
    """MLE estimate of ability theta for a single response vector.

    Uses scipy bounded scalar minimization. Returns boundary value for
    all-correct or all-wrong patterns.

    Parameters
    ----------
    x : 1-d array, shape (J,)
    a, b, c, d : 1-d arrays, shape (J,)
    theta_init : float
    bounds : tuple

    Returns
    -------
    theta_hat : float
    """
    x = np.asarray(x, dtype=np.float64)
    total = x.sum()
    if total == 0:
        return float(bounds[0])
    if total == len(x):
        return float(bounds[1])

    def neg_ll(theta):
        return -log_likelihood(x, theta, a, b, c, d)

    res = minimize_scalar(neg_ll, bounds=bounds, method='bounded',
                          options={'xatol': 1e-6, 'maxiter': 200})
    return float(res.x)


def _estimate_theta_mle_batch(X, a, b, c, d, bounds=(-4, 4)):
    """Vectorized MLE theta estimation for a batch of response vectors.

    Uses proportion-logit as initial guess, then refines with bounded optimization.

    Parameters
    ----------
    X : ndarray, shape (N, J)
    a, b, c, d : 1-d arrays, shape (J,)
    bounds : tuple

    Returns
    -------
    thetas : ndarray, shape (N,)
    """
    N = X.shape[0]
    thetas = np.empty(N, dtype=np.float64)

    totals = X.sum(axis=1)
    all_zero = totals == 0
    all_one = totals == X.shape[1]
    thetas[all_zero] = bounds[0]
    thetas[all_one] = bounds[1]

    mask = ~(all_zero | all_one)
    indices = np.where(mask)[0]

    for i in indices:
        thetas[i] = estimate_theta_mle(X[i], a, b, c, d, bounds=bounds)

    return thetas


def compute_lz(x, theta, a, b, c, d):
    """Standardized log-likelihood person-fit statistic lz (Drasgow et al., 1985).

    Parameters
    ----------
    x : array, shape (..., J)
    theta : float or array
    a, b, c, d : 1-d arrays, shape (J,)

    Returns
    -------
    lz : float or ndarray
    """
    P = prob_4pl(theta, a, b, c, d)
    Q = 1 - P
    x = np.asarray(x, dtype=np.float64)

    l = np.sum(x * np.log(P) + (1 - x) * np.log(Q), axis=-1)
    E_l = np.sum(P * np.log(P) + Q * np.log(Q), axis=-1)
    Var_l = np.sum(P * Q * (np.log(P / Q)) ** 2, axis=-1)

    return (l - E_l) / np.sqrt(Var_l)


def compute_lz_star(x, theta_hat, a, b, c, d):
    """Corrected lz* statistic (Snijders, 2001) accounting for estimated theta.

    The correction reduces the variance of l to account for the covariance
    between the MLE theta and the log-likelihood.

    Parameters
    ----------
    x : array, shape (..., J)
    theta_hat : float or array
    a, b, c, d : 1-d arrays, shape (J,)

    Returns
    -------
    lz_star : float or ndarray
    """
    a_ = np.asarray(a, dtype=np.float64)
    b_ = np.asarray(b, dtype=np.float64)
    c_ = np.asarray(c, dtype=np.float64)
    d_ = np.asarray(d, dtype=np.float64)

    P = prob_4pl(theta_hat, a_, b_, c_, d_)
    Q = 1 - P
    x = np.asarray(x, dtype=np.float64)

    z = a_ * (np.asarray(theta_hat, dtype=np.float64) - b_)
    sigma = 1.0 / (1.0 + np.exp(-np.clip(z, -30, 30)))

    dP = a_ * (d_ - c_) * sigma * (1 - sigma)

    h = dP / (P * Q)
    g = np.log(P / Q)

    l = np.sum(x * np.log(P) + (1 - x) * np.log(Q), axis=-1)
    E_l = np.sum(P * np.log(P) + Q * np.log(Q), axis=-1)
    Var_l = np.sum(P * Q * g ** 2, axis=-1)

    I_theta = np.sum(P * Q * h ** 2, axis=-1)
    C_theta = np.sum(P * Q * h * g, axis=-1)

    Var_star = Var_l - C_theta ** 2 / I_theta

    fallback = Var_star <= 0
    Var_use = np.where(fallback, Var_l, Var_star)

    return (l - E_l) / np.sqrt(Var_use)


def compute_outfit(x, theta, a, b, c, d):
    """Outfit (unweighted) mean-square statistic.

    Expected value is 1. Values > 1 indicate unexpected responses.

    Parameters
    ----------
    x : array, shape (..., J)
    theta : float or array
    a, b, c, d : 1-d arrays, shape (J,)

    Returns
    -------
    outfit : float or ndarray
    """
    P = prob_4pl(theta, a, b, c, d)
    Q = 1 - P
    x = np.asarray(x, dtype=np.float64)
    n = P.shape[-1]
    residual_sq = (x - P) ** 2 / (P * Q)
    return np.sum(residual_sq, axis=-1) / n


def compute_infit(x, theta, a, b, c, d):
    """Infit (weighted) mean-square statistic.

    Items with higher information (P*Q) receive greater weight.

    Parameters
    ----------
    x : array, shape (..., J)
    theta : float or array
    a, b, c, d : 1-d arrays, shape (J,)

    Returns
    -------
    infit : float or ndarray
    """
    P = prob_4pl(theta, a, b, c, d)
    Q = 1 - P
    x = np.asarray(x, dtype=np.float64)
    numerator = np.sum((x - P) ** 2, axis=-1)
    denominator = np.sum(P * Q, axis=-1)
    return numerator / denominator


def filter_valid_items(a, b, c, d, min_a=0.0):
    """Return boolean mask for items with a > min_a.

    Parameters
    ----------
    a, b, c, d : 1-d arrays
    min_a : float
        Items with a <= min_a are excluded.

    Returns
    -------
    mask : ndarray of bool
    """
    return np.asarray(a) > min_a
