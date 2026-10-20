# analysis mcnemar exp079 supplement

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mcnemar-exp079-supplement_20260520T001728_result.json`
- **Structured JSON:** [`87115607c599c3cd9aab.json`](../../sessions/87/87115607c599c3cd9aab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6/6 方法矩阵完成。

```
exp-079  ICG × LogiQA-200       (n=200, Δ=-0.5pp):
  a=91  b=4  c=3  d=102
  χ²=0.1429, p=0.7055  [不显著]
  χ²_cc=0.0000, p_cc=1.0000  [不显著]
```

b=4 vs c=3，差异极小，McNemar 完全不显著（p=0.71）。与 exp-074 (ICG/FOLIO, p=0.21) 一致：ICG 在两个数据集上均未显著改变 SC 的正确/错误模式。已追加到 `mcnemar_method_experiments.json`，summary 同步更新。

---
