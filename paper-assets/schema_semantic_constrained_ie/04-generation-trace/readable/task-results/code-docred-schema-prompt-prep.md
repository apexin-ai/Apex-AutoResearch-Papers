# code docred schema prompt prep

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_docred_schema_prompt_prep_20260513T193903_result.json`
- **Structured JSON:** [`290a6b334dbe66464480.json`](../../sessions/29/290a6b334dbe66464480.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完毕。

## 报告：DocRED schema-informed prompt 就绪状态

### 结论：已就绪，无 bug

**代码实现完整：**
- `--prompt_mode schema_informed` 和 `--constraints_path` 参数已实现
- `build_schema_informed_relation_str()` 按训练频率排序，截取 top-50（`--max_relations 50`），剩余 46 个低频 relation 以一行汇总
- prompt 模板正确包含 type constraint 注释（"Each extracted relation's (head_type, tail_type) must be a valid pair..."）

**数据文件正确：**
- `ontology_constraints_docred.json` 包含全部 96 个 relation types 的 valid_pairs 和 stats
- 平均每个 relation 5.68 个 valid pairs，格式与代码预期一致
- 无 unseen relation types

**Token 长度（Qwen3-8B tokenizer 精确计数）：**

| | Schema-informed | Minimal | Delta |
|---|---|---|---|
| Relation section | 2209 tok | 396 tok | +1813 |
| 完整 prompt（含典型 doc） | ~2500-2700 tok | ~700-850 tok | ~+1800 |

远低于 4000 token 阈值，max_length=8192 的上下文也完全够用。

**无 `--dry_run` 参数**，但不影响功能。DocRED minimal 跑完后可直接启动 schema-informed 实验。

---
