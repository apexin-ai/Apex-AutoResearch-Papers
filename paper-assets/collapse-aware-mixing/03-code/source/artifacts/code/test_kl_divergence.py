"""Unit test for compute_kl_divergence vocab size mismatch fix."""

import sys
import numpy as np


def test_kl_with_oov_tokens():
    """Token IDs exceeding vocab_size should not crash."""
    sys.path.insert(0, ".")
    from metrics import compute_kl_divergence

    # ids contain token 50300, but vocab_size is 50254
    ids_a = [0, 1, 50300, 2, 3, 100, 200, 50300, 1, 0]
    ids_b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    vocab_size = 50254

    result = compute_kl_divergence(ids_a, ids_b, vocab_size, n_bootstrap=10)

    assert "kl_unigram" in result, "Missing kl_unigram"
    assert "kl_bigram" in result, "Missing kl_bigram"
    assert "js_divergence" in result, "Missing js_divergence"
    assert result["kl_unigram"] >= 0, f"KL should be non-negative, got {result['kl_unigram']}"
    assert result["js_divergence"] >= 0, f"JS should be non-negative, got {result['js_divergence']}"
    assert np.isfinite(result["kl_unigram"]), f"KL not finite: {result['kl_unigram']}"
    print(f"PASS: kl_unigram={result['kl_unigram']:.4f}, js={result['js_divergence']:.4f}")


def test_kl_same_distribution():
    """KL of identical distributions should be ~0."""
    sys.path.insert(0, ".")
    from metrics import compute_kl_divergence

    ids = list(range(100)) * 10
    result = compute_kl_divergence(ids, ids, vocab_size=200, n_bootstrap=10)
    assert result["kl_unigram"] < 1e-6, f"KL of same dist should be ~0, got {result['kl_unigram']}"
    print(f"PASS: kl_unigram={result['kl_unigram']:.8f} (expected ~0)")


def test_kl_bootstrap_ci():
    """Bootstrap CI should bracket the point estimate."""
    sys.path.insert(0, ".")
    from metrics import compute_kl_divergence

    rng = np.random.default_rng(42)
    ids_a = rng.integers(0, 1000, size=5000).tolist()
    ids_b = rng.integers(0, 1000, size=5000).tolist()
    result = compute_kl_divergence(ids_a, ids_b, vocab_size=1000, n_bootstrap=100)
    assert result["kl_ci_lower_95"] <= result["kl_ci_upper_95"], "CI bounds inverted"
    print(f"PASS: CI=[{result['kl_ci_lower_95']:.6f}, {result['kl_ci_upper_95']:.6f}]")


if __name__ == "__main__":
    test_kl_with_oov_tokens()
    test_kl_same_distribution()
    test_kl_bootstrap_ci()
    print("\nAll KL divergence tests passed.")
