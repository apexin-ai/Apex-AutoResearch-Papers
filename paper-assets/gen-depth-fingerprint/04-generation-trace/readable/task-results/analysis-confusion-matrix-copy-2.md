# analysis confusion matrix

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_confusion-matrix_20260515T083418_result.json`
- **Structured JSON:** [`3a14b627e39647ac617c.json`](../../sessions/3a/3a14b627e39647ac617c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**3×3 混淆矩阵 (6-gen LOGO, N=27,529)**

| | Pred gen-0 | Pred gen-1 | Pred gen-2+ |
|---|---|---|---|
| **True gen-0** | 5,937 (99.4%) | 35 (0.6%) | 0 (0.0%) |
| **True gen-1** | 368 (6.2%) | 4,437 (75.0%) | 1,113 (18.8%) |
| **True gen-2+** | 464 (3.0%) | 3,646 (23.3%) | 11,529 (73.7%) |

**Gen-1 错误分析：**
- 正确率 75.0%
- 误判为 gen-0：6.2% (368)
- 误判为 gen-2+：18.8% (1,113)
- gen-2+ 方向的错误是 gen-0 方向的 **3倍** (ratio = 0.33)，说明 gen-1 文本已携带可检测的递归失真信号，更容易被归为更深层而非人类文本

**产出文件：**
- 服务器：`/root/gen-depth-fingerprint/results/confusion_matrix_results.json`
- LaTeX：`artifacts/_project/paper/appendix_confusion_matrix.tex`
- `main.tex` 已添加 `\input{appendix_confusion_matrix}` 到 appendix 末尾

---
