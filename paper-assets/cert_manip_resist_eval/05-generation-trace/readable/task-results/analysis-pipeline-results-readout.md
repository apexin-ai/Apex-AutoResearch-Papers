# analysis pipeline results readout

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pipeline-results-readout_20260522T170140_result.json`
- **Structured JSON:** [`345f2baa1cfd44069b87.json`](../../sessions/34/345f2baa1cfd44069b87.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部收集完毕。以下是汇总。

---

## 1. Confound Diagnosis

**Overall: mean r = +0.650, verdict = CONFOUND_BROKEN**

对比历史：6-model r=−0.8 → 7-model r=+0.47 → **15-model r=+0.65**

| Condition | Pearson r |
|-----------|-----------|
| mmlu×prompt_injection | +0.653 |
| mmlu×sycophancy | +0.158 |
| mmlu×score_manipulation | +0.899 |
| mmlu×verbosity_bias | +0.158 |
| mmlu×position_bias | +0.455 |
| mmlu×authority_bias | +0.516 |
| arc×prompt_injection | +0.887 |
| arc×sycophancy | +0.770 |
| arc×score_manipulation | +0.887 |
| arc×verbosity_bias | +0.781 |
| arc×position_bias | +0.890 |
| arc×authority_bias | +0.750 |

所有 12 条件 verdict 均为 CONFOUND_BROKEN。但注意 r 值翻正且多数 >0.7，K_eff 和 η_max 现在是**正相关**（更大模型 → 更高 manipulation susceptibility）。VIF 在 1.0–4.2 范围，回归可分离。

---

## 2. Step 4 Panel Regression — Claim 1

- **η_max FDR 显著：9/12** 条件
- **K_eff FDR 显著：4/12** 条件
- **K_eff 系数方向：10/12 正，2/12 负**

| Condition | K_eff β | K_eff p | K_eff FDR p | FDR sig? |
|-----------|---------|---------|-------------|----------|
| mmlu×prompt_injection | +2.317 | 0.00498 | **0.0260** | ✓ |
| mmlu×sycophancy | +1.778 | 0.0419 | 0.0837 | ✗ |
| mmlu×score_manipulation | +1.642 | 0.212 | 0.318 | ✗ |
| mmlu×verbosity_bias | +1.966 | 0.0249 | 0.0598 | ✗ |
| mmlu×position_bias | −0.064 | 0.345 | 0.414 | ✗ |
| mmlu×authority_bias | +1.251 | 0.112 | 0.191 | ✗ |
| arc×prompt_injection | +3.384 | 0.00108 | **0.0130** | ✓ |
| arc×sycophancy | −0.774 | 0.336 | 0.414 | ✗ |
| arc×score_manipulation | +2.707 | 0.00669 | **0.0260** | ✓ |
| arc×verbosity_bias | +0.644 | 0.619 | 0.675 | ✗ |
| arc×position_bias | +0.317 | 0.00866 | **0.0260** | ✓ |
| arc×authority_bias | +0.211 | 0.773 | 0.773 | ✗ |

**K_eff 系数为正** = 更多有效组件 → ASR 更高（与 Claim 1 预期方向相反，Claim 1 期望 K_eff 负即多样性保护）。

---

## 3. Step 5 Random Fault — Claim 2

- **RF 模型下 K_eff 显著：12/12** 条件（`keff_gains_significance_count: 12/12`）
- **Adaptive 模型下 K_eff 显著（raw p<0.05）：6/12；FDR<0.05：4/12**
- **K_eff sig negative：0/12**（adaptive 和 RF 均无显著负系数）
- **Mean ΔR²（RF − adaptive）= +0.274**
- 解读：RF 模型解释力更强，K_eff 在 RF 下全面显著但方向为正——diversity benefit 被 adaptive attack 削弱但 K_eff 并非保护因子（系数正表示更多有效组件反而提高 ASR）

---

## 4. Sensitivity Analysis

`sensitivity_exclude_low_acc` 字段存在。排除 clean ACC < 0.5 后：

- 6 个 arc_challenge 条件：84 → **56 panels**（excluded_low_acc=91）
- 6 个 mmlu 条件：n_panels 不变（84），但 FDR 校正因 arc 条件变化而改变

**K_eff FDR 显著：4/12 → 0/12**

关键变化：
- mmlu×prompt_injection FDR: 0.026 → 0.060 ✗
- arc×prompt_injection FDR: 0.013 → 0.206 ✗
- arc×score_manipulation FDR: 0.026 → 0.356 ✗
- arc×position_bias FDR: 0.026 → 0.863 ✗

**结论：K_eff 显著性极度脆弱，排除低 ACC 模型后完全消失。**

---

## 5. MI Matrix 数据质量

**Gemini valid samples（MMLU clean 条件）：**
- gemini-2.5-pro: **265/300** valid（35 errors, 11.7%）
- gemini-2.5-flash: **221/300** valid（79 errors, 26.3%）

两者均 > 150，无低样本量 warning。但 gemini-2.5-flash 错误率较高。

**MI 矩阵零值问题：** 6/15 模型 MI 全为 0（claude-opus-4, gemini-2.5-pro, claude-sonnet-4, gpt-4o, gemini-2.5-flash, gpt-4o-mini），无法计算 token-level MI。9/15 模型有有效 MI 数据。MI 矩阵 JSON 无 metadata/warning 字段。

---
