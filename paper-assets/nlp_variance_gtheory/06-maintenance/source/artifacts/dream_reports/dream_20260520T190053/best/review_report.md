---
dream_id: dream_20260520T190053
tier: best
overall_score: weak reject
timestamp: 2026-05-20T19:49:23.440123+00:00
---

---
dream_id: dream_20260520T190053
tier: best
reviewer: R2
focus: Novelty and Related Work
timestamp: 2026-05-20T20:15:00+00:00
---

# Reviewer R2: Novelty and Related Work

## 1. Summary

This paper applies Generalizability Theory (G-theory) to LLM evaluation, crossing infrastructure facets (hardware, numerical precision) with methodology facets (prompt, seed, temperature, ordering) and item selection as the measurement facet. Across 6 models, 5 benchmarks, and 2M+ evaluation records, it finds that item selection dominates variance (42--58%), infrastructure--methodology interactions are negligible (<0.5%), and current evaluation practices yield G < 0.40. D-study projections provide reproducibility budgets, and a fine-tuning extension shows an inverted variance hierarchy. A vLLM engine confound (FP32 using a different backend) is identified and corrected.

## 2. Strengths

1. **The cross-benchmark variance gradient is a genuine empirical contribution.** Showing that item dominance systematically weakens from 58.4% (MMLU) to 42.1% (MATH) as task difficulty and reasoning demands increase, with temperature x item and seed x item interactions correspondingly increasing, is a well-supported quantitative finding. This gradient was intuited but never measured across this many benchmarks in a unified framework. It explains why prior single-benchmark studies reached apparently contradictory conclusions.

2. **The two-level separability decomposition is more nuanced than a binary answer.** Distinguishing aggregate-level separability (<0.5% direct interaction) from item-conditional interactions (14.2% combined) is a mature analytical move. The "empirical license with caveats" framing -- isolated-factor studies are valid on average but their conclusions are item-conditional -- is the right level of nuance and provides a useful guideline for future work.

3. **D-study reproducibility budgets fill a genuine practical gap.** Translating variance components into concrete recommendations (600 items, 3 prompts, 2 seeds for G >= 0.90 on MMLU; different budgets for other benchmarks) is immediately actionable. The cross-benchmark budget table showing that HellaSwag needs 550 items while MATH needs 1,100 is the kind of task-specific guidance the field lacks.

4. **The engine confound discovery is a standalone methodological contribution.** Identifying that vLLM routes FP32 through a different execution backend (V1 vs V0), inflating precision variance from 0.3% to 7.24% and creating an 8.5pp accuracy gap, is genuinely valuable to any researcher comparing precision modes. The before/after validation is convincing.

5. **The fine-tuning extension adds structural insight.** Demonstrating that the variance hierarchy inverts in fine-tuning (learning rate and seed dominate over items, explaining the "5 seeds, report mean +/- std" convention) is a non-trivial contribution that connects inference and training reproducibility.

6. **Experimental scale is impressive.** 7 experiments, 2M+ records, 6 models (7B--14B), 5 benchmarks spanning MC knowledge to multi-step reasoning, plus a fine-tuning scenario. Few empirical papers in this area match the breadth.

## 3. Weaknesses

### Major

**(W1) Incremental novelty over Mesting (2026).** The paper's stated methodological advance over Mesting is the addition of infrastructure facets (hardware, precision) to the G-theory design. But these infrastructure facets contribute negligibly: hardware main effect 1.2% (in Exp 3), precision 0.3%, direct infrastructure x methodology interactions <0.5%. The paper's strongest findings -- item dominance, the benchmark-dependent variance gradient, D-study budgets, the task-difficulty modulation -- would emerge from a Mesting-style design with fixed infrastructure. The infrastructure extension is effectively a confirmatory null result: infrastructure does not interact with methodology. This is useful information, but it is a confirmation, not a discovery. The paper frames the infrastructure crossing as the primary novelty ("first fully-crossed G-theory study spanning infrastructure and methodology"), yet the results demonstrate that crossing infrastructure was unnecessary for arriving at the main conclusions. The actual novelty lies elsewhere (cross-benchmark gradient, D-study budgets, engine confound), and the paper needs to honestly acknowledge that.

**(W2) Severely inadequate bibliography.** Seven references is far below the standard for a top-venue submission on evaluation methodology. Critical omissions include:

- **Bouthillier et al. (2021, JMLR), "Accounting for Variance in Machine Learning Benchmarks."** This is the closest ML-native predecessor: it decomposes benchmark variance via ANOVA across hyperparameters, data splits, initialization seeds, and implementation choices. Not citing it inflates the paper's apparent novelty -- the idea of factorial variance decomposition for ML evaluation is not new, and Bouthillier et al. established the template. The paper's claim of being the "first" to decompose variance across multiple factors needs qualification.

- **IRT-based item analysis in NLP.** Lalor et al. (2019, NAACL), Rodriguez et al. (2021, ACL), and Vania et al. (2021) have studied item-level properties in NLP benchmarks using Item Response Theory. The paper claims item selection is an overlooked variance source, but IRT researchers have been analyzing item difficulty, discrimination, and selection effects for years. The item dominance finding should be contextualized against this existing body of work.

- **Benchmark subsampling literature.** Polo et al. (2024, "tinyBenchmarks"), HELM-Lite, and Perlitz et al. (2023, "Efficient Benchmarking of LLMs") address the same practical question -- how many items suffice for reliable evaluation? -- from a different methodological angle (IRT-based subsampling vs. G-theory D-study). The D-study recommendations should be directly compared against these approaches.

- **Henderson et al. (2018), "Deep Reinforcement Learning that Matters."** A pioneering study on variance sources in ML evaluation (hyperparameters, implementations, environments, seeds). Foundational for the "variance in evaluation" literature that this paper belongs to.

- **Shavelson & Webb (1991), "Generalizability Theory: A Primer."** A canonical G-theory reference. The paper cites only Cronbach et al. (1972) for G-theory foundations, but the Shavelson & Webb primer and the full Brennan (2001) textbook are standard citations in any G-theory paper. The Brennan textbook appears in the task summary but not in the "best" paper's bibliography.

- **Lu et al. (2022) and Pezeshkpour & Hruschka (2024) on option ordering effects.** Directly relevant to the ordering facet. The paper includes ordering as a facet but does not cite any prior work on ordering sensitivity.

- **Dodge et al. (2020, "Fine-Tuning Pretrained Language Models: Weight Initializations, Data Orders, and Early Stopping."** Directly relevant to the fine-tuning G-study (Exp 6), which examines seed and data shuffle variance.

With only 7 references, the paper creates a misleading impression of operating in a vacuum. Expanding to 25+ references with proper contextualization is essential.

**(W3) Item dominance is partially expected from measurement theory -- the framing oversells it.** Any assessment instrument with a wide difficulty range will show item variance as the dominant source. This is a well-established property in psychometrics (Brennan, 2001, Chapter 3; Shavelson & Webb, 1991). MMLU spans trivial factual recall to expert-level reasoning; GSM8K spans single-step arithmetic to multi-step word problems. The paper's hook -- "Researchers debating whether to standardize prompts, seeds, or GPU hardware for LLM evaluation are optimizing the wrong knobs" -- oversells a finding that is, from a measurement theory perspective, expected. The contribution is in (a) quantifying the magnitude and (b) showing its benchmark-dependence, but the paper should acknowledge: "Item dominance is expected from measurement theory when item difficulty varies widely; our contribution is in quantifying its magnitude (42--58%), demonstrating its systematic variation with task reasoning demands, and deriving D-study implications specific to LLM evaluation."

**(W4) The "diagnostic tool" contribution is not substantiated.** Contribution 1 claims G-theory as a "practical diagnostic tool for evaluation pipeline designers" and mentions releasing 172,800+ records. But no software tool, library, or interactive diagnostic is provided. The "tool" is simply running G-theory analysis on evaluation data, which Mesting (2026) and GeneralizIT (2024) already provide. The paper contributes data and analysis, not a tool. Either substantiate the tool claim (e.g., release a pipeline that takes raw evaluation logs and produces variance decompositions + D-study recommendations) or reframe the contribution as "empirical analysis" rather than "diagnostic tool."

### Moderate

**(W5) The fine-tuning extension uses RoBERTa-large (355M, encoder-only, classification), which is architecturally distant from the 7--14B decoder-only autoregressive models in the inference experiments.** The claim that "these findings extend to fine-tuning settings" implies generalization across paradigms, but fine-tuning RoBERTa on SST-2 is a fundamentally different operation than fine-tuning Llama-8B with LoRA on a generation task. The variance hierarchy inversion (LR and seed dominating) may be specific to small encoder-only models on classification tasks with high baseline accuracy. Fine-tuning a decoder model would make the cross-paradigm claim far more credible. At minimum, the paper should explicitly qualify: "Our fine-tuning analysis is limited to encoder-only models on classification tasks and may not generalize to decoder-only fine-tuning."

**(W6) The "fully crossed" claim is overstated.** Only MMLU Exp 1 has the richest factorial design (4 models x 3 precisions x 6 prompts x 6 seeds x 3 temperatures x 4 orderings x 200 items). Other benchmarks use reduced designs (Exp 2: 2 precisions, 2 temperatures). The hardware experiment (Exp 3) uses only 2 GPU types with partial crossing (2/4 models on both). The paper's title and abstract claim a "fully-crossed" study, but only one of seven experiments is fully crossed. The other experiments are partially crossed replications with reduced designs, which is fine methodologically but should be honestly described.

**(W7) Zero figures is a serious presentation weakness for a paper about variance decomposition.** The distilled writing patterns from the field identify stacked-bar variance decomposition charts and D-study projection curves as expected idioms in this literature (Mesting 2026, Brittlebench 2026 both use them). With 11 tables and 0 figures, the paper buries its most visually compelling findings -- the cross-benchmark variance gradient, the D-study cost-effectiveness curves, the before/after engine confound comparison -- in dense tabular format. A stacked-bar chart showing variance components across 5 benchmarks would communicate the benchmark-dependency finding far more effectively than Tables 3--4. D-study projection curves showing G vs. item count for different benchmarks would make the budget recommendations intuitive. This is not cosmetic: at a competitive venue, reviewers have limited time, and visual communication of the key findings would substantially strengthen the paper's impact.

**(W8) The paper does not adequately address the relationship between its findings and the paper summary title claim.** The paper summary states the central finding is that "variance attribution patterns are benchmark-conditional and model-conditional -- no universal reproducibility recipe exists." This negative result framing is potentially powerful, but the paper itself leans more toward positive claims ("item selection dominates," "separability holds," "here are budgets"). The tension between these two framings is unresolved. If the central message is "no universal recipe," the paper should lead with how different benchmarks and models require different remediation strategies. If the central message is "item selection dominates," the paper should explain why this holds despite the benchmark gradient. The current framing tries to claim both simultaneously, which weakens both.

### Minor

**(W9)** The inference-fine-tuning correlation of r=0.15 (mentioned in the task summary) is never discussed in the paper text. If this is an actual finding, it reinforces the "no universal recipe" message and deserves discussion. If it was not computed, it should be.

**(W10)** The paper uses "first" language extensively ("first fully-crossed G-theory study," "first empirical evidence," "first formal test of separability"). Priority claims require thorough literature review to sustain, and with only 7 references, these claims are vulnerable.

## 4. Missing Related Work

The following lines of work should be discussed:

| Missing Reference | Why It Matters |
|---|---|
| Bouthillier et al. (2021, JMLR) | ML-native variance decomposition across hyperparameters, data splits, seeds. Direct predecessor. |
| Lalor et al. (2019, NAACL); Rodriguez et al. (2021, ACL) | IRT-based item analysis in NLP. Item dominance is not a new observation in this community. |
| Polo et al. (2024, "tinyBenchmarks"); Perlitz et al. (2023) | Benchmark subsampling -- addresses "how many items?" from IRT perspective. D-study budgets should be compared. |
| Henderson et al. (2018) | Variance in ML evaluation (RL). Established the field's awareness of seed/implementation variance. |
| Shavelson & Webb (1991); Brennan (2001) | Canonical G-theory references. A G-theory paper with only Cronbach 1972 is under-cited. |
| Dodge et al. (2020) | Seed, data order, early stopping variance in fine-tuning PLMs. Directly relevant to Exp 6. |
| Lu et al. (2022); Pezeshkpour & Hruschka (2024) | Option ordering effects in MC evaluation. Relevant to the ordering facet. |
| Bui et al. (2025) | Seed sensitivity in fine-tuning LLMs. In the project's own literature map but not cited in the paper. |
| "Same Prompt, Different Outcomes" (2026) | Seed/sampling variance. Also in the literature map but absent from the paper. |
| GeneralizIT (2024) | G-theory software tool for ML. Relevant to the "diagnostic tool" framing. |

## 5. Questions for Authors

1. How do your D-study item budget recommendations compare to IRT-based subsampling approaches (tinyBenchmarks, HELM-Lite)? These methods also answer "how many items suffice?" -- what does G-theory add beyond what IRT already provides?

2. The infrastructure extension is the claimed methodological advance over Mesting (2026), but infrastructure contributes <1% of variance. If you ran the same study with fixed infrastructure (single GPU, single precision), which of your three contributions would change? Please be specific.

3. You claim G-theory as a "diagnostic tool" (Contribution 1), but no software or pipeline is released. What exactly is the tool? Is it the G-theory framework itself (which Mesting already applied), the data release, or something else?

4. Item dominance (42--58%) is expected from psychometric theory when item difficulty varies widely. How do you respond to the concern that this finding is partially tautological? What would it mean for item dominance *not* to hold -- would that indicate a problem with the assessment, the analysis, or the theory?

5. The fine-tuning experiment uses RoBERTa-large on classification tasks. Would you expect the same inverted variance hierarchy if fine-tuning a 7B decoder model on a generation task (e.g., Llama-8B with LoRA on GSM8K)? What is your basis for generalizing across architectures?

6. Your literature map includes 10 papers (Bui 2025, "Same Prompt Different Outcomes" 2026, GeneralizIT 2024, etc.), but the paper cites only 7. Why were the other 3 dropped? More critically, why are there no citations to the IRT item analysis literature, the benchmark subsampling literature, or the ML variance decomposition literature (Bouthillier et al., Henderson et al.)?

7. The paper has zero figures. The distilled writing patterns from your own field analysis identify stacked-bar charts and D-study curves as expected idioms. Was this a deliberate choice? What would a Figure 1 (variance decomposition across benchmarks) add to the narrative?

## 6. Score

**Score: 3/6 (Weak Reject)**

The paper presents a large-scale empirical study with genuine practical value (D-study budgets, engine confound fix, cross-benchmark gradient). However, the novelty claim rests on infrastructure crossing that yields near-null results (<0.5% variance), the bibliography is severely inadequate (7 references, missing entire lines of relevant work), the item dominance finding is partially expected from measurement theory but oversold, and the "diagnostic tool" contribution is unsubstantiated. The actual novelty -- cross-benchmark variance gradient, task-specific budgets, confound identification -- is real but needs honest reframing and thorough contextualization against related work that currently goes unacknowledged.

## 7. Confidence

**Confidence: 4/5**

I am familiar with the G-theory literature, the LLM evaluation reproducibility literature, and the IRT/benchmark subsampling work. My main uncertainty is whether the full Bouthillier et al. (2021) framework is sufficiently different in scope that the "first" claims could be partially defended, and whether there are very recent (2026) papers in this space that I have not seen.