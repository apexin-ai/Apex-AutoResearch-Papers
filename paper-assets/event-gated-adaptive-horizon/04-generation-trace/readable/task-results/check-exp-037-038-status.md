# check exp 037 038 status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_037_038_status_20260521T161323_result.json`
- **Structured JSON:** [`7d95613b0a7cc4a3778d.json`](../../sessions/7d/7d95613b0a7cc4a3778d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均 **ALIVE**，报告已写入 artifacts。

| 实验 | 服务器 | 进度 | 最新 eval_return | 趋势 |
|------|--------|------|-----------------|------|
| exp_037_wide_critic_cheetah | bjb1-45299 | 156K/210K (74%) | 182.4 | eval 下降（286→182），train 上升（93→129），有 train-eval gap |
| exp_038_dual_critic_walker_s2 | bjb1-40020 | 112K/210K (53%) | 283.1 | eval 和 train 同时下降（344→283），value_mean 持续收缩 |

两点值得关注：
1. **exp_037** train_return 上升但 eval_return 下降，可能过拟合
2. **exp_038** value_mean 从 142 降到 92，整体性能在退化

---
