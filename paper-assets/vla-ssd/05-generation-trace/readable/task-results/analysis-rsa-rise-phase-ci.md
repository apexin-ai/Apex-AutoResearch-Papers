# analysis rsa rise phase ci

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_rsa_rise_phase_ci_20260517T191324_result.json`
- **Structured JSON:** [`054ce93c3dcef9c9f98a.json`](../../sessions/05/054ce93c3dcef9c9f98a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== RSA Rise Phase Bootstrap CI ===

Note: L0 is NaN for last_preaction (no action tokens at embedding layer). Using L1 as start.

Trained last_preaction:
  L1:  ρ = 0.5682, L12: ρ = 0.6425
  Δρ = 0.0743, 95% CI [0.0486, 0.0995], p < 0.0001

Untrained last_preaction:
  L1:  ρ = 0.6262, L12: ρ = 0.5953
  Δρ = -0.0309, 95% CI [-0.0419, -0.0215], p < 0.0001

Trained vs Untrained rise difference:
  Trained rise:   +0.0743
  Untrained rise: -0.0309
  Difference:      0.1052, 95% CI [0.0783, 0.1331], p < 0.0001
```

Method: Paired bootstrap (10,000 resamples) over 10 tasks. Per-task Δρ = ρ(L12) - ρ(L1) resampled with replacement.

Key findings:
- **Trained**: significant rise from L1→L12 (all 10 tasks show positive delta), CI excludes 0
- **Untrained**: significant *decline* from L1→L12 (all 10 tasks show negative delta)
- The trained-vs-untrained rise difference (0.105) is strongly significant, confirming the L1→L12 rise is training-dependent

---
