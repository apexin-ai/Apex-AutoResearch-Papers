# ops check s42 checkpoint

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-s42-checkpoint_20260515T010759_result.json`
- **Structured JSON:** [`d42a0d3cc49e3402d7f5.json`](../../sessions/d4/d42a0d3cc49e3402d7f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**Checkpoint 存在状态：**

| 实验 | 路径 | 状态 |
|------|------|------|
| ISR β=0.3 s42 (plan002) | `/root/autodl-tmp/outputs/plan002_additive_beta03_s42/` | **MISSING** |
| Random β=0.3 s42 (plan017) | `/root/autodl-tmp/outputs/plan017_additive_random_s42/` | **MISSING** |

服务器上当前存在的 checkpoints：
- `exp1_isr_b03_s44_r2/checkpoint-500`
- `exp1_random_b03_s44/checkpoint-100`
- `exp1_random_b03_s44_r2/checkpoint-150`

**exp1-random-b03-s44-r2 训练进度：**
- 当前 step: **156**（checkpoint 在 150）
- prove_rate: 0.875
- isr_mean: 0.184
- parse_rate: 1.0

plan002 和 plan017 的 s42 checkpoints 不在该服务器上（可能已被清理或从未在此训练）。

---
