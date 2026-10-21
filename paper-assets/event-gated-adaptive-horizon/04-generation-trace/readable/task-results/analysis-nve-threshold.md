# analysis nve threshold

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nve_threshold_20260525T195512_result.json`
- **Structured JSON:** [`03c710b61662c45b1530.json`](../../sessions/03/03c710b61662c45b1530.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**N=61** (25 CIVO, 36 Healthy)，**AUROC = 0.989**

| Threshold | Accuracy | Precision | Recall | F1 |
|-----------|----------|-----------|--------|------|
| 1.3× | 86.9% | 75.8% | 100% | 0.862 |
| **1.5×** | **93.4%** | **86.2%** | **100%** | **0.926** |
| 1.7× | 90.2% | 88.0% | 88.0% | 0.880 |
| 2.0× | 95.1% | 100% | 88.0% | 0.936 |

**推荐 θ=1.5×**: 100% recall，4个 FP 均可解释（frozen transient spike + eval-variance-driven），Youden's J 最优点也在 ~1.51×。θ=2.0× 适用于需要零误报的场景，但会漏掉 3 个 self-correcting CIVO seed。

---
