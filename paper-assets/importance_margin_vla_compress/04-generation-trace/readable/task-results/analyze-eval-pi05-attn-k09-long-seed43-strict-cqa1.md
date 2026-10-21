# analyze eval pi05 attn k09 long seed43 strict cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_attn_k09_long_seed43_strict_cqa1_20260527T202032_result.json`
- **Structured JSON:** [`7a6d3424039c82c2a611.json`](../../sessions/7a/7a6d3424039c82c2a611.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。汇总：

```
overall_success_rate: 62.8%
total_episodes: 500
per_task: [T0=46%, T1=88%, T2=42%, T3=92%, T4=62%, T5=92%, T6=48%, T7=52%, T8=14%, T9=92%]
conclusion: success
status: DONE
```

seed43=62.8% vs seed42=64.0%，差异仅 -1.2pp，error bar 非常稳定。Attn k=0.9 Long 均值约 63.4%，确认处于断崖中间位置（k=0.95=78.4% → k=0.9≈63.4% → k=0.85=50.0%），从 0.95 到 0.9 掉了约 15pp。

---
