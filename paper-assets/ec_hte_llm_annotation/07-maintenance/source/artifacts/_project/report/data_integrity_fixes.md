# Data Integrity Fixes

## Issue 1: AUC=0.86 — NO FIX NEEDED
- Source CSV: artifacts/_project/report/delta_pi_only_auc.md (diagnostic revision)
- Source value: Δπ-only diagnostic subgroup-level AUC = 0.865 (rounds to 0.86)
- Resolution: The data audit incorrectly matched paper's AUC=0.86 against exp-005's signed-product diagnostic (AUC=0.833). The paper's Proposition 2 uses the Δπ-only diagnostic |δ_s|/((1-2π̄)·π_s)>1, which achieves AUC=0.865 per the diagnostic revision analysis. The coincidence that exp-005's subgroup_correlation=0.86 led the audit to conclude it was a mix-up, but AUC=0.86 is the correct, traceable value for the Δπ-only diagnostic.
- Paper locations: unchanged (experiments.tex:73, method.tex:52, limitations.tex:21, appendix.tex:275 caption)

## Issue 2: AUC=0.82 (asymmetric diagnostic)
- Source CSV: artifacts/_project/data/exp_asym_diag_v2.csv
- Source analysis: artifacts/_project/report/exp_asym_diag_v2_analysis.md
- Source value: All-subgroup Sym AUC = 0.6571 (rounds to 0.66). tau_s>0 only: AUC = 1.0
- Resolution: 0.82 not found in any CSV or analysis file. Replaced with 0.66 (all-subgroup AUC from asymmetric diagnostic analysis on real LLM confusion matrices).
- Paper locations fixed:
  - theory.tex:58 → "AUC decreases from 0.86 to 0.82" → "AUC decreases from 0.86 to 0.66"
  - limitations.tex:23 → "AUC $= 0.82$" → "AUC $= 0.66$"
  - appendix.tex:170 → "AUC $= 0.82$" → "AUC $= 0.66$"

## Issue 3: 74–82% global coverage — NO FIX NEEDED
- Source CSV: artifacts/w8/data/exp_w8_a5_violation.csv
- Source values: global_corrected subgroup coverages below nominal:
  - aligned, n=250, S1: 0.82
  - aligned, n=500, S1: 0.78
  - adversarial, n=250, S0: 0.74
  - adversarial, n=500, S0: 0.78
- Resolution: The 74–82% range IS traceable — it represents the coverage of affected subgroups (those where Δτ_s–δ_s correlation causes global correction to degrade). The audit's "84.5%" was an average across ALL subgroups (including unaffected ones at ~93%), not a subgroup-level value. Since the paper compares EC-HTE's worst subgroup (≥93%) against global's worst subgroups (74–82%), the comparison is fair and accurate.
- Paper locations: unchanged (theory.tex:65, rebuttal_talking_points.md Q6)

## Compilation
- Status: pass
- Output: 29 pages, 0 errors, 0 undefined references
- Warnings: none relevant
