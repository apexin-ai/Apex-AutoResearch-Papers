# code arcc collect all seeds

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_arcc-collect-all-seeds_20260521T152331_result.json`
- **Structured JSON:** [`6498e4718d92d4977cd7.json`](../../sessions/64/6498e4718d92d4977cd7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 12 个结果已收集。汇总如下：

## ARC-C Clean Seeds (s1-s10)

| Seed | Accuracy | lz* | theta_mle | n_items |
|------|----------|-----|-----------|---------|
| clean_s1 | 0.9017 | **-5.4483** | 0.8106 | 295 |
| clean_s2 | 0.8949 | **-5.4328** | 0.7624 | 295 |
| clean_s3 | 0.8949 | **-5.5244** | 0.7137 | 295 |
| clean_s4 | 0.8847 | **-5.4345** | 0.5502 | 295 |
| clean_s5 | 0.8983 | **-5.2317** | 0.7810 | 295 |
| clean_s6 | 0.8949 | **-5.5724** | 0.7547 | 295 |
| clean_s7 | 0.8915 | **-5.5852** | 0.7058 | 295 |
| clean_s8 | 0.9051 | **-5.4001** | 0.8511 | 295 |
| clean_s9 | 0.9017 | **-5.5359** | 0.8868 | 295 |
| clean_s10 | 0.9051 | **-5.0733** | 0.8111 | 295 |

**Clean lz\* 均值: -5.4239**, 范围: [-5.5852, -5.0733]

## Contam Conditions

| Condition | Accuracy | lz* (overall) | lz* (seen) | lz* (unseen) | theta_mle | n_seen |
|-----------|----------|---------------|------------|--------------|-----------|--------|
| contam_15 | 0.9085 | **-4.9165** | 0.5677 | -5.4137 | 0.9639 | 44 |
| contam_50 | 0.9424 | **-4.5725** | -0.3310 | -3.9023 | 4.0 | 147 |

Clean 的 10 个 lz\* 值（用于 bootstrap CI）：
```
[-5.4483, -5.4328, -5.5244, -5.4345, -5.2317, -5.5724, -5.5852, -5.4001, -5.5359, -5.0733]
```

---
