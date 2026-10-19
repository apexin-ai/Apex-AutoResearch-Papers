"""
SmolVLA wrapper for ACR-VLA.

Provides:
  1. obs_features extraction (mean-pooled VLM hidden states, 960D)
  2. K-sample flow-matching generation with shared KV cache
  3. LIBERO data preprocessing (image, language, state → SmolVLA inputs)

Preprocessing follows the official lerobot pipeline:
  - Images: flip H+W → resize_with_pad 512×512 → normalize [-1,1]
  - State: 8D (eef_pos + axisangle + gripper_qpos) → MEAN_STD normalize → pad 32D
  - Action output: unnormalize with MEAN_STD stats
"""
import math
from pathlib import Path

import torch
import torch.nn.functional as F
import numpy as np
from PIL import Image
from torchvision import transforms as T
from safetensors.torch import load_file

from lerobot.policies.smolvla.modeling_smolvla import (
    SmolVLAPolicy,
    VLAFlowMatching,
    make_att_2d_masks,
    resize_with_pad,
)

try:
    from utils import FULL_ACTION_DIM, CORRECTION_DIM
except ImportError:
    from .utils import FULL_ACTION_DIM, CORRECTION_DIM

NORM_EPS = 1e-8


def split_action(action_7d):
    """Split LIBERO 7D action into 6D pose and 1D gripper.

    Works with numpy arrays and torch tensors, including batched inputs.
    """
    return action_7d[..., :CORRECTION_DIM], action_7d[..., CORRECTION_DIM:FULL_ACTION_DIM]


class SmolVLAWrapper:
    """Frozen SmolVLA for obs_features and K-sample generation."""

    def __init__(self, pretrained_path: str = "/root/autodl-tmp/models/smolvla_libero/",
                 device: str = "cuda"):
        self.device = torch.device(device)
        self.policy = SmolVLAPolicy.from_pretrained(pretrained_path)
        self.policy.to(self.device)
        self.policy.eval()
        for p in self.policy.parameters():
            p.requires_grad = False

        self.flow: VLAFlowMatching = self.policy.model
        self.processor = self.flow.vlm_with_expert.processor
        self.tokenizer = self.processor.tokenizer
        self.config = self.policy.config

        self.vlm_hidden_size = self.flow.vlm_with_expert.config.text_config.hidden_size  # 960
        self._to_tensor = T.ToTensor()  # HWC uint8 → CHW float [0,1]

        # Load normalizer stats
        model_dir = Path(pretrained_path)
        pre_stats = load_file(str(model_dir / "policy_preprocessor_step_5_normalizer_processor.safetensors"))
        post_stats = load_file(str(model_dir / "policy_postprocessor_step_0_unnormalizer_processor.safetensors"))

        self.state_mean = pre_stats["observation.state.mean"].to(self.device)  # (8,)
        self.state_std = pre_stats["observation.state.std"].to(self.device)    # (8,)
        self.action_mean = post_stats["action.mean"].to(self.device)           # (7,)
        self.action_std = post_stats["action.std"].to(self.device)             # (7,)

        # Image resize target from config
        self.resize_wh = self.config.resize_imgs_with_padding  # [512, 512]

    def _preprocess_image(self, img_np: np.ndarray) -> torch.Tensor:
        """HWC uint8 numpy → (1, C, H, W) float tensor ready for SmolVLA."""
        img = self._to_tensor(img_np)       # (C, H, W) float [0,1]
        img = img.flip(dims=[-2, -1])       # flip H and W (LIBERO convention)
        img = img.unsqueeze(0).to(self.device)
        if self.resize_wh is not None:
            img = resize_with_pad(img, *self.resize_wh, pad_value=0)
        img = img * 2.0 - 1.0               # [0,1] → [-1,1] for SigLIP
        return img

    def _normalize_state(self, state_raw: torch.Tensor) -> torch.Tensor:
        """MEAN_STD normalize state. state_raw: (..., D) where D <= len(state_mean)."""
        D = state_raw.shape[-1]
        mean = self.state_mean[:D]
        std = self.state_std[:D]
        return (state_raw - mean) / (std + NORM_EPS)

    def _unnormalize_action(self, action_norm: torch.Tensor) -> torch.Tensor:
        """MEAN_STD unnormalize action. action_norm: (..., 7)."""
        return action_norm * self.action_std + self.action_mean

    @torch.no_grad()
    def preprocess_obs(self, agentview_rgb: np.ndarray,
                       task_name: str,
                       robot_state: np.ndarray,
                       eye_in_hand_rgb: np.ndarray | None = None):
        """
        Convert raw LIBERO observation into SmolVLA-ready tensors.

        Args:
            agentview_rgb: (H, W, 3) uint8
            task_name: task description string
            robot_state: (8,) float — eef_pos(3) + eef_axisangle(3) + gripper_qpos(2)
            eye_in_hand_rgb: optional (H, W, 3) uint8
        Returns:
            images: list of (1, C, H, W) float tensors
            img_masks: list of (1,) bool tensors
            lang_tokens: (1, L) long tensor
            lang_masks: (1, L) bool tensor
            state: (1, max_state_dim) float tensor (normalized + padded)
        """
        dev = self.device

        imgs = [self._preprocess_image(agentview_rgb)]
        img_masks = [torch.ones(1, dtype=torch.bool, device=dev)]
        if eye_in_hand_rgb is not None:
            imgs.append(self._preprocess_image(eye_in_hand_rgb))
            img_masks.append(torch.ones(1, dtype=torch.bool, device=dev))

        # lerobot SmolVLANewLineProcessor: append \n to task string
        task_text = task_name if task_name.endswith("\n") else f"{task_name}\n"
        tokens = self.tokenizer(
            task_text,
            return_tensors="pt",
            padding="max_length",
            max_length=self.config.tokenizer_max_length,
            truncation=True,
        )
        lang_tokens = tokens["input_ids"].to(dev)
        lang_masks = tokens["attention_mask"].to(dev).bool()

        state_t = torch.tensor(robot_state, dtype=torch.float32, device=dev)
        state_t = self._normalize_state(state_t)
        state = torch.zeros(1, self.config.max_state_dim, device=dev, dtype=torch.float32)
        state[0, :state_t.shape[0]] = state_t

        return imgs, img_masks, lang_tokens, lang_masks, state

    @torch.no_grad()
    def preprocess_obs_batch(self, batch_obs):
        dev = self.device
        B = len(batch_obs)

        agentview_tensors = torch.cat(
            [self._preprocess_image(s["agentview_rgb"]) for s in batch_obs], dim=0
        )
        imgs = [agentview_tensors]
        img_masks = [torch.ones(B, dtype=torch.bool, device=dev)]

        if batch_obs[0].get("eye_in_hand_rgb") is not None:
            eih_tensors = torch.cat(
                [self._preprocess_image(s["eye_in_hand_rgb"]) for s in batch_obs], dim=0
            )
            imgs.append(eih_tensors)
            img_masks.append(torch.ones(B, dtype=torch.bool, device=dev))

        task_names = [s["task_name"] if s["task_name"].endswith("\n") else f"{s['task_name']}\n"
                     for s in batch_obs]
        tokens = self.tokenizer(
            task_names,
            return_tensors="pt",
            padding="max_length",
            max_length=self.config.tokenizer_max_length,
            truncation=True,
        )
        lang_tokens = tokens["input_ids"].to(dev)
        lang_masks = tokens["attention_mask"].to(dev).bool()

        state = torch.zeros(B, self.config.max_state_dim, device=dev, dtype=torch.float32)
        for i, s in enumerate(batch_obs):
            es = torch.tensor(s["ee_states"], dtype=torch.float32, device=dev)
            es = self._normalize_state(es)
            state[i, :es.shape[0]] = es

        return imgs, img_masks, lang_tokens, lang_masks, state

    @torch.no_grad()
    def encode_prefix(self, images, img_masks, lang_tokens, lang_masks, state):
        """
        Encode observation prefix through VLM, return obs_features and KV cache.

        Returns:
            obs_features: (B, 960)
            past_key_values: KV cache for denoising
            prefix_pad_masks: (B, seq_len) for denoising attention
        """
        prefix_embs, prefix_pad_masks, prefix_att_masks = self.flow.embed_prefix(
            images, img_masks, lang_tokens, lang_masks, state=state
        )
        prefix_att_2d_masks = make_att_2d_masks(prefix_pad_masks, prefix_att_masks)
        prefix_position_ids = torch.cumsum(prefix_pad_masks, dim=1) - 1

        outputs_embeds, past_key_values = self.flow.vlm_with_expert.forward(
            attention_mask=prefix_att_2d_masks,
            position_ids=prefix_position_ids,
            past_key_values=None,
            inputs_embeds=[prefix_embs, None],
            use_cache=self.config.use_cache,
            fill_kv_cache=True,
        )

        vlm_hidden = outputs_embeds[0]  # (B, seq_len, 960)
        mask = prefix_pad_masks.unsqueeze(-1).float()
        obs_features = (vlm_hidden.float() * mask).sum(1) / mask.sum(1).clamp(min=1)

        return obs_features, past_key_values, prefix_pad_masks

    @torch.no_grad()
    def generate_k_samples(self, past_key_values, prefix_pad_masks,
                           K: int = 10) -> torch.Tensor:
        """
        Generate K action samples using cached prefix KV.

        Returns:
            samples: (B, K, chunk_size, FULL_ACTION_DIM) — unnormalized actions
        """
        B = prefix_pad_masks.shape[0]
        chunk_size = self.config.chunk_size
        max_act_dim = self.config.max_action_dim
        num_steps = self.config.num_steps
        dt = -1.0 / num_steps

        all_samples = []
        for _ in range(K):
            noise = self.flow.sample_noise((B, chunk_size, max_act_dim), self.device)
            x_t = noise

            for step in range(num_steps):
                time_val = 1.0 + step * dt
                time_tensor = torch.full((B,), time_val, dtype=torch.float32,
                                         device=self.device)
                v_t = self.flow.denoise_step(
                    x_t=x_t,
                    prefix_pad_masks=prefix_pad_masks,
                    past_key_values=past_key_values,
                    timestep=time_tensor,
                )
                x_t = x_t + dt * v_t

            raw_action = x_t[:, :, :FULL_ACTION_DIM]  # (B, chunk_size, 7)
            unnorm_action = self._unnormalize_action(raw_action)
            all_samples.append(unnorm_action)

        return torch.stack(all_samples, dim=1)  # (B, K, chunk_size, FULL_ACTION_DIM)

    @torch.no_grad()
    def get_obs_features_and_samples(self, agentview_rgb, task_name, robot_state,
                                     eye_in_hand_rgb=None, K=10):
        """
        End-to-end: raw obs → obs_features (960D) + K action samples (7D).

        Returns:
            obs_features: (1, 960)
            samples: (1, K, chunk_size, FULL_ACTION_DIM)
        """
        imgs, img_masks, lt, lm, state = self.preprocess_obs(
            agentview_rgb, task_name, robot_state, eye_in_hand_rgb
        )
        obs_feat, kv_cache, pad_masks = self.encode_prefix(
            imgs, img_masks, lt, lm, state
        )
        samples = self.generate_k_samples(kv_cache, pad_masks, K=K)
        return obs_feat, samples

    @torch.no_grad()
    def get_obs_features_and_samples_batch(self, batch_obs, K=10):
        imgs, img_masks, lt, lm, state = self.preprocess_obs_batch(batch_obs)
        obs_feat, kv_cache, pad_masks = self.encode_prefix(
            imgs, img_masks, lt, lm, state
        )
        samples = self.generate_k_samples(kv_cache, pad_masks, K=K)
        return obs_feat, samples
