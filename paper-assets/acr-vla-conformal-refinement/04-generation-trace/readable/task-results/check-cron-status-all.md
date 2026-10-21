# check cron status all

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cron-status-all_20260524T145853_result.json`
- **Structured JSON:** [`ab0721538ba2141e4f42.json`](../../sessions/ab/ab0721538ba2141e4f42.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### 1. train-crm-pi05-unified-3suite-r2 (bjb1-18228, PID 326310)
- **进程**: 存活，已运行 4h23m
- **进度**: Epoch 12/50 (24%)，batch 600/684，train_loss≈0.009，val_loss=0.006
- **GPU**: GPU0 — 9% util, 580 MiB（batch 间歇低利用率正常）

### 2. eval-supp-spatial-reconvla-s47 (bjb2-40593, PID 261844)
- **进程**: 存活，已运行 4h15m
- **进度**: 无日志文件（runs 目录无对应 log，可能直接启动未重定向）
- **GPU**: GPU0 — 20% util, 2263 MiB

### 3. eval-supp-long-adapt-tau025-s47-r2 (bjb1-32546, PID 433348)
- **进程**: 存活，已运行 2h49m
- **进度**: 无日志文件（runs 目录无对应 log）
- **GPU**: GPU1 — 24% util, 3027 MiB

### 4. precompute-pi05-long-2048-r2 (bjb1-18228, PID 114507)
- **进程**: 存活，已运行 1d18h41m
- **进度**: 旧日志 `precompute-pi05-long-bjb1-18228.log` 显示到 15400/136090 (11.3%) 后 **Terminated (EXIT_CODE=143)**。当前 PID 114507 是重启后的进程，但 runs 目录下没有对应 r2 的日志文件，无法确认当前进度
- **GPU**: GPU3 — 21% util, 9883 MiB（该 GPU 可能被此进程使用）

### 异常项
- 实验 2、3、4 均无可追踪日志，可能是直接 nohup 启动未重定向到 runs 目录。建议确认日志输出位置。

---
