# analyze eval openvla l2norm k05 goal seed42 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_openvla_l2norm_k05_goal_seed42_v3_20260523T231714_result.json`
- **Structured JSON:** [`724656518a22d5012efe.json`](../../sessions/72/724656518a22d5012efe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果总结：

## eval_openvla_l2norm_k05_goal_seed42_v3 — 结果

**Overall SR: 43.4% (217/500)** — Conclusion: **negative**

### 与 baseline 对比

| 配置 | SR | 相对 baseline 保留率 |
|------|-----|---------------------|
| Goal baseline (full tokens) | 74.8% | 100% |
| **Goal L2norm k=0.5** | **43.4%** | **58.0%** |
| Object baseline | 96.2% | 100% |
| Object L2norm k=0.5 | 39.2% | 40.7% |

Goal suite 下 L2norm k=0.5 造成 **-31.4pp** 绝对下降（74.8% → 43.4%）。相比 Object suite 的 -57.0pp 下降，Goal suite 的绝对损失更小，但仍然严重不可接受。

### Per-task 分布

任务间方差极大：`turn_on_the_stove` 几乎无损 (98%)，`put_wine_bottle_on_cabinet` 也较好 (82%)，但 `open_top_drawer_put_bowl_inside` 仅 6%，多步复合任务受 token 裁剪影响最严重。

### 结论

L2norm k=0.5 的 naive pruning 在两个 suite 上都造成严重性能下降，不具备实用价值。简单任务（单步、空间固定）受影响小，复杂多步任务几乎完全崩溃。需要更智能的 token 选择策略或更保守的压缩比。

---
