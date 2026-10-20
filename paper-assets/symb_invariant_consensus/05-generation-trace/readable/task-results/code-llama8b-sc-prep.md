# code llama8b sc prep

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama8b-sc-prep_20260520T040106_result.json`
- **Structured JSON:** [`023409eb90e9526dd876.json`](../../sessions/02/023409eb90e9526dd876.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

摘要已写入 `artifacts/llama8b_sc_prep.md`。核心发现：

**模型**: westd-16639 已有完整的 `Meta-Llama-3.1-8B-Instruct`（4 shards），westd-25068 没有。

**exp-063 per-trace 数据可复用**: `intermediates/` 下 204 个文件，每题 12 条 trace 各有 `answer` 字段，可直接提取用于 κ 计算，无需重跑 SC。

**待确认**: 是否需要重跑（不同 seed？），端口/GPU 分配，服务器选择。

---
