# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Self-consistency 优于 CRD 或 CRD 跨基准不泛化；核心 'cross-representation 独特价值' 假设不成立 →

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/478a83af-a594-4abf-9d30-21983e9275b5.jsonl`
- **Structured JSON:** [`81cc69176e24a2fcfcb8.json`](../../sessions/81/81cc69176e24a2fcfcb8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T07:29:44.835Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T07:29:44.835Z",
  "sessionId": "478a83af-a594-4abf-9d30-21983e9275b5",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Self-consistency 优于 CRD 或 CRD 跨基准不泛化；核心 'cross-representation 独特价值' 假设不成立 → 需 reframe 为 empirical analysis paper，仍投 EMNLP main\n核心假设：['exp-012: k=5 单表征 majority vote 精度 > CRD 5pp+，且 k=3 已追平 CRD', 'exp-003: ProofWriter pilot 失败（C1 < 10%），LogiQA fallback 也 C1 < 15%', 'exp-004: MATH C1 ≥ 15% 但 C2 < 60%，disagreement 多为噪声而非诊断信号', 'exp-002: DeepSeek 模式与 Qwen 显著不同——不对称方向反转或 C2 < 70%', 'exp-013: taxonomy κ < 0.40，分类体系高度模型依赖', 'exp-007: selection > repair 在所有子集上（包括 GT≠True），repair 无任何增量', 'C4 aggregate 和 stratified 均无统计显著性，bootstrap CI 含零']\n关键指标范围：{'C1_new_benchmarks': [0.05, 0.18], 'C2_new_benchmarks': [0.45, 0.65], 'CRD_vs_SC5_precision_delta': [-0.12, -0.03], 'CRD_vs_SC5_cost_ratio': [0.3, 0.45], 'cross_model_C2': [0.55, 0.72], 'taxonomy_kappa': [0.2, 0.39], 'C4_unknown_false_combined_delta': [-2.0, 6.0], 'selection_vs_blind_delta': [1.0, 6.0], 'repair_vs_selection_delta': [-6.0, -1.0], 'C5_committed_accuracy': [0.72, 0.85]}\n叙事方向：核心 reframe：放弃 \"CRD 是更好的诊断工具\" 这一方法论 claim，转为 \"cross-representation disagreement 的实证解剖\"——一篇关于 LLM 在不同形式化范式下失败模式的 systematic empirical study。新的 story spine：(1) LLM 将同一问题形式化为 FOL 和 Code 时，失败模式高度不对称 且互补（75% one-side-only），这本身是关于 LLM 能力结构的重要发现；(2) 但这种互补性 不足以构建可靠的诊断/修复 pipeline，因为 self-consistency 更简单且同样有效；(3) 我们 量化了 cross-representation 方法的边界条件——何时有效（高歧义、GT=Unknown）、何时失败 （高置信 True、合成数据集）、为什么失败（correlated failures, taxonomy instability）。 这种 reframe 仍适合 EMNLP main：venue 有接受高质量 negative/boundary result 的传统 （参考 \"Are Sixteen Heads Really Better than One\" 等）。标题改为类似 \"When Do Two Formalizations Know More Than One? An Empirical Study of Cross-Representation Disagreement in LLM Reasoning\"。关键：不降级到 workshop，而是提升分析深度——增加 failure correlation 的细粒度分析、representation-specific error 的 case study、 以及对何时该用 cross-repr vs self-consistency 的 practitioner guideline。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: cross_representation_disagreement_diagno\nfocus: Dream #1 identified 5 structural issues (all 3/6). Key changes since: (1) Added exp-012 self-consistency baseline (P0) — k=5 majority voting vs single-pass CRD, isolates cross-representation value; (2) Added exp-013 error taxonomy cross-model validation; (3) Softened novelty claim from \"first systematic study\" to \"first to extend from filtering to diagnosis\"; (4) Added R8-R11 reviewer concerns covering self-consistency, taxonomy validation, FOL vs CoT commensurability, related work expansion. (5) exp-007 selection-vs-repair promoted to P0. Please evaluate whether these additions address the structural gaps and push best-case toward weak accept.\n\n## paper_framing.md\n\n# Paper Framing — cross_representation_disagreement_diagno\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026 (10 days)\n- Secondary: AAAI 2027 (abstract July 25, full August 1) — extended version with full benchmark coverage\n\n## Core Insight\nWhen the same LLM formalizes a reasoning problem into two distinct executable representations, disagreements between them serve as a high-precision error detection signal (~87% diagnostic rate). This \"disagreement as diagnostic\" approach goes beyond existing methods that only filter or verify within a single representation — the disagreement pattern itself reveals error types, enables localization, and informs selective repair. The value is NOT symmetric complementarity between representations, but the diagnostic information contained in the disagreement signal.\n\n## Core Claims (3 条)\n\n### Claim 1: Disagreement as High-Precision Diagnostic Signal\nWhen the same LLM formalizes a reasoning problem into two distinct representations (FOL/Z3 and executable Python), disagreements occur at a substantial rate (~40%) and are diagnostically informative with high precision (~87%). This cross-representation signal detects formalization-specific errors invisible to within-representation verification.\n\n**MVP evidence**: C1=39.6% disagree rate, C2=86.8% diagnostic rate on FOLIO (204 samples, Qwen3-32B).\n\n### Claim 2: Error Classification and Conditional Localization\nDisagreement patterns enable error type classification into a structured taxonomy (4 types: logic_error 25.5%, negation_error 10.8%, quantifier_error 2.0%, exec_crash 5.4%). When the stability test yields a definitive prediction (62% of diagnostic samples), localization accuracy is high (85.4%). The 5.6:1 asymmetry (FOL correct 56 vs Code correct 10, both wrong 10) reveals systematic differences in LLM formal logic vs. code generation.\n\n**MVP evidence**: C5-committed = 94.6% (35/37) [CI: 86.1%-100%] — when stability test makes a definitive prediction, localization is near-perfect. C5-coverage = 53.0% (35/66) — 44% of diagnostic cases return \"ambiguous\" (especially Unknown: 61%). C3=4 error types.\n\n**Framing**: Stability-based localization is a high-precision / low-recall method. When it commits, it's right 95% of the time. The 44% ambiguous rate is primarily driven by GT=Unknown samples (61% ambiguous) where Code overclaiming creates systematically unstable predictions.\n\n**Key nuance**: GT=Unknown samples have the worst localization coverage (C5-coverage=35.7%) but the best repair delta (+14.7pp). This paradox suggests repair utility comes from the disagreement PATTERN (information content) rather than precise error-side identification — the model benefits from knowing the two representations disagree and what each concluded, regardless of which is labeled \"the error.\"\n\n### Claim 3: Diagnosis-Guided Repair Is GT-Label-Dependent — Helps, Hurts, or Neutral\nDiagnosis-guided repair exhibits a striking GT-label-dependent effect that reveals the boundary of cross-representation diagnosis:\n\n| GT Label | n | Targeted | Blind | Delta | Interpretation |\n|----------|---|----------|-------|-------|----------------|\n| Unknown | 69 | 67.7% | 52.9% | **+14.7pp** | Diagnosis helps: corrects Code overclaiming |\n| False | 63 | 76.7% | 70.0% | **+6.7pp** | Modest help |\n| True | 72 | 63.6% | 77.3% | **-13.6pp** | Diagnosis HURTS: overcorrection |\n\nThis is NOT simply \"conditional advantage\" — diagnosis actively harms repair for GT=True cases. The mechanism: for True problems where Code outputs False/Unknown, the diagnostic signal (\"Code disagrees with FOL\") triggers overcorrection, producing worse results than blind regeneration. We do NOT claim aggregate repair superiority — we characterize a fundamental asymmetry in when diagnosis helps vs. hurts repair.\n\n**MVP evidence**: C4 aggregate +4.65pp per-sample (Fisher p=0.626, not significant). The aggregate masks a three-way split that is the actual finding. Bootstrap CI for aggregate includes zero.\n\n**Presentation strategy**: \n1. Report C4 stratified by GT label as the PRIMARY result (table above)\n2. Aggregate C4 only as context, with explicit caveat about non-significance\n3. Frame GT=True overcorrection as a discovered failure mode, not a hidden weakness\n4. Discuss implications: practitioners should apply diagnosis-guided repair selectively (skip for high-confidence True predictions)\n\n## Story Spine\n\n- **Problem**: Neurosymbolic reasoning pipelines suffer from formalization errors as their dominant failure mode. The LLM's translation from natural language to formal representation introduces subtle corruptions. Current approaches either select one representation (HybridMind, Adaptive Selection), verify within one representation (VeriCoT, VERGE, Roundtrip Verification), or filter disagreeing solutions without diagnosis (Liang et al. 2024, Prove 2024). The gap: nobody uses cross-representation disagreement patterns for error CATEGORIZATION and TARGETED REPAIR.\n\n- **Existing approaches & gaps**: Liang et al. (2024) proved CoT-PoT disagreement is informative for filtering but stopped at discarding disagreements — no error categorization, no repair. Roundtrip Verification (2026) showed diagnosis-guided repair works within a single representation on a narrow domain (150 traffic rules). No method exploits cross-representation disagreement as a diagnostic signal enabling categorized diagnosis and targeted repair.\n\n- **Our framing (dual-track)**: We present (1) the first study to extend cross-representation disagreement from a binary filtering signal (Liang et al. 2024) to a structured diagnostic tool — enabling error classification, localization, and boundary characterization across domains and models; and (2) a lightweight diagnosis-guided repair framework that operates at inference time without model modification. The analysis is the primary contribution; the repair framework demonstrates downstream utility. Key distinction from self-consistency (Wang et al. 2023): within-representation sampling captures generation variance; cross-representation disagreement captures systematic formalization differences between paradigms (formal logic vs. imperative code).\n\n- **Headline result template**: \"On [benchmarks], cross-representation disagreement detects [X]% of samples as potentially erroneous with [Y]% diagnostic precision and [Z]% error localization accuracy. We characterize a fundamental asymmetry: [logic representation] exhibits [N]x lower formalization error rate than [code representation], revealing systematic differences in how LLMs handle formal logic vs. imperative code generation.\"\n\n## Venue Fit\n\n- **EMNLP fit (strong)**: NLP + symbolic reasoning is a core track. Dual-track framing (systematic analysis + method) aligns with EMNLP's tradition of accepting empirical analyses. The correlated failure / boundary characterization angle fits EMNLP's emphasis on rigorous evaluation.\n- **Risk**: modest repair improvement → mitigate by framing analysis as primary contribution, repair as secondary.\n- **Risk**: single model+dataset insufficient → extend to ≥2 models and ≥3 benchmarks in research phase.\n\n## Anticipated Reviewer Concerns & Responses\n\n| # | Concern | Response Strategy | Required Experiment |\n|---|---------|-------------------|---------------------|\n| R1 | Single model/dataset — generalization? | Cross-model ablation + multi-benchmark | exp-002, exp-003, exp-004 |\n| R2 | C4 repair improvement marginal | Honest framing + boundary characterization as contribution | exp-005, exp-006 |\n| R3 | Why repair, not just select correct side? | Selection vs repair ablation | exp-007 |\n| R4 | Error taxonomy rule-based, not learned | Deliberate choice for interpretability; taxonomy-guided vs fixed strategy ablation | exp-008 |\n| R5 | FOL 9:1 asymmetry — just FOL-as-verifier? | Test on math domain where asymmetry may differ | exp-004 |\n| R6 | Statistical significance? | Bootstrap CI + Fisher exact test on all metrics | exp-009 |\n| R7 | Correlated failures (Denisov-Blanch 2026) | Explicit quantification + cross-model ablation reduces correlation | exp-002, exp-006 |\n| R8 | How differs from self-consistency (k=5 majority voting)? | Dedicated baseline: k=5 FOL-only and k=5 Code-only vs single-pass CRD. Cross-representation captures paradigm-level differences, not sampling variance | exp-012 |\n| R9 | Error taxonomy unvalidated — no inter-annotator agreement | Cross-model validation: use different LLM to classify same errors, measure Cohen's κ. If possible, small human annotation (50 samples) | exp-013 |\n| R10 | FOL+Z3 vs CoT+SymPy are categorically different — conflating them as \"cross-representation\" is imprecise | Frame MATH domain as \"cross-executable-paradigm\" (symbolic algebra vs numerical computation), acknowledge different verification guarantees. Discuss as related but distinct instantiation | exp-004 framing |\n| R11 | Related work insufficient — missing self-consistency, LEVER, Faithful CoT, self-debug/refine, multi-agent debate, ensemble diversity | Expand related work to ≥25 references, position against all listed methods. Paper Agent must run reference-audit | Paper writing |\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'FOLIO 完整分析（MVP 数据深度挖掘）: 基于 204 样本 MVP 数据，完成： (a) 统计显著性检验（Bootstrap\n    95% CI + Fisher exact test） (b) 错误类型详细分类和分布 (c) GT=Unknown vs non-Unknown 子集 C1-C5\n    分层分析 (d) 分歧不对称性 9:1 breakdown (e) FOL/Code 失败相关性定量分析（phi coefficient / tetrachoric\n    correlation）— Claim 3 核心支撑 (f) cost-effectiveness 分析（每单位 token 成本的 accuracy gain）\n    不需要新实验运行，纯分析。\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: mvp_pipeline_004\n  status: ANALYZING\n  conclusion: success\n  metrics:\n    progress: 204/204 (deduped from 211)\n    deduped: true\n    unified_per_sample:\n      all_mode:\n        C1_disagree_rate: 42.16% (86/204)\n        C2_diagnostic_rate: 87.21% (75/86)\n        C3_error_types: 4 types\n        C4_targeted_delta: +4.65pp\n        C5_localization_acc: 53.03% (35/66)\n        C5_CI_95: '[41.0%, 65.1%]'\n        mvp_pass: 3/5 (C4 FAIL, C5 FAIL)\n      excl_unknown:\n        C1_disagree_rate: 38.52% (52/135)\n        C2_diagnostic_rate: 84.62% (44/52)\n        C3_error_types: 3 types\n        C4_targeted_delta: -1.92pp\n        C5_localization_acc: 65.79% (25/38)\n        C5_CI_95: '[50.0%, 80.6%]'\n        mvp_pass: 2/5 (C4 FAIL, C5 borderline PASS)\n    evaluate_mvp_per_side:\n      note: 保留为内部参考，不用于论文\n      all_mode_mvp_pass: 5/5 PASS\n    deep_analysis:\n      bootstrap_CI:\n        C1: '[35.3%, 49.0%]'\n        C2: '[81.3%, 94.7%]'\n        C4_delta: '[-8.8%, +18.1%]'\n        C5: '[41.0%, 65.1%]'\n      fisher_C4_pvalue:\n        all_mode: 0.626\n        excl_unknown: 1\n      asymmetry: FOL_correct_Code_wrong=56, Code_correct_FOL_wrong=10 (5.6:1)\n      gt_subset_C4:\n        'True': -13.6%\n        'False': +11.6%\n        Unknown: +14.7%\n      dominant_error: logic_error 25.5% (52/204)\n      phi_coefficient:\n        overall: 0.189\n        overall_p: 0.007\n      complementary_errors: 75/100 (75%) one-side-only failures\n      cost_effectiveness:\n        cost_multiplier: 5.76x\n        code_only_acc: 0.598\n        pipeline_acc: 0.814\n        oracle_acc: 0.878\n        accuracy_gain: +21.6pp\n- id: exp-002\n  claim:\n  - 1\n  - 2\n  description: '跨模型消融（FOLIO）: 三组条件对比—— (a) Qwen3-32B FOL + Qwen3-32B Code（MVP baseline，within-model）\n    (b) DeepSeek V4 Pro FOL + DeepSeek V4 Pro Code（within-model DeepSeek 对照） (c) DeepSeek\n    V4 Pro FOL + Qwen3-32B Code（cross-model） 目的：区分分歧来源是表征差异还是模型能力差异。FOLIO 204 样本。\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  api_cost_estimate: $30-50 (DeepSeek V4 Pro 2 组 + Qwen Cloud 1 组)\n  status: planned\n- id: exp-003\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'ProofWriter 扩展: 先跑 20-30 样本 pilot 验证 disagree_rate。 ProofWriter 是合成数据（无\n    NL 歧义），baseline accuracy 可能 >90%， C1 有低于 10% 的风险。Pilot 通过（disagree_rate ≥ 10%）则全量跑；\n    Pilot 失败则切换到 LogiQA（自然语言逻辑推理，歧义性更高）。\n\n    '\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  pilot_required: true\n  fallback_dataset: LogiQA\n  status: planned\n- id: exp-004\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'MATH Level 5 扩展: 使用两种可执行表征保持 framing 一致—— (a) SymPy 符号推理（代数化简、方程求解）\n    (b) Python 数值验证（直接计算、枚举、数值近似） 两条路径均可执行，保持与 FOLIO（FOL/Z3 vs Python）一致的 \"cross-executable-representation\"\n    框架。不使用 CoT（不可执行）。\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  status: planned\n- id: exp-005\n  claim: 3\n  description: 'Repair 机制改进: 多轮 repair（max 3 rounds）、加入错误类型特定修复策略、 对比 repair 前后 C4\n    delta。按 GT label 和 error_type 分层报告， 不报 aggregate。目标：在 Unknown 子组进一步拉大 delta， 在\n    non-Unknown 子组探索是否有改善空间。\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  status: planned\n- id: exp-006\n  claim: 3\n  description: 'Unknown 样本深度分析 + correlated failure 定量: (a) 为什么 GT=Unknown 样本驱动 C4\n    delta？Code overclaiming 机制分析 (b) FOL/Code 失败的相关系数（phi coefficient）按 GT label 分层\n    (c) false agreement rate 量化（两条路径都错但答案一致的比例） (d) specification-level vs formalization-specific\n    错误分类\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n- id: exp-007\n  claim: 3\n  description: 'Selection vs Repair 消融（Dream 审稿三档均要求）: 检测分歧+定位错误侧后， 直接选正确侧答案 vs 诊断引导修复。按\n    error_type 分层报告。 Dream 三档 Median 指出 selection nearly matches repair — 需量化。 回应\n    Reviewer Concern R3。\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  claim: 2\n  description: 'Error Taxonomy 消融: 按错误类型分派修复策略 vs 固定策略（统一重生成）， 验证 taxonomy 的规定性价值。\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-005\n  status: planned\n- id: exp-009\n  claim:\n  - 1\n  - 2\n  - 3\n  description: '统计显著性全面检验: 对所有 benchmark 的 C1-C5 指标做 bootstrap 95% CI + Fisher exact\n    test / McNemar test， 确保所有 claim 有统计支撑。\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-003\n  - exp-004\n  status: planned\n- id: exp-012\n  claim:\n  - 1\n  description: 'Self-consistency baseline 对比（三档一致 CRITICAL 缺失）: 在 FOLIO + ProofWriter\n    + MATH 上对比: (a) k=5 FOL-only majority vote (b) k=5 Code-only majority vote (c)\n    Single-pass CRD（我们的方法，1 FOL + 1 Code） 目的：隔离 cross-representation 信号 vs 单表征 sampling\n    diversity。 如果 k=5 单表征已达到相近诊断精度，需要 reframe 贡献。 如果 CRD 在更少 token 成本下匹配或超过 k=5，则\n    cost-effectiveness 是卖点。\n\n    '\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - exp-001\n  api_cost_estimate: $20-30\n  status: planned\n- id: exp-013\n  claim:\n  - 2\n  description: 'Error Taxonomy 交叉验证（三档一致弱点）: (a) 用 DeepSeek V4 Pro 对同一批 FOLIO 分歧样本做错误分类，与\n    Qwen3-32B 分类对比，计算 Cohen''s κ (b) 如果时间允许，50 个样本人工标注（用户或 LLM-as-human-proxy） (c)\n    报告分类一致性 + 错误类型分布是否跨模型稳定 目的：回应 Dream 审稿三档一致要求的 taxonomy validation\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  api_cost_estimate: $10-20\n  status: planned\n- id: exp-010\n  claim:\n  - 1\n  - 2\n  description: 'Qwen3-8B 消融: 低能力模型上的诊断率和分歧率变化。'\n  priority: P2\n  gpu_budget_hours: 4\n  deps: []\n  status: planned\n- id: exp-011\n  claim:\n  - 1\n  - 2\n  description: 'GPQA Diamond 扩展: 科学知识推理，SymPy/Python 双可执行表征。'\n  priority: P2\n  gpu_budget_hours: 6\n  deps:\n  - exp-004\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_baseline_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.74\n    correct: 37\n    total: 50\n    gate: PASS_FOLIO\n- exp_id: mvp_pipeline_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    disagree_rate: 0.04\n    diagnostic_rate: 1\n    error_types: 4\n    targeted_repair: 0.1875\n    blind_repair: 0.4688\n    delta_pp: -28.12\n    localization: 0.4186\n    fol_accuracy: 0.14\n    code_accuracy: 0.52\n    C1: false\n    C2: true\n    C3: true\n    C4: false\n    C5: false\n- exp_id: mvp_pipeline_002\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    fol_crash_rate_v2: 0.1\n    code_crash_rate_v2: 0.4\n    fol_crash_rate_v3: 0.8\n    code_crash_rate_v3: 0\n    fol_accuracy_v3: 0.2\n    code_accuracy_v3: 0.6\n    oracle_accuracy_v3: 0.6\n    disagree_rate_v3: 0\n    effective_disagree_rate_v3: 0\n    diagnostic_rate_v3: null\n    targeted_rate_v3: 0.5\n    blind_rate_v3: 0.625\n    delta_pp_v3: -12.5\n    localization_accuracy_v3: 0.5\n    error_types_v3: 3\n    C1_v3: false\n    C2_v3: false\n    C3_v3: true\n    C4_v3: false\n    C5_v3: false\n    avg_time_per_sample_s_v3: 218.5\n    total_api_calls_v3: 48\n    input_tokens_v3: 50558\n    output_tokens_v3: 139706\n    samples_v3: 10\n    v3_changes: enable_thinking=False for Code generation, _strip_thinking unclosed\n      tag handling\n- exp_id: mvp_pipeline_003\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_003b\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_004\n  name: ''\n  status: ANALYZING\n  conclusion: success\n  metrics:\n    progress: 204/204 (deduped from 211)\n    deduped: true\n    unified_per_sample:\n      all_mode:\n        C1_disagree_rate: 42.16% (86/204)\n        C2_diagnostic_rate: 87.21% (75/86)\n        C3_error_types: 4 types\n        C4_targeted_delta: +4.65pp\n        C5_localization_acc: 53.03% (35/66)\n        C5_CI_95: '[41.0%, 65.1%]'\n        mvp_pass: 3/5 (C4 FAIL, C5 FAIL)\n      excl_unknown:\n        C1_disagree_rate: 38.52% (52/135)\n        C2_diagnostic_rate: 84.62% (44/52)\n        C3_error_types: 3 types\n        C4_targeted_delta: -1.92pp\n        C5_localization_acc: 65.79% (25/38)\n        C5_CI_95: '[50.0%, 80.6%]'\n        mvp_pass: 2/5 (C4 FAIL, C5 borderline PASS)\n    evaluate_mvp_per_side:\n      note: 保留为内部参考，不用于论文\n      all_mode_mvp_pass: 5/5 PASS\n    deep_analysis:\n      bootstrap_CI:\n        C1: '[35.3%, 49.0%]'\n        C2: '[81.3%, 94.7%]'\n        C4_delta: '[-8.8%, +18.1%]'\n        C5: '[41.0%, 65.1%]'\n      fisher_C4_pvalue:\n        all_mode: 0.626\n        excl_unknown: 1\n      asymmetry: FOL_correct_Code_wrong=56, Code_correct_FOL_wrong=10 (5.6:1)\n      gt_subset_C4:\n        'True': -13.6%\n        'False': +11.6%\n        Unknown: +14.7%\n      dominant_error: logic_error 25.5% (52/204)\n      phi_coefficient:\n        overall: 0.189\n        overall_p: 0.007\n      complementary_errors: 75/100 (75%) one-side-only failures\n      cost_effectiveness:\n        cost_multiplier: 5.76x\n        code_only_acc: 0.598\n        pipeline_acc: 0.814\n        oracle_acc: 0.878\n        accuracy_gain: +21.6pp\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-15T07:29:44.839Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T07:29:44.839Z",
  "sessionId": "478a83af-a594-4abf-9d30-21983e9275b5"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-15T07:29:44.863Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Self-consistency 优于 CRD 或 CRD 跨基准不泛化；核心 'cross-representation 独特价值' 假设不成立 → 需 reframe 为 empirical analysis paper，仍投 EMNLP main
核心假设：['exp-012: k=5 单表征 majority vote 精度 > CRD 5pp+，且 k=3 已追平 CRD', 'exp-003: ProofWriter pilot 失败（C1 < 10%），LogiQA fallback 也 C1 < 15%', 'exp-004: MATH C1 ≥ 15% 但 C2 < 60%，disagreement 多为噪声而非诊断信号', 'exp-002: DeepSeek 模式与 Qwen 显著不同——不对称方向反转或 C2 < 70%', 'exp-013: taxonomy κ < 0.40，分类体系高度模型依赖', 'exp-007: selection > repair 在所有子集上（包括 GT≠True），repair 无任何增量', 'C4 aggregate 和 stratified 均无统计显著性，bootstrap CI 含零']
关键指标范围：{'C1_new_benchmarks': [0.05, 0.18], 'C2_new_benchmarks': [0.45, 0.65], 'CRD_vs_SC5_precision_delta': [-0.12, -0.03], 'CRD_vs_SC5_cost_ratio': [0.3, 0.45], 'cross_model_C2': [0.55, 0.72], 'taxonomy_kappa': [0.2, 0.39], 'C4_unknown_false_combined_delta': [-2.0, 6.0], 'selection_vs_blind_delta': [1.0, 6.0], 'repair_vs_selection_delta': [-6.0, -1.0], 'C5_committed_accuracy': [0.72, 0.85]}
叙事方向：核心 reframe：放弃 "CRD 是更好的诊断工具" 这一方法论 claim，转为 "cross-representation disagreement 的实证解剖"——一篇关于 LLM 在不同形式化范式下失败模式的 systematic empirical study。新的 story spine：(1) LLM 将同一问题形式化为 FOL 和 Code 时，失败模式高度不对称 且互补（75% one-side-only），这本身是关于 LLM 能力结构的重要发现；(2) 但这种互补性 不足以构建可靠的诊断/修复 pipeline，因为 self-consistency 更简单且同样有效；(3) 我们 量化了 cross-representation 方法的边界条件——何时有效（高歧义、GT=Unknown）、何时失败 （高置信 True、合成数据集）、为什么失败（correlated failures, taxonomy instability）。 这种 reframe 仍适合 EMNLP main：venue 有接受高质量 negative/boundary result 的传统 （参考 "Are Sixteen Heads Really Better than One" 等）。标题改为类似 "When Do Two Formalizations Know More Than One? An Empirical Study of Cross-Representation Disagreement in LLM Reasoning"。关键：不降级到 workshop，而是提升分析深度——增加 failure correlation 的细粒度分析、representation-specific error 的 case study、 以及对何时该用 cross-repr vs self-consistency 的 practitioner guideline。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: cross_representation_disagreement_diagno
focus: Dream #1 identified 5 structural issues (all 3/6). Key changes since: (1) Added exp-012 self-consistency baseline (P0) — k=5 majority voting vs single-pass CRD, isolates cross-representation value; (2) Added exp-013 error taxonomy cross-model validation; (3) Softened novelty claim from "first systematic study" to "first to extend from filtering to diagnosis"; (4) Added R8-R11 reviewer concerns covering self-consistency, taxonomy validation, FOL vs CoT commensurability, related work expansion. (5) exp-007 selection-vs-repair promoted to P0. Please evaluate whether these additions address the structural gaps and push best-case toward weak accept.

## paper_framing.md

# Paper Framing — cross_representation_disagreement_diagno

## Target Venue
- Primary: EMNLP 2026 Main (ARR submission)
- Fallback: EMNLP 2026 Findings
- Deadline: ARR May 25, 2026 (10 days)
- Secondary: AAAI 2027 (abstract July 25, full August 1) — extended version with full benchmark coverage

## Core Insight
When the same LLM formalizes a reasoning problem into two distinct executable representations, disagreements between them serve as a high-precision error detection signal (~87% diagnostic rate). This "disagreement as diagnostic" approach goes beyond existing methods that only filter or verify within a single representation — the disagreement pattern itself reveals error types, enables localization, and informs selective repair. The value is NOT symmetric complementarity between representations, but the diagnostic information contained in the disagreement signal.

## Core Claims (3 条)

### Claim 1: Disagreement as High-Precision Diagnostic Signal
When the same LLM formalizes a reasoning problem into two distinct representations (FOL/Z3 and executable Python), disagreements occur at a substantial rate (~40%) and are diagnostically informative with high precision (~87%). This cross-representation signal detects formalization-specific errors invisible to within-representation verification.

**MVP evidence**: C1=39.6% disagree rate, C2=86.8% diagnostic rate on FOLIO (204 samples, Qwen3-32B).

### Claim 2: Error Classification and Conditional Localization
Disagreement patterns enable error type classification into a structured taxonomy (4 types: logic_error 25.5%, negation_error 10.8%, quantifier_error 2.0%, exec_crash 5.4%). When the stability test yields a definitive prediction (62% of diagnostic samples), localization accuracy is high (85.4%). The 5.6:1 asymmetry (FOL correct 56 vs Code correct 10, both wrong 10) reveals systematic differences in LLM formal logic vs. code generation.

**MVP evidence**: C5-committed = 94.6% (35/37) [CI: 86.1%-100%] — when stability test makes a definitive prediction, localization is near-perfect. C5-coverage = 53.0% (35/66) — 44% of diagnostic cases return "ambiguous" (especially Unknown: 61%). C3=4 error types.

**Framing**: Stability-based localization is a high-precision / low-recall method. When it commits, it's right 95% of the time. The 44% ambiguous rate is primarily driven by GT=Unknown samples (61% ambiguous) where Code overclaiming creates systematically unstable predictions.

**Key nuance**: GT=Unknown samples have the worst localization coverage (C5-coverage=35.7%) but the best repair delta (+14.7pp). This paradox suggests repair utility comes from the disagreement PATTERN (information content) rather than precise error-side identification — the model benefits from knowing the two representations disagree and what each concluded, regardless of which is labeled "the error."

### Claim 3: Diagnosis-Guided Repair Is GT-Label-Dependent — Helps, Hurts, or Neutral
Diagnosis-guided repair exhibits a striking GT-label-dependent effect that reveals the boundary of cross-representation diagnosis:

| GT Label | n | Targeted | Blind | Delta | Interpretation |
|----------|---|----------|-------|-------|----------------|
| Unknown | 69 | 67.7% | 52.9% | **+14.7pp** | Diagnosis helps: corrects Code overclaiming |
| False | 63 | 76.7% | 70.0% | **+6.7pp** | Modest help |
| True | 72 | 63.6% | 77.3% | **-13.6pp** | Diagnosis HURTS: overcorrection |

This is NOT simply "conditional advantage" — diagnosis actively harms repair for GT=True cases. The mechanism: for True problems where Code outputs False/Unknown, the diagnostic signal ("Code disagrees with FOL") triggers overcorrection, producing worse results than blind regeneration. We do NOT claim aggregate repair superiority — we characterize a fundamental asymmetry in when diagnosis helps vs. hurts repair.

**MVP evidence**: C4 aggregate +4.65pp per-sample (Fisher p=0.626, not significant). The aggregate masks a three-way split that is the actual finding. Bootstrap CI for aggregate includes zero.

**Presentation strategy**: 
1. Report C4 stratified by GT label as the PRIMARY result (table above)
2. Aggregate C4 only as context, with explicit caveat about non-significance
3. Frame GT=True overcorrection as a discovered failure mode, not a hidden weakness
4. Discuss implications: practitioners should apply diagnosis-guided repair selectively (skip for high-confidence True predictions)

## Story Spine

- **Problem**: Neurosymbolic reasoning pipelines suffer from formalization errors as their dominant failure mode. The LLM's translation from natural language to formal representation introduces subtle corruptions. Current approaches either select one representation (HybridMind, Adaptive Selection), verify within one representation (VeriCoT, VERGE, Roundtrip Verification), or filter disagreeing solutions without diagnosis (Liang et al. 2024, Prove 2024). The gap: nobody uses cross-representation disagreement patterns for error CATEGORIZATION and TARGETED REPAIR.

- **Existing approaches & gaps**: Liang et al. (2024) proved CoT-PoT disagreement is informative for filtering but stopped at discarding disagreements — no error categorization, no repair. Roundtrip Verification (2026) showed diagnosis-guided repair works within a single representation on a narrow domain (150 traffic rules). No method exploits cross-representation disagreement as a diagnostic signal enabling categorized diagnosis and targeted repair.

- **Our framing (dual-track)**: We present (1) the first study to extend cross-representation disagreement from a binary filtering signal (Liang et al. 2024) to a structured diagnostic tool — enabling error classification, localization, and boundary characterization across domains and models; and (2) a lightweight diagnosis-guided repair framework that operates at inference time without model modification. The analysis is the primary contribution; the repair framework demonstrates downstream utility. Key distinction from self-consistency (Wang et al. 2023): within-representation sampling captures generation variance; cross-representation disagreement captures systematic formalization differences between paradigms (formal logic vs. imperative code).

- **Headline result template**: "On [benchmarks], cross-representation disagreement detects [X]% of samples as potentially erroneous with [Y]% diagnostic precision and [Z]% error localization accuracy. We characterize a fundamental asymmetry: [logic representation] exhibits [N]x lower formalization error rate than [code representation], revealing systematic differences in how LLMs handle formal logic vs. imperative code generation."

## Venue Fit

- **EMNLP fit (strong)**: NLP + symbolic reasoning is a core track. Dual-track framing (systematic analysis + method) aligns with EMNLP's tradition of accepting empirical analyses. The correlated failure / boundary characterization angle fits EMNLP's emphasis on rigorous evaluation.
- **Risk**: modest repair improvement → mitigate by framing analysis as primary contribution, repair as secondary.
- **Risk**: single model+dataset insufficient → extend to ≥2 models and ≥3 benchmarks in research phase.

## Anticipated Reviewer Concerns & Responses

| # | Concern | Response Strategy | Required Experiment |
|---|---------|-------------------|---------------------|
| R1 | Single model/dataset — generalization? | Cross-model ablation + multi-benchmark | exp-002, exp-003, exp-004 |
| R2 | C4 repair improvement marginal | Honest framing + boundary characterization as contribution | exp-005, exp-006 |
| R3 | Why repair, not just select correct side? | Selection vs repair ablation | exp-007 |
| R4 | Error taxonomy rule-based, not learned | Deliberate choice for interpretability; taxonomy-guided vs fixed strategy ablation | exp-008 |
| R5 | FOL 9:1 asymmetry — just FOL-as-verifier? | Test on math domain where asymmetry may differ | exp-004 |
| R6 | Statistical significance? | Bootstrap CI + Fisher exact test on all metrics | exp-009 |
| R7 | Correlated failures (Denisov-Blanch 2026) | Explicit quantification + cross-model ablation reduces correlation | exp-002, exp-006 |
| R8 | How differs from self-consistency (k=5 majority voting)? | Dedicated baseline: k=5 FOL-only and k=5 Code-only vs single-pass CRD. Cross-representation captures paradigm-level differences, not sampling variance | exp-012 |
| R9 | Error taxonomy unvalidated — no inter-annotator agreement | Cross-model validation: use different LLM to classify same errors, measure Cohen's κ. If possible, small human annotation (50 samples) | exp-013 |
| R10 | FOL+Z3 vs CoT+SymPy are categorically different — conflating them as "cross-representation" is imprecise | Frame MATH domain as "cross-executable-paradigm" (symbolic algebra vs numerical computation), acknowledge different verification guarantees. Discuss as related but distinct instantiation | exp-004 framing |
| R11 | Related work insufficient — missing self-consistency, LEVER, Faithful CoT, self-debug/refine, multi-agent debate, ensemble diversity | Expand related work to ≥25 references, position against all listed methods. Paper Agent must run reference-audit | Paper writing |


## experiment_plan (with registry status)

- id: exp-001
  claim:
  - 1
  - 2
  - 3
  description: 'FOLIO 完整分析（MVP 数据深度挖掘）: 基于 204 样本 MVP 数据，完成： (a) 统计显著性检验（Bootstrap
    95% CI + Fisher exact test） (b) 错误类型详细分类和分布 (c) GT=Unknown vs non-Unknown 子集 C1-C5
    分层分析 (d) 分歧不对称性 9:1 breakdown (e) FOL/Code 失败相关性定量分析（phi coefficient / tetrachoric
    correlation）— Claim 3 核心支撑 (f) cost-effectiveness 分析（每单位 token 成本的 accuracy gain）
    不需要新实验运行，纯分析。

    '
  priority: P0
  gpu_budget_hours: 0
  deps: []
  registry_id: mvp_pipeline_004
  status: ANALYZING
  conclusion: success
  metrics:
    progress: 204/204 (deduped from 211)
    deduped: true
    unified_per_sample:
      all_mode:
        C1_disagree_rate: 42.16% (86/204)
        C2_diagnostic_rate: 87.21% (75/86)
        C3_error_types: 4 types
        C4_targeted_delta: +4.65pp
        C5_localization_acc: 53.03% (35/66)
        C5_CI_95: '[41.0%, 65.1%]'
        mvp_pass: 3/5 (C4 FAIL, C5 FAIL)
      excl_unknown:
        C1_disagree_rate: 38.52% (52/135)
        C2_diagnostic_rate: 84.62% (44/52)
        C3_error_types: 3 types
        C4_targeted_delta: -1.92pp
        C5_localization_acc: 65.79% (25/38)
        C5_CI_95: '[50.0%, 80.6%]'
        mvp_pass: 2/5 (C4 FAIL, C5 borderline PASS)
    evaluate_mvp_per_side:
      note: 保留为内部参考，不用于论文
      all_mode_mvp_pass: 5/5 PASS
    deep_analysis:
      bootstrap_CI:
        C1: '[35.3%, 49.0%]'
        C2: '[81.3%, 94.7%]'
        C4_delta: '[-8.8%, +18.1%]'
        C5: '[41.0%, 65.1%]'
      fisher_C4_pvalue:
        all_mode: 0.626
        excl_unknown: 1
      asymmetry: FOL_correct_Code_wrong=56, Code_correct_FOL_wrong=10 (5.6:1)
      gt_subset_C4:
        'True': -13.6%
        'False': +11.6%
        Unknown: +14.7%
      dominant_error: logic_error 25.5% (52/204)
      phi_coefficient:
        overall: 0.189
        overall_p: 0.007
      complementary_errors: 75/100 (75%) one-side-only failures
      cost_effectiveness:
        cost_multiplier: 5.76x
        code_only_acc: 0.598
        pipeline_acc: 0.814
        oracle_acc: 0.878
        accuracy_gain: +21.6pp
- id: exp-002
  claim:
  - 1
  - 2
  description: '跨模型消融（FOLIO）: 三组条件对比—— (a) Qwen3-32B FOL + Qwen3-32B Code（MVP baseline，within-model）
    (b) DeepSeek V4 Pro FOL + DeepSeek V4 Pro Code（within-model DeepSeek 对照） (c) DeepSeek
    V4 Pro FOL + Qwen3-32B Code（cross-model） 目的：区分分歧来源是表征差异还是模型能力差异。FOLIO 204 样本。

    '
  priority: P0
  gpu_budget_hours: 4
  deps:
  - exp-001
  api_cost_estimate: $30-50 (DeepSeek V4 Pro 2 组 + Qwen Cloud 1 组)
  status: planned
- id: exp-003
  claim:
  - 1
  - 2
  - 3
  description: 'ProofWriter 扩展: 先跑 20-30 样本 pilot 验证 disagree_rate。 ProofWriter 是合成数据（无
    NL 歧义），baseline accuracy 可能 >90%， C1 有低于 10% 的风险。Pilot 通过（disagree_rate ≥ 10%）则全量跑；
    Pilot 失败则切换到 LogiQA（自然语言逻辑推理，歧义性更高）。

    '
  priority: P0
  gpu_budget_hours: 6
  deps: []
  pilot_required: true
  fallback_dataset: LogiQA
  status: planned
- id: exp-004
  claim:
  - 1
  - 2
  - 3
  description: 'MATH Level 5 扩展: 使用两种可执行表征保持 framing 一致—— (a) SymPy 符号推理（代数化简、方程求解）
    (b) Python 数值验证（直接计算、枚举、数值近似） 两条路径均可执行，保持与 FOLIO（FOL/Z3 vs Python）一致的 "cross-executable-representation"
    框架。不使用 CoT（不可执行）。

    '
  priority: P0
  gpu_budget_hours: 8
  deps: []
  status: planned
- id: exp-005
  claim: 3
  description: 'Repair 机制改进: 多轮 repair（max 3 rounds）、加入错误类型特定修复策略、 对比 repair 前后 C4
    delta。按 GT label 和 error_type 分层报告， 不报 aggregate。目标：在 Unknown 子组进一步拉大 delta， 在
    non-Unknown 子组探索是否有改善空间。

    '
  priority: P0
  gpu_budget_hours: 4
  deps:
  - exp-001
  status: planned
- id: exp-006
  claim: 3
  description: 'Unknown 样本深度分析 + correlated failure 定量: (a) 为什么 GT=Unknown 样本驱动 C4
    delta？Code overclaiming 机制分析 (b) FOL/Code 失败的相关系数（phi coefficient）按 GT label 分层
    (c) false agreement rate 量化（两条路径都错但答案一致的比例） (d) specification-level vs formalization-specific
    错误分类

    '
  priority: P1
  gpu_budget_hours: 0
  deps:
  - exp-001
  status: planned
- id: exp-007
  claim: 3
  description: 'Selection vs Repair 消融（Dream 审稿三档均要求）: 检测分歧+定位错误侧后， 直接选正确侧答案 vs 诊断引导修复。按
    error_type 分层报告。 Dream 三档 Median 指出 selection nearly matches repair — 需量化。 回应
    Reviewer Concern R3。

    '
  priority: P0
  gpu_budget_hours: 2
  deps:
  - exp-001
  status: planned
- id: exp-008
  claim: 2
  description: 'Error Taxonomy 消融: 按错误类型分派修复策略 vs 固定策略（统一重生成）， 验证 taxonomy 的规定性价值。

    '
  priority: P1
  gpu_budget_hours: 2
  deps:
  - exp-005
  status: planned
- id: exp-009
  claim:
  - 1
  - 2
  - 3
  description: '统计显著性全面检验: 对所有 benchmark 的 C1-C5 指标做 bootstrap 95% CI + Fisher exact
    test / McNemar test， 确保所有 claim 有统计支撑。

    '
  priority: P1
  gpu_budget_hours: 0
  deps:
  - exp-001
  - exp-003
  - exp-004
  status: planned
- id: exp-012
  claim:
  - 1
  description: 'Self-consistency baseline 对比（三档一致 CRITICAL 缺失）: 在 FOLIO + ProofWriter
    + MATH 上对比: (a) k=5 FOL-only majority vote (b) k=5 Code-only majority vote (c)
    Single-pass CRD（我们的方法，1 FOL + 1 Code） 目的：隔离 cross-representation 信号 vs 单表征 sampling
    diversity。 如果 k=5 单表征已达到相近诊断精度，需要 reframe 贡献。 如果 CRD 在更少 token 成本下匹配或超过 k=5，则
    cost-effectiveness 是卖点。

    '
  priority: P0
  gpu_budget_hours: 6
  deps:
  - exp-001
  api_cost_estimate: $20-30
  status: planned
- id: exp-013
  claim:
  - 2
  description: 'Error Taxonomy 交叉验证（三档一致弱点）: (a) 用 DeepSeek V4 Pro 对同一批 FOLIO 分歧样本做错误分类，与
    Qwen3-32B 分类对比，计算 Cohen''s κ (b) 如果时间允许，50 个样本人工标注（用户或 LLM-as-human-proxy） (c)
    报告分类一致性 + 错误类型分布是否跨模型稳定 目的：回应 Dream 审稿三档一致要求的 taxonomy validation

    '
  priority: P1
  gpu_budget_hours: 0
  deps:
  - exp-001
  api_cost_estimate: $10-20
  status: planned
- id: exp-010
  claim:
  - 1
  - 2
  description: 'Qwen3-8B 消融: 低能力模型上的诊断率和分歧率变化。'
  priority: P2
  gpu_budget_hours: 4
  deps: []
  status: planned
- id: exp-011
  claim:
  - 1
  - 2
  description: 'GPQA Diamond 扩展: 科学知识推理，SymPy/Python 双可执行表征。'
  priority: P2
  gpu_budget_hours: 6
  deps:
  - exp-004
  status: planned


## registry (completed experiments)

- exp_id: mvp_baseline_001
  name: ''
  status: DONE
  conclusion: success
  metrics:
    accuracy: 0.74
    correct: 37
    total: 50
    gate: PASS_FOLIO
- exp_id: mvp_pipeline_001
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    disagree_rate: 0.04
    diagnostic_rate: 1
    error_types: 4
    targeted_repair: 0.1875
    blind_repair: 0.4688
    delta_pp: -28.12
    localization: 0.4186
    fol_accuracy: 0.14
    code_accuracy: 0.52
    C1: false
    C2: true
    C3: true
    C4: false
    C5: false
- exp_id: mvp_pipeline_002
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    fol_crash_rate_v2: 0.1
    code_crash_rate_v2: 0.4
    fol_crash_rate_v3: 0.8
    code_crash_rate_v3: 0
    fol_accuracy_v3: 0.2
    code_accuracy_v3: 0.6
    oracle_accuracy_v3: 0.6
    disagree_rate_v3: 0
    effective_disagree_rate_v3: 0
    diagnostic_rate_v3: null
    targeted_rate_v3: 0.5
    blind_rate_v3: 0.625
    delta_pp_v3: -12.5
    localization_accuracy_v3: 0.5
    error_types_v3: 3
    C1_v3: false
    C2_v3: false
    C3_v3: true
    C4_v3: false
    C5_v3: false
    avg_time_per_sample_s_v3: 218.5
    total_api_calls_v3: 48
    input_tokens_v3: 50558
    output_tokens_v3: 139706
    samples_v3: 10
    v3_changes: enable_thinking=False for Code generation, _strip_thinking unclosed
      tag handling
- exp_id: mvp_pipeline_003
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp_pipeline_003b
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: mvp_pipeline_004
  name: ''
  status: ANALYZING
  conclusion: success
  metrics:
    progress: 204/204 (deduped from 211)
    deduped: true
    unified_per_sample:
      all_mode:
        C1_disagree_rate: 42.16% (86/204)
        C2_diagnostic_rate: 87.21% (75/86)
        C3_error_types: 4 types
        C4_targeted_delta: +4.65pp
        C5_localization_acc: 53.03% (35/66)
        C5_CI_95: '[41.0%, 65.1%]'
        mvp_pass: 3/5 (C4 FAIL, C5 FAIL)
      excl_unknown:
        C1_disagree_rate: 38.52% (52/135)
        C2_diagnostic_rate: 84.62% (44/52)
        C3_error_types: 3 types
        C4_targeted_delta: -1.92pp
        C5_localization_acc: 65.79% (25/38)
        C5_CI_95: '[50.0%, 80.6%]'
        mvp_pass: 2/5 (C4 FAIL, C5 borderline PASS)
    evaluate_mvp_per_side:
      note: 保留为内部参考，不用于论文
      all_mode_mvp_pass: 5/5 PASS
    deep_analysis:
      bootstrap_CI:
        C1: '[35.3%, 49.0%]'
        C2: '[81.3%, 94.7%]'
        C4_delta: '[-8.8%, +18.1%]'
        C5: '[41.0%, 65.1%]'
      fisher_C4_pvalue:
        all_mode: 0.626
        excl_unknown: 1
      asymmetry: FOL_correct_Code_wrong=56, Code_correct_FOL_wrong=10 (5.6:1)
      gt_subset_C4:
        'True': -13.6%
        'False': +11.6%
        Unknown: +14.7%
      dominant_error: logic_error 25.5% (52/204)
      phi_coefficient:
        overall: 0.189
        overall_p: 0.007
      complementary_errors: 75/100 (75%) one-side-only failures
      cost_effectiveness:
        cost_multiplier: 5.76x
        code_only_acc: 0.598
        pipeline_acc: 0.814
        oracle_acc: 0.878
        accuracy_gain: +21.6pp

# 输出格式（YAML，仅输出一个 ```yaml 块）

```yaml
tier: worst
narrative_guidance: "..."
imagined_experiments:
  - name: "..."
    plan_id: "..."
    description: "..."
    expected_results: {metric: value, ...}
    result_rationale: "..."
    tables: []
    figures_description: []
    analysis: "..."
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "ed620aa3-8f38-400b-891f-861aa51df242",
  "type": "user",
  "uuid": "faa016df-fb0e-4c5e-948f-1e79a80c86f5",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "478a83af-a594-4abf-9d30-21983e9275b5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T07:29:44.862Z_

```json
{
  "parentUuid": "faa016df-fb0e-4c5e-948f-1e79a80c86f5",
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
  "uuid": "42430e74-6e7e-45df-808d-e2b90601ddd1",
  "timestamp": "2026-05-15T07:29:44.862Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "478a83af-a594-4abf-9d30-21983e9275b5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T07:29:44.862Z_

```json
{
  "parentUuid": "42430e74-6e7e-45df-808d-e2b90601ddd1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "79416da9-0167-4d36-a207-b851d992b09e",
  "timestamp": "2026-05-15T07:29:44.862Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "478a83af-a594-4abf-9d30-21983e9275b5",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Self-consistency 优于 CRD 或 CRD 跨基准不泛化；核心 'cross-representation 独特价值' 假设不成立 → 需 reframe 为 empirical analysis paper，仍投 EMNLP main 核心假设：['exp-012: k=5 单表征 maj…",
  "leafUuid": "79416da9-0167-4d36-a207-b851d992b09e",
  "sessionId": "478a83af-a594-4abf-9d30-21983e9275b5"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing cross-representation disagreement boundaries in LLM reasoning",
  "sessionId": "478a83af-a594-4abf-9d30-21983e9275b5"
}
```

---

### Assistant

_source line 8 · 2026-05-15T07:30:03.263Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed "worst" tier predictions for each planned experiment in the experiment plan. I need to carefully go through each experiment, understand what the worst tier means (self-consistency beats CRD, CRD doesn't generalize, core hypothesis fails), and produce realistic predicted results with rationales.

Let me go through the worst tier definition again:
- Self-consistency outperforms CRD or CRD doesn't generalize across benchmarks
- Core "cross-representation unique value" hypothesis doesn't hold
- Reframe as empirical analysis paper, still submit to EMNLP main


Now I'm working through the worst-case scenarios for each experiment. For exp-001, the deep analysis might confirm patterns but fail to strongly support the method claims. With exp-002, DeepSeek could show fundamentally different patterns that reverse the asymmetry and degrade cross-model performance. For exp-003, the ProofWriter pilot might collapse entirely, with LogiQA also showing weak results.

Moving through the rest: exp-004 could see C1 stay above 15% but C2 stall below 60% with noisy disagreement. The repair mechanism in exp-005 might not improve much beyond the baseline, shrinking the Unknown subset gains. Deep analysis in exp-006 could reveal high correlated failures and concerning false agreement rates. Selection might dominate repair in exp-007, leaving no incremental value for the repair approach. The taxonomy-guided strategy in exp-008 could underperform a simpler fixed strategy. Statistical testing in exp-009 might show most confidence intervals crossing zero. Finally, exp-012's self-consistency baseline could outpace the CRD approach by 5+ percentage points even at lower k values.

For exp-013, I'm concerned the taxonomy cross-validation might show weak inter-rater agreement below 0.40, suggesting the taxonomy is too model-dependent to generalize. Now I need to write out detailed predictions for each of these scenarios.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79416da9-0167-4d36-a207-b851d992b09e",
  "isSidechain": false,
  "requestId": "req_011Cb3xk2Y84FgPue6h34bP4",
  "type": "assistant",
  "uuid": "06acfb99-19ba-48ae-9dc1-00c83681c4a4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "478a83af-a594-4abf-9d30-21983e9275b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017gqBmyw3EiXimv1hFuVcz2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13461,
      "cache_read_input_tokens": 11841,
      "output_tokens": 14637,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13461,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 14637,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13461,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13461
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

_source line 9 · 2026-05-15T07:34:10.755Z_

```yaml
tier: worst
narrative_guidance: >
  放弃 "CRD 是更好的诊断工具" 方法论 claim，转为 "cross-representation disagreement 的实证解剖"。
  新 story：(1) LLM 形式化为 FOL 和 Code 时失败模式高度不对称且互补（75% one-side-only），这本身是关于 LLM 能力结构的重要发现；
  (2) 但这种互补性不足以构建可靠的诊断/修复 pipeline，因为 self-consistency 更简单且同样有效；
  (3) 我们量化了 cross-representation 方法的边界条件——何时有效、何时失败、为什么失败。
  标题改为 "When Do Two Formalizations Know More Than One? An Empirical Study of Cross-Representation Disagreement in LLM Reasoning"。
  仍投 EMNLP main，定位为高质量 negative/boundary result paper。

imagined_experiments:
  - name: "FOLIO 完整分析（MVP 数据深度挖掘）"
    plan_id: "exp-001"
    description: "基于 204 样本 MVP 数据的完整统计分析，含 bootstrap CI、Fisher test、分层分析、相关性分析、cost-effectiveness。"
    expected_results:
      C1_disagree_rate: "42.2% [35.3%, 49.0%]"
      C2_diagnostic_rate: "87.2% [81.3%, 94.7%]"
      C4_targeted_delta_aggregate: "+4.65pp"
      C4_bootstrap_CI: "[-8.8%, +18.1%]"
      C4_fisher_p: 0.626
      C4_GT_True: "-13.6pp"
      C4_GT_False: "+11.6pp"  # worst 档下修正：exp-006 深挖后发现 +6.7pp 更合理（部分 False 样本实为 correlated failure）
      C4_GT_Unknown: "+14.7pp"
      C5_committed_accuracy: "53.0% [41.0%, 65.1%]"
      phi_coefficient: 0.189
      phi_p: 0.007
      complementary_error_rate: "75%"
      cost_multiplier: "5.76x"
      accuracy_gain_over_code_only: "+21.6pp"
    result_rationale: >
      exp-001 数据已固定，worst 档不改变已有数值。但 worst 档的关键在于：这些数值在后续实验的对照下被重新解读。
      C4 aggregate CI 含零（[-8.8%, +18.1%]）且 Fisher p=0.626 已经是 worst 档的核心支撑——
      repair 在统计上不显著。phi=0.189 说明 FOL 和 Code 的失败只有微弱正相关，表面上支持互补性，
      但在 worst 档下，exp-012 会证明 self-consistency 以更低成本达到类似效果，
      使得这个 "互补性" 的实用价值大打折扣。cost_multiplier=5.76x 在 worst 档叙事中从 "合理代价" 变为
      "CRD 比 SC5 贵 3-4 倍但精度更低" 的负面论据。
      深度挖掘会揭示 GT=True 的 -13.6pp 不是边缘问题而是系统性缺陷：
      CRD 在高置信正确样本上的 overcorrection 是方法论层面的固有弱点。
    tables:
      - name: "Table 1: FOLIO C1-C5 Metrics with Bootstrap 95% CI"
        columns: ["Metric", "Value", "95% CI", "MVP Gate"]
        rows:
          - ["C1 (Disagree Rate)", "42.2%", "[35.3%, 49.0%]", "PASS"]
          - ["C2 (Diagnostic Rate)", "87.2%", "[81.3%, 94.7%]", "PASS"]
          - ["C4 (Repair Delta)", "+4.65pp", "[-8.8%, +18.1%]", "FAIL (CI includes 0)"]
          - ["C5 (Localization)", "53.0%", "[41.0%, 65.1%]", "FAIL (<70%)"]
      - name: "Table 2: C4 Repair Delta Stratified by GT Label"
        columns: ["GT Label", "n", "Targeted Acc", "Blind Acc", "Delta"]
        rows:
          - ["True", 72, "63.6%", "77.3%", "-13.6pp"]
          - ["False", 63, "76.7%", "70.0%", "+6.7pp"]
          - ["Unknown", 69, "67.7%", "52.9%", "+14.7pp"]
          - ["Aggregate", 204, "69.1%", "64.5%", "+4.65pp (p=0.626)"]
    figures_description:
      - "Fig 1: Confusion heatmap — FOL vs Code correctness 2x2 (both correct, FOL-only correct, Code-only correct, both wrong)，标注 phi=0.189"
      - "Fig 2: C4 delta by GT label bar chart with bootstrap error bars，清晰展示三组分裂"
    analysis: >
      exp-001 的数据在 worst 档下是 pivotal evidence：它确认了 cross-representation disagreement 是真实现象（C1=42%, C2=87%），
      但同时也暴露了该现象无法转化为可靠工具的三个结构性障碍：(1) repair 无统计显著性，(2) GT=True overcorrection，
      (3) localization 覆盖率不足。在 reframe 后的叙事中，这些数据从 "方法缺陷" 转为 "实证发现的核心"——
      我们精确量化了 cross-representation 方法的能力边界。

  - name: "跨模型消融（FOLIO）"
    plan_id: "exp-002"
    description: "DeepSeek V4 Pro within-model + cross-model 对比，验证分歧来源是表征差异还是模型能力差异。"
    expected_results:
      deepseek_within_C1: "35.3%"
      deepseek_within_C2: "72.1%"
      deepseek_within_C5_committed: "78.6%"
      deepseek_within_asymmetry_ratio: "1.8:1 (Code > FOL)"
      cross_model_C1: "48.0%"
      cross_model_C2: "68.5%"
      cross_model_C4_delta: "+1.2pp"
      cross_model_C4_fisher_p: 0.83
      qwen_fol_acc: 0.82
      deepseek_fol_acc: 0.71
      deepseek_code_acc: 0.79
      asymmetry_direction_reversal: true
      cross_model_C2_range: "[0.55, 0.72]"
    result_rationale: >
      worst 档核心假设：DeepSeek 的 FOL/Code 不对称方向反转。Qwen3-32B 展示 FOL >> Code (5.6:1)，
      DeepSeek V4 Pro 反转为 Code > FOL (1.8:1)。原因：DeepSeek V4 Pro 的代码生成能力显著强于 Qwen，
      但其 FOL 生成不如 Qwen——两个模型在形式化能力上的 profile 截然不同。
      这意味着 "FOL 系统性优于 Code" 不是表征层面的规律，而是模型层面的偶然——
      Qwen 恰好 FOL 能力更强。不对称方向的反转直接摧毁了 Claim 2 中 "5.6:1 asymmetry reveals
      systematic differences in LLM formal logic vs code generation" 这个论点。
      cross-model 条件的 C1 虽然更高（48%，因为两个不同模型的形式化更容易分歧），
      但 C2 降到 68.5%——额外的分歧是噪声而非诊断信号，因为它混合了模型能力差异和表征差异。
      C4 delta 几乎为零，cross-model 的 repair 完全无效。
    tables:
      - name: "Table 3: Cross-Model Ablation on FOLIO (204 samples)"
        columns: ["Condition", "C1", "C2", "C4 Delta", "Asymmetry (FOL:Code)", "Cost"]
        rows:
          - ["Qwen within-model (MVP)", "42.2%", "87.2%", "+4.65pp", "5.6:1 FOL>Code", "5.76x"]
          - ["DeepSeek within-model", "35.3%", "72.1%", "+2.8pp", "1.8:1 Code>FOL", "4.2x"]
          - ["Cross-model (DS-FOL + Qwen-Code)", "48.0%", "68.5%", "+1.2pp", "2.3:1 mixed", "5.1x"]
    figures_description:
      - "Fig 3: Asymmetry reversal visualization — stacked bar 展示 Qwen (FOL>>Code) vs DeepSeek (Code>FOL)，说明不对称性是模型依赖而非表征固有属性"
      - "Fig 4: C2 diagnostic rate scatter — within-model vs cross-model，标注 C2 随 cross-model 下降"
    analysis: >
      不对称方向反转是 worst 档的关键实证发现。这意味着我们不能 claim "FOL 是更可靠的形式化"——
      这只是 Qwen 的特性。在 reframe 后的叙事中，这恰恰成为核心贡献之一：
      "cross-representation disagreement 的结构高度模型依赖，不同 LLM 的形式化能力 profile 决定了
      哪种表征更可靠——这一发现对 practitioner 选择表征策略有直接指导意义。"
      cross-model C2 下降到 68.5% 证明：分歧信号的诊断价值来自 same-model 的表征差异，
      混入模型能力差异反而稀释信号质量。

  - name: "ProofWriter 扩展"
    plan_id: "exp-003"
    description: "ProofWriter pilot 20-30 样本，若 C1<10% 则 fallback 到 LogiQA。"
    expected_results:
      proofwriter_pilot_n: 25
      proofwriter_pilot_C1: "4.0% (1/25)"
      proofwriter_pilot_decision: "FAIL → fallback to LogiQA"
      proofwriter_pilot_fol_acc: "92.0%"
      proofwriter_pilot_code_acc: "88.0%"
      logiqua_n: 150
      logiqua_C1: "12.7% (19/150)"
      logiqua_C2: "63.2% (12/19)"
      logiqua_C4_delta: "+2.1pp"
      logiqua_C4_fisher_p: 0.71
      logiqua_C5_committed: "58.3% (7/12)"
      logiqua_asymmetry: "2.1:1 FOL>Code"
      logiqua_fol_acc: 0.76
      logiqua_code_acc: 0.69
    result_rationale: >
      ProofWriter 是合成数据集，每条规则语义精确无歧义。worst 档下，LLM 对合成数据的形式化几乎不出错——
      FOL 准确率 92%、Code 88%，两者同时犯错的概率极低，分歧率仅 4%（1/25 pilot 样本）。
      这直接验证了 worst 档假设："CRD 跨基准不泛化"——合成数据集上 cross-representation disagreement
      几乎不存在，因为形式化任务过于简单。
      Fallback 到 LogiQA 后情况略好但仍不理想：LogiQA 是多选题而非三分类（True/False/Unknown），
      需要适配 pipeline；即使适配后，C1=12.7% 勉强过 10% 阈值但远低于 FOLIO 的 42.2%。
      C2=63.2% 远低于 FOLIO 的 87.2%——LogiQA 的分歧中只有六成是真正的诊断信号，
      其余是两种表征都在猜的噪声分歧。根本原因：LogiQA 的选项结构使得 LLM
      的形式化路径更相似（都倾向于枚举选项而非独立推理），压缩了 cross-representation 的差异空间。
    tables:
      - name: "Table 4: ProofWriter Pilot Results"
        columns: ["Metric", "Value", "Gate"]
        rows:
          - ["n", 25, "-"]
          - ["C1 (Disagree Rate)", "4.0%", "FAIL (<10%)"]
          - ["FOL Accuracy", "92.0%", "-"]
          - ["Code Accuracy", "88.0%", "-"]
          - ["Decision", "Fallback to LogiQA", "-"]
      - name: "Table 5: LogiQA Fallback Results"
        columns: ["Metric", "LogiQA (n=150)", "FOLIO (n=204, reference)"]
        rows:
          - ["C1 (Disagree Rate)", "12.7%", "42.2%"]
          - ["C2 (Diagnostic Rate)", "63.2%", "87.2%"]
          - ["C4 (Repair Delta)", "+2.1pp (p=0.71)", "+4.65pp (p=0.626)"]
          - ["C5 (Localization)", "58.3%", "53.0%"]
          - ["Asymmetry (FOL:Code)", "2.1:1", "5.6:1"]
    figures_description:
      - "Fig 5: C1 across benchmarks bar chart — FOLIO 42.2% vs LogiQA 12.7%，可视化泛化性下降"
    analysis: >
      ProofWriter pilot 失败 + LogiQA fallback 效果大幅退化，共同证明 CRD 的诊断价值高度依赖
      数据集的自然语言歧义程度。合成数据几乎无分歧，结构化多选题分歧稀疏且低质量。
      在 reframe 叙事中，这是 "boundary condition" 分析的核心证据：
      CRD 有效的前提是自然语言到形式化的翻译存在足够的 interpretation space，
      而合成数据和受限选项都压缩了这个空间。

  - name: "MATH Level 5 扩展"
    plan_id: "exp-004"
    description: "MATH Level 5 上 SymPy 符号推理 vs Python 数值验证的 cross-executable-representation 分析。"
    expected_results:
      math_n: 200
      math_C1: "16.5% (33/200)"
      math_C2: "51.5% (17/33)"
      math_C4_delta_aggregate: "+1.8pp"
      math_C4_fisher_p: 0.82
      math_C4_bootstrap_CI: "[-5.2%, +8.7%]"
      math_C5_committed: "76.5%"
      math_C5_coverage: "41.2%"
      math_sympy_acc: 0.68
      math_python_acc: 0.73
      math_asymmetry: "1.4:1 Python>SymPy"
      math_error_types: 3
      math_dominant_error: "computation_error 45.5%"
      math_phi_coefficient: 0.31
      math_disagreement_noise_rate: "48.5%"
    result_rationale: >
      worst 档假设：C1 ≥ 15% 但 C2 < 60%，disagreement 多为噪声。
      MATH Level 5 的两种可执行路径（SymPy 符号化 vs Python 数值计算）在失败模式上的差异
      不如 FOL vs Code 那么根本——两者都是 "写代码执行"，区别仅在于调用的库不同（SymPy vs NumPy/直接计算）。
      这意味着分歧的来源不是 "形式化范式差异" 而是 "实现细节差异"——SymPy 在某些代数操作上超时或溢出，
      Python 在精度要求高的问题上有浮点误差。这些分歧中近半数（48.5%）是两种路径都错只是错法不同，
      不含诊断信息。C2=51.5% 意味着分歧基本是抛硬币——分歧样本中只有一半能正确定位错误侧。
      phi=0.31 高于 FOLIO 的 0.189，说明 SymPy 和 Python 的失败更相关（都在同类问题上失败），
      进一步压缩了 cross-representation 的互补空间。
      不对称性弱（1.4:1 Python>SymPy），无法复现 FOLIO 上的 "一种表征系统性优于另一种" 的发现。
    tables:
      - name: "Table 6: MATH Level 5 Results (n=200)"
        columns: ["Metric", "MATH", "FOLIO (reference)"]
        rows:
          - ["C1 (Disagree Rate)", "16.5%", "42.2%"]
          - ["C2 (Diagnostic Rate)", "51.5%", "87.2%"]
          - ["C4 (Repair Delta)", "+1.8pp (p=0.82)", "+4.65pp (p=0.626)"]
          - ["C5 (Localization)", "76.5% committed / 41.2% coverage", "94.6% / 53.0%"]
          - ["Asymmetry", "1.4:1 Python>SymPy", "5.6:1 FOL>Code"]
          - ["Phi Coefficient", "0.31", "0.189"]
      - name: "Table 7: MATH Disagreement Quality Breakdown"
        columns: ["Category", "Count", "Proportion"]
        rows:
          - ["Diagnostic (one correct)", 17, "51.5%"]
          - ["Both wrong, different answers", 12, "36.4%"]
          - ["Both wrong, same wrong answer", 4, "12.1%"]
    figures_description:
      - "Fig 6: C2 diagnostic rate across domains — FOLIO 87.2% vs LogiQA 63.2% vs MATH 51.5%，展示跨领域退化趋势"
      - "Fig 7: Phi coefficient comparison — 越高的 failure correlation 对应越低的 C2"
    analysis: >
      MATH 的结果直接支持 worst 档核心论点：cross-representation disagreement 的诊断价值不泛化到数学领域。
      SymPy 和 Python 都是 "写代码" 范式，缺乏 FOL vs Code 那样的根本性形式化差异。
      在 reframe 叙事中，这进一步界定了 CRD 的有效边界：需要真正不同的形式化范式（声明式 vs 命令式），
      而非同一范式下的库替换。这是 practitioner guideline 的重要输入。

  - name: "Repair 机制改进"
    plan_id: "exp-005"
    description: "多轮 repair（max 3 rounds）+ 错误类型特定修复策略，按 GT label 和 error_type 分层。"
    expected_results:
      repair_rounds_median: 1.3
      repair_round2_additional_fixes: "4/86 (4.7%)"
      repair_round3_additional_fixes: "1/86 (1.2%)"
      C4_delta_GT_Unknown_improved: "+16.2pp"
      C4_delta_GT_False_improved: "+8.1pp"
      C4_delta_GT_True_improved: "-11.3pp"
      C4_delta_aggregate_improved: "+5.9pp"
      C4_improved_fisher_p: 0.48
      C4_improved_bootstrap_CI: "[-6.1%, +17.9%]"
      error_specific_vs_generic_delta: "+1.3pp"
      error_specific_logic_error_delta: "+2.1pp"
      error_specific_negation_error_delta: "+0.4pp"
      error_specific_quantifier_error_delta: "-0.8pp"
    result_rationale: >
      worst 档下，多轮 repair 的边际收益极小。Round 2 仅修复 4.7% 的额外样本，Round 3 仅 1.2%，
      因为 repair 失败的根因不是 "尝试次数不够" 而是 "诊断信息不足以指导正确修复"。
      LLM 在第一轮 repair 已经利用了分歧信息中的全部有用信号，后续轮次只是在随机搜索。
      GT=True 的 overcorrection 略有缓解（-11.3% vs -13.6%）但仍然严重——
      多轮 repair 的 "更多尝试" 反而放大了 overcorrection 倾向（模型更坚持 "必须修改"）。
      错误类型特定策略仅在 logic_error 上有小幅提升（+2.1pp），其他类型效果为零或负，
      因为 taxonomy 本身不够稳定（exp-013 会证明 κ < 0.40），基于不稳定分类的特定策略不如通用策略。
      aggregate C4 仍无统计显著性（p=0.48, CI 含零）。
    tables:
      - name: "Table 8: Multi-Round Repair Results (FOLIO, n=204)"
        columns: ["Condition", "C4 Delta", "Fisher p", "95% CI"]
        rows:
          - ["Single-round (MVP)", "+4.65pp", "0.626", "[-8.8%, +18.1%]"]
          - ["Multi-round (max 3)", "+5.9pp", "0.48", "[-6.1%, +17.9%]"]
          - ["Multi-round + error-specific", "+7.2pp", "0.39", "[-5.0%, +19.4%]"]
      - name: "Table 9: Multi-Round Repair by GT Label"
        columns: ["GT Label", "Single-Round Delta", "Multi-Round Delta", "Change"]
        rows:
          - ["True", "-13.6pp", "-11.3pp", "+2.3pp"]
          - ["False", "+6.7pp", "+8.1pp", "+1.4pp"]
          - ["Unknown", "+14.7pp", "+16.2pp", "+1.5pp"]
    figures_description:
      - "Fig 8: Repair success rate by round — rapidly diminishing returns curve"
    analysis: >
      多轮 repair 和错误特定策略的边际提升不足以改变统计结论。aggregate C4 仍含零。
      这证明 repair 的瓶颈不在尝试次数或策略细节，而在诊断信号本身的信息量上限。
      在 reframe 叙事中，这强化了 "互补性不足以构建可靠修复 pipeline" 的论点。

  - name: "Unknown 样本深度分析 + correlated failure 定量"
    plan_id: "exp-006"
    description: "Code overclaiming 机制分析、phi 按 GT 分层、false agreement rate、error 分类。"
    expected_results:
      code_overclaiming_rate_unknown: "73.9% (51/69 Unknown 样本中 Code 给出 True/False)"
      fol_overclaiming_rate_unknown: "31.9% (22/69)"
      phi_GT_True: 0.28
      phi_GT_False: 0.15
      phi_GT_Unknown: 0.08
      false_agreement_rate_overall: "11.8% (24/204)"
      false_agreement_rate_True: "4.2% (3/72)"
      false_agreement_rate_False: "7.9% (5/63)"
      false_agreement_rate_Unknown: "23.2% (16/69)"
      specification_vs_formalization_error_split: "38%/62%"
    result_rationale: >
      Code overclaiming 在 Unknown 样本上极为严重（73.9%）——Python 代码倾向于给出确定性答案
      而非 "无法确定"，因为代码执行天然产生 True/False 输出，缺少 "Unknown" 的自然表达。
      这解释了为什么 CRD 在 Unknown 子组上 C4 delta 最高：分歧信号其实主要检测的是 Code overclaiming，
      而非真正的形式化错误。
      phi 按 GT 分层揭示：Unknown 样本的 phi 最低（0.08），说明两种表征在 Unknown 上的失败几乎独立——
      但这种 "独立性" 不是好消息，而是因为两种表征在 Unknown 上都在乱猜，只是猜的方向不同。
      false agreement rate 在 Unknown 上高达 23.2%——近四分之一的 Unknown 样本两条路径都错但答案一致，
      CRD 完全无法检测这些样本。这是 CRD 的根本盲区。
      62% 的错误是 formalization-specific（翻译错误），38% 是 specification-level（对问题本身理解错误）。
      后者两条路径通常犯同样的错，CRD 对此无能为力。
    tables:
      - name: "Table 10: Correlated Failure Analysis by GT Label"
        columns: ["GT Label", "Phi", "False Agreement Rate", "Code Overclaiming Rate"]
        rows:
          - ["True", 0.28, "4.2%", "N/A"]
          - ["False", 0.15, "7.9%", "N/A"]
          - ["Unknown", 0.08, "23.2%", "73.9%"]
          - ["Overall", 0.189, "11.8%", "-"]
    figures_description:
      - "Fig 9: False agreement rate heatmap by GT label × error type"
      - "Fig 10: Code overclaiming distribution — 对 Unknown 样本，Code 输出的 True/False/Unknown 分布"
    analysis: >
      Unknown 子组的 C4 delta 主要来自 Code overclaiming 检测，而非深层诊断。
      23.2% 的 false agreement rate 是 CRD 方法论的固有盲区——当两条路径
      都对问题本身有相同的误解时，分歧信号不存在。这在 reframe 叙事中是
      "为什么 cross-representation 不足以构建可靠 pipeline" 的具体机制解释。

  - name: "Selection vs Repair 消融"
    plan_id: "exp-007"
    description: "检测分歧+定位错误侧后，直接选正确侧 vs 诊断引导修复，按 error_type 分层。"
    expected_results:
      selection_accuracy_all: "78.8% (52/66 diagnostic samples)"
      repair_accuracy_all: "72.7% (48/66)"
      selection_vs_repair_delta: "+6.1pp"
      selection_accuracy_GT_True: "88.9%"
      repair_accuracy_GT_True: "72.2%"
      selection_accuracy_GT_False: "80.0%"
      repair_accuracy_GT_False: "78.3%"
      selection_accuracy_GT_Unknown: "61.9%"
      repair_accuracy_GT_Unknown: "66.7%"
      selection_by_error_type_logic: "+8.2pp over repair"
      selection_by_error_type_negation: "+4.1pp over repair"
      selection_by_error_type_quantifier: "+2.0pp over repair"
      selection_by_error_type_exec_crash: "+12.3pp over repair"
      repair_beats_selection_only_on: "GT=Unknown subset"
    result_rationale: >
      worst 档核心假设：selection > repair 在所有子集上（包括 GT≠True），repair 无任何增量。
      实际预测略有修正：repair 在 GT=Unknown 子集上微弱优于 selection（+4.8pp），
      因为 Unknown 样本的 "正确侧" 经常也不完全正确（FOL 可能输出 True 而非 Unknown），
      repair 可以利用分歧信息生成更准确的 Unknown 判断。
      但在 GT=True 和 GT=False 上，selection 系统性优于 repair——原因很直观：
      如果已经知道哪一侧正确，直接选比修复错误侧更可靠。repair 引入了额外的不确定性
      （修复后的答案可能更错），尤其在 exec_crash 类型上，selection 优势最大（+12.3pp），
      因为 crash 的那侧 repair 难度极高。
      这个结果直接摧毁了 "诊断引导修复" 作为方法论贡献的价值——如果更简单的 selection 更好，
      整个 repair pipeline 的存在意义被质疑。在 reframe 叙事中，这成为 "boundary condition"：
      repair 仅在 ground truth 不可观测且正确侧答案不完全正确时才有小幅优势。
    tables:
      - name: "Table 11: Selection vs Repair (FOLIO diagnostic samples, n=66)"
        columns: ["Condition", "Selection Acc", "Repair Acc", "Δ (Sel-Rep)"]
        rows:
          - ["All diagnostic", "78.8%", "72.7%", "+6.1pp"]
          - ["GT=True", "88.9%", "72.2%", "+16.7pp"]
          - ["GT=False", "80.0%", "78.3%", "+1.7pp"]
          - ["GT=Unknown", "61.9%", "66.7%", "-4.8pp"]
      - name: "Table 12: Selection vs Repair by Error Type"
        columns: ["Error Type", "n", "Selection Acc", "Repair Acc", "Δ"]
        rows:
          - ["logic_error", 38, "76.3%", "68.1%", "+8.2pp"]
          - ["negation_error", 14, "78.6%", "74.5%", "+4.1pp"]
          - ["quantifier_error", 4, "75.0%", "73.0%", "+2.0pp"]
          - ["exec_crash", 10, "90.0%", "77.7%", "+12.3pp"]
    figures_description:
      - "Fig 11: Selection vs Repair accuracy by GT label — grouped bar chart，突出 GT=True 的巨大差距"
    analysis: >
      Selection 系统性优于 repair 是 worst 档对 Claim 3 的致命打击。
      repair 唯一的微弱优势在 GT=Unknown（不可观测标签）上，但这恰恰是最不可操作的场景。
      在 reframe 叙事中，这简化了 practitioner guideline：检测到分歧后，直接选定位为正确的一侧，
      不要尝试修复——这是一个有实用价值的 negative finding。

  - name: "Error Taxonomy 消融"
    plan_id: "exp-008"
    description: "按错误类型分派修复策略 vs 固定策略（统一重生成），验证 taxonomy 的规定性价值。"
    expected_results:
      taxonomy_guided_repair_acc: "73.5%"
      fixed_strategy_repair_acc: "72.7%"
      taxonomy_guided_delta: "+0.8pp"
      taxonomy_guided_fisher_p: 0.91
      taxonomy_useful_only_for: "negation_error (+3.2pp) — 其他类型无差异或负"
      logic_error_taxonomy_vs_fixed: "-0.5pp"
      exec_crash_taxonomy_vs_fixed: "+1.2pp"
    result_rationale: >
      taxonomy 的分类体系在 exp-013 中被证明高度模型依赖（κ < 0.40），
      基于不稳定分类的特定修复策略自然无法系统性优于通用策略。
      唯一例外是 negation_error：取反是明确的操作指令，taxonomy 能准确指导 "翻转否定"，
      但这类错误仅占 10.8%，对 aggregate 贡献微乎其微。
      logic_error 是最大类别（25.5%），但 "逻辑错误" 作为修复指令太宽泛——
      等于告诉模型 "你的逻辑有问题，请修复"，和通用重生成没有本质区别。
      这证明 taxonomy 在当前粒度下缺乏规定性价值（prescriptive value）。
    tables:
      - name: "Table 13: Taxonomy-Guided vs Fixed Strategy Repair"
        columns: ["Error Type", "n", "Taxonomy-Guided", "Fixed (Regen)", "Δ"]
        rows:
          - ["logic_error", 52, "68.3%", "68.8%", "-0.5pp"]
          - ["negation_error", 22, "72.7%", "69.5%", "+3.2pp"]
          - ["quantifier_error", 4, "75.0%", "74.0%", "+1.0pp"]
          - ["exec_crash", 11, "81.8%", "80.6%", "+1.2pp"]
          - ["Aggregate", 89, "73.5%", "72.7%", "+0.8pp (p=0.91)"]
    figures_description: []
    analysis: >
      Taxonomy 缺乏规定性价值——这与 exp-013 的低 κ 互相印证：
      分类体系既不稳定也不实用。在 reframe 叙事中，这是 "为什么失败" 分析的一部分：
      当前错误类型的粒度过粗，无法转化为具体可执行的修复指令。

  - name: "统计显著性全面检验"
    plan_id: "exp-009"
    description: "对所有 benchmark 的 C1-C5 做 bootstrap 95% CI + Fisher exact / McNemar test。"
    expected_results:
      folio_C4_significant: false
      folio_C4_CI: "[-8.8%, +18.1%]"
      folio_C4_mcnemar_p: 0.58
      logiqua_C4_significant: false
      logiqua_C4_CI: "[-5.3%, +9.5%]"
      logiqua_C4_mcnemar_p: 0.74
      math_C4_significant: false
      math_C4_CI: "[-5.2%, +8.7%]"
      math_C4_mcnemar_p: 0.81
      any_benchmark_C4_significant: false
      folio_C1_significant: true
      folio_C2_significant: true
      logiqua_C1_significant: true
      logiqua_C2_significant: false
      math_C1_significant: true
      math_C2_significant: false
      cross_benchmark_C4_meta_effect: "+2.9pp"
      cross_benchmark_C4_meta_CI: "[-2.1%, +7.9%]"
    result_rationale: >
      worst 档核心假设：C4 aggregate 和 stratified 均无统计显著性，bootstrap CI 含零。
      三个 benchmark 的 C4 delta 分别为 +4.65pp (FOLIO), +2.1pp (LogiQA), +1.8pp (MATH)，
      全部 CI 包含零，全部 Fisher/McNemar p > 0.05。即使做 meta-analysis 式的合并，
      效应量仅 +2.9pp 且 CI 仍含零。
      C1 和 C2 在 FOLIO 上是显著的（分歧确实存在且有诊断价值），但在其他 benchmark 上
      C2 不显著——这是 "不泛化" 的统计证据。
      在 reframe 叙事中，统计结果的呈现策略是：承认 repair 无统计显著性，
      将 C1/C2 的显著性作为 "分歧现象的真实性" 的证据（现象存在，但不可操作为工具）。
    tables:
      - name: "Table 14: Statistical Significance Summary Across Benchmarks"
        columns: ["Benchmark", "Metric", "Value", "95% CI", "p-value", "Significant?"]
        rows:
          - ["FOLIO", "C1", "42.2%", "[35.3%, 49.0%]", "<0.001", "Yes"]
          - ["FOLIO", "C2", "87.2%", "[81.3%, 94.7%]", "<0.001", "Yes"]
          - ["FOLIO", "C4", "+4.65pp", "[-8.8%, +18.1%]", "0.626", "No"]
          - ["LogiQA", "C1", "12.7%", "[7.3%, 18.0%]", "<0.001", "Yes"]
          - ["LogiQA", "C2", "63.2%", "[41.5%, 84.9%]", "0.12", "No"]
          - ["LogiQA", "C4", "+2.1pp", "[-5.3%, +9.5%]", "0.71", "No"]
          - ["MATH", "C1", "16.5%", "[11.4%, 21.6%]", "<0.001", "Yes"]
          - ["MATH", "C2", "51.5%", "[34.5%, 68.5%]", "0.47", "No"]
          - ["MATH", "C4", "+1.8pp", "[-5.2%, +8.7%]", "0.82", "No"]
    figures_description:
      - "Fig 12: Forest plot — C4 delta across benchmarks with 95% CI，所有 CI 横跨零线"
    analysis: >
      没有任何 benchmark 的 repair delta 达到统计显著性。C2 在 FOLIO 以外的 benchmark 上也不显著。
      这是 worst 档叙事的统计基石：CRD 作为诊断工具在 FOLIO 上有真实的信号（C1, C2 显著），
      但 (a) 信号无法转化为有效修复（C4 不显著），(b) 信号本身不跨领域泛化（C2 在 LogiQA/MATH 不显著）。

  - name: "Self-consistency baseline 对比"
    plan_id: "exp-012"
    description: "k=5 FOL-only / Code-only majority vote vs single-pass CRD，隔离 cross-representation 独特价值。"
    expected_results:
      # FOLIO
      folio_sc5_fol_precision: "89.3%"
      folio_sc5_fol_recall: "38.9%"
      folio_sc5_code_precision: "82.1%"
      folio_sc5_code_recall: "44.4%"
      folio_crd_precision: "87.2%"
      folio_crd_recall: "42.2%"
      folio_sc5_fol_accuracy: "84.8%"
      folio_sc5_code_accuracy: "72.5%"
      folio_crd_accuracy: "69.1%"
      folio_sc5_fol_cost: "5x"
      folio_crd_cost: "5.76x"
      folio_sc3_fol_accuracy: "83.3%"
      folio_sc3_fol_cost: "3x"
      folio_crd_vs_sc5_fol_delta: "-5.7pp"
      # LogiQA
      logiqua_sc5_code_accuracy: "74.0%"
      logiqua_crd_accuracy: "70.7%"
      logiqua_crd_vs_sc5_delta: "-3.3pp"
      # MATH
      math_sc5_python_accuracy: "78.5%"
      math_crd_accuracy: "74.5%"
      math_crd_vs_sc5_delta: "-4.0pp"
      # Cost efficiency
      crd_cost_ratio_vs_sc5: 0.38
    result_rationale: >
      worst 档核心假设：k=5 单表征 majority vote 精度 > CRD 5pp+，且 k=3 已追平 CRD。
      在 FOLIO 上，k=5 FOL-only majority vote 达到 89.3% precision（vs CRD 87.2%）
      和 84.8% accuracy（vs CRD pipeline 69.1%，即 targeted repair 后的准确率）。
      precision 差距不大（+2.1pp），但 accuracy 差距巨大（+15.7pp），
      因为 SC5 不需要 repair 步骤——majority vote 直接输出答案，避免了 repair 引入的噪声。
      
      关键打击点：k=3 FOL-only 已达 83.3% accuracy，用 3x 成本就超过了 CRD 的 5.76x 成本。
      CRD 不仅精度不如 SC5，成本还更高（5.76x vs 5x），cost-efficiency 全面落败。
      
      根本原因：FOLIO 上 FOL 的基础准确率（82%）远高于 Code（59.8%），
      k=5 majority vote 在高基线上进一步提升了 FOL 的表现。CRD 被 Code 的低准确率拖累——
      cross-representation 不是在互补，而是在用低质量信号（Code）稀释高质量信号（FOL）。
      
      在其他 benchmark 上模式一致：SC5 在各 benchmark 上的最优表征 majority vote 均优于 CRD，
      且成本更低或持平。CRD 的 cost_ratio 为 0.38（即 CRD 每单位准确率提升的 token 成本
      是 SC5 的 2.6 倍），没有 cost-effectiveness 优势。
    tables:
      - name: "Table 15: Self-Consistency vs CRD Comparison (FOLIO, n=204)"
        columns: ["Method", "Precision", "Accuracy", "Cost (vs baseline)", "Δ vs CRD"]
        rows:
          - ["Single-pass FOL", "-", "82.0%", "1x", "+12.9pp"]
          - ["Single-pass Code", "-", "59.8%", "1x", "-9.3pp"]
          - ["SC3 FOL", "86.5%", "83.3%", "3x", "+14.2pp"]
          - ["SC5 FOL", "89.3%", "84.8%", "5x", "+15.7pp"]
          - ["SC5 Code", "82.1%", "72.5%", "5x", "+3.4pp"]
          - ["CRD (1 FOL + 1 Code)", "87.2%", "69.1%*", "5.76x", "baseline"]
        note: "*CRD accuracy = targeted repair accuracy on full 204 samples"
      - name: "Table 16: Cross-Benchmark SC5 vs CRD"
        columns: ["Benchmark", "Best SC5 Acc", "CRD Acc", "Δ", "CRD Cost Ratio"]
        rows:
          - ["FOLIO", "84.8% (FOL)", "69.1%", "-15.7pp", "0.38"]
          - ["LogiQA", "74.0% (Code)", "70.7%", "-3.3pp", "0.41"]
          - ["MATH", "78.5% (Python)", "74.5%", "-4.0pp", "0.42"]
    figures_description:
      - "Fig 13: Accuracy vs Cost scatter — SC3, SC5, CRD 在三个 benchmark 上的 Pareto frontier，CRD 被 SC5 支配"
      - "Fig 14: FOLIO accuracy breakdown — single-pass FOL/Code, SC3/SC5 FOL, CRD pipeline，展示 CRD 被 Code 低准确率拖累"
    analysis: >
      这是 worst 档的核心实验。SC5 在所有 benchmark 上以更低成本达到更高准确率，
      CRD 在 cost-accuracy Pareto frontier 上被完全支配。k=3 FOL-only 已追平甚至超越 CRD。
      Cross-representation 的 "独特价值" 假设不成立——CRD 的分歧信号不如同一表征的多次采样。
      根本原因：cross-representation 引入了异构噪声（Code 的高错误率），
      而 self-consistency 在同质空间内投票，噪声更可控。
      在 reframe 叙事中，这是转折点：我们量化证明了 cross-representation 不如 self-consistency，
      但 WHY 它不如（异构噪声、不对称能力分布）本身是有价值的 empirical finding。

  - name: "Error Taxonomy 交叉验证"
    plan_id: "exp-013"
    description: "DeepSeek V4 Pro 对同一批 FOLIO 分歧样本做错误分类，与 Qwen3-32B 对比，计算 Cohen's κ。"
    expected_results:
      cohens_kappa_4_type: 0.33
      cohens_kappa_binary_logic_vs_other: 0.48
      agreement_rate_raw: "52.3% (45/86)"
      deepseek_logic_error_rate: "35.8%"
      qwen_logic_error_rate: "25.5%"
      deepseek_negation_error_rate: "6.9%"
      qwen_negation_error_rate: "10.8%"
      deepseek_exec_crash_rate: "8.1%"
      qwen_exec_crash_rate: "5.4%"
      category_confusion_matrix_largest_off_diag: "logic_error ↔ negation_error (14 samples)"
      human_proxy_n: 50
      human_proxy_kappa: 0.41
    result_rationale: >
      worst 档核心假设：taxonomy κ < 0.40，分类体系高度模型依赖。
      4-type κ = 0.33（fair agreement），远低于可接受的 0.60 阈值。
      两个模型在 logic_error 和 negation_error 之间有大量混淆（14 个样本），
      因为 "逻辑错误" 和 "否定错误" 的边界本身就是模糊的——
      一个否定处理错误可以被归类为逻辑错误，反之亦然。
      
      DeepSeek 系统性地将更多错误归为 logic_error（35.8% vs 25.5%），
      而 Qwen 更倾向于分出 negation_error（10.8% vs 6.9%）——
      分类反映了模型自身的推理偏好而非错误的客观属性。
      
      二分类（logic vs other）κ = 0.48，好于 4-type 但仍不够强。
      50 样本的 human-proxy（用 GPT-4o 模拟人类标注）κ = 0.41，
      略好于 cross-model 但仍在 "moderate" 区间，说明分类体系本身
      （而非模型差异）是 κ 低的主因——类别定义不够清晰。
    tables:
      - name: "Table 17: Error Taxonomy Cross-Model Validation (FOLIO, n=86 diagnostic samples)"
        columns: ["Error Type", "Qwen3-32B", "DeepSeek V4 Pro", "Agreement"]
        rows:
          - ["logic_error", "25.5% (22)", "35.8% (31)", "14 agree"]
          - ["negation_error", "10.8% (9)", "6.9% (6)", "3 agree"]
          - ["quantifier_error", "2.0% (2)", "3.5% (3)", "1 agree"]
          - ["exec_crash", "5.4% (5)", "8.1% (7)", "4 agree"]
          - ["no_clear_error", "56.3% (48)", "45.7% (39)", "23 agree"]
      - name: "Table 18: Inter-Rater Agreement Summary"
        columns: ["Comparison", "κ (4-type)", "κ (binary)", "Raw Agreement"]
        rows:
          - ["Qwen vs DeepSeek", "0.33", "0.48", "52.3%"]
          - ["Qwen vs Human-Proxy", "0.41", "0.55", "58.0%"]
          - ["DeepSeek vs Human-Proxy", "0.38", "0.51", "54.0%"]
    figures_description:
      - "Fig 15: Confusion matrix heatmap — Qwen vs DeepSeek 错误分类，标注主要 off-diagonal 混淆"
    analysis: >
      κ = 0.33 证明 taxonomy 不具备跨模型稳定性，分类体系反映模型偏好而非客观错误属性。
      这与 exp-008 的结果互相印证——基于不稳定分类的修复策略无法优于通用策略。
      在 reframe 叙事中，taxonomy instability 是 "为什么 CRD 失败" 的关键机制之一：
      如果连错误类型都无法可靠识别，基于错误类型的下游操作（定向修复）自然不可靠。
      同时指出改进方向：需要更粗粒度但更稳定的分类（如 binary: crash vs logical），
      或基于 error pattern 而非 error label 的修复策略。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06acfb99-19ba-48ae-9dc1-00c83681c4a4",
  "isSidechain": false,
  "requestId": "req_011Cb3xk2Y84FgPue6h34bP4",
  "type": "assistant",
  "uuid": "3ed0cb00-51d6-432d-b9ce-2c8e42b3960a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "478a83af-a594-4abf-9d30-21983e9275b5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017gqBmyw3EiXimv1hFuVcz2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13461,
      "cache_read_input_tokens": 11841,
      "output_tokens": 14637,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13461,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 14637,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13461,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13461
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Self-consistency 优于 CRD 或 CRD 跨基准不泛化；核心 'cross-representation 独特价值' 假设不成立 → 需 reframe 为 empirical analysis paper，仍投 EMNLP main 核心假设：['exp-012: k=5 单表征 maj…",
  "leafUuid": "3ed0cb00-51d6-432d-b9ce-2c8e42b3960a",
  "sessionId": "478a83af-a594-4abf-9d30-21983e9275b5"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing cross-representation disagreement boundaries in LLM reasoning",
  "sessionId": "478a83af-a594-4abf-9d30-21983e9275b5"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Self-consistency 优于 CRD 或 CRD 跨基准不泛化；核心 'cross-representation 独特价值' 假设不成立 → 需 reframe 为 empirical analysis paper，仍投 EMNLP main 核心假设：['exp-012: k=5 单表征 maj…",
  "leafUuid": "3ed0cb00-51d6-432d-b9ce-2c8e42b3960a",
  "sessionId": "478a83af-a594-4abf-9d30-21983e9275b5"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterizing cross-representation disagreement boundaries in LLM reasoning",
  "sessionId": "478a83af-a594-4abf-9d30-21983e9275b5"
}
```

---
