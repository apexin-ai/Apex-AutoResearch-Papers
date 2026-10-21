# analysis k5 aggregation bootstrap

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k5-aggregation-bootstrap_20260523T061722_result.json`
- **Structured JSON:** [`dd08175aa520f3514fc5.json`](../../sessions/dd/dd08175aa520f3514fc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## K=5 Aggregation Bootstrap 结果 (B=9999)

| Method | η_max OLS → Boot | K_eff OLS → Boot | K_pos | K_neg |
|--------|------------------|------------------|-------|-------|
| **Majority** | 10/12 → **0/12** | 12/12 → **7/12** | 7 | 0 |
| **Weighted** | 9/12 → **1/12** | 11/12 → **9/12** | 9 | 0 |
| **Threshold** | 12/12 → **6/12** | 11/12 → **10/12** | 10 | 0 |
| **Bayesian** | 8/12 → **1/12** | 10/12 → **0/12** | 0 | 0 |

### 核心发现

1. **Bayesian K_eff 反转确认消失**：OLS 10+/0− → bootstrap 0+/0−。无显著也无负方向。所有 12 个 beta 中仅 1 个为负 (arc×sycophancy -0.043, maxp=0.40)，其余全正但 bootstrap p 值太大未通过 FDR。

2. **Bootstrap deflation 幅度**：
   - Threshold 最稳健：11→10（仅掉 1 个）
   - Weighted 次之：11→9
   - Majority：12→7（大幅下降但比 K=3 的 8→1 好很多）
   - Bayesian：10→0（OLS 结果全是假阳性）

3. **η_max 大幅 deflate**：所有方法 η_max FDR sig 近乎归零（0-6/12），cluster 结构严重影响 η_max 推断。

4. **Validation**：arc×sycophancy majority K_eff β = -0.157（负方向），与 K=3 参考值 -0.192 一致。

---
