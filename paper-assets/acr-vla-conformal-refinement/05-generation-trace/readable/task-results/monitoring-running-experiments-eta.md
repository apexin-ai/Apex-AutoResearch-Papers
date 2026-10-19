# monitoring running experiments eta

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitoring_running-experiments-eta_20260514T020932_result.json`
- **Structured JSON:** [`d092c5b956c10153edc3.json`](../../sessions/d0/d092c5b956c10153edc3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度报告

| 实验 | 服务器 | 进度 | 预计剩余 | 状态 | 备注 |
|------|--------|------|----------|------|------|
| **crm-train-k5** | bjb1-18228 | epoch 10/50 (20%) | ~1.9h | ✅ 正常 | val_loss=0.0119 (epoch 8 best), loss 稳步下降 |
| **eval-acr-spatial-v2** ⭐ | bjb1-18228 | 2/10 tasks (20%) | ~9-10h | ✅ 正常 | task1: 40%, task2: 70%, 正在跑 task3 |
| **eval-reconvla-spatial-v3** | bjb1-18228 | 2.5/10 tasks (25%) | ~7-8h | ✅ 正常 | task1: 60%, task2: 100%, task3 rollout 5/10 |
| **crm-train-a4-scalar-unc** | bjb1-18228 | epoch 48/50 (96%) | **~7min** | ✅ 即将完成 | val_loss=0.0084, 已收敛 |
| **eval-object-v8-full** | bjb2-40593 | 6.5/10 tasks (65%) | ~1.1h | ✅ 正常 | 6 tasks 完成, 正在跑 task7 (butter) |

### 关键观察

- **crm-train-a4-scalar-unc** 几分钟内就会完成，val_loss 在 0.0084 已充分收敛。
- **eval-object-v8-full** 约 1 小时完成，但注意是 **vla_only 模式**（无 CRM），成功率很低：0%, 0%, 20%, 30%, 0%, 10%（前 6 个 task 均值 10%）。
- **eval-acr-spatial-v2** 和 **eval-reconvla-spatial-v3** 还需较长时间（7-10h），两个 eval 在同一台 4×4090 上并行跑。reconvla 的 task2 成功率 100% 是亮点。
- **crm-train-k5** 正常推进，约 2 小时后完成。
- 所有 5 个实验进程均存活，无报错。

---
