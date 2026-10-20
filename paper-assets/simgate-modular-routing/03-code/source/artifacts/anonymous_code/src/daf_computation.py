"""Death Avoidance Fraction (DAF) computation with bootstrap confidence intervals.

DAF = 1 - delta_non_death / delta_full

where:
  delta_full = mean(det_score - int_score) over det-preferred episodes
  delta_non_death = same, excluding episodes where internal agent died

DAF measures the fraction of the routing signal attributable to death avoidance.
"""

import argparse
import json
import os
import numpy as np
from collections import defaultdict

DEATH_SCORE = -100.0
SEED = 42
N_BOOTSTRAP = 10000


def load_episodes(data_path: str) -> list:
    episodes = []
    with open(data_path) as f:
        for line in f:
            d = json.loads(line.strip())
            int_score = d["always_internal"]["final_score"]
            det_score = d["always_deterministic"]["final_score"]
            int_died = int_score <= DEATH_SCORE
            det_died = det_score <= DEATH_SCORE

            if int_died and not det_died:
                label = "det-preferred"
            elif det_died and not int_died:
                label = "internal-preferred"
            elif int_died and det_died:
                label = "no-preference"
            elif det_score > int_score:
                label = "det-preferred"
            elif int_score > det_score:
                label = "internal-preferred"
            else:
                label = "no-preference"

            episodes.append({
                "task_type": d["task_type"],
                "score_det": det_score,
                "score_int": int_score,
                "int_died": int_died,
                "det_died": det_died,
                "oracle_label": label,
            })
    return episodes


def compute_daf(eps: list) -> tuple:
    det_pref = [e for e in eps if e["oracle_label"] == "det-preferred"]
    if not det_pref:
        return None, {}

    delta_full = np.mean([e["score_det"] - e["score_int"] for e in det_pref])

    non_death = [e for e in det_pref if not e["int_died"]]
    if not non_death:
        delta_nd = 0.0
    else:
        delta_nd = np.mean([e["score_det"] - e["score_int"] for e in non_death])

    if delta_full == 0:
        return None, {}

    daf = 1.0 - delta_nd / delta_full
    return daf, {
        "n_det_pref": len(det_pref),
        "n_non_death_det_pref": len(non_death),
        "n_death": sum(1 for e in eps if e["int_died"]),
        "delta_full": float(delta_full),
        "delta_nd": float(delta_nd),
    }


def bootstrap_daf(eps: list, n_boot: int, rng: np.random.Generator) -> dict:
    n = len(eps)
    boot_dafs = []
    for _ in range(n_boot):
        idx = rng.integers(0, n, size=n)
        sample = [eps[i] for i in idx]
        daf, _ = compute_daf(sample)
        if daf is not None:
            boot_dafs.append(daf)

    if not boot_dafs:
        return {"daf": None, "ci_lower": None, "ci_upper": None}

    boot_dafs = np.array(boot_dafs)
    return {
        "daf": float(np.median(boot_dafs)),
        "ci_lower": float(np.percentile(boot_dafs, 2.5)),
        "ci_upper": float(np.percentile(boot_dafs, 97.5)),
        "n_valid_boots": len(boot_dafs),
    }


def main():
    parser = argparse.ArgumentParser(description="DAF bootstrap computation")
    parser.add_argument("--data_path", type=str, required=True,
                        help="Path to episode_details.jsonl")
    parser.add_argument("--n_bootstrap", type=int, default=N_BOOTSTRAP)
    parser.add_argument("--output", type=str, default="results/daf_bootstrap.json")
    parser.add_argument("--seed", type=int, default=SEED)
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    episodes = load_episodes(args.data_path)
    print(f"Loaded {len(episodes)} episodes")

    # Global DAF
    daf_point, details = compute_daf(episodes)
    boot = bootstrap_daf(episodes, args.n_bootstrap, rng)
    print(f"Global DAF = {daf_point:.4f} [{boot['ci_lower']:.4f}, {boot['ci_upper']:.4f}]")

    # Per-task DAF
    task_eps = defaultdict(list)
    for e in episodes:
        task_eps[e["task_type"]].append(e)

    per_task = {}
    for task, eps in sorted(task_eps.items()):
        daf_t, det_t = compute_daf(eps)
        boot_t = bootstrap_daf(eps, min(args.n_bootstrap, 1000), rng)
        per_task[task] = {
            "daf": float(daf_t) if daf_t is not None else None,
            "n_episodes": len(eps),
            **boot_t,
            **det_t,
        }
        if daf_t is not None:
            print(f"  {task}: DAF={daf_t:.4f} (n={len(eps)})")

    result = {
        "global": {"daf": float(daf_point) if daf_point else None, **boot, **details},
        "per_task": per_task,
        "config": {"n_bootstrap": args.n_bootstrap, "seed": args.seed},
    }

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(result, f, indent=2)
    print(f"Saved to {args.output}")


if __name__ == "__main__":
    main()
