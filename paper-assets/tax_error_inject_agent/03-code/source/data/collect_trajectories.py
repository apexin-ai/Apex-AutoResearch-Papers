#!/usr/bin/env python3
"""Collect ALFWorld trajectories using GPT model via OpenAI-compatible API."""

import argparse
import json
import os
import random
import re
import sys
import time
import threading
from collections import defaultdict
from difflib import SequenceMatcher
from concurrent.futures import ThreadPoolExecutor, as_completed

import textworld
import textworld.gym
from alfworld.agents.environment.alfred_tw_env import AlfredDemangler, AlfredInfos

from openai import OpenAI

TASK_TYPES = {
    1: "pick_and_place_simple",
    2: "look_at_obj_in_light",
    3: "pick_clean_then_place_in_recep",
    4: "pick_heat_then_place_in_recep",
    5: "pick_cool_then_place_in_recep",
    6: "pick_two_obj_and_place",
}
TASK_TYPE_NAMES = list(TASK_TYPES.values())

API_KEY = "[REDACTED]"
BASE_URL = "http://47.94.22.126/v1"
MODEL = "openai/gpt-5.2"

MAX_STEPS = 50
HISTORY_WINDOW = 10

write_lock = threading.Lock()
counter_lock = threading.Lock()


def build_prompt(task_desc, step_count, history, current_obs, admissible_commands):
    history_str = ""
    for h in history[-HISTORY_WINDOW:]:
        history_str += f"Observation: {h['observation']}\nAction: {h['action']}\n"
    actions_str = ", ".join(admissible_commands)
    return f"""You are an expert agent operating in the ALFRED Embodied Environment.
Your task is to: {task_desc}
Prior to this step, you have already taken {step_count} step(s).
Below are the most recent observations and actions:
{history_str}
Your current observation is: {current_obs}
Your admissible actions are: [{actions_str}]

Think step by step in <think></think> tags, then choose an action in <action></action> tags.
The action MUST be one of the admissible actions listed above."""


def parse_response(response_text):
    think_match = re.search(r"<think>(.*?)</think>", response_text, re.DOTALL)
    action_match = re.search(r"<action>(.*?)</action>", response_text, re.DOTALL)
    think = think_match.group(1).strip() if think_match else ""
    action = action_match.group(1).strip() if action_match else ""
    return think, action


def fuzzy_match_action(action, admissible_commands):
    action_lower = action.lower().strip()
    for cmd in admissible_commands:
        if cmd.lower().strip() == action_lower:
            return cmd
    best_match = None
    best_ratio = 0.0
    for cmd in admissible_commands:
        ratio = SequenceMatcher(None, action_lower, cmd.lower().strip()).ratio()
        if ratio > best_ratio:
            best_ratio = ratio
            best_match = cmd
    if best_ratio > 0.7:
        return best_match
    return None


def collect_game_files(data_path):
    games_by_type = defaultdict(list)
    for root, dirs, files in os.walk(data_path, topdown=False):
        if "traj_data.json" not in files or "game.tw-pddl" not in files:
            continue
        if "movable" in root or "Sliced" in root:
            continue
        json_path = os.path.join(root, "traj_data.json")
        game_path = os.path.join(root, "game.tw-pddl")
        with open(json_path) as f:
            traj_data = json.load(f)
        task_type = traj_data["task_type"]
        if task_type not in TASK_TYPE_NAMES:
            continue
        with open(game_path) as f:
            gamedata = json.load(f)
        if not gamedata.get("solvable", False):
            continue
        anns = traj_data.get("turk_annotations", {}).get("anns", [])
        task_desc = anns[0]["task_desc"] if anns else task_type.replace("_", " ")
        games_by_type[task_type].append({
            "game_file": game_path,
            "task_type": task_type,
            "task_desc": task_desc,
            "gamefile_dir": root,
        })
    return games_by_type


def sample_games(games_by_type, num_total, seed=42):
    rng = random.Random(seed)
    per_type = num_total // len(games_by_type)
    remainder = num_total % len(games_by_type)
    sampled = []
    types_sorted = sorted(games_by_type.keys())
    for i, t in enumerate(types_sorted):
        n = per_type + (1 if i < remainder else 0)
        pool = games_by_type[t]
        rng.shuffle(pool)
        sampled.extend(pool[:n])
    rng.shuffle(sampled)
    return sampled


def load_existing_trajectories(output_dir):
    existing = set()
    for fname in ["successful_trajectories.jsonl", "failed_trajectories.jsonl"]:
        path = os.path.join(output_dir, fname)
        if os.path.exists(path):
            with open(path) as f:
                for line in f:
                    try:
                        traj = json.loads(line.strip())
                        existing.add(traj.get("gamefile_dir", ""))
                    except (json.JSONDecodeError, KeyError):
                        pass
    return existing


def play_episode(client, game_file, task_desc, task_type, episode_id=""):
    request_infos = textworld.EnvInfos(
        won=True, admissible_commands=True, extras=["gamefile"],
    )
    alfred_demangler = AlfredDemangler(shuffle=False)
    env_id = textworld.gym.register_games(
        [game_file], request_infos,
        batch_size=1, max_episode_steps=MAX_STEPS,
        wrappers=[alfred_demangler, AlfredInfos],
    )
    env = textworld.gym.make(env_id)
    obs, infos = env.reset()
    obs_text = obs[0] if isinstance(obs, (list, tuple)) else obs

    steps = []
    history = []
    done = False
    won = False
    step_count = 0

    while not done and step_count < MAX_STEPS:
        admissible = infos.get("admissible_commands", [[]])[0]
        if not admissible:
            break
        prompt = build_prompt(task_desc, step_count, history, obs_text, admissible)

        response_text = None
        for attempt in range(3):
            try:
                response = client.chat.completions.create(
                    model=MODEL,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.0,
                    max_tokens=512,
                )
                response_text = response.choices[0].message.content
                break
            except Exception as e:
                if attempt < 2:
                    time.sleep(3 * (attempt + 1))
                else:
                    print(f"  [{episode_id}] API failed after 3 attempts: {e}", flush=True)

        if response_text is None:
            break

        think, action = parse_response(response_text)
        if not action:
            action = response_text.strip().split("\n")[-1].strip()

        matched_action = fuzzy_match_action(action, admissible)
        if matched_action is None:
            matched_action = admissible[0]

        steps.append({
            "step": step_count,
            "observation": obs_text,
            "admissible_commands": admissible,
            "think": think,
            "action": matched_action,
            "raw_action": action if action != matched_action else None,
        })
        history.append({"observation": obs_text, "action": matched_action})

        obs, scores, dones, infos = env.step([matched_action])
        obs_text = obs[0] if isinstance(obs, (list, tuple)) else obs
        done = dones[0] if isinstance(dones, (list, tuple)) else dones
        won = infos.get("won", [False])[0]
        step_count += 1

    env.close()
    return steps, won, step_count


class TrajectoryCollector:
    def __init__(self, output_dir, num_target):
        self.output_dir = output_dir
        self.num_target = num_target
        self.success_count = 0
        self.fail_count = 0
        self.total_attempted = 0
        self.type_success_counts = defaultdict(int)
        self.existing = set()

        os.makedirs(output_dir, exist_ok=True)
        self.success_path = os.path.join(output_dir, "successful_trajectories.jsonl")
        self.failed_path = os.path.join(output_dir, "failed_trajectories.jsonl")

        self._load_existing()

        self.success_f = open(self.success_path, "a")
        self.failed_f = open(self.failed_path, "a")

    def _load_existing(self):
        self.existing = load_existing_trajectories(self.output_dir)
        for path in [self.success_path, self.failed_path]:
            if os.path.exists(path):
                with open(path) as f:
                    for line in f:
                        try:
                            t = json.loads(line.strip())
                            if t.get("success"):
                                self.success_count += 1
                                self.type_success_counts[t["task_type"]] += 1
                            else:
                                self.fail_count += 1
                            self.total_attempted += 1
                        except (json.JSONDecodeError, KeyError):
                            pass

    def should_continue(self):
        return self.success_count < self.num_target

    def is_done(self, gamefile_dir):
        return gamefile_dir in self.existing

    def record(self, traj):
        with write_lock:
            self.total_attempted += 1
            if traj["success"]:
                self.success_f.write(json.dumps(traj, ensure_ascii=False) + "\n")
                self.success_f.flush()
                self.success_count += 1
                self.type_success_counts[traj["task_type"]] += 1
            else:
                self.failed_f.write(json.dumps(traj, ensure_ascii=False) + "\n")
                self.failed_f.flush()
                self.fail_count += 1
            self.existing.add(traj["gamefile_dir"])

    def print_progress(self):
        rate = self.success_count / max(self.total_attempted, 1) * 100
        print(f"--- Progress: {self.success_count}/{self.num_target} success, "
              f"{self.fail_count} fail, {self.total_attempted} total, "
              f"rate={rate:.1f}% ---", flush=True)

    def close(self):
        self.success_f.close()
        self.failed_f.close()


def run_episode(args):
    client, game_info, collector, idx = args
    if not collector.should_continue():
        return
    if collector.is_done(game_info["gamefile_dir"]):
        return

    game_id = f"traj_{idx:04d}"
    task_short = game_info["task_desc"][:50]
    print(f"[{idx}] {game_id} | {game_info['task_type']} | {task_short}...", flush=True)

    try:
        steps, won, num_steps = play_episode(
            client, game_info["game_file"],
            game_info["task_desc"], game_info["task_type"],
            episode_id=game_id,
        )
    except Exception as e:
        print(f"  [{game_id}] Episode error: {e}", flush=True)
        traj = {
            "id": game_id, "task_type": game_info["task_type"],
            "task_desc": game_info["task_desc"],
            "gamefile": game_info["game_file"],
            "gamefile_dir": game_info["gamefile_dir"],
            "num_steps": 0, "success": False, "steps": [], "error": str(e),
        }
        collector.record(traj)
        return

    traj = {
        "id": game_id, "task_type": game_info["task_type"],
        "task_desc": game_info["task_desc"],
        "gamefile": game_info["game_file"],
        "gamefile_dir": game_info["gamefile_dir"],
        "num_steps": num_steps, "success": won, "steps": steps,
    }
    collector.record(traj)

    status = "SUCCESS" if won else "FAILED"
    print(f"  [{game_id}] {status} in {num_steps} steps | "
          f"success={collector.success_count}/{collector.num_target}", flush=True)

    if collector.total_attempted % 10 == 0:
        collector.print_progress()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--num_trajectories", type=int, default=500)
    parser.add_argument("--output_dir", type=str, default="data/trajectories/")
    parser.add_argument("--data_path", type=str,
                        default="/root/autodl-tmp/alfworld_data/json_2.1.1/train")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()

    print("Collecting game files...", flush=True)
    games_by_type = collect_game_files(args.data_path)
    for t, games in sorted(games_by_type.items()):
        print(f"  {t}: {len(games)} games", flush=True)
    total_games = sum(len(g) for g in games_by_type.values())
    print(f"  Total: {total_games} valid games", flush=True)

    if total_games == 0:
        print("ERROR: No valid game files found. Run alfworld-generate first.")
        return

    num_to_attempt = int(args.num_trajectories * 1.15)
    sampled = sample_games(games_by_type, min(num_to_attempt, total_games), args.seed)
    print(f"Sampled {len(sampled)} games to attempt", flush=True)

    collector = TrajectoryCollector(args.output_dir, args.num_trajectories)
    print(f"Resuming from {collector.success_count} successes, "
          f"{collector.fail_count} failures", flush=True)

    tasks = []
    for idx, game_info in enumerate(sampled, 1):
        if game_info["gamefile_dir"] in collector.existing:
            continue
        client = OpenAI(api_key=[REDACTED], base_url=BASE_URL)
        tasks.append((client, game_info, collector, idx))

    print(f"Running {len(tasks)} episodes with {args.workers} workers...", flush=True)
    t0 = time.time()

    if args.workers <= 1:
        for task in tasks:
            if not collector.should_continue():
                break
            run_episode(task)
    else:
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = []
            for task in tasks:
                if not collector.should_continue():
                    break
                futures.append(executor.submit(run_episode, task))
            for f in as_completed(futures):
                try:
                    f.result()
                except Exception as e:
                    print(f"Worker error: {e}", flush=True)
                if not collector.should_continue():
                    break

    elapsed = time.time() - t0
    collector.close()

    print(f"\n=== Final Results ({elapsed:.0f}s) ===", flush=True)
    print(f"Successful: {collector.success_count}", flush=True)
    print(f"Failed: {collector.fail_count}", flush=True)
    print(f"Total: {collector.total_attempted}", flush=True)
    rate = collector.success_count / max(collector.total_attempted, 1) * 100
    print(f"Success rate: {rate:.1f}%", flush=True)
    print(f"\nBy task type:", flush=True)
    for t in sorted(collector.type_success_counts.keys()):
        print(f"  {t}: {collector.type_success_counts[t]}", flush=True)
    print(f"\nOutput: {args.output_dir}", flush=True)


if __name__ == "__main__":
    main()
