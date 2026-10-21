# analysis 8b scaling summary

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_8b-scaling-summary_20260512T112417_result.json`
- **Structured JSON:** [`4a148b0c0f8a35c78be8.json`](../../sessions/4a/4a148b0c0f8a35c78be8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。关键分析结论：

**8B cls-cwm gap**: 均值 2.62±0.28pp，两 seed 一致（2.42, 2.81pp）。4B→8B 放大约 2.9x，三个 metric 放大倍数高度一致（2.7-3.2x）。

**Gap 放大机制**: CWM 4B→8B 仅 +0.16pp（触及任务天花板），classification +2.07pp。瓶颈在 BPE token-level 的生成难度，非模型容量。

**Pillar 1 evidence 强度**: 中-强。方向性证据充分（两 seed 一致 + 三 metric 一致），但只有 2 个 model size 点，无法确认 scaling 函数形状。

**不建议补跑第 3 个 8B seed**——gap 变异系数仅 10.7%，优先级应转向 repo-level 实验 debug。

---
