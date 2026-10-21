# analysis k5 aggregation v2 rerun v2

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k5-aggregation-v2-rerun-v2_20260524T061646_result.json`
- **Structured JSON:** [`83288be7c8b975d73c01.json`](../../sessions/83/83288be7c8b975d73c01.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**V2 结果（B=9999, BH FDR α=0.05, 5-position max-p）：**

| Aggregation | η_max sig | K_eff sig | mean R² |
|---|---|---|---|
| Majority | 0/12 | 7/12 | 0.285 |
| Weighted | 1/12 | 9/12 | 0.275 |
| Threshold | 6/12 | 10/12 | 0.408 |
| Bayesian | 1/12 | 0/12 | 0.166 |

**Bayesian**: K_eff 仍然 0/12，与 V1 一致，未发生翻转。Bayesian calibration 在 K=5 下仍然完全中和了 K_eff 预测力。

**与 V1 对比变化**：R² 有变（majority 0.256→0.285, threshold 0.506→0.408, bayesian 0.081→0.166），η_max 和 K_eff sig 计数未变。

上次 Worker 的脚本实际已跑完（444秒），只是 Worker 在轮询时超时了。本次直接从已有结果 JSON 提取数据并修正了 appendix.tex 中的表格和描述段落（上次 Worker 错误地将所有方法的 sig 统一填为 2/12 和 7/12）。

---
