# Literature Positioning Notes — gen-depth-contamination

> 4 篇 must-cite / framing-critical 论文的深度分析与 positioning。
> 可直接用于 Introduction 和 Related Work 撰写。

---

## 1. Drayson et al. (EMNLP 2025) — "Machine-generated text detection prevents language model collapse"

**Role: direct-competitor**

### Method & Core Findings

Drayson et al. train a binary MGT detector (encoder-only transformer with classification head; best model: ModernBERT-150M, AUC .986 in-distribution) to distinguish human vs. machine-generated text, then apply Sampling Importance Resampling (SIR) to upweight human-attributed samples during training. The resampling weight is:

$$w_j = \frac{(1 - q(x_j))^b}{\sum_l (1 - q(x_l))^b}$$

where $q(x)$ is the detector's estimated probability of being machine-generated, and $b \geq 1$ is a bias term correcting for the detector's skew. They resample at rate $k=1.5$ (50% upsampling). Evaluated on GPT-2 and SmolLM2 families (124M–1.7B), the method not only prevents model collapse but improves over training on purely human data (perplexity −0.85% to −25.65%, diversity +3.44% to +14.62%, MAUVE +8.46% to +20.92%).

### Limitations

- Only evaluates fine-tuning, not pretraining from scratch.
- Models ≤2B parameters; unclear if results transfer to larger scales.
- Exclusively binary classification; no discussion of ordinal depth or multi-class generational estimation.
- Open-ended generation only; may not generalize to structured tasks.

### Relationship to Our Work

**Overlaps:** Both use MGT detection for data curation in iterative training loops. Both frame the problem as "detection enables quality-aware data selection."

**Key difference:** Drayson et al. treat synthetic text as a monolithic category (binary: human vs. synthetic). We argue that recursive generation creates a *depth spectrum*—gen-1 text is qualitatively different from gen-4 text—and estimate ordinal depth rather than binary label. Our K* operationalizes *when* this ordinal signal matters: below K*, depth-graduated filtering adds value over binary; above K*, generations are indistinguishable and binary suffices.

**How we cite them:** As the closest prior work and the starting point we generalize. Their SIR framework is a special case of our graduated filtering when K*=1 (i.e., only distinguishing human from all synthetic). We frame our contribution as the binary→ordinal extension: "Drayson et al. (2025) demonstrate that binary MGT detection combined with importance resampling prevents model collapse. We extend this to ordinal depth estimation and show that even a coarse 3-class signal (human/gen-1/gen-2+) yields improved calibration over binary filtering at decision boundaries."

### Related Work Draft

> Drayson et al. (2025) pioneer the use of binary MGT detection for collapse prevention, training an encoder-only classifier to separate human from machine-generated text and applying importance resampling to upweight human-attributed samples during training. Their method demonstrably prevents collapse and even improves over human-only baselines on models up to 1.7B parameters. However, their binary framing treats all synthetic text uniformly, discarding the information encoded in generational depth. We generalize their approach from binary detection to ordinal depth estimation: where they assign weight $w \propto (1-q)^b$ based on a binary human probability, we estimate generational depth $d \in \{0, 1, \ldots, K^*\}$ and apply depth-graduated filtering that exploits the quality gradient across recursive generations.

---

## 2. Schaeffer et al. (ICML 2025) — "Position: Model Collapse Does Not Mean What You Think"

**Role: framing-critical**

### Core Argument & Taxonomy

Schaeffer et al. identify that "model collapse" is used inconsistently across the literature, encompassing eight distinct and sometimes conflicting definitions. They organize these into three families:

**Family A — Population Risk Degrading:**
- **D1: Catastrophic increase of population risk** — rapid, severe performance degradation from synthetic data.
- **D2: Any increase of population risk** — strict: any performance decrease vs. training on real data alone.
- **D3: Asymptotically diverging population risk** — unbounded risk growth across iterations (fundamentally unstable dynamics).

**Family B — Distributions Deforming:**
- **D4: Collapsing variance** — diversity → 0, distributions → delta functions over successive iterations.
- **D5: Change in scaling law** — synthetic data alters the performance–data-size relationship.
- **D6: Disappearance of or entanglement of modes** — synthetic data prevents learning specific distribution modes or causes mode blurring.
- **D7: Disappearance of real tail data** — underrepresentation of rare/minority data ("coverage collapse").

**Family C — Spurious Generation:**
- **D8: Appearance of hallucinated data** — model produces sequences unsupported by the original distribution.

Their main argument: prominent collapse scenarios are "readily avoidable" under realistic conditions (data accumulation, increasing compute). The real harms—tail data loss (D7) and mode entanglement (D6)—have received disproportionately less attention.

### Relationship to Our Work

**Our K* in their taxonomy:** K* (discriminability saturation) belongs squarely to Family B (distributions deforming). Specifically, K* measures when recursive generation causes sufficient distribution deformation (D4: variance collapse + D6: mode entanglement) that successive generations become statistically indistinguishable in feature space. K* is *not* about population risk increase (Family A)—a model trained on gen-2 text might perform fine on downstream tasks, yet gen-2 and gen-3 text are already indistinguishable.

**How we cite them:** To precisely position K* within the collapse discourse. We adopt their taxonomy to clarify that our contribution addresses distribution deformation (Family B), not population risk degradation (Family A): "Following the taxonomy of Schaeffer et al. (2025), our K* measures the discriminability saturation boundary—the generational depth beyond which distribution deformation (Definitions 4, 6) renders successive generations indistinguishable in feature space. This is orthogonal to population risk collapse (Definitions 1–3), which may or may not accompany loss of discriminability."

### Related Work Draft

> The model collapse literature suffers from terminological inconsistency. Schaeffer et al. (2025) identify eight distinct definitions spanning three families: population risk degradation, distribution deformation, and spurious generation. They argue that under realistic conditions—where data accumulates and compute grows—catastrophic risk divergence (Definitions 1–3) is avoidable, but distribution-level harms such as tail data loss and mode entanglement (Definitions 6–7) remain concerning. Our work operationalizes the distribution deformation family: K* measures the generational depth at which feature-space divergence saturates, providing a concrete, measurable boundary for when successive generations become indistinguishable. This positions depth estimation as a diagnostic tool for exactly the harms Schaeffer et al. identify as underexplored.

---

## 3. Kazdan et al. (ICML 2025) — "Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World"

**Role: background**

### Method & Core Findings

Kazdan et al. formally compare three data regimes for iterative training:

1. **Replace:** Each generation trains exclusively on synthetic data from the previous model. All prior data discarded. Formally, $\hat{\mu}^{(t+1)} = \frac{1}{n}\sum X_j^{(t)}$. Result: covariance collapses to zero ($\hat{\Sigma} \to 0$ a.s.), Wasserstein-2 diverges. Collapse is inevitable.

2. **Accumulate:** Each generation trains on *all* historical data (real + all previous synthetic). Dataset grows linearly; real data fraction → 0. Result: covariance stabilizes at $\sigma_0^2 \cdot \sin(\pi/\sqrt{n}) / (\pi/\sqrt{n})$. No collapse.

3. **Accumulate-subsample:** Data accumulates but each iteration uses a fixed-size subsample. Result: degradation plateaus rather than diverges—intermediate between replace and accumulate.

Validated on multivariate Gaussians, kernel density estimation, and LLM fine-tuning (Gemma2-2B on HelpSteer2/TinyStories). Key finding: in the accumulate regime, the *cardinality* of real data matters more than its *proportion* ($R^2=0.59$ vs $0.34$).

### Limitations

- Replace regime collapses within 5–10 iterations in all settings, but precise timescales depend on model/data specifics.
- LLM experiments limited to SFT on 2B models.
- No detection or mitigation method proposed—purely diagnostic.

### Relationship to Our Work

**Our experimental design = replace regime.** Our prompt-chain pipeline generates each subsequent generation from the previous model's output exclusively, without mixing real data. This is the harshest setting per Kazdan et al.'s analysis—covariance collapse is guaranteed, and K* is measured under this maximally adversarial condition.

**Implication for K*:** Our measured K*=2 is a *lower bound* on what would be observed under the more realistic accumulate regime, where distributional stability persists longer. This strengthens our result: if depth estimation already provides value at K*=2 in the replace regime, it can only provide more value when K* shifts upward in accumulate settings.

**How we cite them:** To justify our experimental design and contextualize our K* measurement.

### Related Work Draft

> Kazdan et al. (2025) formalize three data regimes for iterative retraining: replace (complete substitution each generation), accumulate (growing corpus including all historical data), and accumulate-subsample (fixed training budget from accumulated pool). They prove that replace inevitably collapses (covariance → 0), while accumulate maintains stability even as real data fraction vanishes. Our prompt-chain experiments operate in the replace regime—the harshest setting—establishing K*=2 as a conservative lower bound; under the accumulate regime that better models real-world data aggregation, K* would likely shift upward, amplifying the value of depth-graduated curation.

---

## 4. He et al. (NeurIPS 2025 Spotlight) — "A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective"

**Role: background**

### Method & Core Findings

He et al. characterize model collapse as a generalization→memorization transition in iterative training on synthetic data (DDPM on CIFAR-10 subsets). They introduce:

- **Generalization Score (GS):** Average distance between each generated image and its nearest training image. GS drops approximately exponentially across iterations.
- **Entropy measurement:** Kozachenko-Leonenko estimator for differential entropy of training data. Strong linear correlation between training set entropy and log(GS) (Pearson $r=0.91$), establishing entropy as a direct predictor of generalization capability.

They propose entropy-based data selection: greedy selection maximizing nearest-neighbor distances, and threshold-decay filtering. Both preserve entropy and mitigate collapse.

Collapse timescales depend on dataset size: 1,024 images → memorization from iteration 1; 32,768 images → memorization after several iterations (5–10).

### Limitations

- **Diffusion models only.** No LLM experiments; they note "extension to the language modality" as future work.
- **No theoretical analysis** of why entropy collapses—they identify the correlation but not the causal mechanism ("finite dataset size, training and sampling errors, and the model bias could all contribute").
- FID as distributional metric; no JSD analysis.

### Relationship to Our Work

**Parallel phenomena, different modalities.** Their entropy decline across iterations directly parallels our observed JSD monotonic decrease (0.27→0.004) across 5 text generations. Their "generalization score drops exponentially" mirrors our finding that feature-space divergence between consecutive generations vanishes rapidly, leading to K*=2.

**Key distinction:** They measure collapse at the *output distribution* level (pixel-space entropy); we measure *discriminability* in feature space (can a classifier distinguish gen-$k$ from gen-$k+1$?). Our K* complements their entropy metric by providing an operational answer: "at what depth does the entropy decline make generations functionally indistinguishable?"

**Connection to feature convergence:** Their observation that generated images form "tight local clusters" while overall variance remains stable resonates with our finding that depth-discriminative features (vocabulary diversity, surprisal dynamics) converge before global distributional statistics do.

**How we cite them:** To ground our feature-space convergence observations in a broader phenomenon observed across modalities.

### Related Work Draft

> He et al. (2025) characterize model collapse as a generalization-to-memorization transition driven by entropy decline in iteratively retrained diffusion models, establishing a strong correlation ($r=0.91$) between training data entropy and generalization capability. While their work focuses on image generation, the phenomenon parallels our observations in the text domain: their exponentially declining generalization scores mirror our monotonically decreasing JSD across recursive text generations, and their observed clustering in feature space corresponds to the convergence of depth-discriminative linguistic features we measure. Our K* provides an operational complement to their entropy metric—quantifying the generational depth at which this convergence renders successive text generations indistinguishable to classifiers.

---

## Cross-Paper Synthesis: Positioning Summary

| Paper | Their Frame | Our Positioning | Citation Function |
|-------|------------|-----------------|-------------------|
| Drayson et al. | Binary MGT detection + SIR for collapse prevention | We generalize binary→ordinal; K* tells when ordinal adds value | Direct predecessor we extend |
| Schaeffer et al. | 8 definitions, 3 families; realistic conditions matter | K* = distribution deformation (Family B, D4+D6) discriminability measure | Taxonomic anchor for K* |
| Kazdan et al. | Replace collapses, accumulate stabilizes | Our replace-regime K*=2 is a conservative lower bound | Justifies experimental design |
| He et al. | Entropy decline → memorization (diffusion models) | Parallel phenomenon; K* operationalizes "when does entropy decline = indistinguishability?" | Cross-modal validation of convergence |

### Narrative Arc for Introduction

1. **Open** with the model collapse concern (cite Shumailov et al., Alemohammad et al. as foundational).
2. **Complicate** with Schaeffer et al.: "collapse" means many things; the real harm is distribution deformation, not necessarily risk divergence.
3. **Situate** with Kazdan et al.: under replace regime, collapse is inevitable; the question is *how fast* and *can we detect it?*
4. **Motivate depth estimation** via He et al.: entropy/distributional convergence happens over identifiable timescales.
5. **Present our gap** relative to Drayson et al.: binary detection helps, but ignores the depth gradient that carries actionable information.
6. **State contribution:** We formalize depth estimation, measure K*, and show graduated filtering improves on binary.

### Narrative Arc for Related Work

Structure into 3 subsections:
1. **Model Collapse: Definitions and Dynamics** — Schaeffer et al. (taxonomy) + Kazdan et al. (regimes) + Shumailov/Alemohammad/Dohmatob (foundational)
2. **Detecting and Mitigating Synthetic Data** — Drayson et al. (binary detection + SIR) + DivEye + Min-K%++ + watermarking
3. **Feature-Space Characterization of Iterative Degradation** — He et al. (entropy/memorization) + our JSD analysis
