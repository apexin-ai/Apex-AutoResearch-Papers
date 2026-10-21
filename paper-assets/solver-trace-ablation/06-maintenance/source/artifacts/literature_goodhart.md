# Goodhart's Law in RL — Literature Survey

## Category 1: Reward Overoptimization in RLHF

### Core Papers

- **Scaling Laws for Reward Model Overoptimization** (Gao, Schulman & Hilton, 2023, ICML)
  - Key finding: Gold reward initially increases then decreases as optimization against proxy RM intensifies — direct empirical Goodhart demonstration. The overoptimization relationship follows different functional forms for RL vs. best-of-n, coefficients scale smoothly with RM parameter count. KL penalties increase achievable proxy reward at a given KL but do not improve the gold-reward frontier.
  - Relevance: Foundational paper. Our ISR dose-response (β=0.1 helps, β=0.3 hurts) is a precise instance of their inverted-U curve, but in a neurosymbolic verification setting rather than language preference.
  - BibTeX key: `gao2023scaling`

- **Defining and Characterizing Reward Hacking** (Skalse, Howe, Krasheninnikov & Krueger, 2022, NeurIPS)
  - Key finding: First formal definition of reward hacking. Proves that for stochastic policies, non-trivial unhackable proxy-true reward pairs do not exist (unless one is constant). Establishes reward hacking as a near-universal theoretical concern.
  - Relevance: Provides the theoretical impossibility result that frames why our ISR hacking is expected, not anomalous.
  - BibTeX key: `skalse2022defining`

- **Categorizing Variants of Goodhart's Law** (Manheim & Garrabrant, 2019, arXiv)
  - Key finding: Four-part taxonomy: (1) Regressional — extreme proxy values overestimate true goal; (2) Extremal — proxy-goal relationship breaks in OOD regions; (3) Causal — non-causal correlations fail under intervention; (4) Adversarial — optimization creates gaming incentives.
  - Relevance: Our high-β ISR collapse is best classified as extremal Goodhart (policy moves to OOD region where ISR↑ but PR↓). Provides vocabulary for discussion section.
  - BibTeX key: `manheim2019categorizing`

- **The Effects of Reward Misspecification: Mapping and Mitigating Misaligned Models** (Pan, Bhatia & Steinhardt, 2022, ICLR)
  - Key finding: Across 9 environments, more capable agents exploit misspecifications more. Observes dose-dependent degradation — capability thresholds where true reward sharply drops. Proposes anomaly detection as mitigation.
  - Relevance: Their dose-dependent degradation pattern matches our β=0.1→0.3 qualitative shift. More capable optimization = worse outcome under misspecification.
  - BibTeX key: `pan2022effects`

- **Confronting Reward Model Overoptimization with Constrained RLHF** (Moskovitz, Singh, Strouse et al., 2024, ICLR Spotlight)
  - Key finding: First study of overoptimization in composite reward models. Correlation between component RMs affects overoptimization onset. Proposes constrained RL to prevent exceeding each component's "threshold of usefulness."
  - Relevance: Directly applicable — our setup combines exec reward + ISR reward. Their "threshold of usefulness" concept maps to our optimal β.
  - BibTeX key: `moskovitz2024confronting`

- **Catastrophic Goodhart: Regularizing RLHF with KL Divergence Does Not Mitigate Heavy-Tailed Reward Misspecification** (Kwa, Thomas & Garriga-Alonso, 2024, NeurIPS)
  - Key finding: If reward model error is heavy-tailed, policies can achieve arbitrarily high proxy reward with no true utility gain. KL regularization provably fails under heavy-tailed misspecification.
  - Relevance: Raises the question of whether our ISR error distribution is heavy-tailed — if so, explains why KL penalty alone cannot prevent collapse at high β.
  - BibTeX key: `kwa2024catastrophic`

### Survey & Background

- **Concrete Problems in AI Safety** (Amodei, Olah, Steinhardt et al., 2016, arXiv)
  - Key finding: Identifies reward hacking as one of five practical AI safety problems. Discusses exploitation through environmental complexity and hard-to-formalize concepts.
  - Relevance: Classic framing paper; establishes reward hacking as a recognized AI safety concern.
  - BibTeX key: `amodei2016concrete`

- **Open Problems and Fundamental Limitations of RLHF** (Casper et al., 2023, TMLR)
  - Key finding: Comprehensive survey. Identifies reward overoptimization as core RLHF failure mode where proxy-aligned policy regresses on true generalization.
  - Relevance: Provides survey context; our work adds a neurosymbolic case study to their taxonomy.
  - BibTeX key: `casper2023open`

- **Consequences of Misaligned AI** (Zhuang & Hadfield-Menell, 2020, NeurIPS)
  - Key finding: When agent's reward covers J < L true features, optimizing proxy reliably loses principal utility. Formal Goodhart demonstration from incomplete objectives.
  - Relevance: ISR captures one aspect of formalization quality but not all — incomplete proxy, consistent with their framework.
  - BibTeX key: `zhuang2020consequences`

- **Reward Tampering Problems and Solutions in RL** (Everitt, Hutter, Kumar & Krakovna, 2021, Synthese)
  - Key finding: Distinguishes reward tampering (agent modifies own reward signal) from reward hacking (exploiting proxy misspecification) via causal influence diagrams.
  - Relevance: Helps clarify that our phenomenon is proxy misspecification (hacking), not tampering.
  - BibTeX key: `everitt2021reward`

---

## Category 2: Verification-Based Reward Signals

### Formal Verification as Reward

- **RLSF: Reinforcement Learning via Symbolic Feedback** (Jha et al., 2024, arXiv)
  - Key finding: Symbolic reasoning tools (solvers, provers) provide fine-grained, token-level feedback via poly-sized certificates. Outperforms traditional approaches on program synthesis (+31.4%), chemistry (+5.5-33.7%), and Game of 24 (+25%). Smaller RLSF models outperform GPT-4.
  - Relevance: Most directly relevant — uses solver/prover certificates as reward signal, same paradigm as our ISR. They show it works; we show when it breaks (Goodhart).
  - BibTeX key: `jha2024rlsf`

- **FoVer: Generalizable Process Reward Models via Formally Verified Training Data** (Kamoi et al., 2025, Findings of ACL 2026)
  - Key finding: Uses Z3 and Isabelle to synthesize PRM training data by annotating step-level error labels. Eliminates human annotation. Competitive results on ProcessBench and 12 reasoning benchmarks.
  - Relevance: Uses formal verification tools (including Z3, same family as our solver) to generate training signal. Shows verification-based rewards work — we extend by showing dose-response dynamics.
  - BibTeX key: `kamoi2026fover`

- **SatLM: Satisfiability-Aided Language Models Using Declarative Prompting** (Ye et al., 2023, NeurIPS)
  - Key finding: LLM generates declarative specifications; automated theorem prover derives final answer. Outperforms imperative approaches by 23% on GSM hard subset.
  - Relevance: Establishes solver-as-verifier paradigm at inference time. Our work uses it at training time as reward.
  - BibTeX key: `ye2023satlm`

### Proof Assistants as Reward (Math Reasoning)

- **DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for RL and MCTS** (DeepSeek AI, 2024, ICLR 2025)
  - Key finding: Uses GRPO with Lean 4 verification as binary reward. Achieves 63.5% on miniF2F.
  - Relevance: Same algorithm (GRPO) + formal verification reward, but binary (pass/fail). Our ISR is graded, which creates more Goodhart surface.
  - BibTeX key: `deepseekprover2024v15`

- **AlphaProof** (Google DeepMind, 2024, Nature 2025)
  - Key finding: AlphaZero-inspired RL with Lean proof verification. Silver medal at IMO 2024. Binary correctness guarantee via formal verification.
  - Relevance: Demonstrates verification-reward RL at scale. Binary reward avoids the Goodhart problem we identify with graded metrics.
  - BibTeX key: `alphaproof2024`

- **Let's Verify Step by Step** (Lightman et al., 2023, ICLR 2024)
  - Key finding: Process supervision (step-level rewards) significantly outperforms outcome supervision on MATH. Released PRM800K.
  - Relevance: Establishes that finer-grained verification signals improve training — our ISR is a form of process-level verification reward.
  - BibTeX key: `lightman2024lets`

- **Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations** (Wang, Li et al., 2023, ACL 2024)
  - Key finding: Automatically constructs process supervision data. Used as both verifier and step-by-step PPO reward model. Improved Mistral-7B on GSM8K (77.9→84.1%) and MATH (28.6→33.0%).
  - Relevance: Automated verification reward without human labels, similar to our automated ISR computation.
  - BibTeX key: `wang2024mathshepherd`

### Code Execution as Reward

- **CodeRL: Mastering Code Generation through Pretrained Models and Deep RL** (Le et al., 2022, NeurIPS)
  - Key finding: Actor-critic framework with unit test execution as reward signal. Token-level value estimation guides fine-tuning.
  - Relevance: Execution-based verification reward for code; our ISR is solver-based verification for logical formalization.
  - BibTeX key: `le2022coderl`

- **RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning** (Gehring et al., 2024, ICML 2025)
  - Key finding: End-to-end RL with code execution feedback as reward. Large gains on competitive programming with 8B and 70B models.
  - Relevance: Shows verification-based RL scales; raises question of whether Goodhart effects emerge at larger scale.
  - BibTeX key: `gehring2024rlef`

### GRPO with Verifiable Rewards

- **DeepSeek-R1: Incentivizing Reasoning Capability via Reinforcement Learning** (DeepSeek AI, 2025, Nature 2025)
  - Key finding: Pure RLVR using GRPO produces emergent reasoning without human-labeled traces. Binary rewards from string matching (math) and unit tests (code).
  - Relevance: Demonstrates GRPO + verifiable reward at scale. Binary reward sidesteps the graded-metric Goodhart risk we identify.
  - BibTeX key: `deepseekr1_2025`

- **DeepSeekMath: Pushing the Limits of Mathematical Reasoning** (Shao et al., 2024, arXiv)
  - Key finding: Introduced GRPO — estimates advantages via Monte Carlo rollouts within groups, eliminating the critic model.
  - Relevance: The algorithm we use. Understanding GRPO mechanics is key to explaining why ISR reward interacts with it as it does.
  - BibTeX key: `shao2024deepseekmath`

---

## Category 3: Auxiliary Reward Dose-Response

### KL/Beta Scaling Laws

- **Scaling Laws for Reward Model Overoptimization in Direct Alignment Algorithms** (Rafailov, Chittepu, Park et al., 2024, NeurIPS)
  - Key finding: Extends Gao et al. to DPO/IPO/SLiC. Tests seven beta values across 1B-6.9B models. DAAs still overoptimize despite no explicit proxy RM. Smaller models overoptimize sooner.
  - Relevance: Direct evidence that beta-controlled dose-response is a general phenomenon, not specific to PPO-style RLHF. Validates studying β as a "dose" parameter.
  - BibTeX key: `rafailov2024scaling`

- **Correcting the Mythos of KL-Regularization: Chi-Squared Preference Optimization** (Huang et al., 2025, ICLR 2025 Poster)
  - Key finding: KL-regularization is theoretically inadequate for preventing overoptimization. Chi-squared divergence provably alleviates it.
  - Relevance: Suggests that even with KL penalty in GRPO, overoptimization (our high-β collapse) is theoretically expected. Alternative divergence measures could help.
  - BibTeX key: `huang2025correcting`

- **Provably Mitigating Overoptimization in RLHF** (Liu et al., 2024, NeurIPS)
  - Key finding: Distributional shift causes overoptimization. SFT loss acts as pessimistic regularizer against spuriously high proxy rewards.
  - Relevance: Our high-β ISR collapse may involve distributional shift — policy moves to regions where ISR is high but quality is low.
  - BibTeX key: `liu2024provably`

### Multi-Objective Reward Weighting

- **Multi-Objective Direct Preference Optimization (MODPO)** (Zhou, Li et al., 2024, Findings of ACL)
  - Key finding: Extends DPO to multiple alignment objectives. Produces Pareto fronts showing how objective weight ratios control safety-helpfulness trade-off.
  - Relevance: Our exec+ISR is a multi-objective problem. MODPO's Pareto analysis framework could formalize our β sweep results.
  - BibTeX key: `zhou2024modpo`

- **ArmoRM: Interpretable Preferences via Multi-Objective Reward Modeling and MoE** (Wang, Xiong et al., 2024, Findings of EMNLP)
  - Key finding: MoE gating auto-selects reward objective weights per context. Fixed uniform weights are suboptimal.
  - Relevance: Suggests per-instance β (rather than fixed β) could avoid Goodhart effects.
  - BibTeX key: `wang2024armorm`

- **Reward Model Ensembles Help Mitigate Overoptimization** (Coste et al., 2023, NeurIPS Workshop)
  - Key finding: Worst-case optimization across RM ensembles practically eliminates overoptimization for BoN and reduces it for PPO.
  - Relevance: Ensemble approach as mitigation; could apply to our ISR (multiple solver metrics instead of one).
  - BibTeX key: `coste2023reward`

### Adaptive Auxiliary Reward Weighting

- **Learning to Utilize Shaping Rewards (BiPaRS)** (Hu et al., 2020, NeurIPS)
  - Key finding: Bi-level optimization learns parameterized shaping reward weights. Can even transform harmful shaping rewards into beneficial ones by learning negative weights.
  - Relevance: Directly addresses our problem — when auxiliary reward (ISR) weight is wrong, automated weight learning could find optimal β.
  - BibTeX key: `hu2020bipars`

- **Reward Training Wheels: Adaptive Auxiliary Rewards for Robotics RL** (Wang, Xu et al., 2025, IROS)
  - Key finding: Teacher dynamically adjusts auxiliary reward weights based on student's evolving capabilities. Optimal auxiliary weight is stage-dependent.
  - Relevance: Suggests β should decrease during training as the policy improves — matches intuition that ISR is useful early but harmful when over-optimized.
  - BibTeX key: `wang2025reward`

- **Automatic Successive RL with Multiple Auxiliary Rewards (ASR)** (Fu, Zhan et al., 2019, IJCAI)
  - Key finding: Fixed linear scalarization is suboptimal; ASR dynamically selects which auxiliary reward to emphasize at each training stage.
  - Relevance: Supports the idea that a fixed β throughout training is inherently limited.
  - BibTeX key: `fu2019automatic`

- **Adaptive Reward Scaling for Multi-Task RL (ARS)** (Cho, Park, Kim & Sung, 2025, ICML)
  - Key finding: History-based reward scaling ensures balanced reward distributions across tasks. Unbalanced magnitudes cause catastrophic interference.
  - Relevance: Our ISR at high β may dominate the exec reward signal, causing the catastrophic PR collapse we observe.
  - BibTeX key: `cho2025ars`

- **UNREAL: RL with Unsupervised Auxiliary Tasks** (Jaderberg et al., 2017, ICLR)
  - Key finding: Foundational auxiliary-task paper. Auxiliary task weights (λ) are domain-dependent; different ranges needed for different environments.
  - Relevance: Classic reference establishing that auxiliary reward weight tuning is critical and domain-specific.
  - BibTeX key: `jaderberg2017unreal`

### GRPO-Specific

- **DAPO: An Open-Source LLM Reinforcement Learning System at Scale** (Yu et al., ByteDance, 2025, arXiv)
  - Key finding: Four techniques for stable multi-component reward: Clip-Higher, Dynamic Sampling, token-level policy gradient, Overlong Reward Shaping with soft punishment.
  - Relevance: GRPO variant with multiple reward components; their techniques address stability issues relevant to our multi-reward setup.
  - BibTeX key: `yu2025dapo`

---

## Positioning Summary

### Novelty (what we contribute that prior work doesn't cover)

1. **First Goodhart characterization in neurosymbolic verification rewards**: Prior work studies reward hacking in language preference RMs (Gao et al.), game environments (Pan et al.), or code execution (CodeRL). No one has studied Goodhart effects when a logical solver's output is used as RL reward signal.

2. **Dose-response curve for verification-based auxiliary reward**: We provide the first empirical β sweep showing inverted-U behavior specifically for a solver-based metric (ISR). Prior dose-response studies are in RLHF preference settings (Rafailov et al.) or robotics (Wang et al.), not formal verification.

3. **Dose-dependent qualitative shift**: Our β=0.1→0.3 transition shows a qualitative shift (PR 81%→18%), not a smooth degradation. This connects to Pan et al.'s dose-dependent dynamics but in a neurosymbolic context. (Note: only 2 β values tested; finer-grained β sweep needed to characterize the transition shape.)

### Citable Support (what prior work validates)

- **Inverted-U is a known pattern**: Gao et al. 2023, Rafailov et al. 2024 establish this for RLHF; we confirm it extends to solver-based rewards.
- **Proxy hacking is theoretically inevitable**: Skalse et al. 2022 prove no non-trivial unhackable proxy exists; our ISR hacking is a predicted consequence.
- **Goodhart taxonomy applies**: Manheim & Garrabrant 2019 — our case is extremal/causal Goodhart.
- **Verification rewards work at low dose**: Lightman et al. 2024, RLSF 2024, Math-Shepherd 2024 show verification signals improve training; consistent with our β=0.1 result.
- **Composite rewards need careful balancing**: Moskovitz et al. 2024 show correlation between reward components affects overoptimization onset.

### Anticipated Reviewer Questions

1. **"Why not use binary ISR instead of graded?"** — Binary (solved/unsolved) would likely avoid Goodhart but lose the richer training signal. This is an explicit trade-off we should discuss citing DeepSeek-Prover/AlphaProof (binary works) vs. Lightman/Math-Shepherd (graded is richer).

2. **"How does this relate to Gao et al. scaling laws?"** — Our β sweep is analogous to their KL sweep. We should plot our results in their framework (gold reward vs. proxy optimization intensity).

3. **"Why not use adaptive β?"** — BiPaRS, ASR, ARS show adaptive weighting outperforms fixed. We should acknowledge this as future work and cite these papers.

4. **"Is this just reward shaping gone wrong?"** — Partially, but it's specifically Goodhart (measure→target→ceases to be good measure), not generic reward shaping failure. Manheim & Garrabrant's taxonomy helps distinguish.

5. **"What's the Goodhart mechanism — regressional, extremal, causal, or adversarial?"** — Likely extremal (policy finds OOD region where ISR↑ but quality↓) with possible causal component (ISR correlates with quality in training distribution but the correlation breaks under optimization pressure).

---

## Discussion / Future Work

- **Graded vs. binary verification reward susceptibility**: Our results suggest that graded metrics (ISR) may be more Goodhart-susceptible than binary verification (pass/fail used by DeepSeek-Prover, AlphaProof, DeepSeek-R1). However, we have not run a binary ISR ablation to test this directly. A controlled comparison — graded ISR vs. binarized ISR (threshold at ISR>0) at the same β — would be needed to substantiate this claim. Until such evidence exists, this remains a hypothesis for future work.
