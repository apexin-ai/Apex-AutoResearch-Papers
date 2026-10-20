---
dream_id: dream_20260521T075006
tier: best
overall_score: 7 - Good paper, minor issues
timestamp: 2026-05-21T08:42:40.638488+00:00
---

# Reviewer 1 (R1): Methods and Experiments

## 1. Summary

This paper applies Generalizability Theory (G-theory) to LLM evaluation, crossing infrastructure (numerical precision, GPU hardware) with methodology (prompt, seed, temperature, ordering) and measurement (item) factors across five benchmarks and six models. The primary finding is a cross-benchmark variance gradient: item dominance decreases monotonically from MMLU (42.1%) to MATH (18.1%) while model×item interaction increases from 33.6% to 50.8%, explaining contradictory conclusions in prior isolated-factor studies. The paper also shows infrastructure×methodology separability under binary scoring, demonstrates G-theory requires 3.6–4.6× more items than IRT, and provides benchmark-specific reproducibility budgets.

## 2. Strengths

- **Ambitious and well-executed factorial design.** The crossed design spanning ~4.2M records across 5 benchmarks, 6 models, 2 GPU architectures, and multiple methodological facets is substantially more comprehensive than any prior work in this space. The scale alone makes the empirical contribution significant.

- **The cross-benchmark variance gradient is a genuine and valuable finding.** The perfectly monotonic decrease of item_id (42.1% → 18.1%) and increase of model×item (33.6% → 50.8%) across five benchmarks ordered by reasoning complexity is both clean and explanatory. This directly resolves the apparent contradiction between prior studies that each championed "their" variance source as dominant.

- **Thorough robustness package.** The paper addresses essentially every methodological objection a reviewer could raise: binary data validation via null simulation (737.5× ratio), REML confirmation of Henderson I estimates (<0.5pp deviation), bootstrap vs. jackknife CI agreement, fixed vs. random facet sensitivity (<3% change), item resampling stability (CV < 6%), design asymmetry check (<1pp bias), and power analysis. This is unusually thorough for this type of empirical study.

- **Out-of-sample D-study validation is compelling.** The leave-one-model-out validation showing 3-model predictions match 4-model actuals within Δ≤0.007 across all benchmarks provides genuine evidence that D-study projections are trustworthy, not just extrapolations.

- **Honest handling of the FP32 confound.** Rather than hiding the vLLM enforce_eager confound, the authors discovered it, characterized it (§4.1.1 / Table 3), excluded FP32 from subsequent analyses, and reported the BF16-vs-FP16 sensitivity (0.0006%). This is a model of transparent methodology.

- **IRT vs. G-theory comparison fills a real gap.** Quantifying that G-theory requires 3.6–4.6× more items than IRT, and that at IRT's recommended 116 items the G-theory G is only 0.529, gives practitioners a concrete and actionable calibration between the two frameworks.

- **Logprob scoring replication (Table 8 in paper).** Showing the gradient is preserved under logprob scoring rules out the concern that binary scoring creates the gradient as an artifact.

## 3. Weaknesses

- **The "perfectly monotonic" gradient relies on n=5 data points with a post-hoc ordering.** The five benchmarks are ordered by "reasoning complexity," but this ordering is imposed by the authors, not derived from an independent measure. With only 5 points, any ordering has a 1/120 chance of being monotonic by chance. A Spearman ρ = −1.0 on 5 points has p ≈ 0.017 (one-tailed), which is borderline significant. The paper would benefit from (a) an independent operationalization of "reasoning complexity" (e.g., average chain-of-thought length, number of reasoning steps) and (b) additional benchmarks to strengthen this claim. As stated in Limitations, the authors acknowledge n=5 is thin, but the claim is the paper's primary contribution.

- **Confounding between reasoning complexity and other benchmark properties.** MMLU uses 4-choice MC; GSM8K and MATH use free-form generation. HellaSwag uses completion format. The gradient may partially reflect format differences (MC vs. free-form) or answer-space size rather than pure reasoning complexity. The paper's mechanistic interpretation (§5.3) attributes the gradient to knowledge-vs-reasoning, but format is an uncontrolled confound. ARC-Challenge (4-choice MC, but item_id = 28.5%) partially disentangles this, but more analysis is needed.

- **Model diversity is limited and non-random.** Four 7–9B models from different families is reasonable but modest. Treating model as a "crossed random facet" in G-theory requires that the sampled models represent a broader universe of models. All four are instruction-tuned, open-weight, roughly same scale, trained on substantially overlapping data. The 14B extension with only 2 models is too small for reliable variance estimation (acknowledged by the G_item drop from 0.820 to 0.808). The generalizability to API models, much larger models (70B+), or base (non-instruction-tuned) models is unknown. The paper scopes this in Limitations, but it constrains how broadly the "reproducibility budgets" can be recommended.

- **REML convergence issue.** The actual REML run in the codebase (cross_model_reml.json) shows `"converged": false` with only 100 iterations and 2 models. The paper claims "REML-EM (500 iterations, practical convergence Δ<0.002)" — this discrepancy needs clarification. Was a separate REML run done with 500 iterations that did converge? The 2-model REML data shows item_id at 38.4% and model×item at 26.4%, which differs from the 4-model Henderson I values of 42.1% and 33.6% reported in the paper. The authors attribute this to "design differences (factor selection), not estimator bias" — this explanation is plausible but the discrepancy should be more transparently discussed.

- **The D-study budget optimization procedure is underdocumented.** Table 6 provides specific configurations (e.g., MMLU G≥0.80: 414 items, 3 prompts, 3 seeds, 2 orderings), but the paper does not describe how these particular allocations were selected. Is this a grid search? Constrained optimization? The D-study code (`d_study.py`) only implements single-facet sweeps with other facets held at MVP levels — it does not implement the joint optimization needed to produce Table 6. This gap between the code and the claimed results is concerning.

- **Bootstrap CI widths are wide enough to challenge some qualitative claims.** The MMLU item_id CI is [36.0, 48.8] — a 12.8pp range. The model×item CI is [28.4, 37.9]. Since these CIs overlap substantially, the claim that item_id > model×item on MMLU is not statistically decisive. On ARC-Challenge, the CIs for item_id [22.4, 35.2] and model×item [34.1, 47.0] show the reverse ordering is plausible. The gradient narrative is built on point estimates; CI-aware language would be more appropriate.

- **Text-exact-match metric is underdeveloped.** The paper frames "metric-conditional reproducibility" as a contribution but the text-exact-match analysis receives only brief treatment. The abstract mentions it; the hardware section references it; but no full cross-benchmark text-metric gradient is provided. The dual-metric framing from the project planning (D002) is largely absent from the final paper.

- **No correction for multiple comparisons across the 17 sub-analyses.** With 17 robustness analyses, some false positives are expected. The paper does not discuss any correction or address the family-wise error rate.

## 4. Questions for Authors

1. **Monotonicity significance:** Have you tested whether the 5-benchmark gradient is significantly monotonic beyond chance? A permutation test on the Spearman correlation would be informative. Would the gradient survive if you shuffled HellaSwag and ARC-Challenge (whose item_id values, 36.2% vs 28.5%, have overlapping bootstrap CIs)?

2. **Format confound:** Can you disentangle "reasoning complexity" from "answer format" (MC vs. free-form)? For instance, what happens if GSM8K is evaluated in MC format (as some benchmarks allow)?

3. **REML discrepancy:** The cross_model_reml.json shows 2 models, 100 iterations, and non-convergence. Which REML run corresponds to the "500 iterations, Δ<0.002" claim in the paper? Can you provide the converged REML variance components for the full 4-model design?

4. **D-study optimization:** How exactly were the joint facet allocations in Table 6 determined? The released d_study.py code only sweeps one facet at a time. Is there additional optimization code not yet released?

5. **Model universe:** G-theory treats model as a random facet, implying the 4 models sample from a universe. What is that universe? All open-weight 7–9B instruction-tuned models? All LLMs? The interpretation of G_item depends on this definition.

6. **Binary data treatment:** You cite Jiang & Skorupski (2017) on logistic-link G-theory but do not implement it. Given that r=0.42 between Bernoulli p(1-p) and observed item variance, how much of the item_id component is mechanically attributable to item difficulty via the Bernoulli variance link? Could you report a "corrected" item_id that removes this mechanical component?

7. **Higher-order interactions:** Three-way interactions account for 6.2%. Is this decomposition stable across benchmarks, or is 6.2% specific to MMLU?

## 5. Minor Issues

- Table 1 in the paper shows "residual+other" at 11.5% for cross-model, but the experiment_data.json shows 5.4% for "residual_and_higher_order" in cross-model. The paper's §5.7 states the original residual was 19.5%. These three numbers are inconsistent and need reconciliation. The paper text (Section 5.1) also references a "residual" of 19.5% that differs from Table 1's 11.5%.

- The paper abstract says "345,600 MMLU records" but Section 4.5 reports 930,400 total MMLU records (including all precision conditions). The 345,600 figure appears to be for a specific subset. This should be clarified.

- Table 5 (cross-benchmark) in the paper summary mentions "HellaSwag 28.1%" for item dominance, but the actual paper Table 5 (Table \ref{tab:gradient}) shows HellaSwag at 36.2%. The paper summary provided to reviewers appears to contain numbers from an earlier version.

- The G-coefficient formula in Eq. 2 should explicitly state which facets are in the denominator — as written, it is ambiguous whether fixed facets contribute to the error term.

- Section 5.3 states "item dominance monotonically decreasing from MMLU (42.1%) to MATH (18.1%)" — the word "monotonically" should be qualified given n=5 and overlapping CIs.

- The bibliography has several incomplete entries (e.g., Brittlebench lacks full author names; several "et al." entries lack co-author counts).

- The paper mentions "2.9M evaluation records" in the abstract but Section 4.5 sums to ~4.2M. This arithmetic discrepancy needs correction.

- Figure references in the text are absent — the paper mentions no figure numbers despite the framing document planning 5 figures. If figures exist, they should be referenced; if not, the text reads as incomplete.

## 6. Dimension Scores

| Dimension | Score | Justification |
|-----------|-------|---------------|
| **Soundness** | 7/10 | The G-theory application is technically correct for balanced designs. Henderson I is appropriate and REML confirmation strengthens confidence. The binary data concern is adequately addressed. However, the REML convergence discrepancy, the undocumented D-study optimization, and the borderline statistical significance of the n=5 gradient monotonicity claim are genuine concerns. The Bernoulli variance linkage (r=0.42) is acknowledged but not corrected for. |
| **Experimental rigor** | 8/10 | The factorial design is exemplary in scale and comprehensiveness. The robustness package (9 validation analyses) is unusually thorough. The FP32 confound handling is commendable. Weaknesses: the format confound across benchmarks is unaddressed, model diversity is limited (4 models of similar scale/type), and the 14B extension with 2 models is underpowered for variance estimation. |
| **Reproducibility** | 7/10 | The paper provides substantial detail on the experimental design, inference stack (vLLM 0.9.2), and analysis pipeline. The released code covers variance decomposition and D-study. However: the D-study optimization code for Table 6 appears missing, the REML implementation has a convergence discrepancy, and the multi-benchmark/multi-hardware experiments lack released code. The item sampling procedure (stratified-random) is described but the specific items are not identified. |
| **Presentation of results** | 7/10 | Tables are clear and well-organized. The single-model vs. cross-model comparison (Table 1) is effective. The gradient table (Table 5) clearly communicates the main finding. Weaknesses: no figures in the reviewed version (a significant omission for a paper whose primary finding is a visual gradient), inconsistent residual values across tables and text, arithmetic discrepancies between abstract and methods, and bootstrap CIs should be integrated into gradient claims rather than relegated to a separate robustness section. |

## 7. Overall Score: 7/10

**Justification:** This is a good paper with a genuinely valuable empirical contribution. The cross-benchmark variance gradient is the right finding at the right time — it resolves real confusion in the literature about which variance sources matter. The experimental scale (4.2M records, 5 benchmarks) and robustness package are impressive. The IRT comparison and D-study budgets have direct practitioner value.

The paper falls short of "strong" (8) because: (1) the primary claim (monotonic gradient) rests on n=5 benchmarks with a post-hoc ordering and overlapping CIs; (2) format confounds are not disentangled from reasoning complexity; (3) model diversity is limited; (4) there are several data inconsistencies between the code artifacts and the paper text (REML convergence, residual values, record counts); and (5) the absence of figures in this version weakens the presentation of what should be a visually compelling gradient story.

The methodological framework is sound, the robustness analyses are thorough, and the practical implications (benchmark-specific budgets, IRT calibration) are actionable. With the gradient claim appropriately qualified and the inconsistencies resolved, this would be a solid accept at AAAI.

## 8. Confidence: 4/5

I am confident in this assessment. I have expertise in variance decomposition methods, G-theory, and LLM evaluation methodology. I verified claims against the underlying code and data artifacts. The one area where I am less certain is the appropriateness of treating binary data in standard G-theory versus generalized G-theory — the authors' defense is reasonable but the psychometric literature is divided on this point.
