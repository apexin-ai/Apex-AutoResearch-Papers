# analysis confusion matrix

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_confusion-matrix_20260515T083703_result.json`
- **Structured JSON:** [`5da226d9e2833b2d91cd.json`](../../sessions/5d/5da226d9e2833b2d91cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有任务已完成，全部产物已就位：

**混淆矩阵结果 (N=27,529)**：

| | Pred gen-0 | Pred gen-1 | Pred gen-2+ |
|---|---|---|---|
| **True gen-0** | 5,937 (99.4%) | 35 (0.6%) | 0 (0.0%) |
| **True gen-1** | 368 (6.2%) | 4,437 (75.0%) | 1,113 (18.8%) |
| **True gen-2+** | 464 (3.0%) | 3,646 (23.3%) | 11,529 (73.7%) |

**Gen-1 错误分析**：误分主要偏向 gen-2+（18.8%），是误分为 gen-0（6.2%）的 3 倍。说明 gen-1 文本已携带可检测的递归失真特征。

**产物**：
- LaTeX：`artifacts/_project/paper/appendix_confusion_matrix.tex` — 已存在，内容正确
- main.tex：`\input{appendix_confusion_matrix}` 已在 finer-depth 之后
- 服务器 JSON：`/root/gen-depth-fingerprint/results/confusion_matrix_3class.json` — 已创建

---
