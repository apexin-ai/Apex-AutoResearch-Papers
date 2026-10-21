# code phase2 dryrun verify

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_phase2_dryrun_verify_20260513T233402_result.json`
- **Structured JSON:** [`7a06a5b5aed47c666006.json`](../../sessions/7a/7a06a5b5aed47c666006.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证完成。

## 验证结果

### 1. 代码支持状态
`run_constrained_extraction.py` 完整支持 `semantic_only` 和 `full_s1`：
- **semantic_only**: 仅加载 `TypeConstraintProcessor`（domain/range 语义约束），不编译 grammar
- **full_s1**: 同时加载 XGrammar LogitsProcessor + TypeConstraintProcessor，单 pass 生成
- 两个模式都走 `run_single_pass()` 函数（非 two-pass 路径）

### 2. Dry-run 结果

| 模式 | 结果 | 实体数 | 关系数 | 耗时 |
|------|------|--------|--------|------|
| semantic_only | **成功** | E=4 | R=1 | 6.7s |
| full_s1 | **成功** | E=4 | R=1 | 7.4s |

两个模式输出了合法的 JSONL，parsed_output 包含正确结构的 entities 和 relations。full_s1 额外多了 grammar 编译步骤（"Grammar compiled (full schema)"），符合预期。

### 3. violation_checker.py
- 位置：`/root/schema_semantic_constrained_ie/violation_checker.py`（14KB，SciERC 专用）
- DocRED 版本：`violation_checker_docred.py`
- 用法：
  ```bash
  python3 violation_checker.py \
    --input_path outputs/&lt;mode>_scierc.jsonl \
    --constraints_path ontology_constraints.json \
    --output_path outputs/violation_report_&lt;mode>.json
  ```
- 检查 4 类违规：entity_type、relation_vocabulary、domain_range、cross_field_consistency

### 注意事项
- 参数名是 `--max_samples`（非 `--num_samples`）
- `torch_dtype` 弃用警告可忽略（不影响运行）

**结论：semantic_only 和 full_s1 代码就绪，可以在 grammar_only/unconstrained 完成后立即提交。**

---
