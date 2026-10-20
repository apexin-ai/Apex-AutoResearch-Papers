# Research conversation: You are a senior ML research advisor synthesizing a literature review into an actionable research strategy. **Today's da

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/16d354d1-0aea-44ae-a93e-7ed499be64b1.jsonl`
- **Structured JSON:** [`4ea7009cb9f012e7c266.json`](../../sessions/4e/4ea7009cb9f012e7c266.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T05:34:07.299Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T05:34:07.299Z",
  "sessionId": "16d354d1-0aea-44ae-a93e-7ed499be64b1",
  "content": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.\n\n**Today's date: 2026-05-29 (UTC).**\n\n## Research area: Target: AAAI 2026\nTrack: Machine Learning (ML) — Efficient Inference and Reasoning\n\nDirection: Per-instance adaptive co-optimization of generation and verification compute, where both the number of generated solutions (K) and the verification depth (none/ORM/PRM/GenRM) are jointly selected based on online difficulty estimation from early reasoning tokens. Extends static aggregate scaling laws (Singhi et al.) to instance-adaptive, multi-depth allocation with a practical online algorithm.\n\nSeed Papers:\n- Singhi et al., \"When To Solve, When To Verify\" (arXiv 2025) — establishes aggregate scaling laws for generation-verification tradeoff; our work must explicitly extend this to per-instance, multi-depth allocation\n- Setlur et al., \"Scaling TTC Without Verification is Suboptimal\" (arXiv Feb 2025) — proves verification is essential and the gap grows with compute; motivates why verification budget allocation matters\n- Chen et al., \"VG-Search: Rethinking Optimal Verification Granularity\" (arXiv May 2025) — shows verification granularity matters for efficiency; we extend from granularity to depth and per-instance adaptation\n- Wang et al., \"ST-BoN\" (NeurIPS 2025 Spotlight) — early pruning via sampling consistency; a strong baseline for lightweight verification allocation\n\nKnown Gaps:\n- No method selects verification depth (none/ORM/PRM/GenRM) per-instance based on estimated difficulty; all existing work uses a fixed verification strategy across problems\n- Singhi et al.'s scaling laws are static and aggregate (one ratio for all problems); no online algorithm adapts the generation-verification split per-instance during inference\n- No framework jointly optimizes K (number of solutions) and d (verification depth) as coupled decision variables under a shared compute budget\n\nTheoretical Anchor: The bilinear structure of the joint optimization — P(correct) depends on coverage (increasing in K) and selection precision (increasing in d), while cost is c_g*K + c_v(d)*K = K*(c_g + c_v(d)) — admits a clean decomposition: for fixed d, optimal K = B/(c_g + c_v(d)), reducing the problem to selecting d* that maximizes selection precision per unit verification cost. This decomposition enables tractable optimization with provable approximation guarantees under mild assumptions on verifier accuracy monotonicity.\n\nConstraints:\n- Compute: ≤200 H100-hours\n- Must evaluate on ≥4 benchmarks across ≥2 domains (math, code, science)\n- Must compare against Singhi et al.'s aggregate-optimal baseline and fixed-depth baselines\n\nQuality Self-Checks:\n- [x] Core insight: The optimal verification depth varies dramatically per problem — easy problems need no verification while hard problems benefit from expensive generative verification — and this variance is predictable from early tokens.\n- [x] Why not obvious: Singhi et al. showed the aggregate optimal ratio, but the per-instance variance and multi-depth selection weren't explored because their framework only compared two verification strategies (GenRM vs SC), not a continuum of depths.\n- [ ] Baseline fear test: A simple heuristic (e.g., always use PRM for problems longer than X tokens) could capture much of the benefit — must demonstrate learned allocation significantly outperforms simple rules. This is a REAL RISK.\n- [x] Information exploited: Early-token difficulty signals (entropy trajectory, hesitation markers from Zhou et al.) that are available before verification decisions must be made.\n\nAvoid:\n- Framing as 'first to study generation-verification tradeoff' — Singhi et al. already did this; frame as extending to per-instance multi-depth allocation\n- Math-only evaluation — must include code and science benchmarks\n- Pure scaling law contribution — must provide a practical online algorithm, not just power-law fits\n- Ignoring the baseline fear: if a simple threshold on problem length achieves 80% of the adaptive allocation's gain, the paper is dead\n\n## Paper analyses (20 papers)\n\n[\n  {\n    \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\",\n    \"venue\": \"ICLR 2025 (Oral)\",\n    \"problem_identification\": \"Prior work scaled test-time compute uniformly across prompts. Snell et al. identified that the effectiveness of different test-time strategies (search vs. revision) varies dramatically by prompt difficulty, making uniform allocation wasteful.\",\n    \"key_insight\": \"Per-prompt compute-optimal allocation—selecting between PRM-guided search and sequential revision based on estimated difficulty—achieves 4× the efficiency of uniform best-of-N, because easy problems benefit from revision while hard problems need parallel search.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"They formalize test-time scaling as selecting strategy θ* per prompt to maximize P(correct) under budget N. Two mechanisms are studied: (1) PRM-guided search (best-of-N weighted, beam search, lookahead search) and (2) sequential revision chains with hierarchical verifier selection. Difficulty is operationalized via binned pass@1 rates (oracle) or averaged PRM scores (practical), and strategy selection uses two-fold cross-validation across five difficulty bins. Key finding: the optimal sequential-to-parallel ratio shifts systematically with difficulty.\",\n    \"limitations_and_open_questions\": \"Difficulty estimation cost is not fully accounted in compute budgets (requires sampling to estimate PRM scores). Only two strategy families (search vs. revision) are compared—no multi-depth verification hierarchy. Relies on PaLM 2 ecosystem with no open replication.\",\n    \"building_blocks\": [\n      \"Per-prompt difficulty binning via PRM scores\",\n      \"PRM-guided beam/lookahead search\",\n      \"Sequential revision chains with verifier reranking\",\n      \"Compute-optimal strategy selection via cross-validation\"\n    ],\n    \"relevance_to_seed\": \"Direct conceptual ancestor: proves per-prompt adaptive allocation works for test-time compute, but only considers two strategy types—our work extends to a continuum of verification depths (none/ORM/PRM/GenRM) as coupled decision variables with K.\"\n  },\n  {\n    \"title\": \"Sampling-Efficient Test-Time Scaling: Self-Estimating the Best-of-N Sampling in Early Decoding\",\n    \"venue\": \"NeurIPS 2025 (Spotlight)\",\n    \"problem_identification\": \"Full best-of-N sampling generates N complete solutions consuming O(N×T) GPU memory, then applies a reward model adding further overhead. The authors observed that internal representations at early decoding steps already contain signal to identify the most promising sample.\",\n    \"key_insight\": \"Chain-of-Embedding (CoE) curvature across layers at early tokens predicts solution quality via peer consistency—samples whose latent trajectories align most closely with the majority tend to be correct—enabling truncation of N-1 paths after only ~c tokens.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"ST-BoN extracts hidden states across all L layers at the earliest divergence point c, forming a Chain-of-Embedding H = h₀→h₁→...→h_L. A curvature-based feature metric F(H) scores each sample by distance to peers. Over a buffer window of τ steps, majority voting across timestep-wise rankings selects the best sample; remaining N-1 are truncated. Memory drops from O(N×T) to O(max(N×c, T)), yielding >80% GPU memory reduction and 50% latency reduction while matching full BoN accuracy.\",\n    \"limitations_and_open_questions\": \"Requires white-box access to hidden states (inapplicable to closed-source APIs). Buffer window length τ is fixed rather than adaptive to task complexity. CoE metric is validated empirically but lacks theoretical guarantees on when consistency implies correctness.\",\n    \"building_blocks\": [\n      \"Chain-of-Embedding (CoE) feature metric\",\n      \"Early-token consistency-based pruning\",\n      \"Majority voting across buffer window\",\n      \"Reward-model-free sample selection\"\n    ],\n    \"relevance_to_seed\": \"Strong baseline for lightweight verification allocation: ST-BoN's early-signal mechanism could serve as the 'none' or 'lightweight' tier in our verification depth hierarchy, and its CoE features may complement our difficulty estimation from early tokens.\"\n  },\n  {\n    \"title\": \"Scaling LLM Inference with Optimized Sample Compute Allocation\",\n    \"venue\": \"NAACL 2025\",\n    \"problem_identification\": \"Existing test-time scaling uses a single inference configuration (fixed model, temperature, prompt). Zhang et al. recognized that different problems favor different configurations, and the optimal strategy is a mixture—not a single best setting.\",\n    \"key_insight\": \"The pass@C objective under mixed configurations decomposes into a convex optimization (after relaxing integrality), enabling efficient hill-climbing to find optimal configuration mixtures that achieve 128× compute savings over the best pure strategy on code generation.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"They define inference configurations as d-tuples (model, temperature, language, prompt) and formulate allocation as: max_π (1/|D|)Σ_j(1-∏_i(1-p_ij)^π_i) subject to Σπ_i=C. The probability matrix P is estimated by sampling C₀ times per config-problem pair on training data. Convexity of the relaxed problem is proven via composition of exponentials over affine functions. Hill-climbing iteratively shifts one sample between configurations until no improving neighbor exists. Evaluated on HumanEval, MBPP, MATH, GSM8K, and SWE-Bench.\",\n    \"limitations_and_open_questions\": \"Optimization is offline (requires training-set estimation of P), so cannot adapt per-instance at inference time. Configuration space is pre-discretized. Assumes independent sampling which ignores sequential refinement strategies. No verification depth dimension.\",\n    \"building_blocks\": [\n      \"Convex formulation of configuration mixture optimization\",\n      \"Hill-climbing allocation algorithm\",\n      \"Probability matrix estimation from training samples\",\n      \"Multi-model multi-temperature configuration space\"\n    ],\n    \"relevance_to_seed\": \"Closest existing work to our K-allocation component: OSCA optimizes how many samples per configuration but does so offline across a dataset—our work must do this per-instance and jointly with verification depth d, making the online difficulty estimation the key differentiator.\"\n  },\n  {\n    \"title\": \"DiffAdapt: Difficulty-Adaptive Reasoning for Token-Efficient LLM Inference\",\n    \"venue\": \"ICLR 2026\",\n    \"problem_identification\": \"Reasoning LLMs apply uniform-length reasoning traces regardless of problem difficulty, causing 'overthinking' on easy problems. Liu et al. discovered this by analyzing token entropy distributions across difficulty-stratified problem sets, revealing a U-shaped pattern.\",\n    \"key_insight\": \"A U-shaped entropy pattern (high on easy problems from unnecessary exploration, low on medium, high on hard from genuine uncertainty) is detectable from the LLM's final hidden state via a lightweight MLP probe, enabling pre-generation difficulty routing.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"A two-layer MLP probe is trained on final-layer hidden states (300 problems/level from DeepMath-103K, AdamW, 100 epochs) to classify Easy/Normal/Hard. Each class maps to a fixed strategy tuple (temperature, max_tokens multiplier, prompt style). Heuristic labels use correctness rate C(x) and mean entropy H̄(x) with model-specific thresholds. At inference, the probe routes each question to its strategy before generation begins. Achieves 22.4% token reduction with maintained or improved accuracy across 5 models and 8 benchmarks.\",\n    \"limitations_and_open_questions\": \"Only three discrete difficulty levels with heuristic thresholds—no continuous adaptation. Adapts reasoning length and temperature, not verification strategy. Probe trained on math (DeepMath-103K); cross-domain transfer unclear. The baseline fear applies: a simple token-length threshold may capture much of the gain.\",\n    \"building_blocks\": [\n      \"U-shaped entropy pattern as difficulty signal\",\n      \"Lightweight MLP probe on hidden states for difficulty classification\",\n      \"Pre-generation strategy routing\",\n      \"Heuristic difficulty labeling from correctness/entropy\"\n    ],\n    \"relevance_to_seed\": \"Closest concurrent work on per-instance difficulty adaptation, but operates on a different axis (reasoning length) than our verification depth. Their hidden-state probe and entropy-based difficulty characterization are directly reusable as features for our online difficulty estimator.\"\n  },\n  {\n    \"title\": \"Process Reward Models That Think\",\n    \"venue\": \"arXiv 2025 (ICLR 2026 withdrawn)\",\n    \"problem_identification\": \"Discriminative PRMs require massive step-level labels (PRM800K) and generalize poorly out-of-domain. LLM-as-Judge scales inconsistently with more compute. Khalifa et al. identified that framing verification as generation (long CoT) rather than classification bridges both gaps.\",\n    \"key_insight\": \"A generative process verifier that 'thinks' via long chain-of-thought, fine-tuned on only 1% of PRM800K labels, outperforms discriminative PRMs on in-domain tasks and surpasses them by 8% out-of-domain—because generation enables compositional reasoning about step correctness.\",\n    \"innovation_type\": \"simplification\",\n    \"method_summary\": \"ThinkPRM fine-tunes a base LLM to generate step-by-step verification reasoning (long CoT) for each solution step, producing a final correctness judgment. Training uses only 8K process labels or 1K synthetic examples. Verification compute scales by allowing longer thinking traces (up to ~24K tokens), with monotonically improving F1—unlike LLM-as-Judge which plateaus. Evaluated on ProcessBench, MATH-500, AIME'24 (in-domain) and GPQA-Diamond, LiveCodeBench (out-of-domain).\",\n    \"limitations_and_open_questions\": \"Long CoT verification is expensive per solution (up to 24K tokens), creating a compute-accuracy tradeoff that makes it unsuitable for all problems. Withdrawn from ICLR 2026—possibly due to concurrent work or scope concerns. No analysis of when generative verification is cost-effective vs. cheaper alternatives.\",\n    \"building_blocks\": [\n      \"Generative (long-CoT) process reward model\",\n      \"Data-efficient PRM training (<1% labels)\",\n      \"Scalable verification compute via thinking length\",\n      \"Out-of-domain generalization of generative verifiers\"\n    ],\n    \"relevance_to_seed\": \"Key evidence for our verification depth hierarchy: ThinkPRM demonstrates that generative verification (GenRM) achieves highest accuracy but at substantial cost, defining the expensive end of our none→ORM→PRM→GenRM depth spectrum and motivating per-instance selection of when this cost is justified.\"\n  },\n  {\n    \"title\": \"When To Solve, When To Verify: Compute-Optimal Problem Solving and Generative Verification for LLM Reasoning\",\n    \"venue\": \"COLM 2025\",\n    \"problem_identification\": \"No prior work compared SC vs GenRM under a unified compute budget accounting for verification token costs. By normalizing to FLOPs (C = S·(1 + λV)), they revealed GenRM's apparent superiority was an artifact of ignoring verification compute.\",\n    \"key_insight\": \"Under iso-compute comparison, Self-Consistency dominates GenRM for most practical budgets, with GenRM requiring 8× more compute to merely match SC—because solutions should scale 1.5–2× faster than verifications (S_opt ∝ C^0.57 vs V_opt ∝ C^0.39).\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"Derives power-law inference scaling laws by sweeping (S, V) combinations across models (Llama-3.1-8B, Qwen-2.5-7B, Llama-3.3-70B, QwQ-32B) and datasets (MATH, AIME, GPQA, LiveCodeBench). Fits S_opt and V_opt as functions of compute budget C, showing solutions scale faster. Crucially notes GenRM yields up to 30% relative improvement on hard problems, implicitly motivating per-instance allocation.\",\n    \"limitations_and_open_questions\": \"Analysis is aggregate-only (one ratio for all problems) and compares only SC vs GenRM binary, not a continuum of verification depths. The difficulty-dependent finding (GenRM better on hard problems) is acknowledged but not operationalized into an algorithm.\",\n    \"building_blocks\": [\n      \"Unified compute metric C(S,V) = S(1+λV)\",\n      \"Power-law scaling fits for S_opt/V_opt\",\n      \"Difficulty-stratified analysis showing GenRM advantage on hard problems\",\n      \"Multi-model multi-domain evaluation protocol\"\n    ],\n    \"relevance_to_seed\": \"Direct seed paper — our work extends their aggregate scaling laws to per-instance, multi-depth allocation by operationalizing their own finding that difficulty modulates the optimal generation-verification ratio.\"\n  },\n  {\n    \"title\": \"Generative Verifiers: Reward Modeling as Next-Token Prediction\",\n    \"venue\": \"ICLR 2025\",\n    \"problem_identification\": \"Discriminative reward models treat verification as classification, forfeiting LLM generative capabilities — they cannot perform chain-of-thought reasoning during verification or leverage test-time compute scaling via sampling.\",\n    \"key_insight\": \"Recasting verification as next-token prediction (predicting 'Yes'/'No' after optionally generating a CoT rationale) unifies generation and verification objectives, enabling CoT verification and majority-vote scaling at inference time.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Trains with a mixed loss L_GenRM = L_SFT(verify) + λ·L_SFT(generate), where verification uses synthetic CoT rationales generated via reference-guided grading. At inference, GenRM-CoT samples K rationales and averages p(Yes|rationale) for robust scoring. This enables a compute-accuracy tradeoff within verification itself (MajV@K).\",\n    \"limitations_and_open_questions\": \"Synthetic rationales require reference solutions during training (privileged information). The compute cost of CoT verification is substantial but not explicitly traded off against generating more solutions — exactly the gap Singhi et al. later exposed.\",\n    \"building_blocks\": [\n      \"GenRM verification scoring: r = p(Yes|x,y,rationale)\",\n      \"CoT verification rationale generation\",\n      \"MajV@K: majority voting over verification rationales\",\n      \"Unified generation-verification training loss\"\n    ],\n    \"relevance_to_seed\": \"Defines the GenRM verification depth level in our hierarchy; its MajV@K mechanism is a natural candidate for the highest-cost verification tier in our per-instance depth selection framework.\"\n  },\n  {\n    \"title\": \"Optimizing Test-Time Compute via Meta Reinforcement Fine-Tuning\",\n    \"venue\": \"ICML 2025\",\n    \"problem_identification\": \"Standard outcome-reward RL for test-time compute wastes tokens on unproductive reasoning because it only rewards final success, providing no signal for intermediate progress or efficient exploration within the token stream.\",\n    \"key_insight\": \"Test-time generation is structurally analogous to meta-RL: token-stream segments are 'episodes' whose cumulative regret should be minimized, and a dense 'progress' reward (change in success likelihood per episode) achieves this by balancing exploration and exploitation.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Segments output into episodes, defines progress as r_prg = P(correct|episodes_0:j) − P(correct|episodes_0:j−1), and trains with ℓ_MRT = outcome_reward + α·Σ(progress). A meta-prover μ estimates success probability by forcing early termination ('[time is up]&lt;/think>'). Two variants: STaR (filter+SFT on high-progress traces) and RL (on-policy with dense+outcome rewards).\",\n    \"limitations_and_open_questions\": \"The progress reward requires sampling multiple continuations per prefix during training, which is expensive. The framework optimizes within-model reasoning but does not consider external verification as a complementary compute allocation — it's purely about making the generator more efficient.\",\n    \"building_blocks\": [\n      \"Cumulative regret formalization for TTC\",\n      \"Progress reward: Δ_j = P(correct|prefix_j) - P(correct|prefix_{j-1})\",\n      \"Meta-prover via forced early termination\",\n      \"Episode-segmented token stream for RL\"\n    ],\n    \"relevance_to_seed\": \"The cumulative regret framework and progress metric could serve as the online difficulty estimator in our system — if early episodes show low progress, this signals a hard problem needing deeper verification, directly informing our (K, d) allocation.\"\n  },\n  {\n    \"title\": \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\",\n    \"venue\": \"AAAI 2026\",\n    \"problem_identification\": \"Existing PRMs are limited by scalar prediction (no generative reasoning), weak process supervision labels, and inability to scale test-time compute. These three gaps compound: discriminative PRMs cannot explain their judgments or improve with more inference budget.\",\n    \"key_insight\": \"A generative PRM that performs explicit CoT reasoning with code verification before step-level judgment can dramatically outperform discriminative PRMs (1.5B > GPT-4o) with minimal training data (23K samples), because generation enables both better reasoning and test-time compute scaling.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"Introduces Relative Progress Estimation (RPE) to label process supervision by comparing model confidence with/without each step (MC(s_t,a_t)/MC(s_t)). Synthesizes training rationales combining CoT reasoning and executable code verification. Trains GenPRM to generate reasoning+code before judging each step, enabling test-time scaling via sampling multiple verification chains.\",\n    \"limitations_and_open_questions\": \"Evaluated primarily on math (ProcessBench/MATH); generalization to code/science domains unclear. RPE quality depends on the base model's calibration. The compute cost of generative step-level verification is high — when this cost is worthwhile vs. simpler ORM remains unaddressed.\",\n    \"building_blocks\": [\n      \"RPE for automatic process supervision labels\",\n      \"CoT + code verification before step judgment\",\n      \"Generative PRM scaling via sampling\",\n      \"Critic model for policy refinement\"\n    ],\n    \"relevance_to_seed\": \"Provides a concrete high-depth verification option (PRM with CoT+code) in our framework. Its high accuracy but high cost makes it the ideal candidate for the 'hard problem' tier, while its 23K-sample efficiency suggests practical deployability.\"\n  },\n  {\n    \"title\": \"Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens\",\n    \"venue\": \"arXiv 2026\",\n    \"problem_identification\": \"Output length is widely used as a proxy for reasoning effort but correlates negatively with accuracy (r = −0.594). No mechanistically grounded metric existed to measure genuine inferential effort from internal model computations.\",\n    \"key_insight\": \"Deep-thinking tokens — where predictions undergo significant revision in deeper layers (measured by JSD between intermediate and final layer distributions exceeding a settling threshold) — provide a robust, positively correlated difficulty signal (r = 0.683) that enables efficient test-time scaling via early prefix-based filtering.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"Computes JSD(p_{t,L} || p_{t,l}) per token per layer, defines settling depth c_t = min{l: D̄_{t,l} ≤ 0.5}, classifies tokens with c_t ≥ 0.85·L as deep-thinking, and aggregates into Deep-Thinking Ratio (DTR). Think@n generates n samples, ranks by DTR from 50-token prefixes, selects top 50%, and applies majority voting — matching full self-consistency at 50% cost.\",\n    \"limitations_and_open_questions\": \"Requires access to intermediate layer activations (not available via API for proprietary models). The 50-token prefix and ρ=0.85 thresholds are empirically set — sensitivity analysis across architectures is limited. Correlation is shown but causal mechanism (why deep thinking → correctness) is not established.\",\n    \"building_blocks\": [\n      \"Deep-thinking ratio (DTR) as difficulty signal\",\n      \"JSD-based layer-wise prediction divergence\",\n      \"50-token prefix for early quality estimation\",\n      \"Think@n: DTR-filtered majority voting\"\n    ],\n    \"relevance_to_seed\": \"Provides exactly the early-token difficulty signal our framework needs: DTR from short prefixes can drive the online (K, d) allocation — high DTR problems route to expensive verification (GenRM/PRM), low DTR to SC or no verification, before committing compute.\"\n  },\n  {\n    \"title\": \"Scaling Test-Time Compute Without Verification or RL is Suboptimal\",\n    \"venue\": \"ICML 2025 (Spotlight)\",\n    \"problem_identification\": \"The community debated whether verifier-free (VF) methods (distilling search traces) could match verifier-based (VB) methods (RL/search with rewards) as test-time compute scales. No formal separation existed quantifying when and why VB dominates.\",\n    \"key_insight\": \"Anti-concentration of base LLM reward distributions — the property that high-reward traces have non-negligible probability mass — enables VB methods to discover superior policies that VF methods provably cannot identify from expert traces alone, and this gap grows as Ω̃(√H) with test-time compute H.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"Formalizes VB vs VF via learning-theoretic bounds. Theorem 5.4 establishes a VF lower bound scaling as Ω(σ̃_e√(log|Π'|/n)) tied to expert heterogeneity. Theorem 5.7 shows VB upper bound is independent of heterogeneity under anti-concentration (Property 5.6). Theorem 5.8 combines these to prove a separation of Ω̃(H/√n) when the base policy is both heterogeneous and anti-concentrated — conditions empirically verified on Llama-3/8B and S1 models.\",\n    \"limitations_and_open_questions\": \"Assumes bi-level reward structure and n=Ω(H) data budget; the separation under more nuanced reward structures (partial credit, multi-step) is unclear. Does the gap persist when VF methods use iterative self-improvement rather than one-shot distillation?\",\n    \"building_blocks\": [\n      \"Anti-concentration framework for LLM reward distributions\",\n      \"Formal VB vs VF separation theorems\",\n      \"Policy heterogeneity quantification (Property 5.2)\",\n      \"Bi-level reward formalization\"\n    ],\n    \"relevance_to_seed\": \"Provides the theoretical motivation for why verification budget allocation matters — the VB advantage grows with compute, so adaptively choosing verification depth per-instance should amplify this gap for hard problems while saving compute on easy ones.\"\n  },\n  {\n    \"title\": \"Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning\",\n    \"venue\": \"ICLR 2025 (Spotlight)\",\n    \"problem_identification\": \"PRMs trained from automatically-labeled data showed limited gains over ORMs, and human step-level annotation doesn't scale. The gap was that existing PRMs predicted absolute correctness likelihood (Q-values) rather than marginal progress, conflating step quality with prior state quality.\",\n    \"key_insight\": \"Process reward should measure progress — the change in success probability before and after a step under a complementary 'prover' policy — rather than absolute future success likelihood, because advantage-based signals isolate step-level contributions from inherited state quality.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Defines process advantage as the difference in prover policy success rates before vs. after a step, making it an advantage rather than a Q-value. Trains PAVs on automatically-generated advantage labels using a prover policy (empirically Best-of-4 is optimal — neither too weak nor too strong). The prover must be complementary to the base policy: strong enough to distinguish actions via varying advantages, but not so strong that all steps look equally good.\",\n    \"limitations_and_open_questions\": \"Prover policy selection (Best-of-4) is empirically motivated without a principled selection criterion. Does not address when PRM-level verification is worth its cost vs. ORM — the cost-accuracy tradeoff across verification depths remains unexplored.\",\n    \"building_blocks\": [\n      \"Process advantage definition (advantage vs Q-value)\",\n      \"Prover policy concept for auto-labeling PRMs\",\n      \"PAV training pipeline with 1.5-5x compute efficiency over ORMs\",\n      \"Dense reward signals enabling 5-6x RL sample efficiency\"\n    ],\n    \"relevance_to_seed\": \"Directly informs the cost-accuracy curve for PRM verification depth — PAVs provide a concrete, quantified accuracy-vs-compute tradeoff (>8% accuracy gain at 1.5-5x efficiency) that parameterizes the c_v(d) function in our joint optimization framework.\"\n  },\n  {\n    \"title\": \"Is Best-of-N the Best of Them? Coverage, Scaling, and Optimality in Inference-Time Alignment\",\n    \"venue\": \"ICML 2025\",\n    \"problem_identification\": \"Best-of-N is the default inference-time alignment method, but its scaling properties were poorly understood — practitioners observed reward hacking at large N with no theoretical explanation for when BoN breaks down or how to fix it.\",\n    \"key_insight\": \"BoN's regret has two competing terms — coverage (~C★/N, decreasing) and overoptimization (~√(N·ε²_RM), increasing) — and separating regularization strength (β) from sample size (N) via pessimistic rejection sampling eliminates the degradation, achieving scaling-monotonic optimality.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"Formalizes inference-time alignment via coverage-dependent regret bounds. Proves BoN achieves at best ε^(2/3)_RM regret (Theorem 3.2), worse than the √ε_RM skyline. Introduces InferenceTimePessimism: computes per-prompt threshold λ̂(x) satisfying a normalization constraint, then accepts samples via pessimistic weights w(y) = relu(β⁻¹(r̂(x,y)−λ̂(x))). This implements χ²-divergence regularization through rejection sampling, achieving optimal regret √(C★·ε²_RM) that is provably scaling-monotonic (Theorem 4.2).\",\n    \"limitations_and_open_questions\": \"Threshold computation adds per-instance overhead; practical rejection sampling efficiency depends on base policy quality. How does InferenceTimePessimism interact with process-level verification rather than outcome-level reward models?\",\n    \"building_blocks\": [\n      \"Pessimistic rejection sampling algorithm\",\n      \"Scaling-monotonic guarantee framework\",\n      \"Coverage-dependent regret bounds for inference-time methods\",\n      \"Formal separation between N (exploration) and β (regularization)\"\n    ],\n    \"relevance_to_seed\": \"Directly relevant to optimal K selection in our framework — proves naive BoN scaling hits reward hacking, meaning our K allocation must account for verifier imperfection. The per-prompt threshold mechanism is a candidate for our online difficulty estimation signal.\"\n  },\n  {\n    \"title\": \"Budget-aware Test-time Scaling via Discriminative Verification\",\n    \"venue\": \"arXiv 2025 (under review ICLR 2026)\",\n    \"problem_identification\": \"Prior test-time scaling work compared verification methods by accuracy without controlling for compute budget. Generative verification (GenRM) appears superior in accuracy-only comparisons but requires 76x more FLOPs than discriminative alternatives — under fixed budgets, the compute spent on verification could instead generate more candidates.\",\n    \"key_insight\": \"Under practical fixed compute budgets, discriminative verifiers combined with self-consistency consensus signals outperform expensive generative verifiers because the saved compute can be redirected to generating more candidate solutions, exploiting the coverage-selection tradeoff.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"Proposes two hybrid methods: Weighted Self-Consistency (WSC), which selects the answer group with highest total verifier scores, and Pessimistic Verification (PV), which penalizes small answer clusters via a* = argmax_a(r̄(a) − α·ln(N)/(n_a+1)). Discriminative verification adds only 0.1% latency overhead vs. 238% for generative methods. Under equal-budget comparison, PV@32 achieves 15.3% higher accuracy on AIME2025 than generative verification because the budget enables 32 candidates vs. fewer with expensive GenRM.\",\n    \"limitations_and_open_questions\": \"Uses a fixed verification strategy (always discriminative+SC) rather than adapting per-instance. Tested primarily on math benchmarks — discriminative verifiers may underperform on open-ended reasoning where consensus signals are weaker.\",\n    \"building_blocks\": [\n      \"Budget-aware evaluation framework (equal-FLOP comparison)\",\n      \"Pessimistic Verification formula combining consensus + verifier scores\",\n      \"Quantified cost ratios: discriminative=2% vs generative=76x of generation FLOPs\",\n      \"Hybrid WSC and PV methods\"\n    ],\n    \"relevance_to_seed\": \"Provides the strongest existing baseline for budget-aware verification selection and concretely parameterizes the cost ratio c_v(d) across verification depths — but uses a fixed strategy across all instances, exactly the gap our per-instance adaptive allocation addresses.\"\n  },\n  {\n    \"title\": \"Provable Scaling Laws for the Test-Time Compute of Large Language Models\",\n    \"venue\": \"NeurIPS 2025\",\n    \"problem_identification\": \"Existing test-time compute methods (majority voting, BoN with verifiers) lacked provable guarantees on how failure probability scales with compute. No formal scaling laws existed connecting test-time budget to success probability under minimal assumptions.\",\n    \"key_insight\": \"Pairwise comparison via tournament structures — knockout (single-elimination) and league (average win-rate) — requires only two minimal assumptions (p_gen > 0 and p_comp > 0.5) to achieve provable exponential or power-law failure decay, needing no external verifier or reward model.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Knockout tournament: generates N candidates, pairs them for K comparisons each, advances majority winners through ⌈log₂N⌉ rounds. Theorem 2.3 proves failure probability ≤ (1−p_gen)^N + ⌈log₂N⌉·e^(−2K(p_comp−0.5)²), giving exponential decay in both N and K. League tournament: evaluates each candidate's average win rate against K random opponents, selects the highest. Theorem 3.3 proves exponential decay requiring a weaker 'correct-and-strong' assumption with minimum win-rate gap Δ > 0, tolerating systematic pairwise errors.\",\n    \"limitations_and_open_questions\": \"Pairwise comparisons are expensive (O(NK) calls); the assumption p_comp > 0.5 may fail for problems where LLMs cannot reliably compare solutions. How do these bounds tighten when combined with external verifiers of varying quality?\",\n    \"building_blocks\": [\n      \"Tournament-based aggregation algorithms (knockout + league)\",\n      \"Provable exponential/power-law scaling guarantees\",\n      \"Minimal assumption framework (p_gen, p_comp)\",\n      \"Verifier-free test-time scaling with formal bounds\"\n    ],\n    \"relevance_to_seed\": \"Provides theoretical anchoring for our approximation guarantees — the exponential/power-law decay rates under tournament aggregation could upper-bound failure probability for each verification depth d, enabling principled K-d joint optimization with provable per-instance bounds.\"\n  },\n  {\n    \"title\": \"Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling\",\n    \"venue\": \"NeurIPS 2025\",\n    \"problem_identification\": \"Verification frequency during generation is heuristic and static — step-delimited verification has no optimality guarantee. Authors showed >50% of consecutive PRM score deltas are below 1% of score range, revealing massive verification redundancy.\",\n    \"key_insight\": \"A single tunable granularity parameter g creates a continuous spectrum between beam search (g=1) and Best-of-N (g=L), and the optimal g depends dynamically on generator strength, task difficulty, and compute budget — not on any fixed convention.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"VG-Search operates in verify-select-extend-branch cycles with g controlling steps between verifier calls. They derive a closed-form compute cost model C = 2·B₁·(L/g)·[T·(g-1+B₂)·P_g + α·B₂·P_v] that reveals granularity's effect on verification overhead. Two adaptive strategies: CM-gg finds the largest g maintaining accuracy within ε of beam search (minimizing FLOPs), while AM-gg selects g maximizing accuracy under a fixed sample budget. Optimal g is selected on just 5 validation samples.\",\n    \"limitations_and_open_questions\": \"Granularity selection is per-dataset/model, not per-instance — the same g applies to all problems within a configuration. Does not consider verification depth (ORM vs PRM vs GenRM), only frequency.\",\n    \"building_blocks\": [\n      \"Granularity parameter unifying beam search and BoN\",\n      \"Closed-form compute cost model for verification frequency\",\n      \"Adaptive granularity selection strategies (CM-gg, AM-gg)\",\n      \"Score redundancy analysis methodology\"\n    ],\n    \"relevance_to_seed\": \"Directly motivates our extension from tuning verification frequency to jointly selecting verification depth and generation count per-instance — VG-Search optimizes where to verify, we optimize how deeply to verify.\"\n  },\n  {\n    \"title\": \"Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models\",\n    \"venue\": \"ICLR 2025\",\n    \"problem_identification\": \"Training scaling laws were well-studied but compute-optimal inference configurations — how to allocate a fixed inference budget across model size and decoding strategy — were unexplored, leaving practitioners without principled guidance.\",\n    \"key_insight\": \"Scaling inference compute via sophisticated strategies (especially tree search) on smaller models yields Pareto-superior cost-performance tradeoffs compared to simply using larger models with naive decoding.\",\n    \"innovation_type\": \"scaling\",\n    \"method_summary\": \"Systematically compares greedy search, majority voting, Best-of-N, weighted voting, and two tree search variants (including novel REBASE — REward BAlanced SEarch) across Pythia and Llemma model families on MATH/GSM8K. REBASE achieves 7x compute reduction over sampling-based weighted voting at equivalent accuracy. They characterize compute-optimal frontiers showing diminishing returns and model-size-dependent strategy selection.\",\n    \"limitations_and_open_questions\": \"Evaluation limited to math benchmarks (MATH, GSM8K) with Llemma/Pythia families only. Scaling laws are aggregate across problems — no per-instance adaptation. Verification is implicit (PRM scores in tree search) rather than explicitly optimized.\",\n    \"building_blocks\": [\n      \"REBASE tree search algorithm\",\n      \"Compute-optimal inference frontier methodology\",\n      \"FLOPs-based strategy comparison framework\",\n      \"Evidence that model size and inference strategy are substitutes\"\n    ],\n    \"relevance_to_seed\": \"Provides foundational evidence that inference compute allocation matters and establishes the aggregate scaling law methodology that our per-instance adaptive framework explicitly extends with verification depth as a new dimension.\"\n  },\n  {\n    \"title\": \"Variation in Verification: Understanding Verification Dynamics in Large Language Models\",\n    \"venue\": \"ICLR 2026\",\n    \"problem_identification\": \"Verification effectiveness was treated as a static property of the verifier model, but how it varies across problem difficulty, generator capability, and verifier capability was never systematically characterized — obscuring when and why verification helps.\",\n    \"key_insight\": \"Problem difficulty governs True Positive Rate (verifier reliability on correct answers), generator capability determines True Negative Rate (error detectability), and strategic weak-generator/strong-verifier pairing can close 75.7% of the performance gap to stronger generators.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"Studies generative verifiers (CoT reasoning + binary verdict) across 14 open-source models (2B-72B) plus GPT-4o on 12 benchmarks spanning math, knowledge, and NL reasoning. Uses 64 samples per problem for capability estimation and 8 balanced responses (4 correct, 4 incorrect) per verifier evaluation. Decomposes verification into TPR and TNR to isolate difficulty and generator effects, revealing that weak generators produce easier-to-detect errors.\",\n    \"limitations_and_open_questions\": \"Only studies generative verifiers — discriminative ORMs/PRMs may show different dynamics. Provides descriptive analysis without prescribing how to adaptively select verification strategy per-instance based on these dynamics.\",\n    \"building_blocks\": [\n      \"TPR/TNR decomposition of verification effectiveness\",\n      \"Difficulty-dependent verification characterization across 12 benchmarks\",\n      \"Strategic model pairing framework\",\n      \"Empirical evidence that verification benefit varies dramatically per-instance\"\n    ],\n    \"relevance_to_seed\": \"Most directly validates our core hypothesis — verification effectiveness varies dramatically with difficulty and model pairing, providing the empirical grounding that per-instance verification depth selection should yield large gains over fixed strategies.\"\n  },\n  {\n    \"title\": \"Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier\",\n    \"venue\": \"arXiv 2025 (submitted to ICLR 2026, withdrawn)\",\n    \"problem_identification\": \"GenRMs are computationally prohibitive while token-efficient 'NoThinking' verification drops error precision to 39-56%. No system dynamically allocates between fast and slow verification based on instance difficulty.\",\n    \"key_insight\": \"RL-trained fast thinking mode (GRPO on only 1,526 samples) can be reliable enough for most verification instances; consensus-based escalation — measuring agreement among k parallel fast probes — gates expensive slow thinking only when fast assessments disagree, achieving both efficiency and accuracy.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"FlexiVe uses GRPO with a composite reward (correctness + length penalty) to train a dual-mode verifier: fast mode (27-40x fewer tokens via NoThinking template) and slow mode (full deliberation). Flexible allocation runs k fast verifications, computes agreement ratio R = max_i(a_i)/k, and escalates to slow mode only when R < τ. The SDV pipeline adds hesitation-keyword detection with log-probability completeness checks to identify solution endpoints early, triggering targeted verification and feedback-guided refinement.\",\n    \"limitations_and_open_questions\": \"Only evaluated on math benchmarks; k and τ are empirically set without automated tuning; only two verification depths (fast/slow) rather than a richer hierarchy. Withdrawn from ICLR 2026 — reasons unclear but may indicate reviewer concerns.\",\n    \"building_blocks\": [\n      \"GRPO-trained dual-mode verification\",\n      \"Consensus-based escalation from fast to slow verification\",\n      \"Hesitation keyword + log-probability detection of solution completeness\",\n      \"Feedback-guided single-round refinement\"\n    ],\n    \"relevance_to_seed\": \"FlexiVe's binary fast/slow allocation is a special case of our multi-depth hierarchy (none/ORM/PRM/GenRM); their consensus-based difficulty estimation is a candidate signal for our online difficulty estimator, and their hesitation detection directly relates to our early-token difficulty signals.\"\n  },\n  {\n    \"title\": \"Trust but Verify! A Survey on Verification Design for Test-time Scaling\",\n    \"venue\": \"arXiv 2025\",\n    \"problem_identification\": \"The verification landscape for test-time scaling was fragmented across isolated works with no unified taxonomy — researchers lac\n... (truncated)\n\n## Your task\n\nSynthesize these paper analyses into a **Field Guide** — a strategic document that would help a researcher generate novel, high-quality ideas in this area. This is NOT a survey — it's an opinionated strategy guide for innovation.\n\nThink about:\n- What PATTERNS OF INNOVATION keep working in this field?\n- What do reviewers consistently reward?\n- Where are the real gaps (not assumed gaps)?\n- What combinations haven't been tried?\n- What mistakes should we avoid?\n\n## Output format\n\nOutput a JSON object with these sections:\n{\n  \"innovation_patterns\": [\n    {\"pattern\": \"name\", \"description\": \"how it works\", \"examples\": [\"paper1\", \"paper2\"], \"success_rate\": \"high/medium/low\"}\n  ],\n  \"reviewer_preferences\": [\n    \"What reviewers in this area consistently care about (based on evidence from paper analyses)\"\n  ],\n  \"field_gaps\": [\n    {\"gap\": \"description of unsolved problem\", \"evidence\": \"which papers mention this limitation\", \"difficulty\": \"high/medium/low\", \"impact_if_solved\": \"high/medium/low\"}\n  ],\n  \"untried_combinations\": [\n    {\"idea_sketch\": \"what could be combined\", \"from_papers\": [\"which papers inspire this\"], \"why_promising\": \"reason\"}\n  ],\n  \"method_building_blocks\": [\n    {\"tool\": \"name\", \"what_it_does\": \"description\", \"used_by\": [\"papers\"], \"could_be_applied_to\": \"new application\"}\n  ],\n  \"common_pitfalls\": [\n    \"Mistakes to avoid when working in this area (based on reviewer feedback and paper limitations)\"\n  ],\n  \"field_trajectory\": \"Where is this field heading? What are the 2-3 most promising macro-directions? (paragraph)\",\n  \"meta_advice\": \"If you were advising a PhD student to write a strong 2026 paper in this area, what would you tell them? (paragraph)\"\n}\n\nBe specific and evidence-based — every claim should reference specific papers from the analyses. Avoid generic advice like 'be novel' — instead say 'Papers that combine X with Y for task Z have been getting accepted (see Paper A, Paper B).'.\n\nIMPORTANT: You MUST end your response with the JSON object."
}
```

---

### Runtime record

_source line 2 · 2026-05-29T05:34:07.302Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T05:34:07.302Z",
  "sessionId": "16d354d1-0aea-44ae-a93e-7ed499be64b1"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-29T05:34:07.366Z_

You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.

**Today's date: 2026-05-29 (UTC).**

## Research area: Target: AAAI 2026
Track: Machine Learning (ML) — Efficient Inference and Reasoning

Direction: Per-instance adaptive co-optimization of generation and verification compute, where both the number of generated solutions (K) and the verification depth (none/ORM/PRM/GenRM) are jointly selected based on online difficulty estimation from early reasoning tokens. Extends static aggregate scaling laws (Singhi et al.) to instance-adaptive, multi-depth allocation with a practical online algorithm.

Seed Papers:
- Singhi et al., "When To Solve, When To Verify" (arXiv 2025) — establishes aggregate scaling laws for generation-verification tradeoff; our work must explicitly extend this to per-instance, multi-depth allocation
- Setlur et al., "Scaling TTC Without Verification is Suboptimal" (arXiv Feb 2025) — proves verification is essential and the gap grows with compute; motivates why verification budget allocation matters
- Chen et al., "VG-Search: Rethinking Optimal Verification Granularity" (arXiv May 2025) — shows verification granularity matters for efficiency; we extend from granularity to depth and per-instance adaptation
- Wang et al., "ST-BoN" (NeurIPS 2025 Spotlight) — early pruning via sampling consistency; a strong baseline for lightweight verification allocation

Known Gaps:
- No method selects verification depth (none/ORM/PRM/GenRM) per-instance based on estimated difficulty; all existing work uses a fixed verification strategy across problems
- Singhi et al.'s scaling laws are static and aggregate (one ratio for all problems); no online algorithm adapts the generation-verification split per-instance during inference
- No framework jointly optimizes K (number of solutions) and d (verification depth) as coupled decision variables under a shared compute budget

Theoretical Anchor: The bilinear structure of the joint optimization — P(correct) depends on coverage (increasing in K) and selection precision (increasing in d), while cost is c_g*K + c_v(d)*K = K*(c_g + c_v(d)) — admits a clean decomposition: for fixed d, optimal K = B/(c_g + c_v(d)), reducing the problem to selecting d* that maximizes selection precision per unit verification cost. This decomposition enables tractable optimization with provable approximation guarantees under mild assumptions on verifier accuracy monotonicity.

Constraints:
- Compute: ≤200 H100-hours
- Must evaluate on ≥4 benchmarks across ≥2 domains (math, code, science)
- Must compare against Singhi et al.'s aggregate-optimal baseline and fixed-depth baselines

Quality Self-Checks:
- [x] Core insight: The optimal verification depth varies dramatically per problem — easy problems need no verification while hard problems benefit from expensive generative verification — and this variance is predictable from early tokens.
- [x] Why not obvious: Singhi et al. showed the aggregate optimal ratio, but the per-instance variance and multi-depth selection weren't explored because their framework only compared two verification strategies (GenRM vs SC), not a continuum of depths.
- [ ] Baseline fear test: A simple heuristic (e.g., always use PRM for problems longer than X tokens) could capture much of the benefit — must demonstrate learned allocation significantly outperforms simple rules. This is a REAL RISK.
- [x] Information exploited: Early-token difficulty signals (entropy trajectory, hesitation markers from Zhou et al.) that are available before verification decisions must be made.

Avoid:
- Framing as 'first to study generation-verification tradeoff' — Singhi et al. already did this; frame as extending to per-instance multi-depth allocation
- Math-only evaluation — must include code and science benchmarks
- Pure scaling law contribution — must provide a practical online algorithm, not just power-law fits
- Ignoring the baseline fear: if a simple threshold on problem length achieves 80% of the adaptive allocation's gain, the paper is dead

## Paper analyses (20 papers)

[
  {
    "title": "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters",
    "venue": "ICLR 2025 (Oral)",
    "problem_identification": "Prior work scaled test-time compute uniformly across prompts. Snell et al. identified that the effectiveness of different test-time strategies (search vs. revision) varies dramatically by prompt difficulty, making uniform allocation wasteful.",
    "key_insight": "Per-prompt compute-optimal allocation—selecting between PRM-guided search and sequential revision based on estimated difficulty—achieves 4× the efficiency of uniform best-of-N, because easy problems benefit from revision while hard problems need parallel search.",
    "innovation_type": "new_formulation",
    "method_summary": "They formalize test-time scaling as selecting strategy θ* per prompt to maximize P(correct) under budget N. Two mechanisms are studied: (1) PRM-guided search (best-of-N weighted, beam search, lookahead search) and (2) sequential revision chains with hierarchical verifier selection. Difficulty is operationalized via binned pass@1 rates (oracle) or averaged PRM scores (practical), and strategy selection uses two-fold cross-validation across five difficulty bins. Key finding: the optimal sequential-to-parallel ratio shifts systematically with difficulty.",
    "limitations_and_open_questions": "Difficulty estimation cost is not fully accounted in compute budgets (requires sampling to estimate PRM scores). Only two strategy families (search vs. revision) are compared—no multi-depth verification hierarchy. Relies on PaLM 2 ecosystem with no open replication.",
    "building_blocks": [
      "Per-prompt difficulty binning via PRM scores",
      "PRM-guided beam/lookahead search",
      "Sequential revision chains with verifier reranking",
      "Compute-optimal strategy selection via cross-validation"
    ],
    "relevance_to_seed": "Direct conceptual ancestor: proves per-prompt adaptive allocation works for test-time compute, but only considers two strategy types—our work extends to a continuum of verification depths (none/ORM/PRM/GenRM) as coupled decision variables with K."
  },
  {
    "title": "Sampling-Efficient Test-Time Scaling: Self-Estimating the Best-of-N Sampling in Early Decoding",
    "venue": "NeurIPS 2025 (Spotlight)",
    "problem_identification": "Full best-of-N sampling generates N complete solutions consuming O(N×T) GPU memory, then applies a reward model adding further overhead. The authors observed that internal representations at early decoding steps already contain signal to identify the most promising sample.",
    "key_insight": "Chain-of-Embedding (CoE) curvature across layers at early tokens predicts solution quality via peer consistency—samples whose latent trajectories align most closely with the majority tend to be correct—enabling truncation of N-1 paths after only ~c tokens.",
    "innovation_type": "new_technique",
    "method_summary": "ST-BoN extracts hidden states across all L layers at the earliest divergence point c, forming a Chain-of-Embedding H = h₀→h₁→...→h_L. A curvature-based feature metric F(H) scores each sample by distance to peers. Over a buffer window of τ steps, majority voting across timestep-wise rankings selects the best sample; remaining N-1 are truncated. Memory drops from O(N×T) to O(max(N×c, T)), yielding >80% GPU memory reduction and 50% latency reduction while matching full BoN accuracy.",
    "limitations_and_open_questions": "Requires white-box access to hidden states (inapplicable to closed-source APIs). Buffer window length τ is fixed rather than adaptive to task complexity. CoE metric is validated empirically but lacks theoretical guarantees on when consistency implies correctness.",
    "building_blocks": [
      "Chain-of-Embedding (CoE) feature metric",
      "Early-token consistency-based pruning",
      "Majority voting across buffer window",
      "Reward-model-free sample selection"
    ],
    "relevance_to_seed": "Strong baseline for lightweight verification allocation: ST-BoN's early-signal mechanism could serve as the 'none' or 'lightweight' tier in our verification depth hierarchy, and its CoE features may complement our difficulty estimation from early tokens."
  },
  {
    "title": "Scaling LLM Inference with Optimized Sample Compute Allocation",
    "venue": "NAACL 2025",
    "problem_identification": "Existing test-time scaling uses a single inference configuration (fixed model, temperature, prompt). Zhang et al. recognized that different problems favor different configurations, and the optimal strategy is a mixture—not a single best setting.",
    "key_insight": "The pass@C objective under mixed configurations decomposes into a convex optimization (after relaxing integrality), enabling efficient hill-climbing to find optimal configuration mixtures that achieve 128× compute savings over the best pure strategy on code generation.",
    "innovation_type": "new_formulation",
    "method_summary": "They define inference configurations as d-tuples (model, temperature, language, prompt) and formulate allocation as: max_π (1/|D|)Σ_j(1-∏_i(1-p_ij)^π_i) subject to Σπ_i=C. The probability matrix P is estimated by sampling C₀ times per config-problem pair on training data. Convexity of the relaxed problem is proven via composition of exponentials over affine functions. Hill-climbing iteratively shifts one sample between configurations until no improving neighbor exists. Evaluated on HumanEval, MBPP, MATH, GSM8K, and SWE-Bench.",
    "limitations_and_open_questions": "Optimization is offline (requires training-set estimation of P), so cannot adapt per-instance at inference time. Configuration space is pre-discretized. Assumes independent sampling which ignores sequential refinement strategies. No verification depth dimension.",
    "building_blocks": [
      "Convex formulation of configuration mixture optimization",
      "Hill-climbing allocation algorithm",
      "Probability matrix estimation from training samples",
      "Multi-model multi-temperature configuration space"
    ],
    "relevance_to_seed": "Closest existing work to our K-allocation component: OSCA optimizes how many samples per configuration but does so offline across a dataset—our work must do this per-instance and jointly with verification depth d, making the online difficulty estimation the key differentiator."
  },
  {
    "title": "DiffAdapt: Difficulty-Adaptive Reasoning for Token-Efficient LLM Inference",
    "venue": "ICLR 2026",
    "problem_identification": "Reasoning LLMs apply uniform-length reasoning traces regardless of problem difficulty, causing 'overthinking' on easy problems. Liu et al. discovered this by analyzing token entropy distributions across difficulty-stratified problem sets, revealing a U-shaped pattern.",
    "key_insight": "A U-shaped entropy pattern (high on easy problems from unnecessary exploration, low on medium, high on hard from genuine uncertainty) is detectable from the LLM's final hidden state via a lightweight MLP probe, enabling pre-generation difficulty routing.",
    "innovation_type": "combination",
    "method_summary": "A two-layer MLP probe is trained on final-layer hidden states (300 problems/level from DeepMath-103K, AdamW, 100 epochs) to classify Easy/Normal/Hard. Each class maps to a fixed strategy tuple (temperature, max_tokens multiplier, prompt style). Heuristic labels use correctness rate C(x) and mean entropy H̄(x) with model-specific thresholds. At inference, the probe routes each question to its strategy before generation begins. Achieves 22.4% token reduction with maintained or improved accuracy across 5 models and 8 benchmarks.",
    "limitations_and_open_questions": "Only three discrete difficulty levels with heuristic thresholds—no continuous adaptation. Adapts reasoning length and temperature, not verification strategy. Probe trained on math (DeepMath-103K); cross-domain transfer unclear. The baseline fear applies: a simple token-length threshold may capture much of the gain.",
    "building_blocks": [
      "U-shaped entropy pattern as difficulty signal",
      "Lightweight MLP probe on hidden states for difficulty classification",
      "Pre-generation strategy routing",
      "Heuristic difficulty labeling from correctness/entropy"
    ],
    "relevance_to_seed": "Closest concurrent work on per-instance difficulty adaptation, but operates on a different axis (reasoning length) than our verification depth. Their hidden-state probe and entropy-based difficulty characterization are directly reusable as features for our online difficulty estimator."
  },
  {
    "title": "Process Reward Models That Think",
    "venue": "arXiv 2025 (ICLR 2026 withdrawn)",
    "problem_identification": "Discriminative PRMs require massive step-level labels (PRM800K) and generalize poorly out-of-domain. LLM-as-Judge scales inconsistently with more compute. Khalifa et al. identified that framing verification as generation (long CoT) rather than classification bridges both gaps.",
    "key_insight": "A generative process verifier that 'thinks' via long chain-of-thought, fine-tuned on only 1% of PRM800K labels, outperforms discriminative PRMs on in-domain tasks and surpasses them by 8% out-of-domain—because generation enables compositional reasoning about step correctness.",
    "innovation_type": "simplification",
    "method_summary": "ThinkPRM fine-tunes a base LLM to generate step-by-step verification reasoning (long CoT) for each solution step, producing a final correctness judgment. Training uses only 8K process labels or 1K synthetic examples. Verification compute scales by allowing longer thinking traces (up to ~24K tokens), with monotonically improving F1—unlike LLM-as-Judge which plateaus. Evaluated on ProcessBench, MATH-500, AIME'24 (in-domain) and GPQA-Diamond, LiveCodeBench (out-of-domain).",
    "limitations_and_open_questions": "Long CoT verification is expensive per solution (up to 24K tokens), creating a compute-accuracy tradeoff that makes it unsuitable for all problems. Withdrawn from ICLR 2026—possibly due to concurrent work or scope concerns. No analysis of when generative verification is cost-effective vs. cheaper alternatives.",
    "building_blocks": [
      "Generative (long-CoT) process reward model",
      "Data-efficient PRM training (<1% labels)",
      "Scalable verification compute via thinking length",
      "Out-of-domain generalization of generative verifiers"
    ],
    "relevance_to_seed": "Key evidence for our verification depth hierarchy: ThinkPRM demonstrates that generative verification (GenRM) achieves highest accuracy but at substantial cost, defining the expensive end of our none→ORM→PRM→GenRM depth spectrum and motivating per-instance selection of when this cost is justified."
  },
  {
    "title": "When To Solve, When To Verify: Compute-Optimal Problem Solving and Generative Verification for LLM Reasoning",
    "venue": "COLM 2025",
    "problem_identification": "No prior work compared SC vs GenRM under a unified compute budget accounting for verification token costs. By normalizing to FLOPs (C = S·(1 + λV)), they revealed GenRM's apparent superiority was an artifact of ignoring verification compute.",
    "key_insight": "Under iso-compute comparison, Self-Consistency dominates GenRM for most practical budgets, with GenRM requiring 8× more compute to merely match SC—because solutions should scale 1.5–2× faster than verifications (S_opt ∝ C^0.57 vs V_opt ∝ C^0.39).",
    "innovation_type": "analysis",
    "method_summary": "Derives power-law inference scaling laws by sweeping (S, V) combinations across models (Llama-3.1-8B, Qwen-2.5-7B, Llama-3.3-70B, QwQ-32B) and datasets (MATH, AIME, GPQA, LiveCodeBench). Fits S_opt and V_opt as functions of compute budget C, showing solutions scale faster. Crucially notes GenRM yields up to 30% relative improvement on hard problems, implicitly motivating per-instance allocation.",
    "limitations_and_open_questions": "Analysis is aggregate-only (one ratio for all problems) and compares only SC vs GenRM binary, not a continuum of verification depths. The difficulty-dependent finding (GenRM better on hard problems) is acknowledged but not operationalized into an algorithm.",
    "building_blocks": [
      "Unified compute metric C(S,V) = S(1+λV)",
      "Power-law scaling fits for S_opt/V_opt",
      "Difficulty-stratified analysis showing GenRM advantage on hard problems",
      "Multi-model multi-domain evaluation protocol"
    ],
    "relevance_to_seed": "Direct seed paper — our work extends their aggregate scaling laws to per-instance, multi-depth allocation by operationalizing their own finding that difficulty modulates the optimal generation-verification ratio."
  },
  {
    "title": "Generative Verifiers: Reward Modeling as Next-Token Prediction",
    "venue": "ICLR 2025",
    "problem_identification": "Discriminative reward models treat verification as classification, forfeiting LLM generative capabilities — they cannot perform chain-of-thought reasoning during verification or leverage test-time compute scaling via sampling.",
    "key_insight": "Recasting verification as next-token prediction (predicting 'Yes'/'No' after optionally generating a CoT rationale) unifies generation and verification objectives, enabling CoT verification and majority-vote scaling at inference time.",
    "innovation_type": "new_formulation",
    "method_summary": "Trains with a mixed loss L_GenRM = L_SFT(verify) + λ·L_SFT(generate), where verification uses synthetic CoT rationales generated via reference-guided grading. At inference, GenRM-CoT samples K rationales and averages p(Yes|rationale) for robust scoring. This enables a compute-accuracy tradeoff within verification itself (MajV@K).",
    "limitations_and_open_questions": "Synthetic rationales require reference solutions during training (privileged information). The compute cost of CoT verification is substantial but not explicitly traded off against generating more solutions — exactly the gap Singhi et al. later exposed.",
    "building_blocks": [
      "GenRM verification scoring: r = p(Yes|x,y,rationale)",
      "CoT verification rationale generation",
      "MajV@K: majority voting over verification rationales",
      "Unified generation-verification training loss"
    ],
    "relevance_to_seed": "Defines the GenRM verification depth level in our hierarchy; its MajV@K mechanism is a natural candidate for the highest-cost verification tier in our per-instance depth selection framework."
  },
  {
    "title": "Optimizing Test-Time Compute via Meta Reinforcement Fine-Tuning",
    "venue": "ICML 2025",
    "problem_identification": "Standard outcome-reward RL for test-time compute wastes tokens on unproductive reasoning because it only rewards final success, providing no signal for intermediate progress or efficient exploration within the token stream.",
    "key_insight": "Test-time generation is structurally analogous to meta-RL: token-stream segments are 'episodes' whose cumulative regret should be minimized, and a dense 'progress' reward (change in success likelihood per episode) achieves this by balancing exploration and exploitation.",
    "innovation_type": "new_formulation",
    "method_summary": "Segments output into episodes, defines progress as r_prg = P(correct|episodes_0:j) − P(correct|episodes_0:j−1), and trains with ℓ_MRT = outcome_reward + α·Σ(progress). A meta-prover μ estimates success probability by forcing early termination ('[time is up]&lt;/think>'). Two variants: STaR (filter+SFT on high-progress traces) and RL (on-policy with dense+outcome rewards).",
    "limitations_and_open_questions": "The progress reward requires sampling multiple continuations per prefix during training, which is expensive. The framework optimizes within-model reasoning but does not consider external verification as a complementary compute allocation — it's purely about making the generator more efficient.",
    "building_blocks": [
      "Cumulative regret formalization for TTC",
      "Progress reward: Δ_j = P(correct|prefix_j) - P(correct|prefix_{j-1})",
      "Meta-prover via forced early termination",
      "Episode-segmented token stream for RL"
    ],
    "relevance_to_seed": "The cumulative regret framework and progress metric could serve as the online difficulty estimator in our system — if early episodes show low progress, this signals a hard problem needing deeper verification, directly informing our (K, d) allocation."
  },
  {
    "title": "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning",
    "venue": "AAAI 2026",
    "problem_identification": "Existing PRMs are limited by scalar prediction (no generative reasoning), weak process supervision labels, and inability to scale test-time compute. These three gaps compound: discriminative PRMs cannot explain their judgments or improve with more inference budget.",
    "key_insight": "A generative PRM that performs explicit CoT reasoning with code verification before step-level judgment can dramatically outperform discriminative PRMs (1.5B > GPT-4o) with minimal training data (23K samples), because generation enables both better reasoning and test-time compute scaling.",
    "innovation_type": "combination",
    "method_summary": "Introduces Relative Progress Estimation (RPE) to label process supervision by comparing model confidence with/without each step (MC(s_t,a_t)/MC(s_t)). Synthesizes training rationales combining CoT reasoning and executable code verification. Trains GenPRM to generate reasoning+code before judging each step, enabling test-time scaling via sampling multiple verification chains.",
    "limitations_and_open_questions": "Evaluated primarily on math (ProcessBench/MATH); generalization to code/science domains unclear. RPE quality depends on the base model's calibration. The compute cost of generative step-level verification is high — when this cost is worthwhile vs. simpler ORM remains unaddressed.",
    "building_blocks": [
      "RPE for automatic process supervision labels",
      "CoT + code verification before step judgment",
      "Generative PRM scaling via sampling",
      "Critic model for policy refinement"
    ],
    "relevance_to_seed": "Provides a concrete high-depth verification option (PRM with CoT+code) in our framework. Its high accuracy but high cost makes it the ideal candidate for the 'hard problem' tier, while its 23K-sample efficiency suggests practical deployability."
  },
  {
    "title": "Think Deep, Not Just Long: Measuring LLM Reasoning Effort via Deep-Thinking Tokens",
    "venue": "arXiv 2026",
    "problem_identification": "Output length is widely used as a proxy for reasoning effort but correlates negatively with accuracy (r = −0.594). No mechanistically grounded metric existed to measure genuine inferential effort from internal model computations.",
    "key_insight": "Deep-thinking tokens — where predictions undergo significant revision in deeper layers (measured by JSD between intermediate and final layer distributions exceeding a settling threshold) — provide a robust, positively correlated difficulty signal (r = 0.683) that enables efficient test-time scaling via early prefix-based filtering.",
    "innovation_type": "new_technique",
    "method_summary": "Computes JSD(p_{t,L} || p_{t,l}) per token per layer, defines settling depth c_t = min{l: D̄_{t,l} ≤ 0.5}, classifies tokens with c_t ≥ 0.85·L as deep-thinking, and aggregates into Deep-Thinking Ratio (DTR). Think@n generates n samples, ranks by DTR from 50-token prefixes, selects top 50%, and applies majority voting — matching full self-consistency at 50% cost.",
    "limitations_and_open_questions": "Requires access to intermediate layer activations (not available via API for proprietary models). The 50-token prefix and ρ=0.85 thresholds are empirically set — sensitivity analysis across architectures is limited. Correlation is shown but causal mechanism (why deep thinking → correctness) is not established.",
    "building_blocks": [
      "Deep-thinking ratio (DTR) as difficulty signal",
      "JSD-based layer-wise prediction divergence",
      "50-token prefix for early quality estimation",
      "Think@n: DTR-filtered majority voting"
    ],
    "relevance_to_seed": "Provides exactly the early-token difficulty signal our framework needs: DTR from short prefixes can drive the online (K, d) allocation — high DTR problems route to expensive verification (GenRM/PRM), low DTR to SC or no verification, before committing compute."
  },
  {
    "title": "Scaling Test-Time Compute Without Verification or RL is Suboptimal",
    "venue": "ICML 2025 (Spotlight)",
    "problem_identification": "The community debated whether verifier-free (VF) methods (distilling search traces) could match verifier-based (VB) methods (RL/search with rewards) as test-time compute scales. No formal separation existed quantifying when and why VB dominates.",
    "key_insight": "Anti-concentration of base LLM reward distributions — the property that high-reward traces have non-negligible probability mass — enables VB methods to discover superior policies that VF methods provably cannot identify from expert traces alone, and this gap grows as Ω̃(√H) with test-time compute H.",
    "innovation_type": "analysis",
    "method_summary": "Formalizes VB vs VF via learning-theoretic bounds. Theorem 5.4 establishes a VF lower bound scaling as Ω(σ̃_e√(log|Π'|/n)) tied to expert heterogeneity. Theorem 5.7 shows VB upper bound is independent of heterogeneity under anti-concentration (Property 5.6). Theorem 5.8 combines these to prove a separation of Ω̃(H/√n) when the base policy is both heterogeneous and anti-concentrated — conditions empirically verified on Llama-3/8B and S1 models.",
    "limitations_and_open_questions": "Assumes bi-level reward structure and n=Ω(H) data budget; the separation under more nuanced reward structures (partial credit, multi-step) is unclear. Does the gap persist when VF methods use iterative self-improvement rather than one-shot distillation?",
    "building_blocks": [
      "Anti-concentration framework for LLM reward distributions",
      "Formal VB vs VF separation theorems",
      "Policy heterogeneity quantification (Property 5.2)",
      "Bi-level reward formalization"
    ],
    "relevance_to_seed": "Provides the theoretical motivation for why verification budget allocation matters — the VB advantage grows with compute, so adaptively choosing verification depth per-instance should amplify this gap for hard problems while saving compute on easy ones."
  },
  {
    "title": "Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning",
    "venue": "ICLR 2025 (Spotlight)",
    "problem_identification": "PRMs trained from automatically-labeled data showed limited gains over ORMs, and human step-level annotation doesn't scale. The gap was that existing PRMs predicted absolute correctness likelihood (Q-values) rather than marginal progress, conflating step quality with prior state quality.",
    "key_insight": "Process reward should measure progress — the change in success probability before and after a step under a complementary 'prover' policy — rather than absolute future success likelihood, because advantage-based signals isolate step-level contributions from inherited state quality.",
    "innovation_type": "new_formulation",
    "method_summary": "Defines process advantage as the difference in prover policy success rates before vs. after a step, making it an advantage rather than a Q-value. Trains PAVs on automatically-generated advantage labels using a prover policy (empirically Best-of-4 is optimal — neither too weak nor too strong). The prover must be complementary to the base policy: strong enough to distinguish actions via varying advantages, but not so strong that all steps look equally good.",
    "limitations_and_open_questions": "Prover policy selection (Best-of-4) is empirically motivated without a principled selection criterion. Does not address when PRM-level verification is worth its cost vs. ORM — the cost-accuracy tradeoff across verification depths remains unexplored.",
    "building_blocks": [
      "Process advantage definition (advantage vs Q-value)",
      "Prover policy concept for auto-labeling PRMs",
      "PAV training pipeline with 1.5-5x compute efficiency over ORMs",
      "Dense reward signals enabling 5-6x RL sample efficiency"
    ],
    "relevance_to_seed": "Directly informs the cost-accuracy curve for PRM verification depth — PAVs provide a concrete, quantified accuracy-vs-compute tradeoff (>8% accuracy gain at 1.5-5x efficiency) that parameterizes the c_v(d) function in our joint optimization framework."
  },
  {
    "title": "Is Best-of-N the Best of Them? Coverage, Scaling, and Optimality in Inference-Time Alignment",
    "venue": "ICML 2025",
    "problem_identification": "Best-of-N is the default inference-time alignment method, but its scaling properties were poorly understood — practitioners observed reward hacking at large N with no theoretical explanation for when BoN breaks down or how to fix it.",
    "key_insight": "BoN's regret has two competing terms — coverage (~C★/N, decreasing) and overoptimization (~√(N·ε²_RM), increasing) — and separating regularization strength (β) from sample size (N) via pessimistic rejection sampling eliminates the degradation, achieving scaling-monotonic optimality.",
    "innovation_type": "new_technique",
    "method_summary": "Formalizes inference-time alignment via coverage-dependent regret bounds. Proves BoN achieves at best ε^(2/3)_RM regret (Theorem 3.2), worse than the √ε_RM skyline. Introduces InferenceTimePessimism: computes per-prompt threshold λ̂(x) satisfying a normalization constraint, then accepts samples via pessimistic weights w(y) = relu(β⁻¹(r̂(x,y)−λ̂(x))). This implements χ²-divergence regularization through rejection sampling, achieving optimal regret √(C★·ε²_RM) that is provably scaling-monotonic (Theorem 4.2).",
    "limitations_and_open_questions": "Threshold computation adds per-instance overhead; practical rejection sampling efficiency depends on base policy quality. How does InferenceTimePessimism interact with process-level verification rather than outcome-level reward models?",
    "building_blocks": [
      "Pessimistic rejection sampling algorithm",
      "Scaling-monotonic guarantee framework",
      "Coverage-dependent regret bounds for inference-time methods",
      "Formal separation between N (exploration) and β (regularization)"
    ],
    "relevance_to_seed": "Directly relevant to optimal K selection in our framework — proves naive BoN scaling hits reward hacking, meaning our K allocation must account for verifier imperfection. The per-prompt threshold mechanism is a candidate for our online difficulty estimation signal."
  },
  {
    "title": "Budget-aware Test-time Scaling via Discriminative Verification",
    "venue": "arXiv 2025 (under review ICLR 2026)",
    "problem_identification": "Prior test-time scaling work compared verification methods by accuracy without controlling for compute budget. Generative verification (GenRM) appears superior in accuracy-only comparisons but requires 76x more FLOPs than discriminative alternatives — under fixed budgets, the compute spent on verification could instead generate more candidates.",
    "key_insight": "Under practical fixed compute budgets, discriminative verifiers combined with self-consistency consensus signals outperform expensive generative verifiers because the saved compute can be redirected to generating more candidate solutions, exploiting the coverage-selection tradeoff.",
    "innovation_type": "combination",
    "method_summary": "Proposes two hybrid methods: Weighted Self-Consistency (WSC), which selects the answer group with highest total verifier scores, and Pessimistic Verification (PV), which penalizes small answer clusters via a* = argmax_a(r̄(a) − α·ln(N)/(n_a+1)). Discriminative verification adds only 0.1% latency overhead vs. 238% for generative methods. Under equal-budget comparison, PV@32 achieves 15.3% higher accuracy on AIME2025 than generative verification because the budget enables 32 candidates vs. fewer with expensive GenRM.",
    "limitations_and_open_questions": "Uses a fixed verification strategy (always discriminative+SC) rather than adapting per-instance. Tested primarily on math benchmarks — discriminative verifiers may underperform on open-ended reasoning where consensus signals are weaker.",
    "building_blocks": [
      "Budget-aware evaluation framework (equal-FLOP comparison)",
      "Pessimistic Verification formula combining consensus + verifier scores",
      "Quantified cost ratios: discriminative=2% vs generative=76x of generation FLOPs",
      "Hybrid WSC and PV methods"
    ],
    "relevance_to_seed": "Provides the strongest existing baseline for budget-aware verification selection and concretely parameterizes the cost ratio c_v(d) across verification depths — but uses a fixed strategy across all instances, exactly the gap our per-instance adaptive allocation addresses."
  },
  {
    "title": "Provable Scaling Laws for the Test-Time Compute of Large Language Models",
    "venue": "NeurIPS 2025",
    "problem_identification": "Existing test-time compute methods (majority voting, BoN with verifiers) lacked provable guarantees on how failure probability scales with compute. No formal scaling laws existed connecting test-time budget to success probability under minimal assumptions.",
    "key_insight": "Pairwise comparison via tournament structures — knockout (single-elimination) and league (average win-rate) — requires only two minimal assumptions (p_gen > 0 and p_comp > 0.5) to achieve provable exponential or power-law failure decay, needing no external verifier or reward model.",
    "innovation_type": "new_formulation",
    "method_summary": "Knockout tournament: generates N candidates, pairs them for K comparisons each, advances majority winners through ⌈log₂N⌉ rounds. Theorem 2.3 proves failure probability ≤ (1−p_gen)^N + ⌈log₂N⌉·e^(−2K(p_comp−0.5)²), giving exponential decay in both N and K. League tournament: evaluates each candidate's average win rate against K random opponents, selects the highest. Theorem 3.3 proves exponential decay requiring a weaker 'correct-and-strong' assumption with minimum win-rate gap Δ > 0, tolerating systematic pairwise errors.",
    "limitations_and_open_questions": "Pairwise comparisons are expensive (O(NK) calls); the assumption p_comp > 0.5 may fail for problems where LLMs cannot reliably compare solutions. How do these bounds tighten when combined with external verifiers of varying quality?",
    "building_blocks": [
      "Tournament-based aggregation algorithms (knockout + league)",
      "Provable exponential/power-law scaling guarantees",
      "Minimal assumption framework (p_gen, p_comp)",
      "Verifier-free test-time scaling with formal bounds"
    ],
    "relevance_to_seed": "Provides theoretical anchoring for our approximation guarantees — the exponential/power-law decay rates under tournament aggregation could upper-bound failure probability for each verification depth d, enabling principled K-d joint optimization with provable per-instance bounds."
  },
  {
    "title": "Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling",
    "venue": "NeurIPS 2025",
    "problem_identification": "Verification frequency during generation is heuristic and static — step-delimited verification has no optimality guarantee. Authors showed >50% of consecutive PRM score deltas are below 1% of score range, revealing massive verification redundancy.",
    "key_insight": "A single tunable granularity parameter g creates a continuous spectrum between beam search (g=1) and Best-of-N (g=L), and the optimal g depends dynamically on generator strength, task difficulty, and compute budget — not on any fixed convention.",
    "innovation_type": "new_formulation",
    "method_summary": "VG-Search operates in verify-select-extend-branch cycles with g controlling steps between verifier calls. They derive a closed-form compute cost model C = 2·B₁·(L/g)·[T·(g-1+B₂)·P_g + α·B₂·P_v] that reveals granularity's effect on verification overhead. Two adaptive strategies: CM-gg finds the largest g maintaining accuracy within ε of beam search (minimizing FLOPs), while AM-gg selects g maximizing accuracy under a fixed sample budget. Optimal g is selected on just 5 validation samples.",
    "limitations_and_open_questions": "Granularity selection is per-dataset/model, not per-instance — the same g applies to all problems within a configuration. Does not consider verification depth (ORM vs PRM vs GenRM), only frequency.",
    "building_blocks": [
      "Granularity parameter unifying beam search and BoN",
      "Closed-form compute cost model for verification frequency",
      "Adaptive granularity selection strategies (CM-gg, AM-gg)",
      "Score redundancy analysis methodology"
    ],
    "relevance_to_seed": "Directly motivates our extension from tuning verification frequency to jointly selecting verification depth and generation count per-instance — VG-Search optimizes where to verify, we optimize how deeply to verify."
  },
  {
    "title": "Inference Scaling Laws: An Empirical Analysis of Compute-Optimal Inference for Problem-Solving with Language Models",
    "venue": "ICLR 2025",
    "problem_identification": "Training scaling laws were well-studied but compute-optimal inference configurations — how to allocate a fixed inference budget across model size and decoding strategy — were unexplored, leaving practitioners without principled guidance.",
    "key_insight": "Scaling inference compute via sophisticated strategies (especially tree search) on smaller models yields Pareto-superior cost-performance tradeoffs compared to simply using larger models with naive decoding.",
    "innovation_type": "scaling",
    "method_summary": "Systematically compares greedy search, majority voting, Best-of-N, weighted voting, and two tree search variants (including novel REBASE — REward BAlanced SEarch) across Pythia and Llemma model families on MATH/GSM8K. REBASE achieves 7x compute reduction over sampling-based weighted voting at equivalent accuracy. They characterize compute-optimal frontiers showing diminishing returns and model-size-dependent strategy selection.",
    "limitations_and_open_questions": "Evaluation limited to math benchmarks (MATH, GSM8K) with Llemma/Pythia families only. Scaling laws are aggregate across problems — no per-instance adaptation. Verification is implicit (PRM scores in tree search) rather than explicitly optimized.",
    "building_blocks": [
      "REBASE tree search algorithm",
      "Compute-optimal inference frontier methodology",
      "FLOPs-based strategy comparison framework",
      "Evidence that model size and inference strategy are substitutes"
    ],
    "relevance_to_seed": "Provides foundational evidence that inference compute allocation matters and establishes the aggregate scaling law methodology that our per-instance adaptive framework explicitly extends with verification depth as a new dimension."
  },
  {
    "title": "Variation in Verification: Understanding Verification Dynamics in Large Language Models",
    "venue": "ICLR 2026",
    "problem_identification": "Verification effectiveness was treated as a static property of the verifier model, but how it varies across problem difficulty, generator capability, and verifier capability was never systematically characterized — obscuring when and why verification helps.",
    "key_insight": "Problem difficulty governs True Positive Rate (verifier reliability on correct answers), generator capability determines True Negative Rate (error detectability), and strategic weak-generator/strong-verifier pairing can close 75.7% of the performance gap to stronger generators.",
    "innovation_type": "analysis",
    "method_summary": "Studies generative verifiers (CoT reasoning + binary verdict) across 14 open-source models (2B-72B) plus GPT-4o on 12 benchmarks spanning math, knowledge, and NL reasoning. Uses 64 samples per problem for capability estimation and 8 balanced responses (4 correct, 4 incorrect) per verifier evaluation. Decomposes verification into TPR and TNR to isolate difficulty and generator effects, revealing that weak generators produce easier-to-detect errors.",
    "limitations_and_open_questions": "Only studies generative verifiers — discriminative ORMs/PRMs may show different dynamics. Provides descriptive analysis without prescribing how to adaptively select verification strategy per-instance based on these dynamics.",
    "building_blocks": [
      "TPR/TNR decomposition of verification effectiveness",
      "Difficulty-dependent verification characterization across 12 benchmarks",
      "Strategic model pairing framework",
      "Empirical evidence that verification benefit varies dramatically per-instance"
    ],
    "relevance_to_seed": "Most directly validates our core hypothesis — verification effectiveness varies dramatically with difficulty and model pairing, providing the empirical grounding that per-instance verification depth selection should yield large gains over fixed strategies."
  },
  {
    "title": "Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier",
    "venue": "arXiv 2025 (submitted to ICLR 2026, withdrawn)",
    "problem_identification": "GenRMs are computationally prohibitive while token-efficient 'NoThinking' verification drops error precision to 39-56%. No system dynamically allocates between fast and slow verification based on instance difficulty.",
    "key_insight": "RL-trained fast thinking mode (GRPO on only 1,526 samples) can be reliable enough for most verification instances; consensus-based escalation — measuring agreement among k parallel fast probes — gates expensive slow thinking only when fast assessments disagree, achieving both efficiency and accuracy.",
    "innovation_type": "combination",
    "method_summary": "FlexiVe uses GRPO with a composite reward (correctness + length penalty) to train a dual-mode verifier: fast mode (27-40x fewer tokens via NoThinking template) and slow mode (full deliberation). Flexible allocation runs k fast verifications, computes agreement ratio R = max_i(a_i)/k, and escalates to slow mode only when R < τ. The SDV pipeline adds hesitation-keyword detection with log-probability completeness checks to identify solution endpoints early, triggering targeted verification and feedback-guided refinement.",
    "limitations_and_open_questions": "Only evaluated on math benchmarks; k and τ are empirically set without automated tuning; only two verification depths (fast/slow) rather than a richer hierarchy. Withdrawn from ICLR 2026 — reasons unclear but may indicate reviewer concerns.",
    "building_blocks": [
      "GRPO-trained dual-mode verification",
      "Consensus-based escalation from fast to slow verification",
      "Hesitation keyword + log-probability detection of solution completeness",
      "Feedback-guided single-round refinement"
    ],
    "relevance_to_seed": "FlexiVe's binary fast/slow allocation is a special case of our multi-depth hierarchy (none/ORM/PRM/GenRM); their consensus-based difficulty estimation is a candidate signal for our online difficulty estimator, and their hesitation detection directly relates to our early-token difficulty signals."
  },
  {
    "title": "Trust but Verify! A Survey on Verification Design for Test-time Scaling",
    "venue": "arXiv 2025",
    "problem_identification": "The verification landscape for test-time scaling was fragmented across isolated works with no unified taxonomy — researchers lac
... (truncated)

## Your task

Synthesize these paper analyses into a **Field Guide** — a strategic document that would help a researcher generate novel, high-quality ideas in this area. This is NOT a survey — it's an opinionated strategy guide for innovation.

Think about:
- What PATTERNS OF INNOVATION keep working in this field?
- What do reviewers consistently reward?
- Where are the real gaps (not assumed gaps)?
- What combinations haven't been tried?
- What mistakes should we avoid?

## Output format

Output a JSON object with these sections:
{
  "innovation_patterns": [
    {"pattern": "name", "description": "how it works", "examples": ["paper1", "paper2"], "success_rate": "high/medium/low"}
  ],
  "reviewer_preferences": [
    "What reviewers in this area consistently care about (based on evidence from paper analyses)"
  ],
  "field_gaps": [
    {"gap": "description of unsolved problem", "evidence": "which papers mention this limitation", "difficulty": "high/medium/low", "impact_if_solved": "high/medium/low"}
  ],
  "untried_combinations": [
    {"idea_sketch": "what could be combined", "from_papers": ["which papers inspire this"], "why_promising": "reason"}
  ],
  "method_building_blocks": [
    {"tool": "name", "what_it_does": "description", "used_by": ["papers"], "could_be_applied_to": "new application"}
  ],
  "common_pitfalls": [
    "Mistakes to avoid when working in this area (based on reviewer feedback and paper limitations)"
  ],
  "field_trajectory": "Where is this field heading? What are the 2-3 most promising macro-directions? (paragraph)",
  "meta_advice": "If you were advising a PhD student to write a strong 2026 paper in this area, what would you tell them? (paragraph)"
}

Be specific and evidence-based — every claim should reference specific papers from the analyses. Avoid generic advice like 'be novel' — instead say 'Papers that combine X with Y for task Z have been getting accepted (see Paper A, Paper B).'.

IMPORTANT: You MUST end your response with the JSON object.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a3f1dfa5-f6b0-456f-b72a-b1ac5445e1a6",
  "type": "user",
  "uuid": "811542b2-9c4f-4302-81c5-43c3fecdf19b",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "16d354d1-0aea-44ae-a93e-7ed499be64b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T05:34:07.364Z_

```json
{
  "parentUuid": "811542b2-9c4f-4302-81c5-43c3fecdf19b",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
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
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
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
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "cf3d061a-1f62-4133-a498-64128c5fcd9c",
  "timestamp": "2026-05-29T05:34:07.364Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "16d354d1-0aea-44ae-a93e-7ed499be64b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T05:34:07.364Z_

```json
{
  "parentUuid": "cf3d061a-1f62-4133-a498-64128c5fcd9c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "529ff03e-893b-48bc-ab8c-90398fd7d587",
  "timestamp": "2026-05-29T05:34:07.364Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "16d354d1-0aea-44ae-a93e-7ed499be64b1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-29 (UTC).**  ## Research area: Target: AAAI 2026 Track: Machine Lea…",
  "leafUuid": "529ff03e-893b-48bc-ab8c-90398fd7d587",
  "sessionId": "16d354d1-0aea-44ae-a93e-7ed499be64b1"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Adaptive verification depth for efficient reasoning",
  "sessionId": "16d354d1-0aea-44ae-a93e-7ed499be64b1"
}
```

---

### Assistant

_source line 8 · 2026-05-29T05:34:28.742Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to synthesize 20 paper analyses into a strategic "Field Guide" for research in the area of efficient inference and reasoning, specifically around per-instance adaptive co-optimization of generation and verification compute. Let me carefully analyze all the papers and produce a comprehensive, evidence-based JSON output.

Let me organize my thinking:

**Innovation Patterns:**
1. "New formulation" - recasting existing problems with a new lens (Snell et al., Zhang et al., GenRM, Meta-RL, VG-Search, provable scaling laws, PAVs) - very common and successful


2. "Budget-aware comparison" - revealing that prior results depend on unfair compute allocations (Singhi et al., Budget-aware verification)
3. "Early-signal exploitation" - leveraging early tokens or layers to predict final outcomes (ST-BoN, Deep-thinking tokens, DiffAdapt)
4. "Generative verification" - treating verification itself as a generation problem (GenRM, ThinkPRM, GenPRM)
5. "Adaptive allocation" - routing decisions based on per-instance or per-difficulty characteristics (Snell et al., DiffAdapt, FlexiVe, OSCA)
6. "Analysis papers revealing variance" - demonstrating that effectiveness varies significantly across instances and difficulty levels (Variation in Verification, Singhi et al.)

The field seems to value iso-compute comparisons, multi-domain benchmarking, practical algorithms grounded in theory, and clear quantification of efficiency improvements. Key gaps include the lack of per-instance verification depth selection, joint optimization of verification parameters, cross-domain method evaluation, and cheap online difficulty estimation. There are also several unexplored combinations worth investigating: combining routing features with verification depth, using progress signals for difficulty-based gating, pessimistic verification with adaptive depth, and tournament aggregation with adaptive verification.

Now I'm identifying the core building blocks I can draw from—cost-of-effort features, deep-thinking token metrics, lightweight difficulty probes, progress rewards, pessimistic verification approaches, relative position embeddings, and granularity parameters—to construct a comprehensive field guide grounded in evidence.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "529ff03e-893b-48bc-ab8c-90398fd7d587",
  "isSidechain": false,
  "requestId": "req_011CbWKFTKsC6ncP1K9kzh5y",
  "type": "assistant",
  "uuid": "11f28e00-a54b-4931-8661-f3c5429f98d8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "16d354d1-0aea-44ae-a93e-7ed499be64b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EB3NxPdiAk1MjMpCBNbPPD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12857,
      "cache_read_input_tokens": 11014,
      "output_tokens": 7911,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12857,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 7911,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 12857,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12857
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

_source line 9 · 2026-05-29T05:37:25.294Z_

I'll analyze the 20 papers systematically to produce this field guide. Let me first review the key details more carefully to ensure evidence-based claims.

```json
{
  "innovation_patterns": [
    {
      "pattern": "Iso-compute Reframing",
      "description": "Take a method that looks superior in accuracy-only comparisons, show that under a unified compute budget (FLOPs, tokens, or wall-clock), the advantage shrinks or reverses. Then propose a budget-aware alternative. This works because reviewers love 'the emperor has no clothes' narratives grounded in fair comparison.",
      "examples": ["Singhi et al. (COLM 2025) — GenRM vs SC under iso-FLOPs", "Budget-aware Verification (arXiv 2025) — discriminative vs generative at equal budget", "VG-Search (NeurIPS 2025) — beam search vs BoN on a cost continuum"],
      "success_rate": "high"
    },
    {
      "pattern": "Recasting Verification as Generation",
      "description": "Replace discriminative classification (scalar reward) with generative reasoning (CoT before judgment). This unlocks test-time compute scaling for the verifier itself (sample more rationales → better judgment) and improves out-of-domain generalization. The pattern recurs across GenRM, ThinkPRM, and GenPRM, all achieving strong results.",
      "examples": ["GenRM (ICLR 2025) — MajV@K via CoT rationale sampling", "ThinkPRM (arXiv 2025) — long-CoT generative PRM outperforms discriminative with 1% data", "GenPRM (AAAI 2026) — CoT+code verification with RPE labels"],
      "success_rate": "high"
    },
    {
      "pattern": "Early-Signal Exploitation",
      "description": "Extract predictive features from the first few tokens or layers of generation — before the full solution is committed — to make allocation decisions. This saves compute by avoiding generating, then evaluating, then discarding. The signal sources vary (hidden-state curvature, entropy, layer-wise JSD) but the pattern is consistent: internal representations at early decoding steps carry strong quality/difficulty signals.",
      "examples": ["ST-BoN (NeurIPS 2025) — CoE curvature from early divergence point", "Deep-Thinking Tokens (arXiv 2026) — DTR from 50-token prefixes", "DiffAdapt (ICLR 2026) — MLP probe on final hidden states pre-generation"],
      "success_rate": "high"
    },
    {
      "pattern": "Formalize-Then-Optimize",
      "description": "Take a practice that is done heuristically (e.g., choosing N in Best-of-N, selecting temperature, setting verification frequency), formulate it as a clean optimization problem (often convex or decomposable), prove a structural property (convexity, monotonicity, scaling law), then derive an algorithm. Papers that provide both the formulation and the algorithm get top venues; analysis-only papers still publish but at lower impact.",
      "examples": ["OSCA (NAACL 2025) — convex config mixture optimization", "InferenceTimePessimism (ICML 2025) — pessimistic rejection with scaling-monotonic guarantee", "Provable Scaling Laws (NeurIPS 2025) — tournament aggregation with exponential decay bounds"],
      "success_rate": "high"
    },
    {
      "pattern": "Difficulty-Stratified Analysis → Adaptive Method",
      "description": "First show that a quantity of interest (verification effectiveness, optimal strategy, compute efficiency) varies dramatically across difficulty levels. Then build an adaptive method that exploits this variance. The analysis step is essential for motivating the adaptive method and is often the most cited contribution. Papers that stop at analysis still publish but at lower-tier venues or as workshop papers.",
      "examples": ["Snell et al. (ICLR 2025 Oral) — strategy varies by difficulty → cross-validated routing", "Variation in Verification (ICLR 2026) — TPR/TNR varies by difficulty but no adaptive algorithm proposed", "DiffAdapt (ICLR 2026) — U-shaped entropy → MLP probe routing"],
      "success_rate": "high"
    },
    {
      "pattern": "Dual-Mode Escalation",
      "description": "Design a fast/cheap default path and an expensive fallback, then use a lightweight signal (consensus, confidence, entropy) to gate escalation. This is cheaper than always running the expensive path and more accurate than always running the cheap path. FlexiVe and DiffAdapt both use this but only with binary modes — extending to multi-level hierarchies is the obvious next step.",
      "examples": ["FlexiVe/SDV (arXiv 2025) — fast/slow verification gated by consensus ratio", "DiffAdapt (ICLR 2026) — Easy/Normal/Hard routing via MLP probe"],
      "success_rate": "medium"
    }
  ],

  "reviewer_preferences": [
    "Iso-compute comparisons are essentially mandatory for top venues in this area. Both Singhi et al. (COLM 2025) and Budget-aware Verification explicitly built their contributions around fair FLOP-normalized comparison, and Snell et al. (ICLR 2025 Oral) normalized by compute budget. Papers that claim method A beats method B without controlling compute are increasingly rejected.",
    "Multi-domain evaluation across at least 2 domains (math + code, or math + science) is expected. Singhi et al. evaluated on MATH, AIME, GPQA, LiveCodeBench; Snell et al. used MATH-500 and subsets. Papers evaluated only on MATH/GSM8K face domain-generality objections — GenPRM (AAAI 2026) was noted as having unclear cross-domain transfer despite strong math results.",
    "Practical algorithms that a practitioner can implement, not just scaling law fits or analytical results. Singhi et al.'s limitation (acknowledged in seed gap analysis) is that their scaling laws are descriptive, not prescriptive — there is no online algorithm. Variation in Verification (ICLR 2026) provides analysis without an algorithm and published as analysis rather than a methods paper. Contrast with Snell et al., which provides a deployable cross-validated strategy selector and got an Oral.",
    "Quantified compute savings in concrete units (tokens, FLOPs, GPU-hours, latency). ST-BoN reports >80% GPU memory reduction and 50% latency reduction; DiffAdapt reports 22.4% token reduction; Budget-aware Verification quantifies 0.1% vs 238% latency overhead. Vague claims of 'improved efficiency' without numbers are insufficient.",
    "Theoretical grounding paired with empirical validation. The strongest papers (InferenceTimePessimism at ICML 2025, Provable Scaling Laws at NeurIPS 2025, Setlur et al. at ICML 2025 Spotlight) prove formal bounds and then validate empirically. Pure theory without experiments or pure experiments without theoretical insight both fall short of oral/spotlight status.",
    "Addressing 'when does it help and when does it hurt' rather than just average gains. Snell et al. explicitly characterized the difficulty regions where each strategy dominates. Singhi et al. showed GenRM helps only on hard problems. Reviewers increasingly expect failure mode analysis, not just cherry-picked improvements."
  ],

  "field_gaps": [
    {
      "gap": "No method jointly optimizes generation count K and verification depth d per-instance under a shared compute budget",
      "evidence": "Singhi et al. optimize the S/V ratio but aggregate across all problems and only compare SC vs GenRM (binary). OSCA (Zhang et al.) optimizes configuration mixtures but offline across a dataset. VG-Search optimizes verification granularity but not depth. Budget-aware Verification fixes the strategy. No existing work treats (K, d) as coupled per-instance decision variables.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Online difficulty estimation that is cheap, reliable, and causally validated across domains",
      "evidence": "DiffAdapt's MLP probe is trained only on math (DeepMath-103K) with unclear cross-domain transfer. ST-BoN's CoE requires white-box access and uses a fixed buffer window. Deep-Thinking Tokens' DTR uses empirical thresholds (ρ=0.85, 50-token prefix) without cross-architecture sensitivity analysis. No method has demonstrated a unified difficulty estimator that works across math, code, and science with quantified estimation cost.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Per-instance verification depth selection across a continuum (none → ORM → PRM → GenRM)",
      "evidence": "FlexiVe uses binary fast/slow. DiffAdapt uses three discrete difficulty levels mapped to reasoning length, not verification depth. Variation in Verification (ICLR 2026) empirically shows TPR/TNR vary dramatically by difficulty but proposes no adaptive algorithm. The survey (Trust but Verify) notes fragmentation but offers no unifying allocation framework.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Provable approximation guarantees for adaptive verification allocation under verifier imperfection",
      "evidence": "InferenceTimePessimism (ICML 2025) proves scaling-monotonic guarantees but only for outcome-level BoN, not multi-depth verification. Provable Scaling Laws (NeurIPS 2025) gives exponential decay bounds for tournament aggregation but assumes fixed p_comp. Setlur et al. prove VB vs VF separation but don't address adaptive depth selection. No existing theoretical result bounds the regret of an adaptive (K, d) allocation policy relative to the oracle policy.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "Cost-accuracy Pareto curves for verification depth across domains and model scales",
      "evidence": "Budget-aware Verification quantifies cost ratios (discriminative=2% vs generative=76x of generation FLOPs) but only for math. PAVs (Setlur et al.) provide accuracy-compute tradeoffs for PRM vs ORM but only on math. ThinkPRM shows accuracy scales with thinking length but doesn't characterize the cost-accuracy curve across depths. No paper provides a systematic c_v(d) characterization across verification types, domains, and model scales.",
      "difficulty": "low",
      "impact_if_solved": "medium"
    },
    {
      "gap": "Interaction between verification depth adaptation and reward hacking / overoptimization",
      "evidence": "InferenceTimePessimism (ICML 2025) shows BoN hits overoptimization at large N due to RM imperfection. Singhi et al. note GenRM advantages are strongest on hard problems where verifiers are least reliable. No work addresses whether per-instance depth selection amplifies or mitigates reward hacking — deeper verification on harder problems may increase overoptimization risk precisely where accuracy matters most.",
      "difficulty": "high",
      "impact_if_solved": "medium"
    }
  ],

  "untried_combinations": [
    {
      "idea_sketch": "Use Deep-Thinking Ratio (DTR) from 50-token prefixes as a per-instance difficulty signal to route problems through a verification depth hierarchy (none → ORM → PRM → GenRM), jointly selecting K via the bilinear cost decomposition K* = B/(c_g + c_v(d*))",
      "from_papers": ["Deep-Thinking Tokens (arXiv 2026)", "Singhi et al. (COLM 2025)", "Budget-aware Verification (arXiv 2025)"],
      "why_promising": "DTR is the only difficulty metric with positive correlation to actual reasoning effort (r=0.683 vs r=-0.594 for length), is extractable from just 50 tokens, and has been validated for sample filtering (Think@n). Combining it with Singhi et al.'s cost model and Budget-aware Verification's concrete cost ratios gives all components needed for a practical online algorithm. The bilinear cost structure ensures tractable optimization once DTR maps to d*."
    },
    {
      "idea_sketch": "Combine Meta-RL's progress reward (Δ success probability per episode) with FlexiVe's consensus-based escalation to create a multi-level verification cascade that escalates not just fast→slow but through none→ORM→PRM→GenRM, with escalation triggered by low cumulative progress in early episodes",
      "from_papers": ["Meta-RL Fine-Tuning (ICML 2025)", "FlexiVe/SDV (arXiv 2025)", "ThinkPRM (arXiv 2025)"],
      "why_promising": "Progress reward gives a continuous, mechanistically meaningful difficulty signal (how much is the model actually learning from its reasoning) rather than a static feature. FlexiVe's consensus gating generalizes naturally to multi-level escalation. ThinkPRM provides the expensive top tier. The combination creates a dynamic, multi-stage pipeline where verification cost is committed incrementally based on evidence of need."
    },
    {
      "idea_sketch": "Apply InferenceTimePessimism's per-prompt threshold mechanism to select verification depth d* rather than just filter samples — compute pessimistic scores at each verification depth and select the minimum depth where the pessimistic score stabilizes, providing a principled 'sufficient verification' criterion",
      "from_papers": ["InferenceTimePessimism (ICML 2025)", "VG-Search (NeurIPS 2025)", "PAVs (ICLR 2025)"],
      "why_promising": "InferenceTimePessimism already computes per-prompt thresholds and has scaling-monotonic guarantees. VG-Search showed that verification redundancy is massive (>50% consecutive PRM score deltas < 1% of range), suggesting that a 'sufficient depth' criterion would save substantial compute. PAVs' advantage-based PRM provides calibrated step-level signals for the stabilization check. This combination yields both a practical algorithm and provable guarantees."
    },
    {
      "idea_sketch": "Train a single generative verifier (à la GenPRM) with a controllable 'thinking budget' parameter that maps to verification depth — at inference time, allocate thinking budget per-instance using DiffAdapt's hidden-state probe, creating a continuous verification depth spectrum rather than discrete modes",
      "from_papers": ["GenPRM (AAAI 2026)", "DiffAdapt (ICLR 2026)", "ThinkPRM (arXiv 2025)"],
      "why_promising": "ThinkPRM showed accuracy monotonically increases with thinking length. DiffAdapt showed hidden-state probes can predict required reasoning effort pre-generation. GenPRM showed generative PRMs can be trained data-efficiently (23K samples). A single model with a continuous depth knob is cleaner than managing four separate verifiers and avoids the discrete hierarchy's boundary effects."
    },
    {
      "idea_sketch": "Combine ST-BoN's Chain-of-Embedding (CoE) features with PAVs' process advantage signals to create a two-phase filtering pipeline: CoE at early tokens prunes obviously bad candidates (free tier), then PAV scores at intermediate steps rank survivors (PRM tier), with GenRM reserved only for the top-k candidates on which PAV scores are ambiguous",
      "from_papers": ["ST-BoN (NeurIPS 2025)", "PAVs (ICLR 2025)", "GenRM (ICLR 2025)"],
      "why_promising": "Each method operates at a different cost point and captures different quality signals (latent trajectory consistency, step-level progress, holistic solution reasoning). The pipeline leverages the natural compute hierarchy: CoE is near-free (hidden state access at one token), PAV adds modest cost (step-level scoring), GenRM adds heavy cost (full CoT verification). This creates the practical multi-depth allocation that no single paper achieves."
    }
  ],

  "method_building_blocks": [
    {
      "tool": "Chain-of-Embedding (CoE) curvature metric",
      "what_it_does": "Extracts hidden states across all L layers at early divergence points, forms a trajectory H = h₀→...→h_L, and scores samples by curvature distance to peers. Enables sample quality prediction from just ~c early tokens without running a reward model.",
      "used_by": ["ST-BoN (NeurIPS 2025)"],
      "could_be_applied_to": "Lightweight difficulty estimation for verification depth routing — CoE curvature variance across K samples could signal problem difficulty (high variance = hard = needs deeper verification) at near-zero additional cost since hidden states are already computed during generation."
    },
    {
      "tool": "Deep-Thinking Ratio (DTR)",
      "what_it_does": "Measures the fraction of tokens where predictions undergo significant revision in deeper layers (JSD between intermediate and final layer distributions exceeding a settling threshold). Extractable from 50-token prefixes with positive correlation to reasoning effort (r=0.683).",
      "used_by": ["Deep-Thinking Tokens (arXiv 2026)"],
      "could_be_applied_to": "Primary input feature for the online (K, d) allocator — DTR from short prefixes can drive difficulty-based routing before any verification compute is committed. Could also calibrate the expected benefit of each verification depth tier."
    },
    {
      "tool": "Progress reward / process advantage",
      "what_it_does": "Measures the change in success probability before and after a reasoning step (advantage-based, not Q-value-based). Isolates step-level contribution from inherited state quality. Can be automatically labeled using a complementary prover policy (Best-of-4 optimal).",
      "used_by": ["Meta-RL Fine-Tuning (ICML 2025)", "PAVs (ICLR 2025)"],
      "could_be_applied_to": "Online difficulty estimation during generation — if cumulative progress is low after k steps, the problem is likely hard and should be escalated to deeper verification. Also provides dense training signal for learning the difficulty estimator itself."
    },
    {
      "tool": "Pessimistic rejection sampling with per-prompt threshold",
      "what_it_does": "Computes per-prompt threshold λ̂(x) satisfying a normalization constraint, then accepts samples via pessimistic weights w(y) = relu(β⁻¹(r̂(x,y)−λ̂(x))). Implements χ²-divergence regularization through rejection sampling with provable scaling-monotonic guarantees.",
      "used_by": ["InferenceTimePessimism (ICML 2025)"],
      "could_be_applied_to": "Verification depth selection with theoretical guarantees — the per-prompt threshold already captures instance difficulty; extending it to select among multiple verification depths (each with its own reward model r̂_d) while maintaining scaling-monotonicity would provide the provable guarantees our framework needs."
    },
    {
      "tool": "Consensus-based escalation",
      "what_it_does": "Runs k cheap verifications in parallel, computes agreement ratio R = max_i(a_i)/k, and escalates to expensive verification only when R < τ. Provides a principled, threshold-based mechanism for conditional compute allocation.",
      "used_by": ["FlexiVe/SDV (arXiv 2025)"],
      "could_be_applied_to": "Multi-level verification cascade — generalize from binary (fast/slow) to multi-level (none/ORM/PRM/GenRM) by computing escalation criteria at each level, stopping when consensus is reached. The agreement ratio at each level also provides a running difficulty estimate."
    },
    {
      "tool": "Unified compute cost model C(S,V) = S·(1 + λV)",
      "what_it_does": "Normalizes generation and verification compute into a single budget by accounting for the token cost ratio λ between generation and verification. Enables fair strategy comparison and optimal ratio derivation via power-law fitting.",
      "used_by": ["Singhi et al. (COLM 2025)"],
      "could_be_applied_to": "Foundation of the bilinear cost decomposition in our framework — extending to C(K,d) = K·(c_g + c_v(d)) where c_v(d) is parameterized across the depth hierarchy using cost ratios from Budget-aware Verification (discriminative=2%, generative=76x)."
    },
    {
      "tool": "Granularity parameter g unifying beam search and BoN",
      "what_it_does": "A single tunable parameter creating a continuous spectrum between beam search (g=1, verify every step) and Best-of-N (g=L, verify only at end), with closed-form compute cost model revealing verification overhead as a function of g.",
      "used_by": ["VG-Search (NeurIPS 2025)"],
      "could_be_applied_to": "Adding a second continuous axis (granularity g) to our depth hierarchy — instead of discrete (none/ORM/PRM/GenRM), parameterize as (depth d, granularity g) creating a 2D verification strategy space that can be searched per-instance."
    },
    {
      "tool": "MLP probe on hidden states for difficulty classification",
      "what_it_does": "A two-layer MLP trained on final-layer hidden states (300 problems/level, AdamW, 100 epochs) to classify Easy/Normal/Hard before generation begins. Achieves 22.4% token reduction via pre-generation strategy routing.",
      "used_by": ["DiffAdapt (ICLR 2026)"],
      "could_be_applied_to": "Pre-generation verification depth routing — extend from 3 difficulty classes to continuous difficulty scores, and from reasoning-length adaptation to verification-depth selection. The probe architecture is lightweight enough to add negligible overhead to the inference pipeline."
    }
  ],

  "common_pitfalls": [
    "Claiming novelty on the generation-verification tradeoff itself. Singhi et al. (COLM 2025) already established this comprehensively. The contribution must be explicitly framed as extending their aggregate analysis to per-instance multi-depth allocation — any framing that implies 'first to study' this tradeoff will be desk-rejected by reviewers familiar with the field.",
    "Evaluating only on math benchmarks. GenPRM (AAAI 2026), PAVs (ICLR 2025), Provable Scaling Laws (NeurIPS 2025), and FlexiVe all have this limitation explicitly noted. Reviewers increasingly require cross-domain validation — MATH+AIME is not enough; must include code (LiveCodeBench, HumanEval) and science (GPQA, ScienceQA) at minimum.",
    "Ignoring the simple baseline threat. DiffAdapt's limitation section flags that 'a simple token-length threshold may capture much of the gain.' The seed paper's own self-check identifies this as a REAL RISK: if a simple heuristic (e.g., always use PRM for problems with solutions > X tokens) achieves 80% of the adaptive method's gain, the paper is dead. Must include ablations against simple rules (length threshold, entropy threshold, random allocation) and demonstrate statistically significant margins.",
    "Using accuracy-only comparisons without compute normalization. Singhi et al.'s central contribution was showing GenRM's apparent superiority was an artifact of ignoring verification cost. Budget-aware Verification showed 76x FLOP overhead of generative verification. Any comparison that doesn't control for total FLOPs/tokens/wall-clock will be immediately questioned.",
    "Treating verification depth as a fixed taxonomy when it's actually model-dependent. Variation in Verification (ICLR 2026) showed that TPR/TNR dynamics depend on both generator capability and verifier capability. A 2B GenRM may be cheaper and worse than a 70B ORM — the depth hierarchy (none < ORM < PRM < GenRM) is an approximation that may not hold across all model pairings.",
    "Over-engineering the difficulty estimator without accounting for its cost. Snell et al. (ICLR 2025) acknowledged that difficulty estimation cost is not fully accounted in compute budgets. DiffAdapt requires sampling to estimate PRM scores. If the estimator costs 10% of the budget, it must save >10% through better allocation. Always include estimator overhead in the total compute accounting.",
    "Assuming independence of samples when it doesn't hold. OSCA (NAACL 2025) explicitly assumes independent sampling which ignores sequential refinement. Meta-RL (ICML 2025) showed within-model reasoning has episode structure. Papers that model K independent samples but use temperature-based sampling (which creates correlated outputs) will overestimate coverage gains.",
    "Withdrawing or not submitting to the right venue. Both ThinkPRM and FlexiVe were withdrawn from ICLR 2026 — timing and venue selection matter. AAAI 2026 ML track reviewers expect clear algorithmic contributions with strong baselines; pure analysis or incremental extensions of existing frameworks risk rejection."
  ],

  "field_trajectory": "The field is converging on three macro-directions. First, **unified test-time compute allocation frameworks** that jointly optimize all inference-time decisions (how many samples, which models, what verification strategy, how much reasoning) under a single compute budget — the current fragmented approach where each decision is optimized independently is clearly suboptimal, and the community recognizes this (see the survey 'Trust but Verify' and the progression from Snell et al. → Singhi et al. → OSCA → VG-Search, each adding a new dimension). Second, **mechanistic difficulty estimation from internal representations** is maturing rapidly — within 12 months we've seen CoE curvature (ST-BoN), entropy patterns (DiffAdapt), DTR (Deep-Thinking Tokens), and progress rewards (Meta-RL/PAVs), all demonstrating that LLMs already 'know' how hard a problem is before committing full compute. The winning approach will likely fuse multiple signals (hidden states, entropy trajectories, early-token consistency) into a single cheap estimator. Third, **generative verification with controllable cost** is replacing the discrete verifier taxonomy — ThinkPRM and GenPRM both show that generative verifiers can be scaled continuously by controlling thinking length, collapsing the none/ORM/PRM/GenRM hierarchy into a single model with a tunable cost knob. The intersection of these three trends — a unified allocator using mechanistic difficulty signals to control a continuous-cost generative verifier — is the likely shape of top papers in 2026-2027. The theoretical foundations are being laid simultaneously (InferenceTimePessimism, Provable Scaling Laws, Setlur et al.'s VB/VF separation) and the winning empirical papers will combine practical algorithms with at least approximate guarantees.",

  "meta_advice": "If I were advising a PhD student targeting AAAI 2026 ML track with this research direction, here is what I would say. **Start with the cost model, not the algorithm.** The bilinear decomposition (P(correct) depends on coverage from K and precision from d, cost is K·(c_g + c_v(d))) is your paper's backbone — prove it admits a clean optimization, ideally with an approximation guarantee. Singhi et al. showed the field cares deeply about compute-fair comparison, so your theoretical anchor must be airtight. **Pick your difficulty signal carefully and ablate ruthlessly.** You have at least four candidates (DTR, CoE, entropy probe, progress reward), and your contribution is the allocation algorithm, not the signal itself — so pick the cheapest one that works (DTR from 50-token prefixes is the current best candidate at ~2% overhead) and show that the allocation framework is signal-agnostic via ablations with different estimators. **The baseline fear is your biggest risk.** Before writing the paper, run the experiment: implement a simple 3-rule heuristic (e.g., 'use SC for problems where the first sample's entropy < τ₁, PRM for τ₁ ≤ entropy < τ₂, GenRM otherwise') and measure the gap to your learned allocator. If the gap is <5% absolute, either your problem formulation needs refinement or the variance isn't as exploitable as hypothesized. This experiment should happen in week 1, not week 12. **Evaluation must span 4+ benchmarks across math, code, and science** (MATH-500, AIME'24, LiveCodeBench, GPQA-Diamond is the minimum credible set — add ScienceQA or ARC-Challenge for breadth). Use Singhi et al.'s multi-model protocol (at least two model families, e.g., Qwen-2.5-7B and Llama-3.x-8B). **Frame explicitly as extending Singhi et al.** — your abstract should say 'Singhi et al. established aggregate scaling laws for the generation-verification tradeoff; we extend to per-instance, multi-depth allocation with an online algorithm.' This positions you as building on established work rather than competing with it, which reviewers prefer. **Budget your 200 H100-hours carefully**: ~40 hours for difficulty estimator training and calibration, ~80 hours for main experiments (2 models × 4 benchmarks × multiple (K,d) configurations), ~40 hours for ablations and baselines, ~40 hours buffer. Finally, **include a failure analysis**: show cases where your adaptive allocation makes worse decisions than the fixed aggregate-optimal baseline, explain why (e.g., difficulty estimation errors, verifier miscalibration on novel problem types), and quantify the failure rate. This demonstrates intellectual honesty that reviewers reward and preempts the 'when does it fail?' question."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11f28e00-a54b-4931-8661-f3c5429f98d8",
  "isSidechain": false,
  "requestId": "req_011CbWKFTKsC6ncP1K9kzh5y",
  "type": "assistant",
  "uuid": "72b9328c-2b93-4afb-9ef2-733b5c482ec1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "16d354d1-0aea-44ae-a93e-7ed499be64b1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EB3NxPdiAk1MjMpCBNbPPD",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12857,
      "cache_read_input_tokens": 11014,
      "output_tokens": 7911,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12857,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 7911,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 12857,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12857
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

_source line 10_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-29 (UTC).**  ## Research area: Target: AAAI 2026 Track: Machine Lea…",
  "leafUuid": "72b9328c-2b93-4afb-9ef2-733b5c482ec1",
  "sessionId": "16d354d1-0aea-44ae-a93e-7ed499be64b1"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Adaptive verification depth for efficient reasoning",
  "sessionId": "16d354d1-0aea-44ae-a93e-7ed499be64b1"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-29 (UTC).**  ## Research area: Target: AAAI 2026 Track: Machine Lea…",
  "leafUuid": "72b9328c-2b93-4afb-9ef2-733b5c482ec1",
  "sessionId": "16d354d1-0aea-44ae-a93e-7ed499be64b1"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Adaptive verification depth for efficient reasoning",
  "sessionId": "16d354d1-0aea-44ae-a93e-7ed499be64b1"
}
```

---
