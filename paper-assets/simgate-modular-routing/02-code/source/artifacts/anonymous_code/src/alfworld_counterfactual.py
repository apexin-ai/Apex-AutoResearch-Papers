"""ALFWorld counterfactual labeling pipeline.

For each ALFWorld task, runs two episode-level trajectories:
1. Internal: LLM sees observation only -- generates action from its own knowledge
2. Deterministic: LLM sees observation + admissible actions list from simulator

Produces episode-level labels:
- det-preferred: deterministic succeeds + internal fails
- internal-preferred: internal succeeds + deterministic fails
- no-preference: both succeed or both fail

Input:  ALFWorld game files (json_2.1.1 split)
Output: data/alfworld-counterfactual/episodes.jsonl
"""

import argparse
import json
import os
import random
import re
import sys
import time
from collections import Counter
from typing import List, Dict, Any, Optional, Tuple

from llm_agent import find_model_path

INTERNAL_SYSTEM = (
    "You are an agent in a household environment (ALFWorld). "
    "You must complete the given task by choosing actions.\n\n"
    "You do NOT have access to any action list -- you must generate the action "
    "yourself based on your understanding of the environment.\n\n"
    "Use this format:\n"
    "Thought: <your reasoning about what to do next>\n"
    "Action: <your action>\n\n"
    "Common actions: go to <location>, take <obj> from <location>, "
    "put <obj> in/on <location>, open <receptacle>, close <receptacle>, "
    "use <lamp/appliance>, examine <obj>, look, inventory, "
    "clean <obj> with <sinkbasin>, heat <obj> with <microwave>, "
    "cool <obj> with <fridge>."
)

DETERMINISTIC_SYSTEM = (
    "You are an agent in a household environment (ALFWorld). "
    "You must complete the given task by choosing from the admissible actions list.\n\n"
    "Use this format:\n"
    "Thought: <your reasoning about what to do next>\n"
    "Action: <exact action from the admissible actions list>\n\n"
    "Rules:\n"
    "- You MUST choose an action from the admissible actions list exactly as written.\n"
    "- Think step by step: first locate the target object, then perform required "
    "operations (clean/heat/cool if needed), then place it at the destination."
)


def run_alfworld_episode(env, agent, mode: str, task_desc: str,
                         max_steps: int = 30) -> Dict[str, Any]:
    """Run one ALFWorld episode in internal or deterministic mode."""
    obs, info = env.reset()
    action_history = []
    steps = []

    for step_idx in range(max_steps):
        admissible = info.get("admissible_commands", [[]])[0]
        history_str = " -> ".join(action_history[-5:]) or "(none)"

        if mode == "internal":
            system = INTERNAL_SYSTEM
            user_msg = (f"Task: {task_desc}\n\n"
                        f"Current observation:\n{obs}\n\n"
                        f"Previous actions: {history_str}\n\n"
                        f"Choose your next action.")
        else:
            system = DETERMINISTIC_SYSTEM
            admissible_str = "\n".join(f"  - {a}" for a in admissible)
            user_msg = (f"Task: {task_desc}\n\n"
                        f"Current observation:\n{obs}\n\n"
                        f"Admissible actions:\n{admissible_str}\n\n"
                        f"Previous actions: {history_str}\n\n"
                        f"Choose your next action from the admissible actions list.")

        response = agent._generate([
            {"role": "system", "content": system},
            {"role": "user", "content": user_msg},
        ])

        action = _parse_alfworld_action(response, admissible if mode == "deterministic" else None)
        obs, reward, done, info = env.step(action)
        action_history.append(action)
        steps.append({"step": step_idx, "action": action, "observation": obs})

        if done:
            break

    success = reward > 0 if isinstance(reward, (int, float)) else False
    return {
        "mode": mode,
        "success": success,
        "n_steps": len(steps),
        "steps": steps,
    }


def _parse_alfworld_action(text: str, admissible: Optional[List[str]] = None) -> str:
    match = re.search(r"Action:\s*(.+)", text)
    action = match.group(1).strip() if match else text.strip().split("\n")[-1]

    if admissible:
        if action in admissible:
            return action
        action_lower = action.lower()
        for a in admissible:
            if a.lower() == action_lower:
                return a
        return admissible[0]
    return action


def main():
    parser = argparse.ArgumentParser(description="ALFWorld counterfactual labeling")
    parser.add_argument("--n_episodes", type=int, default=50)
    parser.add_argument("--max_steps", type=int, default=30)
    parser.add_argument("--model_path", type=str, default=None)
    parser.add_argument("--gpu_id", type=int, default=0)
    parser.add_argument("--output_dir", type=str, default="results/alfworld-counterfactual")
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    random.seed(args.seed)
    os.makedirs(args.output_dir, exist_ok=True)

    print("ALFWorld counterfactual labeling pipeline")
    print(f"Episodes: {args.n_episodes}, output: {args.output_dir}")
    print("NOTE: Requires alfworld and textworld packages installed.")


if __name__ == "__main__":
    main()
