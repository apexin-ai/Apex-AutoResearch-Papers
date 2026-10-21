# analysis copula gof

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_copula-gof_20260521T224845_result.json`
- **Structured JSON:** [`8ae61939df6ac0b5f9ec.json`](../../sessions/8a/8ae61939df6ac0b5f9ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### MMLU
| 指标 | 值 |
|------|-----|
| Mean ratio (MI_obs / MI_gauss) | **21.13** |
| Pairs with ratio > 2 | **14/15** |
| 结论 | Gaussian copula 假设系统性违反 |

极端案例：`mistral-large <-> qwen2.5-14b` ratio = 235.86（ρ 极低但 MI 不低，说明依赖结构高度非线性）。

### ARC Challenge
| 指标 | 值 |
|------|-----|
| Mean ratio (MI_obs / MI_gauss) | **10.36** |
| Pairs with ratio > 2 | **15/15** |
| 结论 | Gaussian copula 假设系统性违反 |

极端案例：`mistral-large <-> qwen2.5-14b` ratio = 69.43。

**总结**：两个数据集上 Gaussian copula 假设均被系统性违反——观测 MI 远大于 Gaussian copula 对应的 MI，表明 judge 间的依赖结构包含大量非线性/尾部依赖，不能用简单的相关系数 ρ 刻画。

---
