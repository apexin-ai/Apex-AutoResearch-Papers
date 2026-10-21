# analyze openvla l2norm k085 object

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_openvla_l2norm_k085_object_20260527T122529_result.json`
- **Structured JSON:** [`612f9c9e19a567edd7a8.json`](../../sessions/61/612f9c9e19a567edd7a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。结果汇总：

**Overall SR: 55.2% (276/500)，耗时 254.8 min**

| Task | SR |
|---|---|
| ketchup | 92.0% |
| alphabet soup | 60.0% |
| salad dressing | 60.0% |
| milk | 58.0% |
| orange juice | 54.0% |
| chocolate pudding | 52.0% |
| butter | 50.0% |
| bbq sauce | 44.0% |
| tomato sauce | 42.0% |
| cream cheese | 40.0% |

重跑结果与前次 55.2% **完全一致**（per-task SR 也逐项吻合），确认 k=0.85 的非单调现象是真实的：

| k | Object SR |
|---|---|
| 0.95 | 70.6% |
| 0.90 | 70.6% |
| **0.85** | **55.2%** |
| 0.75 | 57.4% |
| 0.70 | 49.8% |

k=0.85→0.75 的反弹（55.2%→57.4%）已确认不是随机波动。

---
