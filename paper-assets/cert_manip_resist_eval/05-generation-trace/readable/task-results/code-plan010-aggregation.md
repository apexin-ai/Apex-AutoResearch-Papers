# code plan010 aggregation

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan010-aggregation_20260522T120049_result.json`
- **Structured JSON:** [`a5b91f59f124698f9ec8.json`](../../sessions/a5/a5b91f59f124698f9ec8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

运行完成。结果：

| 方法 | η_max sig | K_eff sig neg | mean R² |
|------|-----------|---------------|---------|
| majority_vote | 8/12 | 1/12 | 0.446 |
| weighted_vote | 7/12 | 1/12 | 0.378 |
| threshold_vote | 7/12 | 0/12 | 0.693 |
| bayesian | 3/12 | 0/12 | 0.223 |

**关键发现：**

1. **Majority 和 weighted vote** 模式一致：η_max 在多数条件下显著，支持 weakest-link。

2. **Threshold vote**（unanimous）很特殊：η_max 仍然在 7/12 显著，但 K_eff 在 7+ 条件下呈**正**显著（不是负）。解释：unanimity 要求下，diversity 高的 panel 更容易被攻击打破共识。R² 最高（0.693）。

3. **Bayesian** η_max 仅在 3/12 显著 — 可靠性加权有效缓解了 weakest-link 效应。Bayesian 对弱 judge 降权后，最弱 judge 的影响力下降。

**结论：** Theorem 1 的 weakest-link 效应不是普适的，依赖聚合规则。Bayesian aggregation 部分打破了 η_max 主导。结果已保存到 `results_plan010_aggregation.json`。

---
