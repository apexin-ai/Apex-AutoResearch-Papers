# analysis k7 bootstrap v2 collect results

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k7-bootstrap-v2-collect-results_20260524T082430_result.json`
- **Structured JSON:** [`ef8b6e3091f9a681cb86.json`](../../sessions/ef/ef8b6e3091f9a681cb86.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

K=7 V2 Aggregation Bootstrap 已完成，结果如下：

---

## K=7 V2 Aggregation Bootstrap 结果

**文件**: `artifacts/results/plan001/k7_aggregation_bootstrap.json`
**大小**: 77,174 bytes
**生成时间**: 2026-05-24 16:30
**运行时间**: 1339s (~22min), 6435 panels, 9999 bootstrap iterations

### Summary

| Method | eta_max sig | K_eff sig | mean R² |
|---|---|---|---|
| majority_vote | 1/12 | **8/12** | 0.244 |
| weighted_vote | 1/12 | **6/12** | 0.207 |
| threshold_supermajority | 8/12 | **10/12** | 0.509 |
| bayesian | 1/12 | **0/12** | 0.105 |

所有 keff 显著方向均为正（sig_positive = sig count, sig_negative = 0）。

### Per-condition K_eff detail (majority_vote)

| Condition | keff_β_std | keff_fdr_p | sig | eta_β_std | eta_fdr_p | sig | R² |
|---|---|---|---|---|---|---|---|
| mmlu×prompt_injection | +0.545 | 0.0161 | * | +0.112 | 0.438 | | 0.375 |
| mmlu×sycophancy | +0.443 | 0.0161 | * | +0.090 | 0.281 | | 0.227 |
| mmlu×score_manipulation | +0.556 | 0.0161 | * | -0.101 | 0.471 | | 0.240 |
| mmlu×verbosity_bias | +0.295 | 0.0312 | * | +0.429 | 0.069 | | 0.368 |
| mmlu×position_bias | +0.252 | 0.0326 | * | +0.605 | 0.016 | * | 0.558 |
| mmlu×authority_bias | +0.459 | 0.0161 | * | -0.142 | 0.357 | | 0.150 |
| arc×prompt_injection | +0.608 | 0.0816 | | -0.135 | 0.325 | | 0.262 |
| arc×sycophancy | +0.046 | 0.7185 | | +0.345 | 0.069 | | 0.145 |
| arc×score_manipulation | +0.845 | 0.0161 | * | -0.413 | 0.177 | | 0.254 |
| arc×verbosity_bias | +0.367 | 0.0459 | * | +0.131 | 0.325 | | 0.227 |
| arc×position_bias | +0.268 | 0.8395 | | -0.100 | 0.964 | | 0.037 |
| arc×authority_bias | +0.127 | 0.4297 | | +0.187 | 0.218 | | 0.086 |

### 跨 K 对比（majority_vote K_eff sig）

| K | K_eff sig (majority) |
|---|---|
| K=3 | 4/12 |
| K=5 | 7/12 |
| **K=7** | **8/12** |

**单调递增趋势确认**: 4→7→8。Threshold supermajority 更强：K=5=7/12 → K=7=**10/12**。

### 关键发现

- **K_eff 效应随 K 单调增强**：majority 从 4/12 (K=3) → 7/12 (K=5) → 8/12 (K=7)，threshold 达到 10/12
- **MMLU 全面显著**：majority 下 6/6 个 MMLU condition 的 K_eff 全部显著（p<0.05），ARC 仅 2/6
- **Bayesian 方法失效**：K=7 下 0/12 显著，可能是贝叶斯平滑过度抹平了 K_eff 变异
- **最强效应**：arc×score_manipulation 的 keff_β_std=0.845 最大，但 MMLU 条件整体更稳定
- **eta_max 依然弱**：仅 majority 1/12（position_bias）显著，说明 K_eff 是主要驱动因素而非 eta_max

---
