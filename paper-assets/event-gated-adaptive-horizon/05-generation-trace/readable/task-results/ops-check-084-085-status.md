# ops check 084 085 status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_084_085_status_20260525T162524_result.json`
- **Structured JSON:** [`17d610d72894aa487e96.json`](../../sessions/17/17d610d72894aa487e96.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已修复。汇总：

## 结果

| 实验 | PID | 状态 | 运行时间 | GPU | VRAM | Registry |
|------|-----|------|---------|-----|------|----------|
| exp_084 (seed=0) | 296484 | 运行中 | ~8h20m | GPU 0, 15% util | 3.8GB/98GB | PREPARING → RUNNING ✓ |
| exp_085 (seed=1) | 296781 | 运行中 | ~8h11m | GPU 1, 30% util | 2.8GB/98GB | PREPARING → RUNNING ✓ |

**日志最新状态**（均在 step 8000）：
- exp_084: train_return 29.6~55.1, gate_dt_mean=2.0, gate_dt_2_frac=1.0
- exp_085: train_return 30.1~101.7, gate_dt_mean=2.0, gate_dt_2_frac=1.0

gate_dt 始终锁定在 2.0（100% dt=2），符合 frozen dt_emb 不触发 CIVO 的预期。

---
