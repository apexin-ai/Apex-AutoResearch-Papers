# analysis exp 078 cheetah 008d s0

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_078_cheetah_008d_s0_20260525T142917_result.json`
- **Structured JSON:** [`f1ba6cdb8671deb2d1bd.json`](../../sessions/f1/f1ba6cdb8671deb2d1bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新（conclusion=success）。

---

## exp_078_cheetah_008d_s0 分析总结

**结论：CIVO confirmed (success)**

### 核心数据
- eval_return: peak 213.7 (35K) → collapse to 26.1 (75K) → partial recovery 119.5 (105K)
- ve_ratio: peak 2.3 (75K), CIVO detector triggered at 55K & 65K
- **NVE peak = 4.54 at step 55K**（远超 1.5 阈值）

### 与 baseline (exp_077) 对比
| | exp_078 (gate_dt=2) | exp_077 (baseline) |
|---|---|---|
| eval_return_105K | 119.5 | 448.1 |
| eval_return_peak | 213.7 (35K) | 448.1 (105K) |
| ve_ratio_peak | 2.3 (75K) | 0.739 (85K) |
| CIVO alert | triggered | never |

exp_078 性能被 baseline 碾压（final return 低 73%），且呈现典型 CIVO 模式：先学后崩，value estimation 严重膨胀。

### 与 parent seed (exp_010b, seed=1) 对比
| | exp_078 (seed=0) | exp_010b (seed=1) |
|---|---|---|
| NVE peak | 4.54 | 8.27 |
| eval_return_final | 119.5 | 51.7 |
| CIVO | confirmed | confirmed |

两个 seed 均确认 CIVO。seed=1 崩溃更严重（NVE 8.27, final 51.7），seed=0 有部分恢复（105K 回到 119.5），但 CIVO pattern 一致：**跨 seed 复现成功**。

### 附注
- gate_dt_2_frac 始终 = 1.0（fixed gate 未发生自适应变化，符合预期）
- 训练正常完成，EXIT_CODE=0

---
