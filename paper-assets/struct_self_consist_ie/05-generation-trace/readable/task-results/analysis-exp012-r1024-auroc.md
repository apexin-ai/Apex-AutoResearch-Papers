# analysis exp012 r1024 auroc

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp012_r1024_auroc_20260514T224900_result.json`
- **Structured JSON:** [`ff8f47d2413ce12111e9.json`](../../sessions/ff/ff8f47d2413ce12111e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是 exp_012_rerun_1024 的 5-signal AUROC 完整结果（binary threshold: F1≥1.0）：

### NER

| Signal | Full (n=529) | Conditional (n=477) |
|--------|-------------|---------------------|
| **EM** | **0.7493** | **0.7556** |
| SJ | 0.6917 | 0.6772 |
| voting_conf | 0.6841 | 0.6618 |
| FK | 0.6290 | 0.6078 |
| logprob | 0.5783 | 0.5633 |

### RE

| Signal | Full (n=397) | Conditional (n=238) |
|--------|-------------|---------------------|
| **EM** | **0.7059** | **0.7515** |
| voting_conf | 0.6935 | 0.6420 |
| SJ | 0.6702 | 0.6463 |
| FK | 0.6089 | 0.5510 |
| logprob | 0.6005 | 0.5186 |

EM 在所有 split 上 AUROC 最高。结构化信号（SJ、voting_conf、EM）全部优于 logprob baseline。排序稳定：EM > voting_conf ≈ SJ > FK > logprob。

---
