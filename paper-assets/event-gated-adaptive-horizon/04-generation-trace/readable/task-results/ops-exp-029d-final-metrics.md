# ops exp 029d final metrics

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp_029d_final_metrics_20260521T033709_result.json`
- **Structured JSON:** [`c475b019e859c5c1108f.json`](../../sessions/c4/c475b019e859c5c1108f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_029d 状态汇总

### 进程状态
**PROCESS_DEAD** — 进程已终止。

### GPU 状态
| GPU | Util | Mem Used | Mem Total |
|-----|------|----------|-----------|
| 0 | 0% | 1 MiB | 24564 MiB |
| 1 | 10% | 3309 MiB | 24564 MiB |

### Metrics 轨迹（290 lines, 78 unique steps, range 0–224000）

最后一个 eval 在 step 215000（最终 step 224000 只有 train_return 无 eval）。

| step | eval_return | civo/ve_ratio | value_mean | gate_dt_mean | gate_entropy_ratio |
|-----:|------------:|--------------:|-----------:|-------------:|-------------------:|
| 5k | 31.69 | — | 0.00 | 2.0 | 0.0 |
| 15k | 159.09 | 0.0215 | 3.42 | 2.0 | 0.0 |
| 25k | 155.75 | 0.1715 | 26.72 | 2.0 | 0.0 |
| 35k | 190.82 | 0.3124 | 59.62 | 2.0 | 0.0 |
| 45k | 137.07 | 0.6952 | 95.30 | 2.0 | 0.0 |
| 55k | 210.72 | 0.5983 | 126.08 | 2.0 | 0.0 |
| 65k | 189.47 | 0.8630 | 163.54 | 2.0 | 0.0 |
| 75k | 253.24 | 0.7914 | 200.43 | 2.0 | 0.0 |
| 85k | 259.54 | 0.8552 | 221.98 | 2.0 | 0.0 |
| **95k** | **349.56** | **0.6658** | **232.74** | 2.0 | 0.0 |
| 105k | 71.79 | 3.0421 | 218.37 | 2.0 | 0.0 |
| 115k | 69.78 | 2.4871 | 173.53 | 2.0 | 0.0 |
| 125k | 61.45 | 2.4326 | 149.47 | 2.0 | 0.0 |
| 135k | 141.78 | 0.9224 | 130.76 | 2.0 | 0.0 |
| 145k | 98.66 | 1.1408 | 112.55 | 2.0 | 0.0 |
| 155k | 88.86 | 1.0602 | 94.20 | 2.0 | 0.0 |
| 165k | 86.22 | 0.9095 | 78.41 | 2.0 | 0.0 |
| 175k | 123.53 | 0.5557 | 68.64 | 2.0 | 0.0 |
| 185k | 153.71 | 0.3956 | 60.81 | 2.0 | 0.0 |
| 195k | 68.84 | 0.7798 | 53.67 | 2.0 | 0.0 |
| 205k | 63.71 | 0.7473 | 47.61 | 2.0 | 0.0 |
| 215k | 104.51 | 0.4072 | 42.55 | 2.0 | 0.0 |

### 关键观察

1. **峰值 step 95k**: eval_return=349.56, value_mean=232.74 — 之后崩塌
2. **105k 开始剧烈下降**: eval_return 从 349→71, ve_ratio 飙升到 3.04（value 严重高估）
3. **gate 完全未激活**: gate_dt_mean=2.0, gate_entropy_ratio=0.0 全程不变 — gate 网络没学到东西，始终输出固定 dt=2
4. **value_mean 单调下降**: 从 232→42，value function 在崩塌后持续退化
5. **停在 224k**: 进程已死，checkpoint 在 `latest.pt`(220MB)，最后写入 11:30

---
