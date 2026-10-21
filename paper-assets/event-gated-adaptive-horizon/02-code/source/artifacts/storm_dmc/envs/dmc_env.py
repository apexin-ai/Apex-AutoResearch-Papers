"""
DMC Walker Walk gymnasium-compatible wrapper for STORM.

Wraps dm_control's Walker Walk task to provide:
- 24-dim proprioceptive observation (orientations + height + velocity)
- 6-dim continuous action in [-1, 1]
- Standard gymnasium.Env interface for compatibility with STORM's vectorized training loop
"""
import numpy as np
import gymnasium
from gymnasium import spaces


class DMCWalkerWalkEnv(gymnasium.Env):
    """Gymnasium wrapper around dm_control Walker Walk (proprioceptive)."""

    metadata = {"render_modes": ["rgb_array"]}

    def __init__(self, domain="walker", task="walk", seed=None, render_mode=None):
        super().__init__()
        from dm_control import suite
        task_kwargs = {"random": seed} if seed is not None else {}
        self._env = suite.load(domain, task, task_kwargs=task_kwargs)

        # Determine observation and action dimensions
        obs_spec = self._env.observation_spec()
        self._obs_keys = list(obs_spec.keys())
        self._obs_dim = sum(v.shape[0] for v in obs_spec.values())

        action_spec = self._env.action_spec()
        self._action_dim = action_spec.shape[0]

        self.observation_space = spaces.Box(
            low=-np.inf, high=np.inf, shape=(self._obs_dim,), dtype=np.float32
        )
        self.action_space = spaces.Box(
            low=action_spec.minimum.astype(np.float32),
            high=action_spec.maximum.astype(np.float32),
            shape=(self._action_dim,),
            dtype=np.float32,
        )
        self.render_mode = render_mode

    def _flatten_obs(self, time_step):
        parts = [time_step.observation[k].astype(np.float32).flatten() for k in self._obs_keys]
        return np.concatenate(parts)

    def reset(self, *, seed=None, options=None):
        if seed is not None:
            from dm_control import suite
            task_kwargs = {"random": seed}
            domain, task = "walker", "walk"
            self._env = suite.load(domain, task, task_kwargs=task_kwargs)
        time_step = self._env.reset()
        obs = self._flatten_obs(time_step)
        return obs, {}

    def step(self, action):
        action = np.clip(action, -1.0, 1.0).astype(np.float64)
        time_step = self._env.step(action)
        obs = self._flatten_obs(time_step)
        reward = float(time_step.reward or 0.0)
        # discount==0 means true task failure; time-limit truncation has discount>0
        terminated = time_step.last() and float(time_step.discount) == 0.0
        truncated = time_step.last() and not terminated
        return obs, reward, terminated, truncated, {}

    def render(self):
        if self.render_mode == "rgb_array":
            return self._env.physics.render(height=64, width=64, camera_id=0)
        return None


def build_single_dmc_env(domain="walker", task="walk", seed=None):
    return DMCWalkerWalkEnv(domain=domain, task=task, seed=seed)


def build_dmc_vec_env(domain="walker", task="walk", num_envs=1, seed=0):
    def make_env(s):
        return lambda: build_single_dmc_env(domain, task, seed=s)
    env_fns = [make_env(seed + i) for i in range(num_envs)]
    if num_envs == 1:
        vec_env = gymnasium.vector.SyncVectorEnv(env_fns=env_fns)
    else:
        vec_env = gymnasium.vector.AsyncVectorEnv(env_fns=env_fns)
    return vec_env
