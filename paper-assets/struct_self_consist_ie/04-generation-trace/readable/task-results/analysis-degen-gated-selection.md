# analysis degen gated selection

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_degen_gated_selection_20260518T162321_result.json`
- **Structured JSON:** [`debc8e4edf882871c0c8.json`](../../sessions/de/debc8e4edf882871c0c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results:

| Dataset | Degen% | Greedy | LP-all | Gated | G-Greedy | G-LP |
|---------|-------:|-------:|-------:|------:|---------:|-----:|
| SciERC | 18.7% | 0.6436 | 0.6495 | **0.6507** | +0.0071 | +0.0012 |
| CoNLL | 62.0% | **0.9087** | 0.8985 | 0.8985 | -0.0102 | +0.0000 |
| FewNERD | 23.1% | 0.7713 | 0.7800 | **0.7805** | +0.0092 | +0.0004 |

**Gated vs LP-all 改善极小** (+0.00 ~ +0.12pp)。原因：degenerate instances 上所有 sample F1 相同，LP 选谁都一样，gating 没有可修复的 noise。Gated vs Greedy 在 SciERC/FewNERD 上正向（+0.71/+0.92pp），但 CoNLL 上反向（-1.02pp），因为 CoNLL non-degenerate instances 上 LP 本身比 Greedy 差（0.8255 vs 0.8524）。

脚本在 `code/analysis_degen_gated_selection.py`，报告在 `artifacts/degen_gated/degen_gated_selection_results.md`。

---
