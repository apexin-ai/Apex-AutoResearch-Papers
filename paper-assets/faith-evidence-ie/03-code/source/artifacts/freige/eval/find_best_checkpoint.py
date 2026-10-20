"""从 GRPO 实验目录的 trainer_state.json 找到 reward 最高的 checkpoint。

用法:
    python -m freige.eval.find_best_checkpoint /root/autodl-tmp/grpo_extract_r3/
"""

import argparse
import json
import sys
from pathlib import Path


def find_best_checkpoint(experiment_dir: str) -> dict | None:
    """解析 trainer_state.json，返回 reward 最高且实际存在的 checkpoint 信息。

    Returns:
        {"path": str, "step": int, "reward": float} or None
    """
    exp_path = Path(experiment_dir)

    ckpt_dirs = sorted(exp_path.glob("checkpoint-*"), key=lambda p: _step_from_dir(p))
    if not ckpt_dirs:
        print(f"ERROR: no checkpoint-* dirs found in {exp_path}", file=sys.stderr)
        return None

    trainer_state_path = ckpt_dirs[-1] / "trainer_state.json"
    if not trainer_state_path.exists():
        for d in reversed(ckpt_dirs):
            candidate = d / "trainer_state.json"
            if candidate.exists():
                trainer_state_path = candidate
                break
        else:
            print(f"ERROR: no trainer_state.json found in any checkpoint", file=sys.stderr)
            return None

    with open(trainer_state_path) as f:
        state = json.load(f)

    log_history = state.get("log_history", [])
    if not log_history:
        print(f"ERROR: log_history is empty", file=sys.stderr)
        return None

    existing_steps = {_step_from_dir(d) for d in ckpt_dirs}

    best_entry = None
    best_reward = float("-inf")
    for entry in log_history:
        reward = entry.get("reward")
        step = entry.get("step")
        if reward is None or step is None:
            continue
        if step not in existing_steps:
            continue
        if reward > best_reward:
            best_reward = reward
            best_entry = entry

    if best_entry is None:
        print(f"ERROR: no valid reward entries matching existing checkpoints", file=sys.stderr)
        return None

    best_step = best_entry["step"]
    best_path = exp_path / f"checkpoint-{best_step}"

    return {
        "path": str(best_path),
        "step": best_step,
        "reward": best_reward,
    }


def _step_from_dir(ckpt_dir: Path) -> int:
    return int(ckpt_dir.name.split("-")[-1])


def main():
    parser = argparse.ArgumentParser(
        description="Find the best checkpoint by reward in a GRPO experiment."
    )
    parser.add_argument("experiment_dir", help="Path to GRPO experiment directory")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    result = find_best_checkpoint(args.experiment_dir)
    if result is None:
        sys.exit(1)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Best checkpoint: {result['path']}")
        print(f"  Step:   {result['step']}")
        print(f"  Reward: {result['reward']:.6f}")


if __name__ == "__main__":
    main()
