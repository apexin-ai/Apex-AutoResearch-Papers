"""
Phase Segmentation via Attention Sparsity Profiling.

Implements the ThinKV (ICLR 2026 Oral) methodology:
  attention sparsity -> Gaussian KDE -> tri-modal phase detection.

Each token is assigned to one of three phases:
  - execution:   low sparsity (dense attention), focused computation
  - reasoning:   intermediate sparsity, broad cross-token reasoning
  - transition:  high sparsity, uncertainty/backtracking patterns
"""

from __future__ import annotations

import logging
import warnings
from dataclasses import dataclass, field
from typing import List, Optional, Tuple

import numpy as np
import torch
from scipy.signal import argrelmin
from scipy.stats import gaussian_kde

logger = logging.getLogger(__name__)

PHASE_NAMES_BY_SPARSITY = ["execution", "reasoning", "transition"]


@dataclass
class Phase:
    name: str            # "reasoning" / "execution" / "transition"
    start: int           # token start position (inclusive)
    end: int             # token end position (exclusive)
    mean_sparsity: float

    @property
    def token_indices(self) -> List[int]:
        return list(range(self.start, self.end))


@dataclass
class PhaseAnnotation:
    phases: List[Phase]
    boundaries: List[int]       # token indices where phase transitions occur
    sparsity: np.ndarray        # raw per-token sparsity, shape (seq_len,)
    kde_x: np.ndarray
    kde_density: np.ndarray
    metadata: dict = field(default_factory=dict)


class PhaseSegmenter:
    """Segment a token sequence into reasoning / transition / execution phases
    based on the attention sparsity profile and Gaussian KDE peak detection."""

    def __init__(
        self,
        bandwidth: str = "scott",
        min_phase_length: int = 10,
        sparsity_threshold_ratio: float = 0.01,
        kde_grid_points: int = 512,
        min_seq_length: int = 50,
    ):
        """
        Args:
            bandwidth: KDE bandwidth selection — "scott", "silverman", or a float.
            min_phase_length: Minimum tokens per phase; shorter segments are merged
                into their left neighbour.
            sparsity_threshold_ratio: Fraction of row-wise max used as the sparsity
                cutoff (default 1 %).
            kde_grid_points: Resolution of the KDE evaluation grid.
            min_seq_length: Sequences shorter than this are returned as a single phase.
        """
        self.bandwidth = bandwidth
        self.min_phase_length = min_phase_length
        self.sparsity_threshold_ratio = sparsity_threshold_ratio
        self.kde_grid_points = kde_grid_points
        self.min_seq_length = min_seq_length

    # ------------------------------------------------------------------
    # Step 1: per-token attention sparsity
    # ------------------------------------------------------------------

    def compute_attention_sparsity(
        self, attention_weights: torch.Tensor
    ) -> np.ndarray:
        """Compute per-token sparsity averaged over heads.

        For each head and each query position, sparsity is the fraction of
        attention scores below ``row_max * sparsity_threshold_ratio``.

        Args:
            attention_weights: shape ``(num_heads, seq_len, seq_len)``.

        Returns:
            Per-token sparsity array of shape ``(seq_len,)``.
        """
        # (H, S, S)
        attn = attention_weights.detach().float()
        if attn.dim() == 4:
            # (B, H, S, S) -> take first batch element
            attn = attn[0]
        assert attn.dim() == 3, f"Expected 3-D attention tensor, got shape {attn.shape}"

        # Row-wise max per head per query position: (H, S, 1)
        row_max, _ = attn.max(dim=-1, keepdim=True)
        threshold = row_max * self.sparsity_threshold_ratio

        # Fraction of keys below threshold for each (head, query) pair
        sparse_mask = (attn < threshold).float()         # (H, S, S)
        per_head_sparsity = sparse_mask.mean(dim=-1)     # (H, S)

        # Average across heads -> (S,)
        sparsity = per_head_sparsity.mean(dim=0).cpu().numpy()
        return sparsity

    def compute_step_sparsity(self, step_attention: torch.Tensor) -> float:
        """Compute sparsity for a single generation step's attention.

        Args:
            step_attention: (num_heads, 1, kv_len) or (num_heads, kv_len).

        Returns:
            Scalar sparsity (fraction of near-zero weights, averaged over heads).
        """
        attn = step_attention.detach().float()
        if attn.dim() == 4:
            attn = attn[0]
        if attn.dim() == 2:
            attn = attn.unsqueeze(1)  # (H, kv_len) -> (H, 1, kv_len)
        row_max, _ = attn.max(dim=-1, keepdim=True)
        threshold = row_max * self.sparsity_threshold_ratio
        sparse_mask = (attn < threshold).float()
        per_head_sparsity = sparse_mask.mean(dim=-1)  # (H, 1)
        return float(per_head_sparsity.mean())

    # ------------------------------------------------------------------
    # Step 2: Gaussian KDE
    # ------------------------------------------------------------------

    def fit_kde(
        self, sparsity: np.ndarray
    ) -> Tuple[np.ndarray, np.ndarray]:
        """Fit a Gaussian KDE to the sparsity values.

        Returns:
            ``(x_grid, density)`` — the evaluation grid and corresponding
            density estimates, both of shape ``(kde_grid_points,)``.
        """
        bw = self.bandwidth
        if isinstance(bw, str) and bw not in ("scott", "silverman"):
            try:
                bw = float(bw)
            except ValueError:
                logger.warning("Unknown bandwidth '%s', falling back to scott", bw)
                bw = "scott"

        kde = gaussian_kde(sparsity, bw_method=bw)

        lo, hi = sparsity.min(), sparsity.max()
        margin = (hi - lo) * 0.05 + 1e-8
        x_grid = np.linspace(lo - margin, hi + margin, self.kde_grid_points)
        density = kde(x_grid)
        return x_grid, density

    # ------------------------------------------------------------------
    # Step 3: phase boundary detection
    # ------------------------------------------------------------------

    def find_phase_boundaries(
        self, density: np.ndarray, x_grid: np.ndarray,
        sparsity: Optional[np.ndarray] = None,
        _meta: Optional[dict] = None,
    ) -> List[int]:
        """Detect local minima of the KDE density as phase boundaries.

        The method tries progressively wider ``order`` windows (5 -> 10 -> 20)
        and reduced-bandwidth re-fits to obtain exactly 2 boundaries (3 phases).
        If that still fails, falls back to equal-partition boundaries.

        Args:
            density: KDE density values on ``x_grid``.
            x_grid:  The evaluation grid (used only for logging).
            sparsity: Raw per-token sparsity values for narrow-bandwidth retry.
            _meta: If provided, populated with diagnostic metadata in-place.

        Returns:
            Sorted list of *x_grid indices* corresponding to phase boundaries.
        """
        if _meta is None:
            _meta = {}

        for order in (5, 10, 20):
            minima = argrelmin(density, order=order)[0]
            if len(minima) >= 2:
                sorted_by_depth = sorted(minima, key=lambda i: density[i])
                boundaries = sorted(sorted_by_depth[:2])
                _meta["n_minima_found"] = int(len(minima))
                _meta["fallback"] = False
                _meta["boundary_order"] = int(order)
                return boundaries

        logger.warning(
            "Could not find 2 local minima with default bandwidth; "
            "retrying with halved bandwidth."
        )
        result = self._retry_with_narrow_bandwidth(sparsity, x_grid, _meta=_meta)
        return result

    def _retry_with_narrow_bandwidth(
        self, sparsity: Optional[np.ndarray], x_grid: np.ndarray,
        _meta: Optional[dict] = None,
    ) -> List[int]:
        """Re-fit KDE with halved bandwidth and retry boundary detection."""
        if _meta is None:
            _meta = {}

        if sparsity is None:
            _meta["fallback"] = True
            _meta["fallback_reason"] = "no_sparsity_data"
            _meta["n_minima_found"] = 0
            return self._equal_partition_boundaries(len(x_grid))

        bw = self.bandwidth
        try:
            numeric_bw = float(bw) if not isinstance(bw, str) else None
        except (ValueError, TypeError):
            numeric_bw = None

        if numeric_bw is not None:
            narrow_bw = numeric_bw * 0.5
        else:
            narrow_bw = 0.05

        try:
            kde = gaussian_kde(sparsity, bw_method=narrow_bw)
            new_density = kde(x_grid)
            for order in (5, 10, 20):
                minima = argrelmin(new_density, order=order)[0]
                if len(minima) >= 2:
                    sorted_by_depth = sorted(minima, key=lambda i: new_density[i])
                    _meta["n_minima_found"] = int(len(minima))
                    _meta["fallback"] = False
                    _meta["narrow_bandwidth_used"] = float(narrow_bw)
                    _meta["boundary_order"] = int(order)
                    return sorted(sorted_by_depth[:2])
        except Exception:
            pass

        _meta["fallback"] = True
        _meta["fallback_reason"] = "no_minima_after_narrow_retry"
        _meta["n_minima_found"] = 0
        return self._equal_partition_boundaries(len(x_grid))

    def _equal_partition_boundaries(self, grid_len: int) -> List[int]:
        """Divide the grid into 3 equal parts."""
        logger.warning("Falling back to equal-partition phase boundaries.")
        b1 = grid_len // 3
        b2 = 2 * grid_len // 3
        return [b1, b2]

    # ------------------------------------------------------------------
    # Step 4: assign phase labels
    # ------------------------------------------------------------------

    def _assign_phases(
        self,
        sparsity: np.ndarray,
        x_grid: np.ndarray,
        boundary_indices: List[int],
    ) -> List[Phase]:
        """Map each token to a phase based on its sparsity value and the
        KDE-derived boundaries on x_grid."""

        # Convert boundary indices on x_grid to sparsity thresholds
        thresholds = [x_grid[i] for i in boundary_indices]
        thresholds = sorted(thresholds)

        seq_len = len(sparsity)
        labels = np.empty(seq_len, dtype=object)

        for t in range(seq_len):
            s = sparsity[t]
            if s <= thresholds[0]:
                labels[t] = "execution"
            elif s <= thresholds[1]:
                labels[t] = "reasoning"
            else:
                labels[t] = "transition"

        # Build contiguous Phase runs
        phases: List[Phase] = []
        run_start = 0
        for t in range(1, seq_len + 1):
            if t == seq_len or labels[t] != labels[run_start]:
                phases.append(
                    Phase(
                        name=labels[run_start],
                        start=run_start,
                        end=t,
                        mean_sparsity=float(sparsity[run_start:t].mean()),
                    )
                )
                if t < seq_len:
                    run_start = t

        # Merge phases shorter than min_phase_length into left neighbour
        phases = self._merge_short_phases(phases)
        return phases

    def _merge_short_phases(self, phases: List[Phase]) -> List[Phase]:
        if len(phases) <= 1:
            return phases

        merged: List[Phase] = [phases[0]]
        for p in phases[1:]:
            if (p.end - p.start) < self.min_phase_length:
                # Extend previous phase
                prev = merged[-1]
                merged[-1] = Phase(
                    name=prev.name,
                    start=prev.start,
                    end=p.end,
                    mean_sparsity=float(
                        np.mean(
                            np.concatenate([
                                np.full(prev.end - prev.start, prev.mean_sparsity),
                                np.full(p.end - p.start, p.mean_sparsity),
                            ])
                        )
                    ),
                )
            else:
                merged.append(p)
        return merged

    # ------------------------------------------------------------------
    # Main entry point
    # ------------------------------------------------------------------

    def segment(self, attention_weights: torch.Tensor) -> PhaseAnnotation:
        """End-to-end pipeline: attention weights -> phase annotation.

        Args:
            attention_weights: shape ``(num_heads, seq_len, seq_len)``
                or ``(1, num_heads, seq_len, seq_len)``.

        Returns:
            A ``PhaseAnnotation`` with per-token phase labels, boundaries,
            raw sparsity, and the KDE curve.
        """
        sparsity = self.compute_attention_sparsity(attention_weights)
        seq_len = len(sparsity)

        if seq_len < self.min_seq_length:
            logger.info(
                "Sequence length %d < %d; returning single phase.",
                seq_len, self.min_seq_length,
            )
            phase = Phase(
                name="execution",
                start=0,
                end=seq_len,
                mean_sparsity=float(sparsity.mean()),
            )
            dummy_x = np.linspace(0, 1, 2)
            return PhaseAnnotation(
                phases=[phase],
                boundaries=[],
                sparsity=sparsity,
                kde_x=dummy_x,
                kde_density=np.zeros(2),
                metadata={"short_sequence": True, "bandwidth": self.bandwidth},
            )

        kde_x, kde_density = self.fit_kde(sparsity)

        meta: dict = {"bandwidth": self.bandwidth}
        boundary_indices = self.find_phase_boundaries(
            kde_density, kde_x, sparsity=sparsity, _meta=meta,
        )

        phases = self._assign_phases(sparsity, kde_x, boundary_indices)
        token_boundaries = [p.start for p in phases[1:]]

        return PhaseAnnotation(
            phases=phases,
            boundaries=token_boundaries,
            sparsity=sparsity,
            kde_x=kde_x,
            kde_density=kde_density,
            metadata=meta,
        )

    def segment_from_sparsity(self, sparsity: np.ndarray) -> PhaseAnnotation:
        """Segment from a pre-computed per-token sparsity sequence.

        Used when sparsity is computed incrementally (e.g., per generation step)
        rather than from a full attention matrix.
        """
        seq_len = len(sparsity)

        if seq_len < self.min_seq_length:
            logger.info(
                "Sequence length %d < %d; returning single phase.",
                seq_len, self.min_seq_length,
            )
            phase = Phase(
                name="execution",
                start=0,
                end=seq_len,
                mean_sparsity=float(sparsity.mean()),
            )
            dummy_x = np.linspace(0, 1, 2)
            return PhaseAnnotation(
                phases=[phase],
                boundaries=[],
                sparsity=sparsity,
                kde_x=dummy_x,
                kde_density=np.zeros(2),
                metadata={"short_sequence": True, "bandwidth": self.bandwidth},
            )

        kde_x, kde_density = self.fit_kde(sparsity)

        meta: dict = {"bandwidth": self.bandwidth}
        boundary_indices = self.find_phase_boundaries(
            kde_density, kde_x, sparsity=sparsity, _meta=meta,
        )

        phases = self._assign_phases(sparsity, kde_x, boundary_indices)
        token_boundaries = [p.start for p in phases[1:]]

        return PhaseAnnotation(
            phases=phases,
            boundaries=token_boundaries,
            sparsity=sparsity,
            kde_x=kde_x,
            kde_density=kde_density,
            metadata=meta,
        )
