# code plan 002 sft fixes

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan-002-sft-fixes_20260513T225116_result.json`
- **Structured JSON:** [`18ed631f3cb2929a0f5b.json`](../../sessions/18/18ed631f3cb2929a0f5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。总结修改：

**Fix 1 — Episode-level split（数据泄漏）**：
- `_parse_record()` 新增 `episode_id`、`variation` 字段传递
- `stratified_split()` 改为按 `(task_type, episode_id, variation)` 分组 episode，对 episode 而非 step 做 stratified split
- dry-run 日志显示 "2 episodes in train, 1 episodes in val"，确认 episode 级分割生效

**Fix 2 — Best model 指标**：
- `compute_metrics()` 新增 `f1_macro` 和 `balanced_accuracy`
- `metric_for_best_model` 从 `"accuracy"` 改为 `"f1_macro"`

**Fix 3 — 清理过时代码**：
- 已删除 `src/postprocess_to_sft.py`

当前数据只有 3 个 episode 全是 deterministic（no-preference 被 skip），plan-001b 数据收集完会有更多 internal-preferred samples。

---
