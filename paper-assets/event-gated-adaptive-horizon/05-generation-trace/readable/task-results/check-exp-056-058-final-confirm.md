# check exp 056 058 final confirm

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_056_058_final_confirm_20260524T002158_result.json`
- **Structured JSON:** [`f5777c601af291aa349f.json`](../../sessions/f5/f5777c601af291aa349f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已提取。汇总如下：

---

## exp_056 PegInsertion frozen s1（bjb1-40020）

| 项目 | 值 |
|------|-----|
| **进程状态** | 已退出（PID 346430 不存在） |
| **total_steps** | 222,400 |
| **212.5K 后新数据** | 无 — 212.5K 是最终 eval 点 |
| **ve_ratio_peak** | **11.321 @ 82.5K** |
| **ve_ratio_final** | 1.193 @ 212.5K |
| **eval_return_peak** | **24.42 @ 132.5K** |
| **eval_return_final** | 4.37 @ 212.5K |
| **NVE 分类** | **NVE** — ve_ratio 从 peak 11.3 大幅衰退到 1.19，eval 从 24.4 跌到 4.4，后半程持续下行无恢复 |
| **最终 checkpoint** | `checkpoint_202500.pt` |

ve_ratio 轨迹：0.32→0.98→1.84→1.97→5.42→4.05→8.41→**11.32**→3.72→3.03→2.20→2.43→0.84→2.19→2.20→0.65→1.09→1.07→0.47→0.71→1.19

eval 轨迹：2.0→5.8→9.3→9.2→12.3→5.9→10.0→5.4→3.6→8.7→9.6→12.3→10.1→**24.4**→7.7→6.2→16.9→8.8→7.5→15.4→8.7→4.4

---

## exp_058 Cheetah frozen s1（bjb1-45299）

| 项目 | 值 |
|------|-----|
| **进程状态** | 已退出（PID 164830 不存在） |
| **total_steps** | 224,000 |
| **ve_ratio** | **无此指标**（metrics 中不含 civo/ve_ratio） |
| **eval_return_peak** | **191.74 @ 25K** |
| **eval_return_final** | 82.82 @ 215K |
| **train_return_peak** | 273.99 @ 28K |
| **train_return_final** | 60.63 @ 224K |
| **NVE 分类** | **NVE** — eval 从 peak 191.7 (25K) 急跌，后半程在 50-92 区间震荡无恢复趋势，最终 82.8 仅 peak 的 43% |
| **最终 checkpoint** | `checkpoint_225000.pt` |

eval 轨迹：13.5→99.8→**191.7**→190.6→49.8→145.3→91.5→82.4→58.5→49.8→63.5→71.6→92.6→74.0→92.4→91.4→74.8→83.4→66.3→82.5→80.5→82.8

---

两个 frozen 实验均为 **NVE**，peak 出现在训练前期后持续衰退，数据锁定确认完毕。

---
