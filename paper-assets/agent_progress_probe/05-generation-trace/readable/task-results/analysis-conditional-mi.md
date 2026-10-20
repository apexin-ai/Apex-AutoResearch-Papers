# analysis conditional mi

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_conditional-mi_20260515T025351_result.json`
- **Structured JSON:** [`fa25d615abbb6ebbb5df.json`](../../sessions/fa/fa25d615abbb6ebbb5df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

**CMI(X, silver_label | LF) = 0 对所有 30 个特征**——因为 silver label 是 LF 多数投票的确定性函数（13/13 strata 内 label 方差为零）。这是标签构造的数学必然，不是 circularity 的证据。

重新设计为 **feature–LF 独立性分析**，结论为 **STRONG defense**：

| 指标 | Non-overlap (19) | Overlap (11) |
|------|-----------------|-------------|
| Mean max\|r\| with any LF | **0.276** | 0.552 |
| Mean MI(X, matched LF) | 0.133 | 0.437 |
| Standalone F1 (LR, 5-fold) | **0.923** | 0.988 |
| Incremental z > 1.96 | **19/19** | — |

关键证据：
- Non-overlap 特征与 LF 相关性仅为 overlap 特征的一半（2.0x less）
- Non-overlap 特征单独就能达到 F1=0.923（LR），RF/GB 下可达 0.93–0.95
- 全部 19 个 non-overlap 特征在 LF+feature 回归中系数显著（z > 1.96）

产出文件：
- JSON: `artifacts/conditional-mi-analysis/conditional_mi_results.json`
- Report: `artifacts/conditional-mi-analysis/report.md`
- Registry: `conditional-mi-analysis` (DONE)

---
