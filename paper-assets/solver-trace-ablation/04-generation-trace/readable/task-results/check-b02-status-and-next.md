# check b02 status and next

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_b02-status-and-next_20260516T043213_result.json`
- **Structured JSON:** [`0f5c8e3d6b2a959e788e.json`](../../sessions/0f/0f5c8e3d6b2a959e788e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验正常运行中，未完成。

**状态报告：**

| 实验 | 当前 step | GPU | 速率 | 预计剩余 |
|------|----------|-----|------|---------|
| sweep-isr-b02-s42 | 164/500 | cuda:1 (80GB used, 91%) | ~8s/step | ~45 min |
| sweep-isr-b02-s43 | 143/500 | cuda:0 (85GB used, 100%) | ~9.2s/step | ~55 min |

**s42 观察**: 164 步中有 80 步 prove_rate=0（49%）。这在 batch_size=1 × 4 generations 下是正常噪声——单问题如果模型没做对就是 0%。step 161 恢复到 prove_rate=0.375, isr_mean=0.28，无崩塌迹象。

**s43 观察**: step 142 prove_rate=0.75, isr_mean=0.28, step 140-141 prove_rate=1.0。看起来比 s42 更稳定。

**两个 GPU 都被占满，无法提交新实验。** 预计 ~55 分钟后两个 GPU 释放。建议到时再检查并提交 sweep-isr-b02-s44。

---
