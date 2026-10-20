"""Self-Consistency (SC) baseline — majority voting over sampled chains.

Reads the same chain outputs as SVS, selects answer by majority vote.
Used as the baseline comparison for the SVS method.
"""

from collections import Counter
from ..types import Chain


def sc_majority_vote(chains: list[Chain]) -> str:
    """Select answer by majority voting over chains.

    Args:
        chains: List of reasoning chains with extracted answers.

    Returns:
        The most common answer string. Ties broken alphabetically.
    """
    answers = [c.answer for c in chains if c.answer]
    if not answers:
        return "Unknown"
    counter = Counter(answers)
    max_count = max(counter.values())
    candidates = sorted([a for a, cnt in counter.items() if cnt == max_count])
    return candidates[0]


def evaluate_sc_baseline(results_path: str) -> dict:
    """Evaluate SC baseline from saved SVS results.

    Reads results.json (SVS pipeline output), extracts SC answers,
    computes accuracy and per-label breakdown.

    Args:
        results_path: Path to results.json from MVP run.

    Returns:
        Dict with SC accuracy, per-label accuracy, agreement with SVS.
    """
    import json

    with open(results_path) as f:
        results = json.load(f)

    n = len(results)
    sc_correct = sum(1 for r in results if r.get("correct_sc", False))
    svs_correct = sum(1 for r in results if r.get("correct_svs", False))

    agree = sum(1 for r in results
                if r.get("selected_answer") == r.get("sc_answer"))

    label_stats = {}
    for r in results:
        label = r.get("gold_label", "unknown")
        if label not in label_stats:
            label_stats[label] = {"total": 0, "sc_correct": 0, "svs_correct": 0}
        label_stats[label]["total"] += 1
        if r.get("correct_sc"):
            label_stats[label]["sc_correct"] += 1
        if r.get("correct_svs"):
            label_stats[label]["svs_correct"] += 1

    return {
        "sc_accuracy": sc_correct / n if n else 0,
        "svs_accuracy": svs_correct / n if n else 0,
        "delta": (svs_correct - sc_correct) / n if n else 0,
        "agreement_rate": agree / n if n else 0,
        "n_problems": n,
        "per_label": label_stats,
    }
