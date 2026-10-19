"""Construct DPO preference pairs from collected ALFWorld trajectories.

For each task_id with both success and failure trajectories:
  - chosen  = successful trajectory
  - rejected = failed trajectory (truncated to chosen_steps + 5)
  - prompt  = shared prefix (instruction + ICL + first observation)

Usage:
  python src/construct_preference.py \
    --trajectory_dir data/trajectories \
    --output_path data/dpo_pairs.jsonl
"""

import json
import argparse
import logging
from collections import defaultdict
from pathlib import Path

logger = logging.getLogger("construct_pref")


def load_trajectories(trajectory_dir: str) -> list:
    """Load all .jsonl trajectory files from directory."""
    trajs = []
    for p in sorted(Path(trajectory_dir).glob("*.jsonl")):
        with open(p) as f:
            for line in f:
                line = line.strip()
                if line:
                    trajs.append(json.loads(line))
    logger.info(f"Loaded {len(trajs)} trajectories from {trajectory_dir}")
    return trajs


def find_shared_prefix_len(conversations: list) -> int:
    """Find the number of messages that form the shared prefix.

    The prefix is: instruction + "OK" + ICL example turns + first task observation.
    We detect the boundary by finding the last user message before the first
    assistant response that contains "Action:".
    """
    for i, msg in enumerate(conversations):
        if msg["role"] == "assistant" and "Action:" in msg.get("content", ""):
            return i
    return len(conversations)


def truncate_rejected(rejected_turns: list, max_len: int) -> list:
    """Truncate rejected continuation to max_len messages.

    Ensures the last message is from assistant (not a dangling observation).
    """
    truncated = rejected_turns[:max_len]
    if truncated and truncated[-1]["role"] == "user":
        truncated.pop()
    return truncated


def build_pairs(trajs: list) -> list:
    """Build DPO preference pairs from trajectories.

    Groups trajectories by game_file basename, pairs successes with failures.
    """
    by_task = defaultdict(list)
    for t in trajs:
        game_id = t["game_file"].rsplit("/", 2)[-2] if "/" in t["game_file"] else t["game_file"]
        by_task[game_id].append(t)

    successes_by_task = {}
    failures_by_task = defaultdict(list)

    for game_id, task_trajs in by_task.items():
        for t in task_trajs:
            if t["reward"]:
                if game_id not in successes_by_task:
                    successes_by_task[game_id] = t
            else:
                failures_by_task[game_id].append(t)

    pairs = []
    for game_id, success_traj in successes_by_task.items():
        if game_id not in failures_by_task:
            continue

        convs = success_traj["conversations"]
        prefix_len = find_shared_prefix_len(convs)
        prompt = convs[:prefix_len]
        chosen = convs[prefix_len:]

        if chosen and chosen[-1]["role"] == "user":
            chosen.pop()
        if not chosen:
            continue

        chosen_msg_count = len(chosen)
        max_rejected_len = chosen_msg_count + 10  # ~5 extra steps (each step = 2 msgs)

        for fail_traj in failures_by_task[game_id]:
            fail_convs = fail_traj["conversations"]
            fail_prefix_len = find_shared_prefix_len(fail_convs)
            rejected = fail_convs[fail_prefix_len:]

            rejected = truncate_rejected(rejected, max_rejected_len)
            if not rejected:
                continue

            pairs.append({
                "task_id": game_id,
                "task_type": success_traj.get("task_type", ""),
                "prompt": prompt,
                "chosen": chosen,
                "rejected": rejected,
                "error_type": "",
            })

    return pairs


def main():
    parser = argparse.ArgumentParser("Construct DPO preference pairs")
    parser.add_argument("--trajectory_dir", type=str, required=True)
    parser.add_argument("--output_path", type=str, required=True)
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    trajs = load_trajectories(args.trajectory_dir)

    success_count = sum(1 for t in trajs if t["reward"])
    fail_count = len(trajs) - success_count
    logger.info(f"Success: {success_count}, Failure: {fail_count}")

    pairs = build_pairs(trajs)
    logger.info(f"Built {len(pairs)} preference pairs")

    output_path = Path(args.output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w") as f:
        for pair in pairs:
            f.write(json.dumps(pair, ensure_ascii=False) + "\n")

    logger.info(f"Saved to {output_path}")


if __name__ == "__main__":
    main()
