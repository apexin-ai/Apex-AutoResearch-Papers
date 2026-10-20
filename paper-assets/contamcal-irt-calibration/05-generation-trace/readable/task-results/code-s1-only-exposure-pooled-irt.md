# code s1 only exposure pooled irt

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_s1-only-exposure-pooled-irt_20260514T235629_result.json`
- **Structured JSON:** [`ef57a5a30d1cf3e6da37.json`](../../sessions/ef/ef57a5a30d1cf3e6da37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都已正常启动并在运行 Stan MCMC sampling。关键信息：

- **ARC**: S1-only exposure 值 `[0.0, 0.027, 0.099, 0.305, 0.0, 0.027, 0.099, 0.305]` — 完美单调递增，与 D034 预期一致
- **GSM8K**: S1-only exposure 值 `[0.0, 0.016, 0.065, 0.197, 0.0, 0.016, 0.065, 0.197]` — 同样单调

代码修改完成，两个实验正在运行：
1. `exp006-pooled-s1only-arc` — tmux session `irt_s1only_arc`
2. `exp006-pooled-s1only-gsm8k` — tmux session `irt_s1only_gsm8k`

Stan MCMC 4 chains × 2000 iterations (1000 warmup + 1000 sampling)，预计 10-20 分钟完成。

---
