# recovery cuda1 008e v3 s2 and 009e

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_recovery_cuda1-008e_v3_s2-and-009e_20260515T055709_result.json`
- **Structured JSON:** [`f45e87d378c7d31bec55.json`](../../sessions/f4/f45e87d378c7d31bec55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

---

## 1. exp_008e_v3_walker_s2 — DONE (negative)

**Delusional critic collapse at 85K→105K，即使 gate_dt=1 locked。**

| Step | eval | value | v/e | nve |
|------|------|-------|-----|-----|
| 85K | **715.2** (peak) | 339.3 | 0.474 | 0.68x |
| 95K | 452.4 | 384.4 | 0.850 | **1.34x** |
| 105K | **137.0** | 339.8 | **2.481** | **3.78x** |

Cross-seed comparison (C6 config):
- Seed 0: 869.9@105K, nve=0.80x (healthy)
- Seed 1: 869.9@105K, nve=0.53x (healthy)
- **Seed 2: 137.0@105K, nve=3.78x (catastrophic collapse)**

关键发现：dt=1 imagination 并不能完全阻止 delusional critic。subsample ON 训练数据中的 dt=2 transitions 在某些 seed 下足以触发 value overestimation → collapse。Collapse 是 stochastic（1/3 seeds）。

## 2. Registry 已更新
- 008e_v3_s2: DONE, conclusion=negative, 完整 trajectory + nve 数据

## 3. exp_009e_008d_walker_s1 — RUNNING
- PID: 119108, cuda:1, tmux session `exp_009e_008d_walker_s1`
- Config: 与 008d 完全一致（gate_fixed_dt=2, subsample ON, H=8, seed=1）
- 预计运行 ~5-6h

---
