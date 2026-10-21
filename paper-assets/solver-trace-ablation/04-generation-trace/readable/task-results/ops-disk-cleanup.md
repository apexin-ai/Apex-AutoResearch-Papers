# ops disk cleanup

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk-cleanup_20260515T002819_result.json`
- **Structured JSON:** [`5eba4b8c75b84db9e133.json`](../../sessions/5e/5eba4b8c75b84db9e133.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。HF cache 5.3G（含 Qwen3-4B），保留不动。

## 清理结果

| | 使用量 | 占比 |
|---|---|---|
| **清理前** | 210G / 250G | 84% |
| **清理后** | 67G / 250G | 27% |
| **释放** | **143G** | |

保留的目录：
- `exp1_random_b03_s44/` (15G) — 训练中
- `exp1_isr_b03_s44_r2/` (31G) — 待分析

---
