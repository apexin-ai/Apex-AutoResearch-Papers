# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-11 (UTC).** ## Original idea { "tit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-2/7a04977f-b53a-45e0-8aa0-46eb4874f6b0.jsonl`
- **Structured JSON:** [`2e95bbcc4fac9168b465.json`](../../sessions/2e/2e95bbcc4fac9168b465.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-12T00:44:54.304Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-12T00:44:54.304Z",
  "sessionId": "7a04977f-b53a-45e0-8aa0-46eb4874f6b0",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-11 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Formally-Verified Intermediate Constraint Consensus Across Reasoning Paths\",\n  \"core_problem\": \"Recent work (CRAFT, PoLR, Draft-and-Prune) demonstrates that intermediate reasoning step consensus or pruning across candidate solutions provides stronger signals than answer-level majority voting. However, existing methods either rely on statistical similarity that cannot distinguish popular-but-contradictory constraints (CRAFT's TF-IRF/Jaccard), or prune individual paths based on internal consistency without cross-validating constraints across solutions (Draft-and-Prune's per-path |S|=0/|S|>1 checks). Meanwhile, single-output formal verification systems (MATH-VF, SAFE, FoVer, PRoSFI, VERGE) verify constraints within one solution or output but do not cross-validate across multiple reasoning paths, and cross-query consistency checking (arXiv 2604.14525) verifies coherence across different questions but not across multiple traces for the same question. Furthermore, 'Consensus is Not Verification' (arXiv 2603.06612) demonstrates that consensus-based aggregation fails for truthfulness because LLM errors are strongly correlated — but crucially, aggregation improves performance when a verifier exists. Can formally verifying cross-solution intermediate constraints via SMT solving and computer algebra yield more reliable consensus with interpretable provenance, and how frequently does statistical consensus actually retain contradictory constraints in practice?\",\n  \"opportunity\": \"CRAFT (arXiv 2604.14121, April 2026) builds a Reasoning Knowledge Graph from consensus intermediate steps using TF-IRF and Jaccard similarity, achieving significant accuracy improvements. However, CRAFT's authors explicitly acknowledge two key limitations: (1) 'consensus ≠ correctness' — frequently appearing steps can amplify shared errors, and (2) 'reduced effectiveness on symbolic math' due to lexical overlap bias in Jaccard similarity. This concern is empirically grounded by 'Consensus is Not Verification' (arXiv 2603.06612, March 2026), which demonstrates that LLM errors are strongly correlated across samples and even across model families — correlation persists even with random string conditioning — causing polling-style aggregation to yield no consistent accuracy gains over single-sample baselines. Critically, however, the paper finds that 'aggregation improves performance when a verifier exists, but it cannot serve as a verifier substitute,' directly motivating SICA's approach of introducing formal verification into the consensus process.\\n\\nDraft-and-Prune (D&P, arXiv 2603.17233, March 2026) addresses autoformalization brittleness by generating multiple natural-language plans, conditioning program generation on them, pruning individually contradictory or ambiguous formalizations (paths where the solver returns |S|=0 or |S|>1), and aggregating surviving paths via answer-level majority voting. D&P achieves strong results on logical reasoning benchmarks (AR-LSAT 78.43%, ProofWriter 98.33% with GPT-4), but its pruning operates independently on each path — it cannot detect cross-path contradictions where two individually valid paths assert mutually inconsistent constraints. D&P's authors explicitly note a limitation: 'We aggregate predictions at the answer level and do not cluster or de-duplicate candidates by symbolic equivalence.'\\n\\nA parallel line of work verifies individual solutions or outputs formally — MATH-VF (arXiv 2505.20869) uses CAS+Z3 for step-level verification on single solutions; SAFE (ACL 2025) uses Lean4 for retrospective step-aware verification; PRoSFI (arXiv 2603.29500) trains process rewards over structured formal intermediaries verified by Lean/Z3/Prover9, operating on individual 7B-model solutions. VERGE (arXiv 2601.20055, Jan 2026) is a single-output verify-and-refine framework that decomposes an LLM output into atomic claims, autoformalizes them, verifies joint satisfiability via Z3, and uses Minimal Correction Subsets (MCS) to provide targeted feedback for iterative refinement. VERGE's 'multi-model consensus' refers to K=3 candidate formalizations of a single claim checked for semantic equivalence — not cross-path reasoning aggregation. FoVer (arXiv 2505.15960, ACL 2026 Findings) uses Z3 and Isabelle for step-level error annotation in individual solutions for PRM training, demonstrating cross-task generalization to BBH subtasks (temporal sequences, tracking shuffled objects, word sorting). In the adjacent cross-output verification space, 'Quantifying Cross-Query Contradictions' (arXiv 2604.14525, April 2026) uses Z3 (QF_UFLIA) and CaDiCaL for cross-query consistency checking with unsat-core localization and counterexample-guided repair — but addresses cross-query consistency (different questions sharing a case file), not cross-trace consistency (same question, multiple reasoning paths). The EACL 2026 dynamic solver routing framework (arXiv 2510.06774) selects solvers at the problem level. But none of these methods formally cross-validate intermediate constraints across multiple candidate solutions for the same problem.\\n\\nThe gap: no method formally cross-validates intermediate constraints across multiple candidate solutions to produce a consistency-aware consensus signal with interpretable provenance. Concretely, SICA differs from D&P by extracting constraints from ALL paths and finding a globally consistent MAX-SAT-optimal subset (cross-path aggregation), rather than independently pruning paths with internal contradictions (per-path filtering). SICA differs from VERGE by applying MAX-SAT across multiple reasoning paths for answer selection, whereas VERGE applies the dual MCS operation within a single output for refinement feedback. SICA differs from the cross-query contradictions framework by operating on multiple traces for the same question (cross-trace scope) using weighted partial MAX-SAT for consensus, rather than on different questions in a case file (cross-query scope) using unsat-core repair. A key empirical question — how frequently does statistical consensus actually retain contradictory constraints? — remains unanswered and is central to quantifying this opportunity.\\n\\nRecent work on autoformalization faithfulness further motivates SICA's extraction quality pipeline: 'Do LLMs Game Formalization?' (arXiv 2604.19459, VerifAI-2 Workshop, ICLR 2026) shows that high compilation rates should not be equated with faithful reasoning, finding that two-stage formalization pipelines reveal distinct unfaithfulness patterns (axiom fabrication, premise mistranslation) that evade standard verification. This underscores the need for SICA's multi-tier extraction validation.\",\n  \"landscape\": \"Standard self-consistency (Wang et al., ICLR 2023) performs majority voting on final answers and shows diminishing returns on frontier models — gains plateau at <2% with accuracy sometimes declining at high sample counts (arXiv 2511.00751). 'Consensus is Not Verification' (arXiv 2603.06612, March 2026) provides a theoretical explanation: LLM errors are strongly correlated across samples and model families, causing consensus to reinforce shared misconceptions rather than converge on truth; however, the paper finds aggregation succeeds when an external verifier exists. CRAFT (arXiv 2604.14121, April 2026) extracts consensus intermediate steps via a Reasoning Knowledge Graph using TF-IRF/Jaccard similarity and topological generation, achieving up to +8.5% accuracy over SC baselines on GSM8K, FOLIO, FLD, and OlympiadBench with K=3 traces; its authors note 'consensus ≠ correctness' and 'reduced effectiveness on symbolic math' as limitations. PoLR (ICLR 2026) uses prefix consensus to prune reasoning paths, matching SC accuracy while reducing token usage by 50-60%.\\n\\nCross-path intermediate-step analysis with neural verification: 'Correct Reasoning Paths Visit Shared Decision Pivots' (ROMA, arXiv 2509.21549, NeurIPS 2025 Workshop FoRLM; ICLR 2026 Workshop RSI) hypothesizes that correct reasoning paths converge on shared 'decision pivots' — minimal, verifiable checkpoints that any correct path must visit. ROMA mines these pivots across K sampled reasoning paths and uses a learned verifier to distill pivot-focused short-path reasoning, evaluating on LogiQA, MedQA, and MATH-500. ROMA occupies the adjacent conceptual space of cross-path intermediate-step consensus but uses neural verification (a trained pivot verifier) rather than formal solvers. SICA provides formal satisfiability guarantees where ROMA uses learned signals, and operates on typed symbolic constraints rather than natural-language decision pivots — the approaches are complementary, with ROMA better suited to domains where formalization is intractable and SICA to domains with extractable logical structure.\\n\\nDraft-and-Prune (D&P, arXiv 2603.17233, March 2026): An inference-time framework that drafts multiple natural-language plans, conditions program generation on them, prunes executable but contradictory (|S|=0) or ambiguous (|S|>1) formalizations independently for each path, and aggregates surviving paths via answer-level majority voting. Uses Z3Py for AR-LSAT/LogicalDeduction and PyKe for ProofWriter/PrOntoQA. Achieves AR-LSAT 78.43%, ProofWriter 98.33%, PrOntoQA 99.32%, LogicalDeduction 99.50% (GPT-4). Key limitation: no cross-path constraint checking or equivalence-aware deduplication.\\n\\nVERGE (arXiv 2601.20055, Jan 2026): A single-output neurosymbolic verify-and-refine loop. Decomposes an LLM output into atomic claims, classifies them by type, autoformalizes into FOL, and verifies joint satisfiability via Z3. Uses semantic routing (symbolic solvers for logical claims, LLM ensembles for commonsense) and Minimal Correction Subsets (MCS) for precise error localization, providing actionable feedback for iterative refinement. VERGE's K=3 refers to candidate formalizations of a single claim checked for semantic equivalence, not multiple reasoning paths. MCS (minimum claims to remove for satisfiability) is dual to MAX-SAT (maximum satisfiable subset) but is applied within one output for feedback, not across paths for consensus. Evaluated on FOLIO (84.7-89.2%), ProofWriter (85.2-93.0%), AR-LSAT (88.6-91.7%) across GPT-OSS-20B, GPT-OSS-120B, and Claude 3.7 Sonnet.\\n\\nSingle-solution formal verification: MATH-VF (arXiv 2505.20869, May 2025) uses a Formalizer+Critic pipeline with CAS and Z3 SMT solver for step-level verification on individual solutions, evaluated on MATH-500 and ProcessBench. SAFE (ACL 2025, arXiv 2506.04592) uses Lean4 for retrospective step-aware formal verification of individual reasoning chains, introducing the FormalStep benchmark (30,809 formal statements). PRoSFI (arXiv 2603.29500, March 2026) — 'Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries' — trains process rewards over structured formal intermediaries verified by Lean tactics, Z3, and Prover9, operating on individual 7B-model solutions; achieves 92.97% accuracy / 76.07% GPT Soundness on ProverQA-Hard. FoVer (arXiv 2505.15960, ACL 2026 Findings) — 'Training Step-Level Reasoning Verifiers with Formal Verification Tools' — uses Z3 and Isabelle for step-level error annotation in individual solutions for PRM training; demonstrates cross-task generalization to BBH subtasks (temporal sequences 97.2%, tracking shuffled objects 96.0%, word sorting 46.8% with Llama3.1-8B-PRM at Best-of-7) and to MATH, AIME, ANLI, MMLU-Pro.\\n\\nCross-output consistency verification: 'Quantifying Cross-Query Contradictions in Multi-Query LLM Reasoning' (arXiv 2604.14525, April 2026) addresses cross-query consistency — maintaining a globally satisfiable belief state across interdependent queries sharing a case file. Uses Z3 v4.8.17 (QF_UFLIA theory) and CaDiCaL for SAT, with unsat-core localization and counterexample-guided lexicographic repair. Achieves SetCons improvement from 0.56 to 0.94 across 390 case files spanning relational/SAT, temporal/SMT, policy/rules, and abductive domains. Crucially, this operates at cross-query scope (different questions sharing context) rather than cross-trace scope (same question, multiple reasoning paths), and uses unsat-core repair rather than weighted partial MAX-SAT consensus. SICA's differentiators are: cross-trace scope, intermediate constraint extraction from reasoning steps, and popularity-weighted MAX-SAT for answer selection.\\n\\nSolver routing: The EACL 2026 dynamic solver composition framework (arXiv 2510.06774) automatically identifies formal reasoning strategies and routes to specialized solvers at the problem level, achieving 27% improvement over GPT-4o. SICA's theory-aware routing operates at the finer-grained assertion level.\\n\\nVeriCoT (Nov 2025) formalizes individual CoT traces into FOL for entailment checking without cross-solution comparison. FregeLogic (SemEval 2026) uses Z3 as a tiebreaker for syllogistic validity.\\n\\nAutoformalization reliability: Grammars of Formal Uncertainty (NeurIPS 2025) demonstrates that SMT autoformalization is task-dependent: +34.8% on ProofWriter but -44.5% on FOLIO, necessitating careful benchmark selection and per-domain extraction analysis. 'Do LLMs Game Formalization?' (arXiv 2604.19459, VerifAI-2 Workshop, ICLR 2026) evaluates faithfulness of LLM autoformalization on 303 FOL problems, finding that high compilation rates (87-99%) do not guarantee faithful reasoning — two-stage pipelines reveal distinct unfaithfulness patterns: axiom fabrication (GPT-5) and premise mistranslation (DeepSeek-R1). Autoformalization surveys (arXiv 2505.23486) report ~70% success rate on physics kinematics, with selective verification reducing errors by 14-100% with minimal abstention.\\n\\nNo concurrent work (searched arXiv and OpenReview through May 2026) formally cross-validates intermediate constraints across multiple candidate solutions for the same problem.\",\n  \"approach\": \"We propose Symbolic Invariant Consensus Aggregation (SICA): given a problem, sample K reasoning paths from a frontier open-source reasoning model (QwQ-32B via vLLM on 1-2 A100s; Qwen3-32B as secondary model for ablation), then use a prompted LLM extractor to parse each trace into typed symbolic assertions (equations, inequalities, logical predicates). SICA introduces four key technical components:\\n\\n(1) **Theory-aware assertion-level solver routing**: Extracted assertions are classified by constraint type and routed to appropriate solvers — Z3 for tractable theories (linear arithmetic, propositional logic, uninterpreted functions, bitvectors) and SymPy for nonlinear polynomial arithmetic, algebraic equivalence, and modular arithmetic. Unlike the EACL 2026 framework (arXiv 2510.06774) which routes at the problem level, SICA routes at the assertion level, enabling mixed-theory problems where individual steps span different solver domains (common in competition math). Assertions that neither solver can handle receive numerical spot-checking as fallback, with unverifiable assertions flagged and excluded from the consensus set (rather than silently included).\\n\\n(2) **Weighted partial MAX-SAT for invariant consensus**: Rather than enumerating assertion subsets (exponential worst-case), SICA leverages Z3's built-in optimization context to solve weighted partial MAX-SAT directly. Each unique assertion (deduplicated via solver-verified equivalence) is weighted by its cross-solution frequency. The optimizer finds the largest jointly satisfiable subset of assertions, weighted by popularity — a single Z3 optimization call replaces exponential subset enumeration. Per-query timeout caps (10s) bound worst-case latency. This cross-path MAX-SAT consensus is the key differentiator from Draft-and-Prune (D&P), which prunes paths independently based on internal consistency (|S|=0 or |S|>1) and aggregates surviving answers via majority voting without cross-path constraint checking. It is also distinct from VERGE's MCS, which is the dual operation (minimum claims to remove) applied within a single output for refinement feedback rather than across paths for answer selection. It further differs from the cross-query contradictions framework (arXiv 2604.14525), which uses unsat-core localization and counterexample-guided repair across different questions sharing a case file — SICA uses weighted partial MAX-SAT across different reasoning traces for the same question.\\n\\n(3) **Invariant-backed answer scoring**: Each candidate answer is scored by the coverage and weight of its supporting assertions within the MAX-SAT-optimal consistent set, yielding a continuous invariant consensus score. This captures partial structural agreement even when final answers diverge, and provides interpretable provenance (each score is backed by a specific set of formally verified constraints).\\n\\n(4) **Extraction quality assurance pipeline**: To address the documented task-dependence of autoformalization (Grammars of Formal Uncertainty, NeurIPS 2025) and the unfaithfulness risks identified by 'Do LLMs Game Formalization?' (arXiv 2604.19459), we implement a three-tier extraction quality pipeline: (a) syntactic validation — each extracted assertion must parse in the target solver's input language; (b) semantic spot-checking — a random 20% of assertions are checked against the original natural language step via an LLM judge for semantic fidelity, specifically targeting the axiom fabrication and premise mistranslation failure modes identified in the faithfulness literature; (c) coverage tracking — we report 'verifiable assertion coverage' (% of extracted assertions that successfully enter the MAX-SAT pipeline) per benchmark as a first-class metric. Extraction failures cascade to numerical fallback or abstention, preventing malformed inputs from corrupting the consensus signal.\\n\\n**Limitations of formal cross-validation**: SICA's MAX-SAT consensus catches contradictory constraints but cannot detect universally-wrong-but-mutually-consistent constraints caused by correlated extraction errors. 'Consensus is Not Verification' (arXiv 2603.06612) demonstrates that LLM errors are strongly correlated across samples and even across model families, which implies that if all K paths produce the same wrong formalization of a constraint, MAX-SAT will see K consistent-but-wrong assertions and cannot flag the error. This is a fundamental limitation of any approach combining LLM extraction with formal verification: the verifier guarantees consistency, not correctness of the extraction. SICA's semantic spot-checking tier partially mitigates this — by sampling 20% of assertions for LLM-judge semantic fidelity checks, it can catch systematic mistranslation patterns. However, if the extraction LLM and the judge LLM share the same correlated bias (as the correlated errors literature suggests is likely), the mitigation is incomplete. We acknowledge this limitation explicitly and note two potential future mitigations: (a) using structurally diverse extractor models (e.g., symbolic parsers alongside LLM extractors) to decorrelate extraction errors, and (b) grounding extracted constraints against external knowledge sources (CAS simplification, unit-test-style numerical spot-checking) that do not share LLM inductive biases. We include FOLIO as a diagnostic ablation where SMT autoformalization is documented to hurt (-44.5%), precisely to empirically characterize the boundary between domains where SICA's extraction is faithful enough to help versus where correlated errors dominate.\\n\\n**Day-by-day Track A timeline (14-day sprint, May 12–25)**:\\n\\n- *Days 1–3 (May 12–14): Pipeline implementation.* Day 1: extraction prompt development for math domains (MATH-500, AIME) and logical domains (ProofWriter, FOLIO) — two prompt templates covering all benchmarks. Day 2: solver routing infrastructure (Z3 + SymPy dispatch, MAX-SAT wrapper using Z3's optimization context, equivalence deduplication). Day 3: end-to-end pipeline integration and smoke testing on 50 problems from MATH-500.\\n- *Days 4–6 (May 15–17): Core experiments.* Day 4: MATH-500 (K=12) + AIME 2024 (K=12) + AIME 2025 (K=12) — all share the math extraction prompt; batched vLLM inference across 2 A100s. Day 5: ProofWriter (K=12) — direct D&P/VERGE comparison benchmark. Day 6: FOLIO (K=12, negative diagnostic) + begin BBH subtasks if pipeline stable.\\n- *Days 7–8 (May 18–19): Ablations and additional experiments.* Day 7: BBH subtasks (3 configs × K=12) if extraction quality validates; otherwise, begin ablation suite (K sweep, extraction noise injection). Day 8: Contradiction frequency analysis (centerpiece experiment) across all completed benchmarks; correlated extraction error measurement on 100 problems per benchmark.\\n- *Days 9–10 (May 20–21): Analysis and figures.* Compile results tables, generate accuracy/calibration figures, write contradiction frequency analysis, produce extraction quality breakdown per benchmark. Compute-normalized comparison (tokens, wall-clock time).\\n- *Days 11–13 (May 22–24): Paper writing.* Day 11: Introduction, method description, related work. Day 12: Experiments, results, analysis sections. Day 13: Abstract, conclusion, formatting, supplementary material.\\n- *Day 14 (May 25): Final polish and submission.* Buffer day for last-minute fixes, ARR submission.\\n\\n**Honest assessment of timeline risk**: Paper writing in 3 days is aggressive but feasible for a focused 8-page submission with auto-generated figures and tables from Days 9–10. The main risk is pipeline debugging overrunning Days 1–3, which compresses experiment time. The minimum viable scope (below) mitigates this by defining a credible fallback that preserves 1–2 buffer days.\\n\\n**Note on ARR cycle fallback**: There is no June 2026 ARR cycle — ARR operates on 10-week cycles (~5 per year), and the May 25 cycle is the last eligible for EMNLP 2026 commitment (deadline: August 2, 2026). If the May 25 deadline is missed, the fallback is AAAI 2027 (paper deadline: August 1, 2026), which provides an additional 11 weeks and allows full Track A+B evaluation without time pressure.\\n\\n**Minimum viable scope (fallback if full plan proves too ambitious)**: If extraction quality is unreliable on BBH subtasks or timeline slips compress experiment time, the minimum credible submission is 5 benchmarks at K=12: MATH-500, AIME 2024, AIME 2025, ProofWriter, and FOLIO. This scope preserves all core contributions: (a) cross-path MAX-SAT consensus demonstrated on ProofWriter (D&P/VERGE comparison), (b) contradiction frequency analysis on math benchmarks (MATH-500, AIME 2024/2025), (c) negative diagnostic on FOLIO showing domain boundaries, (d) generalization test on unseen competition problems (AIME 2025 vs. AIME 2024), and (e) extraction quality analysis. BBH subtasks and the FoVer comparison would move to the AAAI 2027 extended version (Track B). This fallback saves ~1.5 days of experiment time (BBH extraction prompt development + 3 benchmark runs), creating headroom for pipeline debugging or additional paper writing time. Under this minimum scope, the timeline adjusts to: Days 1–3 implementation, Days 4–5 experiments (5 benchmarks), Days 6–7 ablations/analysis, Days 8–10 paper writing, Days 11–14 polish/buffer — a substantially more comfortable schedule.\\n\\n**Dual-track evaluation plan**:\\n\\n*Track A — EMNLP 2026 (ARR May 25, primary target, 14 days):* Scoped evaluation with K=12 traces on 6 core benchmarks plus 3 BBH subtasks (full scope) or 5 core benchmarks (minimum viable scope):\\n- **MATH-500** (algebraic/arithmetic reasoning; QwQ-32B ~90.6%)\\n- **AIME 2024** (competition math with mixed-theory constraints; QwQ-32B ~79.5%)\\n- **AIME 2025** (unseen competition problems; tests generalization using the identical evaluation pipeline as AIME 2024 — trivially low marginal cost since both share the same extraction prompt and solver routing)\\n- **ProofWriter** (formal logic; enables direct comparison with D&P 98.33% and VERGE 85.2-93.0%)\\n- **FOLIO** (first-order logic; diagnostic ablation — SMT autoformalization documented to hurt -44.5% here)\\n- **BBH** (3 subtasks: logical deduction, tracking shuffled objects, temporal sequences — enables direct comparison with FoVer's BBH evaluation at Best-of-7; tests cross-domain generalization to structured informal reasoning) *[included in full scope; deferred to Track B in minimum viable scope]*\\n\\nBaselines for Track A: self-consistency, CRAFT, D&P (on ProofWriter), VERGE (on ProofWriter/FOLIO).\\n\\n*Track B — AAAI 2027 (abstract deadline: July 25, paper deadline: August 1, 2026; extended version):* Expanded to K=16 traces on all Track A benchmarks plus:\\n- **GPQA Diamond** (graduate-level science; QwQ-32B ~65.2%; per-domain reporting for physics/chemistry vs. biology)\\n- **LogiQA 2.0** (natural language logical reasoning; 8,678 questions; tests constraint extraction beyond math/formal logic)\\n- BBH subtasks (if deferred from Track A) and full ablation suite\\n- Qwen3-32B cross-model ablation\\n\\n**ARC-Challenge exclusion justification**: ARC-Challenge (Clark et al., 2018) consists of multiple-choice grade-school science questions that primarily test factual knowledge retrieval (e.g., 'Which mineral is the hardest?', 'What happens when water freezes?'). Most questions lack the multi-step constraint structure required for meaningful symbolic assertion extraction — they involve domain knowledge rather than chains of extractable equations, inequalities, or logical predicates. Including ARC-Challenge would likely yield near-zero verifiable assertion coverage, providing no insight beyond confirming SICA's domain specificity (which FOLIO already demonstrates as a negative diagnostic). We note this scope limitation explicitly.\\n\\n**Metrics and analyses**:\\n- Primary: accuracy, calibration (ECE), informativeness of partial invariant agreement when candidates disagree\\n- **Contradiction frequency analysis** (centerpiece experiment): For each problem across all benchmarks, we measure how often CRAFT's statistical consensus retains logically contradictory constraint pairs. We report the 'contradiction rate' — the fraction of problems where at least one pair of popular constraints (appearing in ≥3 of K traces) are mutually unsatisfiable. If >15%, this validates SICA's core motivation; if <5%, we honestly acknowledge limited practical impact on this axis and emphasize interpretability/provenance instead.\\n- **D&P comparison**: On ProofWriter (shared benchmark), we compare SICA's cross-path MAX-SAT consensus against D&P's per-path pruning + answer-level voting, specifically measuring: (a) how many problems have cross-path contradictions that D&P's per-path pruning misses, and (b) whether MAX-SAT-backed scoring outperforms answer-level majority voting among surviving paths.\\n- **FoVer comparison on BBH** (full scope only): On the 3 shared BBH subtasks, we compare SICA's inference-time cross-path consensus against FoVer's training-time PRM approach (Llama3.1-8B-PRM at Best-of-7: temporal 97.2%, tracking 96.0%, word sorting 46.8%), analyzing whether cross-path formal consensus provides complementary signal to trained process reward models.\\n- **Extraction accuracy ablation**: Per-benchmark measurement of (a) syntactic parse rate, (b) semantic fidelity (manual annotation on 100 samples per benchmark), and (c) error propagation analysis — how X% extraction error degrades MAX-SAT consensus quality via controlled noise injection. Per the findings of 'Do LLMs Game Formalization?', we specifically track axiom fabrication and premise mistranslation rates.\\n- **Correlated extraction error analysis**: On a subset of problems (100 per benchmark), we measure cross-path extraction agreement — the fraction of assertions that are semantically equivalent across all K traces — to empirically quantify the degree of correlated extraction and assess how much independent signal SICA's MAX-SAT actually receives.\\n- **Compute-normalized comparison**: Report total tokens generated, wall-clock time per problem, and decomposed latency (inference, extraction, solver, MAX-SAT) for each method. Plot accuracy vs. total compute (tokens) curves. If SICA takes 5x compute of vanilla SC for +2% accuracy, we justify via interpretability/soundness or acknowledge the tradeoff.\\n\\nThe primary contribution is not raw accuracy improvement over SC (which has diminishing returns on frontier models) but rather: (a) formal soundness guarantees on the consensus signal, (b) interpretable constraint-level provenance for each answer, (c) detecting logically inconsistent popular reasoning steps that both statistical consensus (CRAFT) and per-path pruning (D&P) miss — with empirical quantification of how frequently this occurs, (d) systematic domain analysis of formal cross-solution verification including where it helps (ProofWriter, BBH logical deduction) vs. hurts (FOLIO), and (e) empirical characterization of correlated extraction errors as a fundamental limitation of LLM-based autoformalization in consensus settings.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~180-240h A100 80GB (6 benchmarks + 3 BBH subtasks × K=12 traces + extraction + ablations)\",\n      \"gpu_utilization\": \"Low (~20-30%); GPUs idle during coding, debugging solver routing, manual extraction annotation\",\n      \"timeline\": \"2-3 months\",\n      \"team\": \"1-2 researchers with formal methods and LLM experience\",\n      \"estimated_gpu_cost\": \"$235-310 (at ~$1.30/hr typical A100 spot rate)\",\n      \"h100_equivalent\": \"~90-120h H100 (well within 200h H100 budget)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~220-300h A100 80GB\",\n      \"gpu_utilization\": \"Moderate (~50-60%); agent codes and runs experiments between human review gates\",\n      \"timeline\": \"4-6 weeks (fits AAAI 2027 extended version with writing buffer)\",\n      \"team\": \"1 researcher, ~40-50min/day reviewing extraction quality, solver routing correctness, contradiction analysis, D&P comparison design, and BBH extraction quality; ~6h total for manual semantic fidelity annotation (100 samples × 6 benchmarks + 3 BBH subtasks)\",\n      \"claude_api_cost\": \"$200-400 (est. 2000-4000 Opus turns)\",\n      \"estimated_gpu_cost\": \"$285-390\",\n      \"h100_equivalent\": \"~110-150h H100 (within 200h H100 budget)\",\n      \"risk_note\": \"Solver routing heuristics require human judgment for edge cases; CRAFT replication may need prompt tuning; BBH logical deduction extraction quality needs validation\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~300-400h A100 80GB (Track A full scope: 6 benchmarks + 3 BBH subtasks × K=12 × core ablations; minimum viable scope: 5 benchmarks × K=12 saves ~40h)\",\n      \"gpu_utilization\": \"High (~85-95%); agent pipelines inference, extraction, and solving continuously; batched vLLM serving keeps GPUs saturated\",\n      \"timeline\": \"14-day sprint (May 12-25) for EMNLP 2026 ARR May 25; see day-by-day timeline in approach section. Minimum viable scope provides 1.5-day buffer by dropping BBH subtasks. If May 25 missed, fallback to AAAI 2027 (August 1) with full Track A+B evaluation over 11 additional weeks.\",\n      \"team\": \"0 (initial setup only, ~3 hours)\",\n      \"claude_api_cost\": \"$350-600 (est. 3500-6000 Opus turns)\",\n      \"estimated_gpu_cost\": \"$390-520\",\n      \"h100_equivalent\": \"~150-200h H100 (within 200h H100 budget with K=12; minimum viable scope ~120-160h H100)\",\n      \"speed_bottleneck\": \"GPU count for parallel vLLM inference across benchmarks × 12 samples; secondary bottleneck is Z3 MAX-SAT optimization time (mitigated by 10s per-query timeout)\",\n      \"risk_note\": \"Primary risk: pipeline debugging overruns Days 1-3, compressing experiment time — mitigated by minimum viable scope fallback (5 benchmarks, saves 1.5 days). Secondary risk: automated extraction may produce malformed solver input in ~10-20% of traces; without human review the agent may over-tune extraction prompts to specific benchmarks. AIME 2025 adds negligible marginal cost (identical pipeline to AIME 2024). No June ARR cycle exists — if May 25 missed, AAAI 2027 (August 1) is the fallback venue.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline: May 25, 2026 — 14 days from now; primary target with Track A scoped evaluation; last ARR cycle eligible for EMNLP 2026 commitment on August 2)\",\n    \"AAAI 2027 (abstract deadline: July 25, 2026; paper deadline: August 1, 2026 — extended version with Track B full evaluation; also serves as fallback if May 25 ARR deadline missed)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"Self-Consistency Improves Chain of Thought Reasoning in Language Models (ICLR 2023)\",\n    \"CRAFT: Correct Prediction, Wrong Steps? Consensus Reasoning Knowledge Graph for Robust Chain-of-Thought Synthesis (arXiv 2604.14121, April 2026)\",\n    \"Draft-and-Prune: Improving the Reliability of Auto-formalization for Logical Reasoning (arXiv 2603.17233, March 2026)\",\n    \"PoLR: The Path of Least Resistance — Guiding LLM Reasoning Trajectories with Prefix Consensus (ICLR 2026)\",\n    \"VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (arXiv 2601.20055, Jan 2026)\",\n    \"VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks (arXiv 2025)\",\n    \"MATH-VF: Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving (arXiv 2505.20869, May 2025)\",\n    \"SAFE: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification (ACL 2025, arXiv 2506.04592)\",\n    \"Adaptive LLM-Symbolic Reasoning via Dynamic Logical Solver Composition (EACL 2026, arXiv 2510.06774)\",\n    \"PRoSFI: Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries (arXiv 2603.29500, March 2026)\",\n    \"FoVer: Training Step-Level Reasoning Verifiers with Formal Verification Tools (arXiv 2505.15960, ACL 2026 Findings)\",\n    \"Grammars of Formal Uncertainty: When to Trust LLMs in Automated Reasoning Tasks (NeurIPS 2025)\",\n    \"FregeLogic at SemEval 2026 Task 11: Hybrid Neuro-Symbolic Architecture for Syllogistic Validity (SemEval 2026)\",\n    \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (arXiv 2604.19459, VerifAI-2 Workshop, ICLR 2026)\",\n    \"Reevaluating Self-Consistency Scaling in Multi-Agent Systems (arXiv 2511.00751)\",\n    \"Reasoning Aware Self-Consistency: Leveraging Reasoning Paths for Efficient LLM Sampling (NAACL 2025)\",\n    \"Faithful Logical Reasoning via Symbolic Chain-of-Thought (ACL 2024)\",\n    \"Autoformalization in the Era of Large Language Models: A Survey (arXiv 2505.23486, May 2025)\",\n    \"Consensus is Not Verification: Why Crowd Wisdom Strategies Fail for LLM Truthfulness (arXiv 2603.06612, March 2026)\",\n    \"Quantifying Cross-Query Contradictions in Multi-Query LLM Reasoning (arXiv 2604.14525, April 2026)\",\n    \"Correct Reasoning Paths Visit Shared Decision Pivots (ROMA, arXiv 2509.21549, NeurIPS 2025 Workshop FoRLM; ICLR 2026 Workshop RSI)\"\n  ],\n  \"description\": \"We propose Symbolic Invariant Consensus Aggregation (SICA), a method that formally cross-validates intermediate constraints extracted from multiple LLM reasoning paths to produce a soundness-guaranteed consensus signal. While CRAFT (April 2026) demonstrates the value of intermediate-step consensus via statistical similarity (TF-IRF/Jaccard), its authors explicitly acknowledge 'consensus ≠ correctness' and 'reduced effectiveness on symbolic math.' This limitation is theoretically grounded by 'Consensus is Not Verification' (arXiv 2603.06612, March 2026), which proves that LLM errors are strongly correlated across samples and model families, causing pure consensus to fail — but critically finds that 'aggregation improves performance when a verifier exists,' directly motivating SICA's approach. ROMA (arXiv 2509.21549, ICLR 2026 Workshop RSI) occupies the adjacent conceptual space of cross-path intermediate-step analysis via shared 'decision pivots' but uses neural verification rather than formal solvers — SICA provides formal satisfiability guarantees where ROMA uses learned signals. Draft-and-Prune (D&P, March 2026) improves autoformalization reliability by independently pruning paths with internal contradictions and aggregating survivors via majority voting, but does not perform cross-path constraint checking — its authors note they 'aggregate predictions at the answer level and do not cluster or de-duplicate candidates by symbolic equivalence.' Meanwhile, VERGE (Jan 2026) verifies and refines a single LLM output by decomposing it into atomic claims, checking joint satisfiability via Z3, and using Minimal Correction Subsets (MCS) to provide targeted refinement feedback — but operates on one output, not across reasoning paths. In the adjacent cross-output verification space, 'Quantifying Cross-Query Contradictions' (arXiv 2604.14525, April 2026) uses Z3 (QF_UFLIA) and CaDiCaL for cross-query consistency checking with unsat-core repair, but addresses cross-query consistency (different questions sharing a case file) rather than cross-trace consistency (same question, multiple paths). Single-solution formal verification (MATH-VF uses CAS+Z3; SAFE uses Lean4; PRoSFI uses Lean/Z3/Prover9 for structured formal intermediaries on 7B models; FoVer (arXiv 2505.15960) uses Z3+Isabelle for PRM training data with cross-task generalization to BBH) improves reliability but none cross-validate across solutions.\\n\\nSICA fills this gap by extracting typed symbolic assertions from K sampled reasoning traces, routing them to appropriate solvers via assertion-level theory-aware dispatch (Z3 for linear arithmetic and propositional logic; SymPy for nonlinear polynomial and algebraic constraints — finer-grained than the EACL 2026 problem-level solver routing), and using Z3's built-in weighted partial MAX-SAT optimization to find the largest jointly satisfiable assertion set weighted by cross-solution frequency. SICA's MAX-SAT consensus across paths is the cross-path counterpart to VERGE's within-output MCS (dual operations: MAX-SAT keeps the maximum consistent subset; MCS removes the minimum inconsistent subset), and differs from cross-query contradiction checking by operating on multiple traces for the same question via weighted consensus rather than unsat-core repair across different questions. A three-tier extraction quality pipeline (syntactic validation, semantic spot-checking targeting the unfaithfulness patterns identified by 'Do LLMs Game Formalization?' (arXiv 2604.19459), and coverage tracking) addresses the documented task-dependence of autoformalization.\\n\\nWe explicitly acknowledge a fundamental limitation: SICA's MAX-SAT consensus catches contradictory constraints but cannot detect universally-wrong-but-consistent constraints caused by correlated extraction errors — the same correlated error phenomenon documented by 'Consensus is Not Verification.' The semantic spot-checking tier partially mitigates this, but correlated biases between the extractor and judge LLMs limit its effectiveness. We include FOLIO as a diagnostic ablation and propose a correlated extraction error analysis to empirically characterize this boundary.\\n\\nWe adopt a dual-track evaluation plan with a concrete day-by-day timeline. Track A (EMNLP 2026, ARR May 25 — 14-day sprint): Days 1-3 pipeline implementation, Days 4-6 core experiments, Days 7-8 ablations/analysis, Days 9-10 figures/tables, Days 11-13 paper writing, Day 14 submission. Full scope: K=12 on MATH-500, AIME 2024, AIME 2025 (identical pipeline to AIME 2024, trivially low marginal cost), ProofWriter, FOLIO, and 3 BBH subtasks (logical deduction, tracking shuffled objects, temporal sequences). Minimum viable scope (fallback if BBH extraction unreliable or timeline slips): 5 benchmarks — MATH-500, AIME 2024, AIME 2025, ProofWriter, FOLIO — which preserves all core contributions while saving ~1.5 days. There is no June ARR cycle (ARR uses 10-week cycles); if May 25 is missed, AAAI 2027 (paper deadline: August 1) serves as the fallback venue with full Track A+B evaluation. Track B (AAAI 2027): expanded to K=16 with GPQA Diamond, LogiQA 2.0, Qwen3-32B cross-model ablation, and any benchmarks deferred from Track A. The centerpiece experiment is a contradiction frequency analysis measuring how often statistical consensus retains logically contradictory constraint pairs. FOLIO serves as a diagnostic ablation where SMT is documented to hurt (-44.5%). Primary contributions: formal soundness guarantees, interpretable constraint-level provenance, empirically-quantified detection of contradictory consensus that both statistical methods and per-path pruning miss, systematic domain analysis of formal cross-solution verification, and honest characterization of the correlated extraction error limitation. Auto-mode compute fits within 200h H100 budget at K=12 with 6+3 benchmarks (full scope) or ~130h H100 with 5 benchmarks (minimum viable scope).\",\n  \"project_name\": \"symb_invariant_consensus\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 7)\nIssues: [\"MINOR — BBH-FoVer comparison overstated: The proposal says BBH subtasks 'enable direct comparison with FoVer's BBH evaluation at Best-of-7,' but SICA tests logical deduction/tracking/temporal while FoVer tests tracking/temporal/word sorting. Direct comparison is only possible on 2 of 3 subtasks (tracking shuffled objects and temporal sequences). Logical deduction enables comparison with D&P, not FoVer. The text should say 'enables comparison with FoVer on 2 of 3 BBH subtasks (temporal sequences, tracking shuffled objects) and with D&P on logical deduction.'\", \"IMPACT WEAKNESS — No concrete worked example of SICA catching a contradiction that CRAFT/D&P miss. The contradiction frequency analysis is the centerpiece experiment, but the opportunity section argues abstractly that 'frequently appearing steps can amplify shared errors.' A single concrete example — even synthetic — showing two popular-but-contradictory constraints that CRAFT's TF-IRF/Jaccard would retain but SICA's MAX-SAT would flag, would make the motivation viscerally compelling rather than merely plausible. This is especially important because the paper's practical value hinges on this phenomenon being common.\", \"MINOR — FoVer word sorting score uncertainty: The proposal cites 46.8% for word sorting at Best-of-7. My independent verification from the latest paper HTML (v3) extracted 80.0% for this cell, though this is likely a confusion with the overall average across 6 unseen tasks (as the Round 5 reviewer identified). The proposal should cite the specific table and column to make this unambiguous (e.g., 'Table 5, Llama3.1-8B FoVer-PRM, word sorting column').\"]\nFeedback: The proposal has matured excellently over 6 rounds — all substantive issues are resolved, all references verified, the gap is genuine, and the intellectual honesty is commendable. The average score (3.875) is very close to the 4.0 threshold, dragged slightly below by feasibility (14-day timeline risk) and impact (contingent on empirical contradiction rates). Two targeted improvements could push this over:\n\n1. **Add a concrete motivating example**: In the opportunity section, construct a specific example (can be synthetic but realistic) showing: here is a math problem where two popular intermediate steps from K=12 traces are logically contradictory (e.g., one path derives x>5 while another derives x<3, but both are popular because they each appear in 4+ traces). Show that CRAFT's Jaccard similarity would retain both as consensus steps, D&P's per-path pruning would not flag either (since each is internally consistent within its path), but SICA's MAX-SAT would detect the {x>5, x<3} inconsistency and exclude the less-supported constraint. This transforms the abstract motivation into something concrete and immediately compelling — and it takes only 1-2 paragraphs.\n\n2. **Fix the BBH-FoVer comparison claim**: Change 'enables direct comparison with FoVer's BBH evaluation' to 'enables comparison with FoVer on 2 of 3 overlapping BBH subtasks (temporal sequences, tracking shuffled objects) and with D&P on logical deduction.' This is a one-sentence fix.\n\n3. **Optional — cite FoVer table number**: For the BBH scores (temporal 97.2%, tracking 96.0%, word sorting 46.8%), cite the specific table number from the latest version (v3) to preempt any reviewer confusion with the overall average (80.0%).\n\nThese are minor, targeted fixes. The proposal is one revision from passing.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\")."
}
```

---

### Runtime record

_source line 2 · 2026-05-12T00:44:54.309Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-12T00:44:54.309Z",
  "sessionId": "7a04977f-b53a-45e0-8aa0-46eb4874f6b0"
}
```

---

## Round 1

19 recorded events

### User

_source line 3 · 2026-05-12T00:44:54.346Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-11 (UTC).**

## Original idea
{
  "title": "Formally-Verified Intermediate Constraint Consensus Across Reasoning Paths",
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

## Reviewer feedback (round 7)
Issues: ["MINOR — BBH-FoVer comparison overstated: The proposal says BBH subtasks 'enable direct comparison with FoVer's BBH evaluation at Best-of-7,' but SICA tests logical deduction/tracking/temporal while FoVer tests tracking/temporal/word sorting. Direct comparison is only possible on 2 of 3 subtasks (tracking shuffled objects and temporal sequences). Logical deduction enables comparison with D&P, not FoVer. The text should say 'enables comparison with FoVer on 2 of 3 BBH subtasks (temporal sequences, tracking shuffled objects) and with D&P on logical deduction.'", "IMPACT WEAKNESS — No concrete worked example of SICA catching a contradiction that CRAFT/D&P miss. The contradiction frequency analysis is the centerpiece experiment, but the opportunity section argues abstractly that 'frequently appearing steps can amplify shared errors.' A single concrete example — even synthetic — showing two popular-but-contradictory constraints that CRAFT's TF-IRF/Jaccard would retain but SICA's MAX-SAT would flag, would make the motivation viscerally compelling rather than merely plausible. This is especially important because the paper's practical value hinges on this phenomenon being common.", "MINOR — FoVer word sorting score uncertainty: The proposal cites 46.8% for word sorting at Best-of-7. My independent verification from the latest paper HTML (v3) extracted 80.0% for this cell, though this is likely a confusion with the overall average across 6 unseen tasks (as the Round 5 reviewer identified). The proposal should cite the specific table and column to make this unambiguous (e.g., 'Table 5, Llama3.1-8B FoVer-PRM, word sorting column')."]
Feedback: The proposal has matured excellently over 6 rounds — all substantive issues are resolved, all references verified, the gap is genuine, and the intellectual honesty is commendable. The average score (3.875) is very close to the 4.0 threshold, dragged slightly below by feasibility (14-day timeline risk) and impact (contingent on empirical contradiction rates). Two targeted improvements could push this over:

1. **Add a concrete motivating example**: In the opportunity section, construct a specific example (can be synthetic but realistic) showing: here is a math problem where two popular intermediate steps from K=12 traces are logically contradictory (e.g., one path derives x>5 while another derives x<3, but both are popular because they each appear in 4+ traces). Show that CRAFT's Jaccard similarity would retain both as consensus steps, D&P's per-path pruning would not flag either (since each is internally consistent within its path), but SICA's MAX-SAT would detect the {x>5, x<3} inconsistency and exclude the less-supported constraint. This transforms the abstract motivation into something concrete and immediately compelling — and it takes only 1-2 paragraphs.

2. **Fix the BBH-FoVer comparison claim**: Change 'enables direct comparison with FoVer's BBH evaluation' to 'enables comparison with FoVer on 2 of 3 overlapping BBH subtasks (temporal sequences, tracking shuffled objects) and with D&P on logical deduction.' This is a one-sentence fix.

3. **Optional — cite FoVer table number**: For the BBH scores (temporal 97.2%, tracking 96.0%, word sorting 46.8%), cite the specific table number from the latest version (v3) to preempt any reviewer confusion with the overall average (80.0%).

These are minor, targeted fixes. The proposal is one revision from passing.

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "78125c4d-4052-4786-80d8-1f2e36a32df4",
  "type": "user",
  "uuid": "baa4e7cd-3871-41d3-b6e5-19c53672169c",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7a04977f-b53a-45e0-8aa0-46eb4874f6b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-12T00:44:54.341Z_

```json
{
  "parentUuid": "baa4e7cd-3871-41d3-b6e5-19c53672169c",
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
  "uuid": "4c52eae5-5e9c-4c70-9888-292f425b96cd",
  "timestamp": "2026-05-12T00:44:54.341Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7a04977f-b53a-45e0-8aa0-46eb4874f6b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-12T00:44:54.341Z_

```json
{
  "parentUuid": "4c52eae5-5e9c-4c70-9888-292f425b96cd",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "01a03abc-fc53-49a3-b579-6492e9bdc646",
  "timestamp": "2026-05-12T00:44:54.341Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7a04977f-b53a-45e0-8aa0-46eb4874f6b0",
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
  "leafUuid": "01a03abc-fc53-49a3-b579-6492e9bdc646",
  "sessionId": "7a04977f-b53a-45e0-8aa0-46eb4874f6b0"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify cross-solution constraints formally for consensus",
  "sessionId": "7a04977f-b53a-45e0-8aa0-46eb4874f6b0"
}
```

---

### Assistant

_source line 8 · 2026-05-12T00:45:08.984Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully:

1. **MINOR — BBH-FoVer comparison overstated**: The proposal claims "direct comparison with FoVer's BBH evaluation at Best-of-7" but only 2 of 3 subtasks overlap (tracking shuffled objects, temporal sequences). Logical deduction overlaps with D&P, not FoVer. Simple text fix needed.

2. **IMPACT WEAKNESS — No concrete worked example**: The reviewer wants a concrete (even synthetic) example showing two popular-but-contradictory constraints that CRAFT/D&P would miss but SICA would catch. 

3. **MINOR — FoVer word sorting score uncertainty**: Need to cite the specific table number from FoVer v3 paper.

The reviewer says the proposal is "one revision from passing" and these are "minor, targeted fixes." The average score is 3.875, close to the 4.0 threshold. Now I need to make the motivation viscerally compelling by constructing a realistic synthetic example that demonstrates the gap between existing approaches and SICA, then track down the exact FoVer citation and verify the word sorting score.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01a03abc-fc53-49a3-b579-6492e9bdc646",
  "isSidechain": false,
  "requestId": "req_011CawkSix4YBeEU5gx3n5VW",
  "type": "assistant",
  "uuid": "82476431-6948-4c5e-8ef7-90996644de89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7a04977f-b53a-45e0-8aa0-46eb4874f6b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019eScuiinG96edc6gXN7VxD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18057,
      "cache_read_input_tokens": 11841,
      "output_tokens": 730,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18057,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 730,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18057,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18057
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

_source line 9 · 2026-05-12T00:45:09.908Z_

I'll address the three reviewer issues. Let me start by researching the FoVer paper to verify the exact table reference and scores, and look for concrete examples of contradictory consensus in math reasoning.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82476431-6948-4c5e-8ef7-90996644de89",
  "isSidechain": false,
  "requestId": "req_011CawkSix4YBeEU5gx3n5VW",
  "type": "assistant",
  "uuid": "d3f566f8-3eae-4978-ac23-7fbbf20e1608",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7a04977f-b53a-45e0-8aa0-46eb4874f6b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019eScuiinG96edc6gXN7VxD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18057,
      "cache_read_input_tokens": 11841,
      "output_tokens": 730,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18057,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 730,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18057,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18057
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

_source line 10 · 2026-05-12T00:45:17.046Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01PZVTJo7P43h5KMcs1g4cTc`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "FoVer paper table verification",
  "prompt": "I need to verify specific details from the FoVer paper (arXiv 2505.15960, \"Training Step-Level Reasoning Verifiers with Formal Verification Tools\"). \n\nSpecifically:\n1. Find the exact table number that reports BBH subtask results (temporal sequences, tracking shuffled objects, word sorting) for Llama3.1-8B FoVer-PRM at Best-of-7.\n2. Verify the scores: temporal sequences 97.2%, tracking shuffled objects 96.0%, word sorting 46.8%.\n3. Check if there's any confusion between these per-subtask scores and an overall average (reportedly 80.0%).\n\nUse WebFetch to read the actual paper at https://arxiv.org/abs/2505.15960 and look for the relevant tables. Also try fetching the HTML version at https://arxiv.org/html/2505.15960v3 for better table rendering.\n\nReport the exact table number, column headers, and the specific cells I need to cite."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3f566f8-3eae-4978-ac23-7fbbf20e1608",
  "isSidechain": false,
  "requestId": "req_011CawkSix4YBeEU5gx3n5VW",
  "type": "assistant",
  "uuid": "aeb21f9d-46e9-48fe-9739-1f62a31cd781",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7a04977f-b53a-45e0-8aa0-46eb4874f6b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019eScuiinG96edc6gXN7VxD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18057,
      "cache_read_input_tokens": 11841,
      "output_tokens": 730,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18057,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 730,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 18057,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18057
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

_source line 11 · 2026-05-12T00:46:56.627Z_

<details><summary>↩ Tool result · `toolu_01PZVTJo7P43h5KMcs1g4cTc`</summary>

```text
I now have a complete and verified picture. Here is my report:

---

## Findings for FoVer Paper (arXiv 2505.15960)

### Relevant Table: Table 5

**Full caption:** "Best-of-K (K=7) performance on tasks that differ from tasks in training data of FoVer-PRMs and existing PRMs (i.e., unseen tasks)."

### Column Structure

Table 5 has three top-level column groups with sub-columns:

| Group | Sub-columns |
|-------|-------------|
| **NLI** | ANLI, HANS, Average |
| **MMLU** | Pro-NoMath |
| **BBH** | Temporal, Tracking, Sorting, Average |

### FoVer-Llama3.1-8B-PRM Row (Best-of-7)

| ANLI | HANS | NLI Avg | MMLU Pro-NoMath | Temporal | Tracking | Sorting | BBH Avg |
|------|------|---------|-----------------|----------|----------|---------|---------|
| 30.0 | 81.2 | 55.6 | 58.0 | **97.2** | **96.0** | **46.8** | **80.0** |

### Verification of Your Scores

1. **Temporal sequences: 97.2%** -- CONFIRMED. This is correct.
2. **Tracking shuffled objects: 96.0%** -- CONFIRMED. This is correct.
3. **Word sorting: 46.8%** -- CONFIRMED. This is correct, **not** 80.0%.

### The Potential Confusion (Question 3)

There is a real risk of confusing the word sorting score with the BBH average, because:

- The **BBH Sorting** column value is **46.8**.
- The **BBH Average** column (immediately adjacent, the next and last column) is **80.0**.
- The BBH Average (80.0) is the mean of Temporal (97.2), Tracking (96.0), and Sorting (46.8): (97.2 + 96.0 + 46.8) / 3 = 80.0.

So the 80.0 figure is the **BBH subtask average across all three subtasks**, not the word sorting score. The adjacency of these two columns in Table 5 makes it easy to accidentally read the average (80.0) as the sorting score. The actual word sorting score of 46.8 is notably the weakest of the three BBH subtasks for this model.

agentId: a3ab3367f4f8bbfde (use SendMessage with to: 'a3ab3367f4f8bbfde' to continue this agent)
&lt;usage>total_tokens: 15195
tool_uses: 6
duration_ms: 99574&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aeb21f9d-46e9-48fe-9739-1f62a31cd781",
  "isSidechain": false,
  "promptId": "78125c4d-4052-4786-80d8-1f2e36a32df4",
  "type": "user",
  "uuid": "474bdeb1-8f8e-417d-b9ed-4936fd71cd07",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify specific details from the FoVer paper (arXiv 2505.15960, \"Training Step-Level Reasoning Verifiers with Formal Verification Tools\"). \n\nSpecifically:\n1. Find the exact table number that reports BBH subtask results (temporal sequences, tracking shuffled objects, word sorting) for Llama3.1-8B FoVer-PRM at Best-of-7.\n2. Verify the scores: temporal sequences 97.2%, tracking shuffled objects 96.0%, word sorting 46.8%.\n3. Check if there's any confusion between these per-subtask scores and an overall average (reportedly 80.0%).\n\nUse WebFetch to read the actual paper at https://arxiv.org/abs/2505.15960 and look for the relevant tables. Also try fetching the HTML version at https://arxiv.org/html/2505.15960v3 for better table rendering.\n\nReport the exact table number, column headers, and the specific cells I need to cite.",
    "agentId": "a3ab3367f4f8bbfde",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have a complete and verified picture. Here is my report:\n\n---\n\n## Findings for FoVer Paper (arXiv 2505.15960)\n\n### Relevant Table: Table 5\n\n**Full caption:** \"Best-of-K (K=7) performance on tasks that differ from tasks in training data of FoVer-PRMs and existing PRMs (i.e., unseen tasks).\"\n\n### Column Structure\n\nTable 5 has three top-level column groups with sub-columns:\n\n| Group | Sub-columns |\n|-------|-------------|\n| **NLI** | ANLI, HANS, Average |\n| **MMLU** | Pro-NoMath |\n| **BBH** | Temporal, Tracking, Sorting, Average |\n\n### FoVer-Llama3.1-8B-PRM Row (Best-of-7)\n\n| ANLI | HANS | NLI Avg | MMLU Pro-NoMath | Temporal | Tracking | Sorting | BBH Avg |\n|------|------|---------|-----------------|----------|----------|---------|---------|\n| 30.0 | 81.2 | 55.6 | 58.0 | **97.2** | **96.0** | **46.8** | **80.0** |\n\n### Verification of Your Scores\n\n1. **Temporal sequences: 97.2%** -- CONFIRMED. This is correct.\n2. **Tracking shuffled objects: 96.0%** -- CONFIRMED. This is correct.\n3. **Word sorting: 46.8%** -- CONFIRMED. This is correct, **not** 80.0%.\n\n### The Potential Confusion (Question 3)\n\nThere is a real risk of confusing the word sorting score with the BBH average, because:\n\n- The **BBH Sorting** column value is **46.8**.\n- The **BBH Average** column (immediately adjacent, the next and last column) is **80.0**.\n- The BBH Average (80.0) is the mean of Temporal (97.2), Tracking (96.0), and Sorting (46.8): (97.2 + 96.0 + 46.8) / 3 = 80.0.\n\nSo the 80.0 figure is the **BBH subtask average across all three subtasks**, not the word sorting score. The adjacency of these two columns in Table 5 makes it easy to accidentally read the average (80.0) as the sorting score. The actual word sorting score of 46.8 is notably the weakest of the three BBH subtasks for this model."
      }
    ],
    "totalDurationMs": 99574,
    "totalTokens": 15195,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 400,
      "cache_read_input_tokens": 14172,
      "output_tokens": 622,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 400
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 622,
          "cache_read_input_tokens": 14172,
          "cache_creation_input_tokens": 400,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 400,
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
      "otherToolCount": 6
    }
  },
  "sourceToolAssistantUUID": "aeb21f9d-46e9-48fe-9739-1f62a31cd781",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7a04977f-b53a-45e0-8aa0-46eb4874f6b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-12T00:47:11.502Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Jsud2Fab1KBhPGiapcENbQ`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research contradictory consensus examples",
  "prompt": "I'm working on a research proposal about formally verifying consensus across multiple LLM reasoning paths (called SICA). A reviewer asks for a concrete worked example showing how two popular-but-contradictory intermediate constraints could survive statistical consensus (like CRAFT's TF-IRF/Jaccard similarity) but be caught by formal MAX-SAT solving.\n\nI need to construct a realistic synthetic example. Help me research:\n\n1. Search for \"CRAFT reasoning knowledge graph consensus\" and \"CRAFT arXiv 2604.14121\" to understand how CRAFT's TF-IRF/Jaccard similarity aggregates intermediate steps — what kinds of errors slip through?\n\n2. Search for common patterns of contradictory reasoning in math competition problems — e.g., where different solution approaches yield contradictory intermediate constraints (like one path deriving x > 5 while another derives x < 3).\n\n3. Search for \"self-consistency chain of thought contradictory\" or \"LLM reasoning contradictions intermediate steps\" to find documented cases of LLMs producing mutually contradictory but individually plausible reasoning steps.\n\n4. Search for \"Draft-and-Prune arXiv 2603.17233\" to understand exactly how D&P's per-path pruning works and why it wouldn't catch cross-path contradictions.\n\nUse WebSearch and WebFetch as needed. I want to construct a compelling, realistic example — not just a trivially artificial one. Report what you find about:\n- How CRAFT's similarity-based consensus works and what it misses\n- Real patterns of contradictory intermediate reasoning in math\n- Why D&P's per-path pruning is blind to cross-path contradictions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "474bdeb1-8f8e-417d-b9ed-4936fd71cd07",
  "isSidechain": false,
  "requestId": "req_011CawkbjYHBBEfYJ6AiW61E",
  "type": "assistant",
  "uuid": "38b7dd2d-96c1-4411-b9e9-491e7dcf427a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7a04977f-b53a-45e0-8aa0-46eb4874f6b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019UYyqimTmQ1uLbhT4CCmPh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1433,
      "cache_read_input_tokens": 29898,
      "output_tokens": 471,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1433,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 471,
          "cache_read_input_tokens": 29898,
          "cache_creation_input_tokens": 1433,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1433
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

_source line 13 · 2026-05-12T00:50:45.161Z_

<details><summary>↩ Tool result · `toolu_01Jsud2Fab1KBhPGiapcENbQ`</summary>

```text
I now have comprehensive research across all four areas. Here is my full report.

---

## Research Findings for SICA Worked Example

### 1. How CRAFT's TF-IRF/Jaccard Similarity Consensus Works and What It Misses

**CRAFT** (arXiv [2604.14121](https://arxiv.org/abs/2604.14121)) builds a "Consensus Reasoning Knowledge Graph" (RKG) from multiple sampled CoT traces. The pipeline has three key mechanisms:

**TF-IRF (Term Frequency -- Inverse Reasoning Frequency):** Adapted from TF-IDF. TF measures how frequently a term appears across the K traces for a single sample; IRF measures how rare that term is across different samples. A consensus term set is defined as terms whose average normalized frequency across traces exceeds threshold beta (default 0.3). This is purely lexical -- it finds terms that appear consistently across traces.

**Jaccard similarity for edge confidence:** Steps in the RKG are scored by their weighted Jaccard overlap with the consensus term set, then z-normalized within the trace group. Steps below cutoff gamma (default -1.0) are pruned as outliers. Edge confidence fuses LLM-reported scores with Jaccard overlap between connected steps.

**Three-pass consensus aggregation:**
- Pass 1: Z-score filtering removes structurally anomalous steps
- Pass 2: Per-trace RKGs are aggregated by counting cross-trace edge frequency; only edges with freq(u,v) >= theta (default 0.3) survive
- Pass 3: Isolated nodes (zero degree) are removed

**Critical failure modes the paper itself acknowledges:**

1. **"Consensus does not equal correctness"** -- On hard problems, many candidate traces share the *same wrong reasoning pattern*, so consensus amplifies rather than suppresses errors. If 7 out of 10 traces make the same algebraic mistake, that mistake passes the frequency threshold.

2. **Lexical overlap bias** -- The method "penalizes valid paraphrases and non-lexicalized reasoning (e.g., algebraic manipulations that change surface form)." Two steps that say the same thing differently get low Jaccard scores; two steps that use similar vocabulary but express contradictory constraints get high scores.

3. **Math domain weakness** -- "Intermediate mathematical results tend to be too symbolic for term-overlap methods." The constraint "x > 5" and the constraint "x < 3" share the same terms ("x", inequality symbols) and would have *high* Jaccard similarity despite being logically contradictory.

**This is the core vulnerability for your worked example:** CRAFT's Jaccard/TF-IRF consensus is structurally blind to logical contradictions expressed in similar vocabulary. Two steps like "Since f(x) is convex on [0, infinity), we require x > 5" and "Since f(x) is concave on [0, infinity), we need x < 3" share overlapping terms (f(x), [0, infinity), constraint on x) and would survive consensus filtering despite being mutually unsatisfiable.

---

### 2. Real Patterns of Contradictory Intermediate Reasoning in Math

From the literature, several concrete patterns emerge:

**Pattern A: Different inequality techniques yielding contradictory bounds.** A classic scenario from competition math: applying AM-GM to an optimization problem may yield a bound like "minimum value >= 5, achieved when x = y," while applying Cauchy-Schwarz to the same problem may (if misapplied) yield "minimum value >= 8, achieved when x = 2y." Both intermediate derivations look individually plausible but produce contradictory constraints on the equality conditions. An LLM applying AM-GM in one trace and Cauchy-Schwarz in another can derive contradictory intermediate conditions that nonetheless point to the same final numerical answer through compensating errors.

**Pattern B: Contradictory problem decompositions.** From [arXiv 2502.11574](https://arxiv.org/html/2502.11574v1), LLMs make "unwarranted assumptions that contradict problem constraints" and show "failure to propagate insights recognized mid-solution into final conclusions." A model may correctly identify that a leash wraps twice around obstacles (geometric constraint) but then compute the path length as if it wraps once -- the intermediate spatial constraint contradicts the final calculation.

**Pattern C: Self-contradictory strategic reasoning.** From [arXiv 2405.19616](https://arxiv.org/html/2405.19616v2), a Russian Roulette problem where the model states "probability of getting shot is 1 (100%)" and then says "in both scenarios, the expected outcome is the same: a 5/6 chance" -- simultaneously claiming certainty and uncertainty for the same outcome. The paper identifies "Illogical Chain of Thought" as a category: "logical inconsistencies and falsehoods within the Chain of Thought process, contradicting the final answer."

**Pattern D: Algebraic sign errors producing contradictory constraints.** When solving systems of equations, LLMs frequently produce intermediate results like deriving x + y = 7 from one equation and x + y = -3 from another (after a sign error), then proceeding to average them or pick one arbitrarily.

**For your synthetic example**, the most realistic scenario would be a competition-style optimization problem where:
- Path 1 uses AM-GM and derives the constraint that equality holds when a = b = c (symmetric case), implying a specific domain constraint
- Path 2 uses Lagrange multipliers and derives that the critical point requires a specific ratio a:b:c = 1:2:3 (asymmetric case)
- Both paths arrive at the same numerical answer (e.g., minimum = 12) through compensating errors
- The intermediate constraints (a=b=c vs. a:b:c=1:2:3) are logically contradictory

---

### 3. Why Self-Consistency (Majority Voting) Misses These Contradictions

From the original self-consistency paper ([arXiv 2203.11171](https://arxiv.org/abs/2203.11171)) and the self-contradictory reasoning study ([arXiv 2311.09603](https://arxiv.org/html/2311.09603v3)):

**Self-consistency marginalizes out reasoning paths.** It samples diverse paths and selects the most common *final answer* via majority vote. It explicitly does *not* inspect intermediate step consistency. The method treats the model as a black box that produces (reasoning, answer) pairs, and only the answer component is aggregated.

**Type 2 errors (wrong reasoning, correct answer)** are invisible to self-consistency. The self-contradictory reasoning paper found these occur at rates of 26-50% across models. If multiple paths reach "minimum = 12" via contradictory intermediate constraints, majority voting *reinforces* the answer.

**Correlated errors defeat sampling diversity.** If the LLM assigns high probability to a flawed inference rule, sampled chains replicate the same mistake. This means self-consistency's diversity assumption breaks down precisely when it matters most.

**CRAFT inherits this blindness** because its consensus is also answer-convergent: it retains steps that *co-occur frequently* across traces, not steps that are *logically consistent*. Two popular-but-contradictory intermediate steps both pass the frequency threshold.

---

### 4. How D&P's Per-Path Pruning Works and Why It Misses Cross-Path Contradictions

**Draft-and-Prune** ([arXiv 2603.17233](https://arxiv.org/abs/2603.17233)) operates in two phases:

**Drafting:** Multiple natural-language plans are generated, and each plan conditions the generation of a formal program (logical formalization).

**Pruning:** Each formalization is run through a symbolic solver. The pruning criterion is **well-definedness: |S_i| = 1**, meaning the formalization must produce exactly one feasible solution:
- |S_i| = 0 (existence failure): formalization is contradictory -- **pruned**
- |S_i| > 1 (uniqueness failure): formalization is ambiguous -- **pruned**
- |S_i| = 1: formalization is well-defined -- **retained**

**Aggregation:** Surviving paths are aggregated via majority voting: y_hat = argmax over Q_j of the count of paths producing Q_j.

**Why D&P is blind to cross-path contradictions:**

The paper explicitly states: *"All paths are independent samples; we do not perform tree search or branching within a path."* Pruning checks only whether each individual path is internally well-defined. There is **no consistency checking across different reasoning paths** before aggregation.

**Concrete failure scenario:** Path A formalizes a problem with constraint set {x > 5, y < 10, x + y = 12} and the solver finds exactly one solution (x=7, y=5) -- well-defined, retained. Path B formalizes the same problem with constraint set {x < 3, y > 8, x + y = 12} and the solver finds exactly one solution (x=2, y=10) -- also well-defined, retained. Both paths are individually consistent, but they encode *contradictory interpretations* of the same problem. D&P retains both and lets majority voting decide, never detecting that the underlying semantic interpretations are incompatible.

The paper acknowledges: *"Aggregation with equivalence awareness...does not cluster or de-duplicate candidates by symbolic equivalence."* The majority of residual errors arise from "coverage limitations" and semantically incorrect but well-defined formalizations.

---

### 5. Constructing Your Worked Example: A Synthesis

Based on all the research, here is a realistic synthetic scenario that would make a compelling example in your SICA proposal:

**Problem:** "Find the minimum value of f(a,b) = a^2/b + b^2/a for positive reals a, b with a + b = 6."

**Path 1 (AM-GM approach):**
- Step 1: Apply AM-GM to a^2/b + b^2/a >= 2*sqrt(ab) [INCORRECT application -- wrong form of AM-GM]
- Step 2: Since a + b = 6, by AM-GM, ab <= 9, so sqrt(ab) <= 3
- Step 3: Therefore minimum >= 6, achieved when a = b = 3
- **Intermediate constraint: a = b = 3, minimum = 6** [correct answer, wrong reasoning in step 1]

**Path 2 (Calculus/Lagrange approach):**
- Step 1: Substitute b = 6-a, minimize g(a) = a^2/(6-a) + (6-a)^2/a
- Step 2: g'(a) = 0 yields [computation with sign error] a = 4, b = 2
- Step 3: g(4) = 16/2 + 4/4 = 8 + 1 = 9... wait, recompute: g(3) = 9/3 + 9/3 = 6
- Step 4: Therefore minimum = 6, achieved when a = 3, b = 3
- **Intermediate constraint: initially a=4, b=2, then corrected to a=b=3, minimum = 6** [self-correction masks error]

Now consider a harder variant where the paths *don't* self-correct:

**Path 1 derives:** "Equality in AM-GM requires a = b, so the minimum is at a = b = 3" (constraint C1: a = b)

**Path 2 derives (with error):** "The critical point of the Lagrangian gives a/b = 2" (constraint C2: a = 2b)

Both paths compute minimum = 6 (Path 2 through a compensating arithmetic error). CRAFT's TF-IRF/Jaccard consensus sees both paths mention "a", "b", "minimum", "= 6", "positive reals" -- high lexical overlap. Both pass the frequency threshold. D&P's solver finds each path internally consistent (each has exactly one solution). Self-consistency sees both paths answer "6" and reinforces confidence.

**But C1 (a = b) and C2 (a = 2b) are mutually contradictory** when combined with a + b = 6. A MAX-SAT solver encoding both constraints:
- phi_1: a = b
- phi_2: a = 2b  
- phi_3: a + b = 6
- phi_4: a > 0, b > 0

This system is UNSAT. MAX-SAT identifies that {phi_1, phi_2} is a minimal unsatisfiable core -- you must drop one. This flags the cross-path contradiction that all three other methods miss.

**VERGE** ([arXiv 2601.20055](https://arxiv.org/html/2601.20055v2)) provides a real precedent for this approach: it uses Z3 SMT solvers to decompose LLM claims into atomic constraints, checks joint satisfiability, and computes MCS (Minimal Correction Subsets) when contradictions arise. The paper establishes that "finding an MCS is equivalent to finding the complement of a Maximal Satisfiable Subset (MSS)" -- directly linking to MAX-SAT.

---

### Summary of Key Findings

| Method | What it checks | What it misses |
|--------|---------------|----------------|
| **Self-consistency** | Final answer agreement across paths | All intermediate step contradictions |
| **CRAFT (TF-IRF/Jaccard)** | Lexical overlap of intermediate steps | Logically contradictory steps with similar vocabulary |
| **D&P (per-path pruning)** | Internal consistency of each path (|S|=1) | Cross-path semantic contradictions |
| **MAX-SAT/SMT (SICA)** | Joint satisfiability of all constraints | Would catch cross-path contradictions by encoding constraints formally |

Sources:
- [CRAFT: Correct Prediction, Wrong Steps?](https://arxiv.org/abs/2604.14121)
- [Draft-and-Prune](https://arxiv.org/abs/2603.17233)
- [Self-Consistency Improves Chain of Thought Reasoning](https://arxiv.org/abs/2203.11171)
- [Self-Contradictory Reasoning Evaluation and Detection](https://arxiv.org/html/2311.09603v3)
- [Easy Problems That LLMs Get Wrong](https://arxiv.org/html/2405.19616v2)
- [Large Language Models and Mathematical Reasoning Failures](https://arxiv.org/html/2502.11574v1)
- [VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning](https://arxiv.org/html/2601.20055v2)
- [SATLM: Satisfiability-Aided Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/file/8e9c7d4a48bdac81a58f983a64aaf42b-Paper-Conference.pdf)
- [Can Large Language Models Reason and Optimize Under Constraints?](https://arxiv.org/html/2603.23004)
- [When Models Ignore Definitions: Measuring Semantic Override Hallucinations](https://arxiv.org/html/2602.17520)

agentId: aa1205c9c1d0dffdd (use SendMessage with to: 'aa1205c9c1d0dffdd' to continue this agent)
&lt;usage>total_tokens: 31766
tool_uses: 21
duration_ms: 213654&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38b7dd2d-96c1-4411-b9e9-491e7dcf427a",
  "isSidechain": false,
  "promptId": "78125c4d-4052-4786-80d8-1f2e36a32df4",
  "type": "user",
  "uuid": "fca19d5b-e858-4020-8076-120e578ab9b5",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm working on a research proposal about formally verifying consensus across multiple LLM reasoning paths (called SICA). A reviewer asks for a concrete worked example showing how two popular-but-contradictory intermediate constraints could survive statistical consensus (like CRAFT's TF-IRF/Jaccard similarity) but be caught by formal MAX-SAT solving.\n\nI need to construct a realistic synthetic example. Help me research:\n\n1. Search for \"CRAFT reasoning knowledge graph consensus\" and \"CRAFT arXiv 2604.14121\" to understand how CRAFT's TF-IRF/Jaccard similarity aggregates intermediate steps — what kinds of errors slip through?\n\n2. Search for common patterns of contradictory reasoning in math competition problems — e.g., where different solution approaches yield contradictory intermediate constraints (like one path deriving x > 5 while another derives x < 3).\n\n3. Search for \"self-consistency chain of thought contradictory\" or \"LLM reasoning contradictions intermediate steps\" to find documented cases of LLMs producing mutually contradictory but individually plausible reasoning steps.\n\n4. Search for \"Draft-and-Prune arXiv 2603.17233\" to understand exactly how D&P's per-path pruning works and why it wouldn't catch cross-path contradictions.\n\nUse WebSearch and WebFetch as needed. I want to construct a compelling, realistic example — not just a trivially artificial one. Report what you find about:\n- How CRAFT's similarity-based consensus works and what it misses\n- Real patterns of contradictory intermediate reasoning in math\n- Why D&P's per-path pruning is blind to cross-path contradictions",
    "agentId": "aa1205c9c1d0dffdd",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive research across all four areas. Here is my full report.\n\n---\n\n## Research Findings for SICA Worked Example\n\n### 1. How CRAFT's TF-IRF/Jaccard Similarity Consensus Works and What It Misses\n\n**CRAFT** (arXiv [2604.14121](https://arxiv.org/abs/2604.14121)) builds a \"Consensus Reasoning Knowledge Graph\" (RKG) from multiple sampled CoT traces. The pipeline has three key mechanisms:\n\n**TF-IRF (Term Frequency -- Inverse Reasoning Frequency):** Adapted from TF-IDF. TF measures how frequently a term appears across the K traces for a single sample; IRF measures how rare that term is across different samples. A consensus term set is defined as terms whose average normalized frequency across traces exceeds threshold beta (default 0.3). This is purely lexical -- it finds terms that appear consistently across traces.\n\n**Jaccard similarity for edge confidence:** Steps in the RKG are scored by their weighted Jaccard overlap with the consensus term set, then z-normalized within the trace group. Steps below cutoff gamma (default -1.0) are pruned as outliers. Edge confidence fuses LLM-reported scores with Jaccard overlap between connected steps.\n\n**Three-pass consensus aggregation:**\n- Pass 1: Z-score filtering removes structurally anomalous steps\n- Pass 2: Per-trace RKGs are aggregated by counting cross-trace edge frequency; only edges with freq(u,v) >= theta (default 0.3) survive\n- Pass 3: Isolated nodes (zero degree) are removed\n\n**Critical failure modes the paper itself acknowledges:**\n\n1. **\"Consensus does not equal correctness\"** -- On hard problems, many candidate traces share the *same wrong reasoning pattern*, so consensus amplifies rather than suppresses errors. If 7 out of 10 traces make the same algebraic mistake, that mistake passes the frequency threshold.\n\n2. **Lexical overlap bias** -- The method \"penalizes valid paraphrases and non-lexicalized reasoning (e.g., algebraic manipulations that change surface form).\" Two steps that say the same thing differently get low Jaccard scores; two steps that use similar vocabulary but express contradictory constraints get high scores.\n\n3. **Math domain weakness** -- \"Intermediate mathematical results tend to be too symbolic for term-overlap methods.\" The constraint \"x > 5\" and the constraint \"x < 3\" share the same terms (\"x\", inequality symbols) and would have *high* Jaccard similarity despite being logically contradictory.\n\n**This is the core vulnerability for your worked example:** CRAFT's Jaccard/TF-IRF consensus is structurally blind to logical contradictions expressed in similar vocabulary. Two steps like \"Since f(x) is convex on [0, infinity), we require x > 5\" and \"Since f(x) is concave on [0, infinity), we need x < 3\" share overlapping terms (f(x), [0, infinity), constraint on x) and would survive consensus filtering despite being mutually unsatisfiable.\n\n---\n\n### 2. Real Patterns of Contradictory Intermediate Reasoning in Math\n\nFrom the literature, several concrete patterns emerge:\n\n**Pattern A: Different inequality techniques yielding contradictory bounds.** A classic scenario from competition math: applying AM-GM to an optimization problem may yield a bound like \"minimum value >= 5, achieved when x = y,\" while applying Cauchy-Schwarz to the same problem may (if misapplied) yield \"minimum value >= 8, achieved when x = 2y.\" Both intermediate derivations look individually plausible but produce contradictory constraints on the equality conditions. An LLM applying AM-GM in one trace and Cauchy-Schwarz in another can derive contradictory intermediate conditions that nonetheless point to the same final numerical answer through compensating errors.\n\n**Pattern B: Contradictory problem decompositions.** From [arXiv 2502.11574](https://arxiv.org/html/2502.11574v1), LLMs make \"unwarranted assumptions that contradict problem constraints\" and show \"failure to propagate insights recognized mid-solution into final conclusions.\" A model may correctly identify that a leash wraps twice around obstacles (geometric constraint) but then compute the path length as if it wraps once -- the intermediate spatial constraint contradicts the final calculation.\n\n**Pattern C: Self-contradictory strategic reasoning.** From [arXiv 2405.19616](https://arxiv.org/html/2405.19616v2), a Russian Roulette problem where the model states \"probability of getting shot is 1 (100%)\" and then says \"in both scenarios, the expected outcome is the same: a 5/6 chance\" -- simultaneously claiming certainty and uncertainty for the same outcome. The paper identifies \"Illogical Chain of Thought\" as a category: \"logical inconsistencies and falsehoods within the Chain of Thought process, contradicting the final answer.\"\n\n**Pattern D: Algebraic sign errors producing contradictory constraints.** When solving systems of equations, LLMs frequently produce intermediate results like deriving x + y = 7 from one equation and x + y = -3 from another (after a sign error), then proceeding to average them or pick one arbitrarily.\n\n**For your synthetic example**, the most realistic scenario would be a competition-style optimization problem where:\n- Path 1 uses AM-GM and derives the constraint that equality holds when a = b = c (symmetric case), implying a specific domain constraint\n- Path 2 uses Lagrange multipliers and derives that the critical point requires a specific ratio a:b:c = 1:2:3 (asymmetric case)\n- Both paths arrive at the same numerical answer (e.g., minimum = 12) through compensating errors\n- The intermediate constraints (a=b=c vs. a:b:c=1:2:3) are logically contradictory\n\n---\n\n### 3. Why Self-Consistency (Majority Voting) Misses These Contradictions\n\nFrom the original self-consistency paper ([arXiv 2203.11171](https://arxiv.org/abs/2203.11171)) and the self-contradictory reasoning study ([arXiv 2311.09603](https://arxiv.org/html/2311.09603v3)):\n\n**Self-consistency marginalizes out reasoning paths.** It samples diverse paths and selects the most common *final answer* via majority vote. It explicitly does *not* inspect intermediate step consistency. The method treats the model as a black box that produces (reasoning, answer) pairs, and only the answer component is aggregated.\n\n**Type 2 errors (wrong reasoning, correct answer)** are invisible to self-consistency. The self-contradictory reasoning paper found these occur at rates of 26-50% across models. If multiple paths reach \"minimum = 12\" via contradictory intermediate constraints, majority voting *reinforces* the answer.\n\n**Correlated errors defeat sampling diversity.** If the LLM assigns high probability to a flawed inference rule, sampled chains replicate the same mistake. This means self-consistency's diversity assumption breaks down precisely when it matters most.\n\n**CRAFT inherits this blindness** because its consensus is also answer-convergent: it retains steps that *co-occur frequently* across traces, not steps that are *logically consistent*. Two popular-but-contradictory intermediate steps both pass the frequency threshold.\n\n---\n\n### 4. How D&P's Per-Path Pruning Works and Why It Misses Cross-Path Contradictions\n\n**Draft-and-Prune** ([arXiv 2603.17233](https://arxiv.org/abs/2603.17233)) operates in two phases:\n\n**Drafting:** Multiple natural-language plans are generated, and each plan conditions the generation of a formal program (logical formalization).\n\n**Pruning:** Each formalization is run through a symbolic solver. The pruning criterion is **well-definedness: |S_i| = 1**, meaning the formalization must produce exactly one feasible solution:\n- |S_i| = 0 (existence failure): formalization is contradictory -- **pruned**\n- |S_i| > 1 (uniqueness failure): formalization is ambiguous -- **pruned**\n- |S_i| = 1: formalization is well-defined -- **retained**\n\n**Aggregation:** Surviving paths are aggregated via majority voting: y_hat = argmax over Q_j of the count of paths producing Q_j.\n\n**Why D&P is blind to cross-path contradictions:**\n\nThe paper explicitly states: *\"All paths are independent samples; we do not perform tree search or branching within a path.\"* Pruning checks only whether each individual path is internally well-defined. There is **no consistency checking across different reasoning paths** before aggregation.\n\n**Concrete failure scenario:** Path A formalizes a problem with constraint set {x > 5, y < 10, x + y = 12} and the solver finds exactly one solution (x=7, y=5) -- well-defined, retained. Path B formalizes the same problem with constraint set {x < 3, y > 8, x + y = 12} and the solver finds exactly one solution (x=2, y=10) -- also well-defined, retained. Both paths are individually consistent, but they encode *contradictory interpretations* of the same problem. D&P retains both and lets majority voting decide, never detecting that the underlying semantic interpretations are incompatible.\n\nThe paper acknowledges: *\"Aggregation with equivalence awareness...does not cluster or de-duplicate candidates by symbolic equivalence.\"* The majority of residual errors arise from \"coverage limitations\" and semantically incorrect but well-defined formalizations.\n\n---\n\n### 5. Constructing Your Worked Example: A Synthesis\n\nBased on all the research, here is a realistic synthetic scenario that would make a compelling example in your SICA proposal:\n\n**Problem:** \"Find the minimum value of f(a,b) = a^2/b + b^2/a for positive reals a, b with a + b = 6.\"\n\n**Path 1 (AM-GM approach):**\n- Step 1: Apply AM-GM to a^2/b + b^2/a >= 2*sqrt(ab) [INCORRECT application -- wrong form of AM-GM]\n- Step 2: Since a + b = 6, by AM-GM, ab <= 9, so sqrt(ab) <= 3\n- Step 3: Therefore minimum >= 6, achieved when a = b = 3\n- **Intermediate constraint: a = b = 3, minimum = 6** [correct answer, wrong reasoning in step 1]\n\n**Path 2 (Calculus/Lagrange approach):**\n- Step 1: Substitute b = 6-a, minimize g(a) = a^2/(6-a) + (6-a)^2/a\n- Step 2: g'(a) = 0 yields [computation with sign error] a = 4, b = 2\n- Step 3: g(4) = 16/2 + 4/4 = 8 + 1 = 9... wait, recompute: g(3) = 9/3 + 9/3 = 6\n- Step 4: Therefore minimum = 6, achieved when a = 3, b = 3\n- **Intermediate constraint: initially a=4, b=2, then corrected to a=b=3, minimum = 6** [self-correction masks error]\n\nNow consider a harder variant where the paths *don't* self-correct:\n\n**Path 1 derives:** \"Equality in AM-GM requires a = b, so the minimum is at a = b = 3\" (constraint C1: a = b)\n\n**Path 2 derives (with error):** \"The critical point of the Lagrangian gives a/b = 2\" (constraint C2: a = 2b)\n\nBoth paths compute minimum = 6 (Path 2 through a compensating arithmetic error). CRAFT's TF-IRF/Jaccard consensus sees both paths mention \"a\", \"b\", \"minimum\", \"= 6\", \"positive reals\" -- high lexical overlap. Both pass the frequency threshold. D&P's solver finds each path internally consistent (each has exactly one solution). Self-consistency sees both paths answer \"6\" and reinforces confidence.\n\n**But C1 (a = b) and C2 (a = 2b) are mutually contradictory** when combined with a + b = 6. A MAX-SAT solver encoding both constraints:\n- phi_1: a = b\n- phi_2: a = 2b  \n- phi_3: a + b = 6\n- phi_4: a > 0, b > 0\n\nThis system is UNSAT. MAX-SAT identifies that {phi_1, phi_2} is a minimal unsatisfiable core -- you must drop one. This flags the cross-path contradiction that all three other methods miss.\n\n**VERGE** ([arXiv 2601.20055](https://arxiv.org/html/2601.20055v2)) provides a real precedent for this approach: it uses Z3 SMT solvers to decompose LLM claims into atomic constraints, checks joint satisfiability, and computes MCS (Minimal Correction Subsets) when contradictions arise. The paper establishes that \"finding an MCS is equivalent to finding the complement of a Maximal Satisfiable Subset (MSS)\" -- directly linking to MAX-SAT.\n\n---\n\n### Summary of Key Findings\n\n| Method | What it checks | What it misses |\n|--------|---------------|----------------|\n| **Self-consistency** | Final answer agreement across paths | All intermediate step contradictions |\n| **CRAFT (TF-IRF/Jaccard)** | Lexical overlap of intermediate steps | Logically contradictory steps with similar vocabulary |\n| **D&P (per-path pruning)** | Internal consistency of each path (|S|=1) | Cross-path semantic contradictions |\n| **MAX-SAT/SMT (SICA)** | Joint satisfiability of all constraints | Would catch cross-path contradictions by encoding constraints formally |\n\nSources:\n- [CRAFT: Correct Prediction, Wrong Steps?](https://arxiv.org/abs/2604.14121)\n- [Draft-and-Prune](https://arxiv.org/abs/2603.17233)\n- [Self-Consistency Improves Chain of Thought Reasoning](https://arxiv.org/abs/2203.11171)\n- [Self-Contradictory Reasoning Evaluation and Detection](https://arxiv.org/html/2311.09603v3)\n- [Easy Problems That LLMs Get Wrong](https://arxiv.org/html/2405.19616v2)\n- [Large Language Models and Mathematical Reasoning Failures](https://arxiv.org/html/2502.11574v1)\n- [VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning](https://arxiv.org/html/2601.20055v2)\n- [SATLM: Satisfiability-Aided Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/file/8e9c7d4a48bdac81a58f983a64aaf42b-Paper-Conference.pdf)\n- [Can Large Language Models Reason and Optimize Under Constraints?](https://arxiv.org/html/2603.23004)\n- [When Models Ignore Definitions: Measuring Semantic Override Hallucinations](https://arxiv.org/html/2602.17520)"
      }
    ],
    "totalDurationMs": 213654,
    "totalTokens": 31766,
    "totalToolUseCount": 21,
    "usage": {
      "input_tokens": 861,
      "cache_creation_input_tokens": 812,
      "cache_read_input_tokens": 26397,
      "output_tokens": 3696,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 812
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 861,
          "output_tokens": 3696,
          "cache_read_input_tokens": 26397,
          "cache_creation_input_tokens": 812,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 812,
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
      "otherToolCount": 21
    }
  },
  "sourceToolAssistantUUID": "38b7dd2d-96c1-4411-b9e9-491e7dcf427a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7a04977f-b53a-45e0-8aa0-46eb4874f6b0",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"Formally-Verified Intermediate Constraint Consensus Across Reasoning P…",
  "leafUuid": "fca19d5b-e858-4020-8076-120e578ab9b5",
  "sessionId": "7a04977f-b53a-45e0-8aa0-46eb4874f6b0"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify cross-solution constraints formally for consensus",
  "sessionId": "7a04977f-b53a-45e0-8aa0-46eb4874f6b0"
}
```

---

### Assistant

_source line 16 · 2026-05-12T00:53:35.946Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent. Now I have all the information I need:

1. **FoVer table reference**: Table 5, BBH subtask columns. Temporal 97.2%, Tracking 96.0%, Sorting 46.8%, BBH Average 80.0%. The confusion is between the BBH Average (80.0%) and the word sorting score (46.8%).

2. **Concrete example**: I have excellent research to construct a compelling synthetic example showing contradictory constraints that CRAFT/D&P would miss but SICA would catch.

3. **BBH-FoVer comparison**: Simple text fix — only 2 of 3 subtasks overlap with FoVer.


4. **Revising the JSON**: I need to fix the BBH-FoVer comparison text to clarify that only temporal sequences and tracking shuffled objects overlap with FoVer, while logical deduction compares with D&P. For the concrete example, I'm adding a motivating scenario with a math optimization problem where two contradictory constraints (like a=b versus a=2b) would both be retained by CRAFT's Jaccard similarity approach, but SICA would identify this as a critical weakness. I'm settling on a cleaner algebra example that'll make the inconsistency obvious—a quadratic with two roots where different solution paths pick different roots based on vague criteria, leading to contradictory intermediate constraints and final answers. I'm seeing that Path B contains an error where a negative sign gets dropped, leading to incorrect intermediate values. Let me pivot to a cleaner example instead — one involving optimization with a constraint, where different solution paths can yield contradictory results.

For the problem of minimizing a²/b + b²/a subject to a + b = 6, I'm tracking two main approaches: the AM-GM method correctly identifies a = b = 3 as the minimum with value 6, while the calculus approach runs into a sign error during differentiation.

The calculus path incorrectly identifies a critical point at a = 4, b = 2, which would give a different constraint (a = 2b) and a minimum value of 9—but this contradicts the AM-GM result. I'm realizing that for SICA to be compelling, I should actually keep these divergent answers, since the contradictory constraints themselves are what would help the method identify which path is reliable. Let me reconsider what the reviewer is actually asking for regarding CRAFT's Jaccard similarity and D&P's per-path pruning behavior.

I'm constructing a cleaner example using a system of equations: 2x + y = 7 and x² + y² = 25. One path group will solve this algebraically by substitution, while another might use a different approach, and the key is that SICA's MAX-SAT formulation can detect when constraints from different paths contradict each other and exclude the less-supported ones to improve the final answer selection. I'm realizing this synthetic example is getting too complicated. Let me step back and use something much cleaner—a basic quadratic where I can clearly show how different solution paths emerge and where errors creep in.

I'll sample multiple reasoning traces through a simple problem: find positive integers x where x² - 5x + 6 = 0 and 2x + 3 is prime. Most traces factor correctly to get x = 2 or x = 3, then check the primality constraint—some catch that only x = 2 works, while others make mistakes in the primality check or miss verifying both conditions.

The key issue is that different reasoning paths extract different intermediate results as "correct," and while each path is internally consistent, they lead to conflicting final answers. Standard consistency checking methods like CRAFT's lexical similarity or D&P's path validation can't catch the primality error because they don't actually verify the mathematical claim that 9 is prime—they just see that the reasoning follows a plausible structure.

Let me try a clearer example with a geometry problem. I'm working through a rectangle problem where the perimeter is 28 and the length is 3 more than twice the width. Setting up the equations: if the width is w and length is l, then the perimeter constraint gives l + w = 14, and the relationship constraint gives l = 2w + 3. Solving these simultaneously yields w = 11/3 and l = 31/3, which produces an area of 341/9.

I'm also tracking an alternative path where the setup makes an error—forgetting to divide the perimeter by 2—which leads to l + w = 28 instead. This incorrect constraint produces w = 25/3, l = 59/3, and an area of 1475/9. A third path group arrives at the same correct answer as the first. Now I'm analyzing how these different solution paths diverge and what causes the error in the second group. ioning "perimeter", "width", "length", "2w+3". The TF-IRF scores for terms like "w", "l", "perimeter", "2w+3" are high across both groups. The Jaccard similarity between Group A's step "l + w = 14" and Group B's step "l + w = 28" is moderate — they share terms "l", "w", "=" but differ in the value. CRAFT might retain both as popular steps since they each appear in 4-5 traces.

D&P analysis: Each path is internally consistent — the solver finds exactly one (w, l) pair for each path's constraint set. Path A: |S|=1 (w=11/3, l=31/3). Path B: |S|=1 (w=25/3, l=59/3). Both survive pruning.

SICA analysis: Now I'm extracting all constraints and deduplicating them. I see φ₁ (l + w = 14) appearing in 8 traces, φ₂ (l + w = 28) in 4 traces, φ₃ (l = 2w + 3) across all 12 traces, and φ₄ (2(l + w) = 28) in 8 traces. When I apply MAX-SAT with these weights, the full constraint set becomes unsatisfiable because φ₁ and φ₂ directly contradict each other, and φ₄ actually implies φ₂.

The optimal MAX-SAT solution excludes φ₂ and keeps {φ₁, φ₃, φ₄} for a total weight of 28, which flags the l + w = 28 constraint as inconsistent with the weighted majority. This is exactly what we want — SICA correctly identifies that Group B's answer is less reliable and scores the Group A/C answer higher.

Now I'm thinking through whether CRAFT would actually keep both contradictory constraints. The issue is that CRAFT operates on term frequency, not semantic contradiction — it sees "l+w=14" appearing in 8 traces and "l+w=28" in 4 traces, so it would likely retain the more frequent one. But the real problem is that CRAFT has no way to detect logical inconsistency; it can only measure lexical overlap and popularity. In my example, both constraints actually exceed the consensus threshold of 4 traces, so CRAFT would retain both contradictory statements simultaneously, which is the core failure mode I'm trying to illustrate.

Let me think about this differently. CRAFT builds a reasoning knowledge graph where nodes are natural language steps connected sequentially. It doesn't extract symbolic constraints — it just looks at whether steps appear frequently enough across traces. So if two steps assert contradictory things but both show up in enough traces, CRAFT keeps both, creating an inconsistent consensus graph.

I should ground this in a concrete example. The reviewer mentioned one path deriving x>5 while another derives x<3. Let me use a specific MATH problem to make this concrete.

Consider a rectangle problem: perimeter is 28 and length is 3 more than twice the width. From 12 sampled traces, two different intermediate steps emerge as popular — one group derives that half the perimeter gives l + w = 14, leading to one set of dimensions and area, while another group derives l + w = 28 directly from the perimeter, leading to different dimensions and area. Both groups internally agree on the constraint l = 2w + 3, so each path is self-consistent. But CRAFT's frequency-based approach sees both equations as popular steps appearing across multiple traces, so it retains both in the consensus graph despite their contradiction.

SICA takes a different approach by extracting these as formal logical constraints and running them through a MAX-SAT solver. The solver receives four weighted formulas: the two conflicting equations about l + w, the shared constraint about l and w, and a fourth equation derived from the perimeter. Since the first two equations are mutually unsatisfiable, MAX-SAT finds the maximum-weight subset that can be satisfied together, selecting the first equation along with the other two constraints that don't conflict.

Now I'm working through the full JSON revision. I need to integrate this concrete example into the opportunity section, update the comparison language around BBH-FoVer throughout the document, and add the missing citation to Table 5. Let me go through each field systematically and make sure the changes are consistent. 's limitations. Something like:

"To illustrate concretely, consider a synthetic but realistic MATH-500 problem: 'A rectangle has perimeter 28 and its length is 3 more than twice its width. Find the area.' From K=12 sampled traces, two popular intermediate derivations emerge: C₁ (8 traces) correctly derives 'half-perimeter gives l + w = 14,' yielding area = 341/9; C₂ (4 traces) erroneously derives 'perimeter gives l + w = 28,' yielding area = 1475/9. All 12 traces share the constraint l = 2w + 3. Each path group is internally consistent (unique solution exists), so D&P's per-path pruning retains all paths. CRAFT's TF-IRF/Jaccard sees both 'l + w = 14' and 'l + w = 28' as popular steps (each appearing in ≥3 traces) with high lexical overlap, and retains both in its consensus RKG — it cannot detect the logical contradiction between them. Self-consistency majority-votes 341/9 (8 traces) over 1475/9 (4 traces), getting the right answer here but without detecting why the minority is wrong. SICA extracts formal constraints from all traces, assigns weights based on frequency, and uses a MAX-SAT solver to find the optimal subset that satisfies as many constraints as possible — it identifies that the two competing equations are unsatisfiable together and intelligibly excludes the erroneous one with clear provenance.

Now I'm working through the BBH-FoVer comparison fixes. I need to locate all the places where the benchmark overlap is mentioned and update them to be more precise about which subtasks are actually shared between the methods. I need to clarify the comparison scope: SICA and FoVer only overlap on 2 of 3 BBH subtasks—tracking shuffled objects and temporal sequences—where I can directly compare their results. Logical deduction is where SICA compares against D&P instead, not FoVer. For the FoVer citations, I should consistently reference Table 5 with the Llama3.1-8B FoVer-PRM Best-of-7 scores (temporal 97.2%, tracking 96.0%). I'm working through the JSON structure systematically, updating each field with the refined citations and comparisons. The key changes involve adding Table 5 references for the FoVer BBH evaluation scores and clarifying how those results demonstrate cross-task generalization compared to the baseline performance. Could argue this should move to "strong" since reviewer says "one revision from passing" — but I'll keep it as "solid" to be conservative. Actually the reviewer gave 3.875, so "solid" is right.

No changes needed for key_references. For the description, I need to fix the BBH-FoVer comparison, add a Table 5 citation, and mention the concrete example. That's marked as a minor change. Project name and source stay the same.

Now I'm ready to write this out with those targeted fixes. I don't think additional searching is worth it here — the reviewer didn't flag any outdated claims or missing related work, just these three specific issues.

For the concrete example, I'm thinking about placement. It should go right before "A key empirical question..." as a new paragraph. That way it bridges from the theoretical limitations of CRAFT and D&P methods to the practical question of how often this actually matters in real data.

Now I'm drafting the example itself — a MATH-500 problem where two different reasoning paths emerge from the samples, each producing different intermediate steps and final answers. I'm showing how both CRAFT and D&P would fail to catch the logical incompatibility between the paths, while SICA's constraint-based approach would detect it. The example walks through the specific numbers and weights to make the limitation concrete.

For the BBH comparison, I need to clarify which subtasks actually overlap with FoVer's evaluation so the comparison is accurate.

For the metrics section, I'm refining how we present the FoVer-PRM baseline numbers and what specific performance we're comparing against. I'm checking the description field to make sure the BBH-FoVer comparison isn't already mentioned there — it looks like it just references the cross-task generalization to BBH without claiming a direct comparison, so that's fine. Now I need to map out the full timeline for Track A, which runs through EMNLP 2026 with a 14-day sprint starting May 25, breaking down into pipeline setup, core experiments, ablations, writeup, and submission. I need to finalize the JSON with the corrections: updating the landscape section to cite Table 5 for FoVer's BBH results, fixing the approach section's BBH bullet to clarify we're evaluating on those specific subtasks rather than claiming direct comparison, and adding a concrete example to the description to make it more self-contained. The timeline stays at May 12–25 since that's the original sprint window.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fca19d5b-e858-4020-8076-120e578ab9b5",
  "isSidechain": false,
  "requestId": "req_011CawktadUMJ7tRzFufBiF8",
  "type": "assistant",
  "uuid": "ff916ea7-5551-4b33-b22a-1c3094f8cd99",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7a04977f-b53a-45e0-8aa0-46eb4874f6b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JaZJ2Rxpj2nYrRmpc39wY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4247,
      "cache_read_input_tokens": 31331,
      "output_tokens": 21119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4247,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 21119,
          "cache_read_input_tokens": 31331,
          "cache_creation_input_tokens": 4247,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4247
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

_source line 17 · 2026-05-12T00:58:51.511Z_

Good — the FoVer paper confirms Table 5, Llama3.1-8B FoVer-PRM at Best-of-7 with temporal 97.2%, tracking 96.0%, word sorting 46.8%, and BBH Average 80.0% (the mean). Now I have everything needed for the three targeted fixes.

The three changes:
1. **Concrete worked example** added to opportunity section — synthetic rectangle problem showing CRAFT/D&P miss a cross-path contradiction that SICA's MAX-SAT catches
2. **BBH-FoVer comparison** corrected: 2 overlapping subtasks with FoVer + logical deduction with D&P
3. **FoVer Table 5 citation** added wherever BBH scores are referenced

```json
{
  "title": "Formally-Verified Intermediate Constraint Consensus Across Reasoning Paths",
  "core_problem": "Recent work (CRAFT, PoLR, Draft-and-Prune) demonstrates that intermediate reasoning step consensus or pruning across candidate solutions provides stronger signals than answer-level majority voting. However, existing methods either rely on statistical similarity that cannot distinguish popular-but-contradictory constraints (CRAFT's TF-IRF/Jaccard), or prune individual paths based on internal consistency without cross-validating constraints across solutions (Draft-and-Prune's per-path |S|=0/|S|>1 checks). Meanwhile, single-output formal verification systems (MATH-VF, SAFE, FoVer, PRoSFI, VERGE) verify constraints within one solution or output but do not cross-validate across multiple reasoning paths, and cross-query consistency checking (arXiv 2604.14525) verifies coherence across different questions but not across multiple traces for the same question. Furthermore, 'Consensus is Not Verification' (arXiv 2603.06612) demonstrates that consensus-based aggregation fails for truthfulness because LLM errors are strongly correlated — but crucially, aggregation improves performance when a verifier exists. Can formally verifying cross-solution intermediate constraints via SMT solving and computer algebra yield more reliable consensus with interpretable provenance, and how frequently does statistical consensus actually retain contradictory constraints in practice?",
  "opportunity": "CRAFT (arXiv 2604.14121, April 2026) builds a Reasoning Knowledge Graph from consensus intermediate steps using TF-IRF and Jaccard similarity, achieving significant accuracy improvements. However, CRAFT's authors explicitly acknowledge two key limitations: (1) 'consensus ≠ correctness' — frequently appearing steps can amplify shared errors, and (2) 'reduced effectiveness on symbolic math' due to lexical overlap bias in Jaccard similarity. This concern is empirically grounded by 'Consensus is Not Verification' (arXiv 2603.06612, March 2026), which demonstrates that LLM errors are strongly correlated across samples and even across model families — correlation persists even with random string conditioning — causing polling-style aggregation to yield no consistent accuracy gains over single-sample baselines. Critically, however, the paper finds that 'aggregation improves performance when a verifier exists, but it cannot serve as a verifier substitute,' directly motivating SICA's approach of introducing formal verification into the consensus process.\n\nDraft-and-Prune (D&P, arXiv 2603.17233, March 2026) addresses autoformalization brittleness by generating multiple natural-language plans, conditioning program generation on them, pruning individually contradictory or ambiguous formalizations (paths where the solver returns |S|=0 or |S|>1), and aggregating surviving paths via answer-level majority voting. D&P achieves strong results on logical reasoning benchmarks (AR-LSAT 78.43%, ProofWriter 98.33% with GPT-4), but its pruning operates independently on each path — it cannot detect cross-path contradictions where two individually valid paths assert mutually inconsistent constraints. D&P's authors explicitly note a limitation: 'We aggregate predictions at the answer level and do not cluster or de-duplicate candidates by symbolic equivalence.'\n\nTo make this gap concrete, consider a synthetic but realistic scenario: a MATH-500 problem asks 'A rectangle has perimeter 28 and its length is 3 more than twice its width. Find the area.' From K=12 sampled reasoning traces, two popular intermediate derivations emerge: C₁ (8 traces) correctly computes 'half-perimeter: l + w = 14,' yielding area = 341/9; C₂ (4 traces) erroneously sets 'perimeter: l + w = 28,' yielding area = 1475/9. All 12 traces share the constraint l = 2w + 3. Each path group produces a unique solution (D&P's |S|=1 check passes), so D&P retains all paths and majority-votes the correct answer — but cannot explain why the minority is wrong. CRAFT's TF-IRF/Jaccard consensus sees both 'l + w = 14' and 'l + w = 28' as popular steps (each exceeding the frequency threshold β = 0.3, since 4/12 ≥ 0.3) with high lexical overlap (shared terms: l, w, +, =), and retains both in its Reasoning Knowledge Graph without detecting their logical incompatibility. SICA extracts typed constraints: φ₁: l+w=14 (weight 8), φ₂: l+w=28 (weight 4), φ₃: l=2w+3 (weight 12), φ₄: 2(l+w)=28 (weight 8). The weighted partial MAX-SAT solver identifies {φ₁, φ₂} as unsatisfiable (and φ₄ entails φ₁, further reinforcing the inconsistency), returns the optimal satisfiable subset {φ₁, φ₃, φ₄} (total weight 28), and provides interpretable provenance: the minority's perimeter setup error is formally identified, localized to φ₂, and excluded from the consensus signal. This illustrates the core pattern: individually-consistent paths can harbor cross-path contradictions invisible to both per-path pruning and lexical consensus, but detectable by formal cross-path satisfiability checking.\n\nA parallel line of work verifies individual solutions or outputs formally — MATH-VF (arXiv 2505.20869) uses CAS+Z3 for step-level verification on single solutions; SAFE (ACL 2025) uses Lean4 for retrospective step-aware verification; PRoSFI (arXiv 2603.29500) trains process rewards over structured formal intermediaries verified by Lean/Z3/Prover9, operating on individual 7B-model solutions. VERGE (arXiv 2601.20055, Jan 2026) is a single-output verify-and-refine framework that decomposes an LLM output into atomic claims, autoformalizes them, verifies joint satisfiability via Z3, and uses Minimal Correction Subsets (MCS) to provide targeted feedback for iterative refinement. VERGE's 'multi-model consensus' refers to K=3 candidate formalizations of a single claim checked for semantic equivalence — not cross-path reasoning aggregation. FoVer (arXiv 2505.15960, ACL 2026 Findings) uses Z3 and Isabelle for step-level error annotation in individual solutions for PRM training, demonstrating cross-task generalization to BBH subtasks (Table 5, Llama3.1-8B FoVer-PRM at Best-of-7: temporal sequences 97.2%, tracking shuffled objects 96.0%, word sorting 46.8%; the BBH Average column reads 80.0%). In the adjacent cross-output verification space, 'Quantifying Cross-Query Contradictions' (arXiv 2604.14525, April 2026) uses Z3 (QF_UFLIA) and CaDiCaL for cross-query consistency checking with unsat-core localization and counterexample-guided repair — but addresses cross-query consistency (different questions sharing a case file), not cross-trace consistency (same question, multiple reasoning paths). The EACL 2026 dynamic solver routing framework (arXiv 2510.06774) selects solvers at the problem level. But none of these methods formally cross-validate intermediate constraints across multiple candidate solutions for the same problem.\n\nThe gap: no method formally cross-validates intermediate constraints across multiple candidate solutions to produce a consistency-aware consensus signal with interpretable provenance. Concretely, SICA differs from D&P by extracting constraints from ALL paths and finding a globally consistent MAX-SAT-optimal subset (cross-path aggregation), rather than independently pruning paths with internal contradictions (per-path filtering). SICA differs from VERGE by applying MAX-SAT across multiple reasoning paths for answer selection, whereas VERGE applies the dual MCS operation within a single output for refinement feedback. SICA differs from the cross-query contradictions framework by operating on multiple traces for the same question (cross-trace scope) using weighted partial MAX-SAT for consensus, rather than on different questions in a case file (cross-query scope) using unsat-core repair. A key empirical question — how frequently does statistical consensus actually retain contradictory constraints? — remains unanswered and is central to quantifying this opportunity. The motivating rectangle example above suggests the pattern is realistic; the centerpiece contradiction frequency analysis will measure its prevalence systematically across benchmarks.\n\nRecent work on autoformalization faithfulness further motivates SICA's extraction quality pipeline: 'Do LLMs Game Formalization?' (arXiv 2604.19459, VerifAI-2 Workshop, ICLR 2026) shows that high compilation rates should not be equated with faithful reasoning, finding that two-stage formalization pipelines reveal distinct unfaithfulness patterns (axiom fabrication, premise mistranslation) that evade standard verification. This underscores the need for SICA's multi-tier extraction validation.",
  "landscape": "Standard self-consistency (Wang et al., ICLR 2023) performs majority voting on final answers and shows diminishing returns on frontier models — gains plateau at <2% with accuracy sometimes declining at high sample counts (arXiv 2511.00751). 'Consensus is Not Verification' (arXiv 2603.06612, March 2026) provides a theoretical explanation: LLM errors are strongly correlated across samples and model families, causing consensus to reinforce shared misconceptions rather than converge on truth; however, the paper finds aggregation succeeds when an external verifier exists. CRAFT (arXiv 2604.14121, April 2026) extracts consensus intermediate steps via a Reasoning Knowledge Graph using TF-IRF/Jaccard similarity and topological generation, achieving up to +8.5% accuracy over SC baselines on GSM8K, FOLIO, FLD, and OlympiadBench with K=3 traces; its authors note 'consensus ≠ correctness' and 'reduced effectiveness on symbolic math' as limitations. PoLR (ICLR 2026) uses prefix consensus to prune reasoning paths, matching SC accuracy while reducing token usage by 50-60%.\n\nCross-path intermediate-step analysis with neural verification: 'Correct Reasoning Paths Visit Shared Decision Pivots' (ROMA, arXiv 2509.21549, NeurIPS 2025 Workshop FoRLM; ICLR 2026 Workshop RSI) hypothesizes that correct reasoning paths converge on shared 'decision pivots' — minimal, verifiable checkpoints that any correct path must visit. ROMA mines these pivots across K sampled reasoning paths and uses a learned verifier to distill pivot-focused short-path reasoning, evaluating on LogiQA, MedQA, and MATH-500. ROMA occupies the adjacent conceptual space of cross-path intermediate-step consensus but uses neural verification (a trained pivot verifier) rather than formal solvers. SICA provides formal satisfiability guarantees where ROMA uses learned signals, and operates on typed symbolic constraints rather than natural-language decision pivots — the approaches are complementary, with ROMA better suited to domains where formalization is intractable and SICA to domains with extractable logical structure.\n\nDraft-and-Prune (D&P, arXiv 2603.17233, March 2026): An inference-time framework that drafts multiple natural-language plans, conditions program generation on them, prunes executable but contradictory (|S|=0) or ambiguous (|S|>1) formalizations independently for each path, and aggregates surviving paths via answer-level majority voting. Uses Z3Py for AR-LSAT/LogicalDeduction and PyKe for ProofWriter/PrOntoQA. Achieves AR-LSAT 78.43%, ProofWriter 98.33%, PrOntoQA 99.32%, LogicalDeduction 99.50% (GPT-4). Key limitation: no cross-path constraint checking or equivalence-aware deduplication.\n\nVERGE (arXiv 2601.20055, Jan 2026): A single-output neurosymbolic verify-and-refine loop. Decomposes an LLM output into atomic claims, classifies them by type, autoformalizes into FOL, and verifies joint satisfiability via Z3. Uses semantic routing (symbolic solvers for logical claims, LLM ensembles for commonsense) and Minimal Correction Subsets (MCS) for precise error localization, providing actionable feedback for iterative refinement. VERGE's K=3 refers to candidate formalizations of a single claim checked for semantic equivalence, not multiple reasoning paths. MCS (minimum claims to remove for satisfiability) is dual to MAX-SAT (maximum satisfiable subset) but is applied within one output for feedback, not across paths for consensus. Evaluated on FOLIO (84.7-89.2%), ProofWriter (85.2-93.0%), AR-LSAT (88.6-91.7%) across GPT-OSS-20B, GPT-OSS-120B, and Claude 3.7 Sonnet.\n\nSingle-solution formal verification: MATH-VF (arXiv 2505.20869, May 2025) uses a Formalizer+Critic pipeline with CAS and Z3 SMT solver for step-level verification on individual solutions, evaluated on MATH-500 and ProcessBench. SAFE (ACL 2025, arXiv 2506.04592) uses Lean4 for retrospective step-aware formal verification of individual reasoning chains, introducing the FormalStep benchmark (30,809 formal statements). PRoSFI (arXiv 2603.29500, March 2026) — 'Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries' — trains process rewards over structured formal intermediaries verified by Lean tactics, Z3, and Prover9, operating on individual 7B-model solutions; achieves 92.97% accuracy / 76.07% GPT Soundness on ProverQA-Hard. FoVer (arXiv 2505.15960, ACL 2026 Findings) — 'Training Step-Level Reasoning Verifiers with Formal Verification Tools' — uses Z3 and Isabelle for step-level error annotation in individual solutions for PRM training; demonstrates cross-task generalization to BBH subtasks (Table 5, Llama3.1-8B FoVer-PRM at Best-of-7: temporal sequences 97.2%, tracking shuffled objects 96.0%, word sorting 46.8%; the BBH Average column reads 80.0%, which is the mean across all three subtasks) and to MATH, AIME, ANLI, MMLU-Pro.\n\nCross-output consistency verification: 'Quantifying Cross-Query Contradictions in Multi-Query LLM Reasoning' (arXiv 2604.14525, April 2026) addresses cross-query consistency — maintaining a globally satisfiable belief state across interdependent queries sharing a case file. Uses Z3 v4.8.17 (QF_UFLIA theory) and CaDiCaL for SAT, with unsat-core localization and counterexample-guided lexicographic repair. Achieves SetCons improvement from 0.56 to 0.94 across 390 case files spanning relational/SAT, temporal/SMT, policy/rules, and abductive domains. Crucially, this operates at cross-query scope (different questions sharing context) rather than cross-trace scope (same question, multiple reasoning paths), and uses unsat-core repair rather than weighted partial MAX-SAT consensus. SICA's differentiators are: cross-trace scope, intermediate constraint extraction from reasoning steps, and popularity-weighted MAX-SAT for answer selection.\n\nSolver routing: The EACL 2026 dynamic solver composition framework (arXiv 2510.06774) automatically identifies formal reasoning strategies and routes to specialized solvers at the problem level, achieving 27% improvement over GPT-4o. SICA's theory-aware routing operates at the finer-grained assertion level.\n\nVeriCoT (Nov 2025) formalizes individual CoT traces into FOL for entailment checking without cross-solution comparison. FregeLogic (SemEval 2026) uses Z3 as a tiebreaker for syllogistic validity.\n\nAutoformalization reliability: Grammars of Formal Uncertainty (NeurIPS 2025) demonstrates that SMT autoformalization is task-dependent: +34.8% on ProofWriter but -44.5% on FOLIO, necessitating careful benchmark selection and per-domain extraction analysis. 'Do LLMs Game Formalization?' (arXiv 2604.19459, VerifAI-2 Workshop, ICLR 2026) evaluates faithfulness of LLM autoformalization on 303 FOL problems, finding that high compilation rates (87-99%) do not guarantee faithful reasoning — two-stage pipelines reveal distinct unfaithfulness patterns: axiom fabrication (GPT-5) and premise mistranslation (DeepSeek-R1). Autoformalization surveys (arXiv 2505.23486) report ~70% success rate on physics kinematics, with selective verification reducing errors by 14-100% with minimal abstention.\n\nNo concurrent work (searched arXiv and OpenReview through May 2026) formally cross-validates intermediate constraints across multiple candidate solutions for the same problem.",
  "approach": "We propose Symbolic Invariant Consensus Aggregation (SICA): given a problem, sample K reasoning paths from a frontier open-source reasoning model (QwQ-32B via vLLM on 1-2 A100s; Qwen3-32B as secondary model for ablation), then use a prompted LLM extractor to parse each trace into typed symbolic assertions (equations, inequalities, logical predicates). SICA introduces four key technical components:\n\n(1) **Theory-aware assertion-level solver routing**: Extracted assertions are classified by constraint type and routed to appropriate solvers — Z3 for tractable theories (linear arithmetic, propositional logic, uninterpreted functions, bitvectors) and SymPy for nonlinear polynomial arithmetic, algebraic equivalence, and modular arithmetic. Unlike the EACL 2026 framework (arXiv 2510.06774) which routes at the problem level, SICA routes at the assertion level, enabling mixed-theory problems where individual steps span different solver domains (common in competition math). Assertions that neither solver can handle receive numerical spot-checking as fallback, with unverifiable assertions flagged and excluded from the consensus set (rather than silently included).\n\n(2) **Weighted partial MAX-SAT for invariant consensus**: Rather than enumerating assertion subsets (exponential worst-case), SICA leverages Z3's built-in optimization context to solve weighted partial MAX-SAT directly. Each unique assertion (deduplicated via solver-verified equivalence) is weighted by its cross-solution frequency. The optimizer finds the largest jointly satisfiable subset of assertions, weighted by popularity — a single Z3 optimization call replaces exponential subset enumeration. Per-query timeout caps (10s) bound worst-case latency. This cross-path MAX-SAT consensus is the key differentiator from Draft-and-Prune (D&P), which prunes paths independently based on internal consistency (|S|=0 or |S|>1) and aggregates surviving answers via majority voting without cross-path constraint checking. It is also distinct from VERGE's MCS, which is the dual operation (minimum claims to remove) applied within a single output for refinement feedback rather than across paths for answer selection. It further differs from the cross-query contradictions framework (arXiv 2604.14525), which uses unsat-core localization and counterexample-guided repair across different questions sharing a case file — SICA uses weighted partial MAX-SAT across different reasoning traces for the same question.\n\n(3) **Invariant-backed answer scoring**: Each candidate answer is scored by the coverage and weight of its supporting assertions within the MAX-SAT-optimal consistent set, yielding a continuous invariant consensus score. This captures partial structural agreement even when final answers diverge, and provides interpretable provenance (each score is backed by a specific set of formally verified constraints).\n\n(4) **Extraction quality assurance pipeline**: To address the documented task-dependence of autoformalization (Grammars of Formal Uncertainty, NeurIPS 2025) and the unfaithfulness risks identified by 'Do LLMs Game Formalization?' (arXiv 2604.19459), we implement a three-tier extraction quality pipeline: (a) syntactic validation — each extracted assertion must parse in the target solver's input language; (b) semantic spot-checking — a random 20% of assertions are checked against the original natural language step via an LLM judge for semantic fidelity, specifically targeting the axiom fabrication and premise mistranslation failure modes identified in the faithfulness literature; (c) coverage tracking — we report 'verifiable assertion coverage' (% of extracted assertions that successfully enter the MAX-SAT pipeline) per benchmark as a first-class metric. Extraction failures cascade to numerical fallback or abstention, preventing malformed inputs from corrupting the consensus signal.\n\n**Limitations of formal cross-validation**: SICA's MAX-SAT consensus catches contradictory constraints but cannot detect universally-wrong-but-mutually-consistent constraints caused by correlated extraction errors. 'Consensus is Not Verification' (arXiv 2603.06612) demonstrates that LLM errors are strongly correlated across samples and even across model families, which implies that if all K paths produce the same wrong formalization of a constraint, MAX-SAT will see K consistent-but-wrong assertions and cannot flag the error. This is a fundamental limitation of any approach combining LLM extraction with formal verification: the verifier guarantees consistency, not correctness of the extraction. SICA's semantic spot-checking tier partially mitigates this — by sampling 20% of assertions for LLM-judge semantic fidelity checks, it can catch systematic mistranslation patterns. However, if the extraction LLM and the judge LLM share the same correlated bias (as the correlated errors literature suggests is likely), the mitigation is incomplete. We acknowledge this limitation explicitly and note two potential future mitigations: (a) using structurally diverse extractor models (e.g., symbolic parsers alongside LLM extractors) to decorrelate extraction errors, and (b) grounding extracted constraints against external knowledge sources (CAS simplification, unit-test-style numerical spot-checking) that do not share LLM inductive biases. We include FOLIO as a diagnostic ablation where SMT autoformalization is documented to hurt (-44.5%), precisely to empirically characterize the boundary between domains where SICA's extraction is faithful enough to help versus where correlated errors dominate.\n\n**Day-by-day Track A timeline (14-day sprint, May 12–25)**:\n\n- *Days 1–3 (May 12–14): Pipeline implementation.* Day 1: extraction prompt development for math domains (MATH-500, AIME) and logical domains (ProofWriter, FOLIO) — two prompt templates covering all benchmarks. Day 2: solver routing infrastructure (Z3 + SymPy dispatch, MAX-SAT wrapper using Z3's optimization context, equivalence deduplication). Day 3: end-to-end pipeline integration and smoke testing on 50 problems from MATH-500.\n- *Days 4–6 (May 15–17): Core experiments.* Day 4: MATH-500 (K=12) + AIME 2024 (K=12) + AIME 2025 (K=12) — all share the math extraction prompt; batched vLLM inference across 2 A100s. Day 5: ProofWriter (K=12) — direct D&P/VERGE comparison benchmark. Day 6: FOLIO (K=12, negative diagnostic) + begin BBH subtasks if pipeline stable.\n- *Days 7–8 (May 18–19): Ablations and additional experiments.* Day 7: BBH subtasks (3 configs × K=12) if extraction quality validates; otherwise, begin ablation suite (K sweep, extraction noise injection). Day 8: Contradiction frequency analysis (centerpiece experiment) across all completed benchmarks; correlated extraction error measurement on 100 problems per benchmark.\n- *Days 9–10 (May 20–21): Analysis and figures.* Compile results tables, generate accuracy/calibration figures, write contradiction frequency analysis, produce extraction quality breakdown per benchmark. Compute-normalized comparison (tokens, wall-clock time).\n- *Days 11–13 (May 22–24): Paper writing.* Day 11: Introduction, method description, related work. Day 12: Experiments, results, analysis sections. Day 13: Abstract, conclusion, formatting, supplementary material.\n- *Day 14 (May 25): Final polish and submission.* Buffer day for last-minute fixes, ARR submission.\n\n**Honest assessment of timeline risk**: Paper writing in 3 days is aggressive but feasible for a focused 8-page submission with auto-generated figures and tables from Days 9–10. The main risk is pipeline debugging overrunning Days 1–3, which compresses experiment time. The minimum viable scope (below) mitigates this by defining a credible fallback that preserves 1–2 buffer days.\n\n**Note on ARR cycle fallback**: There is no June 2026 ARR cycle — ARR operates on 10-week cycles (~5 per year), and the May 25 cycle is the last eligible for EMNLP 2026 commitment (deadline: August 2, 2026). If the May 25 deadline is missed, the fallback is AAAI 2027 (paper deadline: August 1, 2026), which provides an additional 11 weeks and allows full Track A+B evaluation without time pressure.\n\n**Minimum viable scope (fallback if full plan proves too ambitious)**: If extraction quality is unreliable on BBH subtasks or timeline slips compress experiment time, the minimum credible submission is 5 benchmarks at K=12: MATH-500, AIME 2024, AIME 2025, ProofWriter, and FOLIO. This scope preserves all core contributions: (a) cross-path MAX-SAT consensus demonstrated on ProofWriter (D&P/VERGE comparison), (b) contradiction frequency analysis on math benchmarks (MATH-500, AIME 2024/2025), (c) negative diagnostic on FOLIO showing domain boundaries, (d) generalization test on unseen competition problems (AIME 2025 vs. AIME 2024), and (e) extraction quality analysis. BBH subtasks and the FoVer comparison would move to the AAAI 2027 extended version (Track B). This fallback saves ~1.5 days of experiment time (BBH extraction prompt development + 3 benchmark runs), creating headroom for pipeline debugging or additional paper writing time. Under this minimum scope, the timeline adjusts to: Days 1–3 implementation, Days 4–5 experiments (5 benchmarks), Days 6–7 ablations/analysis, Days 8–10 paper writing, Days 11–14 polish/buffer — a substantially more comfortable schedule.\n\n**Dual-track evaluation plan**:\n\n*Track A — EMNLP 2026 (ARR May 25, primary target, 14 days):* Scoped evaluation with K=12 traces on 6 core benchmarks plus 3 BBH subtasks (full scope) or 5 core benchmarks (minimum viable scope):\n- **MATH-500** (algebraic/arithmetic reasoning; QwQ-32B ~90.6%)\n- **AIME 2024** (competition math with mixed-theory constraints; QwQ-32B ~79.5%)\n- **AIME 2025** (unseen competition problems; tests generalization using the identical evaluation pipeline as AIME 2024 — trivially low marginal cost since both share the same extraction prompt and solver routing)\n- **ProofWriter** (formal logic; enables direct comparison with D&P 98.33% and VERGE 85.2-93.0%)\n- **FOLIO** (first-order logic; diagnostic ablation — SMT autoformalization documented to hurt -44.5% here)\n- **BBH** (3 subtasks: logical deduction, tracking shuffled objects, temporal sequences — enables comparison with FoVer on 2 of 3 overlapping BBH subtasks (temporal sequences, tracking shuffled objects) and with D&P on logical deduction; tests cross-domain generalization to structured informal reasoning) *[included in full scope; deferred to Track B in minimum viable scope]*\n\nBaselines for Track A: self-consistency, CRAFT, D&P (on ProofWriter), VERGE (on ProofWriter/FOLIO).\n\n*Track B — AAAI 2027 (abstract deadline: July 25, paper deadline: August 1, 2026; extended version):* Expanded to K=16 traces on all Track A benchmarks plus:\n- **GPQA Diamond** (graduate-level science; QwQ-32B ~65.2%; per-domain reporting for physics/chemistry vs. biology)\n- **LogiQA 2.0** (natural language logical reasoning; 8,678 questions; tests constraint extraction beyond math/formal logic)\n- BBH subtasks (if deferred from Track A) and full ablation suite\n- Qwen3-32B cross-model ablation\n\n**ARC-Challenge exclusion justification**: ARC-Challenge (Clark et al., 2018) consists of multiple-choice grade-school science questions that primarily test factual knowledge retrieval (e.g., 'Which mineral is the hardest?', 'What happens when water freezes?'). Most questions lack the multi-step constraint structure required for meaningful symbolic assertion extraction — they involve domain knowledge rather than chains of extractable equations, inequalities, or logical predicates. Including ARC-Challenge would likely yield near-zero verifiable assertion coverage, providing no insight beyond confirming SICA's domain specificity (which FOLIO already demonstrates as a negative diagnostic). We note this scope limitation explicitly.\n\n**Metrics and analyses**:\n- Primary: accuracy, calibration (ECE), informativeness of partial invariant agreement when candidates disagree\n- **Contradiction frequency analysis** (centerpiece experiment): For each problem across all benchmarks, we measure how often CRAFT's statistical consensus retains logically contradictory constraint pairs. We report the 'contradiction rate' — the fraction of problems where at least one pair of popular constraints (appearing in ≥3 of K traces) are mutually unsatisfiable. If >15%, this validates SICA's core motivation; if <5%, we honestly acknowledge limited practical impact on this axis and emphasize interpretability/provenance instead. The motivating rectangle example (in the opportunity section) illustrates the prototypical pattern: a perimeter setup error producing two individually-consistent but cross-path-contradictory constraints that statistical consensus cannot distinguish.\n- **D&P comparison**: On ProofWriter (shared benchmark), we compare SICA's cross-path MAX-SAT consensus against D&P's per-path pruning + answer-level voting, specifically measuring: (a) how many problems have cross-path contradictions that D&P's per-path pruning misses, and (b) whether MAX-SAT-backed scoring outperforms answer-level majority voting among surviving paths.\n- **FoVer comparison on BBH** (full scope only): On the 2 overlapping BBH subtasks (temporal sequences, tracking shuffled objects), we compare SICA's inference-time cross-path consensus against FoVer's training-time PRM approach (Table 5 of FoVer v3, Llama3.1-8B FoVer-PRM at Best-of-7: temporal sequences 97.2%, tracking shuffled objects 96.0%; the adjacent BBH Average column of 80.0% is the mean across these two and word sorting 46.8%, not a per-subtask score). On the third BBH subtask (logical deduction), we compare against D&P rather than FoVer, as logical deduction is not among FoVer's evaluated BBH subtasks. This analysis tests whether cross-path formal consensus provides complementary signal to trained process reward models.\n- **Extraction accuracy ablation**: Per-benchmark measurement of (a) syntactic parse rate, (b) semantic fidelity (manual annotation on 100 samples per benchmark), and (c) error propagation analysis — how X% extraction error degrades MAX-SAT consensus quality via controlled noise injection. Per the findings of 'Do LLMs Game Formalization?', we specifically track axiom fabrication and premise mistranslation rates.\n- **Correlated extraction error analysis**: On a subset of problems (100 per benchmark), we measure cross-path extraction agreement — the fraction of assertions that are semantically equivalent across all K traces — to empirically quantify the degree of correlated extraction and assess how much independent signal SICA's MAX-SAT actually receives.\n- **Compute-normalized comparison**: Report total tokens generated, wall-clock time per problem, and decomposed latency (inference, extraction, solver, MAX-SAT) for each method. Plot accuracy vs. total compute (tokens) curves. If SICA takes 5x compute of vanilla SC for +2% accuracy, we justify via interpretability/soundness or acknowledge the tradeoff.\n\nThe primary contribution is not raw accuracy improvement over SC (which has diminishing returns on frontier models) but rather: (a) formal soundness guarantees on the consensus signal, (b) interpretable constraint-level provenance for each answer, (c) detecting logically inconsistent popular reasoning steps that both statistical consensus (CRAFT) and per-path pruning (D&P) miss — with empirical quantification of how frequently this occurs (motivated by the concrete rectangle example), (d) systematic domain analysis of formal cross-solution verification including where it helps (ProofWriter, BBH logical deduction) vs. hurts (FOLIO), and (e) empirical characterization of correlated extraction errors as a fundamental limitation of LLM-based autoformalization in consensus settings.",
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
  "description": "We propose Symbolic Invariant Consensus Aggregation (SICA), a method that formally cross-validates intermediate constraints extracted from multiple LLM reasoning paths to produce a soundness-guaranteed consensus signal. While CRAFT (April 2026) demonstrates the value of intermediate-step consensus via statistical similarity (TF-IRF/Jaccard), its authors explicitly acknowledge 'consensus ≠ correctness' and 'reduced effectiveness on symbolic math.' This limitation is theoretically grounded by 'Consensus is Not Verification' (arXiv 2603.06612, March 2026), which proves that LLM errors are strongly correlated across samples and model families, causing pure consensus to fail — but critically finds that 'aggregation improves performance when a verifier exists,' directly motivating SICA's approach. ROMA (arXiv 2509.21549, ICLR 2026 Workshop RSI) occupies the adjacent conceptual space of cross-path intermediate-step analysis via shared 'decision pivots' but uses neural verification rather than formal solvers — SICA provides formal satisfiability guarantees where ROMA uses learned signals. Draft-and-Prune (D&P, March 2026) improves autoformalization reliability by independently pruning paths with internal contradictions and aggregating survivors via majority voting, but does not perform cross-path constraint checking — its authors note they 'aggregate predictions at the answer level and do not cluster or de-duplicate candidates by symbolic equivalence.' Meanwhile, VERGE (Jan 2026) verifies and refines a single LLM output by decomposing it into atomic claims, checking joint satisfiability via Z3, and using Minimal Correction Subsets (MCS) to provide targeted refinement feedback — but operates on one output, not across reasoning paths. In the adjacent cross-output verification space, 'Quantifying Cross-Query Contradictions' (arXiv 2604.14525, April 2026) uses Z3 (QF_UFLIA) and CaDiCaL for cross-query consistency checking with unsat-core repair, but addresses cross-query consistency (different questions sharing a case file) rather than cross-trace consistency (same question, multiple paths). Single-solution formal verification (MATH-VF uses CAS+Z3; SAFE uses Lean4; PRoSFI uses Lean/Z3/Prover9 for structured formal intermediaries on 7B models; FoVer (arXiv 2505.15960) uses Z3+Isabelle for PRM training data with cross-task generalization to BBH) improves reliability but none cross-validate across solutions.\n\nThe gap is made concrete by a motivating example: for a rectangle problem (perimeter 28, length = 2×width + 3), K=12 traces yield two popular but contradictory intermediate constraints — 'l+w=14' (8 traces, correct half-perimeter) and 'l+w=28' (4 traces, erroneous full perimeter). Both pass D&P's per-path consistency check (each yields a unique solution), and both survive CRAFT's lexical consensus (high term overlap, both above the frequency threshold). SICA's MAX-SAT solver detects {l+w=14, l+w=28} as unsatisfiable, excludes the lower-weight constraint, and provides interpretable provenance localizing the error to φ₂.\n\nSICA fills this gap by extracting typed symbolic assertions from K sampled reasoning traces, routing them to appropriate solvers via assertion-level theory-aware dispatch (Z3 for linear arithmetic and propositional logic; SymPy for nonlinear polynomial and algebraic constraints — finer-grained than the EACL 2026 problem-level solver routing), and using Z3's built-in weighted partial MAX-SAT optimization to find the largest jointly satisfiable assertion set weighted by cross-solution frequency. SICA's MAX-SAT consensus across paths is the cross-path counterpart to VERGE's within-output MCS (dual operations: MAX-SAT keeps the maximum consistent subset; MCS removes the minimum inconsistent subset), and differs from cross-query contradiction checking by operating on multiple traces for the same question via weighted consensus rather than unsat-core repair across different questions. A three-tier extraction quality pipeline (syntactic validation, semantic spot-checking targeting the unfaithfulness patterns identified by 'Do LLMs Game Formalization?' (arXiv 2604.19459), and coverage tracking) addresses the documented task-dependence of autoformalization.\n\nWe explicitly acknowledge a fundamental limitation: SICA's MAX-SAT consensus catches contradictory constraints but cannot detect universally-wrong-but-consistent constraints caused by correlated extraction errors — the same correlated error phenomenon documented by 'Consensus is Not Verification.' The semantic spot-checking tier partially mitigates this, but correlated biases between the extractor and judge LLMs limit its effectiveness. We include FOLIO as a diagnostic ablation and propose a correlated extraction error analysis to empirically characterize this boundary.\n\nWe adopt a dual-track evaluation plan with a concrete day-by-day timeline. Track A (EMNLP 2026, ARR May 25 — 14-day sprint): Days 1-3 pipeline implementation, Days 4-6 core experiments, Days 7-8 ablations/analysis, Days 9-10 figures/tables, Days 11-13 paper writing, Day 14 submission. Full scope: K=12 on MATH-500, AIME 2024, AIME 2025 (identical pipeline to AIME 2024, trivially low marginal cost), ProofWriter, FOLIO, and 3 BBH subtasks (logical deduction, tracking shuffled objects, temporal sequences). Minimum viable scope (fallback if BBH extraction unreliable or timeline slips): 5 benchmarks — MATH-500, AIME 2024, AIME 2025, ProofWriter, FOLIO — which preserves all core contributions while saving ~1.5 days. There is no June ARR cycle (ARR uses 10-week cycles); if May 25 is missed, AAAI 2027 (paper deadline: August 1) serves as the fallback venue with full Track A+B evaluation. Track B (AAAI 2027): expanded to K=16 with GPQA Diamond, LogiQA 2.0, Qwen3-32B cross-model ablation, and any benchmarks deferred from Track A. The BBH subtasks enable comparison with FoVer on 2 of 3 overlapping subtasks (temporal sequences, tracking shuffled objects; Table 5 of FoVer v3, Llama3.1-8B FoVer-PRM at Best-of-7: temporal 97.2%, tracking 96.0%) and with D&P on logical deduction. The centerpiece experiment is a contradiction frequency analysis measuring how often statistical consensus retains logically contradictory constraint pairs. FOLIO serves as a diagnostic ablation where SMT is documented to hurt (-44.5%). Primary contributions: formal soundness guarantees, interpretable constraint-level provenance, empirically-quantified detection of contradictory consensus that both statistical methods and per-path pruning miss (illustrated by the rectangle motivating example and measured systematically), systematic domain analysis of formal cross-solution verification, and honest characterization of the correlated extraction error limitation. Auto-mode compute fits within 200h H100 budget at K=12 with 6+3 benchmarks (full scope) or ~130h H100 with 5 benchmarks (minimum viable scope).",
  "project_name": "symb_invariant_consensus",
  "source": "web_research",
  "change_type": "minor"
}
```

**Summary of changes (all minor/targeted):**

1. **Concrete motivating example added** (opportunity + description): A synthetic rectangle problem (perimeter 28, l = 2w+3) where K=12 traces produce two popular but contradictory constraints — `l+w=14` (8 traces) vs `l+w=28` (4 traces). The example walks through why D&P retains both (each internally consistent), CRAFT retains both (high lexical overlap, both above frequency threshold), but SICA's MAX-SAT detects the unsatisfiability and excludes the lower-weight constraint with interpretable provenance.

2. **BBH-FoVer comparison corrected** (approach + description): Changed from "enables direct comparison with FoVer's BBH evaluation" to "enables comparison with FoVer on 2 of 3 overlapping BBH subtasks (temporal sequences, tracking shuffled objects) and with D&P on logical deduction." Updated the FoVer comparison metric section accordingly.

3. **FoVer Table 5 citation added** (opportunity, landscape, approach): All references to BBH scores now cite "Table 5, Llama3.1-8B FoVer-PRM at Best-of-7" and clarify that the BBH Average column (80.0%) is the mean across all three subtasks, not a per-subtask score — disambiguating the word sorting 46.8% vs. average 80.0% confusion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff916ea7-5551-4b33-b22a-1c3094f8cd99",
  "isSidechain": false,
  "requestId": "req_011CawktadUMJ7tRzFufBiF8",
  "type": "assistant",
  "uuid": "91749245-57a9-4e5b-b684-1f06a47e2cb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "7a04977f-b53a-45e0-8aa0-46eb4874f6b0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JaZJ2Rxpj2nYrRmpc39wY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4247,
      "cache_read_input_tokens": 31331,
      "output_tokens": 21119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4247,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 21119,
          "cache_read_input_tokens": 31331,
          "cache_creation_input_tokens": 4247,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4247
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

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"Formally-Verified Intermediate Constraint Consensus Across Reasoning P…",
  "leafUuid": "91749245-57a9-4e5b-b684-1f06a47e2cb3",
  "sessionId": "7a04977f-b53a-45e0-8aa0-46eb4874f6b0"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify cross-solution constraints formally for consensus",
  "sessionId": "7a04977f-b53a-45e0-8aa0-46eb4874f6b0"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-11 (UTC).**  ## Original idea {   \"title\": \"Formally-Verified Intermediate Constraint Consensus Across Reasoning P…",
  "leafUuid": "91749245-57a9-4e5b-b684-1f06a47e2cb3",
  "sessionId": "7a04977f-b53a-45e0-8aa0-46eb4874f6b0"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Verify cross-solution constraints formally for consensus",
  "sessionId": "7a04977f-b53a-45e0-8aa0-46eb4874f6b0"
}
```

---
