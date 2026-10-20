# code theta fixed n3 recompute

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_theta-fixed-n3-recompute_20260520T205807_result.json`
- **Structured JSON:** [`8f18b231cbbcadc88865.json`](../../sessions/8f/8f18b231cbbcadc88865.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个任务均完成。

---

### 任务 1：θ-fixed 重算结果（θ\_fixed = -0.0966）

| Condition | lz\*\_free | lz\*\_fixed | θ\_mle | d\_free | d\_fixed | absorbed |
|-----------|-----------|------------|--------|---------|----------|----------|
| clean\_s1 | 8.0101 | 7.9501 | -0.0987 | 0.55 | 0.67 | -0.0600 |
| clean\_s2 | 5.9440 | 6.2996 | -0.0842 | -1.15 | -1.15 | 0.3555 |
| clean\_s3 | 8.0806 | 7.7808 | -0.1068 | 0.61 | 0.48 | -0.2998 |
| contam\_15 | 3.0046 | **10.0224** | 0.1971 | -3.58 | **2.95** | **7.0178** |
| contam\_50 | 5.4480 | **15.7080** | 0.3703 | -1.56 | **9.21** | **10.2600** |

**Baseline (n=3, ddof=1):**
- Free: mean=7.3449, std=1.2137
- Fixed: mean=7.3435, std=0.9080

**Δlz\* (vs baseline mean):**
- contam\_15: Δfree=-4.3403, Δfixed=+2.6790
- contam\_50: Δfree=-1.8969, Δfixed=+8.3646

结果已保存至 `results/theta_fixed_n3.json`。

### 任务 2：compute\_delta.py ddof 修复

第33行 `ddof=0` → `ddof=1`，已确认修复。

---
