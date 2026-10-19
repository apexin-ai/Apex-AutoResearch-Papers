"""
Data loading for Phase 1 LoRA expert training.

Provides datasets and augmentation for perturbation-specific LoRA fine-tuning
of the pi0 model. Supports synthetic data for dry-run validation and will
support real LIBERO-Plus rollout data for actual training.

Input:  Rollout .pt files from LIBERO-Plus (or synthetic for dry-run)
Output: (Observation, actions) batches for PI0Pytorch.forward()

Dependencies: torch, torchvision
"""

import dataclasses
import logging
from pathlib import Path

import torch
from torch.utils.data import DataLoader, Dataset

log = logging.getLogger(__name__)

IMAGE_KEYS = ("base_0_rgb", "left_wrist_0_rgb", "right_wrist_0_rgb")
IMAGE_RESOLUTION = 224
STATE_DIM = 32
ACTION_DIM = 32
ACTION_HORIZON = 50
MAX_TOKEN_LEN = 48

PERTURBATION_TO_6CLASS = {
    "visual": ["camera_viewpoints", "light_conditions", "background_textures", "sensor_noise"],
    "spatial": ["objects_layout"],
    "physical": ["robot_initial_states"],
    "universal": [
        "camera_viewpoints", "light_conditions", "background_textures",
        "sensor_noise", "objects_layout", "robot_initial_states",
    ],
}


@dataclasses.dataclass
class Observation:
    """Minimal observation container matching PI0Pytorch's expected input.

    This is a lightweight replacement for openpi.models.model.Observation
    to avoid pulling in JAX/Flax dependencies from the original class.
    Works with jax.tree.map for device transfer.
    """
    images: dict
    image_masks: dict
    state: torch.Tensor
    tokenized_prompt: torch.Tensor
    tokenized_prompt_mask: torch.Tensor
    token_ar_mask: object = None
    token_loss_mask: object = None


# ---------------------------------------------------------------------------
# Synthetic dataset (dry-run validation)
# ---------------------------------------------------------------------------

class SyntheticRolloutDataset(Dataset):
    """Generates random observation-action pairs for dry-run validation.

    Produces correctly-shaped tensors that exercise the full PI0Pytorch
    forward pass without requiring real LIBERO data.
    """

    def __init__(self, num_samples=100, seed=42):
        self.num_samples = num_samples
        self.seed = seed

    def __len__(self):
        return self.num_samples

    def __getitem__(self, idx):
        g = torch.Generator().manual_seed(self.seed + idx)

        images = {
            key: torch.randn(3, IMAGE_RESOLUTION, IMAGE_RESOLUTION, generator=g)
            for key in IMAGE_KEYS
        }
        image_masks = {
            "base_0_rgb": torch.tensor(True),
            "left_wrist_0_rgb": torch.tensor(True),
            "right_wrist_0_rgb": torch.tensor(False),
        }
        state = torch.randn(STATE_DIM, generator=g)

        prompt_len = 5 + idx % (MAX_TOKEN_LEN - 5)
        tokenized_prompt = torch.zeros(MAX_TOKEN_LEN, dtype=torch.long)
        tokenized_prompt[:prompt_len] = torch.randint(
            0, 10000, (prompt_len,), generator=g
        )
        tokenized_prompt_mask = torch.zeros(MAX_TOKEN_LEN, dtype=torch.bool)
        tokenized_prompt_mask[:prompt_len] = True

        actions = torch.randn(ACTION_HORIZON, ACTION_DIM, generator=g)

        obs = Observation(
            images=images,
            image_masks=image_masks,
            state=state,
            tokenized_prompt=tokenized_prompt,
            tokenized_prompt_mask=tokenized_prompt_mask,
        )
        return obs, actions


# ---------------------------------------------------------------------------
# Real rollout dataset (placeholder for collected data)
# ---------------------------------------------------------------------------

class LIBERORolloutDataset(Dataset):
    """Loads LIBERO-Plus rollout data for LoRA training.

    Expected rollout file format (.pt):
    [
        {
            'images': {
                'base_0_rgb': tensor (T, 3, 224, 224),  # float32 [-1,1]
                'left_wrist_0_rgb': tensor (T, 3, 224, 224),
            },
            'state': tensor (T, 32),        # padded robot state
            'actions': tensor (T, 32),       # padded actions
            'prompt_tokens': tensor (L,),    # pre-tokenized instruction
            'prompt_mask': tensor (L,),      # token mask
            'perturbation_type': str,
            'metadata': dict,
        },
        ...
    ]
    """

    def __init__(self, data_dir, perturbation_type, seed=42):
        self.data_dir = Path(data_dir)
        self.perturbation_type = perturbation_type
        self.episodes = []
        self._load_episodes()
        log.info(
            f"Loaded {len(self.episodes)} steps from "
            f"{self.perturbation_type} rollouts"
        )

    def _load_episodes(self):
        target_types = PERTURBATION_TO_6CLASS[self.perturbation_type]
        for pt_type in target_types:
            path = self.data_dir / f"{pt_type}.pt"
            if not path.exists():
                log.warning(f"Rollout file not found: {path}")
                continue
            data = torch.load(path, map_location="cpu", weights_only=False)
            for episode in data:
                if episode.get("perturbation_type") in target_types:
                    self._flatten_episode(episode)

    def _flatten_episode(self, episode):
        """Convert episode to per-step training samples."""
        T = episode["actions"].shape[0]
        for t in range(T - ACTION_HORIZON):
            self.episodes.append({
                "images": {
                    k: episode["images"][k][t]
                    for k in episode["images"]
                    if k in IMAGE_KEYS
                },
                "state": episode["state"][t],
                "actions": episode["actions"][t : t + ACTION_HORIZON],
                "prompt_tokens": episode["prompt_tokens"],
                "prompt_mask": episode["prompt_mask"],
            })

    def __len__(self):
        return len(self.episodes)

    def __getitem__(self, idx):
        sample = self.episodes[idx]
        images = dict(sample["images"])
        if "right_wrist_0_rgb" not in images:
            images["right_wrist_0_rgb"] = torch.zeros(
                3, IMAGE_RESOLUTION, IMAGE_RESOLUTION
            )

        image_masks = {
            "base_0_rgb": torch.tensor(True),
            "left_wrist_0_rgb": torch.tensor(True),
            "right_wrist_0_rgb": torch.tensor(False),
        }

        prompt = sample["prompt_tokens"]
        mask = sample["prompt_mask"]
        if prompt.shape[0] < MAX_TOKEN_LEN:
            prompt = torch.nn.functional.pad(
                prompt, (0, MAX_TOKEN_LEN - prompt.shape[0])
            )
            mask = torch.nn.functional.pad(
                mask, (0, MAX_TOKEN_LEN - mask.shape[0])
            )

        obs = Observation(
            images=images,
            image_masks=image_masks,
            state=sample["state"],
            tokenized_prompt=prompt[:MAX_TOKEN_LEN],
            tokenized_prompt_mask=mask[:MAX_TOKEN_LEN],
        )
        actions = sample["actions"]
        if actions.shape[0] < ACTION_HORIZON:
            actions = torch.nn.functional.pad(
                actions, (0, 0, 0, ACTION_HORIZON - actions.shape[0])
            )
        return obs, actions[:ACTION_HORIZON]


# ---------------------------------------------------------------------------
# Visual augmentation (for LoRA-V)
# ---------------------------------------------------------------------------

class VisualAugmentation:
    """Online visual augmentation for LoRA-V training.

    Applies camera jitter, brightness/contrast shifts, and Gaussian noise
    to simulate visual perturbations. Applied to batched image tensors
    (B, C, H, W) in [-1, 1] range.
    """

    def __init__(self, severity=0.5):
        self.severity = severity

    def __call__(self, images):
        """Augment a dict of (B, C, H, W) image tensors in-place."""
        aug = {}
        for key, img in images.items():
            if img.ndim == 3:
                img = img.unsqueeze(0)
            if "wrist" not in key:
                img = self._camera_jitter(img)
            img = self._brightness_contrast(img)
            img = self._gaussian_noise(img)
            aug[key] = img.clamp(-1.0, 1.0)
        return aug

    def _camera_jitter(self, img):
        B, C, H, W = img.shape
        pad = max(1, int(H * 0.05 * self.severity))
        img = torch.nn.functional.pad(img, [pad] * 4, mode="replicate")
        cy = torch.randint(0, 2 * pad + 1, (1,)).item()
        cx = torch.randint(0, 2 * pad + 1, (1,)).item()
        return img[:, :, cy : cy + H, cx : cx + W]

    def _brightness_contrast(self, img):
        s = self.severity
        brightness = 1.0 + (torch.rand(1, device=img.device).item() - 0.5) * 0.6 * s
        contrast = 1.0 + (torch.rand(1, device=img.device).item() - 0.5) * 0.6 * s
        mean = img.mean(dim=(2, 3), keepdim=True)
        return (img - mean) * contrast + mean + (brightness - 1.0)

    def _gaussian_noise(self, img):
        return img + torch.randn_like(img) * 0.05 * self.severity


# ---------------------------------------------------------------------------
# Collate function
# ---------------------------------------------------------------------------

def collate_observations(batch):
    """Collate list of (Observation, actions) into batched tensors."""
    observations, actions_list = zip(*batch)

    images = {
        key: torch.stack([obs.images[key] for obs in observations])
        for key in IMAGE_KEYS
    }
    image_masks = {
        key: torch.stack([obs.image_masks[key] for obs in observations])
        for key in IMAGE_KEYS
    }

    obs = Observation(
        images=images,
        image_masks=image_masks,
        state=torch.stack([o.state for o in observations]),
        tokenized_prompt=torch.stack([o.tokenized_prompt for o in observations]),
        tokenized_prompt_mask=torch.stack(
            [o.tokenized_prompt_mask for o in observations]
        ),
    )
    return obs, torch.stack(actions_list)


# ---------------------------------------------------------------------------
# Factory
# ---------------------------------------------------------------------------

def create_dataloader(
    perturbation_type,
    batch_size=2,
    num_workers=0,
    dry_run=False,
    data_dir=None,
    seed=42,
):
    """Create DataLoader for a specific perturbation type.

    Args:
        perturbation_type: one of visual/spatial/physical/universal
        dry_run: if True, use synthetic data
        data_dir: path to rollout .pt files (required if not dry_run)
    """
    if dry_run:
        dataset = SyntheticRolloutDataset(num_samples=100, seed=seed)
    else:
        if data_dir is None:
            raise ValueError("data_dir required for non-dry-run training")
        data_path = Path(data_dir)
        if not data_path.exists():
            raise FileNotFoundError(
                f"Rollout data directory not found: {data_path}. "
                f"Collect LIBERO-Plus rollout data first, or use --dry_run."
            )
        dataset = LIBERORolloutDataset(data_path, perturbation_type, seed=seed)

    return DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=True,
        num_workers=num_workers,
        collate_fn=collate_observations,
        pin_memory=True,
        drop_last=True,
    )
