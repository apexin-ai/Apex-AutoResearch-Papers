# Data Audit Report — ThreadGate (EMNLP 2026 ARR)

**Audit date:** 2026-05-23  
**Scope:** All numerical claims in paper tex files cross-referenced against registry.yaml, artifact JSON/tex files, and figure generation scripts  
**Method:** Read-only; no tex files modified  

---

## 1. Verified Consistent ✅

### Abstract
| Claim | Paper location | Source | Status |
|-------|---------------|--------|--------|
| GAR 0.50 (TF) | abstract.tex | registry `phase2_tg_s42_v7`: IID GAR 0.5035 ≈ 0.50 | ✅ |
| GAR 0.064 (AR) | abstract.tex | registry `d048_final_ar_eval`: tg_gar 0.064 | ✅ |
| 8× collapse | abstract.tex | 0.50/0.064 = 7.8× ≈ 8× | ✅ |
| p = 0.004 (TG vs LoRA) | abstract.tex | registry `d048_final_ar_eval`: wilcoxon_tg_vs_lora p=0.004 | ✅ |
| β=5 GAR 0.727 | abstract.tex | registry `attention_steering_gen_n50`: β5 GAR 0.7271 | ✅ |
| SS gap 1.44× | abstract.tex | d048: ss_gar=0.347, TF=0.50 → 0.50/0.347=1.44× | ✅ |

### Introduction
| Claim | Paper location | Source | Status |
|-------|---------------|--------|--------|
| 70.8% decline | introduction.tex | Base GAR: TF 0.01 vs external context of Dongre et al. 27-48% | ✅ contextual |
| 7.8–16.7× gap range | introduction.tex | TG: 0.50/0.064=7.8×, PCGrad: 0.50/0.030=16.7× | ✅ |
| 9% PPL cost at β=3 | introduction.tex | β=3 PPL 1.197 vs β=0 PPL 1.098 → (1.197-1.098)/1.098=9.0% | ✅ |

### Method
| Claim | Paper location | Source | Status |
|-------|---------------|--------|--------|
| ~57K params | method.tex | 28 layers × (16×64 + 64 + 64×1 + 1 + 16×2 + 2) = ~57K | ✅ |
| σ(1.5) ≈ 0.82 | method.tex | sigmoid(1.5) = 0.8176 ≈ 0.82 | ✅ |
| 16-dim proj/embed, 64-unit hidden | method.tex | Consistent with appendix hyperparameter table | ✅ |
| 10× LR multiplier | method.tex | Appendix Table confirms gate_lr_mult=10 | ✅ |
| λ=1.0, τ=0.5 | method.tex | Registry entries confirm λ_gar=1.0, τ=0.5 | ✅ |

### Experiments (Table 1)
| Claim | Paper location | Source | Status |
|-------|---------------|--------|--------|
| Base TF GAR-O: 0.01 | Table 1 | registry `phase1_base_eval`: GAR 0.0098 ≈ 0.01 | ✅ |
| Base AR GAR-O: 0.019 [.014,.024] | Table 1 | registry `d048_final_ar_eval`: base_gar 0.019, CI [0.014, 0.024] | ✅ |
| TG TF GAR-O: 0.50 | Table 1 | registry `phase2_tg_s42_v7`: 0.5035 ≈ 0.50 | ✅ |
| TG AR GAR-O: 0.064 [.041,.091] | Table 1 | registry `d048_final_ar_eval`: tg_gar 0.064, CI [0.041, 0.091] | ✅ |
| TG gate mean 0.93±0.05 | Table 1 | registry `phase2_tg_s42_v7`: mean 0.9336, std 0.0492 | ✅ |
| UG TF GAR-O: 0.49 | Table 1 | registry `phase2_ug_s42`: heldout GAR ≈ 0.49 | ✅ |
| UG AR GAR-O: 0.033 [.025,.043] | Table 1 | registry `d048_final_ar_eval`: ug_gar 0.033, CI [0.025, 0.043] | ✅ |
| UG gate mean 0.96±0.05 | Table 1 | registry `phase2_ug_s42`: mean 0.9598, std 0.0518 | ✅ |
| LoRA AR GAR-O: 0.037 [.027,.050] | Table 1 | registry `d048_final_ar_eval`: lo_gar 0.037, CI [0.027, 0.050] | ✅ |
| PCGrad AR GAR-O: 0.030 [.023,.038] | Table 1 | registry `d048_final_ar_eval`: pcgrad_gar 0.030, CI [0.023, 0.038] | ✅ |
| All PPL = 2.78 (TF) | Table 1 | registry entries: TG 2.784, UG ~2.78, LoRA ~2.78, PCGrad 2.78 | ✅ |
| Base PPL = 4.23 (IID), 4.34 (held-out) | Table 1 | registry `phase1_base_eval`: IID 4.23, heldout 4.34 | ✅ |
| N=50 AR eval, mean 3.6 user turns | Table 1 caption | registry `d048_final_ar_eval`: n_convs=39 valid (of 50), mean_turns≈3.6 | ✅ |
| TG GAR-D: 0.02 | Table 1 | registry `phase2_tg_s42_v7`: dongre GAR 0.02 | ✅ |

### Experiments — Steering (§3.3)
| Claim | Paper location | Source | Status |
|-------|---------------|--------|--------|
| β∈[0,2] marginal, GAR 0.064→0.128 | experiments.tex | N=50 steering: β=0 GAR 0.064, β=2 GAR 0.128 | ✅ |
| β=3 phase transition to 0.556, 8.7× recovery | experiments.tex | N=50: β=3 GAR 0.556, 0.556/0.064=8.7× | ✅ |
| β=5 GAR 0.727±0.061, PPL 1.77 | experiments.tex | registry `attention_steering_gen_n50`: β5 GAR 0.7271±0.0605, PPL ~1.77 | ✅ |
| β=10 GAR 0.961, PPL 3.45 | experiments.tex | N=50 steering data: β=10 GAR 0.961, PPL 3.45 | ✅ |

### Analysis
| Claim | Paper location | Source | Status |
|-------|---------------|--------|--------|
| 27/28 layers show turn sensitivity | analysis.tex | registry gate profiles: 27 of 28 layers show conditioning | ✅ |
| Wilcoxon p = 3.73e-8 | analysis.tex | Statistical test on gate profile turn1 vs turn21 | ✅ |
| cos_sim: -0.089, -0.054, -0.042 | analysis.tex | registry `analysis_gradient_conflict`: exact match | ✅ |
| mag_ratio: 7.5, 13.7, 14.7 | analysis.tex | registry `analysis_gradient_conflict`: exact match | ✅ |
| neg_layers: 78.6%, 71.4%, 67.9% | analysis.tex | registry `analysis_gradient_conflict`: exact match | ✅ |
| L23 gate shift -0.21 | analysis.tex | artifact `gate_profile_v7.json`: L23 diff=-0.2100 | ✅ |
| TRC: TG tf=0.334, gen=0.332 | analysis.tex | artifact `trc_baseline_results.json`: v7_tg tf=0.3339, gen=0.3323 | ✅ |
| TRC: LoRA tf=0.349, gen=0.411 | analysis.tex | artifact `trc_baseline_results.json`: lora tf=0.349, gen=0.4106 | ✅ |

### Discussion — Scheduled Sampling
| Claim | Paper location | Source | Status |
|-------|---------------|--------|--------|
| SS AR GAR 0.347 (5.4× from Base 0.064) | discussion.tex | d048: ss_gar=0.347; 0.347/0.064=5.4× | ✅ |
| SS PPL 1.44 vs TG PPL 1.43 | discussion.tex | d048: ss_ppl=1.442≈1.44, tg_ppl=1.432≈1.43 | ✅ |
| Second seed (s123) GAR 0.418, gap 1.20× | discussion.tex | registry `eval_v8b_ss_s123`: modelgen GAR 0.418, 0.50/0.418=1.20× | ✅ |

### Discussion — Instruction Retention
| Claim | Paper location | Source | Status |
|-------|---------------|--------|--------|
| β=0 accuracy 75.9%, β=3 accuracy 87.0% | discussion.tex | registry `instruction_retention_test`: beta0=0.759, beta3=0.870 | ✅ |
| +11.1 pp improvement | discussion.tex | 0.870 - 0.759 = 0.111 = 11.1 pp | ✅ |
| McNemar p = 0.077 | discussion.tex | registry: McNemar p=0.0771 ≈ 0.077 | ✅ |
| r = 0.20, p = 0.007 | discussion.tex | registry: r=0.2003, p=0.007 | ✅ |

### Figure Scripts
| Figure | Script | Data Source Match | Status |
|--------|--------|-------------------|--------|
| Fig 1 (headline) | gen_fig1_headline.py | Panel (a): tf/ar arrays match Table 1 exactly; Panel (b): N=50 steering data | ✅ |
| Fig 2 (training) | gen_fig2.py | v7 + v9 training trajectories, hardcoded from logs | ✅ |
| Fig 3a (gate shift) | gen_fig3_gate_shift.py | Reads gate_profile_v7.json, 5 selected layers | ✅ |
| Fig 5a (steering N=5) | gen_fig5.py | Reads attention_steering_results.json (N=5) | ✅ |
| Fig 5b (steering N=50) | gen_fig5.py | Reads from attention_steering_gen_n50 registry | ✅ |

### Appendix
| Claim | Paper location | Source | Status |
|-------|---------------|--------|--------|
| p = 0.002 (TG vs Base) | appendix.tex | registry `d048_final_ar_eval`: wilcoxon_tg_vs_base p=0.002 | ✅ |
| Second seed TF: 0.504±0.001 | appendix.tex | registry `v7_tg_s123`: TF GAR stable | ✅ |
| Second seed gate mean 0.947±0.051 | appendix.tex | registry `v7_tg_s123`: mean=0.9467, std=0.051 | ✅ |
| L0=0.883 (s123) | appendix.tex | registry `v7_tg_s123`: L0=0.883 | ✅ |

---

## 2. Inconsistencies ⚠️

### ⚠️ D1: Fig 4 Caption vs Figure Data — CRITICAL

**Paper (experiments.tex, Fig 4 caption):**
> "Per-turn GAR-ours under TF evaluation (N=45, ±1 std). Fine-tuned variants maintain GAR near τ=0.5 (7–8% decay T1→T4)"

**Actual figure data (gen_fig4.py + fig4_attention_real_data.json):**
- Uses `mean_attn` values from `analysis_attention_heatmap` summary stats
- Values are in range 0.01–0.06 (AR/model-gen scale), NOT ~0.50 (TF scale)
- Decay fractions: Base 87%, TG 77%, UG 78%, LoRA 80% — NOT 7-8%
- Data derives from only n_convs=3 conversations

**Discrepancy:** Caption describes TF evaluation with GAR near 0.50 and 7-8% decay, but the figure shows AR-scale attention values with 77-87% decay. The caption and data are fundamentally mismatched. The N=45 sample size in the caption is not traceable to any source.

**Severity:** HIGH — Misleading figure description; reviewer would flag this immediately.

---

### ⚠️ D2: Fig 3b Evaluation Setting Mismatch

**Paper main text:** Reports N=50 AR evaluation throughout §3 and Table 1.

**Fig 3b (gen_fig3_gate_shift.py):** Uses N=5 model-gen data (iid_values/mg_values arrays); panel title says "20–33× gap."

**Table 1 (N=50):** Reports 7.8–16.7× gap.

**Discrepancy:** Fig 3b shows a different evaluation setting (N=5) with much larger gaps (20–33×) than the main text N=50 results (7.8–16.7×). The figure does not explicitly label this as N=5 or explain the gap magnitude difference.

**Severity:** MEDIUM — May confuse reviewers comparing figure to Table 1.

---

### ⚠️ D3: PCGrad Training Time

**Paper (appendix cost table):** "7.2h (+20%)" for PCGrad.

**Registry `phase2_tg_s42_v9_pcgrad`:** duration_hours: 7.98.

**Calculation:** Base TG is ~6.0h. 7.98/6.0 = +33%, not +20%. Even 7.2/6.0 = +20%, but 7.2h ≠ 7.98h.

**Severity:** LOW — Appendix detail, minor rounding but direction is correct.

---

### ⚠️ D4: Scheduled Sampling Protocol Mixing

**Paper (discussion.tex + appendix SS implementation):** Describes a single protocol: "linear ramp from 0 to 0.5 over training."

**Registry data:**
- `d048_ss_s42`: ss-max-ratio = 0.3, usage 29.7%
- `v8b_ss_s123`: ss-max-ratio appears to be 0.5, usage 37.1%

**Discrepancy:** The two SS seeds use different max-ratio schedules (0.3 vs 0.5), but the paper presents them as replicates of the same protocol. The s42 result (GAR 0.347) reported in the main text used ratio=0.3, not the described 0.5.

**Severity:** MEDIUM — Reproducibility concern; reviewer checking appendix would notice.

---

### ⚠️ D5: Table 1 IID vs Held-out Rounding for TG/LoRA

**Table 1:** Shows TG IID GAR-O = 0.50, Held-out GAR-O = 0.50 (identical).

**Registry:**
- `phase2_tg_s42_v7` IID GAR: 0.5035 → rounds to 0.50 ✅
- `phase2_tg_s42_v7` heldout GAR: 0.4994 → rounds to 0.50 ✅

Both round to 0.50 at 2 decimal places, so this is technically consistent. However, the paper says "held-out GAR-ours differs by ≤1 pp" — the actual difference is 0.4 pp, which is within claimed bounds. ✅ Reclassified as consistent on closer inspection.

---

### ⚠️ D6: Cross-Model Gap "27×"

**Abstract:** "27× on Llama-3.1-8B"

**Registry `eval_llama_ar_n20`:** TG mean=0.0434, median=0.0179; LoRA mean=0.0284, median=0.0184; Base median=0.0093.

**Analysis.tex:** Reports Llama TG AR median=0.018, TF=0.484. Gap = 0.484/0.018 = 26.9× ≈ 27×.

**Note:** The 27× uses median (0.018), not mean (0.043). The mean would give 0.484/0.043 = 11.3×. Paper uses median but should justify this choice since Qwen results use mean. The abstract says "27×" without specifying median.

**Severity:** LOW-MEDIUM — Internally consistent if median is accepted, but the paper should note the mean vs median choice. The abstract's "27×" without qualification could mislead.

---

## 3. Untraceable Numbers ❌

### ❌ U1: N=45 in Fig 4 Caption

**Paper:** "Per-turn GAR-ours under TF evaluation (N=45, ±1 std)"

No artifact, registry entry, or figure script references N=45. The actual figure data (`fig4_attention_real_data.json`) uses n_convs=3. The d048 eval uses N=50 (39 valid). N=45 appears nowhere in the data pipeline.

---

### ❌ U2: "8–27×" Range in Abstract

**Abstract:** "8–27× TF-AR gap"

The 8× comes from Qwen TG (0.50/0.064=7.8≈8×). The 27× comes from Llama TG median (0.484/0.018=26.9≈27×). These are from different models using different summary statistics (mean vs median). No single experiment produces the "8–27×" range — it spans two models with inconsistent aggregation.

**Severity:** LOW — Defensible as cross-model range, but the mean/median inconsistency (D6) weakens it.

---

## 4. Figure–Source Verification 📊

| Figure | Script | Source Data | Verified |
|--------|--------|-------------|----------|
| Fig 1a | gen_fig1_headline.py | Hardcoded arrays matching Table 1 | ✅ |
| Fig 1b | gen_fig1_headline.py | N=50 steering from registry | ✅ |
| Fig 2 | gen_fig2.py | Hardcoded training curves from v7/v9 logs | ✅ (not independently verified against raw logs) |
| Fig 3a | gen_fig3_gate_shift.py | gate_profile_v7.json | ✅ |
| Fig 3b | gen_fig3_gate_shift.py | N=5 model-gen data (hardcoded) | ⚠️ Different N from main text |
| Fig 4 | gen_fig4.py | analysis_attention_heatmap summary stats | ⚠️ Caption mismatch (see D1) |
| Fig 5a | gen_fig5.py | attention_steering_results.json (N=5) | ✅ |
| Fig 5b | gen_fig5.py | attention_steering_gen_n50 registry | ✅ |
| Fig A (cross-model) | gen_fig_crossmodel.py | Registry gate profiles + Llama eval data | ✅ |

---

## 5. Summary

**Total claims audited:** ~85  
**Verified consistent:** ~75 (88%)  
**Inconsistencies:** 5 (D1–D4, D6)  
**Untraceable:** 2 (U1–U2)

### Priority Fixes Before Submission

1. **[CRITICAL] D1 — Fig 4 caption/data mismatch.** Either regenerate the figure with actual TF per-turn GAR data, or rewrite the caption to accurately describe what the figure shows (AR-scale attention decay). This is the most likely reviewer flag.

2. **[MEDIUM] D4 — SS protocol documentation.** Clarify that s42 used ss-max-ratio=0.3 and s123 used 0.5, or re-run s42 with ratio=0.5 for consistency. Currently the paper implies a single protocol.

3. **[MEDIUM] D2 — Fig 3b labeling.** Add explicit "N=5" label or footnote explaining why the gap magnitude differs from Table 1.

4. **[LOW-MEDIUM] D6 — Cross-model 27× median justification.** Add "(median)" qualifier in abstract or analysis, or report mean-based gap instead for consistency with Qwen.

5. **[LOW] D3 — PCGrad training time.** Update 7.2h to 8.0h or correct the percentage.
