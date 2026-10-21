---
dream_id: dream_20260517T075852
tier: worst
overall_score: borderline reject
timestamp: 2026-05-17T09:06:38.804839+00:00
---

# Dream Review Report: "Characterizing Recursive Generation Depth: Feature-Based Estimation, Degradation Atlas, and Boundary Conditions"

**Venue**: EMNLP 2026 Main  
**Review mode**: Full (2 Reviewers, 4-step roundtable)  
**Scoring basis**: ACL Rolling Review (ARR) form, 1-5 scale with half-point increments

---

## Step 1: Independent Reviews

### Reviewer 1 (R1) — Focus: Methodology + Experiments

**Summary**: The paper formalizes ordinal generation depth estimation as a 4-class classification task, constructs a 3-model x 3-strategy x 4-depth benchmark, and trains RF classifiers on 19 Pythia-160M-derived statistical features, achieving 70-85% accuracy under controlled conditions. The primary contribution is the Depth Degradation Atlas, which reveals perplexity tail statistic universality, non-uniform inter-depth distances (formalized as EDD), and strategy-dependent trajectory reversal. Section 5 systematically characterizes three boundary conditions (scale, generation mode, domain shift) under which the signal attenuates.

**Strengths**:
- Well-defined problem formalization with clear distinction from binary AI-text detection. The ordinal structure is properly motivated by the data curation use case.
- Thorough 3x3 experimental atlas with systematic evaluation across all model-strategy combinations. Table 1 is informative and well-structured.
- Feature universality finding is robust: p90_ppl and var_surprisal consistently dominate across all 9 cells, connecting to Dohmatob et al.'s (2024) tail-erosion theory.
- Unusually honest reporting of negative results (DCOL failure, cross-strategy breakdown, inconclusive curation implications) and boundary conditions. The paper does not overclaim.
- EDD metric is well-defined (Equation 1) and provides a useful framework for quantifying discriminability limits.
- Boundary condition characterization (Section 5) is comprehensive: three dimensions (scale, generation mode, domain) each with dedicated experiments, tables, and mechanistic explanations.

**Weaknesses (Major)**:
- **M1: No statistical significance testing on main results (Table 1).** The 9-cell atlas reports point estimates without confidence intervals. Are the inter-cell differences (e.g., Pythia top-k 70.3% vs GPT-2 XL temp 85.4%) statistically significant? The 5-fold CV provides fold-level estimates that could yield CIs, but none are reported. This is a notable gap for an empirical characterization paper.
- **M2: No comparison with existing AI-text detectors adapted for ordinal depth.** Binoculars and Fast-DetectGPT produce continuous perplexity-based scores that could be calibrated or thresholded for ordinal depth estimation. Not comparing against these obvious baselines leaves the contribution poorly contextualized. The paper only mentions zero-shot LLMs in passing but does not present formal baseline comparisons.
- **M3: d0 separability inflates headline metrics.** d0v1 AUC > 0.99 across all settings means d0 recall > 98%, trivially inflating the 70-85% four-class accuracy. The practically relevant metric is d1-d3 three-class accuracy. The paper reports this in some tables but the Abstract and Introduction lead with the inflated 4-class number.
- **M4: Reference model dependency is underexplored.** All experiments use Pythia-160M as the sole reference model. The cross-scale perplexity measurement gap (Section 5.1) is correctly identified as the bottleneck for 14B, but no alternative reference models are tested at scale (e.g., using a 7B reference for 14B outputs). This leaves open whether the boundary conditions are fundamental or artifacts of the Pythia-160M choice.

**Weaknesses (Minor)**:
- Sample size justification is missing. Why 1,000 passages per condition? No power analysis or convergence curve is provided.
- The 19 features are standard in AI-text detection literature. No exploration of whether additional features (e.g., intrinsic dimension per Tulchinskii et al. 2024) could improve performance.
- LoRA target modules are not specified. Different target modules may produce different depth signals.

**R1 Scores**: Overall 3.0, Soundness 3.0, Excitement 3.0, Confidence 4, Reproducibility 3.5

---

### Reviewer 2 (R2) — Focus: Novelty + Related Work

**Summary**: The paper applies Random Forest classification on 19 perplexity-derived statistical features to estimate how many recursive fine-tuning cycles text has undergone. The core method is standard (RF on known features); the contribution rests on the task formalization, systematic experimentation across a controlled grid, and the boundary condition analysis showing where the approach fails.

**Strengths**:
- Clear task formalization with practical motivation. The distinction between shallow and deep recursive text for data curation is well-argued.
- The strategy-dependent trajectory reversal (Section 4.4) is the most novel empirical finding. Temperature sampling causing d1v2 AUC to collapse to 0.13 in cross-strategy LOO is genuinely surprising and has both scientific and practical implications.
- Boundary condition framing (Section 5) is intellectually honest. Characterizing where a method fails is valuable, especially when the failures are systematic and mechanistically explained.
- Negative DCOL result (Section 4.5) is informative for the community, showing that end-to-end learning faces inherent difficulties on this task.

**Weaknesses (Major)**:
- **M1: Limited novelty beyond systematic experimentation.** The core method is RF on perplexity statistics, both of which are standard tools. The finding that perplexity tails capture depth is predicted by existing model collapse theory (Dohmatob et al. 2024). The "Atlas" is descriptive rather than predictive and does not transfer to new models/strategies without re-running the full pipeline.
- **M2: Ecological validity gap is fundamental.** Under all three boundary conditions tested, EDD collapses from 3 to 1, meaning ordinal depth estimation degrades to binary real-vs-synthetic detection. The practical framing (data curation, early warning) is undermined by: (a) 50% accuracy under prompted generation, (b) 55% at 14B, (c) 23-30% FPR on web-crawl. In realistic scenarios, multiple boundary conditions would compound simultaneously.
- **M3: Cross-strategy transfer is broken for practical use.** Cross-strategy LOO d1-d3 accuracy of ~46% (chance 33%) and the d1v2 AUC inversion (0.13 for GPT-2 XL temp) mean the method requires knowing the decoding strategy a priori. The two-stage pipeline in Discussion (Table 10) confirms this: predicted two-stage (70.6%) underperforms naive pooled (72.0%) because strategy classification at 57.5% is insufficient.
- **M4: Scale degradation raises questions about future relevance.** At 14B, accuracy drops to 55% with EDD=1. As frontier models grow to 70B+, the Pythia-160M reference model's perplexity landscape may become entirely uninformative. The paper does not address whether this approach has a viable scaling path.

**Weaknesses (Minor)**:
- ~22 references is thin for EMNLP. Missing important related work: multi-class provenance estimation, large-scale data filtering pipelines (FineWeb, DataComp), distribution testing methods (MMD, KL divergence).
- The curation PoC mentioned in Discussion is inconclusive, weakening the practical motivation.
- Discussion section is compressed. The cross-strategy pipeline results deserve fuller treatment.

**R2 Scores**: Overall 2.5, Soundness 3.5, Excitement 2.0, Confidence 4, Reproducibility 4.0

---

## Step 2: Cross-Sharing

**R1 findings shared with R2**:
- R1 notes the absence of CIs on Table 1, which R2 had not flagged. R2 agrees this is a gap but considers it minor relative to the novelty concerns.
- R1's concern about reference model dependency at scale resonates with R2's point about future relevance. Both agree this is a structural limitation.

**R2 findings shared with R1**:
- R2's argument that the main finding (perplexity tails capture depth) is predicted by existing theory (Dohmatob et al. 2024) is accepted by R1 as reducing the novelty of the Atlas. R1 adjusts: the Atlas's value is more in the systematic measurement than in surprising discoveries.
- R2's point about missing calibrated detector baselines (Binoculars, Fast-DetectGPT) is strongly endorsed by R1. Both agree this is a significant experimental omission.
- R2's framing of the ecological validity problem as compound (multiple boundary conditions would apply simultaneously in practice) sharpens R1's concern.

---

## Step 3: Convergence

**Agreed strengths**:
1. Task formalization is novel and well-motivated (both reviewers)
2. Experimental thoroughness is commendable (both reviewers)
3. Honest limitation reporting builds credibility (both reviewers)
4. Strategy-dependent trajectory reversal is the most novel finding (both reviewers)
5. Feature universality (p90_ppl, var_surprisal) is a genuine empirical contribution (both reviewers)

**Agreed weaknesses**:
1. Missing calibrated detector baselines (Binoculars, Fast-DetectGPT adapted for ordinal depth). This is the most significant experimental gap.
2. d0 inflation of headline metrics. The 70-85% number is misleading; d1-d3 discrimination is the hard problem.
3. Ecological validity gap is fundamental. All three boundary conditions collapse EDD to 1, and real-world scenarios would compound these conditions.
4. Cross-strategy transfer is broken and the two-stage pipeline does not help (predicted < naive pooled).
5. Reference model (Pythia-160M) dependency limits both scale and practical applicability.

**Disagreement resolved**:
- R1 initially scored Soundness 3.0 vs R2's 3.5. After discussion, both converge to **3.0**: the experiments are thorough within their scope, but the missing baselines and absent CIs on the main table prevent a "strong" soundness rating.
- R1 scored Excitement 3.0 vs R2's 2.0. After R2's argument that the core findings are predicted by existing theory and the practical applicability is severely constrained, R1 adjusts to **2.5**. R2 adjusts slightly upward to **2.5**, acknowledging the strategy-dependent trajectory finding has genuine scientific value. Converged: **2.5**.

---

## Step 4: Consolidated Assessment

### Paper Strengths (ranked by importance)

1. **Novel task formalization**: Ordinal generation depth estimation is a genuine gap between binary AI-text detection and model collapse characterization. The problem is well-defined, practically motivated, and no prior work addresses it directly.

2. **Strategy-dependent trajectory reversal**: The finding that temperature sampling causes feature-boundary reversal at the d1/d2 interface (cross-strategy LOO d1v2 AUC = 0.13) is scientifically interesting and practically important. The mechanistic explanation (uniform logit scaling accelerates convergence to attractor distribution) is convincing.

3. **Honest boundary characterization**: Section 5 systematically maps where the method fails. This is unusually transparent for a submission and provides genuine value by delineating the scope of feature-based approaches.

4. **Feature universality**: p90_ppl and var_surprisal consistently dominate feature importance across all 9 model-strategy cells, connecting empirical findings to theoretical predictions about tail erosion in recursive generation.

5. **EDD metric**: A clean formalization of discriminability limits that could be reused in future work on recursive generation analysis.

### Paper Weaknesses (ranked by severity)

1. **[Critical] Missing calibrated detector baselines**: Existing perplexity-based detectors (Binoculars, Fast-DetectGPT) produce continuous scores that could be directly calibrated for ordinal depth estimation. Not comparing against these baselines makes it impossible to assess whether the 19-feature RF approach offers any advantage over simpler existing methods adapted to the ordinal setting. This is the most significant experimental gap.

2. **[Major] Ecological validity collapses under realistic conditions**: Under each of three boundary conditions (14B scale, prompted generation, web-crawl domain), EDD collapses from 3 to 1, reducing ordinal depth estimation to binary real-vs-synthetic detection. In practice, multiple conditions would compound. The practical framing (data curation) is therefore unsupported by the evidence.

3. **[Major] Limited methodological novelty**: The method (RF on perplexity summary statistics) uses entirely standard tools. The primary finding (perplexity tails capture depth) follows from existing model collapse theory. The "Atlas" is a systematic experiment, not a reusable methodology or predictive framework.

4. **[Major] Cross-strategy transfer is fundamentally broken**: The d1v2 AUC inversion and the failure of the two-stage pipeline (predicted 70.6% < naive pooled 72.0%) mean the method is unusable without prior knowledge of the decoding strategy. This severely limits the practical contribution.

5. **[Moderate] d0 inflation of headline metrics**: The Abstract's "70 to 85% four-class accuracy" is inflated by near-perfect d0 detection. The d1-d3 three-class problem, which is the practically relevant task, achieves substantially lower accuracy.

6. **[Moderate] No confidence intervals on main results (Table 1)**: An empirical characterization paper should report uncertainty on its primary measurements. The 5-fold CV structure permits bootstrap CIs, but none are provided.

7. **[Minor] Thin reference list (~22 citations)**: Missing coverage of multi-class provenance detection, large-scale data filtering pipelines, and distribution testing methods. Below typical EMNLP density.

8. **[Minor] Single reference model (Pythia-160M)**: No alternative reference models tested at scale. The cross-scale perplexity gap may be solvable with scale-matched references, but this is untested.

### Questions for Authors

1. **Calibrated detector baselines**: Can Binoculars or Fast-DetectGPT scores be calibrated for ordinal depth estimation? If so, how does RF on 19 features compare? If not, why?

2. **Compound boundary conditions**: What happens when multiple boundary conditions apply simultaneously (e.g., prompted generation from a 14B model on web-crawl data)? The paper tests each dimension independently but real scenarios compound them.

3. **Scale path**: Given that Pythia-160M's perplexity landscape compresses the depth gradient at 14B, have you considered scale-matched reference models (e.g., 7B reference for 14B outputs)? Is there a principled way to select reference models?

4. **d0 reframing**: Would you consider reporting d1-d3 three-class accuracy as the primary metric, given that d0 detection is trivial?

5. **Cross-strategy practical guidance**: Given the pipeline failure, what is the practical recommendation for a data curator who does not know the decoding strategy used? Is the method usable in any realistic deployment scenario?

### Experiment Coverage Assessment

Comparing against the full experiment design (review_context.yaml):

| Experiment | Status | Paper Coverage |
|---|---|---|
| DCOL ablation (plan_010) | Cancelled (DCOL failed) | Section 4.5 covers DCOL failure adequately |
| 13B FP16 validation (plan_014) | Expected 55% acc, EDD=1 | Section 5.1, Table 3: 55% acc, EDD=1. Fully covered. |
| Wild-data calibration (plan_015) | Expected 23-30% FPR | Section 5.3, Table 8: 23-30% FPR. Fully covered. |
| Prompted generation (plan_016) | Expected 50% acc, EDD=1 | Section 5.2, Tables 5-7: 50% acc, EDD=1. Fully covered. |
| Cross-strategy pipeline (plan_017) | Expected 57.5% clf, predicted < naive | Discussion + Table 10: 57.5% clf, 70.6% < 72.0%. Covered. |

All planned experiments are present in the paper. Coverage is complete.

### Consolidated Scores

| Dimension | R1 | R2 | Consolidated | Justification |
|---|---|---|---|---|
| **Overall** | 3.0 | 2.5 | **2.5** | Borderline Findings / resubmit. The task formalization and experimental thoroughness support a Findings-level contribution, but the missing baselines, limited novelty, and collapsed ecological validity prevent a confident Findings recommendation. |
| **Soundness** | 3.0 | 3.5 | **3.0** | Acceptable. Experiments are thorough within scope, but missing CIs on main results and absent calibrated detector baselines are significant gaps for an empirical paper. |
| **Excitement** | 3.0 | 2.0 | **2.5** | Borderline interesting. The strategy-dependent trajectory finding is genuinely novel, but the core method is standard, the main finding is predicted by theory, and practical applicability is severely limited. |
| **Confidence** | 4.0 | 4.0 | **4.0** | Both reviewers are confident in their assessment. The paper's scope is well within reviewers' expertise. |
| **Reproducibility** | 3.5 | 4.0 | **3.5** | Mostly reproducible. Hyperparameters are specified, but some implementation details (LoRA targets, Wikipedia subset, exact feature computation) need clarification. Code release would resolve this. |

### Recommendation

**Borderline Findings / Resubmit** (Overall 2.5). The paper addresses a genuinely novel task with commendable experimental thoroughness and intellectual honesty. However, three issues prevent acceptance: (1) no comparison with existing detectors adapted for ordinal depth, leaving the contribution's magnitude unclear; (2) the method uses entirely standard tools (RF on perplexity statistics) with findings largely predicted by existing model collapse theory; (3) ecological validity collapses under all tested realistic conditions, with EDD universally dropping to 1. The strategy-dependent trajectory reversal is the strongest finding and could anchor a more focused paper. For resubmission, we recommend: (a) adding calibrated Binoculars/Fast-DetectGPT baselines, (b) providing CIs on all main results, (c) either demonstrating a viable scaling path (scale-matched reference models) or reframing the contribution as purely diagnostic/scientific rather than practically applicable.
