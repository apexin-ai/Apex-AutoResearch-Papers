# Research conversation: You are a senior ML research advisor synthesizing a literature review into an actionable research strategy. **Today's da

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/7cded7ed-6407-48ab-84e6-3517a2852229.jsonl`
- **Structured JSON:** [`03997fa717b752fa4d72.json`](../../sessions/03/03997fa717b752fa4d72.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T08:50:57.178Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T08:50:57.178Z",
  "sessionId": "7cded7ed-6407-48ab-84e6-3517a2852229",
  "content": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.\n\n**Today's date: 2026-05-29 (UTC).**\n\n## Research area: Target: AAAI 2026 (or AAAI 2027 if deadline has passed)\nTrack: Knowledge Representation and Reasoning / Safe and Robust AI\n\nDirection: Build a hybrid PRM that learns to route each reasoning step to either a formal verifier (Z3/Lean 4) or a neural verifier (GenPRM-style) based on a learned formalizability score, then apply this routing framework specifically to detect miracle steps — unjustified logical leaps where the conclusion is correct but not derivable from preceding steps. The formal verifier provides binary derivability judgments for formalizable steps while the neural verifier handles non-formalizable steps, with the router trained on FoVer-style formally verified data as ground truth.\n\nSeed Papers:\n- FoVer (Kamoi et al., ACL 2026 Findings / ICLR 2026) — provides the formal verification infrastructure (Z3 + Isabelle) for PRM training data synthesis; our direct foundation\n- Curing Miracle Steps with Rubric Rewards (Yuan et al., 2025) — taxonomizes the miracle step problem and proposes RRM; our work replaces neural rubrics with formal derivability\n- ARES (You & Xue, EMNLP 2025) — checks step entailment from predecessors probabilistically; our key differentiator is using formal (not neural) derivability checking\n- PRoSFI (2026, under review ICLR 2026) — uses formal intermediaries for process rewards; doesn't route between formal/neural or target miracle steps specifically\n- Safe (ACL 2025) — Lean 4 step-level verification; provides formalization pipeline but doesn't train PRMs or detect miracle steps\n- GenPRM (Liu et al., AAAI 2026) — SOTA generative neural PRM; serves as our neural verifier baseline\n- Typed Chain-of-Thought (ICLR 2026 submission) — Curry-Howard framework for reasoning verification; provides theoretical motivation for our type-checking-as-derivability angle\n\nKnown Gaps:\n- No existing system routes between formal and neural verifiers per step based on a learned formalizability classifier — all current approaches are formal-only or neural-only\n- No work applies formal proof-assistant derivability checking to detect miracle steps — ARES checks entailment neurally, RRM uses neural rubrics, but formal derivability from predecessors is untested\n- The formalizability spectrum (fully formalizable → partially → not at all) has not been characterized or exploited for PRM design\n\nTheoretical Anchor: A reasoning step S_i is justified iff S_i is formally derivable from {S_1, ..., S_{i-1}} ∪ {problem statement} under known inference rules. Steps where formal derivation fails or times out are miracle-step candidates. The formalizability score (proportion of a step's sub-claims that can be expressed in SMT/HOL) determines router behavior. This connects PRMs to classical proof theory: reward = derivability.\n\nConstraints:\n- Compute: ≤200 H100-hours (router ~10h, PRM fine-tuning at 7B ~50h, formal verification CPU-bound, evaluation ~40h)\n- Must clearly differentiate from FoVer (training-only formal), PRoSFI (no routing), ARES (neural-only entailment), and Safe (no PRM training)\n- Target 7B scale for academic tractability\n- Use FoVer's public codebase and data as starting infrastructure\n\nQuality Self-Checks:\n- [x] Core insight: A PRM that knows which steps it can formally verify and which it must judge neurally will catch miracle steps that pure neural PRMs miss.\n- [x] Why not obvious: Routing requires solving the meta-problem of formalizability classification, which no one has tackled because formal and neural verification communities don't overlap. PRoSFI and Safe avoid routing by requiring ALL steps to be formalizable.\n- [x] Baseline fear test: A simple baseline (run Z3 on every step, fall back to neural on timeout) would get ~60% of the routing benefit — the learned router must demonstrably outperform this naive fallback on partial-formalizability cases.\n- [x] Information exploited: The formalizability structure of each step — specifically which sub-claims are expressible in SMT logic and which require informal reasoning — is information that no existing PRM uses.\n\nAvoid:\n- Training only on formally verifiable data (that's FoVer — must show value of the hybrid approach on non-formalizable steps)\n- Claiming formal verification solves everything (formalization success rate will be 40-60% — must be honest about coverage limits and show the neural fallback is essential)\n- Evaluating only on math (AAAI values generality — include code via LiveCodeBench and science via GPQA)\n- Ignoring the ARES comparison (must show formal derivability checking outperforms neural entailment checking on miracle step detection)\n\n## Paper analyses (20 papers)\n\n[\n  {\n    \"title\": \"FoVer: Efficient PRM Training Data Synthesis via Formal Verification\",\n    \"venue\": \"ACL 2026 Findings (withdrawn from ICLR 2026)\",\n    \"problem_identification\": \"PRM training data is expensive: human annotation suffers ~30% discard rates from low inter-annotator agreement, while Monte Carlo rollout methods (Math-Shepherd) require 8×#steps LLM calls per solution and produce noisy labels. The gap is the absence of a cheap, deterministic, accurate step-level label source.\",\n    \"key_insight\": \"Formal verification tools (Z3 for propositional logic, Isabelle/HOL for theorem proving) can serve as zero-cost, deterministic oracles for step-level correctness labels—and surprisingly, PRMs trained only on formal-domain data generalize to informal NL reasoning tasks.\",\n    \"innovation_type\": \"cross_domain\",\n    \"method_summary\": \"FoVer generates step-by-step solutions with base LLMs (7-8B), converts informal math reasoning to Isabelle proofs via a 70B translator, then verifies each step independently—Z3 checks satisfiability of negated conclusions in CNF; Isabelle uses 'sorry' isolation to check individual proof steps. This produces FoVer-40K (20K logic + 20K theorem proving steps, 50% error rate), which fine-tunes PRMs via binary cross-entropy on 'correct'/'incorrect' token prediction. The key technical trick for Isabelle is assuming other steps correct when evaluating a target step, enabling isolated per-step verification.\",\n    \"limitations_and_open_questions\": \"Coverage limited to formalizable domains (~40-60% of real reasoning); Isabelle dataset generation took weeks on multiple servers. Open question: can the formal-to-informal transfer be improved by mixing formal and neural verification signals rather than using formal data alone?\",\n    \"building_blocks\": [\n      \"Z3 step-level satisfiability checking via CNF negation\",\n      \"Isabelle sorry-based step isolation\",\n      \"FoVer-40K dataset with binary step labels\",\n      \"Informal-to-formal conversion pipeline (70B few-shot)\",\n      \"Cross-entropy PRM fine-tuning on verification tokens\",\n      \"Public codebase and data\"\n    ],\n    \"relevance_to_seed\": \"Direct foundation—provides the formal verification infrastructure, public data, and cross-domain generalization evidence that the hybrid router builds upon; the key limitation (formal-only coverage) is exactly what the neural fallback addresses.\"\n  },\n  {\n    \"title\": \"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification\",\n    \"venue\": \"ACL 2025\",\n    \"problem_identification\": \"PRMs and self-consistency methods are opaque—they score steps without providing checkable evidence. The gap: no system translates each NL reasoning step into formal Lean 4 statements for machine-verified correctness proofs, which would provide interpretable, binary ground truth.\",\n    \"key_insight\": \"Step-level formalization difficulty is much lower than whole-problem formalization, making automated theorem proving feasible within small compute budgets (16 proof attempts per step), and retrospective formal verification is complementary to prospective PRM scoring.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"Safe decomposes CoT traces into discrete steps (heuristic or LLM-based), auto-formalizes each into Lean 4 theorem statements via few-shot prompting with syntax validation through Lean REPL, then runs ATPs (COPRA, DeepSeek-Prover-V1.5) to prove or fail each statement. Steps receive one of four states: no-verification-needed, failed-formalization, proved, unprovable. A tiny 2-layer LSTM (hidden=64) aggregates state sequences into a retrospective score, which combines with prospective PRM scores via weighted geometric mean (score = retro^α × pro^(1-α)). FormalStep benchmark: 30,809 formal statements from 500 MATH problems across 5 domains.\",\n    \"limitations_and_open_questions\": \"Lean 4 struggles with geometry and combinatorics; auto-formalization and ATP are both fallible, injecting noise. No routing mechanism exists to decide when formalization is worth attempting. Does the 4-state LSTM capture enough signal, or would richer features (partial proof progress, formalization confidence) help?\",\n    \"building_blocks\": [\n      \"Lean 4 auto-formalization pipeline with REPL validation\",\n      \"4-state step verification taxonomy\",\n      \"LSTM retrospective scorer\",\n      \"Geometric mean score ensembling\",\n      \"FormalStep benchmark (30K+ statements)\"\n    ],\n    \"relevance_to_seed\": \"Provides the Lean 4 formalization pipeline and the retrospective/prospective complementarity insight; the 4-state taxonomy (especially failed-formalization vs. unprovable) directly informs the formalizability classifier design in the proposed router.\"\n  },\n  {\n    \"title\": \"Typed Chain-of-Thought: A Curry-Howard Framework for Verifying LLM Reasoning\",\n    \"venue\": \"arXiv 2025 (ICLR 2026 submission, withdrawn)\",\n    \"problem_identification\": \"CoT verification methods are either post-hoc and heuristic (self-consistency, PRMs) or require full formal proof construction. The gap: no framework provides lightweight, during-generation formal certificates for CoT faithfulness without requiring a separate proof assistant.\",\n    \"key_insight\": \"Under Curry-Howard correspondence, a faithful CoT trace is a well-typed program—so type-checking (much cheaper than theorem proving) suffices to certify reasoning faithfulness, and ill-typed traces can be filtered before answer aggregation.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"PC-CoT (Proof-Carrying CoT) operates in three stages: (1) the LLM emits structured JSON with typed annotations (premises, operations, answers using a type system of ℕ⊆ℤ⊆ℚ plus unit/dimensional types), (2) a Typed Reasoning Graph (bipartite multigraph of statement and rule nodes) is constructed to track dataflow, (3) certification metrics (Coverage, EVR, UVR, Path Existence, Min Path Score) gate which traces aggregate into final answers. Two gates are offered: relaxed (70.4% acceptance, 87.2% precision) and strict (56.3% acceptance, 91.6% precision). Classification of steps to rule schemas uses regex heuristics with fallback.\",\n    \"limitations_and_open_questions\": \"Type system is narrow (numeric/unit types only)—cannot handle logical quantifiers, set theory, or complex mathematical structures. Regex-based rule classification is brittle. The paper was withdrawn from ICLR 2026, suggesting reviewer concerns. Can this type-checking framework scale beyond arithmetic to richer mathematical reasoning?\",\n    \"building_blocks\": [\n      \"Curry-Howard framing of CoT-as-typed-program\",\n      \"Typed Reasoning Graph representation\",\n      \"5 certification metrics (Coverage, EVR, UVR, PE, MPS)\",\n      \"Certified self-consistency filtering\",\n      \"Configurable strictness gates\"\n    ],\n    \"relevance_to_seed\": \"Provides theoretical motivation for the derivability-as-reward formulation—the Curry-Howard framing justifies treating type-checking/proof-checking as a verification signal; the narrow type system illustrates why a neural fallback is needed for steps outside the formalizable fragment.\"\n  },\n  {\n    \"title\": \"VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks\",\n    \"venue\": \"arXiv 2025 (under review)\",\n    \"problem_identification\": \"LLMs can reach correct answers through flawed reasoning, and neither neural verifiers nor self-consistency can reliably detect logical invalidity in intermediate steps. The gap: no system formalizes CoT steps into machine-checkable FOL with explicit premise tracking to enable automated derivability verification.\",\n    \"key_insight\": \"By decomposing verification into (1) autoformalization into FOL/SMT-LIB, (2) explicit premise identification with source categorization (context/commonsense/inference), and (3) Z3 entailment checking, you get both symbolic validity verification AND human-interpretable explanations of why steps fail.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"VeriCoT's pipeline: an LLM translates each CoT step into SMT-LIB format (up to 3 attempts with vocabulary extension via declare-fun/declare-sort), then identifies premises categorized as context-grounded, commonsense, or inference-based. Z3 checks three properties per step: entailment (ℱ_{i-1} ⊨ F_i), contradiction (ℱ_{i-1} ⊨ ¬F_i), and consistency. Steps are classified as valid, ungrounded, contradictory, or untranslatable. The verification signal feeds three downstream applications: inference-time self-reflection, SFT on VeriCoT-distilled data, and DPO with verification-based pairwise rewards. Evaluated on ProofWriter, LegalBench-SARA, and BioASQ.\",\n    \"limitations_and_open_questions\": \"Limited to FOL fragment with linear arithmetic and uninterpreted functions—many mathematical steps require higher-order logic. The 3-attempt autoformalization has unknown success rate on complex math. No learned routing to decide when formalization is worthwhile. How does VeriCoT's entailment checking compare to ARES's neural entailment on miracle step detection?\",\n    \"building_blocks\": [\n      \"SMT-LIB autoformalization with iterative vocabulary extension\",\n      \"3-category premise identification (context/commonsense/inference)\",\n      \"Z3 entailment/contradiction/consistency triple-check\",\n      \"Verification-as-reward for DPO training\",\n      \"4-class step classification (valid/ungrounded/contradictory/untranslatable)\"\n    ],\n    \"relevance_to_seed\": \"Most directly relevant existing system to the formal verification component—VeriCoT's Z3 entailment checking (ℱ_{i-1} ⊨ F_i) is essentially formal derivability checking for miracle steps. The proposed router extends this by learning when to invoke formal vs. neural verification, and VeriCoT's 'untranslatable' category directly motivates the formalizability classifier.\"\n  },\n  {\n    \"title\": \"Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations\",\n    \"venue\": \"ACL 2024\",\n    \"problem_identification\": \"Process reward models require expensive human step-level annotations (PRM800K cost ~$500K+). Outcome reward models ignore intermediate reasoning quality. The gap: no automatic method existed to construct step-level supervision data for PRM training at scale.\",\n    \"key_insight\": \"A step's correctness can be approximated by its potential to reach the correct final answer—if any completion from step i reaches the gold answer, step i is likely correct. This reframes step verification as a reachability problem solvable by Monte Carlo sampling.\",\n    \"innovation_type\": \"simplification\",\n    \"method_summary\": \"A completer model (LLemma-7B fine-tuned on target data) generates N=8 continuations from each intermediate step. Hard estimation assigns binary labels (1 if any completion is correct, 0 otherwise; 86% accuracy at N=4). Soft estimation uses completion success frequency as a continuous label. The PRM scores solutions by taking the minimum step score across all steps. For RL, step-by-step PPO delivers rewards at each reasoning step rather than only at sequence end. Results: Mistral-7B accuracy 77.9%→84.1% (GSM8K) and 28.6%→33.0% (MATH) with PPO; 89.1% and 43.5% with verification reranking.\",\n    \"limitations_and_open_questions\": \"Labels are noisy—a step can be wrong yet still lead to the correct answer by lucky cancellation, and correct steps may fail to reach the answer due to completer weakness. The method requires 8×#steps LLM forward passes per solution. Can formal verification replace Monte Carlo sampling to get deterministic, noise-free step labels (this is exactly what FoVer does)?\",\n    \"building_blocks\": [\n      \"Monte Carlo completion-based step labeling\",\n      \"Hard/soft estimation for step correctness\",\n      \"Min-score solution ranking\",\n      \"Step-level PPO with per-step rewards\",\n      \"Automatic PRM training pipeline without human annotation\"\n    ],\n    \"relevance_to_seed\": \"Foundational method that FoVer and the proposed work build upon—Math-Shepherd established the paradigm of automatic step-level supervision for PRM training. Its key limitation (noisy labels from Monte Carlo approximation) is precisely what formal verification addresses, and its min-score ranking is the evaluation protocol the proposed hybrid PRM must beat.\"\n  },\n  {\n    \"title\": \"Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards\",\n    \"venue\": \"ACL 2026 Main\",\n    \"problem_identification\": \"Through systematic human verification of LLM math solutions, the authors discovered that correct final answers frequently mask logically invalid reasoning — 'miracle steps' where models jump to correct outputs without valid derivation. They taxonomized six false-positive categories (inductive overgeneralization, outcome irrelevance, neglected preconditions, unverified assumptions, numerical coincidence, miracle steps) that existing PRMs fail to catch.\",\n    \"key_insight\": \"Problem-specific rubrics that encode targeted evaluation criteria against known failure modes detect reasoning flaws that outcome-based and step-level process rewards systematically miss.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Three-phase pipeline: (1) Gemini-2.5-Pro synthesizes problem-specific rubrics grounded in structure-based scaffolding and method-agnostic fairness; (2) scoring data is synthesized by evaluating candidate responses against rubrics on a 0-10 scale; (3) Qwen3-4B is fine-tuned via SFT then PPO to predict rubric-aligned quality scores. The RRM receives (question, rubric, response) triples and outputs integer scores normalized to [0,1] as RL training rewards, achieving F1=0.693 (+0.312 over PRM baselines) and reducing miracle steps by 71%.\",\n    \"limitations_and_open_questions\": \"Rubrics are neurally generated (Gemini-2.5-Pro dependency) — no formal guarantee that rubric criteria are complete or sound. The approach doesn't verify logical derivability between steps; it evaluates against heuristic criteria, leaving room for formally grounded alternatives.\",\n    \"building_blocks\": [\n      \"Miracle step taxonomy (6 false-positive categories)\",\n      \"Rubric synthesis pipeline\",\n      \"RRM training recipe (SFT+PPO on rubric scores)\",\n      \"False positive detection benchmarks on AIME2024\"\n    ],\n    \"relevance_to_seed\": \"Defines and taxonomizes the exact problem (miracle steps) our formal-derivability router targets; RRM's 71% reduction is the neural baseline our hybrid approach must surpass by adding formal derivability checking.\"\n  },\n  {\n    \"title\": \"Process Reward Models That Think (ThinkPRM)\",\n    \"venue\": \"arXiv 2025 (Google DeepMind); withdrawn from ICLR 2026\",\n    \"problem_identification\": \"Discriminative PRMs require hundreds of thousands of human-labeled step annotations (PRM800K) yet remain brittle out-of-domain. The authors observed that long-CoT reasoning models already possess latent verification capabilities that can be elicited through generation rather than classification.\",\n    \"key_insight\": \"Recasting process verification as generative chain-of-thought reasoning — rather than discriminative classification — achieves superior data efficiency (100x fewer labels) and enables test-time compute scaling of the verifier itself.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"ThinkPRM fine-tunes reasoning models (R1-Distill-Qwen 1.5B–14B) on ~1K synthetic verification CoTs sampled from QwQ-32B-Preview and filtered against 8K gold process labels from PRM800K. At inference, the model generates verification reasoning up to 8K tokens, then scores via P('yes')/(P('yes')+P('no')) on a forced 'Is the solution correct?' query. Verification compute scales in two axes: parallel (K independent CoTs averaged) and sequential (longer thinking budgets), with stable improvements up to 24K tokens unlike LLM-as-a-Judge which degrades.\",\n    \"limitations_and_open_questions\": \"Withdrawn from ICLR 2026 — unknown review concerns. Verification remains purely neural with no formal grounding; generated critiques may themselves contain reasoning errors. Filtering against gold labels creates a ceiling tied to PRM800K quality.\",\n    \"building_blocks\": [\n      \"Generative verification CoT paradigm\",\n      \"Data-efficient PRM training recipe (1K examples)\",\n      \"Parallel/sequential verifier compute scaling\",\n      \"OOD evaluation protocol (GPQA-Diamond, LiveCodeBench)\"\n    ],\n    \"relevance_to_seed\": \"Strongest neural PRM baseline and natural candidate for the neural verifier component in our hybrid router; its OOD generalization to GPQA/LiveCodeBench validates the evaluation domains we target, and its test-time scaling mechanism could complement formal verification routing.\"\n  },\n  {\n    \"title\": \"Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Model Parameters\",\n    \"venue\": \"ICLR 2025 Oral\",\n    \"problem_identification\": \"Prior work showed test-time compute scaling existed but provided mostly negative results about its efficiency. The authors identified that uniform compute allocation across questions of varying difficulty is fundamentally wasteful — easy questions need little compute while hard questions may not benefit regardless.\",\n    \"key_insight\": \"Difficulty-adaptive compute allocation — choosing between search (PRM-guided) and revision strategies per question based on estimated difficulty — yields 4x efficiency gains over uniform best-of-N, making smaller models competitive with 14x larger ones.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"The paper systematically compares PRM-guided search (best-of-N weighted, beam search, lookahead) against revision-based distribution updates across difficulty bins. PRMs are trained via Monte Carlo rollouts with binary cross-entropy, using last-step predictions as full-answer scores. Questions are binned into 5 difficulty levels using PRM-estimated pass@1 rates, and optimal strategy per bin is selected via two-fold cross-validation. Key finding: beam search excels on medium-difficulty but degrades on easy problems due to PRM exploitation (repetitive low-information steps); revision outperforms parallel sampling sequentially but requires balanced parallel-sequential ratios for hard problems.\",\n    \"limitations_and_open_questions\": \"Evaluated only on MATH with PaLM 2-S*; PRM exploitation in beam search reveals verifier fragility that better verifiers (formal+neural) could mitigate. Hardest problems show minimal improvement from any strategy, suggesting a ceiling on test-time scaling without better base models.\",\n    \"building_blocks\": [\n      \"Compute-optimal test-time scaling framework\",\n      \"Difficulty-adaptive strategy selection\",\n      \"PRM exploitation analysis\",\n      \"FLOPs-matched comparison methodology\"\n    ],\n    \"relevance_to_seed\": \"Foundational motivation: better verifiers directly amplify test-time scaling efficiency. Our hybrid formal+neural PRM should reduce the PRM exploitation problem (formal verifiers are harder to game) and extend the difficulty range where test-time compute helps.\"\n  },\n  {\n    \"title\": \"Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification\",\n    \"venue\": \"arXiv 2026\",\n    \"problem_identification\": \"Existing neuro-symbolic approaches apply formal verification post-hoc (filtering completed solutions), missing the opportunity to prevent error propagation during reasoning. The authors identified that real-time formal feedback during generation — not just after — could correct errors as they arise.\",\n    \"key_insight\": \"Interleaving formal symbolic verification as inline feedback during chain-of-thought generation, with hierarchical penalties for verification failures, prevents error cascading rather than merely filtering post-hoc.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"Each reasoning step is augmented with a formal specification and verification result triple (sᵢ, fᵢ, vᵢ). A two-stage pipeline: (1) SFT on synthesized data containing natural language + formal code blocks + interpreter outputs, validated through exact matching, semantic equivalence, and proof rewriting; (2) GRPO with hierarchical rewards — fatal execution failures (-8.0), format violations (-6.0), structural penalties for undefined tags/excess tool calls. Verification uses Python/Z3 execution in sandboxes. At 7B/14B scale, achieves 10.4%/14.2% gains across six reasoning benchmarks.\",\n    \"limitations_and_open_questions\": \"Uses execution-based validation (Python/Z3) rather than proof-based (Lean/Isabelle), limiting formal guarantees. No routing mechanism — all steps attempt formalization. Coverage/success rate of formal verification per step is not reported, making it unclear how often the formal signal actually helps versus adds noise.\",\n    \"building_blocks\": [\n      \"Interleaved verification architecture (s,f,v triples)\",\n      \"Hierarchical reward design for formal feedback\",\n      \"Two-stage SFT+GRPO pipeline at 7B/14B\",\n      \"Real-time formal verification during generation\"\n    ],\n    \"relevance_to_seed\": \"Demonstrates feasibility of integrating formal verification into the reasoning loop at 7B scale, validating our compute assumptions. Key differentiator: they attempt to formalize every step (no routing), while we route based on formalizability — their coverage gaps motivate our neural fallback.\"\n  },\n  {\n    \"title\": \"Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning\",\n    \"venue\": \"arXiv 2026\",\n    \"problem_identification\": \"The authors identified a critical reliability cliff: Lean-based formal verification is 96% accurate at high proved coverage but drops to 20% at low coverage, yet no prior work quantified when formal signals can be trusted. They further discovered that 7B autoformalizers achieve only 28% coverage with merely 43% proof faithfulness — autoformalization, not proof search, is the bottleneck (zero timeouts observed).\",\n    \"key_insight\": \"Formal verification's value is coverage-dependent with a sharp reliability cliff — risk-controlled abstention with calibrated coverage thresholds transforms an unreliable partial signal into a high-precision selective judge.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"CovCal uses three Lean diagnostic metrics: typed coverage (fraction reaching well-formed Lean), proved coverage (fraction with formal proofs), and formal margin (proved vs. unresolved rival weight). Acceptance requires all three exceeding calibrated thresholds simultaneously. Thresholds are selected from a 125-cell grid under two regimes: conservative Bonferroni bounds (α=δ/125) which often reject-all at low coverage, or development-then-calibration which preselects one threshold on a dev split then certifies on calibration data. Prover-specialized Goedel-Prover-V2-8B achieves 79% coverage (vs. 28% for general 7B), enabling Bonferroni certification on 17/20 bootstrap partitions.\",\n    \"limitations_and_open_questions\": \"Manual faithfulness audit covers only 45 examples with a single annotator. The 28% coverage figure is specific to Qwen2.5-Coder-7B — better formalizers could shift the entire coverage-reliability curve. No step-level analysis; all results are problem-level answer verification rather than intermediate step checking.\",\n    \"building_blocks\": [\n      \"Coverage-reliability cliff quantification (96% → 20%)\",\n      \"CovCal risk-controlled selection mechanism\",\n      \"Proof faithfulness taxonomy (genuine/trivial/structural/spurious)\",\n      \"Autoformalization bottleneck analysis\",\n      \"Coverage diagnostic metrics (C_typ, C_prf, M)\"\n    ],\n    \"relevance_to_seed\": \"Directly validates our hybrid design's core premise: 7B formalization covers only 28% of problems with 43% faithfulness, proving a neural fallback is essential. The coverage-reliability cliff (96% at high, 20% at low coverage) is exactly the signal our formalizability router must learn to exploit — route to formal verification only when coverage is sufficient for reliable judgments.\"\n  },\n  {\n    \"title\": \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\",\n    \"venue\": \"AAAI 2026\",\n    \"problem_identification\": \"Existing PRMs are discriminative scalar predictors that cannot leverage LLM generative capabilities or scale test-time compute. The authors identified that process supervision labels are noisy and verification reasoning is opaque, creating both a data quality and an inference scalability gap.\",\n    \"key_insight\": \"Process reward modeling should be reformulated as a generative task where the PRM produces explicit CoT reasoning with executable code verification before judging each step, enabling test-time scaling via majority voting over multiple verification trajectories.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"GenPRM introduces Relative Progress Estimation (RPE): P_t = (MC(s_t) - MC(s_{t+1})) / MC(s_1), comparing Monte Carlo pass-rate changes between consecutive states to obtain soft step-level labels. A rationale synthesis pipeline uses QwQ-32B to generate CoT reasoning in &lt;analyze> tags plus executable Python code in &lt;verify> tags; code execution results feed back into the generative process. At inference, N verification paths are sampled and majority-voted, enabling test-time compute scaling. Trained on only 23K MATH examples, GenPRM-1.5B outperforms GPT-4o and GenPRM-7B surpasses Qwen2.5-Math-PRM-72B on ProcessBench.\",\n    \"limitations_and_open_questions\": \"RPE still relies on MC sampling which is expensive; code verification only works for computationally checkable claims, leaving non-executable reasoning steps judged purely by CoT. Evaluation is math-centric with unclear generalization to non-mathematical domains.\",\n    \"building_blocks\": [\n      \"Generative PRM architecture with &lt;analyze>/&lt;verify> tags\",\n      \"RPE labeling method\",\n      \"Test-time majority voting for PRMs\",\n      \"23K MATH training data\"\n    ],\n    \"relevance_to_seed\": \"GenPRM serves as the neural verifier component in our hybrid router — its generative architecture handles non-formalizable steps while our formal verifier handles formalizable ones, and our router must outperform GenPRM-alone on miracle step detection.\"\n  },\n  {\n    \"title\": \"Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries (PRoSFI)\",\n    \"venue\": \"arXiv 2026 (under review)\",\n    \"problem_identification\": \"Outcome rewards overlook flawed intermediate steps even when final answers are correct, but direct formal proof generation is beyond 7B models' capabilities. The authors identified this gap between the aspiration for formal verification and practical model capability.\",\n    \"key_insight\": \"Instead of demanding complete formal proofs, models can output structured formal intermediaries — lightweight JSON blocks with formal conclusions in Lean4 syntax and explicit dependency/rule fields — that are individually verifiable by automated provers without requiring end-to-end proof synthesis.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"Each reasoning step outputs a structured block containing an id, dependencies (max 4), a formal conclusion in Lean4 syntax, and the inference rule applied. Formal propositions are extracted and verified independently using Lean4, Z3, or Prover9. Training uses GRPO with a tiered reward: 1.0 for correct answer + all steps verified, 0.3 for correct but unverified steps, 0.1 for format-correct but wrong answer, 0.0 otherwise. On ProverQA-Hard, PRoSFI achieves 76.07% GPT-judged soundness vs 21.97% for outcome-CoT baselines while maintaining 92.97% accuracy. Training takes ~14 hours on 8 Hopper GPUs.\",\n    \"limitations_and_open_questions\": \"Requires ALL steps to be formalizable — no fallback for inherently non-formalizable reasoning. The max-4-dependency constraint and reliance on lightweight tactics (aesop, simp) limit expressiveness. Evaluation is restricted to logic puzzles (ProverQA, Knights & Knaves).\",\n    \"building_blocks\": [\n      \"Structured formal intermediary format (JSON with Lean4 conclusions)\",\n      \"Tiered verification reward function\",\n      \"Multi-prover verification (Lean4/Z3/Prover9)\",\n      \"GRPO training with formal rewards\"\n    ],\n    \"relevance_to_seed\": \"PRoSFI is our primary architectural contrast — it requires all steps to be formalizable while our hybrid router gracefully degrades to neural verification for non-formalizable steps, and PRoSFI doesn't target miracle step detection specifically.\"\n  },\n  {\n    \"title\": \"Let's Verify Step by Step\",\n    \"venue\": \"ICLR 2024\",\n    \"problem_identification\": \"Outcome supervision provides no signal about intermediate reasoning quality, conflating correct final answers with valid reasoning chains. The authors identified that step-level feedback was theoretically motivated but lacked large-scale empirical validation.\",\n    \"key_insight\": \"Process supervision (step-level human labels: positive/negative/neutral) significantly outperforms outcome supervision for training reward models, and active learning that surfaces high-scoring wrong-answer solutions to labelers yields 2.6× data efficiency.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"Human labelers annotated each step as positive, negative, or neutral without reference solutions (only ground-truth final answers). PRM800K contains 800K step-level labels across 75K solutions to 12K MATH problems. The PRM is trained on these labels and used for best-of-N selection over generator outputs. Active learning ranks solutions with the current best PRM and surfaces convincing-but-wrong solutions for labeling, then retrains between generations. The process-supervised PRM achieved 78% on a representative MATH subset, significantly outperforming outcome-supervised equivalents.\",\n    \"limitations_and_open_questions\": \"Labels are human-generated (expensive, subjective — neutral vs positive is ambiguous). The PRM is discriminative and opaque about WHY a step fails. No formal notion of 'correctness' — labels capture human judgment, not logical derivability.\",\n    \"building_blocks\": [\n      \"PRM800K dataset (800K step-level labels)\",\n      \"Process vs outcome supervision framework\",\n      \"Active learning for PRM data collection\",\n      \"Best-of-N evaluation methodology\"\n    ],\n    \"relevance_to_seed\": \"Foundational PRM paper that our work builds upon — we replace expensive human step-level labels with formal derivability judgments from Z3/Lean and neural verification from GenPRM, while PRM800K's annotation protocol informs our evaluation criteria.\"\n  },\n  {\n    \"title\": \"Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models\",\n    \"venue\": \"arXiv 2026\",\n    \"problem_identification\": \"PRMs are increasingly central to LLM reasoning pipelines but have never been stress-tested adversarially. The authors identified the untested assumption that high PRM scores indicate genuine reasoning quality.\",\n    \"key_insight\": \"Current PRMs function as fluency detectors rather than reasoning verifiers — they are invariant to surface-level style changes (|ΔR|<0.1) yet fail inconsistently at detecting logical corruption, and RL policies exploit this by achieving >0.9 PRM reward with <4% actual accuracy.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"A three-tier diagnostic framework: (1) Static perturbation analysis applies semantics-preserving changes (rephrasing, verbosity) and semantics-altering attacks (question shuffling, numerical perturbation, reasoning hallucination) measuring ΔR; (2) Gradient-based adversarial token optimization maximizes reward on flawed AIME trajectories with as few as 1 appended embedding, inflating Skywork-1.5B rewards from 0.237→0.954; (3) RL-induced reward hacking trains Qwen2.5-1.5B via GRPO using PRM feedback, showing reward climbs to >0.9 while accuracy stays <4%, with 43% of gains from stylistic shortcuts (measured via rephrasing intervention on held-out AIME 2025).\",\n    \"limitations_and_open_questions\": \"Tested only Skywork and Qwen PRMs — unclear if findings generalize to generative PRMs like GenPRM. The 43% stylistic attribution method (rephrasing intervention) is approximate. Does not propose solutions beyond diagnostic tooling.\",\n    \"building_blocks\": [\n      \"Three-tier PRM robustness diagnostic framework\",\n      \"PRM-BiasBench benchmark\",\n      \"Gradient-based PRM attack methodology\",\n      \"Stylistic vs content reward decomposition\"\n    ],\n    \"relevance_to_seed\": \"Provides core motivation — formal derivability checking is inherently robust to fluency-based reward hacking since Z3/Lean proofs are immune to stylistic manipulation, directly addressing the 'fluency detector' vulnerability this paper exposes.\"\n  },\n  {\n    \"title\": \"Scaling Test-Time Compute Without Verification or RL is Suboptimal\",\n    \"venue\": \"ICML 2025 (Spotlight)\",\n    \"problem_identification\": \"The relative merits of verification-based (VB: RL + search with rewards) versus verification-free (VF: distillation of correct traces) test-time scaling lacked theoretical grounding. The authors identified that empirical comparisons were confounded by implementation differences.\",\n    \"key_insight\": \"Under heterogeneous solution distributions (high variance in token-level Q-values across paths to the same answer) and anti-concentration (base policy covers above-mean policies with constant probability), VB methods achieve Ω̃(√H) better scaling than any VF method — the gap is structural, not implementational.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"VF methods are formalized as finetuning within a χ²-divergence ball around the base policy using expert traces; VB methods query reward annotations on the policy's own rollouts. The main separation theorem (5.8) proves that with heterogeneous base policies (σ̃_b = Ω(H)) satisfying anti-concentration, VB achieves O(H/n) suboptimality vs VF's Ω(H/√n) — a √H gap when n = Ω(H). Empirically validated on 3B/8B/32B Llama models and the S1 distillation model, showing VB outperforms VF with widening gaps as test-time budget increases. Common pretrained LLMs are shown to empirically satisfy both heterogeneity and anti-concentration conditions.\",\n    \"limitations_and_open_questions\": \"Assumes access to a perfect verifier — the quality of the reward model is not accounted for in the theory. Anti-concentration may not hold for heavily fine-tuned or collapsed policies. The bi-level reward structure (sparse binary) may not capture nuanced step-level verification.\",\n    \"building_blocks\": [\n      \"VB vs VF formal framework\",\n      \"Anti-concentration condition for base policies\",\n      \"Separation theorem for test-time compute scaling\",\n      \"Heterogeneity characterization of LLM solution distributions\"\n    ],\n    \"relevance_to_seed\": \"Provides theoretical justification for investing in better verifiers — our hybrid formal/neural PRM improves verification quality, and this paper proves that better verifiers yield asymptotically better test-time scaling, making the formal derivability router's accuracy improvements compound at inference time.\"\n  },\n  {\n    \"title\": \"Probabilistic Soundness Guarantees in LLM Reasoning Chains (ARES)\",\n    \"venue\": \"EMNLP 2025\",\n    \"problem_identification\": \"Standard sequential error detectors condition on all prior steps including erroneous ones, causing error propagation to corrupt downstream judgments. ARES identifies this as a structural flaw in how premises are consumed during chain evaluation.\",\n    \"key_insight\": \"By marginalizing over exponentially many premise-validity configurations via Monte Carlo sampling, each step's soundness score becomes independent of upstream errors, yielding certified Hoeffding-bound guarantees on per-step soundness estimates.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"ARES defines τ_k = Σ_α E(C(α), C_{n+k}) · Pr[α], averaging NLI entailment scores over all 2^(n+k-1) configurations of premise inclusion/exclusion, weighted by recursively-computed soundness probabilities. Monte Carlo sampling (N iterations) makes this tractable, with Theorem 3.1 guaranteeing |τ̂_k - τ_k| ≤ ε with probability ≥ 1-δ for N ≥ log(2m/δ)/(2ε²). The entailment function is instantiated via LLM prompting (GPT-4o-mini or Qwen3-4B), not formal verification.\",\n    \"limitations_and_open_questions\": \"Entailment is still neural (NLI-based), so it inherits all failure modes of LLM-based logical judgment — it detects propagation artifacts but cannot verify mathematical derivability. The Hoeffding bound gives concentration guarantees on the estimator, not guarantees that the entailment model itself is correct.\",\n    \"building_blocks\": [\n      \"Autoregressive premise-conditioning framework\",\n      \"Monte Carlo premise configuration sampling\",\n      \"Hoeffding-bound certification for step scores\",\n      \"ProcessBench and GSM8K evaluation protocol\"\n    ],\n    \"relevance_to_seed\": \"ARES is the primary neural-entailment baseline our formal derivability checking must outperform; its framework for conditioning on verified premises could be adapted to mix formal and neural entailment signals within our router.\"\n  },\n  {\n    \"title\": \"Verifying Chain-of-Thought Reasoning via Its Computational Graph (CRV)\",\n    \"venue\": \"ICLR 2026 Oral\",\n    \"problem_identification\": \"Black-box and gray-box CoT verification methods predict correctness from outputs or activations but cannot explain why a computation fails. CRV identified that the model's internal computational structure — not just its outputs — encodes verifiable error signatures.\",\n    \"key_insight\": \"Attribution graphs of correct vs. incorrect reasoning steps have distinct structural fingerprints (density, centrality, activation distributions), and these signatures are domain-specific — different reasoning tasks produce different error patterns, implying verification must be domain-aware.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"CRV replaces MLP modules with trained transcoders to produce sparse interpretable features, then applies greedy path-finding to construct weighted directed attribution graphs. Three feature categories are extracted: global statistics (node counts, entropy), node properties (activation distributions), and topological measures (density, betweenness centrality). A gradient boosting classifier trained on these features achieves 98.8% AUROC on arithmetic and 93.4% on GSM8K. Targeted interventions (clamping single transcoder features) demonstrate causal link between structural signatures and errors.\",\n    \"limitations_and_open_questions\": \"Evaluated only on Llama 3.1 8B with synthetic Boolean/arithmetic tasks plus GSM8K — scalability to larger models and complex reasoning domains is untested. Domain-specificity of signatures means a universal verifier seems infeasible; per-domain classifiers are needed.\",\n    \"building_blocks\": [\n      \"Transcoder-based attribution graph construction\",\n      \"Structural feature taxonomy for computational graphs\",\n      \"Domain-specificity of error signatures finding\",\n      \"Causal intervention methodology for verification\"\n    ],\n    \"relevance_to_seed\": \"The domain-specificity finding directly motivates our routing approach: since error signatures vary by domain, a single verifier (formal or neural) cannot be optimal everywhere — routing between formal and neural verifiers per step is the natural response.\"\n  },\n  {\n    \"title\": \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\",\n    \"venue\": \"ACL 2025\",\n    \"problem_identification\": \"Existing PRM evaluations use only GSM8K/MATH-level problems, masking the failure of PRMs on harder mathematical reasoning. ProcessBench identified that no benchmark existed to test step-error detection at competition and Olympiad difficulty level\n... (truncated)\n\n## Your task\n\nSynthesize these paper analyses into a **Field Guide** — a strategic document that would help a researcher generate novel, high-quality ideas in this area. This is NOT a survey — it's an opinionated strategy guide for innovation.\n\nThink about:\n- What PATTERNS OF INNOVATION keep working in this field?\n- What do reviewers consistently reward?\n- Where are the real gaps (not assumed gaps)?\n- What combinations haven't been tried?\n- What mistakes should we avoid?\n\n## Output format\n\nOutput a JSON object with these sections:\n{\n  \"innovation_patterns\": [\n    {\"pattern\": \"name\", \"description\": \"how it works\", \"examples\": [\"paper1\", \"paper2\"], \"success_rate\": \"high/medium/low\"}\n  ],\n  \"reviewer_preferences\": [\n    \"What reviewers in this area consistently care about (based on evidence from paper analyses)\"\n  ],\n  \"field_gaps\": [\n    {\"gap\": \"description of unsolved problem\", \"evidence\": \"which papers mention this limitation\", \"difficulty\": \"high/medium/low\", \"impact_if_solved\": \"high/medium/low\"}\n  ],\n  \"untried_combinations\": [\n    {\"idea_sketch\": \"what could be combined\", \"from_papers\": [\"which papers inspire this\"], \"why_promising\": \"reason\"}\n  ],\n  \"method_building_blocks\": [\n    {\"tool\": \"name\", \"what_it_does\": \"description\", \"used_by\": [\"papers\"], \"could_be_applied_to\": \"new application\"}\n  ],\n  \"common_pitfalls\": [\n    \"Mistakes to avoid when working in this area (based on reviewer feedback and paper limitations)\"\n  ],\n  \"field_trajectory\": \"Where is this field heading? What are the 2-3 most promising macro-directions? (paragraph)\",\n  \"meta_advice\": \"If you were advising a PhD student to write a strong 2026 paper in this area, what would you tell them? (paragraph)\"\n}\n\nBe specific and evidence-based — every claim should reference specific papers from the analyses. Avoid generic advice like 'be novel' — instead say 'Papers that combine X with Y for task Z have been getting accepted (see Paper A, Paper B).'.\n\nIMPORTANT: You MUST end your response with the JSON object."
}
```

---

### Runtime record

_source line 2 · 2026-05-29T08:50:57.182Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T08:50:57.182Z",
  "sessionId": "7cded7ed-6407-48ab-84e6-3517a2852229"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-29T08:50:57.199Z_

You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.

**Today's date: 2026-05-29 (UTC).**

## Research area: Target: AAAI 2026 (or AAAI 2027 if deadline has passed)
Track: Knowledge Representation and Reasoning / Safe and Robust AI

Direction: Build a hybrid PRM that learns to route each reasoning step to either a formal verifier (Z3/Lean 4) or a neural verifier (GenPRM-style) based on a learned formalizability score, then apply this routing framework specifically to detect miracle steps — unjustified logical leaps where the conclusion is correct but not derivable from preceding steps. The formal verifier provides binary derivability judgments for formalizable steps while the neural verifier handles non-formalizable steps, with the router trained on FoVer-style formally verified data as ground truth.

Seed Papers:
- FoVer (Kamoi et al., ACL 2026 Findings / ICLR 2026) — provides the formal verification infrastructure (Z3 + Isabelle) for PRM training data synthesis; our direct foundation
- Curing Miracle Steps with Rubric Rewards (Yuan et al., 2025) — taxonomizes the miracle step problem and proposes RRM; our work replaces neural rubrics with formal derivability
- ARES (You & Xue, EMNLP 2025) — checks step entailment from predecessors probabilistically; our key differentiator is using formal (not neural) derivability checking
- PRoSFI (2026, under review ICLR 2026) — uses formal intermediaries for process rewards; doesn't route between formal/neural or target miracle steps specifically
- Safe (ACL 2025) — Lean 4 step-level verification; provides formalization pipeline but doesn't train PRMs or detect miracle steps
- GenPRM (Liu et al., AAAI 2026) — SOTA generative neural PRM; serves as our neural verifier baseline
- Typed Chain-of-Thought (ICLR 2026 submission) — Curry-Howard framework for reasoning verification; provides theoretical motivation for our type-checking-as-derivability angle

Known Gaps:
- No existing system routes between formal and neural verifiers per step based on a learned formalizability classifier — all current approaches are formal-only or neural-only
- No work applies formal proof-assistant derivability checking to detect miracle steps — ARES checks entailment neurally, RRM uses neural rubrics, but formal derivability from predecessors is untested
- The formalizability spectrum (fully formalizable → partially → not at all) has not been characterized or exploited for PRM design

Theoretical Anchor: A reasoning step S_i is justified iff S_i is formally derivable from {S_1, ..., S_{i-1}} ∪ {problem statement} under known inference rules. Steps where formal derivation fails or times out are miracle-step candidates. The formalizability score (proportion of a step's sub-claims that can be expressed in SMT/HOL) determines router behavior. This connects PRMs to classical proof theory: reward = derivability.

Constraints:
- Compute: ≤200 H100-hours (router ~10h, PRM fine-tuning at 7B ~50h, formal verification CPU-bound, evaluation ~40h)
- Must clearly differentiate from FoVer (training-only formal), PRoSFI (no routing), ARES (neural-only entailment), and Safe (no PRM training)
- Target 7B scale for academic tractability
- Use FoVer's public codebase and data as starting infrastructure

Quality Self-Checks:
- [x] Core insight: A PRM that knows which steps it can formally verify and which it must judge neurally will catch miracle steps that pure neural PRMs miss.
- [x] Why not obvious: Routing requires solving the meta-problem of formalizability classification, which no one has tackled because formal and neural verification communities don't overlap. PRoSFI and Safe avoid routing by requiring ALL steps to be formalizable.
- [x] Baseline fear test: A simple baseline (run Z3 on every step, fall back to neural on timeout) would get ~60% of the routing benefit — the learned router must demonstrably outperform this naive fallback on partial-formalizability cases.
- [x] Information exploited: The formalizability structure of each step — specifically which sub-claims are expressible in SMT logic and which require informal reasoning — is information that no existing PRM uses.

Avoid:
- Training only on formally verifiable data (that's FoVer — must show value of the hybrid approach on non-formalizable steps)
- Claiming formal verification solves everything (formalization success rate will be 40-60% — must be honest about coverage limits and show the neural fallback is essential)
- Evaluating only on math (AAAI values generality — include code via LiveCodeBench and science via GPQA)
- Ignoring the ARES comparison (must show formal derivability checking outperforms neural entailment checking on miracle step detection)

## Paper analyses (20 papers)

[
  {
    "title": "FoVer: Efficient PRM Training Data Synthesis via Formal Verification",
    "venue": "ACL 2026 Findings (withdrawn from ICLR 2026)",
    "problem_identification": "PRM training data is expensive: human annotation suffers ~30% discard rates from low inter-annotator agreement, while Monte Carlo rollout methods (Math-Shepherd) require 8×#steps LLM calls per solution and produce noisy labels. The gap is the absence of a cheap, deterministic, accurate step-level label source.",
    "key_insight": "Formal verification tools (Z3 for propositional logic, Isabelle/HOL for theorem proving) can serve as zero-cost, deterministic oracles for step-level correctness labels—and surprisingly, PRMs trained only on formal-domain data generalize to informal NL reasoning tasks.",
    "innovation_type": "cross_domain",
    "method_summary": "FoVer generates step-by-step solutions with base LLMs (7-8B), converts informal math reasoning to Isabelle proofs via a 70B translator, then verifies each step independently—Z3 checks satisfiability of negated conclusions in CNF; Isabelle uses 'sorry' isolation to check individual proof steps. This produces FoVer-40K (20K logic + 20K theorem proving steps, 50% error rate), which fine-tunes PRMs via binary cross-entropy on 'correct'/'incorrect' token prediction. The key technical trick for Isabelle is assuming other steps correct when evaluating a target step, enabling isolated per-step verification.",
    "limitations_and_open_questions": "Coverage limited to formalizable domains (~40-60% of real reasoning); Isabelle dataset generation took weeks on multiple servers. Open question: can the formal-to-informal transfer be improved by mixing formal and neural verification signals rather than using formal data alone?",
    "building_blocks": [
      "Z3 step-level satisfiability checking via CNF negation",
      "Isabelle sorry-based step isolation",
      "FoVer-40K dataset with binary step labels",
      "Informal-to-formal conversion pipeline (70B few-shot)",
      "Cross-entropy PRM fine-tuning on verification tokens",
      "Public codebase and data"
    ],
    "relevance_to_seed": "Direct foundation—provides the formal verification infrastructure, public data, and cross-domain generalization evidence that the hybrid router builds upon; the key limitation (formal-only coverage) is exactly what the neural fallback addresses."
  },
  {
    "title": "Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification",
    "venue": "ACL 2025",
    "problem_identification": "PRMs and self-consistency methods are opaque—they score steps without providing checkable evidence. The gap: no system translates each NL reasoning step into formal Lean 4 statements for machine-verified correctness proofs, which would provide interpretable, binary ground truth.",
    "key_insight": "Step-level formalization difficulty is much lower than whole-problem formalization, making automated theorem proving feasible within small compute budgets (16 proof attempts per step), and retrospective formal verification is complementary to prospective PRM scoring.",
    "innovation_type": "new_technique",
    "method_summary": "Safe decomposes CoT traces into discrete steps (heuristic or LLM-based), auto-formalizes each into Lean 4 theorem statements via few-shot prompting with syntax validation through Lean REPL, then runs ATPs (COPRA, DeepSeek-Prover-V1.5) to prove or fail each statement. Steps receive one of four states: no-verification-needed, failed-formalization, proved, unprovable. A tiny 2-layer LSTM (hidden=64) aggregates state sequences into a retrospective score, which combines with prospective PRM scores via weighted geometric mean (score = retro^α × pro^(1-α)). FormalStep benchmark: 30,809 formal statements from 500 MATH problems across 5 domains.",
    "limitations_and_open_questions": "Lean 4 struggles with geometry and combinatorics; auto-formalization and ATP are both fallible, injecting noise. No routing mechanism exists to decide when formalization is worth attempting. Does the 4-state LSTM capture enough signal, or would richer features (partial proof progress, formalization confidence) help?",
    "building_blocks": [
      "Lean 4 auto-formalization pipeline with REPL validation",
      "4-state step verification taxonomy",
      "LSTM retrospective scorer",
      "Geometric mean score ensembling",
      "FormalStep benchmark (30K+ statements)"
    ],
    "relevance_to_seed": "Provides the Lean 4 formalization pipeline and the retrospective/prospective complementarity insight; the 4-state taxonomy (especially failed-formalization vs. unprovable) directly informs the formalizability classifier design in the proposed router."
  },
  {
    "title": "Typed Chain-of-Thought: A Curry-Howard Framework for Verifying LLM Reasoning",
    "venue": "arXiv 2025 (ICLR 2026 submission, withdrawn)",
    "problem_identification": "CoT verification methods are either post-hoc and heuristic (self-consistency, PRMs) or require full formal proof construction. The gap: no framework provides lightweight, during-generation formal certificates for CoT faithfulness without requiring a separate proof assistant.",
    "key_insight": "Under Curry-Howard correspondence, a faithful CoT trace is a well-typed program—so type-checking (much cheaper than theorem proving) suffices to certify reasoning faithfulness, and ill-typed traces can be filtered before answer aggregation.",
    "innovation_type": "new_formulation",
    "method_summary": "PC-CoT (Proof-Carrying CoT) operates in three stages: (1) the LLM emits structured JSON with typed annotations (premises, operations, answers using a type system of ℕ⊆ℤ⊆ℚ plus unit/dimensional types), (2) a Typed Reasoning Graph (bipartite multigraph of statement and rule nodes) is constructed to track dataflow, (3) certification metrics (Coverage, EVR, UVR, Path Existence, Min Path Score) gate which traces aggregate into final answers. Two gates are offered: relaxed (70.4% acceptance, 87.2% precision) and strict (56.3% acceptance, 91.6% precision). Classification of steps to rule schemas uses regex heuristics with fallback.",
    "limitations_and_open_questions": "Type system is narrow (numeric/unit types only)—cannot handle logical quantifiers, set theory, or complex mathematical structures. Regex-based rule classification is brittle. The paper was withdrawn from ICLR 2026, suggesting reviewer concerns. Can this type-checking framework scale beyond arithmetic to richer mathematical reasoning?",
    "building_blocks": [
      "Curry-Howard framing of CoT-as-typed-program",
      "Typed Reasoning Graph representation",
      "5 certification metrics (Coverage, EVR, UVR, PE, MPS)",
      "Certified self-consistency filtering",
      "Configurable strictness gates"
    ],
    "relevance_to_seed": "Provides theoretical motivation for the derivability-as-reward formulation—the Curry-Howard framing justifies treating type-checking/proof-checking as a verification signal; the narrow type system illustrates why a neural fallback is needed for steps outside the formalizable fragment."
  },
  {
    "title": "VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks",
    "venue": "arXiv 2025 (under review)",
    "problem_identification": "LLMs can reach correct answers through flawed reasoning, and neither neural verifiers nor self-consistency can reliably detect logical invalidity in intermediate steps. The gap: no system formalizes CoT steps into machine-checkable FOL with explicit premise tracking to enable automated derivability verification.",
    "key_insight": "By decomposing verification into (1) autoformalization into FOL/SMT-LIB, (2) explicit premise identification with source categorization (context/commonsense/inference), and (3) Z3 entailment checking, you get both symbolic validity verification AND human-interpretable explanations of why steps fail.",
    "innovation_type": "combination",
    "method_summary": "VeriCoT's pipeline: an LLM translates each CoT step into SMT-LIB format (up to 3 attempts with vocabulary extension via declare-fun/declare-sort), then identifies premises categorized as context-grounded, commonsense, or inference-based. Z3 checks three properties per step: entailment (ℱ_{i-1} ⊨ F_i), contradiction (ℱ_{i-1} ⊨ ¬F_i), and consistency. Steps are classified as valid, ungrounded, contradictory, or untranslatable. The verification signal feeds three downstream applications: inference-time self-reflection, SFT on VeriCoT-distilled data, and DPO with verification-based pairwise rewards. Evaluated on ProofWriter, LegalBench-SARA, and BioASQ.",
    "limitations_and_open_questions": "Limited to FOL fragment with linear arithmetic and uninterpreted functions—many mathematical steps require higher-order logic. The 3-attempt autoformalization has unknown success rate on complex math. No learned routing to decide when formalization is worthwhile. How does VeriCoT's entailment checking compare to ARES's neural entailment on miracle step detection?",
    "building_blocks": [
      "SMT-LIB autoformalization with iterative vocabulary extension",
      "3-category premise identification (context/commonsense/inference)",
      "Z3 entailment/contradiction/consistency triple-check",
      "Verification-as-reward for DPO training",
      "4-class step classification (valid/ungrounded/contradictory/untranslatable)"
    ],
    "relevance_to_seed": "Most directly relevant existing system to the formal verification component—VeriCoT's Z3 entailment checking (ℱ_{i-1} ⊨ F_i) is essentially formal derivability checking for miracle steps. The proposed router extends this by learning when to invoke formal vs. neural verification, and VeriCoT's 'untranslatable' category directly motivates the formalizability classifier."
  },
  {
    "title": "Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations",
    "venue": "ACL 2024",
    "problem_identification": "Process reward models require expensive human step-level annotations (PRM800K cost ~$500K+). Outcome reward models ignore intermediate reasoning quality. The gap: no automatic method existed to construct step-level supervision data for PRM training at scale.",
    "key_insight": "A step's correctness can be approximated by its potential to reach the correct final answer—if any completion from step i reaches the gold answer, step i is likely correct. This reframes step verification as a reachability problem solvable by Monte Carlo sampling.",
    "innovation_type": "simplification",
    "method_summary": "A completer model (LLemma-7B fine-tuned on target data) generates N=8 continuations from each intermediate step. Hard estimation assigns binary labels (1 if any completion is correct, 0 otherwise; 86% accuracy at N=4). Soft estimation uses completion success frequency as a continuous label. The PRM scores solutions by taking the minimum step score across all steps. For RL, step-by-step PPO delivers rewards at each reasoning step rather than only at sequence end. Results: Mistral-7B accuracy 77.9%→84.1% (GSM8K) and 28.6%→33.0% (MATH) with PPO; 89.1% and 43.5% with verification reranking.",
    "limitations_and_open_questions": "Labels are noisy—a step can be wrong yet still lead to the correct answer by lucky cancellation, and correct steps may fail to reach the answer due to completer weakness. The method requires 8×#steps LLM forward passes per solution. Can formal verification replace Monte Carlo sampling to get deterministic, noise-free step labels (this is exactly what FoVer does)?",
    "building_blocks": [
      "Monte Carlo completion-based step labeling",
      "Hard/soft estimation for step correctness",
      "Min-score solution ranking",
      "Step-level PPO with per-step rewards",
      "Automatic PRM training pipeline without human annotation"
    ],
    "relevance_to_seed": "Foundational method that FoVer and the proposed work build upon—Math-Shepherd established the paradigm of automatic step-level supervision for PRM training. Its key limitation (noisy labels from Monte Carlo approximation) is precisely what formal verification addresses, and its min-score ranking is the evaluation protocol the proposed hybrid PRM must beat."
  },
  {
    "title": "Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards",
    "venue": "ACL 2026 Main",
    "problem_identification": "Through systematic human verification of LLM math solutions, the authors discovered that correct final answers frequently mask logically invalid reasoning — 'miracle steps' where models jump to correct outputs without valid derivation. They taxonomized six false-positive categories (inductive overgeneralization, outcome irrelevance, neglected preconditions, unverified assumptions, numerical coincidence, miracle steps) that existing PRMs fail to catch.",
    "key_insight": "Problem-specific rubrics that encode targeted evaluation criteria against known failure modes detect reasoning flaws that outcome-based and step-level process rewards systematically miss.",
    "innovation_type": "new_formulation",
    "method_summary": "Three-phase pipeline: (1) Gemini-2.5-Pro synthesizes problem-specific rubrics grounded in structure-based scaffolding and method-agnostic fairness; (2) scoring data is synthesized by evaluating candidate responses against rubrics on a 0-10 scale; (3) Qwen3-4B is fine-tuned via SFT then PPO to predict rubric-aligned quality scores. The RRM receives (question, rubric, response) triples and outputs integer scores normalized to [0,1] as RL training rewards, achieving F1=0.693 (+0.312 over PRM baselines) and reducing miracle steps by 71%.",
    "limitations_and_open_questions": "Rubrics are neurally generated (Gemini-2.5-Pro dependency) — no formal guarantee that rubric criteria are complete or sound. The approach doesn't verify logical derivability between steps; it evaluates against heuristic criteria, leaving room for formally grounded alternatives.",
    "building_blocks": [
      "Miracle step taxonomy (6 false-positive categories)",
      "Rubric synthesis pipeline",
      "RRM training recipe (SFT+PPO on rubric scores)",
      "False positive detection benchmarks on AIME2024"
    ],
    "relevance_to_seed": "Defines and taxonomizes the exact problem (miracle steps) our formal-derivability router targets; RRM's 71% reduction is the neural baseline our hybrid approach must surpass by adding formal derivability checking."
  },
  {
    "title": "Process Reward Models That Think (ThinkPRM)",
    "venue": "arXiv 2025 (Google DeepMind); withdrawn from ICLR 2026",
    "problem_identification": "Discriminative PRMs require hundreds of thousands of human-labeled step annotations (PRM800K) yet remain brittle out-of-domain. The authors observed that long-CoT reasoning models already possess latent verification capabilities that can be elicited through generation rather than classification.",
    "key_insight": "Recasting process verification as generative chain-of-thought reasoning — rather than discriminative classification — achieves superior data efficiency (100x fewer labels) and enables test-time compute scaling of the verifier itself.",
    "innovation_type": "new_technique",
    "method_summary": "ThinkPRM fine-tunes reasoning models (R1-Distill-Qwen 1.5B–14B) on ~1K synthetic verification CoTs sampled from QwQ-32B-Preview and filtered against 8K gold process labels from PRM800K. At inference, the model generates verification reasoning up to 8K tokens, then scores via P('yes')/(P('yes')+P('no')) on a forced 'Is the solution correct?' query. Verification compute scales in two axes: parallel (K independent CoTs averaged) and sequential (longer thinking budgets), with stable improvements up to 24K tokens unlike LLM-as-a-Judge which degrades.",
    "limitations_and_open_questions": "Withdrawn from ICLR 2026 — unknown review concerns. Verification remains purely neural with no formal grounding; generated critiques may themselves contain reasoning errors. Filtering against gold labels creates a ceiling tied to PRM800K quality.",
    "building_blocks": [
      "Generative verification CoT paradigm",
      "Data-efficient PRM training recipe (1K examples)",
      "Parallel/sequential verifier compute scaling",
      "OOD evaluation protocol (GPQA-Diamond, LiveCodeBench)"
    ],
    "relevance_to_seed": "Strongest neural PRM baseline and natural candidate for the neural verifier component in our hybrid router; its OOD generalization to GPQA/LiveCodeBench validates the evaluation domains we target, and its test-time scaling mechanism could complement formal verification routing."
  },
  {
    "title": "Scaling LLM Test-Time Compute Optimally Can be More Effective than Scaling Model Parameters",
    "venue": "ICLR 2025 Oral",
    "problem_identification": "Prior work showed test-time compute scaling existed but provided mostly negative results about its efficiency. The authors identified that uniform compute allocation across questions of varying difficulty is fundamentally wasteful — easy questions need little compute while hard questions may not benefit regardless.",
    "key_insight": "Difficulty-adaptive compute allocation — choosing between search (PRM-guided) and revision strategies per question based on estimated difficulty — yields 4x efficiency gains over uniform best-of-N, making smaller models competitive with 14x larger ones.",
    "innovation_type": "analysis",
    "method_summary": "The paper systematically compares PRM-guided search (best-of-N weighted, beam search, lookahead) against revision-based distribution updates across difficulty bins. PRMs are trained via Monte Carlo rollouts with binary cross-entropy, using last-step predictions as full-answer scores. Questions are binned into 5 difficulty levels using PRM-estimated pass@1 rates, and optimal strategy per bin is selected via two-fold cross-validation. Key finding: beam search excels on medium-difficulty but degrades on easy problems due to PRM exploitation (repetitive low-information steps); revision outperforms parallel sampling sequentially but requires balanced parallel-sequential ratios for hard problems.",
    "limitations_and_open_questions": "Evaluated only on MATH with PaLM 2-S*; PRM exploitation in beam search reveals verifier fragility that better verifiers (formal+neural) could mitigate. Hardest problems show minimal improvement from any strategy, suggesting a ceiling on test-time scaling without better base models.",
    "building_blocks": [
      "Compute-optimal test-time scaling framework",
      "Difficulty-adaptive strategy selection",
      "PRM exploitation analysis",
      "FLOPs-matched comparison methodology"
    ],
    "relevance_to_seed": "Foundational motivation: better verifiers directly amplify test-time scaling efficiency. Our hybrid formal+neural PRM should reduce the PRM exploitation problem (formal verifiers are harder to game) and extend the difficulty range where test-time compute helps."
  },
  {
    "title": "Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification",
    "venue": "arXiv 2026",
    "problem_identification": "Existing neuro-symbolic approaches apply formal verification post-hoc (filtering completed solutions), missing the opportunity to prevent error propagation during reasoning. The authors identified that real-time formal feedback during generation — not just after — could correct errors as they arise.",
    "key_insight": "Interleaving formal symbolic verification as inline feedback during chain-of-thought generation, with hierarchical penalties for verification failures, prevents error cascading rather than merely filtering post-hoc.",
    "innovation_type": "combination",
    "method_summary": "Each reasoning step is augmented with a formal specification and verification result triple (sᵢ, fᵢ, vᵢ). A two-stage pipeline: (1) SFT on synthesized data containing natural language + formal code blocks + interpreter outputs, validated through exact matching, semantic equivalence, and proof rewriting; (2) GRPO with hierarchical rewards — fatal execution failures (-8.0), format violations (-6.0), structural penalties for undefined tags/excess tool calls. Verification uses Python/Z3 execution in sandboxes. At 7B/14B scale, achieves 10.4%/14.2% gains across six reasoning benchmarks.",
    "limitations_and_open_questions": "Uses execution-based validation (Python/Z3) rather than proof-based (Lean/Isabelle), limiting formal guarantees. No routing mechanism — all steps attempt formalization. Coverage/success rate of formal verification per step is not reported, making it unclear how often the formal signal actually helps versus adds noise.",
    "building_blocks": [
      "Interleaved verification architecture (s,f,v triples)",
      "Hierarchical reward design for formal feedback",
      "Two-stage SFT+GRPO pipeline at 7B/14B",
      "Real-time formal verification during generation"
    ],
    "relevance_to_seed": "Demonstrates feasibility of integrating formal verification into the reasoning loop at 7B scale, validating our compute assumptions. Key differentiator: they attempt to formalize every step (no routing), while we route based on formalizability — their coverage gaps motivate our neural fallback."
  },
  {
    "title": "Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning",
    "venue": "arXiv 2026",
    "problem_identification": "The authors identified a critical reliability cliff: Lean-based formal verification is 96% accurate at high proved coverage but drops to 20% at low coverage, yet no prior work quantified when formal signals can be trusted. They further discovered that 7B autoformalizers achieve only 28% coverage with merely 43% proof faithfulness — autoformalization, not proof search, is the bottleneck (zero timeouts observed).",
    "key_insight": "Formal verification's value is coverage-dependent with a sharp reliability cliff — risk-controlled abstention with calibrated coverage thresholds transforms an unreliable partial signal into a high-precision selective judge.",
    "innovation_type": "analysis",
    "method_summary": "CovCal uses three Lean diagnostic metrics: typed coverage (fraction reaching well-formed Lean), proved coverage (fraction with formal proofs), and formal margin (proved vs. unresolved rival weight). Acceptance requires all three exceeding calibrated thresholds simultaneously. Thresholds are selected from a 125-cell grid under two regimes: conservative Bonferroni bounds (α=δ/125) which often reject-all at low coverage, or development-then-calibration which preselects one threshold on a dev split then certifies on calibration data. Prover-specialized Goedel-Prover-V2-8B achieves 79% coverage (vs. 28% for general 7B), enabling Bonferroni certification on 17/20 bootstrap partitions.",
    "limitations_and_open_questions": "Manual faithfulness audit covers only 45 examples with a single annotator. The 28% coverage figure is specific to Qwen2.5-Coder-7B — better formalizers could shift the entire coverage-reliability curve. No step-level analysis; all results are problem-level answer verification rather than intermediate step checking.",
    "building_blocks": [
      "Coverage-reliability cliff quantification (96% → 20%)",
      "CovCal risk-controlled selection mechanism",
      "Proof faithfulness taxonomy (genuine/trivial/structural/spurious)",
      "Autoformalization bottleneck analysis",
      "Coverage diagnostic metrics (C_typ, C_prf, M)"
    ],
    "relevance_to_seed": "Directly validates our hybrid design's core premise: 7B formalization covers only 28% of problems with 43% faithfulness, proving a neural fallback is essential. The coverage-reliability cliff (96% at high, 20% at low coverage) is exactly the signal our formalizability router must learn to exploit — route to formal verification only when coverage is sufficient for reliable judgments."
  },
  {
    "title": "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning",
    "venue": "AAAI 2026",
    "problem_identification": "Existing PRMs are discriminative scalar predictors that cannot leverage LLM generative capabilities or scale test-time compute. The authors identified that process supervision labels are noisy and verification reasoning is opaque, creating both a data quality and an inference scalability gap.",
    "key_insight": "Process reward modeling should be reformulated as a generative task where the PRM produces explicit CoT reasoning with executable code verification before judging each step, enabling test-time scaling via majority voting over multiple verification trajectories.",
    "innovation_type": "new_formulation",
    "method_summary": "GenPRM introduces Relative Progress Estimation (RPE): P_t = (MC(s_t) - MC(s_{t+1})) / MC(s_1), comparing Monte Carlo pass-rate changes between consecutive states to obtain soft step-level labels. A rationale synthesis pipeline uses QwQ-32B to generate CoT reasoning in &lt;analyze> tags plus executable Python code in &lt;verify> tags; code execution results feed back into the generative process. At inference, N verification paths are sampled and majority-voted, enabling test-time compute scaling. Trained on only 23K MATH examples, GenPRM-1.5B outperforms GPT-4o and GenPRM-7B surpasses Qwen2.5-Math-PRM-72B on ProcessBench.",
    "limitations_and_open_questions": "RPE still relies on MC sampling which is expensive; code verification only works for computationally checkable claims, leaving non-executable reasoning steps judged purely by CoT. Evaluation is math-centric with unclear generalization to non-mathematical domains.",
    "building_blocks": [
      "Generative PRM architecture with &lt;analyze>/&lt;verify> tags",
      "RPE labeling method",
      "Test-time majority voting for PRMs",
      "23K MATH training data"
    ],
    "relevance_to_seed": "GenPRM serves as the neural verifier component in our hybrid router — its generative architecture handles non-formalizable steps while our formal verifier handles formalizable ones, and our router must outperform GenPRM-alone on miracle step detection."
  },
  {
    "title": "Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries (PRoSFI)",
    "venue": "arXiv 2026 (under review)",
    "problem_identification": "Outcome rewards overlook flawed intermediate steps even when final answers are correct, but direct formal proof generation is beyond 7B models' capabilities. The authors identified this gap between the aspiration for formal verification and practical model capability.",
    "key_insight": "Instead of demanding complete formal proofs, models can output structured formal intermediaries — lightweight JSON blocks with formal conclusions in Lean4 syntax and explicit dependency/rule fields — that are individually verifiable by automated provers without requiring end-to-end proof synthesis.",
    "innovation_type": "combination",
    "method_summary": "Each reasoning step outputs a structured block containing an id, dependencies (max 4), a formal conclusion in Lean4 syntax, and the inference rule applied. Formal propositions are extracted and verified independently using Lean4, Z3, or Prover9. Training uses GRPO with a tiered reward: 1.0 for correct answer + all steps verified, 0.3 for correct but unverified steps, 0.1 for format-correct but wrong answer, 0.0 otherwise. On ProverQA-Hard, PRoSFI achieves 76.07% GPT-judged soundness vs 21.97% for outcome-CoT baselines while maintaining 92.97% accuracy. Training takes ~14 hours on 8 Hopper GPUs.",
    "limitations_and_open_questions": "Requires ALL steps to be formalizable — no fallback for inherently non-formalizable reasoning. The max-4-dependency constraint and reliance on lightweight tactics (aesop, simp) limit expressiveness. Evaluation is restricted to logic puzzles (ProverQA, Knights & Knaves).",
    "building_blocks": [
      "Structured formal intermediary format (JSON with Lean4 conclusions)",
      "Tiered verification reward function",
      "Multi-prover verification (Lean4/Z3/Prover9)",
      "GRPO training with formal rewards"
    ],
    "relevance_to_seed": "PRoSFI is our primary architectural contrast — it requires all steps to be formalizable while our hybrid router gracefully degrades to neural verification for non-formalizable steps, and PRoSFI doesn't target miracle step detection specifically."
  },
  {
    "title": "Let's Verify Step by Step",
    "venue": "ICLR 2024",
    "problem_identification": "Outcome supervision provides no signal about intermediate reasoning quality, conflating correct final answers with valid reasoning chains. The authors identified that step-level feedback was theoretically motivated but lacked large-scale empirical validation.",
    "key_insight": "Process supervision (step-level human labels: positive/negative/neutral) significantly outperforms outcome supervision for training reward models, and active learning that surfaces high-scoring wrong-answer solutions to labelers yields 2.6× data efficiency.",
    "innovation_type": "new_benchmark",
    "method_summary": "Human labelers annotated each step as positive, negative, or neutral without reference solutions (only ground-truth final answers). PRM800K contains 800K step-level labels across 75K solutions to 12K MATH problems. The PRM is trained on these labels and used for best-of-N selection over generator outputs. Active learning ranks solutions with the current best PRM and surfaces convincing-but-wrong solutions for labeling, then retrains between generations. The process-supervised PRM achieved 78% on a representative MATH subset, significantly outperforming outcome-supervised equivalents.",
    "limitations_and_open_questions": "Labels are human-generated (expensive, subjective — neutral vs positive is ambiguous). The PRM is discriminative and opaque about WHY a step fails. No formal notion of 'correctness' — labels capture human judgment, not logical derivability.",
    "building_blocks": [
      "PRM800K dataset (800K step-level labels)",
      "Process vs outcome supervision framework",
      "Active learning for PRM data collection",
      "Best-of-N evaluation methodology"
    ],
    "relevance_to_seed": "Foundational PRM paper that our work builds upon — we replace expensive human step-level labels with formal derivability judgments from Z3/Lean and neural verification from GenPRM, while PRM800K's annotation protocol informs our evaluation criteria."
  },
  {
    "title": "Reward Under Attack: Analyzing the Robustness and Hackability of Process Reward Models",
    "venue": "arXiv 2026",
    "problem_identification": "PRMs are increasingly central to LLM reasoning pipelines but have never been stress-tested adversarially. The authors identified the untested assumption that high PRM scores indicate genuine reasoning quality.",
    "key_insight": "Current PRMs function as fluency detectors rather than reasoning verifiers — they are invariant to surface-level style changes (|ΔR|<0.1) yet fail inconsistently at detecting logical corruption, and RL policies exploit this by achieving >0.9 PRM reward with <4% actual accuracy.",
    "innovation_type": "analysis",
    "method_summary": "A three-tier diagnostic framework: (1) Static perturbation analysis applies semantics-preserving changes (rephrasing, verbosity) and semantics-altering attacks (question shuffling, numerical perturbation, reasoning hallucination) measuring ΔR; (2) Gradient-based adversarial token optimization maximizes reward on flawed AIME trajectories with as few as 1 appended embedding, inflating Skywork-1.5B rewards from 0.237→0.954; (3) RL-induced reward hacking trains Qwen2.5-1.5B via GRPO using PRM feedback, showing reward climbs to >0.9 while accuracy stays <4%, with 43% of gains from stylistic shortcuts (measured via rephrasing intervention on held-out AIME 2025).",
    "limitations_and_open_questions": "Tested only Skywork and Qwen PRMs — unclear if findings generalize to generative PRMs like GenPRM. The 43% stylistic attribution method (rephrasing intervention) is approximate. Does not propose solutions beyond diagnostic tooling.",
    "building_blocks": [
      "Three-tier PRM robustness diagnostic framework",
      "PRM-BiasBench benchmark",
      "Gradient-based PRM attack methodology",
      "Stylistic vs content reward decomposition"
    ],
    "relevance_to_seed": "Provides core motivation — formal derivability checking is inherently robust to fluency-based reward hacking since Z3/Lean proofs are immune to stylistic manipulation, directly addressing the 'fluency detector' vulnerability this paper exposes."
  },
  {
    "title": "Scaling Test-Time Compute Without Verification or RL is Suboptimal",
    "venue": "ICML 2025 (Spotlight)",
    "problem_identification": "The relative merits of verification-based (VB: RL + search with rewards) versus verification-free (VF: distillation of correct traces) test-time scaling lacked theoretical grounding. The authors identified that empirical comparisons were confounded by implementation differences.",
    "key_insight": "Under heterogeneous solution distributions (high variance in token-level Q-values across paths to the same answer) and anti-concentration (base policy covers above-mean policies with constant probability), VB methods achieve Ω̃(√H) better scaling than any VF method — the gap is structural, not implementational.",
    "innovation_type": "new_formulation",
    "method_summary": "VF methods are formalized as finetuning within a χ²-divergence ball around the base policy using expert traces; VB methods query reward annotations on the policy's own rollouts. The main separation theorem (5.8) proves that with heterogeneous base policies (σ̃_b = Ω(H)) satisfying anti-concentration, VB achieves O(H/n) suboptimality vs VF's Ω(H/√n) — a √H gap when n = Ω(H). Empirically validated on 3B/8B/32B Llama models and the S1 distillation model, showing VB outperforms VF with widening gaps as test-time budget increases. Common pretrained LLMs are shown to empirically satisfy both heterogeneity and anti-concentration conditions.",
    "limitations_and_open_questions": "Assumes access to a perfect verifier — the quality of the reward model is not accounted for in the theory. Anti-concentration may not hold for heavily fine-tuned or collapsed policies. The bi-level reward structure (sparse binary) may not capture nuanced step-level verification.",
    "building_blocks": [
      "VB vs VF formal framework",
      "Anti-concentration condition for base policies",
      "Separation theorem for test-time compute scaling",
      "Heterogeneity characterization of LLM solution distributions"
    ],
    "relevance_to_seed": "Provides theoretical justification for investing in better verifiers — our hybrid formal/neural PRM improves verification quality, and this paper proves that better verifiers yield asymptotically better test-time scaling, making the formal derivability router's accuracy improvements compound at inference time."
  },
  {
    "title": "Probabilistic Soundness Guarantees in LLM Reasoning Chains (ARES)",
    "venue": "EMNLP 2025",
    "problem_identification": "Standard sequential error detectors condition on all prior steps including erroneous ones, causing error propagation to corrupt downstream judgments. ARES identifies this as a structural flaw in how premises are consumed during chain evaluation.",
    "key_insight": "By marginalizing over exponentially many premise-validity configurations via Monte Carlo sampling, each step's soundness score becomes independent of upstream errors, yielding certified Hoeffding-bound guarantees on per-step soundness estimates.",
    "innovation_type": "new_formulation",
    "method_summary": "ARES defines τ_k = Σ_α E(C(α), C_{n+k}) · Pr[α], averaging NLI entailment scores over all 2^(n+k-1) configurations of premise inclusion/exclusion, weighted by recursively-computed soundness probabilities. Monte Carlo sampling (N iterations) makes this tractable, with Theorem 3.1 guaranteeing |τ̂_k - τ_k| ≤ ε with probability ≥ 1-δ for N ≥ log(2m/δ)/(2ε²). The entailment function is instantiated via LLM prompting (GPT-4o-mini or Qwen3-4B), not formal verification.",
    "limitations_and_open_questions": "Entailment is still neural (NLI-based), so it inherits all failure modes of LLM-based logical judgment — it detects propagation artifacts but cannot verify mathematical derivability. The Hoeffding bound gives concentration guarantees on the estimator, not guarantees that the entailment model itself is correct.",
    "building_blocks": [
      "Autoregressive premise-conditioning framework",
      "Monte Carlo premise configuration sampling",
      "Hoeffding-bound certification for step scores",
      "ProcessBench and GSM8K evaluation protocol"
    ],
    "relevance_to_seed": "ARES is the primary neural-entailment baseline our formal derivability checking must outperform; its framework for conditioning on verified premises could be adapted to mix formal and neural entailment signals within our router."
  },
  {
    "title": "Verifying Chain-of-Thought Reasoning via Its Computational Graph (CRV)",
    "venue": "ICLR 2026 Oral",
    "problem_identification": "Black-box and gray-box CoT verification methods predict correctness from outputs or activations but cannot explain why a computation fails. CRV identified that the model's internal computational structure — not just its outputs — encodes verifiable error signatures.",
    "key_insight": "Attribution graphs of correct vs. incorrect reasoning steps have distinct structural fingerprints (density, centrality, activation distributions), and these signatures are domain-specific — different reasoning tasks produce different error patterns, implying verification must be domain-aware.",
    "innovation_type": "new_technique",
    "method_summary": "CRV replaces MLP modules with trained transcoders to produce sparse interpretable features, then applies greedy path-finding to construct weighted directed attribution graphs. Three feature categories are extracted: global statistics (node counts, entropy), node properties (activation distributions), and topological measures (density, betweenness centrality). A gradient boosting classifier trained on these features achieves 98.8% AUROC on arithmetic and 93.4% on GSM8K. Targeted interventions (clamping single transcoder features) demonstrate causal link between structural signatures and errors.",
    "limitations_and_open_questions": "Evaluated only on Llama 3.1 8B with synthetic Boolean/arithmetic tasks plus GSM8K — scalability to larger models and complex reasoning domains is untested. Domain-specificity of signatures means a universal verifier seems infeasible; per-domain classifiers are needed.",
    "building_blocks": [
      "Transcoder-based attribution graph construction",
      "Structural feature taxonomy for computational graphs",
      "Domain-specificity of error signatures finding",
      "Causal intervention methodology for verification"
    ],
    "relevance_to_seed": "The domain-specificity finding directly motivates our routing approach: since error signatures vary by domain, a single verifier (formal or neural) cannot be optimal everywhere — routing between formal and neural verifiers per step is the natural response."
  },
  {
    "title": "ProcessBench: Identifying Process Errors in Mathematical Reasoning",
    "venue": "ACL 2025",
    "problem_identification": "Existing PRM evaluations use only GSM8K/MATH-level problems, masking the failure of PRMs on harder mathematical reasoning. ProcessBench identified that no benchmark existed to test step-error detection at competition and Olympiad difficulty level
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
  "promptId": "c5441467-55ce-41ce-8333-734b73ac30c3",
  "type": "user",
  "uuid": "ac612525-ded1-42f5-9e9b-f675c7735647",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "7cded7ed-6407-48ab-84e6-3517a2852229",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T08:50:57.197Z_

```json
{
  "parentUuid": "ac612525-ded1-42f5-9e9b-f675c7735647",
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
  "uuid": "fb75f2cb-7749-43f3-a886-7e3b4d83c5ed",
  "timestamp": "2026-05-29T08:50:57.197Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "7cded7ed-6407-48ab-84e6-3517a2852229",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T08:50:57.197Z_

```json
{
  "parentUuid": "fb75f2cb-7749-43f3-a886-7e3b4d83c5ed",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1ff534e1-ac85-4ee6-82d0-fd513ca70c7c",
  "timestamp": "2026-05-29T08:50:57.197Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "7cded7ed-6407-48ab-84e6-3517a2852229",
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
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-29 (UTC).**  ## Research area: Target: AAAI 2026 (or AAAI 2027 if d…",
  "leafUuid": "1ff534e1-ac85-4ee6-82d0-fd513ca70c7c",
  "sessionId": "7cded7ed-6407-48ab-84e6-3517a2852229"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Hybrid formal-neural PRM for miracle step detection",
  "sessionId": "7cded7ed-6407-48ab-84e6-3517a2852229"
}
```

---

### Assistant

_source line 8 · 2026-05-29T08:51:25.045Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to synthesize 20 paper analyses into a strategic "Field Guide" for innovation in the area of process reward models, formal verification of reasoning, and miracle step detection. This is a comprehensive synthesis task that requires careful analysis of patterns across all the papers.

Let me organize my thinking:

1. **Innovation Patterns**: What approaches keep getting accepted?
2. **Reviewer Preferences**: What do reviewers reward?
3. **Field Gaps**: What's actually unsolved?
4. **Untried Combinations**: What hasn't been tried?
5. **Method Building Blocks**: Reusable components


6. **Common Pitfalls**: What to avoid
7. **Field Trajectory**: Where is this heading?
8. **Meta Advice**: Strategic guidance

Now I'm working through the innovation patterns systematically. I'm seeing that reformulating discriminative tasks as generative reasoning—like GenPRM and ThinkPRM do—consistently gets accepted at top venues. There's also a strong pattern of cross-domain transfer where formal verification techniques trained on structured data generalize surprisingly well to informal reasoning tasks. And across multiple papers, I'm noticing the shift toward replacing expensive human annotations with automated signals derived from model behavior or formal properties.

Beyond that, there's a clear trend toward combining neural and symbolic approaches, scaling verification compute at test time for better performance, and publishing diagnostic papers that expose vulnerabilities in existing methods. I'm also noticing that knowing when *not* to verify—like CovCal demonstrates—is just as valuable as the verification itself. Reviewers seem to favor work with formal guarantees or at least probabilistic bounds backing up the claims.

Looking at what's missing in the field, there are several untackled problems: no one's really routing between formal and neural verifiers, formalizability classification hasn't been addressed, step-level formal verification with coverage awareness is unexplored, and most work stays confined to math domains rather than testing across different problem types. There are also some interesting combinations that haven't been tried yet. Now I'm identifying the key pitfalls to avoid—focusing only on standard benchmarks, assuming formal verification handles every step, neglecting comparisons with strong neural approaches, underestimating the autoformalization challenge, and failing to report actual coverage and success metrics for the formal methods themselves.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ff534e1-ac85-4ee6-82d0-fd513ca70c7c",
  "isSidechain": false,
  "requestId": "req_011CbWaG1a6TdkTaMZ9AwqWY",
  "type": "assistant",
  "uuid": "5cfb1f07-5dd0-4c05-bada-a5ea0e990962",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "7cded7ed-6407-48ab-84e6-3517a2852229",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011jUg9A2TVWuGzEDT3T3zLN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13066,
      "cache_read_input_tokens": 11014,
      "output_tokens": 7438,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13066,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 7438,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 13066,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13066
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

_source line 9 · 2026-05-29T08:53:59.291Z_

I'll analyze the 20 papers systematically to produce the Field Guide. Let me first check if there are any additional details I need from the truncated analyses.

```json
{
  "innovation_patterns": [
    {
      "pattern": "Discriminative-to-Generative Reformulation",
      "description": "Taking a task traditionally framed as discriminative classification (e.g., step scoring) and reformulating it as generative reasoning where the model produces explicit verification CoT before judging. This unlocks test-time compute scaling and improves data efficiency by leveraging pretrained reasoning capabilities.",
      "examples": ["GenPRM (AAAI 2026)", "ThinkPRM (arXiv 2025)"],
      "success_rate": "high"
    },
    {
      "pattern": "Formal-Signal-as-Cheap-Oracle",
      "description": "Using formal verification tools (Z3, Lean 4, Isabelle) as cost-free deterministic label sources to replace expensive human annotation or noisy Monte Carlo sampling. The key insight is that formal labels from a narrow domain transfer surprisingly well to broader informal reasoning tasks.",
      "examples": ["FoVer (ACL 2026 Findings)", "Safe (ACL 2025)", "PRoSFI (2026, under review)", "VeriCoT (2025, under review)"],
      "success_rate": "high"
    },
    {
      "pattern": "Vulnerability-Exposure-then-Solution",
      "description": "Publishing a rigorous diagnostic analysis that exposes a fundamental weakness in the dominant paradigm, then proposing (or enabling others to propose) a principled fix. Papers that quantify failure modes with clean experiments get strong reviews even without proposing a full solution.",
      "examples": ["Reward Under Attack (2026)", "ProcessBench (ACL 2025)", "CRV (ICLR 2026 Oral)", "Risk-Controlled Lean-as-Judge (2026)"],
      "success_rate": "high"
    },
    {
      "pattern": "Automatic-Label-Synthesis-for-PRM-Training",
      "description": "Designing automated pipelines that generate step-level supervision without human annotators. Each generation improves on the prior: MC rollouts (Math-Shepherd) → formal verification (FoVer) → relative progress estimation (GenPRM). The pattern is to find a new signal source that is cheaper, more accurate, or higher coverage than previous methods.",
      "examples": ["Math-Shepherd (ACL 2024)", "FoVer (ACL 2026)", "GenPRM (AAAI 2026)"],
      "success_rate": "high"
    },
    {
      "pattern": "Risk-Controlled Selective Application",
      "description": "Instead of applying a technique universally, learning when to apply it and when to abstain. This converts an unreliable full-coverage tool into a high-precision selective tool. Requires quantifying the reliability-coverage tradeoff.",
      "examples": ["Risk-Controlled Lean-as-Judge (CovCal, 2026)", "Snell et al. difficulty-adaptive strategy (ICLR 2025)"],
      "success_rate": "medium"
    },
    {
      "pattern": "Theoretical-Framework-with-Empirical-Separation",
      "description": "Providing a formal theorem that establishes a structural gap between two approaches (not just empirical differences), then validating it experimentally. Papers with clean separation results earn top-venue orals.",
      "examples": ["Scaling Test-Time Compute Without Verification or RL (ICML 2025 Spotlight)", "ARES Hoeffding bounds (EMNLP 2025)"],
      "success_rate": "high"
    }
  ],

  "reviewer_preferences": [
    "Evaluation beyond GSM8K/MATH is now table-stakes for top venues. ProcessBench explicitly called out the limitation of easy-benchmark evaluation; ThinkPRM and GenPRM earned credibility by evaluating on GPQA-Diamond and LiveCodeBench. AAAI reviewers will expect at least one non-math domain.",
    "Data efficiency claims must be backed by explicit comparisons: ThinkPRM's 100x reduction over PRM800K and GenPRM's 23K-example training are persuasive because they include controlled ablations against data-rich baselines.",
    "Probabilistic or formal guarantees on method properties get rewarded even when practical improvements are modest. ARES's Hoeffding bounds and CovCal's risk-controlled certification transformed incremental empirical gains into publishable contributions at EMNLP and beyond.",
    "Clear taxonomy of failure modes is valued: RRM's 6-category miracle step taxonomy and ProcessBench's error categorization by difficulty level both received strong reviewer reception. Reviewers want to see that you understand the problem structure, not just the aggregate metric.",
    "Honest coverage and limitation reporting builds reviewer trust. CovCal's admission that 7B formalization achieves only 28% coverage with 43% faithfulness was a strength, not a weakness, because it motivated their risk-controlled approach. Hiding coverage gaps (as the interleaved verification paper does by not reporting per-step success rates) weakens papers.",
    "Ablation showing each component is necessary: PRoSFI's tiered reward ablation (1.0/0.3/0.1/0.0) and Snell et al.'s per-difficulty-bin strategy analysis exemplify the granular ablations that reviewers expect. A hybrid system without component-wise ablation will be rejected.",
    "Robustness to adversarial or distributional shift: Reward Under Attack showed PRMs are fluency detectors exploitable by RL. Any new PRM paper must now address adversarial robustness — formal verification provides a natural defense (Z3 proofs are immune to stylistic manipulation), and reviewers will notice if you don't make this argument."
  ],

  "field_gaps": [
    {
      "gap": "No existing system routes between formal and neural verifiers per step based on learned formalizability",
      "evidence": "FoVer uses formal-only data; GenPRM/ThinkPRM are neural-only; PRoSFI requires all steps to be formalizable; Safe's 4-state taxonomy identifies untranslatable steps but doesn't route to an alternative verifier; VeriCoT classifies steps as 'untranslatable' but discards rather than reroutes them",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "The formalizability spectrum has not been characterized or exploited for verification design",
      "evidence": "CovCal quantifies coverage at problem-level (28% at 7B) but not step-level; Safe's 4-state taxonomy hints at partial formalizability but doesn't model the spectrum; no paper measures what fraction of sub-claims within a single step are formalizable vs. not",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Formal derivability from predecessors has never been applied to miracle step detection",
      "evidence": "RRM detects miracle steps via neural rubrics; ARES checks entailment neurally; VeriCoT checks Z3 entailment but doesn't frame it as miracle-step detection or compare against RRM's taxonomy; FoVer verifies step correctness but not derivability from predecessors specifically",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Generative PRMs (GenPRM, ThinkPRM) have not been stress-tested adversarially",
      "evidence": "Reward Under Attack tested only discriminative PRMs (Skywork, Qwen). Whether generative PRMs' CoT reasoning is itself exploitable by RL-induced reward hacking is unknown. The paper explicitly notes this as an open question.",
      "difficulty": "low",
      "impact_if_solved": "medium"
    },
    {
      "gap": "Autoformalization is the bottleneck, not proof search, but no work specifically optimizes step-level (not problem-level) autoformalization",
      "evidence": "CovCal found zero Z3 timeouts — all failures were formalization failures. Safe uses few-shot prompting with REPL validation but reports no formalization success rate. VeriCoT allows 3 attempts with vocabulary extension but doesn't report attempt-level statistics. No paper trains a dedicated step-level autoformalization model.",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "No PRM handles the coverage-reliability cliff at step level",
      "evidence": "CovCal discovered the 96%→20% reliability cliff but only at problem level. At step level, the cliff is likely steeper because individual steps have less context for autoformalization. No work has characterized or mitigated this at step granularity.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Cross-domain formal verification for non-math reasoning (code correctness, scientific claims) is largely untested in the PRM context",
      "evidence": "All formal PRM papers (FoVer, Safe, PRoSFI, VeriCoT) evaluate on math/logic. ThinkPRM and GenPRM evaluate on GPQA/LiveCodeBench but without formal verification. The interleaved verification paper uses Python execution but not formal proofs for code.",
      "difficulty": "high",
      "impact_if_solved": "high"
    }
  ],

  "untried_combinations": [
    {
      "idea_sketch": "ARES's premise-configuration sampling with formal (Z3/Lean) entailment instead of neural NLI — computing τ_k by marginalizing over premise subsets but using formal derivability as the entailment function for formalizable steps",
      "from_papers": ["ARES (EMNLP 2025)", "VeriCoT (2025)", "FoVer (ACL 2026)"],
      "why_promising": "ARES's theoretical framework for isolating per-step soundness from upstream error propagation is elegant but limited by neural entailment quality. Substituting Z3 entailment for formalizable premises would give formally-grounded per-step soundness scores with Hoeffding-bound guarantees that are now backed by deterministic formal judgments rather than noisy neural ones. The combination directly addresses ARES's key limitation while preserving its statistical framework."
    },
    {
      "idea_sketch": "CRV's domain-specific computational graph signatures as the formalizability classifier — using attribution graph structure to predict whether a step is in the 'formalizable' fragment before attempting formalization",
      "from_papers": ["CRV (ICLR 2026 Oral)", "Risk-Controlled Lean-as-Judge (2026)", "FoVer (ACL 2026)"],
      "why_promising": "CRV showed that error signatures are domain-specific, implying verification must be domain-aware. If attribution graph features can predict formalizability (a lighter signal than actually attempting formalization), this would enable a zero-cost routing decision without the latency of a failed formalization attempt. CovCal's 28% coverage figure suggests most formalization attempts fail — predicting failure before attempting would save enormous compute."
    },
    {
      "idea_sketch": "GenPRM's generative verification architecture with formal tool-calling (Z3/Lean) embedded in the &lt;verify> tag instead of only Python execution — the model generates reasoning in &lt;analyze>, then decides whether to call a formal prover or write Python in &lt;verify>",
      "from_papers": ["GenPRM (AAAI 2026)", "PRoSFI (2026)", "VeriCoT (2025)"],
      "why_promising": "GenPRM already uses code execution in &lt;verify> tags but only Python. Extending this to Z3/Lean calls would let the generative PRM itself learn when formal verification is worthwhile through its own CoT reasoning, making the routing decision emergent from training rather than requiring a separate classifier. PRoSFI shows 7B models can produce Lean4 syntax; GenPRM shows generative verification scales with test-time compute."
    },
    {
      "idea_sketch": "ThinkPRM's test-time compute scaling applied to the formalizability routing decision itself — generating K parallel formalizability assessments and majority-voting on whether to route to formal vs. neural verification",
      "from_papers": ["ThinkPRM (2025)", "Safe (ACL 2025)", "Risk-Controlled Lean-as-Judge (2026)"],
      "why_promising": "CovCal showed formalization reliability has a sharp cliff. ThinkPRM showed verification quality scales with parallel sampling. Combining these: rather than making a single binary routing decision, sample multiple formalizability assessments and use the distribution to estimate confidence — route formally only when confidence exceeds a calibrated threshold. This converts the routing decision from a hard classification into a soft risk-controlled selection."
    },
    {
      "idea_sketch": "RRM's rubric synthesis pipeline with formal verification as the rubric evaluator — generate problem-specific rubrics (as RRM does), but evaluate rubric criteria via Z3/Lean derivability checks rather than neural scoring",
      "from_papers": ["Curing Miracle Steps (RRM, ACL 2026)", "VeriCoT (2025)", "FoVer (ACL 2026)"],
      "why_promising": "RRM's rubrics are powerful but neurally evaluated (Gemini-2.5-Pro dependency). Many rubric criteria ('the solution correctly applies the chain rule') are formally checkable. Replacing neural rubric evaluation with formal checks where possible would give RRM's targeted evaluation with formal guarantees, and the hybrid approach handles rubric criteria that resist formalization via the existing neural scorer."
    },
    {
      "idea_sketch": "Reward Under Attack's adversarial diagnostic framework applied to formally-grounded PRMs to empirically demonstrate formal verification's robustness advantage over neural-only PRMs",
      "from_papers": ["Reward Under Attack (2026)", "FoVer (ACL 2026)", "PRoSFI (2026)"],
      "why_promising": "Reward Under Attack showed neural PRMs are exploitable fluency detectors. A straightforward but unpublished experiment: apply the same gradient-based attacks and RL-induced hacking to a FoVer-trained or hybrid PRM. If formal derivability scores resist adversarial manipulation (as Z3 proofs should), this would be the first empirical evidence that formal grounding provides adversarial robustness for PRMs — a major selling point."
    }
  ],

  "method_building_blocks": [
    {
      "tool": "Z3 CNF-negation step checking",
      "what_it_does": "Converts a step's conclusion to CNF, negates it, adds premises, and checks satisfiability. UNSAT means the step is derivable from premises; SAT means it's not. Deterministic, fast (milliseconds for propositional/linear arithmetic), and zero-cost after setup.",
      "used_by": ["FoVer", "VeriCoT", "PRoSFI", "Interleaved Verification"],
      "could_be_applied_to": "Step-level derivability checking from predecessors for miracle step detection — checking S_i derivability from {S_1...S_{i-1}} ∪ {problem} rather than just checking S_i in isolation"
    },
    {
      "tool": "Isabelle/Lean 4 sorry-based step isolation",
      "what_it_does": "Marks all steps except the target with 'sorry' (assumed correct), then attempts to prove only the target step. This enables per-step verification without requiring an end-to-end proof.",
      "used_by": ["FoVer (Isabelle)", "Safe (Lean 4)", "PRoSFI (Lean 4)"],
      "could_be_applied_to": "Building a derivability oracle that checks whether step i follows from steps 1..i-1 by sorry-ing step i and attempting to fill it with ATPs, providing ground truth for miracle step detection"
    },
    {
      "tool": "GenPRM's Relative Progress Estimation (RPE)",
      "what_it_does": "Computes soft step labels as P_t = (MC(s_t) - MC(s_{t+1})) / MC(s_1), measuring how much each step improves the probability of reaching the correct answer. Provides continuous rather than binary supervision.",
      "used_by": ["GenPRM"],
      "could_be_applied_to": "Calibrating the formalizability router — steps with high RPE variance across MC samples may indicate miracle-step candidates where luck rather than derivability explains success"
    },
    {
      "tool": "Safe's 4-state verification taxonomy",
      "what_it_does": "Classifies each step into: no-verification-needed, failed-formalization, proved, unprovable. This provides a structured signal richer than binary correct/incorrect.",
      "used_by": ["Safe"],
      "could_be_applied_to": "Directly as the formalizability classifier's target labels — the failed-formalization vs. unprovable distinction is exactly the signal the router needs to decide formal vs. neural verification"
    },
    {
      "tool": "CovCal's coverage-reliability diagnostics",
      "what_it_does": "Measures typed coverage (fraction reaching well-formed formal statements), proved coverage (fraction with proofs), and formal margin (proved vs. unresolved weight). Calibrates acceptance thresholds to maintain reliability guarantees.",
      "used_by": ["Risk-Controlled Lean-as-Judge"],
      "could_be_applied_to": "Per-step coverage diagnostics for the formalizability router — if a step's typed coverage across multiple formalization attempts exceeds a CovCal-calibrated threshold, route to formal; otherwise route to neural"
    },
    {
      "tool": "ARES's premise-configuration Monte Carlo sampling",
      "what_it_does": "Marginalizes over exponentially many premise validity configurations via sampling, making each step's soundness score independent of upstream errors. Provides Hoeffding-bound guarantees.",
      "used_by": ["ARES"],
      "could_be_applied_to": "The hybrid PRM's aggregation layer — rather than conditioning on all prior steps' formal/neural verdicts, marginalize over their validity to prevent formal verification failures from corrupting downstream neural scores"
    },
    {
      "tool": "PRoSFI's structured formal intermediary format",
      "what_it_does": "Each step outputs a JSON block with id, dependencies (max 4), formal conclusion in Lean4 syntax, and inference rule. This makes the derivability structure explicit and machine-parseable.",
      "used_by": ["PRoSFI"],
      "could_be_applied_to": "As the router's input representation — if the generator produces structured intermediaries, the formalizability classifier can operate on the formal conclusion field's parsability rather than attempting full formalization"
    },
    {
      "tool": "RRM's miracle step taxonomy (6 categories)",
      "what_it_does": "Classifies false-positive reasoning errors into: inductive overgeneralization, outcome irrelevance, neglected preconditions, unverified assumptions, numerical coincidence, and miracle steps proper. Provides granular diagnostic labels.",
      "used_by": ["Curing Miracle Steps (RRM)"],
      "could_be_applied_to": "Evaluation benchmark design — the hybrid PRM should be evaluated on each of the 6 false-positive categories separately to show which categories benefit from formal verification vs. neural verification, justifying the routing approach"
    }
  ],

  "common_pitfalls": [
    "Evaluating only on GSM8K and MATH. ProcessBench showed that PRMs that look strong on MATH-level problems collapse on competition/Olympiad difficulty. CovCal showed coverage drops catastrophically on harder problems. Any new PRM paper must include ProcessBench and at least one non-math benchmark (GPQA, LiveCodeBench) or reviewers will question generality — especially at AAAI which values breadth.",
    "Hiding or ignoring formalization coverage limits. CovCal found 28% coverage at 7B with 43% faithfulness. Safe's Lean 4 pipeline struggles with geometry and combinatorics. The interleaved verification paper doesn't report per-step formalization success rates, which weakens their claims. Be transparent about coverage: if your formal verifier covers 40-60% of steps, report this prominently and show the neural fallback is essential — honesty about limitations strengthens the paper.",
    "Conflating step correctness with step derivability. FoVer checks whether step i is correct in isolation; ARES checks whether step i follows from predecessors. These are different properties — a step can be correct but not derivable from prior steps (this is literally the definition of a miracle step). Any miracle-step detection system must check derivability, not just correctness.",
    "Treating the 'naive timeout fallback' baseline as obviously inferior without empirically verifying. The seed direction's self-check identifies that running Z3 on every step with neural fallback on timeout gets ~60% of the routing benefit. If the learned router doesn't significantly outperform this baseline, the paper's contribution collapses. The router must demonstrably beat the naive fallback on partially-formalizable steps specifically.",
    "Ignoring the autoformalization bottleneck. CovCal found zero Z3 timeouts — all failures were formalization failures, not prover failures. Investing in better provers or longer timeouts while using weak autoformalization is wasted effort. The critical path is formalization quality, and 7B models produce only 28% coverage. Either use a strong formalizer (70B as FoVer does) or accept lower coverage and route accordingly.",
    "Not comparing against ARES. ARES provides the most directly comparable baseline for step-derivability checking (neural entailment from predecessors). Any formal-derivability system that doesn't show improvement over ARES's neural entailment will face 'why not just use ARES?' objections. The comparison should be on miracle step detection specifically, where formal derivability's binary judgments should outperform probabilistic neural entailment.",
    "Overloading the contribution with too many novelties. FoVer succeeds with one clean idea (formal labels transfer to informal domains). GenPRM succeeds with one clean idea (generative verification with test-time scaling). Papers that try to simultaneously introduce a formalizability classifier, a routing mechanism, a new PRM architecture, and a miracle step benchmark risk 'incremental combination' criticism. Lead with one sharp contribution and treat others as supporting experiments.",
    "Underestimating the RL-induced reward hacking risk. Reward Under Attack showed that RL policies exploit PRMs with >0.9 reward at <4% accuracy. If the hybrid PRM is used as an RL reward, the RL policy may learn to generate steps that are trivially formalizable (always routes to formal) or intentionally unformalizable (always routes to neural, which is exploitable). The routing mechanism itself becomes an attack surface."
  ],

  "field_trajectory": "The field is converging on three macro-directions that will define the 2026-2027 publication landscape. First, the formalization of verification: the arc from Math-Shepherd (noisy MC labels) through FoVer (formal labels) to the proposed hybrid routing represents a progressive tightening of the verification signal from probabilistic to deterministic, with the key remaining challenge being coverage — extending formal verification beyond the ~40-60% of steps that current tools can handle. CovCal's coverage-reliability cliff quantification is the critical finding here: the field now knows that formal verification is extremely reliable when it works but catastrophically unreliable at low coverage, which mandates either better autoformalization or intelligent routing. Second, test-time compute scaling of verifiers: GenPRM and ThinkPRM showed that verifiers themselves benefit from scaling inference compute (majority voting, longer thinking budgets), and the ICML 2025 spotlight proved this advantage is structural (√H separation). The next step is scaling formal verification compute at test time — running multiple formalization attempts, multiple proof strategies, and multiple neural verification chains in parallel, then aggregating. Third, adversarial robustness as a first-class requirement: Reward Under Attack transformed PRM robustness from an afterthought to a publication-worthy concern. Formal verification provides a natural defense (Z3 proofs are immune to fluency manipulation), but the routing mechanism introduces new attack surfaces. The 2026-2027 papers that will have the most impact are those that demonstrate formally-grounded PRMs that are both more accurate and more robust than neural-only alternatives, evaluated across difficulty levels and domains, with honest coverage reporting.",

  "meta_advice": "If I were advising a PhD student to write a strong AAAI 2027 paper in this area, I would say: lead with the miracle step detection angle, not the routing mechanism. The routing is your technical contribution, but the story reviewers will remember is 'we can now formally prove when an LLM's reasoning step doesn't follow from its predecessors.' Frame the paper as solving the miracle step problem (well-defined by RRM, ACL 2026) using formal derivability (well-motivated by VeriCoT's Z3 entailment and FoVer's infrastructure), with the hybrid router as the engineering innovation that makes formal derivability practical despite limited coverage. Your sharpest empirical result should be a head-to-head comparison on RRM's miracle step taxonomy showing formal derivability catches categories that neural rubrics miss — especially numerical coincidence and unverified assumptions, which have crisp formal counterparts. Use FoVer's public codebase and data as your starting point (don't rebuild the formal infrastructure), GenPRM-7B as your neural verifier backbone (it's the AAAI 2026 SOTA and reviewers will know it), and evaluate on ProcessBench (step-level, competition difficulty), GPQA-Diamond (science domain), and LiveCodeBench (code domain) — this trifecta shows generality beyond math. For the formalizability classifier, start with the naive timeout baseline and show your learned router provides statistically significant gains specifically on partially-formalizable steps (the 'grey zone' where neither pure formal nor pure neural is optimal). Keep compute under 200 H100-hours and report it prominently — AAAI values academic reproducibility. Most importantly, be honest about coverage: report your formalization success rate per domain, show the coverage-reliability curve à la CovCal, and demonstrate that the neural fallback is not just a safety net but essential for 40-50% of steps. The paper that admits formal verification covers 55% of steps and shows the hybrid system outperforms both formal-only and neural-only on the remaining 45% will be far more convincing than one that inflates coverage claims."
}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cfb1f07-5dd0-4c05-bada-a5ea0e990962",
  "isSidechain": false,
  "requestId": "req_011CbWaG1a6TdkTaMZ9AwqWY",
  "type": "assistant",
  "uuid": "e09fc6d8-bd02-4af3-befe-33c46652c520",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "7cded7ed-6407-48ab-84e6-3517a2852229",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011jUg9A2TVWuGzEDT3T3zLN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13066,
      "cache_read_input_tokens": 11014,
      "output_tokens": 7438,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13066,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 7438,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 13066,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13066
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
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-29 (UTC).**  ## Research area: Target: AAAI 2026 (or AAAI 2027 if d…",
  "leafUuid": "e09fc6d8-bd02-4af3-befe-33c46652c520",
  "sessionId": "7cded7ed-6407-48ab-84e6-3517a2852229"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Hybrid formal-neural PRM for miracle step detection",
  "sessionId": "7cded7ed-6407-48ab-84e6-3517a2852229"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-29 (UTC).**  ## Research area: Target: AAAI 2026 (or AAAI 2027 if d…",
  "leafUuid": "e09fc6d8-bd02-4af3-befe-33c46652c520",
  "sessionId": "7cded7ed-6407-48ab-84e6-3517a2852229"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Hybrid formal-neural PRM for miracle step detection",
  "sessionId": "7cded7ed-6407-48ab-84e6-3517a2852229"
}
```

---
