# analyze eval pi05 l2norm k07 goal seed43 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_l2norm_k07_goal_seed43_v2_20260524T025455_result.json`
- **Structured JSON:** [`be0c77041c3d332efd6b.json`](../../sessions/be/be0c77041c3d332efd6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 结果汇总

**Overall SR: 72.2%** (361/500), 耗时 71.3 min, 无错误。

### Per-task SR

| Task | SR |
|---|---|
| T0 open middle drawer | 78% |
| T1 put bowl on stove | 76% |
| T2 wine bottle on cabinet | 68% |
| T3 open drawer put bowl | 48% |
| T4 bowl on cabinet | 90% |
| T5 push plate front stove | 80% |
| T6 cream cheese in bowl | 66% |
| T7 turn on stove | **98%** |
| T8 bowl on plate | 68% |
| T9 wine bottle on rack | 50% |

### 双种子对比

| Seed | SR |
|---|---|
| seed42 | 71.8% |
| seed43 | 72.2% |
| **Δ** | **+0.4pp** |

差距仅 0.4pp，L2norm k=0.7 在 Goal suite 上表现高度稳定。Conclusion: **success**。

---
