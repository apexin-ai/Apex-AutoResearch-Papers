# analysis phase2 crossmodel perm dstudy

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase2_crossmodel_perm_dstudy_20260521T224225_result.json`
- **Structured JSON:** [`5b4d7024a6f3c3eb5ea9.json`](../../sessions/5b/5b4d7024a6f3c3eb5ea9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三合一分析完成。结果汇总：

## Part A: 8-model MMLU Cross-model G-study

| Component | 4-model | 8-model | 变化 |
|-----------|---------|---------|------|
| item_id% | 41.55% | **37.88%** | -3.67 |
| model:item_id% | 32.81% | **30.21%** | -2.60 |
| G_item | 0.816 | **0.896** [0.874, 0.914] | +0.080 |

8 models: DeepSeek-7B, Gemma-2-9B, InternLM2.5-7B, Llama-3.1-8B, Mistral-7B-v0.3, OLMo-2-7B, Qwen3-8B, Yi-1.5-9B. 更多模型降低了 item 和 model×item 方差占比，但因平均效应改善了 G_item。

## Part B: MC vs FF Permutation Test

| Group | Benchmarks | item_id% | Mean |
|-------|-----------|----------|------|
| MC | MMLU 37.88%, ARC 37.88%, HellaSwag 32.20% | | 35.99% |
| FF | GSM8K 16.86%, MATH 24.05% | | 20.45% |

- **Observed diff**: 15.53%
- **p = 0.0995** (one-sided, 10000 permutations)
- **Cohen's d = 3.91** (very large effect)
- **95% CI for diff**: [10.04%, 21.03%]
- n=5 benchmarks 限制了统计功效。措辞：**format-conditional variance structure**，非 "significant difference"

## Part C: D-study Projections

| Benchmark | n_models | G_current | item_id% | n(G≥0.80) |
|-----------|----------|-----------|----------|-----------|
| MMLU | 8 | 0.896 | 37.88% | **93** |
| ARC | 8 | 0.892 | 37.88% | **98** |
| HellaSwag | 6 | 0.824 | 32.20% | **171** |
| GSM8K | 8 | 0.863 | 16.86% | **128** |
| MATH | 8 | 0.888 | 24.05% | **101** |

所有 D-study 曲线通过单调性断言。MC benchmarks 需要更少 items 达到 G≥0.80（93-98 vs 128-171），但 HellaSwag 例外（model:item 交互最大）。

结果保存：`westd-32570:/root/nlp_variance_gtheory/results/exp004_8model_analysis/three_in_one_8model.json`

---
