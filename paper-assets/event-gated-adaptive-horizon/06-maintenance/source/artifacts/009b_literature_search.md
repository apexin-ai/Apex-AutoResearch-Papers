# Literature Search: Seed-Dependent Value Overestimation in MBRL

**Date**: 2026-05-14
**Context**: DreamerV3 temporal abstraction experiments show seed-dependent delusional critic collapse (seed 0) vs. transient overestimation with self-correction (seed 2).

---

## Key Findings

### Q1: Has anyone reported seed-dependent collapse/recovery in MBRL?

**Yes, partially.** No paper reports exactly our phenomenon (seed-dependent delusional critic collapse in world-model imagination), but several closely related findings exist:

- **Hussing et al. (2024)** show seed-dependent value divergence at high update ratios: some seeds diverge permanently, others recover spontaneously when sufficient "effective dimension" remains. This is the closest analog to our seed 0 (collapse) vs. seed 2 (recovery) pattern.
- **Barkley & Fridovich-Keil (2025)** forensically analyze MBPO and find that residual prediction inflates variance in learned dynamics, causing seed-sensitive training collapse. Only 5/7 MBPO runs are stable.
- **Zhang et al. (2026)** show that structured stochasticity buffers against collapse, and that performance is frequently decoupled from training stability. Low-dimensional "meta-states" precede observable collapse — this could explain why some seeds escape.
- **DreamerV3 GitHub Issue #43**: Users report non-deterministic training curves across identical seeds due to JAX compilation non-determinism.
- **DreamerV3 GitHub Issue #175**: Consistent failure (score -21) across seeds 0-4 on Atari100k Pong, suggesting some environments hit systematic collapse.

### Q2: Theoretical explanation for value overestimation self-correction?

**Partial explanations exist:**

- **Hussing et al. (2024)**: Recovery is possible when the network's effective dimension hasn't collapsed too far. New environmental data provides corrective signal. The agent "immediately starts to learn" after divergence episodes without explicit reset — matching our seed 2 behavior.
- **Zhang et al. (2026)**: Stochasticity enlarges the effective basin of attraction and smooths the local geometry, reducing susceptibility to perturbations. In RL specifically, policy entropy acts as "structured randomness" preventing premature collapse.
- **Talvitie (2017)**: Self-correcting model error bound shows that a model's ability to self-correct is more tightly related to MBRL performance than one-step prediction error.
- **Entropy regularization literature**: Entropy bonus implicitly prevents value collapse by maintaining exploration diversity, which can correct overestimated regions.

### Q3: DreamerV3 community on training variance?

- The DreamerV3 paper itself introduced symlog transforms, two-hot encoding (255 bins), percentile return normalization, and EMA critic regularization specifically to reduce training variance.
- **Liang et al. (2023)** showed these tricks transfer to PPO, confirming they are general stabilization mechanisms rather than architecture-specific.
- GitHub issues document overfitting in reconstruction/dynamics (#150) and non-determinism (#43), but no systematic study of seed-dependent value collapse in DreamerV3 imagination exists.

---

## Paper List

### A. Seed Sensitivity & Reproducibility in Deep RL

| # | paper_id | title | authors | year | venue | relevance |
|---|----------|-------|---------|------|-------|-----------|
| 1 | henderson2018deep | Deep Reinforcement Learning that Matters | Henderson P., Islam R., Bachman P., Pineau J., Precup D., Meger D. | 2018 | AAAI | Foundational work showing random seed variance can flip conclusions in deep RL; methodology framework for our multi-seed analysis |
| 2 | colas2018seeds | How Many Random Seeds? Statistical Power Analysis in Deep RL Experiments | Colas C., Sigaud O., Oudeyer P.-Y. | 2018 | arXiv:1806.08295 | Statistical framework for seed sensitivity; directly relevant to interpreting our 2-seed divergence |
| 3 | clary2018variability | Variability of Deep Reinforcement Learning Agents in Atari | Clary K., Tosch E., Foley J., Jensen D. | 2018 | NeurIPS Workshop | Documents high inter-seed variance in Atari agents; complements our finding in MBRL |

### B. Delusional Bias & Value Overestimation

| # | paper_id | title | authors | year | venue | relevance |
|---|----------|-------|---------|------|-------|-----------|
| 4 | lu2018nondelusional | Non-delusional Q-learning and Value-iteration | Lu T., Schuurmans D., Boutilier C. | 2018 | NeurIPS (Oral) | Defines delusional bias — Q-values backed up from unrealizable action sequences; our "delusional critic" is a temporal-abstraction instance of this |
| 5 | saxena2020conqur | ConQUR: Mitigating Delusional Bias in Deep Q-learning | Saxena S., Tsang A., Roosta F., Schuurmans D. | 2020 | arXiv:2002.12399 | Extends non-delusional Q-learning to deep networks via consistency penalization; relevant to potential fixes |
| 6 | nauman2024bitter | Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of RL | Nauman M., Bortkiewicz M., Miłoś P., Trzciński T., Ostaszewski M., Cygan M. | 2024 | ICML | Shows LayerNorm outperforms RL-specific overestimation fixes; properly regularized SAC matches model-based methods |

### C. Critic Collapse, Plasticity Loss & Recovery

| # | paper_id | title | authors | year | venue | relevance |
|---|----------|-------|---------|------|-------|-----------|
| 7 | hussing2024dissecting | Dissecting Deep RL with High Update Ratios: Combatting Value Divergence | Hussing M., Voelcker C., Gilitschenski I., Farahmand A., Eaton E. | 2024 | RLC | **Most relevant paper.** Shows seed-dependent value divergence with some seeds recovering spontaneously; attributes to optimizer momentum; unit-ball normalization fix |
| 8 | nikishin2022primacy | The Primacy Bias in Deep Reinforcement Learning | Nikishin E., Schwarzer M., D'Oro P., Bacon P.-L., Courville A. | 2022 | ICML | Primacy bias causes overfitting to early data with compounding degradation; periodic reset of last layers as fix; relevant to our seed 0 early lock-in |
| 9 | abbas2023plasticity | Loss of Plasticity in Continual Deep Reinforcement Learning | Abbas Z., Zhao R., Modayil J., White A., Sutton R.S. | 2023 | CoLLAs | Demonstrates plasticity loss in RL through dormant units and rank collapse; continual backpropagation as remedy |
| 10 | lyle2024plasticity | Loss of Plasticity in Deep Continual Learning | Lyle C., Zheng Z., Nikishin E., Khetarpal K., Dwaracherla V., Pascanu R., Dabney W., Rowland M. | 2024 | Nature | General theory of plasticity loss; simple continual backpropagation maintains plasticity indefinitely |
| 11 | doro2024onpolicy | A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning | D'Oro P., Schwarzer M., Nikishin E., Bacon P.-L., Bellemare M.G., Courville A. | 2024 | NeurIPS | Plasticity loss in on-policy setting; critic plasticity as pivotal factor — directly relevant since DreamerV3 trains actor-critic in imagination |

### D. Training Instability & Stochastic Collapse

| # | paper_id | title | authors | year | venue | relevance |
|---|----------|-------|---------|------|-------|-----------|
| 12 | zhang2026instability | Training Instability in Deep Learning Follows Low-Dimensional Dynamical Principles | Zhang Z., Yao Z., Li K., Yang L. | 2026 | arXiv:2601.13160 | Shows stochasticity stabilizes training; low-dim meta-states predict collapse; policy entropy prevents premature collapse in RL |
| 13 | barkley2025forensic | A Forensic Analysis of Synthetic Data in RL: Diagnosing and Solving Algorithmic Failures in MBPO | Barkley B., Fridovich-Keil D. | 2025 | arXiv:2510.01457 | Identifies residual prediction as variance inflator in MBPO causing seed-sensitive collapse; fix via direct prediction + output normalization |

### E. Self-Correcting Models & Compounding Error

| # | paper_id | title | authors | year | venue | relevance |
|---|----------|-------|---------|------|-------|-----------|
| 14 | talvitie2017selfcorrecting | Self-Correcting Models for Model-Based Reinforcement Learning | Talvitie E. | 2017 | AAAI | Model self-correction ability bounds MBRL performance better than one-step error; hallucinated replay technique |
| 15 | jiang2024compounding | A Note on Loss Functions and Error Compounding in Model-based RL | Jiang N. | 2024 | arXiv:2404.09946 | MuZero loss fails in stochastic environments; exponential sample complexity even in deterministic MDPs — relevant to imagination-based training |
| 16 | asadi2019combating | Combating the Compounding-Error Problem with a Multi-step Model | Asadi K., Misra D., Kim S., Littman M.L. | 2019 | arXiv | Multi-step prediction to reduce compounding error; directly relevant to our dt > 1 imagination steps |

### F. Adaptive Horizon & Value Estimation in MBRL

| # | paper_id | title | authors | year | venue | relevance |
|---|----------|-------|---------|------|-------|-----------|
| 17 | wang2020dmve | Dynamic Horizon Value Estimation for Model-based RL | Wang J., Zhang Q., Zhao D., Zhao M., Hao J. | 2020 | arXiv:2009.09593 | Adaptive rollout horizon based on model accuracy; fixed horizon with inaccurate model harms learning — direct connection to our adaptive dt |
| 18 | feinberg2018mve | Model-Based Value Expansion for Efficient Model-Free RL | Feinberg V., Wan A., Stoica I., Jordan M.I., Gonzalez J.E., Levine S. | 2018 | ICML | MVE uses short model rollouts for value estimation; only effective with short horizon and TD-k trick |
| 19 | pan2020rave | Efficient and Robust RL with Uncertainty-based Value Expansion | Pan F., He J., Tu D., He Q. | 2020 | arXiv:1912.05328 | RAVE: risk-averse value expansion using lower confidence bound from ensemble; relevant to mitigating value overestimation in imagination |

### G. Temporal Abstraction + World Models

| # | paper_id | title | authors | year | venue | relevance |
|---|----------|-------|---------|------|-------|-----------|
| 20 | gumbsch2024thick | Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics | Gumbsch C., Sajid N., Martius G., Butz M.V. | 2024 | ICLR (Spotlight) | THICK Dreamer: hierarchical world model with adaptive temporal abstraction; combines low-level rollouts with temporally abstract predictions for faster credit assignment |
| 21 | ahn2025ota | Option-aware Temporally Abstracted Value for Offline Goal-Conditioned RL | Ahn H., Choi H., Han J., Moon T. | 2025 | arXiv:2505.12737 | OTA contracts effective horizon via option-aware TD updates, improving advantage estimates in long-horizon regimes |
| 22 | kulkarni2016hdqn | Hierarchical Deep Reinforcement Learning: Integrating Temporal Abstraction and Intrinsic Motivation | Kulkarni T.D., Narasimhan K., Saeedi A., Tenenbaum J.B. | 2016 | NeurIPS | h-DQN: top-level learns over options/subgoals, bottom-level executes; foundational hierarchical deep RL |

### H. DreamerV3 Stability Mechanisms

| # | paper_id | title | authors | year | venue | relevance |
|---|----------|-------|---------|------|-------|-----------|
| 23 | liang2023dreamer_tricks | Reward Scale Robustness for Proximal Policy Optimization via DreamerV3 Tricks | Liang E., et al. | 2023 | NeurIPS | Validates DreamerV3 stabilization tricks (symlog, two-hot) transfer to PPO; confirms these are general mechanisms not architecture-specific |

---

## YAML Appendix (for literature_map.yaml)

```yaml
# ============================================================
# NEW: Seed-dependent value overestimation & collapse (009b search)
# ============================================================

- paper_id: henderson2018deep
  title: "Deep Reinforcement Learning that Matters"
  authors: [Henderson P., Islam R., Bachman P., Pineau J., Precup D., Meger D.]
  year: 2018
  venue: AAAI
  category: background
  role: "Foundational seed sensitivity analysis; random seed variance can flip deep RL conclusions"
  relevance_score: 3

- paper_id: lu2018nondelusional
  title: "Non-delusional Q-learning and Value-iteration"
  authors: [Lu T., Schuurmans D., Boutilier C.]
  year: 2018
  venue: NeurIPS
  category: background
  role: "Defines delusional bias in Q-learning — pathological over/under-estimation from unrealizable backed-up actions; our delusional critic is a temporal-abstraction instance"
  relevance_score: 5

- paper_id: hussing2024dissecting
  title: "Dissecting Deep RL with High Update Ratios: Combatting Value Divergence"
  authors: [Hussing M., Voelcker C., Gilitschenski I., Farahmand A., Eaton E.]
  year: 2024
  venue: RLC
  category: related-phenomenon
  role: "Seed-dependent value divergence with spontaneous recovery; optimizer momentum drives overestimation on in-distribution data; unit-ball normalization fix"
  relevance_score: 5

- paper_id: nauman2024bitter
  title: "Overestimation, Overfitting, and Plasticity in Actor-Critic: the Bitter Lesson of RL"
  authors: [Nauman M., Bortkiewicz M., Miłoś P., Trzciński T., Ostaszewski M., Cygan M.]
  year: 2024
  venue: ICML
  category: related-phenomenon
  role: "LayerNorm outperforms RL-specific overestimation fixes; properly regularized SAC matches model-based methods"
  relevance_score: 4

- paper_id: nikishin2022primacy
  title: "The Primacy Bias in Deep Reinforcement Learning"
  authors: [Nikishin E., Schwarzer M., D'Oro P., Bacon P.-L., Courville A.]
  year: 2022
  venue: ICML
  category: related-phenomenon
  role: "Overfitting to early data compounds into permanent degradation; periodic layer reset as fix; relevant to our seed 0 early lock-in hypothesis"
  relevance_score: 4

- paper_id: zhang2026instability
  title: "Training Instability in Deep Learning Follows Low-Dimensional Dynamical Principles"
  authors: [Zhang Z., Yao Z., Li K., Yang L.]
  year: 2026
  venue: "arXiv:2601.13160"
  category: related-phenomenon
  role: "Stochasticity stabilizes training; policy entropy prevents premature collapse in RL; low-dim meta-states predict collapse before it occurs"
  relevance_score: 4

- paper_id: barkley2025forensic
  title: "A Forensic Analysis of Synthetic Data in RL: Diagnosing Algorithmic Failures in MBPO"
  authors: [Barkley B., Fridovich-Keil D.]
  year: 2025
  venue: "arXiv:2510.01457"
  category: related-phenomenon
  role: "Residual prediction inflates variance causing seed-sensitive MBPO collapse; direct prediction + output normalization as fix"
  relevance_score: 4

- paper_id: talvitie2017selfcorrecting
  title: "Self-Correcting Models for Model-Based Reinforcement Learning"
  authors: [Talvitie E.]
  year: 2017
  venue: AAAI
  category: background
  role: "Model self-correction ability bounds MBRL performance better than one-step prediction error; hallucinated replay for error compounding"
  relevance_score: 3

- paper_id: jiang2024compounding
  title: "A Note on Loss Functions and Error Compounding in Model-based RL"
  authors: [Jiang N.]
  year: 2024
  venue: "arXiv:2404.09946"
  category: background
  role: "MuZero loss fails in stochastic envs with exponential sample complexity; relevant to imagination-based training with learned world models"
  relevance_score: 3

- paper_id: wang2020dmve
  title: "Dynamic Horizon Value Estimation for Model-based RL"
  authors: [Wang J., Zhang Q., Zhao D., Zhao M., Hao J.]
  year: 2020
  venue: "arXiv:2009.09593"
  category: method-component
  role: "Adaptive rollout horizon based on model accuracy; fixed horizon harms learning — direct analog to our adaptive dt mechanism"
  relevance_score: 4

- paper_id: gumbsch2024thick
  title: "Learning Hierarchical World Models with Adaptive Temporal Abstractions from Discrete Latent Dynamics"
  authors: [Gumbsch C., Sajid N., Martius G., Butz M.V.]
  year: 2024
  venue: ICLR (Spotlight)
  category: method-component
  role: "THICK Dreamer: hierarchical world model with adaptive temporal abstraction; combines low-level + temporally abstract predictions for faster credit assignment"
  relevance_score: 5

- paper_id: ahn2025ota
  title: "Option-aware Temporally Abstracted Value for Offline Goal-Conditioned RL"
  authors: [Ahn H., Choi H., Han J., Moon T.]
  year: 2025
  venue: "arXiv:2505.12737"
  category: method-component
  role: "OTA contracts effective horizon length via option-aware TD; better advantage estimates in long-horizon regimes"
  relevance_score: 3

- paper_id: doro2024onpolicy
  title: "A Study of Plasticity Loss in On-Policy Deep Reinforcement Learning"
  authors: [D'Oro P., Schwarzer M., Nikishin E., Bacon P.-L., Bellemare M.G., Courville A.]
  year: 2024
  venue: NeurIPS
  category: related-phenomenon
  role: "Critic plasticity loss as pivotal factor in training degradation; relevant to DreamerV3 imagination-trained critic"
  relevance_score: 3

- paper_id: lyle2024plasticity
  title: "Loss of Plasticity in Deep Continual Learning"
  authors: [Lyle C., Zheng Z., Nikishin E., Khetarpal K., et al.]
  year: 2024
  venue: Nature
  category: background
  role: "General theory of plasticity loss; continual backpropagation maintains plasticity indefinitely"
  relevance_score: 3

- paper_id: liang2023dreamer_tricks
  title: "Reward Scale Robustness for PPO via DreamerV3 Tricks"
  authors: [Liang E., et al.]
  year: 2023
  venue: NeurIPS
  category: background
  role: "Validates DreamerV3 symlog/two-hot stabilization tricks transfer to PPO; confirms they are general mechanisms"
  relevance_score: 2

- paper_id: saxena2020conqur
  title: "ConQUR: Mitigating Delusional Bias in Deep Q-learning"
  authors: [Saxena S., Tsang A., Roosta F., Schuurmans D.]
  year: 2020
  venue: "arXiv:2002.12399"
  category: background
  role: "Extends non-delusional Q-learning to deep networks via consistency penalization; potential fix direction for delusional critic"
  relevance_score: 3
```

---

## Synthesis & Implications for Our Work

**Our seed-dependent delusional critic collapse is novel but well-supported by adjacent findings:**

1. **The collapse mechanism** aligns with Lu et al.'s delusional bias theory: the dt_embedding learns to request long imagination steps, but the RSSM can't deliver accurate multi-step predictions, so the critic backs up values from "delusional" trajectories. This is conceptually identical to backing up values from unrealizable actions.

2. **The seed-dependence** is consistent with Hussing et al.'s finding that value divergence is seed-dependent, driven by optimizer momentum accumulation. Early trajectory of the dt_embedding likely determines whether the system enters a delusional basin (seed 0) or escapes via sufficient exploration stochasticity (seed 2).

3. **The self-correction in seed 2** matches the "spontaneous recovery" documented by Hussing et al.: when effective network dimension hasn't collapsed too far, new environmental data provides corrective signal. Zhang et al.'s theory about stochasticity enlarging basins of attraction provides a mechanistic explanation.

4. **The THICK Dreamer work** (Gumbsch et al. 2024) is the closest architectural analog — they also combine temporal abstraction with world-model imagination, but use discrete context boundaries rather than learned continuous dt. Their approach sidesteps the delusional critic problem by using categorical temporal abstraction rather than a trainable embedding.

**Novelty claim**: No existing work reports delusional critic collapse specifically arising from a learned temporal abstraction embedding in world-model imagination. The closest is Hussing et al.'s seed-dependent value divergence, but in model-free settings with high UTD ratios, not in imagination-based MBRL with temporal abstraction.
