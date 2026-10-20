# paper reference audit relwork

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_reference_audit_relwork_20260514T054544_result.json`
- **Structured JSON:** [`e0f7ac0af203673a5068.json`](../../sessions/e0/e0f7ac0af203673a5068.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**审计结果：4/4 引用全部真实存在，无幻觉。**

| Bib Key | 状态 | 备注 |
|---------|------|------|
| `zhou2026snowballing` | ✅ | 2026 年 arXiv preprint，确实关于 constrained decoding 的 "structure snowballing" 失败模式 |
| `upadhyay2023openie` | ✅ | Findings of EACL 2023，entity-focused constraints for OpenIE |
| `regino2025kgcurator` | ✅ | GenAIK 2025 Workshop (COLING)，LLM 验证 KG triple 插入 |
| `qi2024adelie` | ✅ | EMNLP 2024 main，IE 对齐训练框架 |

唯一需要注意的小问题：
- `zhou2026snowballing` 的 bib 条目应标注为 `@article` + `journal = {arXiv preprint arXiv:2604.06066}`，不要写错 venue
- `regino2025kgcurator` 的 booktitle 应为完整的 workshop 名称 `Proceedings of the Workshop on Generative AI and Knowledge Graphs (GenAIK)`

报告已写入 `artifacts/reference_audit_relwork.md` 并注册。

---
