# code mbr span fix

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mbr_span_fix_20260518T164439_result.json`
- **Structured JSON:** [`c7a132e5d93ef780255d.json`](../../sessions/c7/c7a132e5d93ef780255d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**MBR confirmed dead.** 两个 confound 都排除了：

| Dataset | Greedy | MBR-text | MBR-span | Oracle | MBR_span-Greedy |
|---------|--------|----------|----------|--------|-----------------|
| SciERC  | 0.6439 | 0.6444   | 0.6451   | 0.7758 | **+0.11pp**     |
| CoNLL   | 0.9070 | 0.9023   | 0.9028   | 0.9494 | **-0.42pp**     |
| FewNERD | 0.7478 | 0.7208   | 0.7214   | 0.8686 | **-2.63pp**     |

关键发现：
- **Text/Span 选择一致率 98.9-99.7%**，度量不对齐几乎不影响选择结果，span-based 只比 text-based 好 +0.05~0.07pp
- **gold_filter 统一后** CoNLL 从 -0.4pp 变为 -0.42pp，无本质变化
- MBR 在 2/3 数据集上劣于 greedy，FewNERD 上严重负面（-2.63pp）

结果已写入 `artifacts/mbr_fix/mbr_span_fix_results.md` 和远程 `output/mbr_selection_results.json`。

---
