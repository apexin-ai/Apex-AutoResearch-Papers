# analysis exp 023a cheetah baseline s0

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_023a_cheetah_baseline_s0_20260517T203313_result.json`
- **Structured JSON:** [`f356b4337dddfcd97f83.json`](../../sessions/f3/f356b4337dddfcd97f83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## 结果摘要

**结论：SUCCESS** — 健康的 baseline。

| 指标 | 值 |
|------|-----|
| eval_return_final | **624.7** (205K) |
| eval_return_peak | **624.7** @ 205K |
| Last-5 eval mean | **554.4** |
| ve_ratio 范围 | 0.0–0.9 |
| CIVO | 185K有一次瞬态警报，随后恢复 |
| 训练总步数 | ~212K env steps |

**与 023b 对比：** 023a 略优于 023b（final 624.7 vs 520.3, last-5 mean 554.4 vs 542.2）。两个seed表现一致，无持续性collapse。

**CIVO 分析：** 185K步 ve_ratio 短暂飙升至0.906触发警报，eval从591.5降至425.0，但20K步内完全恢复（195K: 596.4, 205K: 624.7）。属于RL训练中正常的seed variance，非真实CIVO collapse。

**NVE 归一化基准（两seed平均）：** Last-5 mean = 548.3, Peak = 598.8。

报告已注册：`art_20260517_741a5e`

---
