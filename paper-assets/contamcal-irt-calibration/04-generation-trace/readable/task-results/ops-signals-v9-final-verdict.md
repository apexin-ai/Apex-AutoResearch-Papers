# ops signals v9 final verdict

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_signals-v9-final-verdict_20260516T061050_result.json`
- **Structured JSON:** [`cf102a7126e6e2c54164.json`](../../sessions/cf/cf102a7126e6e2c54164.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**exp_002_signals_3B_d100_s123_v9 → SUCCESS**
- mmlu: s1 + s2 + s4_selfcritique (14042 items) ✓
- gsm8k: s1 + s2 + s4_selfcritique (1319 items) + signals_merged ✓
- Registry 已更新为 success

**cuda:4 提交：无法执行**
- PID 713193 占用 cuda:4 (576 MiB)，正在跑 `compute_signals.py --benchmark arc_challenge` (d100_a32_s123)，已运行 1h23m
- 这是同一 checkpoint 的 arc_challenge 信号计算，属于合法后续任务
- eval 任务需等 arc_challenge 信号完成后 cuda:4 释放才能提交

---
