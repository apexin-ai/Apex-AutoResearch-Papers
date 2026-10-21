# monitor quick status check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_quick_status_check_20260514T223656_result.json`
- **Structured JSON:** [`dcc9236b6ea5039def2d.json`](../../sessions/dc/dcc9236b6ea5039def2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
008e_v3_s1:
  process: alive (running 3h48m, CUDA:1)
  latest_step: 92000 / 105000 (87.6%)
  latest_eval_return: 657.31 (at step 85000)
  status: RUNNING — 估计还需 ~30-45 min

009a_baseline_s2:
  process: alive (running 13h04m, CUDA:0)
  latest_step: 336000 / 500000 (67.2%)
  latest_eval_return: 919.23 (at step 335000)
  status: RUNNING — eval_return 在 215K 之后已收敛在 900-960 区间

GPU utilization:
  cuda:0: 25%, 4165/97887 MiB  (009a_baseline)
  cuda:1: 42%, 4167/97887 MiB  (008e_v3)
```

009a baseline s2 eval_return 趋势（关键节点）：

| step | eval_return |
|------|-------------|
| 65K | 688.9 |
| 105K | 836.5 |
| 135K | 876.1 |
| 215K | **956.0** (peak) |
| 285K | 960.2 (peak) |
| 335K | 919.2 |

---
