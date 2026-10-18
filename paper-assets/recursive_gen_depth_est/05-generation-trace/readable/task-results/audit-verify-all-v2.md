# audit verify all v2

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_verify-all-v2_20260525T202018_result.json`
- **Structured JSON:** [`02349b9825a09b5497cf.json`](../../sessions/02/02349b9825a09b5497cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。核心发现：

1. **78.70% vs 78.2%**：不是矛盾。78.70% 来自当前 pipeline（5-fold CV, 200 trees），78.2% 来自旧 pipeline（single split, 100 trees）。论文 B.22 的 78.70% 正确，registry 的 0.782 是过时值。

2. **Min-K% 40.4%**：确认来自 `mink_prob_results.json` 的 9-cell average K20_methodB (`d1d3_bal_acc = 0.4039`)。

3. **RF d2 recall**：B.14 的 .596 实际是 **DivEye(XGBoost)** 的值，不是 RF。RF 正确值为 .5867。B.6 的 .592 在服务器上无对应原始数据，来源不明。论文需修正方法标注或数值。

报告已写入 `artifacts/audit_discrepancy_verify.md`。

---
