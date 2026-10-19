"""
SDF ground-truth data loading for ColliForce-VLA training.

Loads precomputed SDF data (from pysdf) and provides batched query points
with importance-weighted sampling for near-surface regions.

Data format:
  Per-scene .npz files containing:
    - query_points: [N, 3] xyz coordinates
    - sdf_values: [N] signed distance values
    - object_ids: [N] (optional) per-point object label

DataLoader interface:
  Input: scene_id, timestep
  Output: query_points [n_samples, 3], sdf_gt [n_samples], sample_weights [n_samples]

Dependencies: torch, numpy
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator

import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader


@dataclass
class SDFDataConfig:
    data_dir: str = ""
    n_query_points: int = 4096
    clamp_delta: float = 0.05
    # Importance sampling: points with |SDF| < near_surface_threshold get higher weight
    near_surface_threshold: float = 0.01
    near_surface_weight: float = 5.0
    far_surface_weight: float = 1.0
    # Scene filtering
    scene_ids: list[str] = field(default_factory=list)


class SDFSceneData:
    """Holds precomputed SDF data for a single scene."""

    def __init__(self, npz_path: str | Path, clamp_delta: float = 0.05):
        data = np.load(npz_path)
        self.query_points = data["query_points"].astype(np.float32)  # [N, 3]
        self.sdf_values = data["sdf_values"].astype(np.float32)  # [N]
        self.object_ids = data.get("object_ids", None)  # [N] or None

        # Clamp SDF to [-delta, delta]
        self.sdf_values = np.clip(self.sdf_values, -clamp_delta, clamp_delta)
        self.n_points = len(self.sdf_values)

    def compute_importance_weights(
        self,
        near_threshold: float = 0.01,
        near_weight: float = 5.0,
        far_weight: float = 1.0,
    ) -> np.ndarray:
        """Compute per-point sampling weights. Near-surface points weighted higher."""
        weights = np.where(
            np.abs(self.sdf_values) < near_threshold,
            near_weight,
            far_weight,
        )
        weights = weights / weights.sum()
        return weights


class SDFDataset(Dataset):
    """
    Multi-scene SDF dataset with dynamic importance-weighted point sampling.
    Each __getitem__ returns a random subset of query points from one scene.
    """

    def __init__(self, config: SDFDataConfig):
        self.config = config
        self.scenes: dict[str, SDFSceneData] = {}
        self.scene_list: list[str] = []

        self._load_scenes()

    def _load_scenes(self) -> None:
        data_dir = Path(self.config.data_dir)
        if not data_dir.exists():
            # TODO: Create data_dir and generate SDF data with pysdf pipeline
            return

        if self.config.scene_ids:
            scene_files = [data_dir / f"{sid}.npz" for sid in self.config.scene_ids]
        else:
            scene_files = sorted(data_dir.glob("*.npz"))

        for f in scene_files:
            if f.exists():
                scene_id = f.stem
                self.scenes[scene_id] = SDFSceneData(f, self.config.clamp_delta)
                self.scene_list.append(scene_id)

    def __len__(self) -> int:
        return max(len(self.scene_list), 1)

    def __getitem__(self, idx: int) -> dict[str, torch.Tensor]:
        if not self.scenes:
            # Return dummy data when no scenes loaded (for framework testing)
            return self._dummy_sample()

        scene_id = self.scene_list[idx % len(self.scene_list)]
        scene = self.scenes[scene_id]

        # Importance-weighted random sampling
        weights = scene.compute_importance_weights(
            near_threshold=self.config.near_surface_threshold,
            near_weight=self.config.near_surface_weight,
            far_weight=self.config.far_surface_weight,
        )

        n = min(self.config.n_query_points, scene.n_points)
        indices = np.random.choice(scene.n_points, size=n, replace=False, p=weights)

        query_points = torch.from_numpy(scene.query_points[indices])  # [n, 3]
        sdf_gt = torch.from_numpy(scene.sdf_values[indices])  # [n]

        # Normalize sample weights for loss computation
        sample_weights = torch.from_numpy(weights[indices].astype(np.float32))
        sample_weights = sample_weights / sample_weights.sum() * n

        return {
            "query_points": query_points,
            "sdf_gt": sdf_gt,
            "sample_weights": sample_weights,
        }

    def _dummy_sample(self) -> dict[str, torch.Tensor]:
        n = self.config.n_query_points
        return {
            "query_points": torch.randn(n, 3) * 0.3,
            "sdf_gt": torch.randn(n) * 0.02,
            "sample_weights": torch.ones(n),
        }


def create_sdf_dataloader(
    config: SDFDataConfig,
    batch_size: int = 1,
    num_workers: int = 4,
    shuffle: bool = True,
) -> DataLoader:
    dataset = SDFDataset(config)
    return DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=shuffle,
        num_workers=num_workers,
        pin_memory=True,
        drop_last=True,
    )


class SDFBatchCollator:
    """
    Collates SDF samples to align with VLA training batches.
    Maps scene_id from the VLA batch to the corresponding SDF data.
    """

    def __init__(self, dataset: SDFDataset):
        self.dataset = dataset

    def collate_for_batch(
        self,
        scene_ids: list[str],
    ) -> dict[str, torch.Tensor] | None:
        """
        Fetch SDF data for a list of scene_ids (one per batch element).

        Returns None if SDF data is unavailable for any scene.
        """
        if not self.dataset.scenes:
            return None

        points_list, sdf_list, weights_list = [], [], []
        for sid in scene_ids:
            if sid not in self.dataset.scenes:
                return None
            scene = self.dataset.scenes[sid]
            weights = scene.compute_importance_weights(
                near_threshold=self.dataset.config.near_surface_threshold,
                near_weight=self.dataset.config.near_surface_weight,
                far_weight=self.dataset.config.far_surface_weight,
            )
            n = min(self.dataset.config.n_query_points, scene.n_points)
            idx = np.random.choice(scene.n_points, size=n, replace=False, p=weights)

            points_list.append(torch.from_numpy(scene.query_points[idx]))
            sdf_list.append(torch.from_numpy(scene.sdf_values[idx]))
            w = torch.from_numpy(weights[idx].astype(np.float32))
            weights_list.append(w / w.sum() * n)

        return {
            "query_points": torch.stack(points_list),  # [B, n, 3]
            "sdf_gt": torch.stack(sdf_list),  # [B, n]
            "sample_weights": torch.stack(weights_list),  # [B, n]
        }
