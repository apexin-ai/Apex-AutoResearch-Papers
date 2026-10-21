# analysis k5 rf contrast

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_k5-rf-contrast_20260523T070356_result.json`
- **Structured JSON:** [`6c0aec54cb417aba84f8.json`](../../sessions/6c/6c0aec54cb417aba84f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

K=5 RF contrast analysis 完成。结果：

**K=5 RF vs Adaptive 对比**

| | mmlu R² | arc R² | K_eff boot sig |
|---|---|---|---|
| **K=3 RF** | 0.734 | 0.813 | 2/2 |
| **K=5 RF** | 0.659 | 0.751 | 2/2 |
| **K=5 Adaptive** (mean) | 0.299 | 0.213 | — |

**关键发现**：
- RF mean R²=0.705 vs adaptive mean R²=0.256，gap=+0.449
- K_eff 在 RF 下 2/2 conditions 显著（OLS、clustered SE、bootstrap 三种方法一致）
- eta_max 在 mmlu 下显著（bootstrap p=0.007），arc 下不显著（bootstrap p=0.570）
- K=5 RF R² 略低于 K=3 RF（符合预期：K 增大时 majority vote threshold 提高，RF ASR 下降），但仍远高于 adaptive
- 结论与 K=3 一致：RF 模型（独立误差假设）比 adaptive 模型解释更多方差，K_eff 在 RF 下始终显著

输出文件：`/root/cert_manip_resist_eval/artifacts/results/plan001/k5_rf_contrast.json`

---
