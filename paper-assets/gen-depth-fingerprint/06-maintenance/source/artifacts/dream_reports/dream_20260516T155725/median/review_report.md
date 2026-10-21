---
dream_id: dream_20260516T155725
tier: median
overall_score: weak reject
timestamp: 2026-05-16T16:28:10.283755+00:00
---

# Review Report: Distributional Depth Profiling

**Paper:** Distributional Depth Profiling: An Empirical Study of Differential Feature Response in Recursive LLM Generation
**Venue standard:** Top ML venue, ~25% acceptance rate, 6-point scale

---

## 1. Summary

This paper introduces *generation depth estimation* — an ordinal classification task that determines how many successive rounds of LLM generation produced a given text (depth 0 = human, 1 = first-generation, 2+ = recursive). The authors identify a "differential depth response" pattern: central-tendency and lexical diversity features (entropy_mean, TTR, hapax_ratio) drift monotonically with generation depth, while distributional shape features (entropy_std, tail_decay) remain near-stationary, consistent with a location shift in the NLL distribution. A 7-feature XGBoost ensemble achieves 3-class LOGO macro-F1 of 0.78 across 5 generators from 3 model families (all ≤2.8B). The paper further reports two informative negative findings: finer 5-class classification degrades sharply (F1=0.49), and depth-aware data curation does not outperform random subsampling.

---

## 2. Strengths

- **Novel and well-motivated task formulation.** Ordinal depth estimation is genuinely new. The argument that binary real-vs-synthetic detection discards useful gen-1 content alongside problematic deep-generation text is compelling and practically relevant for data governance.

- **Rigorous evaluation protocol.** LOGO evaluation genuinely tests cross-generator generalization rather than inflating numbers with in-distribution CV. The additional leave-one-*family*-out analysis (Table 4) provides a stricter test of cross-architecture transfer. Reporting per-generator held-out F1 with variance (Table 3) is transparent.

- **Comprehensive experimental coverage.** The paper packs five substantive experiments into 7 pages: feature ablation (Table 1–2), cross-generator LOGO (Table 3–4), paraphrastic vs. continuation chains (Table 5), 5-class ordinal (Table 6), and end-to-end neural comparison (Table 7). Each addresses a distinct question about the depth signal.

- **Honest reporting of limitations and negative results.** The downstream curation negative result is reported transparently rather than omitted. The paper explicitly acknowledges the architecture-dependent transfer gap (OLMo at 0.73 vs. Pythia-1B at 0.84), the ~3-class resolution ceiling, and positions the tool as "diagnostic rather than curative." This calibrated framing is refreshing and mature.

- **Interpretable mechanistic hypothesis.** The differential response pattern (location shift preserving functional form) is a testable, specific claim that goes beyond pure empiricism. The connection to attractor convergence theory for the 3-class ceiling is well-argued.

- **End-to-end comparison adds depth.** The QLoRA experiment (Table 7) serves dual purpose: demonstrating richer depth signal exists beyond 7 features (CV F1=0.89) while exposing the generalization-robustness trade-off (17pp LOGO gap vs. XGBoost's 3pp gap). This strengthens the argument for interpretable features.

---

## 3. Weaknesses

- **Severely limited generator scale.** All 5 generators are ≤2.8B parameters from only 3 families. The paper does not evaluate any model at 7B, 13B, or 70B+ scale. Larger, more capable generators produce more fluent text with potentially compressed depth margins — the already-visible degradation from Pythia-1B (0.84) to OLMo-2-1B (0.73) suggests performance could deteriorate significantly at larger scales. Without any evidence beyond 2.8B, generalizability claims are weak.

- **Single reference model without sensitivity analysis.** All features are computed under a single held-out reference model (Pythia-410M). The paper provides no analysis of how results change with different reference models (e.g., a non-Pythia reference, or a larger reference model). This is a critical confound: features computed under a same-family reference (Pythia-410M evaluating Pythia-generated text) may behave differently than cross-family references.

- **Feature set appears ad hoc despite principled framing.** The 7 features (5 NLL summary statistics + TTR + hapax_ratio) are standard perplexity-based detection features repurposed for depth estimation. The retroactive "differential response" framing is neat but the feature selection itself is not derived from first principles. entropy_min is acknowledged as "borderline; architecture-dependent" yet retained. No systematic feature search or information-theoretic justification is provided.

- **Modest absolute performance and unclear per-document utility.** 3-class LOGO F1=0.78 means substantial misclassification. Binary F1=0.71 implies ~29% error. The paper positions depth profiling as a corpus-level diagnostic tool, but provides no experimental validation of corpus-level composition estimation accuracy (e.g., estimating the gen-2+ fraction in a mixed corpus at various sizes).

- **Downstream experiment insufficiently described.** The negative downstream result — depth-aware curation doesn't beat random subsampling — is a significant finding but receives only brief treatment. No dedicated section, no table showing the comparison, and no details on the experimental setup (corpus size, model trained, evaluation metrics, number of seeds, confidence intervals). This undermines one of the paper's claimed contributions.

- **Single domain.** All generation chains use English Wikipedia seeds. No evaluation on other domains (creative writing, code, scientific text, social media, multilingual). TTR and hapax_ratio are highly domain-sensitive; the differential response pattern may not hold across domains.

- **Paraphrastic comparison lacks depth.** Table 5 shows the comparison but the analysis is brief (~1 paragraph). Cross-transfer results (0.65–0.68 F1) are interesting but not discussed in terms of practical implications. The connection to attractor convergence theory predictions deserves more than a passing mention.

- **Sparse related work.** Only 10 references. Missing citations to important works: FineWeb/CCNet perplexity filtering at scale, Alemohammad et al. (2024) on self-consuming generative models (cited but could be discussed more), recent multi-class source attribution work (SemEval-2024 Task 8), and deeper engagement with the model collapse theoretical literature.

---

## 4. Questions for Authors

1. **Reference model sensitivity:** What happens if you replace Pythia-410M with a non-Pythia reference model (e.g., OLMo or Qwen of similar size)? Does the differential response pattern hold, or is it an artifact of same-family reference scoring? This is critical for the claimed generality of the phenomenon.

2. **Scaling behavior:** The OLMo-2-1B result (0.73) already shows architecture-dependent degradation. Do you have any evidence (even preliminary) for generators at 7B+? The monotonic decline from same-family (0.84) to cross-family (0.73) suggests a troubling trend.

3. **Corpus-level validation:** You position depth profiling as a corpus-level diagnostic. Can you provide empirical validation — e.g., estimating the gen-2+ proportion in synthetic mixed corpora of varying sizes and reporting calibration error?

4. **Downstream experiment details:** How many seeds, what corpus size, what model was trained, what evaluation metrics? The negative result is important but currently unverifiable.

5. **Why not hybrid approach?** XGBoost for interpretable analysis + QLoRA for actual deployment. The 17pp LOGO gap for QLoRA is concerning, but could domain-adaptive fine-tuning or multi-reference ensembles close it?

---

## 5. Experiment Coverage Assessment

Comparing against the 5 planned experiments:

| Experiment | Status | Notes |
|---|---|---|
| Feature ablation & trend (plan_001) | ✅ Fully covered | Tables 1–2, perplexity analysis, clear differential response characterization |
| Cross-generator LOGO (plan_002) | ✅ Fully covered | Tables 3–4, per-generator and per-family results with variance |
| Paraphrastic comparison (plan_006) | ⚠️ Adequately covered but thin | Table 5, ~1 paragraph analysis; cross-transfer results mentioned but not tabled |
| Finer-grained ordinal (plan_009) | ✅ Fully covered | Table 6, per-depth F1, ordinal method comparison, confusion rate analysis |
| End-to-end classifier (plan_012) | ✅ Fully covered | Table 7, CV-vs-LOGO gap analysis, 5-class comparison, inference cost |

**Downstream result:** Claimed as a contribution in abstract and conclusion but lacks a dedicated experimental section. No table, no detailed methodology, no statistical tests reported in the main text. This is the weakest coverage gap.

---

## 6. Overall Assessment

| Dimension | Score | Justification |
|---|---|---|
| **Soundness** | 3/5 | Core claims about differential depth response are empirically supported for the tested regime (≤2.8B base models, Wikipedia domain). But single reference model, no scale sensitivity analysis, and underdescribed downstream experiment weaken confidence. |
| **Novelty** | 4/5 | Ordinal depth estimation is a genuinely new task formulation. The differential response characterization, while following from known NLL location-shift properties, is a useful empirical contribution with a clear connection to theory. |
| **Significance** | 2/5 | Limited to ≤2.8B base models in a single domain. No evidence the approach scales to larger or instruction-tuned models that produce the vast majority of real-world LLM text. Negative downstream result further reduces practical impact. Primary value is scientific understanding of recursive generation dynamics in a controlled setting. |
| **Clarity** | 4/5 | Well-organized, clearly written, transparent about limitations. Dense but readable for 7 pages. Tables are informative and well-captioned. |
| **Overall Score** | **3 — Weak Reject** | See justification below |
| **Confidence** | 4/5 | Familiar with synthetic text detection, model collapse, and data curation literature. |

### Justification for Weak Reject

The paper introduces a genuinely novel task (ordinal depth estimation) and conducts thorough experiments with admirable transparency about limitations. The differential depth response pattern is a solid empirical finding, and the calibrated "diagnostic not curative" positioning shows scientific maturity.

However, several issues prevent acceptance at a top venue:

1. **Scale limitation is fundamental, not incremental.** All generators are ≤2.8B, and the visible degradation trend (0.84 → 0.73 across architectures) raises serious concerns about applicability to the 7B–70B+ models that dominate real-world LLM text generation. Without any evidence at larger scale, the findings may reflect properties of small models rather than universal depth signals.

2. **Single reference model is a critical uncontrolled variable.** Features computed under Pythia-410M scoring Pythia-generated text (same family) may yield artificially clean signals. No sensitivity analysis to reference model choice is provided.

3. **Practical impact is unclear.** The paper's own negative downstream result eliminates the primary applied motivation (data curation). The corpus-level diagnostic use case is asserted but not empirically validated. This leaves the contribution as primarily an empirical characterization study, which needs stronger evidence of generality to justify venue-level impact.

4. **Missing methodological details.** The downstream experiment — one of three claimed contributions — lacks sufficient detail for reproducibility.

The paper would benefit from: (a) evaluation with at least one 7B+ generator, (b) reference model sensitivity analysis, (c) a proper downstream experiment section with full methodology, and (d) corpus-level estimation validation. Addressing (a) and (b) would substantially strengthen the contribution claim.
