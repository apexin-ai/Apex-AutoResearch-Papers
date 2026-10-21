# Literature Incremental Scan: Model Collapse + Synthetic Text Detection (2025-2026)

> Scan date: 2026-05-13
> Coverage: 2025-01 to 2026-05
> Purpose: Expand related work for gen-depth-contamination paper; assess novelty threats

---

## Novelty Impact Summary

| Question | Answer | Impact on Our Paper |
|----------|--------|-------------------|
| Has anyone done **ordinal depth estimation** (K prediction, not binary)? | **No** | Core novelty intact |
| Has anyone quantified a **discrimination boundary K*** (saturation point)? | **No** | Core novelty intact |
| New detection features usable as baselines? | **Yes** — DivEye (surprisal diversity), MAGRET (contrastive rewriting) | Add as baselines in full study |
| New model collapse results that change our framing? | **Yes** — Schaeffer 2025 clarifies 8 definitions; need precise positioning | Tighten our definition of "collapse" vs "saturation" |

---

## Thread 1: Binary Synthetic Text Detection

### [NEW] DivEye: Diversity Boosts AI-Generated Text Detection
- **Authors**: Basani, Chen (IBM Research)
- **Venue**: TMLR 2026 (also PAN 2025 shared task)
- **URL**: https://arxiv.org/abs/2509.18880
- **Core contribution**: Zero-shot detector based on surprisal diversity — measures how token-level surprisal fluctuates across text. Human text has richer variability in lexical/structural unpredictability than LLM outputs. Outperforms existing zero-shot detectors by up to 33.2%.
- **Relation to us**: **Complementary / potential baseline**. DivEye features (surprisal diversity statistics) could be added to our feature set for depth estimation. The "rhythmic unpredictability" signal may degrade monotonically with generation depth — worth testing.
- **Code**: https://github.com/IBM/diveye

### [NEW] MAGRET: Machine-generated Text Detection with Rewritten Texts
- **Authors**: Huang, Cao, Luo, Guan, Liu
- **Venue**: COLING 2025
- **URL**: https://aclanthology.org/2025.coling-main.557/
- **Core contribution**: Fine-tunes BERT encoder via contrastive learning on LLM-rewritten versions of texts. Uses semantic/statistical relationships between rewritten and original texts for detection and source traceability.
- **Relation to us**: **Complementary**. MAGRET's rewriting-based contrastive approach is related but only does binary detection + source model ID, not depth estimation. The rewriting paradigm is tangential to our recursive generation setup.
- **Code**: Not found

### [SURVEY] AI-Generated Text Detection: A Comprehensive Review (2025-2026)
- **URL (ScienceDirect)**: https://www.sciencedirect.com/science/article/abs/pii/S1574013725000693
- **Core contribution**: Comprehensive survey of active (watermarking) and passive (statistical/neural) detection methods. Categorizes approaches into feature-based, neural, and hybrid.
- **Relation to us**: **Context**. Confirms binary detection is well-explored; our ordinal framing is absent from the literature.

### [CONTEXT] COLING 2025 Workshop on Detecting AI Generated Content
- **URL**: https://genai-content-detection.gitlab.io/
- **Note**: Shared tasks on binary detection and cross-domain MGT detection. No task on depth/generation-order estimation.

---

## Thread 2: Model Collapse / Iterative Retraining

### [ALREADY CITED] Strong Model Collapse — Dohmatob, Feng, Subramonian, Kempe
- **Venue**: ICLR 2025
- **URL**: https://arxiv.org/abs/2410.04840
- **Core contribution**: Even 0.1% synthetic data causes collapse in scaling-law regime. Larger models can amplify collapse before the interpolation threshold.
- **Relation to us**: Already in our related work. Key reference for theoretical grounding.

### [NEW] Position: Model Collapse Does Not Mean What You Think — Schaeffer, Kazdan, Koyejo et al.
- **Venue**: ICML 2025
- **URL**: https://arxiv.org/abs/2503.03150
- **Core contribution**: Identifies **8 distinct definitions** of model collapse across 28 papers, grouped into 3 families: (1) test loss behavior over iterations, (2) distribution deformation, (3) scaling behavior. Argues many prominent collapse scenarios rely on unrealistic "replace" assumptions. Real practice accumulates data.
- **Relation to us**: **Critical for framing**. We must precisely define what we mean by "saturation" vs "collapse." Our K* is about **discriminability saturation** (definition family 2: distribution deformation), not test loss. This paper helps us position cleanly. Should cite.
- **Code**: N/A

### [NEW] Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World — Kazdan, Schaeffer et al.
- **Venue**: ICML 2025
- **URL**: https://arxiv.org/abs/2410.16713
- **Core contribution**: Empirically compares "replace" vs "accumulate" regimes across Gaussian estimation, KDE, and LM fine-tuning. Finds non-trivial interaction: value of synthetic data depends on absolute quantity of real data.
- **Relation to us**: **Complementary**. Their accumulate/replace distinction maps to different contamination scenarios we should discuss. In the "accumulate" regime K* may shift upward.
- **Code**: Available

### [NEW] A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective — He et al.
- **Venue**: NeurIPS 2025
- **URL**: https://arxiv.org/abs/2509.16499
- **Core contribution**: Identifies generalization→memorization transition in diffusion models during iterative retraining. Entropy of training data decreases over iterations and correlates with model degradation. Proposes entropy-based data selection.
- **Relation to us**: **Strongly complementary**. The entropy decrease over iterations parallels our feature-space convergence. Their "entropy as collapse indicator" aligns with our use of statistical features to measure generation depth. Different modality (images vs text) but same conceptual framework.
- **Code**: https://shilianghe007.github.io/model-collapse/

### [NEW] Future of AI Models: A Computational Perspective on Model Collapse — Satharasi et al.
- **Venue**: arXiv preprint (Oct 2025)
- **URL**: https://arxiv.org/abs/2511.05535
- **Core contribution**: Measures semantic similarity in Common Crawl/Wikipedia over 2013-2025 using Transformer embeddings. Observes exponential rise in similarity post-ChatGPT. Projects 90% saturation ~2035.
- **Relation to us**: **Supporting**. Provides real-world evidence that recursive contamination is measurable at web scale. Their year-wise similarity trajectory is analogous to our depth-wise feature trajectories.
- **Code**: Not found

### [NEW] Assessing Diversity Collapse in Reasoning — (2025/2026)
- **Venue**: Under review (OpenReview)
- **URL**: https://openreview.net/pdf?id=AMiKsHLjQh
- **Core contribution**: Shows SFT and RL both collapse diversity of reasoning traces. SFT miscalibrates toward oversampling a common response; RL fails to restore diversity.
- **Relation to us**: **Tangential**. Diversity collapse in reasoning is a different phenomenon from recursive generation depth, but shares the theme of iterative degradation.

### [CONTEXT] Self-Consuming Generative Models Go MAD — Alemohammad et al. (ICLR 2024, updated 2025)
- **URL**: https://arxiv.org/abs/2307.01850
- **Core contribution**: Formalized autophagous loops and MAD (Model Autophagy Disorder). Without fresh real data, quality or diversity inevitably decreases.
- **Relation to us**: Already in scope. Foundation paper for our iterative generation setup.

---

## Thread 3: Verification-Based Data Curation / Collapse Mitigation

### [NEW] Machine-Generated Text Detection Prevents Language Model Collapse — Drayson, Yilmaz, Lampos
- **Venue**: EMNLP 2025
- **URL**: https://arxiv.org/abs/2502.15654
- **Core contribution**: Trains MGT detector and uses importance resampling to up-weight likely-human content in training data. Not only prevents collapse but **improves** performance beyond pure human data. Validated on GPT-2 and SmolLM2 (124M–1.7B).
- **Relation to us**: **Strongly complementary**. Directly connects MGT detection to collapse prevention. Our depth estimator could serve as a more granular version of their binary detector — instead of binary filtering, weight by estimated generation depth. **Must cite.**
- **Code**: https://github.com/GeorgeDrayson/model_collapse
- **NOTE**: Dream审稿 previously flagged "Drayson et al. (2025)" as a hallucinated citation. **It is real.** George Drayson, UCL, EMNLP 2025.

### [NEW] Escaping Model Collapse via Synthetic Data Verification — (2025)
- **Venue**: arXiv preprint (under review)
- **URL**: https://arxiv.org/abs/2510.16657
- **Core contribution**: Theoretical analysis showing verifier-guided retraining avoids collapse in the short term but converges to verifier's "knowledge center" long-term. Unless verifier is perfect, gains plateau. Validated on linear regression, VAEs (MNIST), SmolLM2-135M (XSUM).
- **Relation to us**: **Complementary**. Extends the Feng ICLR 2025 verification framework. Their "verifier imperfection → plateau" result connects to our K* concept — there's a depth beyond which even verification-based curation can't help.

### [NEW] Escaping Collapse: The Strength of Weak Data for Large Language Model Training — Amin et al.
- **Venue**: NeurIPS 2025
- **URL**: https://arxiv.org/abs/2502.08924
- **Core contribution**: Boosting-inspired framework showing that if ≥β>0 fraction of external responses are correct, iterative training converges. Dynamically focusing labeling on hardest examples improves performance.
- **Relation to us**: **Complementary**. Their "weak signal suffices" result suggests our depth estimator, even if imperfect, could serve as the weak signal for data curation in iterative training pipelines.

### [ALREADY CITED] Beyond Model Collapse: Scaling Up with Synthesized Data Requires Verification — Feng et al.
- **Venue**: ICLR 2025
- **URL**: https://arxiv.org/abs/2406.07515
- **Note**: Already in our related work (Thread 3).

### [NEW] Learning by Surprise: Surplexity for Mitigating Model Collapse — (2025)
- **Venue**: arXiv preprint (revised Sep 2025)
- **URL**: https://arxiv.org/abs/2410.12341
- **Core contribution**: Proposes "surplexity" — measures collapse via next-token probability distributions rather than text properties. Filters training items by surprise level, effective without knowing human/synthetic origin.
- **Relation to us**: **Complementary**. Surplexity could be an additional feature in our depth estimation pipeline. The key insight — collapse manifests as decreasing surprise — aligns with our observation that deeper generations have lower token-level entropy.

---

## Thread 4: Data Contamination Estimation

### [NEW] CoDeC: Detecting Data Contamination in LLMs via In-Context Learning — Zawalski et al.
- **Venue**: ICLR 2026
- **URL**: https://arxiv.org/abs/2510.27055
- **Core contribution**: Detects contamination by measuring how in-context examples affect model confidence. If ICL examples reduce confidence (disrupting memorization), the data was likely in training. Simple, model/dataset-agnostic, runs in minutes.
- **Relation to us**: **Complementary**. CoDeC detects binary contamination; our depth estimation is a finer-grained version of contamination measurement. Could use CoDeC as a sanity check in our pipeline.

### [NEW] Beyond Surface-Level Similarity: Hierarchical Contamination Detection for Synthetic Training Data — (2025)
- **Venue**: arXiv preprint (Nov 2025)
- **URL**: https://arxiv.org/abs/2511.17602
- **Core contribution**: Four-level contamination detection: token, semantic, reasoning pattern, performance cliff. Existing methods fail at semantic-level contamination (F1=0.17-0.49); hierarchical approach achieves F1=0.76.
- **Relation to us**: **Complementary**. Their multi-level framework is conceptually aligned with our multi-feature approach. The "reasoning pattern" contamination level is analogous to our "generation depth" concept — patterns that propagate through iterations.

### [SURVEY] A Survey on Data Contamination for Large Language Models — (2025)
- **URL**: https://arxiv.org/html/2502.14425v2
- **Core contribution**: Reviews 50+ detection techniques and 100+ papers. Notes that detection during SFT (vs pretraining) remains unsolved.
- **Relation to us**: **Context**. Confirms contamination detection is active area; our depth estimation adds a new dimension.

---

## Papers NOT Found / Verified as Non-existent

No additional hallucinated citations were detected in this scan. All papers listed above have verified URLs on arxiv.org, OpenReview, ACL Anthology, or conference proceedings.

---

## Actionable Recommendations for the Paper

### Must Cite (high relevance, strengthens positioning)
1. **Drayson et al. (EMNLP 2025)** — directly connects MGT detection to collapse prevention; our depth estimator is a natural generalization
2. **Schaeffer et al. (ICML 2025)** — "Model Collapse Does Not Mean What You Think" — forces us to be precise about definitions; we should clarify K* is about discriminability saturation, not test-loss collapse
3. **Kazdan & Schaeffer (ICML 2025)** — "Collapse or Thrive" — accumulate vs replace regimes affect K*
4. **He et al. (NeurIPS 2025)** — generalization→memorization transition parallels our feature convergence

### Should Cite (good context)
5. **DivEye (TMLR 2026)** — new zero-shot detection baseline; surprisal features may work for depth estimation
6. **Amin et al. (NeurIPS 2025)** — weak-signal curation; motivates practical utility of imperfect depth estimators
7. **CoDeC (ICLR 2026)** — state-of-art contamination detection; complementary to our approach
8. **Surplexity (2025)** — surprise-based collapse metric; potential feature for our pipeline

### New Baselines to Test in Full Study
- **DivEye features** (surprisal diversity statistics) as depth-discriminative features
- **Surplexity scores** as an alternative collapse indicator per generation depth

### Framing Adjustments
- Add a paragraph distinguishing our "discriminability saturation" (K*) from model collapse definitions per Schaeffer 2025
- Position Drayson 2025 as the closest work (binary filtering for collapse prevention) and explain how ordinal depth estimation generalizes it
- Discuss accumulate vs replace regimes (Kazdan 2025) as factors that may shift K*
