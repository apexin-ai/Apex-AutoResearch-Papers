# diagnose test eval field compliance bug

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_test_eval_field_compliance_bug_20260521T150154_result.json`
- **Structured JSON:** [`aa9238e75ab6004211bf.json`](../../sessions/aa/aa9238e75ab6004211bf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 总结

**根因**: `evaluator.py` 的 `compute_format_compliance` 用 `_parse_raw_json_list`（不处理截断 JSON）检查 field compliance，而 `parse_model_output`（用于 F1 计算，处理截断）检查 format compliance。426/500 个 doc 的模型输出因重复生成而被 max_new_tokens 截断，outer JSON array 未闭合。`_parse_raw_json_list` 的 `rfind(']')` 找到了 evidence 子数组的 `]`，提取的子串不是合法 JSON，返回 None → 跳过 field 检查。

**修复**: `evaluator.py:244-246`，`_parse_raw_json_list` 返回 None 时用 `_repair_truncated_json` fallback，并 drop 截断 artifact（最后一个不完整 triple）。

**效果**: field_compliance 14.8% → 99.4%（74 → 497/500）

**关于 F1=0.3353**: 这不是 field_compliance bug 导致的。F1 用 `parse_model_output` 正确解析了截断输出。低 F1 的原因是模型退化重复（14616 predictions dedup 后仅 8377，recall=0.2486），这是模型/生成策略的问题，不是评估代码 bug。

---
