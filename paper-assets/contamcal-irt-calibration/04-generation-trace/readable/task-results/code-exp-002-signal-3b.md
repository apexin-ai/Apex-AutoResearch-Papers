# code exp 002 signal 3B

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-002-signal-3B_20260515T144426_result.json`
- **Structured JSON:** [`467cdb8ed2139a06d51b.json`](../../sessions/46/467cdb8ed2139a06d51b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已成功启动 `exp_002_signals_3B`，日志确认：

- **Model**: Qwen2.5-3B
- **Dosages**: d000, d005, d025, d100（4 个）
- **Benchmarks**: mmlu, gsm8k, arc_challenge
- **Tasks**: 12 个（4×3），0 skipped
- **Signals**: embedding, minkpp, selfcritique（ConStat 未启用 — 3B 的 eval_results 路径不匹配 `{model}_{dosage}_s42` 命名约定，有 `_aligned`/`_v2` 后缀）
- **PID**: 576030，tmux session `exp_002_signals_3B`
- 第 1/12 个任务（d000/mmlu）已开始执行

GPU 显存尚未分配是正常的，模型加载需要几秒。

---
