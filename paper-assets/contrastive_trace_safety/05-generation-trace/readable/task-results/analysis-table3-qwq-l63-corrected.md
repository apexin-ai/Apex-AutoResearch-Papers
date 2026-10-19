# analysis table3 qwq l63 corrected

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_table3_qwq_l63_corrected_20260518T182812_result.json`
- **Structured JSON:** [`91cada2d8239a3ce1241.json`](../../sessions/91/91cada2d8239a3ce1241.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

A1 rerun 已有完整 L63 数据，无需重跑。格式化结果：

```
QwQ-32B (W=5, L63, 60/20/20, PCA=100d, 10k bootstrap):
  n_test = 19
  HS Prec: 0.522 [bootstrap mean]
  Text Prec: 0.330 [bootstrap mean]
  ΔPrec: +0.192pp, p=0.0057, CI=[0.093, 0.335]
  
  HS BA: 0.673
  Text BA: 0.543
  ΔBA: +0.130pp, p=0.0000, CI=[0.072, 0.191]
  
  HS FPR: 0.197
  Text FPR: 0.347
  ΔFPR: -0.150pp, p=0.0003, CI=[-0.229, -0.076]
  
  HS AUROC: 0.812
  Text AUROC: 0.554
  ΔAUROC: +0.258pp, p=0.0000, CI=[0.158, 0.368]
  
  HB (3 tests: Prec, BA, FPR): 3/3 pass
```

**来源**：`r14_a1_qwq_rerun/results.json` 参数完全匹配（L63, PCA=100d, max_iter=2000, 60/20/20 seed=42, 95 traces, 10k bootstrap, null-centered two-sided paired）。BA-optimal layer sweep 确认 L63 = 0.893 BA（全层最高）。已复制到 `table3_qwq_l63_corrected/` 并注册 artifact。

---
