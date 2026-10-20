# paper section6 relwork revision

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_section6_relwork_revision_20260514T054538_result.json`
- **Structured JSON:** [`f132469029263de72bfa.json`](../../sessions/f1/f132469029263de72bfa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修订完成。变更汇总：

**新增段落：**
- **§Semantic Constrained Decoding for Code** — 插入在 §Grammar-Constrained 和 §Vocabulary/Type-Constrained 之间，引用 Synchromesh (`synchromesh_neurips2022`)、MGD (`mgd_neurips2023`)、PLDI'25 (`pldi2025_type_constrained_codegen`)，段尾定位句明确 OntoCoDec 首次将 code 领域 type-constrained decoding 迁移到 IE

**6 篇论文归位：**
| 论文 | 放置位置 |
|------|---------|
| Roth & Yih (AAAI'04) | §Vocabulary/Type-Constrained 开头，作为历史起点 |
| AdaKGC (EMNLP'23) | §Vocabulary/Type-Constrained，GenIE 之后 |
| KnowCoder (ACL'24) | §Structural Constraints，GoLLIE 之后 |
| SPIRES/OntoGPT (Bioinformatics'24) | §Post-hoc Ontology Validation |
| OntoLogX (2025) | §Post-hoc Ontology Validation |
| EKAW'24 ontology beam | §Post-hoc Ontology Validation（soft constraint 中间路线） |

**措辞修正：**
1. "14-15% rejection rate" → "14-15% of generated triples contain domain/range violations"
2. EnriCo 从 §Post-hoc Validation 移到 §Structural Constraints，明确标注为 ASP decoding-time constraint

**注意：** 所有新增引用的 cite key 使用 `literature_map.yaml` 中的 `id` 字段（如 `synchromesh_neurips2022`），需确保 `.bib` 文件中有对应条目。

---
