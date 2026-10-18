# code fix loader rerun pipeline

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-loader-rerun-pipeline_20260522T170513_result.json`
- **Structured JSON:** [`ec41d0d4d9f7148cd292.json`](../../sessions/ec/ec41d0d4d9f7148cd292.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据齐全。以下是 5 维结构化汇报：

---

## Pipeline 15-model 结果 (v2)

### 4a. Confound Diagnosis

| Condition | Pearson r | p-value |
|-----------|-----------|---------|
| mmlu×prompt_injection | +0.656 | 2.3e-57 |
| mmlu×sycophancy | +0.348 | 2.2e-14 |
| mmlu×score_manipulation | +0.820 | 7.1e-112 |
| mmlu×verbosity_bias | +0.355 | 6.0e-15 |
| mmlu×position_bias | +0.633 | 2.3e-52 |
| mmlu×authority_bias | +0.595 | 6.9e-45 |
| arc×prompt_injection | +0.888 | 4.7e-155 |
| arc×sycophancy | +0.764 | 2.3e-88 |
| arc×score_manipulation | +0.908 | 6.2e-173 |
| arc×verbosity_bias | +0.790 | 2.0e-98 |
| arc×position_bias | +0.916 | 4.8e-182 |
| arc×authority_bias | +0.732 | 1.2e-77 |

**Mean r = +0.700**。所有 12 条件 verdict = CONFOUND_BROKEN。K_eff 与 η_max 从 6-model 的 r=-0.8 翻转为 15-model 的 r=+0.70，confound 成功打破。

### 4b. Step 4 Regression — Claim 1

**K_eff: 12/12 条件 FDR 显著（全部正系数）。**

| Condition | K_eff β | K_eff p | K_eff FDR p | η_max FDR p |
|-----------|---------|---------|-------------|-------------|
| mmlu×prompt_inj | +7.585 | 9.9e-28 | 1.2e-26 | 4.6e-07 |
| mmlu×sycophancy | +5.573 | 9.9e-27 | 6.0e-26 | 3.6e-11 |
| mmlu×score_manip | +8.087 | 1.7e-26 | 6.8e-26 | 3.4e-01 NS |
| mmlu×verbosity | +4.243 | 1.8e-16 | 4.2e-16 | 4.8e-23 |
| mmlu×position | +0.198 | 8.8e-13 | 1.5e-12 | 1.3e-05 |
| mmlu×authority | +5.071 | 3.5e-21 | 1.1e-20 | 4.5e-03 |
| arc×prompt_inj | +4.969 | 8.5e-14 | 1.7e-13 | 5.0e-04 |
| arc×sycophancy | +1.087 | 1.8e-02 | 1.8e-02 | 1.6e-14 |
| arc×score_manip | +4.737 | 3.3e-11 | 5.0e-11 | 2.6e-01 NS |
| arc×verbosity | +3.753 | 3.7e-10 | 4.5e-10 | 7.0e-06 |
| arc×position | +0.251 | 1.4e-10 | 1.8e-10 | 4.5e-01 NS |
| arc×authority | +2.452 | 9.7e-08 | 1.1e-07 | 7.5e-07 |

**η_max: 9/12 FDR 显著**（score_manipulation 两个 dataset 和 arc×position_bias 不显著）。系数方向一致为正。

### 4c. Step 5 Random Fault — Claim 2

- **RF 下 K_eff: 12/12 条件显著**（全部 p < 1e-9）
- **Adaptive 下 K_eff: 12/12 条件显著**
- **K_eff gains significance: 11/12**（唯一例外：mmlu×verbosity_bias）
- **Mean ΔR² = +0.213**（RF 模型解释方差更高）
- 最大 ΔR²: arc×position_bias (+0.588)，mmlu×position_bias (+0.465)

### 4d. Sensitivity Analysis (排除 clean ACC < 0.5)

- **mmlu 6 条件**：无排除（0 excluded），结果与主分析完全一致
- **arc_challenge 6 条件**：排除 91 panels（455→364），5/6 K_eff FDR 显著
  - 唯一变化：**arc×sycophancy K_eff 从 p=0.018 变为 p=0.175（不显著）**
  - 其余 5 条件均保持显著
- 结论总体稳健，仅 arc×sycophancy 在 sensitivity 下失去显著性

### 4e. MI Matrix 数据质量

- **Gemini 模型 valid sample count 充足，无低样本量 warning**
  - gemini-3.1-pro-preview: mmlu 213–265, arc 277–297
  - gemini-3.5-flash: mmlu 213–221, arc 277
  - 均远超 150 的最低阈值
- 所有 15 个模型全部进入 MI 矩阵，warnings = []

---
