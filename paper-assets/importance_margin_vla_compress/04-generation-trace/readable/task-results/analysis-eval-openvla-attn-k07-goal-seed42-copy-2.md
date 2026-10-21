# analysis eval openvla attn k07 goal seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_openvla_attn_k07_goal_seed42_20260526T175950_result.json`
- **Structured JSON:** [`e68bd00bbf94a6341cdf.json`](../../sessions/e6/e68bd00bbf94a6341cdf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。

**`eval_openvla_attn_k07_goal_seed42`** — conclusion: **negative**
- overall_sr = **66.4%** (332/500)

**对比分析**: Attn 在 Goal 上的 cliff curve 确认：k=0.9 → 73.2%, k=0.85 → 74.6%（平稳甚至微升），k=0.7 → 66.4%（骤降 8.2pp）。Cliff 点在 k=0.85 到 k=0.7 之间，说明 Attention pruning 在 Goal suite 上保留 70% heads 已不足以维持性能，安全压缩上限约为 k=0.85（保留 85% heads）。

---
