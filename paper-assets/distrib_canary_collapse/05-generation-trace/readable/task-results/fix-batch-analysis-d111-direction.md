# fix batch analysis d111 direction

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_batch_analysis_d111_direction_20260519T223814_result.json`
- **Structured JSON:** [`9d5d4cf3a349036b9f84.json`](../../sessions/9d/9d5d4cf3a349036b9f84.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过：

- **naive_xcorr: 3/8** (原来是 8/8)
- **diff_xcorr: 0/8** (原来是 8/8)
- **consensus_k4: 0/8** (原来是 3/8)

与预期验证标准完全匹配。两个文件的 `peak_lag > 0` 方向检查都已修复。

---
