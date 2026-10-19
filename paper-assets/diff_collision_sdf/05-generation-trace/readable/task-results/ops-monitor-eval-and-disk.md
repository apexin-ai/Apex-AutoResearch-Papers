# ops monitor eval and disk

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_monitor_eval_and_disk_20260521T235454_result.json`
- **Structured JSON:** [`bc15b0db365a4f61e8c2.json`](../../sessions/bc/bc15b0db365a4f61e8c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. Eval 进度（westd-45947）

**进程存活**，PID 263983，已运行 3h02m。

| Task | 描述 | TSR | CAR | 状态 |
|------|------|-----|-----|------|
| 0 | (spatial?) | 0.0% | 96.0% | 已完成 50/50 |
| 1 | pick chocolate pudding → basket | 0.0% | 22.0% | 已完成 50/50 |
| 2 | pick milk → basket | — | — | 进行中，30/50 episodes |

当前在 Task 2 的 Episode 30/50。每 10 episodes 约 14 分钟，预计 Task 2 还需 ~28 分钟完成。TSR 全是 0%，Task 0 安全性好（CAR 96%），Task 1 碰撞严重（CAR 22%）。

### 2. westd-35807 磁盘

| 指标 | 值 |
|------|---|
| 总容量 | 350G |
| 已用 | 260G (75%) |
| 可用 | 91G |

Checkpoint 目录：

| 目录 | 大小 |
|------|------|
| baseline_object_pudding | 76G |
| baseline_spatial_bowl | 76G |
| a1_sdf_spatial_bowl | 47G |
| a1_sdf_object_pudding | 41G |
| **合计** | **240G** |

### 3. 四个训练当前 step（westd-35807）

| 训练 | Step | 进度 | Loss |
|------|------|------|------|
| baseline_lora_spa_s0 | 19,344 / 30,000 | 64% | 0.013 |
| baseline_lora_obj_s0 | 19,306 / 30,000 | 64% | 0.013 |
| a1_lora_spa_s0 | 15,813 / 30,000 | 53% | 0.028 |
| a1_lora_obj_s0 | 17,703 / 30,000 | 59% | 0.024 |

四个训练均正常运行，~4s/step。baseline 两组进度一致（64%），a1 两组稍慢（53%-59%）。按当前速度，baseline 预计还需 ~12h，a1_spa ~16h，a1_obj ~14h 完成。

---
