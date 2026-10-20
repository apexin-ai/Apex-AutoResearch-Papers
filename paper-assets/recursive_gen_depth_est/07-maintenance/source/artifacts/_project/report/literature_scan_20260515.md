# Literature Scan: Recursive Generation Depth Estimation
**Date:** 2026-05-15  
**Scope:** 2026 Jan–May (arXiv / published), plus late-2025 papers accepted at 2026 venues  
**Focus:** Is anyone doing recursive generation depth/iteration count estimation?

---

## Executive Summary

**No direct competitor found.** No paper specifically addresses the problem of predicting how many recursive model→data→model iterations a text has undergone. The niche remains open.

Key developments in adjacent areas:
- Model collapse theory has advanced significantly (3 new theoretical papers in Feb 2026)
- AI text detection community is moving toward surprisal-diversity features (DivEye) and generator-agnostic methods — both relevant as method components
- Provenance/attribution work focuses on "which model generated this" rather than "how many generations deep"

---

## Papers by Relevance

### METHOD-COMPONENT (directly usable techniques)

#### 1. DivEye: Diversity Boosts AI-Generated Text Detection
- **arXiv:** 2509.18880 | **Venue:** TMLR Feb 2026, ICLR 2026
- **Authors:** Basani & Chen (IBM)
- **Summary:** Uses token-level surprisal diversity features (distributional moments, first-order shifts, second-order dynamics) to detect AI text. Outperforms zero-shot detectors by up to 33.2%.
- **Relation:** Our project uses similar statistical features (perplexity, surprisal). DivEye's higher-order surprisal statistics could be strong features for depth regression. Their feature set is a natural baseline/component. **Already cited in project — verify feature overlap with our implementation.**

#### 2. Breaking the Generator Barrier: Disentangled Representation for Generalizable AI-Text Detection
- **arXiv:** 2604.13692 | **Date:** Apr 2026
- **Authors:** Pu, Cheng, Yuan, Wu, Bi (Chongqing Univ.)
- **Summary:** Disentangles AI-detection semantics from generator-specific artifacts via dual-bottleneck + perturbation regularization. Aims for cross-generator generalization.
- **Relation:** If we want depth estimation to generalize across different base models, their disentanglement approach could inform our feature design. The "generator-agnostic detection signal" is analogous to what we need for "depth-agnostic-to-model" estimation.

#### 3. Machine-Generated Text Detection Prevents Language Model Collapse
- **arXiv:** 2502.15654 | **Date:** Feb 2025 (updated May 2025)
- **Authors:** (multiple)
- **Summary:** Shows that filtering synthetic data via MGT detection before retraining mitigates collapse. Analyzes text characteristics at each model generation and their similarity to human references.
- **Relation:** They analyze per-generation text characteristics — similar signal space to ours. Difference: they use detection as a filter, we use it for depth regression. Their per-generation analysis may contain useful signal characterization.

#### 4. Why AI-Generated Text Detection Fails: Evidence from Explainable AI
- **arXiv:** 2603.23146 | **Date:** Mar 2026
- **Authors:** Pudasaini et al.
- **Summary:** Despite F1=0.9734 in-domain, detection degrades severely under distribution shift. Most discriminative features are also most shift-sensitive.
- **Relation:** **Important caveat for our approach.** If surface statistical features are domain-fragile for binary detection, they may be even more fragile for ordinal depth regression. We should test cross-domain robustness explicitly.

---

### BACKGROUND (model collapse dynamics — informs what signals exist at each depth)

#### 5. From Collapse to Improvement: Statistical Perspectives on Iterative Training
- **arXiv:** 2602.10531 | **Date:** Feb 2026
- **Authors:** Bakshi & Chakraborty
- **Summary:** Proves that iterative training on contaminated data (mixture of real + synthetic) can *improve* performance if sufficient fresh real data is mixed in. Analyzes how mixture weights and sample size control long-term trajectory.
- **Relation:** Directly relevant to understanding the signal landscape. If some depth levels actually *improve* (not degrade), our regression target may be non-monotonic. Their theoretical framework helps predict when depth signals are strong vs. weak.

#### 6. Can Generative AI Survive Data Contamination? Theoretical Guarantees
- **arXiv:** 2602.16065 | **Date:** Feb 2026
- **Authors:** Wang, Niu, Li
- **Summary:** Extends model collapse theory beyond Gaussian/discrete to more realistic distribution families. Provides guarantees under contaminated recursive training.
- **Relation:** Provides stronger theoretical grounding for why our depth signal should exist in realistic settings (not just toy distributions).

#### 7. Curated Synthetic Data Doesn't Have to Collapse
- **arXiv:** 2605.07724 | **Date:** May 2026
- **Authors:** Falahati, Amiri, Larson, Golab
- **Summary:** Pluralistic curation (multiple reward functions) prevents collapse. Converged distribution satisfies weighted Nash bargaining.
- **Relation:** If curated recursive training doesn't collapse, the statistical drift we rely on for depth detection may not manifest. This defines a harder case for our method — curated pipelines may produce depth-invariant text.

#### 8. Synthetic Eggs in Many Baskets: Impact of Synthetic Data Diversity on LLM Fine-Tuning
- **arXiv:** 2511.01490 | **Venue:** ACL 2026 Findings
- **Authors:** (multiple)
- **Summary:** Multi-source synthetic data reduces distribution collapse. Measures perplexity, Self-BLEU-3, lexical diversity within/across responses.
- **Relation:** Their diversity metrics (Self-BLEU, lexical diversity) are candidate features for our depth predictor. Their finding that source diversity modulates collapse rate means our model needs to be robust to source-diversity variation.

#### 9. Knowledge Collapse in LLMs: Fluency Survives but Facts Fail
- **arXiv:** 2509.04796 | **Date:** Sep 2025
- **Summary:** Defines three-stage knowledge collapse: factual accuracy degrades while surface fluency persists. Domain-specific training delays collapse 15×.
- **Relation:** Key insight: surface fluency is not a reliable depth signal; factual accuracy is. Our features should capture factual degradation, not just stylistic shifts. Suggests incorporating factual consistency metrics.

---

### PROVENANCE/ATTRIBUTION (related problem, different angle)

#### 10. Unknown Aware AI-Generated Content Attribution
- **arXiv:** 2601.00218 | **Date:** Jan 2026
- **Summary:** Attribution framework handling unknown generators. Assigns content to known models or flags as unknown.
- **Relation:** They solve "which model?" — we solve "how many iterations?" Complementary problems. Their open-set recognition approach could inform how we handle unknown base models.

#### 11. Explainable Disentangled Representation for Authorship Attribution in the Era of GenAI
- **arXiv:** 2604.21300 | **Date:** Apr 2026
- **Summary:** Disentangled representations for authorship attribution across human and AI authors.
- **Relation:** Authorship attribution at the model level is adjacent to depth attribution. Their disentanglement framework could extend to depth as an additional latent factor.

#### 12. A Faceted Proposal for Transparent Attribution of AI-Assisted Text
- **arXiv:** 2604.25346 | **Date:** Apr 2026
- **Summary:** Multi-faceted attribution model covering Form, Generation, Evaluation, Intent, Control, Traceability.
- **Relation:** Their "Traceability" facet is closest to our depth problem. Their framework could position our work as solving one specific facet of a broader attribution problem.

---

### EVALUATION (benchmarks/methods)

#### 13. Interpretable Predictability-Based AI Text Detection: A Replication Study
- **arXiv:** 2603.15034 | **Date:** Mar 2026
- **Summary:** Replicates and extends predictability-based detection systems from AuTexTification 2023.
- **Relation:** Provides a reproducibility baseline for predictability-based methods. Useful for sanity-checking our feature pipeline.

---

## Key Takeaways for the Project

1. **No competitor for depth regression.** Binary detection (human vs. AI) and source attribution (which model) are crowded. Ordinal depth estimation remains novel.

2. **DivEye's surprisal features are the closest method overlap.** Ensure we cite it properly and demonstrate that our depth-regression features go beyond their binary classification features.

3. **Model collapse theory now shows non-monotonic dynamics** (paper #5). Our depth signal may not increase linearly — important for regression model design (consider non-linear targets).

4. **Curated/diverse recursive training weakens depth signal** (papers #7, #8). This should be discussed as a limitation and tested as a hard case.

5. **Factual degradation > stylistic degradation as depth signal** (paper #9). Consider adding factual consistency features beyond perplexity/surprisal.

6. **Detection features are domain-fragile** (paper #4). Cross-domain evaluation is essential for credibility.
