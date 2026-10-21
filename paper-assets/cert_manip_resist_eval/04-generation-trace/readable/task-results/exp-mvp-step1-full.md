# exp mvp step1 full

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_mvp-step1-full_20260521T214445_result.json`
- **Structured JSON:** [`78d6413b8a7981d56f06.json`](../../sessions/78/78d6413b8a7981d56f06.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据采集完毕。以下是完整的 Step 1 结果汇报：

---

## Step 1 全量结果：6 模型 × 2 数据集 × 300 样本

**运行时间**：05:50 → 06:22（共 32 分钟）

---

### MMLU 数据集（300 样本）

#### Within-family pairs（4 对）

| Judge i | Judge j | MI | MI 95% CI | ρ (copula) | ρ 95% CI | Agreement | Agree 95% CI |
|---|---|---|---|---|---|---|---|
| llama3.1-70b | llama3.1-8b | 0.0447 | [0.022, 0.077] | 0.174 | [0.077, 0.275] | 0.617 | [0.563, 0.667] |
| qwen2.5-14b | qwen2.5-32b | 0.1911 | [0.141, 0.267] | 0.263 | [0.095, 0.334] | 0.667 | [0.617, 0.720] |
| qwen2.5-14b | qwen2.5-72b | 0.2364 | [0.178, 0.313] | 0.276 | [0.119, 0.361] | 0.697 | [0.643, 0.747] |
| qwen2.5-32b | qwen2.5-72b | **0.3060** | [0.242, 0.389] | **0.364** | [0.276, 0.496] | **0.790** | [0.743, 0.833] |

#### Cross-family pairs（11 对）

| Judge i | Judge j | MI | MI 95% CI | ρ (copula) | ρ 95% CI | Agreement | Agree 95% CI |
|---|---|---|---|---|---|---|---|
| llama3.1-70b | mistral-large | 0.2358 | [0.167, 0.321] | 0.403 | [0.300, 0.500] | 0.793 | [0.743, 0.840] |
| llama3.1-70b | qwen2.5-14b | 0.1222 | [0.080, 0.179] | 0.088 | [-0.024, 0.199] | 0.563 | [0.510, 0.620] |
| llama3.1-70b | qwen2.5-32b | 0.2605 | [0.201, 0.336] | 0.386 | [0.246, 0.451] | 0.763 | [0.713, 0.810] |
| llama3.1-70b | qwen2.5-72b | 0.2780 | [0.216, 0.352] | 0.313 | [0.219, 0.421] | 0.747 | [0.697, 0.797] |
| llama3.1-8b | mistral-large | 0.0428 | [0.018, 0.087] | 0.212 | [0.070, 0.286] | 0.607 | [0.547, 0.663] |
| llama3.1-8b | qwen2.5-14b | 0.0374 | [0.016, 0.073] | 0.177 | [0.056, 0.261] | 0.460 | [0.403, 0.517] |
| llama3.1-8b | qwen2.5-32b | 0.0235 | [0.010, 0.053] | 0.144 | [-0.026, 0.198] | 0.533 | [0.480, 0.593] |
| llama3.1-8b | qwen2.5-72b | 0.0296 | [0.013, 0.062] | 0.132 | [-0.018, 0.191] | 0.533 | [0.473, 0.590] |
| mistral-large | qwen2.5-14b | 0.1052 | [0.066, 0.163] | 0.030 | [-0.030, 0.188] | 0.547 | [0.490, 0.607] |
| mistral-large | qwen2.5-32b | 0.1957 | [0.145, 0.268] | 0.320 | [0.223, 0.424] | 0.717 | [0.663, 0.767] |
| mistral-large | qwen2.5-72b | 0.2617 | [0.204, 0.337] | 0.283 | [0.220, 0.428] | 0.737 | [0.690, 0.790] |

#### MMLU 统计检验

- **Within-family MI mean**: 0.1946
- **Cross-family MI mean**: 0.1448
- **Hypothesis holds**: **True** (within > cross)
- **Mann-Whitney U p**: 0.206（不显著）
- **Permutation p**: 0.218（不显著）

---

### ARC-Challenge 数据集（300 样本）

#### Within-family pairs（4 对）

| Judge i | Judge j | MI | MI 95% CI | ρ (copula) | ρ 95% CI | Agreement | Agree 95% CI |
|---|---|---|---|---|---|---|---|
| llama3.1-70b | llama3.1-8b | 0.0877 | [0.048, 0.136] | 0.284 | [0.162, 0.359] | 0.677 | [0.623, 0.730] |
| qwen2.5-14b | qwen2.5-32b | 0.3190 | [0.247, 0.397] | 0.278 | [0.109, 0.335] | 0.723 | [0.673, 0.770] |
| qwen2.5-14b | qwen2.5-72b | 0.3211 | [0.253, 0.408] | 0.232 | [0.053, 0.298] | 0.733 | [0.683, 0.783] |
| qwen2.5-32b | qwen2.5-72b | **0.4510** | [0.386, 0.534] | **0.408** | [0.278, 0.488] | **0.867** | [0.827, 0.907] |

#### Cross-family pairs（11 对）

| Judge i | Judge j | MI | MI 95% CI | ρ (copula) | ρ 95% CI | Agreement | Agree 95% CI |
|---|---|---|---|---|---|---|---|
| llama3.1-70b | mistral-large | **0.4870** | [0.409, 0.559] | **0.584** | [0.534, 0.632] | **0.943** | [0.913, 0.967] |
| llama3.1-70b | qwen2.5-14b | 0.2321 | [0.172, 0.302] | 0.127 | [-0.023, 0.193] | 0.653 | [0.600, 0.707] |
| llama3.1-70b | qwen2.5-32b | 0.4817 | [0.414, 0.563] | 0.516 | [0.409, 0.574] | 0.907 | [0.873, 0.937] |
| llama3.1-70b | qwen2.5-72b | 0.3824 | [0.310, 0.464] | 0.440 | [0.343, 0.517] | 0.853 | [0.813, 0.893] |
| llama3.1-8b | mistral-large | 0.0863 | [0.047, 0.134] | 0.250 | [0.149, 0.348] | 0.673 | [0.620, 0.727] |
| llama3.1-8b | qwen2.5-14b | 0.1324 | [0.085, 0.190] | 0.203 | [0.078, 0.300] | 0.670 | [0.620, 0.720] |
| llama3.1-8b | qwen2.5-32b | 0.1119 | [0.066, 0.166] | 0.301 | [0.184, 0.378] | 0.700 | [0.647, 0.750] |
| llama3.1-8b | qwen2.5-72b | 0.1137 | [0.069, 0.170] | 0.270 | [0.171, 0.375] | 0.707 | [0.653, 0.757] |
| mistral-large | qwen2.5-14b | 0.2179 | [0.162, 0.285] | 0.079 | [-0.070, 0.146] | 0.633 | [0.580, 0.687] |
| mistral-large | qwen2.5-32b | 0.4500 | [0.381, 0.524] | 0.495 | [0.377, 0.541] | 0.893 | [0.860, 0.927] |
| mistral-large | qwen2.5-72b | 0.3971 | [0.332, 0.477] | 0.412 | [0.308, 0.486] | 0.853 | [0.813, 0.893] |

#### ARC-Challenge 统计检验

- **Within-family MI mean**: 0.2947
- **Cross-family MI mean**: 0.2811
- **Hypothesis holds**: **True** (within > cross)
- **Mann-Whitney U p**: 0.525（不显著）
- **Permutation p**: 0.427（不显著）

---

### 关键发现

1. **假设方向正确但统计不显著**：两个数据集上 within-family MI 均高于 cross-family MI，但 p 值远超 0.05。MMLU (p=0.206/0.218) 比 ARC (p=0.525/0.427) 稍好一些。

2. **主要原因：llama3.1-8b 是 outlier**。它与同家族 70b 的 MI 极低（MMLU 0.045, ARC 0.088），反而拉低了 within-family 均值。而多个 cross-family 大模型对（如 llama-70b↔mistral-large MI=0.487, llama-70b↔qwen-32b MI=0.482）的 MI 远高于 within-family 对。

3. **模型质量主导**：大模型之间（不论家族）一致性很高（agreement 0.85-0.94），小模型与任何大模型的一致性都低（0.46-0.71）。模型能力差异比家族身份对 correlation 的影响大得多。

4. **Qwen 家族内部梯度清晰**：72b↔32b (MI=0.306/0.451) > 72b↔14b (MI=0.236/0.321) > 32b↔14b (MI=0.191/0.319)，与模型规模的接近程度一致。

**结果文件**：`/root/cert_manip_resist_eval/artifacts/results/results_step1_full_20260521_222222.json`

---
