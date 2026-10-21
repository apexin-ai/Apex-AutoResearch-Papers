# monitor scienceworld sft progress

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_scienceworld_sft_progress_20260519T161338_result.json`
- **Structured JSON:** [`fc3a21476ffc0ad326f7.json`](../../sessions/fc/fc3a21476ffc0ad326f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## ScienceWorld SFT 训练进度

| 项目 | 值 |
|------|-----|
| PID | 120838 ✅ 运行中，已运行 1h23m |
| 当前 step | **224 / 448**（epoch 1 刚完成，50%） |
| 最新 loss | 0.0126（step 224），近 100 步在 0.004~0.026 区间波动 |
| 学习率 | 2.70e-6（cosine 衰减中，初始 5e-6） |
| 每步耗时 | ~21.3s |
| 预估剩余 | 224 steps × 21.3s ≈ **1h20m**（预计完成时间约 01:40 UTC） |

训练正常推进，epoch 1 结束，loss 已收敛到较低水平。checkpoint 应在 step 224（刚过）和 step 336、448 保存。

---
