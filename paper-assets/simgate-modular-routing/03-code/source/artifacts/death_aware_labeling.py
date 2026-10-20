import argparse
import json
import os
import sys
from collections import defaultdict
from typing import Dict, List, Any, Tuple

DEATH_THRESHOLD = -100


def is_dead(final_score: float) -> bool:
    return final_score <= DEATH_THRESHOLD


def classify_episode(int_score: float, det_score: float) -> Tuple[str, str, str]:
    """Returns (label, reason, signal_source). Never discards."""
    int_died = is_dead(int_score)
    det_died = is_dead(det_score)

    if int_died and not det_died:
        return "det-preferred", "int_died_det_alive", "death_asymmetry"
    if det_died and not int_died:
        return "internal-preferred", "det_died_int_alive", "death_asymmetry"
    if int_died and det_died:
        return "no-preference", "both_died", "both_dead"
    if det_score > int_score:
        return "det-preferred", "both_alive_det_wins", "score_comparison"
    if int_score > det_score:
        return "internal-preferred", "both_alive_int_wins", "score_comparison"
    return "no-preference", "tie", "tied_alive"


def extract_steps(episode_data: Dict, label: str, reason: str,
                  signal_source: str,
                  task_type: str, episode_idx: int, variation_idx: int,
                  int_score: float, det_score: float,
                  int_died: bool, det_died: bool) -> List[Dict]:
    if label == "internal-preferred":
        source_key = "always_internal"
    elif label == "det-preferred":
        source_key = "always_deterministic"
    else:
        source_key = "always_internal"

    source_ep = episode_data[source_key]
    steps = source_ep.get("steps", [])
    action_history = []
    triples = []

    for s in steps:
        triples.append({
            "task_type": task_type,
            "episode_id": episode_idx,
            "variation": variation_idx,
            "step_idx": s["step"],
            "observation": s.get("observation", ""),
            "action": s["action"],
            "action_history": list(action_history),
            "label": label,
            "signal_source": signal_source,
            "labeling_reason": reason,
            "episode_score_internal": int_score,
            "episode_score_det": det_score,
            "internal_died": int_died,
            "det_died": det_died,
        })
        action_history.append(s["action"])

    return triples


def process_dir(input_dir: str) -> Tuple[List[Dict], Dict[str, int]]:
    task_type = os.path.basename(input_dir.rstrip("/"))
    episodes_path = os.path.join(input_dir, "episodes.jsonl")
    if not os.path.exists(episodes_path):
        print(f"  SKIP {task_type}: no episodes.jsonl")
        return [], {}

    stats = defaultdict(int)
    all_triples = []

    with open(episodes_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            ep = json.loads(line)

            episode_idx = ep.get("episode_idx", stats["total_episodes"])
            variation_idx = ep.get("variation_idx", 0)

            if "always_internal" in ep and "always_deterministic" in ep:
                int_score = ep["always_internal"]["final_score"]
                det_score = ep["always_deterministic"]["final_score"]
            else:
                stats["total_episodes"] += 1
                stats["format_error"] += 1
                continue

            int_died = is_dead(int_score)
            det_died = is_dead(det_score)
            label, reason, signal_source = classify_episode(int_score, det_score)

            stats["total_episodes"] += 1
            reason_key_map = {
                "int_died_det_alive": "det_wins_death",
                "det_died_int_alive": "int_wins_death",
                "both_alive_det_wins": "det_wins_score",
                "both_alive_int_wins": "int_wins_score",
                "tie": "ties",
                "both_died": "both_died",
            }
            stats[reason_key_map[reason]] += 1

            triples = extract_steps(
                ep, label, reason, signal_source,
                task_type, episode_idx, variation_idx,
                int_score, det_score, int_died, det_died,
            )
            all_triples.extend(triples)

            if label == "det-preferred":
                stats["det_preferred_steps"] += len(triples)
            elif label == "internal-preferred":
                stats["int_preferred_steps"] += len(triples)
            else:
                stats["no_preference_steps"] += len(triples)

    return all_triples, dict(stats)


def main():
    parser = argparse.ArgumentParser(description="Death-aware 3-label labeling for SFT")
    parser.add_argument("--input_dirs", required=True, help="Comma-separated input directories")
    parser.add_argument("--output_dir", default="results/sft_data_death_aware/")
    args = parser.parse_args()

    input_dirs = [d.strip() for d in args.input_dirs.split(",")]
    os.makedirs(args.output_dir, exist_ok=True)

    all_triples = []
    per_task = {}
    totals = defaultdict(int)

    for d in input_dirs:
        triples, stats = process_dir(d)
        if not stats:
            continue
        task_type = os.path.basename(d.rstrip("/"))
        per_task[task_type] = stats
        all_triples.extend(triples)
        for k, v in stats.items():
            totals[k] += v

    out_path = os.path.join(args.output_dir, "sft_triples.jsonl")
    with open(out_path, "w") as f:
        for t in all_triples:
            f.write(json.dumps(t) + "\n")

    total_steps = (totals.get("det_preferred_steps", 0) +
                   totals.get("int_preferred_steps", 0) +
                   totals.get("no_preference_steps", 0))

    ep_label_map = {}
    for t in all_triples:
        ep_label_map[(t["task_type"], t["episode_id"], t["variation"])] = t["label"]
    ep_label_counts = defaultdict(int)
    for lbl in ep_label_map.values():
        ep_label_counts[lbl] += 1

    summary = {
        "total_episodes": totals["total_episodes"],
        "episode_labels": {
            "det-preferred": ep_label_counts.get("det-preferred", 0),
            "internal-preferred": ep_label_counts.get("internal-preferred", 0),
            "no-preference": ep_label_counts.get("no-preference", 0),
        },
        "signal_sources": {
            "det_wins_death": totals.get("det_wins_death", 0),
            "int_wins_death": totals.get("int_wins_death", 0),
            "det_wins_score": totals.get("det_wins_score", 0),
            "int_wins_score": totals.get("int_wins_score", 0),
            "ties": totals.get("ties", 0),
            "both_died": totals.get("both_died", 0),
        },
        "total_sft_steps": total_steps,
        "step_labels": {
            "det-preferred": totals.get("det_preferred_steps", 0),
            "internal-preferred": totals.get("int_preferred_steps", 0),
            "no-preference": totals.get("no_preference_steps", 0),
        },
        "per_task": per_task,
    }

    summary_path = os.path.join(args.output_dir, "labeling_summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)

    print("=== 3-LABEL DEATH-AWARE LABELING ===")
    print("Per-task breakdown:")
    for task, s in per_task.items():
        print(f"  {task}: {s['total_episodes']} episodes -> "
              f"det_death={s.get('det_wins_death',0)}, "
              f"int_death={s.get('int_wins_death',0)}, "
              f"det_score={s.get('det_wins_score',0)}, "
              f"int_score={s.get('int_wins_score',0)}, "
              f"tie={s.get('ties',0)}, "
              f"both_died={s.get('both_died',0)}")
    print()
    print(f"Episode labels: {dict(ep_label_counts)}")
    print(f"Total SFT steps: {total_steps}")
    print(f"  det-preferred: {totals.get('det_preferred_steps',0)}")
    print(f"  internal-preferred: {totals.get('int_preferred_steps',0)}")
    print(f"  no-preference: {totals.get('no_preference_steps',0)}")


if __name__ == "__main__":
    main()
