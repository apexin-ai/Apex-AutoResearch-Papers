# ops full status collect

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_full-status-collect_20260519T085800_result.json`
- **Structured JSON:** [`6eb029ee07ac948876ac.json`](../../sessions/6e/6eb029ee07ac948876ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态总览

### GPU 状态

| GPU | 型号 | VRAM | 利用率 | 进程 |
|-----|------|------|--------|------|
| 0 | RTX PRO 6000 Black | 4776/97887 MiB | 38% | cheetah_s4 |
| 1 | RTX PRO 6000 Black | 4776/97887 MiB | 34% | walker_s2 |

### 实验状态

| 实验 | 任务 | 当前step | 目标 | 进程 | 状态 |
|------|------|----------|------|------|------|
| exp_001_baseline_s4 | Walker s4 | 112K | 105K | 无 | **已完成** |
| exp_023_cheetah_s4_ext | Cheetah s4 | 304K | 300K | 运行中 | **已过目标，仍在跑** |
| exp_001_baseline_s2_ext | Walker s2 | 264K | 505K | 运行中 | 52% 进度 |

---

### exp_001_baseline_s4 (Walker, seed=4) — 已完成

| 指标 | 值 |
|------|----|
| eval_return@105K | **922.8** |
| peak eval_return | **922.8** (step 105K) |
| value_mean@final | 576.1 |
| ve_ratio@105K | 0.624 |

eval 曲线持续上升，105K 是最高点。

---

### exp_023_cheetah_baseline_s4_extended — 运行中

200K→300K eval_return 逐步数据：

| Step | eval_return |
|------|-------------|
| 204K | 301.7 |
| 212K | 405.9 |
| 222K | **570.5** |
| 232K | 540.1 |
| 242K | 470.6 |
| 252K | 543.4 |
| 262K | 460.2 |
| 272K | **642.3** ← peak |
| 282K | 494.5 |
| 292K | 496.8 |
| 302K | 580.0 |

**判断：震荡上行，非持续下降。** 200K→300K 区间在 300\~642 间大幅波动，但整体趋势高于 200K 前。Peak 642.3@272K 远高于 200K 前的 peak 537.0@194K。当前 302K 的 580.0 也处于高位。方差很大但没有崩溃迹象。

---

### exp_001_baseline_s2_extended (Walker, seed=2) — 运行中

| 指标 | 值 |
|------|----|
| 当前 step | 264K / 505K (52%) |
| 最新 eval_return@262K | **927.8** |
| 近 5 次 eval | 896.8→907.0→905.8→917.0→927.8 (稳步上升) |
| fps | 10.4 |

表现稳定且持续改善，预计还需约 5 小时完成。

---
