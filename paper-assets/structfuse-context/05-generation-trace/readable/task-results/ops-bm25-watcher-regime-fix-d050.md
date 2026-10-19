# ops bm25 watcher regime fix d050

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bm25-watcher-regime-fix-d050_20260515T102450_result.json`
- **Structured JSON:** [`3bad3f96bd6fc23523db.json`](../../sessions/3b/3bad3f96bd6fc23523db.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成，两个脚本均已更新。

| 脚本 | 字段 | 修改前 | 修改后 |
|------|------|--------|--------|
| `run_m2_full_bm25_qwen.sh` | EPOCHS | `[42]=3 [43]=2 [44]=2` | `[42]=2 [43]=2 [44]=2` |
| | PATIENCE | `[42]=0 [43]=2 [44]=2` | `[42]=2 [43]=2 [44]=2` |
| `run_m2_full_bm25_starcoder.sh` | EPOCHS | `[42]=3 [43]=2 [44]=2` | `[42]=2 [43]=2 [44]=2` |
| | PATIENCE | `[42]=0 [43]=2 [44]=2` | `[42]=2 [43]=2 [44]=2` |

s42 现在统一为 2 epochs + patience=2。Watcher 进程未触碰。

---
