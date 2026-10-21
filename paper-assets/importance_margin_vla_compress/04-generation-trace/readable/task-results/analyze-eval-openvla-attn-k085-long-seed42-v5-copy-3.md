# analyze eval openvla attn k085 long seed42 v5

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_openvla_attn_k085_long_seed42_v5_20260526T211628_result.json`
- **Structured JSON:** [`8539a22f5f0e6d078069.json`](../../sessions/85/8539a22f5f0e6d078069.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已全部更新。结果分析：

**OpenVLA Attn k=0.85 Long Suite: 45.8%**

| k值 | Long SR | 相对变化 |
|-----|---------|----------|
| 0.90 | 44.0% | baseline |
| **0.85** | **45.8%** | **+1.8pp** |
| 0.70 | 24.0% | -20.0pp |

k=0.85 与 k=0.9 性能几乎持平（45.8% vs 44.0%，在噪声范围内），说明 attention pruning 在 Long suite 上的性能 plateau 至少延伸到 k=0.85（移除 15% vision tokens）。**性能悬崖发生在 k=0.85 和 k=0.7 之间**，而非 k=0.9 和 k=0.85 之间。

256 → 217 vision tokens，节省 15% tokens 且无性能损失。无 W&B run。

---
