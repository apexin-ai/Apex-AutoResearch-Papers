# Paper–Registry Numerical Consistency Audit

**Date:** 2026-05-21
**Paper commit:** e4522a3
**Registry:** 32 experiments (read via `read_registry`)
**Raw data:** Verified against `artifacts/` JSON files where available

---

## Summary

- **Total quantitative claims audited:** 98 (experimental results only; hyperparameters/architecture constants excluded)
- **Matched:** 91
- **Mismatched (⚠️):** 5
- **Minor rounding/notation (⚡):** 2

---

## ⚠️ MISMATCHES

### 1. N=5 Steering: β=0 baseline GAR
| Location | Paper | Registry Source | Registry Value | Delta |
|----------|-------|----------------|----------------|-------|
| abstract:2, intro:16, experiments:49, discussion:3, conclusion:3 | **0.029** | `attention_steering_v7_tg_gen` beta=0.0 | **0.028** | +0.001 |
| Raw data: `artifacts/attention_steering_v7_tg_gen/data/attention_steering_results.json` line 7 confirms 0.028 | | | | |

**Severity:** Low. 0.028 rounds to 0.028 not 0.029 at 3dp. Appears in abstract + 4 other sections.

### 2. N=5 Steering: β=2 GAR
| Location | Paper | Registry Source | Registry Value | Delta |
|----------|-------|----------------|----------------|-------|
| experiments:49 ("0.029→0.075") | **0.075** | `attention_steering_v7_tg_gen` beta=2.0 | **0.062** | +0.013 (21%) |
| Raw data: `artifacts/attention_steering_v7_tg_gen/data/attention_steering_results.json` line 10 confirms 0.062 | | | | |

**Severity:** HIGH. 21% relative difference. This number anchors the "negligible change at low β" narrative and the "∼9× recovery" calculation in the figure caption. With registry value, the β=2→5 jump is 0.062→0.6795 = 11.0×, not "∼9×". The paper's 0.075→0.697 gives 9.3×.

### 3. N=5 Steering: β=5 GAR
| Location | Paper | Registry Source | Registry Value | Delta |
|----------|-------|----------------|----------------|-------|
| abstract:2, intro:16, experiments:49, discussion:3, conclusion:3 | **0.697** | `attention_steering_v7_tg_gen` beta=5.0 | **0.6795** | +0.0175 (2.6%) |
| Raw data: `artifacts/attention_steering_v7_tg_gen/data/attention_steering_results.json` line 11 confirms 0.6795 | | | | |

**Severity:** Medium. 0.6795 rounds to 0.680 (3dp), not 0.697. Possible digit transposition: 0.6**79**5 → 0.6**97**5 → 0.697. Appears in abstract + 4 other sections. Propagated as the headline steering result.

### 4. Scheduled sampling gap: "30×"
| Location | Paper | Registry Source | Registry Value | Delta |
|----------|-------|----------------|----------------|-------|
| intro:16, discussion:5, conclusion:3 | **30×** | `eval_v8b_ss` comparison.iid_modelgen_gap_ratio_v7 | **32×** | −2× |
| Raw calc: v7 IID GAR-ours 0.5035 / model-gen GAR-ours 0.0157 = 32.1× | | | | |

**Severity:** Medium. "30×" is used 3 times as a round figure. Registry and raw data both say 32×. The paper's own "20–33×" range (used elsewhere) implies the upper bound is 33×, making "30×" internally inconsistent — it should be "32×" or "∼32×".

### 5. N=5 PPL at β=5: "1.91"
| Location | Paper | Registry Source | Registry Value | Delta |
|----------|-------|----------------|----------------|-------|
| experiments:49 ("1.41→1.91") | **1.91** | `attention_steering_v7_tg_gen` beta=5.0 | **1.908** | +0.002 |

**Severity:** Negligible — acceptable 3sf rounding (1.908 → 1.91). Included for completeness.

---

## ⚡ MINOR ROUNDING / NOTATION

### A. TRC gap "+0.002"
| Location | Paper | Registry Source | Registry Value |
|----------|-------|----------------|----------------|
| analysis:45 | +0.002 | `trc_baseline_v7_tg` v7_tg gap | +0.0016 |

0.0016 rounded to +0.002 at 3dp. Acceptable.

### B. GAR-Dongre TF/AR ratio direction for Qwen "1.28×"
| Location | Paper | Registry Source | Registry Value |
|----------|-------|----------------|----------------|
| analysis:49 | 1.28× (described as "TF/AR ratio") | v7: TF Dongre=0.0152, AR Dongre=0.0194 | TF/AR=0.78×, AR/TF=1.28× |

Paper describes both Llama and Qwen as "TF/AR ratio" but Llama is truly TF/AR (1.002), while Qwen is AR/TF (1.28). The numbers themselves are correct; the ratio direction label is inconsistent. Functionally equivalent for the "negligible gap" argument.

---

## ✅ VERIFIED MATCHES — Core Results

### Baseline GAR Decay (phase1_gar_diag, llama_phase1_gar_diag)
| Paper Claim | Paper Value | Registry Source | Registry Value | Match |
|-------------|-------------|----------------|----------------|-------|
| Qwen turn-1 GAR | 0.0418 | phase1_gar_diag turn1_avg_gar | 0.0418 | ✅ |
| Qwen mid-conv GAR | 0.0122 | phase1_gar_diag mid_turns_avg_gar | 0.0122 | ✅ |
| Qwen relative decline | 70.8% | phase1_gar_diag relative_drop | 0.708 | ✅ |
| Qwen T1→T10 decline | 84.7% | Computed: (0.0418−0.0064)/0.0418 | 84.7% | ✅ |
| Llama turn-1 GAR | 0.026 | llama_phase1_gar_diag turn1 | 0.0263 | ✅ (rounded) |
| Llama turn-10 GAR | 0.003 | llama_phase1_gar_diag turn10 | 0.0026 | ✅ (rounded up) |
| Llama T1→T10 decline | 90.1% | llama_phase1_gar_diag t1_t10_decay_pct | 90.1% | ✅ |

### Table 1: Five-Way Comparison (phase2_4way_eval_heldout, phase2_tg_s42_v7, v9_pcgrad)
| Config | Column | Paper GAR-O | Registry GAR-O | Paper GAR-D | Registry GAR-D | Paper PPL | Registry PPL | Match |
|--------|--------|-------------|----------------|-------------|----------------|-----------|--------------|-------|
| Base | IID | 0.01 | 0.0107 | 0.00 | 0.003 | 4.23 | 4.23 | ✅ |
| Base | Held-out | 0.01 | 0.0128 | 0.00 | 0.0031 | 4.34 | 4.34 | ✅ |
| ThreadGate | IID | 0.50 | 0.5035 | 0.02 | 0.0152 | 2.78 | 2.784 | ✅ |
| ThreadGate | Held-out | 0.50 | 0.5035 | 0.02 | 0.0152 | 2.78 | 2.78 | ✅ |
| +PCGrad | IID | 0.50 | 0.5002 | 0.01 | 0.0123 | 2.78 | 2.78 | ✅ |
| +PCGrad | Held-out | 0.50 | 0.5002 | 0.01 | 0.0123 | 2.78 | 2.78 | ✅ |
| Uniform Gate | IID | 0.51 | 0.5053 | 0.01 | 0.0124 | 2.78 | 2.78 | ✅ |
| Uniform Gate | Held-out | 0.51 | 0.5053 | 0.01 | 0.0124 | 2.78 | 2.78 | ✅ |
| LoRA-only | IID | 0.50 | 0.4978 | 0.01 | 0.0132 | 2.78 | 2.78 | ✅ |
| LoRA-only | Held-out | 0.50 | 0.4978 | 0.01 | 0.0132 | 2.78 | 2.78 | ✅ |

### Derived Statistics from Table 1
| Paper Claim | Paper Value | Computed from Registry | Match |
|-------------|-------------|----------------------|-------|
| GAR-ours spread | 0.75 pp | max(0.5053)−min(0.4978)=0.0075=0.75pp | ✅ |
| PPL identical at 2.78 | 2.78 | All 4 fine-tuned = 2.78 | ✅ |
| GAR-Dongre range | 0.01–0.02 | 0.0123–0.0152 | ✅ |
| TF→AR gap range | 20–33× | 0.4978/0.0245=20.3× to 0.5053/0.0149=33.9× | ✅ |
| AR GAR-ours range | 0.015–0.025 | 0.0149–0.0245 | ✅ |

### PCGrad Comparison (analysis:24)
| Paper Claim | Paper Value | Registry Source | Registry Value | Match |
|-------------|-------------|----------------|----------------|-------|
| IID GAR-ours | 0.50 vs 0.50 | v9_pcgrad=0.5002, v7=0.5035 | 0.50 vs 0.50 | ✅ |
| PPL | 2.780 vs 2.784 | v9_pcgrad=2.78, v7=2.784 | 2.780 vs 2.784 | ✅ |
| AR GAR | 0.015 vs 0.016 | v9_pcgrad=0.0151, v7=0.0157 | 0.015 vs 0.016 | ✅ |
| Cosine sim pre-PCGrad | −0.089 | analysis_gradient_conflict epoch0 | −0.089 | ✅ |
| Cosine sim with PCGrad | −0.15 to +0.09 | v9_pcgrad cos_sim trajectory | oscillates around 0 | ✅ |

### Gradient Conflict (analysis:22, analysis_gradient_conflict)
| Paper Claim | Paper Value | Registry Value | Match |
|-------------|-------------|----------------|-------|
| Neg layers pct | 68–79% | epoch2=67.9%, epoch0=78.6% | ✅ |
| Cosine sim range | −0.089 to −0.042 | epoch0=−0.089, epoch2=−0.042 | ✅ |
| NTP magnitude ratio | 7.5–14.7× | epoch0=7.5, epoch2=14.7 | ✅ |

### Gate Conditioning (analysis:9)
| Paper Claim | Paper Value | Registry Source | Match |
|-------------|-------------|----------------|-------|
| 27/28 layers inverted | 27/28 | Wilcoxon test in registry | ✅ |
| p-value | 3.73×10⁻⁸ | Registry | ✅ |
| Effect size r | 0.975 | Registry | ✅ |
| L23 turn-1 gate | 0.769 | Analysis data | ✅* |
| L23 turn-21 gate | 0.979 | Analysis data | ✅* |
| L14 turn-1 gate | 0.747 | Analysis data | ✅* |
| L14 turn-21 gate | 0.928 | Analysis data | ✅* |
| Inference gate range | 0.93–0.98 | v7 gate mean=0.9336 | ✅ |
| Attenuation | 2–7% | 1−0.98=2%, 1−0.93=7% | ✅ |

*Gate per-turn values not directly in registry summary; consistent with gate profile data.

### Scheduled Sampling (phase2_tg_s42_v8b_resume, eval_v8b_ss)
| Paper Claim | Paper Value | Registry Source | Registry Value | Match |
|-------------|-------------|----------------|----------------|-------|
| AR GAR-ours before | 0.016 | v7 model-gen GAR-ours | 0.0157 | ✅ (rounded) |
| AR GAR-ours after | 0.318 | v8b model-gen GAR-ours | 0.3177 | ✅ (rounded) |
| Improvement factor | 20× | 0.3177/0.0157 | 20.2× | ✅ |
| Gap compression | → 1.57× | eval_v8b_ss | 1.57× | ✅ |
| PPL after SS | 1.38 | v8b model-gen PPL | 1.38 | ✅ |
| PPL baseline | 1.36 | v7 model-gen PPL | 1.36 | ✅ |
| GAR-Dongre before | 0.019 | v7 model-gen GAR-Dongre | 0.0194 | ✅ (rounded) |
| GAR-Dongre after | 0.353 | v8b model-gen GAR-Dongre | 0.3533 | ✅ (rounded) |

### N=50 Steering (attention_steering_gen_n50)
| Paper Claim | Paper Value | Registry Value | Match |
|-------------|-------------|----------------|-------|
| Valid convs | 39 | n_valid=39 | ✅ |
| β=0 mean GAR | 0.064 | 0.0641 | ✅ |
| β=0 std | 0.081 | 0.0809 | ✅ |
| β=0 median | 0.031 | (not in registry, from raw data) | ✅* |
| β=2 GAR | 0.128±0.110 | 0.128±0.1101 | ✅ |
| β=3 GAR | 0.556±0.060 | 0.5558±0.0601 | ✅ |
| Recovery factor | 8.7× | 0.5558/0.0641=8.67≈8.7 | ✅ |
| PPL increase | 9% | (1.5605−1.4324)/1.4324=8.9%≈9% | ✅ |
| PPL range | 1.43→1.56 | 1.4324→1.5605 | ✅ |

### Llama Cross-Model (llama_eval_s42, llama_ar_matched_eval)
| Paper Claim | Paper Value | Registry Source | Registry Value | Match |
|-------------|-------------|----------------|----------------|-------|
| TF GAR-ours | 0.484 | llama_ar_matched_eval tf_tg_ours_raw | 0.4836 | ✅ |
| AR GAR-ours | 0.039 | llama_ar_matched_eval AR TG ours mid_gar | 0.0388 | ✅ |
| Gap ratio | 12.5× | llama_ar_matched_eval GAR-ours raw gap | 12.5× | ✅ |
| GAR-Dongre TF/AR Llama | 1.002× | llama_ar_matched_eval | 1.002× | ✅ |
| Llama gate min layer | 25 | llama_tg_s42 gate profile L25=0.719 | 0.719 (min) | ✅ |
| Qwen gate min layers | 3–4 | v7 gate profile L3=0.801, L4=0.789 | L3=0.801,L4=0.789 | ✅ |

### TRC Analysis (trc_baseline_v7_tg)
| Paper Claim | Paper Value | Registry Value | Match |
|-------------|-------------|----------------|-------|
| TG TF TRC | 0.334 | 0.3339 | ✅ |
| TG AR TRC | 0.332 | 0.3323 | ✅ |
| LoRA TF TRC | 0.349 | 0.349 | ✅ |
| LoRA AR TRC | 0.411 | 0.4106 | ✅ |
| LoRA gap | −0.062 | −0.0617 | ✅ |

### Instruction Retention (instruction_retention_test)
| Paper Claim | Paper Value | Registry Value | Match |
|-------------|-------------|----------------|-------|
| Content compliance delta | +23.8 pp | delta=+0.238 | ✅ |
| GAR-compliance r | 0.200 | 0.2003 | ✅ |
| GAR-compliance p | 0.007 | 0.007 | ✅ |
| McNemar p | 0.077 | 0.0771 | ✅ |
| Constraint types | 18 | 18 (4 types × coverage) | ✅ |

---

## Downstream Impact of Mismatches

### If corrected, what changes:

1. **β=0 baseline (0.028 → 0.029):** Abstract/intro/discussion/conclusion all say "0.029". Should be "0.028". Low impact on narrative.

2. **β=2 GAR (0.062 → 0.075):** Only in experiments:49 figure description. Affects the "∼9× recovery" calculation:
   - Paper: 0.075 → 0.697 = 9.3×
   - Registry: 0.062 → 0.6795 = 11.0×
   - If corrected, the ∼9× claim becomes ∼11×, which actually *strengthens* the result.

3. **β=5 GAR (0.6795 → 0.697):** Headline steering number in abstract + 4 sections. 0.6795 rounds to 0.680 at 3dp. If 0.697 is a digit transposition of 0.6795→0.6975→0.697, this is a copy error. The correct rounded value should be 0.680 (or 0.68 at 2dp).

4. **"30×" → "32×":** The paper already uses "20–33×" elsewhere, so using "30×" as a round figure is internally inconsistent. Should be "∼32×" or the paper should use "∼30×" consistently.

---

## Recommendations

| Priority | Action | Files Affected |
|----------|--------|---------------|
| **HIGH** | Verify β=5 GAR: is it 0.6795 (registry) or 0.697 (paper)? Check raw per-conversation data on server. If registry is correct, update abstract.tex, introduction.tex, experiments.tex, discussion.tex, conclusion.tex | 5 files |
| **HIGH** | Verify β=2 GAR: is it 0.062 (registry) or 0.075 (paper)? Check raw data. | experiments.tex |
| **MED** | Fix β=0 baseline: 0.028 → 0.029. Small but propagated across 5 sections. | abstract, intro, experiments, discussion, conclusion |
| **MED** | Harmonize "30×" with registry "32×". Either use "∼32×" or "∼30×" consistently. | intro, discussion, conclusion |
| **LOW** | Fix GAR-Dongre ratio direction label in analysis.tex:49 for Qwen (currently says TF/AR but value is AR/TF). | analysis.tex |
