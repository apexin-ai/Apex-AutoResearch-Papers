# registry aggregate unification

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_registry_aggregate_unification_20260514T082600_result.json`
- **Structured JSON:** [`0c4e7f2aa7607a603ae8.json`](../../sessions/0c/0c4e7f2aa7607a603ae8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 12 个实验更新成功。汇总：

| exp_id | median_difference |
|--------|-------------------|
| **DeepSeek importance** | |
| bf16_importance_s015 | 0.3925 |
| bf16_importance_s020 | 1.4818 |
| bf16_importance_s025 | 7.1636 |
| bf16_importance_s030 | 14.5861 |
| **Qwen importance** | |
| bf16_qw_imp_s015 | 0.0386 |
| bf16_qw_imp_s020 | 0.2350 |
| bf16_qw_imp_s025 | 1.2677 |
| bf16_qw_imp_s030 | 2.9431 |
| **DeepSeek random** | |
| bf16_ds_rand_s015 | 0.0095 |
| bf16_ds_rand_s020 | -0.0155 |
| bf16_ds_rand_s025 | 0.5445 |
| bf16_ds_rand_s030 | 1.5383 |

4 个 DeepSeek importance 实验的旧 `gradient_paired_aggregate` 已保留为 `gradient_paired_aggregate_legacy`，原字段已移除。

---
