"""Episode-terminal counterfactual labeling for SimGate routing.

Problem: 1-step oracle labeling (phase1_signal.py) yields 98.2% tie rate because
single-step score deltas are almost always 0. This script instead forks the
environment at action-diverge points and continues for K steps, using the
final score difference as the label signal.

Pipeline per episode:
  1. Run main episode step-by-step
  2. At each step, get internal_action (ReAct) and det_action (fork-evaluate candidates)
  3. If they agree → tie, advance
  4. If they differ → fork twice (one per action), continue K steps with base policy,
     compare final scores → label = deterministic / internal / tie
  5. Advance main env with the oracle-chosen action

Inputs:  task type, LLM agent (Qwen2.5-7B on GPU)
Outputs: {output_dir}/{task_type}/cf_labels.jsonl

Relation to phase1_signal.py:
  - Reuses the same ScienceWorldEnv / LLMAgent / fork_and_lookahead infra
  - Replaces the 1-step oracle with K-step counterfactual evaluation
"""

import argparse
import json
import os
import random
import sys
import time
from typing import List, Dict, Any, Optional, Tuple

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
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
    best_delta_fb = float("-inf")
    fork_results = []

    for cand in candidates:
        fr = fork_and_lookahead(task_name, variation_idx, action_history, cand)
        lethal = is_lethal(fr)
        fork_results.append({
            "action": cand, "score_delta": fr["score_delta"],
            "score": fr["score"], "lethal": lethal,
        })
        if fr["score_delta"] > best_delta_fb:
            best_delta_fb = fr["score_delta"]
            best_fallback = cand
        if not lethal and fr["score_delta"] > best_delta:
            best_delta = fr["score_delta"]
            best_action = cand

    if best_action is None:
        best_action = best_fallback if best_fallback else valid_actions[0]
        best_delta = best_delta_fb

    return best_action, best_delta, fork_results


def fork_and_continue(
    agent: LLMAgent,
    task_name: str,
    variation_idx: int,
    action_history: List[str],
    first_action: str,
    continuation_steps: int = 10,
) -> float:
    """Fork env, execute first_action, then continue K steps with base policy
    (always-internal ReAct). Returns final score. Always closes the forked env."""
    fork_env = None
    try:
        fork_env = create_env(task_name, variation_idx)
        reset_env(fork_env)

        for past_action in action_history:
            step_env(fork_env, past_action)

        obs, reward, done, info = step_env(fork_env, first_action)

        history_dicts = []
        for k in range(continuation_steps):
            if done:
                break
            valid = get_valid_actions(fork_env)
            if not valid:
                break
            action, _ = agent.select_action_react(obs, valid, history_dicts)
            obs, reward, done, info = step_env(fork_env, action)
            history_dicts.append({"action": action, "observation": obs[:200], "score": get_score(fork_env)})

        return get_score(fork_env)
    except Exception as e:
        print(f"  [WARN] fork_and_continue failed: {e}")
        return 0.0
    finally:
        if fork_env is not None:
            close_env(fork_env)


def run_episode(
    agent: LLMAgent,
    task_name: str,
    variation_idx: int,
    max_steps: int,
    continuation_steps: int,
    n_candidates: int = 3,
) -> Dict[str, Any]:
    env = create_env(task_name, variation_idx)
    obs, _ = reset_env(env)

    labels = []
    action_history = []
    history_dicts = []
    fork_times = []
    t0 = time.time()

    for step_idx in range(max_steps):
        valid_actions = get_valid_actions(env)
        if not valid_actions:
            break

        # Internal action (ReAct)
        internal_action, react_raw = agent.select_action_react(obs, valid_actions, history_dicts)

        # Death filter for internal action
        _remaining = list(valid_actions)
        for _retry in range(3):
            fr = fork_and_lookahead(task_name, variation_idx, action_history, internal_action)
            if not is_lethal(fr):
                break
            _remaining = [a for a in _remaining if a != internal_action]
            if not _remaining:
                break
            internal_action, react_raw = agent.select_action_react(obs, _remaining, history_dicts)

        # Deterministic action
        det_action, det_delta, det_forks = get_deterministic_action(
            agent, task_name, variation_idx, obs, valid_actions,
            action_history, history_dicts, n_candidates,
        )

        if internal_action == det_action:
            labels.append({"step": step_idx, "label": "tie", "score_diff": 0.0})
            chosen = internal_action
        else:
            # Fork both and continue K steps
            t_fork = time.time()
            fork_int_score = fork_and_continue(
                agent, task_name, variation_idx, action_history,
                internal_action, continuation_steps,
            )
            fork_det_score = fork_and_continue(
                agent, task_name, variation_idx, action_history,
                det_action, continuation_steps,
            )
            fork_elapsed = time.time() - t_fork
            fork_times.append(fork_elapsed)

            score_diff = fork_det_score - fork_int_score
            if score_diff > 0:
                best = "deterministic"
            elif score_diff < 0:
                best = "internal"
            else:
                best = "tie"

            labels.append({
                "step": step_idx,
                "obs": obs[:500],
                "internal_action": internal_action,
                "det_action": det_action,
                "fork_internal_score": fork_int_score,
                "fork_det_score": fork_det_score,
                "score_diff": score_diff,
                "label": best,
                "fork_time_s": round(fork_elapsed, 2),
            })

            chosen = det_action if score_diff > 0 else internal_action

        score_before = get_score(env)
        obs_new, reward, done, info = step_env(env, chosen)
        score_after = get_score(env)

        action_history.append(chosen)
        history_dicts.append({"action": chosen, "observation": obs_new[:200], "score": score_after})
        obs = obs_new

        diverge_tag = "" if internal_action == det_action else f" DIVERGE→{labels[-1]['label']}"
        print(f"    step {step_idx}: score {score_before:.0f}→{score_after:.0f} "
              f"action='{chosen[:40]}'{diverge_tag}")

        if done:
            break

    final_score = get_score(env)
    close_env(env)

    label_counts = {"deterministic": 0, "internal": 0, "tie": 0}
    for lb in labels:
        label_counts[lb["label"]] += 1
    diverge_steps = label_counts["deterministic"] + label_counts["internal"]

    return {
        "episode": -1,  # filled by caller
        "variation": variation_idx,
        "total_steps": len(labels),
        "diverge_steps": diverge_steps,
        "tie_steps": label_counts["tie"],
        "labels": labels,
        "final_score": final_score,
        "label_summary": label_counts,
        "total_time_s": round(time.time() - t0, 1),
        "avg_fork_time_s": round(sum(fork_times) / len(fork_times), 2) if fork_times else 0.0,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Episode-terminal counterfactual labeling for SimGate routing"
    )
    parser.add_argument("--task_type", type=str, required=True,
                        help="ScienceWorld task name (e.g. boil, melt)")
    parser.add_argument("--episodes", type=int, default=20)
    parser.add_argument("--gpu_id", type=int, default=0)
    parser.add_argument("--max_steps", type=int, default=30)
    parser.add_argument("--continuation_steps", type=int, default=10,
                        help="K: steps to continue after fork")
    parser.add_argument("--output_dir", type=str, default="results/cf_labels/")
    parser.add_argument("--model_path", type=str, default=None)
    parser.add_argument("--use_vllm", action="store_true", default=True)
    parser.add_argument("--no_vllm", action="store_true", default=False)
    parser.add_argument("--n_candidates", type=int, default=3)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    if args.no_vllm:
        args.use_vllm = False

    random.seed(args.seed)
    task_name = resolve_task_type(args.task_type)

    print(f"=== CF LABELING SETUP ===")
    print(f"Task: {task_name} | Episodes: {args.episodes} | Max steps: {args.max_steps}")
    print(f"Continuation K={args.continuation_steps} | GPU: {args.gpu_id} | Seed: {args.seed}")

    agent = LLMAgent(
        model_path=args.model_path,
        use_vllm=args.use_vllm,
        gpu_id=args.gpu_id,
    )

    max_var = get_max_variations(task_name)
    task_dir = os.path.join(args.output_dir, task_name.replace(" ", "_"))
    os.makedirs(task_dir, exist_ok=True)
    out_file = os.path.join(task_dir, "cf_labels.jsonl")

    all_diverge = 0
    all_steps = 0
    all_labels = {"deterministic": 0, "internal": 0, "tie": 0}
    all_fork_times = []

    for ep_idx in range(args.episodes):
        variation_idx = ep_idx % max_var
        print(f"\n--- Episode {ep_idx}/{args.episodes} (variation={variation_idx}) ---")

        result = run_episode(
            agent, task_name, variation_idx,
            args.max_steps, args.continuation_steps, args.n_candidates,
        )
        result["episode"] = ep_idx

        with open(out_file, "a") as f:
            f.write(json.dumps(result, default=str) + "\n")

        all_steps += result["total_steps"]
        all_diverge += result["diverge_steps"]
        for k in ("deterministic", "internal", "tie"):
            all_labels[k] += result["label_summary"][k]
        if result["avg_fork_time_s"] > 0:
            all_fork_times.append(result["avg_fork_time_s"])

        print(f"  → score={result['final_score']:.1f} | "
              f"diverge={result['diverge_steps']}/{result['total_steps']} | "
              f"labels: det={result['label_summary']['deterministic']} "
              f"int={result['label_summary']['internal']} "
              f"tie={result['label_summary']['tie']} | "
              f"{result['total_time_s']:.0f}s")

    # Summary
    diverge_pct = 100.0 * all_diverge / all_steps if all_steps > 0 else 0
    avg_fork = sum(all_fork_times) / len(all_fork_times) if all_fork_times else 0
    print(f"\n{'='*50}")
    print(f"=== CF LABELING: {task_name} ===")
    print(f"Episodes: {args.episodes}")
    print(f"Total steps: {all_steps}")
    print(f"Diverge steps: {all_diverge} ({diverge_pct:.1f}%)")
    print(f"Labels: det={all_labels['deterministic']}, int={all_labels['internal']}, tie={all_labels['tie']}")
    print(f"Avg continuation time per fork: {avg_fork:.1f}s")
    print(f"Output: {out_file}")
    print(f"{'='*50}")


if __name__ == "__main__":
    main()
