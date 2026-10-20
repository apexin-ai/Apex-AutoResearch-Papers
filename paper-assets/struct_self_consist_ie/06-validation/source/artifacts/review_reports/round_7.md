---
round: 7
overall_score: borderline
timestamp: 2026-05-15T12:37:15.052031+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Consolidated Review Report — Round 7

**Paper**: Strong Predictors, Weak Selectors: Why Confidence Signals Do Not Scale Structured Information Extraction
**Venue**: EMNLP 2026 Main Conference (ARR May 2026)
**Reviewers**: 2 (R1: 方法严谨性 + 实验设计; R2: 新颖性 + 完整性 + 写作质量)
**Rounds**: 1 (converged after cross-sharing; all critical issues consensual)

---

## Summary

The paper investigates whether confidence signals can identify the best output among multiple LLM-generated candidates for structured IE tasks (NER, RE). It compares five signals from three families—structural (VC, SJ), surface (EM, FK), and model-internal (LP)—across three benchmarks with two 8B-parameter model families. The central finding is the "correlation-selection gap": signals achieve strong quality estimation (ρ up to 0.38, AUROC up to 0.75) but fail at sample selection despite 13–18 pp oracle headroom. A free-form decoding ablation suggests LP score compression is intrinsic rather than a constrained decoding artifact.

The experimental work is extensive and the conceptual distinction between quality estimation and sample selection has genuine value. However, the core contribution framing conflates definitional limitations with empirical findings, key statistical analyses lack multi-seed validation, and the paper's broadest claims (title, abstract) exceed the evidence scope.

---

## Strengths

1. **Conceptual clarity**: The quality estimation vs. sample selection distinction is well-articulated and has practical implications for IE deployment and test-time scaling.

2. **Experimental breadth**: 5 signals × 3 datasets × 2 models with comprehensive ablations (temperature, sample size, free-form decoding, multi-seed QE, diversity stratification, calibration analysis).

3. **Statistical rigor in QE**: Bootstrap CIs (B=10,000), TOST equivalence testing, Bonferroni corrections, 3-seed stability analysis—the quality estimation analysis meets high statistical standards.

4. **Honest hedging**: RE results consistently marked "preliminary, single benchmark" in most locations; Limitations section is thorough and self-aware (7 paragraphs covering scope, scale, ablation limitations).

5. **MBR connection**: Linking consensus-proximity selection to MBR decoding and diagnosing why MBR fails (utility correlates across but not within instances) is insightful and connects to a mature literature. The Eikema et al. (2025) structure-conditional MBR finding corroborates this.

6. **Appendix depth**: 12 supplementary sections with per-relation diagnostics, diversity stratification, LP failure stability analysis, LOO-SJ equivalence proof, calibration reliability diagrams.

7. **Citation integrity**: Both reviewers independently verified all 62 bib entries; 56 confirmed via OpenAlex, no fabricated citations detected.

---

## Weaknesses

### Critical (Must-Fix) — 5 issues, all consensual

**C1. Gap framing conflates definitional and empirical contributions** [Consensus]
Abstract and Introduction present the correlation-selection gap as a unified empirical discovery, but §5 explicitly acknowledges that 4/5 signals fail at selection "by construction" (Layer 1: definitional). The actual empirical contributions are narrower: (a) LP score compression diagnosis (60% instances with range < 0.05), (b) MBR utility-quality misalignment at per-sample level, (c) non-tied subset analysis showing LP becomes significant when compression is mitigated (+2.9 pp, p=0.01). **Action**: Reframe Abstract/Introduction/Contribution 2 — dismiss instance-level failure in one sentence (definitional), then center LP compression + MBR failure as core empirical findings.

**C2. Selection gap lacks multi-seed validation** [Consensus]
The headline finding (LP NER +0.6 pp, p=0.39; Table 3) uses seed=42 only. The 3-seed analysis (Table 10) covers QE metrics but not selection F1. A p=0.39 from a single seed is insufficient to support the paper's central claim. **Action**: Extend 3-seed analysis to Table 3 selection F1; report cross-seed mean±σ and p-value range.

**C3. ε=0.05 "effectively tied" threshold lacks justification** [Consensus]
Table 12 shows a 59× jump from ε=0.01 (1.1%) to ε=0.05 (60.3%), indicating the threshold sits on a steep distribution cliff. "60% of instances effectively tied" appears in the abstract but the 0.05 cutoff has no stated basis. **Action**: Provide LP range CDF; justify ε or replace with continuous measure (within-instance LP-F1 correlation).

**C4. Free-form ablation scope too narrow for claims** [Consensus]
1 dataset × 1 model × 1 seed supports "fundamental challenge" and "intrinsic to the model and task." RE LP selection flips from −0.68 pp (constrained) to +1.69 pp (free-form, Table 14 Panel B), partially contradicting "not an artifact of decoding strategy." NER compression persists. **Action**: Downgrade "fundamental/intrinsic" to "observed in our NER setting"; explicitly acknowledge RE reversal; differentiate NER and RE ablation conclusions.

**C5. Title "Do Not Scale" exceeds evidence scope** [Consensus]
Both models are 8B parameters. The paper's own findings show task difficulty × model capability interaction effects, but only one scale point is tested. The title implies a universal negative result. **Action**: Scope title to "at 8B Scale" or equivalent qualification.

### Warning (Should-Fix) — 8 issues

**W1. RE conclusions inconsistently qualified** [Consensus]
RE analysis uses SciERC alone (preliminary). Abstract and some Discussion passages reference RE results without consistent "preliminary, single benchmark" qualification. R1 corrected R2's factual error (LP negative correlation ρ=−0.410 is WNUT-17 NER, not RE) but agrees with the underlying concern. **Action**: All RE citations carry "(preliminary, single benchmark)" consistently.

**W2. Abstract information density too high** [Consensus]
Abstract packs 5 signal families, 3 datasets, 2 models, 4 metrics, and the gap concept into ~8 sentences. **Action**: Simplify to problem-finding-implication three-paragraph structure; move specific signal names and numbers to Introduction.

**W3. FK independence test near-zero power** [Consensus]
One-sample t-test over n=5 configurations has essentially no statistical power. **Action**: Add permutation test/bootstrap CI, or acknowledge the limitation explicitly.

**W4. VC formula-implementation inconsistency** [Consensus]
Eq. 6 defines continuous QE signal; selection uses majority threshold (>N/2). Table 3 doesn't clarify which. Footnote reports ρ difference (0.252 vs 0.379) but table labeling is ambiguous. **Action**: Clearly label both variants in table captions.

**W5. TOST δ circularly anchored** [Consensus]
δ values anchored to oracle headroom, but oracle headroom is the quantity under investigation. **Action**: Use external standard (IAA variation, deployment threshold) or prominently report breakpoint δ*.

**W6. LP temperature sensitivity missing** [Consensus]
LP—the paper's primary diagnostic target—excluded from temperature comparison (T=0.7 vs T=1.0). Score compression may be temperature-dependent. **Action**: Obtain T=0.7 LP data or discuss this gap more prominently in Limitations.

**W7. Eikema et al. (2025) positioning** [Consensus]
Structure-conditional MBR paper cited only in Discussion; should also appear in Related Work §2 MBR paragraph. **Action**: Add reference in Related Work.

**W8. Contribution 1 framing** [Divergence]
R2: evaluation framework is engineering benchmark, not contribution. R1: ρ-AUROC dissociation finding has genuine value, but agrees "finding" is more accurate than "contribution." **Action**: Consider presenting as methodology/setup with dissociation as secondary finding.

### Minor — 1 issue

**M1. Conditional filtering** [Divergence]
R2: excluding zero-F1 instances introduces selection bias. R1: methodologically necessary to separate binary detection from quality gradation (Table 5 confirms). **Action**: Brief discussion of what filtering controls and doesn't.

---

## Reviewer Consensus

| Issue | R1 | R2 | Status |
|-------|----|----|--------|
| C1 (definitional reframing) | AGREE | Raised | Consensus |
| C2 (multi-seed selection) | Raised | AGREE | Consensus |
| C3 (ε threshold) | Raised | AGREE | Consensus |
| C4 (ablation scope) | Raised | AGREE | Consensus |
| C5 (title scope) | AGREE | Raised | Consensus |
| W1–W7 | Various | Various | Consensus |
| W8 (Contribution 1) | Partial REBUT | Raised | Divergence recorded |
| M1 (conditional filtering) | REBUT | Raised | Divergence recorded |

---

## Reviewer Divergence Detail

**W8**: R1 argues Contribution 1's core is the ρ-AUROC dissociation finding (EM leads AUROC=0.749 but ranks third in ρ=0.295), which has genuine practical value. R2 argues the evaluation framework is an engineering benchmark. Both agree "contribution" may overstate; "finding" is more accurate.

**M1**: R1 argues conditional filtering is a standard methodological step to separate binary detection from quality gradation, supported by Table 5 (full-set ρ=0.724 entirely boundary-driven). R2 argues excluding the hardest instances introduces selection bias. R1's position is stronger—the paper's claim structure requires this decomposition.

---

## Questions for Authors

1. Can you provide multi-seed selection F1 (mean±σ, p-value range) for at least SciERC NER LP?
2. What is the justification for ε=0.05 as the tied/non-tied boundary? Can you show the full CDF?
3. How do you reconcile the RE LP selection reversal under free-form decoding with the "intrinsic compression" claim?
4. Would you consider scoping the title to include "at 8B Scale"?
5. Can LP temperature data (T=0.7) be obtained, or is this a permanent data gap?

---

## Missing References

None identified. Both reviewers independently verified all 62 bib entries (56 OpenAlex-confirmed, 3 recent preprints not indexed, 3 encoding-related false positive mismatches). No fabricated or orphan citations.

---

## External Review

External review not configured (paperreview_ai.enabled not set). Status: not_requested.

---

## Overall Assessment

**Score: Borderline**

The paper identifies a real and practically important phenomenon (quality estimation ≠ sample selection for structured IE) and provides extensive experimental evidence. The conceptual distinction has genuine community value, and the diagnostic analysis (LP compression, MBR failure, non-tied subset) contains non-trivial empirical findings.

However, the core framing issue (C1) is fundamental: readers are led to believe all five signals empirically fail, when four fail by mathematical construction. The actual empirical contribution is narrower but genuinely interesting. The statistical gaps (C2: single-seed selection, C3: unjustified ε threshold), scope-evidence mismatch (C4-C5: "fundamental"/"Do Not Scale" from narrow ablation and 8B-only experiments), and persistent writing issues (W2: abstract density, W4: VC labeling) compound the framing problem.

With reframing (C1), multi-seed selection data (C2), ε justification (C3), claim scope corrections (C4-C5), and writing fixes (W1-W8), this would be a solid EMNLP Findings paper. The current version is not ready for main conference acceptance.

**Confidence: 4/5** (both reviewers independently assessed; thorough reading including all appendices)

---

## Scores Summary

| Dimension | R1 | R2 | Consensus |
|-----------|----|----|-----------|
| Soundness | 3/5 | 3/5 | 3/5 |
| Excitement | 3.5/5 | 3/5 | 3/5 |
| Overall | 3/5 | 3/5 | 3/5 (Borderline) |
| Confidence | 4/5 | 4/5 | 4/5 |
| Reproducibility | 3.5/5 | — | 3.5/5 |
