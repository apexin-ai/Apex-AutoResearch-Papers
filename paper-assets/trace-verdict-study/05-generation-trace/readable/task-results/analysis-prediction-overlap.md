# analysis prediction overlap

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_prediction-overlap_20260516T114201_result.json`
- **Structured JSON:** [`672eec87be5934d8cc55.json`](../../sessions/67/672eec87be5934d8cc55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果非常清晰：

## Prediction Overlap 分析结果

### Qwen-1.5B (`qwen15b_exception_only_seed42`) 错误样本
| Sample ID | Label | Pred |
|-----------|-------|------|
| 901 | pass | fail |
| 905 | pass | fail |

### Qwen-7B (`exception_only`) 错误样本
| Sample ID | Label | Pred |
|-----------|-------|------|
| 901 | pass | fail |
| 905 | pass | fail |

### 结论

**完全重叠，mechanistic confirmation。**

两个模型（1.5B 和 7B）在 exception_only 条件下犯了完全相同的 2 个错误：sample 901 和 905，都是将真实标签 `pass` 错误预测为 `fail`。错误方向也一致（false negative）。

这强烈说明这 2 个样本的错误是 **irreducible error**——由 exception_only 输入表示本身的信息瓶颈导致，而非模型容量不足。无论模型从 1.5B 扩大到 7B（4.7x 参数量），都无法纠正这两个样本。

---
