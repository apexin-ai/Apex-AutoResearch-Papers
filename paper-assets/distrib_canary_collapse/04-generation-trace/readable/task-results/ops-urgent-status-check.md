# ops urgent status check

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent-status-check_20260515T011215_result.json`
- **Structured JSON:** [`9d6d18f028e5522be8f5.json`](../../sessions/9d/9d6d18f028e5522be8f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇报

### 1. alpha_sweep_a025_s42_v3

**状态**: RUNNING — 正在训练 gen_10（最后一代）
**进度**: gen_0~gen_9 已完成，gen_10 训练中 36% (1810/5000 steps, ~15.93 it/s)
**GPU**: 占用 12522 MiB，无报错

**关键 metrics (gen_0 → gen_9)**:

| 指标 | gen_0 | gen_9 | 变化 |
|------|-------|-------|------|
| token_entropy | 3.2342 | 3.1197 | -3.5% |
| ece | 0.0108 | 0.0192 | +77% |
| perplexity | 26.95 | 22.51 | -16.5% |
| distinct_1 | 0.0982 | 0.0590 | **-39.9%** |
| distinct_2 | 0.5178 | 0.2290 | **-55.8%** |
| distinct_3 | 0.8127 | 0.3438 | **-57.7%** |
| mauve | 0.0341 | 0.0167 | -51.0% |

多样性指标（distinct_1/2/3）大幅下降，collapse 信号明显。预计 ~20 分钟完成 gen_10。

---

### 2. plan_006_s42

**状态**: RUNNING — 正在训练 gen_3
**进度**: gen_0~gen_2 已完成（3/20 gens），gen_3 训练中 37% (3730/10000 steps, ~15.81 it/s)
**GPU**: 占用 12522 MiB，无报错

**关键 metrics (gen_0 → gen_1 → gen_2)**:

| 指标 | gen_0 | gen_1 | gen_2 |
|------|-------|-------|-------|
| token_entropy | 3.2342 | 1.5253 | **1.2962** |
| ece | 0.0108 | 0.3268 | **0.3781** |
| perplexity | 26.95 | 185.68 | **380.41** |
| distinct_1 | 0.0982 | 0.0975 | 0.0846 |
| distinct_2 | 0.5178 | 0.5141 | 0.4390 |
| distinct_3 | 0.8127 | 0.8104 | 0.7141 |
| effective_rank | 46.61 | 66.77 | 79.39 |

collapse 更剧烈：仅 2 代 token_entropy 从 3.23 降至 1.30，ECE 从 0.01 爆到 0.38，perplexity 从 27 飙到 380。多样性也开始下降。此实验总共 20 gen，按当前速度预计还需较长时间。

**两个实验均无 error，进程正常运行。**

---
