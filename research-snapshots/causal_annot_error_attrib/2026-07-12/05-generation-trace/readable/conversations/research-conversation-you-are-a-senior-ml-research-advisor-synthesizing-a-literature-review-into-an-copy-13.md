# Research conversation: You are a senior ML research advisor synthesizing a literature review into an actionable research strategy. **Today's da

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/733f9e07-4f23-4518-9a71-bb860175df75.jsonl`
- **Structured JSON:** [`472c8911a0c2242f36fb.json`](../../sessions/47/472c8911a0c2242f36fb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-29T05:33:26.273Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-29T05:33:26.273Z",
  "sessionId": "733f9e07-4f23-4518-9a71-bb860175df75",
  "content": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.\n\n**Today's date: 2026-05-29 (UTC).**\n\n## Research area: Target: AAAI 2026 (or AAAI 2027 if deadline has passed)\nTrack: Knowledge Representation and Reasoning / Safe and Robust AI\n\nDirection: Build a hybrid PRM that learns to route each reasoning step to either a formal verifier (Z3/Lean 4) or a neural verifier (GenPRM-style) based on a learned formalizability score, then apply this routing framework specifically to detect miracle steps — unjustified logical leaps where the conclusion is correct but not derivable from preceding steps. The formal verifier provides binary derivability judgments for formalizable steps while the neural verifier handles non-formalizable steps, with the router trained on FoVer-style formally verified data as ground truth.\n\nSeed Papers:\n- FoVer (Kamoi et al., ACL 2026 Findings / ICLR 2026) — provides the formal verification infrastructure (Z3 + Isabelle) for PRM training data synthesis; our direct foundation\n- Curing Miracle Steps with Rubric Rewards (Yuan et al., 2025) — taxonomizes the miracle step problem and proposes RRM; our work replaces neural rubrics with formal derivability\n- ARES (You & Xue, EMNLP 2025) — checks step entailment from predecessors probabilistically; our key differentiator is using formal (not neural) derivability checking\n- PRoSFI (2026, under review ICLR 2026) — uses formal intermediaries for process rewards; doesn't route between formal/neural or target miracle steps specifically\n- Safe (ACL 2025) — Lean 4 step-level verification; provides formalization pipeline but doesn't train PRMs or detect miracle steps\n- GenPRM (Liu et al., AAAI 2026) — SOTA generative neural PRM; serves as our neural verifier baseline\n- Typed Chain-of-Thought (ICLR 2026 submission) — Curry-Howard framework for reasoning verification; provides theoretical motivation for our type-checking-as-derivability angle\n\nKnown Gaps:\n- No existing system routes between formal and neural verifiers per step based on a learned formalizability classifier — all current approaches are formal-only or neural-only\n- No work applies formal proof-assistant derivability checking to detect miracle steps — ARES checks entailment neurally, RRM uses neural rubrics, but formal derivability from predecessors is untested\n- The formalizability spectrum (fully formalizable → partially → not at all) has not been characterized or exploited for PRM design\n\nTheoretical Anchor: A reasoning step S_i is justified iff S_i is formally derivable from {S_1, ..., S_{i-1}} ∪ {problem statement} under known inference rules. Steps where formal derivation fails or times out are miracle-step candidates. The formalizability score (proportion of a step's sub-claims that can be expressed in SMT/HOL) determines router behavior. This connects PRMs to classical proof theory: reward = derivability.\n\nConstraints:\n- Compute: ≤200 H100-hours (router ~10h, PRM fine-tuning at 7B ~50h, formal verification CPU-bound, evaluation ~40h)\n- Must clearly differentiate from FoVer (training-only formal), PRoSFI (no routing), ARES (neural-only entailment), and Safe (no PRM training)\n- Target 7B scale for academic tractability\n- Use FoVer's public codebase and data as starting infrastructure\n\nQuality Self-Checks:\n- [x] Core insight: A PRM that knows which steps it can formally verify and which it must judge neurally will catch miracle steps that pure neural PRMs miss.\n- [x] Why not obvious: Routing requires solving the meta-problem of formalizability classification, which no one has tackled because formal and neural verification communities don't overlap. PRoSFI and Safe avoid routing by requiring ALL steps to be formalizable.\n- [x] Baseline fear test: A simple baseline (run Z3 on every step, fall back to neural on timeout) would get ~60% of the routing benefit — the learned router must demonstrably outperform this naive fallback on partial-formalizability cases.\n- [x] Information exploited: The formalizability structure of each step — specifically which sub-claims are expressible in SMT logic and which require informal reasoning — is information that no existing PRM uses.\n\nAvoid:\n- Training only on formally verifiable data (that's FoVer — must show value of the hybrid approach on non-formalizable steps)\n- Claiming formal verification solves everything (formalization success rate will be 40-60% — must be honest about coverage limits and show the neural fallback is essential)\n- Evaluating only on math (AAAI values generality — include code via LiveCodeBench and science via GPQA)\n- Ignoring the ARES comparison (must show formal derivability checking outperforms neural entailment checking on miracle step detection)\n\n## Paper analyses (21 papers)\n\n[\n  {\n    \"title\": \"Efficient PRM Training Data Synthesis via Formal Verification (FoVer)\",\n    \"venue\": \"ACL 2026 Findings (withdrawn from ICLR 2026)\",\n    \"problem_identification\": \"PRM training requires expensive human step-level annotation (~800K labels in PRM800K) or costly Monte Carlo LLM sampling. The authors identified that formal verification tools already produce binary correctness judgments that could replace human labelers entirely, yet no one had connected the formal verification and PRM training communities.\",\n    \"key_insight\": \"Step-level correctness labels produced by Z3 (for logic) and Isabelle (for theorem proving) transfer from formal to informal reasoning domains, enabling PRMs trained on purely formal data to improve on NLI, BBH, and math benchmarks they never saw.\",\n    \"innovation_type\": \"cross_domain\",\n    \"method_summary\": \"FoVer has LLMs (Llama 3.1 8B, Qwen 2.5 7B) generate step-by-step solutions for formal tasks. For logic (FLDx2), Z3 checks each step's validity given premises independently. For theorem proving (GSM8K variants), Isabelle verifies each step using a `sorry`-insertion trick that isolates individual steps. The resulting FoVer-40K dataset (20K logic + 20K theorem steps) trains PRMs via standard cross-entropy on binary correct/incorrect tokens. Errors are naturally occurring from LLM generation, not injected.\",\n    \"limitations_and_open_questions\": \"Computationally intensive (weeks on multiple servers for Isabelle); limited to 8B models; PRMs become overly strict on informal reasoning (penalizing valid rounding). Critical open question: can the formal-to-informal transfer be improved by mixing formal and informal training data?\",\n    \"building_blocks\": [\n      \"FoVer-40K dataset with verified step labels\",\n      \"Z3 step-independent verification pipeline\",\n      \"Isabelle sorry-insertion trick for step isolation\",\n      \"Public codebase (GitHub psunlpgroup/FoVer)\",\n      \"Formal-to-informal transfer methodology\"\n    ],\n    \"relevance_to_seed\": \"Direct foundation — provides the formal verification infrastructure, public codebase, and training data synthesis pipeline that our hybrid router would build upon, with our work extending it by adding neural fallback for non-formalizable steps.\"\n  },\n  {\n    \"title\": \"HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs\",\n    \"venue\": \"ICML 2026 (Poster)\",\n    \"problem_identification\": \"Informal LLM reasoning is flexible but accumulates logical drift over long chains; formal theorem proving is rigid but correct. No existing system interleaved them at inference time with feedback loops, forcing a binary choice between flexibility and rigor.\",\n    \"key_insight\": \"Intermediate formal verification during inference (not just at training time) prevents reasoning drift while preserving exploratory freedom, and a memory module across verification cycles avoids redundant exploration — achieving 67% accuracy gains with 80% fewer FLOPs.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"HERMES comprises four modules: (1) an LLM generating informal reasoning steps, (2) a Translator converting them to Lean 4 code, (3) a Prover validating via Lean 4 REPL returning True/False signals, and (4) a Feedback module routing verification results back to guide subsequent reasoning. A Memory module tracks explored paths, successful strategies, and failures. A verification scheduler parallelizes Lean compilation for efficiency. The cycle repeats until verification succeeds or resource limits are hit.\",\n    \"limitations_and_open_questions\": \"Restricted to problems expressible in Lean 4; translation quality bottlenecks the entire pipeline. Does not train PRMs or produce reusable reward signals — verification is inference-only. How would this interleaving degrade on problems with low formalizability?\",\n    \"building_blocks\": [\n      \"Lean 4 REPL integration with Python\",\n      \"Interleaved informal/formal reasoning loop\",\n      \"Memory module for proof continuity\",\n      \"Verification scheduler for parallel Lean compilation\"\n    ],\n    \"relevance_to_seed\": \"Validates that hybrid formal/neural reasoning is viable at scale; our router operates at a different level (PRM training vs. inference-time verification), but HERMES's translator and Lean 4 integration patterns are directly reusable for the formal verifier component.\"\n  },\n  {\n    \"title\": \"Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries (PRoSFI)\",\n    \"venue\": \"arXiv 2026 (under review)\",\n    \"problem_identification\": \"Outcome rewards mask flawed intermediate steps (correct answers via wrong reasoning), but generating full formal proofs is intractable for 7B models. The gap is a lightweight formal representation that a small model can produce and a prover can verify, without requiring complete proof generation.\",\n    \"key_insight\": \"Structured formal intermediaries — lightweight JSON representations containing (id, dependencies, conclusion, inference_rule) per step — bridge the formalization gap, enabling formal verification without full proof generation, and can drive GRPO training via tiered process rewards.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"The model generates natural language reasoning interleaved with structured formal intermediaries in a single forward pass. Each intermediary specifies dependencies (≤5 prior steps), a conclusion in formal language, and the inference rule applied (Modus Ponens, Hypothetical Syllogism, etc.). A formal prover verifies each step independently. GRPO training uses tiered rewards: R=1.0 (correct + all verified), R=0.3 (correct + some unverified), R=0.1 (format OK + wrong answer), R=0.0 (format errors). Trained on ProverQA (769 instances).\",\n    \"limitations_and_open_questions\": \"Limited to first-order logic; no mechanism for unformalizable steps (all steps must produce intermediaries). Binary pass/fail verification loses granularity. Soundness evaluated by GPT-OSS-120B, not human judges. How would this extend beyond logic to math or science?\",\n    \"building_blocks\": [\n      \"Structured formal intermediary format\",\n      \"Tiered GRPO reward scheme (1.0/0.3/0.1/0.0)\",\n      \"ProverQA benchmark suite\",\n      \"Single-pass NL + formal generation approach\"\n    ],\n    \"relevance_to_seed\": \"Closest methodological competitor — our key differentiator is the learned router that handles non-formalizable steps neurally rather than requiring ALL steps to produce formal intermediaries, plus explicit miracle step targeting.\"\n  },\n  {\n    \"title\": \"Let's Verify Step by Step\",\n    \"venue\": \"ICLR 2024\",\n    \"problem_identification\": \"Outcome-supervised reward models (ORMs) cannot localize errors in reasoning chains, leading to reward hacking where models get right answers via wrong reasoning. The authors identified that step-level supervision existed in education/tutoring but had never been systematically compared to outcome supervision for LLM training at scale.\",\n    \"key_insight\": \"Process supervision (step-level human feedback with positive/neutral/negative labels) provides precise credit assignment that significantly outperforms outcome supervision, and an active learning strategy selecting solutions most likely to deceive the current PRM yields 2.6× data efficiency.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"Human labelers annotate each step as positive (correct, progresses), neutral (correct, no progress), or negative (incorrect) without reference solutions but with access to ground-truth answers. PRM800K contains 800K such labels across 75K solution traces for MATH problems. PRMs are trained on these labels and used for best-of-N selection: generate N candidate solutions, score each by the minimum step-level PRM score, select the highest-scoring solution. Active learning selects solutions where the current PRM is most uncertain.\",\n    \"limitations_and_open_questions\": \"Requires expensive human annotation ($$$); limited to MATH domain; labeler agreement rates not thoroughly analyzed. The neutral category is underspecified. Does process supervision's advantage hold for non-mathematical reasoning? What happens at larger model scales?\",\n    \"building_blocks\": [\n      \"PRM800K dataset (800K step labels)\",\n      \"Best-of-N selection via minimum step score\",\n      \"Active learning for PRM data efficiency\",\n      \"Process vs. outcome supervision methodology\",\n      \"Positive/neutral/negative labeling protocol\"\n    ],\n    \"relevance_to_seed\": \"Foundational paradigm paper — defines the PRM framework our work extends; PRM800K's labeling gaps (expensive, domain-limited, no formal grounding) are exactly what FoVer and our hybrid router aim to solve.\"\n  },\n  {\n    \"title\": \"Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving (MATH-VF)\",\n    \"venue\": \"arXiv 2025\",\n    \"problem_identification\": \"Existing PRMs require expensive training and can't verify closed-source model outputs. No training-free framework combined symbolic computation (CAS) with logical verification (SMT) for step-level mathematical verification, despite both tools being mature.\",\n    \"key_insight\": \"A lightweight custom formal language (SimpleMath, extending first-order logic with mathematical constants/syntactic sugar) enables >90% formalization success on MATH500, allowing a training-free Formalizer+Critic pipeline using SymPy and Z3 to verify individual steps with corrective feedback.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"The Formalizer uses few-shot LLM prompting to translate NL solutions into SimpleMath, a readable formal language. The Critic evaluates each step as premises⊢conclusion using two tools: SymPy (CAS) for algebraic/numerical verification and Z3 (SMT) for logical constraint checking. When errors are found, corrective feedback guides solution refinement in iterative cycles. Exploits sparsity in solution dependency graphs, reducing input from O(n²) to O(n×M) where M≤4.\",\n    \"limitations_and_open_questions\": \"Formalization syntax errors cause verification failures; cannot assess step effectiveness (only correctness); trails fine-tuned PRMs (74.1 vs 78.3 F1 on ProcessBench). SimpleMath is limited to math — how would it extend to logic or science domains?\",\n    \"building_blocks\": [\n      \"SimpleMath formal language specification\",\n      \"SymPy + Z3 dual-tool verification pipeline\",\n      \"Training-free verification framework\",\n      \"Corrective feedback loop for refinement\",\n      \"Dependency graph sparsity optimization\"\n    ],\n    \"relevance_to_seed\": \"Directly relevant architecture for our Z3 verification module — SimpleMath's formalization approach and the CAS+SMT dual-tool pattern can be adopted as the formal verifier component, with our router deciding which steps to send through this pipeline vs. neural verification.\"\n  },\n  {\n    \"title\": \"Evaluating Step-by-step Reasoning Traces: A Survey\",\n    \"venue\": \"EMNLP 2025 Findings\",\n    \"problem_identification\": \"Evaluation practices for reasoning traces are highly inconsistent across the field — different papers measure different properties using incompatible metrics, creating fragmented progress. No unified framework existed to categorize what 'good reasoning' means at the step level.\",\n    \"key_insight\": \"Four complementary evaluation dimensions — Factuality (grounded in sources), Validity (logically follows from predecessors), Coherence (connects to subsequent steps), and Utility (progresses toward answer) — capture distinct failure modes, and combining Validity+Utility substantially outperforms either alone for PRM training.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"The survey taxonomizes step-level evaluation into four categories with subcategories: Factuality (groundedness, parametric knowledge), Validity (entailment-based, correctness-based), Coherence (flow, precondition satisfaction), and Utility (progress, value function). Reviews 8 evaluator types (rule-based, uncertainty, cross-encoder, sequence classifier, critic model, generative verifier, etc.) across datasets including PRM800K, ProcessBench, Math-Shepherd, and REVEAL. Identifies five critical gaps including absence of formal verification methods and inability to handle long traces.\",\n    \"limitations_and_open_questions\": \"Survey scope limited to 2022-2025; no experiments conducted to validate the taxonomy empirically. The formal verification gap they identify (symbolic grounding remains unexplored) is exactly the space FoVer and our work address. How should formalizability be added as a fifth dimension?\",\n    \"building_blocks\": [\n      \"Four-category evaluation taxonomy\",\n      \"Eight evaluator type classifications\",\n      \"Validity+Utility complementarity finding\",\n      \"Formal verification as identified gap\",\n      \"Partial-context evaluation strategy\"\n    ],\n    \"relevance_to_seed\": \"Provides the evaluation framework for our work — our formalizability score adds a fifth dimension to their taxonomy, and their finding that validity (our formal verifier's domain) complements utility (our neural verifier's domain) directly motivates the hybrid routing approach.\"\n  },\n  {\n    \"title\": \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\",\n    \"venue\": \"AAAI 2026\",\n    \"problem_identification\": \"Existing PRMs are classification-based scalar predictors that cannot leverage LLMs' generative abilities or scale test-time compute. The authors identified that discriminative PRM formulations create a ceiling that more computation cannot lift.\",\n    \"key_insight\": \"Reframing process reward modeling as a generative reasoning task — where the PRM produces explicit Chain-of-Thought analysis with executable code verification before judging each step — unlocks test-time compute scaling via majority voting over generated rationales.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"GenPRM uses a three-stage pipeline: (1) Monte Carlo estimation generates step-level pass rates, then Relative Progress Estimation (RPE) refines labels by comparing pass-rate changes between consecutive steps — a step is positive if it increases the probability of reaching the correct answer. (2) A rationale synthesis framework prompts an LLM to generate CoT analysis within &lt;analyze> tags plus executable Python code within &lt;verify> tags; code execution feedback is concatenated for self-correction. (3) The model is fine-tuned on 23K MATH-derived examples to generate reasoning-then-judgment. At inference, N verification paths are sampled and majority-voted, enabling 1.5B to outperform GPT-4o on ProcessBench.\",\n    \"limitations_and_open_questions\": \"RPE inherits Monte Carlo estimation noise; code verification only catches computationally verifiable errors (not logical leaps or unjustified assumptions). Unclear how RPE handles steps that are wrong but accidentally lead to correct answers.\",\n    \"building_blocks\": [\n      \"Relative Progress Estimation for step labeling\",\n      \"Rationale synthesis with code verification\",\n      \"Test-time compute scaling via majority voting for PRMs\",\n      \"ProcessBench evaluation protocol\",\n      \"23K training data from MATH\"\n    ],\n    \"relevance_to_seed\": \"Serves as the neural verifier baseline in our hybrid system — GenPRM's generative verification handles the non-formalizable steps that the formal verifier cannot reach, and its RPE labels provide comparison ground truth for our routing-based approach.\"\n  },\n  {\n    \"title\": \"VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning\",\n    \"venue\": \"arXiv 2026\",\n    \"problem_identification\": \"LLM outputs mix logically verifiable claims with commonsense assertions, yet existing verification systems apply a single strategy uniformly. The authors recognized that claim type diversity demands heterogeneous verification routing.\",\n    \"key_insight\": \"Semantic routing — classifying each atomic claim by type (logical/mathematical/temporal vs. commonsense/vague/probabilistic) and dispatching to symbolic SMT solvers or neural LLM ensembles accordingly — enables formal guarantees where possible and soft consensus elsewhere.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"VERGE decomposes LLM outputs into atomic claims, autoformalizes them into SMT-LIB2 (QF_UF/QF_LIA fragments) with K=3 candidate formulas per claim, and enforces semantic equivalence via bidirectional entailment checking. The router (94% accuracy, F1=0.93/0.95) dispatches SMT-amenable claims to Z3 and soft claims to neural ensembles. Error localization uses Minimal Correction Subsets (MCS) via greedy O(n×SAT) approximation to pinpoint exactly which claims to revise. Iterative refinement continues until aggregated score ≥0.75 and joint satisfiability holds.\",\n    \"limitations_and_open_questions\": \"Routing is rule-based on claim type taxonomy rather than learned from data — unclear if a learned router would outperform. Applied only to inference-time refinement, not PRM training. Autoformalization into QF fragments limits expressiveness for complex mathematical reasoning.\",\n    \"building_blocks\": [\n      \"Semantic claim-type routing taxonomy\",\n      \"MCS-based error localization\",\n      \"Multi-candidate autoformalization with semantic equivalence consensus\",\n      \"Iterative refinement with convergence criteria\"\n    ],\n    \"relevance_to_seed\": \"Most directly related to our routing mechanism — VERGE proves semantic routing between formal and neural verifiers works (18.7% uplift), but routes for inference refinement rather than PRM training, and uses rule-based rather than learned routing.\"\n  },\n  {\n    \"title\": \"VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks\",\n    \"venue\": \"ICLR 2026 Poster\",\n    \"problem_identification\": \"CoT reasoning steps lack formal verification — errors propagate unchecked because no system grounds each step's logical dependencies or verifies entailment from predecessors. The gap between neural generation and formal validity was unexploited for training.\",\n    \"key_insight\": \"Formalizing each CoT step into FOL with explicitly grounded premises (from context, commonsense, or prior steps) enables Z3-based entailment/contradiction/consistency checking that simultaneously serves as verification signal AND training reward for SFT and DPO.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"VeriCoT uses two-stage autoformalization: first generating SMT-LIB formulas reusing existing vocabulary, then creating new declarations for inexpressible segments (up to 3 iterations). Each step's premises are identified and categorized by source (context vs. commonsense). Z3 checks three relations: entailment (step follows), contradiction (step conflicts), or consistency (step is contingent, needing premise support). Verification signals feed SFT (training on verified CoTs, +3% accuracy) and DPO (verified=chosen, failed=rejected, +18.4% relative verification improvement). Inference-time self-reflection on failures yields +12.3% absolute gains.\",\n    \"limitations_and_open_questions\": \"Autoformalization success rate is unstated but likely limited — the untranslatable category exists but its frequency isn't characterized. No mechanism for routing around formalization failures; steps that can't be formalized are simply marked. Tested only on ProofWriter, LegalBench, BioASQ — no math benchmarks.\",\n    \"building_blocks\": [\n      \"CoT-to-FOL two-stage autoformalization\",\n      \"Premise grounding and categorization\",\n      \"Z3 entailment/contradiction/consistency triple-check\",\n      \"Verification-as-reward for SFT and DPO training\"\n    ],\n    \"relevance_to_seed\": \"Directly validates our core approach — verification signals from formal checking can train better models via SFT/DPO. The untranslatable step category and premise grounding methodology inform our formalizability classifier design. Multi-domain evaluation (legal, biomedical) supports AAAI generality.\"\n  },\n  {\n    \"title\": \"ProcessBench: Identifying Process Errors in Mathematical Reasoning\",\n    \"venue\": \"ACL 2025\",\n    \"problem_identification\": \"No rigorous benchmark existed for evaluating step-level error localization in mathematical reasoning — prior work used binary correctness or synthetic errors. The authors found that existing PRMs, despite training on process supervision, fail to generalize to competition-level problems.\",\n    \"key_insight\": \"Error localization (identifying the earliest erroneous step) is fundamentally harder than binary solution correctness, and existing PRMs trained on GSM8K/MATH-level data catastrophically fail on harder problems — revealing that scalar process reward models don't truly understand step validity.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"ProcessBench collects problems from four difficulty tiers (GSM8K, MATH, OlympiadBench, Omni-MATH) with solutions from 12 diverse generators (Qwen/LLaMA series). Steps are reformatted via Qwen2.5-72B-Instruct for consistent granularity, then expert-annotated for the earliest erroneous step. The benchmark evaluates PRMs (scoring each step) and critic models (prompted step-by-step critique), revealing that prompted critics like QwQ-32B-Preview match GPT-4o while trained PRMs underperform both on hard problems.\",\n    \"limitations_and_open_questions\": \"Math-only domain limits generality claims. Error taxonomy is implicit — doesn't distinguish miracle steps from calculation errors or logical fallacies. Annotation identifies location but not error type, missing an opportunity to study which errors PRMs can vs. cannot catch.\",\n    \"building_blocks\": [\n      \"3,400 expert-annotated error localization test cases\",\n      \"Multi-difficulty evaluation protocol (GSM8K through Olympiad)\",\n      \"PRM vs. critic model comparison framework\",\n      \"Step reformatting methodology for consistent granularity\"\n    ],\n    \"relevance_to_seed\": \"Primary evaluation benchmark — our hybrid PRM must be tested here. The finding that PRMs fail on hard problems motivates formal verification: hard problems likely contain more miracle steps that neural-only PRMs miss. Lack of error type taxonomy creates an opportunity for our miracle-step-specific evaluation.\"\n  },\n  {\n    \"title\": \"Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning\",\n    \"venue\": \"arXiv 2026\",\n    \"problem_identification\": \"Lean-as-Judge is increasingly used to verify math answers, but its signal is partial and unreliable: a 7B autoformalizer proves only 28% of problems, and manual audit reveals only ~43% of those proofs are faithful to the original problem statement. No principled framework existed for knowing when to trust formal verification.\",\n    \"key_insight\": \"Formal verification's value is bounded by both coverage (what fraction of problems can be formalized and proved) and faithfulness (whether the proof actually captures the intended claim) — and a risk-controlled selector over Lean-trace diagnostics can certify when formal judgments are trustworthy.\",\n    \"innovation_type\": \"analysis\",\n    \"method_summary\": \"The pipeline autoformalizes via Qwen2.5-Coder-7B to Lean 4, generating four artifacts per answer class with error-feedback repair. CovCal selects based on four diagnostics: typed coverage, proved coverage, unresolved rival mass, and formal margin. Two risk regimes are compared: Bonferroni (union-bound over 125-cell threshold grid, conservative) and dev-then-cal (select threshold on dev split, evaluate once on cal). A specialized Goedel-Prover-V2-8B achieves 79% coverage vs. 28% baseline, enabling certification of 17/20 partitions at ~48% acceptance with 0.98 accuracy.\",\n    \"limitations_and_open_questions\": \"Faithfulness gap (43%) is alarming and unresolved — structural proofs often assert true-but-irrelevant claims. Specialization > scale (8B specialized beats 32B general) suggests formalization quality is a training data problem. Step-level analysis is absent — all verification is at the solution level.\",\n    \"building_blocks\": [\n      \"Formalizability coverage quantification (28-79%)\",\n      \"Proof faithfulness audit methodology\",\n      \"CovCal risk-controlled selector with Lean-trace diagnostics\",\n      \"Four-diagnostic acceptance criteria\",\n      \"Evidence that specialization outperforms scale for autoformalization\"\n    ],\n    \"relevance_to_seed\": \"Directly validates our router's necessity — formal verification alone covers 28-79% with questionable faithfulness, empirically proving that a hybrid approach with neural fallback is essential. The coverage diagnostics inform our formalizability score design, and the faithfulness findings motivate our step-level (not solution-level) verification approach.\"\n  },\n  {\n    \"title\": \"Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards\",\n    \"venue\": \"ACL 2026 Main\",\n    \"problem_identification\": \"Through systematic human verification of LLM math solutions, discovered that correct-answer solutions frequently contain unjustified logical leaps ('miracle steps'), enabling reward hacking that inflates Pass@N metrics. No prior taxonomy of these process-level failure modes existed.\",\n    \"key_insight\": \"Problem-specific rubrics that evaluate entire reasoning trajectories against structured criteria outperform both outcome-only rewards and generic step-level PRMs for detecting process flaws, because rubrics encode what valid reasoning *should* look like per problem.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Defines 6 false-positive failure modes (inductive overgeneralization, outcome irrelevance, neglected operational preconditions, unverified assumptions, numerical coincidence, miracle steps). Implements a 3-phase pipeline: (1) Gemini-2.5-Pro synthesizes problem-specific rubrics covering strategy/computation/logic/conclusion, (2) scoring data pairs problems+rubrics with 0-10 rated responses, (3) Qwen3-4B is fine-tuned via SFT+PPO to predict rubric-grounded scores. The RRM-trained policy achieves Verified Pass@1024 of 62.6% on AIME2024 (vs 26.7% outcome-only) and reduces miracle steps by 71%.\",\n    \"limitations_and_open_questions\": \"Rubric generation depends on proprietary Gemini-2.5-Pro (reproducibility concern); 29% of miracle steps persist; rubrics are still neural artifacts — can formal derivability checking close the remaining gap? The 0-10 scoring granularity vs binary formal verification tradeoff is unexplored.\",\n    \"building_blocks\": [\n      \"6-type miracle step taxonomy\",\n      \"Rubric synthesis pipeline\",\n      \"Verified Pass@N evaluation protocol\",\n      \"RRM architecture (SFT+PPO on rubric scores)\"\n    ],\n    \"relevance_to_seed\": \"Directly defines the miracle step problem our system targets; the 71% reduction via neural rubrics sets the quantitative bar our formal derivability approach must surpass.\"\n  },\n  {\n    \"title\": \"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification\",\n    \"venue\": \"ACL 2025 Main\",\n    \"problem_identification\": \"PRMs use opaque neural scoring without interpretable evidence of step correctness; no prior work applied formal mathematical verification at the individual reasoning step level (previous auto-formalization targeted whole problems, not steps).\",\n    \"key_insight\": \"Auto-formalizing individual reasoning steps (not whole problems) into Lean 4 theorem statements enables interpretable, mechanically verifiable correctness judgments that are complementary to — not redundant with — neural PRM scores.\",\n    \"innovation_type\": \"cross_domain\",\n    \"method_summary\": \"Each reasoning step is auto-formalized via GPT-4o into a Lean 4 theorem (taking prior conclusions as premises, current assertion as goal), then proved using DeepSeek-Prover-V1.5 (16-sample budget). Steps receive one of 4 states: no-verification-needed, formalization-failed, proved, unprovable. State sequences are aggregated by a minimal 2-layer LSTM into a trajectory quality score. This formal score is combined with PRM scores for Best-of-N reranking, yielding 2-3% gains over PRM+ORM ensembles on MATH-500.\",\n    \"limitations_and_open_questions\": \"4-8× computational overhead vs baseline PRMs; geometry/combinatorics formalization limited (72% vs 82% proof rate); no learned routing — all steps attempt formalization regardless of formalizability; LSTM aggregation is simplistic.\",\n    \"building_blocks\": [\n      \"FormalStep benchmark (30,809 formal statements)\",\n      \"Step-level auto-formalization pipeline (NL→Lean 4)\",\n      \"4-state verification taxonomy\",\n      \"Formal+neural score combination methodology\"\n    ],\n    \"relevance_to_seed\": \"Provides the Lean 4 step-level formalization pipeline directly reusable by our system; the domain-dependent proof rates (72-82%) empirically motivate the formalizability-aware routing our work introduces.\"\n  },\n  {\n    \"title\": \"Typed Chain-of-Thought: A Curry-Howard Framework for Verifying LLM Reasoning\",\n    \"venue\": \"arXiv 2025 (ICLR 2026 Withdrawn)\",\n    \"problem_identification\": \"CoT verification lacked a formal theoretical grounding — existing methods are heuristic (neural scoring) or require full formalization (proof assistants). No framework connected CoT faithfulness to provable type-theoretic properties.\",\n    \"key_insight\": \"Under the Curry-Howard correspondence, a faithful reasoning trace is isomorphic to a well-typed program; type-checking CoT steps provides a lightweight formal certificate without requiring full theorem proving.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Maps each CoT step to a typed combinator in a minimal type system (ℕ⊆ℤ⊆ℚ with unit types and rule schemas like Compute-Add: ℚ×ℚ→ℚ). Constructs a Typed Reasoning Graph (bipartite: statement nodes with types, rule nodes with signatures). Certifies traces via three metrics: Coverage (proportion typed), EVR (evidence validity rate), PE (path exists from premises to conclusion). On GSM8K, certified runs achieve 91.6% precision (strict gate) vs 42.4% for rejected runs, a 49pp gap validating type-checking as a discriminator.\",\n    \"limitations_and_open_questions\": \"Only tested on GSM8K arithmetic (trivial type system); withdrawn from ICLR 2026 suggesting reviewer concerns; 40-60% of correct answers achieve full typing — precisely the coverage gap motivating a hybrid approach. Can this type system scale beyond arithmetic?\",\n    \"building_blocks\": [\n      \"Typed Reasoning Graph construction\",\n      \"Certification metrics (Coverage, EVR, UVR, PE)\",\n      \"Curry-Howard CoT mapping methodology\",\n      \"Empirical 40-60% formalizability rate\"\n    ],\n    \"relevance_to_seed\": \"Provides theoretical motivation for 'reward = derivability'; the empirically observed 40-60% typing success rate directly justifies our formalizability router — it proves that partial formal coverage is the norm, not an edge case.\"\n  },\n  {\n    \"title\": \"PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models\",\n    \"venue\": \"ACL 2025 Main\",\n    \"problem_identification\": \"Existing PRM benchmarks (PRM800K, MR-Ben) evaluate only step correctness, missing systematic assessment of diverse error detection capabilities. This made it impossible to diagnose *what types* of errors PRMs fail on.\",\n    \"key_insight\": \"PRMs need evaluation across orthogonal capability dimensions (simplicity, soundness, sensitivity) with a fine-grained error taxonomy, not just binary correct/incorrect — the type of error matters as much as whether it's caught.\",\n    \"innovation_type\": \"new_benchmark\",\n    \"method_summary\": \"Defines 3 dimensions subdivided into 9 error categories: Simplicity (non-redundancy, non-circular logic), Soundness (empirical soundness, step consistency, domain consistency, confidence invariance), Sensitivity (prerequisite sensitivity, deception resistance, multi-solution consistency). Constructs 6,216 problems with 83,456 step-level labels. Evaluates 25 models spanning open-source PRMs and prompted LLMs. Best model (Gemini-2-Thinking) scores 68.8 vs human 83.8, with particular weakness on sensitivity dimensions.\",\n    \"limitations_and_open_questions\": \"Math-only scope; diagnoses the performance gap but doesn't prescribe solutions; doesn't evaluate formal verification approaches. Which of the 9 categories would benefit most from formal vs neural verification?\",\n    \"building_blocks\": [\n      \"9-category error taxonomy for reasoning steps\",\n      \"Multi-dimensional PRM evaluation protocol\",\n      \"83,456 step-level annotations\",\n      \"Quantified PRM-human performance gap\"\n    ],\n    \"relevance_to_seed\": \"Provides the evaluation framework for our hybrid PRM; the 9-category taxonomy can map to formalizability (step consistency and empirical soundness are more formalizable than deception resistance), informing router training targets.\"\n  },\n  {\n    \"title\": \"DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition\",\n    \"venue\": \"arXiv 2025\",\n    \"problem_identification\": \"End-to-end neural theorem provers fail on complex multi-step theorems because search space grows exponentially; no method successfully unified informal chain-of-thought reasoning with formal Lean 4 proof generation at scale.\",\n    \"key_insight\": \"Recursive decomposition via a large LM (671B) into formally-stated subgoals, each proved by a small LM (7B), enables scaling formal proving through division of cognitive labor — the large model plans, the small model executes.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"DeepSeek-V3 (671B) generates proof sketches decomposing theorems into Lean 4 subgoals (have statements with sorry placeholders). A 7B prover resolves each subgoal with preceding subgoals as premises. Cold-start training synthesizes data from cases where the 7B fails end-to-end but succeeds on all decomposed subgoals, pairing formal proofs with informal reasoning. GRPO reinforcement learning with binary verification rewards and consistency penalties further optimizes. Achieves 88.9% on MiniF2F-test (Pass@8192) and 49/658 PutnamBench problems.\",\n    \"limitations_and_open_questions\": \"671B model impractical for academic compute budgets; formal-informal gap persists (6/15 vs 8/15 AIME); subgoal decomposition quality depends on DeepSeek-V3's informal understanding. Can the 7B prover alone serve as a step-level verifier?\",\n    \"building_blocks\": [\n      \"Recursive subgoal decomposition pipeline\",\n      \"Cold-start formal-informal training data synthesis\",\n      \"ProverBench (325 problems)\",\n      \"Unified CoT + formal proof generation architecture\"\n    ],\n    \"relevance_to_seed\": \"Provides SOTA autoformalization infrastructure for our formal verifier component; the 7B prover variant is directly usable within academic compute constraints, and the subgoal decomposition paradigm parallels our step-level verification needs.\"\n  },\n  {\n    \"title\": \"Probabilistic Soundness Guarantees in LLM Reasoning Chains (ARES)\",\n    \"venue\": \"EMNLP 2025\",\n    \"problem_identification\": \"Prior step-level verification methods evaluate all steps holistically, so early errors corrupt downstream judgments via error propagation. ARES identified this by analyzing failure modes on long synthetic chains where existing PRMs and LLM-judges degrade catastrophically.\",\n    \"key_insight\": \"Marginalize entailment over exponentially many premise subsets weighted by predecessor soundness probabilities, creating an inductive filter that severs error propagation by treating earlier claims as probabilistically uncertain.\",\n    \"innovation_type\": \"new_formulation\",\n    \"method_summary\": \"Models reasoning chains as base + derived claims. For each derived claim Cₖ, computes stability score τₖ by averaging entailment ℰ(C(α), Cₖ) over Monte Carlo-sampled premise inclusion vectors α, where inclusion probability is recursively determined by prior steps' entailment scores. Provides statistical guarantees via Hoeffding bounds: N ≥ log(2m/δ)/(2ε²) samples ensure |τ̂ₖ - τₖ| ≤ ε with probability 1-δ. Uses neural entailment models (GPT-4o-mini, Qwen3-4B) with binary or Likert-scale outputs.\",\n    \"limitations_and_open_questions\": \"Entailment quality is bottlenecked by neural NLI models — no formal verification, so semantically complex steps may get unreliable scores. The exponential premise-subset formulation is elegant but the Monte Carlo approximation's practical convergence on deeply nested mathematical reasoning is untested.\",\n    \"building_blocks\": [\n      \"Autoregressive premise-subset sampling for entailment\",\n      \"Hoeffding-based statistical certification\",\n      \"Inductive soundness propagation framework\",\n      \"Error propagation-resistant step evaluation\"\n    ],\n    \"relevance_to_seed\": \"Direct comparison target: our formal derivability checking replaces ARES's neural entailment model, and should outperform on miracle steps where neural NLI models cannot assess logical derivability from predecessors.\"\n  },\n  {\n    \"title\": \"Process Reward Models That Think (ThinkPRM)\",\n    \"venue\": \"arXiv 2025 (ICLR 2026 withdrawn)\",\n    \"problem_identification\": \"Discriminative PRMs require massive process-labeled data (PRM800K: 800K labels) yet generalize poorly out-of-domain. LLM-as-Judge avoids fine-tuning but underperforms. The gap is a data-efficient PRM that retains fine-tuning benefits.\",\n    \"key_insight\": \"Frame step verification as a generation task — producing verification chain-of-thought before scoring — then filter synthetic training data on process-level (not just outcome-level) agreement to achieve 100× data reduction.\",\n    \"innovation_type\": \"combination\",\n    \"method_summary\": \"Uses QwQ-32B-Preview to generate verification CoTs for PRM800K problem-solution pairs, then filters aggressively: only ~20% survive format, process-label agreement, and length constraints, yielding ~1K usable chains (8K step labels). Fine-tunes R1-Distill-Qwen models via LoRA (rank 32) on these chains. Scoring extracts P('yes')/(P('yes')+P('no')) at decision tokens. Supports parallel (K independent chains) and sequential (self-correction triggers) test-time scaling.\",\n    \"limitations_and_open_questions\": \"Withdrawn from ICLR 2026 — reasons unclear but may relate to reproducibility or concurrent work. Depends on a stronger teacher model (QwQ-32B) for data synthesis. Still purely neural with no formal verification component — verification CoT can hallucinate plausible-sounding but incorrect critiques.\",\n    \"building_blocks\": [\n      \"Generative verification CoT paradigm\",\n      \"Process-filtered synthetic data pipeline\",\n      \"Dual test-time scaling (parallel + sequential)\",\n      \"LoRA-efficient PRM training\"\n    ],\n    \"relevance_to_seed\": \"Validates the generative PRM paradigm our neural verifier builds on; demonstrates that verification CoT dramatically outperforms discriminative scoring, motivating GenPRM-style neural verifier as the non-formal branch of our router.\"\n  },\n  {\n    \"title\": \"Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification\",\n    \"venue\": \"arXiv 2026\",\n    \"problem_identification\": \"Prior neuro-symbolic methods apply formal verification only as passive post-hoc validation, missing the opportunity to use formal signals during training. The gap is integrating formal verification as an active training signal that penalizes intermediate fallacies.\",\n    \"key_insight\": \"Formal symbolic verification (Python/Z3/SMT solvers) can be dynamically interleaved with natural language generation during both SFT and RL stages, with a hierarchical reward structure that differentiates fatal failures, format errors, and logical correctness.\",\n    \"innovation_type\": \"new_technique\",\n    \"method_summary\": \"Stage 1 (SFT): Decomposes reasoning chains into logical modules, synthesizes formal proof\n... (truncated)\n\n## Your task\n\nSynthesize these paper analyses into a **Field Guide** — a strategic document that would help a researcher generate novel, high-quality ideas in this area. This is NOT a survey — it's an opinionated strategy guide for innovation.\n\nThink about:\n- What PATTERNS OF INNOVATION keep working in this field?\n- What do reviewers consistently reward?\n- Where are the real gaps (not assumed gaps)?\n- What combinations haven't been tried?\n- What mistakes should we avoid?\n\n## Output format\n\nOutput a JSON object with these sections:\n{\n  \"innovation_patterns\": [\n    {\"pattern\": \"name\", \"description\": \"how it works\", \"examples\": [\"paper1\", \"paper2\"], \"success_rate\": \"high/medium/low\"}\n  ],\n  \"reviewer_preferences\": [\n    \"What reviewers in this area consistently care about (based on evidence from paper analyses)\"\n  ],\n  \"field_gaps\": [\n    {\"gap\": \"description of unsolved problem\", \"evidence\": \"which papers mention this limitation\", \"difficulty\": \"high/medium/low\", \"impact_if_solved\": \"high/medium/low\"}\n  ],\n  \"untried_combinations\": [\n    {\"idea_sketch\": \"what could be combined\", \"from_papers\": [\"which papers inspire this\"], \"why_promising\": \"reason\"}\n  ],\n  \"method_building_blocks\": [\n    {\"tool\": \"name\", \"what_it_does\": \"description\", \"used_by\": [\"papers\"], \"could_be_applied_to\": \"new application\"}\n  ],\n  \"common_pitfalls\": [\n    \"Mistakes to avoid when working in this area (based on reviewer feedback and paper limitations)\"\n  ],\n  \"field_trajectory\": \"Where is this field heading? What are the 2-3 most promising macro-directions? (paragraph)\",\n  \"meta_advice\": \"If you were advising a PhD student to write a strong 2026 paper in this area, what would you tell them? (paragraph)\"\n}\n\nBe specific and evidence-based — every claim should reference specific papers from the analyses. Avoid generic advice like 'be novel' — instead say 'Papers that combine X with Y for task Z have been getting accepted (see Paper A, Paper B).'.\n\nIMPORTANT: You MUST end your response with the JSON object."
}
```

---

### Runtime record

_source line 2 · 2026-05-29T05:33:26.278Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-29T05:33:26.278Z",
  "sessionId": "733f9e07-4f23-4518-9a71-bb860175df75"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-29T05:33:26.339Z_

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

## Paper analyses (21 papers)

[
  {
    "title": "Efficient PRM Training Data Synthesis via Formal Verification (FoVer)",
    "venue": "ACL 2026 Findings (withdrawn from ICLR 2026)",
    "problem_identification": "PRM training requires expensive human step-level annotation (~800K labels in PRM800K) or costly Monte Carlo LLM sampling. The authors identified that formal verification tools already produce binary correctness judgments that could replace human labelers entirely, yet no one had connected the formal verification and PRM training communities.",
    "key_insight": "Step-level correctness labels produced by Z3 (for logic) and Isabelle (for theorem proving) transfer from formal to informal reasoning domains, enabling PRMs trained on purely formal data to improve on NLI, BBH, and math benchmarks they never saw.",
    "innovation_type": "cross_domain",
    "method_summary": "FoVer has LLMs (Llama 3.1 8B, Qwen 2.5 7B) generate step-by-step solutions for formal tasks. For logic (FLDx2), Z3 checks each step's validity given premises independently. For theorem proving (GSM8K variants), Isabelle verifies each step using a `sorry`-insertion trick that isolates individual steps. The resulting FoVer-40K dataset (20K logic + 20K theorem steps) trains PRMs via standard cross-entropy on binary correct/incorrect tokens. Errors are naturally occurring from LLM generation, not injected.",
    "limitations_and_open_questions": "Computationally intensive (weeks on multiple servers for Isabelle); limited to 8B models; PRMs become overly strict on informal reasoning (penalizing valid rounding). Critical open question: can the formal-to-informal transfer be improved by mixing formal and informal training data?",
    "building_blocks": [
      "FoVer-40K dataset with verified step labels",
      "Z3 step-independent verification pipeline",
      "Isabelle sorry-insertion trick for step isolation",
      "Public codebase (GitHub psunlpgroup/FoVer)",
      "Formal-to-informal transfer methodology"
    ],
    "relevance_to_seed": "Direct foundation — provides the formal verification infrastructure, public codebase, and training data synthesis pipeline that our hybrid router would build upon, with our work extending it by adding neural fallback for non-formalizable steps."
  },
  {
    "title": "HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs",
    "venue": "ICML 2026 (Poster)",
    "problem_identification": "Informal LLM reasoning is flexible but accumulates logical drift over long chains; formal theorem proving is rigid but correct. No existing system interleaved them at inference time with feedback loops, forcing a binary choice between flexibility and rigor.",
    "key_insight": "Intermediate formal verification during inference (not just at training time) prevents reasoning drift while preserving exploratory freedom, and a memory module across verification cycles avoids redundant exploration — achieving 67% accuracy gains with 80% fewer FLOPs.",
    "innovation_type": "combination",
    "method_summary": "HERMES comprises four modules: (1) an LLM generating informal reasoning steps, (2) a Translator converting them to Lean 4 code, (3) a Prover validating via Lean 4 REPL returning True/False signals, and (4) a Feedback module routing verification results back to guide subsequent reasoning. A Memory module tracks explored paths, successful strategies, and failures. A verification scheduler parallelizes Lean compilation for efficiency. The cycle repeats until verification succeeds or resource limits are hit.",
    "limitations_and_open_questions": "Restricted to problems expressible in Lean 4; translation quality bottlenecks the entire pipeline. Does not train PRMs or produce reusable reward signals — verification is inference-only. How would this interleaving degrade on problems with low formalizability?",
    "building_blocks": [
      "Lean 4 REPL integration with Python",
      "Interleaved informal/formal reasoning loop",
      "Memory module for proof continuity",
      "Verification scheduler for parallel Lean compilation"
    ],
    "relevance_to_seed": "Validates that hybrid formal/neural reasoning is viable at scale; our router operates at a different level (PRM training vs. inference-time verification), but HERMES's translator and Lean 4 integration patterns are directly reusable for the formal verifier component."
  },
  {
    "title": "Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries (PRoSFI)",
    "venue": "arXiv 2026 (under review)",
    "problem_identification": "Outcome rewards mask flawed intermediate steps (correct answers via wrong reasoning), but generating full formal proofs is intractable for 7B models. The gap is a lightweight formal representation that a small model can produce and a prover can verify, without requiring complete proof generation.",
    "key_insight": "Structured formal intermediaries — lightweight JSON representations containing (id, dependencies, conclusion, inference_rule) per step — bridge the formalization gap, enabling formal verification without full proof generation, and can drive GRPO training via tiered process rewards.",
    "innovation_type": "new_formulation",
    "method_summary": "The model generates natural language reasoning interleaved with structured formal intermediaries in a single forward pass. Each intermediary specifies dependencies (≤5 prior steps), a conclusion in formal language, and the inference rule applied (Modus Ponens, Hypothetical Syllogism, etc.). A formal prover verifies each step independently. GRPO training uses tiered rewards: R=1.0 (correct + all verified), R=0.3 (correct + some unverified), R=0.1 (format OK + wrong answer), R=0.0 (format errors). Trained on ProverQA (769 instances).",
    "limitations_and_open_questions": "Limited to first-order logic; no mechanism for unformalizable steps (all steps must produce intermediaries). Binary pass/fail verification loses granularity. Soundness evaluated by GPT-OSS-120B, not human judges. How would this extend beyond logic to math or science?",
    "building_blocks": [
      "Structured formal intermediary format",
      "Tiered GRPO reward scheme (1.0/0.3/0.1/0.0)",
      "ProverQA benchmark suite",
      "Single-pass NL + formal generation approach"
    ],
    "relevance_to_seed": "Closest methodological competitor — our key differentiator is the learned router that handles non-formalizable steps neurally rather than requiring ALL steps to produce formal intermediaries, plus explicit miracle step targeting."
  },
  {
    "title": "Let's Verify Step by Step",
    "venue": "ICLR 2024",
    "problem_identification": "Outcome-supervised reward models (ORMs) cannot localize errors in reasoning chains, leading to reward hacking where models get right answers via wrong reasoning. The authors identified that step-level supervision existed in education/tutoring but had never been systematically compared to outcome supervision for LLM training at scale.",
    "key_insight": "Process supervision (step-level human feedback with positive/neutral/negative labels) provides precise credit assignment that significantly outperforms outcome supervision, and an active learning strategy selecting solutions most likely to deceive the current PRM yields 2.6× data efficiency.",
    "innovation_type": "new_benchmark",
    "method_summary": "Human labelers annotate each step as positive (correct, progresses), neutral (correct, no progress), or negative (incorrect) without reference solutions but with access to ground-truth answers. PRM800K contains 800K such labels across 75K solution traces for MATH problems. PRMs are trained on these labels and used for best-of-N selection: generate N candidate solutions, score each by the minimum step-level PRM score, select the highest-scoring solution. Active learning selects solutions where the current PRM is most uncertain.",
    "limitations_and_open_questions": "Requires expensive human annotation ($$$); limited to MATH domain; labeler agreement rates not thoroughly analyzed. The neutral category is underspecified. Does process supervision's advantage hold for non-mathematical reasoning? What happens at larger model scales?",
    "building_blocks": [
      "PRM800K dataset (800K step labels)",
      "Best-of-N selection via minimum step score",
      "Active learning for PRM data efficiency",
      "Process vs. outcome supervision methodology",
      "Positive/neutral/negative labeling protocol"
    ],
    "relevance_to_seed": "Foundational paradigm paper — defines the PRM framework our work extends; PRM800K's labeling gaps (expensive, domain-limited, no formal grounding) are exactly what FoVer and our hybrid router aim to solve."
  },
  {
    "title": "Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving (MATH-VF)",
    "venue": "arXiv 2025",
    "problem_identification": "Existing PRMs require expensive training and can't verify closed-source model outputs. No training-free framework combined symbolic computation (CAS) with logical verification (SMT) for step-level mathematical verification, despite both tools being mature.",
    "key_insight": "A lightweight custom formal language (SimpleMath, extending first-order logic with mathematical constants/syntactic sugar) enables >90% formalization success on MATH500, allowing a training-free Formalizer+Critic pipeline using SymPy and Z3 to verify individual steps with corrective feedback.",
    "innovation_type": "new_technique",
    "method_summary": "The Formalizer uses few-shot LLM prompting to translate NL solutions into SimpleMath, a readable formal language. The Critic evaluates each step as premises⊢conclusion using two tools: SymPy (CAS) for algebraic/numerical verification and Z3 (SMT) for logical constraint checking. When errors are found, corrective feedback guides solution refinement in iterative cycles. Exploits sparsity in solution dependency graphs, reducing input from O(n²) to O(n×M) where M≤4.",
    "limitations_and_open_questions": "Formalization syntax errors cause verification failures; cannot assess step effectiveness (only correctness); trails fine-tuned PRMs (74.1 vs 78.3 F1 on ProcessBench). SimpleMath is limited to math — how would it extend to logic or science domains?",
    "building_blocks": [
      "SimpleMath formal language specification",
      "SymPy + Z3 dual-tool verification pipeline",
      "Training-free verification framework",
      "Corrective feedback loop for refinement",
      "Dependency graph sparsity optimization"
    ],
    "relevance_to_seed": "Directly relevant architecture for our Z3 verification module — SimpleMath's formalization approach and the CAS+SMT dual-tool pattern can be adopted as the formal verifier component, with our router deciding which steps to send through this pipeline vs. neural verification."
  },
  {
    "title": "Evaluating Step-by-step Reasoning Traces: A Survey",
    "venue": "EMNLP 2025 Findings",
    "problem_identification": "Evaluation practices for reasoning traces are highly inconsistent across the field — different papers measure different properties using incompatible metrics, creating fragmented progress. No unified framework existed to categorize what 'good reasoning' means at the step level.",
    "key_insight": "Four complementary evaluation dimensions — Factuality (grounded in sources), Validity (logically follows from predecessors), Coherence (connects to subsequent steps), and Utility (progresses toward answer) — capture distinct failure modes, and combining Validity+Utility substantially outperforms either alone for PRM training.",
    "innovation_type": "analysis",
    "method_summary": "The survey taxonomizes step-level evaluation into four categories with subcategories: Factuality (groundedness, parametric knowledge), Validity (entailment-based, correctness-based), Coherence (flow, precondition satisfaction), and Utility (progress, value function). Reviews 8 evaluator types (rule-based, uncertainty, cross-encoder, sequence classifier, critic model, generative verifier, etc.) across datasets including PRM800K, ProcessBench, Math-Shepherd, and REVEAL. Identifies five critical gaps including absence of formal verification methods and inability to handle long traces.",
    "limitations_and_open_questions": "Survey scope limited to 2022-2025; no experiments conducted to validate the taxonomy empirically. The formal verification gap they identify (symbolic grounding remains unexplored) is exactly the space FoVer and our work address. How should formalizability be added as a fifth dimension?",
    "building_blocks": [
      "Four-category evaluation taxonomy",
      "Eight evaluator type classifications",
      "Validity+Utility complementarity finding",
      "Formal verification as identified gap",
      "Partial-context evaluation strategy"
    ],
    "relevance_to_seed": "Provides the evaluation framework for our work — our formalizability score adds a fifth dimension to their taxonomy, and their finding that validity (our formal verifier's domain) complements utility (our neural verifier's domain) directly motivates the hybrid routing approach."
  },
  {
    "title": "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning",
    "venue": "AAAI 2026",
    "problem_identification": "Existing PRMs are classification-based scalar predictors that cannot leverage LLMs' generative abilities or scale test-time compute. The authors identified that discriminative PRM formulations create a ceiling that more computation cannot lift.",
    "key_insight": "Reframing process reward modeling as a generative reasoning task — where the PRM produces explicit Chain-of-Thought analysis with executable code verification before judging each step — unlocks test-time compute scaling via majority voting over generated rationales.",
    "innovation_type": "new_formulation",
    "method_summary": "GenPRM uses a three-stage pipeline: (1) Monte Carlo estimation generates step-level pass rates, then Relative Progress Estimation (RPE) refines labels by comparing pass-rate changes between consecutive steps — a step is positive if it increases the probability of reaching the correct answer. (2) A rationale synthesis framework prompts an LLM to generate CoT analysis within &lt;analyze> tags plus executable Python code within &lt;verify> tags; code execution feedback is concatenated for self-correction. (3) The model is fine-tuned on 23K MATH-derived examples to generate reasoning-then-judgment. At inference, N verification paths are sampled and majority-voted, enabling 1.5B to outperform GPT-4o on ProcessBench.",
    "limitations_and_open_questions": "RPE inherits Monte Carlo estimation noise; code verification only catches computationally verifiable errors (not logical leaps or unjustified assumptions). Unclear how RPE handles steps that are wrong but accidentally lead to correct answers.",
    "building_blocks": [
      "Relative Progress Estimation for step labeling",
      "Rationale synthesis with code verification",
      "Test-time compute scaling via majority voting for PRMs",
      "ProcessBench evaluation protocol",
      "23K training data from MATH"
    ],
    "relevance_to_seed": "Serves as the neural verifier baseline in our hybrid system — GenPRM's generative verification handles the non-formalizable steps that the formal verifier cannot reach, and its RPE labels provide comparison ground truth for our routing-based approach."
  },
  {
    "title": "VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning",
    "venue": "arXiv 2026",
    "problem_identification": "LLM outputs mix logically verifiable claims with commonsense assertions, yet existing verification systems apply a single strategy uniformly. The authors recognized that claim type diversity demands heterogeneous verification routing.",
    "key_insight": "Semantic routing — classifying each atomic claim by type (logical/mathematical/temporal vs. commonsense/vague/probabilistic) and dispatching to symbolic SMT solvers or neural LLM ensembles accordingly — enables formal guarantees where possible and soft consensus elsewhere.",
    "innovation_type": "combination",
    "method_summary": "VERGE decomposes LLM outputs into atomic claims, autoformalizes them into SMT-LIB2 (QF_UF/QF_LIA fragments) with K=3 candidate formulas per claim, and enforces semantic equivalence via bidirectional entailment checking. The router (94% accuracy, F1=0.93/0.95) dispatches SMT-amenable claims to Z3 and soft claims to neural ensembles. Error localization uses Minimal Correction Subsets (MCS) via greedy O(n×SAT) approximation to pinpoint exactly which claims to revise. Iterative refinement continues until aggregated score ≥0.75 and joint satisfiability holds.",
    "limitations_and_open_questions": "Routing is rule-based on claim type taxonomy rather than learned from data — unclear if a learned router would outperform. Applied only to inference-time refinement, not PRM training. Autoformalization into QF fragments limits expressiveness for complex mathematical reasoning.",
    "building_blocks": [
      "Semantic claim-type routing taxonomy",
      "MCS-based error localization",
      "Multi-candidate autoformalization with semantic equivalence consensus",
      "Iterative refinement with convergence criteria"
    ],
    "relevance_to_seed": "Most directly related to our routing mechanism — VERGE proves semantic routing between formal and neural verifiers works (18.7% uplift), but routes for inference refinement rather than PRM training, and uses rule-based rather than learned routing."
  },
  {
    "title": "VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks",
    "venue": "ICLR 2026 Poster",
    "problem_identification": "CoT reasoning steps lack formal verification — errors propagate unchecked because no system grounds each step's logical dependencies or verifies entailment from predecessors. The gap between neural generation and formal validity was unexploited for training.",
    "key_insight": "Formalizing each CoT step into FOL with explicitly grounded premises (from context, commonsense, or prior steps) enables Z3-based entailment/contradiction/consistency checking that simultaneously serves as verification signal AND training reward for SFT and DPO.",
    "innovation_type": "combination",
    "method_summary": "VeriCoT uses two-stage autoformalization: first generating SMT-LIB formulas reusing existing vocabulary, then creating new declarations for inexpressible segments (up to 3 iterations). Each step's premises are identified and categorized by source (context vs. commonsense). Z3 checks three relations: entailment (step follows), contradiction (step conflicts), or consistency (step is contingent, needing premise support). Verification signals feed SFT (training on verified CoTs, +3% accuracy) and DPO (verified=chosen, failed=rejected, +18.4% relative verification improvement). Inference-time self-reflection on failures yields +12.3% absolute gains.",
    "limitations_and_open_questions": "Autoformalization success rate is unstated but likely limited — the untranslatable category exists but its frequency isn't characterized. No mechanism for routing around formalization failures; steps that can't be formalized are simply marked. Tested only on ProofWriter, LegalBench, BioASQ — no math benchmarks.",
    "building_blocks": [
      "CoT-to-FOL two-stage autoformalization",
      "Premise grounding and categorization",
      "Z3 entailment/contradiction/consistency triple-check",
      "Verification-as-reward for SFT and DPO training"
    ],
    "relevance_to_seed": "Directly validates our core approach — verification signals from formal checking can train better models via SFT/DPO. The untranslatable step category and premise grounding methodology inform our formalizability classifier design. Multi-domain evaluation (legal, biomedical) supports AAAI generality."
  },
  {
    "title": "ProcessBench: Identifying Process Errors in Mathematical Reasoning",
    "venue": "ACL 2025",
    "problem_identification": "No rigorous benchmark existed for evaluating step-level error localization in mathematical reasoning — prior work used binary correctness or synthetic errors. The authors found that existing PRMs, despite training on process supervision, fail to generalize to competition-level problems.",
    "key_insight": "Error localization (identifying the earliest erroneous step) is fundamentally harder than binary solution correctness, and existing PRMs trained on GSM8K/MATH-level data catastrophically fail on harder problems — revealing that scalar process reward models don't truly understand step validity.",
    "innovation_type": "new_benchmark",
    "method_summary": "ProcessBench collects problems from four difficulty tiers (GSM8K, MATH, OlympiadBench, Omni-MATH) with solutions from 12 diverse generators (Qwen/LLaMA series). Steps are reformatted via Qwen2.5-72B-Instruct for consistent granularity, then expert-annotated for the earliest erroneous step. The benchmark evaluates PRMs (scoring each step) and critic models (prompted step-by-step critique), revealing that prompted critics like QwQ-32B-Preview match GPT-4o while trained PRMs underperform both on hard problems.",
    "limitations_and_open_questions": "Math-only domain limits generality claims. Error taxonomy is implicit — doesn't distinguish miracle steps from calculation errors or logical fallacies. Annotation identifies location but not error type, missing an opportunity to study which errors PRMs can vs. cannot catch.",
    "building_blocks": [
      "3,400 expert-annotated error localization test cases",
      "Multi-difficulty evaluation protocol (GSM8K through Olympiad)",
      "PRM vs. critic model comparison framework",
      "Step reformatting methodology for consistent granularity"
    ],
    "relevance_to_seed": "Primary evaluation benchmark — our hybrid PRM must be tested here. The finding that PRMs fail on hard problems motivates formal verification: hard problems likely contain more miracle steps that neural-only PRMs miss. Lack of error type taxonomy creates an opportunity for our miracle-step-specific evaluation."
  },
  {
    "title": "Risk-Controlled Lean-as-Judge for Natural-Language Mathematical Reasoning",
    "venue": "arXiv 2026",
    "problem_identification": "Lean-as-Judge is increasingly used to verify math answers, but its signal is partial and unreliable: a 7B autoformalizer proves only 28% of problems, and manual audit reveals only ~43% of those proofs are faithful to the original problem statement. No principled framework existed for knowing when to trust formal verification.",
    "key_insight": "Formal verification's value is bounded by both coverage (what fraction of problems can be formalized and proved) and faithfulness (whether the proof actually captures the intended claim) — and a risk-controlled selector over Lean-trace diagnostics can certify when formal judgments are trustworthy.",
    "innovation_type": "analysis",
    "method_summary": "The pipeline autoformalizes via Qwen2.5-Coder-7B to Lean 4, generating four artifacts per answer class with error-feedback repair. CovCal selects based on four diagnostics: typed coverage, proved coverage, unresolved rival mass, and formal margin. Two risk regimes are compared: Bonferroni (union-bound over 125-cell threshold grid, conservative) and dev-then-cal (select threshold on dev split, evaluate once on cal). A specialized Goedel-Prover-V2-8B achieves 79% coverage vs. 28% baseline, enabling certification of 17/20 partitions at ~48% acceptance with 0.98 accuracy.",
    "limitations_and_open_questions": "Faithfulness gap (43%) is alarming and unresolved — structural proofs often assert true-but-irrelevant claims. Specialization > scale (8B specialized beats 32B general) suggests formalization quality is a training data problem. Step-level analysis is absent — all verification is at the solution level.",
    "building_blocks": [
      "Formalizability coverage quantification (28-79%)",
      "Proof faithfulness audit methodology",
      "CovCal risk-controlled selector with Lean-trace diagnostics",
      "Four-diagnostic acceptance criteria",
      "Evidence that specialization outperforms scale for autoformalization"
    ],
    "relevance_to_seed": "Directly validates our router's necessity — formal verification alone covers 28-79% with questionable faithfulness, empirically proving that a hybrid approach with neural fallback is essential. The coverage diagnostics inform our formalizability score design, and the faithfulness findings motivate our step-level (not solution-level) verification approach."
  },
  {
    "title": "Curing Miracle Steps in LLM Mathematical Reasoning with Rubric Rewards",
    "venue": "ACL 2026 Main",
    "problem_identification": "Through systematic human verification of LLM math solutions, discovered that correct-answer solutions frequently contain unjustified logical leaps ('miracle steps'), enabling reward hacking that inflates Pass@N metrics. No prior taxonomy of these process-level failure modes existed.",
    "key_insight": "Problem-specific rubrics that evaluate entire reasoning trajectories against structured criteria outperform both outcome-only rewards and generic step-level PRMs for detecting process flaws, because rubrics encode what valid reasoning *should* look like per problem.",
    "innovation_type": "new_formulation",
    "method_summary": "Defines 6 false-positive failure modes (inductive overgeneralization, outcome irrelevance, neglected operational preconditions, unverified assumptions, numerical coincidence, miracle steps). Implements a 3-phase pipeline: (1) Gemini-2.5-Pro synthesizes problem-specific rubrics covering strategy/computation/logic/conclusion, (2) scoring data pairs problems+rubrics with 0-10 rated responses, (3) Qwen3-4B is fine-tuned via SFT+PPO to predict rubric-grounded scores. The RRM-trained policy achieves Verified Pass@1024 of 62.6% on AIME2024 (vs 26.7% outcome-only) and reduces miracle steps by 71%.",
    "limitations_and_open_questions": "Rubric generation depends on proprietary Gemini-2.5-Pro (reproducibility concern); 29% of miracle steps persist; rubrics are still neural artifacts — can formal derivability checking close the remaining gap? The 0-10 scoring granularity vs binary formal verification tradeoff is unexplored.",
    "building_blocks": [
      "6-type miracle step taxonomy",
      "Rubric synthesis pipeline",
      "Verified Pass@N evaluation protocol",
      "RRM architecture (SFT+PPO on rubric scores)"
    ],
    "relevance_to_seed": "Directly defines the miracle step problem our system targets; the 71% reduction via neural rubrics sets the quantitative bar our formal derivability approach must surpass."
  },
  {
    "title": "Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification",
    "venue": "ACL 2025 Main",
    "problem_identification": "PRMs use opaque neural scoring without interpretable evidence of step correctness; no prior work applied formal mathematical verification at the individual reasoning step level (previous auto-formalization targeted whole problems, not steps).",
    "key_insight": "Auto-formalizing individual reasoning steps (not whole problems) into Lean 4 theorem statements enables interpretable, mechanically verifiable correctness judgments that are complementary to — not redundant with — neural PRM scores.",
    "innovation_type": "cross_domain",
    "method_summary": "Each reasoning step is auto-formalized via GPT-4o into a Lean 4 theorem (taking prior conclusions as premises, current assertion as goal), then proved using DeepSeek-Prover-V1.5 (16-sample budget). Steps receive one of 4 states: no-verification-needed, formalization-failed, proved, unprovable. State sequences are aggregated by a minimal 2-layer LSTM into a trajectory quality score. This formal score is combined with PRM scores for Best-of-N reranking, yielding 2-3% gains over PRM+ORM ensembles on MATH-500.",
    "limitations_and_open_questions": "4-8× computational overhead vs baseline PRMs; geometry/combinatorics formalization limited (72% vs 82% proof rate); no learned routing — all steps attempt formalization regardless of formalizability; LSTM aggregation is simplistic.",
    "building_blocks": [
      "FormalStep benchmark (30,809 formal statements)",
      "Step-level auto-formalization pipeline (NL→Lean 4)",
      "4-state verification taxonomy",
      "Formal+neural score combination methodology"
    ],
    "relevance_to_seed": "Provides the Lean 4 step-level formalization pipeline directly reusable by our system; the domain-dependent proof rates (72-82%) empirically motivate the formalizability-aware routing our work introduces."
  },
  {
    "title": "Typed Chain-of-Thought: A Curry-Howard Framework for Verifying LLM Reasoning",
    "venue": "arXiv 2025 (ICLR 2026 Withdrawn)",
    "problem_identification": "CoT verification lacked a formal theoretical grounding — existing methods are heuristic (neural scoring) or require full formalization (proof assistants). No framework connected CoT faithfulness to provable type-theoretic properties.",
    "key_insight": "Under the Curry-Howard correspondence, a faithful reasoning trace is isomorphic to a well-typed program; type-checking CoT steps provides a lightweight formal certificate without requiring full theorem proving.",
    "innovation_type": "new_formulation",
    "method_summary": "Maps each CoT step to a typed combinator in a minimal type system (ℕ⊆ℤ⊆ℚ with unit types and rule schemas like Compute-Add: ℚ×ℚ→ℚ). Constructs a Typed Reasoning Graph (bipartite: statement nodes with types, rule nodes with signatures). Certifies traces via three metrics: Coverage (proportion typed), EVR (evidence validity rate), PE (path exists from premises to conclusion). On GSM8K, certified runs achieve 91.6% precision (strict gate) vs 42.4% for rejected runs, a 49pp gap validating type-checking as a discriminator.",
    "limitations_and_open_questions": "Only tested on GSM8K arithmetic (trivial type system); withdrawn from ICLR 2026 suggesting reviewer concerns; 40-60% of correct answers achieve full typing — precisely the coverage gap motivating a hybrid approach. Can this type system scale beyond arithmetic?",
    "building_blocks": [
      "Typed Reasoning Graph construction",
      "Certification metrics (Coverage, EVR, UVR, PE)",
      "Curry-Howard CoT mapping methodology",
      "Empirical 40-60% formalizability rate"
    ],
    "relevance_to_seed": "Provides theoretical motivation for 'reward = derivability'; the empirically observed 40-60% typing success rate directly justifies our formalizability router — it proves that partial formal coverage is the norm, not an edge case."
  },
  {
    "title": "PRMBench: A Fine-grained and Challenging Benchmark for Process-Level Reward Models",
    "venue": "ACL 2025 Main",
    "problem_identification": "Existing PRM benchmarks (PRM800K, MR-Ben) evaluate only step correctness, missing systematic assessment of diverse error detection capabilities. This made it impossible to diagnose *what types* of errors PRMs fail on.",
    "key_insight": "PRMs need evaluation across orthogonal capability dimensions (simplicity, soundness, sensitivity) with a fine-grained error taxonomy, not just binary correct/incorrect — the type of error matters as much as whether it's caught.",
    "innovation_type": "new_benchmark",
    "method_summary": "Defines 3 dimensions subdivided into 9 error categories: Simplicity (non-redundancy, non-circular logic), Soundness (empirical soundness, step consistency, domain consistency, confidence invariance), Sensitivity (prerequisite sensitivity, deception resistance, multi-solution consistency). Constructs 6,216 problems with 83,456 step-level labels. Evaluates 25 models spanning open-source PRMs and prompted LLMs. Best model (Gemini-2-Thinking) scores 68.8 vs human 83.8, with particular weakness on sensitivity dimensions.",
    "limitations_and_open_questions": "Math-only scope; diagnoses the performance gap but doesn't prescribe solutions; doesn't evaluate formal verification approaches. Which of the 9 categories would benefit most from formal vs neural verification?",
    "building_blocks": [
      "9-category error taxonomy for reasoning steps",
      "Multi-dimensional PRM evaluation protocol",
      "83,456 step-level annotations",
      "Quantified PRM-human performance gap"
    ],
    "relevance_to_seed": "Provides the evaluation framework for our hybrid PRM; the 9-category taxonomy can map to formalizability (step consistency and empirical soundness are more formalizable than deception resistance), informing router training targets."
  },
  {
    "title": "DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via Reinforcement Learning for Subgoal Decomposition",
    "venue": "arXiv 2025",
    "problem_identification": "End-to-end neural theorem provers fail on complex multi-step theorems because search space grows exponentially; no method successfully unified informal chain-of-thought reasoning with formal Lean 4 proof generation at scale.",
    "key_insight": "Recursive decomposition via a large LM (671B) into formally-stated subgoals, each proved by a small LM (7B), enables scaling formal proving through division of cognitive labor — the large model plans, the small model executes.",
    "innovation_type": "combination",
    "method_summary": "DeepSeek-V3 (671B) generates proof sketches decomposing theorems into Lean 4 subgoals (have statements with sorry placeholders). A 7B prover resolves each subgoal with preceding subgoals as premises. Cold-start training synthesizes data from cases where the 7B fails end-to-end but succeeds on all decomposed subgoals, pairing formal proofs with informal reasoning. GRPO reinforcement learning with binary verification rewards and consistency penalties further optimizes. Achieves 88.9% on MiniF2F-test (Pass@8192) and 49/658 PutnamBench problems.",
    "limitations_and_open_questions": "671B model impractical for academic compute budgets; formal-informal gap persists (6/15 vs 8/15 AIME); subgoal decomposition quality depends on DeepSeek-V3's informal understanding. Can the 7B prover alone serve as a step-level verifier?",
    "building_blocks": [
      "Recursive subgoal decomposition pipeline",
      "Cold-start formal-informal training data synthesis",
      "ProverBench (325 problems)",
      "Unified CoT + formal proof generation architecture"
    ],
    "relevance_to_seed": "Provides SOTA autoformalization infrastructure for our formal verifier component; the 7B prover variant is directly usable within academic compute constraints, and the subgoal decomposition paradigm parallels our step-level verification needs."
  },
  {
    "title": "Probabilistic Soundness Guarantees in LLM Reasoning Chains (ARES)",
    "venue": "EMNLP 2025",
    "problem_identification": "Prior step-level verification methods evaluate all steps holistically, so early errors corrupt downstream judgments via error propagation. ARES identified this by analyzing failure modes on long synthetic chains where existing PRMs and LLM-judges degrade catastrophically.",
    "key_insight": "Marginalize entailment over exponentially many premise subsets weighted by predecessor soundness probabilities, creating an inductive filter that severs error propagation by treating earlier claims as probabilistically uncertain.",
    "innovation_type": "new_formulation",
    "method_summary": "Models reasoning chains as base + derived claims. For each derived claim Cₖ, computes stability score τₖ by averaging entailment ℰ(C(α), Cₖ) over Monte Carlo-sampled premise inclusion vectors α, where inclusion probability is recursively determined by prior steps' entailment scores. Provides statistical guarantees via Hoeffding bounds: N ≥ log(2m/δ)/(2ε²) samples ensure |τ̂ₖ - τₖ| ≤ ε with probability 1-δ. Uses neural entailment models (GPT-4o-mini, Qwen3-4B) with binary or Likert-scale outputs.",
    "limitations_and_open_questions": "Entailment quality is bottlenecked by neural NLI models — no formal verification, so semantically complex steps may get unreliable scores. The exponential premise-subset formulation is elegant but the Monte Carlo approximation's practical convergence on deeply nested mathematical reasoning is untested.",
    "building_blocks": [
      "Autoregressive premise-subset sampling for entailment",
      "Hoeffding-based statistical certification",
      "Inductive soundness propagation framework",
      "Error propagation-resistant step evaluation"
    ],
    "relevance_to_seed": "Direct comparison target: our formal derivability checking replaces ARES's neural entailment model, and should outperform on miracle steps where neural NLI models cannot assess logical derivability from predecessors."
  },
  {
    "title": "Process Reward Models That Think (ThinkPRM)",
    "venue": "arXiv 2025 (ICLR 2026 withdrawn)",
    "problem_identification": "Discriminative PRMs require massive process-labeled data (PRM800K: 800K labels) yet generalize poorly out-of-domain. LLM-as-Judge avoids fine-tuning but underperforms. The gap is a data-efficient PRM that retains fine-tuning benefits.",
    "key_insight": "Frame step verification as a generation task — producing verification chain-of-thought before scoring — then filter synthetic training data on process-level (not just outcome-level) agreement to achieve 100× data reduction.",
    "innovation_type": "combination",
    "method_summary": "Uses QwQ-32B-Preview to generate verification CoTs for PRM800K problem-solution pairs, then filters aggressively: only ~20% survive format, process-label agreement, and length constraints, yielding ~1K usable chains (8K step labels). Fine-tunes R1-Distill-Qwen models via LoRA (rank 32) on these chains. Scoring extracts P('yes')/(P('yes')+P('no')) at decision tokens. Supports parallel (K independent chains) and sequential (self-correction triggers) test-time scaling.",
    "limitations_and_open_questions": "Withdrawn from ICLR 2026 — reasons unclear but may relate to reproducibility or concurrent work. Depends on a stronger teacher model (QwQ-32B) for data synthesis. Still purely neural with no formal verification component — verification CoT can hallucinate plausible-sounding but incorrect critiques.",
    "building_blocks": [
      "Generative verification CoT paradigm",
      "Process-filtered synthetic data pipeline",
      "Dual test-time scaling (parallel + sequential)",
      "LoRA-efficient PRM training"
    ],
    "relevance_to_seed": "Validates the generative PRM paradigm our neural verifier builds on; demonstrates that verification CoT dramatically outperforms discriminative scoring, motivating GenPRM-style neural verifier as the non-formal branch of our router."
  },
  {
    "title": "Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification",
    "venue": "arXiv 2026",
    "problem_identification": "Prior neuro-symbolic methods apply formal verification only as passive post-hoc validation, missing the opportunity to use formal signals during training. The gap is integrating formal verification as an active training signal that penalizes intermediate fallacies.",
    "key_insight": "Formal symbolic verification (Python/Z3/SMT solvers) can be dynamically interleaved with natural language generation during both SFT and RL stages, with a hierarchical reward structure that differentiates fatal failures, format errors, and logical correctness.",
    "innovation_type": "new_technique",
    "method_summary": "Stage 1 (SFT): Decomposes reasoning chains into logical modules, synthesizes formal proof
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
  "promptId": "d6ee2fe3-d930-414e-a289-dd5f30af565e",
  "type": "user",
  "uuid": "be69f467-89a6-4c86-9eef-0a921f2cbf1b",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "733f9e07-4f23-4518-9a71-bb860175df75",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-29T05:33:26.336Z_

```json
{
  "parentUuid": "be69f467-89a6-4c86-9eef-0a921f2cbf1b",
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
  "uuid": "779199b2-03e9-4835-96cd-d1996b78f74f",
  "timestamp": "2026-05-29T05:33:26.336Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "733f9e07-4f23-4518-9a71-bb860175df75",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-29T05:33:26.337Z_

```json
{
  "parentUuid": "779199b2-03e9-4835-96cd-d1996b78f74f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "482006cb-f65d-42b9-9574-a271041f8377",
  "timestamp": "2026-05-29T05:33:26.337Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "733f9e07-4f23-4518-9a71-bb860175df75",
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
  "leafUuid": "482006cb-f65d-42b9-9574-a271041f8377",
  "sessionId": "733f9e07-4f23-4518-9a71-bb860175df75"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Hybrid routing PRM for miracle step detection",
  "sessionId": "733f9e07-4f23-4518-9a71-bb860175df75"
}
```

---

### Assistant

_source line 8 · 2026-05-29T05:33:45.099Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to synthesize 21 paper analyses into a strategic "Field Guide" for a researcher working on hybrid formal/neural process reward models for detecting miracle steps in LLM reasoning. Let me carefully analyze the patterns, gaps, and opportunities across all these papers and produce a comprehensive JSON output.

Let me think through each section systematically:

**Innovation Patterns:**
1. Cross-domain transfer (formal verification → PRM training) - FoVer, Safe, VeriCoT
2. Generative reframing (classification → generation) - GenPRM, ThinkPRM
3. Hybrid neuro-symbolic combination - HERMES, VERGE, VeriCoT, the interleaved bonus paper


4. New evaluation taxonomies and benchmarks emerging across ProcessBench, PRMBench, and the survey work
5. Routing and dispatch mechanisms based on claim type - VERGE's approach
6. Lightweight formal representations like PRoSFI's structured intermediaries, SimpleMath's MATH-VF, and Typed CoT

**Reviewer Preferences:**
- Multi-domain evaluation (not just math)
- Clear differentiation from baselines
- Practical compute constraints
- Formal guarantees where possible
- Error taxonomy and fine-grained analysis

**Field Gaps:**
- No learned routing between formal and neural verifiers yet
- The formalizability spectrum remains uncharacterized
- Faithfulness of autoformalization approaches needs deeper investigation (around 43% faithful based on Risk-Controlled paper findings)
- Step-level formal verification at scale hasn't been achieved
- Detecting miracle steps through formal methods is still an open problem

**Untried Combinations:**
- VERGE routing combined with FoVer training data and GenPRM neural verifier
- PRoSFI intermediaries paired with a formalizability classifier
- ARES entailment framework integrated with Z3 formal checking
- Typed CoT certification alongside PRM training

**Method Building Blocks:**
- Z3 and SMT solvers for verification
- Lean 4 for step formalization
- GenPRM's RPE labeling approach
- VERGE's semantic routing
- VeriCoT's premise grounding
- SimpleMath's formalization language

**Common Pitfalls:**
- Overclaiming formal verification coverage
- Restricting evaluation to math domains
- Overlooking faithfulness issues in autoformalization
- Ignoring computational constraints without efficiency metrics

The field is moving toward hybrid systems that learn meta-reasoning about verification and generalize across multiple domains. I should focus on bridging the routing and formalizability gap, be transparent about coverage limitations, evaluate across diverse domains, and demonstrate that hybrid approaches outperform pure verification or pure learning methods.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "482006cb-f65d-42b9-9574-a271041f8377",
  "isSidechain": false,
  "requestId": "req_011CbWKCRtU7uHy3vtYzYM6A",
  "type": "assistant",
  "uuid": "232659ca-b142-40ca-944a-7898cdd6cb02",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "733f9e07-4f23-4518-9a71-bb860175df75",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ZM2GvPS9qUXXEFaRcZWEF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13032,
      "cache_read_input_tokens": 11014,
      "output_tokens": 7826,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13032,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 7826,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 13032,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13032
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

_source line 9 · 2026-05-29T05:36:40.923Z_

I'll analyze the 21 papers systematically to produce the field guide. Let me first do a careful cross-paper synthesis before generating the final output.

```json
{
  "innovation_patterns": [
    {
      "pattern": "Cross-Domain Transfer of Verification Signals",
      "description": "Taking verification infrastructure from one community (formal methods, theorem proving, type theory) and applying it to a problem owned by another community (PRM training, RLHF, LLM evaluation). The key move is recognizing that formal tools already produce the exact signal needed by the downstream task, but the communities don't talk to each other.",
      "examples": ["FoVer (formal verification → PRM training labels)", "Safe (Lean 4 theorem proving → step-level PRM scores)", "VeriCoT (Z3 entailment → SFT/DPO rewards)", "Typed Chain-of-Thought (Curry-Howard correspondence → CoT certification)"],
      "success_rate": "high"
    },
    {
      "pattern": "Generative Reframing of Discriminative Tasks",
      "description": "Replacing scalar classification heads with generative reasoning-then-judgment pipelines, unlocking test-time compute scaling via sampling/majority-voting. The insight is that verification is itself a reasoning task, not a classification task, and LLMs can explain why a step is wrong before deciding it is wrong.",
      "examples": ["GenPRM (generative PRM with CoT + code verification)", "ThinkPRM (verification chain-of-thought before scoring)"],
      "success_rate": "high"
    },
    {
      "pattern": "Lightweight Formal Representations as Bridge",
      "description": "Instead of requiring full formal proofs (intractable for small models), designing lightweight intermediate representations that capture enough formal structure for automated verification while remaining producible by 7B-scale models. The critical design choice is how much formality to demand.",
      "examples": ["PRoSFI (structured formal intermediaries as JSON)", "MATH-VF (SimpleMath extending FOL with math constants)", "Typed Chain-of-Thought (minimal type system with combinators)"],
      "success_rate": "medium"
    },
    {
      "pattern": "Interleaved Verification During Generation",
      "description": "Rather than verify-after-generate, integrating formal verification as a feedback signal during inference or training. Verification results are routed back to guide subsequent reasoning, creating a closed loop. The memory/state management between verification cycles is the engineering challenge.",
      "examples": ["HERMES (Lean 4 feedback loop during inference)", "Interleaved Bonus paper (formal signals during SFT and RL stages)", "MATH-VF (corrective feedback from SymPy/Z3)"],
      "success_rate": "medium"
    },
    {
      "pattern": "New Evaluation Taxonomy Revealing Hidden Failure Modes",
      "description": "Creating fine-grained benchmarks that decompose binary correctness into multiple orthogonal dimensions, revealing that existing methods fail in specific, previously invisible ways. These papers succeed by showing the field has been measuring the wrong thing.",
      "examples": ["ProcessBench (error localization vs. binary correctness)", "PRMBench (9-category error taxonomy)", "Evaluating Step-by-step Survey (4-dimension evaluation framework)", "Miracle Steps/RRM (6-type false-positive taxonomy)"],
      "success_rate": "high"
    },
    {
      "pattern": "Semantic Routing Between Heterogeneous Verifiers",
      "description": "Recognizing that different claim types demand different verification strategies, and building dispatch systems that route each claim to the appropriate verifier. Currently rule-based; learned routing is the clear next step.",
      "examples": ["VERGE (claim-type taxonomy → Z3 or neural ensemble)", "Safe (4-state verification taxonomy with implicit routing)"],
      "success_rate": "medium"
    }
  ],
  "reviewer_preferences": [
    "Multi-domain evaluation is essentially mandatory at top venues: papers restricted to GSM8K/MATH face skepticism about generality. ProcessBench succeeded at ACL 2025 by spanning four difficulty tiers; PRMBench by covering 9 error categories; FoVer by demonstrating transfer to NLI, BBH, and math. AAAI in particular values KR&R generality — include logic, math, code (LiveCodeBench), and science (GPQA).",
    "Honest reporting of coverage limits builds credibility: Risk-Controlled Lean-as-Judge was valued precisely because it quantified formalization faithfulness at 43% and coverage at 28-79%, rather than cherry-picking success cases. FoVer acknowledged overly-strict PRM behavior on informal reasoning. Papers that overclaim formal verification's reach get flagged.",
    "Compute-aware experimental design: papers accepted at top venues with academic compute budgets (FoVer on 8B, GenPRM showing 1.5B outperforming GPT-4o, ThinkPRM with 1K training examples via LoRA) earn reviewer goodwill. DeepSeek-Prover-V2's 671B model is explicitly noted as impractical for academic settings.",
    "Clear baseline differentiation with ablation chains: GenPRM's acceptance at AAAI 2026 was supported by systematic ablations (RPE vs. MC labels, code verification on/off, majority voting depth). PRoSFI's tiered reward ablation (1.0/0.3/0.1/0.0) shows each component's contribution. Reviewers reward understanding of WHY a method works, not just THAT it works.",
    "Formal guarantees, even partial, are valued over purely empirical claims: ARES's Hoeffding-bound statistical certification and VeriCoT's Z3 entailment/contradiction/consistency triple-check demonstrate that even approximate formal guarantees distinguish papers from incremental neural improvements.",
    "Error type analysis beyond binary localization: RRM's miracle step taxonomy (6 types) and PRMBench's 9-category error classification were rewarded because they enable diagnostic understanding. Papers that only report aggregate F1 miss the opportunity to show which specific failure modes their method addresses.",
    "Training data efficiency is increasingly valued: ThinkPRM's 100× data reduction (800K → 8K labels) and FoVer's automated synthesis (eliminating human annotation) both address the field's data bottleneck. Reviewers are skeptical of methods requiring PRM800K-scale human annotation."
  ],
  "field_gaps": [
    {
      "gap": "No learned routing between formal and neural verifiers based on step-level formalizability",
      "evidence": "VERGE uses rule-based routing (94% accuracy but not learned from data); Safe attempts formalization on ALL steps regardless of formalizability; PRoSFI requires ALL steps to produce formal intermediaries; FoVer trains only on formally verifiable data. The VERGE paper explicitly notes that whether a learned router would outperform rule-based routing is an open question.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Autoformalization faithfulness is catastrophically low and unaddressed",
      "evidence": "Risk-Controlled Lean-as-Judge reveals only ~43% of successful proofs are faithful to the original problem statement. Structural proofs often assert true-but-irrelevant claims. No paper proposes a solution to the faithfulness gap at the step level — all focus on coverage (can we formalize?) not faithfulness (did we formalize the right thing?).",
      "difficulty": "high",
      "impact_if_solved": "high"
    },
    {
      "gap": "The formalizability spectrum has not been characterized or exploited",
      "evidence": "Typed Chain-of-Thought observes 40-60% full typing success empirically. Safe reports 72-82% proof rates varying by math domain. Risk-Controlled reports 28-79% coverage depending on prover specialization. But no paper systematically characterizes WHICH steps are formalizable, WHY, or how partial formalizability (some sub-claims expressible, others not) should be handled. VeriCoT acknowledges an 'untranslatable' category but doesn't quantify its frequency.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Formal derivability from predecessors (not just step correctness) is untested for miracle step detection",
      "evidence": "ARES checks entailment from predecessors but uses neural NLI models, not formal logic. FoVer's Z3 checks step validity given premises independently but doesn't specifically target derivability from preceding reasoning steps. RRM detects miracle steps via neural rubrics. No system checks whether step S_i is formally derivable from {S_1,...,S_{i-1}} using proof-assistant-grade tools — the theoretical anchor of the seed direction.",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Long reasoning chains degrade all existing verification methods",
      "evidence": "The Evaluating Step-by-step Survey identifies inability to handle long traces as one of five critical gaps. ARES's Monte Carlo approximation has untested convergence on deeply nested chains. ProcessBench shows PRMs catastrophically fail on harder problems (which tend to have longer chains). No paper addresses the O(n²) dependency explosion in step-level verification for chains exceeding ~20 steps.",
      "difficulty": "high",
      "impact_if_solved": "medium"
    },
    {
      "gap": "No step-level error TYPE classification in formal verification frameworks",
      "evidence": "ProcessBench identifies error location but not error type. PRMBench provides 9 error categories but no formal verification approach. RRM taxonomizes miracle steps but uses neural detection. The intersection — formal verification that diagnoses error TYPE (not just presence) — is completely empty. Which of PRMBench's 9 categories would benefit from formal vs. neural verification is unstudied.",
      "difficulty": "medium",
      "impact_if_solved": "medium"
    },
    {
      "gap": "Formal verification for non-mathematical domains (code, science, legal) is underdeveloped for PRM training",
      "evidence": "VeriCoT tests on legal (LegalBench) and biomedical (BioASQ) but without PRM training. FoVer is logic + math only. Safe is math only. MATH-VF's SimpleMath is explicitly limited to math. No formal PRM training pipeline exists for code verification (despite mature tools like Dafny, Coq) or scientific reasoning (despite domain ontologies).",
      "difficulty": "medium",
      "impact_if_solved": "high"
    },
    {
      "gap": "Integration of formal verification into RL training loops (not just SFT/evaluation)",
      "evidence": "The Interleaved Bonus paper begins addressing this but is unpublished/arXiv-only. FoVer uses formal labels for SFT only. VeriCoT uses them for SFT and DPO but not PPO/GRPO. GenPRM uses code execution but not formal proof verification during RL. PRoSFI uses GRPO with formal verification but only for fully formalizable logic problems. The gap is formal verification as a dense reward signal during RL training on partially-formalizable problems.",
      "difficulty": "high",
      "impact_if_solved": "high"
    }
  ],
  "untried_combinations": [
    {
      "idea_sketch": "Learned formalizability router (trained on FoVer's verified labels as ground truth) dispatching steps to Z3/Lean 4 formal verifier or GenPRM-style neural verifier, with router confidence calibrated via ARES-style Hoeffding bounds, specifically targeting miracle step detection using RRM's taxonomy as evaluation criteria",
      "from_papers": ["FoVer", "VERGE", "GenPRM", "ARES", "RRM/Miracle Steps", "Risk-Controlled Lean-as-Judge"],
      "why_promising": "VERGE proves routing works (18.7% uplift) but uses rules not learning; FoVer provides ground truth for router training; GenPRM provides the neural branch; ARES provides statistical certification; RRM provides the evaluation target. No paper combines all five elements. The learned router exploits formalizability structure that no existing PRM uses."
    },
    {
      "idea_sketch": "PRoSFI's structured formal intermediaries as the representation layer for a formalizability classifier — instead of classifying raw NL steps, classify the intermediary's completeness (how many fields can be filled with verified content) as the formalizability score",
      "from_papers": ["PRoSFI", "Typed Chain-of-Thought", "VeriCoT"],
      "why_promising": "PRoSFI's JSON format (id, dependencies, conclusion, inference_rule) provides a natural granularity for measuring partial formalizability — a step where 3/4 fields are verifiable scores 0.75. Typed CoT's coverage metric (proportion typed) validates this approach empirically. This avoids the binary formalize-or-not limitation of all current systems."
    },
    {
      "idea_sketch": "ARES's autoregressive premise-subset entailment framework but replacing the neural NLI model with Z3 formal derivability checking for formalizable steps, creating a hybrid soundness propagation that is formal where possible and probabilistic elsewhere",
      "from_papers": ["ARES", "FoVer", "VeriCoT"],
      "why_promising": "ARES's mathematical framework for propagating soundness through chains is elegant but bottlenecked by neural entailment quality. Replacing the entailment oracle with Z3 for formalizable steps would give exact (not approximate) derivability judgments where the formalization succeeds, while preserving the probabilistic fallback. This directly tests whether formal derivability outperforms neural entailment for miracle step detection."
    },
    {
      "idea_sketch": "DeepSeek-Prover-V2's recursive subgoal decomposition applied to step-level verification — decompose each reasoning step's verification into sub-verification goals, enabling formal checking of step COMPONENTS even when the whole step is not formalizable",
      "from_papers": ["DeepSeek-Prover-V2", "Safe", "MATH-VF"],
      "why_promising": "Current approaches treat formalizability as binary (whole step formalizable or not). Decomposing verification into subgoals allows partial formal coverage per step — e.g., the algebraic manipulation is Z3-verifiable while the problem interpretation is not. This is the sub-claim level formalizability the seed direction theorizes about but no paper implements."
    },
    {
      "idea_sketch": "HERMES's inference-time interleaved verification loop but driven by a trained PRM (from FoVer/GenPRM) rather than raw Lean 4 proof success, enabling soft verification signals that can guide exploration even when formal proof fails",
      "from_papers": ["HERMES", "FoVer", "GenPRM"],
      "why_promising": "HERMES gets binary Lean 4 signals (proved/not proved) which are uninformative when proof fails. A PRM trained on FoVer's formal data would provide continuous reward signals even for unprovable steps, enabling gradient-based guidance of the inference loop. This combines HERMES's architecture with FoVer's training methodology."
    },
    {
      "idea_sketch": "RRM's rubric synthesis pipeline but with rubrics grounded in formal derivability criteria — instead of Gemini generating heuristic rubrics, auto-generate rubrics from the formal specification of what inference rules should apply at each step, making rubrics verifiable rather than neural",
      "from_papers": ["RRM/Miracle Steps", "PRoSFI", "VeriCoT"],
      "why_promising": "RRM's 71% miracle step reduction is impressive but rubrics are neural artifacts dependent on proprietary Gemini-2.5-Pro. PRoSFI's inference rule specifications (Modus Ponens, Hypothetical Syllogism, etc.) could serve as formally-grounded rubrics, replacing neural heuristics with checkable criteria. The remaining 29% of miracle steps RRM misses may be exactly those requiring formal grounding."
    }
  ],
  "method_building_blocks": [
    {
      "tool": "Z3 SMT Solver for Step-Level Verification",
      "what_it_does": "Checks satisfiability/entailment of first-order logic formulas with theories (arithmetic, bitvectors, arrays). For PRM use: given premises (prior steps formalized as FOL), check whether the current step's formalization is entailed. Returns SAT/UNSAT/UNKNOWN with counterexamples.",
      "used_by": ["FoVer (step validity)", "VERGE (SMT-amenable claims)", "VeriCoT (entailment/contradiction/consistency)", "MATH-VF (logical constraint checking)"],
      "could_be_applied_to": "Formal derivability checking for miracle step detection — specifically testing whether S_i is derivable from {S_1,...,S_{i-1}} under known inference rules, with timeout → miracle step candidate"
    },
    {
      "tool": "Lean 4 REPL Integration",
      "what_it_does": "Compiles Lean 4 tactic proofs interactively, returning proof state after each tactic. For PRM use: auto-formalize a reasoning step as a Lean 4 theorem statement, attempt automated proof, interpret success/failure as verification signal.",
      "used_by": ["Safe (step-level theorem statements)", "HERMES (inference-time verification)", "DeepSeek-Prover-V2 (subgoal proving)"],
      "could_be_applied_to": "Higher-order logic verification for steps beyond FOL expressiveness (e.g., induction, set theory arguments) — complementing Z3's FOL/SMT coverage"
    },
    {
      "tool": "GenPRM's Relative Progress Estimation (RPE)",
      "what_it_does": "Computes step-level labels by measuring whether a step increases the probability of reaching the correct answer, estimated via Monte Carlo sampling of continuations from each step. Labels are relative (progress vs. regression) rather than absolute (correct vs. incorrect).",
      "used_by": ["GenPRM"],
      "could_be_applied_to": "Generating soft labels for the neural verifier branch of a hybrid router — RPE labels capture utility/progress that formal verification cannot assess, providing complementary signal to formal derivability"
    },
    {
      "tool": "Autoformalization with Semantic Equivalence Consensus",
      "what_it_does": "Generates K candidate formalizations per NL claim, checks pairwise bidirectional entailment, selects the consensus formalization. Reduces single-point autoformalization failure by requiring agreement across multiple attempts.",
      "used_by": ["VERGE (K=3 candidates with entailment checking)"],
      "could_be_applied_to": "Improving autoformalization faithfulness — the 43% faithfulness rate (Risk-Controlled) could be significantly improved by requiring consensus across multiple independent formalizations before trusting the formal verification result"
    },
    {
      "tool": "Structured Formal Intermediaries",
      "what_it_does": "Lightweight JSON representations (id, dependencies, conclusion, inference_rule) that a 7B model can produce alongside natural language, enabling formal verification without full proof generation. Each intermediary specifies its logical dependencies and the rule applied.",
      "used_by": ["PRoSFI"],
      "could_be_applied_to": "Formalizability score computation — the completeness and verifiability of each field in the intermediary naturally quantifies how formalizable a step is, enabling continuous (not binary) formalizability assessment"
    },
    {
      "tool": "Tiered GRPO Reward Scheme",
      "what_it_does": "Assigns different reward levels based on multiple quality dimensions (correctness + verification status + format compliance), enabling nuanced RL training beyond binary rewards. PRoSFI uses 1.0/0.3/0.1/0.0.",
      "used_by": ["PRoSFI", "Interleaved Bonus paper"],
      "could_be_applied_to": "Training the formalizability router via RL — reward tiers could encode: 1.0 (correctly routed to formal, verified), 0.7 (correctly routed to neural, high-confidence), 0.3 (routed to formal but timed out, neural fallback agrees), 0.0 (misrouted, disagreement between verifiers)"
    },
    {
      "tool": "MCS-Based Error Localization",
      "what_it_does": "Computes Minimal Correction Subsets — the smallest set of claims whose removal makes the remaining set satisfiable — to precisely identify which specific claims cause logical inconsistency. Uses greedy O(n×SAT) approximation.",
      "used_by": ["VERGE"],
      "could_be_applied_to": "Precise miracle step identification — rather than flagging a step as entirely unjustified, MCS can pinpoint which specific sub-claims within a step lack derivability support, enabling more targeted feedback"
    },
    {
      "tool": "CovCal Risk-Controlled Selector",
      "what_it_does": "Uses diagnostic features from verification traces (typed coverage, proved coverage, unresolved rival mass, formal margin) to decide when formal verification results are trustworthy enough to use, with statistical guarantees on error rate.",
      "used_by": ["Risk-Controlled Lean-as-Judge"],
      "could_be_applied_to": "Router confidence calibration — instead of always trusting the formal verifier when it returns a result, use CovCal-style diagnostics to assess whether the formal verification is reliable for this specific step, falling back to neural when confidence is low"
    }
  ],
  "common_pitfalls": [
    "Overclaiming formal verification coverage: Risk-Controlled Lean-as-Judge shows baseline autoformalization covers only 28% of problems, and even specialized provers reach only 79%. Worse, only 43% of successful proofs are faithful. Papers that assume 'formal verification = ground truth' without quantifying coverage AND faithfulness will be rejected. Always report formalization success rate, proof rate, and (ideally) faithfulness rate separately.",
    "Math-only evaluation at AAAI: ProcessBench, MATH-VF, Safe, and PRoSFI all evaluate exclusively on math. AAAI's KR&R track values generality. VeriCoT's strength was multi-domain evaluation (legal, biomedical). Include at least three domains: math (ProcessBench/MATH), logic (FoVer's FLDx2/ProverQA), and one non-math domain (code via LiveCodeBench, science via GPQA).",
    "Ignoring the naive baseline trap: A simple 'try formal, fall back to neural on timeout' baseline captures ~60% of a learned router's benefit. If the learned router doesn't demonstrably outperform this on partial-formalizability cases (where some but not all sub-claims are formalizable), reviewers will question the contribution. The ablation against the naive fallback is the most important experiment.",
    "Conflating step correctness with step derivability: FoVer's Z3 checks whether a step is valid given premises. ARES checks whether a step is entailed by predecessors. These are different: a step can be correct (true in the domain) but not derivable from preceding steps (a miracle step). Papers that claim to detect miracle steps but only check correctness miss the point. The derivability framing requires checking S_i against {S_1,...,S_{i-1}}, not against domain axioms.",
    "Requiring proprietary model dependencies: RRM depends on Gemini-2.5-Pro for rubric synthesis; ThinkPRM depends on QwQ-32B for data generation. Reviewers flag reproducibility concerns. Use open-source models (Llama, Qwen, DeepSeek) for all pipeline components, or at minimum provide ablations showing the method works with open alternatives.",
    "Treating formal verification as a black box without error analysis: When Z3 returns UNKNOWN or times out, that's information — it may indicate the step is at the boundary of formalizability. Papers that discard timeout cases miss the opportunity to analyze the formalizability frontier. Report distributions of verification outcomes (proved/disproved/timeout/formalization-failed) and analyze what distinguishes each category.",
    "Underestimating computational overhead without mitigation: Safe reports 4-8× overhead. HERMES mitigates with parallel Lean compilation and memory modules. MATH-VF exploits dependency graph sparsity (O(n×M) where M≤4 instead of O(n²)). Papers that add formal verification without addressing the compute cost will face reviewer pushback at the 7B/academic-compute scale. Budget formal verification CPU time separately and show it fits within constraints.",
    "Training on synthetic errors instead of naturally occurring ones: FoVer explicitly uses naturally occurring LLM errors rather than injected errors, and this is a noted strength. Synthetic error injection creates distribution mismatch — models learn to detect artificial patterns rather than real failure modes. Use natural LLM generation errors wherever possible.",
    "Evaluating only accuracy without analyzing error types: PRMBench shows that aggregate accuracy masks dimension-specific failures — a PRM might score well overall while completely failing on deception resistance or circular logic. Report performance broken down by error category (using PRMBench's 9 categories or RRM's 6 miracle step types) to show where formal verification specifically helps."
  ],
  "field_trajectory": "The field is converging on three macro-directions. First, hybrid neuro-symbolic verification is replacing the false binary of 'all formal' vs. 'all neural' — VERGE, HERMES, and VeriCoT all demonstrate that routing between verification modalities outperforms either alone, and the next frontier is making this routing learned rather than heuristic. The formalizability spectrum (empirically 40-60% full coverage per Typed CoT, 28-79% per Risk-Controlled) is now accepted as a structural feature of the problem, not a limitation to be overcome. Second, verification is moving from post-hoc evaluation to active training signal — FoVer showed formal labels can train PRMs, VeriCoT showed they can drive DPO, the Interleaved Bonus paper shows they can shape RL rewards, and the trajectory points toward formal verification as a dense, per-step reward signal during online RL training. This closes the loop between verification and generation. Third, the generative PRM paradigm (GenPRM, ThinkPRM) is becoming dominant over discriminative scoring because it enables test-time compute scaling — the question is no longer 'how good is the PRM' but 'how much compute can the PRM productively absorb.' The intersection of these three trends — a hybrid router that generates verification rationales, routes to formal/neural verifiers, and produces rewards for RL training — is the natural next system. The 2026-2027 papers that will define the field will be those that build this integrated pipeline while being honest about coverage limits and demonstrating multi-domain generality. The wild card is whether autoformalization faithfulness (currently ~43%) can be improved enough to make formal signals reliable, or whether the field will need to develop formal-signal-confidence-aware training methods that weight formal rewards by their estimated faithfulness.",
  "meta_advice": "If I were advising a PhD student targeting AAAI 2026/2027 in this space, here is what I would say. First, your core contribution must be the learned formalizability router — this is the gap that every paper touches but none fills. VERGE proves routing works but uses rules; Safe and PRoSFI require all steps to be formalizable; FoVer trains only on formal data. The router that learns WHEN to trust formal verification is genuinely novel and sits at the intersection that no existing research group occupies (formal methods people don't do PRM training; PRM people don't do formal verification). Second, invest heavily in the naive-baseline ablation: run Z3 on every step with a 30-second timeout and fall back to GenPRM. If your learned router doesn't beat this by >5% on miracle step detection, the paper is dead. The learned router must show value specifically on partially-formalizable steps — those where some sub-claims are Z3-expressible and others aren't. Third, use FoVer's codebase and data as infrastructure (it's public, it works, and it gives you formal ground truth for router training), but clearly differentiate by showing that your hybrid system outperforms FoVer-trained PRMs on non-formalizable reasoning tasks — this is where pure formal approaches fail and your neural fallback proves essential. Fourth, evaluate on ProcessBench (primary, math), FoVer's FLDx2 (logic), and at least one non-math domain. GPQA for science reasoning is ideal — it's hard enough that miracle steps are common and diverse enough that formalizability varies widely. Fifth, be brutally honest about formal verification's limitations: report formalization success rate, proof rate, faithfulness estimate, and timeout distribution. The Risk-Controlled paper succeeded by quantifying failure modes; overclaiming will sink you. Sixth, frame the paper around the theoretical anchor 'reward = derivability' — this connects PRMs to classical proof theory and gives AAAI's KR&R reviewers something intellectually satisfying beyond empirical gains. The Curry-Howard connection from Typed CoT provides theoretical backing, and ARES's statistical framework provides the rigor. Finally, budget your 200 H100-hours carefully: router training (~10h), 7B PRM fine-tuning (~50h), and evaluation (~40h) leave ~100h for formal verification CPU time and ablation experiments. Use MATH-VF's dependency graph sparsity trick to keep Z3 calls manageable, and parallelize Lean 4 compilation following HERMES's verification scheduler pattern."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "232659ca-b142-40ca-944a-7898cdd6cb02",
  "isSidechain": false,
  "requestId": "req_011CbWKCRtU7uHy3vtYzYM6A",
  "type": "assistant",
  "uuid": "df76c8bd-635b-4fcc-adfa-30c78fbfbf1a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "733f9e07-4f23-4518-9a71-bb860175df75",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ZM2GvPS9qUXXEFaRcZWEF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13032,
      "cache_read_input_tokens": 11014,
      "output_tokens": 7826,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13032,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 7826,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 13032,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13032
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
  "leafUuid": "df76c8bd-635b-4fcc-adfa-30c78fbfbf1a",
  "sessionId": "733f9e07-4f23-4518-9a71-bb860175df75"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Hybrid routing PRM for miracle step detection",
  "sessionId": "733f9e07-4f23-4518-9a71-bb860175df75"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a senior ML research advisor synthesizing a literature review into an actionable research strategy.  **Today's date: 2026-05-29 (UTC).**  ## Research area: Target: AAAI 2026 (or AAAI 2027 if d…",
  "leafUuid": "df76c8bd-635b-4fcc-adfa-30c78fbfbf1a",
  "sessionId": "733f9e07-4f23-4518-9a71-bb860175df75"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Hybrid routing PRM for miracle step detection",
  "sessionId": "733f9e07-4f23-4518-9a71-bb860175df75"
}
```

---
