# ops traj repo 8k s999 eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_traj-repo-8k-s999-eval_20260516T165003_result.json`
- **Structured JSON:** [`ba8e128f2a9fedcaa42e.json`](../../sessions/ba/ba8e128f2a9fedcaa42e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。Registry 已更新到 DONE。

**Eval 结果汇总：**

| Metric | Value |
|--------|-------|
| test_accuracy | 79.17% |
| f1_macro | 78.57% |
| resolved_f1 | 82.14% |
| unresolved_f1 | 75.0% |
| unparseable | 0 |
| best_eval_loss | 0.1565 |
| train_loss | 0.2184 |
| per_test_consistency | 79.17% |

对比同系列 s42/s123（accuracy 77.1%, unparseable 16.7%），s999 的 8k seq_length 版本表现更好：accuracy +2pp，unparseable 从 16.7% 降到 0%，resolved_f1 82.1 vs 82.0 持平，unresolved_f1 75.0 vs 68.6 提升明显。

---
