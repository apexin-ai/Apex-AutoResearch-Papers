# fix disk full emergency

**Meta-Brain: Perturbation-Diagnostic Routing of LoRA Experts for Parameter-E cient VLA Robustness** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_disk_full_emergency_20260516T132153_result.json`
- **Structured JSON:** [`8030b80467fa3e11d698.json`](../../sessions/80/8030b80467fa3e11d698.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

---

## 结果

### 磁盘状态 (before → after)
| 分区 | Before | After |
|------|--------|-------|
| `/root` (根) | 90% (27G/30G, 3.1G free) | **86% (26G/30G, 4.3G free)** |
| `/root/autodl-tmp` (数据盘) | 31% (76G/250G) | 31% (76G/250G) |

释放约 1.2G（v1 checkpoints ~991M + v2 移动 ~186M）。

### Checkpoint 操作
- **移动到数据盘** (+ symlink): `v2_lora_visual_r16`, `v2_lora_physical_r16`, `v2_lora_spatial_r16`, `v2_lora_universal_r16`
- **删除** (v1 已作废): `lora_visual_r16`, `lora_physical_r16`, `lora_spatial_r16`, `lora_universal_r16`, `lora_universal_r48`
- **删除不完整**: `v2_lora_spatial_r16/step_2000`（保存时磁盘满导致损坏）

### 存活训练进程
| 任务 | GPU | 状态 |
|------|-----|------|
| visual | GPU 2 | ✅ 运行中 |
| physical | GPU 3 | ✅ 运行中 |
| universal | GPU 1 | ✅ 运行中 |
| spatial (重启) | GPU 0 | ✅ 从 step=0 重新开始 |

4 张 GPU 全部 99% 利用率，训练正常进行。所有新 checkpoint 将写入数据盘，根分区不会再被填满。

---
