---
round: 47
review_mode: continue
overall_score: 3.0 (Findings)
timestamp: 2026-05-22T09:32:46.396110+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# Round 47 审稿报告 — gen-depth-fingerprint

**论文**: "Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text"
**Venue**: EMNLP 2026 (ACL Rolling Review, May cycle)
**Deadline**: 2026-05-25
**审稿轮次**: Round 47 (Continue from Round 46)
**Reviewers**: R1 (方法严谨性/实验), R2 (新颖性/完整性)
**论文版本**: v51

---

## Summary

This paper introduces "generation depth" as a measurable property of base-model LLM text and proposes the Differential Depth Response (DDR) framework, which decomposes 7 distributional features into drifting (entropy mean, TTR, hapax ratio), stationary (entropy max, min, tail decay), and intermediate (entropy std) components based on their correlation with recursive generation depth. Using an 8-generator corpus from Wikipedia-seeded text, the authors demonstrate depth classification at 3-class resolution (human/gen-1/gen-2+) with F1=0.762 (handcrafted) or 0.905 (QLoRA, 6-gen subset), and at binary level (gen-1 vs gen-2+) with F1=0.694 under Leave-One-Generator-Out cross-validation. This is a **revision evaluation** — v51 addresses ~60 issues accumulated over rounds 29-46.

---

## Revision Assessment (vs Round 46)

The revision shows **significant and systematic improvement** in framing and presentation. Of ~25 actively tracked issues entering Round 47, both Reviewers confirmed ~16 as RESOLVED, ~6 as PARTIAL, and 2 as STILL_OPEN.

### Issues Confirmed RESOLVED by Both Reviewers

1. **R32-W3 (entropy terminology)**: Table 1 caption now explicitly labels features as NLL-based. **14-round persistent issue finally resolved.**
2. **R42-W1 ("preserved" overselling)**: Discussion §5 uses "both supported" instead of "both confirmed". Abstract uses "approximately preserved".
3. **R39-N2 (page overflow)**: Conclusion fits within page 8. Discussion compressed.
4. **R42-N1 (DDR novelty framing)**: Intro Contribution 1 reads "descriptive empirical finding". Discussion distinguishes descriptive observation from mechanistic hypothesis.
5. **R42-N3 (claim scope)**: Discussion uses "analytical dimension"; Results "comparable rather than advance".
6. **R39-N3 (3-class resolution gap)**: Discussion uses "practical resolution limit under available approaches".
7. **R43-W3 (descriptive vs mechanistic)**: Discussion L5 "testable but unproven" — clear separation.
8. **R34-W1 (base-model scope)**: Intro L4 "in base-model pretraining corpora"; instruction limitation front-loaded throughout Abstract/Intro/Discussion/Conclusion.
9. **R42-N2 (instruction-tuned failure)**: Merged with R34-W1; comprehensive coverage.
10. **R45-W1 (seed-sharing)**: §4.1 reports conservative independent-seed estimate (F1=0.680).
11. **R44-N2 (Abstract overclaim)**: Abstract now presents three-part DDR structure.
12. **R44-W1 (QLoRA protocol)**: Abstract labels "(6-gen LOGO; Appendix)".
13. **R43-W1 (Gemma-2-2B)**: Limitations documents "(binary F1=0.440; gen-1 nearly undetectable)".
14. **R43-W2 (6-gen vs 8-gen)**: Conclusion and Abstract now label subset conditions.
15. **R45-W2 (ordinal methods)**: §4.3 reports CORAL/Frank-Hall negative result.
16. **R45-W3 (perturbation wording)**: Discussion uses "degrades gracefully" with specific numbers.

### Issues Partially Resolved

1. **R44-N1 (cross-model chain confound)**: Results L14 provides three-step rebuttal (LOFO=0.686, single-gen=0.810, +2pp). R1 moved RESOLVED→PARTIAL, R2 moved STILL_OPEN→PARTIAL — **converged from opposite directions**. Per-generator variance decomposition still missing.
2. **R46-W1 (tail_decay TOST)**: Text labels tail_decay as "weakly stationary" — appropriate. But TOST pass rate (61.5%) vs partition stability inconsistency still underdiscussed.
3. **R42-W5 (k-means partition)**: §4.2 has threshold stability + epsilon invariance. R1 acknowledged Round 46 factual error (k-means misread), downgraded from Critical to Warning.

### Issues Still Open

1. **R46-W2 (missing references)**: FineWeb (Penedo et al., 2024), Welleck et al. (2020), membership inference parallel — not yet addressed.

---

## Strengths

**S1. Well-defined novel task** (R1+R2 consensus)
Generation depth classification is a genuinely new problem formulation with practical relevance to corpus provenance auditing. Three concurrent works converging on similar phenomena validates the research direction.

**S2. Rigorous evaluation protocol** (R1+R2 consensus)
LOGO cross-validation is the right choice for cross-generator generalization. Independent-seed control (F1=0.680) and cross-family reference model validation (F1 spread=0.013) address key confounds.

**S3. DDR framework provides genuine empirical insight** (R1+R2 consensus)
The drifting/stationary decomposition, validated by k-means (silhouette=0.660, p=0.030) and TOST equivalence testing, offers interpretable structure beyond classification performance.

**S4. Honest scientific reporting** (R1+R2 consensus)
Transparent proof-of-concept status, downstream null result, instruction-tuning limitation, seed-sharing conservative estimate, and baseline comparability.

**S5. Comprehensive supplementary material** (R2)
25 pages of appendices with systematic ablations.

**S6. Excellent revision responsiveness** (R1+R2 consensus)
v51 addresses ~16/25 tracked issues as RESOLVED across 14+ rounds of feedback.

---

## Weaknesses

### Must-Fix (Consensus)

**W1 [Critical] — DDR remains descriptive without mechanistic grounding** (R42-N1, rounds 42-47)
The DDR framework observes that certain features drift while others don't under recursive generation, but offers no mechanistic explanation for WHY. The nucleus sampling hypothesis (§5) is "testable but unproven" by the paper's own admission. Three concurrent works provide varying degrees of mechanistic insight while DDR stays at the observational level. This limits the paper to Findings-level contribution.
- R1: "descriptive observation insufficient for main conference" (3.0)
- R2: "task definition + multi-faceted convergent evidence exceeds typical incremental work" (3.5)

**W2 [Critical] — Fundamental performance and scope limitations unchanged** (R34-W1, R42-N3, rounds 34-47)
Core empirical results remain: binary F1=0.694 (~30% error rate), 3-class resolution ceiling, base-model-only (instruction-tuning causes DDR structural failure with retraining F1=0.487). Framing improved but structural limitations constrain impact. Residual tension in Table 3/Figure 3 baseline comparison framework.

### Should-Fix

**W3 [Warning] — tail_decay stationarity classification fragile** (R46-W1, rounds 46-47)
TOST pass rate (61.5%) far below entropy_max (99.3%) and entropy_min (97.1%). "Weakly stationary" label appropriate but TOST vs partition stability inconsistency needs explicit discussion. Presentation issue, not structural flaw.

**W4 [Warning] — Cross-model chain confound not fully resolved** (R44-N1, rounds 44-47)
Three-step rebuttal suggestive but not conclusive. Per-generator variance decomposition missing. Both reviewers converged to PARTIALLY_RESOLVED.

**W5 [Warning] — Missing references** (R46-W2, rounds 46-47)
Penedo et al. (2024) FineWeb, Welleck et al. (2020) degeneration, membership inference parallel. R1+R2 agree (1)(3) relevant; (2) optional.

### Minor

**W6 [Info] — k-means partition sensitivity** (R42-W5)
Cohen's d domain-specificity secondary concern. R1's prior factual error acknowledged. Downgraded to Warning/Info.

---

## Reviewer Consensus [AGREE]

1. **DDR contribution level**: Solid empirical contribution, lacks mechanistic depth for main conference. [AGREE on characterization, DIVERGE on threshold]
2. **Revision quality**: Significant and systematic improvement. [AGREE]
3. **Entropy terminology (R32-W3)**: RESOLVED after 14 rounds. [AGREE]
4. **"Preserved" overselling (R42-W1)**: RESOLVED. [AGREE]
5. **Base-model scope (R34-W1)**: Front-loading now adequate. [AGREE]
6. **Page limit (R39-N2)**: Conclusion within 8 pages. [AGREE]
7. **tail_decay labeling**: "Weakly stationary" appropriate. [AGREE]
8. **k-means factual correction**: R1's Round 46 misread should not weigh against the paper. [AGREE]
9. **Descriptive vs mechanistic (R43-W3)**: "Testable but unproven" is correct. [AGREE]
10. **Cross-model chain (R44-N1)**: PARTIALLY_RESOLVED. [AGREE]

---

## Reviewer Divergence [REBUT]

**Overall Score — Excitement gap** (R1: 3.0 vs R2: 3.5)

Only substantive remaining divergence. Both agree on all facts; differ on novelty threshold.

- **R1 (3.0 — Findings)**: "Descriptive finding not exciting enough for main conference. Binary F1=0.694 with ~30% error rate and base-model-only scope limits practical impact. Three concurrent works with mechanistic grounding raise the bar."
- **R2 (3.5 — Borderline Conference)**: "Task definition is genuinely novel. DDR framework with drifting/stationary decomposition provides interpretable structure. Multi-faceted evidence package (statistical testing + classification + cross-domain + perturbation robustness) exceeds typical incremental work."

---

## Questions for Authors

1. Per-generator F1 breakdown across different reference models (beyond aggregate spread=0.013)?
2. tail_decay: relationship between TOST pass rate (61.5%) and k-means partition stability?
3. Is ~3-class resolution a fundamental limit of recursive generation or an artifact of current approaches?

---

## Missing References

1. **Penedo et al. (2024)** — FineWeb data curation
2. **Welleck et al. (2020)** — Neural text degeneration
3. **Membership inference literature** — Methodological parallel (optional)

---

## External Review

Not configured (paperreview_ai.enabled not set).

---

## Visual Layout Check (Non-scoring)

**Status**: Done | 0 critical, 2 warnings, 5 info | Improved from Round 46

**Warnings:**
- Pages 1-2: Two consecutive pages of pure text, no display items. Figure 1 at page 6. [wont_fix — page budget]
- Page 37: Figure 15 ~30% of page, rest whitespace.

**Info:**
- 6 display items in 8 pages (low end for empirical paper)
- Table 1 first display item — limited anchoring value
- Pages 6-7 abrupt rhythm shift (consecutive full-width figures)
- Appendix pp. 24-25 bottom whitespace
- Figure 4 tick labels at ~60% body text size

---

## Overall Assessment

**Score: 3.0 (Findings)** | Confidence: 0.75

| Dimension | R1 | R2 | Consensus |
|-----------|----|----|-----------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Novelty | 2.5 | 3.0 | 2.75 |
| Excitement | 2.5 | 3.0 | 2.75 |
| Presentation | 3.5 | 4.0 | 3.75 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| **Overall** | **3.0** | **3.5** | **3.0–3.5** |

**Rationale**: The paper defines a novel task and provides a solid empirical framework validated by multiple complementary approaches. The v51 revision shows excellent responsiveness (~16/25 issues RESOLVED). However, the core contribution remains **descriptive** — DDR observes but does not explain the drifting/stationary decomposition. Combined with structural limitations (F1=0.694, base-model-only, 3-class ceiling), the paper sits at the Findings threshold.

R2's argument for Borderline Conference has merit — comprehensiveness and honest reporting exceed typical empirical work. The Director concurs with R1 that descriptive-only contribution without mechanistic grounding is more naturally positioned for **Findings**.

**Recommendation**: Findings-track paper. For main conference: need (a) mechanistic explanation, (b) higher performance, or (c) demonstrated downstream utility.

---

## Detailed Comments

### Abstract
Improved. Scope-limited, "approximately preserved", F1 labeled with conditions. QLoRA "(6-gen LOGO; Appendix)". Acceptable density.

### §1 Introduction
Improved. "Descriptive empirical finding". Base-model scope front-loaded. Minor residual: broad contamination motivation before narrowing to analytical scope.

### §2 Related Work
New §2.4 concurrent positioning. Table 46 still checklist-style. Missing Penedo (2024), Welleck (2020).

### §3 Method
Table 1 NLL clarification resolves long-standing issue. Feature selection rationale adequate. Cross-family validation documented.

### §4 Results
§4.1: Independent-seed F1=0.680 reported. §4.2: DDR descriptive framing clear; tail_decay TOST underdiscussed. §4.3: Honest baseline comparison.

### §5 Discussion
"Testable but unproven". "Both supported". Downstream null result honest. "Analytical dimension" appropriate. Perturbation language data-grounded.

### §6 Conclusion
Fits page 8. Claims tempered. "Practical resolution limit".

### Limitations
Base-model scope, scale ≤8.2B, English-only, Gemma-2-2B anomaly. Concise per EMNLP.

---

## Issue Tracker Summary

| Status | Count |
|--------|-------|
| Resolved | 55 |
| In Progress | 2 (R44-N1, R46-W1) |
| Open | 1 (R46-W2) |
| Wont Fix | 5 |
| **Total** | **63** |

---

*Round 47 Consolidated Report — Review Director*
*Reviewers: R1 (方法严谨性), R2 (新颖性/完整性)*
*Cross-sharing: completed (R1 + R2)*
*Convergence: achieved in 1 round*