# analysis conll 2seed construction

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_conll-2seed-construction_20260524T073452_result.json`
- **Structured JSON:** [`c188fb6105d4fe257516.json`](../../sessions/c1/c188fb6105d4fe257516.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

CoNLL 2-seed construction 分析完成。

**核心结论**：Construction 在 CoNLL 上一致为负，与论文 seed-42 结果吻合：

| 方法 | Mean Δ ± σ | Pooled p |
|------|-----------|----------|
| MV   | **-1.10 ± 0.11 pp** | 1.0000 |
| LP   | **-0.59 ± 0.22 pp** | 1.0000 |

60% 实例的 8 个 sample 完全相同（high degeneracy），construction 只能引入噪声，无法改善。报告已写入 `artifacts/rebuttal_construction_conll.md`。

---
