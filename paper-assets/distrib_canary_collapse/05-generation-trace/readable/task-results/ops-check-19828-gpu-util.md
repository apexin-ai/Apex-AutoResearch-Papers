# ops check 19828 gpu util

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-19828-gpu-util_20260522T144728_result.json`
- **Structured JSON:** [`351ae6267121878989fc.json`](../../sessions/35/351ae6267121878989fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

第二次采样 GPU1 跳到 96%，确认是正常波动。

## 汇报

| 项目 | GPU0: scale_14b_t15_a075_s42 | GPU1: t10_a050_s42_fp32_14b |
|------|------|------|
| **进程** | PID 793171 ✅ 存活，运行 2h10m | PID 776064 ✅ 存活，运行 5h42m |
| **GPU 利用率** | 66-81%（正常） | 0-96%（波动大但正常，训练/生成交替） |
| **显存占用** | 31.5 GB / 97.9 GB | 32.4 GB / 97.9 GB |
| **Generation 进度** | gen_0 ~ gen_2（共需 15 gen） | gen_0 ~ gen_7（共需 10 gen，从 gen_2 开始） |
| **磁盘** | 130G/250G used (52%) | 同左 |

两个实验运行正常。GPU 利用率波动是因为 iterative training 在训练和文本生成阶段交替（生成阶段是 autoregressive decoding，利用率会短暂降低或跳变）。磁盘剩余 121G，暂无压力。

---
