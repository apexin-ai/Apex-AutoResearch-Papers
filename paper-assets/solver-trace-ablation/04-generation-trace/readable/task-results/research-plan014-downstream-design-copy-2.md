# research plan014 downstream design

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_plan014-downstream-design_20260514T020422_result.json`
- **Structured JSON:** [`060e0dee49aa07645016.json`](../../sessions/06/060e0dee49aa07645016.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

设计文档已写入 `artifacts/plan014_design.md`。

核心设计：

**主方案 — Label-Prediction Accuracy**：用 checkpoint 生成 K=8 个 FOL formalization，对每个做 3-way entailment 分类（prove 原结论 → true，prove 否定结论 → false，均失败 → unknown），与 ground-truth label 比较。ISR 与 label accuracy 的 Spearman 相关性 + Best-of-N selection 实验直接回答 "高 ISR 是否意味着更好的 formalization"。

关键优势：
- **与 ISR 完全正交**：ISR 度量 component necessity，label accuracy 度量 semantic correctness
- **工程量极低**：只需在现有 Prover9 pipeline 上加 negation-prove
- **GPU 仅需 ~20 min**（inference），其余全是 CPU-bound 的 Prover9 调用，可与训练并行
- **Best-of-N framing** 同时证明了 ISR 的实用价值（作为 selection criterion）

预期 7-9h 实现，1.5h 运行，留有充足 buffer 应对 DDL。

---
