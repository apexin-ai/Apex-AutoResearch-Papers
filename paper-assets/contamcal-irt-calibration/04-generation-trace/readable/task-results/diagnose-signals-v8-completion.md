# diagnose signals v8 completion

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_signals_v8_completion_20260516T003155_result.json`
- **Structured JSON:** [`d46f8c768741cc4ca9ba.json`](../../sessions/d4/d46f8c768741cc4ca9ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

**exp_002_signals_3B_v8: FAILED (OOM Killed)**

- **原因**：s4_selfcritique 处理 mmlu (7021 items) 时被 OOM Killer 终止
- **已完成**：d025_s123 的 gsm8k 和 arc_challenge（全部信号+merged）；d025_s123 mmlu 和 d100_a32_s123 mmlu 各有 s1+s2
- **未完成**：两个 dosage 的 mmlu s4+merged；d100_a32_s123 的 gsm8k 和 arc_challenge 全部
- **cuda:4 当前状态**：PID 662616 正在运行 d100_a32_s123/mmlu 信号计算（已跑 17 分钟），占用 6882 MiB

---
