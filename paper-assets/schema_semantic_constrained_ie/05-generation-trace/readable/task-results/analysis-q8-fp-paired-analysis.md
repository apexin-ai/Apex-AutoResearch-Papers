# analysis q8 fp paired analysis

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_q8_fp_paired_analysis_20260515T110950_result.json`
- **Structured JSON:** [`b6907f4653cd46e840c0.json`](../../sessions/b6/b6907f4653cd46e840c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/rebuttal/q8_fp_analysis_report.md`。

核心发现：

- **净 FP 变化几乎为零**：constrained 仅比 unconstrained 多 3 个 FP（1613 → 1616，+0.2%）
- **FP 是"置换"而非"累积"**：constraint 移除了 68 个 FP（主要是无效 relation type），同时引入 71 个新 FP（Type C = 4.4%）
- **Type C 主要机制**：59.2% 是 relation reassignment（无效 relation 被强制映射到最近的 valid relation），40.8% 是 novel pair（概率重分配导致新预测）
- **Type C 集中在高频 relation**：Feature-of / Used-for / Evaluate-for 占 73.2%，充当了 invalid relation 重定向的"catch-all"

---
