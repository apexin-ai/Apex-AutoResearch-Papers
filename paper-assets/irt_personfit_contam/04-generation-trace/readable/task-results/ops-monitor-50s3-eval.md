# ops monitor 50s3 eval

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_monitor-50s3-eval_20260522T193052_result.json`
- **Structured JSON:** [`52e98c182947a5f23058.json`](../../sessions/52/52e98c182947a5f23058.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已获取。汇总报告如下：

---

## contam_50_s3 评估结果

**Accuracy**
| | Overall | Seen (7021) | Unseen (7021) |
|---|---|---|---|
| acc | 0.7666 | 0.8029 | 0.7302 |

**Free-θ (MLE)**
- θ_mle = 0.4261
- lz\* = 2.8695
- |d| = **7.91**, 95% CI = [5.52, 18.29]
  - baseline: mean=8.6838, std=0.7353, n=10

**Fixed-θ (θ = −0.1022)**
- lz_fixed = 13.0362
- lz\*_fixed = 15.3929
- d_fixed = **9.80**, 95% CI = [8.18, 16.46]
  - baseline: mean=7.3522, std=0.5802, n=10

**对比其他 50% seeds**

| Seed | d (free-θ) | d_fixed |
|------|-----------|---------|
| s1 (50%) | — | 14.52 |
| s2 (50%) | — | 12.64 |
| **s3 (50%)** | **7.91** | **9.80** |

contam_50_s3 的 fixed-θ d=9.80 低于 s1/s2（14.52/12.64），但仍然是极显著的异常信号。

---
