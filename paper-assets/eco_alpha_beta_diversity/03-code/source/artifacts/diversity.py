# Core diversity computations: Hill numbers, Jost partition, Baselga decomposition, coverage.

import math
import numpy as np
from collections import Counter


def _hill_from_props(proportions, q):
    """Hill number from a sequence of proportions (must be > 0)."""
    ps = [p for p in proportions if p > 0]
    if not ps:
        return 0.0
    if q == 0:
        return float(len(ps))
    elif abs(q - 1) < 1e-10:
        H = -sum(p * math.log(p) for p in ps)
        return math.exp(H)
    else:
        return sum(p ** q for p in ps) ** (1.0 / (1.0 - q))


def hill_number(freq, q):
    """Hill number of order q from a frequency dict {token: count}."""
    total = sum(freq.values())
    if total == 0:
        return 0.0
    props = [c / total for c in freq.values() if c > 0]
    return _hill_from_props(props, q)


# ---------------------------------------------------------------------------
# Jost (2007) multiplicative diversity partition
# ---------------------------------------------------------------------------

def jost_partition(freq_list, q, weights=None):
    """
    Jost multiplicative partition: gamma = alpha * beta.

    Args:
        freq_list: list of {token: count} dicts, one per community (story).
        q: diversity order (0, 1, or 2).
        weights: community weights (default: equal 1/N).

    Returns:
        (alpha, gamma, beta)
    """
    N = len(freq_list)
    if N == 0:
        return 0.0, 0.0, 1.0
    if weights is None:
        weights = np.full(N, 1.0 / N)

    # proportions per community
    props_list = []
    for freq in freq_list:
        total = sum(freq.values())
        if total > 0:
            props_list.append({w: c / total for w, c in freq.items() if c > 0})
        else:
            props_list.append({})

    all_sp = set()
    for p in props_list:
        all_sp.update(p.keys())
    if not all_sp:
        return 0.0, 0.0, 1.0

    # --- alpha ---
    if q == 0:
        alpha = sum(w * len(p) for w, p in zip(weights, props_list))
    elif abs(q - 1) < 1e-10:
        wH = 0.0
        for w, p in zip(weights, props_list):
            if p:
                H = -sum(v * math.log(v) for v in p.values())
                wH += w * H
        alpha = math.exp(wH)
    else:
        wpq = 0.0
        for w, p in zip(weights, props_list):
            wpq += w * sum(v ** q for v in p.values())
        alpha = wpq ** (1.0 / (1.0 - q))

    # --- gamma (pooled proportions) ---
    pooled = {}
    for sp in all_sp:
        pooled[sp] = sum(w * p.get(sp, 0.0) for w, p in zip(weights, props_list))
    gamma = _hill_from_props(list(pooled.values()), q)

    beta = gamma / alpha if alpha > 0 else float('inf')
    return float(alpha), float(gamma), float(beta)


# ---------------------------------------------------------------------------
# Baselga (2013, 2017) abundance-based Bray-Curtis decomposition
# ---------------------------------------------------------------------------

def baselga_pairwise(freq1, freq2):
    """
    Pairwise Baselga decomposition (Bray-Curtis basis).

    Returns:
        dict with bc_total, bc_balanced (turnover-like), bc_gradient (nestedness-like).
    """
    all_sp = set(freq1) | set(freq2)
    if not all_sp:
        return {'bc_total': 0.0, 'bc_balanced': 0.0, 'bc_gradient': 0.0}

    A = sum(min(freq1.get(sp, 0), freq2.get(sp, 0)) for sp in all_sp)
    B = sum(freq1.values()) - A          # abundance exclusive to community 1
    C = sum(freq2.values()) - A          # abundance exclusive to community 2

    denom = 2 * A + B + C
    if denom == 0:
        return {'bc_total': 0.0, 'bc_balanced': 0.0, 'bc_gradient': 0.0}

    bc_total = (B + C) / denom
    minBC = min(B, C)
    denom_bal = A + minBC
    bc_balanced = minBC / denom_bal if denom_bal > 0 else 0.0
    bc_gradient = bc_total - bc_balanced

    return {
        'bc_total': float(bc_total),
        'bc_balanced': float(bc_balanced),
        'bc_gradient': float(bc_gradient),
    }


def baselga_multi(freq_list):
    # TODO(research-phase): 改为 Baselga (2017) ratio-of-sums 公式
    # 当前 mean-of-ratios 在样本量不均时有偏，Research 阶段必须改为：
    # β_BAL = Σ min(B,C) / Σ (A + min(B,C))
    # β_GRA = Σ |B-C| / Σ (2A + B + C) * Σ A / Σ (A + min(B,C))
    """Average pairwise Baselga decomposition over all pairs."""
    N = len(freq_list)
    if N < 2:
        return {
            'bc_total': 0.0, 'bc_balanced': 0.0, 'bc_gradient': 0.0,
            'bc_total_vals': [], 'bc_balanced_vals': [], 'bc_gradient_vals': [],
            'n_pairs': 0,
        }

    tots, bals, grads = [], [], []
    for i in range(N):
        for j in range(i + 1, N):
            r = baselga_pairwise(freq_list[i], freq_list[j])
            tots.append(r['bc_total'])
            bals.append(r['bc_balanced'])
            grads.append(r['bc_gradient'])

    return {
        'bc_total': float(np.mean(tots)),
        'bc_balanced': float(np.mean(bals)),
        'bc_gradient': float(np.mean(grads)),
        'bc_total_vals': tots,
        'bc_balanced_vals': bals,
        'bc_gradient_vals': grads,
        'n_pairs': len(tots),
    }


# ---------------------------------------------------------------------------
# Sample coverage (Chao & Shen 2003)
# ---------------------------------------------------------------------------

def sample_coverage(freq):
    """Good-Turing sample coverage estimator."""
    n = sum(freq.values())
    if n == 0:
        return 0.0

    counts = list(freq.values())
    f1 = sum(1 for c in counts if c == 1)
    f2 = sum(1 for c in counts if c == 2)

    if f1 == 0:
        return 1.0

    if f2 > 0:
        A = ((n - 1) * f1) / ((n - 1) * f1 + 2 * f2)
    else:
        A = ((n - 1) * (f1 - 1)) / ((n - 1) * (f1 - 1) + 2) if f1 > 1 else 1.0

    return float(1.0 - (f1 / n) * A)


# ---------------------------------------------------------------------------
# Rarefaction helpers
# ---------------------------------------------------------------------------

def _expand_freq(freq):
    """Expand {token: count} to a flat list of tokens."""
    words = []
    for w, c in freq.items():
        words.extend([w] * int(round(c)))
    return words


def rarefy_to_size(freq, m, rng):
    """Subsample m tokens from a frequency distribution without replacement."""
    words = _expand_freq(freq)
    n = len(words)
    if m >= n:
        return dict(freq)
    sub = rng.choice(words, size=m, replace=False)
    return dict(Counter(sub))


def coverage_at_size(freq, m):
    """Expected sample coverage when rarefying freq to size m (analytic)."""
    n = sum(freq.values())
    if m >= n or m <= 0:
        return sample_coverage(freq)
    f1 = sum(1 for c in freq.values() if c == 1)
    return 1.0 - f1 / n * ((n - m) / n) if n > 0 else 0.0


def size_for_target_coverage(freq, target_cov, rng, tol=0.005, max_iter=40):
    """Binary-search for sample size m that yields coverage ~ target_cov."""
    n = sum(freq.values())
    if n == 0:
        return 0
    cur_cov = sample_coverage(freq)
    if cur_cov <= target_cov:
        return n

    lo, hi = 1, n
    best_m = n
    for _ in range(max_iter):
        mid = (lo + hi) // 2
        rarefied = rarefy_to_size(freq, mid, rng)
        c = sample_coverage(rarefied)
        if abs(c - target_cov) < tol:
            return mid
        if c < target_cov:
            lo = mid + 1
        else:
            best_m = mid
            hi = mid - 1
        if lo > hi:
            break
    return best_m
