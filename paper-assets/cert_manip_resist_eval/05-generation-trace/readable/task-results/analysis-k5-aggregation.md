# analysis k5 aggregation

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k5-aggregation_20260523T030937_result.json`
- **Structured JSON:** [`8d33c32b8669b02fde11.json`](../../sessions/8d/8d33c32b8669b02fde11.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## K=5 Aggregation Gradient 结果

### Summary Table

| Method | η_max FDR sig | K_eff FDR sig | K_pos | K_neg | Mean R² |
|--------|--------------|---------------|-------|-------|---------|
| **Majority** | 10/12 | **12/12** | 11 | 1 | 0.256 |
| **Weighted** | 9/12 | **11/12** | 11 | 0 | 0.249 |
| **Threshold (≥4/5)** | 12/12 | **11/12** | 11 | 0 | 0.506 |
| **Bayesian** | 8/12 | **10/12** | **10** | **0** | 0.081 |

### K=3 vs K=5 对比

| Method | K=3 η_max | K=5 η_max | K=3 K_eff | K=5 K_eff |
|--------|-----------|-----------|-----------|-----------|
| Majority | 11/12 | 10/12 | 8/12 | **12/12** |
| Weighted | 9/12 | 9/12 | 9/12 | **11/12** |
| Threshold | 12/12 | 12/12 | 11/12 | 11/12 |
| Bayesian | 9/12 | 8/12 | 7/12 (6neg) | **10/12 (0neg)** |

### 关键发现

**Bayesian K_eff 反转消失**：K=3 下 Bayesian 有 6/7 个显著 K_eff 为负方向（反转），K=5 下 10/10 显著 K_eff 全部正方向，`bayesian_keff_reversal = false`。

机制解释：K=5 下更多 judges 参与 log-odds 累积，Bayesian calibration 的 "高可信度 judge 被少数攻击翻转" 效应被稀释，diversity (K_eff) 恢复为正向保护作用。

Mean standardized β：
- K_eff: majority 0.334, weighted 0.401, threshold 0.442, bayesian 0.136
- η_max: majority 0.180, weighted 0.107, threshold 0.316, bayesian 0.110

K_eff 在 K=5 下全面成为主导因子（所有 4 种 aggregation 的 K_eff β_mean > η_max β_mean）。

---
