# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-27 (UTC).** ## Original idea { "tit

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 90
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/chats/exported-trajectories/account-3/2a30fe45-086a-4752-b69b-cc68f89516e6.jsonl`
- **Structured JSON:** [`f39b93870a13d3b51653.json`](../../sessions/f3/f39b93870a13d3b51653.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T18:16:05.545Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T18:16:05.545Z",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-27 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization\",\n  \"core_problem\": \"Current autoformalization models—even those achieving strong in-distribution results (ATF: 94.51% Pass@1 on FormalMath-Lite; ATLAS: 96.93% pass@128 on miniF2F)—degrade sharply on unfamiliar mathematical domains because they lack both domain-specific Mathlib knowledge and mechanisms to adapt at deployment time. Meanwhile, test-time RL (TTRL) has been shown to boost informal math reasoning dramatically but cannot be naively applied to autoformalization: majority voting over formal statements is ill-defined (unlike numerical answers), and GRPO's advantage normalization amplifies noise from ambiguous pseudo-labels. Can we make TTRL viable for autoformalization by combining a trained semantic critic, dependency-aware retrieval, debiased advantage estimation, and progressive domain curriculum?\",\n  \"opportunity\": \"Three independently validated capabilities have never been combined: (1) Dependency-aware retrieval closes a ~2.9x quality gap—DRIFT reports Oracle* retrieval at 58.90% vs. DPR at 20.08% BEq+@10 on Con-NF (ICLR 2026), confirming domain-specific dependencies are the key bottleneck. (2) TTRL has boosted informal math reasoning by 211% (Qwen-2.5-Math-7B on AIME 2024, NeurIPS 2025), and DDRL's debiased advantage estimation (ACL 2026) fixes the spurious signal amplification problem that otherwise undermines TTRL with noisy pseudo-labels. (3) CriticLean (July 2025) demonstrates that a trained semantic critic raises autoformalization accuracy from 54% to 84% compared to compilation-only feedback, providing the reliable reward signal needed to make RL-based autoformalization work in low-label regimes. Existing strong baselines—ATF's tool-augmented iterative refinement (65.38% Pass@1 on CombiBench) and Monotonic Refinement's multi-model orchestration (90.27% overall on miniF2F)—achieve impressive results but cannot adapt model weights to new domains. Recent infrastructure (DDR's 500K-sample dependency dataset, CRAMF's 26K Mathlib concept index, FormalMATH's multi-domain benchmark, Kimina Lean Server for high-throughput verification, open-source CriticLeanGPT models) makes a critic-guided TTRL approach newly feasible.\",\n  \"landscape\": \"TTRL (NeurIPS 2025) demonstrated test-time RL for informal math using majority-voting pseudo-labels. DDRL (ACL 2026 Findings) identified that GRPO's group-relative advantage normalization causes spurious signal amplification from ambiguous pseudo-labels, proposing fixed ±1 advantages and frequency-based balanced sampling for debiased test-time RL—yielding up to 58.2% relative improvement on hard math benchmarks. Concurrent work on TTRL debiasing includes T³RL (tool-based verification), DCRL (dual consensus), DARE (distribution-aware reward estimation), and ECHO (entropy-confidence hybrid optimization). AlphaProof (Nature 2025) applies test-time RL to formal proving via variant generation. Kimina-Prover (April 2025) internalizes search via RL for Lean proving, achieving 80.7% pass@8192 on miniF2F. FormaRL (COLM 2025) applies GRPO-based RL to autoformalization using compilation + LLM consistency rewards, improving pass@1 from 4% to 26% on ProofNet. CriticLean (July 2025) introduces a trained semantic critic (CriticLeanGPT) for autoformalization quality evaluation—achieving 87% accuracy on CriticLeanBench and raising pipeline accuracy from 54% to 84% over compilation-only feedback—with open-source models from 8B to 32B parameters. ATLAS (NeurIPS 2025) builds a 300K synthetic NL-FL dataset via iterative augmentation, achieving 96.93% pass@128 and 70.08% pass@1 on miniF2F, demonstrating that high-k sampling nearly solves in-distribution benchmarks but pass@1 remains challenging. ATF/Autoformalizer with Tool Feedback (arXiv 2025) achieves 94.51% Pass@1 on FormalMath-Lite and 65.38% on CombiBench using SFT + expert iteration + DPO with multi-LLM consistency checking—representing the state-of-the-art in iterative refinement without RL weight updates. Monotonic Reference-Free Refinement (January 2026) achieves 100% formal validity and 90.27% composite score on miniF2F through multi-model ensemble orchestration with certified monotonic improvement, but requires 6+ models including GPT-4.1-mini as a judge. DDR (December 2025) builds a 500K-sample dependency retrieval dataset with suffix-array verification. DRIFT (ICLR 2026) decomposes informal statements for targeted retrieval, nearly doubling F1 on ProofNet. CRAMF (2025) indexes 26K+ Mathlib definitions for concept-level retrieval, yielding up to 62.1% relative improvement. Aria (ICLR 2026) uses agentic Graph-of-Thought with dependency decomposition, achieving 68.5% accuracy on ProofNet. ProofBridge (ICLR 2026) combines contrastive joint embeddings with retrieval-augmented fine-tuning for proof autoformalization (+31.14% semantic correctness). ReForm (2026) applies position-aware RL rewards for reflective autoformalization (+22.6pp average). StepFun-Formalizer-32B achieves 40.5% BEq@1 SOTA on FormalMath-Lite via BEq-based majority voting for data curation. FormalEvolve (March 2026) frames autoformalization as test-time neuro-symbolic evolutionary search but without RL. After exhaustive search through May 2026, no work combines (a) retrieval-augmented context, (b) a trained semantic critic for reward computation, and (c) debiased test-time RL adaptation for autoformalization: existing retrieval methods (DDR, DRIFT, CRAMF, Aria) are static pipelines without RL; existing RL methods (FormaRL, ReForm) assume fixed-domain training without retrieval or semantic critic rewards; ATF and Monotonic Refinement use iterative inference without weight updates; existing TTRL applications (AlphaProof, Kimina-Prover) target proof search; and CriticLean provides the critic but not the RL adaptation loop.\",\n  \"inspired_by\": \"Field guide untried combination: 'Dependency-aware TTRL with semantic critic reward: Combine RAutoformalizer's dependency retrieval + CriticLean's semantic critic + DDRL's debiased advantage estimation + AlphaProof's Test-Time Reinforcement Learning.' Also: gap 'Dependency-aware autoformalization: models are context-blind to formal library contents' + gap 'Pseudo-reward design for formal statement agreement is ill-defined without a trained critic' + pattern 'Test-Time Compute Scaling via Problem-Specific Adaptation' + pattern 'Debiased RL for noisy reward environments.'\",\n  \"approach\": \"We propose TTRA (Test-Time Retrieval-Augmented autoformalization), a three-phase framework that makes TTRL viable for autoformalization through a multi-tier reward mechanism, debiased advantage estimation, and progressive domain curriculum.\\n\\n**Phase 1 — Base Formalizer and Critic Training.** Fine-tune a Qwen3-8B base model as a retrieval-augmented autoformalizer using DDR's 500K-sample dependency dataset and FormaRL's GRPO pipeline with a multi-tier reward function R(y, x) = r_compile × (α·r_critic + β·r_beq), where: r_compile ∈ {0,1} is the Lean 4 compilation gate (verified via Kimina Lean Server with 128 parallel pre-warmed REPL workers and LRU header caching); r_critic ∈ {0,1} is the semantic fidelity judgment from CriticLeanGPT-Qwen3-14B-RL (the open-source critic from CriticLean, achieving 84.8% accuracy on CriticLeanBench); r_beq ∈ [0,1] is the BEq consensus density (fraction of compilable candidates in the same BEq equivalence class, computed via Lean's exact? tactic for bidirectional implication). We set α=0.7, β=0.3 to weight semantic fidelity over syntactic consensus, since BEq has high precision (98.6%) but low recall (~33% on ProofNet). This avoids the fundamental problem of majority voting on formal statements by using a trained semantic critic rather than ill-defined agreement measures.\\n\\n**Phase 2 — Retrieval Module.** Build a domain-adaptive retrieval module that generates candidate Mathlib dependencies via DDR's suffix-array verification and injects retrieved formal definitions into the autoformalization prompt. Train the retriever on DDR's dataset and augment with CRAMF-style concept-level retrieval for broader coverage.\\n\\n**Phase 3 — Progressive Domain Curriculum for Test-Time Adaptation.** This directly addresses the bootstrapping problem: if retrieval is poor on the target domain, formalizations are wrong, rewards are noisy, and TTRL fails. We break this cycle through a three-stage curriculum:\\n  (a) Near-distribution warm-start: Apply TTRL on domains close to training data (e.g., elementary number theory, basic algebra) where retrieval coverage is high and the critic is reliable. Generate K=32 formalization candidates per problem, compute multi-tier rewards, and perform debiased GRPO updates following DDRL: replace GRPO's normalized advantages with fixed +1/-1 values (severing the amplification pathway where dividing by small std inflates gradients for ambiguous groups) and apply frequency-based balanced sampling to exclude ambiguous candidates from the training signal.\\n  (b) Retrieval bootstrapping: Use the adapted model from (a) to generate improved retrieval queries for moderately OOD domains (e.g., real analysis, combinatorics). The adapted model produces better formalization attempts that yield more informative retrieval feedback, breaking the chicken-and-egg cycle.\\n  (c) Far-OOD adaptation: Apply TTRL on truly OOD domains (algebraic geometry, PDE theory, condensed mathematics) using the bootstrapped retriever and optionally a critic fine-tuned on verified pairs accumulated from stage (b).\\n\\n**Evaluation.** Measure BEq@K and compilation success on FormalMATH's 5,560-problem multi-domain benchmark, the OOD Con-NF benchmark, and CombiBench. Compare against: (1) ATF-32B as the state-of-the-art iterative refinement baseline (94.51%/65.38% FormalMath-Lite/CombiBench), (2) ATLAS as the strong SFT-only data augmentation baseline (70.08% pass@1 miniF2F), (3) Monotonic Reference-Free Refinement as the inference-time orchestration upper bound (90.27% overall miniF2F), (4) FormaRL as the RL-without-retrieval baseline, (5) compilation-only TTRL and critic-only TTRL ablations, (6) standard GRPO vs. DDRL's debiased advantages, and (7) iterative self-refinement with compilation feedback (ATF-style) as a simpler non-RL baseline. Report per-domain breakdown to quantify adaptation gains across the progressive curriculum.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"1100-1500 A100-80GB hours (base formalizer GRPO training with multi-tier reward: ~350h on 8 GPUs; DDR retriever fine-tuning: ~80h on 4 GPUs; TTRL progressive adaptation across 3 curriculum stages × 5 domains with DDRL debiasing and ablations: ~550h on 4 GPUs; CriticLean critic inference during training: ~80h on 2 GPUs for the 14B critic; evaluation and inference: ~100h) + 12,000-18,000 CPU-hours for Lean 4 verification (128 parallel workers via Kimina Lean Server with LRU caching)\",\n      \"timeline\": \"14-18 weeks (4 wk base training + critic integration, 2 wk retriever, 5 wk progressive TTRL experiments across curriculum stages, 3-4 wk ablations and writing)\",\n      \"estimated_gpu_cost\": \"$2,200-$3,800 at ~$2.00/A100-hr + ~$600-$900 CPU verification costs\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"900-1200 A100-80GB hours (Claude handles critic evaluation augmentation and data synthesis, reducing CriticLean annotation overhead ~25%) + 10,000-14,000 CPU-hours for Lean verification\",\n      \"timeline\": \"10-14 weeks (Claude-assisted critic calibration in Phase 1; parallel curriculum experiment management in Phase 3)\",\n      \"claude_api_cost\": \"$500-$800 (critic reward calibration during GRPO training, synthetic domain-specific formalization examples, automated curriculum scheduling, ablation analysis)\",\n      \"estimated_gpu_cost\": \"$1,800-$3,000 + ~$500-$700 CPU costs\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"1800-2400 A100-80GB hours (automated hyperparameter sweeps over retrieval top-k, DDRL sampling parameters, critic threshold, GRPO group sizes K ∈ {16,32,64}, curriculum staging boundaries, plus multi-seed evaluation) + 25,000-35,000 CPU-hours for Lean verification at scale\",\n      \"timeline\": \"7-10 weeks (highly parallelized; wall-clock bottleneck is Lean 4 verification, mitigated by 128+ Kimina Lean Server workers with LRU caching achieving ~0.35s amortized per proof at 32 CPUs, ~0.10s at 64 CPUs)\",\n      \"claude_api_cost\": \"$900-$1,400 (automated experiment design, reward function ablation analysis, curriculum boundary optimization, paper drafting)\",\n      \"estimated_gpu_cost\": \"$3,600-$6,000 + ~$1,200-$1,700 CPU costs\",\n      \"speed_bottleneck\": \"Lean 4 compilation latency (~3.65s per statement with warm LRU cache on single worker; ~0.35s amortized at 32 parallel workers) dominates reward computation. Mitigated with Kimina Lean Server's pre-warmed REPL pool and LRU header caching (1.94x speedup over cold start). For K=32, batch=256: ~4,600 verifications/step requiring ~27 min at 32 CPUs or ~3.9 min at 128 CPUs. CriticLean inference (~14B model) adds ~0.5s per candidate on A100 but runs on GPU in parallel with CPU verification.\"\n    }\n  },\n  \"target_venues\": [\n    \"AAAI 2027 (abstract: July 21, full paper: July 28, 2026 — confirmed)\",\n    \"EACL 2027 via ARR August cycle (submission: August 3, 2026; commitment deadline TBD — confirmed, note corrected from originally announced August 6)\",\n    \"NeurIPS 2026 Workshops (suggested contribution deadline: August 29, 2026 — confirmed; suitable for early results from curriculum stages 1-2)\",\n    \"ICLR 2027 (deadline not yet announced as of May 2026 — best fit for full pipeline results if timeline allows)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"TTRL: Test-Time Reinforcement Learning (NeurIPS 2025)\",\n    \"Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning [DDRL] (ACL 2026 Findings)\",\n    \"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization (arXiv 2025, ByteDance/Nanjing)\",\n    \"Autoformalizer with Tool Feedback [ATF] (arXiv 2025)\",\n    \"ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data (NeurIPS 2025)\",\n    \"Monotonic Reference-Free Refinement for Autoformalization (arXiv 2026)\",\n    \"Olympiad-level formal mathematical reasoning with reinforcement learning [AlphaProof] (Nature 2025)\",\n    \"FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)\",\n    \"Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach (ICLR 2025 Spotlight)\",\n    \"Improving Autoformalization Using Direct Dependency Retrieval [DDR] (arXiv 2025)\",\n    \"DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026)\",\n    \"Automated Formalization via Conceptual Retrieval-Augmented LLMs [CRAMF] (arXiv 2025)\",\n    \"Kimina-Prover Preview: Towards Large Formal Reasoning Models with Reinforcement Learning (arXiv 2025)\",\n    \"Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification (arXiv 2025)\",\n    \"FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)\",\n    \"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion (AAAI 2026)\",\n    \"Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026)\",\n    \"ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (ICLR 2026)\",\n    \"ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (arXiv 2025)\",\n    \"GTED: Generalized Tree Edit Distance—A Faithful Evaluation Metric for Statement Autoformalization (arXiv 2025)\",\n    \"ASSESS: A Semantic and Structural Evaluation Framework for Statement Similarity (arXiv 2025)\"\n  ],\n  \"description\": \"Current autoformalization models achieve strong in-distribution results (ATF: 94.51% Pass@1 on FormalMath-Lite; ATLAS: 96.93% pass@128 on miniF2F) but collapse on unfamiliar mathematical domains due to missing domain-specific formal library dependencies and fixed inference-time behavior. We propose TTRA (Test-Time Retrieval-Augmented autoformalization), the first method unifying dependency-aware retrieval, a trained semantic critic, and debiased test-time reinforcement learning for domain-adaptive autoformalization. Building on a GRPO-trained Qwen3-8B base formalizer, we deploy DDR-style suffix-array-verified dependency retrieval to inject domain-relevant Mathlib definitions at inference time. Unlike prior TTRL work that relies on majority voting (ill-defined for formal statements), we introduce a multi-tier reward: Lean 4 compilation as a binary gate, CriticLeanGPT-14B as a semantic fidelity critic (87% accuracy on CriticLeanBench), and BEq consensus density as a precision-oriented bonus signal. We incorporate DDRL's debiased advantage estimation—replacing GRPO's group-relative normalization (which amplifies noise from ambiguous candidates by up to 58.2%) with fixed ±1 advantages and frequency-based balanced sampling. To break the bootstrapping problem (poor OOD retrieval → bad formalizations → noisy rewards → failed adaptation), we introduce a progressive domain curriculum: warm-start on near-distribution domains where retrieval is reliable, bootstrap improved retrieval queries from adapted models, then transfer to truly OOD domains. This directly targets the ~2.9x quality gap between oracle and model-based retrieval (Oracle* 58.90% vs. DPR 20.08% BEq+@10 on Con-NF, per DRIFT ICLR 2026) while providing the principled reward mechanism that prior TTRL-for-autoformalization attempts lacked. Evaluation spans FormalMATH's multi-domain benchmark, the OOD Con-NF and CombiBench benchmarks, with explicit comparisons against ATF (iterative refinement), ATLAS (SFT-only), Monotonic Refinement (multi-model orchestration), and FormaRL (RL without retrieval). After exhaustive search through May 2026, no prior work combines retrieval augmentation, semantic critic rewards, and debiased test-time RL for autoformalization.\",\n  \"project_name\": \"ttra_critic_guided\",\n  \"source\": \"web_research\",\n  \"reviewer_response\": {\n    \"issue_1_pseudo_reward\": \"ADDRESSED: Replaced vague 'majority-voting consistency' with a concrete multi-tier reward: (1) Lean 4 compilation binary gate, (2) CriticLeanGPT-Qwen3-14B-RL semantic fidelity judgment (87% accuracy, open-source), (3) BEq consensus density among compilable candidates. Weighted combination R = r_compile × (0.7·r_critic + 0.3·r_beq) prioritizes the critic's balanced precision/recall over BEq's high precision but ~33% recall. This is grounded in CriticLean's demonstrated 54%→84% accuracy improvement from adding semantic critique to compilation-only feedback.\",\n    \"issue_2_bootstrapping\": \"ADDRESSED: Introduced a progressive domain curriculum with three stages: (a) near-distribution warm-start where retrieval is reliable, (b) retrieval bootstrapping using the adapted model's improved queries for moderately OOD domains, (c) far-OOD adaptation using the bootstrapped retriever and optionally a critic fine-tuned on verified pairs from stage (b). Each stage's adaptation provides the foundation for the next, breaking the chicken-and-egg cycle.\",\n    \"issue_3_ddrl_spurious_amplification\": \"ADDRESSED: Incorporated DDRL's (ACL 2026 Findings) two-component fix: (1) fixed ±1 advantages replacing GRPO's normalized advantages (severing the amplification pathway where dividing by small std inflates gradients for low-consensus groups), and (2) frequency-based balanced sampling excluding ambiguous candidates. DDRL shows up to 58.2% relative improvement on AIME 2024 from these fixes alone. Also acknowledged concurrent work (T³RL, DCRL, DARE, ECHO) as alternative debiasing strategies.\",\n    \"issue_4_missing_baselines\": \"ADDRESSED: Added ATLAS (NeurIPS 2025, 70.08% pass@1 / 96.93% pass@128 miniF2F — motivates OOD and pass@1 focus), ATF (94.51%/65.38% FormalMath-Lite/CombiBench — strongest iterative refinement baseline, key differentiator is TTRL's weight adaptation vs ATF's frozen policy), CriticLean (critic architecture integrated into our reward), and Monotonic Reference-Free Refinement (100% FV, 90.27% overall miniF2F — inference-time orchestration ceiling). Included iterative self-refinement with compilation feedback as explicit simpler baseline.\",\n    \"issue_5_oracle_numbers\": \"CORRECTED: The 55.36% (BEq@8, Con-NF) is model-based retrieval (+R from RAutoformalizer), not oracle retrieval. Replaced with DRIFT's verified oracle numbers: Oracle* 58.90% vs DPR (RAuto) 20.08% BEq+@10 on Con-NF, a ~2.9x gap. Metrics and attribution are now precise.\",\n    \"issue_6_lean_latency\": \"ADDRESSED: Specified Kimina Lean Server with 128 parallel pre-warmed REPL workers and LRU header caching (1.94x speedup). Concrete throughput: ~3.65s/proof single-worker cached, ~0.10s amortized at 64 workers. Reduced K from 64 to 32 candidates. For K=32, batch=256: ~8,192 verifications/step requiring ~3.9 min at 128 CPUs. CPU costs explicitly budgeted (12,000-35,000 CPU-hours depending on automation level).\",\n    \"issue_7_iclr_deadline\": \"CORRECTED: ICLR 2027 deadline confirmed as unannounced as of May 2026. Listed as tentative with explicit caveat. EACL 2027 ARR deadline corrected to August 3, 2026 (from originally announced August 6).\"\n  }\n}\n\n## Reviewer feedback (round 2)\nIssues: [\"FACTUAL ERROR: The claim 'DDRL shows up to 58.2% relative improvement on AIME 2024' is false. Independent verification via WebFetch of the full DDRL paper (arxiv:2604.21327) confirms the best improvement is 19.0% on AIME 2024 (Qwen2.5-Math-1.5B). The number 58.2% does not appear anywhere in the paper. This error appears in both the reviewer_response and description sections.\", \"INTERNAL INCONSISTENCY: CriticLeanBench accuracy is cited as '87% accuracy on CriticLeanBench' in the description but '84.8% accuracy on CriticLeanBench' in the reviewer_response for CriticLeanGPT-Qwen3-14B-RL. Only one number can be correct.\", \"UNDERSPECIFIED: Progressive curriculum transition criteria are vague. What quantitative conditions trigger progression from stage (a) to (b) to (c)? What happens if near-distribution warm-start produces marginal improvements? The bootstrapping argument is intuitive but the mechanism is not concrete enough to be reproducible.\", \"BEq CONSENSUS DENSITY FRAGILITY: On truly OOD domains (algebraic geometry, condensed mathematics), very few of K=32 candidates will compile, making BEq consensus density (fraction of compilable candidates in same equivalence class) a degenerate signal — likely 0 or 1 for most groups. The multi-tier reward degrades to just r_compile × r_critic on the hardest problems.\", \"DRIFT ALREADY CLOSES THE RETRIEVAL GAP: DRIFT (ICLR 2026) achieves 62.33% BEq+@10 on Con-NF with GPT-4.1, actually surpassing Oracle* (58.90%). This partially undermines the motivation that retrieval is the key bottleneck — if decomposition-based retrieval already exceeds oracle performance, the marginal value of retrieval bootstrapping through TTRL may be limited.\", \"MISSING RECENT BENCHMARK: MathAtlas (arxiv:2605.14061, May 13 2026) introduces 52K graduate-level problems with ~178K dependency relations from 103 textbooks, with best models achieving only 2.6% on the hardest subset. This directly supports the OOD motivation and should be included as an evaluation benchmark.\"]\nFeedback: The proposal has significantly improved from round 1 and the core idea remains strong. Three targeted fixes are needed:\n\n1. **Fix the DDRL numbers**: The 58.2% figure is fabricated. Replace with the actual 19.0% best improvement and 9.2 absolute point gain on AIME 2024 (Qwen2.5-Math-1.5B: 15.8→25.0). The debiasing mechanism itself is still well-motivated — just use accurate numbers. Also fix the CriticLeanBench accuracy inconsistency.\n\n2. **Specify curriculum transition criteria**: Define quantitative thresholds for stage progression. For example: 'Transition from stage (a) to (b) when compilation rate exceeds X% and critic agreement exceeds Y% on the current domain; transition to (c) when retrieval precision on bootstrapped queries reaches Z%.' Also address what happens when BEq consensus density becomes degenerate on hard OOD domains — consider falling back to R = r_compile × r_critic (dropping the BEq term) when fewer than M candidates compile.\n\n3. **Engage with DRIFT's oracle-exceeding result**: DRIFT already surpasses oracle retrieval on Con-NF (62.33% vs 58.90%). Reframe the retrieval contribution: the value isn't just closing the retrieval gap (which DRIFT handles for decomposable statements), but making retrieval *adaptive* to the model's evolving capabilities during TTRL, which static retrieval pipelines like DRIFT cannot do. Also add MathAtlas (May 2026) as an evaluation benchmark — its 178K dependency graph and 2.6% hardest-subset performance directly validates the OOD motivation.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.\n- Address each issue specifically.\n\n## 深度调研要求\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。\n3. **深度思考**：\n   - 核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach？\n4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。\n\n## 针对 Review 意见的定向搜索\n\n1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点\n2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline\n3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现\n4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot\n\n- You have full freedom: minor fix, major revision, or pivot.\n- Include a \"change_type\" field: \"minor\", \"major\", or \"pivot\".\n- Output a COMPLETE JSON object with ALL fields."
}
```

---

### Runtime record

_source line 2 · 2026-05-27T18:16:05.549Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T18:16:05.549Z",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6"
}
```

---

## Round 1

88 recorded events

### User

_source line 3 · 2026-05-27T18:16:05.595Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-27 (UTC).**

## Original idea
{
  "title": "Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization",
  "core_problem": "Current autoformalization models—even those achieving strong in-distribution results (ATF: 94.51% Pass@1 on FormalMath-Lite; ATLAS: 96.93% pass@128 on miniF2F)—degrade sharply on unfamiliar mathematical domains because they lack both domain-specific Mathlib knowledge and mechanisms to adapt at deployment time. Meanwhile, test-time RL (TTRL) has been shown to boost informal math reasoning dramatically but cannot be naively applied to autoformalization: majority voting over formal statements is ill-defined (unlike numerical answers), and GRPO's advantage normalization amplifies noise from ambiguous pseudo-labels. Can we make TTRL viable for autoformalization by combining a trained semantic critic, dependency-aware retrieval, debiased advantage estimation, and progressive domain curriculum?",
  "opportunity": "Three independently validated capabilities have never been combined: (1) Dependency-aware retrieval closes a ~2.9x quality gap—DRIFT reports Oracle* retrieval at 58.90% vs. DPR at 20.08% BEq+@10 on Con-NF (ICLR 2026), confirming domain-specific dependencies are the key bottleneck. (2) TTRL has boosted informal math reasoning by 211% (Qwen-2.5-Math-7B on AIME 2024, NeurIPS 2025), and DDRL's debiased advantage estimation (ACL 2026) fixes the spurious signal amplification problem that otherwise undermines TTRL with noisy pseudo-labels. (3) CriticLean (July 2025) demonstrates that a trained semantic critic raises autoformalization accuracy from 54% to 84% compared to compilation-only feedback, providing the reliable reward signal needed to make RL-based autoformalization work in low-label regimes. Existing strong baselines—ATF's tool-augmented iterative refinement (65.38% Pass@1 on CombiBench) and Monotonic Refinement's multi-model orchestration (90.27% overall on miniF2F)—achieve impressive results but cannot adapt model weights to new domains. Recent infrastructure (DDR's 500K-sample dependency dataset, CRAMF's 26K Mathlib concept index, FormalMATH's multi-domain benchmark, Kimina Lean Server for high-throughput verification, open-source CriticLeanGPT models) makes a critic-guided TTRL approach newly feasible.",
  "landscape": "TTRL (NeurIPS 2025) demonstrated test-time RL for informal math using majority-voting pseudo-labels. DDRL (ACL 2026 Findings) identified that GRPO's group-relative advantage normalization causes spurious signal amplification from ambiguous pseudo-labels, proposing fixed ±1 advantages and frequency-based balanced sampling for debiased test-time RL—yielding up to 58.2% relative improvement on hard math benchmarks. Concurrent work on TTRL debiasing includes T³RL (tool-based verification), DCRL (dual consensus), DARE (distribution-aware reward estimation), and ECHO (entropy-confidence hybrid optimization). AlphaProof (Nature 2025) applies test-time RL to formal proving via variant generation. Kimina-Prover (April 2025) internalizes search via RL for Lean proving, achieving 80.7% pass@8192 on miniF2F. FormaRL (COLM 2025) applies GRPO-based RL to autoformalization using compilation + LLM consistency rewards, improving pass@1 from 4% to 26% on ProofNet. CriticLean (July 2025) introduces a trained semantic critic (CriticLeanGPT) for autoformalization quality evaluation—achieving 87% accuracy on CriticLeanBench and raising pipeline accuracy from 54% to 84% over compilation-only feedback—with open-source models from 8B to 32B parameters. ATLAS (NeurIPS 2025) builds a 300K synthetic NL-FL dataset via iterative augmentation, achieving 96.93% pass@128 and 70.08% pass@1 on miniF2F, demonstrating that high-k sampling nearly solves in-distribution benchmarks but pass@1 remains challenging. ATF/Autoformalizer with Tool Feedback (arXiv 2025) achieves 94.51% Pass@1 on FormalMath-Lite and 65.38% on CombiBench using SFT + expert iteration + DPO with multi-LLM consistency checking—representing the state-of-the-art in iterative refinement without RL weight updates. Monotonic Reference-Free Refinement (January 2026) achieves 100% formal validity and 90.27% composite score on miniF2F through multi-model ensemble orchestration with certified monotonic improvement, but requires 6+ models including GPT-4.1-mini as a judge. DDR (December 2025) builds a 500K-sample dependency retrieval dataset with suffix-array verification. DRIFT (ICLR 2026) decomposes informal statements for targeted retrieval, nearly doubling F1 on ProofNet. CRAMF (2025) indexes 26K+ Mathlib definitions for concept-level retrieval, yielding up to 62.1% relative improvement. Aria (ICLR 2026) uses agentic Graph-of-Thought with dependency decomposition, achieving 68.5% accuracy on ProofNet. ProofBridge (ICLR 2026) combines contrastive joint embeddings with retrieval-augmented fine-tuning for proof autoformalization (+31.14% semantic correctness). ReForm (2026) applies position-aware RL rewards for reflective autoformalization (+22.6pp average). StepFun-Formalizer-32B achieves 40.5% BEq@1 SOTA on FormalMath-Lite via BEq-based majority voting for data curation. FormalEvolve (March 2026) frames autoformalization as test-time neuro-symbolic evolutionary search but without RL. After exhaustive search through May 2026, no work combines (a) retrieval-augmented context, (b) a trained semantic critic for reward computation, and (c) debiased test-time RL adaptation for autoformalization: existing retrieval methods (DDR, DRIFT, CRAMF, Aria) are static pipelines without RL; existing RL methods (FormaRL, ReForm) assume fixed-domain training without retrieval or semantic critic rewards; ATF and Monotonic Refinement use iterative inference without weight updates; existing TTRL applications (AlphaProof, Kimina-Prover) target proof search; and CriticLean provides the critic but not the RL adaptation loop.",
  "inspired_by": "Field guide untried combination: 'Dependency-aware TTRL with semantic critic reward: Combine RAutoformalizer's dependency retrieval + CriticLean's semantic critic + DDRL's debiased advantage estimation + AlphaProof's Test-Time Reinforcement Learning.' Also: gap 'Dependency-aware autoformalization: models are context-blind to formal library contents' + gap 'Pseudo-reward design for formal statement agreement is ill-defined without a trained critic' + pattern 'Test-Time Compute Scaling via Problem-Specific Adaptation' + pattern 'Debiased RL for noisy reward environments.'",
  "approach": "We propose TTRA (Test-Time Retrieval-Augmented autoformalization), a three-phase framework that makes TTRL viable for autoformalization through a multi-tier reward mechanism, debiased advantage estimation, and progressive domain curriculum.\n\n**Phase 1 — Base Formalizer and Critic Training.** Fine-tune a Qwen3-8B base model as a retrieval-augmented autoformalizer using DDR's 500K-sample dependency dataset and FormaRL's GRPO pipeline with a multi-tier reward function R(y, x) = r_compile × (α·r_critic + β·r_beq), where: r_compile ∈ {0,1} is the Lean 4 compilation gate (verified via Kimina Lean Server with 128 parallel pre-warmed REPL workers and LRU header caching); r_critic ∈ {0,1} is the semantic fidelity judgment from CriticLeanGPT-Qwen3-14B-RL (the open-source critic from CriticLean, achieving 84.8% accuracy on CriticLeanBench); r_beq ∈ [0,1] is the BEq consensus density (fraction of compilable candidates in the same BEq equivalence class, computed via Lean's exact? tactic for bidirectional implication). We set α=0.7, β=0.3 to weight semantic fidelity over syntactic consensus, since BEq has high precision (98.6%) but low recall (~33% on ProofNet). This avoids the fundamental problem of majority voting on formal statements by using a trained semantic critic rather than ill-defined agreement measures.\n\n**Phase 2 — Retrieval Module.** Build a domain-adaptive retrieval module that generates candidate Mathlib dependencies via DDR's suffix-array verification and injects retrieved formal definitions into the autoformalization prompt. Train the retriever on DDR's dataset and augment with CRAMF-style concept-level retrieval for broader coverage.\n\n**Phase 3 — Progressive Domain Curriculum for Test-Time Adaptation.** This directly addresses the bootstrapping problem: if retrieval is poor on the target domain, formalizations are wrong, rewards are noisy, and TTRL fails. We break this cycle through a three-stage curriculum:\n  (a) Near-distribution warm-start: Apply TTRL on domains close to training data (e.g., elementary number theory, basic algebra) where retrieval coverage is high and the critic is reliable. Generate K=32 formalization candidates per problem, compute multi-tier rewards, and perform debiased GRPO updates following DDRL: replace GRPO's normalized advantages with fixed +1/-1 values (severing the amplification pathway where dividing by small std inflates gradients for ambiguous groups) and apply frequency-based balanced sampling to exclude ambiguous candidates from the training signal.\n  (b) Retrieval bootstrapping: Use the adapted model from (a) to generate improved retrieval queries for moderately OOD domains (e.g., real analysis, combinatorics). The adapted model produces better formalization attempts that yield more informative retrieval feedback, breaking the chicken-and-egg cycle.\n  (c) Far-OOD adaptation: Apply TTRL on truly OOD domains (algebraic geometry, PDE theory, condensed mathematics) using the bootstrapped retriever and optionally a critic fine-tuned on verified pairs accumulated from stage (b).\n\n**Evaluation.** Measure BEq@K and compilation success on FormalMATH's 5,560-problem multi-domain benchmark, the OOD Con-NF benchmark, and CombiBench. Compare against: (1) ATF-32B as the state-of-the-art iterative refinement baseline (94.51%/65.38% FormalMath-Lite/CombiBench), (2) ATLAS as the strong SFT-only data augmentation baseline (70.08% pass@1 miniF2F), (3) Monotonic Reference-Free Refinement as the inference-time orchestration upper bound (90.27% overall miniF2F), (4) FormaRL as the RL-without-retrieval baseline, (5) compilation-only TTRL and critic-only TTRL ablations, (6) standard GRPO vs. DDRL's debiased advantages, and (7) iterative self-refinement with compilation feedback (ATF-style) as a simpler non-RL baseline. Report per-domain breakdown to quantify adaptation gains across the progressive curriculum.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "1100-1500 A100-80GB hours (base formalizer GRPO training with multi-tier reward: ~350h on 8 GPUs; DDR retriever fine-tuning: ~80h on 4 GPUs; TTRL progressive adaptation across 3 curriculum stages × 5 domains with DDRL debiasing and ablations: ~550h on 4 GPUs; CriticLean critic inference during training: ~80h on 2 GPUs for the 14B critic; evaluation and inference: ~100h) + 12,000-18,000 CPU-hours for Lean 4 verification (128 parallel workers via Kimina Lean Server with LRU caching)",
      "timeline": "14-18 weeks (4 wk base training + critic integration, 2 wk retriever, 5 wk progressive TTRL experiments across curriculum stages, 3-4 wk ablations and writing)",
      "estimated_gpu_cost": "$2,200-$3,800 at ~$2.00/A100-hr + ~$600-$900 CPU verification costs"
    },
    "human_in_loop": {
      "gpu_hours": "900-1200 A100-80GB hours (Claude handles critic evaluation augmentation and data synthesis, reducing CriticLean annotation overhead ~25%) + 10,000-14,000 CPU-hours for Lean verification",
      "timeline": "10-14 weeks (Claude-assisted critic calibration in Phase 1; parallel curriculum experiment management in Phase 3)",
      "claude_api_cost": "$500-$800 (critic reward calibration during GRPO training, synthetic domain-specific formalization examples, automated curriculum scheduling, ablation analysis)",
      "estimated_gpu_cost": "$1,800-$3,000 + ~$500-$700 CPU costs"
    },
    "auto_research": {
      "gpu_hours": "1800-2400 A100-80GB hours (automated hyperparameter sweeps over retrieval top-k, DDRL sampling parameters, critic threshold, GRPO group sizes K ∈ {16,32,64}, curriculum staging boundaries, plus multi-seed evaluation) + 25,000-35,000 CPU-hours for Lean verification at scale",
      "timeline": "7-10 weeks (highly parallelized; wall-clock bottleneck is Lean 4 verification, mitigated by 128+ Kimina Lean Server workers with LRU caching achieving ~0.35s amortized per proof at 32 CPUs, ~0.10s at 64 CPUs)",
      "claude_api_cost": "$900-$1,400 (automated experiment design, reward function ablation analysis, curriculum boundary optimization, paper drafting)",
      "estimated_gpu_cost": "$3,600-$6,000 + ~$1,200-$1,700 CPU costs",
      "speed_bottleneck": "Lean 4 compilation latency (~3.65s per statement with warm LRU cache on single worker; ~0.35s amortized at 32 parallel workers) dominates reward computation. Mitigated with Kimina Lean Server's pre-warmed REPL pool and LRU header caching (1.94x speedup over cold start). For K=32, batch=256: ~4,600 verifications/step requiring ~27 min at 32 CPUs or ~3.9 min at 128 CPUs. CriticLean inference (~14B model) adds ~0.5s per candidate on A100 but runs on GPU in parallel with CPU verification."
    }
  },
  "target_venues": [
    "AAAI 2027 (abstract: July 21, full paper: July 28, 2026 — confirmed)",
    "EACL 2027 via ARR August cycle (submission: August 3, 2026; commitment deadline TBD — confirmed, note corrected from originally announced August 6)",
    "NeurIPS 2026 Workshops (suggested contribution deadline: August 29, 2026 — confirmed; suitable for early results from curriculum stages 1-2)",
    "ICLR 2027 (deadline not yet announced as of May 2026 — best fit for full pipeline results if timeline allows)"
  ],
  "level": "top-tier",
  "key_references": [
    "TTRL: Test-Time Reinforcement Learning (NeurIPS 2025)",
    "Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning [DDRL] (ACL 2026 Findings)",
    "CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization (arXiv 2025, ByteDance/Nanjing)",
    "Autoformalizer with Tool Feedback [ATF] (arXiv 2025)",
    "ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data (NeurIPS 2025)",
    "Monotonic Reference-Free Refinement for Autoformalization (arXiv 2026)",
    "Olympiad-level formal mathematical reasoning with reinforcement learning [AlphaProof] (Nature 2025)",
    "FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)",
    "Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach (ICLR 2025 Spotlight)",
    "Improving Autoformalization Using Direct Dependency Retrieval [DDR] (arXiv 2025)",
    "DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026)",
    "Automated Formalization via Conceptual Retrieval-Augmented LLMs [CRAMF] (arXiv 2025)",
    "Kimina-Prover Preview: Towards Large Formal Reasoning Models with Reinforcement Learning (arXiv 2025)",
    "Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification (arXiv 2025)",
    "FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)",
    "StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion (AAAI 2026)",
    "Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026)",
    "ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (ICLR 2026)",
    "ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (arXiv 2025)",
    "GTED: Generalized Tree Edit Distance—A Faithful Evaluation Metric for Statement Autoformalization (arXiv 2025)",
    "ASSESS: A Semantic and Structural Evaluation Framework for Statement Similarity (arXiv 2025)"
  ],
  "description": "Current autoformalization models achieve strong in-distribution results (ATF: 94.51% Pass@1 on FormalMath-Lite; ATLAS: 96.93% pass@128 on miniF2F) but collapse on unfamiliar mathematical domains due to missing domain-specific formal library dependencies and fixed inference-time behavior. We propose TTRA (Test-Time Retrieval-Augmented autoformalization), the first method unifying dependency-aware retrieval, a trained semantic critic, and debiased test-time reinforcement learning for domain-adaptive autoformalization. Building on a GRPO-trained Qwen3-8B base formalizer, we deploy DDR-style suffix-array-verified dependency retrieval to inject domain-relevant Mathlib definitions at inference time. Unlike prior TTRL work that relies on majority voting (ill-defined for formal statements), we introduce a multi-tier reward: Lean 4 compilation as a binary gate, CriticLeanGPT-14B as a semantic fidelity critic (87% accuracy on CriticLeanBench), and BEq consensus density as a precision-oriented bonus signal. We incorporate DDRL's debiased advantage estimation—replacing GRPO's group-relative normalization (which amplifies noise from ambiguous candidates by up to 58.2%) with fixed ±1 advantages and frequency-based balanced sampling. To break the bootstrapping problem (poor OOD retrieval → bad formalizations → noisy rewards → failed adaptation), we introduce a progressive domain curriculum: warm-start on near-distribution domains where retrieval is reliable, bootstrap improved retrieval queries from adapted models, then transfer to truly OOD domains. This directly targets the ~2.9x quality gap between oracle and model-based retrieval (Oracle* 58.90% vs. DPR 20.08% BEq+@10 on Con-NF, per DRIFT ICLR 2026) while providing the principled reward mechanism that prior TTRL-for-autoformalization attempts lacked. Evaluation spans FormalMATH's multi-domain benchmark, the OOD Con-NF and CombiBench benchmarks, with explicit comparisons against ATF (iterative refinement), ATLAS (SFT-only), Monotonic Refinement (multi-model orchestration), and FormaRL (RL without retrieval). After exhaustive search through May 2026, no prior work combines retrieval augmentation, semantic critic rewards, and debiased test-time RL for autoformalization.",
  "project_name": "ttra_critic_guided",
  "source": "web_research",
  "reviewer_response": {
    "issue_1_pseudo_reward": "ADDRESSED: Replaced vague 'majority-voting consistency' with a concrete multi-tier reward: (1) Lean 4 compilation binary gate, (2) CriticLeanGPT-Qwen3-14B-RL semantic fidelity judgment (87% accuracy, open-source), (3) BEq consensus density among compilable candidates. Weighted combination R = r_compile × (0.7·r_critic + 0.3·r_beq) prioritizes the critic's balanced precision/recall over BEq's high precision but ~33% recall. This is grounded in CriticLean's demonstrated 54%→84% accuracy improvement from adding semantic critique to compilation-only feedback.",
    "issue_2_bootstrapping": "ADDRESSED: Introduced a progressive domain curriculum with three stages: (a) near-distribution warm-start where retrieval is reliable, (b) retrieval bootstrapping using the adapted model's improved queries for moderately OOD domains, (c) far-OOD adaptation using the bootstrapped retriever and optionally a critic fine-tuned on verified pairs from stage (b). Each stage's adaptation provides the foundation for the next, breaking the chicken-and-egg cycle.",
    "issue_3_ddrl_spurious_amplification": "ADDRESSED: Incorporated DDRL's (ACL 2026 Findings) two-component fix: (1) fixed ±1 advantages replacing GRPO's normalized advantages (severing the amplification pathway where dividing by small std inflates gradients for low-consensus groups), and (2) frequency-based balanced sampling excluding ambiguous candidates. DDRL shows up to 58.2% relative improvement on AIME 2024 from these fixes alone. Also acknowledged concurrent work (T³RL, DCRL, DARE, ECHO) as alternative debiasing strategies.",
    "issue_4_missing_baselines": "ADDRESSED: Added ATLAS (NeurIPS 2025, 70.08% pass@1 / 96.93% pass@128 miniF2F — motivates OOD and pass@1 focus), ATF (94.51%/65.38% FormalMath-Lite/CombiBench — strongest iterative refinement baseline, key differentiator is TTRL's weight adaptation vs ATF's frozen policy), CriticLean (critic architecture integrated into our reward), and Monotonic Reference-Free Refinement (100% FV, 90.27% overall miniF2F — inference-time orchestration ceiling). Included iterative self-refinement with compilation feedback as explicit simpler baseline.",
    "issue_5_oracle_numbers": "CORRECTED: The 55.36% (BEq@8, Con-NF) is model-based retrieval (+R from RAutoformalizer), not oracle retrieval. Replaced with DRIFT's verified oracle numbers: Oracle* 58.90% vs DPR (RAuto) 20.08% BEq+@10 on Con-NF, a ~2.9x gap. Metrics and attribution are now precise.",
    "issue_6_lean_latency": "ADDRESSED: Specified Kimina Lean Server with 128 parallel pre-warmed REPL workers and LRU header caching (1.94x speedup). Concrete throughput: ~3.65s/proof single-worker cached, ~0.10s amortized at 64 workers. Reduced K from 64 to 32 candidates. For K=32, batch=256: ~8,192 verifications/step requiring ~3.9 min at 128 CPUs. CPU costs explicitly budgeted (12,000-35,000 CPU-hours depending on automation level).",
    "issue_7_iclr_deadline": "CORRECTED: ICLR 2027 deadline confirmed as unannounced as of May 2026. Listed as tentative with explicit caveat. EACL 2027 ARR deadline corrected to August 3, 2026 (from originally announced August 6)."
  }
}

## Reviewer feedback (round 2)
Issues: ["FACTUAL ERROR: The claim 'DDRL shows up to 58.2% relative improvement on AIME 2024' is false. Independent verification via WebFetch of the full DDRL paper (arxiv:2604.21327) confirms the best improvement is 19.0% on AIME 2024 (Qwen2.5-Math-1.5B). The number 58.2% does not appear anywhere in the paper. This error appears in both the reviewer_response and description sections.", "INTERNAL INCONSISTENCY: CriticLeanBench accuracy is cited as '87% accuracy on CriticLeanBench' in the description but '84.8% accuracy on CriticLeanBench' in the reviewer_response for CriticLeanGPT-Qwen3-14B-RL. Only one number can be correct.", "UNDERSPECIFIED: Progressive curriculum transition criteria are vague. What quantitative conditions trigger progression from stage (a) to (b) to (c)? What happens if near-distribution warm-start produces marginal improvements? The bootstrapping argument is intuitive but the mechanism is not concrete enough to be reproducible.", "BEq CONSENSUS DENSITY FRAGILITY: On truly OOD domains (algebraic geometry, condensed mathematics), very few of K=32 candidates will compile, making BEq consensus density (fraction of compilable candidates in same equivalence class) a degenerate signal — likely 0 or 1 for most groups. The multi-tier reward degrades to just r_compile × r_critic on the hardest problems.", "DRIFT ALREADY CLOSES THE RETRIEVAL GAP: DRIFT (ICLR 2026) achieves 62.33% BEq+@10 on Con-NF with GPT-4.1, actually surpassing Oracle* (58.90%). This partially undermines the motivation that retrieval is the key bottleneck — if decomposition-based retrieval already exceeds oracle performance, the marginal value of retrieval bootstrapping through TTRL may be limited.", "MISSING RECENT BENCHMARK: MathAtlas (arxiv:2605.14061, May 13 2026) introduces 52K graduate-level problems with ~178K dependency relations from 103 textbooks, with best models achieving only 2.6% on the hardest subset. This directly supports the OOD motivation and should be included as an evaluation benchmark."]
Feedback: The proposal has significantly improved from round 1 and the core idea remains strong. Three targeted fixes are needed:

1. **Fix the DDRL numbers**: The 58.2% figure is fabricated. Replace with the actual 19.0% best improvement and 9.2 absolute point gain on AIME 2024 (Qwen2.5-Math-1.5B: 15.8→25.0). The debiasing mechanism itself is still well-motivated — just use accurate numbers. Also fix the CriticLeanBench accuracy inconsistency.

2. **Specify curriculum transition criteria**: Define quantitative thresholds for stage progression. For example: 'Transition from stage (a) to (b) when compilation rate exceeds X% and critic agreement exceeds Y% on the current domain; transition to (c) when retrieval precision on bootstrapped queries reaches Z%.' Also address what happens when BEq consensus density becomes degenerate on hard OOD domains — consider falling back to R = r_compile × r_critic (dropping the BEq term) when fewer than M candidates compile.

3. **Engage with DRIFT's oracle-exceeding result**: DRIFT already surpasses oracle retrieval on Con-NF (62.33% vs 58.90%). Reframe the retrieval contribution: the value isn't just closing the retrieval gap (which DRIFT handles for decomposable statements), but making retrieval *adaptive* to the model's evolving capabilities during TTRL, which static retrieval pipelines like DRIFT cannot do. Also add MathAtlas (May 2026) as an evaluation benchmark — its 178K dependency graph and 2.6% hardest-subset performance directly validates the OOD motivation.

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
  "promptId": "4b0c0804-0c80-4fc4-bd2d-54c91b4a93a7",
  "type": "user",
  "uuid": "f8e900b2-7f07-4440-9c32-4d2c52a49b95",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T18:16:05.594Z_

```json
{
  "parentUuid": "f8e900b2-7f07-4440-9c32-4d2c52a49b95",
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
  "uuid": "f09e1078-72ec-4537-9a94-05e1912926f3",
  "timestamp": "2026-05-27T18:16:05.594Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T18:16:05.594Z_

```json
{
  "parentUuid": "f09e1078-72ec-4537-9a94-05e1912926f3",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9111ced8-b00b-4db3-85d8-d6d9c3026c28",
  "timestamp": "2026-05-27T18:16:05.594Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Aut…",
  "leafUuid": "9111ced8-b00b-4db3-85d8-d6d9c3026c28",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise autoformalization TTRL paper with verified data and concrete curriculum",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6"
}
```

---

### Assistant

_source line 8 · 2026-05-27T18:16:15.854Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully and plan my research accordingly.

The reviewer has 6 issues:

1. **FACTUAL ERROR**: DDRL 58.2% claim is fabricated. Actual best is 19.0% on AIME 2024. Need to verify the actual numbers.
2. **INTERNAL INCONSISTENCY**: CriticLeanBench accuracy - 87% vs 84.8%. Need to verify which is correct.
3. **UNDERSPECIFIED**: Progressive curriculum transition criteria need quantitative thresholds.


4. **BEq CONSENSUS DENSITY FRAGILITY**: On hard OOD domains, BEq becomes degenerate and needs clarification on when this occurs.
5. **DRIFT ALREADY CLOSES THE RETRIEVAL GAP**: DRIFT surpasses oracle retrieval (62.33% vs 58.90%), which undermines the retrieval bottleneck motivation for the work.
6. **MISSING RECENT BENCHMARK**: MathAtlas (arxiv:2605.14061) should be included in the evaluation.

The reviewer's summary indicates three targeted fixes are needed: correct the DDRL and CriticLeanBench numbers, specify quantitative curriculum transition criteria and address BEq degeneracy, and handle the DRIFT retrieval gap issue.

Now I need to dig into the source papers to resolve these issues—I'll pull the DDRL and CriticLean papers to verify the accuracy numbers, examine DRIFT's oracle-exceeding result to understand how it's possible, check MathAtlas to see if it's relevant, and think through what curriculum transition criteria would make sense and when BEq actually breaks down.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9111ced8-b00b-4db3-85d8-d6d9c3026c28",
  "isSidechain": false,
  "requestId": "req_011CbTXji7H6WbGBTVbvTfc3",
  "type": "assistant",
  "uuid": "dad29ee6-f9fa-4f2f-a2f4-a76480cce698",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UavCNEjHRz7ATwJrSKx1Mt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9025,
      "cache_read_input_tokens": 11014,
      "output_tokens": 529,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9025,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 529,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 9025,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9025
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

_source line 9 · 2026-05-27T18:16:15.856Z_

I'll start by doing deep research on each issue the reviewer flagged. Let me fetch the key papers to verify facts and understand the landscape properly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dad29ee6-f9fa-4f2f-a2f4-a76480cce698",
  "isSidechain": false,
  "requestId": "req_011CbTXji7H6WbGBTVbvTfc3",
  "type": "assistant",
  "uuid": "5fd41f6d-afee-4670-849a-3844cbb45942",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UavCNEjHRz7ATwJrSKx1Mt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9025,
      "cache_read_input_tokens": 11014,
      "output_tokens": 529,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9025,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 529,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 9025,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9025
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

_source line 10 · 2026-05-27T18:16:15.865Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019YzqyFMuBMPUdUGkFNZ7Bf`</summary>

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
  "parentUuid": "5fd41f6d-afee-4670-849a-3844cbb45942",
  "isSidechain": false,
  "requestId": "req_011CbTXji7H6WbGBTVbvTfc3",
  "type": "assistant",
  "uuid": "db95703b-d41b-4900-92a4-c8d24c3dd3f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UavCNEjHRz7ATwJrSKx1Mt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9025,
      "cache_read_input_tokens": 11014,
      "output_tokens": 529,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9025,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 529,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 9025,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9025
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

_source line 11 · 2026-05-27T18:16:15.872Z_

<details><summary>↩ Tool result · `toolu_019YzqyFMuBMPUdUGkFNZ7Bf`</summary>

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
  "parentUuid": "db95703b-d41b-4900-92a4-c8d24c3dd3f5",
  "isSidechain": false,
  "promptId": "4b0c0804-0c80-4fc4-bd2d-54c91b4a93a7",
  "type": "user",
  "uuid": "a1d53bc2-a344-4a66-b8e7-5a62e22814f1",
  "toolUseResult": {
    "matches": [
      "WebFetch",
      "WebSearch"
    ],
    "query": "select:WebFetch,WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "db95703b-d41b-4900-92a4-c8d24c3dd3f5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-27T18:16:18.762Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the key papers in parallel to verify the facts and gather information.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1d53bc2-a344-4a66-b8e7-5a62e22814f1",
  "isSidechain": false,
  "requestId": "req_011CbTXkUF8PhbbDQ98vUVxj",
  "type": "assistant",
  "uuid": "df3c478f-0529-4d65-885c-87279b2ee11c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNcMWusiTwjtrXAp8vCtsZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1549,
      "cache_read_input_tokens": 20039,
      "output_tokens": 616,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1549,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 616,
          "cache_read_input_tokens": 20039,
          "cache_creation_input_tokens": 1549,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1549
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

_source line 13 · 2026-05-27T18:16:18.763Z_

Now let me fetch the key papers in parallel to verify all the facts.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df3c478f-0529-4d65-885c-87279b2ee11c",
  "isSidechain": false,
  "requestId": "req_011CbTXkUF8PhbbDQ98vUVxj",
  "type": "assistant",
  "uuid": "be3895d9-543b-4379-94e6-ab5cc5316cce",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNcMWusiTwjtrXAp8vCtsZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1549,
      "cache_read_input_tokens": 20039,
      "output_tokens": 616,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1549,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 616,
          "cache_read_input_tokens": 20039,
          "cache_creation_input_tokens": 1549,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1549
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

_source line 14 · 2026-05-27T18:16:21.612Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_018yVkSmtP2J5umTTpuyCCeG`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.21327",
  "prompt": "Extract the FULL results table for DDRL. I need: 1) The exact relative improvement percentages on AIME 2024 for each model size. 2) The exact absolute scores (before and after DDRL). 3) Any mention of \"58.2%\" anywhere in the paper. 4) The best improvement number they report. 5) The exact method names (fixed advantages, balanced sampling, etc.) and their individual contributions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be3895d9-543b-4379-94e6-ab5cc5316cce",
  "isSidechain": false,
  "requestId": "req_011CbTXkUF8PhbbDQ98vUVxj",
  "type": "assistant",
  "uuid": "19fc632c-6f69-48cd-8fe7-0846278bb8e5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNcMWusiTwjtrXAp8vCtsZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1549,
      "cache_read_input_tokens": 20039,
      "output_tokens": 616,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1549,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 616,
          "cache_read_input_tokens": 20039,
          "cache_creation_input_tokens": 1549,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1549
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

_source line 15 · 2026-05-27T18:16:24.411Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01TnXgeqZWiZgRkBhBaHFz9Z`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.CriticLean",
  "prompt": "Find the CriticLean paper about critic-guided reinforcement learning for mathematical formalization. Extract: 1) CriticLeanBench accuracy for each model variant (8B, 14B, 32B). 2) The specific accuracy for CriticLeanGPT-Qwen3-14B-RL. 3) The pipeline accuracy improvement (54% to 84% claim). 4) Any accuracy numbers that are 87% or 84.8%."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "19fc632c-6f69-48cd-8fe7-0846278bb8e5",
  "isSidechain": false,
  "requestId": "req_011CbTXkUF8PhbbDQ98vUVxj",
  "type": "assistant",
  "uuid": "8c612ef6-7eee-4d74-8b65-b594ec935b17",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNcMWusiTwjtrXAp8vCtsZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1549,
      "cache_read_input_tokens": 20039,
      "output_tokens": 616,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1549,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 616,
          "cache_read_input_tokens": 20039,
          "cache_creation_input_tokens": 1549,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1549
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

_source line 16 · 2026-05-27T18:16:24.668Z_

<details><summary>↩ Tool result · `toolu_01TnXgeqZWiZgRkBhBaHFz9Z`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c612ef6-7eee-4d74-8b65-b594ec935b17",
  "isSidechain": false,
  "promptId": "4b0c0804-0c80-4fc4-bd2d-54c91b4a93a7",
  "type": "user",
  "uuid": "e9a9571c-a0a8-45af-8199-fa987638e399",
  "toolUseResult": {
    "bytes": 0,
    "code": 404,
    "codeText": "Not Found",
    "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 254,
    "url": "https://arxiv.org/abs/2505.CriticLean"
  },
  "sourceToolAssistantUUID": "8c612ef6-7eee-4d74-8b65-b594ec935b17",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-27T18:16:25.142Z_

<details><summary>↩ Tool result · `toolu_018yVkSmtP2J5umTTpuyCCeG`</summary>

```text
# Response

Based on the provided webpage content, I cannot extract the requested information. The page contains only the abstract and metadata for the arXiv paper (arXiv:2604.21327), not the full results tables.

The abstract mentions that "DDRL consistently outperforms existing TTRL baselines" across benchmarks, but does not include:

- Specific AIME 2024 improvement percentages
- Absolute scores before/after DDRL
- The figure "58.2%"
- Individual component contributions

**To obtain this data, you would need to access the full PDF or HTML version** of the paper using the links provided on the page ([View PDF](/pdf/2604.21327) or [HTML (experimental)](https://arxiv.org/html/2604.21327v1)).

The abstract only confirms the methodology includes: "frequency-based sampling strategy," "debiased advantage estimation with fixed advantages," and "consensus-based off-policy refinement."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "19fc632c-6f69-48cd-8fe7-0846278bb8e5",
  "isSidechain": false,
  "promptId": "4b0c0804-0c80-4fc4-bd2d-54c91b4a93a7",
  "type": "user",
  "uuid": "f1978174-f27d-4f97-8d23-8b2c7722c061",
  "toolUseResult": {
    "bytes": 48386,
    "code": 200,
    "codeText": "OK",
    "result": "# Response\n\nBased on the provided webpage content, I cannot extract the requested information. The page contains only the abstract and metadata for the arXiv paper (arXiv:2604.21327), not the full results tables.\n\nThe abstract mentions that \"DDRL consistently outperforms existing TTRL baselines\" across benchmarks, but does not include:\n\n- Specific AIME 2024 improvement percentages\n- Absolute scores before/after DDRL\n- The figure \"58.2%\"\n- Individual component contributions\n\n**To obtain this data, you would need to access the full PDF or HTML version** of the paper using the links provided on the page ([View PDF](/pdf/2604.21327) or [HTML (experimental)](https://arxiv.org/html/2604.21327v1)).\n\nThe abstract only confirms the methodology includes: \"frequency-based sampling strategy,\" \"debiased advantage estimation with fixed advantages,\" and \"consensus-based off-policy refinement.\"",
    "durationMs": 3526,
    "url": "https://arxiv.org/abs/2604.21327"
  },
  "sourceToolAssistantUUID": "19fc632c-6f69-48cd-8fe7-0846278bb8e5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-27T18:16:26.290Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017NPX7ueWnzSii7RrKbwyKG`</summary>

```json
{
  "url": "https://arxiv.org/abs/2605.14061",
  "prompt": "Extract all key information about MathAtlas: 1) Total number of problems and dependency relations. 2) Number of textbooks. 3) Performance of best models on hardest subset (the 2.6% claim). 4) Domain coverage. 5) How dependencies are structured. 6) Evaluation metrics used. 7) Key findings about model performance across difficulty levels."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f1978174-f27d-4f97-8d23-8b2c7722c061",
  "isSidechain": false,
  "requestId": "req_011CbTXkUF8PhbbDQ98vUVxj",
  "type": "assistant",
  "uuid": "15aba9a8-a9a7-45f4-9a15-c45594a53a8c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNcMWusiTwjtrXAp8vCtsZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1549,
      "cache_read_input_tokens": 20039,
      "output_tokens": 616,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1549,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 616,
          "cache_read_input_tokens": 20039,
          "cache_creation_input_tokens": 1549,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1549
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

_source line 19 · 2026-05-27T18:16:27.079Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LC3ep7SERnHJ15oFmSbuE5`</summary>

```json
{
  "query": "DDRL \"spurious signal amplification\" test-time reinforcement learning ACL 2026 arxiv 2604.21327"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15aba9a8-a9a7-45f4-9a15-c45594a53a8c",
  "isSidechain": false,
  "requestId": "req_011CbTXkUF8PhbbDQ98vUVxj",
  "type": "assistant",
  "uuid": "09b27913-be2d-4070-a5b1-474dbad2b8dc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNcMWusiTwjtrXAp8vCtsZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1549,
      "cache_read_input_tokens": 20039,
      "output_tokens": 616,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1549,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 616,
          "cache_read_input_tokens": 20039,
          "cache_creation_input_tokens": 1549,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1549
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

_source line 20 · 2026-05-27T18:16:30.613Z_

<details><summary>↩ Tool result · `toolu_017NPX7ueWnzSii7RrKbwyKG`</summary>

```text
# MathAtlas Benchmark: Key Information

**1) Scale of Dataset:**
The benchmark contains "~52k theorems, definitions, exercises, examples, and proofs" with "~178k relations" in its dependency graph.

**2) Source Material:**
Data was extracted from 103 graduate mathematics textbooks.

**3) Performance on Hardest Subset:**
On MA-Hard (700 entities with deepest dependency trees), the leading model achieved only 2.6% correctness for autoformalization tasks.

**4) Domain Coverage:**
The benchmark focuses on graduate-level mathematics "in the wild," representing research-level content previously underexplored in autoformalization benchmarks.

**5) Dependency Structure:**
This is "the first autoformalization benchmark to include" mathematical dependency relations, enabling development of systems that account for these connections.

**6) Evaluation Metrics:**
Models were assessed on correctness rates for theorem statements and definitions, with state-of-the-art baselines reaching at most 9.8% correctness on theorems and 16.7% on definitions.

**7) Key Performance Findings:**
A critical observation is that "performance of state-of-the-art models degrades substantially with dependency depth," showing the benchmark's challenge level increases with structural complexity.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15aba9a8-a9a7-45f4-9a15-c45594a53a8c",
  "isSidechain": false,
  "promptId": "4b0c0804-0c80-4fc4-bd2d-54c91b4a93a7",
  "type": "user",
  "uuid": "582b817b-a09a-45a7-9ed6-e7efac99f6fa",
  "toolUseResult": {
    "bytes": 47274,
    "code": 200,
    "codeText": "OK",
    "result": "# MathAtlas Benchmark: Key Information\n\n**1) Scale of Dataset:**\nThe benchmark contains \"~52k theorems, definitions, exercises, examples, and proofs\" with \"~178k relations\" in its dependency graph.\n\n**2) Source Material:**\nData was extracted from 103 graduate mathematics textbooks.\n\n**3) Performance on Hardest Subset:**\nOn MA-Hard (700 entities with deepest dependency trees), the leading model achieved only 2.6% correctness for autoformalization tasks.\n\n**4) Domain Coverage:**\nThe benchmark focuses on graduate-level mathematics \"in the wild,\" representing research-level content previously underexplored in autoformalization benchmarks.\n\n**5) Dependency Structure:**\nThis is \"the first autoformalization benchmark to include\" mathematical dependency relations, enabling development of systems that account for these connections.\n\n**6) Evaluation Metrics:**\nModels were assessed on correctness rates for theorem statements and definitions, with state-of-the-art baselines reaching at most 9.8% correctness on theorems and 16.7% on definitions.\n\n**7) Key Performance Findings:**\nA critical observation is that \"performance of state-of-the-art models degrades substantially with dependency depth,\" showing the benchmark's challenge level increases with structural complexity.",
    "durationMs": 4320,
    "url": "https://arxiv.org/abs/2605.14061"
  },
  "sourceToolAssistantUUID": "15aba9a8-a9a7-45f4-9a15-c45594a53a8c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-27T18:16:33.712Z_

<details><summary>↩ Tool result · `toolu_01LC3ep7SERnHJ15oFmSbuE5`</summary>

```text
Web search results for query: "DDRL "spurious signal amplification" test-time reinforcement learning ACL 2026 arxiv 2604.21327"

Links: [{"title":"[2604.21327] Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning","url":"https://arxiv.org/abs/2604.21327"},{"title":"Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning","url":"https://arxiv.org/html/2604.21327"},{"title":"Amplification Effects in Test-Time Reinforcement Learning: Safety and Reasoning Vulnerabilities","url":"https://arxiv.org/pdf/2603.15417"},{"title":"What If Consensus Lies? Selective-Complementary Reinforcement Learning at Test Time","url":"https://arxiv.org/pdf/2603.19880"},{"title":"Tool Verification for Test-Time Reinforcement Learning","url":"https://arxiv.org/pdf/2603.02203"},{"title":"Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning","url":"https://arxiv.org/pdf/2512.15146"}]

Based on the search results, I found the paper you're looking for. Here's what I found:

Test-time reinforcement learning (TTRL) always adapts models at inference time via pseudo-labeling, leaving it vulnerable to spurious optimization signals from label noise. 

The paper proposes a unified framework called Debiased and Denoised test-time Reinforcement Learning (DDRL), to mitigate spurious signals. The framework has three key components:

1. DDRL first applies a frequency-based sampling strategy to exclude ambiguous samples while maintaining a balanced set of positive and negative examples.

2. It then adopts a debiased advantage estimation with fixed advantages, removing the bias introduced by group-relative policy optimization.

3. Finally, DDRL incorporates a consensus-based off-policy refinement stage, which leverages the rejection-sampled dataset to enable efficient and stable model updates.

Experiments on three large language models across multiple mathematical reasoning benchmarks demonstrate that DDRL consistently outperforms existing TTRL baselines. The paper was submitted to arXiv on April 23, 2026 with ID 2604.21327.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09b27913-be2d-4070-a5b1-474dbad2b8dc",
  "isSidechain": false,
  "promptId": "4b0c0804-0c80-4fc4-bd2d-54c91b4a93a7",
  "type": "user",
  "uuid": "2cc2fb3a-1850-420c-bfb3-e04180100ee0",
  "toolUseResult": {
    "query": "DDRL \"spurious signal amplification\" test-time reinforcement learning ACL 2026 arxiv 2604.21327",
    "results": [
      {
        "tool_use_id": "srvtoolu_015eEunRacd3P4U4uQmACXJg",
        "content": [
          {
            "title": "[2604.21327] Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning",
            "url": "https://arxiv.org/abs/2604.21327"
          },
          {
            "title": "Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning",
            "url": "https://arxiv.org/html/2604.21327"
          },
          {
            "title": "Amplification Effects in Test-Time Reinforcement Learning: Safety and Reasoning Vulnerabilities",
            "url": "https://arxiv.org/pdf/2603.15417"
          },
          {
            "title": "What If Consensus Lies? Selective-Complementary Reinforcement Learning at Test Time",
            "url": "https://arxiv.org/pdf/2603.19880"
          },
          {
            "title": "Tool Verification for Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2603.02203"
          },
          {
            "title": "Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2512.15146"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's what I found:\n\nTest-time reinforcement learning (TTRL) always adapts models at inference time via pseudo-labeling, leaving it vulnerable to spurious optimization signals from label noise. \n\nThe paper proposes a unified framework called Debiased and Denoised test-time Reinforcement Learning (DDRL), to mitigate spurious signals. The framework has three key components:\n\n1. DDRL first applies a frequency-based sampling strategy to exclude ambiguous samples while maintaining a balanced set of positive and negative examples.\n\n2. It then adopts a debiased advantage estimation with fixed advantages, removing the bias introduced by group-relative policy optimization.\n\n3. Finally, DDRL incorporates a consensus-based off-policy refinement stage, which leverages the rejection-sampled dataset to enable efficient and stable model updates.\n\nExperiments on three large language models across multiple mathematical reasoning benchmarks demonstrate that DDRL consistently outperforms existing TTRL baselines. The paper was submitted to arXiv on April 23, 2026 with ID 2604.21327."
    ],
    "durationSeconds": 6.626985349999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "09b27913-be2d-4070-a5b1-474dbad2b8dc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-27T18:16:36.474Z_

<details><summary>Logged reasoning block</summary>

```text
I need to get the full DDRL paper to extract exact numbers. Let me also search for the CriticLean paper properly and fetch the DRIFT paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2cc2fb3a-1850-420c-bfb3-e04180100ee0",
  "isSidechain": false,
  "requestId": "req_011CbTXmnEdcRyKiD4NT6p4h",
  "type": "assistant",
  "uuid": "2895cc8d-c265-455a-a3e5-e2b6d688b49d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuZptkiPtEW71b3ejRJrwX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1867,
      "cache_read_input_tokens": 21588,
      "output_tokens": 396,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1867,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 396,
          "cache_read_input_tokens": 21588,
          "cache_creation_input_tokens": 1867,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1867
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

_source line 23 · 2026-05-27T18:16:36.987Z_

Let me fetch the full papers to get exact numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2895cc8d-c265-455a-a3e5-e2b6d688b49d",
  "isSidechain": false,
  "requestId": "req_011CbTXmnEdcRyKiD4NT6p4h",
  "type": "assistant",
  "uuid": "28e98fa4-29b2-4609-a7d3-e36ef1445c5b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuZptkiPtEW71b3ejRJrwX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1867,
      "cache_read_input_tokens": 21588,
      "output_tokens": 396,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1867,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 396,
          "cache_read_input_tokens": 21588,
          "cache_creation_input_tokens": 1867,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1867
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

_source line 24 · 2026-05-27T18:16:39.903Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RhUHyP3YUoNdGRUygMY8MB`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.21327",
  "prompt": "Extract ALL results tables from this paper. I need: 1) The exact scores on AIME 2024 for each model (Qwen2.5-Math-1.5B, 7B, etc.) both before and after DDRL. 2) All relative improvement percentages reported. 3) Whether \"58.2%\" appears anywhere. 4) Results on MATH-500 and any other benchmarks. 5) The breakdown of individual component contributions (fixed advantages alone, balanced sampling alone, etc.). 6) The best single improvement number they highlight."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "28e98fa4-29b2-4609-a7d3-e36ef1445c5b",
  "isSidechain": false,
  "requestId": "req_011CbTXmnEdcRyKiD4NT6p4h",
  "type": "assistant",
  "uuid": "c2c57edb-20b3-40d9-902c-6c5a8dc3bd42",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuZptkiPtEW71b3ejRJrwX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1867,
      "cache_read_input_tokens": 21588,
      "output_tokens": 396,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1867,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 396,
          "cache_read_input_tokens": 21588,
          "cache_creation_input_tokens": 1867,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1867
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

_source line 25 · 2026-05-27T18:16:40.843Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MovMcRvtkZwVe1hwFeBh5y`</summary>

```json
{
  "query": "CriticLean critic-guided reinforcement learning mathematical formalization CriticLeanBench accuracy arxiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2c57edb-20b3-40d9-902c-6c5a8dc3bd42",
  "isSidechain": false,
  "requestId": "req_011CbTXmnEdcRyKiD4NT6p4h",
  "type": "assistant",
  "uuid": "f9761040-1bb6-401b-b0a1-adb73e5f1a1b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuZptkiPtEW71b3ejRJrwX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1867,
      "cache_read_input_tokens": 21588,
      "output_tokens": 396,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1867,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 396,
          "cache_read_input_tokens": 21588,
          "cache_creation_input_tokens": 1867,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1867
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

_source line 26 · 2026-05-27T18:16:41.504Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018nZwGHqmcVfVXRM8Zgihuc`</summary>

```json
{
  "query": "DRIFT decompose retrieve formalize theorems ICLR 2026 Con-NF oracle retrieval 62.33% BEq"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9761040-1bb6-401b-b0a1-adb73e5f1a1b",
  "isSidechain": false,
  "requestId": "req_011CbTXmnEdcRyKiD4NT6p4h",
  "type": "assistant",
  "uuid": "2cd166f5-5540-4fe6-9b85-2e3aef3a3513",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuZptkiPtEW71b3ejRJrwX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1867,
      "cache_read_input_tokens": 21588,
      "output_tokens": 396,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1867,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 396,
          "cache_read_input_tokens": 21588,
          "cache_creation_input_tokens": 1867,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1867
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

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Aut…",
  "leafUuid": "2cd166f5-5540-4fe6-9b85-2e3aef3a3513",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise autoformalization TTRL paper with verified data and concrete curriculum",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6"
}
```

---

### Tool result

_source line 29 · 2026-05-27T18:16:46.222Z_

<details><summary>↩ Tool result · `toolu_01MovMcRvtkZwVe1hwFeBh5y`</summary>

```text
Web search results for query: "CriticLean critic-guided reinforcement learning mathematical formalization CriticLeanBench accuracy arxiv 2025"

Links: [{"title":"[2507.06181v1] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://arxiv.org/abs/2507.06181v1"},{"title":"[2507.06181] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://arxiv.org/abs/2507.06181"},{"title":"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/criticlean-critic-guided-reinforcement-learning-mathematical-formalization"},{"title":"(PDF) CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://www.researchgate.net/publication/393512361_CriticLean_Critic-Guided_Reinforcement_Learning_for_Mathematical_Formalization"},{"title":"m-a-p/CriticLeanBench · Datasets at Hugging Face","url":"https://huggingface.co/datasets/m-a-p/CriticLeanBench"},{"title":"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://openreview.net/pdf/604b63db1bbddb963505ecbeca441f5b94bd143c.pdf"},{"title":"Paper page - CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://huggingface.co/papers/2507.06181"}]

Based on the search results, here's what I found about CriticLean:

## Overview

CriticLean is a novel critic-guided reinforcement learning framework that elevates the role of the critic from a passive validator to an active learning component. The work addresses the fundamental challenge of translating natural language mathematical statements into formal, executable code for automated theorem proving, focusing on the critic phase—the evaluation of whether generated formalizations truly capture the semantic intent of the original problem.

## Key Components

CriticLeanGPT is trained via supervised fine-tuning and reinforcement learning to rigorously assess the semantic fidelity of Lean 4 formalizations.

CriticLeanBench is a benchmark containing 500 natural language and Lean 4 language statement pairs (250 correct and 250 incorrect). Models trained via CriticLean can significantly outperform strong open- and closed-source baselines on this benchmark.

## Dataset

FineLeanCorpus is a dataset comprising over 285K problems that exhibits rich domain diversity, broad difficulty coverage, and high correctness based on human evaluation.

The paper (arxiv 2507.06181) was published in July 2025 and demonstrates that optimizing the critic phase is essential for producing reliable mathematical formalizations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9761040-1bb6-401b-b0a1-adb73e5f1a1b",
  "isSidechain": false,
  "promptId": "4b0c0804-0c80-4fc4-bd2d-54c91b4a93a7",
  "type": "user",
  "uuid": "af531143-e44f-435e-ba33-e5bb35137f6d",
  "toolUseResult": {
    "query": "CriticLean critic-guided reinforcement learning mathematical formalization CriticLeanBench accuracy arxiv 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_015vUj84zBf18aCa2qUAR2s8",
        "content": [
          {
            "title": "[2507.06181v1] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization",
            "url": "https://arxiv.org/abs/2507.06181v1"
          },
          {
            "title": "[2507.06181] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization",
            "url": "https://arxiv.org/abs/2507.06181"
          },
          {
            "title": "CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/criticlean-critic-guided-reinforcement-learning-mathematical-formalization"
          },
          {
            "title": "(PDF) CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization",
            "url": "https://www.researchgate.net/publication/393512361_CriticLean_Critic-Guided_Reinforcement_Learning_for_Mathematical_Formalization"
          },
          {
            "title": "m-a-p/CriticLeanBench · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/m-a-p/CriticLeanBench"
          },
          {
            "title": "CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization",
            "url": "https://openreview.net/pdf/604b63db1bbddb963505ecbeca441f5b94bd143c.pdf"
          },
          {
            "title": "Paper page - CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization",
            "url": "https://huggingface.co/papers/2507.06181"
          }
        ]
      },
      "Based on the search results, here's what I found about CriticLean:\n\n## Overview\n\nCriticLean is a novel critic-guided reinforcement learning framework that elevates the role of the critic from a passive validator to an active learning component. The work addresses the fundamental challenge of translating natural language mathematical statements into formal, executable code for automated theorem proving, focusing on the critic phase—the evaluation of whether generated formalizations truly capture the semantic intent of the original problem.\n\n## Key Components\n\nCriticLeanGPT is trained via supervised fine-tuning and reinforcement learning to rigorously assess the semantic fidelity of Lean 4 formalizations.\n\nCriticLeanBench is a benchmark containing 500 natural language and Lean 4 language statement pairs (250 correct and 250 incorrect). Models trained via CriticLean can significantly outperform strong open- and closed-source baselines on this benchmark.\n\n## Dataset\n\nFineLeanCorpus is a dataset comprising over 285K problems that exhibits rich domain diversity, broad difficulty coverage, and high correctness based on human evaluation.\n\nThe paper (arxiv 2507.06181) was published in July 2025 and demonstrates that optimizing the critic phase is essential for producing reliable mathematical formalizations."
    ],
    "durationSeconds": 5.372472024999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f9761040-1bb6-401b-b0a1-adb73e5f1a1b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-27T18:16:46.964Z_

<details><summary>↩ Tool result · `toolu_01RhUHyP3YUoNdGRUygMY8MB`</summary>

```text
# Results Tables from DDRL Paper

## Main Performance Results (Table 2)

**Qwen2.5-Math-1.5B:**
- AIME 2024: DDRL 25.0 (vs TTRL 15.8, +19.0% vs ETMR)
- AMC: DDRL 52.9 (vs TTRL 48.9, +4.1% vs ETMR)
- MATH-500: DDRL 80.7 (vs TTRL 73.0, +4.9% vs ETMR)

**Qwen2.5-Base-3B:**
- AIME 2024: DDRL 10.0 (vs TTRL 7.9)
- AMC: DDRL 42.2 (vs TTRL 40.7)
- MATH-500: DDRL 72.7 (vs TTRL 72.2)

**Llama-3.1-8B-Instruct:**
- AIME 2024: DDRL 13.3 (vs TTRL 10.0)
- AMC: DDRL 38.6 (vs TTRL 32.3, +9.0% vs ETMR)
- MATH-500: DDRL 67.6 (vs TTRL 63.7, +13.6% vs ETMR)

**Qwen2.5-Math-7B (Appendix):**
- AIME 2024: DDRL 40.3 (vs TTRL 40.2)
- AMC: DDRL 69.0 (vs TTRL 68.1)
- MATH-500: DDRL 86.7 (vs TTRL 83.4)

## Ablation Study (Table 3)

Individual component contributions on Qwen2.5-Math-1.5B:
- Baseline TTRL: 45.9% average
- +Balanced Confidence-Aware Sampling: 46.1%
- +Debiased Advantage Estimation: 47.0%
- +All components (DDRL): 52.9%

## Highest Single Improvement

The best highlighted improvement is **+19.0% on AIME 2024** for Qwen2.5-Math-1.5B versus ETMR baseline.

## Note on "58.2%"

This percentage does **not appear** anywhere in the provided content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2c57edb-20b3-40d9-902c-6c5a8dc3bd42",
  "isSidechain": false,
  "promptId": "4b0c0804-0c80-4fc4-bd2d-54c91b4a93a7",
  "type": "user",
  "uuid": "7df4909f-c3c5-4bf8-a3ba-8569aa1417bb",
  "toolUseResult": {
    "bytes": 242042,
    "code": 200,
    "codeText": "OK",
    "result": "# Results Tables from DDRL Paper\n\n## Main Performance Results (Table 2)\n\n**Qwen2.5-Math-1.5B:**\n- AIME 2024: DDRL 25.0 (vs TTRL 15.8, +19.0% vs ETMR)\n- AMC: DDRL 52.9 (vs TTRL 48.9, +4.1% vs ETMR)\n- MATH-500: DDRL 80.7 (vs TTRL 73.0, +4.9% vs ETMR)\n\n**Qwen2.5-Base-3B:**\n- AIME 2024: DDRL 10.0 (vs TTRL 7.9)\n- AMC: DDRL 42.2 (vs TTRL 40.7)\n- MATH-500: DDRL 72.7 (vs TTRL 72.2)\n\n**Llama-3.1-8B-Instruct:**\n- AIME 2024: DDRL 13.3 (vs TTRL 10.0)\n- AMC: DDRL 38.6 (vs TTRL 32.3, +9.0% vs ETMR)\n- MATH-500: DDRL 67.6 (vs TTRL 63.7, +13.6% vs ETMR)\n\n**Qwen2.5-Math-7B (Appendix):**\n- AIME 2024: DDRL 40.3 (vs TTRL 40.2)\n- AMC: DDRL 69.0 (vs TTRL 68.1)\n- MATH-500: DDRL 86.7 (vs TTRL 83.4)\n\n## Ablation Study (Table 3)\n\nIndividual component contributions on Qwen2.5-Math-1.5B:\n- Baseline TTRL: 45.9% average\n- +Balanced Confidence-Aware Sampling: 46.1%\n- +Debiased Advantage Estimation: 47.0%\n- +All components (DDRL): 52.9%\n\n## Highest Single Improvement\n\nThe best highlighted improvement is **+19.0% on AIME 2024** for Qwen2.5-Math-1.5B versus ETMR baseline.\n\n## Note on \"58.2%\"\n\nThis percentage does **not appear** anywhere in the provided content.",
    "durationMs": 7058,
    "url": "https://arxiv.org/html/2604.21327"
  },
  "sourceToolAssistantUUID": "c2c57edb-20b3-40d9-902c-6c5a8dc3bd42",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-27T18:16:47.620Z_

<details><summary>↩ Tool result · `toolu_018nZwGHqmcVfVXRM8Zgihuc`</summary>

```text
Web search results for query: "DRIFT decompose retrieve formalize theorems ICLR 2026 Con-NF oracle retrieval 62.33% BEq"

Links: [{"title":"DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems | OpenReview","url":"https://openreview.net/forum?id=IGEs577RFz"},{"title":"ICLR Poster DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems","url":"https://iclr.cc/virtual/2026/poster/10010321"},{"title":"(PDF) DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems","url":"https://www.researchgate.net/publication/396458949_DRIFT_Decompose_Retrieve_Illustrate_then_Formalize_Theorems"},{"title":"DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems","url":"https://arxiv.org/html/2510.10815v2"},{"title":"DRIFT: DECOMPOSE, RETRIEVE, ILLUSTRATE, THEN ...","url":"https://openreview.net/pdf/3f497d563de1ccd4d5d0f6acc356e345dba4baa3.pdf"},{"title":"[2510.10815] DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems","url":"https://arxiv.org/abs/2510.10815"},{"title":"Preprint DRIFT: DECOMPOSE, RETRIEVE, ILLUSTRATE, THEN FORMALIZE THEOREMS","url":"https://arxiv.org/pdf/2510.10815"}]

I found information about the DRIFT paper. Here's what the search results show:

DRIFT is a novel framework that enables LLMs to decompose informal mathematical statements into smaller, more tractable "sub-components" which facilitates targeted retrieval of premises from mathematical libraries such as Mathlib. DRIFT also retrieves illustrative theorems to help models use premises more effectively in formalization tasks.

This is an ICLR 2026 Conference submission that addresses autoformalization and retrieval augmented generation.

Regarding the specific evaluation mentioned in your query: The paper evaluates on ConNF, a benchmark based on topological informalization to test out-of-distribution (OOD) generalization. ConNF contains 961 research-level theorems and formalizes a consistency proof for Quine's New Foundations.

However, the search results do not contain the specific performance metrics you mentioned (62.33% BEq oracle retrieval score). To find those specific numbers, you would need to review the full paper directly from the arXiv or OpenReview links provided in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2cd166f5-5540-4fe6-9b85-2e3aef3a3513",
  "isSidechain": false,
  "promptId": "4b0c0804-0c80-4fc4-bd2d-54c91b4a93a7",
  "type": "user",
  "uuid": "f9cae461-c5a0-4870-bd10-a34971ef01b8",
  "toolUseResult": {
    "query": "DRIFT decompose retrieve formalize theorems ICLR 2026 Con-NF oracle retrieval 62.33% BEq",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DWKUbJ64CcfTnZnpfpdy5T",
        "content": [
          {
            "title": "DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems | OpenReview",
            "url": "https://openreview.net/forum?id=IGEs577RFz"
          },
          {
            "title": "ICLR Poster DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems",
            "url": "https://iclr.cc/virtual/2026/poster/10010321"
          },
          {
            "title": "(PDF) DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems",
            "url": "https://www.researchgate.net/publication/396458949_DRIFT_Decompose_Retrieve_Illustrate_then_Formalize_Theorems"
          },
          {
            "title": "DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems",
            "url": "https://arxiv.org/html/2510.10815v2"
          },
          {
            "title": "DRIFT: DECOMPOSE, RETRIEVE, ILLUSTRATE, THEN ...",
            "url": "https://openreview.net/pdf/3f497d563de1ccd4d5d0f6acc356e345dba4baa3.pdf"
          },
          {
            "title": "[2510.10815] DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems",
            "url": "https://arxiv.org/abs/2510.10815"
          },
          {
            "title": "Preprint DRIFT: DECOMPOSE, RETRIEVE, ILLUSTRATE, THEN FORMALIZE THEOREMS",
            "url": "https://arxiv.org/pdf/2510.10815"
          }
        ]
      },
      "I found information about the DRIFT paper. Here's what the search results show:\n\nDRIFT is a novel framework that enables LLMs to decompose informal mathematical statements into smaller, more tractable \"sub-components\" which facilitates targeted retrieval of premises from mathematical libraries such as Mathlib. DRIFT also retrieves illustrative theorems to help models use premises more effectively in formalization tasks.\n\nThis is an ICLR 2026 Conference submission that addresses autoformalization and retrieval augmented generation.\n\nRegarding the specific evaluation mentioned in your query: The paper evaluates on ConNF, a benchmark based on topological informalization to test out-of-distribution (OOD) generalization. ConNF contains 961 research-level theorems and formalizes a consistency proof for Quine's New Foundations.\n\nHowever, the search results do not contain the specific performance metrics you mentioned (62.33% BEq oracle retrieval score). To find those specific numbers, you would need to review the full paper directly from the arXiv or OpenReview links provided in the search results."
    ],
    "durationSeconds": 6.113220150000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2cd166f5-5540-4fe6-9b85-2e3aef3a3513",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32 · 2026-05-27T18:16:47.624Z_

```json
{
  "parentUuid": "f9cae461-c5a0-4870-bd10-a34971ef01b8",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "afa79a46-8162-4650-a025-b5d2117c3952",
  "timestamp": "2026-05-27T18:16:47.624Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 33 · 2026-05-27T18:16:50.359Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I got the DDRL numbers. Now let me fetch the CriticLean paper and DRIFT paper to get the exact accuracy numbers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afa79a46-8162-4650-a025-b5d2117c3952",
  "isSidechain": false,
  "requestId": "req_011CbTXnoixKCxxhmGpk547K",
  "type": "assistant",
  "uuid": "2d0f82a3-2e89-47bd-9aae-fbacd90d64df",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AuovwFUYv6cVi1ddXjLJCa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2607,
      "cache_read_input_tokens": 23455,
      "output_tokens": 589,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2607,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 589,
          "cache_read_input_tokens": 23455,
          "cache_creation_input_tokens": 2607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2607
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

_source line 34 · 2026-05-27T18:16:51.310Z_

Good, I have the DDRL numbers confirmed. Now let me fetch the CriticLean and DRIFT papers for exact accuracy figures.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d0f82a3-2e89-47bd-9aae-fbacd90d64df",
  "isSidechain": false,
  "requestId": "req_011CbTXnoixKCxxhmGpk547K",
  "type": "assistant",
  "uuid": "012bb7c0-efc7-4856-a791-88659fdd3faf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AuovwFUYv6cVi1ddXjLJCa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2607,
      "cache_read_input_tokens": 23455,
      "output_tokens": 589,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2607,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 589,
          "cache_read_input_tokens": 23455,
          "cache_creation_input_tokens": 2607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2607
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

_source line 35 · 2026-05-27T18:16:55.152Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01H1wjSHqKL74oGamWbewNEn`</summary>

```json
{
  "url": "https://arxiv.org/html/2507.06181v1",
  "prompt": "Extract ALL accuracy numbers from this paper. I need: 1) CriticLeanBench accuracy for EACH model variant (CriticLeanGPT-8B, CriticLeanGPT-14B, CriticLeanGPT-32B, and their -RL variants). 2) The specific accuracy for CriticLeanGPT-Qwen3-14B-RL on CriticLeanBench. 3) The pipeline accuracy improvement numbers (the 54% to 84% claim). 4) Any numbers that are exactly 87% or 84.8%. 5) Comparison with GPT-4o and other baselines on CriticLeanBench. 6) The overall best critic accuracy they achieve."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "012bb7c0-efc7-4856-a791-88659fdd3faf",
  "isSidechain": false,
  "requestId": "req_011CbTXnoixKCxxhmGpk547K",
  "type": "assistant",
  "uuid": "ee14f733-3ac5-46f7-8962-5448fbd3d8a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AuovwFUYv6cVi1ddXjLJCa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2607,
      "cache_read_input_tokens": 23455,
      "output_tokens": 589,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2607,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 589,
          "cache_read_input_tokens": 23455,
          "cache_creation_input_tokens": 2607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2607
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

_source line 36 · 2026-05-27T18:16:55.163Z_

<details><summary>↩ Tool result · `toolu_01H1wjSHqKL74oGamWbewNEn`</summary>

```text
The server returned HTTP 404 Not Found.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee14f733-3ac5-46f7-8962-5448fbd3d8a3",
  "isSidechain": false,
  "promptId": "4b0c0804-0c80-4fc4-bd2d-54c91b4a93a7",
  "type": "user",
  "uuid": "1d8e88df-2b19-4de6-aca2-090e9bac2682",
  "toolUseResult": {
    "bytes": 0,
    "code": 404,
    "codeText": "Not Found",
    "result": "The server returned HTTP 404 Not Found.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 6,
    "url": "https://arxiv.org/html/2507.06181v1"
  },
  "sourceToolAssistantUUID": "ee14f733-3ac5-46f7-8962-5448fbd3d8a3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-27T18:16:59.108Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01BDerKC4VSFeMh7beiC3unF`</summary>

```json
{
  "url": "https://arxiv.org/html/2510.10815v2",
  "prompt": "Extract the FULL results on Con-NF benchmark. I need: 1) The exact BEq+@10 score for DRIFT with GPT-4.1 (the 62.33% claim). 2) The Oracle* retrieval score (58.90%). 3) The DPR baseline score (20.08%). 4) All other method scores on Con-NF. 5) Any discussion of why DRIFT exceeds oracle retrieval. 6) Results on ProofNet too. 7) Any limitations DRIFT acknowledges about its retrieval approach."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d8e88df-2b19-4de6-aca2-090e9bac2682",
  "isSidechain": false,
  "requestId": "req_011CbTXnoixKCxxhmGpk547K",
  "type": "assistant",
  "uuid": "87701a30-6ed2-4ddc-a356-8ddb5106fb67",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AuovwFUYv6cVi1ddXjLJCa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2607,
      "cache_read_input_tokens": 23455,
      "output_tokens": 589,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2607,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 589,
          "cache_read_input_tokens": 23455,
          "cache_creation_input_tokens": 2607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2607
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

_source line 38 · 2026-05-27T18:16:59.527Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PKk2hN8nTaBV6tHzfUMhb6`</summary>

```json
{
  "query": "MathAtlas arxiv 2605.14061 autoformalization benchmark graduate level dependency graph evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "87701a30-6ed2-4ddc-a356-8ddb5106fb67",
  "isSidechain": false,
  "requestId": "req_011CbTXnoixKCxxhmGpk547K",
  "type": "assistant",
  "uuid": "a9b0eda5-33df-401a-8669-cd3c11afc75c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AuovwFUYv6cVi1ddXjLJCa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2607,
      "cache_read_input_tokens": 23455,
      "output_tokens": 589,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2607,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 589,
          "cache_read_input_tokens": 23455,
          "cache_creation_input_tokens": 2607,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2607
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

_source line 39 · 2026-05-27T18:17:04.847Z_

<details><summary>↩ Tool result · `toolu_01BDerKC4VSFeMh7beiC3unF`</summary>

```text
# DRIFT Results Analysis

## ConNF Benchmark Results (Table 2)

**BEq+@10 Scores:**
- **DRIFT (GPT-4.1): 62.33%** (+55.57 vs zero-shot)
- Oracle*: 58.90%
- DPR (RAuto): 20.08% (+13.32 vs zero-shot)
- Zero-shot: 6.76%

**DRIFT (DeepSeek-3.1): 54.21%** (+43.18 vs zero-shot)

## Why DRIFT Exceeds Oracle*

The paper notes that "the Oracle* provides only necessary premises based on the reference statement, while the illustrative theorems selected with Drift provide crucial demonstrations of premise usage." This suggests illustrative theorems offer practical guidance beyond definition retrieval alone.

## ProofNet Results (Table 2)

**BEq+@10 Scores:**
- DRIFT (GPT-4.1): 21.93% (+8.56 vs DPR)
- DRIFT (DeepSeek-3.1): 20.59% (+0.27 vs DPR)
- Oracle*: 27.54%
- DPR (RAuto): ~19.25%

## Acknowledged Limitations

The framework identifies that "retrieval effectiveness in mathematical autoformalization depends heavily on model-specific knowledge boundaries." On simpler benchmarks like MiniF2F-test with minimal dependencies, adding context "can act as a distractor rather than an aid," suggesting decomposition-based retrieval isn't universally beneficial across all problem types.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "87701a30-6ed2-4ddc-a356-8ddb5106fb67",
  "isSidechain": false,
  "promptId": "4b0c0804-0c80-4fc4-bd2d-54c91b4a93a7",
  "type": "user",
  "uuid": "51aa0bdb-15d6-491c-b384-b29a6311b852",
  "toolUseResult": {
    "bytes": 367512,
    "code": 200,
    "codeText": "OK",
    "result": "# DRIFT Results Analysis\n\n## ConNF Benchmark Results (Table 2)\n\n**BEq+@10 Scores:**\n- **DRIFT (GPT-4.1): 62.33%** (+55.57 vs zero-shot)\n- Oracle*: 58.90%\n- DPR (RAuto): 20.08% (+13.32 vs zero-shot)\n- Zero-shot: 6.76%\n\n**DRIFT (DeepSeek-3.1): 54.21%** (+43.18 vs zero-shot)\n\n## Why DRIFT Exceeds Oracle*\n\nThe paper notes that \"the Oracle* provides only necessary premises based on the reference statement, while the illustrative theorems selected with Drift provide crucial demonstrations of premise usage.\" This suggests illustrative theorems offer practical guidance beyond definition retrieval alone.\n\n## ProofNet Results (Table 2)\n\n**BEq+@10 Scores:**\n- DRIFT (GPT-4.1): 21.93% (+8.56 vs DPR)\n- DRIFT (DeepSeek-3.1): 20.59% (+0.27 vs DPR)\n- Oracle*: 27.54%\n- DPR (RAuto): ~19.25%\n\n## Acknowledged Limitations\n\nThe framework identifies that \"retrieval effectiveness in mathematical autoformalization depends heavily on model-specific knowledge boundaries.\" On simpler benchmarks like MiniF2F-test with minimal dependencies, adding context \"can act as a distractor rather than an aid,\" suggesting decomposition-based retrieval isn't universally beneficial across all problem types.",
    "durationMs": 5735,
    "url": "https://arxiv.org/html/2510.10815v2"
  },
  "sourceToolAssistantUUID": "87701a30-6ed2-4ddc-a356-8ddb5106fb67",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-27T18:17:06.260Z_

<details><summary>↩ Tool result · `toolu_01PKk2hN8nTaBV6tHzfUMhb6`</summary>

```text
Web search results for query: "MathAtlas arxiv 2605.14061 autoformalization benchmark graduate level dependency graph evaluation"

Links: [{"title":"MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/html/2605.14061"},{"title":"[2605.14061] MathAtlas: A Benchmark for Autoformalization in the Wild","url":"https://arxiv.org/abs/2605.14061"},{"title":"ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data","url":"https://arxiv.org/html/2502.05567v2"},{"title":"Autoformalizer with Tool Feedback","url":"https://arxiv.org/html/2510.06857v1"},{"title":"Autoformalizing Mathematical Statements by Symbolic Equivalence and Semantic Consistency","url":"https://arxiv.org/html/2410.20936v1"},{"title":"A New Approach Towards Autoformalization","url":"https://arxiv.org/pdf/2310.07957"},{"title":"Autoformalize Mathematical Statements by Symbolic Equivalence and   Semantic Consistency","url":"https://arxiv.org/pdf/2410.20936"},{"title":"Autoformalization in the Era of Large Language Models: A Survey","url":"https://arxiv.org/pdf/2505.23486"}]

Based on the search results, I found detailed information about MathAtlas (arxiv 2605.14061):

## Overview

MathAtlas is the first large-scale autoformalization benchmark of graduate-level mathematics, containing ~52k theorems, definitions, exercises, examples, and proofs extracted from 103 graduate mathematics textbooks.

## Key Features

MathAtlas is enriched with a mathematical dependency graph containing ~178k relations, and is the first autoformalization benchmark to include such relations, facilitating evaluation and development of dependency-aware autoformalization systems. Dependencies needed to correctly formalize theorems include object references to previously defined mathematical concepts, and these objects each have their own dependency tree.

## Motivation

Current autoformalization benchmarks are largely focused on olympiad or undergraduate mathematics, while graduate and research-level mathematics remains underexplored, which motivated the creation of MathAtlas.

## Benchmark Difficulty

MathAtlas is high quality but extremely challenging: strong baselines achieve at most 9.8% correctness on theorem statements and 16.7% on definitions. Additionally, performance of state-of-the-art models degrades substantially with dependency depth.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a9b0eda5-33df-401a-8669-cd3c11afc75c",
  "isSidechain": false,
  "promptId": "4b0c0804-0c80-4fc4-bd2d-54c91b4a93a7",
  "type": "user",
  "uuid": "4467a034-c623-4a46-afd7-009b8ac5d96a",
  "toolUseResult": {
    "query": "MathAtlas arxiv 2605.14061 autoformalization benchmark graduate level dependency graph evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DDCFLfwmTi2W4ju15v3XBM",
        "content": [
          {
            "title": "MathAtlas: A Benchmark for Autoformalization in the Wild",
            "url": "https://arxiv.org/html/2605.14061"
          },
          {
            "title": "[2605.14061] MathAtlas: A Benchmark for Autoformalization in the Wild",
            "url": "https://arxiv.org/abs/2605.14061"
          },
          {
            "title": "ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data",
            "url": "https://arxiv.org/html/2502.05567v2"
          },
          {
            "title": "Autoformalizer with Tool Feedback",
            "url": "https://arxiv.org/html/2510.06857v1"
          },
          {
            "title": "Autoformalizing Mathematical Statements by Symbolic Equivalence and Semantic Consistency",
            "url": "https://arxiv.org/html/2410.20936v1"
          },
          {
            "title": "A New Approach Towards Autoformalization",
            "url": "https://arxiv.org/pdf/2310.07957"
          },
          {
            "title": "Autoformalize Mathematical Statements by Symbolic Equivalence and   Semantic Consistency",
            "url": "https://arxiv.org/pdf/2410.20936"
          },
          {
            "title": "Autoformalization in the Era of Large Language Models: A Survey",
            "url": "https://arxiv.org/pdf/2505.23486"
          }
        ]
      },
      "Based on the search results, I found detailed information about MathAtlas (arxiv 2605.14061):\n\n## Overview\n\nMathAtlas is the first large-scale autoformalization benchmark of graduate-level mathematics, containing ~52k theorems, definitions, exercises, examples, and proofs extracted from 103 graduate mathematics textbooks.\n\n## Key Features\n\nMathAtlas is enriched with a mathematical dependency graph containing ~178k relations, and is the first autoformalization benchmark to include such relations, facilitating evaluation and development of dependency-aware autoformalization systems. Dependencies needed to correctly formalize theorems include object references to previously defined mathematical concepts, and these objects each have their own dependency tree.\n\n## Motivation\n\nCurrent autoformalization benchmarks are largely focused on olympiad or undergraduate mathematics, while graduate and research-level mathematics remains underexplored, which motivated the creation of MathAtlas.\n\n## Benchmark Difficulty\n\nMathAtlas is high quality but extremely challenging: strong baselines achieve at most 9.8% correctness on theorem statements and 16.7% on definitions. Additionally, performance of state-of-the-art models degrades substantially with dependency depth."
    ],
    "durationSeconds": 6.729987537000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a9b0eda5-33df-401a-8669-cd3c11afc75c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Aut…",
  "leafUuid": "4467a034-c623-4a46-afd7-009b8ac5d96a",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise autoformalization TTRL paper with verified data and concrete curriculum",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6"
}
```

---

### Assistant

_source line 43 · 2026-05-27T18:17:09.462Z_

<details><summary>Logged reasoning block</summary>

```text
Let me get the CriticLean paper - the HTML version returned 404. Let me try the PDF or the abstract page, or try a different URL format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4467a034-c623-4a46-afd7-009b8ac5d96a",
  "isSidechain": false,
  "requestId": "req_011CbTXpBVvM3kMTM3geYQPJ",
  "type": "assistant",
  "uuid": "38fc505c-3b50-428f-8a89-b31dca767a7c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165gXYwwGzXjgGRiD3wbYNt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1725,
      "cache_read_input_tokens": 26062,
      "output_tokens": 592,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1725,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 592,
          "cache_read_input_tokens": 26062,
          "cache_creation_input_tokens": 1725,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1725
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

_source line 44 · 2026-05-27T18:17:09.908Z_

Let me try a different URL for the CriticLean paper and get more details on MathAtlas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38fc505c-3b50-428f-8a89-b31dca767a7c",
  "isSidechain": false,
  "requestId": "req_011CbTXpBVvM3kMTM3geYQPJ",
  "type": "assistant",
  "uuid": "d318a506-a171-4bb2-8176-c41eb9f9ea3d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165gXYwwGzXjgGRiD3wbYNt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1725,
      "cache_read_input_tokens": 26062,
      "output_tokens": 592,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1725,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 592,
          "cache_read_input_tokens": 26062,
          "cache_creation_input_tokens": 1725,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1725
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

_source line 45 · 2026-05-27T18:17:11.378Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019vzintMJXjs8xMLsTxotLw`</summary>

```json
{
  "url": "https://arxiv.org/abs/2507.06181",
  "prompt": "Extract ALL accuracy numbers mentioned in the abstract and paper metadata. I need: 1) CriticLeanBench accuracy for each model. 2) Pipeline accuracy improvement. 3) Any numbers 87% or 84.8%. 4) The specific model names and their scores."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d318a506-a171-4bb2-8176-c41eb9f9ea3d",
  "isSidechain": false,
  "requestId": "req_011CbTXpBVvM3kMTM3geYQPJ",
  "type": "assistant",
  "uuid": "228b3794-846f-4308-b54a-538e587b5eea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165gXYwwGzXjgGRiD3wbYNt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1725,
      "cache_read_input_tokens": 26062,
      "output_tokens": 592,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1725,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 592,
          "cache_read_input_tokens": 26062,
          "cache_creation_input_tokens": 1725,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1725
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

_source line 46 · 2026-05-27T18:17:13.750Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01PskNSYMHRqjoEDAZHpS7sU`</summary>

```json
{
  "url": "https://www.aimodels.fyi/papers/arxiv/criticlean-critic-guided-reinforcement-learning-mathematical-formalization",
  "prompt": "Extract ALL accuracy numbers and results from this CriticLean paper summary. I need: 1) CriticLeanBench accuracy for each model variant (8B, 14B, 32B, and -RL variants). 2) The specific accuracy for CriticLeanGPT-Qwen3-14B-RL. 3) The pipeline accuracy numbers (54% to 84%). 4) Any numbers 87% or 84.8%. 5) Comparison baselines (GPT-4o, etc.)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "228b3794-846f-4308-b54a-538e587b5eea",
  "isSidechain": false,
  "requestId": "req_011CbTXpBVvM3kMTM3geYQPJ",
  "type": "assistant",
  "uuid": "9f836012-5865-4dc1-a1c5-421ce9e68ecd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165gXYwwGzXjgGRiD3wbYNt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1725,
      "cache_read_input_tokens": 26062,
      "output_tokens": 592,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1725,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 592,
          "cache_read_input_tokens": 26062,
          "cache_creation_input_tokens": 1725,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1725
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

_source line 47 · 2026-05-27T18:17:13.958Z_

<details><summary>↩ Tool result · `toolu_019vzintMJXjs8xMLsTxotLw`</summary>

```text
# Accuracy Numbers from CriticLean Paper

Based on the provided abstract and metadata, **no specific accuracy numbers are mentioned**. The document does not include:

- CriticLeanBench accuracy scores for individual models
- Pipeline accuracy improvements
- References to 87% or 84.8%
- Specific model performance metrics with scores

The abstract only states that researchers "demonstrate that our trained CriticLeanGPT models can significantly outperform strong open- and closed-source baselines," but provides no quantitative results.

**To access the detailed accuracy numbers**, you would need to review the full PDF paper, which is available at `/pdf/2507.06181` on arXiv.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "228b3794-846f-4308-b54a-538e587b5eea",
  "isSidechain": false,
  "promptId": "4b0c0804-0c80-4fc4-bd2d-54c91b4a93a7",
  "type": "user",
  "uuid": "f7be4a10-6ce6-44b9-8a30-8ca9b52a99a2",
  "toolUseResult": {
    "bytes": 48790,
    "code": 200,
    "codeText": "OK",
    "result": "# Accuracy Numbers from CriticLean Paper\n\nBased on the provided abstract and metadata, **no specific accuracy numbers are mentioned**. The document does not include:\n\n- CriticLeanBench accuracy scores for individual models\n- Pipeline accuracy improvements\n- References to 87% or 84.8%\n- Specific model performance metrics with scores\n\nThe abstract only states that researchers \"demonstrate that our trained CriticLeanGPT models can significantly outperform strong open- and closed-source baselines,\" but provides no quantitative results.\n\n**To access the detailed accuracy numbers**, you would need to review the full PDF paper, which is available at `/pdf/2507.06181` on arXiv.",
    "durationMs": 2576,
    "url": "https://arxiv.org/abs/2507.06181"
  },
  "sourceToolAssistantUUID": "228b3794-846f-4308-b54a-538e587b5eea",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-27T18:17:13.967Z_

<details><summary>↩ Tool result · `toolu_01PskNSYMHRqjoEDAZHpS7sU`</summary>

```text
The server returned HTTP 403 Forbidden.

The response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f836012-5865-4dc1-a1c5-421ce9e68ecd",
  "isSidechain": false,
  "promptId": "4b0c0804-0c80-4fc4-bd2d-54c91b4a93a7",
  "type": "user",
  "uuid": "393022c4-a877-43b4-84be-d774ae1b7064",
  "toolUseResult": {
    "bytes": 0,
    "code": 403,
    "codeText": "Forbidden",
    "result": "The server returned HTTP 403 Forbidden.\n\nThe response body was not retrieved. If this URL requires authentication, use an authenticated tool (e.g. `gh` for GitHub, or an MCP-provided fetch tool) instead of WebFetch.",
    "durationMs": 214,
    "url": "https://www.aimodels.fyi/papers/arxiv/criticlean-critic-guided-reinforcement-learning-mathematical-formalization"
  },
  "sourceToolAssistantUUID": "9f836012-5865-4dc1-a1c5-421ce9e68ecd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-27T18:17:16.427Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01YW5k9jcwffXZqjAngb7Lz9`</summary>

```json
{
  "url": "https://arxiv.org/html/2605.14061",
  "prompt": "Extract ALL evaluation results from MathAtlas. I need: 1) Performance of each model on MA-Hard, MA-Medium, MA-Easy. 2) The 2.6% claim on hardest subset - which model achieves this? 3) Dependency depth analysis - how does performance degrade? 4) Evaluation metrics (BEq, compilation, etc.). 5) Domain breakdown. 6) Any information about retrieval-augmented approaches tested."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "393022c4-a877-43b4-84be-d774ae1b7064",
  "isSidechain": false,
  "requestId": "req_011CbTXpBVvM3kMTM3geYQPJ",
  "type": "assistant",
  "uuid": "0690da2b-b520-43fb-91cc-d6415d8ada5a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165gXYwwGzXjgGRiD3wbYNt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1725,
      "cache_read_input_tokens": 26062,
      "output_tokens": 592,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1725,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 592,
          "cache_read_input_tokens": 26062,
          "cache_creation_input_tokens": 1725,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1725
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

_source line 50 · 2026-05-27T18:17:25.879Z_

<details><summary>↩ Tool result · `toolu_01YW5k9jcwffXZqjAngb7Lz9`</summary>

```text
# MathAtlas Evaluation Results

## 1) Performance by Difficulty Subset

The paper provides results on **MA-Hard** (700 entities with deepest dependency trees) but does not explicitly stratify results into MA-Medium and MA-Easy categories.

**MA-Hard Results:**
- gpt-oss-20b: 2.1% correctness
- gpt-oss-120b: 2.6% correctness (best performer)

**Full Dataset Results:**
- Statements: Best model (ReForm 8B) achieves 9.8% correctness
- Definitions: Best model (gpt-oss-120b) achieves 16.7% correctness

## 2) The 2.6% Claim

"gpt-oss-120b" with few-shot prompting achieves the 2.6% correctness rate on MA-Hard. This represents the strongest baseline tested on the hardest subset.

## 3) Dependency Depth Analysis

Performance degrades substantially with increased dependency depth. The study found "a clear trend, showing that our best systems is less likely to correctly formalize deeper targets." A Kolmogorov–Smirnov test confirmed "significant difference between the max depth distributions for correct and incorrect examples (p<0.001)."

Average dependency depth is 30 (median 17), ranging from 0 to 80.

## 4) Evaluation Metrics

- **Compile rate**: Percentage of generated code that successfully compiles
- **Faithfulness**: Percentage of compilable statements that preserve mathematical meaning
- **Correctness**: Combined metric requiring both compilation and semantic faithfulness
- **Semantic faithfulness tools tested**: CriticLean (32B), custom LLM-as-judge approaches

## 5) Domain Breakdown

Mathematics spans 87 fields across 103 textbooks. Field-specific variations in dependency depth were noted: "entities from textbooks on Lie algebra or Quantum groups had an average depth of ∼50, whereas those from books on set theory and logic had an average depth of ∼6."

## 6) Retrieval-Augmented Approaches

The paper evaluated adding local context (500 tokens) to prompted systems, finding it actually *degraded* performance: "including 300 tokens of local context seems to confuse prompted systems." No dependency retrieval-augmented methods were successfully evaluated due to unavailable implementations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0690da2b-b520-43fb-91cc-d6415d8ada5a",
  "isSidechain": false,
  "promptId": "4b0c0804-0c80-4fc4-bd2d-54c91b4a93a7",
  "type": "user",
  "uuid": "f0785a7b-4cc6-42ad-bd73-788180a87a41",
  "toolUseResult": {
    "bytes": 690508,
    "code": 200,
    "codeText": "OK",
    "result": "# MathAtlas Evaluation Results\n\n## 1) Performance by Difficulty Subset\n\nThe paper provides results on **MA-Hard** (700 entities with deepest dependency trees) but does not explicitly stratify results into MA-Medium and MA-Easy categories.\n\n**MA-Hard Results:**\n- gpt-oss-20b: 2.1% correctness\n- gpt-oss-120b: 2.6% correctness (best performer)\n\n**Full Dataset Results:**\n- Statements: Best model (ReForm 8B) achieves 9.8% correctness\n- Definitions: Best model (gpt-oss-120b) achieves 16.7% correctness\n\n## 2) The 2.6% Claim\n\n\"gpt-oss-120b\" with few-shot prompting achieves the 2.6% correctness rate on MA-Hard. This represents the strongest baseline tested on the hardest subset.\n\n## 3) Dependency Depth Analysis\n\nPerformance degrades substantially with increased dependency depth. The study found \"a clear trend, showing that our best systems is less likely to correctly formalize deeper targets.\" A Kolmogorov–Smirnov test confirmed \"significant difference between the max depth distributions for correct and incorrect examples (p<0.001).\"\n\nAverage dependency depth is 30 (median 17), ranging from 0 to 80.\n\n## 4) Evaluation Metrics\n\n- **Compile rate**: Percentage of generated code that successfully compiles\n- **Faithfulness**: Percentage of compilable statements that preserve mathematical meaning\n- **Correctness**: Combined metric requiring both compilation and semantic faithfulness\n- **Semantic faithfulness tools tested**: CriticLean (32B), custom LLM-as-judge approaches\n\n## 5) Domain Breakdown\n\nMathematics spans 87 fields across 103 textbooks. Field-specific variations in dependency depth were noted: \"entities from textbooks on Lie algebra or Quantum groups had an average depth of ∼50, whereas those from books on set theory and logic had an average depth of ∼6.\"\n\n## 6) Retrieval-Augmented Approaches\n\nThe paper evaluated adding local context (500 tokens) to prompted systems, finding it actually *degraded* performance: \"including 300 tokens of local context seems to confuse prompted systems.\" No dependency retrieval-augmented methods were successfully evaluated due to unavailable implementations.",
    "durationMs": 9447,
    "url": "https://arxiv.org/html/2605.14061"
  },
  "sourceToolAssistantUUID": "0690da2b-b520-43fb-91cc-d6415d8ada5a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-27T18:17:29.409Z_

<details><summary>Logged reasoning block</summary>

```text
Interesting! MathAtlas found that adding local context actually degraded performance for prompted systems. This is important - it means naive retrieval doesn't work, reinforcing the need for smarter retrieval approaches.

Let me try to get the CriticLean paper PDF or look for it elsewhere to resolve the 87% vs 84.8% inconsistency.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0785a7b-4cc6-42ad-bd73-788180a87a41",
  "isSidechain": false,
  "requestId": "req_011CbTXqdGzLZ7RAdvPkpzoD",
  "type": "assistant",
  "uuid": "1204da5d-cd45-4868-9bfc-4ce9b6f2a3c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKyp7Ma2WTz1NVyALJkb8J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1434,
      "cache_read_input_tokens": 27787,
      "output_tokens": 458,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1434,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 458,
          "cache_read_input_tokens": 27787,
          "cache_creation_input_tokens": 1434,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1434
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

_source line 52 · 2026-05-27T18:17:29.842Z_

Let me try to get the CriticLean accuracy numbers from the PDF and the HuggingFace page.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1204da5d-cd45-4868-9bfc-4ce9b6f2a3c9",
  "isSidechain": false,
  "requestId": "req_011CbTXqdGzLZ7RAdvPkpzoD",
  "type": "assistant",
  "uuid": "0a775495-96d4-4231-9562-99e311827c21",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKyp7Ma2WTz1NVyALJkb8J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1434,
      "cache_read_input_tokens": 27787,
      "output_tokens": 458,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1434,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 458,
          "cache_read_input_tokens": 27787,
          "cache_creation_input_tokens": 1434,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1434
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

_source line 53 · 2026-05-27T18:17:31.727Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016rqZDKmFkzrH3XvWTnogpJ`</summary>

```json
{
  "url": "https://huggingface.co/papers/2507.06181",
  "prompt": "Extract ALL accuracy numbers and results from this CriticLean paper page. I need the CriticLeanBench accuracy for each model, especially CriticLeanGPT-Qwen3-14B-RL. Any numbers like 87%, 84.8%, 84%, or similar. The pipeline improvement numbers."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a775495-96d4-4231-9562-99e311827c21",
  "isSidechain": false,
  "requestId": "req_011CbTXqdGzLZ7RAdvPkpzoD",
  "type": "assistant",
  "uuid": "55197c63-d15c-48eb-81f7-ef6f93158156",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKyp7Ma2WTz1NVyALJkb8J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1434,
      "cache_read_input_tokens": 27787,
      "output_tokens": 458,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1434,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 458,
          "cache_read_input_tokens": 27787,
          "cache_creation_input_tokens": 1434,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1434
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

_source line 54 · 2026-05-27T18:17:32.678Z_

<details><summary>↩ Tool result · `toolu_016rqZDKmFkzrH3XvWTnogpJ`</summary>

```text
&lt;persisted-output>
Output too large (91.1KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/2a30fe45-086a-4752-b69b-cc68f89516e6/tool-results/toolu_016rqZDKmFkzrH3XvWTnogpJ.txt

Preview (first 2KB):
# CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization

ByteDance Seed      Nanjing University

Full author list in Contributions

## Abstract

Translating natural language mathematical statements into formal, executable code is a fundamental challenge in automated theorem proving. While prior work has focused on generation and compilation success, little attention has been paid to the *critic phase*—the evaluation of whether generated formalizations truly capture the semantic intent of the original problem. In this paper, we introduce **CriticLean**, a novel critic-guided reinforcement learning framework that elevates the role of the critic from a passive validator to an active learning component. Specifically, first, we propose the **CriticLeanGPT**, trained via supervised fine-tuning and reinforcement learning, to rigorously assess the semantic fidelity of Lean 4 formalizations. Then, we introduce **CriticLeanBench**, a benchmark designed to measure models’ ability to distinguish semantically correct from incorrect formalizations, and demonstrate that our trained CriticLeanGPT models can significantly outperform strong open- and closed-source baselines. Building on the CriticLean framework, we construct **FineLeanCorpus**, a dataset comprising over 285K problems that exhibits rich domain diversity, broad difficulty coverage, and high correctness based on human evaluation. Overall, our findings highlight that optimizing the critic phase is essential for producing reliable formalizations and we hope our CriticLean will provide valuable insights for future advances in formal mathematical reasoning.

**Date:** July 8, 2025

**Correspondence:** [liujiaheng@nju.edu.cn](mailto:liujiaheng@nju.edu.cn), [zhangge.eli@bytedance.com](mailto:zhangge.eli@bytedance.com)

**Project Page:** &lt;https://github.com/multimodal-art-projection/CriticLean>

## 1 Introduction

...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "55197c63-d15c-48eb-81f7-ef6f93158156",
  "isSidechain": false,
  "promptId": "4b0c0804-0c80-4fc4-bd2d-54c91b4a93a7",
  "type": "user",
  "uuid": "68b6fa0b-e3f3-464a-b990-e213b0301e05",
  "toolUseResult": {
    "bytes": 93671,
    "code": 200,
    "codeText": "OK",
    "result": "# CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization\n\nByteDance Seed      Nanjing University\n\nFull author list in Contributions\n\n## Abstract\n\nTranslating natural language mathematical statements into formal, executable code is a fundamental challenge in automated theorem proving. While prior work has focused on generation and compilation success, little attention has been paid to the *critic phase*—the evaluation of whether generated formalizations truly capture the semantic intent of the original problem. In this paper, we introduce **CriticLean**, a novel critic-guided reinforcement learning framework that elevates the role of the critic from a passive validator to an active learning component. Specifically, first, we propose the **CriticLeanGPT**, trained via supervised fine-tuning and reinforcement learning, to rigorously assess the semantic fidelity of Lean 4 formalizations. Then, we introduce **CriticLeanBench**, a benchmark designed to measure models’ ability to distinguish semantically correct from incorrect formalizations, and demonstrate that our trained CriticLeanGPT models can significantly outperform strong open- and closed-source baselines. Building on the CriticLean framework, we construct **FineLeanCorpus**, a dataset comprising over 285K problems that exhibits rich domain diversity, broad difficulty coverage, and high correctness based on human evaluation. Overall, our findings highlight that optimizing the critic phase is essential for producing reliable formalizations and we hope our CriticLean will provide valuable insights for future advances in formal mathematical reasoning.\n\n**Date:** July 8, 2025\n\n**Correspondence:** [liujiaheng@nju.edu.cn](mailto:liujiaheng@nju.edu.cn), [zhangge.eli@bytedance.com](mailto:zhangge.eli@bytedance.com)\n\n**Project Page:** &lt;https://github.com/multimodal-art-projection/CriticLean>\n\n## 1 Introduction\n\nThe formalization of mathematical statements [64] is a critical task in modern mathematical computation, particularly in the context of theorem provers like Lean 4 [22]. The translation of natural language mathematical problems into formal, executable code remains a significant challenge, as it requires not only syntactical accuracy but also a deep understanding of the problem’s semantics [44, 49]. Existing approaches have shown progress, but they often face limitations in accuracy, especially in the context of complex, high-level problems that involve sophisticated mathematical reasoning [3, 23, 58, 59, 75]. In contrast to existing works, we argue that the *critic* phase—the step where the semantic correctness of generated formalizations is evaluated—is not only underexplored but also fundamentally essential to the success of mathematical autoformalization.\n\nTherefore, in this paper, we systematically investigate and optimize the critic component and introduce **CriticLean**, a comprehensive framework that places the critic model at the center of the formalization pipeline. Unlike prior work that primarily focuses on generation quality or compiler validity, CriticLean introduces the reinforcement learning-based **CriticLeanGPT** models explicitly trained to evaluate whether the Lean 4 output truly reflects the intent of the original mathematical statement., and we present a full methodology forThe diagram illustrates the CriticLean framework for mathematics autoformalization. It starts with a **Natural Language Statement** box containing a mathematical problem about permutations. This statement is processed by an **AutoFormalizer**. The AutoFormalizer's output is then evaluated by two verification steps: a **Verify** box for syntax checking and name resolution, and another **Verify** box for semantic meaning and logical consistency. The **Verify** boxes are supported by a **Lean Compiler** and **CriticLeanGPT** respectively. If a **Compilation Error** or **Critique Error** occurs, the AutoFormalizer receives feedback and iterates. If successful, the final output is a **Lean Formal Language Statement** box showing the formalized theorem.\n\n**Figure 1** Illustration of CriticLean framework based on Critic-Guided Reinforcement Learning for Mathematics Autoformalization.\n\ntraining, and evaluating CriticLeanGPT model. Specifically, as shown in Figure 1, for each natural language statement, we apply the autoformalization iteratively based on the feedback from the Lean compiler and the CriticLeanGPT models, which is trained to critically assess whether a generated formalization accurately represents the semantics of the original mathematical statement. In each iteration, the feedback provides valuable signals that drive an iterative refinement process, further improving the quality of the final Lean code output.\n\nAdditionally, we present **CriticLeanBench**, a benchmark designed to evaluate the performance of CriticLeanGPT models, which contain 500 natural language and Lean 4 language statement pairs (i.e., 250 correct and 250 incorrect pairs). Through extensive experiments, we demonstrate that our trained CriticLeanGPT models outperform the SOTA open-source models [4, 10, 11] and many closed-source API models [9, 12, 42] greatly.\n\nFurthermore, building upon our critic-centric CriticLean pipeline, we propose the high-quality open-source Lean 4 statement dataset **FineLeanCorpus**, comprising 285,957 fully verified entries. When compared to the previous related datasets (e.g., LeanWorkBook [65]), FineLeanCorpus is distinguished by its diversity in mathematical domains, difficulty distribution, and strict semantic validation via critical feedback loops. Notably, its difficulty distribution and targeted domain enrichment create a more structurally balanced training environment, mitigating overfitting and transforming sparse topics into well-supported sub-domains. Furthermore, to foster research into the upper echelons of mathematical reasoning, we have curated the specialized subset called FineLeanCorpus-Diamond, comprising over 36,000 high-difficulty problems.\n\n## 2 Related Works\n\n### 2.1 Autoformalization\n\nAutoformalization [48, 60, 68] refers to the process by which AI systems parse natural language (NL) contents and translate them into machine-verifiable formal representations, such as those in theorem provers like Lean4 [38] or Isabelle [40]. Recent advances leverage large language models (LLMs) [72] to tackle this problem through two primary paradigms: (1) In-context learning [57], where models utilize annotated examples [28, 33, 60] to generate formalizations without explicit fine-tuning, (2) Supervised fine-tuning (e.g., [26, 61, 67]), which adapts general-purpose LLMs into domain-specific autoformalization experts. To assess correctness, prior works [26, 61, 67] employ LLM-as-judge [76] to verify semantic alignment between formal and informal statements. We advance this by training the first open-sourced, domain-specific light LLM on top of Qwen [52] family for critiquing Lean4 statement alignment via reinforcement learning [46], enhancingboth critique capability and formalization robustness.\n\n## 2.2 RL for LLM Reasoning\n\nThe exploration of complex reasoning capabilities in Large Language Models (LLMs) has achieved significant advancements [14, 17, 29–31, 55], with Reinforcement Learning (RL) establishing itself as a critical paradigm for transcending the constraints inherent to Supervised Fine-Tuning (SFT) [29, 32, 56, 66, 70]. Notable methodologies, including GRPO [11, 46], DAPO [66] have demonstrated substantial gains in mathematical reasoning and intricate problem-solving domains. However, the underlying mechanisms by which RL enhances reasoning capabilities remain insufficiently characterized. Empirical analyses increasingly indicate that RL primarily functions to activate, refine, or optimize the sampling of latent reasoning competencies rather than generating entirely novel cognitive frameworks de novo. For example, Yue et al. [69] interrogate whether current reinforcement learning frameworks incorporating verifiable rewards (RLVR) genuinely expand the frontier of reasoning performance or merely enhance the efficiency of retrieving pre-existing solutions.\n\n## 3 CriticLeanGPT\n\n### 3.1 CriticLeanBench\n\n#### 3.1.1 Overview of CriticLeanBench\n\nCriticLeanBench aims to evaluate the critical reasoning of LLMs in key aspects such as translating natural language mathematical statements into formally verified theorem declarations in Lean 4, including critique and correction. By integrating these core dimensions, CriticLeanBench can comprehensively measure the performance of models in Formalization tasks. In this section, we will elaborate on the construction principles and processes of CriticLeanBench; the construction process is shown in Figure 2.\n\nCriticLeanBench is constructed following the following principles: (1) It covers various types of errors, aiming to thoroughly evaluate the comprehensive capabilities of LLMs in capturing the semantic intent of formalized statements, using Template G for systematic assessment; (2) It incorporates diverse data sources to enhance the diversity and representativeness of evaluation data; and (3) It ensures the reliability and validity of the evaluation benchmark through a combination of expert review and automated verification.\n\n#### 3.1.2 Automatically verified\n\nThis section outlines the methodology employed to apply the Automatic Validation Filter, guided by predefined criteria for compiler and model-based verification.\n\n**Data Collection** We selected Math Statements from data sources [1, 16, 24, 36, 41, 43, 66], such as Omni-MATH [8], AIME [75], U-MATH [5], DEMI-MathAnalysis [6], HARDMath [7], OlympiadBench [13], and BlueMO [73], along with their corresponding Lean 4 Statements from public dataset [67].\n\n**Compiler Verified** We submitted the Lean 4 statements from the above dataset to the Lean 4 compiler. If the compilation succeeded, the results were passed to the DeepSeek R1 [11] model for further processing.\n\n- • **Compile false:** For statements that failed to compile, we randomly sampled 50 entries and retained the compiler feedback messages, which were included as part of our CriticLeanBench benchmark.\n\n**LLM Verified** For the data that has passed compilation, we utilize a template G to process each sample’s Math Statement and its corresponding Lean 4 Code Statement through the DeepSeek R1 large language model. The model is tasked with determining whether the Lean 4 Code Statement is consistent with the Math Statement, producing for each sample a tag indicating consistency or inconsistency along with a reasoning statement. To extract structured outputs from the model’s responses, we employ regular expression-based pattern matching. The results are then submitted to human reviewers for further validation.**Figure 2** An overview for the CriticLeanBench construction.\n\n### 3.1.3 Human Validation Filter\n\nThis section outlines the methodology employed to apply the Human Validation Filter, guided by predefined criteria (detailed in Appendix C).\n\nWe categorize the data into two groups based on whether the **Lean-compiled** autoformalization output semantically aligns with the refined statement. Therefore, a Lean-compiled autoformalization falls into the following:\n\n- • **Human Check right:** If the autoformalized statement both compiles and accurately captures the mathematical meaning, logic, and intended behavior of the original problem, it satisfies the semantic consistency criteria.\n- • **Human Check false:** If the autoformalized statement compiles but fails to accurately represent the original mathematical problem’s semantics. It violates one or more of the semantic consistency criteria, despite being syntactically valid Lean code. This often happens when there’s a mismatch between the code’s logic and the intended mathematical meaning.\n\nWithin the two categories, we select representative samples that mirror the characteristics of the original autoformalization statements while maximizing diversity within each subset and capturing the full spectrum of observed error types in the negative samples. This is achieved by balancing several factors:\n\n**Stratified Representation:** The selected samples should maintain a similar distribution across different strata of the original dataset. These strata are defined by:\n\n- • **Problem Complexity:** This encompasses factors like the number of variables, quantifiers, logical connectives, and the depth of nested mathematical structures.\n- • **Mathematical Branches:** The samples should represent the various mathematical domains present in the original data.\n- • **Statement Well-Formedness:** This refers to the degree to which the original mathematical statementsadhere to standard mathematical notation and conventions. This stratification ensures that the subsets reflect the variability in the quality of the original problem statements.\n\n**Comprehensive Error Coverage:** The negative samples are specifically chosen to exemplify the full range of typical errors observed in the autoformalization process. This range includes fundamental semantic and logical issues, such as Premise Translation Errors (e.g., incorrect domains or missing conditions), Mathematical Representation Errors (e.g., faulty expressions or definitions), and Goal Translation Errors. The set also covers issues such as Incorrect Assumptions, logical flaws like Operator & Parenthesis Errors (e.g., misplaced quantifiers), and high-level structural problems like Incomplete Formalization, where crucial context is omitted (detailed in figure 9).\n\n### 3.1.4 Data Statistics\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Statistics&lt;/th>\n&lt;th>Number&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>&lt;b>#Problems&lt;/b>&lt;/td>\n&lt;td>500&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Correct Pairs&lt;/b>&lt;/td>\n&lt;td>250&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>- &lt;i>human check&lt;/i>&lt;/td>\n&lt;td>250&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Incorrect Pairs&lt;/b>&lt;/td>\n&lt;td>250&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>- &lt;i>human/compiler check&lt;/i>&lt;/td>\n&lt;td>200/50&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Question Tokens Length&lt;/b>&lt;/td>\n&lt;td>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>- &lt;i>max/min/avg&lt;/i>&lt;/td>\n&lt;td>1,583/495/700.94&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Benchmark&lt;/th>\n&lt;th>Critic&lt;/th>\n&lt;th>Lean&lt;/th>\n&lt;th>Test&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>CriticBench&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>CodeCriticBench&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>LLaVA-Critic&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>CriticLeanBench (ours)&lt;/b>&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 1** Dataset statistics and comparison of various code benchmark datasets.\n\nTable 1 (left) presents the dataset statistics for CriticLeanBench. The dataset contains a total of 500 problems, comprising 250 correct and 250 incorrect Q/GT (Question and GT label) pairs distributed across the collection. The questions exhibit a notable variation in length, with a maximum token count of 1,583 and a minimum of 495 tokens, calculated using the Qwen2.5 [4] tokenizer. On average, each question contains approximately 700.94 tokens. This characteristic distinguishes CriticLeanBench as a complex evaluation benchmark that requires models to process relatively lengthy inputs compared to those in standard datasets.\n\n### 3.1.5 Comparison to Other Benchmarks\n\nIn Table 1 (right), CriticLeanBench has the following features: (1) We focus on a modest data size of 500 samples, acknowledging the expensive manual annotation costs (ranging from tens to hundreds of dollars per instance) and prioritizing efficiency without compromising evaluation rigor; (2) We integrate both Critic and Lean functionalities, distinguishing ourselves from benchmarks like CriticBench [27] and CodeCriticBench [71] that lack Lean capabilities, and LLaVA-Critic [63] that omits both Lean capabilities and test evaluation components; (3) We incorporate a test component focused on translating mathematical statements into formally verified theorem declarations in Lean 4, offering a fine-grained evaluation framework to assess the correctness of model transformations. This aspect of evaluative completeness remains unmatched by existing datasets.\n\n## 4 CriticLeanInstruct\n\nTo enhance the CriticLeanGPT model’s efficacy in critically evaluating the successful transformation of mathematical statements into Lean code, we construct a comprehensive training dataset comprising 48,000 samples. This dataset consists of three high-quality components, designed to comprehensively improve the model’s critical thinking and reasoning capabilities.\n\nTo significantly broaden the CriticLeanGPT model’s knowledge coverage, we also integrates three times additional code and math [18] datasets, enabling it to more comprehensively understand mathematical concepts and Lean code structures.Specifically, the Seed Data, with a 1:3 mix of math and code, is termed **CriticLeanInstruct(16K)**. When combined with data augmentation while retaining the same ratio, it forms the full **CriticLeanInstruct** dataset.\n\n## 4.1 Seed Data\n\nThe seed data comprises 4,000 samples evenly split into 2,000 correct and 2,000 incorrect instances. For both correct and incorrect samples, human experts provided critical feedback [F](#). Additionally, the incorrect samples include compiler error messages generated by the Lean 4 Compiler as supplementary feedback. Then, we adopt the Gemini2.5-Pro [\\[9\\]](#) to extend the critical feedback to detailed Chain-of-Thought (CoT) explanations.\n\n**Figure 3** Distribution of Different Error Types.\n\nTo understand the primary failure modes, we analyzed the error distribution across the 2,000 incorrect samples in our seed data as illustrated in Figure 3. The analysis reveals two primary challenges: (1) Syntactic Barriers: The most frequent obstacles are syntactic, such as Type Error and Syntax Errors. These issues typically prevent the code from compiling, indicating a fundamental difficulty in mastering the formal language. (2) Semantic Gaps: Beyond syntax, these errors stem from a failure to interpret the natural language scenario and accurately model its key information. This is evident in high rates of errors when translating a problem’s core logical components—including its premises, goal, and mathematical representation. This semantic challenge is particularly acute in application-style \"word problems,\" where difficulty comprehending complex contexts leads to a fundamentally flawed formalization.\n\nDrawing from the error taxonomy (detailed in Appendix D) and building upon our initial annotation standards (detailed in Appendix C), we established a fine-grained checklist, which is provided in full in Appendix E. This checklist formalizes the observed error paradigms, providing the foundational framework for methodically constructing the negative samples used throughout our study.\n\n## 4.2 Data Augmentation\n\n### 4.2.1 Correct Samples\n\nWe selected **5560** correct mathematical statements and Lean code pairs from the FormalMATH [\\[67\\]](#) dataset and used the Gemini-2.5-Pro model to generate Critical Chain-of-Thought for initial assessment. To ensure data quality, we kept these samples where the model’s judgment is “correct.”## 4.2.2 Incorrect Samples\n\nWe provide two strategies to obtain the incorrect samples as follows:\n\n- • Based on OmniMath, we adopt the Kimina-Autoformalizer-7B [54] to generate the Lean 4 code statements, and we kept 2,000 Lean code snippets that failed to compile due to syntactic or logical issues during automated formalization processes. For each detected error, a detailed Chain-of-Thought (CoT) explanation was generated to elucidate the error’s cause, enabling the model to recognize common compilation error patterns and thereby enhance its understanding of Lean 4 code syntax.\n- • Based on correct mathematical statements and Lean 4 code from the FormalMATH [67] dataset, we implemented a three-step collaborative process to generate negative samples, aiming to enhance the CriticLeanGPT model’s ability to identify subtle errors and logical flaws. First, a checklist of various potential issues, refined by human experts, was established as shown in Appendix E. Second, the Gemini 2.5 Pro model was invoked to randomly select error types from this checklist and modify correct Lean code accordingly, generating incorrect samples (detailed in Appendix H). Then, we adopt the Gemini model to generate the critical Chain-of-Thought explanation.\n\n## 4.3 Training Paradigm\n\n*Supervised fine-tuning (SFT).* These models are instruction-tuned versions based on their respective pre-trained Qwen2.5 checkpoints, with a focus on improving their ability to interpret and formalize complex mathematical statements expressed in natural language. The CriticLeanInstruct 4 dataset includes Critic data consisting of mathematical statements converted into formally verified theorem declarations in Lean 4, along with three times as much code and mathematics data for SFT (Supervised Fine-Tuning). We used the LLaMA-Factory [77] framework to facilitate the fine-tuning process and optimize model performance.\n\n*Reinforcement Learning Optimization (RL).* The recent success of R1-style methods has demonstrated the effectiveness of online RL using discrete, rule-based rewards [45]. In our pipeline, Qwen2.5 series and Qwen3 [52] series are further refined using reinforcement learning signals derived from both format validation of the generated critic data and consistency checking between model predictions and expert-labeled ground truth (GT) labels. Specifically, the RL training data consists of 4,000 Seed Data 4.1, where each example transforms a mathematical statement into a corresponding formal proof in Lean 4. Based on this dataset, we apply a rule-based RL approach to optimize the model’s capability in judgment reasoning. More specifically, we mainly utilize the GRPO [46] algorithm within the VeRL [47] reinforcement learning framework, whose optimization objective is:\n\n$$J_{\\text{online}}(\\pi_{\\theta}; \\mathcal{D}) = \\mathbb{E}_{x \\sim \\mathcal{D}, \\{y_i\\}_{i=1}^G \\sim \\pi_{\\theta_{\\text{old}}}(y|x)} \\left[ \\frac{1}{G} \\sum_{i=1}^G \\min \\left( \\frac{\\pi_{\\theta}(y_i|x)}{\\pi_{\\theta_{\\text{old}}}(y_i|x)} A_i, \\text{clip} \\left( \\frac{\\pi_{\\theta}(y_i|x)}{\\pi_{\\theta_{\\text{old}}}(y_i|x)}, 1 - \\epsilon, 1 + \\epsilon \\right) A_i \\right) - \\beta D_{\\text{KL}}(\\pi_{\\theta} || \\pi_{\\text{ref}}) \\right] \\quad (1)$$\n\nwhere  $G$  is group size, and  $A_i$  is advantage. The reward function is designed as follows&lt;sup>1&lt;/sup>:\n\n$$r_{\\text{accuracy}} = \\begin{cases} 1, & \\text{if judgement} = \\text{label} \\\\ 0, & \\text{if judgement} \\neq \\text{label} \\end{cases} \\quad (2)$$\n\n$$r_{\\text{format}} = \\begin{cases} 1, & \\text{if format is right} \\\\ 0, & \\text{if format is wrong} \\end{cases} \\quad (3)$$\n\n$$r_{\\text{final}} = \\min(r_{\\text{accuracy}}, r_{\\text{format}}) \\quad (4)$$\n\n\n---\n\n&lt;sup>1&lt;/sup>We do not include a length penalty in rewards to encourage longer thinking.## 5 Experiments\n\n### 5.1 Experimental Setup\n\n**Baseline Models.** For the closed-sourced API models, we select the following models: Claude35\\_Sonnet2 [2], Doubao-1.5-pro-32k [12], Gemini 2.5 Pro [50], GPT-4o-2024-11-20 [42]. We select a group of the most advanced open-source LLMs to serve as critic models for evaluation, which includes various reasoning models (DeepSeek-R1 [11], QwQ-32B [53], Qwen3-8B [52], Qwen3-14B [52], Qwen3-32B [52]), DeepSeek-Prover models [62] (DeepSeek-Prover-V1.5-RL, DeepSeek-Prover-V1.5-SFT), Llama-3.3-70B-Instruct [10] and several Qwen models (Qwen2.5-Coder-7B-Instruct [19], Qwen2.5-Coder-32B-Instruct [19], Qwen2.5-7B-Instruct [51], Qwen2.5-14B-Instruct [51] and Qwen2.5-32B-Instruct [51]).\n\n**CriticLeanGPT Models.** We further evaluate three variants from the Qwen2.5 series and Qwen3 series. These are instruction-based models fine-tuned specifically on either the CriticLeanInstruct 4 dataset or the RL-based clean critic Seed Data 4.1. All open-source models are inferred using the vLLM [21] framework with default inference parameters.\n\n### 5.2 Main Results\n\n#### 5.2.1 Evaluation of Critic Capability\n\nAs indicated in Table 2, the experimental results clearly demonstrate the effectiveness of the CriticLeanGPT models trained on our CriticLeanInstruct, in converting natural language mathematical statements into Lean 4 formal theorem declarations. Within the CriticLeanBench benchmark, our CriticLeanGPT models trained via supervised fine-tuning (SFT) and reinforcement learning (RL), along with their enhanced variants—outperform a range of closed-source API models, open-source models, and baseline models, highlighting distinct advantages. These outcomes yield several key insights: (1) Reasoning models excel in critical tasks, with Gemini 2.5 Pro, QwQ-32B, Qwen3-32B, and DeepSeek-R1 all attaining scores above 80. When compared to baseline models, our Qwen3-32B-RL model, optimized through RL, achieves a strong accuracy level, underscoring the efficacy of both our training methodology and dataset. (3) Our innovative mixed SFT strategy substantially boosts the performance of the Qwen2.5 family, with notable improvements observed across the 7B, 14B, and 32B models. (4) Additionally, SFT and RL significantly strengthen the models’ capacity to identify erroneous samples, as evidenced by higher true negative rates (TNR) and lower false negative rates (FNR)—a critical enhancement for accurate detection of incorrect formalizations, which is indispensable for effective critical tasks.\n\n### 5.3 Ablation Study\n\n#### 5.3.1 Effect of Reasoning Data\n\nWe conduct an ablation study on CriticLeanBench to evaluate the impact of different training strategies. As shown in Table 3, incorporating code and math reasoning data significantly improves performance across all model sizes compared to using Seed Data 4.1. Specifically, using the CriticLeanInstruct 4, which samples Critic and non-Critic data at a ratio of 1:3, leads to substantial gains, demonstrating that integrating diverse reasoning tasks enhances the critical reasoning capabilities of the model. This suggests that multi-task learning with math and code data improves the critique abilities of mathematical formalization.\n\n#### 5.3.2 Effect of SFT Dataset Size\n\nFigure 6 highlights a notable parameter-dependent relationship between the size of the SFT dataset and key reasoning performance. Across all model scales, performance improvements are observed through SFT, albeit with varying degrees of fluctuation depending on the training set size. Smaller models (e.g., 7B) exhibit more pronounced gains as the dataset expands, whereas larger models (e.g., 32B) demonstrate a less consistent trend, with marginal improvements at lower data volumes but substantial gains at higher data volumes. These findings align with prior studies [39, 78], underscoring the interplay between model capacity, data scale, and performance optimization in SFT scenarios. The results emphasize the need for tailored strategies to balance data efficiency and model generalization, particularly for large-scale architectures.&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>ACC&lt;/th>\n&lt;th>TPR&lt;/th>\n&lt;th>FPR&lt;/th>\n&lt;th>TNR&lt;/th>\n&lt;th>FNR&lt;/th>\n&lt;th>Reasoning&lt;/th>\n&lt;th>Open-source&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"8\" style=\"text-align: center;\">&lt;b>SOTA LLMs&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Gemini-2.5-Pro&lt;/td>\n&lt;td>&lt;u>89.2&lt;/u>&lt;/td>\n&lt;td>&lt;u>95.6&lt;/u>&lt;/td>\n&lt;td>&lt;u>4.4&lt;/u>&lt;/td>\n&lt;td>&lt;u>82.8&lt;/u>&lt;/td>\n&lt;td>&lt;u>17.2&lt;/u>&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>QwQ-32B&lt;/td>\n&lt;td>&lt;u>86.4&lt;/u>&lt;/td>\n&lt;td>93.6&lt;/td>\n&lt;td>6.4&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>20.8&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-32B&lt;/td>\n&lt;td>85.6&lt;/td>\n&lt;td>&lt;b>96.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>4.0&lt;/b>&lt;/td>\n&lt;td>75.2&lt;/td>\n&lt;td>24.8&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-235B-A22B&lt;/td>\n&lt;td>84.8&lt;/td>\n&lt;td>90.4&lt;/td>\n&lt;td>9.6&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>20.8&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-R1&lt;/td>\n&lt;td>84.0&lt;/td>\n&lt;td>90.8&lt;/td>\n&lt;td>9.2&lt;/td>\n&lt;td>77.2&lt;/td>\n&lt;td>22.8&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-14B&lt;/td>\n&lt;td>83.6&lt;/td>\n&lt;td>92.4&lt;/td>\n&lt;td>7.6&lt;/td>\n&lt;td>74.8&lt;/td>\n&lt;td>25.2&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-8B&lt;/td>\n&lt;td>79.8&lt;/td>\n&lt;td>94.4&lt;/td>\n&lt;td>5.6&lt;/td>\n&lt;td>65.2&lt;/td>\n&lt;td>34.8&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Doubao-1.5-pro-32k&lt;/td>\n&lt;td>78.4&lt;/td>\n&lt;td>95.2&lt;/td>\n&lt;td>4.8&lt;/td>\n&lt;td>61.6&lt;/td>\n&lt;td>38.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Claude35-Sonnet&lt;/td>\n&lt;td>74.2&lt;/td>\n&lt;td>&lt;u>97.2&lt;/u>&lt;/td>\n&lt;td>&lt;u>2.8&lt;/u>&lt;/td>\n&lt;td>51.2&lt;/td>\n&lt;td>48.8&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>73.0&lt;/td>\n&lt;td>91.6&lt;/td>\n&lt;td>8.4&lt;/td>\n&lt;td>54.4&lt;/td>\n&lt;td>45.6&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>\n&lt;td>71.6&lt;/td>\n&lt;td>91.6&lt;/td>\n&lt;td>8.4&lt;/td>\n&lt;td>51.6&lt;/td>\n&lt;td>48.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.3-70B-Instruct&lt;/td>\n&lt;td>68.2&lt;/td>\n&lt;td>95.2&lt;/td>\n&lt;td>4.8&lt;/td>\n&lt;td>41.2&lt;/td>\n&lt;td>58.8&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4o-2024-11-20&lt;/td>\n&lt;td>67.8&lt;/td>\n&lt;td>95.6&lt;/td>\n&lt;td>4.4&lt;/td>\n&lt;td>40.0&lt;/td>\n&lt;td>60.0&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>66.6&lt;/td>\n&lt;td>80.4&lt;/td>\n&lt;td>19.6&lt;/td>\n&lt;td>52.8&lt;/td>\n&lt;td>47.2&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>\n&lt;td>65.4&lt;/td>\n&lt;td>88.4&lt;/td>\n&lt;td>11.6&lt;/td>\n&lt;td>42.4&lt;/td>\n&lt;td>57.6&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>60.8&lt;/td>\n&lt;td>89.6&lt;/td>\n&lt;td>10.4&lt;/td>\n&lt;td>32.0&lt;/td>\n&lt;td>68.0&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-Prover-V1.5-SFT&lt;/td>\n&lt;td>52.4&lt;/td>\n&lt;td>78.8&lt;/td>\n&lt;td>21.2&lt;/td>\n&lt;td>26.0&lt;/td>\n&lt;td>74.0&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-Prover-V1.5-RL&lt;/td>\n&lt;td>50.0&lt;/td>\n&lt;td>76.4&lt;/td>\n&lt;td>23.6&lt;/td>\n&lt;td>23.6&lt;/td>\n&lt;td>76.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"8\" style=\"text-align: center;\">&lt;b>CriticLeanGPT (Ours)&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-8B-RL&lt;/td>\n&lt;td>79.8&lt;/td>\n&lt;td>90.0&lt;/td>\n&lt;td>10.0&lt;/td>\n&lt;td>72.0&lt;/td>\n&lt;td>28.0&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-14B-RL&lt;/td>\n&lt;td>84.8&lt;/td>\n&lt;td>91.6&lt;/td>\n&lt;td>8.4&lt;/td>\n&lt;td>78.0&lt;/td>\n&lt;td>22.0&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-32B-RL&lt;/td>\n&lt;td>&lt;b>87.0&lt;/b>&lt;/td>\n&lt;td>88.4&lt;/td>\n&lt;td>11.6&lt;/td>\n&lt;td>&lt;u>85.6&lt;/u>&lt;/td>\n&lt;td>&lt;u>14.4&lt;/u>&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct-RL&lt;/td>\n&lt;td>68.6&lt;/td>\n&lt;td>85.6&lt;/td>\n&lt;td>14.4&lt;/td>\n&lt;td>51.6&lt;/td>\n&lt;td>48.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct-RL&lt;/td>\n&lt;td>69.4&lt;/td>\n&lt;td>85.2&lt;/td>\n&lt;td>14.8&lt;/td>\n&lt;td>53.6&lt;/td>\n&lt;td>46.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct-RL&lt;/td>\n&lt;td>72.0&lt;/td>\n&lt;td>60.4&lt;/td>\n&lt;td>39.6&lt;/td>\n&lt;td>&lt;b>83.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>16.4&lt;/b>&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct-SFT&lt;/td>\n&lt;td>69.8&lt;/td>\n&lt;td>94.4&lt;/td>\n&lt;td>5.6&lt;/td>\n&lt;td>45.2&lt;/td>\n&lt;td>54.8&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct-SFT&lt;/td>\n&lt;td>70.6&lt;/td>\n&lt;td>83.6&lt;/td>\n&lt;td>16.4&lt;/td>\n&lt;td>57.6&lt;/td>\n&lt;td>42.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct-SFT&lt;/td>\n&lt;td>76.2&lt;/td>\n&lt;td>85.2&lt;/td>\n&lt;td>14.8&lt;/td>\n&lt;td>67.2&lt;/td>\n&lt;td>32.8&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct-SFT-RL&lt;/td>\n&lt;td>68.2&lt;/td>\n&lt;td>90.4&lt;/td>\n&lt;td>9.6&lt;/td>\n&lt;td>46.0&lt;/td>\n&lt;td>54.0&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct-SFT-RL&lt;/td>\n&lt;td>74.6&lt;/td>\n&lt;td>81.6&lt;/td>\n&lt;td>18.4&lt;/td>\n&lt;td>67.6&lt;/td>\n&lt;td>32.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct-SFT-RL&lt;/td>\n&lt;td>78.6&lt;/td>\n&lt;td>88.0&lt;/td>\n&lt;td>12.0&lt;/td>\n&lt;td>69.2&lt;/td>\n&lt;td>30.8&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 2 Performance on CriticLeanBench.** The best, the second-best and the third-best scores for each indicator are shown in box, **bold** and underlined, respectively.&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>ACC&lt;/th>\n&lt;th>TPR&lt;/th>\n&lt;th>FPR&lt;/th>\n&lt;th>TNR&lt;/th>\n&lt;th>FNR&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"6\" style=\"text-align: center;\">&lt;b>7B Size Models&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>60.8&lt;/td>\n&lt;td>89.6&lt;/td>\n&lt;td>10.4&lt;/td>\n&lt;td>32.0&lt;/td>\n&lt;td>68.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct-SFT(Critic Only)&lt;/td>\n&lt;td>64.0&lt;/td>\n&lt;td>70.8&lt;/td>\n&lt;td>29.2&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">57.2&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">42.8&lt;/span>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct-SFT&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">69.8&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">94.4&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">5.6&lt;/span>&lt;/td>\n&lt;td>45.2&lt;/td>\n&lt;td>54.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\" style=\"text-align: center;\">&lt;b>14B Size Models&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>66.6&lt;/td>\n&lt;td>80.4&lt;/td>\n&lt;td>19.6&lt;/td>\n&lt;td>52.8&lt;/td>\n&lt;td>47.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct-SFT(Critic Only)&lt;/td>\n&lt;td>67.4&lt;/td>\n&lt;td>80.8&lt;/td>\n&lt;td>19.2&lt;/td>\n&lt;td>54.0&lt;/td>\n&lt;td>46.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct-SFT&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">70.6&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">83.6&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">16.4&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">57.6&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">42.4&lt;/span>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\" style=\"text-align: center;\">&lt;b>32B Size Models&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>73.0&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">91.6&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">8.4&lt;/span>&lt;/td>\n&lt;td>54.4&lt;/td>\n&lt;td>45.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct-SFT(Critic Only)&lt;/td>\n&lt;td>71.0&lt;/td>\n&lt;td>72.0&lt;/td>\n&lt;td>28.0&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">70.0&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">30.0&lt;/span>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct-SFT&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">76.2&lt;/span>&lt;/td>\n&lt;td>85.2&lt;/td>\n&lt;td>14.8&lt;/td>\n&lt;td>67.2&lt;/td>\n&lt;td>32.8&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 3 Comparison of model performance under different training strategies:** base model, SFT on Critic data only, and SFT on combined Critic, code, and math data. The best score for each indicator is shown in box.\n\n## 5.4 Analysis\n\n### 5.4.1 Scaling Analysis\n\nWe evaluate the performance of Qwen series models on CriticLeanBench across different model scales, including Qwen2.5-Coder, Qwen2.5-Instruct, Qwen2.5-Instruct-SFT, Qwen2.5-Instruct-SFT-RL, Qwen3, and Qwen3-RL. The results in Figure 4 show that the performance improves consistently as the model size increases, demonstrating a clear scaling law of LLMs on CriticLeanBench.\n\n### 5.4.2 Effect of Pass@k\n\nThe Pass@k metric serves as a means to identify the highest-quality answers from multi-modal large language models (MLLMs) for final responses, highlighting the models’ potential for enhancement through post-training techniques like Reinforcement Learning from Human Feedback (RLHF [25]) and Gradient Penalty Policy Optimization (GRPO [46]). In this study, Pass@k evaluations were conducted on Qwen2.5-7B-Instruct, Qwen2.5-7B-Instruct-SFT-RL, Qwen3-8B, and Qwen3-8B-RL using CriticLeanBench, with k set to 8 and 32, and evaluation metrics including Accuracy (ACC), True Positive Rate (TPR), and True Negative Rate (TNR).\n\nAs shown in Figure 5, we observe that models subjected to Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) achieve better overall performance. Considering Pass@32, the Accuracy of Qwen2.5-7B-Instruct is outperformed by that of Qwen2.5-7B-Instruct-SFT-RL, which has undergone SFT and RL processing, leading to a notable improvement in the overall correctness rate. Regarding the True Negative Rate, models without SFT and RL processing are more prone to misclassifying incorrect samples as correct, whereas processed models effectively mitigate such errors; this is evident in the higher TNR of Qwen2.5-7B-Instruct-SFT-RL compared to Qwen2.5-7B-Instruct at Pass@32, reducing the likelihood of\n\n**Figure 6 Comparison of model performance under different amounts of SFT data:** base model, CriticLeanInstruct(16K), and CriticLeanInstruct.**Figure 4** Scaling Analysis of LLMs on CriticLeanBench.  $\\hat{\\square}$  denoted closed-source LLMs.\n\nsuch misclassifications. A similar trend is observed in Qwen3-8B. Additionally, all models exhibit improved performance as  $k$  increases, suggesting that SFT- and RL-optimized models can more effectively select high-quality answers when provided with more candidate responses.\n\n## 6 FineLeanCorpus\n\nTo construct the FineLeanCorpus, we began by aggregating a vast and diverse collection of natural language mathematical problems. Sourcing from a wide array of materials, including high school olympiad datasets (e.g., AoPS, BlueMO), standard high school curricula (e.g., TAL-SCQ5), and undergraduate-level challenges (e.g., Omni-MATH), we ensured an extensive initial distribution in both the mathematical domain and difficulty. The first step in our process was to standardize this heterogeneous collection into a uniform, proof-based format, making each problem compatible with the Lean 4 theorem prover and ready for the subsequent formalization pipeline.\n\nThese standardized problems were then subjected to a rigorous, gated auto-formalization process powered by our CriticLean framework (Figure 1). The Kimina-Autoformalizer-7B model first generates a candidate formal statement. This statement must pass a syntactic check via the Lean 4 compiler; failure leads to regeneration. A successful compilation is followed by a semantic correctness check from our CriticLeanGPT model, with rejection also triggering a new attempt. This regenerative approach is critical, maximizing the yield from our source corpus by iteratively seeking a valid formalization. Finally, to further enhance precision, we apply a final filtering stage using another,\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Statistics&lt;/th>\n&lt;th>Number&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>#Problems&lt;/td>\n&lt;td>285957&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Length&lt;/b>&lt;/td>\n&lt;td>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;i>Statement&lt;/i>&lt;/td>\n&lt;td>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>maximum length&lt;/td>\n&lt;td>2980 tokens&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>minimum length&lt;/td>\n&lt;td>9 tokens&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>avg length&lt;/td>\n&lt;td>78.4 tokens&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;i>Lean Result(success)&lt;/i>&lt;/td>\n&lt;td>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>maximum length&lt;/td>\n&lt;td>768 tokens&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>minimum length&lt;/td>\n&lt;td>14 tokens&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>avg length&lt;/td>\n&lt;td>87.8 tokens&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 5** Dataset statistics of FineLeanCorpus.**Figure 5** Performance on CriticLeanBench using **Pass@k** metrics, where **k = 8** (left) and **k = 32** (right).\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Dataset&lt;/th>\n&lt;th>Difficulty Level&lt;/th>\n&lt;th>Size&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>AOPs [35]&lt;/td>\n&lt;td>High School Olympiad&lt;/td>\n&lt;td>199982&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepMath-103k [15]&lt;/td>\n&lt;td>Diverse&lt;/td>\n&lt;td>28538&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>NuminaMath-TIR [24]&lt;/td>\n&lt;td>High School&lt;/td>\n&lt;td>22847&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepTheorem [74]&lt;/td>\n&lt;td>High School Olympiad&lt;/td>\n&lt;td>15131&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepScaleR [34]&lt;/td>\n&lt;td>High School Olympiad&lt;/td>\n&lt;td>11544&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DAPO-Math-17k [66]&lt;/td>\n&lt;td>High School&lt;/td>\n&lt;td>4078&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Omni-MATH [8]&lt;/td>\n&lt;td>Undergraduate&lt;/td>\n&lt;td>1176&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>IneqMath [20]&lt;/td>\n&lt;td>High School Olympiad&lt;/td>\n&lt;td>963&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>BlueMO [73]&lt;/td>\n&lt;td>High School Olympiad&lt;/td>\n&lt;td>616&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>TAL-SCQ5K [37]&lt;/td>\n&lt;td>High School&lt;/td>\n&lt;td>393&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>OnlineMathContest&lt;/td>\n&lt;td>High School&lt;/td>\n&lt;td>70&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Multi-Source Math Competition&lt;/td>\n&lt;td>High School Olympiad&lt;/td>\n&lt;td>619&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 4** Overview of different sources for FineLeanCorpus.\n\nhigher-performance CriticLeanGPT model. Manual validation indicates that this step is expected to eliminate 74.7% of the remaining incorrect formalizations. The resulting corpus is characterized by its expressive range: natural language statements vary from a concise 9 tokens to a complex 2,980 tokens (avg. 78.4), while their corresponding Lean formalizations span from 14 to 768 tokens (avg. 87.8), reflecting the deep spectrum of complexity successfully captured by our pipeline.\n\nTo further analyze the differences between our FineLeanCorpus dataset and the Lean-Workbook, we employed the templates from Appendix J and Appendix I to assess the difficulty levels and classify the mathematical domains of the datasets using Doubao-1.5-pro [12]. A comparative analysis of our proposed FineLeanCorpus against Lean-Workbook (Figure 7, Figure 8, Table 4 and Table 5) reveals two fundamental advancements: (1) Scale and Coverage: Our corpus provides a significant quantitative expansion in both problem difficulty and domain coverage. This expansion is evident not only across nearly the entire difficulty spectrum—offering a much richer data pool for training foundational skills—but also in the substantial augmentation of high-volume domains like Intermediate Algebra and Elementary Number Theory. (2) FineLeanCorpus exhibits a more diverse and structurally balanced profile, achieved by collecting natural language statements from numerous sources. From a difficulty perspective, it features a multimodal distribution with substantial problem counts at several distinct complexity points, in stark contrast to the unimodal distribution of Lean-Workbook. This characteristic is crucial for mitigating model overfitting to a narrow complexity band. From a domain perspective, it substantially reinforces previously underrepresented areas. For instance, categories such as Analytic Geometry and Integral Calculus are significantly expanded, while niche topics like Algorithms and Graph Theory are also robustly augmented. This targeted enrichment transforms sparsely sampled topics into well-supported, learnable sub-domains, yielding a more comprehensive dataset designed to fosterholistic reasoning capabilities. More details regarding our FineLeanCorpus dataset, including its fine-grained mathematical domain distribution (see Appendix A), are provided for further analysis.\n\nFurthermore, to push the boundaries of current models and foster research into the upper echelons of mathematical reasoning, we have curated a specialized training subset from FineLeanCorpus, which we designate as Diamond. This subset comprises 36,033 problems with a difficulty rating exceeding 5. The purpose of this high-difficulty training set is to create a demanding training environment that fosters the development of the sophisticated, multi-step reasoning required to tackle the most formidable mathematical problems. A detailed breakdown of the mathematical domain distribution within this subset is provided in table 11.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Dataset&lt;/th>\n&lt;th>Source&lt;/th>\n&lt;th>Theorems&lt;/th>\n&lt;th>Level&lt;/th>\n&lt;th>Detailed Critic Process&lt;/th>\n&lt;th>Difficulty Profile&lt;/th>\n&lt;th>Topic Diversity&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Lean-Workbook [65]&lt;/td>\n&lt;td>Synthetic&lt;/td>\n&lt;td>140K&lt;/td>\n&lt;td>Undergraduate&lt;/td>\n&lt;td>Opaque&lt;/td>\n&lt;td>Avg: 3.70&lt;br/>Top-tier (&lt;math>\\geq 6&lt;/math>): 7.81%&lt;/td>\n&lt;td>Highly Skewed&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>FineLeanCorpus (ours)&lt;/td>\n&lt;td>Synthetic&lt;/td>\n&lt;td>285K&lt;/td>\n&lt;td>Diverse&lt;/td>\n&lt;td>Transparent&lt;/td>\n&lt;td>Avg: 3.24&lt;br/>Top-tier (&lt;math>\\geq 6&lt;/math>): 11.10%&lt;/td>\n&lt;td>Balanced &amp; Diverse&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 6** Comparison of dataset statistics. FineLeanCorpus offers a transparent critic process, a higher proportion of top-tier problems, and a more balanced and diverse topic distribution compared to the highly skewed Lean-Workbook.\n\n**Figure 7** Comparison of dataset statistics. FineLeanCorpus offers a transparent critic process, a higher proportion of top-tier problems, and a more balanced and diverse topic distribution compared to the highly skewed Lean-Workbook.\n\n## 6.1 Analysis on CriticLean Pipeline\n\nAs shown in Table 7, our autoformalization pipeline significantly improves accuracy. We selected 50 problems from the Omni-MATH and applied the following three formalization strategies, with the correctness of all outputs confirmed by manual human inspection.\n\nOur baseline model, Kimina-Autoformalizer-7B, is used in each strategy: (1) a **Single Pass** baseline (38.0% accuracy); (2) a **Compiler Feedback** loop, where the model regenerates formalizations until they successfully compile (54.0% accuracy); (3) our **CriticLean Pipeline**, which extends this process, regenerating formalizations until they both compile successfully and are validated by our integrated **CriticLeanGPT Model** (84.0% accuracy).\n\nWhile compiler feedback resolves syntactical errors, it fails to detect logical flaws. Our pipeline addresses this gap. The integration of critic model, which performs deeper semantic and logical validation, is directly\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>AVG&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Kimina-Autoformalizer-7B&lt;/td>\n&lt;td>38.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Kimina-Autoformalizer-7B (Compiler)&lt;/td>\n&lt;td>54.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Kimina-Autoformalizer-7B (CriticLean)&lt;/td>\n&lt;td>84.0&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 7** Human evaluation accuracy results for autoformalization performance: The best score is highlighted in *box*.**Figure 8** Math Domain Distributions: FineLeanCorpus vs. Lean-Workbook.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th># Attempt&lt;/th>\n&lt;th>1&lt;/th>\n&lt;th>5&lt;/th>\n&lt;th>10&lt;/th>\n&lt;th>50&lt;/th>\n&lt;th>100&lt;/th>\n&lt;th>200&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Count / Ratio&lt;/td>\n&lt;td>63 / 12.6%&lt;/td>\n&lt;td>137 / 27.4%&lt;/td>\n&lt;td>170 / 34.0%&lt;/td>\n&lt;td>229 / 45.8%&lt;/td>\n&lt;td>245 / 49.0%&lt;/td>\n&lt;td>264 / 52.8%&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 8 Effectiveness of the Multi-Attempt Strategy on Formalization Yield.** The table shows the cumulative number of successfully formalized problems retained by the critic model as the attempt limit increases. Statistics are from a 500-problem sample.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Dataset&lt;/th>\n&lt;th>Accuracy&lt;/th>\n&lt;th>Dataset&lt;/th>\n&lt;th>Accuracy&lt;/th>\n&lt;th>Dataset&lt;/th>\n&lt;th>Accuracy&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>NuminaMath-TIR [24]&lt;/td>\n&lt;td>78%&lt;/td>\n&lt;td>IneqMath [20]&lt;/td>\n&lt;td>96%&lt;/td>\n&lt;td>BlueMO [73]&lt;/td>\n&lt;td>86%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepMath-103k [16]&lt;/td>\n&lt;td>84%&lt;/td>\n&lt;td>DAPO-Math-17k [66]&lt;/td>\n&lt;td>69%&lt;/td>\n&lt;td>OnlineMathContest&lt;/td>\n&lt;td>88%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>AOPs [35]&lt;/td>\n&lt;td>73%&lt;/td>\n&lt;td>TAL-SCQ5K [37]&lt;/td>\n&lt;td>75%&lt;/td>\n&lt;td>Omni-MATH [8]&lt;/td>\n&lt;td>84%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepTheorem [74]&lt;/td>\n&lt;td>100%&lt;/td>\n&lt;td>DeepScaleR [34]&lt;/td>\n&lt;td>100%&lt;/td>\n&lt;td>&lt;/td>\n&lt;td>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 9** Human evaluation results of different sources.\n\nresponsible for the accuracy increase from 54.0% to 84.0%. By filtering out plausible but incorrect formalizations, our method provides a more robust path toward reliable autoformalization. These manually-verified results present strong empirical evidence for the efficacy of our approach.\n\nTable 8 shows our pipeline achieved a 52.8% success rate across 500 problems, where success required passing both syntactic validation and our critic model’s semantic check. The value of our multi-attempt strategy is evident: while only 12.6% of samples passed on the first try, the pipeline successfully recovered an additional 40.2% that would be discarded by single-pass systems. Conversely, the 47.2% failure rate within the 200-attempt limit highlights a fundamental bottleneck: the pipeline’s performance is ultimately constrained by the base auto-formalization model’s ability to produce a candidate our critic can approve.\n\nMoreover, as shown in Table 9, we also provide the human evaluation results of different sources. We observe that the accuracy varies across different sources, a discrepancy we attribute primarily to the differing domain and difficulty distributions of the respective datasets.&lt;sup>2&lt;/sup>\n\n&lt;sup>2&lt;/sup>Our human evaluation standard is particularly stringent. To calibrate our criteria, we inspected a random sample of 50## 7 Conclusion\n\nThis paper presents CriticLean, a comprehensive framework that positions the critic as a central component in the autoformalization of mathematical statements. Through the development of CriticLeanGPT and the construction of CriticLeanBench, we demonstrate that explicitly modeling and training the critic yields significant improvements in formalization quality. Our pipeline not only refines the translation process through semantic validation, but also enables the construction of FineLeanCorpus, which is validated by both compiler and critic.\n\n---\n\nentries from the Lean-Workbook, which yielded an accuracy of 84%.## **8 Contributions and Acknowledgments**\n\n### **Co-First Authors**\n\nZhongyuan Peng, Yifan Yao, Kaijing Ma\n\n### **Co-Authors**\n\nShuyue Guo, Yizhe Li, Yichi Zhang, Chenchen Zhang, Yifan Zhang, Zhouliang Yu, Luming Li, Minghao Liu, Yihang Xia, Jiawei Shen, Yuchen Wu, Yixin Cao, Zhaoxiang Zhang, Wenhao Huang\n\n### **Corresponding Authors**\n\nJiaheng Liu, Ge Zhang## References\n\n- [1] AI Research Group of TAL Education Group. K-12 handwritten mathematical expressions dataset (hme100k). &lt;https://ai.100tal.com/dataset>. Accessed: 2025-04-05.\n- [2] Anthropic. Claude 3.5 sonnet model card addendum, 2024. URL &lt;https://www.paperswithcode.com/paper/claude-3-5-sonnet-model-card-addendum>. Accessed: 2024-09-21.\n- [3] Zhangir Azerbayev, Bartosz Piotrowski, Hailey Schoelkopf, Edward W Ayers, Dragomir Radev, and Jeremy Avigad. Proofnet: Autoformalizing and formally proving undergraduate-level mathematics. [arXiv preprint arXiv:2302.12433](#), 2023.\n- [4] Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei Huang, Binyuan Hui, Luo Ji, Mei Li, Junyang Lin, Runji Lin, Dayiheng Liu, Gao Liu, Chengqiang Lu, Keming Lu, Jianxin Ma, Rui Men, Xingzhang Ren, Xuancheng Ren, Chuanqi Tan, Sinan Tan, Jianhong Tu, Peng Wang, Shijie Wang, Wei Wang, Shengguang Wu, Benfeng Xu, Jin Xu, An Yang, Hao Yang, Jian Yang, Shusheng Yang, Yang Yao, Bowen Yu, Hongyi Yuan, Zheng Yuan, Jianwei Zhang, Xingxuan Zhang, Yichang Zhang, Zhenru Zhang, Chang Zhou, Jingren Zhou, Xiaohuan Zhou, and Tianhang Zhu. Qwen technical report. [arXiv preprint arXiv:2309.16609](#), 2023.\n- [5] Konstantin Chernyshev, Vitaliy Polshkov, Ekaterina Artemova, Alex Myasnikov, Vlad Stepanov, Alexei Miasnikov, and Sergei Tilga. U-math: A university-level benchmark for evaluating mathematical skills in llms. [arXiv preprint arXiv:2412.03205](#), 2024.\n- [6] B.P. Demidovich. Problems in Mathematical Analysis. Edited by B. Demidovich. Translated From the Russian by G. Yankovsky. Russian Monographs and Texts on Advanced Mathematics and Physics. Mir Publishers, 1964. URL &lt;https://books.google.com/books?id=XdmpwgEACA AJ>.\n- [7] J Fan, S Martinson, EY Wang, K Hausknecht, J Brenner, D Liu, N Peng, C Wang, and MP Brenner. Hardmath: A benchmark dataset for challenging problems in applied mathematics. arxiv 2024. [arXiv preprint arXiv:2410.09988](#).\n- [8] Bofei Gao, Feifan Song, Zhe Yang, Zefan Cai, Yibo Miao, Qingxiu Dong, Lei Li, Chenghao Ma, Liang Chen, Runxin Xu, et al. Omni-math: A universal olympiad level mathematic benchmark for large language models. [arXiv preprint arXiv:2410.07985](#), 2024.\n- [9] Google. Gemini: A family of highly capable multimodal models, 2023.\n- [10] Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten, Alex Vaughan, et al. The llama 3 herd of models. [arXiv preprint arXiv:2407.21783](#), 2024.\n- [11] Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-R1: Incentivizing reasoning capability in LLMs via reinforcement learning. [arXiv preprint arXiv:2501.12948](#), 2025.\n- [12] Dong Guo, Faming Wu, Feida Zhu, Fuxing Leng, Guang Shi, Haobin Chen, Haoqi Fan, Jian Wang, Jianyu Jiang, Jiawei Wang, et al. Seed1. 5-vl technical report. [arXiv preprint arXiv:2505.07062](#), 2025.\n- [13] Chaoqun He, Renjie Luo, Yuzhuo Bai, Shengding Hu, Zhen Leng Thai, Junhao Shen, Jinyi Hu, Xu Han, Yujie Huang, Yuxiang Zhang, Jie Liu, Lei Qi, Zhiyuan Liu, and Maosong Sun. Olympiadbench: A challenging benchmark for promoting agi with olympiad-level bilingual multimodal scientific problems, 2024.\n- [14] Yancheng He, Shilong Li, Jiaheng Liu, Weixun Wang, Xingyuan Bu, Ge Zhang, Zhongyuan Peng, Zhaoxiang Zhang, Zhicheng Zheng, Wenbo Su, and Bo Zheng. Can large language models detect errors in long chain-of-thought reasoning?, 2025. URL &lt;https://arxiv.org/abs/2502.19361>.\n- [15] Zhiwei He, Tian Liang, Jiahao Xu, Qiuzhi Liu, Xingyu Chen, Yue Wang, Linfeng Song, Dian Yu, Zhenwen Liang, Wenxuan Wang, Zhuosheng Zhang, Rui Wang, Zhaopeng Tu, Haitao Mi, and Dong Yu. Deepmath-103k: A large-scale, challenging, decontaminated, and verifiable mathematical dataset for advancing reasoning. 2025. URL &lt;https://arxiv.org/abs/2504.11456>.\n- [16] Zhiwei He, Tian Liang, Jiahao Xu, Qiuzhi Liu, Xingyu Chen, Yue Wang, Linfeng Song, Dian Yu, Zhenwen Liang, Wenxuan Wang, et al. Deepmath-103k: A large-scale, challenging, decontaminated, and verifiable mathematical dataset for advancing reasoning. [arXiv preprint arXiv:2504.11456](#), 2025.- [17] Hui Huang, Yancheng He, Hongli Zhou, Rui Zhang, Wei Liu, Weixun Wang, Wenbo Su, Bo Zheng, and Jiaheng Liu. Think-j: Learning to think for generative llm-as-a-judge. [ArXiv](https://arxiv.org/abs/2505.14268), abs/2505.14268, 2025. URL &lt;https://api.semanticscholar.org/CorpusID:278769843>.\n- [18] Hugging Face. Open r1: A fully open reproduction of deepseek-r1, January 2025. URL &lt;https://github.com/huggingface/open-r1>.\n- [19] Binyuan Hui, Jian Yang, Zeyu Cui, Jiaxi Yang, Dayiheng Liu, Lei Zhang, Tianyu Liu, Jiajun Zhang, Bowen Yu, Kai Dang, et al. Qwen2. 5-coder technical report. [arXiv preprint arXiv:2409.12186](https://arxiv.org/abs/2409.12186), 2024.\n- [20] Sheng Jiayi, Lyu Luna, Jin Jikai, Xia Tony, Gu Alex, Zou James, and Lu Pan. Solving inequality proofs with large language models. [arXiv preprint arXiv:2506.07927](https://arxiv.org/abs/2506.07927), 2025.\n- [21] Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Gonzalez, Hao Zhang, and Ion Stoica. Efficient memory management for large language model serving with pagedattention. In [Proceedings of the ACM SIGOPS 29th Symposium on Operating Systems Principles](#), 2023.\n- [22] Leanprover Community. A read-eval-print-loop for Lean 4, 2023. &lt;https://github.com/leanprover-community/repl>.\n- [23] Aitor Lewkowycz, Anders Andreassen, David Dohan, Ethan Dyer, Henryk Michalewski, Vinay Ramasesh, Ambrose Slone, Cem Anil, Imanol Schlag, Theo Gutman-Solo, Yuhuai Wu, Behnam Neyshabur, Guy Gur-Ari, and Vedant Misra. Solving quantitative reasoning problems with language models, 2022. URL &lt;https://arxiv.org/abs/2206.14858>.\n- [24] Jia LI, Edward Beeching, Lewis Tunstall, Ben Lipkin, Roman Soletskyi, Shengyi Costa Huang, Kashif Rasul, Longhui Yu, Albert Jiang, Ziju Shen, Zihan Qin, Bin Dong, Li Zhou, Yann Fleureau, Guillaume Lample, and Stanislas Polu. NuminaMath tir. [&lt;https://huggingface.co/AI-MO/NuminaMath-TIR>] ([https://github.com/project-numina/aimo-progress-prize/blob/main/report/numina\\\\_dataset.pdf](https://github.com/project-numina/aimo-progress-prize/blob/main/report/numina_dataset.pdf)), 2024.\n- [25] Zihao Li, Zhuoran Yang, and Mengdi Wang. Reinforcement learning with human feedback: Learning dynamic choices via pessimism. [arXiv preprint arXiv:2305.18438](https://arxiv.org/abs/2305.18438), 2023.\n- [26] Yong Lin, Shange Tang, Bohan Lyu, Jiayun Wu, Hongzhou Lin, Kaiyu Yang, Jia Li, Mengzhou Xia, Danqi Chen, Sanjeev Arora, and Chi Jin. Goedel-prover: A frontier model for open-source automated theorem proving, 2025. URL &lt;https://arxiv.org/abs/2502.07640>.\n- [27] Zicheng Lin, Zhibin Gou, Tian Liang, Ruilin Luo, Haowei Liu, and Yujiu Yang. Criticbench: Benchmarking llms for critique-correct reasoning. [arXiv preprint arXiv:2402.14809](https://arxiv.org/abs/2402.14809), 2024.\n- [28] Chengwu Liu, Jianhao Shen, Huajian Xin, Zhengying Liu, Ye Yuan, Haiming Wang, Wei Ju, Chuanyang Zheng, Yichun Yin, Lin Li, et al. Fimo: A challenge formal dataset for automated theorem proving. [arXiv preprint arXiv:2309.04295](https://arxiv.org/abs/2309.04295), 2023.\n- [29] Jiaheng Liu, Ken Deng, Congnan Liu, Jian Yang, Shukai Liu, He Zhu, Peng Zhao, Linzheng Chai, Yanan Wu, Ke Jin, et al. M2rc-eval: Massively multilingual repository-level code completion evaluation. [arXiv preprint arXiv:2410.21157](https://arxiv.org/abs/2410.21157), 2024.\n- [30] Jiaheng Liu, Chenchen Zhang, Jinyang Guo, Yuanxing Zhang, Haoran Que, Ken Deng, Zhiqi Bai, Jie Liu, Ge Zhang, Jiakai Wang, Yanan Wu, Congnan Liu, Jiamang Wang, Lin Qu, Wenbo Su, and Bo Zheng. DDK: Distilling domain knowledge for efficient large language models. In [The Thirty-eighth Annual Conference on Neural Information Processing Systems](#), 2024. URL &lt;https://openreview.net/forum?id=xgiurUq0ss>.\n- [31] Jiaheng Liu, Dawei Zhu, Zhiqi Bai, Yancheng He, Huanxuan Liao, Haoran Que, Zekun Wang, Chenchen Zhang, Ge Zhang, Jiebin Zhang, et al. A comprehensive survey on long context language modeling. [arXiv preprint arXiv:2503.17407](https://arxiv.org/abs/2503.17407), 2025.\n- [32] Mingjie Liu, Shizhe Diao, Ximing Lu, Jian Hu, Xin Dong, Yejin Choi, Jan Kautz, and Yi Dong. ProRL: Prolonged reinforcement learning expands reasoning boundaries in large language models. [arXiv preprint arXiv:2505.24864](https://arxiv.org/abs/2505.24864), 2025.\n- [33] Jianqiao Lu, Yingjia Wan, Zhengying Liu, Yinya Huang, Jing Xiong, Chengwu Liu, Jianhao Shen, Hui Jin, Jipeng Zhang, Haiming Wang, Zhicheng Yang, Jing Tang, and Zhijiang Guo. Process-driven autoformalization in lean 4, 2024. URL &lt;https://arxiv.org/abs/2406.01940>.- [34] Michael Luo, Sijun Tan, Justin Wong, Xiaoxiang Shi, William Tang, Manan Roongta, Colin Cai, Jeffrey Luo, Tianjun Zhang, Erran Li, Raluca Ada Popa, and Ion Stoica. DeepScaler: Surpassing o1-preview with a 1.5b model by scaling rl. &lt;https://pretty-radio-b75.notion.site/DeepScaleR-Surpassing-O1-Preview-with-a-1-5B-Model-by-Scaling-RL-19681902c1468005bed8ca303013a4e> 2025. Notion Blog.\n- [35] Sadegh Mahdavi, Muchen Li, Kaiwen Liu, Christos Thrampoulidis, Leonid Sigal, and Renjie Liao. Leveraging online olympiad-level math problems for llms training and contamination-resistant evaluation, 2025. URL &lt;https://arxiv.org/abs/2501.14275>.\n- [36] Sadegh Mahdavi, Muchen Li, Kaiwen Liu, Christos Thrampoulidis, Leonid Sigal, and Renjie Liao. Leveraging online olympiad-level math problems for llms training and contamination-resistant evaluation. [arXiv preprint arXiv:2501.14275](#), 2025.\n- [37] Math-eval. TAL-SCQ5K. &lt;https://github.com/math-eval/TAL-SCQ5K>, 2023.\n- [38] Leonardo de Moura and Sebastian Ullrich. The lean 4 theorem prover and programming language. In Automated Deduction – CADE 28: 28th International Conference on Automated Deduction, Virtual Event, July 12–15, 2021, Proceedings, page 625–635, Berlin, Heidelberg, 2021. Springer-Verlag. ISBN 978-3-030-79875-8. doi: 10.1007/978-3-030-79876-5\\_37. URL [https://doi.org/10.1007/978-3-030-79876-5\\\\_37](https://doi.org/10.1007/978-3-030-79876-5_37).\n- [39] Niklas Muennighoff, Zitong Yang, Weijia Shi, Xiang Lisa Li, Li Fei-Fei, Hannaneh Hajishirzi, Luke Zettlemoyer, Percy Liang, Emmanuel Candès, and Tatsunori Hashimoto. s1: Simple test-time scaling. [arXiv preprint arXiv:2501.19393](#), 2025.\n- [40] Tobias Nipkow, Markus Wenzel, and Lawrence C. Paulson. Isabelle/HOL: a proof assistant for higher-order logic. Springer-Verlag, Berlin, Heidelberg, 2002. ISBN 3540433767.\n- [41] Online Math Contest. Online math contest. &lt;https://onlinemathcontest.com/>. Accessed: 2025-04-05.\n- [42] R OpenAI. Gpt-4 technical report. arxiv 2303.08774. [View in Article](#), 2(5), 2023.\n- [43] Miguel Angel Peñaloza Perez, Bruno Lopez Orozco, Jesus Tadeo Cruz Soto, Michelle Bruno Hernandez, Miguel Angel Alvarado Gonzalez, and Sandra Malagon. Ai4math: A native spanish benchmark for university-level mathematical reasoning in large language models. [arXiv preprint arXiv:2505.18978](#), 2025.\n- [44] Peter Scholze. Liquid tensor experiment. Experimental Mathematics, 31(2):349–354, 2022.\n- [45] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, Y. K. Li, Y. Wu, and Daya Guo. Deepseekmath: Pushing the limits of mathematical reasoning in open language models, 2024. URL &lt;https://arxiv.org/abs/2402.03300>.\n- [46] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Y Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. [arXiv preprint arXiv:2402.03300](#), 2024.\n- [47] Guangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua Peng, Haibin Lin, and Chuan Wu. Hybridflow: A flexible and efficient rlhf framework. [arXiv preprint arXiv: 2409.19256](#), 2024.\n- [48] Christian Szegedy. A promising path towards autoformalization and general artificial intelligence. In Intelligent Computer Mathematics: 13th International Conference, CICM 2020, Bertinoro, Italy, July 26–31, 2020, Proceedings 13, pages 3–20. Springer, 2020.\n- [49] Terence Tao. The polynomial freiman-ruzsa conjecture, 2023. &lt;https://github.com/teorth/pf>.\n- [50] Gemini Team, Rohan Anil, Sebastian Borgeaud, Jean-Baptiste Alayrac, Jiahui Yu, Radu Soricut, Johan Schalkwyk, Andrew M Dai, Anja Hauth, Katie Millican, et al. Gemini: a family of highly capable multimodal models. [arXiv preprint arXiv:2312.11805](#), 2023.\n- [51] Qwen Team. Qwen2.5: A party of foundation models, September 2024. URL &lt;https://qwenlm.github.io/blog/qwen2.5/>.\n- [52] Qwen Team. Qwen3 technical report, 2025. URL &lt;https://arxiv.org/abs/2505.09388>.\n- [53] Qwen Team. Qwq-32b: Embracing the power of reinforcement learning, March 2025. URL &lt;https://qwenlm.github.io/blog/qwq-32b/>.- [54] Haiming Wang, Mert Unsal, Xiaohan Lin, Mantas Baksys, Junqi Liu, Marco Dos Santos, Flood Sung, Marina Vinyes, Zhenzhe Ying, Zekai Zhu, Jianqiao Lu, Hugues de Saxcé, Bolton Bailey, Chendong Song, Chenjun Xiao, Dehao Zhang, Ebony Zhang, Frederick Pu, Han Zhu, Jiawei Liu, Jonas Bayer, Julien Michel, Longhui Yu, Léo Dreyfus-Schmidt, Lewis Tunstall, Luigi Pagani, Moreira Machado, Pauline Bourigault, Ran Wang, Stanislas Polu, Thibaut Barroyer, Wen-Ding Li, Yazhe Niu, Yann Fleureau, Yangyang Hu, Zhouliang Yu, Zihan Wang, Zhilin Yang, Zhengying Liu, and Jia Li. Kimina-prover preview: Towards large formal reasoning models with reinforcement learning. 2025. URL &lt;http://arxiv.org/abs/2504.11354>.\n- [55] Weixun Wang, Shaopan Xiong, Gengru Chen, Wei Gao, Sheng Guo, Yancheng He, Ju Huang, Jiaheng Liu, Zhendong Li, Xiaoyang Li, Zichen Liu, Haizhou Zhao, Dakai An, Lunxi Cao, Qi Cao, Wanxi Deng, Feilei Du, Yiliang Gu, Jiahe Li, Xiang Li, Mingjie Liu, Yijia Luo, Zihe Liu, Yadao Wang, Pei Wang, Tianyuan Wu, Yanan Wu, Yuheng Zhao, Shu-Man Zhao, Jin Yang, Si-Yue Yang, Ying Tan, Huimin Yi, Yuchi Xu, Yu-Ming Yuan, Xingyao Zhang, Lin Qu, Wenbo Su, Wei Wang, Jiamang Wang, and Boyuan Zheng. Reinforcement learning optimization for large-scale learning: An efficient and user-friendly scaling library. 2025.\n- [56] Yiping Wang, Qing Yang, Zhiyuan Zeng, Liliang Ren, Liyuan Liu, Baolin Peng, Hao Cheng, Xuehai He, Kuan Wang, Jianfeng Gao, Weizhu Chen, Shuohang Wang, Simon Shaolei Du, and Yelong Shen. Reinforcement learning for reasoning in large language models with one training example, 2025. URL &lt;https://arxiv.org/abs/2504.20571>.\n- [57] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models. *Advances in neural information processing systems*, 35:24824–24837, 2022.\n- [58] Sean Welleck, Jiacheng Liu, Ronan Le Bras, Hannaneh Hajishirzi, Yejin Choi, and Kyunghyun Cho. Naturalproofs: Mathematical theorem proving in natural language, 2021. URL &lt;https://arxiv.org/abs/2104.01112>.\n- [59] Sean Welleck, Jiacheng Liu, Ximing Lu, Hannaneh Hajishirzi, and Yejin Choi. Naturalprover: Grounded mathematical proof generation with language models, 2022. URL &lt;https://arxiv.org/abs/2205.12910>.\n- [60] Yuhuai Wu, Albert Q. Jiang, Wenda Li, Markus N. Rabe, Charles Staats, Mateja Jamnik, and Christian Szegedy. Autoformalization with large language models, 2022.\n- [61] Huajian Xin, Daya Guo, Zhihong Shao, Zhizhou Ren, Qihao Zhu, Bo Liu, Chong Ruan, Wenda Li, and Xiaodan Liang. Deepseek-prover: Advancing theorem proving in llms through large-scale synthetic data. *arXiv preprint arXiv:2405.14333*, 2024.\n- [62] Huajian Xin, Z. Z. Ren, Junxiao Song, Zhihong Shao, Wanjia Zhao, Haocheng Wang, Bo Liu, Liyue Zhang, Xuan Lu, Qiushi Du, Wenjun Gao, Qihao Zhu, Dejian Yang, Zhibin Gou, Z. F. Wu, Fuli Luo, and Chong Ruan. Deepseek-prover-v1.5: Harnessing proof assistant feedback for reinforcement learning and monte-carlo tree search. 2024. URL &lt;https://arxiv.org/abs/2408.08152>.\n- [63] Tianyi Xiong, Xiyao Wang, Dong Guo, Qinghao Ye, Haoqi Fan, Quanquan Gu, Heng Huang, and Chunyuan Li. Llava-critic: Learning to evaluate multimodal models. In *Proceedings of the Computer Vision and Pattern Recognition Conference*, pages 13618–13628, 2025.\n- [64] Kaiyu Yang, Gabriel Poesia, Jingxuan He, Wenda Li, Kristin Lauter, Swarat Chaudhuri, and Dawn Song. Formal mathematical reasoning: A new frontier in ai, 2024. URL &lt;https://arxiv.org/abs/2412.16075>.\n- [65] Huaiyuan Ying, Zijian Wu, Yihan Geng, Zheng Yuan, Dahua Lin, and Kai Chen. Lean workbook: A large-scale lean problem set formalized from natural language math problems, 2025. URL &lt;https://arxiv.org/abs/2406.03847>.\n- [66] Qiyong Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Tiantian Fan, GaoHong Liu, Lingjun Liu, Xin Liu, et al. DAPO: An open-source LLM reinforcement learning system at scale. *arXiv preprint arXiv:2503.14476*, 2025.\n- [67] Zhouliang Yu, Ruotian Peng, Keyi Ding, Yizhe Li, Zhongyuan Peng, Minghao Liu, Yifan Zhang, Zheng Yuan, Huajian Xin, Wenhao Huang, Yandong Wen, Ge Zhang, and Weiyang Liu. Formalmath: Benchmarking formal mathematical reasoning of large language models, 2025. URL &lt;https://arxiv.org/abs/2505.02735>.\n- [68] Zhouliang Yu, Yuhuan Yuan, Tim Z Xiao, Fuxiang Frank Xia, Jie Fu, Ge Zhang, Ge Lin, and Weiyang Liu. Generating symbolic world models via test-time scaling of large language models. *arXiv preprint arXiv:2502.04728*, 2025.- [69] Yang Yue, Zhiqi Chen, Rui Lu, Andrew Zhao, Zhaokai Wang, Shiji Song, and Gao Huang. Does reinforcement learning really incentivize reasoning capacity in LLMs beyond the base model? [arXiv preprint arXiv:2504.13837](#), 2025.\n- [70] Yu Yue, Yufeng Yuan, Qiyong Yu, Xiaochen Zuo, Ruofei Zhu, Wenyuan Xu, Jiaze Chen, Chengyi Wang, TianTian Fan, Zhengyin Du, et al. VAPO: Efficient and reliable reinforcement learning for advanced reasoning tasks. [arXiv preprint arXiv:2504.05118](#), 2025.\n- [71] Alexander Zhang, Marcus Dong, Jiaheng Liu, Wei Zhang, Yejie Wang, Jian Yang, Ge Zhang, Tianyu Liu, Zhongyuan Peng, Yingshui Tan, et al. Codecriticbench: A holistic code critique benchmark for large language models. [arXiv preprint arXiv:2502.16614](#), 2025.\n- [72] Ge Zhang, Scott Qu, Jiaheng Liu, Chenchen Zhang, Chenghua Lin, Chou Leuang Yu, Danny Pan, Esther Cheng, Jie Liu, Qunshu Lin, et al. Map-neo: Highly capable and transparent bilingual large language model series. [arXiv preprint arXiv:2405.19327](#), 2024.\n- [73] Yifan Zhang, Yifan Luo, and Yizhou Chen. Bluemo: A comprehensive collection of challenging mathematical olympiad problems from the little blue book series., 2024.\n- [74] Ziyin Zhang, Jiahao Xu, Zhiwei He, Tian Liang, Qiuzhi Liu, Yansi Li, Linfeng Song, Zhenwen Liang, Zhuosheng Zhang, Rui Wang, Zhaopeng Tu, Haitao Mi, and Dong Yu. Deeptheorem: Advancing llm reasoning for theorem proving through natural language and reinforcement learning, 2025. URL &lt;https://arxiv.org/abs/2505.23754>.\n- [75] Kunhao Zheng, Jesse Michael Han, and Stanislas Polu. Minif2f: a cross-system benchmark for formal olympiad-level mathematics. [arXiv preprint arXiv:2109.00110](#), 2021.\n- [76] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric Xing, et al. Judging llm-as-a-judge with mt-bench and chatbot arena. *Advances in Neural Information Processing Systems*, 36:46595–46623, 2023.\n- [77] Yaowei Zheng, Richong Zhang, Junhao Zhang, Yanhan Ye, Zheyuan Luo, Zhangchi Feng, and Yongqiang Ma. Llamafactory: Unified efficient fine-tuning of 100+ language models. In *Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations)*, Bangkok, Thailand, 2024. Association for Computational Linguistics. URL &lt;http://arxiv.org/abs/2403.13372>.\n- [78] Chunting Zhou, Pengfei Liu, Puxin Xu, Srinivasan Iyer, Jiao Sun, Yuning Mao, Xuezhe Ma, Avia Efrat, Ping Yu, Lili Yu, et al. Lima: Less is more for alignment. *Advances in Neural Information Processing Systems*, 36: 55006–55021, 2023.# Appendix\n\n## A Fine-Grained Domain Distribution of FineLeanCorpus\n\nThe following table illustrates the fine-grained domain distribution of the FineLeanCorpus by presenting its 50 most frequent mathematical topics for illustrative purposes. To enhance readability and highlight the hierarchical structure, entries are sorted alphabetically by Main Category, then Sub-Category, and Topic.\n\n**Table 10** Fine-Grained Domain Distribution of FineLeanCorpus\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Main Category&lt;/th>\n&lt;th>Sub-Category&lt;/th>\n&lt;th>Topic&lt;/th>\n&lt;th>Count&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td rowspan=\"8\">Algebra&lt;/td>\n&lt;td rowspan=\"5\">Intermediate Algebra&lt;/td>\n&lt;td>Diophantine Equations&lt;/td>\n&lt;td>23&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Functional Equations&lt;/td>\n&lt;td>30178&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Inequalities&lt;/td>\n&lt;td>75339&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>65171&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Polynomials&lt;/td>\n&lt;td>32424&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"3\">Linear Algebra&lt;/td>\n&lt;td>Matrices&lt;/td>\n&lt;td>4361&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>54&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Vector Spaces&lt;/td>\n&lt;td>2179&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"8\">Applied Mathematics&lt;/td>\n&lt;td>Algorithms&lt;/td>\n&lt;td>Greedy Algorithms&lt;/td>\n&lt;td>46&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"2\">Optimization&lt;/td>\n&lt;td>Linear Programming&lt;/td>\n&lt;td>258&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>3165&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>273&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"3\">Probability&lt;/td>\n&lt;td>Conditional Probability&lt;/td>\n&lt;td>363&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Expected Value&lt;/td>\n&lt;td>792&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>2417&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"8\">Calculus&lt;/td>\n&lt;td rowspan=\"4\">Differential Calculus&lt;/td>\n&lt;td>Applications of Derivatives&lt;/td>\n&lt;td>57&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Derivatives&lt;/td>\n&lt;td>14948&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Limits&lt;/td>\n&lt;td>787&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>5391&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"2\">Integral Calculus&lt;/td>\n&lt;td>Definite Integrals&lt;/td>\n&lt;td>15165&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>18761&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"4\">Other&lt;/td>\n&lt;td>Limits&lt;/td>\n&lt;td>1086&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Limits of Multivariable Functions&lt;/td>\n&lt;td>35&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Limits of Sequences&lt;/td>\n&lt;td>106&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>8592&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"8\">Combinatorics&lt;/td>\n&lt;td rowspan=\"2\">Constructive Combinatorics&lt;/td>\n&lt;td>Invariants&lt;/td>\n&lt;td>320&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>54&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"3\">Enumerative Combinatorics&lt;/td>\n&lt;td>Combinations&lt;/td>\n&lt;td>5579&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>10460&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Permutations&lt;/td>\n&lt;td>869&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"2\">Extremal Combinatorics&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>375&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Pigeonhole Principle&lt;/td>\n&lt;td>1377&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Graph Theory&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>42&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>(Continued) Distribution of Problems by Mathematical Topic\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Main Category&lt;/th>\n&lt;th>Sub-Category&lt;/th>\n&lt;th>Topic&lt;/th>\n&lt;th>Count&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td rowspan=\"4\">Discrete Mathematics&lt;/td>\n&lt;td>Logic&lt;/td>\n&lt;td>Propositional Logic&lt;/td>\n&lt;td>444&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>3994&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"2\">Set Theory&lt;/td>\n&lt;td>Cardinality&lt;/td>\n&lt;td>1262&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>1585&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"7\">Geometry&lt;/td>\n&lt;td rowspan=\"2\">Analytic Geometry&lt;/td>\n&lt;td>Conic Sections&lt;/td>\n&lt;td>1498&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>254&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"5\">Euclidean Geometry&lt;/td>\n&lt;td>Circles&lt;/td>\n&lt;td>1880&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Coordinate Geometry&lt;/td>\n&lt;td>3584&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>4172&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Transformations&lt;/td>\n&lt;td>404&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Triangles&lt;/td>\n&lt;td>7243&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"6\">Number Theory&lt;/td>\n&lt;td rowspan=\"6\">Elementary Number Theory&lt;/td>\n&lt;td>Diophantine Equations&lt;/td>\n&lt;td>17208&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Divisibility&lt;/td>\n&lt;td>21160&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Inequalities&lt;/td>\n&lt;td>42&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Modular Arithmetic&lt;/td>\n&lt;td>9284&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>18636&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Prime Numbers&lt;/td>\n&lt;td>12071&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n## B Fine-Grained Domain Distribution of FineLeanCorpus-Diamond\n\nThe following table illustrates the fine-grained domain distribution of the Diamond dataset, our high-difficulty subset, by presenting its 50 most frequent mathematical topics for illustrative purposes. To enhance readability and highlight the hierarchical structure, entries are sorted alphabetically by Main Category, then Sub-Category, and Topic.\n\n**Table 11** Fine-Grained Domain Distribution of FineLeanCorpus-Diamond\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Main Category&lt;/th>\n&lt;th>Sub-Category&lt;/th>\n&lt;th>Topic&lt;/th>\n&lt;th>Count&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td rowspan=\"7\">Algebra&lt;/td>\n&lt;td rowspan=\"4\">Intermediate Algebra&lt;/td>\n&lt;td>Functional Equations&lt;/td>\n&lt;td>6732&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Inequalities&lt;/td>\n&lt;td>12533&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>3621&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Polynomials&lt;/td>\n&lt;td>2798&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"3\">Linear Algebra&lt;/td>\n&lt;td>Matrices&lt;/td>\n&lt;td>955&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>7&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Vector Spaces&lt;/td>\n&lt;td>206&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Analysis&lt;/td>\n&lt;td>Real Analysis&lt;/td>\n&lt;td>Density of Sets&lt;/td>\n&lt;td>3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"5\">Applied Mathematics&lt;/td>\n&lt;td>Optimization&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>108&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"3\">Probability&lt;/td>\n&lt;td>Conditional Probability&lt;/td>\n&lt;td>9&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Expected Value&lt;/td>\n&lt;td>23&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>63&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Calculus&lt;/td>\n&lt;td>Differential Calculus&lt;/td>\n&lt;td>Derivatives&lt;/td>\n&lt;td>913&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>(Continued) Distribution of Problems by Mathematical Topic\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Main Category&lt;/th>\n&lt;th>Sub-Category&lt;/th>\n&lt;th>Topic&lt;/th>\n&lt;th>Count&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>&lt;/td>\n&lt;td>Differential Equations&lt;/td>\n&lt;td>3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>&lt;/td>\n&lt;td>Limits&lt;/td>\n&lt;td>31&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>375&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>Integral Calculus&lt;/td>\n&lt;td>Definite Integrals&lt;/td>\n&lt;td>2280&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>2666&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>Limits&lt;/td>\n&lt;td>44&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;/td>\n&lt;td>&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>814&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"10\">Combinatorics&lt;/td>\n&lt;td rowspan=\"2\">Constructive Combinatorics&lt;/td>\n&lt;td>Invariants&lt;/td>\n&lt;td>144&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>33&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"3\">Enumerative Combinatorics&lt;/td>\n&lt;td>Combinations&lt;/td>\n&lt;td>620&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>1165&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Permutations&lt;/td>\n&lt;td>70&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"2\">Extremal Combinatorics&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>201&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Pigeonhole Principle&lt;/td>\n&lt;td>442&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"2\">Graph Theory&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>18&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Trees&lt;/td>\n&lt;td>6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>3&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"4\">Discrete Mathematics&lt;/td>\n&lt;td>Logic&lt;/td>\n&lt;td>Propositional Logic&lt;/td>\n&lt;td>21&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>1260&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"2\">Set Theory&lt;/td>\n&lt;td>Cardinality&lt;/td>\n&lt;td>463&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>379&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"8\">Geometry&lt;/td>\n&lt;td rowspan=\"2\">Analytic Geometry&lt;/td>\n&lt;td>Conic Sections&lt;/td>\n&lt;td>29&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>21&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"5\">Euclidean Geometry&lt;/td>\n&lt;td>Circles&lt;/td>\n&lt;td>132&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Coordinate Geometry&lt;/td>\n&lt;td>45&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>306&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Transformations&lt;/td>\n&lt;td>15&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Triangles&lt;/td>\n&lt;td>1200&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>Other&lt;/td>\n&lt;td>6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td rowspan=\"6\">Number Theory&lt;/td>\n&lt;td rowspan=\"6\">Elementary Number Theory&lt;/td>\n&lt;td>Diophantine Equations&lt;/td>\n&lt;td>2106&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Divisibility&lt;/td>\n&lt;td>3877&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Inequalities&lt;/td>\n&lt;td>18&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Modular Arithmetic&lt;/td>\n&lt;td>1593&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Other&lt;/td>\n&lt;td>3523&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Prime Numbers&lt;/td>\n&lt;td>3699&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>Figure 9 Distribution of Different Error Types of CriticLeanBench.\n\n## C Formalization Quality Assessment Criteria\n\n### Formalization Quality Assessment Criteria\n\n#### I. Integrity & Accuracy of Mathematical Content\n\n- • **Conditions & Hypotheses:** Are all explicit premises, variable domains (e.g.,  $\\mathbb{N}$ ,  $\\mathbb{R}$ ,  $\\mathbb{F}_k$ ), index ranges (e.g.,  $a_0$  vs.  $a_1$ ), properties of specific objects (e.g., geometric shapes, algebraic structures), and implicit context (e.g., non-zero divisors) accurately translated? Are mathematical meanings preserved (e.g.,  $\\neq 0$  vs.  $> 0$ )?\n- • **Goals & Conclusions:** Are all goals/conclusions translated (including multiple parts/cases)? Is the goal type accurate (e.g., specific value, extremum, existence/uniqueness)? For extrema, is attainability addressed? Is the mathematical meaning accurately translated?\n\n#### II. Clarity & Correctness of Logical Structure\n\n- • **Propositional Structure:** Are logical connectives ( $\\leftrightarrow$ ,  $\\rightarrow$ ,  $\\wedge$ ,  $\\vee$ ,  $\\neg$ ) and quantifiers ( $\\forall$ ,  $\\exists$ ,  $\\exists!$ ) used correctly? Are quantifier order, scope, and nesting accurate (e.g., dependencies like  $\\forall \\epsilon > 0, \\exists \\delta > 0, \\dots$ )?\n- • **Relation of Conditions to Conclusions:** How do multiple premises combine (e.g.,  $(A \\wedge B) \\rightarrow C$  vs.  $A \\rightarrow (B \\rightarrow C)$ )? Are constraints within the correct scope?\n- • **Reasoning Path:** Does the formalization reflect the original logic and key steps without introducing flaws or altering proof difficulty?### III. Lean Conventions & Technical Accuracy\n\n- • **Syntax & Declarations:** Is the syntax (e.g., parentheses, keywords, type declarations) correct? Are theorem, example, lemma used appropriately?\n- • **Type System:** Do operations, parameters, and return values satisfy type constraints? Are numerals used in the correct type? Are mathematical concepts correctly mapped to Lean counterparts?\n- • **Definitions & Library Usage:** Are custom definitions clear? Are imports correct and non-redundant? Are standard symbols and operations used correctly (e.g., `Complex.abs`, `Nat.Prime`)?\n- • **Code Style & Readability:** Are names clear and consistent? Are there sufficient comments for complex parts? Is there any redundancy?\n\n### IV. Problem Comprehension & Overall Consistency\n\n- • **Grasping the Core:** Does the formalization capture the core mathematical idea?\n- • **Internal Self-Consistency:** Are there any logical contradictions between the translated parts?\n- • **Suitability for Formalization:** Is the problem suitable for formalization? Are assumptions/interpretations documented?\n\n### V. Formalization Strategy & Choices\n\n- • **Abstraction Level:** Is the abstraction level appropriate, avoiding unnecessary generalization or over-specification?\n- • **Alternative Evaluation:** Were alternatives considered? Was decomposition/modularization used for complex problems?\n\n### VI. Provability & Proof Assistance\n\n- • **Proof Complexity:** Does the formalization maintain a similar proof complexity? Were lemmas added to simplify the proof?\n- • **Automation Potential:** Is the structure amenable to automation tools?\n\n## D Error Taxonomy\n\n#### Error Taxonomy\n\n##### 1. Semantic and Logical Errors\n\n###### 1.1 Premise Translation Error\n\n- • **Description:** This error occurs when formalizing the given conditions, constraints, or assumptions from the original problem, resulting in a discrepancy between the logical premises in the Lean code and the problem's description.\n- • **Examples:** Failing to constrain variables to be positive, integers, or coprime as required; not ensuring that denominators in mathematical expressions are non-zero; omitting geometric constraints such as \"A, B, C form a triangle\" in geometry problems; not explicitly specifying the exact range of a variable. For instance, relationships between angles and sides must beprecisely defined in Lean, otherwise the resulting correspondence may not be unique.\n\nGenerated code\n\n## 1.2 Mathematical Representation Error\n\n- • **Description:** This error involves an inaccurate representation of the form and meaning of mathematical entities such as variables and expressions from the original problem. This leads to the formalized mathematical proposition in the code being inconsistent with the original problem, thereby undermining formal semantic correspondence.\n- • **Examples:** Formalizing a cubic polynomial as a quadratic one; mistranslating \"all eigenvalues are 1\" as \"the determinant is 1\"; simplifying a complex algebraic relationship into an incorrect equation; using the conclusion as a premise; mismatch of mathematical entities. An incorrect expression structure can change the intrinsic structure and semantics of the original mathematical expression, even if the computed result might happen to be the same. For example, incorrectly formalizing a finite nested expression (e.g.,  $2002 + 21(2001 + \\dots)$ ) as the sum of an infinite series.\n\n## 1.3 Goal Translation Error\n\n- • **Description:** The final goal or conclusion achieved by the code does not match what the problem asks for, failing to complete the specified task.\n- • **Examples:** The problem asks for a specific numerical value, but the code only proves its existence; the problem asks to calculate the radius of convergence, but the code incorrectly solves for the sum of the series; the final answer has a numerical calculation error or a formal writing error (e.g., writing a fraction  $n/m$  as  $m/n$ ). The final goal might also be translated incompletely, with omissions.\n\n## 1.4 Variable Usage Error\n\n- • **Description:** Improper use of a variable's type, scope, name, or index.\n- • **Examples:** Using natural numbers ( $\\mathbb{N}$ ) for a variable that requires real numbers ( $\\mathbb{R}$ ); off-by-one errors in summation or sequence indices; confusing or redefining variable names.\n\n## 1.5 Misuse of Mathematical Concepts\n\n- • **Description:** Incorrectly using a mathematical formalism in Lean to represent a different mathematical concept.\n- • **Examples:** Translating \"calculate the residue\" as \"find the limit\"; formalizing \"locally uniform convergence\" as \"pointwise convergence\"; treating a problem of counting unordered combinations (e.g., non-congruent triangles) as one of counting ordered tuples.\n\n## 1.6 Incorrect Assumption\n\n- • **Description:** Adding conditions that are not present in the original problem, which oversimplifies the problem or leads to an incorrect conclusion.\n- • **Example:** Introducing an unfounded assumption, such as a specific numerical value.\n\n## 2. Lean Syntax and Technical Errors\n\n- • **Description:** These are technical issues at the code level that prevent the code from compiling or cause unexpected runtime behavior.\n\n### 2.1 Syntax Error\n\n- • **Description:** The code does not conform to the basic syntax rules of Lean 4.\n- • **Examples:** A theorem statement is missing its name; the `by sorry` block to skip a proof is absent; incorrect keywords or symbols are used.Generated code\n\n## 2.2 Type Error\n\n- • **Description:** Performing incompatible operations on variables of different data types, including type mismatches and type casting errors.\n- • **Examples:** Performing division on a natural number ( $\\mathbb{N}$ ) and expecting a fractional result, but the outcome is floored to 0; failing to cast integers or natural numbers to real numbers before performing real-valued operations.\n\n## 2.3 Operator & Parenthesis Error\n\n- • **Description:** The calculation order of an expression does not match the intended logic due to misunderstandings of operator precedence, improper placement of quantifiers, or incorrect use of parentheses.\n- • **Example:**  $\\tan^2(\\frac{\\pi}{9})$  is incorrectly parsed as  $(\\frac{\\tan \\pi}{9})^2$ .\n\n## 2.4 Library Usage Error\n\n- • **Description:** Improper use of functions or definitions from `mathlib`.\n- • **Examples:** Using `.ncard` on an incorrect type of set; using a deprecated function name like `Complex.abs`.\n\n## 3. Translation Completeness and Other Meta-Errors\n\n- • **Description:** These errors reflect that the formalization fails to cover all requirements of the problem, or that the problem itself is difficult to formalize.\n\n### 3.1 Unformalizable Problem\n\n- • **Description:** The original problem description is vague, ambiguous, relies on diagrams, or involves real-world scenarios that are difficult to express in formal logic.\n- • **Examples:** The problem depends on a geometric figure that is not explicitly defined; a physical context or narrative scenario cannot be modeled precisely; the problem statement itself contains mathematical errors.\n\nGenerated code\n\n### 3.2 Incomplete Formalization\n\n- • **Description:** The code only formalizes part of the problem, omitting other requirements.\n- • **Examples:** Ignoring a \"prove or disprove\" requirement and assuming the statement is true by default; omitting multi-step derivation requirements from the problem.\n\n### 3.3 Improvable Code Style\n\n- • **Description:** The code may be logically correct but can be improved in terms of clarity, robustness, or adherence to conventions.\n- • **Examples:** Adding parentheses could enhance logical clarity; variable names are not intuitive; better use could be made of Lean's syntactic features.\n\n## E Complete Checklist for Lean4 Mathematical Formalization\n\n### Complete Checklist for Lean4 Mathematical Formalization\n\n#### Conditions & Hypotheses:\n\n1. 1. Completeness of Preconditions: Are all explicitly stated preconditions in the problem translated without omission?1. 2. Accuracy of Variable Domains: Are the domains of variables (e.g.,  $\\mathbb{N}, \\mathbb{N}^+, \\mathbb{R}$ , `Fin k`, `Set.Icc a b`) accurately translated?\n2. 3. Accuracy of Indexing: Do the starting points and ranges of sequence/function indices (e.g.,  $a_0$  vs  $a_1$ , `Finset.range n` vs `Finset.Icc l n`) align with the original intent?\n3. 4. Clarity of Object Properties: Are the properties of specific objects (e.g., geometric figures like trapezoids, incircles; algebraic structures like groups, rings) clearly expressed?\n4. 5. Inclusion of Implicit Conditions: Are common implicit contextual conditions in mathematics (e.g., non-zero divisors, non-negative radicands, non-degenerate geometric objects, definedness of functions/sequences at application points, default to real numbers if unspecified) appropriately added?\n5. 6. Accuracy of Conditional Semantics: Is the mathematical meaning of conditions (e.g., \"not equal to 0\" ( $\\neq 0$ ) vs \"greater than 0\" ( $> 0$ ), direction of inequality signs ( $>$  vs  $\\geq$ )) accurately translated?\n\n#### Goals & Conclusions:\n\n1. 1. Completeness of Goals/Conclusions: Are all goals/conclusions that need to be proven or solved translated? (Pay special attention to multi-part conclusions and multiple solution scenarios).\n2. 2. Precision of Goal Type: Is the type of goal to be solved precise (e.g., specific value, extremum, existence/uniqueness, universal property, equivalence relation, implication)?\n3. 3. Attainability in Extremum Problems: For extremum problems, is \"attainability\" explicitly stated (i.e., demonstrating not just an inequality, but also that equality can be achieved)?\n4. 4. Accuracy of Goal Semantics: Is the mathematical meaning of the goals accurately translated?\n\n#### Combination of Preconditions\n\n#### Logical Structure:\n\n1. 1. Accuracy of Logical Connectives: Does the use of logical connectives ( $\\leftrightarrow$  (iff),  $\\rightarrow$  (if...then...),  $\\wedge$  (and),  $\\vee$  (or),  $\\neg$  (not)) accurately reflect the logical relationships of the original proposition?\n2. 2. Appropriateness of Quantifiers: Is the use of quantifiers ( $\\forall$  (for all),  $\\exists$  (exists),  $\\exists!$  (exists uniquely)) appropriate?\n3. 3. Correctness of Quantifier Scope and Nesting: Do the order, scope, and nesting of quantifiers correctly express the dependencies between variables (e.g., in  $\\forall \\epsilon > 0, \\exists \\delta > 0, \\dots, \\delta$  depends on  $\\epsilon$ )?\n4. 4. Combination of Preconditions: How do multiple preconditions combine to affect the conclusion (e.g., differentiate  $(A \\wedge B) \\rightarrow C$  from  $A \\rightarrow (B \\rightarrow C)$ )?\n5. 5. Fidelity to Original Logic: Does the formalization faithfully represent the inherent logic and key steps of the original mathematical problem?\n\n#### Lean Technical Accuracy:\n\n1. 1. Correctness of Basic Syntax: Is the basic Lean syntax (parenthesis matching, keywords like `theorem`, `def`, `variable`, `let`, `by`) entirely correct?\n2. 2. Adherence to Type Constraints: Do all operations, function parameters, and return values satisfy Lean's type constraints?\n3. 3. Correct Mapping of Mathematical Concepts: Are mathematical concepts correctly mapped to their Lean counterparts?\n4. 4. Clarity of Custom Definitions: Are all custom functions, predicates, and notations used clearly defined?\n5. 5. Correctness of Imports: Are necessary definitions and lemmas correctly imported from Mathlib?**Overall Consistency:**\n\n1. 1. Capturing Core Mathematical Ideas: Does the formalization truly capture the core mathematical ideas and goals of the original problem?\n2. 2. Absence of Logical Contradictions: Are there any logical contradictions between the translated conditions, definitions, and goals?\n3. 3. Appropriateness for Formalization: Is the problem itself suitable for precise, unambiguous mathematical formalization?\n4. 4. Documentation of Assumptions: Are any assumptions or interpretative choices made during the formalization process documented?\n\n## F Prompt:Critical Feedback to CoT\n\n### Prompt:Critical Feedback to CoT\n\n**Instruction:** You will be provided with a mathematical text and its Lean4 code representation. Your task is to evaluate whether the Lean4 code accurately and semantically represents the mathematical text. You will be given a boolean indicating conversion success and potentially failure information. Based on this, use a step-by-step Chain of Thought (COT) to generate a detailed explanation for why the conversion is considered successful or failed, focusing on the semantic equivalence and formal correctness of the Lean4 code relative to the mathematical meaning. The Lean4 code must preserve the intended meaning in the mathematical text and use correct Lean4 syntax and structure.\n\n**Input:** You will receive the following four values:\n\n1. 1. **Mathematical Text:** A string containing mathematical content.\n2. 2. **Lean4Code:** A string representing the code equivalent of the mathematical text.\n3. 3. **Conversion Success:** A boolean value (True or False) indicating whether the mathematical text was successfully converted to the Lean4 code representation.\n4. 4. **Reason:** A string representing the code equivalent of the mathematical text.\n5. 5. If Conversion Success is True, this field will typically be empty. You must generate the detailed justification for the success.\n6. 6. If Conversion Success is False, this field will contain specific information pinpointing why the conversion failed. You must elaborate on this identified failure, incorporating the analysis modules described below.\n\n**Your Role:** You are an AI language assistant. Your role is to analyze the provided information and, using a step-by-step Chain of Thought (COT) approach, generate the explanation for the conversion's success (if indicated as successful) or elaborate on the identified failure information (if indicated as failed). **Guidelines:**\n\n1. 1. **Understand the Content:** Carefully read the mathematical text, the code representation, the Conversion Success value, and the Reason input (if Conversion Success is False).\n2. 2. **Generating the Explanation for Success (if Conversion Success is True):** If the conversion is successful, provide a detailed, step-by-step explanation using COT to justify why it is successful. Your justification should implicitly cover:\n   1. (a) **Mathematical Text Analysis:** Briefly identify the core mathematical components (definitions, variables, operations, relations, constraints, statements) present in the text.\n",
    "durationMs": 945,
    "url": "https://huggingface.co/papers/2507.06181"
  },
  "sourceToolAssistantUUID": "55197c63-d15c-48eb-81f7-ef6f93158156",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-27T18:17:33.605Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01T1n4iAZ6F4c2aRaYaPM73P`</summary>

```json
{
  "url": "https://huggingface.co/datasets/m-a-p/CriticLeanBench",
  "prompt": "Extract any accuracy numbers, model performance results, or leaderboard data from this CriticLeanBench dataset page. I need accuracy figures for different models evaluated on this benchmark."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "68b6fa0b-e3f3-464a-b990-e213b0301e05",
  "isSidechain": false,
  "requestId": "req_011CbTXqdGzLZ7RAdvPkpzoD",
  "type": "assistant",
  "uuid": "afbec88d-9db9-4db7-a517-5d65613c2fbe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKyp7Ma2WTz1NVyALJkb8J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1434,
      "cache_read_input_tokens": 27787,
      "output_tokens": 458,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1434,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 458,
          "cache_read_input_tokens": 27787,
          "cache_creation_input_tokens": 1434,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1434
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

_source line 56 · 2026-05-27T18:17:34.195Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019rhrRf6C9FCgy3zTfUmqUp`</summary>

```json
{
  "query": "CriticLeanGPT accuracy CriticLeanBench 87% 84% \"Qwen3-14B\" formalization critic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "afbec88d-9db9-4db7-a517-5d65613c2fbe",
  "isSidechain": false,
  "requestId": "req_011CbTXqdGzLZ7RAdvPkpzoD",
  "type": "assistant",
  "uuid": "009b5f28-8483-4b55-9b17-18236cde6b9d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QKyp7Ma2WTz1NVyALJkb8J",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1434,
      "cache_read_input_tokens": 27787,
      "output_tokens": 458,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1434,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 458,
          "cache_read_input_tokens": 27787,
          "cache_creation_input_tokens": 1434,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1434
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

_source line 57_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Aut…",
  "leafUuid": "009b5f28-8483-4b55-9b17-18236cde6b9d",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6"
}
```

---

### Runtime record

_source line 58_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise autoformalization TTRL paper with verified data and concrete curriculum",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6"
}
```

---

### Tool result

_source line 59 · 2026-05-27T18:17:38.871Z_

<details><summary>↩ Tool result · `toolu_01T1n4iAZ6F4c2aRaYaPM73P`</summary>

````text
# CriticLeanBench Model Performance Results

Based on the webpage content, here are the key performance metrics:

## Dataset Overview
- **Total Size**: 500 problem pairs (250 correct, 250 incorrect formalizations)
- **Average Input Length**: 700.94 tokens
- **Format**: Parquet, < 1K size category

## Evaluation Metrics Used
The benchmark recommends evaluating models using:
- **Accuracy (ACC)**
- **True Positive Rate (TPR)**
- **False Positive Rate (FPR)**
- **True Negative Rate (TNR)**
- **False Negative Rate (FNR)**

## Performance Results

While the page references **Table 2: "Performance on CriticLeanBench"** with results showing:
- Best scores (boxed)
- Second-best scores (bold)
- Third-best scores (underlined)

**The specific accuracy numbers and individual model performance figures are not displayed in the text content provided** — they appear only as an image file (`results.png`).

## Additional Resources
- **Scaling Analysis** (Figure 2) shows performance trends across model sizes
- The page notes that "ˆ denoted closed-source LLMs"
- Paper reference: [arXiv:2507.06181](https://arxiv.org/abs/2507.06181)

## Loading the Dataset
```python
from datasets import load_dataset

dataset = load_dataset("m-a-p/CriticLeanBench")
```

**Note**: To view the actual accuracy numbers and detailed leaderboard data, you would need to access the images or consult the referenced paper directly.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "afbec88d-9db9-4db7-a517-5d65613c2fbe",
  "isSidechain": false,
  "promptId": "4b0c0804-0c80-4fc4-bd2d-54c91b4a93a7",
  "type": "user",
  "uuid": "73e0d8be-2447-42aa-a89b-802113fbc554",
  "toolUseResult": {
    "bytes": 853528,
    "code": 200,
    "codeText": "OK",
    "result": "# CriticLeanBench Model Performance Results\n\nBased on the webpage content, here are the key performance metrics:\n\n## Dataset Overview\n- **Total Size**: 500 problem pairs (250 correct, 250 incorrect formalizations)\n- **Average Input Length**: 700.94 tokens\n- **Format**: Parquet, < 1K size category\n\n## Evaluation Metrics Used\nThe benchmark recommends evaluating models using:\n- **Accuracy (ACC)**\n- **True Positive Rate (TPR)**\n- **False Positive Rate (FPR)**\n- **True Negative Rate (TNR)**\n- **False Negative Rate (FNR)**\n\n## Performance Results\n\nWhile the page references **Table 2: \"Performance on CriticLeanBench\"** with results showing:\n- Best scores (boxed)\n- Second-best scores (bold)\n- Third-best scores (underlined)\n\n**The specific accuracy numbers and individual model performance figures are not displayed in the text content provided** — they appear only as an image file (`results.png`).\n\n## Additional Resources\n- **Scaling Analysis** (Figure 2) shows performance trends across model sizes\n- The page notes that \"ˆ denoted closed-source LLMs\"\n- Paper reference: [arXiv:2507.06181](https://arxiv.org/abs/2507.06181)\n\n## Loading the Dataset\n```python\nfrom datasets import load_dataset\n\ndataset = load_dataset(\"m-a-p/CriticLeanBench\")\n```\n\n**Note**: To view the actual accuracy numbers and detailed leaderboard data, you would need to access the images or consult the referenced paper directly.",
    "durationMs": 5263,
    "url": "https://huggingface.co/datasets/m-a-p/CriticLeanBench"
  },
  "sourceToolAssistantUUID": "afbec88d-9db9-4db7-a517-5d65613c2fbe",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Tool result

_source line 60 · 2026-05-27T18:17:40.245Z_

<details><summary>↩ Tool result · `toolu_019rhrRf6C9FCgy3zTfUmqUp`</summary>

```text
Web search results for query: "CriticLeanGPT accuracy CriticLeanBench 87% 84% "Qwen3-14B" formalization critic"

Links: [{"title":"(PDF) CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://www.researchgate.net/publication/393512361_CriticLean_Critic-Guided_Reinforcement_Learning_for_Mathematical_Formalization"},{"title":"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/criticlean-critic-guided-reinforcement-learning-mathematical-formalization"},{"title":"M-A-P CriticLean: Critic-Guided Reinforcement Learning for","url":"https://arxiv.org/pdf/2507.06181"},{"title":"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://openreview.net/pdf/604b63db1bbddb963505ecbeca441f5b94bd143c.pdf"},{"title":"[2507.06181] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://arxiv.org/abs/2507.06181"},{"title":"[2507.06181v1] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization","url":"https://arxiv.org/abs/2507.06181v1"},{"title":"GitHub - multimodal-art-projection/CriticLean · GitHub","url":"https://github.com/multimodal-art-projection/CriticLean"},{"title":"m-a-p/CriticLeanGPT-Qwen3-14B-RL · Hugging Face","url":"https://huggingface.co/m-a-p/CriticLeanGPT-Qwen3-14B-RL"},{"title":"m-a-p/CriticLeanBench · Datasets at Hugging Face","url":"https://huggingface.co/datasets/m-a-p/CriticLeanBench"},{"title":"CriticLeanBench: A Benchmark for Evaluating Mathematical Formalization Critics - 2077AI","url":"https://www.2077ai.com/dataset/dataset-criticlean"}]

Based on the search results, here's information about CriticLeanGPT accuracy on CriticLeanBench:

## Overview

CriticLeanGPT is trained via supervised fine-tuning and reinforcement learning to rigorously assess the semantic fidelity of Lean 4 formalizations. CriticLeanBench is a benchmark designed to measure models' ability to distinguish semantically correct from incorrect formalizations.

## Performance Results

The CriticLeanGPT models, particularly the Qwen3-32B-RL variant, achieve 87.0% accuracy compared to GPT-4o's 67.8%.

## Dataset Details

CriticLeanBench contains 500 carefully curated problem pairs with 250 correct and 250 incorrect formalizations. Each problem features relatively lengthy inputs with an average of 700.94 tokens.

## Key Findings

Within the CriticLeanBench benchmark, the CriticLeanGPT models trained via supervised fine-tuning and reinforcement learning outperform a range of closed-source API models, open-source models, and baseline models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "009b5f28-8483-4b55-9b17-18236cde6b9d",
  "isSidechain": false,
  "promptId": "4b0c0804-0c80-4fc4-bd2d-54c91b4a93a7",
  "type": "user",
  "uuid": "53e04d3f-2818-4d74-a984-7acbaaef065e",
  "toolUseResult": {
    "query": "CriticLeanGPT accuracy CriticLeanBench 87% 84% \"Qwen3-14B\" formalization critic",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UivCe1NWyeBefndHZTwitA",
        "content": [
          {
            "title": "(PDF) CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization",
            "url": "https://www.researchgate.net/publication/393512361_CriticLean_Critic-Guided_Reinforcement_Learning_for_Mathematical_Formalization"
          },
          {
            "title": "CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/criticlean-critic-guided-reinforcement-learning-mathematical-formalization"
          },
          {
            "title": "M-A-P CriticLean: Critic-Guided Reinforcement Learning for",
            "url": "https://arxiv.org/pdf/2507.06181"
          },
          {
            "title": "CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization",
            "url": "https://openreview.net/pdf/604b63db1bbddb963505ecbeca441f5b94bd143c.pdf"
          },
          {
            "title": "[2507.06181] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization",
            "url": "https://arxiv.org/abs/2507.06181"
          },
          {
            "title": "[2507.06181v1] CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization",
            "url": "https://arxiv.org/abs/2507.06181v1"
          },
          {
            "title": "GitHub - multimodal-art-projection/CriticLean · GitHub",
            "url": "https://github.com/multimodal-art-projection/CriticLean"
          },
          {
            "title": "m-a-p/CriticLeanGPT-Qwen3-14B-RL · Hugging Face",
            "url": "https://huggingface.co/m-a-p/CriticLeanGPT-Qwen3-14B-RL"
          },
          {
            "title": "m-a-p/CriticLeanBench · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/m-a-p/CriticLeanBench"
          },
          {
            "title": "CriticLeanBench: A Benchmark for Evaluating Mathematical Formalization Critics - 2077AI",
            "url": "https://www.2077ai.com/dataset/dataset-criticlean"
          }
        ]
      },
      "Based on the search results, here's information about CriticLeanGPT accuracy on CriticLeanBench:\n\n## Overview\n\nCriticLeanGPT is trained via supervised fine-tuning and reinforcement learning to rigorously assess the semantic fidelity of Lean 4 formalizations. CriticLeanBench is a benchmark designed to measure models' ability to distinguish semantically correct from incorrect formalizations.\n\n## Performance Results\n\nThe CriticLeanGPT models, particularly the Qwen3-32B-RL variant, achieve 87.0% accuracy compared to GPT-4o's 67.8%.\n\n## Dataset Details\n\nCriticLeanBench contains 500 carefully curated problem pairs with 250 correct and 250 incorrect formalizations. Each problem features relatively lengthy inputs with an average of 700.94 tokens.\n\n## Key Findings\n\nWithin the CriticLeanBench benchmark, the CriticLeanGPT models trained via supervised fine-tuning and reinforcement learning outperform a range of closed-source API models, open-source models, and baseline models."
    ],
    "durationSeconds": 6.046622770000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "009b5f28-8483-4b55-9b17-18236cde6b9d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 61 · 2026-05-27T18:17:40.248Z_

```json
{
  "parentUuid": "53e04d3f-2818-4d74-a984-7acbaaef065e",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "4547e632-4ee4-4c7b-be19-5f729a2e7a96",
  "timestamp": "2026-05-27T18:17:40.248Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 62 · 2026-05-27T18:17:43.866Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a crucial piece of information: CriticLeanGPT-Qwen3-32B-RL achieves 87.0% accuracy on CriticLeanBench. GPT-4o achieves 67.8%. But I still need the specific number for the 14B-RL variant.

Let me read the persisted output of the HuggingFace paper page to find the detailed results table.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4547e632-4ee4-4c7b-be19-5f729a2e7a96",
  "isSidechain": false,
  "requestId": "req_011CbTXrghQ4TxjzGhiGBr4J",
  "type": "assistant",
  "uuid": "901563b1-e81c-418a-bb49-296ab21b500a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016FxwBy5boRhzK1KYpbS2Hr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2471,
      "cache_read_input_tokens": 29221,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2471,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 296,
          "cache_read_input_tokens": 29221,
          "cache_creation_input_tokens": 2471,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2471
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

_source line 63 · 2026-05-27T18:17:44.350Z_

Let me read the persisted CriticLean paper content and get more specific accuracy numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "901563b1-e81c-418a-bb49-296ab21b500a",
  "isSidechain": false,
  "requestId": "req_011CbTXrghQ4TxjzGhiGBr4J",
  "type": "assistant",
  "uuid": "64e56c3f-60ab-4f4e-bd14-c366d4d3ae21",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016FxwBy5boRhzK1KYpbS2Hr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2471,
      "cache_read_input_tokens": 29221,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2471,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 296,
          "cache_read_input_tokens": 29221,
          "cache_creation_input_tokens": 2471,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2471
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

_source line 64 · 2026-05-27T18:17:45.470Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PpfyJtGEQkUgQ5b2GxgF3e`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/2a30fe45-086a-4752-b69b-cc68f89516e6/tool-results/toolu_016rqZDKmFkzrH3XvWTnogpJ.txt",
  "limit": 200,
  "offset": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "64e56c3f-60ab-4f4e-bd14-c366d4d3ae21",
  "isSidechain": false,
  "requestId": "req_011CbTXrghQ4TxjzGhiGBr4J",
  "type": "assistant",
  "uuid": "6f193386-f5dc-4747-8579-10fb58768d35",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016FxwBy5boRhzK1KYpbS2Hr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2471,
      "cache_read_input_tokens": 29221,
      "output_tokens": 296,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2471,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 296,
          "cache_read_input_tokens": 29221,
          "cache_creation_input_tokens": 2471,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2471
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

_source line 65 · 2026-05-27T18:17:45.481Z_

<details><summary>↩ Tool result · `toolu_01PpfyJtGEQkUgQ5b2GxgF3e`</summary>

```text
0	# CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization
1	
2	ByteDance Seed      Nanjing University
3	
4	Full author list in Contributions
5	
6	## Abstract
7	
8	Translating natural language mathematical statements into formal, executable code is a fundamental challenge in automated theorem proving. While prior work has focused on generation and compilation success, little attention has been paid to the *critic phase*—the evaluation of whether generated formalizations truly capture the semantic intent of the original problem. In this paper, we introduce **CriticLean**, a novel critic-guided reinforcement learning framework that elevates the role of the critic from a passive validator to an active learning component. Specifically, first, we propose the **CriticLeanGPT**, trained via supervised fine-tuning and reinforcement learning, to rigorously assess the semantic fidelity of Lean 4 formalizations. Then, we introduce **CriticLeanBench**, a benchmark designed to measure models’ ability to distinguish semantically correct from incorrect formalizations, and demonstrate that our trained CriticLeanGPT models can significantly outperform strong open- and closed-source baselines. Building on the CriticLean framework, we construct **FineLeanCorpus**, a dataset comprising over 285K problems that exhibits rich domain diversity, broad difficulty coverage, and high correctness based on human evaluation. Overall, our findings highlight that optimizing the critic phase is essential for producing reliable formalizations and we hope our CriticLean will provide valuable insights for future advances in formal mathematical reasoning.
9	
10	**Date:** July 8, 2025
11	
12	**Correspondence:** [liujiaheng@nju.edu.cn](mailto:liujiaheng@nju.edu.cn), [zhangge.eli@bytedance.com](mailto:zhangge.eli@bytedance.com)
13	
14	**Project Page:** &lt;https://github.com/multimodal-art-projection/CriticLean>
15	
16	## 1 Introduction
17	
18	The formalization of mathematical statements [64] is a critical task in modern mathematical computation, particularly in the context of theorem provers like Lean 4 [22]. The translation of natural language mathematical problems into formal, executable code remains a significant challenge, as it requires not only syntactical accuracy but also a deep understanding of the problem’s semantics [44, 49]. Existing approaches have shown progress, but they often face limitations in accuracy, especially in the context of complex, high-level problems that involve sophisticated mathematical reasoning [3, 23, 58, 59, 75]. In contrast to existing works, we argue that the *critic* phase—the step where the semantic correctness of generated formalizations is evaluated—is not only underexplored but also fundamentally essential to the success of mathematical autoformalization.
19	
20	Therefore, in this paper, we systematically investigate and optimize the critic component and introduce **CriticLean**, a comprehensive framework that places the critic model at the center of the formalization pipeline. Unlike prior work that primarily focuses on generation quality or compiler validity, CriticLean introduces the reinforcement learning-based **CriticLeanGPT** models explicitly trained to evaluate whether the Lean 4 output truly reflects the intent of the original mathematical statement., and we present a full methodology forThe diagram illustrates the CriticLean framework for mathematics autoformalization. It starts with a **Natural Language Statement** box containing a mathematical problem about permutations. This statement is processed by an **AutoFormalizer**. The AutoFormalizer's output is then evaluated by two verification steps: a **Verify** box for syntax checking and name resolution, and another **Verify** box for semantic meaning and logical consistency. The **Verify** boxes are supported by a **Lean Compiler** and **CriticLeanGPT** respectively. If a **Compilation Error** or **Critique Error** occurs, the AutoFormalizer receives feedback and iterates. If successful, the final output is a **Lean Formal Language Statement** box showing the formalized theorem.
21	
22	**Figure 1** Illustration of CriticLean framework based on Critic-Guided Reinforcement Learning for Mathematics Autoformalization.
23	
24	training, and evaluating CriticLeanGPT model. Specifically, as shown in Figure 1, for each natural language statement, we apply the autoformalization iteratively based on the feedback from the Lean compiler and the CriticLeanGPT models, which is trained to critically assess whether a generated formalization accurately represents the semantics of the original mathematical statement. In each iteration, the feedback provides valuable signals that drive an iterative refinement process, further improving the quality of the final Lean code output.
25	
26	Additionally, we present **CriticLeanBench**, a benchmark designed to evaluate the performance of CriticLeanGPT models, which contain 500 natural language and Lean 4 language statement pairs (i.e., 250 correct and 250 incorrect pairs). Through extensive experiments, we demonstrate that our trained CriticLeanGPT models outperform the SOTA open-source models [4, 10, 11] and many closed-source API models [9, 12, 42] greatly.
27	
28	Furthermore, building upon our critic-centric CriticLean pipeline, we propose the high-quality open-source Lean 4 statement dataset **FineLeanCorpus**, comprising 285,957 fully verified entries. When compared to the previous related datasets (e.g., LeanWorkBook [65]), FineLeanCorpus is distinguished by its diversity in mathematical domains, difficulty distribution, and strict semantic validation via critical feedback loops. Notably, its difficulty distribution and targeted domain enrichment create a more structurally balanced training environment, mitigating overfitting and transforming sparse topics into well-supported sub-domains. Furthermore, to foster research into the upper echelons of mathematical reasoning, we have curated the specialized subset called FineLeanCorpus-Diamond, comprising over 36,000 high-difficulty problems.
29	
30	## 2 Related Works
31	
32	### 2.1 Autoformalization
33	
34	Autoformalization [48, 60, 68] refers to the process by which AI systems parse natural language (NL) contents and translate them into machine-verifiable formal representations, such as those in theorem provers like Lean4 [38] or Isabelle [40]. Recent advances leverage large language models (LLMs) [72] to tackle this problem through two primary paradigms: (1) In-context learning [57], where models utilize annotated examples [28, 33, 60] to generate formalizations without explicit fine-tuning, (2) Supervised fine-tuning (e.g., [26, 61, 67]), which adapts general-purpose LLMs into domain-specific autoformalization experts. To assess correctness, prior works [26, 61, 67] employ LLM-as-judge [76] to verify semantic alignment between formal and informal statements. We advance this by training the first open-sourced, domain-specific light LLM on top of Qwen [52] family for critiquing Lean4 statement alignment via reinforcement learning [46], enhancingboth critique capability and formalization robustness.
35	
36	## 2.2 RL for LLM Reasoning
37	
38	The exploration of complex reasoning capabilities in Large Language Models (LLMs) has achieved significant advancements [14, 17, 29–31, 55], with Reinforcement Learning (RL) establishing itself as a critical paradigm for transcending the constraints inherent to Supervised Fine-Tuning (SFT) [29, 32, 56, 66, 70]. Notable methodologies, including GRPO [11, 46], DAPO [66] have demonstrated substantial gains in mathematical reasoning and intricate problem-solving domains. However, the underlying mechanisms by which RL enhances reasoning capabilities remain insufficiently characterized. Empirical analyses increasingly indicate that RL primarily functions to activate, refine, or optimize the sampling of latent reasoning competencies rather than generating entirely novel cognitive frameworks de novo. For example, Yue et al. [69] interrogate whether current reinforcement learning frameworks incorporating verifiable rewards (RLVR) genuinely expand the frontier of reasoning performance or merely enhance the efficiency of retrieving pre-existing solutions.
39	
40	## 3 CriticLeanGPT
41	
42	### 3.1 CriticLeanBench
43	
44	#### 3.1.1 Overview of CriticLeanBench
45	
46	CriticLeanBench aims to evaluate the critical reasoning of LLMs in key aspects such as translating natural language mathematical statements into formally verified theorem declarations in Lean 4, including critique and correction. By integrating these core dimensions, CriticLeanBench can comprehensively measure the performance of models in Formalization tasks. In this section, we will elaborate on the construction principles and processes of CriticLeanBench; the construction process is shown in Figure 2.
47	
48	CriticLeanBench is constructed following the following principles: (1) It covers various types of errors, aiming to thoroughly evaluate the comprehensive capabilities of LLMs in capturing the semantic intent of formalized statements, using Template G for systematic assessment; (2) It incorporates diverse data sources to enhance the diversity and representativeness of evaluation data; and (3) It ensures the reliability and validity of the evaluation benchmark through a combination of expert review and automated verification.
49	
50	#### 3.1.2 Automatically verified
51	
52	This section outlines the methodology employed to apply the Automatic Validation Filter, guided by predefined criteria for compiler and model-based verification.
53	
54	**Data Collection** We selected Math Statements from data sources [1, 16, 24, 36, 41, 43, 66], such as Omni-MATH [8], AIME [75], U-MATH [5], DEMI-MathAnalysis [6], HARDMath [7], OlympiadBench [13], and BlueMO [73], along with their corresponding Lean 4 Statements from public dataset [67].
55	
56	**Compiler Verified** We submitted the Lean 4 statements from the above dataset to the Lean 4 compiler. If the compilation succeeded, the results were passed to the DeepSeek R1 [11] model for further processing.
57	
58	- • **Compile false:** For statements that failed to compile, we randomly sampled 50 entries and retained the compiler feedback messages, which were included as part of our CriticLeanBench benchmark.
59	
60	**LLM Verified** For the data that has passed compilation, we utilize a template G to process each sample’s Math Statement and its corresponding Lean 4 Code Statement through the DeepSeek R1 large language model. The model is tasked with determining whether the Lean 4 Code Statement is consistent with the Math Statement, producing for each sample a tag indicating consistency or inconsistency along with a reasoning statement. To extract structured outputs from the model’s responses, we employ regular expression-based pattern matching. The results are then submitted to human reviewers for further validation.**Figure 2** An overview for the CriticLeanBench construction.
61	
62	### 3.1.3 Human Validation Filter
63	
64	This section outlines the methodology employed to apply the Human Validation Filter, guided by predefined criteria (detailed in Appendix C).
65	
66	We categorize the data into two groups based on whether the **Lean-compiled** autoformalization output semantically aligns with the refined statement. Therefore, a Lean-compiled autoformalization falls into the following:
67	
68	- • **Human Check right:** If the autoformalized statement both compiles and accurately captures the mathematical meaning, logic, and intended behavior of the original problem, it satisfies the semantic consistency criteria.
69	- • **Human Check false:** If the autoformalized statement compiles but fails to accurately represent the original mathematical problem’s semantics. It violates one or more of the semantic consistency criteria, despite being syntactically valid Lean code. This often happens when there’s a mismatch between the code’s logic and the intended mathematical meaning.
70	
71	Within the two categories, we select representative samples that mirror the characteristics of the original autoformalization statements while maximizing diversity within each subset and capturing the full spectrum of observed error types in the negative samples. This is achieved by balancing several factors:
72	
73	**Stratified Representation:** The selected samples should maintain a similar distribution across different strata of the original dataset. These strata are defined by:
74	
75	- • **Problem Complexity:** This encompasses factors like the number of variables, quantifiers, logical connectives, and the depth of nested mathematical structures.
76	- • **Mathematical Branches:** The samples should represent the various mathematical domains present in the original data.
77	- • **Statement Well-Formedness:** This refers to the degree to which the original mathematical statementsadhere to standard mathematical notation and conventions. This stratification ensures that the subsets reflect the variability in the quality of the original problem statements.
78	
79	**Comprehensive Error Coverage:** The negative samples are specifically chosen to exemplify the full range of typical errors observed in the autoformalization process. This range includes fundamental semantic and logical issues, such as Premise Translation Errors (e.g., incorrect domains or missing conditions), Mathematical Representation Errors (e.g., faulty expressions or definitions), and Goal Translation Errors. The set also covers issues such as Incorrect Assumptions, logical flaws like Operator & Parenthesis Errors (e.g., misplaced quantifiers), and high-level structural problems like Incomplete Formalization, where crucial context is omitted (detailed in figure 9).
80	
81	### 3.1.4 Data Statistics
82	
83	&lt;table border="1">
84	&lt;thead>
85	&lt;tr>
86	&lt;th>Statistics&lt;/th>
87	&lt;th>Number&lt;/th>
88	&lt;/tr>
89	&lt;/thead>
90	&lt;tbody>
91	&lt;tr>
92	&lt;td>&lt;b>#Problems&lt;/b>&lt;/td>
93	&lt;td>500&lt;/td>
94	&lt;/tr>
95	&lt;tr>
96	&lt;td>&lt;b>Correct Pairs&lt;/b>&lt;/td>
97	&lt;td>250&lt;/td>
98	&lt;/tr>
99	&lt;tr>
100	&lt;td>- &lt;i>human check&lt;/i>&lt;/td>
101	&lt;td>250&lt;/td>
102	&lt;/tr>
103	&lt;tr>
104	&lt;td>&lt;b>Incorrect Pairs&lt;/b>&lt;/td>
105	&lt;td>250&lt;/td>
106	&lt;/tr>
107	&lt;tr>
108	&lt;td>- &lt;i>human/compiler check&lt;/i>&lt;/td>
109	&lt;td>200/50&lt;/td>
110	&lt;/tr>
111	&lt;tr>
112	&lt;td>&lt;b>Question Tokens Length&lt;/b>&lt;/td>
113	&lt;td>&lt;/td>
114	&lt;/tr>
115	&lt;tr>
116	&lt;td>- &lt;i>max/min/avg&lt;/i>&lt;/td>
117	&lt;td>1,583/495/700.94&lt;/td>
118	&lt;/tr>
119	&lt;/tbody>
120	&lt;/table>
121	
122	&lt;table border="1">
123	&lt;thead>
124	&lt;tr>
125	&lt;th>Benchmark&lt;/th>
126	&lt;th>Critic&lt;/th>
127	&lt;th>Lean&lt;/th>
128	&lt;th>Test&lt;/th>
129	&lt;/tr>
130	&lt;/thead>
131	&lt;tbody>
132	&lt;tr>
133	&lt;td>CriticBench&lt;/td>
134	&lt;td>✓&lt;/td>
135	&lt;td>✗&lt;/td>
136	&lt;td>✓&lt;/td>
137	&lt;/tr>
138	&lt;tr>
139	&lt;td>CodeCriticBench&lt;/td>
140	&lt;td>✓&lt;/td>
141	&lt;td>✗&lt;/td>
142	&lt;td>✓&lt;/td>
143	&lt;/tr>
144	&lt;tr>
145	&lt;td>LLaVA-Critic&lt;/td>
146	&lt;td>✓&lt;/td>
147	&lt;td>✗&lt;/td>
148	&lt;td>✗&lt;/td>
149	&lt;/tr>
150	&lt;tr>
151	&lt;td>&lt;b>CriticLeanBench (ours)&lt;/b>&lt;/td>
152	&lt;td>✓&lt;/td>
153	&lt;td>✓&lt;/td>
154	&lt;td>✓&lt;/td>
155	&lt;/tr>
156	&lt;/tbody>
157	&lt;/table>
158	
159	**Table 1** Dataset statistics and comparison of various code benchmark datasets.
160	
161	Table 1 (left) presents the dataset statistics for CriticLeanBench. The dataset contains a total of 500 problems, comprising 250 correct and 250 incorrect Q/GT (Question and GT label) pairs distributed across the collection. The questions exhibit a notable variation in length, with a maximum token count of 1,583 and a minimum of 495 tokens, calculated using the Qwen2.5 [4] tokenizer. On average, each question contains approximately 700.94 tokens. This characteristic distinguishes CriticLeanBench as a complex evaluation benchmark that requires models to process relatively lengthy inputs compared to those in standard datasets.
162	
163	### 3.1.5 Comparison to Other Benchmarks
164	
165	In Table 1 (right), CriticLeanBench has the following features: (1) We focus on a modest data size of 500 samples, acknowledging the expensive manual annotation costs (ranging from tens to hundreds of dollars per instance) and prioritizing efficiency without compromising evaluation rigor; (2) We integrate both Critic and Lean functionalities, distinguishing ourselves from benchmarks like CriticBench [27] and CodeCriticBench [71] that lack Lean capabilities, and LLaVA-Critic [63] that omits both Lean capabilities and test evaluation components; (3) We incorporate a test component focused on translating mathematical statements into formally verified theorem declarations in Lean 4, offering a fine-grained evaluation framework to assess the correctness of model transformations. This aspect of evaluative completeness remains unmatched by existing datasets.
166	
167	## 4 CriticLeanInstruct
168	
169	To enhance the CriticLeanGPT model’s efficacy in critically evaluating the successful transformation of mathematical statements into Lean code, we construct a comprehensive training dataset comprising 48,000 samples. This dataset consists of three high-quality components, designed to comprehensively improve the model’s critical thinking and reasoning capabilities.
170	
171	To significantly broaden the CriticLeanGPT model’s knowledge coverage, we also integrates three times additional code and math [18] datasets, enabling it to more comprehensively understand mathematical concepts and Lean code structures.Specifically, the Seed Data, with a 1:3 mix of math and code, is termed **CriticLeanInstruct(16K)**. When combined with data augmentation while retaining the same ratio, it forms the full **CriticLeanInstruct** dataset.
172	
173	## 4.1 Seed Data
174	
175	The seed data comprises 4,000 samples evenly split into 2,000 correct and 2,000 incorrect instances. For both correct and incorrect samples, human experts provided critical feedback [F](#). Additionally, the incorrect samples include compiler error messages generated by the Lean 4 Compiler as supplementary feedback. Then, we adopt the Gemini2.5-Pro [\[9\]](#) to extend the critical feedback to detailed Chain-of-Thought (CoT) explanations.
176	
177	**Figure 3** Distribution of Different Error Types.
178	
179	To understand the primary failure modes, we analyzed the error distribution across the 2,000 incorrect samples in our seed data as illustrated in Figure 3. The analysis reveals two primary challenges: (1) Syntactic Barriers: The most frequent obstacles are syntactic, such as Type Error and Syntax Errors. These issues typically prevent the code from compiling, indicating a fundamental difficulty in mastering the formal language. (2) Semantic Gaps: Beyond syntax, these errors stem from a failure to interpret the natural language scenario and accurately model its key information. This is evident in high rates of errors when translating a problem’s core logical components—including its premises, goal, and mathematical representation. This semantic challenge is particularly acute in application-style "word problems," where difficulty comprehending complex contexts leads to a fundamentally flawed formalization.
180	
181	Drawing from the error taxonomy (detailed in Appendix D) and building upon our initial annotation standards (detailed in Appendix C), we established a fine-grained checklist, which is provided in full in Appendix E. This checklist formalizes the observed error paradigms, providing the foundational framework for methodically constructing the negative samples used throughout our study.
182	
183	## 4.2 Data Augmentation
184	
185	### 4.2.1 Correct Samples
186	
187	We selected **5560** correct mathematical statements and Lean code pairs from the FormalMATH [\[67\]](#) dataset and used the Gemini-2.5-Pro model to generate Critical Chain-of-Thought for initial assessment. To ensure data quality, we kept these samples where the model’s judgment is “correct.”## 4.2.2 Incorrect Samples
188	
189	We provide two strategies to obtain the incorrect samples as follows:
190	
191	- • Based on OmniMath, we adopt the Kimina-Autoformalizer-7B [54] to generate the Lean 4 code statements, and we kept 2,000 Lean code snippets that failed to compile due to syntactic or logical issues during automated formalization processes. For each detected error, a detailed Chain-of-Thought (CoT) explanation was generated to elucidate the error’s cause, enabling the model to recognize common compilation error patterns and thereby enhance its understanding of Lean 4 code syntax.
192	- • Based on correct mathematical statements and Lean 4 code from the FormalMATH [67] dataset, we implemented a three-step collaborative process to generate negative samples, aiming to enhance the CriticLeanGPT model’s ability to identify subtle errors and logical flaws. First, a checklist of various potential issues, refined by human experts, was established as shown in Appendix E. Second, the Gemini 2.5 Pro model was invoked to randomly select error types from this checklist and modify correct Lean code accordingly, generating incorrect samples (detailed in Appendix H). Then, we adopt the Gemini model to generate the critical Chain-of-Thought explanation.
193	
194	## 4.3 Training Paradigm
195	
196	*Supervised fine-tuning (SFT).* These models are instruction-tuned versions based on their respective pre-trained Qwen2.5 checkpoints, with a focus on improving their ability to interpret and formalize complex mathematical statements expressed in natural language. The CriticLeanInstruct 4 dataset includes Critic data consisting of mathematical statements converted into formally verified theorem declarations in Lean 4, along with three times as much code and mathematics data for SFT (Supervised Fine-Tuning). We used the LLaMA-Factory [77] framework to facilitate the fine-tuning process and optimize model performance.
197	
198	*Reinforcement Learning Optimization (RL).* The recent success of R1-style methods has demonstrated the effectiveness of online RL using discrete, rule-based rewards [45]. In our pipeline, Qwen2.5 series and Qwen3 [52] series are further refined using reinforcement learning signals derived from both format validation of the generated critic data and consistency checking between model predictions and expert-labeled ground truth (GT) labels. Specifically, the RL training data consists of 4,000 Seed Data 4.1, where each example transforms a mathematical statement into a corresponding formal proof in Lean 4. Based on this dataset, we apply a rule-based RL approach to optimize the model’s capability in judgment reasoning. More specifically, we mainly utilize the GRPO [46] algorithm within the VeRL [47] reinforcement learning framework, whose optimization objective is:
199	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f193386-f5dc-4747-8579-10fb58768d35",
  "isSidechain": false,
  "promptId": "4b0c0804-0c80-4fc4-bd2d-54c91b4a93a7",
  "type": "user",
  "uuid": "c48abedb-5d51-4b3f-9b16-95cd51bb7669",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/2a30fe45-086a-4752-b69b-cc68f89516e6/tool-results/toolu_016rqZDKmFkzrH3XvWTnogpJ.txt",
      "content": "# CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization\n\nByteDance Seed      Nanjing University\n\nFull author list in Contributions\n\n## Abstract\n\nTranslating natural language mathematical statements into formal, executable code is a fundamental challenge in automated theorem proving. While prior work has focused on generation and compilation success, little attention has been paid to the *critic phase*—the evaluation of whether generated formalizations truly capture the semantic intent of the original problem. In this paper, we introduce **CriticLean**, a novel critic-guided reinforcement learning framework that elevates the role of the critic from a passive validator to an active learning component. Specifically, first, we propose the **CriticLeanGPT**, trained via supervised fine-tuning and reinforcement learning, to rigorously assess the semantic fidelity of Lean 4 formalizations. Then, we introduce **CriticLeanBench**, a benchmark designed to measure models’ ability to distinguish semantically correct from incorrect formalizations, and demonstrate that our trained CriticLeanGPT models can significantly outperform strong open- and closed-source baselines. Building on the CriticLean framework, we construct **FineLeanCorpus**, a dataset comprising over 285K problems that exhibits rich domain diversity, broad difficulty coverage, and high correctness based on human evaluation. Overall, our findings highlight that optimizing the critic phase is essential for producing reliable formalizations and we hope our CriticLean will provide valuable insights for future advances in formal mathematical reasoning.\n\n**Date:** July 8, 2025\n\n**Correspondence:** [liujiaheng@nju.edu.cn](mailto:liujiaheng@nju.edu.cn), [zhangge.eli@bytedance.com](mailto:zhangge.eli@bytedance.com)\n\n**Project Page:** &lt;https://github.com/multimodal-art-projection/CriticLean>\n\n## 1 Introduction\n\nThe formalization of mathematical statements [64] is a critical task in modern mathematical computation, particularly in the context of theorem provers like Lean 4 [22]. The translation of natural language mathematical problems into formal, executable code remains a significant challenge, as it requires not only syntactical accuracy but also a deep understanding of the problem’s semantics [44, 49]. Existing approaches have shown progress, but they often face limitations in accuracy, especially in the context of complex, high-level problems that involve sophisticated mathematical reasoning [3, 23, 58, 59, 75]. In contrast to existing works, we argue that the *critic* phase—the step where the semantic correctness of generated formalizations is evaluated—is not only underexplored but also fundamentally essential to the success of mathematical autoformalization.\n\nTherefore, in this paper, we systematically investigate and optimize the critic component and introduce **CriticLean**, a comprehensive framework that places the critic model at the center of the formalization pipeline. Unlike prior work that primarily focuses on generation quality or compiler validity, CriticLean introduces the reinforcement learning-based **CriticLeanGPT** models explicitly trained to evaluate whether the Lean 4 output truly reflects the intent of the original mathematical statement., and we present a full methodology forThe diagram illustrates the CriticLean framework for mathematics autoformalization. It starts with a **Natural Language Statement** box containing a mathematical problem about permutations. This statement is processed by an **AutoFormalizer**. The AutoFormalizer's output is then evaluated by two verification steps: a **Verify** box for syntax checking and name resolution, and another **Verify** box for semantic meaning and logical consistency. The **Verify** boxes are supported by a **Lean Compiler** and **CriticLeanGPT** respectively. If a **Compilation Error** or **Critique Error** occurs, the AutoFormalizer receives feedback and iterates. If successful, the final output is a **Lean Formal Language Statement** box showing the formalized theorem.\n\n**Figure 1** Illustration of CriticLean framework based on Critic-Guided Reinforcement Learning for Mathematics Autoformalization.\n\ntraining, and evaluating CriticLeanGPT model. Specifically, as shown in Figure 1, for each natural language statement, we apply the autoformalization iteratively based on the feedback from the Lean compiler and the CriticLeanGPT models, which is trained to critically assess whether a generated formalization accurately represents the semantics of the original mathematical statement. In each iteration, the feedback provides valuable signals that drive an iterative refinement process, further improving the quality of the final Lean code output.\n\nAdditionally, we present **CriticLeanBench**, a benchmark designed to evaluate the performance of CriticLeanGPT models, which contain 500 natural language and Lean 4 language statement pairs (i.e., 250 correct and 250 incorrect pairs). Through extensive experiments, we demonstrate that our trained CriticLeanGPT models outperform the SOTA open-source models [4, 10, 11] and many closed-source API models [9, 12, 42] greatly.\n\nFurthermore, building upon our critic-centric CriticLean pipeline, we propose the high-quality open-source Lean 4 statement dataset **FineLeanCorpus**, comprising 285,957 fully verified entries. When compared to the previous related datasets (e.g., LeanWorkBook [65]), FineLeanCorpus is distinguished by its diversity in mathematical domains, difficulty distribution, and strict semantic validation via critical feedback loops. Notably, its difficulty distribution and targeted domain enrichment create a more structurally balanced training environment, mitigating overfitting and transforming sparse topics into well-supported sub-domains. Furthermore, to foster research into the upper echelons of mathematical reasoning, we have curated the specialized subset called FineLeanCorpus-Diamond, comprising over 36,000 high-difficulty problems.\n\n## 2 Related Works\n\n### 2.1 Autoformalization\n\nAutoformalization [48, 60, 68] refers to the process by which AI systems parse natural language (NL) contents and translate them into machine-verifiable formal representations, such as those in theorem provers like Lean4 [38] or Isabelle [40]. Recent advances leverage large language models (LLMs) [72] to tackle this problem through two primary paradigms: (1) In-context learning [57], where models utilize annotated examples [28, 33, 60] to generate formalizations without explicit fine-tuning, (2) Supervised fine-tuning (e.g., [26, 61, 67]), which adapts general-purpose LLMs into domain-specific autoformalization experts. To assess correctness, prior works [26, 61, 67] employ LLM-as-judge [76] to verify semantic alignment between formal and informal statements. We advance this by training the first open-sourced, domain-specific light LLM on top of Qwen [52] family for critiquing Lean4 statement alignment via reinforcement learning [46], enhancingboth critique capability and formalization robustness.\n\n## 2.2 RL for LLM Reasoning\n\nThe exploration of complex reasoning capabilities in Large Language Models (LLMs) has achieved significant advancements [14, 17, 29–31, 55], with Reinforcement Learning (RL) establishing itself as a critical paradigm for transcending the constraints inherent to Supervised Fine-Tuning (SFT) [29, 32, 56, 66, 70]. Notable methodologies, including GRPO [11, 46], DAPO [66] have demonstrated substantial gains in mathematical reasoning and intricate problem-solving domains. However, the underlying mechanisms by which RL enhances reasoning capabilities remain insufficiently characterized. Empirical analyses increasingly indicate that RL primarily functions to activate, refine, or optimize the sampling of latent reasoning competencies rather than generating entirely novel cognitive frameworks de novo. For example, Yue et al. [69] interrogate whether current reinforcement learning frameworks incorporating verifiable rewards (RLVR) genuinely expand the frontier of reasoning performance or merely enhance the efficiency of retrieving pre-existing solutions.\n\n## 3 CriticLeanGPT\n\n### 3.1 CriticLeanBench\n\n#### 3.1.1 Overview of CriticLeanBench\n\nCriticLeanBench aims to evaluate the critical reasoning of LLMs in key aspects such as translating natural language mathematical statements into formally verified theorem declarations in Lean 4, including critique and correction. By integrating these core dimensions, CriticLeanBench can comprehensively measure the performance of models in Formalization tasks. In this section, we will elaborate on the construction principles and processes of CriticLeanBench; the construction process is shown in Figure 2.\n\nCriticLeanBench is constructed following the following principles: (1) It covers various types of errors, aiming to thoroughly evaluate the comprehensive capabilities of LLMs in capturing the semantic intent of formalized statements, using Template G for systematic assessment; (2) It incorporates diverse data sources to enhance the diversity and representativeness of evaluation data; and (3) It ensures the reliability and validity of the evaluation benchmark through a combination of expert review and automated verification.\n\n#### 3.1.2 Automatically verified\n\nThis section outlines the methodology employed to apply the Automatic Validation Filter, guided by predefined criteria for compiler and model-based verification.\n\n**Data Collection** We selected Math Statements from data sources [1, 16, 24, 36, 41, 43, 66], such as Omni-MATH [8], AIME [75], U-MATH [5], DEMI-MathAnalysis [6], HARDMath [7], OlympiadBench [13], and BlueMO [73], along with their corresponding Lean 4 Statements from public dataset [67].\n\n**Compiler Verified** We submitted the Lean 4 statements from the above dataset to the Lean 4 compiler. If the compilation succeeded, the results were passed to the DeepSeek R1 [11] model for further processing.\n\n- • **Compile false:** For statements that failed to compile, we randomly sampled 50 entries and retained the compiler feedback messages, which were included as part of our CriticLeanBench benchmark.\n\n**LLM Verified** For the data that has passed compilation, we utilize a template G to process each sample’s Math Statement and its corresponding Lean 4 Code Statement through the DeepSeek R1 large language model. The model is tasked with determining whether the Lean 4 Code Statement is consistent with the Math Statement, producing for each sample a tag indicating consistency or inconsistency along with a reasoning statement. To extract structured outputs from the model’s responses, we employ regular expression-based pattern matching. The results are then submitted to human reviewers for further validation.**Figure 2** An overview for the CriticLeanBench construction.\n\n### 3.1.3 Human Validation Filter\n\nThis section outlines the methodology employed to apply the Human Validation Filter, guided by predefined criteria (detailed in Appendix C).\n\nWe categorize the data into two groups based on whether the **Lean-compiled** autoformalization output semantically aligns with the refined statement. Therefore, a Lean-compiled autoformalization falls into the following:\n\n- • **Human Check right:** If the autoformalized statement both compiles and accurately captures the mathematical meaning, logic, and intended behavior of the original problem, it satisfies the semantic consistency criteria.\n- • **Human Check false:** If the autoformalized statement compiles but fails to accurately represent the original mathematical problem’s semantics. It violates one or more of the semantic consistency criteria, despite being syntactically valid Lean code. This often happens when there’s a mismatch between the code’s logic and the intended mathematical meaning.\n\nWithin the two categories, we select representative samples that mirror the characteristics of the original autoformalization statements while maximizing diversity within each subset and capturing the full spectrum of observed error types in the negative samples. This is achieved by balancing several factors:\n\n**Stratified Representation:** The selected samples should maintain a similar distribution across different strata of the original dataset. These strata are defined by:\n\n- • **Problem Complexity:** This encompasses factors like the number of variables, quantifiers, logical connectives, and the depth of nested mathematical structures.\n- • **Mathematical Branches:** The samples should represent the various mathematical domains present in the original data.\n- • **Statement Well-Formedness:** This refers to the degree to which the original mathematical statementsadhere to standard mathematical notation and conventions. This stratification ensures that the subsets reflect the variability in the quality of the original problem statements.\n\n**Comprehensive Error Coverage:** The negative samples are specifically chosen to exemplify the full range of typical errors observed in the autoformalization process. This range includes fundamental semantic and logical issues, such as Premise Translation Errors (e.g., incorrect domains or missing conditions), Mathematical Representation Errors (e.g., faulty expressions or definitions), and Goal Translation Errors. The set also covers issues such as Incorrect Assumptions, logical flaws like Operator & Parenthesis Errors (e.g., misplaced quantifiers), and high-level structural problems like Incomplete Formalization, where crucial context is omitted (detailed in figure 9).\n\n### 3.1.4 Data Statistics\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Statistics&lt;/th>\n&lt;th>Number&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>&lt;b>#Problems&lt;/b>&lt;/td>\n&lt;td>500&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Correct Pairs&lt;/b>&lt;/td>\n&lt;td>250&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>- &lt;i>human check&lt;/i>&lt;/td>\n&lt;td>250&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Incorrect Pairs&lt;/b>&lt;/td>\n&lt;td>250&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>- &lt;i>human/compiler check&lt;/i>&lt;/td>\n&lt;td>200/50&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Question Tokens Length&lt;/b>&lt;/td>\n&lt;td>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>- &lt;i>max/min/avg&lt;/i>&lt;/td>\n&lt;td>1,583/495/700.94&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Benchmark&lt;/th>\n&lt;th>Critic&lt;/th>\n&lt;th>Lean&lt;/th>\n&lt;th>Test&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>CriticBench&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>CodeCriticBench&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>LLaVA-Critic&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>CriticLeanBench (ours)&lt;/b>&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 1** Dataset statistics and comparison of various code benchmark datasets.\n\nTable 1 (left) presents the dataset statistics for CriticLeanBench. The dataset contains a total of 500 problems, comprising 250 correct and 250 incorrect Q/GT (Question and GT label) pairs distributed across the collection. The questions exhibit a notable variation in length, with a maximum token count of 1,583 and a minimum of 495 tokens, calculated using the Qwen2.5 [4] tokenizer. On average, each question contains approximately 700.94 tokens. This characteristic distinguishes CriticLeanBench as a complex evaluation benchmark that requires models to process relatively lengthy inputs compared to those in standard datasets.\n\n### 3.1.5 Comparison to Other Benchmarks\n\nIn Table 1 (right), CriticLeanBench has the following features: (1) We focus on a modest data size of 500 samples, acknowledging the expensive manual annotation costs (ranging from tens to hundreds of dollars per instance) and prioritizing efficiency without compromising evaluation rigor; (2) We integrate both Critic and Lean functionalities, distinguishing ourselves from benchmarks like CriticBench [27] and CodeCriticBench [71] that lack Lean capabilities, and LLaVA-Critic [63] that omits both Lean capabilities and test evaluation components; (3) We incorporate a test component focused on translating mathematical statements into formally verified theorem declarations in Lean 4, offering a fine-grained evaluation framework to assess the correctness of model transformations. This aspect of evaluative completeness remains unmatched by existing datasets.\n\n## 4 CriticLeanInstruct\n\nTo enhance the CriticLeanGPT model’s efficacy in critically evaluating the successful transformation of mathematical statements into Lean code, we construct a comprehensive training dataset comprising 48,000 samples. This dataset consists of three high-quality components, designed to comprehensively improve the model’s critical thinking and reasoning capabilities.\n\nTo significantly broaden the CriticLeanGPT model’s knowledge coverage, we also integrates three times additional code and math [18] datasets, enabling it to more comprehensively understand mathematical concepts and Lean code structures.Specifically, the Seed Data, with a 1:3 mix of math and code, is termed **CriticLeanInstruct(16K)**. When combined with data augmentation while retaining the same ratio, it forms the full **CriticLeanInstruct** dataset.\n\n## 4.1 Seed Data\n\nThe seed data comprises 4,000 samples evenly split into 2,000 correct and 2,000 incorrect instances. For both correct and incorrect samples, human experts provided critical feedback [F](#). Additionally, the incorrect samples include compiler error messages generated by the Lean 4 Compiler as supplementary feedback. Then, we adopt the Gemini2.5-Pro [\\[9\\]](#) to extend the critical feedback to detailed Chain-of-Thought (CoT) explanations.\n\n**Figure 3** Distribution of Different Error Types.\n\nTo understand the primary failure modes, we analyzed the error distribution across the 2,000 incorrect samples in our seed data as illustrated in Figure 3. The analysis reveals two primary challenges: (1) Syntactic Barriers: The most frequent obstacles are syntactic, such as Type Error and Syntax Errors. These issues typically prevent the code from compiling, indicating a fundamental difficulty in mastering the formal language. (2) Semantic Gaps: Beyond syntax, these errors stem from a failure to interpret the natural language scenario and accurately model its key information. This is evident in high rates of errors when translating a problem’s core logical components—including its premises, goal, and mathematical representation. This semantic challenge is particularly acute in application-style \"word problems,\" where difficulty comprehending complex contexts leads to a fundamentally flawed formalization.\n\nDrawing from the error taxonomy (detailed in Appendix D) and building upon our initial annotation standards (detailed in Appendix C), we established a fine-grained checklist, which is provided in full in Appendix E. This checklist formalizes the observed error paradigms, providing the foundational framework for methodically constructing the negative samples used throughout our study.\n\n## 4.2 Data Augmentation\n\n### 4.2.1 Correct Samples\n\nWe selected **5560** correct mathematical statements and Lean code pairs from the FormalMATH [\\[67\\]](#) dataset and used the Gemini-2.5-Pro model to generate Critical Chain-of-Thought for initial assessment. To ensure data quality, we kept these samples where the model’s judgment is “correct.”## 4.2.2 Incorrect Samples\n\nWe provide two strategies to obtain the incorrect samples as follows:\n\n- • Based on OmniMath, we adopt the Kimina-Autoformalizer-7B [54] to generate the Lean 4 code statements, and we kept 2,000 Lean code snippets that failed to compile due to syntactic or logical issues during automated formalization processes. For each detected error, a detailed Chain-of-Thought (CoT) explanation was generated to elucidate the error’s cause, enabling the model to recognize common compilation error patterns and thereby enhance its understanding of Lean 4 code syntax.\n- • Based on correct mathematical statements and Lean 4 code from the FormalMATH [67] dataset, we implemented a three-step collaborative process to generate negative samples, aiming to enhance the CriticLeanGPT model’s ability to identify subtle errors and logical flaws. First, a checklist of various potential issues, refined by human experts, was established as shown in Appendix E. Second, the Gemini 2.5 Pro model was invoked to randomly select error types from this checklist and modify correct Lean code accordingly, generating incorrect samples (detailed in Appendix H). Then, we adopt the Gemini model to generate the critical Chain-of-Thought explanation.\n\n## 4.3 Training Paradigm\n\n*Supervised fine-tuning (SFT).* These models are instruction-tuned versions based on their respective pre-trained Qwen2.5 checkpoints, with a focus on improving their ability to interpret and formalize complex mathematical statements expressed in natural language. The CriticLeanInstruct 4 dataset includes Critic data consisting of mathematical statements converted into formally verified theorem declarations in Lean 4, along with three times as much code and mathematics data for SFT (Supervised Fine-Tuning). We used the LLaMA-Factory [77] framework to facilitate the fine-tuning process and optimize model performance.\n\n*Reinforcement Learning Optimization (RL).* The recent success of R1-style methods has demonstrated the effectiveness of online RL using discrete, rule-based rewards [45]. In our pipeline, Qwen2.5 series and Qwen3 [52] series are further refined using reinforcement learning signals derived from both format validation of the generated critic data and consistency checking between model predictions and expert-labeled ground truth (GT) labels. Specifically, the RL training data consists of 4,000 Seed Data 4.1, where each example transforms a mathematical statement into a corresponding formal proof in Lean 4. Based on this dataset, we apply a rule-based RL approach to optimize the model’s capability in judgment reasoning. More specifically, we mainly utilize the GRPO [46] algorithm within the VeRL [47] reinforcement learning framework, whose optimization objective is:\n",
      "numLines": 200,
      "startLine": 0,
      "totalLines": 1768
    }
  },
  "sourceToolAssistantUUID": "6f193386-f5dc-4747-8579-10fb58768d35",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 66_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Aut…",
  "leafUuid": "c48abedb-5d51-4b3f-9b16-95cd51bb7669",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6"
}
```

---

### Runtime record

_source line 67_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise autoformalization TTRL paper with verified data and concrete curriculum",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6"
}
```

---

### Assistant

_source line 68 · 2026-05-27T18:17:48.334Z_

<details><summary>Logged reasoning block</summary>

```text
Let me continue reading the paper to find the results table with specific accuracy numbers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c48abedb-5d51-4b3f-9b16-95cd51bb7669",
  "isSidechain": false,
  "requestId": "req_011CbTXs5N9wCJXbL7zP8V9m",
  "type": "assistant",
  "uuid": "191fa49a-5bbc-4d9d-a3e7-82d93606de16",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FFmVbsfJ9AFJPAueWusmUo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6087,
      "cache_read_input_tokens": 31692,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6087,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 31692,
          "cache_creation_input_tokens": 6087,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6087
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

_source line 69 · 2026-05-27T18:17:51.724Z_

<details open><summary>🔧 Tool call — Read · `toolu_018qEcfYmZuW7MUqCxBw4MDH`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/2a30fe45-086a-4752-b69b-cc68f89516e6/tool-results/toolu_016rqZDKmFkzrH3XvWTnogpJ.txt",
  "limit": 300,
  "offset": 199
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "191fa49a-5bbc-4d9d-a3e7-82d93606de16",
  "isSidechain": false,
  "requestId": "req_011CbTXs5N9wCJXbL7zP8V9m",
  "type": "assistant",
  "uuid": "7759c2ec-e23f-435c-8333-7475d73266eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FFmVbsfJ9AFJPAueWusmUo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6087,
      "cache_read_input_tokens": 31692,
      "output_tokens": 192,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6087,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 192,
          "cache_read_input_tokens": 31692,
          "cache_creation_input_tokens": 6087,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6087
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

_source line 70 · 2026-05-27T18:17:51.737Z_

<details><summary>↩ Tool result · `toolu_018qEcfYmZuW7MUqCxBw4MDH`</summary>

```text
199	*Reinforcement Learning Optimization (RL).* The recent success of R1-style methods has demonstrated the effectiveness of online RL using discrete, rule-based rewards [45]. In our pipeline, Qwen2.5 series and Qwen3 [52] series are further refined using reinforcement learning signals derived from both format validation of the generated critic data and consistency checking between model predictions and expert-labeled ground truth (GT) labels. Specifically, the RL training data consists of 4,000 Seed Data 4.1, where each example transforms a mathematical statement into a corresponding formal proof in Lean 4. Based on this dataset, we apply a rule-based RL approach to optimize the model’s capability in judgment reasoning. More specifically, we mainly utilize the GRPO [46] algorithm within the VeRL [47] reinforcement learning framework, whose optimization objective is:
200	
201	$$J_{\text{online}}(\pi_{\theta}; \mathcal{D}) = \mathbb{E}_{x \sim \mathcal{D}, \{y_i\}_{i=1}^G \sim \pi_{\theta_{\text{old}}}(y|x)} \left[ \frac{1}{G} \sum_{i=1}^G \min \left( \frac{\pi_{\theta}(y_i|x)}{\pi_{\theta_{\text{old}}}(y_i|x)} A_i, \text{clip} \left( \frac{\pi_{\theta}(y_i|x)}{\pi_{\theta_{\text{old}}}(y_i|x)}, 1 - \epsilon, 1 + \epsilon \right) A_i \right) - \beta D_{\text{KL}}(\pi_{\theta} || \pi_{\text{ref}}) \right] \quad (1)$$
202	
203	where  $G$  is group size, and  $A_i$  is advantage. The reward function is designed as follows&lt;sup>1&lt;/sup>:
204	
205	$$r_{\text{accuracy}} = \begin{cases} 1, & \text{if judgement} = \text{label} \\ 0, & \text{if judgement} \neq \text{label} \end{cases} \quad (2)$$
206	
207	$$r_{\text{format}} = \begin{cases} 1, & \text{if format is right} \\ 0, & \text{if format is wrong} \end{cases} \quad (3)$$
208	
209	$$r_{\text{final}} = \min(r_{\text{accuracy}}, r_{\text{format}}) \quad (4)$$
210	
211	
212	---
213	
214	&lt;sup>1&lt;/sup>We do not include a length penalty in rewards to encourage longer thinking.## 5 Experiments
215	
216	### 5.1 Experimental Setup
217	
218	**Baseline Models.** For the closed-sourced API models, we select the following models: Claude35\_Sonnet2 [2], Doubao-1.5-pro-32k [12], Gemini 2.5 Pro [50], GPT-4o-2024-11-20 [42]. We select a group of the most advanced open-source LLMs to serve as critic models for evaluation, which includes various reasoning models (DeepSeek-R1 [11], QwQ-32B [53], Qwen3-8B [52], Qwen3-14B [52], Qwen3-32B [52]), DeepSeek-Prover models [62] (DeepSeek-Prover-V1.5-RL, DeepSeek-Prover-V1.5-SFT), Llama-3.3-70B-Instruct [10] and several Qwen models (Qwen2.5-Coder-7B-Instruct [19], Qwen2.5-Coder-32B-Instruct [19], Qwen2.5-7B-Instruct [51], Qwen2.5-14B-Instruct [51] and Qwen2.5-32B-Instruct [51]).
219	
220	**CriticLeanGPT Models.** We further evaluate three variants from the Qwen2.5 series and Qwen3 series. These are instruction-based models fine-tuned specifically on either the CriticLeanInstruct 4 dataset or the RL-based clean critic Seed Data 4.1. All open-source models are inferred using the vLLM [21] framework with default inference parameters.
221	
222	### 5.2 Main Results
223	
224	#### 5.2.1 Evaluation of Critic Capability
225	
226	As indicated in Table 2, the experimental results clearly demonstrate the effectiveness of the CriticLeanGPT models trained on our CriticLeanInstruct, in converting natural language mathematical statements into Lean 4 formal theorem declarations. Within the CriticLeanBench benchmark, our CriticLeanGPT models trained via supervised fine-tuning (SFT) and reinforcement learning (RL), along with their enhanced variants—outperform a range of closed-source API models, open-source models, and baseline models, highlighting distinct advantages. These outcomes yield several key insights: (1) Reasoning models excel in critical tasks, with Gemini 2.5 Pro, QwQ-32B, Qwen3-32B, and DeepSeek-R1 all attaining scores above 80. When compared to baseline models, our Qwen3-32B-RL model, optimized through RL, achieves a strong accuracy level, underscoring the efficacy of both our training methodology and dataset. (3) Our innovative mixed SFT strategy substantially boosts the performance of the Qwen2.5 family, with notable improvements observed across the 7B, 14B, and 32B models. (4) Additionally, SFT and RL significantly strengthen the models’ capacity to identify erroneous samples, as evidenced by higher true negative rates (TNR) and lower false negative rates (FNR)—a critical enhancement for accurate detection of incorrect formalizations, which is indispensable for effective critical tasks.
227	
228	### 5.3 Ablation Study
229	
230	#### 5.3.1 Effect of Reasoning Data
231	
232	We conduct an ablation study on CriticLeanBench to evaluate the impact of different training strategies. As shown in Table 3, incorporating code and math reasoning data significantly improves performance across all model sizes compared to using Seed Data 4.1. Specifically, using the CriticLeanInstruct 4, which samples Critic and non-Critic data at a ratio of 1:3, leads to substantial gains, demonstrating that integrating diverse reasoning tasks enhances the critical reasoning capabilities of the model. This suggests that multi-task learning with math and code data improves the critique abilities of mathematical formalization.
233	
234	#### 5.3.2 Effect of SFT Dataset Size
235	
236	Figure 6 highlights a notable parameter-dependent relationship between the size of the SFT dataset and key reasoning performance. Across all model scales, performance improvements are observed through SFT, albeit with varying degrees of fluctuation depending on the training set size. Smaller models (e.g., 7B) exhibit more pronounced gains as the dataset expands, whereas larger models (e.g., 32B) demonstrate a less consistent trend, with marginal improvements at lower data volumes but substantial gains at higher data volumes. These findings align with prior studies [39, 78], underscoring the interplay between model capacity, data scale, and performance optimization in SFT scenarios. The results emphasize the need for tailored strategies to balance data efficiency and model generalization, particularly for large-scale architectures.&lt;table border="1">
237	&lt;thead>
238	&lt;tr>
239	&lt;th>Model&lt;/th>
240	&lt;th>ACC&lt;/th>
241	&lt;th>TPR&lt;/th>
242	&lt;th>FPR&lt;/th>
243	&lt;th>TNR&lt;/th>
244	&lt;th>FNR&lt;/th>
245	&lt;th>Reasoning&lt;/th>
246	&lt;th>Open-source&lt;/th>
247	&lt;/tr>
248	&lt;/thead>
249	&lt;tbody>
250	&lt;tr>
251	&lt;td colspan="8" style="text-align: center;">&lt;b>SOTA LLMs&lt;/b>&lt;/td>
252	&lt;/tr>
253	&lt;tr>
254	&lt;td>Gemini-2.5-Pro&lt;/td>
255	&lt;td>&lt;u>89.2&lt;/u>&lt;/td>
256	&lt;td>&lt;u>95.6&lt;/u>&lt;/td>
257	&lt;td>&lt;u>4.4&lt;/u>&lt;/td>
258	&lt;td>&lt;u>82.8&lt;/u>&lt;/td>
259	&lt;td>&lt;u>17.2&lt;/u>&lt;/td>
260	&lt;td>✓&lt;/td>
261	&lt;td>✗&lt;/td>
262	&lt;/tr>
263	&lt;tr>
264	&lt;td>QwQ-32B&lt;/td>
265	&lt;td>&lt;u>86.4&lt;/u>&lt;/td>
266	&lt;td>93.6&lt;/td>
267	&lt;td>6.4&lt;/td>
268	&lt;td>79.2&lt;/td>
269	&lt;td>20.8&lt;/td>
270	&lt;td>✓&lt;/td>
271	&lt;td>✓&lt;/td>
272	&lt;/tr>
273	&lt;tr>
274	&lt;td>Qwen3-32B&lt;/td>
275	&lt;td>85.6&lt;/td>
276	&lt;td>&lt;b>96.0&lt;/b>&lt;/td>
277	&lt;td>&lt;b>4.0&lt;/b>&lt;/td>
278	&lt;td>75.2&lt;/td>
279	&lt;td>24.8&lt;/td>
280	&lt;td>✓&lt;/td>
281	&lt;td>✓&lt;/td>
282	&lt;/tr>
283	&lt;tr>
284	&lt;td>Qwen3-235B-A22B&lt;/td>
285	&lt;td>84.8&lt;/td>
286	&lt;td>90.4&lt;/td>
287	&lt;td>9.6&lt;/td>
288	&lt;td>79.2&lt;/td>
289	&lt;td>20.8&lt;/td>
290	&lt;td>✓&lt;/td>
291	&lt;td>✓&lt;/td>
292	&lt;/tr>
293	&lt;tr>
294	&lt;td>DeepSeek-R1&lt;/td>
295	&lt;td>84.0&lt;/td>
296	&lt;td>90.8&lt;/td>
297	&lt;td>9.2&lt;/td>
298	&lt;td>77.2&lt;/td>
299	&lt;td>22.8&lt;/td>
300	&lt;td>✓&lt;/td>
301	&lt;td>✓&lt;/td>
302	&lt;/tr>
303	&lt;tr>
304	&lt;td>Qwen3-14B&lt;/td>
305	&lt;td>83.6&lt;/td>
306	&lt;td>92.4&lt;/td>
307	&lt;td>7.6&lt;/td>
308	&lt;td>74.8&lt;/td>
309	&lt;td>25.2&lt;/td>
310	&lt;td>✓&lt;/td>
311	&lt;td>✓&lt;/td>
312	&lt;/tr>
313	&lt;tr>
314	&lt;td>Qwen3-8B&lt;/td>
315	&lt;td>79.8&lt;/td>
316	&lt;td>94.4&lt;/td>
317	&lt;td>5.6&lt;/td>
318	&lt;td>65.2&lt;/td>
319	&lt;td>34.8&lt;/td>
320	&lt;td>✓&lt;/td>
321	&lt;td>✓&lt;/td>
322	&lt;/tr>
323	&lt;tr>
324	&lt;td>Doubao-1.5-pro-32k&lt;/td>
325	&lt;td>78.4&lt;/td>
326	&lt;td>95.2&lt;/td>
327	&lt;td>4.8&lt;/td>
328	&lt;td>61.6&lt;/td>
329	&lt;td>38.4&lt;/td>
330	&lt;td>✗&lt;/td>
331	&lt;td>✗&lt;/td>
332	&lt;/tr>
333	&lt;tr>
334	&lt;td>Claude35-Sonnet&lt;/td>
335	&lt;td>74.2&lt;/td>
336	&lt;td>&lt;u>97.2&lt;/u>&lt;/td>
337	&lt;td>&lt;u>2.8&lt;/u>&lt;/td>
338	&lt;td>51.2&lt;/td>
339	&lt;td>48.8&lt;/td>
340	&lt;td>✗&lt;/td>
341	&lt;td>✗&lt;/td>
342	&lt;/tr>
343	&lt;tr>
344	&lt;td>Qwen2.5-32B-Instruct&lt;/td>
345	&lt;td>73.0&lt;/td>
346	&lt;td>91.6&lt;/td>
347	&lt;td>8.4&lt;/td>
348	&lt;td>54.4&lt;/td>
349	&lt;td>45.6&lt;/td>
350	&lt;td>✗&lt;/td>
351	&lt;td>✓&lt;/td>
352	&lt;/tr>
353	&lt;tr>
354	&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>
355	&lt;td>71.6&lt;/td>
356	&lt;td>91.6&lt;/td>
357	&lt;td>8.4&lt;/td>
358	&lt;td>51.6&lt;/td>
359	&lt;td>48.4&lt;/td>
360	&lt;td>✗&lt;/td>
361	&lt;td>✓&lt;/td>
362	&lt;/tr>
363	&lt;tr>
364	&lt;td>Llama-3.3-70B-Instruct&lt;/td>
365	&lt;td>68.2&lt;/td>
366	&lt;td>95.2&lt;/td>
367	&lt;td>4.8&lt;/td>
368	&lt;td>41.2&lt;/td>
369	&lt;td>58.8&lt;/td>
370	&lt;td>✗&lt;/td>
371	&lt;td>✓&lt;/td>
372	&lt;/tr>
373	&lt;tr>
374	&lt;td>GPT-4o-2024-11-20&lt;/td>
375	&lt;td>67.8&lt;/td>
376	&lt;td>95.6&lt;/td>
377	&lt;td>4.4&lt;/td>
378	&lt;td>40.0&lt;/td>
379	&lt;td>60.0&lt;/td>
380	&lt;td>✗&lt;/td>
381	&lt;td>✗&lt;/td>
382	&lt;/tr>
383	&lt;tr>
384	&lt;td>Qwen2.5-14B-Instruct&lt;/td>
385	&lt;td>66.6&lt;/td>
386	&lt;td>80.4&lt;/td>
387	&lt;td>19.6&lt;/td>
388	&lt;td>52.8&lt;/td>
389	&lt;td>47.2&lt;/td>
390	&lt;td>✗&lt;/td>
391	&lt;td>✓&lt;/td>
392	&lt;/tr>
393	&lt;tr>
394	&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>
395	&lt;td>65.4&lt;/td>
396	&lt;td>88.4&lt;/td>
397	&lt;td>11.6&lt;/td>
398	&lt;td>42.4&lt;/td>
399	&lt;td>57.6&lt;/td>
400	&lt;td>✗&lt;/td>
401	&lt;td>✓&lt;/td>
402	&lt;/tr>
403	&lt;tr>
404	&lt;td>Qwen2.5-7B-Instruct&lt;/td>
405	&lt;td>60.8&lt;/td>
406	&lt;td>89.6&lt;/td>
407	&lt;td>10.4&lt;/td>
408	&lt;td>32.0&lt;/td>
409	&lt;td>68.0&lt;/td>
410	&lt;td>✗&lt;/td>
411	&lt;td>✓&lt;/td>
412	&lt;/tr>
413	&lt;tr>
414	&lt;td>DeepSeek-Prover-V1.5-SFT&lt;/td>
415	&lt;td>52.4&lt;/td>
416	&lt;td>78.8&lt;/td>
417	&lt;td>21.2&lt;/td>
418	&lt;td>26.0&lt;/td>
419	&lt;td>74.0&lt;/td>
420	&lt;td>✗&lt;/td>
421	&lt;td>✓&lt;/td>
422	&lt;/tr>
423	&lt;tr>
424	&lt;td>DeepSeek-Prover-V1.5-RL&lt;/td>
425	&lt;td>50.0&lt;/td>
426	&lt;td>76.4&lt;/td>
427	&lt;td>23.6&lt;/td>
428	&lt;td>23.6&lt;/td>
429	&lt;td>76.4&lt;/td>
430	&lt;td>✗&lt;/td>
431	&lt;td>✓&lt;/td>
432	&lt;/tr>
433	&lt;tr>
434	&lt;td colspan="8" style="text-align: center;">&lt;b>CriticLeanGPT (Ours)&lt;/b>&lt;/td>
435	&lt;/tr>
436	&lt;tr>
437	&lt;td>Qwen3-8B-RL&lt;/td>
438	&lt;td>79.8&lt;/td>
439	&lt;td>90.0&lt;/td>
440	&lt;td>10.0&lt;/td>
441	&lt;td>72.0&lt;/td>
442	&lt;td>28.0&lt;/td>
443	&lt;td>✓&lt;/td>
444	&lt;td>✓&lt;/td>
445	&lt;/tr>
446	&lt;tr>
447	&lt;td>Qwen3-14B-RL&lt;/td>
448	&lt;td>84.8&lt;/td>
449	&lt;td>91.6&lt;/td>
450	&lt;td>8.4&lt;/td>
451	&lt;td>78.0&lt;/td>
452	&lt;td>22.0&lt;/td>
453	&lt;td>✓&lt;/td>
454	&lt;td>✓&lt;/td>
455	&lt;/tr>
456	&lt;tr>
457	&lt;td>Qwen3-32B-RL&lt;/td>
458	&lt;td>&lt;b>87.0&lt;/b>&lt;/td>
459	&lt;td>88.4&lt;/td>
460	&lt;td>11.6&lt;/td>
461	&lt;td>&lt;u>85.6&lt;/u>&lt;/td>
462	&lt;td>&lt;u>14.4&lt;/u>&lt;/td>
463	&lt;td>✓&lt;/td>
464	&lt;td>✓&lt;/td>
465	&lt;/tr>
466	&lt;tr>
467	&lt;td>Qwen2.5-7B-Instruct-RL&lt;/td>
468	&lt;td>68.6&lt;/td>
469	&lt;td>85.6&lt;/td>
470	&lt;td>14.4&lt;/td>
471	&lt;td>51.6&lt;/td>
472	&lt;td>48.4&lt;/td>
473	&lt;td>✗&lt;/td>
474	&lt;td>✓&lt;/td>
475	&lt;/tr>
476	&lt;tr>
477	&lt;td>Qwen2.5-14B-Instruct-RL&lt;/td>
478	&lt;td>69.4&lt;/td>
479	&lt;td>85.2&lt;/td>
480	&lt;td>14.8&lt;/td>
481	&lt;td>53.6&lt;/td>
482	&lt;td>46.4&lt;/td>
483	&lt;td>✗&lt;/td>
484	&lt;td>✓&lt;/td>
485	&lt;/tr>
486	&lt;tr>
487	&lt;td>Qwen2.5-32B-Instruct-RL&lt;/td>
488	&lt;td>72.0&lt;/td>
489	&lt;td>60.4&lt;/td>
490	&lt;td>39.6&lt;/td>
491	&lt;td>&lt;b>83.6&lt;/b>&lt;/td>
492	&lt;td>&lt;b>16.4&lt;/b>&lt;/td>
493	&lt;td>✗&lt;/td>
494	&lt;td>✓&lt;/td>
495	&lt;/tr>
496	&lt;tr>
497	&lt;td>Qwen2.5-7B-Instruct-SFT&lt;/td>
498	&lt;td>69.8&lt;/td>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7759c2ec-e23f-435c-8333-7475d73266eb",
  "isSidechain": false,
  "promptId": "4b0c0804-0c80-4fc4-bd2d-54c91b4a93a7",
  "type": "user",
  "uuid": "5620acf7-69b7-45f1-97d6-2567e52382b9",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/2a30fe45-086a-4752-b69b-cc68f89516e6/tool-results/toolu_016rqZDKmFkzrH3XvWTnogpJ.txt",
      "content": "*Reinforcement Learning Optimization (RL).* The recent success of R1-style methods has demonstrated the effectiveness of online RL using discrete, rule-based rewards [45]. In our pipeline, Qwen2.5 series and Qwen3 [52] series are further refined using reinforcement learning signals derived from both format validation of the generated critic data and consistency checking between model predictions and expert-labeled ground truth (GT) labels. Specifically, the RL training data consists of 4,000 Seed Data 4.1, where each example transforms a mathematical statement into a corresponding formal proof in Lean 4. Based on this dataset, we apply a rule-based RL approach to optimize the model’s capability in judgment reasoning. More specifically, we mainly utilize the GRPO [46] algorithm within the VeRL [47] reinforcement learning framework, whose optimization objective is:\n\n$$J_{\\text{online}}(\\pi_{\\theta}; \\mathcal{D}) = \\mathbb{E}_{x \\sim \\mathcal{D}, \\{y_i\\}_{i=1}^G \\sim \\pi_{\\theta_{\\text{old}}}(y|x)} \\left[ \\frac{1}{G} \\sum_{i=1}^G \\min \\left( \\frac{\\pi_{\\theta}(y_i|x)}{\\pi_{\\theta_{\\text{old}}}(y_i|x)} A_i, \\text{clip} \\left( \\frac{\\pi_{\\theta}(y_i|x)}{\\pi_{\\theta_{\\text{old}}}(y_i|x)}, 1 - \\epsilon, 1 + \\epsilon \\right) A_i \\right) - \\beta D_{\\text{KL}}(\\pi_{\\theta} || \\pi_{\\text{ref}}) \\right] \\quad (1)$$\n\nwhere  $G$  is group size, and  $A_i$  is advantage. The reward function is designed as follows&lt;sup>1&lt;/sup>:\n\n$$r_{\\text{accuracy}} = \\begin{cases} 1, & \\text{if judgement} = \\text{label} \\\\ 0, & \\text{if judgement} \\neq \\text{label} \\end{cases} \\quad (2)$$\n\n$$r_{\\text{format}} = \\begin{cases} 1, & \\text{if format is right} \\\\ 0, & \\text{if format is wrong} \\end{cases} \\quad (3)$$\n\n$$r_{\\text{final}} = \\min(r_{\\text{accuracy}}, r_{\\text{format}}) \\quad (4)$$\n\n\n---\n\n&lt;sup>1&lt;/sup>We do not include a length penalty in rewards to encourage longer thinking.## 5 Experiments\n\n### 5.1 Experimental Setup\n\n**Baseline Models.** For the closed-sourced API models, we select the following models: Claude35\\_Sonnet2 [2], Doubao-1.5-pro-32k [12], Gemini 2.5 Pro [50], GPT-4o-2024-11-20 [42]. We select a group of the most advanced open-source LLMs to serve as critic models for evaluation, which includes various reasoning models (DeepSeek-R1 [11], QwQ-32B [53], Qwen3-8B [52], Qwen3-14B [52], Qwen3-32B [52]), DeepSeek-Prover models [62] (DeepSeek-Prover-V1.5-RL, DeepSeek-Prover-V1.5-SFT), Llama-3.3-70B-Instruct [10] and several Qwen models (Qwen2.5-Coder-7B-Instruct [19], Qwen2.5-Coder-32B-Instruct [19], Qwen2.5-7B-Instruct [51], Qwen2.5-14B-Instruct [51] and Qwen2.5-32B-Instruct [51]).\n\n**CriticLeanGPT Models.** We further evaluate three variants from the Qwen2.5 series and Qwen3 series. These are instruction-based models fine-tuned specifically on either the CriticLeanInstruct 4 dataset or the RL-based clean critic Seed Data 4.1. All open-source models are inferred using the vLLM [21] framework with default inference parameters.\n\n### 5.2 Main Results\n\n#### 5.2.1 Evaluation of Critic Capability\n\nAs indicated in Table 2, the experimental results clearly demonstrate the effectiveness of the CriticLeanGPT models trained on our CriticLeanInstruct, in converting natural language mathematical statements into Lean 4 formal theorem declarations. Within the CriticLeanBench benchmark, our CriticLeanGPT models trained via supervised fine-tuning (SFT) and reinforcement learning (RL), along with their enhanced variants—outperform a range of closed-source API models, open-source models, and baseline models, highlighting distinct advantages. These outcomes yield several key insights: (1) Reasoning models excel in critical tasks, with Gemini 2.5 Pro, QwQ-32B, Qwen3-32B, and DeepSeek-R1 all attaining scores above 80. When compared to baseline models, our Qwen3-32B-RL model, optimized through RL, achieves a strong accuracy level, underscoring the efficacy of both our training methodology and dataset. (3) Our innovative mixed SFT strategy substantially boosts the performance of the Qwen2.5 family, with notable improvements observed across the 7B, 14B, and 32B models. (4) Additionally, SFT and RL significantly strengthen the models’ capacity to identify erroneous samples, as evidenced by higher true negative rates (TNR) and lower false negative rates (FNR)—a critical enhancement for accurate detection of incorrect formalizations, which is indispensable for effective critical tasks.\n\n### 5.3 Ablation Study\n\n#### 5.3.1 Effect of Reasoning Data\n\nWe conduct an ablation study on CriticLeanBench to evaluate the impact of different training strategies. As shown in Table 3, incorporating code and math reasoning data significantly improves performance across all model sizes compared to using Seed Data 4.1. Specifically, using the CriticLeanInstruct 4, which samples Critic and non-Critic data at a ratio of 1:3, leads to substantial gains, demonstrating that integrating diverse reasoning tasks enhances the critical reasoning capabilities of the model. This suggests that multi-task learning with math and code data improves the critique abilities of mathematical formalization.\n\n#### 5.3.2 Effect of SFT Dataset Size\n\nFigure 6 highlights a notable parameter-dependent relationship between the size of the SFT dataset and key reasoning performance. Across all model scales, performance improvements are observed through SFT, albeit with varying degrees of fluctuation depending on the training set size. Smaller models (e.g., 7B) exhibit more pronounced gains as the dataset expands, whereas larger models (e.g., 32B) demonstrate a less consistent trend, with marginal improvements at lower data volumes but substantial gains at higher data volumes. These findings align with prior studies [39, 78], underscoring the interplay between model capacity, data scale, and performance optimization in SFT scenarios. The results emphasize the need for tailored strategies to balance data efficiency and model generalization, particularly for large-scale architectures.&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>ACC&lt;/th>\n&lt;th>TPR&lt;/th>\n&lt;th>FPR&lt;/th>\n&lt;th>TNR&lt;/th>\n&lt;th>FNR&lt;/th>\n&lt;th>Reasoning&lt;/th>\n&lt;th>Open-source&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"8\" style=\"text-align: center;\">&lt;b>SOTA LLMs&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Gemini-2.5-Pro&lt;/td>\n&lt;td>&lt;u>89.2&lt;/u>&lt;/td>\n&lt;td>&lt;u>95.6&lt;/u>&lt;/td>\n&lt;td>&lt;u>4.4&lt;/u>&lt;/td>\n&lt;td>&lt;u>82.8&lt;/u>&lt;/td>\n&lt;td>&lt;u>17.2&lt;/u>&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>QwQ-32B&lt;/td>\n&lt;td>&lt;u>86.4&lt;/u>&lt;/td>\n&lt;td>93.6&lt;/td>\n&lt;td>6.4&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>20.8&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-32B&lt;/td>\n&lt;td>85.6&lt;/td>\n&lt;td>&lt;b>96.0&lt;/b>&lt;/td>\n&lt;td>&lt;b>4.0&lt;/b>&lt;/td>\n&lt;td>75.2&lt;/td>\n&lt;td>24.8&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-235B-A22B&lt;/td>\n&lt;td>84.8&lt;/td>\n&lt;td>90.4&lt;/td>\n&lt;td>9.6&lt;/td>\n&lt;td>79.2&lt;/td>\n&lt;td>20.8&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-R1&lt;/td>\n&lt;td>84.0&lt;/td>\n&lt;td>90.8&lt;/td>\n&lt;td>9.2&lt;/td>\n&lt;td>77.2&lt;/td>\n&lt;td>22.8&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-14B&lt;/td>\n&lt;td>83.6&lt;/td>\n&lt;td>92.4&lt;/td>\n&lt;td>7.6&lt;/td>\n&lt;td>74.8&lt;/td>\n&lt;td>25.2&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-8B&lt;/td>\n&lt;td>79.8&lt;/td>\n&lt;td>94.4&lt;/td>\n&lt;td>5.6&lt;/td>\n&lt;td>65.2&lt;/td>\n&lt;td>34.8&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Doubao-1.5-pro-32k&lt;/td>\n&lt;td>78.4&lt;/td>\n&lt;td>95.2&lt;/td>\n&lt;td>4.8&lt;/td>\n&lt;td>61.6&lt;/td>\n&lt;td>38.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Claude35-Sonnet&lt;/td>\n&lt;td>74.2&lt;/td>\n&lt;td>&lt;u>97.2&lt;/u>&lt;/td>\n&lt;td>&lt;u>2.8&lt;/u>&lt;/td>\n&lt;td>51.2&lt;/td>\n&lt;td>48.8&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>73.0&lt;/td>\n&lt;td>91.6&lt;/td>\n&lt;td>8.4&lt;/td>\n&lt;td>54.4&lt;/td>\n&lt;td>45.6&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-32B-Instruct&lt;/td>\n&lt;td>71.6&lt;/td>\n&lt;td>91.6&lt;/td>\n&lt;td>8.4&lt;/td>\n&lt;td>51.6&lt;/td>\n&lt;td>48.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Llama-3.3-70B-Instruct&lt;/td>\n&lt;td>68.2&lt;/td>\n&lt;td>95.2&lt;/td>\n&lt;td>4.8&lt;/td>\n&lt;td>41.2&lt;/td>\n&lt;td>58.8&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>GPT-4o-2024-11-20&lt;/td>\n&lt;td>67.8&lt;/td>\n&lt;td>95.6&lt;/td>\n&lt;td>4.4&lt;/td>\n&lt;td>40.0&lt;/td>\n&lt;td>60.0&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>66.6&lt;/td>\n&lt;td>80.4&lt;/td>\n&lt;td>19.6&lt;/td>\n&lt;td>52.8&lt;/td>\n&lt;td>47.2&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-Coder-7B-Instruct&lt;/td>\n&lt;td>65.4&lt;/td>\n&lt;td>88.4&lt;/td>\n&lt;td>11.6&lt;/td>\n&lt;td>42.4&lt;/td>\n&lt;td>57.6&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>60.8&lt;/td>\n&lt;td>89.6&lt;/td>\n&lt;td>10.4&lt;/td>\n&lt;td>32.0&lt;/td>\n&lt;td>68.0&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-Prover-V1.5-SFT&lt;/td>\n&lt;td>52.4&lt;/td>\n&lt;td>78.8&lt;/td>\n&lt;td>21.2&lt;/td>\n&lt;td>26.0&lt;/td>\n&lt;td>74.0&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepSeek-Prover-V1.5-RL&lt;/td>\n&lt;td>50.0&lt;/td>\n&lt;td>76.4&lt;/td>\n&lt;td>23.6&lt;/td>\n&lt;td>23.6&lt;/td>\n&lt;td>76.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"8\" style=\"text-align: center;\">&lt;b>CriticLeanGPT (Ours)&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-8B-RL&lt;/td>\n&lt;td>79.8&lt;/td>\n&lt;td>90.0&lt;/td>\n&lt;td>10.0&lt;/td>\n&lt;td>72.0&lt;/td>\n&lt;td>28.0&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-14B-RL&lt;/td>\n&lt;td>84.8&lt;/td>\n&lt;td>91.6&lt;/td>\n&lt;td>8.4&lt;/td>\n&lt;td>78.0&lt;/td>\n&lt;td>22.0&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen3-32B-RL&lt;/td>\n&lt;td>&lt;b>87.0&lt;/b>&lt;/td>\n&lt;td>88.4&lt;/td>\n&lt;td>11.6&lt;/td>\n&lt;td>&lt;u>85.6&lt;/u>&lt;/td>\n&lt;td>&lt;u>14.4&lt;/u>&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct-RL&lt;/td>\n&lt;td>68.6&lt;/td>\n&lt;td>85.6&lt;/td>\n&lt;td>14.4&lt;/td>\n&lt;td>51.6&lt;/td>\n&lt;td>48.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct-RL&lt;/td>\n&lt;td>69.4&lt;/td>\n&lt;td>85.2&lt;/td>\n&lt;td>14.8&lt;/td>\n&lt;td>53.6&lt;/td>\n&lt;td>46.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct-RL&lt;/td>\n&lt;td>72.0&lt;/td>\n&lt;td>60.4&lt;/td>\n&lt;td>39.6&lt;/td>\n&lt;td>&lt;b>83.6&lt;/b>&lt;/td>\n&lt;td>&lt;b>16.4&lt;/b>&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct-SFT&lt;/td>\n&lt;td>69.8&lt;/td>",
      "numLines": 300,
      "startLine": 199,
      "totalLines": 1768
    }
  },
  "sourceToolAssistantUUID": "7759c2ec-e23f-435c-8333-7475d73266eb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 71 · 2026-05-27T18:17:55.528Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the critical data. Let me continue reading to get the remaining results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5620acf7-69b7-45f1-97d6-2567e52382b9",
  "isSidechain": false,
  "requestId": "req_011CbTXsYTKqtgz1Qz7HRdV3",
  "type": "assistant",
  "uuid": "1b341449-28fa-4e62-919e-01098953dd7d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016R6PWZzFBRKVtGRQQxCo8L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5168,
      "cache_read_input_tokens": 37779,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5168,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 37779,
          "cache_creation_input_tokens": 5168,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5168
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

_source line 72 · 2026-05-27T18:17:59.200Z_

<details open><summary>🔧 Tool call — Read · `toolu_01M6DsWSLs9AQA3AZCuSkpPD`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/2a30fe45-086a-4752-b69b-cc68f89516e6/tool-results/toolu_016rqZDKmFkzrH3XvWTnogpJ.txt",
  "limit": 300,
  "offset": 495
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b341449-28fa-4e62-919e-01098953dd7d",
  "isSidechain": false,
  "requestId": "req_011CbTXsYTKqtgz1Qz7HRdV3",
  "type": "assistant",
  "uuid": "a70d6d98-9f21-4d29-8995-9be57c3a1958",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016R6PWZzFBRKVtGRQQxCo8L",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5168,
      "cache_read_input_tokens": 37779,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5168,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 37779,
          "cache_creation_input_tokens": 5168,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5168
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

_source line 73 · 2026-05-27T18:17:59.206Z_

<details><summary>↩ Tool result · `toolu_01M6DsWSLs9AQA3AZCuSkpPD`</summary>

```text
495	&lt;/tr>
496	&lt;tr>
497	&lt;td>Qwen2.5-7B-Instruct-SFT&lt;/td>
498	&lt;td>69.8&lt;/td>
499	&lt;td>94.4&lt;/td>
500	&lt;td>5.6&lt;/td>
501	&lt;td>45.2&lt;/td>
502	&lt;td>54.8&lt;/td>
503	&lt;td>✗&lt;/td>
504	&lt;td>✓&lt;/td>
505	&lt;/tr>
506	&lt;tr>
507	&lt;td>Qwen2.5-14B-Instruct-SFT&lt;/td>
508	&lt;td>70.6&lt;/td>
509	&lt;td>83.6&lt;/td>
510	&lt;td>16.4&lt;/td>
511	&lt;td>57.6&lt;/td>
512	&lt;td>42.4&lt;/td>
513	&lt;td>✗&lt;/td>
514	&lt;td>✓&lt;/td>
515	&lt;/tr>
516	&lt;tr>
517	&lt;td>Qwen2.5-32B-Instruct-SFT&lt;/td>
518	&lt;td>76.2&lt;/td>
519	&lt;td>85.2&lt;/td>
520	&lt;td>14.8&lt;/td>
521	&lt;td>67.2&lt;/td>
522	&lt;td>32.8&lt;/td>
523	&lt;td>✗&lt;/td>
524	&lt;td>✓&lt;/td>
525	&lt;/tr>
526	&lt;tr>
527	&lt;td>Qwen2.5-7B-Instruct-SFT-RL&lt;/td>
528	&lt;td>68.2&lt;/td>
529	&lt;td>90.4&lt;/td>
530	&lt;td>9.6&lt;/td>
531	&lt;td>46.0&lt;/td>
532	&lt;td>54.0&lt;/td>
533	&lt;td>✗&lt;/td>
534	&lt;td>✓&lt;/td>
535	&lt;/tr>
536	&lt;tr>
537	&lt;td>Qwen2.5-14B-Instruct-SFT-RL&lt;/td>
538	&lt;td>74.6&lt;/td>
539	&lt;td>81.6&lt;/td>
540	&lt;td>18.4&lt;/td>
541	&lt;td>67.6&lt;/td>
542	&lt;td>32.4&lt;/td>
543	&lt;td>✗&lt;/td>
544	&lt;td>✓&lt;/td>
545	&lt;/tr>
546	&lt;tr>
547	&lt;td>Qwen2.5-32B-Instruct-SFT-RL&lt;/td>
548	&lt;td>78.6&lt;/td>
549	&lt;td>88.0&lt;/td>
550	&lt;td>12.0&lt;/td>
551	&lt;td>69.2&lt;/td>
552	&lt;td>30.8&lt;/td>
553	&lt;td>✗&lt;/td>
554	&lt;td>✓&lt;/td>
555	&lt;/tr>
556	&lt;/tbody>
557	&lt;/table>
558	
559	**Table 2 Performance on CriticLeanBench.** The best, the second-best and the third-best scores for each indicator are shown in box, **bold** and underlined, respectively.&lt;table border="1">
560	&lt;thead>
561	&lt;tr>
562	&lt;th>Model&lt;/th>
563	&lt;th>ACC&lt;/th>
564	&lt;th>TPR&lt;/th>
565	&lt;th>FPR&lt;/th>
566	&lt;th>TNR&lt;/th>
567	&lt;th>FNR&lt;/th>
568	&lt;/tr>
569	&lt;/thead>
570	&lt;tbody>
571	&lt;tr>
572	&lt;td colspan="6" style="text-align: center;">&lt;b>7B Size Models&lt;/b>&lt;/td>
573	&lt;/tr>
574	&lt;tr>
575	&lt;td>Qwen2.5-7B-Instruct&lt;/td>
576	&lt;td>60.8&lt;/td>
577	&lt;td>89.6&lt;/td>
578	&lt;td>10.4&lt;/td>
579	&lt;td>32.0&lt;/td>
580	&lt;td>68.0&lt;/td>
581	&lt;/tr>
582	&lt;tr>
583	&lt;td>Qwen2.5-7B-Instruct-SFT(Critic Only)&lt;/td>
584	&lt;td>64.0&lt;/td>
585	&lt;td>70.8&lt;/td>
586	&lt;td>29.2&lt;/td>
587	&lt;td>&lt;span style="border: 1px solid black;">57.2&lt;/span>&lt;/td>
588	&lt;td>&lt;span style="border: 1px solid black;">42.8&lt;/span>&lt;/td>
589	&lt;/tr>
590	&lt;tr>
591	&lt;td>Qwen2.5-7B-Instruct-SFT&lt;/td>
592	&lt;td>&lt;span style="border: 1px solid black;">69.8&lt;/span>&lt;/td>
593	&lt;td>&lt;span style="border: 1px solid black;">94.4&lt;/span>&lt;/td>
594	&lt;td>&lt;span style="border: 1px solid black;">5.6&lt;/span>&lt;/td>
595	&lt;td>45.2&lt;/td>
596	&lt;td>54.8&lt;/td>
597	&lt;/tr>
598	&lt;tr>
599	&lt;td colspan="6" style="text-align: center;">&lt;b>14B Size Models&lt;/b>&lt;/td>
600	&lt;/tr>
601	&lt;tr>
602	&lt;td>Qwen2.5-14B-Instruct&lt;/td>
603	&lt;td>66.6&lt;/td>
604	&lt;td>80.4&lt;/td>
605	&lt;td>19.6&lt;/td>
606	&lt;td>52.8&lt;/td>
607	&lt;td>47.2&lt;/td>
608	&lt;/tr>
609	&lt;tr>
610	&lt;td>Qwen2.5-14B-Instruct-SFT(Critic Only)&lt;/td>
611	&lt;td>67.4&lt;/td>
612	&lt;td>80.8&lt;/td>
613	&lt;td>19.2&lt;/td>
614	&lt;td>54.0&lt;/td>
615	&lt;td>46.0&lt;/td>
616	&lt;/tr>
617	&lt;tr>
618	&lt;td>Qwen2.5-14B-Instruct-SFT&lt;/td>
619	&lt;td>&lt;span style="border: 1px solid black;">70.6&lt;/span>&lt;/td>
620	&lt;td>&lt;span style="border: 1px solid black;">83.6&lt;/span>&lt;/td>
621	&lt;td>&lt;span style="border: 1px solid black;">16.4&lt;/span>&lt;/td>
622	&lt;td>&lt;span style="border: 1px solid black;">57.6&lt;/span>&lt;/td>
623	&lt;td>&lt;span style="border: 1px solid black;">42.4&lt;/span>&lt;/td>
624	&lt;/tr>
625	&lt;tr>
626	&lt;td colspan="6" style="text-align: center;">&lt;b>32B Size Models&lt;/b>&lt;/td>
627	&lt;/tr>
628	&lt;tr>
629	&lt;td>Qwen2.5-32B-Instruct&lt;/td>
630	&lt;td>73.0&lt;/td>
631	&lt;td>&lt;span style="border: 1px solid black;">91.6&lt;/span>&lt;/td>
632	&lt;td>&lt;span style="border: 1px solid black;">8.4&lt;/span>&lt;/td>
633	&lt;td>54.4&lt;/td>
634	&lt;td>45.6&lt;/td>
635	&lt;/tr>
636	&lt;tr>
637	&lt;td>Qwen2.5-32B-Instruct-SFT(Critic Only)&lt;/td>
638	&lt;td>71.0&lt;/td>
639	&lt;td>72.0&lt;/td>
640	&lt;td>28.0&lt;/td>
641	&lt;td>&lt;span style="border: 1px solid black;">70.0&lt;/span>&lt;/td>
642	&lt;td>&lt;span style="border: 1px solid black;">30.0&lt;/span>&lt;/td>
643	&lt;/tr>
644	&lt;tr>
645	&lt;td>Qwen2.5-32B-Instruct-SFT&lt;/td>
646	&lt;td>&lt;span style="border: 1px solid black;">76.2&lt;/span>&lt;/td>
647	&lt;td>85.2&lt;/td>
648	&lt;td>14.8&lt;/td>
649	&lt;td>67.2&lt;/td>
650	&lt;td>32.8&lt;/td>
651	&lt;/tr>
652	&lt;/tbody>
653	&lt;/table>
654	
655	**Table 3 Comparison of model performance under different training strategies:** base model, SFT on Critic data only, and SFT on combined Critic, code, and math data. The best score for each indicator is shown in box.
656	
657	## 5.4 Analysis
658	
659	### 5.4.1 Scaling Analysis
660	
661	We evaluate the performance of Qwen series models on CriticLeanBench across different model scales, including Qwen2.5-Coder, Qwen2.5-Instruct, Qwen2.5-Instruct-SFT, Qwen2.5-Instruct-SFT-RL, Qwen3, and Qwen3-RL. The results in Figure 4 show that the performance improves consistently as the model size increases, demonstrating a clear scaling law of LLMs on CriticLeanBench.
662	
663	### 5.4.2 Effect of Pass@k
664	
665	The Pass@k metric serves as a means to identify the highest-quality answers from multi-modal large language models (MLLMs) for final responses, highlighting the models’ potential for enhancement through post-training techniques like Reinforcement Learning from Human Feedback (RLHF [25]) and Gradient Penalty Policy Optimization (GRPO [46]). In this study, Pass@k evaluations were conducted on Qwen2.5-7B-Instruct, Qwen2.5-7B-Instruct-SFT-RL, Qwen3-8B, and Qwen3-8B-RL using CriticLeanBench, with k set to 8 and 32, and evaluation metrics including Accuracy (ACC), True Positive Rate (TPR), and True Negative Rate (TNR).
666	
667	As shown in Figure 5, we observe that models subjected to Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) achieve better overall performance. Considering Pass@32, the Accuracy of Qwen2.5-7B-Instruct is outperformed by that of Qwen2.5-7B-Instruct-SFT-RL, which has undergone SFT and RL processing, leading to a notable improvement in the overall correctness rate. Regarding the True Negative Rate, models without SFT and RL processing are more prone to misclassifying incorrect samples as correct, whereas processed models effectively mitigate such errors; this is evident in the higher TNR of Qwen2.5-7B-Instruct-SFT-RL compared to Qwen2.5-7B-Instruct at Pass@32, reducing the likelihood of
668	
669	**Figure 6 Comparison of model performance under different amounts of SFT data:** base model, CriticLeanInstruct(16K), and CriticLeanInstruct.**Figure 4** Scaling Analysis of LLMs on CriticLeanBench.  $\hat{\square}$  denoted closed-source LLMs.
670	
671	such misclassifications. A similar trend is observed in Qwen3-8B. Additionally, all models exhibit improved performance as  $k$  increases, suggesting that SFT- and RL-optimized models can more effectively select high-quality answers when provided with more candidate responses.
672	
673	## 6 FineLeanCorpus
674	
675	To construct the FineLeanCorpus, we began by aggregating a vast and diverse collection of natural language mathematical problems. Sourcing from a wide array of materials, including high school olympiad datasets (e.g., AoPS, BlueMO), standard high school curricula (e.g., TAL-SCQ5), and undergraduate-level challenges (e.g., Omni-MATH), we ensured an extensive initial distribution in both the mathematical domain and difficulty. The first step in our process was to standardize this heterogeneous collection into a uniform, proof-based format, making each problem compatible with the Lean 4 theorem prover and ready for the subsequent formalization pipeline.
676	
677	These standardized problems were then subjected to a rigorous, gated auto-formalization process powered by our CriticLean framework (Figure 1). The Kimina-Autoformalizer-7B model first generates a candidate formal statement. This statement must pass a syntactic check via the Lean 4 compiler; failure leads to regeneration. A successful compilation is followed by a semantic correctness check from our CriticLeanGPT model, with rejection also triggering a new attempt. This regenerative approach is critical, maximizing the yield from our source corpus by iteratively seeking a valid formalization. Finally, to further enhance precision, we apply a final filtering stage using another,
678	
679	&lt;table border="1">
680	&lt;thead>
681	&lt;tr>
682	&lt;th>Statistics&lt;/th>
683	&lt;th>Number&lt;/th>
684	&lt;/tr>
685	&lt;/thead>
686	&lt;tbody>
687	&lt;tr>
688	&lt;td>#Problems&lt;/td>
689	&lt;td>285957&lt;/td>
690	&lt;/tr>
691	&lt;tr>
692	&lt;td>&lt;b>Length&lt;/b>&lt;/td>
693	&lt;td>&lt;/td>
694	&lt;/tr>
695	&lt;tr>
696	&lt;td>&lt;i>Statement&lt;/i>&lt;/td>
697	&lt;td>&lt;/td>
698	&lt;/tr>
699	&lt;tr>
700	&lt;td>maximum length&lt;/td>
701	&lt;td>2980 tokens&lt;/td>
702	&lt;/tr>
703	&lt;tr>
704	&lt;td>minimum length&lt;/td>
705	&lt;td>9 tokens&lt;/td>
706	&lt;/tr>
707	&lt;tr>
708	&lt;td>avg length&lt;/td>
709	&lt;td>78.4 tokens&lt;/td>
710	&lt;/tr>
711	&lt;tr>
712	&lt;td>&lt;i>Lean Result(success)&lt;/i>&lt;/td>
713	&lt;td>&lt;/td>
714	&lt;/tr>
715	&lt;tr>
716	&lt;td>maximum length&lt;/td>
717	&lt;td>768 tokens&lt;/td>
718	&lt;/tr>
719	&lt;tr>
720	&lt;td>minimum length&lt;/td>
721	&lt;td>14 tokens&lt;/td>
722	&lt;/tr>
723	&lt;tr>
724	&lt;td>avg length&lt;/td>
725	&lt;td>87.8 tokens&lt;/td>
726	&lt;/tr>
727	&lt;/tbody>
728	&lt;/table>
729	
730	**Table 5** Dataset statistics of FineLeanCorpus.**Figure 5** Performance on CriticLeanBench using **Pass@k** metrics, where **k = 8** (left) and **k = 32** (right).
731	
732	&lt;table border="1">
733	&lt;thead>
734	&lt;tr>
735	&lt;th>Dataset&lt;/th>
736	&lt;th>Difficulty Level&lt;/th>
737	&lt;th>Size&lt;/th>
738	&lt;/tr>
739	&lt;/thead>
740	&lt;tbody>
741	&lt;tr>
742	&lt;td>AOPs [35]&lt;/td>
743	&lt;td>High School Olympiad&lt;/td>
744	&lt;td>199982&lt;/td>
745	&lt;/tr>
746	&lt;tr>
747	&lt;td>DeepMath-103k [15]&lt;/td>
748	&lt;td>Diverse&lt;/td>
749	&lt;td>28538&lt;/td>
750	&lt;/tr>
751	&lt;tr>
752	&lt;td>NuminaMath-TIR [24]&lt;/td>
753	&lt;td>High School&lt;/td>
754	&lt;td>22847&lt;/td>
755	&lt;/tr>
756	&lt;tr>
757	&lt;td>DeepTheorem [74]&lt;/td>
758	&lt;td>High School Olympiad&lt;/td>
759	&lt;td>15131&lt;/td>
760	&lt;/tr>
761	&lt;tr>
762	&lt;td>DeepScaleR [34]&lt;/td>
763	&lt;td>High School Olympiad&lt;/td>
764	&lt;td>11544&lt;/td>
765	&lt;/tr>
766	&lt;tr>
767	&lt;td>DAPO-Math-17k [66]&lt;/td>
768	&lt;td>High School&lt;/td>
769	&lt;td>4078&lt;/td>
770	&lt;/tr>
771	&lt;tr>
772	&lt;td>Omni-MATH [8]&lt;/td>
773	&lt;td>Undergraduate&lt;/td>
774	&lt;td>1176&lt;/td>
775	&lt;/tr>
776	&lt;tr>
777	&lt;td>IneqMath [20]&lt;/td>
778	&lt;td>High School Olympiad&lt;/td>
779	&lt;td>963&lt;/td>
780	&lt;/tr>
781	&lt;tr>
782	&lt;td>BlueMO [73]&lt;/td>
783	&lt;td>High School Olympiad&lt;/td>
784	&lt;td>616&lt;/td>
785	&lt;/tr>
786	&lt;tr>
787	&lt;td>TAL-SCQ5K [37]&lt;/td>
788	&lt;td>High School&lt;/td>
789	&lt;td>393&lt;/td>
790	&lt;/tr>
791	&lt;tr>
792	&lt;td>OnlineMathContest&lt;/td>
793	&lt;td>High School&lt;/td>
794	&lt;td>70&lt;/td>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a70d6d98-9f21-4d29-8995-9be57c3a1958",
  "isSidechain": false,
  "promptId": "4b0c0804-0c80-4fc4-bd2d-54c91b4a93a7",
  "type": "user",
  "uuid": "b50f9e67-0630-4c05-86dc-b2219c411903",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/2a30fe45-086a-4752-b69b-cc68f89516e6/tool-results/toolu_016rqZDKmFkzrH3XvWTnogpJ.txt",
      "content": "&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct-SFT&lt;/td>\n&lt;td>69.8&lt;/td>\n&lt;td>94.4&lt;/td>\n&lt;td>5.6&lt;/td>\n&lt;td>45.2&lt;/td>\n&lt;td>54.8&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct-SFT&lt;/td>\n&lt;td>70.6&lt;/td>\n&lt;td>83.6&lt;/td>\n&lt;td>16.4&lt;/td>\n&lt;td>57.6&lt;/td>\n&lt;td>42.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct-SFT&lt;/td>\n&lt;td>76.2&lt;/td>\n&lt;td>85.2&lt;/td>\n&lt;td>14.8&lt;/td>\n&lt;td>67.2&lt;/td>\n&lt;td>32.8&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct-SFT-RL&lt;/td>\n&lt;td>68.2&lt;/td>\n&lt;td>90.4&lt;/td>\n&lt;td>9.6&lt;/td>\n&lt;td>46.0&lt;/td>\n&lt;td>54.0&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct-SFT-RL&lt;/td>\n&lt;td>74.6&lt;/td>\n&lt;td>81.6&lt;/td>\n&lt;td>18.4&lt;/td>\n&lt;td>67.6&lt;/td>\n&lt;td>32.4&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct-SFT-RL&lt;/td>\n&lt;td>78.6&lt;/td>\n&lt;td>88.0&lt;/td>\n&lt;td>12.0&lt;/td>\n&lt;td>69.2&lt;/td>\n&lt;td>30.8&lt;/td>\n&lt;td>✗&lt;/td>\n&lt;td>✓&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 2 Performance on CriticLeanBench.** The best, the second-best and the third-best scores for each indicator are shown in box, **bold** and underlined, respectively.&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>ACC&lt;/th>\n&lt;th>TPR&lt;/th>\n&lt;th>FPR&lt;/th>\n&lt;th>TNR&lt;/th>\n&lt;th>FNR&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td colspan=\"6\" style=\"text-align: center;\">&lt;b>7B Size Models&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct&lt;/td>\n&lt;td>60.8&lt;/td>\n&lt;td>89.6&lt;/td>\n&lt;td>10.4&lt;/td>\n&lt;td>32.0&lt;/td>\n&lt;td>68.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct-SFT(Critic Only)&lt;/td>\n&lt;td>64.0&lt;/td>\n&lt;td>70.8&lt;/td>\n&lt;td>29.2&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">57.2&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">42.8&lt;/span>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-7B-Instruct-SFT&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">69.8&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">94.4&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">5.6&lt;/span>&lt;/td>\n&lt;td>45.2&lt;/td>\n&lt;td>54.8&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\" style=\"text-align: center;\">&lt;b>14B Size Models&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct&lt;/td>\n&lt;td>66.6&lt;/td>\n&lt;td>80.4&lt;/td>\n&lt;td>19.6&lt;/td>\n&lt;td>52.8&lt;/td>\n&lt;td>47.2&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct-SFT(Critic Only)&lt;/td>\n&lt;td>67.4&lt;/td>\n&lt;td>80.8&lt;/td>\n&lt;td>19.2&lt;/td>\n&lt;td>54.0&lt;/td>\n&lt;td>46.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-14B-Instruct-SFT&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">70.6&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">83.6&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">16.4&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">57.6&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">42.4&lt;/span>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td colspan=\"6\" style=\"text-align: center;\">&lt;b>32B Size Models&lt;/b>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct&lt;/td>\n&lt;td>73.0&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">91.6&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">8.4&lt;/span>&lt;/td>\n&lt;td>54.4&lt;/td>\n&lt;td>45.6&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct-SFT(Critic Only)&lt;/td>\n&lt;td>71.0&lt;/td>\n&lt;td>72.0&lt;/td>\n&lt;td>28.0&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">70.0&lt;/span>&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">30.0&lt;/span>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Qwen2.5-32B-Instruct-SFT&lt;/td>\n&lt;td>&lt;span style=\"border: 1px solid black;\">76.2&lt;/span>&lt;/td>\n&lt;td>85.2&lt;/td>\n&lt;td>14.8&lt;/td>\n&lt;td>67.2&lt;/td>\n&lt;td>32.8&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 3 Comparison of model performance under different training strategies:** base model, SFT on Critic data only, and SFT on combined Critic, code, and math data. The best score for each indicator is shown in box.\n\n## 5.4 Analysis\n\n### 5.4.1 Scaling Analysis\n\nWe evaluate the performance of Qwen series models on CriticLeanBench across different model scales, including Qwen2.5-Coder, Qwen2.5-Instruct, Qwen2.5-Instruct-SFT, Qwen2.5-Instruct-SFT-RL, Qwen3, and Qwen3-RL. The results in Figure 4 show that the performance improves consistently as the model size increases, demonstrating a clear scaling law of LLMs on CriticLeanBench.\n\n### 5.4.2 Effect of Pass@k\n\nThe Pass@k metric serves as a means to identify the highest-quality answers from multi-modal large language models (MLLMs) for final responses, highlighting the models’ potential for enhancement through post-training techniques like Reinforcement Learning from Human Feedback (RLHF [25]) and Gradient Penalty Policy Optimization (GRPO [46]). In this study, Pass@k evaluations were conducted on Qwen2.5-7B-Instruct, Qwen2.5-7B-Instruct-SFT-RL, Qwen3-8B, and Qwen3-8B-RL using CriticLeanBench, with k set to 8 and 32, and evaluation metrics including Accuracy (ACC), True Positive Rate (TPR), and True Negative Rate (TNR).\n\nAs shown in Figure 5, we observe that models subjected to Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL) achieve better overall performance. Considering Pass@32, the Accuracy of Qwen2.5-7B-Instruct is outperformed by that of Qwen2.5-7B-Instruct-SFT-RL, which has undergone SFT and RL processing, leading to a notable improvement in the overall correctness rate. Regarding the True Negative Rate, models without SFT and RL processing are more prone to misclassifying incorrect samples as correct, whereas processed models effectively mitigate such errors; this is evident in the higher TNR of Qwen2.5-7B-Instruct-SFT-RL compared to Qwen2.5-7B-Instruct at Pass@32, reducing the likelihood of\n\n**Figure 6 Comparison of model performance under different amounts of SFT data:** base model, CriticLeanInstruct(16K), and CriticLeanInstruct.**Figure 4** Scaling Analysis of LLMs on CriticLeanBench.  $\\hat{\\square}$  denoted closed-source LLMs.\n\nsuch misclassifications. A similar trend is observed in Qwen3-8B. Additionally, all models exhibit improved performance as  $k$  increases, suggesting that SFT- and RL-optimized models can more effectively select high-quality answers when provided with more candidate responses.\n\n## 6 FineLeanCorpus\n\nTo construct the FineLeanCorpus, we began by aggregating a vast and diverse collection of natural language mathematical problems. Sourcing from a wide array of materials, including high school olympiad datasets (e.g., AoPS, BlueMO), standard high school curricula (e.g., TAL-SCQ5), and undergraduate-level challenges (e.g., Omni-MATH), we ensured an extensive initial distribution in both the mathematical domain and difficulty. The first step in our process was to standardize this heterogeneous collection into a uniform, proof-based format, making each problem compatible with the Lean 4 theorem prover and ready for the subsequent formalization pipeline.\n\nThese standardized problems were then subjected to a rigorous, gated auto-formalization process powered by our CriticLean framework (Figure 1). The Kimina-Autoformalizer-7B model first generates a candidate formal statement. This statement must pass a syntactic check via the Lean 4 compiler; failure leads to regeneration. A successful compilation is followed by a semantic correctness check from our CriticLeanGPT model, with rejection also triggering a new attempt. This regenerative approach is critical, maximizing the yield from our source corpus by iteratively seeking a valid formalization. Finally, to further enhance precision, we apply a final filtering stage using another,\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Statistics&lt;/th>\n&lt;th>Number&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>#Problems&lt;/td>\n&lt;td>285957&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;b>Length&lt;/b>&lt;/td>\n&lt;td>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;i>Statement&lt;/i>&lt;/td>\n&lt;td>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>maximum length&lt;/td>\n&lt;td>2980 tokens&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>minimum length&lt;/td>\n&lt;td>9 tokens&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>avg length&lt;/td>\n&lt;td>78.4 tokens&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>&lt;i>Lean Result(success)&lt;/i>&lt;/td>\n&lt;td>&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>maximum length&lt;/td>\n&lt;td>768 tokens&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>minimum length&lt;/td>\n&lt;td>14 tokens&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>avg length&lt;/td>\n&lt;td>87.8 tokens&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 5** Dataset statistics of FineLeanCorpus.**Figure 5** Performance on CriticLeanBench using **Pass@k** metrics, where **k = 8** (left) and **k = 32** (right).\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Dataset&lt;/th>\n&lt;th>Difficulty Level&lt;/th>\n&lt;th>Size&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>AOPs [35]&lt;/td>\n&lt;td>High School Olympiad&lt;/td>\n&lt;td>199982&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepMath-103k [15]&lt;/td>\n&lt;td>Diverse&lt;/td>\n&lt;td>28538&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>NuminaMath-TIR [24]&lt;/td>\n&lt;td>High School&lt;/td>\n&lt;td>22847&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepTheorem [74]&lt;/td>\n&lt;td>High School Olympiad&lt;/td>\n&lt;td>15131&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepScaleR [34]&lt;/td>\n&lt;td>High School Olympiad&lt;/td>\n&lt;td>11544&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DAPO-Math-17k [66]&lt;/td>\n&lt;td>High School&lt;/td>\n&lt;td>4078&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Omni-MATH [8]&lt;/td>\n&lt;td>Undergraduate&lt;/td>\n&lt;td>1176&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>IneqMath [20]&lt;/td>\n&lt;td>High School Olympiad&lt;/td>\n&lt;td>963&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>BlueMO [73]&lt;/td>\n&lt;td>High School Olympiad&lt;/td>\n&lt;td>616&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>TAL-SCQ5K [37]&lt;/td>\n&lt;td>High School&lt;/td>\n&lt;td>393&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>OnlineMathContest&lt;/td>\n&lt;td>High School&lt;/td>\n&lt;td>70&lt;/td>",
      "numLines": 300,
      "startLine": 495,
      "totalLines": 1768
    }
  },
  "sourceToolAssistantUUID": "a70d6d98-9f21-4d29-8995-9be57c3a1958",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 74_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Aut…",
  "leafUuid": "b50f9e67-0630-4c05-86dc-b2219c411903",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6"
}
```

---

### Runtime record

_source line 75_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise autoformalization TTRL paper with verified data and concrete curriculum",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6"
}
```

---

### Assistant

_source line 76 · 2026-05-27T18:18:05.307Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the key data I need. Let me also check the pipeline accuracy improvement claims (54% to 84%). Let me continue reading the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b50f9e67-0630-4c05-86dc-b2219c411903",
  "isSidechain": false,
  "requestId": "req_011CbTXt6txZAhm5xgQEFUU8",
  "type": "assistant",
  "uuid": "3493290a-f8aa-4834-a667-2cd16a133721",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9AyA5CVZm8s9MGNxoSwXM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4589,
      "cache_read_input_tokens": 42947,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4589,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 42947,
          "cache_creation_input_tokens": 4589,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4589
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

_source line 77 · 2026-05-27T18:18:08.524Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Kj3v7qiAggk3RD3asCfhsC`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/2a30fe45-086a-4752-b69b-cc68f89516e6/tool-results/toolu_016rqZDKmFkzrH3XvWTnogpJ.txt",
  "limit": 200,
  "offset": 790
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3493290a-f8aa-4834-a667-2cd16a133721",
  "isSidechain": false,
  "requestId": "req_011CbTXt6txZAhm5xgQEFUU8",
  "type": "assistant",
  "uuid": "240aae25-e7d0-411b-8445-e3a59da92010",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9AyA5CVZm8s9MGNxoSwXM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4589,
      "cache_read_input_tokens": 42947,
      "output_tokens": 208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4589,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 208,
          "cache_read_input_tokens": 42947,
          "cache_creation_input_tokens": 4589,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4589
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

_source line 78 · 2026-05-27T18:18:08.530Z_

<details><summary>↩ Tool result · `toolu_01Kj3v7qiAggk3RD3asCfhsC`</summary>

```text
790	&lt;/tr>
791	&lt;tr>
792	&lt;td>OnlineMathContest&lt;/td>
793	&lt;td>High School&lt;/td>
794	&lt;td>70&lt;/td>
795	&lt;/tr>
796	&lt;tr>
797	&lt;td>Multi-Source Math Competition&lt;/td>
798	&lt;td>High School Olympiad&lt;/td>
799	&lt;td>619&lt;/td>
800	&lt;/tr>
801	&lt;/tbody>
802	&lt;/table>
803	
804	**Table 4** Overview of different sources for FineLeanCorpus.
805	
806	higher-performance CriticLeanGPT model. Manual validation indicates that this step is expected to eliminate 74.7% of the remaining incorrect formalizations. The resulting corpus is characterized by its expressive range: natural language statements vary from a concise 9 tokens to a complex 2,980 tokens (avg. 78.4), while their corresponding Lean formalizations span from 14 to 768 tokens (avg. 87.8), reflecting the deep spectrum of complexity successfully captured by our pipeline.
807	
808	To further analyze the differences between our FineLeanCorpus dataset and the Lean-Workbook, we employed the templates from Appendix J and Appendix I to assess the difficulty levels and classify the mathematical domains of the datasets using Doubao-1.5-pro [12]. A comparative analysis of our proposed FineLeanCorpus against Lean-Workbook (Figure 7, Figure 8, Table 4 and Table 5) reveals two fundamental advancements: (1) Scale and Coverage: Our corpus provides a significant quantitative expansion in both problem difficulty and domain coverage. This expansion is evident not only across nearly the entire difficulty spectrum—offering a much richer data pool for training foundational skills—but also in the substantial augmentation of high-volume domains like Intermediate Algebra and Elementary Number Theory. (2) FineLeanCorpus exhibits a more diverse and structurally balanced profile, achieved by collecting natural language statements from numerous sources. From a difficulty perspective, it features a multimodal distribution with substantial problem counts at several distinct complexity points, in stark contrast to the unimodal distribution of Lean-Workbook. This characteristic is crucial for mitigating model overfitting to a narrow complexity band. From a domain perspective, it substantially reinforces previously underrepresented areas. For instance, categories such as Analytic Geometry and Integral Calculus are significantly expanded, while niche topics like Algorithms and Graph Theory are also robustly augmented. This targeted enrichment transforms sparsely sampled topics into well-supported, learnable sub-domains, yielding a more comprehensive dataset designed to fosterholistic reasoning capabilities. More details regarding our FineLeanCorpus dataset, including its fine-grained mathematical domain distribution (see Appendix A), are provided for further analysis.
809	
810	Furthermore, to push the boundaries of current models and foster research into the upper echelons of mathematical reasoning, we have curated a specialized training subset from FineLeanCorpus, which we designate as Diamond. This subset comprises 36,033 problems with a difficulty rating exceeding 5. The purpose of this high-difficulty training set is to create a demanding training environment that fosters the development of the sophisticated, multi-step reasoning required to tackle the most formidable mathematical problems. A detailed breakdown of the mathematical domain distribution within this subset is provided in table 11.
811	
812	&lt;table border="1">
813	&lt;thead>
814	&lt;tr>
815	&lt;th>Dataset&lt;/th>
816	&lt;th>Source&lt;/th>
817	&lt;th>Theorems&lt;/th>
818	&lt;th>Level&lt;/th>
819	&lt;th>Detailed Critic Process&lt;/th>
820	&lt;th>Difficulty Profile&lt;/th>
821	&lt;th>Topic Diversity&lt;/th>
822	&lt;/tr>
823	&lt;/thead>
824	&lt;tbody>
825	&lt;tr>
826	&lt;td>Lean-Workbook [65]&lt;/td>
827	&lt;td>Synthetic&lt;/td>
828	&lt;td>140K&lt;/td>
829	&lt;td>Undergraduate&lt;/td>
830	&lt;td>Opaque&lt;/td>
831	&lt;td>Avg: 3.70&lt;br/>Top-tier (&lt;math>\geq 6&lt;/math>): 7.81%&lt;/td>
832	&lt;td>Highly Skewed&lt;/td>
833	&lt;/tr>
834	&lt;tr>
835	&lt;td>FineLeanCorpus (ours)&lt;/td>
836	&lt;td>Synthetic&lt;/td>
837	&lt;td>285K&lt;/td>
838	&lt;td>Diverse&lt;/td>
839	&lt;td>Transparent&lt;/td>
840	&lt;td>Avg: 3.24&lt;br/>Top-tier (&lt;math>\geq 6&lt;/math>): 11.10%&lt;/td>
841	&lt;td>Balanced &amp; Diverse&lt;/td>
842	&lt;/tr>
843	&lt;/tbody>
844	&lt;/table>
845	
846	**Table 6** Comparison of dataset statistics. FineLeanCorpus offers a transparent critic process, a higher proportion of top-tier problems, and a more balanced and diverse topic distribution compared to the highly skewed Lean-Workbook.
847	
848	**Figure 7** Comparison of dataset statistics. FineLeanCorpus offers a transparent critic process, a higher proportion of top-tier problems, and a more balanced and diverse topic distribution compared to the highly skewed Lean-Workbook.
849	
850	## 6.1 Analysis on CriticLean Pipeline
851	
852	As shown in Table 7, our autoformalization pipeline significantly improves accuracy. We selected 50 problems from the Omni-MATH and applied the following three formalization strategies, with the correctness of all outputs confirmed by manual human inspection.
853	
854	Our baseline model, Kimina-Autoformalizer-7B, is used in each strategy: (1) a **Single Pass** baseline (38.0% accuracy); (2) a **Compiler Feedback** loop, where the model regenerates formalizations until they successfully compile (54.0% accuracy); (3) our **CriticLean Pipeline**, which extends this process, regenerating formalizations until they both compile successfully and are validated by our integrated **CriticLeanGPT Model** (84.0% accuracy).
855	
856	While compiler feedback resolves syntactical errors, it fails to detect logical flaws. Our pipeline addresses this gap. The integration of critic model, which performs deeper semantic and logical validation, is directly
857	
858	&lt;table border="1">
859	&lt;thead>
860	&lt;tr>
861	&lt;th>Model&lt;/th>
862	&lt;th>AVG&lt;/th>
863	&lt;/tr>
864	&lt;/thead>
865	&lt;tbody>
866	&lt;tr>
867	&lt;td>Kimina-Autoformalizer-7B&lt;/td>
868	&lt;td>38.0&lt;/td>
869	&lt;/tr>
870	&lt;tr>
871	&lt;td>Kimina-Autoformalizer-7B (Compiler)&lt;/td>
872	&lt;td>54.0&lt;/td>
873	&lt;/tr>
874	&lt;tr>
875	&lt;td>Kimina-Autoformalizer-7B (CriticLean)&lt;/td>
876	&lt;td>84.0&lt;/td>
877	&lt;/tr>
878	&lt;/tbody>
879	&lt;/table>
880	
881	**Table 7** Human evaluation accuracy results for autoformalization performance: The best score is highlighted in *box*.**Figure 8** Math Domain Distributions: FineLeanCorpus vs. Lean-Workbook.
882	
883	&lt;table border="1">
884	&lt;thead>
885	&lt;tr>
886	&lt;th># Attempt&lt;/th>
887	&lt;th>1&lt;/th>
888	&lt;th>5&lt;/th>
889	&lt;th>10&lt;/th>
890	&lt;th>50&lt;/th>
891	&lt;th>100&lt;/th>
892	&lt;th>200&lt;/th>
893	&lt;/tr>
894	&lt;/thead>
895	&lt;tbody>
896	&lt;tr>
897	&lt;td>Count / Ratio&lt;/td>
898	&lt;td>63 / 12.6%&lt;/td>
899	&lt;td>137 / 27.4%&lt;/td>
900	&lt;td>170 / 34.0%&lt;/td>
901	&lt;td>229 / 45.8%&lt;/td>
902	&lt;td>245 / 49.0%&lt;/td>
903	&lt;td>264 / 52.8%&lt;/td>
904	&lt;/tr>
905	&lt;/tbody>
906	&lt;/table>
907	
908	**Table 8 Effectiveness of the Multi-Attempt Strategy on Formalization Yield.** The table shows the cumulative number of successfully formalized problems retained by the critic model as the attempt limit increases. Statistics are from a 500-problem sample.
909	
910	&lt;table border="1">
911	&lt;thead>
912	&lt;tr>
913	&lt;th>Dataset&lt;/th>
914	&lt;th>Accuracy&lt;/th>
915	&lt;th>Dataset&lt;/th>
916	&lt;th>Accuracy&lt;/th>
917	&lt;th>Dataset&lt;/th>
918	&lt;th>Accuracy&lt;/th>
919	&lt;/tr>
920	&lt;/thead>
921	&lt;tbody>
922	&lt;tr>
923	&lt;td>NuminaMath-TIR [24]&lt;/td>
924	&lt;td>78%&lt;/td>
925	&lt;td>IneqMath [20]&lt;/td>
926	&lt;td>96%&lt;/td>
927	&lt;td>BlueMO [73]&lt;/td>
928	&lt;td>86%&lt;/td>
929	&lt;/tr>
930	&lt;tr>
931	&lt;td>DeepMath-103k [16]&lt;/td>
932	&lt;td>84%&lt;/td>
933	&lt;td>DAPO-Math-17k [66]&lt;/td>
934	&lt;td>69%&lt;/td>
935	&lt;td>OnlineMathContest&lt;/td>
936	&lt;td>88%&lt;/td>
937	&lt;/tr>
938	&lt;tr>
939	&lt;td>AOPs [35]&lt;/td>
940	&lt;td>73%&lt;/td>
941	&lt;td>TAL-SCQ5K [37]&lt;/td>
942	&lt;td>75%&lt;/td>
943	&lt;td>Omni-MATH [8]&lt;/td>
944	&lt;td>84%&lt;/td>
945	&lt;/tr>
946	&lt;tr>
947	&lt;td>DeepTheorem [74]&lt;/td>
948	&lt;td>100%&lt;/td>
949	&lt;td>DeepScaleR [34]&lt;/td>
950	&lt;td>100%&lt;/td>
951	&lt;td>&lt;/td>
952	&lt;td>&lt;/td>
953	&lt;/tr>
954	&lt;/tbody>
955	&lt;/table>
956	
957	**Table 9** Human evaluation results of different sources.
958	
959	responsible for the accuracy increase from 54.0% to 84.0%. By filtering out plausible but incorrect formalizations, our method provides a more robust path toward reliable autoformalization. These manually-verified results present strong empirical evidence for the efficacy of our approach.
960	
961	Table 8 shows our pipeline achieved a 52.8% success rate across 500 problems, where success required passing both syntactic validation and our critic model’s semantic check. The value of our multi-attempt strategy is evident: while only 12.6% of samples passed on the first try, the pipeline successfully recovered an additional 40.2% that would be discarded by single-pass systems. Conversely, the 47.2% failure rate within the 200-attempt limit highlights a fundamental bottleneck: the pipeline’s performance is ultimately constrained by the base auto-formalization model’s ability to produce a candidate our critic can approve.
962	
963	Moreover, as shown in Table 9, we also provide the human evaluation results of different sources. We observe that the accuracy varies across different sources, a discrepancy we attribute primarily to the differing domain and difficulty distributions of the respective datasets.&lt;sup>2&lt;/sup>
964	
965	&lt;sup>2&lt;/sup>Our human evaluation standard is particularly stringent. To calibrate our criteria, we inspected a random sample of 50## 7 Conclusion
966	
967	This paper presents CriticLean, a comprehensive framework that positions the critic as a central component in the autoformalization of mathematical statements. Through the development of CriticLeanGPT and the construction of CriticLeanBench, we demonstrate that explicitly modeling and training the critic yields significant improvements in formalization quality. Our pipeline not only refines the translation process through semantic validation, but also enables the construction of FineLeanCorpus, which is validated by both compiler and critic.
968	
969	---
970	
971	entries from the Lean-Workbook, which yielded an accuracy of 84%.## **8 Contributions and Acknowledgments**
972	
973	### **Co-First Authors**
974	
975	Zhongyuan Peng, Yifan Yao, Kaijing Ma
976	
977	### **Co-Authors**
978	
979	Shuyue Guo, Yizhe Li, Yichi Zhang, Chenchen Zhang, Yifan Zhang, Zhouliang Yu, Luming Li, Minghao Liu, Yihang Xia, Jiawei Shen, Yuchen Wu, Yixin Cao, Zhaoxiang Zhang, Wenhao Huang
980	
981	### **Corresponding Authors**
982	
983	Jiaheng Liu, Ge Zhang## References
984	
985	- [1] AI Research Group of TAL Education Group. K-12 handwritten mathematical expressions dataset (hme100k). &lt;https://ai.100tal.com/dataset>. Accessed: 2025-04-05.
986	- [2] Anthropic. Claude 3.5 sonnet model card addendum, 2024. URL &lt;https://www.paperswithcode.com/paper/claude-3-5-sonnet-model-card-addendum>. Accessed: 2024-09-21.
987	- [3] Zhangir Azerbayev, Bartosz Piotrowski, Hailey Schoelkopf, Edward W Ayers, Dragomir Radev, and Jeremy Avigad. Proofnet: Autoformalizing and formally proving undergraduate-level mathematics. [arXiv preprint arXiv:2302.12433](#), 2023.
988	- [4] Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei Huang, Binyuan Hui, Luo Ji, Mei Li, Junyang Lin, Runji Lin, Dayiheng Liu, Gao Liu, Chengqiang Lu, Keming Lu, Jianxin Ma, Rui Men, Xingzhang Ren, Xuancheng Ren, Chuanqi Tan, Sinan Tan, Jianhong Tu, Peng Wang, Shijie Wang, Wei Wang, Shengguang Wu, Benfeng Xu, Jin Xu, An Yang, Hao Yang, Jian Yang, Shusheng Yang, Yang Yao, Bowen Yu, Hongyi Yuan, Zheng Yuan, Jianwei Zhang, Xingxuan Zhang, Yichang Zhang, Zhenru Zhang, Chang Zhou, Jingren Zhou, Xiaohuan Zhou, and Tianhang Zhu. Qwen technical report. [arXiv preprint arXiv:2309.16609](#), 2023.
989	- [5] Konstantin Chernyshev, Vitaliy Polshkov, Ekaterina Artemova, Alex Myasnikov, Vlad Stepanov, Alexei Miasnikov, and Sergei Tilga. U-math: A university-level benchmark for evaluating mathematical skills in llms. [arXiv preprint arXiv:2412.03205](#), 2024.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "240aae25-e7d0-411b-8445-e3a59da92010",
  "isSidechain": false,
  "promptId": "4b0c0804-0c80-4fc4-bd2d-54c91b4a93a7",
  "type": "user",
  "uuid": "6364ac6f-d5ff-49a2-9a8c-6f753841bef4",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu-idea-review/2a30fe45-086a-4752-b69b-cc68f89516e6/tool-results/toolu_016rqZDKmFkzrH3XvWTnogpJ.txt",
      "content": "&lt;/tr>\n&lt;tr>\n&lt;td>OnlineMathContest&lt;/td>\n&lt;td>High School&lt;/td>\n&lt;td>70&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Multi-Source Math Competition&lt;/td>\n&lt;td>High School Olympiad&lt;/td>\n&lt;td>619&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 4** Overview of different sources for FineLeanCorpus.\n\nhigher-performance CriticLeanGPT model. Manual validation indicates that this step is expected to eliminate 74.7% of the remaining incorrect formalizations. The resulting corpus is characterized by its expressive range: natural language statements vary from a concise 9 tokens to a complex 2,980 tokens (avg. 78.4), while their corresponding Lean formalizations span from 14 to 768 tokens (avg. 87.8), reflecting the deep spectrum of complexity successfully captured by our pipeline.\n\nTo further analyze the differences between our FineLeanCorpus dataset and the Lean-Workbook, we employed the templates from Appendix J and Appendix I to assess the difficulty levels and classify the mathematical domains of the datasets using Doubao-1.5-pro [12]. A comparative analysis of our proposed FineLeanCorpus against Lean-Workbook (Figure 7, Figure 8, Table 4 and Table 5) reveals two fundamental advancements: (1) Scale and Coverage: Our corpus provides a significant quantitative expansion in both problem difficulty and domain coverage. This expansion is evident not only across nearly the entire difficulty spectrum—offering a much richer data pool for training foundational skills—but also in the substantial augmentation of high-volume domains like Intermediate Algebra and Elementary Number Theory. (2) FineLeanCorpus exhibits a more diverse and structurally balanced profile, achieved by collecting natural language statements from numerous sources. From a difficulty perspective, it features a multimodal distribution with substantial problem counts at several distinct complexity points, in stark contrast to the unimodal distribution of Lean-Workbook. This characteristic is crucial for mitigating model overfitting to a narrow complexity band. From a domain perspective, it substantially reinforces previously underrepresented areas. For instance, categories such as Analytic Geometry and Integral Calculus are significantly expanded, while niche topics like Algorithms and Graph Theory are also robustly augmented. This targeted enrichment transforms sparsely sampled topics into well-supported, learnable sub-domains, yielding a more comprehensive dataset designed to fosterholistic reasoning capabilities. More details regarding our FineLeanCorpus dataset, including its fine-grained mathematical domain distribution (see Appendix A), are provided for further analysis.\n\nFurthermore, to push the boundaries of current models and foster research into the upper echelons of mathematical reasoning, we have curated a specialized training subset from FineLeanCorpus, which we designate as Diamond. This subset comprises 36,033 problems with a difficulty rating exceeding 5. The purpose of this high-difficulty training set is to create a demanding training environment that fosters the development of the sophisticated, multi-step reasoning required to tackle the most formidable mathematical problems. A detailed breakdown of the mathematical domain distribution within this subset is provided in table 11.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Dataset&lt;/th>\n&lt;th>Source&lt;/th>\n&lt;th>Theorems&lt;/th>\n&lt;th>Level&lt;/th>\n&lt;th>Detailed Critic Process&lt;/th>\n&lt;th>Difficulty Profile&lt;/th>\n&lt;th>Topic Diversity&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Lean-Workbook [65]&lt;/td>\n&lt;td>Synthetic&lt;/td>\n&lt;td>140K&lt;/td>\n&lt;td>Undergraduate&lt;/td>\n&lt;td>Opaque&lt;/td>\n&lt;td>Avg: 3.70&lt;br/>Top-tier (&lt;math>\\geq 6&lt;/math>): 7.81%&lt;/td>\n&lt;td>Highly Skewed&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>FineLeanCorpus (ours)&lt;/td>\n&lt;td>Synthetic&lt;/td>\n&lt;td>285K&lt;/td>\n&lt;td>Diverse&lt;/td>\n&lt;td>Transparent&lt;/td>\n&lt;td>Avg: 3.24&lt;br/>Top-tier (&lt;math>\\geq 6&lt;/math>): 11.10%&lt;/td>\n&lt;td>Balanced &amp; Diverse&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 6** Comparison of dataset statistics. FineLeanCorpus offers a transparent critic process, a higher proportion of top-tier problems, and a more balanced and diverse topic distribution compared to the highly skewed Lean-Workbook.\n\n**Figure 7** Comparison of dataset statistics. FineLeanCorpus offers a transparent critic process, a higher proportion of top-tier problems, and a more balanced and diverse topic distribution compared to the highly skewed Lean-Workbook.\n\n## 6.1 Analysis on CriticLean Pipeline\n\nAs shown in Table 7, our autoformalization pipeline significantly improves accuracy. We selected 50 problems from the Omni-MATH and applied the following three formalization strategies, with the correctness of all outputs confirmed by manual human inspection.\n\nOur baseline model, Kimina-Autoformalizer-7B, is used in each strategy: (1) a **Single Pass** baseline (38.0% accuracy); (2) a **Compiler Feedback** loop, where the model regenerates formalizations until they successfully compile (54.0% accuracy); (3) our **CriticLean Pipeline**, which extends this process, regenerating formalizations until they both compile successfully and are validated by our integrated **CriticLeanGPT Model** (84.0% accuracy).\n\nWhile compiler feedback resolves syntactical errors, it fails to detect logical flaws. Our pipeline addresses this gap. The integration of critic model, which performs deeper semantic and logical validation, is directly\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Model&lt;/th>\n&lt;th>AVG&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Kimina-Autoformalizer-7B&lt;/td>\n&lt;td>38.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Kimina-Autoformalizer-7B (Compiler)&lt;/td>\n&lt;td>54.0&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>Kimina-Autoformalizer-7B (CriticLean)&lt;/td>\n&lt;td>84.0&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 7** Human evaluation accuracy results for autoformalization performance: The best score is highlighted in *box*.**Figure 8** Math Domain Distributions: FineLeanCorpus vs. Lean-Workbook.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th># Attempt&lt;/th>\n&lt;th>1&lt;/th>\n&lt;th>5&lt;/th>\n&lt;th>10&lt;/th>\n&lt;th>50&lt;/th>\n&lt;th>100&lt;/th>\n&lt;th>200&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>Count / Ratio&lt;/td>\n&lt;td>63 / 12.6%&lt;/td>\n&lt;td>137 / 27.4%&lt;/td>\n&lt;td>170 / 34.0%&lt;/td>\n&lt;td>229 / 45.8%&lt;/td>\n&lt;td>245 / 49.0%&lt;/td>\n&lt;td>264 / 52.8%&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 8 Effectiveness of the Multi-Attempt Strategy on Formalization Yield.** The table shows the cumulative number of successfully formalized problems retained by the critic model as the attempt limit increases. Statistics are from a 500-problem sample.\n\n&lt;table border=\"1\">\n&lt;thead>\n&lt;tr>\n&lt;th>Dataset&lt;/th>\n&lt;th>Accuracy&lt;/th>\n&lt;th>Dataset&lt;/th>\n&lt;th>Accuracy&lt;/th>\n&lt;th>Dataset&lt;/th>\n&lt;th>Accuracy&lt;/th>\n&lt;/tr>\n&lt;/thead>\n&lt;tbody>\n&lt;tr>\n&lt;td>NuminaMath-TIR [24]&lt;/td>\n&lt;td>78%&lt;/td>\n&lt;td>IneqMath [20]&lt;/td>\n&lt;td>96%&lt;/td>\n&lt;td>BlueMO [73]&lt;/td>\n&lt;td>86%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepMath-103k [16]&lt;/td>\n&lt;td>84%&lt;/td>\n&lt;td>DAPO-Math-17k [66]&lt;/td>\n&lt;td>69%&lt;/td>\n&lt;td>OnlineMathContest&lt;/td>\n&lt;td>88%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>AOPs [35]&lt;/td>\n&lt;td>73%&lt;/td>\n&lt;td>TAL-SCQ5K [37]&lt;/td>\n&lt;td>75%&lt;/td>\n&lt;td>Omni-MATH [8]&lt;/td>\n&lt;td>84%&lt;/td>\n&lt;/tr>\n&lt;tr>\n&lt;td>DeepTheorem [74]&lt;/td>\n&lt;td>100%&lt;/td>\n&lt;td>DeepScaleR [34]&lt;/td>\n&lt;td>100%&lt;/td>\n&lt;td>&lt;/td>\n&lt;td>&lt;/td>\n&lt;/tr>\n&lt;/tbody>\n&lt;/table>\n\n**Table 9** Human evaluation results of different sources.\n\nresponsible for the accuracy increase from 54.0% to 84.0%. By filtering out plausible but incorrect formalizations, our method provides a more robust path toward reliable autoformalization. These manually-verified results present strong empirical evidence for the efficacy of our approach.\n\nTable 8 shows our pipeline achieved a 52.8% success rate across 500 problems, where success required passing both syntactic validation and our critic model’s semantic check. The value of our multi-attempt strategy is evident: while only 12.6% of samples passed on the first try, the pipeline successfully recovered an additional 40.2% that would be discarded by single-pass systems. Conversely, the 47.2% failure rate within the 200-attempt limit highlights a fundamental bottleneck: the pipeline’s performance is ultimately constrained by the base auto-formalization model’s ability to produce a candidate our critic can approve.\n\nMoreover, as shown in Table 9, we also provide the human evaluation results of different sources. We observe that the accuracy varies across different sources, a discrepancy we attribute primarily to the differing domain and difficulty distributions of the respective datasets.&lt;sup>2&lt;/sup>\n\n&lt;sup>2&lt;/sup>Our human evaluation standard is particularly stringent. To calibrate our criteria, we inspected a random sample of 50## 7 Conclusion\n\nThis paper presents CriticLean, a comprehensive framework that positions the critic as a central component in the autoformalization of mathematical statements. Through the development of CriticLeanGPT and the construction of CriticLeanBench, we demonstrate that explicitly modeling and training the critic yields significant improvements in formalization quality. Our pipeline not only refines the translation process through semantic validation, but also enables the construction of FineLeanCorpus, which is validated by both compiler and critic.\n\n---\n\nentries from the Lean-Workbook, which yielded an accuracy of 84%.## **8 Contributions and Acknowledgments**\n\n### **Co-First Authors**\n\nZhongyuan Peng, Yifan Yao, Kaijing Ma\n\n### **Co-Authors**\n\nShuyue Guo, Yizhe Li, Yichi Zhang, Chenchen Zhang, Yifan Zhang, Zhouliang Yu, Luming Li, Minghao Liu, Yihang Xia, Jiawei Shen, Yuchen Wu, Yixin Cao, Zhaoxiang Zhang, Wenhao Huang\n\n### **Corresponding Authors**\n\nJiaheng Liu, Ge Zhang## References\n\n- [1] AI Research Group of TAL Education Group. K-12 handwritten mathematical expressions dataset (hme100k). &lt;https://ai.100tal.com/dataset>. Accessed: 2025-04-05.\n- [2] Anthropic. Claude 3.5 sonnet model card addendum, 2024. URL &lt;https://www.paperswithcode.com/paper/claude-3-5-sonnet-model-card-addendum>. Accessed: 2024-09-21.\n- [3] Zhangir Azerbayev, Bartosz Piotrowski, Hailey Schoelkopf, Edward W Ayers, Dragomir Radev, and Jeremy Avigad. Proofnet: Autoformalizing and formally proving undergraduate-level mathematics. [arXiv preprint arXiv:2302.12433](#), 2023.\n- [4] Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan, Wenbin Ge, Yu Han, Fei Huang, Binyuan Hui, Luo Ji, Mei Li, Junyang Lin, Runji Lin, Dayiheng Liu, Gao Liu, Chengqiang Lu, Keming Lu, Jianxin Ma, Rui Men, Xingzhang Ren, Xuancheng Ren, Chuanqi Tan, Sinan Tan, Jianhong Tu, Peng Wang, Shijie Wang, Wei Wang, Shengguang Wu, Benfeng Xu, Jin Xu, An Yang, Hao Yang, Jian Yang, Shusheng Yang, Yang Yao, Bowen Yu, Hongyi Yuan, Zheng Yuan, Jianwei Zhang, Xingxuan Zhang, Yichang Zhang, Zhenru Zhang, Chang Zhou, Jingren Zhou, Xiaohuan Zhou, and Tianhang Zhu. Qwen technical report. [arXiv preprint arXiv:2309.16609](#), 2023.\n- [5] Konstantin Chernyshev, Vitaliy Polshkov, Ekaterina Artemova, Alex Myasnikov, Vlad Stepanov, Alexei Miasnikov, and Sergei Tilga. U-math: A university-level benchmark for evaluating mathematical skills in llms. [arXiv preprint arXiv:2412.03205](#), 2024.",
      "numLines": 200,
      "startLine": 790,
      "totalLines": 1768
    }
  },
  "sourceToolAssistantUUID": "240aae25-e7d0-411b-8445-e3a59da92010",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 79 · 2026-05-27T18:19:45.811Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me summarize the key findings:

**DDRL (arxiv:2604.21327):**
- Best improvement: +19.0% relative on AIME 2024 (Qwen2.5-Math-1.5B: 15.8→25.0 vs ETMR)
- NOT 58.2% — that number doesn't appear anywhere in the paper
- Other improvements: +4.1% AMC, +4.9% MATH-500 for same model
- Llama-3.1-8B: +9.0% AMC, +13.6% MATH-500


- Uses a consensus-based off-policy refinement stage as its third component

**CriticLean:**
- The Qwen3 variants show strong performance on CriticLeanBench: 79.8% for the 8B model, 84.8% for 14B, and 87.0% for 32B
- The pipeline achieves 38.0% accuracy with a single pass, improving with compiler feedback to 54.0%, and reaching 84.0% with the full CriticLean pipeline

**DRIFT (ICLR 2026):**
- DRIFT with GPT-4.1 achieves 62.33% BEq+@10 on Con-NF, outperforming Oracle* at 58.90%, while DPR trails significantly at 20.08%
- The key insight is that Oracle* only provides necessary premises, whereas DRIFT's illustrative theorems demonstrate how premises are actually used
- However, on ProofNet the results flip—Oracle* reaches 27.54% while DRIFT only gets 21.93%, so DRIFT doesn't consistently outperform across all benchmarks

**MathAtlas (arxiv:2605.14061):**
- This dataset contains around 52K problems with 178K dependency relations across 103 textbooks, with the hardest subset (MA-Hard) having only 700 entities where the best model achieves just 2.6% correctness
- Performance on the full dataset maxes out at 9.8% for theorems and 16.7% for definitions, with dependency depth averaging 30 (median 17, ranging up to 80) across 87 mathematical fields
- There's a clear performance degradation as dependency depth increases (statistically significant at p<0.001), and interestingly, adding 500 tokens of local context actually made things worse rather than better

Now I'm noticing a discrepancy with the DDRL numbers—the 58.2% improvement appears to be fabricated, and I need to identify what the actual best improvement is.

The real DDRL improvement on AIME 2024 is 19.0% relative gain, and I should also clarify that DDRL has a third component involving consensus-based off-policy refinement. For CriticLeanBench, there's a model size distinction: the 32B-RL variant achieves 87.0% while the 14B-RL achieves 84.8%, so since we're using the 14B model in our approach, I should consistently reference 84.8% rather than the higher 32B number.

Now I need to address several remaining issues. The curriculum transition criteria need quantitative thresholds defined. For the BEq degeneracy problem, I should implement a fallback mechanism using compiled reward times critic reward when few candidates compile. On the DRIFT comparison, the key reframing is that DRIFT doesn't actually exceed our oracle on ProofNet—it's 21.93% versus our 27.54%—and DRIFT's static nature means it can't adapt as the model's capabilities evolve during training, whereas our approach handles both decomposable and simpler statements more flexibly.

Looking at the broader picture, MathAtlas provides valuable evidence that naive retrieval actually hurts performance in prompted systems, which reinforces that the bottleneck isn't just retrieval itself but model-adaptive retrieval. The core assumption that retrieval is a bottleneck still holds because DRIFT doesn't exceed oracle on ProofNet, MathAtlas demonstrates performance degradation with naive approaches, and DRIFT's reliance on expensive models like GPT-4.1 highlights why a more efficient, adaptive strategy matters.

The key distinction I'm making is that this isn't about static versus oracle retrieval—it's about static versus adaptive retrieval. DRIFT shows decomposition-based retrieval can match or exceed oracle on certain benchmarks, but it's fundamentally a fixed pipeline that can't evolve with the model. During TTRL, as formalization improves, better attempts reveal missing dependencies, creating a feedback loop that static retrieval can't capture. MathAtlas demonstrates this limitation empirically.

Now I'm thinking through concrete transition criteria for the curriculum stages. For moving from warm-start to retrieval bootstrapping, I need compilation rate above 40%, critic agreement around 60% on compilable outputs, and at least 3 absolute points of BEq@K improvement. Then for bootstrapping to far-OOD adaptation, I'm looking at retrieval recall of 30% on bootstrapped queries, 25% compilation on moderate-OOD domains, and 50% critic agreement in those domains.

For handling BEq degeneracy when few candidates compile, I'm implementing a fallback that drops the BEq term entirely when there are fewer than 4 compilable outputs out of 32 candidates — this keeps the reward signal clean and principled rather than noisy. The MathAtlas data showing average dependency depth around 30 and ranging up to 80 really validates why dependency-aware retrieval matters at scale.

I should also verify the DDRL components more carefully — it's actually three pieces: frequency-balanced sampling, debiased advantage estimation with fixed advantages, and consensus-based off-policy refinement, so I need to make sure I'm incorporating all three rather than just the first two.

Looking at the ablation results, the off-policy refinement component delivers the biggest single jump — going from 47.0% to 52.9% when added to the other two components — so that's definitely worth highlighting. On AIME 2024, the improvement from 15.8% to 25.0% is a 58.2% relative gain, though I'm seeing some discrepancy with what the reviewer cited as 19.0%. The 58.2% improvement I calculated is actually DDRL over TTRL, but the paper doesn't report this number—it only compares DDRL to ETMR with a +19.0% gain. I need to figure out what ETMR is and why the paper uses that as the baseline instead of TTRL. I see the confusion now—the paper reports a 19.0% improvement versus ETMR as their main baseline, while the 9.2 absolute point gain (25.0 - 15.8) comes from comparing DDRL to vanilla TTRL. The reviewer is correctly distinguishing between these two metrics: the relative improvement the paper highlights versus the absolute performance gain on the benchmark. I need to figure out what ETMR is and how the 19.0% improvement is calculated. The reviewer confirms the paper reports 19.0% as the best improvement on AIME 2024, with absolute scores going from 15.8 to 25.0 (a 9.2 percentage point gain), but I'm still unclear whether 19.0% is relative improvement versus ETMR or some other baseline. ETMR is likely a specific baseline method for test-time math reasoning, and the paper's reported 19.0% improvement is relative to that approach, not TTRL. The key takeaway is that DDRL achieves 25.0 on AIME 2024 with a 9.2 absolute point gain, and I should stick with the paper's reported 19.0% figure rather than computing my own 58.2% relative improvement against TTRL.

Now I'm reconsidering whether DRIFT exceeding oracle performance actually undermines our approach. It doesn't—DRIFT only surpasses oracle on Con-NF, not ProofNet, so the gap isn't universally closed. More importantly, DRIFT's advantage comes from providing illustrative theorems that show how premises are used, which complements adaptive retrieval rather than replacing it. The real insight is that static retrieval strategies like DRIFT can outperform oracle performance when they include usage demonstrations, but our approach could potentially do better by adapting the retrieval strategy dynamically. Now I'm putting together the complete revised proposal, making sure to fix the factual inaccuracies, clarify the curriculum progression, handle the BEq degeneracy issue, and incorporate MathAtlas as a key motivation point.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6364ac6f-d5ff-49a2-9a8c-6f753841bef4",
  "isSidechain": false,
  "requestId": "req_011CbTXtn2BTVAsNgvWeUXob",
  "type": "assistant",
  "uuid": "7bec5551-f1b1-428b-894d-536f98f7185c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HN4eF2UWTjsHePJc6KkR3c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4151,
      "cache_read_input_tokens": 47536,
      "output_tokens": 4769,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4151,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4769,
          "cache_read_input_tokens": 47536,
          "cache_creation_input_tokens": 4151,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4151
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

_source line 80 · 2026-05-27T18:19:45.813Z_

Now I have all the data I need. Let me also verify the DDRL improvement calculation to understand the discrepancy.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bec5551-f1b1-428b-894d-536f98f7185c",
  "isSidechain": false,
  "requestId": "req_011CbTXtn2BTVAsNgvWeUXob",
  "type": "assistant",
  "uuid": "1c15fdd7-606c-430f-9e91-48045987ba3e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HN4eF2UWTjsHePJc6KkR3c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4151,
      "cache_read_input_tokens": 47536,
      "output_tokens": 4769,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4151,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4769,
          "cache_read_input_tokens": 47536,
          "cache_creation_input_tokens": 4151,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4151
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

_source line 81 · 2026-05-27T18:19:48.358Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GgHaVBpMc1ZKxJ9ApgW2of`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.21327",
  "prompt": "I need to understand what ETMR is in this paper and how the improvement percentages are computed. Specifically: 1) What does ETMR stand for? Is it a specific baseline method? 2) How is the +19.0% on AIME 2024 computed — is it relative to ETMR or to vanilla TTRL? 3) What are ALL the baselines compared against (TTRL, ETMR, others)? 4) What is the ETMR score on AIME 2024 for Qwen2.5-Math-1.5B? 5) Also extract any information about the consensus-based off-policy refinement component — what exactly is it?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c15fdd7-606c-430f-9e91-48045987ba3e",
  "isSidechain": false,
  "requestId": "req_011CbTXtn2BTVAsNgvWeUXob",
  "type": "assistant",
  "uuid": "e10f3f2a-abc3-439f-8f9b-7f071e67454c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HN4eF2UWTjsHePJc6KkR3c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4151,
      "cache_read_input_tokens": 47536,
      "output_tokens": 4769,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4151,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4769,
          "cache_read_input_tokens": 47536,
          "cache_creation_input_tokens": 4151,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4151
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

_source line 82_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Aut…",
  "leafUuid": "e10f3f2a-abc3-439f-8f9b-7f071e67454c",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6"
}
```

---

### Runtime record

_source line 83_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise autoformalization TTRL paper with verified data and concrete curriculum",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6"
}
```

---

### Tool result

_source line 84 · 2026-05-27T18:19:53.315Z_

<details><summary>↩ Tool result · `toolu_01GgHaVBpMc1ZKxJ9ApgW2of`</summary>

```text
# Analysis of ETMR and DDRL Improvements

## 1. What is ETMR?

ETMR stands for "Entropy-Fork Tree Majority Rollout" (also referenced as ETTRL in citations). According to the paper, it's a baseline method that "improves rollout diversity by selectively forking trajectories at high-entropy tokens."

## 2. How Are Improvement Percentages Computed?

The +19.0% improvement on AIME 2024 is **relative to ETMR**, not vanilla TTRL. The paper states: "Δ represents the percentage performance gain achieved by our method compared to ETMR."

## 3. All Baselines Compared

The paper compares against three categories:
- **No Adaptation** (baseline pretrained models)
- **TTRL** (Zuo et al., 2025) - the foundational unsupervised RL approach
- **ETMR** (Liu et al., 2025) - the strongest baseline with entropy-based improvements

## 4. ETMR Score on AIME 2024 for Qwen2.5-Math-1.5B

ETMR achieved **21.0** on AIME 2024. DDRL scored 25.0, yielding the +19.0% relative improvement (calculated as (25.0-21.0)/21.0 ≈ 0.190).

## 5. Consensus-Based Off-Policy Refinement

This component operates after the RL phase. The process involves: sampling 128 responses per query, obtaining a consensus pseudo-label via majority voting, and applying rejection sampling to retain only responses matching consensus. These high-confidence samples then undergo supervised fine-tuning for stable model refinement.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e10f3f2a-abc3-439f-8f9b-7f071e67454c",
  "isSidechain": false,
  "promptId": "4b0c0804-0c80-4fc4-bd2d-54c91b4a93a7",
  "type": "user",
  "uuid": "a4503fea-71f6-400c-9245-190b151a69c9",
  "toolUseResult": {
    "bytes": 242042,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of ETMR and DDRL Improvements\n\n## 1. What is ETMR?\n\nETMR stands for \"Entropy-Fork Tree Majority Rollout\" (also referenced as ETTRL in citations). According to the paper, it's a baseline method that \"improves rollout diversity by selectively forking trajectories at high-entropy tokens.\"\n\n## 2. How Are Improvement Percentages Computed?\n\nThe +19.0% improvement on AIME 2024 is **relative to ETMR**, not vanilla TTRL. The paper states: \"Δ represents the percentage performance gain achieved by our method compared to ETMR.\"\n\n## 3. All Baselines Compared\n\nThe paper compares against three categories:\n- **No Adaptation** (baseline pretrained models)\n- **TTRL** (Zuo et al., 2025) - the foundational unsupervised RL approach\n- **ETMR** (Liu et al., 2025) - the strongest baseline with entropy-based improvements\n\n## 4. ETMR Score on AIME 2024 for Qwen2.5-Math-1.5B\n\nETMR achieved **21.0** on AIME 2024. DDRL scored 25.0, yielding the +19.0% relative improvement (calculated as (25.0-21.0)/21.0 ≈ 0.190).\n\n## 5. Consensus-Based Off-Policy Refinement\n\nThis component operates after the RL phase. The process involves: sampling 128 responses per query, obtaining a consensus pseudo-label via majority voting, and applying rejection sampling to retain only responses matching consensus. These high-confidence samples then undergo supervised fine-tuning for stable model refinement.",
    "durationMs": 4949,
    "url": "https://arxiv.org/html/2604.21327"
  },
  "sourceToolAssistantUUID": "e10f3f2a-abc3-439f-8f9b-7f071e67454c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 85 · 2026-05-27T18:20:12.765Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full picture:

**DDRL improvements:**
- ETMR = "Entropy-Fork Tree Majority Rollout" — the strongest baseline
- DDRL: 25.0 on AIME 2024 vs ETMR: 21.0 → (25.0-21.0)/21.0 = 19.0% relative improvement
- DDRL vs vanilla TTRL: 25.0 vs 15.8 → 9.2 absolute pp gain, or (25.0-15.8)/15.8 = 58.2% relative (BUT this is NOT reported in the paper)


- The 58.2% improvement over vanilla TTRL is mathematically correct but not what the paper emphasizes — they report the 19.0% gain over ETMR, the strongest prior method, which is the fairer comparison. The third component involves consensus-based off-policy refinement using rejection sampling and SFT.

Now I'm pulling together the revised proposal with corrected numbers: DDRL achieves 25.0 on AIME 2024 versus ETMR's 21.0 (a 19.0% relative improvement), and I need to clarify the CriticLeanBench numbers — 84.8% for the 14B-RL model we're actually deploying, with 87.0% as the best overall result from the 32B-RL variant.

I'm also defining the quantitative thresholds for curriculum transitions: moving from stage (a) to (b) requires hitting 40% compilation rate, 60% critic approval among compilable candidates, and at least 3 percentage points of BEq improvement; advancing to stage (c) needs 30% retrieval recall on bootstrapped queries and 25% compilation on moderate out-of-distribution cases.

For the BEq degeneracy issue, I'm implementing a fallback mechanism that switches to the simpler reward formulation when fewer than 4 candidates compile out of 32, treating this as an adaptive tier rather than a failure mode.

On DRIFT, I need to reframe the narrative: while it does beat the oracle on Con-NF, it actually underperforms on ProofNet, so the real insight isn't about closing a static retrieval gap but about making retrieval co-adaptive with the model's weight updates—static retrieval can't evolve with the model's improving capabilities, and MathAtlas demonstrates that naive context addition actually hurts performance.

I'm adding MathAtlas as an evaluation benchmark with its 52K problems, 178K dependencies across 103 textbooks, and noting how performance degrades with depth and the MA-Hard subset represents only 2.6% of the dataset.

Writing the revised JSON...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4503fea-71f6-400c-9245-190b151a69c9",
  "isSidechain": false,
  "requestId": "req_011CbTY2VdujpNwBXQqr5sbA",
  "type": "assistant",
  "uuid": "15c4ba1f-c07d-443b-82f8-6143f5f4d3ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011STzMQ9y7BXBfihwmUZEof",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5192,
      "cache_read_input_tokens": 51687,
      "output_tokens": 9414,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5192,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9414,
          "cache_read_input_tokens": 51687,
          "cache_creation_input_tokens": 5192,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5192
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

_source line 86 · 2026-05-27T18:23:23.849Z_

Now I have all the verified facts. Let me synthesize everything and produce the revised proposal.

**Key findings from research:**

1. **DDRL numbers**: The 58.2% was actually DDRL/TTRL relative gain (25.0-15.8)/15.8, but it's NOT a number the paper reports. The paper reports +19.0% vs ETMR (the strongest baseline, scoring 21.0). DDRL also has a third component: consensus-based off-policy refinement.

2. **CriticLeanBench**: CriticLeanGPT-Qwen3-14B-RL = **84.8%**, CriticLeanGPT-Qwen3-32B-RL = **87.0%**. The 87% is the 32B model, the 84.8% is the 14B model we use. Pipeline: 38%→54%→84%.

3. **DRIFT**: Exceeds oracle on Con-NF (62.33% vs 58.90%) but NOT on ProofNet (21.93% vs 27.54%). DRIFT's own paper notes retrieval "depends heavily on model-specific knowledge boundaries" and can "act as a distractor."

4. **MathAtlas**: 52K problems, 178K deps, 103 textbooks, avg depth 30. Best model gets 2.6% on MA-Hard. Adding local context actually DEGRADED performance for prompted systems.

Now let me produce the complete revised JSON:

```json
{
  "title": "Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Autoformalization",
  "core_problem": "Current autoformalization models—even those achieving strong in-distribution results (ATF: 94.51% Pass@1 on FormalMath-Lite; ATLAS: 96.93% pass@128 on miniF2F)—degrade sharply on unfamiliar mathematical domains because they lack both domain-specific Mathlib knowledge and mechanisms to adapt at deployment time. Meanwhile, test-time RL (TTRL) has been shown to boost informal math reasoning dramatically but cannot be naively applied to autoformalization: majority voting over formal statements is ill-defined (unlike numerical answers), and GRPO's advantage normalization amplifies noise from ambiguous pseudo-labels. Can we make TTRL viable for autoformalization by combining a trained semantic critic, co-adaptive retrieval that evolves with the model during adaptation, debiased advantage estimation, and progressive domain curriculum?",
  "opportunity": "Three independently validated capabilities have never been combined: (1) Dependency-aware retrieval is critical—but static retrieval has fundamental limits. DRIFT (ICLR 2026) shows that decomposition-based retrieval can match or exceed oracle performance on specific benchmarks (62.33% vs Oracle* 58.90% BEq+@10 on Con-NF with GPT-4.1), yet still falls short on others (21.93% vs 27.54% on ProofNet) and its own authors note effectiveness 'depends heavily on model-specific knowledge boundaries.' MathAtlas (May 2026) demonstrates that naive context addition actually degrades performance for prompted systems, and that model accuracy drops precipitously with dependency depth (avg depth 30, best model 2.6% on MA-Hard). What is missing is retrieval that co-adapts with the model's evolving capabilities—something no static pipeline can provide. (2) TTRL has boosted informal math reasoning substantially (Qwen-2.5-Math-7B on AIME 2024, NeurIPS 2025), and DDRL's debiased advantage estimation (ACL 2026) fixes spurious signal amplification, achieving up to 19.0% relative improvement over the strongest baseline (ETMR) on AIME 2024, with a 9.2 absolute point gain (15.8→25.0) for Qwen2.5-Math-1.5B. (3) CriticLean (July 2025) demonstrates that a trained semantic critic raises autoformalization accuracy from 54% to 84% compared to compilation-only feedback, with CriticLeanGPT-Qwen3-32B-RL achieving 87.0% accuracy on CriticLeanBench, providing the reliable reward signal needed to make RL-based autoformalization work in low-label regimes. Existing strong baselines—ATF's tool-augmented iterative refinement (65.38% Pass@1 on CombiBench) and Monotonic Refinement's multi-model orchestration (90.27% overall on miniF2F)—achieve impressive results but cannot adapt model weights to new domains. Recent infrastructure (DDR's 500K-sample dependency dataset, CRAMF's 26K Mathlib concept index, FormalMATH's multi-domain benchmark, MathAtlas's 52K graduate-level problems with 178K dependency relations, Kimina Lean Server for high-throughput verification, open-source CriticLeanGPT models) makes a critic-guided TTRL approach newly feasible.",
  "landscape": "TTRL (NeurIPS 2025) demonstrated test-time RL for informal math using majority-voting pseudo-labels. DDRL (ACL 2026 Findings) identified that GRPO's group-relative advantage normalization causes spurious signal amplification from ambiguous pseudo-labels, proposing a three-component fix: (1) frequency-based balanced sampling to exclude ambiguous samples, (2) fixed ±1 advantages replacing GRPO's normalized advantages, and (3) consensus-based off-policy refinement using rejection sampling for stable model updates—yielding up to 19.0% relative improvement over the strongest baseline (ETMR) on AIME 2024 (Qwen2.5-Math-1.5B: 15.8→25.0, 9.2pp absolute gain). Concurrent work on TTRL debiasing includes T³RL (tool-based verification), DCRL (dual consensus), DARE (distribution-aware reward estimation), and ECHO (entropy-confidence hybrid optimization). AlphaProof (Nature 2025) applies test-time RL to formal proving via variant generation. Kimina-Prover (April 2025) internalizes search via RL for Lean proving, achieving 80.7% pass@8192 on miniF2F. FormaRL (COLM 2025) applies GRPO-based RL to autoformalization using compilation + LLM consistency rewards, improving pass@1 from 4% to 26% on ProofNet. CriticLean (July 2025) introduces a trained semantic critic (CriticLeanGPT) for autoformalization quality evaluation—achieving 87.0% accuracy on CriticLeanBench (32B-RL variant; 84.8% for 14B-RL) and raising pipeline accuracy from 54% to 84% over compilation-only feedback—with open-source models from 8B to 32B parameters. ATLAS (NeurIPS 2025) builds a 300K synthetic NL-FL dataset via iterative augmentation, achieving 96.93% pass@128 and 70.08% pass@1 on miniF2F, demonstrating that high-k sampling nearly solves in-distribution benchmarks but pass@1 remains challenging. ATF/Autoformalizer with Tool Feedback (arXiv 2025) achieves 94.51% Pass@1 on FormalMath-Lite and 65.38% on CombiBench using SFT + expert iteration + DPO with multi-LLM consistency checking—representing the state-of-the-art in iterative refinement without RL weight updates. Monotonic Reference-Free Refinement (January 2026) achieves 100% formal validity and 90.27% composite score on miniF2F through multi-model ensemble orchestration with certified monotonic improvement, but requires 6+ models including GPT-4.1-mini as a judge. DDR (December 2025) builds a 500K-sample dependency retrieval dataset with suffix-array verification. DRIFT (ICLR 2026) decomposes informal statements for targeted retrieval, achieving 62.33% BEq+@10 on Con-NF with GPT-4.1—actually surpassing Oracle* retrieval (58.90%)—by providing illustrative theorems that demonstrate premise usage beyond mere definition retrieval. However, DRIFT still falls short of oracle on ProofNet (21.93% vs 27.54%), and its authors note that retrieval effectiveness 'depends heavily on model-specific knowledge boundaries' and can 'act as a distractor rather than an aid' on simpler problems. CRAMF (2025) indexes 26K+ Mathlib definitions for concept-level retrieval, yielding up to 62.1% relative improvement. Aria (ICLR 2026) uses agentic Graph-of-Thought with dependency decomposition, achieving 68.5% accuracy on ProofNet. ProofBridge (ICLR 2026) combines contrastive joint embeddings with retrieval-augmented fine-tuning for proof autoformalization (+31.14% semantic correctness). ReForm (2026) applies position-aware RL rewards for reflective autoformalization (+22.6pp average). StepFun-Formalizer-32B achieves 40.5% BEq@1 SOTA on FormalMath-Lite via BEq-based majority voting for data curation. FormalEvolve (March 2026) frames autoformalization as test-time neuro-symbolic evolutionary search but without RL. MathAtlas (May 2026) introduces 52K graduate-level problems from 103 textbooks with 178K dependency relations and average dependency depth of 30—where the best model achieves only 2.6% correctness on MA-Hard and adding local context actually degrades prompted systems' performance, demonstrating that naive retrieval fails at scale and adaptive dependency handling is essential. After exhaustive search through May 2026, no work combines (a) co-adaptive retrieval that evolves with the model during test-time training, (b) a trained semantic critic for reward computation, and (c) debiased test-time RL adaptation for autoformalization: existing retrieval methods (DDR, DRIFT, CRAMF, Aria) are static pipelines without RL; existing RL methods (FormaRL, ReForm) assume fixed-domain training without retrieval or semantic critic rewards; ATF and Monotonic Refinement use iterative inference without weight updates; existing TTRL applications (AlphaProof, Kimina-Prover) target proof search; and CriticLean provides the critic but not the RL adaptation loop.",
  "inspired_by": "Field guide untried combination: 'Dependency-aware TTRL with semantic critic reward: Combine RAutoformalizer's dependency retrieval + CriticLean's semantic critic + DDRL's debiased advantage estimation + AlphaProof's Test-Time Reinforcement Learning.' Also: gap 'Dependency-aware autoformalization: models are context-blind to formal library contents' + gap 'Pseudo-reward design for formal statement agreement is ill-defined without a trained critic' + pattern 'Test-Time Compute Scaling via Problem-Specific Adaptation' + pattern 'Debiased RL for noisy reward environments.' + insight 'DRIFT shows static retrieval can match oracle but cannot adapt to evolving model capabilities' + insight 'MathAtlas shows naive context injection degrades performance, demanding adaptive retrieval.'",
  "approach": "We propose TTRA (Test-Time Retrieval-Augmented autoformalization), a three-phase framework that makes TTRL viable for autoformalization through a multi-tier adaptive reward mechanism, debiased advantage estimation, and progressive domain curriculum with quantitative transition criteria.\n\n**Phase 1 — Base Formalizer and Critic Training.** Fine-tune a Qwen3-8B base model as a retrieval-augmented autoformalizer using DDR's 500K-sample dependency dataset and FormaRL's GRPO pipeline with a multi-tier reward function R(y, x) = r_compile × (α·r_critic + β·r_beq), where: r_compile ∈ {0,1} is the Lean 4 compilation gate (verified via Kimina Lean Server with 128 parallel pre-warmed REPL workers and LRU header caching); r_critic ∈ {0,1} is the semantic fidelity judgment from CriticLeanGPT-Qwen3-14B-RL (the open-source critic from CriticLean, achieving 84.8% accuracy on CriticLeanBench); r_beq ∈ [0,1] is the BEq consensus density (fraction of compilable candidates in the same BEq equivalence class, computed via Lean's exact? tactic for bidirectional implication). We set α=0.7, β=0.3 to weight semantic fidelity over syntactic consensus, since BEq has high precision (98.6%) but low recall (~33% on ProofNet). **Adaptive reward degradation:** When fewer than M=4 candidates out of K=32 compile successfully (common on hard OOD domains), BEq consensus density becomes degenerate (trivially 0 or 1), so we fall back to R = r_compile × r_critic, dropping the BEq term entirely. This provides a principled reward signal even on the hardest problems where compilation rates are very low.\n\n**Phase 2 — Co-Adaptive Retrieval Module.** Build a domain-adaptive retrieval module that generates candidate Mathlib dependencies via DDR's suffix-array verification and injects retrieved formal definitions into the autoformalization prompt. Train the retriever on DDR's dataset and augment with CRAMF-style concept-level retrieval for broader coverage. Critically, unlike static retrieval pipelines (DRIFT, DDR, CRAMF), our retrieval module co-evolves with the formalizer during TTRL: as the model's formalization attempts improve through adaptation, they produce more informative retrieval queries that expose which specific dependencies are missing. DRIFT (ICLR 2026) demonstrates that sophisticated static retrieval can match or exceed oracle performance on certain benchmarks (62.33% vs 58.90% BEq+@10 on Con-NF) through decomposition and illustrative examples—but this pipeline is frozen, unable to capitalize on the model's evolving knowledge during test-time training. MathAtlas further shows that naive context addition actually degrades prompted systems' performance, underscoring that retrieval quality (not quantity) is paramount and must adapt to the model's current capabilities.\n\n**Phase 3 — Progressive Domain Curriculum for Test-Time Adaptation with Quantitative Transition Criteria.** This directly addresses the bootstrapping problem: if retrieval is poor on the target domain, formalizations are wrong, rewards are noisy, and TTRL fails. We break this cycle through a three-stage curriculum with explicit, reproducible transition criteria:\n\n  (a) Near-distribution warm-start: Apply TTRL on domains close to training data (e.g., elementary number theory, basic algebra) where retrieval coverage is high and the critic is reliable. Generate K=32 formalization candidates per problem, compute multi-tier rewards, and perform debiased GRPO updates following DDRL's three-component fix: (1) frequency-based balanced sampling to exclude ambiguous candidates, (2) fixed +1/-1 advantages replacing GRPO's normalized advantages (severing the amplification pathway where dividing by small std inflates gradients for ambiguous groups), and (3) consensus-based off-policy refinement using rejection sampling on high-confidence samples for stable model updates.\n  **Transition criterion (a)→(b):** Advance when all three conditions are met on the current domain batch: (i) compilation rate ≥ 40% (model produces structurally viable formalizations), (ii) critic approval rate ≥ 60% among compilable candidates (semantic fidelity is above random), and (iii) BEq@32 improves ≥ 3 absolute points over the pre-adaptation baseline (confirming TTRL is providing meaningful signal). If after T_max=500 GRPO steps these thresholds are not met, the domain is flagged as too difficult for warm-start and reclassified to stage (c).\n  (b) Retrieval bootstrapping: Use the adapted model from (a) to generate improved formalization attempts on moderately OOD domains (e.g., real analysis, combinatorics). These improved attempts yield more informative retrieval feedback—failed compilations with specific missing-import errors identify which Mathlib definitions are needed, while successful formalizations validate retrieved dependencies. Re-rank and update the retrieval index based on these signals.\n  **Transition criterion (b)→(c):** Advance when: (i) retrieval recall@10 on bootstrapped queries ≥ 30% (measured against ground-truth dependencies from DDR's dataset for domains where available, or estimated via compilation success improvement with/without retrieval), and (ii) compilation rate on moderate-OOD domains ≥ 25%. If compilation rate plateaus (< 2pp improvement over 200 consecutive steps), trigger early transition to (c) with current retriever.\n  (c) Far-OOD adaptation: Apply TTRL on truly OOD domains (algebraic geometry, PDE theory, condensed mathematics, MathAtlas MA-Hard) using the bootstrapped retriever and optionally a critic fine-tuned on verified pairs accumulated from stage (b). On these hard domains, the adaptive reward automatically falls back to R = r_compile × r_critic (since fewer than M=4 candidates typically compile), providing clean gradient signal without degenerate BEq consensus.\n\n**Evaluation.** Measure BEq@K and compilation success on FormalMATH's 5,560-problem multi-domain benchmark, the OOD Con-NF benchmark, CombiBench, and MathAtlas's 52K graduate-level problems (with emphasis on MA-Hard's 700 entities with average dependency depth 30, where the best current model achieves only 2.6% correctness). Compare against: (1) ATF-32B as the state-of-the-art iterative refinement baseline (94.51%/65.38% FormalMath-Lite/CombiBench), (2) ATLAS as the strong SFT-only data augmentation baseline (70.08% pass@1 miniF2F), (3) Monotonic Reference-Free Refinement as the inference-time orchestration upper bound (90.27% overall miniF2F), (4) DRIFT as the strongest static retrieval baseline (62.33% BEq+@10 Con-NF), (5) FormaRL as the RL-without-retrieval baseline, (6) compilation-only TTRL and critic-only TTRL ablations, (7) standard GRPO vs. DDRL's debiased advantages (including separate ablations for each of DDRL's three components), (8) static retrieval vs. co-adaptive retrieval during TTRL, and (9) iterative self-refinement with compilation feedback (ATF-style) as a simpler non-RL baseline. Report per-domain breakdown to quantify adaptation gains across the progressive curriculum, with particular attention to how retrieval precision evolves across curriculum stages and whether co-adaptive retrieval outperforms frozen DRIFT-style retrieval during adaptation.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "1100-1500 A100-80GB hours (base formalizer GRPO training with multi-tier reward: ~350h on 8 GPUs; DDR retriever fine-tuning: ~80h on 4 GPUs; TTRL progressive adaptation across 3 curriculum stages × 5 domains with DDRL debiasing and ablations: ~550h on 4 GPUs; CriticLean critic inference during training: ~80h on 2 GPUs for the 14B critic; evaluation and inference: ~100h) + 12,000-18,000 CPU-hours for Lean 4 verification (128 parallel workers via Kimina Lean Server with LRU caching)",
      "timeline": "14-18 weeks (4 wk base training + critic integration, 2 wk retriever, 5 wk progressive TTRL experiments across curriculum stages, 3-4 wk ablations and writing)",
      "estimated_gpu_cost": "$2,200-$3,800 at ~$2.00/A100-hr + ~$600-$900 CPU verification costs"
    },
    "human_in_loop": {
      "gpu_hours": "900-1200 A100-80GB hours (Claude handles critic evaluation augmentation and data synthesis, reducing CriticLean annotation overhead ~25%) + 10,000-14,000 CPU-hours for Lean verification",
      "timeline": "10-14 weeks (Claude-assisted critic calibration in Phase 1; parallel curriculum experiment management in Phase 3)",
      "claude_api_cost": "$500-$800 (critic reward calibration during GRPO training, synthetic domain-specific formalization examples, automated curriculum scheduling, ablation analysis)",
      "estimated_gpu_cost": "$1,800-$3,000 + ~$500-$700 CPU costs"
    },
    "auto_research": {
      "gpu_hours": "1800-2400 A100-80GB hours (automated hyperparameter sweeps over retrieval top-k, DDRL sampling parameters, critic threshold, GRPO group sizes K ∈ {16,32,64}, curriculum staging boundaries and transition thresholds, plus multi-seed evaluation) + 25,000-35,000 CPU-hours for Lean verification at scale",
      "timeline": "7-10 weeks (highly parallelized; wall-clock bottleneck is Lean 4 verification, mitigated by 128+ Kimina Lean Server workers with LRU caching achieving ~0.35s amortized per proof at 32 CPUs, ~0.10s at 64 CPUs)",
      "claude_api_cost": "$900-$1,400 (automated experiment design, reward function ablation analysis, curriculum boundary optimization, paper drafting)",
      "estimated_gpu_cost": "$3,600-$6,000 + ~$1,200-$1,700 CPU costs",
      "speed_bottleneck": "Lean 4 compilation latency (~3.65s per statement with warm LRU cache on single worker; ~0.10s amortized at 64 workers) dominates reward computation. Mitigated with Kimina Lean Server's pre-warmed REPL pool and LRU header caching (1.94x speedup over cold start). For K=32, batch=256: ~4,600 verifications/step requiring ~27 min at 32 CPUs or ~3.9 min at 128 CPUs. CriticLean inference (~14B model) adds ~0.5s per candidate on A100 but runs on GPU in parallel with CPU verification."
    }
  },
  "target_venues": [
    "AAAI 2027 (abstract: July 21, full paper: July 28, 2026 — confirmed)",
    "EACL 2027 via ARR August cycle (submission: August 3, 2026; commitment deadline TBD — confirmed, note corrected from originally announced August 6)",
    "NeurIPS 2026 Workshops (suggested contribution deadline: August 29, 2026 — confirmed; suitable for early results from curriculum stages 1-2)",
    "ICLR 2027 (deadline not yet announced as of May 2026 — best fit for full pipeline results including MathAtlas evaluation)"
  ],
  "level": "top-tier",
  "key_references": [
    "TTRL: Test-Time Reinforcement Learning (NeurIPS 2025)",
    "Understanding and Mitigating Spurious Signal Amplification in Test-Time Reinforcement Learning for Math Reasoning [DDRL] (ACL 2026 Findings)",
    "CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization (arXiv 2507.06181, ByteDance/Nanjing)",
    "Autoformalizer with Tool Feedback [ATF] (arXiv 2025)",
    "ATLAS: Autoformalizing Theorems through Lifting, Augmentation, and Synthesis of Data (NeurIPS 2025)",
    "Monotonic Reference-Free Refinement for Autoformalization (arXiv 2026)",
    "Olympiad-level formal mathematical reasoning with reinforcement learning [AlphaProof] (Nature 2025)",
    "FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)",
    "Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach (ICLR 2025 Spotlight)",
    "Improving Autoformalization Using Direct Dependency Retrieval [DDR] (arXiv 2025)",
    "DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems (ICLR 2026)",
    "Automated Formalization via Conceptual Retrieval-Augmented LLMs [CRAMF] (arXiv 2025)",
    "Kimina-Prover Preview: Towards Large Formal Reasoning Models with Reinforcement Learning (arXiv 2025)",
    "Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification (arXiv 2025)",
    "FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)",
    "MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv 2605.14061, May 2026)",
    "StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs through Knowledge-Reasoning Fusion (AAAI 2026)",
    "Aria: An Agent For Retrieval and Iterative Auto-Formalization via Dependency Graph (ICLR 2026)",
    "ProofBridge: Auto-Formalization of Natural Language Proofs in Lean via Joint Embeddings (ICLR 2026)",
    "ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (arXiv 2025)",
    "GTED: Generalized Tree Edit Distance—A Faithful Evaluation Metric for Statement Autoformalization (arXiv 2025)",
    "ASSESS: A Semantic and Structural Evaluation Framework for Statement Similarity (arXiv 2025)"
  ],
  "description": "Current autoformalization models achieve strong in-distribution results (ATF: 94.51% Pass@1 on FormalMath-Lite; ATLAS: 96.93% pass@128 on miniF2F) but collapse on unfamiliar mathematical domains due to missing domain-specific formal library dependencies and fixed inference-time behavior. We propose TTRA (Test-Time Retrieval-Augmented autoformalization), the first method unifying co-adaptive retrieval, a trained semantic critic, and debiased test-time reinforcement learning for domain-adaptive autoformalization. Building on a GRPO-trained Qwen3-8B base formalizer, we deploy DDR-style suffix-array-verified dependency retrieval that co-evolves with the model during test-time adaptation—unlike static pipelines such as DRIFT, which can match oracle performance on specific benchmarks (62.33% vs Oracle* 58.90% BEq+@10 on Con-NF) but cannot adapt to the model's evolving capabilities, and which MathAtlas (May 2026) shows can even degrade performance when context is naively injected. We introduce a multi-tier adaptive reward: Lean 4 compilation as a binary gate, CriticLeanGPT-14B as a semantic fidelity critic (84.8% accuracy on CriticLeanBench), and BEq consensus density as a precision-oriented bonus—with automatic fallback to R = r_compile × r_critic when fewer than 4 candidates compile, preventing degenerate BEq signals on hard OOD problems. We incorporate DDRL's three-component debiased advantage estimation—frequency-based balanced sampling, fixed ±1 advantages replacing GRPO's normalized advantages, and consensus-based off-policy refinement—which achieves up to 19.0% relative improvement over the strongest baseline (ETMR) on AIME 2024 (9.2pp absolute gain: 15.8→25.0 for Qwen2.5-Math-1.5B). To break the bootstrapping problem (poor OOD retrieval → bad formalizations → noisy rewards → failed adaptation), we introduce a progressive domain curriculum with quantitative transition criteria: advance from near-distribution warm-start to retrieval bootstrapping when compilation rate ≥ 40% and critic approval ≥ 60%, then to far-OOD adaptation when retrieval recall@10 ≥ 30% on bootstrapped queries. Evaluation spans FormalMATH, Con-NF, CombiBench, and MathAtlas's 52K graduate-level problems (where the best model achieves only 2.6% on MA-Hard with average dependency depth 30), with explicit comparisons against ATF (iterative refinement), ATLAS (SFT-only), DRIFT (static retrieval SOTA), Monotonic Refinement (multi-model orchestration), FormaRL (RL without retrieval), and static-vs-adaptive retrieval ablations. After exhaustive search through May 2026, no prior work combines co-adaptive retrieval, semantic critic rewards, and debiased test-time RL for autoformalization.",
  "project_name": "ttra_critic_guided",
  "source": "web_research",
  "change_type": "minor",
  "reviewer_response": {
    "issue_1_ddrl_numbers_corrected": "FIXED: The 58.2% figure was not reported in the DDRL paper (arxiv:2604.21327). It was an externally computed relative gain of DDRL (25.0) over vanilla TTRL (15.8) on AIME 2024, but the paper itself reports improvements relative to ETMR (the strongest baseline, scoring 21.0), yielding +19.0% relative improvement. All instances replaced: now consistently cite '19.0% relative improvement over the strongest baseline (ETMR) on AIME 2024' and '9.2 absolute point gain (Qwen2.5-Math-1.5B: 15.8→25.0).' Additionally corrected DDRL's method description to include all three components: (1) frequency-based balanced sampling, (2) fixed ±1 advantages, and (3) consensus-based off-policy refinement using rejection sampling — the ablation shows the third component contributes the largest single gain (47.0→52.9 average).",
    "issue_2_criticleanbench_inconsistency_resolved": "FIXED: The inconsistency arose from conflating two model sizes. Verified from CriticLean Table 2: CriticLeanGPT-Qwen3-14B-RL achieves 84.8% accuracy, CriticLeanGPT-Qwen3-32B-RL achieves 87.0% accuracy. Since our approach uses the 14B-RL model (balancing cost and capability for reward computation during TTRL), all method sections now consistently cite 84.8%. The 87.0% figure is retained only when referencing the best CriticLeanGPT variant (32B-RL) in the landscape/opportunity sections for context.",
    "issue_3_curriculum_transitions_specified": "ADDRESSED: Defined quantitative, reproducible transition criteria. Stage (a)→(b): compilation rate ≥ 40%, critic approval rate ≥ 60% among compilable candidates, BEq@32 improvement ≥ 3pp over pre-adaptation baseline. Timeout: T_max=500 GRPO steps, after which the domain is reclassified to stage (c). Stage (b)→(c): retrieval recall@10 ≥ 30% on bootstrapped queries (measured against DDR ground-truth where available, otherwise estimated via compilation improvement with/without retrieval), compilation rate on moderate-OOD ≥ 25%. Early transition trigger: compilation rate plateaus (< 2pp improvement over 200 consecutive steps). These thresholds are motivated by: 40% compilation rate ensures sufficient signal for GRPO (at least ~13 compilable candidates from K=32); 60% critic approval avoids training on predominantly incorrect formalizations; 3pp BEq improvement confirms TTRL provides meaningful adaptation.",
    "issue_4_beq_degeneracy_addressed": "ADDRESSED: Introduced adaptive reward degradation: when fewer than M=4 candidates out of K=32 compile (common on hard OOD domains like algebraic geometry, condensed mathematics, and MathAtlas MA-Hard), BEq consensus density becomes degenerate (trivially 0 or 1 for most groups). In this regime, the reward automatically falls back to R = r_compile × r_critic, dropping the BEq term entirely. This provides clean gradient signal on the hardest problems. The M=4 threshold is motivated by: with fewer than 4 compilable candidates, BEq equivalence classes are too small for meaningful consensus statistics. This fallback is especially relevant for stage (c) of the progressive curriculum.",
    "issue_5_drift_oracle_reframed": "ADDRESSED: Engaged substantively with DRIFT's oracle-exceeding result rather than dismissing it. Key reframing: (1) DRIFT exceeds oracle on Con-NF (62.33% vs 58.90%) because illustrative theorems provide premise usage demonstrations beyond mere definitions, but DRIFT still falls short on ProofNet (21.93% vs 27.54%), showing the gap isn't universally closed. (2) DRIFT's own authors note effectiveness 'depends heavily on model-specific knowledge boundaries' and can 'act as a distractor' on simpler problems. (3) The core value proposition is shifted from 'closing the static retrieval gap' to 'co-adaptive retrieval that evolves with model capabilities during TTRL' — something no static pipeline (including DRIFT) can achieve. (4) MathAtlas (May 2026) provides strong supporting evidence: adding 500 tokens of local context actually DEGRADED prompted systems' performance, demonstrating that retrieval quality (not quantity) is paramount and must adapt to the model's current state. (5) Added DRIFT as an explicit evaluation baseline to directly measure the marginal value of co-adaptive over static retrieval.",
    "issue_6_mathatlas_added": "ADDRESSED: Added MathAtlas (arxiv:2605.14061, May 2026) as both supporting evidence and evaluation benchmark. Key statistics: 52K graduate-level problems from 103 textbooks, 178K dependency relations, average dependency depth 30 (range 0-80), best model achieves only 2.6% on MA-Hard (700 entities), performance degrades with dependency depth (KS test p<0.001). MathAtlas is the first autoformalization benchmark to include dependency relations, making it ideally suited for evaluating our dependency-aware approach. Added to: opportunity (motivation for adaptive retrieval), landscape (as new benchmark), approach (evaluation plan), and key_references."
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15c4ba1f-c07d-443b-82f8-6143f5f4d3ae",
  "isSidechain": false,
  "requestId": "req_011CbTY2VdujpNwBXQqr5sbA",
  "type": "assistant",
  "uuid": "19bf5449-4e89-43b7-aee0-2c54e0f80f06",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011STzMQ9y7BXBfihwmUZEof",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5192,
      "cache_read_input_tokens": 51687,
      "output_tokens": 9414,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5192,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 9414,
          "cache_read_input_tokens": 51687,
          "cache_creation_input_tokens": 5192,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5192
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

_source line 87_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Aut…",
  "leafUuid": "19bf5449-4e89-43b7-aee0-2c54e0f80f06",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6"
}
```

---

### Runtime record

_source line 88_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise autoformalization TTRL paper with verified data and concrete curriculum",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6"
}
```

---

### Runtime record

_source line 89_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Critic-Guided Test-Time Retrieval-Augmented RL for Domain-Adaptive Aut…",
  "leafUuid": "19bf5449-4e89-43b7-aee0-2c54e0f80f06",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6"
}
```

---

### Runtime record

_source line 90_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise autoformalization TTRL paper with verified data and concrete curriculum",
  "sessionId": "2a30fe45-086a-4752-b69b-cc68f89516e6"
}
```

---
