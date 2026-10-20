# PRISM: Probing the Decoupling of Loss and Collapse Signals in Iterative Synthetic Training

---

## 2. Related Work

### 2.1 Model Collapse in Iterative Training

Training generative models on their own outputs across successive generations leads to *model collapse*—a progressive loss of distributional fidelity that manifests as tail truncation and mode reduction. Shumailov et al. (2024) established this phenomenon across LLMs, VAEs, and GMMs, showing that distribution tails vanish first while bulk statistics remain superficially intact. Dohmatob et al. (2025) provided a theoretical grounding through the lens of the data processing inequality (DPI), proving that even trace amounts of synthetic contamination (as low as 1/1000) suffice to trigger collapse under iterative retraining, with degradation following an exponential decay in effective distributional support.

A critical design variable is whether synthetic data *replaces* or *accumulates* alongside real data across generations. Gerstgrasser et al. (2024) demonstrated that accumulation strategies can avoid collapse entirely, while replacement strategies—where each generation discards prior data—reliably induce it. Our experimental design deliberately adopts the replacement paradigm (fixed 50/50 real-synthetic ratio, re-generated each generation) to create conditions under which collapse is expected, enabling controlled study of its detection.

Schaeffer et al. (2025) drew attention to definitional ambiguity in the collapse literature, cataloguing eight distinct operationalizations. They argued that population-level risk (i.e., validation loss) can remain stable even as tail risk deteriorates—a conceptual precursor to the loss–signal decoupling we investigate. Yi et al. (2025) showed that external verifiers injecting fresh information can prevent collapse, suggesting that if collapse signals can serve as verification criteria, they may enable principled data filtering in iterative pipelines.

### 2.2 Data Mixing Strategies

Online data mixing methods dynamically adjust domain proportions during training to optimize learning efficiency. DoReMi (Xie et al., 2024) uses a small proxy model to reweight domain mixtures via distributionally robust optimization. AIOLI (Chen et al., 2024) extends this with online gradient-based updates to mixing coefficients. ODM (Fan et al., 2024) optimizes domain mixtures by tracking per-domain loss trajectories.

These methods share a common dependency: they use *loss* (or loss-derived gradients) as the sole signal for mixture adjustment. This is well-motivated when training data is static and well-characterized, but becomes problematic in iterative synthetic training where the data distribution itself degrades across generations. If collapse manifests in ways that loss fails to capture—a possibility suggested by the theoretical work reviewed above—then loss-driven mixing may be blind to distributional deterioration.

### 2.3 Collapse Detection Beyond Loss

Several lines of work have developed signals that capture aspects of model behavior orthogonal to loss.

**Entropy-based monitoring.** He et al. (2025) demonstrated a strong linear correlation between training data entropy and model generalization capacity, observing that entropy decline drives a generalization-to-memorization transition during iterative training. Truong & Truong (2025) formalized entropy collapse as a first-order phase transition, arguing that collapsed systems can maintain stable local performance (i.e., loss) while the effective dimensionality of their adaptive behavior has already contracted. This theoretical prediction—that loss stability can coexist with entropy collapse—directly motivates our empirical investigation, but neither work validated the claim in LLM iterative training.

**Spectral methods.** Gu et al. (2026) proposed SIGMA, which tracks collapse via the eigenspectrum of embedding Gram matrices, providing scalable one-sided monitoring bounds that serve as early warnings for representation space contraction. Qiu et al. (2025) introduced Spectral Alignment (SA), showing that spectral distributional shifts in weight matrices precede loss explosions by a detectable margin, implying a temporal lag between spectral degradation and loss response. Both works establish spectral signals as informative collapse indicators but neither examines how their correlation with loss evolves across generations.

**Diversity metrics.** Zhu et al. (2025) systematically compared diversity measures for synthetic data—including n-gram distinctness, self-BLEU, and the proposed DCScore—finding that classification-based diversity metrics correlate most strongly with human judgments. We adopt distinct-n (n=1,2,3) as a lightweight, interpretable generation-diversity signal alongside our representation-level metrics.

**Gap in the literature.** Existing work has (a) theoretically predicted that collapse can occur without loss degradation (Truong & Truong, 2025; Schaeffer et al., 2025), (b) shown that entropy tracks generalization within a single generation (He et al., 2025), and (c) developed spectral monitoring tools that detect collapse independently of loss (Gu et al., 2026; Qiu et al., 2025). However, no prior work has quantified how the *correlation* between loss and these collapse signals evolves across iterative training generations. We address this gap by tracking Spearman rank correlation ρ(loss, signal) across multiple generations, testing whether signals that are initially coupled to loss become progressively decoupled as collapse advances.

---

## 3. Method

### 3.1 Iterative Synthetic Training Setup

**Model.** We use Pythia-410M-deduped (Biderman et al., 2023), a decoder-only transformer with 410M parameters pretrained on the Pile (deduplicated). This model is small enough to permit rapid multi-generation iteration on 2× RTX 6000 GPUs while being large enough to exhibit nontrivial language modeling behavior and collapse dynamics. The deduplication ensures our baseline is not already compromised by near-duplicate memorization artifacts.

**Real data.** We sample a fixed subset from FineWeb (Penedo et al., 2024), a curated web corpus. Each training generation uses the same real-data pool to isolate the effect of synthetic data degradation across generations.

**Synthetic data generation.** At each generation $g$, the model $M_g$ generates synthetic text via nucleus sampling (top-p = 0.9, temperature = 1.0) starting from the BOS token (unconditional generation) to match the token count of the real data portion. Each sample generates up to 256 new tokens. Each generation produces fresh synthetic data; prior generations' synthetic outputs are discarded (replacement paradigm).

**Training configuration.** Each generation trains for approximately 200M tokens with a 50/50 real-synthetic mixing ratio (by token count). We use AdamW (β₁=0.9, β₂=0.999, weight decay 0.01) with a cosine learning rate schedule (peak lr = 1e-5, warmup over the first 2% of steps). Batch size is 32 sequences of 1024 tokens. Training resumes from the previous generation's final checkpoint, simulating the iterative retraining scenario studied in the collapse literature (Shumailov et al., 2024; Gerstgrasser et al., 2024).

**Iterative protocol.** Starting from the pretrained Pythia-410M checkpoint (Gen 0 baseline), we execute three generations of iterative training:
- **Gen 0→1:** Train on 50% FineWeb + 50% synthetic from the pretrained Pythia-410M.
- **Gen 1→2:** Train on 50% FineWeb + 50% synthetic from the Gen 1 model.
- **Gen 2→3:** Train on 50% FineWeb + 50% synthetic from the Gen 2 model.

Each generation produces a model checkpoint and a corresponding set of collapse signal measurements on a fixed probe set.

**Reproducibility.** We run the full pipeline with two independent random seeds (42 and 137), controlling for initialization noise in both synthetic data generation and training stochasticity. Both seeds share the same real data subset and probe set.

### 3.2 Collapse Signal Definitions

We define four collapse signals spanning three levels of granularity: token-level, representation-level, and generation-level. All signals are computed on a fixed **probe set** of 5,000 sequences (256 tokens each) sampled from the FineWeb validation split, with no overlap with the training data.

#### 3.2.1 Per-Example Output Entropy

For each probe sequence $x = (x_1, \ldots, x_T)$, we compute the mean next-token prediction entropy:

$$H(x) = -\frac{1}{T} \sum_{t=1}^{T} \sum_{v \in \mathcal{V}} p_\theta(v \mid x_{<t}) \log p_\theta(v \mid x_{<t})$$

where $\mathcal{V}$ is the vocabulary and $p_\theta$ is the model's softmax distribution. Output entropy measures the uncertainty of the model's predictions; collapse concentrates probability mass on fewer tokens, reducing $H$. This yields one scalar per probe example, enabling per-example correlation with loss.

#### 3.2.2 Per-Example Spectral Effective Rank

For each probe sequence $x$, let $\mathbf{H}_x \in \mathbb{R}^{T \times d}$ be the matrix of last-layer hidden states across all $T$ positions. The spectral effective rank (Roy & Vetterli, 2007) is:

$$\text{erank}(\mathbf{H}_x) = \exp\left( -\sum_{i=1}^{\min(T,d)} \hat{\sigma}_i \log \hat{\sigma}_i \right)$$

where $\hat{\sigma}_i = \sigma_i / \sum_j \sigma_j$ are the normalized singular values of $\mathbf{H}_x$. Effective rank captures the dimensionality of the representation manifold: collapse reduces the number of directions the model actively uses, concentrating variance into fewer singular values. This yields one scalar per probe example.

#### 3.2.3 Distinct-n

For a set of generated continuations (all probe-set sequences, each continued for 128 new tokens from 64-token prefixes using the same sampling parameters as training synthetic data), we compute:

$$\text{distinct-}n = \frac{|\text{unique } n\text{-grams}|}{|\text{total } n\text{-grams}|}$$

for $n \in \{1, 2, 3\}$. Distinct-n directly measures lexical diversity of model outputs; collapse produces repetitive text with declining distinct-n. This is a corpus-level metric (one scalar per generation) and thus contributes to trend analysis rather than per-example correlation.

#### 3.2.4 Corpus-Level Spectral Rank

For each probe sequence, we mean-pool its last-layer hidden states across token positions into a single $d$-dimensional vector, yielding a matrix $\mathbf{H}_{\text{corpus}} \in \mathbb{R}^{5000 \times d}$. We form the Gram matrix $\mathbf{G} = \mathbf{H}_{\text{corpus}}^\top \mathbf{H}_{\text{corpus}} \in \mathbb{R}^{d \times d}$ and compute its spectral effective rank:

$$\text{erank}(\mathbf{G}) = \exp\left( -\sum_{i=1}^{d} \hat{\lambda}_i \log \hat{\lambda}_i \right)$$

where $\lambda_i$ are the eigenvalues of $\mathbf{G}$ (obtained via SVD; since $\mathbf{G}$ is positive semi-definite, its singular values equal its eigenvalues) and $\hat{\lambda}_i = \lambda_i / \sum_j \lambda_j$ are their normalized values. This differs from the per-example effective rank (§3.2.2) in two respects: (1) the input is an inter-example Gram matrix constructed from mean-pooled representations, rather than the intra-sequence hidden-state matrix of a single example; and (2) the effective rank operates on eigenvalues $\lambda_i$ of $\mathbf{G}$ (equivalently, the squared singular values $\sigma_i^2$ of $\mathbf{H}_{\text{corpus}}$), not on singular values directly. This captures global representation diversity across the probe set. Following Gu et al. (2026), we compute this on the last transformer layer. This is a corpus-level scalar (one per generation).

### 3.3 Statistical Methods

Our central analysis quantifies how the relationship between loss and each collapse signal evolves across generations.

**Primary metric: Spearman rank correlation.** For each generation $g$ and each per-example signal $s \in \{\text{entropy}, \text{spectral effective rank}\}$, we compute the Spearman rank correlation $\rho_g$ between per-example loss $\ell(x)$ and signal value $s(x)$ across the 5,000 probe examples. Spearman correlation is chosen over Pearson because it captures monotonic relationships without assuming linearity, and is robust to outliers in either loss or signal distributions.

**Confidence intervals.** We construct 95% bootstrap confidence intervals for each $\rho_g$ by resampling the 5,000 probe examples with replacement (1,000 bootstrap iterations). This provides uncertainty estimates that account for probe-set heterogeneity without distributional assumptions.

**Effect size.** To quantify the magnitude of decoupling, we report $\Delta\rho = \rho_0 - \rho_g$ (the drop in correlation from baseline) and normalize by bootstrap standard error: $\text{effect size} = \Delta\rho / \text{SE}_{\text{bootstrap}}$. This enables comparison across signals with different baseline correlation strengths.

**Trend significance.** To assess whether the observed $\rho$ decline constitutes a statistically reliable trend rather than noise, we employ a permutation test: we randomly shuffle the generation labels (0, 1, 2, 3) 10,000 times and compute the Spearman correlation of $\rho$ values with generation index under each permutation. The p-value is the fraction of permuted slopes as steep or steeper than the observed slope.

**Signal degradation.** For each collapse signal, we report the mean value per generation and test for monotonic decline. Degradation magnitude is quantified as the relative change from Gen 0 to the final generation: $\Delta_{\text{rel}} = (s_0 - s_G) / s_0$.

### 3.4 Pre-registered Pass/Fail Criteria

We pre-register three conditions that must all be satisfied for the hypothesis to pass:

**C1 (Decoupling).** At least one collapse signal exhibits $|\rho_g|$ with loss dropping from $> 0.7$ at Gen 0–1 to $< 0.5$ at Gen 3. This threshold ensures that the signal begins meaningfully coupled to loss (sharing >49% of rank variance) and ends meaningfully decoupled (sharing <25%).

**C2 (Signal degradation).** The same signal's mean value monotonically degrades across generations (each generation lower than the previous), with a cumulative decline of $\geq 15\%$ from Gen 0 to Gen 3. This condition ensures that decoupling is driven by genuine collapse (the signal detects worsening behavior) rather than mere noise inflation that could artificially reduce $\rho$.

**C3 (Reproducibility).** C1 and C2 are both observed under both random seeds (42 and 137). Single-seed results cannot distinguish systematic phenomena from run-specific artifacts.

**Contingency.** If the pattern emerges in one seed but not the other (weak pass), we run a third seed (7) as a tiebreaker. If all three conditions fail outright, we conclude that three generations are insufficient to observe decoupling at this model scale and either extend to five generations or reassess the hypothesis.

---

## References

- Biderman, S., Schoelkopf, H., Anthony, Q., et al. (2023). Pythia: A suite for analyzing large language models across training and scaling. *ICML 2023*.
- Chen, M., et al. (2024). AIOLI: Online data mixing via gradient-based optimization. *arXiv*.
- Dohmatob, E., Feng, Y., Yang, P., Charton, F., & Kempe, J. (2025). Strong model collapse. *ICLR 2025 (Spotlight)*.
- Fan, Y., et al. (2024). Online data mixing for language model pre-training. *arXiv*.
- Gerstgrasser, M., Schaeffer, R., Dey, A., Rafailov, R., et al. (2024). Is model collapse inevitable? Breaking the curse of recursion by accumulating real and synthetic data. *COLM 2024*.
- Gu, Y., et al. (2026). SIGMA: Scalable spectral insights for LLM model collapse. *arXiv*.
- He, S., et al. (2025). A closer look at model collapse: From a generalization-to-memorization perspective. *NeurIPS 2025 (Spotlight)*.
- Penedo, G., et al. (2024). The FineWeb datasets: Decanting the web for the finest text data at scale. *arXiv*.
- Qiu, H., Wu, Y., Tan, Y., Wang, Y., & Yao, Q. (2025). Spectral alignment as predictor of loss explosion in neural network training. *arXiv*.
- Roy, O. & Vetterli, M. (2007). The effective rank: A measure of effective dimensionality. *European Signal Processing Conference*.
- Schaeffer, R., Kazdan, J., Arulandu, A. C., & Koyejo, S. (2025). Position: Model collapse does not mean what you think. *arXiv (NeurIPS 2025 Position Track)*.
- Shumailov, I., Shumaylov, Z., Zhao, Y., Papernot, N., Anderson, R., & Gal, Y. (2024). AI models collapse when trained on recursively generated data. *Nature*.
- Truong, X. K. & Truong, Q. H. (2025). Entropy collapse: A universal failure mode of intelligent systems. *arXiv*.
- Xie, S. M., et al. (2024). DoReMi: Optimizing data mixtures speeds up language model pretraining. *NeurIPS 2024*.
- Yi, B., Liu, Q., Cheng, Y., & Xu, H. (2025). Escaping model collapse via synthetic data verification. *ICML 2025*.
- Zhu, Y., Zhang, H., Wu, B., et al. (2025). Measuring diversity in synthetic datasets. *ICML 2025*.
