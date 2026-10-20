# monitor live metrics check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_live-metrics-check_20260515T045604_result.json`
- **Structured JSON:** [`2389283b7504fb0d5fa1.json`](../../sessions/23/2389283b7504fb0d5fa1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_008e_v3_walker_s2
- Current step: **85K/105K** (81%)
- Latest eval_return: **715.21** (seed=1 final=869.9)
- gate_dt_mean: 1.0 (gate collapsed — 100% dt=1, zero entropy)
- PID 43437: **alive** (uptime 4.2h)
- FPS: 6.47 → ETA: **~51min**

## exp_009a_baseline_walker_s2
- Current step: **460K/500K** (92%)
- Latest eval_return: **937.72** @ step 455K (exp_001 final=950.9)
- Recent train_returns @ 460K: 960, 949, 954, 917 — tracking well
- PID 142508: **alive** (uptime 19.4h)
- FPS: 7.33 → ETA: **~1.5h**

## GPU
- cuda:0: 12% util, 4165/97887 MiB
- cuda:1: 21% util, 4167/97887 MiB

Notable: exp_008e gate is fully collapsed to dt=1 (no adaptive horizon behavior). exp_009a baseline seed=2 eval 937.7 is tracking close to seed=1's 950.9 final — looks on pace.

---
