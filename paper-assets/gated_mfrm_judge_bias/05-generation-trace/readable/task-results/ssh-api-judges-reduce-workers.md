# ssh api judges reduce workers

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_api_judges_reduce_workers_20260524T011357_result.json`
- **Structured JSON:** [`44ff2d3197648b542e0a.json`](../../sessions/44/44ff2d3197648b542e0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已设置 15 分钟后自动检查。

**当前进度汇总：**
- Step 1 ✅ Baseline 已记录
- Step 2 ✅ 旧进程 (--workers 10) 已全部 kill
- Step 3 ✅ 4 个 judges 已以 --workers 5 重启
- Step 4 ⏳ 15 分钟后 (约 09:34 UTC) 自动检查

**Baseline (09:15 UTC, --workers 10):**

| Judge | JSONL | 500 errors / log lines | Speed | ETA |
|-------|-------|----------------------|-------|-----|
| sonnet | 1324 | 42/176 (23.9%) | 0.2 items/s | ~1237 min |
| gemini | 944 | 30/125 (24.0%) | 0.2 items/s | ~1759 min |
| deepseek | 779 | 26/105 (24.8%) | 0.1 items/s | ~2144 min |
| qwen3 | 917 | 24/119 (20.2%) | 0.2 items/s | ~1797 min |

---
