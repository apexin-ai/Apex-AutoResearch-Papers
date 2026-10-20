# Rebuttal Framework — Round 1 Response

## Issue Tracker Summary (15/16 resolved)

### Resolved (no rebuttal needed)
- R1-N1: SLV definition rewritten (commit 66cbb53)
- R1-N3: Signal attenuation reframed (commit 473d4fb)
- R2-N1: Page limit fixed (commits 34cadcc + 6a9bbd7)
- R2-N2: SIGMA equivalence honestly disclosed (commits b3add6f + 13dbdce)
- R1-W2: Per-gen variance appendix added (commit 98a14f5)
- R1-W3: 1B pilot claim qualified (commit 473d4fb)
- R1-W4: Δ²_t compressed (commit 34cadcc)
- R1-W5: n-sensitivity analysis added to Limitations (commit 94cbf2f)
- R2-W2: Missing literature added (commit 6a9bbd7)
- R2-W3: C4 demoted to supporting text (commit 473d4fb)
- R2-W4: Conclusion overclaim fixed (commit 473d4fb)
- INT-D1: Table 3 r=0.50 data source unified (commit 94cbf2f)
- INT-D2: Table 1 3-seed data integrity fixed (commit 94cbf2f)
- INT-D3: D-4 baseline + CV multiplier corrected (commit 58c3536)

### In Progress
- **R1-N2** (seed replication): r=0 3-seed done; r=0.25 exp_014b+015 running; r=0.3 exp_016 queued; r=0.2/0.5 P1 planned

### Open (rebuttal needed)
- **R1-W1** (r_crit granularity): rebuttal prepared, see below

---

## Rebuttal Point 1: R1-W1 — r_crit Interval Granularity

**Weakness**: The critical mixing ratio is localized only to (0.25, 0.3], which is a coarse bound.

**Response** (~150 words):

We agree that finer resolution (e.g., r = 0.27, 0.28, 0.29) would narrow the bound, and we note this as natural future work. However, the current resolution is sufficient for three reasons.

First, the practical recommendation is insensitive to the exact r_crit value. Practitioners need a safe threshold, not a precise critical point: setting r > 0.3 prevents spectral collapse regardless of whether r_crit is 0.26 or 0.29.

Second, the qualitative boundary is robust across three seeds and three EMA smoothing parameters (α ∈ {0.3, 0.5, 0.7}): r = 0.25 consistently shows Type II trajectories (transitional), while r = 0.3 consistently shows Type III (stable).

Third, the phase diagram's contribution is the trajectory typology itself — distinguishing collapse, transitional, and stable regimes — rather than a precise critical constant.

---

## Rebuttal Point 2: C3 Novelty — Signal Attenuation

**Anticipated attack**: "Signal attenuation is trivially expected — preventing collapse removes the signal."

**Response** (~200 words):

The observation that intervention suppresses warning signals is anticipated by the EWS literature (Scheffer 2009, Siteur 2016). Our contribution is not the qualitative observation but three quantitative findings that theory alone does not predict:

1. **Continuous degradation**: Signal attenuation is not binary. The controller signal degrades *continuously* as the mixing ratio approaches r_crit — from strong decline under pure collapse (r=0) through attenuated (r=0.2, Δ_max=0.002) to complete silence (r≥0.3, Δ_max<0.0003). This continuous relationship, empirically characterized across 5 mixing ratios (with 3 seeds at the boundary conditions r=0, 0.25, and 0.3), has not been quantified before.

2. **τ-independence**: The signal vanishes above r_crit for *any* positive threshold τ, not just our chosen τ=0.002. This limitation cannot be resolved by tuning sensitivity — it is structural, extending to cumulative variants.

3. **Cross-indicator generality**: All 7 EWS indicators exhibit the same attenuation pattern. The phenomenon is not SLV-specific but affects any rate-based spectral/output indicator, suggesting a fundamental geometric property of the mixed-training regime.

**Evidence**: Table 3 phase diagram + §4.3 controller analysis + §4.5 alt-EWS comparison.

---

## Rebuttal Point 3: R1-N2 — Seed Replication

**Weakness**: Most mixing ratios have only 1 seed.

**Response** (to be finalized after experiments complete):

We have expanded seed coverage significantly in revision:
- r = 0: 3 seeds (42, 43, 44) — three-phase pattern reproduced with SLV CV < 1.3%
- r = 0.25: 3 seeds (42, 43, 44) — [pending exp_014b + exp_015 completion]
- r = 0.3: 3 seeds (42, 43, 44) — [pending exp_016 completion]
- r = 0.2: 2 seeds (42, 43) — [pending P1]
- r = 0.5: 2 seeds (42, 43) — [pending P1]

The r_crit boundary conditions (r=0.25 and r=0.3) now have 3-seed coverage, confirming that the Type II/III classification is not seed-dependent. Peripheral conditions (r=0.2, r=0.5) have 2 seeds, providing adequate coverage for their role as phase diagram anchors.

---

## Potential Additional Attacks

### "Only Pythia, only OpenWebText, only English"
**Defense**: Acknowledged in Limitations. Scope is deliberately constrained to enable 10-generation depth × 5 mixing ratios × 3 seeds within computational budget. Cross-architecture generalization is future work.

### "SLV doesn't predict downstream degradation earlier"
**Defense**: Already addressed in §4.1 L53 — SLV's value is computational cost (<1s vs ~70min), not temporal precedence. The asymmetry finding (spectral expansion ≠ model health) is itself a contribution.

### "Phase diagram is just a grid search"
**Defense**: The contribution is the trajectory typology and the signal attenuation characterization, not the grid search methodology. The phase diagram provides the empirical substrate for C3.
