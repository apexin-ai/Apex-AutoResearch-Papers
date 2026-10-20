# research docred constrained readiness

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_docred_constrained_readiness_20260514T010448_result.json`
- **Structured JSON:** [`b797b824572db74976ae.json`](../../sessions/b7/b797b824572db74976ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。

## DocRED Constrained Decoding 就绪度报告

### 结论：**Ready to Run (Y)** — 零代码修改

所有组件已完整支持 DocRED：

| 组件 | 状态 | 说明 |
|------|------|------|
| `--dataset docred` | ✅ | `choices=["scierc", "docred"]` (L557) |
| `load_docred_data()` | ✅ | L113，读取 dev.json 格式 |
| DocRED prompt 模板 | ✅ | `build_messages`/`build_s2_entity_messages`/`build_s2_relation_messages` 均有 docred 分支 |
| `load_constraint_spec()` | ✅ | L341-374，自动检测 DocRED dict 格式，P-code→关系名转换 |
| 约束文件 | ✅ | `ontology_constraints_docred.json`：6 entity types, 96 relations, avg 5.68 valid pairs/relation |
| XGrammar schema | ✅ | `build_full_schema()` 数据集无关，enum 使用 `spec.relation_types`（已转为关系名） |
| TypeConstraintProcessor | ✅ | DocRED first-token IDs 已验证唯一（PER=9654, ORG=44927, LOC=12052, TIME=18129, NUM=17488, MISC=44） |
| violation_checker_docred.py | ✅ | `normalize_relation()` 支持关系名→P-code 映射，输出格式兼容 |

### 建议实验命令

```bash
cd /root/schema_semantic_constrained_ie

# grammar_only
python run_constrained_extraction.py \
  --mode grammar_only --dataset docred \
  --data_path data/docred/dev.json \
  --constraints_path data/docred/ontology_constraints_docred.json \
  --output_path outputs/docred_grammar_only.jsonl \
  --max_new_tokens 4096 --resume

# full_s1
python run_constrained_extraction.py \
  --mode full_s1 --dataset docred \
  --data_path data/docred/dev.json \
  --constraints_path data/docred/ontology_constraints_docred.json \
  --output_path outputs/docred_full_s1.jsonl \
  --max_new_tokens 4096 --resume
```

**注意**：DocRED 是文档级（比 SciERC 句子级长得多），建议 `--max_new_tokens 4096`。998 个文档 × 文档级推理，预计耗时显著长于 SciERC。

### 预估工作量：**0 分钟**

---
