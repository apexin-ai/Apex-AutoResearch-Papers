"""TurnKVPress — turn-aware KV cache compression built on kvpress ScorerPress.

Inherits from ScorerPress so that __call__(model) context manager, compress(),
and forward_hook all work correctly with the kvpress framework. Wraps an
internal ExpectedAttentionPress for per-token scoring, then applies segment-
level budget modulation based on structural priors and EASS."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Optional, Sequence

if TYPE_CHECKING:
    import torch

from .eass import Segment, compute_budget, compute_eass, map_budget_to_scores

# ---------------------------------------------------------------------------
# Import ScorerPress with fallback stub for local dev without kvpress
# ---------------------------------------------------------------------------

try:
    from kvpress.presses.scorer_press import ScorerPress as _ScorerPress
except ImportError:
    @dataclass
    class _ScorerPress:
        """Stub for development without kvpress installed."""
        compression_ratio: float = 0.0

        def score(self, module, hidden_states, keys, values, attentions, kwargs):
            raise NotImplementedError


@dataclass
class TurnKVPress(_ScorerPress):
    """ScorerPress that re-weights EA scores with turn-level structural budgets.

    Usage::

        from turnkv import TurnKVPress

        press = TurnKVPress(compression_ratio=0.7, beta=0.5)
        press.set_segments(segments)
        with press(model) as compressed_model:
            outputs = compressed_model.generate(input_ids)
    """

    compression_ratio: float = 0.0
    beta: float = 0.5
    b_min: float = 0.1
    b_max: float = 1.0

    def __post_init__(self):
        if hasattr(super(), '__post_init__'):
            super().__post_init__()
        self._ea_press = None
        self._segments: Optional[Sequence[Segment]] = None

    def _get_ea_press(self):
        """Lazily create the internal EA scorer on first use."""
        if self._ea_press is None:
            from kvpress import ExpectedAttentionPress
            self._ea_press = ExpectedAttentionPress(
                compression_ratio=self.compression_ratio
            )
        return self._ea_press

    # ------------------------------------------------------------------
    # Segment management
    # ------------------------------------------------------------------

    def set_segments(self, segments: Sequence[Segment]) -> None:
        self._segments = segments

    @property
    def segments(self) -> Optional[Sequence[Segment]]:
        return self._segments

    # ------------------------------------------------------------------
    # ScorerPress interface
    # ------------------------------------------------------------------

    def score(
        self,
        module: object,
        hidden_states: "torch.Tensor",
        keys: "torch.Tensor",
        values: "torch.Tensor",
        attentions: "torch.Tensor",
        kwargs: dict,
    ) -> "torch.Tensor":
        """Compute turn-aware importance scores for KV cache eviction.

        Returns shape (batch, num_kv_heads, seq_len) where higher = keep.
        """
        ea_press = self._get_ea_press()
        ea_scores = ea_press.score(
            module, hidden_states, keys, values, attentions, kwargs
        )

        if not self._segments:
            return ea_scores

        segments = list(self._segments)
        max_turn = max(s.turn_index for s in segments)

        eass = compute_eass(ea_scores, segments)

        budgets = compute_budget(
            segments,
            eass,
            beta=self.beta,
            b_min=self.b_min,
            b_max=self.b_max,
            max_turn=max_turn,
        )

        return map_budget_to_scores(ea_scores, segments, budgets)
