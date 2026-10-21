# research fisher info derivation

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_fisher-info-derivation_20260513T185207_result.json`
- **Structured JSON:** [`ef1d992ed403b39c08c2.json`](../../sessions/ef/ef1d992ed403b39c08c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

LaTeX compiles cleanly (6 pages, no errors).

## Summary

**All three parts complete. All verifications passed.**

### Theorem 1 (verified)
`I(γ) = Σ_ij w_ij τ_ij²` where `w_ij = [(d_j-c_j)·s_ij(1-s_ij)]² / [p_ij(1-p_ij)]`

- MC score variance vs analytic: ratio = 1.0067
- Expected Hessian vs analytic: ratio = 1.0000
- 2PL simplification (`w_ij = p_ij(1-p_ij)`): exact match

### Corollary 1 — AUC scaling (verified)
`E[I(γ)] = W̄·NM·[1/(2(Φ⁻¹(A))²) + π]` — all 5 AUC values within [0.998, 1.001] of theory.

Key insight: in the DGP where σ is determined by AUC (Δ=1 fixed), lower AUC → larger noise σ → larger E[τ²] → MORE conditional Fisher information. This is because the noise creates large τ values that make γ easy to estimate statistically, even though the estimate is less interpretable as a contamination effect.

### Corollary 2 — ME attenuation (verified)
`I_ME/I_oracle = σ_τ²/(σ_τ²+σ_e²)` — all 5 σ_e values match theory within [0.998, 1.002].

### exp-004 comparison
- All tested conditions (AUC ∈ {0.55, 0.80}, N ∈ {20, 50}) successfully detect γ (100% exclude zero).
- Conditional Fisher info predicts detection at all AUC ≥ 0.50 (the bound is never binding at these dimensions).
- Observed CI widths are 1.3× to 4.0× wider than conditional predictions, as expected — the conditional formula assumes other parameters known, while the Bayesian model estimates them jointly.
- The gap is largest at low AUC (ratio 3.7–4.0 at AUC=0.55) where noise-inflated τ creates more confounding with item difficulty.

### Files
- `fisher_info_appendix.tex` — 6-page standalone LaTeX (EMNLP appendix format)
- `verify_fisher_info.py` — pure numpy/scipy verification
- `fisher_info_verification.json` — full numeric results

---
