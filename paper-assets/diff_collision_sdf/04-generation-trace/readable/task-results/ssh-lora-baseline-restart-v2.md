# ssh lora baseline restart v2

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_lora_baseline_restart_v2_20260521T021014_result.json`
- **Structured JSON:** [`f2acf018304827f27f40.json`](../../sessions/f2/f2acf018304827f27f40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常进行，两个实验都在 step 6 左右，速度约 5 s/it。checkpoint 目录中尚未出现独立的 LoRA 目录（因为还没到 step 2000）。

汇报：

### 结果

| 项目 | 状态 |
|------|------|
| **Kill 确认** | PID 263726、263799 已 SIGTERM 成功 |
| **新 PID** | spatial_bowl: **281554** (cuda:1), object_pudding: **281629** (cuda:3) |
| **GPU 占用** | 各 23893 MiB / 100% 利用率（LoRA 比 full-FT 35747 MiB 少约 1/3，符合预期） |
| **Checkpoint 目录** | 当前仅有 `baseline_spatial_bowl` 和 `baseline_object_pudding`（full-FT 的），新的 `baseline_lora_*_seed0` 目录将在 step 2000 首次保存时创建 |
| **训练进度** | 两个实验均在 step 6，loss ~0.19-0.27，lr 正常 warmup，约 5 s/step，预计 step 2000 在 ~2.8h 后 |

**关键修正**：原指令用了 `conda activate base`，实际环境应为 `conda activate libero`，并需加 `WANDB_MODE=disabled`。已修正重启。

---
