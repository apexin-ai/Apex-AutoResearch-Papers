# ssh create snapshot monitor

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_create-snapshot-monitor_20260524T095403_result.json`
- **Structured JSON:** [`a105222e40ae38d3f56f.json`](../../sessions/a1/a105222e40ae38d3f56f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个脚本均测试通过。

### check_collection_progress.sh 结果

| Judge | Records | % | Status |
|-------|---------|---|--------|
| claude-sonnet-4.6-proxy_n17 | 8,501 | 47.2% | STOPPED |
| deepseek-v4-pro-proxy_n17 | 5,050 | 28.0% | STOPPED |
| gemini-2.5-pro-proxy_n17 | 5,951 | 33.0% | STOPPED |
| llama-3.3-70b-local_n17 | 2,003 | 11.1% | STOPPED |
| mistral-large-2-local_n17 | 118 | 0.6% | STOPPED |
| qwen2.5-72b-local_n17 | 1,365 | 7.5% | STOPPED |
| qwen3-235b-proxy_n17 | 6,341 | 35.2% | STOPPED |

Sonnet 和 Qwen3-235B 均未达到 18,000 目标，触发条件未满足。

### snapshot_judge_data.sh 结果

`prepare_n17_data.py` 正常刷新了 7 个 judge 的 symlinks，共 28,109 条 status=ok 记录，覆盖 18 个 target models，7×18 judge×model 矩阵全覆盖。

---
