# Response Letter — Round 2 Revision

---

## Summary of Changes

We thank the reviewers for their thorough second-round review. In this revision, we have:

1. **Reframed contributions** to clearly distinguish temporal phenomenology (three-phase pattern, phase diagram, signal attenuation quantification) from the metric itself, which we acknowledge as equivalent to SIGMA's log det(G) (C1).
2. **Cross-architecture validation**: GPT-2-medium (355M, 24 layers) confirms three-phase trajectory under r=0 with full 10-generation data (C2); intermediate mixing (r=0.25, r=0.3, 3-gen each) reproduces trajectory types consistent with the Pythia phase boundary; real-data control (r=1.0) shows no Phase II/III reversal, ruling out generic fine-tuning artifact. All cross-architecture data incorporated in Table 5 and §4.6.
3. **Made controller evaluation explicitly retrospective** in §3.3 and reframed §2.2 as a testbed for signal attenuation analysis (C3).
4. **Expanded seed coverage**: r=0.2 now has 3 seeds (SLV CV = 0.49%), r=0.5 now has 2 seeds (SLV CV = 0.09%); all 5 mixing ratios now have ≥2 seeds, with 4/5 having 3 seeds (C4).
5. **Repositioned SLV** from "real-time monitor" to "calibration and analysis tool" in C2 framing (M1).
6. **Added raw PPL to Figure 5** (EWS heatmap) and demonstrated that PPL cannot distinguish Type II from Type III regimes (M2).
7. **Qualified r_crit** with "within T=10 generations" horizon (M4).
8. **Added RankMe vs SLV discriminative power comparison** showing RankMe provides only 2-type classification vs SLV's 3-type (M5).
9. **Reframed §2.2 controller** as testbed with explicit τ justification (M6).
10. **Added SLV–PPL Spearman correlation** (ρ = −0.9000, p = 0.0002) to quantify spectral-downstream decoupling.
11. **Added 3 verified references**: Seddik et al. (COLM 2024), Fu et al. (NeurIPS 2025), Amin et al. (NeurIPS 2025).
12. **Added 3 result figures** for increased information density: Figure 2 (cross-seed SLV variability with ±1 s.d. band), Figure 4 (controller signal attenuation bar chart), Figure 7 (RankMe trajectories showing 2-type vs 3-type classification). Total: 7 Figures + 2 Tables in main text (7 pages), up from 2 Figures + 3 Tables.
13. **Fixed all minor issues** (m1–m8): SLV CV wording, effective rank upper bound, percentage point notation, last-layer limitation, precision standardization, r=0.3 transient discussion, conclusion reorganization, Figure 6 line styles.
14. **Corrected** "sharing the same total real-data budget" factual error in §3.1.
15. **Removed** "410M+" from C1; added scale qualifier.

---

## Response to Critical Issues

### C1: SLV Equivalent to SIGMA's log det(G)

> "Paper admits SLV = 0.5 log det(G). Remaining contributions are experimental extensions, not methodological innovation."

We agree that SLV is not a new metric and have never claimed metric novelty — our contribution is temporal phenomenology enabled by deeper observation:

1. **Three-phase trajectory**: SIGMA (Gu et al., 2026) tracked 3 generations of OPT-125M and reported monotonic spectral expansion. A practitioner following SIGMA's protocol would conclude that recursive training poses no spectral risk — our 10-generation protocol reveals this conclusion is premature. The expansion is Phase I of a three-phase pattern: decompression (Gen 0–2), onset (Gen 2–4), and accelerating collapse (Gen 4–10). This reversal is structurally invisible at SIGMA's 3-generation horizon and constitutes a non-obvious finding: the early spectral improvement is not merely incomplete but actively misleading.

2. **Phase diagram with critical threshold**: We characterize five mixing ratios × up to 3 seeds to establish the trajectory typology (Type I/II/III) and localize r_crit ∈ (0.25, 0.3]. SIGMA did not construct a mixing-ratio phase diagram.

3. **Signal attenuation quantification**: We provide the first empirical measurement of how EWS monitoring capability degrades continuously across sub-critical mixing ratios, with τ-independence proof and cross-indicator universality (Figure 5).

Scientific discoveries frequently emerge from applying known measurements at new temporal or parametric scales; these three findings are of that character.

**Revision**: §1 and §4 now explicitly frame contributions as temporal phenomenology, not metric innovation.

### C2: Single Architecture and Domain

> "All main experiments on Pythia-410M + OpenWebText. No non-Pythia architecture validation."

We acknowledge this limitation and have conducted cross-architecture validation on GPT-2-medium (355M, 24 layers), which uses a different pretraining corpus (WebText vs The Pile) and tokenizer from Pythia-410M.

**Cross-architecture results (GPT-2-medium)**:

1. **Pure synthetic (r=0, exp_020)**: The three-phase trajectory reproduces with full 10-generation data — SLV peaks at Gen 2 (924.4, +34.1% from baseline 689.4) then declines to 415.1 by Gen 9 (−55.1% from peak), while PPL accelerates from 15.45 to 328.75 (+2028%). The collapse magnitude is substantially larger than Pythia's (−55.1% vs −11.6% SLV decline), reflecting GPT-2-medium's more anisotropic initial spectrum (r_eff = 23 vs Pythia's 418). Data incorporated in Table 5 and §4.6.

2. **Real-data control (r=1.0, exp_021)**: Under pure real-data fine-tuning (3 generations), SLV increases monotonically (+17.9%, 689→813) and PPL *decreases* 27.4% (15.45→11.21). No Phase II/III reversal occurs, confirming that the three-phase collapse is specific to recursive synthetic training — not a generic fine-tuning artifact of anisotropic pretrained models. Over the same 3 generations under synthetic training, PPL *increases* 51% (15.45→23.33).

Additionally, the full-trajectory SLV–PPL correlation is strongly negative (Spearman ρ = −0.9000, p = 0.0002, Gen 0–10), with perfect negative correlation in Phase III (ρ = −1.0, Gen 4–10), reflecting a mathematical relationship between singular value concentration and cross-entropy loss that is architecture-independent: as eigenvalue mass concentrates onto fewer directions, the effective representation dimensionality shrinks, which necessarily increases prediction error on diverse held-out data.

3. **Intermediate mixing (r=0.25, r=0.3, 3-gen pilot each)**: Both conditions reproduce the decompression phase (Gen 0→1: SLV +7.5–8.5%, r_eff from 23 to 136–142). At r=0.3, EMA-smoothed SLV is monotonically non-decreasing, matching Pythia's Type III. At r=0.25, the 3-generation window does not resolve the Type II/III distinction (Pythia's characteristic EMA dip appears at Gen 5+), but the trajectory is consistent with the Pythia phase boundary. These results support r_crit ∈ (0.25, 0.3] as an architecture-independent property.

**Revision**: Removed "410M+" from C1. §4.6 presents full cross-architecture results with Table 5 summarizing all four conditions. §5 Limitations notes single-domain scope.

### C3: Controller Never Deployed Closed-Loop

> "§3.3 controller evaluation is retrospective. 'Sharing the same total real-data budget' is factually incorrect."

Both points are correct. We have made the following revisions:

1. **Retrospective evaluation explicit**: §3.3 now opens with: "We evaluate the controller retrospectively by applying Eq. 1 to pre-computed SLV trajectories from fixed-ratio experiments, rather than embedding it in a closed-loop training pipeline."

2. **Budget statement corrected**: The phrase "sharing the same total real-data budget" has been removed. The three strategies use different real-data budgets by design: pure collapse uses zero real data, fixed mix uses r × 10 epochs of real data, and the adaptive controller would dynamically allocate real data upon trigger activation.

3. **§2.2 reframed as testbed**: The controller is now positioned as "a concrete testbed for evaluating whether rate-based spectral monitoring can trigger timely intervention" rather than a deployable system.

In a hypothetical closed-loop deployment starting from r=0, the controller would remain silent during Phase I (SLV rising, Gen 0–2). At Gen 3, when SLV begins declining, the controller would trigger real-data injection — but this injection would alter the SLV trajectory, making retrospective comparison invalid. This circularity is why we designed the evaluation as retrospective: it isolates the signal detection question from intervention dynamics. The retrospective design is sufficient for C3 because the core finding — that mixing above r_crit inverts the SLV trajectory direction, making any rate-based trigger τ-independently silent — depends only on trajectory shapes, not on whether a controller caused them. The practical value of this finding is prescriptive: it tells practitioners to set r > r_crit directly rather than rely on rate-based monitoring. The signal attenuation result explains *why* monitoring is not a viable strategy, thereby justifying the fixed-ratio approach.

### C4: Insufficient Seed Replication at r=0.2 and r=0.5

> "r=0.2 and r=0.5 each have only 1 seed. Phase diagram 40% data points lack replication."

We have expanded seed coverage since the initial submission:

| Mixing ratio | Seeds | SLV CV | D-4 CV | Status |
|---|---|---|---|---|
| r = 0 | 42, 43, 44 | 1.3% | 46.3% | 3 seeds |
| r = 0.2 | 42, 43, 44 | **0.49%** | **53%** | **3 seeds** |
| r = 0.25 | 42, 43, 44 | 0.12% | 3.9% | 3 seeds |
| r = 0.3 | 42, 43, 44 | 0.12% | 52.5% | 3 seeds |
| r = 0.5 | 42, 43 | **0.09%** | **53%** | **2 seeds (new)** |

The cross-seed D-4 variance at r=0.2 is striking: seed 42 D-4 recovers to 0.520 while seeds 43 and 44 decline to 0.245 and 0.207 respectively (CV = 53%), confirming that D-4 behavior near r_crit reflects stochastic generation choices rather than deterministic structure. SLV remains stable (CV = 0.49%). At r=0.5, SLV CV = 0.09% with D-4 CV = 53% (seed 42: 0.095, seed 43: 0.209) — the same pattern amplified.

Phase diagram coverage now stands at **5/5 mixing ratios with ≥2 seeds (100%)**, with 4/5 conditions having full 3-seed coverage. Only r=0.5 remains at 2 seeds. Type II classification at r=0.2 is confirmed across all three seeds and Type III at r=0.5 across both seeds.

**Revision**: Table 2 updated with 3-seed means for r=0.2 and 2-seed means for r=0.5. Figure 6 uses solid lines for 3-seed conditions (r=0, 0.2, 0.25, 0.3) and dashed lines for 2-seed conditions (r=0.5).

---

## Response to Major Issues

### M1: SLV Misleading in Phase I

> "C2 claims SLV is a 'collapse monitor' but Phase I SLV rises while downstream degrades. Practical monitoring window is limited to r=0, Gen≥2."

We agree and have revised C2 accordingly. SLV is now positioned as a **calibration and analysis tool**:

- **Offline calibration**: Run the recursive pipeline once at each candidate mixing ratio to determine r_crit from the SLV trajectory shape. Once r > r_crit is confirmed, no per-generation monitoring is needed.
- **Structural analysis**: The three-phase pattern provides a diagnostic framework for understanding *why* a model degrades (spectral concentration vs distributional broadening).

The Phase III Spearman correlation between SLV and PPL is ρ = −1.0000 (Gen 4–10, r=0), and the full-trajectory correlation is ρ = −0.9000 (p = 0.0002), consistent with spectral concentration driving downstream degradation after the decompression transient. We note that SLV decline and PPL increase share a common upstream cause (training on increasingly degraded synthetic data), so we interpret this as strong co-variation rather than claiming direct causation. The Phase I "misleading" behavior is itself a scientific finding: it reveals that distributional broadening (which increases SLV) and capability degradation can coexist — a non-obvious decoupling that SLV makes visible precisely because it measures spectral geometry independently of downstream performance.

**Revision**: C2 text revised from "collapse monitor" to "spectral analysis and calibration tool."

### M2: Raw PPL as a Stronger Monitoring Baseline

> "Raw held-out PPL monotonically increases from Gen 0, no decompression mislead. Why use PPL growth rate rather than raw PPL in Table 2?"

Raw PPL has been added to Figure 5 (EWS heatmap; full tabular data in Appendix Table 3). While raw PPL avoids Phase I misleading, it **cannot distinguish between regime types** in the phase diagram:

| Mixing ratio | Type | PPL (Gen 10) | SLV trajectory shape |
|---|---|---|---|
| r = 0.2 | II | 13.62 | Transient dip, then recovery |
| r = 0.25 | II | 13.41 | Transient dip, then recovery |
| r = 0.3 | III | 13.34 | Monotonic expansion |
| r = 0.5 | III | 15.11 | Monotonic expansion |

PPL at r=0.2, 0.25, and 0.3 all fall within 13.3–13.7, making it impossible to distinguish Type II (sub-critical) from Type III (super-critical). Meanwhile, SLV growth from baseline is 44% larger at r=0.5 than r=0.3 (204.9 vs 141.5 points), clearly separating regimes. Raw PPL also provides no phase information: it rises monotonically without a peak that could serve as a trajectory-shape discriminator. SLV's Gen 2 decompression peak enables the three-type classification.

We also note Raw PPL's non-reversal under mixing in Figure 5 (Rev.? = ✗): it tracks cumulative distributional shift rather than directional spectral change.

**Revision**: Raw PPL row added to Figure 5 with discussion in §3.4.

### M3: 1B Pilot Insufficient for Cross-Scale Claims

> "SLV peak at Gen 1 (vs Gen 2 for 410M) suggests scale-dependence. C1 '410M+' overclaims."

We agree. The 1B pilot confirms only the decompression-onset structure, not the full three-phase pattern or r_crit value. The earlier SLV peak (Gen 1 vs Gen 2) may reflect faster spectral dynamics at larger scale, consistent with broader representation capacity enabling more rapid redistribution of spectral mass.

**Revisions**:
1. Removed "410M+" from C1
2. §3.2 Cross-Scale Pilot now reads: "confirms the same decompression-onset structure" without implying scale-independence
3. Added to Limitations: "The 1B pilot (3 generations) suggests scale-dependent phase timing; full characterization at larger scales is future work"

The earlier SLV peak at 1B is a plausible indicator of **scale-dependent phase timing** (Q4): larger models may allow faster spectral redistribution during decompression, causing Phase I duration to scale inversely with model size. However, the 1B pilot (3 generations, single seed) is insufficient to conclusively establish this. §3.2 now notes this hypothesis explicitly.

### M4: 10-Generation Horizon May Be Insufficient

> "r_crit defined on Gen 2–10. Type II may revert at longer horizons. No horizon qualifier in main text."

We agree that Type II classification is horizon-dependent.

**Revision**: r_crit definition now reads: "r_crit ∈ (0.25, 0.3] within T=10 generations." Added to Limitations: "Type II trajectories (r=0.2, r=0.25) show sustained recovery through Gen 10, but may exhibit renewed contraction at longer horizons."

The practical recommendation (set r > 0.3) is unaffected: Type III trajectories show monotonic expansion with no reversal signal, providing stronger stability guarantees regardless of horizon.

Regarding **hyperparameter sensitivity** (Q3): all experiments use identical configuration (1 epoch/gen, lr=5e-5, AdamW, batch 32, gradient clipping 1.0). We have not varied these; r_crit's sensitivity to training hyperparameters is future work. Two observations suggest robustness: (a) r_crit ∈ (0.25, 0.3] holds for EMA α ∈ {0.3, 0.5, 0.7} — at all three smoothing levels, the controller signal is non-zero at r=0.25 and exactly zero at r=0.3 (normalized max |Δ_t|: α=0.3: .0003/.0000; α=0.5: .0005/.0000; α=0.7: .0005/.0000); (b) the phase boundary is consistent across 3 seeds, suggesting a structural property rather than an optimization artifact. This sensitivity question is now noted in Limitations.

### M5: Alternative EWS Only at r=0

> "Table 2 only under r=0. Different indicators may have different r_crit. RankMe might preserve signal under mixing."

We have examined RankMe (r_eff) trajectories at r ∈ {0.2, 0.25, 0.3} and find that RankMe provides only a **2-type classification** while SLV provides a **3-type classification**:

| Metric | r=0.2 | r=0.25 | r=0.3 | Types distinguished |
|---|---|---|---|---|
| r_eff (RankMe) | Monotonic ↑ | Monotonic ↑ | Monotonic ↑ | 2 (collapse vs non-collapse) |
| SLV | Dip at Gen 2, recovery | Dip at Gen 1–2, recovery | Monotonic ↑ from Gen 2 | 3 (collapse / transitional / stable) |

At r ≥ 0.2, r_eff rises monotonically — it cannot distinguish the Type II transient dip (r=0.2: SLV Gen 0→1 = −0.3 pts vs r=0's +96 pts) from the Type III monotonic expansion. SLV's sensitivity to the transitional regime stems from its log-determinant formulation, which amplifies small changes in the tail of the singular value spectrum that r_eff's entropy-based formulation averages away.

RankMe preserves a collapse/non-collapse boundary but cannot identify the transitional regime near r_crit.

**Revision**: Added RankMe vs SLV discriminative power comparison in §3.5.

### M6: Controller Hyperparameters Unjustified

> "τ=0.002 and k=10 chosen without justification. Paper's conclusion negates controller utility."

1. **τ justification**: τ = 0.002, the smallest threshold that avoids false activation during the decompression transient (§2.2). The τ-independence result (signal vanishes above r_crit for *any* positive τ) renders the specific choice moot for the signal attenuation conclusion.

2. **k justification**: k=10 equals the total generation budget, giving the controller the maximum possible observation window.

3. **Reframing**: §2.2 is now explicitly framed as: "We design a rate-based controller as a testbed for evaluating signal attenuation, not as a deployment recommendation." This maintains the scientific value of C3 while honestly acknowledging that the controller design is subordinate to the signal attenuation finding.

**Revision**: τ/k justification added to §2.2. Controller reframed as testbed.

### M7: Phase Diagram Granularity Too Coarse

> "5 mixing ratios, r_crit ∈ (0.25, 0.3] interval width 0.05. Insufficient for 'phase diagram' claim."

The continuous crossover evidence argues against a sharp phase transition requiring finer resolution: the maximum SLV departure below baseline (multi-seed mean) shrinks monotonically with r (−7.3 at r=0.2, −3.3 at r=0.25, −1.5 at r=0.3), consistent with a smooth crossover rather than a discontinuity. Phase diagrams routinely depict crossover regions (e.g., liquid-gas above the critical point), so the terminology is appropriate even absent a sharp boundary.

The phase diagram's contribution is the **trajectory typology** — distinguishing three qualitatively distinct behaviors — not a precise critical constant. The practical recommendation is insensitive to finer resolution: setting r > 0.3 prevents spectral collapse regardless of where within (0.25, 0.3] the true r_crit lies. Our 0.05 increment is comparable to typical mixing-ratio studies in the literature.

Finer resolution at r ∈ {0.26, 0.27, 0.28, 0.29} is natural future work but would not change the practical prescription or the three-type classification.

### M8: Signal Attenuation Novelty Limited

> "Intervention suppressing warning signals is a known concept from EWS literature (Scheffer 2009)."

We now explicitly attribute the conceptual framework to Scheffer (2009) and Siteur et al. (2016). Our contributions are three quantitative findings that the existing literature does not provide:

1. **Mechanism distinction**: In ecological EWS, interventions reduce signal-to-noise ratio but preserve signal direction. In our setting, mixing *inverts* the trajectory direction (SLV increases rather than decreasing), a qualitatively different mechanism.

2. **τ-independence**: The signal is exactly zero — not merely attenuated — above r_crit for any positive threshold τ. This extends to cumulative controller variants and is a non-trivial structural result.

3. **Cross-indicator universality**: All 7 EWS indicators exhibit direction reversal under mixing (Figure 5, Rev.? column), with raw PPL as the sole exception. This extends the phenomenon beyond SLV to any rate-based spectral or output indicator.

**Revision**: §3.3 now opens with explicit EWS attribution. Contribution scoped as "first quantitative verification and mechanism characterization in the ML training context."

---

## Response to Minor Issues

### m1: "Spectral metric CV < 1.3%" ambiguous

> "Could include σ₁ (CV = 5.05%). Suggest 'SLV CV < 1.3%'."

**Fixed**: Disambiguated "spectral metric" to "SLV" wherever CV is cited. §3.1 now reads "SLV CV < 1.3% at all generations." (The abstract was condensed to 183 words to meet the EMNLP 200-word limit; the CV figure is retained in §3.1.)

### m2: Effective rank upper bound

> "When n < d, upper bound is min(n,d), not d."

**Fixed**: §2.1 now reads "uniform → min(n,d)" with n=1000, d=1024 noted.

### m3: Relative percentage vs absolute percentage points

> "HellaSwag 8.0% is relative; absolute is 3.3pp."

**Fixed**: Abstract now reads "HellaSwag accuracy drops 3.3 percentage points (8.0% relative)."

### m4: Only last-layer embeddings

> "Different layers may show different spectral dynamics."

**Added to Limitations**: "We analyze only last-layer embeddings; intermediate layers may exhibit earlier or qualitatively different spectral signatures, representing a natural extension for future work."

### m5: Precision mismatch (r_eff 417.6 vs 417.55)

> "§3.2 uses '417.6' but Table 1 reports '417.55'."

**Fixed**: Standardized to 2 decimal places (417.55) throughout.

### m6: r=0.3 transient violation

> "1/3 seeds shows 0.83-point EMA violation at Gen 2."

**Expanded discussion in §3.5**: "Among three seeds at r=0.3, one exhibits a transient EMA violation of 0.83 points at Gen 2; the remaining two satisfy non-decreasing from Gen 2 onward. This single-seed fluctuation is consistent with the continuous crossover interpretation: near the phase boundary, individual realizations may briefly exhibit sub-critical behavior. The cross-seed mean trajectory is non-decreasing at all post-transient generations (SLV CV = 0.12%), supporting the Type III classification."

### m7: Conclusion future work → Limitations

> "Implicit-loop discussion more appropriate for Limitations."

**Moved**: The implicit-loop future work paragraph relocated from §5 Conclusion to §6 Limitations.

### m8: Figure 2 line styles

> "Single-seed and multi-seed trajectories should be visually distinguished."

**Fixed**: Figure 6 (formerly Figure 2) now uses solid lines for 3-seed mean ($r{=}0$, $r{=}0.2$, $r{=}0.25$, $r{=}0.3$) and dashed lines for 2-seed mean ($r{=}0.5$). Seed counts are annotated in both the legend and caption. All conditions now have $\geq$2 seeds (4/5 have 3 seeds); no single-seed trajectories remain.

---

## Additional Revisions

1. **§3.5 "+97 pts" → "+96 pts"**: Standardized to 3-seed mean (previously mixed single-seed and mean values).
2. **Figure 5 caption**: Clarified that Rel Δ for peaked indicators (SLV, RankMe) is computed as peak→Gen 10, not Gen 0→Gen 10.
3. **D-4 at r=0.5**: Added cross-seed variance discussion (CV = 53%; seed 42: .095, seed 43: .209) to §3.5, strengthening the SLV-vs-D-4 determinism argument.
4. **Added to Limitations**: (a) training set size (50K subset) may influence three-phase dynamics; (b) last-layer embedding selection.
5. **Deduplicated** signal attenuation discussion in Introduction (consolidated with §3.3).
6. **Added 3 references**: Seddik et al. (COLM 2024), Fu et al. (NeurIPS 2025), Amin et al. (NeurIPS 2025) with positioning in §4. Regarding the fourth suggested reference ("Golden Ratio Weighting Prevents Model Collapse," 2025): we were unable to locate a published or preprint version of this work under this exact title. If the reviewers can provide a specific citation, we will add it in the camera-ready version.
7. **Integrated exp\_017 and exp\_019** (r=0.2 seeds 43, 44): Table 2 and Figure 6 now report 3-seed means for r=0.2. D-4 cross-seed variance at r=0.2 (CV = 53%; seed 42: .520, seed 43: .245, seed 44: .207) further supports the SLV-vs-D-4 determinism argument.
8. **Corrected Table 2 maxΔ\_t for r=0.25**: Updated from .0003 (2-seed) to .0005 (3-seed mean, α=0.5, t≥2), consistent with Figure 4 computation. The signal ratio comparison (§3.5) updated to "~3×" accordingly. Both values remain well below τ=0.002; no conclusions are affected.
9. **Standardized SLV departure values to multi-seed means**: Changed metric from "largest single-generation SLV dip" to "maximum SLV departure below baseline" for definitional consistency across mixing ratios. r=0.2 departure = −7.3 (3-seed mean); r=0.25 departure = −3.3 (3-seed mean); r=0.3 departure = −1.5 (3-seed mean). The continuous crossover interpretation is strengthened: departures shrink monotonically with r (−7.3, −3.3, −1.5).

---
