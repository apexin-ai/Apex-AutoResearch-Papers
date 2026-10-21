#!/usr/bin/env python3
"""
MiniHack Episode Runner
Runs episodes with deterministic (heuristic) or internal (LLM) agents.
Outputs JSONL compatible with ScienceWorld episode_summary format.

Usage:
  python minihack_episode_runner.py --strategy deterministic --task MiniHack-Room-5x5-v0 --episodes 50
  python minihack_episode_runner.py --strategy internal --task MiniHack-Room-5x5-v0 --episodes 50
"""

import argparse
import json
import os
import sys
import time
from typing import Dict, List, Optional

try:
    import gymnasium as gym
except ImportError:
    import gym

from minihack_det_agent import (
    DeterministicHeuristicAgent,
    OBS_KEYS,
    TASK_TYPES,
    _env_reset,
    _env_step,
)


# ------------------------------------------------------------------ #
#  Agent interface                                                    #
# ------------------------------------------------------------------ #

class BaseAgent:
    def reset(self):
        raise NotImplementedError

    def act(self, obs: Dict) -> int:
        raise NotImplementedError


class RandomAgent(BaseAgent):
    """Uniform random baseline."""

    def __init__(self, env):
        self.n = env.action_space.n

    def reset(self):
        pass

    def act(self, obs: Dict) -> int:
        import random
        return random.randint(0, self.n - 1)


class LLMAgent(BaseAgent):
    """Placeholder for LLM-based (always-internal) agent.

    Integration path:
      1. Use BALROG framework with nle-language-wrapper for text observations.
      2. Plug in vLLM-served model (e.g. Qwen2.5-7B-Instruct).
      3. The act() method sends text observation to LLM and parses action.
    """

    def __init__(self, env, model_name: str = "Qwen/Qwen2.5-7B-Instruct", **kwargs):
        self.env = env
        self.model_name = model_name
        self.history: List[Dict] = []

    def reset(self):
        self.history.clear()

    def act(self, obs: Dict) -> int:
        raise NotImplementedError(
            "LLM agent not yet implemented. "
            "Integrate BALROG or nle-language-wrapper + vLLM to enable."
        )


# ------------------------------------------------------------------ #
#  Episode runner                                                     #
# ------------------------------------------------------------------ #

def run_episode(
    env, agent: BaseAgent, seed: int, max_steps: int = 500
) -> Dict:
    """Run one episode. Returns result dict (ScienceWorld-compatible fields)."""
    obs = _env_reset(env, seed=seed)
    agent.reset()

    total_reward = 0.0
    actions: List[int] = []
    t0 = time.time()

    for _ in range(max_steps):
        action = agent.act(obs)
        actions.append(int(action))
        obs, reward, done, info = _env_step(env, action)
        total_reward += reward
        if done:
            break

    elapsed = time.time() - t0
    end_status = info.get("end_status", -1) if isinstance(info, dict) else -1
    died = total_reward < 0 or end_status == 1
    goal_reached = total_reward > 0 or end_status in (4, 5)

    return {
        "score": float(total_reward),
        "died": bool(died),
        "goal_reached": bool(goal_reached),
        "steps": len(actions),
        "wall_time_s": round(elapsed, 2),
    }


def run_batch(
    task: str,
    strategy: str,
    n_episodes: int,
    base_seed: int,
    max_steps: int,
    output_path: Optional[str] = None,
) -> List[Dict]:
    """Run a batch of episodes, write JSONL, return results."""
    import minihack  # noqa: F401

    env = gym.make(task, observation_keys=OBS_KEYS)

    if strategy == "deterministic":
        agent = DeterministicHeuristicAgent(env)
    elif strategy == "random":
        agent = RandomAgent(env)
    elif strategy == "internal":
        agent = LLMAgent(env)
    else:
        raise ValueError(f"Unknown strategy: {strategy}")

    results = []
    for ep in range(n_episodes):
        seed = base_seed + ep
        result = run_episode(env, agent, seed=seed, max_steps=max_steps)
        result.update({
            "episode_id": ep,
            "task": task,
            "strategy": strategy,
            "seed": seed,
        })
        results.append(result)

        status = "DIED" if result["died"] else ("GOAL" if result["goal_reached"] else "TIMEOUT")
        print(f"  [{strategy}] ep={ep:3d}  seed={seed}  steps={result['steps']:4d}  "
              f"score={result['score']:+.1f}  {status}  ({result['wall_time_s']:.1f}s)")

    env.close()

    if output_path:
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        with open(output_path, "a") as f:
            for r in results:
                f.write(json.dumps(r) + "\n")
        print(f"Appended {len(results)} episodes to {output_path}")

    return results


# ------------------------------------------------------------------ #
#  Summary                                                            #
# ------------------------------------------------------------------ #

def print_summary(results: List[Dict]):
    from collections import defaultdict

    by_key = defaultdict(list)
    for r in results:
        key = (r["task"], r["strategy"])
        by_key[key].append(r)

    print("\n" + "=" * 70)
    print(f"{'Task':<35s} {'Strategy':<15s} {'Episodes':>8s} {'Wins':>6s} {'Deaths':>7s} {'Avg Steps':>10s}")
    print("-" * 70)
    for (task, strat), rlist in sorted(by_key.items()):
        n = len(rlist)
        wins = sum(1 for r in rlist if r["goal_reached"])
        deaths = sum(1 for r in rlist if r["died"])
        avg_steps = sum(r["steps"] for r in rlist) / n
        print(f"{task:<35s} {strat:<15s} {n:>8d} {wins:>6d} {deaths:>7d} {avg_steps:>10.1f}")
    print("=" * 70)


# ------------------------------------------------------------------ #
#  CLI                                                                #
# ------------------------------------------------------------------ #

def main():
    parser = argparse.ArgumentParser(
        description="MiniHack episode runner for counterfactual analysis"
    )
    parser.add_argument(
        "--task", default="MiniHack-Room-5x5-v0",
        help=f"MiniHack task ID. Known tasks: {', '.join(TASK_TYPES)}"
    )
    parser.add_argument(
        "--strategy", default="deterministic",
        choices=["deterministic", "internal", "random"],
        help="Agent strategy"
    )
    parser.add_argument("--episodes", type=int, default=50)
    parser.add_argument("--seed", type=int, default=42, help="Base random seed")
    parser.add_argument("--max-steps", type=int, default=500)
    parser.add_argument(
        "--output", default=None,
        help="JSONL output path (appends). Default: episode_summary_{task}_{strategy}.jsonl"
    )
    parser.add_argument(
        "--tasks-all", action="store_true",
        help="Run across all known task types"
    )
    args = parser.parse_args()

    tasks = TASK_TYPES if args.tasks_all else [args.task]
    output = args.output

    all_results = []
    for task in tasks:
        if output is None:
            safe_name = task.replace("/", "_")
            out = f"episode_summary_{safe_name}_{args.strategy}.jsonl"
        else:
            out = output
        print(f"\n>>> {task} | strategy={args.strategy} | episodes={args.episodes} | seed={args.seed}")
        results = run_batch(
            task=task,
            strategy=args.strategy,
            n_episodes=args.episodes,
            base_seed=args.seed,
            max_steps=args.max_steps,
            output_path=out,
        )
        all_results.extend(results)

    print_summary(all_results)


if __name__ == "__main__":
    main()
