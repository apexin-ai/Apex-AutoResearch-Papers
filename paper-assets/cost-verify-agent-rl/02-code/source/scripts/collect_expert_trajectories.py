#!/usr/bin/env python3
"""Collect expert trajectories from ALFWorld using HandCodedTWAgent.

Plays all train games with the built-in expert agent, records
(observation, expert_action) pairs, converts to SFT format matching
existing data in alfworld_sft_ragen.jsonl, and saves only successful
trajectories.
"""

import os
import json
import random
import traceback
import argparse
from collections import Counter

import textworld
from alfworld.agents.expert import HandCodedTWAgent, HandCodedAgentTimeout, HandCodedAgentFailed
from alfworld.agents.environment.alfred_tw_env import AlfredDemangler, AlfredInfos


SYSTEM_PROMPT = (
    "You're a helpful assistant. You are an expert agent in the ALFRED Embodied Environment.\n"
    "Complete household tasks by navigating and interacting with objects.\n\n"
    "Before each action, you MUST first produce a self-guidance assessment:\n"
    "[Assessment: positive/neutral/negative] - evaluate your current progress.\n"
    "[Reasoning: one sentence analyzing what has been accomplished and what remains.]\n"
    "[Suggestion: the best next action from admissible actions.]\n\n"
    "Your reasoning with self-guidance MUST be enclosed within <think> </think> tags.\n"
    "Then choose an admissible action and present it within <answer>...</answer> tags."
)

SUPPORTED_TASK_TYPES = {
    "pick_and_place_simple",
    "look_at_obj_in_light",
    "pick_clean_then_place_in_recep",
    "pick_heat_then_place_in_recep",
    "pick_cool_then_place_in_recep",
    "pick_two_obj_and_place",
}

ALL_KNOWN_TASK_TYPES = SUPPORTED_TASK_TYPES | {"pick_and_place_with_movable_recep"}


def find_game_files(data_dir, split="train"):
    split_dir = os.path.join(data_dir, split)
    game_files = []
    skipped = Counter()

    for task_dir in sorted(os.listdir(split_dir)):
        task_path = os.path.join(split_dir, task_dir)
        if not os.path.isdir(task_path):
            continue

        task_type = None
        for tt in ALL_KNOWN_TASK_TYPES:
            if task_dir.startswith(tt + "-"):
                task_type = tt
                break

        if task_type is None or task_type not in SUPPORTED_TASK_TYPES:
            skipped[task_type or "unknown"] += 1
            continue

        for trial_dir in sorted(os.listdir(task_path)):
            trial_path = os.path.join(task_path, trial_dir)
            if not os.path.isdir(trial_path):
                continue
            game_file = os.path.join(trial_path, "game.tw-pddl")
            traj_file = os.path.join(trial_path, "traj_data.json")
            if os.path.exists(game_file) and os.path.exists(traj_file):
                game_files.append(game_file)

    if skipped:
        print(f"Skipped task types: {dict(skipped)}")
    return game_files


def clean_obs(obs):
    if "-= Welcome to TextWorld, ALFRED! =-" in obs:
        obs = obs.split("-= Welcome to TextWorld, ALFRED! =-")[-1]
    return obs.strip()


def infer_assessment(prev_obs, action):
    p = prev_obs.lower()
    a = (action or "").lower()

    if "you pick up" in p or "you take" in p:
        return "positive", "Successfully picked up the object."
    if "you put" in p or "you move" in p:
        return "positive", "Successfully placed the object."
    if "nothing happens" in p:
        return "negative", "Action had no effect. Need a different approach."
    if "you open" in p:
        return "neutral", "Opened the receptacle to check contents."
    if "you clean" in p:
        return "positive", "Successfully cleaned the object."
    if "you heat" in p:
        return "positive", "Successfully heated the object."
    if "you cool" in p:
        return "positive", "Successfully cooled the object."
    if "you use" in p:
        return "positive", "Used the lamp to examine the object."
    if "closed" in p:
        return "neutral", "Found a closed receptacle. Should open it."
    if "you see nothing" in p:
        return "negative", "Nothing useful here. Searching elsewhere."
    if "you see" in p:
        return "neutral", "Observing the area for the target object."

    if "go to" in a:
        return "neutral", "Moving to check another location."
    if "look" in a:
        return "neutral", "Looking around to assess the situation."
    return "neutral", "Continuing to work on the task."


def trajectory_to_sft(trajectory):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    init_obs = clean_obs(trajectory[0]["obs"])
    messages.append({"role": "user", "content": init_obs})

    for i in range(1, len(trajectory)):
        entry = trajectory[i]
        action = entry["action"]
        obs = clean_obs(entry["obs"])
        is_last = (i == len(trajectory) - 1)
        prev_obs = clean_obs(trajectory[i - 1]["obs"])

        if is_last:
            assessment, reasoning = "positive", "Task completed successfully."
        else:
            assessment, reasoning = infer_assessment(prev_obs, action)

        assistant_content = (
            f"<think>[Assessment: {assessment}] "
            f"[Reasoning: {reasoning}] "
            f"[Suggestion: {action}]</think>"
            f"<answer>{action}</answer>"
        )
        messages.append({"role": "assistant", "content": assistant_content})

        if not is_last:
            messages.append({"role": "user", "content": obs})

    return {"messages": messages}


def collect_single_game(env, agent, game_file, max_steps=150):
    try:
        env.load(game_file)
        state = env.reset()
    except Exception as e:
        return None, f"load_error: {e}"

    try:
        agent.reset(game=game_file)
        agent.observe(state.feedback)
    except Exception as e:
        return None, f"agent_init_error: {e}"

    done = False
    prev_action = ""
    trajectory = [{"obs": state.feedback, "action": None}]

    for step in range(max_steps):
        try:
            action = agent.act(state, 0, done, prev_action)
        except (HandCodedAgentTimeout, HandCodedAgentFailed):
            return None, "agent_failed"
        except Exception as e:
            return None, f"act_error: {e}"

        try:
            state, reward, done = env.step(action)
        except Exception as e:
            return None, f"step_error: {e}"

        prev_action = action
        trajectory.append({"obs": state.feedback, "action": action})

        if done:
            break

    won = state.get("won", False) if hasattr(state, "get") else getattr(state, "won", False)
    if won:
        return trajectory, "ok"
    return None, "not_won"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", default="/root/autodl-tmp/alfworld/json_2.1.1")
    parser.add_argument("--output-dir", default="/root/autodl-tmp/expert_trajectories/")
    parser.add_argument("--max-games", type=int, default=0, help="0 = all")
    parser.add_argument("--max-steps", type=int, default=150)
    parser.add_argument("--split", default="train")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    output_file = os.path.join(args.output_dir, "expert_trajectories.jsonl")
    progress_file = os.path.join(args.output_dir, "progress.json")

    game_files = find_game_files(args.data_dir, args.split)
    print(f"Found {len(game_files)} game files in {args.split} split")

    if args.max_games > 0:
        game_files = game_files[:args.max_games]
        print(f"Limited to {args.max_games} games")

    completed = set()
    if os.path.exists(progress_file):
        with open(progress_file) as f:
            progress = json.load(f)
            completed = set(progress.get("completed", []))
        print(f"Resuming: {len(completed)} already done")

    remaining = [gf for gf in game_files if gf not in completed]
    print(f"Remaining: {len(remaining)} games to process")

    if not remaining:
        print("Nothing to do.")
        return

    request_infos = textworld.EnvInfos(
        won=True,
        admissible_commands=True,
        facts=True,
    )

    def make_demangler(env):
        return AlfredDemangler(env, shuffle=False)

    env = textworld.start(
        remaining[0],
        request_infos=request_infos,
        wrappers=[make_demangler, AlfredInfos],
    )
    agent = HandCodedTWAgent(max_steps=args.max_steps)

    stats = Counter()
    success_count = sum(1 for _ in open(output_file)) if os.path.exists(output_file) else 0
    print(f"Existing successful trajectories: {success_count}")

    for idx, game_file in enumerate(remaining):
        trajectory, status = collect_single_game(env, agent, game_file, args.max_steps)

        if status == "ok" and trajectory:
            sft_data = trajectory_to_sft(trajectory)
            with open(output_file, "a") as f:
                f.write(json.dumps(sft_data, ensure_ascii=False) + "\n")
            success_count += 1

        completed.add(game_file)
        stats[status] += 1

        if (idx + 1) % 100 == 0 or idx == len(remaining) - 1:
            with open(progress_file, "w") as f:
                json.dump({"completed": list(completed)}, f)
            print(
                f"[{idx + 1}/{len(remaining)}] "
                f"success={success_count} | "
                f"stats={dict(stats)}"
            )

    env.close()
    print(f"\nDone. Total successful trajectories: {success_count}")
    print(f"Final stats: {dict(stats)}")
    print(f"Output: {output_file}")


if __name__ == "__main__":
    main()
