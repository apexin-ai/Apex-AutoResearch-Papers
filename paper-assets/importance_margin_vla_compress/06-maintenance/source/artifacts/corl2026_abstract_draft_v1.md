# CoRL 2026 Abstract Draft v1

**Status**: DRAFT — pending final data (π0.5 Goal/Long, OpenVLA VTC M64)
**Date**: 2026-05-22
**Word count target**: ~250 words (CoRL limit)

---

## Title
Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility

## Abstract

Vision-Language-Action models (VLAs) consume hundreds of vision tokens per inference step, motivating inference-time token pruning for efficient deployment. However, pruning that preserves performance on one VLA can catastrophically fail on another—a phenomenon that remains unexplained.

We present the first systematic study of token pruning robustness across VLA architectures, evaluating 5 models (450M–7B parameters) spanning 3 vision connector families on 4 LIBERO task suites. We discover that pruning sensitivity is governed by two interacting axes: (1) **token coupling**, determined by the vision connector architecture, and (2) **task complexity**. Token-independent connectors (linear projection, MLP) exhibit graceful degradation under pruning, while token-entangling connectors (deep encoder, pixel-shuffle) show dramatically amplified sensitivity under complex tasks—the same model loses 1.6 percentage points on simple manipulation but 27.8 points on goal-conditioned tasks at the same keep ratio.

We show that the coefficient of variation (CV) of token importance norms, computed in a single forward pass, predicts both pruning tolerance and optimal strategy: importance-based selection is actively harmful on low-CV architectures (up to 36-point gap favoring random pruning), while it consistently helps on high-CV models. For architectures where all deletion-based pruning fails, we show that lightweight learned re-encoding (~22M parameters) achieves near-lossless compression at ratios up to 87.5%, recovering from 0% success rate under hard pruning to baseline-level performance.

Our findings provide practitioners with a zero-cost diagnostic pipeline: measure CV, select pruning strategy accordingly, and apply learned re-encoding when deletion fails.

---

## Notes for revision
- Claim 4 (VTR) deliberately weakened: "near-lossless" / "baseline-level" instead of "exceeds baseline"
- If OpenVLA VTC M64 is positive, can strengthen last paragraph
- "5 models" includes π0 (offline metrics only) — verify this is defensible for abstract
- Consider whether "3 connector families" or "4 connector types" is more accurate given 2-axis framework
- Word count: ~235, within limit
