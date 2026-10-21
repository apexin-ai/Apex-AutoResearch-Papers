# ssh refit complete analysis

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_refit_complete_analysis_20260522T212709_result.json`
- **Structured JSON:** [`cc661f2f10452e17cb62.json`](../../sessions/cc/cc661f2f10452e17cb62.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果已保存到 `refit_summary.json`。汇报如下：

---

## Exp-003b Refit 完整后验结果

### 1. InferenceData 文件
- **大小**: 14.7 MB (`joint_gmfrm_idata.nc`)
- **配置**: 4 chains × 4000 samples, warmup=4000, target_accept=0.95

### 2. 收敛诊断
- **Divergent transitions: 0**
- **Max R-hat**: theta 全部 ≤1.01, c 最高 1.03 (llama-3.3-70b), d 全部 1.00, **sigma_c = 1.03**
- sigma_c 的 ESS_bulk=227 偏低（其余参数 ESS_bulk 均 >400），但 R-hat 仍在可接受范围

### 3. θ (ability) 95% CI per model

| Model | Mean | 95% CI | ESS_bulk |
|-------|------|--------|----------|
| gpt-4o | 2.00 | [1.70, 2.30] | 2200 |
| gpt-4o-mini | 1.40 | [1.10, 1.70] | 2552 |
| qwen2.5-72b | 1.20 | [0.85, 1.50] | 1536 |
| llama-3.3-70b | 0.54 | [0.23, 0.85] | 1720 |
| qwen3-8b | 0.51 | [0.22, 0.79] | 1643 |
| gemma-2-9b | -0.50 | [-0.79, -0.21] | 2185 |
| gpt-4-0613 | -1.90 | [-2.20, -1.60] | 3154 |
| gpt-3.5-turbo-0125 | -3.30 | [-3.60, -3.00] | 2400 |

### 4. c (contamination) 95% CI per model — 论文核心

| Model | Mean | 95% CI | ESS_bulk |
|-------|------|--------|----------|
| **gpt-3.5-turbo-0125** | **5.60** | **[4.40, 6.80]** | 1293 |
| **gpt-4-0613** | **4.20** | **[3.10, 5.30]** | 1462 |
| qwen2.5-72b | 3.00 | [1.40, 4.60] | 473 |
| llama-3.3-70b | 2.50 | [1.10, 3.90] | 217 |
| gemma-2-9b | 1.70 | [0.36, 2.90] | 841 |
| qwen3-8b | 1.20 | [0.14, 2.50] | 461 |
| gpt-4o-mini | 0.93 | [0.059, 2.20] | 913 |
| gpt-4o | 0.88 | [0.052, 2.20] | 970 |

**所有模型 c 的 95% CI 下界均 >0**，contamination effect 显著非零。gpt-3.5-turbo 和 gpt-4-0613 的 contamination 远高于其他模型（CI 完全不重叠 gpt-4o/gpt-4o-mini）。

### 5. d (judge severity) 95% CI

| Judge | Mean | 95% CI | ESS_bulk |
|-------|------|--------|----------|
| claude-opus-4.7-proxy | 0.60 | [0.43, 0.76] | 3913 |
| gpt-5.5-proxy | 0.53 | [0.37, 0.70] | 3669 |
| deepseek-v4-pro-proxy | 0.31 | [0.073, 0.54] | 2848 |
| claude-sonnet-4.6-proxy | 0.14 | [-0.037, 0.31] | 4311 |
| gemini-2.5-pro-proxy | -0.036 | [-0.27, 0.19] | 3040 |
| qwen3-235b-proxy | -0.038 | [-0.24, 0.16] | 3825 |
| qwen2.5-72b | -0.35 | [-0.64, -0.066] | 2625 |
| llama-3.3-70b | -0.42 | [-0.66, -0.18] | 3125 |
| mistral-large-2 | -0.74 | [-1.10, -0.37] | 1244 |

Judge d 参数收敛良好（全部 R-hat=1.00, ESS_bulk >1200）。Claude Opus 和 GPT-5.5 最宽松（d>0），Mistral-Large-2 最严格。

### 6. σ_c (contamination spread)
- **Mean: 2.40**, **95% CI: [1.70, 3.40]**
- ESS_bulk=227（偏低），R-hat=1.03
- CI 下界远离 0，确认模型间 contamination 存在显著异质性

### 7. 注意事项
- `c[llama-3.3-70b]` ESS_bulk=217 和 `sigma_c` ESS_bulk=227 偏低，如果论文需要更紧的 claim 可考虑增加 samples 或 warmup
- 无 divergence，整体收敛可接受

---
