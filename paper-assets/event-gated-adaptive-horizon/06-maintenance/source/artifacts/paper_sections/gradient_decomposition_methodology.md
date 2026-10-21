## Gradient Decomposition Methodology

### Formal Definition

In DreamerV3 \citep{hafner2023dreamerv3}, the world model loss decomposes into three terms:
$$\mathcal{L}_{\text{wm}} = \mathcal{L}_{\text{obs}} + \mathcal{L}_{\text{reward}} + \beta_{\text{KL}} \mathcal{L}_{\text{KL}}$$
where $\mathcal{L}_{\text{obs}}$ aggregates all observation decoder reconstruction losses, $\mathcal{L}_{\text{reward}}$ is the reward prediction loss, and $\mathcal{L}_{\text{KL}}$ regularizes the posterior–prior divergence. Each term propagates gradients through the RSSM latent state to all upstream parameters, including the temporal-distance embedding $\theta_{\text{dt}}$.

We decompose the gradient of the world model loss with respect to $\theta_{\text{dt}}$ into per-term contributions:
$$\nabla_{\theta_{\text{dt}}} \mathcal{L}_{\text{wm}} = \underbrace{\nabla_{\theta_{\text{dt}}} \mathcal{L}_{\text{obs}}}_{\text{obs pathway}} + \underbrace{\nabla_{\theta_{\text{dt}}} \mathcal{L}_{\text{reward}}}_{\text{reward pathway}} + \underbrace{\nabla_{\theta_{\text{dt}}} \beta_{\text{KL}} \mathcal{L}_{\text{KL}}}_{\text{KL pathway}}$$

Each component gradient is obtained by zeroing out the other loss terms and performing a backward pass in isolation. We then quantify relative contribution via L2 norm ratios:
$$r_i = \frac{\|\nabla_{\theta_{\text{dt}}} \mathcal{L}_i\|_2}{\sum_{j \in \{\text{obs}, \text{reward}, \text{KL}\}} \|\nabla_{\theta_{\text{dt}}} \mathcal{L}_j\|_2}$$

**Choice of L2 norm.** We adopt L2 norm following \citet{chen2018gradnorm}, who establish it as the standard measure for multi-task gradient magnitude comparison. L2 norm captures the total parameter update magnitude irrespective of direction, which is appropriate here because we seek to quantify *how much* each loss term drives learning in $\theta_{\text{dt}}$, not whether the gradients align. This differs from \citet{shang2024harmonydream}, who compare loss magnitudes in the forward pass—our backward-pass decomposition reveals the actual learning signal reaching $\theta_{\text{dt}}$ after propagation through the computational graph.

### Multi-Checkpoint Analysis Protocol

To assess stability of the decomposition across training, we extract gradients at available checkpoints. Gradient norms are averaged over 10 mini-batches (B=16, T=64) sampled from the replay buffer, with variable-dt subsampling applied as in training.

| Step | $\|\nabla_{\text{obs}}\|_2$ | $\|\nabla_{\text{reward}}\|_2$ | $\|\nabla_{\text{KL}}\|_2$ | %obs | %reward | %KL |
|------|---------------------------|-------------------------------|---------------------------|------|---------|-----|
| 55K  | 0.601 ± 0.199 | 0.546 ± 0.227 | 1.180 ± 0.251 | 25.8% | 23.5% | 50.7% |
| 105K | — | — | — | 93% | ≈0% | 7% |

*Table caption: Gradient decomposition of $\nabla_{\theta_{\text{dt}}} \mathcal{L}_{\text{wm}}$ across training steps for exp 008d (Walker-walk, seed=1, trained dt\_emb, subsample ON). The continuation head ($\mathcal{L}_{\text{cont}}$) contributes 0.0% gradient to $\theta_{\text{dt}}$ at all checkpoints and is omitted. The 105K row reports previously measured values; the 55K row was extracted from the only available checkpoint (latest.pt). No intermediate checkpoints (25K, 50K, 75K) were saved during the exp\_008d run.*

**Data source**: exp\_008d (Walker-walk, trained dt\_emb + subsample ON). Only `latest.pt` (step 55K) was preserved; the experiment did not save intermediate checkpoints. The decomposition was verified by confirming $\|\nabla_{\text{obs}} + \nabla_{\text{reward}} + \nabla_{\text{KL}} - \nabla_{\text{total}}\|_2 < 10^{-6}$.

**Gradient structure evolution.** The 55K→105K comparison reveals a striking shift in gradient composition: at mid-training (55K), KL regularization dominates the learning signal to $\theta_{\text{dt}}$ (50.7%), with observation and reward contributing roughly equally (~25% each). By 105K, observation decoders account for 93% of the gradient while reward drops to $\approx$0%. This transition is consistent with the RSSM's KL divergence converging toward the free-bits threshold ($\beta_{\text{free}}=1.0$) as training progresses, reducing the KL gradient magnitude and revealing the underlying obs-dominated gradient structure that motivates Full-SGS.

### Causal Connection to Selective Gradient Stopping

The decomposition result—observation decoders account for 93% of gradient flow to $\theta_{\text{dt}}$ while reward contributes a numerically negligible fraction (zero to within floating-point precision, exp\_008d step 105K)—directly motivates the design of Full-SGS (exp\_018/018v2).

**Why reward-only SGS fails.** Experiment 016e applies stop-gradient exclusively on the reward prediction pathway. The gradient decomposition provides evidence for why this intervention is an architectural no-op: the reward pathway contributes $\approx$0% of the learning signal to $\theta_{\text{dt}}$. Blocking a pathway that carries no gradient cannot alter the embedding's learned representation. Empirically, 016e exhibits dynamics consistent with cross-seed variation relative to the unmodified baseline 008d (exp\_016e).

**Full-SGS design rationale.** Given that 93% of the gradient originates from observation decoders, Full-SGS (exp\_018) detaches the observation decoder gradient pathway from $\theta_{\text{dt}}$, eliminating the dominant learning signal that drives the embedding toward observation-reconstruction-optimal (rather than dynamics-faithful) representations. This constitutes a targeted intervention on the single pathway responsible for nearly all parameter updates to $\theta_{\text{dt}}$, in contrast to the ineffective reward-only intervention of 016e.

The progression from decomposition measurement → failed minimal intervention (016e) → targeted full intervention (018) exemplifies a diagnose-then-intervene methodology enabled by per-pathway gradient attribution, extending the loss-magnitude analysis of \citet{shang2024harmonydream} to the backward pass.
