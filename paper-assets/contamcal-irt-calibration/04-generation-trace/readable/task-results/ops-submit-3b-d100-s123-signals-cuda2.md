# ops submit 3B d100 s123 signals cuda2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit_3B_d100_s123_signals_cuda2_20260516T131942_result.json`
- **Structured JSON:** [`c936836ea505f3ef7573.json`](../../sessions/c9/c936836ea505f3ef7573.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**cuda:2 占用中**，PID 784230 正在跑 `3B d000_s123 mmlu s4` signals。根据 C001/C002 约束，不能提交到 cuda:2。

当前 GPU 状态：
- cuda:0: 占用 (6817 MiB)
- cuda:1: 占用 (1931 MiB)
- cuda:2: 占用 (7301 MiB) — 3B d000_s123 mmlu s4
- cuda:3: 占用 (6415 MiB)
- cuda:4: 占用 (14210 MiB)
- cuda:5: **空闲** (0 MiB, 0%)

cuda:5 是唯一空闲 GPU。是否改为提交到 cuda:5？

---
