# ssh p0 gpu3 fix and status

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_p0_gpu3_fix_and_status_20260519T230749_result.json`
- **Structured JSON:** [`b834d6fae6ff004460e9.json`](../../sessions/b8/b834d6fae6ff004460e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

A1 训练正常运行。

## 最终结果

### P0: GPU 3 修复 — 完成

| 项目 | 结果 |
|------|------|
| PID 106344 清理 | 已自行退出，无需 kill |
| GPU 3 释放 | 确认（现已被新 A1 占用 13385 MiB） |
| A1 死因 | 日志在 step 160 干净截断，无错误/OOM 信息。dmesg 容器无权限。推测外部 SIGKILL |
| 新 A1 PID | **117514** |
| 前 10 步 loss | 0.27~0.24，符合预期（~0.2 范围） |
| GPU 3 显存 | 13385 MiB / 97887 MiB |
| 配置 | `extra_delta_transform=False`（已正确），`--save_interval 500`，`WANDB_MODE=disabled` |

### P1: Baseline 状态 — 全部正常

| 实验 | PID | 运行时间 | Step | Loss | 日志文件 |
|------|-----|---------|------|------|---------|
| spatial_bowl_s0 | 100319 | 33min | 538 | 0.080 | v3 |
| spatial_bowl_s1 | 94453 | 45min | 742 | 0.084 | v3 |
| object_pudding_s0 | 95429 | 45min | 759 | 0.066 | v3 |

注：Baseline 日志文件实际为 v3 版本（非 v2）。三组训练 loss 均在持续下降，运行正常。

---
