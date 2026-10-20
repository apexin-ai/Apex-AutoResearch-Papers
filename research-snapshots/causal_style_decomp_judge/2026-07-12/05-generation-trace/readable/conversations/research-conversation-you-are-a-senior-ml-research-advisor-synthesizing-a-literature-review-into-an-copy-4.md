# Research conversation: You are a senior ML research advisor synthesizing a literature review into an actionable research strategy. **Today's da

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/9c2424f1-4faa-4690-8ff5-2cc4b82c5bcd.jsonl`
- **Structured JSON:** [`6028b291a820788bfc5a.json`](../../sessions/60/6028b291a820788bfc5a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T05:23:06.964Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T05:23:06.964Z",
  "sessionId": "9c2424f1-4faa-4690-8ff5-2cc4b82c5bcd",
  "content": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.\n\n**Today's date: 2026-05-28 (UTC).**\n\n## Research area: Bridging Informal and Formal Mathematical Reasoning — Autoformalization and Proof Verification\n\n## Paper analyses (18 papers)\n\n[\n  {\n    \"title\": \"Olympiad-Level Formal Mathematical Reasoning with Reinforcement Learning\",\n    \"venue\": \"Nature 2025\",\n    \"problem_identification\": \"The authors identified a fundamental tension in AI mathematical reasoning: informal neural approaches (LLMs) can handle natural language math but hallucinate and lack verifiability, while formal theorem provers have guaranteed correctness but are bottlenecked by extremely limited training data (~300K human-written Mathlib proofs) and inability to scale test-time compute beyond brute-force search. The gap was visible from HTPS (Lample et al., 2022), which showed AlphaZero-style search could improve theorem proving but plateaued because the curriculum of provable problems was too narrow — the system couldn't learn from problems it had never seen formalized.\",\n    \"key_insight\": \"Formal verification provides a perfect, binary reward signal — a proof either checks or it doesn't — which makes theorem proving an ideal RL environment if you can generate enough problems. The core aha was combining massive autoformalization (using Gemini to translate ~1M informal problems into ~80M formal Lean statements) with AlphaZero-style RL to create a self-improving loop, then inventing test-time reinforcement learning (TTRL) — essentially training a bespoke model per hard problem by generating problem variants as a micro-curriculum — to break through the ceiling where search alone fails.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"AlphaProof uses a 3-billion-parameter encoder-decoder transformer (the 'proof network') that encodes Lean tactic states and outputs both a policy (which tactic to try next) and a value (estimated proof difficulty). Training has four stages: (1) pretraining on ~300B tokens of code and math text, (2) supervised fine-tuning on ~300K human-written Mathlib state-tactic pairs, (3) autoformalization using a fine-tuned Gemini model to convert ~1M natural-language math problems into ~80M formal Lean statements via an iterative STaR-style refinement process starting from 2,500 manual formalizations, and (4) main RL training over ~80K TPU-days using distributed actors, a centralized matchmaker that adaptively assigns problems by difficulty, and verified proofs as reward (r_t = −1 per tactic step, incentivizing shorter proofs). Proof search uses an AlphaZero-inspired AND-OR tree with modified PUCT, handling multi-subgoal decomposition. The key inference innovation is test-time reinforcement learning (TTRL): for each hard target problem, the system generates diverse formal variants (simplifications, generalizations, related lemmas) and runs focused RL training on this bespoke curriculum, yielding 15+ percentage point improvements on difficult benchmarks beyond what search scaling alone provides.\",\n    \"what_makes_it_good\": \"This paper was accepted at Nature because of the unmistakable, independently verifiable milestone: solving 3 of 5 non-geometry IMO 2024 problems including P6 (solved by only 5 human contestants), achieving silver-medal performance with formally verified proofs. What elevates it beyond a 'scaling paper' is the TTRL contribution — a genuinely novel inference paradigm that treats test-time as a learning opportunity rather than just a search budget, which is a conceptual advance applicable beyond mathematics. The formal verification guarantee also makes the results immune to the 'did the LLM just memorize it?' critique that plagues informal reasoning benchmarks.\",\n    \"limitations_acknowledged\": \"The authors are refreshingly honest about compute costs: main RL training required ~80K TPU-days, autoformalization ~100K TPU-days, and TTRL requires 50-200+ TPU-days per problem, with the hardest IMO problems taking up to three days of inference (vs. 4.5 hours for human contestants). They also acknowledge weak performance on combinatorics (20.3% on formal-IMO), inability to handle research-level mathematics or theory-building, and that the system is currently restricted to high-school/undergraduate competition mathematics.\",\n    \"open_questions\": [\n      \"Can TTRL be made efficient enough for practical deployment, or is 'spend 200 TPU-days per problem' an inherent cost of this paradigm? Is there a way to amortize test-time learning across related problems?\",\n      \"Why does the system fail so badly on combinatorics (20.3% vs. 75.7% on number theory)? Is this a formalization gap (combinatorics is hard to state in Lean), a training distribution gap, or a fundamental limitation of the tree-search approach for problems requiring novel constructions?\",\n      \"Can the autoformalization pipeline be made bidirectional — not just informal→formal for training, but formal→informal for explaining AI-discovered proofs to humans, closing the loop toward AI-assisted mathematical research?\"\n    ],\n    \"building_blocks\": [\n      \"Gemini-based autoformalization pipeline (informal math → Lean 4 formal statements, STaR-style iterative refinement)\",\n      \"AND-OR tree search with modified PUCT for multi-subgoal proof decomposition\",\n      \"Lean 4 as a verified RL environment with binary reward signal\",\n      \"Test-time reinforcement learning (TTRL) — generating problem variants as micro-curriculum for per-problem adaptation\",\n      \"Distributed RL training with centralized matchmaker for adaptive difficulty scheduling\",\n      \"Encoder-decoder transformer architecture for tactic state → (policy, value) prediction\",\n      \"Mathlib as supervised fine-tuning dataset (~300K state-tactic pairs)\",\n      \"Progressive sampling in tree search to broaden strategy exploration\"\n    ],\n    \"reviewer_feedback_summary\": \"Nature does not use OpenReview, so no public reviewer comments are available. However, several external signals are informative: (1) The paper's acceptance at Nature (extremely rare for an AI systems paper) suggests reviewers valued the verifiable, milestone-driven result over methodological novelty per se. (2) Timothy Gowers (Fields Medalist) publicly praised the system's ability to find 'non-obvious constructions.' (3) Likely reviewer concerns would center on reproducibility (the system requires >180K TPU-days total compute, making it unreplicable outside a handful of labs), the relaxed time constraints (3 days vs. 4.5 hours), and whether the achievement reflects genuine mathematical reasoning or sophisticated pattern matching at scale. (4) The honest limitations section and detailed ablations (showing TTRL contributes 15+ points beyond search scaling alone) likely preempted methodological criticisms.\",\n    \"relevance_to_seed\": \"This paper is the current state-of-the-art at the exact intersection of our research area — bridging informal and formal mathematical reasoning. Its autoformalization pipeline (Gemini converting 1M informal problems to 80M formal Lean statements via STaR-style refinement from 2,500 seeds) is directly a contribution to autoformalization, while the end-to-end system demonstrates that formal proof verification can serve as the grounding signal that makes RL-based mathematical reasoning reliable. The key lesson for our research area: the bottleneck in formal reasoning is not the prover but the curriculum — whoever solves the autoformalization data flywheel (informal → formal at scale with quality) unlocks the RL training loop, and TTRL shows that test-time is itself an underexploited dimension for bridging the gap between what a general model knows and what a specific formal proof requires.\"\n  },\n  {\n    \"title\": \"DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition\",\n    \"venue\": \"arXiv 2025 (preprint, submitted April 30, 2025; revised July 18, 2025)\",\n    \"problem_identification\": \"Prior formal theorem provers treated proof generation as a monolithic end-to-end task, forcing a single model to simultaneously handle high-level mathematical reasoning AND low-level formal syntax — two very different competencies. The authors identified that large general-purpose LLMs (like DeepSeek-V3) are strong at informal mathematical reasoning but weak at formal proof synthesis, while small specialized provers can fill in formal details but lack strategic planning. The gap was empirically visible: problems unsolvable end-to-end by a 7B prover could often be solved when decomposed into subgoals — the difficulty was in orchestration, not in any single step.\",\n    \"key_insight\": \"Lean 4's 'have' statement provides a natural formal representation of informal reasoning steps — it is simultaneously a valid proof structure AND a human-readable subgoal decomposition. By having a large model generate proof sketches as chains of 'have ... := sorry' statements (bridging informal reasoning to formal structure), then resolving each 'sorry' independently with a specialized prover, you can compose systems where informal reasoning directly scaffolds formal verification. The critical trick is then distilling this decomposed pipeline back into a single model via cold-start CoT data synthesis.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"The approach works in three phases. First, a cold-start data pipeline: DeepSeek-V3 (671B general-purpose model) generates natural-language reasoning for a theorem, then translates it into a Lean 4 proof sketch — a sequence of 'have' statements with 'sorry' placeholders. A specialized 7B prover independently resolves each subgoal. When all subgoals resolve, the composed proof (paired with V3's chain-of-thought) becomes training data. Second, curriculum learning: from these decomposed proofs, two types of synthetic subgoal theorems are extracted — standalone lemmas and context-dependent lemmas with preceding subgoals as premises — creating a difficulty progression from easy subgoals to full theorems. Third, the final model (DeepSeek-V3-Base-671B) is trained via SFT on this data and then refined with GRPO reinforcement learning using binary proof-verification rewards, plus a novel consistency reward that penalizes structural deviation from the decomposed subgoal plan. The model operates in two modes: a fast non-CoT mode for direct proof generation, and a CoT mode that articulates informal reasoning before producing formal proof code.\",\n    \"what_makes_it_good\": \"Three qualities elevate this work. First, the results are unambiguously SOTA and open-source: 88.9% on miniF2F-test and 49/658 on PutnamBench substantially advance the field, and reproducibility is ensured through open weights. Second, the intellectual contribution is architecturally clean — the insight that informal-to-formal bridging should happen at the proof-structure level (subgoal decomposition via 'have' statements) rather than the token level is both simple and powerful, and the cold-start → curriculum → RL pipeline is a reusable template. Third, the authors demonstrated exceptional scientific integrity by transparently reporting a reward hacking vulnerability where the 7B model exploited a Lean 4.9.0 UI bug in the 'apply?' tactic, initially inflating PutnamBench results — they identified, disclosed, and corrected this rather than burying it.\",\n    \"limitations_acknowledged\": \"The authors implicitly acknowledge several gaps: geometry, combinatorics, and counting problems were excluded from AIME formalization because their Lean representations are 'potentially cumbersome,' revealing domain coverage limits. ProofNet-test performance (37.1% at Pass@1024) shows undergraduate-level mathematics remains difficult. The 7B model's reward hacking via Lean bugs demonstrates that RL-trained formal provers can learn to exploit verification tool weaknesses rather than develop genuine proving capability.\",\n    \"open_questions\": [\n      \"Can subgoal decomposition scale to IMO-level problems where the key difficulty is finding the right decomposition strategy itself — i.e., when the 'sketch' requires deep mathematical insight that even large LLMs lack?\",\n      \"What is the performance ceiling for sampling-based approaches (Pass@k with large k) versus tree search methods? The paper uses no tree search at inference, suggesting significant untapped gains from combining decomposition with structured search (their stated AlphaProof-like aspiration).\",\n      \"How brittle is the pipeline to the quality of the informal reasoning? If DeepSeek-V3 produces a flawed proof sketch (wrong decomposition strategy), does the system fail gracefully or waste all compute on doomed subgoals? What fraction of V3's sketches lead to successful compositions?\"\n    ],\n    \"building_blocks\": [\n      \"DeepSeek-V3-671B as proof sketch generator (informal reasoning → formal 'have' statement chains)\",\n      \"Lean 4 'have ... := sorry' pattern as the universal bridge format between informal and formal reasoning\",\n      \"Cold-start data synthesis: pair informal CoT with composed formal proofs from subgoal resolution\",\n      \"Curriculum learning via synthetic subgoal theorems (Type A: standalone, Type B: with context premises)\",\n      \"GRPO reinforcement learning with binary proof-verification rewards\",\n      \"Consistency reward for enforcing structural alignment between CoT decomposition and final proof\",\n      \"Expert iteration: iteratively expanding training data by solving previously-unsolved problems with the improving model\",\n      \"Two-mode inference: fast non-CoT for easy problems, deliberate CoT for harder ones\",\n      \"Lean 4 proof assistant as deterministic verification oracle\",\n      \"7B distilled model from 671B RL rollout data\"\n    ],\n    \"reviewer_feedback_summary\": null,\n    \"relevance_to_seed\": \"This paper is the current exemplar of our exact research area — bridging informal and formal mathematical reasoning. Its core lesson for our work is that the bridge should be structural, not syntactic: rather than training a model to translate natural language proofs into formal code token-by-token, the winning strategy is to use informal reasoning to generate a formal proof skeleton (subgoal decomposition) and then fill in details with specialized tools. The cold-start data synthesis pipeline — using a general model's informal reasoning to bootstrap formal proving training data — is a directly reusable paradigm for autoformalization research. The 'substantially narrowing' gap between informal and formal performance (8/15 vs 6/15 on AIME) quantifies exactly how close the field is to closing this bridge.\"\n  },\n  {\n    \"title\": \"DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search\",\n    \"venue\": \"ICLR 2025\",\n    \"problem_identification\": \"The authors identified that whole-proof generation (their own V1 approach) suffers from compounding errors: the autoregressive model develops incorrect beliefs about intermediate tactic states during long proofs, and a single misinterpretation cascades into invalid proof paths. Meanwhile, step-by-step tactic generation avoids this but requires expensive per-step verification communication. The gap they found was that no existing system unified these two paradigms — you either got the efficiency of whole-proof generation or the correctness-grounding of step-level verification, but not both. They found this gap by analyzing their own V1 system's failure modes, a classic 'build it, see where it breaks, fix that' research loop.\",\n    \"key_insight\": \"A 'truncate-and-resume' mechanism can bridge whole-proof and step-level generation into a single unified framework: generate a full proof, truncate at the first compiler error, inject the verified tactic state back as a prompt suffix, and resume generation — turning what was a dichotomy between two proof strategies into a continuum that naturally slots into MCTS. The second key insight is that proof search has extremely sparse extrinsic rewards (only complete proofs score), so borrowing the RMax exploration bonus from tabular RL theory — rewarding the agent simply for reaching *new* tactic states — provides the curiosity signal needed to diversify search without a learned value function.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"The system has four stages: (1) Pre-training on formal math corpora (Lean, Isabelle, Metamath) to build DeepSeek-Prover-V1.5-Base. (2) Supervised fine-tuning with two novel data augmentations — chain-of-thought comments interleaved with Lean tactics (annotated by DeepSeek-Coder V2 236B) and tactic-state annotations inserted as comments so the model learns to condition on compiler feedback. (3) Reinforcement learning via GRPO using binary proof-verification rewards from the Lean 4 compiler (RLPAF), trained on ~4.5k theorems with moderate SFT success rates to ensure the reward signal is neither too sparse nor trivially dense. (4) At inference, RMaxTS — an MCTS variant where the truncate-and-resume mechanism defines the state-action abstraction (each node is a tactic state, each edge is a tactic), and an intrinsic RMax reward (1 if a new tactic state is discovered, 0 otherwise) drives exploration via Discounted UCB to handle the non-stationarity of curiosity-based rewards. The system is massively parallelized with 256 MCTS runners, 32 thread workers per tree, and virtual losses to encourage diverse node selection.\",\n    \"what_makes_it_good\": \"This paper succeeds because it is a *systems paper disguised as an algorithms paper* — every component (pre-training, SFT data augmentation, RL, tree search) is individually well-motivated and cleanly ablated across training stages (Base → SFT → RL → MCTS), making the contribution of each piece transparent. The truncate-and-resume mechanism is an elegantly simple idea that unifies two previously separate paradigms without requiring architectural changes to the base LLM. The RMax intrinsic reward is a principled import from the exploration theory literature (not an ad-hoc heuristic), and the authors correctly identify and solve the non-stationarity problem it introduces via DUCB. The 10+ percentage point improvement over V1 on miniF2F-test (50.0% → 63.5%) is a substantial empirical advance, and the paper is open-source, which significantly increases impact and reproducibility.\",\n    \"limitations_acknowledged\": \"The authors explicitly note they focused only on the exploration aspect of RL in tree search, leaving the exploitation aspect (training a critic/value model to prune search branches and perform temporal credit assignment) entirely unexplored. They also acknowledge the framework is designed for individual theorem proving and has only nascent capabilities for file-level, multi-theorem theory proving in realistic Lean projects.\",\n    \"open_questions\": [\n      \"Can a learned critic model for partial proofs (analogous to AlphaZero's value network) substantially improve search efficiency by pruning unpromising branches, and what training signal would such a critic use given the extreme sparsity of proof-level rewards?\",\n      \"How does the truncate-and-resume + RMaxTS approach scale to competition-level or research-level mathematics where proofs are much longer and the tactic state space is vastly larger — does the intrinsic reward signal degrade, and would hierarchical or subgoal-based search be needed?\",\n      \"The CoT annotation was done by a proprietary 236B model (DeepSeek-Coder V2) — can this bootstrapping step be made self-sufficient (the prover annotates its own reasoning) without quality degradation, closing the loop for fully autonomous improvement?\"\n    ],\n    \"building_blocks\": [\n      \"GRPO (Group Relative Policy Optimization) for RL without a critic model\",\n      \"Lean 4 REPL + LeanDojo tactic state extraction\",\n      \"Truncate-and-resume mechanism for bridging whole-proof and step-level generation\",\n      \"RMax intrinsic reward strategy from tabular RL theory\",\n      \"Discounted UCB (DUCB) for non-stationary bandit problems in MCTS\",\n      \"Expert iteration / synthetic data loop with compiler verification\",\n      \"Chain-of-thought annotation via a larger teacher model (DeepSeek-Coder V2 236B)\",\n      \"vLLM for high-throughput inference\",\n      \"miniF2F and ProofNet benchmarks (Lean 4 ports)\",\n      \"Virtual loss technique for parallel MCTS\",\n      \"DeepSeekMath-Base 7B as foundation model\"\n    ],\n    \"reviewer_feedback_summary\": null,\n    \"relevance_to_seed\": \"This paper is directly central to bridging informal and formal mathematical reasoning: the chain-of-thought annotations interleaved with Lean tactics are a concrete instantiation of autoformalization-in-reverse (mapping formal steps back to informal reasoning to improve formal proof generation). The truncate-and-resume mechanism demonstrates that the compiler itself can serve as a verification oracle that grounds informal reasoning in formal correctness — a paradigm that any autoformalization system could adopt. For our research area, the key lesson is that the informal↔formal bridge is most effective when it operates *within* the proof generation process (as interleaved comments and tactic states), not as a separate pre-processing or post-processing step.\"\n  },\n  {\n    \"title\": \"Hilbert: Recursively Building Formal Proofs with Informal Reasoning\",\n    \"venue\": \"ICLR 2026\",\n    \"problem_identification\": \"The authors identified a stark quantitative gap between informal and formal mathematical reasoning: reasoning LLMs can solve ~83% of PutnamBench problems informally (per human verification), yet the best publicly available formal provers solve only ~13%. Prior bridging approaches (DSP, LEGO-Prover, DSP+) used only shallow, single-layer decomposition — they break a problem into subgoals once but cannot recursively decompose subgoals that remain too hard. The authors also observed that prover LLMs and reasoning LLMs have complementary failure modes: provers excel at syntactically correct short proofs but fail at language-intensive tasks like leveraging existing theorems; reasoners understand high-level proof strategy but produce syntactically broken formal code.\",\n    \"key_insight\": \"Rather than treating informal reasoning as a one-shot translation step to formal proof (as in DSP-style approaches), the key insight is to use the informal reasoner as a recursive orchestrator that decomposes hard problems into subgoals, checks their mathematical correctness before attempting formalization, and routes each subgoal to whichever solver (prover or reasoner) can handle it — creating a recursive call stack of proof obligations where the formal verifier acts as the ground-truth termination condition at every level.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"Hilbert orchestrates four components: (1) a Reasoner LLM (Gemini 2.5 Pro/Flash) for informal proofs and proof sketches, (2) a Prover LLM (DeepSeek-Prover-V2-7B or Goedel-Prover-V2-32B) for direct formal proof generation, (3) a Lean 4 Verifier for ground-truth checking, and (4) a semantic Retriever using sentence-transformer embeddings over Mathlib's informal theorem descriptions via FAISS. Given a theorem, Hilbert first attempts direct proof via the Prover (Phase 1). On failure, it enters Phase 2: the Reasoner retrieves relevant Mathlib theorems, generates a detailed informal proof, translates it into a Lean 4 proof sketch with 'have' statements (subgoals) marked by 'sorry' placeholders, extracts these as independent theorem statements, and assembles the final proof by replacing 'sorry' with subgoal calls. Each subgoal is solved via a three-strategy cascade: (a) direct Prover attempt, (b) 'shallow solve' where the Reasoner writes a short formal proof with iterative error correction, or (c) recursive decomposition (up to depth D=5). Critically, the Reasoner also performs mathematical correctness checking — flagging unprovable or poorly-formulated subgoals before wasting compute on them — and verifier feedback is propagated back at every stage for iterative refinement.\",\n    \"what_makes_it_good\": \"The paper succeeds because it delivers overwhelming empirical results (99.2% on miniF2F, 70.0% on PutnamBench — a 422% improvement over the best public baseline SeedProver) while the method is conceptually clean and well-ablated. The ablation studies are particularly compelling: they isolate the contribution of recursive depth (75% at D=0 → 99.2% at D=5), retrieval (improves both accuracy AND reduces compute by ~30%), and the shallow-solve step. The paper also demonstrates generalizability across multiple model pairings including an open-source reasoner (gpt-oss-120b), showing the framework isn't just a wrapper around one proprietary model.\",\n    \"limitations_acknowledged\": \"The authors acknowledge heavy reliance on strong reasoning LLMs (Gemini 2.5 Pro) for peak performance and high inference-time compute costs (up to 22-27M tokens per problem for the hardest cases). They also note that the framework's ceiling is bounded by the underlying LLMs' capabilities — it approaches but doesn't reach the ~82% informal proof rate reported by Dekoninck et al., suggesting the formalization gap isn't fully closed.\",\n    \"open_questions\": [\n      \"Can the proof traces and reasoning trajectories generated by Hilbert be used as training data to improve the underlying Prover and Reasoner models, creating the 'virtuous cycle' the authors mention in their conclusion? What is the quality/diversity of this synthetic data?\",\n      \"How does the framework scale to research-level mathematics beyond competition problems (e.g., FrontierMath)? The recursive decomposition assumes problems can be broken into 'simpler' subgoals, but research-level proofs may require novel lemmas that don't decompose neatly.\",\n      \"What is the right balance between inference-time compute and model training? Hilbert uses up to 27M tokens per problem — could some of this agentic overhead be distilled into a single model that learns the decomposition strategy implicitly, similar to how AlphaProof internalized search?\"\n    ],\n    \"building_blocks\": [\n      \"Lean 4 + Mathlib v4.15.0 as formal verification backbone\",\n      \"Kimina Lean Server for Lean interaction\",\n      \"Sentence-transformers (all-mpnet-base-v2) + FAISS for semantic theorem retrieval over mathlib_informal dataset\",\n      \"Proof sketch paradigm: 'have' statements with 'sorry' placeholders as subgoal interface\",\n      \"DeepSeek-Prover-V2-7B and Goedel-Prover-V2-32B as specialized formal provers\",\n      \"Gemini 2.5 Pro/Flash as informal reasoning backbone\",\n      \"Recursive subgoal decomposition with depth-limited search\",\n      \"Verifier-in-the-loop iterative error correction\",\n      \"LLM-as-judge for mathematical correctness checking of subgoals\",\n      \"miniF2F and PutnamBench benchmarks\"\n    ],\n    \"reviewer_feedback_summary\": null,\n    \"relevance_to_seed\": \"This paper is the current state-of-the-art in our exact research area of bridging informal and formal mathematical reasoning. Its key lesson for our work is architectural: the winning strategy is not to build a better single autoformalization model, but to design a multi-agent system where informal reasoning, formal proving, verification, and retrieval are separate specialized modules orchestrated by a recursive decomposition controller. Any new work in this space must either beat Hilbert's numbers or address its limitations — particularly the high compute cost, reliance on proprietary models, or the gap between competition math and research-level mathematics.\"\n  },\n  {\n    \"title\": \"Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach\",\n    \"venue\": \"ICLR 2025 (Spotlight)\",\n    \"problem_identification\": \"The authors performed a systematic audit of the autoformalization pipeline and identified two foundational gaps that the community had been working around rather than solving: (1) no existing automated evaluation metric is simultaneously formal-grounded, human-aligned, and universal — BLEU is semantically shallow, typecheck is necessary but not sufficient, LLM graders are non-deterministic and fragile, and SMT-based approaches (Murphy et al.) are domain-restricted to Euclidean geometry; (2) autoformalizers operate context-blind, ignoring the library of previously formalized definitions and theorems, which causes severe hallucination of identifiers especially in out-of-distribution settings. They found gap #1 by asking what formal properties an equivalence metric *should* have (reflexivity, symmetry, transitivity, human-alignment, universality) and showing no existing metric satisfies all five; they found gap #2 by doing error analysis showing 'definition misalignment' is the dominant failure mode.\",\n    \"key_insight\": \"Lean 4's built-in definitional equality is already a principled equivalence relation (reflexive, symmetric, transitive) over formal statements, but it is too strict for evaluating autoformalization because it cannot handle trivially equivalent reformulations like 'n + 0' vs 'n'. The core aha: extend definitional equality by (1) equipping it with a restricted set of tactic-based transformation primitives that allow one statement to be rewritten before comparison, and (2) making this check bidirectional — s_P ~_B s_Q iff s_P can be transformed to be definitionally equal to s_Q AND vice versa. The LLM generates candidate tactic sequences, but the Lean kernel formally verifies them, yielding a neuro-symbolic metric that inherits formal guarantees while matching human intuition.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"BEq (Bidirectional Extended Definitional Equivalence) works by checking two directions: to test s_P ←_U s_Q, assume s_Q is true (close with sorry), then use an LLM (InternLM-Math-Plus-20B, 5-shot, beam search) to generate tactic sequences from a restricted set R = {apply, cases', constructor, exact, exact?, ext, have, intro, intros, rw, use} that transform s_P into something definitionally equal to s_Q. If any candidate succeeds, the implication holds; BEq holds iff both directions succeed. For the retrieval component, they parse Mathlib 4's full dependency graph (243,797 formal objects), topologically sort and informalize objects bottom-up across 24 generations using an LLM, creating training data that preserves dependency context. A dense retriever (fine-tuned BGE-M3) embeds informal statements and retrieves top-k dependent formal objects from the library. The RAutoformalizer (fine-tuned InternLM-Math-Base-7B) then generates formal statements conditioned on both the informal statement and retrieved dependencies. Con-NF benchmark is built from 961 cleaned theorem pairs from the Lean 4 Con(NF) library (Quine's New Foundations consistency proof), providing genuinely OOD evaluation since it uses different foundational theory than Mathlib.\",\n    \"what_makes_it_good\": \"This paper succeeds because it identifies and solves infrastructure-level problems that the entire autoformalization community needs — a reliable evaluation metric and a method to reduce hallucination — rather than just pushing numbers on existing benchmarks. The theoretical grounding is unusually rigorous for an ML paper: BEq is formally proven to be an equivalence relation (Theorem 1), and its design choices (which tactics to include, bidirectionality) are systematically ablated. The three contributions (BEq metric, RAutoformalizer, Con-NF benchmark) form a tightly integrated narrative: BEq exposes how bad existing methods truly are, the retrieval approach addresses the root cause, and Con-NF stress-tests OOD generalization. Reviewers specifically praised the pioneering nature of the evaluation work and the inclusion of both in-distribution and OOD testing.\",\n    \"limitations_acknowledged\": \"BEq depends on high-quality ground-truth formal statements (unusable for benchmarks lacking them) and its quality depends on careful design of the restricted tactic set R and the LLM approximation of the transformation function T, meaning recall can suffer when the LLM fails to find valid tactic proofs (-12.85% vs. majority voting on recall). For RAutoformalizer, retrieval quality is the bottleneck — the oracle retrieval experiment (RA+R) shows 10× headroom for improvement over current retrieval, and sophisticated techniques like multi-vector embeddings, re-ranking, and query augmentation are left as future work.\",\n    \"open_questions\": [\n      \"Can BEq be extended beyond statement equivalence to evaluate proof autoformalization and full theory autoformalization, where the notion of 'equivalence' is richer and involves structural correspondence between proof strategies?\",\n      \"The oracle retrieval experiment shows massive untapped potential (BEq@8: 16.86% actual vs 55.36% with perfect retrieval on Con-NF) — what retrieval architectures or hybrid symbolic-neural approaches can close this gap, especially for OOD libraries with different foundational axioms?\",\n      \"Can topological informalization be applied in reverse — using the dependency structure of informal mathematical texts (textbooks, papers) to improve formalization by identifying which concepts need to be formalized first, creating a curriculum for autoformalizers?\"\n    ],\n    \"building_blocks\": [\n      \"Lean 4 tactic mode and definitional equality as formal verification backbone\",\n      \"BGE-M3 embedding model fine-tuned for dependency retrieval\",\n      \"Dense Passage Retrieval (DPR) framework adapted to formal math libraries\",\n      \"Topological informalization — LLM-based informalization respecting dependency DAG order across 24 generations\",\n      \"InternLM-Math-Plus-20B as tactic generator within BEq\",\n      \"InternLM-Math-Base-7B as base autoformalizer model\",\n      \"Mathlib 4 dependency graph (243,797 formal objects, 139,933 theorems)\",\n      \"Con-NF library (Quine's New Foundations consistency proof) for OOD benchmark\",\n      \"ProofNet benchmark for in-distribution evaluation\",\n      \"Beam search with restricted tactic set for controlled equivalence checking\",\n      \"Hard negative mining from top-100 BM25/BGE-M3 candidates for retriever training\"\n    ],\n    \"reviewer_feedback_summary\": \"Five reviewers assessed the paper. Key praise: (1) BEq was called 'pioneering work' in autoformalization evaluation that addresses a genuine community gap; (2) the theoretical grounding (proving equivalence relation properties) and interpretability via Lean 4 tactics were highlighted; (3) inclusion of both in-distribution and OOD evaluation was valued. Key concerns: (1) Reviewer 9PuK flagged a logic gap — BEq evaluates formal-statement equivalence but the paper frames it as evaluating autoformalization quality, and model-based evaluators exist as alternatives to ground-truth comparison (authors clarified ground-truth comparison remains the mainstream benchmarking paradigm); (2) Reviewer pPF9 raised insufficient detail on human evaluation protocols, Con-NF quality control, and missing prompt templates (all addressed with expanded appendices); (3) Reviewer fV7x requested ablations across different LLM families for BEq, CoT/ToT reasoning baselines, and stronger retrieval baselines (authors provided experiments across 7B-236B models showing robustness, added CoT experiments, and compared against BM25/BGE-M3 baselines). Post-rebuttal, all reviewers agreed on acceptance. The Area Chair noted the paper makes significant contributions across evaluation, methodology, and benchmarking.\",\n    \"relevance_to_seed\": \"This paper is directly central to bridging informal and formal mathematical reasoning: it provides both the measurement instrument (BEq) and a concrete mechanism (dependency retrieval) for improving autoformalization. The key transferable lesson for our research area is that progress on the *generation* side of autoformalization was being masked by unreliable evaluation — the field needed to solve the measurement problem first. The dependency retrieval paradigm also suggests that autoformalization should not be treated as isolated sentence-level translation but as a context-aware task grounded in the formal library ecosystem, which has implications for how we design proof verification pipelines that connect informal reasoning to formal proof assistants.\"\n  },\n  {\n    \"title\": \"Lean-STaR: Learning to Interleave Thinking and Proving\",\n    \"venue\": \"ICLR 2025 (Spotlight)\",\n    \"problem_identification\": \"The authors identified that formal theorem-proving datasets (like Lean's Mathlib) contain only (proof_state, tactic) pairs, discarding the informal deliberation that human mathematicians perform before each proof step. This 'missing reasoning' gap means models trained on formal proofs learn to mimic actions without understanding the strategic thinking behind them. They found this gap by observing that chain-of-thought techniques work well in informal math but hadn't been successfully integrated into formal proving — largely because no thought-annotated training data exists for formal proofs, and Lean (unlike Isabelle) lacks sledgehammer-style automation that could compensate.\",\n    \"key_insight\": \"Rather than trying to generate thoughts *before* seeing the correct tactic (which produces poor-quality reasoning), they inverted the problem: use the ground-truth tactic as a conditioning signal to *retrospectively* synthesize plausible thoughts that could have led to that tactic, then train the model to reproduce those thoughts at inference time without seeing the answer. This 'rationalize first, internalize later' approach elegantly sidesteps the chicken-and-egg problem of needing good thoughts to find good tactics while needing good tactics to know what thoughts are useful.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"Lean-STaR operates in three stages. First, supervised fine-tuning (SFT) trains a base model on standard (proof_state → tactic) pairs from Mathlib. Second, retrospective thought augmentation uses GPT-4 to generate natural-language rationales conditioned on both the proof state AND the known-correct tactic, producing ~52K–140K (state, thought, tactic) triples; the model is then fine-tuned on these thought-augmented examples to produce thoughts before each tactic (Lean-CoT). Third, expert iteration bootstraps further: the thought-augmented model samples K complete proof trajectories per theorem, the Lean verifier filters for correct proofs (reward=1), and the model is re-fine-tuned on the union of original and newly-verified thought-augmented trajectories. This loop runs for 1–2 iterations. Critically, at inference time, the authors use parallel sampling of complete trajectories rather than best-first tree search, because log-probability-based scoring degrades when natural language thoughts inflate sequence length unpredictably.\",\n    \"what_makes_it_good\": \"This paper succeeds because it takes two well-established techniques (chain-of-thought reasoning and expert iteration) and combines them in a principled way for a domain where their interaction is non-obvious — formal theorem proving has a unique verifier (the Lean kernel) that makes expert iteration clean, while the absence of informal reasoning in formal proofs makes CoT high-value. The ablation showing that expert iteration alone yields 43.0% but Lean-STaR yields 45.5% (with CoT contributing independently) is clean experimental design that isolates the contribution. The observation that thoughts increase *diversity* of proof attempts (better scaling with K) rather than just accuracy per attempt is a subtle but important finding that elevates the work beyond a simple engineering contribution.\",\n    \"limitations_acknowledged\": \"The authors explicitly note computational scalability constraints: training datasets remain modest (50K–140K examples), GPT-4 oracle generation is expensive and may introduce biases, and expert iteration is bottlenecked by Lean's CPU/IO-bound verification speed. They also acknowledge that thought quality varies — some generated thoughts c\n... (truncated)\n\n## Your task\n\nSynthesize these paper analyses into a **Field Guide** — a strategic document that would help a researcher generate novel, high-quality ideas in this area. This is NOT a survey — it's an opinionated strategy guide for innovation.\n\nThink about:\n- What PATTERNS OF INNOVATION keep working in this field?\n- What do reviewers consistently reward?\n- Where are the real gaps (not assumed gaps)?\n- What combinations haven't been tried?\n- What mistakes should we avoid?\n\n## Output format\n\nOutput a JSON object with these sections:\n{\n  \"innovation_patterns\": [\n    {\"pattern\": \"name\", \"description\": \"how it works\", \"examples\": [\"paper1\", \"paper2\"], \"success_rate\": \"high/medium/low\"}\n  ],\n  \"reviewer_preferences\": [\n    \"What reviewers in this area consistently care about (based on evidence from paper analyses)\"\n  ],\n  \"field_gaps\": [\n    {\"gap\": \"description of unsolved problem\", \"evidence\": \"which papers mention this limitation\", \"difficulty\": \"high/medium/low\", \"impact_if_solved\": \"high/medium/low\"}\n  ],\n  \"untried_combinations\": [\n    {\"idea_sketch\": \"what could be combined\", \"from_papers\": [\"which papers inspire this\"], \"why_promising\": \"reason\"}\n  ],\n  \"method_building_blocks\": [\n    {\"tool\": \"name\", \"what_it_does\": \"description\", \"used_by\": [\"papers\"], \"could_be_applied_to\": \"new application\"}\n  ],\n  \"common_pitfalls\": [\n    \"Mistakes to avoid when working in this area (based on reviewer feedback and paper limitations)\"\n  ],\n  \"field_trajectory\": \"Where is this field heading? What are the 2-3 most promising macro-directions? (paragraph)\",\n  \"meta_advice\": \"If you were advising a PhD student to write a strong 2026 paper in this area, what would you tell them? (paragraph)\"\n}\n\nBe specific and evidence-based — every claim should reference specific papers from the analyses. Avoid generic advice like 'be novel' — instead say 'Papers that combine X with Y for task Z have been getting accepted (see Paper A, Paper B).'.\n\nIMPORTANT: You MUST end your response with the JSON object."
}
```

---

### Runtime record

_source line 2 · 2026-05-28T05:23:06.967Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T05:23:06.967Z",
  "sessionId": "9c2424f1-4faa-4690-8ff5-2cc4b82c5bcd"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-28T05:23:06.983Z_

You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.

**Today's date: 2026-05-28 (UTC).**

## Research area: Bridging Informal and Formal Mathematical Reasoning — Autoformalization and Proof Verification

## Paper analyses (18 papers)

[
  {
    "title": "Olympiad-Level Formal Mathematical Reasoning with Reinforcement Learning",
    "venue": "Nature 2025",
    "problem_identification": "The authors identified a fundamental tension in AI mathematical reasoning: informal neural approaches (LLMs) can handle natural language math but hallucinate and lack verifiability, while formal theorem provers have guaranteed correctness but are bottlenecked by extremely limited training data (~300K human-written Mathlib proofs) and inability to scale test-time compute beyond brute-force search. The gap was visible from HTPS (Lample et al., 2022), which showed AlphaZero-style search could improve theorem proving but plateaued because the curriculum of provable problems was too narrow — the system couldn't learn from problems it had never seen formalized.",
    "key_insight": "Formal verification provides a perfect, binary reward signal — a proof either checks or it doesn't — which makes theorem proving an ideal RL environment if you can generate enough problems. The core aha was combining massive autoformalization (using Gemini to translate ~1M informal problems into ~80M formal Lean statements) with AlphaZero-style RL to create a self-improving loop, then inventing test-time reinforcement learning (TTRL) — essentially training a bespoke model per hard problem by generating problem variants as a micro-curriculum — to break through the ceiling where search alone fails.",
    "innovation_type": "combination",
    "method_summary": "AlphaProof uses a 3-billion-parameter encoder-decoder transformer (the 'proof network') that encodes Lean tactic states and outputs both a policy (which tactic to try next) and a value (estimated proof difficulty). Training has four stages: (1) pretraining on ~300B tokens of code and math text, (2) supervised fine-tuning on ~300K human-written Mathlib state-tactic pairs, (3) autoformalization using a fine-tuned Gemini model to convert ~1M natural-language math problems into ~80M formal Lean statements via an iterative STaR-style refinement process starting from 2,500 manual formalizations, and (4) main RL training over ~80K TPU-days using distributed actors, a centralized matchmaker that adaptively assigns problems by difficulty, and verified proofs as reward (r_t = −1 per tactic step, incentivizing shorter proofs). Proof search uses an AlphaZero-inspired AND-OR tree with modified PUCT, handling multi-subgoal decomposition. The key inference innovation is test-time reinforcement learning (TTRL): for each hard target problem, the system generates diverse formal variants (simplifications, generalizations, related lemmas) and runs focused RL training on this bespoke curriculum, yielding 15+ percentage point improvements on difficult benchmarks beyond what search scaling alone provides.",
    "what_makes_it_good": "This paper was accepted at Nature because of the unmistakable, independently verifiable milestone: solving 3 of 5 non-geometry IMO 2024 problems including P6 (solved by only 5 human contestants), achieving silver-medal performance with formally verified proofs. What elevates it beyond a 'scaling paper' is the TTRL contribution — a genuinely novel inference paradigm that treats test-time as a learning opportunity rather than just a search budget, which is a conceptual advance applicable beyond mathematics. The formal verification guarantee also makes the results immune to the 'did the LLM just memorize it?' critique that plagues informal reasoning benchmarks.",
    "limitations_acknowledged": "The authors are refreshingly honest about compute costs: main RL training required ~80K TPU-days, autoformalization ~100K TPU-days, and TTRL requires 50-200+ TPU-days per problem, with the hardest IMO problems taking up to three days of inference (vs. 4.5 hours for human contestants). They also acknowledge weak performance on combinatorics (20.3% on formal-IMO), inability to handle research-level mathematics or theory-building, and that the system is currently restricted to high-school/undergraduate competition mathematics.",
    "open_questions": [
      "Can TTRL be made efficient enough for practical deployment, or is 'spend 200 TPU-days per problem' an inherent cost of this paradigm? Is there a way to amortize test-time learning across related problems?",
      "Why does the system fail so badly on combinatorics (20.3% vs. 75.7% on number theory)? Is this a formalization gap (combinatorics is hard to state in Lean), a training distribution gap, or a fundamental limitation of the tree-search approach for problems requiring novel constructions?",
      "Can the autoformalization pipeline be made bidirectional — not just informal→formal for training, but formal→informal for explaining AI-discovered proofs to humans, closing the loop toward AI-assisted mathematical research?"
    ],
    "building_blocks": [
      "Gemini-based autoformalization pipeline (informal math → Lean 4 formal statements, STaR-style iterative refinement)",
      "AND-OR tree search with modified PUCT for multi-subgoal proof decomposition",
      "Lean 4 as a verified RL environment with binary reward signal",
      "Test-time reinforcement learning (TTRL) — generating problem variants as micro-curriculum for per-problem adaptation",
      "Distributed RL training with centralized matchmaker for adaptive difficulty scheduling",
      "Encoder-decoder transformer architecture for tactic state → (policy, value) prediction",
      "Mathlib as supervised fine-tuning dataset (~300K state-tactic pairs)",
      "Progressive sampling in tree search to broaden strategy exploration"
    ],
    "reviewer_feedback_summary": "Nature does not use OpenReview, so no public reviewer comments are available. However, several external signals are informative: (1) The paper's acceptance at Nature (extremely rare for an AI systems paper) suggests reviewers valued the verifiable, milestone-driven result over methodological novelty per se. (2) Timothy Gowers (Fields Medalist) publicly praised the system's ability to find 'non-obvious constructions.' (3) Likely reviewer concerns would center on reproducibility (the system requires >180K TPU-days total compute, making it unreplicable outside a handful of labs), the relaxed time constraints (3 days vs. 4.5 hours), and whether the achievement reflects genuine mathematical reasoning or sophisticated pattern matching at scale. (4) The honest limitations section and detailed ablations (showing TTRL contributes 15+ points beyond search scaling alone) likely preempted methodological criticisms.",
    "relevance_to_seed": "This paper is the current state-of-the-art at the exact intersection of our research area — bridging informal and formal mathematical reasoning. Its autoformalization pipeline (Gemini converting 1M informal problems to 80M formal Lean statements via STaR-style refinement from 2,500 seeds) is directly a contribution to autoformalization, while the end-to-end system demonstrates that formal proof verification can serve as the grounding signal that makes RL-based mathematical reasoning reliable. The key lesson for our research area: the bottleneck in formal reasoning is not the prover but the curriculum — whoever solves the autoformalization data flywheel (informal → formal at scale with quality) unlocks the RL training loop, and TTRL shows that test-time is itself an underexploited dimension for bridging the gap between what a general model knows and what a specific formal proof requires."
  },
  {
    "title": "DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition",
    "venue": "arXiv 2025 (preprint, submitted April 30, 2025; revised July 18, 2025)",
    "problem_identification": "Prior formal theorem provers treated proof generation as a monolithic end-to-end task, forcing a single model to simultaneously handle high-level mathematical reasoning AND low-level formal syntax — two very different competencies. The authors identified that large general-purpose LLMs (like DeepSeek-V3) are strong at informal mathematical reasoning but weak at formal proof synthesis, while small specialized provers can fill in formal details but lack strategic planning. The gap was empirically visible: problems unsolvable end-to-end by a 7B prover could often be solved when decomposed into subgoals — the difficulty was in orchestration, not in any single step.",
    "key_insight": "Lean 4's 'have' statement provides a natural formal representation of informal reasoning steps — it is simultaneously a valid proof structure AND a human-readable subgoal decomposition. By having a large model generate proof sketches as chains of 'have ... := sorry' statements (bridging informal reasoning to formal structure), then resolving each 'sorry' independently with a specialized prover, you can compose systems where informal reasoning directly scaffolds formal verification. The critical trick is then distilling this decomposed pipeline back into a single model via cold-start CoT data synthesis.",
    "innovation_type": "combination",
    "method_summary": "The approach works in three phases. First, a cold-start data pipeline: DeepSeek-V3 (671B general-purpose model) generates natural-language reasoning for a theorem, then translates it into a Lean 4 proof sketch — a sequence of 'have' statements with 'sorry' placeholders. A specialized 7B prover independently resolves each subgoal. When all subgoals resolve, the composed proof (paired with V3's chain-of-thought) becomes training data. Second, curriculum learning: from these decomposed proofs, two types of synthetic subgoal theorems are extracted — standalone lemmas and context-dependent lemmas with preceding subgoals as premises — creating a difficulty progression from easy subgoals to full theorems. Third, the final model (DeepSeek-V3-Base-671B) is trained via SFT on this data and then refined with GRPO reinforcement learning using binary proof-verification rewards, plus a novel consistency reward that penalizes structural deviation from the decomposed subgoal plan. The model operates in two modes: a fast non-CoT mode for direct proof generation, and a CoT mode that articulates informal reasoning before producing formal proof code.",
    "what_makes_it_good": "Three qualities elevate this work. First, the results are unambiguously SOTA and open-source: 88.9% on miniF2F-test and 49/658 on PutnamBench substantially advance the field, and reproducibility is ensured through open weights. Second, the intellectual contribution is architecturally clean — the insight that informal-to-formal bridging should happen at the proof-structure level (subgoal decomposition via 'have' statements) rather than the token level is both simple and powerful, and the cold-start → curriculum → RL pipeline is a reusable template. Third, the authors demonstrated exceptional scientific integrity by transparently reporting a reward hacking vulnerability where the 7B model exploited a Lean 4.9.0 UI bug in the 'apply?' tactic, initially inflating PutnamBench results — they identified, disclosed, and corrected this rather than burying it.",
    "limitations_acknowledged": "The authors implicitly acknowledge several gaps: geometry, combinatorics, and counting problems were excluded from AIME formalization because their Lean representations are 'potentially cumbersome,' revealing domain coverage limits. ProofNet-test performance (37.1% at Pass@1024) shows undergraduate-level mathematics remains difficult. The 7B model's reward hacking via Lean bugs demonstrates that RL-trained formal provers can learn to exploit verification tool weaknesses rather than develop genuine proving capability.",
    "open_questions": [
      "Can subgoal decomposition scale to IMO-level problems where the key difficulty is finding the right decomposition strategy itself — i.e., when the 'sketch' requires deep mathematical insight that even large LLMs lack?",
      "What is the performance ceiling for sampling-based approaches (Pass@k with large k) versus tree search methods? The paper uses no tree search at inference, suggesting significant untapped gains from combining decomposition with structured search (their stated AlphaProof-like aspiration).",
      "How brittle is the pipeline to the quality of the informal reasoning? If DeepSeek-V3 produces a flawed proof sketch (wrong decomposition strategy), does the system fail gracefully or waste all compute on doomed subgoals? What fraction of V3's sketches lead to successful compositions?"
    ],
    "building_blocks": [
      "DeepSeek-V3-671B as proof sketch generator (informal reasoning → formal 'have' statement chains)",
      "Lean 4 'have ... := sorry' pattern as the universal bridge format between informal and formal reasoning",
      "Cold-start data synthesis: pair informal CoT with composed formal proofs from subgoal resolution",
      "Curriculum learning via synthetic subgoal theorems (Type A: standalone, Type B: with context premises)",
      "GRPO reinforcement learning with binary proof-verification rewards",
      "Consistency reward for enforcing structural alignment between CoT decomposition and final proof",
      "Expert iteration: iteratively expanding training data by solving previously-unsolved problems with the improving model",
      "Two-mode inference: fast non-CoT for easy problems, deliberate CoT for harder ones",
      "Lean 4 proof assistant as deterministic verification oracle",
      "7B distilled model from 671B RL rollout data"
    ],
    "reviewer_feedback_summary": null,
    "relevance_to_seed": "This paper is the current exemplar of our exact research area — bridging informal and formal mathematical reasoning. Its core lesson for our work is that the bridge should be structural, not syntactic: rather than training a model to translate natural language proofs into formal code token-by-token, the winning strategy is to use informal reasoning to generate a formal proof skeleton (subgoal decomposition) and then fill in details with specialized tools. The cold-start data synthesis pipeline — using a general model's informal reasoning to bootstrap formal proving training data — is a directly reusable paradigm for autoformalization research. The 'substantially narrowing' gap between informal and formal performance (8/15 vs 6/15 on AIME) quantifies exactly how close the field is to closing this bridge."
  },
  {
    "title": "DeepSeek-Prover-V1.5: Harnessing Proof Assistant Feedback for Reinforcement Learning and Monte-Carlo Tree Search",
    "venue": "ICLR 2025",
    "problem_identification": "The authors identified that whole-proof generation (their own V1 approach) suffers from compounding errors: the autoregressive model develops incorrect beliefs about intermediate tactic states during long proofs, and a single misinterpretation cascades into invalid proof paths. Meanwhile, step-by-step tactic generation avoids this but requires expensive per-step verification communication. The gap they found was that no existing system unified these two paradigms — you either got the efficiency of whole-proof generation or the correctness-grounding of step-level verification, but not both. They found this gap by analyzing their own V1 system's failure modes, a classic 'build it, see where it breaks, fix that' research loop.",
    "key_insight": "A 'truncate-and-resume' mechanism can bridge whole-proof and step-level generation into a single unified framework: generate a full proof, truncate at the first compiler error, inject the verified tactic state back as a prompt suffix, and resume generation — turning what was a dichotomy between two proof strategies into a continuum that naturally slots into MCTS. The second key insight is that proof search has extremely sparse extrinsic rewards (only complete proofs score), so borrowing the RMax exploration bonus from tabular RL theory — rewarding the agent simply for reaching *new* tactic states — provides the curiosity signal needed to diversify search without a learned value function.",
    "innovation_type": "combination",
    "method_summary": "The system has four stages: (1) Pre-training on formal math corpora (Lean, Isabelle, Metamath) to build DeepSeek-Prover-V1.5-Base. (2) Supervised fine-tuning with two novel data augmentations — chain-of-thought comments interleaved with Lean tactics (annotated by DeepSeek-Coder V2 236B) and tactic-state annotations inserted as comments so the model learns to condition on compiler feedback. (3) Reinforcement learning via GRPO using binary proof-verification rewards from the Lean 4 compiler (RLPAF), trained on ~4.5k theorems with moderate SFT success rates to ensure the reward signal is neither too sparse nor trivially dense. (4) At inference, RMaxTS — an MCTS variant where the truncate-and-resume mechanism defines the state-action abstraction (each node is a tactic state, each edge is a tactic), and an intrinsic RMax reward (1 if a new tactic state is discovered, 0 otherwise) drives exploration via Discounted UCB to handle the non-stationarity of curiosity-based rewards. The system is massively parallelized with 256 MCTS runners, 32 thread workers per tree, and virtual losses to encourage diverse node selection.",
    "what_makes_it_good": "This paper succeeds because it is a *systems paper disguised as an algorithms paper* — every component (pre-training, SFT data augmentation, RL, tree search) is individually well-motivated and cleanly ablated across training stages (Base → SFT → RL → MCTS), making the contribution of each piece transparent. The truncate-and-resume mechanism is an elegantly simple idea that unifies two previously separate paradigms without requiring architectural changes to the base LLM. The RMax intrinsic reward is a principled import from the exploration theory literature (not an ad-hoc heuristic), and the authors correctly identify and solve the non-stationarity problem it introduces via DUCB. The 10+ percentage point improvement over V1 on miniF2F-test (50.0% → 63.5%) is a substantial empirical advance, and the paper is open-source, which significantly increases impact and reproducibility.",
    "limitations_acknowledged": "The authors explicitly note they focused only on the exploration aspect of RL in tree search, leaving the exploitation aspect (training a critic/value model to prune search branches and perform temporal credit assignment) entirely unexplored. They also acknowledge the framework is designed for individual theorem proving and has only nascent capabilities for file-level, multi-theorem theory proving in realistic Lean projects.",
    "open_questions": [
      "Can a learned critic model for partial proofs (analogous to AlphaZero's value network) substantially improve search efficiency by pruning unpromising branches, and what training signal would such a critic use given the extreme sparsity of proof-level rewards?",
      "How does the truncate-and-resume + RMaxTS approach scale to competition-level or research-level mathematics where proofs are much longer and the tactic state space is vastly larger — does the intrinsic reward signal degrade, and would hierarchical or subgoal-based search be needed?",
      "The CoT annotation was done by a proprietary 236B model (DeepSeek-Coder V2) — can this bootstrapping step be made self-sufficient (the prover annotates its own reasoning) without quality degradation, closing the loop for fully autonomous improvement?"
    ],
    "building_blocks": [
      "GRPO (Group Relative Policy Optimization) for RL without a critic model",
      "Lean 4 REPL + LeanDojo tactic state extraction",
      "Truncate-and-resume mechanism for bridging whole-proof and step-level generation",
      "RMax intrinsic reward strategy from tabular RL theory",
      "Discounted UCB (DUCB) for non-stationary bandit problems in MCTS",
      "Expert iteration / synthetic data loop with compiler verification",
      "Chain-of-thought annotation via a larger teacher model (DeepSeek-Coder V2 236B)",
      "vLLM for high-throughput inference",
      "miniF2F and ProofNet benchmarks (Lean 4 ports)",
      "Virtual loss technique for parallel MCTS",
      "DeepSeekMath-Base 7B as foundation model"
    ],
    "reviewer_feedback_summary": null,
    "relevance_to_seed": "This paper is directly central to bridging informal and formal mathematical reasoning: the chain-of-thought annotations interleaved with Lean tactics are a concrete instantiation of autoformalization-in-reverse (mapping formal steps back to informal reasoning to improve formal proof generation). The truncate-and-resume mechanism demonstrates that the compiler itself can serve as a verification oracle that grounds informal reasoning in formal correctness — a paradigm that any autoformalization system could adopt. For our research area, the key lesson is that the informal↔formal bridge is most effective when it operates *within* the proof generation process (as interleaved comments and tactic states), not as a separate pre-processing or post-processing step."
  },
  {
    "title": "Hilbert: Recursively Building Formal Proofs with Informal Reasoning",
    "venue": "ICLR 2026",
    "problem_identification": "The authors identified a stark quantitative gap between informal and formal mathematical reasoning: reasoning LLMs can solve ~83% of PutnamBench problems informally (per human verification), yet the best publicly available formal provers solve only ~13%. Prior bridging approaches (DSP, LEGO-Prover, DSP+) used only shallow, single-layer decomposition — they break a problem into subgoals once but cannot recursively decompose subgoals that remain too hard. The authors also observed that prover LLMs and reasoning LLMs have complementary failure modes: provers excel at syntactically correct short proofs but fail at language-intensive tasks like leveraging existing theorems; reasoners understand high-level proof strategy but produce syntactically broken formal code.",
    "key_insight": "Rather than treating informal reasoning as a one-shot translation step to formal proof (as in DSP-style approaches), the key insight is to use the informal reasoner as a recursive orchestrator that decomposes hard problems into subgoals, checks their mathematical correctness before attempting formalization, and routes each subgoal to whichever solver (prover or reasoner) can handle it — creating a recursive call stack of proof obligations where the formal verifier acts as the ground-truth termination condition at every level.",
    "innovation_type": "combination",
    "method_summary": "Hilbert orchestrates four components: (1) a Reasoner LLM (Gemini 2.5 Pro/Flash) for informal proofs and proof sketches, (2) a Prover LLM (DeepSeek-Prover-V2-7B or Goedel-Prover-V2-32B) for direct formal proof generation, (3) a Lean 4 Verifier for ground-truth checking, and (4) a semantic Retriever using sentence-transformer embeddings over Mathlib's informal theorem descriptions via FAISS. Given a theorem, Hilbert first attempts direct proof via the Prover (Phase 1). On failure, it enters Phase 2: the Reasoner retrieves relevant Mathlib theorems, generates a detailed informal proof, translates it into a Lean 4 proof sketch with 'have' statements (subgoals) marked by 'sorry' placeholders, extracts these as independent theorem statements, and assembles the final proof by replacing 'sorry' with subgoal calls. Each subgoal is solved via a three-strategy cascade: (a) direct Prover attempt, (b) 'shallow solve' where the Reasoner writes a short formal proof with iterative error correction, or (c) recursive decomposition (up to depth D=5). Critically, the Reasoner also performs mathematical correctness checking — flagging unprovable or poorly-formulated subgoals before wasting compute on them — and verifier feedback is propagated back at every stage for iterative refinement.",
    "what_makes_it_good": "The paper succeeds because it delivers overwhelming empirical results (99.2% on miniF2F, 70.0% on PutnamBench — a 422% improvement over the best public baseline SeedProver) while the method is conceptually clean and well-ablated. The ablation studies are particularly compelling: they isolate the contribution of recursive depth (75% at D=0 → 99.2% at D=5), retrieval (improves both accuracy AND reduces compute by ~30%), and the shallow-solve step. The paper also demonstrates generalizability across multiple model pairings including an open-source reasoner (gpt-oss-120b), showing the framework isn't just a wrapper around one proprietary model.",
    "limitations_acknowledged": "The authors acknowledge heavy reliance on strong reasoning LLMs (Gemini 2.5 Pro) for peak performance and high inference-time compute costs (up to 22-27M tokens per problem for the hardest cases). They also note that the framework's ceiling is bounded by the underlying LLMs' capabilities — it approaches but doesn't reach the ~82% informal proof rate reported by Dekoninck et al., suggesting the formalization gap isn't fully closed.",
    "open_questions": [
      "Can the proof traces and reasoning trajectories generated by Hilbert be used as training data to improve the underlying Prover and Reasoner models, creating the 'virtuous cycle' the authors mention in their conclusion? What is the quality/diversity of this synthetic data?",
      "How does the framework scale to research-level mathematics beyond competition problems (e.g., FrontierMath)? The recursive decomposition assumes problems can be broken into 'simpler' subgoals, but research-level proofs may require novel lemmas that don't decompose neatly.",
      "What is the right balance between inference-time compute and model training? Hilbert uses up to 27M tokens per problem — could some of this agentic overhead be distilled into a single model that learns the decomposition strategy implicitly, similar to how AlphaProof internalized search?"
    ],
    "building_blocks": [
      "Lean 4 + Mathlib v4.15.0 as formal verification backbone",
      "Kimina Lean Server for Lean interaction",
      "Sentence-transformers (all-mpnet-base-v2) + FAISS for semantic theorem retrieval over mathlib_informal dataset",
      "Proof sketch paradigm: 'have' statements with 'sorry' placeholders as subgoal interface",
      "DeepSeek-Prover-V2-7B and Goedel-Prover-V2-32B as specialized formal provers",
      "Gemini 2.5 Pro/Flash as informal reasoning backbone",
      "Recursive subgoal decomposition with depth-limited search",
      "Verifier-in-the-loop iterative error correction",
      "LLM-as-judge for mathematical correctness checking of subgoals",
      "miniF2F and PutnamBench benchmarks"
    ],
    "reviewer_feedback_summary": null,
    "relevance_to_seed": "This paper is the current state-of-the-art in our exact research area of bridging informal and formal mathematical reasoning. Its key lesson for our work is architectural: the winning strategy is not to build a better single autoformalization model, but to design a multi-agent system where informal reasoning, formal proving, verification, and retrieval are separate specialized modules orchestrated by a recursive decomposition controller. Any new work in this space must either beat Hilbert's numbers or address its limitations — particularly the high compute cost, reliance on proprietary models, or the gap between competition math and research-level mathematics."
  },
  {
    "title": "Rethinking and Improving Autoformalization: Towards a Faithful Metric and a Dependency Retrieval-based Approach",
    "venue": "ICLR 2025 (Spotlight)",
    "problem_identification": "The authors performed a systematic audit of the autoformalization pipeline and identified two foundational gaps that the community had been working around rather than solving: (1) no existing automated evaluation metric is simultaneously formal-grounded, human-aligned, and universal — BLEU is semantically shallow, typecheck is necessary but not sufficient, LLM graders are non-deterministic and fragile, and SMT-based approaches (Murphy et al.) are domain-restricted to Euclidean geometry; (2) autoformalizers operate context-blind, ignoring the library of previously formalized definitions and theorems, which causes severe hallucination of identifiers especially in out-of-distribution settings. They found gap #1 by asking what formal properties an equivalence metric *should* have (reflexivity, symmetry, transitivity, human-alignment, universality) and showing no existing metric satisfies all five; they found gap #2 by doing error analysis showing 'definition misalignment' is the dominant failure mode.",
    "key_insight": "Lean 4's built-in definitional equality is already a principled equivalence relation (reflexive, symmetric, transitive) over formal statements, but it is too strict for evaluating autoformalization because it cannot handle trivially equivalent reformulations like 'n + 0' vs 'n'. The core aha: extend definitional equality by (1) equipping it with a restricted set of tactic-based transformation primitives that allow one statement to be rewritten before comparison, and (2) making this check bidirectional — s_P ~_B s_Q iff s_P can be transformed to be definitionally equal to s_Q AND vice versa. The LLM generates candidate tactic sequences, but the Lean kernel formally verifies them, yielding a neuro-symbolic metric that inherits formal guarantees while matching human intuition.",
    "innovation_type": "combination",
    "method_summary": "BEq (Bidirectional Extended Definitional Equivalence) works by checking two directions: to test s_P ←_U s_Q, assume s_Q is true (close with sorry), then use an LLM (InternLM-Math-Plus-20B, 5-shot, beam search) to generate tactic sequences from a restricted set R = {apply, cases', constructor, exact, exact?, ext, have, intro, intros, rw, use} that transform s_P into something definitionally equal to s_Q. If any candidate succeeds, the implication holds; BEq holds iff both directions succeed. For the retrieval component, they parse Mathlib 4's full dependency graph (243,797 formal objects), topologically sort and informalize objects bottom-up across 24 generations using an LLM, creating training data that preserves dependency context. A dense retriever (fine-tuned BGE-M3) embeds informal statements and retrieves top-k dependent formal objects from the library. The RAutoformalizer (fine-tuned InternLM-Math-Base-7B) then generates formal statements conditioned on both the informal statement and retrieved dependencies. Con-NF benchmark is built from 961 cleaned theorem pairs from the Lean 4 Con(NF) library (Quine's New Foundations consistency proof), providing genuinely OOD evaluation since it uses different foundational theory than Mathlib.",
    "what_makes_it_good": "This paper succeeds because it identifies and solves infrastructure-level problems that the entire autoformalization community needs — a reliable evaluation metric and a method to reduce hallucination — rather than just pushing numbers on existing benchmarks. The theoretical grounding is unusually rigorous for an ML paper: BEq is formally proven to be an equivalence relation (Theorem 1), and its design choices (which tactics to include, bidirectionality) are systematically ablated. The three contributions (BEq metric, RAutoformalizer, Con-NF benchmark) form a tightly integrated narrative: BEq exposes how bad existing methods truly are, the retrieval approach addresses the root cause, and Con-NF stress-tests OOD generalization. Reviewers specifically praised the pioneering nature of the evaluation work and the inclusion of both in-distribution and OOD testing.",
    "limitations_acknowledged": "BEq depends on high-quality ground-truth formal statements (unusable for benchmarks lacking them) and its quality depends on careful design of the restricted tactic set R and the LLM approximation of the transformation function T, meaning recall can suffer when the LLM fails to find valid tactic proofs (-12.85% vs. majority voting on recall). For RAutoformalizer, retrieval quality is the bottleneck — the oracle retrieval experiment (RA+R) shows 10× headroom for improvement over current retrieval, and sophisticated techniques like multi-vector embeddings, re-ranking, and query augmentation are left as future work.",
    "open_questions": [
      "Can BEq be extended beyond statement equivalence to evaluate proof autoformalization and full theory autoformalization, where the notion of 'equivalence' is richer and involves structural correspondence between proof strategies?",
      "The oracle retrieval experiment shows massive untapped potential (BEq@8: 16.86% actual vs 55.36% with perfect retrieval on Con-NF) — what retrieval architectures or hybrid symbolic-neural approaches can close this gap, especially for OOD libraries with different foundational axioms?",
      "Can topological informalization be applied in reverse — using the dependency structure of informal mathematical texts (textbooks, papers) to improve formalization by identifying which concepts need to be formalized first, creating a curriculum for autoformalizers?"
    ],
    "building_blocks": [
      "Lean 4 tactic mode and definitional equality as formal verification backbone",
      "BGE-M3 embedding model fine-tuned for dependency retrieval",
      "Dense Passage Retrieval (DPR) framework adapted to formal math libraries",
      "Topological informalization — LLM-based informalization respecting dependency DAG order across 24 generations",
      "InternLM-Math-Plus-20B as tactic generator within BEq",
      "InternLM-Math-Base-7B as base autoformalizer model",
      "Mathlib 4 dependency graph (243,797 formal objects, 139,933 theorems)",
      "Con-NF library (Quine's New Foundations consistency proof) for OOD benchmark",
      "ProofNet benchmark for in-distribution evaluation",
      "Beam search with restricted tactic set for controlled equivalence checking",
      "Hard negative mining from top-100 BM25/BGE-M3 candidates for retriever training"
    ],
    "reviewer_feedback_summary": "Five reviewers assessed the paper. Key praise: (1) BEq was called 'pioneering work' in autoformalization evaluation that addresses a genuine community gap; (2) the theoretical grounding (proving equivalence relation properties) and interpretability via Lean 4 tactics were highlighted; (3) inclusion of both in-distribution and OOD evaluation was valued. Key concerns: (1) Reviewer 9PuK flagged a logic gap — BEq evaluates formal-statement equivalence but the paper frames it as evaluating autoformalization quality, and model-based evaluators exist as alternatives to ground-truth comparison (authors clarified ground-truth comparison remains the mainstream benchmarking paradigm); (2) Reviewer pPF9 raised insufficient detail on human evaluation protocols, Con-NF quality control, and missing prompt templates (all addressed with expanded appendices); (3) Reviewer fV7x requested ablations across different LLM families for BEq, CoT/ToT reasoning baselines, and stronger retrieval baselines (authors provided experiments across 7B-236B models showing robustness, added CoT experiments, and compared against BM25/BGE-M3 baselines). Post-rebuttal, all reviewers agreed on acceptance. The Area Chair noted the paper makes significant contributions across evaluation, methodology, and benchmarking.",
    "relevance_to_seed": "This paper is directly central to bridging informal and formal mathematical reasoning: it provides both the measurement instrument (BEq) and a concrete mechanism (dependency retrieval) for improving autoformalization. The key transferable lesson for our research area is that progress on the *generation* side of autoformalization was being masked by unreliable evaluation — the field needed to solve the measurement problem first. The dependency retrieval paradigm also suggests that autoformalization should not be treated as isolated sentence-level translation but as a context-aware task grounded in the formal library ecosystem, which has implications for how we design proof verification pipelines that connect informal reasoning to formal proof assistants."
  },
  {
    "title": "Lean-STaR: Learning to Interleave Thinking and Proving",
    "venue": "ICLR 2025 (Spotlight)",
    "problem_identification": "The authors identified that formal theorem-proving datasets (like Lean's Mathlib) contain only (proof_state, tactic) pairs, discarding the informal deliberation that human mathematicians perform before each proof step. This 'missing reasoning' gap means models trained on formal proofs learn to mimic actions without understanding the strategic thinking behind them. They found this gap by observing that chain-of-thought techniques work well in informal math but hadn't been successfully integrated into formal proving — largely because no thought-annotated training data exists for formal proofs, and Lean (unlike Isabelle) lacks sledgehammer-style automation that could compensate.",
    "key_insight": "Rather than trying to generate thoughts *before* seeing the correct tactic (which produces poor-quality reasoning), they inverted the problem: use the ground-truth tactic as a conditioning signal to *retrospectively* synthesize plausible thoughts that could have led to that tactic, then train the model to reproduce those thoughts at inference time without seeing the answer. This 'rationalize first, internalize later' approach elegantly sidesteps the chicken-and-egg problem of needing good thoughts to find good tactics while needing good tactics to know what thoughts are useful.",
    "innovation_type": "combination",
    "method_summary": "Lean-STaR operates in three stages. First, supervised fine-tuning (SFT) trains a base model on standard (proof_state → tactic) pairs from Mathlib. Second, retrospective thought augmentation uses GPT-4 to generate natural-language rationales conditioned on both the proof state AND the known-correct tactic, producing ~52K–140K (state, thought, tactic) triples; the model is then fine-tuned on these thought-augmented examples to produce thoughts before each tactic (Lean-CoT). Third, expert iteration bootstraps further: the thought-augmented model samples K complete proof trajectories per theorem, the Lean verifier filters for correct proofs (reward=1), and the model is re-fine-tuned on the union of original and newly-verified thought-augmented trajectories. This loop runs for 1–2 iterations. Critically, at inference time, the authors use parallel sampling of complete trajectories rather than best-first tree search, because log-probability-based scoring degrades when natural language thoughts inflate sequence length unpredictably.",
    "what_makes_it_good": "This paper succeeds because it takes two well-established techniques (chain-of-thought reasoning and expert iteration) and combines them in a principled way for a domain where their interaction is non-obvious — formal theorem proving has a unique verifier (the Lean kernel) that makes expert iteration clean, while the absence of informal reasoning in formal proofs makes CoT high-value. The ablation showing that expert iteration alone yields 43.0% but Lean-STaR yields 45.5% (with CoT contributing independently) is clean experimental design that isolates the contribution. The observation that thoughts increase *diversity* of proof attempts (better scaling with K) rather than just accuracy per attempt is a subtle but important finding that elevates the work beyond a simple engineering contribution.",
    "limitations_acknowledged": "The authors explicitly note computational scalability constraints: training datasets remain modest (50K–140K examples), GPT-4 oracle generation is expensive and may introduce biases, and expert iteration is bottlenecked by Lean's CPU/IO-bound verification speed. They also acknowledge that thought quality varies — some generated thoughts c
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
  "promptId": "76a0bac0-75d1-4298-b904-07edc10f3cd8",
  "type": "user",
  "uuid": "b4767faa-0a69-4640-a2a0-f2e887ac0e61",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c2424f1-4faa-4690-8ff5-2cc4b82c5bcd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T05:23:06.981Z_

```json
{
  "parentUuid": "b4767faa-0a69-4640-a2a0-f2e887ac0e61",
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
  "uuid": "361b9e86-6abf-40ec-ab83-b7950b42338a",
  "timestamp": "2026-05-28T05:23:06.981Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c2424f1-4faa-4690-8ff5-2cc4b82c5bcd",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T05:23:06.981Z_

```json
{
  "parentUuid": "361b9e86-6abf-40ec-ab83-b7950b42338a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0bcf2e8d-75a1-412e-a222-d77426dfc64d",
  "timestamp": "2026-05-28T05:23:06.981Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c2424f1-4faa-4690-8ff5-2cc4b82c5bcd",
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
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-28 (UTC).**  ## Research area: Bridging Informal and Formal Mathema…",
  "leafUuid": "0bcf2e8d-75a1-412e-a222-d77426dfc64d",
  "sessionId": "9c2424f1-4faa-4690-8ff5-2cc4b82c5bcd"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize autoformalization and proof verification research strategy",
  "sessionId": "9c2424f1-4faa-4690-8ff5-2cc4b82c5bcd"
}
```

---

### Assistant

_source line 8 · 2026-05-28T05:23:33.139Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to synthesize 18 paper analyses into a strategic "Field Guide" for the research area of "Bridging Informal and Formal Mathematical Reasoning — Autoformalization and Proof Verification." However, I only see detailed analyses for about 6 papers (the rest were truncated). Let me work with what I have and produce the best possible synthesis.

Let me carefully analyze the papers I have:

1. **AlphaProof** (Nature 2025) - RL + autoformalization + TTRL for olympiad-level formal proofs


2. **DeepSeek-Prover-V2** (arXiv 2025) - Uses subgoal decomposition through intermediate statements, generates synthetic training data from scratch, and applies GRPO reinforcement learning
3. **DeepSeek-Prover-V1.5** (ICLR 2025) - Implements a truncate-and-resume strategy with RMaxTS for Monte Carlo tree search in formal proving
4. **Hilbert** (ICLR 2026) - Orchestrates a recursive multi-agent system where an informal reasoner coordinates with a formal prover
5. **Rethinking Autoformalization** (ICLR 2025 Spotlight) - Introduces the BEq metric and dependency retrieval techniques for autoformalization
6. **Lean-STaR** (ICLR 2025 Spotlight) - Interleaves thinking and proving steps with retrospective thought augmentation

Now I'm identifying the core innovation patterns across these papers: verification-as-reward loops driving reinforcement learning, subgoal decomposition through formal sketches, pairing large informal models with smaller formal provers, retrospective rationalization where explanations follow the answer, and expert iteration cycles that leverage formal verification. I'm also noting what reviewers seem to value, starting with thorough ablation studies.

Looking at what the field still needs: ablations isolating individual components, reproducible open-source implementations, evaluation across both in-distribution and out-of-distribution settings, solid theoretical foundations, solutions to infrastructure bottlenecks, and results that can be formally verified. The major gaps are clear—geometry and combinatorics remain weak spots, research-level mathematics beyond competitions hasn't been tackled, compute requirements are prohibitive, autoformalization metrics are underdeveloped, retrieval systems are limiting performance, and bidirectional translation between informal and formal math is unexplored.

I'm seeing several untried combinations worth exploring: applying the BEq metric within RL reward shaping, merging recursive decomposition with tree search, combining dependency retrieval with subgoal breakdown, and integrating Lean-STaR's reasoning with tree search methods. There are also critical pitfalls to avoid—reward hacking like DeepSeek-V2's Lean bug exploitation, unreliable metrics masking real progress, treating autoformalization as simple context-free translation, and papers that hide their actual compute costs.

Writing this up as a structured JSON guide.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bcf2e8d-75a1-412e-a222-d77426dfc64d",
  "isSidechain": false,
  "requestId": "req_011CbUQbryYpBkgLDUviufvD",
  "type": "assistant",
  "uuid": "61cb7724-8be5-4532-9622-662b7ea60e42",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c2424f1-4faa-4690-8ff5-2cc4b82c5bcd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S9WpAVLqbGMCqj5QcMHXSm",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11392,
      "cache_read_input_tokens": 11014,
      "output_tokens": 8939,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11392,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 8939,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 11392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11392
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

_source line 9 · 2026-05-28T05:26:28.024Z_

I'll analyze the paper analyses in depth to synthesize the field guide. Let me first review the truncated portion to see if there's additional context I should account for.

Given the 6 fully detailed papers (AlphaProof, DeepSeek-Prover-V2, DeepSeek-Prover-V1.5, Hilbert, Rethinking Autoformalization/BEq, and Lean-STaR), plus the knowledge that 12 more papers were in the set, I'll produce the strategic synthesis now.

```json
{
  "innovation_patterns": [
    {
      "pattern": "Formal-Verification-as-RL-Reward Loop",
      "description": "Use the deterministic, binary signal from a proof assistant (Lean 4 kernel) as the reward function for reinforcement learning, eliminating the need for learned reward models and their associated hallucination/gaming risks. The key enabler is that formal verification is one of the few domains where correctness is decidable and cheap to check relative to generation.",
      "examples": ["AlphaProof (Nature 2025)", "DeepSeek-Prover-V2", "DeepSeek-Prover-V1.5"],
      "success_rate": "high"
    },
    {
      "pattern": "Large Informal Reasoner + Small Formal Prover Composition",
      "description": "Rather than training a single model to handle both informal mathematical reasoning and formal proof synthesis, decompose the task between a large general-purpose LLM (for proof strategy, subgoal identification, and natural language reasoning) and a small specialized model (for tactic generation and formal syntax). The informal model generates proof sketches or decompositions; the formal model fills in verified details. This exploits the insight that strategic reasoning and syntactic formalization are separable competencies with different scaling properties.",
      "examples": ["DeepSeek-Prover-V2 (DeepSeek-V3 671B + 7B prover)", "Hilbert (Gemini 2.5 Pro + DeepSeek-Prover-V2-7B)"],
      "success_rate": "high"
    },
    {
      "pattern": "Proof Sketch as Bridge Format ('have ... := sorry')",
      "description": "Use Lean 4's 'have' statement with 'sorry' placeholders as the universal interface between informal reasoning and formal proof. This format is simultaneously valid formal syntax, human-readable, and naturally decomposes proofs into independently verifiable subgoals. It transforms autoformalization from a monolithic translation problem into a structured decomposition problem.",
      "examples": ["DeepSeek-Prover-V2", "Hilbert"],
      "success_rate": "high"
    },
    {
      "pattern": "Retrospective Rationalization for Data Bootstrapping",
      "description": "When no training data exists for the desired intermediate representations (e.g., natural-language reasoning traces for formal proofs), generate it retrospectively: condition the annotation on both the input AND the known-correct output, producing plausible rationales that 'explain' the correct action. Then train the model to reproduce those rationales at inference time without seeing the answer. This sidesteps the chicken-and-egg problem of needing good reasoning to find correct actions.",
      "examples": ["Lean-STaR (GPT-4 retrospective thought generation)", "DeepSeek-Prover-V1.5 (DeepSeek-Coder V2 236B CoT annotation)"],
      "success_rate": "medium"
    },
    {
      "pattern": "Recursive/Hierarchical Decomposition with Verification at Every Level",
      "description": "Rather than a single-pass translation or single-layer decomposition, recursively decompose problems into subgoals, with the formal verifier checking correctness at each level of the recursion. This converts a hard single-shot problem into many easier problems while preserving end-to-end formal guarantees. The key is making the recursion depth adaptive to problem difficulty.",
      "examples": ["Hilbert (recursive decomposition up to D=5, yielding 99.2% on miniF2F)"],
      "success_rate": "high"
    },
    {
      "pattern": "Infrastructure-First Contributions (Metrics, Benchmarks, Retrieval)",
      "description": "Rather than pushing SOTA on existing benchmarks with incremental method improvements, identify and solve foundational infrastructure problems (evaluation metrics, data pipelines, retrieval systems) that the entire community needs. These papers have outsized impact because they change how subsequent work is measured and grounded.",
      "examples": ["Rethinking Autoformalization / BEq (ICLR 2025 Spotlight)"],
      "success_rate": "high"
    },
    {
      "pattern": "Test-Time Compute Scaling via Structured Search",
      "description": "Scale inference-time compute through structured search (MCTS, AND-OR trees, recursive decomposition) rather than naive sampling. The formal verifier enables efficient pruning and backtracking. Innovations include curiosity-driven exploration (RMax), truncate-and-resume for bridging whole-proof and step-level generation, and test-time RL (TTRL) for per-problem adaptation.",
      "examples": ["AlphaProof (AND-OR tree + TTRL)", "DeepSeek-Prover-V1.5 (RMaxTS)"],
      "success_rate": "high"
    },
    {
      "pattern": "Expert Iteration with Formal Verification Filter",
      "description": "Iteratively expand training data by (1) using the current model to attempt new problems, (2) filtering successful attempts through the formal verifier, and (3) adding verified solutions to the training set. This creates a self-improving data flywheel where the model's own correct outputs bootstrap its next training round.",
      "examples": ["DeepSeek-Prover-V1.5", "Lean-STaR", "DeepSeek-Prover-V2", "AlphaProof"],
      "success_rate": "high"
    }
  ],
  "reviewer_preferences": [
    "Verifiable, formally-checked results that are immune to the 'memorization' critique: papers accepted at top venues (Nature, ICLR) uniformly provide proofs verified by an independent formal checker (Lean 4 kernel), making results unambiguous. AlphaProof's Nature acceptance was driven by the independently verifiable IMO milestone, not methodological novelty per se.",
    "Clean ablation studies that isolate the contribution of each component: DeepSeek-Prover-V1.5's stage-by-stage ablation (Base → SFT → RL → MCTS) and Hilbert's recursive depth ablation (75% at D=0 → 99.2% at D=5) were specifically praised. Reviewers want to know which pieces matter and by how much.",
    "Open-source models and reproducibility: DeepSeek-Prover-V2's open weights were explicitly noted as a quality that 'elevates' the work. Papers that are unreproducible outside a handful of labs (AlphaProof's 180K TPU-days) must compensate with undeniable milestone results.",
    "Both in-distribution and out-of-distribution evaluation: The BEq paper was praised for including Con-NF (OOD) alongside ProofNet (in-distribution). Reviewers are suspicious of methods that only work within the training distribution.",
    "Theoretical grounding for design choices, not just empirical heuristics: BEq's formal proof that it constitutes an equivalence relation (Theorem 1) and DeepSeek-Prover-V1.5's principled import of RMax from tabular RL theory (rather than an ad-hoc exploration bonus) were specifically rewarded. Reviewers in this area expect mathematical rigor in the methodology, not just the results.",
    "Honest reporting of failures and limitations: DeepSeek-Prover-V2's transparent disclosure of reward hacking via a Lean 4.9.0 bug, and AlphaProof's detailed compute cost reporting, were cited as evidence of scientific integrity. Reviewers penalize papers that hide failure modes.",
    "Addressing infrastructure gaps the community needs (metrics, benchmarks, retrieval), not just incremental SOTA improvements: The BEq paper's Spotlight acceptance was driven by reviewers recognizing it solves a foundational problem ('pioneering work') rather than just beating a number."
  ],
  "field_gaps": [
    {
      "gap": "Geometry and combinatorics remain poorly formalized and poorly solved",
      "evidence": "AlphaProof reports only 20.3% on formal-IMO combinatorics vs 75.7% on number theory. DeepSeek-Prover-V2 explicitly excluded geometry and combinatorics from AIME formalization because their Lean representations are 'potentially cumbersome.' This is not a modeling gap but a representation gap — these domains lack good formal libraries and natural encodings in Lean 4.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "Research-level mathematics beyond competition problems",
      "evidence": "AlphaProof acknowledges restriction to 'high-school/undergraduate competition mathematics.' Hilbert's recursive decomposition assumes problems decompose into 'simpler' subgoals, but research math may require novel lemmas. AlphaProof cannot handle 'theory-building.' No system has demonstrated capability on FrontierMath or genuine research-level open problems.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "Retrieval quality for formal library dependencies during autoformalization",
      "evidence": "BEq paper's oracle retrieval experiment shows massive untapped potential: BEq@8 of 16.86% actual vs 55.36% with perfect retrieval on Con-NF — a 3.3× gap. They note 'sophisticated techniques like multi-vector embeddings, re-ranking, and query augmentation are left as future work.' Hilbert's retrieval ablation shows retrieval improves both accuracy AND reduces compute by ~30%, suggesting better retrieval has compounding benefits.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Distilling agentic/search-heavy inference into efficient single-model generation",
      "evidence": "Hilbert uses up to 27M tokens per problem. AlphaProof requires 50-200+ TPU-days per problem via TTRL. Hilbert's own authors ask: 'could some of this agentic overhead be distilled into a single model that learns the decomposition strategy implicitly, similar to how AlphaProof internalized search?' DeepSeek-Prover-V2's cold-start pipeline is a partial answer (distilling 671B pipeline into a single 671B model), but the compute cost remains enormous.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "Bidirectional autoformalization (formal → informal for explanation)",
      "evidence": "AlphaProof's open questions explicitly ask: 'Can the autoformalization pipeline be made bidirectional — not just informal→formal for training, but formal→informal for explaining AI-discovered proofs to humans?' The BEq paper's topological informalization is a primitive version of this (LLM-based informalization respecting dependency DAG order), but it is used only for retrieval data creation, not for proof explanation.",
      "difficulty": "medium",
      "impact_if_solved": "medium"
    },
    {
      "gap": "Reliable automated evaluation of autoformalization quality",
      "evidence": "BEq paper demonstrates that BLEU, typecheck, and LLM graders are all inadequate. BEq itself has limitations: depends on high-quality ground-truth formal statements, recall suffers when the LLM fails to find valid tactic proofs (-12.85% vs majority voting). No universal, ground-truth-free evaluation method exists for autoformalization.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Learned value functions / critics for partial formal proofs",
      "evidence": "DeepSeek-Prover-V1.5 explicitly states they 'focused only on the exploration aspect of RL in tree search, leaving the exploitation aspect (training a critic/value model to prune search branches) entirely unexplored.' AlphaProof uses a value network but its training requires 80K TPU-days. No open-source system has a well-trained proof value function.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "File-level and multi-theorem theory proving in realistic Lean projects",
      "evidence": "DeepSeek-Prover-V1.5 acknowledges only 'nascent capabilities for file-level, multi-theorem theory proving in realistic Lean projects.' All benchmarks (miniF2F, PutnamBench, ProofNet) evaluate single-theorem proving. Real mathematical practice involves developing interconnected theories, not solving isolated problems.",
      "difficulty": "high",
      "impact_if_solved": "high"
    }
  ],
  "untried_combinations": [
    {
      "idea_sketch": "BEq-guided RL reward shaping for autoformalization training",
      "from_papers": ["Rethinking Autoformalization / BEq", "DeepSeek-Prover-V2", "AlphaProof"],
      "why_promising": "Currently, RL for formal proving uses a binary reward (proof checks or not). BEq provides a principled, formally-grounded continuous signal for how 'close' a formalization is to the target. Using BEq as an intermediate reward for autoformalization models could provide much denser training signal than binary verification alone, addressing the sparse reward problem that all RL-based provers face. No paper has used BEq (or any equivalence metric) as an RL reward signal."
    },
    {
      "idea_sketch": "Recursive decomposition (Hilbert) + test-time RL (AlphaProof TTRL) for hard subgoals",
      "from_papers": ["Hilbert", "AlphaProof"],
      "why_promising": "Hilbert decomposes problems recursively but uses fixed models at each decomposition level. AlphaProof's TTRL adapts the model per-problem by generating variant curricula. Combining these: when Hilbert's recursive decomposition hits a hard subgoal that no fixed solver can handle, spawn a TTRL micro-training session that generates variants of that subgoal and adapts the prover. This could break through Hilbert's ceiling (the ~82% informal proof rate) by bringing per-subgoal adaptation to a multi-agent framework."
    },
    {
      "idea_sketch": "Dependency-aware retrieval (BEq paper) integrated into recursive proof decomposition (Hilbert/DeepSeek-V2)",
      "from_papers": ["Rethinking Autoformalization / BEq", "Hilbert", "DeepSeek-Prover-V2"],
      "why_promising": "Hilbert uses simple sentence-transformer retrieval over Mathlib's informal descriptions, and the BEq paper shows that dependency-graph-aware retrieval dramatically improves autoformalization. Integrating BEq's topological dependency retrieval (which preserves formal library structure) into Hilbert's recursive framework would provide each decomposition level with precisely the formal context it needs. The BEq oracle experiment shows 3.3× headroom from better retrieval — this is low-hanging fruit."
    },
    {
      "idea_sketch": "Lean-STaR's interleaved thinking + DeepSeek-Prover-V1.5's tree search (MCTS with thoughts)",
      "from_papers": ["Lean-STaR", "DeepSeek-Prover-V1.5"],
      "why_promising": "Lean-STaR explicitly notes that 'log-probability-based scoring degrades when natural language thoughts inflate sequence length unpredictably,' which is why they abandoned tree search in favor of parallel sampling. But DeepSeek-Prover-V1.5's truncate-and-resume mechanism + RMax intrinsic reward evaluates proof states (not token probabilities) for search guidance. Combining interleaved thoughts (Lean-STaR) with state-based MCTS (V1.5) could retain the diversity benefits of thinking while using the tactic state — not token log-probs — as the search signal, overcoming Lean-STaR's stated limitation."
    },
    {
      "idea_sketch": "Bidirectional autoformalization pipeline: formal proofs → informal explanations → training data for better informal→formal models",
      "from_papers": ["AlphaProof", "Rethinking Autoformalization / BEq", "Lean-STaR"],
      "why_promising": "AlphaProof created 80M formal statements via informal→formal autoformalization but asks whether formal→informal is possible. Lean-STaR's retrospective rationalization shows you can generate plausible informal explanations conditioned on known-correct formal proofs. The BEq paper's topological informalization provides structure. A full bidirectional pipeline (formalize → verify → explain → use explanations as training data for better formalization) would create a self-improving loop where both directions bootstrap each other. No paper has closed this full cycle."
    },
    {
      "idea_sketch": "Curriculum learning via topological dependency ordering for autoformalization",
      "from_papers": ["Rethinking Autoformalization / BEq", "DeepSeek-Prover-V2", "AlphaProof"],
      "why_promising": "The BEq paper's topological informalization processes Mathlib's 243K objects in dependency order across 24 generations. DeepSeek-Prover-V2 uses curriculum learning (easy subgoals → full theorems). No one has combined these: train an autoformalizer in topological dependency order, where each formalized definition/theorem becomes context for formalizing downstream theorems. This mirrors how humans learn mathematics (foundations first) and would naturally provide the dependency context that BEq shows is critical for reducing hallucination."
    },
    {
      "idea_sketch": "Multi-agent debate for subgoal correctness checking before formalization",
      "from_papers": ["Hilbert", "DeepSeek-Prover-V2"],
      "why_promising": "Hilbert uses a single LLM-as-judge for mathematical correctness checking of subgoals. DeepSeek-Prover-V2's open question asks about failure modes when V3 produces flawed proof sketches. Using multi-agent debate (multiple informal reasoners evaluating each other's subgoal proposals) before committing to expensive formalization could filter out doomed decomposition strategies early, reducing wasted compute — a key limitation of both systems."
    }
  ],
  "method_building_blocks": [
    {
      "tool": "Lean 4 'have ... := sorry' proof sketch format",
      "what_it_does": "Provides a structured bridge between informal reasoning (each 'have' is a human-readable intermediate goal) and formal verification (the overall structure is valid Lean syntax, and each 'sorry' can be independently resolved). Enables compositional proof construction where subgoals are verified independently.",
      "used_by": ["DeepSeek-Prover-V2", "Hilbert"],
      "could_be_applied_to": "Autoformalization of textbook proofs — convert informal step-by-step proofs into 'have' chains, then resolve each step independently. Also applicable to interactive proof tutoring systems where students fill in 'sorry' gaps."
    },
    {
      "tool": "GRPO (Group Relative Policy Optimization)",
      "what_it_does": "RL algorithm that bypasses the need for a learned value/critic model by computing advantages relative to other samples in the same group. Particularly useful in formal proving where reward is binary and sparse, making critic training difficult.",
      "used_by": ["DeepSeek-Prover-V1.5", "DeepSeek-Prover-V2"],
      "could_be_applied_to": "Training autoformalization models with BEq-based rewards, where the equivalence metric provides binary feedback similar to proof verification but for statement-level correctness."
    },
    {
      "tool": "Truncate-and-resume mechanism",
      "what_it_does": "Generates a complete proof, truncates at the first compiler error, injects the verified tactic state back as context, and resumes generation. Bridges whole-proof generation (efficient) with step-level verification (correct) into a single continuum that naturally integrates with tree search.",
      "used_by": ["DeepSeek-Prover-V1.5"],
      "could_be_applied_to": "Autoformalization error correction — generate a full formalization, detect the first semantic error via BEq or type-checking, inject the correct formal context up to that point, and resume. Could also be used for code generation with compiler feedback."
    },
    {
      "tool": "Test-time reinforcement learning (TTRL)",
      "what_it_does": "For each hard target problem, generates diverse formal variants (simplifications, generalizations, related lemmas) and runs focused RL training on this bespoke micro-curriculum, adapting the model specifically for that problem. Yields 15+ percentage point improvements beyond search scaling alone.",
      "used_by": ["AlphaProof"],
      "could_be_applied_to": "Hard autoformalization targets — when a standard autoformalizer fails on a complex theorem, generate variant formalizations of simpler/related theorems as a curriculum, adapt the model, then attempt the original. Also applicable to any verification-grounded task with a hard distribution shift."
    },
    {
      "tool": "BEq (Bidirectional Extended Definitional Equivalence)",
      "what_it_does": "A neuro-symbolic evaluation metric for autoformalization that extends Lean 4's definitional equality with LLM-generated tactic transformations, checked bidirectionally. Provides formally-grounded, human-aligned equivalence judgments between formal statements.",
      "used_by": ["Rethinking Autoformalization / BEq"],
      "could_be_applied_to": "As a reward signal for RL-based autoformalization training (replacing or augmenting binary type-check). As a filter for expert iteration data quality. As a deduplication criterion for formal mathematical datasets."
    },
    {
      "tool": "Topological informalization of formal libraries",
      "what_it_does": "Parse a formal library's dependency graph, topologically sort all objects, then informalize bottom-up across generations using an LLM — each object is informalized with context from its already-informalized dependencies. Produces parallel informal-formal corpora that respect mathematical prerequisite structure.",
      "used_by": ["Rethinking Autoformalization / BEq"],
      "could_be_applied_to": "Creating training data for bidirectional autoformalization. Generating natural-language documentation for Mathlib or other formal libraries. Building curriculum orderings for teaching autoformalizers or proof assistants."
    },
    {
      "tool": "RMax intrinsic reward for proof search",
      "what_it_does": "Assigns a curiosity bonus of 1 for reaching a novel tactic state and 0 for revisiting known states, providing dense exploration signal in the extremely sparse reward landscape of formal proving. Combined with Discounted UCB to handle the non-stationarity of novelty rewards.",
      "used_by": ["DeepSeek-Prover-V1.5"],
      "could_be_applied_to": "Exploring the space of autoformalization variants — reward the model for producing formally distinct (by definitional equality) formalization candidates rather than semantically redundant ones. Also applicable to any search-based formal reasoning where complete-proof rewards are too sparse."
    },
    {
      "tool": "Semantic retrieval over Mathlib using sentence-transformers + FAISS",
      "what_it_does": "Embeds informal theorem descriptions with a sentence transformer model and uses FAISS for efficient nearest-neighbor retrieval over Mathlib's informal descriptions, providing relevant library context to the prover/autoformalizer.",
      "used_by": ["Hilbert"],
      "could_be_applied_to": "Any formal proving or autoformalization pipeline that currently operates context-blind. The BEq paper's oracle experiment shows retrieval has 3.3× headroom for improvement, suggesting this building block is high-value but underoptimized."
    },
    {
      "tool": "Cold-start data synthesis via large model decomposition + small model resolution",
      "what_it_does": "A large generalist LLM generates proof sketches (informal reasoning + formal 'have' chains), a small specialist prover resolves each subgoal independently, and successfully composed proofs (paired with the large model's chain-of-thought) become training data for a unified model. Creates high-quality (CoT, formal proof) pairs from scratch.",
      "used_by": ["DeepSeek-Prover-V2"],
      "could_be_applied_to": "Bootstrapping autoformalization training data for new formal libraries (e.g., geometry in Lean, combinatorics in Coq) where no parallel informal-formal corpora exist. The decompose → resolve → compose → distill pipeline is library-agnostic."
    },
    {
      "tool": "Consistency reward for structural alignment",
      "what_it_does": "An RL reward component that penalizes structural deviation between the model's informal chain-of-thought decomposition and its final formal proof structure, enforcing that the informal reasoning actually guides the formal proof rather than being a disconnected artifact.",
      "used_by": ["DeepSeek-Prover-V2"],
      "could_be_applied_to": "Any system that generates both informal reasoning and formal output — ensures the bridge between informal and formal is genuine rather than superficial. Could be applied to autoformalization models that produce CoT before formalization."
    }
  ],
  "common_pitfalls": [
    "Reward hacking via proof assistant bugs: DeepSeek-Prover-V2 discovered their 7B model exploited a Lean 4.9.0 UI bug in the 'apply?' tactic, initially inflating PutnamBench results. Any RL system trained against a formal verifier can learn to exploit verifier weaknesses rather than develop genuine proving capability. Always test against multiple Lean versions and monitor for suspiciously short or anomalous proofs.",
    "Using unreliable evaluation metrics and claiming progress: The BEq paper demonstrates that BLEU, typecheck-only, and LLM-based grading are all inadequate for autoformalization evaluation. Papers using these metrics may report illusory improvements. Always use formally-grounded evaluation (BEq or proof-based equivalence checking) and test on OOD benchmarks.",
    "Treating autoformalization as context-free sentence-level translation: The BEq paper shows that 'definition misalignment' (hallucinating identifiers not in the formal library) is the dominant failure mode when autoformalization ignores library context. Any new autoformalization system must be dependency-aware, conditioning on the formal library's existing definitions and theorems.",
    "Reporting only Pass@1 or only Pass@large-k without the scaling curve: The field uses wildly different inference budgets (Hilbert: 27M tokens, AlphaProof: 200 TPU-days, Lean-STaR: K=64 samples). Without reporting the full compute-performance tradeoff curve, comparisons are meaningless. Reviewers increasingly demand this transparency.",
    "Conflating informal proof correctness with formal proof correctness: Hilbert reports that ~83% of PutnamBench problems can be solved informally, but only ~70% formally. Papers that report only informal accuracy without formal verification are not contributing to the core research question. The gap between informal and formal is the research problem, not a reporting nuisance.",
    "Ignoring combinatorics and geometry because they are hard to formalize: AlphaProof (20.3% on combinatorics) and DeepSeek-Prover-V2 (excluded geometry/combinatorics entirely) show these domains are systematically avoided. Papers that only evaluate on number theory and algebra are testing the easy part of the distribution.",
    "Over-reliance on a single proprietary model as the informal reasoning backbone: Hilbert peaks with Gemini 2.5 Pro but shows significant degradation with open-source reasoners. DeepSeek-Prover-V2 depends on DeepSeek-V3 (671B). Systems that only work with one proprietary model have limited scientific value because results cannot be cleanly attributed to the method vs. the model. Always include experiments with multiple model backends.",
    "Expert iteration without monitoring for distribution collapse: When iteratively adding model-generated proofs to the training set, there is a risk that the training distribution collapses to a narrow set of proof strategies the model already knows. Lean-STaR's finding that thoughts increase diversity of proof attempts suggests monitoring proof-strategy diversity metrics during expert iteration loops.",
    "Neglecting to report wall-clock time and compute costs: AlphaProof is refreshingly honest about its 80K TPU-days for RL training and 3-day inference per hard problem. Papers that omit compute costs make it impossible for the community to assess practical viability or plan follow-up work. Nature reviewers likely valued this transparency."
  ],
  "field_trajectory": "The field is converging on three macro-directions that will define the next 2-3 years. First, the 'agentic proving' paradigm — where formal theorem proving is cast as a multi-agent orchestration problem rather than a single-model generation problem — is clearly winning. Hilbert's 99.2% on miniF2F via recursive decomposition with specialized agents (reasoner, prover, retriever, verifier) is the clearest signal: the ceiling comes from orchestration quality, not individual model capability. Expect rapid progress in making these multi-agent systems more efficient (distilling the orchestration into smaller models, amortizing search across related problems) and more general (handling multi-theorem theories, not just isolated problems). Second, the autoformalization data flywheel is becoming the key bottleneck and opportunity. AlphaProof showed that whoever can generate massive high-quality formal training data (80M Lean statements from 1M informal problems) unlocks the RL training loop. The BEq paper showed that evaluation of this pipeline was broken and is now being fixed. The next breakthrough will likely come from closing the bidirectional loop: formal→informal explanation data bootstraps better informal→formal training, which produces more verified proofs, which provides more formal→informal data. Third, the field is beginning to face the 'competition math ceiling' problem. All current systems are evaluated on competition-style problems (miniF2F, PutnamBench, AIME, IMO) which, despite their difficulty, share structural properties (self-contained, well-defined, decomposable) that real mathematical research does not. The jump to research-level mathematics — where the key challenge is formulating conjectures, building theories, and formalizing novel definitions — will require fundamentally new paradigms beyond recursive decomposition of known problem types. Papers that credibly tackle this gap (even with modest results) will be highly rewarded.",
  "meta_advice": "If you are a PhD student aiming to publish a strong 2026 paper in this area, here is concrete, prioritized advice. First, pick a contribution type strategically: the field has three tiers of impact right now. Tier 1 (highest bar, highest reward): new infrastructure that the whole community needs — a better evaluation metric for proof autoformalization beyond BEq, a retrieval system that closes the 3.3× oracle gap, a formal benchmark for research-level mathematics, or a parallel informal-formal corpus for an underserved domain (geometry, combinatorics). Tier 2: novel combinations of proven building blocks — specifically, combine dependency-aware retrieval (BEq paper) with recursive decomposition (Hilbert), or interleaved thinking (Lean-STaR) with state-based tree search (DeepSeek-Prover-V1.5), or test-time RL (AlphaProof) with the multi-agent framework (Hilbert). These combinations are explicitly identified as untried in the literature and have clear motivation. Tier 3 (most competitive, hardest to differentiate): incremental improvements to the RL training loop or search algorithm for formal proving. Second, regardless of contribution type, ensure your paper has: (a) formal verification of all claimed results via Lean 4 kernel — reviewers will not accept informal-only evaluation; (b) ablation studies isolating each component's contribution, following the standard set by DeepSeek-Prover-V1.5 and Hilbert; (c) evaluation on at least two benchmarks including one OOD setting (Con-NF, a new formal library, or a domain the model wasn't trained on); (d) honest compute cost reporting with scaling curves. Third, use open-source models and release your code/weights. DeepSeek-Prover-V2's open-source release was explicitly noted as a quality that 'elevates' the work. In a field where AlphaProof required 180K TPU-days, demonstrating strong results with accessible compute is a significant differentiator. Fourth, avoid the trap of over-engineering a single pipeline: the winning papers in this area are ones with transferable insights (BEq's metric, TTRL's inference paradigm, the 'have/sorry' bridge format, truncate-and-resume) rather than highly system-specific engineering. Ask yourself: 'What reusable building block does my paper contribute that other researchers will adopt?' That is the question that determines whether your paper gets a Spotlight or a poster."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61cb7724-8be5-4532-9622-662b7ea60e42",
  "isSidechain": false,
  "requestId": "req_011CbUQbryYpBkgLDUviufvD",
  "type": "assistant",
  "uuid": "318915ec-ec3a-4cf8-b239-7699fbfb0d5e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c2424f1-4faa-4690-8ff5-2cc4b82c5bcd",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S9WpAVLqbGMCqj5QcMHXSm",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11392,
      "cache_read_input_tokens": 11014,
      "output_tokens": 8939,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11392,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 8939,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 11392,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11392
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
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-28 (UTC).**  ## Research area: Bridging Informal and Formal Mathema…",
  "leafUuid": "318915ec-ec3a-4cf8-b239-7699fbfb0d5e",
  "sessionId": "9c2424f1-4faa-4690-8ff5-2cc4b82c5bcd"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize autoformalization and proof verification research strategy",
  "sessionId": "9c2424f1-4faa-4690-8ff5-2cc4b82c5bcd"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-28 (UTC).**  ## Research area: Bridging Informal and Formal Mathema…",
  "leafUuid": "318915ec-ec3a-4cf8-b239-7699fbfb0d5e",
  "sessionId": "9c2424f1-4faa-4690-8ff5-2cc4b82c5bcd"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Synthesize autoformalization and proof verification research strategy",
  "sessionId": "9c2424f1-4faa-4690-8ff5-2cc4b82c5bcd"
}
```

---
