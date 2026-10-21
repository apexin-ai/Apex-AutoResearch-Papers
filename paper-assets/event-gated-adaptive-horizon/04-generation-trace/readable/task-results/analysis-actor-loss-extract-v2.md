# analysis actor loss extract v2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_actor_loss_extract_v2_20260515T103340_result.json`
- **Structured JSON:** [`6ed96768e66c13e7266c.json`](../../sessions/6e/6ed96768e66c13e7266c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both files saved with identical content. Summary:

| Experiment | Steps | Range | Zero-crossing |
|---|---|---|---|
| **008d_s0** | 6 pts (5K-55K) | -0.337 → -0.073 | Never (stopped early, collapse) |
| **009b_s2** | 11 pts (5K-105K) | -0.339 → +0.002 | ~75K (self-correction) |
| **009e_s1** | 10 pts (5K-95K) | -0.337 → +0.004 | ~85K (oscillatory) |

Note: 009e steps 5K-55K share identical actor_loss values with 008d — 009e is a same-seed continuation/re-run of 008d's config that extended past its 55K stopping point.

The `actor_loss_data.json` is placed where `fig2_nve_trajectory.py` expects it, so the bottom panel of Fig 2 can now render.

---
