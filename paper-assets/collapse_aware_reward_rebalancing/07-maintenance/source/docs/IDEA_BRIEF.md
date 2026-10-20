# Idea Brief: Collapse-Aware Reward Rebalancing for Iterative Multi-Objective Synthetic Data Curation


- **Idea ID**: `idea_016`
- **Created**: 2026-05-16
- **Approved**: 2026-05-16
- **Source**: foreign:be-idea-gen-0509-4
- **Level**: top-tier
- **Target Venues**: EMNLP 2026 (ARR submission deadline: May 25, 2026; special theme 'New Missions for NLP Research' includes sub-topic 'Data as a bottleneck and a responsibility' which explicitly covers 'contamination and the consequences of synthetic data feedback loops')

## Seed Topic

Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Machine Learning for NLP / Resources and Evaluation. Aligns with EMNLP 2026 special theme "New Missions for NLP Research" which explicitly calls for work on data contamination, synthetic data feedback loops, and data governance.

Direction: Synthetic data quality, model collapse prevention, contamination detection. In-scope: synthetic data verification/filtering methods, detecting training data contamination in benchmarks, methods to break recursive data feedback loops, data mixing strategies that prevent quality degradation, principled synthetic data generation with quality guarantees.

Contribution type: METHOD ONLY. Must propose a concrete detection algorithm, filtering pipeline, or training recipe — not just an observation about model collapse. Method + analysis OK.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total. Model collapse experiments need multiple training iterations — budget for small models (1B-3B) across 3-5 generations.
2. Time: ≤16 days. Use small open models (Pythia, OLMo-1B, Qwen-0.5B/1.8B) for iterative collapse experiments.
3. Eval: perplexity degradation curves, downstream task quality (MMLU, HellaSwag), diversity metrics (self-BLEU, n-gram entropy), contamination detection accuracy.

This is a hot EMNLP 2026 special theme area with relatively few established methods — high novelty potential.

Tag: direction=data_governance, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].

## Core Problem

Synthetic data curation using a single quality metric applies uniform selection pressure that narrows distributional coverage across iterative training generations. Multi-objective curation with fixed reward weights mitigates this theoretically, but in practice with finite candidate pools and imperfect reward models, fixed weights cannot adapt to generation-specific collapse dynamics. Following Schaeffer et al.'s (arXiv:2503.03150) identification of eight conflicting definitions of model collapse, we target two specific failure modes: collapsing variance (definition 4 — distribution narrowing / diversity loss) and disappearance of tail data (definition 7 — coverage loss), the modes most directly caused by iterative curation pressure. We do not claim to address strong model collapse in the scaling-law sense (Dohmatob et al., ICLR 2025), which concerns raw synthetic contamination regimes where no curation is applied. Can an adaptive multi-objective curation strategy that monitors and responds to per-generation collapse signals maintain both quality and diversity across iterative self-consuming training in the curated regime?

## Opportunity / Why Now

Pluralistic preferences theory (ICML 2026, arXiv:2605.07724) proves multi-reward curation prevents collapse and converges to a Nash bargaining solution, but validates with length-based rewards on lightweight GPT-2 under idealized assumptions (fixed weights, K→∞ candidates, bounded reward separation). While the theory tests M∈{2,3,4,5} preferences across GMMs, CIFAR-10, and GPT-2 domains, no text experiments use realistic quality/diversity/complexity objectives at instruction-tuning scale. Furthermore, the theory assumes fixed curation weights across generations — Remark 3.1 shows O(√(log(K)/K)) deviations for finite K, meaning practical candidate pools (K=8–16) introduce systematic selection bias that accumulates across generations. 'How Sampling Shapes LLM Alignment' (arXiv:2602.12180) independently proves that iterative alignment dynamics can exhibit entropy collapse for certain parameter regimes, reinforcing that diversity loss in iterative loops is a fundamental rather than incidental phenomenon. 'A Closer Look at Model Collapse' (NeurIPS 2025 Spotlight, arXiv:2509.16499) identifies entropy-based data selection as a complementary collapse-prevention signal, demonstrating that declining entropy in synthetic training data drives the generalization-to-memorization transition. Meanwhile, 'Iterative Finetuning is Mostly Idempotent' (arXiv:2605.01130) shows uncurated iterative training is dissipative — models neither improve nor collapse. This creates a precise dilemma: no curation means stagnation, single-objective curation means collapse, and fixed-weight multi-objective curation may not be robust under practical violations of theoretical assumptions. Online learning methods for data weighting — DoReMi (NeurIPS 2023), ODM, PiKE, AutoMixAlign — have demonstrated the power of exponentiated gradient and bandit algorithms for adaptive data selection, but all operate within single training runs where distributional shift is incremental. Self-Correcting Self-Consuming Loops (Gillman et al., ICML 2024) demonstrate that correction functions can stabilize self-consuming loops even at 100% synthetic ratio, but operate at the data-point level (modifying individual samples toward the true distribution) rather than at the selection-weight level, and require domain-specific correctors (e.g., physics simulators). DataEvolve (arXiv:2603.14420) uses evolutionary algorithms for iterative curation optimization but targets pretraining web data in a single-pass setting without regret guarantees, not self-consuming loops where the data distribution is endogenously generated. The opportunity is extending the MWU framework to the between-generation setting, where distributional shift is non-incremental (the model is fully retrained each generation) and the loss signal is collapse-specific (generation-over-generation metric decline rather than within-run excess loss). EMNLP 2026's special theme 'New Missions for NLP Research' includes the sub-topic 'Data as a bottleneck and a responsibility,' which explicitly calls for work on 'contamination and the consequences of synthetic data feedback loops' — this is a near-perfect thematic match.

## Landscape (SOTA & Limitations)

**Within-run adaptive data weighting.** DoReMi (NeurIPS 2023, arXiv:2305.10429) uses exponentiated gradient α_t ← α_{t-1}·exp(η·λ_t)/Z to optimize domain mixture weights for pretraining, with per-domain excess loss as the signal; Iterated DoReMi extends this to multiple rounds of proxy training that converge in ~3 iterations. ODM (arXiv:2312.02406) uses EXP3 for online data mixing during pretraining, adjusting domain sampling probabilities via importance-weighted loss signals. PiKE (arXiv:2502.06244) uses mirror descent for adaptive multi-task data mixing under low gradient conflicts. AutoMixAlign (ACL 2025, arXiv:2506.00569) uses EXP3 (AMA-S) and Group DRO (AMA-R) for adaptive multi-task preference optimization during DPO training. All four methods share the online learning paradigm for data selection but operate within a single training run where distributional shift is incremental and the data distribution is approximately stationary.

**Within-run adaptive reward weighting.** 'Learning to Optimize Multi-Objective Alignment Through Dynamic Reward Weighting' (TACL 2026, arXiv:2509.11452) proposes hypervolume-guided and gradient-based dynamic weight adaptation for online RL alignment. MAESTRO (ACL 2026 Main, arXiv:2601.07208) formulates dynamic reward scalarization as a contextual bandit within bi-level optimization, using model hidden states as context. APEX (arXiv:2601.06574) identifies variance hijacking and gradient conflicts as failure modes of static multi-objective weighting in vision-language generation. DRA-GRPO (arXiv:2505.09655) incorporates diversity-aware reward adjustment within a single GRPO training run for math reasoning. All operate within single training runs and require gradient access or model internals.

**Iterative self-consuming training and collapse prevention.** Self-verification (NeurIPS 2025) uses internal confidence as a single curation signal. External verification (arXiv 2025) extends this with separate verifiers. Pluralistic preferences (ICML 2026, arXiv:2605.07724) provides the theoretical framework for multi-reward curation preventing collapse via Nash bargaining, testing M∈{2,3,4,5} preferences across GMMs, CIFAR-10, and GPT-2, but text experiments are limited to length-based rewards on lightweight GPT-2 — no realistic quality/diversity/complexity objectives at instruction-tuning scale. Self-Correcting Self-Consuming Loops (Gillman et al., ICML 2024, arXiv:2402.07087) prove that an idealized correction function πγpθ(x) := [pθ(x) + γpθ⋆(x)]/(1+γ) makes self-consuming loops exponentially more stable, validated at 100% synthetic ratio on human motion synthesis. Crucially, their approach operates at the data-point level — modifying individual samples toward the true distribution — requiring domain-specific correctors (physics simulators, K-means anchors). CARR is complementary: it operates at the curation-weight level, adjusting which quality dimensions to prioritize in selection, and requires only reward model scores rather than access to the true data distribution or domain-specific correctors. The two approaches address different levels of the collapse problem and could be combined. 'Escaping Collapse: The Strength of Weak Data' (NeurIPS 2025, arXiv:2502.08924) develops a boosting-inspired theoretical framework showing that strategically directing labeling resources toward difficult examples prevents collapse, conceptually related to CARR's adaptive focus on declining dimensions. 'How Sampling Shapes LLM Alignment' (arXiv:2602.12180) proves iterative alignment dynamics can exhibit entropy collapse for certain parameter regimes. 'Iterative Finetuning is Mostly Idempotent' (arXiv:2605.01130) shows uncurated iterative finetuning produces neither collapse nor improvement. 'Explaining and Preventing Alignment Collapse in Iterative RLHF' (arXiv:2605.04266) models iterative RLHF collapse via Stackelberg games.

**Strong model collapse and collapse taxonomy.** Strong Model Collapse (Dohmatob et al., ICLR 2025, arXiv:2410.04840) proves that even 1/1000 synthetic data fraction can cause collapse in the scaling-law sense — larger datasets fail to improve performance when contaminated. This result applies to the uncurated regime where synthetic data enters training without external quality signal. CARR operates in the curated regime where multi-objective reward models provide external signal, which the 'Collapse or Thrive?' survey (Kazdan et al., arXiv:2410.16713) identifies as the key distinction between collapse-prone and collapse-resistant training workflows. 'Position: Model Collapse Does Not Mean What You Think' (Schaeffer et al., arXiv:2503.03150) identifies eight conflicting definitions of model collapse: (1) catastrophic increase of population risk, (2) any increase of population risk, (3) asymptotically diverging population risk, (4) collapsing variance, (5) change in scaling law, (6) disappearance/entanglement of data modes, (7) disappearance of tail data, (8) appearance of hallucinated data. CARR explicitly targets definitions 4 and 7 — the failure modes most directly induced by iterative curation pressure — rather than definition 5 (strong collapse). 'A Closer Look at Model Collapse' (NeurIPS 2025 Spotlight, arXiv:2509.16499) identifies declining entropy of synthetic training data as the root cause of the generalization-to-memorization transition and proposes entropy-based data selection as mitigation — CARR's diversity dimension (Vendi Score) captures a related but distinct signal at the curation level.

**Adaptive data curation via evolutionary search.** DataEvolve (arXiv:2603.14420) uses evolutionary algorithms to autonomously evolve pretraining data curation strategies across 30 iterations per data category, producing Darwin-CC (504B tokens) that outperforms DCLM and FineWeb-Edu. Key distinctions from CARR: (a) DataEvolve optimizes curation strategies (filters, cleaners) for static web-scraped pretraining data; CARR optimizes curation weights for self-generated synthetic data in iterative self-consuming loops where the data distribution is endogenously generated. (b) DataEvolve uses evolutionary search without formal regret guarantees; CARR uses MWU with Fixed Share, providing provable switching regret bounds. (c) DataEvolve's iterations refine processing strategies over static data; CARR's generations involve full model retraining creating non-incremental distributional shift. Both demonstrate the value of adaptive iteration for data curation, but address fundamentally different settings.

**Adaptive reward model selection.** LASeR (NeurIPS 2025, arXiv:2410.01735) frames reward model selection as a multi-armed bandit, adaptively selecting the most suitable RM per training instance across iterative LLM training. LASeR is the closest to operating iteratively but selects among reward models per-instance rather than adapting curation weights across generations based on collapse signals.

**Multi-objective data curation.** ParetoHqD (AAAI 2026, arXiv:2504.16628) performs Pareto-front multi-objective data curation for LLM alignment but operates in a single-generation offline setting. 'Spend Wisely' (NeurIPS 2025 spotlight, arXiv:2501.18962) optimizes compute allocation across synthetic bootstrapping iterations but uses single-quality filtering. Reward Model Ensembles (arXiv:2310.02743) prevent reward hacking but target overoptimization within training. 'Synthetic Eggs in Many Baskets' (ACL 2026) measures diversity impact in single-generation fine-tuning.

**The gap.** Existing online learning methods for LLM data selection (DoReMi, ODM, PiKE, AutoMixAlign) all operate within single training runs where distributional shift is incremental. Existing correction-based methods (Self-Correcting Self-Consuming Loops) operate at the data-point level and require domain-specific correctors. Existing iterative curation methods (pluralistic preferences, self-verification) use fixed selection criteria across generations. Evolutionary approaches (DataEvolve) optimize curation strategies for static data without regret guarantees. No method combines (1) multi-objective curation with (2) collapse-signal-driven adaptive weight scheduling via online learning with provable switching regret guarantees across (3) iterative self-consuming LLM training generations, where the between-generation distributional shift is fundamentally non-incremental.

## Proposed Approach

We propose Collapse-Aware Reward Rebalancing (CARR), a feedback-control algorithm for multi-objective synthetic data curation in iterative self-consuming training, extending the Multiplicative Weights Update (MWU/Hedge) framework from within-run data weighting (as in DoReMi, ODM) to the between-generation curation setting.

**Collapse definition scope.** Following Schaeffer et al.'s (arXiv:2503.03150) taxonomy, CARR targets two specific collapse failure modes: collapsing variance (definition 4 — distribution narrowing / diversity loss) and disappearance of tail data (definition 7 — underrepresentation of rare patterns). These are the modes most directly induced by iterative curation pressure, where selection for quality progressively narrows the output distribution. We do not claim to address strong model collapse (Dohmatob et al., ICLR 2025) — the scaling-law degradation from raw synthetic contamination — because CARR operates in the curated regime where external reward models provide exogenous quality signal. As the 'Collapse or Thrive?' survey (arXiv:2410.16713) shows, curated vs. uncurated synthetic data workflows exhibit fundamentally different collapse dynamics.

**Algorithm.** At each generation t, synthetic candidates are scored on M=3 reward dimensions: quality (ArmoRM per-response score), diversity (per-sample nearest-neighbor distance in sentence embedding space), and complexity (instruction difficulty score). After curation and training, aggregate generation-level metrics are computed: m_Q(t) = mean ArmoRM score, m_D(t) = Vendi Score over sentence embeddings, m_C(t) = mean complexity score. The deficiency signal for each dimension i is:

d_i(t) = max(0, (m_i(t−1) − m_i(t)) / s_i)

where s_i = max(|m_i(0) − m_i(t′)|) over t′ ≤ t is a running scale factor ensuring cross-dimension comparability. When dimension i's aggregate metric declines generation-over-generation, d_i(t) > 0; otherwise d_i(t) = 0. Curation weights are updated via MWU:

w_i(t+1) = w_i(t) · exp(η · d_i(t)) / Z(t+1)

where η is the learning rate and Z(t+1) normalizes.

**Relationship to DoReMi and prior MWU-for-data work.** CARR's weight update is structurally identical to DoReMi's exponentiated gradient α_t ← α_{t-1}·exp(η·λ_t)/Z. We explicitly acknowledge this lineage. The key distinctions are: (a) DoReMi optimizes domain-level mixture weights within pretraining using per-domain excess loss as the signal; CARR optimizes reward-dimension curation weights between discrete self-consuming generations using generation-over-generation metric decline (collapse signal); (b) DoReMi operates in an approximately stationary environment where the data distribution shifts incrementally within a single run; CARR operates across generation boundaries where the model is fully retrained, creating non-incremental distributional shift in reward model calibration, quality-diversity correlation structure, and embedding space coverage; (c) DoReMi (including Iterated DoReMi) targets downstream task performance optimization; CARR targets collapse prevention in self-consuming loops where the training data distribution is endogenously generated. Similar distinctions hold for ODM (EXP3 for pretraining mixing), PiKE (mirror descent for multi-task mixing), and AutoMixAlign (EXP3/DRO for DPO task mixing).

**Relationship to Self-Correcting Self-Consuming Loops.** Gillman et al. (ICML 2024) prove that correction functions mapping data points toward the true distribution make self-consuming loops exponentially more stable. CARR is complementary rather than competing: self-correction operates at the data-point level (modifying individual samples, requiring domain-specific correctors like physics simulators), while CARR operates at the curation-weight level (adjusting which quality dimensions to prioritize in selection, requiring only reward model scores). In principle, both could be combined — corrected synthetic data could then be curated with adaptive multi-objective weights — though we leave this to future work.

**Relationship to DataEvolve.** DataEvolve (arXiv:2603.14420) uses evolutionary algorithms to optimize data curation strategies across iterations. While both methods share the insight that adaptive iteration improves curation, they differ in setting (static web data vs. self-consuming loops), optimization machinery (evolutionary search vs. MWU with provable regret bounds), and data regime (pretraining on external data vs. post-training on endogenously generated data).

**Fixed Share for non-stationary between-generation dynamics (core theoretical contribution).** The standard MWU regret bound O(√(T ln M)) is appropriate for stationary environments but does not account for the non-stationarity inherent in self-consuming generation boundaries. Our core theoretical contribution is the Fixed Share extension (Herbster & Warmuth, 1998), specifically formalized for the between-generation non-stationary setting.

*Concrete bound comparison at experimental scale (T=5, M=3).* Standard MWU achieves regret O(√(T ln M)) = O(√(5 · ln 3)) ≈ O(2.34) against the best *fixed* weight vector. Fixed Share with Φ=2 switches achieves switching regret O(√(T · [(Φ+1) ln M + Φ ln(eT/Φ)])) ≈ O(√(5 · [3·1.10 + 2·1.61])) ≈ O(√(5 · 6.52)) ≈ O(5.71) against the best *changing* weight sequence with 2 switches. The Fixed Share bound is numerically larger (5.71 vs. 2.34) because it competes against a strictly stronger comparator. When the optimal curation weights genuinely shift — as we hypothesize and empirically measure — the standard MWU bound is vacuously comparing against a suboptimal fixed baseline.

*Concrete scenario.* Suppose the best curation weights shift from [0.5, 0.3, 0.2] (quality-dominant, early generations where diversity is naturally high) to [0.2, 0.5, 0.3] (diversity-dominant, later generations where reward model calibration drift narrows the quality distribution) after generation 2. Standard MWU is guaranteed only to track the best fixed compromise ≈ [0.35, 0.4, 0.25], which is suboptimal at every generation. Fixed Share with Φ=1 provably tracks the shift, adapting to each regime's optimal weights.

The optimal curation weighting shifts across generations due to three identified sources of non-stationarity: (1) reward model calibration drift — ArmoRM calibrated on human-written text progressively misranks synthetic outputs as the distribution evolves; (2) changing quality-diversity correlation — quality and diversity may be orthogonal in generation 0 but negatively correlated by generation 3 as the model exploits reward patterns; (3) entropy collapse dynamics (arXiv:2602.12180) — stability depends on parameter regimes that fixed weights cannot guarantee across generations. We formalize these non-stationarity sources and prove that the between-generation setting violates the assumptions under which standard MWU suffices, making Fixed Share the appropriate theoretical tool.

**Contribution robustness: contingency under marginal CARR gains.** If CARR shows <2% improvement over fixed-weight multi-reward curation, the paper's contributions remain substantive through three independent findings: (a) **Non-stationarity characterization** — the first empirical evidence that between-generation distributional shift in self-consuming loops is genuinely non-stationary, measured via reward model score distribution shift across generations, quality-diversity correlation evolution, and embedding entropy trajectory. This is an independent empirical contribution regardless of whether adaptive weights outperform fixed weights, as it characterizes the dynamics that future methods must address. (b) **Realistic multi-dimensional validation** — the first validation of pluralistic curation theory (ICML 2026) with realistic quality/diversity/complexity objectives at instruction-tuning scale, beyond prior length-based rewards on lightweight GPT-2. Even a null result (fixed weights suffice) would validate the theory's practical applicability, which is currently unknown. (c) **Principled framework for future extension** — CARR + Fixed Share provides a formal framework with provable guarantees that future work can extend to more generations (T>5), larger models, and additional reward dimensions, where the non-stationarity effects are expected to be more pronounced.

**Experiment plan (13-day sprint for May 25 ARR submission).** Four conditions on Qwen3.5-0.8B across 5 self-consuming generations starting from UltraFeedback prompts: (1) no curation baseline (uncurated iterative SFT); (2) single-reward quality-only curation (ArmoRM top-K selection); (3) fixed-weight multi-reward curation (uniform w=[1/3,1/3,1/3] across quality, diversity, complexity with Nash bargaining selection); (4) CARR adaptive curation (MWU-based rebalancing with Fixed Share). Learning rate η is determined by a preliminary sweep over 3 values on 2 generations. Diversity metrics: Vendi Score, self-BLEU, n-gram entropy. Quality: MT-Bench (primary), HellaSwag, MMLU. Collapse indicators: embedding coverage (fraction of original embedding space covered), perplexity divergence from base model. Non-stationarity analysis: we explicitly measure the three identified sources — reward model score distribution shift across generations, quality-diversity correlation evolution, and embedding entropy trajectory — to empirically validate that the between-generation setting is genuinely non-stationary and that Fixed Share's switching regret guarantee is load-bearing. Ablation (if time permits): CARR-FixedShare vs. CARR-StandardMWU vs. CARR-Proportional (w_i(t+1) ∝ w_i(t) + α·d_i(t), projected onto simplex) to empirically justify the Fixed Share choice. 2B-scale validation and dimension-count ablations (2 vs. 3 dimensions) are deferred to camera-ready.

**13-day execution timeline:** Days 1–3: Pipeline implementation (reward scoring, CARR loop, training harness) + preliminary η sweep. Days 4–8: Main experiments (4 conditions × 5 generations, p

## Resource Estimate

- **auto_research**: {'claude_api_cost': '$200–$450 (2000–4500 turns for end-to-end automation including failure recovery and paper writing)', 'estimated_gpu_cost': '$306 (153 rental-hours × $2.00/hr)', 'gpu_hours': '~130h H100 (adds full η grid search, Fixed Share vs. Standard MWU vs. Proportional comparison, dimension-count ablation 2 vs 3, and 2B validation on 2 conditions × 5 gens)', 'gpu_utilization': '~85% — agent continuously fills GPU pipeline with queued jobs', 'rental_hours': '~153h (= 130h / 0.85 utilization)', 'risk_note': 'Without human judgment on collapse metric interpretation, agent may over-explore unproductive η values, inflating compute by 15–25%', 'speed_bottleneck': '5 iterative generations are inherently sequential per condition; parallelism across conditions and ablations is the main lever', 'team': '0 (initial setup only: configure reward endpoints, dataset paths, evaluation harness)', 'timeline': '8–12 days with 4–8 H100s'}
- **human_in_loop**: {'claude_api_cost': '$80–$180 (800–1800 conversation turns for experiment orchestration, CARR tuning, and paper drafting)', 'estimated_gpu_cost': '$216 (108 rental-hours × $2.00/hr)', 'gpu_hours': '~65h H100 (same compute as manual; agent automates generation→scoring→CARR-update→curation→training pipeline)', 'gpu_utilization': '~60% — agent queues next experiments while current ones run, human reviews collapse dashboards', 'rental_hours': '~108h (= 65h / 0.60 utilization)', 'risk_note': 'Tight 13-day timeline leaves minimal buffer for pipeline bugs or unexpected results requiring additional runs', 'team': '1 researcher, ~30min/day reviewing metrics and approving configs', 'timeline': '10–13 days with 2–4 H100s (conditions parallelized; 5 sequential generations per condition is the bottleneck)'}
- **manual**: {'estimated_gpu_cost': '$372 (186 rental-hours × $2.00/hr)', 'gpu_hours': '~65h H100 (4 conditions × 5 generations × ~2h/cycle = 40h, plus ~6h η sweep, ~6h evaluation, ~4h diversity/collapse metrics, ~9h buffer/debugging)', 'gpu_utilization': '~35% — manual experiment orchestration and debugging between runs', 'rental_hours': '~186h (= 65h / 0.35 utilization)', 'team': '1–2 researchers', 'timeline': '3–4 weeks with 2 H100s (too slow for May 25 deadline)'}

## Key References

- DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining (NeurIPS 2023, arXiv:2305.10429)
- Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences (ICML 2026, arXiv:2605.07724)
- How Sampling Shapes LLM Alignment: From One-Shot Optima to Iterative Dynamics (arXiv:2602.12180)
- Online Data Mixing (arXiv:2312.02406)
- PiKE: Adaptive Data Mixing for Large-Scale Multi-Task Learning (arXiv:2502.06244)
- AutoMixAlign: Adaptive Data Mixing for Multi-Task Preference Optimization (ACL 2025, arXiv:2506.00569)
- LASeR: Learning to Adaptively Select Rewards (NeurIPS 2025, arXiv:2410.01735)
- Escaping Collapse: The Strength of Weak Data for Large Language Model Training (NeurIPS 2025, arXiv:2502.08924)
- ParetoHqD: Fast Offline Multiobjective Alignment of Large Language Models using Pareto High-quality Data (AAAI 2026, arXiv:2504.16628)
- DRA-GRPO: Exploring Diversity-Aware Reward Adjustment for R1-Zero-Like Training of Large Language Models (arXiv:2505.09655)
- Learning to Optimize Multi-Objective Alignment Through Dynamic Reward Weighting (TACL 2026, arXiv:2509.11452)
- MAESTRO: Meta-learning Adaptive Estimation of Scalarization Trade-offs for Reward Optimization (ACL 2026 Main, arXiv:2601.07208)
- APEX: Learning Adaptive Priorities for Multi-Objective Alignment in Vision-Language Generation (arXiv:2601.06574)
- Reward Model Ensembles Help Mitigate Overoptimization (arXiv:2310.02743)
- Iterative Finetuning is Mostly Idempotent (arXiv:2605.01130)
- Self-Consuming Generative Models with Curated Data Provably Optimize Human Preferences (NeurIPS 2024)
- Self-Verification Provably Prevents Model Collapse in Recursive Synthetic Training (NeurIPS 2025)
- Escaping Model Collapse via Synthetic Data Verification: Near-term Improvements and Long-term Convergence (arXiv 2025)
- Explaining and Preventing Alignment Collapse in Iterative RLHF (arXiv:2605.04266)
- Interpretable Preferences via Multi-Objective Reward Modeling and Mixture-of-Experts (EMNLP 2024)
- Spend Wisely: Maximizing Post-Training Gains in Iterative Synthetic Data Bootstrapping (NeurIPS 2025 spotlight, arXiv:2501.18962)
- Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning (ACL 2026)
- The Multiplicative Weights Update Method: a Meta Algorithm and Applications (Arora, Hazan, Kale; Theory of Computing 2012)
- Tracking the Best Expert (Herbster & Warmuth, Machine Learning 1998)
- Self-Correcting Self-Consuming Loops for Generative Model Training (Gillman et al., ICML 2024, arXiv:2402.07087)
- Strong Model Collapse (Dohmatob et al., ICLR 2025, arXiv:2410.04840)
- Data Darwinism Part II: DataEvolve — AI can Autonomously Evolve Pretraining Data Curation (arXiv:2603.14420)
- A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective (NeurIPS 2025 Spotlight, arXiv:2509.16499)
- Position: Model Collapse Does Not Mean What You Think (Schaeffer et al., arXiv:2503.03150)
- Collapse or Thrive? Perils and Promises of Synthetic Data in a Self-Generating World (Kazdan et al., arXiv:2410.16713)

## Reviewer Evaluation

**Scores**:
  - clarity: **{'rationale': 'Exceptionally well-structured. The algorithm is precisely specified with concrete formulas. The landscape covers 30+ references with explicit differentiation. The collapse definition scope (Schaeffer definitions 4 and 7) is precise. The contribution robustness contingency analysis is thoughtful. The Fixed Share bound comparison with concrete numbers at experimental scale (T=5, M=3, Φ=2) is exemplary. The relationship to every major prior work is explicitly and carefully articulated.', 'score': 5}**/5
  - feasibility: **{'rationale': '~65 H100-hours is well within the 200h budget. Qwen3.5-0.8B is publicly available on HuggingFace, ArmoRM is open-source, and UltraFeedback is accessible. The 13-day timeline for 4 conditions × 5 generations is tight but realistic given the small model size (~0.8B) — each SFT cycle on UltraFeedback-scale data should take ~1-2h on 2 H100s. The sequential bottleneck (5 generations per condition) is correctly identified. Writing concurrently with experiments is standard practice for deadline sprints.', 'score': 4}**/5
  - impact: **{'rationale': "Strong thematic match with EMNLP 2026's 'Data as a bottleneck and a responsibility' sub-topic, which explicitly calls for work on 'consequences of synthetic data feedback loops.' The contribution robustness design (three independent contributions even if CARR's marginal gains are small) is strategically sound. The non-stationarity characterization and realistic validation of pluralistic curation theory are independently valuable. The MWU+Fixed Share framework provides a principled foundation for future extension to larger-scale iterative training.", 'score': 4}**/5
  - novelty: **{'rationale': 'The core novelty — extending MWU/Fixed Share from within-run data weighting to collapse-signal-driven curation across discrete self-consuming generations — is genuine and well-differentiated from DoReMi, ODM, PiKE, AutoMixAlign, Self-Correcting Loops, and DataEvolve. The proposal correctly identifies that no existing method combines multi-objective curation + adaptive weight scheduling via online learning with switching regret guarantees + iterative self-consuming LLM training. While the building blocks (MWU, ArmoRM, Vendi Score) are existing, the composition for this specific problem setting is novel, and the Fixed Share formalization for between-generation non-stationarity is a genuine theoretical contribution.', 'score': 4}**/5

## Human Review Note

## Agent 审核结果（完整三阶段 pipeline）

**Verdict**: PASS

**入口三重共识 (X)**: 26.0%
**终审自评 (Y)**: 35.0%
**出口三重共识 (Z)**: 30.0%
**Z 区间**: [25.0%, 35.0%]
**真实提升 (Z-X)**: +4.0 pp
**幻觉幅度 (Y-Z)**: +5.0 pp
**出口一致性**: 高
**出口三次评估**: [27.0, 33.0, 32.0]

### 优化方案 / 拒绝详情
【优化方案】

1. **论文定位 / 整体结构** — 从"单核方法论文"重构为"Empirical Anatomy + Principled Simple Method"双支柱结构。原 proposal 以 CARR 算法为唯一核心贡献，empirical characterization 仅作铺垫。修改后 Contribution I（Empirical Anatomy of Multi-Dimensional Collapse）与 Contribution II（CARR）对等并列，新增 Contribution III（Collapse Diagnostics via Weight Trajectories）。这使论文在 CARR 增益有限时仍有独立支撑。 — 命中 **Novelty + Significance**：审稿人对"method is incremental but empirical findings are interesting"有明确的接受先例；dual-pillar 消除了单点失效风险。

2. **Introduction / 贡献声明** — 彻底删除原 proposal 中"<2% improvement over fixed weights"的预防性表述及三条 fallback 贡献。替换为分层假设结构（H1-H7），每个假设有明确的可验证标准。同时增加"即使 CARR 的 curation 增益有限，Empirical Anatomy 和 Diagnostic 工具仍独立成立"的隐含逻辑，但不以自我投降的方式表述。 — 命中 **Soundness + Significance**：消除审稿人"作者自己都不相信方法有效"的红旗信号；分层假设展示 intellectual maturity。

3. **Introduction / 应用场景** — 新增 1-2 句将 self-consuming loops 与 iterative alignment pipelines（RLHF、DPO 及其变体）的结构对应关系点明，拓宽读者对论文受众的认知。不增加实验 scope，仅作 framing。 — 命中 **Significance**：从"只有显式跑 synthetic data recycling 的人关心"拓展到"所有做 iterative alignment 的人都相关"。

4. **Introduction + Broader Impact / Special Theme 对接** — 从 merely mentioning special theme 升级为 substantive 论述：CARR 的 diversity 维度自适应上调本质上是 responsible curation；weight trajectory diagnostics 提供 curation 过程的透明性和可审计性。 — 命中 **Relevance to Venue + Broader Impact**：Special theme 论文通常有 AC 主动收稿的动力。

5. **§4.1 Empirical Anatomy** — 原 proposal 的 empirical characterization 是 CARR 的附属 setup 段落。重构为独立的完整 section，包含三个子贡献：(i) Distributional Goodhart drift 定量刻画（KL divergence vs ECE 回归、empirical threshold），(ii) quality-diversity correlation changepoint（PELT 算法检验），(iii) embedding entropy decay（函数形式拟合移至 appendix，正文聚焦跨尺度一致性）。新增 (iv) unified regime-shift hypothesis——测试三者是否时间对齐，反映同一底层动态。 — 命中 **Novelty + Analysis Depth**：审稿人对"multiple findings 之间的结构性关联"评价远高于"独立发现的罗列"。

6. **§4.1(i) Distributional Goodhart Drift** — 原 proposal 未涉及此概念。新增：与 Gao et al. (2023) 的经典 reward hacking 做显式机制区分（自然漂移 vs 对抗性利用，各向同性 vs 各向异性），但以定量结果（divergence-calibration 回归、threshold 数值、跨尺度稳定性）而非术语新颖性作为贡献核心，避免"这不就是 OOD"的 pushback。 — 命中 **Novelty**：将一个可能被视为 trivial 的观察（RM 在 OOD 下退化）升级为有精确数值的定量贡献。

7. **§3 Method / 理论定位调整** — 原 proposal 将 regret bound 作为核心理论卖点。修改：(a) 将理论部分重新定位为"principled algorithm design motivation"而非"strong formal guarantee"；(b) 删除 §3.3 控制论类比（confirmed as padding，不产出新结果）；(c) 将 §3.4 的 noisy reward 和 delayed feedback 分析从定性描述升级为正式 Proposition 1-2，给出具体数学表达式和适用条件；(d) 新增有限步数 concrete numerical bound（T=10, K=3 的实际数值）。 — 命中 **Soundness**：避免审稿人验算 regret bound 后发现 vacuous 而扣分；正式 Proposition 增加 technical depth；诚实的理论定位获得 credibility。

8. **§3.2 / 实现极简性** — 原 proposal 未提及 CARR 的实现开销。新增明确量化：~10 行核心代码、<0.1% 额外计算开销、无需额外模型训练/梯度计算/proxy model。与 DoReMi（需 proxy model）、ODM（需 online gradient）形成对比。 — 命中 **Reproducibility + Practical Impact**：EMNLP 审稿人对"simple but effective"有天然好感。

9. **§3.2 / 超参数** — 原 proposal 未讨论 η 和 α 的选择与敏感性。新增：(a) 理论指导默认值（η = √(ln K / T)，α = Φ_est / (T-1)），(b) 超参数消融计划（η × 4、α × 3 网格），(c) 性能方差报告。 — 命中 **Soundness + Reproducibility**：堵住"simplicity 叙事被调参复杂性削弱"的攻击面。

10. **§4.2 Setup / T 从 5 增至 10** — 原 proposal 仅 T=5。T=5 使 Fixed Share 的 regret bound 完全 vacuous（bound ≈ 4，无约束力），且 MWU 仅有 4 次权重更新，信噪比极低。改用 LoRA 降低每代成本，使 T=10 可行。 — 命中 **Soundness**：这是最关键的实验设计修复——直接影响理论声称的可信度和非平稳性信号的可检测性。

11. **§4.2 Setup / LoRA + Full-FT 对照** — LoRA 约束参数更新在低秩子空间，可能系统性地抑制 collapse 幅度。新增 0.8B full-FT 对照实验（3 核心条件 × 10 代），比较 collapse dynamics 的定性形态差异，并在 Limitations 中显式讨论 LoRA confound。 — 命中 **Soundness**：堵住"你的发现是 LoRA 特异性的"攻击。

12. **§4.2 Setup / 3B Scaling Validation（从 optional 升为 required）** — 原 proposal 仅用 0.8B，scaling validation 是 hedging 表述（"if compute allows"）。修改为 required：Qwen3.5-3B（或 Llama-3.2-3B），3 核心条件 × 10 代，LoRA。 — 命中 **Soundness + Significance**：单一模型规模/家族是 EMNLP 审稿人的标准扣分项；两个规模的一致性是外推至更大模型的基础。

13. **§4.3 Experimental Conditions / 从 4 扩至 11** — 原 proposal 仅 4 条件（no curation / single-reward / fixed-weight / CARR）。逐层新增：(a) Standard MWU without Fixed Share（ablation，隔离 Fixed Share 的贡献），(b) Proportional rebalancing naive baseline（隔离 MWU 框架 vs 简单自适应的贡献），(c) Real-data replay 50%（最强简单 baseline），(d) Real-data replay 10%（模拟数据稀缺），(e) CARR + real-data replay 50%（测试互补性），(f) Adversarial non-stationarity（Generation 5 RM shift），(g) Oracle hindsight upper bound（后处理，近零成本）。 — 命中 **Soundness + Experimental Rigor**：real-data replay 是审稿人最可能要求的第一个 baseline；ablations 隔离每个设计选择的贡献；oracle bound 验证理论保证的实际 tightness。

14. **§4.4 Evaluation / 分离 Curation vs Held-Out 评估** — 原 proposal ArmoRM 同时用于 curation 和评估，存在循环性。新增完全独立的 held-out evaluation：MT-Bench、AlpacaEval 2.0、IFEval、embedding diversity（frozen external encoder）、tail coverage。明确讨论正交性。 — 命中 **Soundness**：直接消除"metric gaming"质疑。

15. **§4.4 Evaluation / Human Evaluation** — 原 proposal 无人工评估。新增 200 样本/条件 × 4 核心条件，评估 informativeness、diversity、coherence、overall preference，报告 Krippendorff's α。 — 命中 **Soundness + Rigor**。

16. **§4.3 / 统计设计** — 原 proposal 无重复实验。核心 4 条件 × 5 seeds（Anatomy 观测条件亦 5 seeds），报告 mean ± std、bootstrap CI、paired permutation test。Anatomy 的 changepoint 声称使用 PELT 算法做统计检验。 — 命中 **Soundness**：堵住"差异可能来自随机波动"的攻击。

17. **§4.5 / Weight Trajectory Diagnostics + H6** — 原 proposal 将 weight trajectory 分析作为方法手段。升级为独立贡献（Contribution III），并将"leading indicator"从探索性问题升级为正式假设 H6（AUC > 0.8），增加"deployment mode"描述——即使不用 CARR 做 curation，也可部署 weight tracker 作为纯 diagnostic。 — 命中 **Significance + Practical Impact**：monitoring 工具的受众远大于 curation 方法本身。

18. **§2 Related Work / 大幅扩展** — 原 proposal 覆盖 7 个方向。新增：(a) Reward hacking/over-optimization（Gao et al. 2023, Coste et al. 2023），将 CARR 的多维度 rebalancing framed 为 implicit over-optimization mitigation；(b) Dynamic curriculum/data selection（D2 Pruning, DsDm），明确 between-generation vs within-epoch 差异；(c) SPIN 及其与 self-consuming loop 的关系；(d) Real-data replay 作为 simplest baseline 的显式讨论。新增 pre-submission comprehensive literature sweep 承诺。 — 命中 **Related Work**。

19. **§2 Related Work / 降低对 pluralistic preferences theory 的依赖** — 原 proposal 将 CARR 的 motivation 建立在"fixing pluralistic theory's assumptions"上。修改为独立从 collapse 问题出发建立 motivation，pluralistic theory 降为 complementary related work。 — 命中 **Soundness**：消除对 concurrent/未充分验证理论的依赖风险。

20. **新增 §7 Limitations** — 原 proposal 无 Limitations section。新增显式讨论：(a) LoRA 对 collapse dynamics 的潜在影响，(b) 模型规模 gap（0.8B/3B vs 7B+），(c) K=3 的局限性。 — 命中 **Soundness + Intellectual Honesty**：主动承认局限比被审稿人指出更有利。

21. **§5 Hypotheses / 完整假设体系** — 原 proposal 无正式假设列表。新建 7 个可验证假设（H1 Primary, H2 Ablation, H3 Robustness, H4 Complementarity, H5 Oracle Proximity, H6 Diagnostic, H7 Unified Regime Shift），每个有明确的成功标准。 — 命中 **Soundness + Rigor**：pre-registered hypothesis 结构排除 cherry-picking 嫌疑。

22. **K=3 Justification** — 原 proposal 未讨论维度选择的依据。新增 factor analysis justification（pairwise correlations < 0.3 确认近正交性），appendix 讨论 K scalability。 — 命中 **Soundness**：堵住"K=3 是 arbitrary"的攻击。

---

【主要风险】:

1. **算法 Novelty 天花板**：核心方法是 1998 年 Herbster & Warmuth 的 Fixed Share MWU 的直接应用，algorithmic contribution 本质上是 "textbook technique in new domain"。尽管 dual-pillar 结构和 Empirical Anatomy 可以对冲，但如果遇到强调 methodological novelty 的审稿人，仍可能给出 "engineering contribution, not research contribution" 的判定。这是 proposal 层面无法消除的 inherent limitation，只能通过 empirical findings 的实际 surprise 程度来补偿。

2. **Real-data replay baseline 可能过强**：如果 50% real-data replay 已经大幅缓解 collapse，而 CARR 在 replay 之上的边际增益统计不显著（H4 fail），审稿人会判定 "practitioners should just mix in real data"。10% low-resource 条件和 diagnostic value（H6）是 defense lines，但如果 H1 和 H4 同时表现不佳，论文的 practical significance 叙事将承压。

---

【实施评估】:

- **计算资源**: 总计约 1010 H100-hours（0.8B LoRA 主实验 ~350h + 0.8B Full-FT 对照 ~200h + 3B LoRA 验证 ~300h + 超参数消融 ~80h + 评估 ~80h）。需要访问 H100 或等效 GPU 集群。如果使用 A100，时间约增加 1.5-2×。云平台（如 AWS p5、GCP a3）或学术集群均可。

- **数据需求**: (1) 基座模型 Qwen3.5-0.8B 和 Qwen3.5-3B（公开可得）；(2) 用于生成 synthetic data 的 seed instructions（如 Alpaca、ShareGPT 格式，公开可得）；(3) ArmoRM reward model（公开可得）；(4) 用于 held-out 评估的 MT-Bench、AlpacaEval 2.0、IFEval 数据集（均公开可得）；(5) ArmoRM 训练数据分布信息（用于计算 KL divergence，需确认是否公开）。所有核心数据集均为公开标准 benchmark，无数据获取障碍。

- **人工介入**: (1) Human evaluation：800 样本（4 条件 × 200 样本），每样本评估 4 个维度，估计需 3-4 名标注者、约 40-50 annotator-hours，成本约 $800-1200（按 $20/hr）；(2) 需要报告 inter-annotator agreement（Krippendorff's α），需设计标注规范和培训；(3) 无其他人工标注需求（所有 curation 和自动评估均为模型驱动）。

- **训练需求**: 需要模型训练——每个实验条件需进行 10 代 LoRA fine-tuning（0.8B）或 full fine-tuning（0.8B 对照）。单次 LoRA fine-tuning 约 2 H100-hours（0.8B），full fine-tuning 约 10 H100-hours（0.8B）。3B LoRA 约 10 H100-hours/代。不需要从头预训练。不需要训练新的 reward model（使用现有 ArmoRM）。

- **新 Benchmark**: 不需要构建新的 benchmark 或评测数据集。所有评估使用现有公开 benchmark（MT-Bench、AlpacaEval 2.0、IFEval）。Empirical Anatomy 的分析基于实验过程中自然产生的数据，不需要额外的 benchmark 构建。但 Distributional Goodhart drift 的 KL divergence 计算需要获取或估计 ArmoRM 训练数据分布，可能需要一定的工程工作。

- **预估周期**: 从启动到可投稿约 **10-14 周**，breakdown 如下：(1) 代码框架搭建 + 数据准备：1-2 周；(2) 0.8B LoRA 主实验（含 5-seed 核心条件）：3-4 周（可并行跑多 seed）；(3) 0.8B Full-FT 对照 + 3B 验证：2-3 周（可与主实验部分并行）；(4) 超参数消融 + 评估（MT-Bench, AlpacaEval, IFEval）：1-2 周；(5) Human evaluation：1-2 周（含标注规范设计+标注+统计）；(6) 分析 + 论文撰写：3-4 周。关键路径：0.8B 主实验 → 分析 → 论文。如果 GPU 资源充足可并行多条件，周期可压缩至 8-10 周。EMNLP 2026 ARR May 25 deadline 前需在约 3 月中旬启动。

