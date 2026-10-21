# diagnose bjb1 verify and analyze 20260526

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_bjb1_verify_and_analyze_20260526_20260526T020546_result.json`
- **Structured JSON:** [`1a8e3451a3edc50ec460.json`](../../sessions/1a/1a8e3451a3edc50ec460.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕，汇总如下。

---

## 1. 新实验验证

| 实验 | PID | GPU | 状态 | 运行时间 | GPU 占用 |
|------|-----|-----|------|---------|---------|
| exp_098_cheetah_008a_s0 | 322486 (子进程 322491) | cuda:0 | Ss+ (存活) | 1h17m | 1309MiB |
| exp_099_cheetah_008a_s1 | 322767 (子进程 322772) | cuda:1 | Ss+ (存活) | 1h15m | 794MiB |

**状态: 两个实验均正常运行，GPU 已占用。**

---

## 2. exp_092_cheetah_no_dt_emb_s1 完整结果

**配置**: seed=1, gate_fixed_dt=2, no_dt_emb, 105K steps. EXIT_CODE=0 (完成)

| Step | eval_return | value_mean | ve_ratio | model_loss |
|------|------------|-----------|----------|-----------|
| 5K   | 9.0        | 0.0       | —        | 13.2      |
| 15K  | 129.6      | 1.2       | 0.009    | 3.7       |
| 25K  | 99.0       | 7.0       | 0.071    | 2.5       |
| 35K  | 59.7       | 13.9      | 0.233    | 2.5       |
| 45K  | 66.6       | 21.0      | 0.315    | 2.5       |
| 55K  | 39.0       | 27.4      | 0.703    | 2.4       |
| 65K  | 75.2       | 32.9      | 0.438    | 2.3       |
| 75K  | 79.7       | 35.3      | 0.443    | 2.3       |
| 85K  | 104.5      | 29.1      | 0.278    | 2.3       |
| 95K  | 114.1      | 25.6      | 0.224    | 2.3       |
| 105K | 77.3       | 23.1      | 0.299    | 2.3       |

- **eval_return_final**: 77.3
- **eval_return_peak**: 129.6 @15K
- **ve_ratio_peak**: 0.703 @55K
- **value_mean_peak**: 35.3 @75K
- **Gate**: gate_dt_mean=2.0, gate_dt_2_frac=1.0, gate_empirical_entropy=0.0 (固定 dt=2)
- **Checkpoint**: latest.pt (231MB), metrics.jsonl, events.out.tfevents

---

## 3. exp_093_cheetah_no_dt_emb_s2 完整结果

**配置**: seed=2, gate_fixed_dt=2, no_dt_emb, 105K steps. EXIT_CODE=0 (完成)

| Step | eval_return | value_mean | ve_ratio | model_loss |
|------|------------|-----------|----------|-----------|
| 5K   | 9.1        | 0.0       | —        | 13.2      |
| 15K  | 48.8       | 1.0       | 0.020    | 3.7       |
| 25K  | 64.6       | 6.2       | 0.096    | 2.6       |
| 35K  | 73.5       | 14.4      | 0.196    | 2.5       |
| 45K  | 123.2      | 23.1      | 0.188    | 2.4       |
| 55K  | 135.8      | 32.6      | 0.240    | 2.4       |
| 65K  | 200.8      | 43.3      | 0.216    | 2.4       |
| 75K  | 263.0      | 53.0      | 0.202    | 2.3       |
| 85K  | 153.9      | 57.9      | 0.376    | 2.3       |
| 95K  | 96.4       | 52.1      | 0.540    | 2.4       |
| 105K | 151.2      | 40.9      | 0.270    | 2.3       |

- **eval_return_final**: 151.2
- **eval_return_peak**: 263.0 @75K
- **ve_ratio_peak**: 0.540 @95K
- **value_mean_peak**: 57.9 @85K
- **Gate**: gate_dt_mean=2.0, gate_dt_2_frac=1.0, gate_empirical_entropy=0.0 (固定 dt=2)
- **Checkpoint**: latest.pt (231MB), metrics.jsonl, events.out.tfevents

---

## 4. NVE 计算

Baseline ve_ratio (mean of exp_077 s0 + exp_083 s1):
- baseline ve_ratio_peak = (0.739 + 0.6) / 2 = **0.670**
- baseline ve_ratio_105K = (0.611 + 0.6) / 2 = **0.606**

| 实验 | ve_ratio_peak | NVE_peak | ve_ratio_105K | NVE_105K |
|------|-------------|----------|-------------|----------|
| exp_092 s1 | 0.703 @55K | **1.050** | 0.299 | **0.494** |
| exp_093 s2 | 0.540 @95K | **0.807** | 0.270 | **0.446** |
| **mean** | 0.622 | **0.928** | 0.285 | **0.470** |

**NVE 判定**: no_dt_emb 条件的 NVE 均值接近 1.0 (peak) 但 final 显著低于 baseline (0.47)。两个 seed 差异大——exp_092 性能不稳定（15K 冲高到 129.6 后反复波动），exp_093 中期表现好（75K 峰值 263.0）但后期衰退明显。value_mean 在两个 seed 上都出现了从中后期开始的下降趋势（exp_092: 35.3→23.1, exp_093: 57.9→40.9），说明 value function 的估计在没有 dt embedding 的情况下后期不够稳定。

---
