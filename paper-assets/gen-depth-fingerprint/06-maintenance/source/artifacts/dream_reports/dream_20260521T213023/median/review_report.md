---
dream_id: dream_20260521T213023
tier: median
overall_score: 3.0 — Borderline Findings
timestamp: 2026-05-21T22:28:41.096303+00:00
---

# Dream Review Report — Generation Depth Fingerprinting

**Paper**: "Generation Depth Fingerprinting: Classifying Recursive LLM Output Beyond Binary Detection"
**Venue**: EMNLP 2026 (ARR)
**Review mode**: Full (2-reviewer roundtable)
**Dream ID**: 20260521T213023

---

## Overall Assessment

| Dimension | Score |
|-----------|-------|
| Soundness | 3.5 |
| Excitement / Novelty | 2.5 |
| Reproducibility | 3.0 |
| **Overall Assessment** | **3.0** |

**Verdict**: Borderline Findings. The paper formulates a genuinely new task (generation depth classification) and provides thorough empirical investigation, but the novelty of DDR is partially anticipated by model-collapse literature, the practical significance is modest (binary F1 = 0.694, base models only), and several presentation issues (broken citations, overloaded main text, unfair QLoRA comparison) weaken the submission. With targeted revisions, this could reach a solid Findings acceptance.

---

## Summary

The paper proposes generation depth classification — estimating whether text is original (gen-0), first-generation LLM output (gen-1), or deeper recursive output (gen-2+). It introduces Differential Depth Response (DDR): surface features (hapax ratio, TTR) and central-tendency reference features (entropy mean) drift monotonically with depth (|ρ| > 0.50), while distributional shape features (entropy max, tail decay) remain near-stationary (|ρ| < 0.10), with a ~10× gap in KS statistics. A 7-feature XGBoost classifier achieves leak-free binary F1 = 0.694 under leave-one-generator-out (LOGO) evaluation across 5 generators from 3 families (0.6B–8B). The paper's most robust finding is negative: depth-aware data curation is statistically equivalent to random subsampling for downstream CLM quality (TOST p = 1.1×10⁻⁴ at ±2%), positioning depth fingerprinting as diagnostic rather than curative.

---

## Strengths

### S1. Genuine problem formulation (R2)
Generation depth classification as ordinal estimation is a meaningful reframing of AI-text detection. The distinction between "is this AI-written?" and "how deeply has this been recursively generated?" opens a new research direction with relevance to data provenance in an era of web-scale synthetic contamination.

### S2. Rigorous LOGO evaluation protocol (R1)
The leak-free evaluation design — training on N-1 generators, testing on the held-out — prevents generator-specific artifact leakage. Excluding gen-0 from binary F1 to avoid seed-sharing leakage is a subtle but important design choice. LOFO (cross-family) evaluation further strengthens the generalization claim (delta only 0.8pp).

### S3. Exceptionally thorough experimental coverage (R1 + R2)
16 experiment subsections covering feature ablation, cross-generator, cross-reference (3 models), cross-family, cross-domain (4 domains), prompt-type, paraphrastic chains, cross-model chains, scale effects (up to 8B), length confound exclusion, human-edit robustness, ordinal granularity, LD-Score, and end-to-end comparison. This breadth is unusual and commendable.

### S4. Honest "diagnostic not curative" framing (R2)
The negative finding is refreshingly honest. Many papers would either omit or underplay a result showing their method has no downstream utility. Here it becomes a central contribution, properly supported by TOST equivalence testing.

### S5. Appropriate statistical methodology (R1)
TOST for equivalence (downstream), McNemar for paired ablation, bootstrap for baseline comparison, Spearman ρ + KS statistics for DDR characterization. The statistical framework is well-chosen throughout.

### S6. Cross-reference validation (R1)
Testing DDR with 3 reference models from different families (Pythia-410M, OLMo-2-1B, Qwen3-0.6B) adds credibility. DDR direction is consistent across references; LOGO F1 varies only 1.3pp.

---

## Weaknesses

### W1. Broken citations — critical formatting issue (R2, Major)
Multiple references display "?" in the PDF (FastDetectGPT (?), Binoculars (?), at least one model-collapse reference, GLTR (?)). This is a LaTeX compilation error (\cite keys not resolving) that signals incomplete preparation. Under strict ARR review, this risks reviewer penalty and undermines credibility. **Must be fixed before submission.**

### W2. Related work coverage is inadequate (R2, Major)
- **Model collapse**: Only "LLM as Broken Telephone" (ACL 2025) cited. Missing foundational works: Shumailov et al. "AI models collapse when trained on recursively generated data" (Nature, 2024); Alemohammad et al. "Self-consuming generative models go MAD" (ICML 2024); Dohmatob et al. on scaling laws of model collapse (ICLR 2024). These directly study the recursive generation phenomenon this paper builds on.
- **Watermarking/provenance**: Entirely absent. Kirchenbauer et al. (2023), Christ et al. (2024) are alternative approaches to provenance tracking.
- **OOD detection**: Mentioned in one sentence without engaging specific methods.
- **AI-text detection completeness**: Missing recent works on intrinsic dimensionality (Tulchinskii et al.), training-data membership inference approaches, and multi-model attribution methods.

### W3. Base-model-only scope limits practical impact (R1 + R2, Major)
The paper reports OLMo-Instruct LOGO F1 = 0.338 vs 0.763 base — a 42.5pp degradation. Since virtually all deployed LLMs are instruction-tuned, the motivating scenario (tracking recursive contamination in web-scraped training data) is undermined. The instruct finding appears only in the Conclusion as a brief note. This deserves dedicated analysis: *why* does instruction tuning destroy depth signal? Is it the alignment process, the data, or the decoding? This limitation should be more prominently positioned and analyzed.

### W4. DDR thresholds are ad hoc (R1, Moderate)
The drifting (|ρ| > 0.50) / moderate (0.10 < |ρ| < 0.50) / near-stationary (|ρ| < 0.10) boundaries lack principled justification. No permutation testing, sensitivity analysis, or data-driven threshold selection is presented. The 10× KS gap provides compelling post-hoc support, but the ρ cutoffs appear chosen to fit the observed data pattern rather than derived from a principled criterion.

**Suggestion**: Use permutation testing to establish significance thresholds for ρ, or frame the three-tier structure as a descriptive observation rather than a formal classification.

### W5. Downstream negative finding rests on narrow evidence (R1, Moderate)
Only perplexity on a single CLM task with 3 seeds. Seed variance < 0.002 suggests near-deterministic outcomes — this tests one specific configuration, not robustness to hyperparameters or data splits. TOST at ±1% margin fails (p ≈ 0.09), meaning the equivalence claim is margin-dependent. Additional downstream tasks (text classification, QA) or metrics (loss on domain-specific benchmarks) would substantially strengthen this claim.

### W6. QLoRA comparison is unfair as presented (R1, Moderate)
Table 15 places QLoRA (within-generator CV) and 7-feature XGBoost (LOGO) in the same table under different "Eval" columns. While the paper acknowledges this difference, the visual juxtaposition invites misleading comparisons. QLoRA LOGO results are absent — the paper should either run QLoRA under LOGO or remove the comparison from the main results and discuss it qualitatively.

### W7. Decoding robustness claim is insufficiently supported (R1, Moderate)
Only greedy + top-k tested. The abstract mentions decoding robustness as a key property of DDR, but two strategies is thin evidence. Nucleus sampling (the most common practical strategy) and beam search are untested. The Limitations section acknowledges this, but the claim's prominence (abstract, contributions list) exceeds the evidence base.

### W8. Main text is overloaded (R2, Minor)
16 experiment subsections in ~3.5 pages results in superficial treatment of each (2-4 sentences). Experiments like paraphrastic comparison (§4.8), cross-model chains (§4.9), LD-Score (§4.16), and human-edit robustness (§4.13) could move to an appendix, allowing deeper analysis of core results (DDR characterization, LOGO evaluation, downstream finding).

### W9. DDR novelty is partially anticipated (R2, Minor)
Vocabulary impoverishment under recursive generation is documented in model-collapse literature. The contribution is the *quantitative* three-tier characterization and the *ordinal task formulation*, not the phenomenon itself. The paper should more explicitly position DDR relative to known distribution-narrowing dynamics from model-collapse theory.

---

## Detailed Per-Section Comments

### Abstract
- Well-structured, covers all three claims. The binary F1 = 0.694 headline is appropriately modest.
- "Robust across tested decoding strategies (greedy, top-k)" — the parenthetical hedging is necessary but the abstract should not lead readers to expect broad decoding robustness.
- Missing: Should mention the base-model-only scope restriction.

### §1 Introduction
- Clear motivation connecting recursive contamination to depth estimation.
- Three contributions are cleanly stated.
- "Existing detectors such as FastDetectGPT (?), Binoculars (?)" — broken citations are immediately visible.

### §2 Related Work
- Four subsections (AI-Text Detection, Model Collapse, Data Quality/OOD, Authorship Attribution) provide reasonable structure but each is too brief.
- Model collapse section has only one specific citation (ACL 2025) plus a broken "?" reference.
- OOD detection engagement is one sentence.
- No discussion of watermarking/provenance tracking alternatives.

### §3 Method
- §3.1 Problem formulation is clear and well-defined.
- §3.2 Feature design is motivated by DDR hypothesis — good.
- §3.3 DDR classification thresholds need justification (see W4).
- §3.4 Classifier description is minimal — XGBoost hyperparameters not specified.
- §3.5 Chain construction is adequate but prompt templates should be in appendix.

### §4 Experiments
- §4.1 Setup: Clear specification of 5 generators, 3 families, total dataset size.
- §4.2 Feature ablation (Table 1-2): Clean results, McNemar tests appropriate.
- §4.3 Cross-generator (Table 3): LOGO protocol well-executed. 6.8pp per-generator spread is reasonable.
- §4.4 Cross-reference (Table 5): Strong evidence for DDR non-artifact status.
- §4.5 Baseline comparison (Table 6): The narrow CI argument for 7-feature is the strongest selling point but is underemphasized in the text.
- §4.6 Downstream (Table 7): TOST is correct test but evidence is narrow (see W5).
- §4.7–4.16: Each subsection is too brief for the complexity of the experiment. Consider reorganizing.

### §5 Conclusion
- Appropriately summarizes findings. Instruct-model degradation mentioned here but deserves earlier, dedicated treatment.
- Future work directions are sensible (instruct models, larger scales, more decoding strategies).

### Limitations
- Three limitations adequately identified (base models only, decoding coverage, downstream narrowness). Well-written and honest.
- Missing: DDR threshold arbitrariness, QLoRA evaluation unfairness.

---

## Experiment Coverage Assessment

Comparing paper to the imagined experiment list (review_context.yaml):

| Experiment | Covered? | Quality |
|-----------|----------|---------|
| Feature ablation + DDR trend (plan_001) | ✅ Full | Good — Tables 1-2 |
| Cross-generator LOGO (plan_002) | ✅ Full | Good — Table 3 |
| Cross-reference model (plan_003) | ✅ Full | Good — Table 5 |
| Downstream utility (plan_004) | ✅ Full | Adequate — narrow metrics |
| Prompt-type comparison (plan_005) | ✅ Full | Brief but sufficient |
| Paraphrastic comparison (plan_006) | ✅ Full | Brief — could be appendix |
| Cross-model chains (plan_007) | ✅ Full | Brief — could be appendix |
| Multi-domain seeds (plan_008) | ✅ Full | Good — Table 11 |
| Finer-grained ordinal (plan_009) | ✅ Full | Good — Table 12 |
| Human-edit robustness (plan_010) | ✅ Full | Brief — could be appendix |
| LD-Score feature (plan_011) | ✅ Full | Brief — could be appendix |
| End-to-end classifier (plan_012) | ✅ Partial | Unfair comparison (W6) |
| Text length control (plan_013) | ✅ Full | Good — Table 16 |
| Large-scale generator (plan_014) | ✅ Full | Good — Table 13 |
| Baseline comparison (plan_015) | ✅ Full | Good — Table 6 |

All 15 experiments are present. Coverage is comprehensive. Main issue is depth-vs-breadth tradeoff in main text.

---

## Questions for Authors

1. How were the DDR ρ thresholds (0.50, 0.10) determined? Would a permutation-based approach change the three-tier grouping?
2. Have you considered running QLoRA under LOGO to enable fair comparison with 7-feature XGBoost?
3. Why does instruction tuning destroy depth signal so dramatically (42.5pp drop)? Is this the alignment loss, the instruction data distribution, or RLHF/DPO specifically?
4. Can you test nucleus sampling (p=0.9, 0.95) for decoding robustness before submission?
5. Would adding one more downstream task (e.g., text classification accuracy on depth-stratified training data) strengthen the negative finding?

---

## Recommendation

**Overall: 3.0 — Borderline Findings**

The paper formulates a genuinely new task and provides unusually thorough empirical investigation. The DDR characterization is a useful empirical contribution, and the "diagnostic not curative" negative finding is well-supported by appropriate statistical testing. However, the practical significance is limited by base-model-only scope, the novelty of DDR is partially anticipated by model-collapse literature, and presentation issues (broken citations, missing references, overloaded main text, unfair QLoRA comparison) need addressing.

**To reach solid Findings (3.5):**
1. Fix all broken citations immediately.
2. Add 3-4 foundational model-collapse references and position DDR relative to them.
3. Move 4-5 peripheral experiments to appendix; deepen analysis of core results.
4. Either run QLoRA under LOGO or remove the comparison.
5. Add nucleus sampling to decoding robustness experiments.
6. Expand downstream experiment to at least one additional task/metric.

**To reach Conference (4.0):**
All of the above, plus:
7. Extend to instruction-tuned models with adapted features or alternative approach.
8. Provide principled DDR threshold derivation.
9. Test on frontier-scale models (14B+).

---

## Reviewer Agreement

| Dimension | R1 | R2 | Consensus |
|-----------|----|----|-----------|
| Soundness | 3.5 | 3.0 | 3.5 |
| Excitement | — | 2.5 | 2.5 |
| Reproducibility | 3.0 | — | 3.0 |
| Overall | 3.0 | 3.0 | **3.0** |

Both reviewers independently converged on 3.0. The paper has solid methodology but limited novelty and practical impact in its current form. Findings-level acceptance is plausible if presentation issues are resolved.