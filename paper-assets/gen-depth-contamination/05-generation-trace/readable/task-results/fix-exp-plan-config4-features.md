# fix exp plan config4 features

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp_plan_config4_features_20260513T232722_result.json`
- **Structured JSON:** [`f552c7cf549ded1c4781.json`](../../sessions/f5/f552c7cf549ded1c4781.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修正完成。

**改动**：`registry.yaml` 第 260-263 行，`config4_t12.top3_features_1v2` 从 `[freq_entropy, hapax_ratio, surp_skew]` 改为 `[hapax_ratio, ttr, surp_skew]`。

注意：任务描述说修改 `experiment_plan.yaml`，但该文件中不含 `config4_t12` 或 `top3_features` 字段。实际数据在 `registry.yaml` 中，已完成修正。其余引用该组合的文件均为日志，无需修改。

---
