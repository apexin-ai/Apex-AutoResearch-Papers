# code restore classifiers

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_restore-classifiers_20260513T031810_result.json`
- **Structured JSON:** [`2d3e787cd4ec9fc697b3.json`](../../sessions/2d/2d3e787cd4ec9fc697b3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个文件都通过语法验证。

**完成情况**：

1. **`src/classify_errors.py`** — LLM 错误分类器
   - vLLM 批量推理，三分类（action/verification/planning）
   - PCB 检测（通过 `csf_details` 字段）+ override（PCB → verification）
   - `llm_original_type` 字段保留 LLM 原始分类，`error_type` 为最终分类
   - `run_dual_analysis` 函数与 patch 一致：三版本（with_override / without_override / pcb_excluded）× 两粒度（full / dedup）的 Kruskal-Wallis 检验 + P1 gate
   - dry_run 模式用 `_rule_based_error_type` 做 span-based 分类
   - 支持 `--no_span_hint`、`--few_shot` 参数

2. **`src/classify_errors_rulebased.py`** — 规则分类器
   - 10 条规则按优先级：pcb → wrong_object → wrong_instance → wrong_receptacle → wrong_verb → ignored_failure → repeated_action → missing_subtask → inefficient_search → default
   - 输出格式与 classify_errors.py 兼容（可直接用 `compare_classifiers.py` 对比）
   - 包含 `rule_matched` 字段标识触发的规则

---
