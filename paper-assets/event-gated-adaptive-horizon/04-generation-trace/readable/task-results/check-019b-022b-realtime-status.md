# check 019b 022b realtime status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_019b-022b-realtime-status_20260517T114517_result.json`
- **Structured JSON:** [`006edc56e33b3107c108.json`](../../sessions/00/006edc56e33b3107c108.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 实验进度报告

### exp_019b (PickCube, CIVO trigger, cuda:0)

| 指标 | 值 |
|---|---|
| **状态** | RUNNING (PID 649577, 99.6% CPU) |
| **已运行** | 7h 31min |
| **当前 step** | ~156,200 / 200,000 (78%) |
| **fps** | 5.2 |
| **Gate** | 固定 dt=2（gate_fixed_dt=2，非学习） |
| **预估剩余** | ~2.1 小时 |

**Eval 轨迹（全部 16 个 checkpoint）：**

| Step | Eval | Value | V/E |
|---:|---:|---:|---:|
| 2,500 | 0.8 | 0.00 | 0.001 |
| 22,500 | 24.9 | 17.60 | 0.707 |
| 52,500 | 3.7 | 20.85 | 5.657 |
| 102,500 | 8.4 | 5.54 | 0.662 |
| 122,500 | 13.6 | 4.95 | 0.365 |
| **132,500** | **26.9** (peak) | 4.35 | 0.162 |
| 142,500 | 14.5 | 4.17 | 0.288 |
| **152,500** | **7.6** | 4.16 | 0.544 |

**趋势分析：**
- **性能极差**：eval 始终在 3~27 范围波动，最新 7.6。对比 baseline 019a_v2（eval ~1050），差距超 100x。
- **Value 持续下降**：从 step 32500 的 27.17 单调下降到 4.16，agent 对自身能力的预估在崩塌。
- **V/E 最近两轮上升**（+0.126, +0.256）但原因是 eval 崩得比 value 快，不是好信号。
- **CIVO ALERT level=2** 已在 step 152500 触发（ve_ratio=0.544, delta_ve=0.256）。
- **结论**：实验基本失败，gate 固定 dt=2 在 PickCube 上没有学到有效策略。

---

### exp_022b (Walker Walk, no curriculum, cuda:1)

| 指标 | 值 |
|---|---|
| **状态** | RUNNING (PID 670559, 1225% CPU) |
| **已运行** | ~55 min |
| **当前 step** | ~36,000 / 105,000 (34%) |
| **fps** | 10.1 |
| **Gate** | 学习中（无 curriculum，phase1=0, phase2=0） |
| **预估剩余** | ~1.8 小时 |

**Eval + Gate 轨迹：**

| Step | Eval | Value | V/E | dt_mean | dt1_frac | entropy | dt_std |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 5,000 | 37.4 | 0.00 | 0.000 | 4.40 | 0.065 | 2.01 | 1.94 |
| 15,000 | 167.3 | 2.28 | 0.014 | 4.56 | 0.052 | 1.97 | 1.82 |
| 25,000 | **169.5** | 12.20 | 0.072 | 3.81 | 0.096 | 1.93 | 1.76 |
| 35,000 | 140.4 | 21.40 | 0.152 | 3.48 | 0.124 | 1.88 | 1.70 |

**Gate 学习趋势分析：**
- **dt_mean 下降** 4.40→3.48：gate 偏向选择更短的 horizon，但未退化到 dt=1。
- **dt1_frac 缓慢上升** 0.065→0.124：dt=1 使用率增加但仍只占 12.4%，gate 分布仍然多样。
- **entropy 缓慢下降** 2.01→1.88：gate 在逐步变得更确定，但下降速率温和，没有崩塌迹象。
- **dt_std 下降** 1.94→1.70：方差收缩，gate 选择更集中但未坍缩。
- **结论**：gate 在健康学习，没有退化到 dt=1 的信号。

**性能分析：**
- Eval 在 step 25K 达 169.5 后回落至 140.4（-17%），可能是 gate 分布调整期的暂时波动。
- 对比 baseline exp_001（eval=915.7@105K）：当前 34% 进度时 eval=140.4（baseline 终值的 15.3%）。如果性能非线性增长，还有追赶空间。
- **V/E ratio**：0→0.152，稳步上升，但远低于 NVE 阈值（1.5x），无过拟合信号。
- **无 CIVO alert**（civo/alert=0.0）。

---

### 总结

| 实验 | 状态 | 健康度 | 关键风险 | ETA |
|---|---|---|---|---|
| exp_019b | 78% 完成 | **差** | eval 极低（7.6 vs baseline 1050），CIVO L2 触发 | ~2.1h |
| exp_022b | 34% 完成 | **良好** | eval 轻微回落，需观察下一 checkpoint（45K）是否回升 | ~1.8h |

---
