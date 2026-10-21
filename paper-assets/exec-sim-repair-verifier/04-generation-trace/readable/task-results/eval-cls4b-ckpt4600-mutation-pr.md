# eval cls4b ckpt4600 mutation pr

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cls4b-ckpt4600-mutation-pr_20260516T022739_result.json`
- **Structured JSON:** [`528189401687b1ff1d5d.json`](../../sessions/52/528189401687b1ff1d5d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CLS 4B ckpt-4600 Test Per-Mutation Breakdown

| mutation_type | N | accuracy | prec_pass | rec_pass | f1_pass | prec_fail | rec_fail | f1_fail |
|---|---|---|---|---|---|---|---|---|
| **gold** | 4633 | **98.25%** | 100.00 | 98.25 | 99.12 | - | - | - |
| **operator_swap** | 3357 | **78.91%** | 71.61 | 96.40 | 82.18 | 94.34 | 61.12 | 74.18 |
| **return_value** | 562 | **67.97%** | 59.59 | 83.33 | 69.49 | 81.19 | 56.01 | 66.29 |
| **off_by_one** | 183 | **58.47%** | 66.46 | 82.95 | 73.79 | 0.00 | 0.00 | 0.00 |
| **boundary_removal** | 1049 | **46.90%** | 43.44 | 90.85 | 58.77 | 70.37 | 15.52 | 25.44 |

关键发现：
- **boundary_removal 4B = 46.9%**，与 8B s42 的 46.9% 完全一致（8B seed123 = 44.9%）
- off_by_one 上 4B (58.47%) 模型完全不会预测 fail（recall_fail=0），全部预测 pass
- 所有 mutation 类型都呈现 pass 偏好（recall_pass >> recall_fail），boundary_removal 最严重

JSON 已保存到 home 服务器 `results/cls4b_ckpt4600_test_mutation_breakdown.json`，artifact 已注册。

---
