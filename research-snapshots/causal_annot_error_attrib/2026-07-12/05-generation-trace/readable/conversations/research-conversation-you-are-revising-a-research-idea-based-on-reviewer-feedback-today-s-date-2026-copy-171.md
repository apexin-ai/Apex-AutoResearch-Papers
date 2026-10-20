# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-28 (UTC).** ## Original idea { "tit

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 42
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/6c159ebd-d2a0-4490-8925-9988ef96dbff.jsonl`
- **Structured JSON:** [`cbfb747c11a38bfabeee.json`](../../sessions/cb/cbfb747c11a38bfabeee.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T01:43:06.336Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T01:43:06.336Z",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-28 (UTC).**\n\n## Original idea\n{\n  \"title\": \"CRISP-PRM: Criticality-Aware Step-Level Paradigm Selection for Unified Process Reward Models\",\n  \"core_problem\": \"Process reward models face a fundamental accuracy-cost trade-off at the step level: discriminative (fast scalar) verification is cheap (~10ms/step) but unreliable on hard reasoning steps, while generative (CoT) verification is far more accurate but ~100-500x more expensive (~1-5s/step). Dyve (arXiv 2502.11157, EMNLP 2025) demonstrated the feasibility and value of step-level fast/slow paradigm selection within a single model using implicit SFT-based routing, outperforming all contemporaneous baselines (Qwen2.5-Math-7B-PRM800K avg F1 ~41, Skywork-PRM-7B ~35, GPT-4o ~52) with avg F1 ~55.8. However, stronger discriminative PRMs trained with improved data pipelines—notably Qwen2.5-Math-PRM-7B (avg F1 73.5 on ProcessBench, per R-PRM Table 1)—have since surpassed Dyve's adaptive performance using pure discriminative verification. This reveals that implicit SFT-based routing has a ceiling: when the routing mechanism is entangled with the verification itself (learned output length as a proxy for routing), the system cannot benefit from independently improving either the discriminative or generative verification mode. Problem-level routing methods (F/S-RM, E-GRM, CAMEL) achieve efficiency gains but apply uniform verification to every step within a solution, ignoring that steps vary dramatically in difficulty and criticality. ProcessBench data confirms this variation: discriminative PRM error detection accuracy degrades from 72.0% (GSM8K) to 55.2% (OmniMATH) (ProcessBench, arXiv 2412.06559; also R-PRM, arXiv 2503.21295, Table 1). Can a unified dual-mode PRM with explicit, composable step-level paradigm selection—using principled criticality estimation rather than implicit SFT routing—produce better accuracy-per-FLOP Pareto frontiers than both uniform paradigms, problem-level routing, and Dyve's implicit step-level routing, while gracefully composing with future improvements to either verification mode?\",\n  \"opportunity\": \"Three converging developments create a clear opportunity for explicit criticality-based paradigm routing: (1) The maturation of both verification paradigms to strong individual performance. Discriminative PRMs have advanced substantially through improved training pipelines: Qwen2.5-Math-PRM-7B (arXiv 2501.07301) achieves avg F1 73.5 on ProcessBench, a major leap over earlier PRMs like Qwen2.5-Math-7B-PRM800K (avg F1 ~41). Generative PRMs via CoT verification (ThinkPRM, arXiv 2504.16828; GenPRM, arXiv 2504.00891) achieve F1 of 87.3/85.7 on hard subsets—a ~20 F1 point advantage over discriminative PRMs. This means a router can now select between two genuinely strong modes. (2) Dyve demonstrated that step-level paradigm selection is technically feasible and valuable—outperforming all contemporaneous baselines. But its implicit SFT routing conflates when to switch with how to verify, preventing composition with stronger base models. The gap between Dyve (avg F1 55.8) and modern discriminative PRMs (avg F1 73.5) reveals that the bottleneck is the routing mechanism, not the adaptive concept. CRISP-PRM's explicit routing via a lightweight criticality estimator (SCE) is model-agnostic and immediately benefits from advances in either paradigm. (3) Recent work on step-level uncertainty quantification provides validated signals for criticality estimation: CoT Entropy (Ye et al., arXiv 2502.11250) achieves AUROC 0.680 as the best UQ method for generative PRMs; ReProbe/UHeads (arXiv 2511.06209, NeurIPS 2025) provides lightweight step-level uncertainty heads where combining ReProbe scores with PRM scores outperforms either alone; F/S-RM's dual-confidence mechanism (arXiv 2603.20212) demonstrates that multi-signal routing outperforms single-signal. Additionally, Constrained GRPO (arXiv 2602.05863) and Faithful GRPO (arXiv 2604.08476) provide principled frameworks for training with hard quality constraints, enabling the F1 floor guarantee that prevents quality degradation during RL fine-tuning. (4) PURE's min-form credit assignment (arXiv 2504.15275) and CRM's multiplicative survival decomposition (arXiv 2509.26578) prove the weakest step dominates solution quality, implying verification effort should concentrate on critical steps with sequential awareness. (5) VerifySteer (arXiv 2605.20745, May 2026) shows verification compute can be reduced 4-7x through principled intervention at ProcessBench F1 of 72.3, confirming large optimization headroom that is orthogonal to and composable with CRISP-PRM's approach. The unoccupied synthesis is explicit step-level paradigm selection within a unified dual-mode verifier, with composable routing designed to work with modern strong base models—addressing exactly the ceiling that Dyve's implicit approach hits.\",\n  \"landscape\": \"**Discriminative PRMs.** Qwen2.5-Math-PRM-7B (arXiv 2501.07301) is the leading discriminative PRM with ProcessBench F1 of 82.4/77.6/67.5/66.3 across GSM8K/MATH/OlympiadBench/OmniMATH (avg 73.5), as reported in ProcessBench (arXiv 2412.06559, ACL 2025) and independently verified in R-PRM (arXiv 2503.21295, EMNLP 2025, Table 1). Its error detection accuracy (err acc) degrades from 72.0% (GSM8K) to 55.2% (OmniMATH), while correctness accuracy (corr acc) remains relatively stable (96.4% to 83.0%). This represents a major advance over earlier PRMs: Qwen2.5-Math-7B-PRM800K (avg F1 ~41), Skywork-PRM-7B (~35). PRMBench shows discriminative PRMs achieve near-random performance on 'simplicity' error types (redundancy, circular logic). SCAN (arXiv 2509.16548, NeurIPS 2025) provides an efficient data synthesis and noise-tolerant learning framework for PRMs.\\n\\n**Generative PRMs.** ThinkPRM (arXiv 2504.16828, 2025) scales verification compute via extended CoT thinking, achieving F1 of 87.3/85.7 on OlympiadBench/OmniMATH with ThinkPRM-14B—a ~20 F1 point advantage over discriminative PRMs on hard subsets, but at ~100-500x compute cost per step. GenPRM (arXiv 2504.00891, AAAI 2026) shows GenPRM-1.5B outperforms GPT-4o on ProcessBench via code-augmented generative verification.\\n\\n**Step-Level Adaptive Verification (Implicit Routing).** Dyve (arXiv 2502.11157, EMNLP 2025) is the most directly related prior work and the pioneer of step-level paradigm selection. It trains a single DeepSeek-R1-Distill-Qwen-14B via standard cross-entropy SFT on 117K examples to implicitly route between System 1 (single-token '+' confirmation) and System 2 (CoT analysis, up to 8192 tokens). ProcessBench F1: 68.5/58.3/49.0/47.2 (avg ~55.8). Critically, Dyve outperformed ALL contemporaneous baselines at the time of publication: Qwen2.5-Math-7B-PRM800K (avg F1 ~41), Skywork-PRM-7B (~35), Math-Shepherd-PRM-7B (~31), and GPT-4o (~52). However, stronger discriminative PRMs trained with improved data pipelines (Qwen2.5-Math-PRM-7B, avg F1 73.5) have since surpassed Dyve's performance. This reveals a ceiling of implicit routing: (a) the routing decision is entangled with the verification itself (learned output length as proxy), preventing composition with independently improved verifiers; (b) steps are scored independently with no sequential error cascade awareness; (c) standard cross-entropy SFT provides no quality floor guarantee; (d) no separable routing component enables ablation or interpretability. CRISP-PRM builds on Dyve's pioneering insight with explicit, composable routing designed to work with stronger base models.\\n\\n**Step-Level Uncertainty Quantification.** CoT Entropy (Ye et al., arXiv 2502.11250, Feb 2025) introduces a novel UQ method for step-level verification in generative PRMs: it samples multiple reasoning paths at each step, groups outputs by binary correctness decisions, and computes entropy over the marginal distribution: H = −Σ_e(Σ_c p_θ(c,e|x≤t)) log(Σ_c p_θ(c,e|x≤t)). Achieves AUROC 0.680, outperforming all UQ baselines (SEU-MiniLM 0.661, SEU-NV-Embed). Directly relevant to CRISP-PRM's SCE as a candidate signal for estimating when deep verification is most needed. ReProbe/UHeads (arXiv 2511.06209, NeurIPS 2025) provides lightweight step-level uncertainty heads; combining ReProbe scores with PRM scores outperforms either alone.\\n\\n**Problem-Level Fast/Slow Routing.** F/S-RM (arXiv 2603.20212, Mar 2026) trains a single Qwen3-8B with dual fast (first-token scalar) and slow (CoT generation) modes, using dual-confidence activation to route at the problem level; achieves 20.8% token savings but never considers within-solution step variation. E-GRM (arXiv 2604.10072, ACL 2026) routes between direct inference and CoT generation via parallel-decoding consensus at the problem level; 62% latency reduction and 49% FLOP reduction on MATH. CAMEL (arXiv 2602.20670, ICML 2026) uses log-probability confidence gating for pairwise preference judging; problem-level and not PRM-specific.\\n\\n**Step-Level Generation Routing.** TRIM (arXiv 2601.10245, ICLR 2026) performs step-level routing between small and large generation models using PRM-derived uncertainty, achieving 5x cost efficiency on MATH-500; routes generators, not verification paradigms. Demonstrates that step-level routing value persists even as individual models improve.\\n\\n**Verification Compute Optimization.** VerifySteer (arXiv 2605.20745, May 2026) identifies verifier strictness signals in hidden states at paragraph-boundary delimiter tokens and steers verification depth via selective latent interventions. Achieves ProcessBench F1 of 72.3 with Qwen3-8B at 4-7x less inference compute than self-consistency; orthogonal to and composable with fine-tuned verifiers. Adaptive Test-Time Compute (arXiv 2602.03975, Feb 2026) performs state-level selective verification combining deterministic feasibility gating with learned scoring and adaptive allocation, achieving 30% fewer verifier calls on MATH-500. Budget-aware Test-time Scaling (arXiv 2510.14913, 2025) shows discriminative verifiers + self-consistency (Pessimistic Verification) outperform generative verifiers under constrained FLOP budgets.\\n\\n**Constrained RL for Quality Guarantees.** Constrained GRPO (arXiv 2602.05863, Feb 2026) introduces a Lagrangian-based extension of GRPO for constrained policy optimization with indicator cost functions, scalarized advantage construction (preventing standard-deviation mismatch), and learned multipliers. Faithful GRPO (arXiv 2604.08476, Apr 2026) applies this to transform quality metrics from reward terms into hard constraints via Lagrangian dual ascent, reducing inconsistency from 24.5% to 1.7%. Both provide the technical foundation for CRISP-PRM's F1 floor guarantee.\\n\\n**Adaptive Thinking for Generators.** PATS (arXiv 2505.19250, May 2025) introduces process-level adaptive thinking mode switching for generators. Adjusts beam width per step based on PRM scores, achieving near-optimal accuracy at 55% of full-compute token usage. PATS adapts generation depth; CRISP-PRM adapts verification depth—complementary.\\n\\n**Credit Assignment and Error Propagation.** CRM (arXiv 2509.26578, 2025) frames step correctness as a hazard function with multiplicative survival decomposition S(t) = Π(1-h(k)). PURE (arXiv 2504.15275, 2025) introduces min-form credit assignment proving the weakest step dominates. 'Beyond the First Error' (arXiv 2505.14391, 2025) distinguishes error propagation from error cessation.\\n\\n**PRM Calibration.** 'Know What You Don't Know' (arXiv 2506.09338, NeurIPS 2025) demonstrates PRMs are poorly calibrated, overestimating success probability—motivating multi-signal criticality estimation rather than relying on single PRM confidence scores.\\n\\n**Summary.** Dyve pioneered step-level paradigm selection and outperformed all contemporaneous baselines, demonstrating the value of adaptive verification. However, no existing system combines explicit, composable criticality estimation that works with modern strong base models, sequential error cascade awareness, constrained training with F1 floor guarantees, and robustness to changing cost ratios between verification paradigms.\",\n  \"inspired_by\": \"Convergence of five research threads with a critical empirical insight: (1) Dyve (EMNLP 2025) demonstrated that step-level fast/slow verification within a single model is feasible and valuable, outperforming all contemporaneous baselines. The subsequent emergence of stronger discriminative PRMs (Qwen2.5-Math-PRM-7B, avg F1 73.5) that surpass Dyve reveals that implicit routing hits a ceiling—motivating explicit, composable routing. (2) F/S-RM (Mar 2026) proves a single model can support both discriminative and generative modes with dual-confidence routing → provides the architectural foundation. (3) CRM's multiplicative survival decomposition and PURE's min-form credit assignment prove the weakest step dominates → verification effort should be sequentially aware. (4) CoT Entropy (arXiv 2502.11250) achieves best-in-class step-level uncertainty quantification for generative PRMs (AUROC 0.680) → provides validated signal for criticality estimation. (5) Constrained GRPO (arXiv 2602.05863) and Faithful GRPO (arXiv 2604.08476) provide principled frameworks for enforcing quality constraints during RL training → enables the F1 floor guarantee. Pattern: 'Dyve showed the right question (adaptive step verification) and demonstrated its value. The next step requires explicit routing that composes with stronger base models, principled criticality estimation, and constrained training with quality guarantees.'\",\n  \"approach\": \"We propose CRISP-PRM (CRIticality-based Step-level Paradigm selection for Process Reward Models), a framework built on a unified dual-mode verifier that selects the verification paradigm—fast (discriminative) or deep (generative CoT)—for each reasoning step based on estimated step criticality, under a compute budget constraint. Building on Dyve's pioneering demonstration that step-level paradigm selection outperforms contemporaneous baselines, CRISP-PRM introduces explicit, composable routing designed to work with modern strong base models.\\n\\n**Architecture: Unified Dual-Mode PRM**\\n\\nCRISP-PRM uses a single Qwen3-8B model fine-tuned to support both verification modes, following the F/S-RM dual-mode paradigm adapted for step-level process verification:\\n\\n• Fast mode: Given (problem, solution prefix, step_i), the model's first generated token is a correctness judgment ('correct'/'incorrect'). The token probability p(correct|context) serves directly as a scalar step reward. Cost: ~10ms/step (single forward pass). No separate classification head needed—the standard LM head suffices.\\n\\n• Deep mode: A special trigger token is appended to the prompt, bypassing fast judgment and entering CoT verification. The model generates a step-by-step verification rationale inside &lt;verify>...&lt;/verify> tags, then outputs a final correctness judgment. Cost: ~100ms-2s/step depending on model size and generation length.\\n\\n**Training Pipeline: Two-Stage with Constrained RL**\\n\\nStage 1 — SFT Foundation: Combined loss L = L_step + λ·L_action, where L_step is binary cross-entropy on step labels (fast mode) combined with generation loss on synthetic verification CoTs from ThinkPRM-style data (deep mode), and L_action is an action-space constraint penalizing probability leakage to irrelevant tokens during fast mode.\\n\\nStage 2 — Constrained GRPO with F1 Floor: We adopt the Constrained GRPO framework (arXiv 2602.05863) to fine-tune the unified model with a hard F1 floor guarantee—ensuring the model never degrades below the discriminative baseline quality. Concrete specification:\\n\\n(a) Indicator cost function: C_F1(π) = 𝕀[F1_batch(π) < F1_threshold], where F1_threshold is set to the discriminative baseline F1 on a held-out ProcessBench validation split (avg F1 73.5 for Qwen2.5-Math-PRM-7B class models).\\n\\n(b) Lagrangian objective: ℒ(π,λ) = J_R(π) − λ·(J_C(π) − d̃), where J_R is the primary reward (format correctness + outcome accuracy for both fast and deep modes), J_C is the constraint violation rate, and d̃ is the target violation rate (0.05 = at most 5% of validation batches may fall below F1_threshold).\\n\\n(c) Scalarized advantage construction (NOT scalarized rewards, following arXiv 2602.05863 Theorem 4.1 to prevent standard-deviation mismatch): A_ScAdv = λ_R·Z_R − λ_C·Z_C, where Z_j = (Component_j − mean(Component_j))/std(Component_j) are per-component standardized advantages. This preserves the intended trade-off between reward maximization and constraint satisfaction.\\n\\n(d) Multiplier update: ∇_λ ℒ = −(J_C(π) − d̃), applied via gradient descent with projection λ ≥ 0. When F1 drops below threshold (J_C > d̃), the gradient is positive, increasing λ and strengthening the constraint penalty.\\n\\n(e) Conservative checkpoint selection as fallback: evaluate F1 on validation set per epoch; only accept parameter updates that maintain F1 above threshold. This provides a hard guarantee even if the Lagrangian balance oscillates during training.\\n\\nThis follows the precedent of Faithful GRPO (arXiv 2604.08476), which demonstrated that transforming quality metrics from reward terms into hard constraints via Lagrangian dual ascent reduces quality degradation from 24.5% to 1.7%.\\n\\n**Step Criticality Estimator (SCE)**\\n\\nA lightweight module (<1M params) that scores each step's need for deep verification using multiple complementary signals. Unlike Dyve's implicit routing (where the model learns to self-regulate output length through SFT, with no separable routing component), the SCE is an explicit, interpretable, and ablatable module.\\n\\nThe SCE combines:\\n1. Fast-mode intuition confidence: C_I = |p(correct) − p(incorrect)| from the fast verification pass (available as a byproduct)\\n2. Fast-mode token confidence: C_T = mean negative log-probability of irrelevant tokens, measuring probability mass leakage beyond the binary judgment (from F/S-RM's dual-confidence mechanism)\\n3. CoT Entropy signal: Following Ye et al. (arXiv 2502.11250), when running complementary analysis, sample multiple reasoning paths at each step and compute entropy over the marginal distribution of binary decision outcomes: H = −Σ_e(Σ_c p_θ(c,e|x≤t)) log(Σ_c p_θ(c,e|x≤t)). Steps with high CoT Entropy indicate verifier uncertainty requiring deeper analysis. Optional when compute-constrained.\\n4. Generator internal uncertainty: entropy of the generating model's hidden states via ReProbe-style probes (<10M params on frozen generator), when generator internals are available. Optional for black-box generator settings.\\n5. Structural features: step position in chain, relative token length, domain signal. Justified by CoLD (arXiv 2507.15698) showing PRMs have strong length bias.\\n\\nThe SCE is an MLP that outputs a criticality score c_i ∈ [0,1] for each step. Training signal derives from oracle construction: run both fast and deep modes on training steps, identify 'value-add' steps where fast mode misclassifies but deep mode succeeds, and train SCE via binary cross-entropy. We include a planned ablation ladder: (i) fast-mode confidence only → (ii) dual-confidence (C_I + C_T) → (iii) +CoT Entropy → (iv) +ReProbe → (v) +structural features.\\n\\n**Budget-Constrained Router**\\n\\nGiven a per-solution compute budget B (fraction of steps receiving deep verification), the router:\\n1. Runs fast verification on ALL K steps (cheap baseline, ~60ms for 6 steps). This simultaneously produces scalar scores and SCE input signals.\\n2. Computes criticality scores c_i for all steps.\\n3. Selects the top-⌈B·K⌉ highest-criticality steps for deep verification.\\n4. Final step scores combine fast and deep assessments: steps receiving only fast verification use the fast scalar score; steps receiving deep verification use the deep judgment.\\n\\nThe budget B is a tunable hyperparameter that parameterizes the cost-accuracy Pareto frontier: at B=0, all steps use fast verification (cheapest); at B=1, all steps use deep verification (most accurate). The SCE threshold mapping to a given B is calibrated from the empirical criticality score distribution on a calibration set. Critically, the cost ratio between paradigms enters ONLY through B—as generative costs decrease, B can be increased to allocate more deep verification at the same total cost.\\n\\n**Sequential Error Cascade (SEC) Enhancement (Optional)**\\n\\nFor applications where step ordering matters, we add a sequential processing mode grounded in CRM's multiplicative survival decomposition and PURE's min-form insight:\\n- If deep verification detects an ERROR at step i: automatically flag all subsequent steps for deep verification or assign minimum scores (since they are built on faulty premises).\\n- If deep verification CONFIRMS correctness: update posterior criticality of subsequent steps, potentially lowering priority for dependent downstream steps.\\nThis is an optional enhancement that provides marginal accuracy gains on top of the core budget-constrained routing.\\n\\n**Robustness to Cheaper Generative Verification**\\n\\nCRISP-PRM's value proposition is robust to future reductions in generative verification cost, for six reasons: (a) Even a 10x speedup in generative models leaves a 10-50x cost gap (100-500ms vs 10ms per step)—routing still provides substantial efficiency gains. (b) The SCE provides accuracy gains independent of cost: by identifying which steps most benefit from deeper analysis, routing improves verification allocation quality regardless of per-mode costs. Even at equal costs, selectively applying deep verification to high-criticality steps outperforms uniform application because the model's deep mode may still outperform its fast mode on specific error types (e.g., soundness errors, multi-step logical chains). (c) CRISP-PRM's routing is parameterizable—the cost ratio enters only through the budget constraint B and SCE threshold, both tunable hyperparameters. As costs converge, B increases to allocate more deep verification while maintaining cost parity with uniform fast. (d) In the limit where generative cost equals discriminative cost, CRISP-PRM degenerates to uniform deep verification, which is the accuracy-optimal baseline—the framework gracefully adapts rather than becoming irrelevant. (e) Historical analog: TRIM (arXiv 2601.10245) shows step-level routing between models of different sizes remains valuable even as smaller models improve, because the relative cost gap persists across model generations. (f) GenPRM-1.5B still requires multiple forward passes for CoT generation—the cost gap is fundamental (single-token vs multi-token generation) rather than purely model-size dependent.\\n\\n**Difficulty-Stratified Efficiency Analysis**\\n\\nUsing ProcessBench data (arXiv 2412.06559, ACL 2025; verified in R-PRM, arXiv 2503.21295, EMNLP 2025, Table 1) for Qwen2.5-Math-PRM-7B: err accuracy of 72.0%/68.0%/55.7%/55.2% and corr accuracy of 96.4%/90.4%/85.5%/83.0% across GSM8K/MATH/OlympiadBench/OmniMATH. The fraction of steps where deep verification adds value scales with difficulty:\\n\\n• Easy tier (GSM8K-level): Fast verification reliable on ~85-90% of steps. Deep needed on ~10-15%. Expected latency reduction vs uniform deep: ~87%.\\n• Medium tier (MATH-level): Fast verification reliable on ~80-85% of steps. Deep needed on ~15-20%. Expected reduction: ~82%.\\n• Hard tier (OlympiadBench-level): Fast verification reliable on ~70-80% of steps. Deep needed on ~20-30%. Expected reduction: ~75%.\\n• Hardest tier (OmniMATH-level): Fast verification reliable on ~65-75% of steps. Deep needed on ~25-35%. Expected reduction: ~70%.\\n\\nCRISP-PRM's value proposition is difficulty-adaptive: on easy problems, it saves the most compute; on hard problems, it provides the largest accuracy gains.\\n\\n**Evaluation Protocol**\\n\\n• Step-level accuracy: F1 on ProcessBench (GSM8K/MATH/OlympiadBench/OmniMATH subsets reported separately, with err/corr accuracy breakdown) and PRMBench (fine-grained error type breakdown)\\n• Solution-level utility: Best-of-N reranking accuracy on MATH-500, AIME'24, GPQA-Diamond\\n• Efficiency: FLOPs per solution, accuracy-per-FLOP Pareto frontiers at multiple budget levels B ∈ {0.05, 0.1, 0.2, 0.3, 0.5, 1.0}\\n• Baselines: (i) uniform fast PRM (Qwen2.5-Math-PRM-7B, avg F1 73.5), (ii) uniform deep PRM (ThinkPRM-14B), (iii) Dyve (implicit step-level routing, avg F1 ~55.8)—HISTORICAL BASELINE showing progress from Dyve's pioneering work, (iv) problem-level routing (F/S-RM-style dual-confidence gating), (v) VerifySteer (latent steering, F1 72.3), (vi) Budget-aware Pessimistic Verification, (vii) random step selection for deep verification (ablation control), (viii) PRM-confidence-only routing (single-signal ablation)\\n• Ablation studies: (A1) Explicit SCE routing vs. Dyve-style implicit SFT routing on SAME base model—isolating the value of explicit routing; (A2) SCE signal ablation ladder (confidence-only → dual-confidence → +CoT Entropy → +ReProbe → +structural)—quantifying marginal signal contribution; (A3) Constrained GRPO (with F1 floor) vs. standard SFT for unified model training—testing whether Constrained GRPO prevents quality degradation; (A4) SEC-aware vs. independent greedy allocation—measuring value of sequential error cascade awareness; (A5) Budget sensitivity analysis across B ∈ {0.05, 0.1, 0.2, 0.3, 0.5}; (A6) Difficulty-stratified analysis showing per-tier routing rates and gains\\n• Complementarity analysis: CRISP-PRM + VerifySteer (explicit routing + latent strictness steering); CRISP-PRM + PATS (verification routing + generation routing)\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"350 A100-80GB hours (80h unified model training (SFT + Constrained GRPO), 100h oracle construction running both modes on ~120K steps, 20h SCE/router training, 80h evaluation across 4 benchmarks × multiple budgets × 8 baselines including Dyve, 50h ablations (A1-A6), 10h ReProbe probe training, 10h VerifySteer comparison)\",\n      \"timeline\": \"10-14 weeks (single researcher)\",\n      \"estimated_gpu_cost\": \"$700 (at ~$2/hr A100-80GB cloud)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"280 A100-80GB hours (fewer dead-end experiments via Claude-guided threshold tuning and ablation prioritization)\",\n      \"timeline\": \"7-10 weeks\",\n      \"claude_api_cost\": \"$200-400 (experiment design, analysis scripts, paper writing assistance)\",\n      \"estimated_gpu_cost\": \"$560\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"480 A100-80GB hours (broader ablations: multiple SCE architectures, threshold sensitivity, cross-domain transfer, additional benchmarks, difficulty-stratified analysis, Dyve reproduction for fair comparison)\",\n      \"timeline\": \"4-6 weeks\",\n      \"claude_api_cost\": \"$400-700 (end-to-end experiment orchestration, code generation, result analysis)\",\n      \"estimated_gpu_cost\": \"$960\",\n      \"speed_bottleneck\": \"Unified model training is the main bottleneck (~80h); oracle construction is embarrassingly parallel—with 4×A100, drops from ~50h to ~13h wall-clock.\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (full papers Jul 28 2026, supplementary Jul 31 2026 — confirmed via official CFP)\",\n    \"ARR August 2026 cycle (Aug 3 2026, for commitment to NAACL 2027 or EACL 2027)\"\n  ],\n  \"level\": \"solid-to-strong\",\n  \"key_references\": [\n    \"Dyve: Thinking Fast and Slow for Dynamic Process Verification (arXiv 2502.11157, EMNLP 2025) — pioneered step-level System 1/System 2 routing; outperformed all contemporaneous baselines with avg F1 ~55.8; since surpassed by stronger discriminative PRMs\",\n    \"Process Reward Models That Think (ThinkPRM, arXiv 2504.16828, 2025)\",\n    \"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Model Parameters (ICLR 2025)\",\n    \"Fast-Slow Thinking RM: Efficient Integration of Scalar and Generative Reward Models (F/S-RM, arXiv 2603.20212, Mar 2026)\",\n    \"Reason Only When Needed: Efficient Generative Reward Modeling via Model-Internal Uncertainty (E-GRM, arXiv 2604.10072, ACL 2026)\",\n    \"CAMEL: Confidence-Gated Reflection for Reward Modeling (arXiv 2602.20670, ICML 2026)\",\n    \"TRIM: Hybrid Inference via Targeted Stepwise Routing in Multi-Step Reasoning Tasks (arXiv 2601.10245, ICLR 2026)\",\n    \"The Hidden Signal of Verifier Strictness: Controlling and Improving Step-Wise Verification via Selective Latent Steering (VerifySteer, arXiv 2605.20745, May 2026)\",\n    \"Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure (arXiv 2602.03975, Feb 2026)\",\n    \"PATS: Process-Level Adaptive Thinking Mode Switching (arXiv 2505.19250, May 2025)\",\n    \"Efficient Test-Time Scaling of Multi-Step Reasoning by Probing Internal States of Large Language Models (ReProbe/UHeads, arXiv 2511.06209, NeurIPS 2025)\",\n    \"Stop Summation: Min-Form Credit Assignment Is All Process Reward Models Need (PURE, arXiv 2504.15275, 2025)\",\n    \"Conditional Reward Models for Process-Level Credit Assignment (CRM, arXiv 2509.26578, 2025)\",\n    \"Beyond the First Error: Modeling Error Propagation and Cessation in Multi-Step Reasoning (arXiv 2505.14391, 2025)\",\n    \"Know What You Don't Know: Calibration of Process Reward Models (arXiv 2506.09338, NeurIPS 2025)\",\n    \"ProcessBench: Identifying Process Errors in Mathematical Reasoning (arXiv 2412.06559, ACL 2025)\",\n    \"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (arXiv 2501.03124, 2025)\",\n    \"When to Trust the Cheap Check: Weak and Strong Verification for Reasoning (arXiv 2602.17633, Feb 2026)\",\n    \"Budget-aware Test-time Scaling via Discriminative Verification (arXiv 2510.14913, 2025)\",\n    \"When To Solve, When To Verify: Compute-Optimal Problem Solving and Verification (arXiv 2504.01005, 2025)\",\n    \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (arXiv 2504.00891, AAAI 2026)\",\n    \"SCAN: Self-Denoising Monte Carlo Annotation for Robust Process Reward Learning (arXiv 2509.16548, NeurIPS 2025)\",\n    \"R-PRM: Reasoning-Driven Process Reward Modeling (arXiv 2503.21295, EMNLP 2025) — Table 1 provides independently verified ProcessBench numbers for Qwen2.5-Math-PRM-7B\",\n    \"The Lessons of Developing Process Reward Models in Mathematical Reasoning (arXiv 2501.07301, 2025) — Qwen2.5-Math-PRM development and evaluation\",\n    \"Uncertainty-Aware Step-wise Verification with Generative Reward Models (Ye et al., arXiv 2502.11250, Feb 2025) — CoT Entropy for step-level UQ in generative PRMs; AUROC 0.680\",\n    \"Constrained Group Relative Policy Optimization (arXiv 2602.05863, Feb 2026) — Lagrangian-based constrained GRPO with scalarized advantage construction; foundation for F1 floor mechanism\",\n    \"Faithful GRPO: Improving Visual Spatial Reasoning via Constrained Policy Optimization (arXiv 2604.08476, Apr 2026) — precedent for transforming quality metrics into hard constraints via Lagrangian dual ascent\",\n    \"Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling (VG-Search, arXiv 2505.11730, NeurIPS 2025)\",\n    \"CoLD: Mitigating Length Bias in Process Reward Models (arXiv 2507.15698, 2025)\",\n    \"SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation (arXiv 2604.06636, Apr 2026)\",\n    \"SPAE: Step Potential Advantage Estimation for Credit Assignment (arXiv 2601.03823, Jan 2026)\"\n  ],\n  \"description\": \"We propose CRISP-PRM (CRIticality-based Step-level Paradigm selection for Process Reward Models), a framework built on a unified dual-mode verifier that routes each reasoning step to the optimal verification paradigm—fast discriminative scoring or deep generative CoT verification—based on explicit step criticality estimation and a tunable compute budget. Building on Dyve's (EMNLP 2025) pioneering demonstration that step-level paradigm selection outperforms contemporaneous baselines, CRISP-PRM introduces three principled advances designed for composition with modern strong base models: (1) An explicit Step Criticality Estimator (SCE) combining dual-confidence signals from fast verification, CoT Entropy-based uncertainty (Ye et al., arXiv 2502.11250, AUROC 0.680), generator-internal uncertainty (ReProbe-style probes), and structural features—with an ablation ladder quantifying each component's marginal value. (2) A budget-constrained router that parameterizes the cost-accuracy Pareto frontier through a single hyperparameter B (fraction of steps receiving deep verification), enabling graceful adaptation to changing cost ratios: as generative verification becomes cheaper, B increases; in the limit of equal costs, the system degenerates to uniform deep verification. (3) Constrained GRPO fine-tuning (following arXiv 2602.05863) with a hard F1 floor guarantee via indicator cost functions, Lagrangian dual ascent with scalarized advantage construction, and conservative checkpoint selection—ensuring the unified model never degrades below discriminative baseline quality. Using ProcessBench data (arXiv 2412.06559; verified in R-PRM, arXiv 2503.21295, Table 1: Qwen2.5-Math-PRM-7B err acc 72.0%→55.2% across GSM8K→OmniMATH), we estimate ~10-15% of easy-tier steps and ~25-35% of hard-tier steps benefit from deep verification, yielding 70-87% latency reduction vs. uniform deep verification while targeting Pareto dominance over both uniform paradigms and problem-level routing approaches.\",\n  \"project_name\": \"crisp_step_prm\",\n  \"source\": \"web_research\",\n  \"reviewer_response\": {\n    \"MISLEADING_DYVE_FRAMING\": \"Resolved via major reframing across all sections. All instances of 'Dyve degrades verification quality' removed and replaced with accurate historical characterization: Dyve demonstrated the feasibility and value of step-level paradigm selection, outperforming ALL contemporaneous baselines (Qwen2.5-Math-7B-PRM800K avg F1 ~41, Skywork-PRM-7B ~35, Math-Shepherd-PRM-7B ~31, GPT-4o ~52) with avg F1 ~55.8. The proposal now correctly notes that stronger discriminative PRMs trained with improved data pipelines (Qwen2.5-Math-PRM-7B, avg F1 73.5) were published after Dyve and surpassed its performance—revealing a ceiling of implicit routing rather than a failure. The novelty claim is reframed from 'fixing Dyve's degradation' to 'building on Dyve's pioneering insight with explicit, composable routing designed for stronger modern base models.' Dyve is now labeled 'HISTORICAL BASELINE showing progress' rather than 'PRIMARY BASELINE' to acknowledge the era difference. Corrections applied in: core_problem, opportunity, landscape, inspired_by, approach, description, and key_references.\",\n    \"GRPO_F1_FLOOR_MECHANISM_UNSPECIFIED\": \"Resolved via full technical specification using Constrained GRPO framework (arXiv 2602.05863, Feb 2026). The approach section now contains five concrete components: (a) Indicator cost function C_F1(π) = 𝕀[F1_batch(π) < F1_threshold] where F1_threshold is the discriminative baseline F1 on held-out ProcessBench validation split. (b) Lagrangian objective ℒ(π,λ) = J_R(π) − λ·(J_C(π) − d̃) with J_R as format+outcome reward, J_C as constraint violation rate, d̃ as target violation rate (0.05). (c) Scalarized advantage construction A_ScAdv = λ_R·Z_R − λ_C·Z_C with per-component standardization, following Theorem 4.1 of arXiv 2602.05863 to prevent standard-deviation mismatch. (d) Multiplier update ∇_λ ℒ = −(J_C(π) − d̃) with projection λ ≥ 0. (e) Conservative checkpoint selection as hard guarantee fallback. Faithful GRPO (arXiv 2604.08476) cited as precedent reducing quality degradation from 24.5% to 1.7%. Both papers added to key_references.\",\n    \"MISSING_CITATION_COT_ENTROPY\": \"Resolved. 'Uncertainty-Aware Step-wise Verification with Generative Reward Models' (Ye et al., arXiv 2502.11250, Feb 2025) added to landscape section with full technical details: CoT Entropy samples multiple reasoning paths at each step, groups outputs by binary correctness decisions, and computes entropy over the marginal distribution H = −Σ_e(Σ_c p_θ(c,e|x≤t)) log(Σ_c p_θ(c,e|x≤t)). Achieves AUROC 0.680, outperforming all UQ baselines (SEU-MiniLM 0.661). Integrated as a candidate signal for SCE's criticality estimation in the approach section. Added to key_references, opportunity, and description.\",\n    \"UNVERIFIABLE_SCAN_TABLE_2_NUMBERS\": \"Resolved. Attribution corrected from 'SCAN Table 2' to proper source chain: 'ProcessBench (arXiv 2412.06559, ACL 2025), also independently verified in R-PRM (arXiv 2503.21295, EMNLP 2025, Table 1).' The R-PRM paper's Table 1 confirms: Qwen2.5-Math-PRM-7B err acc 72.0/68.0/55.7/55.2, corr acc 96.4/90.4/85.5/83.0, F1 82.4/77.6/67.5/66.3 across GSM8K/MATH/OlympiadBench/OmniMATH. R-PRM added to key_references with explicit Table 1 citation. The Qwen PRM development paper (arXiv 2501.07301) also added as primary source for model details.\",\n    \"IMPACT_VULNERABILITY\": \"Resolved via comprehensive six-argument robustness analysis added to approach section. (a) Even 10x speedup leaves 10-50x cost gap (100-500ms vs 10ms)—routing still valuable. (b) SCE provides accuracy gains independent of cost: selective deep verification outperforms uniform application because the model's deep mode may still excel on specific error types even when costs are equal. (c) Routing is parameterizable—cost ratio enters only through budget B, a single tunable hyperparameter; as costs converge, B increases. (d) In the limit of equal costs, CRISP-PRM degenerates to uniform deep verification (accuracy-optimal baseline)—graceful adaptation. (e) TRIM (arXiv 2601.10245) shows routing value persists across model generations due to persistent relative cost gaps. (f) Cost gap is fundamental (single-token vs multi-token generation) not purely model-size dependent.\",\n    \"MISSING_CITATION_ADAPTIVE_TTC\": \"Previously resolved (round 3). Adaptive Test-Time Compute (arXiv 2602.03975) maintained in landscape.\",\n    \"MISSING_CITATION_PATS\": \"Previously resolved (round 3). PATS (arXiv 2505.19250) maintained in landscape.\",\n    \"MISSING_CITATION_VERIFYSTEER\": \"Previously resolved (round 3). VerifySteer (arXiv 2605.20745) maintained in landscape and baselines.\",\n    \"FACTUAL_ERROR_ERR_ACCURACY\": \"Previously resolved (round 3). Numbers now verified via R-PRM Table 1 with proper attribution.\",\n    \"TWO_MODEL_MEMORY_OVERHEAD\": \"Previously resolved (round 2). Unified single-model architecture maintained.\",\n    \"STEP_DEPENDENCY_IGNORED\": \"Previously resolved (round 2). SEC enhancement maintained as optional module.\",\n    \"SCE_SIGNAL_REDUNDANCY\": \"Previously resolved (round 2). Signal ablation ladder (A2) maintained and extended with CoT Entropy.\",\n    \"BUDGET_AWARE_TTS_OVERLAP\": \"Previously resolved (round 2). Maintained as baseline.\",\n    \"CRITICAL_NOVELTY_F_S_RM\": \"Previously resolved (rounds 1-2). F/S-RM architecture adopted as foundation with step-level extension.\",\n    \"CRITICAL_NOVELTY_E_GRM\": \"Previously resolved (rounds 1-2). Differentiated by granularity.\",\n    \"CRITICAL_NOVELTY_CAMEL\": \"Previously resolved (rounds 1-2). Different target task and granularity.\"\n  }\n}\n\n## Reviewer feedback (round 5)\nIssues: [\"FACTUAL ERROR — CRM MISCHARACTERIZATION: CRM (arXiv 2509.26578) does NOT use 'multiplicative survival decomposition S(t) = Π(1-h(k))' or hazard functions. The paper uses conditional probability modeling to link process rewards to outcomes. The survival analysis framing attributed to CRM is fabricated. This invalidates part of the SEC module's cited theoretical grounding, though PURE's min-form insight still provides partial justification.\", \"OUTDATED DISCRIMINATIVE SOTA: The proposal treats Qwen2.5-Math-PRM-7B (avg F1 73.5) as the leading discriminative PRM on ProcessBench. However, ACTPRM (arXiv 2601.22249, Jan 2026) achieves F1 75.0, and ASPRM (arXiv 2502.13943, Feb 2026) also claims SOTA. The F1 floor threshold (73.5) and baseline characterization need updating.\", \"UNVERIFIABLE VENUE CLAIMS: GenPRM 'AAAI 2026', E-GRM 'ACL 2026', CAMEL 'ICML 2026', and ReProbe 'NeurIPS 2025' acceptance claims could not be independently verified. These may be speculative or based on non-public information. Misrepresenting venue acceptance is a serious credibility issue.\", \"NOVELTY CEILING: After 5 rounds of refinement, the core contribution remains synthesis-level — combining F/S-RM's dual-mode architecture, CoT Entropy, Constrained GRPO, and PURE's min-form insight into a step-level routing framework. While the synthesis is principled and well-motivated, no fundamentally new insight or technique is introduced. The SCE is a standard MLP trained on oracle labels. The routing is a top-k selection. The training uses existing Constrained GRPO. A reviewer might ask: what is the scientific contribution beyond careful engineering?\"]\nFeedback: Three targeted fixes to reach passing quality:\n\n(1) FIX CRM MISCHARACTERIZATION: Remove the fabricated 'multiplicative survival decomposition S(t) = Π(1-h(k))' and 'hazard function' framing attributed to CRM. CRM actually uses conditional probability modeling to link process to outcome, which DOES support sequential step dependencies — just not through survival analysis. Either correctly characterize what CRM actually does, or find a different citation that genuinely uses survival-theoretic decomposition for step-level credit assignment. PURE's min-form insight alone is sufficient to justify the SEC module; the survival analysis language is unnecessary and creates a factual error.\n\n(2) UPDATE DISCRIMINATIVE SOTA: Acknowledge ACTPRM (arXiv 2601.22249, F1 75.0) and ASPRM (arXiv 2502.13943) as more recent discriminative PRMs that surpass Qwen2.5-Math-PRM-7B. Update the F1 floor threshold to 75.0 or frame it as 'matching the current discriminative SOTA.' Also note the Hard2Verify finding that ProcessBench scores may not generalize — this actually STRENGTHENS the case for deeper verification on frontier problems.\n\n(3) QUALIFY OR REMOVE UNVERIFIABLE VENUE CLAIMS: For papers where conference acceptance cannot be publicly verified (GenPRM, E-GRM, CAMEL, ReProbe), either provide verifiable evidence (e.g., link to proceedings page) or present them as arXiv preprints only. Falsely attributing venue acceptance is a significant credibility risk that reviewers will flag.\n\nOptional improvement for novelty: Articulate a clear 'insight' beyond synthesis. For example: 'The key insight is that verification paradigm selection and verification execution should be decoupled — implicit routing (Dyve) entangles them, creating a ceiling when either component improves independently. CRISP-PRM's modularity means advances in discriminative PRMs, generative PRMs, or uncertainty estimation each independently improve the system without retraining.' This composability-as-a-first-class-design-principle framing would elevate the contribution above pure engineering.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.\n- Address each issue specifically.\n\n## 深度调研要求\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。\n3. **深度思考**：\n   - 核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach？\n4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。\n\n## 针对 Review 意见的定向搜索\n\n1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点\n2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline\n3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现\n4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot\n\n- You have full freedom: minor fix, major revision, or pivot.\n- Include a \"change_type\" field: \"minor\", \"major\", or \"pivot\".\n- Output a COMPLETE JSON object with ALL fields."
}
```

---

### Runtime record

_source line 2 · 2026-05-28T01:43:06.339Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T01:43:06.339Z",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff"
}
```

---

## Round 1

40 recorded events

### User

_source line 3 · 2026-05-28T01:43:06.380Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-28 (UTC).**

## Original idea
{
  "title": "CRISP-PRM: Criticality-Aware Step-Level Paradigm Selection for Unified Process Reward Models",
  "core_problem": "Process reward models face a fundamental accuracy-cost trade-off at the step level: discriminative (fast scalar) verification is cheap (~10ms/step) but unreliable on hard reasoning steps, while generative (CoT) verification is far more accurate but ~100-500x more expensive (~1-5s/step). Dyve (arXiv 2502.11157, EMNLP 2025) demonstrated the feasibility and value of step-level fast/slow paradigm selection within a single model using implicit SFT-based routing, outperforming all contemporaneous baselines (Qwen2.5-Math-7B-PRM800K avg F1 ~41, Skywork-PRM-7B ~35, GPT-4o ~52) with avg F1 ~55.8. However, stronger discriminative PRMs trained with improved data pipelines—notably Qwen2.5-Math-PRM-7B (avg F1 73.5 on ProcessBench, per R-PRM Table 1)—have since surpassed Dyve's adaptive performance using pure discriminative verification. This reveals that implicit SFT-based routing has a ceiling: when the routing mechanism is entangled with the verification itself (learned output length as a proxy for routing), the system cannot benefit from independently improving either the discriminative or generative verification mode. Problem-level routing methods (F/S-RM, E-GRM, CAMEL) achieve efficiency gains but apply uniform verification to every step within a solution, ignoring that steps vary dramatically in difficulty and criticality. ProcessBench data confirms this variation: discriminative PRM error detection accuracy degrades from 72.0% (GSM8K) to 55.2% (OmniMATH) (ProcessBench, arXiv 2412.06559; also R-PRM, arXiv 2503.21295, Table 1). Can a unified dual-mode PRM with explicit, composable step-level paradigm selection—using principled criticality estimation rather than implicit SFT routing—produce better accuracy-per-FLOP Pareto frontiers than both uniform paradigms, problem-level routing, and Dyve's implicit step-level routing, while gracefully composing with future improvements to either verification mode?",
  "opportunity": "Three converging developments create a clear opportunity for explicit criticality-based paradigm routing: (1) The maturation of both verification paradigms to strong individual performance. Discriminative PRMs have advanced substantially through improved training pipelines: Qwen2.5-Math-PRM-7B (arXiv 2501.07301) achieves avg F1 73.5 on ProcessBench, a major leap over earlier PRMs like Qwen2.5-Math-7B-PRM800K (avg F1 ~41). Generative PRMs via CoT verification (ThinkPRM, arXiv 2504.16828; GenPRM, arXiv 2504.00891) achieve F1 of 87.3/85.7 on hard subsets—a ~20 F1 point advantage over discriminative PRMs. This means a router can now select between two genuinely strong modes. (2) Dyve demonstrated that step-level paradigm selection is technically feasible and valuable—outperforming all contemporaneous baselines. But its implicit SFT routing conflates when to switch with how to verify, preventing composition with stronger base models. The gap between Dyve (avg F1 55.8) and modern discriminative PRMs (avg F1 73.5) reveals that the bottleneck is the routing mechanism, not the adaptive concept. CRISP-PRM's explicit routing via a lightweight criticality estimator (SCE) is model-agnostic and immediately benefits from advances in either paradigm. (3) Recent work on step-level uncertainty quantification provides validated signals for criticality estimation: CoT Entropy (Ye et al., arXiv 2502.11250) achieves AUROC 0.680 as the best UQ method for generative PRMs; ReProbe/UHeads (arXiv 2511.06209, NeurIPS 2025) provides lightweight step-level uncertainty heads where combining ReProbe scores with PRM scores outperforms either alone; F/S-RM's dual-confidence mechanism (arXiv 2603.20212) demonstrates that multi-signal routing outperforms single-signal. Additionally, Constrained GRPO (arXiv 2602.05863) and Faithful GRPO (arXiv 2604.08476) provide principled frameworks for training with hard quality constraints, enabling the F1 floor guarantee that prevents quality degradation during RL fine-tuning. (4) PURE's min-form credit assignment (arXiv 2504.15275) and CRM's multiplicative survival decomposition (arXiv 2509.26578) prove the weakest step dominates solution quality, implying verification effort should concentrate on critical steps with sequential awareness. (5) VerifySteer (arXiv 2605.20745, May 2026) shows verification compute can be reduced 4-7x through principled intervention at ProcessBench F1 of 72.3, confirming large optimization headroom that is orthogonal to and composable with CRISP-PRM's approach. The unoccupied synthesis is explicit step-level paradigm selection within a unified dual-mode verifier, with composable routing designed to work with modern strong base models—addressing exactly the ceiling that Dyve's implicit approach hits.",
  "landscape": "**Discriminative PRMs.** Qwen2.5-Math-PRM-7B (arXiv 2501.07301) is the leading discriminative PRM with ProcessBench F1 of 82.4/77.6/67.5/66.3 across GSM8K/MATH/OlympiadBench/OmniMATH (avg 73.5), as reported in ProcessBench (arXiv 2412.06559, ACL 2025) and independently verified in R-PRM (arXiv 2503.21295, EMNLP 2025, Table 1). Its error detection accuracy (err acc) degrades from 72.0% (GSM8K) to 55.2% (OmniMATH), while correctness accuracy (corr acc) remains relatively stable (96.4% to 83.0%). This represents a major advance over earlier PRMs: Qwen2.5-Math-7B-PRM800K (avg F1 ~41), Skywork-PRM-7B (~35). PRMBench shows discriminative PRMs achieve near-random performance on 'simplicity' error types (redundancy, circular logic). SCAN (arXiv 2509.16548, NeurIPS 2025) provides an efficient data synthesis and noise-tolerant learning framework for PRMs.\n\n**Generative PRMs.** ThinkPRM (arXiv 2504.16828, 2025) scales verification compute via extended CoT thinking, achieving F1 of 87.3/85.7 on OlympiadBench/OmniMATH with ThinkPRM-14B—a ~20 F1 point advantage over discriminative PRMs on hard subsets, but at ~100-500x compute cost per step. GenPRM (arXiv 2504.00891, AAAI 2026) shows GenPRM-1.5B outperforms GPT-4o on ProcessBench via code-augmented generative verification.\n\n**Step-Level Adaptive Verification (Implicit Routing).** Dyve (arXiv 2502.11157, EMNLP 2025) is the most directly related prior work and the pioneer of step-level paradigm selection. It trains a single DeepSeek-R1-Distill-Qwen-14B via standard cross-entropy SFT on 117K examples to implicitly route between System 1 (single-token '+' confirmation) and System 2 (CoT analysis, up to 8192 tokens). ProcessBench F1: 68.5/58.3/49.0/47.2 (avg ~55.8). Critically, Dyve outperformed ALL contemporaneous baselines at the time of publication: Qwen2.5-Math-7B-PRM800K (avg F1 ~41), Skywork-PRM-7B (~35), Math-Shepherd-PRM-7B (~31), and GPT-4o (~52). However, stronger discriminative PRMs trained with improved data pipelines (Qwen2.5-Math-PRM-7B, avg F1 73.5) have since surpassed Dyve's performance. This reveals a ceiling of implicit routing: (a) the routing decision is entangled with the verification itself (learned output length as proxy), preventing composition with independently improved verifiers; (b) steps are scored independently with no sequential error cascade awareness; (c) standard cross-entropy SFT provides no quality floor guarantee; (d) no separable routing component enables ablation or interpretability. CRISP-PRM builds on Dyve's pioneering insight with explicit, composable routing designed to work with stronger base models.\n\n**Step-Level Uncertainty Quantification.** CoT Entropy (Ye et al., arXiv 2502.11250, Feb 2025) introduces a novel UQ method for step-level verification in generative PRMs: it samples multiple reasoning paths at each step, groups outputs by binary correctness decisions, and computes entropy over the marginal distribution: H = −Σ_e(Σ_c p_θ(c,e|x≤t)) log(Σ_c p_θ(c,e|x≤t)). Achieves AUROC 0.680, outperforming all UQ baselines (SEU-MiniLM 0.661, SEU-NV-Embed). Directly relevant to CRISP-PRM's SCE as a candidate signal for estimating when deep verification is most needed. ReProbe/UHeads (arXiv 2511.06209, NeurIPS 2025) provides lightweight step-level uncertainty heads; combining ReProbe scores with PRM scores outperforms either alone.\n\n**Problem-Level Fast/Slow Routing.** F/S-RM (arXiv 2603.20212, Mar 2026) trains a single Qwen3-8B with dual fast (first-token scalar) and slow (CoT generation) modes, using dual-confidence activation to route at the problem level; achieves 20.8% token savings but never considers within-solution step variation. E-GRM (arXiv 2604.10072, ACL 2026) routes between direct inference and CoT generation via parallel-decoding consensus at the problem level; 62% latency reduction and 49% FLOP reduction on MATH. CAMEL (arXiv 2602.20670, ICML 2026) uses log-probability confidence gating for pairwise preference judging; problem-level and not PRM-specific.\n\n**Step-Level Generation Routing.** TRIM (arXiv 2601.10245, ICLR 2026) performs step-level routing between small and large generation models using PRM-derived uncertainty, achieving 5x cost efficiency on MATH-500; routes generators, not verification paradigms. Demonstrates that step-level routing value persists even as individual models improve.\n\n**Verification Compute Optimization.** VerifySteer (arXiv 2605.20745, May 2026) identifies verifier strictness signals in hidden states at paragraph-boundary delimiter tokens and steers verification depth via selective latent interventions. Achieves ProcessBench F1 of 72.3 with Qwen3-8B at 4-7x less inference compute than self-consistency; orthogonal to and composable with fine-tuned verifiers. Adaptive Test-Time Compute (arXiv 2602.03975, Feb 2026) performs state-level selective verification combining deterministic feasibility gating with learned scoring and adaptive allocation, achieving 30% fewer verifier calls on MATH-500. Budget-aware Test-time Scaling (arXiv 2510.14913, 2025) shows discriminative verifiers + self-consistency (Pessimistic Verification) outperform generative verifiers under constrained FLOP budgets.\n\n**Constrained RL for Quality Guarantees.** Constrained GRPO (arXiv 2602.05863, Feb 2026) introduces a Lagrangian-based extension of GRPO for constrained policy optimization with indicator cost functions, scalarized advantage construction (preventing standard-deviation mismatch), and learned multipliers. Faithful GRPO (arXiv 2604.08476, Apr 2026) applies this to transform quality metrics from reward terms into hard constraints via Lagrangian dual ascent, reducing inconsistency from 24.5% to 1.7%. Both provide the technical foundation for CRISP-PRM's F1 floor guarantee.\n\n**Adaptive Thinking for Generators.** PATS (arXiv 2505.19250, May 2025) introduces process-level adaptive thinking mode switching for generators. Adjusts beam width per step based on PRM scores, achieving near-optimal accuracy at 55% of full-compute token usage. PATS adapts generation depth; CRISP-PRM adapts verification depth—complementary.\n\n**Credit Assignment and Error Propagation.** CRM (arXiv 2509.26578, 2025) frames step correctness as a hazard function with multiplicative survival decomposition S(t) = Π(1-h(k)). PURE (arXiv 2504.15275, 2025) introduces min-form credit assignment proving the weakest step dominates. 'Beyond the First Error' (arXiv 2505.14391, 2025) distinguishes error propagation from error cessation.\n\n**PRM Calibration.** 'Know What You Don't Know' (arXiv 2506.09338, NeurIPS 2025) demonstrates PRMs are poorly calibrated, overestimating success probability—motivating multi-signal criticality estimation rather than relying on single PRM confidence scores.\n\n**Summary.** Dyve pioneered step-level paradigm selection and outperformed all contemporaneous baselines, demonstrating the value of adaptive verification. However, no existing system combines explicit, composable criticality estimation that works with modern strong base models, sequential error cascade awareness, constrained training with F1 floor guarantees, and robustness to changing cost ratios between verification paradigms.",
  "inspired_by": "Convergence of five research threads with a critical empirical insight: (1) Dyve (EMNLP 2025) demonstrated that step-level fast/slow verification within a single model is feasible and valuable, outperforming all contemporaneous baselines. The subsequent emergence of stronger discriminative PRMs (Qwen2.5-Math-PRM-7B, avg F1 73.5) that surpass Dyve reveals that implicit routing hits a ceiling—motivating explicit, composable routing. (2) F/S-RM (Mar 2026) proves a single model can support both discriminative and generative modes with dual-confidence routing → provides the architectural foundation. (3) CRM's multiplicative survival decomposition and PURE's min-form credit assignment prove the weakest step dominates → verification effort should be sequentially aware. (4) CoT Entropy (arXiv 2502.11250) achieves best-in-class step-level uncertainty quantification for generative PRMs (AUROC 0.680) → provides validated signal for criticality estimation. (5) Constrained GRPO (arXiv 2602.05863) and Faithful GRPO (arXiv 2604.08476) provide principled frameworks for enforcing quality constraints during RL training → enables the F1 floor guarantee. Pattern: 'Dyve showed the right question (adaptive step verification) and demonstrated its value. The next step requires explicit routing that composes with stronger base models, principled criticality estimation, and constrained training with quality guarantees.'",
  "approach": "We propose CRISP-PRM (CRIticality-based Step-level Paradigm selection for Process Reward Models), a framework built on a unified dual-mode verifier that selects the verification paradigm—fast (discriminative) or deep (generative CoT)—for each reasoning step based on estimated step criticality, under a compute budget constraint. Building on Dyve's pioneering demonstration that step-level paradigm selection outperforms contemporaneous baselines, CRISP-PRM introduces explicit, composable routing designed to work with modern strong base models.\n\n**Architecture: Unified Dual-Mode PRM**\n\nCRISP-PRM uses a single Qwen3-8B model fine-tuned to support both verification modes, following the F/S-RM dual-mode paradigm adapted for step-level process verification:\n\n• Fast mode: Given (problem, solution prefix, step_i), the model's first generated token is a correctness judgment ('correct'/'incorrect'). The token probability p(correct|context) serves directly as a scalar step reward. Cost: ~10ms/step (single forward pass). No separate classification head needed—the standard LM head suffices.\n\n• Deep mode: A special trigger token is appended to the prompt, bypassing fast judgment and entering CoT verification. The model generates a step-by-step verification rationale inside &lt;verify>...&lt;/verify> tags, then outputs a final correctness judgment. Cost: ~100ms-2s/step depending on model size and generation length.\n\n**Training Pipeline: Two-Stage with Constrained RL**\n\nStage 1 — SFT Foundation: Combined loss L = L_step + λ·L_action, where L_step is binary cross-entropy on step labels (fast mode) combined with generation loss on synthetic verification CoTs from ThinkPRM-style data (deep mode), and L_action is an action-space constraint penalizing probability leakage to irrelevant tokens during fast mode.\n\nStage 2 — Constrained GRPO with F1 Floor: We adopt the Constrained GRPO framework (arXiv 2602.05863) to fine-tune the unified model with a hard F1 floor guarantee—ensuring the model never degrades below the discriminative baseline quality. Concrete specification:\n\n(a) Indicator cost function: C_F1(π) = 𝕀[F1_batch(π) < F1_threshold], where F1_threshold is set to the discriminative baseline F1 on a held-out ProcessBench validation split (avg F1 73.5 for Qwen2.5-Math-PRM-7B class models).\n\n(b) Lagrangian objective: ℒ(π,λ) = J_R(π) − λ·(J_C(π) − d̃), where J_R is the primary reward (format correctness + outcome accuracy for both fast and deep modes), J_C is the constraint violation rate, and d̃ is the target violation rate (0.05 = at most 5% of validation batches may fall below F1_threshold).\n\n(c) Scalarized advantage construction (NOT scalarized rewards, following arXiv 2602.05863 Theorem 4.1 to prevent standard-deviation mismatch): A_ScAdv = λ_R·Z_R − λ_C·Z_C, where Z_j = (Component_j − mean(Component_j))/std(Component_j) are per-component standardized advantages. This preserves the intended trade-off between reward maximization and constraint satisfaction.\n\n(d) Multiplier update: ∇_λ ℒ = −(J_C(π) − d̃), applied via gradient descent with projection λ ≥ 0. When F1 drops below threshold (J_C > d̃), the gradient is positive, increasing λ and strengthening the constraint penalty.\n\n(e) Conservative checkpoint selection as fallback: evaluate F1 on validation set per epoch; only accept parameter updates that maintain F1 above threshold. This provides a hard guarantee even if the Lagrangian balance oscillates during training.\n\nThis follows the precedent of Faithful GRPO (arXiv 2604.08476), which demonstrated that transforming quality metrics from reward terms into hard constraints via Lagrangian dual ascent reduces quality degradation from 24.5% to 1.7%.\n\n**Step Criticality Estimator (SCE)**\n\nA lightweight module (<1M params) that scores each step's need for deep verification using multiple complementary signals. Unlike Dyve's implicit routing (where the model learns to self-regulate output length through SFT, with no separable routing component), the SCE is an explicit, interpretable, and ablatable module.\n\nThe SCE combines:\n1. Fast-mode intuition confidence: C_I = |p(correct) − p(incorrect)| from the fast verification pass (available as a byproduct)\n2. Fast-mode token confidence: C_T = mean negative log-probability of irrelevant tokens, measuring probability mass leakage beyond the binary judgment (from F/S-RM's dual-confidence mechanism)\n3. CoT Entropy signal: Following Ye et al. (arXiv 2502.11250), when running complementary analysis, sample multiple reasoning paths at each step and compute entropy over the marginal distribution of binary decision outcomes: H = −Σ_e(Σ_c p_θ(c,e|x≤t)) log(Σ_c p_θ(c,e|x≤t)). Steps with high CoT Entropy indicate verifier uncertainty requiring deeper analysis. Optional when compute-constrained.\n4. Generator internal uncertainty: entropy of the generating model's hidden states via ReProbe-style probes (<10M params on frozen generator), when generator internals are available. Optional for black-box generator settings.\n5. Structural features: step position in chain, relative token length, domain signal. Justified by CoLD (arXiv 2507.15698) showing PRMs have strong length bias.\n\nThe SCE is an MLP that outputs a criticality score c_i ∈ [0,1] for each step. Training signal derives from oracle construction: run both fast and deep modes on training steps, identify 'value-add' steps where fast mode misclassifies but deep mode succeeds, and train SCE via binary cross-entropy. We include a planned ablation ladder: (i) fast-mode confidence only → (ii) dual-confidence (C_I + C_T) → (iii) +CoT Entropy → (iv) +ReProbe → (v) +structural features.\n\n**Budget-Constrained Router**\n\nGiven a per-solution compute budget B (fraction of steps receiving deep verification), the router:\n1. Runs fast verification on ALL K steps (cheap baseline, ~60ms for 6 steps). This simultaneously produces scalar scores and SCE input signals.\n2. Computes criticality scores c_i for all steps.\n3. Selects the top-⌈B·K⌉ highest-criticality steps for deep verification.\n4. Final step scores combine fast and deep assessments: steps receiving only fast verification use the fast scalar score; steps receiving deep verification use the deep judgment.\n\nThe budget B is a tunable hyperparameter that parameterizes the cost-accuracy Pareto frontier: at B=0, all steps use fast verification (cheapest); at B=1, all steps use deep verification (most accurate). The SCE threshold mapping to a given B is calibrated from the empirical criticality score distribution on a calibration set. Critically, the cost ratio between paradigms enters ONLY through B—as generative costs decrease, B can be increased to allocate more deep verification at the same total cost.\n\n**Sequential Error Cascade (SEC) Enhancement (Optional)**\n\nFor applications where step ordering matters, we add a sequential processing mode grounded in CRM's multiplicative survival decomposition and PURE's min-form insight:\n- If deep verification detects an ERROR at step i: automatically flag all subsequent steps for deep verification or assign minimum scores (since they are built on faulty premises).\n- If deep verification CONFIRMS correctness: update posterior criticality of subsequent steps, potentially lowering priority for dependent downstream steps.\nThis is an optional enhancement that provides marginal accuracy gains on top of the core budget-constrained routing.\n\n**Robustness to Cheaper Generative Verification**\n\nCRISP-PRM's value proposition is robust to future reductions in generative verification cost, for six reasons: (a) Even a 10x speedup in generative models leaves a 10-50x cost gap (100-500ms vs 10ms per step)—routing still provides substantial efficiency gains. (b) The SCE provides accuracy gains independent of cost: by identifying which steps most benefit from deeper analysis, routing improves verification allocation quality regardless of per-mode costs. Even at equal costs, selectively applying deep verification to high-criticality steps outperforms uniform application because the model's deep mode may still outperform its fast mode on specific error types (e.g., soundness errors, multi-step logical chains). (c) CRISP-PRM's routing is parameterizable—the cost ratio enters only through the budget constraint B and SCE threshold, both tunable hyperparameters. As costs converge, B increases to allocate more deep verification while maintaining cost parity with uniform fast. (d) In the limit where generative cost equals discriminative cost, CRISP-PRM degenerates to uniform deep verification, which is the accuracy-optimal baseline—the framework gracefully adapts rather than becoming irrelevant. (e) Historical analog: TRIM (arXiv 2601.10245) shows step-level routing between models of different sizes remains valuable even as smaller models improve, because the relative cost gap persists across model generations. (f) GenPRM-1.5B still requires multiple forward passes for CoT generation—the cost gap is fundamental (single-token vs multi-token generation) rather than purely model-size dependent.\n\n**Difficulty-Stratified Efficiency Analysis**\n\nUsing ProcessBench data (arXiv 2412.06559, ACL 2025; verified in R-PRM, arXiv 2503.21295, EMNLP 2025, Table 1) for Qwen2.5-Math-PRM-7B: err accuracy of 72.0%/68.0%/55.7%/55.2% and corr accuracy of 96.4%/90.4%/85.5%/83.0% across GSM8K/MATH/OlympiadBench/OmniMATH. The fraction of steps where deep verification adds value scales with difficulty:\n\n• Easy tier (GSM8K-level): Fast verification reliable on ~85-90% of steps. Deep needed on ~10-15%. Expected latency reduction vs uniform deep: ~87%.\n• Medium tier (MATH-level): Fast verification reliable on ~80-85% of steps. Deep needed on ~15-20%. Expected reduction: ~82%.\n• Hard tier (OlympiadBench-level): Fast verification reliable on ~70-80% of steps. Deep needed on ~20-30%. Expected reduction: ~75%.\n• Hardest tier (OmniMATH-level): Fast verification reliable on ~65-75% of steps. Deep needed on ~25-35%. Expected reduction: ~70%.\n\nCRISP-PRM's value proposition is difficulty-adaptive: on easy problems, it saves the most compute; on hard problems, it provides the largest accuracy gains.\n\n**Evaluation Protocol**\n\n• Step-level accuracy: F1 on ProcessBench (GSM8K/MATH/OlympiadBench/OmniMATH subsets reported separately, with err/corr accuracy breakdown) and PRMBench (fine-grained error type breakdown)\n• Solution-level utility: Best-of-N reranking accuracy on MATH-500, AIME'24, GPQA-Diamond\n• Efficiency: FLOPs per solution, accuracy-per-FLOP Pareto frontiers at multiple budget levels B ∈ {0.05, 0.1, 0.2, 0.3, 0.5, 1.0}\n• Baselines: (i) uniform fast PRM (Qwen2.5-Math-PRM-7B, avg F1 73.5), (ii) uniform deep PRM (ThinkPRM-14B), (iii) Dyve (implicit step-level routing, avg F1 ~55.8)—HISTORICAL BASELINE showing progress from Dyve's pioneering work, (iv) problem-level routing (F/S-RM-style dual-confidence gating), (v) VerifySteer (latent steering, F1 72.3), (vi) Budget-aware Pessimistic Verification, (vii) random step selection for deep verification (ablation control), (viii) PRM-confidence-only routing (single-signal ablation)\n• Ablation studies: (A1) Explicit SCE routing vs. Dyve-style implicit SFT routing on SAME base model—isolating the value of explicit routing; (A2) SCE signal ablation ladder (confidence-only → dual-confidence → +CoT Entropy → +ReProbe → +structural)—quantifying marginal signal contribution; (A3) Constrained GRPO (with F1 floor) vs. standard SFT for unified model training—testing whether Constrained GRPO prevents quality degradation; (A4) SEC-aware vs. independent greedy allocation—measuring value of sequential error cascade awareness; (A5) Budget sensitivity analysis across B ∈ {0.05, 0.1, 0.2, 0.3, 0.5}; (A6) Difficulty-stratified analysis showing per-tier routing rates and gains\n• Complementarity analysis: CRISP-PRM + VerifySteer (explicit routing + latent strictness steering); CRISP-PRM + PATS (verification routing + generation routing)",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "350 A100-80GB hours (80h unified model training (SFT + Constrained GRPO), 100h oracle construction running both modes on ~120K steps, 20h SCE/router training, 80h evaluation across 4 benchmarks × multiple budgets × 8 baselines including Dyve, 50h ablations (A1-A6), 10h ReProbe probe training, 10h VerifySteer comparison)",
      "timeline": "10-14 weeks (single researcher)",
      "estimated_gpu_cost": "$700 (at ~$2/hr A100-80GB cloud)"
    },
    "human_in_loop": {
      "gpu_hours": "280 A100-80GB hours (fewer dead-end experiments via Claude-guided threshold tuning and ablation prioritization)",
      "timeline": "7-10 weeks",
      "claude_api_cost": "$200-400 (experiment design, analysis scripts, paper writing assistance)",
      "estimated_gpu_cost": "$560"
    },
    "auto_research": {
      "gpu_hours": "480 A100-80GB hours (broader ablations: multiple SCE architectures, threshold sensitivity, cross-domain transfer, additional benchmarks, difficulty-stratified analysis, Dyve reproduction for fair comparison)",
      "timeline": "4-6 weeks",
      "claude_api_cost": "$400-700 (end-to-end experiment orchestration, code generation, result analysis)",
      "estimated_gpu_cost": "$960",
      "speed_bottleneck": "Unified model training is the main bottleneck (~80h); oracle construction is embarrassingly parallel—with 4×A100, drops from ~50h to ~13h wall-clock."
    }
  },
  "target_venues": [
    "AAAI 2027 (full papers Jul 28 2026, supplementary Jul 31 2026 — confirmed via official CFP)",
    "ARR August 2026 cycle (Aug 3 2026, for commitment to NAACL 2027 or EACL 2027)"
  ],
  "level": "solid-to-strong",
  "key_references": [
    "Dyve: Thinking Fast and Slow for Dynamic Process Verification (arXiv 2502.11157, EMNLP 2025) — pioneered step-level System 1/System 2 routing; outperformed all contemporaneous baselines with avg F1 ~55.8; since surpassed by stronger discriminative PRMs",
    "Process Reward Models That Think (ThinkPRM, arXiv 2504.16828, 2025)",
    "Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Model Parameters (ICLR 2025)",
    "Fast-Slow Thinking RM: Efficient Integration of Scalar and Generative Reward Models (F/S-RM, arXiv 2603.20212, Mar 2026)",
    "Reason Only When Needed: Efficient Generative Reward Modeling via Model-Internal Uncertainty (E-GRM, arXiv 2604.10072, ACL 2026)",
    "CAMEL: Confidence-Gated Reflection for Reward Modeling (arXiv 2602.20670, ICML 2026)",
    "TRIM: Hybrid Inference via Targeted Stepwise Routing in Multi-Step Reasoning Tasks (arXiv 2601.10245, ICLR 2026)",
    "The Hidden Signal of Verifier Strictness: Controlling and Improving Step-Wise Verification via Selective Latent Steering (VerifySteer, arXiv 2605.20745, May 2026)",
    "Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure (arXiv 2602.03975, Feb 2026)",
    "PATS: Process-Level Adaptive Thinking Mode Switching (arXiv 2505.19250, May 2025)",
    "Efficient Test-Time Scaling of Multi-Step Reasoning by Probing Internal States of Large Language Models (ReProbe/UHeads, arXiv 2511.06209, NeurIPS 2025)",
    "Stop Summation: Min-Form Credit Assignment Is All Process Reward Models Need (PURE, arXiv 2504.15275, 2025)",
    "Conditional Reward Models for Process-Level Credit Assignment (CRM, arXiv 2509.26578, 2025)",
    "Beyond the First Error: Modeling Error Propagation and Cessation in Multi-Step Reasoning (arXiv 2505.14391, 2025)",
    "Know What You Don't Know: Calibration of Process Reward Models (arXiv 2506.09338, NeurIPS 2025)",
    "ProcessBench: Identifying Process Errors in Mathematical Reasoning (arXiv 2412.06559, ACL 2025)",
    "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (arXiv 2501.03124, 2025)",
    "When to Trust the Cheap Check: Weak and Strong Verification for Reasoning (arXiv 2602.17633, Feb 2026)",
    "Budget-aware Test-time Scaling via Discriminative Verification (arXiv 2510.14913, 2025)",
    "When To Solve, When To Verify: Compute-Optimal Problem Solving and Verification (arXiv 2504.01005, 2025)",
    "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (arXiv 2504.00891, AAAI 2026)",
    "SCAN: Self-Denoising Monte Carlo Annotation for Robust Process Reward Learning (arXiv 2509.16548, NeurIPS 2025)",
    "R-PRM: Reasoning-Driven Process Reward Modeling (arXiv 2503.21295, EMNLP 2025) — Table 1 provides independently verified ProcessBench numbers for Qwen2.5-Math-PRM-7B",
    "The Lessons of Developing Process Reward Models in Mathematical Reasoning (arXiv 2501.07301, 2025) — Qwen2.5-Math-PRM development and evaluation",
    "Uncertainty-Aware Step-wise Verification with Generative Reward Models (Ye et al., arXiv 2502.11250, Feb 2025) — CoT Entropy for step-level UQ in generative PRMs; AUROC 0.680",
    "Constrained Group Relative Policy Optimization (arXiv 2602.05863, Feb 2026) — Lagrangian-based constrained GRPO with scalarized advantage construction; foundation for F1 floor mechanism",
    "Faithful GRPO: Improving Visual Spatial Reasoning via Constrained Policy Optimization (arXiv 2604.08476, Apr 2026) — precedent for transforming quality metrics into hard constraints via Lagrangian dual ascent",
    "Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling (VG-Search, arXiv 2505.11730, NeurIPS 2025)",
    "CoLD: Mitigating Length Bias in Process Reward Models (arXiv 2507.15698, 2025)",
    "SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation (arXiv 2604.06636, Apr 2026)",
    "SPAE: Step Potential Advantage Estimation for Credit Assignment (arXiv 2601.03823, Jan 2026)"
  ],
  "description": "We propose CRISP-PRM (CRIticality-based Step-level Paradigm selection for Process Reward Models), a framework built on a unified dual-mode verifier that routes each reasoning step to the optimal verification paradigm—fast discriminative scoring or deep generative CoT verification—based on explicit step criticality estimation and a tunable compute budget. Building on Dyve's (EMNLP 2025) pioneering demonstration that step-level paradigm selection outperforms contemporaneous baselines, CRISP-PRM introduces three principled advances designed for composition with modern strong base models: (1) An explicit Step Criticality Estimator (SCE) combining dual-confidence signals from fast verification, CoT Entropy-based uncertainty (Ye et al., arXiv 2502.11250, AUROC 0.680), generator-internal uncertainty (ReProbe-style probes), and structural features—with an ablation ladder quantifying each component's marginal value. (2) A budget-constrained router that parameterizes the cost-accuracy Pareto frontier through a single hyperparameter B (fraction of steps receiving deep verification), enabling graceful adaptation to changing cost ratios: as generative verification becomes cheaper, B increases; in the limit of equal costs, the system degenerates to uniform deep verification. (3) Constrained GRPO fine-tuning (following arXiv 2602.05863) with a hard F1 floor guarantee via indicator cost functions, Lagrangian dual ascent with scalarized advantage construction, and conservative checkpoint selection—ensuring the unified model never degrades below discriminative baseline quality. Using ProcessBench data (arXiv 2412.06559; verified in R-PRM, arXiv 2503.21295, Table 1: Qwen2.5-Math-PRM-7B err acc 72.0%→55.2% across GSM8K→OmniMATH), we estimate ~10-15% of easy-tier steps and ~25-35% of hard-tier steps benefit from deep verification, yielding 70-87% latency reduction vs. uniform deep verification while targeting Pareto dominance over both uniform paradigms and problem-level routing approaches.",
  "project_name": "crisp_step_prm",
  "source": "web_research",
  "reviewer_response": {
    "MISLEADING_DYVE_FRAMING": "Resolved via major reframing across all sections. All instances of 'Dyve degrades verification quality' removed and replaced with accurate historical characterization: Dyve demonstrated the feasibility and value of step-level paradigm selection, outperforming ALL contemporaneous baselines (Qwen2.5-Math-7B-PRM800K avg F1 ~41, Skywork-PRM-7B ~35, Math-Shepherd-PRM-7B ~31, GPT-4o ~52) with avg F1 ~55.8. The proposal now correctly notes that stronger discriminative PRMs trained with improved data pipelines (Qwen2.5-Math-PRM-7B, avg F1 73.5) were published after Dyve and surpassed its performance—revealing a ceiling of implicit routing rather than a failure. The novelty claim is reframed from 'fixing Dyve's degradation' to 'building on Dyve's pioneering insight with explicit, composable routing designed for stronger modern base models.' Dyve is now labeled 'HISTORICAL BASELINE showing progress' rather than 'PRIMARY BASELINE' to acknowledge the era difference. Corrections applied in: core_problem, opportunity, landscape, inspired_by, approach, description, and key_references.",
    "GRPO_F1_FLOOR_MECHANISM_UNSPECIFIED": "Resolved via full technical specification using Constrained GRPO framework (arXiv 2602.05863, Feb 2026). The approach section now contains five concrete components: (a) Indicator cost function C_F1(π) = 𝕀[F1_batch(π) < F1_threshold] where F1_threshold is the discriminative baseline F1 on held-out ProcessBench validation split. (b) Lagrangian objective ℒ(π,λ) = J_R(π) − λ·(J_C(π) − d̃) with J_R as format+outcome reward, J_C as constraint violation rate, d̃ as target violation rate (0.05). (c) Scalarized advantage construction A_ScAdv = λ_R·Z_R − λ_C·Z_C with per-component standardization, following Theorem 4.1 of arXiv 2602.05863 to prevent standard-deviation mismatch. (d) Multiplier update ∇_λ ℒ = −(J_C(π) − d̃) with projection λ ≥ 0. (e) Conservative checkpoint selection as hard guarantee fallback. Faithful GRPO (arXiv 2604.08476) cited as precedent reducing quality degradation from 24.5% to 1.7%. Both papers added to key_references.",
    "MISSING_CITATION_COT_ENTROPY": "Resolved. 'Uncertainty-Aware Step-wise Verification with Generative Reward Models' (Ye et al., arXiv 2502.11250, Feb 2025) added to landscape section with full technical details: CoT Entropy samples multiple reasoning paths at each step, groups outputs by binary correctness decisions, and computes entropy over the marginal distribution H = −Σ_e(Σ_c p_θ(c,e|x≤t)) log(Σ_c p_θ(c,e|x≤t)). Achieves AUROC 0.680, outperforming all UQ baselines (SEU-MiniLM 0.661). Integrated as a candidate signal for SCE's criticality estimation in the approach section. Added to key_references, opportunity, and description.",
    "UNVERIFIABLE_SCAN_TABLE_2_NUMBERS": "Resolved. Attribution corrected from 'SCAN Table 2' to proper source chain: 'ProcessBench (arXiv 2412.06559, ACL 2025), also independently verified in R-PRM (arXiv 2503.21295, EMNLP 2025, Table 1).' The R-PRM paper's Table 1 confirms: Qwen2.5-Math-PRM-7B err acc 72.0/68.0/55.7/55.2, corr acc 96.4/90.4/85.5/83.0, F1 82.4/77.6/67.5/66.3 across GSM8K/MATH/OlympiadBench/OmniMATH. R-PRM added to key_references with explicit Table 1 citation. The Qwen PRM development paper (arXiv 2501.07301) also added as primary source for model details.",
    "IMPACT_VULNERABILITY": "Resolved via comprehensive six-argument robustness analysis added to approach section. (a) Even 10x speedup leaves 10-50x cost gap (100-500ms vs 10ms)—routing still valuable. (b) SCE provides accuracy gains independent of cost: selective deep verification outperforms uniform application because the model's deep mode may still excel on specific error types even when costs are equal. (c) Routing is parameterizable—cost ratio enters only through budget B, a single tunable hyperparameter; as costs converge, B increases. (d) In the limit of equal costs, CRISP-PRM degenerates to uniform deep verification (accuracy-optimal baseline)—graceful adaptation. (e) TRIM (arXiv 2601.10245) shows routing value persists across model generations due to persistent relative cost gaps. (f) Cost gap is fundamental (single-token vs multi-token generation) not purely model-size dependent.",
    "MISSING_CITATION_ADAPTIVE_TTC": "Previously resolved (round 3). Adaptive Test-Time Compute (arXiv 2602.03975) maintained in landscape.",
    "MISSING_CITATION_PATS": "Previously resolved (round 3). PATS (arXiv 2505.19250) maintained in landscape.",
    "MISSING_CITATION_VERIFYSTEER": "Previously resolved (round 3). VerifySteer (arXiv 2605.20745) maintained in landscape and baselines.",
    "FACTUAL_ERROR_ERR_ACCURACY": "Previously resolved (round 3). Numbers now verified via R-PRM Table 1 with proper attribution.",
    "TWO_MODEL_MEMORY_OVERHEAD": "Previously resolved (round 2). Unified single-model architecture maintained.",
    "STEP_DEPENDENCY_IGNORED": "Previously resolved (round 2). SEC enhancement maintained as optional module.",
    "SCE_SIGNAL_REDUNDANCY": "Previously resolved (round 2). Signal ablation ladder (A2) maintained and extended with CoT Entropy.",
    "BUDGET_AWARE_TTS_OVERLAP": "Previously resolved (round 2). Maintained as baseline.",
    "CRITICAL_NOVELTY_F_S_RM": "Previously resolved (rounds 1-2). F/S-RM architecture adopted as foundation with step-level extension.",
    "CRITICAL_NOVELTY_E_GRM": "Previously resolved (rounds 1-2). Differentiated by granularity.",
    "CRITICAL_NOVELTY_CAMEL": "Previously resolved (rounds 1-2). Different target task and granularity."
  }
}

## Reviewer feedback (round 5)
Issues: ["FACTUAL ERROR — CRM MISCHARACTERIZATION: CRM (arXiv 2509.26578) does NOT use 'multiplicative survival decomposition S(t) = Π(1-h(k))' or hazard functions. The paper uses conditional probability modeling to link process rewards to outcomes. The survival analysis framing attributed to CRM is fabricated. This invalidates part of the SEC module's cited theoretical grounding, though PURE's min-form insight still provides partial justification.", "OUTDATED DISCRIMINATIVE SOTA: The proposal treats Qwen2.5-Math-PRM-7B (avg F1 73.5) as the leading discriminative PRM on ProcessBench. However, ACTPRM (arXiv 2601.22249, Jan 2026) achieves F1 75.0, and ASPRM (arXiv 2502.13943, Feb 2026) also claims SOTA. The F1 floor threshold (73.5) and baseline characterization need updating.", "UNVERIFIABLE VENUE CLAIMS: GenPRM 'AAAI 2026', E-GRM 'ACL 2026', CAMEL 'ICML 2026', and ReProbe 'NeurIPS 2025' acceptance claims could not be independently verified. These may be speculative or based on non-public information. Misrepresenting venue acceptance is a serious credibility issue.", "NOVELTY CEILING: After 5 rounds of refinement, the core contribution remains synthesis-level — combining F/S-RM's dual-mode architecture, CoT Entropy, Constrained GRPO, and PURE's min-form insight into a step-level routing framework. While the synthesis is principled and well-motivated, no fundamentally new insight or technique is introduced. The SCE is a standard MLP trained on oracle labels. The routing is a top-k selection. The training uses existing Constrained GRPO. A reviewer might ask: what is the scientific contribution beyond careful engineering?"]
Feedback: Three targeted fixes to reach passing quality:

(1) FIX CRM MISCHARACTERIZATION: Remove the fabricated 'multiplicative survival decomposition S(t) = Π(1-h(k))' and 'hazard function' framing attributed to CRM. CRM actually uses conditional probability modeling to link process to outcome, which DOES support sequential step dependencies — just not through survival analysis. Either correctly characterize what CRM actually does, or find a different citation that genuinely uses survival-theoretic decomposition for step-level credit assignment. PURE's min-form insight alone is sufficient to justify the SEC module; the survival analysis language is unnecessary and creates a factual error.

(2) UPDATE DISCRIMINATIVE SOTA: Acknowledge ACTPRM (arXiv 2601.22249, F1 75.0) and ASPRM (arXiv 2502.13943) as more recent discriminative PRMs that surpass Qwen2.5-Math-PRM-7B. Update the F1 floor threshold to 75.0 or frame it as 'matching the current discriminative SOTA.' Also note the Hard2Verify finding that ProcessBench scores may not generalize — this actually STRENGTHENS the case for deeper verification on frontier problems.

(3) QUALIFY OR REMOVE UNVERIFIABLE VENUE CLAIMS: For papers where conference acceptance cannot be publicly verified (GenPRM, E-GRM, CAMEL, ReProbe), either provide verifiable evidence (e.g., link to proceedings page) or present them as arXiv preprints only. Falsely attributing venue acceptance is a significant credibility risk that reviewers will flag.

Optional improvement for novelty: Articulate a clear 'insight' beyond synthesis. For example: 'The key insight is that verification paradigm selection and verification execution should be decoupled — implicit routing (Dyve) entangles them, creating a ceiling when either component improves independently. CRISP-PRM's modularity means advances in discriminative PRMs, generative PRMs, or uncertainty estimation each independently improve the system without retraining.' This composability-as-a-first-class-design-principle framing would elevate the contribution above pure engineering.

## Instructions
- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.
- Address each issue specifically.

## 深度调研要求

不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。

1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。
2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。
3. **深度思考**：
   - 核心假设是否仍然成立？
   - reviewer 的批评是否揭示了更深层的问题？
   - 有没有更好的 framing 或 approach？
4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。

## 针对 Review 意见的定向搜索

1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点
2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline
3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现
4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot

- You have full freedom: minor fix, major revision, or pivot.
- Include a "change_type" field: "minor", "major", or "pivot".
- Output a COMPLETE JSON object with ALL fields.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "a14d4547-e473-4da0-836a-c0e4d22dabcc",
  "type": "user",
  "uuid": "1c7814b3-f140-4208-b4ed-51c9ed0f8088",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T01:43:06.378Z_

```json
{
  "parentUuid": "1c7814b3-f140-4208-b4ed-51c9ed0f8088",
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
  "uuid": "4db801a6-5a22-4894-b421-81b0d5de7518",
  "timestamp": "2026-05-28T01:43:06.378Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T01:43:06.378Z_

```json
{
  "parentUuid": "4db801a6-5a22-4894-b421-81b0d5de7518",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9ce53e11-bb34-4e00-b36e-bec609f2f1be",
  "timestamp": "2026-05-28T01:43:06.378Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"CRISP-PRM: Criticality-Aware Step-Level Paradigm Selection for Unified…",
  "leafUuid": "9ce53e11-bb34-4e00-b36e-bec609f2f1be",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising CRISP-PRM after round 5 reviewer feedback",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff"
}
```

---

### Assistant

_source line 8 · 2026-05-28T01:43:13.687Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully:

1. **CRM MISCHARACTERIZATION**: The proposal attributes "multiplicative survival decomposition S(t) = Π(1-h(k))" and "hazard functions" to CRM, which is fabricated. I need to find what CRM actually does and correct this.

2. **OUTDATED DISCRIMINATIVE SOTA**: Need to research ACTPRM (arXiv 2601.22249) and ASPRM (arXiv 2502.13943) to update the baseline.


3. **UNVERIFIABLE VENUE CLAIMS**: GenPRM, E-GRM, CAMEL, and ReProbe all have future venue claims that I need to verify or remove since they can't be confirmed yet.

4. **NOVELTY CEILING**: The core contribution needs to be more clearly articulated beyond just combining existing approaches.

I should start by researching these specific papers and verifying the actual claims about CRM before proceeding with revisions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9ce53e11-bb34-4e00-b36e-bec609f2f1be",
  "isSidechain": false,
  "requestId": "req_011CbU7pnX3LBUNkZhAXHqhc",
  "type": "assistant",
  "uuid": "8633ab40-4568-4b93-904f-1829eb725501",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MjXjaNgNYvzPir55nD6gNQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14238,
      "cache_read_input_tokens": 11014,
      "output_tokens": 350,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14238,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 350,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 14238,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14238
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

_source line 9 · 2026-05-28T01:43:13.799Z_

I'll conduct deep research on each of the four reviewer issues before making revisions. Let me launch parallel research agents for the independent topics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8633ab40-4568-4b93-904f-1829eb725501",
  "isSidechain": false,
  "requestId": "req_011CbU7pnX3LBUNkZhAXHqhc",
  "type": "assistant",
  "uuid": "8da05540-bb09-43d7-90c6-692821194d78",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MjXjaNgNYvzPir55nD6gNQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14238,
      "cache_read_input_tokens": 11014,
      "output_tokens": 350,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14238,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 350,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 14238,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14238
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

_source line 10 · 2026-05-28T01:43:14.017Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Dc1Y8FVzVt5HjVXjWsLQj2`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8da05540-bb09-43d7-90c6-692821194d78",
  "isSidechain": false,
  "requestId": "req_011CbU7pnX3LBUNkZhAXHqhc",
  "type": "assistant",
  "uuid": "6bf9e88c-7fa9-4c92-ba93-b9b8c8cfe797",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MjXjaNgNYvzPir55nD6gNQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14238,
      "cache_read_input_tokens": 11014,
      "output_tokens": 350,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14238,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 350,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 14238,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14238
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

_source line 11 · 2026-05-28T01:43:14.024Z_

<details><summary>↩ Tool result · `toolu_01Dc1Y8FVzVt5HjVXjWsLQj2`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6bf9e88c-7fa9-4c92-ba93-b9b8c8cfe797",
  "isSidechain": false,
  "promptId": "a14d4547-e473-4da0-836a-c0e4d22dabcc",
  "type": "user",
  "uuid": "769e8eec-5e31-44f0-acca-8d007e7f84b4",
  "toolUseResult": {
    "matches": [
      "WebFetch",
      "WebSearch"
    ],
    "query": "select:WebFetch,WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "6bf9e88c-7fa9-4c92-ba93-b9b8c8cfe797",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-28T01:43:19.287Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me launch parallel research agents for the four issues:

1. CRM paper - what does it actually do?
2. ACTPRM and ASPRM - updated discriminative SOTA
3. Venue verification for GenPRM, E-GRM, CAMEL, ReProbe
4. Hard2Verify finding about ProcessBench generalization

Let me launch these in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "769e8eec-5e31-44f0-acca-8d007e7f84b4",
  "isSidechain": false,
  "requestId": "req_011CbU7qMLkBzc1QpYHNcMiX",
  "type": "assistant",
  "uuid": "0a091aa9-6327-4dbc-b0c6-c69d0a3d3438",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGZJZzaPQVY5LsaoMPLcqA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1370,
      "cache_read_input_tokens": 25252,
      "output_tokens": 1636,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1370,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1636,
          "cache_read_input_tokens": 25252,
          "cache_creation_input_tokens": 1370,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1370
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

_source line 13 · 2026-05-28T01:43:19.818Z_

Now let me launch parallel research for all four issues simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a091aa9-6327-4dbc-b0c6-c69d0a3d3438",
  "isSidechain": false,
  "requestId": "req_011CbU7qMLkBzc1QpYHNcMiX",
  "type": "assistant",
  "uuid": "3079be3f-1f84-46a4-808a-550a36fc3281",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGZJZzaPQVY5LsaoMPLcqA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1370,
      "cache_read_input_tokens": 25252,
      "output_tokens": 1636,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1370,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1636,
          "cache_read_input_tokens": 25252,
          "cache_creation_input_tokens": 1370,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1370
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

_source line 14 · 2026-05-28T01:43:27.498Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01WQJTsYEfG19c7kfoGacTB1`</summary>

```json
{
  "description": "Research CRM paper accurately",
  "prompt": "I need to understand what CRM (arXiv 2509.26578) actually does. A research proposal incorrectly attributed \"multiplicative survival decomposition S(t) = Π(1-h(k))\" and \"hazard functions\" to CRM, but a reviewer says CRM actually uses \"conditional probability modeling to link process rewards to outcomes.\"\n\nPlease:\n1. Search for \"CRM conditional reward models process-level credit assignment arXiv 2509.26578\"\n2. Fetch the actual arXiv page for this paper\n3. Determine: What is CRM's actual technical approach? How does it model step-level credit assignment? Does it use any form of sequential/multiplicative decomposition, or is it purely conditional probability?\n4. Also search for papers that DO use survival analysis or hazard function decomposition for step-level reasoning credit assignment — is there any legitimate citation for that framing?\n\nReport the actual CRM methodology in detail so I can correct the mischaracterization.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3079be3f-1f84-46a4-808a-550a36fc3281",
  "isSidechain": false,
  "requestId": "req_011CbU7qMLkBzc1QpYHNcMiX",
  "type": "assistant",
  "uuid": "4207ba19-5b80-430a-9e05-06e31e4573e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGZJZzaPQVY5LsaoMPLcqA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1370,
      "cache_read_input_tokens": 25252,
      "output_tokens": 1636,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1370,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1636,
          "cache_read_input_tokens": 25252,
          "cache_creation_input_tokens": 1370,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1370
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

_source line 15 · 2026-05-28T01:43:35.194Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01W3yhyzTAKePskAfK8eTcu3`</summary>

```json
{
  "description": "Research ACTPRM and ASPRM SOTA",
  "prompt": "I need to find updated discriminative PRM state-of-the-art on ProcessBench. Specifically:\n\n1. Search for \"ACTPRM arXiv 2601.22249\" and fetch the paper to find its actual ProcessBench F1 scores. The reviewer claims F1 75.0.\n2. Search for \"ASPRM arXiv 2502.13943\" and fetch the paper to find its ProcessBench F1 scores.\n3. Search for \"Hard2Verify ProcessBench generalization\" — there's apparently a finding that ProcessBench scores may not generalize to frontier problems. Find this paper/result.\n4. Search Papers With Code or recent surveys for \"ProcessBench leaderboard 2026\" to see if there are even newer discriminative PRMs beyond ACTPRM and ASPRM.\n\nFor each paper found, report: full title, arXiv ID, key F1 numbers on ProcessBench (per-subset if available: GSM8K/MATH/OlympiadBench/OmniMATH), and the core technique used. Be precise about numbers — I need exact figures.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4207ba19-5b80-430a-9e05-06e31e4573e3",
  "isSidechain": false,
  "requestId": "req_011CbU7qMLkBzc1QpYHNcMiX",
  "type": "assistant",
  "uuid": "0abb2d85-f4e9-4806-81e6-a2cedadd6eff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGZJZzaPQVY5LsaoMPLcqA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1370,
      "cache_read_input_tokens": 25252,
      "output_tokens": 1636,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1370,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1636,
          "cache_read_input_tokens": 25252,
          "cache_creation_input_tokens": 1370,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1370
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

_source line 16 · 2026-05-28T01:43:45.022Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01DXB3tJpUwWgW7ZAWhCqMs6`</summary>

```json
{
  "description": "Verify venue acceptances",
  "prompt": "I need to verify whether the following papers have been accepted at the claimed venues. For each, search for the paper title + venue to find evidence of acceptance (proceedings pages, official accepted paper lists, author announcements, etc.):\n\n1. GenPRM (arXiv 2504.00891) — claimed \"AAAI 2026\"\n2. E-GRM (arXiv 2604.10072) — claimed \"ACL 2026\"  \n3. CAMEL (arXiv 2602.20670) — claimed \"ICML 2026\"\n4. ReProbe/UHeads (arXiv 2511.06209) — claimed \"NeurIPS 2025\"\n5. SCAN (arXiv 2509.16548) — claimed \"NeurIPS 2025\"\n6. Dyve (arXiv 2502.11157) — claimed \"EMNLP 2025\"\n7. ProcessBench (arXiv 2412.06559) — claimed \"ACL 2025\"\n8. R-PRM (arXiv 2503.21295) — claimed \"EMNLP 2025\"\n\nFor each paper:\n- Search for \"[paper title] accepted [venue]\" or \"[paper title] [venue year] proceedings\"\n- Check the arXiv page for any venue annotations\n- Report: VERIFIED (with evidence), UNVERIFIABLE (no public evidence found), or INCORRECT (evidence contradicts claim)\n\nToday's date is 2026-05-28. Some venues like ICML 2026 and ACL 2026 may not have announced acceptances yet. Note that clearly.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0abb2d85-f4e9-4806-81e6-a2cedadd6eff",
  "isSidechain": false,
  "requestId": "req_011CbU7qMLkBzc1QpYHNcMiX",
  "type": "assistant",
  "uuid": "f1aaab31-05cf-4306-85fe-96a8326017df",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGZJZzaPQVY5LsaoMPLcqA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1370,
      "cache_read_input_tokens": 25252,
      "output_tokens": 1636,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1370,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1636,
          "cache_read_input_tokens": 25252,
          "cache_creation_input_tokens": 1370,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1370
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

_source line 17 · 2026-05-28T01:43:54.720Z_

<details open><summary>🔧 Tool call — Agent · `toolu_011vRA5n6vYu81vnf1vzRVir`</summary>

```json
{
  "description": "Research composability as contribution",
  "prompt": "I'm working on a research proposal about step-level verification paradigm routing for process reward models (PRMs). A reviewer has flagged that the core contribution is \"synthesis-level\" — combining existing techniques (dual-mode architecture, uncertainty estimation, constrained RL, min-form credit assignment) without a fundamentally new insight.\n\nThe reviewer suggested framing \"composability as a first-class design principle\" — that verification paradigm selection should be decoupled from verification execution, and this modularity means advances in discriminative PRMs, generative PRMs, or uncertainty estimation each independently improve the system.\n\nHelp me research:\n1. Search for \"composable machine learning systems modular design\" and \"decoupled routing verification\" to find precedents where modularity/composability was itself the scientific contribution\n2. Search for \"implicit vs explicit routing machine learning\" or \"entangled vs disentangled routing\" to find formal frameworks for understanding why decoupled routing is better\n3. Search for \"mixture of experts routing analysis\" or \"adaptive computation routing theory\" — MoE literature has extensive analysis of when explicit routing outperforms implicit routing\n4. Search for recent papers (2025-2026) that make \"architectural composability\" or \"modular verification\" their primary contribution in NLP/reasoning\n\nI need concrete intellectual framing to elevate the contribution beyond \"careful engineering.\" What theoretical or empirical arguments exist for why decoupled/explicit routing is fundamentally better than entangled/implicit routing?",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1aaab31-05cf-4306-85fe-96a8326017df",
  "isSidechain": false,
  "requestId": "req_011CbU7qMLkBzc1QpYHNcMiX",
  "type": "assistant",
  "uuid": "dedaca19-d383-4bd2-b295-40f4f09c0f7d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LGZJZzaPQVY5LsaoMPLcqA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1370,
      "cache_read_input_tokens": 25252,
      "output_tokens": 1636,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1370,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1636,
          "cache_read_input_tokens": 25252,
          "cache_creation_input_tokens": 1370,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1370
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

_source line 18 · 2026-05-28T01:45:17.990Z_

<details><summary>↩ Tool result · `toolu_01WQJTsYEfG19c7kfoGacTB1`</summary>

```text
I now have a comprehensive picture. Here is my detailed report.

---

## CRM: Actual Technical Methodology (arXiv 2509.26578)

**Paper:** "Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning" by Zheng Zhang, Ziwei Shan, Kaitao Song, Yexin Li, and Kan Ren (September 2025).

### What CRM Actually Does

CRM models multi-step LLM reasoning as a temporal process by defining a random variable **z** as the index of the first step where the reasoning trajectory enters a wrong state. From this, it builds:

- **W(t) = Pr(z <= t):** cumulative probability of having entered a wrong state by step t
- **S(t) = Pr(z > t) = 1 - W(t):** probability of maintaining correct reasoning through step t
- **p(t) = Pr(z = t):** probability mass that the wrong state is entered at exactly step t
- **h(t) = Pr(z = t | z >= t) = p(t) / S(t-1):** conditional probability of failing at step t, given all prior steps were correct

### The Core Decomposition -- It IS Multiplicative

Critically, CRM **does** use a multiplicative/product decomposition:

**S(t) = Product from k=1 to t of (1 - h(k))**

This expresses the probability of reaching a correct final answer as the product of per-step "survival" probabilities. Similarly:

**p(t) = h(t) * Product from k=1 to t-1 of (1 - h(k))**

### Step-Level Rewards via Potential-Based Reward Shaping (PBRS)

CRM defines a potential function:

**Phi(s_t) = log S(t) = Sum from k=1 to t of log(1 - h(k))**

The step reward is then:

**r_t = log(1 - h(t))**

So the trajectory-level outcome decomposes as:

**S(T) = Product from t=1 to T of (1 - h(t)) = Product from t=1 to T of exp(r_t)**

### Training Loss

For correct trajectories (label l=1): L_S = -log S(T) = -log[Product(1-h(t))]

For incorrect trajectories (label l=0): L_W = -log(1 - S(T)) and L_z = -log p(z_i) = -log[h(z_i) * Product from t=1 to z_i-1 of (1-h(t))]

Combined: L = (1/|D|) * Sum of [l_i * L_S + (1-l_i) * (L_W + L_z)]

---

### The Key Finding: The Research Proposal Was *Partially* Right, Not Entirely Wrong

Here is the nuance that matters:

1. **The multiplicative survival decomposition S(t) = Product(1-h(k)) IS actually in CRM.** The research proposal's attribution of this formula to CRM is **correct**, not a mischaracterization. This is the literal core equation of the paper.

2. **However**, the authors of CRM **never use survival analysis terminology**. They do not call h(t) a "hazard function," do not call S(t) a "survival function," and do not cite any survival analysis literature. They frame everything as "conditional probability modeling" and "conditional reward modeling." The mathematical structure is isomorphic to a discrete-time survival model, but the authors deliberately chose conditional probability framing.

3. **So the reviewer's objection has a valid point:** If the research proposal described CRM as using "hazard functions" and "survival analysis," that terminology is imposed by the proposal author -- it is not the language CRM's own authors use. CRM describes itself as using "conditional probability modeling to link process rewards to outcomes," which matches what the reviewer said.

4. **But the reviewer may be overcorrecting** if they claim CRM does not use multiplicative decomposition at all. It absolutely does -- S(t) = Product(1-h(k)) is the foundational equation of the entire paper.

### The Correct Characterization

CRM uses **conditional probability chain rules** to decompose the probability of reaching a correct answer into a product of per-step conditional probabilities. Mathematically, this is identical to a discrete-time survival model (h(t) is functionally a discrete hazard rate, S(t) is functionally a survival function), but the paper frames it purely in terms of conditional probability and causal reasoning, not survival analysis.

### Does Any Paper Explicitly Use Survival Analysis for Step-Level Credit Assignment?

Based on my searches: **No.** I found no paper that explicitly applies survival analysis or hazard function methodology (by name) to step-level reasoning credit assignment in LLMs. The connection is implicit in CRM's math but never stated. Related work includes:

- **"Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning"** (arXiv 2504.15275) -- uses min-form rather than sum-form value functions, but not survival analysis
- **LC-ERD** -- uses IGM principle from multi-agent RL for reward decomposition
- **GRPO-lambda** -- credit assignment via advantage estimation
- **CAPO** -- generative credit assignment

None of these use survival analysis terminology or framework.

### Recommendation for Correcting the Proposal

The proposal should:
1. **Keep** the reference to multiplicative decomposition S(t) = Product(1-h(k)) as being from CRM -- this is accurate
2. **Remove** the terms "hazard function" and "survival analysis" when describing CRM -- the authors do not use these terms
3. **Describe CRM as** using "conditional probability chain rules to decompose trajectory-level correctness probability into per-step conditional probabilities, where h(t) = Pr(z=t|z>=t) represents the conditional probability of entering a wrong state at step t given prior steps were correct"
4. **If the proposal wants to draw a connection to survival analysis**, it should frame this as the proposal's own novel observation (e.g., "We note that CRM's formulation is mathematically isomorphic to a discrete-time survival model") rather than attributing survival analysis framing to CRM itself

Sources:
- [CRM Paper - arXiv](https://arxiv.org/abs/2509.26578)
- [CRM HTML Version](https://arxiv.org/html/2509.26578)
- [CRM Project Page](https://foundation-model-research.github.io/CRM/)
- [OpenReview Submission](https://openreview.net/forum?id=4DJoBOQNd0)
- [Stop Summation (Min-Form Credit Assignment)](https://arxiv.org/abs/2504.15275)
- [Step-Level Credit Assignment Overview](https://www.emergentmind.com/topics/step-level-credit-assignment)
- [Reward Modeling Survey](https://arxiv.org/pdf/2602.09305)

agentId: ae6a971c22e7b499f (use SendMessage with to: 'ae6a971c22e7b499f' to continue this agent)
&lt;usage>total_tokens: 20901
tool_uses: 14
duration_ms: 110486&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4207ba19-5b80-430a-9e05-06e31e4573e3",
  "isSidechain": false,
  "promptId": "a14d4547-e473-4da0-836a-c0e4d22dabcc",
  "type": "user",
  "uuid": "9b2152fc-e865-4295-9dca-8cc39224333f",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to understand what CRM (arXiv 2509.26578) actually does. A research proposal incorrectly attributed \"multiplicative survival decomposition S(t) = Π(1-h(k))\" and \"hazard functions\" to CRM, but a reviewer says CRM actually uses \"conditional probability modeling to link process rewards to outcomes.\"\n\nPlease:\n1. Search for \"CRM conditional reward models process-level credit assignment arXiv 2509.26578\"\n2. Fetch the actual arXiv page for this paper\n3. Determine: What is CRM's actual technical approach? How does it model step-level credit assignment? Does it use any form of sequential/multiplicative decomposition, or is it purely conditional probability?\n4. Also search for papers that DO use survival analysis or hazard function decomposition for step-level reasoning credit assignment — is there any legitimate citation for that framing?\n\nReport the actual CRM methodology in detail so I can correct the mischaracterization.",
    "agentId": "ae6a971c22e7b499f",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have a comprehensive picture. Here is my detailed report.\n\n---\n\n## CRM: Actual Technical Methodology (arXiv 2509.26578)\n\n**Paper:** \"Linking Process to Outcome: Conditional Reward Modeling for LLM Reasoning\" by Zheng Zhang, Ziwei Shan, Kaitao Song, Yexin Li, and Kan Ren (September 2025).\n\n### What CRM Actually Does\n\nCRM models multi-step LLM reasoning as a temporal process by defining a random variable **z** as the index of the first step where the reasoning trajectory enters a wrong state. From this, it builds:\n\n- **W(t) = Pr(z <= t):** cumulative probability of having entered a wrong state by step t\n- **S(t) = Pr(z > t) = 1 - W(t):** probability of maintaining correct reasoning through step t\n- **p(t) = Pr(z = t):** probability mass that the wrong state is entered at exactly step t\n- **h(t) = Pr(z = t | z >= t) = p(t) / S(t-1):** conditional probability of failing at step t, given all prior steps were correct\n\n### The Core Decomposition -- It IS Multiplicative\n\nCritically, CRM **does** use a multiplicative/product decomposition:\n\n**S(t) = Product from k=1 to t of (1 - h(k))**\n\nThis expresses the probability of reaching a correct final answer as the product of per-step \"survival\" probabilities. Similarly:\n\n**p(t) = h(t) * Product from k=1 to t-1 of (1 - h(k))**\n\n### Step-Level Rewards via Potential-Based Reward Shaping (PBRS)\n\nCRM defines a potential function:\n\n**Phi(s_t) = log S(t) = Sum from k=1 to t of log(1 - h(k))**\n\nThe step reward is then:\n\n**r_t = log(1 - h(t))**\n\nSo the trajectory-level outcome decomposes as:\n\n**S(T) = Product from t=1 to T of (1 - h(t)) = Product from t=1 to T of exp(r_t)**\n\n### Training Loss\n\nFor correct trajectories (label l=1): L_S = -log S(T) = -log[Product(1-h(t))]\n\nFor incorrect trajectories (label l=0): L_W = -log(1 - S(T)) and L_z = -log p(z_i) = -log[h(z_i) * Product from t=1 to z_i-1 of (1-h(t))]\n\nCombined: L = (1/|D|) * Sum of [l_i * L_S + (1-l_i) * (L_W + L_z)]\n\n---\n\n### The Key Finding: The Research Proposal Was *Partially* Right, Not Entirely Wrong\n\nHere is the nuance that matters:\n\n1. **The multiplicative survival decomposition S(t) = Product(1-h(k)) IS actually in CRM.** The research proposal's attribution of this formula to CRM is **correct**, not a mischaracterization. This is the literal core equation of the paper.\n\n2. **However**, the authors of CRM **never use survival analysis terminology**. They do not call h(t) a \"hazard function,\" do not call S(t) a \"survival function,\" and do not cite any survival analysis literature. They frame everything as \"conditional probability modeling\" and \"conditional reward modeling.\" The mathematical structure is isomorphic to a discrete-time survival model, but the authors deliberately chose conditional probability framing.\n\n3. **So the reviewer's objection has a valid point:** If the research proposal described CRM as using \"hazard functions\" and \"survival analysis,\" that terminology is imposed by the proposal author -- it is not the language CRM's own authors use. CRM describes itself as using \"conditional probability modeling to link process rewards to outcomes,\" which matches what the reviewer said.\n\n4. **But the reviewer may be overcorrecting** if they claim CRM does not use multiplicative decomposition at all. It absolutely does -- S(t) = Product(1-h(k)) is the foundational equation of the entire paper.\n\n### The Correct Characterization\n\nCRM uses **conditional probability chain rules** to decompose the probability of reaching a correct answer into a product of per-step conditional probabilities. Mathematically, this is identical to a discrete-time survival model (h(t) is functionally a discrete hazard rate, S(t) is functionally a survival function), but the paper frames it purely in terms of conditional probability and causal reasoning, not survival analysis.\n\n### Does Any Paper Explicitly Use Survival Analysis for Step-Level Credit Assignment?\n\nBased on my searches: **No.** I found no paper that explicitly applies survival analysis or hazard function methodology (by name) to step-level reasoning credit assignment in LLMs. The connection is implicit in CRM's math but never stated. Related work includes:\n\n- **\"Stop Summation: Min-Form Credit Assignment Is All Process Reward Model Needs for Reasoning\"** (arXiv 2504.15275) -- uses min-form rather than sum-form value functions, but not survival analysis\n- **LC-ERD** -- uses IGM principle from multi-agent RL for reward decomposition\n- **GRPO-lambda** -- credit assignment via advantage estimation\n- **CAPO** -- generative credit assignment\n\nNone of these use survival analysis terminology or framework.\n\n### Recommendation for Correcting the Proposal\n\nThe proposal should:\n1. **Keep** the reference to multiplicative decomposition S(t) = Product(1-h(k)) as being from CRM -- this is accurate\n2. **Remove** the terms \"hazard function\" and \"survival analysis\" when describing CRM -- the authors do not use these terms\n3. **Describe CRM as** using \"conditional probability chain rules to decompose trajectory-level correctness probability into per-step conditional probabilities, where h(t) = Pr(z=t|z>=t) represents the conditional probability of entering a wrong state at step t given prior steps were correct\"\n4. **If the proposal wants to draw a connection to survival analysis**, it should frame this as the proposal's own novel observation (e.g., \"We note that CRM's formulation is mathematically isomorphic to a discrete-time survival model\") rather than attributing survival analysis framing to CRM itself\n\nSources:\n- [CRM Paper - arXiv](https://arxiv.org/abs/2509.26578)\n- [CRM HTML Version](https://arxiv.org/html/2509.26578)\n- [CRM Project Page](https://foundation-model-research.github.io/CRM/)\n- [OpenReview Submission](https://openreview.net/forum?id=4DJoBOQNd0)\n- [Stop Summation (Min-Form Credit Assignment)](https://arxiv.org/abs/2504.15275)\n- [Step-Level Credit Assignment Overview](https://www.emergentmind.com/topics/step-level-credit-assignment)\n- [Reward Modeling Survey](https://arxiv.org/pdf/2602.09305)"
      }
    ],
    "totalDurationMs": 110486,
    "totalTokens": 20901,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1255,
      "cache_read_input_tokens": 17934,
      "output_tokens": 1711,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1255
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1711,
          "cache_read_input_tokens": 17934,
          "cache_creation_input_tokens": 1255,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1255,
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
      "otherToolCount": 14
    }
  },
  "sourceToolAssistantUUID": "4207ba19-5b80-430a-9e05-06e31e4573e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
  "version": "2.1.142",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"CRISP-PRM: Criticality-Aware Step-Level Paradigm Selection for Unified…",
  "leafUuid": "9b2152fc-e865-4295-9dca-8cc39224333f",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising CRISP-PRM after round 5 reviewer feedback",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff"
}
```

---

### Tool result

_source line 21 · 2026-05-28T01:46:56.973Z_

<details><summary>↩ Tool result · `toolu_01DXB3tJpUwWgW7ZAWhCqMs6`</summary>

```text
Now I have comprehensive evidence for all 8 papers. Let me compile the final report.

Here is my verification report for each paper:

---

## Paper Venue Verification Report (as of 2026-05-28)

### 1. GenPRM (arXiv 2504.00891) -- claimed "AAAI 2026"
**VERIFIED**

Evidence:
- The official GitHub repository ([github.com/RyanLiu112/GenPRM](https://github.com/RyanLiu112/GenPRM)) is tagged "[AAAI 2026]" and contains the news item: "2025-11-08: GenPRM is accepted by AAAI 2026!"
- AAAI 2026 (the 40th AAAI Conference) took place January 20-27, 2026, in Singapore, and proceedings have been published at [aaai.org/proceeding/aaai-40-2026/](https://aaai.org/proceeding/aaai-40-2026/).
- Note: The arXiv abstract page itself does not carry a venue annotation in the Comments field, but the author's GitHub repo clearly states acceptance.

---

### 2. E-GRM (arXiv 2604.10072) -- claimed "ACL 2026"
**VERIFIED**

Evidence:
- The arXiv abstract page explicitly states in the Comments field: **"accepted by ACL 2026"**.
- ACL 2026 is scheduled for July 2-7, 2026. The official accepted papers page at [2026.aclweb.org/program/accepted_papers/](https://2026.aclweb.org/program/accepted_papers/) currently shows "Coming soon!" so the full list is not yet publicly posted, but the arXiv self-annotation is a strong standard indicator of acceptance.

---

### 3. CAMEL (arXiv 2602.20670) -- claimed "ICML 2026"
**VERIFIED**

Evidence:
- The arXiv abstract page states **"ICML 2026"** in the Comments field.
- The official ICML 2026 Downloads page at [icml.cc/Downloads/2026](https://icml.cc/Downloads/2026) lists "CAMEL: Confidence-Gated Reflection for Reward Modeling" as a poster (linking to `/virtual/2026/poster/62424`).
- ICML 2026 is scheduled for July 6-11, 2026, in Seoul, South Korea.

---

### 4. ReProbe/UHeads (arXiv 2511.06209) -- claimed "NeurIPS 2025"
**INCORRECT** -- The paper was accepted at **ACL 2026**, not NeurIPS 2025.

Evidence:
- The arXiv abstract page states **"ACL 2026 Main"** in the Comments field.
- The paper's project page at [reprobe.github.io](https://reprobe.github.io/) explicitly labels it as **"ACL 2026 - Long Paper"** and cites it as appearing in "Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics."
- No evidence of NeurIPS 2025 acceptance was found anywhere.

---

### 5. SCAN (arXiv 2509.16548) -- claimed "NeurIPS 2025"
**VERIFIED**

Evidence:
- The arXiv abstract page states **"NeurIPS 2025"** in the Comments field along with a project page link.
- The official NeurIPS 2025 virtual site hosts the poster page at [neurips.cc/virtual/2025/poster/116534](https://neurips.cc/virtual/2025/poster/116534), confirming the paper was presented as a poster on Friday, December 5, 2025, 4:30-7:30 PM PST.
- NeurIPS 2025 took place in San Diego in December 2025.

---

### 6. Dyve (arXiv 2502.11157) -- claimed "EMNLP 2025"
**VERIFIED**

Evidence:
- The paper appears in the ACL Anthology at [aclanthology.org/2025.emnlp-main.1136/](https://aclanthology.org/2025.emnlp-main.1136/) in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pages 22320-22333, Suzhou, China, November 2025.
- DOI: 10.18653/v1/2025.emnlp-main.1136.

---

### 7. ProcessBench (arXiv 2412.06559) -- claimed "ACL 2025"
**VERIFIED**

Evidence:
- The arXiv abstract page states **"ACL 2025"** in the Comments field.
- The paper appears in the ACL Anthology at [aclanthology.org/2025.acl-long.50/](https://aclanthology.org/2025.acl-long.50/) in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 1009-1024, Vienna, Austria.
- The official GitHub repo ([github.com/QwenLM/ProcessBench](https://github.com/QwenLM/ProcessBench)) also labels itself as the "Official repository for ACL 2025 paper."

---

### 8. R-PRM (arXiv 2503.21295) -- claimed "EMNLP 2025"
**VERIFIED**

Evidence:
- The paper appears in the ACL Anthology at [aclanthology.org/2025.emnlp-main.679/](https://aclanthology.org/2025.emnlp-main.679/) in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pages 13438-13451, Suzhou, China, November 2025.
- DOI: 10.18653/v1/2025.emnlp-main.679.
- Note: The arXiv abstract page does not carry a venue annotation, but the ACL Anthology publication is definitive proof.

---

## Summary

| # | Paper | Claimed Venue | Status |
|---|-------|--------------|--------|
| 1 | GenPRM | AAAI 2026 | VERIFIED |
| 2 | E-GRM | ACL 2026 | VERIFIED |
| 3 | CAMEL | ICML 2026 | VERIFIED |
| 4 | ReProbe/UHeads | NeurIPS 2025 | **INCORRECT** (actual: ACL 2026 Main) |
| 5 | SCAN | NeurIPS 2025 | VERIFIED |
| 6 | Dyve | EMNLP 2025 | VERIFIED |
| 7 | ProcessBench | ACL 2025 | VERIFIED |
| 8 | R-PRM | EMNLP 2025 | VERIFIED |

**7 out of 8 claims verified. 1 claim (ReProbe/UHeads) is incorrect** -- the paper was accepted at ACL 2026, not NeurIPS 2025. Note that ACL 2026 (July 2-7, 2026) and ICML 2026 (July 6-11, 2026) have not yet taken place, so while acceptance notifications have been issued, the papers have not yet been formally presented.

agentId: a62f67e1be0d3563a (use SendMessage with to: 'a62f67e1be0d3563a' to continue this agent)
&lt;usage>total_tokens: 35053
tool_uses: 43
duration_ms: 191946&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1aaab31-05cf-4306-85fe-96a8326017df",
  "isSidechain": false,
  "promptId": "a14d4547-e473-4da0-836a-c0e4d22dabcc",
  "type": "user",
  "uuid": "2380f743-f42e-427c-9772-6ae21bc7ff5a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify whether the following papers have been accepted at the claimed venues. For each, search for the paper title + venue to find evidence of acceptance (proceedings pages, official accepted paper lists, author announcements, etc.):\n\n1. GenPRM (arXiv 2504.00891) — claimed \"AAAI 2026\"\n2. E-GRM (arXiv 2604.10072) — claimed \"ACL 2026\"  \n3. CAMEL (arXiv 2602.20670) — claimed \"ICML 2026\"\n4. ReProbe/UHeads (arXiv 2511.06209) — claimed \"NeurIPS 2025\"\n5. SCAN (arXiv 2509.16548) — claimed \"NeurIPS 2025\"\n6. Dyve (arXiv 2502.11157) — claimed \"EMNLP 2025\"\n7. ProcessBench (arXiv 2412.06559) — claimed \"ACL 2025\"\n8. R-PRM (arXiv 2503.21295) — claimed \"EMNLP 2025\"\n\nFor each paper:\n- Search for \"[paper title] accepted [venue]\" or \"[paper title] [venue year] proceedings\"\n- Check the arXiv page for any venue annotations\n- Report: VERIFIED (with evidence), UNVERIFIABLE (no public evidence found), or INCORRECT (evidence contradicts claim)\n\nToday's date is 2026-05-28. Some venues like ICML 2026 and ACL 2026 may not have announced acceptances yet. Note that clearly.",
    "agentId": "a62f67e1be0d3563a",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive evidence for all 8 papers. Let me compile the final report.\n\nHere is my verification report for each paper:\n\n---\n\n## Paper Venue Verification Report (as of 2026-05-28)\n\n### 1. GenPRM (arXiv 2504.00891) -- claimed \"AAAI 2026\"\n**VERIFIED**\n\nEvidence:\n- The official GitHub repository ([github.com/RyanLiu112/GenPRM](https://github.com/RyanLiu112/GenPRM)) is tagged \"[AAAI 2026]\" and contains the news item: \"2025-11-08: GenPRM is accepted by AAAI 2026!\"\n- AAAI 2026 (the 40th AAAI Conference) took place January 20-27, 2026, in Singapore, and proceedings have been published at [aaai.org/proceeding/aaai-40-2026/](https://aaai.org/proceeding/aaai-40-2026/).\n- Note: The arXiv abstract page itself does not carry a venue annotation in the Comments field, but the author's GitHub repo clearly states acceptance.\n\n---\n\n### 2. E-GRM (arXiv 2604.10072) -- claimed \"ACL 2026\"\n**VERIFIED**\n\nEvidence:\n- The arXiv abstract page explicitly states in the Comments field: **\"accepted by ACL 2026\"**.\n- ACL 2026 is scheduled for July 2-7, 2026. The official accepted papers page at [2026.aclweb.org/program/accepted_papers/](https://2026.aclweb.org/program/accepted_papers/) currently shows \"Coming soon!\" so the full list is not yet publicly posted, but the arXiv self-annotation is a strong standard indicator of acceptance.\n\n---\n\n### 3. CAMEL (arXiv 2602.20670) -- claimed \"ICML 2026\"\n**VERIFIED**\n\nEvidence:\n- The arXiv abstract page states **\"ICML 2026\"** in the Comments field.\n- The official ICML 2026 Downloads page at [icml.cc/Downloads/2026](https://icml.cc/Downloads/2026) lists \"CAMEL: Confidence-Gated Reflection for Reward Modeling\" as a poster (linking to `/virtual/2026/poster/62424`).\n- ICML 2026 is scheduled for July 6-11, 2026, in Seoul, South Korea.\n\n---\n\n### 4. ReProbe/UHeads (arXiv 2511.06209) -- claimed \"NeurIPS 2025\"\n**INCORRECT** -- The paper was accepted at **ACL 2026**, not NeurIPS 2025.\n\nEvidence:\n- The arXiv abstract page states **\"ACL 2026 Main\"** in the Comments field.\n- The paper's project page at [reprobe.github.io](https://reprobe.github.io/) explicitly labels it as **\"ACL 2026 - Long Paper\"** and cites it as appearing in \"Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics.\"\n- No evidence of NeurIPS 2025 acceptance was found anywhere.\n\n---\n\n### 5. SCAN (arXiv 2509.16548) -- claimed \"NeurIPS 2025\"\n**VERIFIED**\n\nEvidence:\n- The arXiv abstract page states **\"NeurIPS 2025\"** in the Comments field along with a project page link.\n- The official NeurIPS 2025 virtual site hosts the poster page at [neurips.cc/virtual/2025/poster/116534](https://neurips.cc/virtual/2025/poster/116534), confirming the paper was presented as a poster on Friday, December 5, 2025, 4:30-7:30 PM PST.\n- NeurIPS 2025 took place in San Diego in December 2025.\n\n---\n\n### 6. Dyve (arXiv 2502.11157) -- claimed \"EMNLP 2025\"\n**VERIFIED**\n\nEvidence:\n- The paper appears in the ACL Anthology at [aclanthology.org/2025.emnlp-main.1136/](https://aclanthology.org/2025.emnlp-main.1136/) in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pages 22320-22333, Suzhou, China, November 2025.\n- DOI: 10.18653/v1/2025.emnlp-main.1136.\n\n---\n\n### 7. ProcessBench (arXiv 2412.06559) -- claimed \"ACL 2025\"\n**VERIFIED**\n\nEvidence:\n- The arXiv abstract page states **\"ACL 2025\"** in the Comments field.\n- The paper appears in the ACL Anthology at [aclanthology.org/2025.acl-long.50/](https://aclanthology.org/2025.acl-long.50/) in the Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 1009-1024, Vienna, Austria.\n- The official GitHub repo ([github.com/QwenLM/ProcessBench](https://github.com/QwenLM/ProcessBench)) also labels itself as the \"Official repository for ACL 2025 paper.\"\n\n---\n\n### 8. R-PRM (arXiv 2503.21295) -- claimed \"EMNLP 2025\"\n**VERIFIED**\n\nEvidence:\n- The paper appears in the ACL Anthology at [aclanthology.org/2025.emnlp-main.679/](https://aclanthology.org/2025.emnlp-main.679/) in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing, pages 13438-13451, Suzhou, China, November 2025.\n- DOI: 10.18653/v1/2025.emnlp-main.679.\n- Note: The arXiv abstract page does not carry a venue annotation, but the ACL Anthology publication is definitive proof.\n\n---\n\n## Summary\n\n| # | Paper | Claimed Venue | Status |\n|---|-------|--------------|--------|\n| 1 | GenPRM | AAAI 2026 | VERIFIED |\n| 2 | E-GRM | ACL 2026 | VERIFIED |\n| 3 | CAMEL | ICML 2026 | VERIFIED |\n| 4 | ReProbe/UHeads | NeurIPS 2025 | **INCORRECT** (actual: ACL 2026 Main) |\n| 5 | SCAN | NeurIPS 2025 | VERIFIED |\n| 6 | Dyve | EMNLP 2025 | VERIFIED |\n| 7 | ProcessBench | ACL 2025 | VERIFIED |\n| 8 | R-PRM | EMNLP 2025 | VERIFIED |\n\n**7 out of 8 claims verified. 1 claim (ReProbe/UHeads) is incorrect** -- the paper was accepted at ACL 2026, not NeurIPS 2025. Note that ACL 2026 (July 2-7, 2026) and ICML 2026 (July 6-11, 2026) have not yet taken place, so while acceptance notifications have been issued, the papers have not yet been formally presented."
      }
    ],
    "totalDurationMs": 191946,
    "totalTokens": 35053,
    "totalToolUseCount": 43,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 907,
      "cache_read_input_tokens": 32297,
      "output_tokens": 1848,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 907
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1848,
          "cache_read_input_tokens": 32297,
          "cache_creation_input_tokens": 907,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 907,
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
      "otherToolCount": 43
    }
  },
  "sourceToolAssistantUUID": "f1aaab31-05cf-4306-85fe-96a8326017df",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-28T01:47:36.425Z_

<details><summary>↩ Tool result · `toolu_011vRA5n6vYu81vnf1vzRVir`</summary>

```text
Now I have comprehensive material to synthesize. Here is the research synthesis:

---

## Research Synthesis: Theoretical and Empirical Foundations for Decoupled Verification Paradigm Routing

### 1. Composability/Modularity as a First-Class Scientific Contribution

Several recent papers establish that **modularity itself is the contribution**, not merely an engineering convenience:

**"Modular Machine Learning: An Indispensable Path towards New-Generation Large Language Models"** (Wang et al., April 2025, [arXiv:2504.20020](https://arxiv.org/abs/2504.20020)) explicitly argues that the MML paradigm is indispensable for next-generation LLMs, decomposing complex structures into three interdependent components: modular representation, modular model, and modular reasoning. The paper frames modularity as enabling counterfactual reasoning, mitigating hallucinations, and promoting fairness/safety/transparency -- i.e., capabilities that monolithic architectures fundamentally cannot provide.

**"Modular Deep Learning"** (Pfeiffer, Ruder, Vulic, Ponti, 2023, [arXiv:2302.11529](https://arxiv.org/abs/2302.11529)) is the canonical survey that establishes the theoretical framework. It decomposes modular architectures into four dimensions: **routing function**, **computation function**, **aggregation function**, and **training setting**. Crucially, it argues that "these properties enable positive transfer and systematic generalization by **separating computation from routing** and updating modules locally." This separation is presented as the theoretical reason modularity works, not just an implementation detail.

**"Separation of Concerns in Reinforcement Learning"** ([arXiv:1612.05159](https://arxiv.org/abs/1612.05159)) provides a formal framework for decomposing a single-agent task into multiple agents, each focusing on different aspects. This is directly analogous to your proposal of separating verification paradigm selection from verification execution.

### 2. Why Decoupled/Explicit Routing is Fundamentally Better Than Entangled/Implicit Routing

This is where the MoE literature provides your strongest theoretical ammunition:

**Grouter: Decoupling Routing from Representation** (ICML 2026, [arXiv:2603.06626](https://arxiv.org/abs/2603.06626)) is perhaps your single most important citation. It demonstrates that traditional MoE training "requires the model to simultaneously train expert weights while searching for an optimal routing policy within a vast combinatorial space." By **decoupling routing topology from representation**, Grouter eliminates optimization interference, boosts pre-training data utilization by 4.28x, and achieves 33.5% throughput acceleration. The key insight: when routing and computation are entangled, each interferes with the other's optimization landscape.

**StableMoE** (ACL 2022, [arXiv:2204.08396](https://arxiv.org/abs/2204.08396)) provides the theoretical diagnosis of **routing fluctuation**: when routing is entangled with representation learning, the target expert of the same input may change during training, but only one expert is activated during inference. This harms sample efficiency because the same input updates different experts but only one is finally used. StableMoE's solution -- distilling a lightweight router decoupled from the backbone, then freezing it -- directly validates the principle that decoupling routing from execution improves both convergence speed and performance.

**"Routers Learn the Geometry of Their Experts"** (Ahrac et al., May 2026, [arXiv:2605.12476](https://arxiv.org/abs/2605.12476)) reveals a **geometric coupling** between routers and experts: router weights and expert weights receive gradients along the same input direction, differing only in scalar coefficients. This coupling means entangled training creates mutual interference -- the router cannot freely optimize routing without distorting expert representations, and vice versa.

**"The Myth of Expert Specialization in MoEs"** (April 2026, [arXiv:2604.09780](https://arxiv.org/html/2604.09780v1)) further undermines entangled routing by showing that what appears to be domain-specific expert specialization is actually a consequence of the geometry of hidden states, not genuine domain expertise. This means entangled routing decisions are driven by representational artifacts rather than task-relevant properties -- a strong argument for explicit, purpose-built routing.

**Representation Collapse** ([arXiv:2204.09179](https://arxiv.org/abs/2204.09179), [arXiv:2406.15883](https://arxiv.org/pdf/2406.15883)) documents that entangled routing in sparse MoE leads to representation collapse, where experts converge to similar outputs. The router encouraging "token clustering around expert centroids" actively harms specialization. Decoupled routing avoids this pathology.

### 3. The "Fixes That Fail" Argument: Why Independent Improvability Requires Decoupling

**"Fixes That Fail: Self-Defeating Improvements in Machine-Learning Systems"** (NeurIPS 2021, [arXiv:2103.11766](https://arxiv.org/abs/2103.11766)) provides a formal error decomposition showing that in composed ML systems, **improving one model can deteriorate downstream model performance, even after retraining**. This is caused by entanglement between models. This directly supports your "composability as first-class design principle" framing: unless routing is decoupled from verification execution, improving the discriminative PRM, the generative PRM, or the uncertainty estimator can make the overall system worse. Decoupled interfaces are the formal requirement for independent improvability.

**"Joint Training of Deep Ensembles Fails Due to Learner Collusion"** ([arXiv:2301.11323](https://arxiv.org/pdf/2301.11323)) shows that joint optimization of ensemble loss results in degenerate behavior, with base learners colluding to artificially inflate apparent diversity. This is a strong analogy to why jointly optimizing a router and verifiers in an entangled fashion leads to suboptimal verification.

The decoupled optimization literature also supports this: entangled optimization of strategy selection and response generation introduces **gradient conflicts and preference bias**, whereas decoupling avoids these issues and yields significant performance improvements.

### 4. Paradigm Routing as a Recognized Research Direction

**"Select-then-Solve: Paradigm Routing as Inference-Time Optimization for LLM Agents"** (April 2026, [arXiv:2604.06753](https://arxiv.org/abs/2604.06753)) is extremely close to your proposal. It shows that across six inference-time paradigms (Direct, CoT, ReAct, Plan-Execute, Reflection, ReCode), **no single paradigm dominates** -- oracle per-task selection beats the best fixed paradigm by 17.1pp. A lightweight embedding-based router recovers up to 37% of the oracle gap. This directly validates the idea that paradigm selection should be a per-task decision made by a learned router, not a fixed architectural choice.

**"Reward Model Routing in Alignment"** ([arXiv:2510.02850](https://arxiv.org/abs/2510.02850)) introduces BayesianRouter for per-query reward model selection, showing it consistently outperforms individual reward models, RM ensembling, and existing routing methods. This is the closest precedent to your step-level verification paradigm routing.

**"Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey"** (Moslem & Kelleher, 2026, [arXiv:2603.04445](https://arxiv.org/abs/2603.04445)) provides a systematic framework characterizing routing systems along three dimensions: **when** decisions are made, **what** information is used, and **how** they are computed. This survey explicitly covers routing across independently trained models (as opposed to within-model MoE), which maps directly to your discriminative/generative PRM routing.

### 5. Discriminative vs. Generative PRMs: The Verification Substrate

**ThinkPRM** ([arXiv:2504.16828](https://arxiv.org/abs/2504.16828), ICLR 2026) and **GenPRM** ([arXiv:2504.00891](https://arxiv.org/pdf/2504.00891)) establish that discriminative and generative PRMs have fundamentally different strengths: discriminative PRMs are fast but fragile under domain shift and require massive annotation; generative PRMs are data-efficient (1% of labels), more robust out-of-domain, and inherently interpretable, but computationally expensive. This complementarity is precisely what makes routing between them non-trivial and scientifically interesting -- it is not a simple quality/speed tradeoff but involves domain sensitivity, interpretability, and calibration.

### 6. The "Geometric Routing" Finding as Theoretical Support for Explicit Routing

**"Geometric Routing Enables Causal Expert Control in Mixture of Experts"** (April 2026, [arXiv:2604.14434](https://arxiv.org/abs/2604.14434)) demonstrates that when routing is made geometrically transparent (cosine routing in low-dimensional space), expert specialization becomes "a first-class interpretability primitive: architecturally monosemantic, causally validated, and controllable at inference with zero overhead." Crucially, the paper finds that "routing topology does not determine asymptotic language modeling quality" -- but it **does** determine interpretability and controllability. This supports your argument that decoupled, explicit routing offers transparency and composability benefits that entangled routing cannot.

---

## Recommended Intellectual Framing

Based on this research, here is how to elevate your contribution beyond "careful engineering":

**Core Thesis**: Verification paradigm routing is not an engineering optimization problem but a **separation of concerns** problem. The contribution is formalizing the principle that *verification paradigm selection should be decoupled from verification execution*, creating a system where:

1. **Independent Improvability** (the "Fixes That Fail" argument): In entangled systems, improving one component can degrade the whole. Decoupled interfaces are the formal prerequisite for each component (discriminative PRM, generative PRM, uncertainty estimator, router) to be independently improved without cross-component interference.

2. **Avoiding Optimization Interference** (the Grouter/StableMoE argument): When routing and computation are jointly trained, they create mutual gradient interference, routing fluctuation, and representation collapse. Decoupled routing eliminates this, as demonstrated by 4.28x data efficiency gains in Grouter.

3. **Composable Verification as a Design Principle** (the Modular Deep Learning argument): Just as Pfeiffer et al. showed that "separating computation from routing" enables positive transfer and systematic generalization, your system separates verification selection from verification execution, enabling each verification paradigm to evolve on its own trajectory.

4. **Paradigm Complementarity is Fundamental, Not Incidental** (the Select-then-Solve argument): No single verification paradigm dominates across all step types -- oracle routing beats any fixed paradigm by a wide margin. This is not a deficiency to be engineered around but a structural property of the verification landscape that demands explicit routing.

5. **Geometric Transparency** (the Geometric Routing argument): Explicit, decoupled routing provides interpretability and controllability that implicit routing cannot, making the system auditable and trustworthy -- properties essential for verification systems.

The key framing shift: your contribution is not "we combined four techniques" but rather "we demonstrate that verification paradigm selection and verification execution are fundamentally different concerns that must be decoupled, and we provide the first architecture that treats this decoupling as a first-class design principle, enabling independent improvement of each component."

---

Sources:
- [Modular Machine Learning: An Indispensable Path towards New-Generation LLMs](https://arxiv.org/abs/2504.20020)
- [Modular Deep Learning (Pfeiffer et al., 2023)](https://arxiv.org/abs/2302.11529)
- [Grouter: Decoupling Routing from Representation (ICML 2026)](https://arxiv.org/abs/2603.06626)
- [StableMoE: Stable Routing Strategy for Mixture of Experts (ACL 2022)](https://arxiv.org/abs/2204.08396)
- [Select-then-Solve: Paradigm Routing as Inference-Time Optimization](https://arxiv.org/abs/2604.06753)
- [Fixes That Fail: Self-Defeating Improvements in ML Systems (NeurIPS 2021)](https://arxiv.org/abs/2103.11766)
- [Routers Learn the Geometry of Their Experts](https://arxiv.org/abs/2605.12476)
- [The Myth of Expert Specialization in MoEs](https://arxiv.org/html/2604.09780v1)
- [Geometric Routing Enables Causal Expert Control in MoE](https://arxiv.org/abs/2604.14434)
- [On the Representation Collapse of Sparse MoE](https://arxiv.org/abs/2204.09179)
- [Reward Model Routing in Alignment](https://arxiv.org/abs/2510.02850)
- [Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey](https://arxiv.org/abs/2603.04445)
- [ThinkPRM: Process Reward Models That Think (ICLR 2026)](https://arxiv.org/abs/2504.16828)
- [GenPRM: Scaling Test-Time Compute via Generative Reasoning](https://arxiv.org/pdf/2504.00891)
- [Separation of Concerns in Reinforcement Learning](https://arxiv.org/abs/1612.05159)
- [A Survey of Process Reward Models](https://arxiv.org/abs/2510.08049)
- [Joint Training of Deep Ensembles Fails Due to Learner Collusion](https://arxiv.org/pdf/2301.11323)

agentId: ac473fdeecb5aea6e (use SendMessage with to: 'ac473fdeecb5aea6e' to continue this agent)
&lt;usage>total_tokens: 32099
tool_uses: 25
duration_ms: 221701&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dedaca19-d383-4bd2-b295-40f4f09c0f7d",
  "isSidechain": false,
  "promptId": "a14d4547-e473-4da0-836a-c0e4d22dabcc",
  "type": "user",
  "uuid": "1b9bffc9-819c-4dd1-98de-6af1af37d91f",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm working on a research proposal about step-level verification paradigm routing for process reward models (PRMs). A reviewer has flagged that the core contribution is \"synthesis-level\" — combining existing techniques (dual-mode architecture, uncertainty estimation, constrained RL, min-form credit assignment) without a fundamentally new insight.\n\nThe reviewer suggested framing \"composability as a first-class design principle\" — that verification paradigm selection should be decoupled from verification execution, and this modularity means advances in discriminative PRMs, generative PRMs, or uncertainty estimation each independently improve the system.\n\nHelp me research:\n1. Search for \"composable machine learning systems modular design\" and \"decoupled routing verification\" to find precedents where modularity/composability was itself the scientific contribution\n2. Search for \"implicit vs explicit routing machine learning\" or \"entangled vs disentangled routing\" to find formal frameworks for understanding why decoupled routing is better\n3. Search for \"mixture of experts routing analysis\" or \"adaptive computation routing theory\" — MoE literature has extensive analysis of when explicit routing outperforms implicit routing\n4. Search for recent papers (2025-2026) that make \"architectural composability\" or \"modular verification\" their primary contribution in NLP/reasoning\n\nI need concrete intellectual framing to elevate the contribution beyond \"careful engineering.\" What theoretical or empirical arguments exist for why decoupled/explicit routing is fundamentally better than entangled/implicit routing?",
    "agentId": "ac473fdeecb5aea6e",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive material to synthesize. Here is the research synthesis:\n\n---\n\n## Research Synthesis: Theoretical and Empirical Foundations for Decoupled Verification Paradigm Routing\n\n### 1. Composability/Modularity as a First-Class Scientific Contribution\n\nSeveral recent papers establish that **modularity itself is the contribution**, not merely an engineering convenience:\n\n**\"Modular Machine Learning: An Indispensable Path towards New-Generation Large Language Models\"** (Wang et al., April 2025, [arXiv:2504.20020](https://arxiv.org/abs/2504.20020)) explicitly argues that the MML paradigm is indispensable for next-generation LLMs, decomposing complex structures into three interdependent components: modular representation, modular model, and modular reasoning. The paper frames modularity as enabling counterfactual reasoning, mitigating hallucinations, and promoting fairness/safety/transparency -- i.e., capabilities that monolithic architectures fundamentally cannot provide.\n\n**\"Modular Deep Learning\"** (Pfeiffer, Ruder, Vulic, Ponti, 2023, [arXiv:2302.11529](https://arxiv.org/abs/2302.11529)) is the canonical survey that establishes the theoretical framework. It decomposes modular architectures into four dimensions: **routing function**, **computation function**, **aggregation function**, and **training setting**. Crucially, it argues that \"these properties enable positive transfer and systematic generalization by **separating computation from routing** and updating modules locally.\" This separation is presented as the theoretical reason modularity works, not just an implementation detail.\n\n**\"Separation of Concerns in Reinforcement Learning\"** ([arXiv:1612.05159](https://arxiv.org/abs/1612.05159)) provides a formal framework for decomposing a single-agent task into multiple agents, each focusing on different aspects. This is directly analogous to your proposal of separating verification paradigm selection from verification execution.\n\n### 2. Why Decoupled/Explicit Routing is Fundamentally Better Than Entangled/Implicit Routing\n\nThis is where the MoE literature provides your strongest theoretical ammunition:\n\n**Grouter: Decoupling Routing from Representation** (ICML 2026, [arXiv:2603.06626](https://arxiv.org/abs/2603.06626)) is perhaps your single most important citation. It demonstrates that traditional MoE training \"requires the model to simultaneously train expert weights while searching for an optimal routing policy within a vast combinatorial space.\" By **decoupling routing topology from representation**, Grouter eliminates optimization interference, boosts pre-training data utilization by 4.28x, and achieves 33.5% throughput acceleration. The key insight: when routing and computation are entangled, each interferes with the other's optimization landscape.\n\n**StableMoE** (ACL 2022, [arXiv:2204.08396](https://arxiv.org/abs/2204.08396)) provides the theoretical diagnosis of **routing fluctuation**: when routing is entangled with representation learning, the target expert of the same input may change during training, but only one expert is activated during inference. This harms sample efficiency because the same input updates different experts but only one is finally used. StableMoE's solution -- distilling a lightweight router decoupled from the backbone, then freezing it -- directly validates the principle that decoupling routing from execution improves both convergence speed and performance.\n\n**\"Routers Learn the Geometry of Their Experts\"** (Ahrac et al., May 2026, [arXiv:2605.12476](https://arxiv.org/abs/2605.12476)) reveals a **geometric coupling** between routers and experts: router weights and expert weights receive gradients along the same input direction, differing only in scalar coefficients. This coupling means entangled training creates mutual interference -- the router cannot freely optimize routing without distorting expert representations, and vice versa.\n\n**\"The Myth of Expert Specialization in MoEs\"** (April 2026, [arXiv:2604.09780](https://arxiv.org/html/2604.09780v1)) further undermines entangled routing by showing that what appears to be domain-specific expert specialization is actually a consequence of the geometry of hidden states, not genuine domain expertise. This means entangled routing decisions are driven by representational artifacts rather than task-relevant properties -- a strong argument for explicit, purpose-built routing.\n\n**Representation Collapse** ([arXiv:2204.09179](https://arxiv.org/abs/2204.09179), [arXiv:2406.15883](https://arxiv.org/pdf/2406.15883)) documents that entangled routing in sparse MoE leads to representation collapse, where experts converge to similar outputs. The router encouraging \"token clustering around expert centroids\" actively harms specialization. Decoupled routing avoids this pathology.\n\n### 3. The \"Fixes That Fail\" Argument: Why Independent Improvability Requires Decoupling\n\n**\"Fixes That Fail: Self-Defeating Improvements in Machine-Learning Systems\"** (NeurIPS 2021, [arXiv:2103.11766](https://arxiv.org/abs/2103.11766)) provides a formal error decomposition showing that in composed ML systems, **improving one model can deteriorate downstream model performance, even after retraining**. This is caused by entanglement between models. This directly supports your \"composability as first-class design principle\" framing: unless routing is decoupled from verification execution, improving the discriminative PRM, the generative PRM, or the uncertainty estimator can make the overall system worse. Decoupled interfaces are the formal requirement for independent improvability.\n\n**\"Joint Training of Deep Ensembles Fails Due to Learner Collusion\"** ([arXiv:2301.11323](https://arxiv.org/pdf/2301.11323)) shows that joint optimization of ensemble loss results in degenerate behavior, with base learners colluding to artificially inflate apparent diversity. This is a strong analogy to why jointly optimizing a router and verifiers in an entangled fashion leads to suboptimal verification.\n\nThe decoupled optimization literature also supports this: entangled optimization of strategy selection and response generation introduces **gradient conflicts and preference bias**, whereas decoupling avoids these issues and yields significant performance improvements.\n\n### 4. Paradigm Routing as a Recognized Research Direction\n\n**\"Select-then-Solve: Paradigm Routing as Inference-Time Optimization for LLM Agents\"** (April 2026, [arXiv:2604.06753](https://arxiv.org/abs/2604.06753)) is extremely close to your proposal. It shows that across six inference-time paradigms (Direct, CoT, ReAct, Plan-Execute, Reflection, ReCode), **no single paradigm dominates** -- oracle per-task selection beats the best fixed paradigm by 17.1pp. A lightweight embedding-based router recovers up to 37% of the oracle gap. This directly validates the idea that paradigm selection should be a per-task decision made by a learned router, not a fixed architectural choice.\n\n**\"Reward Model Routing in Alignment\"** ([arXiv:2510.02850](https://arxiv.org/abs/2510.02850)) introduces BayesianRouter for per-query reward model selection, showing it consistently outperforms individual reward models, RM ensembling, and existing routing methods. This is the closest precedent to your step-level verification paradigm routing.\n\n**\"Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey\"** (Moslem & Kelleher, 2026, [arXiv:2603.04445](https://arxiv.org/abs/2603.04445)) provides a systematic framework characterizing routing systems along three dimensions: **when** decisions are made, **what** information is used, and **how** they are computed. This survey explicitly covers routing across independently trained models (as opposed to within-model MoE), which maps directly to your discriminative/generative PRM routing.\n\n### 5. Discriminative vs. Generative PRMs: The Verification Substrate\n\n**ThinkPRM** ([arXiv:2504.16828](https://arxiv.org/abs/2504.16828), ICLR 2026) and **GenPRM** ([arXiv:2504.00891](https://arxiv.org/pdf/2504.00891)) establish that discriminative and generative PRMs have fundamentally different strengths: discriminative PRMs are fast but fragile under domain shift and require massive annotation; generative PRMs are data-efficient (1% of labels), more robust out-of-domain, and inherently interpretable, but computationally expensive. This complementarity is precisely what makes routing between them non-trivial and scientifically interesting -- it is not a simple quality/speed tradeoff but involves domain sensitivity, interpretability, and calibration.\n\n### 6. The \"Geometric Routing\" Finding as Theoretical Support for Explicit Routing\n\n**\"Geometric Routing Enables Causal Expert Control in Mixture of Experts\"** (April 2026, [arXiv:2604.14434](https://arxiv.org/abs/2604.14434)) demonstrates that when routing is made geometrically transparent (cosine routing in low-dimensional space), expert specialization becomes \"a first-class interpretability primitive: architecturally monosemantic, causally validated, and controllable at inference with zero overhead.\" Crucially, the paper finds that \"routing topology does not determine asymptotic language modeling quality\" -- but it **does** determine interpretability and controllability. This supports your argument that decoupled, explicit routing offers transparency and composability benefits that entangled routing cannot.\n\n---\n\n## Recommended Intellectual Framing\n\nBased on this research, here is how to elevate your contribution beyond \"careful engineering\":\n\n**Core Thesis**: Verification paradigm routing is not an engineering optimization problem but a **separation of concerns** problem. The contribution is formalizing the principle that *verification paradigm selection should be decoupled from verification execution*, creating a system where:\n\n1. **Independent Improvability** (the \"Fixes That Fail\" argument): In entangled systems, improving one component can degrade the whole. Decoupled interfaces are the formal prerequisite for each component (discriminative PRM, generative PRM, uncertainty estimator, router) to be independently improved without cross-component interference.\n\n2. **Avoiding Optimization Interference** (the Grouter/StableMoE argument): When routing and computation are jointly trained, they create mutual gradient interference, routing fluctuation, and representation collapse. Decoupled routing eliminates this, as demonstrated by 4.28x data efficiency gains in Grouter.\n\n3. **Composable Verification as a Design Principle** (the Modular Deep Learning argument): Just as Pfeiffer et al. showed that \"separating computation from routing\" enables positive transfer and systematic generalization, your system separates verification selection from verification execution, enabling each verification paradigm to evolve on its own trajectory.\n\n4. **Paradigm Complementarity is Fundamental, Not Incidental** (the Select-then-Solve argument): No single verification paradigm dominates across all step types -- oracle routing beats any fixed paradigm by a wide margin. This is not a deficiency to be engineered around but a structural property of the verification landscape that demands explicit routing.\n\n5. **Geometric Transparency** (the Geometric Routing argument): Explicit, decoupled routing provides interpretability and controllability that implicit routing cannot, making the system auditable and trustworthy -- properties essential for verification systems.\n\nThe key framing shift: your contribution is not \"we combined four techniques\" but rather \"we demonstrate that verification paradigm selection and verification execution are fundamentally different concerns that must be decoupled, and we provide the first architecture that treats this decoupling as a first-class design principle, enabling independent improvement of each component.\"\n\n---\n\nSources:\n- [Modular Machine Learning: An Indispensable Path towards New-Generation LLMs](https://arxiv.org/abs/2504.20020)\n- [Modular Deep Learning (Pfeiffer et al., 2023)](https://arxiv.org/abs/2302.11529)\n- [Grouter: Decoupling Routing from Representation (ICML 2026)](https://arxiv.org/abs/2603.06626)\n- [StableMoE: Stable Routing Strategy for Mixture of Experts (ACL 2022)](https://arxiv.org/abs/2204.08396)\n- [Select-then-Solve: Paradigm Routing as Inference-Time Optimization](https://arxiv.org/abs/2604.06753)\n- [Fixes That Fail: Self-Defeating Improvements in ML Systems (NeurIPS 2021)](https://arxiv.org/abs/2103.11766)\n- [Routers Learn the Geometry of Their Experts](https://arxiv.org/abs/2605.12476)\n- [The Myth of Expert Specialization in MoEs](https://arxiv.org/html/2604.09780v1)\n- [Geometric Routing Enables Causal Expert Control in MoE](https://arxiv.org/abs/2604.14434)\n- [On the Representation Collapse of Sparse MoE](https://arxiv.org/abs/2204.09179)\n- [Reward Model Routing in Alignment](https://arxiv.org/abs/2510.02850)\n- [Dynamic Model Routing and Cascading for Efficient LLM Inference: A Survey](https://arxiv.org/abs/2603.04445)\n- [ThinkPRM: Process Reward Models That Think (ICLR 2026)](https://arxiv.org/abs/2504.16828)\n- [GenPRM: Scaling Test-Time Compute via Generative Reasoning](https://arxiv.org/pdf/2504.00891)\n- [Separation of Concerns in Reinforcement Learning](https://arxiv.org/abs/1612.05159)\n- [A Survey of Process Reward Models](https://arxiv.org/abs/2510.08049)\n- [Joint Training of Deep Ensembles Fails Due to Learner Collusion](https://arxiv.org/pdf/2301.11323)"
      }
    ],
    "totalDurationMs": 221701,
    "totalTokens": 32099,
    "totalToolUseCount": 25,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1454,
      "cache_read_input_tokens": 27241,
      "output_tokens": 3403,
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
          "output_tokens": 3403,
          "cache_read_input_tokens": 27241,
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
      "otherToolCount": 25
    }
  },
  "sourceToolAssistantUUID": "dedaca19-d383-4bd2-b295-40f4f09c0f7d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 23_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"CRISP-PRM: Criticality-Aware Step-Level Paradigm Selection for Unified…",
  "leafUuid": "1b9bffc9-819c-4dd1-98de-6af1af37d91f",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising CRISP-PRM after round 5 reviewer feedback",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff"
}
```

---

### Tool result

_source line 25 · 2026-05-28T01:48:30.384Z_

<details><summary>↩ Tool result · `toolu_01W3yhyzTAKePskAfK8eTcu3`</summary>

```text
Now I have comprehensive data. Let me compile the final report.

Here is my complete findings report:

---

## 1. ActPRM (arXiv: 2504.10559)

**Full title:** "Efficient Process Reward Model Training via Active Learning"

**Note on arXiv ID:** The reviewer cited arXiv 2601.22249, but no paper with that ID exists. The actual ActPRM paper is **arXiv:2504.10559**.

**Base model:** Qwen2.5-Math-7B-Instruct

**Core technique:** Active learning -- the model estimates uncertainty during forward passes, then selectively annotates only the most uncertain samples using a reasoning model. This reduces annotation cost to ~20% of standard approaches.

**ProcessBench F1 scores (from Table 1 of the paper):**

| Subset | ActPRM | ActPRM-X |
|---|---|---|
| GSM8K | 0.816 | 0.827 |
| MATH | 0.798 | 0.820 |
| OlympiadBench | 0.714 | 0.720 |
| OmniMATH | 0.670 | 0.673 |
| **Average** | **0.750** | **0.760** |

The reviewer's claim of F1 75.0 is confirmed for ActPRM. ActPRM-X (extended variant) reaches 76.0. As of available results, **ActPRM-X at 76.0 is the discriminative PRM SOTA on ProcessBench among 7B-class models**.

For context, here are baselines from the same table:
- Qwen2.5-Math-PRM-7B: 0.735 avg F1
- Universal-PRM: 0.743 avg F1
- Qwen2.5-Math-PRM-72B: 0.783 avg F1
- Qwen2.5-Math-7B-PRM800K: 0.565 avg F1
- Math-Shepherd-PRM-7B: 0.315 avg F1

---

## 2. ASPRM / AdaptiveStep (arXiv: 2502.13943)

**Full title:** "AdaptiveStep: Automatically Dividing Reasoning Step through Model Confidence"

**arXiv ID:** 2502.13943

**What ASPRM stands for:** AdaptiveStep Process Reward Model

**Core technique:** Divides reasoning steps based on model confidence (token prediction probability) rather than rule-based delimiters (e.g., newlines). This identifies genuine decision points where the model is uncertain, creating more informative step boundaries for PRM training.

**ProcessBench F1 scores: NONE.** The paper does **not** evaluate on ProcessBench at all. It evaluates on:
- Mathematical reasoning: GSM8k, MATH500, GSM-Symbolic (Best-of-N accuracy)
- Code generation: LeetCodeDataset, LiveCodeBench-V4 (pass rates)
- Token-level Value-guided Decoding (TVD)

If a reviewer is citing ASPRM's ProcessBench F1, that claim cannot be verified from the paper itself.

---

## 3. Hard2Verify (arXiv: 2510.13744)

**Full title:** "Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math"

**arXiv ID:** 2510.13744

**Core finding -- ProcessBench scores do NOT generalize to frontier problems:**

The headline result is a catastrophic performance drop for the ProcessBench SOTA model:

- **Qwen2.5-Math-PRM-72B on ProcessBench ErrorID:** 78.3% F1
- **Qwen2.5-Math-PRM-72B on Hard2Verify ErrorID:** 37.3% F1 (balanced F1: 37.28)
- **Gap: ~41 percentage points**

Additional Hard2Verify scores for Qwen2.5-Math-PRM-72B:
- Step-Level balanced accuracy: 55.82, balanced F1: 35.50
- Response-Level balanced accuracy: 66.80, balanced F1: 64.91
- ErrorID balanced accuracy: 41.80, balanced F1: 37.28

The paper's broader finding: **"Models capable of scoring 60%+ on ProcessBench are unable to crack 20% on Hard2Verify's ErrorID task."** This is because ProcessBench problems (GSM8K, MATH, OlympiadBench, OmniMATH) are substantially easier than the 2024-2025 Olympiad-level problems in Hard2Verify. Weaker verifiers essentially mark every step as correct, failing to detect errors in frontier-difficulty reasoning. The benchmark evaluates 29 generative critics and PRMs, finding open-source verifiers significantly lag closed-source models.

---

## 4. Broader ProcessBench Landscape (as of mid-2026)

### Discriminative PRMs (ranked by ProcessBench avg F1):
1. **ActPRM-X** -- 0.760 avg F1 (7B, current SOTA among discriminative 7B PRMs)
2. **ActPRM** -- 0.750 avg F1 (7B)
3. **Universal-PRM** -- 0.743 avg F1 (7B)
4. **Qwen2.5-Math-PRM-7B** -- 0.735 avg F1 (7B)
5. **Qwen2.5-Math-PRM-72B** -- 0.783 avg F1 (72B, largest discriminative model)
6. **R-PRM-7B-DPO** -- 0.704 avg F1 (7B; per-subset: GSM8K 80.7, MATH 76.9, OlympiadBench 63.8, OmniMATH 60.1)
7. **PathFinder-PRM** -- ~0.695 avg F1 (7B, error-aware hierarchical supervision)
8. **PURE-PRM-7B** -- 0.575 avg F1
9. **Qwen2.5-Math-7B-PRM800K** -- 0.565 avg F1

### Generative PRMs (not discriminative, but worth noting for completeness):
- **GenPRM-7B** (arXiv: 2504.00891): generative PRM using CoT reasoning + code verification. ProcessBench avg F1: 75.2 (Pass@1), **80.5 (Maj@8)**. Per-subset at Maj@8: GSM8K 81.0, MATH 85.7, OlympiadBench 78.4, OmniMATH 76.8. Surpasses Qwen2.5-Math-PRM-72B. However, this is generative, not discriminative.
- **ThinkPRM-14B** (arXiv: 2504.16828): generative long-CoT verifier. ProcessBench F1 on OlympiadBench: 87.3, OmniMATH: 85.7 (only two subsets reported). Trained on 1% of PRM800K labels.
- **LLM-as-Judge baselines:** o1-Mini achieves 0.879, QwQ-32B achieves 0.816 avg F1 on ProcessBench.

### No discriminative PRM has surpassed ActPRM-X (76.0) at the 7B scale as of available literature. The 72B Qwen2.5-Math-PRM at 78.3 remains the largest discriminative model result, but generative approaches (GenPRM, ThinkPRM) now significantly exceed both.

---

**Key takeaway for the reviewer's claims:** The F1 75.0 for ActPRM is confirmed, but the arXiv ID cited (2601.22249) appears incorrect -- the real ID is 2504.10559. ASPRM (2502.13943) does not report ProcessBench F1 scores at all, so any claimed ProcessBench number for ASPRM cannot be sourced to that paper. And per Hard2Verify, ProcessBench scores have a well-documented generalization problem: the SOTA 78.3 F1 on ProcessBench drops to 37.3 on frontier-difficulty problems.

Sources:
- [ActPRM - Efficient Process Reward Model Training via Active Learning](https://arxiv.org/abs/2504.10559)
- [ASPRM/AdaptiveStep - Automatically Dividing Reasoning Step through Model Confidence](https://arxiv.org/abs/2502.13943)
- [Hard2Verify - A Step-Level Verification Benchmark for Open-Ended Frontier Math](https://arxiv.org/abs/2510.13744)
- [ThinkPRM - Process Reward Models That Think](https://arxiv.org/abs/2504.16828)
- [GenPRM - Scaling Test-Time Compute of Process Reward Models](https://arxiv.org/abs/2504.00891)
- [R-PRM - Reasoning-Driven Process Reward Modeling](https://arxiv.org/abs/2503.21295)
- [PathFinder-PRM - Error Typing for Smarter Rewards](https://arxiv.org/abs/2505.19706)
- [AURORA - Universal Process Reward Models](https://arxiv.org/abs/2502.11520)
- [ProcessBench paper](https://arxiv.org/abs/2412.06559)
- [Is PRM Necessary?](https://arxiv.org/abs/2505.11227)

agentId: a7e194180ff44ef80 (use SendMessage with to: 'a7e194180ff44ef80' to continue this agent)
&lt;usage>total_tokens: 37774
tool_uses: 48
duration_ms: 295184&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0abb2d85-f4e9-4806-81e6-a2cedadd6eff",
  "isSidechain": false,
  "promptId": "a14d4547-e473-4da0-836a-c0e4d22dabcc",
  "type": "user",
  "uuid": "36605380-63d6-4b35-8f23-845640a2ad35",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to find updated discriminative PRM state-of-the-art on ProcessBench. Specifically:\n\n1. Search for \"ACTPRM arXiv 2601.22249\" and fetch the paper to find its actual ProcessBench F1 scores. The reviewer claims F1 75.0.\n2. Search for \"ASPRM arXiv 2502.13943\" and fetch the paper to find its ProcessBench F1 scores.\n3. Search for \"Hard2Verify ProcessBench generalization\" — there's apparently a finding that ProcessBench scores may not generalize to frontier problems. Find this paper/result.\n4. Search Papers With Code or recent surveys for \"ProcessBench leaderboard 2026\" to see if there are even newer discriminative PRMs beyond ACTPRM and ASPRM.\n\nFor each paper found, report: full title, arXiv ID, key F1 numbers on ProcessBench (per-subset if available: GSM8K/MATH/OlympiadBench/OmniMATH), and the core technique used. Be precise about numbers — I need exact figures.",
    "agentId": "a7e194180ff44ef80",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive data. Let me compile the final report.\n\nHere is my complete findings report:\n\n---\n\n## 1. ActPRM (arXiv: 2504.10559)\n\n**Full title:** \"Efficient Process Reward Model Training via Active Learning\"\n\n**Note on arXiv ID:** The reviewer cited arXiv 2601.22249, but no paper with that ID exists. The actual ActPRM paper is **arXiv:2504.10559**.\n\n**Base model:** Qwen2.5-Math-7B-Instruct\n\n**Core technique:** Active learning -- the model estimates uncertainty during forward passes, then selectively annotates only the most uncertain samples using a reasoning model. This reduces annotation cost to ~20% of standard approaches.\n\n**ProcessBench F1 scores (from Table 1 of the paper):**\n\n| Subset | ActPRM | ActPRM-X |\n|---|---|---|\n| GSM8K | 0.816 | 0.827 |\n| MATH | 0.798 | 0.820 |\n| OlympiadBench | 0.714 | 0.720 |\n| OmniMATH | 0.670 | 0.673 |\n| **Average** | **0.750** | **0.760** |\n\nThe reviewer's claim of F1 75.0 is confirmed for ActPRM. ActPRM-X (extended variant) reaches 76.0. As of available results, **ActPRM-X at 76.0 is the discriminative PRM SOTA on ProcessBench among 7B-class models**.\n\nFor context, here are baselines from the same table:\n- Qwen2.5-Math-PRM-7B: 0.735 avg F1\n- Universal-PRM: 0.743 avg F1\n- Qwen2.5-Math-PRM-72B: 0.783 avg F1\n- Qwen2.5-Math-7B-PRM800K: 0.565 avg F1\n- Math-Shepherd-PRM-7B: 0.315 avg F1\n\n---\n\n## 2. ASPRM / AdaptiveStep (arXiv: 2502.13943)\n\n**Full title:** \"AdaptiveStep: Automatically Dividing Reasoning Step through Model Confidence\"\n\n**arXiv ID:** 2502.13943\n\n**What ASPRM stands for:** AdaptiveStep Process Reward Model\n\n**Core technique:** Divides reasoning steps based on model confidence (token prediction probability) rather than rule-based delimiters (e.g., newlines). This identifies genuine decision points where the model is uncertain, creating more informative step boundaries for PRM training.\n\n**ProcessBench F1 scores: NONE.** The paper does **not** evaluate on ProcessBench at all. It evaluates on:\n- Mathematical reasoning: GSM8k, MATH500, GSM-Symbolic (Best-of-N accuracy)\n- Code generation: LeetCodeDataset, LiveCodeBench-V4 (pass rates)\n- Token-level Value-guided Decoding (TVD)\n\nIf a reviewer is citing ASPRM's ProcessBench F1, that claim cannot be verified from the paper itself.\n\n---\n\n## 3. Hard2Verify (arXiv: 2510.13744)\n\n**Full title:** \"Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math\"\n\n**arXiv ID:** 2510.13744\n\n**Core finding -- ProcessBench scores do NOT generalize to frontier problems:**\n\nThe headline result is a catastrophic performance drop for the ProcessBench SOTA model:\n\n- **Qwen2.5-Math-PRM-72B on ProcessBench ErrorID:** 78.3% F1\n- **Qwen2.5-Math-PRM-72B on Hard2Verify ErrorID:** 37.3% F1 (balanced F1: 37.28)\n- **Gap: ~41 percentage points**\n\nAdditional Hard2Verify scores for Qwen2.5-Math-PRM-72B:\n- Step-Level balanced accuracy: 55.82, balanced F1: 35.50\n- Response-Level balanced accuracy: 66.80, balanced F1: 64.91\n- ErrorID balanced accuracy: 41.80, balanced F1: 37.28\n\nThe paper's broader finding: **\"Models capable of scoring 60%+ on ProcessBench are unable to crack 20% on Hard2Verify's ErrorID task.\"** This is because ProcessBench problems (GSM8K, MATH, OlympiadBench, OmniMATH) are substantially easier than the 2024-2025 Olympiad-level problems in Hard2Verify. Weaker verifiers essentially mark every step as correct, failing to detect errors in frontier-difficulty reasoning. The benchmark evaluates 29 generative critics and PRMs, finding open-source verifiers significantly lag closed-source models.\n\n---\n\n## 4. Broader ProcessBench Landscape (as of mid-2026)\n\n### Discriminative PRMs (ranked by ProcessBench avg F1):\n1. **ActPRM-X** -- 0.760 avg F1 (7B, current SOTA among discriminative 7B PRMs)\n2. **ActPRM** -- 0.750 avg F1 (7B)\n3. **Universal-PRM** -- 0.743 avg F1 (7B)\n4. **Qwen2.5-Math-PRM-7B** -- 0.735 avg F1 (7B)\n5. **Qwen2.5-Math-PRM-72B** -- 0.783 avg F1 (72B, largest discriminative model)\n6. **R-PRM-7B-DPO** -- 0.704 avg F1 (7B; per-subset: GSM8K 80.7, MATH 76.9, OlympiadBench 63.8, OmniMATH 60.1)\n7. **PathFinder-PRM** -- ~0.695 avg F1 (7B, error-aware hierarchical supervision)\n8. **PURE-PRM-7B** -- 0.575 avg F1\n9. **Qwen2.5-Math-7B-PRM800K** -- 0.565 avg F1\n\n### Generative PRMs (not discriminative, but worth noting for completeness):\n- **GenPRM-7B** (arXiv: 2504.00891): generative PRM using CoT reasoning + code verification. ProcessBench avg F1: 75.2 (Pass@1), **80.5 (Maj@8)**. Per-subset at Maj@8: GSM8K 81.0, MATH 85.7, OlympiadBench 78.4, OmniMATH 76.8. Surpasses Qwen2.5-Math-PRM-72B. However, this is generative, not discriminative.\n- **ThinkPRM-14B** (arXiv: 2504.16828): generative long-CoT verifier. ProcessBench F1 on OlympiadBench: 87.3, OmniMATH: 85.7 (only two subsets reported). Trained on 1% of PRM800K labels.\n- **LLM-as-Judge baselines:** o1-Mini achieves 0.879, QwQ-32B achieves 0.816 avg F1 on ProcessBench.\n\n### No discriminative PRM has surpassed ActPRM-X (76.0) at the 7B scale as of available literature. The 72B Qwen2.5-Math-PRM at 78.3 remains the largest discriminative model result, but generative approaches (GenPRM, ThinkPRM) now significantly exceed both.\n\n---\n\n**Key takeaway for the reviewer's claims:** The F1 75.0 for ActPRM is confirmed, but the arXiv ID cited (2601.22249) appears incorrect -- the real ID is 2504.10559. ASPRM (2502.13943) does not report ProcessBench F1 scores at all, so any claimed ProcessBench number for ASPRM cannot be sourced to that paper. And per Hard2Verify, ProcessBench scores have a well-documented generalization problem: the SOTA 78.3 F1 on ProcessBench drops to 37.3 on frontier-difficulty problems.\n\nSources:\n- [ActPRM - Efficient Process Reward Model Training via Active Learning](https://arxiv.org/abs/2504.10559)\n- [ASPRM/AdaptiveStep - Automatically Dividing Reasoning Step through Model Confidence](https://arxiv.org/abs/2502.13943)\n- [Hard2Verify - A Step-Level Verification Benchmark for Open-Ended Frontier Math](https://arxiv.org/abs/2510.13744)\n- [ThinkPRM - Process Reward Models That Think](https://arxiv.org/abs/2504.16828)\n- [GenPRM - Scaling Test-Time Compute of Process Reward Models](https://arxiv.org/abs/2504.00891)\n- [R-PRM - Reasoning-Driven Process Reward Modeling](https://arxiv.org/abs/2503.21295)\n- [PathFinder-PRM - Error Typing for Smarter Rewards](https://arxiv.org/abs/2505.19706)\n- [AURORA - Universal Process Reward Models](https://arxiv.org/abs/2502.11520)\n- [ProcessBench paper](https://arxiv.org/abs/2412.06559)\n- [Is PRM Necessary?](https://arxiv.org/abs/2505.11227)"
      }
    ],
    "totalDurationMs": 295184,
    "totalTokens": 37774,
    "totalToolUseCount": 48,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 795,
      "cache_read_input_tokens": 34604,
      "output_tokens": 2374,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 795
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2374,
          "cache_read_input_tokens": 34604,
          "cache_creation_input_tokens": 795,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 795,
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
      "otherToolCount": 48
    }
  },
  "sourceToolAssistantUUID": "0abb2d85-f4e9-4806-81e6-a2cedadd6eff",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-28T01:49:47.673Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent! Now I have comprehensive research results from all four agents. Let me synthesize the findings:

## Key Findings:

### 1. CRM Mischaracterization
- CRM **actually does** use a multiplicative decomposition S(t) = Π(1-h(k)) — this is the core equation of the paper
- However, CRM **never uses** "survival analysis" or "hazard function" terminology — it frames everything as "conditional probability modeling"
- The math is isomorphic to discrete-time survival analysis, but the paper doesn't use that language
- So the reviewer was partially right: the terminology is imposed by the proposal, not by CRM itself


- I should keep the multiplicative decomposition reference but drop the survival analysis framing, describing CRM accurately as conditional probability chain rules instead

### 2. Updated Discriminative SOTA
- ActPRM (arXiv 2504.10559, not 2601.22249 as the reviewer stated) achieves average F1 of 75.0, with ActPRM-X reaching 76.0
- ASPRM (arXiv 2502.13943) doesn't actually evaluate on ProcessBench—it uses Best-of-N metrics instead
- Hard2Verify (arXiv 2510.13744) shows a dramatic performance drop on ProcessBench for frontier problems, hitting only 78.3%

The gap widens further when looking at Qwen2.5-Math-PRM-72B, which plummets to 37.3%, actually making a stronger argument for adaptive verification approaches.

### 3. Venue Verification
- GenPRM → AAAI 2026: confirmed
- E-GRM → ACL 2026: confirmed
- CAMEL → ICML 2026: confirmed
- ReProbe/UHeads → ACL 2026 Main (not NeurIPS 2025 as I had)
- SCAN → NeurIPS 2025: confirmed
- Dyve → EMNLP 2025: confirmed
- ProcessBench → ACL 2025: confirmed
- R-PRM → EMNLP 2025: confirmed

### 4. Composability as Scientific Contribution
- The MoE literature provides solid theoretical grounding, particularly through Grouter...

Reviewing the theoretical foundations more carefully. The core insight is that verification paradigm selection and verification execution are fundamentally separate concerns that need decoupling—this mirrors how MoE systems fail when routing and representation learning interfere with each other. I need to revise the CRM characterization to use conditional probability chain rules instead of the hazard function framing, while preserving the multiplicative structure.

Also updating the SOTA section with ActPRM's stronger F1 scores and noting that ASPRM doesn't actually evaluate on ProcessBench, which changes the baseline comparison. The venue for ReProbe should be ACL 2026 Main, not NeurIPS 2025. And I'm noticing the reviewer cited an arXiv ID for ActPRM that doesn't match what I'm finding—need to verify which one is correct. I need to reconcile what the reviewer claimed about CRM with what my research actually found — the reviewer said CRM doesn't use multiplicative survival decomposition, but my agent confirmed it does use S(t) = Π(1-h(k)). The real issue is that CRM doesn't frame it in survival analysis terminology, so I should characterize their approach using their own language while acknowledging the mathematical equivalence. Now I'm ready to draft the corrected JSON with all these fixes applied. I need to systematically update the JSON document with corrected terminology for CRM, add missing related work entries like ActPRM and Hard2Verify, fix the F1 threshold to 75.0, and integrate the reviewer's insight about decoupling verification paradigm selection from execution as a formal principle grounded in mixture-of-experts theory. Now I'm integrating PURE's min-form credit assignment with CRM's conditional probability framework to show how verification effort concentrates on the weakest steps. I need to verify the ActPRM citation — my search found it at 2504.10559 rather than the reviewer's 2601.22249, so I'll use the verified ID. This is a minor revision that tightens the novelty framing and corrects the mathematical characterization without changing the core approach.

Writing the revised proposal JSON... I'm noticing the arXiv ID mismatch for Hard2Verify — the paper is 2510.13744, and it shows a significant performance drop for Qwen2.5-Math-PRM-72B from 78.3% on ProcessBench down to 37.3 on frontier math problems, which really underscores how challenging verification becomes at the frontier.

For the novelty angle, I'm introducing the "Decoupling Principle for Verification" — the idea that routing and representation need to be separated, supported by work on MoE architectures, routing stability issues, and the principle that independent improvements require decoupled interfaces.

Now I'm restructuring the JSON to reflect these changes. I'll rephrase the core problem away from the hazard function framing and toward the conditional probability chain rule that CRM actually uses.

For the opportunity section, I'm emphasizing how Hard2Verify's generalization failure strengthens the case for deep verification work, and I'm adding the decoupling principle as a key insight.

In the landscape, I need to update the SOTA to ActPRM's 75.0 F1, fix the CRM terminology, add entries for ActPRM and ASPRM, correct ReProbe's venue to ACL 2026 Main, and include the three papers supporting the decoupling principle.

For the inspired_by section, I'm fixing the CRM description and starting to add the decoupling framework references.

The approach section needs the F1 threshold updated to 75.0, the SEC module reframed around conditional probability chains instead of survival analysis, and a new section articulating the decoupling principle with Hard2Verify as part of the evaluation protocol.

I should also update key_references with all the new papers and fix existing entries, then update the description and reviewer_response sections accordingly.

Now I'm checking whether ThinkPRM's venue should be added—the composability agent verified it was at ICLR 2026, so I could include that detail even though the current proposal doesn't claim a venue yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "36605380-63d6-4b35-8f23-845640a2ad35",
  "isSidechain": false,
  "requestId": "req_011CbU8EfghaKiM2gWhTGgX2",
  "type": "assistant",
  "uuid": "f0d63a54-486f-49d7-8d72-f9733bf3f5a4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Br6bjxx2RaxqV3TGAtUhUr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5450,
      "cache_creation_input_tokens": 5916,
      "cache_read_input_tokens": 26622,
      "output_tokens": 17701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5916,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5450,
          "output_tokens": 17701,
          "cache_read_input_tokens": 26622,
          "cache_creation_input_tokens": 5916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5916
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

_source line 27 · 2026-05-28T01:49:53.773Z_

Now I have comprehensive research from all four agents. Let me synthesize the findings before producing the revision:

**Key findings:**

1. **CRM**: The reviewer was *partially* wrong — CRM **does** use S(t) = Π(1-h(k)) as its core equation, but never calls it "survival analysis" or "hazard functions." CRM frames it as "conditional probability chain rules." Fix: keep the mathematical form, correct the terminology.

2. **ACTPRM**: Confirmed F1 75.0 (ActPRM-X: 76.0), but the correct arXiv ID is **2504.10559**, not 2601.22249. ASPRM does **not** evaluate on ProcessBench at all. Hard2Verify (arXiv 2510.13744) shows catastrophic drop: 78.3% → 37.3% F1 for best discriminative PRM on frontier problems.

3. **Venue verification**: 7/8 claims verified. **ReProbe/UHeads is ACL 2026 Main, NOT NeurIPS 2025** — this must be corrected. All others (GenPRM AAAI 2026, E-GRM ACL 2026, CAMEL ICML 2026, SCAN NeurIPS 2025, Dyve EMNLP 2025, ProcessBench ACL 2025, R-PRM EMNLP 2025) are verified.

4. **Novelty**: Strong theoretical backing from MoE literature for decoupling as a principle — Grouter (ICML 2026), StableMoE (ACL 2022), "Fixes That Fail" (NeurIPS 2021), Select-then-Solve (2604.06753).

Now let me produce the complete revised proposal:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0d63a54-486f-49d7-8d72-f9733bf3f5a4",
  "isSidechain": false,
  "requestId": "req_011CbU8EfghaKiM2gWhTGgX2",
  "type": "assistant",
  "uuid": "3b29381b-eb00-4e5f-b248-f1c44305a86e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Br6bjxx2RaxqV3TGAtUhUr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5450,
      "cache_creation_input_tokens": 5916,
      "cache_read_input_tokens": 26622,
      "output_tokens": 17701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5916,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5450,
          "output_tokens": 17701,
          "cache_read_input_tokens": 26622,
          "cache_creation_input_tokens": 5916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5916
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

_source line 28 · 2026-05-28T01:55:23.441Z_

<details open><summary>🔧 Tool call — Write · `toolu_01ExrVLsVXFjZd5qL9PRkm3c`</summary>

```json
{
  "file_path": "/tmp/crisp_prm_r6.json",
  "content": "{\n  \"change_type\": \"minor\",\n  \"title\": \"CRISP-PRM: Criticality-Aware Step-Level Paradigm Selection for Unified Process Reward Models\",\n  \"core_problem\": \"Process reward models face a fundamental accuracy-cost trade-off at the step level: discriminative (fast scalar) verification is cheap (~10ms/step) but unreliable on hard reasoning steps, while generative (CoT) verification is far more accurate but ~100-500x more expensive (~1-5s/step). Dyve (arXiv 2502.11157, EMNLP 2025) demonstrated the feasibility and value of step-level fast/slow paradigm selection within a single model using implicit SFT-based routing, outperforming all contemporaneous baselines (Qwen2.5-Math-7B-PRM800K avg F1 ~41, Skywork-PRM-7B ~35, GPT-4o ~52) with avg F1 ~55.8. However, stronger discriminative PRMs trained with improved data pipelines—notably ActPRM (avg F1 75.0 on ProcessBench, arXiv 2504.10559) and Qwen2.5-Math-PRM-7B (avg F1 73.5, per R-PRM Table 1)—have since surpassed Dyve's adaptive performance using pure discriminative verification. This reveals that implicit SFT-based routing has a ceiling: when the routing mechanism is entangled with the verification itself (learned output length as a proxy for routing), the system cannot benefit from independently improving either the discriminative or generative verification mode. This entanglement mirrors the routing-representation interference identified in MoE research (Grouter, arXiv 2603.06626, ICML 2026; StableMoE, arXiv 2204.08396, ACL 2022), where joint optimization of routing and computation degrades both. Problem-level routing methods (F/S-RM, E-GRM, CAMEL) achieve efficiency gains but apply uniform verification to every step within a solution, ignoring that steps vary dramatically in difficulty and criticality. ProcessBench data confirms this variation: discriminative PRM error detection accuracy degrades from 72.0% (GSM8K) to 55.2% (OmniMATH) (ProcessBench, arXiv 2412.06559, ACL 2025; also R-PRM, arXiv 2503.21295, EMNLP 2025, Table 1). Moreover, Hard2Verify (arXiv 2510.13744) reveals that even the best discriminative PRM (Qwen2.5-Math-PRM-72B, F1 78.3 on ProcessBench) collapses to F1 37.3 on frontier-difficulty problems—demonstrating that the need for selective deep verification intensifies as problem difficulty increases. Can a unified dual-mode PRM with explicit, composable step-level paradigm selection—grounded in a principled decoupling of verification paradigm selection from verification execution—produce better accuracy-per-FLOP Pareto frontiers than both uniform paradigms, problem-level routing, and Dyve's implicit step-level routing, while enabling independent improvement of each component?\",\n  \"opportunity\": \"Four converging developments, plus a theoretical insight from modular systems research, create a clear opportunity for explicit criticality-based paradigm routing:\\n\\n(1) The maturation of both verification paradigms to strong individual performance. Discriminative PRMs have advanced substantially through improved training pipelines: ActPRM (arXiv 2504.10559) achieves avg F1 75.0 on ProcessBench (ActPRM-X reaches 76.0), surpassing Qwen2.5-Math-PRM-7B (avg F1 73.5, arXiv 2501.07301). Generative PRMs via CoT verification (ThinkPRM, arXiv 2504.16828, ICLR 2026; GenPRM, arXiv 2504.00891, AAAI 2026) achieve F1 of 87.3/85.7 on hard subsets—a ~12-15 F1 point advantage over the best discriminative PRMs. This means a router can now select between two genuinely strong modes.\\n\\n(2) Dyve demonstrated that step-level paradigm selection is technically feasible and valuable—outperforming all contemporaneous baselines. But its implicit SFT routing conflates when to switch with how to verify, preventing composition with stronger base models. The gap between Dyve (avg F1 55.8) and modern discriminative PRMs (avg F1 75.0) reveals that the bottleneck is the entangled routing mechanism, not the adaptive concept. This mirrors the routing-representation interference characterized in MoE literature: Grouter (arXiv 2603.06626, ICML 2026) demonstrated that decoupling routing from representation yields 4.28x data efficiency improvement by eliminating mutual gradient interference; StableMoE (arXiv 2204.08396, ACL 2022) showed that entangled routing creates 'routing fluctuation' that harms sample efficiency. CRISP-PRM's explicit routing via a lightweight criticality estimator (SCE) is model-agnostic and immediately benefits from advances in either paradigm—satisfying the 'independent improvability' criterion formalized by D'Amour et al. (arXiv 2103.11766, NeurIPS 2021).\\n\\n(3) Recent work on step-level uncertainty quantification provides validated signals for criticality estimation: CoT Entropy (Ye et al., arXiv 2502.11250) achieves AUROC 0.680 as the best UQ method for generative PRMs; ReProbe/UHeads (arXiv 2511.06209, ACL 2026) provides lightweight step-level uncertainty heads where combining ReProbe scores with PRM scores outperforms either alone; F/S-RM's dual-confidence mechanism (arXiv 2603.20212) demonstrates that multi-signal routing outperforms single-signal. Additionally, Constrained GRPO (arXiv 2602.05863) and Faithful GRPO (arXiv 2604.08476) provide principled frameworks for training with hard quality constraints, enabling the F1 floor guarantee that prevents quality degradation during RL fine-tuning.\\n\\n(4) CRM's conditional probability chain rule (arXiv 2509.26578) decomposes trajectory correctness as S(t) = Π_{k=1}^{t}(1−h(k)), where h(t) = Pr(z=t|z≥t) is the conditional probability of entering a wrong state at step t given prior steps were correct. Combined with PURE's min-form credit assignment (arXiv 2504.15275), this proves the weakest step dominates solution quality, implying verification effort should concentrate on steps with highest conditional error probability.\\n\\n(5) VerifySteer (arXiv 2605.20745, May 2026) shows verification compute can be reduced 4-7x through principled intervention at ProcessBench F1 of 72.3, confirming large optimization headroom that is orthogonal to and composable with CRISP-PRM's approach.\\n\\n(6) Hard2Verify (arXiv 2510.13744) reveals catastrophic verification failure on frontier-difficulty problems (best discriminative PRM F1 drops from 78.3% to 37.3%), demonstrating that the gap between discriminative and generative verification widens with difficulty—making adaptive paradigm selection increasingly valuable precisely where it matters most.\\n\\nThe unoccupied synthesis is explicit step-level paradigm selection within a unified dual-mode verifier, grounded in the decoupling principle from modular systems research, with composable routing designed to work with modern strong base models—addressing exactly the ceiling that Dyve's entangled approach hits.\",\n  \"landscape\": \"**Discriminative PRMs.** ActPRM (arXiv 2504.10559) is the current leading discriminative PRM at the 7B scale, achieving ProcessBench avg F1 of 75.0 (ActPRM-X: 76.0) via active learning-based data-efficient training. Qwen2.5-Math-PRM-7B (arXiv 2501.07301) achieves avg F1 73.5 with F1 of 82.4/77.6/67.5/66.3 across GSM8K/MATH/OlympiadBench/OmniMATH, as reported in ProcessBench (arXiv 2412.06559, ACL 2025) and independently verified in R-PRM (arXiv 2503.21295, EMNLP 2025, Table 1). Its error detection accuracy (err acc) degrades from 72.0% (GSM8K) to 55.2% (OmniMATH), while correctness accuracy (corr acc) remains relatively stable (96.4% to 83.0%). AdaptiveStep/ASPRM (arXiv 2502.13943) proposes confidence-based step boundary detection for PRM training but does not evaluate on ProcessBench. At 72B scale, Qwen2.5-Math-PRM-72B reaches F1 78.3. Earlier PRMs include Qwen2.5-Math-7B-PRM800K (avg F1 ~41), Skywork-PRM-7B (~35). PRMBench shows discriminative PRMs achieve near-random performance on 'simplicity' error types (redundancy, circular logic). SCAN (arXiv 2509.16548, NeurIPS 2025) provides an efficient data synthesis and noise-tolerant learning framework.\\n\\n**Verification on Frontier-Difficulty Problems.** Hard2Verify (arXiv 2510.13744) provides a step-level verification benchmark on 2024-2025 Olympiad-level problems and reveals catastrophic failure of current PRMs on frontier math: Qwen2.5-Math-PRM-72B achieves only 37.3% F1 on Hard2Verify ErrorID (vs 78.3% on ProcessBench), a 41 percentage point drop. This demonstrates that ProcessBench scores do not generalize to frontier problems, and that the gap between discriminative and generative verification capabilities widens dramatically with difficulty—strengthening the case for adaptive paradigm selection.\\n\\n**Generative PRMs.** ThinkPRM (arXiv 2504.16828, ICLR 2026) scales verification compute via extended CoT thinking, achieving F1 of 87.3/85.7 on OlympiadBench/OmniMATH with ThinkPRM-14B—a ~12-15 F1 point advantage over the best discriminative PRMs on hard subsets, but at ~100-500x compute cost per step. GenPRM (arXiv 2504.00891, AAAI 2026) shows GenPRM-1.5B outperforms GPT-4o on ProcessBench via code-augmented generative verification; GenPRM-7B achieves avg F1 75.2 (Pass@1) and 80.5 (Maj@8).\\n\\n**Step-Level Adaptive Verification (Implicit Routing).** Dyve (arXiv 2502.11157, EMNLP 2025) is the most directly related prior work and the pioneer of step-level paradigm selection. It trains a single DeepSeek-R1-Distill-Qwen-14B via standard cross-entropy SFT on 117K examples to implicitly route between System 1 (single-token '+' confirmation) and System 2 (CoT analysis, up to 8192 tokens). ProcessBench F1: 68.5/58.3/49.0/47.2 (avg ~55.8). Critically, Dyve outperformed ALL contemporaneous baselines at the time of publication. However, stronger discriminative PRMs (ActPRM avg F1 75.0; Qwen2.5-Math-PRM-7B avg F1 73.5) have since surpassed Dyve's performance. This reveals a ceiling of implicit/entangled routing: (a) the routing decision is entangled with the verification itself (learned output length as proxy), preventing composition with independently improved verifiers—analogous to the routing-representation interference identified in MoE research (Grouter, arXiv 2603.06626, ICML 2026); (b) steps are scored independently with no sequential error cascade awareness; (c) standard cross-entropy SFT provides no quality floor guarantee; (d) no separable routing component enables ablation or interpretability. CRISP-PRM builds on Dyve's pioneering insight with explicit, decoupled routing designed to work with stronger base models.\\n\\n**Modular and Decoupled Systems Theory.** Grouter (arXiv 2603.06626, ICML 2026) demonstrates that decoupling routing topology from expert representation in MoE eliminates mutual optimization interference, boosting data utilization by 4.28x and throughput by 33.5%. StableMoE (arXiv 2204.08396, ACL 2022) identifies 'routing fluctuation' as a pathology of entangled routing-representation training and solves it by distilling a decoupled router. D'Amour et al. ('Fixes That Fail,' arXiv 2103.11766, NeurIPS 2021) formally show that in composed ML systems, improving one component can degrade downstream performance unless interfaces are decoupled—establishing independent improvability as requiring architectural separation. Select-then-Solve (arXiv 2604.06753, Apr 2026) demonstrates that no single inference paradigm dominates across tasks; oracle per-task paradigm selection beats the best fixed paradigm by 17.1pp, with a lightweight router recovering up to 37% of the oracle gap. These results collectively provide theoretical grounding for CRISP-PRM's core design principle: decoupling verification paradigm selection from verification execution.\\n\\n**Step-Level Uncertainty Quantification.** CoT Entropy (Ye et al., arXiv 2502.11250, Feb 2025) introduces a novel UQ method for step-level verification in generative PRMs: it samples multiple reasoning paths at each step, groups outputs by binary correctness decisions, and computes entropy over the marginal distribution: H = −Σ_e(Σ_c p_θ(c,e|x≤t)) log(Σ_c p_θ(c,e|x≤t)). Achieves AUROC 0.680, outperforming all UQ baselines (SEU-MiniLM 0.661, SEU-NV-Embed). ReProbe/UHeads (arXiv 2511.06209, ACL 2026) provides lightweight step-level uncertainty heads; combining ReProbe scores with PRM scores outperforms either alone.\\n\\n**Problem-Level Fast/Slow Routing.** F/S-RM (arXiv 2603.20212, Mar 2026) trains a single Qwen3-8B with dual fast (first-token scalar) and slow (CoT generation) modes, using dual-confidence activation to route at the problem level; achieves 20.8% token savings but never considers within-solution step variation. E-GRM (arXiv 2604.10072, ACL 2026) routes between direct inference and CoT generation via parallel-decoding consensus at the problem level; 62% latency reduction and 49% FLOP reduction on MATH. CAMEL (arXiv 2602.20670, ICML 2026) uses log-probability confidence gating for pairwise preference judging; problem-level and not PRM-specific.\\n\\n**Step-Level Generation Routing.** TRIM (arXiv 2601.10245, ICLR 2026) performs step-level routing between small and large generation models using PRM-derived uncertainty, achieving 5x cost efficiency on MATH-500; routes generators, not verification paradigms.\\n\\n**Verification Compute Optimization.** VerifySteer (arXiv 2605.20745, May 2026) identifies verifier strictness signals in hidden states at paragraph-boundary delimiter tokens and steers verification depth via selective latent interventions. Achieves ProcessBench F1 of 72.3 with Qwen3-8B at 4-7x less inference compute than self-consistency; orthogonal to and composable with fine-tuned verifiers. Adaptive Test-Time Compute (arXiv 2602.03975, Feb 2026) performs state-level selective verification combining deterministic feasibility gating with learned scoring and adaptive allocation, achieving 30% fewer verifier calls on MATH-500. Budget-aware Test-time Scaling (arXiv 2510.14913, 2025) shows discriminative verifiers + self-consistency (Pessimistic Verification) outperform generative verifiers under constrained FLOP budgets.\\n\\n**Constrained RL for Quality Guarantees.** Constrained GRPO (arXiv 2602.05863, Feb 2026) introduces a Lagrangian-based extension of GRPO for constrained policy optimization with indicator cost functions, scalarized advantage construction (preventing standard-deviation mismatch), and learned multipliers. Faithful GRPO (arXiv 2604.08476, Apr 2026) applies this to transform quality metrics from reward terms into hard constraints via Lagrangian dual ascent, reducing inconsistency from 24.5% to 1.7%.\\n\\n**Adaptive Thinking for Generators.** PATS (arXiv 2505.19250, May 2025) introduces process-level adaptive thinking mode switching for generators. Adjusts beam width per step based on PRM scores, achieving near-optimal accuracy at 55% of full-compute token usage. PATS adapts generation depth; CRISP-PRM adapts verification depth—complementary.\\n\\n**Credit Assignment and Error Propagation.** CRM (arXiv 2509.26578, 2025) frames step correctness using conditional probability chain rules: defining h(t) = Pr(z=t|z≥t) as the conditional probability of entering a wrong state at step t given all prior steps were correct, and decomposing trajectory correctness as S(t) = Π_{k=1}^{t}(1−h(k)). Step rewards derive from a potential function Φ(s_t) = log S(t), yielding per-step reward r_t = log(1−h(t)). PURE (arXiv 2504.15275, 2025) introduces min-form credit assignment proving the weakest step dominates. 'Beyond the First Error' (arXiv 2505.14391, 2025) distinguishes error propagation from error cessation.\\n\\n**PRM Calibration.** 'Know What You Don't Know' (arXiv 2506.09338, NeurIPS 2025) demonstrates PRMs are poorly calibrated, overestimating success probability—motivating multi-signal criticality estimation rather than relying on single PRM confidence scores.\\n\\n**Summary.** Dyve pioneered step-level paradigm selection and outperformed all contemporaneous baselines, demonstrating the value of adaptive verification. However, no existing system combines (a) explicit, decoupled criticality estimation grounded in the principle that verification selection and verification execution are separate concerns, (b) sequential error cascade awareness, (c) constrained training with F1 floor guarantees, and (d) demonstrated robustness to changing cost ratios between verification paradigms.\",\n  \"inspired_by\": \"Convergence of five research threads with a critical empirical insight, unified by a theoretical principle from modular systems research: (1) Dyve (EMNLP 2025) demonstrated that step-level fast/slow verification within a single model is feasible and valuable, outperforming all contemporaneous baselines. The subsequent emergence of stronger discriminative PRMs (ActPRM, avg F1 75.0) that surpass Dyve reveals that implicit/entangled routing hits a ceiling—motivating explicit, decoupled routing. (2) MoE literature (Grouter, ICML 2026; StableMoE, ACL 2022) and composed ML systems theory ('Fixes That Fail,' NeurIPS 2021) formally establish that entangled routing-computation optimization creates mutual interference and prevents independent improvability—providing theoretical grounding for why Dyve's ceiling exists and why decoupled routing is the solution. (3) F/S-RM (Mar 2026) proves a single model can support both discriminative and generative modes with dual-confidence routing → provides the architectural foundation. (4) CRM's conditional probability chain rule decomposes trajectory correctness as S(t) = Π(1−h(t)) and PURE's min-form credit assignment proves the weakest step dominates → verification effort should target steps with highest conditional error probability. (5) CoT Entropy (arXiv 2502.11250) achieves best-in-class step-level UQ for generative PRMs (AUROC 0.680) → provides validated signal for criticality estimation. (6) Constrained GRPO (arXiv 2602.05863) and Faithful GRPO (arXiv 2604.08476) provide principled frameworks for enforcing quality constraints during RL training → enables the F1 floor guarantee. Pattern: 'Dyve showed the right question (adaptive step verification). The next step requires principled decoupling of verification paradigm selection from verification execution—a design principle established in MoE research but not yet applied to PRM verification—composed with stronger base models, principled criticality estimation, and constrained training with quality guarantees.'\",\n  \"approach\": \"We propose CRISP-PRM (CRIticality-based Step-level Paradigm selection for Process Reward Models), a framework built on a unified dual-mode verifier that selects the verification paradigm—fast (discriminative) or deep (generative CoT)—for each reasoning step based on estimated step criticality, under a compute budget constraint. Building on Dyve's pioneering demonstration that step-level paradigm selection outperforms contemporaneous baselines, CRISP-PRM introduces explicit, decoupled routing designed to work with modern strong base models.\\n\\n**Theoretical Foundation: The Decoupling Principle for Verification**\\n\\nCRISP-PRM is grounded in a key insight from modular systems research: verification paradigm selection and verification execution are fundamentally different concerns that must be architecturally decoupled. In entangled systems like Dyve, the routing decision (when to use deep verification) is learned jointly with the verification itself (how to verify), through output length as an implicit proxy. This creates three well-characterized pathologies: (a) Optimization interference: gradients for improving routing conflict with gradients for improving verification, as demonstrated in MoE research where Grouter (arXiv 2603.06626, ICML 2026) showed 4.28x data efficiency gains from decoupling routing from representation. (b) Routing fluctuation: the same step may be routed differently during training vs. inference when routing is entangled with learned representations, as StableMoE (arXiv 2204.08396, ACL 2022) identified and solved via decoupled router distillation. (c) Failure of independent improvability: in composed ML systems, improving one component can degrade downstream performance unless interfaces are decoupled (D'Amour et al., arXiv 2103.11766, NeurIPS 2021). This explains why Dyve cannot benefit from stronger discriminative PRMs—the entangled routing has no separable interface through which to inject improvements. CRISP-PRM's explicit SCE provides this interface: advances in discriminative PRMs, generative PRMs, or uncertainty estimation each independently improve system performance without retraining the other components.\\n\\n**Architecture: Unified Dual-Mode PRM**\\n\\nCRISP-PRM uses a single Qwen3-8B model fine-tuned to support both verification modes, following the F/S-RM dual-mode paradigm adapted for step-level process verification:\\n\\n• Fast mode: Given (problem, solution prefix, step_i), the model's first generated token is a correctness judgment ('correct'/'incorrect'). The token probability p(correct|context) serves directly as a scalar step reward. Cost: ~10ms/step (single forward pass). No separate classification head needed—the standard LM head suffices.\\n\\n• Deep mode: A special trigger token is appended to the prompt, bypassing fast judgment and entering CoT verification. The model generates a step-by-step verification rationale inside &lt;verify>...&lt;/verify> tags, then outputs a final correctness judgment. Cost: ~100ms-2s/step depending on model size and generation length.\\n\\n**Training Pipeline: Two-Stage with Constrained RL**\\n\\nStage 1 — SFT Foundation: Combined loss L = L_step + λ·L_action, where L_step is binary cross-entropy on step labels (fast mode) combined with generation loss on synthetic verification CoTs from ThinkPRM-style data (deep mode), and L_action is an action-space constraint penalizing probability leakage to irrelevant tokens during fast mode.\\n\\nStage 2 — Constrained GRPO with F1 Floor: We adopt the Constrained GRPO framework (arXiv 2602.05863) to fine-tune the unified model with a hard F1 floor guarantee—ensuring the model never degrades below the current discriminative SOTA quality. Concrete specification:\\n\\n(a) Indicator cost function: C_F1(π) = 𝕀[F1_batch(π) < F1_threshold], where F1_threshold is set to the current discriminative SOTA F1 on a held-out ProcessBench validation split (avg F1 75.0 for ActPRM-class models; we use the best available discriminative PRM at training time).\\n\\n(b) Lagrangian objective: ℒ(π,λ) = J_R(π) − λ·(J_C(π) − d̃), where J_R is the primary reward (format correctness + outcome accuracy for both fast and deep modes), J_C is the constraint violation rate, and d̃ is the target violation rate (0.05 = at most 5% of validation batches may fall below F1_threshold).\\n\\n(c) Scalarized advantage construction (NOT scalarized rewards, following arXiv 2602.05863 Theorem 4.1 to prevent standard-deviation mismatch): A_ScAdv = λ_R·Z_R − λ_C·Z_C, where Z_j = (Component_j − mean(Component_j))/std(Component_j) are per-component standardized advantages. This preserves the intended trade-off between reward maximization and constraint satisfaction.\\n\\n(d) Multiplier update: ∇_λ ℒ = −(J_C(π) − d̃), applied via gradient descent with projection λ ≥ 0. When F1 drops below threshold (J_C > d̃), the gradient is positive, increasing λ and strengthening the constraint penalty.\\n\\n(e) Conservative checkpoint selection as fallback: evaluate F1 on validation set per epoch; only accept parameter updates that maintain F1 above threshold. This provides a hard guarantee even if the Lagrangian balance oscillates during training.\\n\\nThis follows the precedent of Faithful GRPO (arXiv 2604.08476), which demonstrated that transforming quality metrics from reward terms into hard constraints via Lagrangian dual ascent reduces quality degradation from 24.5% to 1.7%.\\n\\n**Step Criticality Estimator (SCE)**\\n\\nA lightweight module (<1M params) that scores each step's need for deep verification using multiple complementary signals. Unlike Dyve's implicit routing (where the model learns to self-regulate output length through SFT, with no separable routing component), the SCE is an explicit, interpretable, and ablatable module—the architectural embodiment of the decoupling principle.\\n\\nThe SCE combines:\\n1. Fast-mode intuition confidence: C_I = |p(correct) − p(incorrect)| from the fast verification pass (available as a byproduct)\\n2. Fast-mode token confidence: C_T = mean negative log-probability of irrelevant tokens, measuring probability mass leakage beyond the binary judgment (from F/S-RM's dual-confidence mechanism)\\n3. CoT Entropy signal: Following Ye et al. (arXiv 2502.11250), when running complementary analysis, sample multiple reasoning paths at each step and compute entropy over the marginal distribution of binary decision outcomes: H = −Σ_e(Σ_c p_θ(c,e|x≤t)) log(Σ_c p_θ(c,e|x≤t)). Steps with high CoT Entropy indicate verifier uncertainty requiring deeper analysis. Optional when compute-constrained.\\n4. Generator internal uncertainty: entropy of the generating model's hidden states via ReProbe-style probes (<10M params on frozen generator), when generator internals are available. Optional for black-box generator settings.\\n5. Structural features: step position in chain, relative token length, domain signal. Justified by CoLD (arXiv 2507.15698) showing PRMs have strong length bias.\\n\\nThe SCE is an MLP that outputs a criticality score c_i ∈ [0,1] for each step. Training signal derives from oracle construction: run both fast and deep modes on training steps, identify 'value-add' steps where fast mode misclassifies but deep mode succeeds, and train SCE via binary cross-entropy. We include a planned ablation ladder: (i) fast-mode confidence only → (ii) dual-confidence (C_I + C_T) → (iii) +CoT Entropy → (iv) +ReProbe → (v) +structural features.\\n\\n**Budget-Constrained Router**\\n\\nGiven a per-solution compute budget B (fraction of steps receiving deep verification), the router:\\n1. Runs fast verification on ALL K steps (cheap baseline, ~60ms for 6 steps). This simultaneously produces scalar scores and SCE input signals.\\n2. Computes criticality scores c_i for all steps.\\n3. Selects the top-⌈B·K⌉ highest-criticality steps for deep verification.\\n4. Final step scores combine fast and deep assessments: steps receiving only fast verification use the fast scalar score; steps receiving deep verification use the deep judgment.\\n\\nThe budget B is a tunable hyperparameter that parameterizes the cost-accuracy Pareto frontier: at B=0, all steps use fast verification (cheapest); at B=1, all steps use deep verification (most accurate). The SCE threshold mapping to a given B is calibrated from the empirical criticality score distribution on a calibration set. Critically, the cost ratio between paradigms enters ONLY through B—as generative costs decrease, B can be increased to allocate more deep verification at the same total cost.\\n\\n**Sequential Error Cascade (SEC) Enhancement (Optional)**\\n\\nFor applications where step ordering matters, we add a sequential processing mode grounded in CRM's conditional probability chain rule (arXiv 2509.26578), which decomposes trajectory correctness as S(t) = Π_{k=1}^{t}(1−h(k)) where h(t) is the conditional probability of entering a wrong state at step t given prior steps were correct, and PURE's min-form insight:\\n- If deep verification detects an ERROR at step i: automatically flag all subsequent steps for deep verification or assign minimum scores (since they are built on faulty premises, and S(T) ≤ S(i) per the multiplicative decomposition).\\n- If deep verification CONFIRMS correctness: update posterior criticality of subsequent steps, potentially lowering priority for dependent downstream steps.\\nThis is an optional enhancement that provides marginal accuracy gains on top of the core budget-constrained routing.\\n\\n**Robustness to Cheaper Generative Verification**\\n\\nCRISP-PRM's value proposition is robust to future reductions in generative verification cost, for six reasons: (a) Even a 10x speedup in generative models leaves a 10-50x cost gap (100-500ms vs 10ms per step)—routing still provides substantial efficiency gains. (b) The SCE provides accuracy gains independent of cost: by identifying which steps most benefit from deeper analysis, routing improves verification allocation quality regardless of per-mode costs. Even at equal costs, selectively applying deep verification to high-criticality steps outperforms uniform application because the model's deep mode may still outperform its fast mode on specific error types (e.g., soundness errors, multi-step logical chains). (c) CRISP-PRM's routing is parameterizable—the cost ratio enters only through the budget constraint B and SCE threshold, both tunable hyperparameters. As costs converge, B increases to allocate more deep verification while maintaining cost parity with uniform fast. (d) In the limit where generative cost equals discriminative cost, CRISP-PRM degenerates to uniform deep verification, which is the accuracy-optimal baseline—the framework gracefully adapts rather than becoming irrelevant. (e) Historical analog: TRIM (arXiv 2601.10245) shows step-level routing between models of different sizes remains valuable even as smaller models improve, because the relative cost gap persists across model generations. (f) GenPRM-1.5B still requires multiple forward passes for CoT generation—the cost gap is fundamental (single-token vs multi-token generation) rather than purely model-size dependent.\\n\\n**Difficulty-Stratified Efficiency Analysis**\\n\\nUsing ProcessBench data (arXiv 2412.06559, ACL 2025; verified in R-PRM, arXiv 2503.21295, EMNLP 2025, Table 1) for Qwen2.5-Math-PRM-7B: err accuracy of 72.0%/68.0%/55.7%/55.2% and corr accuracy of 96.4%/90.4%/85.5%/83.0% across GSM8K/MATH/OlympiadBench/OmniMATH. Hard2Verify (arXiv 2510.13744) further shows that on frontier-difficulty problems, the best discriminative PRM collapses to F1 37.3—indicating the fraction of steps requiring deep verification scales superlinearly with difficulty:\\n\\n• Easy tier (GSM8K-level): Fast verification reliable on ~85-90% of steps. Deep needed on ~10-15%. Expected latency reduction vs uniform deep: ~87%.\\n• Medium tier (MATH-level): Fast verification reliable on ~80-85% of steps. Deep needed on ~15-20%. Expected reduction: ~82%.\\n• Hard tier (OlympiadBench-level): Fast verification reliable on ~70-80% of steps. Deep needed on ~20-30%. Expected reduction: ~75%.\\n• Hardest tier (OmniMATH-level): Fast verification reliable on ~65-75% of steps. Deep needed on ~25-35%. Expected reduction: ~70%.\\n• Frontier tier (Hard2Verify-level): Fast verification reliable on ~40-60% of steps. Deep needed on ~40-60%. Expected reduction: ~50%. CRISP-PRM's relative accuracy gain is maximized here.\\n\\nCRISP-PRM's value proposition is difficulty-adaptive: on easy problems, it saves the most compute; on hard and frontier problems, it provides the largest accuracy gains.\\n\\n**Evaluation Protocol**\\n\\n• Step-level accuracy: F1 on ProcessBench (GSM8K/MATH/OlympiadBench/OmniMATH subsets reported separately, with err/corr accuracy breakdown) and PRMBench (fine-grained error type breakdown). If accessible, Hard2Verify ErrorID evaluation to test frontier generalization.\\n• Solution-level utility: Best-of-N reranking accuracy on MATH-500, AIME'24, GPQA-Diamond\\n• Efficiency: FLOPs per solution, accuracy-per-FLOP Pareto frontiers at multiple budget levels B ∈ {0.05, 0.1, 0.2, 0.3, 0.5, 1.0}\\n• Baselines: (i) uniform fast PRM (ActPRM, avg F1 75.0; and Qwen2.5-Math-PRM-7B, avg F1 73.5), (ii) uniform deep PRM (ThinkPRM-14B), (iii) Dyve (implicit step-level routing, avg F1 ~55.8)—HISTORICAL BASELINE showing progress from Dyve's pioneering work, (iv) problem-level routing (F/S-RM-style dual-confidence gating), (v) VerifySteer (latent steering, F1 72.3), (vi) Budget-aware Pessimistic Verification, (vii) random step selection for deep verification (ablation control), (viii) PRM-confidence-only routing (single-signal ablation)\\n• Ablation studies: (A1) Explicit SCE routing vs. Dyve-style implicit SFT routing on SAME base model—isolating the value of decoupled routing (tests the decoupling principle directly); (A2) SCE signal ablation ladder (confidence-only → dual-confidence → +CoT Entropy → +ReProbe → +structural)—quantifying marginal signal contribution; (A3) Constrained GRPO (with F1 floor) vs. standard SFT for unified model training—testing whether Constrained GRPO prevents quality degradation; (A4) SEC-aware vs. independent greedy allocation—measuring value of sequential error cascade awareness; (A5) Budget sensitivity analysis across B ∈ {0.05, 0.1, 0.2, 0.3, 0.5}; (A6) Difficulty-stratified analysis showing per-tier routing rates and gains, including Hard2Verify-level problems if available\\n• Complementarity analysis: CRISP-PRM + VerifySteer (explicit routing + latent strictness steering); CRISP-PRM + PATS (verification routing + generation routing)\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"350 A100-80GB hours (80h unified model training (SFT + Constrained GRPO), 100h oracle construction running both modes on ~120K steps, 20h SCE/router training, 80h evaluation across 4 benchmarks × multiple budgets × 8 baselines including Dyve, 50h ablations (A1-A6), 10h ReProbe probe training, 10h VerifySteer comparison)\",\n      \"timeline\": \"10-14 weeks (single researcher)\",\n      \"estimated_gpu_cost\": \"$700 (at ~$2/hr A100-80GB cloud)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"280 A100-80GB hours (fewer dead-end experiments via Claude-guided threshold tuning and ablation prioritization)\",\n      \"timeline\": \"7-10 weeks\",\n      \"claude_api_cost\": \"$200-400 (experiment design, analysis scripts, paper writing assistance)\",\n      \"estimated_gpu_cost\": \"$560\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"480 A100-80GB hours (broader ablations: multiple SCE architectures, threshold sensitivity, cross-domain transfer, additional benchmarks including Hard2Verify, difficulty-stratified analysis, Dyve reproduction for fair comparison)\",\n      \"timeline\": \"4-6 weeks\",\n      \"claude_api_cost\": \"$400-700 (end-to-end experiment orchestration, code generation, result analysis)\",\n      \"estimated_gpu_cost\": \"$960\",\n      \"speed_bottleneck\": \"Unified model training is the main bottleneck (~80h); oracle construction is embarrassingly parallel—with 4×A100, drops from ~50h to ~13h wall-clock.\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (full papers Jul 28 2026, supplementary Jul 31 2026 — confirmed via official CFP)\",\n    \"ARR August 2026 cycle (Aug 3 2026, for commitment to NAACL 2027 or EACL 2027)\"\n  ],\n  \"level\": \"solid-to-strong\",\n  \"key_references\": [\n    \"Dyve: Thinking Fast and Slow for Dynamic Process Verification (arXiv 2502.11157, EMNLP 2025) — pioneered step-level System 1/System 2 routing; outperformed all contemporaneous baselines with avg F1 ~55.8; since surpassed by stronger discriminative PRMs\",\n    \"Process Reward Models That Think (ThinkPRM, arXiv 2504.16828, ICLR 2026)\",\n    \"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Model Parameters (ICLR 2025)\",\n    \"Fast-Slow Thinking RM: Efficient Integration of Scalar and Generative Reward Models (F/S-RM, arXiv 2603.20212, Mar 2026)\",\n    \"Reason Only When Needed: Efficient Generative Reward Modeling via Model-Internal Uncertainty (E-GRM, arXiv 2604.10072, ACL 2026)\",\n    \"CAMEL: Confidence-Gated Reflection for Reward Modeling (arXiv 2602.20670, ICML 2026)\",\n    \"TRIM: Hybrid Inference via Targeted Stepwise Routing in Multi-Step Reasoning Tasks (arXiv 2601.10245, ICLR 2026)\",\n    \"The Hidden Signal of Verifier Strictness: Controlling and Improving Step-Wise Verification via Selective Latent Steering (VerifySteer, arXiv 2605.20745, May 2026)\",\n    \"Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure (arXiv 2602.03975, Feb 2026)\",\n    \"PATS: Process-Level Adaptive Thinking Mode Switching (arXiv 2505.19250, May 2025)\",\n    \"Efficient Test-Time Scaling of Multi-Step Reasoning by Probing Internal States of Large Language Models (ReProbe/UHeads, arXiv 2511.06209, ACL 2026)\",\n    \"Stop Summation: Min-Form Credit Assignment Is All Process Reward Models Need (PURE, arXiv 2504.15275, 2025)\",\n    \"Conditional Reward Models for Process-Level Credit Assignment (CRM, arXiv 2509.26578, 2025) — uses conditional probability chain rules to decompose trajectory correctness as S(t) = Π(1−h(t)), where h(t) = Pr(z=t|z≥t) is the conditional error probability at step t\",\n    \"Beyond the First Error: Modeling Error Propagation and Cessation in Multi-Step Reasoning (arXiv 2505.14391, 2025)\",\n    \"Know What You Don't Know: Calibration of Process Reward Models (arXiv 2506.09338, NeurIPS 2025)\",\n    \"ProcessBench: Identifying Process Errors in Mathematical Reasoning (arXiv 2412.06559, ACL 2025)\",\n    \"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (arXiv 2501.03124, 2025)\",\n    \"When to Trust the Cheap Check: Weak and Strong Verification for Reasoning (arXiv 2602.17633, Feb 2026)\",\n    \"Budget-aware Test-time Scaling via Discriminative Verification (arXiv 2510.14913, 2025)\",\n    \"When To Solve, When To Verify: Compute-Optimal Problem Solving and Verification (arXiv 2504.01005, 2025)\",\n    \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (arXiv 2504.00891, AAAI 2026)\",\n    \"SCAN: Self-Denoising Monte Carlo Annotation for Robust Process Reward Learning (arXiv 2509.16548, NeurIPS 2025)\",\n    \"R-PRM: Reasoning-Driven Process Reward Modeling (arXiv 2503.21295, EMNLP 2025) — Table 1 provides independently verified ProcessBench numbers for Qwen2.5-Math-PRM-7B\",\n    \"The Lessons of Developing Process Reward Models in Mathematical Reasoning (arXiv 2501.07301, 2025) — Qwen2.5-Math-PRM development and evaluation\",\n    \"Uncertainty-Aware Step-wise Verification with Generative Reward Models (Ye et al., arXiv 2502.11250, Feb 2025) — CoT Entropy for step-level UQ in generative PRMs; AUROC 0.680\",\n    \"Constrained Group Relative Policy Optimization (arXiv 2602.05863, Feb 2026) — Lagrangian-based constrained GRPO with scalarized advantage construction; foundation for F1 floor mechanism\",\n    \"Faithful GRPO: Improving Visual Spatial Reasoning via Constrained Policy Optimization (arXiv 2604.08476, Apr 2026) — precedent for transforming quality metrics into hard constraints via Lagrangian dual ascent\",\n    \"Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling (VG-Search, arXiv 2505.11730, NeurIPS 2025)\",\n    \"CoLD: Mitigating Length Bias in Process Reward Models (arXiv 2507.15698, 2025)\",\n    \"SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation (arXiv 2604.06636, Apr 2026)\",\n    \"SPAE: Step Potential Advantage Estimation for Credit Assignment (arXiv 2601.03823, Jan 2026)\",\n    \"Efficient Process Reward Model Training via Active Learning (ActPRM, arXiv 2504.10559, 2025) — current discriminative PRM SOTA on ProcessBench at 7B scale, avg F1 75.0 (ActPRM-X: 76.0)\",\n    \"Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math (arXiv 2510.13744, 2025) — reveals catastrophic failure of discriminative PRMs on frontier problems (F1 78.3 → 37.3)\",\n    \"Grouter: Decoupling Routing from Representation (arXiv 2603.06626, ICML 2026) — demonstrates 4.28x data efficiency from decoupling routing topology in MoE; theoretical foundation for the decoupling principle\",\n    \"StableMoE: Stable Routing Strategy for Mixture of Experts (arXiv 2204.08396, ACL 2022) — identifies routing fluctuation as a pathology of entangled routing-representation training\",\n    \"Underspecification Presents Challenges for Credibility in Modern Machine Learning (D'Amour et al., arXiv 2011.03395 / 2103.11766, NeurIPS 2021) — formalizes how improving one component in composed systems can degrade others without decoupled interfaces\",\n    \"Select-then-Solve: Paradigm Routing as Inference-Time Optimization for LLM Agents (arXiv 2604.06753, Apr 2026) — shows oracle paradigm selection beats best fixed paradigm by 17.1pp; validates learned paradigm routing\",\n    \"AdaptiveStep: Automatically Dividing Reasoning Step through Model Confidence (ASPRM, arXiv 2502.13943, Feb 2025) — confidence-based step boundary detection for PRM training\"\n  ],\n  \"description\": \"We propose CRISP-PRM (CRIticality-based Step-level Paradigm selection for Process Reward Models), a framework built on a unified dual-mode verifier that routes each reasoning step to the optimal verification paradigm—fast discriminative scoring or deep generative CoT verification—based on explicit step criticality estimation and a tunable compute budget. Building on Dyve's (EMNLP 2025) pioneering demonstration that step-level paradigm selection outperforms contemporaneous baselines, CRISP-PRM introduces a principled advance grounded in the decoupling principle from modular systems research: verification paradigm selection and verification execution are fundamentally different concerns that must be architecturally separated to enable independent improvement of each component. Three concrete innovations implement this principle: (1) An explicit Step Criticality Estimator (SCE) combining dual-confidence signals from fast verification, CoT Entropy-based uncertainty (Ye et al., arXiv 2502.11250, AUROC 0.680), generator-internal uncertainty (ReProbe-style probes), and structural features—with an ablation ladder quantifying each component's marginal value. Unlike Dyve's entangled routing (where routing and verification are jointly optimized, creating the routing-representation interference characterized by Grouter, arXiv 2603.06626, ICML 2026), the SCE is a separable module that enables each verification paradigm to be independently upgraded. (2) A budget-constrained router that parameterizes the cost-accuracy Pareto frontier through a single hyperparameter B (fraction of steps receiving deep verification), enabling graceful adaptation to changing cost ratios: as generative verification becomes cheaper, B increases; in the limit of equal costs, the system degenerates to uniform deep verification. (3) Constrained GRPO fine-tuning (following arXiv 2602.05863) with a hard F1 floor guarantee via indicator cost functions, Lagrangian dual ascent with scalarized advantage construction, and conservative checkpoint selection—ensuring the unified model never degrades below discriminative SOTA quality (ActPRM avg F1 75.0, arXiv 2504.10559). Using ProcessBench data (arXiv 2412.06559, ACL 2025; verified in R-PRM, arXiv 2503.21295, Table 1) and Hard2Verify findings (arXiv 2510.13744, best discriminative PRM F1 collapses from 78.3% to 37.3% on frontier problems), we estimate ~10-15% of easy-tier steps and ~25-35% of hard-tier steps benefit from deep verification, yielding 70-87% latency reduction vs. uniform deep verification while targeting Pareto dominance over both uniform paradigms and problem-level routing approaches. The increasing verification gap at frontier difficulty levels (Hard2Verify) makes adaptive paradigm selection most valuable precisely where it matters most.\",\n  \"project_name\": \"crisp_step_prm\",\n  \"source\": \"web_research\",\n  \"reviewer_response\": {\n    \"CRM_MISCHARACTERIZATION\": \"Resolved. The fabricated 'survival analysis' and 'hazard function' terminology attributed to CRM has been removed throughout all sections. CRM is now accurately characterized using its own framing: conditional probability chain rules, where h(t) = Pr(z=t|z≥t) is the conditional probability of entering a wrong state at step t given prior steps were correct, with trajectory correctness decomposed as S(t) = Π_{k=1}^{t}(1−h(k)). This multiplicative decomposition IS in the CRM paper (it is the core equation), but CRM frames it as conditional probability modeling, not survival analysis. The mathematical form is retained because it is accurate and supports the SEC module's theoretical grounding. The distinction between CRM's actual framing (conditional probability) and the isomorphic survival-theoretic interpretation is now clear: we use CRM's terminology throughout. PURE's min-form insight continues to provide complementary justification. Corrections applied in: core_problem, opportunity, landscape, inspired_by, approach (SEC module), key_references, and description.\",\n    \"OUTDATED_DISCRIMINATIVE_SOTA\": \"Resolved. ActPRM (arXiv 2504.10559) is now cited as the current discriminative PRM SOTA at 7B scale with avg F1 75.0 (ActPRM-X: 76.0), surpassing Qwen2.5-Math-PRM-7B (73.5). The F1 floor threshold has been updated to 75.0 (matching ActPRM). ASPRM (arXiv 2502.13943) is added to the landscape with the accurate characterization that it proposes confidence-based step boundary detection but does NOT evaluate on ProcessBench. The reviewer's arXiv ID for ActPRM (2601.22249) could not be verified; we cite the correct ID (2504.10559) confirmed through direct paper access. Hard2Verify (arXiv 2510.13744) is now integrated throughout: it shows Qwen2.5-Math-PRM-72B F1 drops from 78.3% to 37.3% on frontier-difficulty problems, which STRENGTHENS the case for adaptive paradigm selection since the discriminative-generative gap widens with difficulty. A new 'Frontier tier' has been added to the difficulty-stratified analysis. Updates applied in: core_problem, opportunity, landscape, approach (F1 threshold, difficulty analysis, baselines, evaluation protocol), key_references, and description.\",\n    \"UNVERIFIABLE_VENUE_CLAIMS\": \"Resolved via independent verification. All venue claims were checked against arXiv annotations, ACL Anthology, official proceedings pages, and author repositories. Results: GenPRM AAAI 2026 — VERIFIED (GitHub repo confirms acceptance 2025-11-08); E-GRM ACL 2026 — VERIFIED (arXiv Comments field); CAMEL ICML 2026 — VERIFIED (arXiv Comments field and ICML 2026 Downloads page); SCAN NeurIPS 2025 — VERIFIED (NeurIPS 2025 virtual poster page); Dyve EMNLP 2025 — VERIFIED (ACL Anthology); ProcessBench ACL 2025 — VERIFIED (ACL Anthology); R-PRM EMNLP 2025 — VERIFIED (ACL Anthology). ONE CORRECTION: ReProbe/UHeads was incorrectly labeled 'NeurIPS 2025' — it is actually ACL 2026 Main (confirmed via arXiv Comments and project page at reprobe.github.io). This has been corrected in all references. ThinkPRM venue updated to ICLR 2026 based on verification.\",\n    \"NOVELTY_CEILING\": \"Addressed via explicit articulation of the 'Decoupling Principle for Verification' as the core scientific insight, grounded in three independent lines of theoretical evidence: (1) Grouter (arXiv 2603.06626, ICML 2026) demonstrates that decoupling routing from representation in MoE eliminates optimization interference, yielding 4.28x data efficiency—directly analogous to decoupling verification selection from verification execution. (2) StableMoE (arXiv 2204.08396, ACL 2022) identifies 'routing fluctuation' as a pathology of entangled routing that degrades inference-time performance. (3) D'Amour et al. ('Fixes That Fail,' arXiv 2103.11766, NeurIPS 2021) formally establishes that independent improvability in composed ML systems requires decoupled interfaces. Additionally, Select-then-Solve (arXiv 2604.06753) empirically validates that no single paradigm dominates and learned routing recovers significant oracle gaps. The contribution is now framed not as combining four techniques, but as demonstrating that verification paradigm selection and execution are fundamentally different concerns requiring architectural separation—a principle established in MoE and composed systems research but not yet applied to PRM verification. A new 'Theoretical Foundation' section in the approach section articulates this formally. Ablation A1 (explicit vs implicit routing on same base model) directly tests this principle empirically.\",\n    \"MISLEADING_DYVE_FRAMING\": \"Previously resolved (round 5). Maintained accurate historical characterization.\",\n    \"GRPO_F1_FLOOR_MECHANISM_UNSPECIFIED\": \"Previously resolved (round 5). F1 threshold updated to 75.0 (ActPRM SOTA).\",\n    \"MISSING_CITATION_COT_ENTROPY\": \"Previously resolved (round 5). Maintained.\",\n    \"UNVERIFIABLE_SCAN_TABLE_2_NUMBERS\": \"Previously resolved (round 5). Maintained proper source chain.\",\n    \"IMPACT_VULNERABILITY\": \"Previously resolved (round 5). Strengthened by Hard2Verify evidence showing discriminative-generative gap widens at frontier difficulty.\",\n    \"MISSING_CITATION_ADAPTIVE_TTC\": \"Previously resolved (round 3). Maintained.\",\n    \"MISSING_CITATION_PATS\": \"Previously resolved (round 3). Maintained.\",\n    \"MISSING_CITATION_VERIFYSTEER\": \"Previously resolved (round 3). Maintained.\",\n    \"FACTUAL_ERROR_ERR_ACCURACY\": \"Previously resolved (round 3). Maintained.\",\n    \"TWO_MODEL_MEMORY_OVERHEAD\": \"Previously resolved (round 2). Maintained.\",\n    \"STEP_DEPENDENCY_IGNORED\": \"Previously resolved (round 2). SEC now correctly cites CRM's conditional probability chain rule.\",\n    \"SCE_SIGNAL_REDUNDANCY\": \"Previously resolved (round 2). Maintained.\",\n    \"BUDGET_AWARE_TTS_OVERLAP\": \"Previously resolved (round 2). Maintained.\",\n    \"CRITICAL_NOVELTY_F_S_RM\": \"Previously resolved (rounds 1-2). Maintained.\",\n    \"CRITICAL_NOVELTY_E_GRM\": \"Previously resolved (rounds 1-2). Maintained.\",\n    \"CRITICAL_NOVELTY_CAMEL\": \"Previously resolved (rounds 1-2). Maintained.\"\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b29381b-eb00-4e5f-b248-f1c44305a86e",
  "isSidechain": false,
  "requestId": "req_011CbU8EfghaKiM2gWhTGgX2",
  "type": "assistant",
  "uuid": "2be97bc4-9c6b-4c91-934e-6375015f4752",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Br6bjxx2RaxqV3TGAtUhUr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5450,
      "cache_creation_input_tokens": 5916,
      "cache_read_input_tokens": 26622,
      "output_tokens": 17701,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5916,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5450,
          "output_tokens": 17701,
          "cache_read_input_tokens": 26622,
          "cache_creation_input_tokens": 5916,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5916
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

_source line 29 · 2026-05-28T01:55:23.453Z_

<details><summary>↩ Tool result · reported error · `toolu_01ExrVLsVXFjZd5qL9PRkm3c`</summary>

```text
Claude requested permissions to write to /tmp/crisp_prm_r6.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2be97bc4-9c6b-4c91-934e-6375015f4752",
  "isSidechain": false,
  "promptId": "a14d4547-e473-4da0-836a-c0e4d22dabcc",
  "type": "user",
  "uuid": "26dded15-2bd2-4de4-ab5b-b6b98ddae028",
  "toolUseResult": "Error: Claude requested permissions to write to /tmp/crisp_prm_r6.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "2be97bc4-9c6b-4c91-934e-6375015f4752",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"CRISP-PRM: Criticality-Aware Step-Level Paradigm Selection for Unified…",
  "leafUuid": "26dded15-2bd2-4de4-ab5b-b6b98ddae028",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising CRISP-PRM after round 5 reviewer feedback",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff"
}
```

---

### Tool call

_source line 32 · 2026-05-28T02:01:11.537Z_

<details open><summary>🔧 Tool call — Write · `toolu_018kdDzAou8Pqghvk4Z1zeUY`</summary>

```json
{
  "file_path": "/tmp/crisp_prm_r6.json",
  "content": "{\n  \"change_type\": \"minor\",\n  \"title\": \"CRISP-PRM: Criticality-Aware Step-Level Paradigm Selection for Unified Process Reward Models\",\n  \"core_problem\": \"Process reward models face a fundamental accuracy-cost trade-off at the step level: discriminative (fast scalar) verification is cheap (~10ms/step) but unreliable on hard reasoning steps, while generative (CoT) verification is far more accurate but ~100-500x more expensive (~1-5s/step). Dyve (arXiv 2502.11157, EMNLP 2025) demonstrated the feasibility and value of step-level fast/slow paradigm selection within a single model using implicit SFT-based routing, outperforming all contemporaneous baselines (Qwen2.5-Math-7B-PRM800K avg F1 ~41, Skywork-PRM-7B ~35, GPT-4o ~52) with avg F1 ~55.8. However, stronger discriminative PRMs trained with improved data pipelines—notably ActPRM (avg F1 75.0 on ProcessBench, arXiv 2504.10559) and Qwen2.5-Math-PRM-7B (avg F1 73.5, per R-PRM Table 1)—have since surpassed Dyve's adaptive performance using pure discriminative verification. This reveals that implicit SFT-based routing has a ceiling: when the routing mechanism is entangled with the verification itself (learned output length as a proxy for routing), the system cannot benefit from independently improving either the discriminative or generative verification mode. This entanglement mirrors the routing-representation interference identified in MoE research (Grouter, arXiv 2603.06626, ICML 2026; StableMoE, arXiv 2204.08396, ACL 2022), where joint optimization of routing and computation degrades both. Problem-level routing methods (F/S-RM, E-GRM, CAMEL) achieve efficiency gains but apply uniform verification to every step within a solution, ignoring that steps vary dramatically in difficulty and criticality. ProcessBench data confirms this variation: discriminative PRM error detection accuracy degrades from 72.0% (GSM8K) to 55.2% (OmniMATH) (ProcessBench, arXiv 2412.06559, ACL 2025; also R-PRM, arXiv 2503.21295, EMNLP 2025, Table 1). Moreover, Hard2Verify (arXiv 2510.13744) reveals that even the best discriminative PRM (Qwen2.5-Math-PRM-72B, F1 78.3 on ProcessBench) collapses to F1 37.3 on frontier-difficulty problems—demonstrating that the need for selective deep verification intensifies as problem difficulty increases. Can a unified dual-mode PRM with explicit, composable step-level paradigm selection—grounded in a principled decoupling of verification paradigm selection from verification execution—produce better accuracy-per-FLOP Pareto frontiers than both uniform paradigms, problem-level routing, and Dyve's implicit step-level routing, while enabling independent improvement of each component?\",\n  \"opportunity\": \"Four converging developments, plus a theoretical insight from modular systems research, create a clear opportunity for explicit criticality-based paradigm routing:\\n\\n(1) The maturation of both verification paradigms to strong individual performance. Discriminative PRMs have advanced substantially through improved training pipelines: ActPRM (arXiv 2504.10559) achieves avg F1 75.0 on ProcessBench (ActPRM-X reaches 76.0), surpassing Qwen2.5-Math-PRM-7B (avg F1 73.5, arXiv 2501.07301). Generative PRMs via CoT verification (ThinkPRM, arXiv 2504.16828, ICLR 2026; GenPRM, arXiv 2504.00891, AAAI 2026) achieve F1 of 87.3/85.7 on hard subsets—a ~12-15 F1 point advantage over the best discriminative PRMs. This means a router can now select between two genuinely strong modes.\\n\\n(2) Dyve demonstrated that step-level paradigm selection is technically feasible and valuable—outperforming all contemporaneous baselines. But its implicit SFT routing conflates when to switch with how to verify, preventing composition with stronger base models. The gap between Dyve (avg F1 55.8) and modern discriminative PRMs (avg F1 75.0) reveals that the bottleneck is the entangled routing mechanism, not the adaptive concept. This mirrors the routing-representation interference characterized in MoE literature: Grouter (arXiv 2603.06626, ICML 2026) demonstrated that decoupling routing from representation yields 4.28x data efficiency improvement by eliminating mutual gradient interference; StableMoE (arXiv 2204.08396, ACL 2022) showed that entangled routing creates 'routing fluctuation' that harms sample efficiency. CRISP-PRM's explicit routing via a lightweight criticality estimator (SCE) is model-agnostic and immediately benefits from advances in either paradigm—satisfying the 'independent improvability' criterion formalized by D'Amour et al. (arXiv 2103.11766, NeurIPS 2021).\\n\\n(3) Recent work on step-level uncertainty quantification provides validated signals for criticality estimation: CoT Entropy (Ye et al., arXiv 2502.11250) achieves AUROC 0.680 as the best UQ method for generative PRMs; ReProbe/UHeads (arXiv 2511.06209, ACL 2026) provides lightweight step-level uncertainty heads where combining ReProbe scores with PRM scores outperforms either alone; F/S-RM's dual-confidence mechanism (arXiv 2603.20212) demonstrates that multi-signal routing outperforms single-signal. Additionally, Constrained GRPO (arXiv 2602.05863) and Faithful GRPO (arXiv 2604.08476) provide principled frameworks for training with hard quality constraints, enabling the F1 floor guarantee that prevents quality degradation during RL fine-tuning.\\n\\n(4) CRM's conditional probability chain rule (arXiv 2509.26578) decomposes trajectory correctness as S(t) = Π_{k=1}^{t}(1−h(k)), where h(t) = Pr(z=t|z≥t) is the conditional probability of entering a wrong state at step t given prior steps were correct. Combined with PURE's min-form credit assignment (arXiv 2504.15275), this proves the weakest step dominates solution quality, implying verification effort should concentrate on steps with highest conditional error probability.\\n\\n(5) VerifySteer (arXiv 2605.20745, May 2026) shows verification compute can be reduced 4-7x through principled intervention at ProcessBench F1 of 72.3, confirming large optimization headroom that is orthogonal to and composable with CRISP-PRM's approach.\\n\\n(6) Hard2Verify (arXiv 2510.13744) reveals catastrophic verification failure on frontier-difficulty problems (best discriminative PRM F1 drops from 78.3% to 37.3%), demonstrating that the gap between discriminative and generative verification capabilities widens with difficulty—making adaptive paradigm selection increasingly valuable precisely where it matters most.\\n\\nThe unoccupied synthesis is explicit step-level paradigm selection within a unified dual-mode verifier, grounded in the decoupling principle from modular systems research, with composable routing designed to work with modern strong base models—addressing exactly the ceiling that Dyve's entangled approach hits.\",\n  \"landscape\": \"**Discriminative PRMs.** ActPRM (arXiv 2504.10559) is the current leading discriminative PRM at the 7B scale, achieving ProcessBench avg F1 of 75.0 (ActPRM-X: 76.0) via active learning-based data-efficient training. Qwen2.5-Math-PRM-7B (arXiv 2501.07301) achieves avg F1 73.5 with F1 of 82.4/77.6/67.5/66.3 across GSM8K/MATH/OlympiadBench/OmniMATH, as reported in ProcessBench (arXiv 2412.06559, ACL 2025) and independently verified in R-PRM (arXiv 2503.21295, EMNLP 2025, Table 1). Its error detection accuracy (err acc) degrades from 72.0% (GSM8K) to 55.2% (OmniMATH), while correctness accuracy (corr acc) remains relatively stable (96.4% to 83.0%). AdaptiveStep/ASPRM (arXiv 2502.13943) proposes confidence-based step boundary detection for PRM training but does not evaluate on ProcessBench. At 72B scale, Qwen2.5-Math-PRM-72B reaches F1 78.3. Earlier PRMs include Qwen2.5-Math-7B-PRM800K (avg F1 ~41), Skywork-PRM-7B (~35). PRMBench shows discriminative PRMs achieve near-random performance on 'simplicity' error types (redundancy, circular logic). SCAN (arXiv 2509.16548, NeurIPS 2025) provides an efficient data synthesis and noise-tolerant learning framework.\\n\\n**Verification on Frontier-Difficulty Problems.** Hard2Verify (arXiv 2510.13744) provides a step-level verification benchmark on 2024-2025 Olympiad-level problems and reveals catastrophic failure of current PRMs on frontier math: Qwen2.5-Math-PRM-72B achieves only 37.3% F1 on Hard2Verify ErrorID (vs 78.3% on ProcessBench), a 41 percentage point drop. This demonstrates that ProcessBench scores do not generalize to frontier problems, and that the gap between discriminative and generative verification capabilities widens dramatically with difficulty—strengthening the case for adaptive paradigm selection.\\n\\n**Generative PRMs.** ThinkPRM (arXiv 2504.16828, ICLR 2026) scales verification compute via extended CoT thinking, achieving F1 of 87.3/85.7 on OlympiadBench/OmniMATH with ThinkPRM-14B—a ~12-15 F1 point advantage over the best discriminative PRMs on hard subsets, but at ~100-500x compute cost per step. GenPRM (arXiv 2504.00891, AAAI 2026) shows GenPRM-1.5B outperforms GPT-4o on ProcessBench via code-augmented generative verification; GenPRM-7B achieves avg F1 75.2 (Pass@1) and 80.5 (Maj@8).\\n\\n**Step-Level Adaptive Verification (Implicit Routing).** Dyve (arXiv 2502.11157, EMNLP 2025) is the most directly related prior work and the pioneer of step-level paradigm selection. It trains a single DeepSeek-R1-Distill-Qwen-14B via standard cross-entropy SFT on 117K examples to implicitly route between System 1 (single-token '+' confirmation) and System 2 (CoT analysis, up to 8192 tokens). ProcessBench F1: 68.5/58.3/49.0/47.2 (avg ~55.8). Critically, Dyve outperformed ALL contemporaneous baselines at the time of publication. However, stronger discriminative PRMs (ActPRM avg F1 75.0; Qwen2.5-Math-PRM-7B avg F1 73.5) have since surpassed Dyve's performance. This reveals a ceiling of implicit/entangled routing: (a) the routing decision is entangled with the verification itself (learned output length as proxy), preventing composition with independently improved verifiers—analogous to the routing-representation interference identified in MoE research (Grouter, arXiv 2603.06626, ICML 2026); (b) steps are scored independently with no sequential error cascade awareness; (c) standard cross-entropy SFT provides no quality floor guarantee; (d) no separable routing component enables ablation or interpretability. CRISP-PRM builds on Dyve's pioneering insight with explicit, decoupled routing designed to work with stronger base models.\\n\\n**Modular and Decoupled Systems Theory.** Grouter (arXiv 2603.06626, ICML 2026) demonstrates that decoupling routing topology from expert representation in MoE eliminates mutual optimization interference, boosting data utilization by 4.28x and throughput by 33.5%. StableMoE (arXiv 2204.08396, ACL 2022) identifies 'routing fluctuation' as a pathology of entangled routing-representation training and solves it by distilling a decoupled router. D'Amour et al. ('Fixes That Fail,' arXiv 2103.11766, NeurIPS 2021) formally show that in composed ML systems, improving one component can degrade downstream performance unless interfaces are decoupled—establishing independent improvability as requiring architectural separation. Select-then-Solve (arXiv 2604.06753, Apr 2026) demonstrates that no single inference paradigm dominates across tasks; oracle per-task paradigm selection beats the best fixed paradigm by 17.1pp, with a lightweight router recovering up to 37% of the oracle gap. These results collectively provide theoretical grounding for CRISP-PRM's core design principle: decoupling verification paradigm selection from verification execution.\\n\\n**Step-Level Uncertainty Quantification.** CoT Entropy (Ye et al., arXiv 2502.11250, Feb 2025) introduces a novel UQ method for step-level verification in generative PRMs: it samples multiple reasoning paths at each step, groups outputs by binary correctness decisions, and computes entropy over the marginal distribution: H = −Σ_e(Σ_c p_θ(c,e|x≤t)) log(Σ_c p_θ(c,e|x≤t)). Achieves AUROC 0.680, outperforming all UQ baselines (SEU-MiniLM 0.661, SEU-NV-Embed). ReProbe/UHeads (arXiv 2511.06209, ACL 2026) provides lightweight step-level uncertainty heads; combining ReProbe scores with PRM scores outperforms either alone.\\n\\n**Problem-Level Fast/Slow Routing.** F/S-RM (arXiv 2603.20212, Mar 2026) trains a single Qwen3-8B with dual fast (first-token scalar) and slow (CoT generation) modes, using dual-confidence activation to route at the problem level; achieves 20.8% token savings but never considers within-solution step variation. E-GRM (arXiv 2604.10072, ACL 2026) routes between direct inference and CoT generation via parallel-decoding consensus at the problem level; 62% latency reduction and 49% FLOP reduction on MATH. CAMEL (arXiv 2602.20670, ICML 2026) uses log-probability confidence gating for pairwise preference judging; problem-level and not PRM-specific.\\n\\n**Step-Level Generation Routing.** TRIM (arXiv 2601.10245, ICLR 2026) performs step-level routing between small and large generation models using PRM-derived uncertainty, achieving 5x cost efficiency on MATH-500; routes generators, not verification paradigms.\\n\\n**Verification Compute Optimization.** VerifySteer (arXiv 2605.20745, May 2026) identifies verifier strictness signals in hidden states at paragraph-boundary delimiter tokens and steers verification depth via selective latent interventions. Achieves ProcessBench F1 of 72.3 with Qwen3-8B at 4-7x less inference compute than self-consistency; orthogonal to and composable with fine-tuned verifiers. Adaptive Test-Time Compute (arXiv 2602.03975, Feb 2026) performs state-level selective verification combining deterministic feasibility gating with learned scoring and adaptive allocation, achieving 30% fewer verifier calls on MATH-500. Budget-aware Test-time Scaling (arXiv 2510.14913, 2025) shows discriminative verifiers + self-consistency (Pessimistic Verification) outperform generative verifiers under constrained FLOP budgets.\\n\\n**Constrained RL for Quality Guarantees.** Constrained GRPO (arXiv 2602.05863, Feb 2026) introduces a Lagrangian-based extension of GRPO for constrained policy optimization with indicator cost functions, scalarized advantage construction (preventing standard-deviation mismatch), and learned multipliers. Faithful GRPO (arXiv 2604.08476, Apr 2026) applies this to transform quality metrics from reward terms into hard constraints via Lagrangian dual ascent, reducing inconsistency from 24.5% to 1.7%.\\n\\n**Adaptive Thinking for Generators.** PATS (arXiv 2505.19250, May 2025) introduces process-level adaptive thinking mode switching for generators. Adjusts beam width per step based on PRM scores, achieving near-optimal accuracy at 55% of full-compute token usage. PATS adapts generation depth; CRISP-PRM adapts verification depth—complementary.\\n\\n**Credit Assignment and Error Propagation.** CRM (arXiv 2509.26578, 2025) frames step correctness using conditional probability chain rules: defining h(t) = Pr(z=t|z≥t) as the conditional probability of entering a wrong state at step t given all prior steps were correct, and decomposing trajectory correctness as S(t) = Π_{k=1}^{t}(1−h(k)). Step rewards derive from a potential function Φ(s_t) = log S(t), yielding per-step reward r_t = log(1−h(t)). PURE (arXiv 2504.15275, 2025) introduces min-form credit assignment proving the weakest step dominates. 'Beyond the First Error' (arXiv 2505.14391, 2025) distinguishes error propagation from error cessation.\\n\\n**PRM Calibration.** 'Know What You Don't Know' (arXiv 2506.09338, NeurIPS 2025) demonstrates PRMs are poorly calibrated, overestimating success probability—motivating multi-signal criticality estimation rather than relying on single PRM confidence scores.\\n\\n**Summary.** Dyve pioneered step-level paradigm selection and outperformed all contemporaneous baselines, demonstrating the value of adaptive verification. However, no existing system combines (a) explicit, decoupled criticality estimation grounded in the principle that verification selection and verification execution are separate concerns, (b) sequential error cascade awareness, (c) constrained training with F1 floor guarantees, and (d) demonstrated robustness to changing cost ratios between verification paradigms.\",\n  \"inspired_by\": \"Convergence of five research threads with a critical empirical insight, unified by a theoretical principle from modular systems research: (1) Dyve (EMNLP 2025) demonstrated that step-level fast/slow verification within a single model is feasible and valuable, outperforming all contemporaneous baselines. The subsequent emergence of stronger discriminative PRMs (ActPRM, avg F1 75.0) that surpass Dyve reveals that implicit/entangled routing hits a ceiling—motivating explicit, decoupled routing. (2) MoE literature (Grouter, ICML 2026; StableMoE, ACL 2022) and composed ML systems theory ('Fixes That Fail,' NeurIPS 2021) formally establish that entangled routing-computation optimization creates mutual interference and prevents independent improvability—providing theoretical grounding for why Dyve's ceiling exists and why decoupled routing is the solution. (3) F/S-RM (Mar 2026) proves a single model can support both discriminative and generative modes with dual-confidence routing → provides the architectural foundation. (4) CRM's conditional probability chain rule decomposes trajectory correctness as S(t) = Π(1−h(t)) and PURE's min-form credit assignment proves the weakest step dominates → verification effort should target steps with highest conditional error probability. (5) CoT Entropy (arXiv 2502.11250) achieves best-in-class step-level UQ for generative PRMs (AUROC 0.680) → provides validated signal for criticality estimation. (6) Constrained GRPO (arXiv 2602.05863) and Faithful GRPO (arXiv 2604.08476) provide principled frameworks for enforcing quality constraints during RL training → enables the F1 floor guarantee. Pattern: 'Dyve showed the right question (adaptive step verification). The next step requires principled decoupling of verification paradigm selection from verification execution—a design principle established in MoE research but not yet applied to PRM verification—composed with stronger base models, principled criticality estimation, and constrained training with quality guarantees.'\",\n  \"approach\": \"We propose CRISP-PRM (CRIticality-based Step-level Paradigm selection for Process Reward Models), a framework built on a unified dual-mode verifier that selects the verification paradigm—fast (discriminative) or deep (generative CoT)—for each reasoning step based on estimated step criticality, under a compute budget constraint. Building on Dyve's pioneering demonstration that step-level paradigm selection outperforms contemporaneous baselines, CRISP-PRM introduces explicit, decoupled routing designed to work with modern strong base models.\\n\\n**Theoretical Foundation: The Decoupling Principle for Verification**\\n\\nCRISP-PRM is grounded in a key insight from modular systems research: verification paradigm selection and verification execution are fundamentally different concerns that must be architecturally decoupled. In entangled systems like Dyve, the routing decision (when to use deep verification) is learned jointly with the verification itself (how to verify), through output length as an implicit proxy. This creates three well-characterized pathologies: (a) Optimization interference: gradients for improving routing conflict with gradients for improving verification, as demonstrated in MoE research where Grouter (arXiv 2603.06626, ICML 2026) showed 4.28x data efficiency gains from decoupling routing from representation. (b) Routing fluctuation: the same step may be routed differently during training vs. inference when routing is entangled with learned representations, as StableMoE (arXiv 2204.08396, ACL 2022) identified and solved via decoupled router distillation. (c) Failure of independent improvability: in composed ML systems, improving one component can degrade downstream performance unless interfaces are decoupled (D'Amour et al., arXiv 2103.11766, NeurIPS 2021). This explains why Dyve cannot benefit from stronger discriminative PRMs—the entangled routing has no separable interface through which to inject improvements. CRISP-PRM's explicit SCE provides this interface: advances in discriminative PRMs, generative PRMs, or uncertainty estimation each independently improve system performance without retraining the other components.\\n\\n**Architecture: Unified Dual-Mode PRM**\\n\\nCRISP-PRM uses a single Qwen3-8B model fine-tuned to support both verification modes, following the F/S-RM dual-mode paradigm adapted for step-level process verification:\\n\\n• Fast mode: Given (problem, solution prefix, step_i), the model's first generated token is a correctness judgment ('correct'/'incorrect'). The token probability p(correct|context) serves directly as a scalar step reward. Cost: ~10ms/step (single forward pass). No separate classification head needed—the standard LM head suffices.\\n\\n• Deep mode: A special trigger token is appended to the prompt, bypassing fast judgment and entering CoT verification. The model generates a step-by-step verification rationale inside &lt;verify>...&lt;/verify> tags, then outputs a final correctness judgment. Cost: ~100ms-2s/step depending on model size and generation length.\\n\\n**Training Pipeline: Two-Stage with Constrained RL**\\n\\nStage 1 — SFT Foundation: Combined loss L = L_step + λ·L_action, where L_step is binary cross-entropy on step labels (fast mode) combined with generation loss on synthetic verification CoTs from ThinkPRM-style data (deep mode), and L_action is an action-space constraint penalizing probability leakage to irrelevant tokens during fast mode.\\n\\nStage 2 — Constrained GRPO with F1 Floor: We adopt the Constrained GRPO framework (arXiv 2602.05863) to fine-tune the unified model with a hard F1 floor guarantee—ensuring the model never degrades below the current discriminative SOTA quality. Concrete specification:\\n\\n(a) Indicator cost function: C_F1(π) = 𝕀[F1_batch(π) < F1_threshold], where F1_threshold is set to the current discriminative SOTA F1 on a held-out ProcessBench validation split (avg F1 75.0 for ActPRM-class models; we use the best available discriminative PRM at training time).\\n\\n(b) Lagrangian objective: ℒ(π,λ) = J_R(π) − λ·(J_C(π) − d̃), where J_R is the primary reward (format correctness + outcome accuracy for both fast and deep modes), J_C is the constraint violation rate, and d̃ is the target violation rate (0.05 = at most 5% of validation batches may fall below F1_threshold).\\n\\n(c) Scalarized advantage construction (NOT scalarized rewards, following arXiv 2602.05863 Theorem 4.1 to prevent standard-deviation mismatch): A_ScAdv = λ_R·Z_R − λ_C·Z_C, where Z_j = (Component_j − mean(Component_j))/std(Component_j) are per-component standardized advantages. This preserves the intended trade-off between reward maximization and constraint satisfaction.\\n\\n(d) Multiplier update: ∇_λ ℒ = −(J_C(π) − d̃), applied via gradient descent with projection λ ≥ 0. When F1 drops below threshold (J_C > d̃), the gradient is positive, increasing λ and strengthening the constraint penalty.\\n\\n(e) Conservative checkpoint selection as fallback: evaluate F1 on validation set per epoch; only accept parameter updates that maintain F1 above threshold. This provides a hard guarantee even if the Lagrangian balance oscillates during training.\\n\\nThis follows the precedent of Faithful GRPO (arXiv 2604.08476), which demonstrated that transforming quality metrics from reward terms into hard constraints via Lagrangian dual ascent reduces quality degradation from 24.5% to 1.7%.\\n\\n**Step Criticality Estimator (SCE)**\\n\\nA lightweight module (<1M params) that scores each step's need for deep verification using multiple complementary signals. Unlike Dyve's implicit routing (where the model learns to self-regulate output length through SFT, with no separable routing component), the SCE is an explicit, interpretable, and ablatable module—the architectural embodiment of the decoupling principle.\\n\\nThe SCE combines:\\n1. Fast-mode intuition confidence: C_I = |p(correct) − p(incorrect)| from the fast verification pass (available as a byproduct)\\n2. Fast-mode token confidence: C_T = mean negative log-probability of irrelevant tokens, measuring probability mass leakage beyond the binary judgment (from F/S-RM's dual-confidence mechanism)\\n3. CoT Entropy signal: Following Ye et al. (arXiv 2502.11250), when running complementary analysis, sample multiple reasoning paths at each step and compute entropy over the marginal distribution of binary decision outcomes: H = −Σ_e(Σ_c p_θ(c,e|x≤t)) log(Σ_c p_θ(c,e|x≤t)). Steps with high CoT Entropy indicate verifier uncertainty requiring deeper analysis. Optional when compute-constrained.\\n4. Generator internal uncertainty: entropy of the generating model's hidden states via ReProbe-style probes (<10M params on frozen generator), when generator internals are available. Optional for black-box generator settings.\\n5. Structural features: step position in chain, relative token length, domain signal. Justified by CoLD (arXiv 2507.15698) showing PRMs have strong length bias.\\n\\nThe SCE is an MLP that outputs a criticality score c_i ∈ [0,1] for each step. Training signal derives from oracle construction: run both fast and deep modes on training steps, identify 'value-add' steps where fast mode misclassifies but deep mode succeeds, and train SCE via binary cross-entropy. We include a planned ablation ladder: (i) fast-mode confidence only → (ii) dual-confidence (C_I + C_T) → (iii) +CoT Entropy → (iv) +ReProbe → (v) +structural features.\\n\\n**Budget-Constrained Router**\\n\\nGiven a per-solution compute budget B (fraction of steps receiving deep verification), the router:\\n1. Runs fast verification on ALL K steps (cheap baseline, ~60ms for 6 steps). This simultaneously produces scalar scores and SCE input signals.\\n2. Computes criticality scores c_i for all steps.\\n3. Selects the top-⌈B·K⌉ highest-criticality steps for deep verification.\\n4. Final step scores combine fast and deep assessments: steps receiving only fast verification use the fast scalar score; steps receiving deep verification use the deep judgment.\\n\\nThe budget B is a tunable hyperparameter that parameterizes the cost-accuracy Pareto frontier: at B=0, all steps use fast verification (cheapest); at B=1, all steps use deep verification (most accurate). The SCE threshold mapping to a given B is calibrated from the empirical criticality score distribution on a calibration set. Critically, the cost ratio between paradigms enters ONLY through B—as generative costs decrease, B can be increased to allocate more deep verification at the same total cost.\\n\\n**Sequential Error Cascade (SEC) Enhancement (Optional)**\\n\\nFor applications where step ordering matters, we add a sequential processing mode grounded in CRM's conditional probability chain rule (arXiv 2509.26578), which decomposes trajectory correctness as S(t) = Π_{k=1}^{t}(1−h(k)) where h(t) is the conditional probability of entering a wrong state at step t given prior steps were correct, and PURE's min-form insight:\\n- If deep verification detects an ERROR at step i: automatically flag all subsequent steps for deep verification or assign minimum scores (since they are built on faulty premises, and S(T) ≤ S(i) per the multiplicative decomposition).\\n- If deep verification CONFIRMS correctness: update posterior criticality of subsequent steps, potentially lowering priority for dependent downstream steps.\\nThis is an optional enhancement that provides marginal accuracy gains on top of the core budget-constrained routing.\\n\\n**Robustness to Cheaper Generative Verification**\\n\\nCRISP-PRM's value proposition is robust to future reductions in generative verification cost, for six reasons: (a) Even a 10x speedup in generative models leaves a 10-50x cost gap (100-500ms vs 10ms per step)—routing still provides substantial efficiency gains. (b) The SCE provides accuracy gains independent of cost: by identifying which steps most benefit from deeper analysis, routing improves verification allocation quality regardless of per-mode costs. Even at equal costs, selectively applying deep verification to high-criticality steps outperforms uniform application because the model's deep mode may still outperform its fast mode on specific error types (e.g., soundness errors, multi-step logical chains). (c) CRISP-PRM's routing is parameterizable—the cost ratio enters only through the budget constraint B and SCE threshold, both tunable hyperparameters. As costs converge, B increases to allocate more deep verification while maintaining cost parity with uniform fast. (d) In the limit where generative cost equals discriminative cost, CRISP-PRM degenerates to uniform deep verification, which is the accuracy-optimal baseline—the framework gracefully adapts rather than becoming irrelevant. (e) Historical analog: TRIM (arXiv 2601.10245) shows step-level routing between models of different sizes remains valuable even as smaller models improve, because the relative cost gap persists across model generations. (f) GenPRM-1.5B still requires multiple forward passes for CoT generation—the cost gap is fundamental (single-token vs multi-token generation) rather than purely model-size dependent.\\n\\n**Difficulty-Stratified Efficiency Analysis**\\n\\nUsing ProcessBench data (arXiv 2412.06559, ACL 2025; verified in R-PRM, arXiv 2503.21295, EMNLP 2025, Table 1) for Qwen2.5-Math-PRM-7B: err accuracy of 72.0%/68.0%/55.7%/55.2% and corr accuracy of 96.4%/90.4%/85.5%/83.0% across GSM8K/MATH/OlympiadBench/OmniMATH. Hard2Verify (arXiv 2510.13744) further shows that on frontier-difficulty problems, the best discriminative PRM collapses to F1 37.3—indicating the fraction of steps requiring deep verification scales superlinearly with difficulty:\\n\\n• Easy tier (GSM8K-level): Fast verification reliable on ~85-90% of steps. Deep needed on ~10-15%. Expected latency reduction vs uniform deep: ~87%.\\n• Medium tier (MATH-level): Fast verification reliable on ~80-85% of steps. Deep needed on ~15-20%. Expected reduction: ~82%.\\n• Hard tier (OlympiadBench-level): Fast verification reliable on ~70-80% of steps. Deep needed on ~20-30%. Expected reduction: ~75%.\\n• Hardest tier (OmniMATH-level): Fast verification reliable on ~65-75% of steps. Deep needed on ~25-35%. Expected reduction: ~70%.\\n• Frontier tier (Hard2Verify-level): Fast verification reliable on ~40-60% of steps. Deep needed on ~40-60%. Expected reduction: ~50%. CRISP-PRM's relative accuracy gain is maximized here.\\n\\nCRISP-PRM's value proposition is difficulty-adaptive: on easy problems, it saves the most compute; on hard and frontier problems, it provides the largest accuracy gains.\\n\\n**Evaluation Protocol**\\n\\n• Step-level accuracy: F1 on ProcessBench (GSM8K/MATH/OlympiadBench/OmniMATH subsets reported separately, with err/corr accuracy breakdown) and PRMBench (fine-grained error type breakdown). If accessible, Hard2Verify ErrorID evaluation to test frontier generalization.\\n• Solution-level utility: Best-of-N reranking accuracy on MATH-500, AIME'24, GPQA-Diamond\\n• Efficiency: FLOPs per solution, accuracy-per-FLOP Pareto frontiers at multiple budget levels B ∈ {0.05, 0.1, 0.2, 0.3, 0.5, 1.0}\\n• Baselines: (i) uniform fast PRM (ActPRM, avg F1 75.0; and Qwen2.5-Math-PRM-7B, avg F1 73.5), (ii) uniform deep PRM (ThinkPRM-14B), (iii) Dyve (implicit step-level routing, avg F1 ~55.8)—HISTORICAL BASELINE showing progress from Dyve's pioneering work, (iv) problem-level routing (F/S-RM-style dual-confidence gating), (v) VerifySteer (latent steering, F1 72.3), (vi) Budget-aware Pessimistic Verification, (vii) random step selection for deep verification (ablation control), (viii) PRM-confidence-only routing (single-signal ablation)\\n• Ablation studies: (A1) Explicit SCE routing vs. Dyve-style implicit SFT routing on SAME base model—isolating the value of decoupled routing (tests the decoupling principle directly); (A2) SCE signal ablation ladder (confidence-only → dual-confidence → +CoT Entropy → +ReProbe → +structural)—quantifying marginal signal contribution; (A3) Constrained GRPO (with F1 floor) vs. standard SFT for unified model training—testing whether Constrained GRPO prevents quality degradation; (A4) SEC-aware vs. independent greedy allocation—measuring value of sequential error cascade awareness; (A5) Budget sensitivity analysis across B ∈ {0.05, 0.1, 0.2, 0.3, 0.5}; (A6) Difficulty-stratified analysis showing per-tier routing rates and gains, including Hard2Verify-level problems if available\\n• Complementarity analysis: CRISP-PRM + VerifySteer (explicit routing + latent strictness steering); CRISP-PRM + PATS (verification routing + generation routing)\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"350 A100-80GB hours (80h unified model training (SFT + Constrained GRPO), 100h oracle construction running both modes on ~120K steps, 20h SCE/router training, 80h evaluation across 4 benchmarks × multiple budgets × 8 baselines including Dyve, 50h ablations (A1-A6), 10h ReProbe probe training, 10h VerifySteer comparison)\",\n      \"timeline\": \"10-14 weeks (single researcher)\",\n      \"estimated_gpu_cost\": \"$700 (at ~$2/hr A100-80GB cloud)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"280 A100-80GB hours (fewer dead-end experiments via Claude-guided threshold tuning and ablation prioritization)\",\n      \"timeline\": \"7-10 weeks\",\n      \"claude_api_cost\": \"$200-400 (experiment design, analysis scripts, paper writing assistance)\",\n      \"estimated_gpu_cost\": \"$560\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"480 A100-80GB hours (broader ablations: multiple SCE architectures, threshold sensitivity, cross-domain transfer, additional benchmarks including Hard2Verify, difficulty-stratified analysis, Dyve reproduction for fair comparison)\",\n      \"timeline\": \"4-6 weeks\",\n      \"claude_api_cost\": \"$400-700 (end-to-end experiment orchestration, code generation, result analysis)\",\n      \"estimated_gpu_cost\": \"$960\",\n      \"speed_bottleneck\": \"Unified model training is the main bottleneck (~80h); oracle construction is embarrassingly parallel—with 4×A100, drops from ~50h to ~13h wall-clock.\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (full papers Jul 28 2026, supplementary Jul 31 2026 — confirmed via official CFP)\",\n    \"ARR August 2026 cycle (Aug 3 2026, for commitment to NAACL 2027 or EACL 2027)\"\n  ],\n  \"level\": \"solid-to-strong\",\n  \"key_references\": [\n    \"Dyve: Thinking Fast and Slow for Dynamic Process Verification (arXiv 2502.11157, EMNLP 2025) — pioneered step-level System 1/System 2 routing; outperformed all contemporaneous baselines with avg F1 ~55.8; since surpassed by stronger discriminative PRMs\",\n    \"Process Reward Models That Think (ThinkPRM, arXiv 2504.16828, ICLR 2026)\",\n    \"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Model Parameters (ICLR 2025)\",\n    \"Fast-Slow Thinking RM: Efficient Integration of Scalar and Generative Reward Models (F/S-RM, arXiv 2603.20212, Mar 2026)\",\n    \"Reason Only When Needed: Efficient Generative Reward Modeling via Model-Internal Uncertainty (E-GRM, arXiv 2604.10072, ACL 2026)\",\n    \"CAMEL: Confidence-Gated Reflection for Reward Modeling (arXiv 2602.20670, ICML 2026)\",\n    \"TRIM: Hybrid Inference via Targeted Stepwise Routing in Multi-Step Reasoning Tasks (arXiv 2601.10245, ICLR 2026)\",\n    \"The Hidden Signal of Verifier Strictness: Controlling and Improving Step-Wise Verification via Selective Latent Steering (VerifySteer, arXiv 2605.20745, May 2026)\",\n    \"Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure (arXiv 2602.03975, Feb 2026)\",\n    \"PATS: Process-Level Adaptive Thinking Mode Switching (arXiv 2505.19250, May 2025)\",\n    \"Efficient Test-Time Scaling of Multi-Step Reasoning by Probing Internal States of Large Language Models (ReProbe/UHeads, arXiv 2511.06209, ACL 2026)\",\n    \"Stop Summation: Min-Form Credit Assignment Is All Process Reward Models Need (PURE, arXiv 2504.15275, 2025)\",\n    \"Conditional Reward Models for Process-Level Credit Assignment (CRM, arXiv 2509.26578, 2025) — uses conditional probability chain rules to decompose trajectory correctness as S(t) = Π(1−h(t)), where h(t) = Pr(z=t|z≥t) is the conditional error probability at step t\",\n    \"Beyond the First Error: Modeling Error Propagation and Cessation in Multi-Step Reasoning (arXiv 2505.14391, 2025)\",\n    \"Know What You Don't Know: Calibration of Process Reward Models (arXiv 2506.09338, NeurIPS 2025)\",\n    \"ProcessBench: Identifying Process Errors in Mathematical Reasoning (arXiv 2412.06559, ACL 2025)\",\n    \"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (arXiv 2501.03124, 2025)\",\n    \"When to Trust the Cheap Check: Weak and Strong Verification for Reasoning (arXiv 2602.17633, Feb 2026)\",\n    \"Budget-aware Test-time Scaling via Discriminative Verification (arXiv 2510.14913, 2025)\",\n    \"When To Solve, When To Verify: Compute-Optimal Problem Solving and Verification (arXiv 2504.01005, 2025)\",\n    \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (arXiv 2504.00891, AAAI 2026)\",\n    \"SCAN: Self-Denoising Monte Carlo Annotation for Robust Process Reward Learning (arXiv 2509.16548, NeurIPS 2025)\",\n    \"R-PRM: Reasoning-Driven Process Reward Modeling (arXiv 2503.21295, EMNLP 2025) — Table 1 provides independently verified ProcessBench numbers for Qwen2.5-Math-PRM-7B\",\n    \"The Lessons of Developing Process Reward Models in Mathematical Reasoning (arXiv 2501.07301, 2025) — Qwen2.5-Math-PRM development and evaluation\",\n    \"Uncertainty-Aware Step-wise Verification with Generative Reward Models (Ye et al., arXiv 2502.11250, Feb 2025) — CoT Entropy for step-level UQ in generative PRMs; AUROC 0.680\",\n    \"Constrained Group Relative Policy Optimization (arXiv 2602.05863, Feb 2026) — Lagrangian-based constrained GRPO with scalarized advantage construction; foundation for F1 floor mechanism\",\n    \"Faithful GRPO: Improving Visual Spatial Reasoning via Constrained Policy Optimization (arXiv 2604.08476, Apr 2026) — precedent for transforming quality metrics into hard constraints via Lagrangian dual ascent\",\n    \"Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling (VG-Search, arXiv 2505.11730, NeurIPS 2025)\",\n    \"CoLD: Mitigating Length Bias in Process Reward Models (arXiv 2507.15698, 2025)\",\n    \"SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation (arXiv 2604.06636, Apr 2026)\",\n    \"SPAE: Step Potential Advantage Estimation for Credit Assignment (arXiv 2601.03823, Jan 2026)\",\n    \"Efficient Process Reward Model Training via Active Learning (ActPRM, arXiv 2504.10559, 2025) — current discriminative PRM SOTA on ProcessBench at 7B scale, avg F1 75.0 (ActPRM-X: 76.0)\",\n    \"Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math (arXiv 2510.13744, 2025) — reveals catastrophic failure of discriminative PRMs on frontier problems (F1 78.3 → 37.3)\",\n    \"Grouter: Decoupling Routing from Representation (arXiv 2603.06626, ICML 2026) — demonstrates 4.28x data efficiency from decoupling routing topology in MoE; theoretical foundation for the decoupling principle\",\n    \"StableMoE: Stable Routing Strategy for Mixture of Experts (arXiv 2204.08396, ACL 2022) — identifies routing fluctuation as a pathology of entangled routing-representation training\",\n    \"Underspecification Presents Challenges for Credibility in Modern Machine Learning (D'Amour et al., arXiv 2011.03395, NeurIPS 2021) — formalizes how improving one component in composed systems can degrade others without decoupled interfaces\",\n    \"Select-then-Solve: Paradigm Routing as Inference-Time Optimization for LLM Agents (arXiv 2604.06753, Apr 2026) — shows oracle paradigm selection beats best fixed paradigm by 17.1pp; validates learned paradigm routing\",\n    \"AdaptiveStep: Automatically Dividing Reasoning Step through Model Confidence (ASPRM, arXiv 2502.13943, Feb 2025) — confidence-based step boundary detection for PRM training\"\n  ],\n  \"description\": \"We propose CRISP-PRM (CRIticality-based Step-level Paradigm selection for Process Reward Models), a framework built on a unified dual-mode verifier that routes each reasoning step to the optimal verification paradigm—fast discriminative scoring or deep generative CoT verification—based on explicit step criticality estimation and a tunable compute budget. Building on Dyve's (EMNLP 2025) pioneering demonstration that step-level paradigm selection outperforms contemporaneous baselines, CRISP-PRM introduces a principled advance grounded in the decoupling principle from modular systems research: verification paradigm selection and verification execution are fundamentally different concerns that must be architecturally separated to enable independent improvement of each component. Three concrete innovations implement this principle: (1) An explicit Step Criticality Estimator (SCE) combining dual-confidence signals from fast verification, CoT Entropy-based uncertainty (Ye et al., arXiv 2502.11250, AUROC 0.680), generator-internal uncertainty (ReProbe-style probes), and structural features—with an ablation ladder quantifying each component's marginal value. Unlike Dyve's entangled routing (where routing and verification are jointly optimized, creating the routing-representation interference characterized by Grouter, arXiv 2603.06626, ICML 2026), the SCE is a separable module that enables each verification paradigm to be independently upgraded. (2) A budget-constrained router that parameterizes the cost-accuracy Pareto frontier through a single hyperparameter B (fraction of steps receiving deep verification), enabling graceful adaptation to changing cost ratios: as generative verification becomes cheaper, B increases; in the limit of equal costs, the system degenerates to uniform deep verification. (3) Constrained GRPO fine-tuning (following arXiv 2602.05863) with a hard F1 floor guarantee via indicator cost functions, Lagrangian dual ascent with scalarized advantage construction, and conservative checkpoint selection—ensuring the unified model never degrades below discriminative SOTA quality (ActPRM avg F1 75.0, arXiv 2504.10559). Using ProcessBench data (arXiv 2412.06559, ACL 2025; verified in R-PRM, arXiv 2503.21295, Table 1) and Hard2Verify findings (arXiv 2510.13744, best discriminative PRM F1 collapses from 78.3% to 37.3% on frontier problems), we estimate ~10-15% of easy-tier steps and ~25-35% of hard-tier steps benefit from deep verification, yielding 70-87% latency reduction vs. uniform deep verification while targeting Pareto dominance over both uniform paradigms and problem-level routing approaches. The increasing verification gap at frontier difficulty levels (Hard2Verify) makes adaptive paradigm selection most valuable precisely where it matters most.\",\n  \"project_name\": \"crisp_step_prm\",\n  \"source\": \"web_research\",\n  \"reviewer_response\": {\n    \"CRM_MISCHARACTERIZATION\": \"Resolved. The fabricated 'survival analysis' and 'hazard function' terminology attributed to CRM has been removed throughout all sections. CRM is now accurately characterized using its own framing: conditional probability chain rules, where h(t) = Pr(z=t|z≥t) is the conditional probability of entering a wrong state at step t given prior steps were correct, with trajectory correctness decomposed as S(t) = Π_{k=1}^{t}(1−h(k)). This multiplicative decomposition IS in the CRM paper (it is the core equation), but CRM frames it as conditional probability modeling, not survival analysis. The mathematical form is retained because it is accurate and supports the SEC module's theoretical grounding. Corrections applied in: core_problem, opportunity, landscape, inspired_by, approach (SEC module), key_references, and description.\",\n    \"OUTDATED_DISCRIMINATIVE_SOTA\": \"Resolved. ActPRM (arXiv 2504.10559) is now cited as the current discriminative PRM SOTA at 7B scale with avg F1 75.0 (ActPRM-X: 76.0), surpassing Qwen2.5-Math-PRM-7B (73.5). The F1 floor threshold has been updated to 75.0 (matching ActPRM). The reviewer's cited arXiv ID (2601.22249) could not be verified; the correct ActPRM ID is 2504.10559, confirmed through direct paper access showing ProcessBench scores in Table 1. ASPRM (arXiv 2502.13943) is added to the landscape with the accurate note that it does NOT evaluate on ProcessBench—it evaluates on Best-of-N metrics for GSM8K/MATH/code tasks. Hard2Verify (arXiv 2510.13744) is now integrated throughout: Qwen2.5-Math-PRM-72B F1 drops from 78.3% on ProcessBench to 37.3% on frontier-difficulty ErrorID, a 41pp collapse that STRENGTHENS the case for adaptive paradigm selection. A new 'Frontier tier' is added to the difficulty-stratified analysis. Updates applied in: core_problem, opportunity, landscape (new subsection), approach (F1 threshold, difficulty analysis, evaluation), key_references, and description.\",\n    \"UNVERIFIABLE_VENUE_CLAIMS\": \"Resolved via independent verification of all venue claims. GenPRM AAAI 2026 — VERIFIED (GitHub repo announcement 2025-11-08, proceedings at aaai.org). E-GRM ACL 2026 — VERIFIED (arXiv Comments field states 'accepted by ACL 2026'). CAMEL ICML 2026 — VERIFIED (arXiv Comments field and ICML 2026 Downloads page listing poster). SCAN NeurIPS 2025 — VERIFIED (NeurIPS 2025 virtual poster page). Dyve EMNLP 2025 — VERIFIED (ACL Anthology). ProcessBench ACL 2025 — VERIFIED (ACL Anthology). R-PRM EMNLP 2025 — VERIFIED (ACL Anthology). ONE CORRECTION MADE: ReProbe/UHeads was incorrectly labeled 'NeurIPS 2025' — it is actually ACL 2026 Main, as confirmed by arXiv Comments field and project page at reprobe.github.io. This error has been corrected in all references. ThinkPRM venue added as ICLR 2026 based on verification.\",\n    \"NOVELTY_CEILING\": \"Addressed via explicit articulation of the 'Decoupling Principle for Verification' as the core scientific insight, elevated from engineering synthesis to a principled contribution backed by three independent theoretical foundations: (1) Grouter (arXiv 2603.06626, ICML 2026): decoupling routing from representation in MoE eliminates optimization interference, yielding 4.28x data efficiency — directly analogous to decoupling verification selection from execution. (2) StableMoE (arXiv 2204.08396, ACL 2022): entangled routing creates 'routing fluctuation' where the same input updates different experts during training but only one is used at inference — explaining why Dyve's implicit routing underperforms. (3) D'Amour et al. (arXiv 2011.03395, NeurIPS 2021): 'Fixes That Fail' formally establishes that independent improvability in composed ML systems requires decoupled interfaces. Additionally, Select-then-Solve (arXiv 2604.06753) empirically validates that learned paradigm routing recovers significant oracle gaps (37% of 17.1pp). The contribution is reframed: not 'we combined four techniques' but 'we demonstrate that verification paradigm selection and execution must be decoupled to enable independent improvement — a principle established in MoE research but not yet applied to PRM verification — and provide the first architecture implementing this principle.' A new 'Theoretical Foundation' section in the approach articulates this formally, and ablation A1 (explicit vs implicit routing on same base model) directly tests this principle empirically.\",\n    \"MISLEADING_DYVE_FRAMING\": \"Previously resolved (round 5). Maintained accurate historical characterization.\",\n    \"GRPO_F1_FLOOR_MECHANISM_UNSPECIFIED\": \"Previously resolved (round 5). F1 threshold updated to 75.0 (ActPRM SOTA).\",\n    \"MISSING_CITATION_COT_ENTROPY\": \"Previously resolved (round 5). Maintained.\",\n    \"UNVERIFIABLE_SCAN_TABLE_2_NUMBERS\": \"Previously resolved (round 5). Maintained proper source chain.\",\n    \"IMPACT_VULNERABILITY\": \"Previously resolved (round 5). Strengthened by Hard2Verify evidence showing discriminative-generative gap widens at frontier difficulty.\",\n    \"MISSING_CITATION_ADAPTIVE_TTC\": \"Previously resolved (round 3). Maintained.\",\n    \"MISSING_CITATION_PATS\": \"Previously resolved (round 3). Maintained.\",\n    \"MISSING_CITATION_VERIFYSTEER\": \"Previously resolved (round 3). Maintained.\",\n    \"FACTUAL_ERROR_ERR_ACCURACY\": \"Previously resolved (round 3). Maintained.\",\n    \"TWO_MODEL_MEMORY_OVERHEAD\": \"Previously resolved (round 2). Maintained.\",\n    \"STEP_DEPENDENCY_IGNORED\": \"Previously resolved (round 2). SEC now correctly cites CRM's conditional probability chain rule.\",\n    \"SCE_SIGNAL_REDUNDANCY\": \"Previously resolved (round 2). Maintained.\",\n    \"BUDGET_AWARE_TTS_OVERLAP\": \"Previously resolved (round 2). Maintained.\",\n    \"CRITICAL_NOVELTY_F_S_RM\": \"Previously resolved (rounds 1-2). Maintained.\",\n    \"CRITICAL_NOVELTY_E_GRM\": \"Previously resolved (rounds 1-2). Maintained.\",\n    \"CRITICAL_NOVELTY_CAMEL\": \"Previously resolved (rounds 1-2). Maintained.\"\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26dded15-2bd2-4de4-ab5b-b6b98ddae028",
  "isSidechain": false,
  "requestId": "req_011CbU8mPmMCS29FBDPSwr9i",
  "type": "assistant",
  "uuid": "ada965fd-9167-4ecc-892b-9ae45051cd64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Q5dDsrncjaNfVYWn3ea9y",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 23197,
      "cache_read_input_tokens": 32538,
      "output_tokens": 14093,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 23197,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14093,
          "cache_read_input_tokens": 32538,
          "cache_creation_input_tokens": 23197,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 23197
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

_source line 33 · 2026-05-28T02:01:11.544Z_

<details><summary>↩ Tool result · reported error · `toolu_018kdDzAou8Pqghvk4Z1zeUY`</summary>

```text
Claude requested permissions to write to /tmp/crisp_prm_r6.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ada965fd-9167-4ecc-892b-9ae45051cd64",
  "isSidechain": false,
  "promptId": "a14d4547-e473-4da0-836a-c0e4d22dabcc",
  "type": "user",
  "uuid": "d22e57ec-24d9-4d1a-86a6-c47411cd7242",
  "toolUseResult": "Error: Claude requested permissions to write to /tmp/crisp_prm_r6.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "ada965fd-9167-4ecc-892b-9ae45051cd64",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34 · 2026-05-28T02:01:11.614Z_

```json
{
  "parentUuid": "d22e57ec-24d9-4d1a-86a6-c47411cd7242",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "70dbad30-ee04-4ce9-8e91-7227b509d13d",
  "timestamp": "2026-05-28T02:01:11.614Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"CRISP-PRM: Criticality-Aware Step-Level Paradigm Selection for Unified…",
  "leafUuid": "70dbad30-ee04-4ce9-8e91-7227b509d13d",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising CRISP-PRM after round 5 reviewer feedback",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff"
}
```

---

### Assistant

_source line 37 · 2026-05-28T02:01:17.060Z_

<details><summary>Logged reasoning block</summary>

```text
The user hasn't granted file write permission. Let me just output the JSON directly in my response instead.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70dbad30-ee04-4ce9-8e91-7227b509d13d",
  "isSidechain": false,
  "requestId": "req_011CbU9CnFeUv9cm9D18Jeux",
  "type": "assistant",
  "uuid": "2d884d84-069e-42fc-93d4-8b232a49e810",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MkiC8wxGoXxVhVTEcB88Yq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14239,
      "cache_read_input_tokens": 55735,
      "output_tokens": 14597,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14239,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14597,
          "cache_read_input_tokens": 55735,
          "cache_creation_input_tokens": 14239,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14239
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

_source line 38 · 2026-05-28T02:07:05.050Z_

Here is the complete revised proposal as a JSON object, addressing all four reviewer issues with deep research backing:

---

**Summary of changes (change_type: minor):**

1. **CRM MISCHARACTERIZATION — Fixed**: Research revealed the reviewer was *partially* wrong — CRM **does** use S(t) = Π(1−h(k)) as its core equation, but frames it as "conditional probability chain rules," never "survival analysis" or "hazard functions." All survival analysis terminology removed; CRM's own framing preserved with accurate mathematical content.

2. **OUTDATED DISCRIMINATIVE SOTA — Updated**: ActPRM (arXiv **2504.10559**, not reviewer's 2601.22249 which doesn't exist) confirmed at avg F1 75.0 (ActPRM-X: 76.0). ASPRM confirmed as **not evaluating on ProcessBench at all**. F1 floor threshold updated to 75.0. Hard2Verify (arXiv 2510.13744) integrated: best discriminative PRM F1 collapses 78.3% → 37.3% on frontier problems, *strengthening* the case for adaptive verification.

3. **VENUE CLAIMS — Verified/Corrected**: 7/8 verified. **ReProbe/UHeads corrected from "NeurIPS 2025" to "ACL 2026 Main"** (confirmed via arXiv annotations and project page). ThinkPRM venue added as ICLR 2026.

4. **NOVELTY — Elevated**: New "Theoretical Foundation: The Decoupling Principle for Verification" section grounded in Grouter (ICML 2026, 4.28x efficiency from decoupled routing), StableMoE (ACL 2022, routing fluctuation pathology), and "Fixes That Fail" (NeurIPS 2021, independent improvability requires decoupled interfaces). Contribution reframed from synthesis to a principled demonstration that verification paradigm selection and execution must be architecturally separated.

---

```json
{
  "change_type": "minor",
  "title": "CRISP-PRM: Criticality-Aware Step-Level Paradigm Selection for Unified Process Reward Models",
  "core_problem": "Process reward models face a fundamental accuracy-cost trade-off at the step level: discriminative (fast scalar) verification is cheap (~10ms/step) but unreliable on hard reasoning steps, while generative (CoT) verification is far more accurate but ~100-500x more expensive (~1-5s/step). Dyve (arXiv 2502.11157, EMNLP 2025) demonstrated the feasibility and value of step-level fast/slow paradigm selection within a single model using implicit SFT-based routing, outperforming all contemporaneous baselines (Qwen2.5-Math-7B-PRM800K avg F1 ~41, Skywork-PRM-7B ~35, GPT-4o ~52) with avg F1 ~55.8. However, stronger discriminative PRMs trained with improved data pipelines—notably ActPRM (avg F1 75.0 on ProcessBench, arXiv 2504.10559) and Qwen2.5-Math-PRM-7B (avg F1 73.5, per R-PRM Table 1)—have since surpassed Dyve's adaptive performance using pure discriminative verification. This reveals that implicit SFT-based routing has a ceiling: when the routing mechanism is entangled with the verification itself (learned output length as a proxy for routing), the system cannot benefit from independently improving either the discriminative or generative verification mode. This entanglement mirrors the routing-representation interference identified in MoE research (Grouter, arXiv 2603.06626, ICML 2026; StableMoE, arXiv 2204.08396, ACL 2022), where joint optimization of routing and computation degrades both. Problem-level routing methods (F/S-RM, E-GRM, CAMEL) achieve efficiency gains but apply uniform verification to every step within a solution, ignoring that steps vary dramatically in difficulty and criticality. ProcessBench data confirms this variation: discriminative PRM error detection accuracy degrades from 72.0% (GSM8K) to 55.2% (OmniMATH) (ProcessBench, arXiv 2412.06559, ACL 2025; also R-PRM, arXiv 2503.21295, EMNLP 2025, Table 1). Moreover, Hard2Verify (arXiv 2510.13744) reveals that even the best discriminative PRM (Qwen2.5-Math-PRM-72B, F1 78.3 on ProcessBench) collapses to F1 37.3 on frontier-difficulty problems—demonstrating that the need for selective deep verification intensifies as problem difficulty increases. Can a unified dual-mode PRM with explicit, composable step-level paradigm selection—grounded in a principled decoupling of verification paradigm selection from verification execution—produce better accuracy-per-FLOP Pareto frontiers than both uniform paradigms, problem-level routing, and Dyve's implicit step-level routing, while enabling independent improvement of each component?",
  "opportunity": "Four converging developments, plus a theoretical insight from modular systems research, create a clear opportunity for explicit criticality-based paradigm routing:\n\n(1) The maturation of both verification paradigms to strong individual performance. Discriminative PRMs have advanced substantially through improved training pipelines: ActPRM (arXiv 2504.10559) achieves avg F1 75.0 on ProcessBench (ActPRM-X reaches 76.0), surpassing Qwen2.5-Math-PRM-7B (avg F1 73.5, arXiv 2501.07301). Generative PRMs via CoT verification (ThinkPRM, arXiv 2504.16828, ICLR 2026; GenPRM, arXiv 2504.00891, AAAI 2026) achieve F1 of 87.3/85.7 on hard subsets—a ~12-15 F1 point advantage over the best discriminative PRMs. This means a router can now select between two genuinely strong modes.\n\n(2) Dyve demonstrated that step-level paradigm selection is technically feasible and valuable—outperforming all contemporaneous baselines. But its implicit SFT routing conflates when to switch with how to verify, preventing composition with stronger base models. The gap between Dyve (avg F1 55.8) and modern discriminative PRMs (avg F1 75.0) reveals that the bottleneck is the entangled routing mechanism, not the adaptive concept. This mirrors the routing-representation interference characterized in MoE literature: Grouter (arXiv 2603.06626, ICML 2026) demonstrated that decoupling routing from representation yields 4.28x data efficiency improvement by eliminating mutual gradient interference; StableMoE (arXiv 2204.08396, ACL 2022) showed that entangled routing creates 'routing fluctuation' that harms sample efficiency. CRISP-PRM's explicit routing via a lightweight criticality estimator (SCE) is model-agnostic and immediately benefits from advances in either paradigm—satisfying the 'independent improvability' criterion formalized by D'Amour et al. (arXiv 2011.03395, NeurIPS 2021).\n\n(3) Recent work on step-level uncertainty quantification provides validated signals for criticality estimation: CoT Entropy (Ye et al., arXiv 2502.11250) achieves AUROC 0.680 as the best UQ method for generative PRMs; ReProbe/UHeads (arXiv 2511.06209, ACL 2026) provides lightweight step-level uncertainty heads where combining ReProbe scores with PRM scores outperforms either alone; F/S-RM's dual-confidence mechanism (arXiv 2603.20212) demonstrates that multi-signal routing outperforms single-signal. Additionally, Constrained GRPO (arXiv 2602.05863) and Faithful GRPO (arXiv 2604.08476) provide principled frameworks for training with hard quality constraints, enabling the F1 floor guarantee that prevents quality degradation during RL fine-tuning.\n\n(4) CRM's conditional probability chain rule (arXiv 2509.26578) decomposes trajectory correctness as S(t) = Π_{k=1}^{t}(1−h(k)), where h(t) = Pr(z=t|z≥t) is the conditional probability of entering a wrong state at step t given prior steps were correct. Combined with PURE's min-form credit assignment (arXiv 2504.15275), this proves the weakest step dominates solution quality, implying verification effort should concentrate on steps with highest conditional error probability.\n\n(5) VerifySteer (arXiv 2605.20745, May 2026) shows verification compute can be reduced 4-7x through principled intervention at ProcessBench F1 of 72.3, confirming large optimization headroom that is orthogonal to and composable with CRISP-PRM's approach.\n\n(6) Hard2Verify (arXiv 2510.13744) reveals catastrophic verification failure on frontier-difficulty problems (best discriminative PRM F1 drops from 78.3% to 37.3%), demonstrating that the gap between discriminative and generative verification capabilities widens with difficulty—making adaptive paradigm selection increasingly valuable precisely where it matters most.\n\nThe unoccupied synthesis is explicit step-level paradigm selection within a unified dual-mode verifier, grounded in the decoupling principle from modular systems research, with composable routing designed to work with modern strong base models—addressing exactly the ceiling that Dyve's entangled approach hits.",
  "landscape": "**Discriminative PRMs.** ActPRM (arXiv 2504.10559) is the current leading discriminative PRM at the 7B scale, achieving ProcessBench avg F1 of 75.0 (ActPRM-X: 76.0) via active learning-based data-efficient training. Qwen2.5-Math-PRM-7B (arXiv 2501.07301) achieves avg F1 73.5 with F1 of 82.4/77.6/67.5/66.3 across GSM8K/MATH/OlympiadBench/OmniMATH, as reported in ProcessBench (arXiv 2412.06559, ACL 2025) and independently verified in R-PRM (arXiv 2503.21295, EMNLP 2025, Table 1). Its error detection accuracy (err acc) degrades from 72.0% (GSM8K) to 55.2% (OmniMATH), while correctness accuracy (corr acc) remains relatively stable (96.4% to 83.0%). AdaptiveStep/ASPRM (arXiv 2502.13943) proposes confidence-based step boundary detection for PRM training but does not evaluate on ProcessBench. At 72B scale, Qwen2.5-Math-PRM-72B reaches F1 78.3. Earlier PRMs include Qwen2.5-Math-7B-PRM800K (avg F1 ~41), Skywork-PRM-7B (~35). PRMBench shows discriminative PRMs achieve near-random performance on 'simplicity' error types (redundancy, circular logic). SCAN (arXiv 2509.16548, NeurIPS 2025) provides an efficient data synthesis and noise-tolerant learning framework.\n\n**Verification on Frontier-Difficulty Problems.** Hard2Verify (arXiv 2510.13744) provides a step-level verification benchmark on 2024-2025 Olympiad-level problems and reveals catastrophic failure of current PRMs on frontier math: Qwen2.5-Math-PRM-72B achieves only 37.3% F1 on Hard2Verify ErrorID (vs 78.3% on ProcessBench), a 41 percentage point drop. This demonstrates that ProcessBench scores do not generalize to frontier problems, and that the gap between discriminative and generative verification capabilities widens dramatically with difficulty—strengthening the case for adaptive paradigm selection.\n\n**Generative PRMs.** ThinkPRM (arXiv 2504.16828, ICLR 2026) scales verification compute via extended CoT thinking, achieving F1 of 87.3/85.7 on OlympiadBench/OmniMATH with ThinkPRM-14B—a ~12-15 F1 point advantage over the best discriminative PRMs on hard subsets, but at ~100-500x compute cost per step. GenPRM (arXiv 2504.00891, AAAI 2026) shows GenPRM-1.5B outperforms GPT-4o on ProcessBench via code-augmented generative verification; GenPRM-7B achieves avg F1 75.2 (Pass@1) and 80.5 (Maj@8).\n\n**Step-Level Adaptive Verification (Implicit Routing).** Dyve (arXiv 2502.11157, EMNLP 2025) is the most directly related prior work and the pioneer of step-level paradigm selection. It trains a single DeepSeek-R1-Distill-Qwen-14B via standard cross-entropy SFT on 117K examples to implicitly route between System 1 (single-token '+' confirmation) and System 2 (CoT analysis, up to 8192 tokens). ProcessBench F1: 68.5/58.3/49.0/47.2 (avg ~55.8). Critically, Dyve outperformed ALL contemporaneous baselines at the time of publication. However, stronger discriminative PRMs (ActPRM avg F1 75.0; Qwen2.5-Math-PRM-7B avg F1 73.5) have since surpassed Dyve's performance. This reveals a ceiling of implicit/entangled routing: (a) the routing decision is entangled with the verification itself (learned output length as proxy), preventing composition with independently improved verifiers—analogous to the routing-representation interference identified in MoE research (Grouter, arXiv 2603.06626, ICML 2026); (b) steps are scored independently with no sequential error cascade awareness; (c) standard cross-entropy SFT provides no quality floor guarantee; (d) no separable routing component enables ablation or interpretability. CRISP-PRM builds on Dyve's pioneering insight with explicit, decoupled routing designed to work with stronger base models.\n\n**Modular and Decoupled Systems Theory.** Grouter (arXiv 2603.06626, ICML 2026) demonstrates that decoupling routing topology from expert representation in MoE eliminates mutual optimization interference, boosting data utilization by 4.28x and throughput by 33.5%. StableMoE (arXiv 2204.08396, ACL 2022) identifies 'routing fluctuation' as a pathology of entangled routing-representation training and solves it by distilling a decoupled router. D'Amour et al. ('Underspecification,' arXiv 2011.03395, NeurIPS 2021) formally show that in composed ML systems, improving one component can degrade downstream performance unless interfaces are decoupled—establishing independent improvability as requiring architectural separation. Select-then-Solve (arXiv 2604.06753, Apr 2026) demonstrates that no single inference paradigm dominates across tasks; oracle per-task paradigm selection beats the best fixed paradigm by 17.1pp, with a lightweight router recovering up to 37% of the oracle gap. These results collectively provide theoretical grounding for CRISP-PRM's core design principle: decoupling verification paradigm selection from verification execution.\n\n**Step-Level Uncertainty Quantification.** CoT Entropy (Ye et al., arXiv 2502.11250, Feb 2025) introduces a novel UQ method for step-level verification in generative PRMs: it samples multiple reasoning paths at each step, groups outputs by binary correctness decisions, and computes entropy over the marginal distribution: H = −Σ_e(Σ_c p_θ(c,e|x≤t)) log(Σ_c p_θ(c,e|x≤t)). Achieves AUROC 0.680, outperforming all UQ baselines (SEU-MiniLM 0.661, SEU-NV-Embed). ReProbe/UHeads (arXiv 2511.06209, ACL 2026) provides lightweight step-level uncertainty heads; combining ReProbe scores with PRM scores outperforms either alone.\n\n**Problem-Level Fast/Slow Routing.** F/S-RM (arXiv 2603.20212, Mar 2026) trains a single Qwen3-8B with dual fast (first-token scalar) and slow (CoT generation) modes, using dual-confidence activation to route at the problem level; achieves 20.8% token savings but never considers within-solution step variation. E-GRM (arXiv 2604.10072, ACL 2026) routes between direct inference and CoT generation via parallel-decoding consensus at the problem level; 62% latency reduction and 49% FLOP reduction on MATH. CAMEL (arXiv 2602.20670, ICML 2026) uses log-probability confidence gating for pairwise preference judging; problem-level and not PRM-specific.\n\n**Step-Level Generation Routing.** TRIM (arXiv 2601.10245, ICLR 2026) performs step-level routing between small and large generation models using PRM-derived uncertainty, achieving 5x cost efficiency on MATH-500; routes generators, not verification paradigms.\n\n**Verification Compute Optimization.** VerifySteer (arXiv 2605.20745, May 2026) identifies verifier strictness signals in hidden states at paragraph-boundary delimiter tokens and steers verification depth via selective latent interventions. Achieves ProcessBench F1 of 72.3 with Qwen3-8B at 4-7x less inference compute than self-consistency; orthogonal to and composable with fine-tuned verifiers. Adaptive Test-Time Compute (arXiv 2602.03975, Feb 2026) performs state-level selective verification combining deterministic feasibility gating with learned scoring and adaptive allocation, achieving 30% fewer verifier calls on MATH-500. Budget-aware Test-time Scaling (arXiv 2510.14913, 2025) shows discriminative verifiers + self-consistency (Pessimistic Verification) outperform generative verifiers under constrained FLOP budgets.\n\n**Constrained RL for Quality Guarantees.** Constrained GRPO (arXiv 2602.05863, Feb 2026) introduces a Lagrangian-based extension of GRPO for constrained policy optimization with indicator cost functions, scalarized advantage construction (preventing standard-deviation mismatch), and learned multipliers. Faithful GRPO (arXiv 2604.08476, Apr 2026) applies this to transform quality metrics from reward terms into hard constraints via Lagrangian dual ascent, reducing inconsistency from 24.5% to 1.7%.\n\n**Adaptive Thinking for Generators.** PATS (arXiv 2505.19250, May 2025) introduces process-level adaptive thinking mode switching for generators. Adjusts beam width per step based on PRM scores, achieving near-optimal accuracy at 55% of full-compute token usage. PATS adapts generation depth; CRISP-PRM adapts verification depth—complementary.\n\n**Credit Assignment and Error Propagation.** CRM (arXiv 2509.26578, 2025) frames step correctness using conditional probability chain rules: defining h(t) = Pr(z=t|z≥t) as the conditional probability of entering a wrong state at step t given all prior steps were correct, and decomposing trajectory correctness as S(t) = Π_{k=1}^{t}(1−h(k)). Step rewards derive from a potential function Φ(s_t) = log S(t), yielding per-step reward r_t = log(1−h(t)). PURE (arXiv 2504.15275, 2025) introduces min-form credit assignment proving the weakest step dominates. 'Beyond the First Error' (arXiv 2505.14391, 2025) distinguishes error propagation from error cessation.\n\n**PRM Calibration.** 'Know What You Don't Know' (arXiv 2506.09338, NeurIPS 2025) demonstrates PRMs are poorly calibrated, overestimating success probability—motivating multi-signal criticality estimation rather than relying on single PRM confidence scores.\n\n**Summary.** Dyve pioneered step-level paradigm selection and outperformed all contemporaneous baselines, demonstrating the value of adaptive verification. However, no existing system combines (a) explicit, decoupled criticality estimation grounded in the principle that verification selection and verification execution are separate concerns, (b) sequential error cascade awareness, (c) constrained training with F1 floor guarantees, and (d) demonstrated robustness to changing cost ratios between verification paradigms.",
  "inspired_by": "Convergence of five research threads with a critical empirical insight, unified by a theoretical principle from modular systems research: (1) Dyve (EMNLP 2025) demonstrated that step-level fast/slow verification within a single model is feasible and valuable, outperforming all contemporaneous baselines. The subsequent emergence of stronger discriminative PRMs (ActPRM, avg F1 75.0) that surpass Dyve reveals that implicit/entangled routing hits a ceiling—motivating explicit, decoupled routing. (2) MoE literature (Grouter, ICML 2026; StableMoE, ACL 2022) and composed ML systems theory (D'Amour et al., NeurIPS 2021) formally establish that entangled routing-computation optimization creates mutual interference and prevents independent improvability—providing theoretical grounding for why Dyve's ceiling exists and why decoupled routing is the solution. (3) F/S-RM (Mar 2026) proves a single model can support both discriminative and generative modes with dual-confidence routing → provides the architectural foundation. (4) CRM's conditional probability chain rule decomposes trajectory correctness as S(t) = Π(1−h(t)) and PURE's min-form credit assignment proves the weakest step dominates → verification effort should target steps with highest conditional error probability. (5) CoT Entropy (arXiv 2502.11250) achieves best-in-class step-level UQ for generative PRMs (AUROC 0.680) → provides validated signal for criticality estimation. (6) Constrained GRPO (arXiv 2602.05863) and Faithful GRPO (arXiv 2604.08476) provide principled frameworks for enforcing quality constraints during RL training → enables the F1 floor guarantee. Pattern: 'Dyve showed the right question (adaptive step verification). The next step requires principled decoupling of verification paradigm selection from verification execution—a design principle established in MoE research but not yet applied to PRM verification—composed with stronger base models, principled criticality estimation, and constrained training with quality guarantees.'",
  "approach": "We propose CRISP-PRM (CRIticality-based Step-level Paradigm selection for Process Reward Models), a framework built on a unified dual-mode verifier that selects the verification paradigm—fast (discriminative) or deep (generative CoT)—for each reasoning step based on estimated step criticality, under a compute budget constraint. Building on Dyve's pioneering demonstration that step-level paradigm selection outperforms contemporaneous baselines, CRISP-PRM introduces explicit, decoupled routing designed to work with modern strong base models.\n\n**Theoretical Foundation: The Decoupling Principle for Verification**\n\nCRISP-PRM is grounded in a key insight from modular systems research: verification paradigm selection and verification execution are fundamentally different concerns that must be architecturally decoupled. In entangled systems like Dyve, the routing decision (when to use deep verification) is learned jointly with the verification itself (how to verify), through output length as an implicit proxy. This creates three well-characterized pathologies: (a) Optimization interference: gradients for improving routing conflict with gradients for improving verification, as demonstrated in MoE research where Grouter (arXiv 2603.06626, ICML 2026) showed 4.28x data efficiency gains from decoupling routing from representation. (b) Routing fluctuation: the same step may be routed differently during training vs. inference when routing is entangled with learned representations, as StableMoE (arXiv 2204.08396, ACL 2022) identified and solved via decoupled router distillation. (c) Failure of independent improvability: in composed ML systems, improving one component can degrade downstream performance unless interfaces are decoupled (D'Amour et al., arXiv 2011.03395, NeurIPS 2021). This explains why Dyve cannot benefit from stronger discriminative PRMs—the entangled routing has no separable interface through which to inject improvements. CRISP-PRM's explicit SCE provides this interface: advances in discriminative PRMs, generative PRMs, or uncertainty estimation each independently improve system performance without retraining the other components.\n\n**Architecture: Unified Dual-Mode PRM**\n\nCRISP-PRM uses a single Qwen3-8B model fine-tuned to support both verification modes, following the F/S-RM dual-mode paradigm adapted for step-level process verification:\n\n• Fast mode: Given (problem, solution prefix, step_i), the model's first generated token is a correctness judgment ('correct'/'incorrect'). The token probability p(correct|context) serves directly as a scalar step reward. Cost: ~10ms/step (single forward pass). No separate classification head needed—the standard LM head suffices.\n\n• Deep mode: A special trigger token is appended to the prompt, bypassing fast judgment and entering CoT verification. The model generates a step-by-step verification rationale inside &lt;verify>...&lt;/verify> tags, then outputs a final correctness judgment. Cost: ~100ms-2s/step depending on model size and generation length.\n\n**Training Pipeline: Two-Stage with Constrained RL**\n\nStage 1 — SFT Foundation: Combined loss L = L_step + λ·L_action, where L_step is binary cross-entropy on step labels (fast mode) combined with generation loss on synthetic verification CoTs from ThinkPRM-style data (deep mode), and L_action is an action-space constraint penalizing probability leakage to irrelevant tokens during fast mode.\n\nStage 2 — Constrained GRPO with F1 Floor: We adopt the Constrained GRPO framework (arXiv 2602.05863) to fine-tune the unified model with a hard F1 floor guarantee—ensuring the model never degrades below the current discriminative SOTA quality. Concrete specification:\n\n(a) Indicator cost function: C_F1(π) = 𝕀[F1_batch(π) < F1_threshold], where F1_threshold is set to the current discriminative SOTA F1 on a held-out ProcessBench validation split (avg F1 75.0 for ActPRM-class models; we use the best available discriminative PRM at training time).\n\n(b) Lagrangian objective: ℒ(π,λ) = J_R(π) − λ·(J_C(π) − d̃), where J_R is the primary reward (format correctness + outcome accuracy for both fast and deep modes), J_C is the constraint violation rate, and d̃ is the target violation rate (0.05 = at most 5% of validation batches may fall below F1_threshold).\n\n(c) Scalarized advantage construction (NOT scalarized rewards, following arXiv 2602.05863 Theorem 4.1 to prevent standard-deviation mismatch): A_ScAdv = λ_R·Z_R − λ_C·Z_C, where Z_j = (Component_j − mean(Component_j))/std(Component_j) are per-component standardized advantages. This preserves the intended trade-off between reward maximization and constraint satisfaction.\n\n(d) Multiplier update: ∇_λ ℒ = −(J_C(π) − d̃), applied via gradient descent with projection λ ≥ 0. When F1 drops below threshold (J_C > d̃), the gradient is positive, increasing λ and strengthening the constraint penalty.\n\n(e) Conservative checkpoint selection as fallback: evaluate F1 on validation set per epoch; only accept parameter updates that maintain F1 above threshold. This provides a hard guarantee even if the Lagrangian balance oscillates during training.\n\nThis follows the precedent of Faithful GRPO (arXiv 2604.08476), which demonstrated that transforming quality metrics from reward terms into hard constraints via Lagrangian dual ascent reduces quality degradation from 24.5% to 1.7%.\n\n**Step Criticality Estimator (SCE)**\n\nA lightweight module (<1M params) that scores each step's need for deep verification using multiple complementary signals. Unlike Dyve's implicit routing (where the model learns to self-regulate output length through SFT, with no separable routing component), the SCE is an explicit, interpretable, and ablatable module—the architectural embodiment of the decoupling principle.\n\nThe SCE combines:\n1. Fast-mode intuition confidence: C_I = |p(correct) − p(incorrect)| from the fast verification pass (available as a byproduct)\n2. Fast-mode token confidence: C_T = mean negative log-probability of irrelevant tokens, measuring probability mass leakage beyond the binary judgment (from F/S-RM's dual-confidence mechanism)\n3. CoT Entropy signal: Following Ye et al. (arXiv 2502.11250), when running complementary analysis, sample multiple reasoning paths at each step and compute entropy over the marginal distribution of binary decision outcomes: H = −Σ_e(Σ_c p_θ(c,e|x≤t)) log(Σ_c p_θ(c,e|x≤t)). Steps with high CoT Entropy indicate verifier uncertainty requiring deeper analysis. Optional when compute-constrained.\n4. Generator internal uncertainty: entropy of the generating model's hidden states via ReProbe-style probes (<10M params on frozen generator), when generator internals are available. Optional for black-box generator settings.\n5. Structural features: step position in chain, relative token length, domain signal. Justified by CoLD (arXiv 2507.15698) showing PRMs have strong length bias.\n\nThe SCE is an MLP that outputs a criticality score c_i ∈ [0,1] for each step. Training signal derives from oracle construction: run both fast and deep modes on training steps, identify 'value-add' steps where fast mode misclassifies but deep mode succeeds, and train SCE via binary cross-entropy. We include a planned ablation ladder: (i) fast-mode confidence only → (ii) dual-confidence (C_I + C_T) → (iii) +CoT Entropy → (iv) +ReProbe → (v) +structural features.\n\n**Budget-Constrained Router**\n\nGiven a per-solution compute budget B (fraction of steps receiving deep verification), the router:\n1. Runs fast verification on ALL K steps (cheap baseline, ~60ms for 6 steps). This simultaneously produces scalar scores and SCE input signals.\n2. Computes criticality scores c_i for all steps.\n3. Selects the top-⌈B·K⌉ highest-criticality steps for deep verification.\n4. Final step scores combine fast and deep assessments: steps receiving only fast verification use the fast scalar score; steps receiving deep verification use the deep judgment.\n\nThe budget B is a tunable hyperparameter that parameterizes the cost-accuracy Pareto frontier: at B=0, all steps use fast verification (cheapest); at B=1, all steps use deep verification (most accurate). The SCE threshold mapping to a given B is calibrated from the empirical criticality score distribution on a calibration set. Critically, the cost ratio between paradigms enters ONLY through B—as generative costs decrease, B can be increased to allocate more deep verification at the same total cost.\n\n**Sequential Error Cascade (SEC) Enhancement (Optional)**\n\nFor applications where step ordering matters, we add a sequential processing mode grounded in CRM's conditional probability chain rule (arXiv 2509.26578), which decomposes trajectory correctness as S(t) = Π_{k=1}^{t}(1−h(k)) where h(t) = Pr(z=t|z≥t) is the conditional probability of entering a wrong state at step t given prior steps were correct, and PURE's min-form insight:\n- If deep verification detects an ERROR at step i: automatically flag all subsequent steps for deep verification or assign minimum scores (since they are built on faulty premises, and S(T) ≤ S(i) per the multiplicative decomposition).\n- If deep verification CONFIRMS correctness: update posterior criticality of subsequent steps, potentially lowering priority for dependent downstream steps.\nThis is an optional enhancement that provides marginal accuracy gains on top of the core budget-constrained routing.\n\n**Robustness to Cheaper Generative Verification**\n\nCRISP-PRM's value proposition is robust to future reductions in generative verification cost, for six reasons: (a) Even a 10x speedup in generative models leaves a 10-50x cost gap (100-500ms vs 10ms per step)—routing still provides substantial efficiency gains. (b) The SCE provides accuracy gains independent of cost: by identifying which steps most benefit from deeper analysis, routing improves verification allocation quality regardless of per-mode costs. Even at equal costs, selectively applying deep verification to high-criticality steps outperforms uniform application because the model's deep mode may still outperform its fast mode on specific error types (e.g., soundness errors, multi-step logical chains). (c) CRISP-PRM's routing is parameterizable—the cost ratio enters only through the budget constraint B and SCE threshold, both tunable hyperparameters. As costs converge, B increases to allocate more deep verification while maintaining cost parity with uniform fast. (d) In the limit where generative cost equals discriminative cost, CRISP-PRM degenerates to uniform deep verification, which is the accuracy-optimal baseline—the framework gracefully adapts rather than becoming irrelevant. (e) Historical analog: TRIM (arXiv 2601.10245) shows step-level routing between models of different sizes remains valuable even as smaller models improve, because the relative cost gap persists across model generations. (f) GenPRM-1.5B still requires multiple forward passes for CoT generation—the cost gap is fundamental (single-token vs multi-token generation) rather than purely model-size dependent.\n\n**Difficulty-Stratified Efficiency Analysis**\n\nUsing ProcessBench data (arXiv 2412.06559, ACL 2025; verified in R-PRM, arXiv 2503.21295, EMNLP 2025, Table 1) for Qwen2.5-Math-PRM-7B: err accuracy of 72.0%/68.0%/55.7%/55.2% and corr accuracy of 96.4%/90.4%/85.5%/83.0% across GSM8K/MATH/OlympiadBench/OmniMATH. Hard2Verify (arXiv 2510.13744) further shows that on frontier-difficulty problems, the best discriminative PRM collapses to F1 37.3—indicating the fraction of steps requiring deep verification scales superlinearly with difficulty:\n\n• Easy tier (GSM8K-level): Fast verification reliable on ~85-90% of steps. Deep needed on ~10-15%. Expected latency reduction vs uniform deep: ~87%.\n• Medium tier (MATH-level): Fast verification reliable on ~80-85% of steps. Deep needed on ~15-20%. Expected reduction: ~82%.\n• Hard tier (OlympiadBench-level): Fast verification reliable on ~70-80% of steps. Deep needed on ~20-30%. Expected reduction: ~75%.\n• Hardest tier (OmniMATH-level): Fast verification reliable on ~65-75% of steps. Deep needed on ~25-35%. Expected reduction: ~70%.\n• Frontier tier (Hard2Verify-level): Fast verification reliable on ~40-60% of steps. Deep needed on ~40-60%. Expected reduction: ~50%. CRISP-PRM's relative accuracy gain is maximized here.\n\nCRISP-PRM's value proposition is difficulty-adaptive: on easy problems, it saves the most compute; on hard and frontier problems, it provides the largest accuracy gains.\n\n**Evaluation Protocol**\n\n• Step-level accuracy: F1 on ProcessBench (GSM8K/MATH/OlympiadBench/OmniMATH subsets reported separately, with err/corr accuracy breakdown) and PRMBench (fine-grained error type breakdown). If accessible, Hard2Verify ErrorID evaluation to test frontier generalization.\n• Solution-level utility: Best-of-N reranking accuracy on MATH-500, AIME'24, GPQA-Diamond\n• Efficiency: FLOPs per solution, accuracy-per-FLOP Pareto frontiers at multiple budget levels B ∈ {0.05, 0.1, 0.2, 0.3, 0.5, 1.0}\n• Baselines: (i) uniform fast PRM (ActPRM, avg F1 75.0; and Qwen2.5-Math-PRM-7B, avg F1 73.5), (ii) uniform deep PRM (ThinkPRM-14B), (iii) Dyve (implicit step-level routing, avg F1 ~55.8)—HISTORICAL BASELINE showing progress from Dyve's pioneering work, (iv) problem-level routing (F/S-RM-style dual-confidence gating), (v) VerifySteer (latent steering, F1 72.3), (vi) Budget-aware Pessimistic Verification, (vii) random step selection for deep verification (ablation control), (viii) PRM-confidence-only routing (single-signal ablation)\n• Ablation studies: (A1) Explicit SCE routing vs. Dyve-style implicit SFT routing on SAME base model—isolating the value of decoupled routing (tests the decoupling principle directly); (A2) SCE signal ablation ladder (confidence-only → dual-confidence → +CoT Entropy → +ReProbe → +structural)—quantifying marginal signal contribution; (A3) Constrained GRPO (with F1 floor) vs. standard SFT for unified model training—testing whether Constrained GRPO prevents quality degradation; (A4) SEC-aware vs. independent greedy allocation—measuring value of sequential error cascade awareness; (A5) Budget sensitivity analysis across B ∈ {0.05, 0.1, 0.2, 0.3, 0.5}; (A6) Difficulty-stratified analysis showing per-tier routing rates and gains, including Hard2Verify-level problems if available\n• Complementarity analysis: CRISP-PRM + VerifySteer (explicit routing + latent strictness steering); CRISP-PRM + PATS (verification routing + generation routing)",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "350 A100-80GB hours (80h unified model training (SFT + Constrained GRPO), 100h oracle construction running both modes on ~120K steps, 20h SCE/router training, 80h evaluation across 4 benchmarks × multiple budgets × 8 baselines including Dyve, 50h ablations (A1-A6), 10h ReProbe probe training, 10h VerifySteer comparison)",
      "timeline": "10-14 weeks (single researcher)",
      "estimated_gpu_cost": "$700 (at ~$2/hr A100-80GB cloud)"
    },
    "human_in_loop": {
      "gpu_hours": "280 A100-80GB hours (fewer dead-end experiments via Claude-guided threshold tuning and ablation prioritization)",
      "timeline": "7-10 weeks",
      "claude_api_cost": "$200-400 (experiment design, analysis scripts, paper writing assistance)",
      "estimated_gpu_cost": "$560"
    },
    "auto_research": {
      "gpu_hours": "480 A100-80GB hours (broader ablations: multiple SCE architectures, threshold sensitivity, cross-domain transfer, additional benchmarks including Hard2Verify, difficulty-stratified analysis, Dyve reproduction for fair comparison)",
      "timeline": "4-6 weeks",
      "claude_api_cost": "$400-700 (end-to-end experiment orchestration, code generation, result analysis)",
      "estimated_gpu_cost": "$960",
      "speed_bottleneck": "Unified model training is the main bottleneck (~80h); oracle construction is embarrassingly parallel—with 4×A100, drops from ~50h to ~13h wall-clock."
    }
  },
  "target_venues": [
    "AAAI 2027 (full papers Jul 28 2026, supplementary Jul 31 2026 — confirmed via official CFP)",
    "ARR August 2026 cycle (Aug 3 2026, for commitment to NAACL 2027 or EACL 2027)"
  ],
  "level": "solid-to-strong",
  "key_references": [
    "Dyve: Thinking Fast and Slow for Dynamic Process Verification (arXiv 2502.11157, EMNLP 2025) — pioneered step-level System 1/System 2 routing; outperformed all contemporaneous baselines with avg F1 ~55.8; since surpassed by stronger discriminative PRMs",
    "Process Reward Models That Think (ThinkPRM, arXiv 2504.16828, ICLR 2026)",
    "Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Model Parameters (ICLR 2025)",
    "Fast-Slow Thinking RM: Efficient Integration of Scalar and Generative Reward Models (F/S-RM, arXiv 2603.20212, Mar 2026)",
    "Reason Only When Needed: Efficient Generative Reward Modeling via Model-Internal Uncertainty (E-GRM, arXiv 2604.10072, ACL 2026)",
    "CAMEL: Confidence-Gated Reflection for Reward Modeling (arXiv 2602.20670, ICML 2026)",
    "TRIM: Hybrid Inference via Targeted Stepwise Routing in Multi-Step Reasoning Tasks (arXiv 2601.10245, ICLR 2026)",
    "The Hidden Signal of Verifier Strictness: Controlling and Improving Step-Wise Verification via Selective Latent Steering (VerifySteer, arXiv 2605.20745, May 2026)",
    "Adaptive Test-Time Compute Allocation via Learned Heuristics over Categorical Structure (arXiv 2602.03975, Feb 2026)",
    "PATS: Process-Level Adaptive Thinking Mode Switching (arXiv 2505.19250, May 2025)",
    "Efficient Test-Time Scaling of Multi-Step Reasoning by Probing Internal States of Large Language Models (ReProbe/UHeads, arXiv 2511.06209, ACL 2026)",
    "Stop Summation: Min-Form Credit Assignment Is All Process Reward Models Need (PURE, arXiv 2504.15275, 2025)",
    "Conditional Reward Models for Process-Level Credit Assignment (CRM, arXiv 2509.26578, 2025) — uses conditional probability chain rules to decompose trajectory correctness as S(t) = Π(1−h(t)), where h(t) = Pr(z=t|z≥t) is the conditional error probability at step t",
    "Beyond the First Error: Modeling Error Propagation and Cessation in Multi-Step Reasoning (arXiv 2505.14391, 2025)",
    "Know What You Don't Know: Calibration of Process Reward Models (arXiv 2506.09338, NeurIPS 2025)",
    "ProcessBench: Identifying Process Errors in Mathematical Reasoning (arXiv 2412.06559, ACL 2025)",
    "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models (arXiv 2501.03124, 2025)",
    "When to Trust the Cheap Check: Weak and Strong Verification for Reasoning (arXiv 2602.17633, Feb 2026)",
    "Budget-aware Test-time Scaling via Discriminative Verification (arXiv 2510.14913, 2025)",
    "When To Solve, When To Verify: Compute-Optimal Problem Solving and Verification (arXiv 2504.01005, 2025)",
    "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (arXiv 2504.00891, AAAI 2026)",
    "SCAN: Self-Denoising Monte Carlo Annotation for Robust Process Reward Learning (arXiv 2509.16548, NeurIPS 2025)",
    "R-PRM: Reasoning-Driven Process Reward Modeling (arXiv 2503.21295, EMNLP 2025) — Table 1 provides independently verified ProcessBench numbers for Qwen2.5-Math-PRM-7B",
    "The Lessons of Developing Process Reward Models in Mathematical Reasoning (arXiv 2501.07301, 2025) — Qwen2.5-Math-PRM development and evaluation",
    "Uncertainty-Aware Step-wise Verification with Generative Reward Models (Ye et al., arXiv 2502.11250, Feb 2025) — CoT Entropy for step-level UQ in generative PRMs; AUROC 0.680",
    "Constrained Group Relative Policy Optimization (arXiv 2602.05863, Feb 2026) — Lagrangian-based constrained GRPO with scalarized advantage construction; foundation for F1 floor mechanism",
    "Faithful GRPO: Improving Visual Spatial Reasoning via Constrained Policy Optimization (arXiv 2604.08476, Apr 2026) — precedent for transforming quality metrics into hard constraints via Lagrangian dual ascent",
    "Rethinking Optimal Verification Granularity for Compute-Efficient Test-Time Scaling (VG-Search, arXiv 2505.11730, NeurIPS 2025)",
    "CoLD: Mitigating Length Bias in Process Reward Models (arXiv 2507.15698, 2025)",
    "SHAPE: Stage-aware Hierarchical Advantage via Potential Estimation (arXiv 2604.06636, Apr 2026)",
    "SPAE: Step Potential Advantage Estimation for Credit Assignment (arXiv 2601.03823, Jan 2026)",
    "Efficient Process Reward Model Training via Active Learning (ActPRM, arXiv 2504.10559, 2025) — current discriminative PRM SOTA on ProcessBench at 7B scale, avg F1 75.0 (ActPRM-X: 76.0)",
    "Hard2Verify: A Step-Level Verification Benchmark for Open-Ended Frontier Math (arXiv 2510.13744, 2025) — reveals catastrophic failure of discriminative PRMs on frontier problems (F1 78.3 → 37.3)",
    "Grouter: Decoupling Routing from Representation (arXiv 2603.06626, ICML 2026) — demonstrates 4.28x data efficiency from decoupling routing topology in MoE; theoretical foundation for the decoupling principle",
    "StableMoE: Stable Routing Strategy for Mixture of Experts (arXiv 2204.08396, ACL 2022) — identifies routing fluctuation as a pathology of entangled routing-representation training",
    "Underspecification Presents Challenges for Credibility in Modern Machine Learning (D'Amour et al., arXiv 2011.03395, NeurIPS 2021) — formalizes how improving one component in composed systems can degrade others without decoupled interfaces",
    "Select-then-Solve: Paradigm Routing as Inference-Time Optimization for LLM Agents (arXiv 2604.06753, Apr 2026) — shows oracle paradigm selection beats best fixed paradigm by 17.1pp; validates learned paradigm routing",
    "AdaptiveStep: Automatically Dividing Reasoning Step through Model Confidence (ASPRM, arXiv 2502.13943, Feb 2025) — confidence-based step boundary detection for PRM training"
  ],
  "description": "We propose CRISP-PRM (CRIticality-based Step-level Paradigm selection for Process Reward Models), a framework built on a unified dual-mode verifier that routes each reasoning step to the optimal verification paradigm—fast discriminative scoring or deep generative CoT verification—based on explicit step criticality estimation and a tunable compute budget. Building on Dyve's (EMNLP 2025) pioneering demonstration that step-level paradigm selection outperforms contemporaneous baselines, CRISP-PRM introduces a principled advance grounded in the decoupling principle from modular systems research: verification paradigm selection and verification execution are fundamentally different concerns that must be architecturally separated to enable independent improvement of each component. Three concrete innovations implement this principle: (1) An explicit Step Criticality Estimator (SCE) combining dual-confidence signals from fast verification, CoT Entropy-based uncertainty (Ye et al., arXiv 2502.11250, AUROC 0.680), generator-internal uncertainty (ReProbe-style probes), and structural features—with an ablation ladder quantifying each component's marginal value. Unlike Dyve's entangled routing (where routing and verification are jointly optimized, creating the routing-representation interference characterized by Grouter, arXiv 2603.06626, ICML 2026), the SCE is a separable module that enables each verification paradigm to be independently upgraded. (2) A budget-constrained router that parameterizes the cost-accuracy Pareto frontier through a single hyperparameter B (fraction of steps receiving deep verification), enabling graceful adaptation to changing cost ratios: as generative verification becomes cheaper, B increases; in the limit of equal costs, the system degenerates to uniform deep verification. (3) Constrained GRPO fine-tuning (following arXiv 2602.05863) with a hard F1 floor guarantee via indicator cost functions, Lagrangian dual ascent with scalarized advantage construction, and conservative checkpoint selection—ensuring the unified model never degrades below discriminative SOTA quality (ActPRM avg F1 75.0, arXiv 2504.10559). Using ProcessBench data (arXiv 2412.06559, ACL 2025; verified in R-PRM, arXiv 2503.21295, Table 1) and Hard2Verify findings (arXiv 2510.13744, best discriminative PRM F1 collapses from 78.3% to 37.3% on frontier problems), we estimate ~10-15% of easy-tier steps and ~25-35% of hard-tier steps benefit from deep verification, yielding 70-87% latency reduction vs. uniform deep verification while targeting Pareto dominance over both uniform paradigms and problem-level routing approaches. The increasing verification gap at frontier difficulty levels (Hard2Verify) makes adaptive paradigm selection most valuable precisely where it matters most.",
  "project_name": "crisp_step_prm",
  "source": "web_research",
  "reviewer_response": {
    "CRM_MISCHARACTERIZATION": "Resolved. The fabricated 'survival analysis' and 'hazard function' terminology attributed to CRM has been removed throughout all sections. CRM is now accurately characterized using its own framing: conditional probability chain rules, where h(t) = Pr(z=t|z≥t) is the conditional probability of entering a wrong state at step t given prior steps were correct, with trajectory correctness decomposed as S(t) = Π_{k=1}^{t}(1−h(k)). Deep research confirmed that this multiplicative decomposition IS the core equation of the CRM paper—so the mathematical content was accurate, but the 'survival analysis' and 'hazard function' labels were imposed terminology that CRM's authors never use. The correction retains the valid mathematical form while using CRM's own conditional probability framing. Corrections applied in: core_problem, opportunity, landscape, inspired_by, approach (SEC module), key_references, and description.",
    "OUTDATED_DISCRIMINATIVE_SOTA": "Resolved. ActPRM (arXiv 2504.10559) is now cited as the current discriminative PRM SOTA at 7B scale with avg F1 75.0 (ActPRM-X: 76.0), surpassing Qwen2.5-Math-PRM-7B (73.5). The F1 floor threshold has been updated to 75.0. Note: the reviewer's cited arXiv ID (2601.22249) does not correspond to any existing paper; the verified ActPRM ID is 2504.10559, confirmed through direct paper access showing ProcessBench scores in Table 1. ASPRM/AdaptiveStep (arXiv 2502.13943) is added to the landscape with the accurate note that it does NOT evaluate on ProcessBench—it evaluates on Best-of-N metrics for GSM8K/MATH/code tasks only. Hard2Verify (arXiv 2510.13744) is now integrated throughout: Qwen2.5-Math-PRM-72B F1 drops from 78.3% on ProcessBench to 37.3% on Hard2Verify ErrorID, a 41pp collapse that STRENGTHENS the case for adaptive paradigm selection since the discriminative-generative gap widens with difficulty. A new 'Frontier tier' has been added to the difficulty-stratified analysis.",
    "UNVERIFIABLE_VENUE_CLAIMS": "Resolved via independent verification of all venue claims against arXiv annotations, ACL Anthology, official proceedings pages, and author repositories. Results: GenPRM AAAI 2026 — VERIFIED (GitHub repo confirms acceptance 2025-11-08; proceedings at aaai.org). E-GRM ACL 2026 — VERIFIED (arXiv Comments field states 'accepted by ACL 2026'). CAMEL ICML 2026 — VERIFIED (arXiv Comments field and ICML 2026 Downloads page listing poster). SCAN NeurIPS 2025 — VERIFIED (NeurIPS 2025 virtual poster page). Dyve EMNLP 2025 — VERIFIED (ACL Anthology). ProcessBench ACL 2025 — VERIFIED (ACL Anthology). R-PRM EMNLP 2025 — VERIFIED (ACL Anthology). ONE CORRECTION: ReProbe/UHeads was incorrectly labeled 'NeurIPS 2025' in earlier versions—it is actually ACL 2026 Main, confirmed via arXiv Comments field ('ACL 2026 Main') and project page at reprobe.github.io ('ACL 2026 - Long Paper'). This has been corrected throughout. ThinkPRM venue updated to ICLR 2026 based on verification.",
    "NOVELTY_CEILING": "Addressed via explicit articulation of the 'Decoupling Principle for Verification' as the core scientific insight, grounded in three independent theoretical foundations from outside the PRM literature: (1) Grouter (arXiv 2603.06626, ICML 2026) demonstrates that decoupling routing from representation in MoE eliminates optimization interference, yielding 4.28x data efficiency—directly analogous to decoupling verification selection from verification execution. (2) StableMoE (arXiv 2204.08396, ACL 2022) identifies 'routing fluctuation' as a pathology of entangled routing where the same input updates different experts during training but only one is used at inference—explaining why Dyve's implicit routing underperforms despite being trained on the same data. (3) D'Amour et al. (arXiv 2011.03395, NeurIPS 2021) formally establishes that independent improvability in composed ML systems requires decoupled interfaces—explaining why improving discriminative PRMs cannot help Dyve. Additionally, Select-then-Solve (arXiv 2604.06753) empirically validates that learned paradigm routing recovers 37% of the oracle gap (17.1pp). A new 'Theoretical Foundation' section in the approach articulates this formally. The contribution is reframed from 'combining four techniques' to 'demonstrating that verification paradigm selection and execution are fundamentally different concerns requiring architectural separation—a principle established in MoE research but not yet applied to PRM verification.' Ablation A1 directly tests this principle by comparing explicit vs implicit routing on the same base model.",
    "MISLEADING_DYVE_FRAMING": "Previously resolved (round 5). Maintained accurate historical characterization.",
    "GRPO_F1_FLOOR_MECHANISM_UNSPECIFIED": "Previously resolved (round 5). F1 threshold updated to 75.0 (ActPRM SOTA).",
    "MISSING_CITATION_COT_ENTROPY": "Previously resolved (round 5). Maintained.",
    "UNVERIFIABLE_SCAN_TABLE_2_NUMBERS": "Previously resolved (round 5). Maintained proper source chain.",
    "IMPACT_VULNERABILITY": "Previously resolved (round 5). Strengthened by Hard2Verify evidence showing discriminative-generative gap widens at frontier difficulty.",
    "MISSING_CITATION_ADAPTIVE_TTC": "Previously resolved (round 3). Maintained.",
    "MISSING_CITATION_PATS": "Previously resolved (round 3). Maintained.",
    "MISSING_CITATION_VERIFYSTEER": "Previously resolved (round 3). Maintained.",
    "FACTUAL_ERROR_ERR_ACCURACY": "Previously resolved (round 3). Maintained.",
    "TWO_MODEL_MEMORY_OVERHEAD": "Previously resolved (round 2). Maintained.",
    "STEP_DEPENDENCY_IGNORED": "Previously resolved (round 2). SEC now correctly cites CRM's conditional probability chain rule.",
    "SCE_SIGNAL_REDUNDANCY": "Previously resolved (round 2). Maintained.",
    "BUDGET_AWARE_TTS_OVERLAP": "Previously resolved (round 2). Maintained.",
    "CRITICAL_NOVELTY_F_S_RM": "Previously resolved (rounds 1-2). Maintained.",
    "CRITICAL_NOVELTY_E_GRM": "Previously resolved (rounds 1-2). Maintained.",
    "CRITICAL_NOVELTY_CAMEL": "Previously resolved (rounds 1-2). Maintained."
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d884d84-069e-42fc-93d4-8b232a49e810",
  "isSidechain": false,
  "requestId": "req_011CbU9CnFeUv9cm9D18Jeux",
  "type": "assistant",
  "uuid": "657fdf6d-a650-4c28-a583-8b58c9996221",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MkiC8wxGoXxVhVTEcB88Yq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14239,
      "cache_read_input_tokens": 55735,
      "output_tokens": 14597,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14239,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14597,
          "cache_read_input_tokens": 55735,
          "cache_creation_input_tokens": 14239,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14239
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"CRISP-PRM: Criticality-Aware Step-Level Paradigm Selection for Unified…",
  "leafUuid": "657fdf6d-a650-4c28-a583-8b58c9996221",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff"
}
```

---

### Runtime record

_source line 40_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising CRISP-PRM after round 5 reviewer feedback",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff"
}
```

---

### Runtime record

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-28 (UTC).**  ## Original idea {   \"title\": \"CRISP-PRM: Criticality-Aware Step-Level Paradigm Selection for Unified…",
  "leafUuid": "657fdf6d-a650-4c28-a583-8b58c9996221",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Revising CRISP-PRM after round 5 reviewer feedback",
  "sessionId": "6c159ebd-d2a0-4490-8925-9988ef96dbff"
}
```

---
