# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-13 (UTC).** ## Original idea { "tit

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 8
- **Original source:** `logs/chats/exported-trajectories/account-2/4e300a02-b1f1-43f9-b3ff-536ae7295d96.jsonl`
- **Structured JSON:** [`f5a99436431d9fc71453.json`](../../sessions/f5/f5a99436431d9fc71453.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-13T11:40:38.217Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-13T11:40:38.217Z",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-13 (UTC).**\n\n## Original idea\n{\n  \"title\": \"When to Filter, When to Weight: A Bias-Variance Framework for Adaptive Demo Curation\",\n  \"core_problem\": \"Given a quality scoring function for robot demonstrations, should training signals be binarized (keep/discard) or used as continuous weights? The demo curation field has produced 15+ methods in 2024–2026, each making an ad hoc choice: SCIZOR and Demo-SCORE use binary filtering, TOPReward and VACO use continuous weighting, and SARM/RA-BC (ICLR 2026) uses a hybrid with adaptive threshold parameters but a fixed functional form. While the general ML literature offers relevant theory — An et al. (ICLR 2021) prove resampling outperforms reweighting under SGD dynamics, Byrd & Lipton (ICML 2019) show diminishing weighting effects in overparameterized networks — these results address the optimizer level (SGD) but not the estimator level: whether the quality scores themselves are precise enough to justify continuous use. The choice between filtering and weighting remains ad hoc and disconnected from the properties of the specific quality estimator being used.\",\n  \"opportunity\": \"The proliferation of diverse quality estimators — Q-function advantages (IQL), temporal contrastive encoders (VIP, R3M), smoothness metrics (RINSE SAL/TED), VLM reward models, and influence functions — makes this question increasingly urgent. These estimators differ fundamentally in their noise properties: IQL Q-values arise from bootstrapped TD learning that amplifies estimation errors across Bellman backups; VIP/R3M scores come from frozen pretrained encoders with stable supervised/contrastive objectives; RINSE smoothness metrics are deterministic functions of trajectory geometry. Our key insight is that the reliability of ordinal information in quality scores — measurable as rank-order stability under bootstrap resampling — is the primary factor governing whether binary filtering or continuous weighting is optimal. This connects to a classical intuition: noisy estimates are better thresholded (only the sign/rank-class matters), while precise estimates should be used continuously (preserving ordinal information). Unlike prior work that provides better scores (SCIZOR, RINSE, QoQ) or proposes a specific weighting scheme (SARM/RA-BC, CWBC), we address the orthogonal question of what to DO with any given set of scores. The opportunity is twofold: (a) a theoretical decomposition of weighted BC suboptimality into strategy-specific terms that reveals the estimator-property dependence, and (b) a practical adaptive algorithm that measures score reliability and automatically selects the appropriate strategy.\",\n  \"landscape\": \"Demo curation for robot learning is an extremely active area with 15+ papers at top venues in 2024–2026.\\n\\n**Binary filtering methods**: SCIZOR (ICRA 2026) uses a self-supervised temporal distance classifier for binary keep/discard, achieving 15.4% average improvement (5.4% RoboMimic, 8.1% OXEMagic, 32.9% Sirius-Fleet). Demo-SCORE (RSS 2025) trains a success/failure classifier from online rollouts, achieving 15–35% higher success rate.\\n\\n**Continuous/weighted methods**: TOPReward (Feb 2026) extracts task progress from VLM token logits for advantage-weighted BC. VACO (ICLR 2025) uses a meta-scoring network with value alignment for weighted BC via bi-level optimization.\\n\\n**Hybrid filtering+weighting**: SARM/RA-BC (ICLR 2026) introduces a hybrid weight formula w_i = 1{r̂_i > κ} + 1{0 ≤ r̂_i ≤ κ} · w̃_i where w̃_i = clip((r̂_i − (μ−2σ))/(4σ+ε), 0, 1), with κ derived adaptively from running statistics of progress deltas. This is the closest work to ours: it adapts threshold parameters within a FIXED functional form (always hybrid), whereas we select the functional form itself (binary vs. continuous) based on measured estimator properties.\\n\\n**Quality-quantity analysis**: RINSE (ICML 2025 Workshop, DataWorld) derives E(k) ≈ σ̄²(k) + C·d/(kT), decomposing error into a noise floor (reduced by filtering) and a statistical estimation term (increased by reducing data), and uses smoothness-based metrics for both binary filtering and continuous exponential weighting w(τ)=exp(−λq(τ)). However, this analysis applies only to smoothness metrics, does not compare across estimator classes, and provides no decision rule for when each strategy is optimal. Our framework subsumes RINSE's decomposition as a special case (smoothness estimators, single-class) while extending to the multi-estimator adaptive setting with a principled selection criterion.\\n\\n**Prior work on filtering vs. weighting**: AFBC (Grigsby & Qi, arXiv 2021) tested binary AND exponential AWR weighting for BC with Q-function advantages, finding binary more robust. They attributed this to temperature sensitivity ('a change in β is enough to take us from near-failure to state-of-the-art performance') and advantage concentration near zero. Our framework offers a deeper explanation: Q-function advantages from bootstrapped TD have high score variance and low rank-order stability, which our analysis predicts should favor binarization.\\n\\n**General ML theory**: An et al. (ICLR 2021) prove resampling outperforms reweighting under SGD dynamics via dynamical stability analysis — a strong prior FAVORING filtering. However, their analysis operates at the optimizer level (SGD trajectory stability) and does not account for estimator-level signal quality. Our framework adds an orthogonal factor: when estimator variance is sufficiently low, the ordinal information preserved by continuous weights can compensate for the SGD-level disadvantage, a prediction we test empirically with VIP/R3M encoders. Byrd & Lipton (ICML 2019) show importance weighting has diminishing effects in overparameterized networks. 'Why Less is More (Sometimes)' (ICLR 2026) derives phase transitions for data pruning quantity but does not address the filter-vs-weight modality. CWBC (arXiv 2022) proposes trajectory weighting with conservative regularization but does not derive when filtering outperforms weighting. Density-Ratio Weighted BC (Oct 2025) provides finite-sample bounds for weighted BC assuming known density ratios, not noisy quality estimators.\\n\\n**Policy-aware methods**: DataMIL (2025) uses datamodels for end-to-end data selection on OXE. CUPID (CoRL 2025) and QoQ (ICRA 2026) use influence functions for per-sample curation.\\n\\n**Critical gap**: Despite this extensive literature, no existing work (1) derives a suboptimality decomposition for weighted BC that separately characterizes the regimes where binary filtering vs. continuous weighting is tighter, (2) empirically demonstrates that estimator-level score reliability (not just score quality) predicts the optimal strategy, or (3) provides an adaptive algorithm that selects between strategies based on measured estimator properties. SARM/RA-BC adapts parameters within a fixed hybrid form; our contribution is selecting the form itself.\",\n  \"approach\": \"We propose Variance-Guided Demo Curation (VGDC), a framework with two co-primary contributions — a theoretical decomposition and an empirical characterization — synthesized into a practical adaptive algorithm.\\n\\n**Co-Primary Contribution A: Bias-Variance Decomposition for Weighted BC**. We derive a novel decomposition of weighted BC suboptimality that reveals why different quality estimators favor different strategies. Consider a dataset {τ_i}_{i=1}^N of demonstrations with true quality f*(τ_i) and estimated quality f(τ_i) = f*(τ_i) + ε_i. For binary filtering at threshold c, the suboptimality decomposes as:\\n\\nR_filter ≤ P(sign(f(τ)−c) ≠ sign(f*(τ)−c)) · Δ_q + d/(k·m)\\n\\nwhere the first term is the misclassification rate at the decision boundary (misclassifying good demos as bad or vice versa) scaled by the quality impact Δ_q, and the second term is the estimation error from the reduced dataset of size k. For continuous weighting with w_i ∝ exp(f(τ_i)/T), the suboptimality decomposes as:\\n\\nR_weight ≤ C · σ_f²/T + α · T + d/N_eff(T)\\n\\nwhere σ_f² = E[ε²] is the estimator MSE amplified through weights (noise amplification term), α·T captures the bias from temperature smoothing (higher T → more uniform → more bias from including low-quality demos), and N_eff(T) is the effective sample size under the weight distribution. The key structural difference: binary filtering suboptimality depends on noise at the DECISION BOUNDARY (only misclassifications matter — a local property), while continuous weighting suboptimality depends on GLOBAL noise properties (all scores contribute to weight errors). This explains why high-variance estimators favor filtering (most noise is away from the boundary and doesn't affect the binary decision) while low-variance estimators favor weighting (precise ordinal information is preserved). The optimal temperature T* that minimizes R_weight satisfies T* ∝ σ_f (noisier estimators require higher temperature, which reduces noise amplification but increases bias — eventually, binary filtering dominates). We provide a proof sketch in the main paper and full proofs in the appendix.\\n\\nThis decomposition is distinct from and complementary to: An et al.'s SGD dynamics analysis (optimizer-level; our analysis is estimator-level), RINSE's E(k) formula (single-estimator special case without strategy comparison), CWBC's trajectory weighting (proposes a scheme but doesn't derive when filtering wins), and Density-Ratio Weighted BC (assumes known density ratios, not noisy quality scores). We explicitly show that RINSE's E(k) ≈ σ̄²(k) + C·d/(kT) is recovered as a special case of our R_filter bound for deterministic smoothness estimators (σ_f = 0, no misclassification noise, only data quantity tradeoff).\\n\\n**Co-Primary Contribution B: Empirical Characterization Across 3 Estimator Classes**. We conduct the first systematic measurement of quality score reliability across three classes that span the variance spectrum: (1) IQL Q-function advantages — high variance from bootstrapped TD learning where Bellman backup errors compound across iterations, with known issues of Q-value overestimation and concentration near zero (as documented by Grigsby & Qi); (2) VIP/R3M temporal contrastive encoders — low variance from frozen pretrained representations trained with stable contrastive/supervised objectives on large video datasets (Ego4D); (3) RINSE smoothness metrics (SAL, TED) — moderate variance, deterministic functions of trajectory geometry but sensitive to trajectory segmentation. For each estimator class, we measure: (a) rank-order stability via bootstrap Kendall's τ (the primary reliability metric), (b) score variance across dataset subsamples, (c) calibration (correlation between estimated and true quality). The central empirical result: estimators with low rank stability (IQL, expected τ̄ ≈ 0.4–0.6) consistently favor binary filtering, while estimators with high rank stability (VIP/R3M, expected τ̄ ≈ 0.85–0.95) favor continuous weighting, with smoothness metrics (expected τ̄ ≈ 0.7–0.8) falling near the crossover region.\\n\\n**Critical empirical test of the An et al. tension**: We directly address the strongest theoretical objection. An et al. prove resampling > reweighting in general under SGD. We show that for VIP/R3M scores (low variance, high rank stability), continuous weighting outperforms binary filtering DESPITE the SGD dynamics favoring resampling. This demonstrates that estimator-level signal quality can overcome the optimizer-level disadvantage — a novel empirical result that extends the An et al. framework.\\n\\n**Practical Adaptive Algorithm (3 stages)**:\\n(1) Score: Compute per-transition quality scores using any pretrained estimator. We demonstrate with frozen VIP/R3M embeddings (cosine similarity to goal embedding) and IQL Q-values (pretrained on the same dataset) — no from-scratch training required.\\n(2) Adapt: Estimate score reliability via bootstrap rank stability. Draw B=50 bootstrap resamples of the score vector, compute pairwise Kendall's τ, and take the mean τ̄. If τ̄ > τ_crit, select continuous softmax weighting with temperature T = c · σ_f (where c is calibrated via held-out validation, and σ_f is the bootstrap-estimated score standard deviation); if τ̄ ≤ τ_crit, select binary filtering at the median-split threshold. We ablate over: (a) the threshold τ_crit ∈ {0.6, 0.7, 0.8}, (b) alternative reliability metrics (coefficient of variation σ_f/|μ_f|, split-half correlation), and (c) temperature schedules (T = c·σ_f vs. T = c·σ_f·sqrt(log N) vs. cross-validated T). This replaces the previously proposed Hartigan's dip test, which measures score bimodality — a property disconnected from the theoretical decomposition. Rank stability directly measures ordinal information reliability, which is what the theory says determines the filter-vs-weight choice.\\n(3) Train: Fine-tune the policy (diffusion policy or OpenVLA-OFT with LoRA) using the selected weighted/filtered BC loss.\\n\\n**Robustness to partial hypothesis support**: Even if the variance-performance correlation is imperfect across all estimator classes (e.g., R² < 0.5), we add a fallback experiment: the adaptive algorithm vs. any fixed strategy (always-filter, always-weight) across the full estimator × task grid. The adaptive algorithm should match or outperform the best fixed strategy because it can select per-estimator. This gives a weaker but still valuable result: 'measuring score reliability and adapting never hurts, even if variance is an imperfect predictor.'\\n\\n**Evaluation (CoRL-scope)**: Evaluate on RoboMimic (5 tasks: Lift, Can, Square, Transport, ToolHang) and LIBERO-Long (10 tasks) using diffusion policy as the primary backbone and OpenVLA-OFT as secondary. Compare against: (a) unweighted BC (no curation), (b) SCIZOR binary filtering, (c) RINSE SAL/TED filtering and weighting, (d) SARM/RA-BC fixed hybrid, (e) fixed-binary and fixed-continuous baselines with our scores. Critical experiments:\\n(i) Binary vs. continuous with SAME scores across all 3 estimator classes — the central experiment isolating the strategy question.\\n(ii) Rank stability vs. performance correlation: for each estimator × task, measure τ̄ and plot against the relative performance gap of binary vs. continuous.\\n(iii) Adaptive selection accuracy: prediction accuracy of the τ̄-based criterion.\\n(iv) Adaptive vs. fixed strategies: show VGDC ≥ max(always-filter, always-weight) across the full grid.\\n(v) Ablation on reliability metrics, temperature formulas, and bootstrap parameters.\\n(vi) Direct test of An et al. tension: VIP/R3M continuous weighting vs. binary filtering.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~120h A100-80GB (scoring: ~3h forward passes across 3 estimator classes on RoboMimic+LIBERO using frozen checkpoints, policy training: ~8h/run × 10 runs for binary/continuous × 3 estimators × 2 benchmarks with early stopping, evaluation: ~15h rollouts)\",\n      \"gpu_utilization\": \"Good (~65%); scoring is lightweight frozen encoder forward passes, training is the bottleneck\",\n      \"timeline\": \"2–2.5 weeks (3 days scoring + variance characterization, 5 days main experiments with 2-GPU parallelism, 3 days analysis + writing + ablations) — feasible for CoRL 2026 deadline with existing infrastructure\",\n      \"team\": \"1–2 researchers with existing RoboMimic/LIBERO setup and pretrained IQL/VIP/R3M checkpoints\",\n      \"estimated_gpu_cost\": \"$180–240 (120h × $1.50–2.00/hr)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~160h A100-80GB (additional runs for full ablation grid and robustness experiments)\",\n      \"gpu_utilization\": \"Good (~65%); agent orchestrates scoring and training while human develops proof sketch and reviews theoretical framing\",\n      \"timeline\": \"12–14 days (targeting CoRL 2026 abstract May 26, paper May 28)\",\n      \"team\": \"1 researcher, ~3h/day for proof sketch, experiment design, and paper drafting\",\n      \"claude_api_cost\": \"$80–150 (~800–1500 Opus turns for experiment orchestration, analysis, LaTeX writing)\",\n      \"estimated_gpu_cost\": \"$240–320 (160h × $1.50–2.00/hr)\",\n      \"risk_note\": \"Tight timeline requires existing infrastructure. Bias-variance decomposition needs careful but informal proof sketch — full formal proofs can go in appendix or camera-ready.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~220h A100-80GB (full estimator × strategy × benchmark × ablation grid)\",\n      \"gpu_utilization\": \"High (~70%); scoring parallelizable, training is sequential bottleneck\",\n      \"timeline\": \"8–11 days with 2× A100 parallelism\",\n      \"team\": \"0 (initial setup: provide pretrained VIP/R3M/IQL checkpoints, RINSE implementation, benchmark configs)\",\n      \"claude_api_cost\": \"$120–250 (~1200–2500 Opus turns)\",\n      \"estimated_gpu_cost\": \"$330–440 (220h × $1.50–2.00/hr)\",\n      \"speed_bottleneck\": \"Policy training (~8h/run) is sequential; with 2 GPUs and ~10 unique conditions, ~40h for training phase. Scoring and variance characterization are fully parallelizable.\",\n      \"risk_note\": \"Agent can run experiments but proof sketch requires human review. Risk: if VIP/R3M do not outperform binary filtering with continuous weights, the An et al. tension experiment fails — but the adaptive-vs-fixed fallback remains valid.\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (abstract deadline May 26, paper deadline May 28, 8 pages) — primary target. Two co-primary contributions (theory + empirical characterization) with 3 estimator classes. Proof sketch in main paper, full proofs in appendix.\",\n    \"ICRA 2027 (expected deadline ~September 2026) — fallback with expanded scope: 5+ estimator classes (add VLM reward models, MI estimators), OXE-scale experiments, full formal theorems.\"\n  ],\n  \"level\": \"solid-to-strong\",\n  \"key_references\": [\n    \"Why Resampling Outperforms Reweighting for Correcting Sampling Bias with Stochastic Gradients (An et al., ICLR 2021) — proves resampling > reweighting under SGD dynamics; our framework adds the orthogonal estimator-level factor and empirically tests whether low-variance estimators can overcome this SGD disadvantage\",\n    \"What is the Effect of Importance Weighting in Deep Learning? (Byrd & Lipton, ICML 2019) — shows importance weighting has diminishing effects in overparameterized networks; context for why continuous weighting may underperform with noisy scores\",\n    \"SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation (Chen et al., ICLR 2026) — introduces RA-BC with adaptive hybrid w_i = 1{r̂_i > κ} + 1{0 ≤ r̂_i ≤ κ} · w̃_i; adapts parameters within fixed hybrid form, we select the form itself based on estimator properties\",\n    \"Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning (RINSE, ICML 2025 Workshop DataWorld) — derives E(k) ≈ σ̄²(k) + C·d/(kT) and uses smoothness for both filtering and weighting; our framework subsumes this as single-estimator special case and adds cross-estimator adaptive selection\",\n    \"A Closer Look at Advantage-Filtered Behavioral Cloning in High-Noise Datasets (Grigsby & Qi, arXiv 2021) — found binary filtering more robust than AWR weighting for Q-function scores due to advantage concentration and temperature sensitivity; our framework provides variance-based explanation\",\n    \"Why Less is More (Sometimes): A Theory of Data Curation (ICLR 2026) — derives phase transitions for data pruning; addresses quantity not filter-vs-weight modality\",\n    \"Reliable Conditioning of Behavioral Cloning for Offline Reinforcement Learning (CWBC, arXiv 2022) — trajectory weighting with conservative regularization; proposes a scheme but does not derive when filtering outperforms weighting\",\n    \"Density-Ratio Weighted Behavioral Cloning (Oct 2025) — finite-sample bounds for weighted BC from corrupted datasets assuming known density ratios\",\n    \"Ideal Spatial Adaptation by Wavelet Shrinkage (Donoho & Johnstone, Biometrika 1994) — classical hard vs. soft thresholding theory; conceptual inspiration for noise-dependent strategy selection\",\n    \"SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (ICRA 2026) — self-supervised binary filtering baseline achieving 15.4% average improvement\",\n    \"Curating Demonstrations using Online Experience (Demo-SCORE, RSS 2025) — online experience-based binary filtering\",\n    \"TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics (Feb 2026) — VLM-based continuous weighting; future extension estimator class\",\n    \"Value-aligned Behavior Cloning for Offline RL via Bi-level Optimization (VACO, ICLR 2025) — meta-scoring for weighted BC\",\n    \"DataMIL: Selecting Data for Robot Imitation Learning with Datamodels (UT Austin, 2025) — policy-aware data selection on OXE\",\n    \"CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025) — influence-function-based curation\",\n    \"Quality over Quantity: Demonstration Curation via Influence Functions (QoQ, ICRA 2026) — influence-function-based per-sample curation\",\n    \"Robot Data Curation with Mutual Information Estimators (DemInf, RSS 2025) — MI-based quality estimation; future extension estimator class\",\n    \"VIP: Towards Universal Visual Reward and Representation via Value-Implicit Pre-Training (ICLR 2023) — temporal contrastive encoder, low-variance estimator class\",\n    \"R3M: A Universal Visual Representation for Robot Manipulation (CoRL 2023) — time-contrastive + video-language encoder, low-variance estimator class\",\n    \"Offline Reinforcement Learning with Implicit Q-Learning (IQL, ICLR 2022) — Q-function estimation with bootstrapped TD, high-variance estimator class\",\n    \"OpenVLA: An Open-Source Vision-Language-Action Model (ICML 2025) — VLA backbone\",\n    \"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success (OpenVLA-OFT, 2025) — LoRA fine-tuning recipe\",\n    \"Advantage-Weighted Regression (Peng et al., ICLR 2020) — AWR theoretical foundation for exponential weighting\",\n    \"Thresholding Data Shapley for Data Cleansing Using Multi-Armed Bandits (Namba et al., 2024) — thresholding theory applied to data quality scores\"\n  ],\n  \"description\": \"We propose Variance-Guided Demo Curation (VGDC), a framework with two co-primary contributions addressing the unresolved question of whether robot demonstration quality scores should be used for binary filtering or continuous weighting.\\n\\nFirst, we derive a novel bias-variance decomposition of weighted BC suboptimality that structurally distinguishes the two strategies. Binary filtering suboptimality is dominated by misclassification at the decision boundary — P(sign(f−c) ≠ sign(f*−c)) · Δ_q — a LOCAL noise property (only errors near the threshold matter). Continuous weighting suboptimality is dominated by global estimator MSE amplified through weights — C·σ_f²/T + α·T — where all score errors contribute. This decomposition reveals that high-variance estimators favor filtering (noise away from the boundary is harmless) while low-variance estimators favor weighting (precise ordinal information is preserved). The optimal temperature satisfies T* ∝ σ_f, derived from our own analysis rather than borrowed from Donoho-Johnstone. This result is distinct from An et al.'s SGD-level analysis (ours is estimator-level), RINSE's single-estimator E(k) formula (which we subsume as a special case), and CWBC/Density-Ratio Weighted BC (which propose schemes but don't characterize the filter-vs-weight boundary).\\n\\nSecond, we conduct the first systematic empirical characterization of quality score reliability across three estimator classes spanning the variance spectrum: IQL Q-function advantages (high variance, bootstrapped TD), VIP/R3M contrastive encoders (low variance, frozen pretrained), and RINSE smoothness metrics (moderate variance, deterministic). We measure rank-order stability under bootstrap resampling (Kendall's τ̄) as the primary reliability metric and demonstrate that τ̄ predicts the optimal strategy: low stability (IQL, τ̄ ≈ 0.4–0.6) → binary filtering wins; high stability (VIP/R3M, τ̄ ≈ 0.85–0.95) → continuous weighting wins. Critically, we show VIP/R3M continuous weighting outperforms binary filtering DESPITE An et al.'s general result favoring resampling — demonstrating that estimator-level signal quality can compensate for optimizer-level disadvantages.\\n\\nThe practical synthesis is an adaptive algorithm: score demos with any pretrained estimator, measure rank stability via bootstrap, and automatically select binary filtering or continuous weighting (with temperature T = c·σ_f calibrated on held-out data). We replace the previously proposed Hartigan's dip test — which measures bimodality, disconnected from the theory — with rank stability, which directly measures ordinal information reliability as predicted by the decomposition. As robustness insurance, we show the adaptive algorithm outperforms any fixed strategy (always-filter, always-weight) across the full estimator × task grid, even if the variance-performance correlation is imperfect. We evaluate on RoboMimic (5 tasks) and LIBERO-Long (10 tasks) with diffusion policy and OpenVLA-OFT, comparing against SCIZOR, RINSE, SARM/RA-BC, and fixed baselines. Estimated compute: 120–220 A100-hours. Primary target: CoRL 2026.\",\n  \"project_name\": \"ss_temporal_adv_scoring\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 6)\nIssues: [\"PERSISTENT FACTUAL ERROR (flagged Round 5, NOT fixed): The proposal still states 'κ derived adaptively from running statistics of progress deltas' for SARM/RA-BC. My independent verification (WebFetch of arxiv.org/html/2509.25358) confirms κ=0.01 is a FIXED hyperparameter corresponding to 'a task duration of 1 minute 30 seconds, the threshold for the top 5% of demonstrations.' Only w̃_i uses adaptive running statistics (μ, σ) via Welford's estimator. This was explicitly flagged in Round 5 feedback item #1 and remains uncorrected. Repeated factual errors about the closest competing work will severely damage credibility with reviewers who check the original paper.\", \"PERSISTENT MISSING REFERENCES (flagged Round 5, NOT addressed): Robometer (RSS 2026) — a general-purpose robotic reward model trained on 1M+ trajectories providing dense rewards, directly relevant as a quality estimator class and as context for reward model reliability. IWR (CoRL 2025) — importance-weighted retrieval for IL data selection using density ratios. Green-VLA (Feb 2026) — includes DataQA pipeline using heuristic metrics for demonstration filtering. While none are direct competitors, their omission after being flagged in Round 5 suggests inadequate response to review feedback.\", \"RINSE venue characterization needs correction: The proposal says 'ICML 2025 Workshop, DataWorld' which my verification confirms is correct for the workshop presentation. However, the arXiv preprint (2604.23000) was posted April 24, 2026 — nearly a year after the workshop. The proposal should note that the arXiv version may contain substantial revisions beyond the workshop paper, and check whether the full paper has been submitted to a main venue (if so, it carries more weight as prior art than a workshop paper).\", \"Unvalidated Kendall's τ̄ predictions carry significant narrative risk: The expected ranges (IQL ≈ 0.4-0.6, VIP/R3M ≈ 0.85-0.95, smoothness ≈ 0.7-0.8) are central to the paper's story but are entirely theoretical predictions. If VIP/R3M scores have lower rank stability than expected due to domain gap (Ego4D pretraining → robot manipulation) or if IQL scores are more stable than expected due to IQL's expectile regression (which specifically reduces Q-value variance), the clean three-class narrative breaks down. The proposal should explicitly quantify the minimum separation needed to support the thesis (e.g., 'the framework requires at least 0.15 τ̄ gap between estimator classes').\", \"The An et al. tension experiment is the paper's highest-risk, highest-reward claim: An et al.'s result is a THEOREM (not an empirical tendency) under specific assumptions (bounded weights, SGD, constant learning rate). The proposal correctly notes that Adam optimizer and finite training may violate these assumptions, but this argument cuts both ways — if Adam makes reweighting and resampling equivalent (as Byrd & Lipton 2019 suggest for overparameterized networks), then neither strategy dominates, and the entire framework loses predictive power. The proposal needs a clearer discussion of what happens in the 'null result' scenario where the strategy choice doesn't matter much.\", \"Sim-only evaluation is increasingly weak for CoRL 2026: Since Round 5, the ICRA 2026 'From Data to Decisions: VLA Pipelines for Real Robots' workshop signals that the community is actively demanding real-world validation of data curation pipelines. All close competitors include real-robot results: SCIZOR (Franka, YAM), Demo-SCORE (Franka), CUPID (hardware experiments), TOPReward (SO-100/101). The user's statement that 'from a theoretical perspective, sim-only is acceptable' may not align with CoRL reviewer expectations. Even 1-2 simple real tasks with a single estimator class would significantly strengthen the submission.\"]\nFeedback: The proposal has matured significantly over 6 rounds and the core idea — a bias-variance decomposition that reveals when binary filtering vs. continuous weighting is optimal, depending on estimator noise properties — is genuinely novel and fills a real gap. But two categories of issues prevent a pass:\n\n**Category 1: Quality control failures (must fix immediately)**\n\n1. Fix the SARM κ characterization. This was flagged in Round 5 and ignored. Change 'κ derived adaptively from running statistics of progress deltas' to 'κ=0.01 is a fixed hyperparameter; only w̃_i uses adaptive running statistics (μ, σ) via Welford's estimator.' Your differentiation (selecting functional form vs. adapting parameters within it) is unaffected and actually strengthened by this correction — SARM fixes BOTH the form AND the threshold, making your adaptive form-selection more clearly distinct.\n\n2. Add the three missing references flagged in Round 5: Robometer (RSS 2026) as context for reward model reliability and a future estimator class; IWR (CoRL 2025) as relevant prior work on importance-weighted data selection for IL; Green-VLA (Feb 2026) as evidence that heuristic-based demo filtering pipelines are being deployed in practice (which motivates principled alternatives like yours).\n\n**Category 2: Scientific robustness (needs strengthening)**\n\n3. Quantify the minimum effect size needed. State explicitly: 'For the framework to be informative, we need the gap between τ̄ values across estimator classes to exceed X, and the strategy-performance correlation to achieve R² > Y.' This protects against reviewer criticism that the framework offers no predictive power if the effect is weak.\n\n4. Prepare a concrete null-result contingency. If VIP/R3M continuous weighting does NOT outperform binary filtering (the An et al. tension experiment fails), the paper should pivot cleanly to: 'The adaptive algorithm still matches the best fixed strategy because it measures before committing.' Frame this as the PRIMARY result in the failure scenario, with the variance-spectrum correlation as secondary supporting evidence.\n\n5. Either justify sim-only more forcefully or add minimal real-robot experiments. For justification: emphasize that the contribution is a DIAGNOSTIC FRAMEWORK (characterizing estimator properties), not a new curation METHOD — the insights about estimator reliability transfer regardless of sim/real, and the specific estimators tested (frozen VIP/R3M, pretrained IQL) are the same checkpoints used in real-world deployments. For experiments: even 2 tasks on a single robot platform with 1 estimator class (VIP, since it's easiest to deploy) would suffice.\n\n6. Address the RINSE arXiv timing: The arXiv version (April 2026) is newer than the ICML 2025 workshop paper. Check whether the full version includes additional results or analysis that overlaps with your contributions. If the April 2026 arXiv version of RINSE now includes cross-estimator analysis or an adaptive strategy selection, your novelty claim needs adjustment.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 6 轮修订，近 3 轮的平均分从 3.5 到 3.5，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-13T11:40:38.225Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-13T11:40:38.225Z",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96"
}
```

---

## Round 1

40 recorded events

### User

_source line 3 · 2026-05-13T11:40:38.263Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-13 (UTC).**

## Original idea
{
  "title": "When to Filter, When to Weight: A Bias-Variance Framework for Adaptive Demo Curation",
  "core_problem": "Given a quality scoring function for robot demonstrations, should training signals be binarized (keep/discard) or used as continuous weights? The demo curation field has produced 15+ methods in 2024–2026, each making an ad hoc choice: SCIZOR and Demo-SCORE use binary filtering, TOPReward and VACO use continuous weighting, and SARM/RA-BC (ICLR 2026) uses a hybrid with adaptive threshold parameters but a fixed functional form. While the general ML literature offers relevant theory — An et al. (ICLR 2021) prove resampling outperforms reweighting under SGD dynamics, Byrd & Lipton (ICML 2019) show diminishing weighting effects in overparameterized networks — these results address the optimizer level (SGD) but not the estimator level: whether the quality scores themselves are precise enough to justify continuous use. The choice between filtering and weighting remains ad hoc and disconnected from the properties of the specific quality estimator being used.",
  "opportunity": "The proliferation of diverse quality estimators — Q-function advantages (IQL), temporal contrastive encoders (VIP, R3M), smoothness metrics (RINSE SAL/TED), VLM reward models, and influence functions — makes this question increasingly urgent. These estimators differ fundamentally in their noise properties: IQL Q-values arise from bootstrapped TD learning that amplifies estimation errors across Bellman backups; VIP/R3M scores come from frozen pretrained encoders with stable supervised/contrastive objectives; RINSE smoothness metrics are deterministic functions of trajectory geometry. Our key insight is that the reliability of ordinal information in quality scores — measurable as rank-order stability under bootstrap resampling — is the primary factor governing whether binary filtering or continuous weighting is optimal. This connects to a classical intuition: noisy estimates are better thresholded (only the sign/rank-class matters), while precise estimates should be used continuously (preserving ordinal information). Unlike prior work that provides better scores (SCIZOR, RINSE, QoQ) or proposes a specific weighting scheme (SARM/RA-BC, CWBC), we address the orthogonal question of what to DO with any given set of scores. The opportunity is twofold: (a) a theoretical decomposition of weighted BC suboptimality into strategy-specific terms that reveals the estimator-property dependence, and (b) a practical adaptive algorithm that measures score reliability and automatically selects the appropriate strategy.",
  "landscape": "Demo curation for robot learning is an extremely active area with 15+ papers at top venues in 2024–2026.\n\n**Binary filtering methods**: SCIZOR (ICRA 2026) uses a self-supervised temporal distance classifier for binary keep/discard, achieving 15.4% average improvement (5.4% RoboMimic, 8.1% OXEMagic, 32.9% Sirius-Fleet). Demo-SCORE (RSS 2025) trains a success/failure classifier from online rollouts, achieving 15–35% higher success rate.\n\n**Continuous/weighted methods**: TOPReward (Feb 2026) extracts task progress from VLM token logits for advantage-weighted BC. VACO (ICLR 2025) uses a meta-scoring network with value alignment for weighted BC via bi-level optimization.\n\n**Hybrid filtering+weighting**: SARM/RA-BC (ICLR 2026) introduces a hybrid weight formula w_i = 1{r̂_i > κ} + 1{0 ≤ r̂_i ≤ κ} · w̃_i where w̃_i = clip((r̂_i − (μ−2σ))/(4σ+ε), 0, 1), with κ derived adaptively from running statistics of progress deltas. This is the closest work to ours: it adapts threshold parameters within a FIXED functional form (always hybrid), whereas we select the functional form itself (binary vs. continuous) based on measured estimator properties.\n\n**Quality-quantity analysis**: RINSE (ICML 2025 Workshop, DataWorld) derives E(k) ≈ σ̄²(k) + C·d/(kT), decomposing error into a noise floor (reduced by filtering) and a statistical estimation term (increased by reducing data), and uses smoothness-based metrics for both binary filtering and continuous exponential weighting w(τ)=exp(−λq(τ)). However, this analysis applies only to smoothness metrics, does not compare across estimator classes, and provides no decision rule for when each strategy is optimal. Our framework subsumes RINSE's decomposition as a special case (smoothness estimators, single-class) while extending to the multi-estimator adaptive setting with a principled selection criterion.\n\n**Prior work on filtering vs. weighting**: AFBC (Grigsby & Qi, arXiv 2021) tested binary AND exponential AWR weighting for BC with Q-function advantages, finding binary more robust. They attributed this to temperature sensitivity ('a change in β is enough to take us from near-failure to state-of-the-art performance') and advantage concentration near zero. Our framework offers a deeper explanation: Q-function advantages from bootstrapped TD have high score variance and low rank-order stability, which our analysis predicts should favor binarization.\n\n**General ML theory**: An et al. (ICLR 2021) prove resampling outperforms reweighting under SGD dynamics via dynamical stability analysis — a strong prior FAVORING filtering. However, their analysis operates at the optimizer level (SGD trajectory stability) and does not account for estimator-level signal quality. Our framework adds an orthogonal factor: when estimator variance is sufficiently low, the ordinal information preserved by continuous weights can compensate for the SGD-level disadvantage, a prediction we test empirically with VIP/R3M encoders. Byrd & Lipton (ICML 2019) show importance weighting has diminishing effects in overparameterized networks. 'Why Less is More (Sometimes)' (ICLR 2026) derives phase transitions for data pruning quantity but does not address the filter-vs-weight modality. CWBC (arXiv 2022) proposes trajectory weighting with conservative regularization but does not derive when filtering outperforms weighting. Density-Ratio Weighted BC (Oct 2025) provides finite-sample bounds for weighted BC assuming known density ratios, not noisy quality estimators.\n\n**Policy-aware methods**: DataMIL (2025) uses datamodels for end-to-end data selection on OXE. CUPID (CoRL 2025) and QoQ (ICRA 2026) use influence functions for per-sample curation.\n\n**Critical gap**: Despite this extensive literature, no existing work (1) derives a suboptimality decomposition for weighted BC that separately characterizes the regimes where binary filtering vs. continuous weighting is tighter, (2) empirically demonstrates that estimator-level score reliability (not just score quality) predicts the optimal strategy, or (3) provides an adaptive algorithm that selects between strategies based on measured estimator properties. SARM/RA-BC adapts parameters within a fixed hybrid form; our contribution is selecting the form itself.",
  "approach": "We propose Variance-Guided Demo Curation (VGDC), a framework with two co-primary contributions — a theoretical decomposition and an empirical characterization — synthesized into a practical adaptive algorithm.\n\n**Co-Primary Contribution A: Bias-Variance Decomposition for Weighted BC**. We derive a novel decomposition of weighted BC suboptimality that reveals why different quality estimators favor different strategies. Consider a dataset {τ_i}_{i=1}^N of demonstrations with true quality f*(τ_i) and estimated quality f(τ_i) = f*(τ_i) + ε_i. For binary filtering at threshold c, the suboptimality decomposes as:\n\nR_filter ≤ P(sign(f(τ)−c) ≠ sign(f*(τ)−c)) · Δ_q + d/(k·m)\n\nwhere the first term is the misclassification rate at the decision boundary (misclassifying good demos as bad or vice versa) scaled by the quality impact Δ_q, and the second term is the estimation error from the reduced dataset of size k. For continuous weighting with w_i ∝ exp(f(τ_i)/T), the suboptimality decomposes as:\n\nR_weight ≤ C · σ_f²/T + α · T + d/N_eff(T)\n\nwhere σ_f² = E[ε²] is the estimator MSE amplified through weights (noise amplification term), α·T captures the bias from temperature smoothing (higher T → more uniform → more bias from including low-quality demos), and N_eff(T) is the effective sample size under the weight distribution. The key structural difference: binary filtering suboptimality depends on noise at the DECISION BOUNDARY (only misclassifications matter — a local property), while continuous weighting suboptimality depends on GLOBAL noise properties (all scores contribute to weight errors). This explains why high-variance estimators favor filtering (most noise is away from the boundary and doesn't affect the binary decision) while low-variance estimators favor weighting (precise ordinal information is preserved). The optimal temperature T* that minimizes R_weight satisfies T* ∝ σ_f (noisier estimators require higher temperature, which reduces noise amplification but increases bias — eventually, binary filtering dominates). We provide a proof sketch in the main paper and full proofs in the appendix.\n\nThis decomposition is distinct from and complementary to: An et al.'s SGD dynamics analysis (optimizer-level; our analysis is estimator-level), RINSE's E(k) formula (single-estimator special case without strategy comparison), CWBC's trajectory weighting (proposes a scheme but doesn't derive when filtering wins), and Density-Ratio Weighted BC (assumes known density ratios, not noisy quality scores). We explicitly show that RINSE's E(k) ≈ σ̄²(k) + C·d/(kT) is recovered as a special case of our R_filter bound for deterministic smoothness estimators (σ_f = 0, no misclassification noise, only data quantity tradeoff).\n\n**Co-Primary Contribution B: Empirical Characterization Across 3 Estimator Classes**. We conduct the first systematic measurement of quality score reliability across three classes that span the variance spectrum: (1) IQL Q-function advantages — high variance from bootstrapped TD learning where Bellman backup errors compound across iterations, with known issues of Q-value overestimation and concentration near zero (as documented by Grigsby & Qi); (2) VIP/R3M temporal contrastive encoders — low variance from frozen pretrained representations trained with stable contrastive/supervised objectives on large video datasets (Ego4D); (3) RINSE smoothness metrics (SAL, TED) — moderate variance, deterministic functions of trajectory geometry but sensitive to trajectory segmentation. For each estimator class, we measure: (a) rank-order stability via bootstrap Kendall's τ (the primary reliability metric), (b) score variance across dataset subsamples, (c) calibration (correlation between estimated and true quality). The central empirical result: estimators with low rank stability (IQL, expected τ̄ ≈ 0.4–0.6) consistently favor binary filtering, while estimators with high rank stability (VIP/R3M, expected τ̄ ≈ 0.85–0.95) favor continuous weighting, with smoothness metrics (expected τ̄ ≈ 0.7–0.8) falling near the crossover region.\n\n**Critical empirical test of the An et al. tension**: We directly address the strongest theoretical objection. An et al. prove resampling > reweighting in general under SGD. We show that for VIP/R3M scores (low variance, high rank stability), continuous weighting outperforms binary filtering DESPITE the SGD dynamics favoring resampling. This demonstrates that estimator-level signal quality can overcome the optimizer-level disadvantage — a novel empirical result that extends the An et al. framework.\n\n**Practical Adaptive Algorithm (3 stages)**:\n(1) Score: Compute per-transition quality scores using any pretrained estimator. We demonstrate with frozen VIP/R3M embeddings (cosine similarity to goal embedding) and IQL Q-values (pretrained on the same dataset) — no from-scratch training required.\n(2) Adapt: Estimate score reliability via bootstrap rank stability. Draw B=50 bootstrap resamples of the score vector, compute pairwise Kendall's τ, and take the mean τ̄. If τ̄ > τ_crit, select continuous softmax weighting with temperature T = c · σ_f (where c is calibrated via held-out validation, and σ_f is the bootstrap-estimated score standard deviation); if τ̄ ≤ τ_crit, select binary filtering at the median-split threshold. We ablate over: (a) the threshold τ_crit ∈ {0.6, 0.7, 0.8}, (b) alternative reliability metrics (coefficient of variation σ_f/|μ_f|, split-half correlation), and (c) temperature schedules (T = c·σ_f vs. T = c·σ_f·sqrt(log N) vs. cross-validated T). This replaces the previously proposed Hartigan's dip test, which measures score bimodality — a property disconnected from the theoretical decomposition. Rank stability directly measures ordinal information reliability, which is what the theory says determines the filter-vs-weight choice.\n(3) Train: Fine-tune the policy (diffusion policy or OpenVLA-OFT with LoRA) using the selected weighted/filtered BC loss.\n\n**Robustness to partial hypothesis support**: Even if the variance-performance correlation is imperfect across all estimator classes (e.g., R² < 0.5), we add a fallback experiment: the adaptive algorithm vs. any fixed strategy (always-filter, always-weight) across the full estimator × task grid. The adaptive algorithm should match or outperform the best fixed strategy because it can select per-estimator. This gives a weaker but still valuable result: 'measuring score reliability and adapting never hurts, even if variance is an imperfect predictor.'\n\n**Evaluation (CoRL-scope)**: Evaluate on RoboMimic (5 tasks: Lift, Can, Square, Transport, ToolHang) and LIBERO-Long (10 tasks) using diffusion policy as the primary backbone and OpenVLA-OFT as secondary. Compare against: (a) unweighted BC (no curation), (b) SCIZOR binary filtering, (c) RINSE SAL/TED filtering and weighting, (d) SARM/RA-BC fixed hybrid, (e) fixed-binary and fixed-continuous baselines with our scores. Critical experiments:\n(i) Binary vs. continuous with SAME scores across all 3 estimator classes — the central experiment isolating the strategy question.\n(ii) Rank stability vs. performance correlation: for each estimator × task, measure τ̄ and plot against the relative performance gap of binary vs. continuous.\n(iii) Adaptive selection accuracy: prediction accuracy of the τ̄-based criterion.\n(iv) Adaptive vs. fixed strategies: show VGDC ≥ max(always-filter, always-weight) across the full grid.\n(v) Ablation on reliability metrics, temperature formulas, and bootstrap parameters.\n(vi) Direct test of An et al. tension: VIP/R3M continuous weighting vs. binary filtering.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~120h A100-80GB (scoring: ~3h forward passes across 3 estimator classes on RoboMimic+LIBERO using frozen checkpoints, policy training: ~8h/run × 10 runs for binary/continuous × 3 estimators × 2 benchmarks with early stopping, evaluation: ~15h rollouts)",
      "gpu_utilization": "Good (~65%); scoring is lightweight frozen encoder forward passes, training is the bottleneck",
      "timeline": "2–2.5 weeks (3 days scoring + variance characterization, 5 days main experiments with 2-GPU parallelism, 3 days analysis + writing + ablations) — feasible for CoRL 2026 deadline with existing infrastructure",
      "team": "1–2 researchers with existing RoboMimic/LIBERO setup and pretrained IQL/VIP/R3M checkpoints",
      "estimated_gpu_cost": "$180–240 (120h × $1.50–2.00/hr)"
    },
    "human_in_loop": {
      "gpu_hours": "~160h A100-80GB (additional runs for full ablation grid and robustness experiments)",
      "gpu_utilization": "Good (~65%); agent orchestrates scoring and training while human develops proof sketch and reviews theoretical framing",
      "timeline": "12–14 days (targeting CoRL 2026 abstract May 26, paper May 28)",
      "team": "1 researcher, ~3h/day for proof sketch, experiment design, and paper drafting",
      "claude_api_cost": "$80–150 (~800–1500 Opus turns for experiment orchestration, analysis, LaTeX writing)",
      "estimated_gpu_cost": "$240–320 (160h × $1.50–2.00/hr)",
      "risk_note": "Tight timeline requires existing infrastructure. Bias-variance decomposition needs careful but informal proof sketch — full formal proofs can go in appendix or camera-ready."
    },
    "auto_research": {
      "gpu_hours": "~220h A100-80GB (full estimator × strategy × benchmark × ablation grid)",
      "gpu_utilization": "High (~70%); scoring parallelizable, training is sequential bottleneck",
      "timeline": "8–11 days with 2× A100 parallelism",
      "team": "0 (initial setup: provide pretrained VIP/R3M/IQL checkpoints, RINSE implementation, benchmark configs)",
      "claude_api_cost": "$120–250 (~1200–2500 Opus turns)",
      "estimated_gpu_cost": "$330–440 (220h × $1.50–2.00/hr)",
      "speed_bottleneck": "Policy training (~8h/run) is sequential; with 2 GPUs and ~10 unique conditions, ~40h for training phase. Scoring and variance characterization are fully parallelizable.",
      "risk_note": "Agent can run experiments but proof sketch requires human review. Risk: if VIP/R3M do not outperform binary filtering with continuous weights, the An et al. tension experiment fails — but the adaptive-vs-fixed fallback remains valid."
    }
  },
  "target_venues": [
    "CoRL 2026 (abstract deadline May 26, paper deadline May 28, 8 pages) — primary target. Two co-primary contributions (theory + empirical characterization) with 3 estimator classes. Proof sketch in main paper, full proofs in appendix.",
    "ICRA 2027 (expected deadline ~September 2026) — fallback with expanded scope: 5+ estimator classes (add VLM reward models, MI estimators), OXE-scale experiments, full formal theorems."
  ],
  "level": "solid-to-strong",
  "key_references": [
    "Why Resampling Outperforms Reweighting for Correcting Sampling Bias with Stochastic Gradients (An et al., ICLR 2021) — proves resampling > reweighting under SGD dynamics; our framework adds the orthogonal estimator-level factor and empirically tests whether low-variance estimators can overcome this SGD disadvantage",
    "What is the Effect of Importance Weighting in Deep Learning? (Byrd & Lipton, ICML 2019) — shows importance weighting has diminishing effects in overparameterized networks; context for why continuous weighting may underperform with noisy scores",
    "SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation (Chen et al., ICLR 2026) — introduces RA-BC with adaptive hybrid w_i = 1{r̂_i > κ} + 1{0 ≤ r̂_i ≤ κ} · w̃_i; adapts parameters within fixed hybrid form, we select the form itself based on estimator properties",
    "Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning (RINSE, ICML 2025 Workshop DataWorld) — derives E(k) ≈ σ̄²(k) + C·d/(kT) and uses smoothness for both filtering and weighting; our framework subsumes this as single-estimator special case and adds cross-estimator adaptive selection",
    "A Closer Look at Advantage-Filtered Behavioral Cloning in High-Noise Datasets (Grigsby & Qi, arXiv 2021) — found binary filtering more robust than AWR weighting for Q-function scores due to advantage concentration and temperature sensitivity; our framework provides variance-based explanation",
    "Why Less is More (Sometimes): A Theory of Data Curation (ICLR 2026) — derives phase transitions for data pruning; addresses quantity not filter-vs-weight modality",
    "Reliable Conditioning of Behavioral Cloning for Offline Reinforcement Learning (CWBC, arXiv 2022) — trajectory weighting with conservative regularization; proposes a scheme but does not derive when filtering outperforms weighting",
    "Density-Ratio Weighted Behavioral Cloning (Oct 2025) — finite-sample bounds for weighted BC from corrupted datasets assuming known density ratios",
    "Ideal Spatial Adaptation by Wavelet Shrinkage (Donoho & Johnstone, Biometrika 1994) — classical hard vs. soft thresholding theory; conceptual inspiration for noise-dependent strategy selection",
    "SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (ICRA 2026) — self-supervised binary filtering baseline achieving 15.4% average improvement",
    "Curating Demonstrations using Online Experience (Demo-SCORE, RSS 2025) — online experience-based binary filtering",
    "TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics (Feb 2026) — VLM-based continuous weighting; future extension estimator class",
    "Value-aligned Behavior Cloning for Offline RL via Bi-level Optimization (VACO, ICLR 2025) — meta-scoring for weighted BC",
    "DataMIL: Selecting Data for Robot Imitation Learning with Datamodels (UT Austin, 2025) — policy-aware data selection on OXE",
    "CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025) — influence-function-based curation",
    "Quality over Quantity: Demonstration Curation via Influence Functions (QoQ, ICRA 2026) — influence-function-based per-sample curation",
    "Robot Data Curation with Mutual Information Estimators (DemInf, RSS 2025) — MI-based quality estimation; future extension estimator class",
    "VIP: Towards Universal Visual Reward and Representation via Value-Implicit Pre-Training (ICLR 2023) — temporal contrastive encoder, low-variance estimator class",
    "R3M: A Universal Visual Representation for Robot Manipulation (CoRL 2023) — time-contrastive + video-language encoder, low-variance estimator class",
    "Offline Reinforcement Learning with Implicit Q-Learning (IQL, ICLR 2022) — Q-function estimation with bootstrapped TD, high-variance estimator class",
    "OpenVLA: An Open-Source Vision-Language-Action Model (ICML 2025) — VLA backbone",
    "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success (OpenVLA-OFT, 2025) — LoRA fine-tuning recipe",
    "Advantage-Weighted Regression (Peng et al., ICLR 2020) — AWR theoretical foundation for exponential weighting",
    "Thresholding Data Shapley for Data Cleansing Using Multi-Armed Bandits (Namba et al., 2024) — thresholding theory applied to data quality scores"
  ],
  "description": "We propose Variance-Guided Demo Curation (VGDC), a framework with two co-primary contributions addressing the unresolved question of whether robot demonstration quality scores should be used for binary filtering or continuous weighting.\n\nFirst, we derive a novel bias-variance decomposition of weighted BC suboptimality that structurally distinguishes the two strategies. Binary filtering suboptimality is dominated by misclassification at the decision boundary — P(sign(f−c) ≠ sign(f*−c)) · Δ_q — a LOCAL noise property (only errors near the threshold matter). Continuous weighting suboptimality is dominated by global estimator MSE amplified through weights — C·σ_f²/T + α·T — where all score errors contribute. This decomposition reveals that high-variance estimators favor filtering (noise away from the boundary is harmless) while low-variance estimators favor weighting (precise ordinal information is preserved). The optimal temperature satisfies T* ∝ σ_f, derived from our own analysis rather than borrowed from Donoho-Johnstone. This result is distinct from An et al.'s SGD-level analysis (ours is estimator-level), RINSE's single-estimator E(k) formula (which we subsume as a special case), and CWBC/Density-Ratio Weighted BC (which propose schemes but don't characterize the filter-vs-weight boundary).\n\nSecond, we conduct the first systematic empirical characterization of quality score reliability across three estimator classes spanning the variance spectrum: IQL Q-function advantages (high variance, bootstrapped TD), VIP/R3M contrastive encoders (low variance, frozen pretrained), and RINSE smoothness metrics (moderate variance, deterministic). We measure rank-order stability under bootstrap resampling (Kendall's τ̄) as the primary reliability metric and demonstrate that τ̄ predicts the optimal strategy: low stability (IQL, τ̄ ≈ 0.4–0.6) → binary filtering wins; high stability (VIP/R3M, τ̄ ≈ 0.85–0.95) → continuous weighting wins. Critically, we show VIP/R3M continuous weighting outperforms binary filtering DESPITE An et al.'s general result favoring resampling — demonstrating that estimator-level signal quality can compensate for optimizer-level disadvantages.\n\nThe practical synthesis is an adaptive algorithm: score demos with any pretrained estimator, measure rank stability via bootstrap, and automatically select binary filtering or continuous weighting (with temperature T = c·σ_f calibrated on held-out data). We replace the previously proposed Hartigan's dip test — which measures bimodality, disconnected from the theory — with rank stability, which directly measures ordinal information reliability as predicted by the decomposition. As robustness insurance, we show the adaptive algorithm outperforms any fixed strategy (always-filter, always-weight) across the full estimator × task grid, even if the variance-performance correlation is imperfect. We evaluate on RoboMimic (5 tasks) and LIBERO-Long (10 tasks) with diffusion policy and OpenVLA-OFT, comparing against SCIZOR, RINSE, SARM/RA-BC, and fixed baselines. Estimated compute: 120–220 A100-hours. Primary target: CoRL 2026.",
  "project_name": "ss_temporal_adv_scoring",
  "source": "web_research"
}

## Reviewer feedback (round 6)
Issues: ["PERSISTENT FACTUAL ERROR (flagged Round 5, NOT fixed): The proposal still states 'κ derived adaptively from running statistics of progress deltas' for SARM/RA-BC. My independent verification (WebFetch of arxiv.org/html/2509.25358) confirms κ=0.01 is a FIXED hyperparameter corresponding to 'a task duration of 1 minute 30 seconds, the threshold for the top 5% of demonstrations.' Only w̃_i uses adaptive running statistics (μ, σ) via Welford's estimator. This was explicitly flagged in Round 5 feedback item #1 and remains uncorrected. Repeated factual errors about the closest competing work will severely damage credibility with reviewers who check the original paper.", "PERSISTENT MISSING REFERENCES (flagged Round 5, NOT addressed): Robometer (RSS 2026) — a general-purpose robotic reward model trained on 1M+ trajectories providing dense rewards, directly relevant as a quality estimator class and as context for reward model reliability. IWR (CoRL 2025) — importance-weighted retrieval for IL data selection using density ratios. Green-VLA (Feb 2026) — includes DataQA pipeline using heuristic metrics for demonstration filtering. While none are direct competitors, their omission after being flagged in Round 5 suggests inadequate response to review feedback.", "RINSE venue characterization needs correction: The proposal says 'ICML 2025 Workshop, DataWorld' which my verification confirms is correct for the workshop presentation. However, the arXiv preprint (2604.23000) was posted April 24, 2026 — nearly a year after the workshop. The proposal should note that the arXiv version may contain substantial revisions beyond the workshop paper, and check whether the full paper has been submitted to a main venue (if so, it carries more weight as prior art than a workshop paper).", "Unvalidated Kendall's τ̄ predictions carry significant narrative risk: The expected ranges (IQL ≈ 0.4-0.6, VIP/R3M ≈ 0.85-0.95, smoothness ≈ 0.7-0.8) are central to the paper's story but are entirely theoretical predictions. If VIP/R3M scores have lower rank stability than expected due to domain gap (Ego4D pretraining → robot manipulation) or if IQL scores are more stable than expected due to IQL's expectile regression (which specifically reduces Q-value variance), the clean three-class narrative breaks down. The proposal should explicitly quantify the minimum separation needed to support the thesis (e.g., 'the framework requires at least 0.15 τ̄ gap between estimator classes').", "The An et al. tension experiment is the paper's highest-risk, highest-reward claim: An et al.'s result is a THEOREM (not an empirical tendency) under specific assumptions (bounded weights, SGD, constant learning rate). The proposal correctly notes that Adam optimizer and finite training may violate these assumptions, but this argument cuts both ways — if Adam makes reweighting and resampling equivalent (as Byrd & Lipton 2019 suggest for overparameterized networks), then neither strategy dominates, and the entire framework loses predictive power. The proposal needs a clearer discussion of what happens in the 'null result' scenario where the strategy choice doesn't matter much.", "Sim-only evaluation is increasingly weak for CoRL 2026: Since Round 5, the ICRA 2026 'From Data to Decisions: VLA Pipelines for Real Robots' workshop signals that the community is actively demanding real-world validation of data curation pipelines. All close competitors include real-robot results: SCIZOR (Franka, YAM), Demo-SCORE (Franka), CUPID (hardware experiments), TOPReward (SO-100/101). The user's statement that 'from a theoretical perspective, sim-only is acceptable' may not align with CoRL reviewer expectations. Even 1-2 simple real tasks with a single estimator class would significantly strengthen the submission."]
Feedback: The proposal has matured significantly over 6 rounds and the core idea — a bias-variance decomposition that reveals when binary filtering vs. continuous weighting is optimal, depending on estimator noise properties — is genuinely novel and fills a real gap. But two categories of issues prevent a pass:

**Category 1: Quality control failures (must fix immediately)**

1. Fix the SARM κ characterization. This was flagged in Round 5 and ignored. Change 'κ derived adaptively from running statistics of progress deltas' to 'κ=0.01 is a fixed hyperparameter; only w̃_i uses adaptive running statistics (μ, σ) via Welford's estimator.' Your differentiation (selecting functional form vs. adapting parameters within it) is unaffected and actually strengthened by this correction — SARM fixes BOTH the form AND the threshold, making your adaptive form-selection more clearly distinct.

2. Add the three missing references flagged in Round 5: Robometer (RSS 2026) as context for reward model reliability and a future estimator class; IWR (CoRL 2025) as relevant prior work on importance-weighted data selection for IL; Green-VLA (Feb 2026) as evidence that heuristic-based demo filtering pipelines are being deployed in practice (which motivates principled alternatives like yours).

**Category 2: Scientific robustness (needs strengthening)**

3. Quantify the minimum effect size needed. State explicitly: 'For the framework to be informative, we need the gap between τ̄ values across estimator classes to exceed X, and the strategy-performance correlation to achieve R² > Y.' This protects against reviewer criticism that the framework offers no predictive power if the effect is weak.

4. Prepare a concrete null-result contingency. If VIP/R3M continuous weighting does NOT outperform binary filtering (the An et al. tension experiment fails), the paper should pivot cleanly to: 'The adaptive algorithm still matches the best fixed strategy because it measures before committing.' Frame this as the PRIMARY result in the failure scenario, with the variance-spectrum correlation as secondary supporting evidence.

5. Either justify sim-only more forcefully or add minimal real-robot experiments. For justification: emphasize that the contribution is a DIAGNOSTIC FRAMEWORK (characterizing estimator properties), not a new curation METHOD — the insights about estimator reliability transfer regardless of sim/real, and the specific estimators tested (frozen VIP/R3M, pretrained IQL) are the same checkpoints used in real-world deployments. For experiments: even 2 tasks on a single robot platform with 1 estimator class (VIP, since it's easiest to deploy) would suffice.

6. Address the RINSE arXiv timing: The arXiv version (April 2026) is newer than the ICML 2025 workshop paper. Check whether the full version includes additional results or analysis that overlaps with your contributions. If the April 2026 arXiv version of RINSE now includes cross-estimator analysis or an adaptive strategy selection, your novelty claim needs adjustment.

## Instructions
- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.
- Address each issue specifically.

## 深度调研要求（每一轮修订都必须执行）

不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。

1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。
   - 搜索最新的相关论文（arXiv, conference proceedings）
   - 搜索 benchmark/leaderboard 确认当前 SOTA
   - 搜索可能遗漏的相关工作和 concurrent work

2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，
   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。

3. **深度思考**：在修订之前，先独立思考以下问题：
   - 这个 idea 的核心假设是否仍然成立？
   - reviewer 的批评是否揭示了更深层的问题？
   - 有没有更好的 framing 或 approach 来解决同一个核心问题？
   - 修订后的 idea 相比上一版有什么本质性的改进？

4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，
   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。

## 针对 Review 意见的定向搜索

对 reviewer 指出的每个问题，执行以下搜索流程：

1. **如果 reviewer 说'已有类似工作'**：
   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读
   - 搜索该论文的 cited-by，找到后续跟进工作
   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot

2. **如果 reviewer 说'SOTA 过时'**：
   - 用 Papers With Code 查看当前排行榜
   - 搜索过去 6 个月的最新方法
   - 更新你的 landscape 和 baseline

3. **如果 reviewer 说'可行性有问题'**：
   - 搜索类似规模实验的实际成本和时间线
   - 搜索 GitHub 上是否有可复用的实现
   - 搜索相关数据集/模型的可获取性

4. **如果 reviewer 说'novelty 不足'**：
   - 对核心方法尽量做 3-5 种不同关键词组合的搜索
   - 搜索相邻领域是否有类似思路
   - 如果确实 novelty 不足，考虑 major revision 或 pivot

- Use WebSearch to find updated information if the reviewer flagged outdated claims.
- You have full freedom in how much to change:
  - Minor fix: if only specific details are wrong, correct them and keep everything else.
  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.
  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.
- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.
- In the output JSON, include a "change_type" field with one of: "minor", "major", or "pivot" to indicate the scope of your changes.
- Output the revised idea as a COMPLETE JSON object (same schema as original, plus "change_type").

## 停滞提醒
这个 idea 已经经过 6 轮修订，近 3 轮的平均分从 3.5 到 3.5，没有明显改善。

请认真思考：
- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？
- 如果你认为问题出在 approach 而非 framing，可以做 major revision。
- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。
- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。

最终由你判断——做你认为最能提升 idea 质量的选择。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "type": "user",
  "uuid": "e76e46b7-0939-4fe7-88b8-087ebdeb6a14",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-13T11:40:38.261Z_

```json
{
  "parentUuid": "e76e46b7-0939-4fe7-88b8-087ebdeb6a14",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "64a2f349-3088-4562-b938-ae55a9b658d4",
  "timestamp": "2026-05-13T11:40:38.261Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-13T11:40:38.261Z_

```json
{
  "parentUuid": "64a2f349-3088-4562-b938-ae55a9b658d4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9c812a3c-7725-4880-9fd8-bda012e33be3",
  "timestamp": "2026-05-13T11:40:38.261Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"When to Filter, When to Weight: A Bias-Variance Framework for Adaptive…",
  "leafUuid": "9c812a3c-7725-4880-9fd8-bda012e33be3",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Adaptive demo curation via estimator reliability",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96"
}
```

---

### Assistant

_source line 8 · 2026-05-13T11:40:52.174Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the reviewer feedback and think deeply about whether this idea needs minor fixes, major revision, or a pivot.

**Analyzing the feedback:**

1. **SARM κ characterization** - This is a factual error that was flagged twice and not fixed. Simple fix but embarrassing.

2. **Missing references** - Robometer, IWR, Green-VLA. Need to find and add these.

3. **RINSE arXiv timing** - Need to check the April 2026 arXiv version for overlap.

4. **Unvalidated τ̄ predictions** - The clean three-class narrative is fragile. Need minimum effect size.


5. **An et al. tension experiment** - High risk. Need null-result contingency.

6. **Sim-only evaluation** - Increasingly weak for CoRL 2026.

The core insight about how estimator noise shapes optimal curation strategy is genuinely novel, but six rounds without score improvement suggests deeper issues beyond just quality control—the untested τ̄ predictions, the risky An et al. tension experiment, and the sim-only limitation are real scientific vulnerabilities that need addressing.

This isn't a pivot moment though; the reviewer confirms the idea fills a genuine gap. What I need is a focused major revision that eliminates factual errors and missing references, establishes explicit minimum effect sizes and null-result contingencies, either justifies the simulation-only approach more rigorously or proposes minimal real-robot validation, and checks for RINSE arXiv overlap. Let me start with the research.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c812a3c-7725-4880-9fd8-bda012e33be3",
  "isSidechain": false,
  "requestId": "req_011CazWFr6FR7XP1Xk1rS93o",
  "type": "assistant",
  "uuid": "cd43c851-7441-4353-84a6-0ac58f7811ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R25WjnLvDrgQKSwCQzfjJK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15040,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2625,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15040,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2625,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15040,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15040
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-13T11:40:52.228Z_

I'll start by doing deep research on the specific issues flagged by the reviewer, then synthesize and revise. Let me launch several parallel research threads.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd43c851-7441-4353-84a6-0ac58f7811ca",
  "isSidechain": false,
  "requestId": "req_011CazWFr6FR7XP1Xk1rS93o",
  "type": "assistant",
  "uuid": "d15163f4-3b67-4791-b782-f48cecad1bf9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R25WjnLvDrgQKSwCQzfjJK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15040,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2625,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15040,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2625,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15040,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15040
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-13T11:40:55.973Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01PQT51E1tpKqLGxsaiyxeSU`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify SARM/RA-BC κ details",
  "prompt": "I need to verify specific technical details about the SARM/RA-BC paper (arxiv ID 2509.25358). Use WebFetch to read the HTML version at https://arxiv.org/html/2509.25358 and find:\n\n1. Is κ (kappa) a FIXED hyperparameter or derived adaptively? What is its exact value?\n2. How is w̃_i computed? Does it use adaptive running statistics (μ, σ) via Welford's estimator?\n3. What is the exact formula for the hybrid weight w_i?\n4. Any details about how κ relates to task duration or demonstration quality thresholds.\n\nReport the exact quotes and section numbers. Be precise - this is resolving a factual dispute about the paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d15163f4-3b67-4791-b782-f48cecad1bf9",
  "isSidechain": false,
  "requestId": "req_011CazWFr6FR7XP1Xk1rS93o",
  "type": "assistant",
  "uuid": "a4fd94b8-259c-4c2b-96f8-dcfb0bb87bce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R25WjnLvDrgQKSwCQzfjJK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15040,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2625,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15040,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2625,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15040,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15040
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-13T11:41:00.260Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01UWjK3KxnnGZ6YteoXpmRYK`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Find Robometer RSS 2026 paper",
  "prompt": "Search for \"Robometer\" - a general-purpose robotic reward model paper, reportedly at RSS 2026. I need to:\n\n1. Use WebSearch to find this paper with queries like \"Robometer robot reward model RSS 2026\", \"Robometer general purpose robotic reward model\"\n2. Use WebFetch to read the abstract and key details\n3. Report: full title, authors, venue, what it does (reward model trained on 1M+ trajectories?), how it provides dense rewards, and its relevance as a quality estimator for robot demonstration curation.\n\nIf you can't find \"Robometer\" exactly, try variations like \"RoboMeter\" or \"Robo-Meter\"."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4fd94b8-259c-4c2b-96f8-dcfb0bb87bce",
  "isSidechain": false,
  "requestId": "req_011CazWFr6FR7XP1Xk1rS93o",
  "type": "assistant",
  "uuid": "a925a1ae-faa6-4e4a-b271-174b6d365e54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R25WjnLvDrgQKSwCQzfjJK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15040,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2625,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15040,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2625,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15040,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15040
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-13T11:41:03.006Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01MB8G9qQJrV8QqSSfwu7rte`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Find IWR CoRL 2025 paper",
  "prompt": "Search for \"IWR\" - an importance-weighted retrieval paper for imitation learning data selection, reportedly at CoRL 2025. I need to:\n\n1. Use WebSearch with queries like \"IWR importance weighted retrieval imitation learning CoRL 2025\", \"importance weighted retrieval robot learning data selection\", \"importance weighted retrieval demonstration selection\"\n2. Use WebFetch to read the abstract and key details\n3. Report: full title, authors, venue, what it does (importance-weighted data selection using density ratios for IL?), and how it relates to the question of filtering vs. weighting demonstrations.\n\nAlso try searching \"importance weighted data selection robot imitation learning 2025\"."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a925a1ae-faa6-4e4a-b271-174b6d365e54",
  "isSidechain": false,
  "requestId": "req_011CazWFr6FR7XP1Xk1rS93o",
  "type": "assistant",
  "uuid": "2b99e746-d969-4a97-a785-146027c9c6df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R25WjnLvDrgQKSwCQzfjJK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15040,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2625,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15040,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2625,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15040,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15040
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-13T11:41:06.872Z_

<details open><summary>🔧 Tool call — Agent · `toolu_017LsAWo8DF3gNDHmQRhX6vy`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Find Green-VLA paper",
  "prompt": "Search for \"Green-VLA\" - a paper from approximately February 2026 that includes a \"DataQA\" pipeline using heuristic metrics for demonstration filtering. I need to:\n\n1. Use WebSearch with queries like \"Green-VLA DataQA demonstration filtering 2026\", \"Green-VLA robot learning data quality\", \"Green-VLA vision language action\"\n2. Use WebFetch to read the abstract and key details\n3. Report: full title, authors, venue/arXiv date, what DataQA does (heuristic metrics for filtering demonstrations?), and its relevance to principled demo curation.\n\nTry alternative queries if the first ones don't work: \"green VLA data quality assurance robot\", \"efficient VLA data filtering\"."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2b99e746-d969-4a97-a785-146027c9c6df",
  "isSidechain": false,
  "requestId": "req_011CazWFr6FR7XP1Xk1rS93o",
  "type": "assistant",
  "uuid": "5705f47a-d3d7-4684-95f1-e46af42d4137",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R25WjnLvDrgQKSwCQzfjJK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15040,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2625,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15040,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2625,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15040,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15040
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-13T11:41:13.129Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01MbcW7yJsBJHyTQEyBrUvJA`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check RINSE arXiv April 2026 version",
  "prompt": "I need to check the RINSE paper's arXiv version. The paper is about \"smoothness-driven metrics for data quality in imitation learning\" with arXiv ID 2604.23000, posted April 24, 2026.\n\n1. Use WebFetch to read https://arxiv.org/abs/2604.23000 to get the abstract and check for version history\n2. Then try WebFetch on https://arxiv.org/html/2604.23000 to read the full paper content\n3. Specifically look for:\n   - Does the April 2026 version include cross-estimator analysis (comparing smoothness metrics against other quality estimator types)?\n   - Does it include any adaptive strategy selection (choosing between filtering and weighting)?\n   - Does it include any analysis of estimator reliability/rank stability?\n   - Has it been submitted to a main venue (ICML, NeurIPS, CoRL)?\n   - What are the key differences from the ICML 2025 workshop version?\n\nThis is critical - if the new RINSE version already does cross-estimator analysis or adaptive strategy selection, our novelty claim needs adjustment."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5705f47a-d3d7-4684-95f1-e46af42d4137",
  "isSidechain": false,
  "requestId": "req_011CazWFr6FR7XP1Xk1rS93o",
  "type": "assistant",
  "uuid": "0e2b3cfa-859b-422d-a5ed-4434f5cfc762",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R25WjnLvDrgQKSwCQzfjJK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15040,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2625,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15040,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2625,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15040,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15040
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-13T11:41:19.891Z_

<details open><summary>🔧 Tool call — Agent · `toolu_011Xr5e2g8q8PfznnPkwAwYN`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research real-robot eval feasibility",
  "prompt": "I'm working on a paper about robot demonstration curation (filtering vs. weighting) targeting CoRL 2026 (deadline May 28, 2026). Reviewers say sim-only evaluation is weak. I need to understand:\n\n1. Use WebSearch to find: \"CoRL 2026 call for papers\", \"CoRL 2026 submission requirements real robot\" to understand reviewer expectations\n2. Search for \"ICRA 2026 From Data to Decisions VLA Pipelines Real Robots workshop\" to understand community expectations\n3. Search for recent demo curation papers that are sim-only vs. those with real-robot results. Specifically check what SCIZOR, Demo-SCORE, CUPID, TOPReward include for real-robot experiments.\n4. Search for \"VIP robot manipulation real world deployment\" and \"R3M real robot evaluation\" to understand how easy it is to deploy these estimators on real hardware.\n\nReport: (a) Is sim-only acceptable at CoRL 2026 for a primarily theoretical/framework paper? (b) What's the minimum real-robot experiment that would satisfy reviewers? (c) How feasible is adding real-robot experiments in ~2 weeks?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e2b3cfa-859b-422d-a5ed-4434f5cfc762",
  "isSidechain": false,
  "requestId": "req_011CazWFr6FR7XP1Xk1rS93o",
  "type": "assistant",
  "uuid": "b7c860ac-04ce-49ab-aadf-ead3115886a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R25WjnLvDrgQKSwCQzfjJK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15040,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2625,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15040,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2625,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15040,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15040
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-13T11:41:25.855Z_

<details><summary>↩ Tool result · `toolu_01PQT51E1tpKqLGxsaiyxeSU`</summary>

```text
Here are the precise findings from the paper (arXiv: 2509.25358):

---

**1. Is κ (kappa) fixed or adaptive? What is its value?**

κ is a **fixed hyperparameter**, not adaptively derived. It is introduced in **Section 3.2 ("Prior overrides and validity mask")** with the quote:

> "We incorporate lightweight prior knowledge via a threshold κ > 0"

Its exact value is given in **Appendix A.7 ("Implementation Detail")**:

> "The RA-BC hyperparameters are set to **κ = 0.01** and ε = 10⁻⁶"

---

**2. How is w̃\_i computed? Does it use Welford's estimator?**

**Yes**, it uses adaptive running statistics via Welford's estimator. From **Section 3.2 ("Weighting from running statistics")**:

> "RA-BC maintains online running statistics (mean μ and standard deviation σ) of the raw progress deltas {r̂ⱼ} via a numerically stable estimator (Welford)."

The formula is given in **Equation 8**:

> w̃\_i = clip( (r̂\_i − (μ − 2σ)) / (4σ + ε) , 0, 1 )

So w̃\_i is computed by normalizing the raw progress delta r̂\_i against the adaptive running mean and standard deviation, clipped to [0, 1].

---

**3. Exact formula for the hybrid weight w\_i**

From **Equation 9**:

> w\_i = **1**{r̂\_i > κ} + **1**{0 ≤ r̂\_i ≤ κ} · w̃\_i

In words: if the raw progress delta r̂\_i exceeds the fixed threshold κ, the weight is 1 (full inclusion). If r̂\_i falls in [0, κ], the weight falls back to the adaptive soft weight w̃\_i. (Implicitly, if r̂\_i < 0, the weight is 0.)

---

**4. How κ relates to task duration / demonstration quality**

From **Appendix A.7 ("Implementation Detail")**:

> "κ = 0.01 corresponds roughly to a task duration of 1 minute 30 seconds, which represents the threshold for the **top 5% of demonstrations**."

This is the only discussion of how κ was selected -- it is grounded in a quality percentile of the demonstration distribution.

---

**Summary for the dispute:** κ is unambiguously a **fixed** hyperparameter (set to 0.01), not derived adaptively. However, the *soft weight* w̃\_i that operates in the [0, κ] zone **is** computed adaptively using Welford's online estimator for running μ and σ. The hybrid weight w\_i (Eq. 9) combines the fixed-threshold indicator with the adaptive soft weight, giving the method both a hard prior gate (κ) and an adaptive weighting component (w̃\_i).

agentId: ab43434f3f5eeeb76 (use SendMessage with to: 'ab43434f3f5eeeb76' to continue this agent)
&lt;usage>total_tokens: 11866
tool_uses: 2
duration_ms: 29873&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a4fd94b8-259c-4c2b-96f8-dcfb0bb87bce",
  "isSidechain": false,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "type": "user",
  "uuid": "d7219e87-a21a-4113-8c17-44711ce7fb1d",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify specific technical details about the SARM/RA-BC paper (arxiv ID 2509.25358). Use WebFetch to read the HTML version at https://arxiv.org/html/2509.25358 and find:\n\n1. Is κ (kappa) a FIXED hyperparameter or derived adaptively? What is its exact value?\n2. How is w̃_i computed? Does it use adaptive running statistics (μ, σ) via Welford's estimator?\n3. What is the exact formula for the hybrid weight w_i?\n4. Any details about how κ relates to task duration or demonstration quality thresholds.\n\nReport the exact quotes and section numbers. Be precise - this is resolving a factual dispute about the paper.",
    "agentId": "ab43434f3f5eeeb76",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the precise findings from the paper (arXiv: 2509.25358):\n\n---\n\n**1. Is κ (kappa) fixed or adaptive? What is its value?**\n\nκ is a **fixed hyperparameter**, not adaptively derived. It is introduced in **Section 3.2 (\"Prior overrides and validity mask\")** with the quote:\n\n> \"We incorporate lightweight prior knowledge via a threshold κ > 0\"\n\nIts exact value is given in **Appendix A.7 (\"Implementation Detail\")**:\n\n> \"The RA-BC hyperparameters are set to **κ = 0.01** and ε = 10⁻⁶\"\n\n---\n\n**2. How is w̃\\_i computed? Does it use Welford's estimator?**\n\n**Yes**, it uses adaptive running statistics via Welford's estimator. From **Section 3.2 (\"Weighting from running statistics\")**:\n\n> \"RA-BC maintains online running statistics (mean μ and standard deviation σ) of the raw progress deltas {r̂ⱼ} via a numerically stable estimator (Welford).\"\n\nThe formula is given in **Equation 8**:\n\n> w̃\\_i = clip( (r̂\\_i − (μ − 2σ)) / (4σ + ε) , 0, 1 )\n\nSo w̃\\_i is computed by normalizing the raw progress delta r̂\\_i against the adaptive running mean and standard deviation, clipped to [0, 1].\n\n---\n\n**3. Exact formula for the hybrid weight w\\_i**\n\nFrom **Equation 9**:\n\n> w\\_i = **1**{r̂\\_i > κ} + **1**{0 ≤ r̂\\_i ≤ κ} · w̃\\_i\n\nIn words: if the raw progress delta r̂\\_i exceeds the fixed threshold κ, the weight is 1 (full inclusion). If r̂\\_i falls in [0, κ], the weight falls back to the adaptive soft weight w̃\\_i. (Implicitly, if r̂\\_i < 0, the weight is 0.)\n\n---\n\n**4. How κ relates to task duration / demonstration quality**\n\nFrom **Appendix A.7 (\"Implementation Detail\")**:\n\n> \"κ = 0.01 corresponds roughly to a task duration of 1 minute 30 seconds, which represents the threshold for the **top 5% of demonstrations**.\"\n\nThis is the only discussion of how κ was selected -- it is grounded in a quality percentile of the demonstration distribution.\n\n---\n\n**Summary for the dispute:** κ is unambiguously a **fixed** hyperparameter (set to 0.01), not derived adaptively. However, the *soft weight* w̃\\_i that operates in the [0, κ] zone **is** computed adaptively using Welford's online estimator for running μ and σ. The hybrid weight w\\_i (Eq. 9) combines the fixed-threshold indicator with the adaptive soft weight, giving the method both a hard prior gate (κ) and an adaptive weighting component (w̃\\_i)."
      }
    ],
    "totalDurationMs": 29873,
    "totalTokens": 11866,
    "totalToolUseCount": 2,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 10347,
      "output_tokens": 756,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 762
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 756,
          "cache_read_input_tokens": 10347,
          "cache_creation_input_tokens": 762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 762,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 2
    }
  },
  "sourceToolAssistantUUID": "a4fd94b8-259c-4c2b-96f8-dcfb0bb87bce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-13T11:41:28.744Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01JxJHFEmc17gfHM3URPijzZ`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research An et al. assumptions and null results",
  "prompt": "I'm writing a paper about when to use binary filtering vs. continuous weighting for robot demo quality scores. A key claim is that An et al. (ICLR 2021, \"Why Resampling Outperforms Reweighting\") proves resampling > reweighting, but we claim low-variance estimators can overcome this.\n\n1. Use WebSearch to find and then WebFetch to read An et al. 2021's key assumptions. Specifically: what are the exact conditions under which their theorem holds? (bounded weights, SGD with constant LR, etc.) Do they discuss Adam optimizer? Do they discuss cases where their result doesn't hold?\n\n2. Search for \"Byrd Lipton importance weighting deep learning ICML 2019\" and check: do they show that importance weighting has NO effect in overparameterized networks, or diminishing effect? What are the implications for the filter-vs-weight question?\n\n3. Search for any papers from 2024-2026 that empirically test resampling vs. reweighting in imitation learning or offline RL specifically. Any evidence that the choice matters or doesn't matter?\n\n4. Search for \"IQL expectile regression Q-value variance\" to understand whether IQL's expectile regression already reduces Q-value variance compared to standard TD, which could undermine the \"high variance\" characterization.\n\nReport findings concisely with exact quotes where relevant."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d7219e87-a21a-4113-8c17-44711ce7fb1d",
  "isSidechain": false,
  "requestId": "req_011CazWFr6FR7XP1Xk1rS93o",
  "type": "assistant",
  "uuid": "ab198120-f0a0-48e7-8915-5866b3e8c3e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R25WjnLvDrgQKSwCQzfjJK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15040,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2625,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15040,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2625,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 15040,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15040
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-13T11:41:50.940Z_

<details><summary>↩ Tool result · `toolu_01MbcW7yJsBJHyTQEyBrUvJA`</summary>

```text
Here is my analysis of the RINSE paper (arXiv 2604.23000):

---

**Paper**: "Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning"
**Authors**: Soham Kulkarni, Raayan Dhar, Yuchen Cui
**Posted**: April 24, 2026 (v1 only, no revisions yet)
**Length**: 8 pages, 5 figures

---

**Answers to your specific questions:**

1. **Cross-estimator analysis (comparing smoothness metrics against other quality estimator types)?** -- **Not present.** The paper does not compare SAL/TED against other estimator families like reward models, confidence scores, or ensemble disagreement. They compare against random subset baselines and show correlation with Re-Mix allocations, but there is no systematic cross-estimator comparison.

2. **Adaptive strategy selection (choosing between filtering and weighting)?** -- **Not present.** Both filtering and reweighting are evaluated in separate experiment sections (IV-C/D for filtering, IV-B for reweighting via Re-Mix), but there is no mechanism or analysis for choosing between them based on dataset characteristics. They are treated as independent use-cases.

3. **Estimator reliability / rank stability analysis?** -- **Limited only.** They report Spearman correlations (rho >= 0.89) with Re-Mix allocations across normalization methods, but there is no comprehensive cross-environment or cross-task rank stability analysis of the kind you would need for a reliability study.

4. **Venue submission?** -- **No venue indicated.** The paper is an arXiv preprint only (cs.RO). No mention of ICML, NeurIPS, CoRL, or any other conference submission in the comments or text. At 8 pages it reads like a conference submission length, but no target is disclosed.

5. **Differences from ICML 2025 workshop version?** -- **No prior workshop version is mentioned.** The paper does not reference itself as an extension of earlier work. This appears to be presented as a standalone contribution. (If there was a workshop version, they don't acknowledge it here.)

---

**Bottom line for your novelty claim**: The April 2026 RINSE paper does **none** of the three things you were concerned about -- no cross-estimator analysis, no adaptive strategy selection, and no substantive rank stability analysis. Their contribution stays squarely within smoothness-based metrics (SAL and TED) applied to filtering, retrieval, and reweighting, with comparisons limited to random baselines and correlation with Re-Mix. They even explicitly state in the conclusion that "smoothness is necessary but not sufficient for quality," which leaves clear room for work on when and why smoothness-based estimators fail relative to other estimator families.

Your novelty on cross-estimator comparison, adaptive filtering-vs-weighting selection, and estimator reliability analysis appears to be safe relative to this version of the paper. That said, since this is only v1 with no stated venue, it is worth monitoring for a v2 revision that could expand the scope before submission.

agentId: a1a581854aec890d4 (use SendMessage with to: 'a1a581854aec890d4' to continue this agent)
&lt;usage>total_tokens: 12602
tool_uses: 3
duration_ms: 37808&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e2b3cfa-859b-422d-a5ed-4434f5cfc762",
  "isSidechain": false,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "type": "user",
  "uuid": "bd16b771-db95-4ede-995f-9dc53ab6878e",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to check the RINSE paper's arXiv version. The paper is about \"smoothness-driven metrics for data quality in imitation learning\" with arXiv ID 2604.23000, posted April 24, 2026.\n\n1. Use WebFetch to read https://arxiv.org/abs/2604.23000 to get the abstract and check for version history\n2. Then try WebFetch on https://arxiv.org/html/2604.23000 to read the full paper content\n3. Specifically look for:\n   - Does the April 2026 version include cross-estimator analysis (comparing smoothness metrics against other quality estimator types)?\n   - Does it include any adaptive strategy selection (choosing between filtering and weighting)?\n   - Does it include any analysis of estimator reliability/rank stability?\n   - Has it been submitted to a main venue (ICML, NeurIPS, CoRL)?\n   - What are the key differences from the ICML 2025 workshop version?\n\nThis is critical - if the new RINSE version already does cross-estimator analysis or adaptive strategy selection, our novelty claim needs adjustment.",
    "agentId": "a1a581854aec890d4",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is my analysis of the RINSE paper (arXiv 2604.23000):\n\n---\n\n**Paper**: \"Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning\"\n**Authors**: Soham Kulkarni, Raayan Dhar, Yuchen Cui\n**Posted**: April 24, 2026 (v1 only, no revisions yet)\n**Length**: 8 pages, 5 figures\n\n---\n\n**Answers to your specific questions:**\n\n1. **Cross-estimator analysis (comparing smoothness metrics against other quality estimator types)?** -- **Not present.** The paper does not compare SAL/TED against other estimator families like reward models, confidence scores, or ensemble disagreement. They compare against random subset baselines and show correlation with Re-Mix allocations, but there is no systematic cross-estimator comparison.\n\n2. **Adaptive strategy selection (choosing between filtering and weighting)?** -- **Not present.** Both filtering and reweighting are evaluated in separate experiment sections (IV-C/D for filtering, IV-B for reweighting via Re-Mix), but there is no mechanism or analysis for choosing between them based on dataset characteristics. They are treated as independent use-cases.\n\n3. **Estimator reliability / rank stability analysis?** -- **Limited only.** They report Spearman correlations (rho >= 0.89) with Re-Mix allocations across normalization methods, but there is no comprehensive cross-environment or cross-task rank stability analysis of the kind you would need for a reliability study.\n\n4. **Venue submission?** -- **No venue indicated.** The paper is an arXiv preprint only (cs.RO). No mention of ICML, NeurIPS, CoRL, or any other conference submission in the comments or text. At 8 pages it reads like a conference submission length, but no target is disclosed.\n\n5. **Differences from ICML 2025 workshop version?** -- **No prior workshop version is mentioned.** The paper does not reference itself as an extension of earlier work. This appears to be presented as a standalone contribution. (If there was a workshop version, they don't acknowledge it here.)\n\n---\n\n**Bottom line for your novelty claim**: The April 2026 RINSE paper does **none** of the three things you were concerned about -- no cross-estimator analysis, no adaptive strategy selection, and no substantive rank stability analysis. Their contribution stays squarely within smoothness-based metrics (SAL and TED) applied to filtering, retrieval, and reweighting, with comparisons limited to random baselines and correlation with Re-Mix. They even explicitly state in the conclusion that \"smoothness is necessary but not sufficient for quality,\" which leaves clear room for work on when and why smoothness-based estimators fail relative to other estimator families.\n\nYour novelty on cross-estimator comparison, adaptive filtering-vs-weighting selection, and estimator reliability analysis appears to be safe relative to this version of the paper. That said, since this is only v1 with no stated venue, it is worth monitoring for a v2 revision that could expand the scope before submission."
      }
    ],
    "totalDurationMs": 37808,
    "totalTokens": 12602,
    "totalToolUseCount": 3,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1454,
      "cache_read_input_tokens": 10428,
      "output_tokens": 719,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1454
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 719,
          "cache_read_input_tokens": 10428,
          "cache_creation_input_tokens": 1454,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1454,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 3
    }
  },
  "sourceToolAssistantUUID": "0e2b3cfa-859b-422d-a5ed-4434f5cfc762",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"When to Filter, When to Weight: A Bias-Variance Framework for Adaptive…",
  "leafUuid": "bd16b771-db95-4ede-995f-9dc53ab6878e",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Adaptive demo curation via estimator reliability",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96"
}
```

---

### Tool result

_source line 21 · 2026-05-13T11:42:02.301Z_

<details><summary>↩ Tool result · `toolu_01UWjK3KxnnGZ6YteoXpmRYK`</summary>

```text
Now I have comprehensive information. Here is the full report:

---

## Robometer: Full Paper Report

**Full Title:** Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons

**Authors (17 total, * = equal contribution):**
Anthony Liang\*, Yigit Korkmaz\*, Jiahui Zhang, Minyoung Hwang, Abrar Anwar, Sidhant Kaushik, Aditya Shah, Alex S. Huang, Luke Zettlemoyer, Dieter Fox, Yu Xiang, Anqi Li, Andreea Bobu, Abhishek Gupta, Stephen Tu, Erdem Biyik, and Jesse Zhang

**Affiliations:** University of Southern California, UT Dallas, MIT, University of Washington, Ai2, NVIDIA, and independent researchers.

**Venue:** Robotics: Science and Systems (RSS) 2026. ArXiv preprint: 2603.02115 (submitted March 2, 2026).

---

### What It Does

Robometer is a **dense, general-purpose, video-language robotic reward model**. It addresses a fundamental scaling bottleneck: prior reward models are trained to predict absolute task progress from expert demonstrations only, providing local frame-level supervision. This scales poorly to large datasets where failed and suboptimal trajectories are abundant and assigning dense progress labels to them is ambiguous.

Robometer solves this via a **dual training objective** combining:

1. **Intra-trajectory progress supervision** -- a frame-level progress loss (plus a success prediction loss) that anchors the magnitude of predicted rewards by regressing per-frame progress and success values on expert demonstration data. Progress is predicted as a categorical distribution over N bins, with the continuous value obtained by taking the expectation over bin centers.

2. **Inter-trajectory preference supervision** -- a trajectory-comparison preference loss that imposes global ordering constraints across pairs of trajectories for the same task. This enables effective learning from both real and synthetically augmented failed/suboptimal trajectories without needing dense progress labels for them.

The composite loss is: L = L_pref + L_prog + L_succ

---

### Training Data: RBM-1M

The model is trained on **RBM-1M**, a massive reward-learning dataset comprising:
- **1M+ trajectories** total
- **21 robot embodiments**
- **140,000+ trajectories from mixed-expertise datasets** (including suboptimal and failure data)
- Diverse tasks spanning manipulation and other robotic domains

---

### How It Provides Dense Rewards

Robometer inserts **progress tokens** at each video frame, producing dense, frame-level progress estimates during inference. For any given video frame and language task instruction, the model outputs:
- A continuous **progress value** (how far along the task is)
- A **success prediction** (binary task completion)
- A **preference score** (pairwise comparison between trajectories)

This means it can assign a reward signal at every timestep, not just at episode termination -- critical for effective RL training.

---

### Relevance as a Quality Estimator for Robot Demonstration Curation

This is one of Robometer's explicitly evaluated downstream applications, called **"Data Retrieval + IL" (Imitation Learning)**. The model functions as a quality estimator in two ways:

1. **Preference-based pairwise trajectory comparisons** -- given two trajectories, Robometer can judge which one better satisfies a task instruction, enabling ranking and filtering of demonstration datasets.

2. **Progress-based ranking** -- by computing per-timestep reward/progress values for each trajectory, Robometer can rank trajectories (or sub-trajectories) by quality and retrieve the most relevant ones for a given task instruction.

The paper reports that Robometer **consistently achieves higher retrieval relevance** compared to prior methods when filtering trajectories for downstream imitation learning. This makes it directly applicable as a scalable quality filter for curating large, noisy robot demonstration datasets -- you can use it to automatically identify and select the highest-quality demonstrations from a mixed-quality corpus.

---

### Evaluated Downstream Applications (5 total)
1. Model-free online RL
2. Model-based online RL
3. Offline RL
4. Failure detection
5. Data retrieval for imitation learning (demonstration curation)

Across all benchmarks and real-world evaluations, Robometer learns more generalizable reward functions than prior methods. Code, model weights, and dataset are publicly available.

---

Sources:
- [Robometer Project Page](https://robometer.github.io/)
- [ArXiv Paper (abs)](https://arxiv.org/abs/2603.02115)
- [ArXiv Paper (HTML)](https://arxiv.org/html/2603.02115v1)
- [GitHub Repository](https://github.com/robometer/robometer)
- [AlphaXiv Discussion](https://www.alphaxiv.org/overview/2603.02115)

agentId: a6897071c75c75e33 (use SendMessage with to: 'a6897071c75c75e33' to continue this agent)
&lt;usage>total_tokens: 16489
tool_uses: 7
duration_ms: 62038&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a925a1ae-faa6-4e4a-b271-174b6d365e54",
  "isSidechain": false,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "type": "user",
  "uuid": "fa724330-ced2-4e7a-bafc-5cbb697e759b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for \"Robometer\" - a general-purpose robotic reward model paper, reportedly at RSS 2026. I need to:\n\n1. Use WebSearch to find this paper with queries like \"Robometer robot reward model RSS 2026\", \"Robometer general purpose robotic reward model\"\n2. Use WebFetch to read the abstract and key details\n3. Report: full title, authors, venue, what it does (reward model trained on 1M+ trajectories?), how it provides dense rewards, and its relevance as a quality estimator for robot demonstration curation.\n\nIf you can't find \"Robometer\" exactly, try variations like \"RoboMeter\" or \"Robo-Meter\".",
    "agentId": "a6897071c75c75e33",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Here is the full report:\n\n---\n\n## Robometer: Full Paper Report\n\n**Full Title:** Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons\n\n**Authors (17 total, * = equal contribution):**\nAnthony Liang\\*, Yigit Korkmaz\\*, Jiahui Zhang, Minyoung Hwang, Abrar Anwar, Sidhant Kaushik, Aditya Shah, Alex S. Huang, Luke Zettlemoyer, Dieter Fox, Yu Xiang, Anqi Li, Andreea Bobu, Abhishek Gupta, Stephen Tu, Erdem Biyik, and Jesse Zhang\n\n**Affiliations:** University of Southern California, UT Dallas, MIT, University of Washington, Ai2, NVIDIA, and independent researchers.\n\n**Venue:** Robotics: Science and Systems (RSS) 2026. ArXiv preprint: 2603.02115 (submitted March 2, 2026).\n\n---\n\n### What It Does\n\nRobometer is a **dense, general-purpose, video-language robotic reward model**. It addresses a fundamental scaling bottleneck: prior reward models are trained to predict absolute task progress from expert demonstrations only, providing local frame-level supervision. This scales poorly to large datasets where failed and suboptimal trajectories are abundant and assigning dense progress labels to them is ambiguous.\n\nRobometer solves this via a **dual training objective** combining:\n\n1. **Intra-trajectory progress supervision** -- a frame-level progress loss (plus a success prediction loss) that anchors the magnitude of predicted rewards by regressing per-frame progress and success values on expert demonstration data. Progress is predicted as a categorical distribution over N bins, with the continuous value obtained by taking the expectation over bin centers.\n\n2. **Inter-trajectory preference supervision** -- a trajectory-comparison preference loss that imposes global ordering constraints across pairs of trajectories for the same task. This enables effective learning from both real and synthetically augmented failed/suboptimal trajectories without needing dense progress labels for them.\n\nThe composite loss is: L = L_pref + L_prog + L_succ\n\n---\n\n### Training Data: RBM-1M\n\nThe model is trained on **RBM-1M**, a massive reward-learning dataset comprising:\n- **1M+ trajectories** total\n- **21 robot embodiments**\n- **140,000+ trajectories from mixed-expertise datasets** (including suboptimal and failure data)\n- Diverse tasks spanning manipulation and other robotic domains\n\n---\n\n### How It Provides Dense Rewards\n\nRobometer inserts **progress tokens** at each video frame, producing dense, frame-level progress estimates during inference. For any given video frame and language task instruction, the model outputs:\n- A continuous **progress value** (how far along the task is)\n- A **success prediction** (binary task completion)\n- A **preference score** (pairwise comparison between trajectories)\n\nThis means it can assign a reward signal at every timestep, not just at episode termination -- critical for effective RL training.\n\n---\n\n### Relevance as a Quality Estimator for Robot Demonstration Curation\n\nThis is one of Robometer's explicitly evaluated downstream applications, called **\"Data Retrieval + IL\" (Imitation Learning)**. The model functions as a quality estimator in two ways:\n\n1. **Preference-based pairwise trajectory comparisons** -- given two trajectories, Robometer can judge which one better satisfies a task instruction, enabling ranking and filtering of demonstration datasets.\n\n2. **Progress-based ranking** -- by computing per-timestep reward/progress values for each trajectory, Robometer can rank trajectories (or sub-trajectories) by quality and retrieve the most relevant ones for a given task instruction.\n\nThe paper reports that Robometer **consistently achieves higher retrieval relevance** compared to prior methods when filtering trajectories for downstream imitation learning. This makes it directly applicable as a scalable quality filter for curating large, noisy robot demonstration datasets -- you can use it to automatically identify and select the highest-quality demonstrations from a mixed-quality corpus.\n\n---\n\n### Evaluated Downstream Applications (5 total)\n1. Model-free online RL\n2. Model-based online RL\n3. Offline RL\n4. Failure detection\n5. Data retrieval for imitation learning (demonstration curation)\n\nAcross all benchmarks and real-world evaluations, Robometer learns more generalizable reward functions than prior methods. Code, model weights, and dataset are publicly available.\n\n---\n\nSources:\n- [Robometer Project Page](https://robometer.github.io/)\n- [ArXiv Paper (abs)](https://arxiv.org/abs/2603.02115)\n- [ArXiv Paper (HTML)](https://arxiv.org/html/2603.02115v1)\n- [GitHub Repository](https://github.com/robometer/robometer)\n- [AlphaXiv Discussion](https://www.alphaxiv.org/overview/2603.02115)"
      }
    ],
    "totalDurationMs": 62038,
    "totalTokens": 16489,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 556,
      "cache_read_input_tokens": 14756,
      "output_tokens": 1176,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 556
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1176,
          "cache_read_input_tokens": 14756,
          "cache_creation_input_tokens": 556,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 556,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 7
    }
  },
  "sourceToolAssistantUUID": "a925a1ae-faa6-4e4a-b271-174b6d365e54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-13T11:42:14.317Z_

<details><summary>↩ Tool result · `toolu_017LsAWo8DF3gNDHmQRhX6vy`</summary>

```text
I now have all the details needed. Here is the full report.

---

## Green-VLA Paper Report

**Full Title:** Green-VLA: Staged Vision-Language-Action Model for Generalist Robots

**Authors:** 28+ authors from **Sber Robotics Center**, including I. Apanasevich, M. Artemyev, R. Babakyan, P. Fedotova, D. Grankin, E. Kupryashin, A. Misailidi, D. Nerus, A. Nutalapati, G. Sidorov, I. Efremov, M. Gerasyov, D. Pikurov, Y. Senchenko, S. Davidenko, D. Kulikov, M. Sultankin, K. Askarbek, O. Shamanin, D. Statovoy, E. Zalyaev, I. Zorin, A. Letkin, E. Rusakov, A. Silchenko, V. Vorobyov, S. Sobolnikov, A. Postnikov, and others.

**Venue / Date:** arXiv preprint (cs.RO), arXiv ID **2602.00919**. Submitted January 31, 2026 (v1), revised March 7, 2026 (v2). No conference venue listed; it is a preprint.

---

### What Green-VLA Does (Overall)

Green-VLA is a ~4B-parameter staged VLA framework for generalist robots, with a five-stage curriculum: (L0) foundational VLM pretraining, (L1) multimodal grounding, (R0) multi-embodiment pretraining, (R1) embodiment-specific adaptation, and (R2) reinforcement-learning policy alignment. It targets the "Green" humanoid robot (32 DoF upper body) but generalizes across humanoids, mobile manipulators, and fixed-base arms via a unified, embodiment-aware action interface.

---

### The DataQA Pipeline -- Heuristic Metrics for Demonstration Filtering

DataQA is Green-VLA's automated data quality assurance pipeline that filters 3,000+ hours of raw demonstrations before training. It uses the following heuristic metrics:

1. **Basic sanity checks:** Removes episodes with missing cameras/frames, episodes that are too short or suspiciously long, and episodes lacking sufficient motion activity.

2. **Tremble Score (Jitter Detection):** Identifies erratic, jerky motions using the formula `S_tremble = |s_dot_smooth - s_dot| / (|s_dot_smooth| + |s_dot|)`, where `s_dot` is the velocity trajectory and `s_dot_smooth` is its Gaussian-smoothed version. High tremble scores indicate poor-quality teleoperator demonstrations.

3. **Sharpness (S_sharp):** Assesses image quality using Laplacian standard deviation scores computed on 4x4 pixel blocks, with max-pooling across 16x16 regions. The median regional sharpness score represents overall episode visual quality -- filtering out blurry or degraded visual data.

4. **Visual Diversity (D_vis):** Measures temporal variance of spatially-averaged DINOv3 feature representations: `D_vis = E_d[std_t(E_s[f_{t,s,d}])]`. This ensures episodes contain meaningful visual variation rather than static or repetitive scenes.

5. **State-Space Diversity (D_state):** Computed as `D_state = sqrt(tr(Cov(s)))` -- the square root of the trace of the robot state covariance matrix. Filters out episodes where the robot barely moves or repeats the same state.

6. **Optical-flow-based Temporal Alignment:** Resamples actions using monotonic cubic splines to normalize effective motion per step, aligning motion statistics across heterogeneous datasets collected at different speeds and frame rates.

7. **Trajectory Smoothing:** Applies smoothing to reduce high-frequency noise in action trajectories post-filtering.

---

### Relevance to Principled Demonstration Curation

Green-VLA's DataQA pipeline is highly relevant to principled demo curation for several reasons:

- **Quality over quantity thesis:** The paper's central argument is that a staged training pipeline emphasizing quality alignment, unified action spaces, and RL refinement outperforms raw data scaling. The broader 2026 consensus they cite is that a well-curated 500-demo fine-tune of a 7B VLA can outperform a poorly curated fine-tune of a 70B model.

- **Multi-metric, automated filtering:** Rather than relying on a single quality score or manual inspection, DataQA combines perceptual metrics (sharpness, visual diversity via DINOv3), kinematic metrics (jitter/tremble, state-space diversity), and temporal normalization (optical-flow alignment). This provides a principled, reproducible, multi-dimensional quality assessment.

- **Addresses real-world data messiness:** The pipeline explicitly handles problems endemic to large-scale teleoperation data collection -- jerky operators, camera failures, uninformative episodes, and speed mismatches across different data sources and embodiments.

- **Enables multi-embodiment training:** By normalizing and filtering across heterogeneous data sources, DataQA makes it feasible to train a single policy on demonstrations from very different robots without low-quality data from one source degrading performance on others.

- **Limitation -- heuristics, not learned:** The metrics are hand-designed heuristics rather than learned quality predictors. This is transparent and interpretable but may miss subtler quality dimensions (e.g., task relevance, strategy optimality). A more principled approach might learn quality scores end-to-end or use outcome-based filtering (success/failure labels).

---

Sources:
- [Green-VLA arXiv abstract](https://arxiv.org/abs/2602.00919)
- [Green-VLA full paper (HTML)](https://arxiv.org/html/2602.00919v1)
- [Green-VLA project page](https://greenvla.github.io/)
- [Green-VLA on HuggingFace Papers](https://huggingface.co/papers/2602.00919)
- [Green-VLA GitHub repository](https://github.com/greenvla/GreenVLA)

agentId: ab68eb3795eb14002 (use SendMessage with to: 'ab68eb3795eb14002' to continue this agent)
&lt;usage>total_tokens: 16863
tool_uses: 7
duration_ms: 67442&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5705f47a-d3d7-4684-95f1-e46af42d4137",
  "isSidechain": false,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "type": "user",
  "uuid": "a912a997-5349-41c5-ae24-bdefd58f04e4",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for \"Green-VLA\" - a paper from approximately February 2026 that includes a \"DataQA\" pipeline using heuristic metrics for demonstration filtering. I need to:\n\n1. Use WebSearch with queries like \"Green-VLA DataQA demonstration filtering 2026\", \"Green-VLA robot learning data quality\", \"Green-VLA vision language action\"\n2. Use WebFetch to read the abstract and key details\n3. Report: full title, authors, venue/arXiv date, what DataQA does (heuristic metrics for filtering demonstrations?), and its relevance to principled demo curation.\n\nTry alternative queries if the first ones don't work: \"green VLA data quality assurance robot\", \"efficient VLA data filtering\".",
    "agentId": "ab68eb3795eb14002",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have all the details needed. Here is the full report.\n\n---\n\n## Green-VLA Paper Report\n\n**Full Title:** Green-VLA: Staged Vision-Language-Action Model for Generalist Robots\n\n**Authors:** 28+ authors from **Sber Robotics Center**, including I. Apanasevich, M. Artemyev, R. Babakyan, P. Fedotova, D. Grankin, E. Kupryashin, A. Misailidi, D. Nerus, A. Nutalapati, G. Sidorov, I. Efremov, M. Gerasyov, D. Pikurov, Y. Senchenko, S. Davidenko, D. Kulikov, M. Sultankin, K. Askarbek, O. Shamanin, D. Statovoy, E. Zalyaev, I. Zorin, A. Letkin, E. Rusakov, A. Silchenko, V. Vorobyov, S. Sobolnikov, A. Postnikov, and others.\n\n**Venue / Date:** arXiv preprint (cs.RO), arXiv ID **2602.00919**. Submitted January 31, 2026 (v1), revised March 7, 2026 (v2). No conference venue listed; it is a preprint.\n\n---\n\n### What Green-VLA Does (Overall)\n\nGreen-VLA is a ~4B-parameter staged VLA framework for generalist robots, with a five-stage curriculum: (L0) foundational VLM pretraining, (L1) multimodal grounding, (R0) multi-embodiment pretraining, (R1) embodiment-specific adaptation, and (R2) reinforcement-learning policy alignment. It targets the \"Green\" humanoid robot (32 DoF upper body) but generalizes across humanoids, mobile manipulators, and fixed-base arms via a unified, embodiment-aware action interface.\n\n---\n\n### The DataQA Pipeline -- Heuristic Metrics for Demonstration Filtering\n\nDataQA is Green-VLA's automated data quality assurance pipeline that filters 3,000+ hours of raw demonstrations before training. It uses the following heuristic metrics:\n\n1. **Basic sanity checks:** Removes episodes with missing cameras/frames, episodes that are too short or suspiciously long, and episodes lacking sufficient motion activity.\n\n2. **Tremble Score (Jitter Detection):** Identifies erratic, jerky motions using the formula `S_tremble = |s_dot_smooth - s_dot| / (|s_dot_smooth| + |s_dot|)`, where `s_dot` is the velocity trajectory and `s_dot_smooth` is its Gaussian-smoothed version. High tremble scores indicate poor-quality teleoperator demonstrations.\n\n3. **Sharpness (S_sharp):** Assesses image quality using Laplacian standard deviation scores computed on 4x4 pixel blocks, with max-pooling across 16x16 regions. The median regional sharpness score represents overall episode visual quality -- filtering out blurry or degraded visual data.\n\n4. **Visual Diversity (D_vis):** Measures temporal variance of spatially-averaged DINOv3 feature representations: `D_vis = E_d[std_t(E_s[f_{t,s,d}])]`. This ensures episodes contain meaningful visual variation rather than static or repetitive scenes.\n\n5. **State-Space Diversity (D_state):** Computed as `D_state = sqrt(tr(Cov(s)))` -- the square root of the trace of the robot state covariance matrix. Filters out episodes where the robot barely moves or repeats the same state.\n\n6. **Optical-flow-based Temporal Alignment:** Resamples actions using monotonic cubic splines to normalize effective motion per step, aligning motion statistics across heterogeneous datasets collected at different speeds and frame rates.\n\n7. **Trajectory Smoothing:** Applies smoothing to reduce high-frequency noise in action trajectories post-filtering.\n\n---\n\n### Relevance to Principled Demonstration Curation\n\nGreen-VLA's DataQA pipeline is highly relevant to principled demo curation for several reasons:\n\n- **Quality over quantity thesis:** The paper's central argument is that a staged training pipeline emphasizing quality alignment, unified action spaces, and RL refinement outperforms raw data scaling. The broader 2026 consensus they cite is that a well-curated 500-demo fine-tune of a 7B VLA can outperform a poorly curated fine-tune of a 70B model.\n\n- **Multi-metric, automated filtering:** Rather than relying on a single quality score or manual inspection, DataQA combines perceptual metrics (sharpness, visual diversity via DINOv3), kinematic metrics (jitter/tremble, state-space diversity), and temporal normalization (optical-flow alignment). This provides a principled, reproducible, multi-dimensional quality assessment.\n\n- **Addresses real-world data messiness:** The pipeline explicitly handles problems endemic to large-scale teleoperation data collection -- jerky operators, camera failures, uninformative episodes, and speed mismatches across different data sources and embodiments.\n\n- **Enables multi-embodiment training:** By normalizing and filtering across heterogeneous data sources, DataQA makes it feasible to train a single policy on demonstrations from very different robots without low-quality data from one source degrading performance on others.\n\n- **Limitation -- heuristics, not learned:** The metrics are hand-designed heuristics rather than learned quality predictors. This is transparent and interpretable but may miss subtler quality dimensions (e.g., task relevance, strategy optimality). A more principled approach might learn quality scores end-to-end or use outcome-based filtering (success/failure labels).\n\n---\n\nSources:\n- [Green-VLA arXiv abstract](https://arxiv.org/abs/2602.00919)\n- [Green-VLA full paper (HTML)](https://arxiv.org/html/2602.00919v1)\n- [Green-VLA project page](https://greenvla.github.io/)\n- [Green-VLA on HuggingFace Papers](https://huggingface.co/papers/2602.00919)\n- [Green-VLA GitHub repository](https://github.com/greenvla/GreenVLA)"
      }
    ],
    "totalDurationMs": 67442,
    "totalTokens": 16863,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 446,
      "cache_read_input_tokens": 14910,
      "output_tokens": 1506,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 446
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1506,
          "cache_read_input_tokens": 14910,
          "cache_creation_input_tokens": 446,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 446,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 7
    }
  },
  "sourceToolAssistantUUID": "5705f47a-d3d7-4684-95f1-e46af42d4137",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-13T11:42:17.595Z_

<details><summary>↩ Tool result · `toolu_01MB8G9qQJrV8QqSSfwu7rte`</summary>

```text
Here is a comprehensive report on the IWR paper.

---

**Full Title:** "Data Retrieval with Importance Weights for Few-Shot Imitation Learning"

**Authors:** Amber Xie, Rahul Chand, Dorsa Sadigh, Joey Hejna (all Stanford)

**Venue:** The 9th Conference on Robot Learning (CoRL 2025) -- Oral presentation. Published in Proceedings of Machine Learning Research, Volume 305, pages 1-16. Conference dates: September 27-30, 2025.

**ArXiv:** 2509.01657 (submitted September 1, 2025)

---

### What It Does

IWR addresses the problem of **retrieval-based few-shot imitation learning**: given a small target demonstration dataset and a large heterogeneous prior dataset, how do you select the most useful prior data to augment training?

**Key insight:** Existing retrieval methods (like Behavior Retrieval) select prior data points based on minimum L2 distance to the target set in a learned latent space. The paper proves this is mathematically equivalent to the **limiting case of a Gaussian KDE** as bandwidth h approaches 0. This means prior methods were implicitly doing density estimation of the target distribution, but with maximally high variance (nearest-neighbor = zero-bandwidth KDE) and **without accounting for the prior data distribution at all**.

**The method:** IWR computes importance weights as the **density ratio p_target / p_prior**, where both densities are estimated via Gaussian KDE over learned state-action embeddings. A prior data point is retrieved if this ratio exceeds a threshold eta. The bandwidth is set using a multiplicative factor of Scott's rule: h = c * |D|^(-1/(d+4)).

**Why the ratio matters:** Without the prior density in the denominator, retrieval is biased toward regions where the prior dataset happens to be dense (e.g., early timesteps in demonstrations, common objects). By normalizing by p_prior, IWR upweights samples that are relevant to the target task but underrepresented in the prior -- such as later-stage demonstration steps or uncommon object interactions.

---

### Filtering vs. Weighting -- The Central Question

This is where IWR sits in an interesting middle ground:

1. **It uses soft/smooth density estimation** (Gaussian KDE with reasonable bandwidth) rather than the hard nearest-neighbor approach of prior work, which considers all data points when estimating densities rather than just the single closest point.

2. **But it applies a hard threshold for final selection**: data points where p_target/p_prior > eta are included; others are excluded. This is binary filtering, not continuous weighting.

3. **It does NOT do importance-weighted training**: The authors explicitly note that "IWR is still a biased estimate, as we do not perform importance sampling, but only retrieve based on importance weights." They chose hard thresholding over true importance resampling because it "easily integrates with prior methods."

So IWR occupies a hybrid position: the **selection criterion** is based on continuous density ratios (a weighting idea), but the **output** is a hard-filtered subset (a filtering operation). The density ratio informs *which* demonstrations to include, but once selected, all retrieved data points are treated equally during policy training.

---

### Key Results

- **Simulation (LIBERO):** +5.8% success rate over Behavior Retrieval, +4.4% over Flow Retrieval, +5.8% over SAILOR
- **Real-world (Bridge dataset):** +30% average success rate over Behavior Retrieval, with the most dramatic gains on long-horizon and complex tasks
- **Ablations:** Smoother KDEs (larger bandwidth) perform slightly better on average; the prior-density normalization is critical to the gains
- On simple tasks where baseline retrieval already works well (>50% relevant retrievals), IWR offers minimal additional benefit

---

### Key Files/URLs

- ArXiv: `https://arxiv.org/abs/2509.01657`
- Project page: `https://rahulschand.github.io/iwr/` and `https://sites.google.com/stanford.edu/iwr`
- Proceedings: `https://proceedings.mlr.press/v305/xie25a.html`

Sources:
- [ArXiv Abstract](https://arxiv.org/abs/2509.01657)
- [ArXiv HTML Full Paper](https://arxiv.org/html/2509.01657)
- [PMLR Proceedings](https://proceedings.mlr.press/v305/xie25a.html)
- [Project Page (Rahul Chand)](https://rahulschand.github.io/iwr/)
- [Stanford Project Page](https://sites.google.com/stanford.edu/iwr)
- [EmergentMind Topic Page](https://www.emergentmind.com/topics/importance-weighted-retrieval-iwr)

agentId: ae8490a92fcb2dd4d (use SendMessage with to: 'ae8490a92fcb2dd4d' to continue this agent)
&lt;usage>total_tokens: 18449
tool_uses: 9
duration_ms: 74584&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b99e746-d969-4a97-a785-146027c9c6df",
  "isSidechain": false,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "type": "user",
  "uuid": "6bf6fd21-e547-4010-a938-cdc43ef31cd8",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for \"IWR\" - an importance-weighted retrieval paper for imitation learning data selection, reportedly at CoRL 2025. I need to:\n\n1. Use WebSearch with queries like \"IWR importance weighted retrieval imitation learning CoRL 2025\", \"importance weighted retrieval robot learning data selection\", \"importance weighted retrieval demonstration selection\"\n2. Use WebFetch to read the abstract and key details\n3. Report: full title, authors, venue, what it does (importance-weighted data selection using density ratios for IL?), and how it relates to the question of filtering vs. weighting demonstrations.\n\nAlso try searching \"importance weighted data selection robot imitation learning 2025\".",
    "agentId": "ae8490a92fcb2dd4d",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is a comprehensive report on the IWR paper.\n\n---\n\n**Full Title:** \"Data Retrieval with Importance Weights for Few-Shot Imitation Learning\"\n\n**Authors:** Amber Xie, Rahul Chand, Dorsa Sadigh, Joey Hejna (all Stanford)\n\n**Venue:** The 9th Conference on Robot Learning (CoRL 2025) -- Oral presentation. Published in Proceedings of Machine Learning Research, Volume 305, pages 1-16. Conference dates: September 27-30, 2025.\n\n**ArXiv:** 2509.01657 (submitted September 1, 2025)\n\n---\n\n### What It Does\n\nIWR addresses the problem of **retrieval-based few-shot imitation learning**: given a small target demonstration dataset and a large heterogeneous prior dataset, how do you select the most useful prior data to augment training?\n\n**Key insight:** Existing retrieval methods (like Behavior Retrieval) select prior data points based on minimum L2 distance to the target set in a learned latent space. The paper proves this is mathematically equivalent to the **limiting case of a Gaussian KDE** as bandwidth h approaches 0. This means prior methods were implicitly doing density estimation of the target distribution, but with maximally high variance (nearest-neighbor = zero-bandwidth KDE) and **without accounting for the prior data distribution at all**.\n\n**The method:** IWR computes importance weights as the **density ratio p_target / p_prior**, where both densities are estimated via Gaussian KDE over learned state-action embeddings. A prior data point is retrieved if this ratio exceeds a threshold eta. The bandwidth is set using a multiplicative factor of Scott's rule: h = c * |D|^(-1/(d+4)).\n\n**Why the ratio matters:** Without the prior density in the denominator, retrieval is biased toward regions where the prior dataset happens to be dense (e.g., early timesteps in demonstrations, common objects). By normalizing by p_prior, IWR upweights samples that are relevant to the target task but underrepresented in the prior -- such as later-stage demonstration steps or uncommon object interactions.\n\n---\n\n### Filtering vs. Weighting -- The Central Question\n\nThis is where IWR sits in an interesting middle ground:\n\n1. **It uses soft/smooth density estimation** (Gaussian KDE with reasonable bandwidth) rather than the hard nearest-neighbor approach of prior work, which considers all data points when estimating densities rather than just the single closest point.\n\n2. **But it applies a hard threshold for final selection**: data points where p_target/p_prior > eta are included; others are excluded. This is binary filtering, not continuous weighting.\n\n3. **It does NOT do importance-weighted training**: The authors explicitly note that \"IWR is still a biased estimate, as we do not perform importance sampling, but only retrieve based on importance weights.\" They chose hard thresholding over true importance resampling because it \"easily integrates with prior methods.\"\n\nSo IWR occupies a hybrid position: the **selection criterion** is based on continuous density ratios (a weighting idea), but the **output** is a hard-filtered subset (a filtering operation). The density ratio informs *which* demonstrations to include, but once selected, all retrieved data points are treated equally during policy training.\n\n---\n\n### Key Results\n\n- **Simulation (LIBERO):** +5.8% success rate over Behavior Retrieval, +4.4% over Flow Retrieval, +5.8% over SAILOR\n- **Real-world (Bridge dataset):** +30% average success rate over Behavior Retrieval, with the most dramatic gains on long-horizon and complex tasks\n- **Ablations:** Smoother KDEs (larger bandwidth) perform slightly better on average; the prior-density normalization is critical to the gains\n- On simple tasks where baseline retrieval already works well (>50% relevant retrievals), IWR offers minimal additional benefit\n\n---\n\n### Key Files/URLs\n\n- ArXiv: `https://arxiv.org/abs/2509.01657`\n- Project page: `https://rahulschand.github.io/iwr/` and `https://sites.google.com/stanford.edu/iwr`\n- Proceedings: `https://proceedings.mlr.press/v305/xie25a.html`\n\nSources:\n- [ArXiv Abstract](https://arxiv.org/abs/2509.01657)\n- [ArXiv HTML Full Paper](https://arxiv.org/html/2509.01657)\n- [PMLR Proceedings](https://proceedings.mlr.press/v305/xie25a.html)\n- [Project Page (Rahul Chand)](https://rahulschand.github.io/iwr/)\n- [Stanford Project Page](https://sites.google.com/stanford.edu/iwr)\n- [EmergentMind Topic Page](https://www.emergentmind.com/topics/importance-weighted-retrieval-iwr)"
      }
    ],
    "totalDurationMs": 74584,
    "totalTokens": 18449,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1103,
      "cache_read_input_tokens": 16182,
      "output_tokens": 1163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1103
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1163,
          "cache_read_input_tokens": 16182,
          "cache_creation_input_tokens": 1103,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1103,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 9
    }
  },
  "sourceToolAssistantUUID": "2b99e746-d969-4a97-a785-146027c9c6df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"When to Filter, When to Weight: A Bias-Variance Framework for Adaptive…",
  "leafUuid": "6bf6fd21-e547-4010-a938-cdc43ef31cd8",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Adaptive demo curation via estimator reliability",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96"
}
```

---

### Tool result

_source line 26 · 2026-05-13T11:43:11.104Z_

<details><summary>↩ Tool result · `toolu_011Xr5e2g8q8PfznnPkwAwYN`</summary>

```text
Now I have a comprehensive picture. Here is my report.

---

## Report: Sim-Only vs. Real-Robot Experiments for CoRL 2026 Demo Curation Paper

### (a) Is sim-only acceptable at CoRL 2026 for a primarily theoretical/framework paper?

**Technically yes, but practically risky -- especially for a demo curation paper.**

CoRL 2026's official call for papers states: *"Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots."* The CoRL 2024 reviewer instructions (which CoRL 2026 follows the same tradition) explicitly say: *"You must demonstrate on a real robot! is not a strict policy and not sufficient reason for rejection on its own."*

However, there are important caveats:

1. **Your paper is empirical, not theoretical.** The "sim-only is OK for theoretical papers" exception applies to things like convergence proofs or novel RL algorithms with formal guarantees. A demo curation paper (filtering vs. weighting) is fundamentally an empirical contribution. Reviewers will ask: "Does this actually work on messy real-world data?"

2. **Every competing paper in this space now includes real-robot results.** The competitive landscape has shifted dramatically:
   - **CUPID** (CoRL 2025): 3 simulated RoboMimic tasks + **3 real-world tasks on Franka FR3**
   - **SCIZOR** (ICRA 2026): RoboMimic + OXE + **Sirius-Fleet real-robot tasks** (32.9% gains)
   - **Demo-SCORE** (RSS 2025): Sim + **real-world experiments** (15-35% absolute success rate gains)
   - **DemInf** (RSS 2025): RoboMimic sim + **real-world ALOHA and Franka experiments**
   - **TOPReward**: Evaluated on **130+ real-world tasks across Franka, YAM, SO-100/101**

   A sim-only submission would be an outlier in this subfield, and reviewers will notice.

3. **Community expectations are rising.** The ICRA 2026 "From Data to Decisions: VLA Pipelines for Real Robots" workshop explicitly centers real-robot deployment, including a competition with physical robot evaluation. This signals that the community considers real-hardware validation essential for data pipeline work.

**Bottom line:** A sim-only submission is not auto-rejected, but you would be swimming upstream. Expect at least one reviewer to flag it as a significant weakness, and the AC will see that every comparable accepted paper had real-robot results.

### (b) What's the minimum real-robot experiment that would satisfy reviewers?

Based on what the accepted papers in this space include, the minimum viable real-robot experiment is:

1. **1-2 manipulation tasks** on a single robot platform (Franka Panda/FR3 is the most common; ALOHA is another option). Pick tasks where demonstration quality naturally varies -- e.g., pick-and-place with varying object positions, or a task where teleoperation quality differs across operators.

2. **Show the curation pipeline end-to-end:** Collect ~50-100 demonstrations (mix of good and poor quality), run your filtering/weighting method, train a policy on curated vs. uncurated data, and report success rates over 20+ evaluation rollouts.

3. **One table or figure** showing: (i) baseline (all demos), (ii) your method (filtered/weighted), (iii) at least one competing curation method (e.g., DemInf or random subsampling). Even 2-3 tasks with clear trends is sufficient -- CUPID used exactly 3 real tasks.

4. **A supplementary video** showing the robot executing the task with curated vs. uncurated policies. This is strongly encouraged by CoRL and is highly persuasive for reviewers.

The bar is NOT: dozens of tasks, multiple robot platforms, or extensive ablations on hardware. A focused, clean experiment on 1-2 tasks that validates your sim findings transfers is sufficient.

### (c) How feasible is adding real-robot experiments in ~2 weeks (by May 28)?

**Feasible but tight. Here's the realistic breakdown:**

**If you already have access to a robot platform (Franka, ALOHA, etc.):**
- Days 1-2: Set up data collection pipeline (teleoperation interface, camera calibration). If using an existing framework like SERL or robomimic's data collection tools, this is faster.
- Days 3-5: Collect demonstrations (~50-100 demos for 1-2 tasks). Budget 1-2 days per task for collection at ~2-3 min per demo.
- Days 5-7: Run your curation method on collected data (this should be fast if your sim pipeline works).
- Days 7-10: Train policies on curated vs. uncurated datasets and run evaluation rollouts (20-50 per condition).
- Days 10-13: Write up results, create video, integrate into paper.
- Day 14: Buffer for things going wrong (they always do).

**Key enablers that make this easier:**
- **VIP and R3M** both have open-source pre-trained models from Facebook Research that work out-of-the-box as frozen feature extractors on real robot images. VIP demonstrated real-world few-shot offline RL with as few as 20 trajectories. R3M enabled real manipulation with just 20 demonstrations and 10 minutes of supervision. If your curation method uses these representations, deployment is straightforward.
- **SERL** documentation notes that their simplest real-robot setup (peg insertion on Franka) converges within 30 minutes on a single GPU, showing that minimal real experiments are achievable quickly.

**If you do NOT have robot access:**
- This is the critical bottleneck. Securing robot time at a collaborator's lab on short notice is possible but uncertain. Consider: (1) reaching out to collaborators immediately, (2) using a low-cost platform like SO-100/LeRobot if available, or (3) contacting your institution's robotics lab about emergency access.

**Risk mitigation -- if real-robot experiments are truly impossible in 2 weeks:**
- Include a strong Limitations section acknowledging sim-only evaluation and commit to real-robot validation.
- Use the most realistic simulators possible (e.g., RoboMimic, ManiSkill with realistic rendering).
- Show your method works on real-world datasets like Open X-Embodiment or Sirius-Fleet even if you cannot run the robot yourself (curating existing real data and training on it is partial real-world validation).
- Submit to the workshop track or include an appendix with concrete plans for real experiments.

**My recommendation:** If you have robot access, spend the next 2 weeks doing a focused 2-task real-robot experiment. It does not need to be exhaustive -- just enough to show the sim findings transfer. Given that your deadline is May 28 and today is May 13, you have exactly 15 days, which is tight but doable for a minimal experiment. Start data collection immediately.

---

Sources:
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)
- [CoRL 2026 Instruction for Authors](https://www.corl.org/contributions/instruction-for-authors)
- [CoRL 2024 Instruction for Reviews](https://2024.corl.org/contributions/instruction-for-reviews)
- [CoRL 2023 Reviewer Guidelines](https://www.corl2023.org/reviewer-guidelines)
- [ICRA 2026 From Data to Decisions Workshop](https://icra2026vlapipeline.github.io/)
- [SCIZOR Paper (ICRA 2026)](https://arxiv.org/abs/2505.22626)
- [SCIZOR Project Page](https://ut-austin-rpl.github.io/SCIZOR/)
- [Demo-SCORE Project Page](https://anniesch.github.io/demo-score/)
- [Demo-SCORE at RSS](https://roboticsconference.org/program/papers/71/)
- [CUPID Paper (CoRL 2025)](https://arxiv.org/abs/2506.19121)
- [CUPID Project Page](https://cupid-curation.github.io/)
- [CUPID GitHub](https://github.com/agiachris/cupid)
- [DemInf Paper](https://arxiv.org/abs/2502.08623)
- [DemInf at RSS](https://roboticsconference.org/program/papers/23/)
- [TOPReward Project Page](https://topreward.github.io/webpage/)
- [TOPReward Paper](https://arxiv.org/abs/2602.19313)
- [VIP Paper (ICLR 2023)](https://arxiv.org/abs/2210.00030)
- [VIP Project Page](https://sites.google.com/view/vip-rl)
- [VIP GitHub](https://github.com/facebookresearch/vip)
- [R3M Paper](https://ar5iv.labs.arxiv.org/html/2203.12601)
- [R3M GitHub](https://github.com/facebookresearch/r3m)
- [R3M Project Page](https://sites.google.com/view/robot-r3m/)
- [SERL Real Franka Setup](https://rail-berkeley.github.io/serl/docs/real_franka.html)
- [Quality over Quantity (QoQ) Paper](https://arxiv.org/abs/2603.09056)
- [CoRL 2026 OpenReview](https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference)

agentId: ac8954d6827cada92 (use SendMessage with to: 'ac8954d6827cada92' to continue this agent)
&lt;usage>total_tokens: 28302
tool_uses: 18
duration_ms: 111209&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7c860ac-04ce-49ab-aadf-ead3115886a1",
  "isSidechain": false,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "type": "user",
  "uuid": "400a3024-57cc-46b0-9f2b-7cf35eb77d83",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm working on a paper about robot demonstration curation (filtering vs. weighting) targeting CoRL 2026 (deadline May 28, 2026). Reviewers say sim-only evaluation is weak. I need to understand:\n\n1. Use WebSearch to find: \"CoRL 2026 call for papers\", \"CoRL 2026 submission requirements real robot\" to understand reviewer expectations\n2. Search for \"ICRA 2026 From Data to Decisions VLA Pipelines Real Robots workshop\" to understand community expectations\n3. Search for recent demo curation papers that are sim-only vs. those with real-robot results. Specifically check what SCIZOR, Demo-SCORE, CUPID, TOPReward include for real-robot experiments.\n4. Search for \"VIP robot manipulation real world deployment\" and \"R3M real robot evaluation\" to understand how easy it is to deploy these estimators on real hardware.\n\nReport: (a) Is sim-only acceptable at CoRL 2026 for a primarily theoretical/framework paper? (b) What's the minimum real-robot experiment that would satisfy reviewers? (c) How feasible is adding real-robot experiments in ~2 weeks?",
    "agentId": "ac8954d6827cada92",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have a comprehensive picture. Here is my report.\n\n---\n\n## Report: Sim-Only vs. Real-Robot Experiments for CoRL 2026 Demo Curation Paper\n\n### (a) Is sim-only acceptable at CoRL 2026 for a primarily theoretical/framework paper?\n\n**Technically yes, but practically risky -- especially for a demo curation paper.**\n\nCoRL 2026's official call for papers states: *\"Authors are encouraged to report real-robot experiments or provide convincing evidence that simulation experiments are transferable to real robots.\"* The CoRL 2024 reviewer instructions (which CoRL 2026 follows the same tradition) explicitly say: *\"You must demonstrate on a real robot! is not a strict policy and not sufficient reason for rejection on its own.\"*\n\nHowever, there are important caveats:\n\n1. **Your paper is empirical, not theoretical.** The \"sim-only is OK for theoretical papers\" exception applies to things like convergence proofs or novel RL algorithms with formal guarantees. A demo curation paper (filtering vs. weighting) is fundamentally an empirical contribution. Reviewers will ask: \"Does this actually work on messy real-world data?\"\n\n2. **Every competing paper in this space now includes real-robot results.** The competitive landscape has shifted dramatically:\n   - **CUPID** (CoRL 2025): 3 simulated RoboMimic tasks + **3 real-world tasks on Franka FR3**\n   - **SCIZOR** (ICRA 2026): RoboMimic + OXE + **Sirius-Fleet real-robot tasks** (32.9% gains)\n   - **Demo-SCORE** (RSS 2025): Sim + **real-world experiments** (15-35% absolute success rate gains)\n   - **DemInf** (RSS 2025): RoboMimic sim + **real-world ALOHA and Franka experiments**\n   - **TOPReward**: Evaluated on **130+ real-world tasks across Franka, YAM, SO-100/101**\n\n   A sim-only submission would be an outlier in this subfield, and reviewers will notice.\n\n3. **Community expectations are rising.** The ICRA 2026 \"From Data to Decisions: VLA Pipelines for Real Robots\" workshop explicitly centers real-robot deployment, including a competition with physical robot evaluation. This signals that the community considers real-hardware validation essential for data pipeline work.\n\n**Bottom line:** A sim-only submission is not auto-rejected, but you would be swimming upstream. Expect at least one reviewer to flag it as a significant weakness, and the AC will see that every comparable accepted paper had real-robot results.\n\n### (b) What's the minimum real-robot experiment that would satisfy reviewers?\n\nBased on what the accepted papers in this space include, the minimum viable real-robot experiment is:\n\n1. **1-2 manipulation tasks** on a single robot platform (Franka Panda/FR3 is the most common; ALOHA is another option). Pick tasks where demonstration quality naturally varies -- e.g., pick-and-place with varying object positions, or a task where teleoperation quality differs across operators.\n\n2. **Show the curation pipeline end-to-end:** Collect ~50-100 demonstrations (mix of good and poor quality), run your filtering/weighting method, train a policy on curated vs. uncurated data, and report success rates over 20+ evaluation rollouts.\n\n3. **One table or figure** showing: (i) baseline (all demos), (ii) your method (filtered/weighted), (iii) at least one competing curation method (e.g., DemInf or random subsampling). Even 2-3 tasks with clear trends is sufficient -- CUPID used exactly 3 real tasks.\n\n4. **A supplementary video** showing the robot executing the task with curated vs. uncurated policies. This is strongly encouraged by CoRL and is highly persuasive for reviewers.\n\nThe bar is NOT: dozens of tasks, multiple robot platforms, or extensive ablations on hardware. A focused, clean experiment on 1-2 tasks that validates your sim findings transfers is sufficient.\n\n### (c) How feasible is adding real-robot experiments in ~2 weeks (by May 28)?\n\n**Feasible but tight. Here's the realistic breakdown:**\n\n**If you already have access to a robot platform (Franka, ALOHA, etc.):**\n- Days 1-2: Set up data collection pipeline (teleoperation interface, camera calibration). If using an existing framework like SERL or robomimic's data collection tools, this is faster.\n- Days 3-5: Collect demonstrations (~50-100 demos for 1-2 tasks). Budget 1-2 days per task for collection at ~2-3 min per demo.\n- Days 5-7: Run your curation method on collected data (this should be fast if your sim pipeline works).\n- Days 7-10: Train policies on curated vs. uncurated datasets and run evaluation rollouts (20-50 per condition).\n- Days 10-13: Write up results, create video, integrate into paper.\n- Day 14: Buffer for things going wrong (they always do).\n\n**Key enablers that make this easier:**\n- **VIP and R3M** both have open-source pre-trained models from Facebook Research that work out-of-the-box as frozen feature extractors on real robot images. VIP demonstrated real-world few-shot offline RL with as few as 20 trajectories. R3M enabled real manipulation with just 20 demonstrations and 10 minutes of supervision. If your curation method uses these representations, deployment is straightforward.\n- **SERL** documentation notes that their simplest real-robot setup (peg insertion on Franka) converges within 30 minutes on a single GPU, showing that minimal real experiments are achievable quickly.\n\n**If you do NOT have robot access:**\n- This is the critical bottleneck. Securing robot time at a collaborator's lab on short notice is possible but uncertain. Consider: (1) reaching out to collaborators immediately, (2) using a low-cost platform like SO-100/LeRobot if available, or (3) contacting your institution's robotics lab about emergency access.\n\n**Risk mitigation -- if real-robot experiments are truly impossible in 2 weeks:**\n- Include a strong Limitations section acknowledging sim-only evaluation and commit to real-robot validation.\n- Use the most realistic simulators possible (e.g., RoboMimic, ManiSkill with realistic rendering).\n- Show your method works on real-world datasets like Open X-Embodiment or Sirius-Fleet even if you cannot run the robot yourself (curating existing real data and training on it is partial real-world validation).\n- Submit to the workshop track or include an appendix with concrete plans for real experiments.\n\n**My recommendation:** If you have robot access, spend the next 2 weeks doing a focused 2-task real-robot experiment. It does not need to be exhaustive -- just enough to show the sim findings transfer. Given that your deadline is May 28 and today is May 13, you have exactly 15 days, which is tight but doable for a minimal experiment. Start data collection immediately.\n\n---\n\nSources:\n- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers)\n- [CoRL 2026 Instruction for Authors](https://www.corl.org/contributions/instruction-for-authors)\n- [CoRL 2024 Instruction for Reviews](https://2024.corl.org/contributions/instruction-for-reviews)\n- [CoRL 2023 Reviewer Guidelines](https://www.corl2023.org/reviewer-guidelines)\n- [ICRA 2026 From Data to Decisions Workshop](https://icra2026vlapipeline.github.io/)\n- [SCIZOR Paper (ICRA 2026)](https://arxiv.org/abs/2505.22626)\n- [SCIZOR Project Page](https://ut-austin-rpl.github.io/SCIZOR/)\n- [Demo-SCORE Project Page](https://anniesch.github.io/demo-score/)\n- [Demo-SCORE at RSS](https://roboticsconference.org/program/papers/71/)\n- [CUPID Paper (CoRL 2025)](https://arxiv.org/abs/2506.19121)\n- [CUPID Project Page](https://cupid-curation.github.io/)\n- [CUPID GitHub](https://github.com/agiachris/cupid)\n- [DemInf Paper](https://arxiv.org/abs/2502.08623)\n- [DemInf at RSS](https://roboticsconference.org/program/papers/23/)\n- [TOPReward Project Page](https://topreward.github.io/webpage/)\n- [TOPReward Paper](https://arxiv.org/abs/2602.19313)\n- [VIP Paper (ICLR 2023)](https://arxiv.org/abs/2210.00030)\n- [VIP Project Page](https://sites.google.com/view/vip-rl)\n- [VIP GitHub](https://github.com/facebookresearch/vip)\n- [R3M Paper](https://ar5iv.labs.arxiv.org/html/2203.12601)\n- [R3M GitHub](https://github.com/facebookresearch/r3m)\n- [R3M Project Page](https://sites.google.com/view/robot-r3m/)\n- [SERL Real Franka Setup](https://rail-berkeley.github.io/serl/docs/real_franka.html)\n- [Quality over Quantity (QoQ) Paper](https://arxiv.org/abs/2603.09056)\n- [CoRL 2026 OpenReview](https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2026%2FConference)"
      }
    ],
    "totalDurationMs": 111209,
    "totalTokens": 28302,
    "totalToolUseCount": 18,
    "usage": {
      "input_tokens": 745,
      "cache_creation_input_tokens": 4298,
      "cache_read_input_tokens": 20874,
      "output_tokens": 2385,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4298
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 745,
          "output_tokens": 2385,
          "cache_read_input_tokens": 20874,
          "cache_creation_input_tokens": 4298,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4298,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 18
    }
  },
  "sourceToolAssistantUUID": "b7c860ac-04ce-49ab-aadf-ead3115886a1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-13T11:46:26.798Z_

<details><summary>↩ Tool result · `toolu_01JxJHFEmc17gfHM3URPijzZ`</summary>

```text
I now have comprehensive findings across all four questions. Here is my report.

---

## Research Findings Report

### 1. An et al. (ICLR 2021) -- "Why Resampling Outperforms Reweighting"

**Key Assumptions and Conditions:**

The theoretical analysis is **restricted to SGD with a constant learning rate** (constant step size eta). The paper analyzes stability using tools from dynamical stability and stochastic asymptotics (SDE approximations to SGD).

**Theorem Statements (from the ar5iv HTML version):**

- **Lemma 1 (Resampling Stability):** "For resampling, the conditions for the SGD to be stochastically stable around theta=-1 and theta=1 are respectively (1-eta*a1)^2 + eta^2*a1*a2 <= 1, (1-eta*a2)^2 + eta^2*a1*a2 <= 1"

- **Lemma 2 (Reweighting Stability):** "For reweighting, the condition for the SGD to be stochastically stable around theta=-1 and theta=1 are respectively (1-eta*a1)^2 + eta^2*f1*f2*(a1/f1)^2 <= 1, (1-eta*a2)^2 + eta^2*f1*f2*(a2/f2)^2 <= 1"

The critical insight: "the stability conditions for resampling are independent of the sampling proportions (f1,f2), while the ones for reweighting clearly depend on (f1,f2)." When f2/f1 is small (severe imbalance), the reweighting stability condition becomes much harder to satisfy.

**Loss function assumptions:** The theory is developed on (a) piecewise quadratic losses (Section 3) and (b) piecewise linear non-smooth losses (Section 4). Lemmas 5-6 require "strictly convex functions." There is no general nonconvex theory.

**Key mechanism:** "The key reason is that the variances experienced for Vw(theta) and Vs(theta) can be drastically different." For reweighting, variance is scaled by (ai/fi)^2 terms, which blow up when sampling proportions diverge from population proportions.

**Adam optimizer:** The paper explicitly **does use Adam in experiments**: "adaptive stochastic gradient methods such as Adam...are applied in the first two experiments" (Bank Marketing classification and California Housing regression). However, the theoretical analysis is **SGD-only**. The authors acknowledge this gap: "An immediate direction for future work is to apply the analysis to more sophisticated stochastic training algorithms."

**Limitations / where result doesn't hold:**
- Theory is restricted to SGD with constant learning rate -- does not cover Adam or other adaptive methods
- Stability analysis uses simplified 1D/low-dimensional examples (quadratic, piecewise linear)
- Authors note: "it is still an open problem how the stochastic process behaves when the covariance matrix...depends on Theta in high dimensions"
- Lemma 4 requires specific conditions on sampling proportions: "Under the condition f2/f1 <= (a2/a1)*sqrt(V(-1)/V(1))"
- Batch size effects are not formally treated

**Implications for your paper:** The An et al. result is proven for **SGD with constant learning rate on convex/simple losses**. It does not formally cover Adam (which most modern IL/RL uses), decreasing learning rates, or high-dimensional nonconvex losses. Their own experiments use Adam but without theoretical backing. This is a significant gap your paper can exploit: if you use Adam (which normalizes gradient magnitudes and thus partially neutralizes the variance difference), the theoretical basis for "resampling > reweighting" is unproven.

---

### 2. Byrd & Lipton (ICML 2019) -- "What is the Effect of Importance Weighting in Deep Learning?"

**Core finding: DIMINISHING effect, not NO effect.** The paper shows: "while importance weighting impacts deep nets early in training, so long as the nets are able to separate the training data, its effect diminishes over successive epochs."

**Mechanism:** This is tied to overparameterization and data separability. On separable data, SGD-trained networks converge toward max-margin-like solutions that are "weight-agnostic" -- the final solution doesn't depend on the importance weights. The authors cite Soudry et al. (2017) and Gunasekar et al. (2018): "deep linear networks optimized by SGD learn weight-agnostic solutions" on separable data. They acknowledge: "Note that although these theoretical analyses cover only shallow linear, deep linear, and deep convolutional linear neural networks, our experiments draw intuition from the results."

**This is an empirical paper -- no novel theorems are proven.** The theoretical grounding comes from prior work on implicit bias of gradient descent.

**L2 regularization restores the effect:** "L2 regularization and batch normalization (but not dropout), restore some of the impact of importance weighting, they express the effect via (seemingly) the wrong abstraction: why should practitioners tweak the L2 regularization, and by how much, to produce the correct weighting effect?" The mechanism: "the L2 penalty prevents SGD from reaching the large norm solutions whose loss is dominated by the support vectors, thus preventing convergence to max-margin-like solutions."

**Timing matters:** "models with more extreme weighting converge more slowly in decision boundary, and convergence in classification ratio begins to occur long after perfect training accuracy is achieved." After sufficient epochs, the effect becomes indistinguishable from unweighted training.

**Practical implications:** The authors note this "calls into question the standard application of importance weighting when applied to deep networks, a finding with practical consequences on the fields of causal inference, domain adaptation, and off-policy reinforcement learning."

**Implications for your paper:** This is nuanced. Byrd & Lipton show weighting effects diminish for overparameterized networks on separable data trained to convergence. However:
- This applies most directly to classification (separability assumption). Regression tasks (like policy learning) may not be separable.
- L2 regularization restores the effect, and many IL/RL methods use weight decay.
- The effect is present early in training, which may matter for RL where training is iterative.
- This actually argues that **filtering** (binary) may be more robust than continuous weighting, since filtering changes the dataset itself rather than relying on weights that may lose effect during training.

---

### 3. Recent (2024-2026) Empirical Comparisons of Resampling vs. Reweighting in IL/Offline RL

**ODPR / OPER (2023, published NeurIPS):** The "Decoupled Prioritized Resampling for Offline RL" paper by Yang et al. is the most relevant direct comparison. Key findings:
- They provide reweighting results in Appendix C-E, with the main paper using resampling
- On Pen tasks with IQL, "resampling performed well while reweighting was unable to achieve meaningful scores, hypothesized to be due to exceedingly large weights that may alter the learning rate"
- They note "clipping gives a biased estimation to the weights and hinders the performance of ODPR-A," showing that the standard fix for large weights (clipping) introduces its own problems
- Their key innovation is **decoupled** sampling: uniform sampling for policy evaluation, prioritized sampling for policy improvement, because prioritized sampling destabilizes value estimation

**RINSE (2025, arxiv 2604.23000):** "Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning" tests **both filtering and weighting** with quality scores. They demonstrate that quality-based curation "can reduce the conditional action variance of the retained data distribution." SAL filtering achieves 16% higher success using one-sixth of the data; TED filtering achieves 20% improvement with half the data. The framework works in "filtering, retrieval, and reweighting settings, especially in noisy or heterogeneous data regimes."

**A3RL (2025):** Proposes advantage-aligned prioritized sampling for offline-to-online RL, improving over RLPD's symmetric sampling. They "distribute [weights] non-uniformly" rather than using uniform sampling, showing the choice of sampling strategy matters.

**Bottom line:** There is limited head-to-head comparison, but the available evidence (especially ODPR) supports that resampling tends to be more stable than reweighting in offline RL, primarily because large importance weights destabilize training. However, this doesn't necessarily mean binary filtering beats continuous scoring -- ODPR uses continuous priority scores for resampling probabilities.

---

### 4. IQL Expectile Regression and Q-Value Variance

**IQL does NOT explicitly claim variance reduction as a property of expectile regression.** The paper (Kostrikov et al., ICLR 2022) frames the benefit as avoiding **extrapolation error** on out-of-distribution actions, not as variance reduction per se.

**The exact loss function:** L_V(psi) = E_{(s,a)~D} [L^2_tau(Q_hat(s,a) - V_psi(s))], where L^2_tau(u) = |tau - 1(u<0)| * u^2.

**The "lucky sample" framing (variance-adjacent):** Rather than discussing variance explicitly, the authors address what they call the "lucky sample" issue. They introduce a separate value function V specifically to avoid incorporating stochasticity from environment dynamics, noting that "a large target value might not necessarily reflect the existence of a single action that achieves that value, but rather a 'lucky' sample." This is conceptually about reducing variance from stochastic dynamics, but it's framed as an architectural choice (separate V network) rather than a property of expectile regression itself.

**Statistical properties of expectile regression (from statistics literature):** Expectile estimators have computational advantages over quantile estimators: "the asymptotic covariance matrix can be estimated without the need of estimating the conditional density function." Expectile regression uses squared loss (vs. absolute loss for quantiles), which yields smoother optimization and potentially lower estimation variance for the estimator itself. However, this is a property of the estimator, not of the quantity being estimated.

**How tau affects things:** "For tau > 0.5, this asymmetric loss function downweights the contributions of x values smaller than m_tau while giving more weights to larger values." As tau approaches 1, it approximates the maximum. Higher tau increases **bias** (toward optimistic values) while potentially reducing sensitivity to low-quality actions.

**Implications for your paper:** You should be careful about claiming IQL's expectile regression "reduces Q-value variance" -- the IQL paper itself does not make this claim. What it does is:
1. Avoid querying OOD actions (avoiding extrapolation error, which is a bias problem more than a variance problem)
2. Use a separate V network to handle stochastic dynamics (the "lucky sample" issue, which is variance-related)
3. Use expectile regression to approximate the max without explicitly computing it (avoiding the argmax-over-Q operator that can be unstable)

The variance story is more nuanced than "expectile regression reduces variance." It would be more accurate to say IQL's in-sample learning avoids the high-variance extrapolation errors that plague standard offline RL, and the expectile provides a smoother approximation to the max operator.

---

**Key Sources:**

- [An et al. - Why Resampling Outperforms Reweighting (Stanford PDF)](https://web.stanford.edu/~lexing/resw.pdf)
- [An et al. - OpenReview](https://openreview.net/forum?id=iQQK02mxVIT)
- [An et al. - arXiv](https://arxiv.org/abs/2009.13447)
- [An & Ying - Combining Resampling and Reweighting](https://arxiv.org/abs/2105.14694)
- [Byrd & Lipton - ICML 2019 Proceedings](https://proceedings.mlr.press/v97/byrd19a.html)
- [Byrd & Lipton - arXiv](https://arxiv.org/abs/1812.03372)
- [Yang et al. - Decoupled Prioritized Resampling (ODPR)](https://arxiv.org/abs/2306.05412)
- [RINSE - Smoothness-Driven Metrics for Demo Quality](https://arxiv.org/abs/2604.23000)
- [Kostrikov et al. - IQL (ICLR 2022)](https://arxiv.org/abs/2110.06169)
- [IQL OpenReview](https://openreview.net/forum?id=68n2s9ZJWF8)
- [IDQL Technical Report](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2023/EECS-2023-62.pdf)
- [Expectile vs Quantile Regression Properties](https://epub.ub.uni-muenchen.de/31542/1/1471082x14561155.pdf)
- [DP-IL - Imitation Learning from Purified Demonstrations](https://arxiv.org/html/2310.07143v2)

agentId: ab33db2d612882ce2 (use SendMessage with to: 'ab33db2d612882ce2' to continue this agent)
&lt;usage>total_tokens: 44916
tool_uses: 46
duration_ms: 298050&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ab198120-f0a0-48e7-8915-5866b3e8c3e4",
  "isSidechain": false,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "type": "user",
  "uuid": "13e58fb2-7a3c-44e3-82c3-c4a756a63ef6",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm writing a paper about when to use binary filtering vs. continuous weighting for robot demo quality scores. A key claim is that An et al. (ICLR 2021, \"Why Resampling Outperforms Reweighting\") proves resampling > reweighting, but we claim low-variance estimators can overcome this.\n\n1. Use WebSearch to find and then WebFetch to read An et al. 2021's key assumptions. Specifically: what are the exact conditions under which their theorem holds? (bounded weights, SGD with constant LR, etc.) Do they discuss Adam optimizer? Do they discuss cases where their result doesn't hold?\n\n2. Search for \"Byrd Lipton importance weighting deep learning ICML 2019\" and check: do they show that importance weighting has NO effect in overparameterized networks, or diminishing effect? What are the implications for the filter-vs-weight question?\n\n3. Search for any papers from 2024-2026 that empirically test resampling vs. reweighting in imitation learning or offline RL specifically. Any evidence that the choice matters or doesn't matter?\n\n4. Search for \"IQL expectile regression Q-value variance\" to understand whether IQL's expectile regression already reduces Q-value variance compared to standard TD, which could undermine the \"high variance\" characterization.\n\nReport findings concisely with exact quotes where relevant.",
    "agentId": "ab33db2d612882ce2",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive findings across all four questions. Here is my report.\n\n---\n\n## Research Findings Report\n\n### 1. An et al. (ICLR 2021) -- \"Why Resampling Outperforms Reweighting\"\n\n**Key Assumptions and Conditions:**\n\nThe theoretical analysis is **restricted to SGD with a constant learning rate** (constant step size eta). The paper analyzes stability using tools from dynamical stability and stochastic asymptotics (SDE approximations to SGD).\n\n**Theorem Statements (from the ar5iv HTML version):**\n\n- **Lemma 1 (Resampling Stability):** \"For resampling, the conditions for the SGD to be stochastically stable around theta=-1 and theta=1 are respectively (1-eta*a1)^2 + eta^2*a1*a2 <= 1, (1-eta*a2)^2 + eta^2*a1*a2 <= 1\"\n\n- **Lemma 2 (Reweighting Stability):** \"For reweighting, the condition for the SGD to be stochastically stable around theta=-1 and theta=1 are respectively (1-eta*a1)^2 + eta^2*f1*f2*(a1/f1)^2 <= 1, (1-eta*a2)^2 + eta^2*f1*f2*(a2/f2)^2 <= 1\"\n\nThe critical insight: \"the stability conditions for resampling are independent of the sampling proportions (f1,f2), while the ones for reweighting clearly depend on (f1,f2).\" When f2/f1 is small (severe imbalance), the reweighting stability condition becomes much harder to satisfy.\n\n**Loss function assumptions:** The theory is developed on (a) piecewise quadratic losses (Section 3) and (b) piecewise linear non-smooth losses (Section 4). Lemmas 5-6 require \"strictly convex functions.\" There is no general nonconvex theory.\n\n**Key mechanism:** \"The key reason is that the variances experienced for Vw(theta) and Vs(theta) can be drastically different.\" For reweighting, variance is scaled by (ai/fi)^2 terms, which blow up when sampling proportions diverge from population proportions.\n\n**Adam optimizer:** The paper explicitly **does use Adam in experiments**: \"adaptive stochastic gradient methods such as Adam...are applied in the first two experiments\" (Bank Marketing classification and California Housing regression). However, the theoretical analysis is **SGD-only**. The authors acknowledge this gap: \"An immediate direction for future work is to apply the analysis to more sophisticated stochastic training algorithms.\"\n\n**Limitations / where result doesn't hold:**\n- Theory is restricted to SGD with constant learning rate -- does not cover Adam or other adaptive methods\n- Stability analysis uses simplified 1D/low-dimensional examples (quadratic, piecewise linear)\n- Authors note: \"it is still an open problem how the stochastic process behaves when the covariance matrix...depends on Theta in high dimensions\"\n- Lemma 4 requires specific conditions on sampling proportions: \"Under the condition f2/f1 <= (a2/a1)*sqrt(V(-1)/V(1))\"\n- Batch size effects are not formally treated\n\n**Implications for your paper:** The An et al. result is proven for **SGD with constant learning rate on convex/simple losses**. It does not formally cover Adam (which most modern IL/RL uses), decreasing learning rates, or high-dimensional nonconvex losses. Their own experiments use Adam but without theoretical backing. This is a significant gap your paper can exploit: if you use Adam (which normalizes gradient magnitudes and thus partially neutralizes the variance difference), the theoretical basis for \"resampling > reweighting\" is unproven.\n\n---\n\n### 2. Byrd & Lipton (ICML 2019) -- \"What is the Effect of Importance Weighting in Deep Learning?\"\n\n**Core finding: DIMINISHING effect, not NO effect.** The paper shows: \"while importance weighting impacts deep nets early in training, so long as the nets are able to separate the training data, its effect diminishes over successive epochs.\"\n\n**Mechanism:** This is tied to overparameterization and data separability. On separable data, SGD-trained networks converge toward max-margin-like solutions that are \"weight-agnostic\" -- the final solution doesn't depend on the importance weights. The authors cite Soudry et al. (2017) and Gunasekar et al. (2018): \"deep linear networks optimized by SGD learn weight-agnostic solutions\" on separable data. They acknowledge: \"Note that although these theoretical analyses cover only shallow linear, deep linear, and deep convolutional linear neural networks, our experiments draw intuition from the results.\"\n\n**This is an empirical paper -- no novel theorems are proven.** The theoretical grounding comes from prior work on implicit bias of gradient descent.\n\n**L2 regularization restores the effect:** \"L2 regularization and batch normalization (but not dropout), restore some of the impact of importance weighting, they express the effect via (seemingly) the wrong abstraction: why should practitioners tweak the L2 regularization, and by how much, to produce the correct weighting effect?\" The mechanism: \"the L2 penalty prevents SGD from reaching the large norm solutions whose loss is dominated by the support vectors, thus preventing convergence to max-margin-like solutions.\"\n\n**Timing matters:** \"models with more extreme weighting converge more slowly in decision boundary, and convergence in classification ratio begins to occur long after perfect training accuracy is achieved.\" After sufficient epochs, the effect becomes indistinguishable from unweighted training.\n\n**Practical implications:** The authors note this \"calls into question the standard application of importance weighting when applied to deep networks, a finding with practical consequences on the fields of causal inference, domain adaptation, and off-policy reinforcement learning.\"\n\n**Implications for your paper:** This is nuanced. Byrd & Lipton show weighting effects diminish for overparameterized networks on separable data trained to convergence. However:\n- This applies most directly to classification (separability assumption). Regression tasks (like policy learning) may not be separable.\n- L2 regularization restores the effect, and many IL/RL methods use weight decay.\n- The effect is present early in training, which may matter for RL where training is iterative.\n- This actually argues that **filtering** (binary) may be more robust than continuous weighting, since filtering changes the dataset itself rather than relying on weights that may lose effect during training.\n\n---\n\n### 3. Recent (2024-2026) Empirical Comparisons of Resampling vs. Reweighting in IL/Offline RL\n\n**ODPR / OPER (2023, published NeurIPS):** The \"Decoupled Prioritized Resampling for Offline RL\" paper by Yang et al. is the most relevant direct comparison. Key findings:\n- They provide reweighting results in Appendix C-E, with the main paper using resampling\n- On Pen tasks with IQL, \"resampling performed well while reweighting was unable to achieve meaningful scores, hypothesized to be due to exceedingly large weights that may alter the learning rate\"\n- They note \"clipping gives a biased estimation to the weights and hinders the performance of ODPR-A,\" showing that the standard fix for large weights (clipping) introduces its own problems\n- Their key innovation is **decoupled** sampling: uniform sampling for policy evaluation, prioritized sampling for policy improvement, because prioritized sampling destabilizes value estimation\n\n**RINSE (2025, arxiv 2604.23000):** \"Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning\" tests **both filtering and weighting** with quality scores. They demonstrate that quality-based curation \"can reduce the conditional action variance of the retained data distribution.\" SAL filtering achieves 16% higher success using one-sixth of the data; TED filtering achieves 20% improvement with half the data. The framework works in \"filtering, retrieval, and reweighting settings, especially in noisy or heterogeneous data regimes.\"\n\n**A3RL (2025):** Proposes advantage-aligned prioritized sampling for offline-to-online RL, improving over RLPD's symmetric sampling. They \"distribute [weights] non-uniformly\" rather than using uniform sampling, showing the choice of sampling strategy matters.\n\n**Bottom line:** There is limited head-to-head comparison, but the available evidence (especially ODPR) supports that resampling tends to be more stable than reweighting in offline RL, primarily because large importance weights destabilize training. However, this doesn't necessarily mean binary filtering beats continuous scoring -- ODPR uses continuous priority scores for resampling probabilities.\n\n---\n\n### 4. IQL Expectile Regression and Q-Value Variance\n\n**IQL does NOT explicitly claim variance reduction as a property of expectile regression.** The paper (Kostrikov et al., ICLR 2022) frames the benefit as avoiding **extrapolation error** on out-of-distribution actions, not as variance reduction per se.\n\n**The exact loss function:** L_V(psi) = E_{(s,a)~D} [L^2_tau(Q_hat(s,a) - V_psi(s))], where L^2_tau(u) = |tau - 1(u<0)| * u^2.\n\n**The \"lucky sample\" framing (variance-adjacent):** Rather than discussing variance explicitly, the authors address what they call the \"lucky sample\" issue. They introduce a separate value function V specifically to avoid incorporating stochasticity from environment dynamics, noting that \"a large target value might not necessarily reflect the existence of a single action that achieves that value, but rather a 'lucky' sample.\" This is conceptually about reducing variance from stochastic dynamics, but it's framed as an architectural choice (separate V network) rather than a property of expectile regression itself.\n\n**Statistical properties of expectile regression (from statistics literature):** Expectile estimators have computational advantages over quantile estimators: \"the asymptotic covariance matrix can be estimated without the need of estimating the conditional density function.\" Expectile regression uses squared loss (vs. absolute loss for quantiles), which yields smoother optimization and potentially lower estimation variance for the estimator itself. However, this is a property of the estimator, not of the quantity being estimated.\n\n**How tau affects things:** \"For tau > 0.5, this asymmetric loss function downweights the contributions of x values smaller than m_tau while giving more weights to larger values.\" As tau approaches 1, it approximates the maximum. Higher tau increases **bias** (toward optimistic values) while potentially reducing sensitivity to low-quality actions.\n\n**Implications for your paper:** You should be careful about claiming IQL's expectile regression \"reduces Q-value variance\" -- the IQL paper itself does not make this claim. What it does is:\n1. Avoid querying OOD actions (avoiding extrapolation error, which is a bias problem more than a variance problem)\n2. Use a separate V network to handle stochastic dynamics (the \"lucky sample\" issue, which is variance-related)\n3. Use expectile regression to approximate the max without explicitly computing it (avoiding the argmax-over-Q operator that can be unstable)\n\nThe variance story is more nuanced than \"expectile regression reduces variance.\" It would be more accurate to say IQL's in-sample learning avoids the high-variance extrapolation errors that plague standard offline RL, and the expectile provides a smoother approximation to the max operator.\n\n---\n\n**Key Sources:**\n\n- [An et al. - Why Resampling Outperforms Reweighting (Stanford PDF)](https://web.stanford.edu/~lexing/resw.pdf)\n- [An et al. - OpenReview](https://openreview.net/forum?id=iQQK02mxVIT)\n- [An et al. - arXiv](https://arxiv.org/abs/2009.13447)\n- [An & Ying - Combining Resampling and Reweighting](https://arxiv.org/abs/2105.14694)\n- [Byrd & Lipton - ICML 2019 Proceedings](https://proceedings.mlr.press/v97/byrd19a.html)\n- [Byrd & Lipton - arXiv](https://arxiv.org/abs/1812.03372)\n- [Yang et al. - Decoupled Prioritized Resampling (ODPR)](https://arxiv.org/abs/2306.05412)\n- [RINSE - Smoothness-Driven Metrics for Demo Quality](https://arxiv.org/abs/2604.23000)\n- [Kostrikov et al. - IQL (ICLR 2022)](https://arxiv.org/abs/2110.06169)\n- [IQL OpenReview](https://openreview.net/forum?id=68n2s9ZJWF8)\n- [IDQL Technical Report](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2023/EECS-2023-62.pdf)\n- [Expectile vs Quantile Regression Properties](https://epub.ub.uni-muenchen.de/31542/1/1471082x14561155.pdf)\n- [DP-IL - Imitation Learning from Purified Demonstrations](https://arxiv.org/html/2310.07143v2)"
      }
    ],
    "totalDurationMs": 298050,
    "totalTokens": 44916,
    "totalToolUseCount": 46,
    "usage": {
      "input_tokens": 225,
      "cache_creation_input_tokens": 1118,
      "cache_read_input_tokens": 40363,
      "output_tokens": 3210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1118
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 225,
          "output_tokens": 3210,
          "cache_read_input_tokens": 40363,
          "cache_creation_input_tokens": 1118,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1118,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 46
    }
  },
  "sourceToolAssistantUUID": "ab198120-f0a0-48e7-8915-5866b3e8c3e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"When to Filter, When to Weight: A Bias-Variance Framework for Adaptive…",
  "leafUuid": "13e58fb2-7a3c-44e3-82c3-c4a756a63ef6",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Adaptive demo curation via estimator reliability",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96"
}
```

---

### Assistant

_source line 30 · 2026-05-13T11:47:03.703Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent. Now I have comprehensive research findings on all the issues. Let me synthesize and produce the revised idea.

**Summary of research findings:**

1. **SARM/RA-BC κ**: Confirmed κ=0.01 is FIXED. Only w̃_i uses adaptive running statistics via Welford's. Must fix this.

2. **Robometer (RSS 2026)**: Dense general-purpose reward model trained on 1M+ trajectories (RBM-1M), 21 embodiments. Uses dual training (progress + preference). Explicitly evaluated for data retrieval + IL. 

3. **IWR (CoRL 2025)**: Importance-weighted retrieval using density ratios (p_target/p_prior via KDE). Uses continuous density ratios for selection but applies hard threshold for final filtering. Oral at CoRL 2025. Relevant as prior work on importance-weighted data selection.

4. **Green-VLA (Feb 2026)**: Staged VLA with DataQA pipeline using heuristic metrics (tremble score, sharpness, visual diversity, state-space diversity). Heuristic-based filtering motivates principled alternatives.

5. **RINSE**: Looking at the remaining approaches to understand how they handle quality estimation and data selection.

6. **Real-robot experiments**: CoRL 2026 expects real-robot validation, and while it's not automatic grounds for rejection, competing papers all have it. I should plan for at least 1-2 tasks on a single platform with a complete end-to-end demonstration, which is achievable in roughly 2 weeks if robot access is available.

7. **An et al.**: Their theoretical result only applies to SGD with constant learning rates on convex or simple losses—it doesn't extend to Adam. Their experiments use Adam without theoretical justification, which is a meaningful gap I can address.

8. **Byrd & Lipton**: They show diminishing rather than complete absence of effects, and their analysis relies on data separability assumptions. L2 regularization can restore the effect, and their focus is more on classification than regression tasks.

9. **IQL expectile regression**: This approach doesn't directly target Q-value variance reduction. It addresses extrapolation error through a bias-correction mechanism rather than variance control.

Now I'm thinking through the revision strategy. The reviewer acknowledges the core idea is genuinely novel and addresses a real gap, so the issues are mostly about quality control and scientific rigor rather than fundamental flaws. Given the submission history, a major revision makes sense—I'd keep the core concept but substantially strengthen the scientific foundation, add minimum effect size specifications, prepare contingency plans for null results, and tackle the real-robot evaluation gap. The key fixes are straightforward: correct the SARM κ value, integrate Robometer for benchmarking, and address the remaining robustness concerns.

I need to be precise about a few technical details as I revise: the SARM formulation uses κ=0.01 as a fixed parameter with adaptive Welford statistics for the weights, IQL's advantage isn't about variance reduction per se but about sidestepping extrapolation error, and I should propose a minimal real-robot experiment rather than dismissing the sim-only limitation. I'm also setting explicit minimum effect sizes for the τ̄ metric and framing null results as a clean pivot within the paper itself.

Looking at the stagnation across three review rounds at 3.5, the core issues are quality control and scientific robustness—both addressable. A major revision that fundamentally strengthens the experimental rigor and addresses the tension in the An et al. experiment seems necessary rather than incremental fixes.

Writing the revised JSON...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13e58fb2-7a3c-44e3-82c3-c4a756a63ef6",
  "isSidechain": false,
  "requestId": "req_011CazWhY8EUNjjxmr1j8yCV",
  "type": "assistant",
  "uuid": "3b4495fa-4894-41a0-abf6-6b454c250e38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rgbr6udj9D36797vCGcRDC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14204,
      "cache_read_input_tokens": 26881,
      "output_tokens": 10903,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10903,
          "cache_read_input_tokens": 26881,
          "cache_creation_input_tokens": 14204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14204
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 31 · 2026-05-13T11:47:08.390Z_

All research is back. Let me synthesize the findings before writing the revision.

**Key findings:**
- **SARM κ**: Confirmed fixed at 0.01. Only w̃_i uses adaptive Welford statistics.
- **Robometer (RSS 2026)**: Dense reward model on 1M+ trajectories, 21 embodiments, explicitly evaluated for demo retrieval+IL.
- **IWR (CoRL 2025)**: Density-ratio retrieval (p_target/p_prior via KDE) with hard threshold — hybrid of continuous scoring + binary selection.
- **Green-VLA**: DataQA pipeline with heuristic metrics (tremble, sharpness, diversity).
- **RINSE arXiv (April 2026)**: No cross-estimator analysis, no adaptive strategy selection, no rank stability — our novelty is safe.
- **An et al.**: Theorem is SGD-only with constant LR on convex losses. Does NOT cover Adam. Significant gap we can exploit.
- **IQL**: Expectile regression avoids extrapolation error (bias), not explicitly variance reduction. Need more careful characterization.
- **Real-robot**: All competing papers have real results. CoRL doesn't auto-reject sim-only but reviewers will flag it.

Now writing the complete revision — this is a **major revision** that keeps the core idea but substantially strengthens scientific robustness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b4495fa-4894-41a0-abf6-6b454c250e38",
  "isSidechain": false,
  "requestId": "req_011CazWhY8EUNjjxmr1j8yCV",
  "type": "assistant",
  "uuid": "b0b4192b-a0d4-400e-a8c9-9c099b493843",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rgbr6udj9D36797vCGcRDC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14204,
      "cache_read_input_tokens": 26881,
      "output_tokens": 10903,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10903,
          "cache_read_input_tokens": 26881,
          "cache_creation_input_tokens": 14204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14204
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-13T11:50:56.712Z_

<details open><summary>🔧 Tool call — Write · `toolu_01S419qa1a4teamFraSqP1vk`</summary>

```json
{
  "file_path": "/tmp/revised_idea_round7.json",
  "content": "{\n  \"change_type\": \"major\",\n  \"title\": \"When to Filter, When to Weight: A Bias-Variance Framework for Adaptive Demo Curation\",\n  \"core_problem\": \"Given a quality scoring function for robot demonstrations, should training signals be binarized (keep/discard) or used as continuous weights? The demo curation field has produced 15+ methods in 2024–2026, each making an ad hoc choice: SCIZOR and Demo-SCORE use binary filtering, TOPReward and VACO use continuous weighting, IWR uses continuous density ratios but applies a hard selection threshold, Green-VLA's DataQA uses heuristic-based binary filtering, and SARM/RA-BC (ICLR 2026) uses a hybrid with a fixed threshold κ=0.01 and adaptive soft weights w̃_i but a fixed functional form. While the general ML literature offers relevant theory — An et al. (ICLR 2021) prove resampling outperforms reweighting under SGD dynamics with constant learning rate on convex losses, Byrd & Lipton (ICML 2019) show diminishing weighting effects in overparameterized networks on separable data — these results address the optimizer level (SGD) under restrictive assumptions (constant LR, convexity) that do not hold for modern IL training (Adam, nonconvex policy networks). They also do not address the estimator level: whether the quality scores themselves are precise enough to justify continuous use. The choice between filtering and weighting remains ad hoc and disconnected from the properties of the specific quality estimator being used.\",\n  \"opportunity\": \"The proliferation of diverse quality estimators — Q-function advantages (IQL), temporal contrastive encoders (VIP, R3M), smoothness metrics (RINSE SAL/TED), VLM reward models (TOPReward), dense general-purpose reward models (Robometer), influence functions (CUPID, QoQ), and density-ratio methods (IWR) — makes this question increasingly urgent. These estimators differ fundamentally in their noise properties: IQL Q-values arise from in-sample bootstrapped TD learning that, despite expectile regression reducing extrapolation error, still accumulates estimation errors across Bellman backups and suffers from advantage concentration near zero; VIP/R3M scores come from frozen pretrained encoders with stable contrastive/supervised objectives on large video datasets (Ego4D); RINSE smoothness metrics are deterministic functions of trajectory geometry; Robometer provides dense progress scores from preference-trained reward models on 1M+ trajectories. Our key insight is that the reliability of ordinal information in quality scores — measurable as rank-order stability under bootstrap resampling — is the primary factor governing whether binary filtering or continuous weighting is optimal. This connects to a classical intuition: noisy estimates are better thresholded (only the sign/rank-class matters), while precise estimates should be used continuously (preserving ordinal information). Unlike prior work that provides better scores (SCIZOR, RINSE, QoQ, Robometer) or proposes a specific weighting scheme (SARM/RA-BC, CWBC), we address the orthogonal question of what to DO with any given set of scores. The opportunity is twofold: (a) a theoretical decomposition of weighted BC suboptimality into strategy-specific terms that reveals the estimator-property dependence, and (b) a practical adaptive algorithm that measures score reliability and automatically selects the appropriate strategy.\",\n  \"landscape\": \"Demo curation for robot learning is an extremely active area with 15+ papers at top venues in 2024–2026.\\n\\n**Binary filtering methods**: SCIZOR (ICRA 2026) uses a self-supervised temporal distance classifier for binary keep/discard, achieving 15.4% average improvement (5.4% RoboMimic, 8.1% OXEMagic, 32.9% Sirius-Fleet), with real-robot results on Franka and YAM. Demo-SCORE (RSS 2025) trains a success/failure classifier from online rollouts, achieving 15–35% higher success rate with real-world Franka experiments. Green-VLA (arXiv, Jan 2026) includes a DataQA pipeline using heuristic metrics (tremble score, sharpness, visual/state-space diversity via DINOv3 features) for binary filtering of 3,000+ hours of teleoperation data — demonstrating that heuristic-based filtering is being deployed at scale, motivating principled alternatives.\\n\\n**Continuous/weighted methods**: TOPReward (Feb 2026) extracts task progress from VLM token logits for advantage-weighted BC, evaluated on 130+ real-world tasks across Franka, YAM, SO-100/101. VACO (ICLR 2025) uses a meta-scoring network with value alignment for weighted BC via bi-level optimization.\\n\\n**Hybrid and density-ratio methods**: SARM/RA-BC (ICLR 2026) introduces a hybrid weight formula w_i = 1{r̂_i > κ} + 1{0 ≤ r̂_i ≤ κ} · w̃_i where w̃_i = clip((r̂_i − (μ−2σ))/(4σ+ε), 0, 1), with κ=0.01 as a fixed hyperparameter (corresponding to the top 5% of demonstrations at ~90s task duration) and w̃_i computed adaptively via Welford's estimator for running μ and σ of progress deltas. This is the closest work to ours: it adapts soft-weight parameters within a FIXED functional form (always hybrid with fixed threshold + adaptive soft weights), whereas we select the functional form itself (binary vs. continuous) based on measured estimator properties. IWR (CoRL 2025, Oral) computes importance weights as the density ratio p_target/p_prior via Gaussian KDE for few-shot IL data retrieval — using continuous scores for selection but applying a hard threshold for final inclusion, an interesting hybrid that does not address which strategy is optimal given estimator noise properties.\\n\\n**General-purpose reward models**: Robometer (RSS 2026) is a dense, general-purpose robotic reward model trained on RBM-1M (1M+ trajectories, 21 embodiments) via dual progress + preference objectives. It provides frame-level quality scores and is explicitly evaluated for data retrieval + IL, making it directly relevant as a quality estimator class. Its reliability properties (trained on massive diverse data with preference regularization) are an interesting test case for our framework — prediction: preference-trained reward models should have moderate-to-high rank stability.\\n\\n**Quality-quantity analysis**: RINSE (ICML 2025 Workshop, DataWorld; extended arXiv version 2604.23000, April 2026) derives E(k) ≈ σ̄²(k) + C·d/(kT), decomposing error into a noise floor (reduced by filtering) and a statistical estimation term (increased by reducing data), and uses smoothness-based metrics for both binary filtering and continuous exponential weighting w(τ)=exp(−λq(τ)). The April 2026 arXiv version (v1, no stated venue) does NOT include cross-estimator analysis, adaptive strategy selection, or rank stability analysis — it remains focused on smoothness metrics (SAL, TED) with comparisons limited to random baselines and Re-Mix correlation. Our framework subsumes RINSE's decomposition as a special case (smoothness estimators, single-class) while extending to the multi-estimator adaptive setting with a principled selection criterion.\\n\\n**Prior work on filtering vs. weighting**: AFBC (Grigsby & Qi, arXiv 2021) tested binary AND exponential AWR weighting for BC with Q-function advantages, finding binary more robust. They attributed this to temperature sensitivity ('a change in β is enough to take us from near-failure to state-of-the-art performance') and advantage concentration near zero. ODPR (Yang et al., NeurIPS 2023) found resampling outperformed reweighting for offline RL prioritization, noting 'exceedingly large weights that may alter the learning rate' destabilize reweighting; they introduced decoupled sampling (uniform for value estimation, prioritized for policy improvement). Our framework provides a unifying explanation: both findings are consistent with high-variance estimators (bootstrapped Q-values) favoring binary/resampling strategies.\\n\\n**General ML theory**: An et al. (ICLR 2021) prove resampling outperforms reweighting via dynamical stability analysis of SGD — a strong prior FAVORING filtering. Critically, their theorem requires constant learning rate SGD on convex/piecewise-quadratic losses. They acknowledge this does not cover Adam, and their experiments using Adam lack theoretical backing. Modern IL training (Adam optimizer, nonconvex policy networks, weight decay) violates these assumptions, creating a gap between the theorem and practice that our empirical investigation directly addresses. Byrd & Lipton (ICML 2019) show importance weighting has diminishing effects in overparameterized networks on separable data — but this relies on convergence to max-margin solutions on separable data, and IL policy regression may not be separable; moreover, L2 regularization (common in IL) restores the weighting effect. 'Why Less is More (Sometimes)' (ICLR 2026) derives phase transitions for data pruning quantity but does not address the filter-vs-weight modality.\\n\\n**Policy-aware methods**: DataMIL (2025) uses datamodels for end-to-end data selection on OXE. CUPID (CoRL 2025) uses influence functions with real-robot experiments on Franka FR3. QoQ (ICRA 2026) uses influence functions for per-sample curation. DemInf (RSS 2025) uses mutual information estimators with real ALOHA and Franka experiments.\\n\\n**Critical gap**: Despite this extensive literature, no existing work (1) derives a suboptimality decomposition for weighted BC that separately characterizes the regimes where binary filtering vs. continuous weighting is tighter, (2) empirically demonstrates that estimator-level score reliability (not just score quality) predicts the optimal strategy, or (3) provides an adaptive algorithm that selects between strategies based on measured estimator properties. SARM/RA-BC fixes both its functional form (always hybrid) and its threshold (κ=0.01), adapting only the soft-weight statistics; our contribution is selecting the functional form itself based on measured estimator reliability.\",\n  \"approach\": \"We propose Variance-Guided Demo Curation (VGDC), a framework with two co-primary contributions — a theoretical decomposition and an empirical characterization — synthesized into a practical adaptive algorithm.\\n\\n**Co-Primary Contribution A: Bias-Variance Decomposition for Weighted BC**. We derive a novel decomposition of weighted BC suboptimality that reveals why different quality estimators favor different strategies. Consider a dataset {τ_i}_{i=1}^N of demonstrations with true quality f*(τ_i) and estimated quality f(τ_i) = f*(τ_i) + ε_i. For binary filtering at threshold c, the suboptimality decomposes as:\\n\\nR_filter ≤ P(sign(f(τ)−c) ≠ sign(f*(τ)−c)) · Δ_q + d/(k·m)\\n\\nwhere the first term is the misclassification rate at the decision boundary (misclassifying good demos as bad or vice versa) scaled by the quality impact Δ_q, and the second term is the estimation error from the reduced dataset of size k. For continuous weighting with w_i ∝ exp(f(τ_i)/T), the suboptimality decomposes as:\\n\\nR_weight ≤ C · σ_f²/T + α · T + d/N_eff(T)\\n\\nwhere σ_f² = E[ε²] is the estimator MSE amplified through weights (noise amplification term), α·T captures the bias from temperature smoothing (higher T → more uniform → more bias from including low-quality demos), and N_eff(T) is the effective sample size under the weight distribution. The key structural difference: binary filtering suboptimality depends on noise at the DECISION BOUNDARY (only misclassifications matter — a local property), while continuous weighting suboptimality depends on GLOBAL noise properties (all scores contribute to weight errors). This explains why high-variance estimators favor filtering (most noise is away from the boundary and doesn't affect the binary decision) while low-variance estimators favor weighting (precise ordinal information is preserved). The optimal temperature T* that minimizes R_weight satisfies T* ∝ σ_f (noisier estimators require higher temperature, which reduces noise amplification but increases bias — eventually, binary filtering dominates). We provide a proof sketch in the main paper and full proofs in the appendix.\\n\\nThis decomposition is distinct from and complementary to: An et al.'s SGD dynamics analysis (optimizer-level under constant-LR SGD; our analysis is estimator-level and holds regardless of optimizer), RINSE's E(k) formula (single-estimator special case without strategy comparison), CWBC's trajectory weighting (proposes a scheme but doesn't derive when filtering wins), ODPR's decoupled sampling (addresses prioritized sampling but not the binary-vs-continuous modality), and Density-Ratio Weighted BC (assumes known density ratios, not noisy quality scores). We explicitly show that RINSE's E(k) ≈ σ̄²(k) + C·d/(kT) is recovered as a special case of our R_filter bound for deterministic smoothness estimators (σ_f = 0, no misclassification noise, only data quantity tradeoff).\\n\\n**Co-Primary Contribution B: Empirical Characterization Across 3 Estimator Classes**. We conduct the first systematic measurement of quality score reliability across three classes that span the variance spectrum: (1) IQL Q-function advantages — high variance from in-sample bootstrapped TD learning where Bellman backup errors compound across iterations, with known issues of advantage concentration near zero (Grigsby & Qi) and large weight instability (ODPR). Note: while IQL's expectile regression avoids out-of-distribution extrapolation error (a bias improvement), it does not eliminate the fundamental variance from iterative Bellman backups — the expected high variance is an empirical prediction to be validated; (2) VIP/R3M temporal contrastive encoders — expected low variance from frozen pretrained representations trained with stable contrastive/supervised objectives on large video datasets (Ego4D), though domain gap (Ego4D → robot manipulation) could degrade rank stability — this is an empirical question; (3) RINSE smoothness metrics (SAL, TED) — expected moderate variance, deterministic functions of trajectory geometry but sensitive to trajectory segmentation.\\n\\nFor each estimator class, we measure: (a) rank-order stability via bootstrap Kendall's τ (the primary reliability metric), (b) score variance across dataset subsamples, (c) calibration (correlation between estimated and true quality).\\n\\n**Minimum effect size requirements**: For the framework to be informative, we require: (i) at least 0.15 τ̄ gap between the highest and lowest estimator classes (e.g., VIP/R3M vs. IQL), sufficient to place them in distinct strategy-preference regimes; (ii) a statistically significant correlation (p < 0.05) between τ̄ and the relative performance of continuous-vs-binary weighting across the estimator × task grid; (iii) the adaptive algorithm matching or exceeding the best fixed strategy on ≥80% of estimator × task combinations. If (i) holds but (ii) does not achieve R² > 0.3, we present the adaptive algorithm result (iii) as the primary contribution and the variance-spectrum correlation as suggestive rather than definitive.\\n\\n**Critical empirical test of the An et al. tension**: We directly address the strongest theoretical objection. An et al. prove resampling > reweighting under constant-LR SGD on convex losses. Our IL training uses Adam with weight decay on nonconvex diffusion policy networks — violating all three assumptions. We show that for VIP/R3M scores (low variance, high rank stability), continuous weighting outperforms binary filtering, demonstrating that (a) the optimizer-level disadvantage does not manifest under Adam, consistent with the gap An et al. themselves acknowledge, and (b) estimator-level signal quality becomes the dominant factor in modern IL training. If this result does NOT hold (see null-result contingency below), this constitutes evidence that the SGD dynamics advantage of resampling extends beyond its theoretical assumptions, which is itself a novel and publishable finding.\\n\\n**Null-result contingency (structured as a paper-internal pivot)**: If VIP/R3M continuous weighting does NOT outperform binary filtering — i.e., the An et al. tension experiment fails — the paper pivots cleanly:\\n- PRIMARY result becomes: 'The adaptive algorithm matches or exceeds the best fixed strategy across the full estimator × task grid, because it measures estimator reliability before committing to a strategy.' This is the 'measuring before committing never hurts' result — weaker but practical and independently valuable.\\n- SECONDARY result: the variance-spectrum correlation, presented as a partial characterization with caveats about which regime transitions are reliable.\\n- REFRAMING: instead of 'low-variance estimators overcome SGD dynamics,' the narrative becomes 'score reliability predicts ROBUSTNESS to strategy choice' — high-stability estimators are less sensitive to the filter/weight decision, while low-stability estimators strongly favor filtering. This reframing is consistent with the same theoretical decomposition (when σ_f is small, R_filter ≈ R_weight, so the choice matters less).\\n- IMPLICATION: Even in the null-result scenario, the contribution over SARM/RA-BC (which fixes the form) and RINSE (which is single-estimator) remains clear.\\n\\n**Practical Adaptive Algorithm (3 stages)**:\\n(1) Score: Compute per-transition quality scores using any pretrained estimator. We demonstrate with frozen VIP/R3M embeddings (cosine similarity to goal embedding) and IQL Q-values (pretrained on the same dataset) — no from-scratch training required.\\n(2) Adapt: Estimate score reliability via bootstrap rank stability. Draw B=50 bootstrap resamples of the score vector, compute pairwise Kendall's τ, and take the mean τ̄. If τ̄ > τ_crit, select continuous softmax weighting with temperature T = c · σ_f (where c is calibrated via held-out validation, and σ_f is the bootstrap-estimated score standard deviation); if τ̄ ≤ τ_crit, select binary filtering at the median-split threshold. We ablate over: (a) the threshold τ_crit ∈ {0.6, 0.7, 0.8}, (b) alternative reliability metrics (coefficient of variation σ_f/|μ_f|, split-half correlation), and (c) temperature schedules (T = c·σ_f vs. T = c·σ_f·sqrt(log N) vs. cross-validated T).\\n(3) Train: Fine-tune the policy (diffusion policy or OpenVLA-OFT with LoRA) using the selected weighted/filtered BC loss.\\n\\n**Evaluation**: We evaluate on two tiers:\\n\\n*Tier 1 — Simulation (primary, all experiments)*: RoboMimic (5 tasks: Lift, Can, Square, Transport, ToolHang) and LIBERO-Long (10 tasks) using diffusion policy as the primary backbone and OpenVLA-OFT as secondary. Compare against: (a) unweighted BC (no curation), (b) SCIZOR binary filtering, (c) RINSE SAL/TED filtering and weighting, (d) SARM/RA-BC fixed hybrid, (e) fixed-binary and fixed-continuous baselines with our scores. Critical experiments:\\n(i) Binary vs. continuous with SAME scores across all 3 estimator classes — the central experiment isolating the strategy question.\\n(ii) Rank stability vs. performance correlation: for each estimator × task, measure τ̄ and plot against the relative performance gap of binary vs. continuous. Report R² and p-value; require R² > 0.3 for the correlation claim.\\n(iii) Adaptive selection accuracy: prediction accuracy of the τ̄-based criterion.\\n(iv) Adaptive vs. fixed strategies: show VGDC ≥ max(always-filter, always-weight) across the full grid.\\n(v) Ablation on reliability metrics, temperature formulas, and bootstrap parameters.\\n(vi) Direct test of An et al. tension: VIP/R3M continuous weighting vs. binary filtering under Adam training.\\n\\n*Tier 2 — Minimal real-robot validation (2 tasks)*: To validate that the framework transfers beyond simulation, we include a focused real-robot experiment on 2 manipulation tasks (e.g., pick-and-place and stacking on Franka Panda) with a single estimator pair (VIP vs. IQL). Protocol: collect ~80 demonstrations per task with mixed quality (varied teleoperator skill), run VGDC adaptive selection, and compare against fixed-binary and fixed-continuous baselines over 25 evaluation rollouts per condition. This tests the core prediction (VIP → weighting, IQL → filtering) on real data distributions without requiring the full estimator × task grid. If robot access is unavailable, we substitute with curating real-world demonstration data from Open X-Embodiment using our framework and training in simulation with the curated real data — partial real-world validation that still tests the framework on real data distributions.\\n\\n**Justification for simulation emphasis**: Our contribution is a DIAGNOSTIC FRAMEWORK for characterizing estimator properties and selecting strategies, not a new curation method. The estimators tested (frozen VIP/R3M checkpoints, pretrained IQL) are the same checkpoints used in real-world deployments (VIP demonstrated real-world few-shot RL with 20 trajectories; R3M enabled real manipulation with 20 demos). The diagnostic (rank stability measurement) is a property of the ESTIMATOR, not the environment — it transfers by construction. The sim experiments provide the controlled conditions needed for the systematic estimator × strategy comparison that is the paper's primary contribution, while the Tier 2 experiment validates transfer.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~160h A100-80GB (scoring: ~3h forward passes across 3 estimator classes on RoboMimic+LIBERO using frozen checkpoints, policy training: ~8h/run × 10 runs for binary/continuous × 3 estimators × 2 benchmarks with early stopping, evaluation: ~15h rollouts, real-robot training+eval: ~20h)\",\n      \"gpu_utilization\": \"Good (~65%); scoring is lightweight frozen encoder forward passes, training is the bottleneck\",\n      \"timeline\": \"2–2.5 weeks (3 days scoring + variance characterization, 5 days main sim experiments with 2-GPU parallelism, 2 days real-robot data collection + training, 3 days analysis + writing + ablations) — feasible for CoRL 2026 deadline with existing infrastructure\",\n      \"team\": \"1–2 researchers with existing RoboMimic/LIBERO setup, pretrained IQL/VIP/R3M checkpoints, and access to a Franka Panda or similar platform\",\n      \"estimated_gpu_cost\": \"$240–320 (160h × $1.50–2.00/hr)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~200h A100-80GB (additional runs for full ablation grid, robustness experiments, and real-robot training)\",\n      \"gpu_utilization\": \"Good (~65%); agent orchestrates scoring and training while human develops proof sketch, manages real-robot experiments, and reviews theoretical framing\",\n      \"timeline\": \"12–14 days (targeting CoRL 2026 abstract May 26, paper May 28)\",\n      \"team\": \"1 researcher, ~4h/day for proof sketch, real-robot experiments, experiment design, and paper drafting\",\n      \"claude_api_cost\": \"$80–150 (~800–1500 Opus turns for experiment orchestration, analysis, LaTeX writing)\",\n      \"estimated_gpu_cost\": \"$300–400 (200h × $1.50–2.00/hr)\",\n      \"risk_note\": \"Tight timeline requires existing infrastructure and robot access. Real-robot experiments can be descoped to Tier 2 fallback (OXE data curation) if hardware is unavailable. Bias-variance decomposition needs careful but informal proof sketch — full formal proofs can go in appendix or camera-ready.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~260h A100-80GB (full estimator × strategy × benchmark × ablation grid + real-robot training)\",\n      \"gpu_utilization\": \"High (~70%); scoring parallelizable, training is sequential bottleneck\",\n      \"timeline\": \"10–13 days with 2× A100 parallelism\",\n      \"team\": \"0 (initial setup: provide pretrained VIP/R3M/IQL checkpoints, RINSE implementation, benchmark configs, robot access for Tier 2)\",\n      \"claude_api_cost\": \"$120–250 (~1200–2500 Opus turns)\",\n      \"estimated_gpu_cost\": \"$390–520 (260h × $1.50–2.00/hr)\",\n      \"speed_bottleneck\": \"Policy training (~8h/run) is sequential; with 2 GPUs and ~10 unique conditions, ~40h for training phase. Scoring and variance characterization are fully parallelizable. Real-robot data collection requires human involvement.\",\n      \"risk_note\": \"Agent can run sim experiments but proof sketch and real-robot experiments require human involvement. Risk: if VIP/R3M do not outperform binary filtering with continuous weights, the paper pivots to the 'adaptive-vs-fixed' framing (see null-result contingency). If τ̄ separation between estimator classes is < 0.15, the clean three-class narrative weakens but the adaptive algorithm contribution remains valid.\"\n    }\n  },\n  \"target_venues\": [\n    \"CoRL 2026 (abstract deadline May 26, paper deadline May 28, 8 pages) — primary target. Two co-primary contributions (theory + empirical characterization) with 3 estimator classes. Proof sketch in main paper, full proofs in appendix. Minimal real-robot validation (2 tasks) strengthens empirical grounding.\",\n    \"ICRA 2027 (expected deadline ~September 2026) — fallback with expanded scope: 5+ estimator classes (add Robometer, VLM reward models, MI estimators), OXE-scale experiments, full formal theorems, comprehensive real-robot experiments.\"\n  ],\n  \"level\": \"solid-to-strong\",\n  \"key_references\": [\n    \"Why Resampling Outperforms Reweighting for Correcting Sampling Bias with Stochastic Gradients (An et al., ICLR 2021) — proves resampling > reweighting under constant-LR SGD on convex losses; theorem does not cover Adam/nonconvex networks; our framework adds the orthogonal estimator-level factor and tests whether their result extends beyond its theoretical assumptions\",\n    \"What is the Effect of Importance Weighting in Deep Learning? (Byrd & Lipton, ICML 2019) — shows importance weighting has diminishing effects in overparameterized networks on separable data; L2 regularization restores the effect; context for why continuous weighting may underperform but not a universal result\",\n    \"SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation (Chen et al., ICLR 2026) — introduces RA-BC with hybrid w_i = 1{r̂_i > κ} + 1{0 ≤ r̂_i ≤ κ} · w̃_i; κ=0.01 is a fixed hyperparameter (top 5% at ~90s task duration); only w̃_i uses adaptive running statistics (μ, σ) via Welford's estimator. Fixes both form AND threshold; we select the form based on estimator properties\",\n    \"Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning (RINSE, ICML 2025 Workshop DataWorld; extended arXiv 2604.23000, April 2026) — derives E(k) ≈ σ̄²(k) + C·d/(kT) for smoothness metrics; April 2026 arXiv version does not include cross-estimator analysis or adaptive strategy selection. Our framework subsumes this as single-estimator special case and adds cross-estimator adaptive selection\",\n    \"A Closer Look at Advantage-Filtered Behavioral Cloning in High-Noise Datasets (Grigsby & Qi, arXiv 2021) — found binary filtering more robust than AWR weighting for Q-function scores due to advantage concentration and temperature sensitivity; our framework provides variance-based explanation\",\n    \"Decoupled Prioritized Resampling for Offline RL (Yang et al., NeurIPS 2023) — found resampling outperforms reweighting for offline RL; identified large weight instability; introduced decoupled sampling. Addresses prioritized sampling but not binary-vs-continuous modality\",\n    \"Why Less is More (Sometimes): A Theory of Data Curation (ICLR 2026) — derives phase transitions for data pruning; addresses quantity not filter-vs-weight modality\",\n    \"Reliable Conditioning of Behavioral Cloning for Offline Reinforcement Learning (CWBC, arXiv 2022) — trajectory weighting with conservative regularization; proposes a scheme but does not derive when filtering outperforms weighting\",\n    \"Density-Ratio Weighted Behavioral Cloning (Oct 2025) — finite-sample bounds for weighted BC from corrupted datasets assuming known density ratios\",\n    \"Ideal Spatial Adaptation by Wavelet Shrinkage (Donoho & Johnstone, Biometrika 1994) — classical hard vs. soft thresholding theory; conceptual inspiration for noise-dependent strategy selection\",\n    \"SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (ICRA 2026) — self-supervised binary filtering baseline achieving 15.4% average improvement; real-robot results on Franka and YAM\",\n    \"Curating Demonstrations using Online Experience (Demo-SCORE, RSS 2025) — online experience-based binary filtering with real-world Franka experiments\",\n    \"TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics (Feb 2026) — VLM-based continuous weighting; evaluated on 130+ real-world tasks\",\n    \"Value-aligned Behavior Cloning for Offline RL via Bi-level Optimization (VACO, ICLR 2025) — meta-scoring for weighted BC\",\n    \"Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons (Liang & Korkmaz et al., RSS 2026) — dense reward model trained on RBM-1M (1M+ trajectories, 21 embodiments) via dual progress + preference objectives; explicitly evaluated for data retrieval + IL; relevant as a quality estimator class with potentially high rank stability due to preference regularization\",\n    \"Data Retrieval with Importance Weights for Few-Shot Imitation Learning (IWR, Xie et al., CoRL 2025 Oral) — density-ratio retrieval (p_target/p_prior via KDE) with hard threshold selection; hybrid of continuous scoring + binary filtering that does not address which modality is optimal given estimator noise\",\n    \"Green-VLA: Staged Vision-Language-Action Model for Generalist Robots (Apanasevich et al., arXiv Jan 2026) — includes DataQA pipeline using heuristic metrics (tremble score, sharpness, visual/state-space diversity) for binary filtering at scale; motivates principled alternatives to hand-designed quality heuristics\",\n    \"DataMIL: Selecting Data for Robot Imitation Learning with Datamodels (UT Austin, 2025) — policy-aware data selection on OXE\",\n    \"CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025) — influence-function-based curation with real-robot Franka FR3 experiments\",\n    \"Quality over Quantity: Demonstration Curation via Influence Functions (QoQ, ICRA 2026) — influence-function-based per-sample curation\",\n    \"Robot Data Curation with Mutual Information Estimators (DemInf, RSS 2025) — MI-based quality estimation with real ALOHA and Franka experiments; future extension estimator class\",\n    \"VIP: Towards Universal Visual Reward and Representation via Value-Implicit Pre-Training (ICLR 2023) — temporal contrastive encoder; demonstrated real-world few-shot RL with 20 trajectories\",\n    \"R3M: A Universal Visual Representation for Robot Manipulation (CoRL 2023) — time-contrastive + video-language encoder; enabled real manipulation with 20 demonstrations\",\n    \"Offline Reinforcement Learning with Implicit Q-Learning (IQL, ICLR 2022) — in-sample Q-function estimation with expectile regression; reduces extrapolation error (bias) but retains variance from iterative Bellman backups\",\n    \"OpenVLA: An Open-Source Vision-Language-Action Model (ICML 2025) — VLA backbone\",\n    \"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success (OpenVLA-OFT, 2025) — LoRA fine-tuning recipe\",\n    \"Advantage-Weighted Regression (Peng et al., ICLR 2020) — AWR theoretical foundation for exponential weighting\",\n    \"Thresholding Data Shapley for Data Cleansing Using Multi-Armed Bandits (Namba et al., 2024) — thresholding theory applied to data quality scores\"\n  ],\n  \"description\": \"We propose Variance-Guided Demo Curation (VGDC), a framework with two co-primary contributions addressing the unresolved question of whether robot demonstration quality scores should be used for binary filtering or continuous weighting.\\n\\nFirst, we derive a novel bias-variance decomposition of weighted BC suboptimality that structurally distinguishes the two strategies. Binary filtering suboptimality is dominated by misclassification at the decision boundary — P(sign(f−c) ≠ sign(f*−c)) · Δ_q — a LOCAL noise property (only errors near the threshold matter). Continuous weighting suboptimality is dominated by global estimator MSE amplified through weights — C·σ_f²/T + α·T — where all score errors contribute. This decomposition reveals that high-variance estimators favor filtering (noise away from the boundary is harmless) while low-variance estimators favor weighting (precise ordinal information is preserved). The optimal temperature satisfies T* ∝ σ_f, derived from our own analysis. This result is distinct from An et al.'s SGD-level analysis (ours is estimator-level and holds regardless of optimizer), RINSE's single-estimator E(k) formula (which we subsume as a special case), ODPR's decoupled sampling (prioritized but not binary-vs-continuous), and CWBC/Density-Ratio Weighted BC (which propose schemes but don't characterize the filter-vs-weight boundary).\\n\\nSecond, we conduct the first systematic empirical characterization of quality score reliability across three estimator classes spanning the variance spectrum: IQL Q-function advantages (expected high variance from iterative Bellman backups, despite expectile regression reducing extrapolation error), VIP/R3M contrastive encoders (expected low variance from frozen pretrained representations, subject to domain gap verification), and RINSE smoothness metrics (expected moderate variance, deterministic). We measure rank-order stability under bootstrap resampling (Kendall's τ̄) as the primary reliability metric. We state explicit minimum effect size requirements: ≥0.15 τ̄ gap between estimator classes, R² > 0.3 for the strategy-performance correlation, and ≥80% adaptive selection accuracy.\\n\\nThe framework includes a structured null-result contingency. If continuous weighting does NOT outperform binary filtering for VIP/R3M (the An et al. tension experiment fails), the paper pivots: the primary result becomes 'the adaptive algorithm matches or exceeds any fixed strategy because it measures reliability before committing' — the 'measuring never hurts' result. This is independently valuable (SARM/RA-BC commits to a fixed form; we adapt) and consistent with the decomposition (when estimator variance is low, R_filter ≈ R_weight, so the strategy choice matters less, and the adaptive algorithm correctly identifies this regime).\\n\\nThe practical synthesis is an adaptive algorithm: score demos with any pretrained estimator, measure rank stability via bootstrap, and automatically select binary filtering or continuous weighting (with temperature T = c·σ_f). We evaluate on RoboMimic (5 tasks) and LIBERO-Long (10 tasks) with diffusion policy and OpenVLA-OFT, plus minimal real-robot validation (2 tasks on Franka with VIP vs. IQL) to demonstrate framework transfer. We compare against SCIZOR, RINSE, SARM/RA-BC, IWR, and fixed baselines. Estimated compute: 160–260 A100-hours. Primary target: CoRL 2026.\",\n  \"project_name\": \"ss_temporal_adv_scoring\",\n  \"source\": \"web_research\"\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0b4192b-a0d4-400e-a8c9-9c099b493843",
  "isSidechain": false,
  "requestId": "req_011CazWhY8EUNjjxmr1j8yCV",
  "type": "assistant",
  "uuid": "867f55d1-f19f-4e07-8096-4ddf2313dea7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rgbr6udj9D36797vCGcRDC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14204,
      "cache_read_input_tokens": 26881,
      "output_tokens": 10903,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14204,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10903,
          "cache_read_input_tokens": 26881,
          "cache_creation_input_tokens": 14204,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14204
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-13T11:50:56.722Z_

<details><summary>↩ Tool result · reported error · `toolu_01S419qa1a4teamFraSqP1vk`</summary>

```text
Claude requested permissions to write to /tmp/revised_idea_round7.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "867f55d1-f19f-4e07-8096-4ddf2313dea7",
  "isSidechain": false,
  "promptId": "be2e7cb9-6b3c-4100-b637-6009b3c1fbfe",
  "type": "user",
  "uuid": "70f5b8ba-3743-4077-92c7-f894eb26bdca",
  "toolUseResult": "Error: Claude requested permissions to write to /tmp/revised_idea_round7.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "867f55d1-f19f-4e07-8096-4ddf2313dea7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34 · 2026-05-13T11:50:56.727Z_

```json
{
  "parentUuid": "70f5b8ba-3743-4077-92c7-f894eb26bdca",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "cade5958-220b-4b94-a772-dc134da5014f",
  "timestamp": "2026-05-13T11:50:56.727Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"When to Filter, When to Weight: A Bias-Variance Framework for Adaptive…",
  "leafUuid": "cade5958-220b-4b94-a772-dc134da5014f",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Adaptive demo curation via estimator reliability",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96"
}
```

---

### Assistant

_source line 37 · 2026-05-13T11:50:59.391Z_

<details><summary>Logged reasoning block</summary>

```text
The user hasn't granted permission to write to /tmp. Let me just output the JSON directly in my response.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cade5958-220b-4b94-a772-dc134da5014f",
  "isSidechain": false,
  "requestId": "req_011CazX3SAci2faSho8QrXeP",
  "type": "assistant",
  "uuid": "fd6ea327-25d1-4fb0-989a-2c3596106db1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AgXWqAu23UdMoQo1hGKe2V",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11051,
      "cache_read_input_tokens": 41085,
      "output_tokens": 9841,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11051,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9841,
          "cache_read_input_tokens": 41085,
          "cache_creation_input_tokens": 11051,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11051
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-13T11:54:31.741Z_

Here is the complete revised idea. This is a **major revision** that keeps the core idea but substantially strengthens scientific robustness across all six reviewer issues.

**What changed and why:**

1. **SARM κ fixed** — Corrected throughout to "κ=0.01 is a fixed hyperparameter; only w̃_i uses adaptive running statistics (μ, σ) via Welford's estimator." This actually strengthens our differentiation: SARM fixes both form AND threshold.

2. **Three missing references added** — Robometer (RSS 2026, dense reward model on 1M+ trajectories), IWR (CoRL 2025 Oral, density-ratio retrieval with hard threshold), Green-VLA (Jan 2026, DataQA heuristic filtering at scale). All integrated into landscape, opportunity, and key_references.

3. **RINSE arXiv timing addressed** — Noted the April 2026 arXiv version (v1, no stated venue) and confirmed it does NOT include cross-estimator analysis or adaptive strategy selection. Our novelty is safe.

4. **Minimum effect sizes quantified** — Explicitly requires ≥0.15 τ̄ gap between estimator classes, R² > 0.3 for strategy-performance correlation, ≥80% adaptive selection accuracy. If R² < 0.3, the adaptive algorithm becomes the primary contribution.

5. **Structured null-result contingency** — If VIP/R3M continuous weighting doesn't beat binary (An et al. tension fails), paper pivots to "measuring reliability before committing never hurts" as primary result. Reframing: score reliability predicts robustness to strategy choice, not necessarily which strategy wins.

6. **Real-robot experiments added** — Two-tier evaluation: Tier 1 (sim, all experiments) + Tier 2 (2 real tasks on Franka with VIP vs. IQL). Fallback: curate OXE real data if hardware unavailable. Strong justification for simulation emphasis (diagnostic framework, same frozen checkpoints used in real deployments).

7. **An et al. characterization sharpened** — Exploits the key gap: theorem requires constant-LR SGD on convex losses; modern IL uses Adam + nonconvex networks. Their own paper acknowledges this doesn't cover Adam.

8. **IQL characterization corrected** — Changed from "high variance" to more nuanced: expectile regression reduces extrapolation error (bias improvement) but retains variance from iterative Bellman backups. Framed as empirical prediction to validate.

9. **ODPR (NeurIPS 2023) added** — New reference for resampling vs. reweighting in offline RL, supporting the high-variance → filtering pattern.

```json
{
  "change_type": "major",
  "title": "When to Filter, When to Weight: A Bias-Variance Framework for Adaptive Demo Curation",
  "core_problem": "Given a quality scoring function for robot demonstrations, should training signals be binarized (keep/discard) or used as continuous weights? The demo curation field has produced 15+ methods in 2024–2026, each making an ad hoc choice: SCIZOR and Demo-SCORE use binary filtering, TOPReward and VACO use continuous weighting, IWR uses continuous density ratios but applies a hard selection threshold, Green-VLA's DataQA uses heuristic-based binary filtering, and SARM/RA-BC (ICLR 2026) uses a hybrid with a fixed threshold κ=0.01 and adaptive soft weights w̃_i but a fixed functional form. While the general ML literature offers relevant theory — An et al. (ICLR 2021) prove resampling outperforms reweighting under SGD dynamics with constant learning rate on convex losses, Byrd & Lipton (ICML 2019) show diminishing weighting effects in overparameterized networks on separable data — these results address the optimizer level (SGD) under restrictive assumptions (constant LR, convexity) that do not hold for modern IL training (Adam, nonconvex policy networks). They also do not address the estimator level: whether the quality scores themselves are precise enough to justify continuous use. The choice between filtering and weighting remains ad hoc and disconnected from the properties of the specific quality estimator being used.",
  "opportunity": "The proliferation of diverse quality estimators — Q-function advantages (IQL), temporal contrastive encoders (VIP, R3M), smoothness metrics (RINSE SAL/TED), VLM reward models (TOPReward), dense general-purpose reward models (Robometer), influence functions (CUPID, QoQ), and density-ratio methods (IWR) — makes this question increasingly urgent. These estimators differ fundamentally in their noise properties: IQL Q-values arise from in-sample bootstrapped TD learning that, despite expectile regression reducing extrapolation error, still accumulates estimation errors across Bellman backups and suffers from advantage concentration near zero; VIP/R3M scores come from frozen pretrained encoders with stable contrastive/supervised objectives on large video datasets (Ego4D); RINSE smoothness metrics are deterministic functions of trajectory geometry; Robometer provides dense progress scores from preference-trained reward models on 1M+ trajectories. Our key insight is that the reliability of ordinal information in quality scores — measurable as rank-order stability under bootstrap resampling — is the primary factor governing whether binary filtering or continuous weighting is optimal. This connects to a classical intuition: noisy estimates are better thresholded (only the sign/rank-class matters), while precise estimates should be used continuously (preserving ordinal information). Unlike prior work that provides better scores (SCIZOR, RINSE, QoQ, Robometer) or proposes a specific weighting scheme (SARM/RA-BC, CWBC), we address the orthogonal question of what to DO with any given set of scores. The opportunity is twofold: (a) a theoretical decomposition of weighted BC suboptimality into strategy-specific terms that reveals the estimator-property dependence, and (b) a practical adaptive algorithm that measures score reliability and automatically selects the appropriate strategy.",
  "landscape": "Demo curation for robot learning is an extremely active area with 15+ papers at top venues in 2024–2026.\n\n**Binary filtering methods**: SCIZOR (ICRA 2026) uses a self-supervised temporal distance classifier for binary keep/discard, achieving 15.4% average improvement (5.4% RoboMimic, 8.1% OXEMagic, 32.9% Sirius-Fleet), with real-robot results on Franka and YAM. Demo-SCORE (RSS 2025) trains a success/failure classifier from online rollouts, achieving 15–35% higher success rate with real-world Franka experiments. Green-VLA (arXiv, Jan 2026) includes a DataQA pipeline using heuristic metrics (tremble score, sharpness, visual/state-space diversity via DINOv3 features) for binary filtering of 3,000+ hours of teleoperation data — demonstrating that heuristic-based filtering is being deployed at scale, motivating principled alternatives.\n\n**Continuous/weighted methods**: TOPReward (Feb 2026) extracts task progress from VLM token logits for advantage-weighted BC, evaluated on 130+ real-world tasks across Franka, YAM, SO-100/101. VACO (ICLR 2025) uses a meta-scoring network with value alignment for weighted BC via bi-level optimization.\n\n**Hybrid and density-ratio methods**: SARM/RA-BC (ICLR 2026) introduces a hybrid weight formula w_i = 1{r̂_i > κ} + 1{0 ≤ r̂_i ≤ κ} · w̃_i where w̃_i = clip((r̂_i − (μ−2σ))/(4σ+ε), 0, 1), with κ=0.01 as a fixed hyperparameter (corresponding to the top 5% of demonstrations at ~90s task duration) and w̃_i computed adaptively via Welford's estimator for running μ and σ of progress deltas. This is the closest work to ours: it adapts soft-weight parameters within a FIXED functional form (always hybrid with fixed threshold + adaptive soft weights), whereas we select the functional form itself (binary vs. continuous) based on measured estimator properties. IWR (CoRL 2025, Oral) computes importance weights as the density ratio p_target/p_prior via Gaussian KDE for few-shot IL data retrieval — using continuous scores for selection but applying a hard threshold for final inclusion, an interesting hybrid that does not address which strategy is optimal given estimator noise properties.\n\n**General-purpose reward models**: Robometer (RSS 2026) is a dense, general-purpose robotic reward model trained on RBM-1M (1M+ trajectories, 21 embodiments) via dual progress + preference objectives. It provides frame-level quality scores and is explicitly evaluated for data retrieval + IL, making it directly relevant as a quality estimator class. Its reliability properties (trained on massive diverse data with preference regularization) are an interesting test case for our framework — prediction: preference-trained reward models should have moderate-to-high rank stability.\n\n**Quality-quantity analysis**: RINSE (ICML 2025 Workshop, DataWorld; extended arXiv version 2604.23000, April 2026) derives E(k) ≈ σ̄²(k) + C·d/(kT), decomposing error into a noise floor (reduced by filtering) and a statistical estimation term (increased by reducing data), and uses smoothness-based metrics for both binary filtering and continuous exponential weighting w(τ)=exp(−λq(τ)). The April 2026 arXiv version (v1, no stated venue) does NOT include cross-estimator analysis, adaptive strategy selection, or rank stability analysis — it remains focused on smoothness metrics (SAL, TED) with comparisons limited to random baselines and Re-Mix correlation. Our framework subsumes RINSE's decomposition as a special case (smoothness estimators, single-class) while extending to the multi-estimator adaptive setting with a principled selection criterion.\n\n**Prior work on filtering vs. weighting**: AFBC (Grigsby & Qi, arXiv 2021) tested binary AND exponential AWR weighting for BC with Q-function advantages, finding binary more robust. They attributed this to temperature sensitivity ('a change in β is enough to take us from near-failure to state-of-the-art performance') and advantage concentration near zero. ODPR (Yang et al., NeurIPS 2023) found resampling outperformed reweighting for offline RL prioritization, noting 'exceedingly large weights that may alter the learning rate' destabilize reweighting; they introduced decoupled sampling (uniform for value estimation, prioritized for policy improvement). Our framework provides a unifying explanation: both findings are consistent with high-variance estimators (bootstrapped Q-values) favoring binary/resampling strategies.\n\n**General ML theory**: An et al. (ICLR 2021) prove resampling outperforms reweighting via dynamical stability analysis of SGD — a strong prior FAVORING filtering. Critically, their theorem requires constant learning rate SGD on convex/piecewise-quadratic losses. They acknowledge this does not cover Adam, and their experiments using Adam lack theoretical backing. Modern IL training (Adam optimizer, nonconvex policy networks, weight decay) violates these assumptions, creating a gap between the theorem and practice that our empirical investigation directly addresses. Byrd & Lipton (ICML 2019) show importance weighting has diminishing effects in overparameterized networks on separable data — but this relies on convergence to max-margin solutions on separable data, and IL policy regression may not be separable; moreover, L2 regularization (common in IL) restores the weighting effect. 'Why Less is More (Sometimes)' (ICLR 2026) derives phase transitions for data pruning quantity but does not address the filter-vs-weight modality.\n\n**Policy-aware methods**: DataMIL (2025) uses datamodels for end-to-end data selection on OXE. CUPID (CoRL 2025) uses influence functions with real-robot experiments on Franka FR3. QoQ (ICRA 2026) uses influence functions for per-sample curation. DemInf (RSS 2025) uses mutual information estimators with real ALOHA and Franka experiments.\n\n**Critical gap**: Despite this extensive literature, no existing work (1) derives a suboptimality decomposition for weighted BC that separately characterizes the regimes where binary filtering vs. continuous weighting is tighter, (2) empirically demonstrates that estimator-level score reliability (not just score quality) predicts the optimal strategy, or (3) provides an adaptive algorithm that selects between strategies based on measured estimator properties. SARM/RA-BC fixes both its functional form (always hybrid) and its threshold (κ=0.01), adapting only the soft-weight statistics; our contribution is selecting the functional form itself based on measured estimator reliability.",
  "approach": "We propose Variance-Guided Demo Curation (VGDC), a framework with two co-primary contributions — a theoretical decomposition and an empirical characterization — synthesized into a practical adaptive algorithm.\n\n**Co-Primary Contribution A: Bias-Variance Decomposition for Weighted BC**. We derive a novel decomposition of weighted BC suboptimality that reveals why different quality estimators favor different strategies. Consider a dataset {τ_i}_{i=1}^N of demonstrations with true quality f*(τ_i) and estimated quality f(τ_i) = f*(τ_i) + ε_i. For binary filtering at threshold c, the suboptimality decomposes as:\n\nR_filter ≤ P(sign(f(τ)−c) ≠ sign(f*(τ)−c)) · Δ_q + d/(k·m)\n\nwhere the first term is the misclassification rate at the decision boundary (misclassifying good demos as bad or vice versa) scaled by the quality impact Δ_q, and the second term is the estimation error from the reduced dataset of size k. For continuous weighting with w_i ∝ exp(f(τ_i)/T), the suboptimality decomposes as:\n\nR_weight ≤ C · σ_f²/T + α · T + d/N_eff(T)\n\nwhere σ_f² = E[ε²] is the estimator MSE amplified through weights (noise amplification term), α·T captures the bias from temperature smoothing (higher T → more uniform → more bias from including low-quality demos), and N_eff(T) is the effective sample size under the weight distribution. The key structural difference: binary filtering suboptimality depends on noise at the DECISION BOUNDARY (only misclassifications matter — a local property), while continuous weighting suboptimality depends on GLOBAL noise properties (all scores contribute to weight errors). This explains why high-variance estimators favor filtering (most noise is away from the boundary and doesn't affect the binary decision) while low-variance estimators favor weighting (precise ordinal information is preserved). The optimal temperature T* that minimizes R_weight satisfies T* ∝ σ_f (noisier estimators require higher temperature, which reduces noise amplification but increases bias — eventually, binary filtering dominates). We provide a proof sketch in the main paper and full proofs in the appendix.\n\nThis decomposition is distinct from and complementary to: An et al.'s SGD dynamics analysis (optimizer-level under constant-LR SGD; our analysis is estimator-level and holds regardless of optimizer), RINSE's E(k) formula (single-estimator special case without strategy comparison), CWBC's trajectory weighting (proposes a scheme but doesn't derive when filtering wins), ODPR's decoupled sampling (addresses prioritized sampling but not the binary-vs-continuous modality), and Density-Ratio Weighted BC (assumes known density ratios, not noisy quality scores). We explicitly show that RINSE's E(k) ≈ σ̄²(k) + C·d/(kT) is recovered as a special case of our R_filter bound for deterministic smoothness estimators (σ_f = 0, no misclassification noise, only data quantity tradeoff).\n\n**Co-Primary Contribution B: Empirical Characterization Across 3 Estimator Classes**. We conduct the first systematic measurement of quality score reliability across three classes that span the variance spectrum: (1) IQL Q-function advantages — expected high variance from in-sample bootstrapped TD learning where Bellman backup errors compound across iterations, with known issues of advantage concentration near zero (Grigsby & Qi) and large weight instability (ODPR). Note: while IQL's expectile regression avoids out-of-distribution extrapolation error (a bias improvement), it does not eliminate the fundamental variance from iterative Bellman backups — the expected high variance is an empirical prediction to be validated; (2) VIP/R3M temporal contrastive encoders — expected low variance from frozen pretrained representations trained with stable contrastive/supervised objectives on large video datasets (Ego4D), though domain gap (Ego4D → robot manipulation) could degrade rank stability — this is an empirical question; (3) RINSE smoothness metrics (SAL, TED) — expected moderate variance, deterministic functions of trajectory geometry but sensitive to trajectory segmentation.\n\nFor each estimator class, we measure: (a) rank-order stability via bootstrap Kendall's τ (the primary reliability metric), (b) score variance across dataset subsamples, (c) calibration (correlation between estimated and true quality).\n\n**Minimum effect size requirements**: For the framework to be informative, we require: (i) at least 0.15 τ̄ gap between the highest and lowest estimator classes (e.g., VIP/R3M vs. IQL), sufficient to place them in distinct strategy-preference regimes; (ii) a statistically significant correlation (p < 0.05) between τ̄ and the relative performance of continuous-vs-binary weighting across the estimator × task grid; (iii) the adaptive algorithm matching or exceeding the best fixed strategy on ≥80% of estimator × task combinations. If (i) holds but (ii) does not achieve R² > 0.3, we present the adaptive algorithm result (iii) as the primary contribution and the variance-spectrum correlation as suggestive rather than definitive.\n\n**Critical empirical test of the An et al. tension**: We directly address the strongest theoretical objection. An et al. prove resampling > reweighting under constant-LR SGD on convex losses. Our IL training uses Adam with weight decay on nonconvex diffusion policy networks — violating all three assumptions of their theorem. We show that for VIP/R3M scores (low variance, high rank stability), continuous weighting outperforms binary filtering, demonstrating that (a) the optimizer-level disadvantage does not manifest under Adam, consistent with the gap An et al. themselves acknowledge, and (b) estimator-level signal quality becomes the dominant factor in modern IL training. If this result does NOT hold (see null-result contingency below), this constitutes evidence that the SGD dynamics advantage of resampling extends beyond its theoretical assumptions, which is itself a novel and publishable finding.\n\n**Null-result contingency (structured as a paper-internal pivot)**: If VIP/R3M continuous weighting does NOT outperform binary filtering — i.e., the An et al. tension experiment fails — the paper pivots cleanly:\n- PRIMARY result becomes: 'The adaptive algorithm matches or exceeds the best fixed strategy across the full estimator × task grid, because it measures estimator reliability before committing to a strategy.' This is the 'measuring before committing never hurts' result — weaker but practical and independently valuable.\n- SECONDARY result: the variance-spectrum correlation, presented as a partial characterization with caveats about which regime transitions are reliable.\n- REFRAMING: instead of 'low-variance estimators overcome SGD dynamics,' the narrative becomes 'score reliability predicts ROBUSTNESS to strategy choice' — high-stability estimators are less sensitive to the filter/weight decision, while low-stability estimators strongly favor filtering. This reframing is consistent with the same theoretical decomposition (when σ_f is small, R_filter ≈ R_weight, so the choice matters less).\n- IMPLICATION: Even in the null-result scenario, the contribution over SARM/RA-BC (which fixes the form) and RINSE (which is single-estimator) remains clear.\n\n**Practical Adaptive Algorithm (3 stages)**:\n(1) Score: Compute per-transition quality scores using any pretrained estimator. We demonstrate with frozen VIP/R3M embeddings (cosine similarity to goal embedding) and IQL Q-values (pretrained on the same dataset) — no from-scratch training required.\n(2) Adapt: Estimate score reliability via bootstrap rank stability. Draw B=50 bootstrap resamples of the score vector, compute pairwise Kendall's τ, and take the mean τ̄. If τ̄ > τ_crit, select continuous softmax weighting with temperature T = c · σ_f (where c is calibrated via held-out validation, and σ_f is the bootstrap-estimated score standard deviation); if τ̄ ≤ τ_crit, select binary filtering at the median-split threshold. We ablate over: (a) the threshold τ_crit ∈ {0.6, 0.7, 0.8}, (b) alternative reliability metrics (coefficient of variation σ_f/|μ_f|, split-half correlation), and (c) temperature schedules (T = c·σ_f vs. T = c·σ_f·sqrt(log N) vs. cross-validated T).\n(3) Train: Fine-tune the policy (diffusion policy or OpenVLA-OFT with LoRA) using the selected weighted/filtered BC loss.\n\n**Evaluation**: We evaluate on two tiers:\n\n*Tier 1 — Simulation (primary, all experiments)*: RoboMimic (5 tasks: Lift, Can, Square, Transport, ToolHang) and LIBERO-Long (10 tasks) using diffusion policy as the primary backbone and OpenVLA-OFT as secondary. Compare against: (a) unweighted BC (no curation), (b) SCIZOR binary filtering, (c) RINSE SAL/TED filtering and weighting, (d) SARM/RA-BC fixed hybrid, (e) fixed-binary and fixed-continuous baselines with our scores. Critical experiments:\n(i) Binary vs. continuous with SAME scores across all 3 estimator classes — the central experiment isolating the strategy question.\n(ii) Rank stability vs. performance correlation: for each estimator × task, measure τ̄ and plot against the relative performance gap of binary vs. continuous. Report R² and p-value; require R² > 0.3 for the correlation claim.\n(iii) Adaptive selection accuracy: prediction accuracy of the τ̄-based criterion.\n(iv) Adaptive vs. fixed strategies: show VGDC ≥ max(always-filter, always-weight) across the full grid.\n(v) Ablation on reliability metrics, temperature formulas, and bootstrap parameters.\n(vi) Direct test of An et al. tension: VIP/R3M continuous weighting vs. binary filtering under Adam training.\n\n*Tier 2 — Minimal real-robot validation (2 tasks)*: To validate that the framework transfers beyond simulation, we include a focused real-robot experiment on 2 manipulation tasks (e.g., pick-and-place and stacking on Franka Panda) with a single estimator pair (VIP vs. IQL). Protocol: collect ~80 demonstrations per task with mixed quality (varied teleoperator skill), run VGDC adaptive selection, and compare against fixed-binary and fixed-continuous baselines over 25 evaluation rollouts per condition. This tests the core prediction (VIP → weighting, IQL → filtering) on real data distributions without requiring the full estimator × task grid. If robot access is unavailable, we substitute with curating real-world demonstration data from Open X-Embodiment using our framework and training in simulation with the curated real data — partial real-world validation that still tests the framework on real data distributions.\n\n**Justification for simulation emphasis**: Our contribution is a DIAGNOSTIC FRAMEWORK for characterizing estimator properties and selecting strategies, not a new curation method. The estimators tested (frozen VIP/R3M checkpoints, pretrained IQL) are the same checkpoints used in real-world deployments (VIP demonstrated real-world few-shot RL with 20 trajectories; R3M enabled real manipulation with 20 demos). The diagnostic (rank stability measurement) is a property of the ESTIMATOR, not the environment — it transfers by construction. The sim experiments provide the controlled conditions needed for the systematic estimator × strategy comparison that is the paper's primary contribution, while the Tier 2 experiment validates transfer.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~160h A100-80GB (scoring: ~3h forward passes across 3 estimator classes on RoboMimic+LIBERO using frozen checkpoints, policy training: ~8h/run × 10 runs for binary/continuous × 3 estimators × 2 benchmarks with early stopping, evaluation: ~15h rollouts, real-robot training+eval: ~20h)",
      "gpu_utilization": "Good (~65%); scoring is lightweight frozen encoder forward passes, training is the bottleneck",
      "timeline": "2–2.5 weeks (3 days scoring + variance characterization, 5 days main sim experiments with 2-GPU parallelism, 2 days real-robot data collection + training, 3 days analysis + writing + ablations) — feasible for CoRL 2026 deadline with existing infrastructure",
      "team": "1–2 researchers with existing RoboMimic/LIBERO setup, pretrained IQL/VIP/R3M checkpoints, and access to a Franka Panda or similar platform",
      "estimated_gpu_cost": "$240–320 (160h × $1.50–2.00/hr)"
    },
    "human_in_loop": {
      "gpu_hours": "~200h A100-80GB (additional runs for full ablation grid, robustness experiments, and real-robot training)",
      "gpu_utilization": "Good (~65%); agent orchestrates scoring and training while human develops proof sketch, manages real-robot experiments, and reviews theoretical framing",
      "timeline": "12–14 days (targeting CoRL 2026 abstract May 26, paper May 28)",
      "team": "1 researcher, ~4h/day for proof sketch, real-robot experiments, experiment design, and paper drafting",
      "claude_api_cost": "$80–150 (~800–1500 Opus turns for experiment orchestration, analysis, LaTeX writing)",
      "estimated_gpu_cost": "$300–400 (200h × $1.50–2.00/hr)",
      "risk_note": "Tight timeline requires existing infrastructure and robot access. Real-robot experiments can be descoped to Tier 2 fallback (OXE data curation) if hardware is unavailable. Bias-variance decomposition needs careful but informal proof sketch — full formal proofs can go in appendix or camera-ready."
    },
    "auto_research": {
      "gpu_hours": "~260h A100-80GB (full estimator × strategy × benchmark × ablation grid + real-robot training)",
      "gpu_utilization": "High (~70%); scoring parallelizable, training is sequential bottleneck",
      "timeline": "10–13 days with 2× A100 parallelism",
      "team": "0 (initial setup: provide pretrained VIP/R3M/IQL checkpoints, RINSE implementation, benchmark configs, robot access for Tier 2)",
      "claude_api_cost": "$120–250 (~1200–2500 Opus turns)",
      "estimated_gpu_cost": "$390–520 (260h × $1.50–2.00/hr)",
      "speed_bottleneck": "Policy training (~8h/run) is sequential; with 2 GPUs and ~10 unique conditions, ~40h for training phase. Scoring and variance characterization are fully parallelizable. Real-robot data collection requires human involvement.",
      "risk_note": "Agent can run sim experiments but proof sketch and real-robot experiments require human involvement. Risk: if VIP/R3M do not outperform binary filtering with continuous weights, the paper pivots to the 'adaptive-vs-fixed' framing (see null-result contingency). If τ̄ separation between estimator classes is < 0.15, the clean three-class narrative weakens but the adaptive algorithm contribution remains valid."
    }
  },
  "target_venues": [
    "CoRL 2026 (abstract deadline May 26, paper deadline May 28, 8 pages) — primary target. Two co-primary contributions (theory + empirical characterization) with 3 estimator classes. Proof sketch in main paper, full proofs in appendix. Minimal real-robot validation (2 tasks) strengthens empirical grounding.",
    "ICRA 2027 (expected deadline ~September 2026) — fallback with expanded scope: 5+ estimator classes (add Robometer, VLM reward models, MI estimators), OXE-scale experiments, full formal theorems, comprehensive real-robot experiments."
  ],
  "level": "solid-to-strong",
  "key_references": [
    "Why Resampling Outperforms Reweighting for Correcting Sampling Bias with Stochastic Gradients (An et al., ICLR 2021) — proves resampling > reweighting under constant-LR SGD on convex losses; theorem does not cover Adam/nonconvex networks; our framework adds the orthogonal estimator-level factor and tests whether their result extends beyond its theoretical assumptions",
    "What is the Effect of Importance Weighting in Deep Learning? (Byrd & Lipton, ICML 2019) — shows importance weighting has diminishing effects in overparameterized networks on separable data; L2 regularization restores the effect; context for why continuous weighting may underperform but not a universal result",
    "SARM: Stage-Aware Reward Modeling for Long Horizon Robot Manipulation (Chen et al., ICLR 2026) — introduces RA-BC with hybrid w_i = 1{r̂_i > κ} + 1{0 ≤ r̂_i ≤ κ} · w̃_i; κ=0.01 is a fixed hyperparameter (top 5% at ~90s task duration); only w̃_i uses adaptive running statistics (μ, σ) via Welford's estimator. Fixes both form AND threshold; we select the form based on estimator properties",
    "Learning from the Best: Smoothness-Driven Metrics for Data Quality in Imitation Learning (RINSE, ICML 2025 Workshop DataWorld; extended arXiv 2604.23000, April 2026) — derives E(k) ≈ σ̄²(k) + C·d/(kT) for smoothness metrics; April 2026 arXiv version does not include cross-estimator analysis or adaptive strategy selection. Our framework subsumes this as single-estimator special case and adds cross-estimator adaptive selection",
    "A Closer Look at Advantage-Filtered Behavioral Cloning in High-Noise Datasets (Grigsby & Qi, arXiv 2021) — found binary filtering more robust than AWR weighting for Q-function scores due to advantage concentration and temperature sensitivity; our framework provides variance-based explanation",
    "Decoupled Prioritized Resampling for Offline RL (Yang et al., NeurIPS 2023) — found resampling outperforms reweighting for offline RL; identified large weight instability; introduced decoupled sampling. Addresses prioritized sampling but not binary-vs-continuous modality",
    "Why Less is More (Sometimes): A Theory of Data Curation (ICLR 2026) — derives phase transitions for data pruning; addresses quantity not filter-vs-weight modality",
    "Reliable Conditioning of Behavioral Cloning for Offline Reinforcement Learning (CWBC, arXiv 2022) — trajectory weighting with conservative regularization; proposes a scheme but does not derive when filtering outperforms weighting",
    "Density-Ratio Weighted Behavioral Cloning (Oct 2025) — finite-sample bounds for weighted BC from corrupted datasets assuming known density ratios",
    "Ideal Spatial Adaptation by Wavelet Shrinkage (Donoho & Johnstone, Biometrika 1994) — classical hard vs. soft thresholding theory; conceptual inspiration for noise-dependent strategy selection",
    "SCIZOR: A Self-Supervised Approach to Data Curation for Large-Scale Imitation Learning (ICRA 2026) — self-supervised binary filtering baseline achieving 15.4% average improvement; real-robot results on Franka and YAM",
    "Curating Demonstrations using Online Experience (Demo-SCORE, RSS 2025) — online experience-based binary filtering with real-world Franka experiments",
    "TOPReward: Token Probabilities as Hidden Zero-Shot Rewards for Robotics (Feb 2026) — VLM-based continuous weighting; evaluated on 130+ real-world tasks",
    "Value-aligned Behavior Cloning for Offline RL via Bi-level Optimization (VACO, ICLR 2025) — meta-scoring for weighted BC",
    "Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparisons (Liang & Korkmaz et al., RSS 2026) — dense reward model trained on RBM-1M (1M+ trajectories, 21 embodiments) via dual progress + preference objectives; explicitly evaluated for data retrieval + IL; relevant as a quality estimator class with potentially high rank stability due to preference regularization",
    "Data Retrieval with Importance Weights for Few-Shot Imitation Learning (IWR, Xie et al., CoRL 2025 Oral) — density-ratio retrieval (p_target/p_prior via KDE) with hard threshold selection; hybrid of continuous scoring + binary filtering that does not address which modality is optimal given estimator noise",
    "Green-VLA: Staged Vision-Language-Action Model for Generalist Robots (Apanasevich et al., arXiv Jan 2026) — includes DataQA pipeline using heuristic metrics (tremble score, sharpness, visual/state-space diversity) for binary filtering at scale; motivates principled alternatives to hand-designed quality heuristics",
    "DataMIL: Selecting Data for Robot Imitation Learning with Datamodels (UT Austin, 2025) — policy-aware data selection on OXE",
    "CUPID: Curating Data your Robot Loves with Influence Functions (CoRL 2025) — influence-function-based curation with real-robot Franka FR3 experiments",
    "Quality over Quantity: Demonstration Curation via Influence Functions (QoQ, ICRA 2026) — influence-function-based per-sample curation",
    "Robot Data Curation with Mutual Information Estimators (DemInf, RSS 2025) — MI-based quality estimation with real ALOHA and Franka experiments; future extension estimator class",
    "VIP: Towards Universal Visual Reward and Representation via Value-Implicit Pre-Training (ICLR 2023) — temporal contrastive encoder; demonstrated real-world few-shot RL with 20 trajectories",
    "R3M: A Universal Visual Representation for Robot Manipulation (CoRL 2023) — time-contrastive + video-language encoder; enabled real manipulation with 20 demonstrations",
    "Offline Reinforcement Learning with Implicit Q-Learning (IQL, ICLR 2022) — in-sample Q-function estimation with expectile regression; reduces extrapolation error (bias) but retains variance from iterative Bellman backups",
    "OpenVLA: An Open-Source Vision-Language-Action Model (ICML 2025) — VLA backbone",
    "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success (OpenVLA-OFT, 2025) — LoRA fine-tuning recipe",
    "Advantage-Weighted Regression (Peng et al., ICLR 2020) — AWR theoretical foundation for exponential weighting",
    "Thresholding Data Shapley for Data Cleansing Using Multi-Armed Bandits (Namba et al., 2024) — thresholding theory applied to data quality scores"
  ],
  "description": "We propose Variance-Guided Demo Curation (VGDC), a framework with two co-primary contributions addressing the unresolved question of whether robot demonstration quality scores should be used for binary filtering or continuous weighting.\n\nFirst, we derive a novel bias-variance decomposition of weighted BC suboptimality that structurally distinguishes the two strategies. Binary filtering suboptimality is dominated by misclassification at the decision boundary — P(sign(f−c) ≠ sign(f*−c)) · Δ_q — a LOCAL noise property (only errors near the threshold matter). Continuous weighting suboptimality is dominated by global estimator MSE amplified through weights — C·σ_f²/T + α·T — where all score errors contribute. This decomposition reveals that high-variance estimators favor filtering (noise away from the boundary is harmless) while low-variance estimators favor weighting (precise ordinal information is preserved). The optimal temperature satisfies T* ∝ σ_f, derived from our own analysis. This result is distinct from An et al.'s SGD-level analysis (ours is estimator-level and holds regardless of optimizer), RINSE's single-estimator E(k) formula (which we subsume as a special case), ODPR's decoupled sampling (prioritized but not binary-vs-continuous), and CWBC/Density-Ratio Weighted BC (which propose schemes but don't characterize the filter-vs-weight boundary).\n\nSecond, we conduct the first systematic empirical characterization of quality score reliability across three estimator classes spanning the variance spectrum: IQL Q-function advantages (expected high variance from iterative Bellman backups, despite expectile regression reducing extrapolation error), VIP/R3M contrastive encoders (expected low variance from frozen pretrained representations, subject to domain gap verification), and RINSE smoothness metrics (expected moderate variance, deterministic). We measure rank-order stability under bootstrap resampling (Kendall's τ̄) as the primary reliability metric. We state explicit minimum effect size requirements: ≥0.15 τ̄ gap between estimator classes, R² > 0.3 for the strategy-performance correlation, and ≥80% adaptive selection accuracy.\n\nThe framework includes a structured null-result contingency. If continuous weighting does NOT outperform binary filtering for VIP/R3M (the An et al. tension experiment fails), the paper pivots: the primary result becomes 'the adaptive algorithm matches or exceeds any fixed strategy because it measures reliability before committing' — the 'measuring never hurts' result. This is independently valuable (SARM/RA-BC commits to a fixed form; we adapt) and consistent with the decomposition (when estimator variance is low, R_filter ≈ R_weight, so the strategy choice matters less, and the adaptive algorithm correctly identifies this regime).\n\nThe practical synthesis is an adaptive algorithm: score demos with any pretrained estimator, measure rank stability via bootstrap, and automatically select binary filtering or continuous weighting (with temperature T = c·σ_f). We evaluate on RoboMimic (5 tasks) and LIBERO-Long (10 tasks) with diffusion policy and OpenVLA-OFT, plus minimal real-robot validation (2 tasks on Franka with VIP vs. IQL) to demonstrate framework transfer. We compare against SCIZOR, RINSE, SARM/RA-BC, IWR, and fixed baselines. Estimated compute: 160–260 A100-hours. Primary target: CoRL 2026.",
  "project_name": "ss_temporal_adv_scoring",
  "source": "web_research"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd6ea327-25d1-4fb0-989a-2c3596106db1",
  "isSidechain": false,
  "requestId": "req_011CazX3SAci2faSho8QrXeP",
  "type": "assistant",
  "uuid": "fdf75f19-dd28-466d-ae46-3c7d7b42d19a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AgXWqAu23UdMoQo1hGKe2V",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11051,
      "cache_read_input_tokens": 41085,
      "output_tokens": 9841,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11051,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9841,
          "cache_read_input_tokens": 41085,
          "cache_creation_input_tokens": 11051,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11051
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 39_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"When to Filter, When to Weight: A Bias-Variance Framework for Adaptive…",
  "leafUuid": "fdf75f19-dd28-466d-ae46-3c7d7b42d19a",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Adaptive demo curation via estimator reliability",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-13 (UTC).**  ## Original idea {   \"title\": \"When to Filter, When to Weight: A Bias-Variance Framework for Adaptive…",
  "leafUuid": "fdf75f19-dd28-466d-ae46-3c7d7b42d19a",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Adaptive demo curation via estimator reliability",
  "sessionId": "4e300a02-b1f1-43f9-b3ff-536ae7295d96"
}
```

---
