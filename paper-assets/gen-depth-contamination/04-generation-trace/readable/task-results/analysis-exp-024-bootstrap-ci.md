# analysis exp 024 bootstrap ci

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_024_bootstrap_ci_20260516T171648_result.json`
- **Structured JSON:** [`01c82cd0a04a7dd55460.json`](../../sessions/01/01c82cd0a04a7dd55460.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_024 arXiv Domain Bootstrap CI 结果

**方法**: GroupKFold(5) OOF + 10000-iteration doc-level bootstrap CI + 10000 permutation test

| Pair | AUC (OOF) | 95% CI | Perm p | CI lower > 0.60? |
|------|-----------|--------|--------|-------------------|
| **0v1** | 0.9946 | [0.9929, 0.9961] | 0.0001 | PASS |
| **1v2** | 0.8580 | [0.8480, 0.8679] | 0.0001 | PASS |
| **2v3** | **0.6427** | **[0.6275, 0.6575]** | **0.0001** | **PASS** |
| 3v4 | 0.5437 | [0.5276, 0.5598] | 0.0001 | FAIL |
| 4v5 | 0.5294 | [0.5133, 0.5455] | 0.0006 | FAIL |

**K\* (CI-based) = 3**

**2v3 关键判定**: CI lower = 0.6275 > 0.60 阈值，arXiv domain K\*=3 成立。所有 permutation test p < 0.001，AUC 显著高于随机。3v4 CI upper 仅 0.5598，远低于 0.60，信号在 depth 3 后清晰衰减。

Registry 已更新 bootstrap_ci metrics。

---
