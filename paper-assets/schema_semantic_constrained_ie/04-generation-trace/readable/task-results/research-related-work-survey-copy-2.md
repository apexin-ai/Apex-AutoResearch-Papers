# research related work survey

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_related_work_survey_20260514T023514_result.json`
- **Structured JSON:** [`166864891ae06c24ffe4.json`](../../sessions/16/166864891ae06c24ffe4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出文件已写入并注册：
`artifacts/related_work_survey.md`

**覆盖 5 个 paradigm，共 20 篇论文：**

| Paradigm | 论文数 | 代表工作 |
|----------|--------|----------|
| Grammar-constrained decoding | 5 | XGrammar (MLSys'25), Outlines, LMQL (PLDI'23), DOMINO (ICML'24), ASAp (NeurIPS'24) |
| Vocabulary/type-constrained generation | 4 | GENRE (ICLR'21), GenIE (NAACL'22), NeuroLogic (NAACL'21), GCD (EMNLP'23) |
| Structural constraints for IE | 5 | UIE (ACL'22), GoLLIE (ICLR'24), CodeIE (ACL'23), InstructUIE, ADELIE (EMNLP'24) |
| Ontology validation | 4 | ODKE+ (Apple'25), OpenIE w/ entity constraints (EACL'23), EnriCo, KG validation (GenAIK'25) |
| Constrained decoding quality | 4 | Let Me Speak Freely (EMNLP'24), CRANE (ICML'25), Structure Snowballing, Hidden Cost (RANLP'25) |

**OntoCoDec 定位总结（3 个差异化维度）：**
1. **约束层次**：从格式（grammar）扩展到语义（domain/range）
2. **执行时机**：decoding-time preventive enforcement vs post-hoc validation / training-time soft guidance
3. **质量保持**：F1 无损 + S2 两通道策略符合 CRANE 的 alternating approach 理论

注意：CRANE 实际是 ICML 2025 而非 NeurIPS 2024，已在文档中修正。

---
