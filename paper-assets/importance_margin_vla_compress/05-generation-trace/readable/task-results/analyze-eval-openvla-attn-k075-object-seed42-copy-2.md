# analyze eval openvla attn k075 object seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_openvla_attn_k075_object_seed42_20260526T231335_result.json`
- **Structured JSON:** [`97c3f48a99cbdbf2429d.json`](../../sessions/97/97c3f48a99cbdbf2429d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果汇总：

**Overall SR: 53.2%** (266/500)

| Task | SR |
|---|---|
| chocolate_pudding | 86.0% |
| ketchup | 76.0% |
| salad_dressing | 70.0% |
| orange_juice | 70.0% |
| alphabet_soup | 56.0% |
| milk | 54.0% |
| bbq_sauce | 34.0% |
| tomato_sauce | 30.0% |
| cream_cheese | 28.0% |
| butter | 28.0% |

**Object Attn cliff curve 更新：**

| k | SR | Δ |
|---|---|---|
| 0.90 | 61.4% | — |
| 0.85 | 55.0% | -6.4pp |
| **0.75** | **53.2%** | **-1.8pp** |
| 0.70 | 43.8% | -9.4pp |
| 0.50 | 40.6% | -3.2pp |

Cliff 定位清晰：k=0.85→0.75 仅下降 1.8pp（平缓区），k=0.75→0.70 骤降 9.4pp（断崖）。**Cliff 位于 k=0.70~0.75 之间**，k=0.75 是安全压缩的下界——保留 75% attention tokens 仍能维持接近 k=0.85 的性能。

---
