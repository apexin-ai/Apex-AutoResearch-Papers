## Treated vs Untreated Item Analysis (d025 MMLU, seed=42)

### Key Finding: ALL DiD non-significant
2.5% SFT injection does NOT produce item-level memorization.
Effects are global (SFT general effect), not item-specific.

### MMLU Results (d025: 3540 treated / 10502 untreated)
| Model | Treated Δ | Untreated Δ | DiD | Verdict |
|-------|-----------|-------------|-----|---------|
| Gemma-2-9B | +0.031** | +0.026*** | +0.006 (ns) | generalization |
| OLMo-2-7B | +0.016 (ns) | +0.027*** | -0.011 (ns) | mixed |
| Phi-4 | +0.003 (ns) | +0.006 (ns) | -0.003 (ns) | no-effect |
| Qwen2.5-14B | -0.069*** | -0.076*** | +0.007 (ns) | anti-contamination |
| Qwen2.5-7B | -0.038** | -0.029*** | -0.008 (ns) | anti-contamination |

### ARC Challenge (d025)
All 5 models: no-effect (treated/untreated delta both non-significant)

### Difficulty Interaction (d025 MMLU, 5-model mean)
| Bin | Treated Δ | Untreated Δ | Gap |
|-----|-----------|-------------|-----|
| Hard (&lt;0.4) | +0.061 | +0.064 | -0.003 |
| Medium | -0.006 | -0.002 | -0.004 |
| Easy (&gt;0.7) | -0.040 | -0.039 | -0.000 |

Regression-to-mean effect symmetric across treated/untreated.

### Files
Remote: westd:/root/contamcal-irt-calibration/artifacts/treated_untreated/
- treated_untreated_summary.csv (40 rows)
- treated_untreated_mmlu.pdf / _arc_challenge.pdf (5-panel bar plots)
- difficulty_interaction.csv + PDFs
- did_dose_response.pdf (DiD vs dosage trend)