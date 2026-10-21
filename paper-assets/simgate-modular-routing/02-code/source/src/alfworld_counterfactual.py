"""ALFWorld counterfactual labeling pipeline.

For each ALFWorld task, runs two episode-level trajectories:
1. Internal: LLM sees observation only — generates action from its own knowledge
2. Deterministic: LLM sees observation + admissible actions list from simulator

The admissible actions list is the "deterministic computation" source:
it constrains the LLM to valid simulator actions.

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

import textworld
import textworld.gym
from alfworld.agents.environment.alfred_tw_env import AlfredDemangler, AlfredInfos

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from llm_agent import find_model_path, sanitize_messages_for_template

# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------

INTERNAL_SYSTEM = (
    "You are an agent in a household environment (ALFWorld). "
    "You must complete the given task by choosing actions.\n\n"
    "You do NOT have access to any action list — you must generate the action "
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

USER_TEMPLATE_INTERNAL = (
    "Task: {task_desc}\n\n"
    "Current observation:\n{observation}\n\n"
    "Previous actions: {history}\n\n"
    "Choose your next action."
)

USER_TEMPLATE_DETERMINISTIC = (
    "Task: {task_desc}\n\n"
    "Current observation:\n{observation}\n\n"
    "Admissible actions:\n{admissible_str}\n\n"
    "Previous actions: {history}\n\n"
    "Choose your next action from the admissible actions list."
)

# ---------------------------------------------------------------------------
# Task types
# ---------------------------------------------------------------------------

TASK_TYPES = [
    "pick_and_place",
    "pick_clean_then_place",
    "pick_heat_then_place",
    "pick_cool_then_place",
    "look_at_obj_in_light",
    "pick_two_obj_and_place",
]


# ---------------------------------------------------------------------------
# Action parsing
# ---------------------------------------------------------------------------

def parse_action_free(text: str) -> Optional[str]:
    """Parse free-form action from LLM output (internal mode)."""
    m = re.search(r"Action:\s*(.+?)(?:\n|$)", text, re.IGNORECASE)
    if m:
        return m.group(1).strip().strip('"').strip("'")
    lines = [l.strip() for l in text.strip().split("\n") if l.strip()]
    if lines:
        return lines[-1].strip().strip('"').strip("'")
    return None


def match_to_admissible(free_action: str, admissible: List[str]) -> Optional[str]:
    """Best-effort match a free-form action string to admissible actions."""
    if free_action in admissible:
        return free_action
    fl = free_action.lower()
    for va in admissible:
        if va.lower() == fl:
            return va
    for va in admissible:
        if fl in va.lower() or va.lower() in fl:
            return va
    return None


def parse_action_constrained(text: str, admissible: List[str]) -> Optional[str]:
    """Parse action from LLM output, matching against admissible actions."""
    m = re.search(r"Action:\s*(.+?)(?:\n|$)", text, re.IGNORECASE)
    candidate = m.group(1).strip().strip('"').strip("'") if m else text.strip()

    matched = match_to_admissible(candidate, admissible)
    if matched:
        return matched

    for va in admissible:
        if va in text:
            return va
    return None


# ---------------------------------------------------------------------------
# LLM wrapper
# ---------------------------------------------------------------------------

class ALFWorldLLM:
    def __init__(self, model_path: str, use_vllm: bool = True, gpu_id: int = 0):
        self.model_path = model_path
        self.use_vllm = use_vllm
        self.gpu_id = gpu_id
        self._llm = None
        self._tokenizer = None
        self.max_new_tokens = 256

    def _load(self):
        if self._llm is not None:
            return
        if self.use_vllm:
            os.environ["CUDA_VISIBLE_DEVICES"] = str(self.gpu_id)
            from vllm import LLM
            self._llm = LLM(
                model=self.model_path,
                trust_remote_code=True,
                gpu_memory_utilization=0.85,
                max_model_len=4096,
            )
            from transformers import AutoTokenizer
            self._tokenizer = AutoTokenizer.from_pretrained(
                self.model_path, trust_remote_code=True
            )
        else:
            import torch
            from transformers import AutoModelForCausalLM, AutoTokenizer
            self._tokenizer = AutoTokenizer.from_pretrained(
                self.model_path, trust_remote_code=True
            )
            self._llm = AutoModelForCausalLM.from_pretrained(
                self.model_path,
                torch_dtype=torch.float16,
                device_map=f"cuda:{self.gpu_id}",
                trust_remote_code=True,
            )

    def generate(self, messages: List[dict], temperature: float = 0.3) -> str:
        self._load()
        if self.use_vllm:
            return self._generate_vllm(messages, temperature)
        else:
            return self._generate_hf(messages, temperature)

    def _generate_vllm(self, messages: List[dict], temperature: float) -> str:
        from vllm import SamplingParams
        messages = sanitize_messages_for_template(messages, self._tokenizer)
        prompt = self._tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        params = SamplingParams(
            temperature=max(temperature, 0.01),
            max_tokens=self.max_new_tokens,
            stop=["Observation:", "\nObservation"],
        )
        outputs = self._llm.generate([prompt], params)
        return outputs[0].outputs[0].text.strip()

    def _generate_hf(self, messages: List[dict], temperature: float) -> str:
        import torch
        messages = sanitize_messages_for_template(messages, self._tokenizer)
        text = self._tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )
        inputs = self._tokenizer(text, return_tensors="pt").to(self._llm.device)
        with torch.no_grad():
            outputs = self._llm.generate(
                **inputs,
                max_new_tokens=self.max_new_tokens,
                temperature=max(temperature, 0.01),
                do_sample=temperature > 0,
                top_p=0.9,
            )
        new_tokens = outputs[0][inputs["input_ids"].shape[1]:]
        return self._tokenizer.decode(new_tokens, skip_special_tokens=True).strip()


# ---------------------------------------------------------------------------
# Environment helpers
# ---------------------------------------------------------------------------

def collect_game_files(data_root: str, split: str = "valid_seen",
                       task_types: Optional[List[str]] = None,
                       max_per_type: int = 0) -> List[Dict[str, str]]:
    """Collect game files from ALFWorld data directory."""
    split_path = os.path.join(data_root, "json_2.1.1", split)
    if not os.path.exists(split_path):
        raise FileNotFoundError(f"Split path not found: {split_path}")

    games = []
    type_counts = Counter()

    for task_dir in sorted(os.listdir(split_path)):
        task_type = None
        for tt in TASK_TYPES:
            if task_dir.startswith(tt):
                task_type = tt
                break
        if task_type is None:
            continue
        if task_types and task_type not in task_types:
            continue
        if max_per_type > 0 and type_counts[task_type] >= max_per_type:
            continue

        full_dir = os.path.join(split_path, task_dir)
        trials = sorted([d for d in os.listdir(full_dir) if d.startswith("trial_")])
        if not trials:
            continue

        trial_dir = os.path.join(full_dir, trials[0])
        game_path = os.path.join(trial_dir, "game.tw-pddl")
        if not os.path.exists(game_path):
            continue

        traj_path = os.path.join(trial_dir, "traj_data.json")
        task_desc = ""
        if os.path.exists(traj_path):
            with open(traj_path) as f:
                traj = json.load(f)
            anns = traj.get("turk_annotations", {}).get("anns", [{}])
            task_desc = anns[0].get("task_desc", "") if anns else ""

        games.append({
            "game_path": game_path,
            "task_type": task_type,
            "task_id": f"{task_dir}/{trials[0]}",
            "task_desc": task_desc,
        })
        type_counts[task_type] += 1

    return games


def make_env(game_path: str, max_steps: int = 50):
    """Create a TextWorld gym env for a single ALFWorld game with demangler."""
    request_infos = textworld.EnvInfos(
        won=True, admissible_commands=True, extras=["gamefile"]
    )
    env_id = textworld.gym.register_game(
        game_path, request_infos,
        max_episode_steps=max_steps,
        wrappers=[AlfredDemangler(shuffle=False), AlfredInfos],
    )
    return textworld.gym.make(env_id)


def extract_task_desc_from_obs(obs: str) -> str:
    """Extract task description from initial observation."""
    if "Your task is to:" in obs:
        return obs.split("Your task is to:")[-1].strip().rstrip(".")
    return ""


def format_history(actions: List[str], last_k: int = 10) -> str:
    if not actions:
        return "(none)"
    return " → ".join(actions[-last_k:])


# ---------------------------------------------------------------------------
# Episode runners
# ---------------------------------------------------------------------------

def run_internal_episode(
    llm: ALFWorldLLM, game_info: dict, max_steps: int = 50,
) -> Dict[str, Any]:
    """Internal mode: LLM sees observation only, no admissible actions list."""
    env = make_env(game_info["game_path"], max_steps)
    trajectory = []
    actions_taken = []
    won = False

    try:
        obs, infos = env.reset()
        task_desc = game_info.get("task_desc") or extract_task_desc_from_obs(obs)

        for step in range(max_steps):
            admissible = infos["admissible_commands"]

            messages = [
                {"role": "system", "content": INTERNAL_SYSTEM},
                {"role": "user", "content": USER_TEMPLATE_INTERNAL.format(
                    task_desc=task_desc,
                    observation=obs,
                    history=format_history(actions_taken),
                )},
            ]
            raw = llm.generate(messages, temperature=0.3)
            free_action = parse_action_free(raw)

            action = None
            if free_action:
                action = match_to_admissible(free_action, admissible)
            if not action:
                action = admissible[0] if admissible else "look"

            trajectory.append({
                "step": step,
                "observation": obs[:500],
                "thought": raw[:300],
                "action": action,
                "action_raw": free_action,
                "action_matched": action != free_action if free_action else True,
                "admissible_count": len(admissible),
            })

            obs, score, done, infos = env.step(action)
            actions_taken.append(action)
            won = infos.get("won", False)

            if done or won:
                break

        return {
            "trajectory": trajectory,
            "success": bool(won),
            "n_steps": len(trajectory),
            "score": 1.0 if won else 0.0,
        }
    finally:
        env.close()


def run_deterministic_episode(
    llm: ALFWorldLLM, game_info: dict, max_steps: int = 50,
) -> Dict[str, Any]:
    """Deterministic mode: LLM sees observation + admissible actions list."""
    env = make_env(game_info["game_path"], max_steps)
    trajectory = []
    actions_taken = []
    won = False

    try:
        obs, infos = env.reset()
        task_desc = game_info.get("task_desc") or extract_task_desc_from_obs(obs)

        for step in range(max_steps):
            admissible = infos["admissible_commands"]
            admissible_str = "\n".join(
                f"  [{i}] {a}" for i, a in enumerate(admissible)
            )

            messages = [
                {"role": "system", "content": DETERMINISTIC_SYSTEM},
                {"role": "user", "content": USER_TEMPLATE_DETERMINISTIC.format(
                    task_desc=task_desc,
                    observation=obs,
                    admissible_str=admissible_str,
                    history=format_history(actions_taken),
                )},
            ]
            raw = llm.generate(messages, temperature=0.3)
            action = parse_action_constrained(raw, admissible)
            if not action:
                action = admissible[0] if admissible else "look"

            trajectory.append({
                "step": step,
                "observation": obs[:500],
                "thought": raw[:300],
                "action": action,
                "admissible_count": len(admissible),
            })

            obs, score, done, infos = env.step(action)
            actions_taken.append(action)
            won = infos.get("won", False)

            if done or won:
                break

        return {
            "trajectory": trajectory,
            "success": bool(won),
            "n_steps": len(trajectory),
            "score": 1.0 if won else 0.0,
        }
    finally:
        env.close()


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def run_pipeline(args):
    games = collect_game_files(
        args.data_dir,
        split=args.split,
        task_types=args.task_types.split(",") if args.task_types else None,
        max_per_type=args.max_per_type,
    )
    if args.n_tasks > 0:
        games = games[:args.n_tasks]

    print(f"=== ALFWorld Counterfactual Labeling ===")
    print(f"Split: {args.split} | Games: {len(games)} | Max steps: {args.max_steps}")
    print(f"Model: {args.model_path} | GPU: {args.gpu_id} | vLLM: {not args.no_vllm}")

    llm = ALFWorldLLM(
        model_path=args.model_path,
        use_vllm=not args.no_vllm,
        gpu_id=args.gpu_id,
    )

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    if os.path.exists(args.output):
        os.remove(args.output)

    label_counts = Counter()
    results = []

    for i, game in enumerate(games):
        t0 = time.time()
        print(f"\n[{i+1}/{len(games)}] {game['task_type']}: {game['task_id'][:60]}")
        print(f"  Task: {game['task_desc']}")

        try:
            internal = run_internal_episode(llm, game, args.max_steps)
            print(f"  Internal: {'OK' if internal['success'] else 'FAIL'} "
                  f"({internal['n_steps']} steps)")

            det = run_deterministic_episode(llm, game, args.max_steps)
            print(f"  Deterministic: {'OK' if det['success'] else 'FAIL'} "
                  f"({det['n_steps']} steps)")
        except Exception as e:
            print(f"  ERROR: {e}")
            continue

        if det["success"] and not internal["success"]:
            label = "det-preferred"
        elif internal["success"] and not det["success"]:
            label = "internal-preferred"
        else:
            label = "no-preference"

        label_counts[label] += 1
        elapsed = round(time.time() - t0, 1)

        record = {
            "env": "alfworld",
            "task_id": game["task_id"],
            "task_type": game["task_type"],
            "task_desc": game["task_desc"],
            "internal_success": internal["success"],
            "deterministic_success": det["success"],
            "internal_steps": internal["n_steps"],
            "deterministic_steps": det["n_steps"],
            "label": label,
            "internal": internal,
            "deterministic": det,
            "metadata": {
                "split": args.split,
                "time_s": elapsed,
            },
        }
        results.append(record)

        with open(args.output, "a") as f:
            f.write(json.dumps(record, default=str) + "\n")

        print(f"  Label: {label} ({elapsed}s)")

    # Summary
    n = len(results)
    print(f"\n{'='*50}")
    print(f"Total: {n} games")
    if n > 0:
        for lb in ["det-preferred", "internal-preferred", "no-preference"]:
            c = label_counts.get(lb, 0)
            print(f"  {lb}: {c} ({c/n*100:.1f}%)")
        iw = sum(1 for r in results if r["internal_success"])
        dw = sum(1 for r in results if r["deterministic_success"])
        print(f"  Internal success: {iw}/{n} ({iw/n*100:.1f}%)")
        print(f"  Deterministic success: {dw}/{n} ({dw/n*100:.1f}%)")
    print(f"Output: {args.output}")

    return results


def main():
    parser = argparse.ArgumentParser(description="ALFWorld counterfactual labeling")
    parser.add_argument("--data_dir", type=str,
                        default="/root/autodl-tmp/alfworld_data")
    parser.add_argument("--split", type=str, default="valid_seen")
    parser.add_argument("--task_types", type=str, default=None,
                        help="Comma-separated task types")
    parser.add_argument("--max_per_type", type=int, default=0)
    parser.add_argument("--n_tasks", type=int, default=10)
    parser.add_argument("--max_steps", type=int, default=50)
    parser.add_argument("--output", type=str,
                        default="data/alfworld-counterfactual/episodes.jsonl")
    parser.add_argument("--model_path", type=str, default=None)
    parser.add_argument("--no_vllm", action="store_true")
    parser.add_argument("--gpu_id", type=int, default=0)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    if args.model_path is None:
        args.model_path = find_model_path()
    print(f"Model: {args.model_path}")

    random.seed(args.seed)
    run_pipeline(args)


if __name__ == "__main__":
    main()
