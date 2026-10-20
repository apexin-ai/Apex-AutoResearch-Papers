---
dream_id: dream_20260521T075006
tier: median
overall_score: borderline accept
timestamp: 2026-05-21T08:46:30.367856+00:00
---

# Dream Review Report — Full Roundtable

**Paper:** "Reproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks and Models"
**Dream ID:** 20260521T075006
**Review mode:** full (2 Reviewers + 4-step roundtable)
**Target venue:** AAAI (1–10 scale)
**Date:** 2026-05-21

---

## Step 1: Independent Reviews

### Reviewer 1 (R1) — Methods & Experiments

**Dimension scores:**
- Soundness: 7
- Experimental rigor: 7
- Reproducibility: 7
- Presentation of results: 6

**Overall: 7/10**

**Strengths:**
- Exceptional experimental scale: 345,600 fully-crossed MMLU records + ~920K records across 4 additional benchmarks + 1,728 fine-tuning runs. This is among the largest controlled evaluation variance studies in the literature.
- The D-study out-of-sample validation (leave-one-model-out, median Δ=0.004, range 0.001–0.023) is the methodological highlight — it demonstrates that G-theory projections have genuine predictive validity in this domain, not just descriptive fit.
- The FP32/vLLM `enforce_eager` confound identification (§4.1.1) is a valuable methodological contribution on its own. Tracing a 0.4% "precision effect" to graph optimization rather than numerical precision shows careful experimental practice.
- The 8-check robustness battery (Table 9) — binary-vs-null, REML confirmation, bootstrap-vs-jackknife, fixed-vs-random sensitivity, etc. — demonstrates unusual thoroughness for an empirical NLP paper.
- Item resampling stability analysis (CV=7.3% across 3 independent 200-item samples) honestly addresses a key concern about the representativeness of the 200-item subsample.
- Henderson Method I confirmed by REML-EM (Δ<0.5pp) provides methodological assurance.

**Weaknesses:**
- **Incomplete cross-benchmark tables:** Table 5 shows "—" for Seed×Item on ARC-C, GSM8K, and HellaSwag. Table 6 has "—" for G≥0.90 and G≥0.95 budgets on ARC-C and GSM8K. Table 7 shows "—" for absolute IRT/G-theory item counts on all non-MMLU benchmarks. This pattern suggests the cross-benchmark analysis is substantially less complete than MMLU, undermining Contribution 2.
- **Hardware crossing is thin:** Only 2 GPU architectures tested, with 65% data completeness on the second GPU (3/4 models). The 1.4% hardware×methodology aggregate, while small, is derived from an incomplete design with wider CIs. "Preliminary evidence" is the correct framing, but it weakens the separability claim.
- **Format confound in cross-benchmark comparison:** The paper attributes ARC-Challenge's high item_id (39.8%, close to MMLU's 42.1%) to "4-choice format similarity" but does not formally test this. MC-format benchmarks (MMLU, ARC-C) vs. free-form/completion (GSM8K, MATH, HellaSwag) are confounded with task type. Without controlling for format, the "benchmark-conditional" claim conflates format effects with task-type effects.
- **Model count at lower bound for random facet:** 4–6 models is explicitly acknowledged as a limitation (G spread = 0.023 across leave-one-out subsets). Variance component estimates for the model facet have substantial uncertainty at this sample size. The paper handles this honestly but it limits the generalizability of exact percentages.
- **200-item subsampling:** CV=7.3% means reported percentages (e.g., "item_id = 42.1%") should be interpreted as ~42±4pp. The paper acknowledges this but the main tables present point estimates without this caveat prominently displayed.
- **Text-exact-match scoring barely discussed:** Listed as secondary metric but results are not reported in the main text for any benchmark. If text scoring produces qualitatively different variance structures (as the review context suggests with G_text < 0.05), this deserves at least a brief treatment.
- **Reduced design for non-MMLU benchmarks:** 2 precisions × 2 temperatures × 4 orderings (vs. MMLU's 3 × 3 × 4) means the non-MMLU designs have less statistical power for detecting interactions, yet this asymmetry is not discussed.

**Questions for authors:**
1. Can you provide the complete Table 5/6/7 entries currently shown as "—"? What prevents reporting Seed×Item for ARC-C and HellaSwag?
2. For the hardware crossing, what was the specific scheduling constraint that prevented completing the 4th model on A100? Is completion planned?
3. What does the text-exact-match variance decomposition look like? Does model×item remain the second-largest source?
4. How sensitive is the benchmark ordering in Table 5 to the choice of 200-item subsample? The resampling stability test (§4.2) was only done on MMLU/Llama — have you verified stability for other benchmarks?

---

### Reviewer 2 (R2) — Novelty & Related Work

**Dimension scores:**
- Novelty: 7
- Significance: 7
- Related work coverage: 7
- Positioning: 8

**Overall: 7/10**

**Strengths:**
- **Clear differentiation from Mesting (2026):** The paper identifies three specific axes of extension — (a) crossing infrastructure with methodology, (b) multi-benchmark analysis, (c) model as crossed random facet — and delivers on all three to varying degrees. This is honest and well-positioned.
- **Model×item = 33.6% is the standout finding:** Quantifying that item difficulty rankings are substantially model-specific (not just item-intrinsic) has real implications for how the community thinks about evaluation. The finding that this interaction *exceeds* item dominance on reasoning benchmarks (GSM8K 38.7% > 32.5%, MATH 35.8% > 30.2%) is both surprising and actionable.
- **IRT vs. G-theory comparison bridges parallel literatures:** The 2.8–4.7× ratio directly addresses the disconnect between IRT-based item selection (Polo et al. 2024) and multi-facet evaluation design. Showing that G-theory G=0.529 at IRT's recommended 116 items is a sharp, quotable finding.
- **The "benchmark-conditional" framing is more honest than a forced gradient narrative.** The paper could have cherry-picked an ordering and claimed monotonicity; instead, it explicitly discusses ARC-C's anomalous position and HellaSwag's residual dominance. This intellectual honesty strengthens credibility.
- **Practical deliverables enhance significance:** Budget tables (Table 6), GPU cost projections (Table 14), and an open-source pipeline translate abstract findings into tools practitioners can use immediately.
- **Fine-tuning extension adds breadth:** Even as a preliminary observation, showing that fine-tuning has a qualitatively different variance hierarchy (learning rate dominant, not item) with cross-study validation against Bui et al. (2025) enriches the paper's scope.

**Weaknesses:**
- **Application novelty, not methodological novelty:** G-theory is a well-established psychometric framework (Shavelson & Webb 1991, Brennan 2001). The paper's contribution is applying it to LLM evaluation with appropriate design choices, not developing new statistical methods. This is legitimate but limits the novelty ceiling. AAAI reviewers may view this as primarily an empirical contribution.
- **"Infrastructure" is narrowly defined as numerical precision.** The paper claims to "cross infrastructure with methodology" (Contribution/Introduction), but the infrastructure facet is just BF16 vs. FP16 — two nearly identical floating-point formats. Real infrastructure variance includes GPU architecture (partially addressed, incomplete), batch size (ThinkingMachines 2025, cited but not tested), inference framework, quantization level, etc. The separability finding (precision×methodology < 2%) is less surprising when "infrastructure" means "two similar precisions."
- **Risk of being perceived as incremental over Mesting (2026):** The three differentiation axes are clear but each is individually modest: (a) infrastructure crossing yields a near-null result; (b) cross-benchmark analysis has gaps; (c) model-as-facet is a design choice, not a methodological advance. Whether the sum exceeds the parts depends on presentation quality.
- **Missing related work:**
  - **Computerized Adaptive Testing (CAT):** Natural connection to efficient evaluation design. CAT dynamically selects items based on estimated ability — directly relevant to the D-study budget question. Not cited.
  - **Multi-Trait Multi-Method (MTMM) framework** (Campbell & Fiske 1959): Classic psychometric approach for crossing traits with methods. Conceptually adjacent to crossing benchmarks with methodology. Not discussed.
  - **Deeper engagement with Sclar et al. (2024):** The paper cites "up to 76% accuracy swings" but doesn't discuss whether Sclar's findings are consistent with the prompt×item = 3.8% found here. The discrepancy (76% vs. 3.8%) deserves explanation — likely because Sclar studies worst-case sensitivity while G-theory decomposes average variance.
  - **Biderman et al. (2024):** Cited but not discussed. Their "Lessons from the trenches" on reproducible evaluation shares significant thematic overlap and likely has specific findings worth engaging with.
  - **No engagement with LLM-as-judge evaluation literature** beyond fixing the judge: The decision to fix the judge (citing Mesting's 43.8% judge variance) is well-motivated but the growing literature on judge agreement/disagreement (e.g., Zheng et al. 2023) is not discussed.
- **The 22-reference bibliography is lean for a paper of this scope.** A multi-benchmark, multi-method study touching psychometrics, NLP evaluation, hardware nondeterminism, and fine-tuning instability would benefit from 35–45 references to adequately contextualize all claims.

**Questions for authors:**
1. How do you reconcile Sclar et al.'s "76% accuracy swings" with your prompt×item = 3.8%? Is this an average-vs-worst-case difference, a benchmark-specific difference, or something else?
2. Have you considered CAT/adaptive testing as an alternative to fixed D-study budgets? G-theory could inform initial item pool sizing while CAT optimizes per-examinee efficiency.
3. What specific aspects of Mesting (2026)'s single-benchmark findings do your multi-benchmark results confirm vs. contradict?
4. Would including batch size as an infrastructure facet change the separability conclusion?

---

## Step 2: Cross-Sharing Summary

After exchanging reviews, the reviewers identified the following convergences and divergences:

**Convergences (both reviewers agree):**
- The MMLU analysis (Exp 1) is the paper's strongest section — large-scale, well-executed, with the D-study validation as the methodological highlight.
- Model×item = 33.6% is the most important finding, genuinely new and well-supported.
- The cross-benchmark analysis has significant gaps (missing table entries, reduced designs for non-MMLU benchmarks) that weaken Contribution 2.
- The hardware crossing is too incomplete to support strong claims about separability.
- The paper is commendably honest about its limitations.
- Score: both independently arrived at 7/10.

**Divergences and complementary observations:**
- R1 is more concerned about format confounds in cross-benchmark comparison (MC vs free-form conflated with task type); R2 focuses on the narrow definition of "infrastructure."
- R2 identifies missing related work (CAT, MTMM, deeper Sclar engagement) that R1 did not flag.
- R1 notes the under-discussed text-exact-match scoring and design asymmetry for non-MMLU benchmarks; R2 notes the lean bibliography.
- R2 raises the "application novelty vs. methodological novelty" concern more explicitly; R1 implicitly accepts the framework and focuses on execution quality.

---

## Step 3: Convergence Discussion

**Key discussion points and resolutions:**

1. **Should the cross-benchmark gaps lower the score?**
   - R1 argues the many "—" entries in Tables 5–7 are a significant concern — Contribution 2 claims benchmark-conditional variance structure, but the supporting evidence is patchy for non-MMLU benchmarks.
   - R2 notes that the qualitative findings (item dominance varies, model×item exceeds item on reasoning tasks) are supported even with gaps, but agrees the paper overpromises relative to what's fully reported.
   - **Resolution:** Both agree this is a weakness but not fatal. The paper should either complete the tables or explicitly note which cross-benchmark claims rest on partial data. Score impact: −0.5 from both reviewers' perspective.

2. **Is the novelty sufficient for AAAI?**
   - R2 raised the "application novelty" concern. R1 partially agrees but argues that the empirical scale and D-study validation demonstrate sufficient methodological craft.
   - **Resolution:** The novelty is adequate for AAAI if the paper is viewed as an empirical contribution with practical impact, not a methods paper. The IRT comparison and practitioner toolkit strengthen the case. The concern is legitimate but does not push below threshold.

3. **How much does the thin "infrastructure" facet matter?**
   - R2 argues strongly that BF16/FP16 is too narrow to claim "crossing infrastructure with methodology." R1 agrees that the separability finding is less impressive when the two precision levels are nearly identical.
   - **Resolution:** This is a framing issue more than a scientific one. The paper should temper "infrastructure" claims or rename to "numerical precision." The actual finding (precision nearly negligible) is useful even if unsurprising.

4. **Revised consensus score:**
   - Both reviewers shift from 7 to 6 after considering the combined weight of: (a) incomplete cross-benchmark tables, (b) narrow infrastructure definition, (c) application-level novelty. However, both acknowledge the paper's strengths (scale, D-study validation, honesty, practical tools) keep it above the threshold.
   - **Final consensus: 6/10 — Borderline Accept**

---

## Step 4: Synthesized Assessment

### Overall Recommendation: **6/10 — Borderline Accept**

### Meta-Review

This paper applies Generalizability Theory to LLM evaluation, conducting a large-scale study (345,600 MMLU records + ~920K across 4 additional benchmarks) that crosses numerical precision with methodology factors (prompt, seed, temperature, ordering) and treats model as a crossed random facet. The core finding — that model×item interaction constitutes 33.6% of score variance on MMLU, making item difficulty rankings substantially model-specific — is the paper's strongest and most novel contribution. The D-study out-of-sample validation (Δ=0.004) demonstrates that G-theory projections have predictive validity for LLM evaluation design, and the IRT comparison (2.8–4.7× more items needed) usefully bridges two parallel literatures.

The paper's main vulnerabilities are: (1) the cross-benchmark analysis, while conceptually valuable, has significant gaps — multiple table entries are missing for non-MMLU benchmarks, and the reduced experimental design (2 precisions, 2 temperatures) provides less statistical power; (2) "infrastructure" is narrowly just BF16-vs-FP16, making the separability finding unsurprising; (3) the hardware crossing is incomplete (65% data on second GPU); and (4) the novelty is primarily in application of an established psychometric framework rather than methodological innovation.

Despite these concerns, the paper makes a genuine empirical contribution: the model×item magnitude quantification, the benchmark-conditional variance finding, and the practical budget tables are all useful to the evaluation community. The paper is honest about its limitations, conducts an extensive robustness battery, and provides open-source tools. The fine-tuning G-study extension adds breadth.

### Dimension Scores (Consensus)

| Dimension | Score | Notes |
|-----------|-------|-------|
| Soundness | 7 | Methods technically correct; Henderson I + REML confirmation; appropriate bootstrap CIs |
| Novelty | 6 | Application of existing framework; model×item quantification and D-study validation are new empirical contributions |
| Significance | 7 | Practical impact via budget tables and pipeline; model×item finding changes how we think about item difficulty |
| Experimental rigor | 6 | MMLU excellent; cross-benchmark has gaps; hardware crossing incomplete; format confounds uncontrolled |
| Related work | 6 | Adequate but lean (22 refs); missing CAT, MTMM, deeper engagement with Sclar/Biderman |
| Clarity | 7 | Well-written; honest framing; but many "—" in tables and text-scoring results absent |
| Reproducibility | 7 | Open-source pipeline promised; design details sufficient; vLLM version specified |
| **Overall** | **6** | **Borderline accept — strong MMLU analysis with practical tools, weakened by incomplete cross-benchmark evidence and narrow infrastructure scope** |

### Strengths (in order of importance)
1. Model×item = 33.6% on MMLU with D-study validation (Δ=0.004) is a genuine, well-supported, and impactful finding
2. Massive experimental scale with comprehensive robustness checks (8 analyses, Table 9)
3. IRT vs. G-theory comparison directly addresses a practical gap (2.8–4.7× item ratio)
4. Honest "benchmark-conditional" framing avoids overclaiming a gradient
5. FP32/vLLM confound identification is independently valuable
6. Practical deliverables: budget tables, GPU cost projections, open-source pipeline
7. Fine-tuning extension with cross-study validation (Bui et al. 2025)

### Weaknesses (in order of importance)
1. Cross-benchmark tables (5, 6, 7) have many missing entries; Contribution 2 ("benchmark-conditional variance structure") rests on incomplete evidence for non-MMLU benchmarks
2. "Infrastructure" facet is narrowly BF16-vs-FP16; the separability claim is weakened by the near-identity of these two formats
3. Hardware crossing incomplete (3/4 models on A100); "preliminary evidence" is the correct but weak framing
4. Application novelty (established psychometric framework applied to new domain) rather than methodological novelty
5. Format confound (MC vs. free-form/completion) conflated with task type in cross-benchmark comparison; ARC-C's position is attributed to format but not tested
6. 4–6 models at the lower bound for random facet estimation; G spread=0.023 indicates non-trivial instability
7. 200-item subsamples with CV=7.3% — point estimates in tables should carry explicit uncertainty caveats
8. Lean bibliography (22 references) for a paper spanning psychometrics, NLP evaluation, hardware effects, and fine-tuning instability; missing CAT, MTMM, deeper engagement with prior work
9. Text-exact-match scoring results not reported despite being listed as secondary metric

### Questions for Authors
1. Can you complete the missing entries in Tables 5, 6, and 7? If these analyses were not run, please explain what prevents them.
2. How do you reconcile Sclar et al.'s "76% accuracy swings" with your prompt×item = 3.8%?
3. Would you consider renaming "infrastructure" to "numerical precision" to more accurately scope the separability claim?
4. What does the text-exact-match variance decomposition look like? Does model×item remain dominant?
5. Have you run the item resampling stability test on non-MMLU benchmarks?
6. What specific scheduling constraint prevented completing the 4th model on A100?

### Suggestions for Improvement
- Complete cross-benchmark tables or explicitly flag which claims are MMLU-only vs. multi-benchmark
- Add batch size or quantization level as an infrastructure facet to strengthen the separability analysis
- Include a brief CAT/adaptive testing discussion to connect D-study budgets to the adaptive evaluation literature
- Report text-exact-match results at least in supplement
- Expand bibliography to 35+ references with deeper engagement on Sclar, Biderman, and psychometric foundations
- Add a paragraph on the format confound in the cross-benchmark discussion

### Experiment Coverage Assessment
All planned experiments from the design document are represented in the paper:
- exp-001 (MMLU precision study): ✓ Complete
- exp-001b (item resampling): ✓ Complete
- exp-002 (cross-benchmark): ✓ Present but tables have gaps
- exp-003 (multi-hardware): ✓ Present, explicitly partial
- exp-004 (comprehensive analysis): ✓ Present
- exp-005 (14B extension): ✓ Present
- exp-006 (fine-tuning): ✓ Present in Discussion
- exp-007 (LayerCast): ✓ Present in supplement (Table 13)
- exp-008 (MATH): ✓ Present in main results

Coverage is comprehensive in breadth. The main gap is depth on non-MMLU benchmarks where several analysis pipelines appear to have been run with fewer conditions or with incomplete results reporting.

### Verdict
The paper sits at the borderline for AAAI. Its strongest contribution — model×item quantification with D-study validation on MMLU — is genuinely valuable and well-executed. The practical deliverables (budget tables, pipeline) enhance significance. However, the cross-benchmark story, which is positioned as a primary contribution, is undermined by incomplete tables and uncontrolled format confounds. The narrow "infrastructure" definition and incomplete hardware crossing further weaken secondary claims. With revisions addressing the cross-benchmark gaps and more precise scoping of the infrastructure/separability claims, this paper would be a solid accept. In its current form, it is a borderline accept whose fate may depend on the strength of the remaining pool.

**Confidence: 4/5** — Both reviewers have strong familiarity with variance decomposition, psychometric methods, and LLM evaluation. The lower-than-maximum confidence reflects uncertainty about how AAAI reviewers would weight application novelty vs. empirical contribution.
