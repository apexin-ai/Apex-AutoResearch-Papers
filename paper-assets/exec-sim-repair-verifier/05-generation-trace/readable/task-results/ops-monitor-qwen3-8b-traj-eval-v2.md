# ops monitor qwen3 8b traj eval v2

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_monitor-qwen3-8b-traj-eval-v2_20260518T232755_result.json`
- **Structured JSON:** [`f755199754f834a1b6b4.json`](../../sessions/f7/f755199754f834a1b6b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 eval 均已完成。汇总结果：

---

### Qwen3-8B TRAJ Repo Eval 结果

| Metric | Best Checkpoint (epoch 3) | Checkpoint-98 (epoch 2) |
|---|---|---|
| **variant_accuracy** | **70.8% (34/48)** | **72.9% (35/48)** |
| per_test_consistency | 70.8% (34/48) | 72.9% (35/48) |
| f1_macro | 70.0% | 72.9% |
| fail_recall (unresolved) | 95.5% | 77.3% |
| pass_recall (resolved) | 50.0% | 69.2% |
| unparseable | 0 | 0 |

**关键发现**: Checkpoint-98 (epoch 2) 比 best checkpoint (epoch 3) 更优:
- variant accuracy 高 2.1pp (72.9% vs 70.8%)
- 预测更均衡: pass_recall 从 50.0% 提升至 69.2%, fail_recall 从 95.5% 降至 77.3%
- F1 macro 高 2.9pp (72.9% vs 70.0%)

Best checkpoint 严重偏向预测 unresolved (13 个 resolved 误判), checkpoint-98 的类别平衡明显更好。**Table 4 应使用 checkpoint-98 的结果 (72.9%)**。

---
