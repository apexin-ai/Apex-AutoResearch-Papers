# analysis eval openvla attn k07 goal seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_openvla_attn_k07_goal_seed42_20260526T172945_result.json`
- **Structured JSON:** [`5cd907969da99a7abbc6.json`](../../sessions/5c/5cd907969da99a7abbc6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验正常完成，结果如下：

## eval_openvla_attn_k07_goal_seed42

**Overall SR: 66.4% (332/500)** — EXIT_CODE=0，10 tasks × 50 episodes = 500，无报错。

Vision tokens: 256 → 179 (30% pruning)

### Per-task breakdown

| Task | SR | Count |
|---|---|---|
| open the middle drawer of the cabinet | 62.0% | 31/50 |
| put the bowl on the stove | 80.0% | 40/50 |
| put the wine bottle on top of the cabinet | 76.0% | 38/50 |
| open the top drawer and put the bowl inside | 28.0% | 14/50 |
| put the bowl on top of the cabinet | 90.0% | 45/50 |
| push the plate to the front of the stove | 74.0% | 37/50 |
| put the cream cheese in the bowl | 60.0% | 30/50 |
| turn on the stove | 90.0% | 45/50 |
| put the bowl on the plate | 62.0% | 31/50 |
| put the wine bottle on the rack | 42.0% | 21/50 |

### Cliff 分析

| Config | Goal SR | Δ vs baseline |
|---|---|---|
| Baseline (full) | 74.8% | — |
| Attn k=0.9 (10% prune) | 73.2% | -1.6 |
| Attn k=0.85 (15% prune) | 74.6% | -0.2 |
| **Attn k=0.7 (30% prune)** | **66.4%** | **-8.4** |

### Conclusion: **Cliff confirmed**

k=0.85 → k=0.7 出现显著性能断崖，SR 从 74.6% 骤降至 66.4%（-8.2pp）。Attention pruning 的安全区间在 k∈[0.85, 0.9]，保留 85%+ tokens 时性能接近 baseline，但压缩到 70% 时性能急剧下降。Cliff 发生在 k=0.85 和 k=0.7 之间。

---
