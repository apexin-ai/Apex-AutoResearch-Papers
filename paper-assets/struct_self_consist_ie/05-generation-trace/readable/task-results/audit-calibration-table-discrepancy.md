# audit calibration table discrepancy

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_calibration-table-discrepancy_20260519T182822_result.json`
- **Structured JSON:** [`90f963d024a01761a16f.json`](../../sessions/90/90f963d024a01761a16f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

**差异原因**：数据源不同，非同一配置。

| 表 | FewNERD 数据 | Greedy F1 |
|---|---|---|
| tab:fewnerd（主表）| 全测试集 n=32,565, 3-seed mean | .748 |
| tab:calibration（校准表）| exp_027 5K 子样本, single seed | .771 |

SciERC 和 CoNLL 在两个表中一致，因为它们的测试集本身就小（529 / ~2756），两个实验都用了全量。只有 FewNERD（全量 32,565）在校准实验中用了 5K 子样本导致数值偏高。

**已修复**：在 tab:calibration 的 caption 中添加了说明："Few-NERD evaluated on a 5K subsample (greedy .771); full-set greedy is .748 (Table~\ref{tab:fewnerd}). Calibration conclusions are unchanged."

**建议后续**：在服务器上用全量 FewNERD 测试集重跑 `calibration_baseline.py`，彻底消除数值不一致。校准结论（Platt/TempScale 不改变选择，MF-Platt 无显著提升）不会因此改变。

---
