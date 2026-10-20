# ops check both experiments

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-both-experiments_20260515T041623_result.json`
- **Structured JSON:** [`eb4f0296a923b52af77d.json`](../../sessions/eb/eb4f0296a923b52af77d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。汇总如下：

---

## 实验 1: alpha_sweep_a050_s42 (cuda:1)

**进度**: 7/11 gens 完成 (gen_0 → gen_6)，gen_7 生成中（训练已完成，正在采样）

| gen | entropy | ece | ppl | d1 | d2 | d3 |
|----:|--------:|----:|----:|---:|---:|---:|
| 0 | 3.2342 | 0.0108 | 26.95 | 0.0982 | 0.5178 | 0.8127 |
| 1 | 2.5174 | 0.0669 | 22.96 | 0.0975 | 0.5141 | 0.8104 |
| 2 | 2.4984 | 0.0871 | 26.38 | 0.0827 | 0.4311 | 0.7153 |
| 3 | 2.5644 | 0.0880 | 27.48 | 0.0756 | 0.3838 | 0.6401 |
| 4 | 2.5486 | 0.0933 | 28.69 | 0.0706 | 0.3346 | 0.5493 |
| 5 | 2.5461 | 0.0978 | 29.94 | 0.0675 | 0.3089 | 0.5048 |
| 6 | 2.5670 | 0.0981 | 30.19 | 0.0658 | 0.2897 | 0.4663 |

**趋势**: entropy 从 3.23 骤降到 ~2.55 后稳定；ECE 从 0.01 上升到 ~0.10；distinct_N 持续下降（collapse 明显）；ppl 缓慢上升。

**剩余**: ~3.5 gens（gen_7 采样中 + gen_8/9/10），每 gen ~8 min，预计 **~30 min** 完成。

---

## 实验 2: plan_006_s42 (cuda:0, extended_20gen)

**进度**: 9/20 gens 完成 (gen_0 → gen_8)，gen_9 训练中（6608/10000 steps, 65%）

| gen | entropy | ece | ppl | d1 | d2 |
|----:|--------:|----:|----:|---:|---:|
| 0 | 3.2342 | 0.0108 | 26.95 | 0.0982 | 0.5178 |
| 1 | 1.5253 | 0.3268 | 185.68 | 0.0975 | 0.5141 |
| 2 | 1.2962 | 0.3781 | 380.41 | 0.0846 | 0.4390 |
| 3 | 1.2141 | 0.3986 | 568.76 | 0.0798 | 0.4025 |
| 4 | 1.2192 | 0.4093 | 734.41 | 0.0782 | 0.3890 |
| 5 | 1.1711 | 0.4223 | 930.22 | 0.0780 | 0.3867 |
| 6 | 1.1343 | 0.4322 | 1187.47 | 0.0780 | 0.3865 |
| 7 | 1.1313 | 0.4371 | 1389.60 | 0.0780 | 0.3865 |
| 8 | 1.1402 | 0.4384 | 1566.03 | 0.0780 | 0.3865 |

**趋势**: 比 a050 **崩塌得更剧烈** — entropy 降到 ~1.13（vs a050 的 ~2.55），ECE 高达 0.44（vs 0.10），ppl 爆涨到 1566（vs 30）。distinct_1/2 在 gen_5 后已完全收敛不再变化，进入稳态 collapse。

**剩余**: gen_9 训练还剩 ~3400 steps (~3.5 min)，之后 gen_10-19 共 11 gens，每 gen ~12-15 min（10000 steps），预计 **~2.5 小时** 完成。

---

**总结**: 两个实验均在正常运行，双 GPU 满载。a050_s42 约 30 min 后完成；plan_006_s42 约 2.5 小时后完成。

---
