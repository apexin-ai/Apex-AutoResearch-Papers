# paper section6 relwork outline

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_section6_relwork_outline_20260514T053338_result.json`
- **Structured JSON:** [`32d7b7735ee48b590e83.json`](../../sessions/32/32d7b7735ee48b590e83.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/section6_relwork_outline.tex` 并注册。结构概要：

| Paragraph | Topic Sentence 定位 | Key Citations | Differentiation |
|-----------|-------------------|---------------|-----------------|
| **Grammar-Constrained Decoding** | CFG 约束保证结构合法性 | XGrammar, Outlines, LMQL, DOMINO, ASAp | OntoCoDec grammar 层基于此，但这些方法止于语法层，无法处理 domain/range |
| **Vocabulary/Type-Constrained** | 词汇级限制输出到合法标识符 | GENRE, GenIE, GCD, NeuroLogic | 限制"哪些 token"但不限制"哪些类型组合"对特定 relation 合法 |
| **Structural Constraints (Training)** | 通过训练/prompt 编码 IE 结构 | UIE, GoLLIE, CodeIE, ADELIE | Soft guidance vs. OntoCoDec 的 hard enforcement，两者互补 |
| **Post-hoc Ontology Validation** | 生成后验证 ontology 合规 | ODKE+, Upadhyay'23, Regino'25, EnriCo | Post-hoc 浪费 14-15% 计算（reject），OntoCoDec 在解码时 prevent |
| **Quality Concerns** | 约束解码降低推理质量的担忧 | Let Me Speak Freely, CRANE (ICML'25), Hidden Cost, Snowballing | OntoCoDec F1 无损实证回应；IE 属 extraction 非 reasoning，影响有限 |
| **Our Approach** | 三句话定位 OntoCoDec 独特性 | — | 首个 ontology→decoding semantic constraint 编译；stateful cross-field enforcement；training-free + zero cost |

每段末有 `% TODO` 标注需补充完整段落的位置。

---
