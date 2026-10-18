# analysis aggregation bootstrap v2

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_aggregation-bootstrap-v2_20260523T191130_result.json`
- **Structured JSON:** [`9437ffee69501578d042.json`](../../sessions/94/9437ffee69501578d042.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。V2 aggregation bootstrap 重跑结果总结：

### 新旧对比

| Method | V1 OLS dir | V2 OLS dir | V2 Boot sig |
|--------|-----------|-----------|------------|
| Majority | 11+/1- | **12+/0-** | 12/12 |
| Weighted | 11+/1- | **12+/0-** | 12/12 |
| Threshold | 10+/2- | **12+/0-** | 12/12 |
| **Bayesian** | **3+/9-** | **8+/4-** | 6/12 |

### 关键发现

- **Bayesian 方向反转消失**：V1 的 3+/9- 是 `.get("winner","tie")` 将 API error 计为 tie 的 artifact。V2 修复后变为 8+/4-，正方向主导。
- **其余 3 种方法更强**：Majority/Weighted/Threshold 全部变为 12+/0-（unanimously positive），boot sig 全部 12/12。
- Bayesian 的 4 个负方向条件集中在 ARC-Challenge 的 prompt_injection（-6.68）、sycophancy（-0.71）、score_manipulation（-0.46）、verbosity_bias（-0.96），这些 CI 跨零，非显著。

结果已保存至本地 `docs/paper/data/aggregation_bootstrap_corrected.json`。

---
