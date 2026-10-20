# fix p0 val metrics truncation recompute

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_p0-val-metrics-truncation-recompute_20260514T085057_result.json`
- **Structured JSON:** [`175503416c79ff0308a3.json`](../../sessions/17/175503416c79ff0308a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果出来了，情况比预期更严重。

## 结果摘要

**截断样本分析**：1883 个截断样本中，全部被预测为 pass（majority class）。其中 697 个实际是 fail，被错误标为 pass。

**排除截断后的 val metrics 与原始对比**：

| Checkpoint | Val Acc(filt) | F1_macro(filt) | F1_fail(filt) | Orig Acc | Test Acc |
|---|---|---|---|---|---|
| ckpt-1000 | **87.18%** | 75.90 | 59.41 | 82.30% | 73.14% |
| ckpt-800 | 86.57% | **77.08** | **62.33** | 81.81% | 74.27% |
| ckpt-400 | 85.20% | 74.48 | 57.95 | 80.72% | 75.05% |
| ckpt-600 | 80.26% | 72.66 | 58.25 | 76.78% | **80.73%** |

**排序一致性**：

- **Spearman(val_filtered acc → test acc) = -1.00** — 完全负相关
- **Spearman(val_filtered f1_macro → test f1_macro) = -0.80**
- 排除截断 **没有改善排序一致性**，filtered 和 original 的排序完全一样

**根因**：问题不仅是截断。截断样本在所有 checkpoint 中数量相同（同一批样本被截断），排除后只是等比例去掉了同一批预测为 pass 的样本，不改变 checkpoint 间的相对排序。真正的问题是 **val 和 test 的分布差异** + **max_seq_length=2048 训练本身导致模型在长样本上行为异常**。

**结论**：排除截断不够，需要 **max_seq_length=4096 重跑 val sweep**。

---
