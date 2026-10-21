# ops rsync k07 k03 to westd

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_rsync_k07_k03_to_westd_20260517T081013_result.json`
- **Structured JSON:** [`9ab25ef0b742384901e2.json`](../../sessions/9a/9ab25ef0b742384901e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

| 项目 | 状态 |
|------|------|
| k=0.7 checkpoint (920,907,737 bytes) | westd 已到位，大小一致 |
| k=0.3 checkpoint (920,907,737 bytes) | westd 已到位，大小一致 |
| configs/libero_acis_stage1only_k07.yaml | westd 已到位 |
| configs/libero_acis_stage1only_k03.yaml | westd 已到位 |
| eval_success_rate_libero.py (offset-tracking fix) | westd 已存在 |

westd-27271 上 k=0.7 和 k=0.3 的 Stage1-only ACIS checkpoint 及对应 config 已全部就绪，可以开始 eval。

---
