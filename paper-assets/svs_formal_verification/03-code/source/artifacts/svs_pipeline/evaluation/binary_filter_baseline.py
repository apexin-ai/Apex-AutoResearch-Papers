"""Binary Filter + SC baseline — discard Z3-inconsistent chains, majority vote on rest.

Implements the FoVer/LINC-style approach: chains that fail Z3 internal consistency
checks are filtered out, and the remaining chains are aggregated by majority vote.
This is the "binary verification + majority vote" cell in the 2x2 ablation matrix.
"""

from collections import Counter
from ..types import SVSResult, ChainVerification


def binary_filter_sc(result: SVSResult, ic_threshold: float = 0.5) -> str:
    """Filter chains by IC threshold, majority vote on survivors.

    Args:
        result: SVSResult with chain_verifications populated.
        ic_threshold: Chains with IC >= threshold survive. Default 0.5.

    Returns:
        Selected answer string. Falls back to SC (all chains) if no chain survives.
    """
    survivors = [cv for cv in result.chain_verifications if cv.ic_score >= ic_threshold]

    if not survivors:
        answers = [cv.answer for cv in result.chain_verifications if cv.answer]
        if not answers:
            return "Unknown"
        counter = Counter(answers)
        max_count = max(counter.values())
        return sorted([a for a, c in counter.items() if c == max_count])[0]

    answers = [cv.answer for cv in survivors if cv.answer]
    if not answers:
        return "Unknown"
    counter = Counter(answers)
    max_count = max(counter.values())
    return sorted([a for a, c in counter.items() if c == max_count])[0]


def evaluate_binary_filter(results: list[SVSResult], ic_threshold: float = 0.5) -> dict:
    """Evaluate binary filter baseline across all problems.

    Args:
        results: List of SVSResult from MVP run.
        ic_threshold: IC threshold for chain filtering.

    Returns:
        Dict with accuracy, filter stats, comparison with SVS and SC.
    """
    n = len(results)
    bf_correct = 0
    total_chains = 0
    surviving_chains = 0
    fallback_count = 0

    per_problem = []
    for r in results:
        bf_answer = binary_filter_sc(r, ic_threshold)
        is_correct = bf_answer == r.gold_label
        if is_correct:
            bf_correct += 1

        survivors = [cv for cv in r.chain_verifications if cv.ic_score >= ic_threshold]
        total_chains += len(r.chain_verifications)
        surviving_chains += len(survivors)
        if not survivors:
            fallback_count += 1

        per_problem.append({
            "problem_id": r.problem_id,
            "bf_answer": bf_answer,
            "gold": r.gold_label,
            "correct": is_correct,
            "chains_total": len(r.chain_verifications),
            "chains_surviving": len(survivors),
            "svs_answer": r.selected_answer,
            "sc_answer": r.sc_answer,
        })

    return {
        "binary_filter_accuracy": bf_correct / n if n else 0,
        "svs_accuracy": sum(1 for r in results if r.correct_svs) / n if n else 0,
        "sc_accuracy": sum(1 for r in results if r.correct_sc) / n if n else 0,
        "ic_threshold": ic_threshold,
        "total_chains": total_chains,
        "surviving_chains": surviving_chains,
        "filter_rate": 1 - surviving_chains / total_chains if total_chains else 0,
        "fallback_to_sc": fallback_count,
        "n_problems": n,
        "per_problem": per_problem,
    }
