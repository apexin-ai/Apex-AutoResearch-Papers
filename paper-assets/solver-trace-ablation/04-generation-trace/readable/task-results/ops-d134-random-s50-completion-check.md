# ops d134 random s50 completion check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d134-random-s50-completion-check_20260518T234244_result.json`
- **Structured JSON:** [`53a03de0ade284f95662.json`](../../sessions/53/53a03de0ade284f95662.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结构化摘要

**d134-4b-random-b01-s50**
- **Train**: 完成 500/500 步，~1h41m
  - final prove_rate=0.656, mean_isr=0.094, parse_rate=1.0
- **Eval**: 进行中（7/100），PID 217113，使用正确数据 `proofwriter_fol_100.jsonl`
- **Classify**: 未开始（等 eval 完成后 pipeline v2 自动启动）
- **Registry**: 保持 RUNNING，等 eval+classify 全部完成后更新
- **Cron**: 已删除

**d134-4b-random-b01-s51**: 未启动（目录不存在）

**GPU**: 1 个进程占用 16432 MiB（eval 进程）
**磁盘**: 56G/250G used (23%)，充足

eval 每题约 11s，剩余 93 题预计约 17 分钟完成，之后 pipeline 会自动跑 classify。需要后续检查 eval+classify 结果并更新 registry。

---
