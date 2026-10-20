"""ScienceWorld environment utilities: creation, forking via action-replay, episode logging.

Dependencies: scienceworld (pip install scienceworld)
Key constraint: ScienceWorld uses py4j; each env is a separate JVM process.
Fork = new JVM instance + replay all historical actions.
"""

import time
import os
import traceback
from typing import List, Tuple, Optional, Dict, Any

import scienceworld


def get_task_types() -> List[str]:
    env = scienceworld.ScienceWorldEnv("")
    try:
        names = env.get_task_names()
    finally:
        env.close()
    return list(names)


def get_max_variations(task_name: str) -> int:
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
    env = scienceworld.ScienceWorldEnv(task_name, envStepLimit=100)
    env.load(task_name, variation_idx, simplificationStr=simplification_str)
    return env


def reset_env(env: scienceworld.ScienceWorldEnv) -> str:
    obs, info = env.reset()
    return obs


def get_valid_actions(env: scienceworld.ScienceWorldEnv) -> List[str]:
    return list(env.get_valid_action_object_combinations())


def get_score(env: scienceworld.ScienceWorldEnv) -> float:
    return env.get_score()


def step_env(env: scienceworld.ScienceWorldEnv, action: str) -> Tuple[str, float, bool, dict]:
    obs, reward, done, info = env.step(action)
    return obs, reward, done, info


def close_env(env: scienceworld.ScienceWorldEnv):
    try:
        env.close()
    except Exception:
        pass


def fork_and_lookahead(
    task_name: str,
    variation_idx: int,
    action_history: List[str],
    new_action: str,
    steps: int = 1,
    simplification_str: str = "",
) -> Dict[str, Any]:
    """Fork environment by replaying action history, then take new_action and
    continue for `steps` steps with a random valid action policy.

    Returns dict with score, done, n_steps."""
    fork_env = create_env(task_name, variation_idx, simplification_str)
    reset_env(fork_env)

    for past_action in action_history:
        try:
            fork_env.step(past_action)
        except Exception:
            close_env(fork_env)
            return {"score": -100, "done": True, "n_steps": 0, "error": "replay_fail"}

    try:
        obs, reward, done, info = fork_env.step(new_action)
    except Exception:
        close_env(fork_env)
        return {"score": -100, "done": True, "n_steps": 0, "error": "action_fail"}

    if done:
        score = get_score(fork_env)
        close_env(fork_env)
        return {"score": score, "done": True, "n_steps": 1}

    import random
    for s in range(steps - 1):
        valid = get_valid_actions(fork_env)
        if not valid:
            break
        act = random.choice(valid)
        obs, reward, done, info = fork_env.step(act)
        if done:
            break

    score = get_score(fork_env)
    close_env(fork_env)
    return {"score": score, "done": done, "n_steps": s + 2 if steps > 1 else 1}
