# Adversarial Review Report: EMNLP 2026 Simulation

**Paper**: "Exception Events Are All You Need: Cross-Model Fault Detection for Verdict Prediction"

**Simulated venue**: EMNLP 2026 Main Conference (ARR May cycle)

---

## Reviewer 1: Methodology Expert

**Overall Assessment: Borderline**
**Confidence: 4/5**

### Strengths

1. **Clean experimental decomposition.** The information density decomposition (gradient dilution 26% vs. information overload 74%) via the `full_trace_label_only` ablation is a well-designed causal intervention. This is the most methodologically novel contribution — it separates training signal quality from input signal quality in a way that is reusable by future work.

2. **Transparent reporting of negative/messy results.** The paper does not hide the DeepSeek seed 123 outlier, the VOTA truncation confound, or the DebugBench ceiling effect. The irreducible error analysis (GeneratorExit) is a model of thoroughness.

### Weaknesses (by severity)

**W1 (Major): Insufficient seed coverage — most conditions have n=1 seed.**
The headline robustness claim rests on 3 seeds for `exception_only` only. All other conditions (VOTA, full_trace, label_only, ae_only, loop_only, no_trace) report a single seed (42). This is a critical gap: the entire Claim 2 (gradient dilution decomposition) and Claim 3 (two-tier hierarchy) hang on single-seed point estimates. The 86.22% for `label_only` could shift substantially with different seeds, invalidating the 26/74 ratio. At minimum, `ae_only`, `label_only`, and `loop_only` need 3-seed validation on Qwen to confirm the hierarchy is stable.

**Recommendation**: Run 3 seeds for `label_only` and `ae_only` at minimum. If infeasible, add explicit caveats that the decomposition ratio is a point estimate from a single seed.

**W2 (Major): Statistical testing is incomplete for key comparisons.**
- The `exception_only` vs. `ae_only` comparison (99.83% vs. 99.92%, p=0.80) correctly reports non-significance, but **no effect size or equivalence test** is provided. Non-significance ≠ equivalence. A TOST equivalence test with a meaningful margin (e.g., 1pp) would substantiate the "statistically indistinguishable" claim.
- The 26/74 decomposition has no uncertainty quantification on the ratio itself. Bootstrap the ratio directly (gap_gradient / gap_total) to get a CI on the percentage split.
- DeepSeek `exception_only` 3-seed results (99.33, 99.33, 91.09) — reporting σ=4.76pp from n=3 is essentially uninformative. The distribution is bimodal, not normal; σ is a misleading summary statistic. Acknowledge the bimodality explicitly and avoid parametric summaries.

**W3 (Moderate): The VOTA cross-model gap is acknowledged as confounded but then used for narrative support.**
The paper correctly states "the two factors cannot be disentangled" (model capability vs. truncation), but then uses the 14.96pp gap repeatedly to argue that "richer representations are model-dependent." This is overclaiming from confounded evidence. The group analysis (intact 100% vs. truncated 83.04%) provides *directional* evidence but cannot estimate the truncation contribution because the groups differ in other ways (e.g., problem complexity correlates with trace length). The honest framing is: "VOTA degrades on DeepSeek; truncation is a plausible contributor, but the magnitude of its effect is unknown."

**W4 (Moderate): No cross-condition comparison on DeepSeek for ablation.**
The two-tier hierarchy (Claim 3) is established entirely on Qwen. DeepSeek only has 4 conditions (exception_only, VOTA, full_trace, no_trace) — no `ae_only`, `loop_only`, or `label_only`. The hierarchy could look different on a weaker model. This limits the "cross-model" framing.

**W5 (Minor): Confidence intervals assume independent Bernoulli trials despite acknowledged duplication.**
The paper notes 48.99% test set duplication for `exception_only` but reports CIs assuming n=1190. The deduplicated CI (n=607) is mentioned in passing but all main tables use n=1190. This inflates precision. At minimum, report the deduplicated CI as the primary one, or use cluster-robust CIs where duplicates form clusters.

---

## Reviewer 2: Domain Expert / Skeptic

**Overall Assessment: Weak Reject**
**Confidence: 4/5**

### Strengths

1. **Practical design principle is clear and actionable.** "Extract the highest-specificity diagnostic signal and discard everything else" is a useful takeaway for practitioners building trace-augmented systems. The paper demonstrates that over-engineering trace representations can hurt.

2. **Honest self-assessment of contribution scope.** The paper explicitly acknowledges (Introduction, para 4) that exception dominance is "not itself surprising" and locates the novelty in the decomposition and cross-model analysis.

### Weaknesses (by severity)

**W1 (Major): The task may be trivially solvable, undermining the significance of findings.**
99.83% accuracy with a simple presence/absence signal raises a fundamental question: **is this task interesting enough to warrant a paper?** The `exception_only` representation effectively reduces verdict prediction to: "does the trace contain `[ERROR]`?" → fail; "does it not?" → pass. This is a regex, not a learned representation. The paper argues that the *decomposition* of why other representations fail is the contribution, but if the task is solvable by string matching, the decomposition explains something obvious: noisy inputs hurt classifiers more than clean inputs.

The irreducible error analysis confirms this — the only errors are where the representation *incorrectly* marks a pass as containing errors (GeneratorExit). The model has learned precisely the trivial rule.

**Counter-argument the paper should address**: What is the accuracy of a zero-shot regex baseline (`grep -c "[ERROR]"`)? If it matches 99.83%, the entire SFT pipeline is unnecessary and the contribution collapses. The paper never reports this baseline.

**W2 (Major): Extreme narrowness of evaluation scope.**
- **2 models, both ~7B, both instruction-tuned**: No encoder models (e.g., CodeBERT for classification), no larger models (13B+, 70B), no API models. The "cross-model" framing overstates the diversity — both are decoder-only instruction-tuned code LLMs from the same generation.
- **1 primary dataset (591 problems)**: HumanEval + MBPP are toy benchmarks with short, self-contained functions. Real verdict prediction involves multi-file projects, complex dependencies, flaky tests, environment-dependent failures, timeout errors without exceptions, assertion failures that don't raise exceptions, etc. The exception_only signal would likely fail catastrophically on assertion-based test frameworks (e.g., pytest where `assert x == y` raises `AssertionError` for both logic errors and expectation mismatches).
- **DebugBench validation is weak**: 96.71% no_trace baseline → only 3.29pp headroom. This does not validate trace importance; it shows the dataset is too easy.
- **Python only**: No evidence this transfers to statically-typed languages where exception semantics differ (e.g., Java checked exceptions, Rust panics, Go error returns).

**W3 (Major): The "fault detection reframing" is a known perspective, not a novel contribution.**
The SE community has long understood that test verdict prediction is fault detection. FuseFL (cited in the paper) already uses structured fault signals including error messages. TRACED uses execution-aware features for vulnerability detection (a fault detection task). The paper's reframing adds terminology but not conceptual novelty.

**W4 (Moderate): Solution generation creates a distribution confound.**
All 5,910 solutions were generated by Qwen-2.5-Coder-7B — the same model used for evaluation. This means:
1. The failure modes in the dataset are Qwen-specific (the types of bugs Qwen makes).
2. The exception patterns are also Qwen-specific.
3. Evaluating Qwen on its own failure modes may inflate accuracy (the model "recognizes" its own error patterns).
The paper acknowledges this in Limitations but dismisses it ("does not affect verdict prediction"). This dismissal is unjustified — a model may be better at recognizing bugs it typically makes than bugs from a different distribution.

**W5 (Moderate): Missing practical motivation.**
When would you need ML-based verdict prediction? If you can execute the code (which you must, to get the trace), you already have the verdict. The paper never addresses this deployment scenario question. Possible answers (predicting verdicts for unseen tests, or for partial executions) are not discussed.

---

## Reviewer 3: Writing & Presentation Expert

**Overall Assessment: Weak Accept**
**Confidence: 3/5**

### Strengths

1. **Exceptionally well-structured paper.** The progression from single-model ablation → decomposition → cross-model validation → cross-dataset validation is logical and easy to follow. Each section answers a clear question.

2. **Tables and figures are information-dense.** Table 1 (cross-model) and Table 2 (ablation) convey the core results efficiently. The trace overview figure (Fig 1) provides helpful visual context. CIs are consistently reported.

### Weaknesses (by severity)

**W1 (Major): The title overclaims.**
"Exception Events Are All You Need" implies universality across tasks and settings. The paper demonstrates this for one task (verdict prediction), one language (Python), two very similar models, and one dataset family. A more accurate title: "Exception Events Suffice for Verdict Prediction: A Component Ablation Study." The AIAYN allusion sets expectations the paper cannot meet.

**W2 (Moderate): Claim 1 framing is convoluted and defensive.**
The abstract contains a 4-line sentence describing the DeepSeek seed results with parenthetical qualifications. The Claim 1 statement in the Introduction is 5 lines long with inline statistics. This defensiveness — trying to simultaneously claim robustness while acknowledging the outlier — produces confusing prose. Suggestion: lead with the clean Qwen result as the primary finding, then dedicate a separate paragraph to DeepSeek seed sensitivity as a nuanced secondary finding. Don't try to fit both into a single sentence.

**W3 (Moderate): Overclaiming in several specific places.**
- Abstract: "the first systematic component ablation of trace representations for verdict prediction" — this is likely true but unfalsifiable unless the authors have done an exhaustive literature survey. Consider "a systematic" instead.
- §5.1: "trace representations should match the model capability floor, not the ceiling" — this design principle is asserted from a 2-model comparison where the "floor" model has a known truncation confound. The evidence doesn't support such a general principle.
- Conclusion: "These results reframe verdict prediction as fault detection" — the reframing is a perspective shift, not a result. The results are accuracy numbers; the reframing is interpretation.

**W4 (Moderate): Related work positioning is incomplete.**
- No mention of **test outcome prediction** literature from SE (e.g., Bertolino et al.'s work on test case prioritization, or ML-based test flakiness detection). These communities have studied pass/fail prediction for decades.
- No comparison with **simple ML baselines** (logistic regression on trace features, random forest on exception presence/absence). The paper only compares LLM-based approaches against each other, missing the opportunity to show when LLMs are actually needed.
- The TRACED citation discusses execution-aware *pretraining* for encoder models — a fundamentally different setup (encoder vs. decoder, pretraining vs. SFT). The comparison is not apples-to-apples but the paper doesn't acknowledge this.

**W5 (Minor): DebugBench results are over-interpreted.**
The paper says "the component ranking is preserved" on DebugBench but all three conditions are within 3.29pp at >96% accuracy. At these margins, the ranking is not meaningfully testable — CIs likely overlap for VOTA vs. exception_only (99.77% vs. 100%, $\Delta$=0.23pp). The paper should state that DebugBench confirms the method does not degrade, rather than claiming it "preserves the ranking."

**W6 (Minor): Appendix is heavy; some content belongs in the main paper.**
The irreducible error analysis (GeneratorExit) is one of the paper's strongest methodological contributions but is relegated to the appendix. The training dynamics section (loss/accuracy decoupling) is interesting but tangential. Consider promoting the irreducible error analysis and demoting the training dynamics.

---

## Meta-Review: Consolidated Analysis

### Top Weaknesses Flagged by Multiple Reviewers

| # | Weakness | R1 | R2 | R3 | Severity |
|---|----------|----|----|-----|----------|
| 1 | **Task triviality / missing regex baseline** | — | W1 | — | Critical |
| 2 | **Narrow evaluation scope** (2 models, 1 dataset, Python only) | W4 | W2 | W1 | Critical |
| 3 | **Single-seed conditions** for non-headline results | W1 | — | — | Major |
| 4 | **VOTA confound used for narrative despite acknowledged limitations** | W3 | — | W3 | Major |
| 5 | **Overclaiming** (title, design principles, reframing language) | — | W3 | W1,W3 | Major |
| 6 | **Missing practical motivation** for the task | — | W5 | — | Moderate |

### Most Likely Rejection Reason

**"The task is too simple and the evaluation too narrow to constitute a sufficient contribution for EMNLP Main."**

A skeptical AC would synthesize R2-W1 (task triviality) and R2-W2 (narrow scope) into: the paper demonstrates that a binary classification task with an obvious feature (exception presence) is solvable by that feature, across two similar models on toy benchmarks. The decomposition (Claim 2) and hierarchy (Claim 3) are interesting but rely on single-seed estimates and apply only to this narrow setting. The cross-model story is weakened by the truncation confound.

Findings would be a more appropriate venue unless the evaluation scope is expanded.

### Priority Repair Order (for EMNLP Main acceptance)

**P0 — Must fix before submission (9 days):**

1. **Add a regex/heuristic baseline.** Implement `has_error = "[ERROR]" in trace` and report its accuracy. If it matches 99.83%, pivot the framing to: "SFT is unnecessary for exception-based verdict prediction; the contribution is the decomposition showing *why* simpler signals dominate." If it doesn't match (e.g., because the model handles edge cases like GeneratorExit differently), this becomes a strength.

2. **Run 3 seeds for `label_only` and `ae_only` on Qwen.** These are cheap experiments (~2h each × 2 extra seeds = ~8h total). Without them, Claims 2 and 3 rest on single-seed point estimates, which any methodological reviewer will flag.

3. **Soften the title.** "Exception Events Suffice for Verdict Prediction" or "Exception Events Are the Dominant Signal for Verdict Prediction: A Cross-Model Trace Ablation Study."

**P1 — Should fix:**

4. **Add a practical motivation paragraph** in the Introduction. Explain *when* verdict prediction without execution is useful (e.g., predicting test outcomes for candidate patches before execution to save CI compute; predicting flakiness; handling partial executions).

5. **Tighten the VOTA cross-model narrative.** Remove all instances where the 14.96pp gap is used to argue general model-dependence of rich representations. Instead, frame it as: "VOTA performance on DeepSeek is confounded by training-time truncation; the clean cross-model comparison is on exception_only (0.50pp gap)."

6. **Report deduplicated CIs as primary** for `exception_only` results, or use cluster-robust standard errors.

7. **Promote irreducible error analysis** to the main paper (even 1 paragraph in Discussion). This is one of the paper's strongest selling points.

**P2 — Nice to have:**

8. **Add one more model** (e.g., CodeLlama-7B or StarCoder2-7B) for `exception_only` to strengthen the "cross-model" claim. A single condition on a third model is ~2h of compute.

9. **Add one non-ML baseline** (logistic regression on binary exception-presence feature) to demonstrate that SFT adds value beyond the trivial feature.

10. **Acknowledge test outcome prediction literature** from SE in Related Work.

11. **Run DeepSeek ablation** for at least `ae_only` to test whether the two-tier hierarchy holds cross-model.

---

## Predicted Outcome

| Reviewer | Score | Likely disposition |
|----------|-------|--------------------|
| R1 (Methodology) | Borderline | Leans reject without multi-seed fixes |
| R2 (Domain/Skeptic) | Weak Reject | Needs scope expansion or framing pivot |
| R3 (Writing) | Weak Accept | Fixable with title change and tightening |
| **Meta** | **Borderline → likely Findings** | Main needs P0 fixes + ideally P1 |

**Bottom line**: The paper has a clean experimental design and honest reporting, but the task triviality concern and narrow scope are the primary threats. The P0 fixes (regex baseline, multi-seed, title) are feasible within 9 days and would shift the paper from "likely Findings" to "competitive for Main."
