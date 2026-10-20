# ops verify tail2048 started

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_tail2048_started_20260518T034807_result.json`
- **Structured JSON:** [`1f40dff9ec82e1c2b775.json`](../../sessions/1f/1f40dff9ec82e1c2b775.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**启动失败。** 原因和状态：

1. **PID 404579 不存在** — `codellama13b_full_trace_tail2048_seed42` 进程已退出。

2. **Log 显示参数错误** — `--condition full_trace_tail_2048` 不是合法选项。`train_sft.py` 支持的 tail 变体只有：`full_trace_tail`、`full_trace_tail_512`、`full_trace_tail_256`、`full_trace_tail_1024`。没有 `full_trace_tail_2048`。退出码 EXIT_CODE=2。

3. **GPU 占用情况** — GPU 0 被 PID 403391 占用（`codellama13b_full_trace_tail1024_seed42_v2`，正在训练中）。GPU 1 空闲。

**结论：** 需要先在 `train_sft.py` 中注册 `full_trace_tail_2048` 这个 condition choice，然后重新启动。

---
