# analysis reverse cutoff s2 v2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_reverse_cutoff_s2_v2_20260526T232225_result.json`
- **Structured JSON:** [`2122b1f8fcd54f832fba.json`](../../sessions/21/2122b1f8fcd54f832fba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练状态
- 完成步数: **50005 / 50005**
- 最终 action loss: **0.0610**
- 最终 occ loss: **0.0095**
- 正常结束: **Yes** (EXIT_CODE=0, "Max step 50005 reached!")

## Checkpoint
- 路径: `/root/autodl-tmp/checkpoints/reverse_cutoff_s2_v2/`
- 保存的 checkpoints: **30000, 40000, 50000**
- 最新 checkpoint: `step-50000` (merged model, 保存于 05/27 07:18)
- 总大小: **45 GB**

## 对比参考
| 实验 | CAR | TSR | action loss | occ loss |
|------|-----|-----|-------------|----------|
| reverse_cutoff_s0 | **0.700** | 0.788 | 0.0481 | 0.0083 |
| reverse_cutoff_s1 | **0.736** | 0.890 | - | - |
| reverse_cutoff_s2_v2 | 待评估 | 待评估 | 0.0610 | 0.0095 |

## 备注
- s2_v2 的 action loss (0.0610) 和 occ loss (0.0095) 均高于 s0 (0.0481 / 0.0083)，seed 不同所致的差异，需评估后看实际 CAR/TSR
- 训练耗时约 14h15m，速度 ~1.07 it/s
- 50000 步 checkpoint 已含 merged model，可直接用于评估

---
