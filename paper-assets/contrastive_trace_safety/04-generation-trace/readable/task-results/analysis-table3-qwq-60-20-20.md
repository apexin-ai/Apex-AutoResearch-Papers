# analysis table3 qwq 60 20 20

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_table3_qwq_60_20_20_20260518T172831_result.json`
- **Structured JSON:** [`1c0527db7189ecea508a.json`](../../sessions/1c/1c0527db7189ecea508a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果如下：

```
QwQ-32B (W=5, L60, 60/20/20, PCA=100d, 10k bootstrap):
  n_test = 1029
  HS Prec: 0.566 [0.121, 0.384]
  Text Prec: 0.330
  ΔPrec: +0.236pp, p=0.0019
  
  HS BA: 0.705 [0.091, 0.218]
  Text BA: 0.543
  ΔBA: +0.162pp, p=0.0000
  
  HS FPR: 0.178 [-0.243, -0.102]
  Text FPR: 0.347
  ΔFPR: -0.169pp, p=0.0000
  
  HS AUROC: 0.833 [0.166, 0.391]
  Text AUROC: 0.554
  ΔAUROC: +0.279pp, p=0.0000
  
  HB (3 tests: Prec, BA, FPR): 3/3 pass
```

配置验证：95 traces → 57/19/19 split, train+val=76 用于训练, test=19 traces (1029 steps)。PCA explained variance 51.3%。全部在 60/20/20 下完成，所有差异高度显著。

结果已写入服务器 `artifacts/table3_qwq_60_20_20/results.json` 并注册。

---
