"""Phase 1: 3-way signal detection — always-internal vs always-deterministic vs oracle-routing.

For each task type × episode:
  A) always-internal: ReAct LLM picks every action
  B) always-deterministic: LLM generates candidates, fork evaluates each, pick best score_delta
  C) oracle-routing: run both A and B, pick whichever has higher score_delta

Usage:
  python src/phase1_signal.py --task_types "boil,melt" --episodes 20 --gpu_id 0
"""

import argparse
import json
import os
import random
import sys
import time
from typing import List, Dict, Any, Optional

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scienceworld_utils import (
    create_env, reset_env, get_valid_actions, get_score,
    step_env, close_env, fork_and_lookahead, get_task_types,
    get_max_variations,
    STRONG_TASKS, MEDIUM_TASKS, WEAK_TASKS, ALL_MVP_TASKS,
)
from llm_agent import LLMAgent, find_model_path


def resolve_task_type(name: str) -> str:
    """Resolve a short task name to the actual ScienceWorld task name."""
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
    """Check if a fork result indicates a lethal action."""
    if fr["done"] and fr["score"] < 0:
        return True
    if fr["score"] <= -100:
        return True
    return False


def run_episode_always_internal(
    agent: LLMAgent,
    task_name: str,
    variation_idx: int,
    max_steps: int,
) -> Dict[str, Any]:
    """Mode A: LLM ReAct picks every action."""
    env = create_env(task_name, variation_idx)
    obs, _ = reset_env(env)
    initial_score = get_score(env)

    steps = []
    action_history = []
    history_dicts = []
    t0 = time.time()

    for step_idx in range(max_steps):
        valid_actions = get_valid_actions(env)
        if not valid_actions:
            break

        action, raw_output = agent.select_action_react(obs, valid_actions, history_dicts)
        _remaining = list(valid_actions)
        for _retry in range(3):
            fr = fork_and_lookahead(task_name, variation_idx, action_history, action)
            if not is_lethal(fr):
                break
            _remaining = [a for a in _remaining if a != action]
            if not _remaining:
                break
            action, raw_output = agent.select_action_react(obs, _remaining, history_dicts)

        score_before = get_score(env)
        obs_new, reward, done, info = step_env(env, action)
        score_after = get_score(env)

        step_record = {
            "step": step_idx,
            "action": action,
            "modality": "internal",
            "score_before": score_before,
            "score_after": score_after,
            "score_delta": score_after - score_before,
            "observation": obs_new[:500],
            "llm_output": raw_output[:300],
        }
        steps.append(step_record)
        action_history.append(action)
        history_dicts.append({"action": action, "observation": obs_new[:200], "score": score_after})
        obs = obs_new

        if done:
            break

    final_score = get_score(env)
    close_env(env)

    return {
        "mode": "always-internal",
        "task_name": task_name,
        "variation_idx": variation_idx,
        "final_score": final_score,
        "initial_score": initial_score,
        "num_steps": len(steps),
        "total_time_s": time.time() - t0,
        "steps": steps,
        "action_history": action_history,
    }


def run_episode_always_deterministic(
    agent: LLMAgent,
    task_name: str,
    variation_idx: int,
    max_steps: int,
    n_candidates: int = 3,
) -> Dict[str, Any]:
    """Mode B: LLM generates candidates, fork evaluates each, pick best."""
    env = create_env(task_name, variation_idx)
    obs, _ = reset_env(env)
    initial_score = get_score(env)

    steps = []
    action_history = []
    history_dicts = []
    t0 = time.time()

    for step_idx in range(max_steps):
        valid_actions = get_valid_actions(env)
        if not valid_actions:
            break

        candidates, raw_output = agent.generate_candidate_actions(
            obs, valid_actions, history_dicts, n=n_candidates
        )

        # Fork-evaluate each candidate (filter lethal)
        best_action = None
        best_delta = float("-inf")
        best_action_fallback = None
        best_delta_fallback = float("-inf")
        fork_results = []
        for cand in candidates:
            fr = fork_and_lookahead(task_name, variation_idx, action_history, cand)
            lethal = is_lethal(fr)
            fork_results.append({"action": cand, "score_delta": fr["score_delta"], "score": fr["score"], "lethal": lethal})
            if fr["score_delta"] > best_delta_fallback:
                best_delta_fallback = fr["score_delta"]
                best_action_fallback = cand
            if not lethal and fr["score_delta"] > best_delta:
                best_delta = fr["score_delta"]
                best_action = cand

        if best_action is None:
            best_action = best_action_fallback if best_action_fallback else valid_actions[0]

        score_before = get_score(env)
        obs_new, reward, done, info = step_env(env, best_action)
        score_after = get_score(env)

        step_record = {
            "step": step_idx,
            "action": best_action,
            "modality": "deterministic",
            "score_before": score_before,
            "score_after": score_after,
            "score_delta": score_after - score_before,
            "candidates": fork_results,
            "observation": obs_new[:500],
        }
        steps.append(step_record)
        action_history.append(best_action)
        history_dicts.append({"action": best_action, "observation": obs_new[:200], "score": score_after})
        obs = obs_new

        if done:
            break

    final_score = get_score(env)
    close_env(env)

    return {
        "mode": "always-deterministic",
        "task_name": task_name,
        "variation_idx": variation_idx,
        "final_score": final_score,
        "initial_score": initial_score,
        "num_steps": len(steps),
        "total_time_s": time.time() - t0,
        "steps": steps,
        "action_history": action_history,
    }


def run_episode_oracle_routing(
    agent: LLMAgent,
    task_name: str,
    variation_idx: int,
    max_steps: int,
    n_candidates: int = 3,
) -> Dict[str, Any]:
    """Mode C: Oracle routing — run both modalities, pick better score_delta."""
    env = create_env(task_name, variation_idx)
    obs, _ = reset_env(env)
    initial_score = get_score(env)

    steps = []
    action_history = []
    history_dicts = []
    modality_counts = {"internal": 0, "deterministic": 0}
    t0 = time.time()

    for step_idx in range(max_steps):
        valid_actions = get_valid_actions(env)
        if not valid_actions:
            break

        # --- Internal modality ---
        internal_action, react_raw = agent.select_action_react(obs, valid_actions, history_dicts)
        internal_fr = fork_and_lookahead(task_name, variation_idx, action_history, internal_action)
        _remaining_int = list(valid_actions)
        for _retry in range(3):
            if not is_lethal(internal_fr):
                break
            _remaining_int = [a for a in _remaining_int if a != internal_action]
            if not _remaining_int:
                break
            internal_action, react_raw = agent.select_action_react(obs, _remaining_int, history_dicts)
            internal_fr = fork_and_lookahead(task_name, variation_idx, action_history, internal_action)
        internal_delta = internal_fr["score_delta"]

        # --- Deterministic modality ---
        candidates, cand_raw = agent.generate_candidate_actions(
            obs, valid_actions, history_dicts, n=n_candidates
        )
        best_det_action = None
        best_det_delta = float("-inf")
        best_det_fallback = None
        best_det_delta_fb = float("-inf")
        det_fork_results = []
        for cand in candidates:
            fr = fork_and_lookahead(task_name, variation_idx, action_history, cand)
            lethal = is_lethal(fr)
            det_fork_results.append({"action": cand, "score_delta": fr["score_delta"], "lethal": lethal})
            if fr["score_delta"] > best_det_delta_fb:
                best_det_delta_fb = fr["score_delta"]
                best_det_fallback = cand
            if not lethal and fr["score_delta"] > best_det_delta:
                best_det_delta = fr["score_delta"]
                best_det_action = cand

        if best_det_action is None:
            if best_det_fallback:
                best_det_action = best_det_fallback
                best_det_delta = best_det_delta_fb
            else:
                best_det_action = internal_action
                best_det_delta = internal_delta

        # --- Oracle: pick higher delta ---
        if internal_delta > best_det_delta:
            chosen_action = internal_action
            chosen_modality = "internal"
        else:
            chosen_action = best_det_action
            chosen_modality = "deterministic"

        modality_counts[chosen_modality] += 1

        score_before = get_score(env)
        obs_new, reward, done, info = step_env(env, chosen_action)
        score_after = get_score(env)

        step_record = {
            "step": step_idx,
            "action": chosen_action,
            "modality": chosen_modality,
            "score_before": score_before,
            "score_after": score_after,
            "score_delta": score_after - score_before,
            "internal_action": internal_action,
            "internal_delta": internal_delta,
            "det_action": best_det_action,
            "det_delta": best_det_delta,
            "observation": obs_new[:500],
        }
        steps.append(step_record)
        action_history.append(chosen_action)
        history_dicts.append({"action": chosen_action, "observation": obs_new[:200], "score": score_after})
        obs = obs_new

        if done:
            break

    final_score = get_score(env)
    close_env(env)

    return {
        "mode": "oracle-routing",
        "task_name": task_name,
        "variation_idx": variation_idx,
        "final_score": final_score,
        "initial_score": initial_score,
        "num_steps": len(steps),
        "total_time_s": time.time() - t0,
        "steps": steps,
        "action_history": action_history,
        "modality_counts": modality_counts,
    }


def run_task_type(
    agent: LLMAgent,
    task_name: str,
    n_episodes: int,
    max_steps: int,
    output_dir: str,
    n_candidates: int = 3,
) -> Dict[str, Any]:
    """Run all 3 modes for a task type across n_episodes variations."""
    task_dir = os.path.join(output_dir, task_name.replace(" ", "_"))
    os.makedirs(task_dir, exist_ok=True)

    episodes_file = os.path.join(task_dir, "episodes.jsonl")
    all_episodes = []

    max_var = get_max_variations(task_name)
    actual_unique = min(n_episodes, max_var)
    print(f"\n{'='*60}")
    print(f"Task: {task_name} | Episodes: {n_episodes} | Max steps: {max_steps}")
    print(f"Max variations: {max_var} | Unique variations used: {actual_unique}")
    if actual_unique < n_episodes:
        print(f"  WARNING: {n_episodes} episodes > {max_var} variations, some will repeat")
    print(f"{'='*60}")

    for ep_idx in range(n_episodes):
        variation_idx = ep_idx % max_var
        print(f"\n--- Episode {ep_idx}/{n_episodes} (variation={variation_idx}) ---")

        # A) always-internal
        print(f"  [A] always-internal...", end=" ", flush=True)
        t = time.time()
        r_internal = run_episode_always_internal(agent, task_name, variation_idx, max_steps)
        print(f"score={r_internal['final_score']:.1f} ({time.time()-t:.0f}s)")

        # B) always-deterministic
        print(f"  [B] always-deterministic...", end=" ", flush=True)
        t = time.time()
        r_det = run_episode_always_deterministic(
            agent, task_name, variation_idx, max_steps, n_candidates
        )
        print(f"score={r_det['final_score']:.1f} ({time.time()-t:.0f}s)")

        # C) oracle-routing
        print(f"  [C] oracle-routing...", end=" ", flush=True)
        t = time.time()
        r_oracle = run_episode_oracle_routing(
            agent, task_name, variation_idx, max_steps, n_candidates
        )
        mc = r_oracle.get("modality_counts", {})
        print(f"score={r_oracle['final_score']:.1f} "
              f"(int={mc.get('internal',0)}/det={mc.get('deterministic',0)}) "
              f"({time.time()-t:.0f}s)")

        episode_record = {
            "episode_idx": ep_idx,
            "variation_idx": variation_idx,
            "always_internal": r_internal,
            "always_deterministic": r_det,
            "oracle_routing": r_oracle,
        }
        all_episodes.append(episode_record)

        # Append to JSONL incrementally
        with open(episodes_file, "a") as f:
            f.write(json.dumps(episode_record, default=str) + "\n")

    # Compute summary
    scores_internal = [e["always_internal"]["final_score"] for e in all_episodes]
    scores_det = [e["always_deterministic"]["final_score"] for e in all_episodes]
    scores_oracle = [e["oracle_routing"]["final_score"] for e in all_episodes]

    import numpy as np
    summary = {
        "task_name": task_name,
        "n_episodes": n_episodes,
        "max_variations": max_var,
        "unique_variations": actual_unique,
        "note": "oracle uses greedy 1-step lookahead, not true upper bound",
        "always_internal": {
            "mean": float(np.mean(scores_internal)),
            "std": float(np.std(scores_internal)),
            "scores": scores_internal,
        },
        "always_deterministic": {
            "mean": float(np.mean(scores_det)),
            "std": float(np.std(scores_det)),
            "scores": scores_det,
        },
        "oracle_routing": {
            "mean": float(np.mean(scores_oracle)),
            "std": float(np.std(scores_oracle)),
            "scores": scores_oracle,
        },
        "oracle_minus_internal": {
            "mean": float(np.mean(scores_oracle) - np.mean(scores_internal)),
            "diffs": [o - i for o, i in zip(scores_oracle, scores_internal)],
        },
        "oracle_minus_det": {
            "mean": float(np.mean(scores_oracle) - np.mean(scores_det)),
            "diffs": [o - d for o, d in zip(scores_oracle, scores_det)],
        },
    }

    summary_file = os.path.join(task_dir, "summary.json")
    with open(summary_file, "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\n--- {task_name} Summary ---")
    print(f"  always-internal:      {summary['always_internal']['mean']:.1f} ± {summary['always_internal']['std']:.1f}")
    print(f"  always-deterministic: {summary['always_deterministic']['mean']:.1f} ± {summary['always_deterministic']['std']:.1f}")
    print(f"  oracle-routing:       {summary['oracle_routing']['mean']:.1f} ± {summary['oracle_routing']['std']:.1f}")
    print(f"  oracle - internal:    {summary['oracle_minus_internal']['mean']:+.1f}")
    print(f"  oracle - det:         {summary['oracle_minus_det']['mean']:+.1f}")

    return summary


def main():
    parser = argparse.ArgumentParser(description="Phase 1: 3-way signal detection")
    parser.add_argument("--task_types", type=str, required=True,
                        help="Comma-separated task type names")
    parser.add_argument("--episodes", type=int, default=20,
                        help="Episodes per task type")
    parser.add_argument("--gpu_id", type=int, default=0)
    parser.add_argument("--model_path", type=str, default=None)
    parser.add_argument("--use_vllm", action="store_true", default=True)
    parser.add_argument("--no_vllm", action="store_true", default=False,
                        help="Use HF transformers instead of vLLM")
    parser.add_argument("--output_dir", type=str, default="results/mvp/")
    parser.add_argument("--max_steps", type=int, default=30)
    parser.add_argument("--n_candidates", type=int, default=3,
                        help="Number of candidate actions for deterministic mode")
    args = parser.parse_args()

    if args.no_vllm:
        args.use_vllm = False

    random.seed(42)

    task_names_raw = [t.strip() for t in args.task_types.split(",") if t.strip()]
    task_names = [resolve_task_type(t) for t in task_names_raw]
    print(f"Task types: {task_names}")
    print(f"Episodes: {args.episodes}, Max steps: {args.max_steps}")
    print(f"GPU: {args.gpu_id}, vLLM: {args.use_vllm}")
    print(f"Random seed: 42")

    agent = LLMAgent(
        model_path=args.model_path,
        use_vllm=args.use_vllm,
        gpu_id=args.gpu_id,
    )

    os.makedirs(args.output_dir, exist_ok=True)
    all_summaries = {}

    for task_name in task_names:
        summary = run_task_type(
            agent, task_name, args.episodes, args.max_steps,
            args.output_dir, args.n_candidates,
        )
        all_summaries[task_name] = summary

    # Save global summary
    global_summary_path = os.path.join(args.output_dir, "global_summary.json")
    with open(global_summary_path, "w") as f:
        json.dump(all_summaries, f, indent=2)
    print(f"\nGlobal summary saved to {global_summary_path}")


if __name__ == "__main__":
    main()
