# check recovery datagen progress

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_recovery-datagen-progress_20260515T151757_result.json`
- **Structured JSON:** [`33f777f6320c0c630e85.json`](../../sessions/33/33f777f6320c0c630e85.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 1. Recovery-paired datagen (PID 158010)
- **状态**: 存活，已运行 1h12m
- **进度**: 100/760 (13.2%)
- **输出文件**: 尚未生成（`data/recovery_paired/` 目录不存在），可能攒够批次后写入
- **预计剩余**: 按当前速率 (~1.4 条/min)，剩余 660 条约需 **~8 小时**
- **GPU**: 未占用 GPU，纯 CPU 运行

### 2. GPU 状态

| GPU | 显存占用 | 利用率 | 任务 |
|-----|---------|--------|------|
| cuda:0 | 0 MiB / 32G | 0% | **空闲** |
| cuda:1 | 0 MiB / 32G | 0% | **空闲** |
| cuda:2 | 19.5G / 32G | 85% | SFT v4 seed1 训练 (PID 155352) |
| cuda:3 | 19.5G / 32G | 91% | SFT v4 seed7 训练 (PID 155559) |

### 3. Eval 状态
两个 vanilla eval **均已完成**，cuda:0/1 已释放：

| Eval | 结果 | Success Rate | 完成时间 |
|------|------|-------------|---------|
| v4-vanilla-seed1 | ✅ 完成 | **0.660** (31/47) | 23:03 |
| v4-vanilla-seed7 | ✅ 完成 | **0.745** (35/47) | 23:06 |

---
