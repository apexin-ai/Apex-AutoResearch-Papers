# paper section4 composition draft

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_section4_composition_draft_20260514T051358_result.json`
- **Structured JSON:** [`de8284323f413261370e.json`](../../sessions/de/de8284323f413261370e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`register_artifact` 工具在当前环境中不可用（可能是 MCP server 未暴露）。

文件已写到：
`artifacts/section4_composition_draft.tex`

### 结构概览

1. **Constraint Composition** — 定义 $G(t)$, $S(t)$, conjunction $M_{\text{final}} = M_{\text{grammar}} \wedge M_{\text{semantic}}$；解释 asymmetric enabling dependency（grammar 是 semantic 的前提）
2. **Grammar-First Invariant** — 形式化 $S(t) \cap G(t) \neq \emptyset$ 前提条件；描述违反后果（argmax 选中 grammar-invalid token → crash）；resolution 策略（阈值检查 + skip semantic masking）；优先级设计原则（structural integrity > type compliance）
3. **Decidability Taxonomy** — local（entity/relation vocabulary → grammar CFG）、prefix-decidable（domain/range → semantic layer + stateful registry）、non-local（forward coreference → 超出单 pass 范围，引向 S2 和 limitations）

需要手动注册 artifact 或后续由 worker 补注册。

---
