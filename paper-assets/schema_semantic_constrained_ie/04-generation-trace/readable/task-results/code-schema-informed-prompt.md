# code schema informed prompt

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_schema_informed_prompt_20260513T180437_result.json`
- **Structured JSON:** [`d1c1bf7ef87d9445d28e.json`](../../sessions/d1/d1c1bf7ef87d9445d28e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both dry-runs completed successfully. Here's a summary:

## 产出

### 1. 修改后的脚本
- **`run_extraction.py`** (SciERC): 新增 `--prompt_mode minimal|schema_informed` 和 `--constraints_path` 参数。`build_schema_informed_system_prompt()` 函数读取 `ontology_constraints.json`，为每个 relation 列出 top-5 最高频 (head→tail) type pairs。
- **`run_extraction_docred.py`** (DocRED): 同样新增 `--prompt_mode` 和 `--max_relations` 参数。`build_schema_informed_relation_str()` 按训练频率排序 relation，列出所有 valid (head→tail) pairs，默认 top-50 relations。

### 2. Prompt 预览

**SciERC schema-informed** (480 tokens, +353 vs minimal):
```
- Used-for: valid (head→tail) pairs: (Method→Task), (Generic→Task), (Method→OtherScientificTerm), (Method→Method), (Method→Generic), and 30 more
- Feature-of: valid (head→tail) pairs: (OtherScientificTerm→OtherScientificTerm), (OtherScientificTerm→Method), ...
- Evaluate-for: valid (head→tail) pairs: (Metric→Generic), (Metric→Method), (Task→Generic), ...
```

**DocRED schema-informed** (2354 tokens, top-50):
```
- country: valid pairs: (LOC→LOC), (LOC→MISC), (LOC→ORG), ..., (TIME→LOC)
- sister city: valid pairs: (LOC→LOC)
- sibling: valid pairs: (PER→PER)
```

### 3. Token 统计
| | Minimal | Schema-informed | 需要截断? |
|---|---|---|---|
| SciERC | 127 tok | 480 tok | NO |
| DocRED (top-50) | 514 tok | 2354 tok | NO |
| DocRED (all 96) | 514 tok | 3816 tok | NO |

即使 all-96 + 最长文档也只有 ~4.3k tokens，远低于 32k 限制。

### 4. Dry-run 结果
- **SciERC**: 1/1 parsed OK. 模型输出了有效的 entities + relations JSON。
- **DocRED**: 1/1 parsed OK. 2554 input tokens, 35.3s generation time.

### 关键发现
SciERC 的 type 约束非常松散（Used-for 有 35/36 种 pair 都合法），所以改用 top-K 频率 pair 展示分布特征，而非简单列出所有 valid types（那样每种 relation 的约束都一样）。DocRED 约束紧凑（平均 5.7 pairs/relation），直接列出所有 valid pairs。

---
