"""ScienceWorld environment utilities: creation, forking via action-replay, episode logging.

Dependencies: scienceworld (pip install scienceworld)
Key constraint: ScienceWorld uses py4j → each env is a separate JVM process.
Fork = new JVM instance + replay all historical actions.
"""

import time
import os
import traceback
from typing import List, Tuple, Optional, Dict, Any

import scienceworld

# ---------------------------------------------------------------------------
# Task type constants — update after running get_task_types() on the server
# ---------------------------------------------------------------------------
STRONG_TASKS = [
    "boil",
    "melt",
    "change-the-state-of-matter-of",
]
MEDIUM_TASKS = [
    "chemistry-mix-paint-secondary-color",
]
WEAK_TASKS = [
    "grow-plant",
]
ALL_MVP_TASKS = STRONG_TASKS + MEDIUM_TASKS + WEAK_TASKS


def get_task_types() -> List[str]:
    """Return all ScienceWorld task type names."""
    env = scienceworld.ScienceWorldEnv("")
    try:
        names = env.get_task_names()
    finally:
        env.close()
    return list(names)


def get_max_variations(task_name: str) -> int:
    """Return the number of available variations for a task type."""
    env = scienceworld.ScienceWorldEnv("")
    try:
        n = env.get_max_variations(task_name)
        return int(n)
    except Exception:
        return 100
    finally:
        env.close()


def create_env(task_name: str, variation_idx: int = 0,
               simplification_str: str = "") -> scienceworld.ScienceWorldEnv:
    """Create and initialize a ScienceWorld environment."""
    env = scienceworld.ScienceWorldEnv(task_name, envStepLimit=100)
    env.load(task_name, variation_idx, simplificationStr=simplification_str)
    return env


def reset_env(env: scienceworld.ScienceWorldEnv) -> Tuple[str, dict]:
    """Reset environment, return (observation, info). Tracks score via info dict."""
    result = env.reset()
    if isinstance(result, tuple):
        obs = str(result[0])
        info = result[1] if len(result) > 1 else {}
    else:
        obs = str(result)
        info = {}
    env._last_score = float(info.get("score", 0))
    return obs, info


def get_valid_actions(env: scienceworld.ScienceWorldEnv) -> List[str]:
    """Get current valid action list."""
    actions = env.get_valid_action_object_combinations()
    if isinstance(actions, list):
        return actions
    return list(actions)


def get_score(env: scienceworld.ScienceWorldEnv) -> float:
    """Get score cached from last step()/reset() info dict."""
    return getattr(env, "_last_score", 0.0)


def step_env(env: scienceworld.ScienceWorldEnv, action: str
             ) -> Tuple[str, float, bool, dict]:
    """Execute action, return (observation, reward, done, info). Updates cached score."""
    result = env.step(action)
    if isinstance(result, tuple) and len(result) >= 3:
        obs = str(result[0])
        reward = float(result[1])
        done = bool(result[2])
        info = result[3] if len(result) > 3 else {}
        env._last_score = float(info.get("score", 0))
        return obs, reward, done, info
    return str(result), 0.0, False, {}


def close_env(env: scienceworld.ScienceWorldEnv) -> None:
    """Safely close environment and release JVM resources."""
    try:
        env.close()
    except Exception:
        pass


# ---------------------------------------------------------------------------
# State forking via action-replay
# ---------------------------------------------------------------------------

def fork_and_lookahead(
    task_name: str,
    variation_idx: int,
    action_history: List[str],
    candidate_action: str,
    simplification_str: str = "",
) -> Dict[str, Any]:
    """Fork environment state and evaluate a candidate action.

    Creates a fresh JVM instance, replays action_history, then executes
    candidate_action. Returns dict with observation, score, score_delta,
    replay_success, and timing info. Always closes the forked env.
    """
    t0 = time.time()
    fork_env = None
    try:
        fork_env = create_env(task_name, variation_idx, simplification_str)
        reset_env(fork_env)

        # Replay history
        replay_ok = True
        replay_errors = []
        score_before_candidate = 0.0
        for i, past_action in enumerate(action_history):
            try:
                step_env(fork_env, past_action)
            except Exception as e:
                replay_ok = False
                replay_errors.append({"step": i, "action": past_action, "error": str(e)})

        score_before_candidate = get_score(fork_env)

        # Execute candidate
        obs, reward, done, info = step_env(fork_env, candidate_action)
        score_after = get_score(fork_env)
        score_delta = score_after - score_before_candidate

        elapsed = time.time() - t0
        return {
            "observation": obs,
            "score": score_after,
            "score_delta": score_delta,
            "score_before": score_before_candidate,
            "reward": reward,
            "done": done,
            "replay_success": replay_ok,
            "replay_errors": replay_errors,
            "elapsed_seconds": elapsed,
        }
    except Exception as e:
        elapsed = time.time() - t0
        return {
            "observation": "",
            "score": 0.0,
            "score_delta": 0.0,
            "score_before": 0.0,
            "reward": 0.0,
            "done": False,
            "replay_success": False,
            "replay_errors": [{"step": -1, "action": "fork_init", "error": str(e)}],
            "elapsed_seconds": elapsed,
        }
    finally:
        if fork_env is not None:
            close_env(fork_env)


def run_episode_with_logging(
    task_name: str,
    variation_idx: int = 0,
    max_steps: int = 100,
    action_selector=None,
    simplification_str: str = "",
) -> Dict[str, Any]:
    """Run a full episode, recording (action, obs, score) at each step.

    Args:
        action_selector: callable(obs, valid_actions, history) -> action string.
            If None, picks first valid action (for testing).

    Returns dict with steps list, final_score, total_time, etc.
    """
    env = create_env(task_name, variation_idx, simplification_str)
    obs, info = reset_env(env)
    initial_score = get_score(env)

    steps = []
    action_history = []
    t0 = time.time()

    for step_idx in range(max_steps):
        valid_actions = get_valid_actions(env)
        if not valid_actions:
            break

        if action_selector is not None:
            action = action_selector(obs, valid_actions, action_history)
        else:
            action = valid_actions[0]

        obs_new, reward, done, step_info = step_env(env, action)
        score = get_score(env)

        steps.append({
            "step": step_idx,
            "action": action,
            "observation": obs_new,
            "score": score,
            "reward": reward,
            "done": done,
        })
        action_history.append(action)
        obs = obs_new

        if done:
            break

    total_time = time.time() - t0
    final_score = get_score(env)
    close_env(env)

    return {
        "task_name": task_name,
        "variation_idx": variation_idx,
        "steps": steps,
        "action_history": action_history,
        "final_score": final_score,
        "initial_score": initial_score,
        "num_steps": len(steps),
        "total_time_seconds": total_time,
    }
