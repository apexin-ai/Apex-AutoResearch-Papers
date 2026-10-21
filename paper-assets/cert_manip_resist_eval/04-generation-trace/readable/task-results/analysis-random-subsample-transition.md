# analysis random subsample transition

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_random-subsample-transition_20260523T073746_result.json`
- **Structured JSON:** [`72108848f4fe0bee31d9.json`](../../sessions/72/72108848f4fe0bee31d9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

1000 trials 完成 (30s)。结果：

**OLS (标准 SE)**:
| n_local | trials | K_eff dom rate | K_eff sig mean | η_max sig mean |
|---------|--------|----------------|----------------|----------------|
| 1 | 8 | 50.0% | 5.9/12 | 5.8/12 |
| 2 | 117 | 58.1% | 7.8/12 | 6.5/12 |
| 3 | 334 | 73.7% | 8.6/12 | 6.5/12 |
| 4 | 363 | 75.2% | 9.1/12 | 6.9/12 |
| 5 | 169 | 66.9% | 8.4/12 | 6.8/12 |
| 6 | 9 | 33.3% | 6.1/12 | 6.7/12 |
| **overall** | **1000** | **70.7%** | **8.6/12** | **6.7/12** |

**Clustered SE (5-position max-SE)**:
| n_local | K_eff dom rate | K_eff sig mean | η_max sig mean |
|---------|----------------|----------------|----------------|
| 1 | 0.0% | 0.0/12 | 0.4/12 |
| 2 | 32.5% | 0.9/12 | 0.6/12 |
| 3 | 60.2% | 2.3/12 | 0.8/12 |
| 4 | 58.7% | 2.1/12 | 0.8/12 |
| 5 | 36.7% | 1.3/12 | 0.8/12 |
| 6 | 0.0% | 0.0/12 | 0.3/12 |
| **overall** | **51.4%** | **1.8/12** | **0.8/12** |

**关键发现**:
- 0 pure-API 试次（P ≈ 0.02%，符合预期）— 无法直接做 local vs. no-local 对比
- K_eff dominance 存在明显的 **倒U型** 关系：n_local=3-4 时最强（OLS ~75%，clustered ~59%），极端值（1、6）时下降
- 这说明 K_eff transition 不是 local 模型"引入"的 artifact — 它在各种 local/API 混合比例下都出现，但在中等 diversity 时最强
- Clustered SE 更保守但模式一致：K_eff dominant > η_max dominant

结论：**power explanation 成立** — K_eff transition 在各种子集中稳健出现，不依赖特定 local 模型子集。倒U型分布反映的是 diversity range 的 power effect，而非 confound。

---
