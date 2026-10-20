# check bjb1 40020 nve snapshot

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bjb1_40020_nve_snapshot_20260520T051742_result.json`
- **Structured JSON:** [`02773991f7f67b9534df.json`](../../sessions/02/02773991f7f67b9534df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都训到 **45K step**，最新 checkpoint 就是 45K。以下是完整数据：

---

## exp_027_tcn_walker_s0_sigma02 (TCN baseline)

**当前步数: 45,000**

### Eval Checkpoint 表格

| Step | eval_return | value_mean | ve_ratio (NVE) | civo/alert |
|------|------------|------------|----------------|------------|
| 5K   | 35.57      | 0.001      | ~0.00003       | — (无记录) |
| 15K  | 150.63     | 2.893      | 0.0192         | 0.0        |
| 25K  | 199.36     | 19.176     | 0.0961         | 0.0        |
| 35K  | 278.16     | 52.171     | 0.1875         | 0.0        |
| 45K  | **315.64** | 94.982     | **0.3009**     | 0.0        |

### Train Return (最近几个 step，每 step 4 episodes)

| Step | train_return (4 eps) |
|------|---------------------|
| 36K  | 243, 273, 280, 252  |
| 40K  | 317, 288, 194, 344  |
| 44K  | 189, 222, 289, 306  |

---

## exp_028_rave_walker_s0_ceil15 (RAVE, ceil=1.5)

**当前步数: 45,000**

### Eval Checkpoint 表格

| Step | eval_return | value_mean | ve_ratio (NVE) | civo/alert |
|------|------------|------------|----------------|------------|
| 5K   | 31.55      | 0.001      | ~0.00003       | — (无记录) |
| 15K  | 99.39      | 2.991      | 0.0300         | 0.0        |
| 25K  | 155.29     | 19.848     | 0.1278         | 0.0        |
| 35K  | 180.10     | 44.410     | 0.2465         | 0.0        |
| 45K  | **166.91** | 71.448     | **0.4280**     | 0.0        |

### Train Return (最近几个 step，每 step 4 episodes)

| Step | train_return (4 eps) |
|------|---------------------|
| 36K  | 178, 175, 176, 140  |
| 40K  | 78, 96, 164, 94     |
| 44K  | 167, 162, 167, 162  |

---

## 关键判断

| 指标 | exp_027 (TCN) | exp_028 (RAVE) |
|------|--------------|----------------|
| eval_return @45K | **315.6** | **166.9** |
| NVE @45K | 0.30× | 0.43× |
| CIVO 发生? | **否** (0.30 < 1.5) | **否** (0.43 < 1.5) |
| vs baseline @45K (~450-514) | **远低于** baseline | **远低于** baseline |
| 趋势 | 持续上升 | **35K→45K 下降**（180→167，回落） |

两个实验 NVE 都远低于 1.5× 阈值，CIVO 未发生。但 exp_028 (RAVE) 在 35K→45K 出现 eval_return 回落（180→167），同时 NVE 从 0.25 跳到 0.43（value 增长快于 return），值得关注。两者性能都显著低于 baseline 的 450-514 水平。gate_dt 始终固定在 2.0（100% dt=2），gate 机制未激活。

---
