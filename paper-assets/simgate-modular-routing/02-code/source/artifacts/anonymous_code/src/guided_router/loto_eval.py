"""LOTO (Leave-One-Task-Out) evaluation for guided router.

11-fold: each fold leaves out 1 task type, uses remaining 10 to determine
routing decision for the held-out task type.

Strategies:
  - prior_majority: majority of training tasks are death-risk -> predict det
  - prior_mean_threshold: mean death rate of training tasks > threshold -> predict det
  - learned: use string-pattern matching (naturally generalizes to unseen tasks)
"""

import argparse
import json
import os
from collections import defaultdict

from .config import ALL_TASKS, DEATH_THRESHOLD
from .eval_episode import load_episodes, classify_episode_gt, compute_balanced_accuracy
from .router import GuidedRouter


def loto_evaluation(episodes, tasks):
    """Run leave-one-task-out evaluation."""
    task_episodes = defaultdict(list)
    for ep in episodes:
        task_episodes[ep["task_type"]].append(ep)

    results = {}
    for held_out in sorted(tasks.keys()):
        test_eps = task_episodes.get(held_out, [])
        if not test_eps:
            continue

        train_tasks = {t: r for t, r in tasks.items() if t != held_out}

        # Strategy 1: majority vote from training tasks
        n_death = sum(1 for r in train_tasks.values() if r > DEATH_THRESHOLD)
        majority_route = "deterministic" if n_death > len(train_tasks) / 2 else "internal"

        # Strategy 2: learned (pattern matching)
        learned_router = GuidedRouter(variant="learned")
        learned_route = learned_router.route(held_out)

        # Evaluate
        gt_labels = []
        for ep in test_eps:
            gt = classify_episode_gt(ep)
            if gt != "no-preference":
                gt_labels.append(gt)

        def acc_for_route(route, labels):
            pred = "det-preferred" if route == "deterministic" else "internal-preferred"
            return sum(1 for gt in labels if gt == pred) / len(labels) if labels else 0

        results[held_out] = {
            "n_episodes": len(gt_labels),
            "majority_route": majority_route,
            "majority_acc": acc_for_route(majority_route, gt_labels),
            "learned_route": learned_route,
            "learned_acc": acc_for_route(learned_route, gt_labels),
            "ground_truth_death_rate": tasks[held_out],
        }

    return results


def main():
    parser = argparse.ArgumentParser(description="LOTO evaluation for guided router")
    parser.add_argument("--data_path", type=str, required=True)
    parser.add_argument("--output", type=str, default="results/loto_results.json")
    args = parser.parse_args()

    episodes = load_episodes(args.data_path)
    results = loto_evaluation(episodes, ALL_TASKS)

    print("LOTO Results:")
    for task, r in sorted(results.items()):
        print(f"  {task}: majority={r['majority_acc']:.2f}, learned={r['learned_acc']:.2f} "
              f"(n={r['n_episodes']}, dr={r['ground_truth_death_rate']:.2f})")

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)


if __name__ == "__main__":
    main()
