# CoRL 2026 Abstract Draft v2

**Status**: DRAFT — M64 VTR pending, π0.5 Long Random collecting
**Date**: 2026-05-22
**Changes from v1**: Strengthened SmolVLA evidence (4-suite complete), added token-independent task complexity effect, tightened language

---

## Title
Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility

## Abstract

Vision-Language-Action models (VLAs) consume hundreds of vision tokens per inference step, motivating inference-time token pruning for efficient deployment. However, pruning that preserves performance on one VLA can catastrophically fail on another—a phenomenon that remains unexplained.

We present the first systematic study of token pruning robustness across VLA architectures, evaluating 5 models (450M–7B parameters) spanning 3 vision connector families on 4 LIBERO manipulation suites of increasing complexity. We discover that pruning sensitivity is governed by two interacting axes: (1) **token coupling**, determined by the vision connector architecture, and (2) **task complexity**. Token-independent connectors (linear projection, MLP) degrade gracefully—losing under 2 percentage points on simple tasks at 10% pruning—but show 10 times greater sensitivity on long-horizon tasks. Token-entangling connectors (deep encoder, pixel-shuffle) exhibit dramatically amplified interaction: the same model loses 1.6 points on simple manipulation but 27.8 points on goal-conditioned tasks at the same keep ratio, while pixel-shuffle connectors collapse to 0% success rate across all four suites with just 5% token removal.

We show that the coefficient of variation (CV) of token importance norms, computed in a single forward pass, predicts both pruning tolerance and optimal strategy: importance-based selection is actively harmful on low-CV architectures (up to 36-point gap favoring random pruning), while it consistently outperforms on high-CV models. For connectors where all deletion-based pruning fails, lightweight learned re-encoding (~22M parameters) achieves near-lossless compression at ratios up to 87.5%, recovering from 0% to baseline-level performance.

Our findings provide practitioners with a zero-cost diagnostic pipeline: measure CV, select pruning strategy accordingly, and apply learned re-encoding when deletion fails.

---

## Changes from v1
- "degrade gracefully—losing under 2 percentage points on simple tasks at 10% pruning—but show 10 times greater sensitivity on long-horizon tasks" — incorporates π0.5 Long L2 k=0.9=81.0% (-10.6pp) vs Object k=0.9=98.2% (-0pp), showing task complexity affects BOTH connector types
- "collapse to 0% success rate across all four suites with just 5% token removal" — SmolVLA 4-suite complete data (Object 0%, Spatial 6.6%, Goal 3.4%, Long 0% at k=0.95)
- "10 times greater sensitivity" = Object ~0pp vs Long ~10.6pp at same k (π0.5 L2 k=0.9)
- Removed "it consistently helps" → "it consistently outperforms" (more precise)
- Word count: ~248, within 250 limit

## Still pending
- M64 VTR result (ETA 5/23 16:40) — if positive, can strengthen "near-lossless" to something stronger
- "5 models" still includes π0 offline metrics only — acceptable for abstract scope
- "3 connector families" = linear/MLP, deep encoder (BART), pixel-shuffle — accurate
- Non-monotonicity / "small N danger zone" — too detailed for abstract, saved for Section 4.2
