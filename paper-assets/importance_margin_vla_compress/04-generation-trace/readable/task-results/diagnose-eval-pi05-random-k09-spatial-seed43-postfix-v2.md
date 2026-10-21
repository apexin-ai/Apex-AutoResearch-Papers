# diagnose eval pi05 random k09 spatial seed43 postfix v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_eval_pi05_random_k09_spatial_seed43_postfix_v2_20260524T231034_result.json`
- **Structured JSON:** [`64a31e0caf390e3f99c2.json`](../../sessions/64/64a31e0caf390e3f99c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

**结果汇总：**
- **Random k=0.9 Spatial seed43: SR = 54.0%**（500 eps, 94.1 min）
- Per-task: 92%, 44%, 76%, 10%, 28%, 58%, 56%, 72%, 76%, 28%
- Registry → DONE (success), cron 已清除

**Cliff zone k=0.9 Spatial dual-seed 对比：**
| Method | seed43 |
|--------|--------|
| L2norm | 96.2% |
| Random | 54.0% |
| **Margin** | **42.2pp** |

L2norm 在 k=0.9 Spatial 上对 Random 的优势巨大（+42.2pp），进一步确认 cliff zone 处 importance-aware pruning 的价值。

---
