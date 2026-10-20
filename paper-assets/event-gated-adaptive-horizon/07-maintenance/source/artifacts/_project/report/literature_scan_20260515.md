# Literature Scan: Temporal Abstraction in MBRL (2024-2026)

**Date**: 2026-05-15
**Purpose**: Related work survey for CoRL 2026 diagnostic paper on dt_embedding → delusional critic in DreamerV3

---

## Direct Competitors

### 1. THICK: Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics
- **Authors**: Christian Gumbsch, Noor Sajid, Georg Martius, Martin V. Butz
- **Venue**: ICLR 2024
- **Link**: https://openreview.net/forum?id=TjCDNssXKU
- **Summary**: Learns a world model hierarchy via discrete latent dynamics. Lower level updates latent state sparsely (forming "invariant contexts"), higher level predicts context changes. Enables multi-timescale reasoning in MBRL.
- **Relation**: **Direct competitor** — addresses temporal abstraction in Dreamer-style world models. However, focuses on *hierarchical prediction* rather than diagnosing failure modes of temporal embeddings. Does NOT study delusional critic effects from trained dt embeddings.
- **Key difference**: THICK adds hierarchy on top of RSSM; we diagnose a pathology *within* the existing DreamerV3 temporal mechanism.

### 2. Time-Aware World Model for Adaptive Prediction and Control (TAWM)
- **Authors**: Anh N. Nhu, Sanghyun Son, Ming Lin
- **Venue**: ICML 2025 (arXiv: 2506.08441)
- **Link**: https://arxiv.org/abs/2506.08441
- **Summary**: Conditions world model on time-step size (Δt), training over diverse Δt values to learn both high- and low-frequency dynamics. Uses RK4 to stabilize learning at large temporal gaps. Adapts TD-MPC2 architecture.
- **Relation**: **Direct competitor** — explicitly incorporates variable time steps into world model. However, focuses on *continuous control with variable observation rates*, not on diagnosing how learned temporal embeddings cause value overestimation in imagination. Architecture is TD-MPC2 based, not RSSM/Dreamer.
- **Key difference**: TAWM treats Δt as beneficial conditioning; we show that *learning* such conditioning in DreamerV3 causes delusional critic collapse.

### 3. Improving Planning and MBRL with Temporally-Extended Actions
- **Authors**: Palash Chatterjee, Roni Khardon
- **Venue**: NeurIPS 2025 (arXiv: 2505.15754)
- **Link**: https://arxiv.org/abs/2505.15754
- **Summary**: Treats action duration as optimization variable in continuous-time MBRL planning. Speeds up simulation, enables deep horizon search with shallow planner depth, reduces compounding model errors.
- **Relation**: **Direct competitor** — variable-duration actions in MBRL. Complementary angle: they optimize duration for planning efficiency; we show that *learned* duration embeddings create pathological value estimates.
- **Key difference**: Focus on planning efficiency, not on critic pathologies.

### 4. Learning World Models With Hierarchical Temporal Abstractions: A Probabilistic Perspective
- **Authors**: Vaisakh Shaj
- **Venue**: arXiv 2024 (2404.16078)
- **Link**: https://arxiv.org/abs/2404.16078
- **Summary**: Proposes Hidden-Parameter SSMs and Multi-Time Scale SSMs for scalable hierarchical world models with nonstationary dynamics across temporal scales.
- **Relation**: **Complementary/competitor** — theoretical framework for multi-timescale SSMs. Does not empirically study DreamerV3's dt_embedding or its failure modes.

---

## Complementary Work

### 5. Exploring the Limits of Hierarchical World Models in Reinforcement Learning
- **Authors**: Robin Schiewer, Anand Subramoney, Laurenz Wiskott
- **Venue**: Scientific Reports, Nov 2024 (arXiv: 2406.00483)
- **Link**: https://arxiv.org/abs/2406.00483
- **Summary**: Systematic study of HMBRL with static, environment-agnostic temporal abstraction. Constructs hierarchical world models at various temporal resolutions, trains stacked agents with top-down goal communication.
- **Relation**: **Complementary** — empirical analysis of temporal abstraction limits in hierarchical MBRL. Shares diagnostic spirit but focuses on hierarchical goal-conditioned setting, not single-agent DreamerV3.

### 6. NE-Dreamer: Next Embedding Prediction Makes World Models Stronger
- **Authors**: CoRL Team (arXiv: 2603.02765, March 2026)
- **Venue**: arXiv 2026
- **Link**: https://arxiv.org/abs/2603.02765
- **Summary**: Decoder-free MBRL agent replacing pixel reconstruction with next-embedding prediction via causal temporal transformer. Keeps RSSM dynamics and imagination-based actor-critic.
- **Relation**: **Complementary** — improves DreamerV3's representation learning (decoder-free). Does not address temporal abstraction or dt_embedding pathologies.

### 7. Dreamer-CDP: Improving Reconstruction-free World Models Via Continuous Deterministic Representation Prediction
- **Venue**: arXiv 2026 (2603.07083)
- **Link**: https://arxiv.org/html/2603.07083
- **Summary**: Adds continuous deterministic representation prediction to Dreamer, matching performance without reconstruction.
- **Relation**: **Complementary** — architectural improvement to Dreamer, orthogonal to temporal abstraction issues.

### 8. Dreamer 4: Training Agents Inside of Scalable World Models
- **Authors**: Danijar Hafner, Wilson Yan
- **Venue**: arXiv 2025 (2509.24527)
- **Link**: https://arxiv.org/abs/2509.24527
- **Summary**: Block-causal transformer world model with "shortcut forcing" objective. First agent to obtain diamonds in Minecraft from offline data. Scalable architecture trained on diverse videos + small action-conditioned data.
- **Relation**: **Complementary** — next-gen Dreamer architecture (transformer-based, not RSSM). Does not retain dt_embedding mechanism. Our diagnostic applies to DreamerV3's RSSM + dt_embedding specifically.

### 9. Recall to Imagine (R2I): Mastering Memory Tasks with World Models
- **Authors**: Samsami, Zholus, Rajendran, Chandar
- **Venue**: ICLR 2024
- **Link**: https://arxiv.org/abs/2403.04253
- **Summary**: Integrates state space models (S3M) into DreamerV3's world model for long-term memory and credit assignment. 9x speedup over DreamerV3.
- **Relation**: **Complementary** — DreamerV3 extension for long-horizon tasks. Addresses temporal credit assignment but not temporal abstraction via dt embeddings.

### 10. Optimistic World Models: Efficient Exploration in Model-Based Deep RL
- **Venue**: arXiv 2026 (2602.10044)
- **Link**: https://arxiv.org/abs/2602.10044
- **Summary**: Adds optimistic dynamics loss to DreamerV3 ("Optimistic DreamerV3"), biasing imagined transitions toward higher rewards. Achieves 152.68% mean HNS vs DreamerV3's 97.45%.
- **Relation**: **Complementary** — modifies DreamerV3's imagination to be optimistic. Interesting contrast: they *intentionally* bias value upward for exploration; we show *unintentional* upward bias from dt_embedding causes collapse.

### 11. MAD-TD: Model-Augmented Data Stabilizes High Update Ratio RL
- **Authors**: Voelcker et al.
- **Venue**: ICLR 2025 (arXiv: 2410.08896)
- **Link**: https://arxiv.org/abs/2410.08896
- **Summary**: Uses small amounts of model-generated on-policy data to combat value overestimation and stabilize high UTD training. Shows model-generated data can suppress overestimation bias.
- **Relation**: **Complementary** — addresses value overestimation via model-generated data augmentation. Different mechanism (UTD instability) but related symptom (overestimation).

### 12. TempoRL: Learning When to Act
- **Venue**: ICML 2021
- **Link**: https://ml.informatik.uni-freiburg.de/wp-content/uploads/papers/21-ICML-TempoRL.pdf
- **Summary**: Agent learns both action selection and action duration. Two-level control: what to do + how long to do it.
- **Relation**: **Background** — foundational work on variable-duration actions. Model-free, predates DreamerV3.

### 13. MOSEAC: Streamlined Variable Time Step Reinforcement Learning
- **Venue**: arXiv 2024 (2406.01521)
- **Link**: https://arxiv.org/html/2406.01521
- **Summary**: VTS-RL algorithm learning actions and durations simultaneously.
- **Relation**: **Background** — variable time step in model-free RL.

---

## Background / Delusional Critic

### 14. Non-Delusional Q-learning and Value-Iteration
- **Authors**: Tyler Lu, Dale Schuurmans, Craig Boutilier
- **Venue**: NeurIPS 2018
- **Link**: https://proceedings.neurips.cc/paper_files/paper/2018/hash/5fd0245f6c9ddbdf3eff0f505975b6a7-Abstract.html
- **Summary**: Identifies "delusional bias" in Q-learning with function approximation — standard Q-updates make globally uncoordinated action choices, producing inconsistent/conflicting Q-values. Introduces "information sets" ensuring policy consistency. Proves model-based and model-free variants remove delusional bias.
- **Relation**: **Key background** — defines the "delusional" terminology in RL. Their delusion arises from function approximation constraints on policy class; ours arises from temporal embedding enabling the critic to hallucinate unreachable temporal states during imagination.
- **Key difference**: They address model-free Q-learning with restricted policy class. We identify a new delusional mechanism specific to learned temporal embeddings in model-based imagination.

### 15. ConQUR: Mitigating Delusional Bias in Deep Q-Learning
- **Venue**: ICLR 2020 submission
- **Link**: https://openreview.net/forum?id=ryg8WJSKPr
- **Summary**: Extends non-delusional Q-learning to deep RL with continuous actions using hindsight relabeling to identify delusional updates.
- **Relation**: **Background** — extension of Lu et al. (2018) delusion concept. Still model-free focused.

### 16. Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of RL
- **Authors**: Nauman, Bortkiewicz, Miłoś, Trzcinski, Ostaszewski, Cygan
- **Venue**: ICML 2024
- **Link**: https://arxiv.org/abs/2403.00514
- **Summary**: Large-scale diagnostic study (60+ agents, 14 tasks) showing overestimation, overfitting, and plasticity loss are interconnected failure modes in actor-critic methods. Regularization techniques have limited generalization.
- **Relation**: **Important background** — shares diagnostic methodology spirit. Shows overestimation is systemic in actor-critic. Our work pinpoints a *specific structural cause* (dt_embedding) in a specific agent (DreamerV3) rather than studying generic regularization.

### 17. Stochastic Actor-Critic: Mitigating Overestimation via Temporal Aleatoric Uncertainty
- **Venue**: arXiv Jan 2026 (2601.00737)
- **Link**: https://arxiv.org/abs/2601.00737
- **Summary**: Uses distributional critic modeling one-step temporal return uncertainty to scale pessimistic bias. Eliminates need for double/ensemble critics.
- **Relation**: **Background** — addresses overestimation in model-free AC via distributional approach. Different mechanism from our model-based diagnosis.

### 18. Emergent Temporal Abstractions in Autoregressive Models Enable Hierarchical RL
- **Venue**: arXiv Dec 2025 (2512.20605)
- **Link**: https://arxiv.org/abs/2512.20605
- **Summary**: Higher-order non-causal sequence model controls residual stream of a base autoregressive model to discover temporally-abstract actions during RL finetuning.
- **Relation**: **Background** — temporal abstraction in LLM-based RL agents, not world-model MBRL.

---

## Novelty Assessment

### Our contribution relative to existing literature:

1. **No prior work diagnoses dt_embedding → delusional critic in DreamerV3.** The temporal abstraction literature (THICK, TAWM, Chatterjee & Khardon) focuses on *adding* temporal abstraction capabilities. None identifies that DreamerV3's *existing* trained dt_embedding is pathological.

2. **"Delusional critic" in a new context.** Lu et al. (2018) coined "delusional" for policy-inconsistent Q-backups in function approximation. We extend this concept to model-based imagination: the critic learns to exploit unreachable temporal states during imagined rollouts, causing systematic overestimation. This is a genuinely novel mechanism.

3. **Diagnostic methodology for MBRL is underexplored.** Nauman et al. (ICML 2024) did a large diagnostic for model-free AC. No comparable diagnostic exists for DreamerV3's imagination pipeline. Our C6 (dt=1 imagination) finding — that a zero-cost fix eliminates the pathology — is practically impactful.

4. **The dt=1 mitigation is novel.** No prior work proposes fixing DreamerV3's performance collapse by simply forcing dt=1 during imagination. This is a free lunch that the community should know about.

5. **Complementary to Dreamer 4.** Dreamer 4 moves to transformers, abandoning RSSM+dt_embedding. Our diagnostic explains *why* this architectural shift helps — the old temporal mechanism was broken. This provides theoretical justification for Dreamer 4's design choices.

### Positioning:
- **Not scooped**: No one has published this specific diagnosis.
- **Timely**: DreamerV3 remains widely used (Nature 2025 publication); Dreamer 4 just appeared. A diagnostic explaining the transition is valuable.
- **Risk**: TAWM (ICML 2025) shows variable-Δt world models can work — but in TD-MPC2, not RSSM/Dreamer. We should cite and contrast clearly.
