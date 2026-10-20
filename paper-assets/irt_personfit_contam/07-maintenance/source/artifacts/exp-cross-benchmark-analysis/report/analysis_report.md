# Cross-Benchmark lz* Analysis Report

## 1. Overview

This analysis examines the person-fit statistic lz* across 12 LLMs and 5 benchmarks (MMLU, ARC-C, HellaSwag, GSM8K, HumanEval). Of 60 model–benchmark cells, 57 are flagged as anomalous (BH-adjusted p < 0.05).

## 2. lz* Magnitude Patterns

**Benchmark severity ranking** (mean |lz*| across models):

- MMLU: 26.1
- HellaSwag: 18.9
- GSM8K: 7.9
- ARC-C: 3.3
- HumanEval: 2.9

**Model severity ranking** (mean |lz*| across benchmarks):

- Mistral-7B-Instruct-v0.1: 17.6
- Vicuna-7B-v1.3: 14.1
- Gemma-2B-it: 13.7
- Yi-Lightning: 12.6
- Qwen2.5-3B-Instruct: 12.6
- Gemini-1.5: 12.0
- Qwen-Plus: 11.4
- Hunyuan-Turbo: 10.0
- Moonshot-v1: 9.6
- 360GPT2-Pro: 9.5
- Doubao-pro: 9.3
- DeepSeek-V3: 9.3

The most anomalous model overall is **Mistral-7B-Instruct-v0.1** (mean |lz*| = 17.6). MMLU and HellaSwag exhibit the highest lz* magnitudes across all models, suggesting that these large-scale MCQ benchmarks are most susceptible to response pattern anomalies.

## 3. Anomaly Profiles

**10/12** models are flagged on all 5 benchmarks. Only 360GPT2-Pro, Yi-Lightning escape full flagging.

- **360GPT2-Pro**: 4/5 flagged (positive) — arc_c; gsm8k; hellaswag; mmlu
- **DeepSeek-V3**: 5/5 flagged (positive)
- **Doubao-pro**: 5/5 flagged (mixed)
- **Gemini-1.5**: 5/5 flagged (mixed)
- **Gemma-2B-it**: 5/5 flagged (positive)
- **Hunyuan-Turbo**: 5/5 flagged (positive)
- **Mistral-7B-Instruct-v0.1**: 5/5 flagged (positive)
- **Moonshot-v1**: 5/5 flagged (positive)
- **Qwen-Plus**: 5/5 flagged (positive)
- **Qwen2.5-3B-Instruct**: 5/5 flagged (positive)
- **Vicuna-7B-v1.3**: 5/5 flagged (positive)
- **Yi-Lightning**: 3/5 flagged (positive) — gsm8k; hellaswag; mmlu

## 4. Cross-Benchmark Correlations

**Highly correlated benchmark pairs** (ρ > 0.6, p < 0.05):

- GSM8K–HumanEval: ρ = 0.790 (p = 0.0022)
- ARC-C–GSM8K: ρ = 0.776 (p = 0.0030)
- ARC-C–HumanEval: ρ = 0.720 (p = 0.0082)
- ARC-C–HellaSwag: ρ = 0.664 (p = 0.0185)
- HellaSwag–HumanEval: ρ = 0.615 (p = 0.0332)
- HellaSwag–GSM8K: ρ = 0.608 (p = 0.0358)

High correlations suggest shared contamination patterns — models that show anomalous behavior on one benchmark in a correlated pair tend to show similar anomalies on the other.

**Weakly correlated pairs** (|ρ| < 0.3):

- MMLU–ARC-C: ρ = -0.182 (p = 0.5717)
- MMLU–HellaSwag: ρ = -0.014 (p = 0.9656)
- MMLU–GSM8K: ρ = 0.119 (p = 0.7129)
- MMLU–HumanEval: ρ = 0.014 (p = 0.9656)

Weak correlations indicate benchmark-specific behavior — misfit on one benchmark does not predict misfit on the other.

## 5. Benchmark Type Grouping

### MCQ (MMLU, ARC-C, HellaSwag)

- Mean lz*: 14.06 (mean |lz*|: 16.10)
- Direction: 34 positive / 2 negative cells
- Flag rate: 97.2% (35/36)

### Math (GSM8K)

- Mean lz*: 6.57 (mean |lz*|: 7.87)
- Direction: 11 positive / 1 negative cells
- Flag rate: 100.0% (12/12)

### Code (HumanEval)

- Mean lz*: 2.39 (mean |lz*|: 2.91)
- Direction: 11 positive / 1 negative cells
- Flag rate: 83.3% (10/12)

MCQ benchmarks show the highest absolute lz* values, likely due to their large item pools amplifying the person-fit signal. GSM8K shows uniformly positive lz* except for Gemini-1.5, while HumanEval has the lowest magnitudes, consistent with code generation tasks being harder to contaminate via memorization.

## 6. Model Clustering

- **Cluster 1**: 360GPT2-Pro, DeepSeek-V3, Gemma-2B-it, Hunyuan-Turbo, Mistral-7B-Instruct-v0.1, Moonshot-v1, Qwen-Plus, Qwen2.5-3B-Instruct, Vicuna-7B-v1.3, Yi-Lightning
- **Cluster 2**: Gemini-1.5
- **Cluster 3**: Doubao-pro

**Gemini-1.5 forms a singleton cluster**, distinguished by its unique pattern of negative lz* on GSM8K, HellaSwag, and HumanEval. This aberrant (under-fitting) profile contrasts sharply with all other models' over-consistent patterns, suggesting a fundamentally different response mechanism.

## 7. lz* Direction Analysis

Of 60 cells, **56 (93.3%)** are positive (over-consistent) and **4** are negative (aberrant).

**Benchmark-level patterns:**

- MMLU: 11 positive / 1 negative
- ARC-C: 12 positive / 0 negative ← all positive
- HellaSwag: 11 positive / 1 negative
- GSM8K: 11 positive / 1 negative
- HumanEval: 11 positive / 1 negative

**Key finding:** The overwhelming majority of cells are positive, indicating over-consistent response patterns (a hallmark of benchmark contamination). Negative lz* values are concentrated in specific model–benchmark combinations:

- **Doubao-pro**: 1 negative cell(s) — mostly_positive
- **Gemini-1.5**: 3 negative cell(s) — mostly_negative

## 8. Implications for Contamination Detection

The cross-benchmark analysis reveals three key patterns:

1. **Pervasive over-consistency**: 95% of cells are flagged, and the vast majority show positive lz*, consistent with widespread benchmark contamination across the LLM ecosystem.

2. **Benchmark sensitivity hierarchy**: MMLU and HellaSwag produce the strongest signals (highest |lz*|), while HumanEval produces the weakest. This aligns with the hypothesis that MCQ benchmarks with large, publicly available item pools are most vulnerable.

3. **Gemini-1.5 anomaly**: The unique negative lz* pattern on GSM8K, HellaSwag, and HumanEval suggests a qualitatively different response mechanism — possibly reflecting post-training calibration, chain-of-thought reasoning patterns, or deliberate contamination mitigation.
