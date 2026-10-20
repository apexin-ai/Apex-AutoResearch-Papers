"""Episode-level counterfactual labeling (Algorithm 1).

Runs each task instance under two pure strategies (internal-only vs.
deterministic-only) and compares terminal scores to produce a routing label.

Pipeline per episode (paired mode, default):
  1. Run full episode under internal strategy (ReAct chain-of-thought)
  2. Run full episode under deterministic strategy (ground-truth observations)
  3. Compare terminal scores with death-aware priority: if one strategy
     dies and the other survives, the survivor is preferred regardless of
     score; otherwise compare scores directly (Algorithm 1 in paper)

Also supports oracle mode (fork-and-lookahead at diverge points) for
per-step labeling experiments.

Inputs:  task type, LLM agent (Qwen2.5-7B on GPU)
Outputs: {output_dir}/{task_type}/cf_labels.jsonl
"""

import argparse
import json
import os
import random
import sys
import time
from typing import List, Dict, Any, Optional, Tuple

from scienceworld_utils import (
    create_env, reset_env, get_valid_actions, get_score,
    step_env, close_env, fork_and_lookahead, get_task_types,
    get_max_variations,
)
from llm_agent import LLMAgent, find_model_path


def resolve_task_type(name: str) -> str:
    try:
        available = get_task_types()
    except Exception:
        return name
    if name in available:
        return name
    matches = [t for t in available if name.lower() in t.lower()]
    if matches:
        return matches[0]
    return name


def is_lethal(fr: Dict[str, Any]) -> bool:
    if fr["done"] and fr["score"] < 0:
        return True
    if fr["score"] <= -100:
        return True
    return False


def get_deterministic_action(
    agent: LLMAgent,
    task_name: str,
    variation_idx: int,
    obs: str,
    valid_actions: List[str],
    action_history: List[str],
    history_dicts: List[dict],
    n_candidates: int = 3,
) -> Tuple[str, float, List[dict]]:
    """Generate candidates via LLM, fork-evaluate each with 1-step lookahead,
    return (best_action, best_delta, fork_results). Filters lethal actions."""
    candidates, _ = agent.generate_candidate_actions(
        obs, valid_actions, history_dicts, n=n_candidates
    )

    best_action = None
    best_delta = float("-inf")
    best_fallback = None
    fork_results = []

    current_score = get_score()

    for action in candidates:
        fr = fork_and_lookahead(
            task_name, variation_idx, action_history, action, steps=1
        )
        fork_results.append(fr)

        if is_lethal(fr):
            continue

        delta = fr["score"] - current_score
        if delta > best_delta:
            best_delta = delta
            best_action = action
        if best_fallback is None:
            best_fallback = action

    if best_action is None:
        best_action = best_fallback or candidates[0]
        best_delta = 0.0

    return best_action, best_delta, fork_results


def run_counterfactual_episode(
    agent: LLMAgent,
    task_name: str,
    variation_idx: int,
    lookahead_steps: int = 5,
    max_steps: int = 30,
) -> Dict[str, Any]:
    """Run one episode with counterfactual forking at diverge points."""

    env = create_env(task_name, variation_idx)
    obs = reset_env(env)
    action_history = []
    history_dicts = []
    step_records = []
    diverge_count = 0

    for step_idx in range(max_steps):
        valid_actions = get_valid_actions(env)
        score_before = get_score(env)

        internal_action = agent.select_action_react(
            obs, valid_actions, history_dicts
        )

        det_action, det_delta, fork_results = get_deterministic_action(
            agent, task_name, variation_idx, obs, valid_actions,
            action_history, history_dicts
        )

        if internal_action == det_action:
            label = "tie"
            chosen_action = internal_action
        else:
            diverge_count += 1
            fr_internal = fork_and_lookahead(
                task_name, variation_idx, action_history,
                internal_action, steps=lookahead_steps
            )
            fr_det = fork_and_lookahead(
                task_name, variation_idx, action_history,
                det_action, steps=lookahead_steps
            )

            if fr_det["score"] > fr_internal["score"]:
                label = "det-preferred"
                chosen_action = det_action
            elif fr_internal["score"] > fr_det["score"]:
                label = "internal-preferred"
                chosen_action = internal_action
            else:
                label = "tie"
                chosen_action = internal_action

        step_records.append({
            "step": step_idx,
            "observation": obs,
            "internal_action": internal_action,
            "det_action": det_action,
            "label": label,
            "chosen_action": chosen_action,
            "score_before": score_before,
        })

        obs, reward, done, info = step_env(env, chosen_action)
        action_history.append(chosen_action)
        history_dicts.append({
            "step": step_idx,
            "action": chosen_action,
            "observation": obs,
        })

        if done:
            break

    final_score = get_score(env)
    close_env(env)

    return {
        "task_type": task_name,
        "variation": variation_idx,
        "steps": step_records,
        "final_score": final_score,
        "n_diverge": diverge_count,
        "n_steps": len(step_records),
    }


def run_paired_episode(
    agent: LLMAgent,
    task_name: str,
    variation_idx: int,
    max_steps: int = 30,
) -> Dict[str, Any]:
    """Run always-internal and always-deterministic trajectories for comparison."""
    results = {}

    for mode in ["internal", "deterministic"]:
        env = create_env(task_name, variation_idx)
        obs = reset_env(env)
        action_history = []
        history_dicts = []
        steps = []

        for step_idx in range(max_steps):
            valid_actions = get_valid_actions(env)

            if mode == "internal":
                action = agent.select_action_react(obs, valid_actions, history_dicts)
            else:
                action, _, _ = get_deterministic_action(
                    agent, task_name, variation_idx, obs, valid_actions,
                    action_history, history_dicts
                )

            obs, reward, done, info = step_env(env, action)
            steps.append({"step": step_idx, "action": action, "observation": obs})
            action_history.append(action)
            history_dicts.append({"step": step_idx, "action": action, "observation": obs})

            if done:
                break

        final_score = get_score(env)
        close_env(env)
        results[f"always_{mode}"] = {
            "final_score": final_score,
            "steps": steps,
            "n_steps": len(steps),
            "death": final_score <= -100,
        }

    return {
        "task_type": task_name,
        "variation": variation_idx,
        **results,
    }


def main():
    parser = argparse.ArgumentParser(description="Counterfactual labeling for routing")
    parser.add_argument("--task_type", type=str, required=True)
    parser.add_argument("--n_episodes", type=int, default=30)
    parser.add_argument("--lookahead_steps", type=int, default=5)
    parser.add_argument("--max_steps", type=int, default=30)
    parser.add_argument("--model_path", type=str, default=None)
    parser.add_argument("--gpu_id", type=int, default=0)
    parser.add_argument("--output_dir", type=str, default="results/counterfactual")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--mode", type=str, default="paired",
                        choices=["paired", "oracle"],
                        help="paired: always-int vs always-det. oracle: per-step forking.")
    args = parser.parse_args()

    random.seed(args.seed)
    task_name = resolve_task_type(args.task_type)
    model_path = find_model_path(args.model_path)
    agent = LLMAgent(model_path=model_path, gpu_id=args.gpu_id)

    out_dir = os.path.join(args.output_dir, task_name)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "episodes.jsonl")

    max_var = get_max_variations(task_name)
    variations = random.sample(range(max_var), min(args.n_episodes, max_var))

    print(f"Task: {task_name}, {len(variations)} episodes, mode={args.mode}")

    with open(out_path, "w") as f:
        for i, var in enumerate(variations):
            t0 = time.time()
            if args.mode == "paired":
                result = run_paired_episode(agent, task_name, var, args.max_steps)
            else:
                result = run_counterfactual_episode(
                    agent, task_name, var, args.lookahead_steps, args.max_steps
                )
            elapsed = time.time() - t0
            f.write(json.dumps(result) + "\n")
            f.flush()
            print(f"  [{i+1}/{len(variations)}] var={var} done ({elapsed:.1f}s)")

    print(f"Saved {len(variations)} episodes to {out_path}")


if __name__ == "__main__":
    main()
