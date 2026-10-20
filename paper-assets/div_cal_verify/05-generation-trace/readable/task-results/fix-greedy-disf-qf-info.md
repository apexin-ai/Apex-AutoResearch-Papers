# fix greedy disf qf info

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_greedy_disf_qf_info_20260513T033443_result.json`
- **Structured JSON:** [`e9adfc82b54f2d2eca71.json`](../../sessions/e9/e9adfc82b54f2d2eca71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成：

- 第 102 行 `greedy_disf_selection` 末尾 `return selected, qf_info` → `return selected`
- 第 157 行 `select_data` 中的 `return selected, qf_info` 未改动
- 语法检查通过

---
