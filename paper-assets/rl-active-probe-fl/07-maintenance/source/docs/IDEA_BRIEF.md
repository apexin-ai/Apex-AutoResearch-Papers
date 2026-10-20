# Idea Brief: DiagProbe: Training Code LLMs to Generate Diagnostic Runtime Probes via Reinforcement Learning


- **Idea ID**: `idea_008`
- **Created**: 2026-05-14
- **Approved**: 2026-05-14
- **Source**: foreign:be-idea-gen-0509-5
- **Level**: top-tier
- **Target Venues**: EMNLP 2026 (ARR submission deadline May 25, 2026, track: NLP and Code Models)

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

Code LLMs can generate and complete code but lack the ability to systematically reason about program runtime behavior—they cannot reliably form debugging hypotheses or generate targeted diagnostic queries that discriminate between failure modes. Current dynamic analysis approaches for debugging (DAIRA, ADI, DynaFix, TraceCoder, InspectCoder, LDB) all rely on fixed or rule-based strategies for generating diagnostic probes or collecting runtime information, never learning which probes are maximally informative. Meanwhile, recent RL-for-code work trains models to predict execution outcomes (CodeReasoner), internalize textual self-reflection (ReflexiCoder), or generate iterative code solutions (RLEF)—but none trains the generation of executable diagnostic instrumentation, a distinct action space that is both harder than textual reasoning (probes must compile, execute, and produce meaningful output) and naturally verifiable (probe-informed fixes either pass tests or don't). Can we train code LLMs via RL to generate diagnostic runtime probes (assertions, prints, variable inspections), and does this learned 'diagnostic questioning' capability improve debugging performance?

## Opportunity / Why Now

Dynamic analysis is demonstrably powerful for debugging: DAIRA achieves 79.4% on SWE-bench Verified with test-tracing, ADI provides 6.2-18.5% gains as a plug-in via Frame Lifetime Traces, DynaFix repairs 186 bugs on Defects4J via iterative execution-level dynamic information, and LDB improves code debugging by up to 9.8% through runtime variable tracking at basic-block granularity. Yet all use fixed prompting or rule-based strategies for diagnostic generation—none trains the probe strategy itself. Separately, CodeReasoner (SFT+GRPO) dramatically improves code reasoning via RL but targets execution prediction (I/O, coverage) rather than generating executable diagnostic code; ReflexiCoder internalizes self-reflection into model weights via RL-zero but generates textual reflections without execution grounding; RLEF proves RL with execution feedback improves iterative code generation; and LeDex shows SFT+RL can improve self-debugging via textual explanations. The key gap: no work applies RL specifically to train the generation of executable runtime instrumentation—the skill of producing diagnostic code that runs, reveals program behavior, and directly informs bug fixing. The critical insight for EMNLP: this action space has a unique alignment between difficulty and verifiability. Textual explanations (LeDex, ReflexiCoder) are cheap to generate but fundamentally unverifiable—the model can confabulate plausible-sounding reasoning. Executable probes are harder (must compile, execute, produce meaningful output) but their quality is naturally verifiable through downstream fix success. This difficulty-verifiability alignment is precisely what makes RL effective: the reward signal is informative because the action space is meaningfully constrained by execution.

## Landscape (SOTA & Limitations)

DAIRA (arXiv:2603.22048, Apr 2026) achieves 79.4% on SWE-bench Verified using test-tracing-driven dynamic analysis with Gemini 3 Flash Preview, capturing call stacks and variable states as structured semantic reports. It sets the SOTA for dynamic analysis-enhanced debugging but uses fixed prompting for trace collection. ADI (arXiv:2604.24212, Apr 2026) introduces a function-level Agent-centric Debugging Interface with Frame Lifetime Traces, achieving 63.8% on SWE-bench Verified at $1.28/task with Claude-Sonnet-3.7 and delivering 6.2-18.5% plug-in gains; its debugging interface is complementary to our learned probe generation. DynaFix (arXiv:2512.24635, Dec 2025) iteratively leverages execution-level dynamic information—variable states, control-flow paths, call stacks collected via ByteTrace—to guide LLM-based program repair, achieving 186 single-function bug fixes on Defects4J (10% over SOTA) with 70% reduction in patch search space. Like DAIRA and ADI, DynaFix uses fixed prompting for instrumentation: it transforms execution data into structured prompts rather than learning which information to collect. DiagProbe is complementary—DynaFix's ByteTrace-style collection could serve as probe execution infrastructure, but the probe generation strategy itself would be learned. LDB (ACL 2024 Findings, arXiv:2402.16906) segments programs into basic blocks and tracks intermediate variable values during runtime execution, enabling LLMs to verify correctness block-by-block and pinpoint errors, achieving up to 9.8% improvement on HumanEval, MBPP, and TransCoder. LDB demonstrates the value of fine-grained runtime state inspection for debugging but operates as a fixed prompting framework—it does not train the model to decide which variables to inspect or where to place probes. DiagProbe learns this selection skill via RL, which is strictly more general: a trained DiagProbe could learn to produce LDB-style block-level inspections when they are most informative, or generate different probe types when they are not. CodeReasoner (arXiv:2507.17548, Jul 2025) applies SFT+GRPO to train a 7B model for code reasoning tasks (I/O prediction, statement coverage), achieving 27-40% improvement over prior methods and matching GPT-4o—the closest methodological parallel to DiagProbe in training pipeline, but targeting execution outcome prediction rather than generating executable diagnostic instrumentation. The key difference: CodeReasoner's model predicts what code does, while DiagProbe's model generates code that reveals what buggy code does. ReflexiCoder (arXiv:2603.05863, Mar 2026) trains an 8B model via RL-zero to internalize structured self-reflection and self-correction trajectories into model weights, achieving 94.51% on HumanEval. It shifts from external-dependent refinement to intrinsic self-correction but generates textual reflections rather than executable diagnostic code, and explicitly operates without execution feedback at inference time—a fundamentally different paradigm from DiagProbe's execution-grounded approach. RLEF (ICML 2025, arXiv:2410.02089) trains code LLMs with PPO using execution feedback for iterative code synthesis on CodeContests, achieving SOTA at both 8B and 70B scales—a closely related RL+execution paradigm targeting generation rather than diagnostic reasoning. LeDex (arXiv:2405.18649) trains LLMs for self-debugging via SFT+RL, achieving up to 15.92% pass@1 improvement on CodeLlama-7B/13B, but generates natural language explanations rather than executable diagnostic probes. Posterior-GRPO (arXiv:2508.05170, Aug 2025) introduces process-reward conditioning for code generation, mitigating reward hacking by applying rewards only to reasoning processes of successful outcomes—relevant to our reward design. TraceCoder (ICSE 2026) uses multi-agent Analyzer/Fixer for trace-driven debugging with fixed agent protocols. DebugRepair refines patches using debugging statements with DeepSeek-V3, fixing 295 Defects4J bugs but using rule-based probe generation. InspectCoder enables interactive LLM-debugger collaboration with a fixed dual-agent framework. ToolTrain (arXiv:2508.03012) applies RL for repo-level tool-calling navigation (grep, search, file read), a different action space from diagnostic code generation. The 'Towards Effectively Leveraging Execution Traces' paper (KnowledgeNLP @ ACL 2025) found that full trace effectiveness decreases with complexity, directly motivating selective, learned probing. TraceRepair (arXiv:2604.02647) uses probe agents with multi-agent debate but employs fixed prompting. DebugBench (ACL 2024 Findings) provides 4,253 instances across C++/Java/Python with 18 bug types, serving as our primary training and evaluation benchmark. The recent finding that semantic-preserving mutations cause LLMs to fail at fault localization in 78% of cases (ICST 2026) further motivates training models for deeper runtime-grounded reasoning rather than relying on pattern matching.

## Proposed Approach

Fine-tune Qwen3-8B-Instruct via SFT followed by single-step GRPO to generate diagnostic runtime probes that improve downstream bug fixing, using verl with sandbox-fusion for execution (TRL v1.0 GRPOTrainer as fallback). We use Qwen3-8B as the current-generation dense model at the smallest scale suitable for full fine-tuning within our compute budget; the smallest Qwen3-Coder variant (30B-A3B, 3B active MoE) exceeds our budget for full-parameter fine-tuning and is included only as a LoRA-based scaling experiment.

Phase 1—Data Distillation and SFT (Days 1-5): Prompt a strong model (Claude Sonnet 4.6 API) on DebugBench's Python and Java subsets (~2,800 instances total, ~1,400 per language) to generate (diagnostic_probe, expected_insight, fix) triplets for each buggy program paired with its failing test. Diagnostic probes include targeted print statements exposing variable states at suspect locations, assertions testing specific hypotheses about bug causes, and conditional checks discriminating between fault candidates. We standardize the probe format across languages: all probes follow a common structure (probe_type, target_location, hypothesis, expected_output) while generating language-appropriate syntax. Filter by fix correctness (must pass all tests). Fine-tune Qwen3-8B-Instruct on this curated data (~30 H100-hours on 4× H100). We hold out C++ for cross-language transfer evaluation.

Training data scale justification: While CodeReasoner used ~17,332 instances for SFT across multiple diverse tasks (I/O prediction, coverage analysis), our SFT phase serves a narrower purpose—warm-starting the model on probe format and structure for a single focused objective (diagnostic probe generation). The primary learning mechanism is GRPO, which generates its own on-policy training signal through execution feedback. Evidence from DeepSeek-R1-Zero demonstrates that GRPO can improve reasoning from base models with zero SFT data; our ~2,800-instance SFT provides substantially more warm-start signal than the minimum required. We empirically validate this by tracking SFT loss convergence and comparing SFT-only vs. SFT+GRPO performance.

Phase 2—GRPO with Execution Feedback and Probe-Dependence Rewards (Days 6-11): Apply single-step GRPO (2 runs with different seeds for reproducibility) where the model generates one diagnostic probe given (buggy_code, failing_test), the probe executes in a pre-built sandbox via verl's sandbox-fusion integration (with TRL v1.0 GRPOTrainer + Daytona sandboxes as a tested fallback), then the model generates a fix conditioned on the probe's output. The reward function has three components: (1) Binary fix reward: 1 if the fix passes all tests, 0 otherwise. (2) Probe executability bonus: +0.1 if the probe runs without errors, preventing degenerate probes. (3) Probe-dependence reward: For a random subset of training samples (~20%), we additionally generate a fix conditioned on null probe output (empty string); if the fix differs from the probe-conditioned fix, the probe receives an additional +0.1 bonus, directly incentivizing probes that the model actually uses for diagnosis rather than ignoring. This counterfactual probe-dependence check serves as both a training-time reward component and an evaluation metric, providing a direct measure against reward hacking (the model cannot score high by generating trivial probes it ignores). Train on DebugBench Python subset (~1,400 instances), holding out Java for SFT-exposure-without-RL analysis and C++ for cross-language generalization (~80 H100-hours for 2 GRPO runs).

Phase 3—Comprehensive Evaluation (Days 12-16): Evaluate on all required benchmarks:

(1) DebugBench full (4,253 instances, primary metric: debugging accuracy across 18 bug types, 3 languages)—the core evaluation of diagnostic probe quality. This includes three distinct transfer conditions: Python (in-distribution for both SFT and GRPO), Java (SFT-exposed but no GRPO), and C++ (fully held-out cross-language transfer).

(2) SWE-bench Verified (500 instances, repo-level debugging): We evaluate DiagProbe as a plug-in diagnostic component within a minimal SWE-agent scaffold (bash-tool ReAct loop). When the scaffold identifies a candidate bug location, DiagProbe generates a diagnostic probe that executes in the SWE-bench Docker environment; the probe output is appended to the agent's context before fix generation. We compare: (a) scaffold with DiagProbe probes, (b) scaffold with fixed-prompt probes (ablation), (c) scaffold without probes (baseline). We pre-commit to paired statistical analysis: McNemar's test on the paired binary outcomes (resolved/not resolved) across the same 500 instances for each condition, with bootstrap confidence intervals (10,000 resamples) for effect size estimation. We do not claim competitive SOTA on SWE-bench Verified—given DiagProbe is an 8B model in a minimal scaffold—but test whether learned probing provides statistically significant gains over the no-probe and fixed-probe baselines. With 500 paired instances, McNemar's test has adequate power to detect effect sizes of ≥3-4 percentage points.

(3) HumanEval and MBPP (zero-shot code generation): Included to verify that diagnostic training does not degrade general code generation capabilities, not to claim positive transfer.

(4) CrossCodeEval (zero-shot cross-file code completion) and RepoBench (zero-shot repo-level completion): Included as exploratory evaluations testing whether probe training's emphasis on understanding variable flow and program state provides any incidental benefit to code completion tasks. Framed as hypothesis-testing (H0: no effect; H1: modest positive transfer from deeper code understanding), not as claimed contributions.

(5) CodeContests (zero-shot competitive programming): Included to test reasoning transfer; we hypothesize that diagnostic training may improve systematic reasoning about program behavior, but state this as exploratory.

Compare against: base Qwen3-8B-Instruct (no training), Qwen2.5-Coder-7B-Instruct (code-specialized baseline to isolate RL training contribution from base model choice—if DiagProbe on Qwen3-8B outperforms Qwen2.5-Coder-7B on debugging, it confirms that learned probe generation adds value beyond code pretraining), SFT-only ablation (no RL), LeDex-style textual debugging baseline (explanations instead of executable probes), direct-fix baseline (no probe step), CodeReasoner-style execution prediction baseline (predict output instead of generating probes), and zero-shot prompting of larger models (Claude Sonnet 4.6, GPT-4o). Perform LoRA-based scaling analysis with Qwen3-Coder-30B-A3B-Instruct (3B active MoE) if compute budget permits.

Key analyses include: (a) Probe taxonomy (what kinds of probes does the RL-trained model prefer?), (b) Probe-dependence analysis across all evaluation samples (what fraction of fixes change when given real vs. null vs. random-other-sample probe output?—this is the primary guard against reward hacking and the primary measure of probe utility), (c) Three-way cross-language transfer analysis (Python: SFT+GRPO, Java: SFT-only, C++: fully held-out), (d) SFT vs. GRPO probe quality distributions, (e) Function-level to repo-level transfer analysis (DebugBench → SWE-bench Verified), (f) Base model ablation (Qwen3-8B vs. Qwen2.5-Coder-7B, with and without DiagProbe training). The key EMNLP contribution: framing diagnostic probe generation as a trainable code reasoning skill with a uniquely favorable difficulty-verifiability alignment for RL, and demonstrating that this skill improves debugging performance on both function-level and repository-level benchmarks.

## Resource Estimate

- **auto_research**: {'claude_api_cost': '$150-250 (data distillation ~$60, experiment orchestration ~$50-100, analysis and paper drafting ~$40-90)', 'estimated_gpu_cost': '$600-800', 'gpu_hours': '~200 H100-hours (maximum budget; enables hyperparameter sweeps over probe-dependence reward weight, GRPO temperature, and Qwen2.5-Coder-7B comparative training)', 'gpu_utilization': '~85-90%; automated experiment scheduling fills GPU gaps between training and evaluation', 'risk_note': 'Reward hacking risk is actively mitigated during training via probe-dependence rewards (counterfactual null-probe comparison on ~20% of samples), not just post-hoc analysis. Additional risk: Qwen3-8B is a general model, not code-specialized—mitigated by explicit Qwen2.5-Coder-7B baseline comparison to isolate the RL contribution.', 'speed_bottleneck': "Parallel sandbox capacity for GRPO rollouts—need container pooling for ~500+ concurrent DebugBench instances; mitigated by verl's async rollout execution or TRL's async reward function support", 'team': '0 researchers after initial setup (verl/TRL config, DebugBench Docker images, SWE-bench Docker environments, evaluation scripts)', 'timeline': '10-14 days with 4-8 H100 GPUs concurrently'}
- **human_in_loop**: {'claude_api_cost': '$80-150 (SFT data distillation via Sonnet API ~$60 for ~2,800 instances, experiment orchestration and analysis ~$20-90)', 'estimated_gpu_cost': '$585-800', 'gpu_hours': '~195-200 H100-hours (SFT ~30h, 2 GRPO runs ~80h, full evaluation suite including SWE-bench Verified ~55h, Qwen2.5-Coder-7B baseline eval ~10h, Qwen3-Coder-30B-A3B LoRA scaling ~15h, buffer ~10h)', 'gpu_utilization': '~65-75%; agent handles overnight training, evaluation batching, and result collation', 'risk_note': 'Primary engineering risk: verl sandbox-fusion integration requires implementing a custom BaseTool subclass (reference implementation removed from tree). Fallback: TRL v1.0 GRPOTrainer with Daytona sandboxes for code execution, which has production-tested documentation and examples. SWE-bench Verified evaluation requires running a minimal agentic scaffold (~500 instances × ~5 agent turns × inference cost), adding ~10-15 H100-hours.', 'team': '1 researcher, ~1h/day reviewing training curves, probe quality samples, probe-dependence metrics, and cross-benchmark results', 'timeline': '12-16 days'}
- **manual**: {'estimated_gpu_cost': '$525-700 (H100 at ~$3-4/hr spot pricing)', 'gpu_hours': '~175 H100-hours (SFT ~30h on ~2,800 instances, 2 GRPO runs ~80h, evaluation across 7 benchmarks including SWE-bench Verified inference ~50h, buffer ~15h)', 'gpu_utilization': '~50-60% effective utilization; single-step rollouts with pre-built Docker images minimize sandbox overhead', 'team': '1 researcher with RL + code LLM experience', 'timeline': '16-18 days'}

## Key References

- DAIRA: Dynamic Analysis-enhanced Issue Resolution Agent (arXiv:2603.22048, Apr 2026)
- ADI: Empowering Autonomous Debugging Agents with Efficient Dynamic Analysis (arXiv:2604.24212, Apr 2026)
- DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information (arXiv:2512.24635, Dec 2025)
- LDB: Debug like a Human: A Large Language Model Debugger via Verifying Runtime Execution Step-by-step (ACL 2024 Findings, arXiv:2402.16906)
- CodeReasoner: Enhancing the Code Reasoning Ability with Reinforcement Learning (arXiv:2507.17548, Jul 2025)
- ReflexiCoder: Teaching LLMs to Self-Reflect and Self-Correct via Reinforcement Learning (arXiv:2603.05863, Mar 2026)
- RLEF: Grounding Code LLMs in Execution Feedback with Reinforcement Learning (ICML 2025, arXiv:2410.02089)
- LeDex: Training LLMs to Better Self-Debug and Explain Code (arXiv:2405.18649)
- Posterior-GRPO: Rewarding Reasoning Processes in Code Generation (arXiv:2508.05170, Aug 2025)
- DebugBench: Evaluating Debugging Capability of Large Language Models (ACL 2024 Findings)
- TraceCoder: A Trace-Driven Multi-Agent Framework for Automated Debugging of LLM-Generated Code (ICSE 2026)
- DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging (arXiv 2026)
- InspectCoder: Dynamic Analysis-Enabled Self Repair through Interactive LLM-Debugger Collaboration (arXiv 2025)
- Towards Effectively Leveraging Execution Traces for Program Repair with Code LLMs (KnowledgeNLP @ ACL 2025)
- ToolTrain: Tool-integrated Reinforcement Learning for Repo Deep Search (arXiv 2025)
- TraceRepair: Runtime Execution Traces Guided APR with Multi-Agent Debate (arXiv 2026)
- ARISE: A Repository-level Graph Representation for Agentic Fault Localization and Program Repair (arXiv 2026)
- RLocator: Reinforcement Learning for Bug Localization (IEEE TSE 2024)
- Assessing the Impact of Code Changes on the Fault Localizability of LLMs (ICST 2026)

## Reviewer Evaluation

**Scores**:
  - clarity: **{'rationale': "Exceptionally well-structured after 4 revision rounds. Every design choice is justified with references. Clear differentiation from 19 related works. Pre-committed statistical methodology (McNemar's test, bootstrap CIs) for SWE-bench. Evaluation framing (primary vs. exploratory) is honest and appropriate.", 'score': 4}**/5
  - feasibility: **{'rationale': '175 H100-hours is within budget with margin. verl+sandbox-fusion and TRL+Daytona are both verified production-ready. DebugBench is public on HuggingFace. Timeline is tight but the phased plan (SFT→GRPO→eval) is well-structured. Main risk is GRPO sandbox integration engineering, adequately mitigated by the TRL fallback.', 'score': 4}**/5
  - impact: **{'rationale': "Introduces a new trainable action space for code LLMs (diagnostic probes) with natural RL suitability. The difficulty-verifiability alignment is a conceptual lens that could generalize beyond this paper. Practical value depends on empirical gains, but the framework of 'learned debugging questions' addresses a real limitation of fixed-strategy dynamic analysis systems (DAIRA, ADI, DynaFix all use fixed prompting).", 'score': 4}**/5
  - novelty: **{'rationale': 'First work to train executable diagnostic probe generation via RL; the probe-dependence reward is a genuinely novel anti-reward-hacking mechanism; the difficulty-verifiability alignment concept for action space design is a useful contribution. InspectCoder/TraceCoder/DynaFix/LDB all use fixed strategies—the trained vs. prompted distinction is real and meaningful.', 'score': 4}**/5

## Human Review Note

## Agent 审核结果（完整三阶段 pipeline）

**Verdict**: PASS

**入口三重共识 (X)**: 32.0%
**终审自评 (Y)**: 37.0%
**出口三重共识 (Z)**: 34.0%
**Z 区间**: [28.0%, 39.0%]
**真实提升 (Z-X)**: +2.0 pp
**幻觉幅度 (Y-Z)**: +3.0 pp
**出口一致性**: 中
**出口三次评估**: [39.0, 30.0, 36.0]

### 优化方案 / 拒绝详情
【优化方案】

1. **[Introduction / Motivation] — 从平铺"Unlike X"对比重构为 action-space 三维分析框架 + 中心实验假说** — [命中 Novelty + Clarity + Significance]
   原始 proposal 用 4 段"Unlike DAIRA/CodeReasoner/ReflexiCoder/LeDex..."做差异化，读起来是 laundry list。优化后：(a) 建立 4×3 对比表（Quality Variance / Verifiability / Downstream Measurability），将 4 种 action space 系统性对比；(b) 为每个维度给出操作化定义（Quality Variance = naive-vs-optimal gap；Verifiability = automated assessment without human judge；Downstream Measurability = non-circular utility quantification）；(c) 将"self-referential"改为精确论述："direct fix 的 reward 只有 binary pass/fail，无法区分 lucky guess 和 principled fix"；(d) 从表格推导出中心实验假说："RL on probe generation yields greater lift over SFT than RL on direct fix, because the separable intermediate-artifact structure provides counterfactual causal reward signal"；(e) 表格标注为 "motivated hypotheses to be empirically tested"，避免被质疑为 cherry-picked 分类。

2. **[Contribution Statement] — 从隐含贡献重组为显式三层结构** — [命中 Novelty + Clarity]
   原始 proposal 贡献散落在方法描述中，审稿人需自行提炼。优化后显式列三层：(1) Counterfactual causal reward（方法论贡献）；(2) Action-space thesis 实证验证——probe RL vs. direct-fix RL（实验贡献）；(3) 跨语言/跨分布迁移实证（generalization 贡献）。Behavioral analysis（probe strategy evolution）降为 supporting analysis 而非独立贡献——因 checkpoint-level 行为分析在 RL-for-code 文献中已有先例，作为独立贡献重量不足。同时在 supporting analysis 段点出 probe 作为"externalized reasoning trace"比 CoT 更适合量化 RL 行为变化（discrete/structured/execution-verifiable）。

3. **[Reward Design] — 将一句话的"probe-dependence reward"升级为完整形式化的 Counterfactual Causal Reward (CCR)** — [命中 Novelty + Technical Soundness]
   原始 proposal 仅有"counterfactually compares fixes with real vs. null probe output"一句。优化后：
   - **形式化定义**：R_causal(a) = 𝟙[downstream(a) succeeds] · 𝟙[downstream(∅) fails]，先给通用形式再给 probe instantiation
   - **ORM/PRM/CCR 三元定位**（一句话 crisp positioning）："ORM 评估结果对不对，PRM 评估步骤对不对，CCR 评估步骤有没有用"——抓住"correct but useless"这个 PRM 抓不到但 CCR 能抓到的 failure mode
   - **Null probe 操作定义**：probe output 替换为空字符串，保留 pipeline 结构
   - **Discriminative window 分析**：R_causal 增量信号仅

