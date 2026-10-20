# analysis phase2 math 8model verify and clean permutation

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase2_math_8model_verify_and_clean_permutation_20260521T234320_result.json`
- **Structured JSON:** [`30f608f1eff7e6652bd5.json`](../../sessions/30/30f608f1eff7e6652bd5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Part A: MATH 8-model Henderson I

| 指标 | 值 |
|------|------|
| 数据 | 8 models × 57,600 = 460,800 records |
| item_id% | **24.03%** [95% CI: 20.73%, 27.17%] |
| G_item | **0.888** |
| model:item_id% | 17.28% |
| model% | 8.51% |
| residual% | 43.88% |
| grand mean accuracy | 0.2858 |

**与 7-model 对比**: 26.48% → 24.03% (**-2.45pp**)。加入 DeepSeek 后 item_id% 略降，但在 bootstrap CI 范围内，变化不显著。

### Part B: Clean MC vs FF Permutation Test

| 指标 | 值 |
|------|------|
| MC benchmarks | MMLU (37.88%), ARC (37.88%), HellaSwag (34.27%) |
| FF benchmarks | GSM8K (16.86%), MATH (24.03%) |
| MC mean | **36.68%** |
| FF mean | **20.45%** |
| Difference | **16.23pp** |
| p-value (one-sided) | **0.10** (1/10, exhaustive) |
| Cohen's d | **1.73** [95% CI: 1.72, 1.83] |
| Diff 95% CI | [11.44, 21.02]pp |

观测到的 MC-FF 差异（16.23pp）是所有 C(5,3)=10 种排列中最大的。p=0.10 是 n=5 时理论最小 p 值，描述的是 **format-conditional variance structure**（MC 格式的 item_id% 系统性高于 FF 格式），而非传统统计显著性。Cohen's d=1.73 表明效应量很大。

JSON 已保存至 `results/exp004_8model_analysis/math_8model_verified.json` 和 `clean_permutation_test.json`。

---
