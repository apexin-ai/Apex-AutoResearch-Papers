# ssh verify phi4 eval alive

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify-phi4-eval-alive_20260519T070708_result.json`
- **Structured JSON:** [`d0a3556b98907a10c828.json`](../../sessions/d0/d0a3556b98907a10c828.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

- **PID 118080**: 存活，cuda:3 上运行中
- **cuda:3 VRAM**: 31706 MiB / 97887 MiB，GPU-Util 99%，功耗 602W/600W（满载）
- **当前进度**: MMLU eval，6026/14042（约 43%），速度 ~9 it/s，预计剩余 ~15 分钟

日志显示正在跑 MMLU benchmark，尚未看到 dosage 级别信息（d005/d025/d050）。这是单个 benchmark 内的进度，MMLU 完成后会继续下一个 dosage 或 benchmark。

---
