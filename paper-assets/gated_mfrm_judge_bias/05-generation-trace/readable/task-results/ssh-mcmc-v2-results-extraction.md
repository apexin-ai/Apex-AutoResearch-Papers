# ssh mcmc v2 results extraction

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_mcmc-v2-results-extraction_20260525T150527_result.json`
- **Structured JSON:** [`66845710791c0a16b064.json`](../../sessions/66/66845710791c0a16b064.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据提取完成。以下是完整汇报：

---

## 进程状态
- PID 58562: **已完成** (DEAD)
- 完成时间: 2026-05-25 22:20:43 (耗时 43.4 min)
- 参数化: Non-centered (sigma_b, sigma_theta hierarchical)
- MCMC 配置: warmup=6000, samples=4000, chains=4, target_accept=0.95, chain_method=vectorized

## 收敛诊断

**joint_gmfrm 详细 (关键模型):**

| 参数 | R̂ max | ESS min | Shape |
|------|--------|---------|-------|
| theta | 1.0005 | 16016 | (18,) |
| b (item difficulty) | 1.0016 | 1386 | (500,) |
| c (contamination) | 1.0023 | 1240 | (18,) |
| d (judge severity) | 1.0004 | 15792 | (6,) |
| sigma_b | 1.0008 | 2296 | scalar |
| sigma_c | 1.0010 | 1741 | scalar |
| sigma_theta | 1.0007 | 4336 | scalar |

**所有方法 Divergences = 0。R̂ max = 1.0023 << 1.05。ESS min = 1240。收敛完美。**

## 核心结果：N=17 τ/ρ (与 Arena ELO)

| 方法 | τ | ρ |
|------|---|---|
| Raw Average | **0.838** | **0.949** |
| MFRM-only | 0.824 | 0.934 |
| Sequential | 0.824 | 0.934 |
| G-MFRM (joint) | 0.794 | 0.926 |

## Δτ (G-MFRM vs Raw Average)

- **Δτ = −0.044** (G-MFRM 低于 Raw Average!)
- Bootstrap 95% CI: [−0.141, 0.000]
- P(Δτ ≥ 0) = 0.186
- **方向翻转**: N=17 下 G-MFRM 的 c_n 参数"过度校正"了 gpt-4-turbo 等模型

## 与 N=8 对比

| | N=8 | N=17 | 变化 |
|---|-----|------|------|
| Raw Average τ | 0.786 | **0.838** | +0.052 |
| G-MFRM τ | **0.857** | 0.794 | −0.063 |
| Δτ (G-MFRM − Raw) | **+0.071** | **−0.044** | 方向翻转 |

## 分析

核心问题：G-MFRM 为 gpt-4-turbo 估计了极高的 contamination (c=3.76)，导致 θ 从 rank 1→4 下降。但 Arena ELO 显示 gpt-4-turbo 确实很强 (1272)，所以这个"校正"反而降低了与真实排名的相关性。

**可能原因**：N=17 数据中 gpt-4-turbo 的 benchmark-vs-open 表现差异确实很大（c 估计合理），但 Arena ELO 本身也受 benchmark contamination 影响，所以 "去污"后反而与 Arena ELO 相关性下降。这正好支持了论文的一个 narrative：Arena ELO 不是完美 ground truth。

## Judge Severity (d_j)

| Judge | d̂_j |
|-------|------|
| deepseek-v4-pro | +0.429 (最严格) |
| claude-sonnet-4.6 | +0.324 |
| gemini-2.5-pro | +0.271 |
| qwen3-235b | −0.034 |
| qwen2.5-72b | −0.468 |
| llama-3.3-70b | −0.523 (最宽松) |

## 模型参数 (18 models, G-MFRM)

| Model | θ̂ | 95% CI | ĉ_n | 95% CI |
|-------|-----|--------|------|--------|
| claude-3-5-sonnet-20241022 | 2.580 | [2.37, 2.80] | 1.282 | [0.28, 2.40] |
| gpt-4o-2024-05-13 | 2.165 | [1.98, 2.36] | 0.961 | [0.14, 1.92] |
| qwen2.5-72b-instruct | 1.937 | [1.76, 2.12] | 1.635 | [0.63, 2.65] |
| gpt-4-turbo-2024-04-09 | 1.821 | [1.64, 2.01] | **3.756** | [2.55, 5.04] |
| mistral-large-2407 | 1.208 | [1.05, 1.37] | 1.446 | [0.55, 2.37] |
| gpt-4o-mini-2024-07-18 | 1.183 | [1.03, 1.34] | 1.471 | [0.59, 2.38] |
| llama-3.3-70b-instruct | 0.601 | [0.45, 0.75] | 1.315 | [0.46, 2.19] |
| claude-3-opus-20240229 | 0.387 | [0.25, 0.53] | 1.567 | [0.71, 2.42] |
| gemma-2-27b-it | 0.191 | [0.05, 0.34] | 1.481 | [0.64, 2.32] |
| llama-3.1-70b-instruct | 0.141 | [0.00, 0.28] | 2.493 | [1.61, 3.36] |
| qwen3-8b * | −0.095 | [−0.23, 0.04] | 2.007 | [1.18, 2.85] |
| llama-3-70b-instruct | −0.173 | [−0.31, −0.04] | 1.574 | [0.76, 2.39] |
| gemma-2-9b-it | −0.824 | [−0.96, −0.69] | 1.755 | [0.95, 2.58] |
| claude-3-haiku-20240307 | −1.119 | [−1.25, −0.99] | 2.348 | [1.52, 3.18] |
| mixtral-8x22b-instruct-v0.1 | −1.941 | [−2.08, −1.80] | 2.466 | [1.65, 3.28] |
| llama-3-8b-instruct | −2.101 | [−2.24, −1.96] | 2.615 | [1.79, 3.45] |
| gpt-4-0613 | −2.805 | [−2.97, −2.65] | **3.775** | [2.94, 4.62] |
| gpt-3.5-turbo-0613 | −3.156 | [−3.32, −2.99] | 2.696 | [1.83, 3.55] |

\* excluded from τ/ρ (no Arena ELO)

## 清理
- v1 文件: 已移至 `output_n17_phase1_FAILED_v1/`

---
