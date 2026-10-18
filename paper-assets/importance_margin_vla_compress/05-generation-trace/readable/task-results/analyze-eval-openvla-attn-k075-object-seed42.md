# analyze eval openvla attn k075 object seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_openvla_attn_k075_object_seed42_20260526T211624_result.json`
- **Structured JSON:** [`63d90b78b478ad3f165f.json`](../../sessions/63/63d90b78b478ad3f165f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。结论：

**Attn k=0.75 Object SR = 53.2%**，conclusion = success。

Cliff curve 完整图谱：

| k | SR | Δ (vs 上一点) |
|---|---|---|
| 0.90 | 61.4% | — |
| 0.85 | 55.0% | -6.4pp |
| **0.75** | **53.2%** | **-1.8pp** |
| 0.70 | 43.8% | -9.4pp |

关键发现：k=0.85→0.75 退化非常平缓（仅 -1.8pp），而 k=0.75→0.70 出现断崖式下降（-9.4pp）。**Cliff 位置精确定位在 k=0.70~0.75 之间**，k=0.75 仍是安全的压缩点。

---
