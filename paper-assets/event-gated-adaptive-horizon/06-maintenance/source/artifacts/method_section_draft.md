# 3. Method

We build on DreamerV3 \citep{hafner2023dreamerv3}, a model-based reinforcement learning agent that learns a world model in a recurrent latent space (RSSM) and optimizes a policy purely through imagined rollouts. Our key contribution is an **event gate** that selects a per-step temporal stride $\Delta t \in \{1, \dots, K\}$, enabling variable-rate imagination. When the latent state changes slowly, the gate skips multiple environment steps in a single model transition; when the state changes rapidly, it falls back to single-step updates. This extends the effective planning horizon without a proportional increase in computation. We describe the five components of our approach below.

## 3.1 Variable-Rate RSSM

The standard RSSM in DreamerV3 maintains a deterministic recurrent state $h_t$ and a stochastic state $z_t$, updated at every environment step via a GRU cell:

$$h_t = \text{GRU}(h_{t-1}, [z_{t-1}; a_{t-1}]).$$

We extend this transition to accept a temporal stride $\Delta t \in \{1, \dots, K\}$ that specifies how many environment steps the model traverses in a single recurrence. To inform the GRU of the stride magnitude, we introduce a learned embedding $e: \{1, \dots, K\} \to \mathbb{R}^{d_e}$ via a lookup table $\mathbf{E} \in \mathbb{R}^{K \times d_e}$ (we use $K{=}8$, $d_e{=}32$). The modified transition becomes:

$$h_t = \text{GRU}\!\left(h_{t-1},\; [z_{t-1};\; a_{t-1};\; e(\Delta t)]\right).$$

The GRU input is first projected through a linear layer followed by LayerNorm and SiLU activation before entering the recurrent cell, which absorbs the scale difference introduced by the additional embedding dimension. The stochastic state $z_t$ is then sampled from a categorical distribution (with uniform mixture) parameterized by an MLP applied to $h_t$, exactly as in DreamerV3.

When $\Delta t = 1$, the model reduces to the standard RSSM. The embedding weights are initialized near zero ($\sigma = 0.01$) so that the initial model behavior is nearly identical to vanilla DreamerV3, ensuring stable early training.

**Training with variable strides.** To teach the RSSM to predict across different temporal strides, we sub-sample replay trajectories at variable $\Delta t$ during training (Section 3.4). Each sub-sampled trajectory carries per-step $\Delta t$ labels that are passed through the observation loop to the GRU, allowing the model to learn stride-conditioned dynamics.

## 3.2 Event Gate

The event gate is a lightweight MLP that examines the current latent state and decides the temporal stride for the next imagination step.

**Architecture.** The gate takes as input the feature vector $f_t = [z_t; h_t] \in \mathbb{R}^{d_f}$ (where $d_f = d_z \cdot C + d_h$; for DreamerV3's default configuration, $d_f = 32 \times 32 + 512 = 1536$). It consists of two hidden layers of 256 units each, with LayerNorm and SiLU activations, followed by a linear projection to $K$ logits:

$$\ell_t = W_2\,\text{SiLU}\!\left(\text{LN}(W_1\,f_t)\right) \in \mathbb{R}^K.$$

The output distribution over strides is obtained via Gumbel-Softmax:

$$\Delta t \sim \text{Gumbel-Softmax}(\ell_t, \tau),$$

which provides differentiable sampling during training while producing hard (argmax) decisions during imagination. The temperature $\tau$ is linearly annealed from $\tau_0 = 5.0$ to $\tau_{\min} = 0.5$ over 200K training steps, transitioning from near-uniform exploration to confident stride selection.

**Latent-state delta supervision.** Rather than relying solely on task reward to shape the gate, we provide a direct supervision signal derived from the rate of change in latent space. Let $\delta_t = \|f_t - f_{t-1}\|_2$ be the L2 distance between consecutive feature vectors (with stop-gradient on both $f_t$ and $f_{t-1}$). We normalize $\delta_t$ to $[0, 1]$ within each batch via min-max scaling and compute a preferred stride:

$$\Delta t^* = 1 + (K - 1)(1 - \bar{\delta}_t),$$

where $\bar{\delta}_t$ is the normalized delta. Large state changes ($\bar{\delta}_t \to 1$) yield $\Delta t^* \to 1$ (fine resolution); small changes ($\bar{\delta}_t \to 0$) yield $\Delta t^* \to K$ (skip ahead). The supervision target is a soft categorical distribution formed by a Gaussian kernel centered at $\Delta t^*$:

$$q_t(k) \propto \exp\!\left(-\frac{(k - \Delta t^*)^2}{2\sigma^2}\right), \quad k = 1, \dots, K,$$

with $\sigma = 1.0$. The gate supervision loss is the cross-entropy between the gate's predicted distribution and this soft target:

$$\mathcal{L}_{\text{gate}} = -\sum_{k=1}^{K} q_t(k) \log p_{\theta}(k \mid f_t),$$

where $p_{\theta}(k \mid f_t) = \text{softmax}(\ell_t)_k$. Crucially, the gate loss does not backpropagate into the RSSM: the input features are detached, so the gate learns to *read* the latent dynamics rather than *shape* them.

## 3.3 Adapted $\lambda$-Returns

DreamerV3 computes $\lambda$-returns over imagined trajectories with a fixed per-step discount $\gamma$. With variable-rate imagination, each step spans $\Delta t$ environment steps, requiring adaptations to both the reward aggregation and the discount factor.

**Cumulative discounted reward.** When sub-sampling a replay trajectory at stride $\Delta t$, we pre-compute the cumulative discounted reward for each gap:

$$r_t^{\text{cum}} = \sum_{k=0}^{\Delta t - 1} \gamma^k\, r_{t+k}.$$

The reward head is trained to predict $r_t^{\text{cum}}$ directly (the sub-sampled training data replaces per-step rewards with their cumulative-discounted aggregates), so no approximation is needed at imagination time.

**Minimum continuation.** For the continuation signal across a gap, we take the conservative estimate:

$$c_t^{\min} = \min_{k=0,\dots,\Delta t - 1} c_{t+k},$$

so that if any frame within the gap is terminal, the entire interval is marked as terminal.

**Variable-stride $\lambda$-return.** The adapted $\lambda$-return replaces the fixed discount $\gamma$ with $\gamma^{\Delta t}$:

$$V_t^{\lambda} = r_t^{\text{cum}} + \gamma^{\Delta t}\!\left[(1 - \lambda)\,V(s_{t+\Delta t}) + \lambda\, V_{t+\Delta t}^{\lambda}\right],$$

with the recursion terminating at the bootstrap value $V(s_H)$. This is computed via the same backward scan as the standard $\lambda$-return, but with per-step adjusted discount $(\gamma \cdot c_t)^{\Delta t}$ in place of $\gamma \cdot c_t$. When $\Delta t = 1$ for all steps, this expression reduces exactly to the standard DreamerV3 $\lambda$-return.

**Importance weights.** The per-step weights used for the actor and value losses are similarly adjusted:

$$w_t = \prod_{i=0}^{t-1} (\gamma \cdot c_i)^{\Delta t_i},$$

so that steps further in effective time receive appropriately decayed weight.

## 3.4 Gate Collapse Prevention

A central failure mode is *gate collapse*, where the gate converges to a constant stride (typically $\Delta t = 1$ or $\Delta t = K$), eliminating the adaptive benefit. We employ three complementary countermeasures.

**Entropy regularization.** We add an entropy bonus to the gate loss:

$$\mathcal{L}_{\text{total}} = \lambda_g\,\mathcal{L}_{\text{gate}} - \lambda_H\,\mathcal{H}[p_\theta(\cdot \mid f_t)],$$

where $\mathcal{H}$ is the categorical entropy of the gate distribution and $\lambda_H$ is annealed from 0.1 to 0.01 over 200K steps. The high initial $\lambda_H$ prevents the gate from committing to a narrow $\Delta t$ range before the RSSM has learned good multi-stride dynamics.

**Three-phase curriculum.** We introduce the gate gradually:

| Phase | Steps | Behavior |
|-------|-------|----------|
| 1 | $0$--$50\text{K}$ | Gate frozen ($\Delta t \equiv 1$); gate loss weight $= 0$ |
| 2 | $50\text{K}$--$150\text{K}$ | Gate loss linearly ramped from 0 to 1; gate active in imagination |
| 3 | $> 150\text{K}$ | Full gating; gate scale $= 1.0$ |

Phase 1 allows the RSSM to first learn stable single-step dynamics identical to standard DreamerV3. Phase 2 gradually introduces multi-stride predictions, giving the RSSM time to adapt. Phase 3 permits unconstrained gate optimization.

Formally, the gate scale factor is:

$$\alpha(s) = \begin{cases} 0 & s < s_1 \\ (s - s_1) / (s_2 - s_1) & s_1 \leq s < s_2 \\ 1 & s \geq s_2 \end{cases}$$

where $s$ is the training step, $s_1 = 50\text{K}$, and $s_2 = 150\text{K}$.

**Synchronized sub-sampling curriculum.** A naive implementation applies full variable-$\Delta t$ sub-sampling from step 0, forcing the RSSM to train on multi-stride data while imagination only uses $\Delta t = 1$ during Phase 1. This train--imagination mismatch degrades performance. We resolve it by tying the sub-sampling range to the curriculum schedule:

$$\Delta t_{\max}^{\text{eff}} = 1 + \alpha(s) \cdot (K - 1).$$

During Phase 1, $\Delta t_{\max}^{\text{eff}} = 1$ and the training data is identical to vanilla DreamerV3 (no sub-sampling). During Phase 2, the maximum stride ramps linearly from 1 to $K$, synchronizing the distribution of $\Delta t$ in training data with the gate's expanding range in imagination. During Phase 3, the full log-uniform distribution over $\{1, \dots, K\}$ is used.

## 3.5 Comparison with Related Approaches

Our method occupies a distinct point in the design space of temporal abstraction for model-based RL. We highlight the key differences with the most closely related approaches.

**THICK** \citep{romac2024thick} decomposes planning into a hierarchy of coarse sub-goals and fine-grained actions, with a fixed sub-goal horizon. In contrast, our approach operates within a single-level RSSM and learns a *per-step* temporal stride, avoiding the complexity of hierarchical world models while still achieving variable temporal resolution.

**TAWM** \citep{freed2024tawm} introduces time-aware world models that condition on a fixed or scheduled $\Delta t$ to predict future states. Our event gate makes $\Delta t$ *state-dependent*---the stride is chosen dynamically based on the current latent state rather than being fixed or globally scheduled, enabling the model to allocate temporal resolution where it is most needed within a single trajectory.

**ASI** \citep{neitz2018adaptive} learns to skip timesteps by min-pooling over reconstruction losses, selecting intervals that are *easiest to predict*. It operates on raw observation prediction without integration into a model-based RL loop. In contrast, our gate optimizes for *dynamical significance* via latent-state deltas rather than prediction ease, and is fully integrated into the RSSM imagination pipeline for policy optimization.

**LS-Imagine** \citep{li2025lsimagine} learns jumping flags based on affordance-map kurtosis for open-world exploration in MineDojo, with goal-conditioned jumpy state transitions that skip over low-information states. Our gate differs in two key ways: it operates within the actor-critic MBRL imagination loop with policy-dependent variable-rate stepping, rather than goal-conditioned exploration jumps; and it selects strides based on latent-state dynamics rather than observation-space affordance maps.

**DyMoDreamer** \citep{dymodreamer2025} extracts motion cues via inter-frame differencing masks at the observation level and integrates stochastic categorical dynamic modulation into the RSSM latent space, focusing on motion-relevant features. Our method changes the *temporal resolution* of imagination rather than the per-step representation quality, achieving complementary benefits---the two approaches target orthogonal axes of improvement and could in principle be combined.
