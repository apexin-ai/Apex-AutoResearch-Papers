"""Self-Certainty baseline — use token-level logprobs as chain selection signal.

Computes average log-probability across generated tokens as a proxy for
model confidence. Higher average logprob = model is more "certain" about
the reasoning chain. Used as a non-verification baseline for comparison.
"""

import math
import numpy as np
from collections import Counter


def compute_chain_certainty(logprobs: list[float] | None) -> float:
    """Compute average log-probability (certainty score) for a chain.

    Args:
        logprobs: List of per-token log probabilities.

    Returns:
        Average logprob. Returns -inf if no logprobs available.
    """
    if not logprobs:
        return float('-inf')
    return sum(logprobs) / len(logprobs)


def self_certainty_select(chains_with_logprobs: list[dict]) -> str:
    """Select answer from the chain with highest average logprob.

    Args:
        chains_with_logprobs: List of dicts with 'answer' and 'logprobs' keys.

    Returns:
        Answer from the most confident chain.
    """
    if not chains_with_logprobs:
        return "Unknown"

    scored = []
    for c in chains_with_logprobs:
        certainty = compute_chain_certainty(c.get("logprobs"))
        scored.append((certainty, c.get("answer", "Unknown")))

    scored.sort(reverse=True)
    return scored[0][1]


def evaluate_self_certainty(results_with_logprobs: list[dict]) -> dict:
    """Evaluate self-certainty baseline.

    Args:
        results_with_logprobs: List of problem dicts with chain logprobs.

    Returns:
        Accuracy and comparison metrics.
    """
    n = len(results_with_logprobs)
    correct = 0

    for problem in results_with_logprobs:
        selected = self_certainty_select(problem.get("chains", []))
        if selected == problem.get("gold_label"):
            correct += 1

    return {
        "self_certainty_accuracy": correct / n if n else 0,
        "n_problems": n,
    }
