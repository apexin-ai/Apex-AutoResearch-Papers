# Research conversation: You are a senior ML research advisor synthesizing a literature review into an actionable research strategy. **Today's da

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/5426ac1b-6861-47ee-b4fa-9d7f4ce993ea.jsonl`
- **Structured JSON:** [`0e194c21af98d9488e58.json`](../../sessions/0e/0e194c21af98d9488e58.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T07:33:33.276Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T07:33:33.276Z",
  "sessionId": "5426ac1b-6861-47ee-b4fa-9d7f4ce993ea",
  "content": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.\n\n**Today's date: 2026-05-29 (UTC).**\n\n## Research area: Target: AAAI 2026\nTrack: Machine Learning (ML) — Reinforcement Learning / Mathematical Reasoning\n\nDirection: RL-trained mathematical reasoning models exhibit 47-73% accuracy drops under trivial perturbations (numerical substitution, variable renaming) despite achieving SOTA on clean benchmarks. We propose Math-Aware Consistency Regularization (MACR): adding a JS-divergence consistency term between model outputs on original and mathematically-equivalent perturbed problems during GRPO training, with a complementary discrimination loss against surface-similar but semantically different problems. This adapts proven NLP consistency techniques (F²C, PPCL) to mathematical reasoning with math-equivalence-aware perturbation generation and RL integration — a combination no existing work provides.\n\nSeed Papers:\n- Mirzadeh et al., GSM-Symbolic (Apple, ICLR 2025) — documents up to 65% accuracy drops from single irrelevant clause; establishes that models pattern-match rather than reason\n- VAR-MATH (arXiv 2025) — most damning evidence: 47.9-72.9% drops for RL models on numerically re-parameterized competition math; directly motivates why RL training is the problem\n- Gao et al., AbstRaL (ICLR 2026) — only existing training-time intervention; uses abstraction not invariance; limited to GSM-level; our primary comparison baseline\n- Flip-Flop Consistency / F²C (arXiv 2024) — JS-divergence consistency for prompt perturbation robustness in NLP; proves the technique works but has never been adapted to math reasoning or RL\n- PPCL (EACL 2024) — KL-based consistency regularization recovering 59-69% of perturbation-induced drops in NLU; complementary theoretical grounding\n- CSR: Causal Consistency Regularization (arXiv 2025) — enforces causal faithfulness via operator-level interventions during SFT; closest methodological cousin but SFT-only and targets faithfulness not perturbation invariance\n- APRM (arXiv 2025) — adversarial PRM training on reasoning errors; shows PRM quality matters for downstream RL; motivates our perturbation-robust PRM extension\n\nKnown Gaps:\n- No work applies consistency regularization (JS/KL divergence across equivalent problem variants) during RL training for mathematical reasoning — F²C and PPCL remain NLP-only and SFT-only\n- No PRM has been trained to be robust to surface-form variations of equivalent problems — APRM addresses reasoning errors, not perturbation invariance\n- No training-time robustness intervention has been demonstrated on competition-level math (AIME/Putnam); AbstRaL is GSM-only\n\nTheoretical Anchor: Mathematical equivalence defines a natural invariance class — problems that differ only in surface form (variable names, specific numbers, phrasing) but share identical mathematical structure should produce identical solution distributions. RL training violates this invariance because the reward signal (correct/incorrect final answer) provides no gradient against surface-form-dependent reasoning. A consistency regularization term explicitly penalizes policy divergence across equivalent variants, forcing the model to learn representations that are invariant to mathematically irrelevant features. This is a direct instantiation of Invariant Risk Minimization principles in the RL-for-reasoning setting.\n\nConstraints:\n- Compute: ≤200 H100-hours (budget: 40h baseline GRPO + 90h method variants + 30h evaluation + 20h analysis + 20h buffer)\n- Models: Primary experiments on 7B (Qwen2.5-Math-7B); scaling verification on 14B\n- Evaluation: GSM-Symbolic, GSM-Plus, VAR-MATH (AMC23/AIME24/AIME25), MATH-Perturb; train-time perturbations (numerical substitution, variable renaming) held out from eval perturbations (distractor insertion, structural changes)\n\nQuality Self-Checks:\n- [x] Core insight: RL training optimizes for reward on fixed problem forms, creating surface-form dependencies that consistency regularization can break by enforcing invariance across equivalent variants.\n- [x] Why not obvious: Consistency regularization is well-known in NLP but requires math-aware equivalence-preserving perturbation generation (not just paraphrase) and RL integration (not just SFT) — two non-trivial adaptations that straddle communities.\n- [ ] Baseline fear test: A pure data-augmentation baseline (adding perturbed problems to RL training without consistency loss) could achieve substantial gains. The paper MUST include this baseline and show the consistency term provides additional benefit beyond augmentation. If the gap is <5%, the contribution is weak.\n- [x] Information exploited: Mathematical equivalence structure — the method uses symbolic verification that perturbations preserve the problem's mathematical structure, which pure augmentation or paraphrase-based consistency ignores.\n\nAvoid:\n- Framing this as 'just data augmentation with extra steps' — the consistency objective is the contribution, not the perturbation generation. Must clearly show augmentation-only baseline is insufficient.\n- Over-claiming generality without testing on held-out perturbation types — the key differentiator from augmentation is transfer to unseen perturbation types, so this MUST be demonstrated.\n- Testing only on GSM-level math — this repeats AbstRaL's limitation and loses the competition-math differentiator.\n- Ignoring clean accuracy — if MACR degrades unperturbed accuracy by >2 points, reviewers will question practicality.\n\n## Paper analyses (20 papers)\n\n[\n  {\n    \"title\": \"GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models\",\n    \"venue\": \"ICLR 2025\",\n    \"problem_identification\": \"Identified that GSM8K's fixed test set provides no variance signal and is contamination-prone, by converting 100 questions into symbolic templates with 50 instantiations each and measuring distributional performance — revealing that 21/25 models score >1σ above their GSM-Symbolic mean on original GSM8K.\",\n    \"key_insight\": \"Genuine reasoning must be invariant to mathematically irrelevant surface changes; the GSM-NoOp experiment (adding a single irrelevant clause) exposed catastrophic pattern-matching failures (up to 65% drops) that in-context examples cannot recover, proving models integrate surface cues rather than parsing problem structure.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"Creates symbolic templates from GSM8K with parameterized names, numbers, and objects, generating 50 instantiations per template. Introduces controlled difficulty variants (GSM-M1 through GSM-P2, adding/removing reasoning clauses) and GSM-NoOp (irrelevant-but-plausible distractors). Evaluates 25+ models using 8-shot CoT with greedy decoding, reporting distributional statistics rather than point estimates.\",\n    \"limitations_and_open_questions\": \"Statistical critique (Ivanova) showed only 4/25 models exhibit statistically significant drops under proper Wilson intervals; frontier models (o1-preview: 15.3% NoOp drop vs. Phi-3-mini: 62.7%) are far more resilient, undermining universal claims. How do distribution shifts in numerical ranges confound the reasoning-failure narrative?\",\n    \"building_blocks\": [\n      \"GSM-Symbolic templates\",\n      \"GSM-NoOp distractor design\",\n      \"Distributional evaluation methodology\",\n      \"Controlled difficulty scaling (M1/P1/P2)\"\n    ],\n    \"relevance_to_seed\": \"Foundational motivation for MACR — establishes the surface-form fragility problem that consistency regularization targets, and provides one of our evaluation benchmarks.\"\n  },\n  {\n    \"title\": \"GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers\",\n    \"venue\": \"ACL 2024\",\n    \"problem_identification\": \"Found that prior robustness benchmarks each tested only one perturbation type (SVAMP: paraphrasing; GSM-IC: distractors), giving an incomplete robustness picture. Surveyed existing datasets (Table 1) and demonstrated that solving a GSM8K question does not imply solving its trivially modified variant — GPT-3.5-Turbo fails when 'leave' becomes 'return.'\",\n    \"key_insight\": \"Robustness requires simultaneous testing across qualitatively different reasoning capabilities grounded in Polya's problem-solving stages; critically, math-specific SFT improves accuracy but NOT robustness (SFT PDR ≈ foundation PDR), meaning the training paradigm itself is insufficient.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"Designs 8 perturbation types from 5 perspectives mapped to Polya's principles: numerical (substitution, digit expansion, IDF conversion), arithmetic (adding/reversing operations), problem understanding (rephrasing), distractor insertion, and critical thinking (removing essential info). GPT-4 generates 10,552 variants from 1,319 GSM8K questions with 18.85% human correction. Tests 25 LLMs across 4 prompting methods.\",\n    \"limitations_and_open_questions\": \"Limited to grade-school math — no competition-level evaluation. No analysis of intermediate reasoning step correctness or root-cause failure mechanisms. Does the proposed Compositional Prompting (COMP) method scale beyond GPT-3.5-Turbo, and can it close the human-LLM robustness gap?\",\n    \"building_blocks\": [\n      \"8-type perturbation taxonomy\",\n      \"PDR/ASP robustness metrics\",\n      \"Polya-grounded evaluation framework\",\n      \"Compositional Prompting (COMP)\"\n    ],\n    \"relevance_to_seed\": \"Provides our perturbation taxonomy and one evaluation benchmark (GSM-Plus); the finding that SFT doesn't fix robustness directly motivates training-time interventions like MACR.\"\n  },\n  {\n    \"title\": \"CREAM: Consistency Regularized Self-Rewarding Language Models\",\n    \"venue\": \"ICLR 2025\",\n    \"problem_identification\": \"Observed that 7B self-rewarding LMs degrade after 2-3 iterations (Llama-2 7B: ARC-Easy drops 60.44%→46.55%) due to compounding errors in self-generated preference labels — each iteration's reward inaccuracies snowball into corrupted training data.\",\n    \"key_insight\": \"Cross-iteration reward consistency (measured via Kendall's Tau between current and previous model rankings) provides a lightweight, principled signal for preference data reliability — disagreement between iterations indicates unreliable labels that should be downweighted.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"Computes global consistency rate C via Kendall's Tau between rankings from consecutive model checkpoints. Proves (Theorem 3.3) this is equivalent to soft-labeled DPO: L = C·L_DPO(chosen,rejected) + (1-C)·L_DPO(rejected,chosen), effectively label-smoothing for preferences. Lemma 3.4 links empirical Tau to the regularization parameter. Only requires two checkpoints — no ensembles.\",\n    \"limitations_and_open_questions\": \"Limited to 7B-13B scale; ranking accuracy tops ~70% (acknowledged as unsatisfying). Requires at least SFT-level alignment to bootstrap. Does the consistency principle transfer to RL training objectives beyond DPO, and to domain-specific (e.g., math) rather than general preference alignment?\",\n    \"building_blocks\": [\n      \"Cross-iteration consistency as regularization signal\",\n      \"Soft-labeled DPO formulation\",\n      \"Kendall's Tau as dynamic regularization strength\",\n      \"Reversed-DPO loss component\"\n    ],\n    \"relevance_to_seed\": \"Validates consistency regularization within iterative LLM training (RL-adjacent); the cross-iteration consistency principle parallels MACR's cross-perturbation consistency — both use agreement signals to stabilize training.\"\n  },\n  {\n    \"title\": \"rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking\",\n    \"venue\": \"ICML 2025 (Oral)\",\n    \"problem_identification\": \"Identified three bottlenecks: diminishing returns from CoT data scaling (OpenMathInstruct-2: 8× data → only 3.9% gain), weak open-source test-time compute scaling due to poor reward models, and the PRM training dilemma — MCTS Q-values are too noisy for regression-based PRM training but human step-level annotations are prohibitively expensive.\",\n    \"key_insight\": \"Reframing process reward model training from regression (predict precise Q-values) to preference ranking (which step is better?) dramatically improves PRM quality because Q-values, while too noisy for absolute scoring, reliably distinguish positive from negative steps — a much weaker requirement.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"Introduces Process Preference Model (PPM) trained with Bradley-Terry pairwise loss on MCTS-derived preference pairs (top-2 vs. bottom-2 Q-value candidates sharing identical context). Runs 4-round self-evolution: MCTS generates code-augmented CoT trajectories, PPM trains on resulting preferences, improved PPM guides next-round MCTS. Code execution provides step-level verification. Achieves 90% MATH with Qwen-7B.\",\n    \"limitations_and_open_questions\": \"Massive compute (10 nodes × 8 H100s for weeks); Round 1 bootstraps from 236B-parameter model. PPM robustness to adversarial perturbations is untested — if surface-form changes corrupt Q-value orderings, the preference pair construction breaks. Does PPM quality degrade under distribution shift?\",\n    \"building_blocks\": [\n      \"Process Preference Model (PPM) with Bradley-Terry loss\",\n      \"MCTS-guided CoT trajectory generation\",\n      \"Code-augmented step verification\",\n      \"4-round policy-PRM co-evolution\"\n    ],\n    \"relevance_to_seed\": \"Demonstrates PRM is the performance bottleneck in RL-for-math, directly motivating MACR's perturbation-robust PRM extension; PPM's preference-based formulation suggests a natural integration point for consistency-based robustness.\"\n  },\n  {\n    \"title\": \"Robust Reasoning Benchmark\",\n    \"venue\": \"arXiv 2026\",\n    \"problem_identification\": \"Observed that prior adversarial benchmarks (GSM-Symbolic, GSM-Plus) conflate reasoning failures with arithmetic failures by changing numerical values. Identified that it was unknown whether competition-math (AIME) performance reflects robust reasoning or fragile pattern-matching on standard formatting.\",\n    \"key_insight\": \"You can isolate pure structural fragility without touching mathematical content — 13 deterministic, reversible textual transformations preserve exact mathematical state while exposing that LLM reasoning is overfit to standard presentation, with failures attributable to tokenization breakdown and attention dilution rather than mathematical incompetence.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"Applies 13 perturbations across 4 categories to AIME 2024/2025: semantic substitutions (double negation, antonyms, wrappers), contextual overload (line/word/symbol interleaving), syntactic distortions (sentence/word/symbol reversal), and visual encodings (Rail Fence cipher, rectangle perimeter, snake patterns). All transformations are algorithmically invertible with explicit decoding protocols provided in prompts. Separately studies Intra-Query Attention Dilution via sequential problem contexts.\",\n    \"limitations_and_open_questions\": \"AIME-only domain; proprietary models tested less comprehensively. Claude's failures stem from safety-filter refusals, not reasoning — raising questions about confounding. The concept of 'atomic reasoning unit' (maximum computation before structural noise degrades logic) is proposed but not formally quantified.\",\n    \"building_blocks\": [\n      \"13 deterministic reversible perturbation types\",\n      \"Failure mode taxonomy (cognitive thrashing, tokenization breakdown)\",\n      \"IQAD attention dilution analysis\",\n      \"Competition-math robustness evaluation\"\n    ],\n    \"relevance_to_seed\": \"Validates MACR's focus on competition-level math robustness; finding that open-weights models drop ~47-54% on AIME under surface-only changes confirms the problem persists at competition level and is not limited to GSM-level math.\"\n  },\n  {\n    \"title\": \"VAR-MATH: Probing True Mathematical Reasoning in LLMs via Symbolic Multi-Instance Benchmarks\",\n    \"venue\": \"arXiv 2025\",\n    \"problem_identification\": \"Standard math benchmarks use fixed numerical instances susceptible to data contamination and pattern memorization; the authors identified that RL-trained models show gains even with flawed reward signals, suggesting performance reflects memorized surface patterns rather than genuine mathematical reasoning.\",\n    \"key_insight\": \"By converting competition problems into parameterized symbolic templates with feasible variable domains, you can generate unlimited structurally equivalent instances that expose whether a model has learned the mathematical structure or merely memorized specific numerical patterns.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"VAR-MATH applies a four-step variabilization pipeline: structural analysis of algebraic relationships, symbolic parameterization (replacing constants with constrained variables via Random_linespace/Random_Set specifications), parametric solution formulation (answers as symbolic functions), and precision specification for numerical stability. They transform AMC23, AIME24, and AIME25 into symbolic benchmarks and evaluate models on multiple instantiations per problem. Two metrics are introduced: strict (all-or-nothing across all variants) and loose (average accuracy), separating contamination effects from reasoning instability.\",\n    \"limitations_and_open_questions\": \"Only 3 competition benchmarks are variabilized; the process requires expert mathematical analysis per problem and cannot be fully automated. The largest models (DeepSeek-R1, SEED-THINK) show minimal drops, raising the question of whether scale alone solves the problem, which would undermine training-time interventions like MACR.\",\n    \"building_blocks\": [\n      \"VAR-AMC23/AIME24/AIME25 benchmarks\",\n      \"Symbolic parameterization pipeline for math problems\",\n      \"Strict vs. loose evaluation metrics for reasoning consistency\",\n      \"Per-model drop quantification methodology\"\n    ],\n    \"relevance_to_seed\": \"Provides the most direct motivation for MACR by quantifying 47.9–72.9% accuracy drops specifically for RL-trained models on competition math, and supplies ready-made evaluation benchmarks (VAR-AMC23/AIME24/AIME25) for measuring MACR's effectiveness.\"\n  },\n  {\n    \"title\": \"Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs\",\n    \"venue\": \"arXiv 2025\",\n    \"problem_identification\": \"LLMs produce inconsistent predictions across semantically equivalent prompt phrasings, undermining deployment reliability; prior work focused on prompt engineering or ensembling at inference time rather than training the model to be inherently invariant.\",\n    \"key_insight\": \"A model's own majority vote across prompt variations provides sufficient signal—without any labeled data—to train consistency via pseudo-labels, making the approach fully unsupervised and scalable.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"F²C combines two losses: Consensus Cross-Entropy (CCE), which creates hard pseudo-labels from majority vote across V prompt variations and trains all variations toward the consensus; and a representation alignment loss using KL divergence to pull non-confident/non-majority predictions toward confident majority predictions, weighted by a sigmoid-scaled confidence gap. A JSD term enforces agreement within the high-confidence set. Training uses LoRA on Qwen2.5-3B-Instruct with dynamic per-instance partitioning into confident-consensus (CC) and non-confident (NC) sets.\",\n    \"limitations_and_open_questions\": \"Evaluated only on classification tasks with a 3B model; open-ended generation, chain-of-thought reasoning, and larger models untested. Relies on availability of multiple prompt templates—a constraint that doesn't map directly to math problems. The majority-vote pseudo-label assumption may fail when the model is systematically wrong, which is common in hard math.\",\n    \"building_blocks\": [\n      \"JS-divergence consistency loss formulation\",\n      \"Consensus pseudo-labeling from majority vote\",\n      \"CC/NC dynamic partitioning algorithm\",\n      \"KL-based representation alignment with confidence weighting\"\n    ],\n    \"relevance_to_seed\": \"MACR's direct methodological ancestor: the CCE + JSD + KL loss architecture can be adapted from classification-over-prompt-variations to RL-over-math-perturbations, but requires replacing template-based prompt perturbations with math-equivalence-preserving transformations and integrating into GRPO's policy gradient rather than SFT.\"\n  },\n  {\n    \"title\": \"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning\",\n    \"venue\": \"Nature 2025\",\n    \"problem_identification\": \"Prior reasoning LLMs depended on large-scale supervised chain-of-thought data (expensive, bottlenecked by human annotation); DeepSeek identified that rule-based verifiable rewards alone might suffice to elicit reasoning if the RL algorithm is efficient enough to avoid critic-model overhead.\",\n    \"key_insight\": \"GRPO eliminates the critic model by estimating advantage from group-relative reward normalization, making pure RL on base LLMs computationally tractable and enabling emergent reasoning behaviors (self-reflection, verification, strategy adaptation) without any supervised reasoning demonstrations.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"GRPO samples G outputs per query, computes advantages as normalized deviations from group mean reward, and optimizes a clipped surrogate objective with KL regularization against a reference policy—no value network needed. The full pipeline has four stages: cold-start SFT on curated CoT examples, reasoning-focused RL with rule-based accuracy/format rewards, rejection sampling to generate 800K diverse SFT examples, and a final general-purpose RL phase. Rule-based rewards deliberately avoid neural reward models to prevent reward hacking at scale.\",\n    \"limitations_and_open_questions\": \"The reward signal is purely outcome-based (correct final answer), providing no gradient for process quality or perturbation robustness—exactly the gap MACR targets. Training data is opaque (criticized in Nature peer review). PRM and MCTS approaches were tried and failed, suggesting process-level signals are hard to integrate, which is a risk factor for MACR's PRM extension.\",\n    \"building_blocks\": [\n      \"GRPO algorithm (critic-free RL)\",\n      \"Rule-based reward design for math/code\",\n      \"Four-stage training pipeline\",\n      \"Emergent reasoning behavior analysis\"\n    ],\n    \"relevance_to_seed\": \"Defines the exact training paradigm MACR modifies: GRPO's outcome-only reward provides no invariance signal, and MACR's JS-divergence consistency term is designed to fill this gap by adding a perturbation-invariance objective alongside the correctness reward.\"\n  },\n  {\n    \"title\": \"Adversarial Training for Process Reward Models\",\n    \"venue\": \"arXiv 2025\",\n    \"problem_identification\": \"PRMs trained on static datasets with expensive manual step-level annotations generalize poorly to novel reasoning error types; the authors recognized that the static nature of training data creates a distribution mismatch when deployed on diverse downstream problems.\",\n    \"key_insight\": \"Framing PRM training as a general-sum (not zero-sum) game between a generator that creates plausible reasoning errors and a discriminator PRM yields provably convergent training via OGDA, producing progressively harder negatives without human annotation.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"A Llama-3.1-8B generator is trained via PPO to perturb correct reasoning steps into plausible errors that fool the PRM (+1 reward for fooling, -1 for producing correct steps). The PRM learns to detect these errors via binary cross-entropy. Unlike zero-sum formulations, the asymmetric reward structure forms a general-sum game, and training is stabilized using Optimistic Gradient Descent-Ascent (OGDA) with KL and entropy regularization ensuring strong monotonicity and linear convergence to Nash equilibrium. Downstream, the trained PRM serves as a step-level reward signal for GRPO, yielding +6.8–10.4pp gains over outcome-based RL on Gemma-3-12B.\",\n    \"limitations_and_open_questions\": \"The adversarial errors target reasoning mistakes (calculation errors, logical gaps), not surface-form variations of equivalent problems—a fundamentally different robustness axis than what MACR addresses. Whether the two approaches compose (perturbation-robust PRM + consistency-regularized policy) remains untested.\",\n    \"building_blocks\": [\n      \"General-sum game formulation for adversarial training\",\n      \"OGDA optimizer for stable GAN-like training\",\n      \"PPO-trained error generator\",\n      \"PRM-as-reward-for-GRPO pipeline\"\n    ],\n    \"relevance_to_seed\": \"Demonstrates that PRM quality directly impacts downstream RL (+6.8–10.4pp), motivating MACR's perturbation-robust PRM extension; the adversarial training framework could be adapted to generate surface-form-equivalent perturbations rather than reasoning errors, creating a complementary robustness signal.\"\n  },\n  {\n    \"title\": \"Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning\",\n    \"venue\": \"NeurIPS 2025\",\n    \"problem_identification\": \"RL dramatically improves math accuracy, but the field lacks granular understanding of what cognitive capabilities RL actually enhances—knowing this is critical for designing targeted training interventions rather than hoping undirected RL suffices.\",\n    \"key_insight\": \"RL does not primarily improve execution of externally provided plans but rather empowers models to formulate and follow internal strategies; paradoxically, explicit human-crafted plans can degrade performance, but RL-trained models are more robust to such interference.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"SPARKLE evaluates RL's effects along three dimensions: (1) plan following—comparing performance with/without solution skeletons reveals RL models develop superior internal strategies; (2) knowledge integration—providing external facts/theorems shows RL models gain +4.3% while base models drop -5.4%; (3) chain of subproblems—decomposing problems into sequential checkpoints exposes where reasoning chains break. They also introduce SparkleRL-PSS, a two-stage pipeline: Stage 1 trains GRPO on 40K diverse problems, Stage 2 continues on 5.7K hard problems with partial solution scaffolding (0–4 semantic chunks provided as context), achieving 50.42% on AIME24.\",\n    \"limitations_and_open_questions\": \"The analysis framework doesn't examine surface-form sensitivity—a critical dimension for MACR. The subproblem decomposition finding (50.4% full-problem accuracy but only 17.5% all-subproblems accuracy) suggests RL models may take shortcuts that correlate with pattern-matching rather than systematic reasoning, which is consistent with VAR-MATH's findings.\",\n    \"building_blocks\": [\n      \"Three-dimensional reasoning analysis framework\",\n      \"SparkleRL-PSS partial scaffolding pipeline\",\n      \"Plan-following measurement methodology\",\n      \"Knowledge integration controlled experiments\"\n    ],\n    \"relevance_to_seed\": \"Provides mechanistic understanding of what MACR's consistency term should preserve: RL enhances internal strategy formulation and knowledge integration, so the consistency loss must regularize these capabilities across perturbations without destroying the internal planning that RL develops.\"\n  },\n  {\n    \"title\": \"AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking\",\n    \"venue\": \"ICLR 2026\",\n    \"problem_identification\": \"LLMs suffer accuracy drops under trivial distribution shifts (numerical substitution, variable renaming, distractor insertion) because they pattern-match on surface features rather than reasoning abstractly. The authors identified that prior robustness work focused on evaluation or data augmentation but lacked a training-time intervention targeting the root cause: absence of abstract problem representations.\",\n    \"key_insight\": \"Teaching LLMs to explicitly de-contextualize math problems into symbolic abstractions (replacing specific values with placeholder variables) before solving, trained via RL rather than SFT which fails to produce faithful abstractions, forces representations invariant to surface-form changes.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"AbstRaL constructs GranulAR (Granularly-decomposed Abstract Reasoning) data by having an oracle LLM rewrite CoT solutions with abstract symbols (e.g., '12' → '[in0]') within socratic decomposition structure, verified by symbolic solvers. A two-stage pipeline applies SFT on GranulAR data followed by GRPO RL training with two model-free rewards: a symbolic distance reward (edit distance to gold abstraction) and an answer correctness reward. This avoids training a separate reward model while directly incentivizing faithful abstraction.\",\n    \"limitations_and_open_questions\": \"Evaluated only on GSM-level math (not competition-level AIME/Putnam); depends on a strong oracle LLM (70B) for data generation; abstractions are rigid symbolic templates rather than learned invariances — unclear if this scales to problems requiring flexible mathematical reformulation rather than simple variable substitution.\",\n    \"building_blocks\": [\n      \"GranulAR abstraction data pipeline\",\n      \"GRPO with symbolic distance reward\",\n      \"Two-stage SFT→RL training for reasoning robustness\",\n      \"GSM-Symbolic and GSM-Plus evaluation protocols\"\n    ],\n    \"relevance_to_seed\": \"Primary comparison baseline for MACR — AbstRaL targets the same robustness problem but via explicit abstraction rather than invariance-enforcing consistency regularization, and is limited to GSM-level math, leaving competition-level robustness as MACR's key differentiator.\"\n  },\n  {\n    \"title\": \"Prompt Perturbation Consistency Learning for Robust Language Models\",\n    \"venue\": \"EACL 2024 Findings\",\n    \"problem_identification\": \"Fine-tuned LLMs on NLU tasks (intent classification, slot filling) suffer significant accuracy drops from input perturbations (oronyms, synonyms, paraphrasing), and standard data augmentation requires large augmented datasets to partially mitigate this. The authors identified that augmentation addresses symptoms (insufficient coverage) while ignoring the core issue: models learn perturbation-sensitive representations.\",\n    \"key_insight\": \"Regularizing the JS divergence between output distributions on clean and perturbed inputs during training forces perturbation-invariant representations more efficiently than augmentation alone, recovering 59-69% of perturbation-induced drops with 10× fewer augmented samples.\",\n    \"innovation_type\": \"cross_domain\",\n    \"method_summary\": \"PPCL combines three loss terms: L = λ₁Lc + λ₂Lp + λ₃Ljs, where Lc and Lp are cross-entropy losses on clean and perturbed samples respectively, and Ljs is a JS divergence consistency term between the output distributions. JS divergence is chosen over KL for its symmetry: JS(ŷc‖ŷp) = ½(KL(ŷc‖ŷm) + KL(ŷp‖ŷm)) where ŷm is the averaged distribution. For variable-length paraphrases, divergence is computed on averaged probability distributions rather than token-aligned pairs.\",\n    \"limitations_and_open_questions\": \"Applied only to NLU classification tasks (IC/SF), not generative reasoning; perturbations are surface-level text transformations (not math-equivalence-preserving); SFT-only with no RL integration — the gap of adapting this consistency framework to RL training and mathematical domains remains entirely open.\",\n    \"building_blocks\": [\n      \"JS divergence consistency loss formulation\",\n      \"Three-term loss weighting (clean + perturbed + consistency)\",\n      \"Evidence that consistency loss > pure augmentation\",\n      \"Perturbation type taxonomy (oronyms/synonyms/paraphrasing)\"\n    ],\n    \"relevance_to_seed\": \"Provides the core theoretical and empirical grounding that MACR adapts: the JS consistency loss formulation and the critical evidence that consistency regularization outperforms pure data augmentation with far fewer samples — MACR's key claim that the consistency term matters beyond augmentation rests on PPCL's precedent.\"\n  },\n  {\n    \"title\": \"DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models\",\n    \"venue\": \"arXiv 2024\",\n    \"problem_identification\": \"PPO-based RL for mathematical reasoning requires training a separate critic/value network, roughly doubling memory requirements and adding training instability, making it impractical for large-scale math reasoning models. The authors identified that the critic model is unnecessary when reward signals are verifiable (math correctness) and advantages can be estimated from group statistics.\",\n    \"key_insight\": \"Replacing the learned value baseline in PPO with group-relative normalization of rewards — computing advantages as Ai = (ri − mean(r))/std(r) within a sampled group — eliminates the critic model entirely while providing stable advantage estimates for verifiable tasks.\",\n    \"innovation_type\": \"simplification\",\n    \"method_summary\": \"GRPO samples G responses per question from the current policy, assigns binary correctness rewards, and normalizes within-group to compute advantages. The policy is updated via a clipped surrogate objective (identical to PPO's clip) plus a KL divergence penalty β·DKL(πθ‖πref) to prevent drift from the reference model (β=0.04). This achieves ~50% memory reduction over PPO by eliminating the value network. Combined with a web-scale math pretraining pipeline (120B tokens selected from Common Crawl), DeepSeekMath-7B achieved 51.7% on MATH.\",\n    \"limitations_and_open_questions\": \"GRPO's group-relative advantage is a biased estimator when group sizes are small or reward distributions are skewed; the binary reward signal provides no gradient for partial correctness or reasoning quality; no analysis of robustness to problem perturbations — the reward signal optimizes for correct answers on fixed problem forms without penalizing surface-form dependence.\",\n    \"building_blocks\": [\n      \"GRPO algorithm (the RL backbone MACR extends)\",\n      \"Group-relative advantage estimation\",\n      \"Clipped objective + KL penalty framework\",\n      \"Web-scale math data selection pipeline\"\n    ],\n    \"relevance_to_seed\": \"GRPO is the specific RL algorithm MACR extends — MACR adds a JS-divergence consistency term to GRPO's objective, requiring understanding of how the group sampling, advantage computation, and KL penalty interact with an additional regularization loss on paired (original, perturbed) problem groups.\"\n  },\n  {\n    \"title\": \"Scaling Behaviors of LLM Reinforcement Learning Post-Training: An Empirical Study in Mathematical Reasoning\",\n    \"venue\": \"ACL 2026\",\n    \"problem_identification\": \"Despite widespread adoption of RL post-training for math reasoning, no systematic characterization existed of how model scale, data volume, and compute budget interact — practitioners relied on ad-hoc hyperparameter choices. The authors identified this gap by running controlled GRPO experiments across the full Qwen2.5 series (0.5B–72B).\",\n    \"key_insight\": \"RL post-training performance follows a predictive power-law log L(N,X) = −k(N)·log X + E(N) where learning efficiency k(N) saturates via k(N) = Kmax/(1+N₀/N), enabling extrapolation of larger-model performance from smaller-scale experiments and revealing diminishing returns beyond ~32B parameters.\",\n    \"innovation_type\": \"scaling\",\n    \"method_summary\": \"The study uses GRPO across Qwen2.5 0.5B–72B models with controlled hyperparameters (lr=1e-6, batch=512, variable rollout sizes 4–32). They fit power-law models to test loss as a function of compute and data, discovering predictive relationships (R²>0.99 intra-model). A key finding is that data reuse up to 25× repetition produces no significant degradation, with performance governed by total optimization steps rather than sample uniqueness. The saturation curve reveals practical efficiency ceilings at extreme scales.\",\n    \"limitations_and_open_questions\": \"Mathematical RL shows negligible transfer to out-of-domain tasks; scaling laws characterized only for GRPO (not PPO or other RL variants); does not address robustness — all scaling analysis assumes clean benchmark performance without perturbation evaluation.\",\n    \"building_blocks\": [\n      \"Power-law scaling formulas for RL post-training\",\n      \"Data reuse tolerance bounds (≤25×)\",\n      \"Compute-optimal model-size guidance for budget-constrained experiments\",\n      \"GRPO hyperparameter configurations across model scales\"\n    ],\n    \"relevance_to_seed\": \"Directly informs MACR's experimental design: validates 7B as a cost-effective primary model size, confirms GRPO's stability across scales for the 14B verification experiments, and the data reuse finding suggests MACR's perturbation-augmented training data can be recycled without degradation within the 200 H100-hour budget.\"\n  },\n  {\n    \"title\": \"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters\",\n    \"venue\": \"ICLR 2025 (Oral)\",\n    \"problem_identification\": \"Prior work on test-time compute scaling provided largely negative results, and no framework existed for compute-optimal allocation across problem difficulties. The authors identified that uniform allocation wastes compute on easy problems and starves hard ones, and that the choice between parallel search vs. sequential revision depends critically on question difficulty.\",\n    \"key_insight\": \"Difficulty-conditioned allocation of test-time compute — selecting between PRM-guided beam search and sequential revision per difficulty bin — achieves 4× efficiency over best-of-N and allows a smaller model to match a 14× larger model on easy-to-medium questions under FLOPs-matched evaluation.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"The paper studies two mechanisms: (1) PRM-guided search (best-of-N weighted, beam search, lookahead search) where PRMs score intermediate steps to prune/select solution paths, and (2) sequential revision where models iteratively improve answers conditioned on prior incorrect attempts. Questions are binned into five difficulty quantiles via pass@1 rates estimated from 2048 samples. A compute-optimal strategy independently selects the best mechanism per bin on a validation fold. Key finding: beam search dominates at small budgets but best-of-N wins at large budgets due to PRM exploitation/overoptimization.\",\n    \"limitations_and_open_questions\": \"PRM quality is the bottleneck — beam search degrades at high compute due to reward model exploitation; PRMs are not robust to surface-form variations of equivalent problems; difficulty estimation requires 2048 samples per question, limiting practicality; the 14× comparison holds only for easy/medium questions with low inference-to-pretraining ratio.\",\n    \"building_blocks\": [\n      \"Difficulty-conditioned compute allocation framework\",\n      \"PRM exploitation analysis (beam search vs. best-of-N tradeoff)\",\n      \"Sequential revision training via edit-distance pairing\",\n      \"FLOPs-matched train-time vs. test-time compute comparison methodology\"\n    ],\n    \"relevance_to_seed\": \"Establishes that PRM quality is the critical bottleneck for test-time compute scaling — PRM exploitation at high compute directly motivates MACR's perturbation-robust PRM extension, since a PRM that is invariant to surface-form variations would be less susceptible to reward hacking during search.\"\n  },\n  {\n    \"title\": \"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations\",\n    \"venue\": \"ICML 2025\",\n    \"problem_identification\": \"Prior perturbation benchmarks (GSM-Symbolic, VAR-MATH) only tested structure-preserving modifications; no benchmark existed for 'hard' perturbations that fundamentally change the problem's mathematical structure, requiring entirely different solution methods.\",\n    \"key_insight\": \"The distinction between simple perturbations (same method, different numbers) and hard perturbations (same surface form, different required method) reveals a novel failure mode: 'blind technique application' where models apply memorized solution strategies without verifying applicability to the modified problem.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"279 level-5 MATH problems were modified by 12 PhD-level annotators into simple (structure-preserving) and hard (structure-changing) variants with minimal textual edits but different answers. Error analysis taxonomizes failures into assumption ignorance (40%), blind technique application, and answer memorization. ICL experiments show that providing original-problem demonstrations actively hurts performance on hard perturbations (18-40% degradation), confirming models transfer solution templates rather than reason from scratch.\",\n    \"limitations_and_open_questions\": \"Small scale (279 problems) limits statistical power; level-5 only may miss difficulty-dependent failure patterns; no training-time mitigation is proposed — purely diagnostic. Does 'blind application' correlate with training data frequency of specific solution templates?\",\n    \"building_blocks\": [\n      \"Simple vs. hard perturbation taxonomy\",\n      \"Blind technique application error category\",\n      \"ICL-as-diagnostic methodology\",\n      \"Level-5 MATH perturbation dataset\"\n    ],\n    \"relevance_to_seed\": \"Provides a key evaluation benchmark for MACR and validates that structure-changing perturbations (which MACR's discrimination loss targets) are fundamentally harder than the structure-preserving perturbations (which MACR's consistency term targets).\"\n  },\n  {\n    \"title\": \"Causal Consistency Regularization: Training Verifiably Sensitive Reasoning in Large Language Models\",\n    \"venue\": \"arXiv 2025\",\n    \"problem_identification\": \"Standard training rewards final-answer correctness regardless of whether intermediate reasoning steps causally determine the answer, allowing models to produce correct outputs via unfaithful reasoning (36-42% of cases in standard fine-tuning).\",\n    \"key_insight\": \"Faithfulness can be enforced by penalizing invariance of predictions under operator-level counterfactual interventions on reasoning traces — if swapping '+' to '−' doesn't change the answer, the model isn't actually using that reasoning step.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"CSR adds a KL-divergence term L_CSR = D_KL(p(Y|T,X) || p(Y|T',X)) penalizing unchanged predictions under counterfactual traces T'. A learned 6-layer Transformer editor generates minimal, causally significant perturbations (operator swaps, entity substitutions) optimized via REINFORCE for validity, impact, and minimality. Warm-start curriculum and token-subset optimization keep overhead at ~9%. Faithfulness measured via Counterfactual Outcome Sensitivity (COS): CSR achieves +32-35 COS points across GSM8K, HotpotQA, and ProofWriter with p<0.001.\",\n    \"limitations_and_open_questions\": \"SFT-only (no RL integration); effectiveness degrades below 50% operator identification precision, limiting applicability to unstructured domains; targets faithfulness (does the model use its reasoning?) rather than perturbation invariance (does the model handle equivalent problems identically?) — complementary but distinct goals.\",\n    \"building_blocks\": [\n      \"Learned counterfactual trace editor\",\n      \"COS faithfulness metric\",\n      \"Warm-start curriculum for regularization overhead\",\n      \"Operator-level intervention framework\"\n    ],\n    \"relevance_to_seed\": \"Closest methodological cousin to MACR — both use consistency regularization during training but differ on three axes: CSR perturbs reasoning traces vs. MACR perturbs problem inputs; CSR targets faithfulness vs. MACR targets invariance; CSR is SFT-only vs. MACR integrates with RL. MACR should cite CSR's overhead management techniques.\"\n  },\n  {\n    \"title\": \"Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?\",\n    \"venue\": \"NeurIPS 2025 (Best Paper Runner-Up)\",\n    \"problem_identification\": \"The community assumed RLVR enables models to discover novel reasoning strategies (analogous to AlphaGo), but no systematic study had tested whether RL-trained models solve problems the base model fundamentally cannot, versus merely sampling existing solutions more efficiently.\",\n    \"key_insight\": \"RLVR functions as a distribution sharpener, not a capability expander — at large k, base models achieve higher pass@k than their RL-trained counterparts, and 13.3% of AIME24 problems are solvable only by the base model, proving RL narrows the solution space.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"Uses unbiased pass@k at large k as a boundary probe across math, code, and visual reasoning, comparing six RLVR algorithms (PPO, GRPO, Reinforce++, ReMax, etc.) against base models. Coverage analysis reveals almost every RL-model solution exists in the base distribution. Distillation serves as a positive control, demonstrating genuine capability expansion when superior teacher data is introduced — proving the methodology can detect expansion when it exists\n... (truncated)\n\n## Your task\n\nSynthesize these paper analyses into a **Field Guide** — a strategic document that would help a researcher generate novel, high-quality ideas in this area. This is NOT a survey — it's an opinionated strategy guide for innovation.\n\nThink about:\n- What PATTERNS OF INNOVATION keep working in this field?\n- What do reviewers consistently reward?\n- Where are the real gaps (not assumed gaps)?\n- What combinations haven't been tried?\n- What mistakes should we avoid?\n\n## Output format\n\nOutput a JSON object with these sections:\n{\n  \"innovation_patterns\": [\n    {\"pattern\": \"name\", \"description\": \"how it works\", \"examples\": [\"paper1\", \"paper2\"], \"success_rate\": \"high/medium/low\"}\n  ],\n  \"reviewer_preferences\": [\n    \"What reviewers in this area consistently care about (based on evidence from paper analyses)\"\n  ],\n  \"field_gaps\": [\n    {\"gap\": \"description of unsolved problem\", \"evidence\": \"which papers mention this limitation\", \"difficulty\": \"high/medium/low\", \"impact_if_solved\": \"high/medium/low\"}\n  ],\n  \"untried_combinations\": [\n    {\"idea_sketch\": \"what could be combined\", \"from_papers\": [\"which papers inspire this\"], \"why_promising\": \"reason\"}\n  ],\n  \"method_building_blocks\": [\n    {\"tool\": \"name\", \"what_it_does\": \"description\", \"used_by\": [\"papers\"], \"could_be_applied_to\": \"new application\"}\n  ],\n  \"common_pitfalls\": [\n    \"Mistakes to avoid when working in this area (based on reviewer feedback and paper limitations)\"\n  ],\n  \"field_trajectory\": \"Where is this field heading? What are the 2-3 most promising macro-directions? (paragraph)\",\n  \"meta_advice\": \"If you were advising a PhD student to write a strong 2026 paper in this area, what would you tell them? (paragraph)\"\n}\n\nBe specific and evidence-based — every claim should reference specific papers from the analyses. Avoid generic advice like 'be novel' — instead say 'Papers that combine X with Y for task Z have been getting accepted (see Paper A, Paper B).'.\n\nIMPORTANT: You MUST end your response with the JSON object."
}
```

---

### Runtime record

_source line 2 · 2026-05-29T07:33:33.284Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T07:33:33.284Z",
  "sessionId": "5426ac1b-6861-47ee-b4fa-9d7f4ce993ea"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-29T07:33:33.305Z_

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

## Paper analyses (20 papers)

[
  {
    "title": "GSM-Symbolic: Understanding the Limitations of Mathematical Reasoning in Large Language Models",
    "venue": "ICLR 2025",
    "problem_identification": "Identified that GSM8K's fixed test set provides no variance signal and is contamination-prone, by converting 100 questions into symbolic templates with 50 instantiations each and measuring distributional performance — revealing that 21/25 models score >1σ above their GSM-Symbolic mean on original GSM8K.",
    "key_insight": "Genuine reasoning must be invariant to mathematically irrelevant surface changes; the GSM-NoOp experiment (adding a single irrelevant clause) exposed catastrophic pattern-matching failures (up to 65% drops) that in-context examples cannot recover, proving models integrate surface cues rather than parsing problem structure.",
    "innovation_type": "new_benchmark",
    "method_summary": "Creates symbolic templates from GSM8K with parameterized names, numbers, and objects, generating 50 instantiations per template. Introduces controlled difficulty variants (GSM-M1 through GSM-P2, adding/removing reasoning clauses) and GSM-NoOp (irrelevant-but-plausible distractors). Evaluates 25+ models using 8-shot CoT with greedy decoding, reporting distributional statistics rather than point estimates.",
    "limitations_and_open_questions": "Statistical critique (Ivanova) showed only 4/25 models exhibit statistically significant drops under proper Wilson intervals; frontier models (o1-preview: 15.3% NoOp drop vs. Phi-3-mini: 62.7%) are far more resilient, undermining universal claims. How do distribution shifts in numerical ranges confound the reasoning-failure narrative?",
    "building_blocks": [
      "GSM-Symbolic templates",
      "GSM-NoOp distractor design",
      "Distributional evaluation methodology",
      "Controlled difficulty scaling (M1/P1/P2)"
    ],
    "relevance_to_seed": "Foundational motivation for MACR — establishes the surface-form fragility problem that consistency regularization targets, and provides one of our evaluation benchmarks."
  },
  {
    "title": "GSM-Plus: A Comprehensive Benchmark for Evaluating the Robustness of LLMs as Mathematical Problem Solvers",
    "venue": "ACL 2024",
    "problem_identification": "Found that prior robustness benchmarks each tested only one perturbation type (SVAMP: paraphrasing; GSM-IC: distractors), giving an incomplete robustness picture. Surveyed existing datasets (Table 1) and demonstrated that solving a GSM8K question does not imply solving its trivially modified variant — GPT-3.5-Turbo fails when 'leave' becomes 'return.'",
    "key_insight": "Robustness requires simultaneous testing across qualitatively different reasoning capabilities grounded in Polya's problem-solving stages; critically, math-specific SFT improves accuracy but NOT robustness (SFT PDR ≈ foundation PDR), meaning the training paradigm itself is insufficient.",
    "innovation_type": "new_benchmark",
    "method_summary": "Designs 8 perturbation types from 5 perspectives mapped to Polya's principles: numerical (substitution, digit expansion, IDF conversion), arithmetic (adding/reversing operations), problem understanding (rephrasing), distractor insertion, and critical thinking (removing essential info). GPT-4 generates 10,552 variants from 1,319 GSM8K questions with 18.85% human correction. Tests 25 LLMs across 4 prompting methods.",
    "limitations_and_open_questions": "Limited to grade-school math — no competition-level evaluation. No analysis of intermediate reasoning step correctness or root-cause failure mechanisms. Does the proposed Compositional Prompting (COMP) method scale beyond GPT-3.5-Turbo, and can it close the human-LLM robustness gap?",
    "building_blocks": [
      "8-type perturbation taxonomy",
      "PDR/ASP robustness metrics",
      "Polya-grounded evaluation framework",
      "Compositional Prompting (COMP)"
    ],
    "relevance_to_seed": "Provides our perturbation taxonomy and one evaluation benchmark (GSM-Plus); the finding that SFT doesn't fix robustness directly motivates training-time interventions like MACR."
  },
  {
    "title": "CREAM: Consistency Regularized Self-Rewarding Language Models",
    "venue": "ICLR 2025",
    "problem_identification": "Observed that 7B self-rewarding LMs degrade after 2-3 iterations (Llama-2 7B: ARC-Easy drops 60.44%→46.55%) due to compounding errors in self-generated preference labels — each iteration's reward inaccuracies snowball into corrupted training data.",
    "key_insight": "Cross-iteration reward consistency (measured via Kendall's Tau between current and previous model rankings) provides a lightweight, principled signal for preference data reliability — disagreement between iterations indicates unreliable labels that should be downweighted.",
    "innovation_type": "new_technique",
    "method_summary": "Computes global consistency rate C via Kendall's Tau between rankings from consecutive model checkpoints. Proves (Theorem 3.3) this is equivalent to soft-labeled DPO: L = C·L_DPO(chosen,rejected) + (1-C)·L_DPO(rejected,chosen), effectively label-smoothing for preferences. Lemma 3.4 links empirical Tau to the regularization parameter. Only requires two checkpoints — no ensembles.",
    "limitations_and_open_questions": "Limited to 7B-13B scale; ranking accuracy tops ~70% (acknowledged as unsatisfying). Requires at least SFT-level alignment to bootstrap. Does the consistency principle transfer to RL training objectives beyond DPO, and to domain-specific (e.g., math) rather than general preference alignment?",
    "building_blocks": [
      "Cross-iteration consistency as regularization signal",
      "Soft-labeled DPO formulation",
      "Kendall's Tau as dynamic regularization strength",
      "Reversed-DPO loss component"
    ],
    "relevance_to_seed": "Validates consistency regularization within iterative LLM training (RL-adjacent); the cross-iteration consistency principle parallels MACR's cross-perturbation consistency — both use agreement signals to stabilize training."
  },
  {
    "title": "rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking",
    "venue": "ICML 2025 (Oral)",
    "problem_identification": "Identified three bottlenecks: diminishing returns from CoT data scaling (OpenMathInstruct-2: 8× data → only 3.9% gain), weak open-source test-time compute scaling due to poor reward models, and the PRM training dilemma — MCTS Q-values are too noisy for regression-based PRM training but human step-level annotations are prohibitively expensive.",
    "key_insight": "Reframing process reward model training from regression (predict precise Q-values) to preference ranking (which step is better?) dramatically improves PRM quality because Q-values, while too noisy for absolute scoring, reliably distinguish positive from negative steps — a much weaker requirement.",
    "innovation_type": "combination",
    "method_summary": "Introduces Process Preference Model (PPM) trained with Bradley-Terry pairwise loss on MCTS-derived preference pairs (top-2 vs. bottom-2 Q-value candidates sharing identical context). Runs 4-round self-evolution: MCTS generates code-augmented CoT trajectories, PPM trains on resulting preferences, improved PPM guides next-round MCTS. Code execution provides step-level verification. Achieves 90% MATH with Qwen-7B.",
    "limitations_and_open_questions": "Massive compute (10 nodes × 8 H100s for weeks); Round 1 bootstraps from 236B-parameter model. PPM robustness to adversarial perturbations is untested — if surface-form changes corrupt Q-value orderings, the preference pair construction breaks. Does PPM quality degrade under distribution shift?",
    "building_blocks": [
      "Process Preference Model (PPM) with Bradley-Terry loss",
      "MCTS-guided CoT trajectory generation",
      "Code-augmented step verification",
      "4-round policy-PRM co-evolution"
    ],
    "relevance_to_seed": "Demonstrates PRM is the performance bottleneck in RL-for-math, directly motivating MACR's perturbation-robust PRM extension; PPM's preference-based formulation suggests a natural integration point for consistency-based robustness."
  },
  {
    "title": "Robust Reasoning Benchmark",
    "venue": "arXiv 2026",
    "problem_identification": "Observed that prior adversarial benchmarks (GSM-Symbolic, GSM-Plus) conflate reasoning failures with arithmetic failures by changing numerical values. Identified that it was unknown whether competition-math (AIME) performance reflects robust reasoning or fragile pattern-matching on standard formatting.",
    "key_insight": "You can isolate pure structural fragility without touching mathematical content — 13 deterministic, reversible textual transformations preserve exact mathematical state while exposing that LLM reasoning is overfit to standard presentation, with failures attributable to tokenization breakdown and attention dilution rather than mathematical incompetence.",
    "innovation_type": "new_benchmark",
    "method_summary": "Applies 13 perturbations across 4 categories to AIME 2024/2025: semantic substitutions (double negation, antonyms, wrappers), contextual overload (line/word/symbol interleaving), syntactic distortions (sentence/word/symbol reversal), and visual encodings (Rail Fence cipher, rectangle perimeter, snake patterns). All transformations are algorithmically invertible with explicit decoding protocols provided in prompts. Separately studies Intra-Query Attention Dilution via sequential problem contexts.",
    "limitations_and_open_questions": "AIME-only domain; proprietary models tested less comprehensively. Claude's failures stem from safety-filter refusals, not reasoning — raising questions about confounding. The concept of 'atomic reasoning unit' (maximum computation before structural noise degrades logic) is proposed but not formally quantified.",
    "building_blocks": [
      "13 deterministic reversible perturbation types",
      "Failure mode taxonomy (cognitive thrashing, tokenization breakdown)",
      "IQAD attention dilution analysis",
      "Competition-math robustness evaluation"
    ],
    "relevance_to_seed": "Validates MACR's focus on competition-level math robustness; finding that open-weights models drop ~47-54% on AIME under surface-only changes confirms the problem persists at competition level and is not limited to GSM-level math."
  },
  {
    "title": "VAR-MATH: Probing True Mathematical Reasoning in LLMs via Symbolic Multi-Instance Benchmarks",
    "venue": "arXiv 2025",
    "problem_identification": "Standard math benchmarks use fixed numerical instances susceptible to data contamination and pattern memorization; the authors identified that RL-trained models show gains even with flawed reward signals, suggesting performance reflects memorized surface patterns rather than genuine mathematical reasoning.",
    "key_insight": "By converting competition problems into parameterized symbolic templates with feasible variable domains, you can generate unlimited structurally equivalent instances that expose whether a model has learned the mathematical structure or merely memorized specific numerical patterns.",
    "innovation_type": "new_benchmark",
    "method_summary": "VAR-MATH applies a four-step variabilization pipeline: structural analysis of algebraic relationships, symbolic parameterization (replacing constants with constrained variables via Random_linespace/Random_Set specifications), parametric solution formulation (answers as symbolic functions), and precision specification for numerical stability. They transform AMC23, AIME24, and AIME25 into symbolic benchmarks and evaluate models on multiple instantiations per problem. Two metrics are introduced: strict (all-or-nothing across all variants) and loose (average accuracy), separating contamination effects from reasoning instability.",
    "limitations_and_open_questions": "Only 3 competition benchmarks are variabilized; the process requires expert mathematical analysis per problem and cannot be fully automated. The largest models (DeepSeek-R1, SEED-THINK) show minimal drops, raising the question of whether scale alone solves the problem, which would undermine training-time interventions like MACR.",
    "building_blocks": [
      "VAR-AMC23/AIME24/AIME25 benchmarks",
      "Symbolic parameterization pipeline for math problems",
      "Strict vs. loose evaluation metrics for reasoning consistency",
      "Per-model drop quantification methodology"
    ],
    "relevance_to_seed": "Provides the most direct motivation for MACR by quantifying 47.9–72.9% accuracy drops specifically for RL-trained models on competition math, and supplies ready-made evaluation benchmarks (VAR-AMC23/AIME24/AIME25) for measuring MACR's effectiveness."
  },
  {
    "title": "Flip-Flop Consistency: Unsupervised Training for Robustness to Prompt Perturbations in LLMs",
    "venue": "arXiv 2025",
    "problem_identification": "LLMs produce inconsistent predictions across semantically equivalent prompt phrasings, undermining deployment reliability; prior work focused on prompt engineering or ensembling at inference time rather than training the model to be inherently invariant.",
    "key_insight": "A model's own majority vote across prompt variations provides sufficient signal—without any labeled data—to train consistency via pseudo-labels, making the approach fully unsupervised and scalable.",
    "innovation_type": "new_technique",
    "method_summary": "F²C combines two losses: Consensus Cross-Entropy (CCE), which creates hard pseudo-labels from majority vote across V prompt variations and trains all variations toward the consensus; and a representation alignment loss using KL divergence to pull non-confident/non-majority predictions toward confident majority predictions, weighted by a sigmoid-scaled confidence gap. A JSD term enforces agreement within the high-confidence set. Training uses LoRA on Qwen2.5-3B-Instruct with dynamic per-instance partitioning into confident-consensus (CC) and non-confident (NC) sets.",
    "limitations_and_open_questions": "Evaluated only on classification tasks with a 3B model; open-ended generation, chain-of-thought reasoning, and larger models untested. Relies on availability of multiple prompt templates—a constraint that doesn't map directly to math problems. The majority-vote pseudo-label assumption may fail when the model is systematically wrong, which is common in hard math.",
    "building_blocks": [
      "JS-divergence consistency loss formulation",
      "Consensus pseudo-labeling from majority vote",
      "CC/NC dynamic partitioning algorithm",
      "KL-based representation alignment with confidence weighting"
    ],
    "relevance_to_seed": "MACR's direct methodological ancestor: the CCE + JSD + KL loss architecture can be adapted from classification-over-prompt-variations to RL-over-math-perturbations, but requires replacing template-based prompt perturbations with math-equivalence-preserving transformations and integrating into GRPO's policy gradient rather than SFT."
  },
  {
    "title": "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning",
    "venue": "Nature 2025",
    "problem_identification": "Prior reasoning LLMs depended on large-scale supervised chain-of-thought data (expensive, bottlenecked by human annotation); DeepSeek identified that rule-based verifiable rewards alone might suffice to elicit reasoning if the RL algorithm is efficient enough to avoid critic-model overhead.",
    "key_insight": "GRPO eliminates the critic model by estimating advantage from group-relative reward normalization, making pure RL on base LLMs computationally tractable and enabling emergent reasoning behaviors (self-reflection, verification, strategy adaptation) without any supervised reasoning demonstrations.",
    "innovation_type": "combination",
    "method_summary": "GRPO samples G outputs per query, computes advantages as normalized deviations from group mean reward, and optimizes a clipped surrogate objective with KL regularization against a reference policy—no value network needed. The full pipeline has four stages: cold-start SFT on curated CoT examples, reasoning-focused RL with rule-based accuracy/format rewards, rejection sampling to generate 800K diverse SFT examples, and a final general-purpose RL phase. Rule-based rewards deliberately avoid neural reward models to prevent reward hacking at scale.",
    "limitations_and_open_questions": "The reward signal is purely outcome-based (correct final answer), providing no gradient for process quality or perturbation robustness—exactly the gap MACR targets. Training data is opaque (criticized in Nature peer review). PRM and MCTS approaches were tried and failed, suggesting process-level signals are hard to integrate, which is a risk factor for MACR's PRM extension.",
    "building_blocks": [
      "GRPO algorithm (critic-free RL)",
      "Rule-based reward design for math/code",
      "Four-stage training pipeline",
      "Emergent reasoning behavior analysis"
    ],
    "relevance_to_seed": "Defines the exact training paradigm MACR modifies: GRPO's outcome-only reward provides no invariance signal, and MACR's JS-divergence consistency term is designed to fill this gap by adding a perturbation-invariance objective alongside the correctness reward."
  },
  {
    "title": "Adversarial Training for Process Reward Models",
    "venue": "arXiv 2025",
    "problem_identification": "PRMs trained on static datasets with expensive manual step-level annotations generalize poorly to novel reasoning error types; the authors recognized that the static nature of training data creates a distribution mismatch when deployed on diverse downstream problems.",
    "key_insight": "Framing PRM training as a general-sum (not zero-sum) game between a generator that creates plausible reasoning errors and a discriminator PRM yields provably convergent training via OGDA, producing progressively harder negatives without human annotation.",
    "innovation_type": "new_technique",
    "method_summary": "A Llama-3.1-8B generator is trained via PPO to perturb correct reasoning steps into plausible errors that fool the PRM (+1 reward for fooling, -1 for producing correct steps). The PRM learns to detect these errors via binary cross-entropy. Unlike zero-sum formulations, the asymmetric reward structure forms a general-sum game, and training is stabilized using Optimistic Gradient Descent-Ascent (OGDA) with KL and entropy regularization ensuring strong monotonicity and linear convergence to Nash equilibrium. Downstream, the trained PRM serves as a step-level reward signal for GRPO, yielding +6.8–10.4pp gains over outcome-based RL on Gemma-3-12B.",
    "limitations_and_open_questions": "The adversarial errors target reasoning mistakes (calculation errors, logical gaps), not surface-form variations of equivalent problems—a fundamentally different robustness axis than what MACR addresses. Whether the two approaches compose (perturbation-robust PRM + consistency-regularized policy) remains untested.",
    "building_blocks": [
      "General-sum game formulation for adversarial training",
      "OGDA optimizer for stable GAN-like training",
      "PPO-trained error generator",
      "PRM-as-reward-for-GRPO pipeline"
    ],
    "relevance_to_seed": "Demonstrates that PRM quality directly impacts downstream RL (+6.8–10.4pp), motivating MACR's perturbation-robust PRM extension; the adversarial training framework could be adapted to generate surface-form-equivalent perturbations rather than reasoning errors, creating a complementary robustness signal."
  },
  {
    "title": "Beyond Accuracy: Dissecting Mathematical Reasoning for LLMs Under Reinforcement Learning",
    "venue": "NeurIPS 2025",
    "problem_identification": "RL dramatically improves math accuracy, but the field lacks granular understanding of what cognitive capabilities RL actually enhances—knowing this is critical for designing targeted training interventions rather than hoping undirected RL suffices.",
    "key_insight": "RL does not primarily improve execution of externally provided plans but rather empowers models to formulate and follow internal strategies; paradoxically, explicit human-crafted plans can degrade performance, but RL-trained models are more robust to such interference.",
    "innovation_type": "analysis",
    "method_summary": "SPARKLE evaluates RL's effects along three dimensions: (1) plan following—comparing performance with/without solution skeletons reveals RL models develop superior internal strategies; (2) knowledge integration—providing external facts/theorems shows RL models gain +4.3% while base models drop -5.4%; (3) chain of subproblems—decomposing problems into sequential checkpoints exposes where reasoning chains break. They also introduce SparkleRL-PSS, a two-stage pipeline: Stage 1 trains GRPO on 40K diverse problems, Stage 2 continues on 5.7K hard problems with partial solution scaffolding (0–4 semantic chunks provided as context), achieving 50.42% on AIME24.",
    "limitations_and_open_questions": "The analysis framework doesn't examine surface-form sensitivity—a critical dimension for MACR. The subproblem decomposition finding (50.4% full-problem accuracy but only 17.5% all-subproblems accuracy) suggests RL models may take shortcuts that correlate with pattern-matching rather than systematic reasoning, which is consistent with VAR-MATH's findings.",
    "building_blocks": [
      "Three-dimensional reasoning analysis framework",
      "SparkleRL-PSS partial scaffolding pipeline",
      "Plan-following measurement methodology",
      "Knowledge integration controlled experiments"
    ],
    "relevance_to_seed": "Provides mechanistic understanding of what MACR's consistency term should preserve: RL enhances internal strategy formulation and knowledge integration, so the consistency loss must regularize these capabilities across perturbations without destroying the internal planning that RL develops."
  },
  {
    "title": "AbstRaL: Augmenting LLMs' Reasoning by Reinforcing Abstract Thinking",
    "venue": "ICLR 2026",
    "problem_identification": "LLMs suffer accuracy drops under trivial distribution shifts (numerical substitution, variable renaming, distractor insertion) because they pattern-match on surface features rather than reasoning abstractly. The authors identified that prior robustness work focused on evaluation or data augmentation but lacked a training-time intervention targeting the root cause: absence of abstract problem representations.",
    "key_insight": "Teaching LLMs to explicitly de-contextualize math problems into symbolic abstractions (replacing specific values with placeholder variables) before solving, trained via RL rather than SFT which fails to produce faithful abstractions, forces representations invariant to surface-form changes.",
    "innovation_type": "new_technique",
    "method_summary": "AbstRaL constructs GranulAR (Granularly-decomposed Abstract Reasoning) data by having an oracle LLM rewrite CoT solutions with abstract symbols (e.g., '12' → '[in0]') within socratic decomposition structure, verified by symbolic solvers. A two-stage pipeline applies SFT on GranulAR data followed by GRPO RL training with two model-free rewards: a symbolic distance reward (edit distance to gold abstraction) and an answer correctness reward. This avoids training a separate reward model while directly incentivizing faithful abstraction.",
    "limitations_and_open_questions": "Evaluated only on GSM-level math (not competition-level AIME/Putnam); depends on a strong oracle LLM (70B) for data generation; abstractions are rigid symbolic templates rather than learned invariances — unclear if this scales to problems requiring flexible mathematical reformulation rather than simple variable substitution.",
    "building_blocks": [
      "GranulAR abstraction data pipeline",
      "GRPO with symbolic distance reward",
      "Two-stage SFT→RL training for reasoning robustness",
      "GSM-Symbolic and GSM-Plus evaluation protocols"
    ],
    "relevance_to_seed": "Primary comparison baseline for MACR — AbstRaL targets the same robustness problem but via explicit abstraction rather than invariance-enforcing consistency regularization, and is limited to GSM-level math, leaving competition-level robustness as MACR's key differentiator."
  },
  {
    "title": "Prompt Perturbation Consistency Learning for Robust Language Models",
    "venue": "EACL 2024 Findings",
    "problem_identification": "Fine-tuned LLMs on NLU tasks (intent classification, slot filling) suffer significant accuracy drops from input perturbations (oronyms, synonyms, paraphrasing), and standard data augmentation requires large augmented datasets to partially mitigate this. The authors identified that augmentation addresses symptoms (insufficient coverage) while ignoring the core issue: models learn perturbation-sensitive representations.",
    "key_insight": "Regularizing the JS divergence between output distributions on clean and perturbed inputs during training forces perturbation-invariant representations more efficiently than augmentation alone, recovering 59-69% of perturbation-induced drops with 10× fewer augmented samples.",
    "innovation_type": "cross_domain",
    "method_summary": "PPCL combines three loss terms: L = λ₁Lc + λ₂Lp + λ₃Ljs, where Lc and Lp are cross-entropy losses on clean and perturbed samples respectively, and Ljs is a JS divergence consistency term between the output distributions. JS divergence is chosen over KL for its symmetry: JS(ŷc‖ŷp) = ½(KL(ŷc‖ŷm) + KL(ŷp‖ŷm)) where ŷm is the averaged distribution. For variable-length paraphrases, divergence is computed on averaged probability distributions rather than token-aligned pairs.",
    "limitations_and_open_questions": "Applied only to NLU classification tasks (IC/SF), not generative reasoning; perturbations are surface-level text transformations (not math-equivalence-preserving); SFT-only with no RL integration — the gap of adapting this consistency framework to RL training and mathematical domains remains entirely open.",
    "building_blocks": [
      "JS divergence consistency loss formulation",
      "Three-term loss weighting (clean + perturbed + consistency)",
      "Evidence that consistency loss > pure augmentation",
      "Perturbation type taxonomy (oronyms/synonyms/paraphrasing)"
    ],
    "relevance_to_seed": "Provides the core theoretical and empirical grounding that MACR adapts: the JS consistency loss formulation and the critical evidence that consistency regularization outperforms pure data augmentation with far fewer samples — MACR's key claim that the consistency term matters beyond augmentation rests on PPCL's precedent."
  },
  {
    "title": "DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models",
    "venue": "arXiv 2024",
    "problem_identification": "PPO-based RL for mathematical reasoning requires training a separate critic/value network, roughly doubling memory requirements and adding training instability, making it impractical for large-scale math reasoning models. The authors identified that the critic model is unnecessary when reward signals are verifiable (math correctness) and advantages can be estimated from group statistics.",
    "key_insight": "Replacing the learned value baseline in PPO with group-relative normalization of rewards — computing advantages as Ai = (ri − mean(r))/std(r) within a sampled group — eliminates the critic model entirely while providing stable advantage estimates for verifiable tasks.",
    "innovation_type": "simplification",
    "method_summary": "GRPO samples G responses per question from the current policy, assigns binary correctness rewards, and normalizes within-group to compute advantages. The policy is updated via a clipped surrogate objective (identical to PPO's clip) plus a KL divergence penalty β·DKL(πθ‖πref) to prevent drift from the reference model (β=0.04). This achieves ~50% memory reduction over PPO by eliminating the value network. Combined with a web-scale math pretraining pipeline (120B tokens selected from Common Crawl), DeepSeekMath-7B achieved 51.7% on MATH.",
    "limitations_and_open_questions": "GRPO's group-relative advantage is a biased estimator when group sizes are small or reward distributions are skewed; the binary reward signal provides no gradient for partial correctness or reasoning quality; no analysis of robustness to problem perturbations — the reward signal optimizes for correct answers on fixed problem forms without penalizing surface-form dependence.",
    "building_blocks": [
      "GRPO algorithm (the RL backbone MACR extends)",
      "Group-relative advantage estimation",
      "Clipped objective + KL penalty framework",
      "Web-scale math data selection pipeline"
    ],
    "relevance_to_seed": "GRPO is the specific RL algorithm MACR extends — MACR adds a JS-divergence consistency term to GRPO's objective, requiring understanding of how the group sampling, advantage computation, and KL penalty interact with an additional regularization loss on paired (original, perturbed) problem groups."
  },
  {
    "title": "Scaling Behaviors of LLM Reinforcement Learning Post-Training: An Empirical Study in Mathematical Reasoning",
    "venue": "ACL 2026",
    "problem_identification": "Despite widespread adoption of RL post-training for math reasoning, no systematic characterization existed of how model scale, data volume, and compute budget interact — practitioners relied on ad-hoc hyperparameter choices. The authors identified this gap by running controlled GRPO experiments across the full Qwen2.5 series (0.5B–72B).",
    "key_insight": "RL post-training performance follows a predictive power-law log L(N,X) = −k(N)·log X + E(N) where learning efficiency k(N) saturates via k(N) = Kmax/(1+N₀/N), enabling extrapolation of larger-model performance from smaller-scale experiments and revealing diminishing returns beyond ~32B parameters.",
    "innovation_type": "scaling",
    "method_summary": "The study uses GRPO across Qwen2.5 0.5B–72B models with controlled hyperparameters (lr=1e-6, batch=512, variable rollout sizes 4–32). They fit power-law models to test loss as a function of compute and data, discovering predictive relationships (R²>0.99 intra-model). A key finding is that data reuse up to 25× repetition produces no significant degradation, with performance governed by total optimization steps rather than sample uniqueness. The saturation curve reveals practical efficiency ceilings at extreme scales.",
    "limitations_and_open_questions": "Mathematical RL shows negligible transfer to out-of-domain tasks; scaling laws characterized only for GRPO (not PPO or other RL variants); does not address robustness — all scaling analysis assumes clean benchmark performance without perturbation evaluation.",
    "building_blocks": [
      "Power-law scaling formulas for RL post-training",
      "Data reuse tolerance bounds (≤25×)",
      "Compute-optimal model-size guidance for budget-constrained experiments",
      "GRPO hyperparameter configurations across model scales"
    ],
    "relevance_to_seed": "Directly informs MACR's experimental design: validates 7B as a cost-effective primary model size, confirms GRPO's stability across scales for the 14B verification experiments, and the data reuse finding suggests MACR's perturbation-augmented training data can be recycled without degradation within the 200 H100-hour budget."
  },
  {
    "title": "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters",
    "venue": "ICLR 2025 (Oral)",
    "problem_identification": "Prior work on test-time compute scaling provided largely negative results, and no framework existed for compute-optimal allocation across problem difficulties. The authors identified that uniform allocation wastes compute on easy problems and starves hard ones, and that the choice between parallel search vs. sequential revision depends critically on question difficulty.",
    "key_insight": "Difficulty-conditioned allocation of test-time compute — selecting between PRM-guided beam search and sequential revision per difficulty bin — achieves 4× efficiency over best-of-N and allows a smaller model to match a 14× larger model on easy-to-medium questions under FLOPs-matched evaluation.",
    "innovation_type": "new_formulation",
    "method_summary": "The paper studies two mechanisms: (1) PRM-guided search (best-of-N weighted, beam search, lookahead search) where PRMs score intermediate steps to prune/select solution paths, and (2) sequential revision where models iteratively improve answers conditioned on prior incorrect attempts. Questions are binned into five difficulty quantiles via pass@1 rates estimated from 2048 samples. A compute-optimal strategy independently selects the best mechanism per bin on a validation fold. Key finding: beam search dominates at small budgets but best-of-N wins at large budgets due to PRM exploitation/overoptimization.",
    "limitations_and_open_questions": "PRM quality is the bottleneck — beam search degrades at high compute due to reward model exploitation; PRMs are not robust to surface-form variations of equivalent problems; difficulty estimation requires 2048 samples per question, limiting practicality; the 14× comparison holds only for easy/medium questions with low inference-to-pretraining ratio.",
    "building_blocks": [
      "Difficulty-conditioned compute allocation framework",
      "PRM exploitation analysis (beam search vs. best-of-N tradeoff)",
      "Sequential revision training via edit-distance pairing",
      "FLOPs-matched train-time vs. test-time compute comparison methodology"
    ],
    "relevance_to_seed": "Establishes that PRM quality is the critical bottleneck for test-time compute scaling — PRM exploitation at high compute directly motivates MACR's perturbation-robust PRM extension, since a PRM that is invariant to surface-form variations would be less susceptible to reward hacking during search."
  },
  {
    "title": "MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations",
    "venue": "ICML 2025",
    "problem_identification": "Prior perturbation benchmarks (GSM-Symbolic, VAR-MATH) only tested structure-preserving modifications; no benchmark existed for 'hard' perturbations that fundamentally change the problem's mathematical structure, requiring entirely different solution methods.",
    "key_insight": "The distinction between simple perturbations (same method, different numbers) and hard perturbations (same surface form, different required method) reveals a novel failure mode: 'blind technique application' where models apply memorized solution strategies without verifying applicability to the modified problem.",
    "innovation_type": "new_benchmark",
    "method_summary": "279 level-5 MATH problems were modified by 12 PhD-level annotators into simple (structure-preserving) and hard (structure-changing) variants with minimal textual edits but different answers. Error analysis taxonomizes failures into assumption ignorance (40%), blind technique application, and answer memorization. ICL experiments show that providing original-problem demonstrations actively hurts performance on hard perturbations (18-40% degradation), confirming models transfer solution templates rather than reason from scratch.",
    "limitations_and_open_questions": "Small scale (279 problems) limits statistical power; level-5 only may miss difficulty-dependent failure patterns; no training-time mitigation is proposed — purely diagnostic. Does 'blind application' correlate with training data frequency of specific solution templates?",
    "building_blocks": [
      "Simple vs. hard perturbation taxonomy",
      "Blind technique application error category",
      "ICL-as-diagnostic methodology",
      "Level-5 MATH perturbation dataset"
    ],
    "relevance_to_seed": "Provides a key evaluation benchmark for MACR and validates that structure-changing perturbations (which MACR's discrimination loss targets) are fundamentally harder than the structure-preserving perturbations (which MACR's consistency term targets)."
  },
  {
    "title": "Causal Consistency Regularization: Training Verifiably Sensitive Reasoning in Large Language Models",
    "venue": "arXiv 2025",
    "problem_identification": "Standard training rewards final-answer correctness regardless of whether intermediate reasoning steps causally determine the answer, allowing models to produce correct outputs via unfaithful reasoning (36-42% of cases in standard fine-tuning).",
    "key_insight": "Faithfulness can be enforced by penalizing invariance of predictions under operator-level counterfactual interventions on reasoning traces — if swapping '+' to '−' doesn't change the answer, the model isn't actually using that reasoning step.",
    "innovation_type": "new_technique",
    "method_summary": "CSR adds a KL-divergence term L_CSR = D_KL(p(Y|T,X) || p(Y|T',X)) penalizing unchanged predictions under counterfactual traces T'. A learned 6-layer Transformer editor generates minimal, causally significant perturbations (operator swaps, entity substitutions) optimized via REINFORCE for validity, impact, and minimality. Warm-start curriculum and token-subset optimization keep overhead at ~9%. Faithfulness measured via Counterfactual Outcome Sensitivity (COS): CSR achieves +32-35 COS points across GSM8K, HotpotQA, and ProofWriter with p<0.001.",
    "limitations_and_open_questions": "SFT-only (no RL integration); effectiveness degrades below 50% operator identification precision, limiting applicability to unstructured domains; targets faithfulness (does the model use its reasoning?) rather than perturbation invariance (does the model handle equivalent problems identically?) — complementary but distinct goals.",
    "building_blocks": [
      "Learned counterfactual trace editor",
      "COS faithfulness metric",
      "Warm-start curriculum for regularization overhead",
      "Operator-level intervention framework"
    ],
    "relevance_to_seed": "Closest methodological cousin to MACR — both use consistency regularization during training but differ on three axes: CSR perturbs reasoning traces vs. MACR perturbs problem inputs; CSR targets faithfulness vs. MACR targets invariance; CSR is SFT-only vs. MACR integrates with RL. MACR should cite CSR's overhead management techniques."
  },
  {
    "title": "Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?",
    "venue": "NeurIPS 2025 (Best Paper Runner-Up)",
    "problem_identification": "The community assumed RLVR enables models to discover novel reasoning strategies (analogous to AlphaGo), but no systematic study had tested whether RL-trained models solve problems the base model fundamentally cannot, versus merely sampling existing solutions more efficiently.",
    "key_insight": "RLVR functions as a distribution sharpener, not a capability expander — at large k, base models achieve higher pass@k than their RL-trained counterparts, and 13.3% of AIME24 problems are solvable only by the base model, proving RL narrows the solution space.",
    "innovation_type": "analysis",
    "method_summary": "Uses unbiased pass@k at large k as a boundary probe across math, code, and visual reasoning, comparing six RLVR algorithms (PPO, GRPO, Reinforce++, ReMax, etc.) against base models. Coverage analysis reveals almost every RL-model solution exists in the base distribution. Distillation serves as a positive control, demonstrating genuine capability expansion when superior teacher data is introduced — proving the methodology can detect expansion when it exists
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
  "promptId": "b45e719a-33c9-42df-a409-c2c10b2f1aa7",
  "type": "user",
  "uuid": "53284b7b-bb95-44b7-9cd4-6fa4759d79e2",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5426ac1b-6861-47ee-b4fa-9d7f4ce993ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T07:33:33.301Z_

```json
{
  "parentUuid": "53284b7b-bb95-44b7-9cd4-6fa4759d79e2",
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
  "uuid": "3fde373d-9c8b-4196-bf6e-1d2679244572",
  "timestamp": "2026-05-29T07:33:33.301Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5426ac1b-6861-47ee-b4fa-9d7f4ce993ea",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T07:33:33.301Z_

```json
{
  "parentUuid": "3fde373d-9c8b-4196-bf6e-1d2679244572",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "53b4e1d6-1890-44b7-9e12-b9197c6a6faa",
  "timestamp": "2026-05-29T07:33:33.301Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5426ac1b-6861-47ee-b4fa-9d7f4ce993ea",
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
  "leafUuid": "53b4e1d6-1890-44b7-9e12-b9197c6a6faa",
  "sessionId": "5426ac1b-6861-47ee-b4fa-9d7f4ce993ea"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesizing RL-based math reasoning robustness strategies for AAAI 2026",
  "sessionId": "5426ac1b-6861-47ee-b4fa-9d7f4ce993ea"
}
```

---

### Assistant

_source line 8 · 2026-05-29T07:33:59.502Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to synthesize 20 paper analyses into a strategic "Field Guide" for innovation in the area of RL-trained mathematical reasoning robustness. Let me carefully analyze the papers and produce a comprehensive, evidence-based JSON document.

Let me organize my thinking by the required sections:

**Innovation Patterns:**
1. "Benchmark-first" - Create a diagnostic benchmark that exposes a failure mode, then the community builds solutions. GSM-Symbolic, GSM-Plus, VAR-MATH, MATH-Perturb, Robust Reasoning Benchmark all follow this.


2. "Consistency regularization transfer" - Adapt regularization techniques across domains, like F²C bringing NLP methods into math, PPCL applying NLU approaches, and CSR extending faithfulness principles to reasoning.
3. "Simplification of complex pipelines" - Strip away unnecessary components to improve efficiency, as GRPO did by removing the critic from PPO and DeepSeekMath streamlined its entire training workflow.
4. "Adversarial co-training" - Pair generators with discriminators in training loops, seen in APRM and rStar-Math's self-evolution mechanisms.
5. "Analysis-driven intervention" - SPARKLE demonstrates how analyzing RL behavior informs the design of targeted improvements like SparkleRL-PSS.

Now I'm looking at the reviewer preferences and field gaps. The key missing pieces are consistency regularization applied to RL for math problems, robust process reward models that handle perturbations, and a deeper understanding of how RL affects solution diversity. There's also no work integrating faithfulness with invariance properties, and no training-time robustness interventions at competition level.

I'm considering several untried combinations that could address these gaps: pairing consistency losses with GRPO and math-specific perturbations, combining adversarial training with surface-form robustness, dual regularization for both faithfulness and perturbation invariance, and integrating abstraction-based approaches with consistency constraints. The building blocks are already available—consistency losses from prior work, the GRPO algorithm, symbolic parameterization, adversarial training methods, and process preference models—so the main work is assembling them into a coherent framework that handles process-level rewards robust to surface form variations.

I need to be careful about common pitfalls like limiting evaluation to basic math benchmarks, overlooking accuracy degradation, and conflating different training techniques. The field is moving toward training-time interventions on harder problems with process-aware methods, so I should focus on closing the gap between consistency regularization and RL integration while demonstrating results on competition-level math with thorough ablations.

Writing this up as structured JSON...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53b4e1d6-1890-44b7-9e12-b9197c6a6faa",
  "isSidechain": false,
  "requestId": "req_011CbWUMgph4qwD9ZhD2WtdW",
  "type": "assistant",
  "uuid": "7fcc2aae-1ca9-4913-9b21-ca3797ee60a7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5426ac1b-6861-47ee-b4fa-9d7f4ce993ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0143queA7rs5PN5L8dD6d6TF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13083,
      "cache_read_input_tokens": 11014,
      "output_tokens": 8641,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13083,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 8641,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 13083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13083
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

_source line 9 · 2026-05-29T07:37:02.156Z_

I'll analyze the 20 papers carefully to synthesize a strategic field guide. Let me work through the patterns systematically.

```json
{
  "innovation_patterns": [
    {
      "pattern": "Benchmark-as-Thesis",
      "description": "Construct a diagnostic benchmark that operationalizes a specific claim about model failure, making the claim falsifiable and generating immediate community uptake. The benchmark IS the contribution — it reframes what the community measures and therefore what it optimizes for. Success requires: (1) a clean experimental design that isolates one variable, (2) a surprising quantitative finding that challenges conventional wisdom, and (3) sufficient scale/diversity to resist 'cherry-picking' critiques.",
      "examples": ["GSM-Symbolic (ICLR 2025)", "VAR-MATH (arXiv 2025)", "GSM-Plus (ACL 2024)", "MATH-Perturb (ICML 2025)", "Robust Reasoning Benchmark (arXiv 2026)"],
      "success_rate": "high"
    },
    {
      "pattern": "Cross-Domain Technique Transfer with Domain-Specific Adaptation",
      "description": "Take a well-validated technique from an adjacent field (NLP classification, NLU robustness, causal inference) and adapt it to mathematical reasoning by replacing the domain-agnostic component with a math-aware equivalent. The adaptation is non-trivial because mathematical equivalence has richer structure than textual paraphrase — symbolic verification, numerical re-parameterization, and structural preservation must replace surface-level text transformations. Papers succeed when they clearly articulate what makes the transfer non-obvious.",
      "examples": ["F²C (NLP consistency → prompt robustness)", "PPCL (NLU perturbation → consistency regularization)", "CSR (causal inference → reasoning faithfulness)", "AbstRaL (symbolic abstraction → RL robustness)"],
      "success_rate": "high"
    },
    {
      "pattern": "Pipeline Simplification via Principled Elimination",
      "description": "Remove a costly component (critic network, human annotations, separate reward model) by proving that a simpler alternative achieves equivalent or better results. The key is providing theoretical justification for why the component was unnecessary — not just empirical evidence. GRPO eliminated the critic via group-relative normalization; APRM eliminated human step-level annotations via adversarial generation; rStar-Math replaced regression PRM with preference-based PPM.",
      "examples": ["GRPO/DeepSeekMath (eliminate critic)", "rStar-Math (regression → preference PRM)", "APRM (human annotations → adversarial generation)"],
      "success_rate": "high"
    },
    {
      "pattern": "Provocative Negative Result with Mechanistic Explanation",
      "description": "Demonstrate that a widely assumed capability (RL expands reasoning, SFT improves robustness, scaling solves fragility) does not hold, then provide a mechanistic explanation. The negative result alone is insufficient — reviewers reward the 'why' more than the 'what'. 'Does RL Really Incentivize' earned Best Paper Runner-Up by showing RL is a distribution sharpener with pass@k boundary analysis; SPARKLE's plan-following analysis revealed RL builds internal strategies that explicit plans can degrade.",
      "examples": ["Does RL Really Incentivize Reasoning (NeurIPS 2025 Best Paper Runner-Up)", "SPARKLE/Beyond Accuracy (NeurIPS 2025)", "GSM-Symbolic (ICLR 2025)"],
      "success_rate": "medium"
    },
    {
      "pattern": "Adversarial Co-Training with Convergence Guarantees",
      "description": "Frame a training problem as a game between a generator (of hard examples/errors) and a discriminator (reward model/policy), then stabilize training via game-theoretic optimization (OGDA, general-sum formulation). The convergence guarantee differentiates this from ad-hoc adversarial training. APRM's general-sum formulation with OGDA achieved linear convergence to Nash equilibrium.",
      "examples": ["APRM (adversarial PRM training)", "rStar-Math (4-round policy-PRM co-evolution)"],
      "success_rate": "medium"
    },
    {
      "pattern": "Scaling Law Characterization for Practical Guidance",
      "description": "Run controlled experiments across model sizes/data volumes/compute budgets to derive predictive power-law relationships, enabling practitioners to extrapolate performance without running full-scale experiments. Requires comprehensive coverage (multiple model sizes) and statistical rigor (R² reporting, confidence intervals).",
      "examples": ["Scaling Behaviors of LLM RL Post-Training (ACL 2026)", "Scaling LLM Test-Time Compute (ICLR 2025 Oral)"],
      "success_rate": "medium"
    }
  ],

  "reviewer_preferences": [
    "Clean accuracy preservation is non-negotiable: any robustness method that degrades unperturbed performance by >2 points will face strong pushback. GSM-Plus found SFT improves accuracy but not robustness — reviewers expect MACR-type methods to improve robustness WITHOUT this accuracy tax. AbstRaL succeeded partly because it maintained or improved clean accuracy.",
    "Augmentation-only baselines are mandatory: PPCL's strongest evidence was showing consistency regularization recovers 59-69% of perturbation drops with 10× fewer augmented samples than pure augmentation. Any consistency-based method must include the 'just add perturbed data without the consistency loss' ablation — if the gap is small, reviewers will reject the consistency term as unnecessary overhead.",
    "Competition-level math evaluation is now expected: GSM-level-only papers face the 'toy benchmark' critique. VAR-MATH, Robust Reasoning Benchmark, and MATH-Perturb all evaluate on AIME/competition math. AbstRaL's GSM-only limitation is explicitly noted as a weakness in multiple follow-up papers. Reviewers at AAAI/NeurIPS/ICLR now expect at least one competition-level benchmark.",
    "Statistical rigor over point estimates: GSM-Symbolic was challenged (Ivanova critique) for lacking proper confidence intervals. VAR-MATH's strict vs. loose metrics and distributional evaluation methodology set the new standard. Reviewers expect Wilson intervals, multiple random seeds, and significance testing — especially when claiming improvements are meaningful.",
    "Mechanistic analysis beyond accuracy numbers: SPARKLE's three-dimensional analysis (plan following, knowledge integration, subproblem chains) and 'Does RL Really Incentivize's pass@k boundary probing both demonstrate that reviewers reward understanding WHY a method works, not just THAT it works. Include analysis of what the consistency term actually changes in learned representations or reasoning patterns.",
    "Compute budget transparency and reproducibility: Scaling Behaviors (ACL 2026) provides exact GRPO hyperparameters across model scales; DeepSeek-R1 was criticized for opaque training data. Reviewers now expect explicit compute accounting (H100-hours), hyperparameter sensitivity analysis, and sufficient detail for reproduction. The ≤200 H100-hour constraint should be reported as a feature, not hidden.",
    "Transfer to held-out perturbation types: The distinction between interpolation (handling perturbation types seen during training) and extrapolation (handling novel perturbation types) is critical. MATH-Perturb's simple vs. hard perturbation taxonomy and GSM-Plus's 8-type framework set the expectation that robustness methods must generalize beyond training-time perturbation distributions."
  ],

  "field_gaps": [
    {
      "gap": "No consistency regularization (JS/KL divergence) applied during RL training for mathematical reasoning — F²C and PPCL remain NLP/SFT-only, and CSR targets faithfulness not perturbation invariance",
      "evidence": "F²C evaluated only on classification tasks with 3B model, explicitly noting open-ended generation untested; PPCL applied only to NLU (IC/SF) with no RL integration; CSR is SFT-only and targets reasoning trace faithfulness, not input perturbation invariance",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "No PRM trained to be robust to surface-form variations of mathematically equivalent problems — APRM addresses reasoning errors but not perturbation invariance, and test-time compute scaling papers show PRM quality is the critical bottleneck",
      "evidence": "APRM's adversarial errors target reasoning mistakes (calculation errors, logical gaps), not surface-form variations; Scaling LLM Test-Time Compute shows beam search degrades at high compute due to PRM exploitation; rStar-Math's PPM robustness to adversarial perturbations is explicitly noted as untested",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "No training-time robustness intervention demonstrated on competition-level math (AIME/Putnam) — AbstRaL is GSM-only, and all perturbation benchmarks at competition level are evaluation-only with no proposed mitigations",
      "evidence": "AbstRaL evaluated only on GSM-level math; VAR-MATH, Robust Reasoning Benchmark, and MATH-Perturb document 47-73% drops at competition level but propose no training interventions; Robust Reasoning Benchmark finds open-weights models drop ~47-54% on AIME under surface-only changes",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "RL training narrows the solution distribution (distribution sharpening) but no method exists to preserve solution diversity while still achieving the accuracy gains of RL",
      "evidence": "'Does RL Really Incentivize' shows base models achieve higher pass@k than RL-trained models at large k, and 13.3% of AIME24 problems are solvable only by the base model; SPARKLE shows RL models develop strong internal strategies but at the cost of flexibility",
      "difficulty": "high",
      "impact_if_solved": "medium"
    },
    {
      "gap": "No framework integrates faithfulness (CSR's goal: model uses its reasoning steps) with invariance (MACR's goal: model handles equivalent problems identically) — these are complementary but no work addresses both simultaneously",
      "evidence": "CSR explicitly targets faithfulness via operator-level interventions on reasoning traces but is SFT-only and does not address input perturbation invariance; F²C/PPCL target invariance but not faithfulness; no paper combines both objectives",
      "difficulty": "medium",
      "impact_if_solved": "medium"
    },
    {
      "gap": "No understanding of how perturbation robustness interacts with test-time compute scaling — a perturbation-robust model may require fundamentally different compute allocation strategies than a standard model",
      "evidence": "Scaling LLM Test-Time Compute's difficulty-conditioned allocation assumes a fixed robustness profile; PRM exploitation analysis does not consider whether robustness training changes the exploitation curve; no paper studies the interaction between training-time robustness and inference-time scaling",
      "difficulty": "medium",
      "impact_if_solved": "medium"
    },
    {
      "gap": "Discrimination between mathematically equivalent and surface-similar-but-semantically-different problems is unexplored — all existing consistency work enforces invariance but none simultaneously trains models to detect when superficially similar changes alter mathematical meaning",
      "evidence": "MATH-Perturb's hard perturbations (same surface form, different required method) reveal 'blind technique application' failures; F²C and PPCL only enforce consistency without contrastive discrimination; AbstRaL's abstraction approach cannot distinguish structure-preserving from structure-changing perturbations",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Scale-dependent robustness is poorly characterized — VAR-MATH notes largest models (DeepSeek-R1, SEED-THINK) show minimal drops, but whether scale alone solves the problem or whether robustness training provides diminishing returns at scale is unknown",
      "evidence": "VAR-MATH raises the question explicitly; Scaling Behaviors (ACL 2026) characterizes scaling laws for accuracy but not robustness; no paper provides scaling laws for perturbation robustness across model sizes",
      "difficulty": "medium",
      "impact_if_solved": "medium"
    }
  ],

  "untried_combinations": [
    {
      "idea_sketch": "JS-divergence consistency regularization (from F²C/PPCL) integrated into GRPO's policy gradient objective, with math-equivalence-preserving perturbation generation replacing NLP paraphrase templates — this is exactly MACR",
      "from_papers": ["F²C", "PPCL", "GRPO/DeepSeekMath", "DeepSeek-R1", "VAR-MATH"],
      "why_promising": "F²C proves JS-divergence consistency works for prompt robustness; PPCL proves it outperforms pure augmentation by 10× sample efficiency; GRPO's group-sampling naturally extends to paired (original, perturbed) groups; VAR-MATH's symbolic parameterization provides ready-made math-equivalence-preserving perturbation generators. The three-way intersection (consistency regularization + RL training + mathematical equivalence) is genuinely novel."
    },
    {
      "idea_sketch": "APRM's adversarial training framework adapted to generate surface-form-equivalent perturbations rather than reasoning errors, producing a perturbation-robust PRM",
      "from_papers": ["APRM", "rStar-Math", "Scaling LLM Test-Time Compute", "VAR-MATH"],
      "why_promising": "APRM proves adversarial PRM training yields +6.8-10.4pp downstream gains; test-time compute scaling shows PRM quality is the bottleneck; rStar-Math's PPM formulation offers a natural integration point. A PRM robust to surface-form variations would resist exploitation during beam search and improve test-time compute scaling, combining two independent high-impact improvements."
    },
    {
      "idea_sketch": "Dual regularization combining CSR's faithfulness enforcement (model must use its reasoning steps) with MACR-style perturbation invariance (model must handle equivalent problems identically) during RL training",
      "from_papers": ["CSR", "F²C", "PPCL", "SPARKLE"],
      "why_promising": "CSR shows faithfulness regularization adds only ~9% overhead via warm-start curriculum; SPARKLE demonstrates RL builds internal strategies that faithfulness constraints should preserve. A dual loss L = L_RL + λ₁L_consistency + λ₂L_faithfulness would simultaneously enforce 'reason the same way across equivalent problems' and 'actually use the reasoning you produce,' addressing the complementary failure modes of surface-form dependence and unfaithful reasoning."
    },
    {
      "idea_sketch": "AbstRaL's explicit abstraction + MACR's consistency regularization as complementary mechanisms: abstraction provides an inductive bias toward invariance, while consistency regularization enforces it even when abstraction fails",
      "from_papers": ["AbstRaL", "F²C", "PPCL", "GSM-Symbolic"],
      "why_promising": "AbstRaL's rigid symbolic templates work at GSM level but may not scale to competition math where flexible mathematical reformulation is needed. Consistency regularization provides a softer invariance signal that doesn't require explicit abstraction templates. The combination could inherit AbstRaL's strong GSM performance while generalizing to competition-level problems where template-based abstraction breaks down."
    },
    {
      "idea_sketch": "CREAM's cross-iteration consistency principle applied to perturbation robustness: measure whether the model's rankings of solution candidates are consistent across perturbed problem variants, and downweight training signals where they disagree",
      "from_papers": ["CREAM", "VAR-MATH", "GRPO/DeepSeekMath"],
      "why_promising": "CREAM proves cross-iteration Kendall's Tau is equivalent to soft-labeled DPO (Theorem 3.3). Replacing 'cross-iteration' with 'cross-perturbation' yields a preference learning signal that naturally penalizes solutions that are correct on one variant but fail on equivalent variants — a mathematically principled way to select for genuinely robust solutions during GRPO training without explicitly computing consistency losses."
    },
    {
      "idea_sketch": "Scaling law characterization for perturbation robustness across model sizes, combined with compute-optimal allocation between clean accuracy training and robustness training",
      "from_papers": ["Scaling Behaviors of LLM RL Post-Training", "Scaling LLM Test-Time Compute", "VAR-MATH"],
      "why_promising": "The ACL 2026 scaling paper provides power-law formulas for clean accuracy but not robustness. If robustness follows different scaling dynamics (e.g., slower improvement, different saturation curves), the compute-optimal balance between standard RL and consistency-regularized RL would shift with model scale. This would provide practical guidance for when robustness training is cost-effective vs. when scaling alone suffices — directly addressing VAR-MATH's open question about whether scale resolves fragility."
    }
  ],

  "method_building_blocks": [
    {
      "tool": "JS-divergence consistency loss",
      "what_it_does": "Penalizes divergence between model output distributions on semantically equivalent inputs: JS(p(y|x) || p(y|x')) = ½(KL(p(y|x)||m) + KL(p(y|x')||m)) where m is the averaged distribution. Symmetric, bounded [0, ln2], and differentiable — advantages over asymmetric KL for bidirectional consistency.",
      "used_by": ["F²C", "PPCL"],
      "could_be_applied_to": "GRPO's policy gradient as an auxiliary loss on paired (original, math-equivalent-perturbed) problem groups, replacing NLP paraphrase templates with symbolic perturbation generators from VAR-MATH"
    },
    {
      "tool": "GRPO algorithm",
      "what_it_does": "Samples G outputs per query, computes advantages as normalized deviations from group mean reward Ai=(ri−μ)/σ, optimizes clipped surrogate objective with KL penalty against reference policy. No critic model needed — ~50% memory savings over PPO.",
      "used_by": ["DeepSeek-R1", "DeepSeekMath", "AbstRaL", "APRM (downstream)", "SPARKLE"],
      "could_be_applied_to": "Extended to sample from both original and perturbed problems within the same group, computing consistency-aware advantages that reward solutions invariant across equivalent problem forms"
    },
    {
      "tool": "VAR-MATH symbolic parameterization pipeline",
      "what_it_does": "Four-step process: structural analysis → symbolic parameterization (constants → constrained variables) → parametric solution formulation → precision specification. Generates unlimited structurally equivalent problem instances from a single template.",
      "used_by": ["VAR-MATH"],
      "could_be_applied_to": "Train-time perturbation generation for MACR — providing mathematically verified equivalent problems during GRPO training, with symbolic verification that perturbations preserve problem structure"
    },
    {
      "tool": "General-sum adversarial training with OGDA",
      "what_it_does": "Frames generator-discriminator training as a general-sum game (not zero-sum) stabilized by Optimistic Gradient Descent-Ascent. KL and entropy regularization ensure strong monotonicity and linear convergence to Nash equilibrium.",
      "used_by": ["APRM"],
      "could_be_applied_to": "Training a perturbation generator that produces maximally challenging surface-form-equivalent problems (not reasoning errors) to adversarially train perturbation-robust PRMs"
    },
    {
      "tool": "Process Preference Model (PPM) with Bradley-Terry loss",
      "what_it_does": "Trains a step-level reward model using pairwise preferences (which reasoning step is better?) rather than regression on Q-values, because Q-values are too noisy for absolute scoring but reliably distinguish positive from negative steps.",
      "used_by": ["rStar-Math"],
      "could_be_applied_to": "A perturbation-robust PPM that additionally requires consistent step rankings across surface-form-equivalent problem variants — extending the preference pairs to include cross-perturbation comparisons"
    },
    {
      "tool": "GranulAR abstraction data pipeline",
      "what_it_does": "Has an oracle LLM rewrite chain-of-thought solutions with abstract symbols (e.g., '12' → '[in0]') within socratic decomposition structure, verified by symbolic solvers. Produces training data that forces models to represent problems abstractly.",
      "used_by": ["AbstRaL"],
      "could_be_applied_to": "Generating the 'abstracted problem representation' that serves as a shared anchor for consistency regularization — instead of regularizing across two concrete perturbations, regularize each perturbation's representation toward a shared abstract form"
    },
    {
      "tool": "Counterfactual Outcome Sensitivity (COS) metric",
      "what_it_does": "Measures whether model predictions change appropriately when reasoning traces are counterfactually modified — quantifies faithfulness as sensitivity to causally relevant changes. +32-35 COS improvement demonstrated via CSR training.",
      "used_by": ["CSR"],
      "could_be_applied_to": "A dual metric for MACR evaluation: COS measures sensitivity to structure-changing perturbations (model SHOULD change its answer) while consistency metrics measure invariance to structure-preserving perturbations (model SHOULD NOT change) — together they characterize the full robustness profile"
    },
    {
      "tool": "Warm-start curriculum for regularization overhead",
      "what_it_does": "Introduces regularization terms gradually during training using a curriculum schedule, keeping total overhead at ~9% despite adding complex consistency/faithfulness losses.",
      "used_by": ["CSR"],
      "could_be_applied_to": "MACR's consistency term — start with pure GRPO, gradually increase the consistency regularization weight λ to avoid early-training interference with reward signal learning"
    },
    {
      "tool": "PDR/ASP robustness metrics",
      "what_it_does": "Performance Drop Rate (PDR) measures relative accuracy drop from clean to perturbed, and Accuracy Spread (ASP) measures variance across perturbation types. Together they separate magnitude from consistency of robustness.",
      "used_by": ["GSM-Plus"],
      "could_be_applied_to": "Standardized MACR evaluation — reporting PDR per perturbation type and ASP across types provides a richer picture than average accuracy, and enables direct comparison with AbstRaL and other baselines"
    },
    {
      "tool": "Data reuse tolerance bounds",
      "what_it_does": "Demonstrates that GRPO training data can be reused up to 25× without significant degradation, with performance governed by total optimization steps rather than sample uniqueness.",
      "used_by": ["Scaling Behaviors of LLM RL Post-Training"],
      "could_be_applied_to": "Budget optimization for MACR — the perturbation-augmented training dataset can be generated once and reused across multiple training runs, reducing the perturbation generation cost within the 200 H100-hour budget"
    }
  ],

  "common_pitfalls": [
    "Evaluating only on GSM-level math and claiming generality: AbstRaL's GSM-only limitation is cited as a weakness by at least 3 subsequent papers (VAR-MATH, Robust Reasoning Benchmark, MATH-Perturb). Any 2026 paper that doesn't evaluate on AIME-level math will face immediate 'toy benchmark' objections. GSM-level results are necessary but insufficient.",
    "Conflating augmentation with regularization: PPCL's key finding is that consistency regularization with 10× fewer samples outperforms pure augmentation. If a paper introduces consistency regularization but fails to include an augmentation-only baseline showing the same perturbed data without the consistency loss, reviewers will (correctly) question whether the contribution is the regularization or just seeing more data. The augmentation-only vs. augmentation+consistency ablation is make-or-break.",
    "Ignoring clean accuracy degradation: Any robustness method that degrades unperturbed accuracy by >2 points will trigger the 'not practical' critique. GSM-Plus found that math SFT improves accuracy but not robustness — reviewers are primed to expect that robustness training might trade off against accuracy. Report clean accuracy prominently, and if there's a small degradation, acknowledge it with analysis of the accuracy-robustness Pareto frontier.",
    "Over-claiming RL discovers novel reasoning: 'Does RL Really Incentivize' (NeurIPS 2025 Best Paper Runner-Up) proved RL is a distribution sharpener, not a capability expander. Any paper that claims its RL-based method 'teaches models to reason' rather than 'makes existing reasoning more reliable' will face skepticism. Frame contributions as improving reliability/consistency of existing capabilities, not creating new ones.",
    "Testing only on perturbation types seen during training: If MACR trains with numerical substitution and variable renaming, and only evaluates on those same perturbation types, reviewers will argue the model simply memorized the perturbation distribution. Transfer to held-out perturbation types (distractor insertion, structural changes) is essential for claiming that consistency regularization induces genuine invariance rather than perturbation-specific memorization.",
    "Using point estimates without distributional analysis: GSM-Symbolic's distributional evaluation methodology (50 instantiations per template, variance reporting) and the Ivanova critique (only 4/25 models show statistically significant drops under Wilson intervals) have raised the bar. Report confidence intervals, variance across perturbation instances, and significance tests — not just mean accuracy.",
    "Neglecting the interaction between consistency loss and RL reward signal: GRPO's clipped objective + KL penalty creates a specific optimization landscape. Adding a consistency term changes the gradient dynamics — if the consistency loss dominates early training, it may prevent the model from learning the basic reward signal. CSR's warm-start curriculum approach (9% overhead via gradual introduction) provides a proven mitigation strategy that should be adopted.",
    "Assuming frontier model results transfer to 7B: VAR-MATH notes DeepSeek-R1 and SEED-THINK show minimal drops, while smaller models show 47-73% drops. If MACR's primary experiments are on 7B, reviewers may question whether the method is addressing a real problem at frontier scale or just patching a capability gap that scale would resolve. Include a brief analysis of whether the robustness gap correlates with model size and whether consistency regularization provides diminishing returns at scale.",
    "Framing the perturbation generator as the contribution rather than the consistency objective: If the paper spends most of its novelty budget on how to generate math-equivalent perturbations (which VAR-MATH's pipeline already largely solves), the contribution looks incremental. The novel contribution must be the RL-integrated consistency regularization framework, with perturbation generation as a necessary component, not the centerpiece."
  ],

  "field_trajectory": "The field is undergoing a phase transition from diagnostic benchmarking to training-time intervention. 2024-2025 produced five major perturbation benchmarks (GSM-Symbolic, GSM-Plus, VAR-MATH, MATH-Perturb, Robust Reasoning Benchmark) that thoroughly documented the fragility problem across all difficulty levels. AbstRaL (ICLR 2026) represents the first training-time response, but its GSM-only scope leaves competition-level math as an open frontier. The next 12-18 months will be dominated by three macro-directions: (1) Training-time robustness interventions that scale to competition math — this is the immediate high-value target, with MACR positioned to be first-to-market. The key question is whether consistency regularization, explicit abstraction (AbstRaL), or adversarial training (APRM-style) wins, or whether they compose. (2) Process-level reward robustness — rStar-Math, APRM, and the test-time compute scaling paper collectively establish that PRM quality is the critical bottleneck for both training and inference. Perturbation-robust PRMs that resist surface-form exploitation during beam search would unlock both better RL training and more efficient test-time compute. (3) Understanding scale-robustness interactions — VAR-MATH's observation that the largest models show minimal drops raises the fundamental question of whether robustness training is a permanent contribution or a temporary patch for capability gaps that scale will resolve. Papers that characterize robustness scaling laws (analogous to ACL 2026's accuracy scaling laws) will inform whether this research direction has a long-term future or a narrow window. A secondary trend is the convergence of faithfulness (CSR) and invariance (MACR) as complementary training objectives — enforcing both 'the model uses its reasoning' and 'the model reasons consistently across equivalent inputs' addresses the complete failure mode taxonomy. The field's center of gravity is shifting from 'can we measure fragility?' (solved) to 'can we fix it during training without sacrificing clean performance?' (open).",

  "meta_advice": "If you're writing a 2026 paper on RL robustness for mathematical reasoning, your first priority is the augmentation-only ablation — this is the single experiment most likely to make or break your paper. PPCL showed consistency regularization outperforms augmentation in NLU, but that result has never been replicated in math reasoning with RL. If pure augmentation (adding perturbed problems to GRPO training without the consistency loss) closes 80% of the gap, your consistency term is a marginal contribution and reviewers will reject. Design your experiments to decisively answer this question first, before investing compute in ablations and analysis. Your second priority is competition-level evaluation. AbstRaL occupied the GSM-level niche at ICLR 2026; repeating that at AAAI is a losing strategy. VAR-MATH's VAR-AIME24/AIME25 and MATH-Perturb's level-5 MATH problems are ready-made evaluation sets that differentiate your work. Your third priority is held-out perturbation transfer. The strongest possible result is: train with numerical substitution and variable renaming, evaluate on distractor insertion and structural changes, and show significant gains on the held-out types. This proves the consistency term induces genuine invariance rather than perturbation-specific memorization — and it's the claim that pure augmentation cannot match. Mechanistically, leverage the 'Does RL Really Incentivize' framing: RL is a distribution sharpener, and your consistency term prevents it from sharpening toward surface-form-dependent solutions. This framing is both accurate and reviewer-friendly because it doesn't over-claim capability expansion. For practical execution within 200 H100-hours: the ACL 2026 scaling paper validates 7B as cost-effective and confirms data reuse tolerance up to 25×; run your primary sweep on Qwen2.5-Math-7B with a single 14B verification. Budget 40 hours for the critical augmentation-vs-consistency ablation, 30 hours for the held-out perturbation transfer experiment, and 20 hours for the competition-level evaluation — these three results determine acceptance. Finally, use CSR's warm-start curriculum approach for the consistency loss to avoid early-training interference with GRPO's reward signal, and report the accuracy-robustness Pareto frontier explicitly to preempt the clean-accuracy-degradation critique."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7fcc2aae-1ca9-4913-9b21-ca3797ee60a7",
  "isSidechain": false,
  "requestId": "req_011CbWUMgph4qwD9ZhD2WtdW",
  "type": "assistant",
  "uuid": "63884d42-c45d-461c-985d-cf0bd4d1d477",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "5426ac1b-6861-47ee-b4fa-9d7f4ce993ea",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0143queA7rs5PN5L8dD6d6TF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13083,
      "cache_read_input_tokens": 11014,
      "output_tokens": 8641,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13083,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 8641,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 13083,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13083
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
  "leafUuid": "63884d42-c45d-461c-985d-cf0bd4d1d477",
  "sessionId": "5426ac1b-6861-47ee-b4fa-9d7f4ce993ea"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesizing RL-based math reasoning robustness strategies for AAAI 2026",
  "sessionId": "5426ac1b-6861-47ee-b4fa-9d7f4ce993ea"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-29 (UTC).**  ## Research area: Target: AAAI 2026 Track: Machine Lea…",
  "leafUuid": "63884d42-c45d-461c-985d-cf0bd4d1d477",
  "sessionId": "5426ac1b-6861-47ee-b4fa-9d7f4ce993ea"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesizing RL-based math reasoning robustness strategies for AAAI 2026",
  "sessionId": "5426ac1b-6861-47ee-b4fa-9d7f4ce993ea"
}
```

---
