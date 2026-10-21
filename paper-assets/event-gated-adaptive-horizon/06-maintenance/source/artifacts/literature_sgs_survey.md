# SGS / Stop-Gradient Literature Survey
Date: 2026-05-15

## 1. Stop-Gradient in MBRL

### 1.1 Dreamer Family

- **Mastering Diverse Domains through World Models** (Hafner et al., Nature 2025 / arXiv 2023) — DreamerV3 uses stop-gradient for KL balancing (asymmetric sg on prior/posterior) and critic targets (sg on bootstrapped returns), but **reward head gradients flow freely** into the world model encoder/RSSM. Actor-critic is isolated from the world model (no shared gradients). No sg on decoder either.

- **Mastering Atari with Discrete World Models** (Hafner et al., ICLR 2021) — DreamerV2 contains a **critical ablation**: stopping reward gradients from the world model representation **improved** performance on some tasks. The paper notes "representations not specifically trained to predict previously experienced rewards may generalize better to new situations." This is the closest precedent to our SGS, but a blunt binary on/off rather than targeted surgery on a specific input (dt_emb).

- **MuDreamer: Learning Predictive World Models without Reconstruction** (Burchi & Timofte, arXiv 2024) — Applies sg on the decoder input `o_hat ~ p(o | sg(s_t))`, preventing reconstruction gradients from shaping representations. Reward/value heads have NO sg. The key architectural departure from DreamerV3 is stopping reconstruction gradients, not reward gradients.

- **Dreamer-CDP: Improving Reconstruction-free World Models via Continuous Deterministic Representation Prediction** (Hauri & Zenke, arXiv 2026) — JEPA-style predictor with sg on target embeddings `L_CDP = -cos(sg(u_t), u_hat_t)`. Decoder trained with detached gradients (visualization only). Reward head: no sg.

### 1.2 TD-MPC / MuZero Family

- **TD-MPC2: Scalable, Robust World Models for Continuous Control** (Hansen et al., arXiv 2023) — sg on latent state targets `||z'_t - sg(h(s'_t))||^2` to prevent collapse in joint-embedding consistency loss. EMA target for Q. Reward head: **no sg**, gradients flow through latent dynamics to encoder.

- **EfficientZero** (Ye et al., NeurIPS 2021) / **EfficientZero V2** (Wang et al., ICML 2024) — SimSiam-style sg on true next-state representation for temporal consistency. Reward/value heads: no sg.

- **UniZero** (Pu et al., TMLR 2025) — sg on target encoder output `sg(h_bar(o_{t+1}))`. All head gradients (reward, value, policy) flow through transformer backbone.

- **DCWM: Discrete Codebook World Models** (Scannell et al., ICLR 2025) — sg on target latent code + straight-through Gumbel-softmax. Reward head: no sg.

### 1.3 Theoretical Work on sg in RL

- **Bridging State and History Representations: Understanding Self-Predictive RL** (Ni et al., ICLR 2024) — Provides theoretical grounding for why sg is necessary in self-predictive representations: sg targets avoid representational collapse under linear assumptions; non-sg targets lack this property.

- **A Unifying Framework for Action-Conditional Self-Predictive RL** (Khetarpal et al., DeepMind, arXiv 2024) — Analyzes BYOL-style self-predictive objectives; sg prevents collapse in ODE dynamics analysis.

- **Do Transformer World Models Give Better Policy Gradients?** (Ma et al., arXiv 2024) — Proposes Action World Models eliminating "circuitous gradient paths." Proves transformer AWMs produce policy gradients bounded by O(H^3) vs exponential growth.

### 1.4 Anti-Stop-Gradient Evidence

- **JOWA: Scaling Offline Model-Based RL via Jointly-Optimized World-Action Model Pretraining** (Zhang et al., ICLR 2025) — Ablation with `sg(L_action)` causes **catastrophic failure**: joint optimization provides mutual regularization at scale. An important counter-example showing sg is not always beneficial.

### 1.5 Summary Table

| Method | sg on KL/consistency | sg on reward head | sg on value targets | sg on decoder |
|--------|---------------------|-------------------|--------------------|----|
| DreamerV3 | Yes (asymmetric) | **No** | Yes | No |
| DreamerV2 | Yes | **No** (ablation showed benefit of sg) | Yes | No |
| TD-MPC2 | Yes (latent target) | **No** | Yes (EMA) | N/A |
| MuZero/EfficientZero | Yes (SimSiam) | **No** | Yes (target net) | N/A |
| MuDreamer | Yes | **No** | Yes | **Yes** |
| Dreamer-CDP | Yes (JEPA) | **No** | Yes | Detached |
| JOWA | N/A | **No** | Yes | N/A |

**Key gap: No major MBRL method applies stop-gradient to the reward head. Our SGS — selectively detaching dt_emb input to the reward head — is novel.**


## 2. Value Overestimation in World Models

### 2.1 Foundational Delusional Bias

- **Non-delusional Q-learning and Value-iteration** (Lu, Schuurmans, Boutilier, NeurIPS 2018 Best Paper) — Defines "delusional bias": globally uncoordinated action choices w.r.t. the expressible policy class produce inconsistent Q-values. Introduces policy-consistent backups.

- **Identifying and Addressing Delusions for Target-Directed Decision-Making** (Zhao et al., ICML 2025) — Target-directed MBRL agents chase hallucinated infeasible targets. Proposes target feasibility evaluator to reject infeasible targets before they corrupt planning.

### 2.2 Compounding Error → Overestimation

- **MAD-TD: Model-Augmented Data stabilizes High Update Ratio RL** (Voelcker et al., ICLR 2025 Spotlight) — High update-to-data ratios cause value overestimation. Synthetic world model data fills coverage gaps, combating overestimation without parameter resets.

- **On Rollouts in Model-Based RL (Infoprop)** (Frauenknecht et al., ICLR 2025) — Model errors during rollouts cause overestimated total variance. Infoprop terminates rollouts when epistemic uncertainty exceeds threshold, enabling 100-step rollouts.

- **Dynamic-Horizon Model-Based Value Estimation (DMVE)** (Wang et al., IEEE TNNLS 2022) — Dynamically adjusts rollout horizon per state by comparing value expansion errors, selecting horizons where model is most reliable.

- **Lower Expectile Q-Learning (LEQ)** (Park & Lee, arXiv 2024) — Targets lower tail of value distribution for conservative estimates in model-based offline RL.

### 2.3 Objective Mismatch

- **A Unified View on Solving Objective Mismatch in MBRL** (Wei et al., arXiv 2024, survey of 46 papers) — Model predictive accuracy is often not correlated with action quality. Taxonomy: Distribution Correction, Control-As-Inference, Value-Equivalence, Differentiable Planning.

- **VaGraM: Value Gradient weighted Model-Based RL** (Voelcker et al., ICLR 2022) — Rescales model MSE loss with value function gradient information. Model focuses accuracy on value-relevant state dimensions. **Closest to gradient-pathway analysis of overestimation**, but focuses on model error direction, not on gradient flow through shared parameters causing systematic bias.

- **ALM: Simplifying Model-based RL** (Ghugare et al., ICLR 2023) — Unified lower bound on expected returns, jointly optimizing latent model and policy without reconstruction. Avoids auxiliary objective misalignment.

### 2.4 Gradient Pathway Perspective

- **MAAC: Model-Augmented Actor-Critic** (Clavera et al., ICLR 2020) — **Most direct gradient-pathway analysis**: backpropagating policy gradients through learned models causes gradient instability from compounding model errors. Terminal value function truncates gradient propagation.

- **Stable Gradients for Stable Learning at Scale in Deep RL** (Creus Castanyer et al., NeurIPS 2025 Spotlight) — Suboptimal architecture choices create gradient pathologies that worsen with scale. Direct interventions stabilizing gradient flow enable robust scaling.

- **Stop Regressing: Training Value Functions via Classification** (Farebrother et al., ICML 2024 Oral) — MSE regression creates unstable gradients for value learning; categorical cross-entropy (HL-Gauss) provides stable gradients and better representations.

### 2.5 Critic Instability Mechanisms

- **Overestimation, Overfitting, and Plasticity in Actor-Critic** (Nauman et al., ICML 2024) — These three pathologies are intertwined. Properly regularized SAC matches model-based approaches.

- **CHAIN: Reducing the Chain Effect of Value and Policy Churn** (Tang & Berseth, NeurIPS 2024) — Value churn and policy churn form a compounding cycle: value estimation errors bias policy improvement, which generates new value errors.

- **Plasticity Loss in Deep RL** (Klein et al., arXiv 2024, survey) — Networks lose ability to adapt; plasticity loss directly contributes to value overestimation.

### 2.6 Novelty Assessment for This Direction

**No paper frames value overestimation in MBRL as arising from a specific gradient pathway (reward → shared embedding → critic).** MAAC (2020) analyzes gradient instability through models but focuses on explosion rather than systematic positive bias. VaGraM analyzes which model errors matter for value but doesn't identify a specific gradient pathway as the cause. **Our CIVO mechanism (reward gradients shaping dt_emb → critic exploiting biased dt_emb → overestimation) is a novel causal pathway not previously identified.**


## 3. Temporal Embedding Issues

### 3.1 Timestep Embedding Instability (Direct Evidence)

- **The Disappearance of Timestep Embedding in Modern Time-Dependent Neural Networks** (Kim et al., arXiv 2024) — **Highly relevant.** Documents "vanishing timestep embedding": normalization layers (BatchNorm, GroupNorm) cancel out channel-wise scalar offsets from timestep embeddings. Affects Neural ODEs and diffusion models. Proposed fixes: positional (spatially-varying) embeddings, zero bias init, fewer normalization groups. Supports our concern that learned dt embeddings can degenerate.

### 3.2 Variable dt in World Models

- **Time-Aware World Model for Adaptive Prediction and Control (TAWM)** (Nhu, Son, Lin, ICML 2025) — **Most directly relevant.** Conditions world model on variable dt using direct numerical input with log scaling `tau(dt) = max(0, log10(dt) + 5)`. Authors explicitly report **"convergence failures when employing linear dt integration"** — only log-scaled approach was stable. Does NOT use learned dt embeddings. Encoder deliberately NOT conditioned on dt.

- **Making Deep Q-learning Methods Robust to Time Discretization** (Tallec et al., ICML 2019) — Proves Q-learning **does not exist in continuous time**; standard DQN/DDPG collapse with small time steps. Foundational evidence for why naive dt conditioning causes instability.

- **Continuous-Time Model-Based RL** (Yildiz et al., ICML 2021) — Uses Bayesian Neural ODEs to avoid time-discretization approximation. Robust against irregular and noisy data.

- **DyMoDreamer: World Modeling with Dynamic Modulation** (Zhang et al., arXiv 2025) — Predicted dt enhances world model temporal awareness. Uses differential observations from inter-frame differencing.

### 3.3 Hierarchical Temporal Abstraction (Architectural Alternatives)

- **THICK: Learning Hierarchical World Models with Adaptive Temporal Abstractions** (Gumbsch et al., ICLR 2024 Spotlight) — Lower level updates latent state sparsely (invariant contexts); higher level predicts context transitions. Achieves temporal abstraction through architecture, not dt embeddings. **No dt conditioning on the RSSM.**

- **Director: Deep Hierarchical Planning from Pixels** (Hafner et al., NeurIPS 2022) — High-level policy selects latent goals; temporal abstraction emerges from goal-reaching, no explicit duration conditioning.

- **Emergent Temporal Abstractions in Autoregressive Models** (Kobayashi et al., arXiv 2025) — Higher-order model generates temporally-abstract actions via residual stream. Learned termination conditions.

### 3.4 Action Duration / Repetition (Related but Distinct)

- **TempoRL: Learning When to Act** (Biedenkapp et al., ICML 2021) — Learns skip-policy for action commitment duration. Duration is a **policy output**, not a world model input.

- **SDAR: Select before Act** (Nie et al., ICLR 2025) — Per-dimension act-or-repeat decisions for continuous control.

- **Improving Planning and MBRL with Temporally-Extended Actions** (Chatterjee & Khardon, NeurIPS 2025) — Treats action duration as optimization variable; reduces compounding errors.

### 3.5 Novelty Assessment for This Direction

**No prior work conditions Dreamer-family RSSM on a learned dt embedding.** TAWM uses numerical dt with log scaling (not learned embedding). THICK/Director achieve temporal abstraction architecturally. Action repetition literature treats duration as policy output, not world model input. **The failure mode we identify — learned dt_emb being co-opted by reward gradients to encode reward-predictive features rather than temporal information — is unprecedented in the literature.**


## 4. Gradient Surgery Techniques

### 4.1 Foundational Methods

- **PCGrad: Gradient Surgery for Multi-Task Learning** (Yu et al., NeurIPS 2020) — Projects conflicting task gradients onto the normal plane of each other. 2-15M fewer samples in multi-task RL.

- **GradNorm** (Chen et al., ICML 2018) — Dynamically tunes gradient magnitudes across tasks to equalize training rates. Single hyperparameter alpha.

- **CAGrad: Conflict-Averse Gradient Descent** (Liu et al., NeurIPS 2021) — Maximizes worst-case local improvement across tasks. Generalizes both standard GD and MGDA.

- **Nash-MTL** (Navon et al., ICML 2022) — Nash Bargaining game for gradient combination. Proportional fairness with convergence guarantees. SOTA on MT10.

- **Aligned-MTL** (Senushkin et al., CVPR 2023) — Aligns principal components of gradient matrix for orthogonal, equal-magnitude gradients. Provable convergence to global optimum.

### 4.2 Recent Advances (2024-2026)

- **ConicGrad** (Hassanpour et al., arXiv 2025) — Angular cone constraints on gradient updates. Balances task gradients without over-constraining.

- **SAM-GS: Gradient Similarity Surgery** (Bergmeister et al., ECML-PKDD 2025) — Similarity-aware momentum gradient surgery.

- **DTME-MTL** (Jeong & Yoon, ICCV 2025) — Token-space gradient conflict resolution for transformers.

- **RECON: Reducing Conflicting Gradients from the Root** (Shi et al., ICLR 2023) — Converts high-conflict shared layers to task-specific layers. Reduces severe conflicts by 67-79%. Structural separation > soft gradient surgery.

- **Proactive Gradient Conflict Mitigation via Sparse Training** (Zhang et al., arXiv 2024) — Sparse training reduces conflicts; complementary to gradient manipulation.

### 4.3 Gradient Surgery in RL (Not World Models)

- **GCR-PPO** (Munn et al., arXiv 2025) — Gradient conflict resolution for multi-objective robot RL via multi-headed critic.

- **Gradient Shaping for Multi-Constraint Safe RL** (Yao et al., L4DC 2024) — Manipulates gradients from multiple safety constraints.

- **Gradient Routing** (arXiv 2024) — Data-dependent masks on gradients during backprop to isolate capabilities to network subregions. Enables unlearning and scalable oversight.

- **Imbalanced Gradients in RL Post-Training of Multi-Task LLMs** (Wu et al., EACL 2026) — First systematic study of gradient imbalance in multi-task RL training; certain tasks produce larger gradients but this does NOT correlate with learning gains.

### 4.4 Gradient Management in World Models (Closest to Our Work)

- **HarmonyDream: Task Harmonization Inside World Models** (Ma et al., ICML 2024) — **Most relevant.** Addresses observation vs. reward gradient imbalance (observation loss ~100x larger). Uses learnable sigma parameters for loss-scale balancing: `sum_i [1/sigma_i * L_i + log(1 + sigma_i)]`. Achieves 10-69% boost on visual robotic tasks. **However, this is loss-magnitude balancing, NOT gradient-direction surgery.** They do NOT analyze gradient directions/conflicts between heads.

- **VaGraM** (Voelcker et al., ICLR 2022) — Value-gradient-weighted model learning. Addresses model-policy mismatch but not inter-head conflicts.

- **Learning Latent Dynamic Robust Representations (HRSSM)** (Sun et al., ICML 2024) — Gradient detachment in spatio-temporal masking: gradients flow only through mask branch, RSSM updated via EMA. Addresses joint training instability.

### 4.5 Novelty Assessment for This Direction

**No paper applies gradient surgery (PCGrad, CAGrad, etc.) to manage conflicts between world model prediction heads.** HarmonyDream is the closest but uses loss-scale balancing, not direction-aware surgery. No one has measured gradient cosine similarity between world model heads.

**Our SGS is a minimal, targeted gradient intervention**: rather than full gradient surgery across all heads, we apply a single stop-gradient on one specific input (dt_emb) to one specific head (reward). This is simpler than PCGrad/CAGrad and directly addresses a diagnosed causal pathway (reward → dt_emb → CIVO) rather than a generic multi-task conflict.


## 5. Novelty Assessment

### What exists:
1. Stop-gradient is standard in MBRL for **consistency targets** (preventing collapse) and **value bootstrapping** (stable TD). No one applies sg to the reward head.
2. DreamerV2 found empirically that stopping all reward gradients from representations can help, but this was a blunt intervention, not a targeted one on a specific input.
3. HarmonyDream addresses magnitude imbalance between observation and reward losses, but via loss scaling, not gradient surgery.
4. TAWM conditions world models on dt but uses numerical input with log scaling, not learned embeddings, and does not analyze gradient pathways.
5. Gradient surgery (PCGrad, CAGrad, etc.) has never been applied within world model multi-head training.

### What is novel in our SGS:
1. **Causal diagnosis**: We identify a specific gradient pathway (reward → dt_emb) as the cause of CIVO — no prior work traces value overestimation to a gradient pathway through a shared embedding.
2. **Targeted intervention**: SGS detaches only the dt_emb input to the reward head, preserving all other gradient flows. This is neither full sg on reward (DreamerV2) nor loss reweighting (HarmonyDream) nor generic gradient surgery (PCGrad).
3. **Temporal embedding corruption**: We show that reward gradients co-opt dt_emb to encode reward-predictive features rather than temporal information — a failure mode not documented in prior work (Kim et al. 2024 studied timestep embedding vanishing from normalization, a different mechanism).
4. **MBRL-specific gradient surgery**: We are the first to apply targeted gradient intervention within the prediction heads of a world model, opening a new design dimension between "all gradients shared" and "all heads isolated."

### Positioning relative to key papers:
- vs. **DreamerV2** sg ablation: We provide the *mechanism* (CIVO via dt_emb corruption) and a *targeted* fix (detach only dt_emb, not all reward gradients)
- vs. **HarmonyDream**: We address gradient *direction* conflict on a specific input, not gradient *magnitude* imbalance across heads
- vs. **TAWM**: We identify *why* learned dt conditioning is dangerous (gradient pathway co-optation) and provide a fix; they avoid the problem by using fixed numerical input
- vs. **PCGrad/CAGrad**: We use a simpler, more interpretable intervention (single sg) motivated by causal diagnosis rather than generic conflict resolution
