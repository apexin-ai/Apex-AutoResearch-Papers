---
dream_id: dream_20260517T165032
tier: best
overall_score: weak reject
timestamp: 2026-05-17T17:28:19.890520+00:00
---

# Dream Review Report: "The Capability Trap: Why Self-Extracted Constraints Cannot Improve LLM Majority Voting"

**Dream ID**: 20260517T165032 | **Tier**: best | **Review Mode**: full | **Date**: 2026-05-17

---

## Roundtable Summary

Two reviewers conducted independent reviews (R1: Methods+Experiments; R2: Novelty+Related Work), followed by cross-sharing and convergence discussion.

**Consensus rating: 3/6 (Weak Reject)**

Both reviewers agree the paper presents a substantial empirical effort with a well-designed oracle control experiment and compelling constraint ablation. However, two critical issues prevent acceptance: (1) the constraint evaluation function sigma(c,a) may be a source-answer indicator rather than genuine cross-answer evaluation, potentially making the "capability trap" a design artifact rather than a discovered phenomenon; (2) the core finding (LLM self-formalization produces low-quality constraints) has significant overlap with prior work (LINC, Logic-LM, Huang et al. 2024) and the novelty is insufficiently differentiated.

---

## R1 Review: Methods + Experiments

### Scores
- Soundness: 2/4
- Contribution: 3/4
- Presentation: 2/4
- Overall: 3/6 (Weak Reject)
- Confidence: 4/5

### Strengths

1. **Well-structured negative result with clear mechanistic explanation.** The three-way constraint ablation (MAX-SAT = count-only = random-weight, >99.6% agreement on n=804) is convincing evidence that the satisfiability machinery is vacuous given non-discriminative constraints. This moves beyond a simple empirical null to a structural explanation.

2. **Oracle control experiment is the strongest contribution.** The oracle-SICA result (+8.82pp, p<0.001 on FOLIO n=204 with gold FOL annotations) cleanly separates the aggregation mechanism from extraction quality. This establishes that the MAX-SAT framework *can* work, pinpointing the bottleneck at constraint quality.

3. **Breadth of experimental conditions.** 5 model families, 3 primary + 2 supplementary domains, within-family scaling (7B/14B/72B), K ablation, weighted SC baselines, Logic-LM comparison. The 18-condition C0 diagnostic validation provides reasonable coverage.

4. **Powered replications discipline.** The authors conducted n=60 pilots then followed up with n>=200 powered tests for key conditions (LLaMA-8B StrategyQA, LLaMA-8B FOLIO, GSM8K expanded), demonstrating methodological rigor.

5. **C0 diagnostic is practically useful.** Computing multi-candidate rate from Stage 1 alone before investing in constraint extraction is a genuinely useful early-stopping criterion.

6. **Per-problem constraint precision analysis (n=307) is thorough.** Mean precision=0.50, sigma=0.12, 89% in [0.4,0.6], zero correlation with diversity (r=0.03), positive flip precision 0.52 vs negative flip 0.48.

### Weaknesses

1. **[CRITICAL] The constraint evaluation function sigma(c,a) is underspecified and possibly trivial by construction.** The method description indicates that sigma(c,a) = 1 if and only if c was extracted from a trace whose final answer is a, reducing sigma to a source-answer indicator rather than an independent logical evaluation. If so, Equation 2 is *by construction* equivalent to weighted vote counting, making the entire MAX-SAT apparatus a tautological no-op. The "capability trap" may be a design artifact rather than a fundamental limitation. The paper should either (a) implement genuine cross-answer constraint evaluation via Z3, or (b) clearly acknowledge that the negative result may be an artifact of this design choice.

2. **Data discrepancies between paper versions.** The structured LaTeX sections and the dream report show different numbers for the same conditions (e.g., composition of the n=804 aggregate, LLaMA-8B C0 values, p-values for StrategyQA-14B). These inconsistencies undermine confidence in reported numbers.

3. **Many conditions are underpowered (n=60).** Of 18 conditions, a majority use n=60. McNemar's test with n=60 has very low power to detect effects <5pp. The claimed N>1,300 total is misleading when most conditions cannot detect even moderate effects. For example, Qwen-14B StrategyQA n=60 shows delta=+3.33pp (suggestive but inconclusive).

4. **Missing cross-model constraint extraction baseline.** Testing even one cross-model condition (e.g., Qwen-72B extracting constraints from Qwen-7B traces) would distinguish between "self-extracted constraints are non-discriminative" and "all LLM-extracted constraints are non-discriminative."

5. **Z3 parser confound undisclosed.** Development logs reveal the Z3 parser had 41-100% constraint loss rates in early experiments. The paper does not discuss whether parsing failures in final experiments remain a confound.

6. **Temperature ablation too narrow.** Only 4 temperatures on n=60 with a single model. Insufficient to draw conclusions.

### Questions for Authors

1. Is sigma(c,a) implemented as a source-answer indicator, or does the code evaluate each constraint against each candidate answer via Z3? If the former, has the team considered implementing genuine cross-answer evaluation?

2. The constraint ablation shows agreement 802/804 between MAX-SAT and SC. What happens on the 2 disagreeing problems?

3. What is the Z3 constraint-level parsing success rate (not trace-level extraction rate)?

4. The Qwen-72B-AWQ uses 4-bit quantization. Has quantization been verified to not affect constraint extraction quality?

5. How were the 8 problems selected for qualitative analysis -- randomly sampled or selected for illustration?

---

## R2 Review: Novelty + Related Work

### Scores
- Soundness: 3/4
- Contribution: 2/4
- Presentation: 2/4
- Overall: 3/6 (Weak Reject)
- Confidence: 4/5

### Strengths

1. **Well-designed oracle control experiment.** The gold-FOL oracle cleanly separates the aggregation mechanism (which works) from the extraction quality (which fails), providing causal localization that elevates this beyond "we tried X and it didn't work."

2. **Thorough ablation design.** The three-way constraint ablation demonstrates not just that SICA fails, but precisely *how* it fails: MAX-SAT reduces to counting because constraints lack discriminative power.

3. **Appropriate scope of claims.** The paper restricts its finding to same-model self-extraction and acknowledges that DyLoS, Aristotle, FoVer achieve gains through different mechanisms.

4. **Multi-dimensional evidence.** Cross-model, cross-domain, within-family scaling, K ablation, weighted SC, Logic-LM comparison. Thoroughness makes the null result convincing.

5. **Good connection between theory and experiment.** The degeneration equation predicts MAX-SAT reduces to counting when constraints are non-discriminative; the ablation confirms this.

### Weaknesses

1. **[CRITICAL] The "capability trap" framing overstates novelty.** The core observation (LLMs cannot reliably formalize their own reasoning into discriminative FOL) is established in prior work. LINC (Olausson et al., 2023) documented ~40% translation error rates. Logic-LM (Pan et al., 2023) showed similar issues. The paper's contribution is systematic quantification and oracle-controlled separation, not discovery. The paper should position more modestly.

2. **[CRITICAL] Missing important related work on LLM self-evaluation.** The paper does not engage with:
   - Huang et al. (2024) "Large Language Models Cannot Self-Correct Reasoning Yet" (ICLR 2024) -- the most direct precedent, structurally parallel to this paper's finding
   - Self-refinement/self-critique literature (Madaan et al. 2023 "Self-Refine"; Shinn et al. 2023 "Reflexion")
   - LLM calibration/uncertainty estimation (Kadavath et al. 2022) -- the capability trap is fundamentally a calibration/metacognition failure
   - Multi-agent debate (Liang et al. 2023; Du et al. 2024) -- listed in bibliography but not discussed

3. **Statistical power concerns underplayed.** 4 of 8 Table 1 conditions have n=60. Within-family scaling results (Appendix D) are entirely n=60 yet treated as confirmatory. The C0 progression (70%->38%->22%) should be "directionally consistent" rather than "confirming the trap from both ends."

4. **SICA pipeline may not be the strongest instantiation.** Several design choices may artificially weaken SICA: source-answer indicator sigma, potentially unoptimized extraction prompt (no prompt ablation), only FOL constraints tested (propositional/numerical bounds might differ). The title claim "Cannot Improve" is too strong for one extraction method and one solver.

5. **C0 diagnostic has limited value beyond the obvious.** C0<5% predicting SICA=SC is near-tautological (one candidate answer means any aggregation is equivalent). The correlation analysis (r=0.05 across 18 conditions) uses too few data points with too heterogeneous conditions.

6. **Bibliography quality issues.** Several entries (DyLoS, Aristotle, FoVer, SATBench, LLM-CP) lack proper author information. This would be a desk-reject risk at top venues.

### Questions for Authors

1. Have you tested a variant where constraints are genuinely evaluated against all candidate answers (not using the source-answer indicator)?

2. Have you considered a cross-model control (e.g., GPT-4/Claude extracting constraints from same traces)?

3. What is constraint precision conditional on problem difficulty? Do easy vs. hard problems show different constraint quality?

4. Why not frame this as "current LLMs lack metacognitive capability for discriminative self-formalization" rather than a structural "trap"?

5. How sensitive are results to the extraction prompt? Any prompt engineering ablation?

---

## Roundtable Convergence

### Points of Agreement (both reviewers)

1. **The oracle control experiment is the paper's strongest and most novel contribution.** It provides genuine causal separation between aggregation mechanism quality and extraction quality.

2. **The sigma(c,a) source-answer indicator issue is the most critical technical concern.** If sigma merely indicates whether a constraint came from a trace supporting answer a (rather than independently evaluating the constraint against a), then MAX-SAT is equivalent to weighted voting *by construction*, not merely empirically. The "capability trap" would be a design artifact. Both reviewers flag this as potentially undermining the paper's central claim.

3. **Underpowered conditions weaken claimed generality.** The majority of conditions use n=60, which cannot support confirmatory conclusions. The "18 conditions, N>1300" framing overstates the effective statistical power.

4. **Paper is structurally incomplete.** Placeholder sections, missing figures, incomplete bibliography entries.

5. **The three-way constraint ablation (Table 2) is compelling.** Both reviewers find the MAX-SAT = count-only = random-weight equivalence to be strong mechanistic evidence.

### Points of Divergence

| Dimension | R1 | R2 | Resolution |
|-----------|----|----|------------|
| Soundness | 2/4 (sigma artifact concern) | 3/4 (methodology rigorous within scope) | **2.5** -- sigma issue is serious but oracle partially addresses it |
| Contribution | 3/4 (ablation and diagnostic are valuable) | 2/4 (core finding not novel enough) | **2.5** -- oracle is novel, but framing overstates originality |
| Primary concern | Design artifact (sigma) | Novelty vs prior work | Both valid; address both for resubmission |

### Consolidated Verdict

**Overall Score: 3/6 (Weak Reject)**

The paper presents a substantial empirical investigation with genuine methodological contributions (oracle control, constraint ablation, C0 diagnostic). However, two issues prevent acceptance at a top venue:

1. **Methodological clarity**: The sigma(c,a) evaluation function must be clarified. If it is a source-answer indicator, the paper must either (a) implement genuine cross-answer Z3 evaluation and re-run experiments, or (b) explicitly scope all claims to this specific (and potentially trivially degenerate) pipeline variant.

2. **Novelty positioning**: The "capability trap" must be positioned relative to established findings on LLM self-formalization quality (LINC, Logic-LM) and self-correction limitations (Huang et al. 2024). The paper's genuine novelty (systematic quantification, oracle-controlled causal separation, constraint ablation) should be foregrounded over the "new concept" framing.

### Recommendations for Revision

1. **Resolve the sigma question**: Implement genuine cross-answer constraint evaluation (evaluate each constraint against each candidate via Z3) and compare with the source-answer indicator variant. This single experiment would either (a) confirm the capability trap holds under proper evaluation (strengthening the paper dramatically) or (b) reveal that the negative result was an artifact (requiring major revision).

2. **Add missing related work**: Cite and discuss Huang et al. (2024), Madaan et al. (2023), Kadavath et al. (2022). Reposition the capability trap as systematic quantification and causal localization of a known limitation class.

3. **Power up key conditions**: Expand within-family scaling, StrategyQA-14B, ARC-Challenge, and DeepSeek conditions to n>=200 with bootstrap CIs.

4. **Add one cross-model condition**: Use a stronger model to extract constraints from weaker model traces. This would distinguish "self-extraction fails" from "all LLM extraction fails."

5. **Complete the paper**: Fill placeholders, include figures (especially the F2 hero figure), fix bibliography entries, reconcile data discrepancies.

6. **Soften the title**: "Cannot Improve" -> "Does Not Improve" or "Fails to Improve" to match the empirical (not impossibility) nature of the finding.

---

## Experiment Coverage Assessment

All 18 imagined experiments from the design document appear to be covered in the paper:
- K ablation, tiebreak analysis, within-family scaling (7B/14B/72B), QwQ-32B, C0 diagnostic, constraint quality case studies, overhead analysis, LLaMA-8B (powered), GSM8K (pilot+expanded), constraint ablation, DeepSeek-R1, Logic-LM baseline, weighted SC, StrategyQA-14B, ARC-Challenge-14B, constraint quality correlation -- all present.

**Coverage**: Complete (18/18 experiments). The paper faithfully reflects the experimental design.

**Quality of reflection**: Results are reported consistently with design expectations. The narrative coherently integrates all experiments into the capability trap storyline. However, the statistical power of individual conditions varies significantly (n=30 to n=804), and the paper could be more transparent about which conditions are confirmatory vs. exploratory.
