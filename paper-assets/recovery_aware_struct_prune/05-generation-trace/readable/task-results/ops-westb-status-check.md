# ops westb status check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb-status-check_20260516T014303_result.json`
- **Structured JSON:** [`91aff7c14b9c4fd1c7ce.json`](../../sessions/91/91aff7c14b9c4fd1c7ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态汇总

### GPU 状态
| GPU | 型号 | 显存占用 | 利用率 |
|-----|------|---------|--------|
| cuda:0 | RTX PRO 6000 Blackwell | 71.7/97.9 GB | 100% |
| cuda:1 | RTX PRO 6000 Blackwell | 71.7/97.9 GB | 100% |

### RASP GRPO v9 (PID 566666, cuda:0)
- **状态**: 运行中，已运行 1h39m
- **当前 step**: 10 / 30 (33%)
- **每 step 耗时**: ~401 秒 (~6.7 分钟)
- **预计剩余**: ~20 steps × 6.7 min ≈ **2h14m**
- **已保存 checkpoints**: checkpoint-5, checkpoint-10
- **关键指标** (step 10):
  - reward: 0.015, reward_std: 0.057
  - KL: 0.00074
  - loss: 0.0069
  - clipped_ratio: 95.6% (生成大量被截断)
  - frac_reward_zero_std: 87.5%
  - mean_length: 991 / max 1024

### Standard v8 (PID 534667, cuda:1)
- **状态**: 运行中，已运行 11h00m

### 磁盘
- /root/autodl-tmp: 126G/250G 已用，剩余 125G (51%)，充足

### 注意
- v9 的 `completions/clipped_ratio` 高达 95.6%，绝大多数生成都撞到 max_length=1024 被截断，mean_terminated_length 仅 131 token。reward 极低 (0.015)，frac_reward_zero_std=87.5% 表明大部分 batch 内 reward 无方差。这可能导致 GRPO 学习信号不足。

---
