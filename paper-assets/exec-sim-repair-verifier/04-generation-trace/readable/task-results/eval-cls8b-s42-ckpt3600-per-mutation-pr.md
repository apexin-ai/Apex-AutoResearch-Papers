# eval cls8b s42 ckpt3600 per mutation pr

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cls8b-s42-ckpt3600-per-mutation-pr_20260516T023513_result.json`
- **Structured JSON:** [`0151e578d67f0849d442.json`](../../sessions/01/0151e578d67f0849d442.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CLS 8B s42 ckpt-3600 per-mutation P/R 分析完成。核心发现：

| mutation_type | n | acc | prec_fail | rec_fail | f1_fail | predict_pass_rate |
|---|---|---|---|---|---|---|
| **gold** | 4633 | 96.24 | — | — | — | 96.24% |
| **operator_swap** | 3357 | 81.38 | 90.62 | 69.65 | 78.76 | 61.9% |
| **off_by_one** | 183 | 86.89 | 85.71 | 66.67 | 75.00 | 77.05% |
| **return_value** | 562 | 75.44 | 97.85 | 57.59 | 72.51 | 66.9% |
| **boundary_removal** | 1049 | 46.90 | 64.10 | 20.42 | 30.97 | 81.41% |

**与 4B 对比关键差异：**
- **off_by_one**: 8B rec_fail=66.67% vs 4B rec_fail=0% — 8B 显著改善，不再完全漏判
- **boundary_removal**: 8B rec_fail=20.42% vs 4B rec_fail=15.5% — 略有改善但仍严重 PASS bias (81.4% predict pass)
- **operator_swap**: 8B rec_fail=69.65% vs 4B rec_fail=61.1% — 稳步提升
- **return_value**: 8B rec_fail=57.59% vs 4B rec_fail=56.0% — 基本持平

结果已保存到 `artifacts/cls8b_s42_ckpt3600_per_mutation_pr.json`。

---
