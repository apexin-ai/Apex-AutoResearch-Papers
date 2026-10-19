# ops starcoder random data fix

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_starcoder-random-data-fix_20260513T112208_result.json`
- **Structured JSON:** [`5f1056a9645b177a3571.json`](../../sessions/5f/5f1056a9645b177a3571.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件中 StarCoder random 行的数据已经是完整的，不需要修复：

- **pilot_results_summary.md**: StarCoder random 行已显示 `| random | completed | 500 | 0.5113 | 0.4922 | 0.98 | 1.0 |`，cross-model comparison 表也已填入。
- **pilot_results.json**: `starcoder2-3b.strategies.random.best_metrics` 已包含 `val_loss: 0.5113, recall_at_1: 0.4922, recall_at_5: 0.98, recall_at_10: 1.0`。

两个文件中没有任何 "—" 标记在 StarCoder random 行上。数据此前已被修复。

---
