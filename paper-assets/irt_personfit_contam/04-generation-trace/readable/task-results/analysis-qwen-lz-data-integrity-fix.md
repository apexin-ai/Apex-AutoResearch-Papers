# analysis qwen lz data integrity fix

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen-lz-data-integrity-fix_20260521T173127_result.json`
- **Structured JSON:** [`049d6730bbffc1cd80fc.json`](../../sessions/04/049d6730bbffc1cd80fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

### Table 1: Per-condition values

| Condition | θ_MLE | lz (Drasgow) | lz* (Snijders) | lz*_fixed | accuracy |
|-----------|-------|-------------|----------------|-----------|----------|
| clean_s1 | -0.0987 | +8.0101 | +9.4676 | +9.5814 | 0.6787 |
| clean_s2 | -0.0842 | +5.9440 | +7.0539 | +7.6262 | 0.6789 |
| clean_s3 | -0.1068 | +8.0806 | +9.5293 | +9.3838 | 0.6783 |
| clean_s4 | -0.1092 | +7.6090 | +8.9673 | +8.7458 | 0.6786 |
| clean_s5 | -0.0875 | +7.1963 | +8.5322 | +8.9982 | 0.6787 |
| clean_s6 | -0.1036 | +6.9848 | +8.2445 | +8.2020 | 0.6771 |
| clean_s7 | -0.0892 | +7.4005 | +8.7702 | +9.1835 | 0.6783 |
| clean_s8 | -0.1035 | +7.7188 | +9.1110 | +9.0705 | 0.6768 |
| clean_s9 | -0.1242 | +7.6799 | +9.0132 | +8.3038 | 0.6743 |
| clean_s10 | -0.1156 | +6.9272 | +8.1492 | +7.7185 | 0.6758 |
| **contam_15** | **+0.1971** | **+3.0046** | **+3.8494** | **+11.9491** | **0.7310** |
| **contam_50** | **+0.3703** | **+5.4480** | **+7.2892** | **+18.6302** | **0.7643** |

θ_fixed = -0.1022 (10 clean seeds 均值)

### Table 2: Cohen's d + 95% Bootstrap CI

| Metric | d(15%) | 95% CI | d(50%) | 95% CI |
|--------|--------|--------|--------|--------|
| lz* free-θ | **-2.99** | [-3.25, -2.73] | **-1.71** | [-2.80, -1.04] |
| lz* θ-fixed | **+2.77** | [+2.60, +3.08] | **+3.24** | [+3.21, +3.29] |

### 关键观察

- **free-θ lz***: contam_15 的 lz* 显著**低于** clean（d=-2.99），因为 MLE θ 被污染题目拉高（+0.197 vs ~-0.10），但 response pattern 在高 θ 下反而不一致
- **θ-fixed lz***: 方向反转，contam 的 lz* 显著**高于** clean（d=+2.77/+3.24），因为固定 θ 在 clean 水平时，污染条件的高正确率产生异常高的 observed log-likelihood
- 所有 12 条件来自**同一份代码的同一次执行**，消除了实现差异

结果 JSON 已保存至 `/root/autodl-tmp/ctrl_contam_pilot/unified_lz_results.json`。

---
