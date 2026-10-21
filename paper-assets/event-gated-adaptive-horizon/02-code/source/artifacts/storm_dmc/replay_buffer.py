"""
Replay buffer for continuous observation and action spaces (DMC).

Key changes vs original STORM:
1. obs stored as float32 vectors (not uint8 images)
2. action stored as (max_length, num_envs, action_dim) float32 (not scalar)
3. No /255 normalization or image rearranging during sample()
"""
import numpy as np
import torch
from einops import rearrange


class ReplayBuffer:
    def __init__(self, obs_dim, action_dim, num_envs,
                 max_length=int(1e6), warmup_length=5000, store_on_gpu=False):
        self.store_on_gpu = store_on_gpu
        self.obs_dim = obs_dim
        self.action_dim = action_dim

        buf_len = max_length // num_envs

        if store_on_gpu:
            self.obs_buffer = torch.empty((buf_len, num_envs, obs_dim), dtype=torch.float32, device="cuda")
            self.action_buffer = torch.empty((buf_len, num_envs, action_dim), dtype=torch.float32, device="cuda")
            self.reward_buffer = torch.empty((buf_len, num_envs), dtype=torch.float32, device="cuda")
            self.termination_buffer = torch.empty((buf_len, num_envs), dtype=torch.float32, device="cuda")
        else:
            self.obs_buffer = np.empty((buf_len, num_envs, obs_dim), dtype=np.float32)
            self.action_buffer = np.empty((buf_len, num_envs, action_dim), dtype=np.float32)
            self.reward_buffer = np.empty((buf_len, num_envs), dtype=np.float32)
            self.termination_buffer = np.empty((buf_len, num_envs), dtype=np.float32)

        self.length = 0
        self.num_envs = num_envs
        self.last_pointer = -1
        self.max_length = max_length
        self.warmup_length = warmup_length

    def ready(self):
        return self.length * self.num_envs > self.warmup_length

    @torch.no_grad()
    def sample(self, batch_size, external_batch_size, batch_length, to_device="cuda"):
        """
        Sample a batch of trajectories.
        Returns: obs (B, L, obs_dim), action (B, L, action_dim), reward (B, L), termination (B, L)
        """
        if self.store_on_gpu:
            obs, action, reward, termination = [], [], [], []
            if batch_size > 0:
                for i in range(self.num_envs):
                    indexes = np.random.randint(0, self.length + 1 - batch_length, size=batch_size // self.num_envs)
                    obs.append(torch.stack([self.obs_buffer[idx:idx+batch_length, i] for idx in indexes]))
                    action.append(torch.stack([self.action_buffer[idx:idx+batch_length, i] for idx in indexes]))
                    reward.append(torch.stack([self.reward_buffer[idx:idx+batch_length, i] for idx in indexes]))
                    termination.append(torch.stack([self.termination_buffer[idx:idx+batch_length, i] for idx in indexes]))

            obs = torch.cat(obs, dim=0)         # (B, L, obs_dim)
            action = torch.cat(action, dim=0)   # (B, L, action_dim)
            reward = torch.cat(reward, dim=0)   # (B, L)
            termination = torch.cat(termination, dim=0)  # (B, L)
        else:
            obs, action, reward, termination = [], [], [], []
            if batch_size > 0:
                for i in range(self.num_envs):
                    indexes = np.random.randint(0, self.length + 1 - batch_length, size=batch_size // self.num_envs)
                    obs.append(np.stack([self.obs_buffer[idx:idx+batch_length, i] for idx in indexes]))
                    action.append(np.stack([self.action_buffer[idx:idx+batch_length, i] for idx in indexes]))
                    reward.append(np.stack([self.reward_buffer[idx:idx+batch_length, i] for idx in indexes]))
                    termination.append(np.stack([self.termination_buffer[idx:idx+batch_length, i] for idx in indexes]))

            obs = torch.from_numpy(np.concatenate(obs, axis=0)).float().cuda()
            action = torch.from_numpy(np.concatenate(action, axis=0)).float().cuda()
            reward = torch.from_numpy(np.concatenate(reward, axis=0)).cuda()
            termination = torch.from_numpy(np.concatenate(termination, axis=0)).cuda()

        return obs, action, reward, termination

    def append(self, obs, action, reward, termination):
        """
        Append a single transition from vectorized env.
        obs: (num_envs, obs_dim), action: (num_envs, action_dim),
        reward: (num_envs,), termination: (num_envs,)
        """
        self.last_pointer = (self.last_pointer + 1) % (self.max_length // self.num_envs)
        if self.store_on_gpu:
            self.obs_buffer[self.last_pointer] = torch.from_numpy(obs).float()
            self.action_buffer[self.last_pointer] = torch.from_numpy(action).float()
            self.reward_buffer[self.last_pointer] = torch.from_numpy(reward).float()
            self.termination_buffer[self.last_pointer] = torch.from_numpy(termination).float()
        else:
            self.obs_buffer[self.last_pointer] = obs
            self.action_buffer[self.last_pointer] = action
            self.reward_buffer[self.last_pointer] = reward
            self.termination_buffer[self.last_pointer] = termination

        if self.length < self.max_length // self.num_envs:
            self.length += 1

    def __len__(self):
        return self.length * self.num_envs
