"""Shared utilities: OLS, dummy encoding, softmax sampling."""

import numpy as np


def softmax_sample(logits, rng):
    """Sample categorical variable from row-wise softmax probabilities.

    Args:
        logits: (N, K) array of logits
        rng: numpy random Generator

    Returns:
        (N,) integer array with values in {0, ..., K-1}
    """
    e = np.exp(logits - logits.max(axis=1, keepdims=True))
    p = e / e.sum(axis=1, keepdims=True)
    cum = np.cumsum(p, axis=1)
    u = rng.uniform(size=logits.shape[0])
    K = logits.shape[1]
    result = np.zeros(logits.shape[0], dtype=int)
    for k in range(K - 1):
        result += (u >= cum[:, k]).astype(int)
    return result


def misclassify(A, C, rng):
    """Apply misclassification: A*_i ~ Cat(C[:, A_i]).

    Args:
        A: (N,) true labels in {0, ..., K-1}
        C: (K, K) column-stochastic confusion matrix
        rng: numpy random Generator

    Returns:
        (N,) misclassified labels
    """
    K = C.shape[0]
    probs = C[:, A]
    cum = np.cumsum(probs, axis=0)
    u = rng.uniform(size=len(A))
    result = np.zeros(len(A), dtype=int)
    for k in range(K - 1):
        result += (u >= cum[k]).astype(int)
    return result


def make_dummies(A, K=None):
    """Create K-1 dummy variables (reference category 0).

    Args:
        A: (N,) categorical labels in {0, ..., K-1}
        K: number of categories (inferred from A if None)

    Returns:
        (N, K-1) dummy matrix
    """
    if K is None:
        K = int(A.max()) + 1
    N = len(A)
    D = np.zeros((N, K - 1))
    for j in range(K - 1):
        D[:, j] = (A == j + 1).astype(float)
    return D


def make_full_dummies(A, K=None):
    """Create full K one-hot encoding.

    Args:
        A: (N,) categorical labels in {0, ..., K-1}
        K: number of categories (inferred from A if None)

    Returns:
        (N, K) one-hot matrix
    """
    if K is None:
        K = int(A.max()) + 1
    N = len(A)
    D = np.zeros((N, K))
    for j in range(K):
        D[:, j] = (A == j).astype(float)
    return D


def ols(X, Y):
    """OLS point estimate via least-squares.

    Args:
        X: (N, p) design matrix
        Y: (N,) response

    Returns:
        (p,) coefficient vector
    """
    return np.linalg.lstsq(X, Y, rcond=None)[0]


def ols_with_se(X, Y):
    """OLS point estimate with homoskedastic standard errors.

    Args:
        X: (N, p) design matrix
        Y: (N,) response

    Returns:
        (beta, se) tuple of (p,) arrays
    """
    beta = np.linalg.lstsq(X, Y, rcond=None)[0]
    resid = Y - X @ beta
    n, p = X.shape
    s2 = resid @ resid / max(n - p, 1)
    try:
        XtX_inv = np.linalg.inv(X.T @ X)
        se = np.sqrt(np.maximum(np.diag(s2 * XtX_inv), 0.0))
    except np.linalg.LinAlgError:
        se = np.full(p, np.nan)
    return beta, se
