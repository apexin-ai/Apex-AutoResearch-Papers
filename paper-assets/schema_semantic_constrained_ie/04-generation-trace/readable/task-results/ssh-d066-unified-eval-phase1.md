# ssh d066 unified eval phase1

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d066_unified_eval_phase1_20260520T015708_result.json`
- **Structured JSON:** [`22e37d566781936d061e.json`](../../sessions/22/22e37d566781936d061e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/_project/report/d066_unified_eval_phase1.md`。

核心发现：

**唯一显著变化**：Llama DocRED LoRA S1（Row 4）
- E-F1: 85.23 → 83.94 (−1.29pp)
- R-F1: 44.23 → 43.78 (−0.45pp)
- 旧值排除了 PF 文档，导致 S1 看起来比 unc 高 1.30pp，这是评估方法不一致造成的假象

**对 narrative 影响**：Table 3 中 Llama DocRED 的 ΔR-F1 从 +0.51pp 缩小到 +0.06pp，ΔE-F1 从 +1.30pp 缩小到 +0.01pp。"constrained decoding helps Llama stay on-schema" 的 claim 需要修改为更保守的表述。其他所有行（14/16）的 E-F1/R-F1 不变或变化 <0.5pp。

---
