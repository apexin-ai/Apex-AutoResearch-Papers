# analyze eval openvla l2norm k085 long seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_openvla_l2norm_k085_long_seed42_v2_20260526T025702_result.json`
- **Structured JSON:** [`e7747bf95d0617a769e6.json`](../../sessions/e7/e7747bf95d0617a769e6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE (success)。

**结果摘要**：L2norm pruning k=0.85 Long suite → **38.8%** SR。

Cliff curve 当前数据：
- k=0.9 → 43.6%
- k=0.85 → 38.8% (↓4.8pp)
- k=0.7 → 待定

从 0.9 到 0.85（仅丢弃额外 5% vision tokens），性能下降约 5pp，说明这个区间的衰减斜率约为 1pp/1% tokens，是比较线性的衰退而非悬崖式骤降。k=0.7 的结果将确认是否在更低 k 值出现 cliff。

---
