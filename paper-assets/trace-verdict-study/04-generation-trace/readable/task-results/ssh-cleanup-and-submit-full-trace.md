# ssh cleanup and submit full trace

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cleanup_and_submit_full_trace_20260515T134001_result.json`
- **Structured JSON:** [`c8d8b0758e2f5ef02932.json`](../../sessions/c8/c8d8b0758e2f5ef02932.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**tmux 清理**
- `deepseek_full_trace_seed42` — 已 kill
- `deepseek_no_trace_seed42` — 不存在，无需操作
- `deepseek_exception_only_seed42` — 仍保留（未在清理列表中）

**cuda:0 状态 — 未空闲**
- GPU 0: 71525 MiB 显存占用，利用率 89%，进程 PID 111481 占用 22360 MiB
- GPU 1: 39586 MiB 显存占用，利用率 100%，两个进程（PID 107198 + 110354）

cuda:0 上仍有活跃进程，不是空闲状态。可能是刚 kill 的 tmux session 里的进程还没完全退出，或者是 `deepseek_exception_only_seed42` session 的进程。

**代码状态**
`train_sft.py` 第 148-151 行，`load_best_model_at_end`、`save_total_limit`、`metric_for_best_model`、`greater_is_better` 四项均已用 `# TEMP_DISABLED:` 注释掉，符合预期。

---
