"""Episode-level balanced accuracy evaluation for guided router.

Input: counterfactual episodes.jsonl (245 episodes, 11 tasks)
Each episode has: internal trajectory (with death/score), deterministic trajectory.
Ground truth label: 'det-preferred' or 'internal-preferred' or 'no-preference'.
"""

import argparse
import json
from collections import defaultdict
from typing import Dict, List

DEATH_SCORE = -100


def classify_episode_gt(episode: Dict) -> str:
    """Determine ground-truth preferred route from counterfactual data."""
    int_data = episode["always_internal"] if "always_internal" in episode else episode["internal"]
    det_data = episode["always_deterministic"] if "always_deterministic" in episode else episode["deterministic"]

    int_score = int_data["final_score"]
    det_score = det_data["final_score"]
    int_died = int_data.get("death", int_score <= DEATH_SCORE)
    det_died = det_data.get("death", det_score <= DEATH_SCORE)

    if int_died and not det_died:
        return "det-preferred"
    if det_died and not int_died:
        return "internal-preferred"
    if int_died and det_died:
        return "no-preference"
    if det_score > int_score:
        return "det-preferred"
    if int_score > det_score:
        return "internal-preferred"
    return "no-preference"


def load_episodes(data_path: str) -> List[Dict]:
    episodes = []
    with open(data_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            episodes.append(json.loads(line))
    return episodes


def compute_balanced_accuracy(y_true: List[str], y_pred: List[str]) -> float:
    """Balanced accuracy across classes."""
    classes = sorted(set(y_true))
    per_class_acc = []
    for c in classes:
        mask = [yt == c for yt in y_true]
        n = sum(mask)
        if n == 0:
            continue
        correct = sum(1 for m, yp in zip(mask, y_pred) if m and yp == c)
        per_class_acc.append(correct / n)
    return sum(per_class_acc) / len(per_class_acc) if per_class_acc else 0.0


def evaluate_router(router, episodes: List[Dict]) -> Dict:
    """Evaluate router on counterfactual episodes."""
    y_true = []
    y_pred = []
    per_task = defaultdict(lambda: {"correct": 0, "total": 0})

    for ep in episodes:
        gt = classify_episode_gt(ep)
        if gt == "no-preference":
            continue

        task_type = ep.get("task_type", "unknown")
        route = router.route(task_type)

        pred_label = "det-preferred" if route == "deterministic" else "internal-preferred"
        y_true.append(gt)
        y_pred.append(pred_label)

        correct = (pred_label == gt)
        per_task[task_type]["correct"] += int(correct)
        per_task[task_type]["total"] += 1

    balanced_acc = compute_balanced_accuracy(y_true, y_pred)
    accuracy = sum(1 for yt, yp in zip(y_true, y_pred) if yt == yp) / len(y_true) if y_true else 0

    return {
        "balanced_accuracy": balanced_acc,
        "accuracy": accuracy,
        "n_episodes": len(y_true),
        "per_task": dict(per_task),
    }


def main():
    parser = argparse.ArgumentParser(description="Evaluate guided router")
    parser.add_argument("--data_path", type=str, required=True)
    parser.add_argument("--variant", type=str, default="oracle", choices=["oracle", "learned"])
    args = parser.parse_args()

    from .router import GuidedRouter
    router = GuidedRouter(variant=args.variant)
    episodes = load_episodes(args.data_path)

    results = evaluate_router(router, episodes)
    print(f"Variant: {args.variant}")
    print(f"Balanced Accuracy: {results['balanced_accuracy']:.4f}")
    print(f"Accuracy: {results['accuracy']:.4f}")
    print(f"Episodes: {results['n_episodes']}")

    for task, stats in sorted(results["per_task"].items()):
        acc = stats["correct"] / stats["total"] if stats["total"] else 0
        print(f"  {task}: {acc:.2f} ({stats['correct']}/{stats['total']})")


if __name__ == "__main__":
    main()
