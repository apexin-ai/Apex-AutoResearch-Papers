# analysis metric consistency check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_metric-consistency-check_20260517T112414_result.json`
- **Structured JSON:** [`73f76fb54abcbfeeb92c.json`](../../sessions/73/73f76fb54abcbfeeb92c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `/root/schema-dag-extraction/artifacts/metric_consistency_report.md`。

## 结论

**根本原因**: 70B 脚本的 `evaluate_ner_results` 计算的是 **type-agnostic text recall**（只看文本是否出现在预测中，不检查 type label 是否正确），而 d051 脚本用 `src/evaluate.py` 的 `_text_match` 函数计算 **type+text match recall**（要求 type 和 text 同时匹配）。

对 count_2 的影响尤其大：schema 只有 2 个 type 时，模型能正确提取文本但常分错 type → 70B 报 0.970（不看 type），d051 报 0.527（看 type）。

**修复路径**: 如果 westd-24295 上还有 70B 的 `results_count_*.jsonl`（含 per-entity type 字段），可直接用 `evaluate_all(preds, samples, eval_mode="text_match")` 重算，无需重跑 inference。

---
