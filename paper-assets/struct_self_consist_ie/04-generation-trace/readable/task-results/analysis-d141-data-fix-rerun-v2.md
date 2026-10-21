# analysis d141 data fix rerun v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d141_data_fix_rerun_v2_20260518T144046_result.json`
- **Structured JSON:** [`1185ab9bce240d8ddf37.json`](../../sessions/11/1185ab9bce240d8ddf37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。报告已写入 `artifacts/d141_data_fix_rerun_v2_report.md`。

### 执行摘要

**修改内容：**
- `code/evaluation.py` 和 `analysis_d141_scatter_plot.py` 的 entity matching 从 `(text, type)` 改回 `(start, end, type)`
- `analysis_d141_conditional_decomp.py` 已经正确，无需修改
- 数据路径、gold filter、N=8 均已正确就位

**关键结果：**

| | SciERC | CoNLL | FewNERD |
|---|---|---|---|
| **Favorable Δ** | **+2.52 pp** | **-1.88 pp** | **+0.69 pp** |
| **Best merge F1** | 0.6596 (k=3) | 0.9032 (k=3) | 0.7435 (k=2) |
| **Gap recovery** | +11.9% | -9.0% | -3.6% |

**CoNLL Favorable bucket 确认为负值** (-1.88 pp, CI [-2.93, -0.85])，span-based matching 下 LP selection 在 CoNLL 上即使在 favorable 条件下也无法改善 greedy。Entity merge 在所有数据集上均未突破 oracle ceiling，仅 SciERC 回收了 11.9% 的 gap。

---
