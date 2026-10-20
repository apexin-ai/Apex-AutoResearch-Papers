# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-10 (UTC).** ## Original idea { "tit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 29
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b.jsonl`
- **Structured JSON:** [`6b1fe57541fdf2a5bc81.json`](../../sessions/6b/6b1fe57541fdf2a5bc81.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T18:09:07.462Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T18:09:07.462Z",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-10 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Symbolic Pre-Filtering for Compute-Efficient Best-of-N Verification: An Empirical Study of Complementary Error Detection\",\n  \"core_problem\": \"Best-of-N sampling with neural verifiers (ORM/PRM) is the dominant paradigm for test-time compute scaling in mathematical reasoning, but neural verifiers suffer from reward hacking, poor OOD calibration, and high per-candidate scoring cost. Symbolic checks (arithmetic re-execution via SymPy, constraint validation) offer perfect precision on detected errors but unknown recall. The open question: can cheap symbolic pre-filtering meaningfully complement neural verifiers in best-of-N selection, and if so, what is the empirical error-type coverage of each verification modality?\",\n  \"opportunity\": \"Neural verifiers and symbolic checks likely detect different error distributions—neural verifiers catch 'plausible but wrong' reasoning via learned patterns, while symbolic checks catch 'mechanically incorrect' computation with zero false positives. No prior work empirically characterizes this complementarity for best-of-N selection with modern reasoning models. FANS (EMNLP 2025) uses expensive Lean4 uniformly; VERGE (Jan 2026) uses SMT for iterative refinement, not candidate filtering; FlexiVe (May 2025) adapts verification budget but uses only neural verifiers; Orlanski et al. (2025) apply syntactic pruning for code, not semantic symbolic verification for math. The gap: no systematic study of whether cheap symbolic verification provides useful complementary signal to neural verifiers in best-of-N pipelines, and no quantification of the error-type separation between modalities.\",\n  \"landscape\": \"Best-of-N with ORM/PRM (Rewarding Progress, ICLR 2025) scales to ~64 samples with diminishing returns, partially due to reward hacking (InferenceTimePessimism, 2025). Compute-optimal allocation research shows solutions should scale faster than verifications (S∝C^0.57, V∝C^0.39). FANS (EMNLP 2025) applies Lean4 for formal answer selection in best-of-N—high precision but ~2% gain with expensive per-candidate formalization. Safe (ACL 2025) performs step-aware Lean4 verification—closest to our verification pipeline but uniformly expensive. VERGE (Jan 2026) routes claims to SMT solvers vs LLM ensembles via semantic routing for iterative refinement—conceptually related but targets single-answer refinement, not candidate pool filtering. FlexiVe/Solve-Detect-Verify (May 2025) adaptively allocates verification budget between fast/slow neural thinking—no symbolic component. MATH-VF (May 2025) uses SymPy+Z3 uniformly per chain for step-wise verification but applies both tools to every candidate equally. HERMES (Nov 2025) verifies inline during generation with Lean4—fundamentally different (early termination vs post-hoc selection). Scalable Code Verification (Orlanski et al., 2025) uses syntax/lint pruning before ORM scoring for code—shallow checks without semantic verification. Self-Certainty (NeurIPS 2025) uses model confidence for selection without external verification. VeriCoT (ICLR 2026) formalizes CoT into FOL for validation but does not study complementarity with neural verifiers. SymCode (EACL 2026) generates verifiable SymPy code for single candidates. ThinkPRM (2025) trains process reward models that think—strong but purely neural. NSRSA (Mar 2026) uses SymPy for training data quality, not test-time selection. The critical gap: while individual symbolic and neural verification methods exist, no work empirically studies their complementarity in a combined pipeline for best-of-N, quantifies error-type coverage separation, or establishes when symbolic pre-filtering provides meaningful gain over pure neural selection.\",\n  \"approach\": \"We propose SymFilter, a two-stage verification pipeline that combines cheap symbolic pre-filtering with neural verifier scoring for best-of-N mathematical reasoning. The study has three components: (1) Error Taxonomy Study: Given N=64 candidate solutions from DeepSeek-R1-Distill-Qwen-7B on MATH-500 and AIME 2024, we manually annotate a stratified sample of 500 incorrect chains with fine-grained error types (arithmetic slip, algebraic manipulation error, logical non-sequitur, conceptual misunderstanding, constraint violation, answer format error). This establishes the empirical ceiling for each verification modality. (2) SymFilter Pipeline: Level 0 applies sub-millisecond heuristic checks (answer format validation, numerical bound checks, dimensional consistency); Level 1 extracts and re-executes arithmetic/algebraic sub-expressions via SymPy (adapting extraction patterns from SymCode and MATH-VF). Candidates flagged as definitively incorrect are eliminated; uncertain candidates pass through. The key design principle: symbolic filtering only REJECTS (never selects)—it eliminates candidates with verified computational errors, then a neural verifier ranks survivors. (3) Combined Pipeline Evaluation: We compare (a) ORM/PRM alone (best-of-N), (b) SymFilter alone (eliminate + majority vote on survivors), (c) SymFilter → ORM/PRM on survivors, (d) SymFilter → ThinkPRM/generative verifier on survivors. We measure accuracy, compute cost, and error-type-specific recall. We test N∈{8, 16, 32, 64} on MATH-500 and AIME 2024, with a focused N=64 comparison on DeepSeek-R1-Distill-Qwen-32B to assess how model strength affects the complementarity. Key hypotheses (explicitly framed as testable, not assumed): H1: SymFilter catches 20-50% of incorrect chains from the 7B model (lower bound based on error type priors for distilled models); H2: The errors caught by SymFilter have <30% overlap with the candidates that ORM already scores lowest (complementarity); H3: SymFilter+ORM at N=64 matches or exceeds ORM-alone at N=64 while reducing neural scoring cost by 20-40% (survivors only). We also report negative results if H1-H3 fail, as characterizing the limitations is itself a contribution.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~120h H100 (candidate generation: 7B model N=64 on MATH-500+AIME2024 ~30h; 32B model comparison ~25h; neural verifier scoring ~30h; baselines and ablations ~35h)\",\n      \"gpu_utilization\": \"Low-moderate (~25-35%). Human implements SymPy extraction pipeline, annotation interface, analysis scripts. GPU active during generation and scoring phases.\",\n      \"timeline\": \"6-8 weeks (Week 1-2: pilot study + error annotation + SymPy extraction pipeline; Week 3-4: full generation runs + SymFilter implementation; Week 5-6: combined pipeline experiments + ablations; Week 7-8: analysis and writing)\",\n      \"team\": \"1 researcher with Python/SymPy experience (no Lean4 expertise needed)\",\n      \"estimated_gpu_cost\": \"$250-350 (at ~$2.50/hr H100 on cloud providers)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~160h H100 (agent runs more configuration sweeps, threshold sensitivity analysis, additional model comparisons)\",\n      \"gpu_utilization\": \"Moderate (~45-55%). Agent implements pipeline and queues experiments; human reviews error annotations and validates SymPy extraction quality.\",\n      \"timeline\": \"3-5 weeks\",\n      \"team\": \"1 researcher, ~30min/day reviewing extraction patterns and annotation samples\",\n      \"claude_api_cost\": \"$80-150 (estimated 800-1200 turns for implementation, experiment orchestration, and analysis)\",\n      \"estimated_gpu_cost\": \"$350-450\",\n      \"risk_note\": \"SymPy expression extraction from natural language CoT requires pattern engineering; agent may need human guidance on edge cases in mathematical notation parsing.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~200h H100 (comprehensive N-sweeps, per-level ablations, threshold sensitivity, multiple model sizes, error type analysis across difficulty levels)\",\n      \"gpu_utilization\": \"High (~80-90%). Agent runs 24/7, queuing generation batches and scoring runs with minimal idle time.\",\n      \"timeline\": \"1-2 weeks with 2-4 H100 GPUs available\",\n      \"team\": \"0 researchers (initial setup ~1 hour for API keys and dataset download)\",\n      \"claude_api_cost\": \"$150-300 (estimated 1500-2500 turns for full pipeline, ablations, and paper drafting)\",\n      \"estimated_gpu_cost\": \"$500-600\",\n      \"speed_bottleneck\": \"Generation throughput for 7B model at N=64 across 500+ problems; neural verifier scoring on surviving candidates.\",\n      \"risk_note\": \"Automated error annotation may be less reliable than human annotation for the taxonomy study; agent should use LLM-as-judge with human-validated calibration set rather than fully automated annotation.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR deadline May 25, 2026 — feasible with pre-existing infrastructure for the 2-level system)\",\n    \"AAAI 2027 (expected abstract Jul 25, paper Aug 1, 2026 — comfortable timeline for full study)\",\n    \"NeurIPS 2026 workshops (e.g., MATH-AI workshop — good venue for empirical study)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"FANS: Formal Answer Selection for LLM Natural Language Math Reasoning Using Lean4 (EMNLP 2025)\",\n    \"Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification (ACL 2025)\",\n    \"VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (arXiv Jan 2026)\",\n    \"Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier (arXiv May 2025)\",\n    \"Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning (ICLR 2025)\",\n    \"When To Solve, When To Verify: Compute-Optimal Problem Solving and Generative Verification (arXiv Apr 2025)\",\n    \"Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving [MATH-VF] (arXiv 2025)\",\n    \"Reward Models Enable Scalable Code Verification by Trading Accuracy for Throughput (arXiv 2025)\",\n    \"Process Reward Models That Think [ThinkPRM] (arXiv 2025)\",\n    \"HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs (arXiv Nov 2025)\",\n    \"VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks (ICLR 2026)\",\n    \"SymCode: A Neurosymbolic Approach to Mathematical Reasoning via Verifiable Code Generation (EACL 2026)\",\n    \"Scalable Best-of-N Selection for Large Language Models via Self-Certainty (NeurIPS 2025)\",\n    \"Mathematical Reasoning in LLMs: Assessing Logical and Arithmetic Errors across Wide Numerical Ranges (arXiv Feb 2025)\",\n    \"Inference-Time Reward Hacking in Large Language Models (2025)\",\n    \"Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment (arXiv 2026)\"\n  ],\n  \"description\": \"We present SymFilter, a two-stage verification pipeline that empirically studies whether cheap symbolic pre-filtering (heuristic checks + SymPy arithmetic re-execution) provides complementary error detection to neural verifiers (ORM/PRM) in best-of-N mathematical reasoning. Unlike FANS/Safe (expensive Lean4 per candidate), VERGE (SMT for iterative refinement), or FlexiVe (adaptive neural-only verification), SymFilter investigates a fundamental empirical question: do symbolic and neural verification modalities catch different error types, and can their combination improve selection accuracy while reducing compute? We conduct a systematic error taxonomy study on 500 annotated incorrect reasoning chains from DeepSeek-R1-Distill-Qwen-7B, measure the detection rate of each verification level by error type, quantify the complementarity (overlap) between symbolic rejection and neural ranking, and evaluate the combined pipeline across N∈{8,16,32,64} on MATH-500 and AIME 2024. The study contributes: (1) the first fine-grained error type distribution for modern reasoning model outputs, (2) empirical bounds on symbolic verification utility as model capability increases, and (3) a practical recipe for when symbolic pre-filtering helps (or doesn't). We explicitly frame testable hypotheses and commit to reporting negative results. Targeting EMNLP 2026 or AAAI 2027.\",\n  \"project_name\": \"sym_filter_verify\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 2)\nIssues: [\"CRITICAL: The proposal claims to 'adapt extraction patterns from SymCode and MATH-VF' (Level 1), but this is based on a fundamental misunderstanding. SymCode generates Python/SymPy code directly instead of natural language CoT—it has NO extraction patterns. MATH-VF uses a full LLM-based Formalizer with a custom formal language (SimpleMath) and achieves only ~90% formalization accuracy—this is not pattern matching but an additional LLM inference call per step, which undermines the 'cheap pre-filtering' premise. The extraction mechanism needs to be completely rethought.\", \"CRITICAL: Error type analysis from recent literature (arXiv 2502.19361) shows calculation errors comprise only ~15.4% of errors in math reasoning, behind reasoning errors (25.3%) and understanding errors (15.7%). Furthermore, the same study finds that neural verifiers 'exhibit strong performance on calculation errors but struggle with strategy errors.' This means: (a) SymFilter's realistic catch rate is likely 5-12%, not the hypothesized 20-50%; (b) the errors SymFilter catches overlap heavily with errors neural verifiers already detect well, predicting HIGH overlap rather than the hypothesized <30% (H2 is likely wrong).\", \"CRITICAL: Missing highly relevant competing work—T3RL (arXiv 2603.02203, March 2026) compiles reasoning traces into executable Python code, executes for validation, and weights verified rollouts during voting, achieving +31.6% on harder problems. This is conceptually very close to SymFilter's core mechanism (code execution as verification signal in test-time scaling) and must be cited and differentiated from.\", \"The 'first fine-grained error type distribution for modern reasoning model outputs' claim (contribution 1) is invalid. Multiple error taxonomy studies exist: Zhang & Graf (AIME-Con 2025) categorized errors into Conditionally Correct, Procedural, Conceptual, and Impasse errors; Sun et al. (EMNLP 2025 Findings) created a 39-category framework from 300K+ error samples across 15 LLMs; ErrorAtlas provides a 17-category model-agnostic taxonomy. At best, this could be 'error type distribution specific to distilled reasoning models in best-of-N contexts.'\", \"Additional missing related work: (1) FoVer (ACL 2026 Findings)—uses Z3/Isabelle to generate PRM training data with step-level labels; (2) 'Controllable and Verifiable Process Data Synthesis for PRMs' (arXiv May 2026)—uses symbolic recomputation similar to SymFilter, likely concurrent; (3) BoN-MAV (Feb 2025)—multi-agent verification combining heterogeneous verifiers for best-of-N; (4) 'When Does Verification Pay Off?' (Nov 2025)—systematic study showing verification benefits are highest when solver and verifier distributions differ; (5) PAL (ICML 2023) and ToRA (ICLR 2024) as foundational code-execution-for-math works.\", \"Sun et al. (EMNLP 2025 Findings) found that 'as model sophistication increases, errors shift from computational mistakes to reasoning failures.' This directly threatens SymFilter's utility: the 7B distilled model may show moderate arithmetic error rates, but scaling to the 32B model (where you plan a focused comparison) will likely show even fewer catchable errors, weakening the cross-model generalization story.\", \"The 15-day timeline (May 10 to May 25) remains very tight even for the reduced scope. The extraction pipeline alone—whether regex-based (unreliable) or LLM-based (expensive, adding inference cost)—requires significant engineering and validation. Combined with generation runs at N=64 for 500+ problems, neural verifier baselines, error annotation of 500 chains, ablations across N∈{8,16,32,64}, and paper writing, this is a 4-6 week project compressed into 2 weeks.\"]\nFeedback: The revised proposal is much improved in scope and honesty, but three fundamental issues remain:\n\n1. **Resolve the extraction mechanism**: You have four options: (a) Use an LLM Formalizer like MATH-VF—but acknowledge this adds ~$50-100 in API costs per experiment and undermines the 'cheap' framing; (b) Use regex/heuristic extraction targeting only explicit arithmetic lines (e.g., '3 × 4 = 13')—but accept very low recall (~5-10% of errors) and reframe hypotheses accordingly; (c) Adopt SymCode's approach and generate code solutions directly, then compare code-execution-verified best-of-N vs. ORM-only best-of-N—this changes the research question but is more tractable; (d) Focus on answer-level verification only (check if the final numerical answer satisfies basic constraints, dimensional analysis, etc.) rather than step-level extraction.\n\n2. **Recalibrate hypotheses to match evidence**: H1 should be 5-15% (not 20-50%) given the 15.4% calculation error rate and imperfect extraction. H2 should acknowledge that high overlap is the more likely outcome. H3 should target modest gains (2-5% accuracy improvement at best). The paper should be positioned as 'empirically quantifying the (possibly small) utility of deterministic symbolic checks in best-of-N pipelines' rather than claiming large complementarity gains.\n\n3. **Differentiate from T3RL and MATH-VF**: T3RL (March 2026) already uses code execution as verification for test-time reasoning. MATH-VF already does step-wise symbolic verification on MATH-500. Your key differentiation should be the complementarity analysis and the cost-accuracy tradeoff study—not the mechanism itself. Frame the contribution as: 'We are the first to systematically measure how much cheap deterministic checks overlap with or complement learned neural verifiers in best-of-N, and establish when the additional symbolic stage is cost-justified.'\n\n4. **For the 15-day timeline**: Target option (b) or (d) above for extraction, which are implementable in days. Use only the 7B model (drop the 32B comparison). Use only MATH-500 + AIME 2024 (drop other benchmarks). Use only one neural verifier baseline (e.g., majority vote + one ORM). This minimal version could be a solid workshop paper (NeurIPS MATH-AI 2026) and could be expanded for AAAI 2027.\n\n5. **Drop the error taxonomy contribution claim**: This is not novel given existing work. Instead, contribute (a) the complementarity measurement and (b) the cost-accuracy Pareto analysis.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\")."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T18:09:07.467Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T18:09:07.467Z",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b"
}
```

---

## Round 1

27 recorded events

### User

_source line 3 · 2026-05-10T18:09:07.504Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-10 (UTC).**

## Original idea
{
  "title": "Symbolic Pre-Filtering for Compute-Efficient Best-of-N Verification: An Empirical Study of Complementary Error Detection",
  "core_problem": "Best-of-N sampling with neural verifiers (ORM/PRM) is the dominant paradigm for test-time compute scaling in mathematical reasoning, but neural verifiers suffer from reward hacking, poor OOD calibration, and high per-candidate scoring cost. Symbolic checks (arithmetic re-execution via SymPy, constraint validation) offer perfect precision on detected errors but unknown recall. The open question: can cheap symbolic pre-filtering meaningfully complement neural verifiers in best-of-N selection, and if so, what is the empirical error-type coverage of each verification modality?",
  "opportunity": "Neural verifiers and symbolic checks likely detect different error distributions—neural verifiers catch 'plausible but wrong' reasoning via learned patterns, while symbolic checks catch 'mechanically incorrect' computation with zero false positives. No prior work empirically characterizes this complementarity for best-of-N selection with modern reasoning models. FANS (EMNLP 2025) uses expensive Lean4 uniformly; VERGE (Jan 2026) uses SMT for iterative refinement, not candidate filtering; FlexiVe (May 2025) adapts verification budget but uses only neural verifiers; Orlanski et al. (2025) apply syntactic pruning for code, not semantic symbolic verification for math. The gap: no systematic study of whether cheap symbolic verification provides useful complementary signal to neural verifiers in best-of-N pipelines, and no quantification of the error-type separation between modalities.",
  "landscape": "Best-of-N with ORM/PRM (Rewarding Progress, ICLR 2025) scales to ~64 samples with diminishing returns, partially due to reward hacking (InferenceTimePessimism, 2025). Compute-optimal allocation research shows solutions should scale faster than verifications (S∝C^0.57, V∝C^0.39). FANS (EMNLP 2025) applies Lean4 for formal answer selection in best-of-N—high precision but ~2% gain with expensive per-candidate formalization. Safe (ACL 2025) performs step-aware Lean4 verification—closest to our verification pipeline but uniformly expensive. VERGE (Jan 2026) routes claims to SMT solvers vs LLM ensembles via semantic routing for iterative refinement—conceptually related but targets single-answer refinement, not candidate pool filtering. FlexiVe/Solve-Detect-Verify (May 2025) adaptively allocates verification budget between fast/slow neural thinking—no symbolic component. MATH-VF (May 2025) uses SymPy+Z3 uniformly per chain for step-wise verification but applies both tools to every candidate equally. HERMES (Nov 2025) verifies inline during generation with Lean4—fundamentally different (early termination vs post-hoc selection). Scalable Code Verification (Orlanski et al., 2025) uses syntax/lint pruning before ORM scoring for code—shallow checks without semantic verification. Self-Certainty (NeurIPS 2025) uses model confidence for selection without external verification. VeriCoT (ICLR 2026) formalizes CoT into FOL for validation but does not study complementarity with neural verifiers. SymCode (EACL 2026) generates verifiable SymPy code for single candidates. ThinkPRM (2025) trains process reward models that think—strong but purely neural. NSRSA (Mar 2026) uses SymPy for training data quality, not test-time selection. The critical gap: while individual symbolic and neural verification methods exist, no work empirically studies their complementarity in a combined pipeline for best-of-N, quantifies error-type coverage separation, or establishes when symbolic pre-filtering provides meaningful gain over pure neural selection.",
  "approach": "We propose SymFilter, a two-stage verification pipeline that combines cheap symbolic pre-filtering with neural verifier scoring for best-of-N mathematical reasoning. The study has three components: (1) Error Taxonomy Study: Given N=64 candidate solutions from DeepSeek-R1-Distill-Qwen-7B on MATH-500 and AIME 2024, we manually annotate a stratified sample of 500 incorrect chains with fine-grained error types (arithmetic slip, algebraic manipulation error, logical non-sequitur, conceptual misunderstanding, constraint violation, answer format error). This establishes the empirical ceiling for each verification modality. (2) SymFilter Pipeline: Level 0 applies sub-millisecond heuristic checks (answer format validation, numerical bound checks, dimensional consistency); Level 1 extracts and re-executes arithmetic/algebraic sub-expressions via SymPy (adapting extraction patterns from SymCode and MATH-VF). Candidates flagged as definitively incorrect are eliminated; uncertain candidates pass through. The key design principle: symbolic filtering only REJECTS (never selects)—it eliminates candidates with verified computational errors, then a neural verifier ranks survivors. (3) Combined Pipeline Evaluation: We compare (a) ORM/PRM alone (best-of-N), (b) SymFilter alone (eliminate + majority vote on survivors), (c) SymFilter → ORM/PRM on survivors, (d) SymFilter → ThinkPRM/generative verifier on survivors. We measure accuracy, compute cost, and error-type-specific recall. We test N∈{8, 16, 32, 64} on MATH-500 and AIME 2024, with a focused N=64 comparison on DeepSeek-R1-Distill-Qwen-32B to assess how model strength affects the complementarity. Key hypotheses (explicitly framed as testable, not assumed): H1: SymFilter catches 20-50% of incorrect chains from the 7B model (lower bound based on error type priors for distilled models); H2: The errors caught by SymFilter have <30% overlap with the candidates that ORM already scores lowest (complementarity); H3: SymFilter+ORM at N=64 matches or exceeds ORM-alone at N=64 while reducing neural scoring cost by 20-40% (survivors only). We also report negative results if H1-H3 fail, as characterizing the limitations is itself a contribution.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~120h H100 (candidate generation: 7B model N=64 on MATH-500+AIME2024 ~30h; 32B model comparison ~25h; neural verifier scoring ~30h; baselines and ablations ~35h)",
      "gpu_utilization": "Low-moderate (~25-35%). Human implements SymPy extraction pipeline, annotation interface, analysis scripts. GPU active during generation and scoring phases.",
      "timeline": "6-8 weeks (Week 1-2: pilot study + error annotation + SymPy extraction pipeline; Week 3-4: full generation runs + SymFilter implementation; Week 5-6: combined pipeline experiments + ablations; Week 7-8: analysis and writing)",
      "team": "1 researcher with Python/SymPy experience (no Lean4 expertise needed)",
      "estimated_gpu_cost": "$250-350 (at ~$2.50/hr H100 on cloud providers)"
    },
    "human_in_loop": {
      "gpu_hours": "~160h H100 (agent runs more configuration sweeps, threshold sensitivity analysis, additional model comparisons)",
      "gpu_utilization": "Moderate (~45-55%). Agent implements pipeline and queues experiments; human reviews error annotations and validates SymPy extraction quality.",
      "timeline": "3-5 weeks",
      "team": "1 researcher, ~30min/day reviewing extraction patterns and annotation samples",
      "claude_api_cost": "$80-150 (estimated 800-1200 turns for implementation, experiment orchestration, and analysis)",
      "estimated_gpu_cost": "$350-450",
      "risk_note": "SymPy expression extraction from natural language CoT requires pattern engineering; agent may need human guidance on edge cases in mathematical notation parsing."
    },
    "auto_research": {
      "gpu_hours": "~200h H100 (comprehensive N-sweeps, per-level ablations, threshold sensitivity, multiple model sizes, error type analysis across difficulty levels)",
      "gpu_utilization": "High (~80-90%). Agent runs 24/7, queuing generation batches and scoring runs with minimal idle time.",
      "timeline": "1-2 weeks with 2-4 H100 GPUs available",
      "team": "0 researchers (initial setup ~1 hour for API keys and dataset download)",
      "claude_api_cost": "$150-300 (estimated 1500-2500 turns for full pipeline, ablations, and paper drafting)",
      "estimated_gpu_cost": "$500-600",
      "speed_bottleneck": "Generation throughput for 7B model at N=64 across 500+ problems; neural verifier scoring on surviving candidates.",
      "risk_note": "Automated error annotation may be less reliable than human annotation for the taxonomy study; agent should use LLM-as-judge with human-validated calibration set rather than fully automated annotation."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR deadline May 25, 2026 — feasible with pre-existing infrastructure for the 2-level system)",
    "AAAI 2027 (expected abstract Jul 25, paper Aug 1, 2026 — comfortable timeline for full study)",
    "NeurIPS 2026 workshops (e.g., MATH-AI workshop — good venue for empirical study)"
  ],
  "level": "solid",
  "key_references": [
    "FANS: Formal Answer Selection for LLM Natural Language Math Reasoning Using Lean4 (EMNLP 2025)",
    "Safe: Enhancing Mathematical Reasoning in Large Language Models via Retrospective Step-aware Formal Verification (ACL 2025)",
    "VERGE: Formal Refinement and Guidance Engine for Verifiable LLM Reasoning (arXiv Jan 2026)",
    "Solve-Detect-Verify: Inference-Time Scaling with Flexible Generative Verifier (arXiv May 2025)",
    "Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning (ICLR 2025)",
    "When To Solve, When To Verify: Compute-Optimal Problem Solving and Generative Verification (arXiv Apr 2025)",
    "Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving [MATH-VF] (arXiv 2025)",
    "Reward Models Enable Scalable Code Verification by Trading Accuracy for Throughput (arXiv 2025)",
    "Process Reward Models That Think [ThinkPRM] (arXiv 2025)",
    "HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs (arXiv Nov 2025)",
    "VeriCoT: Neuro-symbolic Chain-of-Thought Validation via Logical Consistency Checks (ICLR 2026)",
    "SymCode: A Neurosymbolic Approach to Mathematical Reasoning via Verifiable Code Generation (EACL 2026)",
    "Scalable Best-of-N Selection for Large Language Models via Self-Certainty (NeurIPS 2025)",
    "Mathematical Reasoning in LLMs: Assessing Logical and Arithmetic Errors across Wide Numerical Ranges (arXiv Feb 2025)",
    "Inference-Time Reward Hacking in Large Language Models (2025)",
    "Stabilizing Iterative Self-Training with Verified Reasoning via Symbolic Recursive Self-Alignment (arXiv 2026)"
  ],
  "description": "We present SymFilter, a two-stage verification pipeline that empirically studies whether cheap symbolic pre-filtering (heuristic checks + SymPy arithmetic re-execution) provides complementary error detection to neural verifiers (ORM/PRM) in best-of-N mathematical reasoning. Unlike FANS/Safe (expensive Lean4 per candidate), VERGE (SMT for iterative refinement), or FlexiVe (adaptive neural-only verification), SymFilter investigates a fundamental empirical question: do symbolic and neural verification modalities catch different error types, and can their combination improve selection accuracy while reducing compute? We conduct a systematic error taxonomy study on 500 annotated incorrect reasoning chains from DeepSeek-R1-Distill-Qwen-7B, measure the detection rate of each verification level by error type, quantify the complementarity (overlap) between symbolic rejection and neural ranking, and evaluate the combined pipeline across N∈{8,16,32,64} on MATH-500 and AIME 2024. The study contributes: (1) the first fine-grained error type distribution for modern reasoning model outputs, (2) empirical bounds on symbolic verification utility as model capability increases, and (3) a practical recipe for when symbolic pre-filtering helps (or doesn't). We explicitly frame testable hypotheses and commit to reporting negative results. Targeting EMNLP 2026 or AAAI 2027.",
  "project_name": "sym_filter_verify",
  "source": "web_research"
}

## Reviewer feedback (round 2)
Issues: ["CRITICAL: The proposal claims to 'adapt extraction patterns from SymCode and MATH-VF' (Level 1), but this is based on a fundamental misunderstanding. SymCode generates Python/SymPy code directly instead of natural language CoT—it has NO extraction patterns. MATH-VF uses a full LLM-based Formalizer with a custom formal language (SimpleMath) and achieves only ~90% formalization accuracy—this is not pattern matching but an additional LLM inference call per step, which undermines the 'cheap pre-filtering' premise. The extraction mechanism needs to be completely rethought.", "CRITICAL: Error type analysis from recent literature (arXiv 2502.19361) shows calculation errors comprise only ~15.4% of errors in math reasoning, behind reasoning errors (25.3%) and understanding errors (15.7%). Furthermore, the same study finds that neural verifiers 'exhibit strong performance on calculation errors but struggle with strategy errors.' This means: (a) SymFilter's realistic catch rate is likely 5-12%, not the hypothesized 20-50%; (b) the errors SymFilter catches overlap heavily with errors neural verifiers already detect well, predicting HIGH overlap rather than the hypothesized <30% (H2 is likely wrong).", "CRITICAL: Missing highly relevant competing work—T3RL (arXiv 2603.02203, March 2026) compiles reasoning traces into executable Python code, executes for validation, and weights verified rollouts during voting, achieving +31.6% on harder problems. This is conceptually very close to SymFilter's core mechanism (code execution as verification signal in test-time scaling) and must be cited and differentiated from.", "The 'first fine-grained error type distribution for modern reasoning model outputs' claim (contribution 1) is invalid. Multiple error taxonomy studies exist: Zhang & Graf (AIME-Con 2025) categorized errors into Conditionally Correct, Procedural, Conceptual, and Impasse errors; Sun et al. (EMNLP 2025 Findings) created a 39-category framework from 300K+ error samples across 15 LLMs; ErrorAtlas provides a 17-category model-agnostic taxonomy. At best, this could be 'error type distribution specific to distilled reasoning models in best-of-N contexts.'", "Additional missing related work: (1) FoVer (ACL 2026 Findings)—uses Z3/Isabelle to generate PRM training data with step-level labels; (2) 'Controllable and Verifiable Process Data Synthesis for PRMs' (arXiv May 2026)—uses symbolic recomputation similar to SymFilter, likely concurrent; (3) BoN-MAV (Feb 2025)—multi-agent verification combining heterogeneous verifiers for best-of-N; (4) 'When Does Verification Pay Off?' (Nov 2025)—systematic study showing verification benefits are highest when solver and verifier distributions differ; (5) PAL (ICML 2023) and ToRA (ICLR 2024) as foundational code-execution-for-math works.", "Sun et al. (EMNLP 2025 Findings) found that 'as model sophistication increases, errors shift from computational mistakes to reasoning failures.' This directly threatens SymFilter's utility: the 7B distilled model may show moderate arithmetic error rates, but scaling to the 32B model (where you plan a focused comparison) will likely show even fewer catchable errors, weakening the cross-model generalization story.", "The 15-day timeline (May 10 to May 25) remains very tight even for the reduced scope. The extraction pipeline alone—whether regex-based (unreliable) or LLM-based (expensive, adding inference cost)—requires significant engineering and validation. Combined with generation runs at N=64 for 500+ problems, neural verifier baselines, error annotation of 500 chains, ablations across N∈{8,16,32,64}, and paper writing, this is a 4-6 week project compressed into 2 weeks."]
Feedback: The revised proposal is much improved in scope and honesty, but three fundamental issues remain:

1. **Resolve the extraction mechanism**: You have four options: (a) Use an LLM Formalizer like MATH-VF—but acknowledge this adds ~$50-100 in API costs per experiment and undermines the 'cheap' framing; (b) Use regex/heuristic extraction targeting only explicit arithmetic lines (e.g., '3 × 4 = 13')—but accept very low recall (~5-10% of errors) and reframe hypotheses accordingly; (c) Adopt SymCode's approach and generate code solutions directly, then compare code-execution-verified best-of-N vs. ORM-only best-of-N—this changes the research question but is more tractable; (d) Focus on answer-level verification only (check if the final numerical answer satisfies basic constraints, dimensional analysis, etc.) rather than step-level extraction.

2. **Recalibrate hypotheses to match evidence**: H1 should be 5-15% (not 20-50%) given the 15.4% calculation error rate and imperfect extraction. H2 should acknowledge that high overlap is the more likely outcome. H3 should target modest gains (2-5% accuracy improvement at best). The paper should be positioned as 'empirically quantifying the (possibly small) utility of deterministic symbolic checks in best-of-N pipelines' rather than claiming large complementarity gains.

3. **Differentiate from T3RL and MATH-VF**: T3RL (March 2026) already uses code execution as verification for test-time reasoning. MATH-VF already does step-wise symbolic verification on MATH-500. Your key differentiation should be the complementarity analysis and the cost-accuracy tradeoff study—not the mechanism itself. Frame the contribution as: 'We are the first to systematically measure how much cheap deterministic checks overlap with or complement learned neural verifiers in best-of-N, and establish when the additional symbolic stage is cost-justified.'

4. **For the 15-day timeline**: Target option (b) or (d) above for extraction, which are implementable in days. Use only the 7B model (drop the 32B comparison). Use only MATH-500 + AIME 2024 (drop other benchmarks). Use only one neural verifier baseline (e.g., majority vote + one ORM). This minimal version could be a solid workshop paper (NeurIPS MATH-AI 2026) and could be expanded for AAAI 2027.

5. **Drop the error taxonomy contribution claim**: This is not novel given existing work. Instead, contribute (a) the complementarity measurement and (b) the cost-accuracy Pareto analysis.

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
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "type": "user",
  "uuid": "5a303e5d-7aaa-4d2f-b4d7-0d596c2d1fcc",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T18:09:07.502Z_

```json
{
  "parentUuid": "5a303e5d-7aaa-4d2f-b4d7-0d596c2d1fcc",
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
  "uuid": "07063519-3854-4d14-8617-97b64ed7e694",
  "timestamp": "2026-05-10T18:09:07.502Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T18:09:07.502Z_

```json
{
  "parentUuid": "07063519-3854-4d14-8617-97b64ed7e694",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1c6a8562-c340-4dbd-a5cc-fc6bd51610fc",
  "timestamp": "2026-05-10T18:09:07.502Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Symbolic Pre-Filtering for Compute-Efficient Best-of-N Verification: A…",
  "leafUuid": "1c6a8562-c340-4dbd-a5cc-fc6bd51610fc",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Quantifying symbolic-neural verifier complementarity in best-of-N reasoning",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b"
}
```

---

### Assistant

_source line 8 · 2026-05-10T18:09:22.537Z_

<details><summary>Logged reasoning block</summary>

```text
Let me carefully analyze the reviewer feedback and plan my research before revising the idea.

The key issues are:
1. **Extraction mechanism** - SymCode has no extraction patterns, MATH-VF uses expensive LLM formalization
2. **Error type distribution** - calculation errors are only ~15.4%, neural verifiers already catch them well
3. **Missing work** - T3RL, FoVer, BoN-MAV, PAL, ToRA, etc.
4. **Error taxonomy claim is not novel**
5. **Model scaling weakens the case** - stronger models make fewer arithmetic errors


6. **Timeline is tight**

I need to dig into the research on each of these points to understand what's actually feasible to address.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1c6a8562-c340-4dbd-a5cc-fc6bd51610fc",
  "isSidechain": false,
  "requestId": "req_011CauLTLk49XqR7xvMyoH5y",
  "type": "assistant",
  "uuid": "76fd16bd-1bcb-4006-a3d7-cb58b2d197aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018eVzwHeqEGGVP46BXioDr6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11120,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1891,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11120,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1891,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 11120,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11120
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

_source line 9 · 2026-05-10T18:09:22.538Z_

I'll start by deeply researching each critical issue the reviewer raised. Let me search for the key papers and current state of the field in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76fd16bd-1bcb-4006-a3d7-cb58b2d197aa",
  "isSidechain": false,
  "requestId": "req_011CauLTLk49XqR7xvMyoH5y",
  "type": "assistant",
  "uuid": "66d85806-4b0f-40d6-8df0-269f538e0179",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018eVzwHeqEGGVP46BXioDr6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11120,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1891,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11120,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1891,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 11120,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11120
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

_source line 10 · 2026-05-10T18:09:31.546Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Wr8exWq564ra2gqCKL6p8e`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research T3RL and code-execution verification",
  "prompt": "I'm revising a research proposal about symbolic pre-filtering for best-of-N verification in mathematical reasoning. A reviewer pointed out I'm missing T3RL (arXiv 2603.02203, March 2026), which compiles reasoning traces into executable Python code for verification.\n\nPlease do the following:\n1. Use WebSearch to find T3RL (arXiv 2603.02203) and any related work on code-execution-based verification for test-time scaling\n2. Use WebFetch to read the T3RL paper abstract and method section from its arXiv page\n3. Search for \"code execution verification best-of-N mathematical reasoning 2025 2026\" to find other related works\n4. Search for \"PAL program-aided language models\" and \"ToRA tool-integrated reasoning\" to understand the foundational code-execution works\n\nFor each paper found, report:\n- Title, venue, date\n- Core method (2-3 sentences)\n- How it relates to using symbolic/code verification in best-of-N selection\n- Key results (accuracy numbers on MATH/AIME if available)\n\nBe thorough - I need to understand the full landscape of code-execution-based verification approaches."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66d85806-4b0f-40d6-8df0-269f538e0179",
  "isSidechain": false,
  "requestId": "req_011CauLTLk49XqR7xvMyoH5y",
  "type": "assistant",
  "uuid": "41ea2268-9dc0-4d45-bf9d-cf4e6f1f7003",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018eVzwHeqEGGVP46BXioDr6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11120,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1891,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11120,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1891,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 11120,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11120
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

_source line 11 · 2026-05-10T18:09:41.047Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01G4gtCmyi9Kr1VMxo5CzPE2`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research error taxonomy and calculation error rates",
  "prompt": "I'm revising a research proposal about symbolic verification for math reasoning. A reviewer cited arXiv 2502.19361 showing calculation errors are only ~15.4% of errors. I need to deeply understand error distributions in LLM mathematical reasoning.\n\nPlease do the following:\n1. Use WebSearch to find arXiv 2502.19361 (about mathematical reasoning errors, logical and arithmetic errors) and use WebFetch to read its abstract and key findings\n2. Search for \"Sun et al EMNLP 2025 error taxonomy LLM mathematical reasoning 39 category\" and fetch the paper\n3. Search for \"ErrorAtlas error taxonomy language model\" and fetch details\n4. Search for \"Zhang Graf AIME-Con 2025 error categorization\" \n5. Search for \"LLM mathematical reasoning error distribution calculation vs reasoning 2025 2026\"\n6. Search for \"model scaling error type shift computational reasoning failures\"\n\nFor each source, I need:\n- The actual error type percentages (especially: what % are calculation/arithmetic errors vs reasoning/strategy errors)\n- How error distributions change with model capability\n- Whether neural verifiers are already good at catching calculation errors\n- Any evidence about what types of errors are hardest to catch\n\nThis is critical for recalibrating my hypotheses about how much a symbolic checker can actually help."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "41ea2268-9dc0-4d45-bf9d-cf4e6f1f7003",
  "isSidechain": false,
  "requestId": "req_011CauLTLk49XqR7xvMyoH5y",
  "type": "assistant",
  "uuid": "6f9bff96-38e0-4fe4-baae-698d4fea7397",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018eVzwHeqEGGVP46BXioDr6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11120,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1891,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11120,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1891,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 11120,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11120
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

_source line 12 · 2026-05-10T18:09:50.037Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Cyw9CPwhjutGmTunjFwFr1`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research MATH-VF extraction and FoVer/BoN-MAV",
  "prompt": "I'm revising a research proposal about symbolic pre-filtering for best-of-N verification in math reasoning. I need to understand several key related works deeply.\n\nPlease do the following:\n\n1. **MATH-VF**: Search for \"MATH-VF step-wise formal verification LLM SymPy Z3 2025\" and use WebFetch to read the paper. I specifically need to understand:\n   - How does MATH-VF extract/formalize mathematical expressions from CoT? Is it LLM-based or pattern-based?\n   - What is their formalization accuracy?\n   - What is the computational cost of their approach?\n\n2. **FoVer**: Search for \"FoVer ACL 2026 Z3 Isabelle PRM training data\" and fetch the paper. I need:\n   - How they use formal verification to generate training labels\n   - Their approach to step-level verification\n\n3. **BoN-MAV**: Search for \"BoN-MAV multi-agent verification best-of-N 2025\" and fetch details. I need:\n   - How they combine heterogeneous verifiers\n   - Their results on combining different verification modalities\n\n4. **\"When Does Verification Pay Off?\"**: Search for \"when does verification pay off 2025 solver verifier distribution\" and fetch the paper. I need:\n   - Their findings on when verification helps\n   - The solver-verifier distribution difference claim\n\n5. **\"Controllable and Verifiable Process Data Synthesis for PRMs\"**: Search for \"controllable verifiable process data synthesis PRM symbolic recomputation 2026\" and fetch details.\n\n6. **SymCode**: Search for \"SymCode neurosymbolic verifiable code generation EACL 2026\" to confirm it generates code directly (no extraction patterns).\n\nReport detailed findings for each paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f9bff96-38e0-4fe4-baae-698d4fea7397",
  "isSidechain": false,
  "requestId": "req_011CauLTLk49XqR7xvMyoH5y",
  "type": "assistant",
  "uuid": "35646cf2-27d7-4e8f-af2d-8e824bd1fd9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018eVzwHeqEGGVP46BXioDr6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11120,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1891,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11120,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1891,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 11120,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11120
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

_source line 13 · 2026-05-10T18:09:58.835Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Y2VcCGWEqwb7y6Nuj7TPAd`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research extraction feasibility and answer-level verification",
  "prompt": "I'm revising a research proposal. A key challenge is: how to extract mathematical expressions from natural language chain-of-thought (CoT) for symbolic verification. The reviewer says my options are:\n(a) LLM-based formalization (expensive, undermines \"cheap\" premise)\n(b) Regex/heuristic extraction (low recall, ~5-10%)\n(c) Generate code solutions directly (changes research question)\n(d) Answer-level verification only (check final answer constraints)\n\nPlease research:\n\n1. Search for \"extract mathematical expressions chain of thought symbolic verification regex heuristic\" to find approaches to expression extraction\n2. Search for \"answer-level verification mathematical reasoning constraint checking final answer\" \n3. Search for \"numerical answer verification MATH benchmark consistency checking\"\n4. Search for \"code generation verification mathematical reasoning test-time compute 2025 2026\" to understand option (c)\n5. Search for \"Python code execution verification math reasoning best-of-N\"\n6. Search for existing tools/repos on GitHub: \"sympy verify math reasoning chain of thought\"\n\nI need to understand:\n- What's the realistic extraction accuracy for regex/heuristic approaches on CoT?\n- Has anyone done answer-level-only verification (e.g., plug final answer back into original constraints)?\n- What's the actual cost differential between LLM formalization vs direct code generation?\n- Are there any papers studying the cost-accuracy Pareto frontier of different verification approaches?\n\nReport findings with specific numbers where available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35646cf2-27d7-4e8f-af2d-8e824bd1fd9e",
  "isSidechain": false,
  "requestId": "req_011CauLTLk49XqR7xvMyoH5y",
  "type": "assistant",
  "uuid": "4db5ece4-b53f-42e4-84ed-8967764003fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018eVzwHeqEGGVP46BXioDr6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11120,
      "cache_read_input_tokens": 11804,
      "output_tokens": 1891,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11120,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1891,
          "cache_read_input_tokens": 11804,
          "cache_creation_input_tokens": 11120,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11120
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

_source line 14 · 2026-05-10T18:12:23.354Z_

<details><summary>↩ Tool result · `toolu_01Y2VcCGWEqwb7y6Nuj7TPAd`</summary>

```text
I now have comprehensive findings across all your research questions. Here is my report.

---

## Research Findings: Verification Approaches for Mathematical CoT Reasoning

### 1. Regex/Heuristic Extraction Accuracy (Option B)

**For final answers: reasonably high. For intermediate expressions: very low.**

The critical distinction is between extracting the *final answer* versus extracting *intermediate mathematical expressions* from CoT text.

**Final answer extraction** is a largely solved problem when models use standard formatting. HuggingFace's [Math-Verify](https://github.com/huggingface/Math-Verify) library uses a three-step pipeline (Regex Extraction -> SymPy Conversion -> Gold Comparison) with prioritized regex patterns (boxed mode for `\boxed{}`, explicit mode for "Answer:" markers, speculative mode as fallback). It achieves higher accuracy than prior evaluators on the MATH dataset -- models solved an average of 61 more problems (a 4.66-point accuracy increase) when Math-Verify replaced older evaluators. OpenCompass uses a similar [MATHVerifyEvaluator](https://doc.opencompass.org.cn/advanced_guides/math_verify.html).

However, these tools target **only the final boxed answer**, not intermediate reasoning steps. For intermediate expression extraction from free-form CoT, the picture is much worse:
- LLM outputs contain answers in "varied surface forms" (e.g., "alpha" vs "10^3") that are semantically equivalent but textually different.
- Regex-based tools "typically handle only LaTeX expressions or simple string patterns, and struggle with basic semantic equivalence."
- No published system reports recall figures for extracting intermediate mathematical expressions from CoT. Your reviewer's estimate of ~5-10% recall for intermediate steps appears reasonable -- this is essentially an unsolved problem for heuristic methods.

**Key takeaway**: Regex works well for final-answer extraction (the `\boxed{}` convention makes this tractable). It fails for extracting the full chain of intermediate symbolic expressions needed for step-level symbolic verification.

### 2. Answer-Level-Only Verification (Option D)

This is the best-studied and most practical approach, and multiple strong systems exist:

**Outcome Reward Models (ORMs)** check only the final answer. The landmark [Let's Verify Step by Step](https://cdn.openai.com/improving-mathematical-reasoning-with-process-supervision/Lets_Verify_Step_by_Step.pdf) (OpenAI, 2023) found that outcome supervision and process supervision led to "similar final performance" on grade-school math. ORMs are far cheaper to train: they require only final outcome labels, while Process Reward Models (PRMs) require correctness labels for every step (benchmarks average 7-13 steps per problem, so PRM annotation cost is 7-13x higher).

**Self-consistency / majority voting** is the dominant answer-level verification method. Multiple CoT samples are generated and the most common final answer is selected. [DeepConf](https://jiaweizzhao.github.io/deepconf/static/pdfs/deepconf_arxiv.pdf) (Meta AI, 2025) pushed this to **99.9% accuracy on AIME 2025** by:
- Filtering out low-confidence traces using token/group/tail confidence metrics
- Weighting votes by confidence scores
- Reducing total tokens by 43-84.7% compared to naive majority voting

**Constraint-based answer checking** (plugging the final answer back into the original problem constraints) is used in specific settings. The [IJCAI 2025 instantiation-based formalization](https://www.ijcai.org/proceedings/2025/0516.pdf) paper infers concrete instantiations (positive and negative test cases) for each constraint, then verifies satisfiability -- but uses an LLM for the instantiation step. For numerical MATH-style problems, the simpler approach of checking `answer == gold_answer` (with SymPy equivalence) is standard.

**Key takeaway**: Answer-level verification is cheap, well-understood, and with confidence-weighted voting achieves near-perfect accuracy on competition math. The limitation is it cannot detect *correct answers arrived at through flawed reasoning*.

### 3. Cost Differential: LLM Formalization vs. Direct Code Generation (Options A vs. C)

Several recent papers quantify this tradeoff:

**SymCode** ([arXiv 2510.25975](https://arxiv.org/abs/2510.25975), Jan 2026): A training-free framework that instructs the LLM to generate SymPy code directly rather than formalizing natural language CoT. Achieves **up to 13.6 percentage point accuracy improvement** over baselines on MATH-500 and OlympiadBench, and is "more token-efficient" than natural language CoT because it shifts failures from "opaque logical fallacies" to "transparent, programmatic errors."

**HERMES** ([arXiv 2511.18760](https://arxiv.org/abs/2511.18760), Nov 2025): Interleaves informal reasoning with formally verified Lean proof steps. Achieves **up to 67% accuracy improvement on AIME'25 while using 80% fewer total inference FLOPs** compared to reward-based approaches. This represents the LLM-formalization approach (option A) but with a clever architecture that reduces cost.

**MATH-VF** ([arXiv 2505.20869](https://arxiv.org/abs/2505.20869), May 2025): Step-wise formal verification using a custom SimpleMath language. Key finding: "less than 10% of correct informal solutions can pass Coq verification" -- full formalization is extremely hard. MATH-VF addresses this by allowing gaps and using a simpler language closer to natural mathematical text. It exploits sparsity (most conclusions depend on at most 4 premises) to reduce token cost.

**S*** ([arXiv 2502.14382](https://arxiv.org/abs/2502.14382)): Test-time scaling for code generation. Uses iterative debugging with interpreter execution. A **3B model with S* outperforms GPT-4o-mini**; GPT-4o-mini with S* outperforms o1-preview by 3.7%. The key advantage of code generation: "the availability of programmatic interpreters enables execution of programs to obtain precise outputs and error messages."

**AIMO-2 winning solution** ([arXiv 2504.16891](https://arxiv.org/abs/2504.16891)): Used Tool-Integrated Reasoning (TIR) -- the LLM generates code within its reasoning chain, executes it, and continues. 1.7M high-quality TIR solutions were generated, with SymPy and Python execution as the verification backbone. This is essentially option (C) deployed at scale and winning the competition.

**Cost comparison summary**:
| Approach | Relative Token Cost | Accuracy Gain | Verification Guarantee |
|----------|-------------------|---------------|----------------------|
| LLM formalization to Lean/Coq (A) | Very high (multiple LLM calls + prover) | Strong but <10% formalization success rate for Coq | Formal proof |
| MATH-VF SimpleMath (A, simplified) | High but reduced via sparsity | Moderate | Semi-formal |
| HERMES (A, hybrid) | 80% fewer FLOPs than reward methods | +67% on AIME'25 | Formal for verified steps |
| SymCode / direct code gen (C) | Lower than NL CoT | +13.6 pp on MATH-500 | Execution-based |
| Answer-level voting (D) | Low (just run N samples) | 99.9% on AIME'25 with DeepConf | Final answer only |

### 4. Pareto Frontier Studies

Yes, this has been explicitly studied:

**[Compute-Accuracy Pareto Frontiers for Open-Source Reasoning LLMs](https://arxiv.org/abs/2512.24776)** (Dec 2025): Maps FLOPs-accuracy Pareto frontiers across math benchmarks. Key findings:
- MoE models consistently lead the Pareto frontier (higher accuracy at comparable FLOP budgets)
- There is a **task-dependent Pareto knee** beyond which additional compute gives negligible accuracy gain
- Easier benchmarks plateau at lower compute; competition-level problems require significantly more
- A 1.5B model with parallel scaling achieves 83.6% on MATH-500, exceeding a 7B model's vanilla 82.0%

**[Scaling LLM Test-Time Compute Optimally](https://arxiv.org/html/2408.03314v1)** (ICLR 2025): Proposes compute-optimal inference with the REBASE method. An adaptive, prompt-dependent strategy improves test-time compute efficiency by **2-4x**.

**Joint reasoner-verifier training** ([arXiv 2505.04842](https://arxiv.org/html/2505.04842v2)): Training the LLM as both reasoner and generative verifier enables **8-32x more efficient test-time compute scaling** compared to base RL methods.

### Synthesis and Recommendation for Your Proposal

Given these findings, the reviewer's four options have a clear ordering:

1. **Option (D) -- answer-level verification -- is the strongest starting point.** It is cheap, well-studied, and achieves near-perfect accuracy with methods like DeepConf. You can frame this as "outcome-based verification" and cite the ORM literature showing it matches PRM performance for final accuracy.

2. **Option (C) -- code generation -- is the most promising for going beyond final answers.** SymCode and the AIMO-2 winning approach show that generating SymPy code is cheaper than LLM formalization, provides execution-based verification guarantees, and achieves large accuracy improvements. The research question shifts, but the shift is well-motivated: the field is moving this direction anyway.

3. **Option (A) -- LLM formalization -- is viable if scoped to a simplified formal language** (like MATH-VF's SimpleMath rather than full Lean/Coq). HERMES shows this can be cost-effective with hybrid approaches. But the <10% Coq formalization success rate makes full formalization impractical.

4. **Option (B) -- regex/heuristic extraction -- is viable only for final answers** (where it works well via Math-Verify), not for intermediate expressions. No published work achieves meaningful recall on intermediate CoT expression extraction with regex alone.

A strong proposal could combine (D) and (C): use answer-level verification as the cheap baseline, then upgrade to code-generation verification for problems where answer-level checking is insufficient, explicitly studying the cost-accuracy Pareto frontier between these approaches.

Sources:
- [HuggingFace Math-Verify](https://github.com/huggingface/Math-Verify)
- [Math-Verify fixing Open LLM Leaderboard](https://huggingface.co/blog/math_verify_leaderboard)
- [OpenCompass Math Evaluation Guidance](https://doc.opencompass.org.cn/advanced_guides/math_verify.html)
- [Let's Verify Step by Step (OpenAI)](https://cdn.openai.com/improving-mathematical-reasoning-with-process-supervision/Lets_Verify_Step_by_Step.pdf)
- [DeepConf: Deep Think with Confidence (Meta AI)](https://jiaweizzhao.github.io/deepconf/static/pdfs/deepconf_arxiv.pdf)
- [SymCode: Neurosymbolic Math Reasoning via Verifiable Code Generation](https://arxiv.org/abs/2510.25975)
- [HERMES: Efficient and Verifiable Mathematical Reasoning](https://arxiv.org/abs/2511.18760)
- [MATH-VF: Step-Wise Formal Verification](https://arxiv.org/abs/2505.20869)
- [S*: Test Time Scaling for Code Generation](https://arxiv.org/abs/2502.14382)
- [AIMO-2 Winning Solution](https://arxiv.org/abs/2504.16891)
- [Compute-Accuracy Pareto Frontiers for Open-Source Reasoning LLMs](https://arxiv.org/abs/2512.24776)
- [Scaling LLM Test-Time Compute Optimally (ICLR 2025)](https://arxiv.org/html/2408.03314v1)
- [Survey of Process Reward Models](https://arxiv.org/abs/2510.08049)
- [A Chain-of-Thought Is as Strong as Its Weakest Link: Verifier Benchmark](https://arxiv.org/html/2402.00559v4)
- [Instantiation-based Formalization (IJCAI 2025)](https://www.ijcai.org/proceedings/2025/0516.pdf)
- [IMO 2025 Verification-and-Refinement Pipeline](https://arxiv.org/abs/2507.15855)
- [DeepConf coverage (MLQ AI)](https://mlq.ai/news/meta-ai-unveils-deepconf-999-accuracy-on-aime-2025-marks-new-era-for-ai-reasoning/)

agentId: ae561688f22bb9758 (use SendMessage with to: 'ae561688f22bb9758' to continue this agent)
&lt;usage>total_tokens: 32629
tool_uses: 20
duration_ms: 144515&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4db5ece4-b53f-42e4-84ed-8967764003fd",
  "isSidechain": false,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "type": "user",
  "uuid": "4b9e10b7-02e1-477e-abb7-0fbfc2a5fecd",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm revising a research proposal. A key challenge is: how to extract mathematical expressions from natural language chain-of-thought (CoT) for symbolic verification. The reviewer says my options are:\n(a) LLM-based formalization (expensive, undermines \"cheap\" premise)\n(b) Regex/heuristic extraction (low recall, ~5-10%)\n(c) Generate code solutions directly (changes research question)\n(d) Answer-level verification only (check final answer constraints)\n\nPlease research:\n\n1. Search for \"extract mathematical expressions chain of thought symbolic verification regex heuristic\" to find approaches to expression extraction\n2. Search for \"answer-level verification mathematical reasoning constraint checking final answer\" \n3. Search for \"numerical answer verification MATH benchmark consistency checking\"\n4. Search for \"code generation verification mathematical reasoning test-time compute 2025 2026\" to understand option (c)\n5. Search for \"Python code execution verification math reasoning best-of-N\"\n6. Search for existing tools/repos on GitHub: \"sympy verify math reasoning chain of thought\"\n\nI need to understand:\n- What's the realistic extraction accuracy for regex/heuristic approaches on CoT?\n- Has anyone done answer-level-only verification (e.g., plug final answer back into original constraints)?\n- What's the actual cost differential between LLM formalization vs direct code generation?\n- Are there any papers studying the cost-accuracy Pareto frontier of different verification approaches?\n\nReport findings with specific numbers where available.",
    "agentId": "ae561688f22bb9758",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive findings across all your research questions. Here is my report.\n\n---\n\n## Research Findings: Verification Approaches for Mathematical CoT Reasoning\n\n### 1. Regex/Heuristic Extraction Accuracy (Option B)\n\n**For final answers: reasonably high. For intermediate expressions: very low.**\n\nThe critical distinction is between extracting the *final answer* versus extracting *intermediate mathematical expressions* from CoT text.\n\n**Final answer extraction** is a largely solved problem when models use standard formatting. HuggingFace's [Math-Verify](https://github.com/huggingface/Math-Verify) library uses a three-step pipeline (Regex Extraction -> SymPy Conversion -> Gold Comparison) with prioritized regex patterns (boxed mode for `\\boxed{}`, explicit mode for \"Answer:\" markers, speculative mode as fallback). It achieves higher accuracy than prior evaluators on the MATH dataset -- models solved an average of 61 more problems (a 4.66-point accuracy increase) when Math-Verify replaced older evaluators. OpenCompass uses a similar [MATHVerifyEvaluator](https://doc.opencompass.org.cn/advanced_guides/math_verify.html).\n\nHowever, these tools target **only the final boxed answer**, not intermediate reasoning steps. For intermediate expression extraction from free-form CoT, the picture is much worse:\n- LLM outputs contain answers in \"varied surface forms\" (e.g., \"alpha\" vs \"10^3\") that are semantically equivalent but textually different.\n- Regex-based tools \"typically handle only LaTeX expressions or simple string patterns, and struggle with basic semantic equivalence.\"\n- No published system reports recall figures for extracting intermediate mathematical expressions from CoT. Your reviewer's estimate of ~5-10% recall for intermediate steps appears reasonable -- this is essentially an unsolved problem for heuristic methods.\n\n**Key takeaway**: Regex works well for final-answer extraction (the `\\boxed{}` convention makes this tractable). It fails for extracting the full chain of intermediate symbolic expressions needed for step-level symbolic verification.\n\n### 2. Answer-Level-Only Verification (Option D)\n\nThis is the best-studied and most practical approach, and multiple strong systems exist:\n\n**Outcome Reward Models (ORMs)** check only the final answer. The landmark [Let's Verify Step by Step](https://cdn.openai.com/improving-mathematical-reasoning-with-process-supervision/Lets_Verify_Step_by_Step.pdf) (OpenAI, 2023) found that outcome supervision and process supervision led to \"similar final performance\" on grade-school math. ORMs are far cheaper to train: they require only final outcome labels, while Process Reward Models (PRMs) require correctness labels for every step (benchmarks average 7-13 steps per problem, so PRM annotation cost is 7-13x higher).\n\n**Self-consistency / majority voting** is the dominant answer-level verification method. Multiple CoT samples are generated and the most common final answer is selected. [DeepConf](https://jiaweizzhao.github.io/deepconf/static/pdfs/deepconf_arxiv.pdf) (Meta AI, 2025) pushed this to **99.9% accuracy on AIME 2025** by:\n- Filtering out low-confidence traces using token/group/tail confidence metrics\n- Weighting votes by confidence scores\n- Reducing total tokens by 43-84.7% compared to naive majority voting\n\n**Constraint-based answer checking** (plugging the final answer back into the original problem constraints) is used in specific settings. The [IJCAI 2025 instantiation-based formalization](https://www.ijcai.org/proceedings/2025/0516.pdf) paper infers concrete instantiations (positive and negative test cases) for each constraint, then verifies satisfiability -- but uses an LLM for the instantiation step. For numerical MATH-style problems, the simpler approach of checking `answer == gold_answer` (with SymPy equivalence) is standard.\n\n**Key takeaway**: Answer-level verification is cheap, well-understood, and with confidence-weighted voting achieves near-perfect accuracy on competition math. The limitation is it cannot detect *correct answers arrived at through flawed reasoning*.\n\n### 3. Cost Differential: LLM Formalization vs. Direct Code Generation (Options A vs. C)\n\nSeveral recent papers quantify this tradeoff:\n\n**SymCode** ([arXiv 2510.25975](https://arxiv.org/abs/2510.25975), Jan 2026): A training-free framework that instructs the LLM to generate SymPy code directly rather than formalizing natural language CoT. Achieves **up to 13.6 percentage point accuracy improvement** over baselines on MATH-500 and OlympiadBench, and is \"more token-efficient\" than natural language CoT because it shifts failures from \"opaque logical fallacies\" to \"transparent, programmatic errors.\"\n\n**HERMES** ([arXiv 2511.18760](https://arxiv.org/abs/2511.18760), Nov 2025): Interleaves informal reasoning with formally verified Lean proof steps. Achieves **up to 67% accuracy improvement on AIME'25 while using 80% fewer total inference FLOPs** compared to reward-based approaches. This represents the LLM-formalization approach (option A) but with a clever architecture that reduces cost.\n\n**MATH-VF** ([arXiv 2505.20869](https://arxiv.org/abs/2505.20869), May 2025): Step-wise formal verification using a custom SimpleMath language. Key finding: \"less than 10% of correct informal solutions can pass Coq verification\" -- full formalization is extremely hard. MATH-VF addresses this by allowing gaps and using a simpler language closer to natural mathematical text. It exploits sparsity (most conclusions depend on at most 4 premises) to reduce token cost.\n\n**S*** ([arXiv 2502.14382](https://arxiv.org/abs/2502.14382)): Test-time scaling for code generation. Uses iterative debugging with interpreter execution. A **3B model with S* outperforms GPT-4o-mini**; GPT-4o-mini with S* outperforms o1-preview by 3.7%. The key advantage of code generation: \"the availability of programmatic interpreters enables execution of programs to obtain precise outputs and error messages.\"\n\n**AIMO-2 winning solution** ([arXiv 2504.16891](https://arxiv.org/abs/2504.16891)): Used Tool-Integrated Reasoning (TIR) -- the LLM generates code within its reasoning chain, executes it, and continues. 1.7M high-quality TIR solutions were generated, with SymPy and Python execution as the verification backbone. This is essentially option (C) deployed at scale and winning the competition.\n\n**Cost comparison summary**:\n| Approach | Relative Token Cost | Accuracy Gain | Verification Guarantee |\n|----------|-------------------|---------------|----------------------|\n| LLM formalization to Lean/Coq (A) | Very high (multiple LLM calls + prover) | Strong but <10% formalization success rate for Coq | Formal proof |\n| MATH-VF SimpleMath (A, simplified) | High but reduced via sparsity | Moderate | Semi-formal |\n| HERMES (A, hybrid) | 80% fewer FLOPs than reward methods | +67% on AIME'25 | Formal for verified steps |\n| SymCode / direct code gen (C) | Lower than NL CoT | +13.6 pp on MATH-500 | Execution-based |\n| Answer-level voting (D) | Low (just run N samples) | 99.9% on AIME'25 with DeepConf | Final answer only |\n\n### 4. Pareto Frontier Studies\n\nYes, this has been explicitly studied:\n\n**[Compute-Accuracy Pareto Frontiers for Open-Source Reasoning LLMs](https://arxiv.org/abs/2512.24776)** (Dec 2025): Maps FLOPs-accuracy Pareto frontiers across math benchmarks. Key findings:\n- MoE models consistently lead the Pareto frontier (higher accuracy at comparable FLOP budgets)\n- There is a **task-dependent Pareto knee** beyond which additional compute gives negligible accuracy gain\n- Easier benchmarks plateau at lower compute; competition-level problems require significantly more\n- A 1.5B model with parallel scaling achieves 83.6% on MATH-500, exceeding a 7B model's vanilla 82.0%\n\n**[Scaling LLM Test-Time Compute Optimally](https://arxiv.org/html/2408.03314v1)** (ICLR 2025): Proposes compute-optimal inference with the REBASE method. An adaptive, prompt-dependent strategy improves test-time compute efficiency by **2-4x**.\n\n**Joint reasoner-verifier training** ([arXiv 2505.04842](https://arxiv.org/html/2505.04842v2)): Training the LLM as both reasoner and generative verifier enables **8-32x more efficient test-time compute scaling** compared to base RL methods.\n\n### Synthesis and Recommendation for Your Proposal\n\nGiven these findings, the reviewer's four options have a clear ordering:\n\n1. **Option (D) -- answer-level verification -- is the strongest starting point.** It is cheap, well-studied, and achieves near-perfect accuracy with methods like DeepConf. You can frame this as \"outcome-based verification\" and cite the ORM literature showing it matches PRM performance for final accuracy.\n\n2. **Option (C) -- code generation -- is the most promising for going beyond final answers.** SymCode and the AIMO-2 winning approach show that generating SymPy code is cheaper than LLM formalization, provides execution-based verification guarantees, and achieves large accuracy improvements. The research question shifts, but the shift is well-motivated: the field is moving this direction anyway.\n\n3. **Option (A) -- LLM formalization -- is viable if scoped to a simplified formal language** (like MATH-VF's SimpleMath rather than full Lean/Coq). HERMES shows this can be cost-effective with hybrid approaches. But the <10% Coq formalization success rate makes full formalization impractical.\n\n4. **Option (B) -- regex/heuristic extraction -- is viable only for final answers** (where it works well via Math-Verify), not for intermediate expressions. No published work achieves meaningful recall on intermediate CoT expression extraction with regex alone.\n\nA strong proposal could combine (D) and (C): use answer-level verification as the cheap baseline, then upgrade to code-generation verification for problems where answer-level checking is insufficient, explicitly studying the cost-accuracy Pareto frontier between these approaches.\n\nSources:\n- [HuggingFace Math-Verify](https://github.com/huggingface/Math-Verify)\n- [Math-Verify fixing Open LLM Leaderboard](https://huggingface.co/blog/math_verify_leaderboard)\n- [OpenCompass Math Evaluation Guidance](https://doc.opencompass.org.cn/advanced_guides/math_verify.html)\n- [Let's Verify Step by Step (OpenAI)](https://cdn.openai.com/improving-mathematical-reasoning-with-process-supervision/Lets_Verify_Step_by_Step.pdf)\n- [DeepConf: Deep Think with Confidence (Meta AI)](https://jiaweizzhao.github.io/deepconf/static/pdfs/deepconf_arxiv.pdf)\n- [SymCode: Neurosymbolic Math Reasoning via Verifiable Code Generation](https://arxiv.org/abs/2510.25975)\n- [HERMES: Efficient and Verifiable Mathematical Reasoning](https://arxiv.org/abs/2511.18760)\n- [MATH-VF: Step-Wise Formal Verification](https://arxiv.org/abs/2505.20869)\n- [S*: Test Time Scaling for Code Generation](https://arxiv.org/abs/2502.14382)\n- [AIMO-2 Winning Solution](https://arxiv.org/abs/2504.16891)\n- [Compute-Accuracy Pareto Frontiers for Open-Source Reasoning LLMs](https://arxiv.org/abs/2512.24776)\n- [Scaling LLM Test-Time Compute Optimally (ICLR 2025)](https://arxiv.org/html/2408.03314v1)\n- [Survey of Process Reward Models](https://arxiv.org/abs/2510.08049)\n- [A Chain-of-Thought Is as Strong as Its Weakest Link: Verifier Benchmark](https://arxiv.org/html/2402.00559v4)\n- [Instantiation-based Formalization (IJCAI 2025)](https://www.ijcai.org/proceedings/2025/0516.pdf)\n- [IMO 2025 Verification-and-Refinement Pipeline](https://arxiv.org/abs/2507.15855)\n- [DeepConf coverage (MLQ AI)](https://mlq.ai/news/meta-ai-unveils-deepconf-999-accuracy-on-aime-2025-marks-new-era-for-ai-reasoning/)"
      }
    ],
    "totalDurationMs": 144515,
    "totalTokens": 32629,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5562,
      "cache_read_input_tokens": 23841,
      "output_tokens": 3225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5562
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3225,
          "cache_read_input_tokens": 23841,
          "cache_creation_input_tokens": 5562,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5562,
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
      "otherToolCount": 20
    }
  },
  "sourceToolAssistantUUID": "4db5ece4-b53f-42e4-84ed-8967764003fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Symbolic Pre-Filtering for Compute-Efficient Best-of-N Verification: A…",
  "leafUuid": "4b9e10b7-02e1-477e-abb7-0fbfc2a5fecd",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Quantifying symbolic-neural verifier complementarity in best-of-N reasoning",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b"
}
```

---

### Tool result

_source line 17 · 2026-05-10T18:12:41.810Z_

<details><summary>↩ Tool result · `toolu_01Cyw9CPwhjutGmTunjFwFr1`</summary>

```text
Here are the detailed findings for each of the six papers.

---

## 1. MATH-VF (Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving)

**Formalization approach -- LLM-based, not pattern-based.** MATH-VF uses an LLM (DeepSeek-V3 or GPT-4) as the "Formalizer" via few-shot prompting to translate natural language CoT steps into a custom formal language called **SimpleMath**, which extends first-order logic. The LLM is given detailed grammar instructions and inference rule specifications along with few-shot examples. The formal representation uses Fitch-style proofs organized into five statement types: Facts, Assumptions, Theorems, Definitions, and Conclusions. This is categorically different from pattern-based extraction -- it relies entirely on the LLM's ability to interpret and translate prose reasoning into formal structure.

**Formalization accuracy.** The paper reports that over 90% of statements in natural language solutions (on MATH500) can be correctly formalized and verified. However, they acknowledge a significant failure mode: syntax errors in the formalized output can cause the Critic (solver) to fail entirely. There is no separate metric isolating how often the Formalizer produces syntactically invalid output vs. semantically incorrect formalizations.

**Computational cost.** The paper emphasizes token efficiency through a "Solution Graph" structure that limits each verification step to at most M <= 4 premises (rather than the full cumulative context). This means input tokens scale as C_2(n) <= n x M rather than n(n+1)/2. However, the paper does **not** report wall-clock time, total token counts, or number of LLM calls per solution. The approach requires at minimum: one LLM call for formalization + multiple solver calls (SymPy/Z3) per step. Being training-free, it avoids the cost of training reward models but requires per-solution inference-time computation.

**Key results.** On correctness verification: DeepSeek-V3 achieves 95.7% accuracy vs. LLM+Coq at only 6.8%. On ProcessBench, MATH-VF achieves F1 of 74.1 -- lower than the trained Qwen2.5-MATH-PRM (78.3) but notably more stable across difficulty levels. A striking finding: only ~10% of correct informal solutions could produce valid Coq proofs, highlighting the fragility of full formal proof generation vs. MATH-VF's lighter-weight formalization.

**Limitations.** (1) Syntax errors in formalization cascade to solver failures. (2) No analysis of step "effectiveness" -- validates correctness but not whether a step actually advances toward the solution. (3) Lower F1 than training-based methods on ProcessBench.

---

## 2. FoVer (Efficient PRM Training Data Synthesis via Formal Verification, ACL 2026 Findings)

**Pipeline for generating training labels.** FoVer operates in two stages. Stage 1: LLMs (Llama 3.1 8B and Qwen 2.5 7B) generate step-by-step **formal** solutions formatted for Z3 or Isabelle, guided by few-shot demonstrations. Stage 2: Formal verification tools automatically assign step-level binary labels (correct=1, incorrect=0) without any human annotation or additional LLM calls. The key insight is that by having the LLM generate solutions in a formal language amenable to tool-based checking, verification becomes deterministic and free.

**Step-level verification.** Each reasoning step is verified independently. For logical entailment tasks (using Z3), they test satisfiability of each step in isolation. For theorem proving tasks (using Isabelle), each proof line is checked independently while assuming other steps are correct. This yields per-step binary labels suitable for PRM training.

**Data composition.** The FoVer-80K dataset (they also mention a 40K variant) spans two domains: (1) formal logic -- logical entailment tasks from FLDx2 verified with Z3, and (2) formal theorem proving -- math word problem proofs from GSM8K/MetaMathQA/Big-Math verified with Isabelle. The dataset maintains a 50% error rate for balanced training.

**Generalization.** PRMs trained on FoVer data generalize remarkably well. They improve performance not only on math and logic tasks (informal variants of the formal training tasks) but also on substantially different benchmarks: NLI, BBH, and MMLU. This "formal-to-informal transfer" is a key contribution.

**Comparison to alternatives.** vs. human annotation: eliminates annotators entirely (prior work discarded 30% of annotations due to low inter-annotator agreement). vs. Monte Carlo rollouts: requires only one LLM call per solution vs. multiple calls per step with noisy labels. vs. stronger-LLM labeling: introduces an external verification signal independent of LLM capabilities.

**Limitation.** FoVer-PRMs can become "overly strict," penalizing acceptable approximations in intermediate steps -- a side effect of formal verification's precision.

---

## 3. BoN-MAV (Multi-Agent Verification: Scaling Test-Time Compute with Multiple Verifiers, COLM 2025)

**How they combine heterogeneous verifiers.** BoN-MAV uses a simple democratic voting mechanism: each Aspect Verifier (AV) produces a binary True/False approval, and the aggregated score for a candidate is the **sum of positive votes** from all AVs, with equal weighting. No calibration is needed because the signals are binary, avoiding the score-normalization issues that plague continuous-valued reward models.

**Verifier diversity.** AVs vary along three axes: (1) **Base LLMs**: Gemini-1.5-Flash and GPT-4o-mini. (2) **Aspects verified**: mathematical correctness, logical soundness, factuality, unit conversions, domain knowledge, general correctness. (3) **Verification strategies**: direct yes/no, step-by-step analysis, solution rephrasing/summarization, edge case checking, identifying common mistakes. This combinatorial design yields 20 total verifiers (10 per base model), with domain-specific subsets selected via validation.

**Results combining different modalities.** At n=16 candidates: MATH with Gemini-1.5-Flash: BoN-MAV 66.0% vs. reward model 61.7% vs. self-consistency 59.0%. MMLU-Pro with GPT-4o: 75.7% vs. 72.7% (RM) vs. 76.3% (SC). GPQA diamond: 59.0% vs. 58.0% vs. 59.0%.

**Scaling to N=256.** On MATH with Gemini-1.5-Flash, baselines plateau at ~61% while BoN-MAV continues scaling to 69% accuracy -- nearly double the improvement. When accounting for total compute budget (verification overhead), BoN-MAV initially underperforms but eventually significantly outperforms both baselines with sufficient compute.

**Weak-to-strong generalization.** Using only weak verifiers (Flash/mini), strong generators improve substantially: Gemini-1.5-Pro gains +8.0 on MATH, +4.3 on MMLU-Pro, +4.0 on GPQA. GPT-4o gains +8.0 on MATH, +2.4 on MMLU-Pro, +5.0 on GPQA. This demonstrates that diverse perspectives from multiple smaller models produce a verification signal robust enough to improve SOTA generators.

**Self-improvement.** Using the same base LLM for generation and verification: Gemini-1.5-Flash gains +6.3 on MATH; GPT-4o-mini gains +7.0 on MATH, +8.0 on GPQA. Gains are strongest on mathematical/scientific reasoning.

---

## 4. "When Does Verification Pay Off?" (arXiv 2512.02304)

**Core finding.** Verification does not always help. Its effectiveness depends critically on the relationship between solver and verifier. The paper evaluates 37 models across 7 families (Llama3, Qwen2.5, Qwen3, DeepSeek-R1, plus base variants) on 9 benchmarks (GSM8K, AIME, 3SAT, Sudoku, Matrix Multiplication, MMLU-STEM, MMLU-Social Sciences, CSQA, GPQA).

**The solver-verifier distribution difference claim.** They measure distribution similarity via **cosine similarity between solution embeddings** (using sentence-transformers). Key finding: higher cosine similarity between solver and verifier solution distributions correlates with increased false positive rates and reduced verifier gain. In other words, **the more similarly two models "think," the less useful one is for verifying the other**. They validate this with generation log-likelihood as an alternative metric.

**Hierarchy of verification effectiveness.** Clear ordering: cross-family verification >> intra-family verification >> self-verification. Self-verification yields the smallest gains. DeepSeek and Qwen3 models showed negligible self-verification gains because they already perform "spontaneous self-verification" during solving (73-96% of solutions include self-checking, vs. 1-2% for other families).

**Impact of reasoning post-training.** Post-training improves solver accuracy substantially (e.g., Qwen3 improved by 35.4%) but simultaneously **reduces** self- and intra-family verification gains while **boosting** cross-family verification effectiveness. Post-trained models have higher false positive rates when verifying same-family outputs.

**False positive rate analysis.** FPR increases during self and intra-family verification as verifier strength increases (strong reasoners are biased toward accepting solutions that resemble their own reasoning patterns). In cross-family settings, FPR decreases slightly with stronger verifiers.

**Verifier gain metric.** Defined as Precision - SolverAccuracy, measuring the improvement from rejection sampling. Mathematical/logical tasks (AIME, GSM8K, 3SAT) yield higher gains. Factual recall tasks show minimal verification benefit.

**Practical recommendations.** (1) Use verifier gain, not accuracy alone, to evaluate pairings. (2) Prefer verifiers that "think differently" from solvers -- maximize distribution dissimilarity. (3) Avoid strong reasoning models as self-verifiers. (4) Prioritize mathematical/logical tasks for verification. (5) Cross-family pairing significantly outperforms self-verification for SOTA models.

---

## 5. "Controllable and Verifiable Process Data Synthesis for PRMs" (arXiv 2605.02395)

**Symbolic recomputation pipeline.** The framework follows four stages: (1) Construct a correct symbolic reasoning chain from base facts to target conclusions using an LLM-symbolic prover. (2) Select an intermediate step k and inject a **template-aware error** constrained by the rule template at that position. (3) **Recompute** all downstream steps from the corrupted state, maintaining logical coherence with the error. (4) Verify the injected error via prefix non-derivability checks.

**Error types.** 11 error categories across two groups. **Truth-state errors** (7 types): XOR-as-OR, XOR-as-equivalence, AND/OR confusion, implication misuse, dropped conditions, partial evaluation, vacuous truth errors. **Structural errors** (4 types): converse errors (applying rules in unsupported direction), missing prerequisites, circular references, redundant steps. Errors are "structurally compatible" with the rule template at the injection point.

**Key definitions.** "Prefix-invalid" means the corrupted step cannot be derived from the correct prefix (steps before the error). "Trajectory-consistent" means all steps after the error are logically coherent with the corrupted state. Together, these ensure the erroneous chain has a clearly identifiable first-error point while remaining internally consistent afterward -- critical for training PRMs to localize errors.

**Verification.** For non-structural errors: the corrupted conclusion is tested against the original prefix; samples are rejected if still derivable. For structural errors: verification confirms the step violates intended rule direction, dependency order, or acyclic constraints.

**Results.** Logical reasoning (Best-of-8 reranking): Llama-3.1-8B improves from 0.528 to 0.591 average; Qwen-2.5-7B from 0.567 to 0.615. Tested across FOLIO, LogicNLI, ANLI, HANS, and others. Mathematical reasoning transfer (ProcessBench F1): GSM8K 21.2%, MATH 21.3%, Olympiad 18.6% with 20k training instances. Performance improves with training data scale (5k to 20k), suggesting the process-level signal transfers beyond the symbolic setting.

**Key advantage over alternatives.** Unlike rollout/search methods, this approach provides explicit control over error type, error location, and trajectory consistency. Unlike ProverGen (which synthesizes correct chains), this method produces erroneous trajectories with controlled first-error injection and downstream propagation.

---

## 6. SymCode (A Neurosymbolic Approach to Mathematical Reasoning via Verifiable Code Generation, EACL 2026)

**Confirmed: Direct code generation, no extraction patterns.** SymCode generates Python/SymPy code **directly** from the problem statement. It does NOT first produce prose CoT and then extract/formalize expressions. As the paper states: "Instead of prompting an LLM to describe its reasoning in prose, SymCode instructs it to construct a verifiable, executable Python script where the code serves as the reasoning trace." This fundamentally distinguishes it from methods like MATH-VF that formalize existing prose reasoning.

**Pipeline.** Problem statement -> LLM generates a complete Python script (importing SymPy, with step-by-step comments, symbolic definitions, algebraic manipulations, verification assertions, and LaTeX-boxed output) -> execution in sandboxed interpreter -> if failure, error feedback is returned to the LLM for self-debugging (2-3 attempts) -> final answer extracted.

**Self-debugging mechanism.** If execution fails (syntax error, runtime exception, or assertion failure), the error message and traceback are captured and fed back to the LLM with the instruction to debug. This iterative cycle repeats for a preset limit (typically 2-3 attempts). This deterministic feedback loop is unavailable to prose-based reasoners.

**Training-free.** Entirely training-free; operates through specialized prompting at inference time.

**SymPy role.** SymPy serves as a Computer Algebra System manipulating expressions in exact symbolic form (e.g., representing sqrt(2) precisely rather than 1.414...), enabling true algebraic reasoning including equation solving, simplification, differentiation, and integration without rounding errors.

**Results.** Performance gains increase with problem difficulty. On OlympiadBench with GPT-5-nano: SymCode+ 80.0% vs. best baseline (ToT) 68.0% (+12.0 pts). On AIME 24-25: 65.0% vs. 51.7% (+13.3 pts). On MATH-500: 91.4% vs. CoT 93.4% (-2.0 pts -- slightly lower on easier problems where prose CoT suffices).

---

Sources:
- [MATH-VF: Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving](https://arxiv.org/abs/2505.20869)
- [MATH-VF Full HTML](https://arxiv.org/html/2505.20869v1)
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)
- [FoVer Project Page](https://fover-prm.github.io/)
- [FoVer GitHub](https://github.com/psunlpgroup/FoVer)
- [Multi-Agent Verification: Scaling Test-Time Compute with Multiple Verifiers](https://arxiv.org/abs/2502.20379)
- [MAV OpenReview (COLM 2025)](https://openreview.net/forum?id=LriQ3NY9uL)
- [When Does Verification Pay Off?](https://arxiv.org/abs/2512.02304)
- [Controllable and Verifiable Process Data Synthesis for PRMs](https://arxiv.org/abs/2605.02395v1)
- [SymCode: A Neurosymbolic Approach to Mathematical Reasoning via Verifiable Code Generation](https://arxiv.org/abs/2510.25975)
- [SymCode ACL Anthology (EACL 2026 Findings)](https://aclanthology.org/2026.findings-eacl.76.pdf)

agentId: a58dc4de6f5c97c2c (use SendMessage with to: 'a58dc4de6f5c97c2c' to continue this agent)
&lt;usage>total_tokens: 27674
tool_uses: 14
duration_ms: 171769&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35646cf2-27d7-4e8f-af2d-8e824bd1fd9e",
  "isSidechain": false,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "type": "user",
  "uuid": "e49e32a8-6813-4542-ad24-c4508f083caa",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm revising a research proposal about symbolic pre-filtering for best-of-N verification in math reasoning. I need to understand several key related works deeply.\n\nPlease do the following:\n\n1. **MATH-VF**: Search for \"MATH-VF step-wise formal verification LLM SymPy Z3 2025\" and use WebFetch to read the paper. I specifically need to understand:\n   - How does MATH-VF extract/formalize mathematical expressions from CoT? Is it LLM-based or pattern-based?\n   - What is their formalization accuracy?\n   - What is the computational cost of their approach?\n\n2. **FoVer**: Search for \"FoVer ACL 2026 Z3 Isabelle PRM training data\" and fetch the paper. I need:\n   - How they use formal verification to generate training labels\n   - Their approach to step-level verification\n\n3. **BoN-MAV**: Search for \"BoN-MAV multi-agent verification best-of-N 2025\" and fetch details. I need:\n   - How they combine heterogeneous verifiers\n   - Their results on combining different verification modalities\n\n4. **\"When Does Verification Pay Off?\"**: Search for \"when does verification pay off 2025 solver verifier distribution\" and fetch the paper. I need:\n   - Their findings on when verification helps\n   - The solver-verifier distribution difference claim\n\n5. **\"Controllable and Verifiable Process Data Synthesis for PRMs\"**: Search for \"controllable verifiable process data synthesis PRM symbolic recomputation 2026\" and fetch details.\n\n6. **SymCode**: Search for \"SymCode neurosymbolic verifiable code generation EACL 2026\" to confirm it generates code directly (no extraction patterns).\n\nReport detailed findings for each paper.",
    "agentId": "a58dc4de6f5c97c2c",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the detailed findings for each of the six papers.\n\n---\n\n## 1. MATH-VF (Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving)\n\n**Formalization approach -- LLM-based, not pattern-based.** MATH-VF uses an LLM (DeepSeek-V3 or GPT-4) as the \"Formalizer\" via few-shot prompting to translate natural language CoT steps into a custom formal language called **SimpleMath**, which extends first-order logic. The LLM is given detailed grammar instructions and inference rule specifications along with few-shot examples. The formal representation uses Fitch-style proofs organized into five statement types: Facts, Assumptions, Theorems, Definitions, and Conclusions. This is categorically different from pattern-based extraction -- it relies entirely on the LLM's ability to interpret and translate prose reasoning into formal structure.\n\n**Formalization accuracy.** The paper reports that over 90% of statements in natural language solutions (on MATH500) can be correctly formalized and verified. However, they acknowledge a significant failure mode: syntax errors in the formalized output can cause the Critic (solver) to fail entirely. There is no separate metric isolating how often the Formalizer produces syntactically invalid output vs. semantically incorrect formalizations.\n\n**Computational cost.** The paper emphasizes token efficiency through a \"Solution Graph\" structure that limits each verification step to at most M <= 4 premises (rather than the full cumulative context). This means input tokens scale as C_2(n) <= n x M rather than n(n+1)/2. However, the paper does **not** report wall-clock time, total token counts, or number of LLM calls per solution. The approach requires at minimum: one LLM call for formalization + multiple solver calls (SymPy/Z3) per step. Being training-free, it avoids the cost of training reward models but requires per-solution inference-time computation.\n\n**Key results.** On correctness verification: DeepSeek-V3 achieves 95.7% accuracy vs. LLM+Coq at only 6.8%. On ProcessBench, MATH-VF achieves F1 of 74.1 -- lower than the trained Qwen2.5-MATH-PRM (78.3) but notably more stable across difficulty levels. A striking finding: only ~10% of correct informal solutions could produce valid Coq proofs, highlighting the fragility of full formal proof generation vs. MATH-VF's lighter-weight formalization.\n\n**Limitations.** (1) Syntax errors in formalization cascade to solver failures. (2) No analysis of step \"effectiveness\" -- validates correctness but not whether a step actually advances toward the solution. (3) Lower F1 than training-based methods on ProcessBench.\n\n---\n\n## 2. FoVer (Efficient PRM Training Data Synthesis via Formal Verification, ACL 2026 Findings)\n\n**Pipeline for generating training labels.** FoVer operates in two stages. Stage 1: LLMs (Llama 3.1 8B and Qwen 2.5 7B) generate step-by-step **formal** solutions formatted for Z3 or Isabelle, guided by few-shot demonstrations. Stage 2: Formal verification tools automatically assign step-level binary labels (correct=1, incorrect=0) without any human annotation or additional LLM calls. The key insight is that by having the LLM generate solutions in a formal language amenable to tool-based checking, verification becomes deterministic and free.\n\n**Step-level verification.** Each reasoning step is verified independently. For logical entailment tasks (using Z3), they test satisfiability of each step in isolation. For theorem proving tasks (using Isabelle), each proof line is checked independently while assuming other steps are correct. This yields per-step binary labels suitable for PRM training.\n\n**Data composition.** The FoVer-80K dataset (they also mention a 40K variant) spans two domains: (1) formal logic -- logical entailment tasks from FLDx2 verified with Z3, and (2) formal theorem proving -- math word problem proofs from GSM8K/MetaMathQA/Big-Math verified with Isabelle. The dataset maintains a 50% error rate for balanced training.\n\n**Generalization.** PRMs trained on FoVer data generalize remarkably well. They improve performance not only on math and logic tasks (informal variants of the formal training tasks) but also on substantially different benchmarks: NLI, BBH, and MMLU. This \"formal-to-informal transfer\" is a key contribution.\n\n**Comparison to alternatives.** vs. human annotation: eliminates annotators entirely (prior work discarded 30% of annotations due to low inter-annotator agreement). vs. Monte Carlo rollouts: requires only one LLM call per solution vs. multiple calls per step with noisy labels. vs. stronger-LLM labeling: introduces an external verification signal independent of LLM capabilities.\n\n**Limitation.** FoVer-PRMs can become \"overly strict,\" penalizing acceptable approximations in intermediate steps -- a side effect of formal verification's precision.\n\n---\n\n## 3. BoN-MAV (Multi-Agent Verification: Scaling Test-Time Compute with Multiple Verifiers, COLM 2025)\n\n**How they combine heterogeneous verifiers.** BoN-MAV uses a simple democratic voting mechanism: each Aspect Verifier (AV) produces a binary True/False approval, and the aggregated score for a candidate is the **sum of positive votes** from all AVs, with equal weighting. No calibration is needed because the signals are binary, avoiding the score-normalization issues that plague continuous-valued reward models.\n\n**Verifier diversity.** AVs vary along three axes: (1) **Base LLMs**: Gemini-1.5-Flash and GPT-4o-mini. (2) **Aspects verified**: mathematical correctness, logical soundness, factuality, unit conversions, domain knowledge, general correctness. (3) **Verification strategies**: direct yes/no, step-by-step analysis, solution rephrasing/summarization, edge case checking, identifying common mistakes. This combinatorial design yields 20 total verifiers (10 per base model), with domain-specific subsets selected via validation.\n\n**Results combining different modalities.** At n=16 candidates: MATH with Gemini-1.5-Flash: BoN-MAV 66.0% vs. reward model 61.7% vs. self-consistency 59.0%. MMLU-Pro with GPT-4o: 75.7% vs. 72.7% (RM) vs. 76.3% (SC). GPQA diamond: 59.0% vs. 58.0% vs. 59.0%.\n\n**Scaling to N=256.** On MATH with Gemini-1.5-Flash, baselines plateau at ~61% while BoN-MAV continues scaling to 69% accuracy -- nearly double the improvement. When accounting for total compute budget (verification overhead), BoN-MAV initially underperforms but eventually significantly outperforms both baselines with sufficient compute.\n\n**Weak-to-strong generalization.** Using only weak verifiers (Flash/mini), strong generators improve substantially: Gemini-1.5-Pro gains +8.0 on MATH, +4.3 on MMLU-Pro, +4.0 on GPQA. GPT-4o gains +8.0 on MATH, +2.4 on MMLU-Pro, +5.0 on GPQA. This demonstrates that diverse perspectives from multiple smaller models produce a verification signal robust enough to improve SOTA generators.\n\n**Self-improvement.** Using the same base LLM for generation and verification: Gemini-1.5-Flash gains +6.3 on MATH; GPT-4o-mini gains +7.0 on MATH, +8.0 on GPQA. Gains are strongest on mathematical/scientific reasoning.\n\n---\n\n## 4. \"When Does Verification Pay Off?\" (arXiv 2512.02304)\n\n**Core finding.** Verification does not always help. Its effectiveness depends critically on the relationship between solver and verifier. The paper evaluates 37 models across 7 families (Llama3, Qwen2.5, Qwen3, DeepSeek-R1, plus base variants) on 9 benchmarks (GSM8K, AIME, 3SAT, Sudoku, Matrix Multiplication, MMLU-STEM, MMLU-Social Sciences, CSQA, GPQA).\n\n**The solver-verifier distribution difference claim.** They measure distribution similarity via **cosine similarity between solution embeddings** (using sentence-transformers). Key finding: higher cosine similarity between solver and verifier solution distributions correlates with increased false positive rates and reduced verifier gain. In other words, **the more similarly two models \"think,\" the less useful one is for verifying the other**. They validate this with generation log-likelihood as an alternative metric.\n\n**Hierarchy of verification effectiveness.** Clear ordering: cross-family verification >> intra-family verification >> self-verification. Self-verification yields the smallest gains. DeepSeek and Qwen3 models showed negligible self-verification gains because they already perform \"spontaneous self-verification\" during solving (73-96% of solutions include self-checking, vs. 1-2% for other families).\n\n**Impact of reasoning post-training.** Post-training improves solver accuracy substantially (e.g., Qwen3 improved by 35.4%) but simultaneously **reduces** self- and intra-family verification gains while **boosting** cross-family verification effectiveness. Post-trained models have higher false positive rates when verifying same-family outputs.\n\n**False positive rate analysis.** FPR increases during self and intra-family verification as verifier strength increases (strong reasoners are biased toward accepting solutions that resemble their own reasoning patterns). In cross-family settings, FPR decreases slightly with stronger verifiers.\n\n**Verifier gain metric.** Defined as Precision - SolverAccuracy, measuring the improvement from rejection sampling. Mathematical/logical tasks (AIME, GSM8K, 3SAT) yield higher gains. Factual recall tasks show minimal verification benefit.\n\n**Practical recommendations.** (1) Use verifier gain, not accuracy alone, to evaluate pairings. (2) Prefer verifiers that \"think differently\" from solvers -- maximize distribution dissimilarity. (3) Avoid strong reasoning models as self-verifiers. (4) Prioritize mathematical/logical tasks for verification. (5) Cross-family pairing significantly outperforms self-verification for SOTA models.\n\n---\n\n## 5. \"Controllable and Verifiable Process Data Synthesis for PRMs\" (arXiv 2605.02395)\n\n**Symbolic recomputation pipeline.** The framework follows four stages: (1) Construct a correct symbolic reasoning chain from base facts to target conclusions using an LLM-symbolic prover. (2) Select an intermediate step k and inject a **template-aware error** constrained by the rule template at that position. (3) **Recompute** all downstream steps from the corrupted state, maintaining logical coherence with the error. (4) Verify the injected error via prefix non-derivability checks.\n\n**Error types.** 11 error categories across two groups. **Truth-state errors** (7 types): XOR-as-OR, XOR-as-equivalence, AND/OR confusion, implication misuse, dropped conditions, partial evaluation, vacuous truth errors. **Structural errors** (4 types): converse errors (applying rules in unsupported direction), missing prerequisites, circular references, redundant steps. Errors are \"structurally compatible\" with the rule template at the injection point.\n\n**Key definitions.** \"Prefix-invalid\" means the corrupted step cannot be derived from the correct prefix (steps before the error). \"Trajectory-consistent\" means all steps after the error are logically coherent with the corrupted state. Together, these ensure the erroneous chain has a clearly identifiable first-error point while remaining internally consistent afterward -- critical for training PRMs to localize errors.\n\n**Verification.** For non-structural errors: the corrupted conclusion is tested against the original prefix; samples are rejected if still derivable. For structural errors: verification confirms the step violates intended rule direction, dependency order, or acyclic constraints.\n\n**Results.** Logical reasoning (Best-of-8 reranking): Llama-3.1-8B improves from 0.528 to 0.591 average; Qwen-2.5-7B from 0.567 to 0.615. Tested across FOLIO, LogicNLI, ANLI, HANS, and others. Mathematical reasoning transfer (ProcessBench F1): GSM8K 21.2%, MATH 21.3%, Olympiad 18.6% with 20k training instances. Performance improves with training data scale (5k to 20k), suggesting the process-level signal transfers beyond the symbolic setting.\n\n**Key advantage over alternatives.** Unlike rollout/search methods, this approach provides explicit control over error type, error location, and trajectory consistency. Unlike ProverGen (which synthesizes correct chains), this method produces erroneous trajectories with controlled first-error injection and downstream propagation.\n\n---\n\n## 6. SymCode (A Neurosymbolic Approach to Mathematical Reasoning via Verifiable Code Generation, EACL 2026)\n\n**Confirmed: Direct code generation, no extraction patterns.** SymCode generates Python/SymPy code **directly** from the problem statement. It does NOT first produce prose CoT and then extract/formalize expressions. As the paper states: \"Instead of prompting an LLM to describe its reasoning in prose, SymCode instructs it to construct a verifiable, executable Python script where the code serves as the reasoning trace.\" This fundamentally distinguishes it from methods like MATH-VF that formalize existing prose reasoning.\n\n**Pipeline.** Problem statement -> LLM generates a complete Python script (importing SymPy, with step-by-step comments, symbolic definitions, algebraic manipulations, verification assertions, and LaTeX-boxed output) -> execution in sandboxed interpreter -> if failure, error feedback is returned to the LLM for self-debugging (2-3 attempts) -> final answer extracted.\n\n**Self-debugging mechanism.** If execution fails (syntax error, runtime exception, or assertion failure), the error message and traceback are captured and fed back to the LLM with the instruction to debug. This iterative cycle repeats for a preset limit (typically 2-3 attempts). This deterministic feedback loop is unavailable to prose-based reasoners.\n\n**Training-free.** Entirely training-free; operates through specialized prompting at inference time.\n\n**SymPy role.** SymPy serves as a Computer Algebra System manipulating expressions in exact symbolic form (e.g., representing sqrt(2) precisely rather than 1.414...), enabling true algebraic reasoning including equation solving, simplification, differentiation, and integration without rounding errors.\n\n**Results.** Performance gains increase with problem difficulty. On OlympiadBench with GPT-5-nano: SymCode+ 80.0% vs. best baseline (ToT) 68.0% (+12.0 pts). On AIME 24-25: 65.0% vs. 51.7% (+13.3 pts). On MATH-500: 91.4% vs. CoT 93.4% (-2.0 pts -- slightly lower on easier problems where prose CoT suffices).\n\n---\n\nSources:\n- [MATH-VF: Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving](https://arxiv.org/abs/2505.20869)\n- [MATH-VF Full HTML](https://arxiv.org/html/2505.20869v1)\n- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)\n- [FoVer Project Page](https://fover-prm.github.io/)\n- [FoVer GitHub](https://github.com/psunlpgroup/FoVer)\n- [Multi-Agent Verification: Scaling Test-Time Compute with Multiple Verifiers](https://arxiv.org/abs/2502.20379)\n- [MAV OpenReview (COLM 2025)](https://openreview.net/forum?id=LriQ3NY9uL)\n- [When Does Verification Pay Off?](https://arxiv.org/abs/2512.02304)\n- [Controllable and Verifiable Process Data Synthesis for PRMs](https://arxiv.org/abs/2605.02395v1)\n- [SymCode: A Neurosymbolic Approach to Mathematical Reasoning via Verifiable Code Generation](https://arxiv.org/abs/2510.25975)\n- [SymCode ACL Anthology (EACL 2026 Findings)](https://aclanthology.org/2026.findings-eacl.76.pdf)"
      }
    ],
    "totalDurationMs": 171769,
    "totalTokens": 27674,
    "totalToolUseCount": 14,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1028,
      "cache_read_input_tokens": 22605,
      "output_tokens": 4040,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1028
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4040,
          "cache_read_input_tokens": 22605,
          "cache_creation_input_tokens": 1028,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1028,
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
      "otherToolCount": 14
    }
  },
  "sourceToolAssistantUUID": "35646cf2-27d7-4e8f-af2d-8e824bd1fd9e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Symbolic Pre-Filtering for Compute-Efficient Best-of-N Verification: A…",
  "leafUuid": "e49e32a8-6813-4542-ad24-c4508f083caa",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Quantifying symbolic-neural verifier complementarity in best-of-N reasoning",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b"
}
```

---

### Tool result

_source line 20 · 2026-05-10T18:13:25.019Z_

<details><summary>↩ Tool result · `toolu_01G4gtCmyi9Kr1VMxo5CzPE2`</summary>

```text
I now have comprehensive data from all the key sources. Let me compile the findings.

---

## Comprehensive Analysis: Error Distributions in LLM Mathematical Reasoning

### 1. arXiv 2502.19361 -- "Can Large Language Models Detect Errors in Long Chain-of-Thought Reasoning?" (DeltaBench)

This is the paper your reviewer cited. It introduces **DeltaBench**, the first benchmark for evaluating error detection in long CoT reasoning from o1-like models (QwQ, DeepSeek-R1, Gemini 2.0 Flash Thinking).

**The 15.4% figure confirmed**: In the math domain, the error distribution is:
- **Reasoning Error: 25.3%** (the dominant category)
- **Understanding Error: 15.7%**
- **Calculation Error: 15.4%** (this is what the reviewer cited)
- Remaining ~43.6% spread across other categories (strategy errors, knowledge errors, formal errors, etc.)

**Critical finding for your proposal**: Calculation errors are real but represent only about **1 in 6** of all math errors. Reasoning errors are nearly **twice as common**.

**Verifier performance data** (this is directly relevant to your symbolic checker argument):
- The best critic model (GPT-4-turbo-128k) achieves only **F1 = 40.76%** overall for error detection
- The best PRM (Qwen2.5-Math-PRM-7B) achieves only **F1 = 29.22%**
- **Crucially: "Most models demonstrate the highest accuracy in recognizing calculation errors"** while **"recognition of strategy errors is generally the weakest."**
- DeepSeek-V3 achieves ~36% F1 on calculation errors but drops to ~23% F1 on strategy errors

This means **calculation errors are already the easiest type for neural verifiers to detect**, and strategy/reasoning errors are the hardest.

**Model-specific error profiles**:
- DeepSeek-R1: Only 3.1% calculation errors (very low), 22.7% reasoning errors
- QwQ-32B-Preview: 17.9% calculation errors (high), relatively weaker fundamentals
- The stronger the reasoning model, the fewer calculation errors remain

Sources:
- [DeltaBench paper](https://arxiv.org/abs/2502.19361)
- [DeltaBench HTML](https://arxiv.org/html/2502.19361)

---

### 2. Yin, Sun et al. (EMNLP 2025 Findings) -- "Error Classification of LLMs on Math Word Problems"

**Dataset**: MWPES-300K, containing 304,865 error samples from 15 LLMs across 4 datasets (SVAMP, GSM8K, MATH, AQuA).

**Error evolution with model scaling** (critical for your hypotheses):
- As models scale up within a family (e.g., Llama-3.1-8B to 405B), "Misunderstanding of problem requirements" drops from **13.56% to 8.58%**
- Stronger models (GPT-4o, o1-mini) show *emergence of new error types* like "boundary condition" errors (2.33%) -- errors shift from basic to sophisticated
- o1-mini reduces "misunderstanding" errors to **4.83%** vs GPT-3.5-turbo's 11.93%
- **Key insight**: "Error patterns evolve from basic to complex manifestations as model capabilities increase." Stronger models don't just make fewer errors -- they make *different* errors, and these tend to be reasoning/strategy errors rather than arithmetic ones.

Source: [ACL Anthology](https://aclanthology.org/2025.findings-emnlp.20/)

---

### 3. ErrorMap and ErrorAtlas (arXiv 2601.15812)

Built from 83 LLMs across 35 datasets. **17 top-level error categories**.

**Overall prevalence across all tasks**:
- Missing Required Element: 15.56%
- Specification Misinterpretation: 11.50%
- Logical Reasoning Error: 9.09%
- Incorrect Identification: 8.98%
- **Computation Error: 8.45%**

**On reasoning-heavy benchmarks** (MMLU-Pro, Omni-MATH, GPQA): approximately **44% of errors have "weak reasoning orientation"** -- they manifest as technical issues (computation error, missing elements, counting) rather than deep reasoning failures. This might seem to support symbolic checking, but note that "missing required element" and "counting error" are not the same as simple arithmetic.

**MMLU-Pro breakdown** (ErrorMap vs manual annotation):
- Logical Reasoning Error: 44% (manual: 39%)
- Mathematical Mistake: 24% (manual: 12%)
- Factual Error: 12% (manual: 35%)

**Model comparison**: Gemini 1.5 Pro makes "significantly less computation and incomplete reasoning errors" than Gemini 1.5 Flash, confirming that scaling reduces computation errors preferentially.

Source: [ErrorAtlas paper](https://arxiv.org/abs/2601.15812)

---

### 4. Zhang & Graf (AIME-Con 2025) -- "Mathematical Computation and Reasoning Errors by Large Language Models"

Evaluated GPT-4o, o1, DeepSeek-V3, DeepSeek-R1 on three task types (5-digit multiplication, algebraic word problems, Diophantine equations).

**Four-category taxonomy**: Conditionally Correct, Procedural Error, Conceptual Error, Impasse Error.

**Key findings**:
- **"Procedural slips were the most frequent error type and significantly impacted overall performance, while conceptual misunderstandings were less frequent."**
- GPT-4o: most frequent PE (procedural errors), scoring 2/30 on multiplication and 8/30 on Diophantine equations
- o1: **flawless accuracy** on multiplication, near-perfect overall -- demonstrating that reasoning-enhanced models essentially eliminate procedural/arithmetic errors
- DeepSeek-R1 paradoxically underperformed DeepSeek-V3 due to "overthinking" -- excessive reflection caused critical component omission (a *reasoning* failure, not arithmetic)
- o1 achieves kappa = 0.737 (substantial agreement) with human coders; GPT-4o only kappa = 0.366

**Implication**: For frontier reasoning models (o1-class), procedural/arithmetic errors are essentially solved. The residual errors are conceptual.

Source: [Zhang & Graf AIME-Con](https://arxiv.org/html/2508.09932v2)

---

### 5. arXiv 2502.11574 -- "Large Language Models and Mathematical Reasoning Failures"

50 high-school word problems across 8 models.

**Results by model capability**:
| Model | Correct |
|-------|---------|
| Mixtral 8x7B | 0/50 |
| Llama 3.3-70B | 10/50 |
| GPT-4o | 14/50 |
| o1 | 37/50 |
| o3-mini | 40/50 |

**Hardest error types**: Spatial reasoning (universally failed), strategic planning, and physics-to-math translation. These are categorically beyond what any symbolic arithmetic checker can help with.

**False positives**: 21 questions (5%) had correct final answers but flawed reasoning -- highlighting that outcome-only verification misses reasoning errors.

Source: [arXiv 2502.11574](https://arxiv.org/abs/2502.11574)

---

### 6. Verifier Effectiveness Data (Cross-Source Synthesis)

**FoVer** (arXiv 2505.15960, ACL 2026 Findings): Trains PRMs on formally verified data from Z3/Isabelle. Shows cross-task generalization but does not report per-error-type detection rates.

**MATH-VF** (Step-Wise Formal Verification, arXiv 2505.20869): Achieves 93.2-95.7% step-verification accuracy on MATH500 using SymPy + Z3. But acknowledges it **"can only assess the correctness of each step...without analyzing the effectiveness of each step"** -- it catches whether a step is locally valid but not whether the strategy is sound.

**PRM performance** (from DeltaBench): PRMs reduce trace error rates from 14.0% to 3.4%, but this is on step-level correctness, not strategy-level reasoning.

Sources: [FoVer](https://fover-prm.github.io/), [MATH-VF](https://arxiv.org/html/2505.20869v1)

---

### 7. Additional Error Distribution Data

From other search results, one study categorized errors as: Symbol Confusion, Step Omission, Arithmetic, and Logic Hallucination, with **"logic hallucinations dominating and accounting for roughly three-fifths (~60%) of all wrong answers."**

From GSM-Ranges (arXiv 2502.08680): On Level 6 perturbations, o3-mini has **0% non-logical (arithmetic) errors** but still 4% logical errors. GPT-4o has 5.2% non-logical and 5.3% logical errors. Weaker models like Llama 3.2-3B: 68.8% non-logical errors. This demonstrates the **error type crossover**: as models improve, arithmetic errors vanish first, leaving reasoning errors as the residual.

Source: [GSM-Ranges](https://arxiv.org/abs/2502.08680)

---

## Synthesis: Implications for Your Symbolic Verification Proposal

Here are the key takeaways for recalibrating your hypotheses:

**1. The ceiling on symbolic arithmetic checking is low and model-dependent.**
- For frontier reasoning models (o1, o3-mini, DeepSeek-R1), calculation errors are already 3-5% of all errors. A perfect symbolic checker would address at most this fraction.
- For weaker models, calculation errors are more prevalent (~15-18%), but these models also make so many other errors that the marginal improvement is small relative to the total error rate.

**2. Calculation errors are already the easiest for neural verifiers to detect.**
DeltaBench explicitly shows verifiers achieve their *highest* accuracy on calculation errors and their *lowest* on strategy errors. A symbolic checker competes in the space where neural methods are already strongest.

**3. The error distribution shifts with capability -- against your approach.**
The consistent finding across all papers is: as models scale up, arithmetic errors decrease faster than reasoning errors. The residual errors in frontier models are predominantly reasoning/strategy/conceptual -- exactly the types a symbolic checker cannot address.

**4. Formal verification has a narrow but real niche.**
MATH-VF shows 93%+ accuracy for step-level correctness verification, but explicitly cannot evaluate strategy soundness. It complements rather than replaces reasoning verification. The value proposition is strongest for: (a) catching procedural errors in weaker models, (b) providing certified step-level correctness as a building block.

**5. The real verification gap is in strategy and reasoning errors.**
Across all sources, strategy errors have the lowest detection rates (F1 ~23% in DeltaBench), and these are the dominant error type in strong models. This is where the field needs innovation.

**Recommended framing for your revised proposal**: Rather than claiming symbolic verification addresses a large fraction of math errors, position it as: (a) providing *certified* correctness for the arithmetic layer, which neural verifiers cannot guarantee even when they often detect such errors, and (b) freeing neural verification capacity to focus on the harder reasoning/strategy errors where current methods are weakest (F1 ~23%). The value is in certification and complementarity, not in coverage percentage.

agentId: a2a99f3df2827afd3 (use SendMessage with to: 'a2a99f3df2827afd3' to continue this agent)
&lt;usage>total_tokens: 35084
tool_uses: 26
duration_ms: 223968&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6f9bff96-38e0-4fe4-baae-698d4fea7397",
  "isSidechain": false,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "type": "user",
  "uuid": "bbd3cb70-cde0-4a02-b16d-a32fe5cfa173",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm revising a research proposal about symbolic verification for math reasoning. A reviewer cited arXiv 2502.19361 showing calculation errors are only ~15.4% of errors. I need to deeply understand error distributions in LLM mathematical reasoning.\n\nPlease do the following:\n1. Use WebSearch to find arXiv 2502.19361 (about mathematical reasoning errors, logical and arithmetic errors) and use WebFetch to read its abstract and key findings\n2. Search for \"Sun et al EMNLP 2025 error taxonomy LLM mathematical reasoning 39 category\" and fetch the paper\n3. Search for \"ErrorAtlas error taxonomy language model\" and fetch details\n4. Search for \"Zhang Graf AIME-Con 2025 error categorization\" \n5. Search for \"LLM mathematical reasoning error distribution calculation vs reasoning 2025 2026\"\n6. Search for \"model scaling error type shift computational reasoning failures\"\n\nFor each source, I need:\n- The actual error type percentages (especially: what % are calculation/arithmetic errors vs reasoning/strategy errors)\n- How error distributions change with model capability\n- Whether neural verifiers are already good at catching calculation errors\n- Any evidence about what types of errors are hardest to catch\n\nThis is critical for recalibrating my hypotheses about how much a symbolic checker can actually help.",
    "agentId": "a2a99f3df2827afd3",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive data from all the key sources. Let me compile the findings.\n\n---\n\n## Comprehensive Analysis: Error Distributions in LLM Mathematical Reasoning\n\n### 1. arXiv 2502.19361 -- \"Can Large Language Models Detect Errors in Long Chain-of-Thought Reasoning?\" (DeltaBench)\n\nThis is the paper your reviewer cited. It introduces **DeltaBench**, the first benchmark for evaluating error detection in long CoT reasoning from o1-like models (QwQ, DeepSeek-R1, Gemini 2.0 Flash Thinking).\n\n**The 15.4% figure confirmed**: In the math domain, the error distribution is:\n- **Reasoning Error: 25.3%** (the dominant category)\n- **Understanding Error: 15.7%**\n- **Calculation Error: 15.4%** (this is what the reviewer cited)\n- Remaining ~43.6% spread across other categories (strategy errors, knowledge errors, formal errors, etc.)\n\n**Critical finding for your proposal**: Calculation errors are real but represent only about **1 in 6** of all math errors. Reasoning errors are nearly **twice as common**.\n\n**Verifier performance data** (this is directly relevant to your symbolic checker argument):\n- The best critic model (GPT-4-turbo-128k) achieves only **F1 = 40.76%** overall for error detection\n- The best PRM (Qwen2.5-Math-PRM-7B) achieves only **F1 = 29.22%**\n- **Crucially: \"Most models demonstrate the highest accuracy in recognizing calculation errors\"** while **\"recognition of strategy errors is generally the weakest.\"**\n- DeepSeek-V3 achieves ~36% F1 on calculation errors but drops to ~23% F1 on strategy errors\n\nThis means **calculation errors are already the easiest type for neural verifiers to detect**, and strategy/reasoning errors are the hardest.\n\n**Model-specific error profiles**:\n- DeepSeek-R1: Only 3.1% calculation errors (very low), 22.7% reasoning errors\n- QwQ-32B-Preview: 17.9% calculation errors (high), relatively weaker fundamentals\n- The stronger the reasoning model, the fewer calculation errors remain\n\nSources:\n- [DeltaBench paper](https://arxiv.org/abs/2502.19361)\n- [DeltaBench HTML](https://arxiv.org/html/2502.19361)\n\n---\n\n### 2. Yin, Sun et al. (EMNLP 2025 Findings) -- \"Error Classification of LLMs on Math Word Problems\"\n\n**Dataset**: MWPES-300K, containing 304,865 error samples from 15 LLMs across 4 datasets (SVAMP, GSM8K, MATH, AQuA).\n\n**Error evolution with model scaling** (critical for your hypotheses):\n- As models scale up within a family (e.g., Llama-3.1-8B to 405B), \"Misunderstanding of problem requirements\" drops from **13.56% to 8.58%**\n- Stronger models (GPT-4o, o1-mini) show *emergence of new error types* like \"boundary condition\" errors (2.33%) -- errors shift from basic to sophisticated\n- o1-mini reduces \"misunderstanding\" errors to **4.83%** vs GPT-3.5-turbo's 11.93%\n- **Key insight**: \"Error patterns evolve from basic to complex manifestations as model capabilities increase.\" Stronger models don't just make fewer errors -- they make *different* errors, and these tend to be reasoning/strategy errors rather than arithmetic ones.\n\nSource: [ACL Anthology](https://aclanthology.org/2025.findings-emnlp.20/)\n\n---\n\n### 3. ErrorMap and ErrorAtlas (arXiv 2601.15812)\n\nBuilt from 83 LLMs across 35 datasets. **17 top-level error categories**.\n\n**Overall prevalence across all tasks**:\n- Missing Required Element: 15.56%\n- Specification Misinterpretation: 11.50%\n- Logical Reasoning Error: 9.09%\n- Incorrect Identification: 8.98%\n- **Computation Error: 8.45%**\n\n**On reasoning-heavy benchmarks** (MMLU-Pro, Omni-MATH, GPQA): approximately **44% of errors have \"weak reasoning orientation\"** -- they manifest as technical issues (computation error, missing elements, counting) rather than deep reasoning failures. This might seem to support symbolic checking, but note that \"missing required element\" and \"counting error\" are not the same as simple arithmetic.\n\n**MMLU-Pro breakdown** (ErrorMap vs manual annotation):\n- Logical Reasoning Error: 44% (manual: 39%)\n- Mathematical Mistake: 24% (manual: 12%)\n- Factual Error: 12% (manual: 35%)\n\n**Model comparison**: Gemini 1.5 Pro makes \"significantly less computation and incomplete reasoning errors\" than Gemini 1.5 Flash, confirming that scaling reduces computation errors preferentially.\n\nSource: [ErrorAtlas paper](https://arxiv.org/abs/2601.15812)\n\n---\n\n### 4. Zhang & Graf (AIME-Con 2025) -- \"Mathematical Computation and Reasoning Errors by Large Language Models\"\n\nEvaluated GPT-4o, o1, DeepSeek-V3, DeepSeek-R1 on three task types (5-digit multiplication, algebraic word problems, Diophantine equations).\n\n**Four-category taxonomy**: Conditionally Correct, Procedural Error, Conceptual Error, Impasse Error.\n\n**Key findings**:\n- **\"Procedural slips were the most frequent error type and significantly impacted overall performance, while conceptual misunderstandings were less frequent.\"**\n- GPT-4o: most frequent PE (procedural errors), scoring 2/30 on multiplication and 8/30 on Diophantine equations\n- o1: **flawless accuracy** on multiplication, near-perfect overall -- demonstrating that reasoning-enhanced models essentially eliminate procedural/arithmetic errors\n- DeepSeek-R1 paradoxically underperformed DeepSeek-V3 due to \"overthinking\" -- excessive reflection caused critical component omission (a *reasoning* failure, not arithmetic)\n- o1 achieves kappa = 0.737 (substantial agreement) with human coders; GPT-4o only kappa = 0.366\n\n**Implication**: For frontier reasoning models (o1-class), procedural/arithmetic errors are essentially solved. The residual errors are conceptual.\n\nSource: [Zhang & Graf AIME-Con](https://arxiv.org/html/2508.09932v2)\n\n---\n\n### 5. arXiv 2502.11574 -- \"Large Language Models and Mathematical Reasoning Failures\"\n\n50 high-school word problems across 8 models.\n\n**Results by model capability**:\n| Model | Correct |\n|-------|---------|\n| Mixtral 8x7B | 0/50 |\n| Llama 3.3-70B | 10/50 |\n| GPT-4o | 14/50 |\n| o1 | 37/50 |\n| o3-mini | 40/50 |\n\n**Hardest error types**: Spatial reasoning (universally failed), strategic planning, and physics-to-math translation. These are categorically beyond what any symbolic arithmetic checker can help with.\n\n**False positives**: 21 questions (5%) had correct final answers but flawed reasoning -- highlighting that outcome-only verification misses reasoning errors.\n\nSource: [arXiv 2502.11574](https://arxiv.org/abs/2502.11574)\n\n---\n\n### 6. Verifier Effectiveness Data (Cross-Source Synthesis)\n\n**FoVer** (arXiv 2505.15960, ACL 2026 Findings): Trains PRMs on formally verified data from Z3/Isabelle. Shows cross-task generalization but does not report per-error-type detection rates.\n\n**MATH-VF** (Step-Wise Formal Verification, arXiv 2505.20869): Achieves 93.2-95.7% step-verification accuracy on MATH500 using SymPy + Z3. But acknowledges it **\"can only assess the correctness of each step...without analyzing the effectiveness of each step\"** -- it catches whether a step is locally valid but not whether the strategy is sound.\n\n**PRM performance** (from DeltaBench): PRMs reduce trace error rates from 14.0% to 3.4%, but this is on step-level correctness, not strategy-level reasoning.\n\nSources: [FoVer](https://fover-prm.github.io/), [MATH-VF](https://arxiv.org/html/2505.20869v1)\n\n---\n\n### 7. Additional Error Distribution Data\n\nFrom other search results, one study categorized errors as: Symbol Confusion, Step Omission, Arithmetic, and Logic Hallucination, with **\"logic hallucinations dominating and accounting for roughly three-fifths (~60%) of all wrong answers.\"**\n\nFrom GSM-Ranges (arXiv 2502.08680): On Level 6 perturbations, o3-mini has **0% non-logical (arithmetic) errors** but still 4% logical errors. GPT-4o has 5.2% non-logical and 5.3% logical errors. Weaker models like Llama 3.2-3B: 68.8% non-logical errors. This demonstrates the **error type crossover**: as models improve, arithmetic errors vanish first, leaving reasoning errors as the residual.\n\nSource: [GSM-Ranges](https://arxiv.org/abs/2502.08680)\n\n---\n\n## Synthesis: Implications for Your Symbolic Verification Proposal\n\nHere are the key takeaways for recalibrating your hypotheses:\n\n**1. The ceiling on symbolic arithmetic checking is low and model-dependent.**\n- For frontier reasoning models (o1, o3-mini, DeepSeek-R1), calculation errors are already 3-5% of all errors. A perfect symbolic checker would address at most this fraction.\n- For weaker models, calculation errors are more prevalent (~15-18%), but these models also make so many other errors that the marginal improvement is small relative to the total error rate.\n\n**2. Calculation errors are already the easiest for neural verifiers to detect.**\nDeltaBench explicitly shows verifiers achieve their *highest* accuracy on calculation errors and their *lowest* on strategy errors. A symbolic checker competes in the space where neural methods are already strongest.\n\n**3. The error distribution shifts with capability -- against your approach.**\nThe consistent finding across all papers is: as models scale up, arithmetic errors decrease faster than reasoning errors. The residual errors in frontier models are predominantly reasoning/strategy/conceptual -- exactly the types a symbolic checker cannot address.\n\n**4. Formal verification has a narrow but real niche.**\nMATH-VF shows 93%+ accuracy for step-level correctness verification, but explicitly cannot evaluate strategy soundness. It complements rather than replaces reasoning verification. The value proposition is strongest for: (a) catching procedural errors in weaker models, (b) providing certified step-level correctness as a building block.\n\n**5. The real verification gap is in strategy and reasoning errors.**\nAcross all sources, strategy errors have the lowest detection rates (F1 ~23% in DeltaBench), and these are the dominant error type in strong models. This is where the field needs innovation.\n\n**Recommended framing for your revised proposal**: Rather than claiming symbolic verification addresses a large fraction of math errors, position it as: (a) providing *certified* correctness for the arithmetic layer, which neural verifiers cannot guarantee even when they often detect such errors, and (b) freeing neural verification capacity to focus on the harder reasoning/strategy errors where current methods are weakest (F1 ~23%). The value is in certification and complementarity, not in coverage percentage."
      }
    ],
    "totalDurationMs": 223968,
    "totalTokens": 35084,
    "totalToolUseCount": 26,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 567,
      "cache_read_input_tokens": 31643,
      "output_tokens": 2873,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 567
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2873,
          "cache_read_input_tokens": 31643,
          "cache_creation_input_tokens": 567,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 567,
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
      "otherToolCount": 26
    }
  },
  "sourceToolAssistantUUID": "6f9bff96-38e0-4fe4-baae-698d4fea7397",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T18:13:50.205Z_

<details><summary>↩ Tool result · `toolu_01Wr8exWq564ra2gqCKL6p8e`</summary>

```text
Now I have comprehensive information. Let me compile the full landscape analysis.

---

Here is the full landscape of code-execution-based verification approaches relevant to your research proposal on symbolic pre-filtering for best-of-N verification in mathematical reasoning.

---

## 1. CORE PAPER: T3RL (Tool Verification for Test-Time Reinforcement Learning)

- **Title:** Tool Verification for Test-Time Reinforcement Learning
- **Authors:** Ruotong Liao, Nikolai Rohrich, Xiaohan Wang, Yuhui Zhang, Yasaman Samadzadeh, Volker Tresp, Serena Yeung-Levy
- **Date/Venue:** arXiv:2603.02203, March 2, 2026
- **Core method:** T3RL addresses a critical failure mode in TTRL (test-time reinforcement learning) where spurious high-frequency consensus among sampled rollouts creates biased reward signals leading to incorrect mode collapse. The system compiles each rollout's claimed computations into lightweight Python code, queries a code interpreter to obtain executable evidence, and then an LLM verifier uses the execution result to upweight verified rollouts in a "verification-aware voting" scheme. This produces more reliable pseudo-labels for self-training.
- **Relation to best-of-N:** Directly replaces naive majority voting in best-of-N with verification-aware weighted voting. The code execution acts as a symbolic pre-filter that distinguishes genuinely correct solutions from plausible-looking but wrong ones that happen to be frequent.
- **Key results:** Improvements over TTRL across MATH-500, AMC, and AIME 2024, with larger gains on harder problems (exact numbers not in abstract).

**Sources:**
- [T3RL on arXiv](https://arxiv.org/abs/2603.02203)
- [T3RL on HuggingFace Papers](https://huggingface.co/papers/2603.02203)

---

## 2. FOUNDATIONAL WORKS: Code-Execution for Reasoning

### PAL: Program-Aided Language Models
- **Title:** PAL: Program-aided Language Models
- **Authors:** Luyu Gao, Aman Madaan, Shuyan Zhou, Uri Alon, Pengfei Liu, Yiming Yang, Jamie Callan, Graham Neubig
- **Date/Venue:** arXiv:2211.10435, ICML 2023
- **Core method:** Instead of having the LLM solve math problems end-to-end in natural language, PAL has the LLM decompose the problem into a Python program and delegates actual computation to a Python interpreter. The LLM focuses on semantic understanding and program structure; the interpreter provides guaranteed-correct arithmetic.
- **Relation to best-of-N:** PAL establishes the foundational insight that code execution provides a deterministic verification channel. In a best-of-N setting, solutions that produce executable code with correct outputs can be trivially verified, while prose-only reasoning cannot.
- **Key results:** 72.0% on GSM8K (top-1, surpassing PaLM-540B CoT by 15% absolute), 61.2% on GSM-Hard. Demonstrated across 12 BIG-Bench Hard tasks.

**Source:** [PAL on arXiv](https://arxiv.org/abs/2211.10435)

### ToRA: Tool-Integrated Reasoning Agent
- **Title:** ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving
- **Authors:** Zhibin Gou, Zhihong Shao, Yeyun Gong, et al. (Microsoft Research)
- **Date/Venue:** arXiv:2309.17452, ICLR 2024
- **Core method:** ToRA interleaves natural language reasoning with programmatic tool use (computation libraries, symbolic solvers) in a unified format. Models are trained via imitation learning on interactive tool-use trajectories, followed by output space shaping to refine reasoning behavior. The method achieves fast inference averaging only 1.02 tool interaction rounds per problem.
- **Relation to best-of-N:** ToRA's interleaved format means each candidate solution contains executable code segments whose outputs can be checked, providing a natural verification signal for selection among candidates.
- **Key results:** ToRA-7B reaches 44.6% on MATH (surpassing WizardMath-70B by 22% absolute). ToRA-Code-34B exceeds 50% on MATH, competitive with GPT-4. 13-19% absolute improvements over open-source baselines across 10 math datasets.

**Source:** [ToRA on arXiv](https://arxiv.org/abs/2309.17452)

### MathCoder: Seamless Code Integration in LLMs
- **Title:** MathCoder: Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning
- **Authors:** Ke Wang, Houxing Ren, Aojun Zhou, Zimu Lu, et al.
- **Date/Venue:** arXiv:2310.03731, October 2023
- **Core method:** Fine-tunes open-source LLMs on MathCodeInstruct, a dataset where each solution interleaves natural language, executable code, and code execution results. Inspired by GPT-4 Code Interpreter's seamless reasoning-code-execution loop.
- **Relation to best-of-N:** Each generated solution contains embedded code that can be re-executed for verification. The interleaved format creates a trace where computational claims are checkable.
- **Key results:** 45.2% on MATH, 83.9% on GSM8K. Surpasses ChatGPT-3.5 and PaLM-2; competitive with GPT-4 on MATH.

**Source:** [MathCoder on arXiv](https://arxiv.org/abs/2310.03731)

---

## 3. CODE-EXECUTION-BASED VERIFICATION SYSTEMS

### SymCode: Neurosymbolic Verifiable Code Generation
- **Title:** SymCode: A Neurosymbolic Approach to Mathematical Reasoning via Verifiable Code Generation
- **Authors:** Sina Bagheri Nezhad, Yao Li, Ameeta Agrawal
- **Date/Venue:** arXiv:2510.25975, EACL 2026 Findings
- **Core method:** Reframes mathematical problem-solving as verifiable SymPy code generation. The LLM translates a natural language problem into an executable Python/SymPy script, which is then iteratively refined through a self-debugging loop using deterministic interpreter feedback. Training-free -- works purely through structured prompting.
- **Relation to best-of-N:** Highly relevant. SymCode shifts model failures from opaque logical fallacies to transparent, programmatic errors. In a best-of-N setting, candidates that execute successfully and produce consistent symbolic outputs can be verified deterministically. The self-debugging loop is itself a form of iterative verification.
- **Key results:** Up to 13.6 percentage points improvement (16.8 with SymCode+) over CoT baselines on MATH-500, OlympiadBench, and AIME, with gains increasing on harder problems.

**Source:** [SymCode on arXiv](https://arxiv.org/abs/2510.25975)

### HERMES: Efficient and Verifiable Mathematical Reasoning
- **Title:** HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs
- **Authors:** Azim Ospanov, Zijin Feng, Jiacheng Sun, Haoli Bai, Xin Shen, Farzan Farnia
- **Date/Venue:** arXiv:2511.18760, November 2025
- **Core method:** The first tool-assisted agent that explicitly interleaves informal reasoning with formally verified proof steps in Lean. Uses intermediate formal checking to prevent reasoning drift and employs a memory module for proof continuity across long multi-step chains. Combines exploratory informal reasoning with the rigor of formal theorem-proving verification.
- **Relation to best-of-N:** Uses formal verification (Lean compiler) rather than code execution, but addresses the same core problem: verifying correctness of candidate solutions. HERMES shows that symbolic verification can dramatically reduce the number of candidates needed by filtering out incorrect reasoning early.
- **Key results:** Up to 67% accuracy improvement on AIME'25 while using 80% fewer total inference FLOPs compared to reward-based approaches.

**Source:** [HERMES on arXiv](https://arxiv.org/abs/2511.18760)

### DeepSeekMath-V2: Self-Verifiable Mathematical Reasoning
- **Title:** DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning
- **Authors:** Zhihong Shao et al. (DeepSeek)
- **Date/Venue:** arXiv:2511.22570, November 2025
- **Core method:** Trains an LLM-based verifier for theorem proving, then trains a generator using the verifier as a reward model. Critically introduces a meta-verifier that evaluates the verifier's own analyses, reducing hallucinated errors. The generator is incentivized to self-identify and resolve issues in its proofs before finalizing them.
- **Relation to best-of-N:** The self-verification paradigm means each candidate can be scored by the model's own verification module. The meta-verifier addresses the key failure mode in verification-guided best-of-N: the verifier itself being unreliable. Analysis quality improves from 0.85 to 0.96 with the meta-verifier.
- **Key results:** Gold-level on IMO 2025 and CMO 2024; 118/120 on Putnam 2024 with scaled test-time compute.

**Source:** [DeepSeekMath-V2 on arXiv](https://arxiv.org/abs/2511.22570)

---

## 4. PROCESS REWARD MODELS WITH CODE VERIFICATION

### GenPRM: Generative PRM with Code Verification
- **Title:** GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning
- **Authors:** Jian Zhao, Runze Liu, Kaiyan Zhang, et al.
- **Date/Venue:** arXiv:2504.00891, AAAI 2026
- **Core method:** Redefines process supervision as a generative task. GenPRM performs explicit Chain-of-Thought reasoning with code verification before judging each reasoning step. Uses Relative Progress Estimation (RPE) and a rationale synthesis framework incorporating code verification for training data. Trained on only 23K examples from MATH.
- **Relation to best-of-N:** Directly applicable as a verifier for best-of-N selection. The code verification component provides a deterministic signal within the generative PRM framework. GenPRM can rank candidates by verified step-level correctness.
- **Key results:** 1.5B GenPRM outperforms GPT-4o on ProcessBench; 7B GenPRM surpasses Qwen2.5-Math-PRM-72B (a 10x larger discriminative PRM).

**Source:** [GenPRM on arXiv](https://arxiv.org/abs/2504.00891)

### CodePRM: Execution Feedback-Enhanced Process Reward Model
- **Title:** CodePRM: Execution Feedback-enhanced Process Reward Model for Code Generation
- **Authors:** (ACL 2025 Findings)
- **Date/Venue:** ACL 2025 Findings
- **Core method:** Collects thought traces where each step is labeled with derived code pass rates from execution feedback. Trains a PRM that takes both the reasoning process and code execution feedback as input to score individual thought steps. Deployed in a Generate-Verify-Refine (GVR) pipeline.
- **Relation to best-of-N:** The GVR pipeline is essentially a refined best-of-N: generate candidates, verify each step using code execution feedback, and refine failing candidates. Code execution provides the ground-truth signal for step-level scoring.
- **Key results:** Outperforms strong baselines on code generation benchmarks.

**Source:** [CodePRM at ACL Anthology](https://aclanthology.org/2025.findings-acl.428/)

### CodeRM: Dynamic Scaling of Unit Tests for Reward Modeling
- **Title:** Dynamic Scaling of Unit Tests for Code Reward Modeling
- **Authors:** Zeyao Ma, Xiaokang Zhang, Jing Zhang, Jifan Yu, Sijia Luo, Jie Tang
- **Date/Venue:** ACL 2025 (Long Papers)
- **Core method:** Reveals a positive correlation between the number of unit tests and reward signal quality. Trains CodeRM-8B, a lightweight unit test generator, and employs dynamic scaling -- generating more unit tests for harder problems -- to improve verification quality.
- **Relation to best-of-N:** Directly addresses the quality of reward signals used in best-of-N selection via code execution. Shows that scaling the number of verification tests per candidate improves selection accuracy, especially for harder problems.
- **Key results:** 18.43% improvement for Llama3-8B and 3.42% for GPT-4o-mini on HumanEval Plus.

**Source:** [CodeRM on arXiv](https://arxiv.org/abs/2501.01054)

---

## 5. TEST-TIME SCALING AND VERIFICATION CONTEXT

### TTRL: Test-Time Reinforcement Learning (baseline for T3RL)
- **Title:** TTRL: Test-Time Reinforcement Learning
- **Authors:** (PRIME-RL team)
- **Date/Venue:** arXiv:2504.16084, NeurIPS 2025
- **Core method:** Uses majority voting among multiple sampled predictions to create pseudo-labels on unlabeled test data, then uses these as reward signals for RL training at test time. The key insight is that majority voting provides surprisingly effective rewards without ground-truth labels.
- **Relation to best-of-N:** TTRL is the direct predecessor to T3RL. It demonstrates that majority voting (a form of best-of-N) can drive self-improvement, but is vulnerable to "spurious signal amplification" where frequent-but-wrong answers dominate. T3RL fixes this with code-execution verification.
- **Key results:** Boosts Qwen-2.5-Math-7B pass@1 by ~211% on AIME 2024 with only unlabeled test data.

**Source:** [TTRL on arXiv](https://arxiv.org/abs/2504.16084)

### Snell et al.: Scaling LLM Test-Time Compute
- **Title:** Scaling LLM Test-Time Compute Optimally Can Be More Effective than Scaling Model Parameters
- **Authors:** Charlie Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar
- **Date/Venue:** arXiv:2408.03314, ICLR 2025 (Oral)
- **Core method:** Analyzes two mechanisms for scaling test-time compute: (1) searching against process-based verifier reward models (PRMs) and (2) adaptively updating the model's response distribution. Introduces compute-optimal strategies that adaptively allocate test-time compute per prompt.
- **Relation to best-of-N:** Establishes the theoretical framework for best-of-N with verification. Shows compute-optimal strategies improve efficiency 2-4x over naive best-of-N. The quality of the verifier is the key bottleneck -- directly motivating symbolic/code-based verification as a stronger signal.
- **Key results:** Compute-optimal test-time scaling can match the performance of a 14x larger model on certain prompts.

**Source:** [Snell et al. on arXiv](https://arxiv.org/abs/2408.03314)

### Scoring Verifiers: Evaluating Synthetic Verification
- **Title:** Scoring Verifiers: Evaluating Synthetic Verification for Code and Reasoning
- **Authors:** Aleksander Ficek, Somshubra Majumdar, Vahid Noroozi, Boris Ginsburg
- **Date/Venue:** arXiv:2502.13820, COLM 2025
- **Core method:** Proposes benchmarks and metrics to evaluate synthetic verifiers (test case generators, reward models) for code and reasoning tasks. Releases HE-R, HE-R+, MBPP-R, MBPP-R+ benchmarks for scoring and ranking candidate solutions.
- **Relation to best-of-N:** Directly evaluates the ranking quality of different verification methods for selecting among candidates. Shows that reasoning-enhanced models substantially improve test case generation quality, and scaling the number of test cases improves verification accuracy.
- **Key results:** Reasoning models significantly improve synthetic verification quality; more test cases yield better ranking accuracy.

**Source:** [Scoring Verifiers on arXiv](https://arxiv.org/abs/2502.13820)

---

## 6. ADDITIONAL RELATED WORK

### ExecVerify: White-Box RL with Verifiable Stepwise Rewards
- **Title:** ExecVerify: White-Box RL with Verifiable Stepwise Rewards for Code Execution Reasoning
- **Authors:** Lingxiao Tang, He Ye, et al. (Zhejiang University, UCL)
- **Date/Venue:** arXiv:2603.11226, March 2026
- **Core method:** Derives verifiable white-box rewards from execution traces (next-statement prediction, variable value/type prediction). Uses a two-stage training pipeline: first enhances execution reasoning, then transfers to code generation. Note: this paper focuses on code execution reasoning rather than mathematical reasoning specifically.
- **Relation to best-of-N:** Demonstrates that execution traces can provide reliable step-level verification signals, which could be applied to verify mathematical reasoning steps that are expressed as code.
- **Key results:** 7B model matches 32B models on code reasoning benchmarks; up to 5.9% pass@1 improvement on code generation.

**Source:** [ExecVerify on arXiv](https://arxiv.org/abs/2603.11226)

### Agentic Code Reasoning
- **Title:** Agentic Code Reasoning
- **Authors:** Shubham Ugare, Satish Chandra (Meta)
- **Date/Venue:** arXiv:2603.01896, March 2026
- **Core method:** Introduces "semi-formal reasoning" -- structured prompting that requires agents to construct explicit premises, trace execution paths, and derive formal conclusions. Acts as a certificate that prevents the agent from skipping cases or making unsupported claims.
- **Relation to best-of-N:** Demonstrates that structured code reasoning without execution can still serve as verification. The semi-formal certificates provide verifiable traces that could be used to filter/rank candidates in a best-of-N setting.
- **Key results:** Accuracy improves from 78% to 88% on patch equivalence verification; 87% on RubberDuckBench (9 point gain).

**Source:** [Agentic Code Reasoning on arXiv](https://arxiv.org/abs/2603.01896)

---

## SYNTHESIS: The Landscape

The field can be organized along two axes:

**Axis 1 -- What is verified:**
- Final answer only (majority voting, ORM)
- Step-level process (PRM, GenPRM, CodePRM)
- Full symbolic trace (PAL, SymCode, HERMES, T3RL)

**Axis 2 -- How verification is performed:**
- Neural/learned verifiers (PRM, ORM, ThinkPRM)
- Code execution against test cases (PAL, ToRA, MathCoder, CodeRM)
- Formal proof checking (HERMES via Lean, DeepSeekMath-V2)
- Hybrid: neural + code execution (T3RL, GenPRM, CodePRM)

T3RL sits at the intersection of step-level verification and hybrid neural+code execution, making it directly relevant to your symbolic pre-filtering proposal. The key gap it fills is using code execution not just for generating answers (as in PAL/ToRA) but specifically for filtering/reweighting candidates in the best-of-N selection process during test-time self-improvement.

The most important papers for your related work section are likely: T3RL, TTRL (as baseline), GenPRM (code-verified PRM), SymCode (neurosymbolic verification), HERMES (formal verification for efficiency), Snell et al. (compute-optimal best-of-N framework), and the foundational PAL/ToRA works.

Sources:
- [T3RL - arXiv:2603.02203](https://arxiv.org/abs/2603.02203)
- [TTRL - arXiv:2504.16084](https://arxiv.org/abs/2504.16084)
- [PAL - arXiv:2211.10435](https://arxiv.org/abs/2211.10435)
- [ToRA - arXiv:2309.17452](https://arxiv.org/abs/2309.17452)
- [MathCoder - arXiv:2310.03731](https://arxiv.org/abs/2310.03731)
- [SymCode - arXiv:2510.25975](https://arxiv.org/abs/2510.25975)
- [HERMES - arXiv:2511.18760](https://arxiv.org/abs/2511.18760)
- [DeepSeekMath-V2 - arXiv:2511.22570](https://arxiv.org/abs/2511.22570)
- [GenPRM - arXiv:2504.00891](https://arxiv.org/abs/2504.00891)
- [CodePRM - ACL 2025 Findings](https://aclanthology.org/2025.findings-acl.428/)
- [CodeRM - arXiv:2501.01054](https://arxiv.org/abs/2501.01054)
- [Snell et al. - arXiv:2408.03314](https://arxiv.org/abs/2408.03314)
- [Scoring Verifiers - arXiv:2502.13820](https://arxiv.org/abs/2502.13820)
- [ExecVerify - arXiv:2603.11226](https://arxiv.org/abs/2603.11226)
- [Agentic Code Reasoning - arXiv:2603.01896](https://arxiv.org/abs/2603.01896)

agentId: a40596f27d93c653d (use SendMessage with to: 'a40596f27d93c653d' to continue this agent)
&lt;usage>total_tokens: 40598
tool_uses: 29
duration_ms: 258653&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "41ea2268-9dc0-4d45-bf9d-cf4e6f1f7003",
  "isSidechain": false,
  "promptId": "69f1b1b5-9a23-4db7-a386-a90dcc391d95",
  "type": "user",
  "uuid": "d49c3a54-3e77-4481-8fde-1d7e065fc1ae",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm revising a research proposal about symbolic pre-filtering for best-of-N verification in mathematical reasoning. A reviewer pointed out I'm missing T3RL (arXiv 2603.02203, March 2026), which compiles reasoning traces into executable Python code for verification.\n\nPlease do the following:\n1. Use WebSearch to find T3RL (arXiv 2603.02203) and any related work on code-execution-based verification for test-time scaling\n2. Use WebFetch to read the T3RL paper abstract and method section from its arXiv page\n3. Search for \"code execution verification best-of-N mathematical reasoning 2025 2026\" to find other related works\n4. Search for \"PAL program-aided language models\" and \"ToRA tool-integrated reasoning\" to understand the foundational code-execution works\n\nFor each paper found, report:\n- Title, venue, date\n- Core method (2-3 sentences)\n- How it relates to using symbolic/code verification in best-of-N selection\n- Key results (accuracy numbers on MATH/AIME if available)\n\nBe thorough - I need to understand the full landscape of code-execution-based verification approaches.",
    "agentId": "a40596f27d93c653d",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information. Let me compile the full landscape analysis.\n\n---\n\nHere is the full landscape of code-execution-based verification approaches relevant to your research proposal on symbolic pre-filtering for best-of-N verification in mathematical reasoning.\n\n---\n\n## 1. CORE PAPER: T3RL (Tool Verification for Test-Time Reinforcement Learning)\n\n- **Title:** Tool Verification for Test-Time Reinforcement Learning\n- **Authors:** Ruotong Liao, Nikolai Rohrich, Xiaohan Wang, Yuhui Zhang, Yasaman Samadzadeh, Volker Tresp, Serena Yeung-Levy\n- **Date/Venue:** arXiv:2603.02203, March 2, 2026\n- **Core method:** T3RL addresses a critical failure mode in TTRL (test-time reinforcement learning) where spurious high-frequency consensus among sampled rollouts creates biased reward signals leading to incorrect mode collapse. The system compiles each rollout's claimed computations into lightweight Python code, queries a code interpreter to obtain executable evidence, and then an LLM verifier uses the execution result to upweight verified rollouts in a \"verification-aware voting\" scheme. This produces more reliable pseudo-labels for self-training.\n- **Relation to best-of-N:** Directly replaces naive majority voting in best-of-N with verification-aware weighted voting. The code execution acts as a symbolic pre-filter that distinguishes genuinely correct solutions from plausible-looking but wrong ones that happen to be frequent.\n- **Key results:** Improvements over TTRL across MATH-500, AMC, and AIME 2024, with larger gains on harder problems (exact numbers not in abstract).\n\n**Sources:**\n- [T3RL on arXiv](https://arxiv.org/abs/2603.02203)\n- [T3RL on HuggingFace Papers](https://huggingface.co/papers/2603.02203)\n\n---\n\n## 2. FOUNDATIONAL WORKS: Code-Execution for Reasoning\n\n### PAL: Program-Aided Language Models\n- **Title:** PAL: Program-aided Language Models\n- **Authors:** Luyu Gao, Aman Madaan, Shuyan Zhou, Uri Alon, Pengfei Liu, Yiming Yang, Jamie Callan, Graham Neubig\n- **Date/Venue:** arXiv:2211.10435, ICML 2023\n- **Core method:** Instead of having the LLM solve math problems end-to-end in natural language, PAL has the LLM decompose the problem into a Python program and delegates actual computation to a Python interpreter. The LLM focuses on semantic understanding and program structure; the interpreter provides guaranteed-correct arithmetic.\n- **Relation to best-of-N:** PAL establishes the foundational insight that code execution provides a deterministic verification channel. In a best-of-N setting, solutions that produce executable code with correct outputs can be trivially verified, while prose-only reasoning cannot.\n- **Key results:** 72.0% on GSM8K (top-1, surpassing PaLM-540B CoT by 15% absolute), 61.2% on GSM-Hard. Demonstrated across 12 BIG-Bench Hard tasks.\n\n**Source:** [PAL on arXiv](https://arxiv.org/abs/2211.10435)\n\n### ToRA: Tool-Integrated Reasoning Agent\n- **Title:** ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving\n- **Authors:** Zhibin Gou, Zhihong Shao, Yeyun Gong, et al. (Microsoft Research)\n- **Date/Venue:** arXiv:2309.17452, ICLR 2024\n- **Core method:** ToRA interleaves natural language reasoning with programmatic tool use (computation libraries, symbolic solvers) in a unified format. Models are trained via imitation learning on interactive tool-use trajectories, followed by output space shaping to refine reasoning behavior. The method achieves fast inference averaging only 1.02 tool interaction rounds per problem.\n- **Relation to best-of-N:** ToRA's interleaved format means each candidate solution contains executable code segments whose outputs can be checked, providing a natural verification signal for selection among candidates.\n- **Key results:** ToRA-7B reaches 44.6% on MATH (surpassing WizardMath-70B by 22% absolute). ToRA-Code-34B exceeds 50% on MATH, competitive with GPT-4. 13-19% absolute improvements over open-source baselines across 10 math datasets.\n\n**Source:** [ToRA on arXiv](https://arxiv.org/abs/2309.17452)\n\n### MathCoder: Seamless Code Integration in LLMs\n- **Title:** MathCoder: Seamless Code Integration in LLMs for Enhanced Mathematical Reasoning\n- **Authors:** Ke Wang, Houxing Ren, Aojun Zhou, Zimu Lu, et al.\n- **Date/Venue:** arXiv:2310.03731, October 2023\n- **Core method:** Fine-tunes open-source LLMs on MathCodeInstruct, a dataset where each solution interleaves natural language, executable code, and code execution results. Inspired by GPT-4 Code Interpreter's seamless reasoning-code-execution loop.\n- **Relation to best-of-N:** Each generated solution contains embedded code that can be re-executed for verification. The interleaved format creates a trace where computational claims are checkable.\n- **Key results:** 45.2% on MATH, 83.9% on GSM8K. Surpasses ChatGPT-3.5 and PaLM-2; competitive with GPT-4 on MATH.\n\n**Source:** [MathCoder on arXiv](https://arxiv.org/abs/2310.03731)\n\n---\n\n## 3. CODE-EXECUTION-BASED VERIFICATION SYSTEMS\n\n### SymCode: Neurosymbolic Verifiable Code Generation\n- **Title:** SymCode: A Neurosymbolic Approach to Mathematical Reasoning via Verifiable Code Generation\n- **Authors:** Sina Bagheri Nezhad, Yao Li, Ameeta Agrawal\n- **Date/Venue:** arXiv:2510.25975, EACL 2026 Findings\n- **Core method:** Reframes mathematical problem-solving as verifiable SymPy code generation. The LLM translates a natural language problem into an executable Python/SymPy script, which is then iteratively refined through a self-debugging loop using deterministic interpreter feedback. Training-free -- works purely through structured prompting.\n- **Relation to best-of-N:** Highly relevant. SymCode shifts model failures from opaque logical fallacies to transparent, programmatic errors. In a best-of-N setting, candidates that execute successfully and produce consistent symbolic outputs can be verified deterministically. The self-debugging loop is itself a form of iterative verification.\n- **Key results:** Up to 13.6 percentage points improvement (16.8 with SymCode+) over CoT baselines on MATH-500, OlympiadBench, and AIME, with gains increasing on harder problems.\n\n**Source:** [SymCode on arXiv](https://arxiv.org/abs/2510.25975)\n\n### HERMES: Efficient and Verifiable Mathematical Reasoning\n- **Title:** HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs\n- **Authors:** Azim Ospanov, Zijin Feng, Jiacheng Sun, Haoli Bai, Xin Shen, Farzan Farnia\n- **Date/Venue:** arXiv:2511.18760, November 2025\n- **Core method:** The first tool-assisted agent that explicitly interleaves informal reasoning with formally verified proof steps in Lean. Uses intermediate formal checking to prevent reasoning drift and employs a memory module for proof continuity across long multi-step chains. Combines exploratory informal reasoning with the rigor of formal theorem-proving verification.\n- **Relation to best-of-N:** Uses formal verification (Lean compiler) rather than code execution, but addresses the same core problem: verifying correctness of candidate solutions. HERMES shows that symbolic verification can dramatically reduce the number of candidates needed by filtering out incorrect reasoning early.\n- **Key results:** Up to 67% accuracy improvement on AIME'25 while using 80% fewer total inference FLOPs compared to reward-based approaches.\n\n**Source:** [HERMES on arXiv](https://arxiv.org/abs/2511.18760)\n\n### DeepSeekMath-V2: Self-Verifiable Mathematical Reasoning\n- **Title:** DeepSeekMath-V2: Towards Self-Verifiable Mathematical Reasoning\n- **Authors:** Zhihong Shao et al. (DeepSeek)\n- **Date/Venue:** arXiv:2511.22570, November 2025\n- **Core method:** Trains an LLM-based verifier for theorem proving, then trains a generator using the verifier as a reward model. Critically introduces a meta-verifier that evaluates the verifier's own analyses, reducing hallucinated errors. The generator is incentivized to self-identify and resolve issues in its proofs before finalizing them.\n- **Relation to best-of-N:** The self-verification paradigm means each candidate can be scored by the model's own verification module. The meta-verifier addresses the key failure mode in verification-guided best-of-N: the verifier itself being unreliable. Analysis quality improves from 0.85 to 0.96 with the meta-verifier.\n- **Key results:** Gold-level on IMO 2025 and CMO 2024; 118/120 on Putnam 2024 with scaled test-time compute.\n\n**Source:** [DeepSeekMath-V2 on arXiv](https://arxiv.org/abs/2511.22570)\n\n---\n\n## 4. PROCESS REWARD MODELS WITH CODE VERIFICATION\n\n### GenPRM: Generative PRM with Code Verification\n- **Title:** GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning\n- **Authors:** Jian Zhao, Runze Liu, Kaiyan Zhang, et al.\n- **Date/Venue:** arXiv:2504.00891, AAAI 2026\n- **Core method:** Redefines process supervision as a generative task. GenPRM performs explicit Chain-of-Thought reasoning with code verification before judging each reasoning step. Uses Relative Progress Estimation (RPE) and a rationale synthesis framework incorporating code verification for training data. Trained on only 23K examples from MATH.\n- **Relation to best-of-N:** Directly applicable as a verifier for best-of-N selection. The code verification component provides a deterministic signal within the generative PRM framework. GenPRM can rank candidates by verified step-level correctness.\n- **Key results:** 1.5B GenPRM outperforms GPT-4o on ProcessBench; 7B GenPRM surpasses Qwen2.5-Math-PRM-72B (a 10x larger discriminative PRM).\n\n**Source:** [GenPRM on arXiv](https://arxiv.org/abs/2504.00891)\n\n### CodePRM: Execution Feedback-Enhanced Process Reward Model\n- **Title:** CodePRM: Execution Feedback-enhanced Process Reward Model for Code Generation\n- **Authors:** (ACL 2025 Findings)\n- **Date/Venue:** ACL 2025 Findings\n- **Core method:** Collects thought traces where each step is labeled with derived code pass rates from execution feedback. Trains a PRM that takes both the reasoning process and code execution feedback as input to score individual thought steps. Deployed in a Generate-Verify-Refine (GVR) pipeline.\n- **Relation to best-of-N:** The GVR pipeline is essentially a refined best-of-N: generate candidates, verify each step using code execution feedback, and refine failing candidates. Code execution provides the ground-truth signal for step-level scoring.\n- **Key results:** Outperforms strong baselines on code generation benchmarks.\n\n**Source:** [CodePRM at ACL Anthology](https://aclanthology.org/2025.findings-acl.428/)\n\n### CodeRM: Dynamic Scaling of Unit Tests for Reward Modeling\n- **Title:** Dynamic Scaling of Unit Tests for Code Reward Modeling\n- **Authors:** Zeyao Ma, Xiaokang Zhang, Jing Zhang, Jifan Yu, Sijia Luo, Jie Tang\n- **Date/Venue:** ACL 2025 (Long Papers)\n- **Core method:** Reveals a positive correlation between the number of unit tests and reward signal quality. Trains CodeRM-8B, a lightweight unit test generator, and employs dynamic scaling -- generating more unit tests for harder problems -- to improve verification quality.\n- **Relation to best-of-N:** Directly addresses the quality of reward signals used in best-of-N selection via code execution. Shows that scaling the number of verification tests per candidate improves selection accuracy, especially for harder problems.\n- **Key results:** 18.43% improvement for Llama3-8B and 3.42% for GPT-4o-mini on HumanEval Plus.\n\n**Source:** [CodeRM on arXiv](https://arxiv.org/abs/2501.01054)\n\n---\n\n## 5. TEST-TIME SCALING AND VERIFICATION CONTEXT\n\n### TTRL: Test-Time Reinforcement Learning (baseline for T3RL)\n- **Title:** TTRL: Test-Time Reinforcement Learning\n- **Authors:** (PRIME-RL team)\n- **Date/Venue:** arXiv:2504.16084, NeurIPS 2025\n- **Core method:** Uses majority voting among multiple sampled predictions to create pseudo-labels on unlabeled test data, then uses these as reward signals for RL training at test time. The key insight is that majority voting provides surprisingly effective rewards without ground-truth labels.\n- **Relation to best-of-N:** TTRL is the direct predecessor to T3RL. It demonstrates that majority voting (a form of best-of-N) can drive self-improvement, but is vulnerable to \"spurious signal amplification\" where frequent-but-wrong answers dominate. T3RL fixes this with code-execution verification.\n- **Key results:** Boosts Qwen-2.5-Math-7B pass@1 by ~211% on AIME 2024 with only unlabeled test data.\n\n**Source:** [TTRL on arXiv](https://arxiv.org/abs/2504.16084)\n\n### Snell et al.: Scaling LLM Test-Time Compute\n- **Title:** Scaling LLM Test-Time Compute Optimally Can Be More Effective than Scaling Model Parameters\n- **Authors:** Charlie Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar\n- **Date/Venue:** arXiv:2408.03314, ICLR 2025 (Oral)\n- **Core method:** Analyzes two mechanisms for scaling test-time compute: (1) searching against process-based verifier reward models (PRMs) and (2) adaptively updating the model's response distribution. Introduces compute-optimal strategies that adaptively allocate test-time compute per prompt.\n- **Relation to best-of-N:** Establishes the theoretical framework for best-of-N with verification. Shows compute-optimal strategies improve efficiency 2-4x over naive best-of-N. The quality of the verifier is the key bottleneck -- directly motivating symbolic/code-based verification as a stronger signal.\n- **Key results:** Compute-optimal test-time scaling can match the performance of a 14x larger model on certain prompts.\n\n**Source:** [Snell et al. on arXiv](https://arxiv.org/abs/2408.03314)\n\n### Scoring Verifiers: Evaluating Synthetic Verification\n- **Title:** Scoring Verifiers: Evaluating Synthetic Verification for Code and Reasoning\n- **Authors:** Aleksander Ficek, Somshubra Majumdar, Vahid Noroozi, Boris Ginsburg\n- **Date/Venue:** arXiv:2502.13820, COLM 2025\n- **Core method:** Proposes benchmarks and metrics to evaluate synthetic verifiers (test case generators, reward models) for code and reasoning tasks. Releases HE-R, HE-R+, MBPP-R, MBPP-R+ benchmarks for scoring and ranking candidate solutions.\n- **Relation to best-of-N:** Directly evaluates the ranking quality of different verification methods for selecting among candidates. Shows that reasoning-enhanced models substantially improve test case generation quality, and scaling the number of test cases improves verification accuracy.\n- **Key results:** Reasoning models significantly improve synthetic verification quality; more test cases yield better ranking accuracy.\n\n**Source:** [Scoring Verifiers on arXiv](https://arxiv.org/abs/2502.13820)\n\n---\n\n## 6. ADDITIONAL RELATED WORK\n\n### ExecVerify: White-Box RL with Verifiable Stepwise Rewards\n- **Title:** ExecVerify: White-Box RL with Verifiable Stepwise Rewards for Code Execution Reasoning\n- **Authors:** Lingxiao Tang, He Ye, et al. (Zhejiang University, UCL)\n- **Date/Venue:** arXiv:2603.11226, March 2026\n- **Core method:** Derives verifiable white-box rewards from execution traces (next-statement prediction, variable value/type prediction). Uses a two-stage training pipeline: first enhances execution reasoning, then transfers to code generation. Note: this paper focuses on code execution reasoning rather than mathematical reasoning specifically.\n- **Relation to best-of-N:** Demonstrates that execution traces can provide reliable step-level verification signals, which could be applied to verify mathematical reasoning steps that are expressed as code.\n- **Key results:** 7B model matches 32B models on code reasoning benchmarks; up to 5.9% pass@1 improvement on code generation.\n\n**Source:** [ExecVerify on arXiv](https://arxiv.org/abs/2603.11226)\n\n### Agentic Code Reasoning\n- **Title:** Agentic Code Reasoning\n- **Authors:** Shubham Ugare, Satish Chandra (Meta)\n- **Date/Venue:** arXiv:2603.01896, March 2026\n- **Core method:** Introduces \"semi-formal reasoning\" -- structured prompting that requires agents to construct explicit premises, trace execution paths, and derive formal conclusions. Acts as a certificate that prevents the agent from skipping cases or making unsupported claims.\n- **Relation to best-of-N:** Demonstrates that structured code reasoning without execution can still serve as verification. The semi-formal certificates provide verifiable traces that could be used to filter/rank candidates in a best-of-N setting.\n- **Key results:** Accuracy improves from 78% to 88% on patch equivalence verification; 87% on RubberDuckBench (9 point gain).\n\n**Source:** [Agentic Code Reasoning on arXiv](https://arxiv.org/abs/2603.01896)\n\n---\n\n## SYNTHESIS: The Landscape\n\nThe field can be organized along two axes:\n\n**Axis 1 -- What is verified:**\n- Final answer only (majority voting, ORM)\n- Step-level process (PRM, GenPRM, CodePRM)\n- Full symbolic trace (PAL, SymCode, HERMES, T3RL)\n\n**Axis 2 -- How verification is performed:**\n- Neural/learned verifiers (PRM, ORM, ThinkPRM)\n- Code execution against test cases (PAL, ToRA, MathCoder, CodeRM)\n- Formal proof checking (HERMES via Lean, DeepSeekMath-V2)\n- Hybrid: neural + code execution (T3RL, GenPRM, CodePRM)\n\nT3RL sits at the intersection of step-level verification and hybrid neural+code execution, making it directly relevant to your symbolic pre-filtering proposal. The key gap it fills is using code execution not just for generating answers (as in PAL/ToRA) but specifically for filtering/reweighting candidates in the best-of-N selection process during test-time self-improvement.\n\nThe most important papers for your related work section are likely: T3RL, TTRL (as baseline), GenPRM (code-verified PRM), SymCode (neurosymbolic verification), HERMES (formal verification for efficiency), Snell et al. (compute-optimal best-of-N framework), and the foundational PAL/ToRA works.\n\nSources:\n- [T3RL - arXiv:2603.02203](https://arxiv.org/abs/2603.02203)\n- [TTRL - arXiv:2504.16084](https://arxiv.org/abs/2504.16084)\n- [PAL - arXiv:2211.10435](https://arxiv.org/abs/2211.10435)\n- [ToRA - arXiv:2309.17452](https://arxiv.org/abs/2309.17452)\n- [MathCoder - arXiv:2310.03731](https://arxiv.org/abs/2310.03731)\n- [SymCode - arXiv:2510.25975](https://arxiv.org/abs/2510.25975)\n- [HERMES - arXiv:2511.18760](https://arxiv.org/abs/2511.18760)\n- [DeepSeekMath-V2 - arXiv:2511.22570](https://arxiv.org/abs/2511.22570)\n- [GenPRM - arXiv:2504.00891](https://arxiv.org/abs/2504.00891)\n- [CodePRM - ACL 2025 Findings](https://aclanthology.org/2025.findings-acl.428/)\n- [CodeRM - arXiv:2501.01054](https://arxiv.org/abs/2501.01054)\n- [Snell et al. - arXiv:2408.03314](https://arxiv.org/abs/2408.03314)\n- [Scoring Verifiers - arXiv:2502.13820](https://arxiv.org/abs/2502.13820)\n- [ExecVerify - arXiv:2603.11226](https://arxiv.org/abs/2603.11226)\n- [Agentic Code Reasoning - arXiv:2603.01896](https://arxiv.org/abs/2603.01896)"
      }
    ],
    "totalDurationMs": 258653,
    "totalTokens": 40598,
    "totalToolUseCount": 29,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1836,
      "cache_read_input_tokens": 33266,
      "output_tokens": 5495,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1836
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5495,
          "cache_read_input_tokens": 33266,
          "cache_creation_input_tokens": 1836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1836,
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
      "otherToolCount": 29
    }
  },
  "sourceToolAssistantUUID": "41ea2268-9dc0-4d45-bf9d-cf4e6f1f7003",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Symbolic Pre-Filtering for Compute-Efficient Best-of-N Verification: A…",
  "leafUuid": "d49c3a54-3e77-4481-8fde-1d7e065fc1ae",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Quantifying symbolic-neural verifier complementarity in best-of-N reasoning",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b"
}
```

---

### Assistant

_source line 24 · 2026-05-10T18:15:46.974Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent. I now have comprehensive research findings. Let me synthesize everything before writing the revised proposal.

## Key Takeaways from Research

### 1. Extraction Mechanism Problem
- SymCode generates code directly, has NO extraction patterns (confirmed)
- MATH-VF uses LLM-based formalization to SimpleMath language, ~90% accuracy but expensive
- Regex works well for final answers only (via \boxed{}), fails for intermediate expressions
- The "cheap pre-filtering" premise is undermined if we need LLM calls

### 2. Error Distribution Reality
- Calculation errors: only ~15.4% of all errors (DeltaBench)


- Reasoning errors dominate at ~25.3%, while DeepSeek-R1 shows just 3.1% calculation errors
- Neural verifiers already excel at catching arithmetic mistakes, and as models improve, these errors shrink fastest—which actually weakens the case for SymFilter on stronger models

### 3. Key Missing Works
- **T3RL** (March 2026): Compiles reasoning traces into Python code for verification-aware voting, very similar to our approach
- **GenPRM** (AAAI 2026): Integrates code verification into PRM
- **BoN-MAV** (COLM 2025): Multi-agent verification combining heterogeneous verifiers
- **"When Does Verification Pay Off?"**: Shows cross-family verification outperforms self-verification when there's distribution diversity
- **FoVer** (ACL 2026): Uses Z3/Isabelle for PRM training data
- **DeepConf**: Achieves 99.9% on AIME 2025 through confidence-weighted voting
- **AIMO-2**: Won the competition leveraging SymPy and Python code execution verification
- **Controllable and Verifiable Process Data Synthesis**: Applies symbolic recomputation for PRM training

### 4. The Real Landscape
Code execution verification has become standard practice across multiple approaches, heterogeneous multi-agent verification is already being explored, the fundamental question of when verification helps has been partially resolved, and researchers are actively mapping out the Pareto frontier of these methods.

### Fundamental Assessment

The SymFilter approach has some serious flaws—the extraction mechanism doesn't work as intended, the error types it targets are already well-handled by neural verifiers, the actual catch rate falls short of expectations, and code-execution verification for best-of-N selection is already implemented in T3RL and similar systems. The error taxonomy doesn't offer anything particularly novel either.

I need to decide whether to pivot entirely, do a major overhaul, or just patch things up. Given how fundamental these issues are, a major revision makes more sense. The core problem—improving verification for best-of-N selection—is still worth solving, but the approach itself needs to be rethought from the ground up.

What actually stands out is the insight from "When Does Verification Pay Off?"—verification becomes most valuable when the solver and verifier operate from different distributions. That's the theoretical bedrock for combining symbolic and neural verification approaches. The implementation strategy, though, needs to change significantly.

Rather than positioning this as a pre-filtering mechanism, I should focus on what's genuinely unexplored: the **cost-accuracy tradeoff** when combining different verification modalities. Existing work looks at multiple neural verifiers together, T3RL applies code execution within a training loop rather than for pure selection, and "When Does Verification Pay Off?" examines cross-model verification but only between neural systems. What's missing is a systematic study of how symbolic and neural verification complement or overlap each other in best-of-N scenarios, and how to optimize the cost-accuracy frontier across these different approaches.

For the extraction mechanism, I'm leaning toward answer-level verification—checking whether the final numerical answer satisfies the problem constraints, matches the expected format, and passes basic arithmetic checks. It's implementable and honest about its limitations, though I'm uncertain if it's substantial enough for a strong contribution. The reviewer's suggestion to focus on options B or D given the timeline is pushing me to reconsider whether studying verification diversity more broadly could yield something more compelling than a narrow symbolic pre-filter.

What if I frame this around the "When Does Verification Pay Off?" framework and treat deterministic verification as the maximally diverse verifier—something with zero distribution overlap compared to neural approaches? I could measure whether this extreme diversity yields gains beyond what cross-model neural verification alone provides. This grounds the work in existing theory, positions symbolic checking as one dimension of a larger diversity study, and delivers a clear contribution regardless of whether symbolic methods help significantly. The practical side would combine answer-level deterministic checks, Math-Verify style equivalence checking, and a single neural verifier to keep things tractable.

But I'm realizing the real contribution might be deeper—combining insights about how verification works best when solver and verifier distributions differ, how different error types need different detection methods, and how heterogeneous verification outperforms homogeneous approaches. The actual gap in the literature is studying the verification modality Pareto frontier: what's the optimal combination of verification approaches given a fixed compute budget?

Actually, let me step back. The reviewer gave concrete guidance and I have a 15-day timeline, so I should focus there instead of chasing the most general formulation. They want me to pick a specific extraction method, recalibrate my hypotheses to realistic ranges with high overlap, differentiate from prior work through complementarity analysis and cost-accuracy tradeoffs, and figure out the timeline constraints.

For the scope: use a 7B model, MATH-500 plus AIME 2024, and just one neural baseline. Drop the error taxonomy work entirely and focus on measuring complementarity and building out the Pareto frontier between cost and accuracy.

This actually clarifies things. I should reframe the whole paper away from "SymFilter as a pipeline" and toward "an empirical study of how different verification modalities complement each other and where the cost-accuracy tradeoffs matter most." Use straightforward deterministic checks—answer-level matching and regex for explicit arithmetic—acknowledge that the catch rate will be low, and study when and why these methods actually help. Make the cost-accuracy Pareto analysis the core contribution, properly cite the related work like T3RL and MATH-VF, and drop any claims about novel error taxonomies.

Now I'm reconsidering whether this is ambitious enough. The reviewer's suggestion gives me a solid workshop paper, but I'm wondering if there's a way to make it more compelling for a top venue. What does the field actually need right now?

There's recent work on when neural verification helps—showing that cross-family verification beats intra-family, which beats self-verification. The gap I see is understanding where deterministic and symbolic verification fit into that hierarchy. Theory suggests they should be maximally effective since they have zero distribution overlap with neural verifiers, but in practice they're limited by what they can actually detect.

Then there's the heterogeneous verifier work combining multiple LLM-based checkers at scale. What if I added a non-neural dimension to that? Testing whether diversity gains extend beyond purely neural approaches could be genuinely interesting.

So I'm reframing this as: deterministic checks are maximally different from neural reasoning in mechanism, so the theory predicts they should provide the most useful signal for best-of-N selection. The real question is whether that theoretical maximum difference actually translates to practical gains.

The tension is clear—theory says orthogonality should help, but deterministic checks only catch a narrow slice of errors. I'd measure whether that orthogonality compensates for the limited coverage, analyze the cost-accuracy tradeoff since these checks are nearly free, and derive a practical recipe for optimal verification mixes at different compute budgets.

For the experiment, I'll use lightweight deterministic checks plus a single neural verifier baseline, test across N ∈ {8, 16, 32, 64} on MATH-500 and AIME 2024 using a 7B model, and track accuracy, cost, overlap, and per-error-type detection rates. My recalibrated hypotheses are that deterministic checks reject only 5-15% of incorrect answers and that the overlap with neural verifier rejections is substantial enough to question whether the modest signal justifies the added complexity.

The real question is whether this combination actually yields meaningful gains when both approaches share the same neural budget, or if I'm just adding noise to an already-effective verifier. I need to be honest about the limitations before committing to a full paper.

But the motivation is solid—the field is pouring resources into symbolic verification methods, yet nobody's actually measured whether cheap deterministic checks complement neural verifiers in practice. That's a gap worth filling, even if the answer turns out to be "not much." Practitioners need that signal to decide whether the engineering overhead is justified.

Now I'm clarifying how my approach differs from related work: T3RL requires expensive LLM compilation steps to generate executable code, whereas I'm proposing lightweight heuristic checks that don't need any LLM calls. MATH-VF and GenPRM both rely on neural components for formalization or verification, and existing verification papers focus on neural-neural pairs—none of them isolate the value of deterministic checks as a cheap add-on layer.

The key insight is that I'm testing whether the simplest possible deterministic checks—just pattern matching and answer-level constraints—can provide orthogonal signal to neural verifiers in best-of-N selection, and whether that payoff justifies the computational cost. This seems too trivial to study, which is probably why it hasn't been done empirically.

Now I need to decide if this is a major revision or a pivot. The core question has shifted from "can cheap symbolic pre-filtering complement neural verifiers?" to "do deterministic checks provide orthogonal signal in best-of-N, and when is adding them cost-justified?"—and the mechanism has changed from multi-level filtering to something different.

Going through the specifics: I'm dropping the SymPy pipeline and expression extraction entirely, keeping only answer-level and explicit arithmetic checks. The expected improvements are now 5-15% instead of 20-50%. I'm removing the error taxonomy contribution and adding a cost-accuracy Pareto analysis instead. The framing now connects to "When Does Verification Pay Off?" rather than the original angle.

This feels like a major revision rather than a pivot—the core research area stays the same, but the approach, contributions, and framing are substantially different. Now I need to write out the full revised proposal and address each reviewer issue systematically.

For the extraction mechanism, I'm completely removing SymPy and expression extraction, relying only on regex for arithmetic lines and answer-level verification. For the error rate concern, I'm recalibrating H1 down to 5-15% and reframing H2 as measuring complementarity rather than claiming large gains. On T3RL, I'm differentiating by noting they use expensive LLM compilation while I'm studying the cheapest deterministic checks—the question is whether zero-cost checks add marginal value on top of neural verification. I'm dropping the error taxonomy claim and citing existing work instead. And I'm adding citations to FoVer, BoN-MAV, "When Does Verification Pay Off?", and PAL to address the missing related work.

I also need to add ToRA, Controllable PRM synthesis, GenPRM, and DeepConf as relevant baselines. For the model scaling issue, I'm acknowledging it explicitly and using only the 7B model, then reframing the finding as establishing bounds on when deterministic checks are most and least useful across problem difficulty. Given the 15-day timeline, I'm scoping down to 7B, MATH-500 plus AIME 2024, one ORM with majority vote baselines, and simple deterministic checks implementable in days, targeting the NeurIPS MATH-AI workshop.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d49c3a54-3e77-4481-8fde-1d7e065fc1ae",
  "isSidechain": false,
  "requestId": "req_011CauLpAHbDQKSGwsv93Mrt",
  "type": "assistant",
  "uuid": "6365cbbc-9175-49fe-820b-732a8fce40a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YJVrUwMhSGHp7LQjuumr74",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 10433,
      "cache_creation_input_tokens": 7487,
      "cache_read_input_tokens": 22924,
      "output_tokens": 9424,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7487,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 10433,
          "output_tokens": 9424,
          "cache_read_input_tokens": 22924,
          "cache_creation_input_tokens": 7487,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7487
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

_source line 25 · 2026-05-10T18:17:43.023Z_

Now let me synthesize all this research before writing the revised proposal. The findings are comprehensive and reveal that the original idea needs major revision:

**Key findings from research:**
1. **Extraction is fundamentally broken**: SymCode generates code directly (no extraction patterns). MATH-VF uses expensive LLM formalization (~90% accuracy). Regex works only for final answers.
2. **Calculation errors are ~15.4% of all errors** and already the easiest for neural verifiers to detect. For DeepSeek-R1 specifically, only 3.1% are calculation errors.
3. **T3RL** already does code-execution verification for test-time reasoning. **BoN-MAV** combines heterogeneous verifiers. **"When Does Verification Pay Off?"** shows cross-distribution diversity is key.
4. **Error taxonomy claim is invalid** - multiple existing works (Sun et al., ErrorAtlas, Zhang & Graf).
5. **Model scaling shifts errors away from arithmetic** - exactly against the original approach.

I need to do a major revision. The core contribution should shift to the **complementarity measurement and cost-accuracy Pareto analysis** — not the mechanism itself. Let me draft the revised proposal.

```json
{
  "change_type": "major",
  "title": "Beyond Neural Verification Diversity: Measuring the Marginal Value of Deterministic Checks in Best-of-N Mathematical Reasoning",
  "core_problem": "Best-of-N sampling with neural verifiers (ORM/PRM) is the standard paradigm for test-time compute scaling in mathematical reasoning. Recent work ('When Does Verification Pay Off?', arXiv 2512.02304) establishes that verification is most effective when solver and verifier have maximally different solution distributions—cross-family neural verification outperforms intra-family and self-verification. Deterministic checks (answer-format validation, numerical bound checking, explicit arithmetic re-execution via regex+SymPy) represent the maximally different 'verifier'—they use entirely non-neural mechanisms with zero distribution overlap. Yet no work has empirically measured whether this maximal mechanism-level diversity translates to useful outcome-level complementarity, or whether deterministic checks are too limited in error-type coverage (~5-15% of errors are arithmetic) to provide marginal signal over neural verifiers that already detect calculation errors well. The open question: given a fixed compute budget for best-of-N, is the near-zero cost of deterministic pre-filtering worth the modest signal it provides on top of neural verification?",
  "opportunity": "There is a surprising gap between the theoretical prediction (maximal verifier diversity → maximal complementarity) and what empirical evidence suggests about deterministic verification's utility. Error taxonomy studies (DeltaBench, arXiv 2502.19361; Sun et al., EMNLP 2025 Findings; ErrorAtlas, arXiv 2601.15812) consistently find that calculation errors are only ~15% of math reasoning errors and are already the easiest category for neural verifiers to detect. This predicts HIGH overlap between deterministic rejection and neural low-scoring—directly contradicting the diversity-implies-complementarity hypothesis. Yet this prediction has never been empirically tested: no prior work quantifies the actual overlap between deterministic rejection and neural ranking in best-of-N. BoN-MAV (COLM 2025) combines heterogeneous verifiers but all are LLM-based. T3RL (arXiv 2603.02203) uses code execution for verification but requires expensive LLM compilation of reasoning traces—it is not cheap. MATH-VF (arXiv 2505.20869) applies SymPy+Z3 step-wise but uses LLM formalization per step, again undermining cheapness. The gap: empirically testing whether the CHEAPEST possible deterministic checks (no LLM calls, sub-millisecond) provide marginal value over neural verification, and characterizing the cost-accuracy Pareto frontier of verification modality combinations.",
  "landscape": "Test-time compute scaling via best-of-N is well-studied (Snell et al., ICLR 2025; compute-optimal allocation showing S∝C^0.57, V∝C^0.39). Neural verifiers include ORMs (Rewarding Progress, ICLR 2025), PRMs, ThinkPRM (2025), and generative verifiers (GenPRM, AAAI 2026). Code-execution verification has emerged as a powerful modality: PAL (ICML 2023) and ToRA (ICLR 2024) generate code solutions directly; SymCode (EACL 2026) produces verifiable SymPy code; T3RL (March 2026) compiles reasoning traces into Python for verification-aware voting in test-time RL; the AIMO-2 winning solution used tool-integrated reasoning with SymPy execution at scale. Formal verification approaches include FANS (EMNLP 2025) and Safe (ACL 2025) using Lean4, and HERMES (Nov 2025) achieving 80% fewer FLOPs via interleaved formal verification. On verification diversity, 'When Does Verification Pay Off?' (arXiv 2512.02304) systematically shows cross-family verification >> self-verification due to distribution dissimilarity, but only studies neural-neural pairs. BoN-MAV (COLM 2025) combines multiple LLM-based verifiers with democratic voting, scaling to N=256 with continued gains. FoVer (ACL 2026) uses Z3/Isabelle to synthesize PRM training data. DeepConf (2025) achieves 99.9% on AIME 2025 with confidence-weighted majority voting—no external verifier needed. On error distributions, DeltaBench (arXiv 2502.19361) finds calculation errors at ~15.4% behind reasoning (25.3%) and understanding (15.7%) errors; Sun et al. (EMNLP 2025 Findings) show errors shift from computational to reasoning as models scale; Zhang & Graf (AIME-Con 2025) find o1-class models achieve flawless arithmetic with residual errors being purely conceptual. The critical gap: while individual verification modalities are well-studied, no work measures the marginal value of the cheapest deterministic layer (answer-level + regex arithmetic checks, no LLM calls) on top of neural verification in best-of-N, or maps the cost-accuracy Pareto frontier across verification modality combinations.",
  "approach": "We propose an empirical study measuring whether cheap deterministic checks provide marginal value over neural verifiers in best-of-N mathematical reasoning. Unlike T3RL (which requires LLM compilation of traces), MATH-VF (which requires LLM formalization per step), or BoN-MAV (which uses only neural verifiers), we study the cheapest possible deterministic verification layer—one requiring no LLM calls and running in sub-milliseconds per candidate.\n\n**Deterministic Check Suite (DCS):** (a) Answer-format validation: verify the final answer is a well-formed number/expression matching expected format; (b) Numerical bound checks: verify the answer falls within problem-implied ranges (e.g., a probability ∈ [0,1], a count ≥ 0, a length > 0); (c) Constraint back-substitution: for problems with explicit constraints (e.g., 'find x such that 2x+3=7'), substitute the final answer back and verify; (d) Explicit arithmetic re-execution: regex extraction of lines matching patterns like 'A op B = C' (e.g., '3 × 4 = 13') and re-execution via SymPy. The DCS only REJECTS candidates with verified errors—it never selects.\n\n**Experimental Design:** Generator: DeepSeek-R1-Distill-Qwen-7B with N∈{8,16,32,64}. Benchmarks: MATH-500 and AIME 2024. Neural baseline: Qwen2.5-Math-PRM-7B as the process reward model. Configurations compared: (1) Majority vote (MV); (2) ORM/PRM best-of-N; (3) DCS → MV on survivors; (4) DCS → PRM on survivors (our pipeline); (5) Oracle: DCS with perfect precision, measuring the upper-bound gain from any deterministic pre-filter.\n\n**Measurements:** (M1) DCS rejection rate: what fraction of incorrect candidates does DCS catch? We predict 5-15% based on prior error-type distributions. (M2) DCS-neural overlap: of candidates DCS rejects, what fraction are already in the bottom quartile of PRM scores? We predict >50% overlap (testing whether mechanism-level orthogonality implies outcome-level complementarity). (M3) Accuracy delta: DCS+PRM vs. PRM-alone accuracy across N values. We predict 0.5-3% improvement, with larger gains at higher N where more incorrect candidates exist to filter. (M4) Cost-accuracy Pareto: for a fixed total compute budget, compare (a) spending it all on more N with PRM scoring, (b) same N with DCS pre-filtering to reduce PRM scoring cost, (c) reducing N but using the saved budget on a stronger PRM. (M5) Per-difficulty analysis: measure DCS utility by MATH difficulty level, testing whether cheap checks help more on easier problems (where arithmetic errors are more prevalent).\n\n**Hypotheses (explicitly testable, calibrated to prior evidence):** H1: DCS rejects 5-15% of incorrect candidates from the 7B model (based on ~15% calculation error rate in DeltaBench, discounted for imperfect regex recall). H2: >50% of DCS-rejected candidates overlap with the bottom-25% PRM-scored candidates (based on DeltaBench finding that neural verifiers already excel at calculation errors). H3: DCS+PRM at N=64 yields 0.5-3% accuracy gain over PRM-alone (modest, reflecting low rejection rate and high overlap). H_null: If H1 yields <5% rejection and H3 shows <0.5% gain, the conclusion is that deterministic checks do not provide meaningful marginal signal—itself a useful finding that tells practitioners to invest in better neural verifiers rather than symbolic pipelines.\n\n**Negative result commitment:** We explicitly frame this as a measurement study. The contribution holds regardless of direction: if DCS helps, we provide a practical recipe for when to add it; if DCS doesn't help, we provide empirical evidence that the 'verification diversity' principle has limits when the diverse verifier has very narrow error-type coverage, and we save the community from building expensive symbolic verification pipelines that provide marginal returns.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~60h H100 (candidate generation: 7B model N=64 on MATH-500+AIME2024 ~25h; PRM scoring ~20h; baselines and ablations ~15h)",
      "gpu_utilization": "Low (~20-30%). Human implements DCS regex patterns, analysis scripts. GPU active only during generation and PRM scoring phases.",
      "timeline": "2-3 weeks (Days 1-3: implement DCS regex+answer checks, generate candidates; Days 4-7: PRM scoring baselines; Days 8-10: combined pipeline experiments + Pareto analysis; Days 11-15: analysis and writing)",
      "team": "1 researcher with Python/SymPy experience",
      "estimated_gpu_cost": "$150-200 (at ~$2.50/hr H100)"
    },
    "human_in_loop": {
      "gpu_hours": "~80h H100 (additional N-sweeps and per-difficulty breakdowns)",
      "gpu_utilization": "Moderate (~35-45%). Agent implements pipeline and runs experiments; human validates DCS check quality on sample of candidates.",
      "timeline": "10-14 days",
      "team": "1 researcher, ~20min/day reviewing DCS rejection samples",
      "claude_api_cost": "$40-80 (estimated 400-600 turns for implementation and analysis)",
      "estimated_gpu_cost": "$200-250",
      "risk_note": "The main risk is that DCS regex extraction recall is so low (<3%) that there are insufficient rejections to draw statistically meaningful conclusions about complementarity. Mitigation: answer-level checks (format, bounds, constraint back-substitution) should provide a baseline rejection rate independent of regex quality."
    },
    "auto_research": {
      "gpu_hours": "~100h H100 (comprehensive N-sweeps, per-difficulty analysis, threshold sensitivity for bound checks)",
      "gpu_utilization": "High (~70-80%). Agent runs generation batches and scoring runs with minimal idle time.",
      "timeline": "5-8 days with 2 H100 GPUs",
      "team": "0 researchers (initial setup ~30 min)",
      "claude_api_cost": "$80-150 (estimated 800-1200 turns)",
      "estimated_gpu_cost": "$250-300",
      "speed_bottleneck": "Generation throughput for 7B model at N=64 across 500+ problems.",
      "risk_note": "Automated DCS implementation may miss edge cases in numerical format parsing; agent should validate on a human-checked sample of 50 candidates before full runs."
    }
  },
  "target_venues": [
    "NeurIPS 2026 MATH-AI Workshop (primary target — good venue for focused empirical measurement studies; submission deadline expected Aug-Sep 2026)",
    "AAAI 2027 (expanded version with additional models and benchmarks; expected abstract Jul 25, paper Aug 1, 2026)",
    "EMNLP 2026 (if results are strong enough to warrant full paper; ARR deadline May 25, 2026 is too tight for current scope)"
  ],
  "level": "solid",
  "key_references": [
    "When Does Verification Pay Off? (arXiv 2512.02304, Nov 2025) — establishes solver-verifier distribution diversity principle; we extend to non-neural verification",
    "Multi-Agent Verification: Scaling Test-Time Compute with Multiple Verifiers [BoN-MAV] (COLM 2025) — heterogeneous neural verification; we add deterministic dimension",
    "T3RL: Tool Verification for Test-Time Reinforcement Learning (arXiv 2603.02203, Mar 2026) — LLM-compiled code execution for verification; we study cheapest deterministic alternative",
    "Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving [MATH-VF] (arXiv 2505.20869, May 2025) — LLM-formalized step-wise SymPy/Z3 verification",
    "Can Large Language Models Detect Errors in Long Chain-of-Thought Reasoning? [DeltaBench] (arXiv 2502.19361, Feb 2025) — error type distribution: 15.4% calculation errors, verifiers best at catching these",
    "Error Classification of LLMs on Math Word Problems (Sun et al., EMNLP 2025 Findings) — 39-category error taxonomy across 15 LLMs; errors shift from computational to reasoning with scaling",
    "ErrorAtlas: A Large-Scale Benchmark of LLM Reasoning Errors (arXiv 2601.15812) — 17-category taxonomy from 83 models, ~8.5% computation errors",
    "Mathematical Computation and Reasoning Errors by LLMs (Zhang & Graf, AIME-Con 2025) — o1-class models achieve flawless arithmetic; residual errors are conceptual",
    "PAL: Program-aided Language Models (ICML 2023) — foundational code-execution-for-math",
    "ToRA: A Tool-Integrated Reasoning Agent for Mathematical Problem Solving (ICLR 2024) — interleaved code execution",
    "SymCode: Neurosymbolic Verifiable Code Generation (EACL 2026) — generates SymPy code directly, no extraction patterns",
    "FoVer: Efficient PRM Training Data Synthesis via Formal Verification (ACL 2026 Findings) — Z3/Isabelle for PRM training labels",
    "Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning (ICLR 2025)",
    "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (AAAI 2026) — PRM with code verification",
    "FANS: Formal Answer Selection Using Lean4 (EMNLP 2025)",
    "Safe: Step-aware Formal Verification (ACL 2025)",
    "HERMES: Efficient and Verifiable Mathematical Reasoning in LLMs (arXiv Nov 2025) — 80% fewer FLOPs via interleaved formal verification",
    "Scalable Best-of-N Selection via Self-Certainty (NeurIPS 2025)",
    "DeepConf: Deep Think with Confidence (2025) — 99.9% on AIME 2025 with confidence-weighted voting",
    "Scaling LLM Test-Time Compute Optimally (Snell et al., ICLR 2025)",
    "Inference-Time Reward Hacking in Large Language Models (2025)",
    "Reward Models Enable Scalable Code Verification by Trading Accuracy for Throughput (Orlanski et al., 2025)",
    "Controllable and Verifiable Process Data Synthesis for PRMs (arXiv 2605.02395, May 2026) — symbolic recomputation for PRM training",
    "Compute-Accuracy Pareto Frontiers for Open-Source Reasoning LLMs (arXiv 2512.24776, Dec 2025)"
  ],
  "description": "We present an empirical measurement study asking: do the cheapest possible deterministic checks (answer-format validation, numerical bound checking, constraint back-substitution, and regex-based arithmetic re-execution—all sub-millisecond, no LLM calls) provide marginal value over neural verifiers in best-of-N mathematical reasoning? The 'When Does Verification Pay Off?' framework predicts that maximally different verifiers provide the most useful signal, and deterministic checks are maximally different from neural reasoning. Yet error taxonomy studies consistently find calculation errors are only ~15% of math reasoning errors and are already the easiest category for neural verifiers to detect—predicting high overlap rather than complementarity. We resolve this tension empirically by measuring DCS rejection rates, DCS-neural overlap, accuracy deltas, and cost-accuracy Pareto frontiers across N∈{8,16,32,64} on MATH-500 and AIME 2024 using DeepSeek-R1-Distill-Qwen-7B as the generator and Qwen2.5-Math-PRM-7B as the neural baseline. Unlike T3RL (expensive LLM compilation), MATH-VF (expensive LLM formalization), or BoN-MAV (neural-only diversity), we isolate the value of the cheapest possible deterministic layer. The contribution holds regardless of outcome: if deterministic checks help, we provide a practical cost-justified recipe; if they don't, we establish empirical bounds on the verification diversity principle and redirect practitioners toward better neural verifiers. We explicitly commit to reporting negative results with calibrated hypotheses (5-15% rejection rate, >50% overlap with neural low-scoring, 0.5-3% accuracy gain). Targeting NeurIPS 2026 MATH-AI Workshop, expandable to AAAI 2027.",
  "project_name": "det_check_complementarity",
  "source": "web_research"
}
```

**Summary of changes (major revision):**

1. **Extraction mechanism resolved**: Dropped all claims about adapting SymCode/MATH-VF patterns. The approach now uses only cheap, no-LLM deterministic checks: answer-format validation, numerical bounds, constraint back-substitution, and regex-based explicit arithmetic re-execution. No expression extraction from CoT.

2. **Hypotheses recalibrated**: H1 from 20-50% → 5-15%; H2 acknowledges high overlap (>50%) as the likely outcome; H3 from "matching/exceeding" → 0.5-3% modest gain. Explicit null hypothesis included.

3. **T3RL and all missing work addressed**: Cited and differentiated. T3RL uses expensive LLM compilation; MATH-VF uses expensive LLM formalization; BoN-MAV is neural-only. Our study isolates the cheapest possible deterministic layer — the question is whether near-zero-cost checks provide marginal value.

4. **Error taxonomy claim dropped**: Cited DeltaBench, Sun et al., ErrorAtlas, Zhang & Graf as existing taxonomies. No longer claimed as contribution.

5. **Reframed around "When Does Verification Pay Off?"**: The theoretical motivation is now the tension between maximal mechanism-level diversity (deterministic vs neural) and limited error-type coverage. This gives the study a clear contribution regardless of outcome.

6. **Timeline scoped appropriately**: 7B model only, MATH-500 + AIME 2024 only, one PRM baseline. Implementable in 2 weeks. Primary target shifted to NeurIPS MATH-AI Workshop.

7. **Cost-accuracy Pareto analysis added**: Explicitly studying the optimal compute allocation between more candidates vs. deterministic filtering vs. neural verification budget.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6365cbbc-9175-49fe-820b-732a8fce40a5",
  "isSidechain": false,
  "requestId": "req_011CauLpAHbDQKSGwsv93Mrt",
  "type": "assistant",
  "uuid": "dff5ac3b-53ee-4d30-adec-c3949b61f003",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YJVrUwMhSGHp7LQjuumr74",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 10433,
      "cache_creation_input_tokens": 7487,
      "cache_read_input_tokens": 22924,
      "output_tokens": 9424,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 7487,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 10433,
          "output_tokens": 9424,
          "cache_read_input_tokens": 22924,
          "cache_creation_input_tokens": 7487,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 7487
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

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Symbolic Pre-Filtering for Compute-Efficient Best-of-N Verification: A…",
  "leafUuid": "dff5ac3b-53ee-4d30-adec-c3949b61f003",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Quantifying symbolic-neural verifier complementarity in best-of-N reasoning",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Symbolic Pre-Filtering for Compute-Efficient Best-of-N Verification: A…",
  "leafUuid": "dff5ac3b-53ee-4d30-adec-c3949b61f003",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Quantifying symbolic-neural verifier complementarity in best-of-N reasoning",
  "sessionId": "f0b56d5e-da8c-4bc6-8308-ec1d19ecad9b"
}
```

---
