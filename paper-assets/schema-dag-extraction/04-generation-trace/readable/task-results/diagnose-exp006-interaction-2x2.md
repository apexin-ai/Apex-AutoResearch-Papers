# diagnose exp006 interaction 2x2

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp006_interaction_2x2_20260515T174931_result.json`
- **Structured JSON:** [`7ce4b0c03a2e9652a797.json`](../../sessions/7c/7ce4b0c03a2e9652a797.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。

**根因**：`run_extraction.py:231` 把 `strategies["low_bcs"]` 当单个 dict 索引，但 exp006 的 `build_factorial_batches` 返回的是 list（每个 cell 10 个 batch dict）。附带问题：batch_id 用 `_` 拼接但下游 `compute_interaction_analysis` 按 `/` 分割，即使不崩溃也会丢掉所有分析结果。

**修复内容**（`src/run_extraction.py` lines 227-244）：
- `low_bcs`/`high_bcs` 策略支持 list 和 dict 两种格式（`isinstance` 判断），向后兼容
- batch_id 分隔符从 `_` 改为 `/`，使 `"low_count/low_bcs/0"` 能正确归入 `"low_count/low_bcs"` cell

**验证**：`--dry_run --max_samples 10` 通过，4 个 factorial cell 共 22 batches 正常生成。脚本已可重新提交。

---
