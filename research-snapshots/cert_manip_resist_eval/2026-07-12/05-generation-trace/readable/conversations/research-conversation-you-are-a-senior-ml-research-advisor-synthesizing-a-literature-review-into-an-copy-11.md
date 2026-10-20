# Research conversation: You are a senior ML research advisor synthesizing a literature review into an actionable research strategy. **Today's da

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/f0e056d9-d209-4ed0-8a96-6ccdc25ef9c5.jsonl`
- **Structured JSON:** [`be06719352ff2bd60120.json`](../../sessions/be/be06719352ff2bd60120.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T05:35:04.309Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T05:35:04.309Z",
  "sessionId": "f0e056d9-d209-4ed0-8a96-6ccdc25ef9c5",
  "content": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.\n\n**Today's date: 2026-05-29 (UTC).**\n\n## Research area: Target: AAAI 2026\nTrack: Machine Learning (ML) — Reinforcement Learning / Mathematical Reasoning\n\nDirection: RL-trained mathematical reasoning models exhibit 47-73% accuracy drops under trivial perturbations (numerical substitution, variable renaming) despite achieving SOTA on clean benchmarks. We propose Math-Aware Consistency Regularization (MACR): adding a JS-divergence consistency term between model outputs on original and mathematically-equivalent perturbed problems during GRPO training, with a complementary discrimination loss against surface-similar but semantically different problems. This adapts proven NLP consistency techniques (F²C, PPCL) to mathematical reasoning with math-equivalence-aware perturbation generation and RL integration — a combination no existing work provides.\n\nSeed Papers:\n- Mirzadeh et al., GSM-Symbolic (Apple, ICLR 2025) — documents up to 65% accuracy drops from single irrelevant clause; establishes that models pattern-match rather than reason\n- VAR-MATH (arXiv 2025) — most damning evidence: 47.9-72.9% drops for RL models on numerically re-parameterized competition math; directly motivates why RL training is the problem\n- Gao et al., AbstRaL (ICLR 2026) — only existing training-time intervention; uses abstraction not invariance; limited to GSM-level; our primary comparison baseline\n- Flip-Flop Consistency / F²C (arXiv 2024) — JS-divergence consistency for prompt perturbation robustness in NLP; proves the technique works but has never been adapted to math reasoning or RL\n- PPCL (EACL 2024) — KL-based consistency regularization recovering 59-69% of perturbation-induced drops in NLU; complementary theoretical grounding\n- CSR: Causal Consistency Regularization (arXiv 2025) — enforces causal faithfulness via operator-level interventions during SFT; closest methodological cousin but SFT-only and targets faithfulness not perturbation invariance\n- APRM (arXiv 2025) — adversarial PRM training on reasoning errors; shows PRM quality matters for downstream RL; motivates our perturbation-robust PRM extension\n\nKnown Gaps:\n- No work applies consistency regularization (JS/KL divergence across equivalent problem variants) during RL training for mathematical reasoning — F²C and PPCL remain NLP-only and SFT-only\n- No PRM has been trained to be robust to surface-form variations of equivalent problems — APRM addresses reasoning errors, not perturbation invariance\n- No training-time robustness intervention has been demonstrated on competition-level math (AIME/Putnam); AbstRaL is GSM-only\n\nTheoretical Anchor: Mathematical equivalence defines a natural invariance class — problems that differ only in surface form (variable names, specific numbers, phrasing) but share identical mathematical structure should produce identical solution distributions. RL training violates this invariance because the reward signal (correct/incorrect final answer) provides no gradient against surface-form-dependent reasoning. A consistency regularization term explicitly penalizes policy divergence across equivalent variants, forcing the model to learn representations that are invariant to mathematically irrelevant features. This is a direct instantiation of Invariant Risk Minimization principles in the RL-for-reasoning setting.\n\nConstraints:\n- Compute: ≤200 H100-hours (budget: 40h baseline GRPO + 90h method variants + 30h evaluation + 20h analysis + 20h buffer)\n- Models: Primary experiments on 7B (Qwen2.5-Math-7B); scaling verification on 14B\n- Evaluation: GSM-Symbolic, GSM-Plus, VAR-MATH (AMC23/AIME24/AIME25), MATH-Perturb; train-time perturbations (numerical substitution, variable renaming) held out from eval perturbations (distractor insertion, structural changes)\n\nQuality Self-Checks:\n- [x] Core insight: RL training optimizes for reward on fixed problem forms, creating surface-form dependencies that consistency regularization can break by enforcing invariance across equivalent variants.\n- [x] Why not obvious: Consistency regularization is well-known in NLP but requires math-aware equivalence-preserving perturbation generation (not just paraphrase) and RL integration (not just SFT) — two non-trivial adaptations that straddle communities.\n- [ ] Baseline fear test: A pure data-augmentation baseline (adding perturbed problems to RL training without consistency loss) could achieve substantial gains. The paper MUST include this baseline and show the consistency term provides additional benefit beyond augmentation. If the gap is <5%, the contribution is weak.\n- [x] Information exploited: Mathematical equivalence structure — the method uses symbolic verification that perturbations preserve the problem's mathematical structure, which pure augmentation or paraphrase-based consistency ignores.\n\nAvoid:\n- Framing this as 'just data augmentation with extra steps' — the consistency objective is the contribution, not the perturbation generation. Must clearly show augmentation-only baseline is insufficient.\n- Over-claiming generality without testing on held-out perturbation types — the key differentiator from augmentation is transfer to unseen perturbation types, so this MUST be demonstrated.\n- Testing only on GSM-level math — this repeats AbstRaL's limitation and loses the competition-math differentiator.\n- Ignoring clean accuracy — if MACR degrades unperturbed accuracy by >2 points, reviewers will question practicality.\n\n## Paper analyses (22 papers)\n\n[\n  {\n    \"title\": \"GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models\",\n    \"venue\": \"ICLR 2025 (Poster)\",\n    \"problem_identification\": \"GSM8K is a static benchmark vulnerable to contamination and overfitting, providing no mechanism to test whether models are robust to superficial changes — yet it is the dominant math reasoning evaluation. The authors showed 21/25 models had statistically inflated GSM8K scores vs. parameterized variants.\",\n    \"key_insight\": \"Converting fixed benchmarks into symbolic templates with parameterized variables (names, numbers, clauses) enables controlled measurement of reasoning invariance — revealing that LLMs pattern-match rather than reason, as evidenced by up to 65% accuracy drops from a single irrelevant clause (GSM-NoOp).\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"100 GSM8K questions were manually converted into symbolic templates parameterizing names, numerical values, and object descriptors with validity constraints. 50 instantiations per template yield 5,000 examples across 50 parallel datasets. Three perturbation types (name-only, number-only, combined) plus difficulty scaling (GSM-M1/P1/P2) and the novel GSM-NoOp (inserting a single mathematically irrelevant clause) systematically probe fragility. Statistical significance is assessed via one-sample t-tests.\",\n    \"limitations_and_open_questions\": \"Post-publication audit (Sturgeon 2026) found only 12.4% of GSM-NoOp distractors were truly unambiguous, with drops becoming insignificant for frontier models on clean distractors. Templates cover only grade-school math; no competition-level extension. Reviewer criticism of statistical methodology (Ivanova analysis) reduced the '21/25 significant' claim to ~3-4 models.\",\n    \"building_blocks\": [\n      \"GSM-Symbolic parameterized templates\",\n      \"GSM-NoOp distractor insertion methodology\",\n      \"Performance variance measurement across instantiations\",\n      \"Symbolic template generation with validity constraints\"\n    ],\n    \"relevance_to_seed\": \"Foundational benchmark establishing the fragility phenomenon MACR aims to fix; GSM-Symbolic serves as a primary evaluation target, though the GSM-NoOp findings may be less damning than originally claimed.\"\n  },\n  {\n    \"title\": \"Prompt Perturbation Consistency Learning for Robust Language Models\",\n    \"venue\": \"EACL 2024 Findings\",\n    \"problem_identification\": \"LLMs suffer 13-41% performance drops on intent classification and slot filling under realistic perturbations (ASR oronyms, synonyms, paraphrases), and standard data augmentation requires 10x more perturbed samples to achieve comparable recovery because it treats each augmented example independently, ignoring semantic equivalence.\",\n    \"key_insight\": \"Augmented data should not merely add training volume — a JS-divergence consistency term between output distributions on clean and perturbed inputs extracts alignment signal that raw augmentation misses, recovering 59-69% of perturbation-induced drops with only 1/10th the augmented data.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"For each clean input x_c and its perturbed counterpart x_p (generated via oronym substitution, synonym replacement, or paraphrase with BERTScore≥0.85 filtering), the model produces token-level softmax distributions. The training loss combines three terms: L = λ₁·CE(clean) + λ₂·CE(perturbed) + λ₃·JS(ŷ_c ∥ ŷ_p), where JS divergence is computed token-by-token for length-preserving perturbations or over averaged distributions for paraphrases. Ablations confirm all three terms are necessary.\",\n    \"limitations_and_open_questions\": \"Evaluated only on NLU tasks (IC/SF) with discriminative-style outputs, not generative reasoning. Paraphrase perturbation is the hardest case due to length-mismatch requiring averaged distributions. Never tested in RL training or on mathematical reasoning — the two key adaptations MACR requires.\",\n    \"building_blocks\": [\n      \"JS-divergence consistency loss formulation\",\n      \"Three-term loss architecture (clean CE + perturbed CE + consistency)\",\n      \"BERTScore-based semantic equivalence filtering\",\n      \"10x data efficiency over pure augmentation\"\n    ],\n    \"relevance_to_seed\": \"Direct theoretical ancestor of MACR's consistency objective; the JS-divergence formulation and data-efficiency advantage over augmentation are the core claims MACR must replicate in the math-RL setting.\"\n  },\n  {\n    \"title\": \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\",\n    \"venue\": \"Nature 2025\",\n    \"problem_identification\": \"Existing reasoning approaches required expensive human-annotated chain-of-thought trajectories, creating a scalability bottleneck and constraining models to mimic human reasoning patterns rather than discovering potentially superior strategies.\",\n    \"key_insight\": \"Final-answer rewards alone, without process supervision or human-written reasoning traces, suffice to grow genuine reasoning behaviors (self-reflection, backtracking, verification) via pure RL — demonstrated by R1-Zero improving from 15.6% to 71.0% on AIME 2024.\",\n    \"innovation_type\": \"scaling\",\n    \"method_summary\": \"GRPO eliminates the value network by normalizing rewards within groups: A_i = (r_i - mean(r))/std(r) for G sampled outputs per prompt, combining clipped PPO ratios with KL penalty against a reference policy. The full pipeline has four stages: cold-start SFT on curated R1-Zero outputs, reasoning RL with rule-based rewards on verifiable tasks, rejection sampling + SFT for quality broadening, and diverse RL with hybrid rewards. Only accuracy and format rewards are used — no process reward model.\",\n    \"limitations_and_open_questions\": \"GRPO optimizes purely for final-answer correctness, providing no gradient against surface-form-dependent reasoning — exactly the vulnerability MACR targets. Language mixing and readability degradation in pure RL motivate the cold-start stage. The group-relative advantage normalization (dividing by std) is later shown by MathForge to suppress updates for very easy and very hard problems.\",\n    \"building_blocks\": [\n      \"GRPO algorithm (group sampling, relative advantage, no value network)\",\n      \"Four-stage training pipeline\",\n      \"Rule-based verifiable rewards\",\n      \"KL-divergence reference policy regularization\"\n    ],\n    \"relevance_to_seed\": \"The training paradigm MACR augments — GRPO's reward structure provides no invariance pressure, making it the precise point where consistency regularization must be injected.\"\n  },\n  {\n    \"title\": \"Harder Is Better: Boosting Mathematical Reasoning via Difficulty-Aware GRPO and Multi-Aspect Question Reformulation (MathForge)\",\n    \"venue\": \"ICLR 2026 (Poster)\",\n    \"problem_identification\": \"Standard GRPO's advantage normalization (dividing by std) produces maximum update magnitudes for ~50% accuracy questions while suppressing updates for both easy and hard problems — formally proved in Theorem 1. Existing augmentation adds diversity but not systematic difficulty.\",\n    \"key_insight\": \"Replacing std with mean absolute deviation (MAD) in advantage normalization yields constant total update magnitude regardless of difficulty, and coupling this with answer-preserving difficulty-increasing reformulation creates a synergistic data-algorithm loop yielding +4.56% average improvement.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"DGPO uses MAD normalization (A_i = (r_i - mean(r))/MAD(r)) ensuring difficulty-balanced updates, plus softmax question-level weighting prioritizing harder problems. MQR reformulates questions along three aspects — background (narrative context), term (abstract terminology), sub-problem (nested conditions) — all preserving gold answers for 4x dataset expansion. Best results use o3 as reformulator (~$184 for 22.5K questions).\",\n    \"limitations_and_open_questions\": \"No evaluation of adversarial robustness, perturbation consistency, or out-of-distribution resilience — only clean accuracy on standard benchmarks. Ablations show ~75% of gains come from MQR augmentation alone (+3.43% vs +4.56% combined), raising questions about DGPO's marginal contribution. Best reformulation requires frontier model (o3).\",\n    \"building_blocks\": [\n      \"MAD-based difficulty-balanced advantage estimation\",\n      \"Answer-preserving question reformulation (3 aspects)\",\n      \"Difficulty-aware question-level weighting\",\n      \"Formal analysis of GRPO update magnitude imbalance\"\n    ],\n    \"relevance_to_seed\": \"Key 'augmentation-only' baseline: MQR represents the strongest form of augmentation+RL without consistency objectives. MACR must demonstrate gains beyond what MQR-style difficulty augmentation achieves, and should test whether MathForge models are robust to perturbations (likely not, since robustness was never evaluated).\"\n  },\n  {\n    \"title\": \"Beyond Correctness: Learning Robust Reasoning via Transfer (RLTR)\",\n    \"venue\": \"arXiv 2026\",\n    \"problem_identification\": \"RLVR optimizes solely for final-answer correctness and actually *degrades* multi-sample consistency — on MATH-500, Maj@16 drops from 81.2% (base) to 80.2% (after RLVR), revealing that accuracy gains come at the cost of reasoning brittleness.\",\n    \"key_insight\": \"Robust reasoning should be transferable: if a partial reasoning prefix can guide a separate frozen receiver model to the correct answer, the reasoning is genuinely stable and interpretable rather than relying on model-specific shortcuts.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"The generator produces a reasoning trace, which is truncated at random ratio τ~Uniform(0.3,0.9). A frozen receiver model (e.g., Qwen2.5-3B) attempts completion from the prefix. Transfer reward R_trans=1 if the receiver reaches the correct answer. Combined reward: R = R_RLVR + t·R_trans (t=1.0). Training uses GRPO on 3K MATH problems. The ~7% per-step overhead is offset by 2.5x fewer steps to convergence, with net ~57% compute reduction.\",\n    \"limitations_and_open_questions\": \"Robustness is defined as cross-model transferability of reasoning traces, not invariance under input perturbation — these are complementary but distinct mechanisms. No evaluation on perturbed inputs (GSM-Symbolic, VAR-MATH). The receiver model choice and truncation ratio sensitivity are not thoroughly ablated. Potential circularity: receiver quality bounds what transfer reward can measure.\",\n    \"building_blocks\": [\n      \"Transfer reward via cross-model prefix completion\",\n      \"Random truncation ratio for robustness\",\n      \"Empirical evidence that RLVR degrades Maj@K consistency\",\n      \"Demonstration of 2.5x training efficiency gain\"\n    ],\n    \"relevance_to_seed\": \"Most directly comparable work addressing reasoning robustness in RL training. RLTR's transfer-based robustness is complementary to MACR's invariance-based approach — the two could potentially be combined. RLTR's finding that RLVR degrades consistency strongly motivates MACR's intervention.\"\n  },\n  {\n    \"title\": \"Toward Automated Robustness Evaluation of Mathematical Reasoning (MaSTer)\",\n    \"venue\": \"ACL 2026 Findings\",\n    \"problem_identification\": \"Existing robustness benchmarks (GSM-Plus, GSM-Symbolic) rely on hand-crafted templates or fixed perturbation rules that lack model-adaptivity, are susceptible to contamination, and underutilize target-model characteristics — producing incomplete vulnerability assessments.\",\n    \"key_insight\": \"Reframing LLM robustness evaluation as software stress testing enables a dynamic adversarial loop where the rewriter self-discovers perturbation strategies through multi-round feedback, achieving 15-45pp higher failure rates than static benchmarks without requiring predefined perturbation rules.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"Three-component loop: a Rewriter (Qwen2.5-32B, temp=1.0) generates adversarial variants without prescribed rules, a Verifier validates semantic equivalence and checks target failure (98% precision), and the Target model is queried at temp=0. N=5 parallel streams each run K=3 iterations (15 attempts/problem), with cumulative conversation history enabling strategy refinement. Generated variants also serve as training data: SFT on 3,678 variants reduced target failure rate by 13.3 points.\",\n    \"limitations_and_open_questions\": \"Verifier relies on LLM judgment for semantic equivalence rather than symbolic verification — the 98% precision leaves room for false positives at scale. Generated perturbations are model-specific by design, potentially limiting generalizability as training data. Computational cost (32-61s/problem on 4×4090) may limit large-scale training data generation.\",\n    \"building_blocks\": [\n      \"Multi-round rewrite-verify adversarial loop\",\n      \"Model-adaptive perturbation discovery (no predefined rules)\",\n      \"Dual-use framework (evaluation + training data generation)\",\n      \"Cross-domain extension to MMLU/CommonsenseQA\"\n    ],\n    \"relevance_to_seed\": \"Complementary to MACR as both evaluation tool and perturbation generator — MaSTer's self-discovered perturbations could provide diverse training-time variants, while its adversarial evaluation could stress-test MACR-trained models beyond fixed benchmarks.\"\n  },\n  {\n    \"title\": \"VAR-MATH: Probing True Mathematical Reasoning in LLMs via Symbolic Multi-Instance Benchmarks\",\n    \"venue\": \"arXiv 2025\",\n    \"problem_identification\": \"Existing math benchmarks use fixed numerical instances, conflating memorization with reasoning; RL-trained models show inflated scores due to benchmark contamination and surface-form overfitting. The authors identified this by observing that models achieving near-perfect scores fail when numbers change.\",\n    \"key_insight\": \"Converting fixed competition problems into parameterized symbolic templates with constrained variable domains enables all-or-nothing evaluation across multiple instantiations, exposing whether models generalize across mathematically equivalent variants.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"A four-stage pipeline: (1) structural analysis of algebraic relationships, (2) symbolic parameterization replacing numerical constants with constrained variables, (3) parametric solution formulation verified by hand as symbolic functions, (4) precision specification for numerical stability. The strict evaluation metric requires correct answers on ALL instantiations of a template. Applied to AMC23, AIME24, AIME25 to create VAR-AMC23/AIME24/AIME25.\",\n    \"limitations_and_open_questions\": \"Templates require manual expert construction (not scalable); only numerical re-parameterization is tested — structural or phrasing perturbations are unexplored. Frontier models (DeepSeek-R1) show only 3.6-24.8% drops, suggesting the problem may be scale-dependent.\",\n    \"building_blocks\": [\n      \"VAR-AMC23/AIME24/AIME25 benchmarks\",\n      \"Symbolic template methodology\",\n      \"Strict all-or-nothing evaluation metric\",\n      \"Quantified fragility evidence for RL-trained models\"\n    ],\n    \"relevance_to_seed\": \"Provides the primary empirical motivation for MACR: 47.9-72.9% accuracy drops for RL models on numerically re-parameterized competition math directly justify why consistency regularization during RL training is needed.\"\n  },\n  {\n    \"title\": \"Causal Consistency Regularization: Training Verifiably Sensitive Reasoning in Large Language Models\",\n    \"venue\": \"arXiv 2025\",\n    \"problem_identification\": \"Models produce correct answers from logically invalid reasoning traces (unfaithful reasoning), with 36-42% of correct outputs relying on spurious shortcuts. Identified via counterfactual sensitivity testing: swapping operators in valid traces and checking if answers change appropriately.\",\n    \"key_insight\": \"A learned editor (6-layer Transformer trained via REINFORCE) can generate minimal, causally significant operator-level interventions that, combined with a KL-divergence penalty between original and counterfactual output distributions, forces genuine causal dependence between reasoning steps and answers during SFT.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"CSR adds ℒ_total = ℒ_task − λ·D_KL(p(Y|T,X) ∥ p(Y|T',X)) where T' is a minimally perturbed counterfactual trace. The learned editor generates perturbations optimizing validity-breaking, impact-maximizing, and minimality objectives. A warm-start curriculum progressively introduces the CSR loss, and token-subset optimization applies regularization only to high-impact positions, reducing overhead from 92.5% to ~9%.\",\n    \"limitations_and_open_questions\": \"Explicitly SFT-only — no RL integration demonstrated. Targets faithfulness (answer should change when reasoning breaks) rather than invariance (answer should stay same when problem surface-form changes). Tested on GSM8K-level math, not competition-level.\",\n    \"building_blocks\": [\n      \"KL-divergence consistency loss formulation\",\n      \"Learned perturbation editor architecture\",\n      \"Warm-start curriculum for regularization\",\n      \"Token-subset optimization for efficiency\"\n    ],\n    \"relevance_to_seed\": \"Closest methodological cousin — MACR adapts the same core idea (divergence penalty between original and perturbed outputs) but inverts the direction (enforcing invariance not sensitivity), targets problem perturbations not trace perturbations, and integrates with RL not SFT.\"\n  },\n  {\n    \"title\": \"DAPO: An Open-Source LLM Reinforcement Learning System at Scale\",\n    \"venue\": \"NeurIPS 2025\",\n    \"problem_identification\": \"Reproducing RL training for reasoning LLMs is blocked by undisclosed implementation details; naive GRPO/PPO suffer entropy collapse, wasted gradient computation on trivially solved/unsolvable prompts, length instability, and reward noise from truncated sequences.\",\n    \"key_insight\": \"Four orthogonal, individually-ablatable engineering innovations — asymmetric clipping (Clip-Higher, ε_low=0.2, ε_high=0.28), dynamic sampling filtering mixed-outcome groups only, token-level loss normalization, and graduated overlong reward shaping — together resolve entropy collapse and achieve SOTA with 50% fewer training steps.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"DAPO modifies GRPO with: (1) Clip-Higher decouples upper/lower clipping bounds to prevent entropy collapse while maintaining downward pressure; (2) Dynamic Sampling oversamples then filters to keep only groups with mixed correct/incorrect responses, ensuring non-zero advantages; (3) Token-level loss normalization weights each token equally regardless of sequence length; (4) Overlong Reward Shaping uses a graduated penalty zone instead of binary truncation penalties. Achieves 50 AIME 2024 points with Qwen2.5-32B.\",\n    \"limitations_and_open_questions\": \"No robustness evaluation — AIME 2024 scores may reflect contamination (per MathArena). Engineering-focused with limited theoretical analysis of why each component works. Does not address surface-form fragility at all.\",\n    \"building_blocks\": [\n      \"DAPO training algorithm as GRPO replacement\",\n      \"Clip-Higher for entropy preservation\",\n      \"Dynamic Sampling for gradient efficiency\",\n      \"Open-source verl-based training infrastructure\"\n    ],\n    \"relevance_to_seed\": \"Primary baseline RL algorithm for MACR experiments; MACR's consistency term provides complementary entropy preservation to Clip-Higher, and MACR could be implemented as an add-on to DAPO's training pipeline.\"\n  },\n  {\n    \"title\": \"The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward (DPH-RL)\",\n    \"venue\": \"arXiv 2025 (ICLR 2026 Poster)\",\n    \"problem_identification\": \"RLVR improves Pass@1 but degrades Pass@k due to diversity collapse — the policy narrows to single solution modes. Root cause: reverse-KL divergence (used in GRPO/PPO) is mode-seeking, actively suppressing low-probability solution paths.\",\n    \"key_insight\": \"Mass-covering f-divergences (forward-KL, JS) function as a rehearsal mechanism that forces continuous revisitation of the reference policy's solution space, preventing diversity collapse without sacrificing Pass@1 gains.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"DPH-RL uses a two-stage approach: (1) pre-sampling partitions data into mastered (D_pef) and challenging (D_exp) sets; (2) online training applies standard PPO-clip with no KL penalty on D_exp for aggressive exploration, while applying forward-KL or JS-divergence penalties on D_pef to maintain knowledge. The combined objective L_DPH-RL = L_exp + η·L_pef balances exploration and retention. Critically, f-divergence is computed via generator functions requiring only reference policy samples, eliminating online reference model overhead.\",\n    \"limitations_and_open_questions\": \"The two-stage data partitioning adds pipeline complexity. Results primarily on SQL (Bird) and math with Llama-8B — scaling to larger models and harder benchmarks is unverified. Does not address surface-form robustness, only solution diversity.\",\n    \"building_blocks\": [\n      \"JS-divergence formulation in RL-for-reasoning context\",\n      \"Forward-KL as rehearsal mechanism\",\n      \"Two-stage mastered/challenging data partitioning\",\n      \"Theoretical monotonic improvement guarantee for mass-covering divergences\"\n    ],\n    \"relevance_to_seed\": \"Directly validates JS-divergence as a viable regularizer in RL-for-reasoning, which MACR's consistency term also uses. DPH-RL applies JS between current and reference policy distributions; MACR applies JS between outputs on original and perturbed problems — complementary applications of the same divergence.\"\n  },\n  {\n    \"title\": \"Generative Adversarial Reasoner: Enhancing LLM Reasoning with Adversarial Reinforcement Learning (GAR)\",\n    \"venue\": \"ICLR 2026\",\n    \"problem_identification\": \"Sparse outcome-level rewards (correct/incorrect final answer) provide poor credit assignment for long reasoning chains, failing to distinguish partially-correct reasoning from fully flawed attempts. Existing PRMs are static and don't co-evolve with the policy.\",\n    \"key_insight\": \"Co-evolving a discriminator and reasoner through adversarial RL — where the discriminator evaluates reasoning chain slices for logical soundness and provides dense step-level rewards — creates an adaptive, increasingly challenging training signal that improves credit assignment without external annotation.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"GAR partitions reasoning chains into logically complete slices (~320 tokens) and trains a discriminator to evaluate each slice's soundness with structured justifications. The reasoner's reward combines exact-match and mean slice scores: R_rea = λ₁R_m + λ₂R_s. The discriminator optimizes R_dis = λ₃R_d + λ₄R_a, combining GAN-style discrimination (real vs. generated slices) and alignment (slice judgments must be consistent with answer correctness, preventing reward hacking). Both are trained via GRPO. Discriminator output is capped at 128 tokens, reducing training from 43h to 19h.\",\n    \"limitations_and_open_questions\": \"Adversarial co-training introduces instability risks and hyperparameter sensitivity (four λ weights). No robustness evaluation — gains may reflect better optimization not better reasoning. The discriminator's quality ceiling limits reasoner improvement.\",\n    \"building_blocks\": [\n      \"Slice-based reasoning chain decomposition\",\n      \"Adversarial co-training framework for reasoner+discriminator\",\n      \"Dense step-level reward from LLM discriminator\",\n      \"Alignment reward as anti-reward-hacking regularizer\"\n    ],\n    \"relevance_to_seed\": \"GAR's discriminator provides an alternative to MACR's consistency loss for improving reasoning quality during RL. The slice-based evaluation could complement MACR — a perturbation-robust discriminator (GAR + MACR's invariance objective) would provide both dense and robust rewards.\"\n  },\n  {\n    \"title\": \"MathArena: Evaluating LLMs on Uncontaminated Math Competitions\",\n    \"venue\": \"NeurIPS 2025 Datasets & Benchmarks\",\n    \"problem_identification\": \"AIME 2024 and other standard math benchmarks are contaminated in training data, inflating reported scores and making it impossible to distinguish memorization from reasoning. Detected by comparing model performance on widely-available vs. freshly-released competition problems.\",\n    \"key_insight\": \"Recurring math competitions provide a natural stream of expert-curated, pre-vetted, uncontaminated problems; evaluating models immediately upon problem release (before web dissemination) creates a contamination-proof evaluation methodology.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"MathArena aggregates 162 problems from seven recent competitions (AMC, AIME, CMIMC, HMMT, Putnam, IMO, etc.), evaluating 50+ models in real-time as competitions occur. The framework includes the first systematic proof-writing evaluation, where models must produce valid mathematical proofs scored against competition rubrics. Contamination analysis compares performance on pre-2024 (potentially contaminated) vs. post-2024 (clean) problems, finding statistically significant inflation on AIME 2024.\",\n    \"limitations_and_open_questions\": \"Competition problems have limited volume (tens per competition per year) and skew toward specific mathematical styles. Real-time evaluation creates a moving target — historical comparisons become difficult. Proof evaluation requires expert judges, limiting scalability.\",\n    \"building_blocks\": [\n      \"Contamination-free competition math benchmark\",\n      \"Real-time evaluation methodology\",\n      \"AIME 2024 contamination evidence\",\n      \"Proof-writing evaluation framework\"\n    ],\n    \"relevance_to_seed\": \"Critical for interpreting MACR's results: AIME 2024 is contaminated, so MACR must report on both AIME24 (with caveat) and cleaner benchmarks (AIME25, CMIMC). MathArena's methodology validates using recent competitions for evaluation, supporting MACR's use of VAR-MATH variants.\"\n  },\n  {\n    \"title\": \"AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking\",\n    \"venue\": \"ICLR 2026\",\n    \"problem_identification\": \"LLMs suffer severe accuracy drops under GSM perturbations (numerical changes, distractors) because they pattern-match on surface forms rather than reasoning abstractly. The authors identified this by connecting GSM-Symbolic fragility evidence to the observation that SFT-trained abstraction produces unfaithful outputs, implying RL is necessary.\",\n    \"key_insight\": \"Abstraction — converting concrete math problems into symbolic variable-operator representations — is a learnable skill better acquired through RL (GRPO with symbolic-distance rewards) than SFT, and this single capability broadly transfers to OOD mathematical and general reasoning tasks.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"Constructs GranulAR data by having an oracle LLM decompose GSM problems into abstract representations with symbolic variables (in0, in1, out0), verified via SymPy. Trains models with GRPO using two rewards: binary answer correctness (r_answer) and a continuous symbolic edit-distance reward (r_symbolic) measuring closeness to gold abstraction. The contextualized learning pipeline (problem → abstract question → abstract answer → abstraction) is critical — ablations show direct abstraction generation collapses performance.\",\n    \"limitations_and_open_questions\": \"Limited to GSM-level math (no competition-level evaluation); requires full model tuning limiting scalability; theoretical grounding for why abstraction helps OOD transfer is acknowledged as an open problem. Does the approach survive harder math where abstraction patterns are less formulaic?\",\n    \"building_blocks\": [\n      \"GranulAR data pipeline for abstraction generation\",\n      \"Symbolic edit-distance reward for GRPO\",\n      \"SymPy-based abstraction verification\",\n      \"Contextualized multi-step learning format\"\n    ],\n    \"relevance_to_seed\": \"Primary comparison baseline for MACR: AbstRaL addresses the same robustness problem but via abstraction rather than invariance-enforcing consistency regularization, and its GSM-only evaluation scope is exactly the gap MACR targets with competition-level math.\"\n  },\n  {\n    \"title\": \"Adversarial Training for Process Reward Models\",\n    \"authors\": \"Juneja et al.\",\n    \"venue\": \"arXiv 2025 (desk rejected at venue submission)\",\n    \"problem_identification\": \"PRMs trained on static datasets with fixed negative examples fail to generalize to novel reasoning errors, and collecting step-level human annotations is prohibitively expensive. The authors identified this by observing that existing PRMs overfit to the error distribution in their training data.\",\n    \"key_insight\": \"An adversarial generator-discriminator loop creates an automatic curriculum of increasingly sophisticated reasoning errors, eliminating the need for manual step-level annotation while producing PRMs that generalize better to unseen error types.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"Generator G (Llama-3.1-8B) takes correct reasoning steps and produces corrupted variants rewarded (+1) for deceiving PRM R, penalized (-1) for producing correct steps. R trains on 50/50 mix of gold and adversarial negatives. Optimization uses alternating PPO (5 steps each) stabilized by Optimistic Gradient Descent-Ascent (OGDA) for convergence toward Nash equilibrium, with KL and entropy regularization preventing mode collapse. A non-LLM correctness oracle (cosine similarity + entity matching) avoids human annotation dependency.\",\n    \"limitations_and_open_questions\": \"2-3× computational cost over standard PRM training; adversarial examples may concentrate in few exploit classes risking overfitting; desk rejected suggesting concerns about novelty or rigor. How does adversarial PRM training interact with perturbation-invariance — does the generator learn to exploit surface-form sensitivity?\",\n    \"building_blocks\": [\n      \"OGDA-stabilized adversarial RL for reward model training\",\n      \"Non-LLM correctness oracle for annotation-free PRM training\",\n      \"Progressive hard-negative curriculum generation\"\n    ],\n    \"relevance_to_seed\": \"Motivates MACR's perturbation-robust PRM extension: APRM shows adversarial training improves PRM generalization (+5.3pp OOD), but targets reasoning errors rather than surface-form invariance — combining APRM's adversarial framework with MACR's equivalence-preserving perturbations is a natural extension.\"\n  },\n  {\n    \"title\": \"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations\",\n    \"venue\": \"ICML 2025\",\n    \"problem_identification\": \"Prior perturbation benchmarks (GSM-Symbolic, GSM-Plus) only tested simple perturbations preserving solution methods, missing the harder case where small problem modifications fundamentally change the required approach. Identified by noting that no benchmark distinguished method-preserving from method-changing perturbations at competition difficulty.\",\n    \"key_insight\": \"The critical distinction is between simple perturbations (same method, different numbers) and hard perturbations (small textual changes that invalidate the original solution strategy), with the latter revealing a more insidious memorization pattern: models blindly apply learned solution templates without checking applicability.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"Constructs 558 perturbed problems (279 simple, 279 hard) from MATH Level-5, verified by 12 PhD-level math experts. Simple perturbations change values/constraints while preserving solution methods; hard perturbations make minimal edits that require entirely different approaches. Evaluates 20+ models finding severe drops on hard perturbations (o1-mini: -16.5%, GPT-4o: -27.6%) and a novel memorization signature: ICL with original solutions actively hurts performance (18-40% problems flip to incorrect), proving models apply memorized templates rather than reasoning.\",\n    \"limitations_and_open_questions\": \"Only 279 problems per category — small benchmark size limits statistical power. No training-time mitigation proposed, only diagnosis. The simple/hard dichotomy may miss intermediate perturbation difficulties. How do RL-trained models specifically compare to SFT models on hard perturbations?\",\n    \"building_blocks\": [\n      \"558 expert-verified Level-5 perturbed math problems\",\n      \"Simple vs. hard perturbation taxonomy\",\n      \"ICL-based memorization detection methodology\"\n    ],\n    \"relevance_to_seed\": \"Directly in MACR's evaluation suite: MATH-Perturb provides competition-level perturbation evaluation that AbstRaL lacks, and its hard perturbations test whether MACR's consistency training transfers to unseen perturbation types (method-changing variants not seen during training).\"\n  },\n  {\n    \"title\": \"Process Reward Models That Think (ThinkPRM)\",\n    \"venue\": \"arXiv 2025 (withdrawn from ICLR 2026)\",\n    \"problem_identification\": \"Discriminative PRMs require ~800K expensive step-level human labels yet still underperform on OOD tasks, while LLM-as-Judge approaches lack controllable compute scaling. The authors identified this gap by recognizing that reasoning models already have verification capabilities that can be elicited with minimal fine-tuning.\",\n    \"key_insight\": \"A reasoning model fine-tuned on just 1K synthetic verification chain-of-thought examples can outperform discriminative PRMs trained on 100× more data, because generative verification leverages the model's pre-existing reasoning capacity rather than learning a separate classification head.\",\n    \"innovation_type\": \"simplification\",\n    \"method_summary\": \"Samples verification CoTs from QwQ-32B-Preview on PRM800K problem-solution pairs, filters by format compliance, label agreement with gold annotations, and <4096 token length to avoid overthinking. Fine-tunes R1-Distill-Qwen models (1.5B–14B) with standard language modeling loss on ~1K filtered examples (~8K process labels). At inference, scores each step via conditional probability of 'correct' vs 'incorrect' tokens after generating verification reasoning. Supports compute scaling through parallel (multiple independent CoTs) and sequential (longer thinking) modes.\",\n    \"limitations_and_open_questions\": \"Withdrawn from ICLR 2026, suggesting potential concerns about evaluation rigor or novelty. Step label interference (earlier judgments biasing later ones) is acknowledged but not fully solved. Verification CoT quality depends on seed reasoning model capability. Is ThinkPRM robust to surface-form variations of mathematically equivalent problems?\",\n    \"building_blocks\": [\n      \"Verification CoT data synthesis pipeline from reasoning models\",\n      \"Generative step-level scoring via token probabilities\",\n      \"Parallel/sequential compute scaling for verification\"\n    ],\n    \"relevance_to_seed\": \"Relevant to MACR's perturbation-robust PRM extension: ThinkPRM's data-efficient generative verification framework could be combined with equivalence-preserving perturbation training to create PRMs that verify reasoning consistency across problem variants, not just step correctness.\"\n  },\n  {\n    \"title\": \"Scaling Behaviors of LLM Reinforcement Learning Post-Training: An Empirical Study in Mathematical Reasoning\",\n    \"venue\": \"ACL 2026\",\n    \"problem_identification\": \"While pre-training scaling laws (Chinchilla, Kaplan) are well-established, RL post-training scaling behavior was entirely uncharacterized — practitioners had no principled way to allocate compute between model size and training steps for RL fine-tuning. Identified by noting this gap in the scaling laws literature as RL post-training became standard practice.\",\n    \"key_insight\": \"RL post-training follows predictable power-law scaling (R²>0.99) in test loss vs. compute and data, but with a critical saturation effect: learning efficiency k(N) asymptotically approaches K_max, meaning larger models yield diminishing marginal returns beyond ~32B parameters.\",\n    \"innovation_type\": \"scaling\",\n    \"method_summary\": \"Conducts 63 GRPO fine-tuning experiments across Qwen2.5 (0.5B–72B) on 50K+ math problems with 3 repetitions each. Fits power-law models: log L(N,X) = -k(N)·log X + E(N) where k(N) = K_max/(1+N₀/N) captures efficiency saturation. Validates cross-architecture on Llama-3 (1B–70B). Key practical finding: data reuse up to 25× shows no degradation when total optimization steps are held constant, meaning performance is step-governed not uniqueness-governed. Inter-model extrapolation from 0.5B–32B accurately predicts 72B performance.\",\n    \"limitations_and_open_questions\": \"Only studies GRPO — do other RL algorithms (PPO, REINFORCE) follow the same scaling laws? Tested only on math reasoning — generalization to code, general reasoning unknown. Saturation analysis beyond 72B is extrapolation. How does adding auxiliary losses (like consistency regularization) affect scaling behavior?\",\n    \"building_blocks\": [\n      \"Power-law scaling formulations for RL post-training\",\n      \"Efficiency saturation model k(N) = K_max/(1+N₀/N)\",\n      \"Data reuse viability up to 25× without degradation\",\n      \"Compute-optimal model-size/steps allocation framework\"\n    ],\n    \"relevance_to_seed\": \"Directly informs MACR compute budgeting: the scaling laws predict that 7B Qwen2.5-Math is near-optimal for our 200 H100-hour budget, the data reuse finding validates training on augmented (perturbed) versions of the same problems, and the saturation model helps predict whether 14B scaling verification will show meaningful gains.\"\n  },\n  {\n    \"title\": \"Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs\",\n    \"venue\": \"arXiv 2025\",\n    \"problem_identification\": \"LLMs produce inconsistent predictions across semantically equivalent prompt templates, undermining reliability. Identified by measuring observed agreement (PoP_o) across 4-15 prompt formats per dataset and finding large variance in predictions for identical inputs.\",\n    \"key_insight\": \"Majority vote across prompt variations provides a reliable unsupervised pseudo-label, enabling self-supervised consistency training without any gold labels — the model's own consensus becomes the teaching signal.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"F²C combines three losses: (1) Consensus Cross-Entropy (CCE) trains all prompt variants toward the majority-vote pseudo-label c*; (2) JSD alignment minimizes Jensen-Shannon divergence among high-confidence consensus predictions; (3) a KL flip loss pulls non-consensus predictions toward the confident-consensus mixture q̄. Cases are stratified by agreement level (unanimous/consensus/no-consensus) with adaptive weighting via sigmoid-scaled log-likelihood gaps. Training uses LoRA on Qwen2.5-3B-Instruct.\",\n    \"limitations_and_open_questions\": \"Ablations show CCE dominates (+11.68% agreement alone vs +11.62% full F²C); the JSD/flip components add only marginal gains (+0.58% F1). Untested on generative tasks, math reasoning, or within RL training loops — all critical gaps for MACR adaptation.\",\n    \"building_blocks\": [\n      \"JS-divergence consistency loss between input variants\",\n      \"Majority-vote pseudo-labeling without supervision\",\n      \"Confidence-stratified case handling for alignment losses\",\n      \"LoRA-based unsupervised consistency fine-tuning\"\n    ],\n    \"relevance_to_seed\": \"Direct technical ancestor of MACR: the CCE + JSD loss framework can be adapted from NLP prompt-template invariance to math-equivalence invariance, but requires replacing paraphrase-based perturbations with structure-preserving mathematical\n... (truncated)\n\n## Your task\n\nSynthesize these paper analyses into a **Field Guide** — a strategic document that would help a researcher generate novel, high-quality ideas in this area. This is NOT a survey — it's an opinionated strategy guide for innovation.\n\nThink about:\n- What PATTERNS OF INNOVATION keep working in this field?\n- What do reviewers consistently reward?\n- Where are the real gaps (not assumed gaps)?\n- What combinations haven't been tried?\n- What mistakes should we avoid?\n\n## Output format\n\nOutput a JSON object with these sections:\n{\n  \"innovation_patterns\": [\n    {\"pattern\": \"name\", \"description\": \"how it works\", \"examples\": [\"paper1\", \"paper2\"], \"success_rate\": \"high/medium/low\"}\n  ],\n  \"reviewer_preferences\": [\n    \"What reviewers in this area consistently care about (based on evidence from paper analyses)\"\n  ],\n  \"field_gaps\": [\n    {\"gap\": \"description of unsolved problem\", \"evidence\": \"which papers mention this limitation\", \"difficulty\": \"high/medium/low\", \"impact_if_solved\": \"high/medium/low\"}\n  ],\n  \"untried_combinations\": [\n    {\"idea_sketch\": \"what could be combined\", \"from_papers\": [\"which papers inspire this\"], \"why_promising\": \"reason\"}\n  ],\n  \"method_building_blocks\": [\n    {\"tool\": \"name\", \"what_it_does\": \"description\", \"used_by\": [\"papers\"], \"could_be_applied_to\": \"new application\"}\n  ],\n  \"common_pitfalls\": [\n    \"Mistakes to avoid when working in this area (based on reviewer feedback and paper limitations)\"\n  ],\n  \"field_trajectory\": \"Where is this field heading? What are the 2-3 most promising macro-directions? (paragraph)\",\n  \"meta_advice\": \"If you were advising a PhD student to write a strong 2026 paper in this area, what would you tell them? (paragraph)\"\n}\n\nBe specific and evidence-based — every claim should reference specific papers from the analyses. Avoid generic advice like 'be novel' — instead say 'Papers that combine X with Y for task Z have been getting accepted (see Paper A, Paper B).'.\n\nIMPORTANT: You MUST end your response with the JSON object."
}
```

---

### Runtime record

_source line 2 · 2026-05-29T05:35:04.313Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T05:35:04.313Z",
  "sessionId": "f0e056d9-d209-4ed0-8a96-6ccdc25ef9c5"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-29T05:35:04.327Z_

You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.

**Today's date: 2026-05-29 (UTC).**

## Research area: Target: AAAI 2026
Track: Machine Learning (ML) — Reinforcement Learning / Mathematical Reasoning

Direction: RL-trained mathematical reasoning models exhibit 47-73% accuracy drops under trivial perturbations (numerical substitution, variable renaming) despite achieving SOTA on clean benchmarks. We propose Math-Aware Consistency Regularization (MACR): adding a JS-divergence consistency term between model outputs on original and mathematically-equivalent perturbed problems during GRPO training, with a complementary discrimination loss against surface-similar but semantically different problems. This adapts proven NLP consistency techniques (F²C, PPCL) to mathematical reasoning with math-equivalence-aware perturbation generation and RL integration — a combination no existing work provides.

Seed Papers:
- Mirzadeh et al., GSM-Symbolic (Apple, ICLR 2025) — documents up to 65% accuracy drops from single irrelevant clause; establishes that models pattern-match rather than reason
- VAR-MATH (arXiv 2025) — most damning evidence: 47.9-72.9% drops for RL models on numerically re-parameterized competition math; directly motivates why RL training is the problem
- Gao et al., AbstRaL (ICLR 2026) — only existing training-time intervention; uses abstraction not invariance; limited to GSM-level; our primary comparison baseline
- Flip-Flop Consistency / F²C (arXiv 2024) — JS-divergence consistency for prompt perturbation robustness in NLP; proves the technique works but has never been adapted to math reasoning or RL
- PPCL (EACL 2024) — KL-based consistency regularization recovering 59-69% of perturbation-induced drops in NLU; complementary theoretical grounding
- CSR: Causal Consistency Regularization (arXiv 2025) — enforces causal faithfulness via operator-level interventions during SFT; closest methodological cousin but SFT-only and targets faithfulness not perturbation invariance
- APRM (arXiv 2025) — adversarial PRM training on reasoning errors; shows PRM quality matters for downstream RL; motivates our perturbation-robust PRM extension

Known Gaps:
- No work applies consistency regularization (JS/KL divergence across equivalent problem variants) during RL training for mathematical reasoning — F²C and PPCL remain NLP-only and SFT-only
- No PRM has been trained to be robust to surface-form variations of equivalent problems — APRM addresses reasoning errors, not perturbation invariance
- No training-time robustness intervention has been demonstrated on competition-level math (AIME/Putnam); AbstRaL is GSM-only

Theoretical Anchor: Mathematical equivalence defines a natural invariance class — problems that differ only in surface form (variable names, specific numbers, phrasing) but share identical mathematical structure should produce identical solution distributions. RL training violates this invariance because the reward signal (correct/incorrect final answer) provides no gradient against surface-form-dependent reasoning. A consistency regularization term explicitly penalizes policy divergence across equivalent variants, forcing the model to learn representations that are invariant to mathematically irrelevant features. This is a direct instantiation of Invariant Risk Minimization principles in the RL-for-reasoning setting.

Constraints:
- Compute: ≤200 H100-hours (budget: 40h baseline GRPO + 90h method variants + 30h evaluation + 20h analysis + 20h buffer)
- Models: Primary experiments on 7B (Qwen2.5-Math-7B); scaling verification on 14B
- Evaluation: GSM-Symbolic, GSM-Plus, VAR-MATH (AMC23/AIME24/AIME25), MATH-Perturb; train-time perturbations (numerical substitution, variable renaming) held out from eval perturbations (distractor insertion, structural changes)

Quality Self-Checks:
- [x] Core insight: RL training optimizes for reward on fixed problem forms, creating surface-form dependencies that consistency regularization can break by enforcing invariance across equivalent variants.
- [x] Why not obvious: Consistency regularization is well-known in NLP but requires math-aware equivalence-preserving perturbation generation (not just paraphrase) and RL integration (not just SFT) — two non-trivial adaptations that straddle communities.
- [ ] Baseline fear test: A pure data-augmentation baseline (adding perturbed problems to RL training without consistency loss) could achieve substantial gains. The paper MUST include this baseline and show the consistency term provides additional benefit beyond augmentation. If the gap is <5%, the contribution is weak.
- [x] Information exploited: Mathematical equivalence structure — the method uses symbolic verification that perturbations preserve the problem's mathematical structure, which pure augmentation or paraphrase-based consistency ignores.

Avoid:
- Framing this as 'just data augmentation with extra steps' — the consistency objective is the contribution, not the perturbation generation. Must clearly show augmentation-only baseline is insufficient.
- Over-claiming generality without testing on held-out perturbation types — the key differentiator from augmentation is transfer to unseen perturbation types, so this MUST be demonstrated.
- Testing only on GSM-level math — this repeats AbstRaL's limitation and loses the competition-math differentiator.
- Ignoring clean accuracy — if MACR degrades unperturbed accuracy by >2 points, reviewers will question practicality.

## Paper analyses (22 papers)

[
  {
    "title": "GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models",
    "venue": "ICLR 2025 (Poster)",
    "problem_identification": "GSM8K is a static benchmark vulnerable to contamination and overfitting, providing no mechanism to test whether models are robust to superficial changes — yet it is the dominant math reasoning evaluation. The authors showed 21/25 models had statistically inflated GSM8K scores vs. parameterized variants.",
    "key_insight": "Converting fixed benchmarks into symbolic templates with parameterized variables (names, numbers, clauses) enables controlled measurement of reasoning invariance — revealing that LLMs pattern-match rather than reason, as evidenced by up to 65% accuracy drops from a single irrelevant clause (GSM-NoOp).",
    "innovation_type": "new_benchmark",
    "method_summary": "100 GSM8K questions were manually converted into symbolic templates parameterizing names, numerical values, and object descriptors with validity constraints. 50 instantiations per template yield 5,000 examples across 50 parallel datasets. Three perturbation types (name-only, number-only, combined) plus difficulty scaling (GSM-M1/P1/P2) and the novel GSM-NoOp (inserting a single mathematically irrelevant clause) systematically probe fragility. Statistical significance is assessed via one-sample t-tests.",
    "limitations_and_open_questions": "Post-publication audit (Sturgeon 2026) found only 12.4% of GSM-NoOp distractors were truly unambiguous, with drops becoming insignificant for frontier models on clean distractors. Templates cover only grade-school math; no competition-level extension. Reviewer criticism of statistical methodology (Ivanova analysis) reduced the '21/25 significant' claim to ~3-4 models.",
    "building_blocks": [
      "GSM-Symbolic parameterized templates",
      "GSM-NoOp distractor insertion methodology",
      "Performance variance measurement across instantiations",
      "Symbolic template generation with validity constraints"
    ],
    "relevance_to_seed": "Foundational benchmark establishing the fragility phenomenon MACR aims to fix; GSM-Symbolic serves as a primary evaluation target, though the GSM-NoOp findings may be less damning than originally claimed."
  },
  {
    "title": "Prompt Perturbation Consistency Learning for Robust Language Models",
    "venue": "EACL 2024 Findings",
    "problem_identification": "LLMs suffer 13-41% performance drops on intent classification and slot filling under realistic perturbations (ASR oronyms, synonyms, paraphrases), and standard data augmentation requires 10x more perturbed samples to achieve comparable recovery because it treats each augmented example independently, ignoring semantic equivalence.",
    "key_insight": "Augmented data should not merely add training volume — a JS-divergence consistency term between output distributions on clean and perturbed inputs extracts alignment signal that raw augmentation misses, recovering 59-69% of perturbation-induced drops with only 1/10th the augmented data.",
    "innovation_type": "new_technique",
    "method_summary": "For each clean input x_c and its perturbed counterpart x_p (generated via oronym substitution, synonym replacement, or paraphrase with BERTScore≥0.85 filtering), the model produces token-level softmax distributions. The training loss combines three terms: L = λ₁·CE(clean) + λ₂·CE(perturbed) + λ₃·JS(ŷ_c ∥ ŷ_p), where JS divergence is computed token-by-token for length-preserving perturbations or over averaged distributions for paraphrases. Ablations confirm all three terms are necessary.",
    "limitations_and_open_questions": "Evaluated only on NLU tasks (IC/SF) with discriminative-style outputs, not generative reasoning. Paraphrase perturbation is the hardest case due to length-mismatch requiring averaged distributions. Never tested in RL training or on mathematical reasoning — the two key adaptations MACR requires.",
    "building_blocks": [
      "JS-divergence consistency loss formulation",
      "Three-term loss architecture (clean CE + perturbed CE + consistency)",
      "BERTScore-based semantic equivalence filtering",
      "10x data efficiency over pure augmentation"
    ],
    "relevance_to_seed": "Direct theoretical ancestor of MACR's consistency objective; the JS-divergence formulation and data-efficiency advantage over augmentation are the core claims MACR must replicate in the math-RL setting."
  },
  {
    "title": "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning",
    "venue": "Nature 2025",
    "problem_identification": "Existing reasoning approaches required expensive human-annotated chain-of-thought trajectories, creating a scalability bottleneck and constraining models to mimic human reasoning patterns rather than discovering potentially superior strategies.",
    "key_insight": "Final-answer rewards alone, without process supervision or human-written reasoning traces, suffice to grow genuine reasoning behaviors (self-reflection, backtracking, verification) via pure RL — demonstrated by R1-Zero improving from 15.6% to 71.0% on AIME 2024.",
    "innovation_type": "scaling",
    "method_summary": "GRPO eliminates the value network by normalizing rewards within groups: A_i = (r_i - mean(r))/std(r) for G sampled outputs per prompt, combining clipped PPO ratios with KL penalty against a reference policy. The full pipeline has four stages: cold-start SFT on curated R1-Zero outputs, reasoning RL with rule-based rewards on verifiable tasks, rejection sampling + SFT for quality broadening, and diverse RL with hybrid rewards. Only accuracy and format rewards are used — no process reward model.",
    "limitations_and_open_questions": "GRPO optimizes purely for final-answer correctness, providing no gradient against surface-form-dependent reasoning — exactly the vulnerability MACR targets. Language mixing and readability degradation in pure RL motivate the cold-start stage. The group-relative advantage normalization (dividing by std) is later shown by MathForge to suppress updates for very easy and very hard problems.",
    "building_blocks": [
      "GRPO algorithm (group sampling, relative advantage, no value network)",
      "Four-stage training pipeline",
      "Rule-based verifiable rewards",
      "KL-divergence reference policy regularization"
    ],
    "relevance_to_seed": "The training paradigm MACR augments — GRPO's reward structure provides no invariance pressure, making it the precise point where consistency regularization must be injected."
  },
  {
    "title": "Harder Is Better: Boosting Mathematical Reasoning via Difficulty-Aware GRPO and Multi-Aspect Question Reformulation (MathForge)",
    "venue": "ICLR 2026 (Poster)",
    "problem_identification": "Standard GRPO's advantage normalization (dividing by std) produces maximum update magnitudes for ~50% accuracy questions while suppressing updates for both easy and hard problems — formally proved in Theorem 1. Existing augmentation adds diversity but not systematic difficulty.",
    "key_insight": "Replacing std with mean absolute deviation (MAD) in advantage normalization yields constant total update magnitude regardless of difficulty, and coupling this with answer-preserving difficulty-increasing reformulation creates a synergistic data-algorithm loop yielding +4.56% average improvement.",
    "innovation_type": "combination",
    "method_summary": "DGPO uses MAD normalization (A_i = (r_i - mean(r))/MAD(r)) ensuring difficulty-balanced updates, plus softmax question-level weighting prioritizing harder problems. MQR reformulates questions along three aspects — background (narrative context), term (abstract terminology), sub-problem (nested conditions) — all preserving gold answers for 4x dataset expansion. Best results use o3 as reformulator (~$184 for 22.5K questions).",
    "limitations_and_open_questions": "No evaluation of adversarial robustness, perturbation consistency, or out-of-distribution resilience — only clean accuracy on standard benchmarks. Ablations show ~75% of gains come from MQR augmentation alone (+3.43% vs +4.56% combined), raising questions about DGPO's marginal contribution. Best reformulation requires frontier model (o3).",
    "building_blocks": [
      "MAD-based difficulty-balanced advantage estimation",
      "Answer-preserving question reformulation (3 aspects)",
      "Difficulty-aware question-level weighting",
      "Formal analysis of GRPO update magnitude imbalance"
    ],
    "relevance_to_seed": "Key 'augmentation-only' baseline: MQR represents the strongest form of augmentation+RL without consistency objectives. MACR must demonstrate gains beyond what MQR-style difficulty augmentation achieves, and should test whether MathForge models are robust to perturbations (likely not, since robustness was never evaluated)."
  },
  {
    "title": "Beyond Correctness: Learning Robust Reasoning via Transfer (RLTR)",
    "venue": "arXiv 2026",
    "problem_identification": "RLVR optimizes solely for final-answer correctness and actually *degrades* multi-sample consistency — on MATH-500, Maj@16 drops from 81.2% (base) to 80.2% (after RLVR), revealing that accuracy gains come at the cost of reasoning brittleness.",
    "key_insight": "Robust reasoning should be transferable: if a partial reasoning prefix can guide a separate frozen receiver model to the correct answer, the reasoning is genuinely stable and interpretable rather than relying on model-specific shortcuts.",
    "innovation_type": "new_formulation",
    "method_summary": "The generator produces a reasoning trace, which is truncated at random ratio τ~Uniform(0.3,0.9). A frozen receiver model (e.g., Qwen2.5-3B) attempts completion from the prefix. Transfer reward R_trans=1 if the receiver reaches the correct answer. Combined reward: R = R_RLVR + t·R_trans (t=1.0). Training uses GRPO on 3K MATH problems. The ~7% per-step overhead is offset by 2.5x fewer steps to convergence, with net ~57% compute reduction.",
    "limitations_and_open_questions": "Robustness is defined as cross-model transferability of reasoning traces, not invariance under input perturbation — these are complementary but distinct mechanisms. No evaluation on perturbed inputs (GSM-Symbolic, VAR-MATH). The receiver model choice and truncation ratio sensitivity are not thoroughly ablated. Potential circularity: receiver quality bounds what transfer reward can measure.",
    "building_blocks": [
      "Transfer reward via cross-model prefix completion",
      "Random truncation ratio for robustness",
      "Empirical evidence that RLVR degrades Maj@K consistency",
      "Demonstration of 2.5x training efficiency gain"
    ],
    "relevance_to_seed": "Most directly comparable work addressing reasoning robustness in RL training. RLTR's transfer-based robustness is complementary to MACR's invariance-based approach — the two could potentially be combined. RLTR's finding that RLVR degrades consistency strongly motivates MACR's intervention."
  },
  {
    "title": "Toward Automated Robustness Evaluation of Mathematical Reasoning (MaSTer)",
    "venue": "ACL 2026 Findings",
    "problem_identification": "Existing robustness benchmarks (GSM-Plus, GSM-Symbolic) rely on hand-crafted templates or fixed perturbation rules that lack model-adaptivity, are susceptible to contamination, and underutilize target-model characteristics — producing incomplete vulnerability assessments.",
    "key_insight": "Reframing LLM robustness evaluation as software stress testing enables a dynamic adversarial loop where the rewriter self-discovers perturbation strategies through multi-round feedback, achieving 15-45pp higher failure rates than static benchmarks without requiring predefined perturbation rules.",
    "innovation_type": "new_benchmark",
    "method_summary": "Three-component loop: a Rewriter (Qwen2.5-32B, temp=1.0) generates adversarial variants without prescribed rules, a Verifier validates semantic equivalence and checks target failure (98% precision), and the Target model is queried at temp=0. N=5 parallel streams each run K=3 iterations (15 attempts/problem), with cumulative conversation history enabling strategy refinement. Generated variants also serve as training data: SFT on 3,678 variants reduced target failure rate by 13.3 points.",
    "limitations_and_open_questions": "Verifier relies on LLM judgment for semantic equivalence rather than symbolic verification — the 98% precision leaves room for false positives at scale. Generated perturbations are model-specific by design, potentially limiting generalizability as training data. Computational cost (32-61s/problem on 4×4090) may limit large-scale training data generation.",
    "building_blocks": [
      "Multi-round rewrite-verify adversarial loop",
      "Model-adaptive perturbation discovery (no predefined rules)",
      "Dual-use framework (evaluation + training data generation)",
      "Cross-domain extension to MMLU/CommonsenseQA"
    ],
    "relevance_to_seed": "Complementary to MACR as both evaluation tool and perturbation generator — MaSTer's self-discovered perturbations could provide diverse training-time variants, while its adversarial evaluation could stress-test MACR-trained models beyond fixed benchmarks."
  },
  {
    "title": "VAR-MATH: Probing True Mathematical Reasoning in LLMs via Symbolic Multi-Instance Benchmarks",
    "venue": "arXiv 2025",
    "problem_identification": "Existing math benchmarks use fixed numerical instances, conflating memorization with reasoning; RL-trained models show inflated scores due to benchmark contamination and surface-form overfitting. The authors identified this by observing that models achieving near-perfect scores fail when numbers change.",
    "key_insight": "Converting fixed competition problems into parameterized symbolic templates with constrained variable domains enables all-or-nothing evaluation across multiple instantiations, exposing whether models generalize across mathematically equivalent variants.",
    "innovation_type": "new_benchmark",
    "method_summary": "A four-stage pipeline: (1) structural analysis of algebraic relationships, (2) symbolic parameterization replacing numerical constants with constrained variables, (3) parametric solution formulation verified by hand as symbolic functions, (4) precision specification for numerical stability. The strict evaluation metric requires correct answers on ALL instantiations of a template. Applied to AMC23, AIME24, AIME25 to create VAR-AMC23/AIME24/AIME25.",
    "limitations_and_open_questions": "Templates require manual expert construction (not scalable); only numerical re-parameterization is tested — structural or phrasing perturbations are unexplored. Frontier models (DeepSeek-R1) show only 3.6-24.8% drops, suggesting the problem may be scale-dependent.",
    "building_blocks": [
      "VAR-AMC23/AIME24/AIME25 benchmarks",
      "Symbolic template methodology",
      "Strict all-or-nothing evaluation metric",
      "Quantified fragility evidence for RL-trained models"
    ],
    "relevance_to_seed": "Provides the primary empirical motivation for MACR: 47.9-72.9% accuracy drops for RL models on numerically re-parameterized competition math directly justify why consistency regularization during RL training is needed."
  },
  {
    "title": "Causal Consistency Regularization: Training Verifiably Sensitive Reasoning in Large Language Models",
    "venue": "arXiv 2025",
    "problem_identification": "Models produce correct answers from logically invalid reasoning traces (unfaithful reasoning), with 36-42% of correct outputs relying on spurious shortcuts. Identified via counterfactual sensitivity testing: swapping operators in valid traces and checking if answers change appropriately.",
    "key_insight": "A learned editor (6-layer Transformer trained via REINFORCE) can generate minimal, causally significant operator-level interventions that, combined with a KL-divergence penalty between original and counterfactual output distributions, forces genuine causal dependence between reasoning steps and answers during SFT.",
    "innovation_type": "new_technique",
    "method_summary": "CSR adds ℒ_total = ℒ_task − λ·D_KL(p(Y|T,X) ∥ p(Y|T',X)) where T' is a minimally perturbed counterfactual trace. The learned editor generates perturbations optimizing validity-breaking, impact-maximizing, and minimality objectives. A warm-start curriculum progressively introduces the CSR loss, and token-subset optimization applies regularization only to high-impact positions, reducing overhead from 92.5% to ~9%.",
    "limitations_and_open_questions": "Explicitly SFT-only — no RL integration demonstrated. Targets faithfulness (answer should change when reasoning breaks) rather than invariance (answer should stay same when problem surface-form changes). Tested on GSM8K-level math, not competition-level.",
    "building_blocks": [
      "KL-divergence consistency loss formulation",
      "Learned perturbation editor architecture",
      "Warm-start curriculum for regularization",
      "Token-subset optimization for efficiency"
    ],
    "relevance_to_seed": "Closest methodological cousin — MACR adapts the same core idea (divergence penalty between original and perturbed outputs) but inverts the direction (enforcing invariance not sensitivity), targets problem perturbations not trace perturbations, and integrates with RL not SFT."
  },
  {
    "title": "DAPO: An Open-Source LLM Reinforcement Learning System at Scale",
    "venue": "NeurIPS 2025",
    "problem_identification": "Reproducing RL training for reasoning LLMs is blocked by undisclosed implementation details; naive GRPO/PPO suffer entropy collapse, wasted gradient computation on trivially solved/unsolvable prompts, length instability, and reward noise from truncated sequences.",
    "key_insight": "Four orthogonal, individually-ablatable engineering innovations — asymmetric clipping (Clip-Higher, ε_low=0.2, ε_high=0.28), dynamic sampling filtering mixed-outcome groups only, token-level loss normalization, and graduated overlong reward shaping — together resolve entropy collapse and achieve SOTA with 50% fewer training steps.",
    "innovation_type": "combination",
    "method_summary": "DAPO modifies GRPO with: (1) Clip-Higher decouples upper/lower clipping bounds to prevent entropy collapse while maintaining downward pressure; (2) Dynamic Sampling oversamples then filters to keep only groups with mixed correct/incorrect responses, ensuring non-zero advantages; (3) Token-level loss normalization weights each token equally regardless of sequence length; (4) Overlong Reward Shaping uses a graduated penalty zone instead of binary truncation penalties. Achieves 50 AIME 2024 points with Qwen2.5-32B.",
    "limitations_and_open_questions": "No robustness evaluation — AIME 2024 scores may reflect contamination (per MathArena). Engineering-focused with limited theoretical analysis of why each component works. Does not address surface-form fragility at all.",
    "building_blocks": [
      "DAPO training algorithm as GRPO replacement",
      "Clip-Higher for entropy preservation",
      "Dynamic Sampling for gradient efficiency",
      "Open-source verl-based training infrastructure"
    ],
    "relevance_to_seed": "Primary baseline RL algorithm for MACR experiments; MACR's consistency term provides complementary entropy preservation to Clip-Higher, and MACR could be implemented as an add-on to DAPO's training pipeline."
  },
  {
    "title": "The Choice of Divergence: A Neglected Key to Mitigating Diversity Collapse in Reinforcement Learning with Verifiable Reward (DPH-RL)",
    "venue": "arXiv 2025 (ICLR 2026 Poster)",
    "problem_identification": "RLVR improves Pass@1 but degrades Pass@k due to diversity collapse — the policy narrows to single solution modes. Root cause: reverse-KL divergence (used in GRPO/PPO) is mode-seeking, actively suppressing low-probability solution paths.",
    "key_insight": "Mass-covering f-divergences (forward-KL, JS) function as a rehearsal mechanism that forces continuous revisitation of the reference policy's solution space, preventing diversity collapse without sacrificing Pass@1 gains.",
    "innovation_type": "new_formulation",
    "method_summary": "DPH-RL uses a two-stage approach: (1) pre-sampling partitions data into mastered (D_pef) and challenging (D_exp) sets; (2) online training applies standard PPO-clip with no KL penalty on D_exp for aggressive exploration, while applying forward-KL or JS-divergence penalties on D_pef to maintain knowledge. The combined objective L_DPH-RL = L_exp + η·L_pef balances exploration and retention. Critically, f-divergence is computed via generator functions requiring only reference policy samples, eliminating online reference model overhead.",
    "limitations_and_open_questions": "The two-stage data partitioning adds pipeline complexity. Results primarily on SQL (Bird) and math with Llama-8B — scaling to larger models and harder benchmarks is unverified. Does not address surface-form robustness, only solution diversity.",
    "building_blocks": [
      "JS-divergence formulation in RL-for-reasoning context",
      "Forward-KL as rehearsal mechanism",
      "Two-stage mastered/challenging data partitioning",
      "Theoretical monotonic improvement guarantee for mass-covering divergences"
    ],
    "relevance_to_seed": "Directly validates JS-divergence as a viable regularizer in RL-for-reasoning, which MACR's consistency term also uses. DPH-RL applies JS between current and reference policy distributions; MACR applies JS between outputs on original and perturbed problems — complementary applications of the same divergence."
  },
  {
    "title": "Generative Adversarial Reasoner: Enhancing LLM Reasoning with Adversarial Reinforcement Learning (GAR)",
    "venue": "ICLR 2026",
    "problem_identification": "Sparse outcome-level rewards (correct/incorrect final answer) provide poor credit assignment for long reasoning chains, failing to distinguish partially-correct reasoning from fully flawed attempts. Existing PRMs are static and don't co-evolve with the policy.",
    "key_insight": "Co-evolving a discriminator and reasoner through adversarial RL — where the discriminator evaluates reasoning chain slices for logical soundness and provides dense step-level rewards — creates an adaptive, increasingly challenging training signal that improves credit assignment without external annotation.",
    "innovation_type": "new_technique",
    "method_summary": "GAR partitions reasoning chains into logically complete slices (~320 tokens) and trains a discriminator to evaluate each slice's soundness with structured justifications. The reasoner's reward combines exact-match and mean slice scores: R_rea = λ₁R_m + λ₂R_s. The discriminator optimizes R_dis = λ₃R_d + λ₄R_a, combining GAN-style discrimination (real vs. generated slices) and alignment (slice judgments must be consistent with answer correctness, preventing reward hacking). Both are trained via GRPO. Discriminator output is capped at 128 tokens, reducing training from 43h to 19h.",
    "limitations_and_open_questions": "Adversarial co-training introduces instability risks and hyperparameter sensitivity (four λ weights). No robustness evaluation — gains may reflect better optimization not better reasoning. The discriminator's quality ceiling limits reasoner improvement.",
    "building_blocks": [
      "Slice-based reasoning chain decomposition",
      "Adversarial co-training framework for reasoner+discriminator",
      "Dense step-level reward from LLM discriminator",
      "Alignment reward as anti-reward-hacking regularizer"
    ],
    "relevance_to_seed": "GAR's discriminator provides an alternative to MACR's consistency loss for improving reasoning quality during RL. The slice-based evaluation could complement MACR — a perturbation-robust discriminator (GAR + MACR's invariance objective) would provide both dense and robust rewards."
  },
  {
    "title": "MathArena: Evaluating LLMs on Uncontaminated Math Competitions",
    "venue": "NeurIPS 2025 Datasets & Benchmarks",
    "problem_identification": "AIME 2024 and other standard math benchmarks are contaminated in training data, inflating reported scores and making it impossible to distinguish memorization from reasoning. Detected by comparing model performance on widely-available vs. freshly-released competition problems.",
    "key_insight": "Recurring math competitions provide a natural stream of expert-curated, pre-vetted, uncontaminated problems; evaluating models immediately upon problem release (before web dissemination) creates a contamination-proof evaluation methodology.",
    "innovation_type": "new_benchmark",
    "method_summary": "MathArena aggregates 162 problems from seven recent competitions (AMC, AIME, CMIMC, HMMT, Putnam, IMO, etc.), evaluating 50+ models in real-time as competitions occur. The framework includes the first systematic proof-writing evaluation, where models must produce valid mathematical proofs scored against competition rubrics. Contamination analysis compares performance on pre-2024 (potentially contaminated) vs. post-2024 (clean) problems, finding statistically significant inflation on AIME 2024.",
    "limitations_and_open_questions": "Competition problems have limited volume (tens per competition per year) and skew toward specific mathematical styles. Real-time evaluation creates a moving target — historical comparisons become difficult. Proof evaluation requires expert judges, limiting scalability.",
    "building_blocks": [
      "Contamination-free competition math benchmark",
      "Real-time evaluation methodology",
      "AIME 2024 contamination evidence",
      "Proof-writing evaluation framework"
    ],
    "relevance_to_seed": "Critical for interpreting MACR's results: AIME 2024 is contaminated, so MACR must report on both AIME24 (with caveat) and cleaner benchmarks (AIME25, CMIMC). MathArena's methodology validates using recent competitions for evaluation, supporting MACR's use of VAR-MATH variants."
  },
  {
    "title": "AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking",
    "venue": "ICLR 2026",
    "problem_identification": "LLMs suffer severe accuracy drops under GSM perturbations (numerical changes, distractors) because they pattern-match on surface forms rather than reasoning abstractly. The authors identified this by connecting GSM-Symbolic fragility evidence to the observation that SFT-trained abstraction produces unfaithful outputs, implying RL is necessary.",
    "key_insight": "Abstraction — converting concrete math problems into symbolic variable-operator representations — is a learnable skill better acquired through RL (GRPO with symbolic-distance rewards) than SFT, and this single capability broadly transfers to OOD mathematical and general reasoning tasks.",
    "innovation_type": "new_technique",
    "method_summary": "Constructs GranulAR data by having an oracle LLM decompose GSM problems into abstract representations with symbolic variables (in0, in1, out0), verified via SymPy. Trains models with GRPO using two rewards: binary answer correctness (r_answer) and a continuous symbolic edit-distance reward (r_symbolic) measuring closeness to gold abstraction. The contextualized learning pipeline (problem → abstract question → abstract answer → abstraction) is critical — ablations show direct abstraction generation collapses performance.",
    "limitations_and_open_questions": "Limited to GSM-level math (no competition-level evaluation); requires full model tuning limiting scalability; theoretical grounding for why abstraction helps OOD transfer is acknowledged as an open problem. Does the approach survive harder math where abstraction patterns are less formulaic?",
    "building_blocks": [
      "GranulAR data pipeline for abstraction generation",
      "Symbolic edit-distance reward for GRPO",
      "SymPy-based abstraction verification",
      "Contextualized multi-step learning format"
    ],
    "relevance_to_seed": "Primary comparison baseline for MACR: AbstRaL addresses the same robustness problem but via abstraction rather than invariance-enforcing consistency regularization, and its GSM-only evaluation scope is exactly the gap MACR targets with competition-level math."
  },
  {
    "title": "Adversarial Training for Process Reward Models",
    "authors": "Juneja et al.",
    "venue": "arXiv 2025 (desk rejected at venue submission)",
    "problem_identification": "PRMs trained on static datasets with fixed negative examples fail to generalize to novel reasoning errors, and collecting step-level human annotations is prohibitively expensive. The authors identified this by observing that existing PRMs overfit to the error distribution in their training data.",
    "key_insight": "An adversarial generator-discriminator loop creates an automatic curriculum of increasingly sophisticated reasoning errors, eliminating the need for manual step-level annotation while producing PRMs that generalize better to unseen error types.",
    "innovation_type": "new_technique",
    "method_summary": "Generator G (Llama-3.1-8B) takes correct reasoning steps and produces corrupted variants rewarded (+1) for deceiving PRM R, penalized (-1) for producing correct steps. R trains on 50/50 mix of gold and adversarial negatives. Optimization uses alternating PPO (5 steps each) stabilized by Optimistic Gradient Descent-Ascent (OGDA) for convergence toward Nash equilibrium, with KL and entropy regularization preventing mode collapse. A non-LLM correctness oracle (cosine similarity + entity matching) avoids human annotation dependency.",
    "limitations_and_open_questions": "2-3× computational cost over standard PRM training; adversarial examples may concentrate in few exploit classes risking overfitting; desk rejected suggesting concerns about novelty or rigor. How does adversarial PRM training interact with perturbation-invariance — does the generator learn to exploit surface-form sensitivity?",
    "building_blocks": [
      "OGDA-stabilized adversarial RL for reward model training",
      "Non-LLM correctness oracle for annotation-free PRM training",
      "Progressive hard-negative curriculum generation"
    ],
    "relevance_to_seed": "Motivates MACR's perturbation-robust PRM extension: APRM shows adversarial training improves PRM generalization (+5.3pp OOD), but targets reasoning errors rather than surface-form invariance — combining APRM's adversarial framework with MACR's equivalence-preserving perturbations is a natural extension."
  },
  {
    "title": "MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations",
    "venue": "ICML 2025",
    "problem_identification": "Prior perturbation benchmarks (GSM-Symbolic, GSM-Plus) only tested simple perturbations preserving solution methods, missing the harder case where small problem modifications fundamentally change the required approach. Identified by noting that no benchmark distinguished method-preserving from method-changing perturbations at competition difficulty.",
    "key_insight": "The critical distinction is between simple perturbations (same method, different numbers) and hard perturbations (small textual changes that invalidate the original solution strategy), with the latter revealing a more insidious memorization pattern: models blindly apply learned solution templates without checking applicability.",
    "innovation_type": "new_benchmark",
    "method_summary": "Constructs 558 perturbed problems (279 simple, 279 hard) from MATH Level-5, verified by 12 PhD-level math experts. Simple perturbations change values/constraints while preserving solution methods; hard perturbations make minimal edits that require entirely different approaches. Evaluates 20+ models finding severe drops on hard perturbations (o1-mini: -16.5%, GPT-4o: -27.6%) and a novel memorization signature: ICL with original solutions actively hurts performance (18-40% problems flip to incorrect), proving models apply memorized templates rather than reasoning.",
    "limitations_and_open_questions": "Only 279 problems per category — small benchmark size limits statistical power. No training-time mitigation proposed, only diagnosis. The simple/hard dichotomy may miss intermediate perturbation difficulties. How do RL-trained models specifically compare to SFT models on hard perturbations?",
    "building_blocks": [
      "558 expert-verified Level-5 perturbed math problems",
      "Simple vs. hard perturbation taxonomy",
      "ICL-based memorization detection methodology"
    ],
    "relevance_to_seed": "Directly in MACR's evaluation suite: MATH-Perturb provides competition-level perturbation evaluation that AbstRaL lacks, and its hard perturbations test whether MACR's consistency training transfers to unseen perturbation types (method-changing variants not seen during training)."
  },
  {
    "title": "Process Reward Models That Think (ThinkPRM)",
    "venue": "arXiv 2025 (withdrawn from ICLR 2026)",
    "problem_identification": "Discriminative PRMs require ~800K expensive step-level human labels yet still underperform on OOD tasks, while LLM-as-Judge approaches lack controllable compute scaling. The authors identified this gap by recognizing that reasoning models already have verification capabilities that can be elicited with minimal fine-tuning.",
    "key_insight": "A reasoning model fine-tuned on just 1K synthetic verification chain-of-thought examples can outperform discriminative PRMs trained on 100× more data, because generative verification leverages the model's pre-existing reasoning capacity rather than learning a separate classification head.",
    "innovation_type": "simplification",
    "method_summary": "Samples verification CoTs from QwQ-32B-Preview on PRM800K problem-solution pairs, filters by format compliance, label agreement with gold annotations, and <4096 token length to avoid overthinking. Fine-tunes R1-Distill-Qwen models (1.5B–14B) with standard language modeling loss on ~1K filtered examples (~8K process labels). At inference, scores each step via conditional probability of 'correct' vs 'incorrect' tokens after generating verification reasoning. Supports compute scaling through parallel (multiple independent CoTs) and sequential (longer thinking) modes.",
    "limitations_and_open_questions": "Withdrawn from ICLR 2026, suggesting potential concerns about evaluation rigor or novelty. Step label interference (earlier judgments biasing later ones) is acknowledged but not fully solved. Verification CoT quality depends on seed reasoning model capability. Is ThinkPRM robust to surface-form variations of mathematically equivalent problems?",
    "building_blocks": [
      "Verification CoT data synthesis pipeline from reasoning models",
      "Generative step-level scoring via token probabilities",
      "Parallel/sequential compute scaling for verification"
    ],
    "relevance_to_seed": "Relevant to MACR's perturbation-robust PRM extension: ThinkPRM's data-efficient generative verification framework could be combined with equivalence-preserving perturbation training to create PRMs that verify reasoning consistency across problem variants, not just step correctness."
  },
  {
    "title": "Scaling Behaviors of LLM Reinforcement Learning Post-Training: An Empirical Study in Mathematical Reasoning",
    "venue": "ACL 2026",
    "problem_identification": "While pre-training scaling laws (Chinchilla, Kaplan) are well-established, RL post-training scaling behavior was entirely uncharacterized — practitioners had no principled way to allocate compute between model size and training steps for RL fine-tuning. Identified by noting this gap in the scaling laws literature as RL post-training became standard practice.",
    "key_insight": "RL post-training follows predictable power-law scaling (R²>0.99) in test loss vs. compute and data, but with a critical saturation effect: learning efficiency k(N) asymptotically approaches K_max, meaning larger models yield diminishing marginal returns beyond ~32B parameters.",
    "innovation_type": "scaling",
    "method_summary": "Conducts 63 GRPO fine-tuning experiments across Qwen2.5 (0.5B–72B) on 50K+ math problems with 3 repetitions each. Fits power-law models: log L(N,X) = -k(N)·log X + E(N) where k(N) = K_max/(1+N₀/N) captures efficiency saturation. Validates cross-architecture on Llama-3 (1B–70B). Key practical finding: data reuse up to 25× shows no degradation when total optimization steps are held constant, meaning performance is step-governed not uniqueness-governed. Inter-model extrapolation from 0.5B–32B accurately predicts 72B performance.",
    "limitations_and_open_questions": "Only studies GRPO — do other RL algorithms (PPO, REINFORCE) follow the same scaling laws? Tested only on math reasoning — generalization to code, general reasoning unknown. Saturation analysis beyond 72B is extrapolation. How does adding auxiliary losses (like consistency regularization) affect scaling behavior?",
    "building_blocks": [
      "Power-law scaling formulations for RL post-training",
      "Efficiency saturation model k(N) = K_max/(1+N₀/N)",
      "Data reuse viability up to 25× without degradation",
      "Compute-optimal model-size/steps allocation framework"
    ],
    "relevance_to_seed": "Directly informs MACR compute budgeting: the scaling laws predict that 7B Qwen2.5-Math is near-optimal for our 200 H100-hour budget, the data reuse finding validates training on augmented (perturbed) versions of the same problems, and the saturation model helps predict whether 14B scaling verification will show meaningful gains."
  },
  {
    "title": "Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs",
    "venue": "arXiv 2025",
    "problem_identification": "LLMs produce inconsistent predictions across semantically equivalent prompt templates, undermining reliability. Identified by measuring observed agreement (PoP_o) across 4-15 prompt formats per dataset and finding large variance in predictions for identical inputs.",
    "key_insight": "Majority vote across prompt variations provides a reliable unsupervised pseudo-label, enabling self-supervised consistency training without any gold labels — the model's own consensus becomes the teaching signal.",
    "innovation_type": "new_technique",
    "method_summary": "F²C combines three losses: (1) Consensus Cross-Entropy (CCE) trains all prompt variants toward the majority-vote pseudo-label c*; (2) JSD alignment minimizes Jensen-Shannon divergence among high-confidence consensus predictions; (3) a KL flip loss pulls non-consensus predictions toward the confident-consensus mixture q̄. Cases are stratified by agreement level (unanimous/consensus/no-consensus) with adaptive weighting via sigmoid-scaled log-likelihood gaps. Training uses LoRA on Qwen2.5-3B-Instruct.",
    "limitations_and_open_questions": "Ablations show CCE dominates (+11.68% agreement alone vs +11.62% full F²C); the JSD/flip components add only marginal gains (+0.58% F1). Untested on generative tasks, math reasoning, or within RL training loops — all critical gaps for MACR adaptation.",
    "building_blocks": [
      "JS-divergence consistency loss between input variants",
      "Majority-vote pseudo-labeling without supervision",
      "Confidence-stratified case handling for alignment losses",
      "LoRA-based unsupervised consistency fine-tuning"
    ],
    "relevance_to_seed": "Direct technical ancestor of MACR: the CCE + JSD loss framework can be adapted from NLP prompt-template invariance to math-equivalence invariance, but requires replacing paraphrase-based perturbations with structure-preserving mathematical
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
  "promptId": "f2835c10-987c-4be6-9beb-11987ad7a8ae",
  "type": "user",
  "uuid": "b34fc98e-b299-44a4-a066-0c64debbb5ea",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f0e056d9-d209-4ed0-8a96-6ccdc25ef9c5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T05:35:04.325Z_

```json
{
  "parentUuid": "b34fc98e-b299-44a4-a066-0c64debbb5ea",
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
  "uuid": "073043aa-8472-4740-a0c3-a45794c4c544",
  "timestamp": "2026-05-29T05:35:04.325Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f0e056d9-d209-4ed0-8a96-6ccdc25ef9c5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T05:35:04.326Z_

```json
{
  "parentUuid": "073043aa-8472-4740-a0c3-a45794c4c544",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "4aaeaef2-5716-4810-808c-6173796c0dc7",
  "timestamp": "2026-05-29T05:35:04.326Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f0e056d9-d209-4ed0-8a96-6ccdc25ef9c5",
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
  "leafUuid": "4aaeaef2-5716-4810-808c-6173796c0dc7",
  "sessionId": "f0e056d9-d209-4ed0-8a96-6ccdc25ef9c5"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesizing math robustness via consistency regularization",
  "sessionId": "f0e056d9-d209-4ed0-8a96-6ccdc25ef9c5"
}
```

---

### Assistant

_source line 8 · 2026-05-29T05:35:20.935Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to synthesize 22 paper analyses into a strategic "Field Guide" for innovation in the area of RL-trained mathematical reasoning robustness. Let me carefully analyze the papers and produce a comprehensive, evidence-based JSON output.

Let me organize my thinking across the required sections:

**Innovation Patterns:**
1. "Benchmark-first, then fix" - GSM-Symbolic, VAR-MATH, MATH-Perturb all diagnose the problem; AbstRaL, MACR attempt to fix
2. "Consistency/invariance regularization" - PPCL, F²C, CSR all add divergence penalties


3. "Adversarial co-training loops" - GAR, APRM, MaSTer use adversarial dynamics
4. "Engineering refinements to GRPO" - DAPO, MathForge/DGPO, DPH-RL modify the base algorithm
5. "Simplification/data efficiency" - ThinkPRM shows 1K examples can beat 100K
6. "Combining existing techniques across domains" - adapting NLP techniques to math reasoning

**Reviewer Preferences:**
- Ablation studies showing each component is necessary
- Clean accuracy preservation (not just robustness)
- Comparison with strong augmentation baselines
- Evaluation on multiple benchmarks/perturbation types
- Compute efficiency analysis

There are several unexplored areas I'm noticing: consistency regularization hasn't been applied to RL for math problems, no one's built a perturbation-robust PRM yet, and there's potential in combining diversity preservation with perturbation robustness. I'm also seeing promising untried combinations like pairing consistency regularization with adversarial dense rewards, or merging transfer robustness techniques with perturbation invariance, and I want to explore how these could work together with existing methods like adaptive perturbation generation and diversity-preserving RL. Now I'm structuring this into a detailed JSON object with evidence-based entries.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4aaeaef2-5716-4810-808c-6173796c0dc7",
  "isSidechain": false,
  "requestId": "req_011CbWKKfQkYrTCkvcWxCRWy",
  "type": "assistant",
  "uuid": "bc72883b-1630-4f39-bfef-7b7e13086975",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f0e056d9-d209-4ed0-8a96-6ccdc25ef9c5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MpzpMs522rRQ8m69WQCo1W",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13248,
      "cache_read_input_tokens": 11014,
      "output_tokens": 7719,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13248,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 7719,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 13248,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13248
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

_source line 9 · 2026-05-29T05:38:11.951Z_

I'll analyze the 22 papers carefully and synthesize them into a strategic field guide. Let me work through the key dimensions systematically.

```json
{
  "innovation_patterns": [
    {
      "pattern": "Diagnose-then-fix pipeline",
      "description": "A benchmark paper documents a systematic failure mode with controlled experiments, then a follow-up paper proposes a training-time intervention targeting that exact failure. The diagnostic paper provides both the motivation narrative and the evaluation suite for the fix paper. This two-step pattern dominates the robustness subfield.",
      "examples": ["GSM-Symbolic → AbstRaL", "VAR-MATH → (MACR opportunity)", "MATH-Perturb → (no fix yet)"],
      "success_rate": "high"
    },
    {
      "pattern": "Cross-domain technique transfer with domain-specific adaptation",
      "description": "Take a well-validated technique from one ML subfield (NLP robustness, computer vision invariance, causal inference) and adapt it to math reasoning with domain-specific modifications. The key is that the adaptation is non-trivial — requiring new perturbation generators, loss reformulations, or training loop integration — not a direct plug-in. Papers that merely apply an existing technique without meaningful adaptation get rejected.",
      "examples": ["PPCL (NLU consistency → math reasoning opportunity)", "F²C (prompt template invariance → math equivalence opportunity)", "CSR (causal inference → reasoning faithfulness)", "AbstRaL (program abstraction → math problem abstraction)"],
      "success_rate": "high"
    },
    {
      "pattern": "GRPO algorithm surgery",
      "description": "Identify a specific mathematical pathology in GRPO's objective (update magnitude imbalance, entropy collapse, mode-seeking KL, reward noise from truncation) via formal analysis, then propose a targeted surgical fix with theoretical justification. The formal proof of the pathology is as important as the fix itself — reviewers reward rigor in diagnosing the problem.",
      "examples": ["MathForge/DGPO (MAD normalization fixing std-based suppression)", "DAPO (Clip-Higher fixing entropy collapse)", "DPH-RL (forward-KL/JS replacing reverse-KL to prevent diversity collapse)"],
      "success_rate": "high"
    },
    {
      "pattern": "Adversarial co-training loops",
      "description": "Two models co-evolve: one generates increasingly challenging content (perturbations, reasoning errors, adversarial examples) while the other learns to handle them. Stabilized by techniques borrowed from GAN training (OGDA, alternating updates, alignment rewards to prevent reward hacking). The self-improving curriculum is the key selling point over static data.",
      "examples": ["GAR (reasoner + discriminator)", "APRM (generator + PRM)", "MaSTer (rewriter + verifier, though evaluation-focused)"],
      "success_rate": "medium"
    },
    {
      "pattern": "Data-efficient simplification of expensive pipelines",
      "description": "Show that a conceptually simpler approach with 10-100× less data/annotation can match or beat the expensive incumbent. Requires a clear explanation of why less is more (usually: leveraging pre-existing model capabilities rather than training new ones from scratch).",
      "examples": ["ThinkPRM (1K examples beating 800K-label PRMs)", "PPCL (1/10th augmented data with consistency loss matching 10× augmentation)", "RLTR (57% compute reduction via transfer reward)"],
      "success_rate": "high"
    },
    {
      "pattern": "Parameterized symbolic benchmarking",
      "description": "Convert fixed benchmark problems into symbolic templates with constrained variable domains, enabling controlled measurement of specific reasoning invariances via multiple instantiations. The strict all-or-nothing metric (correct on ALL instantiations) is particularly impactful because it eliminates noise from lucky guessing.",
      "examples": ["GSM-Symbolic (GSM8K templates)", "VAR-MATH (AMC/AIME templates)", "MATH-Perturb (simple/hard perturbation taxonomy)"],
      "success_rate": "high"
    }
  ],
  "reviewer_preferences": [
    "Rigorous ablation isolating each component's contribution: MathForge was questioned because 75% of gains came from augmentation alone (+3.43 vs +4.56); F²C's JSD/flip components added only 0.58% over CCE alone. Reviewers will hammer any multi-component method where one component dominates. MACR MUST show consistency loss adds meaningfully beyond augmentation-only baseline.",
    "Clean accuracy preservation as a non-negotiable: Any robustness method that degrades unperturbed performance by >2 points faces immediate reviewer skepticism about practicality. Papers like AbstRaL and RLTR carefully report clean accuracy alongside robustness gains.",
    "Formal analysis of WHY the method works, not just that it works: DGPO's Theorem 1 (proving GRPO update magnitude imbalance), DPH-RL's theoretical monotonic improvement guarantee, and the scaling laws paper's R²>0.99 power-law fits all demonstrate that reviewers reward mathematical rigor. A JS-divergence consistency term needs information-theoretic justification for why it enforces the right invariance.",
    "Transfer to unseen perturbation types as the gold standard for robustness: If a method only helps on the perturbation types it was trained on, reviewers will dismiss it as sophisticated data augmentation. MATH-Perturb's simple/hard taxonomy and the distinction between train-time and eval-time perturbation types are specifically designed to test this.",
    "Compute-awareness and reproducibility: DAPO's open-source verl infrastructure, MathForge's explicit cost reporting ($184 for o3 reformulation), and RLTR's 57% compute reduction all signal that reviewers penalize methods that are computationally intractable. The 200 H100-hour budget should be reported as a constraint, not hidden.",
    "Contamination-aware evaluation: MathArena proved AIME 2024 is contaminated. Any paper reporting AIME 2024 results without acknowledging contamination risks reviewer distrust. Use AIME25 or explicitly flag the caveat.",
    "Engagement with post-publication critiques: GSM-Symbolic's GSM-NoOp finding was undermined by Sturgeon 2026's audit (only 12.4% of distractors truly unambiguous). Reviewers increasingly check whether cited fragility evidence has been contested. Citing GSM-Symbolic without noting the Sturgeon/Ivanova critiques signals insufficient literature awareness."
  ],
  "field_gaps": [
    {
      "gap": "No consistency regularization during RL training for mathematical reasoning",
      "evidence": "PPCL and F²C demonstrate JS/KL consistency regularization for NLP robustness but are SFT-only and NLU-only. CSR applies divergence penalties during SFT but for faithfulness not invariance. DPH-RL uses JS-divergence in RL but between policy and reference, not between equivalent inputs. No paper combines math-equivalence-aware perturbations with consistency loss in an RL training loop.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "No training-time robustness intervention demonstrated on competition-level math (AIME/Putnam)",
      "evidence": "AbstRaL is GSM-only. VAR-MATH documents 47.9-72.9% drops on competition math but proposes no fix. MATH-Perturb benchmarks Level-5 perturbations but provides no training-time mitigation. MathForge evaluates on competition benchmarks but never tests robustness.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "No perturbation-robust process reward model",
      "evidence": "APRM shows adversarial training improves PRM generalization to unseen error types but targets reasoning errors not surface-form invariance. ThinkPRM provides data-efficient generative verification but was never tested on perturbed problem variants. No PRM has been evaluated on whether it gives consistent step scores for mathematically equivalent problem reformulations.",
      "difficulty": "medium",
      "impact_if_solved": "medium"
    },
    {
      "gap": "No integration of diversity preservation with perturbation robustness in RL",
      "evidence": "DPH-RL shows RLVR causes diversity collapse (Pass@k degradation); RLTR shows RLVR degrades Maj@16 consistency. Both address solution diversity but not input robustness. MACR addresses input robustness but could exacerbate diversity collapse by adding another regularization term. No work studies the interaction between these two robustness dimensions.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "No scalable, symbolic-verification-backed perturbation generation beyond numerical re-parameterization",
      "evidence": "VAR-MATH requires manual expert template construction for numerical re-parameterization only. GSM-Symbolic covers names/numbers/clauses but only at grade-school level. MaSTer generates diverse perturbations automatically but relies on LLM judgment (not symbolic verification) for equivalence, achieving 98% precision that may degrade at scale. No method combines automatic generation with formal mathematical equivalence guarantees across perturbation types.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "No characterization of how auxiliary losses (consistency regularization, transfer rewards) affect RL scaling laws",
      "evidence": "The ACL 2026 scaling laws paper (63 GRPO experiments) explicitly notes it studies only standard GRPO. Open question: does adding a consistency term change the power-law exponents, shift the compute-optimal model size, or alter the data reuse tolerance (currently viable up to 25×)?",
      "difficulty": "medium",
      "impact_if_solved": "medium"
    },
    {
      "gap": "Method-changing (hard) perturbation robustness remains entirely unaddressed at training time",
      "evidence": "MATH-Perturb distinguishes simple perturbations (same method, different numbers) from hard perturbations (small edits requiring entirely different solution strategies). All existing robustness interventions (AbstRaL, data augmentation approaches) target simple perturbations. Hard perturbation robustness may require fundamentally different approaches — possibly meta-reasoning about when a solution strategy applies rather than invariance enforcement.",
      "difficulty": "high",
      "impact_if_solved": "high"
    }
  ],
  "untried_combinations": [
    {
      "idea_sketch": "MACR consistency loss + DAPO training infrastructure: Implement JS-divergence consistency regularization as a plug-in module within DAPO's open-source verl framework, combining Clip-Higher (entropy preservation) with consistency loss (invariance enforcement) during GRPO training on math-equivalent problem pairs.",
      "from_papers": ["PPCL", "F²C", "DAPO", "DPH-RL"],
      "why_promising": "DAPO provides the strongest open-source RL infrastructure with solved entropy collapse, while DPH-RL validates JS-divergence as viable in RL-for-reasoning. The consistency term addresses an orthogonal failure mode (surface-form sensitivity) that DAPO's engineering innovations do not touch. DAPO's Dynamic Sampling (filtering for mixed-outcome groups) could naturally extend to include cross-perturbation consistency in the filtering criterion."
    },
    {
      "idea_sketch": "Perturbation-robust generative PRM via ThinkPRM + equivalence-aware training: Fine-tune ThinkPRM's data-efficient verification framework on paired (original, perturbed) problem-solution instances, adding a consistency objective requiring identical step-level verification scores for equivalent problems.",
      "from_papers": ["ThinkPRM", "APRM", "VAR-MATH"],
      "why_promising": "ThinkPRM shows 1K examples suffice for competitive PRM performance, meaning a perturbation-robust PRM extension might need only hundreds of paired examples. APRM proves adversarial PRM training yields +5.3pp OOD gains, and VAR-MATH provides the evaluation infrastructure. A PRM that gives consistent scores across equivalent problem variants would be both a standalone contribution and a building block for MACR (providing perturbation-aware dense rewards)."
    },
    {
      "idea_sketch": "RLTR transfer reward + MACR invariance objective as dual regularizers: Combine RLTR's cross-model reasoning transferability reward (reasoning should guide a frozen receiver to correct answers) with MACR's cross-perturbation consistency loss (outputs should match across equivalent problems) as complementary regularizers during GRPO training.",
      "from_papers": ["RLTR", "PPCL", "F²C"],
      "why_promising": "RLTR and MACR address orthogonal robustness dimensions: RLTR ensures reasoning is model-general (not relying on model-specific shortcuts), MACR ensures reasoning is input-general (not relying on surface-form patterns). RLTR's finding that standard RLVR degrades Maj@16 consistency provides direct evidence that additional regularization is needed, and the 2.5× training efficiency gain from transfer reward could offset MACR's computational overhead."
    },
    {
      "idea_sketch": "MaSTer's adaptive adversarial perturbation generator as MACR's training-time perturbation engine: Replace MACR's rule-based perturbation generation with MaSTer's multi-round rewrite-verify loop, creating model-adaptive perturbations that target each training model's specific weaknesses.",
      "from_papers": ["MaSTer", "PPCL", "AbstRaL"],
      "why_promising": "MaSTer achieves 15-45pp higher failure rates than static benchmarks by self-discovering perturbation strategies, meaning it generates harder training signal than rule-based perturbations. MaSTer's dual-use design (evaluation + training data) was validated with SFT (13.3pp failure rate reduction), but never tested with consistency regularization during RL — combining adaptive perturbation difficulty with an explicit invariance objective could be synergistic."
    },
    {
      "idea_sketch": "GAR's slice-based dense rewards + MACR's consistency loss: Train GAR's discriminator to provide step-level reasoning quality scores while simultaneously requiring consistency of slice scores across equivalent problem perturbations, creating a dense perturbation-robust reward signal.",
      "from_papers": ["GAR", "APRM", "CSR"],
      "why_promising": "MACR's consistency loss operates at the trajectory level (matching output distributions across perturbations), which provides sparse signal for long reasoning chains. GAR's slice-based decomposition could provide step-level consistency enforcement, catching surface-form sensitivity at individual reasoning steps rather than only at the final answer. This addresses GAR's weakness (no robustness evaluation) and MACR's potential weakness (coarse-grained consistency signal)."
    },
    {
      "idea_sketch": "DPH-RL diversity preservation + MACR invariance enforcement as a joint objective with shared JS-divergence framework: Use DPH-RL's data partitioning (mastered vs. challenging) to apply MACR's consistency regularization selectively — enforce perturbation invariance on mastered problems while allowing unconstrained exploration on challenging ones.",
      "from_papers": ["DPH-RL", "PPCL", "F²C"],
      "why_promising": "Both methods use JS-divergence but for different purposes (diversity vs. invariance), creating a natural unified framework. DPH-RL's key insight — that mastered problems need rehearsal/retention while challenging problems need exploration — directly maps to MACR's needs: consistency regularization is most meaningful for problems the model can already solve (where surface-form sensitivity is the failure mode) and potentially counterproductive for problems it cannot solve at all (where it needs exploratory freedom)."
    }
  ],
  "method_building_blocks": [
    {
      "tool": "JS-divergence consistency loss",
      "what_it_does": "Penalizes distributional divergence between model outputs on semantically equivalent inputs, forcing invariant representations. Computed token-by-token for length-preserving transformations or over averaged distributions for length-changing ones. Three-term loss architecture (clean CE + perturbed CE + JS alignment) shown to be necessary via ablation.",
      "used_by": ["PPCL", "F²C", "DPH-RL"],
      "could_be_applied_to": "Mathematical reasoning RL: replacing NLP paraphrase equivalence with math-equivalence-preserving perturbations (numerical substitution, variable renaming) and integrating the loss with GRPO's objective. The key adaptation is defining the JS computation over reasoning chain distributions (variable-length generative outputs) rather than classification logits."
    },
    {
      "tool": "GRPO with group-relative advantage estimation",
      "what_it_does": "Eliminates the value network by sampling G outputs per prompt and normalizing rewards within the group: A_i = (r_i - mean(r))/std(r). Combined with clipped PPO ratios and KL penalty against reference policy. Foundation of all RL-for-reasoning training.",
      "used_by": ["DeepSeek-R1", "DAPO", "MathForge", "AbstRaL", "GAR", "RLTR"],
      "could_be_applied_to": "Extended GRPO objective with consistency term: L = L_GRPO + λ_cons · JS(π(·|x) ∥ π(·|x̃)) where x̃ is a math-equivalent perturbation of x. The group sampling naturally supports this — generate G/2 outputs for x and G/2 for x̃, compute advantages jointly, add consistency loss."
    },
    {
      "tool": "Symbolic template parameterization with validity constraints",
      "what_it_does": "Converts fixed math problems into parameterized templates where numerical constants become constrained variables with domain restrictions ensuring problem validity. Enables generation of arbitrary numbers of mathematically equivalent problem instances from a single template.",
      "used_by": ["GSM-Symbolic", "VAR-MATH"],
      "could_be_applied_to": "Training-time perturbation generation for MACR: instead of using templates only for evaluation, use them to generate on-the-fly perturbations during RL training. SymPy-based verification (as in AbstRaL) can validate that perturbations preserve mathematical structure. The scaling laws paper's data reuse finding (up to 25× viable) suggests training on multiple instantiations of the same template is safe."
    },
    {
      "tool": "Adversarial co-training with OGDA stabilization",
      "what_it_does": "Alternating optimization of generator (producing hard examples) and discriminator (learning to handle them), stabilized by Optimistic Gradient Descent-Ascent for convergence toward Nash equilibrium, with KL and entropy regularization preventing mode collapse.",
      "used_by": ["APRM", "GAR"],
      "could_be_applied_to": "Adversarial perturbation generation during MACR training: instead of fixed perturbation rules, co-train a perturbation generator that learns to find surface-form changes that maximally violate the model's consistency, creating an adaptive curriculum of increasingly challenging equivalence-preserving perturbations."
    },
    {
      "tool": "MAD-based difficulty-balanced advantage estimation",
      "what_it_does": "Replaces standard deviation with mean absolute deviation in GRPO's advantage normalization, formally proven (Theorem 1) to yield constant total update magnitude regardless of problem difficulty, eliminating the bias toward 50%-accuracy questions.",
      "used_by": ["MathForge/DGPO"],
      "could_be_applied_to": "MACR's training loop: perturbation robustness is likely correlated with problem difficulty (easy problems may already be robust, hard problems may be unsolvable regardless). MAD normalization ensures that the consistency signal from medium-difficulty perturbed problems doesn't dominate the gradient, allowing learning from the full difficulty spectrum."
    },
    {
      "tool": "Transfer reward via cross-model prefix completion",
      "what_it_does": "Truncates reasoning traces at random points and tests whether a frozen receiver model can complete them correctly, rewarding reasoning transferability as a proxy for genuine understanding rather than model-specific shortcuts.",
      "used_by": ["RLTR"],
      "could_be_applied_to": "Perturbation-aware transfer reward: test whether reasoning traces for problem x transfer to a receiver model solving perturbed problem x̃, and vice versa. If reasoning is genuinely mathematical (not surface-form-dependent), traces should transfer across equivalent problem variants."
    },
    {
      "tool": "Clip-Higher asymmetric clipping",
      "what_it_does": "Decouples upper and lower clipping bounds in PPO's ratio clipping (ε_low=0.2, ε_high=0.28), allowing more aggressive upward probability updates than downward, preventing entropy collapse while maintaining learning pressure.",
      "used_by": ["DAPO"],
      "could_be_applied_to": "MACR training stability: the consistency regularization term adds a new gradient signal that could interact pathologically with entropy dynamics. Clip-Higher provides a tested mechanism to prevent the consistency loss from collapsing policy entropy by allowing the model to maintain exploration even under the additional invariance constraint."
    },
    {
      "tool": "Multi-round rewrite-verify adversarial loop with cumulative strategy refinement",
      "what_it_does": "An LLM rewriter generates problem perturbations without prescribed rules, a verifier validates semantic equivalence and checks target failure, and cumulative conversation history enables strategy self-discovery across iterations. Achieves 15-45pp higher failure rates than static benchmarks.",
      "used_by": ["MaSTer"],
      "could_be_applied_to": "Dynamic training-time perturbation curriculum for MACR: instead of fixed perturbation types, use MaSTer's loop to continuously discover new perturbation strategies that the current model fails on, creating an adversarial curriculum that prevents the model from overfitting to specific perturbation patterns."
    }
  ],
  "common_pitfalls": [
    "Conflating augmentation with regularization: MathForge shows 75% of gains from augmentation alone, and PPCL demonstrates that consistency loss provides 10× data efficiency over pure augmentation. But if your consistency term adds <5% over a well-tuned augmentation-only baseline, reviewers will dismiss the contribution as 'just data augmentation with extra steps.' The augmentation-only baseline is the most important experiment in any consistency regularization paper — do it first, not last.",
    "Citing GSM-Symbolic uncritically: The Sturgeon 2026 audit found only 12.4% of GSM-NoOp distractors were truly unambiguous, and the Ivanova analysis reduced the '21/25 models significantly affected' claim to ~3-4 models. Citing the original 65% drop figure without acknowledging these critiques signals insufficient literature awareness and gives reviewers an easy rejection rationale. Use VAR-MATH's 47.9-72.9% drops as the primary motivation instead — those findings haven't been contested.",
    "Testing only on GSM-level math: AbstRaL was accepted at ICLR 2026 despite this limitation, but it was the first training-time intervention. A second paper with the same limitation would be viewed as incremental. Competition-level evaluation (AIME, MATH Level-5) is now table stakes for robustness papers, especially given MATH-Perturb's availability.",
    "Ignoring clean accuracy degradation: Any robustness intervention that trades >2 points of clean accuracy will face the 'not practical' objection. CSR's warm-start curriculum and token-subset optimization were specifically designed to minimize clean accuracy impact. Plan for this from the start — don't discover it during rebuttal.",
    "Using AIME 2024 as a primary evaluation benchmark without contamination caveats: MathArena proved statistically significant score inflation on AIME 2024. Report AIME 2024 results with explicit contamination disclaimers and use AIME 2025 or CMIMC as the clean comparison.",
    "Adversarial co-training instability without sufficient stabilization engineering: Both APRM and GAR require careful stabilization (OGDA, alignment rewards, KL/entropy regularization). APRM was desk-rejected, possibly due to insufficient rigor. Any adversarial component needs thorough stability analysis and failure mode documentation.",
    "Assuming robustness to trained perturbation types implies robustness to unseen types: The entire value proposition of consistency regularization over augmentation is transfer to unseen perturbation types. If you train on numerical substitution and variable renaming, you MUST evaluate on distractor insertion, structural changes, and method-changing perturbations (MATH-Perturb hard). Without this, the paper reduces to a sophisticated augmentation study.",
    "Overloading the method with too many components without clear ablation: F²C has three loss terms but ablation shows CCE alone captures 95%+ of gains. GAR has four λ weights creating a hyperparameter nightmare. Every component must be individually justified with clean ablation. If a component adds <1% in ablation, drop it for clarity.",
    "Neglecting compute reporting: The field has moved toward compute-aware evaluation (RLTR reports 57% reduction, MathForge reports $184 reformulation cost, scaling laws paper provides explicit compute-optimal allocation). Reporting only accuracy without compute/time budgets is increasingly penalized.",
    "Treating the consistency term's λ weighting as a simple hyperparameter: The interaction between consistency regularization strength and RL training dynamics is non-trivial. Too strong a consistency term can suppress exploration (the model becomes invariant by producing identical low-quality outputs). Too weak and it provides no gradient. CSR's warm-start curriculum (progressively introducing the loss) is a proven solution — don't skip this and then wonder why training is unstable."
  ],
  "field_trajectory": "The field is converging on a three-layer stack for robust mathematical reasoning: (1) robust training algorithms that enforce the right inductive biases during RL, (2) robust reward models that provide consistent evaluation signals across problem variants, and (3) dynamic adversarial evaluation that continuously stress-tests trained models. Currently, each layer is being developed independently — MACR-style consistency regularization for layer 1, APRM/ThinkPRM for layer 2, MaSTer/VAR-MATH for layer 3 — but the high-impact 2026-2027 papers will integrate across layers. The most promising macro-direction is the unification of diversity preservation (DPH-RL, RLTR) with perturbation invariance (MACR) under a single information-theoretic framework: the model should explore diverse solution strategies (high entropy over solution paths) while being invariant to irrelevant surface features (low divergence across equivalent inputs). This is essentially the mathematical reasoning instantiation of invariant risk minimization, and formalizing it as such would give the work theoretical weight beyond empirical contributions. A second macro-direction is the shift from static to adaptive training curricula — MaSTer's self-discovering perturbations, GAR's co-evolving discriminator, and MathForge's difficulty-aware weighting all point toward training loops that continuously adapt their challenge level to the model's current weaknesses. The third direction, enabled by the ACL 2026 scaling laws paper, is compute-optimal co-design: jointly optimizing model size, training steps, perturbation diversity, and regularization strength within a fixed compute budget, replacing the current practice of grid-searching hyperparameters independently.",
  "meta_advice": "If you're writing a 2026 paper in this area, your #1 risk is being dismissed as 'data augmentation with extra steps.' The augmentation-only baseline is your make-or-break experiment — run it in Week 1, not Week 8. If the consistency term doesn't add at least 5 points beyond augmentation-only on at least one major benchmark, pivot immediately. Your #2 risk is scope limitation: AbstRaL got accepted as the first training-time intervention despite GSM-only evaluation, but that slot is taken. You need competition-level math results (AIME25, MATH-Perturb hard) and transfer to unseen perturbation types. For compute efficiency under a 200 H100-hour budget, the scaling laws paper's data reuse finding (up to 25×) is your best friend — you can train on perturbed variants of the same problems without performance degradation. Use DAPO as your base RL algorithm (open-source, strongest engineering, solved entropy collapse) and implement consistency regularization as a modular add-on — this also makes the contribution cleaner. For evaluation, lead with VAR-MATH drops (47.9-72.9%, uncontested) not GSM-Symbolic (65% drops, contested by Sturgeon audit). Design your perturbation generation pipeline to produce math-equivalent perturbations verified by SymPy, not LLM-judged equivalence — symbolic verification is both more rigorous and a concrete technical contribution. Finally, the reviewer-winning move is showing that your consistency-trained model improves on perturbation types it never saw during training (e.g., train on numerical substitution + variable renaming, evaluate on distractor insertion + structural changes from MATH-Perturb). This is the only clean way to distinguish consistency regularization from augmentation, and it's the claim that will make the paper memorable. Allocate at least 30% of your evaluation compute budget to this transfer analysis — it's where the paper lives or dies."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc72883b-1630-4f39-bfef-7b7e13086975",
  "isSidechain": false,
  "requestId": "req_011CbWKKfQkYrTCkvcWxCRWy",
  "type": "assistant",
  "uuid": "f009ecc5-7b4e-4b10-9ba4-fc5a4ab94c5a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f0e056d9-d209-4ed0-8a96-6ccdc25ef9c5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MpzpMs522rRQ8m69WQCo1W",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13248,
      "cache_read_input_tokens": 11014,
      "output_tokens": 7719,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13248,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 7719,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 13248,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13248
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
  "leafUuid": "f009ecc5-7b4e-4b10-9ba4-fc5a4ab94c5a",
  "sessionId": "f0e056d9-d209-4ed0-8a96-6ccdc25ef9c5"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesizing math robustness via consistency regularization",
  "sessionId": "f0e056d9-d209-4ed0-8a96-6ccdc25ef9c5"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-29 (UTC).**  ## Research area: Target: AAAI 2026 Track: Machine Lea…",
  "leafUuid": "f009ecc5-7b4e-4b10-9ba4-fc5a4ab94c5a",
  "sessionId": "f0e056d9-d209-4ed0-8a96-6ccdc25ef9c5"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesizing math robustness via consistency regularization",
  "sessionId": "f0e056d9-d209-4ed0-8a96-6ccdc25ef9c5"
}
```

---
