# compute exp 059 step matched nve

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_compute_exp_059_step_matched_nve_20260524T065728_result.json`
- **Structured JSON:** [`87e864c9d13a489bbcb3.json`](../../sessions/87/87e864c9d13a489bbcb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Let me compile the results.

**Baseline ve_ratio @step 85K (4 seeds):**

| Seed | Step | value_mean | eval_return | ve_ratio |
|------|------|-----------|-------------|----------|
| s1 (baseline_s1) | 85000 | 500.218 | 713.932 | 0.7007 |
| s2 (exp_001_baseline_s2) | 85000 | 264.905 | 389.307 | 0.6804 |
| s3 (exp_001_baseline_s3) | 82000/92000 interp | — | — | 0.6113 |
| s4 (exp_001_baseline_s4) | 85000 | 468.168 | 882.527 | 0.5305 |

s3 interpolated: 0.6063 + 3/10 × (0.6230 − 0.6063) = 0.6113

**Mean baseline ve_ratio @85K** = (0.7007 + 0.6804 + 0.6113 + 0.5305) / 4 = **0.6307**

---

```
exp_001 baseline ve_ratio @85K: 0.6307 (mean of 4 seeds)
exp_059 ve_ratio @85K:          3.3075
step-matched NVE @85K:          5.2444 (= 3.3075 / 0.6307)
```

---
