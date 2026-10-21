# ssh urgent gpu status all

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_gpu_status_all_20260521T081626_result.json`
- **Structured JSON:** [`5a5a231ca734490693b8.json`](../../sessions/5a/5a5a231ca734490693b8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| 服务器 | GPU | 预期实验 | 预期PID | alive/dead | 实际进程 | VRAM | GPU利用率 | 运行时长 |
|--------|-----|----------|---------|------------|----------|------|-----------|----------|
| westd-35807 | 0 | a1_lora_spatial_bowl | 299910 | **alive** | train_a1_sdf_aux --scene spatial_bowl | 16864/97887 MiB | 100% | 1h27m |
| westd-35807 | 1 | baseline_lora_spatial_bowl | 281554 | **alive** | train_baseline --scene spatial_bowl | 23884/97887 MiB | 100% | 6h04m |
| westd-35807 | 2 | a1_lora_object_pudding | 292258 | **alive** | train_a1_sdf_aux --scene object_pudding | 16864/97887 MiB | **0%** | 3h33m |
| westd-35807 | 3 | baseline_lora_object_pudding | 281629 | **alive** | train_baseline --scene object_pudding | 23884/97887 MiB | 100% | 6h04m |
| westd-45947 | 0 | a3_spatial | 143451 | **DEAD** | — | 0/97887 MiB | 0% | — |
| westd-45947 | 1 | a3_object | 143525 | **DEAD** | — | 0/97887 MiB | 0% | — |

**异常：**
1. **westd-45947 两张卡全挂** — PID 143451 和 143525 均已不存在，GPU 完全空闲，无任何进程。
2. **westd-35807 GPU 2 利用率 0%** — PID 292258 进程存活且占用 16.8GB VRAM，但 GPU utilization 报 0%。可能处于数据加载/checkpoint 保存阶段，或卡住。值得关注。

---
