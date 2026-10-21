# analysis prediction overlap 1 5b vs 7b

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_prediction_overlap_1_5b_vs_7b_20260516T174644_result.json`
- **Structured JSON:** [`288fa8be4c8dc1e7c1c1.json`](../../sessions/28/288fa8be4c8dc1e7c1c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。报告已写入 `artifacts/prediction_overlap_1.5b_vs_7b.md`。

关键发现：

- **Jaccard = 1.0** — 两个模型在完全相同的 2 个样本上犯错（ID 901, 905），均为 false negative
- 7B 的 3 个 seed 也都一致失败在这两个样本上
- 两个样本都来自 **HumanEval/95**，区别仅是 trace 中迭代器的内存地址不同（近乎重复）
- 根因：`all()` 短路时 Python 正常触发的 `GeneratorExit` 被 trace 格式标记为 `[ERROR]`，误导模型预测 "fail"

结论：99.83% 是由 trace 格式标注伪影造成的不可约上限，与模型容量无关。Ensemble 在此无额外收益。

---
