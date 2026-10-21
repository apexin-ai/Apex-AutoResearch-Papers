# paper section3 violation landscape

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_section3_violation_landscape_20260514T061352_result.json`
- **Structured JSON:** [`65b465c99fa58b5799ed.json`](../../sessions/65/65b465c99fa58b5799ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/section3_violation_landscape.tex` 并注册。

Section 结构：
- **§3.1 Experimental Setup** — 数据集/模型/4类 violation 定义
- **§3.2 Violation Distribution** — 跨数据集对比，核心发现：DR 由 constraint tightness 驱动而非 ontology size；DocRED RV 高达 28.9% 反映 vocabulary capacity 瓶颈
- **§3.3 Per-Relation Analysis** — 7 个 relation 的 DR 分布（42.4%→0%），与 constraint tightness 正相关
- **§3.4 Prompt Insufficiency** — schema-informed prompting 整体有效但 per-relation 不可靠（Evaluate-for +5.8pp），且随 ontology 复杂度衰减（DocRED ↓31% vs SciERC ↓62%），motivate decoding-time enforcement

所有数字与 registry 一致，引用了 Table 2 (`\ref{tab:prompt_comparison}`)、Figure 2 (`\ref{fig:per_relation_dr}`)、三篇文献。

---
