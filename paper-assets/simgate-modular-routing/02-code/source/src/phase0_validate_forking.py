"""Phase 0: Validate ScienceWorld state forking via action-replay.

Tests fork feasibility across multiple task types and variations.
Gate criteria:
  - Fork success rate >= 80%
  - Single fork latency < 5s (p95)
  - JVM memory stays bounded

Usage: python src/phase0_validate_forking.py [--num_steps 10] [--fork_at 5]
"""

import argparse
import json
import os
import sys
import time
import resource
from collections import defaultdict
from typing import List, Dict, Any

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scienceworld_utils import (
    create_env, reset_env, get_valid_actions, get_score,
    step_env, close_env, fork_and_lookahead, get_task_types,
    STRONG_TASKS, MEDIUM_TASKS, WEAK_TASKS,
)

# All 5 MVP task types — validate forking on each to avoid Phase 1 surprises
PHASE0_TASKS = {
    "boil": [0, 1, 2, 3],
    "melt": [0, 1, 2],
    "change-the-state-of-matter-of": [0, 1, 2],
    "chemistry-mix-paint-secondary-color": [0, 1],
    "grow-plant": [0, 1],
}


def get_memory_mb() -> float:
    """Current process RSS in MB (Linux)."""
    try:
        with open("/proc/self/status") as f:
            for line in f:
                if line.startswith("VmRSS:"):
                    return int(line.split()[1]) / 1024.0
    except Exception:
        pass
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024.0


def validate_one_variation(
    task_name: str,
    variation_idx: int,
    num_steps: int = 10,
    fork_at: int = 5,
) -> Dict[str, Any]:
    """Run one variation, fork at fork_at step, measure fork quality."""
    result = {
        "task_name": task_name,
        "variation_idx": variation_idx,
        "fork_success": False,
        "fork_latency_s": None,
        "obs_match": False,
        "score_match": False,
        "error": None,
        "mem_before_mb": get_memory_mb(),
    }

    env = None
    try:
        env = create_env(task_name, variation_idx)
        obs, _ = reset_env(env)

        action_history = []
        observations = []
        scores = []

        for step_i in range(num_steps):
            valid_actions = get_valid_actions(env)
            if not valid_actions:
                break
            # Pick first valid action (deterministic, for reproducibility)
            action = valid_actions[0]
            obs_new, reward, done, info = step_env(env, action)
            score = get_score(env)

            action_history.append(action)
            observations.append(obs_new)
            scores.append(score)

            if done:
                break

        actual_steps = len(action_history)
        actual_fork_at = min(fork_at, actual_steps - 1) if actual_steps > 1 else 0

        if actual_steps < 2:
            result["error"] = f"Only {actual_steps} steps completed, cannot fork"
            return result

        # The observation and score right after fork_at-th action in original
        target_obs = observations[actual_fork_at]
        target_score = scores[actual_fork_at]

        # Pick a candidate action: the action taken at fork_at+1 if available
        if actual_fork_at + 1 < actual_steps:
            candidate = action_history[actual_fork_at + 1]
            expected_obs = observations[actual_fork_at + 1]
            expected_score = scores[actual_fork_at + 1]
        else:
            candidate = action_history[actual_fork_at]
            expected_obs = observations[actual_fork_at]
            expected_score = scores[actual_fork_at]

        # Fork: replay first fork_at+1 actions, then execute candidate
        fork_history = action_history[: actual_fork_at + 1]

        mem_before_fork = get_memory_mb()
        fork_result = fork_and_lookahead(
            task_name, variation_idx, fork_history, candidate
        )
        mem_after_fork = get_memory_mb()

        result["fork_latency_s"] = fork_result["elapsed_seconds"]
        result["fork_replay_success"] = fork_result["replay_success"]
        result["fork_replay_errors"] = fork_result["replay_errors"]
        result["mem_after_mb"] = mem_after_fork
        result["mem_delta_mb"] = mem_after_fork - mem_before_fork

        # Check observation match (fuzzy: first 200 chars)
        fork_obs = fork_result["observation"]
        obs_match = fork_obs.strip()[:200] == expected_obs.strip()[:200]
        score_match = abs(fork_result["score"] - expected_score) < 0.01

        result["obs_match"] = obs_match
        result["score_match"] = score_match
        result["fork_success"] = fork_result["replay_success"] and (obs_match or score_match)
        result["fork_score"] = fork_result["score"]
        result["expected_score"] = expected_score

    except Exception as e:
        result["error"] = str(e)
    finally:
        if env is not None:
            close_env(env)
        result["mem_after_mb"] = get_memory_mb()

    return result


def resolve_task_names(configured_tasks: Dict[str, List[int]]) -> Dict[str, List[int]]:
    """Resolve configured task names against actual ScienceWorld task names.

    Tries exact match first, then substring match.
    """
    try:
        available = get_task_types()
    except Exception as e:
        print(f"[WARN] Cannot get task names from ScienceWorld: {e}")
        print("[WARN] Using configured task names as-is")
        return configured_tasks

    print(f"Available ScienceWorld tasks ({len(available)}):")
    for t in available:
        print(f"  - {t}")
    print()

    resolved = {}
    for cfg_name, variations in configured_tasks.items():
        if cfg_name in available:
            resolved[cfg_name] = variations
        else:
            # Substring match
            matches = [t for t in available if cfg_name.lower() in t.lower()]
            if len(matches) == 1:
                print(f"[RESOLVE] '{cfg_name}' -> '{matches[0]}'")
                resolved[matches[0]] = variations
            elif len(matches) > 1:
                print(f"[RESOLVE] '{cfg_name}' has multiple matches: {matches}, using first")
                resolved[matches[0]] = variations
            else:
                print(f"[WARN] '{cfg_name}' not found in ScienceWorld, skipping")

    return resolved


def main():
    parser = argparse.ArgumentParser(description="Phase 0: Validate ScienceWorld state forking")
    parser.add_argument("--num_steps", type=int, default=10, help="Steps per variation")
    parser.add_argument("--fork_at", type=int, default=5, help="Step index to fork at")
    parser.add_argument("--output", type=str, default=None, help="Output JSON path")
    args = parser.parse_args()

    print("=" * 60)
    print("Phase 0: ScienceWorld State Forking Validation")
    print("=" * 60)

    tasks = resolve_task_names(PHASE0_TASKS)
    if not tasks:
        print("ERROR: No valid task types found. Aborting.")
        sys.exit(1)

    all_results = []
    for task_name, variations in tasks.items():
        print(f"\n--- Task: {task_name} ---")
        for var_idx in variations:
            print(f"  Variation {var_idx}: ", end="", flush=True)
            r = validate_one_variation(task_name, var_idx, args.num_steps, args.fork_at)
            status = "OK" if r["fork_success"] else "FAIL"
            latency = f"{r['fork_latency_s']:.2f}s" if r['fork_latency_s'] else "N/A"
            print(f"{status} | latency={latency} | obs_match={r['obs_match']} | score_match={r['score_match']}")
            if r.get("error"):
                print(f"    Error: {r['error']}")
            all_results.append(r)

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    total = len(all_results)
    successes = sum(1 for r in all_results if r["fork_success"])
    success_rate = successes / total if total > 0 else 0

    latencies = [r["fork_latency_s"] for r in all_results if r["fork_latency_s"] is not None]
    if latencies:
        latencies_sorted = sorted(latencies)
        avg_lat = sum(latencies) / len(latencies)
        p50_lat = latencies_sorted[len(latencies_sorted) // 2]
        p95_idx = min(int(len(latencies_sorted) * 0.95), len(latencies_sorted) - 1)
        p95_lat = latencies_sorted[p95_idx]
    else:
        avg_lat = p50_lat = p95_lat = float("nan")

    mem_values = [r.get("mem_after_mb", 0) for r in all_results]
    max_mem = max(mem_values) if mem_values else 0

    print(f"Fork success rate: {successes}/{total} = {success_rate:.1%}  {'PASS' if success_rate >= 0.8 else 'FAIL'} (gate: >=80%)")
    print(f"Fork latency — avg: {avg_lat:.2f}s | p50: {p50_lat:.2f}s | p95: {p95_lat:.2f}s  {'PASS' if p95_lat < 5.0 else 'FAIL'} (gate: p95<5s)")
    print(f"Max memory: {max_mem:.0f} MB")

    # Per-task breakdown
    print(f"\nPer-task breakdown:")
    by_task = defaultdict(list)
    for r in all_results:
        by_task[r["task_name"]].append(r)
    for tn, results in by_task.items():
        n_ok = sum(1 for r in results if r["fork_success"])
        lats = [r["fork_latency_s"] for r in results if r["fork_latency_s"] is not None]
        avg = sum(lats) / len(lats) if lats else 0
        print(f"  {tn}: {n_ok}/{len(results)} success, avg latency {avg:.2f}s")

    # Overall gate
    gate_pass = success_rate >= 0.8 and (len(latencies) == 0 or p95_lat < 5.0)
    print(f"\n{'=' * 60}")
    print(f"PHASE 0 GATE: {'PASS' if gate_pass else 'FAIL'}")
    print(f"{'=' * 60}")

    # Save results
    output_path = args.output or "results/phase0_validation.json"
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    summary = {
        "total_variations": total,
        "fork_success_rate": success_rate,
        "avg_latency_s": avg_lat,
        "p50_latency_s": p50_lat,
        "p95_latency_s": p95_lat,
        "max_memory_mb": max_mem,
        "gate_pass": gate_pass,
        "details": all_results,
    }
    with open(output_path, "w") as f:
        json.dump(summary, f, indent=2, default=str)
    print(f"\nResults saved to {output_path}")


if __name__ == "__main__":
    main()
