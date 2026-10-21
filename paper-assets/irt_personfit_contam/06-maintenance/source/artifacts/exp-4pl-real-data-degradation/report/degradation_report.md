# 3PL vs 4PL lz* Degradation Analysis on Real Data

## Overview

Compared 4PL lz* (with estimated d parameters) against 3PL lz* (d=1.0) for 12 PSN-IRT models across 5 benchmarks.

## d-Parameter Statistics by Benchmark

| Benchmark | Items | Mean d | Std d | % d<0.95 | % d<0.90 | % d<0.80 |
|-----------|-------|--------|-------|----------|----------|----------|
| MMLU | 14042 | 0.8921 | 0.1499 | 46.1% | 28.4% | 16.7% |
| HellaSwag | 10042 | 0.9304 | 0.1109 | 34.2% | 16.8% | 7.9% |
| GSM8K | 1319 | 0.9167 | 0.1297 | 38.4% | 20.3% | 10.6% |
| ARC-C | 295 | 0.9481 | 0.0901 | 24.1% | 10.5% | 4.7% |
| HumanEval | 164 | 0.8957 | 0.1393 | 50.6% | 28.0% | 14.6% |

## Δlz* Summary by Benchmark

| Benchmark | Mean Δlz* | Std Δlz* | Mean |Δlz*| | Max |Δlz*| |
|-----------|-----------|----------|-------------|-------------|
| MMLU | 51.925 | 101.674 | 58.314 | 357.083 |
| HellaSwag | 46.012 | 94.604 | 46.498 | 341.244 |
| GSM8K | 14.377 | 20.399 | 14.717 | 61.842 |
| ARC-C | 5.899 | 11.131 | 5.983 | 40.584 |
| HumanEval | 6.286 | 11.861 | 6.467 | 42.191 |

## Δlz* by Model (sorted by impact)

| Model | Mean Δlz* | Mean |Δlz*| |
|-------|-----------|-------------|
| DeepSeek-V3 | 168.589 | 168.589 |
| Hunyuan-Turbo | 35.407 | 35.407 |
| 360GPT2-Pro | 24.643 | 24.643 |
| Qwen-Plus | 19.458 | 19.458 |
| Doubao-pro | 19.117 | 19.117 |
| Gemini-1.5 | 2.911 | 14.488 |
| Moonshot-v1 | 14.482 | 14.482 |
| Yi-Lightning | 13.219 | 13.219 |
| Qwen2.5-3B-Instruct | 3.970 | 4.124 |
| Gemma-2B-it | -1.251 | 1.251 |
| Vicuna-7B-v1.3 | -0.848 | 1.070 |
| Mistral-7B-Instruct-v0.1 | -0.902 | 0.902 |

## Full Comparison Table

| Model | Benchmark | lz*_4pl | lz*_3pl | Δlz* | %Change |
|-------|-----------|---------|---------|------|---------|
| 360GPT2-Pro | ARC-C | 7.27 | 3.92 | 3.346 | 46.1% |
| DeepSeek-V3 | ARC-C | 1.35 | -39.24 | 40.584 | 3016.5% |
| Doubao-pro | ARC-C | 2.11 | -4.37 | 6.477 | 307.0% |
| Gemini-1.5 | ARC-C | 4.28 | 0.92 | 3.361 | 78.5% |
| Gemma-2B-it | ARC-C | 2.87 | 3.09 | -0.228 | -8.0% |
| Hunyuan-Turbo | ARC-C | 7.47 | 3.59 | 3.881 | 52.0% |
| Mistral-7B-Instruct-v0.1 | ARC-C | 5.52 | 5.80 | -0.281 | -5.1% |
| Moonshot-v1 | ARC-C | 5.41 | 1.76 | 3.656 | 67.5% |
| Qwen-Plus | ARC-C | 6.47 | 3.10 | 3.368 | 52.1% |
| Qwen2.5-3B-Instruct | ARC-C | 5.28 | 4.52 | 0.762 | 14.4% |
| Vicuna-7B-v1.3 | ARC-C | 1.72 | 1.16 | 0.557 | 32.4% |
| Yi-Lightning | ARC-C | -0.71 | -6.00 | 5.300 | 751.6% |
| 360GPT2-Pro | GSM8K | 11.23 | -3.42 | 14.649 | 130.5% |
| DeepSeek-V3 | GSM8K | 8.08 | -53.76 | 61.842 | 765.2% |
| Doubao-pro | GSM8K | 11.03 | 3.75 | 7.274 | 66.0% |
| Gemini-1.5 | GSM8K | -15.71 | -30.42 | 14.710 | 93.7% |
| Gemma-2B-it | GSM8K | 11.95 | 12.29 | -0.337 | -2.8% |
| Hunyuan-Turbo | GSM8K | -4.15 | -54.57 | 50.423 | 1215.9% |
| Mistral-7B-Instruct-v0.1 | GSM8K | 11.65 | 12.87 | -1.213 | -10.4% |
| Moonshot-v1 | GSM8K | 11.07 | 0.94 | 10.128 | 91.5% |
| Qwen-Plus | GSM8K | 12.95 | 4.94 | 8.012 | 61.9% |
| Qwen2.5-3B-Instruct | GSM8K | 13.89 | 12.36 | 1.529 | 11.0% |
| Vicuna-7B-v1.3 | GSM8K | 14.43 | 14.92 | -0.489 | -3.4% |
| Yi-Lightning | GSM8K | 12.22 | 6.23 | 5.996 | 49.1% |
| 360GPT2-Pro | HellaSwag | 33.58 | -3.30 | 36.874 | 109.8% |
| DeepSeek-V3 | HellaSwag | 7.90 | -333.34 | 341.244 | 4319.7% |
| Doubao-pro | HellaSwag | 15.92 | -26.33 | 42.249 | 265.4% |
| Gemini-1.5 | HellaSwag | -3.65 | -19.36 | 15.714 | 430.5% |
| Gemma-2B-it | HellaSwag | 25.43 | 26.88 | -1.448 | -5.7% |
| Hunyuan-Turbo | HellaSwag | 40.69 | 15.82 | 24.865 | 61.1% |
| Mistral-7B-Instruct-v0.1 | HellaSwag | 31.85 | 32.06 | -0.216 | -0.7% |
| Moonshot-v1 | HellaSwag | 39.63 | 28.44 | 11.190 | 28.2% |
| Qwen-Plus | HellaSwag | -18.42 | -68.81 | 50.391 | 273.5% |
| Qwen2.5-3B-Instruct | HellaSwag | 23.02 | 16.75 | 6.271 | 27.2% |
| Vicuna-7B-v1.3 | HellaSwag | 25.30 | 26.55 | -1.251 | -4.9% |
| Yi-Lightning | HellaSwag | 19.79 | -6.47 | 26.261 | 132.7% |
| 360GPT2-Pro | HumanEval | 2.24 | -4.59 | 6.822 | 305.1% |
| DeepSeek-V3 | HumanEval | 2.43 | -39.77 | 42.191 | 1739.2% |
| Doubao-pro | HumanEval | -0.58 | -9.01 | 8.439 | 1467.3% |
| Gemini-1.5 | HumanEval | -12.37 | -22.08 | 9.711 | 78.5% |
| Gemma-2B-it | HumanEval | 3.79 | 3.94 | -0.152 | -4.0% |
| Hunyuan-Turbo | HumanEval | 4.14 | 0.81 | 3.332 | 80.4% |
| Mistral-7B-Instruct-v0.1 | HumanEval | 5.03 | 5.43 | -0.401 | -8.0% |
| Moonshot-v1 | HumanEval | 4.66 | 1.11 | 3.548 | 76.2% |
| Qwen-Plus | HumanEval | 5.33 | 5.17 | 0.162 | 3.0% |
| Qwen2.5-3B-Instruct | HumanEval | 4.25 | 4.63 | -0.384 | -9.1% |
| Vicuna-7B-v1.3 | HumanEval | 5.00 | 5.15 | -0.152 | -3.0% |
| Yi-Lightning | HumanEval | 2.55 | 0.23 | 2.314 | 90.8% |
| 360GPT2-Pro | MMLU | 24.90 | -36.62 | 61.523 | 247.0% |
| DeepSeek-V3 | MMLU | 16.45 | -340.64 | 357.083 | 2171.3% |
| Doubao-pro | MMLU | -14.60 | -45.75 | 31.148 | 213.4% |
| Gemini-1.5 | MMLU | 34.75 | 63.69 | -28.942 | -83.3% |
| Gemma-2B-it | MMLU | 21.78 | 25.87 | -4.090 | -18.8% |
| Hunyuan-Turbo | MMLU | 12.14 | -82.39 | 94.533 | 778.7% |
| Mistral-7B-Instruct-v0.1 | MMLU | 32.89 | 35.29 | -2.401 | -7.3% |
| Moonshot-v1 | MMLU | 18.69 | -25.20 | 43.890 | 234.9% |
| Qwen-Plus | MMLU | 44.91 | 9.55 | 35.361 | 78.7% |
| Qwen2.5-3B-Instruct | MMLU | 20.27 | 8.60 | 11.674 | 57.6% |
| Vicuna-7B-v1.3 | MMLU | 29.97 | 32.87 | -2.903 | -9.7% |
| Yi-Lightning | MMLU | 48.15 | 21.92 | 26.224 | 54.5% |

## Figures

- **scatter_4pl_vs_3pl.png**: 4PL vs 3PL lz* scatter. Pearson r = 0.2250, RMSE = 68.41.
- **delta_distribution.png**: Grouped bar chart and histogram of Δlz* by model and benchmark.
- **d_vs_delta_relationship.png**: Benchmark mean d vs mean |Δlz*| with linear trend.

## Key Findings

1. **Most affected benchmark**: MMLU (mean |Δlz*| = 58.314), consistent with having the most items with d < 0.95 (46.1%).

2. **Least affected benchmark**: ARC-C (mean |Δlz*| = 5.983).

3. **Most affected model**: DeepSeek-V3 (mean |Δlz*| = 168.589).

4. **Direction of bias**: Mean Δlz* across all pairs = 24.900 (positive = 4PL gives higher lz* than 3PL). Without d-capping, 3PL overestimates expected performance for high-ability models, making their errors look catastrophically aberrant. This effect is strongest for DeepSeek-V3 (θ=3.77), where 3PL lz* drops to -340 on MMLU/HellaSwag.

5. **Overall correlation**: 4PL and 3PL lz* show weak correlation (r = 0.2250) with large RMSE = 68.41, driven primarily by high-ability models where d-capping has outsized impact. Low-ability models (Gemma-2B-it, Vicuna-7B, Mistral-7B) are barely affected (|Δlz*| < 2), confirming d only matters near the probability ceiling.

6. **Practical implication**: Using 3PL (ignoring d) would render lz* unusable for contamination detection in high-ability LLMs — the d-induced bias dwarfs any contamination signal. The 4PL d parameter is essential for valid person-fit analysis on LLM benchmark data.
