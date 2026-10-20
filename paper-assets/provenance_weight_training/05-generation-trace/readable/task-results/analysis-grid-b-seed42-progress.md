# analysis grid b seed42 progress

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grid_b_seed42_progress_20260514T142925_result.json`
- **Structured JSON:** [`7773dbc556a4ce2043a3.json`](../../sessions/77/7773dbc556a4ce2043a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
PROGRESS:
- Current b value: 2.0
- Current step: 5585/6103 (92%)
- Completed b values: [0.5, 1.0, 1.5]
- Remaining: b=2.0 (~18min), then b=3.0 (~3.6h), b=5.0 (~3.6h) → ~7.5 hours total

EVAL RESULTS (seed42, holdout ppl):
- b=0.5: ppl=17.651
- b=1.0: ppl=17.692
- b=1.5: ppl=17.718
- b=2.0: IN_PROGRESS (92%)
- b=3.0: NOT_STARTED
- b=5.0: NOT_STARTED

GPU STATUS:
- cuda:0: 99% util, 46523/97887 MiB
- cuda:1: 95% util, 46523/97887 MiB
- cuda:2: 99% util, 46523/97887 MiB
- cuda:3: 98% util, 46523/97887 MiB
```

趋势：ppl 随 b 增大而轻微上升（17.651 → 17.692 → 17.718），b=0.5 目前最优。4 块 GPU 全部高负载但只用了约 48% 显存（训练只用 cuda:0 串行，其余 GPU 可能被其他任务占用）。

---
