# Related Work — Expanded (26 references)

> Organized for Framing B: Diagnostic analysis of temporal abstraction in DreamerV3, with CIVO (Compounding Imagination Variance Overflow) as the central finding and Full-SGS as proof-of-concept intervention.

---

## 1. World Model Learning in Model-Based RL

This section covers the systems our diagnostic analysis builds upon.

- **Hafner, Lillicrap, Norouzi & Ba (2021).** *Mastering Atari with Discrete World Models.* ICLR 2021. Introduces DreamerV2 with categorical latent representations and KL balancing for world model training, achieving human-level Atari. **[support]** DreamerV2 establishes the RSSM + multi-head decoder architecture whose gradient interactions we diagnose; our analysis of obs-decoder gradient pathways directly applies to its training pipeline.

- **Hafner, Pasukonis, Ba & Lillicrap (2023).** *Mastering Diverse Domains through World Models.* arXiv 2301.04104 (Nature 2025). DreamerV3 introduces symlog predictions, discrete regression critics, and fixed hyperparameters across 150+ tasks. **[support]** DreamerV3 is the primary subject of our diagnostic analysis; its trained `dt_embedding` and obs decoder gradient pathway are where we identify the CIVO mechanism.

- **Chua, Calandra, McAllister & Levine (2018).** *Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models.* NeurIPS 2018. PETS uses probabilistic ensemble dynamics with trajectory sampling for sample-efficient planning. **[contrast]** PETS uses explicit uncertainty quantification via ensembles; our work shows that implicit variance accumulation through gradient interference—not epistemic uncertainty—is the dominant failure mode in DreamerV3's imagination.

- **Janner, Fu, Zhang & Levine (2019).** *When to Trust Your Model: Model-Based Policy Optimization.* NeurIPS 2019. MBPO derives monotonic improvement bounds for model-based RL by branching short rollouts from real data, with rollout horizon bounded by model error. **[support]** MBPO's theoretical analysis formalizes how model error compounds over horizon length; our CIVO finding provides a concrete mechanistic account of *how* this compounding arises in latent-space world models through gradient-mediated representation pollution.

- **Hansen, Su & Wang (2024).** *TD-MPC2: Scalable, Robust World Models for Continuous Control.* ICLR 2024. Scales implicit (decoder-free) latent world models to 317M parameters across 104 tasks. **[contrast]** TD-MPC2 avoids observation reconstruction entirely, implicitly sidestepping the obs-decoder gradient pathway we identify as the CIVO trigger—supporting our finding that the reconstruction head is architecturally implicated.

- **Micheli, Alonso & Fleuret (2023).** *Transformers are Sample-Efficient World Models.* ICLR 2023. IRIS uses discrete autoregressive world modeling with transformers, achieving strong Atari 100K results. **[contrast]** IRIS's discrete tokenization and autoregressive architecture represent a fundamentally different gradient flow from RSSM-based models; whether analogous variance compounding occurs in transformer world models remains an open question our diagnostic framework could address.

---

## 2. Temporal Abstraction in RL

Our work examines how temporal embeddings interact with world model training; this section contextualizes temporal abstraction mechanisms.

- **Sutton, Precup & Singh (1999).** *Between MDPs and Semi-MDPs: A Framework for Temporal Abstraction in Reinforcement Learning.* Artificial Intelligence 112(1-2):181–211. The foundational options framework unifying temporally extended actions with initiation sets, policies, and termination conditions. **[support]** Provides the theoretical grounding for temporal abstraction; our `dt_embedding` can be viewed as a continuous relaxation of discrete temporal options within imagination.

- **Biedenkapp, Rajan, Hutter & Lindauer (2021).** *TempoRL: Learning When to Act.* ICML 2021. Learns adaptive action repetition via a skip network that jointly optimizes action selection and persistence duration. **[contrast]** TempoRL operates in the policy execution loop (model-free); our analysis concerns temporal embeddings within the *world model training* pipeline, where the gradient pathways create qualitatively different failure modes.

- **Gumbsch, Sajid, Martius & Butz (2024).** *Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics.* ICLR 2024. THICK learns a two-level temporal hierarchy where the lower level forms invariant contexts and the upper level predicts context-change events. **[extend]** THICK introduces temporal abstraction into world model dynamics but does not analyze how temporal conditioning interacts with multi-head decoder gradients; our CIVO diagnosis applies to any world model architecture that trains temporal embeddings through reconstruction objectives.

- **Hansen, Wang & Su (2022).** *Temporal Difference Learning for Model Predictive Control.* ICML 2022. TD-MPC combines TD learning with model predictive control, using a learned value function to extend effective planning horizon beyond explicit rollout length. **[contrast]** TD-MPC uses value bootstrapping rather than long imagination rollouts, avoiding the variance compounding regime we diagnose; this architectural choice implicitly circumvents CIVO.

---

## 3. Compounding Errors in Model-Based Rollouts

CIVO is a specific instance of error compounding; this section covers the broader literature.

- **Talvitie (2017).** *Self-Correcting Models for Model-Based Reinforcement Learning.* AAAI 2017. Analyzes hallucinated features from iterated predictions and proposes self-correcting models trained on their own multi-step outputs. **[support]** Talvitie's "hallucination" phenomenon is analogous to our CIVO: both describe how errors amplify through multi-step model application, but we identify the *gradient mechanism* (obs decoder → representation) rather than the *distributional shift* mechanism.

- **Venkatraman, Hebert & Bagnell (2015).** *Improving Multi-Step Prediction of Learned Time Series Models.* AAAI 2015. Formulates multi-step prediction as imitation learning ("Data as Demonstrator"), providing theoretical bounds on compounding error. **[support]** Provides foundational error-compounding bounds; our contribution is identifying a previously unknown compounding channel (gradient interference through temporal embeddings) that operates orthogonally to the distributional-shift channel this work addresses.

- **Lambert, Amos, Yadan & Calandra (2020).** *Objective Mismatch in Model-based Reinforcement Learning.* L4DC 2020, PMLR 120:761–770. Shows that training-loss minimization does not correlate with downstream control performance. **[support]** The objective mismatch problem is a manifestation of the multi-head optimization tension we diagnose: the obs decoder objective can improve reconstruction loss while degrading imagination quality through gradient interference.

- **Yu, Thomas, Yu, Ermon, Zou, Levine, Kumar & Finn (2020).** *MOPO: Model-based Offline Policy Optimization.* NeurIPS 2020. Uses learned uncertainty penalties to constrain policy optimization under model error. **[contrast]** MOPO addresses model error through pessimistic reward shaping; our analysis reveals that in DreamerV3, the variance problem originates not from epistemic uncertainty but from gradient-mediated representation corruption—a qualitatively different mechanism that pessimism alone cannot resolve.

- **Fröhlich, Lefarov, Zeilinger & Berkenkamp (2022).** *On-Policy Model Errors in Reinforcement Learning.* ICLR 2022. Provides tighter characterization of model error compounding under the on-policy distribution. **[extend]** Our CIVO analysis extends this line by showing that even when the model is accurate at the *one-step* level, gradient interference through the obs decoder can cause representation drift that compounds specifically during multi-step imagination.

---

## 4. Gradient Interference in Multi-Task and Multi-Objective Learning

Our core finding is that the obs decoder gradient interferes with representation quality; this section covers gradient conflict analysis more broadly.

- **Chen, Badrinarayanan, Lee & Rabinovich (2018).** *GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks.* ICML 2018. Dynamically tunes task loss weights by matching gradient norms across tasks. **[support]** GradNorm addresses gradient magnitude imbalance; our gradient decomposition analysis reveals that the obs decoder gradient has disproportionate magnitude flowing through `dt_embedding`, which GradNorm-style balancing could in principle mitigate.

- **Sener & Koltun (2018).** *Multi-Task Learning as Multi-Objective Optimization.* NeurIPS 2018. Casts multi-task learning as multi-objective optimization and uses MGDA to find Pareto-optimal updates. **[support]** Provides the theoretical framework for understanding gradient conflicts in shared-parameter architectures; our 2×2 ablation can be interpreted as testing whether the obs decoder objective is Pareto-incompatible with imagination quality.

- **Yu, Kumar, Gupta, Levine, Hausman & Finn (2020).** *Gradient Surgery for Multi-Task Learning.* NeurIPS 2020. PCGrad projects conflicting gradients to remove destructive interference between tasks. **[extend]** PCGrad surgically removes conflicting gradient components; our Full-SGS is a more aggressive intervention that *completely* blocks gradients from non-KL decoder heads into the representation, which we show is necessary because the conflict is structural (obs decoder fundamentally corrupts temporal representations), not merely directional.

- **Liu, Liu, Jin, Stone & Liu (2021).** *Conflict-Averse Gradient Descent for Multi-task Learning.* NeurIPS 2021. CAGrad minimizes average loss while regularizing for worst-case task improvement. **[extend]** CAGrad and similar methods assume all task gradients should contribute to the shared representation; our finding challenges this assumption for world model training—some gradient pathways (obs decoder → `dt_embedding`) are *categorically harmful* and should be blocked entirely.

- **Ma, Wu, Feng, Xiao, Li, Hao, Wang & Long (2024).** *HarmonyDream: Task Harmonization Inside World Models.* ICML 2024. Identifies task imbalance between observation and reward modeling in world models (including DreamerV3) and proposes dynamic loss rebalancing, achieving 10–69% gains on visual tasks. **[extend]** HarmonyDream addresses the *magnitude* of gradient conflicts in world model training through loss reweighting; our analysis goes further by identifying the specific *pathway* (`dt_embedding` → obs decoder gradient → representation pollution) responsible for CIVO and showing that reweighting alone is insufficient—stop-gradient surgery is required.

---

## 5. Plasticity Loss and Representation Degradation in Deep RL

CIVO causes progressive representation degradation during imagination; plasticity loss is a related phenomenon in the parameter space.

- **Nikishin, Schwarzer, D'Oro, Bacon & Courville (2022).** *The Primacy Bias in Deep Reinforcement Learning.* ICML 2022. Shows early training experiences dominate RL agents' learning, and periodic resets restore plasticity. **[support]** Primacy bias describes representation rigidity from early data; CIVO describes representation corruption from ongoing gradient interference—both are forms of progressive representation degradation, but with distinct causal mechanisms.

- **Lyle, Zheng, Nikishin, Pires, Pascanu & Dabney (2023).** *Understanding Plasticity in Neural Networks.* ICML 2023. Systematic analysis linking plasticity loss to dead units and weight norm growth, with layer normalization and weight decay as mitigations. **[support]** Lyle et al. diagnose plasticity loss through network-level statistics (dead units, weight norms); our analysis diagnoses representation degradation through *gradient pathway analysis* (which decoder head's gradients corrupt which embedding), offering a complementary diagnostic methodology.

- **Nikishin, Oh, Ostrovski, Lyle, Pascanu, Dabney & Barreto (2023).** *Deep Reinforcement Learning with Plasticity Injection.* NeurIPS 2023. Proposes periodically reinitializing neuron subsets while preserving learned features to maintain plasticity. **[contrast]** Plasticity injection addresses capacity loss through periodic resets; Full-SGS addresses gradient-mediated corruption through architectural gradient routing—preventing the damage rather than periodically repairing it.

- **Juliani & Ash (2024).** *A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning.* NeurIPS 2024. Extends plasticity loss findings to on-policy methods (PPO), showing the phenomenon is pervasive. **[support]** Confirms that representation degradation is widespread in deep RL; our work adds a new mechanism (gradient interference through auxiliary decoder heads) to the taxonomy of causes.

---

## 6. Representation Learning and Stop-Gradient Methods in RL

Full-SGS uses stop-gradient to prevent representation corruption; this section covers related representation learning approaches.

- **Schwarzer, Anand, Goel, Hjelm, Courville & Bachman (2021).** *Data-Efficient Reinforcement Learning with Self-Predictive Representations.* ICLR 2021. SPR learns representations by predicting future latent states with an EMA target encoder, achieving strong Atari 100K results. **[support]** SPR uses a stop-gradient target encoder to prevent representation collapse—architecturally similar to our Full-SGS, which uses stop-gradient to prevent the obs decoder from corrupting representations through `dt_embedding`. Both demonstrate that selective gradient blocking is essential for stable representation learning.

- **Tian, Chen & Ganguli (2021).** *Understanding Self-Supervised Learning Dynamics without Contrastive Pairs.* ICML 2021. Theoretical analysis of stop-gradient mechanics in self-supervised learning (e.g., BYOL/SimSiam), showing they prevent representation collapse by breaking symmetry in the loss landscape. **[support]** Provides theoretical grounding for why stop-gradient is effective; our Full-SGS can be understood through this lens—blocking obs decoder gradients breaks a harmful symmetry where the representation optimizes for reconstruction at the cost of imagination quality.

- **Guo, Thakoor, Pires et al. (2022).** *BYOL-Explore: Exploration by Bootstrapped Prediction.* NeurIPS 2022. Combines self-supervised representation learning (BYOL-style) with exploration bonuses, using prediction error in latent space as intrinsic motivation. **[contrast]** BYOL-Explore uses stop-gradient in the representation learning objective itself; our work reveals that stop-gradient is also critical in the *decoder gradient pathway* of world model training—a previously unrecognized application of the same principle.

- **Ma, Wu, Feng, Xiao, Li, Hao, Wang & Long (2024).** *HarmonyDream: Task Harmonization Inside World Models.* ICML 2024. (See §4 above.) **[extend]** HarmonyDream's finding of task imbalance in world models is the *symptom*; our gradient decomposition identifies the specific *mechanism* (obs decoder → `dt_embedding` → CIVO) and shows that stop-gradient surgery, not just loss reweighting, is needed to resolve it.

---

## 7. Positioning Statement

Our work is a **diagnostic analysis** of temporal abstraction in world-model RL, distinct from both method papers and benchmark papers. While the world model literature (§1) has focused on architectural improvements and the compounding error literature (§3) has characterized error growth theoretically, we provide the first mechanistic account of *how* trained temporal embeddings create a specific failure mode (CIVO) through gradient interactions in multi-head world model architectures. 

Unlike gradient interference work in multi-task learning (§4), which proposes general-purpose gradient surgery (PCGrad) or loss rebalancing (GradNorm, HarmonyDream), our analysis identifies a *structural* conflict: the obs decoder gradient flowing through `dt_embedding` is not merely imbalanced but categorically harmful to imagination quality. This finding is supported by a 2×2 ablation matrix (trained/fixed embedding × with/without obs-decoder gradient) and gradient decomposition, establishing a causal chain rather than a correlation.

Unlike plasticity loss diagnoses (§5), which attribute representation degradation to training dynamics (overfitting, capacity loss), we identify an *architectural* cause: the gradient pathway from the obs decoder through shared representations to the temporal embedding. Our proof-of-concept intervention (Full-SGS) is not a training trick but an architectural modification that eliminates the problematic gradient pathway entirely.

Our diagnostic methodology—combining variance tracking across imagination horizons, 2×2 factorial ablation, and per-head gradient decomposition—offers a reusable framework for analyzing representation pathologies in any multi-head world model architecture.

---

## Reference Summary Table

| # | Citation | Year | Venue | Direction | Relation |
|---|----------|------|-------|-----------|----------|
| 1 | Hafner et al. (DreamerV2) | 2021 | ICLR | World Models | support |
| 2 | Hafner et al. (DreamerV3) | 2023 | arXiv/Nature | World Models | support |
| 3 | Chua et al. (PETS) | 2018 | NeurIPS | World Models | contrast |
| 4 | Janner et al. (MBPO) | 2019 | NeurIPS | World Models | support |
| 5 | Hansen et al. (TD-MPC2) | 2024 | ICLR | World Models | contrast |
| 6 | Micheli et al. (IRIS) | 2023 | ICLR | World Models | contrast |
| 7 | Sutton et al. (Options) | 1999 | Artif. Intell. | Temporal Abstraction | support |
| 8 | Biedenkapp et al. (TempoRL) | 2021 | ICML | Temporal Abstraction | contrast |
| 9 | Gumbsch et al. (THICK) | 2024 | ICLR | Temporal Abstraction | extend |
| 10 | Hansen et al. (TD-MPC) | 2022 | ICML | Temporal Abstraction | contrast |
| 11 | Talvitie (Self-Correcting) | 2017 | AAAI | Compounding Errors | support |
| 12 | Venkatraman et al. (DaD) | 2015 | AAAI | Compounding Errors | support |
| 13 | Lambert et al. (Obj. Mismatch) | 2020 | L4DC | Compounding Errors | support |
| 14 | Yu et al. (MOPO) | 2020 | NeurIPS | Compounding Errors | contrast |
| 15 | Fröhlich et al. (On-Policy Errors) | 2022 | ICLR | Compounding Errors | extend |
| 16 | Chen et al. (GradNorm) | 2018 | ICML | Gradient Interference | support |
| 17 | Sener & Koltun (MTL-MOO) | 2018 | NeurIPS | Gradient Interference | support |
| 18 | Yu et al. (PCGrad) | 2020 | NeurIPS | Gradient Interference | extend |
| 19 | Liu et al. (CAGrad) | 2021 | NeurIPS | Gradient Interference | extend |
| 20 | Ma et al. (HarmonyDream) | 2024 | ICML | Gradient Interference | extend |
| 21 | Nikishin et al. (Primacy Bias) | 2022 | ICML | Plasticity Loss | support |
| 22 | Lyle et al. (Plasticity) | 2023 | ICML | Plasticity Loss | support |
| 23 | Nikishin et al. (Plasticity Inj.) | 2023 | NeurIPS | Plasticity Loss | contrast |
| 24 | Juliani & Ash (On-Policy Plast.) | 2024 | NeurIPS | Plasticity Loss | support |
| 25 | Schwarzer et al. (SPR) | 2021 | ICLR | Representation / SG | support |
| 26 | Tian et al. (Stop-Gradient) | 2021 | ICML | Representation / SG | support |

**Total: 26 unique references** (HarmonyDream appears in §4 and §6 but counted once; BYOL-Explore discussed in §6 as contextual reference = 27 if counted separately).
