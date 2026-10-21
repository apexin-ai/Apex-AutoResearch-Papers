# monitor training status check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training-status-check_20260514T072959_result.json`
- **Structured JSON:** [`44cda496da5396e83a65.json`](../../sessions/44/44cda496da5396e83a65.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据齐了。汇总如下：

---

## 实验 1: exp_008f_no_dt_embed_subsample_on_h8 (C2 causal control)

**状态**: RUNNING — GPU PID 127766, cuda:0, 2742 MiB | 进程 elapsed 2h38m

| 指标 | @45K | @55K (最新 eval) |
|------|------|---------|
| eval_return | 194.08 | 173.45 |
| value_mean | 53.43 | 67.90 |
| v/e ratio | 0.275 | 0.392 |
| baseline v/e | 0.331 | 0.404 |
| **normalized v/e** | **0.832x** | **0.969x** |
| fps | 6.70 | 6.97 |
| gate_dt | 100% dt=2 | 100% dt=2 |

**当前进度**: step 65K（65K eval 正在运行中，结果尚未写入）
**train_return @64K**: avg 263.3（282.6, 245.9, 210.1, 314.5）
**预计完成**: ~1h37m（基于 410 steps/min）

### v/e 趋势分析
normalized v/e 从 45K→55K 急升（0.832x → 0.969x），主要因为:
- eval_return **下降** (194 → 173)，而 value_mean **上升** (53 → 68)
- 65K 的 eval 结果将决定是否突破 1.0x 阈值
- train_return @64K（263）远高于 55K eval_return（173），存在 train-eval gap

**gate**: 完全 collapsed 到 dt=2，entropy=0。符合 C2 设计预期（dt_embed_dim=0 → gate 无法区分 dt）。

---

## 实验 2: exp_008e_v3_subsample_on_dt1_h15 (B+ confound control)

**状态**: RUNNING — GPU PID 126115, cuda:1, 4158 MiB | 进程 elapsed 3h01m

| 指标 | @65K | @75K (最新 eval) |
|------|------|---------|
| eval_return | 580.67 | 574.09 |
| value_mean | 235.05 | 300.51 |
| v/e ratio | 0.405 | 0.523 |
| baseline v/e | 0.563 | 0.719 |
| **normalized v/e** | **0.719x** | **0.728x** |
| fps | 6.87 | 7.01 |
| gate_dt | 100% dt=1 | 100% dt=1 |

**当前进度**: step 75K（75K eval 已完成，正在收集 76K+ 数据）
**train_return @72K**: avg 607.4（571.8, 626.5, 631.4, 600.1）
**预计完成**: ~1h12m（基于 415 steps/min）

### v/e 趋势
normalized v/e 稳定在 0.72x-0.73x，远低于 1.0x。eval_return 基本持平（581→574），健康。

---

## 关键发现

1. **008f 是焦点** — normalized v/e 已逼近 1.0x（0.969x @55K），65K eval 即将出结果。如果 eval_return 继续下降或 value_mean 继续上升，将突破 1.0x，意味着 C2 控制条件下 value 已被 confound。

2. **008e_v3 稳定** — normalized v/e = 0.728x，与 B+ confound control 假设一致（dt=1 固定 → gate 无变化空间 → value 不被 confound）。

3. **两个实验 gate 都完全 collapsed**（entropy=0）。008f→dt=2，008e_v3→dt=1，符合各自设计。

4. **无异常信号** — 两个进程正常运行，GPU 占用稳定，fps 无衰减。

---
