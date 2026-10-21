# code fix token selection

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-token-selection_20260515T114140_result.json`
- **Structured JSON:** [`afe31cf68e9e6b335bd3.json`](../../sessions/af/afe31cf68e9e6b335bd3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All four changes applied:

1. **三分区逻辑**：用 `delta_k = s_k - s_{k+1}` 计算 margin zone `[s_k - Δ/2, s_k + Δ/2]`，替换原来固定 rank 边界
2. **preserve 固定 top-k**：输出长度始终为 k，borderline/prune 只对 non-top-k tokens 分区
3. **info dict**：新增 `delta_k` 字段
4. **TODO 注释**：`_merge_borderline_tokens` 循环前已标记

`__init__` 默认 `method="sigmoid"` 已确认（line 25）。

本地环境无 torch，无法运行验证脚本。需要在服务器上执行验证测试。

---
