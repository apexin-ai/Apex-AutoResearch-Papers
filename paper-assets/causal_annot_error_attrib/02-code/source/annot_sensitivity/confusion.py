"""Confusion matrix utilities: validation, generation, interpolation.

Convention: C[j, i] = P(A*=j | A=i), columns sum to 1 (column-stochastic).
"""

import numpy as np


def validate_confusion_matrix(C):
    """Check if C is a valid column-stochastic confusion matrix.

    Args:
        C: array to validate

    Returns:
        True if valid, False otherwise
    """
    if not isinstance(C, np.ndarray):
        return False
    if C.ndim != 2 or C.shape[0] != C.shape[1]:
        return False
    if C.shape[0] < 2:
        return False
    if (C < -1e-10).any():
        return False
    if not np.allclose(C.sum(axis=0), 1.0, atol=1e-6):
        return False
    return True


def random_confusion_matrix(K, diag_dominance=0.8, rng=None):
    """Generate a random column-stochastic confusion matrix.

    Args:
        K: number of categories
        diag_dominance: controls diagonal strength (0 to 1)
        rng: numpy random Generator (created if None)

    Returns:
        (K, K) column-stochastic matrix
    """
    if rng is None:
        rng = np.random.default_rng()
    diag_alpha = diag_dominance * 10
    offdiag_alpha = max((1 - diag_dominance) * 10 / max(K - 1, 1), 0.1)
    C = np.zeros((K, K))
    for k in range(K):
        alphas = np.full(K, offdiag_alpha)
        alphas[k] = diag_alpha
        C[:, k] = rng.dirichlet(alphas)
    return C


def interpolate_confusion(C0, delta):
    """Interpolate between identity and C0: C(delta) = (1-delta)*I + delta*C0.

    Args:
        C0: (K, K) base confusion matrix
        delta: interpolation parameter (0 = identity, 1 = C0)

    Returns:
        (K, K) interpolated column-stochastic matrix
    """
    K = C0.shape[0]
    C = (1 - delta) * np.eye(K) + delta * C0
    C = np.maximum(C, 0.0)
    col_sums = C.sum(axis=0)
    col_sums = np.where(col_sums < 1e-10, 1.0, col_sums)
    return C / col_sums


def delta_range(C0):
    """Compute valid delta range for interpolation.

    Args:
        C0: (K, K) base confusion matrix

    Returns:
        (delta_min, delta_max) tuple
    """
    min_diag = np.diag(C0).min()
    if min_diag >= 1.0:
        return (0.0, 10.0)
    delta_max = min(1.0 / (1.0 - min_diag), 10.0)
    return (0.0, delta_max)


def predefined_matrices(K=3):
    """Return a dict of predefined K x K confusion matrices.

    Args:
        K: number of categories (only K=3 supported)

    Returns:
        dict mapping name to (K, K) confusion matrix
    """
    if K != 3:
        raise ValueError(f"Predefined matrices only available for K=3, got K={K}")
    return {
        "symmetric_high": np.array([
            [0.80, 0.10, 0.10],
            [0.10, 0.80, 0.10],
            [0.10, 0.10, 0.80]]),
        "mild_uniform": np.array([
            [0.8 + 0.2 / 3, 0.2 / 3, 0.2 / 3],
            [0.2 / 3, 0.8 + 0.2 / 3, 0.2 / 3],
            [0.2 / 3, 0.2 / 3, 0.8 + 0.2 / 3]]),
        "moderate_uniform": np.array([
            [0.6 + 0.4 / 3, 0.4 / 3, 0.4 / 3],
            [0.4 / 3, 0.6 + 0.4 / 3, 0.4 / 3],
            [0.4 / 3, 0.4 / 3, 0.6 + 0.4 / 3]]),
        "severe_uniform": np.array([
            [0.4 + 0.6 / 3, 0.6 / 3, 0.6 / 3],
            [0.6 / 3, 0.4 + 0.6 / 3, 0.6 / 3],
            [0.6 / 3, 0.6 / 3, 0.4 + 0.6 / 3]]),
        "asymmetric": np.array([
            [0.75, 0.05, 0.05],
            [0.20, 0.80, 0.10],
            [0.05, 0.15, 0.85]]),
        "near_permutation": np.array([
            [0.05, 0.05, 0.90],
            [0.90, 0.05, 0.05],
            [0.05, 0.90, 0.05]]),
        "realistic_llm": np.array([
            [0.78, 0.15, 0.03],
            [0.18, 0.72, 0.18],
            [0.04, 0.13, 0.79]]),
    }
