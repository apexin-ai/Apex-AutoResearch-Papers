# Paper Framing — contrastive_trace_safety

## Target Venue
- Primary: EMNLP 2026 Main (LLM Security Track)
- Deadline: ARR submission May 25, 2026

## Core Claims (D031: layer selection as primary contribution, 4 models)

**Contribution structure (D031)**:
- **Primary (methodological)**: Layer selection metric sensitivity — biased metrics reverse conclusions
- **Secondary (empirical)**: HS advantage at correct layers, qualified by scale; temporal improvement universal
- **Tertiary (negative results)**: 6 alternative methods fail, establishing what doesn't work

1. **Temporal context universally improves probe accuracy across both modalities** (D014 + D023 nuanced) — Temporal context is the most robust improvement across all 4 models and both modalities. Text probes benefit consistently from larger windows across all models. HS probes benefit in 3/4 models; OT-7B HS peaks at W=3 and declines at larger W (confirmed on both layer 0 and layer 16).

   **HS temporal gains** (W=1→best, 3 original models): accuracy +3pp (77.8%→81.0%), precision +13pp (69.3%→82.2%), FPR halved (9.65%→4.83%).
   **OT-7B HS temporal** (layer 16): bal_acc peaks at W=3 (68.8%), declines to 65.9% at W=25 (-2.9pp). BUT precision and FPR continue improving (prec 42.8%→49.4%, FPR 12.0%→7.5%). Temporal saturation is bal_acc-specific; larger W trades bal_acc for better precision/FPR. Confirmed on both layer 0 and layer 16 — genuine OT-7B characteristic.
   **Text temporal gains** (all 4 models, W=1→best): universally +3-12pp bal_acc, +8-23pp precision, FPR reduced.

   **IMPORTANT: coverage direction depends on detection criterion K.** K=1 (single crossing): coverage DECREASES with W. K=5 (consecutive crossings): coverage may INCREASE with W. Claim 1 is about accuracy/precision improvement, NOT coverage.

   The core insight: "Temporal context universally improves text probes across all 4 models. For HS probes, 3/4 models benefit from larger temporal windows, while OT-7B shows early saturation (W=3 peak)."

2. **HS probes outperform text probes at correctly selected layers, with strong evidence at 7-8B and model-specific patterns at 32B** (D031: qualified from D030 "universal") —

   **KEY FINDING (D029)**: The apparent "scale-dependent" HS advantage (significant at 7-8B, absent at 32B) was an artifact of the layer selection metric `bal_acc × crossing_rate`, which systematically selects shallow layers for 32B models. At correctly selected deep layers, HS outperforms text on all 4 models, but the NATURE of the advantage differs by scale.

   **Layer selection metric bias (D028, refined D036)**: `bal_acc × crossing_rate` selects shallow layers because shallow layers have higher crossing rates (more trigger-happy probes). 3/4 non-biased threshold-dependent metrics (precision, pre_cp_fpr, composite) converge on deep layers; pure bal_acc (threshold-free) selects middle layers (L30/L47). Deployment-relevant metric consensus selects L60/L63 for 32B models.

   **7-8B models: HS significantly outperforms text (2/2 models) — UNCHANGED**

   **R1-8B (Llama-8B, R1-distilled, n=43):**
   - Precision: 69.7% vs 47.2% (+22.4pp, p<0.001, **Holm-Bonferroni ✅**)
   - Accuracy: 81.3% vs 72.9% (+8.2pp, p=0.005, **Holm-Bonferroni ✅**)
   - Pre-CP FPR: 14.8% vs 22.2% (-7.4pp, p=0.044, **Holm-Bonferroni ✅** — rank 12/12, threshold=0.0500)

   **OT-7B (Qwen-7B, STILL-trained, n=47, layer 16, matched W=3) — D026 M001 corrected:**
   - Bal Acc: 68.8% vs 58.1% (+10.7pp, p<0.001, **Holm-Bonferroni ✅**)
   - Precision: 46.6% vs 24.7% (+21.9pp, p<0.001, **Holm-Bonferroni ✅**)
   - Pre-CP FPR: 10.0% vs 27.1% (-17.1pp, p<0.001, **Holm-Bonferroni ✅**)
   - **3/3 metrics significant — OT-7B cleanest single-model evidence**

   **32B models: HS outperforms text at CORRECTED LAYERS but with model-specific caveats (D029+D031)**

   **QwQ-32B (Qwen-32B, native, n=19-20, Layer 60 corrected from L2):**
   - Bal Acc: +11-22pp across all 15 window sizes, all p<0.005 (bootstrap, null-centered)
   - 15/15 W values show significant HS advantage
   - **CRITICAL CAVEAT (D031)**: HS lead time NEGATIVE (-1.2 to 1.9 steps vs text 3.7-12.3). HS is "more accurate but detects later." Position baseline bal_acc=0.746 > HS=0.740. In safety deployment, detecting 8-12 steps earlier may outweigh higher accuracy.
   - W=3: bal_acc +15.4pp, precision +23.6pp, FPR -9.8pp — **3/3 Holm-Bonferroni ✅**

   **R1-32B (Qwen-32B, R1-distilled, n=20, Layer 63 corrected from L10):**
   - W=1: bal_acc +18.7pp (0.826 vs 0.639), p=0.000; precision +15.4pp (0.603 vs 0.448), p=0.000; FPR -14.6pp (0.235 vs 0.380), p=0.007 — **3/3 Bonferroni ✅**
   - W=3: bal_acc +11.2pp p=0.020, precision p=0.032, FPR p=0.077 — **0/3 Bonferroni** (v2 null-centered)
   - W=5-15: all NS
   - **CRITICAL CAVEAT (D031)**: Only W=1 passes Bonferroni, coverage=25% (5/20 traces). Evidence statistically narrow.
   - **POSITIVE**: Lead time +11.7-13.3 steps (excellent early warning). HS >> Position (+14.2pp).
   - **NOTE**: L10 vs L63 at W=10: L10=0.795 vs L63=0.754 — L10 slightly better. "Scheme B选错层" narrative weaker for R1-32B.
   - ✅ P-VALUE UNIFIED: null-centered two-sided, consistent with QwQ.

   **32B cross-model divergence (D031 key finding for Discussion):**
   | Dimension | R1-32B L63 | QwQ L60 |
   |-----------|-----------|---------|
   | Bonferroni | W=1 only (3/3) | All 15 W (3/3) |
   | Lead time | +11.7 to +13.3 (excellent) | -1.2 to +1.9 (poor) |
   | HS vs Position | HS >> Pos (+14.2pp) | HS < Pos (-0.6pp) |
   | Coverage (W=1) | 25% | 74% |
   Paper MUST discuss this divergence per-model, not unify into single narrative.

   **OLD 32B results at BIASED layers (L2/L10) — RETRACTED as metric artifact:**
   - R1-32B L10: precision +9.4pp (p=0.064), accuracy +6.2pp (p=0.13)
   - QwQ-32B L2: precision +5.8pp (p=0.35), accuracy +0.9pp (p=0.83)
   - These non-significant results were caused by the biased `bal_acc × crossing_rate` metric selecting layers where HS signal is weak.

   **Holm-Bonferroni COMPLETE (D032): 12/12 ALL PASS**
   Previously 5/12 (biased layers). With corrected layers: **12/12** step-down pass (α=0.05).

   | Rank | Model | Metric | p-value | Threshold | Pass |
   |------|-------|--------|---------|-----------|------|
   | 1 | R1-8B | precision | <0.001 | 0.0042 | ✅ |
   | 2 | OT-7B | bal_acc | <0.001 | 0.0045 | ✅ |
   | 3 | OT-7B | precision | <0.001 | 0.0050 | ✅ |
   | 4 | OT-7B | FPR | <0.001 | 0.0056 | ✅ |
   | 5 | QwQ | bal_acc | <0.001 | 0.0063 | ✅ |
   | 6 | QwQ | precision | <0.001 | 0.0071 | ✅ |
   | 7 | R1-32B | bal_acc | <0.001 | 0.0083 | ✅ |
   | 8 | R1-32B | precision | <0.001 | 0.0100 | ✅ |
   | 9 | QwQ | FPR | 0.004 | 0.0125 | ✅ |
   | 10 | R1-8B | bal_acc | 0.005 | 0.0167 | ✅ |
   | 11 | R1-32B | FPR | 0.007 | 0.0250 | ✅ |
   | 12 | R1-8B | FPR | 0.044 | 0.0500 | ✅ |

   **Caveats**: Different W per model (R1-8B W=15, OT-7B/QwQ W=3, R1-32B W=1). Tests measure "HS > text at each model's best setting," not "at uniform W." R1-32B W=1 has 25% coverage. Paper must state these conditions.

   **FPR dual reporting**: Step-level (r1-8b: HS 8.8%, text 20.5%) vs trace-level (HS 14.8%, text 22.2%). Both reported.

   **FPR reversal RESOLVED (D026)**: OT-7B HS FPR@L16 (10.0%) < Text FPR at ANY window (16.1%). HS dominates on FPR at 7-8B.

   **Effect size consistency**: Precision advantage across all 4 models at corrected layers: R1-8B +22.4pp, OT-7B +21.2pp, QwQ +23.6pp, R1-32B +15.4pp. Remarkably consistent +15-24pp range.

   Paper recommended claim (D032): "At correctly selected layers, HS probes significantly outperform text probes on all 4 models (12/12 Holm-Bonferroni, precision +15-24pp). The layer selection metric `bal_acc × crossing_rate` systematically biases toward shallow layers, entirely masking this advantage at 32B scale. Practical implications differ by model: 7-8B models show strong HS advantage with comparable timing; R1-32B shows excellent lead time (+13 steps) but narrow coverage at the significant window; QwQ shows robust statistical significance but HS detects later than text."

3. **HS and text monitoring exhibit different detection timing profiles** (narrowed from old Claim 3, now 4/4 models with GRU) — On r1-8b: HS temporal LR detects AT the commitment point (lead ~0) while text detects ~10 steps earlier. GRU achieves modest positive lead (+4.5+-3.0, worst seed +0.9). BOCPD/CUSUM fail to improve over simple thresholds. The oracle's +31-step advantage shows hidden states encode current safety state but poorly predict future trajectory. On 32B models: timing profiles vary (QwQ GRU lead +15.9, R1-32B +8.8) but FPR differences are non-significant. OT-7B GRU (layer 16, multi-layer L13-19, 3 seeds): bal_acc 74.6+-1.3%, coverage 64.5+-7.0%, lead +33.6+-4.8, FPR 27.4+-6.1%. GRU trades higher FPR for longer lead (consistent with R1-8B pattern). NOTE: OT-7B absolute lead times are inflated by long traces (~80 sentences vs ~30). Paper should normalize or explicitly caveat trace length differences when comparing across models.

   NOTE: 32B timing profiles should be RE-EVALUATED at corrected layers (L60/L63) — current GRU results used old biased layers.

## Methodological Contribution: Layer Selection Sensitivity (D028, elevated from RETRACTED Claim 4)

The layer selection metric `bal_acc × crossing_rate` systematically biases toward shallow layers because shallow layers have higher crossing rates (more frequently crossing the detection threshold). This bias is especially problematic for 32B models, where it selects layers at 3-16% depth instead of deep layers selected by threshold-dependent metrics.

**Ablation evidence (4 models × 5 metrics) — UPDATED D036**:
- `bal_acc × crossing_rate`: selects L2 (QwQ), L10 (R1-32B) — shallow, biased
- Pure `bal_acc`: selects **middle layers** for 32B — L30 (QwQ, 47%), L47 (R1-32B, 73%); deep for 7-8B (agrees with other metrics). Threshold-free metric, behaves like AUROC.
- `precision`: selects deep layers for all models (L60/L63 for 32B)
- `pre_cp_fpr`: selects deep layers for all models
- `composite` (additive): selects deep layers for all models
- **Pattern**: Threshold-FREE metrics (bal_acc, AUROC) → middle layers; threshold-DEPENDENT metrics (precision, FPR, composite) → deep layers. Crossing_rate-contaminated metrics → shallow layers.

**LOO-CV stability (D036)**: Under LOO-CV, the dominant layer is selected in 65-68% of folds regardless of metric. QwQ L30 selected 13/19 folds (bal_acc), R1-32B L47 selected 13/20 folds (bal_acc). Selection is robust to val set composition.

**Corrected layer definition (D036)**: "Corrected layers" = consensus of threshold-dependent metrics (precision, inverse FPR, additive composite) — 3 of 4 non-biased metrics, not all 4. Pure bal_acc selects middle layers (L30/L47) with higher step-level accuracy (0.75/0.83 vs 0.71/0.76 at deep layers), but deployment-relevant metrics (precision, FPR) favor deep layers where all 4 models achieve HB-significant HS advantage.

**Impact**: Incorrect layer selection entirely masked the HS advantage at 32B scale, leading to the false conclusion that HS advantage is scale-dependent. Even among unbiased metrics, metric choice affects optimal layer depth — threshold-free vs threshold-dependent is a second dimension of researcher degrees of freedom beyond the crossing_rate bias.

**Anti-circular-reasoning defense (D031, refined D036)**: The claim that deep layers are "correct" for deployment rests on: (1) `crossing_rate` has a MECHANISTIC bias — shallow layers have compressed representations (1.4-2.7× smaller cosine distances) generating noise-driven crossings; (2) threshold-dependent metrics (precision, FPR) directly measure deployment-relevant properties; (3) at deep layers, all 4 models show significant HS advantage (HB corrected); (4) LOO-CV confirms selection stability. The paper presents layer selection as a "researcher degree of freedom" with systematic audit via sensitivity analysis.

**Paper treatment**: Dedicated subsection in Method + Table showing metric × model → selected layer + downstream HS-text comparison. Frame as sensitivity analysis, not "correct vs incorrect."

## Story Spine

- **Problem**: Reasoning models exhibit "self-jailbreak" — safety reasoning and harmful execution interleave throughout extended CoT, culminating in a "commitment point" where safety reasoning permanently ceases. Existing hidden-state detectors (TrajGuard, SafeSwitch, SIREN) target adversarial INPUT attacks on instruction-tuned models; they have never been evaluated on reasoning-model self-jailbreak where the threat is the model's OWN reasoning process.

- **Existing approaches & gaps**: Hidden-state detectors achieve 95% defense on standard LLMs (TrajGuard) but operate at token-level. Reasoning-model safety analysis (Self-Jailbreaking, HarmThoughts) characterizes the phenomenon without providing deployable detectors. Text-level CoT monitors (SafeRemind, SafeThink) are vulnerable to pathological CoT. No prior work systematically compares detection modalities for reasoning-model self-jailbreak.

- **Our framing**: We provide the first systematic evaluation of detection methods for reasoning-model safety commitment across **4 models, 2 architectures (Llama + Qwen), 2 training methods (R1-distilled + STILL), and 2 scales (7-8B + 32B)**, comparing hidden-state probes, text-based probes, sequence models (GRU), change-point detection (BOCPD/CUSUM), unsupervised methods (Mahalanobis, RepE direction, CCS), and nonlinear probes (MLP). We discover that: (a) temporal context is the most robust improvement, benefiting both modalities universally; (b) HS probes universally outperform text at correctly selected layers, with a critical sensitivity to layer selection methodology; (c) existing methods designed for other settings (TrajGuard, BOCPD, CCS, RepE) fail on reasoning model commitment; (d) linear probes are sufficient (MLP adds no value); (e) safety representations are model-specific (cross-transfer fails entirely), validated by control task (selectivity 7.5-18.5pp).

- **Headline result (D032)**: "Hidden-state probes significantly outperform text probes for safety commitment detection on all 4 models (12/12 Holm-Bonferroni, precision +15-24pp), but this advantage is entirely invisible under biased layer selection metrics. The composite metric `bal_acc × crossing_rate` systematically selects shallow layers at 32B scale, masking the HS signal and producing false negatives. This methodological finding, together with model-specific practical trade-offs at 32B (early detection vs broad coverage) and the comprehensive failure of 6 alternative methods, establishes that supervised temporal probing with principled layer selection is the most effective and robust approach for monitoring reasoning-model safety commitment."

## Key Evidence Summary

### R1-8B (Llama-8B, R1-distilled, n=43 test, class_weight=balanced, 60/20/20 split — CANONICAL)

Best layer: 14 (45% depth). Full sweep layers 0-24 confirmed: layer 12 marginally better (+0.4pp bal_acc), no practical difference.

| Method | Coverage | Lead Time | Pre-CP FPR | Safe FPR |
|--------|----------|-----------|------------|----------|
| HS Static LR L14 | — | -2.0 | **9.7%** | — |
| HS Temporal W=5 | — | +0.6 | **10.2%** | — |
| HS Temporal W=15 | — | **-0.1** | **8.8%** | — |
| Text Temporal W=15 | — | +10.3* | 20.5% | — |
| GRU Multi-7L (3-seed) | 72.9+-4.0% | +4.5+-3.0 | 16.5+-4.1% | — |

*Text lead time inflated by high pre-CP FPR (trigger-happy detection)
NOTE: HS LR lead time collapsed to ~0 with balanced weights — HS detects AT commitment, not before. Only GRU achieves positive lead (+4.5, worst seed +0.9).

### OT-7B (Qwen-7B, STILL-trained, n=47 test, 228 total traces) — D026 CORRECTED to layer 16

Best layer: **16 (57% depth)**. M001 corrected: layer 0 was selected by bal_acc x crossing_rate bug; layer 16 selected by bal_acc.

| Method | Bal Acc | Precision | Coverage | Pre-CP FPR | Lead |
|--------|---------|-----------|----------|-----------|------|
| HS Temporal W=3 L16 (best) | **68.8%** | **46.6%** | 53.2% | **10.0%** | — |
| Text Temporal W=25 (best) | 61.4% | 32.9% | 66.0% | 16.1% | 45.5 |
| Text Temporal W=3 (matched) | 57.9% | 25.4% | — | 27.1% | — |

Bootstrap (layer 16, matched W=3, 1000 resamples):
   bal_acc +10.7pp, 95% CI [4.9, 16.3], p<0.001 ✅
   precision +21.9pp, 95% CI [14.0, 29.6], p<0.001 ✅
   FPR -17.1pp, 95% CI [-22.2, -12.2], p<0.001 ✅ — **3/3 Holm-Bonferroni**
Selectivity: 18.3pp (real=0.688, random=0.505) — highest across all models

### 32B Cross-Architecture — D029 CORRECTED LAYERS

**QwQ-32B (Qwen-32B, native, n=19-20, Layer 60 — corrected from L2)**
- HS vs Text bootstrap (null-centered, 1000 resamples):
  - Bal Acc: +11-22pp across W=1-15, ALL 15/15 significant (p<0.005)
  - W=3 (matched): bal_acc +15.4pp (p<0.001 ✅), precision +23.6pp (p<0.001 ✅), FPR -9.8pp (p=0.004 ✅) — **3/3 Holm-Bonferroni**
- Caveats: HS lead time poor (-1.2 to 1.9 steps vs text 3.7-12.3), position baseline competitive
- Layer selection: `bal_acc × crossing_rate` selected L2 (3.1%); threshold-dependent metrics consensus selects L60 (94%); pure `bal_acc` selects L30 (47%, bal_acc=0.7513 vs L60=0.7101) (D036)

**R1-32B (Qwen-32B, R1-distilled, n=20, Layer 63 — corrected from L10)**
- W=1: bal_acc +18.7pp, p<0.001 ✅
- W≥5: NS (dimensionality: 51200 × W features for n=20)
- W=1: 3/3 Holm-Bonferroni ✅; W=3: 0/3 Bonferroni (null-centered v2); W≥5: NS
- Layer selection: `bal_acc × crossing_rate` selected L10 (15.6%); threshold-dependent metrics consensus selects L63 (98%); pure `bal_acc` selects L47 (73%, bal_acc=0.8290 vs L63=0.7585) (D036)

**OLD biased-layer results (RETRACTED as metric artifact):**
| Model | Biased Layer | Corrected Layer | Biased p-value | Corrected p-value |
|-------|-------------|----------------|----------------|-------------------|
| R1-32B | L10 (16%) | L63 (98%) | 0.064-0.13 (NS) | <0.001 (W=1) ✅ |
| QwQ-32B | L2 (3%) | L60 (94%) | 0.35-0.83 (NS) | <0.005 (all W) ✅ |

### 4-Model Holm-Bonferroni Summary (D032 — COMPLETE: 12/12 ✅)

| Model | Arch | Training | Scale | Layer | W | bal_acc | precision | FPR | Selectivity |
|-------|------|----------|-------|-------|---|--------|-----------|-----|-------------|
| R1-8B | Llama | R1-distilled | 8B | L14 (45%) | 15 | +8.2pp ✅ | +22.4pp ✅ | -7.4pp ✅ | 12.5pp |
| OT-7B | Qwen | STILL | 7B | L16 (57%) | 3 | +10.7pp ✅ | +21.9pp ✅ | -17.1pp ✅ | 18.3pp |
| QwQ-32B | Qwen | native | 32B | L60 (94%) | 3 | +15.4pp ✅ | +23.6pp ✅ | -9.8pp ✅ | 15.3pp |
| R1-32B | Qwen | R1-distilled | 32B | L63 (98%) | 1 | +18.7pp ✅ | +15.4pp ✅ | -14.6pp ✅ | 7.5pp |

**12/12 all pass Holm-Bonferroni step-down (α=0.05)**. Previously 5/12 with biased layers.
Precision advantage remarkably consistent: +15.4 to +23.6pp across all 4 models.
Caveats: Different W per model; R1-32B W=1 coverage=25%; QwQ lead time negative.

### Position Mediation Analysis (D038 → D039 → D042 complete)

**Finding**: Position (relative step t/T) is a significant component of probe performance. 3/4 models retain HS advantage after residualization; R1-32B is the exception.

| Model | W | Resid HS BA | Resid Text BA | HS-Text Gap | Gap p | HB |
|-------|---|------------|--------------|-------------|-------|-----|
| OT-7B | 3 | 0.609 | 0.540 | **+6.9pp** | <0.001 | ✅ |
| R1-8B | 15 | 0.669 | 0.605 | **+6.4pp** | <0.001 | ✅ |
| R1-8B | 3 | 0.571 | 0.534 | **+3.7pp** | <0.001 | ✅ |
| QwQ-32B | 3 | 0.619 | 0.582 | **+3.7pp** | 0.011 | ✅ |
| R1-32B | 1 | 0.552 | 0.532 | +1.9pp | 0.914 | ❌ |

Position-only BA: OT-7B/R1-8B/QwQ ≈ 0.706; R1-32B = 0.686.

**D042 final picture**: HS advantage has two separable components — position-mediated and non-positional. 3/4 models retain significant non-positional HS advantage (HB pass); R1-32B's advantage is almost entirely position-mediated (drop 20.4pp, residualized gap NS). This is consistent with R1-32B's other caveats (W=1 only significant, 25% coverage).

**Key implications for paper**:
1. Position is a significant component (12-20pp drop) — universal
2. 3/4 models retain non-positional HS advantage (residualized BA gap +3.7 to +6.9pp, HB pass)
3. R1-32B is the exception: HS advantage position-mediated, residualized gap NS
4. Temporal windowing preserves non-positional signal (R1-8B: 24pp drop@W=3 → 16pp@W=15)
5. Paper framing: "HS advantage persists after position removal in 3/4 models; R1-32B advantage is position-mediated"

### 5-Seed Robustness (D041)

| Model | HB Pass Rate | Mean ΔPrec ± std | Mean ΔBA ± std |
|-------|-------------|------------------|----------------|
| OT-7B | **5/5** | +20.9 ± 1.3pp | +11.3 ± 1.5pp |
| R1-32B | **5/5** | +13.7 ± 2.0pp | +11.8 ± 2.4pp |
| QwQ-32B | **5/5** | +19.9 ± 2.5pp | +11.4 ± 3.2pp |
| R1-8B | **3/5** | +14.6 ± 4.5pp | +9.4 ± 2.4pp |

R1-8B failures are FPR-specific (seed 123 FPR p=0.262, seed 456 FPR p=0.952). Precision is directionally consistent across all 20 seed-model combinations (always positive). ΔPrec never reverses.

**D041 insight**: Robustness splits by MODEL not SCALE. R1-32B (5/5, ΔPrec std=2.0pp) is more stable than R1-8B (3/5, ΔPrec std=4.5pp). "7-8B robust / 32B sample-limited" is factually wrong. R1-32B's absolute precision std (12.8pp) vs paired delta std (2.0pp) — paper must distinguish these.

**Per-model evidence tier (D042)**:
- **OT-7B**: Cleanest — 5/5 HB, largest residualized gap (+6.9pp), highest selectivity (18.3pp)
- **QwQ-32B**: Robust — 5/5 HB, residualized gap holds (+3.7pp), but position baseline competitive
- **R1-8B**: Precision-robust — residualized holds (+3.7-6.4pp), but FPR unstable (3/5 HB)
- **R1-32B**: Statistically stable (5/5 HB, ΔPrec std=2.0pp) but advantage position-mediated (residualized NS)

**Residualized precision**: Not tested (scope limited to BA per Reviewer recommendation).

### BA-Layer Robustness: Metric Circularity Refuted (D044)

R13 W1 concern: corrected selection uses threshold-dependent metrics (precision, FPR), evaluation also uses precision/FPR — potential circularity. Test: compute HS vs text on BA-selected layers (threshold-free criterion).

| Model | BA-Opt Layer | ΔPrec | ΔBA | ΔFPR | ΔAUROC | All 4 HB? |
|-------|-------------|-------|-----|------|--------|-----------|
| R1-8B | L12 | +17.8pp | +7.8pp | -12.9pp | +9.3pp | ✅ |
| OT-7B | L9 | +25.4pp | +11.7pp | -19.3pp | +14.8pp | ✅ |
| QwQ-32B | L30 | +18.0pp | +14.8pp | -8.0pp | +17.3pp | ✅ |
| R1-32B | L47 | +13.7pp | +14.9pp | -23.1pp | +21.1pp | ✅ |

**4/4 models × 4 metrics = 16/16 HB pass.** HS advantage is a genuine modality property, not a layer selection artifact.

Key insight: R1-32B on BA-layer L47 shows ΔPrec +13.7pp and ΔAUROC +21.1pp — stronger than corrected L63 in threshold-free metrics. OT-7B on BA-layer L9 has ΔPrec +25.4pp > corrected L16 (+21.9pp). HS advantage is robust to layer selection criterion.

Caveat: QwQ FPR adj_p=0.041 (marginal, CI close to zero). Other 15/16 tests p≤0.006.

### Post-hoc Power Analysis (D044)

| Model | n (test) | MDE (80% power, α=0.05) |
|-------|----------|------------------------|
| OT-7B | 47-69 | 6.7-8.1pp |
| R1-8B | 43-63 | 7.4-9.0pp |
| QwQ-32B | 29 | 9.5pp |
| R1-32B | 20-30 | 8.6-11.2pp |

All significant effects (15-24pp) are well above MDE → adequately powered. R1-32B residualized gap (+1.9pp) is far below MDE (11.2pp) → NS is power limitation, not evidence of absence.

### Negative Results (expanded with R3 supplementary experiments)
- **BOCPD/CUSUM (4/4 models)**: R1-8B BOCPD 93% detection but lead +3.5 < threshold +4.9; OT-7B/R1-32B/QwQ all 0% detection across all λ. CUSUM worse than threshold on all models.
- **Mahalanobis (4/4 models confirmed negative)**: R1-8B (+0.07), OT-7B (+0.031), R1-32B (+0.148), QwQ (+0.204) — all separation ≈ 0. Signal in minor PCA components, not principal directions.
- **RepE direction probing (4/4 models, corrected layers confirmed)**: Direction-based supervised method (needs CP labels). Results highly layer-dependent and model-specific:
  - R1-32B L63 (corrected): bal_acc=0.559 (near-random), FPR=49.9% — **direction vector fails at deep layer** where supervised LR excels (0.826). Train-test gap 13.3pp shows poor generalization.
  - QwQ L60 (corrected): bal_acc=0.756, precision=0.512, FPR=0.309 — **improves** from L2 (0.666), narrows gap with supervised LR W=1 (0.740 bal_acc), but still inferior in precision/FPR.
  - R1-8B L14: bal_acc=0.749, OT-7B L16: bal_acc=0.642
  - **Key insight**: Supervised LR is necessary — mean-difference direction cannot decode safety commitment at deep layers for R1-32B (discriminative training finds signal that simple direction averaging misses). Layer selection sensitivity applies to RepE too, but in model-specific ways (R1-32B: shallow better for RepE; QwQ: deep better for both).
- **MLP nonlinear probe (4/4 models)**: 3/4 models worse than LR. Linear probes sufficient; nonlinearity adds no value.
- **CCS-adapted (Burns et al. 2023, 4/4 models)**: WEAKLY SUPERVISED (needs CP labels for pair construction, not truly unsupervised). R1-8B bal_acc=0.777 (between supervised LR 0.817 and RepE 0.749). R1-32B FPR=0.410 (near-chance). OT-7B precision=0.319 (near-chance, high lead=20.5 is artifact of high FPR). Uses scheme B layers (biased). Paper must: (a) label as "weakly supervised" not "unsupervised"; (b) disclose pair construction differs from Burns et al.; (c) note scheme B layer limitation.
- **Cross-model transfer (exp-003)**: All directions fail entirely (best: 58.3% acc, 40.7% crossing).

## Venue Fit Risks

- **EMNLP LLM Security track fit**: Strong — defense/detection evaluation for reasoning model jailbreak.
- **Method simplicity risk**: Mitigate: frame as empirical study. Contribution is systematic evaluation + layer selection sensitivity discovery + comprehensive negative results.
- **Statistical power**: With corrected layers, **12/12** tests pass Holm-Bonferroni across ALL 4 models (up from 5/12 with biased layers).
- **HS advantage universal**: UPGRADED from "scale-dependent" — layer selection is the true moderator, not scale. Cleaner story.
- **Trace vs step FPR**: Both reported with explanation.
- **High safe FPR risk**: All methods 39-62% safe FPR. Frame as diagnostic tool limitation.
- **32B caveats**: HS advantage exists but is more sensitive to window size (R1-32B W=1 only) and affected by dimensionality (51200-d at large W with n=20). Lead times shorter than 7-8B. These are honest limitations, not disqualifiers.

## Anticipated Reviewer Concerns

1. "Method novelty?" → Empirical study + systematic method comparison + layer selection sensitivity as methodological contribution + comprehensive negative results (6 methods fail).
2. "Only one model family?" → **RESOLVED**: 4 models, 2 architectures (Llama + Qwen), 2 training methods, 2 scales. ALL showing significant HS advantage at corrected layers.
3. "GRU unstable?" → 3-seed reporting with worst-seed bounds. R1-32B GRU at L10 was unstable; needs re-evaluation at L63.
4. "Too few traces?" → Cross-model validation + control task selectivity 7.5-18.5pp.
5. "Fine-grained taxonomy?" → Out of scope for current study.
6. "HS doesn't beat text?" → **QUALIFIED REBUTTAL (D031)**: HS outperforms text at correct layers with STRONG evidence at 7-8B (precision +22pp, Holm-Bonf) and QUALIFIED evidence at 32B (R1-32B: significant W=1 but narrow; QwQ: significant all W but late detection). 32B non-significance at OLD layers was artifact. Layer selection sensitivity analysis shows this is a methodological issue, not absence of signal.
7. "Commitment point circular?" → Cross-model consistency + control task selectivity argues against artifact.
8. "Missing related work?" → Expansion to 30+ citations.
9. "No FPR analysis?" → RESOLVED: both trace-level and step-level FPR reported.
10. "High safe FPR?" → Limitation acknowledged.
11. "Control task / position confound?" → RESOLVED (C2, D011): selectivity 7.5-18.5pp, HS FPR < position-only FPR.
12. "Multiple testing correction?" → **RESOLVED**: 12/12 Holm-Bonferroni step-down (α=0.05) across all 4 models (up from 5/12 with biased layers).
13. "Trace vs step FPR?" → Both reported with explanation.
14. "Layer selection is just hyperparameter tuning?" → No — we show a systematic bias in a commonly used composite metric. The ablation across 5 metrics × 4 models is a reproducible methodological finding, not a one-off parameter choice.
15. "Why not just use the best layer for each model?" → We do. The point is that the METRIC for selecting "best" matters. Biased metrics produce systematically wrong selections, masking real effects.
16. "32B results are marginal / only W=1 significant for R1-32B?" → Dimensionality constraint (51200 × W > n=20 at W≥5). QwQ L60 significant at ALL W values. R1-32B L63 significant at W=1. Both confirm HS advantage exists; practical deployment would use W=1-3 for 32B models.

## Title Candidates (D031)
- "Layer Selection Matters: How Metric Choice Determines Hidden-State Probe Effectiveness for Safety Monitoring"
- "Temporal Probing for Safety Commitment Detection in Reasoning Models: A Comprehensive Evaluation"
- "What Detects Safety Commitment in Reasoning Models? A Systematic Comparison of Probe-Based Methods"
- "Hidden-State vs Text Monitoring for Reasoning Model Safety: Layer Selection as the Missing Variable"
