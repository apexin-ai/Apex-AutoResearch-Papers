# paper number consistency audit v2

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_number_consistency_audit_v2_20260514T122819_result.json`
- **Structured JSON:** [`4030ae88bd6fee26bbd3.json`](../../sessions/40/4030ae88bd6fee26bbd3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**审查结果：119 matched / 0 mismatched / 1 partially verifiable**

论文6个 .tex 文件中的所有定量数字与服务器 canonical 数据一致。逐一核对了：

- **Tables 2–5** 中所有数值（per-phase medians、unpaired median_diff、paired d_z、per-problem paired median_diff、95% CIs）
- **正文**中所有 Cohen's d、p 值、Spearman ρ、amplification 倍数、growth rate ratios
- **Table 6** 中所有 ΔGini 和 ΔCV 数值
- **entropy redistribution** 的具体 ΔH 值
- 跨模型比较的所有数字

唯一标记为 ⚠️ 的是 discussion.tex 中 s=0.35 supplementary experiment 的 II_high=0.105，该值来自 log 文件而非结构化 JSON，但 log 中数值（0.1051）与论文一致。

报告已注册到 `artifacts/number_consistency_audit_v2.md`。

---
