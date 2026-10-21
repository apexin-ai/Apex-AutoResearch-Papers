# research constrained decoding literature

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_constrained_decoding_literature_20260513T200558_result.json`
- **Structured JSON:** [`021e3d698342eec99141.json`](../../sessions/02/021e3d698342eec99141.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。三个维度共覆盖 40+ 篇论文，核心结论：

### Novelty 确认

**OntoCoDec 的核心创新点成立** — 没有先前工作在 LLM 解码时对 IE 任务执行 ontology domain/range type constraints。

Gap 结构：
| 约束层级 | IE 任务? | 解码时? | 现有工作 |
|---------|---------|--------|---------|
| 句法 (valid JSON) | ✓ | ✓ | GCD, XGrammar, Outlines |
| 词汇 (valid type names) | ✓ | ✓ | GENRE, iNERD, AdaKGC |
| **语义 (domain/range 类型兼容性)** | **✗** | **✗** | **空白 ← OntoCoDec** |
| 语义 (类型检查) | 仅代码生成 | ✓ | MGD, Synchromesh, PLDI'25 |
| 语义 (ontology 合规) | KG 构建 | 仅后处理 | RELATE, ODKE+, OntoLogX |

### 最近似工作 (must differentiate)
1. **PLDI'25 Type-Constrained Code Gen** — 同机制（type system → automaton → logits mask）但用于编程语言
2. **MGD (NeurIPS'23)** — 代码生成的解码时类型检查
3. **ODKE+ (Apple'25)** — 产品级 ontology-guided IE，但用后处理而非解码约束

### 需注意的风险
- **CRANE (ICML'25)**: 严格约束可能降低推理质量
- **Grammar-Aligned Decoding (NeurIPS'24)**: naive masking 会扭曲 token 分布

### 产出文件
- `artifacts/literature_map.yaml` — 结构化文献地图 + novelty 评估 + 引用建议（16 篇 must-cite）
- `artifacts/literature_survey_constrained_decoding_ie.md` — 维度 1 详细报告
- `artifacts/literature_survey_ontology_constrained_ie.md` — 维度 2+3 详细报告
- `memory.md` — 已更新关键结论

---
