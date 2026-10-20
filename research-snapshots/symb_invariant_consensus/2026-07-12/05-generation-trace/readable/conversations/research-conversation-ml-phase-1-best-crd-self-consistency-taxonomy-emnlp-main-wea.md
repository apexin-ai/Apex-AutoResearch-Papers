# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：CRD 信号在精度和成本上明确优于 self-consistency；跨基准/跨模型泛化成立；taxonomy 可复现 → EMNLP main wea

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/5247ca7a-726d-48b5-ab06-75a8e4729652.jsonl`
- **Structured JSON:** [`e32329be40fee9ec90f0.json`](../../sessions/e3/e32329be40fee9ec90f0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T07:19:28.415Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T07:19:28.415Z",
  "sessionId": "5247ca7a-726d-48b5-ab06-75a8e4729652",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：CRD 信号在精度和成本上明确优于 self-consistency；跨基准/跨模型泛化成立；taxonomy 可复现 → EMNLP main weak accept\n核心假设：['exp-012: CRD 诊断精度 ≥ k=5 单表征 majority vote，且 token 成本 ≤ 40%', 'exp-003: 第二基准（ProofWriter 或 LogiQA）C1 ≥ 20%, C2 ≥ 75%', 'exp-004: MATH 双可执行表征 C1 ≥ 15%, C2 ≥ 70%，不对称方向可能反转但仍存在', 'exp-002: DeepSeek within-model C2 在 MVP ±8pp 内，不对称方向一致', \"exp-013: taxonomy Cohen's κ ≥ 0.60\", 'exp-007: repair 在 GT≠True 子集上 ≥ selection +3pp，selection 本身已优于 blind baseline', 'exp-005: 多轮修复将 GT=Unknown delta 从 +14.7pp 拉到 +20pp+']\n关键指标范围：{'C1_new_benchmarks': [0.2, 0.45], 'C2_new_benchmarks': [0.75, 0.92], 'CRD_vs_SC5_precision_delta': [0.0, 0.12], 'CRD_vs_SC5_cost_ratio': [0.3, 0.45], 'cross_model_C2': [0.78, 0.9], 'taxonomy_kappa': [0.6, 0.8], 'C4_unknown_false_combined_delta': [8.0, 18.0], 'selection_vs_blind_delta': [5.0, 15.0], 'repair_vs_selection_delta': [3.0, 8.0], 'C5_committed_accuracy': [0.9, 0.98]}\n叙事方向：原始 framing 完全成立。Cross-representation disagreement 是一个比 within-representation self-consistency 更高效的诊断信号：用 1/3 的 token 成本获得相当或更高的诊断精度。 三条 claim 无需调整——C1/C2 跨三个基准和两个模型稳定，C3 的 GT-label-dependent 效应 在新基准复现，taxonomy 跨模型一致。论文双轨叙事（分析为主 + 方法为辅）自然成立。 Selection ablation 展示 repair 在可诊断子集上的增量价值。Repair 的 GT=True overcorrection 作为 discovered boundary 是加分项而非弱点。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: cross_representation_disagreement_diagno\nfocus: Dream #1 identified 5 structural issues (all 3/6). Key changes since: (1) Added exp-012 self-consistency baseline (P0) — k=5 majority voting vs single-pass CRD, isolates cross-representation value; (2) Added exp-013 error taxonomy cross-model validation; (3) Softened novelty claim from \"first systematic study\" to \"first to extend from filtering to diagnosis\"; (4) Added R8-R11 reviewer concerns covering self-consistency, taxonomy validation, FOL vs CoT commensurability, related work expansion. (5) exp-007 selection-vs-repair promoted to P0. Please evaluate whether these additions address the structural gaps and push best-case toward weak accept.\n\n## paper_framing.md\n\n# Paper Framing — cross_representation_disagreement_diagno\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026 (10 days)\n- Secondary: AAAI 2027 (abstract July 25, full August 1) — extended version with full benchmark coverage\n\n## Core Insight\nWhen the same LLM formalizes a reasoning problem into two distinct executable representations, disagreements between them serve as a high-precision error detection signal (~87% diagnostic rate). This \"disagreement as diagnostic\" approach goes beyond existing methods that only filter or verify within a single representation — the disagreement pattern itself reveals error types, enables localization, and informs selective repair. The value is NOT symmetric complementarity between representations, but the diagnostic information contained in the disagreement signal.\n\n## Core Claims (3 条)\n\n### Claim 1: Disagreement as High-Precision Diagnostic Signal\nWhen the same LLM formalizes a reasoning problem into two distinct representations (FOL/Z3 and executable Python), disagreements occur at a substantial rate (~40%) and are diagnostically informative with high precision (~87%). This cross-representation signal detects formalization-specific errors invisible to within-representation verification.\n\n**MVP evidence**: C1=39.6% disagree rate, C2=86.8% diagnostic rate on FOLIO (204 samples, Qwen3-32B).\n\n### Claim 2: Error Classification and Conditional Localization\nDisagreement patterns enable error type classification into a structured taxonomy (4 types: logic_error 25.5%, negation_error 10.8%, quantifier_error 2.0%, exec_crash 5.4%). When the stability test yields a definitive prediction (62% of diagnostic samples), localization accuracy is high (85.4%). The 5.6:1 asymmetry (FOL correct 56 vs Code correct 10, both wrong 10) reveals systematic differences in LLM formal logic vs. code generation.\n\n**MVP evidence**: C5-committed = 94.6% (35/37) [CI: 86.1%-100%] — when stability test makes a definitive prediction, localization is near-perfect. C5-coverage = 53.0% (35/66) — 44% of diagnostic cases return \"ambiguous\" (especially Unknown: 61%). C3=4 error types.\n\n**Framing**: Stability-based localization is a high-precision / low-recall method. When it commits, it's right 95% of the time. The 44% ambiguous rate is primarily driven by GT=Unknown samples (61% ambiguous) where Code overclaiming creates systematically unstable predictions.\n\n**Key nuance**: GT=Unknown samples have the worst localization coverage (C5-coverage=35.7%) but the best repair delta (+14.7pp). This paradox suggests repair utility comes from the disagreement PATTERN (information content) rather than precise error-side identification — the model benefits from knowing the two representations disagree and what each concluded, regardless of which is labeled \"the error.\"\n\n### Claim 3: Diagnosis-Guided Repair Is GT-Label-Dependent — Helps, Hurts, or Neutral\nDiagnosis-guided repair exhibits a striking GT-label-dependent effect that reveals the boundary of cross-representation diagnosis:\n\n| GT Label | n | Targeted | Blind | Delta | Interpretation |\n|----------|---|----------|-------|-------|----------------|\n| Unknown | 69 | 67.7% | 52.9% | **+14.7pp** | Diagnosis helps: corrects Code overclaiming |\n| False | 63 | 76.7% | 70.0% | **+6.7pp** | Modest help |\n| True | 72 | 63.6% | 77.3% | **-13.6pp** | Diagnosis HURTS: overcorrection |\n\nThis is NOT simply \"conditional advantage\" — diagnosis actively harms repair for GT=True cases. The mechanism: for True problems where Code outputs False/Unknown, the diagnostic signal (\"Code disagrees with FOL\") triggers overcorrection, producing worse results than blind regeneration. We do NOT claim aggregate repair superiority — we characterize a fundamental asymmetry in when diagnosis helps vs. hurts repair.\n\n**MVP evidence**: C4 aggregate +4.65pp per-sample (Fisher p=0.626, not significant). The aggregate masks a three-way split that is the actual finding. Bootstrap CI for aggregate includes zero.\n\n**Presentation strategy**: \n1. Report C4 stratified by GT label as the PRIMARY result (table above)\n2. Aggregate C4 only as context, with explicit caveat about non-significance\n3. Frame GT=True overcorrection as a discovered failure mode, not a hidden weakness\n4. Discuss implications: practitioners should apply diagnosis-guided repair selectively (skip for high-confidence True predictions)\n\n## Story Spine\n\n- **Problem**: Neurosymbolic reasoning pipelines suffer from formalization errors as their dominant failure mode. The LLM's translation from natural language to formal representation introduces subtle corruptions. Current approaches either select one representation (HybridMind, Adaptive Selection), verify within one representation (VeriCoT, VERGE, Roundtrip Verification), or filter disagreeing solutions without diagnosis (Liang et al. 2024, Prove 2024). The gap: nobody uses cross-representation disagreement patterns for error CATEGORIZATION and TARGETED REPAIR.\n\n- **Existing approaches & gaps**: Liang et al. (2024) proved CoT-PoT disagreement is informative for filtering but stopped at discarding disagreements — no error categorization, no repair. Roundtrip Verification (2026) showed diagnosis-guided repair works within a single representation on a narrow domain (150 traffic rules). No method exploits cross-representation disagreement as a diagnostic signal enabling categorized diagnosis and targeted repair.\n\n- **Our framing (dual-track)**: We present (1) the first study to extend cross-representation disagreement from a binary filtering signal (Liang et al. 2024) to a structured diagnostic tool — enabling error classification, localization, and boundary characterization across domains and models; and (2) a lightweight diagnosis-guided repair framework that operates at inference time without model modification. The analysis is the primary contribution; the repair framework demonstrates downstream utility. Key distinction from self-consistency (Wang et al. 2023): within-representation sampling captures generation variance; cross-representation disagreement captures systematic formalization differences between paradigms (formal logic vs. imperative code).\n\n- **Headline result template**: \"On [benchmarks], cross-representation disagreement detects [X]% of samples as potentially erroneous with [Y]% diagnostic precision and [Z]% error localization accuracy. We characterize a fundamental asymmetry: [logic representation] exhibits [N]x lower formalization error rate than [code representation], revealing systematic differences in how LLMs handle formal logic vs. imperative code generation.\"\n\n## Venue Fit\n\n- **EMNLP fit (strong)**: NLP + symbolic reasoning is a core track. Dual-track framing (systematic analysis + method) aligns with EMNLP's tradition of accepting empirical analyses. The correlated failure / boundary characterization angle fits EMNLP's emphasis on rigorous evaluation.\n- **Risk**: modest repair improvement → mitigate by framing analysis as primary contribution, repair as secondary.\n- **Risk**: single model+dataset insufficient → extend to ≥2 models and ≥3 benchmarks in research phase.\n\n## Anticipated Reviewer Concerns & Responses\n\n| # | Concern | Response Strategy | Required Experiment |\n|---|---------|-------------------|---------------------|\n| R1 | Single model/dataset — generalization? | Cross-model ablation + multi-benchmark | exp-002, exp-003, exp-004 |\n| R2 | C4 repair improvement marginal | Honest framing + boundary characterization as contribution | exp-005, exp-006 |\n| R3 | Why repair, not just select correct side? | Selection vs repair ablation | exp-007 |\n| R4 | Error taxonomy rule-based, not learned | Deliberate choice for interpretability; taxonomy-guided vs fixed strategy ablation | exp-008 |\n| R5 | FOL 9:1 asymmetry — just FOL-as-verifier? | Test on math domain where asymmetry may differ | exp-004 |\n| R6 | Statistical significance? | Bootstrap CI + Fisher exact test on all metrics | exp-009 |\n| R7 | Correlated failures (Denisov-Blanch 2026) | Explicit quantification + cross-model ablation reduces correlation | exp-002, exp-006 |\n| R8 | How differs from self-consistency (k=5 majority voting)? | Dedicated baseline: k=5 FOL-only and k=5 Code-only vs single-pass CRD. Cross-representation captures paradigm-level differences, not sampling variance | exp-012 |\n| R9 | Error taxonomy unvalidated — no inter-annotator agreement | Cross-model validation: use different LLM to classify same errors, measure Cohen's κ. If possible, small human annotation (50 samples) | exp-013 |\n| R10 | FOL+Z3 vs CoT+SymPy are categorically different — conflating them as \"cross-representation\" is imprecise | Frame MATH domain as \"cross-executable-paradigm\" (symbolic algebra vs numerical computation), acknowledge different verification guarantees. Discuss as related but distinct instantiation | exp-004 framing |\n| R11 | Related work insufficient — missing self-consistency, LEVER, Faithful CoT, self-debug/refine, multi-agent debate, ensemble diversity | Expand related work to ≥25 references, position against all listed methods. Paper Agent must run reference-audit | Paper writing |\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'FOLIO 完整分析（MVP 数据深度挖掘）: 基于 204 样本 MVP 数据，完成： (a) 统计显著性检验（Bootstrap\n    95% CI + Fisher exact test） (b) 错误类型详细分类和分布 (c) GT=Unknown vs non-Unknown 子集 C1-C5\n    分层分析 (d) 分歧不对称性 9:1 breakdown (e) FOL/Code 失败相关性定量分析（phi coefficient / tetrachoric\n    correlation）— Claim 3 核心支撑 (f) cost-effectiveness 分析（每单位 token 成本的 accuracy gain）\n    不需要新实验运行，纯分析。\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: mvp_pipeline_004\n  status: ANALYZING\n  conclusion: success\n  metrics:\n    progress: 204/204 (deduped from 211)\n    deduped: true\n    unified_per_sample:\n      all_mode:\n        C1_disagree_rate: 42.16% (86/204)\n        C2_diagnostic_rate: 87.21% (75/86)\n        C3_error_types: 4 types\n        C4_targeted_delta: +4.65pp\n        C5_localization_acc: 53.03% (35/66)\n        C5_CI_95: '[41.0%, 65.1%]'\n        mvp_pass: 3/5 (C4 FAIL, C5 FAIL)\n      excl_unknown:\n        C1_disagree_rate: 38.52% (52/135)\n        C2_diagnostic_rate: 84.62% (44/52)\n        C3_error_types: 3 types\n        C4_targeted_delta: -1.92pp\n        C5_localization_acc: 65.79% (25/38)\n        C5_CI_95: '[50.0%, 80.6%]'\n        mvp_pass: 2/5 (C4 FAIL, C5 borderline PASS)\n    evaluate_mvp_per_side:\n      note: 保留为内部参考，不用于论文\n      all_mode_mvp_pass: 5/5 PASS\n    deep_analysis:\n      bootstrap_CI:\n        C1: '[35.3%, 49.0%]'\n        C2: '[81.3%, 94.7%]'\n        C4_delta: '[-8.8%, +18.1%]'\n        C5: '[41.0%, 65.1%]'\n      fisher_C4_pvalue:\n        all_mode: 0.626\n        excl_unknown: 1\n      asymmetry: FOL_correct_Code_wrong=56, Code_correct_FOL_wrong=10 (5.6:1)\n      gt_subset_C4:\n        'True': -13.6%\n        'False': +11.6%\n        Unknown: +14.7%\n      dominant_error: logic_error 25.5% (52/204)\n      phi_coefficient:\n        overall: 0.189\n        overall_p: 0.007\n      complementary_errors: 75/100 (75%) one-side-only failures\n      cost_effectiveness:\n        cost_multiplier: 5.76x\n        code_only_acc: 0.598\n        pipeline_acc: 0.814\n        oracle_acc: 0.878\n        accuracy_gain: +21.6pp\n- id: exp-002\n  claim:\n  - 1\n  - 2\n  description: '跨模型消融（FOLIO）: 三组条件对比—— (a) Qwen3-32B FOL + Qwen3-32B Code（MVP baseline，within-model）\n    (b) DeepSeek V4 Pro FOL + DeepSeek V4 Pro Code（within-model DeepSeek 对照） (c) DeepSeek\n    V4 Pro FOL + Qwen3-32B Code（cross-model） 目的：区分分歧来源是表征差异还是模型能力差异。FOLIO 204 样本。\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  api_cost_estimate: $30-50 (DeepSeek V4 Pro 2 组 + Qwen Cloud 1 组)\n  status: planned\n- id: exp-003\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'ProofWriter 扩展: 先跑 20-30 样本 pilot 验证 disagree_rate。 ProofWriter 是合成数据（无\n    NL 歧义），baseline accuracy 可能 >90%， C1 有低于 10% 的风险。Pilot 通过（disagree_rate ≥ 10%）则全量跑；\n    Pilot 失败则切换到 LogiQA（自然语言逻辑推理，歧义性更高）。\n\n    '\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  pilot_required: true\n  fallback_dataset: LogiQA\n  status: planned\n- id: exp-004\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'MATH Level 5 扩展: 使用两种可执行表征保持 framing 一致—— (a) SymPy 符号推理（代数化简、方程求解）\n    (b) Python 数值验证（直接计算、枚举、数值近似） 两条路径均可执行，保持与 FOLIO（FOL/Z3 vs Python）一致的 \"cross-executable-representation\"\n    框架。不使用 CoT（不可执行）。\n\n    '\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  status: planned\n- id: exp-005\n  claim: 3\n  description: 'Repair 机制改进: 多轮 repair（max 3 rounds）、加入错误类型特定修复策略、 对比 repair 前后 C4\n    delta。按 GT label 和 error_type 分层报告， 不报 aggregate。目标：在 Unknown 子组进一步拉大 delta， 在\n    non-Unknown 子组探索是否有改善空间。\n\n    '\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  status: planned\n- id: exp-006\n  claim: 3\n  description: 'Unknown 样本深度分析 + correlated failure 定量: (a) 为什么 GT=Unknown 样本驱动 C4\n    delta？Code overclaiming 机制分析 (b) FOL/Code 失败的相关系数（phi coefficient）按 GT label 分层\n    (c) false agreement rate 量化（两条路径都错但答案一致的比例） (d) specification-level vs formalization-specific\n    错误分类\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n- id: exp-007\n  claim: 3\n  description: 'Selection vs Repair 消融（Dream 审稿三档均要求）: 检测分歧+定位错误侧后， 直接选正确侧答案 vs 诊断引导修复。按\n    error_type 分层报告。 Dream 三档 Median 指出 selection nearly matches repair — 需量化。 回应\n    Reviewer Concern R3。\n\n    '\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  claim: 2\n  description: 'Error Taxonomy 消融: 按错误类型分派修复策略 vs 固定策略（统一重生成）， 验证 taxonomy 的规定性价值。\n\n    '\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-005\n  status: planned\n- id: exp-009\n  claim:\n  - 1\n  - 2\n  - 3\n  description: '统计显著性全面检验: 对所有 benchmark 的 C1-C5 指标做 bootstrap 95% CI + Fisher exact\n    test / McNemar test， 确保所有 claim 有统计支撑。\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-003\n  - exp-004\n  status: planned\n- id: exp-012\n  claim:\n  - 1\n  description: 'Self-consistency baseline 对比（三档一致 CRITICAL 缺失）: 在 FOLIO + ProofWriter\n    + MATH 上对比: (a) k=5 FOL-only majority vote (b) k=5 Code-only majority vote (c)\n    Single-pass CRD（我们的方法，1 FOL + 1 Code） 目的：隔离 cross-representation 信号 vs 单表征 sampling\n    diversity。 如果 k=5 单表征已达到相近诊断精度，需要 reframe 贡献。 如果 CRD 在更少 token 成本下匹配或超过 k=5，则\n    cost-effectiveness 是卖点。\n\n    '\n  priority: P0\n  gpu_budget_hours: 6\n  deps:\n  - exp-001\n  api_cost_estimate: $20-30\n  status: planned\n- id: exp-013\n  claim:\n  - 2\n  description: 'Error Taxonomy 交叉验证（三档一致弱点）: (a) 用 DeepSeek V4 Pro 对同一批 FOLIO 分歧样本做错误分类，与\n    Qwen3-32B 分类对比，计算 Cohen''s κ (b) 如果时间允许，50 个样本人工标注（用户或 LLM-as-human-proxy） (c)\n    报告分类一致性 + 错误类型分布是否跨模型稳定 目的：回应 Dream 审稿三档一致要求的 taxonomy validation\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  api_cost_estimate: $10-20\n  status: planned\n- id: exp-010\n  claim:\n  - 1\n  - 2\n  description: 'Qwen3-8B 消融: 低能力模型上的诊断率和分歧率变化。'\n  priority: P2\n  gpu_budget_hours: 4\n  deps: []\n  status: planned\n- id: exp-011\n  claim:\n  - 1\n  - 2\n  description: 'GPQA Diamond 扩展: 科学知识推理，SymPy/Python 双可执行表征。'\n  priority: P2\n  gpu_budget_hours: 6\n  deps:\n  - exp-004\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_baseline_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.74\n    correct: 37\n    total: 50\n    gate: PASS_FOLIO\n- exp_id: mvp_pipeline_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    disagree_rate: 0.04\n    diagnostic_rate: 1\n    error_types: 4\n    targeted_repair: 0.1875\n    blind_repair: 0.4688\n    delta_pp: -28.12\n    localization: 0.4186\n    fol_accuracy: 0.14\n    code_accuracy: 0.52\n    C1: false\n    C2: true\n    C3: true\n    C4: false\n    C5: false\n- exp_id: mvp_pipeline_002\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    fol_crash_rate_v2: 0.1\n    code_crash_rate_v2: 0.4\n    fol_crash_rate_v3: 0.8\n    code_crash_rate_v3: 0\n    fol_accuracy_v3: 0.2\n    code_accuracy_v3: 0.6\n    oracle_accuracy_v3: 0.6\n    disagree_rate_v3: 0\n    effective_disagree_rate_v3: 0\n    diagnostic_rate_v3: null\n    targeted_rate_v3: 0.5\n    blind_rate_v3: 0.625\n    delta_pp_v3: -12.5\n    localization_accuracy_v3: 0.5\n    error_types_v3: 3\n    C1_v3: false\n    C2_v3: false\n    C3_v3: true\n    C4_v3: false\n    C5_v3: false\n    avg_time_per_sample_s_v3: 218.5\n    total_api_calls_v3: 48\n    input_tokens_v3: 50558\n    output_tokens_v3: 139706\n    samples_v3: 10\n    v3_changes: enable_thinking=False for Code generation, _strip_thinking unclosed\n      tag handling\n- exp_id: mvp_pipeline_003\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_003b\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_004\n  name: ''\n  status: ANALYZING\n  conclusion: success\n  metrics:\n    progress: 204/204 (deduped from 211)\n    deduped: true\n    unified_per_sample:\n      all_mode:\n        C1_disagree_rate: 42.16% (86/204)\n        C2_diagnostic_rate: 87.21% (75/86)\n        C3_error_types: 4 types\n        C4_targeted_delta: +4.65pp\n        C5_localization_acc: 53.03% (35/66)\n        C5_CI_95: '[41.0%, 65.1%]'\n        mvp_pass: 3/5 (C4 FAIL, C5 FAIL)\n      excl_unknown:\n        C1_disagree_rate: 38.52% (52/135)\n        C2_diagnostic_rate: 84.62% (44/52)\n        C3_error_types: 3 types\n        C4_targeted_delta: -1.92pp\n        C5_localization_acc: 65.79% (25/38)\n        C5_CI_95: '[50.0%, 80.6%]'\n        mvp_pass: 2/5 (C4 FAIL, C5 borderline PASS)\n    evaluate_mvp_per_side:\n      note: 保留为内部参考，不用于论文\n      all_mode_mvp_pass: 5/5 PASS\n    deep_analysis:\n      bootstrap_CI:\n        C1: '[35.3%, 49.0%]'\n        C2: '[81.3%, 94.7%]'\n        C4_delta: '[-8.8%, +18.1%]'\n        C5: '[41.0%, 65.1%]'\n      fisher_C4_pvalue:\n        all_mode: 0.626\n        excl_unknown: 1\n      asymmetry: FOL_correct_Code_wrong=56, Code_correct_FOL_wrong=10 (5.6:1)\n      gt_subset_C4:\n        'True': -13.6%\n        'False': +11.6%\n        Unknown: +14.7%\n      dominant_error: logic_error 25.5% (52/204)\n      phi_coefficient:\n        overall: 0.189\n        overall_p: 0.007\n      complementary_errors: 75/100 (75%) one-side-only failures\n      cost_effectiveness:\n        cost_multiplier: 5.76x\n        code_only_acc: 0.598\n        pipeline_acc: 0.814\n        oracle_acc: 0.878\n        accuracy_gain: +21.6pp\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-15T07:19:28.422Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T07:19:28.422Z",
  "sessionId": "5247ca7a-726d-48b5-ab06-75a8e4729652"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-15T07:19:28.457Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：CRD 信号在精度和成本上明确优于 self-consistency；跨基准/跨模型泛化成立；taxonomy 可复现 → EMNLP main weak accept
核心假设：['exp-012: CRD 诊断精度 ≥ k=5 单表征 majority vote，且 token 成本 ≤ 40%', 'exp-003: 第二基准（ProofWriter 或 LogiQA）C1 ≥ 20%, C2 ≥ 75%', 'exp-004: MATH 双可执行表征 C1 ≥ 15%, C2 ≥ 70%，不对称方向可能反转但仍存在', 'exp-002: DeepSeek within-model C2 在 MVP ±8pp 内，不对称方向一致', "exp-013: taxonomy Cohen's κ ≥ 0.60", 'exp-007: repair 在 GT≠True 子集上 ≥ selection +3pp，selection 本身已优于 blind baseline', 'exp-005: 多轮修复将 GT=Unknown delta 从 +14.7pp 拉到 +20pp+']
关键指标范围：{'C1_new_benchmarks': [0.2, 0.45], 'C2_new_benchmarks': [0.75, 0.92], 'CRD_vs_SC5_precision_delta': [0.0, 0.12], 'CRD_vs_SC5_cost_ratio': [0.3, 0.45], 'cross_model_C2': [0.78, 0.9], 'taxonomy_kappa': [0.6, 0.8], 'C4_unknown_false_combined_delta': [8.0, 18.0], 'selection_vs_blind_delta': [5.0, 15.0], 'repair_vs_selection_delta': [3.0, 8.0], 'C5_committed_accuracy': [0.9, 0.98]}
叙事方向：原始 framing 完全成立。Cross-representation disagreement 是一个比 within-representation self-consistency 更高效的诊断信号：用 1/3 的 token 成本获得相当或更高的诊断精度。 三条 claim 无需调整——C1/C2 跨三个基准和两个模型稳定，C3 的 GT-label-dependent 效应 在新基准复现，taxonomy 跨模型一致。论文双轨叙事（分析为主 + 方法为辅）自然成立。 Selection ablation 展示 repair 在可诊断子集上的增量价值。Repair 的 GT=True overcorrection 作为 discovered boundary 是加分项而非弱点。


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
tier: best
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
  "promptId": "29f69a91-4512-4ba6-bc39-c4b31123db89",
  "type": "user",
  "uuid": "8ff5afe0-2bac-42e2-a31c-059400ce0b1b",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "5247ca7a-726d-48b5-ab06-75a8e4729652",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T07:19:28.455Z_

```json
{
  "parentUuid": "8ff5afe0-2bac-42e2-a31c-059400ce0b1b",
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
  "uuid": "47076717-b095-4a48-a599-c78298fb6688",
  "timestamp": "2026-05-15T07:19:28.455Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "5247ca7a-726d-48b5-ab06-75a8e4729652",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T07:19:28.455Z_

```json
{
  "parentUuid": "47076717-b095-4a48-a599-c78298fb6688",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b033866f-b64f-4400-ab19-4521ba54f5ee",
  "timestamp": "2026-05-15T07:19:28.455Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "5247ca7a-726d-48b5-ab06-75a8e4729652",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：CRD 信号在精度和成本上明确优于 self-consistency；跨基准/跨模型泛化成立；taxonomy 可复现 → EMNLP main weak accept 核心假设：['exp-012: CRD 诊断精度 ≥ k=5 单表征 majority vote，且 token 成本 ≤ 40%', 'e…",
  "leafUuid": "b033866f-b64f-4400-ab19-4521ba54f5ee",
  "sessionId": "5247ca7a-726d-48b5-ab06-75a8e4729652"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-representation disagreement diagnostic signal validation",
  "sessionId": "5247ca7a-726d-48b5-ab06-75a8e4729652"
}
```

---

### Assistant

_source line 8 · 2026-05-15T07:19:44.962Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for the "best" tier across all planned experiments in the experiment plan. Each prediction needs a result_rationale explaining why the results would look that way under the best-case scenario.

Let me carefully go through each experiment and generate realistic best-case predictions that are consistent with:
1. The best tier definition (weak accept at EMNLP main)
2. The key metric ranges provided
3. The MVP data already collected
4. The narrative direction

Let me work through each experiment systematically.

**exp-001**: Already done (ANALYZING status), so I need to predict the final deep analysis results.


**exp-002**: For the cross-model ablation on FOLIO with DeepSeek V4 Pro, I'm predicting DeepSeek's within-model C2 performance stays within ±8 percentage points of the MVP baseline with consistent asymmetry patterns. **exp-003**: The ProofWriter or LogiQA extension should hit at least 20% on C1 and 75% on C2 in the best case. **exp-004**: MATH Level 5 with SymPy versus Python numerical approaches would reach 15% or higher on C1 and 70% or higher on C2. **exp-005**: The multi-round repair experiment is still being defined, but I'm working through what the best-case targets should be.

There's an unexplained jump somewhere between +14.7 and +20 percentage points that I need to investigate. Beyond that, I'm planning a series of ablations: deep-diving into an unknown sample, comparing selection versus repair strategies on the GT≠True subset, running an error taxonomy breakdown, checking statistical significance, testing Qwen3-8B, evaluating GPQA Diamond, validating self-consistency against majority voting with token cost constraints, and cross-validating the taxonomy across models using Cohen's kappa. Now I'm organizing all these experiments into a structured YAML output with detailed rationales for each.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b033866f-b64f-4400-ab19-4521ba54f5ee",
  "isSidechain": false,
  "requestId": "req_011Cb3wxbFqw42Mmtk7Qjxeo",
  "type": "assistant",
  "uuid": "8a163692-60e8-4fb7-9dc6-12fa7061dcdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "5247ca7a-726d-48b5-ab06-75a8e4729652",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015eX11QC85BhRQHYSod6bMo",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13226,
      "cache_read_input_tokens": 11841,
      "output_tokens": 15208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 15208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13226
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

_source line 9 · 2026-05-15T07:24:12.344Z_

```yaml
tier: best
narrative_guidance: >
  原始 framing 完全成立。Cross-representation disagreement 是一个比 within-representation self-consistency
  更高效的诊断信号：用 1/3 的 token 成本获得相当或更高的诊断精度。三条 claim 无需调整——C1/C2 跨三个基准和两个模型稳定，
  C3 的 GT-label-dependent 效应在新基准复现，taxonomy 跨模型一致。论文双轨叙事（分析为主 + 方法为辅）自然成立。
  Selection ablation 展示 repair 在可诊断子集上的增量价值。Repair 的 GT=True overcorrection 作为 discovered
  boundary 是加分项而非弱点。

imagined_experiments:
  - name: "FOLIO 完整分析（MVP 数据深度挖掘）"
    plan_id: "exp-001"
    description: >
      基于 204 样本 MVP 数据的统计检验、错误分类、子集分层分析、不对称性 breakdown、
      失败相关性定量分析和 cost-effectiveness 分析。纯分析，无新实验运行。
    expected_results:
      C1_disagree_rate: "42.16% [35.3%, 49.0%]"
      C2_diagnostic_rate: "87.21% [81.3%, 94.7%]"
      C3_error_types: 4
      C4_targeted_delta_aggregate: "+4.65pp (Fisher p=0.626, n.s.)"
      C4_GT_True: "-13.6pp"
      C4_GT_False: "+11.6pp"
      C4_GT_Unknown: "+14.7pp"
      C5_committed_accuracy: "94.6% (35/37)"
      C5_coverage: "53.0% (35/66)"
      asymmetry_ratio: "5.6:1 (FOL=56, Code=10, Both=10)"
      phi_coefficient: 0.189
      phi_p_value: 0.007
      complementary_error_rate: "75% (75/100)"
      cost_multiplier_vs_code_only: "5.76x tokens"
      accuracy_gain_over_code_only: "+21.6pp"
      dominant_error: "logic_error 25.5%"
    result_rationale: >
      这是已有 MVP 数据的深度挖掘，数值已固定。在 best 档位下，关键价值在于：(1) Bootstrap CI
      对 C1/C2 给出了紧致的区间，C2 下界 81.3% 远超 75% 阈值，为高精度诊断信号提供统计支撑；
      (2) phi=0.189 (p=0.007) 表明 FOL/Code 失败相关性低但统计显著——恰好落在"足够独立以产生互补信号，
      又不完全独立"的理想区间；(3) 75% 单侧失败率直接支撑 cross-representation 的互补性叙事；
      (4) GT-stratified C4 揭示三路分裂是 Claim 3 的核心发现，aggregate 非显著反而强化了
      "必须分层报告"的方法论贡献。cost_multiplier 5.76x 看似高，但对比 k=5 self-consistency
      的 5x 成本，CRD 以相近成本获得更丰富的诊断信息（错误类型 + 定位），而非仅 majority vote。
    tables:
      - name: "Table 1: FOLIO C1-C5 Metrics with Bootstrap 95% CI"
        columns: ["Metric", "Point Estimate", "95% CI", "MVP Gate"]
        rows:
          - ["C1 (Disagree Rate)", "42.16%", "[35.3%, 49.0%]", "PASS (≥15%)"]
          - ["C2 (Diagnostic Rate)", "87.21%", "[81.3%, 94.7%]", "PASS (≥75%)"]
          - ["C3 (Error Types)", "4 types", "—", "PASS (≥3)"]
          - ["C4 (Repair Delta)", "+4.65pp", "[-8.8%, +18.1%]", "FAIL (CI includes 0)"]
          - ["C5 (Localization)", "53.0%", "[41.0%, 65.1%]", "FAIL (<70%)"]
      - name: "Table 2: GT-Label-Stratified Repair Effect"
        columns: ["GT Label", "n", "Targeted Acc", "Blind Acc", "Delta", "Interpretation"]
        rows:
          - ["True", 72, "63.6%", "77.3%", "-13.6pp", "Overcorrection"]
          - ["False", 63, "76.7%", "70.0%", "+6.7pp", "Modest help"]
          - ["Unknown", 69, "67.7%", "52.9%", "+14.7pp", "Diagnosis helps"]
      - name: "Table 3: Error Taxonomy Distribution"
        columns: ["Error Type", "Count", "Proportion"]
        rows:
          - ["logic_error", 52, "25.5%"]
          - ["negation_error", 22, "10.8%"]
          - ["exec_crash", 11, "5.4%"]
          - ["quantifier_error", 4, "2.0%"]
    figures_description:
      - "Fig 1: Confusion matrix heatmap — FOL correct/wrong × Code correct/wrong，标注 5.6:1 不对称"
      - "Fig 2: GT-stratified repair delta bar chart，三色柱状图显示三路分裂效应"
      - "Fig 3: phi coefficient 按 GT label 分层的热图"
    analysis: >
      exp-001 作为 anchor 实验，所有数值已确定。best 档位下的分析重点是将 C4 aggregate 非显著
      和 C5 低覆盖率重新 frame 为方法论发现而非失败：(1) aggregate 非显著正是因为 GT-label-dependent
      效应相互抵消，分层报告是正确的分析粒度；(2) C5 coverage 53% 但 committed accuracy 94.6%
      是高精度/低召回的 deliberate tradeoff，ambiguous 标签中 61% 来自 GT=Unknown 驱动——
      这些样本恰好是 repair delta 最大的子集，说明即使定位不确定，disagreement pattern 本身
      就有修复价值。

  - name: "跨模型消融（FOLIO）"
    plan_id: "exp-002"
    description: >
      三组条件：(a) Qwen3-32B within-model (MVP baseline), (b) DeepSeek V4 Pro within-model,
      (c) DeepSeek FOL + Qwen Code cross-model。区分分歧来源。
    expected_results:
      deepseek_within_C1: "38.7%"
      deepseek_within_C2: "83.5%"
      deepseek_within_C2_CI: "[74.2%, 91.8%]"
      deepseek_within_asymmetry: "4.2:1 (FOL-favored)"
      deepseek_within_C4_GT_Unknown: "+12.1pp"
      deepseek_within_C4_GT_True: "-10.3pp"
      deepseek_within_C4_GT_False: "+8.4pp"
      cross_model_C1: "47.5%"
      cross_model_C2: "80.9%"
      cross_model_asymmetry: "3.8:1 (FOL-favored)"
      C2_delta_vs_MVP: "-3.7pp (within ±8pp gate)"
      asymmetry_direction: "consistent (FOL-favored in all 3 conditions)"
    result_rationale: >
      在 best 档位下，DeepSeek within-model C2 落在 MVP ±8pp 内（83.5% vs 87.2%，delta=-3.7pp），
      证明诊断精度不是 Qwen3-32B 的特异性质，而是 cross-representation disagreement 的结构性属性。
      DeepSeek C1 略低（38.7% vs 42.2%）合理——DeepSeek 作为更强模型，两条表征路径各自精度更高，
      分歧率自然略低，但 C2 保持在 80%+ 说明分歧样本仍然高度诊断性。不对称方向一致（FOL-favored）
      是关键：这不是模型偶然，而是 FOL+Z3 的形式验证保证系统性地比 Python 执行更可靠。
      Cross-model 条件 C1 更高（47.5%）因为两个不同模型的 formalization bias 不同，
      增加了分歧概率，但 C2 略降（80.9%）因为部分分歧来自模型差异而非 formalization 错误。
      这个分离正好支撑论文的核心论点：within-model cross-representation disagreement
      更纯粹地反映 formalization 错误，cross-model 混入了 capability 噪声。
    tables:
      - name: "Table 4: Cross-Model Ablation Results on FOLIO (n=204)"
        columns: ["Condition", "C1", "C2", "C2 95% CI", "Asymmetry", "C4 (Unknown)", "C4 (True)"]
        rows:
          - ["Qwen3-32B within (MVP)", "42.2%", "87.2%", "[81.3%, 94.7%]", "5.6:1 FOL", "+14.7pp", "-13.6pp"]
          - ["DeepSeek within", "38.7%", "83.5%", "[74.2%, 91.8%]", "4.2:1 FOL", "+12.1pp", "-10.3pp"]
          - ["DeepSeek×Qwen cross", "47.5%", "80.9%", "[71.8%, 89.1%]", "3.8:1 FOL", "+9.8pp", "-8.7pp"]
    figures_description:
      - "Fig 4: 三条件 C1/C2 对比柱状图，带 error bars"
      - "Fig 5: 不对称比例的 stacked bar，三条件均 FOL-favored"
    analysis: >
      三组数据形成清晰的叙事梯度：within-model(同模型) > cross-model(跨模型) 在 C2 上，
      说明 within-model 的诊断信号更纯净。DeepSeek GT-stratified 效应方向完全一致
      （Unknown 正, True 负, False 正），证明 Claim 3 的 GT-label-dependent 效应
      是表征结构属性而非模型特异。C2 delta -3.7pp 在 ±8pp gate 内——这是 best 档的
      sweet spot，既证明泛化，又不大到暗示 MVP 是 outlier。

  - name: "ProofWriter / LogiQA 扩展"
    plan_id: "exp-003"
    description: >
      第二逻辑推理基准。先 pilot 20-30 样本验证 disagree_rate ≥ 10%，
      通过则全量跑 ProofWriter；失败则切换 LogiQA。
    expected_results:
      dataset_used: "LogiQA"
      pilot_proofwriter_disagree_rate: "6.7% (2/30) — pilot FAIL"
      pilot_switch_reason: "ProofWriter 合成数据过于规则，FOL/Code 均高精度 (>93%)，分歧率不足"
      logiqA_n: 200
      logiqA_C1: "34.0%"
      logiqA_C2: "81.5%"
      logiqA_C2_CI: "[73.8%, 88.2%]"
      logiqA_C3_error_types: 4
      logiqA_asymmetry: "3.2:1 (FOL-favored)"
      logiqA_C4_GT_stratified_positive_subset: "+11.3pp"
      logiqA_C4_GT_stratified_negative_subset: "-9.8pp"
      logiqA_C5_committed: "91.2%"
      logiqA_C5_coverage: "48.5%"
    result_rationale: >
      在 best 档位下，ProofWriter pilot 失败是预期且合理的——合成数据的逻辑结构简单规则，
      两条表征路径都能高精度处理，分歧率仅 6.7%。这不是坏消息：切换到 LogiQA（自然语言逻辑，
      4 选 1）反而更好，因为 NL 歧义性更高，更能展示 CRD 在真实场景中的价值。LogiQA C1=34%
      略低于 FOLIO（42%）合理——选择题格式约束了输出空间，减少了 formalization 分歧；但 C2=81.5%
      仍然高（≥75% gate），证明分歧样本跨基准稳定诊断。不对称比仍 FOL-favored（3.2:1）但比
      FOLIO 的 5.6:1 低——LogiQA 的命题逻辑复杂度低于 FOLIO 的一阶逻辑，FOL 路径的优势
      相对缩小。GT-stratified 效应方向复现（正/负分裂），证明 Claim 3 跨基准泛化。
      C5 committed 91.2% 保持在 90%+ 高精度区间。
    tables:
      - name: "Table 5: LogiQA Results (n=200, Qwen3-32B)"
        columns: ["Metric", "LogiQA", "FOLIO (ref)", "Delta"]
        rows:
          - ["C1 (Disagree Rate)", "34.0%", "42.2%", "-8.2pp"]
          - ["C2 (Diagnostic Rate)", "81.5%", "87.2%", "-5.7pp"]
          - ["C3 (Error Types)", "4", "4", "—"]
          - ["C5 Committed Acc", "91.2%", "94.6%", "-3.4pp"]
          - ["Asymmetry (FOL:Code)", "3.2:1", "5.6:1", "narrower"]
      - name: "Table 5b: ProofWriter Pilot Results (n=30)"
        columns: ["Metric", "Value", "Gate", "Decision"]
        rows:
          - ["Disagree Rate", "6.7%", "≥10%", "FAIL → switch to LogiQA"]
          - ["FOL Accuracy", "93.3%", "—", "—"]
          - ["Code Accuracy", "90.0%", "—", "—"]
    figures_description:
      - "Fig 6: FOLIO vs LogiQA C1/C2 并排对比，带 CI error bars"
      - "Fig 7: LogiQA GT-stratified repair delta 复现 FOLIO 三路分裂模式"
    analysis: >
      LogiQA 作为第二基准完美补充 FOLIO：不同数据源（中国公务员考试 vs 专家标注 FOL），
      不同任务格式（4 选 1 vs 3 分类），C2 仍在 [75%, 92%] range 内。ProofWriter pilot
      失败在论文中可以作为 1 段讨论："合成数据过于规则，分歧信号需要自然语言的 formalization
      挑战"——这反而强化了 CRD 适用场景的 characterization。

  - name: "MATH Level 5 双可执行表征扩展"
    plan_id: "exp-004"
    description: >
      MATH Level 5 使用 SymPy 符号推理 vs Python 数值计算两条可执行路径，
      保持 cross-executable-representation 框架一致性。
    expected_results:
      n: 200
      math_C1: "28.5%"
      math_C2: "76.0%"
      math_C2_CI: "[66.1%, 85.2%]"
      math_C3_error_types: 3
      math_asymmetry: "1.8:1 (Code-favored)"
      math_asymmetry_direction: "反转——Python 数值计算在 MATH 上优于 SymPy 符号推理"
      math_C4_GT_correct_delta: "+3.2pp"
      math_C4_GT_wrong_delta: "+7.8pp"
      math_C5_committed: "88.5%"
      math_C5_coverage: "55.0%"
      sympy_crash_rate: "12.5%"
      python_crash_rate: "4.0%"
    result_rationale: >
      在 best 档位下，MATH C1=28.5% 满足 ≥15% gate。C1 低于 FOLIO（42%）合理——
      数学问题有唯一正确答案，两条计算路径比逻辑推理的 formalization 更容易达成一致。
      C2=76% 刚好在 [70%, 85%] 范围内——数学分歧中更多是计算错误而非 formalization 错误，
      部分分歧来自数值精度问题（如浮点近似 vs 精确符号解），诊断性略低但仍超 70% gate。
      关键发现：不对称方向反转（Code-favored 1.8:1），与 FOLIO 的 FOL-favored 5.6:1 相反。
      这是 best 档的 killer result——证明不对称性不是 FOL 固有优势，而是表征-任务匹配：
      在逻辑推理上 FOL+Z3 有形式验证优势，在数学计算上 Python 的灵活数值方法更鲁棒。
      SymPy crash rate 12.5% > Python 4% 因为 SymPy 对输入格式敏感（符号化简失败、
      方程无解析解等），而 Python 数值方法更容错。这个反转直接回应 R5（"不只是 FOL-as-verifier"）。
    tables:
      - name: "Table 6: MATH Level 5 Results (n=200, Qwen3-32B)"
        columns: ["Metric", "MATH", "FOLIO (ref)", "LogiQA (ref)"]
        rows:
          - ["C1 (Disagree Rate)", "28.5%", "42.2%", "34.0%"]
          - ["C2 (Diagnostic Rate)", "76.0%", "87.2%", "81.5%"]
          - ["C3 (Error Types)", "3", "4", "4"]
          - ["Asymmetry", "1.8:1 Code-fav", "5.6:1 FOL-fav", "3.2:1 FOL-fav"]
          - ["C5 Committed", "88.5%", "94.6%", "91.2%"]
      - name: "Table 7: Asymmetry Direction Across Domains"
        columns: ["Domain", "Representation A", "Representation B", "Favored", "Ratio"]
        rows:
          - ["Logic (FOLIO)", "FOL+Z3", "Python exec", "FOL", "5.6:1"]
          - ["Logic (LogiQA)", "FOL+Z3", "Python exec", "FOL", "3.2:1"]
          - ["Math (MATH)", "SymPy symbolic", "Python numerical", "Python", "1.8:1"]
    figures_description:
      - "Fig 8: 三基准 asymmetry direction 可视化——逻辑 vs 数学域的反转"
      - "Fig 9: MATH 错误类型分布（computation_error, symbolic_failure, exec_crash）"
    analysis: >
      MATH 的不对称反转是 best 档位的标志性结果。它将 paper 的 story 从 "FOL is better"
      升级为 "cross-representation disagreement reveals domain-specific representation
      strengths"——更深层的洞察，更广的适用性。C2=76% 虽然低于 FOLIO，但 CI 下界 66.1%
      接近 70% gate，在 best 档位下 point estimate 通过。C3=3 types（少了 quantifier_error，
      因为数学域没有量词问题），但新增 computation_error（截断/精度）类型。

  - name: "Repair 机制改进（多轮修复）"
    plan_id: "exp-005"
    description: >
      最多 3 轮 repair，加入错误类型特定修复策略，按 GT label 和 error_type 分层报告。
      目标：Unknown 子组 delta 从 +14.7pp 拉到 +20pp+。
    expected_results:
      repair_rounds_avg: 1.8
      GT_Unknown_delta_round1: "+14.7pp"
      GT_Unknown_delta_round3: "+22.1pp"
      GT_False_delta_round1: "+6.7pp"
      GT_False_delta_round3: "+10.4pp"
      GT_True_delta_round1: "-13.6pp"
      GT_True_delta_round3: "-11.2pp"
      C4_unknown_false_combined_delta: "+15.8pp"
      error_type_repair_success:
        logic_error: "68.3%"
        negation_error: "72.0%"
        exec_crash: "81.8%"
        quantifier_error: "50.0%"
      round2_additional_fixes: "8 samples"
      round3_additional_fixes: "3 samples"
    result_rationale: >
      在 best 档位下，多轮 repair 将 GT=Unknown delta 从 +14.7pp 拉到 +22.1pp（超过 +20pp gate）。
      机制：第一轮修复了大部分 Code overclaiming（Code 输出 True/False 但应为 Unknown），
      第二轮处理残余的 logic_error（FOL 形式化中的量词/否定遗漏导致第一轮修复方向偏移），
      第三轮边际收益递减（仅 3 个 additional fix）。GT=True overcorrection 从 -13.6pp
      改善到 -11.2pp——多轮 repair 的错误类型感知策略对 GT=True 的伤害略有缓解
      （negation_error 特定策略避免了盲目翻转），但仍然为负，证明 overcorrection boundary
      是结构性的而非策略不足。exec_crash 81.8% 修复率最高因为这类错误最容易诊断和修复
      （语法/运行时错误，重新生成即可）。quantifier_error 50% 最低因为量词错误需要
      深层理解全称/存在量词的语义。combined delta +15.8pp 落在 [8, 18] range 的偏高区域。
    tables:
      - name: "Table 8: Multi-Round Repair Results (FOLIO, n=204)"
        columns: ["GT Label", "n", "Round 1 Delta", "Round 3 Delta", "Improvement"]
        rows:
          - ["Unknown", 69, "+14.7pp", "+22.1pp", "+7.4pp"]
          - ["False", 63, "+6.7pp", "+10.4pp", "+3.7pp"]
          - ["True", 72, "-13.6pp", "-11.2pp", "+2.4pp (still negative)"]
      - name: "Table 9: Repair Success Rate by Error Type (Round 3)"
        columns: ["Error Type", "Attempted", "Fixed", "Success Rate"]
        rows:
          - ["logic_error", 41, 28, "68.3%"]
          - ["negation_error", 18, 13, "72.0%"]
          - ["exec_crash", 11, 9, "81.8%"]
          - ["quantifier_error", 4, 2, "50.0%"]
    figures_description:
      - "Fig 10: 多轮 repair 收益曲线（Round 1/2/3 delta 按 GT label）"
      - "Fig 11: 错误类型特定修复成功率 bar chart"
    analysis: >
      多轮 repair 的递减收益模式（Round 1: +14.7→+22.1, Round 2: +5.2, Round 3: +2.2）
      是 best 档位的理想结果——证明错误类型特定策略有增量价值，但不是无限的。
      GT=True 仍为负是论文的 honesty signal——不掩饰 boundary。错误类型分层报告
      为 exp-008（taxonomy ablation）提供了直接支撑。

  - name: "Unknown 样本深度分析 + correlated failure 定量"
    plan_id: "exp-006"
    description: >
      分析 GT=Unknown 驱动 C4 delta 的机制，FOL/Code 相关系数按 GT 分层，
      false agreement rate，specification vs formalization 错误分类。
    expected_results:
      code_overclaiming_rate_unknown: "78.3% (54/69)"
      code_overclaiming_mechanism: "Code 路径倾向输出 True/False 而非 Unknown，因为 Python 缺乏三值逻辑原生支持"
      fol_overclaiming_rate_unknown: "21.7% (15/69)"
      phi_by_GT:
        "True": 0.245
        "False": 0.162
        Unknown: 0.098
      false_agreement_rate: "12.3% (25/204)"
      false_agreement_breakdown: "GT=True 14/72 (19.4%), GT=False 7/63 (11.1%), GT=Unknown 4/69 (5.8%)"
      specification_error_rate: "8.3% (17/204)"
      formalization_specific_error_rate: "91.7% (187/204 non-spec-error)"
    result_rationale: >
      在 best 档位下，Code overclaiming 78.3% 的高比率清晰解释了 GT=Unknown 子集的
      repair delta 来源：Python 执行路径缺乏三值逻辑（True/False/Unknown）的原生表达能力，
      倾向将 insufficient-information 情况强制映射为 True 或 False。当 CRD 诊断出分歧后，
      repair prompt 包含"FOL 路径返回 Unknown"的信息，帮助模型认识到证据不足，修正
      Code 的 overclaiming。phi 按 GT 分层显示 Unknown 相关性最低（0.098），意味着
      FOL/Code 在 Unknown 上最不相关——互补信号最强，这直接解释了为什么 repair delta 最大。
      False agreement rate 12.3% 相对低（Denisov-Blanch 2026 担忧的 correlated failure
      不严重），且 GT=Unknown 子集仅 5.8% false agreement——再次证明 Unknown 是 CRD 的
      最佳应用场景。specification error 仅 8.3% 说明绝大多数错误是 formalization-specific
      而非原始问题歧义导致，支撑 CRD 的诊断靶点合理性。
    tables:
      - name: "Table 10: Correlated Failure Analysis"
        columns: ["GT Label", "n", "phi", "False Agreement Rate", "Code Overclaiming"]
        rows:
          - ["True", 72, 0.245, "19.4%", "N/A"]
          - ["False", 63, 0.162, "11.1%", "N/A"]
          - ["Unknown", 69, 0.098, "5.8%", "78.3%"]
          - ["Overall", 204, 0.189, "12.3%", "—"]
    figures_description:
      - "Fig 12: Code overclaiming 机制图——Unknown→True/False 的映射路径"
      - "Fig 13: phi coefficient 按 GT label 分层 + false agreement rate 联合可视化"
    analysis: >
      此分析为 Claim 3 提供了因果机制：不是 repair 策略差异导致 GT-dependent 效应，
      而是 Code 表征的结构性局限（缺乏三值逻辑）× GT label 的交互作用。这使得
      GT=True overcorrection 也有了合理解释——当 GT=True 但 Code 错误输出 False/Unknown 时，
      诊断信号误导 repair 认为应该远离 True，导致 overcorrection。

  - name: "Selection vs Repair 消融"
    plan_id: "exp-007"
    description: >
      分歧检测+定位错误侧后，直接选正确侧 vs 诊断引导修复，按 error_type 分层报告。
    expected_results:
      blind_baseline_acc_GT_not_true: "61.4%"
      selection_acc_GT_not_true: "72.7%"
      repair_acc_GT_not_true: "76.2%"
      selection_vs_blind_delta: "+11.3pp"
      repair_vs_selection_delta: "+3.5pp"
      selection_by_error_type:
        logic_error: "70.7%"
        negation_error: "77.8%"
        exec_crash: "90.9%"
        quantifier_error: "50.0%"
      repair_by_error_type:
        logic_error: "75.6%"
        negation_error: "77.8%"
        exec_crash: "90.9%"
        quantifier_error: "75.0%"
      repair_advantage_concentrated_on: "logic_error (+4.9pp) 和 quantifier_error (+25pp)"
    result_rationale: >
      在 best 档位下，selection 已经大幅优于 blind baseline（+11.3pp，远超 +5pp gate），
      证明 CRD 诊断+定位的基本价值。repair 在 selection 之上再加 +3.5pp（刚超 +3pp gate），
      增量价值集中在 logic_error 和 quantifier_error——这两类错误需要修正 formalization
      而非简单选边，selection 无法解决因为两侧都可能部分正确（如 FOL 量词正确但谓词错误，
      Code 谓词正确但逻辑流错误）。negation_error 和 exec_crash 上 repair ≈ selection，
      因为这两类错误通常有明确的"一侧对一侧错"模式，选正确侧就足够了。
      这个分层结果支撑了论文的 nuanced claim：repair 不是全面优于 selection，
      而是在特定错误类型上有不可替代的价值——正是 taxonomy 驱动修复的意义。
      限制在 GT≠True 子集报告（n=132），因为 GT=True overcorrection 对 selection
      和 repair 都适用，不影响二者的相对对比。
    tables:
      - name: "Table 11: Selection vs Repair on GT≠True Subset (n=132)"
        columns: ["Method", "Overall Acc", "logic_error", "negation_error", "exec_crash", "quantifier_error"]
        rows:
          - ["Blind Baseline", "61.4%", "56.1%", "66.7%", "72.7%", "25.0%"]
          - ["Selection", "72.7%", "70.7%", "77.8%", "90.9%", "50.0%"]
          - ["Repair (Round 3)", "76.2%", "75.6%", "77.8%", "90.9%", "75.0%"]
    figures_description:
      - "Fig 14: 三方法对比 grouped bar chart，按 error_type 分层"
      - "Fig 15: Repair 增量价值热图（repair - selection delta 按 error type）"
    analysis: >
      Selection vs repair 的分层结果是 exp-007 的核心贡献：证明 taxonomy 不仅是分析工具，
      还有规定性价值（prescriptive value）——知道错误类型决定了应该 select 还是 repair。
      这直接回应 R3 并为 exp-008 铺路。selection_vs_blind +11.3pp 是强结果，
      证明即使不 repair，CRD 诊断+定位已经有实用价值。

  - name: "Error Taxonomy 消融"
    plan_id: "exp-008"
    description: >
      按错误类型分派修复策略 vs 固定策略（统一重生成），验证 taxonomy 的规定性价值。
    expected_results:
      taxonomy_guided_acc: "76.2%"
      fixed_strategy_acc: "71.2%"
      taxonomy_delta: "+5.0pp"
      taxonomy_advantage_by_type:
        logic_error: "+6.2pp"
        negation_error: "+2.3pp"
        exec_crash: "+0.0pp"
        quantifier_error: "+18.0pp"
      mcnemar_p: 0.042
    result_rationale: >
      在 best 档位下，taxonomy-guided 策略整体优于 fixed strategy +5.0pp（McNemar p=0.042，
      显著）。增量主要来自 logic_error（最大类，+6.2pp——targeted prompt 包含"检查谓词定义
      和推理链"vs 盲目重生成）和 quantifier_error（最小类但增幅最大 +18.0pp——targeted prompt
      显式提示"检查全称/存在量词的作用域"，盲目重生成几乎无法修复这类细微错误）。
      exec_crash 无差异因为重生成本身就是最优策略（崩溃了就重新生成）。negation_error
      增量小因为否定翻转相对简单，固定策略也能偶然修复。McNemar p=0.042 刚好显著，
      反映样本量有限但效应真实。
    tables:
      - name: "Table 12: Taxonomy-Guided vs Fixed Strategy Repair"
        columns: ["Error Type", "n", "Taxonomy-Guided", "Fixed (regen)", "Delta"]
        rows:
          - ["logic_error", 41, "75.6%", "69.4%", "+6.2pp"]
          - ["negation_error", 18, "77.8%", "75.5%", "+2.3pp"]
          - ["exec_crash", 11, "90.9%", "90.9%", "+0.0pp"]
          - ["quantifier_error", 4, "75.0%", "57.0%", "+18.0pp"]
          - ["Overall", 74, "76.2%", "71.2%", "+5.0pp (p=0.042)"]
    figures_description:
      - "Fig 16: Taxonomy-guided vs fixed strategy 按 error type 对比"
    analysis: >
      Taxonomy ablation 证明 error classification 不只是 analysis contribution——
      它有 prescriptive value。这将 Claim 2 从纯分析升级为方法贡献，
      增加论文的实用性维度。quantifier_error 的 +18pp 虽然 n 太小（4 samples）不能
      单独做统计检验，但方向明确。

  - name: "统计显著性全面检验"
    plan_id: "exp-009"
    description: >
      对所有 benchmark 的 C1-C5 指标做 Bootstrap 95% CI + Fisher exact / McNemar test。
    expected_results:
      FOLIO_C2_CI: "[81.3%, 94.7%]"
      LogiQA_C2_CI: "[73.8%, 88.2%]"
      MATH_C2_CI: "[66.1%, 85.2%]"
      cross_benchmark_C2_min_lower: "66.1%"
      FOLIO_C4_unknown_fisher_p: 0.038
      FOLIO_C4_true_fisher_p: 0.021
      LogiQA_C4_positive_subset_fisher_p: 0.045
      CRD_vs_SC5_mcnemar_p: 0.031
      all_primary_claims_significant: true
      aggregate_C4_significant: false
    result_rationale: >
      在 best 档位下，所有主要 claim 的分层指标都达到统计显著：FOLIO GT=Unknown
      C4 delta Fisher p=0.038（n=69，+14.7pp→+22.1pp 多轮后更强），GT=True overcorrection
      p=0.021（负方向也显著，strengthens boundary characterization）。LogiQA 的正子集
      p=0.045 复现效应。CRD vs SC5 McNemar p=0.031 证明诊断精度差异显著。
      关键：aggregate C4 仍然不显著——这在 best 档位下是 feature not bug，
      因为分层报告是我们的 methodological contribution。CI 紧致度随样本量提高
      （FOLIO n=204 > LogiQA n=200 > MATH n=200），MATH C2 下界 66.1% 最低
      但 point estimate 76% 仍超 70% gate。
    tables:
      - name: "Table 13: Statistical Significance Summary Across Benchmarks"
        columns: ["Test", "Benchmark", "Metric", "Statistic", "p-value", "Significant?"]
        rows:
          - ["Fisher", "FOLIO", "C4 GT=Unknown", "+22.1pp", "0.038", "Yes"]
          - ["Fisher", "FOLIO", "C4 GT=True", "-11.2pp", "0.021", "Yes"]
          - ["Fisher", "LogiQA", "C4 positive subset", "+11.3pp", "0.045", "Yes"]
          - ["McNemar", "FOLIO", "CRD vs SC5 precision", "+7.2pp", "0.031", "Yes"]
          - ["Fisher", "FOLIO", "C4 aggregate", "+4.65pp", "0.626", "No"]
          - ["Bootstrap", "All", "C2 range", "[66.1%, 94.7%]", "—", "—"]
    figures_description:
      - "Fig 17: 跨基准 C2 Bootstrap CI 的 forest plot"
    analysis: >
      统计检验结果在 best 档位下完美支撑叙事：分层指标显著而 aggregate 不显著，
      证明分层分析的必要性。Forest plot 显示三基准 C2 CI 重叠但中心递减
      （FOLIO > LogiQA > MATH），反映任务复杂度梯度。

  - name: "Self-Consistency Baseline 对比"
    plan_id: "exp-012"
    description: >
      FOLIO + LogiQA + MATH 上对比 k=5 FOL-only majority vote, k=5 Code-only majority vote,
      vs single-pass CRD。隔离 cross-representation 信号 vs 单表征 sampling diversity。
    expected_results:
      FOLIO:
        SC5_FOL_precision: "79.3%"
        SC5_Code_precision: "72.1%"
        CRD_precision: "87.2%"
        CRD_vs_SC5_FOL_delta: "+7.9pp"
        SC5_FOL_cost_tokens: "5x baseline"
        SC5_Code_cost_tokens: "5x baseline"
        CRD_cost_tokens: "2x baseline"
        CRD_vs_SC5_cost_ratio: "0.40"
      LogiQA:
        SC5_FOL_precision: "75.8%"
        SC5_Code_precision: "69.4%"
        CRD_precision: "81.5%"
        CRD_vs_SC5_FOL_delta: "+5.7pp"
      MATH:
        SC5_SymPy_precision: "71.2%"
        SC5_Python_precision: "74.8%"
        CRD_precision: "76.0%"
        CRD_vs_SC5_best_delta: "+1.2pp"
      overall_CRD_vs_SC5_precision_delta: "+4.9pp (avg across benchmarks)"
      overall_CRD_vs_SC5_cost_ratio: 0.40
    result_rationale: >
      在 best 档位下，CRD 在所有三个基准上诊断精度均优于 k=5 单表征 majority vote，
      且 token 成本仅为 40%（2 次生成 vs 5 次生成）。机制：k=5 同表征 sampling 捕获的是
      generation variance（同一 prompt 的随机性），而 CRD 捕获的是 paradigm-level difference
      （形式逻辑 vs 命令式代码的系统性差异）。前者在高温度下有效但容易被 mode collapse 削弱
      （LLM 倾向于收敛到同一错误模式），后者因为表征范式根本不同而产生更互补的错误信号。
      FOLIO delta 最大（+7.9pp）因为 FOL 和 Python 的范式差异最大；MATH delta 最小（+1.2pp）
      因为 SymPy 和 Python numerical 都是 Python 生态，范式差异较小。MATH 上 SC5_Python
      甚至略优于 SC5_SymPy（74.8% vs 71.2%），与 exp-004 的不对称反转一致。
      CRD cost ratio 0.40 落在 [0.30, 0.45] range——2 次生成 vs 5 次生成 = 0.40，
      考虑 CRD 额外的 diagnosis prompt 开销后正好 40%。
    tables:
      - name: "Table 14: CRD vs Self-Consistency (k=5) Across Benchmarks"
        columns: ["Benchmark", "SC5-FOL Prec", "SC5-Code Prec", "CRD Prec", "CRD-SC5 Δ", "Cost Ratio"]
        rows:
          - ["FOLIO", "79.3%", "72.1%", "87.2%", "+7.9pp", "0.40"]
          - ["LogiQA", "75.8%", "69.4%", "81.5%", "+5.7pp", "0.40"]
          - ["MATH", "71.2%", "74.8%", "76.0%", "+1.2pp", "0.40"]
          - ["Average", "75.4%", "72.1%", "81.6%", "+4.9pp", "0.40"]
    figures_description:
      - "Fig 18: CRD vs SC5 precision-cost Pareto 图——CRD 在 Pareto front 上"
      - "Fig 19: 按基准的 CRD vs SC5 对比 grouped bar chart"
    analysis: >
      exp-012 是回应 R8 的核心实验。best 档位下 CRD Pareto-dominates SC5（更高精度+更低成本），
      headline 变为"用 40% 的 token 成本获得平均 +4.9pp 的诊断精度提升"。
      MATH 上 delta 仅 +1.2pp 是可接受的——因为 SymPy/Python 范式差异较小，
      但仍为正且 cost advantage 不变。论文可以讨论 "paradigm distance" 作为
      CRD 效果的调节变量——范式差异越大，CRD 相对于 SC5 的优势越大。

  - name: "Error Taxonomy 交叉验证"
    plan_id: "exp-013"
    description: >
      DeepSeek V4 Pro 对 FOLIO 分歧样本做错误分类，与 Qwen3-32B 分类对比，
      计算 Cohen's κ。验证 taxonomy 跨模型稳定性。
    expected_results:
      n_classified: 75
      cohens_kappa: 0.67
      kappa_CI: "[0.54, 0.80]"
      agreement_by_type:
        logic_error: "78.8%"
        negation_error: "72.7%"
        exec_crash: "90.9%"
        quantifier_error: "50.0%"
      deepseek_type_distribution:
        logic_error: "28.0%"
        negation_error: "12.0%"
        exec_crash: "6.7%"
        quantifier_error: "1.3%"
        unclassified: "4.0%"
      distribution_stability: "rank order preserved (logic > negation > crash > quantifier)"
    result_rationale: >
      在 best 档位下，Cohen's κ=0.67 落在 [0.60, 0.80] range，达到 "substantial agreement"
      标准。κ 不更高的原因合理：两个模型对 logic_error vs negation_error 的边界划分有
      模糊区域（一些否定相关的逻辑错误可以归入任一类别），这是分类本身的固有模糊性而非
      taxonomy 设计缺陷。exec_crash 一致性最高（90.9%）因为执行崩溃是客观可验证的。
      quantifier_error 一致性最低（50%）因为 n 太小（仅 4 样本）且量词错误判断需要
      深层语义理解。关键发现：两个模型的错误类型分布 rank order 完全一致
      （logic > negation > crash > quantifier），说明 taxonomy 反映的是错误结构而非
      模型偏好。DeepSeek 的 logic_error 比例略高（28% vs 25.5%）、unclassified 略低
      （4% vs 0%），因为 DeepSeek 更倾向给出明确分类而非其他 catch-all。
    tables:
      - name: "Table 15: Cross-Model Taxonomy Validation (n=75 diagnostic samples)"
        columns: ["Error Type", "Qwen3-32B %", "DeepSeek %", "Pairwise Agreement", "κ contribution"]
        rows:
          - ["logic_error", "25.5%", "28.0%", "78.8%", "0.71"]
          - ["negation_error", "10.8%", "12.0%", "72.7%", "0.62"]
          - ["exec_crash", "5.4%", "6.7%", "90.9%", "0.88"]
          - ["quantifier_error", "2.0%", "1.3%", "50.0%", "0.45"]
          - ["Overall κ", "—", "—", "—", "0.67"]
    figures_description:
      - "Fig 20: 4×4 confusion matrix heatmap (Qwen classification vs DeepSeek classification)"
      - "Fig 21: 两个模型的错误类型分布 side-by-side bar chart"
    analysis: >
      κ=0.67 回应 R9 的 taxonomy validation 要求。substantial agreement 证明
      taxonomy 不是单模型的 artifact——不同 LLM 从同一组分歧样本中识别出一致的错误模式。
      rank order 稳定性是更强的信号：即使个别样本分类不同，宏观分布结构跨模型复现，
      说明四类错误反映了 formalization 的真实失败模式。

  - name: "Qwen3-8B 消融"
    plan_id: "exp-010"
    description: >
      低能力模型上的诊断率和分歧率变化。P2 优先级。
    expected_results:
      n: 204
      C1_disagree_rate: "55.4%"
      C2_diagnostic_rate: "74.5%"
      asymmetry: "2.8:1 (FOL-favored, compressed)"
      fol_accuracy: "58.3%"
      code_accuracy: "47.1%"
      C4_aggregate: "+2.1pp"
    result_rationale: >
      在 best 档位下，8B 模型 C1 上升到 55.4%（更弱模型→更多 formalization 错误→更多分歧），
      但 C2 降至 74.5%（更多分歧来自"两侧都错"的 correlated failure，诊断性下降）。
      这个 C1↑C2↓ 的 tradeoff 是 model-capability 对 CRD 有效性的重要 characterization：
      存在一个能力下限，低于此 CRD 的诊断价值被 correlated failure 侵蚀。
      不对称比压缩到 2.8:1 因为 8B 的 FOL 能力下降更快（形式逻辑对模型能力更敏感）。
      作为 P2 实验，这提供了有价值的 scaling 分析但不影响核心 claim。
    tables:
      - name: "Table 16: Model Scale Ablation on FOLIO"
        columns: ["Model", "C1", "C2", "Asymmetry", "FOL Acc", "Code Acc"]
        rows:
          - ["Qwen3-32B", "42.2%", "87.2%", "5.6:1", "78.4%", "59.8%"]
          - ["Qwen3-8B", "55.4%", "74.5%", "2.8:1", "58.3%", "47.1%"]
          - ["DeepSeek V4 Pro", "38.7%", "83.5%", "4.2:1", "81.2%", "64.7%"]
    figures_description:
      - "Fig 22: Model capability vs C1/C2 scatter plot (三模型)"
    analysis: >
      三个模型形成 capability 梯度（8B < 32B < DeepSeek Pro），C2 单调递增，
      C1 单调递减——完美的 scaling story。论文 1 段 discussion 即可，不需要更多。

  - name: "GPQA Diamond 扩展"
    plan_id: "exp-011"
    description: >
      科学知识推理，SymPy/Python 双可执行表征。P2 优先级。
    expected_results:
      n: 150
      C1_disagree_rate: "22.0%"
      C2_diagnostic_rate: "72.7%"
      asymmetry: "1.4:1 (slight Python-favored)"
      note: "C2 略低于 70% gate——科学推理中 domain knowledge 错误占比高，CRD 对 knowledge gap 诊断力有限"
    result_rationale: >
      在 best 档位下，GPQA C1=22% 较低（科学推理需要 domain knowledge 而非纯 formalization，
      两条路径的差异更多来自知识错误而非表征差异），C2=72.7% 在 70% gate 边缘。
      这是 CRD 适用边界的有价值 characterization：cross-representation disagreement
      对 formalization errors 诊断力强，对 domain knowledge errors 诊断力弱。
      作为 P2 可选实验，如果时间不够可以省略，核心三基准已足够。
    tables:
      - name: "Table 17: Cross-Domain CRD Effectiveness"
        columns: ["Domain", "Benchmark", "C1", "C2", "Primary Error Source"]
        rows:
          - ["Logic", "FOLIO", "42.2%", "87.2%", "Formalization"]
          - ["Logic", "LogiQA", "34.0%", "81.5%", "Formalization"]
          - ["Math", "MATH L5", "28.5%", "76.0%", "Computation"]
          - ["Science", "GPQA", "22.0%", "72.7%", "Knowledge gap"]
    figures_description:
      - "Fig 23: Domain × C2 effectiveness 趋势图——formalization-heavy 域 CRD 最有效"
    analysis: >
      四基准形成清晰的域梯度：纯逻辑 > 数学 > 科学，C2 随 formalization 占比下降。
      这是 best 档位的 bonus result——不是每个域都好用恰恰证明我们理解了 CRD 的机制和边界。
      但 GPQA 作为 P2 实验，若时间不足可省略，不影响核心结论。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a163692-60e8-4fb7-9dc6-12fa7061dcdc",
  "isSidechain": false,
  "requestId": "req_011Cb3wxbFqw42Mmtk7Qjxeo",
  "type": "assistant",
  "uuid": "490762c6-ca36-4e74-a6cb-01d1eab37578",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "5247ca7a-726d-48b5-ab06-75a8e4729652",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015eX11QC85BhRQHYSod6bMo",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13226,
      "cache_read_input_tokens": 11841,
      "output_tokens": 15208,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13226,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 15208,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13226,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13226
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：CRD 信号在精度和成本上明确优于 self-consistency；跨基准/跨模型泛化成立；taxonomy 可复现 → EMNLP main weak accept 核心假设：['exp-012: CRD 诊断精度 ≥ k=5 单表征 majority vote，且 token 成本 ≤ 40%', 'e…",
  "leafUuid": "490762c6-ca36-4e74-a6cb-01d1eab37578",
  "sessionId": "5247ca7a-726d-48b5-ab06-75a8e4729652"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-representation disagreement diagnostic signal validation",
  "sessionId": "5247ca7a-726d-48b5-ab06-75a8e4729652"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：CRD 信号在精度和成本上明确优于 self-consistency；跨基准/跨模型泛化成立；taxonomy 可复现 → EMNLP main weak accept 核心假设：['exp-012: CRD 诊断精度 ≥ k=5 单表征 majority vote，且 token 成本 ≤ 40%', 'e…",
  "leafUuid": "490762c6-ca36-4e74-a6cb-01d1eab37578",
  "sessionId": "5247ca7a-726d-48b5-ab06-75a8e4729652"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-representation disagreement diagnostic signal validation",
  "sessionId": "5247ca7a-726d-48b5-ab06-75a8e4729652"
}
```

---
