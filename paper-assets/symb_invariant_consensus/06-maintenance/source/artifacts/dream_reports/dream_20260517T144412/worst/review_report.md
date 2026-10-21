---
dream_id: dream_20260517T144412
tier: worst
overall_score: 3/6 Weak Reject
timestamp: 2026-05-17T16:04:18.820199+00:00
---

# Dream Review Report: "When Does Symbolic Consensus Help? A Systematic Empirical Study"

**Review Mode:** Full (2 Reviewers + Roundtable)
**Venue Standard:** Top ML venue (acceptance rate ~25%, 6-point scale)

---

## Consolidated Score

| | Score | Confidence |
|---|---|---|
| R1 (Methods + Experiments) | 3/6 (Weak Reject) | 4/5 |
| R2 (Novelty + Related Work) | 3/6 (Weak Reject) | 4/5 |
| **Consensus** | **3/6 (Weak Reject)** | **4/5** |

---

## Paper Summary

The paper presents SICA (Symbolic Invariant Consensus Aggregation), which extracts first-order logic (FOL) constraints from K reasoning traces and selects answers via weighted MAX-SAT. Evaluated across 5 model families, 3+ reasoning domains, and >1,300 problems, the main finding is negative: SICA provides no significant accuracy gain over Self-Consistency (majority voting). The authors identify a "capability trap" pattern and propose C0 (fraction of problems with multiple candidate answers) as a binary diagnostic. The only statistically significant positive result occurs at temperature T=1.0 (+8.3pp, p=0.034), but with degraded extraction quality and output coherence.

---

## Strengths (Consensus)

- **S1: Constraint ablation (Table 3) is the paper's strongest and most publishable result.** MAX-SAT, count-only, and random-weight agree on 802/804 problems. This cleanly demonstrates that the MAX-SAT solver contributes nothing beyond vote counting under tested conditions. Both reviewers independently identified this as the core contribution.

- **S2: Well-powered main experiment.** The Qwen-14B PW+FOLIO experiment (n=804) is appropriately sized. The observed Δ=+0.3pp convincingly rules out practically meaningful gains at default operating conditions.

- **S3: Per-problem constraint precision analysis (Table 2) is methodologically sound.** Mean precision 0.57 (std 0.23) on 307 multi-candidate problems, with no correlation to vote entropy (R²=0.008), provides fine-grained mechanistic evidence.

- **S4: K=11 odd-K ablation is an elegant diagnostic.** At odd K, ties are impossible; the resulting Δ=0 directly confirms SICA's only effective mechanism is tiebreaking.

- **S5: Honest framing of negative results.** The paper does not cherry-pick or bury unfavorable results. The LLaMA-8B +8.3pp outlier is explicitly discussed with confounds (48 truncated traces, failure to replicate at n≥200).

- **S6: Overhead quantification is practically useful.** 48.7% additional compute, dominated by constraint extraction (47%), with solver overhead negligible (<0.01%). The overhead-to-gain ratio of ~162 at default settings is actionable.

- **S7: Temperature ablation provides quasi-causal evidence.** Manipulating diversity continuously (C0 from 18% to 72%) while holding model and data constant is a well-designed ablation.

---

## Weaknesses (Consensus, Severity-Ordered)

### Critical

- **W1: Claims exceed evidence (scope-evidence mismatch).** The title and abstract generalize to "symbolic consensus" broadly, but only one specific pipeline is tested (same-model FOL extraction + MAX-SAT). Published neuro-symbolic methods (DyLoS, Aristotle, FoVer, LogicAgent) reportedly achieve gains on the exact same benchmarks (FOLIO, ProofWriter). Without citing or comparing against these, the paper cannot claim that symbolic consensus in general does not help. *Both reviewers flagged this independently.*

- **W2: Self-extraction confound is unaddressed.** The same model generates traces and extracts constraints. A model that commits a reasoning error will likely extract constraints consistent with that error. Without testing a stronger/separate extraction model or using FOLIO's gold FOL annotations as an oracle, the paper cannot distinguish "symbolic aggregation is fundamentally limited" from "same-model self-extraction produces non-discriminative constraints." *Both reviewers flagged this as a critical gap.*

- **W3: 8 references is critically below venue standards.** Top ML venues expect 30-60 citations for an empirical study. Critical omissions include:
  - Methods that work on the same benchmarks: DyLoS (EACL 2026), FoVer (TACL 2025), Aristotle (ACL 2025), LogicAgent
  - Test-time compute scaling: Snell et al. (ICLR 2025 Oral)
  - SC scaling plateaus: Loo et al. (2025)
  - DeepSeek-R1 technical report
  - Confidence-weighted SC: Taubenfeld et al. (2025)
  - SATBench and other SAT-based reasoning benchmarks
  
  The absence of methods that achieve positive results on the same benchmarks is particularly damaging to the paper's central claim. *Both reviewers flagged this.*

### Major

- **W4: "Capability trap" lacks novelty.** The diversity-quality tradeoff in LLM scaling is documented by Loo et al. (2025) and others. C0 as a diagnostic trivially separates reasoning models (C0<5%) from instruction models (C0>20%) with only 2 clusters and no gradient. Relabeling the known property that "more capable models have lower output diversity" as a "capability trap" does not constitute a conceptual contribution. *(R2 primary, R1 concurred)*

- **W5: Domain coverage is substantively thinner than claimed.** SICA operates meaningfully (C0>20%) almost exclusively on formal logic (ProofWriter + FOLIO). On StrategyQA (C0=10%), ARC (C0=5%), and GSM8K (C0=27% but n=30), conditions are degenerate or underpowered. The "3 reasoning domains" claim is misleading. *(Both reviewers)*

- **W6: Underpowered cross-model experiments.** 8 of 9 conditions in Table 1 use n≤60 (SE ≈ 6-8pp). At n=60, the minimum detectable effect at 80% power is ~12-15pp. Claims that these conditions "confirm" the null are statistically unjustified. The "combined N>1,300" figure in the abstract is misleading when 804/1,300 come from one model on one domain pair. *(R1 primary)*

- **W7: Missing/broken figures.** The hero scatter plots (F2: constraint precision vs. vote entropy; F4: C0 vs. gap) are referenced in the text but not rendered. Cross-references appear as "Figure ??". For a paper whose argument centers on diversity-quality relationships, these missing visualizations are a serious presentation failure. *(Both reviewers)*

- **W8: MAX-SAT formulation ambiguity.** R1 raised a critical question: as written, the formula sums only over traces whose answer matches each candidate. If constraints are never evaluated cross-answer, the method is structurally just a weighted vote, making the negative result trivially expected rather than informative. This must be clarified. *(R1)*

### Moderate

- **W9: Temperature ablation confounded.** T=1.0 simultaneously affects diversity, trace quality, and extraction quality. The positive result (p=0.034) at T=1.0 is from a single model at n=60, without replication across models. The constraint ablation (Table 3) was only performed at T=0.7; if MAX-SAT > count-only at T=1.0, the core "mechanism is vacuous" claim would be undermined. *(R1)*

- **W10: The paper reads more like an experiment report than a compelling narrative.** Sections 5.1-5.6 present results sequentially without building toward a unified insight. The "capability trap" framing appears late and feels post-hoc. *(R2)*

- **W11: Taubenfeld et al. (2024) citation appears incorrect.** The cited paper is about debate biases, not confidence-weighted SC. *(R1)*

---

## Questions for Authors (Priority-Ordered)

1. **(Critical)** In the MAX-SAT formulation, are constraints from trace t_i evaluated against candidate answers other than ans(t_i)? If constraints are never tested cross-answer, the method is structurally a weighted vote, and the negative result is trivially expected.

2. **(Critical)** Have you tested using a stronger model (e.g., Qwen-72B or a frontier model) as the constraint extractor while keeping Qwen-14B as the trace generator? This would separate extraction quality from the aggregation mechanism.

3. **(Critical)** How do you reconcile the claim that symbolic consensus does not help with published results showing that DyLoS, FoVer, Aristotle, and Logic-LM variants achieve gains on FOLIO and ProofWriter?

4. FOLIO provides gold FOL annotations. Have you considered an oracle experiment using these as constraints to establish an upper bound on what perfect extraction would achieve?

5. The LLaMA-8B large-n replications (StrategyQA n=200, FOLIO n=204) are mentioned but not in Table 1. Why were they excluded?

6. For the 2 problems where MAX-SAT and count-only disagree (out of 804), can you characterize what makes them different?

7. What is the distribution of constraint counts per trace? If most traces produce only 1-2 constraints, the negative result may reflect insufficient signal density rather than a fundamental limitation.

8. Has the constraint-sharing analysis (Section 6/Appendix F: 8 case studies) been verified at scale across the 307 multi-candidate problems?

---

## Minor Issues

- Broken LaTeX figure cross-references ("Figure ??")
- QwQ-32B row in Table 1 reports "--" for SC/SICA accuracy; actual numbers should be shown
- Paper uses custom geometry rather than target venue template
- Case study selection criteria (Appendix F) not described
- Abstract states "4 instruction-scale model families" but Mistral-7B results are absent from Table 1
- Several numerical discrepancies noted between different sections (R1 flagged specific instances)

---

## Roundtable Convergence Notes

**Step 2 (Cross-sharing):** Both reviewers independently arrived at the same score (3/6) and identified the same top-3 weaknesses (claim scope, self-extraction confound, insufficient references). R1 contributed the MAX-SAT formulation concern (W8) which R2 had not flagged; R2 contributed the specific missing references (DyLoS, Aristotle, FoVer) that demonstrate gains on the same benchmarks.

**Step 3 (Convergence):** Full agreement on score. The key deliberation point was whether the constraint ablation alone (Table 3) is sufficient for acceptance despite other weaknesses. Consensus: it is a necessary but insufficient contribution. Without addressing the self-extraction confound and the existence of methods that DO work on these benchmarks, the ablation's interpretation remains ambiguous (does it show symbolic consensus is limited, or that this particular extraction pipeline is limited?).

**Step 4 (Final assessment):** The paper has a genuinely strong empirical core in the constraint ablation and precision analysis. However, the scope-evidence mismatch (generalizing from one pipeline to "symbolic consensus"), the critically thin bibliography that misses methods achieving positive results on the same benchmarks, the unaddressed self-extraction confound, and the missing figures collectively place it below the acceptance threshold. The path to improvement is clear: narrow claims to match evidence (e.g., "same-model FOL extraction + MAX-SAT does not improve over voting"), expand scholarship to 30+ references including competing positive results, add gold-FOL oracle and stronger-extractor controls, and render all figures.

---

## Experiment Coverage Assessment

Comparing against the planned experiment list (review_context.yaml):

| Experiment | Status in Paper |
|---|---|
| Main results (exp-001) | Present (Table 1, n=804) |
| K ablation (exp-002) | Present (Appendix A, Table 7) |
| Tiebreak analysis (exp-003) | Present (Table 4) |
| Qwen-7B scaling (exp-004) | Present (Table 1 row) |
| QwQ-32B (exp-005) | Present (Table 1 row, but sparse data n=46) |
| C0 diagnostic (exp-006) | Present (Table 6, Table 11) |
| Qwen-72B (exp-007) | Present (Table 1 row) |
| Case studies (exp-008) | Present (Appendix F) |
| Overhead (exp-009) | Present (Appendix B, Table 8) |
| Mistral-7B (exp-010) | Mentioned in text but ABSENT from Table 1 |
| LLaMA-8B (exp-011) | Present (Table 1 row) |
| GSM8K pilot (exp-012) | Present (Appendix E) |
| Constraint ablation (exp-013) | Present (Table 3) |
| DeepSeek-R1 (exp-014) | Present (Table 1 row) |
| Logic-LM (exp-015) | Present (Appendix D, Table 10) |
| Weighted SC (exp-016) | Present (Appendix C, Table 9) |
| StrategyQA (exp-017) | Present (Table 1 row) |
| ARC-Challenge (exp-018) | Present (Table 1 row) |
| Constraint quality (exp-019) | Present (Table 2) |
| Temperature ablation (what_if_01) | Present (Table 5) |
| GSM8K pilot duplicate (what_if_02) | Merged with exp-012 |

Coverage is reasonably complete. Main gap: Mistral-7B results (exp-010) are discussed in text but missing from Table 1. Large-n LLaMA replications (mentioned in context as exp-019/020 with n=200/204) are referenced in prose but not tabulated.