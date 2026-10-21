# analyze eval openvla attn k085 long seed42 v5

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_openvla_attn_k085_long_seed42_v5_20260526T202938_result.json`
- **Structured JSON:** [`850a7532c9ca988d3c33.json`](../../sessions/85/850a7532c9ca988d3c33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。

```
exp_id: eval_openvla_attn_k085_long_seed42_v5
overall_sr: 45.8%
conclusion: success
对比: Attn k=0.9=44.0% → k=0.85=45.8% (Δ=+1.8%)
```

**分析要点：**

更新后的 Long cliff curve：

| k | L2norm | Attn | Random |
|---|--------|------|--------|
| 0.9 | 43.6% | 44.0% | 46.8% |
| 0.85 | 38.8% | **45.8%** | running |
| 0.7 | 31.2% | 24.0% | 38.8% |
| 0.5 | — | running | running |

Attn k=0.85 (45.8%) 比 k=0.9 (44.0%) 还高 1.8%，说明在 Long suite 上 attention pruning 在 0.85~0.9 区间性能稳定甚至略有波动上升。关键发现是 **Attn 的 cliff 在 k=0.85→0.7 之间**（45.8% → 24.0%，断崖式下降 21.8pp），而 L2norm 在 0.9→0.85 就已经开始显著下降（43.6% → 38.8%）。这表明 attention-based scoring 在更激进的压缩率下比 L2norm 更能保持性能，但一旦突破某个阈值（约 k=0.75 附近）会急剧崩溃。

---
