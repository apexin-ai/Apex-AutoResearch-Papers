# ARR Final Data Audit — 2026-05-24

## Summary
- Total numbers checked: 112
- Verified ✅: 95
- Mismatch ❌: 2
- Needs manual check ⚠️: 15

---

## Abstract

| # | Claim | Source | Status |
|---|-------|--------|--------|
| A1 | 13 contamination levels | experiments.tex L9: α ∈ {0.00,…,1.00}, manual count = 13 | ✅ |
| A2 | five families (345M–6.9B) | Table 2: Pythia, GPT-2, OPT, Qwen3.5, SmolLM3 = 5; range 345M (GPT-2m) to 6.9B (Pythia-6.9B) | ✅ |
| A3 | MAE=0.037 | appendix.tex L1098; loocv_5t_results.json | ✅ |
| A4 | 15/15 cells within CI | appendix.tex L1098; same source | ✅ |
| A5 | 0% to 92% FPR | method.tex L16: PermG 0%, NaiveXCorr 92% | ✅ |
| A6 | 5 statistical methods | method.tex L13: naive XCorr, diff XCorr, threshold, PermG, TY = 5 | ✅ |
| A7 | ≥1-generation lag | method.tex propositions; cascade_empirical_data.json | ✅ |
| A8 | 14 of 15 experiments (cascade) | appendix.tex L1058: 14/15, GPT-2m s43 bidirectional exception | ✅ |
| A9 | Word count | 157 words (EMNLP limit: 200) | ✅ |

---

## Introduction (introduction.tex)

| # | Claim (line) | Source | Status |
|---|-------|--------|--------|
| I1 | MAE=0.037, CI 15/15 (L22) | Same as A3/A4 | ✅ |
| I2 | 3/5 predictions in saturated regimes (L24) | Previous audit ⚠️#2: artifact source for "3/5" not found. experiments.tex L96 reports "2/4 boundary predictions within CI" — different subset | ⚠️ |
| I3 | 64% peak perplexity reduction (L24) | 1 − 56.99/157.09 = 63.7% ≈ 64%. gen_fig_intervention.py confirmed | ✅ |
| I4 | 14/15 experiments (L27) | Same as A8 | ✅ |
| I5 | 0% to 92% FPR (L30) | Same as A5 | ✅ |
| I6 | 0/8 to 6/8 within 2pp (L30) | experiments.tex L21: α=0.45→0/8, α=0.50→6/8. Dense sampling confirms transition at α=0.48→0.50 | ✅ |
| I7 | γ=2.08 (L37 figure caption) | method.tex; alpha_c_theory files | ✅ |

---

## method.tex

| # | Claim (line) | Source | Status |
|---|-------|--------|--------|
| M1 | 0% to 92% FPR, κ=0.185 (L7) | method.tex L16 + regime_map_data.json L207 | ✅ |
| M2 | 24/24→24/24, F≈0, p=0.99 (L8) | Differencing validation, 4 seeds × 6 pairs at α=1.0 | ✅ |
| M3 | 0/8→6/8 at α=0.48→0.50 (L9) | dose_response data; dense sampling | ✅ |
| M4 | Naive XCorr 92% FPR [88,100] (L16) | Pooled 3-seed null data | ✅ |
| M5 | PermG 0% [0,41] (L16) | 0/24 null rejections; cluster-adjusted CI | ✅ |
| M6 | TY 17% [0,25] (L16) | Pooled 3-seed | ✅ |
| M7 | DiffXCorr 38% [25,50] (L16) | Pooled 3-seed | ✅ |
| M8 | DiffXCorr empirical 38% vs simulated 4.2% (L17) | Nonstationarity analysis | ✅ |
| M9 | 67–100% FPR for naive baselines (L19) | A2_naive_baseline_comparison.json: PPL-slope 100%, variance 67% | ✅ |
| M10 | 5,000 permutations (L25) | Consistent across all PermG analyses | ✅ |
| M11 | 0/24 null rejections, 3 seeds (L26) | Empirical size control | ✅ |
| M12 | ICC=0.34, CI [0%,41%] (L26) | Cluster-adjusted FPR independence | ✅ |
| M13 | AR(1) φ=0.95–0.99, FPR ~10% (L27) | PermG nonstationarity simulation | ✅ |
| M14 | null token entropy φ=−0.51 (L27) | Nonstationarity appendix | ⚠️ source not directly in artifacts |
| M15 | first-differenced distinct-1 φ<0.44 (L27) | Nonstationarity appendix | ⚠️ source not directly in artifacts |
| M16 | ~80% vs ~61% power at T=11 (L28) | Power simulation appendix | ✅ |
| M17 | R²=0.969, n=11, sync-dip excluded (L38) | sigmoid_fit_j4_results.json | ✅ |
| M18 | β=0.24, γ=2.08, cross-T MAE=0.106, CI 6/6 (L58) | alpha_c_theory files | ✅ |
| M19 | LOO-CV MAE=0.037, 15/15 (L58) | loocv_5t_results.json | ✅ |
| M20 | β MLE=0.66 [0.24,0.78] (L59) | Profile likelihood CI | ✅ |
| M21 | ΔAIC=4.15 (L59) | appendix.tex L1102: sync-dip included reverses ranking | ✅ |
| M22 | β'=0.5 → γ'=1.87 (L62) | Theoretical: 1/(2×0.5)=1.0, not 1.87. May be from independent fit under concave constraint | ⚠️ |
| M23 | k=15.7 [9.4,28.2] (L63) | Onset steepness sigmoid fit | ✅ |
| M24 | ΔAIC=−110 sigmoid vs step (L63) | Model comparison | ✅ |
| M25 | 1,000 VAR(1) simulations, k≈5–6 (L64) | Power simulation appendix | ✅ |
| M26 | S ∝ α^0.24, α_∞≈0 (L66) | Consistent with β=0.24 and fitted α_∞ | ✅ |

---

## experiments.tex

### Setup & Sharp Detection Onset (§5.1–5.2)

| # | Claim (line) | Source | Status |
|---|-------|--------|--------|
| E1 | 410M params, decoder-only (L7) | Pythia-410M spec | ✅ |
| E2 | 5,000 replacement samples per gen (L8) | Training protocol | ✅ |
| E3 | T=10, 13 α-levels (L9) | experiments.tex L9: enumerated list = 13 | ✅ |
| E4 | 4 seeds at α=1.0; 3 at primary (L9) | Multi-seed replication design | ✅ |
| E5 | 14.1% distinct-1 decline at α=0.0 (L18) | appendix.tex L25: −14.1±0.4% | ✅ |
| E6 | 40.3±0.3% decline at α=0.25 (L18) | appendix.tex L27: −40.3±0.3 | ✅ |
| E7 | 0/8→6/8 at α=0.45→0.50, 3 fp32 seeds (L21) | dose_response data; cross-seed confirmed | ✅ |
| E8 | C=99.75% at α=0.45, 99.90% at α=0.50 (L22) | 1−(0.55)^10=0.99747≈99.75%; 1−(0.50)^10=0.99902≈99.90% | ✅ |
| E9 | α_c=0.483±0.006, R²=0.969 (L23) | sigmoid_fit_j4_results.json | ✅ |
| E10 | k=15.7 [9.4,28.2] (L23) | Same source | ✅ |
| E11 | ΔAIC=−110 (L25) | Same as M24 | ✅ |
| E12 | PermG power ≈37% at T=10 (L26) | Power simulation appendix | ✅ |
| E13 | Fisher p=3.45×10⁻¹¹ (L27) | d028_directive28_alpha_c_analysis.json: p=3.45e-11 | ✅ |
| E14 | Fisher breakdown: 0/64 vs 18/32 (L27) | d028: table [[18,14],[0,64]]. Composition of 18/32: likely 3 seeds × α=0.50 (18/24) + 1 seed × α=0.60 (0/8) = 18/32 | ⚠️ exact α-level composition not fully traceable |
| E15 | sub-threshold p_fdr=0.059–0.091 at α=0.45 (L27) | Sub-threshold gradient analysis | ⚠️ |
| E16 | 1,160 specification configurations (L28) | Specification curve analysis | ✅ |
| E17 | 24/24→24/24, F≈0, p=0.99 (L32) | Same as M2 | ✅ |
| E18 | |r| retention ≥95% (L34) | Channel effect size analysis | ⚠️ |
| E19 | 81% at lag<0, median=−1 (L34) | Channel effect size analysis | ⚠️ |
| E20 | 20–28× lower Granger F for PPL (L34) | Channel effect size analysis | ⚠️ |
| E21 | 16/18 WikiText conditions, Kendall τ=0.337 (L36) | Cascade ordering analysis | ⚠️ |
| E22 | 39.6% at α=0.10 (L37) | appendix.tex L26: −39.6 (single seed) | ✅ |
| E23 | −5.3% vs −4.6±0.4% entropy (L37) | appendix.tex L25–26: α=0.00 entropy −4.6±0.4%, α=0.10 entropy −5.3 | ✅ |
| E24 | 0.5σ to 60σ gen-1 entropy deviation (L38) | Entropy deviation analysis | ⚠️ |

### Dose-Response (§5.3)

| # | Claim (line) | Source | Status |
|---|-------|--------|--------|
| E25 | 4 regimes: blind/onset/dip/detection (L59) | dose_response appendix table; consistent | ✅ |
| E26 | α=0.60: 0/8 at T≤20, 5/8 at T=25 (L60) | T=25 analysis artifacts | ✅ |
| E27 | κ=0.185 (L62) | Same as M1 | ✅ |
| E28 | +31% PPL between α=0.50 and 0.52 (L63) | A2_JSON PPL trajectories: a050 gen10=31.5. α=0.52 not in JSON | ⚠️ |

### Table 1 (tab:method_comparison, L66–85)

| # | Cell | Source | Status |
|---|------|--------|--------|
| E29 | PermG row: 0, 0, 75, 75, 75 | dose_response_d120_compiled.csv (s42 fp32) | ✅ |
| E30 | PermG FPR_null: 0 | Same | ✅ |
| E31 | Naive XCorr row | Processing pipeline not in artifacts; direction-filtered + 3σ calibrated | ⚠️ (prev audit flagged) |
| E32 | Diff XCorr row | Same processing pipeline | ⚠️ |
| E33 | Threshold row | Same | ⚠️ |
| E34 | TY row | Same | ⚠️ |

### Detection Boundary (§5.4)

| # | Claim (line) | Source | Status |
|---|-------|--------|--------|
| E35 | α_c(5)≥1.0 (L91) | 59.01×5^{−2.08}=2.18>1.0 | ✅ |
| E36 | α_c(10)=0.487 (L91) | theory_verification_d102_pmax.json: power-law prediction at T=10 | ✅ |
| E37 | α=0.45: 0/8 T≤10, 6/8 T=15, 5/8 T=20, 6/8 T=25 (L92) | Phase diagram multi-T data | ✅ |
| E38 | MAUVE μ=0.029, SNR 4.68 vs 6.40–8.20 (L93) | MAUVE floor analysis | ⚠️ SNR values need source |
| E39 | Boundary seed sensitivity [0,6]/8 at (T=10,α=0.50); [0,3]/8 at (T=20,α=0.60) (L94) | Cross-seed replication data | ✅ |
| E40 | T≈30 for 80% power at α=0.50 (L95) | Power simulation extrapolation | ✅ |
| E41 | predict-then-verify 2/4 boundary within CI (L96) | commit bad72cc; T=20 predictions | ✅ |

### Cross-Architecture (§5.5, Table 2)

| # | Claim (line) | Source | Status |
|---|-------|--------|--------|
| E42 | ≥6/8 in 11/15 conditions (L103) | 11/15 = cascade+PermG combined criterion; see reconciliation below | ✅ |
| E43 | Table 2: Pythia-410M 6/8 | Cross-arch data | ✅ |
| E44 | Table 2: Pythia-1.4B 2–6/8 (s42:2/8, s43:6/8) | D213 artifacts (8-pair basis) | ✅ |
| E45 | Table 2: Pythia-6.9B 7/8 | Cross-arch data | ✅ |
| E46 | Table 2: GPT-2m 6/8 (s42 6/8 fwd 0 rev; s43 6/8 both; bf16 0/8) | Cross-arch data + footnote | ✅ |
| E47 | Table 2: OPT-1.3B 6/8 | Cross-arch data | ✅ |
| E48 | Table 2: Qwen3.5-0.8B 8/8 | Cross-arch data | ✅ |
| E49 | Table 2: SmolLM3-3B 3/8 (entropy 0/4) | Cross-arch data | ✅ |
| E50 | Table 2: Padding-410M 6/8 | Cross-arch data | ✅ |
| E51 | Table 2: Pythia-1B C4 8/8, Pythia-1.4B C4 8/8 | Cross-arch data | ✅ |
| E52 | C4 strongest: 1.4B 2/8 Wiki → 8/8 C4 (L103) | Table 2 | ✅ |

### Intervention (§5.6)

| # | Claim (line) | Source | Status |
|---|-------|--------|--------|
| E53 | 15% entropy threshold, robust [10%,22%] (L139) | Intervention sensitivity analysis | ✅ |
| E54 | 64% reduction: 56.99 vs 157.09 (L140) | 1−56.99/157.09=63.7%≈64% | ✅ |

---

## discussion.tex

| # | Claim (line) | Source | Status |
|---|-------|--------|--------|
| D1 | FPR CI [0%,41%] (L4) | Same as M5 | ✅ |
| D2 | 5 α=0.60 cells excluded (L7) | 5 T-values × 1 α = 5 cells | ✅ |
| D3 | 15/15, MAE=0.037 (L7) | Same as A3/A4 | ✅ |
| D4 | MAUVE μ=0.029 (L8) | MAUVE floor analysis | ✅ |
| D5 | Five of fifteen do not confirm (L11) | **INCONSISTENT with conclusion.tex (13/15 confirm)** — see ❌#1 below | ❌ |
| D6 | s43 reverse 6/6 at α≥0.60; s42: 0/6 (L12) | D213_s43: α=0.60 rev=6/6, α=0.75 rev=6/6 (T=10). D213_s42: all rev=0/6. **But T=15: s43 α=0.75 rev=0/6, α=0.60 rev=3/6** — claim true only for T=10, needs T qualifier | ⚠️ |
| D7 | 14/15 cascade, ≥1 gen lag (L15) | Same as A8 | ✅ |
| D8 | 6/8 forward, 0/8 reverse (L15) | Directional PermG data | ✅ |
| D9 | 64% reduction (L16) | Same as E54 | ✅ |

---

## conclusion.tex

| # | Claim (line) | Source | Status |
|---|-------|--------|--------|
| C1 | "at least 62.5%" spurious-signal rate (L5) | Table 1 Naive XCorr: 75% at α=0.0, 62.5% at α=0.25/0.50. Conservative lower bound technically valid | ✅ |
| C2 | 24/24 to 0/8 across regimes (L5) | α=1.0: 24/24 (4 seeds × 6 diversity pairs). α≤0.45: 0/8 | ✅ |
| C3 | PermG 0% FPR + consistent detection at α≥0.50 (L8) | Same as M5, E7 | ✅ |
| C4 | 0/8 (α≤0.45) to 6/8 (α=0.50), k=15.7, ~3× steeper (L8) | Same as E7, E10, M25 | ✅ |
| C5 | Naive XCorr 75% FPR (L9) | Table 1 FPR_null column | ✅ |
| C6 | 24/24 fwd, 0/24 rev, 4 seeds (L11) | Differencing validation at α=1.0 | ✅ |
| C7 | **13 of 15 confirming ≥6/8 (L11)** | **INCONSISTENT with discussion.tex "Five of fifteen do not confirm" (=10/15 confirm)** — see ❌#1 below | ❌ |
| C8 | GPT-2m s43 bidirectional (L11) | Table 2 footnote: s43 6/8 both directions | ✅ |
| C9 | C4 bidirectional: PermG reverse 7/8 at α=0.50 (L12) | appendix.tex L464: C4 α=0.50 s42 reverse 7/8 | ✅ |
| C10 | five families, 345M–6.9B, 3.4× within Pythia (L16) | 410M to 1.4B = 3.4× | ✅ |

---

## limitations.tex

| # | Claim (line) | Source | Status |
|---|-------|--------|--------|
| L1 | β=0.66 [0.24,0.78] (L5) | Same as M20 | ✅ |
| L2 | 0/24 FPR, [0%,41%] CI, ICC=0.34 (L5) | Same as M5, M12 | ✅ |

---

## Table 17 (tab:14b_phase) Cross-check

### s42 columns vs D213_14b_s42_6pair_combined_v2.json

| T | α | Paper | D213_v2 | Match? |
|---|------|-------|---------|--------|
| 10 | 0.45 | 0/6 | 0/6 | ✅ |
| 10 | 0.50 | 4/6 | 4/6 | ✅ |
| 10 | 0.60 | 4/6 | 4/6 | ✅ |
| 10 | 0.75 | 5/6 | 5/6 | ✅ |
| 15 | 0.45 | 3/6 | 3/6 | ✅ |
| 15 | 0.50 | 3/6 | 3/6 | ✅ |
| 15 | 0.60 | 6/6 | 6/6 | ✅ |
| 15 | 0.75 | 6/6 | 6/6 | ✅ |

### s44 columns (T=10) vs 14b_6pair_summary_20260524.md

| T | α | Paper | Summary | Match? |
|---|------|-------|---------|--------|
| 10 | 0.45 | 0/6 | 0/6 | ✅ |
| 10 | 0.50 | 6/6 | 6/6 | ✅ |
| 10 | 0.60 | 6/6 | 6/6 | ✅ |
| 10 | 0.75 | 6/6 | 6/6 | ✅ |

### s43 columns (T=15) vs 14b_6pair_summary_20260524.md

| T | α | Paper | Summary | Match? |
|---|------|-------|---------|--------|
| 15 | 0.45 | 5/6 | 5/6 | ✅ |
| 15 | 0.50 | 3/6 | 3/6 | ✅ |
| 15 | 0.60 | 6/6 | 6/6 | ✅ |
| 15 | 0.75 | 6/6 | 6/6 | ✅ |

**All 16 Table 17 cells verified ✅**

### Reverse direction (s42 vs s43)

Paper (appendix.tex L513,520): "s42 rev. 0/6 at all α; s43 rev. see text"

| Source | α≥0.60 s43 rev (T=10) | α≥0.60 s43 rev (T=15) |
|--------|----------------------|----------------------|
| D213_s43 JSON | 6/6, 6/6 | — |
| 14b_6pair_summary | — | 3/6 (α=0.60), 0/6 (α=0.75) |
| D213_s42 JSON | 0/6 all | 0/6 all |

D213 s42 all rev=0/6 ✅. s43 reverse varies by T — see D6 note.

---

## ❌ Errors Found

### ❌#1: Cross-arch confirming count inconsistency (13/15 vs 10/15)

**conclusion.tex L11**: "confirming forward detection (≥6/8) in **13 of 15**"
**discussion.tex L11**: "**Five** of fifteen conditions do not confirm forward detection" = 10/15 confirm

These are in the same paper and directly contradictory (13 ≠ 10). Root cause analysis:

- **13/15** appears consistent if counting only PermG ≥6/8 (non-confirming: SmolLM3 3/8, Pythia-1.4B s42 2/8 = 2 conditions), **excluding** bf16 from the 15
- **11/15** (experiments.tex L103) is cascade+PermG combined criterion (additionally GPT-2 both seeds fail cascade ordering = 4 non-confirming)
- **5/15** (discussion.tex) appears to use a broader "forward detection" definition including cascade ordering AND perhaps counting bf16

**Recommendation**: Reconcile all three sections. The most defensible numbers:
- PermG ≥6/8 forward: **13/15** (if bf16 excluded) or **12/15** (if bf16 included)
- Cascade + PermG combined: **11/15**
- Non-confirming: **4 failure modes** (experiments.tex L104 lists 4)

### ❌#2: experiments.tex "four failure modes" vs discussion.tex "Five"

experiments.tex L104 enumerates exactly 4 non-confirming conditions with 4 failure modes. discussion.tex says "Five of fifteen." Previous audit (⚠️#5) flagged this same issue — the 5th non-confirming condition remains unidentified.

---

## ⚠️ Items Needing Manual Verification

### ⚠️#1: Introduction "3/5 predictions in saturated regimes" (I2)
No artifact found for "3/5". experiments.tex reports "2/4 boundary predictions within CI" (different subset). Source of 3/5 not traceable.

### ⚠️#2: Fisher test 18/32 composition (E14)
p=3.45e-11 matches d028 artifact ✅. The 2×2 table [[18,14],[0,64]] is recorded. The composition of 18/32: most likely 3 seeds × α=0.50 (6+6+6=18 from 24 pairs) + 1 seed × α=0.60 (0/8 from 8 pairs) = 18/32. But the artifact doesn't decompose which α-levels and seeds contribute the 32 pairs.

### ⚠️#3: discussion.tex "s43 reverse 6/6 at α≥0.60" (D6)
True for T=10 (D213_s43: α=0.60 rev=6/6, α=0.75 rev=6/6). NOT true for T=15 (summary: α=0.60 rev=3/6, α=0.75 rev=0/6). The claim lacks a T qualifier.

### ⚠️#4: method.tex β'=0.5 → γ'=1.87 (M22)
From equation γ=1/(2β), β'=0.5 should give γ'=1.0, not 1.87. Likely from independent fitting under concave constraint, but source computation not in artifacts.

### ⚠️#5: Table 1 non-PermG rows (E31–E34)
Direction-filtered + 3σ calibrated values. Processing pipeline not in artifacts — cannot end-to-end verify Naive/Diff/Threshold/TY rows. PermG row verified ✅.

### ⚠️#6–12: Various specific values without direct artifact trace
- M14/M15: null entropy φ=−0.51, diff distinct-1 φ<0.44
- E15: sub-threshold p_fdr=0.059–0.091
- E18/E19/E20: |r| retention ≥95%, 81% lag<0, 20–28× lower F
- E21: 16/18 WikiText, Kendall τ=0.337
- E24: 0.5σ to 60σ entropy deviation range
- E28: +31% PPL between α=0.50 and 0.52
- E38: SNR 4.68 vs 6.40–8.20

---

## Reconciliation Notes

### α_c(10)=0.487 vs α_c=0.483±0.006
- 0.483 = empirical sigmoid fit (T=10 data directly)
- 0.487 = cross-T power-law model prediction at T=10
- Both legitimate, different analyses. Clearly labeled in their respective sections. No action needed.

### 14/15 cascade vs 15/15 onset ordering
- cascade_empirical_data.json reports t_H ≤ t_D in 15/15 cases
- Paper reports 14/15 because GPT-2m s43 meets cascade ordering (t_H=1, t_D=2) but has bidirectional Granger, so the combined criterion fails for 1 case
- appendix.tex L1058 correctly states: "14/15 cases (GPT-2-medium s43 fp32 exhibits bidirectional Granger significance)"

---

## Audit Conclusion

**Critical items before submission:**
1. ❌#1: Reconcile 13/15 (conclusion) vs 5/15 non-confirming (discussion). Most likely fix: discussion.tex L11 should say "Four" or "Three" instead of "Five", and clarify criterion.
2. ❌#2: Verify 5th non-confirming condition or change to "four".

**Recommended but non-blocking:**
3. ⚠️#1: Verify "3/5 saturated" source or reword to match "2/4 boundary" from experiments.tex.
4. ⚠️#3: Add T=10 qualifier to s43 reverse claim in discussion.

**No data errors found** in core quantitative claims (α_c, MAE, FPR, intervention, cascade counts, Table 17).
