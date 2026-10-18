# analysis beta reg epsilon

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_beta-reg-epsilon_20260522T231659_result.json`
- **Structured JSON:** [`26109583c30a418f935e.json`](../../sessions/26/26109583c30a418f935e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `artifacts/results/plan001/beta_reg_epsilon.json`。

**Part A — Beta Regression vs OLS:**
- Beta regression (GLM Binomial/logit) FDR sig: η_max 1/12, K_eff 0/12（远低于 OLS 的 11/12 和 8/12）
- η_max dominates in 7/12 conditions by |std β|
- 与 OLS 的 η_max vs K_eff 重要性排序在 **10/12 conditions 一致**，2 个 condition 排序反转（`arc_challenge__prompt_injection` 和 `arc_challenge__score_manipulation`，beta regression 中 K_eff > η_max）
- Pseudo R² 范围 0.24–0.65

**Part B — ε Sensitivity:**

| ε | η_max FDR sig | K_eff FDR sig |
|---|---|---|
| 1e-3 | 10/12 | 8/12 |
| 1e-6 | 11/12 | 8/12 |
| 1e-9 | 10/12 | 6/12 |

- max β change vs baseline (ε=1e-6): **472%**，主要来自 ASR 接近 0 的 condition
- η_max 的 FDR sig count 在三个 ε 下基本稳定（10-11/12），K_eff 在 ε=1e-9 时降至 6/12

---
