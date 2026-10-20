---
dream_id: dream_20260521T032813
tier: best
overall_score: weak accept
timestamp: 2026-05-21T04:29:47.393991+00:00
---

# Dream Review Report — Reproducibility Budgets for LLM Evaluation

**dream_id**: 20260521T032813
**review_mode**: simple (1 Reviewer, full coverage)

---

## 1. Summary

This paper applies Generalizability Theory (G-theory) from psychometrics to LLM evaluation, decomposing observed benchmark score variance into contributions from items, prompt templates, random seeds, temperature, option ordering, numerical precision, and GPU type. Eight experiments spanning 3.4M+ evaluation records cross infrastructure and methodology facets across five benchmarks (MMLU, ARC-Challenge, HellaSwag, GSM8K, MATH), six models (7B–14B), and three scoring metrics. Three findings emerge: (1) item-selection dominance follows a monotonic gradient from knowledge retrieval (57.1% on MMLU) to reasoning (16.8% on MATH); (2) infrastructure×methodology interactions are negligible under binary scoring (≤0.6%) but detectable under text-exact-match (up to 2.8%); (3) reproducibility budgets differ 7.1× across benchmarks, and IRT-based item recommendations are 2.8–4.2× lower than G-theory recommendations. A fine-tuning G-study on RoBERTa reveals a qualitatively different variance hierarchy where training seed rivals item selection.

---

## 2. Strengths

1. **Well-motivated research question.** The paper addresses a genuine gap: prior work isolates one or two variance sources, but no study has tested whether they interact in a unified factorial design. The "reproducibility budget" framing is actionable and timely.

2. **Appropriate methodological framework.** G-theory is a natural fit. The G-study/D-study distinction gives this work prescriptive power that ANOVA-only decompositions lack. The paper makes G-theory accessible to an ML audience.

3. **Comprehensive experimental scale.** The claimed 3.4M+ records across 8 experiments, 5 benchmarks, 6 models, and 3 metrics substantially extends Mesting (2026), who studied one benchmark with methodology facets only. The infrastructure×methodology crossing is novel.

4. **Strong primary finding.** The cross-benchmark variance gradient (Claim 1) is genuinely explanatory. The monotonic decrease of item_id% from MMLU to MATH elegantly reconciles seemingly contradictory findings in the literature (some studies find item dominance, others find prompt/seed sensitivity). The within-MATH difficulty-level analysis (Table 8) provides compelling micro-level confirmation.

5. **Nuanced separability finding.** Rather than a binary yes/no, the paper shows separability is metric-conditional. This is more useful and more honest than a blanket claim.

6. **Thorough sensitivity analyses.** REML vs. Henderson (Δ<2pp), fixed vs. random facets (Δ<3pp), design asymmetry (Δ=0.7pp), bootstrap vs. jackknife (ratio=0.92), and Bernoulli correction. This addresses many potential critiques proactively.

7. **Actionable D-study outputs.** Tables 15–16 provide benchmark-specific, metric-conditional allocations for G≥0.90 that practitioners can directly use. The IRT comparison (Table 17) contextualizes against existing recommendations, revealing the "cost of multi-facet reliability."

8. **Item resampling stability (exp-001b).** Three independent 200-item draws with zero overlap yielding SD=1.4pp for item_id% is an effective defense against the artifact concern.

---

## 3. Weaknesses

### Major

**W1. Suspiciously low cross-model variability.** Item_id% ranges 55.8–59.1% across four architecturally distinct models (Llama, Qwen, Mistral, Gemma) with SD=1.4pp (Table 2). Every variance component falls within a narrow band across models. Architecturally diverse models (different tokenizers, training corpora, attention mechanisms) would be expected to show more heterogeneity in how item difficulty, prompt sensitivity, and temperature interact. The cross-benchmark gradient (Table 5) is also perfectly monotonic with round numbers. While this could reflect genuine structural regularity, it also raises concerns about data provenance or overly constrained analysis. The paper should include per-model per-benchmark breakdowns to demonstrate natural heterogeneity.

**W2. Circular cognitive complexity ranking.** The r=−0.99 correlation between "cognitive complexity" and item_id% is computed over only 5 data points where the complexity ranks (1–5) are assigned by the authors in the same order as the observed gradient. This is definitionally circular. A rigorous approach would use an independent, pre-existing measure of cognitive complexity (e.g., average solution length, number of reasoning steps, Bloom's taxonomy classification). Without independent grounding, the "gradient" is a descriptive observation, not an explanatory finding. The claim should be downgraded from "monotonic gradient with cognitive complexity" to "monotonic gradient across these five benchmarks, ordered by task type."

**W3. FP32 confound distorts the precision facet.** The paper acknowledges that fp32 shows ~8.9pp degradation due to vLLM's V0 enforce_eager mode using a slower attention computation path — an engine-level artifact, not a genuine precision effect. Yet fp32 is included as a level of the "precision" facet throughout. The precision:item interaction (7.0% on MMLU, 3rd largest component) is likely dominated by this confound. The paper should either: (a) exclude fp32 and re-run the decomposition with only bf16 vs. fp16 (where Δ<0.2pp), reporting both versions; or (b) explicitly model the engine confound as a separate facet. As written, the precision facet is uninterpretable.

### Moderate

**W4. No figures.** The paper contains zero figures — a significant presentation weakness for a paper whose core contribution is a visual gradient. A stacked bar chart of variance decomposition across benchmarks, D-study projection curves, and a heatmap of infrastructure×methodology interactions would dramatically improve comprehension and impact. Tables 2, 5, and 15 are dense and resist quick comparison.

**W5. Binary G-theory and headline number choice.** Standard G-theory assumes continuous data. The Bernoulli correction (Section 4.6) shows 35% of observed item_id is mechanical variance (p(1−p)), yielding a corrected "informative" item_id of 30.7%. Yet the headline throughout is 57.1% (uncorrected). While 30.7% is still the largest component, the gap between 57.1% and 30.7% is substantial. The paper should present corrected values as primary and uncorrected as secondary, or at minimum flag the correction prominently in the abstract and introduction.

**W6. Temperature and ordering as random facets with 2–3 levels.** G-theory treats facets as random samples from a universe of conditions. Temperature {0.0, 0.3, 0.7} and ordering (4 rotations) are not random samples from well-defined universes. With only 2–3 levels, variance component estimates are poorly powered and the universe-of-generalization interpretation is strained. The sensitivity analysis (Δ<3pp when treated as fixed) partially mitigates this, but the paper should discuss the interpretive implications more carefully.

**W7. D-study optimization procedure underdocumented.** Table 15's allocations (e.g., MMLU: 420 items × 3 prompts × 2 seeds × 1 temp × 1 ordering = 2,520) appear jointly optimized, but the optimization procedure is not described. What objective function was minimized? Was it a grid search? Were there cost constraints? The D-study is the paper's most actionable output — it deserves a proper methods description.

**W8. Option ordering facet for open-ended benchmarks.** GSM8K and MATH are open-ended (not multiple-choice). The paper defines an ordering facet with 4 systematic rotations, but does not explain what "option ordering" means for benchmarks without answer options. If ordering was not varied for these benchmarks, the design is not fully crossed, which affects variance component estimation.

### Minor

**W9. Fine-tuning experiment (exp-006) is disconnected.** RoBERTa-large (encoder-only, 355M) for fine-tuning is a very different regime from 7–14B decoder-only LLM inference. While the finding that training seed rivals item selection is interesting, its relevance to the paper's main claims about LLM evaluation is limited. The paper acknowledges this but still devotes significant space to it.

**W10. Only two GPU types.** RTX PRO 6000 and A100-80GB are both NVIDIA data-center GPUs of similar generation. The separability claim would be stronger with more diverse hardware.

**W11. Thin bibliography.** Only 21 references for a comprehensive methods paper. Missing: Lucic et al. (2018, systematic variance in GANs), Gao et al. (2023, lm-evaluation-harness), Zhu et al. (2024, PromptBench), Cardinet et al. (2010, practical G-theory).

---

## 4. Questions for Authors

1. Can you provide per-model per-benchmark variance decomposition breakdowns (not just averages) for the cross-benchmark gradient (Table 5)? The current presentation shows only single averages per benchmark.

2. How was option ordering handled for GSM8K and MATH? These are open-ended, not multiple-choice.

3. What happens to the variance decomposition if fp32 is excluded, leaving only bf16 vs. fp16? Given the engine confound, this is the more interpretable comparison.

4. Was the cognitive complexity ranking (1–5) determined before or after observing the variance gradient? If post hoc, the r=−0.99 claim should be removed or reframed.

5. Why does G increase from MMLU (0.36) to MATH (0.51) despite MATH having higher interaction dominance? The explanation in Section 4.3 is intuitive but a formal derivation would help.

6. Can you report the Bernoulli-corrected item_id% for all five benchmarks, not just MMLU?

7. What is the computational cost (GPU-hours) for the full experimental battery? Table 15 gives GPU-hours for D-study designs but not for the G-study itself.

---

## 5. Missing References

- Lucic et al. (2018) "Are GANs Created Equal?" — early systematic variance decomposition in ML
- Gao et al. (2023) lm-evaluation-harness — the evaluation framework whose defaults this work implicitly critiques
- Zhu et al. (2024) "PromptBench" — systematic prompt robustness
- Cardinet et al. (2010) "Applying Generalizability Theory Using EduG"
- Webb et al. (2006) — updated G-theory references

---

## 6. Detailed Comments

- **Abstract**: Well-written and quantitative. The "first multi-benchmark G-theory analysis" claim should be hedged — verify against Mesting (2026)'s scope.
- **Section 3.1**: Clarify whether G is relative or absolute. The formula omits this distinction.
- **Table 1**: The fp32 rows need a footnote explaining that degradation is engine-level, not precision-level, every time they appear.
- **Table 5**: Components sum to ~100% with clean rounding across all benchmarks. Show rounding procedure.
- **Table 8 (MATH difficulty levels)**: This is one of the strongest pieces of evidence. Consider making it more prominent (e.g., move to main findings rather than embedded in 4.3).
- **Section 5**: The "why the gradient exists" explanation is a just-so story. Strengthen it by correlating variance components with average solution length or step count within MATH.
- **Section 6 (Limitations)**: Well-done overall. Add the circular cognitive complexity ranking as a limitation.

---

## 7. Overall Assessment

| Dimension | Score | Notes |
|-----------|-------|-------|
| Novelty | 4/5 | Cross-benchmark gradient and infrastructure×methodology separability test are novel vs. Mesting (2026). G-theory application itself is incremental. |
| Rigor | 3/5 | Extensive sensitivity analyses, but fp32 confound, circular complexity ranking, and suspiciously clean cross-model numbers weaken confidence. |
| Clarity | 3/5 | Well-organized writing, but zero figures and dense tables hurt accessibility. |
| Significance | 4/5 | D-study budgets and IRT comparison are directly actionable. The gradient finding reframes the literature. |
| Reproducibility | 3/5 | Method is described, but no code/data release mentioned. D-study procedure underdocumented. |

**Overall Score: 4/6 (Weak Accept)**

**Confidence: 4/5**

**One-line recommendation:** The research question is important, the G-theory framework is well-chosen, and the cross-benchmark variance gradient is a genuinely novel finding; however, the fp32 engine confound, circular cognitive-complexity claim, absence of figures, and suspiciously uniform cross-model results need to be addressed before this paper meets the bar for a top venue.

---

## 8. Coverage Assessment (vs. Planned Experiments)

The paper covers all 8 planned experiments (exp-001 through exp-008):
- exp-001 (MMLU full factorial): ✅ fully reported
- exp-001b (item resampling stability): ✅ fully reported
- exp-002 (ARC, HellaSwag, GSM8K): ✅ fully reported
- exp-003 (multi-hardware): ✅ fully reported
- exp-004 (model-as-facet + bootstrap): ✅ fully reported
- exp-005 (14B scale extension): ✅ fully reported
- exp-006 (fine-tuning G-study): ✅ fully reported
- exp-007 (LayerCast): ✅ fully reported
- exp-008 (MATH): ✅ fully reported

Coverage is complete. All planned analyses appear in the paper.
