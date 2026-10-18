# analysis 15model aggregation regression

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_15model-aggregation-regression_20260522T181241_result.json`
- **Structured JSON:** [`12ca13f1443d6e8670d8.json`](../../sessions/12/12ca13f1443d6e8670d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果保存至 `/root/cert_manip_resist_eval/artifacts/results/plan001/aggregation_regression_15model.json`（944 行）。

### 汇总表格

| Method | η_max FDR sig (/12) | K_eff_resid FDR sig (/12) | K_eff_resid β 方向 | Mean R² |
|---|---|---|---|---|
| majority_vote | **12/12** | **12/12** | 全正 (0 neg) | 0.4333 |
| weighted_vote | **12/12** | **11/12** | 全正 (0 neg) | 0.4185 |
| threshold_vote | 10/12 | 6/12 | 3 neg | 0.1647 |
| bayesian | **12/12** | 5/12 | 3 neg | 0.1414 |

### 关键发现

1. **Bayesian 未能减弱 weakest-link 效应**：η_max 在 bayesian 下仍然 12/12 FDR 显著（与 majority 相同）。这与 6-model 结果（3/12 vs 8/12）不同——扩大到 15 模型后 η_max 的主导性更加稳固。

2. **Bayesian/threshold 大幅降低了 K_eff_resid 的显著性**：majority 12/12 → bayesian 5/12、threshold 6/12。说明这两种聚合削弱了 diversity 的独立预测力。

3. **Dual driver pattern 变化**：majority/weighted 下 K_eff 和 η_max 都强显著（dual driver），但 bayesian/threshold 下转为 η_max 单一主导（K_eff 多数不显著），且 R² 从 ~0.43 降到 ~0.15。

4. **K_eff β 方向翻转**：majority/weighted 下 K_eff_resid β 全正（diversity 增加 vulnerability），bayesian/threshold 出现 3/12 负方向。

---
