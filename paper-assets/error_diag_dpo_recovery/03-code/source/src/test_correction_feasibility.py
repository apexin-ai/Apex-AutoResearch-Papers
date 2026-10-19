"""Correction feasibility test: fresh-start attempts on ALFWorld tasks.

Verifies whether Qwen3-8B/14B can succeed on ALFWorld tasks with multiple
stochastic attempts from scratch. For each selected task, creates a fresh
ALFWorld env and runs max_attempts episodes.

Usage:
  python src/test_correction_feasibility.py \
    --model_name /root/autodl-tmp/.hf_cache/Qwen3-8B \
    --gpu 0 --num_tasks 10 --max_attempts 10

  python src/test_correction_feasibility.py \
    --trajectory_file data/trajectories/train_part0.jsonl \
    --model_name /root/autodl-tmp/.hf_cache/Qwen3-14B-AWQ \
    --gpu 1 --num_tasks 10 --max_attempts 10 \
    --output_path data/feasibility_14b.json
"""

import os
import sys
import json
import time
import logging
import argparse
from pathlib import Path
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import yaml
import textworld
import textworld.gym
from tqdm import tqdm
from alfworld.agents.environment import get_environment
from alfworld.agents.environment.alfred_tw_env import AlfredDemangler, AlfredInfos

from collect_trajectories import (
    load_model,
    load_prompt_resources,
    collect_single_trajectory,
    get_task_type,
)

logger = logging.getLogger("feasibility_test")

ALFWORLD_DATA = "/root/autodl-tmp/alfworld_data"


def get_game_files_and_config(split):
    os.environ["ALFWORLD_DATA"] = ALFWORLD_DATA
    with open(os.path.join(ALFWORLD_DATA, "base_config.yaml")) as f:
        config = yaml.safe_load(f)
    split_map = {
        "train": "train",
        "dev": "eval_in_distribution",
        "test": "eval_out_of_distribution",
    }
    EnvClass = get_environment(config["env"]["type"])
    tw_env = EnvClass(config, train_eval=split_map[split])
    return [str(gf) for gf in tw_env.game_files], config


def select_tasks(game_files, num_tasks, trajectory_file=None):
    if trajectory_file and os.path.exists(trajectory_file):
        failed = []
        with open(trajectory_file) as f:
            for line in f:
                traj = json.loads(line)
                if not traj["reward"]:
                    failed.append(traj)
        gf_to_idx = {gf: i for i, gf in enumerate(game_files)}
        by_type = defaultdict(list)
        for t in failed:
            gf = t["game_file"]
            if gf in gf_to_idx:
                by_type[t["task_type"]].append({
                    "global_idx": gf_to_idx[gf],
                    "game_file": gf,
                    "task_type": t["task_type"],
                })
        matched = sum(len(v) for v in by_type.values())
        logger.info(
            "Loaded %d failed trajectories, %d matched game files",
            len(failed), matched,
        )
    else:
        by_type = defaultdict(list)
        for i, gf in enumerate(game_files):
            tt = get_task_type(gf)
            by_type[tt].append({
                "global_idx": i, "game_file": gf, "task_type": tt,
            })

    selected = []
    types = sorted(by_type.keys())
    per_type = max(1, num_tasks // max(len(types), 1))

    for tt in types:
        for item in by_type[tt][:per_type]:
            selected.append(item)
    if len(selected) < num_tasks:
        for tt in types:
            for item in by_type[tt][per_type:]:
                if len(selected) >= num_tasks:
                    break
                selected.append(item)
            if len(selected) >= num_tasks:
                break

    selected = selected[:num_tasks]
    selected.sort(key=lambda x: x["global_idx"])
    return selected


def create_env(game_files_subset, config):
    training_method = config["general"]["training_method"]
    if training_method == "dqn":
        max_ep_steps = config["rl"]["training"]["max_nb_steps_per_episode"]
    elif training_method == "dagger":
        max_ep_steps = config["dagger"]["training"]["max_nb_steps_per_episode"]
    else:
        max_ep_steps = 100

    wrappers = [AlfredDemangler(shuffle=False), AlfredInfos]
    request_infos = textworld.EnvInfos(
        won=True, admissible_commands=True, extras=["gamefile"],
    )
    env_id = textworld.gym.register_games(
        game_files_subset, request_infos,
        batch_size=1, asynchronous=True,
        max_episode_steps=max_ep_steps,
        wrappers=wrappers,
    )
    return textworld.gym.make(env_id)


def save_results(path, args, per_task, total_ep, total_succ):
    by_type = defaultdict(lambda: {"total": 0, "success": 0})
    for t in per_task:
        tt = t["task_type"]
        by_type[tt]["total"] += t["attempts"]
        by_type[tt]["success"] += t["successes"]
    for v in by_type.values():
        v["rate"] = round(v["success"] / max(v["total"], 1), 4)

    result = {
        "model": os.path.basename(args.model_name),
        "temperature": args.temperature,
        "max_steps": args.max_steps,
        "num_tasks": len(per_task),
        "max_attempts": args.max_attempts,
        "total_episodes": total_ep,
        "total_successes": total_succ,
        "success_rate": round(total_succ / max(total_ep, 1), 4),
        "per_task": [
            {
                "task_id": t["task_id"],
                "task_type": t["task_type"],
                "game_file": t["game_file"],
                "attempts": t["attempts"],
                "successes": t["successes"],
                "rate": round(t["successes"] / max(t["attempts"], 1), 4),
                "episode_details": t["episode_details"],
            }
            for t in per_task
        ],
        "per_type": dict(by_type),
    }
    with open(path, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)


def main():
    parser = argparse.ArgumentParser(
        description="Correction feasibility: fresh-start attempts on ALFWorld tasks",
    )
    parser.add_argument(
        "--trajectory_file", type=str, default=None,
        help="Failed trajectory JSONL for task selection (optional)",
    )
    parser.add_argument(
        "--model_name", type=str,
        default="/root/autodl-tmp/.hf_cache/Qwen3-8B",
        help="Model path",
    )
    parser.add_argument("--gpu", type=int, default=0, help="GPU device index")
    parser.add_argument(
        "--num_tasks", type=int, default=10, help="Number of tasks to test",
    )
    parser.add_argument(
        "--max_attempts", type=int, default=10, help="Attempts per task",
    )
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument(
        "--max_steps", type=int, default=40,
        help="Max interaction steps per episode",
    )
    parser.add_argument("--max_new_tokens", type=int, default=256)
    parser.add_argument(
        "--split", type=str, default="train",
        choices=["train", "dev", "test"],
    )
    parser.add_argument(
        "--output_path", type=str,
        default="data/feasibility_test_results.json",
        help="Output JSON path",
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s",
    )

    logger.info("Loading game file list...")
    game_files, config = get_game_files_and_config(args.split)
    logger.info("Found %d games in %s split", len(game_files), args.split)

    logger.info("Selecting tasks...")
    tasks = select_tasks(game_files, args.num_tasks, args.trajectory_file)
    type_dist = defaultdict(int)
    for t in tasks:
        type_dist[t["task_type"]] += 1
    logger.info("Selected %d tasks: %s", len(tasks), dict(type_dist))
    for t in tasks:
        logger.info("  idx=%d type=%s", t["global_idx"], t["task_type"])

    logger.info("Loading model: %s", args.model_name)
    model, tokenizer = load_model(args.model_name, args.gpu)
    instruction, icl_examples = load_prompt_resources()

    selected_gfs = [t["game_file"] for t in tasks]
    per_task = [
        {
            "task_id": t["global_idx"],
            "task_type": t["task_type"],
            "game_file": t["game_file"],
            "attempts": 0,
            "successes": 0,
            "episode_details": [],
        }
        for t in tasks
    ]

    output_path = Path(args.output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    total_ep = 0
    total_succ = 0
    total_target = args.max_attempts * len(tasks)
    pbar = tqdm(total=total_target, desc="Episodes")

    for attempt in range(args.max_attempts):
        env = create_env(selected_gfs, config)

        for ti in range(len(tasks)):
            obs, info = env.reset()
            obs_text = "\n".join(obs[0].split("\n\n")[1:])
            game_file = info["extra.gamefile"][0]

            task_info = {
                "task_id": tasks[ti]["global_idx"],
                "game_file": game_file,
                "obs": obs_text,
                "env": env,
            }

            t0 = time.time()
            traj = collect_single_trajectory(
                task_info, model, tokenizer,
                instruction, icl_examples,
                temperature=args.temperature,
                max_steps=args.max_steps,
                max_new_tokens=args.max_new_tokens,
            )
            elapsed = time.time() - t0

            total_ep += 1
            if traj["reward"]:
                total_succ += 1
            per_task[ti]["attempts"] += 1
            if traj["reward"]:
                per_task[ti]["successes"] += 1
            per_task[ti]["episode_details"].append({
                "attempt": attempt,
                "reward": traj["reward"],
                "steps": traj["steps"],
                "time": round(elapsed, 1),
            })

            pbar.update(1)
            pbar.set_postfix(sr=f"{total_succ}/{total_ep}")
            logger.info(
                "[%d/%d] attempt=%d task=%d type=%s reward=%s steps=%d "
                "time=%.1fs sr=%d/%d",
                total_ep, total_target, attempt, tasks[ti]["global_idx"],
                tasks[ti]["task_type"], traj["reward"], traj["steps"],
                elapsed, total_succ, total_ep,
            )

            save_results(output_path, args, per_task, total_ep, total_succ)

        env.close()

    pbar.close()
    sr = total_succ / max(total_ep, 1)
    logger.info(
        "Done. %d/%d succeeded (%.1f%%)", total_succ, total_ep, sr * 100,
    )
    logger.info("Results: %s", output_path)


if __name__ == "__main__":
    main()
