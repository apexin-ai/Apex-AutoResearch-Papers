# code prepare phase2 analysis pipeline

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_phase2_analysis_pipeline_20260513T234038_result.json`
- **Structured JSON:** [`1ea557b6fe19d00bea03.json`](../../sessions/1e/1ea557b6fe19d00bea03.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇报如下：

---

### 1. 工具输入输出格式确认

**violation_checker.py**：
- 输入：`--input_path` (JSONL, 每行含 `doc_id`, `gold_entities`, `gold_relations`, `parsed_output`, `mode`)、`--constraints_path` (ontology_constraints.json)、`--output_path`
- 输出 JSON 结构：`summary` (violation counts/rates) + `per_relation_type` (per-relation breakdown) + `quality` (含 `entity_f1` 和 `relation_f1`，micro P/R/F1)
- **F1 在 violation_checker.py 内部计算**（`compute_f1` + `aggregate_f1`），没有独立评估脚本

**文件命名模式**（Phase 2）：
- JSONL：`outputs/phase2_scierc_{mode}.jsonl`
- Violation report：`outputs/violation_report_phase2_{mode}.json`

### 2. 当前实验状态

| Mode | JSONL | Violation Report |
|------|-------|-----------------|
| unconstrained | ✅ 551 samples | ✅ |
| grammar_only | ✅ 551 samples | ✅ |
| semantic_only | ❌ 未开始 | ❌ |
| full_s1 | ❌ 未开始 | ❌ |

### 3. 分析脚本

路径：`/root/schema_semantic_constrained_ie/scripts/compare_phase2.py`

用法：
```bash
# 基本用法（读 outputs/ 下的 4 个 violation report）
python scripts/compare_phase2.py

# 导出 JSON
python scripts/compare_phase2.py --export_json outputs/phase2_comparison.json

# 只比较已完成的
python scripts/compare_phase2.py --modes unconstrained grammar_only
```

输出包含：汇总表（F1 + 4 类 violation rate + delta）、counts 表、per-relation breakdown。缺失实验用 N/A 填充。

### 4. 格式兼容问题

无兼容问题。`run_constrained_extraction.py` 的输出字段（`parsed_output`, `gold_entities`, `gold_relations`）与 `violation_checker.py` 的预期完全一致。4 种 mode 共用同一套 JSONL schema，checker 对所有 mode 通用。

---
