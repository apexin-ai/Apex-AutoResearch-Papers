# ops read all clean reeval results

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_read-all-clean-reeval-results_20260523T145439_result.json`
- **Structured JSON:** [`75df23bd64dacb821fb5.json`](../../sessions/75/75df23bd64dacb821fb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 10 个 Clean Seed Re-eval 结果

| Seed | theta_mle | lz* | accuracy |
|------|-----------|-----|----------|
| clean (s1) | -0.6661 | **0.8446** | 0.5914 |
| clean_s2 | -0.6013 | **-1.8765** | 0.5959 |
| clean_s3 | -0.6700 | **0.3452** | 0.5905 |
| clean_s4 | -0.6435 | **0.0206** | 0.5923 |
| clean_s5 | -0.6300 | **1.7323** | 0.5965 |
| clean_s6 | -0.6027 | **2.8466** | 0.6010 |
| clean_s7 | -0.6356 | **-0.4007** | 0.5929 |
| clean_s8 | -0.6979 | **1.1656** | 0.5860 |
| clean_s9 | -0.6588 | **0.1897** | 0.5922 |
| clean_s10 | -0.6214 | **-2.2497** | 0.5951 |

## 新 Clean Baseline

| 统计量 | 值 |
|--------|-----|
| n | 10 |
| mean(lz*) | **+0.2618** |
| SD(lz*, ddof=0) | **1.4626** |
| SD(lz*, ddof=1) | **1.5418** |
| min(lz*) | -2.2497 |
| max(lz*) | +2.8466 |
| mean(theta) | -0.6427 |
| mean(accuracy) | 0.5934 |

## 与旧值对比

| 版本 | mean(lz*) | SD(lz*) |
|------|-----------|---------|
| V0 硬编码 | -0.312 | 0.840 |
| V1 registry (单次) | +0.29 | — |
| **V2 re-eval (10 seeds)** | **+0.262** | **1.542 (ddof=1)** |

关键发现：
- **mean(lz*) ≈ +0.26**，与 V1 单次值 (+0.29) 非常接近，确认 V0 的 -0.312 是错误的
- **SD 很大 (1.54)**，说明 lz* 在 clean 条件下的种子间方差很高（range: -2.25 到 +2.85）
- contam_15（原始，非 re-eval）：lz* = -2.99，在 clean baseline 均值以下约 2.1 个 SD

---
