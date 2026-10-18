# analysis olmo topk50 001

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_olmo_topk50_001_20260515T014117_result.json`
- **Structured JSON:** [`1a3559c1e8cfdbcf6a9d.json`](../../sessions/1a/1a3559c1e8cfdbcf6a9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。总结：

**olmo_topk50_001 — SUCCESS**

| 指标 | 值 |
|------|-----|
| 4-class LR acc | 75.7% [74.3%, 77.0%] |
| 4-class RF acc | 74.2% [72.8%, 75.6%] |
| d1v2 AUC (LR/RF) | 0.829 / 0.831 |
| 3-class filtered LR/RF | 67.0% / 67.0% |
| Code contamination | < 1% (narrow) |

**vs 对比基准：**

| Config | 4-class LR | d1v2 AUC |
|--------|-----------|----------|
| OLMo temp09 | 82.0% | 0.901 |
| OLMo nucleus | 78.8% | 0.867 |
| **OLMo topk50** | **75.7%** | **0.829** |
| Pythia topk50 | 69.6% | 0.752 |

OLMo topk50 比 nucleus 低 ~3pp，但仍显著高于 Pythia topk50（+6pp），确认模型效应 > 解码策略效应。3×3 矩阵最后一格完成。

---
