"""Plan-004 shared evaluation harness: Explicit vs Implicit Routing ablation.

Three conditions share this eval framework:
  (a) 1.7B Explicit router — plan-002 router_sft_train.py (classification head)
  (b) 1.7B Implicit router — Qwen3-1.7B SFT, outputs [SIMULATE] prefix inline
  (c) 7B Implicit router  — Qwen2.5-7B-Instruct tool-use, calls simulate() tool

Data flow:
  1. Load oracle labels from sft_triples.jsonl for routing accuracy comparison
  2. For each (task, variation), reset ScienceWorld env
  3. At each step, call router_fn(obs, valid_actions, history) → (action, route)
     route ∈ {"deterministic", "internal"}
  4. If route == "deterministic": fork_and_lookahead to evaluate candidate actions
     If route == "internal": use the LLM-chosen action directly
  5. Log step-level decisions and episode-level outcomes
  6. Aggregate: episode score, routing accuracy vs oracle, death rate

Usage:
  from ablation_eval_common import run_ablation_eval, EvalConfig
"""

import argparse
import json
import os
import sys
import time
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Optional, Tuple, Any

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scienceworld_utils import (
    create_env, reset_env, get_valid_actions, get_score,
    step_env, close_env, fork_and_lookahead, get_task_types,
    get_max_variations,
    ALL_MVP_TASKS,
)
from llm_agent import LLMAgent, find_model_path

# Type alias for the router function each condition must implement.
# Signature: (obs, valid_actions, action_history) → (chosen_action, route_decision)
#   route_decision ∈ {"deterministic", "internal"}
RouterFn = Callable[
    [str, List[str], List[dict]],
    Tuple[str, str],
]

DEATH_SCORE = -100.0


@dataclass
class EvalConfig:
    task_types: List[str]
    max_variations: int = 5
    max_steps: int = 30
    gpu_id: int = 0
    output_dir: str = "results/ablation/"
    condition_name: str = "unknown"
    oracle_data_path: str = "results/sft_data_death_aware/sft_triples.jsonl"


@dataclass
class StepRecord:
    step_idx: int
    observation: str
    action: str
    route_decision: str  # "deterministic" or "internal"
    score_after: float
    done: bool


@dataclass
class EpisodeResult:
    task_type: str
    variation: int
    final_score: float
    num_steps: int
    died: bool
    steps: List[StepRecord]
    route_counts: Dict[str, int]


# ---------------------------------------------------------------------------
# Oracle label loading (for routing accuracy comparison)
# ---------------------------------------------------------------------------

def load_oracle_labels(path: str) -> Dict[str, str]:
    """Load oracle routing labels keyed by (task_type, variation, step_idx).

    Returns dict: "{task_type}:{variation}:{step_idx}" → "deterministic" | "internal"
    """
    oracle = {}
    if not os.path.exists(path):
        return oracle
    with open(path) as f:
        for line in f:
            rec = json.loads(line)
            label_raw = rec["label"]
            label = "deterministic" if "det" in label_raw else "internal"
            key = f"{rec['task_type']}:{rec['variation']}:{rec['step_idx']}"
            oracle[key] = label
    return oracle


# ---------------------------------------------------------------------------
# Single episode execution with routing
# ---------------------------------------------------------------------------

def run_routed_episode(
    task_type: str,
    variation: int,
    router_fn: RouterFn,
    max_steps: int = 30,
    gpu_id: int = 0,
) -> EpisodeResult:
    """Run one ScienceWorld episode with step-level routing decisions.

    At each step:
      1. Get observation and valid actions from env
      2. Call router_fn → (action, route_decision)
      3. If route == "deterministic": run fork_and_lookahead on candidate actions,
         pick the best-scoring action
      4. If route == "internal": execute the action directly
      5. Step the environment

    Returns EpisodeResult with full step trace.
    """
    env = create_env(task_type, variation, gpu_id=gpu_id)
    obs, info = reset_env(env)
    history: List[dict] = []
    steps: List[StepRecord] = []
    route_counts = {"deterministic": 0, "internal": 0}
    done = False

    for step_idx in range(max_steps):
        if done:
            break

        valid_actions = get_valid_actions(env)
        action, route = router_fn(obs, valid_actions, history)
        route_counts[route] = route_counts.get(route, 0) + 1

        if route == "deterministic":
            # TODO: fork_and_lookahead with candidate actions
            # For now, use the router-chosen action as-is
            # Full impl: generate candidates → fork each → pick best score
            pass

        obs, reward, done, info = step_env(env, action)
        score = get_score(env)

        steps.append(StepRecord(
            step_idx=step_idx,
            observation=obs,
            action=action,
            route_decision=route,
            score_after=score,
            done=done,
        ))
        history.append({"step": step_idx, "action": action, "observation": obs})

    final_score = get_score(env)
    close_env(env)

    return EpisodeResult(
        task_type=task_type,
        variation=variation,
        final_score=final_score,
        num_steps=len(steps),
        died=(final_score <= DEATH_SCORE),
        steps=steps,
        route_counts=route_counts,
    )


# ---------------------------------------------------------------------------
# Metric computation
# ---------------------------------------------------------------------------

def compute_routing_accuracy(
    episodes: List[EpisodeResult],
    oracle: Dict[str, str],
) -> Dict[str, Any]:
    """Compare predicted routing decisions against oracle labels.

    Returns dict with overall accuracy, per-class precision/recall,
    and confusion matrix counts.
    """
    correct = 0
    total = 0
    confusion = {"tp_det": 0, "fp_det": 0, "fn_det": 0, "tp_int": 0}

    for ep in episodes:
        for s in ep.steps:
            key = f"{ep.task_type}:{ep.variation}:{s.step_idx}"
            if key not in oracle:
                continue
            oracle_route = oracle[key]
            total += 1
            if s.route_decision == oracle_route:
                correct += 1
            if oracle_route == "deterministic":
                if s.route_decision == "deterministic":
                    confusion["tp_det"] += 1
                else:
                    confusion["fn_det"] += 1
            else:
                if s.route_decision == "deterministic":
                    confusion["fp_det"] += 1
                else:
                    confusion["tp_int"] += 1

    accuracy = correct / total if total > 0 else 0.0
    return {
        "accuracy": accuracy,
        "total_compared": total,
        "correct": correct,
        "confusion": confusion,
    }


def compute_episode_metrics(episodes: List[EpisodeResult]) -> Dict[str, Any]:
    """Aggregate episode-level metrics across all evaluated episodes.

    Returns: mean_score, death_rate, mean_steps, route_ratio, per_task breakdown.
    """
    if not episodes:
        return {}

    scores = [e.final_score for e in episodes]
    deaths = sum(1 for e in episodes if e.died)
    total_det = sum(e.route_counts.get("deterministic", 0) for e in episodes)
    total_int = sum(e.route_counts.get("internal", 0) for e in episodes)
    total_steps = total_det + total_int

    per_task: Dict[str, list] = {}
    for e in episodes:
        per_task.setdefault(e.task_type, []).append(e.final_score)

    return {
        "n_episodes": len(episodes),
        "mean_score": sum(scores) / len(scores),
        "death_rate": deaths / len(episodes),
        "mean_steps": sum(e.num_steps for e in episodes) / len(episodes),
        "route_ratio_det": total_det / total_steps if total_steps > 0 else 0,
        "route_ratio_int": total_int / total_steps if total_steps > 0 else 0,
        "per_task_mean_score": {
            t: sum(s) / len(s) for t, s in per_task.items()
        },
    }


# ---------------------------------------------------------------------------
# Full ablation evaluation entry point
# ---------------------------------------------------------------------------

def run_ablation_eval(
    config: EvalConfig,
    router_fn: RouterFn,
) -> Dict[str, Any]:
    """Run full evaluation for one ablation condition.

    Steps:
      1. Load oracle labels
      2. For each task × variation, run_routed_episode
      3. Compute routing accuracy and episode metrics
      4. Save results to config.output_dir/{condition_name}/

    Returns combined metrics dict.
    """
    oracle = load_oracle_labels(config.oracle_data_path)
    all_episodes: List[EpisodeResult] = []

    out_dir = os.path.join(config.output_dir, config.condition_name)
    os.makedirs(out_dir, exist_ok=True)

    for task in config.task_types:
        n_vars = min(config.max_variations, get_max_variations(task))
        for var_idx in range(n_vars):
            print(f"[{config.condition_name}] {task} var={var_idx}")
            ep = run_routed_episode(
                task_type=task,
                variation=var_idx,
                router_fn=router_fn,
                max_steps=config.max_steps,
                gpu_id=config.gpu_id,
            )
            all_episodes.append(ep)

    ep_metrics = compute_episode_metrics(all_episodes)
    routing_metrics = compute_routing_accuracy(all_episodes, oracle)

    results = {
        "condition": config.condition_name,
        "episode_metrics": ep_metrics,
        "routing_accuracy": routing_metrics,
    }

    results_path = os.path.join(out_dir, "eval_results.json")
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Results saved to {results_path}")

    return results


def add_eval_args(parser: argparse.ArgumentParser) -> None:
    """Add shared evaluation CLI args to an argparse parser."""
    parser.add_argument("--task_types", type=str, default="boil,melt,change-the-state-of-matter-of")
    parser.add_argument("--max_variations", type=int, default=5)
    parser.add_argument("--max_steps", type=int, default=30)
    parser.add_argument("--gpu_id", type=int, default=0)
    parser.add_argument("--output_dir", type=str, default="results/ablation/")
    parser.add_argument("--oracle_data", type=str,
                        default="results/sft_data_death_aware/sft_triples.jsonl")


def config_from_args(args, condition_name: str) -> EvalConfig:
    """Build EvalConfig from parsed args."""
    return EvalConfig(
        task_types=[t.strip() for t in args.task_types.split(",")],
        max_variations=args.max_variations,
        max_steps=args.max_steps,
        gpu_id=args.gpu_id,
        output_dir=args.output_dir,
        condition_name=condition_name,
        oracle_data_path=args.oracle_data,
    )
