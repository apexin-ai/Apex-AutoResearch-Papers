"""
Geometric Prior Pruning for SmolVLA

Training-free vision token selection based on Sobel edge detection.
Keeps tokens whose spatial region has high image gradient (object boundaries).

SmolVLA architecture:
  SigLIP (512x512, patch_size=16) -> 32x32 = 1024 tokens
  Connector pixel_shuffle (scale_factor=4) -> 8x8 = 64 tokens per camera
  LIBERO: 2 cameras -> 128 total visual tokens

Each 8x8 output token maps to a 4x4 block of SigLIP patches = 64x64 pixels
in the 512x512 input image = 32x32 pixels in the raw 256x256 observation.
"""

from __future__ import annotations

import logging
from typing import List, Optional

import cv2
import numpy as np
import torch

log = logging.getLogger(__name__)

GRID_H = 8
GRID_W = 8
TOKENS_PER_CAMERA = GRID_H * GRID_W  # 64


def compute_sobel_importance(
    image: np.ndarray,
    grid_h: int = GRID_H,
    grid_w: int = GRID_W,
) -> np.ndarray:
    """
    Compute per-token geometric importance via Sobel edge detection.

    Args:
        image: (H, W, 3) uint8 numpy array, raw observation image.
        grid_h, grid_w: token grid dimensions (8x8 = 64 tokens).

    Returns:
        importance: (grid_h * grid_w,) float64 array, normalized to [0, 1].
    """
    # 180-deg flip to match SmolVLA image preprocessing (torch.flip dims=[2,3])
    image = image[::-1, ::-1].copy()

    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY).astype(np.float64)
    sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    magnitude = np.sqrt(sobelx ** 2 + sobely ** 2)

    H, W = magnitude.shape
    cell_h = H / grid_h
    cell_w = W / grid_w

    importance = np.zeros(grid_h * grid_w, dtype=np.float64)
    for i in range(grid_h):
        for j in range(grid_w):
            r0 = int(i * cell_h)
            r1 = int((i + 1) * cell_h)
            c0 = int(j * cell_w)
            c1 = int((j + 1) * cell_w)
            importance[i * grid_w + j] = magnitude[r0:r1, c0:c1].mean()

    vmin, vmax = importance.min(), importance.max()
    if vmax > vmin:
        importance = (importance - vmin) / (vmax - vmin)
    else:
        importance[:] = 1.0

    return importance


def compute_geometric_mask(
    images: List[np.ndarray],
    k_ratio: float,
    device: torch.device,
    grid_h: int = GRID_H,
    grid_w: int = GRID_W,
) -> torch.Tensor:
    """
    Compute a binary keep-mask for all cameras based on Sobel importance.

    Args:
        images: list of (H, W, 3) uint8 arrays, one per camera.
        k_ratio: fraction of total tokens to keep (0.5 = 50%).
        device: torch device for the output mask.
        grid_h, grid_w: token grid per camera.

    Returns:
        mask: (1, N_total) float tensor, 1.0 = keep, 0.0 = prune.
    """
    all_imp = []
    for img in images:
        imp = compute_sobel_importance(img, grid_h, grid_w)
        all_imp.append(imp)

    importance = np.concatenate(all_imp)
    importance_t = torch.from_numpy(importance).float().to(device)

    N = importance_t.shape[0]
    k = max(1, int(N * k_ratio))
    _, topk_idx = torch.topk(importance_t, k)

    mask = torch.zeros(1, N, device=device)
    mask[0, topk_idx] = 1.0

    return mask


def find_connector(model):
    """Find the SmolVLMConnector module in the model."""
    for name, module in model.named_modules():
        if name.endswith(".connector") or "multi_modal_projector" in name:
            return module
    return None


def register_geometric_hook(
    connector,
    mask: torch.Tensor,
    method: str = "true_removal",
):
    """
    Register a forward hook on the connector that prunes tokens by mask.

    Uses stateful offset tracking for multi-camera support: the connector
    is called once per camera during embed_prefix, and the offset advances
    by 64 tokens each call.

    Args:
        connector: the SmolVLMConnector module.
        mask: (B, N_total) tensor, 1.0 = keep. N_total = num_cameras * 64.
        method: "true_removal" (drop tokens) or "zero_mask" (zero out).

    Returns:
        hook handle (call .remove() after forward pass).
    """
    state = {"offset": 0}

    def hook_fn(module, input, output):
        tokens = output[0] if isinstance(output, tuple) else output
        if tokens.dim() != 3:
            return output

        n = tokens.shape[1]
        offset = state["offset"]
        if offset + n > mask.shape[1]:
            return output

        cam_mask = mask[:, offset : offset + n]
        state["offset"] = offset + n

        B, N, D = tokens.shape
        keep_mask = cam_mask[:B]

        if method == "true_removal":
            kept = keep_mask[0].bool()
            masked = tokens[:, kept, :]
        else:
            masked = tokens * keep_mask.unsqueeze(-1)

        if isinstance(output, tuple):
            return (masked,) + output[1:]
        return masked

    return connector.register_forward_hook(hook_fn)


class GeometricPriorPruner:
    """
    Manages geometric prior pruning lifecycle for SmolVLA evaluation.

    Usage:
        pruner = GeometricPriorPruner(model, k_ratio=0.5)

        for step in rollout:
            raw_images = [obs["pixels"]["image"], obs["pixels"]["image2"]]
            pruner.set_current_images(raw_images)
            pruner.attach(device)
            action_chunk = predict_actions(policy, batch)
            pruner.detach()

        pruner.remove()
    """

    def __init__(
        self,
        model,
        k_ratio: float = 0.5,
        method: str = "true_removal",
    ):
        self.k_ratio = k_ratio
        self.method = method
        self.connector = find_connector(model)
        if self.connector is None:
            raise RuntimeError("Cannot find connector module in model")
        self._current_images: List[np.ndarray] = []
        self._hook_handle = None
        self._last_mask: Optional[torch.Tensor] = None
        self._last_per_camera_importance: List[np.ndarray] = []

    def set_current_images(self, images: List[np.ndarray]):
        """Set raw observation images (list of HxWx3 uint8 arrays)."""
        self._current_images = images

    def attach(self, device: torch.device) -> torch.Tensor:
        """
        Compute Sobel importance, create mask, and register hook.

        Must call set_current_images() first.
        Returns the computed mask (1, N_total).
        """
        if not self._current_images:
            raise RuntimeError("No images set. Call set_current_images() first.")

        self._last_per_camera_importance = []
        for img in self._current_images:
            imp = compute_sobel_importance(img)
            self._last_per_camera_importance.append(imp)

        mask = compute_geometric_mask(
            self._current_images, self.k_ratio, device
        )
        self._last_mask = mask

        self._hook_handle = register_geometric_hook(
            self.connector, mask, method=self.method
        )
        return mask

    def detach(self):
        """Remove the current hook (call after each forward pass)."""
        if self._hook_handle is not None:
            self._hook_handle.remove()
            self._hook_handle = None

    def remove(self):
        """Alias for detach, cleans up hook."""
        self.detach()

    def get_importance_stats(self) -> dict:
        """Return stats from the last attach() call for debugging."""
        if not self._last_per_camera_importance:
            return {}
        stats = {}
        for i, imp in enumerate(self._last_per_camera_importance):
            stats[f"cam{i}_mean"] = float(imp.mean())
            stats[f"cam{i}_std"] = float(imp.std())
            stats[f"cam{i}_min"] = float(imp.min())
            stats[f"cam{i}_max"] = float(imp.max())
            stats[f"cam{i}_nonzero"] = int((imp > 0.01).sum())
        if self._last_mask is not None:
            stats["total_kept"] = int(self._last_mask.sum().item())
            stats["total_tokens"] = self._last_mask.shape[1]
        return stats
