# code libero spatial readiness check

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_libero_spatial_readiness_check_20260517T080757_result.json`
- **Structured JSON:** [`b0c9f17468befcfd669c.json`](../../sessions/b0/b0c9f17468befcfd669c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## LIBERO-Spatial 实验准备状态：已完成

**所有实验已经跑完，无需额外准备。**

### 1. 数据
- **路径**: `/root/autodl-tmp/vla-ssd/data/libero/libero_spatial/` (5.9G)
- **10 个 task**，每个 task 一个 HDF5 文件（~500MB-750MB）
- 全部为 "pick up the black bowl [spatial description] and place it on the plate" 变体

### 2. 特征提取
- **trained**: `/root/autodl-tmp/vla-ssd/features/trained_libero_spatial/` (24G, 10 tasks)
- **untrained**: `/root/autodl-tmp/vla-ssd/features/untrained_libero_spatial/` (25G, 10 tasks)

### 3. Action Probe 结果（已完成，5/16 14:44）
保存于 `results/functional_validation/action_probe_libero_spatial.json`

| Condition | Agg | Best Layer | R² |
|---|---|---|---|
| trained | image_mean | L13 | 0.6963 |
| trained | last_preaction | L21 | 0.6748 |
| untrained | image_mean | L0 | 0.6732 |
| untrained | last_preaction | L1 | 0.6348 |

Bootstrap 对比均显著 (p < 0.001)。

### 4. RSA 结果（已完成，5/16 14:33）
保存于 `results/rsa/rsa_libero_spatial.json`

| Condition | Agg | Best Layer | RSA |
|---|---|---|---|
| trained | image_mean | L14 | 0.6911 |
| trained | last_preaction | L15 | 0.6945 |
| untrained | image_mean | L0 | 0.6523 |
| untrained | last_preaction | L1 | 0.6659 |

### 5. 磁盘
- 总量 250G，已用 192G，剩余 **59G**
- vla-ssd 目录占 179G

### 结论
Action probe 和 RSA 分析均已完成，结果 JSON 已存在。可直接进入下游分析/画图阶段，无需额外 GPU 时间。

---
