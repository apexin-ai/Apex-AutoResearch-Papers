# ops check gpu status 19828

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-gpu-status-19828_20260522T050828_result.json`
- **Structured JSON:** [`8a32c8ae6fb1bfe8c261.json`](../../sessions/8a/8a32c8ae6fb1bfe8c261.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### GPU 状态

| GPU | 利用率 | 显存占用 |
|-----|--------|----------|
| cuda:0 | 66% | 14,689 / 97,887 MiB |
| cuda:1 | 71% | 14,689 / 97,887 MiB |

### 实验进程

| 实验 | PID | 状态 | 运行时长 | 进度 | 完成? |
|------|-----|------|----------|------|-------|
| t25_a075_s43_fp32 | 731312 | Running (Rl) | 55min | gen_11 正在训练 (已完成 gen_0–10, 共11个有 metrics.json) | 未完成 — 目标 25 gens, 从 gen_9 开始, 还需到 gen_24 |
| t10_a050_s43_fp32 | 731717 | Running (Rl+) | 50min | gen_8 正在训练 (已完成 gen_0–7, 共8个有 metrics.json) | 未完成 — 目标 10 gens, 从 gen_6 开始, 还需到 gen_9 |

### 进度细节

- **t25_a075_s43_v3**: gen_0–11 目录已存在，gen_0–10 有 metrics.json（gen_11 正在训练中）。从 gen_9 启动，需跑到 gen_24，当前完成 2/16 新 gens。
- **t10_a050_s43_v2**: gen_0–8 目录已存在，gen_0–7 有 metrics.json（gen_8 正在训练中）。从 gen_6 启动，需跑到 gen_9，当前完成 2/4 新 gens。

两个实验均在正常运行中，GPU 负载健康。t10_a050_s43 预计很快完成（还剩 ~1 gen），t25_a075_s43 还需较长时间（剩余 ~13 gens）。

---
