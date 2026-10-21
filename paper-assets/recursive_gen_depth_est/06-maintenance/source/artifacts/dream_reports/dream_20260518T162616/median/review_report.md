---
dream_id: dream_20260518T162616
tier: median
overall_score: 3/6 Borderline Reject
timestamp: 2026-05-18T17:09:58.266056+00:00
---

# Dream Review Report: Ordinal Depth Estimation for Recursive Model-Generated Text

**Paper Title:** Ordinal Depth Estimation for Recursive Model-Generated Text: A Depth Degradation Atlas

**Headline Assessment:** Borderline Reject (3/6)

**Reviewers:** R1 (Methods + Experiments), R2 (Novelty + Related Work)
**Rounds:** 3 (Round 1 independent → Round 2 cross-share → Round 3 convergence)
**Convergence:** Achieved. R1 score 3/6, R2 score 2.5/6; consolidated to 3/6.

---

## 1. Paper Summary

The paper formalizes ordinal generation depth estimation as a new task: given a text passage and a reference language model, predict the recursive generation depth d ∈ {0,1,2,3} where d=0 denotes human-written text. The authors construct a controlled benchmark spanning 3 model families (Pythia-1.4B, OLMo-1B, GPT-2 XL), 3 decoding strategies (nucleus, temperature, top-k), and 4 depths via recursive LoRA fine-tuning on WikiText-103. They extract 19 statistical features (perplexity, surprisal, diversity) and evaluate 4 classifiers, finding that Random Forest achieves 70-85% four-class accuracy. The paper contributes a "Depth Degradation Atlas" characterizing how features evolve across depths, an EDD (Effective Discriminable Depth) metric, and a two-stage cross-strategy pipeline (+11.5pp over naive transfer). Extended validation covers 14B scale (68% accuracy, nucleus only), API/instruct models (42-45%), and wild data calibration (19-32% FPR on web-crawl).

---

## 2. Consolidated Strengths

**S1. Genuine task novelty.** Ordinal generation depth estimation is a meaningful recast of the model collapse problem. No prior work estimates recursive depth from text alone. The shift from "does recursion degrade?" to "how much?" is a defensible epistemic repositioning with clear practical motivation for data curation.

**S2. Systematic and well-instrumented benchmark.** The 36-condition grid (3×3×4) with 5,000 passages per cell provides strong statistical power. Bootstrap CIs in Table 1 are appropriately reported. The design is principled and, with protocol details added, independently replicable using publicly available model checkpoints.

**S3. Unusually honest limitation reporting.** The paper reports DCOL failure (Section 9), API model attenuation (42-45%, Section 7.2), wild data FPR (19-32%, Section 7.3), and cross-strategy brittleness (Section 6) without burying them. This epistemic honesty is commendable and rare.

**S4. Meaningful baseline comparison.** Adapting Binoculars and Fast-DetectGPT to the ordinal task (Table 3) is the right design choice. The pairwise AUC gaps (d1vd2, d2vd3) are the most convincing evidence that binary detectors cannot address ordinal depth.

**S5. Feature universality finding is actionable.** p90_ppl and var_surprisal as universal top-4 features across all 9 cells (Section 4.3) connects to the tail erosion mechanism from model collapse theory, providing interpretive grounding beyond raw accuracy numbers.

**S6. 3-class metric (Section 4.4) pre-empts the obvious critique.** Reporting 59-82% accuracy excluding the easy d0 class demonstrates ordinal signal beyond the human/machine boundary.

---

## 3. Consolidated Major Issues

### Major Issue 1 [idea]: Missing adjacent baselines weaken novelty verification
**Source:** R2 Round 1, R1 partially concurred in Round 2

Membership inference methods (Min-K% Prob, Shi et al. 2024; DetectGPT, Mitchell et al. 2023) produce continuous scores from token probabilities and are structurally adjacent to ordinal depth estimation. These methods could potentially be calibrated to ordinal depth bins, similar to how the paper calibrates Binoculars and Fast-DetectGPT in Table 3. Corpus fingerprinting and text watermarking (Kirchenbauer et al. 2023; Christ et al. 2024) provide alternative provenance tracking approaches. The Related Work does not engage these literatures at all.

**Why Major:** A reviewer cannot confidently assess the novelty claim without knowing whether membership inference methods, when adapted to the ordinal depth task, already capture comparable signal. This is not a peripheral citation gap but an experimental baseline gap. If Min-K% Prob achieves competitive ordinal accuracy without depth-labeled training data, the contribution narrows significantly.

**R1 Cross-share nuance:** R1 noted these methods are designed for binary detection and would require non-trivial adaptation for ordinal use. Including them as binary recasts (d0 vs d1-d3) in Table 3 would be sufficient to address the concern.

**Fixability:** Medium. Requires running 1-2 additional baseline experiments and adding Related Work discussion.

---

### Major Issue 2 [idea]: Practical scope substantially narrower than framed
**Source:** R2 Round 1, supported by R1's W4 (wild FPR) and W5 (14B single-strategy)

The paper's framing (Abstract, Introduction, Conclusion) implies practical relevance for real-world data curation and AI content auditing. The experimental evidence shows the system works well only when: (a) the source model is a base model (not instruct/API), (b) the decoding strategy is known or identifiable, (c) the deployment domain is clean (not web-crawl). Specifically:
- Base models: 70-85% accuracy
- Instruct/API models: 42-45% accuracy with qualitatively different feature regime (p90_ppl → surprisal_range)
- Wild data FPR: 19-32% on web-crawl, prohibitive for deployment without domain adaptation
- Cross-strategy: requires strategy identification at only 57.8% accuracy

This is a narrow operational regime. Most real-world AI-generated text in 2026 comes from instruction-tuned or API models.

**Why Major:** The Abstract claims "70-85% four-class accuracy" without qualifying that this is within-strategy on base models only. The Introduction motivates the work with "practical data curation" but the experiments show a controlled lab setting. This is a story consistency failure between claims and evidence, not merely a limitation.

**R1 Cross-share nuance:** R1 noted this is partially a method limitation (need different features for different model types) and partially a task limitation (depth signal is inherently regime-conditional). R1 recommended reframing as "regime-dependent feature adaptation" rather than framework failure.

**Fixability:** Medium. Reframe claims to match base-model-only scope, or extend experiments.

---

### Major Issue 3 [idea]: Atlas contribution is primarily observational without demonstrated predictive power
**Source:** R2 Round 1, supported by R1's W1 (shallow depth range)

The four Atlas findings are:
- (a) Perplexity tail statistics as universal markers — expected from model collapse theory (Shumailov 2024)
- (b) Non-uniform inter-depth distances — unsurprising given progressive degradation
- (c) EDD boundary — a useful metric but the empirical coverage (d0-d3) is shallow relative to the theoretical bound (EDD ≤ 6)
- (d) Strategy-dependent feature trajectory reversal — the most genuinely non-obvious finding

The "Atlas" framing implies comprehensive empirical mapping, but the depth coverage stops at d3 when theory predicts discriminability up to d5-d6. The 14B experiment provides partial structural validation (p90_ppl remains top-feature, EDD decay pattern consistent) but reveals feature ranking instability (only 2/4 top features overlap with 1B). No experiment explicitly tests the Atlas's predictive power on unseen settings.

**Why Major:** If the Atlas reduces to "we computed 19 features and found some track depth better than others," the paper's novelty rests primarily on task formalization + benchmark. A 3-model benchmark with Random Forest on handcrafted features, without mechanistic grounding or demonstrated generalization, is below the methodological bar for a top ML venue.

**R1 Cross-share nuance:** R1 argued that the Atlas DOES have partial predictive value (EDD decay pattern correctly predicted 14B behavior; p90_ppl universality partially confirmed). The feature trajectory reversal is genuinely non-obvious. R2 concurred that the "Atlas" branding is the problem, not the underlying findings.

**Fixability:** Medium-High. Reframe as "exploratory empirical characterization" rather than comprehensive Atlas. Alternatively, add d4+ experiments or mechanistic grounding.

---

### Major Issue 4 [idea]: Cross-strategy pipeline contribution oversold relative to strategy classifier performance
**Source:** R1 Round 1 (W3), R2 concurred in Round 2

The two-stage pipeline (strategy ID → conditioned depth classifier) achieves 70.5% cross-strategy accuracy, a +11.5pp improvement over naive transfer (59.1%). However:
- Strategy classifier accuracy: 57.8% (chance = 33.3%)
- Oracle pipeline accuracy: 78.3%
- Gap lost to misrouting: 7.8pp
- No error propagation breakdown: accuracy conditioned on strategy classifier correctness vs incorrectness not reported

**Why Major:** The paper presents the pipeline as Contribution 3, but the 57.8% strategy classifier is a hard limit on deployment utility. Without a conditional accuracy breakdown, the 70.5% number conflates pipeline success with partial luck.

**Cross-share convergence:** Both reviewers agreed the real contribution is the DISCOVERY that cross-strategy transfer is structurally hard (feature trajectory reversal under temperature scaling), not the pipeline solution. The pipeline should be repositioned from a standalone contribution to a proof-of-concept illustrating the discovery.

**Fixability:** High. Add conditional breakdown, reposition as proof-of-concept, emphasize the discovery of cross-strategy difficulty as the contribution.

---

## 4. Consolidated Minor Issues

**m1 [presentation]: LoRA fine-tuning protocol underspecified.** Missing training steps/epochs, learning rate, scheduler, adapter initialization strategy. Critical for benchmark reproducibility. Originally R1 Major (W2), downgraded to Minor after R2 cross-share confirmed this is fixable with an appendix paragraph and does not affect the idea. *(Fixable with 2-3 sentences in methods/appendix.)*

**m2 [idea]: 14B scale validation is single-strategy (nucleus) only.** Strategy effects dominate model effects in the 1B results (16pp strategy gap vs 7pp model gap). A single-strategy 14B result cannot support scale generalization claims. The Δ vs 1B best (-15.9pp) conflates scale and strategy confounds.

**m3 [idea]: Reference model (GPT-2 Large 774M) fixed and not ablated.** Feature universality may be an artifact of the specific reference model's token distribution rather than a property of the depth signal. A second reference model ablation would strengthen the universality claim. *(Section 10 mentions cross-model FPR variance of 8.5pp, acknowledging sensitivity but not resolving it.)*

**m4 [idea]: Wild data FPR reported without calibration mitigation.** 32% FPR on C4 is reported as a limitation but no threshold recalibration (Platt scaling, isotonic regression) is attempted. This makes the result look worse than it may need to be.

**m5 [presentation]: Decoding strategy effects subsection cites only 2 papers** (Holtzman 2020, Garces Arias 2025), yet feature trajectory reversal is one of the four core Atlas findings. Sparse coverage precisely where the paper's most interesting finding lives.

**m6 [presentation]: Binary baseline comparison evaluation regimes differ.** Within-strategy RF (70-85%) uses oracle strategy labels. Cross-strategy pipeline (70.5%) uses predicted labels. Binary detectors (48-54%) use no strategy conditioning. The comparison in Section 5 should clarify these differences.

---

## 5. Questions for Authors

**Q1.** How do membership inference methods (e.g., Min-K% Prob calibrated to ordinal bins) perform on your benchmark? If they achieve competitive accuracy without depth-labeled training, what does this imply about the task's novelty relative to pretraining data detection?

**Q2.** Please provide the full LoRA training protocol: epochs per depth, learning rate, scheduler, whether adapters at depth d are initialized from depth d-1 weights or from scratch.

**Q3.** For the two-stage cross-strategy pipeline, what is the 4-class depth accuracy conditioned on strategy classifier correctness vs incorrectness? What fraction of the 70.5% overall accuracy comes from correctly-routed samples?

**Q4.** Was d4 generation attempted? If the recursive chain extends to d4-d6, what happens to d3vd4 AUC? Even one data point would calibrate how close d3 is to the discriminability ceiling.

**Q5.** For wild data FPR, did you attempt any post-hoc threshold calibration (Platt scaling, domain-adapted threshold)? Reporting a precision-recall tradeoff at the d0/d1 boundary would clarify whether 32% FPR is fundamental or a calibration artifact.

---

## 6. Experiment Coverage Assessment

Compared to the full experiment design (review_context.yaml):

| Experiment | Status | Coverage Quality |
|---|---|---|
| 14B scale validation (plan_014) | Covered (Section 7.1) | Partial — nucleus only, no multi-strategy |
| Wild data calibration (plan_015) | Covered (Section 7.3) | Good — 3 web-crawl + 1 control |
| Detector ordinal baseline (plan_018) | Covered (Section 5) | Good — Binoculars + Fast-DetectGPT |
| Bootstrap CIs (plan_020) | Covered (Table 1) | Complete |
| Theoretical analysis (plan_023) | Covered (Section 8) | Appropriately scoped as "motivation" |
| API model chains (plan_026) | Covered (Section 7.2) | Good — prompted + fine-tuned |
| DCOL ablation (plan_010) | Covered as negative result (Section 9) | Appropriate |

All planned experiments are present. The paper is complete in scope relative to the experiment plan.

---

## 7. Scoring

### Individual Reviewer Scores
| Reviewer | Round 1 | Post-Cross-Share | Confidence |
|---|---|---|---|
| R1 (Methods + Experiments) | 3/6 | 3/6 | 4/5 |
| R2 (Novelty + Related Work) | 2.5/6 | 2.75/6 | 4/5 |

### Consolidated Score: **3 / 6 (Borderline Reject)**

### Calibration Justification
4 Major issues identified (missing baselines, narrow practical scope, Atlas primarily observational, pipeline oversold). Per calibration rules, 3+ Major issues → not higher than Borderline Reject. However:
- Major Issue 4 (pipeline) has high fixability and both reviewers agree to reposition
- Major Issue 3 (Atlas) could be substantially addressed through reframing
- The task formalization IS genuinely novel (no prior work)
- The paper demonstrates unusual intellectual honesty

The paper occupies a difficult position: genuine task novelty with modest methodological contribution. For a top ML venue (25% acceptance rate), the combination of Random Forest on handcrafted features, narrow operational scope, and missing adjacent baselines keeps it below the acceptance threshold. The paper reads as a solid empirical study that would benefit from either: (a) a stronger methodological contribution (learned depth-discriminative representations that work), or (b) substantially broader empirical scope (multiple scales, instruct models, deeper recursion chains) to justify the "Atlas" framing.

**If claims are tightened to match actual scope** (base models at 1B scale, within-strategy or known-strategy, controlled settings), **missing baselines are added**, and **the pipeline is repositioned**, the score could move to 3.5-4.0 (Weak Accept territory).

---

## 8. Actionable Revision Priorities

1. **[High priority]** Add membership inference baselines (Min-K% Prob, DetectGPT) calibrated for ordinal depth to Table 3. Engage watermarking/fingerprinting literature in Related Work.
2. **[High priority]** Reframe Abstract/Introduction claims to match base-model, within-strategy scope. Change "70-85%" headline to either qualify it or use the cross-strategy number.
3. **[Medium priority]** Add LoRA training protocol details (epochs, LR, adapter initialization).
4. **[Medium priority]** Reposition cross-strategy pipeline from Contribution 3 to a practical proof-of-concept. Elevate the discovery of cross-strategy difficulty as the contribution.
5. **[Medium priority]** Add conditional accuracy breakdown for the two-stage pipeline.
6. **[Lower priority]** Attempt d4+ generation to test depth ceiling. Add threshold calibration for wild data FPR. Ablate reference model choice.