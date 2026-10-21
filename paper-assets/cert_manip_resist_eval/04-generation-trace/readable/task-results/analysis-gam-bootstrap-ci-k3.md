# analysis gam bootstrap ci k3

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gam-bootstrap-ci-k3_20260523T163711_result.json`
- **Structured JSON:** [`57bd66d8180930b7d9ba.json`](../../sessions/57/57bd66d8180930b7d9ba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GAM Bootstrap CI (K=3) 完成，已保存到 `docs/paper/data/gam_bootstrap_ci_k3.json`。

**关键发现：当前数据不再复现论文中的 6:6 targeted/shared-bias split。** 所有 12 个条件的 K_eff partial effect 均为正方向：

| 条件 | pos_rate | 95% CI |
|------|----------|--------|
| mmlu×score_manipulation | 0.889 | [-8.48, 44.00] (唯一 CI 跨零) |
| mmlu×prompt_injection | 0.988 | [3.95, 37.64] |
| 其余 10 个条件 | ≥0.999 | 全部显著正 |

`split_consistency_rate = 0.0`——shared-bias 组无一条件显示负方向，与存储在 `gam_tier_analysis_corrected.json` 中的旧 6:6 split 结果矛盾。这是因为底层 score 数据在原始分析之后发生了更新（原始 GCV≈5.81 vs 当前≈0.48）。

---
