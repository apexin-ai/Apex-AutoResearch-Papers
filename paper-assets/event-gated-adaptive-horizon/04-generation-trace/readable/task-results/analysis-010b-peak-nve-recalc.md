# analysis 010b peak nve recalc

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_010b-peak-nve-recalc_20260517T203809_result.json`
- **Structured JSON:** [`4f02783155e7708e95e3.json`](../../sessions/4f/4f02783155e7708e95e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结果：**

- **peak_step** = 65000
- **peak NVE** = **8.27×**（010b V/E = 3.183，baseline avg V/E = 0.385）
- **与论文 14.59× 不一致**

010b 在 step 65000 出现 V/E 尖峰，原因是 eval_return 极低（22.67）而 value_mean 维持高位（72.15）——这是 value 严重高估的信号。baseline 在同步的 V/E 约 0.36–0.41，平均 0.385。比值 3.183/0.385 ≈ 8.27×。

14.59× 的差异可能来自原始计算使用了不同口径（例如单 baseline seed、不同的 value/eval 字段、或不同的 normalization）。

---
