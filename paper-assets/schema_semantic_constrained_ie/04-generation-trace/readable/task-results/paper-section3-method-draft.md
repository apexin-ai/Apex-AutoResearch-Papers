# paper section3 method draft

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_section3_method_draft_20260514T054115_result.json`
- **Structured JSON:** [`9aac554d81e4b4731476.json`](../../sessions/9a/9aac554d81e4b4731476.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `artifacts/section3_method_draft.tex` 并注册到 manifest。

结构概要：
- **3.1 Problem Formulation** — IE as structured generation、ontology schema $\mathcal{O}=(\mathcal{E},\mathcal{R},\operatorname{dom},\operatorname{range})$、type-validity 定义、三类 constraint decidability
- **3.2 Grammar Layer** — JSON Schema → EBNF → XGrammar logit masking；消除 RV/ET，不影响 F1；明确不处理 dom/range
- **3.3 Semantic Layer** — Entity Registry 动态构建、Position Detection、Head/Tail type dynamic masking、grammar-semantic conjunction (Eq.~4)、enabling dependency 实证（semantic-only DR 仅降 24%）、grammar-first invariant fallback，详细分析 refer Section 4
- **3.4 Decoding Strategies** — S1 single-pass（推荐）vs S2 two-pass（ablation），含 SciERC 对比数据

符号体系与 Section 4/5 保持一致：$G(t)$, $S(t)$, $M_{\text{grammar}}$, $M_{\text{semantic}}$, $M_{\text{final}}$。所有数字与 registry 一致。

---
