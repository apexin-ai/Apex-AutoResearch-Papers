# research tightness ablation feasibility

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_tightness_ablation_feasibility_20260515T063131_result.json`
- **Structured JSON:** [`0c7f3f2a7fa32ebabf22.json`](../../sessions/0c/0c7f3f2a7fa32ebabf22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写到 `artifacts/tightness_ablation/feasibility_report.md`。核心结论：

**不推荐做完整 tightness ablation 实验。**

关键发现：
- Schema 是 JSON 格式，编译链路全自动（修改 JSON → `OntologyCompiler` 重编译 → 新 LogitsProcessor），技术上完全可行
- 但投入 ~37 GPU hours，且人为修改 schema 的实验设计科学合理性存疑（收紧约束会 confound recall ceiling）
- SciERC (τ\_avg=0.333) vs DocRED (τ\_avg=0.842) 已经是天然的 tightness 对比，grammar-first fallback 在 DocRED 触发而 SciERC 不触发就是直接证据

**推荐替代**：对 DocRED 96 个 relation 按 τ 分 3 组做 post-hoc 分析（零推理成本，~2 小时开发），作为 tightness 效应的 within-dataset 证据。如果审稿人明确要求 controlled ablation 再执行。

---
