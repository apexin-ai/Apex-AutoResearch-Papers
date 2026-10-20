# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Formal Error Profiling Enables Te

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/da86d49f-2149-4719-af01-f74fce2bddfa.jsonl`
- **Structured JSON:** [`6fa83a04c85d2fa79883.json`](../../sessions/6f/6fa83a04c85d2fa79883.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T09:06:34.445Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T09:06:34.445Z",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Formal Error Profiling Enables Teacher-Free Targeted Math Self-Improvement\n\n## Core Problem\n\nSelf-improvement loops for mathematical reasoning suffer from model collapse (solver-verifier gap theory, ICLR 2026) and untargeted data waste. All existing error-targeted synthesis methods — STAT (ICLR 2026), Self-Error-Instruct (ACL 2025), SwS (NeurIPS 2025), WarriorMath (arXiv 2025) — depend on LLM teachers or LLM metacognition for error diagnosis, introducing teacher bias, hallucinated attributions, and scalability ceilings. Empirically, LLMs cannot reliably spot mathematical errors even with reference solutions (arXiv 2509.01395, EMNLP 2025). Can formal symbolic tools serve as collapse-proof verifiers and ground-truth error diagnosticians, enabling stable, teacher-free, targeted self-improvement?\n\n## Core Contributions\n\n1. **Teacher-free error-targeted self-improvement**: The first self-improvement system where error diagnosis and targeted synthesis are driven entirely by formal symbolic tools (Z3, SymPy), eliminating LLM teacher dependency. Unlike RLVR/GRPO (also teacher-free), FormalLoop targets specific error types rather than optimizing globally.\n\n2. **Formally-verified step-localized DPO**: Preference pairs where trajectories share k formally-verified-correct steps and diverge at step k+1 — providing step-localized credit assignment with formal guarantees. Unlike Step-DPO (NeurIPS 2024) and Full-Step-DPO (ACL 2025 Findings) which use LLM/human annotations, and unlike NSRSA (arXiv 2026) which constructs solution-level accept/reject pairs, our pairs provide zero-noise step-localized preference signals.\n\n3. **Ground-truth error profile dynamics**: FormalLoop uniquely enables tracking formally-verified per-skill-type error evolution across self-improvement iterations — answering whether error types have fixed reduction priority orderings, whether skill dependencies exist (e.g., arithmetic errors must resolve before algebraic errors become visible), and whether error profile entropy predicts convergence. No prior work provides ground-truth skill-decomposed self-improvement dynamics.\n\n4. **Precision-coverage tradeoff hypothesis**: We hypothesize that in self-improvement loops, there exists a verifier noise threshold τ beyond which expanding coverage yields negative marginal returns. Imperfect verifier research (arXiv 2604.07666, arXiv 2026) estimates τ ≈ 15%; solver-verifier gap theory (ICLR 2026) predicts verifier reliability determines the self-improvement ceiling. FormalLoop tests this: formal verification achieves near-zero noise within its scope (~60-70% of amenable categories), which should outperform full-coverage but noisier LLM diagnosis. We validate via noise injection ablation.\n\n## Why Not Simpler Alternatives?\n\n**vs. Outcome verification + STAT-style LLM teacher profiling**: (1) Error attribution precision — outcome verification doesn't localize errors; LLM step diagnosis hallucinates (arXiv 2509.01395, EMNLP 2025); formal verification provides guaranteed step-level attribution. (2) Iterative stability — LLM teacher biases compound across iterations; formal diagnosis is independently calibrated each round. (3) No teacher ceiling — STAT's profiling quality is bounded by teacher metacognition.\n\n**vs. Subcategory-level outcome targeting** (using MATH's existing 7 subcategory labels to oversample weak categories): This requires no formal verification at all. However, subcategory labels are coarse — within Algebra alone, a model may struggle specifically with equation solving but not algebraic manipulation. Formal step-level diagnosis provides within-subcategory skill decomposition that subcategory-level targeting cannot. We include subcategory-level targeting as an explicit baseline to quantify this granularity advantage.\n\n**vs. FoVer-PRM as verifier in a standard self-improvement loop**: FoVer (ACL 2026) trains PRMs from formal verification data for general use. A natural alternative is using a FoVer-trained PRM as the verifier in a self-improvement loop (via Best-of-N or RLVR). FormalLoop differs by using formal verification directly for error categorization and targeted synthesis — not indirectly through a learned PRM. We include FoVer-PRM + RLVR as a baseline to isolate direct formal profiling's advantage.\n\n## Research Landscape\n\nCurrent SOTA in synthetic math data: SPARQ (June 2025, +24% via quality-diversity from 7.5K seeds), CoTEvol (April 2026, +6.6% via evolutionary CoT synthesis), MathMixup (Jan 2026, 47.6% on 7 benchmarks via difficulty-controlled curriculum). Self-improvement: SPICE (Oct 2025, +8.9% via document-grounded self-play), SvS (Aug 2025, +18.3% Pass@32 on AIME24 via variational problem synthesis). Verification: FoVer (ACL 2026) trains PRMs from formal verification across 12 benchmarks; imperfect verifier research (arXiv 2604.07666, arXiv 2026) shows ≤15% noise is tolerable with precision mattering more than recall. Concurrent: Adaptive Problem Generation (arXiv 2602.19187, Feb 2026) uses SymPy in closed-loop RLVR but adapts difficulty globally without error-type diagnosis. SwS (NeurIPS 2025) identifies weaknesses via pass-rate analysis without formal diagnosis. Reasoning Core (March 2026) generates verifiable symbolic data but is not error-targeted or iterative. Safe (ACL 2025) does step-aware Lean 4 verification in one-shot refinement, not closed-loop. Bidirectional Curriculum (March 2026) dynamically adjusts difficulty without formal verification. NSRSA (arXiv 2026) uses SymPy arithmetic verification for iterative self-training on GSM8K with solution-level DPO, but covers only arithmetic operations without error categorization or targeted synthesis. MATH-VF (arXiv 2025) uses Z3+SymPy for step-wise verification but as a training-free inference tool.\n\n## Proposed Approach\n\nFormalLoop runs iterative cycles on a student model (Qwen3.5-9B primary, Qwen3.5-4B validation): (1) student solves problems, (2) solutions are formalized and verified step-by-step via Z3/SymPy, (3) step-level errors classified into a formal taxonomy (algebraic manipulation, equation solving, arithmetic, constraint reasoning, logical inference), (4) SymPy-based synthesis generates targeted problems exercising weak skills with solver-guaranteed solutions, (5) student trains via SFT+DPO on targeted data and formally-constructed preference pairs, then re-profiled.\n\n**Formal coverage scope**: Formal verification covers algebraic and arithmetic domains amenable to Z3/SymPy (Algebra, Number Theory, Prealgebra, portions of Intermediate Algebra and Precalculus). Geometry and Counting & Probability use outcome-based verification as fallback. Per-category formalization success rates are reported. Even partial coverage with near-zero noise can outperform full-coverage noisy LLM diagnosis (imperfect verifier research, arXiv 2604.07666).\n\n**Formalization quality control**: To prevent conflating formalization failures with reasoning errors: (a) distinguish \"verification failed\" from \"formalization failed\" status, (b) exclude solutions where formal rejection co-occurs with correct final answer, (c) use only high-confidence pairs for DPO. Target noise rate well below the 15% tolerance threshold (arXiv 2604.07666).\n\n**DPO pair construction with fallback**: Primary: step-localized pairs (shared k correct steps, diverge at k+1). When step-localized pairs are insufficient (estimated via pilot study yield analysis), mix in solution-level formally-verified pairs (NSRSA-style). Report mixing ratio and its effect on training.\n\n## Experimental Design\n\n**Models**: Qwen3.5-9B (primary, 5 iterations) + Qwen3.5-4B (validation, 3 iterations). Pilot study includes Llama 3.1-8B formalization success rate comparison (not full training loop).\n\n**Benchmarks**: GSM8K, MATH-500, Minerva Math, AMC23, AIME24, AIME25, Olympiad-Bench. OOD generalization on AIME24/25. Per-MATH-subcategory breakdown (formally-covered vs. fallback).\n\n**Evaluation protocol**: Greedy accuracy + Pass@K (K=8, 32) + majority voting@K. 3 independent runs, mean ± std, significance tests. Per-problem sampling: 16-32 solutions for DPO pair construction.\n\n**Baseline matrix**:\n- Training paradigm: Vanilla SFT (uniform), SFT+DPO (uniform), GRPO/RLVR\n- Targeting: SwS (NeurIPS 2025, pass-rate weakness targeting), STAT-style (GPT-4o teacher) profiling + targeted synthesis, subcategory-level outcome targeting\n- Symbolic: Adaptive Problem Generation (arXiv 2602.19187, global difficulty adaptation)\n- Verification: FoVer-PRM (ACL 2026, github.com/psunlpgroup/FoVer) + Best-of-N/RLVR loop, outcome-only verification loop (NSRSA-style)\n\n**Ablation studies** (priority-ranked; ablations run on Qwen3.5-4B, 2-3 iterations, 3 benchmarks: GSM8K, MATH-500, AIME24):\n1. [Must] Error profiling source: Formal vs. LLM-based vs. pass-rate-based vs. subcategory-level vs. random\n2. [Must] Preference pair source: Step-localized formal DPO vs. solution-level formal DPO (NSRSA-style) vs. outcome DPO vs. LLM-annotated DPO (Step-DPO style)\n3. [Must] Targeting vs. uniform: Targeted synthesis vs. uniform synthesis (same quantity)\n4. [Should] Training objective: SFT only vs. DPO only vs. SFT+DPO\n5. [Should] Taxonomy granularity: 5-type vs. 2-type (arithmetic/non-arithmetic) vs. single aggregate\n6. [Should] Iteration dynamics: Per-iteration accuracy, error profile evolution, formalization coverage, entropy curves\n7. [Nice] Precision-coverage tradeoff: Inject artificial noise (5%, 10%, 15%, 20%) into formal labels, measure impact on self-improvement trajectory\n\n**Compute fairness**: Unified metric: total dollar cost (GPU + CPU + API). Report per-method cost breakdown. Compute-matched comparisons: (i) fixed GPU training FLOPs, (ii) fixed total dollar budget. Accuracy vs. total cost curves.\n\n**Pilot study** (before main experiments):\n- Per-subcategory formalization success rate on MATH-Train (200-300 problems per subcategory)\n- Failure mode analysis: formalization failure vs. solver timeout vs. scope limitation\n- Selection bias analysis: compare error type distributions between formalization-success and formalization-failure groups\n- DPO pair yield estimation: 500 problems × 16 solutions, count constructable step-localized pairs\n- Cross-family comparison: Qwen3.5-9B vs. Llama 3.1-8B formalization success rates\n- Taxonomy coverage validation and comparison with STAT's skill taxonomy\n- Human evaluation of 100-200 synthesized problems (well-formedness, difficulty, NL quality)\n\n## Key References\n\n- FoVer: Efficient PRM Training Data Synthesis via Formal Verification (ACL Findings 2026)\n- STAT: Skill-Targeted Adaptive Training (ICLR 2026)\n- Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment [NSRSA] (arXiv 2026)\n- Theoretical Modeling of LLM Self-Improvement Training Dynamics Through Solver-Verifier Gap (ICLR 2026)\n- SPARQ: Synthetic Problem Generation for Reasoning via Quality-Diversity Algorithms (arXiv 2025)\n- CoTEvol: Self-Evolving Chain-of-Thoughts for Data Synthesis in Mathematical Reasoning (arXiv 2026)\n- MathMixup: Boosting LLM Mathematical Reasoning with Difficulty-Controllable Data Synthesis and Curriculum Learning (arXiv 2026)\n- Self-Error-Instruct: Generalizing from Errors for LLMs Mathematical Reasoning (ACL 2025)\n- SPICE: Self-Play In Corpus Environments Improves Reasoning (arXiv 2025)\n- SvS: Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR (arXiv 2025)\n- SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning (NeurIPS 2025)\n- Adaptive Problem Generation via Symbolic Representations (arXiv 2026, arXiv 2602.19187)\n- An Imperfect Verifier is Good Enough: Learning with Noisy Rewards (arXiv 2026, arXiv 2604.07666)\n- Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving [MATH-VF] (arXiv 2025)\n- Safe: Enhancing Mathematical Reasoning via Retrospective Step-aware Formal Verification (ACL 2025)\n- WarriorMath: Enhancing the Mathematical Ability of Large Language Models with a Defect-aware Framework (arXiv 2025)\n- Bidirectional Curriculum Generation: A Multi-Agent Framework for Data-Efficient Mathematical Reasoning (arXiv 2026)\n- Reasoning Core: A Scalable Procedural Data Generation Suite for Symbolic Pre-training and Post-Training (arXiv 2026)\n- Neuro-Symbolic Data Generation for Math Reasoning (NeurIPS 2024)\n- Step-DPO: Step-wise Preference Optimization for Long-chain Reasoning of LLMs (NeurIPS 2024)\n- Full-Step-DPO: Self-Supervised Preference Optimization with Step-wise Rewards for Mathematical Reasoning (ACL 2025 Findings)\n- LLMs Cannot Spot Math Errors Even When Allowed to Peek into the Solution (EMNLP 2025, arXiv 2509.01395)\n\n## Resource Estimate\n\n- **manual**: gpu_hours: 750 H100 hours (5 iterations 9B + 3 iterations 4B + ablations on 4B + pilot study + evaluation), timeline: 4-5 months, estimated_gpu_cost: $1,875\n- **human_in_loop**: gpu_hours: 700 H100 hours, timeline: 3-4 months, claude_api_cost: $500-700 (pipeline code, taxonomy iteration, analysis), teacher_api_cost: $200-400 (GPT-4o for STAT baseline), estimated_gpu_cost: $1,750\n- **auto_research**: gpu_hours: 700 H100 hours, timeline: 6-8 weeks, claude_api_cost: $1,500-2,500, teacher_api_cost: $200-400, estimated_gpu_cost: $1,750, speed_bottleneck: Z3/SymPy step verification is CPU-bound (~0.5-2s per step); LLM-to-formal translation ~60-70% success rate on amenable categories requires retry loops"
}
```

---

### Runtime record

_source line 2 · 2026-05-27T09:06:34.448Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T09:06:34.448Z",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa"
}
```

---

## Round 1

43 recorded events

### User

_source line 3 · 2026-05-27T09:06:34.458Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Formal Error Profiling Enables Teacher-Free Targeted Math Self-Improvement

## Core Problem

Self-improvement loops for mathematical reasoning suffer from model collapse (solver-verifier gap theory, ICLR 2026) and untargeted data waste. All existing error-targeted synthesis methods — STAT (ICLR 2026), Self-Error-Instruct (ACL 2025), SwS (NeurIPS 2025), WarriorMath (arXiv 2025) — depend on LLM teachers or LLM metacognition for error diagnosis, introducing teacher bias, hallucinated attributions, and scalability ceilings. Empirically, LLMs cannot reliably spot mathematical errors even with reference solutions (arXiv 2509.01395, EMNLP 2025). Can formal symbolic tools serve as collapse-proof verifiers and ground-truth error diagnosticians, enabling stable, teacher-free, targeted self-improvement?

## Core Contributions

1. **Teacher-free error-targeted self-improvement**: The first self-improvement system where error diagnosis and targeted synthesis are driven entirely by formal symbolic tools (Z3, SymPy), eliminating LLM teacher dependency. Unlike RLVR/GRPO (also teacher-free), FormalLoop targets specific error types rather than optimizing globally.

2. **Formally-verified step-localized DPO**: Preference pairs where trajectories share k formally-verified-correct steps and diverge at step k+1 — providing step-localized credit assignment with formal guarantees. Unlike Step-DPO (NeurIPS 2024) and Full-Step-DPO (ACL 2025 Findings) which use LLM/human annotations, and unlike NSRSA (arXiv 2026) which constructs solution-level accept/reject pairs, our pairs provide zero-noise step-localized preference signals.

3. **Ground-truth error profile dynamics**: FormalLoop uniquely enables tracking formally-verified per-skill-type error evolution across self-improvement iterations — answering whether error types have fixed reduction priority orderings, whether skill dependencies exist (e.g., arithmetic errors must resolve before algebraic errors become visible), and whether error profile entropy predicts convergence. No prior work provides ground-truth skill-decomposed self-improvement dynamics.

4. **Precision-coverage tradeoff hypothesis**: We hypothesize that in self-improvement loops, there exists a verifier noise threshold τ beyond which expanding coverage yields negative marginal returns. Imperfect verifier research (arXiv 2604.07666, arXiv 2026) estimates τ ≈ 15%; solver-verifier gap theory (ICLR 2026) predicts verifier reliability determines the self-improvement ceiling. FormalLoop tests this: formal verification achieves near-zero noise within its scope (~60-70% of amenable categories), which should outperform full-coverage but noisier LLM diagnosis. We validate via noise injection ablation.

## Why Not Simpler Alternatives?

**vs. Outcome verification + STAT-style LLM teacher profiling**: (1) Error attribution precision — outcome verification doesn't localize errors; LLM step diagnosis hallucinates (arXiv 2509.01395, EMNLP 2025); formal verification provides guaranteed step-level attribution. (2) Iterative stability — LLM teacher biases compound across iterations; formal diagnosis is independently calibrated each round. (3) No teacher ceiling — STAT's profiling quality is bounded by teacher metacognition.

**vs. Subcategory-level outcome targeting** (using MATH's existing 7 subcategory labels to oversample weak categories): This requires no formal verification at all. However, subcategory labels are coarse — within Algebra alone, a model may struggle specifically with equation solving but not algebraic manipulation. Formal step-level diagnosis provides within-subcategory skill decomposition that subcategory-level targeting cannot. We include subcategory-level targeting as an explicit baseline to quantify this granularity advantage.

**vs. FoVer-PRM as verifier in a standard self-improvement loop**: FoVer (ACL 2026) trains PRMs from formal verification data for general use. A natural alternative is using a FoVer-trained PRM as the verifier in a self-improvement loop (via Best-of-N or RLVR). FormalLoop differs by using formal verification directly for error categorization and targeted synthesis — not indirectly through a learned PRM. We include FoVer-PRM + RLVR as a baseline to isolate direct formal profiling's advantage.

## Research Landscape

Current SOTA in synthetic math data: SPARQ (June 2025, +24% via quality-diversity from 7.5K seeds), CoTEvol (April 2026, +6.6% via evolutionary CoT synthesis), MathMixup (Jan 2026, 47.6% on 7 benchmarks via difficulty-controlled curriculum). Self-improvement: SPICE (Oct 2025, +8.9% via document-grounded self-play), SvS (Aug 2025, +18.3% Pass@32 on AIME24 via variational problem synthesis). Verification: FoVer (ACL 2026) trains PRMs from formal verification across 12 benchmarks; imperfect verifier research (arXiv 2604.07666, arXiv 2026) shows ≤15% noise is tolerable with precision mattering more than recall. Concurrent: Adaptive Problem Generation (arXiv 2602.19187, Feb 2026) uses SymPy in closed-loop RLVR but adapts difficulty globally without error-type diagnosis. SwS (NeurIPS 2025) identifies weaknesses via pass-rate analysis without formal diagnosis. Reasoning Core (March 2026) generates verifiable symbolic data but is not error-targeted or iterative. Safe (ACL 2025) does step-aware Lean 4 verification in one-shot refinement, not closed-loop. Bidirectional Curriculum (March 2026) dynamically adjusts difficulty without formal verification. NSRSA (arXiv 2026) uses SymPy arithmetic verification for iterative self-training on GSM8K with solution-level DPO, but covers only arithmetic operations without error categorization or targeted synthesis. MATH-VF (arXiv 2025) uses Z3+SymPy for step-wise verification but as a training-free inference tool.

## Proposed Approach

FormalLoop runs iterative cycles on a student model (Qwen3.5-9B primary, Qwen3.5-4B validation): (1) student solves problems, (2) solutions are formalized and verified step-by-step via Z3/SymPy, (3) step-level errors classified into a formal taxonomy (algebraic manipulation, equation solving, arithmetic, constraint reasoning, logical inference), (4) SymPy-based synthesis generates targeted problems exercising weak skills with solver-guaranteed solutions, (5) student trains via SFT+DPO on targeted data and formally-constructed preference pairs, then re-profiled.

**Formal coverage scope**: Formal verification covers algebraic and arithmetic domains amenable to Z3/SymPy (Algebra, Number Theory, Prealgebra, portions of Intermediate Algebra and Precalculus). Geometry and Counting & Probability use outcome-based verification as fallback. Per-category formalization success rates are reported. Even partial coverage with near-zero noise can outperform full-coverage noisy LLM diagnosis (imperfect verifier research, arXiv 2604.07666).

**Formalization quality control**: To prevent conflating formalization failures with reasoning errors: (a) distinguish "verification failed" from "formalization failed" status, (b) exclude solutions where formal rejection co-occurs with correct final answer, (c) use only high-confidence pairs for DPO. Target noise rate well below the 15% tolerance threshold (arXiv 2604.07666).

**DPO pair construction with fallback**: Primary: step-localized pairs (shared k correct steps, diverge at k+1). When step-localized pairs are insufficient (estimated via pilot study yield analysis), mix in solution-level formally-verified pairs (NSRSA-style). Report mixing ratio and its effect on training.

## Experimental Design

**Models**: Qwen3.5-9B (primary, 5 iterations) + Qwen3.5-4B (validation, 3 iterations). Pilot study includes Llama 3.1-8B formalization success rate comparison (not full training loop).

**Benchmarks**: GSM8K, MATH-500, Minerva Math, AMC23, AIME24, AIME25, Olympiad-Bench. OOD generalization on AIME24/25. Per-MATH-subcategory breakdown (formally-covered vs. fallback).

**Evaluation protocol**: Greedy accuracy + Pass@K (K=8, 32) + majority voting@K. 3 independent runs, mean ± std, significance tests. Per-problem sampling: 16-32 solutions for DPO pair construction.

**Baseline matrix**:
- Training paradigm: Vanilla SFT (uniform), SFT+DPO (uniform), GRPO/RLVR
- Targeting: SwS (NeurIPS 2025, pass-rate weakness targeting), STAT-style (GPT-4o teacher) profiling + targeted synthesis, subcategory-level outcome targeting
- Symbolic: Adaptive Problem Generation (arXiv 2602.19187, global difficulty adaptation)
- Verification: FoVer-PRM (ACL 2026, github.com/psunlpgroup/FoVer) + Best-of-N/RLVR loop, outcome-only verification loop (NSRSA-style)

**Ablation studies** (priority-ranked; ablations run on Qwen3.5-4B, 2-3 iterations, 3 benchmarks: GSM8K, MATH-500, AIME24):
1. [Must] Error profiling source: Formal vs. LLM-based vs. pass-rate-based vs. subcategory-level vs. random
2. [Must] Preference pair source: Step-localized formal DPO vs. solution-level formal DPO (NSRSA-style) vs. outcome DPO vs. LLM-annotated DPO (Step-DPO style)
3. [Must] Targeting vs. uniform: Targeted synthesis vs. uniform synthesis (same quantity)
4. [Should] Training objective: SFT only vs. DPO only vs. SFT+DPO
5. [Should] Taxonomy granularity: 5-type vs. 2-type (arithmetic/non-arithmetic) vs. single aggregate
6. [Should] Iteration dynamics: Per-iteration accuracy, error profile evolution, formalization coverage, entropy curves
7. [Nice] Precision-coverage tradeoff: Inject artificial noise (5%, 10%, 15%, 20%) into formal labels, measure impact on self-improvement trajectory

**Compute fairness**: Unified metric: total dollar cost (GPU + CPU + API). Report per-method cost breakdown. Compute-matched comparisons: (i) fixed GPU training FLOPs, (ii) fixed total dollar budget. Accuracy vs. total cost curves.

**Pilot study** (before main experiments):
- Per-subcategory formalization success rate on MATH-Train (200-300 problems per subcategory)
- Failure mode analysis: formalization failure vs. solver timeout vs. scope limitation
- Selection bias analysis: compare error type distributions between formalization-success and formalization-failure groups
- DPO pair yield estimation: 500 problems × 16 solutions, count constructable step-localized pairs
- Cross-family comparison: Qwen3.5-9B vs. Llama 3.1-8B formalization success rates
- Taxonomy coverage validation and comparison with STAT's skill taxonomy
- Human evaluation of 100-200 synthesized problems (well-formedness, difficulty, NL quality)

## Key References

- FoVer: Efficient PRM Training Data Synthesis via Formal Verification (ACL Findings 2026)
- STAT: Skill-Targeted Adaptive Training (ICLR 2026)
- Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment [NSRSA] (arXiv 2026)
- Theoretical Modeling of LLM Self-Improvement Training Dynamics Through Solver-Verifier Gap (ICLR 2026)
- SPARQ: Synthetic Problem Generation for Reasoning via Quality-Diversity Algorithms (arXiv 2025)
- CoTEvol: Self-Evolving Chain-of-Thoughts for Data Synthesis in Mathematical Reasoning (arXiv 2026)
- MathMixup: Boosting LLM Mathematical Reasoning with Difficulty-Controllable Data Synthesis and Curriculum Learning (arXiv 2026)
- Self-Error-Instruct: Generalizing from Errors for LLMs Mathematical Reasoning (ACL 2025)
- SPICE: Self-Play In Corpus Environments Improves Reasoning (arXiv 2025)
- SvS: Beyond Pass@1: Self-Play with Variational Problem Synthesis Sustains RLVR (arXiv 2025)
- SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning (NeurIPS 2025)
- Adaptive Problem Generation via Symbolic Representations (arXiv 2026, arXiv 2602.19187)
- An Imperfect Verifier is Good Enough: Learning with Noisy Rewards (arXiv 2026, arXiv 2604.07666)
- Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving [MATH-VF] (arXiv 2025)
- Safe: Enhancing Mathematical Reasoning via Retrospective Step-aware Formal Verification (ACL 2025)
- WarriorMath: Enhancing the Mathematical Ability of Large Language Models with a Defect-aware Framework (arXiv 2025)
- Bidirectional Curriculum Generation: A Multi-Agent Framework for Data-Efficient Mathematical Reasoning (arXiv 2026)
- Reasoning Core: A Scalable Procedural Data Generation Suite for Symbolic Pre-training and Post-Training (arXiv 2026)
- Neuro-Symbolic Data Generation for Math Reasoning (NeurIPS 2024)
- Step-DPO: Step-wise Preference Optimization for Long-chain Reasoning of LLMs (NeurIPS 2024)
- Full-Step-DPO: Self-Supervised Preference Optimization with Step-wise Rewards for Mathematical Reasoning (ACL 2025 Findings)
- LLMs Cannot Spot Math Errors Even When Allowed to Peek into the Solution (EMNLP 2025, arXiv 2509.01395)

## Resource Estimate

- **manual**: gpu_hours: 750 H100 hours (5 iterations 9B + 3 iterations 4B + ablations on 4B + pilot study + evaluation), timeline: 4-5 months, estimated_gpu_cost: $1,875
- **human_in_loop**: gpu_hours: 700 H100 hours, timeline: 3-4 months, claude_api_cost: $500-700 (pipeline code, taxonomy iteration, analysis), teacher_api_cost: $200-400 (GPT-4o for STAT baseline), estimated_gpu_cost: $1,750
- **auto_research**: gpu_hours: 700 H100 hours, timeline: 6-8 weeks, claude_api_cost: $1,500-2,500, teacher_api_cost: $200-400, estimated_gpu_cost: $1,750, speed_bottleneck: Z3/SymPy step verification is CPU-bound (~0.5-2s per step); LLM-to-formal translation ~60-70% success rate on amenable categories requires retry loops

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "c26b7c12-66cf-45ce-b59f-91fbd9337461",
  "type": "user",
  "uuid": "8760ec00-2da4-44ad-a90c-377ca1848a10",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T09:06:34.457Z_

```json
{
  "parentUuid": "8760ec00-2da4-44ad-a90c-377ca1848a10",
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
  "uuid": "d108989b-d173-4402-8c6c-ca677315dfd9",
  "timestamp": "2026-05-27T09:06:34.457Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T09:06:34.457Z_

```json
{
  "parentUuid": "d108989b-d173-4402-8c6c-ca677315dfd9",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d8866e4a-134e-41e0-b879-6aceabf6dba7",
  "timestamp": "2026-05-27T09:06:34.457Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal error profiling for teacher-free math self-improvement",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa"
}
```

---

### Assistant

_source line 7 · 2026-05-27T09:06:43.811Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to evaluate a research proposal for AAAI 2026. I need to follow the rubric carefully:

1. First, do 3-5 WebSearch queries to understand the field
2. Then evaluate the idea quality on 3 dimensions (Novelty, Significance, Related Work)
3. Answer the Trivial Alternative and Premise Assumption checks
4. Output in the specified format

Let me start by searching for the key topics in this proposal. The proposal is about using formal symbolic tools (Z3, SymPy) for teacher-free targeted math self-improvement in LLMs.

Let me search for:


1. Formal verification for LLM math reasoning self-improvement
2. STAT skill-targeted adaptive training
3. FoVer formal verification PRM
4. Step-DPO and step-level preference optimization
5. LLM self-improvement math reasoning 2025-2026

I'll load the WebSearch tool and run these queries to understand the current landscape of work in this area.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d8866e4a-134e-41e0-b879-6aceabf6dba7",
  "isSidechain": false,
  "requestId": "req_011CbSoqGPVKsJ6mL3qYjtK7",
  "type": "assistant",
  "uuid": "0f272db4-c2c9-4015-a975-1896310114d0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lw51udEbaWAxkSNeazVCmp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 19236,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 311,
          "cache_read_input_tokens": 19236,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 8 · 2026-05-27T09:06:43.816Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LkMb6bA4uYYSSCj6nH1rYh`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f272db4-c2c9-4015-a975-1896310114d0",
  "isSidechain": false,
  "requestId": "req_011CbSoqGPVKsJ6mL3qYjtK7",
  "type": "assistant",
  "uuid": "ac49f6b0-92ac-4ca9-9a3c-c5825cd4afe4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lw51udEbaWAxkSNeazVCmp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 19236,
      "output_tokens": 311,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 311,
          "cache_read_input_tokens": 19236,
          "cache_creation_input_tokens": 0,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 0
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

_source line 9 · 2026-05-27T09:06:43.824Z_

<details><summary>↩ Tool result · `toolu_01LkMb6bA4uYYSSCj6nH1rYh`</summary>

````text
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
  "parentUuid": "ac49f6b0-92ac-4ca9-9a3c-c5825cd4afe4",
  "isSidechain": false,
  "promptId": "c26b7c12-66cf-45ce-b59f-91fbd9337461",
  "type": "user",
  "uuid": "7f8e72cf-cf2a-4227-9edf-61aa975b65ed",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "ac49f6b0-92ac-4ca9-9a3c-c5825cd4afe4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 10_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Formal Error Profiling Enables Teacher-Free Targeted Math Self-Improvement  ## Core Problem  Self-improvement lo…",
  "leafUuid": "7f8e72cf-cf2a-4227-9edf-61aa975b65ed",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal error profiling for teacher-free math self-improvement",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa"
}
```

---

### Assistant

_source line 12 · 2026-05-27T09:06:48.921Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me do 3-5 targeted web searches to understand the field before evaluating the proposal. Let me search for:

1. Formal verification for LLM math self-improvement (FoVer, MATH-VF, Safe)
2. STAT skill-targeted adaptive training ICLR 2026
3. NSRSA symbolic recursive self-alignment math
4. Step-DPO step-level preference optimization math reasoning
5. LLM self-improvement math reasoning 2025-2026 survey


I'll run these searches in parallel to gather the background information I need.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7f8e72cf-cf2a-4227-9edf-61aa975b65ed",
  "isSidechain": false,
  "requestId": "req_011CbSoqxXUcAauW19K1tFWg",
  "type": "assistant",
  "uuid": "ca868f40-f7c7-496f-a2b7-87e07b9eb14c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Go96Rk3yA7o1hEBXK2gE2x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 839,
      "cache_read_input_tokens": 19236,
      "output_tokens": 435,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 435,
          "cache_read_input_tokens": 19236,
          "cache_creation_input_tokens": 839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 839
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

_source line 13 · 2026-05-27T09:06:48.923Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FWkL94Xw727i6fYkpqJJXo`</summary>

```json
{
  "query": "FoVer formal verification PRM training LLM math reasoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ca868f40-f7c7-496f-a2b7-87e07b9eb14c",
  "isSidechain": false,
  "requestId": "req_011CbSoqxXUcAauW19K1tFWg",
  "type": "assistant",
  "uuid": "45944924-9a84-49b6-a97e-d13838849d6f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Go96Rk3yA7o1hEBXK2gE2x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 839,
      "cache_read_input_tokens": 19236,
      "output_tokens": 435,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 435,
          "cache_read_input_tokens": 19236,
          "cache_creation_input_tokens": 839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 839
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

_source line 14 · 2026-05-27T09:06:49.191Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GkzEzVxEM6ABdW13q7JLLR`</summary>

```json
{
  "query": "STAT skill-targeted adaptive training ICLR 2026 math LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45944924-9a84-49b6-a97e-d13838849d6f",
  "isSidechain": false,
  "requestId": "req_011CbSoqxXUcAauW19K1tFWg",
  "type": "assistant",
  "uuid": "52a817dd-c467-49d4-a2e6-b294e3976ded",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Go96Rk3yA7o1hEBXK2gE2x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 839,
      "cache_read_input_tokens": 19236,
      "output_tokens": 435,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 435,
          "cache_read_input_tokens": 19236,
          "cache_creation_input_tokens": 839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 839
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

_source line 15 · 2026-05-27T09:06:49.682Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018piMmPDm34aDNXc4HmdDj5`</summary>

```json
{
  "query": "NSRSA symbolic recursive self-alignment SymPy math self-improvement iterative"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52a817dd-c467-49d4-a2e6-b294e3976ded",
  "isSidechain": false,
  "requestId": "req_011CbSoqxXUcAauW19K1tFWg",
  "type": "assistant",
  "uuid": "373faa8c-2714-4dd7-9efb-d208d79cef0d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Go96Rk3yA7o1hEBXK2gE2x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 839,
      "cache_read_input_tokens": 19236,
      "output_tokens": 435,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 435,
          "cache_read_input_tokens": 19236,
          "cache_creation_input_tokens": 839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 839
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

_source line 16 · 2026-05-27T09:06:50.672Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014ZtiQ5ExsGAW1vQSCauvnn`</summary>

```json
{
  "query": "formal verification Z3 SymPy step-level error diagnosis LLM mathematical reasoning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "373faa8c-2714-4dd7-9efb-d208d79cef0d",
  "isSidechain": false,
  "requestId": "req_011CbSoqxXUcAauW19K1tFWg",
  "type": "assistant",
  "uuid": "57235888-e447-42d6-acb3-f398e23d4f7f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Go96Rk3yA7o1hEBXK2gE2x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 839,
      "cache_read_input_tokens": 19236,
      "output_tokens": 435,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 435,
          "cache_read_input_tokens": 19236,
          "cache_creation_input_tokens": 839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 839
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

_source line 17 · 2026-05-27T09:06:51.216Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KGWhm7w2m2d9nTLsJyWF9n`</summary>

```json
{
  "query": "LLM math self-improvement teacher-free targeted synthesis error profiling 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57235888-e447-42d6-acb3-f398e23d4f7f",
  "isSidechain": false,
  "requestId": "req_011CbSoqxXUcAauW19K1tFWg",
  "type": "assistant",
  "uuid": "6fb9d9c6-1cf0-4213-a3ce-5599d86fd8d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Go96Rk3yA7o1hEBXK2gE2x",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 839,
      "cache_read_input_tokens": 19236,
      "output_tokens": 435,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 435,
          "cache_read_input_tokens": 19236,
          "cache_creation_input_tokens": 839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 839
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

_source line 18 · 2026-05-27T09:06:56.586Z_

<details><summary>↩ Tool result · `toolu_01FWkL94Xw727i6fYkpqJJXo`</summary>

```text
Web search results for query: "FoVer formal verification PRM training LLM math reasoning 2025 2026"

Links: [{"title":"[2505.15960] Efficient PRM Training Data Synthesis via Formal Verification","url":"https://arxiv.org/abs/2505.15960"},{"title":"Generalizable Process Reward Models via Formally Verified Training Data | OpenReview","url":"https://openreview.net/forum?id=LAejsDitr3"},{"title":"FOVER: Training Verifiers with Formal Tools","url":"https://www.emergentmind.com/papers/2505.15960"},{"title":"Efficient PRM Training Data Synthesis via Formal Verification","url":"https://arxiv.org/html/2505.15960v3"},{"title":"Paper page - Training Step-Level Reasoning Verifiers with Formal Verification Tools","url":"https://huggingface.co/papers/2505.15960"},{"title":"GitHub - psunlpgroup/FoVer: This repository includes code and materials for the paper \"Efficient PRM Training Data Synthesis via Formal Verification\" (ACL 2026 Findings). · GitHub","url":"https://github.com/psunlpgroup/FoVer"},{"title":"000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019","url":"https://openreview.net/pdf?id=LAejsDitr3"},{"title":"Training Step-Level Reasoning Verifiers with Formal ...","url":"https://arxiv.org/pdf/2505.15960"}]

Based on the search results, here's what I found about FoVer:

## Overview

FoVer is a framework that synthesizes PRM training data from formal reasoning tasks by annotating step-level error labels using formal verification tools such as Z3 and Isabelle. Process Reward Models (PRMs) have emerged as a promising approach for improving LLM reasoning capabilities by providing process supervision over reasoning traces.

## Key Innovation

By leveraging formal verification, FoVer enables efficient and accurate PRM data construction without requiring human annotation or additional LLM calls. This addresses a significant challenge, as existing approaches for constructing PRM training data remain costly and noisy, as they typically rely on human annotation or sampling-based labeling methods that require repeated LLM calls.

## Training Data and Applications

FoVer creates PRM training data from formal logic and theorem proving tasks. PRMs trained with FoVer improve performance on diverse reasoning tasks, including MATH, AIME, and MMLU. PRM training data created using formal verification improves PRMs on informal reasoning tasks written in natural language.

## Recent Publication

The work was published in Findings of the Association for Computational Linguistics: ACL 2026, with the paper submitted in May 2025 and revised in April 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45944924-9a84-49b6-a97e-d13838849d6f",
  "isSidechain": false,
  "promptId": "c26b7c12-66cf-45ce-b59f-91fbd9337461",
  "type": "user",
  "uuid": "73d8bbb4-8bab-42fc-9fc5-45ab905c081a",
  "toolUseResult": {
    "query": "FoVer formal verification PRM training LLM math reasoning 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Caj7wXdQHHPYzUrm1Cw77E",
        "content": [
          {
            "title": "[2505.15960] Efficient PRM Training Data Synthesis via Formal Verification",
            "url": "https://arxiv.org/abs/2505.15960"
          },
          {
            "title": "Generalizable Process Reward Models via Formally Verified Training Data | OpenReview",
            "url": "https://openreview.net/forum?id=LAejsDitr3"
          },
          {
            "title": "FOVER: Training Verifiers with Formal Tools",
            "url": "https://www.emergentmind.com/papers/2505.15960"
          },
          {
            "title": "Efficient PRM Training Data Synthesis via Formal Verification",
            "url": "https://arxiv.org/html/2505.15960v3"
          },
          {
            "title": "Paper page - Training Step-Level Reasoning Verifiers with Formal Verification Tools",
            "url": "https://huggingface.co/papers/2505.15960"
          },
          {
            "title": "GitHub - psunlpgroup/FoVer: This repository includes code and materials for the paper \"Efficient PRM Training Data Synthesis via Formal Verification\" (ACL 2026 Findings). · GitHub",
            "url": "https://github.com/psunlpgroup/FoVer"
          },
          {
            "title": "000 001 002 003 004 005 006 007 008 009 010 011 012 013 014 015 016 017 018 019",
            "url": "https://openreview.net/pdf?id=LAejsDitr3"
          },
          {
            "title": "Training Step-Level Reasoning Verifiers with Formal ...",
            "url": "https://arxiv.org/pdf/2505.15960"
          }
        ]
      },
      "Based on the search results, here's what I found about FoVer:\n\n## Overview\n\nFoVer is a framework that synthesizes PRM training data from formal reasoning tasks by annotating step-level error labels using formal verification tools such as Z3 and Isabelle. Process Reward Models (PRMs) have emerged as a promising approach for improving LLM reasoning capabilities by providing process supervision over reasoning traces.\n\n## Key Innovation\n\nBy leveraging formal verification, FoVer enables efficient and accurate PRM data construction without requiring human annotation or additional LLM calls. This addresses a significant challenge, as existing approaches for constructing PRM training data remain costly and noisy, as they typically rely on human annotation or sampling-based labeling methods that require repeated LLM calls.\n\n## Training Data and Applications\n\nFoVer creates PRM training data from formal logic and theorem proving tasks. PRMs trained with FoVer improve performance on diverse reasoning tasks, including MATH, AIME, and MMLU. PRM training data created using formal verification improves PRMs on informal reasoning tasks written in natural language.\n\n## Recent Publication\n\nThe work was published in Findings of the Association for Computational Linguistics: ACL 2026, with the paper submitted in May 2025 and revised in April 2026."
    ],
    "durationSeconds": 7.6586103340000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "45944924-9a84-49b6-a97e-d13838849d6f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-27T09:06:57.863Z_

<details><summary>↩ Tool result · `toolu_018piMmPDm34aDNXc4HmdDj5`</summary>

```text
Web search results for query: "NSRSA symbolic recursive self-alignment SymPy math self-improvement iterative"

Links: [{"title":"Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment","url":"https://arxiv.org/pdf/2603.21558"},{"title":"Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment","url":"https://arxiv.org/html/2603.21558"},{"title":"[2603.21558] Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment","url":"https://arxiv.org/abs/2603.21558"},{"title":"Recursive Self-Improvement","url":"https://www.emergentmind.com/topics/recursive-self-improvement"},{"title":"SAHOO: Safeguarded Alignment for High-Order Optimization Objectives in Recursive Self-Improvement","url":"https://arxiv.org/html/2603.06333"}]

The search results reveal information about **NSRSA (Neuro-Symbolic Recursive Self-Alignment)**, a recent research framework published in March 2026.

## Overview

NSRSA stabilizes iterative self-training by embedding a symbolic verification subsystem that gates training data quality at the reasoning step level. The approach addresses recursive self-improvement—where a model iteratively trains on its own outputs—which promises sustained capability growth but faces the fundamental obstacle of recursive drift, where errors in intermediate reasoning compound across multiple iterations, leading to mode collapse and performance degradation.

## Key Technical Features

NSRSA verifies each arithmetic operation via sympy, checks logical flow consistency across reasoning steps, and enforces domain constraints. Unlike traditional approaches that only filter based on final answers, NSRSA rejects approximately 34% of correct-answer solutions that pass outcome verification, eliminating "lucky guesses" with flawed reasoning from the training set.

## Performance Results

The method was evaluated on GSM8K using Qwen3-4B-Thinking across 5 self-training iterations, and demonstrated that constructing DPO preference pairs from NSRSA verification teaches the model to distinguish sound from flawed reasoning, improving reward accuracy from 46% to 63%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "373faa8c-2714-4dd7-9efb-d208d79cef0d",
  "isSidechain": false,
  "promptId": "c26b7c12-66cf-45ce-b59f-91fbd9337461",
  "type": "user",
  "uuid": "3f73d416-311f-4ee0-87a3-527eac653532",
  "toolUseResult": {
    "query": "NSRSA symbolic recursive self-alignment SymPy math self-improvement iterative",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Wf8U8imyt66CCTXoWTHhi3",
        "content": [
          {
            "title": "Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment",
            "url": "https://arxiv.org/pdf/2603.21558"
          },
          {
            "title": "Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment",
            "url": "https://arxiv.org/html/2603.21558"
          },
          {
            "title": "[2603.21558] Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment",
            "url": "https://arxiv.org/abs/2603.21558"
          },
          {
            "title": "Recursive Self-Improvement",
            "url": "https://www.emergentmind.com/topics/recursive-self-improvement"
          },
          {
            "title": "SAHOO: Safeguarded Alignment for High-Order Optimization Objectives in Recursive Self-Improvement",
            "url": "https://arxiv.org/html/2603.06333"
          }
        ]
      },
      "The search results reveal information about **NSRSA (Neuro-Symbolic Recursive Self-Alignment)**, a recent research framework published in March 2026.\n\n## Overview\n\nNSRSA stabilizes iterative self-training by embedding a symbolic verification subsystem that gates training data quality at the reasoning step level. The approach addresses recursive self-improvement—where a model iteratively trains on its own outputs—which promises sustained capability growth but faces the fundamental obstacle of recursive drift, where errors in intermediate reasoning compound across multiple iterations, leading to mode collapse and performance degradation.\n\n## Key Technical Features\n\nNSRSA verifies each arithmetic operation via sympy, checks logical flow consistency across reasoning steps, and enforces domain constraints. Unlike traditional approaches that only filter based on final answers, NSRSA rejects approximately 34% of correct-answer solutions that pass outcome verification, eliminating \"lucky guesses\" with flawed reasoning from the training set.\n\n## Performance Results\n\nThe method was evaluated on GSM8K using Qwen3-4B-Thinking across 5 self-training iterations, and demonstrated that constructing DPO preference pairs from NSRSA verification teaches the model to distinguish sound from flawed reasoning, improving reward accuracy from 46% to 63%."
    ],
    "durationSeconds": 8.169893057,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "373faa8c-2714-4dd7-9efb-d208d79cef0d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-27T09:06:57.878Z_

<details><summary>↩ Tool result · `toolu_014ZtiQ5ExsGAW1vQSCauvnn`</summary>

```text
Web search results for query: "formal verification Z3 SymPy step-level error diagnosis LLM mathematical reasoning 2025 2026"

Links: [{"title":"[Literature Review] Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving","url":"https://www.themoonlight.io/en/review/step-wise-formal-verification-for-llm-based-mathematical-problem-solving"},{"title":"Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving","url":"https://arxiv.org/html/2505.20869v1"},{"title":"[2505.15960] Training Step-Level Reasoning Verifiers with ...","url":"https://arxiv.org/abs/2505.15960"},{"title":"Training Step-Level Reasoning Verifiers with Formal ...","url":"https://arxiv.org/pdf/2505.15960"},{"title":"Step-Wise Formal Verification for LLM-Based Mathematical ...","url":"https://arxiv.org/pdf/2505.20869"},{"title":"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification","url":"https://arxiv.org/pdf/2506.04592"}]

Based on the search results, here are several recent papers and frameworks related to formal verification, Z3, SymPy, step-level error diagnosis, and LLM mathematical reasoning:

## Key Frameworks and Research (2025-2026)

### MATH-VF: Step-Wise Formal Verification
MATH-VF is a framework for step-wise formal verification of mathematical problem solutions generated by LLMs that aims to formally verify the correctness of each step and provide feedback for errors. The framework integrates LLMs with external tools such as SymPy and Z3-Solver for determining the correctness of mathematical problem solving steps. MATH-VF is a training-free framework for step-by-step verification of mathematical reasoning that not only evaluates the correctness of solutions, but also provides constructive feedback for incorrect ones.

### FoVer: Formal Verification for PRM Training
FoVer is a framework that synthesizes Process Reward Model (PRM) training data from formal reasoning tasks by annotating step-level error labels using formal verification tools such as Z3 and Isabelle, enabling efficient and accurate PRM data construction without requiring human annotation or additional LLM calls.

### SAFE: Retrospective Step-Aware Formal Verification
SAFE is the first study utilizing formal mathematics language Lean 4 to verify the correctness of mathematical reasoning trajectories generated by LLMs. It proposes a step-level formal verifier that outputs one of four distinct states, depending on whether a given step can be auto-formalized by an LLM and resolved by an automated theorem prover.

These recent approaches represent significant advances in combining formal verification tools with LLMs for improved mathematical reasoning and error diagnosis.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57235888-e447-42d6-acb3-f398e23d4f7f",
  "isSidechain": false,
  "promptId": "c26b7c12-66cf-45ce-b59f-91fbd9337461",
  "type": "user",
  "uuid": "7e5f5efa-4105-49da-bafe-916f2b49552a",
  "toolUseResult": {
    "query": "formal verification Z3 SymPy step-level error diagnosis LLM mathematical reasoning 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_012jZSVWvkb5cKdYKrKVtYhT",
        "content": [
          {
            "title": "[Literature Review] Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving",
            "url": "https://www.themoonlight.io/en/review/step-wise-formal-verification-for-llm-based-mathematical-problem-solving"
          },
          {
            "title": "Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving",
            "url": "https://arxiv.org/html/2505.20869v1"
          },
          {
            "title": "[2505.15960] Training Step-Level Reasoning Verifiers with ...",
            "url": "https://arxiv.org/abs/2505.15960"
          },
          {
            "title": "Training Step-Level Reasoning Verifiers with Formal ...",
            "url": "https://arxiv.org/pdf/2505.15960"
          },
          {
            "title": "Step-Wise Formal Verification for LLM-Based Mathematical ...",
            "url": "https://arxiv.org/pdf/2505.20869"
          },
          {
            "title": "Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification",
            "url": "https://arxiv.org/pdf/2506.04592"
          }
        ]
      },
      "Based on the search results, here are several recent papers and frameworks related to formal verification, Z3, SymPy, step-level error diagnosis, and LLM mathematical reasoning:\n\n## Key Frameworks and Research (2025-2026)\n\n### MATH-VF: Step-Wise Formal Verification\nMATH-VF is a framework for step-wise formal verification of mathematical problem solutions generated by LLMs that aims to formally verify the correctness of each step and provide feedback for errors. The framework integrates LLMs with external tools such as SymPy and Z3-Solver for determining the correctness of mathematical problem solving steps. MATH-VF is a training-free framework for step-by-step verification of mathematical reasoning that not only evaluates the correctness of solutions, but also provides constructive feedback for incorrect ones.\n\n### FoVer: Formal Verification for PRM Training\nFoVer is a framework that synthesizes Process Reward Model (PRM) training data from formal reasoning tasks by annotating step-level error labels using formal verification tools such as Z3 and Isabelle, enabling efficient and accurate PRM data construction without requiring human annotation or additional LLM calls.\n\n### SAFE: Retrospective Step-Aware Formal Verification\nSAFE is the first study utilizing formal mathematics language Lean 4 to verify the correctness of mathematical reasoning trajectories generated by LLMs. It proposes a step-level formal verifier that outputs one of four distinct states, depending on whether a given step can be auto-formalized by an LLM and resolved by an automated theorem prover.\n\nThese recent approaches represent significant advances in combining formal verification tools with LLMs for improved mathematical reasoning and error diagnosis."
    ],
    "durationSeconds": 7.2033466509999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "57235888-e447-42d6-acb3-f398e23d4f7f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-27T09:06:57.913Z_

<details><summary>↩ Tool result · `toolu_01GkzEzVxEM6ABdW13q7JLLR`</summary>

```text
Web search results for query: "STAT skill-targeted adaptive training ICLR 2026 math LLM"

Links: [{"title":"STAT: Skill-Targeted Adaptive Training | OpenReview","url":"https://openreview.net/forum?id=m3jG3GaNIj"},{"title":"ICLR Poster STAT: Skill-Targeted Adaptive Training","url":"https://iclr.cc/virtual/2026/poster/10007620"},{"title":"[2510.10023] Skill-Targeted Adaptive Training","url":"https://arxiv.org/abs/2510.10023"},{"title":"Skill-Targeted Adaptive Training","url":"https://arxiv.org/html/2510.10023"},{"title":"Skill-Targeted Adaptive Training | Princeton Language and Intelligence","url":"https://pli.princeton.edu/events/2026/skill-targeted-adaptive-training"},{"title":"Preprint. Under review. Skill-Targeted Adaptive Training","url":"https://arxiv.org/pdf/2510.10023"},{"title":"ICLR 2026 Schedule","url":"https://iclr.cc/virtual/2026/calendar"}]

Based on the search results, I found information about STAT (Skill-Targeted Adaptive Training), which was presented at ICLR 2026.

## Overview

STAT is a new fine-tuning strategy to train a student model by using the metacognition ability of a stronger large language model (LLM) as the teacher.

## How STAT Works

The teacher uses the task dataset to create a list of skills needed for the task, and then labels each data point with its required skills. By monitoring the student's answers, the teacher creates a Missing-Skill-Profile for the student, tracking how often they failed to apply each skill in their responses.

The method has two variants:
- In STAT-Sel, the teacher uses an existing set of training examples but adaptively reweights them according to the Missing-Skill-Profile.
- In STAT-Syn, the teacher synthesizes additional examples involving missing skills.

## Results

Across extensive experiments on Llama and Qwen models, the methods yield improvements of up to 7.5% on MATH, whereas SFT provides only limited gains. Furthermore, STAT enhances performance on out-of-distribution benchmarks (e.g., AIME24/25, AMC23, etc.) by an average of 4.6%.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "52a817dd-c467-49d4-a2e6-b294e3976ded",
  "isSidechain": false,
  "promptId": "c26b7c12-66cf-45ce-b59f-91fbd9337461",
  "type": "user",
  "uuid": "f432f332-90ea-4e46-8e39-29dc6d37eb80",
  "toolUseResult": {
    "query": "STAT skill-targeted adaptive training ICLR 2026 math LLM",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HkrRvbSeU5m3bZzpn3EgLV",
        "content": [
          {
            "title": "STAT: Skill-Targeted Adaptive Training | OpenReview",
            "url": "https://openreview.net/forum?id=m3jG3GaNIj"
          },
          {
            "title": "ICLR Poster STAT: Skill-Targeted Adaptive Training",
            "url": "https://iclr.cc/virtual/2026/poster/10007620"
          },
          {
            "title": "[2510.10023] Skill-Targeted Adaptive Training",
            "url": "https://arxiv.org/abs/2510.10023"
          },
          {
            "title": "Skill-Targeted Adaptive Training",
            "url": "https://arxiv.org/html/2510.10023"
          },
          {
            "title": "Skill-Targeted Adaptive Training | Princeton Language and Intelligence",
            "url": "https://pli.princeton.edu/events/2026/skill-targeted-adaptive-training"
          },
          {
            "title": "Preprint. Under review. Skill-Targeted Adaptive Training",
            "url": "https://arxiv.org/pdf/2510.10023"
          },
          {
            "title": "ICLR 2026 Schedule",
            "url": "https://iclr.cc/virtual/2026/calendar"
          }
        ]
      },
      "Based on the search results, I found information about STAT (Skill-Targeted Adaptive Training), which was presented at ICLR 2026.\n\n## Overview\n\nSTAT is a new fine-tuning strategy to train a student model by using the metacognition ability of a stronger large language model (LLM) as the teacher.\n\n## How STAT Works\n\nThe teacher uses the task dataset to create a list of skills needed for the task, and then labels each data point with its required skills. By monitoring the student's answers, the teacher creates a Missing-Skill-Profile for the student, tracking how often they failed to apply each skill in their responses.\n\nThe method has two variants:\n- In STAT-Sel, the teacher uses an existing set of training examples but adaptively reweights them according to the Missing-Skill-Profile.\n- In STAT-Syn, the teacher synthesizes additional examples involving missing skills.\n\n## Results\n\nAcross extensive experiments on Llama and Qwen models, the methods yield improvements of up to 7.5% on MATH, whereas SFT provides only limited gains. Furthermore, STAT enhances performance on out-of-distribution benchmarks (e.g., AIME24/25, AMC23, etc.) by an average of 4.6%."
    ],
    "durationSeconds": 8.720399418000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "52a817dd-c467-49d4-a2e6-b294e3976ded",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-27T09:07:02.376Z_

<details><summary>↩ Tool result · `toolu_01KGWhm7w2m2d9nTLsJyWF9n`</summary>

```text
Web search results for query: "LLM math self-improvement teacher-free targeted synthesis error profiling 2025 2026"

Links: [{"title":"Self-Error-Instruct: Generalizing from Errors for LLMs Mathematical Reasoning","url":"https://arxiv.org/pdf/2505.22591"},{"title":"Reflect, Retry, Reward: Self-Improving LLMs via Reinforcement Learning","url":"https://arxiv.org/pdf/2505.24726"},{"title":"WarriorMath: Enhancing the Mathematical Ability of Large Language Models with a Defect-aware Framework","url":"https://arxiv.org/pdf/2508.01245"},{"title":"Skill-Targeted Adaptive Training","url":"https://arxiv.org/pdf/2510.10023"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/871ac99fdc5282d0301934d23945ebaa-Paper-Conference.pdf"},{"title":"S^3cMath: Spontaneous Step-level Self-correction Makes Large Language Models Better Mathematical Reasoners","url":"https://arxiv.org/pdf/2409.01524"},{"title":"Self-Explore: Enhancing Mathematical Reasoning in Language Models with   Fine-grained Rewards","url":"https://arxiv.org/pdf/2404.10346"}]

I found several relevant research papers on LLM self-improvement and mathematical reasoning. Here are the key findings:

## Recent Research on LLM Math Self-Improvement (2025-2026)

**Self-Error-Instruct (SEI)**: This framework synthesizes more generalized targeted training data for mathematical reasoning. It generates error keyphrases for bad cases, identifies error types by clustering, and then synthesizes additional training data using a self-instruct approach.

**WarriorMath Framework**: An "Exam Committee" of multiple expert LLMs generates, critiques, and refines problems, retaining only the failure data where the base LLMs struggled. This defect-aware approach addresses model capability defects rather than just increasing difficulty, as increasing difficulty does not necessarily target the failure cases of base LLMs.

**Skill-Targeted Adaptive Training (STAT)**: STAT-Syn synthesizes new questions using frontier LLMs targeted to missing skills.

**Self-Correction with Reinforcement Learning (SCoRe)**: SCoRe is a multi-turn RL approach for teaching LLMs how to correct their own mistakes, attaining an absolute 15.6% gain on self-correction for reasoning problems from MATH and 9.1% gain on coding problems.

These approaches share common themes around error profiling, targeted data synthesis, and teacher-free (or minimal external supervision) improvement mechanisms for mathematical reasoning in LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6fb9d9c6-1cf0-4213-a3ce-5599d86fd8d4",
  "isSidechain": false,
  "promptId": "c26b7c12-66cf-45ce-b59f-91fbd9337461",
  "type": "user",
  "uuid": "a1816aac-3282-4ee3-887a-67c0c3814e14",
  "toolUseResult": {
    "query": "LLM math self-improvement teacher-free targeted synthesis error profiling 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VPe6xU7E4sBfrmcoGYJWLk",
        "content": [
          {
            "title": "Self-Error-Instruct: Generalizing from Errors for LLMs Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2505.22591"
          },
          {
            "title": "Reflect, Retry, Reward: Self-Improving LLMs via Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2505.24726"
          },
          {
            "title": "WarriorMath: Enhancing the Mathematical Ability of Large Language Models with a Defect-aware Framework",
            "url": "https://arxiv.org/pdf/2508.01245"
          },
          {
            "title": "Skill-Targeted Adaptive Training",
            "url": "https://arxiv.org/pdf/2510.10023"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/871ac99fdc5282d0301934d23945ebaa-Paper-Conference.pdf"
          },
          {
            "title": "S^3cMath: Spontaneous Step-level Self-correction Makes Large Language Models Better Mathematical Reasoners",
            "url": "https://arxiv.org/pdf/2409.01524"
          },
          {
            "title": "Self-Explore: Enhancing Mathematical Reasoning in Language Models with   Fine-grained Rewards",
            "url": "https://arxiv.org/pdf/2404.10346"
          }
        ]
      },
      "I found several relevant research papers on LLM self-improvement and mathematical reasoning. Here are the key findings:\n\n## Recent Research on LLM Math Self-Improvement (2025-2026)\n\n**Self-Error-Instruct (SEI)**: This framework synthesizes more generalized targeted training data for mathematical reasoning. It generates error keyphrases for bad cases, identifies error types by clustering, and then synthesizes additional training data using a self-instruct approach.\n\n**WarriorMath Framework**: An \"Exam Committee\" of multiple expert LLMs generates, critiques, and refines problems, retaining only the failure data where the base LLMs struggled. This defect-aware approach addresses model capability defects rather than just increasing difficulty, as increasing difficulty does not necessarily target the failure cases of base LLMs.\n\n**Skill-Targeted Adaptive Training (STAT)**: STAT-Syn synthesizes new questions using frontier LLMs targeted to missing skills.\n\n**Self-Correction with Reinforcement Learning (SCoRe)**: SCoRe is a multi-turn RL approach for teaching LLMs how to correct their own mistakes, attaining an absolute 15.6% gain on self-correction for reasoning problems from MATH and 9.1% gain on coding problems.\n\nThese approaches share common themes around error profiling, targeted data synthesis, and teacher-free (or minimal external supervision) improvement mechanisms for mathematical reasoning in LLMs."
    ],
    "durationSeconds": 11.157761521000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6fb9d9c6-1cf0-4213-a3ce-5599d86fd8d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Formal Error Profiling Enables Teacher-Free Targeted Math Self-Improvement  ## Core Problem  Self-improvement lo…",
  "leafUuid": "a1816aac-3282-4ee3-887a-67c0c3814e14",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa"
}
```

---

### Runtime record

_source line 24_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal error profiling for teacher-free math self-improvement",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa"
}
```

---

### Assistant

_source line 25 · 2026-05-27T09:07:06.734Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have initial search results. Let me do a few more targeted searches to understand:
1. The solver-verifier gap theory (ICLR 2026)
2. The imperfect verifier paper (arXiv 2604.07666)
3. SwS self-aware weakness-driven problem synthesis (NeurIPS 2025)
4. Adaptive Problem Generation via Symbolic Representations (arXiv 2602.19187)

Let me search for these.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1816aac-3282-4ee3-887a-67c0c3814e14",
  "isSidechain": false,
  "requestId": "req_011CbSosKcGkzt2bSQDtH7BG",
  "type": "assistant",
  "uuid": "78e525fe-1b00-4185-8c8f-dde5862035c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VM7CvfJPAEy5y7CV6NQFL6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3814,
      "cache_read_input_tokens": 20075,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3814,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 319,
          "cache_read_input_tokens": 20075,
          "cache_creation_input_tokens": 3814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3814
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

_source line 26 · 2026-05-27T09:07:07.799Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XJNrTGftDf2KLn5GCpuyXv`</summary>

```json
{
  "query": "solver-verifier gap theory LLM self-improvement ICLR 2026 model collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78e525fe-1b00-4185-8c8f-dde5862035c9",
  "isSidechain": false,
  "requestId": "req_011CbSosKcGkzt2bSQDtH7BG",
  "type": "assistant",
  "uuid": "bf68e138-4ef3-43d2-acfd-9588f97dd1ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VM7CvfJPAEy5y7CV6NQFL6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3814,
      "cache_read_input_tokens": 20075,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3814,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 319,
          "cache_read_input_tokens": 20075,
          "cache_creation_input_tokens": 3814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3814
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

_source line 27 · 2026-05-27T09:07:08.266Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019qFyaqcafKYxo83hCLfpVX`</summary>

```json
{
  "query": "imperfect verifier noisy rewards LLM math arXiv 2604.07666 precision coverage tradeoff 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf68e138-4ef3-43d2-acfd-9588f97dd1ac",
  "isSidechain": false,
  "requestId": "req_011CbSosKcGkzt2bSQDtH7BG",
  "type": "assistant",
  "uuid": "d2c98539-faf8-4977-992e-cad10b84d3c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VM7CvfJPAEy5y7CV6NQFL6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3814,
      "cache_read_input_tokens": 20075,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3814,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 319,
          "cache_read_input_tokens": 20075,
          "cache_creation_input_tokens": 3814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3814
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

_source line 28 · 2026-05-27T09:07:08.682Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CtuQyf5AvuL7TPVC7KD4SQ`</summary>

```json
{
  "query": "SwS self-aware weakness-driven problem synthesis NeurIPS 2025 reinforcement learning reasoning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2c98539-faf8-4977-992e-cad10b84d3c0",
  "isSidechain": false,
  "requestId": "req_011CbSosKcGkzt2bSQDtH7BG",
  "type": "assistant",
  "uuid": "24dd8095-9383-4d0b-b925-f6f513350096",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VM7CvfJPAEy5y7CV6NQFL6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3814,
      "cache_read_input_tokens": 20075,
      "output_tokens": 319,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3814,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 319,
          "cache_read_input_tokens": 20075,
          "cache_creation_input_tokens": 3814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3814
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

_source line 29 · 2026-05-27T09:07:15.215Z_

<details><summary>↩ Tool result · `toolu_019qFyaqcafKYxo83hCLfpVX`</summary>

```text
Web search results for query: "imperfect verifier noisy rewards LLM math arXiv 2604.07666 precision coverage tradeoff 2026"

Links: [{"title":"An Imperfect Verifier is Good Enough: Learning with Noisy Rewards","url":"https://arxiv.org/html/2604.07666"},{"title":"[2604.07666] An Imperfect Verifier is Good Enough: Learning with Noisy Rewards","url":"https://arxiv.org/abs/2604.07666"},{"title":"Reinforcement Learning with Verifiable yet Noisy Rewards under Imperfect Verifiers","url":"https://arxiv.org/html/2510.00915v1"},{"title":"An Imperfect Verifier is Good Enough: Learning with Noisy Rewards","url":"https://arxiv.org/pdf/2604.07666"},{"title":"[2510.00915] Reinforcement Learning with Verifiable yet Noisy Rewards under Imperfect Verifiers","url":"https://arxiv.org/abs/2510.00915"}]

I found the paper you're looking for. Here's what I can tell you about arXiv paper 2604.07666:

The paper "An Imperfect Verifier is Good Enough: Learning with Noisy Rewards" addresses the issue that while Reinforcement Learning with Verifiable Rewards (RLVR) has become prominent for post-training LLMs, verifiers are rarely error-free, and questions remain about how robust RLVR is to such noise and what verifier accuracy is required for effective training.

The authors investigate these questions in the domains of code generation and scientific reasoning by introducing noise into RL training.

**Key Findings:**

Noise rates up to 15% yield peak validation accuracy within 2 percentage points of the clean baseline, with findings consistent across controlled and model-based noise types, three model families (Qwen3, GLM4, Llama 3.1), and model sizes from 4B to 9B.

**Precision-Coverage Tradeoff:**

The findings suggest that practitioners should prioritize moderate accuracy with high precision over perfect verification — which directly addresses the precision-coverage tradeoff you mentioned. Overall, the results indicate that imperfect verification does not constitute a fundamental barrier to RLVR.

The paper was submitted on April 9, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2c98539-faf8-4977-992e-cad10b84d3c0",
  "isSidechain": false,
  "promptId": "c26b7c12-66cf-45ce-b59f-91fbd9337461",
  "type": "user",
  "uuid": "6e3ff890-2ca0-4044-be29-b056a466b454",
  "toolUseResult": {
    "query": "imperfect verifier noisy rewards LLM math arXiv 2604.07666 precision coverage tradeoff 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Qwyeoq1G6VMKVsyoJpqLTY",
        "content": [
          {
            "title": "An Imperfect Verifier is Good Enough: Learning with Noisy Rewards",
            "url": "https://arxiv.org/html/2604.07666"
          },
          {
            "title": "[2604.07666] An Imperfect Verifier is Good Enough: Learning with Noisy Rewards",
            "url": "https://arxiv.org/abs/2604.07666"
          },
          {
            "title": "Reinforcement Learning with Verifiable yet Noisy Rewards under Imperfect Verifiers",
            "url": "https://arxiv.org/html/2510.00915v1"
          },
          {
            "title": "An Imperfect Verifier is Good Enough: Learning with Noisy Rewards",
            "url": "https://arxiv.org/pdf/2604.07666"
          },
          {
            "title": "[2510.00915] Reinforcement Learning with Verifiable yet Noisy Rewards under Imperfect Verifiers",
            "url": "https://arxiv.org/abs/2510.00915"
          }
        ]
      },
      "I found the paper you're looking for. Here's what I can tell you about arXiv paper 2604.07666:\n\nThe paper \"An Imperfect Verifier is Good Enough: Learning with Noisy Rewards\" addresses the issue that while Reinforcement Learning with Verifiable Rewards (RLVR) has become prominent for post-training LLMs, verifiers are rarely error-free, and questions remain about how robust RLVR is to such noise and what verifier accuracy is required for effective training.\n\nThe authors investigate these questions in the domains of code generation and scientific reasoning by introducing noise into RL training.\n\n**Key Findings:**\n\nNoise rates up to 15% yield peak validation accuracy within 2 percentage points of the clean baseline, with findings consistent across controlled and model-based noise types, three model families (Qwen3, GLM4, Llama 3.1), and model sizes from 4B to 9B.\n\n**Precision-Coverage Tradeoff:**\n\nThe findings suggest that practitioners should prioritize moderate accuracy with high precision over perfect verification — which directly addresses the precision-coverage tradeoff you mentioned. Overall, the results indicate that imperfect verification does not constitute a fundamental barrier to RLVR.\n\nThe paper was submitted on April 9, 2026."
    ],
    "durationSeconds": 6.9452309930000045,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d2c98539-faf8-4977-992e-cad10b84d3c0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-27T09:07:15.247Z_

<details><summary>↩ Tool result · `toolu_01XJNrTGftDf2KLn5GCpuyXv`</summary>

```text
Web search results for query: "solver-verifier gap theory LLM self-improvement ICLR 2026 model collapse"

Links: [{"title":"Published as a conference paper at ICLR 2026 THEORETICAL MODELING","url":"https://openreview.net/pdf?id=Hh7x3c0cZl"},{"title":"Theoretical Modeling of LLM Self-Improvement Training Dynamics Through Solver-Verifier Gap","url":"https://arxiv.org/html/2507.00075v3"},{"title":"Theoretical Modeling of LLM Self-Improvement Training Dynamics Through Solver-Verifier Gap","url":"https://www.researchgate.net/publication/393260770_Theoretical_Modeling_of_LLM_Self-Improvement_Training_Dynamics_Through_Solver-Verifier_Gap"},{"title":"Theoretical Modeling of Large Language Model Self-Improvement Training Dynamics Through Solver-Verifier Gap","url":"https://arxiv.org/html/2507.00075"},{"title":"Theoretical Modeling of LLM Self-Improvement Training ...","url":"https://arxiv.org/pdf/2507.00075"},{"title":"[2507.00075] Theoretical Modeling of Large Language Model Self-Improvement Training Dynamics Through Solver-Verifier Gap","url":"https://arxiv.org/abs/2507.00075"}]

I found research on the solver-verifier gap theory for LLM self-improvement. Here are the key findings:

## Research Overview

The paper theoretically models the training dynamics of self-improvement via the concept of solver-verifier gap, inspired by the conjecture that performance enhancement of self-improvement stems from the gap between LLM's solver capability and verifier capability.

## Key Concepts

Solver capability is defined as the quality of responses directly generated from an LLM, while verifier capability refers to the quality of responses generated from an LLM and evaluated by an LLM.

## Main Findings

Experimental results across various models and datasets reveal that the capability dynamics indeed follow an exponential law, as implied by the theoretical framework. Theoretical derivations imply an exponential law for the model capability, and the framework further establishes the extreme capability based on this framework.

The verifier capability consistently outperforms the solver throughout the self-improvement process, which provides empirical evidence of the solver-verifier gap's crucial role in driving capability improvement.

## Framework Applications

Beyond self-improvement, the analysis investigates how external data influences these dynamics within the framework, finding that under limited external data regimes, such external data can be utilized at any stage without significantly affecting final performances.

The framework allows quantifying the capability limit of self-improvement by fitting the theoretical model to the experiment results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf68e138-4ef3-43d2-acfd-9588f97dd1ac",
  "isSidechain": false,
  "promptId": "c26b7c12-66cf-45ce-b59f-91fbd9337461",
  "type": "user",
  "uuid": "1bdceabe-bf3d-4017-a793-67808d56f740",
  "toolUseResult": {
    "query": "solver-verifier gap theory LLM self-improvement ICLR 2026 model collapse",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FKTA6Kxh86BqppD9pXrJek",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2026 THEORETICAL MODELING",
            "url": "https://openreview.net/pdf?id=Hh7x3c0cZl"
          },
          {
            "title": "Theoretical Modeling of LLM Self-Improvement Training Dynamics Through Solver-Verifier Gap",
            "url": "https://arxiv.org/html/2507.00075v3"
          },
          {
            "title": "Theoretical Modeling of LLM Self-Improvement Training Dynamics Through Solver-Verifier Gap",
            "url": "https://www.researchgate.net/publication/393260770_Theoretical_Modeling_of_LLM_Self-Improvement_Training_Dynamics_Through_Solver-Verifier_Gap"
          },
          {
            "title": "Theoretical Modeling of Large Language Model Self-Improvement Training Dynamics Through Solver-Verifier Gap",
            "url": "https://arxiv.org/html/2507.00075"
          },
          {
            "title": "Theoretical Modeling of LLM Self-Improvement Training ...",
            "url": "https://arxiv.org/pdf/2507.00075"
          },
          {
            "title": "[2507.00075] Theoretical Modeling of Large Language Model Self-Improvement Training Dynamics Through Solver-Verifier Gap",
            "url": "https://arxiv.org/abs/2507.00075"
          }
        ]
      },
      "I found research on the solver-verifier gap theory for LLM self-improvement. Here are the key findings:\n\n## Research Overview\n\nThe paper theoretically models the training dynamics of self-improvement via the concept of solver-verifier gap, inspired by the conjecture that performance enhancement of self-improvement stems from the gap between LLM's solver capability and verifier capability.\n\n## Key Concepts\n\nSolver capability is defined as the quality of responses directly generated from an LLM, while verifier capability refers to the quality of responses generated from an LLM and evaluated by an LLM.\n\n## Main Findings\n\nExperimental results across various models and datasets reveal that the capability dynamics indeed follow an exponential law, as implied by the theoretical framework. Theoretical derivations imply an exponential law for the model capability, and the framework further establishes the extreme capability based on this framework.\n\nThe verifier capability consistently outperforms the solver throughout the self-improvement process, which provides empirical evidence of the solver-verifier gap's crucial role in driving capability improvement.\n\n## Framework Applications\n\nBeyond self-improvement, the analysis investigates how external data influences these dynamics within the framework, finding that under limited external data regimes, such external data can be utilized at any stage without significantly affecting final performances.\n\nThe framework allows quantifying the capability limit of self-improvement by fitting the theoretical model to the experiment results."
    ],
    "durationSeconds": 7.444591932000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bf68e138-4ef3-43d2-acfd-9588f97dd1ac",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-27T09:07:16.526Z_

<details><summary>↩ Tool result · `toolu_01CtuQyf5AvuL7TPVC7KD4SQ`</summary>

```text
Web search results for query: "SwS self-aware weakness-driven problem synthesis NeurIPS 2025 reinforcement learning reasoning"

Links: [{"title":"SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning | OpenReview","url":"https://openreview.net/forum?id=0jQUNQsZra"},{"title":"SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/sws-self-aware-weakness-driven-problem-synthesis-in-reinforcement-learning-for-llm-reasoning/"},{"title":"NeurIPS Poster SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning","url":"https://neurips.cc/virtual/2025/poster/120292"},{"title":"SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning","url":"https://arxiv.org/pdf/2506.08989"},{"title":"GitHub - MasterVito/SwS: Official Repo for SwS: A Weakness-driven Problem Synthesis Framework in RL for LLM Reasoning","url":"https://github.com/MasterVito/SwS"},{"title":"SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning","url":"https://mastervito.github.io/MasterVito.SwS.github.io/"},{"title":"[2506.08989] SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning","url":"https://arxiv.org/abs/2506.08989"},{"title":"Self-aware Weakness-Driven Synthesis Framework","url":"https://www.emergentmind.com/topics/self-aware-weakness-driven-problem-synthesis-framework-sws"},{"title":"SwS: Self-aware Weakness-driven Problem Synthesis in ...","url":"https://openreview.net/pdf/c3403842de341324f63358f1732f1518761661f2.pdf"},{"title":"SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning","url":"https://arxiv.org/html/2506.08989v1"}]

I found comprehensive information about SwS! Here are the key details:

## Overview

SwS is a NeurIPS 2025 poster presentation about a framework for reinforcement learning with verifiable rewards to train large language models on complex reasoning tasks such as mathematical problem solving.

## The Problem

A prerequisite for the scalability of RLVR is a high-quality problem set with precise and verifiable answers. However, the scarcity of well-crafted human-labeled math problems and limited-verification answers in existing distillation-oriented synthetic datasets limit their effectiveness in RL. Additionally, most problem synthesis strategies indiscriminately expand the problem set without considering the model's capabilities, leading to low efficiency in generating useful questions.

## The Solution

SwS is a Self-aware Weakness-driven Problem Synthesis framework that leverages the model's self-identified weaknesses in RL to generate synthetic problems for training augmentation. The framework records problems that the model consistently struggles to solve or learns inefficiently through iterative sampling during a preliminary RL training phase, and these failed problems are grouped by categories, leveraged to extract common concepts, and used to synthesize new problems with difficulty levels tailored to the model's capabilities.

## Results

The framework yields average performance gains of 10.0% and 7.7% on 7B and 32B models across eight mainstream reasoning benchmarks.

You can find the paper on arXiv (arxiv.org/abs/2506.08989), OpenReview, and Microsoft Research, as well as the official GitHub repository at github.com/MasterVito/SwS.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "24dd8095-9383-4d0b-b925-f6f513350096",
  "isSidechain": false,
  "promptId": "c26b7c12-66cf-45ce-b59f-91fbd9337461",
  "type": "user",
  "uuid": "2d3c3127-3c5a-45aa-aadd-7e65e82ebf76",
  "toolUseResult": {
    "query": "SwS self-aware weakness-driven problem synthesis NeurIPS 2025 reinforcement learning reasoning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GEA8ydpswvTXmkqApCDq5h",
        "content": [
          {
            "title": "SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=0jQUNQsZra"
          },
          {
            "title": "SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning - Microsoft Research",
            "url": "https://www.microsoft.com/en-us/research/publication/sws-self-aware-weakness-driven-problem-synthesis-in-reinforcement-learning-for-llm-reasoning/"
          },
          {
            "title": "NeurIPS Poster SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning",
            "url": "https://neurips.cc/virtual/2025/poster/120292"
          },
          {
            "title": "SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning",
            "url": "https://arxiv.org/pdf/2506.08989"
          },
          {
            "title": "GitHub - MasterVito/SwS: Official Repo for SwS: A Weakness-driven Problem Synthesis Framework in RL for LLM Reasoning",
            "url": "https://github.com/MasterVito/SwS"
          },
          {
            "title": "SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning",
            "url": "https://mastervito.github.io/MasterVito.SwS.github.io/"
          },
          {
            "title": "[2506.08989] SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning",
            "url": "https://arxiv.org/abs/2506.08989"
          },
          {
            "title": "Self-aware Weakness-Driven Synthesis Framework",
            "url": "https://www.emergentmind.com/topics/self-aware-weakness-driven-problem-synthesis-framework-sws"
          },
          {
            "title": "SwS: Self-aware Weakness-driven Problem Synthesis in ...",
            "url": "https://openreview.net/pdf/c3403842de341324f63358f1732f1518761661f2.pdf"
          },
          {
            "title": "SwS: Self-aware Weakness-driven Problem Synthesis in Reinforcement Learning for LLM Reasoning",
            "url": "https://arxiv.org/html/2506.08989v1"
          }
        ]
      },
      "I found comprehensive information about SwS! Here are the key details:\n\n## Overview\n\nSwS is a NeurIPS 2025 poster presentation about a framework for reinforcement learning with verifiable rewards to train large language models on complex reasoning tasks such as mathematical problem solving.\n\n## The Problem\n\nA prerequisite for the scalability of RLVR is a high-quality problem set with precise and verifiable answers. However, the scarcity of well-crafted human-labeled math problems and limited-verification answers in existing distillation-oriented synthetic datasets limit their effectiveness in RL. Additionally, most problem synthesis strategies indiscriminately expand the problem set without considering the model's capabilities, leading to low efficiency in generating useful questions.\n\n## The Solution\n\nSwS is a Self-aware Weakness-driven Problem Synthesis framework that leverages the model's self-identified weaknesses in RL to generate synthetic problems for training augmentation. The framework records problems that the model consistently struggles to solve or learns inefficiently through iterative sampling during a preliminary RL training phase, and these failed problems are grouped by categories, leveraged to extract common concepts, and used to synthesize new problems with difficulty levels tailored to the model's capabilities.\n\n## Results\n\nThe framework yields average performance gains of 10.0% and 7.7% on 7B and 32B models across eight mainstream reasoning benchmarks.\n\nYou can find the paper on arXiv (arxiv.org/abs/2506.08989), OpenReview, and Microsoft Research, as well as the official GitHub repository at github.com/MasterVito/SwS."
    ],
    "durationSeconds": 7.841164800000006,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "24dd8095-9383-4d0b-b925-f6f513350096",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-27T09:07:21.051Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me do one more search to understand the adaptive problem generation paper and see if there's any very closely related work that directly does what FormalLoop proposes.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d3c3127-3c5a-45aa-aadd-7e65e82ebf76",
  "isSidechain": false,
  "requestId": "req_011CbSotN77mpY41aN9rPURp",
  "type": "assistant",
  "uuid": "99eda267-a170-4736-b60f-937d8a0d7675",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MoJpa7upmDnTdTxr2VgFMW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2598,
      "cache_read_input_tokens": 23889,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2598,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 23889,
          "cache_creation_input_tokens": 2598,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2598
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

_source line 33 · 2026-05-27T09:07:21.908Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FPtPXubdeW5vv2WGC7dYpV`</summary>

```json
{
  "query": "adaptive problem generation symbolic representations SymPy closed-loop RLVR arXiv 2602.19187 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "99eda267-a170-4736-b60f-937d8a0d7675",
  "isSidechain": false,
  "requestId": "req_011CbSotN77mpY41aN9rPURp",
  "type": "assistant",
  "uuid": "f34dedd2-7e79-4efc-bb6c-04643a692302",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MoJpa7upmDnTdTxr2VgFMW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2598,
      "cache_read_input_tokens": 23889,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2598,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 23889,
          "cache_creation_input_tokens": 2598,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2598
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

_source line 34 · 2026-05-27T09:07:24.834Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GcHdcXXx3daY8vwC1JnzRG`</summary>

```json
{
  "query": "\"formal error profiling\" OR \"formal error diagnosis\" OR \"symbolic error categorization\" LLM math training loop 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f34dedd2-7e79-4efc-bb6c-04643a692302",
  "isSidechain": false,
  "requestId": "req_011CbSotN77mpY41aN9rPURp",
  "type": "assistant",
  "uuid": "334064d2-4a60-449a-ab3f-7a7a1bbb4810",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MoJpa7upmDnTdTxr2VgFMW",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2598,
      "cache_read_input_tokens": 23889,
      "output_tokens": 194,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2598,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 194,
          "cache_read_input_tokens": 23889,
          "cache_creation_input_tokens": 2598,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2598
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

_source line 35 · 2026-05-27T09:07:32.685Z_

<details><summary>↩ Tool result · `toolu_01FPtPXubdeW5vv2WGC7dYpV`</summary>

```text
Web search results for query: "adaptive problem generation symbolic representations SymPy closed-loop RLVR arXiv 2602.19187 2026"

Links: [{"title":"[2602.19187] Adaptive Problem Generation via Symbolic Representations","url":"https://arxiv.org/abs/2602.19187"},{"title":"Adaptive Problem Generation via Symbolic Representations","url":"https://arxiv.org/pdf/2602.19187"},{"title":"Adaptive Problem Generation via Symbolic Representations","url":"https://arxiv.org/html/2602.19187"},{"title":"System and method of adaptive generation of problem determination decision procedures","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7831537"},{"title":"Curiosity-driven RL for symbolic equation solving Kevin P. O’Keeffe","url":"https://www.arxiv.org/pdf/2510.17022"}]

I found the paper! Here are the key details about arXiv 2602.19187:

**Title:** Adaptive Problem Generation via Symbolic Representations

**Main Contribution:** The paper presents a method for generating training data for reinforcement learning with verifiable rewards to improve small open-weights language models on mathematical tasks.

**Key Approach:** The method performs modifications in a symbolic problem space, representing each problem as a set of symbolic variables and constraints (e.g., via algebraic frameworks such as SymPy or SMT formulations), which enables precise control over problem structure, automatic generation of ground-truth solutions, and decouples mathematical reasoning from linguistic realization.

**Problem with Existing Methods:** Existing data generation approaches rely on open-loop pipelines and fixed modifications that do not adapt to the model's capabilities.

**Solution:** The work introduces a closed-loop framework that learns modification strategies through prompt optimization in symbolic space to adapt the problem difficulty to the model.

**Results:** Experimental results demonstrate that both adaptive problem generation and symbolic representation modifications contribute to improving the model's math solving ability.

The paper was published on February 22, 2026, and combines the concepts of RLVR (reinforcement learning with verifiable rewards) with closed-loop adaptive problem generation for mathematical reasoning tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f34dedd2-7e79-4efc-bb6c-04643a692302",
  "isSidechain": false,
  "promptId": "c26b7c12-66cf-45ce-b59f-91fbd9337461",
  "type": "user",
  "uuid": "52733172-ebca-45d4-b6c1-8d81718ee873",
  "toolUseResult": {
    "query": "adaptive problem generation symbolic representations SymPy closed-loop RLVR arXiv 2602.19187 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TZfHQBxmZyWk565BcuvpM5",
        "content": [
          {
            "title": "[2602.19187] Adaptive Problem Generation via Symbolic Representations",
            "url": "https://arxiv.org/abs/2602.19187"
          },
          {
            "title": "Adaptive Problem Generation via Symbolic Representations",
            "url": "https://arxiv.org/pdf/2602.19187"
          },
          {
            "title": "Adaptive Problem Generation via Symbolic Representations",
            "url": "https://arxiv.org/html/2602.19187"
          },
          {
            "title": "System and method of adaptive generation of problem determination decision procedures",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/7831537"
          },
          {
            "title": "Curiosity-driven RL for symbolic equation solving Kevin P. O’Keeffe",
            "url": "https://www.arxiv.org/pdf/2510.17022"
          }
        ]
      },
      "I found the paper! Here are the key details about arXiv 2602.19187:\n\n**Title:** Adaptive Problem Generation via Symbolic Representations\n\n**Main Contribution:** The paper presents a method for generating training data for reinforcement learning with verifiable rewards to improve small open-weights language models on mathematical tasks.\n\n**Key Approach:** The method performs modifications in a symbolic problem space, representing each problem as a set of symbolic variables and constraints (e.g., via algebraic frameworks such as SymPy or SMT formulations), which enables precise control over problem structure, automatic generation of ground-truth solutions, and decouples mathematical reasoning from linguistic realization.\n\n**Problem with Existing Methods:** Existing data generation approaches rely on open-loop pipelines and fixed modifications that do not adapt to the model's capabilities.\n\n**Solution:** The work introduces a closed-loop framework that learns modification strategies through prompt optimization in symbolic space to adapt the problem difficulty to the model.\n\n**Results:** Experimental results demonstrate that both adaptive problem generation and symbolic representation modifications contribute to improving the model's math solving ability.\n\nThe paper was published on February 22, 2026, and combines the concepts of RLVR (reinforcement learning with verifiable rewards) with closed-loop adaptive problem generation for mathematical reasoning tasks."
    ],
    "durationSeconds": 10.773054169000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f34dedd2-7e79-4efc-bb6c-04643a692302",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Formal Error Profiling Enables Teacher-Free Targeted Math Self-Improvement  ## Core Problem  Self-improvement lo…",
  "leafUuid": "52733172-ebca-45d4-b6c1-8d81718ee873",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal error profiling for teacher-free math self-improvement",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa"
}
```

---

### Tool result

_source line 38 · 2026-05-27T09:07:33.032Z_

<details><summary>↩ Tool result · `toolu_01GcHdcXXx3daY8vwC1JnzRG`</summary>

```text
Web search results for query: ""formal error profiling" OR "formal error diagnosis" OR "symbolic error categorization" LLM math training loop 2025 2026"

Links: [{"title":"LEMMA: Learning from Errors for MatheMatical Advancement in LLMs","url":"https://arxiv.org/html/2503.17439v1"},{"title":"Self-Error-Instruct: Generalizing from Errors for LLMs Mathematical Reasoning","url":"https://arxiv.org/pdf/2505.22591"},{"title":"Improving Math Problem Solving in Large Language Models Through   Categorization and Strategy Tailoring","url":"https://arxiv.org/pdf/2411.00042"},{"title":"Mathematical Computation and Reasoning Errors by Large Language Models","url":"https://arxiv.org/pdf/2508.09932"},{"title":"Error Classification of Large Language Models on Math Word Problems: A Dynamically Adaptive Framework","url":"https://arxiv.org/html/2501.15581v1"},{"title":"Generating Data-Driven Reasoning Rubrics for Domain-Adaptive Reward Modeling","url":"https://arxiv.org/pdf/2602.06795"},{"title":"Error Detection and Correction for Interpretable Mathematics in Large Language Models","url":"https://arxiv.org/pdf/2508.03500"},{"title":"Syntactic Blind Spots: How Misalignment Leads to LLMs Mathematical Errors","url":"https://arxiv.org/pdf/2510.01831"}]

Based on the web search results, here are the most relevant findings on formal error profiling and categorization in LLM math training:

## Recent Work on Error Categorization in LLM Math Training (2025-2026)

**LEMMA: Learning from Errors for Mathematical Advancement**

LEMMA proposes a fine-grained categorization of error types in model-generated solutions, ranging from "question misinterpretation" to "calculation error," as part of a method to systematically enhance LLMs' reflective reasoning through error-corrective trajectories. The approach uses an error-type grounded error augmentation strategy that harvests mistakes from the target model's own reasoning traces and guides advanced models to generate representative errors according to analyzed error type distributions. Models fine-tuned with LEMMA achieved up to 13.3% average accuracy improvement on LLaMA3-8B.

**Self-Error-Instruct Framework**

This framework generates error keyphrases for bad cases based on an instructor model's analysis and identifies error types by clustering these keyphrases, then samples bad cases during generation for each identified error type.

**Error Classification Approaches**

Studies have identified recurring error patterns in math reasoning by LLMs, including calculation errors, counting errors, formula confusion, question misinterpretation, missing solution steps, conceptual confusion, and nonsensical outputs.

**Symbolic Error Detection**

EDCIM uses a symbolic error-detection framework that identifies errors and provides targeted feedback for LLM-based correction in interpretable mathematics tasks.

These recent approaches demonstrate a shift toward systematic, formalized error profiling to improve LLM mathematical reasoning through structured training loops.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "334064d2-4a60-449a-ab3f-7a7a1bbb4810",
  "isSidechain": false,
  "promptId": "c26b7c12-66cf-45ce-b59f-91fbd9337461",
  "type": "user",
  "uuid": "92ca7344-01f2-431c-bfdb-6a890e227146",
  "toolUseResult": {
    "query": "\"formal error profiling\" OR \"formal error diagnosis\" OR \"symbolic error categorization\" LLM math training loop 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DmsS5TFPWuDPX15Z8TJSmV",
        "content": [
          {
            "title": "LEMMA: Learning from Errors for MatheMatical Advancement in LLMs",
            "url": "https://arxiv.org/html/2503.17439v1"
          },
          {
            "title": "Self-Error-Instruct: Generalizing from Errors for LLMs Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2505.22591"
          },
          {
            "title": "Improving Math Problem Solving in Large Language Models Through   Categorization and Strategy Tailoring",
            "url": "https://arxiv.org/pdf/2411.00042"
          },
          {
            "title": "Mathematical Computation and Reasoning Errors by Large Language Models",
            "url": "https://arxiv.org/pdf/2508.09932"
          },
          {
            "title": "Error Classification of Large Language Models on Math Word Problems: A Dynamically Adaptive Framework",
            "url": "https://arxiv.org/html/2501.15581v1"
          },
          {
            "title": "Generating Data-Driven Reasoning Rubrics for Domain-Adaptive Reward Modeling",
            "url": "https://arxiv.org/pdf/2602.06795"
          },
          {
            "title": "Error Detection and Correction for Interpretable Mathematics in Large Language Models",
            "url": "https://arxiv.org/pdf/2508.03500"
          },
          {
            "title": "Syntactic Blind Spots: How Misalignment Leads to LLMs Mathematical Errors",
            "url": "https://arxiv.org/pdf/2510.01831"
          }
        ]
      },
      "Based on the web search results, here are the most relevant findings on formal error profiling and categorization in LLM math training:\n\n## Recent Work on Error Categorization in LLM Math Training (2025-2026)\n\n**LEMMA: Learning from Errors for Mathematical Advancement**\n\nLEMMA proposes a fine-grained categorization of error types in model-generated solutions, ranging from \"question misinterpretation\" to \"calculation error,\" as part of a method to systematically enhance LLMs' reflective reasoning through error-corrective trajectories. The approach uses an error-type grounded error augmentation strategy that harvests mistakes from the target model's own reasoning traces and guides advanced models to generate representative errors according to analyzed error type distributions. Models fine-tuned with LEMMA achieved up to 13.3% average accuracy improvement on LLaMA3-8B.\n\n**Self-Error-Instruct Framework**\n\nThis framework generates error keyphrases for bad cases based on an instructor model's analysis and identifies error types by clustering these keyphrases, then samples bad cases during generation for each identified error type.\n\n**Error Classification Approaches**\n\nStudies have identified recurring error patterns in math reasoning by LLMs, including calculation errors, counting errors, formula confusion, question misinterpretation, missing solution steps, conceptual confusion, and nonsensical outputs.\n\n**Symbolic Error Detection**\n\nEDCIM uses a symbolic error-detection framework that identifies errors and provides targeted feedback for LLM-based correction in interpretable mathematics tasks.\n\nThese recent approaches demonstrate a shift toward systematic, formalized error profiling to improve LLM mathematical reasoning through structured training loops."
    ],
    "durationSeconds": 8.194845343,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "334064d2-4a60-449a-ab3f-7a7a1bbb4810",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 39 · 2026-05-27T09:07:33.036Z_

```json
{
  "parentUuid": "92ca7344-01f2-431c-bfdb-6a890e227146",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "be006c75-ebbb-4836-bb58-979f79dd1443",
  "timestamp": "2026-05-27T09:07:33.036Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 40 · 2026-05-27T09:08:40.868Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the landscape. Let me synthesize my findings and provide the evaluation.

Let me summarize what I've learned:

1. **FoVer** (ACL 2026 Findings): Uses formal verification (Z3, Isabelle) to synthesize PRM training data. Step-level error labels via formal verification. But FoVer trains PRMs — it doesn't directly use formal verification for error categorization in a self-improvement loop.

2. **STAT** (ICLR 2026): Uses a stronger LLM teacher for skill profiling and targeted synthesis. Achieves up to 7.5% improvement on MATH. 

3. **NSRSA** (arXiv 2026, March): Uses SymPy for arithmetic verification in iterative self-training on GSM8K. Constructs DPO pairs. But covers only arithmetic operations, not error categorization or targeted synthesis.

4. **Solver-Verifier Gap Theory** (ICLR 2026): Theoretical framework showing self-improvement dynamics follow exponential law, verifier capability determines ceiling.

5. **Imperfect Verifier** (arXiv 2604.07666, April 2026): Shows noise rates up to 15% are tolerable, precision matters more than recall.

Looking at more recent work, SwS uses pass-rate analysis to identify weaknesses and generate problems accordingly, while Adaptive Problem Generation applies SymPy in a closed-loop setup but focuses on global difficulty rather than specific error types. MATH-VF leverages formal verification tools for step-wise checking during inference, and Safe uses Lean 4 for formal verification in single-pass refinement. LEMMA takes error categorization further with error-corrective trajectories, though it relies on LLM-based analysis rather than formal methods. Self-Error-Instruct appears to be exploring similar territory around error identification and correction.

Now I'm assessing how novel this proposal actually is. The core idea combines formal symbolic verification for pinpointing errors at the step level, organizing those errors into a structured taxonomy, synthesizing targeted problems based on error patterns, and running an iterative improvement cycle without external teachers. The step-level DPO pairs would have formal guarantees backing them.

Looking at what's already out there, FoVer does use formal verification for step-level annotation but applies it to training process reward models rather than directly profiling errors for self-improvement. NSRSA already combines SymPy with iterative self-training and DPO, though it's limited to arithmetic problems without error categorization. STAT does skill-targeted training but requires an LLM teacher. SwS handles weakness-driven synthesis but through pass-rate analysis. The Adaptive Problem Generation work is closest in some ways but doesn't focus on error-type diagnosis.

The genuine novelty here seems to be in the specific combination—using formal verification as an error diagnostician rather than just a filter, pairing that with error categorization, then feeding those insights into targeted synthesis within a closed loop. That's not something existing work does together, though each piece individually exists elsewhere.

But I'm noticing the actual contributions are more incremental than transformative. The error taxonomy is fairly straightforward—just five categories—and the formal verification only covers about 60-70% of cases anyway, so a lot still relies on outcome-based checking. What's really happening is a compositional assembly of existing techniques: formal verification from prior work, targeted synthesis from other systems, and DPO training from Step-DPO and NSRSA. The novelty is in how they're wired together, not in fundamental innovation.

On the significance side, the problem itself matters—self-improving math reasoning without human teachers is definitely relevant. If formal error profiling substantially beats LLM-based profiling, that's a real contribution. But here's the tension: reviewers might find this somewhat predictable. Of course ground-truth error diagnosis from formal tools should outperform noisy LLM diagnosis, so the result wouldn't necessarily feel surprising, even if it's useful.

The error profile dynamics analysis is where the novelty lives—uncovering non-obvious patterns like skill dependencies or using entropy to predict convergence could yield genuine insights, though it's more of a secondary angle.

The related work section is comprehensive, covering direct competitors, formal verification approaches, self-improvement theory, and concurrent work. The differentiation from each is clear, though I should double-check if there are any gaps in the coverage.

Looking at the trivial alternatives: subcategory-level outcome targeting using MATH's existing labels, FoVer-PRM combined with standard self-improvement loops, and outcome-based verification with random oversampling of failed problems all seem like reasonable baselines the proposal is already planning to address. The question is whether the proposal's approach offers enough advantage over these simpler alternatives to justify the added complexity.

The core assumptions I need to scrutinize are whether Z3/SymPy can reliably distinguish between the five error types in the taxonomy, whether knowing the error type actually matters more than just knowing which problems failed, and whether the precision-coverage tradeoff—accepting 60-70% coverage with near-zero noise versus 100% coverage with 15% noise—actually favors formal verification in practice.

I'm also questioning whether SymPy-generated problems can match the diversity and quality of LLM-generated ones, and whether the formal taxonomy is optimized for what Z3/SymPy can diagnose rather than what actually drives model improvement.

The work has genuine strengths—it's well-positioned in the literature with a clear novelty claim around formal tools for teacher-free error profiling, and the error profile dynamics analysis is a novel analytical contribution. But the core finding feels somewhat predictable: formal verification leads to better error diagnosis, which leads to better training. The integration is novel, though each component already exists independently.

The coverage limitation around 60-70% is a practical concern, the formal taxonomy is relatively shallow, and I'm uncertain whether this approach offers a real advantage over simpler baselines like outcome-based training with oversampling. For AAAI 2026, I'd estimate around 35% probability—the idea has substance and the related work is excellent, but the predictable direction and integration-based novelty limit the ceiling.

Actually, stepping back, there are some genuinely strong elements here: the formal error profiling pipeline is novel, the step-localized DPO with formal guarantees is a clean contribution, and the error profile dynamics analysis is unique. The real question is whether the findings will be surprising—showing that better error diagnosis leads to better training is somewhat expected, but the precision-coverage tradeoff, the error dynamics patterns, and whether step-localized DPO outperforms solution-level approaches could push this higher if those results are compelling.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be006c75-ebbb-4836-bb58-979f79dd1443",
  "isSidechain": false,
  "requestId": "req_011CbSouaiv3nX6c3i76AFxy",
  "type": "assistant",
  "uuid": "895f0418-7ff6-47bd-a973-cefe9366a534",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0187SLy4bEjQfjAX6cRXJvmK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1632,
      "cache_read_input_tokens": 26487,
      "output_tokens": 6798,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1632,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6798,
          "cache_read_input_tokens": 26487,
          "cache_creation_input_tokens": 1632,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1632
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

_source line 41 · 2026-05-27T09:10:01.853Z_

Now I have sufficient research to evaluate this proposal. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:

1. **FoVer** (arXiv 2505.15960, ACL 2026 Findings): 使用 Z3/Isabelle 进行 formal verification 来合成 PRM 训练数据，实现 step-level 错误标注。与本 proposal 最直接相关——但 FoVer 的目标是训练 PRM（间接使用 formal verification），而非直接用 formal verification 进行 error categorization + targeted synthesis。本 proposal 明确将 FoVer-PRM+RLVR 作为 baseline。

2. **STAT: Skill-Targeted Adaptive Training** (arXiv 2510.10023, ICLR 2026): 使用强 LLM teacher 进行 skill profiling，识别 missing skills，然后 reweight (STAT-Sel) 或合成 (STAT-Syn) 训练数据。在 MATH 上提升 7.5%、OOD benchmark 平均 4.6%。与本 proposal 最核心的竞争关系——STAT 做的事和 FormalLoop 高度同构，区别在于 error diagnosis 来源：LLM teacher vs. formal tools。

3. **NSRSA** (arXiv 2603.21558, March 2026): 使用 SymPy 验证 arithmetic operations 来过滤 self-training 数据，构建 DPO pairs。在 GSM8K + Qwen3-4B 上测试。**这是当前与本 proposal 最接近的工作**——也用 SymPy、也做 iterative self-training、也构建 DPO pairs。但 NSRSA 仅覆盖 arithmetic verification、不做 error categorization、不做 targeted synthesis。本 proposal 的增量：error taxonomy + targeted problem generation + step-localized DPO。

4. **Solver-Verifier Gap Theory** (arXiv 2507.00075, ICLR 2026): 理论建模 self-improvement dynamics，证明 verifier capability 决定 self-improvement ceiling，dynamics 遵循 exponential law。为本 proposal 的动机提供了理论支撑——formal verification 作为 near-perfect verifier 应能提升 ceiling。

5. **Imperfect Verifier** (arXiv 2604.07666, April 2026): 实证发现 noise rate ≤15% 时 RLVR 仍可达到 clean baseline 2% 以内的 accuracy。Precision matters more than recall。这支撑了 proposal 的"precision-coverage tradeoff"假说，但也构成潜在威胁——如果 15% noise 是可容忍的，formal verification 的 near-zero noise 优势可能边际收益递减。

6. **SwS** (arXiv 2506.08989, NeurIPS 2025): 基于 pass-rate 分析识别 weakness，按 category 聚类失败问题后合成新问题。7B/32B 模型在 8 个 benchmark 平均提升 10%/7.7%。与本 proposal 竞争——SwS 不需要 formal verification，仅用 pass-rate 就能做 weakness-driven synthesis，简单得多。

7. **Adaptive Problem Generation** (arXiv 2602.19187, Feb 2026): 在 symbolic space 用 SymPy 做 closed-loop RLVR problem generation，通过 prompt optimization 适配 difficulty。与 FormalLoop 共享"SymPy + closed-loop"元素，但不做 error-type diagnosis。

8. **LEMMA** (arXiv 2503.17439, 2025): 对 LLM 生成的 math solutions 做 fine-grained error categorization (question misinterpretation → calculation error)，用 error-corrective trajectories 训练。LLaMA3-8B 上 13.3% accuracy improvement。**Proposal 未引用此工作**，但 LEMMA 做的 error categorization + targeted training 思路与本 proposal 类似（区别：LEMMA 用 LLM 做 error analysis，本 proposal 用 formal tools）。

**调研总结**: 这个领域正在快速发展，形成了几条平行的研究线：(a) LLM teacher-based skill profiling + targeted training (STAT, Self-Error-Instruct, LEMMA)；(b) pass-rate/outcome-based weakness targeting (SwS)；(c) symbolic verification for data quality/PRM training (FoVer, NSRSA, MATH-VF)；(d) symbolic problem generation (Adaptive Problem Generation, Reasoning Core)。本 proposal 试图桥接 (c) 和 (a)——用 formal tools 替代 LLM teacher 做 error profiling，这个具体交叉点确实尚未被占据，但周围的工作已经非常密集，留给本 proposal 的 novelty space 是"组合型"的而非"开创型"的。


【Trivial Alternative 检验】:

**存在多个成本更低的替代方案：**

1. **SwS-style pass-rate targeting（最大威胁）**：SwS 仅使用 pass-rate 分析就能识别 weakness 并合成 targeted problems，不需要任何 formal verification，在 8 个 benchmark 上取得了 7.7-10% 的提升。FormalLoop 的 formal error profiling 需要 Z3/SymPy formalization pipeline（成功率仅 60-70%），工程复杂度高得多。核心问题是：formal error profiling 提供的 granularity advantage 能否显著超过 pass-rate targeting？

2. **Outcome verification + category oversampling**：用 MATH 已有的 7 个 subcategory labels，对 weak subcategories 做 oversampling。完全不需要 formal verification。Proposal 承认了这个 alternative 并将其作为 baseline，这是好的。但如果 subcategory-level targeting 已经捕获了大部分收益，formal error profiling 的 within-subcategory granularity advantage 可能是边际的。

3. **FoVer-PRM + Best-of-N/RLVR**：利用 FoVer 已训练好的 PRM 做 verification，在标准 self-improvement loop 中使用。不需要自己构建 formalization pipeline。

**增量价值核心**在于：formal error *categorization*（不仅是 verification）+ *targeted synthesis*（不仅是 filtering）。如果 ablation 显示 error categorization → targeted synthesis 的链条中每一步都有显著增量，idea 成立；否则 trivial alternatives 就够了。这是一个需要实验验证的假设，不是逻辑上显然的。


【前提假设检验】:

**核心 claim 的逻辑链条中有 3 个关键假设未经验证：**

1. **Z3/SymPy 能可靠地将 step-level errors 分类到 5-type taxonomy**：Proposal 假设 formal verification 不仅能判定 step 对错，还能将错误归类为 algebraic manipulation / equation solving / arithmetic / constraint reasoning / logical inference。但 Z3/SymPy 的 verification 本质是检查 symbolic expression 的等价性，从 "verification failure" 到 "error type classification" 之间存在 gap。一个 step 可能同时涉及多种操作，formalization failure 也可能被误分类。这个假设是否成立直接决定 pipeline 的核心功能是否可行。

2. **Error-type-level targeting 显著优于 problem-level targeting**：知道"模型在 equation solving 上弱"比知道"模型做错了这道题"能产生多大的额外收益？这取决于 SymPy 合成的 targeted problems 是否真正练到了弱技能，而不仅仅是生成了更多同类题。数学技能之间的可迁移性（或不可迁移性）是一个未经验证的前提。

3. **Precision-coverage tradeoff 假说中 τ ≈ 15% 的适用性**：Imperfect verifier 论文的 15% threshold 是在 RLVR 设定下测得的（reward noise 对 policy optimization 的影响），而 FormalLoop 的设定是 error profiling → targeted synthesis（diagnosis noise 对 data selection 的影响）。这两个设定下 noise tolerance 是否相同是一个未经验证的类比。


【3 维度打分】:

1. **Novelty: 中** — 
   核心贡献是将 formal verification 从"verification/filtering tool"提升为"error diagnostician + targeted synthesis driver"，这个具体交叉点确实尚未被占据。NSRSA (arXiv 2603.21558) 最接近但仅做 arithmetic verification 不做 error categorization；STAT (ICLR 2026) 做 skill profiling 但依赖 LLM teacher；SwS (NeurIPS 2025) 做 weakness targeting 但用 pass-rate。FormalLoop 的 step-localized formal DPO 相比 Step-DPO (NeurIPS 2024) 和 NSRSA 的 solution-level DPO 也有实质区别。但这本质上是 **组合型 novelty**——formal verification (from FoVer/MATH-VF) + error profiling (from STAT/LEMMA) + targeted synthesis (from SwS/STAT) + step-localized DPO (from Step-DPO/NSRSA) 的交叉。每个组件都有近期先例。Error profile dynamics 是相对独特的分析贡献，但作为 paper 的核心卖点偏弱。

2. **Significance: 中** — 
   研究问题（teacher-free targeted self-improvement）确实重要且 timely，对应 solver-verifier gap theory (ICLR 2026) 指出的 verifier quality 瓶颈。但**核心发现的方向是可预测的**：ground-truth error diagnosis（formal tools）理应优于 noisy error diagnosis（LLM teacher）——如果结果是 positive，审稿人大概率会说 "I would have guessed this, formal verification gives cleaner signals"。真正 interesting 的是 by how much 以及 error profile dynamics 的 patterns，但这些属于 empirical findings 而非 idea-level surprise。此外，60-70% 的 formalization coverage 限制了方法的 generalizability——只有代数和算术类问题能享受 formal profiling，geometry 和 combinatorics 仍用 fallback。Imperfect verifier 论文 (arXiv 2604.07666) 的 15% tolerance 发现也削弱了 near-zero noise 的边际价值。

3. **Related Work: 强** — 
   这是本 proposal 最突出的优势。Related work 覆盖极为全面，包括直接竞争者 (STAT, SwS, Self-Error-Instruct, WarriorMath)、formal verification 线 (FoVer, MATH-VF, Safe)、理论基础 (solver-verifier gap)、concurrent work (Adaptive Problem Generation, NSRSA, Reasoning Core, Bidirectional Curriculum)、以及 imperfect verifier 研究。对每个 related work 的差异化定位清晰准确。唯一遗漏是 LEMMA (arXiv 2503.17439) 做 fine-grained error categorization + targeted training，思路与本 proposal 类似（LLM-based vs. formal-based）。但整体 related work 质量在 AAAI 投稿中属于上乘。


【概率估计】: [28% - 38%] 中位 33%

【估计理由】: 
Novelty 中等（组合型创新，具体交叉点确实空白但非范式转变）+ Significance 中等（问题重要但核心发现方向可预测、coverage 受限）+ Related Work 强（定位清晰，差异化到位）。Related work 的强覆盖保证了下限（不会因为 "missing important baselines" 被直接拒），但 Novelty 和 Significance 的中等评价限制了上限——审稿人可能认可这是 solid engineering integration work 但质疑 "what's the surprising insight?"。上界主要受 Significance 限制：如果核心结果 positive，审稿人可能评价为 "expected result, well-executed"，这在顶会中通常对应 borderline accept/reject。

【主要风险】: 
1. **"Expected result" 风险**：审稿人可能认为 "formal verification 提供更好的 error diagnosis → 更好的 targeted training" 是一个 obvious hypothesis，positive 结果不够 surprising，从而降低 novelty/significance 评分。
2. **Trivial alternative 威胁**：SwS 的 pass-rate targeting 或 subcategory-level oversampling 已经很强且简单得多。如果 FormalLoop 的 formal error profiling 仅带来边际提升（比如 1-2% accuracy gain），审稿人会质疑 engineering complexity 是否值得——这不是 idea 层面的问题，但会放大"组合型 novelty 不够"的 perception。
```

Sources:
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification (ACL 2026)](https://arxiv.org/abs/2505.15960)
- [STAT: Skill-Targeted Adaptive Training (ICLR 2026)](https://arxiv.org/abs/2510.10023)
- [NSRSA: Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment](https://arxiv.org/abs/2603.21558)
- [Solver-Verifier Gap Theory (ICLR 2026)](https://arxiv.org/abs/2507.00075)
- [An Imperfect Verifier is Good Enough: Learning with Noisy Rewards](https://arxiv.org/abs/2604.07666)
- [SwS: Self-aware Weakness-driven Problem Synthesis (NeurIPS 2025)](https://arxiv.org/abs/2506.08989)
- [Adaptive Problem Generation via Symbolic Representations](https://arxiv.org/abs/2602.19187)
- [LEMMA: Learning from Errors for Mathematical Advancement in LLMs](https://arxiv.org/abs/2503.17439)
- [MATH-VF: Step-Wise Formal Verification for LLM-Based Math Problem Solving](https://arxiv.org/abs/2505.20869)
- [Safe: Enhancing Mathematical Reasoning via Retrospective Step-aware Formal Verification (ACL 2025)](https://arxiv.org/abs/2506.04592)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "895f0418-7ff6-47bd-a973-cefe9366a534",
  "isSidechain": false,
  "requestId": "req_011CbSouaiv3nX6c3i76AFxy",
  "type": "assistant",
  "uuid": "d37e55f6-a7d6-4902-93b5-00daa3135153",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0187SLy4bEjQfjAX6cRXJvmK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1632,
      "cache_read_input_tokens": 26487,
      "output_tokens": 6798,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1632,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6798,
          "cache_read_input_tokens": 26487,
          "cache_creation_input_tokens": 1632,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1632
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

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Formal Error Profiling Enables Teacher-Free Targeted Math Self-Improvement  ## Core Problem  Self-improvement lo…",
  "leafUuid": "d37e55f6-a7d6-4902-93b5-00daa3135153",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal error profiling for teacher-free math self-improvement",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Formal Error Profiling Enables Teacher-Free Targeted Math Self-Improvement  ## Core Problem  Self-improvement lo…",
  "leafUuid": "d37e55f6-a7d6-4902-93b5-00daa3135153",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Formal error profiling for teacher-free math self-improvement",
  "sessionId": "da86d49f-2149-4719-af01-f74fce2bddfa"
}
```

---
