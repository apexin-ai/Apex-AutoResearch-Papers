# analysis table8 ordinal accuracy v2

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_table8_ordinal_accuracy_v2_20260521T163334_result.json`
- **Structured JSON:** [`9bf3bee2cc1e83a29c39.json`](../../sessions/9b/9bf3bee2cc1e83a29c39.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

计算完成。结果写入 `artifacts/table8_ordinal_accuracy_v2.md`。

核心结论：

**v2 Off-diagonal ordinal accuracy: 80–100%, aggregate 93.3% (28/30)**

- 仅 2 处 mismatch：OLMo→Pythia 和 OLMo→Qwen 的 1v2（OLMo K\*=1 的 classifier 缺乏 depth-2 判别特征，无法识别 Pythia/Qwen K\*=2 的信号）
- 相比 v1（greedy Pythia, 90.0%），v2 提升了 3.3 个百分点——Pythia→Qwen 的 1v2 mismatch 被修复（AUC 0.49→0.63）
- 原文 "80–92%" 应更新为 **"80–100% (aggregate 93.3%)"**

原始 4-model exp-013 目录已不在服务器上，无法直接对比。

---
