# TF→AR Switching Experiment Analysis

**Experiment**: phase2_tf_ar_switching  
**Date**: 2026-05-26  
**Checkpoint**: Qwen-2.5-7B-Instruct + ThreadGate v7 s42 (epoch_2)  
**Data**: eval_200.json, N=39 conversations (≥3 assistant turns)  
**Runtime**: 1059s on westd-20861

---

## 1. Metric Clarification

This experiment measures **raw mid-point GAR** — the attention weight (averaged across all layers and heads) that a single mid-point token of each assistant turn places on goal (turn-boundary) positions. This is NOT the same as the **normalized GAR (nGAR)** used in the paper:

| Metric | TF baseline | AR baseline (β=0) | Source |
|--------|------------|-------------------|--------|
| nGAR (paper) | ~0.50 | ~0.064 | d048_final_ar_eval |
| Raw mid-point GAR (this exp) | 0.010–0.101 | 0.014–0.118 | switching experiment |

The raw mid-point GAR and nGAR differ by ~1-2 orders of magnitude because nGAR normalizes by expected random attention and aggregates over many query positions, while this experiment queries only a single token per turn.

---

## 2. Per-Turn GAR Summary

| Condition | turn_1 | turn_2 | turn_3 | turn_4 | turn_5 | turn_6 | turn_7 |
|-----------|--------|--------|--------|--------|--------|--------|--------|
| **pure_tf** | 0.1015 | 0.0447 | 0.0253 | 0.0206 | 0.0148 | 0.0122 | 0.0112 |
| **pure_ar** | 0.1179 | 0.0487 | 0.0357 | 0.0240 | 0.0167 | 0.0140 | 0.0309 |
| **switch_k1** | 0.1014 | **0.0387** | 0.0311 | 0.0264 | 0.0140 | 0.0124 | 0.0192 |
| **switch_k2** | 0.1015 | 0.0446 | **0.0265** | 0.0221 | 0.0132 | 0.0150 | 0.0143 |
| **switch_k3** | 0.1014 | 0.0448 | 0.0254 | **0.0218** | 0.0135 | 0.0112 | 0.0116 |
| **switch_k4** | 0.1015 | 0.0447 | 0.0254 | 0.0206 | **0.0147** | 0.0164 | 0.0104 |
| **switch_k5** | 0.1015 | 0.0447 | 0.0254 | 0.0206 | 0.0148 | **0.0213** | 0.0140 |

Sample sizes: turn_1–3: n=39, turn_4: n=22–23, turn_5: n=8, turn_6: n=7, turn_7: n=4

Bold = first AR turn after switch point.

---

## 3. Key Observations

### 3.1 Pre-switch turns perfectly match pure_tf

All pre-switch turns are within 0.0001 of pure_tf (e.g., switch_k3 turn_1=0.1014 vs pure_tf=0.1015). This validates the experimental control: gold context up to turn k produces identical attention patterns regardless of what happens later.

### 3.2 TF-AR gap is minimal in this metric

| Turn | pure_tf | pure_ar | Δ(AR−TF) | %diff | SE(diff)* | t-stat |
|------|---------|---------|----------|-------|-----------|--------|
| 1 | 0.1015 | 0.1179 | +0.016 | +16% | 0.0197 | 0.83 |
| 2 | 0.0447 | 0.0487 | +0.004 | +9% | 0.0084 | 0.48 |
| 3 | 0.0253 | 0.0357 | +0.010 | +41% | 0.0047 | **2.21** |
| 4 | 0.0206 | 0.0240 | +0.003 | +16% | 0.0045 | 0.75 |
| 5 | 0.0148 | 0.0167 | +0.002 | +13% | 0.0038 | 0.50 |
| 6 | 0.0122 | 0.0140 | +0.002 | +15% | 0.0025 | 0.72 |
| 7 | 0.0112 | 0.0309 | +0.020 | +176% | 0.0130 | 1.52 |

*SE pooled from std/√n. Only turn 3 approaches marginal significance (t=2.21, p≈0.03). Turn 7's large gap is unreliable (n=4).

**Critical issue**: pure_ar GAR is *higher* than pure_tf for all turns, opposite to the expected direction (paper shows nGAR_TF >> nGAR_AR). This means the raw mid-point GAR metric does not capture the same signal as nGAR.

### 3.3 Post-switch does not consistently converge to pure_ar

| Switch | 1st AR turn | switch value | pure_tf | pure_ar | Position* |
|--------|-------------|-------------|---------|---------|-----------|
| k1 | turn_2 | 0.0387 | 0.0447 | 0.0487 | −1.50 |
| k2 | turn_3 | 0.0265 | 0.0253 | 0.0357 | 0.12 |
| k3 | turn_4 | 0.0218 | 0.0206 | 0.0240 | 0.35 |
| k4 | turn_5 | 0.0147 | 0.0148 | 0.0167 | −0.05 |
| k5 | turn_6 | 0.0213 | 0.0122 | 0.0140 | 5.06 |

*Position = (switch − pure_tf) / (pure_ar − pure_tf). 0=matches TF, 1=matches AR.

Results are wildly inconsistent: positions range from −1.5 to +5.06. No clear pattern of abrupt or gradual convergence.

### 3.4 Variance is overwhelming

Per-conversation coefficients of variation (CV):
- pure_tf turn_1: CV = 0.090/0.101 = **89%**
- pure_tf turn_2: CV = 0.045/0.045 = **100%**
- pure_ar turn_1: CV = 0.083/0.118 = **71%**

Individual conversations show extreme outliers (e.g., one conversation has turn_1 GAR = 0.374, another has 0.032). The between-condition differences (~0.01) are completely swamped by within-condition variance (~0.05–0.09).

---

## 4. Hypothesis Verdict: **INCONCLUSIVE**

**Hypothesis**: TF→AR switching produces abrupt GAR drop (confirming instantaneous distribution shift).

**Verdict**: Cannot be tested with this metric. The experiment is underpowered for three reasons:

1. **Metric mismatch**: Raw mid-point GAR (single-token query) does not reproduce the TF-AR contrast seen in normalized GAR. The pure_tf vs pure_ar gap is <1 SE for most turns, providing no baseline contrast to detect switching effects.

2. **High variance**: CV of 71–100% means the signal (TF-AR diff of ~0.01) is buried in noise (per-conversation std of ~0.05–0.09).

3. **Small N for late turns**: Turns 5–7 have only n=4–8 conversations, insufficient for any statistical inference.

**What IS validated**: Pre-switch turns perfectly replicate pure_tf, confirming that the experimental design is sound. The issue is sensitivity, not methodology.

---

## 5. Implications for Paper Claim C3 (Exposure Bias Causation)

| Evidence type | Status | Notes |
|---------------|--------|-------|
| SS gap reduction (31×→1.3×) | **Strong** | d048_eval_ss multi-seed, p<0.001 |
| SS cross-model (Llama) | **Moderate** | p1_llama_ss shows similar reduction |
| Switching experiment | **Inconclusive** | This experiment; wrong metric for the analysis |

**Recommendation**: Do NOT include this switching analysis in the paper as evidence for C3. The raw mid-point GAR metric is mismatched. If a switching experiment is desired for the paper, it should be re-run using the same nGAR metric (with full query-position aggregation and normalization) used in the main evaluations.

Alternatively, the experiment could be re-framed as a **PPL-based switching test**: measure per-turn perplexity under TF→AR switching, which might show a clearer signal since PPL captures generation quality more directly.

---

## 6. File Locations

| Item | Path |
|------|------|
| Log | `~/runs/turn_residual_gating/phase2_tf_ar_switching.log` |
| Summary JSON | `/root/turn_residual_gating/results/switching_tg_s42_v7/switching_results.json` |
| Detail JSON | `/root/turn_residual_gating/results/switching_tg_s42_v7/switching_detail.json` |
| Checkpoint | `/root/turn_residual_gating/runs/phase2_tg_s42_v7/epoch_2` |
| Script | `/root/turn_residual_gating/src/eval_switching.py` |
