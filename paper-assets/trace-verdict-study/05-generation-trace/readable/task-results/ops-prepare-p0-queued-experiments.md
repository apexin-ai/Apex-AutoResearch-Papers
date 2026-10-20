# ops prepare p0 queued experiments

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_prepare_p0_queued_experiments_20260518T113829_result.json`
- **Structured JSON:** [`d4be46c796630717395f.json`](../../sessions/d4/d4be46c796630717395f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**所有 7 个 QUEUED 实验已经在不同 exp_id 下完成了。** QUEUED 条目是旧命名（含点号）的残留，实际已用新命名跑完。

对应关系和结果：

| QUEUED exp_id | 已完成的 exp_id | Accuracy |
|---|---|---|
| `codellama_no_trace_seed42` | `codellama13b_no_trace_seed42` | 76.5% |
| `codellama_vota_seed42` | `codellama13b_vota_seed42` | 98.57% |
| `codellama_exception_only_seed42` | `codellama13b_exception_only_seed42` | 99.83% |
| `qwen1.5b_no_trace_seed42` | `qwen15b_no_trace_seed42` | 67.31% |
| `qwen1.5b_vota_seed42` | `qwen15b_vota_seed42` | 99.58% |
| `qwen1.5b_exception_only_seed42` | `qwen15b_exception_only_seed42` | 99.83% |
| `qwen1.5b_full_trace_seed42` | `qwen15b_full_trace_seed42` | 77.06% |

证据：
- QUEUED 条目的 `failure_reason` 已标注 "replaced by qwen15b_* entries (dot in exp_id incompatible with submit_on_allocated)" 和 "user approved 13B not 7B"
- 完成的实验命令、condition、seed 完全一致，只是 exp_id 命名从 `qwen1.5b_*` 改为 `qwen15b_*`，从 `codellama_*` 改为 `codellama13b_*`
- 所有 7 个的 conclusion 均为 success

**建议：** 将这 7 个 QUEUED 条目状态更新为 DONE（或 CANCELLED），指向已完成的对应实验，避免混淆。需要我执行吗？

---
