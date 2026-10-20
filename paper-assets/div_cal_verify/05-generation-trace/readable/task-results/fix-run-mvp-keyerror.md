# fix run mvp keyerror

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_run_mvp_keyerror_20260512T203111_result.json`
- **Structured JSON:** [`ca56cc154625046e91f1.json`](../../sessions/ca/ca56cc154625046e91f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两处修改完成，语法验证通过：

- **第277行**：`metrics['rank_correlation']` → `metrics.get('rank_correlation', float('nan'))`
- **第292行**：`r['rank_correlation']` → `r.get('rank_correlation', float('nan'))`

uncurated 方法不计算 `rank_correlation` 时，这两处会显示 `nan` 而非崩溃。

---
