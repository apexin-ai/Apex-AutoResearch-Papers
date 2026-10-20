# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-11 (UTC).** ## Original idea { "tit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/6e18159e-4361-484e-8c9a-27485b1e4ea3.jsonl`
- **Structured JSON:** [`31c5925c73145bc24e6a.json`](../../sessions/31/31c5925c73145bc24e6a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-12T00:12:39.254Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-12T00:12:39.254Z",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-11 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Formally-Verified Intermediate Constraint Consensus Across Reasoning Paths\",\n  \"core_problem\": \"Recent work (CRAFT, PoLR, Draft-and-Prune) demonstrates that intermediate reasoning step consensus or pruning across candidate solutions provides stronger signals than answer-level majority voting. However, existing methods either rely on statistical similarity that cannot distinguish popular-but-contradictory constraints (CRAFT's TF-IRF/Jaccard), or prune individual paths based on internal consistency without cross-validating constraints across solutions (Draft-and-Prune's per-path |S|=0/|S|>1 checks). Meanwhile, single-output formal verification systems (MATH-VF, SAFE, FoVer, PRoSFI, VERGE) verify constraints within one solution or output but do not cross-validate across multiple reasoning paths, and cross-query consistency checking (arXiv 2604.14525) verifies coherence across different questions but not across multiple traces for the same question. Furthermore, 'Consensus is Not Verification' (arXiv 2603.06612) demonstrates that consensus-based aggregation fails for truthfulness because LLM errors are strongly correlated — but crucially, aggregation improves performance when a verifier exists. Can formally verifying cross-solution intermediate constraints via SMT solving and computer algebra yield more reliable consensus with interpretable provenance, and how frequently does statistical consensus actually retain contradictory constraints in practice?\",\n  \"opportunity\": \"CRAFT (arXiv 2604.14121, April 2026) builds a Reasoning Knowledge Graph from consensus intermediate steps using TF-IRF and Jaccard similarity, achieving significant accuracy improvements. However, CRAFT's authors explicitly acknowledge two key limitations: (1) 'consensus ≠ correctness' — frequently appearing steps can amplify shared errors, and (2) 'reduced effectiveness on symbolic math' due to lexical overlap bias in Jaccard similarity. This concern is empirically grounded by 'Consensus is Not Verification' (arXiv 2603.06612, March 2026), which demonstrates that LLM errors are strongly correlated across samples and even across model families — correlation persists even with random string conditioning — causing polling-style aggregation to yield no consistent accuracy gains over single-sample baselines. Critically, however, the paper finds that 'aggregation improves performance when a verifier exists, but it cannot serve as a verifier substitute,' directly motivating SICA's approach of introducing formal verification into the consensus process.\\n\\nDraft-and-Prune (D&P, arXiv 2603.17233, March 2026) addresses autoformalization brittleness by generating multiple natural-language plans, conditioning program generation on them, pruning individually contradictory or ambiguous formalizations (paths where the solver returns |S|=0 or |S|>1), and aggregating surviving paths via answer-level majority voting. D&P achieves strong results on logical reasoning benchmarks (AR-LSAT 78.43%, ProofWriter 98.33% with GPT-4), but its pruning operates independently on each path — it cannot detect cross-path contradictions where two individually valid paths assert mutually inconsistent constraints. D&P's authors explicitly note a limitation: 'We aggregate predictions at the answer level and do not cluster or de-duplicate candidates by symbolic equivalence.'\\n\\nA parallel line of work verifies individual solutions or outputs formally — MATH-VF (arXiv 2505.20869) uses CAS+Z3 for step-level verification on single solutions; SAFE (ACL 2025) uses Lean4 for retrospective step-aware verification; PRoSFI (arXiv 2603.29500) trains process rewards over structured formal intermediaries verified by Lean/Z3/Prover9, operating on individual 7B-model solutions. VERGE (arXiv 2601.20055, Jan 2026) is a single-output verify-and-refine framework that decomposes an LLM output into atomic claims, autoformalizes them, verifies joint satisfiability via Z3, and uses Minimal Correction Subsets (MCS) to provide targeted feedback for iterative refinement. VERGE's 'multi-model consensus' refers to K=3 candidate formalizations of a single claim checked for semantic equivalence — not cross-path reasoning aggregation. FoVer (arXiv 2505.15960, ACL 2026 Findings) uses Z3 and Isabelle for step-level error annotation in individual solutions for PRM training, demonstrating cross-task generalization to BBH subtasks (temporal sequences, tracking shuffled objects, word sorting). In the adjacent cross-output verification space, 'Quantifying Cross-Query Contradictions' (arXiv 2604.14525, April 2026) uses Z3 (QF_UFLIA) and CaDiCaL for cross-query consistency checking with unsat-core localization and counterexample-guided repair — but addresses cross-query consistency (different questions sharing a case file), not cross-trace consistency (same question, multiple reasoning paths). The EACL 2026 dynamic solver routing framework (arXiv 2510.06774) selects solvers at the problem level. But none of these methods formally cross-validate intermediate constraints across multiple candidate solutions for the same problem.\\n\\nThe gap: no method formally cross-validates intermediate constraints across multiple candidate solutions to produce a consistency-aware consensus signal with interpretable provenance. Concretely, SICA differs from D&P by extracting constraints from ALL paths and finding a globally consistent MAX-SAT-optimal subset (cross-path aggregation), rather than independently pruning paths with internal contradictions (per-path filtering). SICA differs from VERGE by applying MAX-SAT across multiple reasoning paths for answer selection, whereas VERGE applies the dual MCS operation within a single output for refinement feedback. SICA differs from the cross-query contradictions framework by operating on multiple traces for the same question (cross-trace scope) using weighted partial MAX-SAT for consensus, rather than on different questions in a case file (cross-query scope) using unsat-core repair. A key empirical question — how frequently does statistical consensus actually retain contradictory constraints? — remains unanswered and is central to quantifying this opportunity.\\n\\nRecent work on autoformalization faithfulness further motivates SICA's extraction quality pipeline: 'Do LLMs Game Formalization?' (arXiv 2604.19459, VerifAI-2 Workshop, ICLR 2026) shows that high compilation rates should not be equated with faithful reasoning, finding that two-stage formalization pipelines reveal distinct unfaithfulness patterns (axiom fabrication, premise mistranslation) that evade standard verification. This underscores the need for SICA's multi-tier extraction validation.\",\n  \"landscape\": \"Standard self-consistency (Wang et al., ICLR 2023) performs majority voting on final answers and shows diminishing returns on frontier models — gains plateau at <2% with accuracy sometimes declining at high sample counts (arXiv 2511.00751). 'Consensus is Not Verification' (arXiv 2603.06612, March 2026) provides a theoretical explanation: LLM errors are strongly correlated across samples and model families, causing consensus to reinforce shared misconceptions rather than converge on truth; however, the paper finds aggregation succeeds when an external verifier exists. CRAFT (arXiv 2604.14121, April 2026) extracts consensus intermediate steps via a Reasoning Knowledge Graph using TF-IRF/Jaccard similarity and topological generation, achieving up to +8.5% accuracy over SC baselines on GSM8K, FOLIO, FLD, and OlympiadBench with K=3 traces; its authors note 'consensus ≠ correctness' and 'reduced effectiveness on symbolic math' as limitations. PoLR (ICLR 2026) uses prefix consensus to prune reasoning paths, matching SC accuracy while reducing token usage by 50-60%.\\n\\nDraft-and-Prune (D&P, arXiv 2603.17233, March 2026): An inference-time framework that drafts multiple natural-language plans, conditions program generation on them, prunes executable but contradictory (|S|=0) or ambiguous (|S|>1) formalizations independently for each path, and aggregates surviving paths via answer-level majority voting. Uses Z3Py for AR-LSAT/LogicalDeduction and PyKe for ProofWriter/PrOntoQA. Achieves AR-LSAT 78.43%, ProofWriter 98.33%, PrOntoQA 99.32%, LogicalDeduction 99.50% (GPT-4). Key limitation: no cross-path constraint checking or equivalence-aware deduplication.\\n\\nVERGE (arXiv 2601.20055, Jan 2026): A single-output neurosymbolic verify-and-refine loop. Decomposes an LLM output into atomic claims, classifies them by type, autoformalizes into FOL, and verifies joint satisfiability via Z3. Uses semantic routing (symbolic solvers for logical claims, LLM ensembles for commonsense) and Minimal Correction Subsets (MCS) for precise error localization, providing actionable feedback for iterative refinement. VERGE's K=3 refers to candidate formalizations of a single claim checked for semantic equivalence, not multiple reasoning paths. MCS (minimum claims to remove for satisfiability) is dual to MAX-SAT (maximum satisfiable subset) but is applied within one output for feedback, not across paths for consensus. Evaluated on FOLIO (84.7-89.2%), ProofWriter (85.2-93.0%), AR-LSAT (88.6-91.7%) across GPT-OSS-20B, GPT-OSS-120B, and Claude 3.7 Sonnet.\\n\\nSingle-solution formal verification: MATH-VF (arXiv 2505.20869, May 2025) uses a Formalizer+Critic pipeline with CAS and Z3 SMT solver for step-level verification on individual solutions, evaluated on MATH-500 and ProcessBench. SAFE (ACL 2025, arXiv 2506.04592) uses Lean4 for retrospective step-aware formal verification of individual reasoning chains, introducing the FormalStep benchmark (30,809 formal statements). PRoSFI (arXiv 2603.29500, March 2026) — 'Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries' — trains process rewards over structured formal intermediaries verified by Lean tactics, Z3, and Prover9, operating on individual 7B-model solutions; achieves 92.97% accuracy / 76.07% GPT Soundness on ProverQA-Hard. FoVer (arXiv 2505.15960, ACL 2026 Findings) — 'Training Step-Level Reasoning Verifiers with Formal Verification Tools' — uses Z3 and Isabelle for step-level error annotation in individual solutions for PRM training; demonstrates cross-task generalization to BBH subtasks (temporal sequences 97.2%, tracking shuffled objects 96.0%, word sorting 46.8% with Llama3.1-8B-PRM at Best-of-7) and to MATH, AIME, ANLI, MMLU-Pro.\\n\\nCross-output consistency verification: 'Quantifying Cross-Query Contradictions in Multi-Query LLM Reasoning' (arXiv 2604.14525, April 2026) addresses cross-query consistency — maintaining a globally satisfiable belief state across interdependent queries sharing a case file. Uses Z3 v4.8.17 (QF_UFLIA theory) and CaDiCaL for SAT, with unsat-core localization and counterexample-guided lexicographic repair. Achieves SetCons improvement from 0.56 to 0.94 across 390 case files spanning relational/SAT, temporal/SMT, policy/rules, and abductive domains. Crucially, this operates at cross-query scope (different questions sharing context) rather than cross-trace scope (same question, multiple reasoning paths), and uses unsat-core repair rather than weighted partial MAX-SAT consensus. SICA's differentiators are: cross-trace scope, intermediate constraint extraction from reasoning steps, and popularity-weighted MAX-SAT for answer selection.\\n\\nSolver routing: The EACL 2026 dynamic solver composition framework (arXiv 2510.06774) automatically identifies formal reasoning strategies and routes to specialized solvers at the problem level, achieving 27% improvement over GPT-4o. SICA's theory-aware routing operates at the finer-grained assertion level.\\n\\nVeriCoT (Nov 2025) formalizes individual CoT traces into FOL for entailment checking without cross-solution comparison. FregeLogic (SemEval 2026) uses Z3 as a tiebreaker for syllogistic validity.\\n\\nAutoformalization reliability: Grammars of Formal Uncertainty (NeurIPS 2025) demonstrates that SMT autoformalization is task-dependent: +34.8% on ProofWriter but -44.5% on FOLIO, necessitating careful benchmark selection and per-domain extraction analysis. 'Do LLMs Game Formalization?' (arXiv 2604.19459, VerifAI-2 Workshop, ICLR 2026) evaluates faithfulness of LLM autoformalization on 303 FOL problems, finding that high compilation rates (87-99%) do not guarantee faithful reasoning — two-stage pipelines reveal distinct unfaithfulness patterns: axiom fabrication (GPT-5) and premise mistranslation (DeepSeek-R1). Autoformalization surveys (arXiv 2505.23486) report ~70% success rate on physics kinematics, with selective verification reducing errors by 14-100% with minimal abstention.\\n\\nNo concurrent work (searched arXiv and OpenReview through May 2026) formally cross-validates intermediate constraints across multiple candidate solutions for the same problem.\",\n  \"approach\": \"We propose Symbolic Invariant Consensus Aggregation (SICA): given a problem, sample K reasoning paths from a frontier open-source reasoning model (QwQ-32B via vLLM on 1-2 A100s; Qwen3-32B as secondary model for ablation), then use a prompted LLM extractor to parse each trace into typed symbolic assertions (equations, inequalities, logical predicates). SICA introduces four key technical components:\\n\\n(1) **Theory-aware assertion-level solver routing**: Extracted assertions are classified by constraint type and routed to appropriate solvers — Z3 for tractable theories (linear arithmetic, propositional logic, uninterpreted functions, bitvectors) and SymPy for nonlinear polynomial arithmetic, algebraic equivalence, and modular arithmetic. Unlike the EACL 2026 framework (arXiv 2510.06774) which routes at the problem level, SICA routes at the assertion level, enabling mixed-theory problems where individual steps span different solver domains (common in competition math). Assertions that neither solver can handle receive numerical spot-checking as fallback, with unverifiable assertions flagged and excluded from the consensus set (rather than silently included).\\n\\n(2) **Weighted partial MAX-SAT for invariant consensus**: Rather than enumerating assertion subsets (exponential worst-case), SICA leverages Z3's built-in optimization context to solve weighted partial MAX-SAT directly. Each unique assertion (deduplicated via solver-verified equivalence) is weighted by its cross-solution frequency. The optimizer finds the largest jointly satisfiable subset of assertions, weighted by popularity — a single Z3 optimization call replaces exponential subset enumeration. Per-query timeout caps (10s) bound worst-case latency. This cross-path MAX-SAT consensus is the key differentiator from Draft-and-Prune (D&P), which prunes paths independently based on internal consistency (|S|=0 or |S|>1) and aggregates surviving answers via majority voting without cross-path constraint checking. It is also distinct from VERGE's MCS, which is the dual operation (minimum claims to remove) applied within a single output for refinement feedback rather than across paths for answer selection. It further differs from the cross-query contradictions framework (arXiv 2604.14525), which uses unsat-core localization and counterexample-guided repair across different questions sharing a case file — SICA uses weighted partial MAX-SAT across different reasoning traces for the same question.\\n\\n(3) **Invariant-backed answer scoring**: Each candidate answer is scored by the coverage and weight of its supporting assertions within the MAX-SAT-optimal consistent set, yielding a continuous invariant consensus score. This captures partial structural agreement even when final answers diverge, and provides interpretable provenance (each score is backed by a specific set of formally verified constraints).\\n\\n(4) **Extraction quality assurance pipeline**: To address the documented task-dependence of autoformalization (Grammars of Formal Uncertainty, NeurIPS 2025) and the unfaithfulness risks identified by 'Do LLMs Game Formalization?' (arXiv 2604.19459), we implement a three-tier extraction quality pipeline: (a) syntactic validation — each extracted assertion must parse in the target solver's input language; (b) semantic spot-checking — a random 20% of assertions are checked against the original natural language step via an LLM judge for semantic fidelity, specifically targeting the axiom fabrication and premise mistranslation failure modes identified in the faithfulness literature; (c) coverage tracking — we report 'verifiable assertion coverage' (% of extracted assertions that successfully enter the MAX-SAT pipeline) per benchmark as a first-class metric. Extraction failures cascade to numerical fallback or abstention, preventing malformed inputs from corrupting the consensus signal.\\n\\n**Limitations of formal cross-validation**: SICA's MAX-SAT consensus catches contradictory constraints but cannot detect universally-wrong-but-mutually-consistent constraints caused by correlated extraction errors. 'Consensus is Not Verification' (arXiv 2603.06612) demonstrates that LLM errors are strongly correlated across samples and even across model families, which implies that if all K paths produce the same wrong formalization of a constraint, MAX-SAT will see K consistent-but-wrong assertions and cannot flag the error. This is a fundamental limitation of any approach combining LLM extraction with formal verification: the verifier guarantees consistency, not correctness of the extraction. SICA's semantic spot-checking tier partially mitigates this — by sampling 20% of assertions for LLM-judge semantic fidelity checks, it can catch systematic mistranslation patterns. However, if the extraction LLM and the judge LLM share the same correlated bias (as the correlated errors literature suggests is likely), the mitigation is incomplete. We acknowledge this limitation explicitly and note two potential future mitigations: (a) using structurally diverse extractor models (e.g., symbolic parsers alongside LLM extractors) to decorrelate extraction errors, and (b) grounding extracted constraints against external knowledge sources (CAS simplification, unit-test-style numerical spot-checking) that do not share LLM inductive biases. We include FOLIO as a diagnostic ablation where SMT autoformalization is documented to hurt (-44.5%), precisely to empirically characterize the boundary between domains where SICA's extraction is faithful enough to help versus where correlated errors dominate.\\n\\n**Dual-track evaluation plan**:\\n\\n*Track A — EMNLP 2026 (ARR May 25, primary target, 14 days):* Scoped evaluation with K=12 traces on 5 core benchmarks plus 3 BBH subtasks:\\n- **MATH-500** (algebraic/arithmetic reasoning; QwQ-32B ~90.6%)\\n- **AIME 2024** (competition math with mixed-theory constraints; QwQ-32B ~79.5%)\\n- **ProofWriter** (formal logic; enables direct comparison with D&P 98.33% and VERGE 85.2-93.0%)\\n- **FOLIO** (first-order logic; diagnostic ablation — SMT autoformalization documented to hurt -44.5% here)\\n- **BBH** (3 subtasks: logical deduction, tracking shuffled objects, temporal sequences — enables direct comparison with FoVer's BBH evaluation at Best-of-7; tests cross-domain generalization to structured informal reasoning)\\n\\nBaselines for Track A: self-consistency, CRAFT, D&P (on ProofWriter), VERGE (on ProofWriter/FOLIO).\\n\\n*Track B — AAAI 2027 (paper deadline ~August 1, extended version):* Expanded to K=16 traces on all Track A benchmarks plus:\\n- **AIME 2025** (tests generalization to unseen competition problems; available via MathArena/aime_2025 on HuggingFace)\\n- **GPQA Diamond** (graduate-level science; QwQ-32B ~65.2%; per-domain reporting for physics/chemistry vs. biology)\\n- **LogiQA 2.0** (natural language logical reasoning; 8,678 questions; tests constraint extraction beyond math/formal logic)\\n- Additional BBH subtasks and full ablation suite\\n\\n**ARC-Challenge exclusion justification**: ARC-Challenge (Clark et al., 2018) consists of multiple-choice grade-school science questions that primarily test factual knowledge retrieval (e.g., 'Which mineral is the hardest?', 'What happens when water freezes?'). Most questions lack the multi-step constraint structure required for meaningful symbolic assertion extraction — they involve domain knowledge rather than chains of extractable equations, inequalities, or logical predicates. Including ARC-Challenge would likely yield near-zero verifiable assertion coverage, providing no insight beyond confirming SICA's domain specificity (which FOLIO already demonstrates as a negative diagnostic). We note this scope limitation explicitly.\\n\\n**Metrics and analyses**:\\n- Primary: accuracy, calibration (ECE), informativeness of partial invariant agreement when candidates disagree\\n- **Contradiction frequency analysis** (centerpiece experiment): For each problem across all benchmarks, we measure how often CRAFT's statistical consensus retains logically contradictory constraint pairs. We report the 'contradiction rate' — the fraction of problems where at least one pair of popular constraints (appearing in ≥3 of K traces) are mutually unsatisfiable. If >15%, this validates SICA's core motivation; if <5%, we honestly acknowledge limited practical impact on this axis and emphasize interpretability/provenance instead.\\n- **D&P comparison**: On ProofWriter (shared benchmark), we compare SICA's cross-path MAX-SAT consensus against D&P's per-path pruning + answer-level voting, specifically measuring: (a) how many problems have cross-path contradictions that D&P's per-path pruning misses, and (b) whether MAX-SAT-backed scoring outperforms answer-level majority voting among surviving paths.\\n- **FoVer comparison on BBH**: On the 3 shared BBH subtasks, we compare SICA's inference-time cross-path consensus against FoVer's training-time PRM approach (Llama3.1-8B-PRM at Best-of-7: temporal 97.2%, tracking 96.0%, word sorting 46.8%), analyzing whether cross-path formal consensus provides complementary signal to trained process reward models.\\n- **Extraction accuracy ablation**: Per-benchmark measurement of (a) syntactic parse rate, (b) semantic fidelity (manual annotation on 100 samples per benchmark), and (c) error propagation analysis — how X% extraction error degrades MAX-SAT consensus quality via controlled noise injection. Per the findings of 'Do LLMs Game Formalization?', we specifically track axiom fabrication and premise mistranslation rates.\\n- **Correlated extraction error analysis**: On a subset of problems (100 per benchmark), we measure cross-path extraction agreement — the fraction of assertions that are semantically equivalent across all K traces — to empirically quantify the degree of correlated extraction and assess how much independent signal SICA's MAX-SAT actually receives.\\n- **Compute-normalized comparison**: Report total tokens generated, wall-clock time per problem, and decomposed latency (inference, extraction, solver, MAX-SAT) for each method. Plot accuracy vs. total compute (tokens) curves. If SICA takes 5x compute of vanilla SC for +2% accuracy, we justify via interpretability/soundness or acknowledge the tradeoff.\\n\\nThe primary contribution is not raw accuracy improvement over SC (which has diminishing returns on frontier models) but rather: (a) formal soundness guarantees on the consensus signal, (b) interpretable constraint-level provenance for each answer, (c) detecting logically inconsistent popular reasoning steps that both statistical consensus (CRAFT) and per-path pruning (D&P) miss — with empirical quantification of how frequently this occurs, (d) systematic domain analysis of formal cross-solution verification including where it helps (ProofWriter, BBH logical deduction) vs. hurts (FOLIO), and (e) empirical characterization of correlated extraction errors as a fundamental limitation of LLM-based autoformalization in consensus settings.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~180-240h A100 80GB (5 benchmarks + 3 BBH subtasks × K=12 traces + extraction + ablations)\",\n      \"gpu_utilization\": \"Low (~20-30%); GPUs idle during coding, debugging solver routing, manual extraction annotation\",\n      \"timeline\": \"2-3 months\",\n      \"team\": \"1-2 researchers with formal methods and LLM experience\",\n      \"estimated_gpu_cost\": \"$235-310 (at ~$1.30/hr typical A100 spot rate)\",\n      \"h100_equivalent\": \"~90-120h H100 (well within 200h H100 budget)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~220-300h A100 80GB\",\n      \"gpu_utilization\": \"Moderate (~50-60%); agent codes and runs experiments between human review gates\",\n      \"timeline\": \"4-6 weeks (fits AAAI 2027 extended version with writing buffer)\",\n      \"team\": \"1 researcher, ~40-50min/day reviewing extraction quality, solver routing correctness, contradiction analysis, D&P comparison design, and BBH extraction quality; ~6h total for manual semantic fidelity annotation (100 samples × 5 benchmarks + 3 BBH subtasks)\",\n      \"claude_api_cost\": \"$200-400 (est. 2000-4000 Opus turns)\",\n      \"estimated_gpu_cost\": \"$285-390\",\n      \"h100_equivalent\": \"~110-150h H100 (within 200h H100 budget)\",\n      \"risk_note\": \"Solver routing heuristics require human judgment for edge cases; CRAFT replication may need prompt tuning; BBH logical deduction extraction quality needs validation\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~300-400h A100 80GB (Track A: 5 benchmarks + 3 BBH subtasks × K=12 × core ablations)\",\n      \"gpu_utilization\": \"High (~85-95%); agent pipelines inference, extraction, and solving continuously; batched vLLM serving keeps GPUs saturated\",\n      \"timeline\": \"10-14 days with 2-4 A100s available (fits EMNLP 2026 ARR May 25 deadline)\",\n      \"team\": \"0 (initial setup only, ~3 hours)\",\n      \"claude_api_cost\": \"$350-600 (est. 3500-6000 Opus turns)\",\n      \"estimated_gpu_cost\": \"$390-520\",\n      \"h100_equivalent\": \"~150-200h H100 (within 200h H100 budget with K=12 and 5+3 benchmarks)\",\n      \"speed_bottleneck\": \"GPU count for parallel vLLM inference across benchmarks × 12 samples; secondary bottleneck is Z3 MAX-SAT optimization time (mitigated by 10s per-query timeout)\",\n      \"risk_note\": \"Automated extraction may produce malformed solver input in ~10-20% of traces; without human review the agent may over-tune extraction prompts to specific benchmarks; contradiction frequency analysis needs careful statistical framing to avoid over-claiming; 14-day timeline is tight but feasible in full auto mode with scoped benchmark set\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline: May 25, 2026 — 14 days from now; primary target with Track A scoped evaluation)\",\n    \"AAAI 2027 (abstract deadline: ~July 25, 2026; paper deadline: ~August 1, 2026 — extended version with Track B full evaluation)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Self-Consistency Improves Chain of Thought Reasoning in Language Models (ICLR 2023)\",\n    \"CRAFT: Correct Prediction, Wrong Steps? Consensus Reasoning Knowledge Graph for Robust Chain-of-Thought Synthesis (arXiv 2604.14121, April 2026)\",\n    \"Draft-and-Prune: Improving the Reliability of Auto-formalization for Logical Reasoning (arXiv 2603.17233, March 2026)\",\n    \"PoLR: The Path of Least Resistance — Guiding LLM Reasoning Trajectories with Prefix Consensus (ICLR 2026)\",\n    \"VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (arXiv 2601.20055, Jan 2026)\",\n    \"VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks (arXiv 2025)\",\n    \"MATH-VF: Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving (arXiv 2505.20869, May 2025)\",\n    \"SAFE: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification (ACL 2025, arXiv 2506.04592)\",\n    \"Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition (EACL 2026, arXiv 2510.06774)\",\n    \"PRoSFI: Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries (arXiv 2603.29500, March 2026)\",\n    \"FoVer: Training Step-Level Reasoning Verifiers with Formal Verification Tools (arXiv 2505.15960, ACL 2026 Findings)\",\n    \"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks (NeurIPS 2025)\",\n    \"FregeLogic at SemEval 2026 Task 11: Hybrid Neuro-Symbolic Architecture for Syllogistic Validity (SemEval 2026)\",\n    \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (arXiv 2604.19459, VerifAI-2 Workshop, ICLR 2026)\",\n    \"Reevaluating Self-Consistency Scaling in Multi-Agent Systems (arXiv 2511.00751)\",\n    \"Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling (NAACL 2025)\",\n    \"Faithful Logical Reasoning via Symbolic Chain-of-Thought (ACL 2024)\",\n    \"Autoformalization in the Era of Large Language Models: A Survey (arXiv 2505.23486, May 2025)\",\n    \"Consensus is Not Verification: Why Crowd Wisdom Strategies Fail for LLM Truthfulness (arXiv 2603.06612, March 2026)\",\n    \"Quantifying Cross-Query Contradictions in Multi-Query LLM Reasoning (arXiv 2604.14525, April 2026)\"\n  ],\n  \"description\": \"We propose Symbolic Invariant Consensus Aggregation (SICA), a method that formally cross-validates intermediate constraints extracted from multiple LLM reasoning paths to produce a soundness-guaranteed consensus signal. While CRAFT (April 2026) demonstrates the value of intermediate-step consensus via statistical similarity (TF-IRF/Jaccard), its authors explicitly acknowledge 'consensus ≠ correctness' and 'reduced effectiveness on symbolic math.' This limitation is theoretically grounded by 'Consensus is Not Verification' (arXiv 2603.06612, March 2026), which proves that LLM errors are strongly correlated across samples and model families, causing pure consensus to fail — but critically finds that 'aggregation improves performance when a verifier exists,' directly motivating SICA's approach. Draft-and-Prune (D&P, March 2026) improves autoformalization reliability by independently pruning paths with internal contradictions and aggregating survivors via majority voting, but does not perform cross-path constraint checking — its authors note they 'aggregate predictions at the answer level and do not cluster or de-duplicate candidates by symbolic equivalence.' Meanwhile, VERGE (Jan 2026) verifies and refines a single LLM output by decomposing it into atomic claims, checking joint satisfiability via Z3, and using Minimal Correction Subsets (MCS) to provide targeted refinement feedback — but operates on one output, not across reasoning paths. In the adjacent cross-output verification space, 'Quantifying Cross-Query Contradictions' (arXiv 2604.14525, April 2026) uses Z3 (QF_UFLIA) and CaDiCaL for cross-query consistency checking with unsat-core repair, but addresses cross-query consistency (different questions sharing a case file) rather than cross-trace consistency (same question, multiple paths). Single-solution formal verification (MATH-VF uses CAS+Z3; SAFE uses Lean4; PRoSFI uses Lean/Z3/Prover9 for structured formal intermediaries on 7B models; FoVer (arXiv 2505.15960) uses Z3+Isabelle for PRM training data with cross-task generalization to BBH) improves reliability but none cross-validate across solutions.\\n\\nSICA fills this gap by extracting typed symbolic assertions from K sampled reasoning traces, routing them to appropriate solvers via assertion-level theory-aware dispatch (Z3 for linear arithmetic and propositional logic; SymPy for nonlinear polynomial and algebraic constraints — finer-grained than the EACL 2026 problem-level solver routing), and using Z3's built-in weighted partial MAX-SAT optimization to find the largest jointly satisfiable assertion set weighted by cross-solution frequency. SICA's MAX-SAT consensus across paths is the cross-path counterpart to VERGE's within-output MCS (dual operations: MAX-SAT keeps the maximum consistent subset; MCS removes the minimum inconsistent subset), and differs from cross-query contradiction checking by operating on multiple traces for the same question via weighted consensus rather than unsat-core repair across different questions. A three-tier extraction quality pipeline (syntactic validation, semantic spot-checking targeting the unfaithfulness patterns identified by 'Do LLMs Game Formalization?' (arXiv 2604.19459), and coverage tracking) addresses the documented task-dependence of autoformalization.\\n\\nWe explicitly acknowledge a fundamental limitation: SICA's MAX-SAT consensus catches contradictory constraints but cannot detect universally-wrong-but-consistent constraints caused by correlated extraction errors — the same correlated error phenomenon documented by 'Consensus is Not Verification.' The semantic spot-checking tier partially mitigates this, but correlated biases between the extractor and judge LLMs limit its effectiveness. We include FOLIO as a diagnostic ablation and propose a correlated extraction error analysis to empirically characterize this boundary.\\n\\nWe adopt a dual-track evaluation plan. Track A (EMNLP 2026, ARR May 25): scoped evaluation with K=12 on MATH-500, AIME 2024, ProofWriter, FOLIO, and 3 BBH subtasks (logical deduction, tracking shuffled objects, temporal sequences) using QwQ-32B via vLLM, comparing against SC, CRAFT, D&P, VERGE, and FoVer. BBH subtasks enable direct comparison with FoVer (ACL 2026) which reports Best-of-7 results on the same tasks (temporal 97.2%, tracking 96.0%, word sorting 46.8%). Track B (AAAI 2027): expanded to K=16 with AIME 2025, GPQA Diamond, and LogiQA 2.0 added. ARC-Challenge is excluded because its multiple-choice science knowledge questions lack the multi-step constraint structure needed for meaningful symbolic extraction (most test factual recall rather than chains of extractable logical predicates). The centerpiece experiment is a contradiction frequency analysis measuring how often statistical consensus retains logically contradictory constraint pairs. FOLIO serves as a diagnostic ablation where SMT is documented to hurt (-44.5%). Primary contributions: formal soundness guarantees, interpretable constraint-level provenance, empirically-quantified detection of contradictory consensus that both statistical methods and per-path pruning miss, systematic domain analysis of formal cross-solution verification, and honest characterization of the correlated extraction error limitation. Auto-mode compute fits within 200h H100 budget at K=12 with 5+3 benchmarks.\",\n  \"project_name\": \"symb_invariant_consensus\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 6)\nIssues: [\"FEASIBILITY — No day-by-day timeline for the 13-day sprint to ARR May 25. The proposal says '10-14 days' in auto mode but does not allocate time for: (1) pipeline implementation and debugging, (2) extraction prompt development per domain, (3) running experiments across 8 benchmark configs, (4) analysis and figure generation, (5) paper writing and formatting. A credible timeline would show these phases don't overlap impossibly. Paper writing alone typically takes 3-5 days for a polished submission.\", \"FEASIBILITY — No minimum viable scope fallback. If extraction quality proves unreliable on 1-2 benchmarks (plausible given documented task-dependence of autoformalization), what is the minimum credible submission? E.g., could Track A be scoped to 3 benchmarks (MATH-500, ProofWriter, AIME 2024) at K=8 with a shortened paper? Without a fallback plan, the proposal is all-or-nothing on a 13-day deadline.\", \"USER REQUIREMENT — AIME 2025 excluded from Track A despite user explicitly listing it. Since AIME 2025 uses the identical evaluation pipeline as AIME 2024 (same problem format, same constraint extraction approach), adding it to Track A is trivially low-cost (one additional benchmark run) and directly satisfies a user requirement. No justification is given for deferring it to Track B.\", \"MINOR — 'Correct Reasoning Paths Visit Shared Decision Pivots' (ROMA, arXiv 2509.21549, ICLR 2026 under review) extracts shared intermediate checkpoints ('decision pivots') across multiple reasoning paths and uses a learned verifier to identify correct reasoning. While ROMA uses neural verification rather than formal solvers, it occupies the adjacent conceptual space of cross-path intermediate-step analysis and could be cited in the landscape section to strengthen the positioning: SICA provides formal guarantees where ROMA uses learned signals.\"]\nFeedback: The proposal is close to passing — all prior substantive issues are resolved, references are verified, the gap is genuine, and the intellectual honesty (FOLIO diagnostic, correlated error limitations) is commendable. Three targeted fixes to cross the threshold:\n\n1. **Add a realistic day-by-day timeline for Track A**: Break the 13-day sprint into phases: Days 1-3 (pipeline implementation: extraction prompts, solver routing, MAX-SAT wrapper), Days 4-7 (experiments: 8 benchmark configs × K=12), Days 8-10 (analysis: contradiction frequency, ablations, figures), Days 11-13 (paper writing and formatting). If paper writing cannot fit, acknowledge this honestly and consider submitting to the June ARR cycle instead (which would still allow EMNLP 2026 commitment via prior-cycle papers, though this depends on ARR policy — verify).\n\n2. **Define a minimum viable scope**: If the full 5+3 benchmark plan proves too ambitious, what is the minimum credible submission? Suggest: 3 core benchmarks (MATH-500, ProofWriter, AIME 2024) at K=12, plus FOLIO as negative diagnostic = 4 benchmarks total. This would still demonstrate the core contribution (cross-path MAX-SAT consensus, contradiction frequency analysis, domain analysis including negative results) while leaving headroom for implementation and writing.\n\n3. **Move AIME 2025 to Track A**: It uses the identical pipeline as AIME 2024 and is essentially free to add. This satisfies the user's explicit requirement and provides a generalization test (unseen competition problems).\n\nMinor: cite ROMA (arXiv 2509.21549) as a neural counterpart to SICA's formal cross-path analysis in the landscape section.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 6 轮修订，近 3 轮的平均分从 3.5 到 3.6，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-12T00:12:39.261Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-12T00:12:39.261Z",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3"
}
```

---

## Round 1

51 recorded events

### User

_source line 3 · 2026-05-12T00:12:39.296Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-11 (UTC).**

## Original idea
{
  "title": "Formally-Verified Intermediate Constraint Consensus Across Reasoning Paths",
  "core_problem": "Recent work (CRAFT, PoLR, Draft-and-Prune) demonstrates that intermediate reasoning step consensus or pruning across candidate solutions provides stronger signals than answer-level majority voting. However, existing methods either rely on statistical similarity that cannot distinguish popular-but-contradictory constraints (CRAFT's TF-IRF/Jaccard), or prune individual paths based on internal consistency without cross-validating constraints across solutions (Draft-and-Prune's per-path |S|=0/|S|>1 checks). Meanwhile, single-output formal verification systems (MATH-VF, SAFE, FoVer, PRoSFI, VERGE) verify constraints within one solution or output but do not cross-validate across multiple reasoning paths, and cross-query consistency checking (arXiv 2604.14525) verifies coherence across different questions but not across multiple traces for the same question. Furthermore, 'Consensus is Not Verification' (arXiv 2603.06612) demonstrates that consensus-based aggregation fails for truthfulness because LLM errors are strongly correlated — but crucially, aggregation improves performance when a verifier exists. Can formally verifying cross-solution intermediate constraints via SMT solving and computer algebra yield more reliable consensus with interpretable provenance, and how frequently does statistical consensus actually retain contradictory constraints in practice?",
  "opportunity": "CRAFT (arXiv 2604.14121, April 2026) builds a Reasoning Knowledge Graph from consensus intermediate steps using TF-IRF and Jaccard similarity, achieving significant accuracy improvements. However, CRAFT's authors explicitly acknowledge two key limitations: (1) 'consensus ≠ correctness' — frequently appearing steps can amplify shared errors, and (2) 'reduced effectiveness on symbolic math' due to lexical overlap bias in Jaccard similarity. This concern is empirically grounded by 'Consensus is Not Verification' (arXiv 2603.06612, March 2026), which demonstrates that LLM errors are strongly correlated across samples and even across model families — correlation persists even with random string conditioning — causing polling-style aggregation to yield no consistent accuracy gains over single-sample baselines. Critically, however, the paper finds that 'aggregation improves performance when a verifier exists, but it cannot serve as a verifier substitute,' directly motivating SICA's approach of introducing formal verification into the consensus process.\n\nDraft-and-Prune (D&P, arXiv 2603.17233, March 2026) addresses autoformalization brittleness by generating multiple natural-language plans, conditioning program generation on them, pruning individually contradictory or ambiguous formalizations (paths where the solver returns |S|=0 or |S|>1), and aggregating surviving paths via answer-level majority voting. D&P achieves strong results on logical reasoning benchmarks (AR-LSAT 78.43%, ProofWriter 98.33% with GPT-4), but its pruning operates independently on each path — it cannot detect cross-path contradictions where two individually valid paths assert mutually inconsistent constraints. D&P's authors explicitly note a limitation: 'We aggregate predictions at the answer level and do not cluster or de-duplicate candidates by symbolic equivalence.'\n\nA parallel line of work verifies individual solutions or outputs formally — MATH-VF (arXiv 2505.20869) uses CAS+Z3 for step-level verification on single solutions; SAFE (ACL 2025) uses Lean4 for retrospective step-aware verification; PRoSFI (arXiv 2603.29500) trains process rewards over structured formal intermediaries verified by Lean/Z3/Prover9, operating on individual 7B-model solutions. VERGE (arXiv 2601.20055, Jan 2026) is a single-output verify-and-refine framework that decomposes an LLM output into atomic claims, autoformalizes them, verifies joint satisfiability via Z3, and uses Minimal Correction Subsets (MCS) to provide targeted feedback for iterative refinement. VERGE's 'multi-model consensus' refers to K=3 candidate formalizations of a single claim checked for semantic equivalence — not cross-path reasoning aggregation. FoVer (arXiv 2505.15960, ACL 2026 Findings) uses Z3 and Isabelle for step-level error annotation in individual solutions for PRM training, demonstrating cross-task generalization to BBH subtasks (temporal sequences, tracking shuffled objects, word sorting). In the adjacent cross-output verification space, 'Quantifying Cross-Query Contradictions' (arXiv 2604.14525, April 2026) uses Z3 (QF_UFLIA) and CaDiCaL for cross-query consistency checking with unsat-core localization and counterexample-guided repair — but addresses cross-query consistency (different questions sharing a case file), not cross-trace consistency (same question, multiple reasoning paths). The EACL 2026 dynamic solver routing framework (arXiv 2510.06774) selects solvers at the problem level. But none of these methods formally cross-validate intermediate constraints across multiple candidate solutions for the same problem.\n\nThe gap: no method formally cross-validates intermediate constraints across multiple candidate solutions to produce a consistency-aware consensus signal with interpretable provenance. Concretely, SICA differs from D&P by extracting constraints from ALL paths and finding a globally consistent MAX-SAT-optimal subset (cross-path aggregation), rather than independently pruning paths with internal contradictions (per-path filtering). SICA differs from VERGE by applying MAX-SAT across multiple reasoning paths for answer selection, whereas VERGE applies the dual MCS operation within a single output for refinement feedback. SICA differs from the cross-query contradictions framework by operating on multiple traces for the same question (cross-trace scope) using weighted partial MAX-SAT for consensus, rather than on different questions in a case file (cross-query scope) using unsat-core repair. A key empirical question — how frequently does statistical consensus actually retain contradictory constraints? — remains unanswered and is central to quantifying this opportunity.\n\nRecent work on autoformalization faithfulness further motivates SICA's extraction quality pipeline: 'Do LLMs Game Formalization?' (arXiv 2604.19459, VerifAI-2 Workshop, ICLR 2026) shows that high compilation rates should not be equated with faithful reasoning, finding that two-stage formalization pipelines reveal distinct unfaithfulness patterns (axiom fabrication, premise mistranslation) that evade standard verification. This underscores the need for SICA's multi-tier extraction validation.",
  "landscape": "Standard self-consistency (Wang et al., ICLR 2023) performs majority voting on final answers and shows diminishing returns on frontier models — gains plateau at <2% with accuracy sometimes declining at high sample counts (arXiv 2511.00751). 'Consensus is Not Verification' (arXiv 2603.06612, March 2026) provides a theoretical explanation: LLM errors are strongly correlated across samples and model families, causing consensus to reinforce shared misconceptions rather than converge on truth; however, the paper finds aggregation succeeds when an external verifier exists. CRAFT (arXiv 2604.14121, April 2026) extracts consensus intermediate steps via a Reasoning Knowledge Graph using TF-IRF/Jaccard similarity and topological generation, achieving up to +8.5% accuracy over SC baselines on GSM8K, FOLIO, FLD, and OlympiadBench with K=3 traces; its authors note 'consensus ≠ correctness' and 'reduced effectiveness on symbolic math' as limitations. PoLR (ICLR 2026) uses prefix consensus to prune reasoning paths, matching SC accuracy while reducing token usage by 50-60%.\n\nDraft-and-Prune (D&P, arXiv 2603.17233, March 2026): An inference-time framework that drafts multiple natural-language plans, conditions program generation on them, prunes executable but contradictory (|S|=0) or ambiguous (|S|>1) formalizations independently for each path, and aggregates surviving paths via answer-level majority voting. Uses Z3Py for AR-LSAT/LogicalDeduction and PyKe for ProofWriter/PrOntoQA. Achieves AR-LSAT 78.43%, ProofWriter 98.33%, PrOntoQA 99.32%, LogicalDeduction 99.50% (GPT-4). Key limitation: no cross-path constraint checking or equivalence-aware deduplication.\n\nVERGE (arXiv 2601.20055, Jan 2026): A single-output neurosymbolic verify-and-refine loop. Decomposes an LLM output into atomic claims, classifies them by type, autoformalizes into FOL, and verifies joint satisfiability via Z3. Uses semantic routing (symbolic solvers for logical claims, LLM ensembles for commonsense) and Minimal Correction Subsets (MCS) for precise error localization, providing actionable feedback for iterative refinement. VERGE's K=3 refers to candidate formalizations of a single claim checked for semantic equivalence, not multiple reasoning paths. MCS (minimum claims to remove for satisfiability) is dual to MAX-SAT (maximum satisfiable subset) but is applied within one output for feedback, not across paths for consensus. Evaluated on FOLIO (84.7-89.2%), ProofWriter (85.2-93.0%), AR-LSAT (88.6-91.7%) across GPT-OSS-20B, GPT-OSS-120B, and Claude 3.7 Sonnet.\n\nSingle-solution formal verification: MATH-VF (arXiv 2505.20869, May 2025) uses a Formalizer+Critic pipeline with CAS and Z3 SMT solver for step-level verification on individual solutions, evaluated on MATH-500 and ProcessBench. SAFE (ACL 2025, arXiv 2506.04592) uses Lean4 for retrospective step-aware formal verification of individual reasoning chains, introducing the FormalStep benchmark (30,809 formal statements). PRoSFI (arXiv 2603.29500, March 2026) — 'Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries' — trains process rewards over structured formal intermediaries verified by Lean tactics, Z3, and Prover9, operating on individual 7B-model solutions; achieves 92.97% accuracy / 76.07% GPT Soundness on ProverQA-Hard. FoVer (arXiv 2505.15960, ACL 2026 Findings) — 'Training Step-Level Reasoning Verifiers with Formal Verification Tools' — uses Z3 and Isabelle for step-level error annotation in individual solutions for PRM training; demonstrates cross-task generalization to BBH subtasks (temporal sequences 97.2%, tracking shuffled objects 96.0%, word sorting 46.8% with Llama3.1-8B-PRM at Best-of-7) and to MATH, AIME, ANLI, MMLU-Pro.\n\nCross-output consistency verification: 'Quantifying Cross-Query Contradictions in Multi-Query LLM Reasoning' (arXiv 2604.14525, April 2026) addresses cross-query consistency — maintaining a globally satisfiable belief state across interdependent queries sharing a case file. Uses Z3 v4.8.17 (QF_UFLIA theory) and CaDiCaL for SAT, with unsat-core localization and counterexample-guided lexicographic repair. Achieves SetCons improvement from 0.56 to 0.94 across 390 case files spanning relational/SAT, temporal/SMT, policy/rules, and abductive domains. Crucially, this operates at cross-query scope (different questions sharing context) rather than cross-trace scope (same question, multiple reasoning paths), and uses unsat-core repair rather than weighted partial MAX-SAT consensus. SICA's differentiators are: cross-trace scope, intermediate constraint extraction from reasoning steps, and popularity-weighted MAX-SAT for answer selection.\n\nSolver routing: The EACL 2026 dynamic solver composition framework (arXiv 2510.06774) automatically identifies formal reasoning strategies and routes to specialized solvers at the problem level, achieving 27% improvement over GPT-4o. SICA's theory-aware routing operates at the finer-grained assertion level.\n\nVeriCoT (Nov 2025) formalizes individual CoT traces into FOL for entailment checking without cross-solution comparison. FregeLogic (SemEval 2026) uses Z3 as a tiebreaker for syllogistic validity.\n\nAutoformalization reliability: Grammars of Formal Uncertainty (NeurIPS 2025) demonstrates that SMT autoformalization is task-dependent: +34.8% on ProofWriter but -44.5% on FOLIO, necessitating careful benchmark selection and per-domain extraction analysis. 'Do LLMs Game Formalization?' (arXiv 2604.19459, VerifAI-2 Workshop, ICLR 2026) evaluates faithfulness of LLM autoformalization on 303 FOL problems, finding that high compilation rates (87-99%) do not guarantee faithful reasoning — two-stage pipelines reveal distinct unfaithfulness patterns: axiom fabrication (GPT-5) and premise mistranslation (DeepSeek-R1). Autoformalization surveys (arXiv 2505.23486) report ~70% success rate on physics kinematics, with selective verification reducing errors by 14-100% with minimal abstention.\n\nNo concurrent work (searched arXiv and OpenReview through May 2026) formally cross-validates intermediate constraints across multiple candidate solutions for the same problem.",
  "approach": "We propose Symbolic Invariant Consensus Aggregation (SICA): given a problem, sample K reasoning paths from a frontier open-source reasoning model (QwQ-32B via vLLM on 1-2 A100s; Qwen3-32B as secondary model for ablation), then use a prompted LLM extractor to parse each trace into typed symbolic assertions (equations, inequalities, logical predicates). SICA introduces four key technical components:\n\n(1) **Theory-aware assertion-level solver routing**: Extracted assertions are classified by constraint type and routed to appropriate solvers — Z3 for tractable theories (linear arithmetic, propositional logic, uninterpreted functions, bitvectors) and SymPy for nonlinear polynomial arithmetic, algebraic equivalence, and modular arithmetic. Unlike the EACL 2026 framework (arXiv 2510.06774) which routes at the problem level, SICA routes at the assertion level, enabling mixed-theory problems where individual steps span different solver domains (common in competition math). Assertions that neither solver can handle receive numerical spot-checking as fallback, with unverifiable assertions flagged and excluded from the consensus set (rather than silently included).\n\n(2) **Weighted partial MAX-SAT for invariant consensus**: Rather than enumerating assertion subsets (exponential worst-case), SICA leverages Z3's built-in optimization context to solve weighted partial MAX-SAT directly. Each unique assertion (deduplicated via solver-verified equivalence) is weighted by its cross-solution frequency. The optimizer finds the largest jointly satisfiable subset of assertions, weighted by popularity — a single Z3 optimization call replaces exponential subset enumeration. Per-query timeout caps (10s) bound worst-case latency. This cross-path MAX-SAT consensus is the key differentiator from Draft-and-Prune (D&P), which prunes paths independently based on internal consistency (|S|=0 or |S|>1) and aggregates surviving answers via majority voting without cross-path constraint checking. It is also distinct from VERGE's MCS, which is the dual operation (minimum claims to remove) applied within a single output for refinement feedback rather than across paths for answer selection. It further differs from the cross-query contradictions framework (arXiv 2604.14525), which uses unsat-core localization and counterexample-guided repair across different questions sharing a case file — SICA uses weighted partial MAX-SAT across different reasoning traces for the same question.\n\n(3) **Invariant-backed answer scoring**: Each candidate answer is scored by the coverage and weight of its supporting assertions within the MAX-SAT-optimal consistent set, yielding a continuous invariant consensus score. This captures partial structural agreement even when final answers diverge, and provides interpretable provenance (each score is backed by a specific set of formally verified constraints).\n\n(4) **Extraction quality assurance pipeline**: To address the documented task-dependence of autoformalization (Grammars of Formal Uncertainty, NeurIPS 2025) and the unfaithfulness risks identified by 'Do LLMs Game Formalization?' (arXiv 2604.19459), we implement a three-tier extraction quality pipeline: (a) syntactic validation — each extracted assertion must parse in the target solver's input language; (b) semantic spot-checking — a random 20% of assertions are checked against the original natural language step via an LLM judge for semantic fidelity, specifically targeting the axiom fabrication and premise mistranslation failure modes identified in the faithfulness literature; (c) coverage tracking — we report 'verifiable assertion coverage' (% of extracted assertions that successfully enter the MAX-SAT pipeline) per benchmark as a first-class metric. Extraction failures cascade to numerical fallback or abstention, preventing malformed inputs from corrupting the consensus signal.\n\n**Limitations of formal cross-validation**: SICA's MAX-SAT consensus catches contradictory constraints but cannot detect universally-wrong-but-mutually-consistent constraints caused by correlated extraction errors. 'Consensus is Not Verification' (arXiv 2603.06612) demonstrates that LLM errors are strongly correlated across samples and even across model families, which implies that if all K paths produce the same wrong formalization of a constraint, MAX-SAT will see K consistent-but-wrong assertions and cannot flag the error. This is a fundamental limitation of any approach combining LLM extraction with formal verification: the verifier guarantees consistency, not correctness of the extraction. SICA's semantic spot-checking tier partially mitigates this — by sampling 20% of assertions for LLM-judge semantic fidelity checks, it can catch systematic mistranslation patterns. However, if the extraction LLM and the judge LLM share the same correlated bias (as the correlated errors literature suggests is likely), the mitigation is incomplete. We acknowledge this limitation explicitly and note two potential future mitigations: (a) using structurally diverse extractor models (e.g., symbolic parsers alongside LLM extractors) to decorrelate extraction errors, and (b) grounding extracted constraints against external knowledge sources (CAS simplification, unit-test-style numerical spot-checking) that do not share LLM inductive biases. We include FOLIO as a diagnostic ablation where SMT autoformalization is documented to hurt (-44.5%), precisely to empirically characterize the boundary between domains where SICA's extraction is faithful enough to help versus where correlated errors dominate.\n\n**Dual-track evaluation plan**:\n\n*Track A — EMNLP 2026 (ARR May 25, primary target, 14 days):* Scoped evaluation with K=12 traces on 5 core benchmarks plus 3 BBH subtasks:\n- **MATH-500** (algebraic/arithmetic reasoning; QwQ-32B ~90.6%)\n- **AIME 2024** (competition math with mixed-theory constraints; QwQ-32B ~79.5%)\n- **ProofWriter** (formal logic; enables direct comparison with D&P 98.33% and VERGE 85.2-93.0%)\n- **FOLIO** (first-order logic; diagnostic ablation — SMT autoformalization documented to hurt -44.5% here)\n- **BBH** (3 subtasks: logical deduction, tracking shuffled objects, temporal sequences — enables direct comparison with FoVer's BBH evaluation at Best-of-7; tests cross-domain generalization to structured informal reasoning)\n\nBaselines for Track A: self-consistency, CRAFT, D&P (on ProofWriter), VERGE (on ProofWriter/FOLIO).\n\n*Track B — AAAI 2027 (paper deadline ~August 1, extended version):* Expanded to K=16 traces on all Track A benchmarks plus:\n- **AIME 2025** (tests generalization to unseen competition problems; available via MathArena/aime_2025 on HuggingFace)\n- **GPQA Diamond** (graduate-level science; QwQ-32B ~65.2%; per-domain reporting for physics/chemistry vs. biology)\n- **LogiQA 2.0** (natural language logical reasoning; 8,678 questions; tests constraint extraction beyond math/formal logic)\n- Additional BBH subtasks and full ablation suite\n\n**ARC-Challenge exclusion justification**: ARC-Challenge (Clark et al., 2018) consists of multiple-choice grade-school science questions that primarily test factual knowledge retrieval (e.g., 'Which mineral is the hardest?', 'What happens when water freezes?'). Most questions lack the multi-step constraint structure required for meaningful symbolic assertion extraction — they involve domain knowledge rather than chains of extractable equations, inequalities, or logical predicates. Including ARC-Challenge would likely yield near-zero verifiable assertion coverage, providing no insight beyond confirming SICA's domain specificity (which FOLIO already demonstrates as a negative diagnostic). We note this scope limitation explicitly.\n\n**Metrics and analyses**:\n- Primary: accuracy, calibration (ECE), informativeness of partial invariant agreement when candidates disagree\n- **Contradiction frequency analysis** (centerpiece experiment): For each problem across all benchmarks, we measure how often CRAFT's statistical consensus retains logically contradictory constraint pairs. We report the 'contradiction rate' — the fraction of problems where at least one pair of popular constraints (appearing in ≥3 of K traces) are mutually unsatisfiable. If >15%, this validates SICA's core motivation; if <5%, we honestly acknowledge limited practical impact on this axis and emphasize interpretability/provenance instead.\n- **D&P comparison**: On ProofWriter (shared benchmark), we compare SICA's cross-path MAX-SAT consensus against D&P's per-path pruning + answer-level voting, specifically measuring: (a) how many problems have cross-path contradictions that D&P's per-path pruning misses, and (b) whether MAX-SAT-backed scoring outperforms answer-level majority voting among surviving paths.\n- **FoVer comparison on BBH**: On the 3 shared BBH subtasks, we compare SICA's inference-time cross-path consensus against FoVer's training-time PRM approach (Llama3.1-8B-PRM at Best-of-7: temporal 97.2%, tracking 96.0%, word sorting 46.8%), analyzing whether cross-path formal consensus provides complementary signal to trained process reward models.\n- **Extraction accuracy ablation**: Per-benchmark measurement of (a) syntactic parse rate, (b) semantic fidelity (manual annotation on 100 samples per benchmark), and (c) error propagation analysis — how X% extraction error degrades MAX-SAT consensus quality via controlled noise injection. Per the findings of 'Do LLMs Game Formalization?', we specifically track axiom fabrication and premise mistranslation rates.\n- **Correlated extraction error analysis**: On a subset of problems (100 per benchmark), we measure cross-path extraction agreement — the fraction of assertions that are semantically equivalent across all K traces — to empirically quantify the degree of correlated extraction and assess how much independent signal SICA's MAX-SAT actually receives.\n- **Compute-normalized comparison**: Report total tokens generated, wall-clock time per problem, and decomposed latency (inference, extraction, solver, MAX-SAT) for each method. Plot accuracy vs. total compute (tokens) curves. If SICA takes 5x compute of vanilla SC for +2% accuracy, we justify via interpretability/soundness or acknowledge the tradeoff.\n\nThe primary contribution is not raw accuracy improvement over SC (which has diminishing returns on frontier models) but rather: (a) formal soundness guarantees on the consensus signal, (b) interpretable constraint-level provenance for each answer, (c) detecting logically inconsistent popular reasoning steps that both statistical consensus (CRAFT) and per-path pruning (D&P) miss — with empirical quantification of how frequently this occurs, (d) systematic domain analysis of formal cross-solution verification including where it helps (ProofWriter, BBH logical deduction) vs. hurts (FOLIO), and (e) empirical characterization of correlated extraction errors as a fundamental limitation of LLM-based autoformalization in consensus settings.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~180-240h A100 80GB (5 benchmarks + 3 BBH subtasks × K=12 traces + extraction + ablations)",
      "gpu_utilization": "Low (~20-30%); GPUs idle during coding, debugging solver routing, manual extraction annotation",
      "timeline": "2-3 months",
      "team": "1-2 researchers with formal methods and LLM experience",
      "estimated_gpu_cost": "$235-310 (at ~$1.30/hr typical A100 spot rate)",
      "h100_equivalent": "~90-120h H100 (well within 200h H100 budget)"
    },
    "human_in_loop": {
      "gpu_hours": "~220-300h A100 80GB",
      "gpu_utilization": "Moderate (~50-60%); agent codes and runs experiments between human review gates",
      "timeline": "4-6 weeks (fits AAAI 2027 extended version with writing buffer)",
      "team": "1 researcher, ~40-50min/day reviewing extraction quality, solver routing correctness, contradiction analysis, D&P comparison design, and BBH extraction quality; ~6h total for manual semantic fidelity annotation (100 samples × 5 benchmarks + 3 BBH subtasks)",
      "claude_api_cost": "$200-400 (est. 2000-4000 Opus turns)",
      "estimated_gpu_cost": "$285-390",
      "h100_equivalent": "~110-150h H100 (within 200h H100 budget)",
      "risk_note": "Solver routing heuristics require human judgment for edge cases; CRAFT replication may need prompt tuning; BBH logical deduction extraction quality needs validation"
    },
    "auto_research": {
      "gpu_hours": "~300-400h A100 80GB (Track A: 5 benchmarks + 3 BBH subtasks × K=12 × core ablations)",
      "gpu_utilization": "High (~85-95%); agent pipelines inference, extraction, and solving continuously; batched vLLM serving keeps GPUs saturated",
      "timeline": "10-14 days with 2-4 A100s available (fits EMNLP 2026 ARR May 25 deadline)",
      "team": "0 (initial setup only, ~3 hours)",
      "claude_api_cost": "$350-600 (est. 3500-6000 Opus turns)",
      "estimated_gpu_cost": "$390-520",
      "h100_equivalent": "~150-200h H100 (within 200h H100 budget with K=12 and 5+3 benchmarks)",
      "speed_bottleneck": "GPU count for parallel vLLM inference across benchmarks × 12 samples; secondary bottleneck is Z3 MAX-SAT optimization time (mitigated by 10s per-query timeout)",
      "risk_note": "Automated extraction may produce malformed solver input in ~10-20% of traces; without human review the agent may over-tune extraction prompts to specific benchmarks; contradiction frequency analysis needs careful statistical framing to avoid over-claiming; 14-day timeline is tight but feasible in full auto mode with scoped benchmark set"
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline: May 25, 2026 — 14 days from now; primary target with Track A scoped evaluation)",
    "AAAI 2027 (abstract deadline: ~July 25, 2026; paper deadline: ~August 1, 2026 — extended version with Track B full evaluation)"
  ],
  "level": "solid",
  "key_references": [
    "Self-Consistency Improves Chain of Thought Reasoning in Language Models (ICLR 2023)",
    "CRAFT: Correct Prediction, Wrong Steps? Consensus Reasoning Knowledge Graph for Robust Chain-of-Thought Synthesis (arXiv 2604.14121, April 2026)",
    "Draft-and-Prune: Improving the Reliability of Auto-formalization for Logical Reasoning (arXiv 2603.17233, March 2026)",
    "PoLR: The Path of Least Resistance — Guiding LLM Reasoning Trajectories with Prefix Consensus (ICLR 2026)",
    "VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (arXiv 2601.20055, Jan 2026)",
    "VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks (arXiv 2025)",
    "MATH-VF: Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving (arXiv 2505.20869, May 2025)",
    "SAFE: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification (ACL 2025, arXiv 2506.04592)",
    "Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition (EACL 2026, arXiv 2510.06774)",
    "PRoSFI: Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries (arXiv 2603.29500, March 2026)",
    "FoVer: Training Step-Level Reasoning Verifiers with Formal Verification Tools (arXiv 2505.15960, ACL 2026 Findings)",
    "Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks (NeurIPS 2025)",
    "FregeLogic at SemEval 2026 Task 11: Hybrid Neuro-Symbolic Architecture for Syllogistic Validity (SemEval 2026)",
    "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (arXiv 2604.19459, VerifAI-2 Workshop, ICLR 2026)",
    "Reevaluating Self-Consistency Scaling in Multi-Agent Systems (arXiv 2511.00751)",
    "Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling (NAACL 2025)",
    "Faithful Logical Reasoning via Symbolic Chain-of-Thought (ACL 2024)",
    "Autoformalization in the Era of Large Language Models: A Survey (arXiv 2505.23486, May 2025)",
    "Consensus is Not Verification: Why Crowd Wisdom Strategies Fail for LLM Truthfulness (arXiv 2603.06612, March 2026)",
    "Quantifying Cross-Query Contradictions in Multi-Query LLM Reasoning (arXiv 2604.14525, April 2026)"
  ],
  "description": "We propose Symbolic Invariant Consensus Aggregation (SICA), a method that formally cross-validates intermediate constraints extracted from multiple LLM reasoning paths to produce a soundness-guaranteed consensus signal. While CRAFT (April 2026) demonstrates the value of intermediate-step consensus via statistical similarity (TF-IRF/Jaccard), its authors explicitly acknowledge 'consensus ≠ correctness' and 'reduced effectiveness on symbolic math.' This limitation is theoretically grounded by 'Consensus is Not Verification' (arXiv 2603.06612, March 2026), which proves that LLM errors are strongly correlated across samples and model families, causing pure consensus to fail — but critically finds that 'aggregation improves performance when a verifier exists,' directly motivating SICA's approach. Draft-and-Prune (D&P, March 2026) improves autoformalization reliability by independently pruning paths with internal contradictions and aggregating survivors via majority voting, but does not perform cross-path constraint checking — its authors note they 'aggregate predictions at the answer level and do not cluster or de-duplicate candidates by symbolic equivalence.' Meanwhile, VERGE (Jan 2026) verifies and refines a single LLM output by decomposing it into atomic claims, checking joint satisfiability via Z3, and using Minimal Correction Subsets (MCS) to provide targeted refinement feedback — but operates on one output, not across reasoning paths. In the adjacent cross-output verification space, 'Quantifying Cross-Query Contradictions' (arXiv 2604.14525, April 2026) uses Z3 (QF_UFLIA) and CaDiCaL for cross-query consistency checking with unsat-core repair, but addresses cross-query consistency (different questions sharing a case file) rather than cross-trace consistency (same question, multiple paths). Single-solution formal verification (MATH-VF uses CAS+Z3; SAFE uses Lean4; PRoSFI uses Lean/Z3/Prover9 for structured formal intermediaries on 7B models; FoVer (arXiv 2505.15960) uses Z3+Isabelle for PRM training data with cross-task generalization to BBH) improves reliability but none cross-validate across solutions.\n\nSICA fills this gap by extracting typed symbolic assertions from K sampled reasoning traces, routing them to appropriate solvers via assertion-level theory-aware dispatch (Z3 for linear arithmetic and propositional logic; SymPy for nonlinear polynomial and algebraic constraints — finer-grained than the EACL 2026 problem-level solver routing), and using Z3's built-in weighted partial MAX-SAT optimization to find the largest jointly satisfiable assertion set weighted by cross-solution frequency. SICA's MAX-SAT consensus across paths is the cross-path counterpart to VERGE's within-output MCS (dual operations: MAX-SAT keeps the maximum consistent subset; MCS removes the minimum inconsistent subset), and differs from cross-query contradiction checking by operating on multiple traces for the same question via weighted consensus rather than unsat-core repair across different questions. A three-tier extraction quality pipeline (syntactic validation, semantic spot-checking targeting the unfaithfulness patterns identified by 'Do LLMs Game Formalization?' (arXiv 2604.19459), and coverage tracking) addresses the documented task-dependence of autoformalization.\n\nWe explicitly acknowledge a fundamental limitation: SICA's MAX-SAT consensus catches contradictory constraints but cannot detect universally-wrong-but-consistent constraints caused by correlated extraction errors — the same correlated error phenomenon documented by 'Consensus is Not Verification.' The semantic spot-checking tier partially mitigates this, but correlated biases between the extractor and judge LLMs limit its effectiveness. We include FOLIO as a diagnostic ablation and propose a correlated extraction error analysis to empirically characterize this boundary.\n\nWe adopt a dual-track evaluation plan. Track A (EMNLP 2026, ARR May 25): scoped evaluation with K=12 on MATH-500, AIME 2024, ProofWriter, FOLIO, and 3 BBH subtasks (logical deduction, tracking shuffled objects, temporal sequences) using QwQ-32B via vLLM, comparing against SC, CRAFT, D&P, VERGE, and FoVer. BBH subtasks enable direct comparison with FoVer (ACL 2026) which reports Best-of-7 results on the same tasks (temporal 97.2%, tracking 96.0%, word sorting 46.8%). Track B (AAAI 2027): expanded to K=16 with AIME 2025, GPQA Diamond, and LogiQA 2.0 added. ARC-Challenge is excluded because its multiple-choice science knowledge questions lack the multi-step constraint structure needed for meaningful symbolic extraction (most test factual recall rather than chains of extractable logical predicates). The centerpiece experiment is a contradiction frequency analysis measuring how often statistical consensus retains logically contradictory constraint pairs. FOLIO serves as a diagnostic ablation where SMT is documented to hurt (-44.5%). Primary contributions: formal soundness guarantees, interpretable constraint-level provenance, empirically-quantified detection of contradictory consensus that both statistical methods and per-path pruning miss, systematic domain analysis of formal cross-solution verification, and honest characterization of the correlated extraction error limitation. Auto-mode compute fits within 200h H100 budget at K=12 with 5+3 benchmarks.",
  "project_name": "symb_invariant_consensus",
  "source": "web_research"
}

## Reviewer feedback (round 6)
Issues: ["FEASIBILITY — No day-by-day timeline for the 13-day sprint to ARR May 25. The proposal says '10-14 days' in auto mode but does not allocate time for: (1) pipeline implementation and debugging, (2) extraction prompt development per domain, (3) running experiments across 8 benchmark configs, (4) analysis and figure generation, (5) paper writing and formatting. A credible timeline would show these phases don't overlap impossibly. Paper writing alone typically takes 3-5 days for a polished submission.", "FEASIBILITY — No minimum viable scope fallback. If extraction quality proves unreliable on 1-2 benchmarks (plausible given documented task-dependence of autoformalization), what is the minimum credible submission? E.g., could Track A be scoped to 3 benchmarks (MATH-500, ProofWriter, AIME 2024) at K=8 with a shortened paper? Without a fallback plan, the proposal is all-or-nothing on a 13-day deadline.", "USER REQUIREMENT — AIME 2025 excluded from Track A despite user explicitly listing it. Since AIME 2025 uses the identical evaluation pipeline as AIME 2024 (same problem format, same constraint extraction approach), adding it to Track A is trivially low-cost (one additional benchmark run) and directly satisfies a user requirement. No justification is given for deferring it to Track B.", "MINOR — 'Correct Reasoning Paths Visit Shared Decision Pivots' (ROMA, arXiv 2509.21549, ICLR 2026 under review) extracts shared intermediate checkpoints ('decision pivots') across multiple reasoning paths and uses a learned verifier to identify correct reasoning. While ROMA uses neural verification rather than formal solvers, it occupies the adjacent conceptual space of cross-path intermediate-step analysis and could be cited in the landscape section to strengthen the positioning: SICA provides formal guarantees where ROMA uses learned signals."]
Feedback: The proposal is close to passing — all prior substantive issues are resolved, references are verified, the gap is genuine, and the intellectual honesty (FOLIO diagnostic, correlated error limitations) is commendable. Three targeted fixes to cross the threshold:

1. **Add a realistic day-by-day timeline for Track A**: Break the 13-day sprint into phases: Days 1-3 (pipeline implementation: extraction prompts, solver routing, MAX-SAT wrapper), Days 4-7 (experiments: 8 benchmark configs × K=12), Days 8-10 (analysis: contradiction frequency, ablations, figures), Days 11-13 (paper writing and formatting). If paper writing cannot fit, acknowledge this honestly and consider submitting to the June ARR cycle instead (which would still allow EMNLP 2026 commitment via prior-cycle papers, though this depends on ARR policy — verify).

2. **Define a minimum viable scope**: If the full 5+3 benchmark plan proves too ambitious, what is the minimum credible submission? Suggest: 3 core benchmarks (MATH-500, ProofWriter, AIME 2024) at K=12, plus FOLIO as negative diagnostic = 4 benchmarks total. This would still demonstrate the core contribution (cross-path MAX-SAT consensus, contradiction frequency analysis, domain analysis including negative results) while leaving headroom for implementation and writing.

3. **Move AIME 2025 to Track A**: It uses the identical pipeline as AIME 2024 and is essentially free to add. This satisfies the user's explicit requirement and provides a generalization test (unseen competition problems).

Minor: cite ROMA (arXiv 2509.21549) as a neural counterpart to SICA's formal cross-path analysis in the landscape section.

## Instructions
- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.
- Address each issue specifically.

## 深度调研要求（每一轮修订都必须执行）

不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。

1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。
   - 搜索最新的相关论文（arXiv, conference proceedings）
   - 搜索 benchmark/leaderboard 确认当前 SOTA
   - 搜索可能遗漏的相关工作和 concurrent work

2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，
   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。

3. **深度思考**：在修订之前，先独立思考以下问题：
   - 这个 idea 的核心假设是否仍然成立？
   - reviewer 的批评是否揭示了更深层的问题？
   - 有没有更好的 framing 或 approach 来解决同一个核心问题？
   - 修订后的 idea 相比上一版有什么本质性的改进？

4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，
   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。

## 针对 Review 意见的定向搜索

对 reviewer 指出的每个问题，执行以下搜索流程：

1. **如果 reviewer 说'已有类似工作'**：
   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读
   - 搜索该论文的 cited-by，找到后续跟进工作
   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot

2. **如果 reviewer 说'SOTA 过时'**：
   - 用 Papers With Code 查看当前排行榜
   - 搜索过去 6 个月的最新方法
   - 更新你的 landscape 和 baseline

3. **如果 reviewer 说'可行性有问题'**：
   - 搜索类似规模实验的实际成本和时间线
   - 搜索 GitHub 上是否有可复用的实现
   - 搜索相关数据集/模型的可获取性

4. **如果 reviewer 说'novelty 不足'**：
   - 对核心方法尽量做 3-5 种不同关键词组合的搜索
   - 搜索相邻领域是否有类似思路
   - 如果确实 novelty 不足，考虑 major revision 或 pivot

- Use WebSearch to find updated information if the reviewer flagged outdated claims.
- You have full freedom in how much to change:
  - Minor fix: if only specific details are wrong, correct them and keep everything else.
  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.
  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.
- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.
- In the output JSON, include a "change_type" field with one of: "minor", "major", or "pivot" to indicate the scope of your changes.
- Output the revised idea as a COMPLETE JSON object (same schema as original, plus "change_type").

## 停滞提醒
这个 idea 已经经过 6 轮修订，近 3 轮的平均分从 3.5 到 3.6，没有明显改善。

请认真思考：
- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？
- 如果你认为问题出在 approach 而非 framing，可以做 major revision。
- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。
- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。

最终由你判断——做你认为最能提升 idea 质量的选择。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d9295023-136d-4eec-b865-315f1454c5eb",
  "type": "user",
  "uuid": "2b7d45dd-b6b2-472f-bc91-ae2fd501d917",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-12T00:12:39.293Z_

```json
{
  "parentUuid": "2b7d45dd-b6b2-472f-bc91-ae2fd501d917",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
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
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
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
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "5c7cca6a-5792-4c54-a7d3-88a594ecfcad",
  "timestamp": "2026-05-12T00:12:39.293Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-12T00:12:39.293Z_

```json
{
  "parentUuid": "5c7cca6a-5792-4c54-a7d3-88a594ecfcad",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "804b7841-b63e-4eef-be4e-725ebba1c1a5",
  "timestamp": "2026-05-12T00:12:39.293Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"Formally-Verified Intermediate Constraint Consensus Across Reasoning P…",
  "leafUuid": "804b7841-b63e-4eef-be4e-725ebba1c1a5",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise SICA feasibility with realistic timeline and minimum viable scope",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3"
}
```

---

### Assistant

_source line 8 · 2026-05-12T00:12:51.865Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully. The proposal has gone through 6 rounds of revision with stagnating scores (3.5-3.6). The reviewer says it's "close to passing" and needs three targeted fixes plus one minor addition:

1. Add a realistic day-by-day timeline for the 13-day Track A sprint
2. Define a minimum viable scope fallback
3. Move AIME 2025 to Track A
4. Minor: cite ROMA (arXiv 2509.21549)

The reviewer explicitly says "all prior substantive issues are resolved, references are verified, the gap is genuine, and the intellectual honesty is commendable." This means the core idea is sound — the issues are about feasibility planning and scope, not about the fundamental approach.


The feedback is clear and actionable, so I'll make these targeted changes. I need to search for the ROMA paper to cite it properly, verify the ARR submission timeline for the June cycle, and work out a realistic day-by-day schedule for the sprint along with a fallback scope definition.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "804b7841-b63e-4eef-be4e-725ebba1c1a5",
  "isSidechain": false,
  "requestId": "req_011Cawhz5nCt2dQQkgvWiQBo",
  "type": "assistant",
  "uuid": "d20972a6-79bf-4cd3-abb2-13c06306e165",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVNw4zXSyPUUToupRRKvy9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16473,
      "cache_read_input_tokens": 11841,
      "output_tokens": 429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16473,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 429,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16473,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16473
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-12T00:12:52.058Z_

I'll address the reviewer's targeted feedback. The core idea is validated — these are feasibility and scope fixes. Let me research the specific items mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d20972a6-79bf-4cd3-abb2-13c06306e165",
  "isSidechain": false,
  "requestId": "req_011Cawhz5nCt2dQQkgvWiQBo",
  "type": "assistant",
  "uuid": "86605759-880f-4ede-b36e-f33719b6b6d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVNw4zXSyPUUToupRRKvy9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16473,
      "cache_read_input_tokens": 11841,
      "output_tokens": 429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16473,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 429,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16473,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16473
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-12T00:12:52.458Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UUAz4XUVspA8zzAP7jLKHC`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86605759-880f-4ede-b36e-f33719b6b6d6",
  "isSidechain": false,
  "requestId": "req_011Cawhz5nCt2dQQkgvWiQBo",
  "type": "assistant",
  "uuid": "5aa50679-f57b-40e9-a950-6798f0611526",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LVNw4zXSyPUUToupRRKvy9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16473,
      "cache_read_input_tokens": 11841,
      "output_tokens": 429,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16473,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 429,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16473,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16473
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-12T00:12:52.465Z_

<details><summary>↩ Tool result · `toolu_01UUAz4XUVspA8zzAP7jLKHC`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5aa50679-f57b-40e9-a950-6798f0611526",
  "isSidechain": false,
  "promptId": "d9295023-136d-4eec-b865-315f1454c5eb",
  "type": "user",
  "uuid": "c87d72cf-bd3c-4b1e-b264-11107d2d792c",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "5aa50679-f57b-40e9-a950-6798f0611526",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-12T00:12:56.968Z_

<details><summary>Logged reasoning block</summary>

```text
Let me search for the specific items the reviewer mentioned:
1. ROMA (arXiv 2509.21549) - need to verify this paper and understand it
2. ARR June 2026 cycle dates
3. Any practical timeline references for similar projects
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c87d72cf-bd3c-4b1e-b264-11107d2d792c",
  "isSidechain": false,
  "requestId": "req_011Cawi14cYHxrnBDaDuXgRM",
  "type": "assistant",
  "uuid": "7203087e-d5a9-494f-89bc-040d2908e5d9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GKgYfFdeDsqeqpWtCV8wYe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 28314,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1449,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 314,
          "cache_read_input_tokens": 28314,
          "cache_creation_input_tokens": 1449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1449
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-12T00:12:58.412Z_

Let me research the specific items the reviewer flagged.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7203087e-d5a9-494f-89bc-040d2908e5d9",
  "isSidechain": false,
  "requestId": "req_011Cawi14cYHxrnBDaDuXgRM",
  "type": "assistant",
  "uuid": "7bb91534-7bde-47a7-8ab6-0545d068a974",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GKgYfFdeDsqeqpWtCV8wYe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 28314,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1449,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 314,
          "cache_read_input_tokens": 28314,
          "cache_creation_input_tokens": 1449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1449
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-12T00:12:59.709Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015v2PTCMqpqsjzDT3bNBVT7`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.21549",
  "prompt": "Extract the full title, authors, date, abstract, and key method details of this paper. What are \"decision pivots\"? How does the method work across multiple reasoning paths? What benchmarks are used?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7bb91534-7bde-47a7-8ab6-0545d068a974",
  "isSidechain": false,
  "requestId": "req_011Cawi14cYHxrnBDaDuXgRM",
  "type": "assistant",
  "uuid": "2fd00aa3-2b97-4b94-91ac-7a573f0ffe6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GKgYfFdeDsqeqpWtCV8wYe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 28314,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1449,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 314,
          "cache_read_input_tokens": 28314,
          "cache_creation_input_tokens": 1449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1449
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-12T00:12:59.851Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KSKssQ7p7xXVq4TCmK6LY5`</summary>

```json
{
  "query": "ACL Rolling Review ARR June 2026 submission deadline cycle"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2fd00aa3-2b97-4b94-91ac-7a573f0ffe6d",
  "isSidechain": false,
  "requestId": "req_011Cawi14cYHxrnBDaDuXgRM",
  "type": "assistant",
  "uuid": "3396cc15-4942-4c64-86a1-a7a1c6a599f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GKgYfFdeDsqeqpWtCV8wYe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 28314,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1449,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 314,
          "cache_read_input_tokens": 28314,
          "cache_creation_input_tokens": 1449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1449
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-12T00:13:01.397Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q5uffBbSRSdZzfGbHoyoPp`</summary>

```json
{
  "query": "ROMA \"decision pivots\" reasoning paths ICLR 2026 cross-path verification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3396cc15-4942-4c64-86a1-a7a1c6a599f6",
  "isSidechain": false,
  "requestId": "req_011Cawi14cYHxrnBDaDuXgRM",
  "type": "assistant",
  "uuid": "8fe25d8c-a9bc-4f43-b703-7fc95f777460",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GKgYfFdeDsqeqpWtCV8wYe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1449,
      "cache_read_input_tokens": 28314,
      "output_tokens": 314,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1449,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 314,
          "cache_read_input_tokens": 28314,
          "cache_creation_input_tokens": 1449,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1449
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-12T00:13:04.265Z_

<details><summary>↩ Tool result · `toolu_01KSKssQ7p7xXVq4TCmK6LY5`</summary>

```text
Web search results for query: "ACL Rolling Review ARR June 2026 submission deadline cycle"

Links: [{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"https://aclrollingreview.org/"},{"title":"ACLRollingReview (@ReviewAcl) / Posts / X","url":"https://x.com/ReviewAcl"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"},{"title":"aclrollingreview/dates.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/dates.md"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"}]

Based on my search results, I found information about the ACL Rolling Review schedule. The ACL Peer Review Committee recommended switching to 10-week cycles, with the new schedule starting in May 2025.

However, the search results don't contain specific details about a June 2026 submission deadline cycle. The submission deadline is always the 15th of the month following the standard schedule, which would suggest a June 15, 2026 deadline if a June cycle exists. 

The search results show detailed information about the ARR website and various cycles, but they don't explicitly list the complete schedule through June 2026. For the most current and detailed information about the June 2026 submission deadline and cycle details, I recommend checking the official ACL Rolling Review website at **aclrollingreview.org/dates**, which should have a comprehensive table listing all upcoming cycles and key dates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3396cc15-4942-4c64-86a1-a7a1c6a599f6",
  "isSidechain": false,
  "promptId": "d9295023-136d-4eec-b865-315f1454c5eb",
  "type": "user",
  "uuid": "bd4e64a9-5420-4526-9161-4ff0eaca8abf",
  "toolUseResult": {
    "query": "ACL Rolling Review ARR June 2026 submission deadline cycle",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BVemdbStPU84Hx1M6CNtPS",
        "content": [
          {
            "title": "Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/dates"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "Main Conference - ACL 2026",
            "url": "https://2026.aclweb.org/calls/main_conference_papers/"
          },
          {
            "title": "ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "https://aclrollingreview.org/"
          },
          {
            "title": "ACLRollingReview (@ReviewAcl) / Posts / X",
            "url": "https://x.com/ReviewAcl"
          },
          {
            "title": "Call for Main Conference Papers -",
            "url": "https://2026.eacl.org/calls/papers/"
          },
          {
            "title": "How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/reviewing"
          },
          {
            "title": "aclrollingreview/dates.md at main · acl-org/aclrollingreview",
            "url": "https://github.com/acl-org/aclrollingreview/blob/main/dates.md"
          },
          {
            "title": "AI Conference Deadlines",
            "url": "https://mlciv.com/ai-deadlines/"
          },
          {
            "title": "Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics",
            "url": "http://aclrollingreview.org/incentives2026"
          }
        ]
      },
      "Based on my search results, I found information about the ACL Rolling Review schedule. The ACL Peer Review Committee recommended switching to 10-week cycles, with the new schedule starting in May 2025.\n\nHowever, the search results don't contain specific details about a June 2026 submission deadline cycle. The submission deadline is always the 15th of the month following the standard schedule, which would suggest a June 15, 2026 deadline if a June cycle exists. \n\nThe search results show detailed information about the ARR website and various cycles, but they don't explicitly list the complete schedule through June 2026. For the most current and detailed information about the June 2026 submission deadline and cycle details, I recommend checking the official ACL Rolling Review website at **aclrollingreview.org/dates**, which should have a comprehensive table listing all upcoming cycles and key dates."
    ],
    "durationSeconds": 4.409650348000003
  },
  "sourceToolAssistantUUID": "3396cc15-4942-4c64-86a1-a7a1c6a599f6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-12T00:13:05.585Z_

<details><summary>↩ Tool result · `toolu_015v2PTCMqpqsjzDT3bNBVT7`</summary>

```text
# Paper Summary: Correct Reasoning Paths Visit Shared Decision Pivots

**Full Title:** Correct Reasoning Paths Visit Shared Decision Pivots

**Authors:** Dongkyu Cho, Amy B.Z. Zhang, Bilel Fehri, Sheng Wang, Rumi Chunara, Hengrui Cai, Rui Song

**Submission Date:** September 25, 2025 (Latest revision: February 7, 2026)

**Venue:** NeurIPS 2025 Workshop on Foundations of Reasoning in Language Models (FoRLM)

---

## Abstract

The paper addresses verification of chain-of-thought reasoning in LLMs by introducing "decision pivots" as checkpoints that correct reasoning paths must reach. The researchers hypothesize that while correct reasoning may vary stylistically, it converges on shared pivots, whereas incorrect reasoning violates them.

---

## What Are Decision Pivots?

Decision pivots are described as "minimal, verifiable checkpoints that any correct reasoning path must visit." They function as critical junctures in the reasoning process that distinguish correct from incorrect solutions.

---

## Methodology Across Reasoning Paths

The self-training pipeline operates in three stages:

1. **Mining:** Sample diverse reasoning paths and identify shared decision pivots
2. **Compression:** Use an auxiliary verifier to create "pivot-focused short-path reasoning"
3. **Post-training:** Train the model on self-generated outputs without external ground truth or metrics

---

## Benchmarks

The research evaluates on three standard datasets:
- **LogiQA** (logical reasoning)
- **MedQA** (medical question answering)
- **MATH500** (mathematical problems)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2fd00aa3-2b97-4b94-91ac-7a573f0ffe6d",
  "isSidechain": false,
  "promptId": "d9295023-136d-4eec-b865-315f1454c5eb",
  "type": "user",
  "uuid": "23d2bc9f-62a3-46af-bd55-bc4e3964a1ea",
  "toolUseResult": {
    "bytes": 45907,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Summary: Correct Reasoning Paths Visit Shared Decision Pivots\n\n**Full Title:** Correct Reasoning Paths Visit Shared Decision Pivots\n\n**Authors:** Dongkyu Cho, Amy B.Z. Zhang, Bilel Fehri, Sheng Wang, Rumi Chunara, Hengrui Cai, Rui Song\n\n**Submission Date:** September 25, 2025 (Latest revision: February 7, 2026)\n\n**Venue:** NeurIPS 2025 Workshop on Foundations of Reasoning in Language Models (FoRLM)\n\n---\n\n## Abstract\n\nThe paper addresses verification of chain-of-thought reasoning in LLMs by introducing \"decision pivots\" as checkpoints that correct reasoning paths must reach. The researchers hypothesize that while correct reasoning may vary stylistically, it converges on shared pivots, whereas incorrect reasoning violates them.\n\n---\n\n## What Are Decision Pivots?\n\nDecision pivots are described as \"minimal, verifiable checkpoints that any correct reasoning path must visit.\" They function as critical junctures in the reasoning process that distinguish correct from incorrect solutions.\n\n---\n\n## Methodology Across Reasoning Paths\n\nThe self-training pipeline operates in three stages:\n\n1. **Mining:** Sample diverse reasoning paths and identify shared decision pivots\n2. **Compression:** Use an auxiliary verifier to create \"pivot-focused short-path reasoning\"\n3. **Post-training:** Train the model on self-generated outputs without external ground truth or metrics\n\n---\n\n## Benchmarks\n\nThe research evaluates on three standard datasets:\n- **LogiQA** (logical reasoning)\n- **MedQA** (medical question answering)\n- **MATH500** (mathematical problems)",
    "durationMs": 5872,
    "url": "https://arxiv.org/abs/2509.21549"
  },
  "sourceToolAssistantUUID": "2fd00aa3-2b97-4b94-91ac-7a573f0ffe6d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-12T00:13:08.655Z_

<details><summary>↩ Tool result · `toolu_01Q5uffBbSRSdZzfGbHoyoPp`</summary>

```text
Web search results for query: "ROMA "decision pivots" reasoning paths ICLR 2026 cross-path verification"

Links: [{"title":"Correct Reasoning Paths Visit Shared Decision Pivots Dongkyu Cho1∗,","url":"https://arxiv.org/pdf/2509.21549"},{"title":"ICLR 2026 Papers","url":"https://iclr.cc/virtual/2026/papers.html"},{"title":"ICLR 2026 Statistics - Paper Copilot","url":"https://papercopilot.com/statistics/iclr-statistics/iclr-2026-statistics/"},{"title":"ICLR 2026 Workshop LLM Reasoning | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FWorkshop%2FLLM_Reasoning"},{"title":"ICLR 2026 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/iclr-paper-list/iclr-2026-paper-list/"},{"title":"Accepted Papers | ICLR 2026 Workshop RSI","url":"https://recursive-workshop.github.io/papers.html"},{"title":"ICLR 2026 Conference | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FConference"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"ICLR 2026 Schedule","url":"https://iclr.cc/virtual/2026/calendar"},{"title":"ICLR 2026","url":"https://iclr.cc/"}]

Based on the search results, I found relevant information about your query. Here are the key findings:

ROMA is a bootstrap→rewrite framework that formalizes decision pivots and shows that correct reasoning concentrates on a compact pivot set, aggregates K reasoning paths and uses a fine-tuned verifier to distill compact, pivot-consistent short-path reasoning.

The approach draws K diverse chain-of-thought (CoT) reasoning paths for each input sample by bootstrapping the pivots shared by successful reasoning paths, then merges multiple reasoning paths into short-path reasoning (SPR) that focuses on the pivots and removes redundant steps.

ROMA includes a self-training pipeline that leverages the short-path data (e.g., with DPO) to improve both task accuracy and explanation quality across benchmarks like LogiQA, MedQA, and MATH500.

Regarding cross-path verification, combining the pivot score with ROSCOE (a general CoT quality metric) delivers the best results across all three benchmarks, indicating that verifiability via decision pivots is complementary to general CoT quality metrics and leads to more effective data curation.

The paper "Correct Reasoning Paths Visit Shared Decision Pivots" was accepted as paper #31 at the ICLR 2026 Workshop RSI.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8fe25d8c-a9bc-4f43-b703-7fc95f777460",
  "isSidechain": false,
  "promptId": "d9295023-136d-4eec-b865-315f1454c5eb",
  "type": "user",
  "uuid": "ca605506-1097-4533-afdc-19aac1651bcd",
  "toolUseResult": {
    "query": "ROMA \"decision pivots\" reasoning paths ICLR 2026 cross-path verification",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QBCTBFqi1KVZgGpyHQvcA4",
        "content": [
          {
            "title": "Correct Reasoning Paths Visit Shared Decision Pivots Dongkyu Cho1∗,",
            "url": "https://arxiv.org/pdf/2509.21549"
          },
          {
            "title": "ICLR 2026 Papers",
            "url": "https://iclr.cc/virtual/2026/papers.html"
          },
          {
            "title": "ICLR 2026 Statistics - Paper Copilot",
            "url": "https://papercopilot.com/statistics/iclr-statistics/iclr-2026-statistics/"
          },
          {
            "title": "ICLR 2026 Workshop LLM Reasoning | OpenReview",
            "url": "https://openreview.net/group?id=ICLR.cc%2F2026%2FWorkshop%2FLLM_Reasoning"
          },
          {
            "title": "ICLR 2026 Accepted Paper List - Paper Copilot",
            "url": "https://papercopilot.com/paper-list/iclr-paper-list/iclr-2026-paper-list/"
          },
          {
            "title": "Accepted Papers | ICLR 2026 Workshop RSI",
            "url": "https://recursive-workshop.github.io/papers.html"
          },
          {
            "title": "ICLR 2026 Conference | OpenReview",
            "url": "https://openreview.net/group?id=ICLR.cc%2F2026%2FConference"
          },
          {
            "title": "ICLR 2026 Call for Papers",
            "url": "https://iclr.cc/Conferences/2026/CallForPapers"
          },
          {
            "title": "ICLR 2026 Schedule",
            "url": "https://iclr.cc/virtual/2026/calendar"
          },
          {
            "title": "ICLR 2026",
            "url": "https://iclr.cc/"
          }
        ]
      },
      "Based on the search results, I found relevant information about your query. Here are the key findings:\n\nROMA is a bootstrap→rewrite framework that formalizes decision pivots and shows that correct reasoning concentrates on a compact pivot set, aggregates K reasoning paths and uses a fine-tuned verifier to distill compact, pivot-consistent short-path reasoning.\n\nThe approach draws K diverse chain-of-thought (CoT) reasoning paths for each input sample by bootstrapping the pivots shared by successful reasoning paths, then merges multiple reasoning paths into short-path reasoning (SPR) that focuses on the pivots and removes redundant steps.\n\nROMA includes a self-training pipeline that leverages the short-path data (e.g., with DPO) to improve both task accuracy and explanation quality across benchmarks like LogiQA, MedQA, and MATH500.\n\nRegarding cross-path verification, combining the pivot score with ROSCOE (a general CoT quality metric) delivers the best results across all three benchmarks, indicating that verifiability via decision pivots is complementary to general CoT quality metrics and leads to more effective data curation.\n\nThe paper \"Correct Reasoning Paths Visit Shared Decision Pivots\" was accepted as paper #31 at the ICLR 2026 Workshop RSI."
    ],
    "durationSeconds": 7.253023172000001
  },
  "sourceToolAssistantUUID": "8fe25d8c-a9bc-4f43-b703-7fc95f777460",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 20 · 2026-05-12T00:13:11.562Z_

<details><summary>Logged reasoning block</summary>

```text
Good. Now let me get the ARR dates more specifically, and also check the EMNLP 2026 commitment deadline for prior ARR cycle submissions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca605506-1097-4533-afdc-19aac1651bcd",
  "isSidechain": false,
  "requestId": "req_011Cawi2FBox17mHWc35R5fY",
  "type": "assistant",
  "uuid": "bb2b16b2-8558-4210-855b-187c7a05ef94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLoNsW9scoYwXLeCRSTV4r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2185,
      "cache_read_input_tokens": 29763,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2185,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 241,
          "cache_read_input_tokens": 29763,
          "cache_creation_input_tokens": 2185,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2185
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-12T00:13:12.530Z_

Let me get the exact ARR dates and verify the EMNLP 2026 commitment timeline.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb2b16b2-8558-4210-855b-187c7a05ef94",
  "isSidechain": false,
  "requestId": "req_011Cawi2FBox17mHWc35R5fY",
  "type": "assistant",
  "uuid": "11712a36-eacf-448b-a226-19cad6e7c3cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLoNsW9scoYwXLeCRSTV4r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2185,
      "cache_read_input_tokens": 29763,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2185,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 241,
          "cache_read_input_tokens": 29763,
          "cache_creation_input_tokens": 2185,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2185
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-12T00:13:14.523Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_012tzFCaiouJDv4QcdUFyCQA`</summary>

```json
{
  "url": "https://aclrollingreview.org/dates",
  "prompt": "List all ARR submission deadlines in 2026, especially May and June cycles. What are the exact dates? Also note any information about review cycle length and when reviews are returned."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11712a36-eacf-448b-a226-19cad6e7c3cf",
  "isSidechain": false,
  "requestId": "req_011Cawi2FBox17mHWc35R5fY",
  "type": "assistant",
  "uuid": "29ceb21b-d032-439b-abb6-d2b39a512e41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLoNsW9scoYwXLeCRSTV4r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2185,
      "cache_read_input_tokens": 29763,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2185,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 241,
          "cache_read_input_tokens": 29763,
          "cache_creation_input_tokens": 2185,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2185
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-12T00:13:14.703Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019QDUUKzcFr4fhsYorUKLJ4`</summary>

```json
{
  "query": "EMNLP 2026 commitment deadline ARR cycle papers accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29ceb21b-d032-439b-abb6-d2b39a512e41",
  "isSidechain": false,
  "requestId": "req_011Cawi2FBox17mHWc35R5fY",
  "type": "assistant",
  "uuid": "a6c27af9-6c2f-4a51-a813-44a347e75326",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLoNsW9scoYwXLeCRSTV4r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2185,
      "cache_read_input_tokens": 29763,
      "output_tokens": 241,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2185,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 241,
          "cache_read_input_tokens": 29763,
          "cache_creation_input_tokens": 2185,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2185
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"Formally-Verified Intermediate Constraint Consensus Across Reasoning P…",
  "leafUuid": "a6c27af9-6c2f-4a51-a813-44a347e75326",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise SICA feasibility with realistic timeline and minimum viable scope",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3"
}
```

---

### Tool result

_source line 26 · 2026-05-12T00:13:18.324Z_

<details><summary>↩ Tool result · `toolu_012tzFCaiouJDv4QcdUFyCQA`</summary>

```text
# ARR 2026 Submission Deadlines

Based on the page content, here are the 2026 ARR submission deadlines:

## Key Dates

**May 2026 Cycle:**
- Submission deadline: May 25, 2026
- Reviews due: June 29, 2026
- Author response period: July 7-13, 2026
- Meta-reviews released: July 30, 2026

**March 2026 Cycle:**
- Submission deadline: March 16, 2026
- Reviews due: April 20, 2026
- Author response period: April 28-May 4, 2026

## Review Cycle Length

The platform transitioned to a new schedule in May 2025: "instead of 6 cycles a year there will generally be 5, but with more reasonable timelines for the review tasks." The new format uses 10-week cycles rather than the previous 8-week cycles.

## Venue Commitment Dates

Papers can be committed to participating venues on these dates:
- **EMNLP 2026**: August 2, 2026
- **AACL 2026**: August 26, 2026
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "29ceb21b-d032-439b-abb6-d2b39a512e41",
  "isSidechain": false,
  "promptId": "d9295023-136d-4eec-b865-315f1454c5eb",
  "type": "user",
  "uuid": "edef0cd0-16c5-4e09-95f1-4f59bbd17b44",
  "toolUseResult": {
    "bytes": 25438,
    "code": 200,
    "codeText": "OK",
    "result": "# ARR 2026 Submission Deadlines\n\nBased on the page content, here are the 2026 ARR submission deadlines:\n\n## Key Dates\n\n**May 2026 Cycle:**\n- Submission deadline: May 25, 2026\n- Reviews due: June 29, 2026\n- Author response period: July 7-13, 2026\n- Meta-reviews released: July 30, 2026\n\n**March 2026 Cycle:**\n- Submission deadline: March 16, 2026\n- Reviews due: April 20, 2026\n- Author response period: April 28-May 4, 2026\n\n## Review Cycle Length\n\nThe platform transitioned to a new schedule in May 2025: \"instead of 6 cycles a year there will generally be 5, but with more reasonable timelines for the review tasks.\" The new format uses 10-week cycles rather than the previous 8-week cycles.\n\n## Venue Commitment Dates\n\nPapers can be committed to participating venues on these dates:\n- **EMNLP 2026**: August 2, 2026\n- **AACL 2026**: August 26, 2026",
    "durationMs": 3797,
    "url": "https://aclrollingreview.org/dates"
  },
  "sourceToolAssistantUUID": "29ceb21b-d032-439b-abb6-d2b39a512e41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-12T00:13:21.087Z_

<details><summary>↩ Tool result · `toolu_019QDUUKzcFr4fhsYorUKLJ4`</summary>

```text
Web search results for query: "EMNLP 2026 commitment deadline ARR cycle papers accepted"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Dates and Venues","url":"http://aclrollingreview.org/dates"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"},{"title":"EMNLP 2026 (@emnlpmeeting) / Posts / X","url":"https://x.com/emnlpmeeting?lang=en"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"}]

Based on the search results, here is the information about EMNLP 2026 commitment deadline and ARR cycle for papers:

## Key Deadlines for EMNLP 2026

The ARR submission deadline for long and short papers is May 25, 2026, and the EMNLP commitment deadline is August 2, 2026.

## Paper Submission Requirements

Papers must be submitted at latest by the ARR 2026 May cycle, and papers that have received reviews and a meta-review from ARR may be committed to EMNLP via the commitment link.

## Additional Important Dates

The reviewer registration deadline for all authors is May 27, 2026, author response and author-reviewer discussion occurs July 7-13, 2026, and meta-review is released July 30, 2026. Acceptance notifications are provided on August 20, 2026, and camera-ready papers are due September 20, 2026.

## Special Policy for ARR May 2026 Cycle

For the ARR 2026 May cycle specifically, authors must explicitly declare which conference they intend to commit to at submission time, and this choice is binding for EMNLP 2026. However, this policy does not apply to papers submitted and reviewed in prior ARR cycles that wish to commit to EMNLP.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a6c27af9-6c2f-4a51-a813-44a347e75326",
  "isSidechain": false,
  "promptId": "d9295023-136d-4eec-b865-315f1454c5eb",
  "type": "user",
  "uuid": "7a50bbc2-53e3-4ea5-b4db-afc0060845a2",
  "toolUseResult": {
    "query": "EMNLP 2026 commitment deadline ARR cycle papers accepted",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WHk46WK5REVRj6w1CqbHeE",
        "content": [
          {
            "title": "Call for Main Conference Papers - EMNLP 2026",
            "url": "https://2026.emnlp.org/calls/main_conference_papers/"
          },
          {
            "title": "Dates and Venues",
            "url": "http://aclrollingreview.org/dates"
          },
          {
            "title": "LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)",
            "url": "https://linguistlist.org/issues/37/972/"
          },
          {
            "title": "Call for Main Conference Papers -",
            "url": "https://2026.eacl.org/calls/papers/"
          },
          {
            "title": "CALL FOR PAPERS – ACL Rolling Review",
            "url": "http://aclrollingreview.org/cfp"
          },
          {
            "title": "EMNLP 2026 : The 2026 Conference on Empirical Methods in N",
            "url": "https://callforpaper.org/call-for-papers-emnlp-2026"
          },
          {
            "title": "EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X",
            "url": "https://x.com/emnlpmeeting/status/2029508292637061462"
          },
          {
            "title": "EMNLP 2026 (@emnlpmeeting) / Posts / X",
            "url": "https://x.com/emnlpmeeting?lang=en"
          },
          {
            "title": "AI Conference Deadlines",
            "url": "https://mlciv.com/ai-deadlines/"
          },
          {
            "title": "Workshop on Multimodal Interaction in Face-to-Face Dialogue (MINT @ EMNLP 2026) | ACL Member Portal",
            "url": "https://www.aclweb.org/portal/content/workshop-multimodal-interaction-face-face-dialogue-mint-emnlp-2026"
          }
        ]
      },
      "Based on the search results, here is the information about EMNLP 2026 commitment deadline and ARR cycle for papers:\n\n## Key Deadlines for EMNLP 2026\n\nThe ARR submission deadline for long and short papers is May 25, 2026, and the EMNLP commitment deadline is August 2, 2026.\n\n## Paper Submission Requirements\n\nPapers must be submitted at latest by the ARR 2026 May cycle, and papers that have received reviews and a meta-review from ARR may be committed to EMNLP via the commitment link.\n\n## Additional Important Dates\n\nThe reviewer registration deadline for all authors is May 27, 2026, author response and author-reviewer discussion occurs July 7-13, 2026, and meta-review is released July 30, 2026. Acceptance notifications are provided on August 20, 2026, and camera-ready papers are due September 20, 2026.\n\n## Special Policy for ARR May 2026 Cycle\n\nFor the ARR 2026 May cycle specifically, authors must explicitly declare which conference they intend to commit to at submission time, and this choice is binding for EMNLP 2026. However, this policy does not apply to papers submitted and reviewed in prior ARR cycles that wish to commit to EMNLP."
    ],
    "durationSeconds": 6.38071514
  },
  "sourceToolAssistantUUID": "a6c27af9-6c2f-4a51-a813-44a347e75326",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-12T00:14:23.608Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the key information:

1. **ARR May 2026 deadline**: May 25, 2026 (confirmed). Today is May 11, 2026 — so that's 14 days.
2. **EMNLP 2026 commitment deadline**: August 2, 2026
3. **ARR June 2026 cycle**: The ARR page doesn't mention a June cycle — they moved to 10-week cycles (5 cycles per year), so the next cycle after May 25 would likely be around July/August. Let me check if there's a June/July cycle.


4. **ROMA paper**: "Correct Reasoning Paths Visit Shared Decision Pivots" — NeurIPS 2025 Workshop FoRLM, also accepted at ICLR 2026 Workshop RSI. arXiv 2509.21549. It mines shared decision pivots across reasoning paths using a learned verifier. Since there are only 5 cycles per year with 10-week intervals, the next ARR cycle after May 25 would fall around late July or early August.

The reviewer's suggestion to submit to a June ARR cycle is actually incorrect — there is no June cycle. This matters because if we miss the May 25 deadline, we lose the opportunity to submit to EMNLP 2026, since that's the last eligible cycle for that venue's commitment deadline.

With just 14 days until May 25, this is tight but doable if we run everything in full auto mode. For the minimum viable scope, I'm thinking 5 benchmarks: MATH-500, ProofWriter, AIME 2024, FOLIO as a negative diagnostic, and AIME 2025 (which adds trivially to the AIME pipeline). We can drop BBH subtasks if needed to save time. I should also consider whether a July/August ARR cycle could serve as a fallback for AAAI 2027 instead.

Let me map out a realistic day-by-day timeline starting from today (May 11) through the May 25 deadline.

The first three days focus on building the core infrastructure: developing the extraction prompt for parsing QwQ-32B traces, setting up the solver routing system with Z3 and SymPy, implementing a MAX-SAT wrapper, and establishing quality checks through syntactic validation and spot-checking. Then over the next four days, I'll run experiments across the benchmarks—MATH and AIME variants on day 4 using the same extraction pipeline, ProofWriter on day 5 for logical reasoning, FOLIO and any remaining subtasks on day 6, and ablations on day 7.

For the analysis phase, I'm planning to measure extraction quality and run a K sweep while tracking contradiction frequency. Days 8-10 will focus on the core analysis work—examining contradiction patterns, annotating extraction quality, generating figures and tables, and correlating extraction errors. Then I need to write the paper in three days: introduction and methods on day 11, experiments and results on day 12, and polishing on day 13, with day 14 as a buffer before submission.

I'm acknowledging that three days for paper writing is tight, though technically feasible for a focused submission. But the reviewer's point about considering the June ARR cycle if the timeline doesn't work is worth taking seriously.

Actually, there's no June ARR cycle—the next one would be August, which is too late for EMNLP 2026. So I'm really choosing between submitting to ARR on May 25 with a compressed timeline, or aiming for AAAI 2027 with an August deadline instead. I should present both paths honestly.

For a minimum viable scope that still demonstrates the core contribution, I'd focus on MATH-500, ProofWriter, AIME 2024, and AIME 2025 as my main benchmarks—using the same extraction pipeline for the AIME pair—plus FOLIO as a negative diagnostic case. That's five benchmarks at K=12, dropping the BBH subtasks. This is still sufficient to show the work's value.

Now I need to revise the proposal with a few key updates: add a detailed day-by-day timeline in the approach section, spell out the minimum viable scope as a fallback plan, move AIME 2025 up to Track A, and properly cite ROMA in the landscape and references. I should also verify the citation details for that arXiv paper—it was presented at NeurIPS 2025 Workshop FoRLM and ICLR 2026 Workshop RSI, not just ICLR 2026 under review. Since these are mostly structural additions and clarifications rather than major changes, I'll treat this as a minor revision to the JSON.

For the timeline, I'm working with 14 days from May 11 to May 25 for the ARR deadline, which aligns with what's already noted in the proposal. Let me make sure the day-by-day breakdown is realistic and accounts for the tight schedule.

I should also confirm that May 25 is indeed the final ARR cycle eligible for EMNLP 2026, which the search results confirm—so there's no buffer for a later submission window.

Now I'll draft the specific revisions, starting with the approach section to add the timeline and minimum viable scope, then update the landscape section with ROMA, and adjust the resource estimate to reflect AIME 2025 in Track A. So I'm laying out the specific changes needed across each section of the JSON—the core intellectual content stays the same, but I need to be precise about the benchmarks, timeline, and venue strategy. I should verify the AAAI 2027 deadline before finalizing everything.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a50bbc2-53e3-4ea5-b4db-afc0060845a2",
  "isSidechain": false,
  "requestId": "req_011Cawi3ABhpGtEDH9dcTTsh",
  "type": "assistant",
  "uuid": "c0e8f426-abed-4b10-801d-bcff61330b38",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQPjHjrJfmGedQXe6y9eif",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1452,
      "cache_read_input_tokens": 31948,
      "output_tokens": 2573,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1452,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2573,
          "cache_read_input_tokens": 31948,
          "cache_creation_input_tokens": 1452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1452
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-12T00:14:23.619Z_

Now let me verify AAAI 2027 dates and check if there's a next ARR cycle that could still reach EMNLP 2026.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0e8f426-abed-4b10-801d-bcff61330b38",
  "isSidechain": false,
  "requestId": "req_011Cawi3ABhpGtEDH9dcTTsh",
  "type": "assistant",
  "uuid": "5fc8f989-4e26-4e8c-b4ac-fd24515d71cd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQPjHjrJfmGedQXe6y9eif",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1452,
      "cache_read_input_tokens": 31948,
      "output_tokens": 2573,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1452,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2573,
          "cache_read_input_tokens": 31948,
          "cache_creation_input_tokens": 1452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1452
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-12T00:14:23.622Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015KGfJpvySPmKbNMDME7gbX`</summary>

```json
{
  "query": "AAAI 2027 paper submission deadline abstract deadline"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fc8f989-4e26-4e8c-b4ac-fd24515d71cd",
  "isSidechain": false,
  "requestId": "req_011Cawi3ABhpGtEDH9dcTTsh",
  "type": "assistant",
  "uuid": "dd9c639b-4141-4fab-9ba2-232ee3194b4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQPjHjrJfmGedQXe6y9eif",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1452,
      "cache_read_input_tokens": 31948,
      "output_tokens": 2573,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1452,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2573,
          "cache_read_input_tokens": 31948,
          "cache_creation_input_tokens": 1452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1452
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-12T00:14:25.044Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016i4ueJrCXTr7NGNPk5kqSu`</summary>

```json
{
  "url": "https://2026.emnlp.org/calls/main_conference_papers/",
  "prompt": "What are the key dates for EMNLP 2026? Especially: which ARR cycles are eligible for commitment? Is May 2026 the last eligible cycle? What is the commitment deadline? When is the conference?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd9c639b-4141-4fab-9ba2-232ee3194b4f",
  "isSidechain": false,
  "requestId": "req_011Cawi3ABhpGtEDH9dcTTsh",
  "type": "assistant",
  "uuid": "32262f42-0f29-44e3-ada8-4055d07316df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QQPjHjrJfmGedQXe6y9eif",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1452,
      "cache_read_input_tokens": 31948,
      "output_tokens": 2573,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1452,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2573,
          "cache_read_input_tokens": 31948,
          "cache_creation_input_tokens": 1452,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1452
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-12T00:14:27.191Z_

<details><summary>↩ Tool result · `toolu_015KGfJpvySPmKbNMDME7gbX`</summary>

```text
Web search results for query: "AAAI 2027 paper submission deadline abstract deadline"

Links: [{"title":"AAAI-26 Submission Instructions - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/submission-instructions/"},{"title":"AI & ML Conference Deadlines 2026–2027","url":"https://trybibby.com/conference-deadlines"},{"title":"AAAI 2027 Conference Deadline | Live Countdown Tracker","url":"https://www.getpaperpilot.com/deadlines/aaai-2027.html"},{"title":"Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540","url":"https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"},{"title":"🚨AAAI-26 Call for Papers🚨 AAAI-26 will in Singapore from ...","url":"https://www.facebook.com/AAAIOrg/posts/aaai-26-call-for-papersaaai-26-will-in-singapore-from-january-20-to-january-27-2/751564707547430/"},{"title":"The 40th Annual AAAI Conference on Artificial Intelligence","url":"https://aaai.org/conference/aaai/aaai-26/"},{"title":"AI/ML Conference Timeline | NIU AI","url":"https://www.niuai.org/resources/conference-timeline/"},{"title":"AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=3"},{"title":"MPC Deadlines Hub","url":"https://mpc-deadlines.github.io/"},{"title":"AAAI-26 Review Process - AAAI","url":"https://aaai.org/conference/aaai/aaai-26/review-process/"}]

Based on the search results, here's what I found about AAAI 2027 submission deadlines:

The abstract deadline for AAAI 2027 is July 25, and the full paper deadline is August 1, 2026. The conference will be held February 16-23, 2027 in Montreal, Canada.

It's worth noting that some sources still show the paper submission deadline as TBD, though the MPC Deadlines Hub appears to have the most recent confirmed information showing the August 1, 2026 full paper deadline.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd9c639b-4141-4fab-9ba2-232ee3194b4f",
  "isSidechain": false,
  "promptId": "d9295023-136d-4eec-b865-315f1454c5eb",
  "type": "user",
  "uuid": "87089c5c-26b3-4f12-94f7-b7b8f2b9d97f",
  "toolUseResult": {
    "query": "AAAI 2027 paper submission deadline abstract deadline",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TQA4YgJtDussH8azid9rML",
        "content": [
          {
            "title": "AAAI-26 Submission Instructions - AAAI",
            "url": "https://aaai.org/conference/aaai/aaai-26/submission-instructions/"
          },
          {
            "title": "AI & ML Conference Deadlines 2026–2027",
            "url": "https://trybibby.com/conference-deadlines"
          },
          {
            "title": "AAAI 2027 Conference Deadline | Live Countdown Tracker",
            "url": "https://www.getpaperpilot.com/deadlines/aaai-2027.html"
          },
          {
            "title": "Update aaai conference deadlines · huggingface/ai-deadlines at 8e14540",
            "url": "https://huggingface.co/spaces/huggingface/ai-deadlines/commit/8e145403081be22360311ec9ad9565e14b1f2d32"
          },
          {
            "title": "🚨AAAI-26 Call for Papers🚨 AAAI-26 will in Singapore from ...",
            "url": "https://www.facebook.com/AAAIOrg/posts/aaai-26-call-for-papersaaai-26-will-in-singapore-from-january-20-to-january-27-2/751564707547430/"
          },
          {
            "title": "The 40th Annual AAAI Conference on Artificial Intelligence",
            "url": "https://aaai.org/conference/aaai/aaai-26/"
          },
          {
            "title": "AI/ML Conference Timeline | NIU AI",
            "url": "https://www.niuai.org/resources/conference-timeline/"
          },
          {
            "title": "AAAI: National Conference on Artificial Intelligence 2027 2026 2025 ...",
            "url": "http://www.wikicfp.com/cfp/program?id=3"
          },
          {
            "title": "MPC Deadlines Hub",
            "url": "https://mpc-deadlines.github.io/"
          },
          {
            "title": "AAAI-26 Review Process - AAAI",
            "url": "https://aaai.org/conference/aaai/aaai-26/review-process/"
          }
        ]
      },
      "Based on the search results, here's what I found about AAAI 2027 submission deadlines:\n\nThe abstract deadline for AAAI 2027 is July 25, and the full paper deadline is August 1, 2026. The conference will be held February 16-23, 2027 in Montreal, Canada.\n\nIt's worth noting that some sources still show the paper submission deadline as TBD, though the MPC Deadlines Hub appears to have the most recent confirmed information showing the August 1, 2026 full paper deadline."
    ],
    "durationSeconds": 3.5635629390000103
  },
  "sourceToolAssistantUUID": "dd9c639b-4141-4fab-9ba2-232ee3194b4f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"Formally-Verified Intermediate Constraint Consensus Across Reasoning P…",
  "leafUuid": "87089c5c-26b3-4f12-94f7-b7b8f2b9d97f",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise SICA feasibility with realistic timeline and minimum viable scope",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3"
}
```

---

### Tool result

_source line 35 · 2026-05-12T00:14:29.524Z_

<details><summary>↩ Tool result · `toolu_016i4ueJrCXTr7NGNPk5kqSu`</summary>

```text
# EMNLP 2026 Key Dates and ARR Eligibility

## Important Deadlines

- **ARR submission deadline:** May 25, 2026
- **EMNLP commitment deadline:** August 2, 2026
- **Conference dates:** October 24-29, 2026

## ARR Cycle Eligibility

The document states: "Papers must be submitted, at latest, by the ARR 2026 May cycle." However, it also clarifies that papers from earlier ARR cycles remain eligible. Specifically: "Papers that have received reviews and a meta-review from ARR (whether from the ARR 2026 May cycle or an earlier ARR cycle) may be committed to EMNLP via the commitment link."

**Important caveat:** There is a special binding rule for the May 2026 cycle. Authors submitting to the ARR May 2026 cycle "will need to explicitly declare which conference they intend to commit to at submission time. This choice will be binding for EMNLP 2026." Papers that don't select EMNLP during submission cannot later commit to it. This restriction does not apply to papers from prior ARR cycles.

All deadlines follow "11:59PM UTC-12:00 ('anywhere on Earth')" timing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "32262f42-0f29-44e3-ada8-4055d07316df",
  "isSidechain": false,
  "promptId": "d9295023-136d-4eec-b865-315f1454c5eb",
  "type": "user",
  "uuid": "bd945ce8-fffe-4580-a42d-8337cef6acf1",
  "toolUseResult": {
    "bytes": 26681,
    "code": 200,
    "codeText": "OK",
    "result": "# EMNLP 2026 Key Dates and ARR Eligibility\n\n## Important Deadlines\n\n- **ARR submission deadline:** May 25, 2026\n- **EMNLP commitment deadline:** August 2, 2026\n- **Conference dates:** October 24-29, 2026\n\n## ARR Cycle Eligibility\n\nThe document states: \"Papers must be submitted, at latest, by the ARR 2026 May cycle.\" However, it also clarifies that papers from earlier ARR cycles remain eligible. Specifically: \"Papers that have received reviews and a meta-review from ARR (whether from the ARR 2026 May cycle or an earlier ARR cycle) may be committed to EMNLP via the commitment link.\"\n\n**Important caveat:** There is a special binding rule for the May 2026 cycle. Authors submitting to the ARR May 2026 cycle \"will need to explicitly declare which conference they intend to commit to at submission time. This choice will be binding for EMNLP 2026.\" Papers that don't select EMNLP during submission cannot later commit to it. This restriction does not apply to papers from prior ARR cycles.\n\nAll deadlines follow \"11:59PM UTC-12:00 ('anywhere on Earth')\" timing.",
    "durationMs": 4476,
    "url": "https://2026.emnlp.org/calls/main_conference_papers/"
  },
  "sourceToolAssistantUUID": "32262f42-0f29-44e3-ada8-4055d07316df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-12T00:14:29.528Z_

```json
{
  "parentUuid": "bd945ce8-fffe-4580-a42d-8337cef6acf1",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "d3a4af83-e5f1-4749-b247-5355a4bee142",
  "timestamp": "2026-05-12T00:14:29.528Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 37 · 2026-05-12T00:14:56.888Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me summarize:

1. **ROMA paper**: "Correct Reasoning Paths Visit Shared Decision Pivots" (arXiv 2509.21549, Sep 2025, NeurIPS 2025 Workshop FoRLM, also ICLR 2026 Workshop RSI). Mines shared decision pivots across K reasoning paths, uses learned verifier. Neural approach. Benchmarks: LogiQA, MedQA, MATH500.

2. **ARR dates**: 
   - May 25, 2026 is the LAST cycle eligible for EMNLP 2026
   - No June ARR cycle exists (10-week cycles mean roughly 5 per year), so the next opportunity after May would be late July/early August, which misses the August 2 EMNLP commitment deadline
   - EMNLP conference runs October 24-29, 2026

3. **AAAI 2027**: Abstract due July 25, paper due August 1, 2026. Conference February 16-23, 2027 in Montreal.

4. **The May 25 deadline is critical**: The reviewer's suggestion to try the June cycle doesn't work since no June cycle exists—it's either submit by May 25 or forfeit EMNLP 2026 eligibility entirely.

So I need to restructure the plan around this hard constraint. I'm going to build out a complete revised approach with a 14-day execution window from May 12-25, including a minimum viable scope fallback, moving AIME 2025 to Track A, adding ROMA to the landscape, and being explicit about the ARR timeline. Let me map out the daily breakdown: pipeline implementation over the first three days, core experiments batched across GPUs for days four through six, then ablations on days seven and eight.

For the minimum viable scope, if extraction becomes unreliable on BBH or the timeline starts slipping, I'll drop those three BBH subtasks and focus on five core benchmarks—MATH-500, AIME 2024, AIME 2025, ProofWriter, and FOLIO—which still cover the key demonstrations of cross-path MAX-SAT, contradiction frequency patterns, negative diagnostics, and generalization. If things slip further and paper writing becomes impossible by May 25, I'm targeting AAAI 2027 in August as the primary deadline instead of trying to force a June cycle.

Now I'm thinking through the full Track A and B evaluation, though there's no June ARR cycle to consider, so EMNLP 2026 is off the table. I need to be careful about the ROMA citation too—it's arXiv 2509.21549 from September 2025, and based on what I found, it was accepted at the ICLR 2026 Workshop on Recursive Self-Improvement, not just under review. Let me make sure I cite that correctly when I write out the full revision.

I'm planning to add a paragraph about ROMA after the self-consistency section, update Track A to include AIME 2025, add a day-by-day timeline and a minimum viable scope fallback section, and update the benchmark count and resource estimates accordingly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3a4af83-e5f1-4749-b247-5355a4bee142",
  "isSidechain": false,
  "requestId": "req_011Cawi8Co7RppiERiRwbDP8",
  "type": "assistant",
  "uuid": "f62a31da-c81f-4c80-8aa2-83214bd3be27",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WSFNqsZ1mf5fWCJZG5JaYT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3689,
      "cache_read_input_tokens": 33400,
      "output_tokens": 12274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3689,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12274,
          "cache_read_input_tokens": 33400,
          "cache_creation_input_tokens": 3689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3689
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-12T00:15:01.196Z_

Now I have all the information needed. Key findings:

- **ROMA**: "Correct Reasoning Paths Visit Shared Decision Pivots" (arXiv 2509.21549) — mines shared decision pivots across K reasoning paths using a learned verifier. Accepted at ICLR 2026 Workshop RSI. Neural approach, not formal — perfect conceptual counterpart to cite.
- **ARR timing**: May 25 is the **last** cycle eligible for EMNLP 2026. There is **no June ARR cycle** (10-week cycles = 5/year). The reviewer's fallback suggestion of "June ARR cycle" doesn't exist. It's either May 25 or we miss EMNLP 2026 entirely.
- **AAAI 2027**: Abstract July 25, paper August 1, 2026.

These are targeted feasibility and scope fixes on a validated idea — this is a **minor** revision. Let me construct the complete revised JSON.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f62a31da-c81f-4c80-8aa2-83214bd3be27",
  "isSidechain": false,
  "requestId": "req_011Cawi8Co7RppiERiRwbDP8",
  "type": "assistant",
  "uuid": "caf30943-3182-4706-98b0-af43e661d210",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WSFNqsZ1mf5fWCJZG5JaYT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3689,
      "cache_read_input_tokens": 33400,
      "output_tokens": 12274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3689,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12274,
          "cache_read_input_tokens": 33400,
          "cache_creation_input_tokens": 3689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3689
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-12T00:19:47.083Z_

<details open><summary>🔧 Tool call — Write · `toolu_01GRvfozo833qpjJdnmiWNQE`</summary>

```json
{
  "file_path": "/tmp/revised_idea.json",
  "content": "{\n  \"title\": \"Formally-Verified Intermediate Constraint Consensus Across Reasoning Paths\",\n  \"change_type\": \"minor\",\n  \"core_problem\": \"Recent work (CRAFT, PoLR, Draft-and-Prune) demonstrates that intermediate reasoning step consensus or pruning across candidate solutions provides stronger signals than answer-level majority voting. However, existing methods either rely on statistical similarity that cannot distinguish popular-but-contradictory constraints (CRAFT's TF-IRF/Jaccard), or prune individual paths based on internal consistency without cross-validating constraints across solutions (Draft-and-Prune's per-path |S|=0/|S|>1 checks). Meanwhile, single-output formal verification systems (MATH-VF, SAFE, FoVer, PRoSFI, VERGE) verify constraints within one solution or output but do not cross-validate across multiple reasoning paths, and cross-query consistency checking (arXiv 2604.14525) verifies coherence across different questions but not across multiple traces for the same question. Furthermore, 'Consensus is Not Verification' (arXiv 2603.06612) demonstrates that consensus-based aggregation fails for truthfulness because LLM errors are strongly correlated — but crucially, aggregation improves performance when a verifier exists. Can formally verifying cross-solution intermediate constraints via SMT solving and computer algebra yield more reliable consensus with interpretable provenance, and how frequently does statistical consensus actually retain contradictory constraints in practice?\",\n  \"opportunity\": \"CRAFT (arXiv 2604.14121, April 2026) builds a Reasoning Knowledge Graph from consensus intermediate steps using TF-IRF and Jaccard similarity, achieving significant accuracy improvements. However, CRAFT's authors explicitly acknowledge two key limitations: (1) 'consensus ≠ correctness' — frequently appearing steps can amplify shared errors, and (2) 'reduced effectiveness on symbolic math' due to lexical overlap bias in Jaccard similarity. This concern is empirically grounded by 'Consensus is Not Verification' (arXiv 2603.06612, March 2026), which demonstrates that LLM errors are strongly correlated across samples and even across model families — correlation persists even with random string conditioning — causing polling-style aggregation to yield no consistent accuracy gains over single-sample baselines. Critically, however, the paper finds that 'aggregation improves performance when a verifier exists, but it cannot serve as a verifier substitute,' directly motivating SICA's approach of introducing formal verification into the consensus process.\\n\\nDraft-and-Prune (D&P, arXiv 2603.17233, March 2026) addresses autoformalization brittleness by generating multiple natural-language plans, conditioning program generation on them, pruning individually contradictory or ambiguous formalizations (paths where the solver returns |S|=0 or |S|>1), and aggregating surviving paths via answer-level majority voting. D&P achieves strong results on logical reasoning benchmarks (AR-LSAT 78.43%, ProofWriter 98.33% with GPT-4), but its pruning operates independently on each path — it cannot detect cross-path contradictions where two individually valid paths assert mutually inconsistent constraints. D&P's authors explicitly note a limitation: 'We aggregate predictions at the answer level and do not cluster or de-duplicate candidates by symbolic equivalence.'\\n\\nA parallel line of work verifies individual solutions or outputs formally — MATH-VF (arXiv 2505.20869) uses CAS+Z3 for step-level verification on single solutions; SAFE (ACL 2025) uses Lean4 for retrospective step-aware verification; PRoSFI (arXiv 2603.29500) trains process rewards over structured formal intermediaries verified by Lean/Z3/Prover9, operating on individual 7B-model solutions. VERGE (arXiv 2601.20055, Jan 2026) is a single-output verify-and-refine framework that decomposes an LLM output into atomic claims, autoformalizes them, verifies joint satisfiability via Z3, and uses Minimal Correction Subsets (MCS) to provide targeted feedback for iterative refinement. VERGE's 'multi-model consensus' refers to K=3 candidate formalizations of a single claim checked for semantic equivalence — not cross-path reasoning aggregation. FoVer (arXiv 2505.15960, ACL 2026 Findings) uses Z3 and Isabelle for step-level error annotation in individual solutions for PRM training, demonstrating cross-task generalization to BBH subtasks (temporal sequences, tracking shuffled objects, word sorting). In the adjacent cross-output verification space, 'Quantifying Cross-Query Contradictions' (arXiv 2604.14525, April 2026) uses Z3 (QF_UFLIA) and CaDiCaL for cross-query consistency checking with unsat-core localization and counterexample-guided repair — but addresses cross-query consistency (different questions sharing a case file), not cross-trace consistency (same question, multiple reasoning paths). The EACL 2026 dynamic solver routing framework (arXiv 2510.06774) selects solvers at the problem level. But none of these methods formally cross-validate intermediate constraints across multiple candidate solutions for the same problem.\\n\\nThe gap: no method formally cross-validates intermediate constraints across multiple candidate solutions to produce a consistency-aware consensus signal with interpretable provenance. Concretely, SICA differs from D&P by extracting constraints from ALL paths and finding a globally consistent MAX-SAT-optimal subset (cross-path aggregation), rather than independently pruning paths with internal contradictions (per-path filtering). SICA differs from VERGE by applying MAX-SAT across multiple reasoning paths for answer selection, whereas VERGE applies the dual MCS operation within a single output for refinement feedback. SICA differs from the cross-query contradictions framework by operating on multiple traces for the same question (cross-trace scope) using weighted partial MAX-SAT for consensus, rather than on different questions in a case file (cross-query scope) using unsat-core repair. A key empirical question — how frequently does statistical consensus actually retain contradictory constraints? — remains unanswered and is central to quantifying this opportunity.\\n\\nRecent work on autoformalization faithfulness further motivates SICA's extraction quality pipeline: 'Do LLMs Game Formalization?' (arXiv 2604.19459, VerifAI-2 Workshop, ICLR 2026) shows that high compilation rates should not be equated with faithful reasoning, finding that two-stage formalization pipelines reveal distinct unfaithfulness patterns (axiom fabrication, premise mistranslation) that evade standard verification. This underscores the need for SICA's multi-tier extraction validation.\",\n  \"landscape\": \"Standard self-consistency (Wang et al., ICLR 2023) performs majority voting on final answers and shows diminishing returns on frontier models — gains plateau at <2% with accuracy sometimes declining at high sample counts (arXiv 2511.00751). 'Consensus is Not Verification' (arXiv 2603.06612, March 2026) provides a theoretical explanation: LLM errors are strongly correlated across samples and model families, causing consensus to reinforce shared misconceptions rather than converge on truth; however, the paper finds aggregation succeeds when an external verifier exists. CRAFT (arXiv 2604.14121, April 2026) extracts consensus intermediate steps via a Reasoning Knowledge Graph using TF-IRF/Jaccard similarity and topological generation, achieving up to +8.5% accuracy over SC baselines on GSM8K, FOLIO, FLD, and OlympiadBench with K=3 traces; its authors note 'consensus ≠ correctness' and 'reduced effectiveness on symbolic math' as limitations. PoLR (ICLR 2026) uses prefix consensus to prune reasoning paths, matching SC accuracy while reducing token usage by 50-60%.\\n\\nCross-path intermediate-step analysis with neural verification: 'Correct Reasoning Paths Visit Shared Decision Pivots' (ROMA, arXiv 2509.21549, NeurIPS 2025 Workshop FoRLM; ICLR 2026 Workshop RSI) hypothesizes that correct reasoning paths converge on shared 'decision pivots' — minimal, verifiable checkpoints that any correct path must visit. ROMA mines these pivots across K sampled reasoning paths and uses a learned verifier to distill pivot-focused short-path reasoning, evaluating on LogiQA, MedQA, and MATH-500. ROMA occupies the adjacent conceptual space of cross-path intermediate-step consensus but uses neural verification (a trained pivot verifier) rather than formal solvers. SICA provides formal satisfiability guarantees where ROMA uses learned signals, and operates on typed symbolic constraints rather than natural-language decision pivots — the approaches are complementary, with ROMA better suited to domains where formalization is intractable and SICA to domains with extractable logical structure.\\n\\nDraft-and-Prune (D&P, arXiv 2603.17233, March 2026): An inference-time framework that drafts multiple natural-language plans, conditions program generation on them, prunes executable but contradictory (|S|=0) or ambiguous (|S|>1) formalizations independently for each path, and aggregates surviving paths via answer-level majority voting. Uses Z3Py for AR-LSAT/LogicalDeduction and PyKe for ProofWriter/PrOntoQA. Achieves AR-LSAT 78.43%, ProofWriter 98.33%, PrOntoQA 99.32%, LogicalDeduction 99.50% (GPT-4). Key limitation: no cross-path constraint checking or equivalence-aware deduplication.\\n\\nVERGE (arXiv 2601.20055, Jan 2026): A single-output neurosymbolic verify-and-refine loop. Decomposes an LLM output into atomic claims, classifies them by type, autoformalizes into FOL, and verifies joint satisfiability via Z3. Uses semantic routing (symbolic solvers for logical claims, LLM ensembles for commonsense) and Minimal Correction Subsets (MCS) for precise error localization, providing actionable feedback for iterative refinement. VERGE's K=3 refers to candidate formalizations of a single claim checked for semantic equivalence, not multiple reasoning paths. MCS (minimum claims to remove for satisfiability) is dual to MAX-SAT (maximum satisfiable subset) but is applied within one output for feedback, not across paths for consensus. Evaluated on FOLIO (84.7-89.2%), ProofWriter (85.2-93.0%), AR-LSAT (88.6-91.7%) across GPT-OSS-20B, GPT-OSS-120B, and Claude 3.7 Sonnet.\\n\\nSingle-solution formal verification: MATH-VF (arXiv 2505.20869, May 2025) uses a Formalizer+Critic pipeline with CAS and Z3 SMT solver for step-level verification on individual solutions, evaluated on MATH-500 and ProcessBench. SAFE (ACL 2025, arXiv 2506.04592) uses Lean4 for retrospective step-aware formal verification of individual reasoning chains, introducing the FormalStep benchmark (30,809 formal statements). PRoSFI (arXiv 2603.29500, March 2026) — 'Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries' — trains process rewards over structured formal intermediaries verified by Lean tactics, Z3, and Prover9, operating on individual 7B-model solutions; achieves 92.97% accuracy / 76.07% GPT Soundness on ProverQA-Hard. FoVer (arXiv 2505.15960, ACL 2026 Findings) — 'Training Step-Level Reasoning Verifiers with Formal Verification Tools' — uses Z3 and Isabelle for step-level error annotation in individual solutions for PRM training; demonstrates cross-task generalization to BBH subtasks (temporal sequences 97.2%, tracking shuffled objects 96.0%, word sorting 46.8% with Llama3.1-8B-PRM at Best-of-7) and to MATH, AIME, ANLI, MMLU-Pro.\\n\\nCross-output consistency verification: 'Quantifying Cross-Query Contradictions in Multi-Query LLM Reasoning' (arXiv 2604.14525, April 2026) addresses cross-query consistency — maintaining a globally satisfiable belief state across interdependent queries sharing a case file. Uses Z3 v4.8.17 (QF_UFLIA theory) and CaDiCaL for SAT, with unsat-core localization and counterexample-guided lexicographic repair. Achieves SetCons improvement from 0.56 to 0.94 across 390 case files spanning relational/SAT, temporal/SMT, policy/rules, and abductive domains. Crucially, this operates at cross-query scope (different questions sharing context) rather than cross-trace scope (same question, multiple reasoning paths), and uses unsat-core repair rather than weighted partial MAX-SAT consensus. SICA's differentiators are: cross-trace scope, intermediate constraint extraction from reasoning steps, and popularity-weighted MAX-SAT for answer selection.\\n\\nSolver routing: The EACL 2026 dynamic solver composition framework (arXiv 2510.06774) automatically identifies formal reasoning strategies and routes to specialized solvers at the problem level, achieving 27% improvement over GPT-4o. SICA's theory-aware routing operates at the finer-grained assertion level.\\n\\nVeriCoT (Nov 2025) formalizes individual CoT traces into FOL for entailment checking without cross-solution comparison. FregeLogic (SemEval 2026) uses Z3 as a tiebreaker for syllogistic validity.\\n\\nAutoformalization reliability: Grammars of Formal Uncertainty (NeurIPS 2025) demonstrates that SMT autoformalization is task-dependent: +34.8% on ProofWriter but -44.5% on FOLIO, necessitating careful benchmark selection and per-domain extraction analysis. 'Do LLMs Game Formalization?' (arXiv 2604.19459, VerifAI-2 Workshop, ICLR 2026) evaluates faithfulness of LLM autoformalization on 303 FOL problems, finding that high compilation rates (87-99%) do not guarantee faithful reasoning — two-stage pipelines reveal distinct unfaithfulness patterns: axiom fabrication (GPT-5) and premise mistranslation (DeepSeek-R1). Autoformalization surveys (arXiv 2505.23486) report ~70% success rate on physics kinematics, with selective verification reducing errors by 14-100% with minimal abstention.\\n\\nNo concurrent work (searched arXiv and OpenReview through May 2026) formally cross-validates intermediate constraints across multiple candidate solutions for the same problem.\",\n  \"approach\": \"We propose Symbolic Invariant Consensus Aggregation (SICA): given a problem, sample K reasoning paths from a frontier open-source reasoning model (QwQ-32B via vLLM on 1-2 A100s; Qwen3-32B as secondary model for ablation), then use a prompted LLM extractor to parse each trace into typed symbolic assertions (equations, inequalities, logical predicates). SICA introduces four key technical components:\\n\\n(1) **Theory-aware assertion-level solver routing**: Extracted assertions are classified by constraint type and routed to appropriate solvers — Z3 for tractable theories (linear arithmetic, propositional logic, uninterpreted functions, bitvectors) and SymPy for nonlinear polynomial arithmetic, algebraic equivalence, and modular arithmetic. Unlike the EACL 2026 framework (arXiv 2510.06774) which routes at the problem level, SICA routes at the assertion level, enabling mixed-theory problems where individual steps span different solver domains (common in competition math). Assertions that neither solver can handle receive numerical spot-checking as fallback, with unverifiable assertions flagged and excluded from the consensus set (rather than silently included).\\n\\n(2) **Weighted partial MAX-SAT for invariant consensus**: Rather than enumerating assertion subsets (exponential worst-case), SICA leverages Z3's built-in optimization context to solve weighted partial MAX-SAT directly. Each unique assertion (deduplicated via solver-verified equivalence) is weighted by its cross-solution frequency. The optimizer finds the largest jointly satisfiable subset of assertions, weighted by popularity — a single Z3 optimization call replaces exponential subset enumeration. Per-query timeout caps (10s) bound worst-case latency. This cross-path MAX-SAT consensus is the key differentiator from Draft-and-Prune (D&P), which prunes paths independently based on internal consistency (|S|=0 or |S|>1) and aggregates surviving answers via majority voting without cross-path constraint checking. It is also distinct from VERGE's MCS, which is the dual operation (minimum claims to remove) applied within a single output for refinement feedback rather than across paths for answer selection. It further differs from the cross-query contradictions framework (arXiv 2604.14525), which uses unsat-core localization and counterexample-guided repair across different questions sharing a case file — SICA uses weighted partial MAX-SAT across different reasoning traces for the same question.\\n\\n(3) **Invariant-backed answer scoring**: Each candidate answer is scored by the coverage and weight of its supporting assertions within the MAX-SAT-optimal consistent set, yielding a continuous invariant consensus score. This captures partial structural agreement even when final answers diverge, and provides interpretable provenance (each score is backed by a specific set of formally verified constraints).\\n\\n(4) **Extraction quality assurance pipeline**: To address the documented task-dependence of autoformalization (Grammars of Formal Uncertainty, NeurIPS 2025) and the unfaithfulness risks identified by 'Do LLMs Game Formalization?' (arXiv 2604.19459), we implement a three-tier extraction quality pipeline: (a) syntactic validation — each extracted assertion must parse in the target solver's input language; (b) semantic spot-checking — a random 20% of assertions are checked against the original natural language step via an LLM judge for semantic fidelity, specifically targeting the axiom fabrication and premise mistranslation failure modes identified in the faithfulness literature; (c) coverage tracking — we report 'verifiable assertion coverage' (% of extracted assertions that successfully enter the MAX-SAT pipeline) per benchmark as a first-class metric. Extraction failures cascade to numerical fallback or abstention, preventing malformed inputs from corrupting the consensus signal.\\n\\n**Limitations of formal cross-validation**: SICA's MAX-SAT consensus catches contradictory constraints but cannot detect universally-wrong-but-mutually-consistent constraints caused by correlated extraction errors. 'Consensus is Not Verification' (arXiv 2603.06612) demonstrates that LLM errors are strongly correlated across samples and even across model families, which implies that if all K paths produce the same wrong formalization of a constraint, MAX-SAT will see K consistent-but-wrong assertions and cannot flag the error. This is a fundamental limitation of any approach combining LLM extraction with formal verification: the verifier guarantees consistency, not correctness of the extraction. SICA's semantic spot-checking tier partially mitigates this — by sampling 20% of assertions for LLM-judge semantic fidelity checks, it can catch systematic mistranslation patterns. However, if the extraction LLM and the judge LLM share the same correlated bias (as the correlated errors literature suggests is likely), the mitigation is incomplete. We acknowledge this limitation explicitly and note two potential future mitigations: (a) using structurally diverse extractor models (e.g., symbolic parsers alongside LLM extractors) to decorrelate extraction errors, and (b) grounding extracted constraints against external knowledge sources (CAS simplification, unit-test-style numerical spot-checking) that do not share LLM inductive biases. We include FOLIO as a diagnostic ablation where SMT autoformalization is documented to hurt (-44.5%), precisely to empirically characterize the boundary between domains where SICA's extraction is faithful enough to help versus where correlated errors dominate.\\n\\n**Day-by-day Track A timeline (14-day sprint, May 12-25)**:\\n\\n- *Days 1-3 (May 12-14): Pipeline implementation.* Day 1: extraction prompt development for math domains (MATH-500, AIME) and logical domains (ProofWriter, FOLIO) — two prompt templates covering all benchmarks. Day 2: solver routing infrastructure (Z3 + SymPy dispatch, MAX-SAT wrapper using Z3's optimization context, equivalence deduplication). Day 3: end-to-end pipeline integration and smoke testing on 50 problems from MATH-500.\\n- *Days 4-6 (May 15-17): Core experiments.* Day 4: MATH-500 (K=12) + AIME 2024 (K=12) + AIME 2025 (K=12) — all share the math extraction prompt; batched vLLM inference across 2 A100s. Day 5: ProofWriter (K=12) — direct D&P/VERGE comparison benchmark. Day 6: FOLIO (K=12, negative diagnostic) + begin BBH subtasks if pipeline stable.\\n- *Days 7-8 (May 18-19): Ablations and additional experiments.* Day 7: BBH subtasks (3 configs × K=12) if extraction quality validates; otherwise, begin ablation suite (K sweep, extraction noise injection). Day 8: Contradiction frequency analysis (centerpiece experiment) across all completed benchmarks; correlated extraction error measurement on 100 problems per benchmark.\\n- *Days 9-10 (May 20-21): Analysis and figures.* Compile results tables, generate accuracy/calibration figures, write contradiction frequency analysis, produce extraction quality breakdown per benchmark. Compute-normalized comparison (tokens, wall-clock time).\\n- *Days 11-13 (May 22-24): Paper writing.* Day 11: Introduction, method description, related work. Day 12: Experiments, results, analysis sections. Day 13: Abstract, conclusion, formatting, supplementary material.\\n- *Day 14 (May 25): Final polish and submission.* Buffer day for last-minute fixes, ARR submission.\\n\\n**Honest assessment of timeline risk**: Paper writing in 3 days is aggressive but feasible for a focused 8-page submission with auto-generated figures and tables from Days 9-10. The main risk is pipeline debugging overrunning Days 1-3, which compresses experiment time. The minimum viable scope (below) mitigates this by defining a credible fallback that preserves 1-2 buffer days.\\n\\n**Note on ARR cycle fallback**: There is no June 2026 ARR cycle — ARR operates on 10-week cycles (~5 per year), and the May 25 cycle is the last eligible for EMNLP 2026 commitment (deadline: August 2, 2026). If the May 25 deadline is missed, the fallback is AAAI 2027 (paper deadline: August 1, 2026), which provides an additional 11 weeks and allows full Track A+B evaluation without time pressure.\\n\\n**Minimum viable scope (fallback if full plan proves too ambitious)**: If extraction quality is unreliable on BBH subtasks or timeline slips compress experiment time, the minimum credible submission is 5 benchmarks at K=12: MATH-500, AIME 2024, AIME 2025, ProofWriter, and FOLIO. This scope preserves all core contributions: (a) cross-path MAX-SAT consensus demonstrated on ProofWriter (D&P/VERGE comparison), (b) contradiction frequency analysis on math benchmarks (MATH-500, AIME 2024/2025), (c) negative diagnostic on FOLIO showing domain boundaries, (d) generalization test on unseen competition problems (AIME 2025 vs. AIME 2024), and (e) extraction quality analysis. BBH subtasks and the FoVer comparison would move to the AAAI 2027 extended version (Track B). This fallback saves ~1.5 days of experiment time (BBH extraction prompt development + 3 benchmark runs), creating headroom for pipeline debugging or additional paper writing time. Under this minimum scope, the timeline adjusts to: Days 1-3 implementation, Days 4-5 experiments (5 benchmarks), Days 6-7 ablations/analysis, Days 8-10 paper writing, Days 11-14 polish/buffer — a substantially more comfortable schedule.\\n\\n**Dual-track evaluation plan**:\\n\\n*Track A — EMNLP 2026 (ARR May 25, primary target, 14 days):* Scoped evaluation with K=12 traces on 6 core benchmarks plus 3 BBH subtasks (full scope) or 5 core benchmarks (minimum viable scope):\\n- **MATH-500** (algebraic/arithmetic reasoning; QwQ-32B ~90.6%)\\n- **AIME 2024** (competition math with mixed-theory constraints; QwQ-32B ~79.5%)\\n- **AIME 2025** (unseen competition problems; tests generalization using the identical evaluation pipeline as AIME 2024 — trivially low marginal cost since both share the same extraction prompt and solver routing)\\n- **ProofWriter** (formal logic; enables direct comparison with D&P 98.33% and VERGE 85.2-93.0%)\\n- **FOLIO** (first-order logic; diagnostic ablation — SMT autoformalization documented to hurt -44.5% here)\\n- **BBH** (3 subtasks: logical deduction, tracking shuffled objects, temporal sequences — enables direct comparison with FoVer's BBH evaluation at Best-of-7; tests cross-domain generalization to structured informal reasoning) *[included in full scope; deferred to Track B in minimum viable scope]*\\n\\nBaselines for Track A: self-consistency, CRAFT, D&P (on ProofWriter), VERGE (on ProofWriter/FOLIO).\\n\\n*Track B — AAAI 2027 (abstract deadline: July 25, paper deadline: August 1, 2026; extended version):* Expanded to K=16 traces on all Track A benchmarks plus:\\n- **GPQA Diamond** (graduate-level science; QwQ-32B ~65.2%; per-domain reporting for physics/chemistry vs. biology)\\n- **LogiQA 2.0** (natural language logical reasoning; 8,678 questions; tests constraint extraction beyond math/formal logic)\\n- BBH subtasks (if deferred from Track A) and full ablation suite\\n- Qwen3-32B cross-model ablation\\n\\n**ARC-Challenge exclusion justification**: ARC-Challenge (Clark et al., 2018) consists of multiple-choice grade-school science questions that primarily test factual knowledge retrieval (e.g., 'Which mineral is the hardest?', 'What happens when water freezes?'). Most questions lack the multi-step constraint structure required for meaningful symbolic assertion extraction — they involve domain knowledge rather than chains of extractable equations, inequalities, or logical predicates. Including ARC-Challenge would likely yield near-zero verifiable assertion coverage, providing no insight beyond confirming SICA's domain specificity (which FOLIO already demonstrates as a negative diagnostic). We note this scope limitation explicitly.\\n\\n**Metrics and analyses**:\\n- Primary: accuracy, calibration (ECE), informativeness of partial invariant agreement when candidates disagree\\n- **Contradiction frequency analysis** (centerpiece experiment): For each problem across all benchmarks, we measure how often CRAFT's statistical consensus retains logically contradictory constraint pairs. We report the 'contradiction rate' — the fraction of problems where at least one pair of popular constraints (appearing in ≥3 of K traces) are mutually unsatisfiable. If >15%, this validates SICA's core motivation; if <5%, we honestly acknowledge limited practical impact on this axis and emphasize interpretability/provenance instead.\\n- **D&P comparison**: On ProofWriter (shared benchmark), we compare SICA's cross-path MAX-SAT consensus against D&P's per-path pruning + answer-level voting, specifically measuring: (a) how many problems have cross-path contradictions that D&P's per-path pruning misses, and (b) whether MAX-SAT-backed scoring outperforms answer-level majority voting among surviving paths.\\n- **FoVer comparison on BBH** (full scope only): On the 3 shared BBH subtasks, we compare SICA's inference-time cross-path consensus against FoVer's training-time PRM approach (Llama3.1-8B-PRM at Best-of-7: temporal 97.2%, tracking 96.0%, word sorting 46.8%), analyzing whether cross-path formal consensus provides complementary signal to trained process reward models.\\n- **Extraction accuracy ablation**: Per-benchmark measurement of (a) syntactic parse rate, (b) semantic fidelity (manual annotation on 100 samples per benchmark), and (c) error propagation analysis — how X% extraction error degrades MAX-SAT consensus quality via controlled noise injection. Per the findings of 'Do LLMs Game Formalization?', we specifically track axiom fabrication and premise mistranslation rates.\\n- **Correlated extraction error analysis**: On a subset of problems (100 per benchmark), we measure cross-path extraction agreement — the fraction of assertions that are semantically equivalent across all K traces — to empirically quantify the degree of correlated extraction and assess how much independent signal SICA's MAX-SAT actually receives.\\n- **Compute-normalized comparison**: Report total tokens generated, wall-clock time per problem, and decomposed latency (inference, extraction, solver, MAX-SAT) for each method. Plot accuracy vs. total compute (tokens) curves. If SICA takes 5x compute of vanilla SC for +2% accuracy, we justify via interpretability/soundness or acknowledge the tradeoff.\\n\\nThe primary contribution is not raw accuracy improvement over SC (which has diminishing returns on frontier models) but rather: (a) formal soundness guarantees on the consensus signal, (b) interpretable constraint-level provenance for each answer, (c) detecting logically inconsistent popular reasoning steps that both statistical consensus (CRAFT) and per-path pruning (D&P) miss — with empirical quantification of how frequently this occurs, (d) systematic domain analysis of formal cross-solution verification including where it helps (ProofWriter, BBH logical deduction) vs. hurts (FOLIO), and (e) empirical characterization of correlated extraction errors as a fundamental limitation of LLM-based autoformalization in consensus settings.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~180-240h A100 80GB (6 benchmarks + 3 BBH subtasks × K=12 traces + extraction + ablations)\",\n      \"gpu_utilization\": \"Low (~20-30%); GPUs idle during coding, debugging solver routing, manual extraction annotation\",\n      \"timeline\": \"2-3 months\",\n      \"team\": \"1-2 researchers with formal methods and LLM experience\",\n      \"estimated_gpu_cost\": \"$235-310 (at ~$1.30/hr typical A100 spot rate)\",\n      \"h100_equivalent\": \"~90-120h H100 (well within 200h H100 budget)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~220-300h A100 80GB\",\n      \"gpu_utilization\": \"Moderate (~50-60%); agent codes and runs experiments between human review gates\",\n      \"timeline\": \"4-6 weeks (fits AAAI 2027 extended version with writing buffer)\",\n      \"team\": \"1 researcher, ~40-50min/day reviewing extraction quality, solver routing correctness, contradiction analysis, D&P comparison design, and BBH extraction quality; ~6h total for manual semantic fidelity annotation (100 samples × 6 benchmarks + 3 BBH subtasks)\",\n      \"claude_api_cost\": \"$200-400 (est. 2000-4000 Opus turns)\",\n      \"estimated_gpu_cost\": \"$285-390\",\n      \"h100_equivalent\": \"~110-150h H100 (within 200h H100 budget)\",\n      \"risk_note\": \"Solver routing heuristics require human judgment for edge cases; CRAFT replication may need prompt tuning; BBH logical deduction extraction quality needs validation\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~300-400h A100 80GB (Track A full scope: 6 benchmarks + 3 BBH subtasks × K=12 × core ablations; minimum viable scope: 5 benchmarks × K=12 saves ~40h)\",\n      \"gpu_utilization\": \"High (~85-95%); agent pipelines inference, extraction, and solving continuously; batched vLLM serving keeps GPUs saturated\",\n      \"timeline\": \"14-day sprint (May 12-25) for EMNLP 2026 ARR May 25; see day-by-day timeline in approach section. Minimum viable scope provides 1.5-day buffer by dropping BBH subtasks. If May 25 missed, fallback to AAAI 2027 (August 1) with full Track A+B evaluation over 11 additional weeks.\",\n      \"team\": \"0 (initial setup only, ~3 hours)\",\n      \"claude_api_cost\": \"$350-600 (est. 3500-6000 Opus turns)\",\n      \"estimated_gpu_cost\": \"$390-520\",\n      \"h100_equivalent\": \"~150-200h H100 (within 200h H100 budget with K=12; minimum viable scope ~120-160h H100)\",\n      \"speed_bottleneck\": \"GPU count for parallel vLLM inference across benchmarks × 12 samples; secondary bottleneck is Z3 MAX-SAT optimization time (mitigated by 10s per-query timeout)\",\n      \"risk_note\": \"Primary risk: pipeline debugging overruns Days 1-3, compressing experiment time — mitigated by minimum viable scope fallback (5 benchmarks, saves 1.5 days). Secondary risk: automated extraction may produce malformed solver input in ~10-20% of traces; without human review the agent may over-tune extraction prompts to specific benchmarks. AIME 2025 adds negligible marginal cost (identical pipeline to AIME 2024). No June ARR cycle exists — if May 25 missed, AAAI 2027 (August 1) is the fallback venue.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline: May 25, 2026 — 14 days from now; primary target with Track A scoped evaluation; last ARR cycle eligible for EMNLP 2026 commitment on August 2)\",\n    \"AAAI 2027 (abstract deadline: July 25, 2026; paper deadline: August 1, 2026 — extended version with Track B full evaluation; also serves as fallback if May 25 ARR deadline missed)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Self-Consistency Improves Chain of Thought Reasoning in Language Models (ICLR 2023)\",\n    \"CRAFT: Correct Prediction, Wrong Steps? Consensus Reasoning Knowledge Graph for Robust Chain-of-Thought Synthesis (arXiv 2604.14121, April 2026)\",\n    \"Draft-and-Prune: Improving the Reliability of Auto-formalization for Logical Reasoning (arXiv 2603.17233, March 2026)\",\n    \"PoLR: The Path of Least Resistance — Guiding LLM Reasoning Trajectories with Prefix Consensus (ICLR 2026)\",\n    \"VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (arXiv 2601.20055, Jan 2026)\",\n    \"VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks (arXiv 2025)\",\n    \"MATH-VF: Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving (arXiv 2505.20869, May 2025)\",\n    \"SAFE: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification (ACL 2025, arXiv 2506.04592)\",\n    \"Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition (EACL 2026, arXiv 2510.06774)\",\n    \"PRoSFI: Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries (arXiv 2603.29500, March 2026)\",\n    \"FoVer: Training Step-Level Reasoning Verifiers with Formal Verification Tools (arXiv 2505.15960, ACL 2026 Findings)\",\n    \"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks (NeurIPS 2025)\",\n    \"FregeLogic at SemEval 2026 Task 11: Hybrid Neuro-Symbolic Architecture for Syllogistic Validity (SemEval 2026)\",\n    \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (arXiv 2604.19459, VerifAI-2 Workshop, ICLR 2026)\",\n    \"Reevaluating Self-Consistency Scaling in Multi-Agent Systems (arXiv 2511.00751)\",\n    \"Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling (NAACL 2025)\",\n    \"Faithful Logical Reasoning via Symbolic Chain-of-Thought (ACL 2024)\",\n    \"Autoformalization in the Era of Large Language Models: A Survey (arXiv 2505.23486, May 2025)\",\n    \"Consensus is Not Verification: Why Crowd Wisdom Strategies Fail for LLM Truthfulness (arXiv 2603.06612, March 2026)\",\n    \"Quantifying Cross-Query Contradictions in Multi-Query LLM Reasoning (arXiv 2604.14525, April 2026)\",\n    \"Correct Reasoning Paths Visit Shared Decision Pivots (ROMA, arXiv 2509.21549, NeurIPS 2025 Workshop FoRLM; ICLR 2026 Workshop RSI)\"\n  ],\n  \"description\": \"We propose Symbolic Invariant Consensus Aggregation (SICA), a method that formally cross-validates intermediate constraints extracted from multiple LLM reasoning paths to produce a soundness-guaranteed consensus signal. While CRAFT (April 2026) demonstrates the value of intermediate-step consensus via statistical similarity (TF-IRF/Jaccard), its authors explicitly acknowledge 'consensus ≠ correctness' and 'reduced effectiveness on symbolic math.' This limitation is theoretically grounded by 'Consensus is Not Verification' (arXiv 2603.06612, March 2026), which proves that LLM errors are strongly correlated across samples and model families, causing pure consensus to fail — but critically finds that 'aggregation improves performance when a verifier exists,' directly motivating SICA's approach. ROMA (arXiv 2509.21549, ICLR 2026 Workshop RSI) occupies the adjacent conceptual space of cross-path intermediate-step analysis via shared 'decision pivots' but uses neural verification rather than formal solvers — SICA provides formal satisfiability guarantees where ROMA uses learned signals. Draft-and-Prune (D&P, March 2026) improves autoformalization reliability by independently pruning paths with internal contradictions and aggregating survivors via majority voting, but does not perform cross-path constraint checking — its authors note they 'aggregate predictions at the answer level and do not cluster or de-duplicate candidates by symbolic equivalence.' Meanwhile, VERGE (Jan 2026) verifies and refines a single LLM output by decomposing it into atomic claims, checking joint satisfiability via Z3, and using Minimal Correction Subsets (MCS) to provide targeted refinement feedback — but operates on one output, not across reasoning paths. In the adjacent cross-output verification space, 'Quantifying Cross-Query Contradictions' (arXiv 2604.14525, April 2026) uses Z3 (QF_UFLIA) and CaDiCaL for cross-query consistency checking with unsat-core repair, but addresses cross-query consistency (different questions sharing a case file) rather than cross-trace consistency (same question, multiple paths). Single-solution formal verification (MATH-VF uses CAS+Z3; SAFE uses Lean4; PRoSFI uses Lean/Z3/Prover9 for structured formal intermediaries on 7B models; FoVer (arXiv 2505.15960) uses Z3+Isabelle for PRM training data with cross-task generalization to BBH) improves reliability but none cross-validate across solutions.\\n\\nSICA fills this gap by extracting typed symbolic assertions from K sampled reasoning traces, routing them to appropriate solvers via assertion-level theory-aware dispatch (Z3 for linear arithmetic and propositional logic; SymPy for nonlinear polynomial and algebraic constraints — finer-grained than the EACL 2026 problem-level solver routing), and using Z3's built-in weighted partial MAX-SAT optimization to find the largest jointly satisfiable assertion set weighted by cross-solution frequency. SICA's MAX-SAT consensus across paths is the cross-path counterpart to VERGE's within-output MCS (dual operations: MAX-SAT keeps the maximum consistent subset; MCS removes the minimum inconsistent subset), and differs from cross-query contradiction checking by operating on multiple traces for the same question via weighted consensus rather than unsat-core repair across different questions. A three-tier extraction quality pipeline (syntactic validation, semantic spot-checking targeting the unfaithfulness patterns identified by 'Do LLMs Game Formalization?' (arXiv 2604.19459), and coverage tracking) addresses the documented task-dependence of autoformalization.\\n\\nWe explicitly acknowledge a fundamental limitation: SICA's MAX-SAT consensus catches contradictory constraints but cannot detect universally-wrong-but-consistent constraints caused by correlated extraction errors — the same correlated error phenomenon documented by 'Consensus is Not Verification.' The semantic spot-checking tier partially mitigates this, but correlated biases between the extractor and judge LLMs limit its effectiveness. We include FOLIO as a diagnostic ablation and propose a correlated extraction error analysis to empirically characterize this boundary.\\n\\nWe adopt a dual-track evaluation plan with a concrete day-by-day timeline. Track A (EMNLP 2026, ARR May 25 — 14-day sprint): Days 1-3 pipeline implementation, Days 4-6 core experiments, Days 7-8 ablations/analysis, Days 9-10 figures/tables, Days 11-13 paper writing, Day 14 submission. Full scope: K=12 on MATH-500, AIME 2024, AIME 2025 (identical pipeline to AIME 2024, trivially low marginal cost), ProofWriter, FOLIO, and 3 BBH subtasks (logical deduction, tracking shuffled objects, temporal sequences). Minimum viable scope (fallback if BBH extraction unreliable or timeline slips): 5 benchmarks — MATH-500, AIME 2024, AIME 2025, ProofWriter, FOLIO — which preserves all core contributions while saving ~1.5 days. There is no June ARR cycle (ARR uses 10-week cycles); if May 25 is missed, AAAI 2027 (paper deadline: August 1) serves as the fallback venue with full Track A+B evaluation. Track B (AAAI 2027): expanded to K=16 with GPQA Diamond, LogiQA 2.0, Qwen3-32B cross-model ablation, and any benchmarks deferred from Track A. The centerpiece experiment is a contradiction frequency analysis measuring how often statistical consensus retains logically contradictory constraint pairs. FOLIO serves as a diagnostic ablation where SMT is documented to hurt (-44.5%). Primary contributions: formal soundness guarantees, interpretable constraint-level provenance, empirically-quantified detection of contradictory consensus that both statistical methods and per-path pruning miss, systematic domain analysis of formal cross-solution verification, and honest characterization of the correlated extraction error limitation. Auto-mode compute fits within 200h H100 budget at K=12 with 6+3 benchmarks (full scope) or ~130h H100 with 5 benchmarks (minimum viable scope).\",\n  \"project_name\": \"symb_invariant_consensus\",\n  \"source\": \"web_research\"\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "caf30943-3182-4706-98b0-af43e661d210",
  "isSidechain": false,
  "requestId": "req_011Cawi8Co7RppiERiRwbDP8",
  "type": "assistant",
  "uuid": "ac3ea583-2509-4755-bfd6-1f26bd09d053",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WSFNqsZ1mf5fWCJZG5JaYT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3689,
      "cache_read_input_tokens": 33400,
      "output_tokens": 12274,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3689,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 12274,
          "cache_read_input_tokens": 33400,
          "cache_creation_input_tokens": 3689,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3689
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-12T00:19:47.153Z_

<details><summary>↩ Tool result · reported error · `toolu_01GRvfozo833qpjJdnmiWNQE`</summary>

```text
Claude requested permissions to write to /tmp/revised_idea.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac3ea583-2509-4755-bfd6-1f26bd09d053",
  "isSidechain": false,
  "promptId": "d9295023-136d-4eec-b865-315f1454c5eb",
  "type": "user",
  "uuid": "aa67f6a7-7f6f-48e4-b409-72a62b3a3600",
  "toolUseResult": "Error: Claude requested permissions to write to /tmp/revised_idea.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "ac3ea583-2509-4755-bfd6-1f26bd09d053",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"Formally-Verified Intermediate Constraint Consensus Across Reasoning P…",
  "leafUuid": "aa67f6a7-7f6f-48e4-b409-72a62b3a3600",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise SICA feasibility with realistic timeline and minimum viable scope",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3"
}
```

---

### Tool call

_source line 43 · 2026-05-12T00:24:35.312Z_

<details open><summary>🔧 Tool call — Write · `toolu_01KABypiNfXJPtB7YCoUSr93`</summary>

```json
{
  "file_path": "/tmp/revised_idea.json",
  "content": "{\n  \"title\": \"Formally-Verified Intermediate Constraint Consensus Across Reasoning Paths\",\n  \"change_type\": \"minor\",\n  \"core_problem\": \"Recent work (CRAFT, PoLR, Draft-and-Prune) demonstrates that intermediate reasoning step consensus or pruning across candidate solutions provides stronger signals than answer-level majority voting. However, existing methods either rely on statistical similarity that cannot distinguish popular-but-contradictory constraints (CRAFT's TF-IRF/Jaccard), or prune individual paths based on internal consistency without cross-validating constraints across solutions (Draft-and-Prune's per-path |S|=0/|S|>1 checks). Meanwhile, single-output formal verification systems (MATH-VF, SAFE, FoVer, PRoSFI, VERGE) verify constraints within one solution or output but do not cross-validate across multiple reasoning paths, and cross-query consistency checking (arXiv 2604.14525) verifies coherence across different questions but not across multiple traces for the same question. Furthermore, 'Consensus is Not Verification' (arXiv 2603.06612) demonstrates that consensus-based aggregation fails for truthfulness because LLM errors are strongly correlated — but crucially, aggregation improves performance when a verifier exists. Can formally verifying cross-solution intermediate constraints via SMT solving and computer algebra yield more reliable consensus with interpretable provenance, and how frequently does statistical consensus actually retain contradictory constraints in practice?\",\n  \"opportunity\": \"CRAFT (arXiv 2604.14121, April 2026) builds a Reasoning Knowledge Graph from consensus intermediate steps using TF-IRF and Jaccard similarity, achieving significant accuracy improvements. However, CRAFT's authors explicitly acknowledge two key limitations: (1) 'consensus ≠ correctness' — frequently appearing steps can amplify shared errors, and (2) 'reduced effectiveness on symbolic math' due to lexical overlap bias in Jaccard similarity. This concern is empirically grounded by 'Consensus is Not Verification' (arXiv 2603.06612, March 2026), which demonstrates that LLM errors are strongly correlated across samples and even across model families — correlation persists even with random string conditioning — causing polling-style aggregation to yield no consistent accuracy gains over single-sample baselines. Critically, however, the paper finds that 'aggregation improves performance when a verifier exists, but it cannot serve as a verifier substitute,' directly motivating SICA's approach of introducing formal verification into the consensus process.\\n\\nDraft-and-Prune (D&P, arXiv 2603.17233, March 2026) addresses autoformalization brittleness by generating multiple natural-language plans, conditioning program generation on them, pruning individually contradictory or ambiguous formalizations (paths where the solver returns |S|=0 or |S|>1), and aggregating surviving paths via answer-level majority voting. D&P achieves strong results on logical reasoning benchmarks (AR-LSAT 78.43%, ProofWriter 98.33% with GPT-4), but its pruning operates independently on each path — it cannot detect cross-path contradictions where two individually valid paths assert mutually inconsistent constraints. D&P's authors explicitly note a limitation: 'We aggregate predictions at the answer level and do not cluster or de-duplicate candidates by symbolic equivalence.'\\n\\nA parallel line of work verifies individual solutions or outputs formally — MATH-VF (arXiv 2505.20869) uses CAS+Z3 for step-level verification on single solutions; SAFE (ACL 2025) uses Lean4 for retrospective step-aware verification; PRoSFI (arXiv 2603.29500) trains process rewards over structured formal intermediaries verified by Lean/Z3/Prover9, operating on individual 7B-model solutions. VERGE (arXiv 2601.20055, Jan 2026) is a single-output verify-and-refine framework that decomposes an LLM output into atomic claims, autoformalizes them, verifies joint satisfiability via Z3, and uses Minimal Correction Subsets (MCS) to provide targeted feedback for iterative refinement. VERGE's 'multi-model consensus' refers to K=3 candidate formalizations of a single claim checked for semantic equivalence — not cross-path reasoning aggregation. FoVer (arXiv 2505.15960, ACL 2026 Findings) uses Z3 and Isabelle for step-level error annotation in individual solutions for PRM training, demonstrating cross-task generalization to BBH subtasks (temporal sequences, tracking shuffled objects, word sorting). In the adjacent cross-output verification space, 'Quantifying Cross-Query Contradictions' (arXiv 2604.14525, April 2026) uses Z3 (QF_UFLIA) and CaDiCaL for cross-query consistency checking with unsat-core localization and counterexample-guided repair — but addresses cross-query consistency (different questions sharing a case file), not cross-trace consistency (same question, multiple reasoning paths). The EACL 2026 dynamic solver routing framework (arXiv 2510.06774) selects solvers at the problem level. But none of these methods formally cross-validate intermediate constraints across multiple candidate solutions for the same problem.\\n\\nThe gap: no method formally cross-validates intermediate constraints across multiple candidate solutions to produce a consistency-aware consensus signal with interpretable provenance. Concretely, SICA differs from D&P by extracting constraints from ALL paths and finding a globally consistent MAX-SAT-optimal subset (cross-path aggregation), rather than independently pruning paths with internal contradictions (per-path filtering). SICA differs from VERGE by applying MAX-SAT across multiple reasoning paths for answer selection, whereas VERGE applies the dual MCS operation within a single output for refinement feedback. SICA differs from the cross-query contradictions framework by operating on multiple traces for the same question (cross-trace scope) using weighted partial MAX-SAT for consensus, rather than on different questions in a case file (cross-query scope) using unsat-core repair. A key empirical question — how frequently does statistical consensus actually retain contradictory constraints? — remains unanswered and is central to quantifying this opportunity.\\n\\nRecent work on autoformalization faithfulness further motivates SICA's extraction quality pipeline: 'Do LLMs Game Formalization?' (arXiv 2604.19459, VerifAI-2 Workshop, ICLR 2026) shows that high compilation rates should not be equated with faithful reasoning, finding that two-stage formalization pipelines reveal distinct unfaithfulness patterns (axiom fabrication, premise mistranslation) that evade standard verification. This underscores the need for SICA's multi-tier extraction validation.\",\n  \"landscape\": \"Standard self-consistency (Wang et al., ICLR 2023) performs majority voting on final answers and shows diminishing returns on frontier models — gains plateau at <2% with accuracy sometimes declining at high sample counts (arXiv 2511.00751). 'Consensus is Not Verification' (arXiv 2603.06612, March 2026) provides a theoretical explanation: LLM errors are strongly correlated across samples and model families, causing consensus to reinforce shared misconceptions rather than converge on truth; however, the paper finds aggregation succeeds when an external verifier exists. CRAFT (arXiv 2604.14121, April 2026) extracts consensus intermediate steps via a Reasoning Knowledge Graph using TF-IRF/Jaccard similarity and topological generation, achieving up to +8.5% accuracy over SC baselines on GSM8K, FOLIO, FLD, and OlympiadBench with K=3 traces; its authors note 'consensus ≠ correctness' and 'reduced effectiveness on symbolic math' as limitations. PoLR (ICLR 2026) uses prefix consensus to prune reasoning paths, matching SC accuracy while reducing token usage by 50-60%.\\n\\nCross-path intermediate-step analysis with neural verification: 'Correct Reasoning Paths Visit Shared Decision Pivots' (ROMA, arXiv 2509.21549, NeurIPS 2025 Workshop FoRLM; ICLR 2026 Workshop RSI) hypothesizes that correct reasoning paths converge on shared 'decision pivots' — minimal, verifiable checkpoints that any correct path must visit. ROMA mines these pivots across K sampled reasoning paths and uses a learned verifier to distill pivot-focused short-path reasoning, evaluating on LogiQA, MedQA, and MATH-500. ROMA occupies the adjacent conceptual space of cross-path intermediate-step consensus but uses neural verification (a trained pivot verifier) rather than formal solvers. SICA provides formal satisfiability guarantees where ROMA uses learned signals, and operates on typed symbolic constraints rather than natural-language decision pivots — the approaches are complementary, with ROMA better suited to domains where formalization is intractable and SICA to domains with extractable logical structure.\\n\\nDraft-and-Prune (D&P, arXiv 2603.17233, March 2026): An inference-time framework that drafts multiple natural-language plans, conditions program generation on them, prunes executable but contradictory (|S|=0) or ambiguous (|S|>1) formalizations independently for each path, and aggregates surviving paths via answer-level majority voting. Uses Z3Py for AR-LSAT/LogicalDeduction and PyKe for ProofWriter/PrOntoQA. Achieves AR-LSAT 78.43%, ProofWriter 98.33%, PrOntoQA 99.32%, LogicalDeduction 99.50% (GPT-4). Key limitation: no cross-path constraint checking or equivalence-aware deduplication.\\n\\nVERGE (arXiv 2601.20055, Jan 2026): A single-output neurosymbolic verify-and-refine loop. Decomposes an LLM output into atomic claims, classifies them by type, autoformalizes into FOL, and verifies joint satisfiability via Z3. Uses semantic routing (symbolic solvers for logical claims, LLM ensembles for commonsense) and Minimal Correction Subsets (MCS) for precise error localization, providing actionable feedback for iterative refinement. VERGE's K=3 refers to candidate formalizations of a single claim checked for semantic equivalence, not multiple reasoning paths. MCS (minimum claims to remove for satisfiability) is dual to MAX-SAT (maximum satisfiable subset) but is applied within one output for feedback, not across paths for consensus. Evaluated on FOLIO (84.7-89.2%), ProofWriter (85.2-93.0%), AR-LSAT (88.6-91.7%) across GPT-OSS-20B, GPT-OSS-120B, and Claude 3.7 Sonnet.\\n\\nSingle-solution formal verification: MATH-VF (arXiv 2505.20869, May 2025) uses a Formalizer+Critic pipeline with CAS and Z3 SMT solver for step-level verification on individual solutions, evaluated on MATH-500 and ProcessBench. SAFE (ACL 2025, arXiv 2506.04592) uses Lean4 for retrospective step-aware formal verification of individual reasoning chains, introducing the FormalStep benchmark (30,809 formal statements). PRoSFI (arXiv 2603.29500, March 2026) — 'Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries' — trains process rewards over structured formal intermediaries verified by Lean tactics, Z3, and Prover9, operating on individual 7B-model solutions; achieves 92.97% accuracy / 76.07% GPT Soundness on ProverQA-Hard. FoVer (arXiv 2505.15960, ACL 2026 Findings) — 'Training Step-Level Reasoning Verifiers with Formal Verification Tools' — uses Z3 and Isabelle for step-level error annotation in individual solutions for PRM training; demonstrates cross-task generalization to BBH subtasks (temporal sequences 97.2%, tracking shuffled objects 96.0%, word sorting 46.8% with Llama3.1-8B-PRM at Best-of-7) and to MATH, AIME, ANLI, MMLU-Pro.\\n\\nCross-output consistency verification: 'Quantifying Cross-Query Contradictions in Multi-Query LLM Reasoning' (arXiv 2604.14525, April 2026) addresses cross-query consistency — maintaining a globally satisfiable belief state across interdependent queries sharing a case file. Uses Z3 v4.8.17 (QF_UFLIA theory) and CaDiCaL for SAT, with unsat-core localization and counterexample-guided lexicographic repair. Achieves SetCons improvement from 0.56 to 0.94 across 390 case files spanning relational/SAT, temporal/SMT, policy/rules, and abductive domains. Crucially, this operates at cross-query scope (different questions sharing context) rather than cross-trace scope (same question, multiple reasoning paths), and uses unsat-core repair rather than weighted partial MAX-SAT consensus. SICA's differentiators are: cross-trace scope, intermediate constraint extraction from reasoning steps, and popularity-weighted MAX-SAT for answer selection.\\n\\nSolver routing: The EACL 2026 dynamic solver composition framework (arXiv 2510.06774) automatically identifies formal reasoning strategies and routes to specialized solvers at the problem level, achieving 27% improvement over GPT-4o. SICA's theory-aware routing operates at the finer-grained assertion level.\\n\\nVeriCoT (Nov 2025) formalizes individual CoT traces into FOL for entailment checking without cross-solution comparison. FregeLogic (SemEval 2026) uses Z3 as a tiebreaker for syllogistic validity.\\n\\nAutoformalization reliability: Grammars of Formal Uncertainty (NeurIPS 2025) demonstrates that SMT autoformalization is task-dependent: +34.8% on ProofWriter but -44.5% on FOLIO, necessitating careful benchmark selection and per-domain extraction analysis. 'Do LLMs Game Formalization?' (arXiv 2604.19459, VerifAI-2 Workshop, ICLR 2026) evaluates faithfulness of LLM autoformalization on 303 FOL problems, finding that high compilation rates (87-99%) do not guarantee faithful reasoning — two-stage pipelines reveal distinct unfaithfulness patterns: axiom fabrication (GPT-5) and premise mistranslation (DeepSeek-R1). Autoformalization surveys (arXiv 2505.23486) report ~70% success rate on physics kinematics, with selective verification reducing errors by 14-100% with minimal abstention.\\n\\nNo concurrent work (searched arXiv and OpenReview through May 2026) formally cross-validates intermediate constraints across multiple candidate solutions for the same problem.\",\n  \"approach\": \"We propose Symbolic Invariant Consensus Aggregation (SICA): given a problem, sample K reasoning paths from a frontier open-source reasoning model (QwQ-32B via vLLM on 1-2 A100s; Qwen3-32B as secondary model for ablation), then use a prompted LLM extractor to parse each trace into typed symbolic assertions (equations, inequalities, logical predicates). SICA introduces four key technical components:\\n\\n(1) **Theory-aware assertion-level solver routing**: Extracted assertions are classified by constraint type and routed to appropriate solvers — Z3 for tractable theories (linear arithmetic, propositional logic, uninterpreted functions, bitvectors) and SymPy for nonlinear polynomial arithmetic, algebraic equivalence, and modular arithmetic. Unlike the EACL 2026 framework (arXiv 2510.06774) which routes at the problem level, SICA routes at the assertion level, enabling mixed-theory problems where individual steps span different solver domains (common in competition math). Assertions that neither solver can handle receive numerical spot-checking as fallback, with unverifiable assertions flagged and excluded from the consensus set (rather than silently included).\\n\\n(2) **Weighted partial MAX-SAT for invariant consensus**: Rather than enumerating assertion subsets (exponential worst-case), SICA leverages Z3's built-in optimization context to solve weighted partial MAX-SAT directly. Each unique assertion (deduplicated via solver-verified equivalence) is weighted by its cross-solution frequency. The optimizer finds the largest jointly satisfiable subset of assertions, weighted by popularity — a single Z3 optimization call replaces exponential subset enumeration. Per-query timeout caps (10s) bound worst-case latency. This cross-path MAX-SAT consensus is the key differentiator from Draft-and-Prune (D&P), which prunes paths independently based on internal consistency (|S|=0 or |S|>1) and aggregates surviving answers via majority voting without cross-path constraint checking. It is also distinct from VERGE's MCS, which is the dual operation (minimum claims to remove) applied within a single output for refinement feedback rather than across paths for answer selection. It further differs from the cross-query contradictions framework (arXiv 2604.14525), which uses unsat-core localization and counterexample-guided repair across different questions sharing a case file — SICA uses weighted partial MAX-SAT across different reasoning traces for the same question.\\n\\n(3) **Invariant-backed answer scoring**: Each candidate answer is scored by the coverage and weight of its supporting assertions within the MAX-SAT-optimal consistent set, yielding a continuous invariant consensus score. This captures partial structural agreement even when final answers diverge, and provides interpretable provenance (each score is backed by a specific set of formally verified constraints).\\n\\n(4) **Extraction quality assurance pipeline**: To address the documented task-dependence of autoformalization (Grammars of Formal Uncertainty, NeurIPS 2025) and the unfaithfulness risks identified by 'Do LLMs Game Formalization?' (arXiv 2604.19459), we implement a three-tier extraction quality pipeline: (a) syntactic validation — each extracted assertion must parse in the target solver's input language; (b) semantic spot-checking — a random 20% of assertions are checked against the original natural language step via an LLM judge for semantic fidelity, specifically targeting the axiom fabrication and premise mistranslation failure modes identified in the faithfulness literature; (c) coverage tracking — we report 'verifiable assertion coverage' (% of extracted assertions that successfully enter the MAX-SAT pipeline) per benchmark as a first-class metric. Extraction failures cascade to numerical fallback or abstention, preventing malformed inputs from corrupting the consensus signal.\\n\\n**Limitations of formal cross-validation**: SICA's MAX-SAT consensus catches contradictory constraints but cannot detect universally-wrong-but-mutually-consistent constraints caused by correlated extraction errors. 'Consensus is Not Verification' (arXiv 2603.06612) demonstrates that LLM errors are strongly correlated across samples and even across model families, which implies that if all K paths produce the same wrong formalization of a constraint, MAX-SAT will see K consistent-but-wrong assertions and cannot flag the error. This is a fundamental limitation of any approach combining LLM extraction with formal verification: the verifier guarantees consistency, not correctness of the extraction. SICA's semantic spot-checking tier partially mitigates this — by sampling 20% of assertions for LLM-judge semantic fidelity checks, it can catch systematic mistranslation patterns. However, if the extraction LLM and the judge LLM share the same correlated bias (as the correlated errors literature suggests is likely), the mitigation is incomplete. We acknowledge this limitation explicitly and note two potential future mitigations: (a) using structurally diverse extractor models (e.g., symbolic parsers alongside LLM extractors) to decorrelate extraction errors, and (b) grounding extracted constraints against external knowledge sources (CAS simplification, unit-test-style numerical spot-checking) that do not share LLM inductive biases. We include FOLIO as a diagnostic ablation where SMT autoformalization is documented to hurt (-44.5%), precisely to empirically characterize the boundary between domains where SICA's extraction is faithful enough to help versus where correlated errors dominate.\\n\\n**Day-by-day Track A timeline (14-day sprint, May 12–25)**:\\n\\n- *Days 1–3 (May 12–14): Pipeline implementation.* Day 1: extraction prompt development for math domains (MATH-500, AIME) and logical domains (ProofWriter, FOLIO) — two prompt templates covering all benchmarks. Day 2: solver routing infrastructure (Z3 + SymPy dispatch, MAX-SAT wrapper using Z3's optimization context, equivalence deduplication). Day 3: end-to-end pipeline integration and smoke testing on 50 problems from MATH-500.\\n- *Days 4–6 (May 15–17): Core experiments.* Day 4: MATH-500 (K=12) + AIME 2024 (K=12) + AIME 2025 (K=12) — all share the math extraction prompt; batched vLLM inference across 2 A100s. Day 5: ProofWriter (K=12) — direct D&P/VERGE comparison benchmark. Day 6: FOLIO (K=12, negative diagnostic) + begin BBH subtasks if pipeline stable.\\n- *Days 7–8 (May 18–19): Ablations and additional experiments.* Day 7: BBH subtasks (3 configs × K=12) if extraction quality validates; otherwise, begin ablation suite (K sweep, extraction noise injection). Day 8: Contradiction frequency analysis (centerpiece experiment) across all completed benchmarks; correlated extraction error measurement on 100 problems per benchmark.\\n- *Days 9–10 (May 20–21): Analysis and figures.* Compile results tables, generate accuracy/calibration figures, write contradiction frequency analysis, produce extraction quality breakdown per benchmark. Compute-normalized comparison (tokens, wall-clock time).\\n- *Days 11–13 (May 22–24): Paper writing.* Day 11: Introduction, method description, related work. Day 12: Experiments, results, analysis sections. Day 13: Abstract, conclusion, formatting, supplementary material.\\n- *Day 14 (May 25): Final polish and submission.* Buffer day for last-minute fixes, ARR submission.\\n\\n**Honest assessment of timeline risk**: Paper writing in 3 days is aggressive but feasible for a focused 8-page submission with auto-generated figures and tables from Days 9–10. The main risk is pipeline debugging overrunning Days 1–3, which compresses experiment time. The minimum viable scope (below) mitigates this by defining a credible fallback that preserves 1–2 buffer days.\\n\\n**Note on ARR cycle fallback**: There is no June 2026 ARR cycle — ARR operates on 10-week cycles (~5 per year), and the May 25 cycle is the last eligible for EMNLP 2026 commitment (deadline: August 2, 2026). If the May 25 deadline is missed, the fallback is AAAI 2027 (paper deadline: August 1, 2026), which provides an additional 11 weeks and allows full Track A+B evaluation without time pressure.\\n\\n**Minimum viable scope (fallback if full plan proves too ambitious)**: If extraction quality is unreliable on BBH subtasks or timeline slips compress experiment time, the minimum credible submission is 5 benchmarks at K=12: MATH-500, AIME 2024, AIME 2025, ProofWriter, and FOLIO. This scope preserves all core contributions: (a) cross-path MAX-SAT consensus demonstrated on ProofWriter (D&P/VERGE comparison), (b) contradiction frequency analysis on math benchmarks (MATH-500, AIME 2024/2025), (c) negative diagnostic on FOLIO showing domain boundaries, (d) generalization test on unseen competition problems (AIME 2025 vs. AIME 2024), and (e) extraction quality analysis. BBH subtasks and the FoVer comparison would move to the AAAI 2027 extended version (Track B). This fallback saves ~1.5 days of experiment time (BBH extraction prompt development + 3 benchmark runs), creating headroom for pipeline debugging or additional paper writing time. Under this minimum scope, the timeline adjusts to: Days 1–3 implementation, Days 4–5 experiments (5 benchmarks), Days 6–7 ablations/analysis, Days 8–10 paper writing, Days 11–14 polish/buffer — a substantially more comfortable schedule.\\n\\n**Dual-track evaluation plan**:\\n\\n*Track A — EMNLP 2026 (ARR May 25, primary target, 14 days):* Scoped evaluation with K=12 traces on 6 core benchmarks plus 3 BBH subtasks (full scope) or 5 core benchmarks (minimum viable scope):\\n- **MATH-500** (algebraic/arithmetic reasoning; QwQ-32B ~90.6%)\\n- **AIME 2024** (competition math with mixed-theory constraints; QwQ-32B ~79.5%)\\n- **AIME 2025** (unseen competition problems; tests generalization using the identical evaluation pipeline as AIME 2024 — trivially low marginal cost since both share the same extraction prompt and solver routing)\\n- **ProofWriter** (formal logic; enables direct comparison with D&P 98.33% and VERGE 85.2-93.0%)\\n- **FOLIO** (first-order logic; diagnostic ablation — SMT autoformalization documented to hurt -44.5% here)\\n- **BBH** (3 subtasks: logical deduction, tracking shuffled objects, temporal sequences — enables direct comparison with FoVer's BBH evaluation at Best-of-7; tests cross-domain generalization to structured informal reasoning) *[included in full scope; deferred to Track B in minimum viable scope]*\\n\\nBaselines for Track A: self-consistency, CRAFT, D&P (on ProofWriter), VERGE (on ProofWriter/FOLIO).\\n\\n*Track B — AAAI 2027 (abstract deadline: July 25, paper deadline: August 1, 2026; extended version):* Expanded to K=16 traces on all Track A benchmarks plus:\\n- **GPQA Diamond** (graduate-level science; QwQ-32B ~65.2%; per-domain reporting for physics/chemistry vs. biology)\\n- **LogiQA 2.0** (natural language logical reasoning; 8,678 questions; tests constraint extraction beyond math/formal logic)\\n- BBH subtasks (if deferred from Track A) and full ablation suite\\n- Qwen3-32B cross-model ablation\\n\\n**ARC-Challenge exclusion justification**: ARC-Challenge (Clark et al., 2018) consists of multiple-choice grade-school science questions that primarily test factual knowledge retrieval (e.g., 'Which mineral is the hardest?', 'What happens when water freezes?'). Most questions lack the multi-step constraint structure required for meaningful symbolic assertion extraction — they involve domain knowledge rather than chains of extractable equations, inequalities, or logical predicates. Including ARC-Challenge would likely yield near-zero verifiable assertion coverage, providing no insight beyond confirming SICA's domain specificity (which FOLIO already demonstrates as a negative diagnostic). We note this scope limitation explicitly.\\n\\n**Metrics and analyses**:\\n- Primary: accuracy, calibration (ECE), informativeness of partial invariant agreement when candidates disagree\\n- **Contradiction frequency analysis** (centerpiece experiment): For each problem across all benchmarks, we measure how often CRAFT's statistical consensus retains logically contradictory constraint pairs. We report the 'contradiction rate' — the fraction of problems where at least one pair of popular constraints (appearing in ≥3 of K traces) are mutually unsatisfiable. If >15%, this validates SICA's core motivation; if <5%, we honestly acknowledge limited practical impact on this axis and emphasize interpretability/provenance instead.\\n- **D&P comparison**: On ProofWriter (shared benchmark), we compare SICA's cross-path MAX-SAT consensus against D&P's per-path pruning + answer-level voting, specifically measuring: (a) how many problems have cross-path contradictions that D&P's per-path pruning misses, and (b) whether MAX-SAT-backed scoring outperforms answer-level majority voting among surviving paths.\\n- **FoVer comparison on BBH** (full scope only): On the 3 shared BBH subtasks, we compare SICA's inference-time cross-path consensus against FoVer's training-time PRM approach (Llama3.1-8B-PRM at Best-of-7: temporal 97.2%, tracking 96.0%, word sorting 46.8%), analyzing whether cross-path formal consensus provides complementary signal to trained process reward models.\\n- **Extraction accuracy ablation**: Per-benchmark measurement of (a) syntactic parse rate, (b) semantic fidelity (manual annotation on 100 samples per benchmark), and (c) error propagation analysis — how X% extraction error degrades MAX-SAT consensus quality via controlled noise injection. Per the findings of 'Do LLMs Game Formalization?', we specifically track axiom fabrication and premise mistranslation rates.\\n- **Correlated extraction error analysis**: On a subset of problems (100 per benchmark), we measure cross-path extraction agreement — the fraction of assertions that are semantically equivalent across all K traces — to empirically quantify the degree of correlated extraction and assess how much independent signal SICA's MAX-SAT actually receives.\\n- **Compute-normalized comparison**: Report total tokens generated, wall-clock time per problem, and decomposed latency (inference, extraction, solver, MAX-SAT) for each method. Plot accuracy vs. total compute (tokens) curves. If SICA takes 5x compute of vanilla SC for +2% accuracy, we justify via interpretability/soundness or acknowledge the tradeoff.\\n\\nThe primary contribution is not raw accuracy improvement over SC (which has diminishing returns on frontier models) but rather: (a) formal soundness guarantees on the consensus signal, (b) interpretable constraint-level provenance for each answer, (c) detecting logically inconsistent popular reasoning steps that both statistical consensus (CRAFT) and per-path pruning (D&P) miss — with empirical quantification of how frequently this occurs, (d) systematic domain analysis of formal cross-solution verification including where it helps (ProofWriter, BBH logical deduction) vs. hurts (FOLIO), and (e) empirical characterization of correlated extraction errors as a fundamental limitation of LLM-based autoformalization in consensus settings.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~180-240h A100 80GB (6 benchmarks + 3 BBH subtasks × K=12 traces + extraction + ablations)\",\n      \"gpu_utilization\": \"Low (~20-30%); GPUs idle during coding, debugging solver routing, manual extraction annotation\",\n      \"timeline\": \"2-3 months\",\n      \"team\": \"1-2 researchers with formal methods and LLM experience\",\n      \"estimated_gpu_cost\": \"$235-310 (at ~$1.30/hr typical A100 spot rate)\",\n      \"h100_equivalent\": \"~90-120h H100 (well within 200h H100 budget)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~220-300h A100 80GB\",\n      \"gpu_utilization\": \"Moderate (~50-60%); agent codes and runs experiments between human review gates\",\n      \"timeline\": \"4-6 weeks (fits AAAI 2027 extended version with writing buffer)\",\n      \"team\": \"1 researcher, ~40-50min/day reviewing extraction quality, solver routing correctness, contradiction analysis, D&P comparison design, and BBH extraction quality; ~6h total for manual semantic fidelity annotation (100 samples × 6 benchmarks + 3 BBH subtasks)\",\n      \"claude_api_cost\": \"$200-400 (est. 2000-4000 Opus turns)\",\n      \"estimated_gpu_cost\": \"$285-390\",\n      \"h100_equivalent\": \"~110-150h H100 (within 200h H100 budget)\",\n      \"risk_note\": \"Solver routing heuristics require human judgment for edge cases; CRAFT replication may need prompt tuning; BBH logical deduction extraction quality needs validation\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~300-400h A100 80GB (Track A full scope: 6 benchmarks + 3 BBH subtasks × K=12 × core ablations; minimum viable scope: 5 benchmarks × K=12 saves ~40h)\",\n      \"gpu_utilization\": \"High (~85-95%); agent pipelines inference, extraction, and solving continuously; batched vLLM serving keeps GPUs saturated\",\n      \"timeline\": \"14-day sprint (May 12-25) for EMNLP 2026 ARR May 25; see day-by-day timeline in approach section. Minimum viable scope provides 1.5-day buffer by dropping BBH subtasks. If May 25 missed, fallback to AAAI 2027 (August 1) with full Track A+B evaluation over 11 additional weeks.\",\n      \"team\": \"0 (initial setup only, ~3 hours)\",\n      \"claude_api_cost\": \"$350-600 (est. 3500-6000 Opus turns)\",\n      \"estimated_gpu_cost\": \"$390-520\",\n      \"h100_equivalent\": \"~150-200h H100 (within 200h H100 budget with K=12; minimum viable scope ~120-160h H100)\",\n      \"speed_bottleneck\": \"GPU count for parallel vLLM inference across benchmarks × 12 samples; secondary bottleneck is Z3 MAX-SAT optimization time (mitigated by 10s per-query timeout)\",\n      \"risk_note\": \"Primary risk: pipeline debugging overruns Days 1-3, compressing experiment time — mitigated by minimum viable scope fallback (5 benchmarks, saves 1.5 days). Secondary risk: automated extraction may produce malformed solver input in ~10-20% of traces; without human review the agent may over-tune extraction prompts to specific benchmarks. AIME 2025 adds negligible marginal cost (identical pipeline to AIME 2024). No June ARR cycle exists — if May 25 missed, AAAI 2027 (August 1) is the fallback venue.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline: May 25, 2026 — 14 days from now; primary target with Track A scoped evaluation; last ARR cycle eligible for EMNLP 2026 commitment on August 2)\",\n    \"AAAI 2027 (abstract deadline: July 25, 2026; paper deadline: August 1, 2026 — extended version with Track B full evaluation; also serves as fallback if May 25 ARR deadline missed)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Self-Consistency Improves Chain of Thought Reasoning in Language Models (ICLR 2023)\",\n    \"CRAFT: Correct Prediction, Wrong Steps? Consensus Reasoning Knowledge Graph for Robust Chain-of-Thought Synthesis (arXiv 2604.14121, April 2026)\",\n    \"Draft-and-Prune: Improving the Reliability of Auto-formalization for Logical Reasoning (arXiv 2603.17233, March 2026)\",\n    \"PoLR: The Path of Least Resistance — Guiding LLM Reasoning Trajectories with Prefix Consensus (ICLR 2026)\",\n    \"VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (arXiv 2601.20055, Jan 2026)\",\n    \"VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks (arXiv 2025)\",\n    \"MATH-VF: Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving (arXiv 2505.20869, May 2025)\",\n    \"SAFE: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification (ACL 2025, arXiv 2506.04592)\",\n    \"Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition (EACL 2026, arXiv 2510.06774)\",\n    \"PRoSFI: Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries (arXiv 2603.29500, March 2026)\",\n    \"FoVer: Training Step-Level Reasoning Verifiers with Formal Verification Tools (arXiv 2505.15960, ACL 2026 Findings)\",\n    \"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks (NeurIPS 2025)\",\n    \"FregeLogic at SemEval 2026 Task 11: Hybrid Neuro-Symbolic Architecture for Syllogistic Validity (SemEval 2026)\",\n    \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (arXiv 2604.19459, VerifAI-2 Workshop, ICLR 2026)\",\n    \"Reevaluating Self-Consistency Scaling in Multi-Agent Systems (arXiv 2511.00751)\",\n    \"Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling (NAACL 2025)\",\n    \"Faithful Logical Reasoning via Symbolic Chain-of-Thought (ACL 2024)\",\n    \"Autoformalization in the Era of Large Language Models: A Survey (arXiv 2505.23486, May 2025)\",\n    \"Consensus is Not Verification: Why Crowd Wisdom Strategies Fail for LLM Truthfulness (arXiv 2603.06612, March 2026)\",\n    \"Quantifying Cross-Query Contradictions in Multi-Query LLM Reasoning (arXiv 2604.14525, April 2026)\",\n    \"Correct Reasoning Paths Visit Shared Decision Pivots (ROMA, arXiv 2509.21549, NeurIPS 2025 Workshop FoRLM; ICLR 2026 Workshop RSI)\"\n  ],\n  \"description\": \"We propose Symbolic Invariant Consensus Aggregation (SICA), a method that formally cross-validates intermediate constraints extracted from multiple LLM reasoning paths to produce a soundness-guaranteed consensus signal. While CRAFT (April 2026) demonstrates the value of intermediate-step consensus via statistical similarity (TF-IRF/Jaccard), its authors explicitly acknowledge 'consensus ≠ correctness' and 'reduced effectiveness on symbolic math.' This limitation is theoretically grounded by 'Consensus is Not Verification' (arXiv 2603.06612, March 2026), which proves that LLM errors are strongly correlated across samples and model families, causing pure consensus to fail — but critically finds that 'aggregation improves performance when a verifier exists,' directly motivating SICA's approach. ROMA (arXiv 2509.21549, ICLR 2026 Workshop RSI) occupies the adjacent conceptual space of cross-path intermediate-step analysis via shared 'decision pivots' but uses neural verification rather than formal solvers — SICA provides formal satisfiability guarantees where ROMA uses learned signals. Draft-and-Prune (D&P, March 2026) improves autoformalization reliability by independently pruning paths with internal contradictions and aggregating survivors via majority voting, but does not perform cross-path constraint checking — its authors note they 'aggregate predictions at the answer level and do not cluster or de-duplicate candidates by symbolic equivalence.' Meanwhile, VERGE (Jan 2026) verifies and refines a single LLM output by decomposing it into atomic claims, checking joint satisfiability via Z3, and using Minimal Correction Subsets (MCS) to provide targeted refinement feedback — but operates on one output, not across reasoning paths. In the adjacent cross-output verification space, 'Quantifying Cross-Query Contradictions' (arXiv 2604.14525, April 2026) uses Z3 (QF_UFLIA) and CaDiCaL for cross-query consistency checking with unsat-core repair, but addresses cross-query consistency (different questions sharing a case file) rather than cross-trace consistency (same question, multiple paths). Single-solution formal verification (MATH-VF uses CAS+Z3; SAFE uses Lean4; PRoSFI uses Lean/Z3/Prover9 for structured formal intermediaries on 7B models; FoVer (arXiv 2505.15960) uses Z3+Isabelle for PRM training data with cross-task generalization to BBH) improves reliability but none cross-validate across solutions.\\n\\nSICA fills this gap by extracting typed symbolic assertions from K sampled reasoning traces, routing them to appropriate solvers via assertion-level theory-aware dispatch (Z3 for linear arithmetic and propositional logic; SymPy for nonlinear polynomial and algebraic constraints — finer-grained than the EACL 2026 problem-level solver routing), and using Z3's built-in weighted partial MAX-SAT optimization to find the largest jointly satisfiable assertion set weighted by cross-solution frequency. SICA's MAX-SAT consensus across paths is the cross-path counterpart to VERGE's within-output MCS (dual operations: MAX-SAT keeps the maximum consistent subset; MCS removes the minimum inconsistent subset), and differs from cross-query contradiction checking by operating on multiple traces for the same question via weighted consensus rather than unsat-core repair across different questions. A three-tier extraction quality pipeline (syntactic validation, semantic spot-checking targeting the unfaithfulness patterns identified by 'Do LLMs Game Formalization?' (arXiv 2604.19459), and coverage tracking) addresses the documented task-dependence of autoformalization.\\n\\nWe explicitly acknowledge a fundamental limitation: SICA's MAX-SAT consensus catches contradictory constraints but cannot detect universally-wrong-but-consistent constraints caused by correlated extraction errors — the same correlated error phenomenon documented by 'Consensus is Not Verification.' The semantic spot-checking tier partially mitigates this, but correlated biases between the extractor and judge LLMs limit its effectiveness. We include FOLIO as a diagnostic ablation and propose a correlated extraction error analysis to empirically characterize this boundary.\\n\\nWe adopt a dual-track evaluation plan with a concrete day-by-day timeline. Track A (EMNLP 2026, ARR May 25 — 14-day sprint): Days 1-3 pipeline implementation, Days 4-6 core experiments, Days 7-8 ablations/analysis, Days 9-10 figures/tables, Days 11-13 paper writing, Day 14 submission. Full scope: K=12 on MATH-500, AIME 2024, AIME 2025 (identical pipeline to AIME 2024, trivially low marginal cost), ProofWriter, FOLIO, and 3 BBH subtasks (logical deduction, tracking shuffled objects, temporal sequences). Minimum viable scope (fallback if BBH extraction unreliable or timeline slips): 5 benchmarks — MATH-500, AIME 2024, AIME 2025, ProofWriter, FOLIO — which preserves all core contributions while saving ~1.5 days. There is no June ARR cycle (ARR uses 10-week cycles); if May 25 is missed, AAAI 2027 (paper deadline: August 1) serves as the fallback venue with full Track A+B evaluation. Track B (AAAI 2027): expanded to K=16 with GPQA Diamond, LogiQA 2.0, Qwen3-32B cross-model ablation, and any benchmarks deferred from Track A. The centerpiece experiment is a contradiction frequency analysis measuring how often statistical consensus retains logically contradictory constraint pairs. FOLIO serves as a diagnostic ablation where SMT is documented to hurt (-44.5%). Primary contributions: formal soundness guarantees, interpretable constraint-level provenance, empirically-quantified detection of contradictory consensus that both statistical methods and per-path pruning miss, systematic domain analysis of formal cross-solution verification, and honest characterization of the correlated extraction error limitation. Auto-mode compute fits within 200h H100 budget at K=12 with 6+3 benchmarks (full scope) or ~130h H100 with 5 benchmarks (minimum viable scope).\",\n  \"project_name\": \"symb_invariant_consensus\",\n  \"source\": \"web_research\"\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa67f6a7-7f6f-48e4-b409-72a62b3a3600",
  "isSidechain": false,
  "requestId": "req_011CawiXcx4ETfg9mEUgsVgA",
  "type": "assistant",
  "uuid": "fe7f1e06-772b-441b-b20e-59416e5ed14e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014LW9aDMBaL8fHUKE1WjdxL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12309,
      "cache_read_input_tokens": 37089,
      "output_tokens": 11264,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 12309,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11264,
          "cache_read_input_tokens": 37089,
          "cache_creation_input_tokens": 12309,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 12309
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-12T00:24:35.329Z_

<details><summary>↩ Tool result · reported error · `toolu_01KABypiNfXJPtB7YCoUSr93`</summary>

```text
Claude requested permissions to write to /tmp/revised_idea.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fe7f1e06-772b-441b-b20e-59416e5ed14e",
  "isSidechain": false,
  "promptId": "d9295023-136d-4eec-b865-315f1454c5eb",
  "type": "user",
  "uuid": "47fcc8dc-a6e0-49e3-849c-a5f153f7427b",
  "toolUseResult": "Error: Claude requested permissions to write to /tmp/revised_idea.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "fe7f1e06-772b-441b-b20e-59416e5ed14e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 45_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"Formally-Verified Intermediate Constraint Consensus Across Reasoning P…",
  "leafUuid": "47fcc8dc-a6e0-49e3-849c-a5f153f7427b",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise SICA feasibility with realistic timeline and minimum viable scope",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3"
}
```

---

### Tool call

_source line 47 · 2026-05-12T00:24:38.791Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01W1JH5YjqVApCW4XURCepe6`</summary>

```json
{
  "command": "echo \"ready\"",
  "description": "Test command"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47fcc8dc-a6e0-49e3-849c-a5f153f7427b",
  "isSidechain": false,
  "requestId": "req_011CawitsKLj3FH65xup5L9e",
  "type": "assistant",
  "uuid": "144c2073-6684-4882-a467-baa556700ab5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R4oZyS7MvxwgwAJQA5qPWL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11016,
      "cache_read_input_tokens": 49398,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11016,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 49398,
          "cache_creation_input_tokens": 11016,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11016
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-12T00:24:39.033Z_

<details><summary>↩ Tool result · `toolu_01W1JH5YjqVApCW4XURCepe6`</summary>

```text
ready
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "144c2073-6684-4882-a467-baa556700ab5",
  "isSidechain": false,
  "promptId": "d9295023-136d-4eec-b865-315f1454c5eb",
  "type": "user",
  "uuid": "47145270-ca45-49ff-9906-2214d3bccbfa",
  "toolUseResult": {
    "stdout": "ready",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  },
  "sourceToolAssistantUUID": "144c2073-6684-4882-a467-baa556700ab5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-12T00:29:32.118Z_

Here is the revised idea as a complete JSON object. This is a **minor** revision addressing the three targeted fixes plus the ROMA citation:

```json
{
  "title": "Formally-Verified Intermediate Constraint Consensus Across Reasoning Paths",
  "change_type": "minor",
  "core_problem": "Recent work (CRAFT, PoLR, Draft-and-Prune) demonstrates that intermediate reasoning step consensus or pruning across candidate solutions provides stronger signals than answer-level majority voting. However, existing methods either rely on statistical similarity that cannot distinguish popular-but-contradictory constraints (CRAFT's TF-IRF/Jaccard), or prune individual paths based on internal consistency without cross-validating constraints across solutions (Draft-and-Prune's per-path |S|=0/|S|>1 checks). Meanwhile, single-output formal verification systems (MATH-VF, SAFE, FoVer, PRoSFI, VERGE) verify constraints within one solution or output but do not cross-validate across multiple reasoning paths, and cross-query consistency checking (arXiv 2604.14525) verifies coherence across different questions but not across multiple traces for the same question. Furthermore, 'Consensus is Not Verification' (arXiv 2603.06612) demonstrates that consensus-based aggregation fails for truthfulness because LLM errors are strongly correlated — but crucially, aggregation improves performance when a verifier exists. Can formally verifying cross-solution intermediate constraints via SMT solving and computer algebra yield more reliable consensus with interpretable provenance, and how frequently does statistical consensus actually retain contradictory constraints in practice?",
  "opportunity": "CRAFT (arXiv 2604.14121, April 2026) builds a Reasoning Knowledge Graph from consensus intermediate steps using TF-IRF and Jaccard similarity, achieving significant accuracy improvements. However, CRAFT's authors explicitly acknowledge two key limitations: (1) 'consensus ≠ correctness' — frequently appearing steps can amplify shared errors, and (2) 'reduced effectiveness on symbolic math' due to lexical overlap bias in Jaccard similarity. This concern is empirically grounded by 'Consensus is Not Verification' (arXiv 2603.06612, March 2026), which demonstrates that LLM errors are strongly correlated across samples and even across model families — correlation persists even with random string conditioning — causing polling-style aggregation to yield no consistent accuracy gains over single-sample baselines. Critically, however, the paper finds that 'aggregation improves performance when a verifier exists, but it cannot serve as a verifier substitute,' directly motivating SICA's approach of introducing formal verification into the consensus process.\n\nDraft-and-Prune (D&P, arXiv 2603.17233, March 2026) addresses autoformalization brittleness by generating multiple natural-language plans, conditioning program generation on them, pruning individually contradictory or ambiguous formalizations (paths where the solver returns |S|=0 or |S|>1), and aggregating surviving paths via answer-level majority voting. D&P achieves strong results on logical reasoning benchmarks (AR-LSAT 78.43%, ProofWriter 98.33% with GPT-4), but its pruning operates independently on each path — it cannot detect cross-path contradictions where two individually valid paths assert mutually inconsistent constraints. D&P's authors explicitly note a limitation: 'We aggregate predictions at the answer level and do not cluster or de-duplicate candidates by symbolic equivalence.'\n\nA parallel line of work verifies individual solutions or outputs formally — MATH-VF (arXiv 2505.20869) uses CAS+Z3 for step-level verification on single solutions; SAFE (ACL 2025) uses Lean4 for retrospective step-aware verification; PRoSFI (arXiv 2603.29500) trains process rewards over structured formal intermediaries verified by Lean/Z3/Prover9, operating on individual 7B-model solutions. VERGE (arXiv 2601.20055, Jan 2026) is a single-output verify-and-refine framework that decomposes an LLM output into atomic claims, autoformalizes them, verifies joint satisfiability via Z3, and uses Minimal Correction Subsets (MCS) to provide targeted feedback for iterative refinement. VERGE's 'multi-model consensus' refers to K=3 candidate formalizations of a single claim checked for semantic equivalence — not cross-path reasoning aggregation. FoVer (arXiv 2505.15960, ACL 2026 Findings) uses Z3 and Isabelle for step-level error annotation in individual solutions for PRM training, demonstrating cross-task generalization to BBH subtasks (temporal sequences, tracking shuffled objects, word sorting). In the adjacent cross-output verification space, 'Quantifying Cross-Query Contradictions' (arXiv 2604.14525, April 2026) uses Z3 (QF_UFLIA) and CaDiCaL for cross-query consistency checking with unsat-core localization and counterexample-guided repair — but addresses cross-query consistency (different questions sharing a case file), not cross-trace consistency (same question, multiple reasoning paths). The EACL 2026 dynamic solver routing framework (arXiv 2510.06774) selects solvers at the problem level. But none of these methods formally cross-validate intermediate constraints across multiple candidate solutions for the same problem.\n\nThe gap: no method formally cross-validates intermediate constraints across multiple candidate solutions to produce a consistency-aware consensus signal with interpretable provenance. Concretely, SICA differs from D&P by extracting constraints from ALL paths and finding a globally consistent MAX-SAT-optimal subset (cross-path aggregation), rather than independently pruning paths with internal contradictions (per-path filtering). SICA differs from VERGE by applying MAX-SAT across multiple reasoning paths for answer selection, whereas VERGE applies the dual MCS operation within a single output for refinement feedback. SICA differs from the cross-query contradictions framework by operating on multiple traces for the same question (cross-trace scope) using weighted partial MAX-SAT for consensus, rather than on different questions in a case file (cross-query scope) using unsat-core repair. A key empirical question — how frequently does statistical consensus actually retain contradictory constraints? — remains unanswered and is central to quantifying this opportunity.\n\nRecent work on autoformalization faithfulness further motivates SICA's extraction quality pipeline: 'Do LLMs Game Formalization?' (arXiv 2604.19459, VerifAI-2 Workshop, ICLR 2026) shows that high compilation rates should not be equated with faithful reasoning, finding that two-stage formalization pipelines reveal distinct unfaithfulness patterns (axiom fabrication, premise mistranslation) that evade standard verification. This underscores the need for SICA's multi-tier extraction validation.",
  "landscape": "Standard self-consistency (Wang et al., ICLR 2023) performs majority voting on final answers and shows diminishing returns on frontier models — gains plateau at <2% with accuracy sometimes declining at high sample counts (arXiv 2511.00751). 'Consensus is Not Verification' (arXiv 2603.06612, March 2026) provides a theoretical explanation: LLM errors are strongly correlated across samples and model families, causing consensus to reinforce shared misconceptions rather than converge on truth; however, the paper finds aggregation succeeds when an external verifier exists. CRAFT (arXiv 2604.14121, April 2026) extracts consensus intermediate steps via a Reasoning Knowledge Graph using TF-IRF/Jaccard similarity and topological generation, achieving up to +8.5% accuracy over SC baselines on GSM8K, FOLIO, FLD, and OlympiadBench with K=3 traces; its authors note 'consensus ≠ correctness' and 'reduced effectiveness on symbolic math' as limitations. PoLR (ICLR 2026) uses prefix consensus to prune reasoning paths, matching SC accuracy while reducing token usage by 50-60%.\n\nCross-path intermediate-step analysis with neural verification: 'Correct Reasoning Paths Visit Shared Decision Pivots' (ROMA, arXiv 2509.21549, NeurIPS 2025 Workshop FoRLM; ICLR 2026 Workshop RSI) hypothesizes that correct reasoning paths converge on shared 'decision pivots' — minimal, verifiable checkpoints that any correct path must visit. ROMA mines these pivots across K sampled reasoning paths and uses a learned verifier to distill pivot-focused short-path reasoning, evaluating on LogiQA, MedQA, and MATH-500. ROMA occupies the adjacent conceptual space of cross-path intermediate-step consensus but uses neural verification (a trained pivot verifier) rather than formal solvers. SICA provides formal satisfiability guarantees where ROMA uses learned signals, and operates on typed symbolic constraints rather than natural-language decision pivots — the approaches are complementary, with ROMA better suited to domains where formalization is intractable and SICA to domains with extractable logical structure.\n\nDraft-and-Prune (D&P, arXiv 2603.17233, March 2026): An inference-time framework that drafts multiple natural-language plans, conditions program generation on them, prunes executable but contradictory (|S|=0) or ambiguous (|S|>1) formalizations independently for each path, and aggregates surviving paths via answer-level majority voting. Uses Z3Py for AR-LSAT/LogicalDeduction and PyKe for ProofWriter/PrOntoQA. Achieves AR-LSAT 78.43%, ProofWriter 98.33%, PrOntoQA 99.32%, LogicalDeduction 99.50% (GPT-4). Key limitation: no cross-path constraint checking or equivalence-aware deduplication.\n\nVERGE (arXiv 2601.20055, Jan 2026): A single-output neurosymbolic verify-and-refine loop. Decomposes an LLM output into atomic claims, classifies them by type, autoformalizes into FOL, and verifies joint satisfiability via Z3. Uses semantic routing (symbolic solvers for logical claims, LLM ensembles for commonsense) and Minimal Correction Subsets (MCS) for precise error localization, providing actionable feedback for iterative refinement. VERGE's K=3 refers to candidate formalizations of a single claim checked for semantic equivalence, not multiple reasoning paths. MCS (minimum claims to remove for satisfiability) is dual to MAX-SAT (maximum satisfiable subset) but is applied within one output for feedback, not across paths for consensus. Evaluated on FOLIO (84.7-89.2%), ProofWriter (85.2-93.0%), AR-LSAT (88.6-91.7%) across GPT-OSS-20B, GPT-OSS-120B, and Claude 3.7 Sonnet.\n\nSingle-solution formal verification: MATH-VF (arXiv 2505.20869, May 2025) uses a Formalizer+Critic pipeline with CAS and Z3 SMT solver for step-level verification on individual solutions, evaluated on MATH-500 and ProcessBench. SAFE (ACL 2025, arXiv 2506.04592) uses Lean4 for retrospective step-aware formal verification of individual reasoning chains, introducing the FormalStep benchmark (30,809 formal statements). PRoSFI (arXiv 2603.29500, March 2026) — 'Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries' — trains process rewards over structured formal intermediaries verified by Lean tactics, Z3, and Prover9, operating on individual 7B-model solutions; achieves 92.97% accuracy / 76.07% GPT Soundness on ProverQA-Hard. FoVer (arXiv 2505.15960, ACL 2026 Findings) — 'Training Step-Level Reasoning Verifiers with Formal Verification Tools' — uses Z3 and Isabelle for step-level error annotation in individual solutions for PRM training; demonstrates cross-task generalization to BBH subtasks (temporal sequences 97.2%, tracking shuffled objects 96.0%, word sorting 46.8% with Llama3.1-8B-PRM at Best-of-7) and to MATH, AIME, ANLI, MMLU-Pro.\n\nCross-output consistency verification: 'Quantifying Cross-Query Contradictions in Multi-Query LLM Reasoning' (arXiv 2604.14525, April 2026) addresses cross-query consistency — maintaining a globally satisfiable belief state across interdependent queries sharing a case file. Uses Z3 v4.8.17 (QF_UFLIA theory) and CaDiCaL for SAT, with unsat-core localization and counterexample-guided lexicographic repair. Achieves SetCons improvement from 0.56 to 0.94 across 390 case files spanning relational/SAT, temporal/SMT, policy/rules, and abductive domains. Crucially, this operates at cross-query scope (different questions sharing context) rather than cross-trace scope (same question, multiple reasoning paths), and uses unsat-core repair rather than weighted partial MAX-SAT consensus. SICA's differentiators are: cross-trace scope, intermediate constraint extraction from reasoning steps, and popularity-weighted MAX-SAT for answer selection.\n\nSolver routing: The EACL 2026 dynamic solver composition framework (arXiv 2510.06774) automatically identifies formal reasoning strategies and routes to specialized solvers at the problem level, achieving 27% improvement over GPT-4o. SICA's theory-aware routing operates at the finer-grained assertion level.\n\nVeriCoT (Nov 2025) formalizes individual CoT traces into FOL for entailment checking without cross-solution comparison. FregeLogic (SemEval 2026) uses Z3 as a tiebreaker for syllogistic validity.\n\nAutoformalization reliability: Grammars of Formal Uncertainty (NeurIPS 2025) demonstrates that SMT autoformalization is task-dependent: +34.8% on ProofWriter but -44.5% on FOLIO, necessitating careful benchmark selection and per-domain extraction analysis. 'Do LLMs Game Formalization?' (arXiv 2604.19459, VerifAI-2 Workshop, ICLR 2026) evaluates faithfulness of LLM autoformalization on 303 FOL problems, finding that high compilation rates (87-99%) do not guarantee faithful reasoning — two-stage pipelines reveal distinct unfaithfulness patterns: axiom fabrication (GPT-5) and premise mistranslation (DeepSeek-R1). Autoformalization surveys (arXiv 2505.23486) report ~70% success rate on physics kinematics, with selective verification reducing errors by 14-100% with minimal abstention.\n\nNo concurrent work (searched arXiv and OpenReview through May 2026) formally cross-validates intermediate constraints across multiple candidate solutions for the same problem.",
  "approach": "We propose Symbolic Invariant Consensus Aggregation (SICA): given a problem, sample K reasoning paths from a frontier open-source reasoning model (QwQ-32B via vLLM on 1-2 A100s; Qwen3-32B as secondary model for ablation), then use a prompted LLM extractor to parse each trace into typed symbolic assertions (equations, inequalities, logical predicates). SICA introduces four key technical components:\n\n(1) **Theory-aware assertion-level solver routing**: Extracted assertions are classified by constraint type and routed to appropriate solvers — Z3 for tractable theories (linear arithmetic, propositional logic, uninterpreted functions, bitvectors) and SymPy for nonlinear polynomial arithmetic, algebraic equivalence, and modular arithmetic. Unlike the EACL 2026 framework (arXiv 2510.06774) which routes at the problem level, SICA routes at the assertion level, enabling mixed-theory problems where individual steps span different solver domains (common in competition math). Assertions that neither solver can handle receive numerical spot-checking as fallback, with unverifiable assertions flagged and excluded from the consensus set (rather than silently included).\n\n(2) **Weighted partial MAX-SAT for invariant consensus**: Rather than enumerating assertion subsets (exponential worst-case), SICA leverages Z3's built-in optimization context to solve weighted partial MAX-SAT directly. Each unique assertion (deduplicated via solver-verified equivalence) is weighted by its cross-solution frequency. The optimizer finds the largest jointly satisfiable subset of assertions, weighted by popularity — a single Z3 optimization call replaces exponential subset enumeration. Per-query timeout caps (10s) bound worst-case latency. This cross-path MAX-SAT consensus is the key differentiator from Draft-and-Prune (D&P), which prunes paths independently based on internal consistency (|S|=0 or |S|>1) and aggregates surviving answers via majority voting without cross-path constraint checking. It is also distinct from VERGE's MCS, which is the dual operation (minimum claims to remove) applied within a single output for refinement feedback rather than across paths for answer selection. It further differs from the cross-query contradictions framework (arXiv 2604.14525), which uses unsat-core localization and counterexample-guided repair across different questions sharing a case file — SICA uses weighted partial MAX-SAT across different reasoning traces for the same question.\n\n(3) **Invariant-backed answer scoring**: Each candidate answer is scored by the coverage and weight of its supporting assertions within the MAX-SAT-optimal consistent set, yielding a continuous invariant consensus score. This captures partial structural agreement even when final answers diverge, and provides interpretable provenance (each score is backed by a specific set of formally verified constraints).\n\n(4) **Extraction quality assurance pipeline**: To address the documented task-dependence of autoformalization (Grammars of Formal Uncertainty, NeurIPS 2025) and the unfaithfulness risks identified by 'Do LLMs Game Formalization?' (arXiv 2604.19459), we implement a three-tier extraction quality pipeline: (a) syntactic validation — each extracted assertion must parse in the target solver's input language; (b) semantic spot-checking — a random 20% of assertions are checked against the original natural language step via an LLM judge for semantic fidelity, specifically targeting the axiom fabrication and premise mistranslation failure modes identified in the faithfulness literature; (c) coverage tracking — we report 'verifiable assertion coverage' (% of extracted assertions that successfully enter the MAX-SAT pipeline) per benchmark as a first-class metric. Extraction failures cascade to numerical fallback or abstention, preventing malformed inputs from corrupting the consensus signal.\n\n**Limitations of formal cross-validation**: SICA's MAX-SAT consensus catches contradictory constraints but cannot detect universally-wrong-but-mutually-consistent constraints caused by correlated extraction errors. 'Consensus is Not Verification' (arXiv 2603.06612) demonstrates that LLM errors are strongly correlated across samples and even across model families, which implies that if all K paths produce the same wrong formalization of a constraint, MAX-SAT will see K consistent-but-wrong assertions and cannot flag the error. This is a fundamental limitation of any approach combining LLM extraction with formal verification: the verifier guarantees consistency, not correctness of the extraction. SICA's semantic spot-checking tier partially mitigates this — by sampling 20% of assertions for LLM-judge semantic fidelity checks, it can catch systematic mistranslation patterns. However, if the extraction LLM and the judge LLM share the same correlated bias (as the correlated errors literature suggests is likely), the mitigation is incomplete. We acknowledge this limitation explicitly and note two potential future mitigations: (a) using structurally diverse extractor models (e.g., symbolic parsers alongside LLM extractors) to decorrelate extraction errors, and (b) grounding extracted constraints against external knowledge sources (CAS simplification, unit-test-style numerical spot-checking) that do not share LLM inductive biases. We include FOLIO as a diagnostic ablation where SMT autoformalization is documented to hurt (-44.5%), precisely to empirically characterize the boundary between domains where SICA's extraction is faithful enough to help versus where correlated errors dominate.\n\n**Day-by-day Track A timeline (14-day sprint, May 12–25)**:\n\n- *Days 1–3 (May 12–14): Pipeline implementation.* Day 1: extraction prompt development for math domains (MATH-500, AIME) and logical domains (ProofWriter, FOLIO) — two prompt templates covering all benchmarks. Day 2: solver routing infrastructure (Z3 + SymPy dispatch, MAX-SAT wrapper using Z3's optimization context, equivalence deduplication). Day 3: end-to-end pipeline integration and smoke testing on 50 problems from MATH-500.\n- *Days 4–6 (May 15–17): Core experiments.* Day 4: MATH-500 (K=12) + AIME 2024 (K=12) + AIME 2025 (K=12) — all share the math extraction prompt; batched vLLM inference across 2 A100s. Day 5: ProofWriter (K=12) — direct D&P/VERGE comparison benchmark. Day 6: FOLIO (K=12, negative diagnostic) + begin BBH subtasks if pipeline stable.\n- *Days 7–8 (May 18–19): Ablations and additional experiments.* Day 7: BBH subtasks (3 configs × K=12) if extraction quality validates; otherwise, begin ablation suite (K sweep, extraction noise injection). Day 8: Contradiction frequency analysis (centerpiece experiment) across all completed benchmarks; correlated extraction error measurement on 100 problems per benchmark.\n- *Days 9–10 (May 20–21): Analysis and figures.* Compile results tables, generate accuracy/calibration figures, write contradiction frequency analysis, produce extraction quality breakdown per benchmark. Compute-normalized comparison (tokens, wall-clock time).\n- *Days 11–13 (May 22–24): Paper writing.* Day 11: Introduction, method description, related work. Day 12: Experiments, results, analysis sections. Day 13: Abstract, conclusion, formatting, supplementary material.\n- *Day 14 (May 25): Final polish and submission.* Buffer day for last-minute fixes, ARR submission.\n\n**Honest assessment of timeline risk**: Paper writing in 3 days is aggressive but feasible for a focused 8-page submission with auto-generated figures and tables from Days 9–10. The main risk is pipeline debugging overrunning Days 1–3, which compresses experiment time. The minimum viable scope (below) mitigates this by defining a credible fallback that preserves 1–2 buffer days.\n\n**Note on ARR cycle fallback**: There is no June 2026 ARR cycle — ARR operates on 10-week cycles (~5 per year), and the May 25 cycle is the last eligible for EMNLP 2026 commitment (deadline: August 2, 2026). If the May 25 deadline is missed, the fallback is AAAI 2027 (paper deadline: August 1, 2026), which provides an additional 11 weeks and allows full Track A+B evaluation without time pressure.\n\n**Minimum viable scope (fallback if full plan proves too ambitious)**: If extraction quality is unreliable on BBH subtasks or timeline slips compress experiment time, the minimum credible submission is 5 benchmarks at K=12: MATH-500, AIME 2024, AIME 2025, ProofWriter, and FOLIO. This scope preserves all core contributions: (a) cross-path MAX-SAT consensus demonstrated on ProofWriter (D&P/VERGE comparison), (b) contradiction frequency analysis on math benchmarks (MATH-500, AIME 2024/2025), (c) negative diagnostic on FOLIO showing domain boundaries, (d) generalization test on unseen competition problems (AIME 2025 vs. AIME 2024), and (e) extraction quality analysis. BBH subtasks and the FoVer comparison would move to the AAAI 2027 extended version (Track B). This fallback saves ~1.5 days of experiment time (BBH extraction prompt development + 3 benchmark runs), creating headroom for pipeline debugging or additional paper writing time. Under this minimum scope, the timeline adjusts to: Days 1–3 implementation, Days 4–5 experiments (5 benchmarks), Days 6–7 ablations/analysis, Days 8–10 paper writing, Days 11–14 polish/buffer — a substantially more comfortable schedule.\n\n**Dual-track evaluation plan**:\n\n*Track A — EMNLP 2026 (ARR May 25, primary target, 14 days):* Scoped evaluation with K=12 traces on 6 core benchmarks plus 3 BBH subtasks (full scope) or 5 core benchmarks (minimum viable scope):\n- **MATH-500** (algebraic/arithmetic reasoning; QwQ-32B ~90.6%)\n- **AIME 2024** (competition math with mixed-theory constraints; QwQ-32B ~79.5%)\n- **AIME 2025** (unseen competition problems; tests generalization using the identical evaluation pipeline as AIME 2024 — trivially low marginal cost since both share the same extraction prompt and solver routing)\n- **ProofWriter** (formal logic; enables direct comparison with D&P 98.33% and VERGE 85.2-93.0%)\n- **FOLIO** (first-order logic; diagnostic ablation — SMT autoformalization documented to hurt -44.5% here)\n- **BBH** (3 subtasks: logical deduction, tracking shuffled objects, temporal sequences — enables direct comparison with FoVer's BBH evaluation at Best-of-7; tests cross-domain generalization to structured informal reasoning) *[included in full scope; deferred to Track B in minimum viable scope]*\n\nBaselines for Track A: self-consistency, CRAFT, D&P (on ProofWriter), VERGE (on ProofWriter/FOLIO).\n\n*Track B — AAAI 2027 (abstract deadline: July 25, paper deadline: August 1, 2026; extended version):* Expanded to K=16 traces on all Track A benchmarks plus:\n- **GPQA Diamond** (graduate-level science; QwQ-32B ~65.2%; per-domain reporting for physics/chemistry vs. biology)\n- **LogiQA 2.0** (natural language logical reasoning; 8,678 questions; tests constraint extraction beyond math/formal logic)\n- BBH subtasks (if deferred from Track A) and full ablation suite\n- Qwen3-32B cross-model ablation\n\n**ARC-Challenge exclusion justification**: ARC-Challenge (Clark et al., 2018) consists of multiple-choice grade-school science questions that primarily test factual knowledge retrieval (e.g., 'Which mineral is the hardest?', 'What happens when water freezes?'). Most questions lack the multi-step constraint structure required for meaningful symbolic assertion extraction — they involve domain knowledge rather than chains of extractable equations, inequalities, or logical predicates. Including ARC-Challenge would likely yield near-zero verifiable assertion coverage, providing no insight beyond confirming SICA's domain specificity (which FOLIO already demonstrates as a negative diagnostic). We note this scope limitation explicitly.\n\n**Metrics and analyses**:\n- Primary: accuracy, calibration (ECE), informativeness of partial invariant agreement when candidates disagree\n- **Contradiction frequency analysis** (centerpiece experiment): For each problem across all benchmarks, we measure how often CRAFT's statistical consensus retains logically contradictory constraint pairs. We report the 'contradiction rate' — the fraction of problems where at least one pair of popular constraints (appearing in ≥3 of K traces) are mutually unsatisfiable. If >15%, this validates SICA's core motivation; if <5%, we honestly acknowledge limited practical impact on this axis and emphasize interpretability/provenance instead.\n- **D&P comparison**: On ProofWriter (shared benchmark), we compare SICA's cross-path MAX-SAT consensus against D&P's per-path pruning + answer-level voting, specifically measuring: (a) how many problems have cross-path contradictions that D&P's per-path pruning misses, and (b) whether MAX-SAT-backed scoring outperforms answer-level majority voting among surviving paths.\n- **FoVer comparison on BBH** (full scope only): On the 3 shared BBH subtasks, we compare SICA's inference-time cross-path consensus against FoVer's training-time PRM approach (Llama3.1-8B-PRM at Best-of-7: temporal 97.2%, tracking 96.0%, word sorting 46.8%), analyzing whether cross-path formal consensus provides complementary signal to trained process reward models.\n- **Extraction accuracy ablation**: Per-benchmark measurement of (a) syntactic parse rate, (b) semantic fidelity (manual annotation on 100 samples per benchmark), and (c) error propagation analysis — how X% extraction error degrades MAX-SAT consensus quality via controlled noise injection. Per the findings of 'Do LLMs Game Formalization?', we specifically track axiom fabrication and premise mistranslation rates.\n- **Correlated extraction error analysis**: On a subset of problems (100 per benchmark), we measure cross-path extraction agreement — the fraction of assertions that are semantically equivalent across all K traces — to empirically quantify the degree of correlated extraction and assess how much independent signal SICA's MAX-SAT actually receives.\n- **Compute-normalized comparison**: Report total tokens generated, wall-clock time per problem, and decomposed latency (inference, extraction, solver, MAX-SAT) for each method. Plot accuracy vs. total compute (tokens) curves. If SICA takes 5x compute of vanilla SC for +2% accuracy, we justify via interpretability/soundness or acknowledge the tradeoff.\n\nThe primary contribution is not raw accuracy improvement over SC (which has diminishing returns on frontier models) but rather: (a) formal soundness guarantees on the consensus signal, (b) interpretable constraint-level provenance for each answer, (c) detecting logically inconsistent popular reasoning steps that both statistical consensus (CRAFT) and per-path pruning (D&P) miss — with empirical quantification of how frequently this occurs, (d) systematic domain analysis of formal cross-solution verification including where it helps (ProofWriter, BBH logical deduction) vs. hurts (FOLIO), and (e) empirical characterization of correlated extraction errors as a fundamental limitation of LLM-based autoformalization in consensus settings.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~180-240h A100 80GB (6 benchmarks + 3 BBH subtasks × K=12 traces + extraction + ablations)",
      "gpu_utilization": "Low (~20-30%); GPUs idle during coding, debugging solver routing, manual extraction annotation",
      "timeline": "2-3 months",
      "team": "1-2 researchers with formal methods and LLM experience",
      "estimated_gpu_cost": "$235-310 (at ~$1.30/hr typical A100 spot rate)",
      "h100_equivalent": "~90-120h H100 (well within 200h H100 budget)"
    },
    "human_in_loop": {
      "gpu_hours": "~220-300h A100 80GB",
      "gpu_utilization": "Moderate (~50-60%); agent codes and runs experiments between human review gates",
      "timeline": "4-6 weeks (fits AAAI 2027 extended version with writing buffer)",
      "team": "1 researcher, ~40-50min/day reviewing extraction quality, solver routing correctness, contradiction analysis, D&P comparison design, and BBH extraction quality; ~6h total for manual semantic fidelity annotation (100 samples × 6 benchmarks + 3 BBH subtasks)",
      "claude_api_cost": "$200-400 (est. 2000-4000 Opus turns)",
      "estimated_gpu_cost": "$285-390",
      "h100_equivalent": "~110-150h H100 (within 200h H100 budget)",
      "risk_note": "Solver routing heuristics require human judgment for edge cases; CRAFT replication may need prompt tuning; BBH logical deduction extraction quality needs validation"
    },
    "auto_research": {
      "gpu_hours": "~300-400h A100 80GB (Track A full scope: 6 benchmarks + 3 BBH subtasks × K=12 × core ablations; minimum viable scope: 5 benchmarks × K=12 saves ~40h)",
      "gpu_utilization": "High (~85-95%); agent pipelines inference, extraction, and solving continuously; batched vLLM serving keeps GPUs saturated",
      "timeline": "14-day sprint (May 12-25) for EMNLP 2026 ARR May 25; see day-by-day timeline in approach section. Minimum viable scope provides 1.5-day buffer by dropping BBH subtasks. If May 25 missed, fallback to AAAI 2027 (August 1) with full Track A+B evaluation over 11 additional weeks.",
      "team": "0 (initial setup only, ~3 hours)",
      "claude_api_cost": "$350-600 (est. 3500-6000 Opus turns)",
      "estimated_gpu_cost": "$390-520",
      "h100_equivalent": "~150-200h H100 (within 200h H100 budget with K=12; minimum viable scope ~120-160h H100)",
      "speed_bottleneck": "GPU count for parallel vLLM inference across benchmarks × 12 samples; secondary bottleneck is Z3 MAX-SAT optimization time (mitigated by 10s per-query timeout)",
      "risk_note": "Primary risk: pipeline debugging overruns Days 1-3, compressing experiment time — mitigated by minimum viable scope fallback (5 benchmarks, saves 1.5 days). Secondary risk: automated extraction may produce malformed solver input in ~10-20% of traces; without human review the agent may over-tune extraction prompts to specific benchmarks. AIME 2025 adds negligible marginal cost (identical pipeline to AIME 2024). No June ARR cycle exists — if May 25 missed, AAAI 2027 (August 1) is the fallback venue."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline: May 25, 2026 — 14 days from now; primary target with Track A scoped evaluation; last ARR cycle eligible for EMNLP 2026 commitment on August 2)",
    "AAAI 2027 (abstract deadline: July 25, 2026; paper deadline: August 1, 2026 — extended version with Track B full evaluation; also serves as fallback if May 25 ARR deadline missed)"
  ],
  "level": "solid",
  "key_references": [
    "Self-Consistency Improves Chain of Thought Reasoning in Language Models (ICLR 2023)",
    "CRAFT: Correct Prediction, Wrong Steps? Consensus Reasoning Knowledge Graph for Robust Chain-of-Thought Synthesis (arXiv 2604.14121, April 2026)",
    "Draft-and-Prune: Improving the Reliability of Auto-formalization for Logical Reasoning (arXiv 2603.17233, March 2026)",
    "PoLR: The Path of Least Resistance — Guiding LLM Reasoning Trajectories with Prefix Consensus (ICLR 2026)",
    "VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (arXiv 2601.20055, Jan 2026)",
    "VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks (arXiv 2025)",
    "MATH-VF: Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving (arXiv 2505.20869, May 2025)",
    "SAFE: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification (ACL 2025, arXiv 2506.04592)",
    "Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition (EACL 2026, arXiv 2510.06774)",
    "PRoSFI: Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries (arXiv 2603.29500, March 2026)",
    "FoVer: Training Step-Level Reasoning Verifiers with Formal Verification Tools (arXiv 2505.15960, ACL 2026 Findings)",
    "Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks (NeurIPS 2025)",
    "FregeLogic at SemEval 2026 Task 11: Hybrid Neuro-Symbolic Architecture for Syllogistic Validity (SemEval 2026)",
    "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (arXiv 2604.19459, VerifAI-2 Workshop, ICLR 2026)",
    "Reevaluating Self-Consistency Scaling in Multi-Agent Systems (arXiv 2511.00751)",
    "Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling (NAACL 2025)",
    "Faithful Logical Reasoning via Symbolic Chain-of-Thought (ACL 2024)",
    "Autoformalization in the Era of Large Language Models: A Survey (arXiv 2505.23486, May 2025)",
    "Consensus is Not Verification: Why Crowd Wisdom Strategies Fail for LLM Truthfulness (arXiv 2603.06612, March 2026)",
    "Quantifying Cross-Query Contradictions in Multi-Query LLM Reasoning (arXiv 2604.14525, April 2026)",
    "Correct Reasoning Paths Visit Shared Decision Pivots (ROMA, arXiv 2509.21549, NeurIPS 2025 Workshop FoRLM; ICLR 2026 Workshop RSI)"
  ],
  "description": "We propose Symbolic Invariant Consensus Aggregation (SICA), a method that formally cross-validates intermediate constraints extracted from multiple LLM reasoning paths to produce a soundness-guaranteed consensus signal. While CRAFT (April 2026) demonstrates the value of intermediate-step consensus via statistical similarity (TF-IRF/Jaccard), its authors explicitly acknowledge 'consensus ≠ correctness' and 'reduced effectiveness on symbolic math.' This limitation is theoretically grounded by 'Consensus is Not Verification' (arXiv 2603.06612, March 2026), which proves that LLM errors are strongly correlated across samples and model families, causing pure consensus to fail — but critically finds that 'aggregation improves performance when a verifier exists,' directly motivating SICA's approach. ROMA (arXiv 2509.21549, ICLR 2026 Workshop RSI) occupies the adjacent conceptual space of cross-path intermediate-step analysis via shared 'decision pivots' but uses neural verification rather than formal solvers — SICA provides formal satisfiability guarantees where ROMA uses learned signals. Draft-and-Prune (D&P, March 2026) improves autoformalization reliability by independently pruning paths with internal contradictions and aggregating survivors via majority voting, but does not perform cross-path constraint checking — its authors note they 'aggregate predictions at the answer level and do not cluster or de-duplicate candidates by symbolic equivalence.' Meanwhile, VERGE (Jan 2026) verifies and refines a single LLM output by decomposing it into atomic claims, checking joint satisfiability via Z3, and using Minimal Correction Subsets (MCS) to provide targeted refinement feedback — but operates on one output, not across reasoning paths. In the adjacent cross-output verification space, 'Quantifying Cross-Query Contradictions' (arXiv 2604.14525, April 2026) uses Z3 (QF_UFLIA) and CaDiCaL for cross-query consistency checking with unsat-core repair, but addresses cross-query consistency (different questions sharing a case file) rather than cross-trace consistency (same question, multiple paths). Single-solution formal verification (MATH-VF uses CAS+Z3; SAFE uses Lean4; PRoSFI uses Lean/Z3/Prover9 for structured formal intermediaries on 7B models; FoVer (arXiv 2505.15960) uses Z3+Isabelle for PRM training data with cross-task generalization to BBH) improves reliability but none cross-validate across solutions.\n\nSICA fills this gap by extracting typed symbolic assertions from K sampled reasoning traces, routing them to appropriate solvers via assertion-level theory-aware dispatch (Z3 for linear arithmetic and propositional logic; SymPy for nonlinear polynomial and algebraic constraints — finer-grained than the EACL 2026 problem-level solver routing), and using Z3's built-in weighted partial MAX-SAT optimization to find the largest jointly satisfiable assertion set weighted by cross-solution frequency. SICA's MAX-SAT consensus across paths is the cross-path counterpart to VERGE's within-output MCS (dual operations: MAX-SAT keeps the maximum consistent subset; MCS removes the minimum inconsistent subset), and differs from cross-query contradiction checking by operating on multiple traces for the same question via weighted consensus rather than unsat-core repair across different questions. A three-tier extraction quality pipeline (syntactic validation, semantic spot-checking targeting the unfaithfulness patterns identified by 'Do LLMs Game Formalization?' (arXiv 2604.19459), and coverage tracking) addresses the documented task-dependence of autoformalization.\n\nWe explicitly acknowledge a fundamental limitation: SICA's MAX-SAT consensus catches contradictory constraints but cannot detect universally-wrong-but-consistent constraints caused by correlated extraction errors — the same correlated error phenomenon documented by 'Consensus is Not Verification.' The semantic spot-checking tier partially mitigates this, but correlated biases between the extractor and judge LLMs limit its effectiveness. We include FOLIO as a diagnostic ablation and propose a correlated extraction error analysis to empirically characterize this boundary.\n\nWe adopt a dual-track evaluation plan with a concrete day-by-day timeline. Track A (EMNLP 2026, ARR May 25 — 14-day sprint): Days 1-3 pipeline implementation, Days 4-6 core experiments, Days 7-8 ablations/analysis, Days 9-10 figures/tables, Days 11-13 paper writing, Day 14 submission. Full scope: K=12 on MATH-500, AIME 2024, AIME 2025 (identical pipeline to AIME 2024, trivially low marginal cost), ProofWriter, FOLIO, and 3 BBH subtasks (logical deduction, tracking shuffled objects, temporal sequences). Minimum viable scope (fallback if BBH extraction unreliable or timeline slips): 5 benchmarks — MATH-500, AIME 2024, AIME 2025, ProofWriter, FOLIO — which preserves all core contributions while saving ~1.5 days. There is no June ARR cycle (ARR uses 10-week cycles); if May 25 is missed, AAAI 2027 (paper deadline: August 1) serves as the fallback venue with full Track A+B evaluation. Track B (AAAI 2027): expanded to K=16 with GPQA Diamond, LogiQA 2.0, Qwen3-32B cross-model ablation, and any benchmarks deferred from Track A. The centerpiece experiment is a contradiction frequency analysis measuring how often statistical consensus retains logically contradictory constraint pairs. FOLIO serves as a diagnostic ablation where SMT is documented to hurt (-44.5%). Primary contributions: formal soundness guarantees, interpretable constraint-level provenance, empirically-quantified detection of contradictory consensus that both statistical methods and per-path pruning miss, systematic domain analysis of formal cross-solution verification, and honest characterization of the correlated extraction error limitation. Auto-mode compute fits within 200h H100 budget at K=12 with 6+3 benchmarks (full scope) or ~130h H100 with 5 benchmarks (minimum viable scope).",
  "project_name": "symb_invariant_consensus",
  "source": "web_research"
}
```

## Summary of changes (minor revision)

**Issue 1 — Day-by-day timeline**: Added a detailed 14-day sprint plan (May 12–25) broken into 6 phases: implementation (Days 1–3), core experiments (Days 4–6), ablations (Days 7–8), analysis/figures (Days 9–10), paper writing (Days 11–13), buffer/submission (Day 14). Includes an honest assessment that 3 days for paper writing is aggressive but feasible. Critically, I verified that **there is no June ARR cycle** — ARR operates on 10-week cycles, and May 25 is the last cycle eligible for EMNLP 2026 (commitment deadline: August 2). The fallback is AAAI 2027 (paper deadline: August 1), providing 11 additional weeks.

**Issue 2 — Minimum viable scope**: Defined a 5-benchmark fallback (MATH-500, AIME 2024, AIME 2025, ProofWriter, FOLIO) that drops BBH subtasks, saving ~1.5 days while preserving all core contributions. Under this scope, the timeline relaxes to include 3 full days for paper writing plus 4 days of buffer.

**Issue 3 — AIME 2025 moved to Track A**: Now included in Track A with explicit justification that it shares the identical extraction prompt and solver routing pipeline as AIME 2024, making it trivially low marginal cost. It also strengthens the submission by providing a generalization test on unseen competition problems.

**Minor — ROMA citation**: Added a full paragraph in the landscape section positioning ROMA (arXiv 2509.21549, NeurIPS 2025 Workshop FoRLM; ICLR 2026 Workshop RSI) as the neural counterpart to SICA's formal cross-path analysis. Added to key_references and description. The distinction is clean: ROMA uses learned signals on natural-language decision pivots; SICA provides formal satisfiability guarantees on typed symbolic constraints.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47145270-ca45-49ff-9906-2214d3bccbfa",
  "isSidechain": false,
  "requestId": "req_011Cawiu8jYDz6r2BQrhpJae",
  "type": "assistant",
  "uuid": "df787454-d751-44a7-a8a0-80cccc6547a6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kqg6N2hkAfkqsr5P1rVPGB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 86,
      "cache_read_input_tokens": 60414,
      "output_tokens": 11418,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 86,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11418,
          "cache_read_input_tokens": 60414,
          "cache_creation_input_tokens": 86,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 86
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Runtime record

_source line 50_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"Formally-Verified Intermediate Constraint Consensus Across Reasoning P…",
  "leafUuid": "df787454-d751-44a7-a8a0-80cccc6547a6",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise SICA feasibility with realistic timeline and minimum viable scope",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"Formally-Verified Intermediate Constraint Consensus Across Reasoning P…",
  "leafUuid": "df787454-d751-44a7-a8a0-80cccc6547a6",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3"
}
```

---

### Runtime record

_source line 53_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise SICA feasibility with realistic timeline and minimum viable scope",
  "sessionId": "6e18159e-4361-484e-8c9a-27485b1e4ea3"
}
```

---
