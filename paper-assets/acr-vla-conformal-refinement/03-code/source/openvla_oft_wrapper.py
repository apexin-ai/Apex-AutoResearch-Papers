"""
OpenVLA-OFT wrapper for ACR-VLA.

OpenVLA-OFT is a 7B VLA that uses L1 regression (deterministic, not flow matching).
Loaded via HF AutoModelForVision2Seq with trust_remote_code; ActionHead and
ProprioProjector are loaded separately from .pt checkpoints in the model dir.

This wrapper avoids importing experiments.robot.openvla_utils (which pulls
tensorflow / dlimp). We reimplement the small set of helpers we actually need.

Inference contract (matches Pi05Wrapper / SmolVLAWrapper):
  - get_obs_features_and_samples(...) -> (obs_feat, samples)
      obs_feat: (1, llm_dim) — mean-pooled action-token hidden states
      samples: (1, K, chunk_size, FULL_ACTION_DIM)
  - predict_action(...) -> (FULL_ACTION_DIM,) numpy; replays a cached chunk
  - reset_action_queue() — call at env.reset

OpenVLA-OFT specifics:
  - Deterministic L1 regression (no inherent stochasticity)
  - 2 image inputs (third-person + wrist) at 224x224
  - 8D proprio state (eef_pos[3] + eef_axisangle[3] + gripper_qpos[2])
  - chunk_size = 8 (NUM_ACTIONS_CHUNK)
  - LIBERO obs images need 180° rotation (img[::-1, ::-1])
"""
import json
import os
import sys
from collections import deque
from pathlib import Path
from typing import Any, Dict, Optional

import numpy as np
import torch
from PIL import Image

try:
    from utils import FULL_ACTION_DIM, CORRECTION_DIM
except ImportError:
    from .utils import FULL_ACTION_DIM, CORRECTION_DIM


OFT_CODE_PATH = "/root/openvla-oft-code"
NUM_ACTIONS_CHUNK = 8
ACTION_DIM = 7
PROPRIO_DIM = 8
OPENVLA_IMAGE_SIZE = 224


def _ensure_oft_on_path():
    """Add openvla-oft code to sys.path so prismatic.* and trust_remote_code work."""
    if OFT_CODE_PATH not in sys.path:
        sys.path.insert(0, OFT_CODE_PATH)


def _resize_pil(img: np.ndarray, size: int = OPENVLA_IMAGE_SIZE) -> np.ndarray:
    """Lanczos resize (replaces TF lanczos3 — close enough for inference)."""
    if img.shape[0] == size and img.shape[1] == size:
        return img
    pil = Image.fromarray(img.astype(np.uint8))
    pil = pil.resize((size, size), Image.LANCZOS)
    return np.array(pil)


def _center_crop_resize_pil(img: np.ndarray, crop_scale: float = 0.9,
                             size: int = OPENVLA_IMAGE_SIZE) -> Image.Image:
    """OFT-style center crop (scale=0.9 by linear side ratio) then resize back."""
    h, w = img.shape[:2]
    side = (crop_scale ** 0.5)
    new_h = int(round(h * side))
    new_w = int(round(w * side))
    top = (h - new_h) // 2
    left = (w - new_w) // 2
    cropped = img[top:top + new_h, left:left + new_w]
    pil = Image.fromarray(cropped.astype(np.uint8))
    pil = pil.resize((size, size), Image.BILINEAR)
    return pil.convert("RGB")


def _normalize_proprio(proprio: np.ndarray, stats: Dict[str, Any]) -> np.ndarray:
    """Bounds_q99 normalization (LIBERO default). See OFT openvla_utils.normalize_proprio."""
    mask = np.asarray(stats.get("mask", np.ones_like(stats["q01"], dtype=bool)))
    hi = np.asarray(stats["q99"])
    lo = np.asarray(stats["q01"])
    proprio = np.asarray(proprio, dtype=np.float64)
    normalized = np.where(
        mask,
        2 * (proprio - lo) / (hi - lo + 1e-8) - 1,
        proprio,
    )
    return normalized


def _load_state_dict_robust(ckpt_path: str) -> Dict[str, torch.Tensor]:
    """Load checkpoint. OFT saves keys with a `module.` prefix (DDP) and
    sometimes wraps the dict under 'model_state_dict'. Handle both."""
    sd = torch.load(ckpt_path, map_location="cpu", weights_only=True)
    if isinstance(sd, dict) and "model_state_dict" in sd:
        sd = sd["model_state_dict"]
    if any(k.startswith("module.") for k in sd.keys()):
        sd = {k[len("module."):] if k.startswith("module.") else k: v
              for k, v in sd.items()}
    return sd


def _register_openvla_hf_classes():
    """Register OpenVLA custom classes with HF Auto Classes (idempotent).
    transformers 5.x removed AutoModelForVision2Seq — we skip the Vision2Seq
    registration and rely on direct instantiation of OpenVLAForActionPrediction.
    """
    _ensure_oft_on_path()
    from transformers import AutoConfig, AutoImageProcessor, AutoProcessor
    from prismatic.extern.hf.configuration_prismatic import OpenVLAConfig
    from prismatic.extern.hf.processing_prismatic import (
        PrismaticImageProcessor, PrismaticProcessor,
    )
    try:
        AutoConfig.register("openvla", OpenVLAConfig)
    except (ValueError, KeyError):
        pass
    try:
        AutoImageProcessor.register(OpenVLAConfig, PrismaticImageProcessor)
    except (ValueError, KeyError):
        pass
    try:
        AutoProcessor.register(OpenVLAConfig, PrismaticProcessor)
    except (ValueError, KeyError):
        pass


class OpenVLAOFTWrapper:
    """Frozen OpenVLA-OFT for L1-regression action chunk prediction on LIBERO."""

    LLM_HIDDEN_SIZE = 4096

    def __init__(self,
                 pretrained_path: str = "/root/autodl-tmp/models/openvla-oft/object",
                 unnorm_key: str = "libero_object_no_noops",
                 device: str = "cuda",
                 num_images_in_input: int = 2,
                 use_proprio: bool = True,
                 center_crop: bool = True):
        _ensure_oft_on_path()
        self.device = torch.device(device)
        self.pretrained_path = pretrained_path
        self.unnorm_key = unnorm_key
        self.num_images_in_input = num_images_in_input
        self.use_proprio = use_proprio
        self.center_crop = center_crop
        self._action_queue = deque()

        print(f"[OFT] Loading VLA from {pretrained_path}...", flush=True)
        self._load_vla()
        print(f"[OFT] Loading ActionHead + ProprioProjector...", flush=True)
        self._load_action_head()
        if use_proprio:
            self._load_proprio_projector()
        else:
            self.proprio_projector = None
        self._load_norm_stats()

        assert unnorm_key in self.vla.norm_stats, (
            f"unnorm_key '{unnorm_key}' not in norm_stats keys: "
            f"{list(self.vla.norm_stats.keys())}"
        )

        self.vlm_hidden_size = self.vla.llm_dim
        self.action_chunk_size = NUM_ACTIONS_CHUNK
        self.action_dim = ACTION_DIM
        print(f"[OFT] Ready. llm_dim={self.vla.llm_dim}, "
              f"chunk_size={NUM_ACTIONS_CHUNK}, unnorm_key={unnorm_key}", flush=True)

    def _load_vla(self):
        _register_openvla_hf_classes()
        # Direct instantiation (transformers 5.x removed AutoModelForVision2Seq).
        from prismatic.extern.hf.modeling_prismatic import OpenVLAForActionPrediction
        self.vla = OpenVLAForActionPrediction.from_pretrained(
            self.pretrained_path,
            torch_dtype=torch.bfloat16,
            low_cpu_mem_usage=True,
            trust_remote_code=True,
        )
        self.vla.vision_backbone.set_num_images_in_input(self.num_images_in_input)
        self.vla.eval()
        self.vla = self.vla.to(self.device)
        for p in self.vla.parameters():
            p.requires_grad = False

        from transformers import AutoProcessor
        self.processor = AutoProcessor.from_pretrained(
            self.pretrained_path, trust_remote_code=True
        )

    def _load_action_head(self):
        from prismatic.models.action_heads import L1RegressionActionHead
        action_head = L1RegressionActionHead(
            input_dim=self.vla.llm_dim,
            hidden_dim=self.vla.llm_dim,
            action_dim=ACTION_DIM,
        )
        action_head = action_head.to(torch.bfloat16).to(self.device)
        action_head.eval()
        ckpt_path = self._find_checkpoint("action_head")
        sd = _load_state_dict_robust(ckpt_path)
        action_head.load_state_dict(sd)
        for p in action_head.parameters():
            p.requires_grad = False
        self.action_head = action_head

    def _load_proprio_projector(self):
        from prismatic.models.projectors import ProprioProjector
        pp = ProprioProjector(llm_dim=self.vla.llm_dim, proprio_dim=PROPRIO_DIM)
        pp = pp.to(torch.bfloat16).to(self.device)
        pp.eval()
        ckpt_path = self._find_checkpoint("proprio_projector")
        sd = _load_state_dict_robust(ckpt_path)
        pp.load_state_dict(sd)
        for p in pp.parameters():
            p.requires_grad = False
        self.proprio_projector = pp

    def _find_checkpoint(self, name: str) -> str:
        """Find checkpoint file like 'action_head--150000_checkpoint.pt' in model dir."""
        for f in sorted(Path(self.pretrained_path).iterdir()):
            if f.name.startswith(name) and f.suffix == ".pt":
                return str(f)
        raise FileNotFoundError(
            f"No {name}--*_checkpoint.pt under {self.pretrained_path}"
        )

    def _load_norm_stats(self):
        p = Path(self.pretrained_path) / "dataset_statistics.json"
        with open(p) as f:
            self.vla.norm_stats = json.load(f)

    @staticmethod
    def _libero_rotate(img: np.ndarray) -> np.ndarray:
        """LIBERO obs images need 180° rotation to match OFT training preprocessing."""
        return img[::-1, ::-1].copy()

    def _prepare_pil_image(self, img: np.ndarray) -> Image.Image:
        """Resize → (optional center-crop) → PIL RGB."""
        if img.shape != (OPENVLA_IMAGE_SIZE, OPENVLA_IMAGE_SIZE, 3):
            img = _resize_pil(img, OPENVLA_IMAGE_SIZE)
        if self.center_crop:
            return _center_crop_resize_pil(img, crop_scale=0.9,
                                           size=OPENVLA_IMAGE_SIZE)
        return Image.fromarray(img.astype(np.uint8)).convert("RGB")

    @torch.inference_mode()
    def _infer_chunk_with_hidden(self, agentview_rgb: np.ndarray, task_name: str,
                                  robot_state: np.ndarray,
                                  eye_in_hand_rgb: Optional[np.ndarray] = None,
                                  proprio_noise: Optional[np.ndarray] = None):
        """Run a single OFT inference call. Returns:
            actions: (chunk_size, 7) float64 numpy, unnormalized
            obs_feat: (1, llm_dim) float32 mean-pooled action-token hidden states
        """
        DEVICE = next(self.vla.parameters()).device

        agentview = self._libero_rotate(agentview_rgb)
        wrist = self._libero_rotate(eye_in_hand_rgb) if eye_in_hand_rgb is not None else None

        primary = self._prepare_pil_image(agentview)
        wrist_images = []
        if self.num_images_in_input > 1 and wrist is not None:
            wrist_images.append(self._prepare_pil_image(wrist))

        prompt = f"In: What action should the robot take to {task_name.lower()}?\nOut:"
        inputs = self.processor(prompt, primary).to(DEVICE, dtype=torch.bfloat16)
        if wrist_images:
            wrist_inputs = [
                self.processor(prompt, im).to(DEVICE, dtype=torch.bfloat16)
                for im in wrist_images
            ]
            primary_pv = inputs["pixel_values"]
            wrist_pvs = [wi["pixel_values"] for wi in wrist_inputs]
            inputs["pixel_values"] = torch.cat([primary_pv] + wrist_pvs, dim=1)

        proprio = None
        if self.use_proprio:
            proprio = np.asarray(robot_state, dtype=np.float64)
            if proprio_noise is not None:
                proprio = proprio + proprio_noise
            stats = self.vla.norm_stats[self.unnorm_key]["proprio"]
            proprio = _normalize_proprio(proprio, stats)

        actions, actions_hidden_states = self.vla.predict_action(
            **inputs,
            unnorm_key=self.unnorm_key,
            do_sample=False,
            proprio=proprio,
            proprio_projector=self.proprio_projector,
            noisy_action_projector=None,
            action_head=self.action_head,
            use_film=False,
        )
        obs_feat = actions_hidden_states.mean(dim=1).to(torch.float32)
        return np.asarray(actions, dtype=np.float64), obs_feat

    @torch.inference_mode()
    def get_obs_features_and_samples(self, agentview_rgb, task_name,
                                      robot_state, eye_in_hand_rgb=None, K=1):
        """End-to-end inference. K>1 injects small proprio noise for diversity.

        Returns:
            obs_feat: (1, llm_dim)
            samples: (1, K, chunk_size, FULL_ACTION_DIM)
        """
        samples = []
        obs_feat = None
        rng = np.random.default_rng()
        for k in range(K):
            noise = None
            if k > 0:
                noise = rng.normal(scale=0.01, size=PROPRIO_DIM).astype(np.float64)
            actions, of = self._infer_chunk_with_hidden(
                agentview_rgb, task_name, robot_state, eye_in_hand_rgb, noise
            )
            samples.append(actions)
            if obs_feat is None:
                obs_feat = of
        samples_np = np.stack(samples, axis=0)[None, ...]  # (1, K, T, 7)
        samples_t = torch.from_numpy(samples_np).to(torch.float32)
        return obs_feat, samples_t

    @torch.inference_mode()
    def get_obs_features_and_samples_adaptive(self, agentview_rgb, task_name,
                                               robot_state, eye_in_hand_rgb=None,
                                               threshold=0.1, k_init=1, k_full=1):
        """Adaptive K is meaningless for deterministic OFT; run K=k_full."""
        obs_feat, samples = self.get_obs_features_and_samples(
            agentview_rgb, task_name, robot_state, eye_in_hand_rgb, K=k_full
        )
        meta = {"path": "fast", "actual_k": k_full, "l2_distance": 0.0}
        return obs_feat, samples, meta

    def reset_action_queue(self):
        """Clear cached chunk. Call at the start of every rollout (env.reset)."""
        self._action_queue.clear()

    @torch.inference_mode()
    def predict_action(self, agentview_rgb, task_name, robot_state,
                       eye_in_hand_rgb=None, K: int = 1):
        """Return one (FULL_ACTION_DIM,) numpy action per call, with open-loop
        chunk replay. When the queue is empty, runs one inference, takes mean
        over K samples, and enqueues all chunk_size actions.
        """
        if not self._action_queue:
            _obs_feat, samples = self.get_obs_features_and_samples(
                agentview_rgb=agentview_rgb,
                task_name=task_name,
                robot_state=robot_state,
                eye_in_hand_rgb=eye_in_hand_rgb,
                K=K,
            )
            chunk = samples[0].mean(dim=0)  # (chunk_size, 7)
            chunk_np = chunk.detach().cpu().numpy()
            # Apply gripper remap: OFT outputs gripper in [0,1] but LIBERO env
            # expects [-1,+1] with sign inversion (close=+1 in env, but OFT
            # learned close=0 so we invert). Match OFT eval's process_action().
            for i in range(chunk_np.shape[0]):
                a = chunk_np[i].copy()
                # [0,1] -> [-1,+1]
                a[-1] = 2 * a[-1] - 1
                # binarize
                a[-1] = 1.0 if a[-1] > 0 else -1.0
                # invert (OpenVLA dataloader flips gripper to match other datasets;
                # flip back for LIBERO: -1=open, +1=close in env)
                a[-1] = -a[-1]
                self._action_queue.append(a)
        return self._action_queue.popleft()
