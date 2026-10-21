# Supplementary Completeness Check

## Cross-references

### Main → Appendix (all files compiled via main.tex)

| Ref in main | Source file | Label in appendix | Status |
|---|---|---|---|
| `\ref{sec:appendix_threshold}` | claim1.tex:32, method.tex:34 | appendix.tex:45 | ✅ |
| `\ref{sec:appendix_pertask_oracle}` | claim2.tex:7, claim2.tex:30 | appendix.tex:154 | ✅ |
| `\ref{sec:appendix_oracle}` | claim2.tex:31, method.tex:46 | appendix.tex:244 | ✅ |
| `\ref{sec:appendix_null}` | claim3.tex:26, claim3.tex:59 | appendix.tex:203 | ✅ |
| `\ref{sec:appendix_training}` | method.tex:38 | appendix.tex:320 | ✅ |
| `\ref{tab:hyperparams}` | method.tex:38 | appendix.tex:336 | ✅ |

All 6 unique main→appendix references resolve correctly.

### Appendix sections NOT referenced from main

| Label | Section title | Severity |
|---|---|---|
| `sec:appendix_multiseed` | Complete Multi-Seed Results | Low — underlying data for Table 3, implicitly covered |
| `sec:appendix_displacement` | Displacement Distribution | None — just redirects to main text Figure 3 |
| `sec:appendix_tsr_pertask` | Per-Task TSR Breakdown | Low — useful detail, could add reference from §5 |
| `sec:appendix_pertask_car` | Per-Task CAR Breakdown | Medium — main text claims "per-task ordering preserved" but doesn't cite this table |
| `sec:appendix_ssr` | Safe Success Rate Analysis | None — redirects to main text Table 5 |
| `sec:appendix_stepwise` | Step-wise Checkpoint Analysis | Low — supplements λ=0.1 discussion |
| `sec:appendix_spatial_bowl` | Cross-Scene Validation | None — data already in main text Table 6 |
| `sec:appendix_eval_seed` | Evaluation Seed Robustness | Low — standalone robustness check |
| `sec:appendix_tsr_collapse` | TSR Collapse Mechanism | Medium — main text discusses TSR drop (claim3.tex:35) without citing this analysis |
| `sec:appendix_pertask` | (duplicate label on Per-Task Oracle) | Note — unused alias, `sec:appendix_pertask_oracle` is the one referenced |

### Appendix tables not directly `\ref`'d from main

Only `tab:hyperparams` is directly referenced. The remaining 10 appendix tables (multiseed_full, threshold_sensitivity, dfcar_threshold, per_task_tsr, per_task_car, oracle_pertask, oracle_pertask_pi05, stepwise_lambda01, eval_seed_robustness, eval_seed_car_detail) are accessible via section-level references. This is acceptable convention.

## Number Consistency

### Claim 1 (Action-Collapsed Safety)

| Assertion in main | Main value | Appendix value | Status |
|---|---|---|---|
| Pi0+A1 CAR (Table 1) | 91.5% | — (no appendix duplicate) | ✅ |
| Pi0+A1 collapsed rate | 99.6% | — | ✅ |
| Pi0+A1 dfCAR | ≈0% (3/732) | — | ✅ |
| Threshold robustness [2,200] mm | "identical dfCAR" | tab:dfcar_threshold: all 8 configs identical across [2,200] mm | ✅ |
| Threshold sensitivity A1-LoRA | 99.6% at 0.1mm | tab:threshold_sensitivity: 99.6% at 0.1mm | ✅ |

### Claim 2 (EE-Only SDF)

| Assertion in main | Main value | Appendix value | Status |
|---|---|---|---|
| Oracle-adaptive CAR | 75.0% | tab:oracle_pertask: (82.5+55+77.5+85)/4 = 75.0% | ✅ |
| Oracle-fixed CAR | 73.1% | tab:oracle_pertask: (85+50+77.5+80)/4 = 73.125% | ✅ |
| Oracle-feature CAR | 76.9% | tab:oracle_pertask: (90+47.5+82.5+87.5)/4 = 76.875% | ✅ |
| Task 1 (choco_pudding): +9 pp | LoRA 46→Oracle-adaptive 55 | tab:oracle_pertask: 46.0→55.0 | ✅ |
| orange_juice: LoRA 96%→Oracle 82.5% | -13.5 pp | tab:oracle_pertask: 96.0→82.5 | ✅ |
| Pi0.5 Oracle Δ = -5.1 pp | 57.0→51.9 | tab:oracle_pertask_pi05: (50+75+70+12.5)/4 = 51.875 ≈ 51.9 | ✅ |

### Claim 3 (Avoidance Source)

| Assertion in main | Main value | Appendix value | Status |
|---|---|---|---|
| LoRA-only mean CAR | 54.83±2.25 | tab:multiseed_full: (57+52.5+55)/3 = 54.83, std=2.25 | ✅ |
| LoRA-only mean TSR | 49.7±3.2 | tab:multiseed_full: (46+51.5+51.5)/3 = 49.67, std=3.18 | ✅ |
| SDF λ=0.005 mean CAR | 54.5±2.29 | tab:multiseed_full: (57+54+52.5)/3 = 54.5 | ✅ |
| SDF λ=0.01 mean CAR | 56.33±1.61 | tab:multiseed_full: (57+57.5+54.5)/3 = 56.33 | ✅ |
| SDF λ=0.1 mean CAR | 57.00±2.18 | tab:multiseed_full: (58+58.5+54.5)/3 = 57.0 | ✅ |
| SDF λ=0.1 seeds: 58.0, 58.5, 54.5 | claim3.tex:59 | tab:multiseed_full: s0=58.0, s1=58.5, s2=54.5 | ✅ |
| Permutation p=0.155 (two-tailed) | claim3.tex:59 | sec:appendix_null: 13/84 ≈ 0.155 | ✅ |
| Permutation p=0.071 (one-tailed) | — | sec:appendix_null: 6/84 ≈ 0.071 | ✅ |
| Null pool mean=54.67, std=2.04 | — | sec:appendix_null: verified | ✅ |
| Phase 2 ablation CAR=57.5% (18K, s2) | claim3.tex:26 | sec:appendix_null last para: 57.5% at 18K | ✅ |
| SSR/TSR 0.39→0.51–0.60 | Table 5 | — (appendix redirects to main) | ✅ |
| spatial_bowl: 12.0% vs 11.5% | Table 6 | sec:appendix_spatial_bowl: consistent | ✅ |

### Cross-table arithmetic verification

| Check | Result |
|---|---|
| Per-task CAR aggregates match per-seed aggregates | ✅ all verified |
| Eval-seed robustness ranges overlap with training-seed ranges | ✅ |
| Step-wise λ=0.1 30K values match multiseed table | ✅ s0=58.0, s1=58.5, s2=54.5 |

## Content Coverage

| Required content | Present | Location |
|---|---|---|
| Ablation detailed tables | ✅ | threshold (§A.3), per-task CAR (§A.5), per-task TSR (§A.4), step-wise (§A.9), null distribution (§A.8) |
| Extra seed data | ✅ | per-seed results (§A.1), eval-seed robustness (§A.12) |
| Implementation details | ✅ | architecture, training schedule, hyperparams table, eval protocol, data, compute (§A.13) |
| Oracle variant details | ✅ | three variants described (§A.10), per-task breakdown (§A.7) |
| Cross-scene validation | ✅ | spatial_bowl (§A.11), data also in main text |
| TSR collapse mechanism | ✅ | §A.14 |
| SSR analysis | ⚠️ | §A.6 is a stub redirecting to main text Table 5 — no additional analysis |
| Displacement distribution | ⚠️ | §A.2 is a stub redirecting to main text Figure 3 — no additional analysis |

## Issues Found

### Must-fix

None. All cross-references resolve, all numbers are consistent.

### Recommended improvements

1. **Add references to unreferenced appendix sections.** Two appendix sections contain substantial analysis that the main text discusses without citing:
   - claim3.tex "CAR–TSR trade-off" paragraph (line 35) should cite `Appendix~\ref{sec:appendix_tsr_collapse}` for the mechanism analysis.
   - claim3.tex "per-task CAR ordering is preserved" (line 26) should cite `Appendix~\ref{sec:appendix_pertask_car}` for the detailed table.

2. **Remove or substantiate stub sections.** `sec:appendix_displacement` (§A.2) and `sec:appendix_ssr` (§A.6) contain only one-line redirects to main text. Either add supplementary analysis or remove them to save space.

3. **Remove duplicate label.** `sec:appendix_pertask` (appendix.tex:153) is defined but never referenced; only its sibling `sec:appendix_pertask_oracle` (line 154) is used. Remove the unused label to avoid confusion.

4. **Unused file.** `experimental_framework.tex` is not `\input`'d in `main.tex` — it appears to be an earlier draft of `method.tex`. Can be archived or deleted.
