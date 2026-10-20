# ops gpu status check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-status-check_20260515T210741_result.json`
- **Structured JSON:** [`71afda8c09f7282cc5b6.json`](../../sessions/71/71afda8c09f7282cc5b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都确认在跑，资源检查工具误报。

## 检查结果

### 实验 1: deepseek_full_trace_seed42_v3
- **状态**: RUNNING (确认)
- **GPU**: cuda:1, 22414 MiB
- **进度**: 36/444 步 (8%), ~16.35s/step
- **已运行**: ~11 分钟（进程近期才启动，可能是重新提交的）
- **预计剩余**: ~1h 51m
- **日志**: `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_seed42_v3.log`

### 实验 2: deepseek_exception_only_seed456
- **状态**: RUNNING (确认)
- **GPU**: cuda:0, 22386 MiB
- **进度**: 197/444 步 (44%), ~12.78s/step
- **已运行**: ~46 分钟，已通过 step 148 的 eval checkpoint
- **预计剩余**: ~52 分钟
- **日志**: `/root/runs/trace-verdict-study/deepseek_exception_only_seed456.log`

### 磁盘
- `/` 80% (6.2GB free) — 偏紧但够用
- `/root/autodl-tmp/` 40% (151GB free) — 充足

两个实验 registry 状态已经是 RUNNING，无需更新。GPU 实际占用 2 张，资源检查工具报 0 是误报。

---
