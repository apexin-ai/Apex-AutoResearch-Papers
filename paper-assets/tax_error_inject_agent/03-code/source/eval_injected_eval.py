#!/usr/bin/env python3
"""
TaxEI Injected Evaluation — measure error recovery under mid-episode injection.

Runs ALFWorld episodes, injecting an error at a specified step using taxonomy
operators (P1_step_order_swap, P2_sub_goal_deletion, C1_context_truncation,
C4_observation_masking). After injection, tracks:
  - Detection: did the model's <think> output acknowledge the anomaly?
  - Recovery: did the model take corrective/re-grounding actions?
  - Success: did the task succeed despite the injection?

Usage:
  # Full run (47 tasks on cuda:3)
  CUDA_VISIBLE_DEVICES=3 python eval/injected_eval.py \\
      --model_path <checkpoint> --model_variant taxei \\
      --num_episodes 47 --output eval_results/injected_taxei.json

  # Dry-run (3 tasks)
  CUDA_VISIBLE_DEVICES=3 python eval/injected_eval.py \\
      --model_path <checkpoint> --model_variant taxei \\
      --num_episodes 3 --output eval_results/dryrun_recovery.json

  # Compare two result files
  python eval/injected_eval.py \\
      --output eval_results/injected_taxei.json \\
      --compare_with eval_results/injected_vanilla.json \\
      --compare_output eval_results/compare_taxei_vs_vanilla_injected.json

Args:
  --model_path      LoRA adapter checkpoint (omit for base model zero-shot)
  --base_model      Base model path (default: Qwen3-8B)
  --model_variant   Label: taxei / random / vanilla
  --inject_step     Fixed injection step, -1 = random in [2,6] (default: -1)
  --num_episodes    Number of episodes (default: 47)
  --seed            Random seed (default: 42)
  --device          Torch device (default: cuda:0, use with CUDA_VISIBLE_DEVICES)

Output JSON:
  {
    "model", "model_variant", "inject": true,
    "total_episodes", "success_rate", "recovery_rate", "detection_rate",
    "by_operator": {
      "P1_step_order_swap": { "total", "recovered", "detected", ... }, ...
    },
    "by_task_type": { ... },
    "episodes": [ per-episode detail with step-by-step trajectory ]
  }
"""
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
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import torch

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
sys.path.insert(0, str(PROJECT_ROOT / "eval"))

from recovery import (
    ModelInference,
    collect_game_files,
    load_task_list,
    build_prompt,
    parse_response,
    fuzzy_match_action,
    apply_injection,
    OPERATORS,
    OPERATOR_CONFIGS,
    MAX_STEPS,
    HISTORY_WINDOW,
    mcnemar_test,
    bootstrap_ci,
)

import textworld
import textworld.gym
from alfworld.agents.environment.alfred_tw_env import AlfredDemangler, AlfredInfos


# ---------------------------------------------------------------------------
# Error detection heuristics — applied to <think> output post-injection
# ---------------------------------------------------------------------------

DETECTION_PATTERNS = [
    r"\b(?:wrong|error|mistake|incorrect|unexpected)\b",
    r"\b(?:strange|odd|confused|confusing|inconsistent)\b",
    r"\b(?:doesn'?t\s+match|doesn'?t\s+make\s+sense|not\s+right)\b",
    r"\b(?:something\s+(?:is\s+)?(?:off|wrong)|went\s+wrong)\b",
    r"\b(?:missing|lost|truncated|disappeared)\b",
    r"\b(?:should\s+have|need\s+to\s+redo|go\s+back|try\s+again)\b",
    r"\b(?:problem|issue|anomal)",
    r"\b(?:wait|hmm)\b.*\b(?:but|however|actually)\b",
]

RECOVERY_ACTION_PREFIXES = ["look", "examine", "inventory"]


def detect_error_in_think(think_text: str) -> bool:
    """Check if <think> output shows awareness of injected error."""
    if not think_text:
        return False
    text_lower = think_text.lower()
    for pattern in DETECTION_PATTERNS:
        if re.search(pattern, text_lower):
            return True
    return False


def is_recovery_action(action: str) -> bool:
    """Check if an action is a re-grounding/recovery attempt."""
    action_lower = action.lower().strip()
    return any(action_lower.startswith(p) for p in RECOVERY_ACTION_PREFIXES)


# ---------------------------------------------------------------------------
# Enhanced episode runner with per-step tracking
# ---------------------------------------------------------------------------

def run_injected_episode(
    model: ModelInference,
    game_info: Dict[str, Any],
    operator,
    op_config: Dict[str, Any],
    injection_step: int,
) -> Dict[str, Any]:
    """Run one episode with injection, recording per-step behavior."""
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

    trajectory: List[Dict[str, Any]] = []
    detection_step: Optional[int] = None
    recovery_actions_count = 0

    try:
        obs, infos = env.reset()
        obs_text = obs[0] if isinstance(obs, (list, tuple)) else obs

        history: List[Dict[str, str]] = []
        done = False
        won = False
        step_count = 0
        injected = False

        while not done and step_count < MAX_STEPS:
            admissible = infos.get("admissible_commands", [[]])[0]
            if not admissible:
                break

            display_history = history
            injected_this_step = False
            if (not injected and step_count >= injection_step
                    and len(history) >= 2):
                display_history = apply_injection(
                    history, operator, op_config,
                )
                injected = True
                injected_this_step = True

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

            step_detected = False
            step_is_recovery = False
            if injected:
                step_detected = detect_error_in_think(think)
                step_is_recovery = is_recovery_action(action)
                if step_detected and detection_step is None:
                    detection_step = step_count
                if step_is_recovery:
                    recovery_actions_count += 1

            trajectory.append({
                "step": step_count,
                "observation": obs_text[:200],
                "action": action,
                "think_snippet": think[:300] if think else "",
                "injected_this_step": injected_this_step,
                "post_injection": injected,
                "detected_error": step_detected,
                "recovery_action": step_is_recovery,
            })

            history.append({"observation": obs_text, "action": action})

            obs, _rewards, dones, infos = env.step([action])
            obs_text = obs[0] if isinstance(obs, (list, tuple)) else obs
            done = dones[0] if isinstance(dones, (list, tuple)) else dones
            won = infos.get("won", [False])[0]
            step_count += 1
    finally:
        env.close()

    any_detection = detection_step is not None
    steps_after_injection = max(0, step_count - injection_step) if injected else 0

    return {
        "task_name": game_info.get("task_name", ""),
        "task_type": game_info["task_type"],
        "task_desc": game_info["task_desc"],
        "success": bool(won),
        "steps": step_count,
        "operator": operator.name,
        "injection_step": injection_step,
        "injected": injected,
        "recovery_analysis": {
            "detected": any_detection,
            "detection_step": detection_step,
            "recovery_actions_count": recovery_actions_count,
            "steps_after_injection": steps_after_injection,
        },
        "trajectory": trajectory,
    }


# ---------------------------------------------------------------------------
# Report builder
# ---------------------------------------------------------------------------

def build_recovery_report(
    results: List[Dict[str, Any]], args,
) -> Dict[str, Any]:
    """Aggregate per-episode results into summary report."""
    total = len(results)
    successes = sum(1 for r in results if r["success"])
    detected = sum(1 for r in results if r["recovery_analysis"]["detected"])

    report: Dict[str, Any] = {
        "model": args.model_path or args.base_model,
        "model_variant": args.model_variant,
        "inject": True,
        "seed": args.seed,
        "total_episodes": total,
        "success_rate": round(successes / total, 3) if total else 0,
        "recovery_rate": round(successes / total, 3) if total else 0,
        "detection_rate": round(detected / total, 3) if total else 0,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    op_stats: Dict[str, Dict[str, int]] = defaultdict(
        lambda: {"total": 0, "recovered": 0, "detected": 0}
    )
    for r in results:
        op = r["operator"]
        op_stats[op]["total"] += 1
        if r["success"]:
            op_stats[op]["recovered"] += 1
        if r["recovery_analysis"]["detected"]:
            op_stats[op]["detected"] += 1

    report["by_operator"] = {}
    for op_name, s in sorted(op_stats.items()):
        report["by_operator"][op_name] = {
            "total": s["total"],
            "recovered": s["recovered"],
            "detected": s["detected"],
            "recovery_rate": round(s["recovered"] / s["total"], 3) if s["total"] else 0,
            "detection_rate": round(s["detected"] / s["total"], 3) if s["total"] else 0,
        }

    type_stats: Dict[str, Dict[str, int]] = defaultdict(
        lambda: {"total": 0, "success": 0, "detected": 0}
    )
    for r in results:
        tt = r["task_type"]
        type_stats[tt]["total"] += 1
        if r["success"]:
            type_stats[tt]["success"] += 1
        if r["recovery_analysis"]["detected"]:
            type_stats[tt]["detected"] += 1

    report["by_task_type"] = {
        tt: {
            "total": c["total"],
            "success": c["success"],
            "detected": c["detected"],
            "rate": round(c["success"] / c["total"], 3) if c["total"] else 0,
        }
        for tt, c in sorted(type_stats.items())
    }

    report["episodes"] = results
    return report


# ---------------------------------------------------------------------------
# Compare two result files
# ---------------------------------------------------------------------------

def compare_injected_results(
    path_a: str, path_b: str, output_path: Optional[str] = None,
) -> Dict[str, Any]:
    """Compare recovery metrics between two injected eval results."""
    with open(path_a) as f:
        data_a = json.load(f)
    with open(path_b) as f:
        data_b = json.load(f)

    a_by_task = {e["task_name"]: e for e in data_a["episodes"]}
    b_by_task = {e["task_name"]: e for e in data_b["episodes"]}

    common = sorted(set(a_by_task) & set(b_by_task))
    a_succ = [a_by_task[t]["success"] for t in common]
    b_succ = [b_by_task[t]["success"] for t in common]
    a_det = [a_by_task[t]["recovery_analysis"]["detected"] for t in common]
    b_det = [b_by_task[t]["recovery_analysis"]["detected"] for t in common]

    a_rate = float(np.mean(a_succ)) if common else 0
    b_rate = float(np.mean(b_succ)) if common else 0
    a_det_rate = float(np.mean(a_det)) if common else 0
    b_det_rate = float(np.mean(b_det)) if common else 0

    p = mcnemar_test(a_succ, b_succ)
    ci_lo, ci_hi = bootstrap_ci(
        [int(s) for s in a_succ], [int(s) for s in b_succ],
    )

    comparison = {
        "model_a": data_a.get("model", ""),
        "model_b": data_b.get("model", ""),
        "variant_a": data_a.get("model_variant", ""),
        "variant_b": data_b.get("model_variant", ""),
        "num_common_tasks": len(common),
        "recovery_rate_a": round(a_rate, 3),
        "recovery_rate_b": round(b_rate, 3),
        "recovery_diff": round(a_rate - b_rate, 3),
        "detection_rate_a": round(a_det_rate, 3),
        "detection_rate_b": round(b_det_rate, 3),
        "mcnemar_p_value": round(p, 4),
        "bootstrap_ci_95": [round(ci_lo, 3), round(ci_hi, 3)],
        "significant_at_005": p < 0.05,
    }

    print(json.dumps(comparison, indent=2), flush=True)

    if output_path:
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        with open(output_path, "w") as f:
            json.dump(comparison, f, indent=2)
        print(f"Saved to {output_path}", flush=True)

    return comparison


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="TaxEI Injected Evaluation — recovery under error injection",
    )
    parser.add_argument("--model_path", type=str, default=None,
                        help="LoRA adapter checkpoint path (omit for zero-shot)")
    parser.add_argument("--base_model", type=str,
                        default="/root/autodl-tmp/models/Qwen/Qwen3-8B")
    parser.add_argument("--model_variant", type=str, default="taxei",
                        choices=["taxei", "random", "vanilla"],
                        help="Model variant label for reporting")
    parser.add_argument("--alfworld_data", type=str,
                        default="/root/autodl-tmp/alfworld_data")
    parser.add_argument("--eval_split", type=str, default="valid_unseen")
    parser.add_argument("--num_episodes", type=int, default=47)
    parser.add_argument("--output", type=str,
                        default="eval_results/injected_results.json")
    parser.add_argument("--device", type=str, default="cuda:0")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--inject_step", type=int, default=-1,
                        help="Fixed injection step (-1 = random in [2,6])")
    parser.add_argument("--task_list", type=str, default=None,
                        help="Path to JSON file with fixed task list")
    parser.add_argument("--compare_with", type=str, default=None,
                        help="Path to another result JSON for comparison")
    parser.add_argument("--compare_output", type=str, default=None,
                        help="Path to save comparison JSON")

    args = parser.parse_args()

    if args.compare_with:
        if not os.path.exists(args.output):
            print(f"Error: {args.output} not found", file=sys.stderr)
            sys.exit(1)
        compare_injected_results(args.output, args.compare_with, args.compare_output)
        return

    if args.task_list:
        games = load_task_list(args.task_list)
        print(f"Loaded {len(games)} tasks from {args.task_list}", flush=True)
    else:
        data_path = os.path.join(args.alfworld_data, "json_2.1.1", args.eval_split)
        games = collect_game_files(data_path)
        print(f"Found {len(games)} tasks in {args.eval_split}", flush=True)

    if 0 < args.num_episodes < len(games):
        games = games[:args.num_episodes]

    model = ModelInference(
        base_model=args.base_model,
        adapter_path=args.model_path,
        device=args.device,
    )

    results: List[Dict[str, Any]] = []
    rng = random.Random(args.seed)
    num_ops = len(OPERATORS)

    for i, game_info in enumerate(games):
        op = OPERATORS[i % num_ops]
        op_config = OPERATOR_CONFIGS[op.name]
        inj_step = args.inject_step if args.inject_step >= 0 else rng.randint(2, 6)

        result = run_injected_episode(
            model, game_info, op, op_config, inj_step,
        )
        results.append(result)

        status = "OK" if result["success"] else "FAIL"
        det = "D" if result["recovery_analysis"]["detected"] else "-"
        print(
            f"  [{i+1}/{len(games)}] {game_info['task_name']}: {status} "
            f"[{op.name}@step{inj_step}] det={det} "
            f"({result['steps']} steps)",
            flush=True,
        )

    report = build_recovery_report(results, args)

    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\nReport saved to {args.output}", flush=True)

    print(f"\n=== Injected Eval Summary ({args.model_variant}) ===", flush=True)
    print(f"Total: {report['total_episodes']}", flush=True)
    print(f"Recovery rate (task success): {report['recovery_rate']}", flush=True)
    print(f"Detection rate (think analysis): {report['detection_rate']}", flush=True)
    print(f"\nPer-operator:", flush=True)
    for op_name, stats in report["by_operator"].items():
        print(
            f"  {op_name}: recovered={stats['recovered']}/{stats['total']} "
            f"({stats['recovery_rate']}), "
            f"detected={stats['detected']}/{stats['total']} "
            f"({stats['detection_rate']})",
            flush=True,
        )


if __name__ == "__main__":
    main()
