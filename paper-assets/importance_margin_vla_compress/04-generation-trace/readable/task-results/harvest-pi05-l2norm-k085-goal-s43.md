# harvest pi05 l2norm k085 goal s43

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_pi05-l2norm-k085-goal-s43_20260524T023321_result.json`
- **Structured JSON:** [`54c51f7281f07472a028.json`](../../sessions/54/54c51f7281f07472a028.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

收割完成。

**eval_pi05_l2norm_k085_goal_seed43 结果：**

| 指标 | 值 |
|------|-----|
| **Overall SR** | **87.0%** (435/500) |
| Conclusion | **success**（baseline Goal ~88%，几乎无损） |
| 耗时 | 86.5 min |

**Per-task SR：**

| Task | SR |
|------|-----|
| open the middle drawer of the cabinet | 88% |
| put the bowl on the stove | 94% |
| put the wine bottle on top of the cabinet | 96% |
| open the top drawer and put the bowl inside | 80% |
| put the bowl on top of the cabinet | 96% |
| push the plate to the front of the stove | 94% |
| put the cream cheese in the bowl | 86% |
| turn on the stove | 96% |
| put the bowl on the plate | 94% |
| put the wine bottle on the rack | 46% |

L2norm k=0.85 在 Goal suite 上 87% vs baseline ~88%，裁剪 15% vision tokens 几乎无损。唯一弱项是 "put the wine bottle on the rack"（46%），其余 task 均 ≥80%。Registry 已更新为 DONE/success。

---
