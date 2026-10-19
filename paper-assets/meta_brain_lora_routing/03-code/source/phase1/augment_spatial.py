"""
Spatial perturbation augmentation for LoRA-S training.

Approach: Plan B (image-level distractor synthesis).

Why not Plan A (LIBERO env replay of _add_N BDDLs):
- LIBERO-Plus supplies _add_N BDDL files at /root/LIBERO-plus/libero/libero/bddl_files
  and OffScreenRenderEnv loads them, but full re-render requires (a) GPU rendering
  while cuda:0-3 are occupied by the running LoRA training, (b) per-frame init_state
  + action replay (~2s reset + ~50ms/step), and (c) restructuring the LeRobot
  parquet pipeline to consume re-rendered observations. Online per-batch use is
  infeasible; offline preprocess collides with the GPU constraint.

Plan B simulates the visual effect of LIBERO_add_N (distractor objects appearing
in the scene) by compositing 1-N synthetic "object-like" patches onto each image:
- Random small ellipse/rectangle masks with soft alpha edges
- Random uniform colors in [-1, 1]
- Position biased toward the lower portion of the frame (where objects sit on
  the table in LIBERO scenes), with a small no-go zone around the image center
  to avoid covering the manipulation target
- Independent draws per sample and per view (matches what the real env produces
  -- different views see different distractor placements)

Operates on a dict of (B, C, H, W) or (C, H, W) image tensors in [-1, 1].
"""

from __future__ import annotations

import math
from typing import Dict

import numpy as np
import torch


def _make_ellipse_mask(h: int, w: int, soft_edge: float = 1.5) -> np.ndarray:
    """Soft-edged ellipse mask in [0, 1], shape (h, w)."""
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    cy, cx = (h - 1) / 2.0, (w - 1) / 2.0
    ry, rx = h / 2.0, w / 2.0
    d = ((yy - cy) / ry) ** 2 + ((xx - cx) / rx) ** 2
    edge = np.clip((1.0 - d) * max(h, w) / soft_edge, 0.0, 1.0)
    return edge


def _make_rect_mask(h: int, w: int, soft_edge: float = 2.0) -> np.ndarray:
    """Soft-edged rectangle mask in [0, 1]."""
    mask = np.ones((h, w), dtype=np.float32)
    border = max(1, int(min(h, w) / soft_edge / 2))
    for i in range(border):
        a = (i + 1) / border
        mask[i, :] = np.minimum(mask[i, :], a)
        mask[h - 1 - i, :] = np.minimum(mask[h - 1 - i, :], a)
        mask[:, i] = np.minimum(mask[:, i], a)
        mask[:, w - 1 - i] = np.minimum(mask[:, w - 1 - i], a)
    return mask


class SpatialAugmentation:
    """Pastes synthetic distractor patches onto each image to mimic the
    LIBERO _add_N (added-object) perturbation family.

    Args:
        severity: Scales the number and size of distractors. severity=0.5
            yields ~3 distractors of size ~12-22 pixels on a 224x224 image.
        num_distractors_range: (min, max) inclusive range when severity=1.
        patch_size_range: (min, max) inclusive pixel range when severity=1.
        center_keepout: Fraction of the image diagonal around the image
            center to avoid (target object lives near center). 0 disables.
        seed: RNG seed for reproducibility.
    """

    def __init__(
        self,
        severity: float = 0.5,
        num_distractors_range=(1, 5),
        patch_size_range=(8, 28),
        center_keepout: float = 0.18,
        seed: int = 0,
    ):
        self.severity = float(severity)
        self.num_range = tuple(num_distractors_range)
        self.size_range = tuple(patch_size_range)
        self.center_keepout = float(center_keepout)
        self._rng = np.random.default_rng(seed)

    def __call__(self, images: Dict[str, torch.Tensor]) -> Dict[str, torch.Tensor]:
        out = {}
        for key, img in images.items():
            squeeze = img.ndim == 3
            if squeeze:
                img = img.unsqueeze(0)
            out[key] = self._add_distractors(img)
            if squeeze:
                out[key] = out[key].squeeze(0)
        return out

    def _add_distractors(self, img: torch.Tensor) -> torch.Tensor:
        B, C, H, W = img.shape
        device, dtype = img.device, img.dtype
        result = img.clone()

        n_min = max(0, int(round(self.num_range[0] * max(self.severity, 0.1))))
        n_max = max(n_min, int(round(self.num_range[1] * self.severity)))
        if n_max == 0:
            return result

        s_min = max(2, int(round(self.size_range[0] * (0.5 + 0.5 * self.severity))))
        s_max = max(s_min + 1, int(round(self.size_range[1] * (0.5 + 0.5 * self.severity))))

        cy_img, cx_img = H / 2.0, W / 2.0
        keepout_r2 = (self.center_keepout * math.hypot(H, W)) ** 2

        for b in range(B):
            n = int(self._rng.integers(n_min, n_max + 1))
            for _ in range(n):
                ph = int(self._rng.integers(s_min, s_max + 1))
                pw = int(self._rng.integers(s_min, s_max + 1))
                if ph >= H or pw >= W:
                    continue
                # Sample position with a few rejection retries to honor keepout
                # and to bias placement toward the lower 70% of the frame.
                for _try in range(6):
                    cy = int(self._rng.integers(int(H * 0.25), H - ph))
                    cx = int(self._rng.integers(0, W - pw))
                    yc, xc = cy + ph / 2.0, cx + pw / 2.0
                    if (yc - cy_img) ** 2 + (xc - cx_img) ** 2 >= keepout_r2:
                        break

                shape = "ellipse" if self._rng.random() < 0.65 else "rect"
                mask_np = _make_ellipse_mask(ph, pw) if shape == "ellipse" else _make_rect_mask(ph, pw)

                # Object-like color: random hue, plus a mild shading gradient
                # so the patch is not a flat blob.
                color = self._rng.uniform(-0.9, 0.9, size=3).astype(np.float32)
                shade = np.linspace(-0.15, 0.15, ph, dtype=np.float32)[:, None]
                patch_np = np.broadcast_to(color[:, None, None], (3, ph, pw)).copy()
                patch_np = patch_np + shade[None]  # apply vertical shading
                patch_np = np.clip(patch_np, -1.0, 1.0)

                patch = torch.from_numpy(patch_np).to(device=device, dtype=dtype)
                if C != 3:
                    # Replicate or trim channels to match input depth (rare path).
                    patch = patch.mean(dim=0, keepdim=True).expand(C, -1, -1).contiguous()
                mask = torch.from_numpy(mask_np).to(device=device, dtype=dtype)

                region = result[b, :, cy : cy + ph, cx : cx + pw]
                blended = region * (1.0 - mask) + patch * mask
                result[b, :, cy : cy + ph, cx : cx + pw] = blended

        return result.clamp(-1.0, 1.0)
