# analysis exp 086 frozen dt emb cheetah s0

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_086_frozen_dt_emb_cheetah_s0_20260525T202026_result.json`
- **Structured JSON:** [`bb3057146c937e019485.json`](../../sessions/bb/bb3057146c937e019485.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## exp_086 Results

**conclusion: SUCCESS**

Frozen dt_emb on Cheetah s0 does NOT trigger CIVO. Hypothesis confirmed.

### Metrics

| Metric | Value |
|--------|-------|
| NVE | **0.27** |
| ve_ratio_peak | 0.2 (at 105K) |
| eval_return_peak | 326.4 (at 35K) |
| eval_return_105K | 53.3 |
| civo_alert | 0.0 (never triggered) |
| total_steps | 105K |
| gate_dt_mean | 2.0 (locked) |

### eval_return trajectory
5K=8.3, 15K=222.8, 25K=245.2, **35K=326.4**, 45K=153.3, 55K=151.7, 65K=154.6, 75K=144.1, 85K=188.8, 95K=121.0, 105K=53.3

### ve_ratio trajectory
15K=0.0, 25K=0.0, 35K=0.0, 45K=0.1, 55K=0.1, 65K=0.1, 75K=0.1, 85K=0.1, 95K=0.1, 105K=0.2

### Key comparison

| | exp_086 (frozen s0) | exp_078 (trained s0) | exp_087 (frozen s1) |
|---|---|---|---|
| NVE | 0.27 | 4.1 | 0.33 |
| CIVO | No | Yes | No |

### Paths
- **checkpoint_path**: `/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_086_frozen_dt_emb_cheetah_s0/latest.pt`
- **log_path**: `/root/runs/event-gated-adaptive-horizon/exp_086_frozen_dt_emb_cheetah_s0.log`

Note: performance degrades significantly (326→53) but this is policy collapse (actor_entropy→-1.1), not CIVO — ve_ratio stays flat at 0.1-0.2.

---
