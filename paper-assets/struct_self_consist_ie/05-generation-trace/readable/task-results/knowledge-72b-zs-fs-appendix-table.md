# knowledge 72b zs fs appendix table

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_72b-zs-fs-appendix-table_20260520T013450_result.json`
- **Structured JSON:** [`4535a65a2adf8f578a5d.json`](../../sessions/45/4535a65a2adf8f578a5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

表格已写入 `artifacts/tab_72b_zs_vs_fs_appendix.tex`。

**内容总结：**

6 行配置（3 datasets × ZS/FS），核心发现：

- **Construction 仅 SciERC ZS 显著**：Δ=**+1.53pp**, p=.008。其余 5 个条件 Δ 均在 ±0.4pp 以内且不显著。
- **FS 提升基础 F1 但不改善 construction**：SciERC +6.2pp（.399→.461），CoNLL +3.3pp（.712→.745），FewNERD 略降（.628→.619）。但 FS 条件下所有 construction Δ 均不显著（p ∈ [.401, .544]）。
- **Signal 质量**：FS 在 CoNLL 上大幅提升所有 signal（SJ +.14, FK +.15），但在 SciERC/FewNERD 上变化有限。FK ρ 数据完整（ZS 值来自 memory.md）。
- **Degeneracy**：CoNLL 两个 regime 均 ~68-70% 高退化；SciERC ZS 最低（21.0%），是唯一通过 dual-gating 的条件。

---
