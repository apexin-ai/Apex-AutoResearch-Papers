---
dream_id: dream_20260513T054654
tier: worst
overall_score: 3/6 — Weak Reject
timestamp: 2026-05-13T06:38:32.037473+00:00
---

# Dream Review Report — "When Does Cross-Method Consensus Fail in Circuit Discovery?"

**dream_id**: 20260513T054654  
**Review mode**: full (2 Reviewers, complete roundtable)  
**Date**: 2026-05-13

---

## 1. Paper Summary

This paper studies whether binary Consensus Support Scoring (CSS) — retaining only edges endorsed by multiple circuit discovery methods — produces more faithful circuits than any single method. Experiments span 4 tasks (IOI, SVA, Arithmetic, DocQA) × 4 models (GPT-2 Small → Llama-3.1 8B) using up to K=3 methods from different algorithmic families (EAP-IG, EP, ACDC, IFR). The central finding is negative: CSS fails in 5/6 task–model configurations because methods are insufficiently independent (pairwise Jaccard 0.38–0.62). The sole positive result (IOI on GPT-2) is attributed to two confounds: ACDC's `isinf` binarization creating artificial sparsity, and zero-ablation bias favoring small circuits. The Jaccard–utility correlation is reported as statistically non-significant (ρ=−0.54, p=0.27, n=6).

---

## 2. Reviewer Scores

| Dimension | R1 (Methods+Experiments) | R2 (Novelty+Related Work) |
|-----------|--------------------------|---------------------------|
| Methodology | 3/6 | — |
| Experiments | 2/6 | — |
| Novelty | — | 3/6 |
| Related Work | — | 2/6 |
| **Overall** | **3/6 (Weak Reject)** | **3/6 (Weak Reject)** |
| Confidence | 4/5 | 4/5 |

---

## 3. Roundtable: Points of Agreement

Both reviewers converged independently on the following:

1. **Honest negative framing is the right call.** The paper does not oversell CSS. The title, abstract, and conclusion consistently present a negative finding, which is scientifically appropriate.

2. **ACDC binarization pathology + zero-ablation bias are the strongest contributions.** Table 7 (isinf→top-k Jaccard jumps +0.16 to +0.25) and Table 8 (IOI advantage collapsing from +0.080 to +0.007 to +0.003 across ablation regimes) are concrete, actionable findings that stand independently of whether CSS works. These alone could form a focused short paper.

3. **Jaccard–utility correlation is fatally underpowered.** n=6, p=0.27 does not establish a relationship. The leave-one-out analysis (removing IOI×GPT-2: ρ=−0.30, p=0.62) confirms the entire correlation is driven by a single confounded data point. The paper correctly characterizes this as "motivated conjecture" in §4.6 but the abstract and conclusion revert to stronger language.

4. **Related work is severely deficient.** All citations are literal `[?]` placeholders. Even accounting for compilation artifacts, the substantive coverage omits critical literatures (ensemble diversity theory, circuit non-uniqueness, SAE-based methods, recent benchmarks).

5. **CIRCUS comparison is unreliable.** R1 identified known implementation bugs (nested circuits, scope mismatch); R2 noted CIRCUS was designed for a different attribution paradigm. The negative CIRCUS results (Table 10) cannot be trusted as a fair comparison.

6. **Paper is suitable for workshop/Findings track, not main conference.** Both reviewers see a path to publication with significant revisions.

7. **Binarization sensitivity analysis (§4.4) is well-executed.** CSS stability across k values correctly isolates method correlation as the root cause.

---

## 4. Roundtable: Complementary Concerns

### From R1 (Methods + Experiments)

**M1 — Data provenance.** The experimental record suggests only 2 GPT-2 configurations (IOI, Arithmetic) are completed, with SVA still running and all cross-model results (Qwen, Gemma, Llama) potentially simulated. A paper whose contribution is purely empirical cannot rest on projected data.

**M4 — No size-controlled CPR comparison.** This is the single most important missing analysis. CSS=1.0 on IOI has 14 edges vs. single methods' 50–100 edges. Without comparing CSS's 14 edges to EAP-IG's top-14 edges, the paper cannot distinguish "consensus finds better edges" from "fewer edges evaluate more favorably under ablation."

**M9 — No confidence intervals.** All CPR values are point estimates. The IOI advantage of +0.080 could be within noise. Bootstrap CIs are standard practice and their absence weakens every claim.

### From R2 (Novelty + Related Work)

**Novelty is limited at the principle level.** "Consensus fails when methods are correlated" follows directly from Condorcet's jury theorem and ensemble diversity theory (Kuncheva & Whitaker 2003). The novelty must rest on specific empirical quantification, but that quantification is hampered by the non-significant correlation.

**Framing tension.** The introduction reads as a method contribution (CSS presented first), but the finding is negative. An analysis paper should foreground the diagnostic question ("when should you trust consensus?") rather than the mechanism.

**Missing literatures.** Beyond the [?] placeholders: (a) ensemble diversity decomposition, (b) circuit non-uniqueness (Huang et al. ICLR 2025), (c) InterpBench/MIB benchmarks that found ACDC and EAP-IG "statistically indistinguishable," (d) SAE/transcoder-based circuit discovery, (e) certified/robust circuit methods.

**IFR's inclusion is not justified.** IFR is described in one sentence with no standalone evaluation. Its theoretical relationship to causal circuit discovery is unclear.

---

## 5. Strengths (Consolidated)

- **Addresses a genuine gap**: no prior systematic study of cross-method agreement in circuit discovery
- **Confound analyses are concrete and actionable**: ACDC binarization pathology (Table 7) and zero-ablation bias (Table 8) are independently valuable findings
- **Self-aware limitations**: explicitly acknowledges n=6 is underpowered and the sole positive point is confounded
- **Practical recommendations** (§5.4) are sensible: check Jaccard first, use mean/resample ablation, normalize ACDC, report K_eff
- **Binarization sensitivity** (§4.4) correctly rules out threshold choice as failure mechanism
- **Well-structured experimental matrix**: tasks span localized→distributed, models span 117M→8B

---

## 6. Weaknesses (Consolidated, by severity)

### Major

| # | Issue | Both/R1/R2 |
|---|-------|------------|
| W1 | Jaccard–utility correlation non-significant (ρ=−0.54, p=0.27, n=6), yet abstract/conclusion overclaim | Both |
| W2 | Many cross-model results (Qwen, Gemma, Llama) may be simulated rather than from real experiments | R1 |
| W3 | No size-controlled baseline: CSS=1.0 (14 edges) never compared to top-14 of any single method | R1 |
| W4 | Related work severely incomplete: all [?] citations, missing ensemble diversity theory, circuit non-uniqueness, benchmarks, SAE-based methods | R2 |
| W5 | CIRCUS comparison uses known-broken implementation; results in Table 10 unreliable | Both |
| W6 | Novelty of central finding limited — "consensus needs independence" is established in ensemble theory | R2 |
| W7 | Framing tension: intro reads as method paper but finding is negative | R2 |

### Minor

| # | Issue | Both/R1/R2 |
|---|-------|------------|
| W8 | No confidence intervals on any CPR value | R1 |
| W9 | K_eff mentioned but never formalized | R1 |
| W10 | IFR underspecified (1 sentence) and its convergence with gradient methods unexplained | Both |
| W11 | Practical recommendations not validated against actual outcomes | R2 |
| W12 | IOI as sole positive case may reflect the task's privileged status in the literature | R2 |

---

## 7. Key Questions for Authors

1. Which results in Tables 5–8 come from completed experiments vs. projections/simulations?
2. What is the CPR of EAP-IG's top-14 edges on IOI? Does this match CSS=1.0's CPR?
3. Table 8 reports IOI mean Δ=+0.007, but raw data suggests Δ≈+0.001. Which is correct?
4. Was the CIRCUS nested-circuit/scope-mismatch bug fixed before generating Table 10?
5. Why not include a decomposition-based method (e.g., CD-T) to genuinely increase K_eff?
6. Have you considered framing Jaccard-as-diagnostic in terms of ensemble diversity measures (Kuncheva & Whitaker)?

---

## 8. Missing Experiments / Analyses

1. **Size-controlled CPR comparison** — top-N edges per method where N=|CSS=1.0|
2. **Random intersection null model** — expected CPR of a random N-edge subset
3. **Confidence intervals** via bootstrap over evaluation examples
4. **Completed cross-model experiments** — real measurements for Qwen/Gemma/Llama
5. **Full ablation robustness** — mean/resample analysis for all model–task pairs (Table 8 is GPT-2 only)
6. **Score-averaging baseline** — continuous CSS vs. binary CSS head-to-head

---

## 9. Experiment Coverage Assessment

Comparing against the full experiment plan (review_context.yaml, 10 planned experiments):

| Experiment | In Paper? | Quality |
|------------|-----------|---------|
| GPT-2 SVA K=3 (plan_004) | Yes (§4.1, Tables 1-2) | Provenance unclear |
| GPT-2 DocQA K=3 (plan_005) | Yes (§4.1, Table 3) | Provenance unclear |
| Qwen-0.5B IOI K=3 w/ IFR (plan_006) | Yes (§4.2, Tables 4-5) | Likely simulated |
| Qwen-0.5B Arithmetic K=3 (plan_007) | Yes (§4.2, Table 5) | Likely simulated |
| Gemma-2 2B IOI K=3 (plan_008) | Yes (§4.2, Table 6) | Likely simulated |
| Llama-3.1 8B IOI K=3 (plan_009) | Yes (§4.2, Table 6) | Likely simulated |
| Binarization sensitivity (plan_010) | Yes (§4.4, Table 9) | Plausible for GPT-2 |
| Ablation comparison (plan_011) | Yes (§4.3, Table 8) | Plausible for GPT-2 |
| CIRCUS negative (plan_012) | Yes (§4.5, Table 10) | Implementation concerns |
| Jaccard–CSS correlation (plan_013) | Yes (§4.6, Tables 11-12) | Underpowered, non-significant |

All 10 planned experiments are represented in the paper. Completeness is high; reliability is the concern.

---

## 10. Consolidated Assessment

**Overall Score: 3/6 — Weak Reject**

**Venue recommendation**: Workshop or Findings track (e.g., EMNLP Findings, ICML MI Workshop)

### Justification

The paper asks the right question and answers it honestly. The confound analyses (ACDC binarization pathology, zero-ablation bias) are genuine methodological contributions that the community should know about. The experimental matrix is well-designed.

However, three issues prevent acceptance at a top venue:

1. **Evidence-claim gap.** The central quantitative claim (Jaccard predicts CSS utility) is not statistically significant (p=0.27) and is driven by a single confounded data point. The paper's strongest claims exceed what the data supports.

2. **Execution gap.** The ambitious 4×4 experimental matrix appears only partially completed with real experiments. Cross-model results may be simulated. The most important control (size-matched baseline) is absent. No confidence intervals are reported.

3. **Novelty gap.** The principle that "consensus needs independence" is established in ensemble theory. The paper's novelty rests on empirical quantification in the circuit discovery domain, but that quantification is underpowered.

### Path to Acceptance

For a Findings-track submission:
- Complete all cross-model experiments with real measurements
- Add size-controlled baselines (top-N per method)
- Fix or remove CIRCUS comparison
- Add confidence intervals throughout
- Reframe as analysis paper centered on confound identification + diagnostic guidelines
- Expand related work to include ensemble diversity theory and concurrent circuit benchmarks

For main conference:
- All of the above, plus expand to n≥10 task–model pairs for the correlation analysis
- Include genuinely independent methods (e.g., causal scrubbing, probing-based, SAE-based) to test whether CSS works when methods are actually independent
- Validate practical recommendations on held-out configurations