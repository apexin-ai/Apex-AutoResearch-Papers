# 2. Related Work

We situate our approach within five related lines of research: fixed-rate model-based RL, variable-rate and temporal abstraction, learned skipping for planning, imagination quality improvement, and event-aware world models.

## 2.1 Model-Based RL with Fixed-Rate Imagination

Modern model-based RL agents learn latent world models and optimize policies through imagined rollouts at a fixed temporal resolution.

DreamerV3 \citep{hafner2023dreamerv3} learns a Recurrent State-Space Model (RSSM) that maintains deterministic and stochastic latent states, training an actor-critic purely through $H$-step imagined trajectories. It achieves strong performance across diverse domains but operates at a fixed one-environment-step-per-latent-step resolution, limiting the effective planning horizon to $H$ environment steps regardless of episode length. NE-Dreamer \citep{nedreamer2026} replaces pixel-level reconstruction with next-embedding prediction, yielding a decoder-free latent world model that improves sample efficiency while retaining the fixed-rate imagination structure. R2-Dreamer \citep{r2dreamer2026} similarly eliminates the observation decoder by training with redundancy-reduced latent targets, accelerating training and improving robustness.
These methods share a fundamental limitation: each imagination step covers exactly one environment timestep, so for long-horizon tasks (e.g., 250-step manipulation episodes), a rollout of $H{=}15$ steps covers only 6\% of the episode, creating a credit assignment bottleneck. Our method addresses this by learning to skip uneventful timesteps, extending the effective horizon to $\sum \Delta t_i$ environment steps (up to $H \times K$) without additional latent computation.

## 2.2 Variable-Rate and Temporal Abstraction

Several works introduce temporal flexibility into world model dynamics, either through externally specified time gaps or learned hierarchical abstractions.

TAWM \citep{nhu2025tawm} introduces time-aware world models that condition latent dynamics on a temporal gap $\Delta t$ via RK4/Euler integration, enabling the model to predict across variable time scales. However, $\Delta t$ must be externally specified rather than learned, and TAWM is a model-agnostic framework evaluated on TD-MPC2's short-horizon MPC framework ($H{=}3$--$5$ with MPPI planning), where temporal skipping during planning is counterproductive. Our method adapts the variable-$\Delta t$ conditioning principle to DreamerV3's RSSM but makes $\Delta t$ \emph{state-dependent} via a learned event gate. THICK \citep{romac2024thick} learns a two-level temporal hierarchy via discrete latent dynamics, where the lower level forms invariant contexts and the upper level predicts context changes. While this achieves temporal abstraction, the fixed two-level structure cannot express continuous degrees of event significance or variable skip lengths within a single hierarchy level. HWM \citep{zhang2026hwm} extends this line by learning multi-scale latent world models for hierarchical planning with a learned action encoder for temporal compression, but similarly relies on a fixed two-level planner architecture. ASI \citep{neitz2018adaptive} learns to skip timesteps in recurrent dynamics models by min-pooling over reconstruction losses, selecting intervals that are easiest to predict. It operates on raw observation prediction without integration into a model-based RL loop and optimizes for prediction ease rather than dynamical significance.

Our approach avoids the multi-model exploitation problem identified by \citet{schiewer2024hierarchical} in hierarchical world models by operating within a single RSSM, while offering finer temporal adaptation than two-level hierarchies through a continuous per-step stride selection.

## 2.3 Learned Skipping for Planning

A separate line of work learns explicit skip or jump decisions to extend planning horizons.

LS-Imagine \citep{li2025lsimagine} learns jumping flags based on affordance-map kurtosis for open-world exploration in MineDojo, enabling the agent to skip over low-information states during imagination. The jumps are action-independent and designed for exploration in open-world settings. Our gate differs in two key ways: it operates within the actor-critic MBRL imagination loop with policy-dependent variable-rate stepping, and it selects strides based on latent-state dynamics rather than observation-space affordance maps. I-TAP \citep{itap2026} learns temporal abstractions via discrete residual tokens with an RQ-VAE, performing MCTS planning in token space for offline RL. It operates in a fundamentally different paradigm---offline and autoregressive---from our online RSSM-based approach.

While both LS-Imagine and I-TAP demonstrate the value of temporal flexibility in planning, neither addresses the specific setting of online actor-critic training with variable-rate latent imagination. Our event gate fills this gap by integrating state-dependent stride selection directly into DreamerV3's imagination pipeline.

## 2.4 Imagination Quality Improvement

Rather than changing temporal resolution, several recent works improve the quality of fixed-rate imagination rollouts.

DMWM \citep{wang2025dmwm} introduces a dual-mind architecture combining an RSSM-based System~1 for intuitive transitions with a logic-informed neural network (LINN) System~2 that provides logical reasoning feedback, improving long-horizon imagination coherence through logical constraints. It shares our motivation of extending effective RSSM imagination but addresses error accumulation at fixed temporal resolution rather than extending the temporal horizon. DyMoDreamer \citep{dymodreamer2025} uses inter-frame differencing masks with stochastic categorical dynamic modulation to focus RSSM attention on motion-relevant features, achieving strong results on visual benchmarks (Atari 100k, DMC). It operates at the observation/pixel level to improve per-step representation quality, whereas our method operates in latent space and changes the \emph{temporal resolution} of imagination rather than the attention quality of individual steps---the two approaches target complementary axes of improvement and could in principle be combined. ELVIS \citep{du2026elvis} introduces ensemble-calibrated uncertainty-aware $\lambda$-return gating for long-horizon RSSM-based MPC, adaptively weighting bootstrapping versus continued rollout based on epistemic uncertainty. While ELVIS adapts \emph{how much} to trust each imagination step, it does not change \emph{how many} environment steps each imagination step covers---our gate modifies the temporal resolution itself.

## 2.5 Event-Aware World Models

Event-driven representations have recently been applied to world models, though primarily at the observation level.

EA-WM \citep{eawm2026} introduces event-aware fusion via frame-difference supervision for video world models at the pixel level, using event signals to improve generation quality of dynamic regions. While both EA-WM and our method leverage event-like signals (frame differences vs. latent-state deltas), EA-WM applies them to improve pixel-level video prediction quality, whereas we use latent-state change magnitude to drive \emph{temporal stride selection} in the imagination loop for policy optimization. Our event gate operates entirely in the learned latent space, using state-delta magnitude as a proxy for dynamical significance to determine when fine-grained versus coarse-grained imagination is warranted.
