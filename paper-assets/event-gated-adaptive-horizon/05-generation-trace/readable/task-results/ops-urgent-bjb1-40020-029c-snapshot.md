# ops urgent bjb1 40020 029c snapshot

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_bjb1_40020_029c_snapshot_20260520T165101_result.json`
- **Structured JSON:** [`6cd8bce02738a02861d1.json`](../../sessions/6c/6cd8bce02738a02861d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== exp_029c (σ=0.1 s0) ===
PID 59395: running (uptime 5h08m)
当前 step: 148K/210K (~70%)

eval_return 最新 5 点:
  step=105K: 204.7
  step=115K: 296.4
  step=125K: 232.3
  step=135K: 247.4
  step=145K: 323.1  ← 新高

ve_ratio 最新 5 点:
  step=105K: 0.7610
  step=115K: 0.4514
  step=125K: 0.4899
  step=135K: 0.3995
  step=145K: 0.2667

NVE peak: 1.0218 @ step 95K（已回落）

=== GPU ===
cuda:0: 18% util — PID 59400 (python, 3025 MiB)  ← exp_029c
cuda:1:  0% util — 空闲 ✓ (1 MiB, exp_029a PID 50924 已退出)
```

---
