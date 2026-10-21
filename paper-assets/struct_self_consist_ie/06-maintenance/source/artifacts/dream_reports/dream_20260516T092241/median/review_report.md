---
dream_id: dream_20260516T092241
tier: median
overall_score: borderline findings (3.0/5)
timestamp: 2026-05-16T11:59:36.036667+00:00
---

# R2 Review: Novelty & Related Work

## Summary

This paper presents a dual contribution for structured information extraction: (1) a quality estimation framework showing five confidence signals predict output quality, and (2) a diagnostic analysis explaining why these signals fail at best-of-N selection despite strong population-level correlation. The multi-causal failure mechanism (instance degeneracy + logprob compression + insufficient discriminability) is the paper's core novelty claim. While the QE-selection decoupling insight is genuinely useful, the novelty is incremental over concurrent work (Nédellec & Xia 2026, CoCoA 2025), and the trained verifier experiment—which closes 36% of the oracle gap—is underdeveloped relative to its importance in the narrative.

## Strengths

- **The QE-selection decoupling is a genuinely novel conceptual contribution.** The distinction between population-level correlation (useful for selective prediction) and within-instance ranking (needed for selection) is clearly articulated and non-obvious. Prior work in self-consistency and MBR decoding conflates these, and this paper provides the first clean empirical separation for structured IE.

- **The multi-causal diagnosis is well-structured.** Decomposing the failure into (a) design property of instance-level aggregates, (b) instance degeneracy, and (c) LP compression provides actionable understanding. The LoRA rank=8 ablation showing that reducing degeneracy is necessary but not sufficient is particularly compelling—it rules out the simplest explanation.

- **Capability-degeneracy tradeoff is an interesting observation.** The monotone relationship between model capability and degeneracy (CoNLL 91% F1 → 58% degen, SciERC 66% → 21%, WNUT 48% → ~0%) provides a structural explanation for why test-time scaling via unsupervised selection faces diminishing returns as models improve. This has implications beyond IE.

- **Breadth of evaluation.** 3 models × 3 datasets × 2 tasks with consistent findings strengthens the generality claims. The free-form decoding ablation (std ratio 0.97) providing causal evidence that LP compression is intrinsic rather than an artifact of constrained decoding is a well-designed control.

- **Practical value of QE framework.** AUROC 0.82 for quality estimation is genuinely useful for deployment decisions (selective prediction, error flagging) regardless of selection effectiveness.

## Weaknesses

- **Incremental novelty over Nédellec & Xia (2026).** The paper positions itself as substantially advancing beyond Nédellec & Xia by using structural Jaccard rather than surface-level string matching. However, the core finding—consistency correlates with accuracy for LLM-based IE—is the same. The paper's genuine advance is the negative result (selection fails) and the diagnostic, not the QE framework itself. The "dual contribution" framing risks overclaiming: Contribution A (QE works) is largely a replication with better metrics of what Nédellec & Xia already showed.

- **The trained verifier experiment is too thin for its narrative weight.** The paper argues that the "path forward" is trained verifiers, and the logistic regression closing 36% of the NER oracle gap is presented as evidence that signals carry exploitable information. But a 5-feature logistic regression is a minimal baseline—no comparison to even a simple MLP, no cross-dataset transfer evaluation, no analysis of what the verifier learns. For a paper that makes "what would fix it" a core part of Contribution B, this experiment needs substantially more development. It currently reads as a pilot study wrapped in strong claims.

- **The "Capability Trap" claim is based on n=3 data points.** The monotone relationship between capability and degeneracy is observed across exactly 3 datasets with different characteristics (domain, entity types, difficulty). The paper acknowledges this is "illustrative only, not statistically reliable," but it still occupies significant narrative space. This is correlation on 3 points with multiple confounds (domain complexity, annotation granularity, entity type diversity).

- **Missing comparison to constrained decoding / structured generation approaches.** The paper studies confidence signals for selecting among unconstrained samples, but does not engage with the literature on constrained decoding (Willard & Louf 2023, GenIE's bi-level constrained decoding) as an alternative approach to improving structured output quality. If constrained decoding can guarantee structural validity, does the entire selection paradigm become less relevant? The paper's own finding of 99.95% parse rate partially addresses this but doesn't fully engage with the implication.

- **The negative result's novelty is partially diminished by predictability.** For fine-tuned models with high greedy performance (CoNLL 91% F1), it is somewhat expected that sampling at T=1.0 would not easily improve over greedy—the model is already near-converged. The paper argues non-obviousness by citing self-consistency's success for reasoning, but reasoning tasks typically have much lower greedy accuracy (GSM8K ~50-70%) where there is more headroom. The paper would benefit from explicitly addressing this asymmetry in task difficulty.

- **Title may overstate the finding.** "Why Confidence Signals Cannot Scale Structured Information Extraction" implies a universal impossibility, but the paper shows that *unsupervised* confidence signals fail. The trained verifier partially succeeds (+4.8pp), and the paper's own discussion suggests supervised approaches could work. "Cannot" is too strong—"struggle to" or "fail to unsupervisedly" would be more accurate.

## Missing Related Work

**Critical omissions:**

1. **Reward models / ORMs / PRMs for non-math domains.** The paper cites Cobbe et al. (2021) and Lightman et al. (2023) for math verifiers but does not engage with the broader literature on applying verification to non-mathematical structured tasks. Recent work on reward models for code generation (e.g., CodeRM), factual verification, and structured QA is directly relevant to the "trained verifier as path forward" argument. Without this, the Discussion's "path forward" lacks grounding in what has already been attempted.

2. **Test-time compute scaling beyond the cited papers.** The paper misses Sardana et al. (2025) "Beyond Decoding" survey, DeepSeek-R1's approach to test-time scaling via extended reasoning, and the broader "scaling laws for test-time compute" literature (e.g., the compute-optimal allocation work by Wu et al. 2024, which IS in the lit map but not cited in the paper). The paper's contribution is fundamentally about *when test-time scaling fails*—it should engage more deeply with the conditions under which it succeeds.

3. **Entity linking and disambiguation confidence.** The IE confidence literature (Culotta & McCallum 2004 is cited) has evolved significantly. Work on entity linking confidence (Rao et al. 2013), knowledge graph completion confidence (Safavi et al. 2020), and recent neural IE confidence calibration is relevant but missing.

4. **CRF-based structured prediction uncertainty.** The paper jumps from classical IE confidence (Culotta & McCallum 2004) to LLM-based approaches without engaging with the CRF/BiLSTM-CRF era's uncertainty quantification (Xiao & Wang 2019 is in the lit map but appears not cited). The evolution from token-level CRF uncertainty to sample-level LLM consistency deserves explicit discussion.

5. **Universal Self-Consistency (Chen et al. 2024).** This paper extends self-consistency to free-form generation using the LLM itself as a judge—directly relevant as an alternative aggregation mechanism that could potentially address the instance degeneracy problem (by having the model evaluate rather than just vote). Listed in the lit map but the paper's engagement appears superficial.

6. **Multi-output evaluation metrics for IE.** The paper uses entity-level and instance-level F1 but does not discuss the evaluation methodology literature (e.g., Segura-Bedmar et al. 2013 on relaxed matching, Fu et al. 2020 on entity-level evaluation issues). Given that the structural Jaccard metric is a core methodological contribution, positioning it relative to existing set-comparison metrics for IE would strengthen the paper.

**Recommended additions (lower priority):**

7. Calibration of structured predictors beyond Kuleshov & Liang 2015 (e.g., Jagannatha & Yu 2020 on calibrating structured output predictors for NLP—in the lit map, may not be cited).
8. MBR decoding for structured prediction tasks beyond MT (e.g., parsing, semantic role labeling).
9. The abstention/selective prediction survey (Wen et al. 2025, TACL) for positioning the QE contribution.

## Questions for Authors

1. **On the trained verifier**: The logistic regression closes 36% of the oracle gap. What is the performance ceiling of a verifier that has access to the actual output text (not just the 5 scalar signals)? Have you considered a lightweight neural verifier that could assess structural plausibility?

2. **On the capability trap**: With only 3 data points, how do you distinguish the capability-degeneracy relationship from a simpler confound—dataset annotation granularity? CoNLL has 4 coarse entity types, SciERC has 6 scientific types, WNUT has 6 noisy types. Could type granularity rather than model capability drive degeneracy differences?

3. **On the QE-selection decoupling**: You show QE correlation is stable across configurations while selection effectiveness varies. But have you tested whether QE-based selective prediction (abstaining on low-confidence instances) actually improves precision-coverage tradeoffs in a deployment-realistic scenario? This would make Contribution A substantially more concrete.

4. **On Universal Self-Consistency**: Chen et al. (2024) use the LLM itself to select the most consistent answer. Have you evaluated this approach for structured IE? It seems like a natural baseline that could address the instance degeneracy problem by leveraging semantic rather than surface-level comparison.

5. **On the free-form ablation**: The 99.95% parse rate suggests fine-tuned models don't need constrained decoding. Does this mean the entire constrained decoding literature for IE is rendered obsolete for fine-tuned LLMs, or is this specific to your training setup?

## Scores

**Soundness**: 3.5/5
The experimental methodology is generally sound with appropriate controls (free-form ablation, bootstrap significance testing, multi-seed). However, the capability trap claim on n=3 points, the underdeveloped verifier experiment, and the partially predictable negative result for high-accuracy settings weaken confidence. The QE evaluation is solid.

**Excitement**: 3.0/5
The QE-selection decoupling insight is genuinely interesting and the multi-causal diagnosis is well-executed. However, the core finding (unsupervised selection fails for structured IE) is somewhat expected for fine-tuned models near convergence, and the "path forward" (trained verifiers) is insufficiently developed to generate real excitement about follow-up directions. The paper identifies a problem more compellingly than it advances solutions.

**Overall Assessment**: 3.0/5
This is a solid empirical study with a genuinely novel conceptual contribution (QE-selection decoupling) and thorough diagnosis. It is suitable for Findings-level publication. For Main Conference, it would need: (a) a more developed trained verifier showing the gap is closable with moderate supervision, (b) stronger engagement with alternative approaches (USC, constrained decoding), and (c) tighter positioning relative to Nédellec & Xia (2026). The dual-contribution framing currently bundles one strong contribution (diagnostic) with one incremental contribution (QE framework).

**Confidence**: 4/5
I am familiar with the self-consistency, uncertainty quantification, and structured IE literatures. The test-time scaling and reward model literatures are adjacent to my core expertise but I have reviewed multiple papers in these areas.

**Reproducibility**: 4/5
The paper specifies models, datasets, hyperparameters, and evaluation metrics clearly. The 5 signals are well-defined. Reproduction would require LoRA fine-tuning of 3 models but this is standard. The structural Jaccard metric's implementation details (type-grouped Hungarian matching) should be provided in an appendix for full reproducibility.
