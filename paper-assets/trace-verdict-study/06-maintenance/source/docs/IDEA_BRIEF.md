# Idea Brief: Verdict-Optimized Trace Abstraction: When Execution Semantics Help Code Behavior Classification but Not Generation


- **Idea ID**: `idea_009`
- **Created**: 2026-05-14
- **Approved**: 2026-05-14
- **Source**: foreign:be-idea-gen-0509-5
- **Level**: top-tier
- **Target Venues**: EMNLP 2026 (ARR submission deadline: May 25, 2026; commitment deadline: August 2, 2026; conference: October 24–29, 2026, Budapest)

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

## Generation Journey

1. **Start** — 开始生成，seed: 'Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Machine Learning for NLP / Resources and Evaluation. Aligns with EMNLP 2026 special theme "New Missions for NLP Research" which explicitly calls for work on data contamination, synthetic data feedback loops, and data governance.\n\nDirection: Synthetic data quality, model collapse prevention, contamination detection. In-scope: synthetic data verification/filtering methods, detecting training data contamination in benchmarks, methods to break recursive data feedback loops, data mixing strategies that prevent quality degradation, principled synthetic data generation with quality guarantees.\n\nContribution type: METHOD ONLY. Must propose a concrete detection algorithm, filtering pipeline, or training recipe — not just an observation about model collapse. Method + analysis OK.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Model collapse experiments need multiple training iterations — budget for small models (1B-3B) across 3-5 generations.\n2. Time: ≤16 days. Use small open models (Pythia, OLMo-1B, Qwen-0.5B/1.8B) for iterative collapse experiments.\n3. Eval: perplexity degradation curves, downstream task quality (MMLU, HellaSwag), diversity metrics (self-BLEU, n-gram entropy), contamination detection accuracy.\n\nThis is a hot EMNLP 2026 special theme area with relatively few established methods — high novelty potential.\n\nTag: direction=data_governance, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].'
2. **Problem Discovery** (325s) — 发现 4 个研究方向
   - Training-Time Early Warning Signals for Model Collapse
   - Generational Depth Fingerprinting for Synthetic Text Triage
   - Diversity-Calibrated Verification for Collapse-Resistant Synthetic Data
   - Collapse-Aware Adaptive Mixing for Synthetic-Real Training
3. **Method Synthesis** (287s) — 完成: "Training-Time Early Warning Signals for Model Collapse" [top-tier] → EMNLP 2026 (ARR submission May 25, 2026 — special theme: Data as a Bottleneck and a Responsibility), AAAI 2027 (expected deadline ~August 2026)
3. **Method Synthesis** (779s) — 完成: "Generational Depth Fingerprinting for Synthetic Text Triage" [solid] → EMNLP 2026 (ARR deadline: May 25, 2026), AAAI 2027 (paper deadline: August 2, 2026), ICLR 2027 (paper deadline: September 24, 2026), NAACL 2027 (ARR deadline: October 16, 2026), EACL 2027 (ARR deadline: October 16, 2026)
3. **Method Synthesis** (557s) — 完成: "Diversity-Calibrated Verification for Collapse-Resistant Synthetic Data" [solid] → EMNLP 2026 (ARR deadline: May 25, 2026), AACL-IJCNLP 2026 (ARR deadline: May 25, 2026), AAAI 2027 (abstract: July 25, 2026; paper: August 1, 2026)
3. **Method Synthesis** (616s) — 完成: "Collapse-Aware Adaptive Mixing for Synthetic-Real Training" [solid] → EMNLP 2026 (ARR submission deadline: May 25, 2026), AAAI 2027 (paper deadline: August 1, 2026), NeurIPS 2026 Workshops (suggested submission: August 29, 2026), ICLR 2027 (estimated deadline: September-October 2026, not yet announced)

## Core Problem

"Do Code Semantics Help?" (EMNLP Findings 2025, arXiv 2509.11686) concluded that execution trace-based SFT provides limited benefit for Code LLMs, finding it fails to improve code synthesis in 7/9 configurations and yields inconsistent results for CRUXEval reasoning tasks. TracePile (NeurIPS 2025, arXiv 2510.23629) scaled trace SFT to 2.6M samples across four base models and 20 benchmarks, achieving strong gains on math and code reasoning — but evaluated only generative tasks. Across all existing trace SFT studies, every task requires generating exact outputs: complete programs, precise I/O values, repaired code, or mathematical derivations. We ask: does trace SFT help for code behavior verdict tasks — binary/categorical predictions about execution outcomes (pass/fail, correct/incorrect, buggy/clean) — where the output space is fundamentally constrained? Moreover, can a trace representation specifically designed for classification (capturing only decision-relevant execution states) outperform trace formats designed for full execution simulation? This distinction — verdict prediction with task-optimized trace representation vs. open generation with simulation-oriented traces — has not been systematically investigated.

## Opportunity / Why Now

Four converging lines of evidence suggest trace SFT may differentially benefit verdict tasks over generation, and that a task-optimized trace representation can amplify this benefit. First, SemCoder (NeurIPS 2024) demonstrates that trace-supervised training teaches genuine behavioral understanding (63.6% CRUXEval-I vs. 50.3% for Code Llama 34B). Second, TracePile (NeurIPS 2025) shows that even at 2.6M-sample scale, trace SFT has only been applied to generative tasks — the classification regime is entirely untested. Third, TRACED (ICSE 2024) provides a precedent from the pre-training paradigm: execution-aware pre-training significantly improves encoder-model performance on classification tasks (vulnerability detection, clone retrieval), suggesting that execution understanding transfers to classification — but nobody has tested this for decoder SFT. Fourth, "Debugging Code World Models" (arXiv 2602.07672) identifies token-budget exhaustion as a dominant failure mode in dense trace representations, motivating our design of a compact, verdict-focused trace format.

The practical stakes are high: automated patch correctness assessment (APCA) plateaus at ~88% accuracy (ComPass: 88.35%, Historian: 88.4%) using purely static features, test outcome prediction is increasingly critical for efficient CI/CD, and bug detection accuracy determines triage quality. An ensemble combining trace-SFT behavioral analysis with static approaches could break the 90% APCA barrier — a concrete practical headline. The study design ensures publishable value regardless of outcome: if our Verdict-Optimized Trace Abstraction (VOTA) helps for verdict tasks, we contribute both a novel trace representation and a new task regime where code semantics help; if it doesn't, we strengthen and extend the DCSH negative finding with quantitative calibration analysis explaining WHY traces fail across the full task spectrum.

## Landscape (SOTA & Limitations)

Trace SFT for Code LLMs: "Do Code Semantics Help?" (EMNLP Findings 2025, arXiv 2509.11686) is the central prior work. Testing five trace representations (Scratchpad, NExT, SemCoder, CodeExecutor, Concise) across DeepSeek-Coder-6.7B, LLaMA-3.1-8B, and Gemma2-9B, they found trace SFT fails for code synthesis (7/9 configs), yields marginal gains for program repair (+0.3–1.4 pts with SemCoder only), and shows inconsistent CRUXEval results. Crucially, all their tasks are generative — no verdict/classification tasks were evaluated, and their trace representations were designed for execution simulation, not classification. TracePile (arXiv 2510.23629, NeurIPS 2025) represents the largest-scale trace SFT effort: 2.6M Chain of Execution (CoE) samples across LLaMA 3, LLaMA 3.1, Qwen-2.5, and Qwen-2.5 Coder, evaluated on 20 benchmarks covering math, code, logic, and algorithms. It achieves strong gains (e.g., Qwen-2.5-7B CRUXEval: 23.5% → 49.4%) but exclusively targets generative tasks — verdict/classification tasks are absent from their evaluation, reinforcing our gap. SemCoder (arXiv 2406.01006, NeurIPS 2024) trains on monologue-style NL execution descriptions and achieves strong CRUXEval gains, showing trace training CAN teach behavioral understanding. Execution Tuning (E.T., arXiv 2503.05703, 2025) achieves ~80% on CRUXEval-O with dynamic scratchpads but requires traces at inference time — we aim to internalize this capability via SFT. ExecVerify (arXiv 2603.11226, 2026) uses white-box RL rewards from execution traces, enabling 7B ≈ 32B on reasoning benchmarks. "Code Execution as Grounded Supervision" (arXiv 2506.10343, EMNLP 2025) extracts verifiable CoT from code execution for general reasoning. Self-Execution Simulation (arXiv 2604.03253, 2026) trains on NL traces + RL for competitive programming self-verification (+5.5% via best-of-k).

Execution Traces for Code Classification (Pre-training Paradigm): TRACED (arXiv 2306.07487, ICSE 2024) is an important precedent: it pre-trains code language models with source code, executable inputs, and execution traces, then fine-tunes on downstream classification tasks including vulnerability detection and clone retrieval, significantly outperforming statically pre-trained models. This demonstrates that execution understanding transfers to classification. However, TRACED uses encoder-based pre-training (not decoder SFT), operates at the pre-training stage (not task-specific SFT), and does not test on verdict tasks (pass/fail, patch correctness). Our work extends this insight to the decoder SFT paradigm and tests it systematically on code behavior verdict tasks.

Correctness Signals in Code SFT: FGIT (arXiv 2503.16913, ASE 2025) uses correct/incorrect code signal during SFT with dynamic loss weighting on error-sensitive segments, achieving 6.9% relative improvement on pass@1 for code generation. While technically different (loss reweighting for generation, not trace-supervised classification), it occupies a conceptually adjacent space: leveraging fault information to improve code SFT. Our approach differs in both objective (classification vs. generation) and mechanism (trace-grounded reasoning vs. loss reweighting).

Automated Patch Correctness Assessment (APCA): ComPass (arXiv 2602.07561, 2026) achieves 88.35% accuracy on Defects4J via contrastive learning on BERT representations — purely static. Historian (arXiv 2603.00649, 2026) achieves 88.4% accuracy with 95.0% coverage by comparing patches against historically validated fixes — also static. APSG/Graph-LoRA (arXiv 2505.02629, 2025) reaches 85.8–96.8% via attributed semantic graphs + LLaMA3 fine-tuning. RePaCA (arXiv 2507.22580, 2025) uses reasoning LLMs with generic CoT at 83.1%. LLM4PatchCorrect (TSE 2024) is the closest existing work: it uses execution traces as in-context learning input for StarCoder, achieving 84.4% accuracy — but requires traces at inference time (expensive), while we internalize trace reasoning via SFT. Shibboleth (ISSTA 2022) achieves 88.7% but requires test execution at inference. APPT (TSE 2024) uses BERT+LSTM at 79.7%. No existing APCA method uses trace-supervised SFT with a verdict-optimized trace representation.

Calibration of Code LLMs: Spiess et al. (arXiv 2402.02047, ICSE 2025) establish the first calibration framework for code-generating models, finding they are poorly calibrated out-of-the-box and that Platt scaling helps. However, they study calibration only for generation tasks. "Do Code Semantics Help?" (Table 7) observed that trace SFT boosts prediction confidence without increasing correctness for generative tasks. We hypothesize this overconfidence effect is beneficial for classification (sharper decision boundaries) while harmful for generation (confidently wrong outputs), and we operationalize this with ECE, Brier score, and reliability diagrams — the first quantitative calibration analysis of trace SFT across the verdict-generation spectrum.

Benchmarks: CRUXEval (arXiv 2401.03065, ICML 2024) provides 800 Python functions for execution prediction. LiveCodeBench (arXiv 2403.07974) offers contamination-free code evaluation. DebugBench (2024) has 4,253 instances across C++/Java/Python with 18 bug types. CrossCodeEval (arXiv 2310.11248, NeurIPS 2023) evaluates cross-file code completion across 4 languages. RepoBench (arXiv 2306.03091, ICLR 2024) evaluates repository-level code completion; we exclude it because (a) it is a generation benchmark with no verdict-task variant, (b) CrossCodeEval already serves as our cross-file generation baseline, and (c) our study's contribution centers on verdict tasks where RepoBench offers no additional signal. Defects4J provides 2,274 labeled patches for APCA evaluation.

Key gap: No prior work has (1) designed a trace representation specifically optimized for code behavior classification, or (2) systematically compared trace SFT effectiveness across verdict-classification-generation task spectrum with quantitative calibration analysis. DCSH covers generation only. TracePile scales trace SFT but evaluates only generation. TRACED shows traces help classification via pre-training encoders, but doesn't test decoder SFT on verdict tasks. LLM4PatchCorrect uses traces for APCA via ICL, not SFT. We fill all three gaps simultaneously.

## Proposed Approach

We propose Verdict-Optimized Trace Abstraction (VOTA), a novel execution trace representation designed specifically for code behavior classification, and conduct a systematic empirical study demonstrating when and why trace SFT helps across the verdict–prediction–generation task spectrum.

**Method Contribution: VOTA Trace Representation.** Existing trace formats (Scratchpad, NExT, SemCoder, CodeExecutor, Concise from DCSH; CoE from TracePile) are designed for full execution simulation — capturing every variable state, every loop iteration, every line of execution. This is appropriate for generation tasks that require exact output prediction, but excessive for verdict tasks where the model only needs to determine whether code behaves correctly. VOTA is designed around the principle that verdict tasks require only decision-relevant execution states:
• Assertion-point variable snapshots: Capture variable states only at test assertion points and function entry/exit boundaries, not at every line. For a test with 5 assertions, this yields ~5 state snapshots vs. potentially hundreds for full-trace formats.
• Exception summaries: Type + message + triggering line only, not full stack traces. Captures the diagnostic signal while discarding syntactic noise.
• Loop compression: First iteration state, last iteration state, iteration count, and any iteration where state diverges from the pattern. This directly addresses the token-budget exhaustion failure mode identified by Debugging CWM (arXiv 2602.07672).
• Collection boundaries: For lists/dicts/sets, capture size + first/last elements + any elements referenced in assertions, not full contents.
• Behavioral delta format: For patch correctness tasks, VOTA additionally captures a behavioral diff — how the patched code's execution states differ from the original at assertion points — directly encoding the information most relevant to the correct/overfitting verdict.

The design is motivated by an information-theoretic argument: verdict tasks have O(1) output entropy (1 bit for binary, log₂k bits for k-way classification), so the trace should contain only the information needed to determine that output, not the full O(n) execution simulation. We systematically ablate VOTA against all 5 DCSH trace representations (Scratchpad, NExT, SemCoder, CodeExecutor, Concise) on each task type to validate this design.

**Task Taxonomy.** We define three categories by output space constraint: (1) Verdict tasks — binary/categorical judgments: patch correctness (correct/overfitting), test outcome prediction (pass/fail), bug detection (buggy/clean). (2) Constrained prediction — generating specific values: CRUXEval-O, LiveCodeBench test output prediction. (3) Open generation — producing arbitrary code: HumanEval, MBPP, CrossCodeEval. Our hypothesis: VOTA provides maximal benefit for verdict tasks, moderate benefit for constrained prediction, and no benefit (or harm) for generation — and this gradient is explained by calibration dynamics.

**Data Construction & Trace Collection (~35h wall-clock, CPU-bound, parallelizable).**
• APCA-Defects4J: 2,274 labeled patches (1,169 correct, 1,105 overfitting). Apply each patch, run relevant tests (~10–20/patch) with JUnit instrumentation capturing variable states at assertion points, exception types, and loop counts. Generate both VOTA format (assertion-point snapshots + behavioral deltas) and SemCoder-style full NL monologues (for controlled comparison). Augment with PraPatch (1,988 patches). ~30h wall-clock on 4-core machine.
• TestVerdict-HumanEval/MBPP: Generate 10 solutions per problem using Qwen2.5-Coder-32B-Instruct (mix of correct and incorrect). Run each against test cases with Python sys.settrace instrumentation. ~664 problems × 10 solutions = ~6,640 (solution, test, trace, pass/fail) examples. ~3h wall-clock.
• BugDetect-DebugBench: Take 4,253 buggy programs + their correct versions. Run both on LeetCode test cases with trace instrumentation. ~8,500 (program, trace, buggy/clean + bug_type) examples. ~2h wall-clock.
• CRUXEval traces: 800 Python functions, instrument execution with sys.settrace. ~1h wall-clock.

**Trace Abstraction (GPU, ~20–25h H100).** Convert raw traces to six formats for systematic comparison:
(1) VOTA (our proposed format): assertion-point snapshots + exception summaries + loop compression + collection boundaries + behavioral deltas.
(2–6) Five DCSH formats reproduced: Scratchpad, NExT, SemCoder, CodeExecutor, Concise — using Qwen2.5-72B-Instruct for NL conversion following DCSH methodology.
This six-way comparison is the core ablation that validates VOTA as a novel trace representation.

**Trace-Supervised SFT (GPU, ~80–90h H100).** Fine-tune two base models with LoRA (rank 32, alpha 64):
• Qwen2.5-Coder-7B-Instruct (primary, strong code model)
• DeepSeek-Coder-6.7B-Instruct (for direct comparison with DCSH which used this model)

Training format by task type:
• Verdict tasks: input = (code + test + instruction) → output = (trace reasoning in [VOTA | comparison format] + verdict label). The model learns to generate execution-grounded chain-of-thought before predicting the verdict.
• CRUXEval-O: input = (function + input value) → output = (trace reasoning + predicted output). Matches DCSH protocol.
• Generation tasks: standard SFT without trace supervision (replication of DCSH setup).

Training configurations: For each of the 2 models × 6 trace formats × 3 verdict tasks = 36 verdict-task runs, plus 2 models × 6 formats × 2 constrained-prediction tasks = 24 constrained-prediction runs, plus 2 models × 3 generation baselines = 6 generation runs. Total: 66 training runs. We train separate LoRA adapters per configuration to isolate effects, plus a multi-task VOTA model trained on all verdict tasks jointly.

**Go/No-Go Pilot (GPU, ~8h H100).** Before committing full resources, we run a rapid pilot: train on 20% of APCA-Defects4J data with VOTA vs. SemCoder vs. no-trace baseline, evaluate on held-out fold. Decision criteria: (a) If VOTA shows ≥2% improvement over no-trace and ≥1% over SemCoder, proceed with full experiments in positive-result framing; (b) If trace SFT shows no improvement for verdicts, shift to negative-result framing with emphasis on calibration analysis explaining WHY.

**Evaluation Protocol.**
• Verdict tasks: accuracy, precision, recall, F1 with bootstrap 95% confidence intervals (10,000 resamples). McNemar's test for pairwise comparison with baselines. For APCA: 5-fold cross-validation matching ComPass's protocol.
• CRUXEval-O: pass@1, matching DCSH protocol exactly.
• LiveCodeBench test output prediction: pass@1 on problems after model training cutoff.
• Generation tasks (HumanEval, MBPP, CrossCodeEval): pass@1 / exact match / edit similarity, replicating DCSH.

**Core Analyses — Five Primary Contributions.**

(1) VOTA Trace Format Ablation (METHOD contribution): Systematic comparison of VOTA against all 5 DCSH trace representations on each task type. We measure: (a) accuracy/pass@1 per format per task, (b) token efficiency (average trace length in tokens), (c) accuracy-per-token metric showing VOTA achieves better accuracy with fewer tokens for verdict tasks. If VOTA outperforms full-simulation formats on verdict tasks while using 3–5× fewer tokens, this validates the design principle that verdict tasks need decision-relevant states, not full simulation.

(2) Quantitative Calibration Analysis (FINDING contribution): We operationalize the DCSH overconfidence observation with rigorous calibration metrics. For each model × trace format × task configuration, we measure: (a) Expected Calibration Error (ECE) with 15 equal-width bins, following Spiess et al. (ICSE 2025) methodology; (b) Brier score decomposition (reliability + resolution + uncertainty) to isolate whether trace SFT improves discrimination or just shifts confidence; (c) reliability diagrams plotting observed accuracy vs. predicted confidence, comparing trace-SFT vs. no-trace models on verdict tasks and generation tasks; (d) confidence distribution histograms showing how trace SFT reshapes the prediction confidence landscape. The testable prediction: trace SFT decreases ECE for verdict tasks (sharpens decision boundaries → better calibration for binary outcomes) while increasing ECE for generation tasks (overconfident wrong predictions). If confirmed, this provides a mechanistic explanation for the DCSH finding and identifies the task-regime boundary.

(3) Task-Spectrum Analysis (EMPIRICAL contribution): Plot trace SFT improvement (Δ accuracy/pass@1) vs. output space constraint across all tasks, using both VOTA and the best DCSH format. Test the hypothesis that benefit monotonically decreases as output space expands: verdict > constrained prediction > generation.

(4) APCA Ensemble — Breaking the 88% Plateau (PRACTICAL contribution): Error-type analysis showing VOTA-SFT catches behaviorally incorrect patches (execution divergence at assertion points) that static methods (ComPass, Historian) miss, and vice versa. Concrete ensemble configurations: (a) majority vote (VOTA-SFT + ComPass + Historian), (b) learned stacking (logistic regression on the three models' predictions), (c) confidence-weighted ensemble using calibrated probabilities from (2). Target: >90% accuracy on Defects4J, breaking the ~88% plateau. This is positioned as a primary headline result: behavioral + static complementarity yields practical APCA improvement.

(5) SFT Internalization vs. ICL (EFFICIENCY contribution): Head-to-head with LLM4PatchCorrect showing our SFT internalization achieves competitive or better accuracy while requiring no traces at inference time. We measure inference-time speedup (no trace collection overhead) and accuracy comparison.

**Additional Ablations:** (a) LoRA rank (16/32/64), (b) training data size curves (10%/20%/50%/100%), (c) VOTA component ablation (remove each component: assertion-point snapshots, loop compression, behavioral deltas) to validate 

## Resource Estimate

- **auto_research**: {'claude_api_cost': '$200–$400 (Opus, ~3000–5000 turns for autonomous experiment loop)', 'estimated_gpu_cost': '$630–$750', 'gpu_hours': '~210–250h H100 (comprehensive: 2 models × 6 trace formats × 6+ tasks; full calibration analysis with ECE/Brier/reliability diagrams; APCA ensemble search; component ablations)', 'gpu_utilization': 'High (~80–90%). Agent pipelines: trace collection → 6-format generation → pilot → SFT grid → evaluation → calibration analysis → ensemble optimization. Parallel experiment queues across task types.', 'risk_note': "If pilot shows trace SFT doesn't help for verdict tasks, the paper pivots: 'Code semantics don't help even for classification — and here's why (calibration analysis).' The VOTA format comparison and calibration analysis remain valuable contributions regardless. Both framings publishable at EMNLP.", 'speed_bottleneck': 'Defects4J trace collection is CPU-bound (~30h wall-clock on 4-core); parallelizable across projects. The 66-configuration SFT grid is the GPU bottleneck but highly parallelizable across GPUs.', 'team': '0 (initial setup: ~4–6h for Defects4J environment, Python instrumentation, benchmark downloads)', 'timeline': '12–14 days with 2–4× H100 (fits May 25 ARR deadline)'}
- **human_in_loop**: {'claude_api_cost': '$150–$300 (Opus, ~1500–3000 turns)', 'estimated_gpu_cost': '$540–$630', 'gpu_hours': '~180–210h H100 (adds systematic 6-format ablation grid, full calibration analysis suite, ensemble optimization)', 'gpu_utilization': 'Moderate (~55–65%). Agent handles trace collection, SFT pipeline, evaluation. Human reviews pilot results (go/no-go on day 3–4), validates VOTA design choices, and guides calibration analysis interpretation.', 'risk_note': 'Go/no-go pilot on day 3–4 determines positive vs. negative-result framing. VOTA component ablation on day 5–6 validates the trace representation design. Human judgment critical for both decisions.', 'team': '1 researcher, ~30–45min/day check-in for pilot review, VOTA design validation, and calibration analysis direction', 'timeline': '13–15 days (tight for May 25 ARR deadline but feasible with 2× H100)'}
- **manual**: {'estimated_gpu_cost': '$480–$570 (at ~$3.00/hr H100)', 'gpu_hours': '~160–190h H100 (NL trace generation in 6 formats: ~20–25h; LoRA SFT for 66 configurations: ~80–90h; evaluation across 8 benchmarks: ~20–25h; calibration analysis + ablations: ~40–50h)', 'gpu_utilization': 'Low-moderate (~35–45%). GPUs idle during trace collection (CPU-bound), trace abstraction prompt engineering, calibration analysis, and paper writing.', 'team': '1 researcher', 'timeline': '20–24 days (exceeds ARR deadline — manual execution not recommended)'}

## Key References

- Do Code Semantics Help? A Comprehensive Study on Execution Trace-Based Information for Code LLMs (arXiv 2509.11686, EMNLP Findings 2025) — central paper we extend; found trace SFT has limited value for generative code tasks; provides 5 trace formats we compare against
- Chain of Execution Supervision Promotes General Reasoning in LLMs [TracePile] (arXiv 2510.23629, NeurIPS 2025) — largest-scale trace SFT (2.6M CoE samples, 4 models, 20 benchmarks) but evaluates only generative tasks; reinforces our gap
- SemCoder: Training Code Language Models with Comprehensive Semantics Reasoning (arXiv 2406.01006, NeurIPS 2024) — trace-trained code model achieving strong CRUXEval gains
- TRACED: Execution-aware Pre-training for Source Code (arXiv 2306.07487, ICSE 2024) — precedent: execution-trace pre-training improves classification tasks (vulnerability detection, clone retrieval) for encoder models; we extend to decoder SFT
- What I cannot execute, I do not understand: Execution Tuning for Code LLMs (arXiv 2503.05703, 2025) — ~80% CRUXEval-O via dynamic scratchpads with trace training
- ExecVerify: White-Box RL with Verifiable Stepwise Rewards for Code Execution Reasoning (arXiv 2603.11226, 2026) — 7B ≈ 32B via execution-grounded RL
- Code Execution as Grounded Supervision for LLM Reasoning (arXiv 2506.10343, EMNLP 2025) — execution-derived CoT for reasoning transfer
- Self-Execution Simulation Improves Coding Models (arXiv 2604.03253, 2026) — SFT+RL on NL traces for self-verification
- FGIT: Fault-Guided Fine-Tuning for Code Generation (arXiv 2503.16913, ASE 2025) — correctness signals in code SFT via dynamic loss weighting; conceptually adjacent, generation-only
- Debugging Code World Models (arXiv 2602.07672, 2026) — identifies token-budget exhaustion as dominant failure mode in dense trace representations; motivates VOTA's compact design
- Calibration and Correctness of Language Models for Code (arXiv 2402.02047, ICSE 2025) — first calibration framework for code LLMs; methodology we adopt for ECE measurement
- ComPass: Contrastive Learning for Automated Patch Correctness Assessment (arXiv 2602.07561, 2026) — static APCA SOTA at 88.35%
- Historian: LLM-Based Multi-Reference Patch Correctness Assessment (arXiv 2603.00649, 2026) — 88.4% accuracy, 95.0% coverage via historical patch comparison
- Leveraging Large Language Model for Automatic Patch Correctness Assessment [LLM4PatchCorrect] (TSE 2024) — traces + APCA via ICL at 84.4%; closest existing work combining traces and APCA
- APSG/Graph-LoRA: Parameter-Efficient Fine-Tuning with Attributed Patch Semantic Graph for APCA (arXiv 2505.02629, 2025)
- RePaCA: Leveraging Reasoning LLMs for Static APCA (arXiv 2507.22580, 2025) — generic CoT for APCA at 83.1%
- Shibboleth: Patch Correctness Assessment (ISSTA 2022) — dynamic APCA at 88.7%
- CRUXEval: A Benchmark for Code Reasoning, Understanding and Execution (arXiv 2401.03065, ICML 2024)
- LiveCodeBench: Holistic and Contamination Free Evaluation of LLMs for Code (arXiv 2403.07974, 2024)
- CrossCodeEval: A Diverse and Multilingual Benchmark for Cross-File Code Completion (arXiv 2310.11248, NeurIPS 2023)
- RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems (arXiv 2306.03091, ICLR 2024) — excluded: generation benchmark with no verdict-task variant
- DebugBench: Evaluating Debugging Capability of LLMs (2024) — 4,253 instances across 18 bug types
- Towards Effectively Leveraging Execution Traces for Program Repair (arXiv 2505.04441, 2025) — trace-augmented generation limitations
- APPT: Boosting Automated Patch Correctness Prediction via Fine-tuning Pre-trained Models (TSE 2024)
- Patch Correctness Assessment: A Survey (TOSEM 2025)

## Reviewer Evaluation

**Scores**:
  - clarity: **{'rationale': "Exceptionally well-structured proposal with a clean task taxonomy (verdict/constrained-prediction/generation), precise differentiation from 7+ closely related works, well-defined hypotheses, rigorous evaluation protocol with bootstrap CIs and McNemar's test, and a dual-outcome framing (positive or negative results both publishable). The six-way trace format comparison is clearly motivated as the core ablation.", 'score': 5}**/5
  - feasibility: **{'rationale': 'Manual mode (160-190h H100) fits within the 200h budget. LoRA SFT on 7B models with small datasets (2k-8.5k samples per verdict task) is well-established and fast (~1-2h per run). The pilot go/no-go design is smart risk management. Defects4J trace collection (30h CPU) and the 66-configuration grid are ambitious but parallelizable. The auto_research mode (210-250h) exceeds the hard constraint, but the proposal acknowledges this and the core study is achievable in manual/HIL modes. Datasets (Defects4J, PraPatch, DebugBench, CRUXEval, HumanEval/MBPP) are all publicly available.', 'score': 4}**/5
  - impact: **{'rationale': 'Solid for the code understanding subcommunity: the calibration analysis provides mechanistic insight into why trace SFT fails for generation, and the APCA ensemble targeting >90% would break a meaningful plateau. The verdict-task insight could redirect trace SFT research. However, the practical scope is limited to function-level verdict tasks, and the APCA application is niche within SE. For EMNLP Findings, this is well-positioned; for Main, it would be borderline.', 'score': 3}**/5
  - novelty: **{'rationale': "The gap is independently verified as genuine: no prior work has tested trace SFT on code verdict/classification tasks (DCSH and TracePile both test only generation), and no prior work has designed a trace representation optimized for classification rather than simulation. VOTA's design principle (O(1) output entropy → minimal trace) is well-motivated. The calibration hypothesis connecting overconfidence to task type is novel and testable. However, the overall methodology (LoRA SFT with a new data representation) is standard.", 'score': 4}**/5

## Human Review Note

## Agent 审核结果（完整三阶段 pipeline）

**Verdict**: PASS

**入口三重共识 (X)**: 26.0%
**终审自评 (Y)**: 35.0%
**出口三重共识 (Z)**: 30.0%
**Z 区间**: [24.0%, 34.0%]
**真实提升 (Z-X)**: +4.0 pp
**幻觉幅度 (Y-Z)**: +5.0 pp
**出口一致性**: 高
**出口三次评估**: [31.0, 27.0, 33.0]

### 优化方案 / 拒绝详情
【优化方案】

1. [标题] — 从纯方法名 "Verdict-Optimized Trace Abstraction: When Execution Semantics Help Code Behavior Classification but Not Generation" 改为 "Verdict-Optimized Trace Abstraction: When Overconfidence Flips from Bug to Feature Across the Task Spectrum"，在标题层面即传达核心 conceptual flip，使 reviewer 在扫标题时抓住 novelty hook — [命中 Novelty]

2. [叙事重构 / Introduction] — 原始 proposal 以 "extending DCSH to classification" 为出发点（"While prior trace SFT work...evaluated only generative tasks and found limited benefit, we hypothesize that verdict tasks respond differently"），读起来像 follow-up study。改为以独立研究问题 "What makes an effective intermediate representation for code behavior classification?" 为中心，DCSH/TracePile 降为 related work 中的先驱工作。核心叙事从 "补 DCSH 没做的部分" 变为 "统一解释看似矛盾的先前发现，并提供量化预测框架" — [命中 Novelty, Significance]

3. [Core Insight / Central Thesis] — 原始 proposal 将 overconfidence 分析作为第 2 贡献平铺列出。改为将 "overconfidence as feature, not bug" 提升为论文统领性 thesis statement，在 abstract 首句即亮出。同时主动声明：贡献不是重新发现 overconfidence 对分类有利（Guo et al. 2017 等已知），而是将此现象与 trace SFT 的 task-dependent 效果连接起来 — [命中 Novelty, Related Work]

4. [Two-Channel Hypothesis 精确化] — 原始 proposal 假说 "overconfidence effect benefits classification while harming generation" 存在逻辑瑕疵（混淆 accuracy 与 calibration）。修改为明确分离 discriminative accuracy channel 和 calibration channel，表述为 "trace SFT 提升 verdict task 的 discriminative accuracy（channel 1），可能以 calibration degradation 为代价（channel 2），对 verdict tasks channel 1 主导；对 generation tasks 两个 channel 均无净收益" — [命中 Technical Soundness]

5. [Two-Channel 验证实验设计] — 原始 proposal 无通道分离验证方法。新增三重验证：(a) Brier score decomposition (Murphy 1973) 量化 refinement 与 calibration 分量的独立贡献；(b) post-hoc temperature scaling 消除 calibration channel 后观察 accuracy 是否保持；(c) causal identification experiment——将 no-trace baseline logits rescale 到 trace-SFT 同等 overconfidence 水平，测试 accuracy gain 是否来自 trace content 而非 confidence redistribution。第三个实验需在 proposal 中显式阐述其因果推理逻辑（ruling out the alternative hypothesis），而非仅作 bullet point — [命中 Technical Soundness]

6. [VOTA 设计原则] — 原始 proposal 仅列出四个组件但无设计理据（"encoding the minimal information needed"无定义无证明）。改为添加 information-theoretic design motivation（I(Z;Y) vs I(Z;T|Y) 框架），对每个组件说明其信息论目标，但诚实定位为 "design inspiration" 而非声称求解了 IB 优化问题。经验验证通过 component ablation + MI proxy estimation — [命中 Technical Soundness, Novelty]

7. [Data-driven baseline 从 optional 升为 mandatory] — 原始 proposal 仅有 "optionally compared against attention-based trace token importance scoring"。改为 mandatory core experiment，主动回应 "why not learn it" 的必然质疑。同时预注册三种可能结果及各自叙事含义：(i) VOTA 与 attention 对齐 → 验证设计合理性；(ii) 互补 → hybrid 潜力；(iii) attention 主导 → VOTA 工程设计 motivation 削弱但 two-channel analysis 和 task-spectrum framework 独立成立 — [命中 Technical Soundness]

8. [新增 baseline: Dynamic program slicing] — 原始 proposal 无 SE-based trace compression baseline。新增 dynamic program slicing（保留与 assertion 变量有数据/控制依赖的语句）作为与 VOTA 直接竞争的 principled 方法 — [命中 Technical Soundness, Related Work]

9. [贡献结构精简] — 原始 proposal 5 个平铺贡献（VOTA, calibration analysis, task-spectrum, APCA ensemble ">90%", SFT vs ICL）。精简为 2 个核心贡献：(1) VOTA + two-channel analysis（方法 + 机制解释合并为一个有因果链的贡献）；(2) Task-spectrum framework（从 empirical observation 到 reusable analytical tool）。APCA ensemble 去掉 ">90%" 硬承诺降为 supplementary；SFT vs ICL 降为 supplementary analysis — [命中 Novelty, Technical Soundness]

10. [Task-Spectrum Framework 形式化] — 原始 proposal 仅有一句 "task-spectrum analysis plotting trace SFT benefit vs. output space constraint"。改为：(a) primary x-axis 使用 baseline model output entropy（可实际测量），而非不可靠的 theoretical cardinality；(b) 增加中间数据点（CRUXEval multiple-choice, CodeSearchNet summarization, DebugBench multi-class variant）使 spectrum 从 2 个点扩展至 5+ 个点；(c) 声称强度从 "monotonic relationship" 校准为 "consistent empirical trend"；(d) within-dataset 对照（DebugBench binary vs. multi-class, HumanEval verdict vs. generation）作为因果关系最强证据，跨数据集比较为 correlational pattern — [命中 Technical Soundness, Significance]

11. [Confound 显式承认] — 原始 proposal 未讨论 task-spectrum 的混淆变量。新增显式声明：spectrum 上的任务不仅在 output constraint 上不同，还在数据集领域、难度、trace informativeness 上不同。within-dataset variants 提供 causal evidence，cross-dataset trend 为 correlational — [命中 Technical Soundness]

12. [Trace collection pipeline 实施细节] — 原始 proposal 完全未提及 trace 收集方案。新增：Python 端 sys.settrace + AST 自动插桩；Java 端 JDI/ByteBuddy + Defects4J 自带 test infrastructure。各组件获取层级映射。Cross-language instrumentation 差异显式讨论 + trace coverage 分析报告。承诺开源 — [命中 Feasibility, Technical Soundness]

13. [Baselines 扩充] — 原始 proposal 仅提到 LLM4PatchCorrect 和 ComPass/Historian。扩充为：每个 verdict task 上 2-3 个 SOTA baseline（LLMAO, Tare, CodeExecutor, DebugBench reported baselines）；必须有 no-trace baseline 和 full-trace baseline 作为 VOTA 价值的核心对照 — [命中 Technical Soundness]

14. [统计分析计划] — 原始 proposal 无统计方法论。新增：3 random seeds（Tier 1/2 实验），bootstrap CI，McNemar pairwise test，Holm-Bonferroni 多重比较校正，Cohen's d 效应量 — [命中 Technical Soundness]

15. [GPU 预算诚实化] — 原始 "≤250 H100-hours" 严重低估。改为 tiered 实验设计 + 详细 breakdown（Tier 1 全量比较 ~240h, Tier 2 关键 baselines ~160h, Tier 3 spectrum + 小模型 ~58h, 推理/校准分析 ~25h），修正为 ≤500 H100-hours — [命中 Feasibility]

16. [移除 "value regardless of outcome" framing] — 原始 proposal 将其作为卖点，增加被视为 negative result paper 的风险。改为明确正面假说 + 理论/经验预期论证，calibration analysis 定位为 mechanistic understanding 辅助贡献 — [命中 Technical Soundness]

17. [Related Work 扩充至四个文献 thread] — 原始 proposal 仅隐含引用 DCSH/TracePile。扩充为：(1) trace SFT for code；(2) SE-based trace abstraction（program slicing, dynamic invariant detection）；(3) CoT compression（显式区分 execution trace vs. CoT：确定性 vs. 生成性、忠实性 vs. 可能幻觉）；(4) Calibration of fine-tuned LMs（Guo et al. 2017, Desai & Durrett 2020, Kadavath et al. 2022, Tian et al. 2023） — [命中 Related Work]

18. [Broader Impact / Discussion] — 原始 proposal 无跨域讨论。新增 beyond-code generalization roadmap：two-channel framework 可能适用于 CoT distillation、tool-use trace SFT、agent trajectory SFT 等场景，定位为 suggestive hypothesis + testable future work，不过度承诺 — [命中 Significance]

19. [Model-size 分析] — 原始 proposal 仅用两个 ~7B 模型。新增一个小模型（1.5B/3B）在一个 verdict task 上的 supplementary 实验点，回应 "does this scale" — [命中 Technical Soundness]

【主要风险】:

1. **Core novelty 天花板受限**。即使重新定位为 "unified explanation + quantitative framework"，审稿人仍可能认为：(a) overconfidence 对 classification 有利是 calibration 文献已知结论的 domain-specific application；(b) VOTA 本质上是 well-engineered heuristic pipeline 而非方法论突破；(c) task-spectrum 数据点有限（5-6 个），"consistent trend" 的证据力度偏弱。这三点联合可能导致 novelty 评分为 borderline，是最可能被拒的原因。

2. **假说方向风险**。整个论文依赖 "VOTA trace SFT 显著优于 no-trace 和 full-trace baselines" 这一正面结果。如果 VOTA 在 Defects4J 上仅有 marginal improvement（1-2pp 且不显著），或 data-driven attention-based baseline 全面优于 VOTA，则 Contribution (1) 的叙事基础动摇。虽然 two-channel analysis 和 task-spectrum framework 可独立成立，但一篇以方法为名（VOTA）的论文如果方法本身效果不佳，主会接收概率会显著下降。

【实施评估】:

- **计算资源**: ≤500 H100-hours（约 21 GPU-days），需要可访问 H100/A100 集群。Tiered 设计：Tier 1（全量 comparison）~240h，Tier 2（关键 baselines）~160h，Tier 3（spectrum + 小模型）~58h，推理/校准分析 ~25h。如使用 A100 替代 H100，时间约增加 40-50%。
- **数据需求**: Defects4J（公开，Java）、HumanEval/MBPP（公开，Python）、DebugBench（公开，Python）、CRUXEval（公开，Python）、CodeSearchNet（公开）。所有数据集均公开可得。DCSH 的 trace 数据如有开源则可复用，否则需自行收集。
- **人工介入**: 无需人工标注。但 trace collection pipeline 的工程开发需要有 SE 背景的人参与：Python 端插桩约 1-2 周，Java/Defects4J 端 JDI/ByteBuddy 插桩约 2-3 周（工程量最大的部分）。Dynamic program slicing baseline 实现需要 program analysis 工具链经验。
- **训练需求**: 需要模型训练。LoRA fine-tuning Qwen2.5-Coder-7B 和 DeepSeek-Coder-6.7B，每个 condition 约 3-5 H100-hours。不需要全量微调或预训练。小模型（1.5B/3B）LoRA 训练成本更低。
- **新 Benchmark**: 不需要构建全新 benchmark。所有任务使用现有数据集。DebugBench 的 multi-class error type classification variant 需要从现有数据中重新组织标签（工作量小）。Task-spectrum diagram 本身是分析框架而非 benchmark。
- **预估周期**: 从启动到可投稿约 3.5-4.5 个月。Trace collection pipeline 开发（3-4 周）→ 数据收集与预处理（2 周）→ Tier 1 实验（2-3 周）→ Tier 2+3 实验（2-3 周）→ 分析与写作（3-4 周）→ 内部 review 与修改（2 周）。关键路径是 Java/Defects4J 的 trace collection 工程和 Tier 1 全量实验。



## MVP Validation Results

- **Date**: 2026-05-15
- **Hypothesis Supported**: Yes

### Key Metrics

VOTA: 95.63% acc, +20.5pp lift, CI [+17.7, +23.4] excludes 0 | no_trace: 75.13% | full_trace: 28.49% (collapse) | N=1190/condition | Bootstrap N=10000

### Summary

三条件对比完成：VOTA（assertion snapshot 的 actual/expected 值）95.63% accuracy，显著优于 no_trace baseline 75.13%（+20.5pp, CI [+17.7, +23.4]）。full_trace（完整执行 trace）28.49%，模型 collapse 为全预测 fail。核心假设"execution trace 信息能提升 verdict 预测"在 VOTA 条件下得到验证，但需要进一步 ablation 确认是语义理解还是字符串匹配。

### Recommendation

进入 research 阶段。优先级 #1：去 actual/expected ablation（验证 VOTA 是否为准泄漏）。优先级 #2：full_trace label-only loss 训练（尝试修复 gradient dilution）。
