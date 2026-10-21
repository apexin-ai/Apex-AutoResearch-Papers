# signals exp 002 signals 05B s123 v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_signals_exp_002_signals_05B_s123_v2_20260516T030400_result.json`
- **Structured JSON:** [`eb7aa4be59473a756a2e.json`](../../sessions/eb/eb7aa4be59473a756a2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已确认：

- **GPU 5**: 585 MiB 占用，进程正常运行
- **进度**: [1/12] d000_s123 × mmlu，s1 embedding 编码中（3830/6250 batches，~60%）
- **Registry**: `exp_002_signals_05B_s123_v2` 状态 RUNNING
- **tmux session**: `exp002_05B_s123_v2`
- **日志**: `/root/autodl-tmp/exp002/signals/signals_05B_s123_v2.log`

任务覆盖：4 dose (d000/d005/d025/d100) × 3 benchmark (mmlu/gsm8k/arc_challenge) × all signals (s1/s2/s3/s4) = 12 组合，全部由 `run_05B_s123_signals.sh` 串行执行。0.5B 模型较小，预计总耗时 1-2 小时。

---
