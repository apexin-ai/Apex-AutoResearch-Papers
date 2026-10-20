---
dream_id: dream_20260521T044739
tier: best
overall_score: borderline accept
timestamp: 2026-05-21T05:53:06.951774+00:00
---

# Dream Review Report: Reproducibility Budgets for LLM Evaluation

**Paper**: "Reproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics"

**Venue**: AAAI (1-10 scale)

**Review Mode**: Full (2 Reviewers + Roundtable)

---

## Reviewer Assignments

- **R1** — Methods and Experiments (soundness, statistical methodology, design rigor)
- **R2** — Novelty and Related Work (originality, positioning, significance, writing)

---

## R1 Review: Methods and Experiments

### Summary
The paper applies G-theory to decompose LLM evaluation variance across infrastructure, methodology, and measurement facets, with model as a crossed random facet. Nine experiments totaling ~4.3M item-level records yield three claims about item dominance, infrastructure-methodology separability, and benchmark-conditional reproducibility budgets. The experimental scope is ambitious and the methodological defense package (MD1-MD9) is unusually thorough for this literature.

### Strengths

1. **Well-motivated factorial design.** The fully crossed MMLU design (4 models × 3 precisions × 6 prompts × 6 seeds × 3 temperatures × 4 orderings × 200 items) is the most comprehensive variance decomposition in LLM evaluation. Crossing infrastructure with methodology—rather than studying them in isolation—directly tests an implicit field assumption.

2. **Correct statistical implementation.** Henderson's Method III for balanced and REML for unbalanced designs are the right choices. Negative-variance truncation to zero is standard. D-study partition (fixed facets to universe score, random to error) is correctly implemented.

3. **Exemplary robustness analyses (MD1-MD9).** Particularly strong: (a) Bernoulli null simulation showing item_id = 0.08% vs observed 61.1% (671× ratio); (b) REML vs Henderson III comparison (max divergence 1.4%, rank preserved); (c) bootstrap vs jackknife CI comparison (width ratio 0.96–1.04); (d) fixed vs random sensitivity (<3% change).

4. **Item resampling stability (Exp 2).** Three independent stratified 200-item draws with item_id CV = 0.039 and preserved rank order (Friedman p > 0.10) directly addresses the most common criticism of subsampled evaluation studies.

5. **Cross-benchmark gradient is convincing.** Monotonic decrease of item_id from MMLU (60.4%) to MATH (22.1%) with ρ = 1.0 across 5 benchmarks, accompanied by inverse increases in prompt×item and temp×item, provides an elegant reconciliation of seemingly contradictory prior findings.

6. **Power analysis preempts underpowering criticism.** Power > 0.998 for effects ≥5% and MDE = 1.2% at 80% power demonstrates that near-zero infrastructure×methodology interactions are genuine nulls.

7. **Model-as-facet analysis is a genuine contribution.** The demonstration that item_id drops from 60.4% to 36.8% while model×item absorbs 24.1%—collapsing G from 0.618 to 0.065—is clean and important. D-study showing 10 models yield G = 0.179 quantifies irreducibility.

8. **IRT vs G-theory comparison is a standalone contribution.** The 4.4× item requirement gap (510 vs 116) directly informs practitioners using tinyBenchmarks-style approaches.

### Weaknesses

1. **Four models is marginal for random-effects estimation of the model facet (Major).** Variance components from facets with <5–6 levels are known to be unstable and positively biased (Brennan, 2001, Ch. 4). The bootstrap CI [21.3, 27.0] on model×item reflects item-resampling uncertainty only—models are fixed across all bootstrap samples. A leave-one-model-out analysis is needed to quantify sensitivity to the model sample. The 14B extension (Exp 6) adds models in a separate analysis, not the main crossed design.

2. **The "precision" facet conflates genuine numerical effects with vLLM engine artifacts (Major).** FP32 shows consistent ~8-10pp accuracy degradation due to a vLLM-specific code path issue (V1 CUDA graph vs V0 eager), not fundamental precision properties. Two of three precision levels (BF16, FP16) are nearly identical (<0.2pp), while FP32 is dramatically different due to this artifact. The paper should present a BF16-vs-FP16-only decomposition as sensitivity analysis.

3. **Hardware crossing is severely underpowered (Moderate-Major).** Two GPU types (both NVIDIA data-center class) provide df=1 for the hardware facet. The 0.18% [0.03, 0.42] hardware×methodology estimate has almost no statistical power. Hardware×item = 1.2% is 6.7× larger than hardware×methodology. Cross-architecture effects (NVIDIA vs AMD, consumer vs data-center) could plausibly be larger. The separability claim should be scoped as preliminary or limited to "numerical precision separability."

4. **Option ordering facet is undefined for open-ended benchmarks (Moderate).** GSM8K and MATH are open-ended generation tasks without MC options. The paper reports 4 ordering levels for all benchmarks but does not explain what "ordering" means for these tasks. If few-shot exemplar ordering was used as proxy, it measures a different construct than MC option rotation. This is a non-trivial gap.

5. **Temperature and ordering have too few design points for credible random-facet treatment (Moderate).** Temperature has 3 levels (0.0, 0.3, 0.7)—selected boundary/midpoint values, not random draws from a universe. The 4 orderings exhaust ABCD rotations but exclude the 24 total permutations. The fixed-facet analysis should be presented as primary for these facets.

6. **D-study grid search procedure is underdocumented (Moderate).** The optimization appears to be independent per-facet sweeps rather than joint optimization. Jointly optimized allocations could be substantially different. The procedure, objective function, search bounds, and step sizes should be documented.

7. **Cross-benchmark design asymmetry (Minor-Moderate).** MMLU uses 3 precisions × 3 temperatures while other benchmarks use 2 × 2. Precision-related components on non-MMLU benchmarks are mechanically smaller because BF16 and FP16 produce nearly identical results (no FP32).

8. **Gemma FP16 exclusion creates imbalance (Minor).** Gemma has 2 precision levels vs 3 for others. The paper states REML is used for unbalanced cases but should clarify which estimator was actually used for the main cross-model analysis.

### Questions for Authors

1. What fraction of bootstrap resamples show model×item > item_id in the cross-model analysis?
2. What happens to the variance decomposition if FP32 is excluded, leaving only BF16 vs FP16?
3. How was option ordering operationalized for GSM8K and MATH?
4. Leave-one-model-out: does removing any single model change model×item by more than the bootstrap CI width?
5. What is the D-study projection for the common practice of 1 prompt, 1 seed, varying only items?
6. For Exp 7: is seed×LR driven by specific divergent combinations or smooth interaction?
7. Has a Bernoulli null simulation been run specifically for model×item (not just item_id)?
8. How sensitive is the cross-benchmark gradient to the specific 200-item samples on benchmarks other than MMLU?

### Minor Issues
1. Higher-order interaction computation (3.2%) is not reflected in the code that only fits 2-way interactions.
2. Bootstrap resamples items but not models—CIs on model×item only reflect item sampling uncertainty. Should be stated explicitly.
3. Verify "first multi-benchmark G-theory study" claim against Mesting (2026) who may have used multiple benchmarks.
4. The `text_exact_match` canonical answer definition depends on the design itself.
5. Logprob item_id = 53.2% vs binary 60.4%: the 7.2pp difference deserves discussion.
6. Total 4.29M records should be broken down by experiment in a summary table.
7. G coefficient formula should state whether relative G (Eρ²) or absolute G (Φ) is used.

### R1 Scores
- Soundness: 7/10
- Experimental Design: 8/10
- Reproducibility: 7/10
- **Overall (R1): 7/10**
- Confidence: 4/5

---

## R2 Review: Novelty and Related Work

### Summary
The genuine novel contribution is the cross-benchmark variance gradient: item dominance monotonically decreases from 60.4% (MMLU) to 22.1% (MATH) with corresponding increases in methodology×item interactions. The infrastructure×methodology crossing—framed as the primary advance over Mesting (2026)—yields a near-null (<0.5%), informative as confirmation but not carrying the weight the framing places on it. The D-study budget differentiation and model×item irreducibility are strong empirical findings, but the paper is primarily an empirical extension of Mesting's framework rather than a methodological advance.

### Strengths

1. **Cross-benchmark variance gradient is genuinely novel and explanatory.** No prior work has positioned multiple LLM benchmarks along a reasoning-intensity continuum and demonstrated a monotonic shift in variance structure. This resolves genuine confusion about why prior single-benchmark studies reached contradictory conclusions about which factors matter most.

2. **Model×item as cross-model generalizability barrier is a strong finding.** G collapse from 0.618 to 0.065 due to 24.1% model×item, persisting at 21–25% across all 5 benchmarks, is the first G-theory quantification of cross-model item-level disagreement. This directly challenges leaderboard interpretability.

3. **D-study budget differentiation is practically actionable.** The items-to-seeds effectiveness ratio shifting from 14.2:1 (MMLU) to 0.8:1 (GSM8K) crystallizes "no universal reproducibility recipe" with specific guidance.

4. **Metric-conditional separability adds genuine nuance.** Infrastructure×methodology <0.5% under binary but hw×temp = 0.83% under text-exact-match. This metric-dependent distinction is new.

5. **Experimental scale exceeds all prior work.** ~4.3M records, 6 models, 5 benchmarks, 2 GPU types, 9 experiments substantially exceed Mesting (2026), Brittlebench (2026), and Yuan (2025).

6. **IRT vs G-theory cost comparison fills a methodological gap.** The 4.4× item requirement difference quantifies the "hidden cost" of multi-facet reliability.

### Weaknesses

1. **Infrastructure crossing as primary framing vs near-null contribution (Major).** The title, abstract, and introduction frame "crossing infrastructure and methodology in a unified G-theory framework" as the key advance. But infrastructure×methodology < 0.5% across all benchmarks. The three strongest findings (gradient, model×item, D-study budgets) would emerge from a methodology-only design replicated across benchmarks with model as crossed facet. The framing creates a mismatch between what is promised and what is delivered. The paper should foreground the gradient and model-as-facet findings as primary.

2. **Incrementality over Mesting (2026) not fully resolved (Major).** The paper claims four differences from Mesting: (a) infrastructure crossing → near-null; (b) multi-benchmark → genuine advance; (c) model as crossed facet → genuine advance; (d) metric-conditional budgets → genuine advance. Points (b)–(d) are extensions of Mesting's framework, not a fundamentally different approach. The "first" language throughout overstates methodological novelty. The contribution is primarily empirical (new findings from a larger study), not methodological (new framework).

3. **Missing related work creates unfair positioning (Major).** Several important works are insufficiently engaged:
   - **Sclar et al. (2024, ICLR)**: Up to 76% accuracy swing from prompt formatting—relationship to this paper's prompt×item variance undiscussed.
   - **Kunievsky & Evans (2025)**: Alternative variance decomposition (intent/articulation/model uncertainty)—a directly competing framework, absent from the paper.
   - **Bui et al. (2025)**: Seed sensitivity in fine-tuning (RTES variance=18.22 for RoBERTa on COPA)—directly relevant to Exp 7 but uncited.
   - The IRT comparison would be strengthened by explicitly engaging with tinyBenchmarks' ~100-item recommendation and explaining the 4× gap mechanism.

4. **Cross-benchmark gradient ordering is post-hoc (Moderate).** The monotonic ordering was presumably observed after experiments. The explanatory mechanism (CoT stochasticity) is plausible but not independently validated. Without an external measure of reasoning intensity, Spearman ρ = 1.0 is circular: benchmarks are ordered by the quantity being correlated.

5. **Item dominance is partially expected from measurement theory (Moderate).** Any assessment with wide difficulty range shows item variance as dominant—well-established in psychometrics. The contribution is in quantifying the magnitude and deriving the gradient, not the finding per se. The paper should be more explicit about this.

6. **Fine-tuning experiment is architecturally disjoint (Moderate).** RoBERTa-large (355M, encoder-only, classification) vs decoder LLMs (7-9B, generation). The regime change claim (seed×lr supplants item_id) cannot be generalized to decoder fine-tuning (e.g., LoRA on Llama). The paper acknowledges this as a limitation but the cross-paradigm comparison risks overstatement.

7. **"Practitioner toolkit" contribution is vaguely defined (Moderate).** What is actually released is unclear—specific scripts/tables vs a general tool? Mesting (2026) already applied G-theory to LLM eval, and GeneralizIT provides G-theory software.

8. **Zero figures in a variance decomposition paper (Moderate).** 18 tables and no figures. The cross-benchmark gradient demands a stacked-bar chart. The D-study budget reversal demands projection curves. Visual communication at a competitive venue dramatically affects reviewer engagement and comprehension.

### Questions for Authors

1. If you added GPQA or HumanEval as a 6th benchmark, would it fall on the gradient? What independent measure of reasoning intensity validates the ordering?
2. If you removed all infrastructure facets and ran methodology-only G-theory across 5 benchmarks, which claimed contributions would change?
3. Can you provide a precise accounting of where the 4.4× IRT-G-theory gap comes from (fraction from prompt×item, seed×item, residual)?
4. With 4 deliberately selected models, how defensible is treating model as a random facet? How does G change if model is fixed?
5. Full 14K-item MMLU with 1 prompt and 1 seed: what is G? If it exceeds 0.80, the "current practice is inadequate" claim needs qualification.
6. What mechanism drives HellaSwag's position on the gradient, given it doesn't involve explicit multi-step reasoning?
7. If a practitioner uses LLM-as-judge, do your D-study budgets still apply, or would judge variance overwhelm them?

### Minor Issues
1. D-study table internal consistency needs verification (apparent anomalies in GSM8K projections flagged in prior reviews).
2. Cross-benchmark design asymmetry (3×3 vs 2×2) affects comparability of precision-related components.
3. Abstract claim about "current standard practice yields G < 0.25" uses all-facets-random G; many practitioners fix temperature/precision, making practical G higher.
4. Several references have incomplete information; "first" claims are vulnerable without exhaustive literature review.
5. Some reported numbers differ between sections (reconcile 2-model vs 4-model analyses).

### R2 Scores
- Novelty: 6/10
- Significance: 7/10
- Writing Quality: 5/10
- **Overall (R2): 6/10**
- Confidence: 4/5

---

## Roundtable Discussion

### Step 2: Cross-Sharing

R1 and R2 exchanged reviews. Key observations from the exchange:

- **R1 → R2**: R1's concern about the FP32 engine artifact strengthens R2's point about infrastructure crossing yielding near-null genuine results—much of the reported precision variance may be an artifact rather than a finding about numerical precision per se.
- **R2 → R1**: R2's point about post-hoc gradient ordering helps contextualize R1's otherwise positive assessment of the gradient—the statistical evidence is strong but the causal mechanism needs independent validation.
- Both reviewers independently flagged the 4-model limitation and hardware underpowering as concerns.

### Step 3: Convergence

**Points of Agreement:**

1. **The cross-benchmark variance gradient is the paper's strongest contribution.** Both reviewers rate this as genuinely novel and well-supported empirically. The reconciliation of contradictory prior findings is valuable.

2. **Model×item interaction is important and well-quantified.** The G collapse from 0.618 to 0.065 is a clean demonstration with direct practical implications for leaderboard interpretation.

3. **D-study budget differentiation is practically actionable.** The MMLU-vs-GSM8K budget reversal (item-limited vs seed-limited) is non-obvious and useful.

4. **Infrastructure crossing framing is misaligned with results.** The near-null infrastructure×methodology finding, while informative, does not justify its prominence in the title, abstract, and introduction.

5. **4 models is marginal for the model-as-facet claim.** Both reviewers request leave-one-model-out sensitivity analysis.

6. **Hardware separability with 2 GPU types is preliminary.** The claim should be scoped accordingly.

7. **The paper is at or near the AAAI acceptance threshold.** Core findings merit publication; framing and presentation need revision.

**Points of Divergence:**

- R1 is more positive about overall methodological soundness (7/10), viewing the weaknesses as addressable through additional analyses and clarifications.
- R2 is more concerned about framing and novelty positioning (6/10), viewing the infrastructure crossing emphasis and "first" claims as problematic.
- R1 weighs the MD1-MD9 defense package more heavily as a strength; R2 weighs the missing figures and related work gaps more heavily as weaknesses.

### Step 4: Consolidated Assessment

**Overall Score: 6.5/10 — Borderline Accept**

**Core Strengths (what merits publication):**
- Cross-benchmark variance gradient with ρ = 1.0 is a genuinely novel empirical finding
- Model×item interaction quantification (21–25% across 5 benchmarks) with G collapse demonstration
- D-study budget differentiation (MMLU item-limited, GSM8K seed-limited)
- IRT vs G-theory 4.4× cost comparison
- Exemplary robustness package (MD1-MD9)
- Impressive experimental scale (~4.3M records, 9 experiments)

**Core Weaknesses (what threatens acceptance):**
- **Framing mismatch**: Infrastructure crossing is foregrounded but yields a near-null; actual novelty (gradient, model×item) is underemphasized
- **Incrementality**: Primarily an empirical extension of Mesting (2026), not a methodological advance; "first" claims overstate
- **Missing references**: Kunievsky (2025), Sclar et al. (2024), Bui et al. (2025) directly relevant but uncited
- **Presentation**: Zero figures in a variance decomposition paper is a significant handicap at a competitive venue
- **Model facet**: 4 models marginal for random-effects; leave-one-model-out analysis needed
- **FP32 confound**: Precision facet partially measures a vLLM artifact; needs BF16-vs-FP16-only sensitivity
- **Post-hoc gradient**: No independent validation of the reasoning-intensity continuum
- **Hardware**: 2 GPU types insufficient for "confirmatory separability" language

**Recommendation for Revision:**
1. Reframe: Center the gradient and model×item findings as primary contributions; relabel infrastructure crossing as confirmatory
2. Add 3–4 figures: cross-benchmark stacked bars, D-study projection curves, model-as-facet before/after, IRT vs G-theory comparison
3. Complete related work: Add Kunievsky (2025), Sclar et al. (2024), Bui et al. (2025); engage tinyBenchmarks deeply
4. Sensitivity analyses: Leave-one-model-out, FP32-excluded decomposition
5. Clarify: Option ordering for open-ended benchmarks, D-study optimization procedure, G coefficient type (relative vs absolute)
6. Temper claims: Remove "first" where not defensible; scope hardware separability as preliminary

**Experiment Coverage Assessment:**
All 9 planned experiments (exp-001 through exp-008 + MATH extension) are present in the paper, mapped to Experiments 1–9. Coverage: **9/9 (100%)**. The paper faithfully reports all planned analyses, including the fine-tuning regime comparison and LayerCast mitigation study.

---

## Score Summary

| Criterion | R1 | R2 | Consensus |
|---|---|---|---|
| Soundness / Methodology | 7 | — | 7 |
| Experimental Design | 8 | — | 8 |
| Novelty | — | 6 | 6 |
| Significance | — | 7 | 7 |
| Writing / Presentation | — | 5 | 5 |
| Reproducibility | 7 | — | 7 |
| **Overall** | **7** | **6** | **6.5** |
| Confidence | 4/5 | 4/5 | 4/5 |

**Verdict: Borderline Accept (6.5/10)**. The empirical contributions are strong and the experimental scale is impressive, but the framing-results mismatch, missing figures, incomplete related work, and marginal model sample size collectively place the paper just at the acceptance boundary. A revision addressing the six points above would likely push this to a solid 7/10.
