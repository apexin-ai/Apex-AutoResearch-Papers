# ssh plan 004 v2 gpu2 check

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_plan-004-v2-gpu2-check_20260515T030419_result.json`
- **Structured JSON:** [`634f9892ac3bfb4b7b37.json`](../../sessions/63/634f9892ac3bfb4b7b37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU2 正常完成**，日志末尾 `GPU2 ALL DONE`。

**14/15 results.json 已就绪**，缺失：`depth01_seed123`（应在 GPU1 或 GPU3 上）。

各组平均结果（eval_loss / ppl）：

| 数据集 | eval_loss | perplexity |
|--------|-----------|------------|
| **all** | 0.8480 | 2.335 |
| size_matched | 0.8617 | 2.367 |
| depth01 | 0.8701 | 2.387 |
| binary_filtered | 0.8709 | 2.389 |
| depth0_only | 0.9864 | 2.682 |

Registry 已更新。

---
