# ops mc result collect

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_mc-result-collect_20260525T062344_result.json`
- **Structured JSON:** [`8bb641f6184d32d543b1.json`](../../sessions/8b/8bb641f6184d32d543b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已获取全部数据。以下是完整的 Monte Carlo Size Calibration 结果：

## 实验配置

| 参数 | 值 |
|------|-----|
| Method | permutation_wild_cluster_bootstrap |
| n_permutations | 1,000 |
| bootstrap_B | 999 |
| nominal_alpha | 0.05 |
| over_reject_threshold | 0.075 |
| weight_distribution | rademacher |
| clustering | max_p_across_K_positions |
| total_time | 33,109 秒 (~9.2 小时) |

## 逐条件 Rejection Rates

### K=3 (n_panels=455, 13 clusters/position)

| Condition | Rejection Rate | Over-reject |
|-----------|---------------|-------------|
| mmlu × prompt_injection | 0.004 | No |
| mmlu × sycophancy | 0.012 | No |
| mmlu × score_manipulation | 0.008 | No |
| mmlu × verbosity_bias | 0.008 | No |
| mmlu × position_bias | 0.009 | No |
| mmlu × authority_bias | 0.008 | No |
| arc_challenge × prompt_injection | 0.006 | No |
| arc_challenge × sycophancy | **0.016** | No |
| arc_challenge × score_manipulation | 0.011 | No |
| arc_challenge × verbosity_bias | **0.016** | No |
| arc_challenge × position_bias | 0.004 | No |
| arc_challenge × authority_bias | 0.010 | No |

### K=5 (n_panels=3003, 11 clusters/position)

| Condition | Rejection Rate | Over-reject |
|-----------|---------------|-------------|
| mmlu × prompt_injection | 0.001 | No |
| mmlu × sycophancy | 0.006 | No |
| mmlu × score_manipulation | 0.001 | No |
| mmlu × verbosity_bias | 0.003 | No |
| mmlu × position_bias | 0.003 | No |
| mmlu × authority_bias | 0.008 | No |
| arc_challenge × prompt_injection | 0.006 | No |
| arc_challenge × sycophancy | 0.004 | No |
| arc_challenge × score_manipulation | 0.006 | No |
| arc_challenge × verbosity_bias | 0.003 | No |
| arc_challenge × position_bias | 0.000 | No |
| arc_challenge × authority_bias | 0.002 | No |

### K=7 (n_panels=6435, 9 clusters/position)

| Condition | Rejection Rate | Over-reject |
|-----------|---------------|-------------|
| mmlu × prompt_injection | 0.001 | No |
| mmlu × sycophancy | 0.003 | No |
| mmlu × score_manipulation | 0.000 | No |
| mmlu × verbosity_bias | 0.002 | No |
| mmlu × position_bias | 0.001 | No |
| mmlu × authority_bias | 0.002 | No |
| arc_challenge × prompt_injection | 0.000 | No |
| arc_challenge × sycophancy | 0.001 | No |
| arc_challenge × score_manipulation | 0.000 | No |
| arc_challenge × verbosity_bias | 0.002 | No |
| arc_challenge × position_bias | 0.001 | No |
| arc_challenge × authority_bias | 0.001 | No |

## Summary

| K | Mean Rate | Max Rate | Min Rate | Over-reject Count | Conditions |
|---|-----------|----------|----------|--------------------|------------|
| 3 | 0.0093 | 0.016 | 0.004 | **0 / 12** | 12 |
| 5 | 0.0036 | 0.008 | 0.000 | **0 / 12** | 12 |
| 7 | 0.0012 | 0.003 | 0.000 | **0 / 12** | 12 |

**结论：全部 36 个条件均无过度拒绝（0/36 > 7.5% 阈值）。** 检验在名义水平 α=0.05 下偏保守——K=3 的平均拒绝率仅 0.93%，K=7 降至 0.12%。随着 K 增大，检验更加保守（rejection rate 单调递减），size calibration 通过。

---
