"""ManiSkill3 env wrapper for DreamerV3 (event-gated-adaptive-horizon).

Adapts ManiSkill3 gymnasium envs to the DreamerV3 env interface used by
DeepMindControl, Atari, etc. in this codebase.

DreamerV3 expects:
  - obs dict with 'is_first', 'is_terminal', and optionally 'image'
  - step() returns (obs, reward, done, info)
  - reset() returns obs
  - obs values are numpy arrays (no batch dim)
  - action_space and observation_space are gym.spaces

ManiSkill3 returns:
  - obs_mode="state" gives a flat torch.Tensor with shape (1, obs_dim)
  - rewards/terminated/truncated are torch.Tensor with shape (1,)
  - action_space is Box(-1, 1, (act_dim,))
"""

import os

import gym
import gymnasium
import numpy as np
import torch

import mani_skill.envs  # noqa: F401 - registers envs

def _parse_cuda_index(device_str):
    s = str(device_str) if device_str is not None else ""
    if s.startswith("cuda:"):
        return int(s.split(":")[1])
    return 0


def resolve_physical_device(device):
    """Remove CUDA_VISIBLE_DEVICES and remap device to physical GPU index.

    SAPIEN segfaults when CVD remaps GPU indices. Call this once before any
    ManiSkill env creation so that both SAPIEN and torch share the same
    physical device.
    """
    cvd = os.environ.pop("CUDA_VISIBLE_DEVICES", None)
    logical_idx = _parse_cuda_index(device)
    if cvd is not None:
        physical_gpus = [x.strip() for x in cvd.split(",")]
        physical_idx = int(physical_gpus[logical_idx])
    else:
        physical_idx = logical_idx
    resolved = f"cuda:{physical_idx}"
    print(f"[ManiSkill GPU] CVD={cvd!r}, requested={device}, resolved={resolved}")
    return resolved


def _to_np(x):
    if isinstance(x, torch.Tensor):
        return x.detach().cpu().numpy()
    return np.asarray(x)


class ManiSkill:
    """DreamerV3-compatible wrapper for ManiSkill3 state-based envs."""

    metadata = {}

    def __init__(
        self,
        task,
        action_repeat=1,
        size=(64, 64),
        obs_mode="state",
        max_episode_steps=200,
        seed=0,
    ):
        self._task = task
        self._action_repeat = action_repeat
        self._size = size
        self._obs_mode = obs_mode
        self._use_image = obs_mode in ("rgbd", "rgb")

        # Safety net: resolve_physical_device() should have already
        # removed CVD, but clear it if somehow still present.
        os.environ.pop("CUDA_VISIBLE_DEVICES", None)

        make_kwargs = dict(
            obs_mode=obs_mode,
            max_episode_steps=max_episode_steps,
            render_mode="rgb_array" if self._use_image else None,
        )
        if not self._use_image:
            make_kwargs["render_backend"] = "cpu"

        self._env = gymnasium.make(task, **make_kwargs)
        self._env.reset(seed=seed)

        # Cache obs dim from a probe reset
        probe_obs, _ = self._env.reset()
        self._obs_dim = self._flatten_obs(probe_obs).shape[0]
        self.reward_range = [-np.inf, np.inf]

    def _flatten_obs(self, obs):
        """Convert ManiSkill obs to a flat numpy vector (no batch dim)."""
        if isinstance(obs, (torch.Tensor, np.ndarray)):
            arr = _to_np(obs)
            if arr.ndim == 2 and arr.shape[0] == 1:
                arr = arr[0]
            return arr.astype(np.float32)
        elif isinstance(obs, dict):
            parts = []
            for v in obs.values():
                parts.append(self._flatten_obs(v))
            return np.concatenate(parts, axis=-1).astype(np.float32)
        else:
            return np.array([obs], dtype=np.float32)

    @property
    def observation_space(self):
        spaces = {}
        spaces["state"] = gym.spaces.Box(
            -np.inf, np.inf, (self._obs_dim,), dtype=np.float32
        )
        if self._use_image:
            spaces["image"] = gym.spaces.Box(
                0, 255, self._size + (3,), dtype=np.uint8
            )
        return gym.spaces.Dict(spaces)

    @property
    def action_space(self):
        ms_space = self._env.action_space
        return gym.spaces.Box(
            ms_space.low, ms_space.high, dtype=np.float32
        )

    @property
    def act_space(self):
        return {"action": self.action_space}

    @property
    def obs_space(self):
        return self.observation_space.spaces

    def step(self, action):
        assert np.isfinite(action).all(), action
        reward = 0.0
        terminated = False
        truncated = False
        for _ in range(self._action_repeat):
            obs_raw, rew, term, trunc, info = self._env.step(action)
            r = _to_np(rew).item() if isinstance(rew, torch.Tensor) else float(rew)
            reward += r
            terminated = _to_np(term).item() if isinstance(term, torch.Tensor) else bool(term)
            truncated = _to_np(trunc).item() if isinstance(trunc, torch.Tensor) else bool(trunc)
            if terminated or truncated:
                break

        obs = self._build_obs(obs_raw, is_first=False, is_terminal=terminated)
        done = terminated or truncated
        discount = 0.0 if terminated else 1.0
        info["discount"] = np.array(discount, np.float32)
        return obs, reward, done, info

    def reset(self):
        obs_raw, _info = self._env.reset()
        return self._build_obs(obs_raw, is_first=True, is_terminal=False)

    def _build_obs(self, obs_raw, is_first, is_terminal):
        obs = {}
        obs["state"] = self._flatten_obs(obs_raw)
        if self._use_image:
            obs["image"] = self._render_image()
        obs["is_first"] = is_first
        obs["is_terminal"] = is_terminal
        return obs

    def _render_image(self):
        frame = self._env.render()
        frame = _to_np(frame)
        if frame.ndim == 4 and frame.shape[0] == 1:
            frame = frame[0]
        if frame.shape[:2] != self._size:
            from PIL import Image
            img = Image.fromarray(frame)
            img = img.resize((self._size[1], self._size[0]), Image.BILINEAR)
            frame = np.array(img)
        return frame

    def close(self):
        self._env.close()
