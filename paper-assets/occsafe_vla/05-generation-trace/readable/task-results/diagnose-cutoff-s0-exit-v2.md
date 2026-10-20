# diagnose cutoff s0 exit v2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_cutoff-s0-exit-v2_20260522T140430_result.json`
- **Structured JSON:** [`018e691582087c84086b.json`](../../sessions/01/018e691582087c84086b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：实验正常运行中 (still-running)**

- **进程状态**: PID 137021 存活，运行时间 5h55m，状态 Ssl（正常）
- **GPU 占用**: cuda:0 上占用 62194 MiB
- **当前进度**: step 17627/50005 (35%), ~1.05 it/s
- **最新 loss**: step 17600 — occ_loss=0.0096, action_loss=0.1357
- **最新 checkpoint**: `10000_chkpt`（预期下一个 checkpoint 在 step 20000）
- **预计剩余**: ~8.5 小时

Cron 报告的进程退出是**误报**。PID 137021 从未退出，日志显示训练持续推进，step 15700 附近和 17568 附近各有一次短暂减速（可能是 checkpoint 保存或 IO 抖动），但随后恢复正常速度。

---
