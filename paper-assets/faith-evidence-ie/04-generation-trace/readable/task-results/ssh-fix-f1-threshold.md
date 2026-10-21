# ssh fix f1 threshold

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-f1-threshold_20260515T043430_result.json`
- **Structured JSON:** [`92093687c881de8b1aca.json`](../../sessions/92/92093687c881de8b1aca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有修改验证完成：

**rsft_report.json 包含:**
- `f1_filter_stats`: `{"gens_dropped_by_f1": 0, "docs_dropped_by_f1": 0}`（这批数据 f1 最低 0.19，无需过滤）
- `truncation_analysis`: `{"truncated_count": 8, "non_truncated_count": 42, "truncated_mean_f1": 0.5308, "non_truncated_mean_f1": 0.5985, "f1_gap": 0.0677, "gap_significant": false}`
- `args.f1_threshold`: 0.1

**rsft_train.jsonl 中所有样本 f1 ≥ 0.67**，无 f1=0.0 样本。

**已完成的修改汇总:**
1. `--f1_threshold` 默认值 0.0 → 0.1
2. `filter_records` 分离 f1 过滤步骤，独立追踪 `gens_dropped_by_f1` 和 `docs_dropped_by_f1`，返回 `(selected, filter_stats)` 元组
3. `score_all_records` 传递 `truncated` 字段
4. `main()` 中 scoring 后、filtering 前添加截断-F1 相关性分析
5. `rsft_report.json` 写入 `f1_filter_stats` 和 `truncation_analysis`

---
