---
dream_id: dream_20260521T213023
tier: worst
overall_score: 2.0 — Resubmit next cycle
timestamp: 2026-05-21T22:34:08.847115+00:00
---

# Dream Review Report — Differential Depth Response in Recursive Autoregressive Generation

**Dream ID:** 20260521T213023  
**Target Venue:** EMNLP 2026 (via ARR)  
**Review Mode:** Full (2 Reviewers, 4-step roundtable)

---

## Roundtable Summary

**R1 focus:** Methods, experiments, statistical validity, evaluation rigor  
**R2 focus:** Novelty, related work, framing, writing quality, community impact

Both reviewers converge on the assessment that the paper presents a comprehensive experimental study but suffers from (1) modest headline performance that existing tool ensembles match, (2) a theoretical framework (DDR) undermined by the paper's own QLoRA results, (3) scope restrictions that eliminate practical relevance in 2026, and (4) a negative downstream finding that collapses the task motivation without a convincing replacement narrative.

---

## Reviewer 1: Methods & Experiments

### Summary
The paper formulates generation depth classification and presents an extensive experimental evaluation across 8 generators, 4 domains, multiple prompt types, and robustness conditions. The experimental methodology is rigorous (LOGO/LOFO, bootstrap CIs, TOST) but the headline performance (binary F1=0.694, margin 0.194 over chance) is insufficient to support a practical classification tool claim, and multiple results internally undermine the contributions.

### Strengths
- **Comprehensive experimental coverage:** 17 tables spanning ablation, cross-generator, cross-domain, cross-reference, scale, prompt type, chain type, robustness, confound control, baselines, and end-to-end comparison. Few empirical papers at EMNLP achieve this breadth.
- **Leak-free evaluation design:** Excluding gen-0 from binary F1 avoids seed-sharing confound — a subtle but important methodological choice.
- **Rigorous generalization protocol:** LOGO (8-fold, per-generator) and LOFO (5-fold, per-family) provide credible generalization estimates.
- **Honest negative reporting:** Downstream utility (Table 7), scale degradation (Table 9), instruct failure (Limitations), and QLoRA gap (Table 16) are all reported transparently.
- **Statistical rigor:** Bootstrap CIs with 10K resamples, TOST for equivalence testing, McNemar for paired comparisons. Appropriate statistical methods throughout.

### Weaknesses

**W1. Headline performance insufficient (Table 3, Critical).** Binary F1=0.694 provides only 0.194 margin over the random baseline (0.50) for a balanced binary task. Per-generator range spans 9.1pp (Pythia-1B 0.724 → Mistral-7B 0.633). The two largest generators — which are most relevant for real-world contamination — perform worst (Mistral-7B 0.633, Qwen3-8B 0.647). At these models, approximately 1 in 3 gen-2+ samples is misclassified.

**W2. Multi-detector ensemble parity (Table 5, Critical).** The 4-detector + surface ensemble achieves 3-class F1=0.795 vs 7-feature 0.798 (p=0.72, not significant) and binary F1=0.708 vs 0.705 (7-feature is actually *lower*). This means existing detection tools, naively combined in the same XGBoost pipeline, achieve identical depth classification without the DDR framework, without a reference model, and without the 7-feature engineering. The paper's primary contribution — the 7-feature ensemble and DDR — provides zero marginal value over existing tools on the primary metric.

**W3. QLoRA gap undermines feature selection rationale (Table 16, Major).** QLoRA classifiers beat the 7-feature ensemble by 14–17pp binary F1. More critically, instruct-model QLoRA achieves the highest F1 (Qwen-Instruct binary 0.867), directly contradicting the Limitations claim that instruction tuning degrades depth signal. Instruction tuning degrades the *specific features selected*, not the depth signal itself. This means the DDR framework captures a partial, instrument-specific view of depth information, not the underlying phenomenon.

**W4. Scale degradation trajectory (Table 9, Major).** Qwen3-8B shows 10.6pp LOGO degradation vs smaller-model average, with feature drift magnitudes compressed to ~72%. The negative linear relationship between log(model_size) and F1 projects to near-chance performance at ~30B parameters. The paper acknowledges this as a limitation but the implication is severe: the method has no relevance for any model generating text at scale.

**W5. Domain-motivation mismatch (Table 13, Major).** The introduction motivates with "7–17% of recent scientific publications contain LLM content," yet academic domain F1=0.628 (−18.7pp vs Wikipedia). Cross-domain LOGO drops to 0.668. The method is weakest precisely where the stated motivation is strongest. Wikipedia dominance (best domain, primary training domain) suggests feature distributions are overfitted to one domain's characteristics.

**W6. 86% FN bias (Section 5.2, Major).** 86% of binary errors are false negatives — gen-2+ misclassified as gen-1. The method systematically under-detects deeper generations, which are precisely the contamination signals most important to identify. This structural bias means the method would miss the majority of the "deeper contamination" it claims to detect.

**W7. Fragile to editing (Table 14, Moderate).** 5% random replacement or LLM rephrasing reduces binary F1 by 4.5pp. Degradation is approximately linear with perturbation intensity, confirming the signal resides in surface-level distributional properties easily disrupted by any text modification. In practice, LLM-generated text is almost always edited before publication.

**W8. Cross-model confound (Table 6, Moderate).** Cross-model chains yield +13.6pp LOGO over single-model, suggesting the method partly detects generator switching (different model fingerprints at each depth step) rather than pure depth. The "honest" depth number is 0.694 (single-model); the cross-model improvement is trivially explained by OOD detection of different model fingerprints.

**W9. DDR dichotomy not clean (Table 1, Moderate).** entropy_std (ρ=−0.20, R²=0.41) sits in an "ambiguous" zone between drifting and stationary. The binary classification (|ρ|>0.50 = drifting, |ρ|<0.10 = stationary) is threshold-dependent. A continuous degradation spectrum with arbitrary cutpoints better describes the data than a clean bimodal phenomenon.

**W10. Reference model magnitude dependence (Table 10, Moderate).** Drift direction is consistent across reference models, but magnitude varies ~2× (OLMo reference ≈55% of Pythia's drift). The claimed "intrinsic differential response" is substantially measurement-relative: the characterization changes based on reference model choice.

**W11. Length confound (Table 17, Minor).** 4.6pp drop after length matching means ~6% of signal is length-attributable. Combined with editing fragility (W7) and domain dependence (W5), the cumulative confound sensitivity suggests reported numbers may be inflated by uncontrolled factors.

**W12. 5-class collapse (Table 8, Moderate).** F1=0.498 with gen-2/3/4 confusion at 48–51%. Ordinal methods (CORAL, Frank-Hall) provide no improvement. Depth signal lacks ordinal structure beyond coarse 3-class binning. The "generation depth classification" framing overclaims — this is at most binary-plus-one detection.

### Questions for Authors
1. Given multi-detector ensemble parity (Table 5), what is the marginal contribution of the DDR framework beyond providing an interpretive lens?
2. How do you reconcile claiming instruction tuning degrades depth signal (Limitations) with instruct QLoRA achieving the highest F1 (Table 16)?
3. What is the intended use case for a method that works primarily on Wikipedia-domain base-model text at moderate temperature?
4. At what model scale does the method become equivalent to random guessing?

### Scores
- **Soundness:** 3/5 — Experiments are well-designed and appropriately controlled, but conclusions sometimes overreach the data (particularly the "intrinsic" DDR claim and the scope of "generation depth classification").
- **Excitement:** 2/5 — Modest performance matched by existing tool ensembles; narrow scope; no clear impact path.
- **Reproducibility:** 4/5 — Detailed protocol, standard tools (XGBoost, public models), clear evaluation metrics. Dataset construction is reproducible.
- **Overall Assessment:** 2.0 — Resubmit next cycle.
- **Confidence:** 4/5

---

## Reviewer 2: Novelty & Related Work

### Summary
The paper asks an interesting question — can we estimate generation depth beyond binary detection? — but the answers it provides are underwhelming. The task formulation reduces to binary-plus-one classification, the DDR framework repackages known vocabulary impoverishment without novel insight, the negative downstream finding undermines the paper's own motivation, and the scope restrictions eliminate practical relevance. The paper reads as a thorough negative-result report that has not yet found the right framing for its contributions.

### Strengths
- **First systematic study of generation depth:** The question "how many autoregressive passes separate this text from human writing?" is genuinely worth investigating, even if the current results are modest. Formulating the problem is a contribution.
- **Honest scientific reporting:** Negative findings (downstream utility, scale degradation, instruct failure) are given prominent treatment rather than being hidden. This scientific integrity is commendable and rare.
- **DDR interpretation is interesting:** The location-shift-but-shape-preserved characterization of recursive generation is a useful theoretical lens for the model collapse community, even if the evidence is not conclusive.
- **Comprehensive appendix:** Prompt types, paraphrastic chains, multi-domain, robustness, length control, LD-Score, QLoRA — the paper leaves few stones unturned.

### Weaknesses

**W1. Task novelty is shallow (Table 8, Critical).** "Generation depth classification" is positioned as a new task, but the 5-class experiment reveals the truth: F1=0.498, gen-2/3/4 confusion at 48–51%, ordinal methods provide no improvement. The depth signal is effectively binary (source-adjacent vs deep) with a modest third class. This is an incremental extension of binary detection — adding one class boundary — not a qualitatively new task formulation. The "ordinal depth" framing is not supported by the data.

**W2. DDR repackages known phenomena (Critical).** All three "drifting" features (hapax ratio, TTR, entropy_mean) measure vocabulary diversity decline — a phenomenon extensively documented in model collapse literature (Shumailov et al. 2024), stylometry, and information-theoretic analyses of recursive generation. The LD-Score experiment (Table 15, +0.4pp marginal improvement) confirms that character-level, word-level, and NLL-level features all measure the same underlying signal. The DDR "drifting/stationary" dichotomy adds terminology to an existing observation without providing new mechanistic understanding. The paper never shows what DDR enables that "measuring vocabulary impoverishment at multiple levels" does not.

**W3. Negative finding collapses task motivation (Table 7, Critical).** Claim 3 establishes that depth-aware curation provides zero benefit over random subsampling — indeed, depth-filtered data is slightly *worse* (PPL 2.387 vs 2.367). This eliminates the most obvious practical motivation for depth classification. The pivot to "diagnostic tool" is asserted but never demonstrated: the paper provides no concrete scenario where a diagnostic depth estimate (at F1=0.694) changes an analysis, decision, or understanding that wasn't available from binary detection alone.

**W4. Related work is inadequate (Section 2, Major).** Four short paragraphs are insufficient for a paper that spans detection, model collapse, data curation, and stylometry. Missing engagements include:
- Training data attribution (influence functions, membership inference for provenance)
- Watermarking approaches for generation provenance tracking
- Distributional shift and domain adaptation literature (relevant to cross-domain results)
- Recursive self-improvement / self-play literature
- Data contamination detection in benchmarks (relevant to the scientific contamination motivation)
The paper needs to explain why these adjacent approaches do not already answer the questions it poses.

**W5. Scope renders the work impractical (Critical).** The method works only on: base models (instruct LOGO=0.338, per Limitations), temperature ∈ [0.5, 0.9], Wikipedia-dominant domain, continuation chains preferred, no human editing, models ≤8B with degrading performance. In 2026, virtually all deployed LLM text is generated by instruction-tuned models at varying temperatures, often edited, from models ≥70B. The remaining applicable scope — base model text at moderate temperature from small models without editing — is a vanishingly narrow niche that does not justify a top-venue publication.

**W6. QLoRA undermines theoretical framework (Table 16, Major).** Instruct QLoRA achieves 0.867 binary F1, exceeding all base-model QLoRA variants. This proves: (a) depth signal survives instruction tuning; (b) the DDR features are an incomplete measurement, not a characterization of the phenomenon; (c) the "drifting/stationary" split describes feature behavior, not recursive generation dynamics. The paper's central theoretical contribution is undermined by its own appendix experiment.

**W7. No figures in main text (Major, Presentation).** An empirical paper about "distributional dynamics" contains zero visualizations across 8 pages. Feature drift curves, confusion matrices, scale degradation plots, and DDR pattern illustrations would communicate the core findings far more effectively than the 17 tables. This is a significant presentation failure that makes the paper harder to read and less memorable.

**W8. Paraphrastic comparison does not support claims (Table 12, Moderate).** The 3.3pp binary F1 gap between paraphrastic and continuation chains is too small to claim qualitatively different depth dynamics. The paper's own data suggests depth signal is a generic property of recursive generation, undermining the positioning against Briesch et al. (2025) and the claim that non-paraphrastic chains are the interesting case.

**W9. Writing structure needs work (Moderate).** The Conclusion (Section 7) restates the abstract rather than discussing implications. The paper doesn't address what the DDR framework *enables* — it only describes what it *measures*. For a paper positioning DDR as an "analytical framework," the paper needs to demonstrate analysis enabled by the framework. The narrative reads as "we tried many things, most worked modestly, some didn't work at all" rather than building toward a coherent insight.

**W10. "Diagnostic tool" claim is unsubstantiated (Moderate).** After the downstream utility negative finding, the paper pivots to positioning DDR as a "diagnostic rather than curative tool." But no diagnostic use case is demonstrated. What does a researcher or practitioner learn from knowing generation depth (at F1=0.694) that they cannot learn from binary detection? This claim needs an explicit worked example or case study.

### Questions for Authors
1. Can you articulate a specific 2026 scenario where generation depth classification (at F1=0.694) changes a decision that binary detection alone cannot inform?
2. How does the DDR framework differ from "measuring degree of vocabulary impoverishment" — a concept that requires no new framework?
3. Given QLoRA instruct achieves the best depth classification, what is the status of the claim that DDR captures the essential structure of recursive generation dynamics?
4. Why does the paper contain no figures in the main text?

### Scores
- **Soundness:** 3/5 — Experiments are competent; interpretation overclaims in places (particularly "intrinsic" DDR and the generation depth task scope).
- **Excitement:** 1.5/5 — Limited novelty (vocabulary impoverishment repackaged), narrow practical scope, no demonstrated impact beyond the paper itself.
- **Reproducibility:** 4/5 — Clear protocol and standard tools; dataset construction is reproducible.
- **Overall Assessment:** 2.0 — Resubmit next cycle.
- **Confidence:** 4/5

---

## Roundtable Convergence (Step 3)

### Points of Agreement
1. **Performance is insufficient for the claims** — both reviewers agree 0.694 binary F1 with 0.194 margin over chance is too thin for a classification tool contribution, especially with 9.1pp per-generator variance and worst performance on the largest models.
2. **Multi-detector ensemble parity is the strongest counterargument** — existing tools, naively combined, achieve identical performance without DDR. This challenges the paper's reason to exist as a methods contribution.
3. **QLoRA gap fundamentally undermines the DDR framework** — instruct QLoRA achieving highest F1 proves depth signal survives instruction tuning; DDR features are an incomplete measurement. The theoretical framework describes the instrument, not the phenomenon.
4. **Scope is too narrow for 2026 relevance** — base-model-only, moderate temperature, Wikipedia-dominant, no editing, ≤8B models. This niche is vanishingly small.
5. **Negative downstream finding collapses practical motivation** — the pivot to "diagnostic tool" is unsubstantiated. No diagnostic use case is demonstrated.
6. **Task reduces to binary-plus-one** — 5-class collapse (0.498 F1, 48-51% deep confusion) confirms depth is not an ordinal quantity in this feature space.
7. **Experimental methodology is rigorous** — LOGO/LOFO, bootstrap CIs, TOST, comprehensive controls. Both reviewers rate Soundness=3, Reproducibility=4.

### Points of Disagreement
- R2 places more emphasis on the missing figures as a presentation failure; R1 focuses on numerical findings.
- R1 is marginally more generous on novelty ("the question is worth asking") while R2 views the task formulation itself as shallow.
- R2 identifies related work inadequacy more strongly; R1 focuses on internal experimental contradictions.

**Resolution:** Both positions are complementary. The paper has rigorous experiments that comprehensively demonstrate the limitations of its own approach. The contributions — as currently framed — do not meet the EMNLP 2026 bar for Main or Findings.

---

## Consolidated Assessment (Step 4)

### Overall Score: **2.0 — Resubmit next cycle**

### Score Breakdown
| Dimension | R1 | R2 | Consensus |
|-----------|----|----|-----------|
| Soundness | 3 | 3 | **3** |
| Excitement | 2 | 1.5 | **1.5** |
| Reproducibility | 4 | 4 | **4** |
| Overall Assessment | 2.0 | 2.0 | **2.0** |
| Confidence | 4 | 4 | **4** |

### Rationale
The paper is well below the Main conference threshold (4.0) and below the Findings threshold (3.0). While the experimental methodology is commendable, three structural problems prevent acceptance:

1. **No contribution survives internal scrutiny.** Contribution 1 (DDR characterization) is undermined by QLoRA showing the features are instrument-specific, not phenomenon-specific. Contribution 2 (7-feature classifier) is matched by multi-detector ensemble (Table 5). Contribution 3 (negative finding) is scientifically honest but collapses the paper's own motivation.

2. **The scope problem is fatal.** In 2026, restricting to base models at moderate temperature in Wikipedia-like domains without editing covers essentially no real-world text. The paper acknowledges this (Limitations) but the acknowledgment doesn't resolve the problem — it confirms the method has no path to practical impact.

3. **The framing has no clear landing zone.** The paper oscillates between "practical classification tool" (undermined by modest performance and scope restrictions), "analytical framework" (undermined by QLoRA showing DDR captures partial signal), and "negative result contribution" (which requires a stronger theoretical frame than provided). A successful resubmission needs to commit to one framing and support it convincingly.

### Key Recommendations for Resubmission
1. **Reframe around distributional characterization, not classification.** The DDR location-shift-vs-shape-preservation finding is the most interesting theoretical observation. Center the paper on this as an analytical contribution to the model collapse literature. Demote the classifier to a validation probe.
2. **Confront the QLoRA result head-on.** Either explain theoretically why DDR features capture a *different* aspect of depth than end-to-end classifiers, or acknowledge that DDR is an interpretable-but-incomplete approximation and articulate why interpretability matters.
3. **Add instruct-model analysis.** The base-model-only scope is the biggest limitation. Even negative results on instruct models (carefully analyzed) would strengthen the contribution.
4. **Include figures.** Feature drift curves, confusion matrices, scale degradation plots, and DDR pattern illustrations are essential for an empirical distributional dynamics paper.
5. **Expand related work.** Engage with training data attribution, watermarking, distributional shift, and data contamination detection literatures.
6. **Demonstrate a diagnostic use case.** If the paper claims DDR is a "diagnostic tool," provide at least one concrete example where the diagnostic changes an analysis or decision.

### Auto-Reject Signal Check
- ☑ Anonymity: No violations detected
- ☑ Page limit: 8 pages main text (compliant)
- ☑ Limitations section: Present (adequate coverage of 3 key limitations)
- ☐ Figures: None in main text (not an auto-reject signal, but a significant presentation weakness)
- ☑ References: 10 cited works, all appear legitimate (though the bibliography is thin for the scope claimed)