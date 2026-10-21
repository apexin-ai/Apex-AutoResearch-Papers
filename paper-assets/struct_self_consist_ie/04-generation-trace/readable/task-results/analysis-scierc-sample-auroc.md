# analysis scierc sample auroc

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scierc_sample_auroc_20260516T174126_result.json`
- **Structured JSON:** [`79a60495c9d06c5b450d.json`](../../sessions/79/79a60495c9d06c5b450d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

**SciERC N=8 sample-level AUROC (529 instances, 8 samples each):**

| Signal | AUROC |
|--------|-------|
| LP | 0.5035 |
| SJ | 0.4810 |
| FK | 0.4774 |
| EM | 0.4598 |
| VC | 0.4894 |

所有信号的 sample-level AUROC 都在 0.5 附近（随机水平），说明单独信号无法在 sample 粒度预测 oracle。N=32 结果类似（LP=0.4693）。

已将 `code/analyze_fewnerd_results.py` 中 `SCIERC_REF["lp_auroc"]` 从错误的 0.72 更正为 0.5035。

---
