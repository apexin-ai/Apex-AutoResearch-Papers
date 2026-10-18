# analysis aggregation bootstrap

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_aggregation-bootstrap_20260523T171836_result.json`
- **Structured JSON:** [`5fddb9affef3b023643b.json`](../../sessions/5f/5fddb9affef3b023643b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Bootstrap 分析完成 (B=9999, 134s)。结果：

| Method | Paper Table 2 | Bootstrap Direction | Bootstrap Sig |
|--------|--------------|-------------------|--------------|
| **Majority** | 7+/1- | 11+/1- (confirmed) | 9/12 |
| **Weighted** | 9+/0- | 11+/1- (confirmed) | 10/12 |
| **Threshold** | 10+/1- | 11+/1- (confirmed) | 11/12 |
| **Bayesian** | 1+/6- | 3+/9- (reversal confirmed) | 7/12 |

关键验证：
- **Bayesian direction reversal 稳健**：6 个强负向 condition 的 positive rate 为 0-1.3%，95% CI 全在负半轴，不是统计伪迹
- **Threshold 最稳健**：11/12 bootstrap-confirmed significant，最高一致性
- **Weighted 方向最稳定**：除 arc_sycophancy 外全为 100% positive rate

输出已写入 `docs/paper/data/aggregation_bootstrap.json`。

---
