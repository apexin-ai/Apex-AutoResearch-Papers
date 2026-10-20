## Free-Form Decoding Ablation: 3-Seed Robustness Summary

**Setup.** We repeat the free-form decoding ablation (§4.3) with three random seeds (123, 456, 789), each generating 8 samples per instance on SciERC (551 instances). The constrained-decoding reference is held fixed across seeds.

### Key Findings

**LP score compression persists without constrained decoding.** Across three seeds, the ratio of free-form to constrained LP standard deviation averages 0.92 ± 0.04 (range 0.89–0.97×), confirming that LP score compression is intrinsic to model confidence rather than an artifact of constrained decoding.

**NER selection is stable.** The free-form NER selection gap (selected − greedy F1) is negligible across all seeds (≤ 0.28 pp), consistent with the tied LP scores limiting selection effectiveness regardless of decoding mode.

**RE selection flip is robust.** Free-form decoding consistently produces a positive RE selection gap (+1.76 to +2.00 pp), contrasting with the negative gap (−0.68 pp) under constrained decoding. This sign flip is stable across all three seeds, reinforcing that the RE selection advantage is not a constrained-decoding artifact.

### Data Table

| Metric | Seed 123 | Seed 456 | Seed 789 | 3-Seed Mean ± SD |
|--------|----------|----------|----------|-------------------|
| LP σ ratio (free/constr) | 0.97 | 0.90 | 0.89 | 0.92 ± 0.04 |
| LP range ratio | 0.96 | 0.91 | 0.88 | 0.92 ± 0.04 |
| Tied fraction (free) | 57.7% | 58.4% | 59.0% | 58.4 ± 0.7% |
| Tied fraction (constr) | 59.7% | 59.7% | 59.7% | 59.7% (ref) |
| NER selection gap (pp) | +0.28 | +0.07 | +0.27 | +0.21 ± 0.12 |
| RE selection gap (pp) | +1.76 | +2.00 | +1.91 | +1.89 ± 0.12 |
| RE selection gap, constr (pp) | −0.68 | −0.68 | −0.68 | −0.68 (ref) |
| Parse rate | 99.95% | 99.98% | 100.0% | 99.98% |

### QE Signal Robustness (NER, ρ)

| Signal | Seed 123 | Seed 456 | Seed 789 | Mean ± SD |
|--------|----------|----------|----------|-----------|
| SJ | 0.384 | 0.378 | 0.394 | 0.385 ± 0.008 |
| FK | 0.324 | 0.286 | 0.312 | 0.307 ± 0.020 |
| LP | 0.217 | 0.227 | 0.247 | 0.230 ± 0.015 |
| EM | 0.327 | 0.320 | 0.320 | 0.322 ± 0.004 |
| VC | 0.408 | 0.417 | 0.421 | 0.415 ± 0.007 |

### QE Signal Robustness (RE, ρ)

| Signal | Seed 123 | Seed 456 | Seed 789 | Mean ± SD |
|--------|----------|----------|----------|-----------|
| SJ | 0.273 | 0.211 | 0.202 | 0.229 ± 0.039 |
| FK | 0.314 | 0.259 | 0.220 | 0.264 ± 0.047 |
| LP | 0.310 | 0.306 | 0.296 | 0.304 ± 0.007 |
| EM | 0.137 | 0.104 | 0.104 | 0.115 ± 0.019 |
| VC | 0.317 | 0.302 | 0.307 | 0.308 ± 0.008 |

**Source:** Registry exp_freeform_seed123, exp_freeform_seed456, exp_freeform_seed789. All DONE/success.