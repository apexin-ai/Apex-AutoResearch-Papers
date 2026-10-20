# monitor progress check critical

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_progress_check_critical_20260515T041433_result.json`
- **Structured JSON:** [`5b8a9f54583882e5b885.json`](../../sessions/5b/5b8a9f54583882e5b885.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
008e_v3_s2: RUNNING (PID 43437, 3h28m) step=68000/105000 (64.8%), latest eval_return=435.1@65K
009a_s2:    RUNNING (PID 142508, 18h42m) step=445000/500000 (89.0%), latest eval_return=963.7@435K
GPU 0: 0% util, 4165/97887 MiB (009a PID 142513)
GPU 1: 19% util, 4167/97887 MiB (008e PID 43442)
```

### 008e_v3_s2 eval 轨迹（含 ve_ratio）

| step | eval_return | value_mean | ve_ratio |
|------|-------------|------------|----------|
| 5K   | 39.3        | 0.002      | ~0       |
| 15K  | 180.9       | 3.9        | 0.022    |
| 25K  | 211.8       | *(trunc)*  | —        |
| 35K  | 320.4       | *(trunc)*  | —        |
| 45K  | 356.9       | *(trunc)*  | —        |
| 55K  | 418.3       | 172.9      | 0.413    |
| 65K  | 435.1       | 220.5      | 0.507    |

- `gate_dt_mean=1.0` 全程（符合 `gate_fixed_dt=1` 配置）
- 尚未到 95K+，与 seed=1 (869.9@105K) 的对比还需等后续 eval

### 009a baseline_s2 最近 5 个 eval

| step | eval_return |
|------|-------------|
| 395K | 966.9       |
| 405K | 948.0       |
| 415K | 957.1       |
| 425K | 939.4       |
| 435K | 963.7       |

已进入 940-967 平台期，预计 ~5-6 小时完成剩余 55K 步（按 fps≈7.4 估算约 2h，加上 eval 开销）。

---
