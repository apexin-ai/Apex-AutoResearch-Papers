#!/usr/bin/env python3
"""TaxEI Recovery Evaluation — evaluate injection recovery and baseline success."""
from __future__ import annotations

import argparse
import copy
import json
import os
import random
import re
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import torch
from scipy.stats import chi2
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

import textworld
import textworld.gym
from alfworld.agents.environment.alfred_tw_env import AlfredDemangler, AlfredInfos

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from injection import (
    P1_StepOrderSwap,
    P2_SubGoalDeletion,
    C1_ContextTruncation,
    C4_ObservationMasking,
)

MAX_STEPS = 50
HISTORY_WINDOW = 10

OPERATORS = [
    P1_StepOrderSwap(),
    P2_SubGoalDeletion(),
    C1_ContextTruncation(),
    C4_ObservationMasking(),
]

OPERATOR_CONFIGS = {
    "P1_step_order_swap": {"swap_range": 5},
    "P2_sub_goal_deletion": {"deletion_strategy": "critical"},
    "C1_context_truncation": {"truncation_ratio": 0.5},
    "C4_observation_masking": {"mask_type": "generic", "max_masks": 2},
}


# ---------------------------------------------------------------------------
# Prompt (identical to collect_trajectories.py)
# ---------------------------------------------------------------------------

def build_prompt(
    task_desc: str,
    step_count: int,
    history: List[Dict[str, str]],
    current_obs: str,
    admissible_commands: List[str],
) -> str:
    history_str = ""
    for h in history[-HISTORY_WINDOW:]:
        history_str += f"Observation: {h['observation']}\nAction: {h['action']}\n"
    actions_str = ", ".join(admissible_commands)
    return (
        f"You are an expert agent operating in the ALFRED Embodied Environment.\n"
        f"Your task is to: {task_desc}\n"
        f"Prior to this step, you have already taken {step_count} step(s).\n"
        f"Below are the most recent observations and actions:\n"
        f"{history_str}\n"
        f"Your current observation is: {current_obs}\n"
        f"Your admissible actions are: [{actions_str}]\n\n"
        f"Think step by step in <think></think> tags, then choose an action "
        f"in <action></action> tags.\n"
        f"The action MUST be one of the admissible actions listed above."
    )


def parse_response(text: str) -> Tuple[str, str]:
    think_m = re.search(r"<think>(.*?)</think>", text, re.DOTALL)
    action_m = re.search(r"<action>(.*?)</action>", text, re.DOTALL)
    think = think_m.group(1).strip() if think_m else ""
    action = action_m.group(1).strip() if action_m else ""
    return think, action


def fuzzy_match_action(action: str, admissible: List[str]) -> str:
    if action in admissible:
        return action
    best, best_score = admissible[0], 0.0
    for a in admissible:
        score = SequenceMatcher(None, action.lower(), a.lower()).ratio()
        if score > best_score:
            best, best_score = a, score
    return best


# ---------------------------------------------------------------------------
# Action injection helpers
# ---------------------------------------------------------------------------

def select_wrong_action(
    intended_action: str,
    admissible: List[str],
    rng: random.Random,
) -> Optional[str]:
    """Pick a wrong-but-valid action from admissible commands.

    Strategy: prefer same-verb-different-target, fallback to any non-passive action.
    """
    if len(admissible) < 2:
        return None

    parts = intended_action.split()
    verb = parts[0] if parts else ""

    same_verb = [a for a in admissible
                 if a != intended_action and a.split()[0] == verb]
    if same_verb:
        return rng.choice(same_verb)

    passive = {"look", "inventory", "examine"}
    candidates = [a for a in admissible
                  if a != intended_action and a.split()[0] not in passive]
    if candidates:
        return rng.choice(candidates)

    others = [a for a in admissible if a != intended_action]
    if others:
        return rng.choice(others)
    return None


RECOVERY_KEYWORDS = re.compile(
    r"wrong|mistake|error|incorrect|back|return|undo|retry|instead|"
    r"should have|need to go back|not what|oops|fix|correct",
    re.IGNORECASE,
)


def detect_recovery_signal(think_texts: List[str]) -> bool:
    return any(RECOVERY_KEYWORDS.search(t) for t in think_texts if t)


# ---------------------------------------------------------------------------
# Game file collection (valid_unseen, one trial per task)
# ---------------------------------------------------------------------------

def collect_game_files(data_path: str) -> List[Dict[str, Any]]:
    games: List[Dict[str, Any]] = []
    task_dir = Path(data_path)
    if not task_dir.exists():
        raise FileNotFoundError(f"Data path not found: {data_path}")

    for task_folder in sorted(task_dir.iterdir()):
        if not task_folder.is_dir():
            continue
        for trial_folder in sorted(task_folder.iterdir()):
            if not trial_folder.is_dir():
                continue
            game_file = trial_folder / "game.tw-pddl"
            traj_file = trial_folder / "traj_data.json"
            if not (game_file.exists() and traj_file.exists()):
                continue
            with open(game_file) as f:
                gamedata = json.load(f)
            if not gamedata.get("solvable", False):
                continue
            with open(traj_file) as f:
                traj_data = json.load(f)
            task_type = traj_data.get("task_type", "")
            anns = traj_data.get("turk_annotations", {}).get("anns", [])
            task_desc = anns[0]["task_desc"] if anns else task_type.replace("_", " ")
            games.append({
                "game_file": str(game_file),
                "task_type": task_type,
                "task_desc": task_desc,
                "gamefile_dir": str(trial_folder),
                "task_name": task_folder.name,
            })
            break  # one trial per task
    return games


# ---------------------------------------------------------------------------
# Model inference (transformers + optional LoRA / PEFT)
# ---------------------------------------------------------------------------

class ModelInference:
    def __init__(self, base_model: str, adapter_path: Optional[str] = None,
                 device: str = "cuda:0"):
        print(f"Loading base model: {base_model}", flush=True)
        self.tokenizer = AutoTokenizer.from_pretrained(
            base_model, trust_remote_code=True, padding_side="left",
        )
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token

        self.model = AutoModelForCausalLM.from_pretrained(
            base_model,
            torch_dtype=torch.bfloat16,
            device_map=device,
            trust_remote_code=True,
        )

        if adapter_path:
            print(f"Loading LoRA adapter: {adapter_path}", flush=True)
            self.model = PeftModel.from_pretrained(self.model, adapter_path)
            self.model = self.model.merge_and_unload()

        self.model.eval()
        self.device = device

    @torch.inference_mode()
    def generate(self, prompt: str, max_new_tokens: int = 512,
                 temperature: float = 0.0) -> str:
        messages = [{"role": "user", "content": prompt}]
        text = self.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True,
            enable_thinking=False,
        )
        inputs = self.tokenizer(text, return_tensors="pt").to(self.device)

        gen_kwargs: Dict[str, Any] = {
            "max_new_tokens": max_new_tokens,
            "do_sample": temperature > 0,
            "pad_token_id": self.tokenizer.pad_token_id,
        }
        if temperature > 0:
            gen_kwargs["temperature"] = temperature

        outputs = self.model.generate(**inputs, **gen_kwargs)
        new_tokens = outputs[0][inputs["input_ids"].shape[1]:]
        return self.tokenizer.decode(new_tokens, skip_special_tokens=True)


# ---------------------------------------------------------------------------
# Context injection helpers (legacy --inject_mode context)
# ---------------------------------------------------------------------------

def apply_injection(
    history: List[Dict[str, str]],
    operator,
    config: Dict[str, Any],
) -> List[Dict[str, str]]:
    steps = copy.deepcopy(history)
    for s in steps:
        if "observation" in s and "text_obs" not in s:
            s["text_obs"] = s["observation"]

    modified = operator.inject(steps, env_idx=0, step_idx=len(steps) - 1, config=config)

    for s in modified:
        if "text_obs" in s:
            s["observation"] = s["text_obs"]

    return modified


# ---------------------------------------------------------------------------
# Episode runner
# ---------------------------------------------------------------------------

def run_episode(
    model: ModelInference,
    game_info: Dict[str, Any],
    inject: bool = False,
    inject_mode: str = "action",
    operator=None,
    op_config: Optional[Dict[str, Any]] = None,
    injection_step: int = 3,
    rng: Optional[random.Random] = None,
) -> Dict[str, Any]:
    request_infos = textworld.EnvInfos(
        won=True, admissible_commands=True, extras=["gamefile"],
    )
    alfred_demangler = AlfredDemangler(shuffle=False)
    env_id = textworld.gym.register_games(
        [game_info["game_file"]],
        request_infos,
        batch_size=1,
        max_episode_steps=MAX_STEPS,
        wrappers=[alfred_demangler, AlfredInfos],
    )
    env = textworld.gym.make(env_id)

    if rng is None:
        rng = random.Random(42)

    try:
        obs, infos = env.reset()
        obs_text = obs[0] if isinstance(obs, (list, tuple)) else obs

        history: List[Dict[str, str]] = []
        done = False
        won = False
        step_count = 0
        injected = False
        injection_applied_at = -1
        injected_action = None
        intended_action_at_inject = None
        post_inject_thinks: List[str] = []

        while not done and step_count < MAX_STEPS:
            admissible = infos.get("admissible_commands", [[]])[0]
            if not admissible:
                break

            # Context injection: corrupt history display (legacy mode)
            display_history = history
            if (inject and inject_mode == "context" and not injected
                    and operator is not None
                    and step_count >= injection_step and len(history) >= 2):
                display_history = apply_injection(
                    history, operator, op_config or {},
                )
                injected = True
                injection_applied_at = step_count

            prompt = build_prompt(
                game_info["task_desc"], step_count, display_history,
                obs_text, admissible,
            )

            response_text = model.generate(prompt)
            think, action = parse_response(response_text)

            if not action:
                action = admissible[0] if admissible else "look"
            else:
                action = fuzzy_match_action(action, admissible)

            # Action injection: replace agent's action with a wrong one
            if (inject and inject_mode == "action" and not injected
                    and step_count >= injection_step and len(admissible) >= 2):
                wrong = select_wrong_action(action, admissible, rng)
                if wrong is not None:
                    intended_action_at_inject = action
                    action = wrong
                    injected_action = wrong
                    injected = True
                    injection_applied_at = step_count

            if injected and step_count > injection_applied_at:
                post_inject_thinks.append(think)

            history.append({"observation": obs_text, "action": action})

            obs, _rewards, dones, infos = env.step([action])
            obs_text = obs[0] if isinstance(obs, (list, tuple)) else obs
            done = dones[0] if isinstance(dones, (list, tuple)) else dones
            won = infos.get("won", [False])[0]
            step_count += 1
    finally:
        env.close()

    result: Dict[str, Any] = {
        "task_name": game_info.get("task_name", ""),
        "task_type": game_info["task_type"],
        "task_desc": game_info["task_desc"],
        "success": bool(won),
        "steps": step_count,
        "injected": injected if inject else False,
        "operator": operator.name if (operator and inject_mode == "context") else "none",
        "inject_mode": inject_mode if inject else "none",
    }

    if inject and inject_mode == "action":
        result["injection_step"] = injection_applied_at if injected else -1
        result["injected_action"] = injected_action or ""
        result["intended_action"] = intended_action_at_inject or ""
        result["recovery_detected"] = (
            detect_recovery_signal(post_inject_thinks) if injected else False
        )
        result["recovery_steps"] = (
            (step_count - injection_applied_at) if injected else 0
        )
        result["final_success"] = bool(won)

    return result


# ---------------------------------------------------------------------------
# Statistical tests
# ---------------------------------------------------------------------------

def mcnemar_test(successes_a: List[bool], successes_b: List[bool]) -> float:
    n01 = sum(1 for a, b in zip(successes_a, successes_b) if not a and b)
    n10 = sum(1 for a, b in zip(successes_a, successes_b) if a and not b)
    if n01 + n10 == 0:
        return 1.0
    stat = (abs(n01 - n10) - 1) ** 2 / (n01 + n10)
    return float(1 - chi2.cdf(stat, df=1))


def bootstrap_ci(
    values_a: List[int],
    values_b: List[int],
    n_bootstrap: int = 10000,
    ci: float = 0.95,
    seed: int = 42,
) -> Tuple[float, float]:
    rng = np.random.RandomState(seed)
    n = len(values_a)
    arr_a = np.array(values_a, dtype=np.float64)
    arr_b = np.array(values_b, dtype=np.float64)
    diffs = np.empty(n_bootstrap)
    for i in range(n_bootstrap):
        idx = rng.randint(0, n, size=n)
        diffs[i] = arr_a[idx].mean() - arr_b[idx].mean()
    alpha = (1 - ci) / 2
    return float(np.percentile(diffs, alpha * 100)), float(
        np.percentile(diffs, (1 - alpha) * 100)
    )


# ---------------------------------------------------------------------------
# Report builder
# ---------------------------------------------------------------------------

def build_report(results: List[Dict[str, Any]], args) -> Dict[str, Any]:
    total = len(results)
    successes = sum(1 for r in results if r["success"])

    report: Dict[str, Any] = {
        "model": args.model_path or args.base_model,
        "eval_split": args.eval_split,
        "inject": args.inject,
        "inject_mode": args.inject_mode if args.inject else "none",
        "total_episodes": total,
        "success_rate": round(successes / total, 3) if total else 0,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    if args.inject and args.inject_mode == "context":
        op_results: Dict[str, Dict[str, int]] = defaultdict(
            lambda: {"total": 0, "recovered": 0}
        )
        for r in results:
            op = r["operator"]
            op_results[op]["total"] += 1
            if r["success"]:
                op_results[op]["recovered"] += 1

        injection_recovery_rates = {}
        for op_name, counts in sorted(op_results.items()):
            rate = counts["recovered"] / counts["total"] if counts["total"] else 0
            injection_recovery_rates[op_name] = {
                "total": counts["total"],
                "recovered": counts["recovered"],
                "rate": round(rate, 3),
            }
        report["injection_recovery_rates"] = injection_recovery_rates
        report["overall_recovery_rate"] = round(successes / total, 3) if total else 0

    if args.inject and args.inject_mode == "action":
        injected_eps = [r for r in results if r.get("injected")]
        n_injected = len(injected_eps)
        n_recovered = sum(1 for r in injected_eps if r["final_success"])
        n_detected = sum(1 for r in injected_eps if r.get("recovery_detected"))
        avg_recovery_steps = (
            round(float(np.mean([r["recovery_steps"] for r in injected_eps])), 1)
            if injected_eps else 0
        )
        report["action_injection"] = {
            "total_injected": n_injected,
            "recovered": n_recovered,
            "recovery_rate": round(n_recovered / n_injected, 3) if n_injected else 0,
            "detected": n_detected,
            "detection_rate": round(n_detected / n_injected, 3) if n_injected else 0,
            "avg_recovery_steps": avg_recovery_steps,
        }
        report["overall_recovery_rate"] = (
            round(n_recovered / n_injected, 3) if n_injected else 0
        )

    type_results: Dict[str, Dict[str, int]] = defaultdict(
        lambda: {"total": 0, "success": 0}
    )
    for r in results:
        tt = r["task_type"]
        type_results[tt]["total"] += 1
        if r["success"]:
            type_results[tt]["success"] += 1

    report["by_task_type"] = {
        tt: {
            "total": c["total"],
            "success": c["success"],
            "rate": round(c["success"] / c["total"], 3) if c["total"] else 0,
        }
        for tt, c in sorted(type_results.items())
    }
    report["episodes"] = results
    return report


# ---------------------------------------------------------------------------
# Compare two result files
# ---------------------------------------------------------------------------

def compare_results(
    taxei_path: str, vanilla_path: str, output_path: Optional[str] = None
) -> Dict[str, Any]:
    with open(taxei_path) as f:
        taxei = json.load(f)
    with open(vanilla_path) as f:
        vanilla = json.load(f)

    taxei_by_task = {e["task_name"]: e["success"] for e in taxei["episodes"]}
    vanilla_by_task = {e["task_name"]: e["success"] for e in vanilla["episodes"]}

    common = sorted(set(taxei_by_task) & set(vanilla_by_task))
    t_succ = [taxei_by_task[t] for t in common]
    v_succ = [vanilla_by_task[t] for t in common]

    t_rate = float(np.mean(t_succ))
    v_rate = float(np.mean(v_succ))

    p = mcnemar_test(t_succ, v_succ)
    ci_lo, ci_hi = bootstrap_ci(
        [int(s) for s in t_succ], [int(s) for s in v_succ],
    )

    comparison = {
        "taxei_model": taxei["model"],
        "vanilla_model": vanilla["model"],
        "num_common_tasks": len(common),
        "taxei_recovery_rate": round(t_rate, 3),
        "vanilla_recovery_rate": round(v_rate, 3),
        "recovery_rate_diff": round(t_rate - v_rate, 3),
        "mcnemar_p_value": round(p, 4),
        "bootstrap_ci_95": [round(ci_lo, 3), round(ci_hi, 3)],
        "significant_at_005": p < 0.05,
        "ci_excludes_zero": ci_lo > 0 or ci_hi < 0,
    }

    print(json.dumps(comparison, indent=2), flush=True)

    if output_path:
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        with open(output_path, "w") as f:
            json.dump(comparison, f, indent=2)
        print(f"Comparison saved to {output_path}", flush=True)

    return comparison


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def load_task_list(path: str) -> List[Dict[str, Any]]:
    with open(path) as f:
        data = json.load(f)
    games = []
    for t in data["tasks"]:
        games.append({
            "game_file": t["gamefile"],
            "task_type": t["task_type"],
            "task_desc": t.get("task_desc", ""),
            "gamefile_dir": str(Path(t["gamefile"]).parent),
            "task_name": t["task_id"],
        })
    return games


def main():
    parser = argparse.ArgumentParser(description="TaxEI Recovery Evaluation")
    parser.add_argument("--model_path", type=str, default=None,
                       help="LoRA adapter checkpoint path (omit for zero-shot)")
    parser.add_argument("--base_model", type=str,
                        default="/root/autodl-tmp/models/Qwen/Qwen3-8B")
    parser.add_argument("--alfworld_data", type=str,
                        default="/root/autodl-tmp/alfworld_data")
    parser.add_argument("--eval_split", type=str, default="valid_unseen")
    parser.add_argument("--num_episodes", type=int, default=134)
    parser.add_argument("--output", type=str, default="eval_results/results.json")
    parser.add_argument("--inject", action="store_true", default=False)
    parser.add_argument("--no_inject", dest="inject", action="store_false")
    parser.add_argument("--inject_mode", type=str, default="action",
                        choices=["action", "context"],
                        help="'action': replace agent action with wrong one; "
                             "'context': corrupt history display (legacy)")
    parser.add_argument("--inject_step", type=str, default="auto",
                        help="Step to inject at (integer or 'auto' for random 2-6)")
    parser.add_argument("--device", type=str, default="cuda:0")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--task_list", type=str, default=None,
                        help="Path to JSON file with fixed task list for reproducible evaluation")

    parser.add_argument("--compare_with", type=str, default=None,
                        help="Path to vanilla SFT results JSON for comparison")
    parser.add_argument("--compare_output", type=str, default=None,
                        help="Path to save comparison JSON")

    args = parser.parse_args()

    if args.compare_with:
        if not os.path.exists(args.output):
            print(f"Error: --output {args.output} does not exist for comparison.",
                  file=sys.stderr)
            sys.exit(1)
        compare_results(args.output, args.compare_with, args.compare_output)
        return

    # --- Run evaluation ---
    if args.task_list:
        games = load_task_list(args.task_list)
        print(f"Loaded {len(games)} tasks from {args.task_list}", flush=True)
    else:
        data_path = os.path.join(args.alfworld_data, "json_2.1.1", args.eval_split)
        games = collect_game_files(data_path)
        print(f"Found {len(games)} tasks in {args.eval_split}", flush=True)

    if 0 < args.num_episodes < len(games):
        games = games[: args.num_episodes]

    model = ModelInference(
        base_model=args.base_model,
        adapter_path=args.model_path,
        device=args.device,
    )

    results: List[Dict[str, Any]] = []
    rng = random.Random(args.seed)

    for i, game_info in enumerate(games):
        if args.inject:
            if args.inject_step == "auto":
                inj_step = rng.randint(2, 6)
            else:
                inj_step = int(args.inject_step)

            if args.inject_mode == "context":
                op = OPERATORS[i % len(OPERATORS)]
                op_config = OPERATOR_CONFIGS[op.name]
            else:
                op = None
                op_config = None
        else:
            op = None
            op_config = None
            inj_step = 0

        result = run_episode(
            model, game_info,
            inject=args.inject,
            inject_mode=args.inject_mode,
            operator=op,
            op_config=op_config,
            injection_step=inj_step,
            rng=rng,
        )
        results.append(result)

        status = "OK" if result["success"] else "FAIL"
        if args.inject and args.inject_mode == "action":
            inj_info = f" [action@step{result.get('injection_step', '?')}]"
        elif args.inject and args.inject_mode == "context":
            inj_info = f" [{result['operator']}@step{inj_step}]"
        else:
            inj_info = ""
        print(
            f"  [{i + 1}/{len(games)}] {game_info['task_name']}: {status} "
            f"({result['steps']} steps){inj_info}",
            flush=True,
        )

    report = build_report(results, args)

    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\nReport saved to {args.output}", flush=True)

    print(f"\n=== Summary ===", flush=True)
    print(f"Total: {report['total_episodes']}", flush=True)
    print(f"Success rate: {report['success_rate']}", flush=True)
    if args.inject and args.inject_mode == "context" and "injection_recovery_rates" in report:
        print(f"Overall recovery rate: {report['overall_recovery_rate']}", flush=True)
        for op_name, stats in report["injection_recovery_rates"].items():
            print(
                f"  {op_name}: {stats['recovered']}/{stats['total']} "
                f"({stats['rate']})",
                flush=True,
            )
    if args.inject and args.inject_mode == "action" and "action_injection" in report:
        ai = report["action_injection"]
        print(f"Inject mode: action", flush=True)
        print(
            f"Recovery rate: {ai['recovered']}/{ai['total_injected']} "
            f"({ai['recovery_rate']})",
            flush=True,
        )
        print(
            f"Detection rate: {ai['detected']}/{ai['total_injected']} "
            f"({ai['detection_rate']})",
            flush=True,
        )
        print(f"Avg recovery steps: {ai['avg_recovery_steps']}", flush=True)


if __name__ == "__main__":
    main()
