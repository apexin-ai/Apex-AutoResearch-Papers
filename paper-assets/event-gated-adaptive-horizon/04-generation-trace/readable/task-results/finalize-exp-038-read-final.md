# finalize exp 038 read final

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_finalize_exp_038_read_final_20260522T021010_result.json`
- **Structured JSON:** [`6fb424180ad7acb9569e.json`](../../sessions/6f/6fb424180ad7acb9569e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**exp_038 状态：已结束**（无相关进程存活）

**logdir 文件列表：**
```
eval_eps/  events.out.tfevents.*  latest.pt  metrics.jsonl  train_eps/
```
无 `eval.jsonl` 文件。

---

**metrics.jsonl 最后 5 行（step 224000）：**

| step | dataset_size | train_return | train_length | train_episodes |
|------|-------------|--------------|-------------|----------------|
| 220000 | 110000 | 109.73 | 500 | 220 |
| 224000 | 112000 | 202.45 | 500 | 224 |
| 224000 | 112000 | 164.84 | 500 | 224 |
| 224000 | 112000 | 61.23 | 500 | 224 |
| 224000 | 112000 | 133.63 | 500 | 224 |

**最后一条 ve_ratio 记录（step 215000）：**

| 指标 | 值 |
|------|-----|
| civo/ve_ratio | 0.248 |
| civo/delta_ve | -0.022 |
| civo/alert | 0.0 |
| gate_dt_mean | 2.0 |
| gate_dt_2_frac | 1.0 |
| gate_empirical_entropy | 0.0 |
| value_mean | 30.96 |
| EMA_005 / EMA_095 | 7.67 / 72.15 |
| fps | 7.51 |
| update_count | 52599 |

---
