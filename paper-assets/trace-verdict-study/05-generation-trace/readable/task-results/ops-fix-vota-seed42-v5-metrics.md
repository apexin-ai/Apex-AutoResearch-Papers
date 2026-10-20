# ops fix vota seed42 v5 metrics

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fix_vota_seed42_v5_metrics_20260521T062912_result.json`
- **Structured JSON:** [`bdd361cc974a8ca150cd.json`](../../sessions/bd/bdd361cc974a8ca150cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已存在（只是之前查询没检索到），metrics 已更新。

**旧值 → 新值对比：**

| 指标 | 旧值 | 新值 |
|---|---|---|
| pass_recall | 0.9882 (TP=841) | **0.9918** (TP=844) |
| fail_precision | 0.9714 | **0.9798** |
| pass_precision | — | **1.0000** |
| fail_recall | — | **1.0000** |
| pass_f1 | — | **0.9959** |
| fail_f1 | — | **0.9898** |
| accuracy | 0.9941 | 0.9941 (不变) |

**Confusion matrix：** TP=844, FP=0, TN=339, FN=7, N=1190。FP=0 说明模型判 pass 时从不误判，所有 7 个错误都是把 pass 误判为 fail。

---
