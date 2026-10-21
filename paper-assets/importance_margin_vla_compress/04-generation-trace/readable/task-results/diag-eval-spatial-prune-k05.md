# diag eval spatial prune k05

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval_spatial_prune_k05_20260517T113819_result.json`
- **Structured JSON:** [`9c784852fb8ab81fcd51.json`](../../sessions/9c/9c784852fb8ab81fcd51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。

**总结**：
- `eval_spatial_prune_k05` 已正常完成（19:35 结束），非崩溃
- **SR = 0.0%**（0/500），10 个 task 全部 0%，所有 episode 跑满 280 步 timeout
- 与 libero_object 上的 true_removal 结果一致（也是 0%），确认 cliff-edge 效应跨 suite 成立
- Baseline spatial SR = 51.8% → pruning 后完全崩溃
- Registry 已更新：status=DONE, conclusion=success, metrics 已记录

---
