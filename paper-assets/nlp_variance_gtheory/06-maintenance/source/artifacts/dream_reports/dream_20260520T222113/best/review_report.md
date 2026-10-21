---
dream_id: dream_20260520T222113
tier: best
overall_score: weak accept (4/6)
timestamp: 2026-05-20T23:52:25.256921+00:00
---

# Reviewer R1: Methodology Soundness and Experimental Rigor

## 1. Summary

This paper applies Generalizability Theory (G-theory) to decompose variance sources in LLM evaluation across five benchmarks (MMLU, ARC-Challenge, HellaSwag, GSM8K, MATH), six models (4 at 7--9B, 2 at 14B), and approximately 4 million evaluation records. The design crosses infrastructure facets (numerical precision, GPU hardware) with methodology facets (prompt template, random seed, temperature, option ordering) and a measurement facet (item selection). Three claims are advanced: (1) item dominance is benchmark-conditional, following a monotonic 35pp gradient from knowledge retrieval (56%) to complex reasoning (21%); (2) direct infrastructure x methodology interactions are negligible (<0.3%), confirming separability; (3) D-study reproducibility budgets reverse across task types (MMLU is item-limited, GSM8K is seed-limited), rendering universal evaluation recipes illusory. Eight experiments are presented, including a model-as-facet reanalysis, item resampling stability test, multi-hardware separability test, 14B scale extension, RoBERTa fine-tuning study, LayerCast precision mitigation, and MATH benchmark extension.

---

## 2. Methodology Assessment

### 2.1 G-Theory Application

The application of G-theory is broadly correct and represents a natural fit for the research question. The crossed random-effects design, with item as the measurement facet and prompt/seed/temperature/ordering/precision as crossed facets, is the canonical G-theory setup for studying measurement dependability. The paper correctly distinguishes G-studies (variance decomposition) from D-studies (projection under alternative designs), which is the primary advantage of G-theory over standard ANOVA.

**However, there are several methodological concerns:**

**(a) Object of measurement is underspecified.** In classical G-theory, the "object of measurement" (the entity whose score you want to generalize) must be clearly defined. In educational testing, this is typically the person. Here, the paper appears to treat benchmark accuracy as the object, but accuracy is an aggregate over items -- not a single observation. The paper decomposes item-level binary responses (correct/incorrect), which means the effective object of measurement is the *item-level response*. The G coefficient then measures how well item-level responses generalize across facet conditions. This is a valid but nonstandard application. The paper should explicitly state what universe score is being estimated and what generalization is being made. The current framing conflates "reliability of a benchmark score" with "stability of item-level responses across conditions," and these are different quantities.

**(b) Model-as-fixed vs. model-as-facet transition is handled well but incompletely.** The paper correctly identifies that pooling across models inflates item_id (from 56% to 49.2% on MMLU when model is added as a facet). The model x item interaction (10.2%) is properly extracted. However, the paper does not discuss whether model should be treated as random or fixed from a G-theory perspective. With only 4 models drawn from a specific population (7-9B instruction-tuned open-weight models), the "random" assumption implies these 4 are a random sample from some universe of models -- a dubious claim given the deliberate selection. If model is fixed, model x item is not an error component but a systematic interaction, and the G coefficient computation changes. The paper should discuss this inferential scope issue.

**(c) Henderson Method I vs. III naming inconsistency.** The paper claims "Henderson's Method III (expected mean squares)" in Section 3.1, but the balanced fully-crossed design used here would typically employ Henderson Method I (which uses Type-I sums of squares and expected mean squares for balanced designs). Method III is Searle's approach for unbalanced designs. For the balanced design in exp-001, Method I is both simpler and more appropriate. This is either a naming error or an implementation concern -- the paper should clarify which method was actually used and verify consistency with the code.

**(d) Binary response variable creates floor/ceiling artifacts.** All primary analyses use binary correct/incorrect as the response. For items near 0% or 100% accuracy across conditions, variance is mechanically compressed (a Bernoulli variable with p near 0 or 1 has low variance). This means item_id partially reflects the *range* of item difficulties rather than genuine measurement-relevant variance. The logprob analysis in Appendix B (item_id drops to 42.8%) partially addresses this, but it is relegated to a 4-line appendix rather than being integrated into the main analysis. A continuous response variable would provide a more principled decomposition, and the paper should discuss the implications of using binary outcomes for variance component estimation.

### 2.2 Crossed/Nested Design Appropriateness

The fully crossed design for MMLU (exp-001) is the gold standard for G-theory and is correctly specified. All facet levels are combined with all other facet levels, enabling clean estimation of all main effects and two-way interactions.

The reduced designs for non-MMLU benchmarks (2 precisions x 2 temperatures vs. 3 x 3 for MMLU) are a pragmatic budget-driven decision but create a methodological asymmetry that is inadequately discussed. Variance percentages are *relative to total variance*, and the total variance changes when you remove facet levels. Removing the FP32 precision level (which shows the highest deviation post-confound-fix) and the third temperature level changes the denominator of all percentage calculations. The cross-benchmark gradient (Table 4) compares percentages from designs with different factorial structures, which is a validity concern. The paper should either: (a) report a sensitivity analysis re-running MMLU with the reduced 2x2 design to confirm the gradient holds under matched designs, or (b) explicitly discuss why the design asymmetry does not invalidate the comparison.

### 2.3 Bootstrap Procedures

The bootstrap procedure (1,000 item-level resamples) is appropriate in principle for constructing CIs on variance components, as parametric CIs for variance components in mixed models are notoriously unreliable. However:

**(a) Resampling items with replacement in a balanced design creates duplicates.** With 200 items and replacement, each bootstrap draw contains approximately 127 unique items (by the coupon collector / birthday problem). Duplicate items have identical response vectors across all conditions, violating the independence assumption in the ANOVA decomposition. This likely *deflates* the variability of item_id estimates (making CIs too narrow), because the resampled datasets have artificially correlated item effects. A cluster bootstrap that resamples item-condition blocks without re-indexing duplicates, or a delete-d jackknife, would be more appropriate. The tight CI widths (4-6pp) should be interpreted with this caveat.

**(b) Nested bootstrap for D-study projections is not described.** The D-study projections in Table 11 presumably require computing variance components for each bootstrap sample and then projecting G under hypothetical designs. This is a two-stage procedure (bootstrap variance components -> project G), and the uncertainty in G projections depends on the joint distribution of all variance components, not just item_id. The paper reports CIs on item_id but not on D-study projections. The claim that "420 items suffice for G >= 0.90 on MMLU" has no associated uncertainty -- but given the bootstrap CIs on item_id (46.1-52.3%), the projected item count for G >= 0.90 could range substantially. This uncertainty should be reported.

---

## 3. Experimental Rigor

### 3.1 Exp 1b: Item Resampling Stability

The resampling stability test uses 1 model (Llama-3.1-8B) x 1 benchmark (MMLU) x 3 independent 200-item samples x 54 conditions per sample = 32,400 records. The CV of 4.1% on item_id across samples is reassuring but has limited generalizability:

- **Only 1 model tested.** The paper claims item resampling stability as a general property, but models with different accuracy distributions (e.g., Mistral-7B at 64.1% vs. Gemma-2 at 69.1%) might show different resampling sensitivity. A model near the population mean difficulty could show lower CV than one at the extremes.
- **Only 3 samples.** A CV computed from 3 data points has essentially no statistical power. The standard error of a CV from n=3 is enormous. The paper would be better served by reporting the bootstrap distribution of variance components (which they have from exp-004, 1000 resamples) as the stability analysis, rather than the 3-sample CV.
- **Only MMLU.** The critical question is whether resampling stability holds for GSM8K and MATH, where item_id is much lower (21-25%) and closer to competing components. A CV of 4.1% on a 55% estimate is comfortable (55 +/- 2.3pp). But a CV of 4.1% on a 21% estimate would be 21 +/- 0.9pp -- still rank-1, but now within striking distance of temp x item at 20.8%. The resampling stability argument is weakest precisely where it matters most (reasoning benchmarks), and it is not tested there.

**Recommendation:** Replace the 3-sample CV with the bootstrap CI analysis from exp-004, and extend item resampling stability to at least one reasoning benchmark (GSM8K or MATH).

### 3.2 200-Item Sample Size

Using 200 stratified items per benchmark is a reasonable choice that balances statistical power against computational cost. The stratification (by MMLU subject, presumably by difficulty for other benchmarks) ensures representative coverage. However:

- For MMLU (14K total items), 200 items is 1.4% of the pool -- adequate for stable percentage-based decompositions.
- For GSM8K (1,319 items in the test set), 200 items is 15.2% -- a much larger fraction, which reduces the effective resampling space.
- For MATH (5,000 items in the test set), 200 items is 4% -- again adequate.
- For ARC-Challenge (1,172 items), 200 items is 17.1%.

The paper does not discuss how the item pool size interacts with the variance decomposition. When sampling 15-17% of the pool (GSM8K, ARC), the resampling stability results from MMLU (1.4% sampling fraction) may not transfer. This should be acknowledged.

### 3.3 Hardware Experiment (Exp 3): Confounds

The multi-hardware study uses 2 GPU types. This is a minimal design for estimating hardware effects. Specific concerns:

- **n=2 GPU types provides 1 degree of freedom for the hardware main effect.** This is barely identifiable in a variance decomposition. The hardware main effect (0.4%) and hardware x item (1.6%) estimates are based on between-GPU differences that could reflect any systematic difference between the two specific GPUs (driver version, cooling, memory controller characteristics, vLLM kernel selection), not hardware architecture per se.
- **The paper does not specify the second GPU type.** The review context mentions "RTX PRO 6000 + second GPU" but the paper says only "2 GPU types." For a claim about hardware separability to be meaningful, readers need to know whether these are architecturally similar (e.g., two Ampere-class GPUs) or substantially different (e.g., Ampere vs. Hopper). Two GPUs from the same architecture family would underestimate hardware variance.
- **No confound control for driver/CUDA version differences between GPUs.** If the two GPUs run different CUDA toolkit versions or vLLM builds, observed differences reflect the software stack, not the hardware.

Despite these limitations, the separability conclusion (<0.3% direct infra x method) is robust: even if hardware variance is underestimated due to limited GPU diversity, the *interaction* with methodology would need to be orders of magnitude larger to matter. The null result is defensible.

### 3.4 Fine-Tuning Experiment (Exp 6): RoBERTa

Using RoBERTa-large for the fine-tuning study is a significant architectural mismatch. The inference experiments use 7-14B decoder-only autoregressive models on generation tasks; the fine-tuning experiment uses a 355M encoder-only model on classification tasks. The facets are also different (learning rate and data shuffle replace prompt template and temperature). This means:

- The cross-paradigm comparison (Table 13) compares variance percentages from incomparable designs. Item_id being rank-1 in both does not constitute evidence of cross-paradigm generalization -- it could reflect the fact that any assessment with varying item difficulties will show item dominance, which is a tautological property of the design rather than an empirical finding.
- The claim that "infrastructure effects are negligible in fine-tuning too" is trivially expected for RoBERTa-large, which has no autoregressive error accumulation and was trained in FP32/FP16.
- The 1,728 fine-tuning runs (432 per task x 4 tasks) is a reasonable scale, but the number of *items* per evaluation is not specified. If each run evaluates the full dev/test set, the item-level observation count is much larger than 1,728.

**The experiment adds limited value to the core narrative.** Fine-tuning a decoder LLM (e.g., Llama-3.1-8B with LoRA on GSM8K, crossing seed x learning rate x data shuffle x items) would directly test cross-paradigm generalization. The current RoBERTa experiment tests a different claim entirely: that G-theory can decompose fine-tuning variance in encoder-only classification, which is unsurprising given that the same framework has been used in educational testing (which also involves classification-like assessments).

### 3.5 14B Scale Extension (Exp 5)

With n=2 models (Qwen3-14B, DeepSeek-R1-Distill-14B), this experiment has minimal statistical power for any claim about scale effects. The two models differ in both scale and architecture: DeepSeek-R1-Distill-14B is a reasoning-distilled model with fundamentally different training objectives than Qwen3-14B. Scale and training methodology are fully confounded.

The finding that both 14B models fall within the 8B range for item_id is reassuring but does not demonstrate scale invariance -- it demonstrates that these two specific 14B models have similar variance profiles to the four 8B models. The elevated temp x item (8.8%) and seed x item (5.2%) for DeepSeek-R1-Distill-14B is attributed to "reasoning distillation introducing implicit chain-of-thought tendencies" (Section 8.1) -- this is a plausible but untestable hypothesis from n=1.

The experiment contributes at best weak corroborating evidence. Two more 14B models (ideally from different training paradigms) would make the scale claim credible.

### 3.6 LayerCast (Exp 7)

This is a null result experiment: LayerCast adds 0.03% precision variance, which is negligible. The experiment is methodologically clean but its contribution is marginal -- it confirms that precision is not a major concern (already established by exp-001 post-confound-fix) and evaluates a specific mitigation technique. For the paper's core claims, it is dispensable. Its inclusion creates a breadth-over-depth tradeoff that weakens the overall narrative.

---

## 4. Statistical Concerns

### 4.1 CV = 4.1% from 3 Samples

The original review context described CV = 33% from 3 samples -- the paper now reports CV = 4.1%, which is a dramatic improvement, presumably reflecting better stratification and larger item counts in the revised design. However, a CV computed from n=3 is a point estimate with essentially no precision. The 95% CI on a CV from 3 observations is extremely wide (roughly 0.7x to 5x the point estimate under normal assumptions). The paper should not present CV = 4.1% as a precise number but rather as "CV < 15%" or similar bounded claim.

### 4.2 Bootstrap with 1,000 Resamples

1,000 bootstrap resamples is adequate for percentile-based 95% CIs (Monte Carlo error approximately 0.5pp for the tail quantiles). The concern is not the number of resamples but the resampling unit: resampling items with replacement in a balanced design creates duplicate observations that violate independence assumptions in the ANOVA decomposition used within each bootstrap iteration. This is a known problem in bootstrap variance component estimation. The bias direction is toward underestimating CI width.

### 4.3 D-Study Projection Uncertainty

D-study projections are deterministic functions of variance components: given estimated components, the projected G under any hypothetical design is a closed-form calculation. The uncertainty comes entirely from the variance component estimates. The paper reports CIs on item_id (Table 8) but not on D-study projections. This is a significant omission. The practical recommendation "use 420 items for G >= 0.90 on MMLU" has no associated uncertainty band. If item_id is at the upper end of its CI (52.3%), more items are needed; if at the lower end (46.1%), fewer suffice. The authors should propagate bootstrap uncertainty through the D-study projection to report a CI on the required item count.

### 4.4 D-Study Projection for GSM8K: Arithmetic Anomaly

Table 10 shows that reducing items from 200 to 150 while keeping prompts=3 and seeds=10 *increases* G from 0.68 to 0.90. In the G formula, reducing n_items should *decrease* G (because item-related error terms are divided by n_items). The only way G can increase with fewer items is if the optimization simultaneously changes other facet counts or if the table presents results from a joint optimization that is not monotonic in each facet individually. This anomaly is not explained and raises questions about the D-study optimization procedure. If the procedure involves multi-facet grid search, it should be documented; if it is an error, it should be corrected.

---

## 5. Coverage vs. Depth

The paper runs 8 experiments across 20 tables. Several experiments feel thin:

- **Exp 5 (14B):** n=2 models, confounded scale/architecture, 1 paragraph of analysis. Contributes weak corroboration.
- **Exp 7 (LayerCast):** Null result for a specific mitigation technique. One table, 1 paragraph. Could be a footnote.
- **Exp 6 (Fine-tuning):** Architecturally disjoint from the main study. Two tables, 2 paragraphs. The cross-paradigm claim it supports is unsustainable with encoder-only models.

**Recommendation:** Move Exp 5, 6, and 7 to an appendix. Use the freed space for: (a) figures -- the paper has zero figures, which is a critical presentation weakness for a variance decomposition study; (b) deeper analysis of the core gradient (Exp 1+2+8), including per-item analysis showing which items drive the benchmark-conditional variance shift; (c) D-study sensitivity analysis with propagated bootstrap uncertainty.

Fewer, deeper experiments would produce a stronger paper. The current breadth creates an impression of thoroughness but at the cost of inadequate depth on several secondary experiments.

---

## 6. Strengths

- **Cross-benchmark variance gradient is a genuine contribution.** The monotonic shift from item-dominated (56%) to interaction-dominated (21%) across five benchmarks, with non-overlapping bootstrap CIs, is novel, well-supported, and explanatory. It resolves the apparent contradiction between prior single-benchmark studies.
- **Experimental scale is impressive.** Over 1M records for the MMLU full-factorial alone; approximately 3-4M total. This is among the largest factorial designs in the LLM evaluation literature.
- **Engine confound discovery is independently valuable.** The identification and correction of the vLLM FP32/BF16 engine routing difference (V1 CUDA graph vs. V0 eager) is a methodological contribution that benefits any researcher using vLLM for precision-sensitive comparisons.
- **D-study facet effectiveness inversion is the most actionable finding.** Items:seeds ratio shifting from 14.2:1 (MMLU) to 0.8:1 (GSM8K) has direct practical implications. This is the quantitative crystallization of "no universal recipe."
- **Model-as-facet reanalysis properly handles model heterogeneity.** Extracting model x item (10.2% on MMLU) while preserving item_id as rank-1 and the gradient is a clean analytical move that addresses a legitimate concern from prior reviews.
- **Separability confirmation is useful.** While a null result, confirming <0.3% direct infrastructure x methodology interaction across all benchmarks provides empirical license for isolated-factor study designs.
- **REML vs. Henderson sensitivity analysis** with <1.4pp divergence and identical component rankings adds robustness.
- **Item resampling stability** (despite the n=3 limitation) provides evidence that the variance structure is not an artifact of specific item selection.

---

## 7. Weaknesses

### Major

- **(W1) D-study optimization procedure is undocumented.** The joint-optimal allocations in Table 11 (e.g., GSM8K: 150 items, 3 prompts, 10 seeds) appear to come from a multi-facet grid search, but the paper describes only single-facet D-study sweeps. The GSM8K anomaly (150 items yielding G=0.90 while 200 items with the same prompts/seeds yields G=0.68) is unexplained and arithmetically suspicious. Practitioners will use these specific numbers; they must be derived from a transparent procedure.
- **(W2) Object of measurement and G coefficient interpretation.** The paper conflates the G coefficient (which measures generalizability over included facets relative to the universe of admissible observations) with overall measurement reliability. G = 0.22 for "current practice" on MMLU does not mean MMLU is unreliable in a practical sense -- it means that item-level binary responses are not stable across prompt/seed/temperature conditions. Since practitioners use *aggregate accuracy* (averaging over 200+ items and potentially multiple conditions), the effective reliability of the aggregate score is much higher. The paper's alarming framing ("below the minimum threshold accepted in any measurement discipline") risks misleading practitioners by applying item-level G to benchmark-level decisions.
- **(W3) Bootstrap resampling with replacement in balanced designs.** Duplicate items in bootstrap samples violate the independence assumption of the within-bootstrap ANOVA, likely producing CIs that are too narrow. This affects the statistical significance claims for the gradient (non-overlapping CIs across benchmarks). The paper should report results from a cluster bootstrap or jackknife as sensitivity analysis.
- **(W4) Cross-benchmark design asymmetry.** Comparing variance percentages across benchmarks when MMLU uses 3 precisions x 3 temperatures and others use 2 x 2 is methodologically questionable. The total variance denominator differs, and removing facet levels redistributes percentage shares. No sensitivity analysis is provided.
- **(W5) Zero figures.** For a paper about variance decomposition across benchmarks, the absence of any visualization is a critical presentation failure. Stacked-bar charts, D-study projection curves, and bootstrap CI forest plots are standard idioms in this literature and would dramatically improve communication of the key findings.

### Moderate

- **(W6) Fine-tuning experiment (Exp 6) is architecturally mismatched.** RoBERTa-large on classification tasks does not test cross-paradigm generalization to decoder-only LLM fine-tuning. The different facet structure (LR/shuffle vs. prompt/temperature) makes the comparison non-parallel.
- **(W7) 14B scale extension (Exp 5) has n=2 with confounded scale/architecture.** Cannot separate scale effects from training methodology effects (reasoning distillation).
- **(W8) Item resampling stability tested on only 1 model x 1 benchmark x 3 samples.** Not tested on reasoning benchmarks where the stability claim matters most.
- **(W9) Hardware experiment uses only 2 unspecified GPU types.** The second GPU is never identified, and n=2 provides minimal diversity for hardware variance claims.
- **(W10) Missing comparison with IRT-based benchmarking.** tinyBenchmarks recommends approximately 100 items for MMLU; the D-study recommends 420. This 4x discrepancy is never discussed. Since both address "how many items suffice?", the paper should explain why the answers differ and what each framework optimizes.

---

## 8. Questions for Authors

1. **D-study arithmetic:** In Table 10 (GSM8K), how does reducing items from 200 to 150 (with identical prompts=3, seeds=10) increase G from 0.68 to 0.90? This appears to violate the monotonicity of G in n_items. Please describe the exact optimization procedure and verify these numbers.

2. **Object of measurement:** What is the universe score being estimated? Is it the expected accuracy of a model on the full item population, or the expected item-level response across all facet conditions? These yield different G coefficients, and the practical implications differ substantially. If the former, how do you handle the aggregation from items to benchmark score in the G formula?

3. **Bootstrap validity:** Have you conducted any calibration study (e.g., comparing bootstrap CIs to parametric REML-based CIs or to a delete-d jackknife) to verify that your bootstrap procedure produces correct coverage? Given the duplicate-item concern, what is the effective number of unique items per bootstrap sample, and have you assessed whether this deflation affects CI width?

4. **Design asymmetry:** If you re-run the MMLU analysis using only 2 precisions (BF16/FP16) and 2 temperatures (matching the non-MMLU design), does item_id remain at approximately 56%, or does it shift? How large is the shift, and does the gradient survive with matched designs across all benchmarks?

5. **G interpretation for practitioners:** Your D-study says MMLU needs 420 items for G >= 0.90. But the standard MMLU evaluation uses the full 14K items with 1 prompt and 1 seed. What is the G coefficient for the full 14K-item, 1-prompt, 1-seed evaluation? If it is already above 0.90 (which it likely is, given that item-related error shrinks with 70x more items), the practical alarm about "current practice being inadequate" is overstated.

---

## 9. Score

**Score: 4/6 (Weak Accept)**

**Justification:** The paper presents a large-scale, technically competent G-theory analysis with a genuinely novel primary finding (the cross-benchmark variance gradient) that has both explanatory and practical value. The engine confound discovery is independently valuable. The D-study facet effectiveness inversion is the most actionable result. However, several methodological concerns prevent a higher score: (a) the D-study optimization procedure contains an unexplained arithmetic anomaly and is not documented; (b) the G coefficient interpretation risks misleading practitioners by conflating item-level generalizability with benchmark-level reliability; (c) the bootstrap procedure has a known bias from duplicate items in balanced designs; (d) the cross-benchmark gradient is derived from designs with different factorial structures; (e) secondary experiments (Exp 5, 6, 7) are thin and architecturally mismatched. The core contribution -- the gradient + D-study reversal -- merits publication, but the paper needs honest scoping of what its G coefficients actually measure, documented D-study optimization, design-matched gradient validation, and figures.

---

## 10. Confidence

**Confidence: 4/5**

I have working knowledge of G-theory (Brennan 2001, Shavelson & Webb 1991), variance component estimation methods (Henderson, REML), bootstrap procedures for mixed models, and the LLM evaluation reproducibility literature. My main uncertainty is whether the D-study anomaly in Table 10 reflects a multi-facet optimization procedure that I am not recognizing, and whether the binary-response decomposition introduces biases beyond what I have identified. I am confident in the assessment of the experimental design, the bootstrap validity concern, and the G coefficient interpretation issue.
