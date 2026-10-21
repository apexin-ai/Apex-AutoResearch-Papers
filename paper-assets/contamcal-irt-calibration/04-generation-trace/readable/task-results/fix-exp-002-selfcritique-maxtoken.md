# fix exp 002 selfcritique maxtoken

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp-002-selfcritique-maxtoken_20260514T124802_result.json`
- **Structured JSON:** [`0b0d10e189629d09e383.json`](../../sessions/0b/0b0d10e189629d09e383.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成。exp-002 进程正常运行中（`run_batch.py` PID 353388，当前子进程 `compute_signals.py` PID 368115 在 GPU 0 上处理 gsm8k）。

**修改汇总** — `signal_selfcritique.py` 三处 `256→64`：
- **第 88 行**: `batch_generate_answers` 函数默认参数 `max_new_tokens=64`
- **第 180 行**: `compute_selfcritique_signal` 函数默认参数 `max_answer_tokens=64`
- **第 241 行**: CLI `--max-answer-tokens` 默认值 `default=64`

当前 `compute_signals.py` 子进程正在跑 gsm8k 的 selfcritique，这个进程还用旧值 256。下一个 task 启动的子进程将自动使用新的 64。

---
