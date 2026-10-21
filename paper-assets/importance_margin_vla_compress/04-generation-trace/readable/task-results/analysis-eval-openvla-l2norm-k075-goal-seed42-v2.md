# analysis eval openvla l2norm k075 goal seed42 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_openvla_l2norm_k075_goal_seed42_v2_20260526T201559_result.json`
- **Structured JSON:** [`16da2aed11cf4c3c4384.json`](../../sessions/16/16da2aed11cf4c3c4384.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。结果摘要：

## eval_openvla_l2norm_k075_goal_seed42_v2 结果

**Overall SR: 70.2% (351/500)**

### Per-task SR

| Task | SR |
|---|---|
| open the middle drawer of the cabinet | 54.0% |
| put the bowl on the stove | 80.0% |
| put the wine bottle on top of the cabinet | 86.0% |
| open the top drawer and put the bowl inside | 22.0% |
| put the bowl on top of the cabinet | 88.0% |
| push the plate to the front of the stove | 70.0% |
| put the cream cheese in the bowl | 68.0% |
| turn on the stove | 98.0% |
| put the bowl on the plate | 82.0% |
| put the wine bottle on the rack | 54.0% |

### Cliff Curve 对比 (LIBERO Goal, L2norm)

| k | 保留 tokens | SR | Δ vs 上一点 |
|---|---|---|---|
| 0.90 | 230 | 74.8% | — |
| 0.85 | 218 | 75.4% | +0.6pp |
| **0.75** | **192** | **70.2%** | **-5.2pp** |
| 0.70 | 179 | 68.4% | -1.8pp |

k=0.75 (70.2%) 符合预期，落在 k=0.85 和 k=0.7 之间。下降斜率主要集中在 k=0.85→0.75 段（-5.2pp），说明性能 cliff 起点约在 k≈0.8 附近。k=0.75→0.7 段下降仅 1.8pp，曲线趋缓。

---
