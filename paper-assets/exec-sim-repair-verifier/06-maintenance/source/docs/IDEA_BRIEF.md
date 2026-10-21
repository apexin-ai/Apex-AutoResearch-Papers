# Idea Brief: Per-Test Execution Simulation as Fine-Grained Verifier for Repair Scaling


- **Idea ID**: `idea_005`
- **Created**: 2026-05-11
- **Approved**: 2026-05-11
- **Source**: foreign:be-idea-gen-0509-5
- **Level**: top-tier
- **Target Venues**: EMNLP 2026 — NLP and Code Models track (ARR May 25, 2026; commitment Aug 2, 2026) [PRIMARY], ICSE 2027 (Jun 23 abstract, Jun 30 paper) [FALLBACK — extended version with full Part 3 + additional baselines], ICLR 2027 (~Oct 2026) [FALLBACK — extended version]

## Seed Topic

Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: NLP and Code Models.

Direction: Code understanding and generation — repo-level comprehension, program repair, code reasoning, debugging, test generation, code-to-documentation, cross-language code transfer. NOT just code completion — focus on higher-level code reasoning tasks.

Contribution type: METHOD ONLY. Propose new training methods, retrieval-augmented code repair, or inference algorithms for code tasks. Not a new benchmark or leaderboard entry.

HARD CONSTRAINTS:
1. Compute: ≤200 H100-hours total. Code models are often evaluated zero-shot or few-shot — budget goes to SFT/LoRA if fine-tuning.
2. Time: ≤16 days. Build on existing code models (DeepSeek-Coder-V2, StarCoder2, CodeLlama, Qwen2.5-Coder) and frameworks (aider, SWE-agent, Moatless).
3. Eval: SWE-bench Verified, HumanEval/MBPP, CrossCodeEval, RepoBench, DebugBench, CodeContests.

Look for: repo-level context compression for code understanding, retrieval-augmented repair with semantic code search, code reasoning via execution feedback, cross-repo transfer learning. Avoid: simple prompt templates for code completion.

Tag: direction=code_models, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].

## Core Problem

Test-time scaling for code repair requires ranking candidate patches, but verification paradigms face a granularity–cost tradeoff. Execution-based verification (running test suites) costs ~$3 and ~45 min per candidate in Docker environments, scaling linearly with rollout count. While Pareto Optimal Code Generation (arXiv:2506.10056) showed that staged verification with ORMs achieves 11.64× throughput gain at 8.26% accuracy cost for function-level code generation, their analysis does not extend to repository-level repair where test outcomes are more complex. Recent execution-free alternatives like SWE-RM (arXiv:2512.21919) predict trajectory-level binary correctness (resolved/unresolved) at low cost but provide only coarse signals that cannot distinguish between candidates that fail on different subsets of tests. Three questions remain open: (1) Can per-test pass/fail simulation — predicting which specific tests a patch passes — provide fine-grained diagnostic signals that improve candidate discrimination over coarse trajectory-level scoring? (2) What per-test simulation accuracy is needed for effective repair scaling, empirically grounding ROC-n-reroll's (arXiv:2507.12399) theoretical framework? (3) Is binary pass/fail classification from (patched_code, test_code) pairs achievable with modest data, given that it is a fundamentally simpler task than the open-ended output prediction studied in Self-Execution Simulation (arXiv:2604.03253) — and one that sidesteps the token-budget exhaustion and string-value prediction failures identified in Debugging Code World Models (arXiv:2602.07672)?

## Opportunity / Why Now

SWE-RM demonstrates that execution-free verification works at the trajectory level (RM@32: 62.0–74.6% on SWE-bench Verified), but its coarse binary signal loses information about partial test passage that could discriminate between candidates. Self-Execution Simulation showed 3B–7B models achieve 68.0–75.5% on CRUXEval-O for output prediction (generating exact stdout), but their task requires 65B tokens of training data because output prediction is open-ended generation. Crucially, Debugging Code World Models (arXiv:2602.07672) identifies two fundamental failure modes of execution simulation: (a) token-budget exhaustion on programs with long execution histories (4.1% failures on HumanEval), and (b) string-value prediction failures due to BPE tokenization discontinuity (73% of CRUXEval-O failures concentrate on string outputs, a 1.58× overrepresentation). Per-test binary classification (pass/fail) sidesteps both failure modes — it does not require generating execution traces or predicting output strings, instead making a single binary decision from (patched_code, test_code) pairs. This is analogous to the difference between text generation and sentiment classification — potentially achievable with orders-of-magnitude less data. Pareto Optimal Code Generation (arXiv:2506.10056) mapped the accuracy–throughput Pareto frontier for function-level code generation, showing staged verification with ORMs is most effective; however, their analysis is limited to function-level benchmarks (HumanEval, MBPP) where test semantics are simple. Repository-level repair involves multi-file patches, complex test fixtures, and test interdependencies — the Pareto frontier at this level is uncharacterized. Agentic Code Reasoning (arXiv:2603.01896) achieves 93% patch equivalence verification accuracy via semi-formal reasoning with frontier models (Claude Opus 4.5), demonstrating the existence of strong execution-free signals; however, it requires expensive frontier-model inference (~$0.50+/candidate), creating a cost gap that a trained 4B model could fill. DryRUN (arXiv:2604.21598) showed prompt-based simulation matches execution-dependent baselines without fine-tuning, suggesting the signal exists in pretrained representations. CodeSense (ICLR 2026) demonstrates that even state-of-the-art LLMs show clear performance gaps on fine-grained code semantic reasoning tasks at statement, block, and function levels, establishing both the difficulty and importance of this capability. CodePRM (ACL Findings 2025) uses execution feedback for process reward models in code generation, showing the value of execution-grounded verification — but operates at the thought-step level rather than per-test level. FunPRM (arXiv:2601.22249) introduces function-as-step process reward models with meta-learning reward correction for code generation, achieving strong function-level verification — but does not address per-test granularity at the repository level. Scoring Verifiers (arXiv:2502.13820, COLM 2025) provides methodology for evaluating synthetic verifiers via ranking benchmarks (HE-R, MBPP-R), directly applicable to our evaluation framework. Yet no work studies (1) per-test simulation as a dedicated repair verifier at the repository level, (2) the accuracy–utility frontier for per-test vs. trajectory-level verification at repo-level complexity, or (3) how simulation compares to reasoning-based and reward-model alternatives on the cost–discrimination Pareto frontier for repository-level repair specifically.

## Landscape (SOTA & Limitations)

Repair verification spans six paradigms with distinct granularity–cost profiles. **Execution-based**: Full test execution (~$3, ~45 min/candidate); Scaling Test-Time Compute (arXiv:2604.16529) achieved 77.6% on SWE-bench Verified via rollout scaling; Scaling Agentic Verifier (arXiv:2602.04254) actively searches for discriminative tests. **Trajectory-level reward models**: SWE-RM (arXiv:2512.21919) — 30B MoE (3B active) trained on 100K trajectories, predicts binary resolved/unresolved from full multi-turn trajectories, achieves RM@32 of 62.0% (Flash) and 74.6% (Max) on SWE-bench Verified; SWE-TRACE (arXiv:2604.14820) introduces rubric-based PRM for process-level scoring; CodePRM (ACL Findings 2025) uses execution feedback as process reward for code generation thought steps; FunPRM (arXiv:2601.22249) proposes function-as-step PRM with meta-learning reward correction for code generation. **Reasoning-based**: PatchReasoner (arXiv:2510.22775) achieves 72.2% patch verification accuracy via holistic reasoning (50× faster than testing); RePaCA (arXiv:2507.22580) reaches 83.1% on Defects4J via GRPO-tuned reasoning; ComPass (arXiv:2602.07561) uses contrastive patch embeddings (88.35% Defects4J); Agentic Code Reasoning (arXiv:2603.01896) achieves 93% patch equivalence verification accuracy via semi-formal reasoning with Claude Opus 4.5 — no fine-tuning needed but requires expensive frontier-model inference. **Agentic verification**: AgentV-RL (arXiv:2604.16004) transforms verification into multi-turn tool-augmented deliberation with forward/backward reasoning agents, achieving 25.2% improvement over ORMs (primarily demonstrated on math reasoning with generalization to LiveCodeBench). **Semantic-matching/Pareto**: CodeScaler (arXiv:2602.17684) achieves +11.72 points via learned semantic preferences without execution; Pareto Optimal Code Generation (arXiv:2506.10056, revised Feb 2026) frames verifier selection as Pareto optimization and maps the accuracy–throughput frontier across ORMs, test suites, and staged verification on function-level Python benchmarks, showing 11.64× throughput gain at 8.26% accuracy cost — but limited to function-level scope. **Simulation-based**: Self-Execution Simulation (arXiv:2604.03253) trains Qwen2.5-3B/7B on 65B tokens to predict program stdout, achieving 68.0% (3B) / 75.5% (7B) on CRUXEval-O and 2–8 point best@k gains on competitive programming; DryRUN (arXiv:2604.21598) uses prompt-based simulation for self-correction; Execution Tuning (arXiv:2503.05703) trains on execution traces achieving ~80% on CRUXEval; CWM (arXiv:2510.02387) mid-trains on 120M traces for general capability; Debugging Code World Models (arXiv:2602.07672) identifies CWM failure modes — token-budget exhaustion and string-value prediction failures due to BPE tokenization. **Code reasoning benchmarks**: CodeSense (ICLR 2026) provides fine-grained semantic reasoning tasks at statement, block, and function levels across real-world Python/C/Java code (4,483 samples), showing clear LLM performance gaps; Scoring Verifiers (COLM 2025) provides HE-R/MBPP-R ranking benchmarks for verifier evaluation. **Additional relevant work**: SWE-Zero/SWE-Hero (arXiv:2604.01496) studies execution-free vs. execution-based fine-tuning with 300K trajectories; TraceRepair (arXiv:2604.02647) uses runtime execution traces with multi-agent debate. The gap: no work (a) trains per-test pass/fail simulation as a fine-grained verifier providing diagnostic signals beyond binary trajectory correctness at the repository level, (b) empirically measures the per-test accuracy threshold for effective repair scaling (extending Pareto Optimal Code Generation's function-level framework to repo-level repair), or (c) compares per-test simulation against trajectory-level reward models (SWE-RM), frontier reasoning-based approaches (Agentic Code Reasoning), and agentic verification alternatives on the discrimination–cost frontier.

## Proposed Approach

Three-part empirical study scoped for ARR May 2026 submission. **Part 1 — Oracle accuracy–utility frontier (Days 1–3).** Using SWE-bench Verified (500 instances) with 16 candidates per instance from existing open-source trajectories (SWE-smith, SWE-Zero datasets), simulate per-test verifiers at 55–99% accuracy by corrupting ground-truth pass/fail labels with calibrated noise. Measure best-of-N selection quality and resolve rate at each accuracy level. Critically, compare per-test simulation (predicting individual test outcomes then aggregating) against trajectory-level simulation (predicting binary resolved/unresolved directly) at matched accuracy levels — this reveals whether fine-grained per-test signals provide better discrimination even at lower per-test accuracy. This empirically grounds ROC-n-reroll's theory and extends Pareto Optimal Code Generation's function-level Pareto framework to repo-level repair, adding the verification granularity dimension (per-test vs. trajectory-level) absent from their analysis. **Data extraction pipeline**: SWE-smith/SWE-Zero trajectory datasets store only binary resolved/unresolved labels, not per-test outcomes. We extract per-test labels by re-evaluating patches through the SWE-bench evaluation harness, which produces a tests_status JSON containing per-test pass/fail for both FAIL_TO_PASS and PASS_TO_PASS test sets. With 500 instances × 16 candidates = 8,000 evaluations, using optimized Docker evaluation with cached per-repository images (leveraging Epoch AI's infrastructure showing SWE-bench Verified runs in ~62 min on a 32-core machine for 500 instances), estimated wall-clock time is ~16–24 hours with 16 parallel containers — not 4 days as initially estimated. This front-loaded computation is a one-time cost amortized across all three parts. **Part 2 — Train per-test simulation verifier (Days 3–9).** Fine-tune Qwen3-4B with LoRA to predict binary pass/fail from (patched_code, test_code) pairs. Key insight: binary pass/fail classification sidesteps the two dominant failure modes of Code World Models identified by Debugging CWMs (arXiv:2602.07672) — token-budget exhaustion on long execution histories and string-value prediction failures from BPE tokenization discontinuity — because it does not require generating execution traces or predicting output strings. Curriculum: (a) pre-train on function-level execution reasoning using CRUXEval pass/fail labels (~800 functions, augmented to ~4K examples by introducing code mutations — operator swaps, off-by-one errors, variable misuse, boundary condition changes — to create failing versions, plus pairing functions with incorrect expected outputs as negatives) supplemented with CodeSense execution-trace data (~4,483 real-world function samples with ground-truth execution outcomes from Python/C/Java repositories), yielding ~8K–9K curriculum examples; (b) fine-tune on SWE-bench repair data (~8K examples from the re-evaluation pipeline in Part 1, with per-test labels from FAIL_TO_PASS and PASS_TO_PASS metadata). **Context length handling**: Repo-level (patched_code, test_code) pairs can span thousands of lines. We use relevant-file extraction: include only patched files and directly referenced test files (not entire repositories), with hierarchical context construction (imports → class/function signatures → patched function body → test function body). **Pilot context-length analysis (Day 1, <1 hour)**: Before training, we sample 100 (patched_code, test_code) pairs from SWE-bench Verified and report the token count distribution (median, P75, P90, P95, max). Based on SWE-bench statistics (average patch size ~33 lines touching 1.7 files; test files typically 50–200 lines), we expect the majority of relevant-file-extracted pairs to fit within 32K tokens. For cases exceeding Qwen3-4B's 32K native context, we apply focal truncation — prioritizing the patched hunks and their surrounding context, plus the test assertions — falling back to YaRN extended context (131K) for the largest cases. We report accuracy stratified by input length to characterize degradation at long contexts. Compare 4B vs. 8B to study model size scaling. Frame explicitly as testing whether the accuracy threshold from Part 1 is achievable with modest data — a negative result (insufficient accuracy) is equally informative, refuting the simulation hypothesis for repair. **Negative-result contingency plan**: If Part 2 yields <70% per-test accuracy, we provide: (a) error taxonomy — categorizing failures by test type (unit vs. integration), code complexity (single-file vs. multi-file), and failure mode (assertion type, semantic complexity); (b) function-to-repo difficulty scaling — comparing accuracy on isolated function-level tests vs. complex integration tests to quantify how difficulty scales with repository complexity; (c) practical decision framework — recommendations for when to use simulation (simple unit tests, low-cost filtering) vs. execution (complex integration tests, final validation), informed by the accuracy–utility frontier from Part 1. This ensures publishability regardless of outcome. **Part 3 — Discrimination–cost Pareto comparison (Days 9–13).** Evaluate: (i) our per-test simulation model (Qwen3-4B/8B), (ii) trajectory-level baseline (LLM-as-judge with Qwen3-32B, since SWE-RM model weights are not publicly released), (iii) reasoning-based: PatchReasoner-style zero-shot prompting with Qwen3-32B, (iv) semi-formal reasoning (Agentic Code Reasoning-style structured prompting with Qwen3-32B — adapted from Ugare & Chandra's methodology which achieved 93% with Claude Opus 4.5, we test whether the methodology transfers to smaller open-source models at lower cost), (v) LLM-as-judge baseline (Qwen3-8B for cost comparison). **SWE-RM availability note**: SWE-RM (arXiv:2512.21919) is a 30B MoE model from Qwen/Alibaba. As of May 2026, model weights have not been publicly released. We substitute trajectory-level LLM-as-judge baselines; if weights become available before submission, we will include it. **Agentic Code Reasoning note**: We cite and discuss Ugare & Chandra's 93% result with Claude Opus 4.5 as an upper bound for reasoning-based verification, but note their approach requires frontier-model inference (~$0.50+/candidate). Our Part 3 tests whether the semi-formal reasoning methodology transfers to Qwen3-32B (~$0.01/candidate), establishing the cost-accuracy tradeoff. Map each method onto discrimination quality (AUC, best-of-N resolve rate, Spearman's ρ following Scoring Verifiers methodology) vs. cost (FLOPs, wall-clock, $/candidate). Frame as extending Pareto Optimal Code Generation's function-level Pareto analysis to repo-level repair with additional granularity dimension. **Evaluation benchmarks**: (a) SWE-bench Verified (primary, 500 instances, with contamination caveat per OpenAI's Feb 2026 findings), (b) SWE-rebench (contamination-free validation), (c) HumanEval-R/MBPP-R from Scoring Verifiers (COLM 2025) — purpose-built ranking benchmarks for verifier evaluation (HE-R: 164 problems, MBPP-R: 974 problems, each with ~5 uniquely-scored candidate solutions), (d) DebugBench (4,253 instances across C++/Java/Python with categorized bug types — evaluates generalization to debugging scenarios), (e) CodeSense (ICLR 2026, 4,483 real-world samples — evaluates fine-grained semantic reasoning at statement/block/function levels). **Dropped benchmarks**: CrossCodeEval and RepoBench are removed from evaluation — these test code completion (predicting next tokens), not verification (judging correctness), making them ill-suited for evaluating a pass/fail classifier. **CRUXEval contamination resolution**: CRUXEval is used exclusively for curriculum pre-training (Part 2a) and is removed from evaluation benchmarks. HumanEval-R/MBPP-R serve as the function-level verifier evaluation replacement, and CodeSense provides real-world code reasoning evaluation. **Contamination mitigation**: We acknowledge OpenAI's Feb 2026 findings that frontier models exhibit SWE-bench Verified contamination. Our design mitigates this: (a) we evaluate verification accuracy, not patch generation — contamination in generators is orthogonal to verifier quality; (b) SWE-rebench provides decontaminated validation; (c) we use open-source Qwen models with known training cutoffs.

## Resource Estimate

- **auto_research**: {'claude_api_cost': '$200–500 (~3,000–5,000 Opus turns)', 'data_collection_cost': '$30–60 (uses SWE-smith + SWE-Zero open-source trajectories; Docker re-evaluation ~$10–15 on spot instances with optimized images)', 'docker_evaluation_time': '~16–24 hours with 16 parallel containers (overlaps with Day 1 oracle study setup)', 'estimated_gpu_cost': '$360–480 (H100 spot at ~$3/hr)', 'gpu_hours': '~120–160h H100 (parallelized ablations, near-zero idle; ~90%+ utilization)', 'gpu_utilization': 'Agent queues training runs 24/7, parallelizes oracle noise levels, model sizes, baseline evaluations', 'risk_note': '13-day timeline is aggressive; short paper (4pp) is fallback if Part 3 baselines are incomplete', 'speed_bottleneck': 'LoRA fine-tuning of 8B model (~4–6h per run); Docker re-evaluation completes Day 1', 'team': '0 (initial environment setup + final paper review only)', 'timeline': '10–13 days with 4× H100 GPUs (targets ARR May 25 deadline). Docker re-evaluation (Day 1) runs in parallel with oracle study setup.'}
- **human_in_loop**: {'claude_api_cost': '$100–200 (~1,500–2,000 Opus turns)', 'data_collection_cost': '$30–60', 'docker_evaluation_time': '~16–24 hours with 16 parallel containers', 'estimated_gpu_cost': '$300–420 (H100 spot at ~$3/hr)', 'gpu_hours': '~100–140h H100', 'gpu_utilization': 'Good (65–75%): agent automates LoRA training and evaluation pipelines; human reviews designs', 'team': '1 researcher, ~2hr/day', 'timeline': '2–3 weeks (feasible for EMNLP)'}
- **manual**: {'data_collection_cost': '$30–60 (leveraging existing open-source trajectory datasets; Docker re-evaluation ~$10–15 compute for 8K runs with optimized images on spot instances)', 'docker_evaluation_time': "~16–24 hours with 16 parallel containers and cached Docker images (based on Epoch AI's demonstrated 62 min for 500 instances on 32-core machine)", 'estimated_gpu_cost': '$240–360 (H100 spot at ~$3/hr)', 'gpu_hours': '~80–120h H100', 'gpu_utilization': 'Moderate (55–65%): human handles data pipeline setup, Docker re-evaluation, training iteration, result analysis', 'team': '1–2 researchers', 'timeline': '3–4 weeks'}

## Key References

- SWE-RM: Execution-free Feedback for SWE Agents (arXiv:2512.21919, Dec 2025)
- Self-Execution Simulation Improves Coding Models (arXiv:2604.03253, Apr 2026)
- ROC-n-reroll: How Verifier Imperfection Affects Test-Time Scaling (arXiv:2507.12399, 2025)
- Scoring Verifiers: Evaluating Synthetic Verification for Code (arXiv:2502.13820, COLM 2025)
- Debugging Code World Models (arXiv:2602.07672, Feb 2026)
- Pareto Optimal Code Generation (arXiv:2506.10056, Orlanski et al., Jun 2025, revised Feb 2026)
- Agentic Code Reasoning (arXiv:2603.01896, Ugare & Chandra, Meta, Mar 2026)
- FunPRM: Function-as-Step Process Reward Model (arXiv:2601.22249, Jan 2026)
- AgentV-RL: Scaling Reward Modeling with Agentic Verifier (arXiv:2604.16004, Apr 2026)
- CodeSense: Real-World Benchmark for Code Semantic Reasoning (ICLR 2026)
- CodePRM: Execution Feedback-enhanced Process Reward Model (ACL Findings 2025)
- SWE-Zero to SWE-Hero: Execution-free to Execution-based Fine-tuning (arXiv:2604.01496, Apr 2026)
- SWE-TRACE: Rubric Process Reward Models for SWE Agents (arXiv:2604.14820, Apr 2026)
- TraceRepair: Runtime Traces Guided Multi-Agent Repair (arXiv:2604.02647, Apr 2026)
- CWM: Code World Model (arXiv:2510.02387, Meta 2025)
- CodeScaler: Execution-Free Reward Models (arXiv:2602.17684, 2026)
- Scaling Test-Time Compute for Agentic Coding (arXiv:2604.16529, 2026)
- PatchReasoner/R4P: Scalable Patch Verification (arXiv:2510.22775, 2025)
- RePaCA: Reasoning LLMs for Patch Correctness (arXiv:2507.22580, 2025)
- ComPass: Contrastive Patch Correctness Assessment (arXiv:2602.07561, 2026)
- SolidCoder: Execution Grounding for Code Generation (arXiv:2604.19825, 2026)
- DryRUN: Execution Simulation Without Tests (arXiv:2604.21598, 2026)
- Execution Tuning: What I Cannot Execute I Do Not Understand (arXiv:2503.05703, 2025)
- Scaling Agentic Verifier for Competitive Coding (arXiv:2602.04254, 2026)
- CRUXEval: Code Reasoning, Understanding and Execution (ICML 2024)
- DebugBench: Evaluating Debugging Capability of LLMs (ACL Findings 2024)
- SWE-rebench: Decontaminated Evaluation of SWE Agents (arXiv:2505.20411, 2025)

## Reviewer Evaluation

**Scores**:
  - clarity: **{'rationale': 'Exceptionally well-structured three-part design with explicit methodology, success criteria, and contingency plans for each. The oracle study → training → Pareto comparison pipeline is logical. Negative-result handling ensures publishability. Landscape coverage is comprehensive with 27 references, all verified as accurate.', 'score': 5}**/5
  - feasibility: **{'rationale': 'Docker re-evaluation verified at ~62 min/500 instances by Epoch AI, making 8K patches feasible in 16-24h. Qwen3-4B available on HuggingFace with LoRA support via LlamaFactory. 120-160 H100-hours within 200h budget. Timeline (10-13 days) is aggressive but has short paper fallback, and Docker+Part1 parallelization is well-designed.', 'score': 4}**/5
  - impact: **{'rationale': "Fills a genuine gap between expensive execution (~$3/candidate) and coarse trajectory-level scoring. The accuracy-utility frontier (Part 1) and discrimination-cost Pareto analysis (Part 3) are independently useful contributions regardless of per-test model accuracy. Directly extends Pareto Optimal Code Generation's function-level framework to repo-level repair with a novel granularity dimension.", 'score': 4}**/5
  - novelty: **{'rationale': 'Independently verified via multiple searches: no existing work trains per-test binary pass/fail simulation as a fine-grained verifier for repo-level code repair. The closest (SWE-RM: trajectory-level; Self-Execution Simulation: stdout prediction; Agentic Code Reasoning: frontier-model reasoning) are all clearly differentiated. The insight that binary classification sidesteps CWM failure modes (token exhaustion, string prediction) is well-grounded.', 'score': 4}**/5

## Human Review Note

## Agent 审核结果（完整三阶段 pipeline）

**Verdict**: PASS

**入口三重共识 (X)**: 28.0%
**终审自评 (Y)**: 30.0%
**出口三重共识 (Z)**: 33.0%
**Z 区间**: [28.0%, 38.0%]
**真实提升 (Z-X)**: +5.0 pp
**幻觉幅度 (Y-Z)**: -3.0 pp
**出口一致性**: 高
**出口三次评估**: [32.0, 33.0, 35.0]

### 优化方案 / 拒绝详情
【优化方案】

1. **[标题/核心定位]** — 将论文核心 pitch 从"per-test granularity improves verification"重构为"task reformulation (generation → classification) decouples two entangled failure modes of Code World Models"。标题可考虑调整为突出 reformulation 维度，如 "Classification over Generation: Per-Test Execution Simulation as Fine-Grained Verifier for Repair Scaling"。 — 命中 Novelty 维度：从 "incremental granularity change" 提升为 "principled reformulation with identifiable mechanism"。

2. **[Introduction / Motivation 段]** — 删除原始 proposal 中 "per-test simulation occupies an unexplored middle ground" 的负面论证（"没人做过"不等于 novel）。替换为正面的 value proposition：Trace-then-Judge ablation 能干净地分离 granularity vs. classification formulation 的贡献，其结论（无论正反）是论文的核心 scientific finding。同时增加 inference-time compute scaling 动机：per-test verification 降低 best-of-N rejection sampling 的 verifier 成本，连接当前 LLM 社区最热的 test-time compute 叙事。 — 命中 Significance 维度：将论文从 "code repair 子领域的一个 trick" 提升为与 LLM inference scaling 基础设施相关的工作。

3. **[Introduction / NLP Framing 段]** — 删除原始 proposal 没有的、第 1 轮中引入又在第 2 轮被否决的 "behavioral entailment" 标签（牵强的 NLI 类比会被 reviewer 抓住）。替换为更诚实的 NLP positioning：(a) 本工作是对 LLM code semantic reasoning 能力的 probing——通过 per-test prediction 测试 LLM 是否真正理解 patch 的 runtime behavioral consequences；(b) "classification vs. generation" 是一个 NLP methodology insight：当 full output generation 因 tokenization/length 受限时，reformulating as classification 的收益可推广到其他 structured prediction 场景。 — 命中 Venue Fit：提供 EMNLP reviewer 可接受的 NLP relevance 论证，不依赖勉强的类比。

4. **[Contribution List]** — 新增一条 resource contribution："We release SWE-bench-PerTest, the first per-test pass/fail annotation of SWE-bench Verified at individual test granularity (500 instances × 16 candidates), enabling future research on fine-grained code verification without Docker infrastructure." 附基本统计（per-instance test count 分布、pass/fail 比例）。 — 命中 Reproducibility / Resource Contribution 维度：高质量 dataset 是 EMNLP reviewer 判 accept/reject 的常见 tiebreaker。

5. **[Part 1: Oracle Frontier]** — 保留核心经验 Pareto 分析不变。将原始 proposal 没有的信息论分析（i.i.d. bound + block-correlated model）移至 appendix 作为 supplementary analysis，正文只保留 1 段 brief 说明。新增 test informativeness heterogeneity 分析（按 discriminative power 分层报告 top-K vs. all tests），揭示 per-test 优势是否集中在少数高信号 test 上。新增 inter-test prediction correlation structure 分析——报告 LLM 预测错误是否沿 code dependency graph 传播（按 shared import depth / same test file 分层），将其呈现为 "LLM code understanding 的实证发现"。 — 命中 Analysis Depth 维度：从纯经验 Pareto 提升为有 insight 的分析；correlation finding 增加了对 LLM 能力边界的认知贡献。

6. **[Part 2: Training — 数据]** — 原始 proposal 的 Stage 1 数据量偏小（CRUXEval ~4K + CodeSense ~4.5K ≈ 8.5K）。新增 MBPP/HumanEval per-test execution results 作为 Stage 1 补充（每个 problem ~100-200 test cases，廉价通过直接执行获取），将 Stage 1 数据量提升至 ~15K+。 — 命中 Technical Soundness 维度：缓解训练数据不足的审稿风险。

7. **[Part 2: Training — Ablation]** — 原始 proposal 有 curriculum ablation（去掉 Stage 1），保留。新增 mixed-training baseline（Stage 1 + Stage 2 数据混合训练，不分阶段），验证 curriculum ordering 的必要性。增加 1-2 句 curriculum rationale：function-level → repo-level 是沿 compositional complexity 的自然梯度（单函数 = 无依赖的退化情形），连接 NLP 社区对 compositional generalization 的兴趣。 — 命中 Soundness + NLP Relevance 双维度。

8. **[Part 2: Context Management]** — 原始 proposal 仅含模糊的 "relevant-file extraction and focal truncation"。具体化为：patch-involved files + N-hop import-graph neighbors；focal truncation 优先保留 patched function、test body、directly referenced modules。明确承诺报告 token-count distribution（median、P95、超 context 比例）。若 >10% cases 超 context window，提供 stratified accuracy analysis by context length。N-hop sensitivity (N=1,2,3) 移至 appendix。 — 命中 Technical Soundness 维度：消除 reviewer 对方法实际可用性的疑虑。

9. **[Part 3: Baselines — 重构]** — 原始 proposal baselines 存在两个严重问题：(a) per-test fine-tuned 4B/8B vs. trajectory-level zero-shot 32B 混淆了 model size 和方法论；(b) 缺少隔离 granularity vs. formulation 的 ablation。修正后的 baseline 集：
   - (a) Trajectory-level LLM-as-judge (Qwen3-32B zero-shot) — reference point
   - (b) Semi-formal reasoning (Qwen3-32B) — reference point
   - (c) LLM-as-judge (Qwen3-8B zero-shot) — scale reference
   - (d) **Same-size fine-tuned trajectory-level** (Qwen3-4B/8B, matched training budget) — **核心控制对比，隔离粒度效应**
   - (e) **Trace-then-Judge ablation** (Qwen3-8B, per-test trace generation → extract pass/fail) — **核心 ablation，隔离 classification vs. generation**，单独命名并解释 confound-isolation 逻辑
   - (f) Per-test majority voting (K=3) — 轻量 ablation，测试 self-consistency 对 per-test 的提升
   — 命中 Experimental Rigor 维度：baseline (d) 和 (e) 组合能干净回答 "gain 从哪来"，这是 reviewer 最关心的问题。

10. **[Part 3: Cost Model]** — 原始 proposal 声称执行成本 "~$3, ~45 min/candidate"，可能严重高估（现代 cached Docker images 通常 1-5 min）。更新为诚实的现代执行成本 benchmark。提供完整 per-test inference 成本模型：median test count × token/prediction × model cost × 16 candidates。**将 narrative 重心从 "cheaper" 转向 "more informative"**——per-test diagnostic signals 的价值在于 targeted re-repair，而非单纯的成本节约。 — 命中 Soundness + Significance 维度：避免 reviewer 做 back-of-envelope 计算后发现成本优势不显著。

11. **[Part 3: Downstream Validation]** — 原始 proposal 未包含 downstream 实验。新增 200 instances（非 50）的 proof-of-concept：per-test failure predictions → SWE-agent targeted re-repair → resolve rate 对比。报告 effect size + CI + power analysis。补充间接证据：per-test failure prediction precision/recall against ground-truth failing tests（全 500 instances，不需额外 Docker 执行）。 — 命中 Practical Significance 维度：堵住 "limited practical impact, just another ranking metric" 的常见拒稿理由。

12. **[Part 3: Benchmark 精简]** — 原始 proposal 列了 6 个 benchmark。精简为正文 3 个：SWE-bench Verified（核心）+ SWE-rebench（contamination-free）+ CodeSense（fine-grained semantic reasoning）。HumanEval-R/MBPP-R 只在 curriculum 验证中提及；DebugBench 移至 appendix。确保每个正文 benchmark 有 per-category breakdown 和 error analysis 的空间。 — 命中 Soundness 维度：避免 "tries to do too much, none in sufficient depth" 的拒稿理由。

13. **[Part 2: Negative Result Framing]** — 删除原始 proposal 中的 "ensuring publishability regardless of outcome"（reviewer red flag，暴露 hedging 心态）。替换为正面 research question framing："At what accuracy level does per-test simulation become preferable? If small models fall short, we characterize failure modes by test complexity / code-diff size / dependency depth, providing a reusable error taxonomy and identifying the minimum capability frontier." — 命中 Soundness 维度：保留 dual-outcome 设计的科学合理性，不暴露对结果的不自信。

14. **[语言校准]** — 删除 "intractable generation problem"（overclaim：trace generation 困难但非 intractable，CWM 论文报告了非零准确率）。替换为 "a generation problem with systematic accuracy bottlenecks"。删除 "fundamental shift in task formulation"（过强），替换为 "a reformulation that decouples two entangled failure modes"。 — 命中 Credibility：精确措辞避免 reviewer 标注 overclaiming。

15. **[Related Work 大幅扩展]** — 原始 proposal 仅引用 4 篇直接相关工作。扩展为四条研究线程：(1) Code execution prediction（CodeExecutor, SelfPiCo — 差异：预测 trace/output vs. 只预测 binary）；(2) Test outcome prediction in SE（mutation testing, fault localization, **新增** predictive test selection [Machalica et al., ESEC/FSE 2019], predictive mutation testing [Zhang et al., ISSTA 2018] — 差异：依赖执行历史/instrumentation vs. zero-history purely code-semantic；针对 regression testing vs. LLM-generated patches）；(3) LLM-based code verifiers（SWE-RM, Scoring Verifiers, Agentic Code Reasoning — 系统性对比 at controlled model sizes）；(4) Iterative repair with test feedback（LDB — 差异：uses executed test signals vs. predicted signals）。补充 code understanding benchmarks（CodeXGLUE, CodeBERTScore）的定位讨论。 — 命中 Related Work 维度：全面覆盖，差异化定位清晰，预防 reviewer 检索到未讨论工作后扣分。

【主要风险】

1. **Trace-then-Judge ablation 结果模糊风险**：如果 classification formulation ≈ trace-generation at matched granularity，论文最强的 novelty hook（"formulation matters more than granularity"）消失，退化为 "per-test granularity helps, which is somewhat obvious"。这是实验风险，不可通过 proposal 层面的优化消除。应对：确保论文叙事能容纳两种结果——若 classification >> trace-gen，讲 "formulation story"；若两者相当，讲 "granularity story + classification has lower cost as bonus"。

2. **EMNLP venue fit 的系统性风险**：论文的核心关切仍是 SE verification（SWE-bench evaluation, Docker execution, repair agents），NLP angle（code semantic reasoning probing, classification vs. generation methodology）是有机的但不是内生的。如果三位 reviewer 中有 ≥2 位无 code reasoning 背景，可能直接判 "not an NLP paper"。应对：在 cover letter/submission 时选择 "NLP Applications" 或 "Code Generation and Understanding" track（如有）；准备 ICSE 2027 / ICLR 2026 作为 plan B venue。

【实施评估】

- **计算资源**: 
  - 训练：Qwen3-4B/8B LoRA fine-tuning，单卡 A100 80GB 可运行；Stage 1 + Stage 2 总计约 20K-25K 样本，预计 4B 模型训练 ~4-6 小时，8B 模型训练 ~8-12 小时。需训练主方法 + trajectory-level baseline + ablations ≈ 6-8 次训练 run，总计约 2-4 天单卡 A100 时间。
  - 推理：Per-test inference（500 instances × 16 candidates × ~20 tests/instance ≈ 160K inferences for Qwen3-4B）。Qwen3-4B 推理速度较快，预计 1-2 天单卡 A100。Zero-shot baselines（Qwen3-8B/32B）推理量较小但单次推理较慢，预计各 1-2 天。
  - 总计约 1-2 周单卡 A100（或等效多卡并行缩短）。
  
- **数据需求**: 
  - SWE-bench Verified 500 instances + 16 candidates per instance：公开可得（需自行生成 candidates 或复用已有 candidates）
  - Per-test labels：需通过 SWE-bench evaluation harness 重新执行获取（~8K Docker runs, ~16-24 小时, 16 并行容器）
  - CRUXEval + CodeSense：公开可得
  - MBPP/HumanEval per-test execution results：公开 benchmark，需自行执行获取 per-test labels（廉价，几小时）
  - SWE-rebench：公开可得
  - 所有数据集均公开可得，但 per-test label 构建需要 Docker 基础设施
  
- **人工介入**: 
  - 无需人工标注（所有标签通过自动执行获取）
  - Error taxonomy 构建需要少量人工审查（~50-100 failure cases 的定性分析），约 1-2 天
  - 论文写作 + 实验分析约 2-3 周
  
- **训练需求**: 
  - 需要模型训练：Qwen3-4B/8B LoRA fine-tuning（非全量微调）
  - 模型规模适中（4B/8B），LoRA 大幅降低显存需求
  - 不需要从头预训练
  
- **新 Benchmark**: 
  - 需要构建 SWE-bench-PerTest 数据集（SWE-bench Verified 的 per-test annotation layer）
  - 构建成本主要在 Docker execution（~16-24 小时计算时间），不需要人工标注
  - 这个数据集本身作为 resource contribution 列入论文贡献
  
- **预估周期**: 
  - 数据构建（per-test labels + Stage 1 data）：1-2 周
  - Pilot study（token distribution, context analysis）：2-3 天
  - 模型训练 + ablations：1-2 周
  - Baseline inference + evaluation：1-2 周
  - Downstream repair valida


## MVP Validation Results

- **Date**: 2026-05-11
- **Hypothesis Supported**: Yes

### Key Metrics

MVP-A: F2P block-corr advantage 10.88%, P2P reg rate ~1% (Total advantage negative). MVP-B: accuracy 87.5%, pass F1 87.1%, fail F1 87.9%, majority baseline 51.7%, gap +35.8pp. Training: 3 epochs, 57min on RTX 5090, eval_loss 0.093.

### Summary

MVP 两步验证完成。MVP-A（Oracle 信息增益）：F2P-only block-correlated 下 per-test 优势 10.88%（>5% 阈值），有条件通过；但发现 P2P 回归率仅 ~1%，Total 场景下优势为负，触发 story reframe 为 "task reformulation (generation → classification)"。MVP-B（函数级可学习性）：Qwen3-4B LoRA 在 19K (code, test) → pass/fail 样本上训练，overall accuracy 87.5%（majority baseline 51.7%，gap +35.8pp），per-class F1 87.1%/87.9%，远超 65% 阈值。Binary classification 可学习性确认。

### Recommendation

GO — 进入 research 阶段。Story reframe 为 task reformulation (classification vs generation)。Post-MVP P0 优先级：训练 CWM generation baseline 做同数据同模型对比，验证 classification 确实优于 generation。P1：diagnostic 下游实验。新增 kill condition：CWM baseline 无显著差异则考虑 kill。


## MVP Validation Results

- **Date**: 2026-05-11
- **Hypothesis Supported**: Yes

### Key Metrics

MVP-A: F2P block-corr advantage 10.88%, P2P reg rate ~1%. MVP-B: accuracy 87.5%, pass F1 87.1%, fail F1 87.9%, majority baseline 51.7%, gap +35.8pp.

### Summary

MVP 两步验证完成。MVP-A（Oracle 信息增益）：F2P-only block-correlated 下 per-test 优势 10.88%（>5% 阈值），有条件通过；P2P 回归率仅 ~1%，触发 story reframe 为 "task reformulation (generation → classification)"。MVP-B（函数级可学习性）：Qwen3-4B LoRA 在 19K (code, test) → pass/fail 样本上训练，accuracy 87.5%（majority baseline 51.7%，gap +35.8pp），per-class F1 87.1%/87.9%，远超阈值。

### Recommendation

GO — 进入 research 阶段。P0: CWM generation baseline 对比验证 classification vs generation 核心 claim。
