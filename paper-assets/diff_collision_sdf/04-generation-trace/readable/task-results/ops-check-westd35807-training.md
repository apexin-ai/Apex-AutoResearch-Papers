# ops check westd35807 training

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_westd35807_training_20260522T094133_result.json`
- **Structured JSON:** [`da4d0d542272fc1f53e6.json`](../../sessions/da/da4d0d542272fc1f53e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个进程全部存活。汇总如下：

| 实验 | GPU | Step / 30000 | 进度% | Loss | LR | 运行时长 | 状态 |
|------|-----|-------------|-------|------|-----|---------|------|
| baseline_lora_spatial_bowl_s0 | cuda:1 | 28057 / 30000 | **93.5%** | 0.0165 | 2.75e-06 | 1d 7h 30m | 运行中 |
| baseline_lora_object_pudding_s0 | cuda:3 | 28008 / 30000 | **93.4%** | 0.0202 | 2.76e-06 | 1d 7h 30m | 运行中 |
| a1_lora_object_pudding_s0 | cuda:2 | 26408 / 30000 | **88.0%** | 0.0187 | 3.34e-06 | 1d 4h 59m | 运行中 |
| a1_lora_spatial_bowl_s0 | cuda:0 | 24404 / 30000 | **81.3%** | 0.0235 | 4.51e-06 | 1d 2h 53m | 运行中 |

**GPU 利用率：**

| GPU | 利用率 | 显存占用 |
|-----|--------|---------|
| cuda:0 | 100% | 23.9 / 97.9 GB |
| cuda:1 | 100% | 23.9 / 97.9 GB |
| cuda:2 | 100% | 23.9 / 97.9 GB |
| cuda:3 | 100% | 23.9 / 97.9 GB |

按 ~4s/step 估算剩余时间：baseline 两组约 **2h 10m** 完成，a1_obj 约 **4h**，a1_spa 约 **6h 15m**。

---
