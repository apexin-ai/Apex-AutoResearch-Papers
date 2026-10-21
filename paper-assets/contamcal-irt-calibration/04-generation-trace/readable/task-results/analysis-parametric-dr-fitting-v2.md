# analysis parametric dr fitting v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_parametric-dr-fitting-v2_20260521T162436_result.json`
- **Structured JSON:** [`bbfe54aba40de1d30c36.json`](../../sessions/bb/bbfe54aba40de1d30c36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Plot 在服务器 `/root/contamcal-irt-calibration/artifacts/parametric_dr_fitting/dr_model_selection_fits.{png,pdf}`。

## AICc Model Selection Summary

| Family | Constant | Linear | Quadratic | Hill | Best → Classification | Alg1 | Match |
|--------|----------|--------|-----------|------|-----------------------|------|-------|
| **Phi-4** | w=0.008 | w=0.304 | w=0.112 | **w=0.575** | Hill → **Benefit** | Immune | N |
| **Qwen-14B** | w=0.000 | w=0.307 | w=0.142 | **w=0.551** | Hill → **Collapse** | Collapse | **Y** |
| **Qwen-7B** | w=0.159 | w=0.041 | w=0.031 | **w=0.768** | Hill → **Collapse** | V-recovery | N |
| **Gemma-2** | **w=0.386** | w=0.312 | w=0.187 | w=0.115 | Constant → **Immune** | Benefit | N |
| **OLMo-2** | **w=0.620** | w=0.126 | w=0.015 | w=0.239 | Constant → **Immune** | Benefit | N |

**Strict consistency: 1/5. Parsimony (dAICc<2) consistency: 1/5.**

## Best Model Parameters (95% CI)

| Family | Model | Key Params | 95% CI |
|--------|-------|------------|--------|
| Phi-4 | Hill | Emax=+2.43, EC50=1.00 | Emax=[-2.01, 6.88] (crosses 0) |
| Qwen-14B | Hill | Emax=−43.19, EC50=1.71 | Emax=[-119.9, 33.5] (wide, but direction clear) |
| Qwen-7B | Hill | Emax=−1.65, EC50=0.001 | Emax=[-2.42, -0.89] (significant, step-function decline) |
| Gemma-2 | Constant | c=65.25 | c=[64.32, 66.19] |
| OLMo-2 | Constant | c=55.93 | c=[55.54, 56.32] |

## Discrepancy Analysis

1. **Phi-4** (AICc: Benefit, Alg1: Immune): +1.17pp increase across full dose range. Hill beats Constant (dAICc=8.5), but Emax CI crosses 0. Effect is statistically detectable but practically marginal — Alg1's "Immune" label uses an implicit effect-size threshold.

2. **Qwen-7B** (AICc: Collapse, Alg1: V-recovery): Hill fits a rapid step-down (EC50≈0, Emax=−1.65) — essentially "any contamination causes −1.65pp, then flat." Quadratic (which captures V-shape) has dAICc=6.4 — AICc strongly penalizes the extra parameter. The V-recovery in mean trajectory (64.29→65.40) is not statistically separable from noise given cross-seed variance.

3. **Gemma-2/OLMo-2** (AICc: Immune, Alg1: Benefit): No model outperforms Constant. Linear slopes are 1.94 and 0.07 with CIs crossing 0. Algorithm 1's "Benefit" classification is not supported by formal model selection.

## 产出文件

- 服务器: `/root/contamcal-irt-calibration/artifacts/parametric_dr_fitting/` (CSV, JSON, PDF, PNG)
- 脚本: `/root/contamcal-irt-calibration/scripts/parametric_dr_model_selection.py`
- 已注册: `aic_model_selection_summary.csv` (art_20260521_7181a2)

---
