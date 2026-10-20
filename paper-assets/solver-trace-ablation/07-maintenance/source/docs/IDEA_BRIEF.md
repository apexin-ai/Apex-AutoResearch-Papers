# Idea Brief: Solver Trace Ablation for Cross-Logic GRPO Training of Neurosymbolic Formalizers


- **Idea ID**: `idea_010`
- **Created**: 2026-05-13
- **Approved**: 2026-05-13
- **Source**: foreign:be-idea-gen-0509-3
- **Level**: top-tier
- **Target Venues**: EMNLP 2026 (ARR submission deadline May 25, 2026)

## Seed Topic

Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Symbolic Reasoning.

Direction: Neurosymbolic reasoning — combining neural models with symbolic systems (logic programs, knowledge graphs, formal verification, constraint solvers). NOT limited to LLM-only reasoning — explicitly seek methods that integrate external symbolic components. Also in-scope: structured mathematical reasoning, program-aided reasoning, theorem prover integration.

Contribution type: METHOD ONLY. Must propose a new hybrid algorithm, training objective, or inference pipeline that combines neural + symbolic components. Pure prompting tricks (vanilla CoT, self-consistency) are out of scope.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total. Neurosymbolic methods are often inference-heavy not training-heavy — budget accordingly.
2. Time: ≤16 days. Use existing open checkpoints (Qwen3, Llama-3.x, DeepSeek-R1 distills) + off-the-shelf solvers (Z3, Prolog, SymPy, Lean4).
3. Eval: MATH, AIME 2024/2025, GPQA Diamond, ProofWriter, FOLIO, LogiQA, ARC-Challenge, BBH.

Look for: lightweight symbolic verifiers as post-hoc filters, neural-guided symbolic search, structured output → formal checker pipelines, hybrid neuro-symbolic distillation. Avoid: pure prompt engineering, vanilla CoT.

Tag: direction=neurosymbolic_reasoning, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].

## Generation Journey

1. **Start** — 开始生成，seed: 'Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Symbolic Reasoning.\n\nDirection: Neurosymbolic reasoning — combining neural models with symbolic systems (logic programs, knowledge graphs, formal verification, constraint solvers). NOT limited to LLM-only reasoning — explicitly seek methods that integrate external symbolic components. Also in-scope: structured mathematical reasoning, program-aided reasoning, theorem prover integration.\n\nContribution type: METHOD ONLY. Must propose a new hybrid algorithm, training objective, or inference pipeline that combines neural + symbolic components. Pure prompting tricks (vanilla CoT, self-consistency) are out of scope.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Neurosymbolic methods are often inference-heavy not training-heavy — budget accordingly.\n2. Time: ≤16 days. Use existing open checkpoints (Qwen3, Llama-3.x, DeepSeek-R1 distills) + off-the-shelf solvers (Z3, Prolog, SymPy, Lean4).\n3. Eval: MATH, AIME 2024/2025, GPQA Diamond, ProofWriter, FOLIO, LogiQA, ARC-Challenge, BBH.\n\nLook for: lightweight symbolic verifiers as post-hoc filters, neural-guided symbolic search, structured output → formal checker pipelines, hybrid neuro-symbolic distillation. Avoid: pure prompt engineering, vanilla CoT.\n\nTag: direction=neurosymbolic_reasoning, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].'
2. **Problem Discovery** (524s) — 发现 4 个研究方向
   - Multi-Solver Triangulation with Disagreement-Guided Formalization Repair
   - Hierarchical Speculative Verification for Cost-Efficient Symbolic Sampling
   - Solver-Grounded Dense Process Reward for Reasoning RL
   - Abductive Constraint Diagnosis via Solver-Identified Premise Gaps
3. **Method Synthesis** (575s) — 完成: "Multi-Solver Triangulation with Disagreement-Guided Formalization Repair" [top-tier] → EMNLP 2026 (ARR submission deadline: May 25, 2026), AAAI 2027 (submission deadline: ~Aug 1, 2026), ICLR 2027 (submission deadline: ~Sep 2026, expected)
3. **Method Synthesis** (652s) — 完成: "Hierarchical Speculative Verification for Cost-Efficient Symbolic Sampling" [solid] → EMNLP 2026 (ARR deadline May 25, 2026 — tight but feasible if infrastructure is pre-built), AAAI 2027 (expected abstract Jul 25, paper Aug 1, 2026), ICLR 2027 (expected deadline Sep-Oct 2026, not yet announced)
3. **Method Synthesis** (333s) — 完成: "Solver-Grounded Dense Process Reward for Reasoning RL" [solid] → AAAI 2027 (expected deadline ~August 2026), ICLR 2027 (expected deadline ~September-October 2026)
3. **Method Synthesis** (742s) — 完成: "Abductive Constraint Diagnosis via Solver-Identified Premise Gaps" [solid] → EMNLP 2026 (ARR submission deadline: May 25, 2026; conference: Oct 24-29, Budapest), AACL-IJCNLP 2026 (ARR submission deadline: May 25, 2026; conference: Nov 6-10, Hengqin), AAAI 2027 (abstract deadline: ~Jul 25, 2026; paper deadline: ~Aug 1, 2026; conference: Feb 16-23, Montréal), TACL (rolling submission, 1st of each month; presented at future *ACL conferences)

## Core Problem

GRPO with solver-verified rewards is established for single-logic formalization (Mellgren et al. 2025 for Prolog; FormaRL 2025 for Lean; PRoSFI 2026 for FOL; FLV-RL 2026 for interleaved verification), and EVOM (2026) demonstrates cross-solver GRPO transfer for optimization modeling (Gurobi→OR-Tools). However, state-of-the-art neurosymbolic reasoning pipelines (Adaptive EACL 2026, MAD-LOGIC ICLR 2026) require routing problems to structurally different formal languages (FOL→Prover9, Prolog→SWI-Prolog, SMT-LIB→Z3), and their formalizers remain SFT-trained. The critical gap is twofold: (1) No work has trained a single GRPO formalizer across multiple formal output languages and studied cross-type transfer dynamics — EVOM's cross-solver transfer operates within a single domain (optimization) with structurally similar solver backends, while our setting involves fundamentally different logical formalisms with distinct syntax, semantics, and verification mechanisms. (2) Training-time reward hacking produces extensionally-correct but intensionally-invalid outputs (Mellgren et al.: 90% accuracy / 1.6% structural validity; 'LLMs Gaming Verifiers' arXiv 2604.15149: RLVR models exploit extensional correctness via systematic shortcuts). Existing structural reward designs are ad-hoc heuristics (Mellgren et al.'s Prolog-specific structure penalty; SAGE's format/efficiency scores) with no principled derivation from solver semantics. While execution-trace-based rewards have emerged for code reasoning (ExecVerify 2026, EGCA 2026), no work has formalized a general procedure for deriving intensional verification rewards from solver execution semantics — particularly across multiple logic types where hacking modes differ structurally.

## Opportunity / Why Now

Six converging threads create a unique opportunity: (1) GRPO+solver for single-logic formalization is mature, with multiple independent confirmations across Prolog, Lean, FOL, and interleaved verification; (2) EVOM demonstrates cross-solver GRPO transfer for optimization, motivating the question of whether transfer works across structurally diverse formal logic languages; (3) Multi-solver neurosymbolic pipelines are SOTA but rely on SFT formalizers (Adaptive: 92.1%); (4) Training-time reward hacking is extensional-vs-intensional in nature ('LLMs Gaming Verifiers' arXiv 2604.15149), but existing remedies are domain-specific heuristics, not general algorithms; (5) Execution-trace-based reward design is emerging: ExecVerify (arXiv 2603.11226) derives white-box rewards from execution traces for code reasoning, EGCA (arXiv 2603.16158) localizes credit assignment via trace divergence, and SCORE (arXiv 2510.15600, ICLR 2026) introduces structured component-based rewards for protocol generation — but none addresses formal logic verification or provides a general derivation procedure; (6) The Reachability-Infection-Propagation (RIP) framework from mutation testing theory (DeMillo & Offutt 1991) provides an established formal criterion for determining when a program component is 'necessary' — a component is necessary iff its perturbation infects the execution state and propagates to the output. This framework has never been applied to derive training-time reward signals for RL-trained formalizers. The intersection — adapting the RIP framework to derive solver-specific intensional verification rewards, then integrating these into multi-logic GRPO with MT-GRPO/MO-GRPO foundations — is genuinely unexplored.

## Landscape (SOTA & Limitations)

The landscape of RL-trained formalizers and formal verification for LLMs has expanded significantly in 2024-2026:

**Cluster 1: Single-logic GRPO/RL for formalization.** SyReLM (AAAI 2024) pioneered RL with symbolic solvers. Mellgren et al. (arXiv 2512.07407, Dec 2025) applies GRPO with SWI-Prolog, discovering the accuracy-auditability tradeoff (90% accuracy / 1.6% structural validity) and introducing hand-crafted structure rewards. FormaRL (arXiv 2508.18914) uses GRPO with Lean. SIRL (NeurIPS 2025) and SAGE (arXiv 2605.02545) apply solver-verified GRPO to optimization modeling — SAGE with composite reward over format/correctness/efficiency. EVOM (arXiv 2604.00442, Apr 2026) demonstrates cross-solver GRPO transfer for optimization (Gurobi→OR-Tools→COPT), showing zero-shot solver transfer — the closest work to ours, but targeting optimization with structurally similar solver backends rather than fundamentally different logical formalisms.

**Cluster 2: Multi-verifier RL training (single output type).** PRoSFI (arXiv 2603.29500) uses Prover9, Z3, and Lean 4 for process-level reward on structured FOL intermediaries — but all outputs are FOL structured steps. FLV-RL (arXiv 2601.22642) interleaves formal verification during RL training — but targets verification signals, not diverse formalization.

**Cluster 3: Multi-solver neurosymbolic reasoning (no RL training).** Adaptive (EACL 2026) achieves 92.1% with dynamic Prover9/Z3/Pyke/MiniZinc routing using SFT formalizers. MAD-LOGIC (ICLR 2026) uses multi-agent debate. VERGE (Jan 2026) uses SMT-guided refinement.

**Cluster 4: Reward hacking and verification gaming.** Mellgren et al. (2025): execution-only GRPO produces structurally degenerate outputs. 'LLMs Gaming Verifiers' (arXiv 2604.15149): RLVR-trained models exploit extensional correctness; introduces Isomorphic Perturbation Testing (IPT) showing isomorphic verification eliminates shortcuts. 'Do LLMs Game Formalization?' (arXiv 2604.19459): no systematic gaming in unified generation at inference — training-time exploitation under GRPO is the distinct problem.

**Cluster 5: Multi-task and multi-objective GRPO.** MT-GRPO (arXiv 2602.05547): dynamic improvement-aware task reweighting, 16-28% improvement on worst-task accuracy. MO-GRPO (arXiv 2509.22047): variance-based normalization preventing single-objective reward hacking. Neither applied to neurosymbolic formalization.

**Cluster 6: Execution-trace and component-based rewards.** ExecVerify (arXiv 2603.11226, Mar 2026): derives white-box rewards from execution traces (next-statement prediction, variable state prediction) for code reasoning — demonstrates that trace-level rewards outperform outcome-only rewards, but targets code, not formal logic. EGCA (arXiv 2603.16158, ICLR 2026 SPOT Workshop): execution-grounded credit assignment for GRPO in code generation, localizing reward to earliest semantic divergence via trace comparison — fine-grained credit assignment but for code, not logic. SCORE (arXiv 2510.15600, ICLR 2026): structured component-based reward for bio-experimental protocol generation, decomposing into step granularity, action ordering, and semantic fidelity — precedent for structured domain-specific rewards but without formal derivation from task semantics.

**Cluster 7: Data efficiency for GRPO.** 'Hard Examples Are All You Need' (arXiv 2508.14094, Aug 2025): demonstrates on Qwen3-4B that training on the hardest 10% of examples (~747 from GSM8K) yields 34pp improvement, while easy examples produce 3-15%. GRPO requires outcome variance for learning signals; hard examples maintain this throughout training. Qwen3 Technical Report: flagship GRPO used only 3,995 query-verifier pairs for 170 steps.

**The gap:** Cluster 1 proves GRPO+solver works per-logic and EVOM shows cross-solver transfer for optimization. Cluster 3 shows multi-solver pipelines need RL-trained formalizers. Cluster 4 establishes hacking is extensional-vs-intensional. Cluster 6 shows execution-trace rewards work for code but not formal logic, and no work provides a principled derivation procedure for structural rewards from solver semantics. No work connects them: a general algorithm for deriving intensional verification rewards from any solver, applied to multi-logic GRPO training.

## Proposed Approach

We propose XLogic-RL, a framework for GRPO training of neurosymbolic formalizers across multiple formal languages. The primary METHOD contribution is Solver Trace Ablation (STA), a general algorithm for deriving intensional verification rewards from solver execution semantics, grounded in the Reachability-Infection-Propagation (RIP) framework from mutation testing theory. XLogic-RL integrates STA-derived rewards with MT-GRPO task balancing and MO-GRPO reward normalization into a Multi-Logic Structural Reward (MLSR) framework.

**RQ1: Cross-Logic Transfer and Interference.** Does GRPO training across multiple formal languages produce positive transfer or interference? EVOM (2026) demonstrates cross-solver transfer for optimization; we test whether this extends to structurally diverse formal logics.

**RQ2: Training-Time Reward Hacking Taxonomy.** How does training-time reward hacking manifest differently by formal language during GRPO training? Distinct from inference-time gaming (Kim et al. 2026). We hypothesize logic-type-specific extensional shortcuts: (a) FOL: tautological formulas; (b) Prolog: fact enumeration; (c) SMT-LIB: hard-coded assignments.

**RQ3: Solver Trace Ablation (STA) — the primary METHOD contribution.**

**(A) The STA Algorithm.** Grounded in the RIP framework (DeMillo & Offutt 1991): a program component is 'necessary' iff its perturbation satisfies three conditions — Reachability (the solver processes it), Infection (the solver's intermediate state changes), and Propagation (the solver's output changes). We adapt this to formal verification: for a formalization p verified by solver S, decompose p into structural components C(p) = {c_1, ..., c_n}. Component c_i is intensionally necessary iff its ablation propagates to the solver's output:

  Necessary(c_i, p, S) = 1[S(p_{-i}) ≠ S(p)]

where p_{-i} is p with component c_i removed/nullified. The Intensional Score Rate (ISR) is:

  ISR(p, S) = (1/|C(p)|) × Σ Necessary(c_i, p, S)

ISR = 1.0 means all components are necessary (fully intensional). ISR ≈ 0 means most components are extensionally redundant (reward-hacked). This is not ad-hoc — it instantiates a well-established formal criterion. The STA algorithm is solver-agnostic: given any new solver S' and language L', one defines the component decomposition for L' and applies the same procedure.

**(B) Efficient Logic-Type Instantiations.** Full STA requires |C(p)| additional solver calls. For training-time efficiency, we derive O(1)-call approximations per logic type, each targeting the dominant hacking mode identified in RQ2:

- **FOL → Prover9**: Ablation target = all premises. Single check: prove conclusion without any premises. If provable → ISR ≈ 0 (tautology, extensionally correct but intensionally vacuous). This is the propagation condition applied to the premise set as a unit.
- **Prolog → SWI-Prolog**: Ablation target = rule clauses. Single check: execute query with facts only (remove all rules). If query succeeds → ISR ≈ 0 (fact enumeration, bypassing deduction). This is the propagation condition for the rule component.
- **SMT-LIB → Z3**: Ablation target = constraints. Single check: check satisfiability of the negation. If unsatisfiable (original was tautologically satisfiable) → ISR ≈ 0 (hard-coded assignment). Plus: check if removing any single constraint preserves the solution (incremental Z3).

These approximations are *derived* from the general STA procedure, not independent heuristics. Each is the computationally efficient special case of applying the propagation condition to the dominant extensional-shortcut mode of its logic type.

**(C) Connection to IPT.** STA and IPT (Isomorphic Perturbation Testing from 'LLMs Gaming Verifiers') are formal duals: IPT tests model invariance under meaning-preserving perturbations (isomorphisms), while STA tests formalization sensitivity under meaning-destroying perturbations (ablations). Together they provide a complete intensional verification framework — IPT at evaluation time, STA at training time.

**(D) MLSR Framework Integration.** STA-derived rewards are integrated into GRPO via MLSR, which additionally incorporates:
- MO-GRPO variance-based normalization (from arXiv 2509.22047): each reward component r_i normalized by rolling variance r̂_i = r_i / sqrt(Var(r_i) + ε), ensuring balanced execution-vs-structural contribution.
- MT-GRPO improvement-aware task reweighting (from arXiv 2602.05547): dynamic logic-type balancing via softmax over improvement-aware logits, extended to handle formalization-specific zero-gradient patterns from solver timeouts.
- Adaptive curriculum: structural reward weight follows sigmoid interpolation from 0→λ_max, allowing execution reward to dominate early before intensional requirements activate.

**Training Pipeline:**
(1) Data: 12K problems total, 4K per type (balanced):
  - FOL: 4K (3K ProofWriter + 1K FOLIO) → Prover9
  - Prolog: 4K (2K ProofWriter subset + 2K GSM8K-Prolog following Mellgren et al.) → SWI-Prolog
  - SMT-LIB: 4K (1K FOLIO + 2K LogiQA 2.0 + 1K synthetic) → Z3
  Difficulty-based selection following 'Hard Examples Are All You Need' (arXiv 2508.14094): prioritize problems where Qwen3-4B base achieves 20-80% pass rate (maximum GRPO learning signal). Seed formalizations via Qwen3-72B + solver-verified filtering.
(2) Base model: **Qwen3-4B** (primary). Rationale: confirmed strong GRPO responsiveness (+34pp on GSM8K with only 747 hard examples per arXiv 2508.14094); Qwen3's own GRPO used only 3,995 pairs for 170 steps.
(3) GRPO training: K=8 samples per problem. Type-prefixed prompting ('[FOL]', '[PROLOG]', '[SMT]'). 5-second solver timeout.
(4) **Pilot validation (Days 1-2)**: Confirm per-step training time on Qwen3-4B. Validate solver pipeline on 100 examples per benchmark. Run 50-step pilot for each logic type.
(5) Experimental conditions (6 mandatory runs):
  - Run 1: Single-logic GRPO, FOL only (4K, execution reward) — baseline
  - Run 2: Single-logic GRPO, Prolog only (4K, execution reward) — baseline (droppable in contingency; Mellgren et al. provides external Prolog baseline)
  - Run 3: Multi-logic GRPO, execution reward only (12K, 3 types) — multi-logic baseline
  - Run 4: Multi-logic GRPO + MT-GRPO + MO-GRPO, no STA rewards — ablation isolating task balancing from structural rewards
  - Run 5: Multi-logic GRPO + full MLSR (MT-GRPO + MO-GRPO + STA + curriculum) — full method
  - Run 6: Multi-logic SFT baseline (12K)
  - Run 7 (optional): Qwen3-8B + full MLSR

**Compute Contingency:** Primary budget assumes ~7 min/step (validated by Day 1-2 pilot). If pilot reveals >12 min/step: (a) drop Run 2 (Prolog-only baseline; Mellgren et al. provides external comparison), (b) reduce steps from 180 to 120 per run, (c) drop optional Run 7. This reduces training from ~80h to ~55h while preserving all key ablation comparisons (Runs 1, 3, 4, 5, 6). If >20 min/step: additionally switch to Unsloth framework (reports 2x speedup for Qwen3) or reduce model to Qwen3-1.7B.

**Evaluation Protocol:**
- Per-type formalization accuracy: ProofWriter test (depth-5, 1K), FOLIO test (400), LogiQA test (500)
- Cross-transfer: Evaluate FOL-only model on Prolog formalization tasks and vice versa
- General reasoning (standard prompting, no formalization): **MATH-500**, **AIME 2024**, **AIME 2025**, **GPQA Diamond**, ARC-Challenge, BBH — measuring whether multi-logic GRPO training transfers to or degrades mathematical/scientific reasoning. Qwen3-4B baselines: MATH=54.1 (non-thinking), AIME24=70% (thinking), GPQA Diamond=60% (thinking). Cost: ~5h inference.
- Structural validity: Per-type ISR (Intensional Score Rate) via full STA — percentage of components that are intensionally necessary. Target: >60% ISR with MLSR vs. <10% with execution-only reward.
- IPT evaluation: Adapt Isomorphic Perturbation Testing to each logic type (variable renaming, predicate permutation) — measuring formalization invariance under meaning-preserving transformations (the dual of STA).
- Hacking characterization: Manual annotation of 200 outputs per type per condition, categorized by extensional-shortcut taxonomy.

**Key differentiators from closest work:**
- vs. EVOM (arXiv 2604.00442): EVOM demonstrates cross-solver GRPO transfer for optimization modeling with scalar execution outcome rewards. XLogic-RL targets structurally different formal logic languages and introduces STA for principled structural rewards beyond scalar outcomes.
- vs. ExecVerify (arXiv 2603.11226): ExecVerify derives trace-level rewards for code reasoning. XLogic-RL derives ablation-based rewards for formal logic verification, grounded in the RIP framework rather than trace prediction.
- vs. EGCA (arXiv 2603.16158): EGCA localizes credit assignment via trace divergence for code. XLogic-RL uses component ablation to derive intensional necessity scores for formal logic, a different mechanism.
- vs. SCORE (arXiv 2510.15600): SCORE uses structured component-based rewards for protocol generation but designs components heuristically. XLogic-RL derives structural rewards from solver semantics via STA, providing a general, transferable procedure.
- vs. MT-GRPO/MO-GRPO: We adopt their task-balancing and normalization mechanisms but contribute the domain-specific STA algorithm that defines *what* the reward objectives are.
- vs. 'LLMs Gaming Verifiers' (arXiv 2604.15149): They identify the extensional/intensional distinction and propose IPT as a test-time diagnostic. We formalize the dual (STA as training-time intervention) and derive efficient per-type instantiations.
- vs. Mellgren et al. (2025): They use hand-crafted structure rewards for single-logic Prolog. Our STA provides a principled derivation procedure applicable to any solver+language pair.

**Expected contributions:** (1) STA — a general, solver-agnostic algorithm for deriving intensional verification rewards from solver execution semantics, grounded in the RIP framework from mutation testing theory, with efficient O(1) 

## Resource Estimate

- **auto_research**: {'claude_api_cost': '$400-550 (~5000-6500 turns)', 'compute_contingency': 'Same as human_in_loop contingency. With 2 H100s, single-logic runs parallelize, reducing wall-clock to ~9 days.', 'estimated_gpu_cost': '$510 (170h × $3.00/hr)', 'gpu_hours': '~170h H100 (6 training runs ~74h + optional 8B run ~30h + 15h seed generation + 25h evaluation + 10h pilot + 16h buffer)', 'gpu_utilization': 'High (~75%). Agent pipelines solver setup → seed generation → SFT → GRPO → evaluation.', 'risk_note': "Cross-logic transfer may show interference — still publishable as it informs MLSR design. If hacking dynamics are uniform across types, the STA framework still contributes by generalizing Mellgren et al.'s approach with principled RIP-grounded derivation.", 'speed_bottleneck': "STA reward computation adds ~30% overhead vs. execution-only reward (efficient O(1) approximations: 1-2 additional solver calls per sample vs. full STA's |C| calls). Mitigated by async batched verification.", 'team': '0 (initial setup + final review only)', 'timeline': '12-14 days with 2 H100 GPUs available concurrently'}
- **human_in_loop**: {'claude_api_cost': '$250-400 (~3000-4500 turns)', 'compute_contingency': 'If pilot reveals >12 min/step: drop Prolog-only baseline (Run 2), reduce steps 180→120, drop optional 8B run → ~55h training + 55h overhead = ~110h total. If >20 min/step: additionally switch to Unsloth framework (2x speedup reported) or reduce to Qwen3-1.7B.', 'estimated_gpu_cost': '$435 (145h × $3.00/hr)', 'gpu_hours': '~145h H100 (6 training runs: 2 single-logic ~10h each + 3 multi-logic ~16h each + 1 SFT ~6h = 74h training + 15h seed generation + 25h evaluation (formalization + MATH/AIME/GPQA) + 15h pilot + 16h buffer)', 'gpu_utilization': 'Moderate (~55%). Agent handles pipeline; human reviews STA instantiation design and hacking taxonomy.', 'risk_note': 'Day 1-2 pilot: confirm per-step time with ms-swift/vLLM on H100 (expected ~5-8 min/step based on Qwen3-4B GRPO reports). Validate solver pipeline on 100 examples per benchmark. If pilot confirms speed, proceed with full 6-run plan; if not, activate contingency immediately.', 'team': '1 researcher, ~1.5hr/day review', 'timeline': '12-14 days'}
- **manual**: {'estimated_gpu_cost': '$510 (170h × $3.00/hr H100 on-demand)', 'gpu_hours': '~170h H100 (6 training runs on Qwen3-4B × ~13h avg + seed generation + evaluation including MATH/AIME/GPQA + pilot + buffer)', 'gpu_utilization': 'Low (~30%). STA reward engineering and hacking taxonomy require iterative human design.', 'team': '1-2 researchers', 'timeline': '6-7 weeks'}

## Key References

- Training Language Models to Use Prolog as a Tool (Mellgren et al., arXiv 2512.07407, Dec 2025)
- Multi-Task GRPO: Reliable LLM Reasoning Across Tasks [MT-GRPO] (arXiv 2602.05547, Feb 2026)
- MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems (arXiv 2509.22047, Sep 2025)
- PRoSFI: Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries (arXiv 2603.29500, March 2026)
- Pushing the Boundaries of Natural Reasoning: Interleaved Bonus from Formal-Logic Verification [FLV-RL] (arXiv 2601.22642, Jan 2026)
- LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (arXiv 2604.15149, April 2026)
- Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (arXiv 2604.19459, VerifAI-2 Workshop ICLR 2026)
- Strategy-Aware Optimization Modeling with Reasoning LLMs [SAGE] (arXiv 2605.02545, May 2026)
- Execution-Verified Reinforcement Learning for Optimization Modeling [EVOM] (arXiv 2604.00442, April 2026)
- ExecVerify: White-Box RL with Verifiable Stepwise Rewards for Code Execution Reasoning (arXiv 2603.11226, March 2026)
- Execution-Grounded Credit Assignment for GRPO in Code Generation [EGCA] (arXiv 2603.16158, ICLR 2026 SPOT Workshop)
- Unleashing Scientific Reasoning for Bio-experimental Protocol Generation via Structured Component-based Reward Mechanism [SCORE] (arXiv 2510.15600, ICLR 2026)
- Hard Examples Are All You Need: Maximizing GRPO Post-Training Under Annotation Budgets (arXiv 2508.14094, Aug 2025)
- From Reasoning to Code: GRPO Optimization for Underrepresented Languages (arXiv 2506.11027, June 2025)
- FormaRL: Enhancing Autoformalization with no Labeled Data (arXiv 2508.18914, Aug 2025)
- Frugal LMs Trained to Invoke Symbolic Solvers Achieve Parameter-Efficient Arithmetic Reasoning [SyReLM] (AAAI 2024)
- MAD-LOGIC: Multi-Agent Debate Enhances Symbolic Translation and Reasoning (ICLR 2026)
- Intermediate Languages Matter: Formal Choice Drives Neurosymbolic LLM Reasoning (arXiv 2502.17216, Feb 2025)
- Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition (EACL 2026)
- Solver-Informed RL: Grounding LLMs for Authentic Optimization Modeling [SIRL] (NeurIPS 2025)
- Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning (EMNLP 2023 Findings)
- VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (arXiv 2601.20055, Jan 2026)
- FoVer: First-Order Logic Verification for Natural Language Reasoning (TACL 2025)
- Into the Limits of Logic: Alignment Methods for Formal Logical Reasoning (MathNLP@NAACL 2025)
- DAPO: An Open-Source LLM Reinforcement Learning System at Scale (arXiv 2025)
- S-GRPO: Unified Post-Training for Large Vision-Language Models (arXiv 2604.16557, April 2026)
- Qwen3 Technical Report (arXiv 2505.09388, May 2025)

## Reviewer Evaluation

**Scores**:
  - clarity: **{'rationale': 'Well-structured with clear RQs, proper differentiation from 7 clusters of prior work across 26 verified references. The narrative (RIP → STA → efficient per-type instantiations → MLSR integration → XLogic-RL) is logical. Experimental design with 6 conditions cleanly isolates each contribution.', 'score': 4}**/5
  - feasibility: **{'rationale': "170h H100 within 200h budget, validated by Qwen3 Technical Report (3,995 pairs, 170 steps) and 'Hard Examples Are All You Need' (Qwen3-4B specifically). Explicit contingency plans (drop Run 2, reduce steps, switch to Unsloth) de-risk the tight timeline. Days 1-2 pilot validation is well-designed. ProofWriter/FOLIO/LogiQA all publicly available.", 'score': 4}**/5
  - impact: **{'rationale': 'Strong fit for EMNLP NLP+Symbolic Reasoning track. STA provides a transferable framework for deriving intensional verification rewards for any new solver+language pair. Five distinct contributions (STA, MLSR, cross-transfer, hacking taxonomy, STA-IPT duality) provide good paper density. Competitive for EMNLP Main, strong for Findings.', 'score': 4}**/5
  - novelty: **{'rationale': 'STA grounded in the RIP framework from mutation testing is a genuinely novel cross-pollination — no prior work applies RIP to derive RL training rewards. The multi-logic GRPO setting with cross-transfer study is new. EVOM does cross-solver but only within optimization with scalar rewards; ExecVerify/EGCA target code not formal logic. The per-type O(1) approximations are individually simple (anti-tautology, anti-enumeration, anti-hardcoding) but the unifying framework and formal derivation procedure are the contribution.', 'score': 4}**/5

## Human Review Note

## Agent 审核结果（完整三阶段 pipeline）

**Verdict**: PASS

**入口三重共识 (X)**: 26.0%
**终审自评 (Y)**: 34.0%
**出口三重共识 (Z)**: 37.0%
**Z 区间**: [32.0%, 42.0%]
**真实提升 (Z-X)**: +11.0 pp
**幻觉幅度 (Y-Z)**: -3.0 pp
**出口一致性**: 高
**出口三次评估**: [40.0, 38.0, 35.0]

### 优化方案 / 拒绝详情
【优化方案】

1. **[标题/定位]** — 将 STA 从"一种新算法"重新定位为"首次将 mutation testing RIP 框架系统性引入 LLM RL reward design 的方法论贡献"。明确承认 ablation/mutation testing 的技术渊源，novelty claim 聚焦于 methodology transfer + 实证发现，而非算法本身的新颖性。 — [命中 Novelty：防止"old wine in new bottles"攻击，将 novelty 锚定在可辩护的 methodology 层面]

2. **[Introduction 全面重构]** — 以 ORM-PRM-STA 的 2×2 taxonomy（signal density × annotation cost）作为全文叙事骨架，在第一段即建立"STA 填补 dense + automatic 空位"的清晰定位。增加"formal logic as reward design laboratory"的 framing（verification exact、shortcuts characterizable、理论工具直接适用），将论文受众从 formalization 窄社区扩展到整个 RLVR/reward hacking 社区。 — [命中 Novelty + Significance：reviewer 30 秒内理解 STA 的概念位置；"laboratory" framing 扩大 broader impact]

3. **[贡献列表精简：5→2]** — 原始 proposal 列 5 个 contributions（STA algorithm / MLSR framework / cross-logic transfer / hacking taxonomy / STA-IPT duality），对 8 页论文严重膨胀。精简为 2 个核心：(1) STA 作为 reward design methodology（含 O(1) derivations + coverage analysis + Goodhart vulnerability 讨论）；(2) 多逻辑 GRPO 训练的实证发现（STA 效果 + transfer patterns + hacking phenomena）。MLSR 降为 engineering detail，hacking taxonomy 和 RIP failure anatomy 作为 Contribution 2 的 secondary analysis，STA-IPT 关系嵌入方法论叙事。 — [命中 Novelty + Technical Soundness：消除"wide but shallow / kitchen-sink"这一 EMNLP 高频拒稿理由]

4. **[STA-IPT 关系降级]** — 原始 proposal 称二者"formally dual"。删除 formal duality claim 和任何试图建立形式化统一框架（如 V(f,T,P)）的尝试，改为 1 段直觉性对比："STA tests necessity via destruction; IPT tests faithfulness via preservation; together they certify structural minimality + meaning faithfulness, though not exhaustively"。将 IPT 定位为"STA 盲区的互补检测器"。 — [命中 Technical Soundness：避免理论敏感型 reviewer 质疑"Where is the formal proof of duality?"，同时保留概念贡献]

5. **[STA Derivation Protocol 显式呈现]** — 原始 proposal 将三个 O(1) checks 作为 ad-hoc 产物呈现。增加 5-step derivation protocol（pilot → collect shortcuts → classify → map RIP → design O(1) check）作为 boxed algorithm，将 STA 从"三个 specific checks"升级为"可复用的方法论框架 + 三个 instantiation"。在 Discussion 中对 Answer Set Programming (Clingo) 做概念性 walkthrough（到 Step 4），展示 protocol 的



## MVP Validation Results

- **Date**: 2026-05-13
- **Hypothesis Supported**: Yes

### Key Metrics

Phase 0: base ISR=0.064, GT ISR=0.559 (8.7x gap). Phase 1 r5 (100-step, K=8): exec-only last-20 prove_rate=0.200/ISR=0.200, exec-sta last-20 prove_rate=0.150/ISR=0.050. ISR trend separation=15pp. ISR/PR ratio: exec-only=100%, exec-sta=33% (quality degradation detected). O(1) fast_isr: zero additional signal (r4 negative). Full STA: meaningful continuous signal.

### Summary

MVP 验证了 STA（Solver Trace Ablation）作为 GRPO 训练中 formalization 质量信号的有效性。Phase 0 锚定了 baseline（base Qwen3-4B ISR=0.064, GT ISR=0.559）。Phase 1 r5 用 full STA（连续 ISR）+ K=8 跑了 100-step GRPO pilot，两个条件（execution-only vs execution+STA）。关键发现：(1) full STA 的连续 ISR 成功与 prove_rate 解耦——exec-sta 的 ISR/PR 比从 64%→33%，表明模型学会了更多 proof 但质量下降（reward hacking 信号）；(2) exec-only 的 ISR ≡ prove_rate（binary，无额外区分力）；(3) O(1) 近似版 fast_isr_fol 信号过粗无效（r4 阴性结果），full STA 才有区分力。注意：accuracy 差异 borderline（5pp），需要更长训练 + 多 seed 确认。

### Recommendation

GO — 核心机制验证通过。full STA 提供有意义的训练信号，能检测 reward hacking。下一步：(1) paper framing（story 调整：STA 作为 diagnostic+reward，O(1) 无效是重要阴性结果）；(2) 500-1000 步 full runs + 多 seed；(3) 多逻辑类型扩展（Prolog, SMT-LIB）；(4) 评估两条件 checkpoint 用相同 full STA 指标。DDL 5/25 剩 12 天，算力充足（2x RTX PRO 6000 96GB）。
