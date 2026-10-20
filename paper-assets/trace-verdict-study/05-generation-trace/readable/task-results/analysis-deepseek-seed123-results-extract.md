# analysis deepseek seed123 results extract

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek_seed123_results_extract_20260518T162921_result.json`
- **Structured JSON:** [`f3bcda8971781956fb2c.json`](../../sessions/f3/f3bcda8971781956fb2c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

| 字段 | 值 |
|------|-----|
| **status** | DONE |
| **conclusion** | negative |
| **失败原因** | CUDA OOM at step 0/444 |
| **根因** | GPU 0 被占满（PyTorch 已用 43.45 GiB，仅剩 167 MiB），分配 178 MiB 失败 |
| **退出时间** | 2026-05-18T15:49:48Z |

当前服务器上 GPU 0 在跑 `qwen7b_full_trace_tail512_seed123`，GPU 1 在跑 `deepseek_full_trace_tail512_seed456`。需要等当前任务结束后重新提交 seed123。

---
