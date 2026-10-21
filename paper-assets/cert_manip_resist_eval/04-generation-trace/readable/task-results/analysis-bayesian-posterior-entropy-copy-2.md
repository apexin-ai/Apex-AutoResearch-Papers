# analysis bayesian posterior entropy

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bayesian-posterior-entropy_20260524T190152_result.json`
- **Structured JSON:** [`2cb78b74d13968a1cc25.json`](../../sessions/2c/2cb78b74d13968a1cc25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果：

**核心发现：**

| K | Entropy (mean±sd) | Effective Judges | Concentration Ratio |
|---|---|---|---|
| 3 | 0.975 ± 0.120 | 2.67 / 3 | 0.890 |
| 5 | 1.470 ± 0.089 | 4.37 / 5 | 0.874 |
| 7 | 1.800 ± 0.069 | 6.07 / 7 | 0.867 |

**统计检验：** Concentration ratio 单调递减（K7/7 < K3/3, p=1.4e-45; K7/7 < K5/5, p=1.4e-27），假说获统计支持。

**但效果量较小：** 比率仅从 0.89 下降到 0.87（~2.3pp）。K=7 时 effective judges 仍有 6.07/7，并非假说预测的 "collapse to 1-2 judges"。concentration 方向正确但幅度不足以完全解释 0/12 neutralization — 可能需要结合其他机制（如攻击选择性靶向高权重 judges、或绝对 log-odds 总量效应）。

输出已保存至 `/root/cert_manip_resist_eval/artifacts/results/plan001/bayesian_posterior_entropy.json`。

---
