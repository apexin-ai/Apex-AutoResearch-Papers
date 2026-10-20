# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：诊断信号在 FOLIO 外不稳健——disagree rate 过低或 precision 大幅下降，repair 无正向效果，核心 framing 

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/ecc5382a-3f63-45a1-993b-0dee29c58083.jsonl`
- **Structured JSON:** [`d0c17de280344d31d6a7.json`](../../sessions/d0/d0c17de280344d31d6a7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T06:14:27.831Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T06:14:27.831Z",
  "sessionId": "ecc5382a-3f63-45a1-993b-0dee29c58083",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：诊断信号在 FOLIO 外不稳健——disagree rate 过低或 precision 大幅下降，repair 无正向效果，核心 framing 需重构\n核心假设：['ProofWriter/MATH 上 C1 disagree rate <20% 或 C2 diagnostic precision <65%，信号不具跨域一致性', 'exp-005 repair 改进未能突破，C4 delta ≤3pp (All-mode)，Excl-Unknown 为负', 'MATH 域双表征分歧模式与逻辑域本质不同，不支持统一框架叙事', 'exp-002 跨模型消融未有效降低 correlated failures', '统计显著性在新 benchmark 上不成立 (p>0.05 或 CI 跨零)', '仅 FOLIO 单 benchmark 数据可靠']\n关键指标范围：{'C1_disagree_rate_cross_bench': [0.1, 0.25], 'C2_diagnostic_precision_cross_bench': [0.55, 0.7], 'C4_targeted_vs_blind_delta_pp_all_mode': [-2.0, 3.0], 'C4_targeted_vs_blind_delta_pp_excl_unknown': [-4.0, 0.0], 'C5_localization_accuracy_cross_bench': [0.6, 0.75], 'cross_model_false_agreement_reduction_pp': [-1.0, 2.0], 'MATH_fol_code_error_ratio': [5.0, 9.0], 'benchmarks_with_5of5_pass': [0, 1]}\n叙事方向：放弃 'general cross-representation diagnosis framework' 的普适性叙事。Reframe 为 domain-specific 深度研究：'When and Why Cross-Representation Disagreement Works: A Case Study in Formal Logic Reasoning'。核心 angle 转向：(1) 深度刻画 FOL-Code 分歧在逻辑推理中的独特有效性及其认知/结构原因（为什么 FOL 几乎总对而 Code 几乎总错），(2) 系统性分析跨域失败的原因（correlated failures、specification-level errors 的普遍性），(3) 提出 cross-representation diagnosis 的 applicability conditions。这个 reframe 仍然是 EMNLP Main 级别——深度 empirical analysis + negative results + boundary conditions 的组合在 EMNLP 有先例。但需要 FOLIO 上的分析足够深（补充 exp-006/007/008 全部完成），用深度补广度。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: cross_representation_disagreement_diagno\nfocus: C4 repair improvement is the main weakness (0.2pp margin). Key questions: (1) Is the dual-track framing (systematic analysis + lightweight repair) strong enough for EMNLP Main? (2) Does the boundary characterization (Claim 3) compensate for weak repair results? (3) Is 3 benchmarks (FOLIO + ProofWriter + MATH) sufficient or do we need more? (4) The 9:1 FOL:Code asymmetry — strength or weakness for the story?\n\n## paper_framing.md\n\n# Paper Framing — cross_representation_disagreement_diagno\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026 (10 days)\n- Secondary: AAAI 2027 (abstract July 25, full August 1) — extended version with full benchmark coverage\n\n## Core Insight\nCross-representation disagreement (FOL/Z3 vs Python Code) produced by the same LLM for the same reasoning problem is an underexploited diagnostic signal that detects formalization errors, enables error localization and classification, and guides targeted repair — going beyond existing approaches that only filter or verify within a single representation.\n\n## Core Claims (3 条)\n\n### Claim 1: Disagreement as High-Precision Diagnostic Signal\nWhen the same LLM formalizes a reasoning problem into two distinct representations (FOL/Z3 and executable Python), disagreements occur at a substantial rate (~40%) and are diagnostically informative with high precision (~87%). This cross-representation signal detects formalization-specific errors invisible to within-representation verification.\n\n**MVP evidence**: C1=39.6% disagree rate, C2=86.8% diagnostic rate on FOLIO (204 samples, Qwen3-32B).\n\n### Claim 2: Accurate Error Localization and Classification\nDisagreement patterns enable automatic error localization (identifying which representation contains the error) with high accuracy (~85%), and error type classification into a structured taxonomy (≥3 distinct types). The 9:1 asymmetry (FOL almost always correct, Code almost always erroneous) itself reveals fundamental differences in how LLMs handle formal logic vs. imperative code generation.\n\n**MVP evidence**: C5=85.4% localization accuracy, C3=3 error types. FOL:Code error ratio 9:1.\n\n### Claim 3: Characterizing the Boundary of Diagnosis-Guided Repair\nWe systematically characterize when cross-representation diagnosis enables effective targeted repair vs. when correlated failures limit repair gains. Targeted repair shows modest improvement over blind regeneration in All-mode (+5.2pp), but the advantage concentrates on specific sample subsets (GT=Unknown). This boundary characterization — distinguishing formalization-specific errors (catchable) from specification-level errors (producing false agreement) — is itself a contribution to understanding neurosymbolic failure modes.\n\n**MVP evidence**: C4 All-mode +5.2pp, Excl-Unknown +0.0pp. Unknown samples drive the repair delta.\n\n## Story Spine\n\n- **Problem**: Neurosymbolic reasoning pipelines suffer from formalization errors as their dominant failure mode. The LLM's translation from natural language to formal representation introduces subtle corruptions. Current approaches either select one representation (HybridMind, Adaptive Selection), verify within one representation (VeriCoT, VERGE, Roundtrip Verification), or filter disagreeing solutions without diagnosis (Liang et al. 2024, Prove 2024). The gap: nobody uses cross-representation disagreement patterns for error CATEGORIZATION and TARGETED REPAIR.\n\n- **Existing approaches & gaps**: Liang et al. (2024) proved CoT-PoT disagreement is informative for filtering but stopped at discarding disagreements — no error categorization, no repair. Roundtrip Verification (2026) showed diagnosis-guided repair works within a single representation on a narrow domain (150 traffic rules). No method exploits cross-representation disagreement as a diagnostic signal enabling categorized diagnosis and targeted repair.\n\n- **Our framing (dual-track)**: We present (1) the first systematic empirical analysis of cross-representation disagreement patterns in neurosymbolic reasoning — characterizing disagreement rates, error types, localization accuracy, and failure mode boundaries across domains and models; and (2) a lightweight diagnosis-guided repair framework that operates at inference time without model modification. The analysis is the primary contribution; the repair framework demonstrates downstream utility.\n\n- **Headline result template**: \"On [benchmarks], cross-representation disagreement detects [X]% of samples as potentially erroneous with [Y]% diagnostic precision and [Z]% error localization accuracy. We characterize a fundamental asymmetry: [logic representation] exhibits [N]x lower formalization error rate than [code representation], revealing systematic differences in how LLMs handle formal logic vs. imperative code generation.\"\n\n## Venue Fit\n\n- **EMNLP fit (strong)**: NLP + symbolic reasoning is a core track. Dual-track framing (systematic analysis + method) aligns with EMNLP's tradition of accepting empirical analyses. The correlated failure / boundary characterization angle fits EMNLP's emphasis on rigorous evaluation.\n- **Risk**: modest repair improvement → mitigate by framing analysis as primary contribution, repair as secondary.\n- **Risk**: single model+dataset insufficient → extend to ≥2 models and ≥3 benchmarks in research phase.\n\n## Anticipated Reviewer Concerns & Responses\n\n| # | Concern | Response Strategy | Required Experiment |\n|---|---------|-------------------|---------------------|\n| R1 | Single model/dataset — generalization? | Cross-model ablation + multi-benchmark | exp-002, exp-003, exp-004 |\n| R2 | C4 repair improvement marginal | Honest framing + boundary characterization as contribution | exp-005, exp-006 |\n| R3 | Why repair, not just select correct side? | Selection vs repair ablation | exp-007 |\n| R4 | Error taxonomy rule-based, not learned | Deliberate choice for interpretability; taxonomy-guided vs fixed strategy ablation | exp-008 |\n| R5 | FOL 9:1 asymmetry — just FOL-as-verifier? | Test on math domain where asymmetry may differ | exp-004 |\n| R6 | Statistical significance? | Bootstrap CI + Fisher exact test on all metrics | exp-009 |\n| R7 | Correlated failures (Denisov-Blanch 2026) | Explicit quantification + cross-model ablation reduces correlation | exp-002, exp-006 |\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'FOLIO 完整分析（MVP 数据深度挖掘）: 基于 204 样本 MVP 数据，完成统计显著性检验、错误类型详细分类、Unknown\n    样本子集分析、repair 前后对比。不需要新实验运行，纯分析。'\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: mvp_pipeline_004\n  status: ANALYZING\n  conclusion: success\n  metrics:\n    progress: 204/204 (deduped from 211)\n    deduped: true\n    dedup_original:\n      all_mode:\n        C1_disagree_rate: 39.6% (76/192)\n        C2_diagnostic_rate: 86.8% (66/76)\n        C3_error_types: 3 types\n        C4_targeted_vs_blind: +6.2pp (T:60/96 B:54/96)\n        C5_localization: 85.4% (35/41)\n        mvp_pass: 5/5 PASS\n      excl_unknown:\n        C1_disagree_rate: 35.7% (45/126)\n        C2_diagnostic_rate: 84.4% (38/45)\n        C3_error_types: 2 types\n        C4_targeted_vs_blind: -1.7pp (T:34/59 B:35/59)\n        C5_localization: 89.3% (25/28)\n        mvp_pass: 4/5 (C4 FAIL)\n    repair_fixed:\n      all_mode:\n        C1_disagree_rate: 39.6% (76/192)\n        C2_diagnostic_rate: 86.8% (66/76)\n        C3_error_types: 3 types\n        C4_targeted_vs_blind: +5.2pp (T:61/96 B:56/96)\n        C5_localization: 85.4% (35/41)\n        mvp_pass: 5/5 PASS\n      excl_unknown:\n        C1_disagree_rate: 35.7% (45/126)\n        C2_diagnostic_rate: 84.4% (38/45)\n        C3_error_types: 2 types\n        C4_targeted_vs_blind: +0.0pp (T:38/59 B:38/59)\n        C5_localization: 89.3% (25/28)\n        mvp_pass: 4/5 (C4 FAIL)\n    final_verdict: All-mode 5/5 PASS (both original and repair)\n- id: exp-002\n  claim:\n  - 1\n  - 2\n  description: '跨模型消融（FOLIO）: DeepSeek V4 Pro 生成一种表征 + Qwen3-32B 生成另一种，测试模型多样性是否降低\n    correlated failures、提升诊断覆盖率。FOLIO 204 样本。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  api_cost_estimate: $15-25 (DeepSeek V4 Pro promotional pricing)\n  status: planned\n- id: exp-003\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'ProofWriter 扩展: 在 ProofWriter 数据集上运行完整 pipeline（双表征+诊断+repair），验证方法在第二个逻辑推理\n    benchmark 上的泛化性。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  status: planned\n- id: exp-004\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'MATH Level 5 扩展: 在 MATH 难题子集上运行 pipeline（CoT vs SymPy/Python 双表征），测试跨领域泛化性。数学领域的\n    FOL:Code 不对称性可能不同。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  status: planned\n- id: exp-005\n  claim: 3\n  description: 'Repair 机制改进: 多轮 repair（max 3 rounds）、改进 repair prompt（加入错误类型特定的修复策略）、对比\n    repair 前后的 C4 delta。目标：拉大 targeted vs blind 差距。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  status: planned\n- id: exp-006\n  claim: 3\n  description: 'Unknown 样本深度分析: 为什么 GT=Unknown 样本驱动 C4 delta？分析 Unknown 样本的错误模式分布，是否存在\n    specification-level vs formalization-specific 的系统性差异。'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n- id: exp-007\n  claim: 3\n  description: 'Selection vs Repair 消融: 当检测到分歧且定位了错误侧后，直接选择另一侧答案（selection）vs 诊断引导修复（repair）的对比。回应\n    Reviewer Concern R3。'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  claim: 2\n  description: 'Error Taxonomy 消融: 按错误类型分派修复策略 vs 固定策略（统一重生成），验证 taxonomy 的规定性价值。'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-005\n  status: planned\n- id: exp-009\n  claim:\n  - 1\n  - 2\n  - 3\n  description: '统计显著性全面检验: 对所有 benchmark 的 C1-C5 指标做 bootstrap 95% CI + Fisher exact\n    test / McNemar test，确保所有 claim 有统计支撑。'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-003\n  - exp-004\n  status: planned\n- id: exp-010\n  claim:\n  - 1\n  - 2\n  description: 'Qwen3-8B 消融: 低能力模型上的诊断率和分歧率是否变化？测试方法对模型能力的鲁棒性。'\n  priority: P2\n  gpu_budget_hours: 4\n  deps: []\n  status: planned\n- id: exp-011\n  claim:\n  - 1\n  - 2\n  description: 'GPQA Diamond 扩展: 科学知识推理领域，CoT vs Python 验证代码。'\n  priority: P2\n  gpu_budget_hours: 6\n  deps:\n  - exp-004\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_baseline_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.74\n    correct: 37\n    total: 50\n    gate: PASS_FOLIO\n- exp_id: mvp_pipeline_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    disagree_rate: 0.04\n    diagnostic_rate: 1\n    error_types: 4\n    targeted_repair: 0.1875\n    blind_repair: 0.4688\n    delta_pp: -28.12\n    localization: 0.4186\n    fol_accuracy: 0.14\n    code_accuracy: 0.52\n    C1: false\n    C2: true\n    C3: true\n    C4: false\n    C5: false\n- exp_id: mvp_pipeline_002\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    fol_crash_rate_v2: 0.1\n    code_crash_rate_v2: 0.4\n    fol_crash_rate_v3: 0.8\n    code_crash_rate_v3: 0\n    fol_accuracy_v3: 0.2\n    code_accuracy_v3: 0.6\n    oracle_accuracy_v3: 0.6\n    disagree_rate_v3: 0\n    effective_disagree_rate_v3: 0\n    diagnostic_rate_v3: null\n    targeted_rate_v3: 0.5\n    blind_rate_v3: 0.625\n    delta_pp_v3: -12.5\n    localization_accuracy_v3: 0.5\n    error_types_v3: 3\n    C1_v3: false\n    C2_v3: false\n    C3_v3: true\n    C4_v3: false\n    C5_v3: false\n    avg_time_per_sample_s_v3: 218.5\n    total_api_calls_v3: 48\n    input_tokens_v3: 50558\n    output_tokens_v3: 139706\n    samples_v3: 10\n    v3_changes: enable_thinking=False for Code generation, _strip_thinking unclosed\n      tag handling\n- exp_id: mvp_pipeline_003\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_003b\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_004\n  name: ''\n  status: ANALYZING\n  conclusion: success\n  metrics:\n    progress: 204/204 (deduped from 211)\n    deduped: true\n    dedup_original:\n      all_mode:\n        C1_disagree_rate: 39.6% (76/192)\n        C2_diagnostic_rate: 86.8% (66/76)\n        C3_error_types: 3 types\n        C4_targeted_vs_blind: +6.2pp (T:60/96 B:54/96)\n        C5_localization: 85.4% (35/41)\n        mvp_pass: 5/5 PASS\n      excl_unknown:\n        C1_disagree_rate: 35.7% (45/126)\n        C2_diagnostic_rate: 84.4% (38/45)\n        C3_error_types: 2 types\n        C4_targeted_vs_blind: -1.7pp (T:34/59 B:35/59)\n        C5_localization: 89.3% (25/28)\n        mvp_pass: 4/5 (C4 FAIL)\n    repair_fixed:\n      all_mode:\n        C1_disagree_rate: 39.6% (76/192)\n        C2_diagnostic_rate: 86.8% (66/76)\n        C3_error_types: 3 types\n        C4_targeted_vs_blind: +5.2pp (T:61/96 B:56/96)\n        C5_localization: 85.4% (35/41)\n        mvp_pass: 5/5 PASS\n      excl_unknown:\n        C1_disagree_rate: 35.7% (45/126)\n        C2_diagnostic_rate: 84.4% (38/45)\n        C3_error_types: 2 types\n        C4_targeted_vs_blind: +0.0pp (T:38/59 B:38/59)\n        C5_localization: 89.3% (25/28)\n        mvp_pass: 4/5 (C4 FAIL)\n    final_verdict: All-mode 5/5 PASS (both original and repair)\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-15T06:14:27.837Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T06:14:27.837Z",
  "sessionId": "ecc5382a-3f63-45a1-993b-0dee29c58083"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-15T06:14:27.863Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：诊断信号在 FOLIO 外不稳健——disagree rate 过低或 precision 大幅下降，repair 无正向效果，核心 framing 需重构
核心假设：['ProofWriter/MATH 上 C1 disagree rate <20% 或 C2 diagnostic precision <65%，信号不具跨域一致性', 'exp-005 repair 改进未能突破，C4 delta ≤3pp (All-mode)，Excl-Unknown 为负', 'MATH 域双表征分歧模式与逻辑域本质不同，不支持统一框架叙事', 'exp-002 跨模型消融未有效降低 correlated failures', '统计显著性在新 benchmark 上不成立 (p>0.05 或 CI 跨零)', '仅 FOLIO 单 benchmark 数据可靠']
关键指标范围：{'C1_disagree_rate_cross_bench': [0.1, 0.25], 'C2_diagnostic_precision_cross_bench': [0.55, 0.7], 'C4_targeted_vs_blind_delta_pp_all_mode': [-2.0, 3.0], 'C4_targeted_vs_blind_delta_pp_excl_unknown': [-4.0, 0.0], 'C5_localization_accuracy_cross_bench': [0.6, 0.75], 'cross_model_false_agreement_reduction_pp': [-1.0, 2.0], 'MATH_fol_code_error_ratio': [5.0, 9.0], 'benchmarks_with_5of5_pass': [0, 1]}
叙事方向：放弃 'general cross-representation diagnosis framework' 的普适性叙事。Reframe 为 domain-specific 深度研究：'When and Why Cross-Representation Disagreement Works: A Case Study in Formal Logic Reasoning'。核心 angle 转向：(1) 深度刻画 FOL-Code 分歧在逻辑推理中的独特有效性及其认知/结构原因（为什么 FOL 几乎总对而 Code 几乎总错），(2) 系统性分析跨域失败的原因（correlated failures、specification-level errors 的普遍性），(3) 提出 cross-representation diagnosis 的 applicability conditions。这个 reframe 仍然是 EMNLP Main 级别——深度 empirical analysis + negative results + boundary conditions 的组合在 EMNLP 有先例。但需要 FOLIO 上的分析足够深（补充 exp-006/007/008 全部完成），用深度补广度。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: cross_representation_disagreement_diagno
focus: C4 repair improvement is the main weakness (0.2pp margin). Key questions: (1) Is the dual-track framing (systematic analysis + lightweight repair) strong enough for EMNLP Main? (2) Does the boundary characterization (Claim 3) compensate for weak repair results? (3) Is 3 benchmarks (FOLIO + ProofWriter + MATH) sufficient or do we need more? (4) The 9:1 FOL:Code asymmetry — strength or weakness for the story?

## paper_framing.md

# Paper Framing — cross_representation_disagreement_diagno

## Target Venue
- Primary: EMNLP 2026 Main (ARR submission)
- Fallback: EMNLP 2026 Findings
- Deadline: ARR May 25, 2026 (10 days)
- Secondary: AAAI 2027 (abstract July 25, full August 1) — extended version with full benchmark coverage

## Core Insight
Cross-representation disagreement (FOL/Z3 vs Python Code) produced by the same LLM for the same reasoning problem is an underexploited diagnostic signal that detects formalization errors, enables error localization and classification, and guides targeted repair — going beyond existing approaches that only filter or verify within a single representation.

## Core Claims (3 条)

### Claim 1: Disagreement as High-Precision Diagnostic Signal
When the same LLM formalizes a reasoning problem into two distinct representations (FOL/Z3 and executable Python), disagreements occur at a substantial rate (~40%) and are diagnostically informative with high precision (~87%). This cross-representation signal detects formalization-specific errors invisible to within-representation verification.

**MVP evidence**: C1=39.6% disagree rate, C2=86.8% diagnostic rate on FOLIO (204 samples, Qwen3-32B).

### Claim 2: Accurate Error Localization and Classification
Disagreement patterns enable automatic error localization (identifying which representation contains the error) with high accuracy (~85%), and error type classification into a structured taxonomy (≥3 distinct types). The 9:1 asymmetry (FOL almost always correct, Code almost always erroneous) itself reveals fundamental differences in how LLMs handle formal logic vs. imperative code generation.

**MVP evidence**: C5=85.4% localization accuracy, C3=3 error types. FOL:Code error ratio 9:1.

### Claim 3: Characterizing the Boundary of Diagnosis-Guided Repair
We systematically characterize when cross-representation diagnosis enables effective targeted repair vs. when correlated failures limit repair gains. Targeted repair shows modest improvement over blind regeneration in All-mode (+5.2pp), but the advantage concentrates on specific sample subsets (GT=Unknown). This boundary characterization — distinguishing formalization-specific errors (catchable) from specification-level errors (producing false agreement) — is itself a contribution to understanding neurosymbolic failure modes.

**MVP evidence**: C4 All-mode +5.2pp, Excl-Unknown +0.0pp. Unknown samples drive the repair delta.

## Story Spine

- **Problem**: Neurosymbolic reasoning pipelines suffer from formalization errors as their dominant failure mode. The LLM's translation from natural language to formal representation introduces subtle corruptions. Current approaches either select one representation (HybridMind, Adaptive Selection), verify within one representation (VeriCoT, VERGE, Roundtrip Verification), or filter disagreeing solutions without diagnosis (Liang et al. 2024, Prove 2024). The gap: nobody uses cross-representation disagreement patterns for error CATEGORIZATION and TARGETED REPAIR.

- **Existing approaches & gaps**: Liang et al. (2024) proved CoT-PoT disagreement is informative for filtering but stopped at discarding disagreements — no error categorization, no repair. Roundtrip Verification (2026) showed diagnosis-guided repair works within a single representation on a narrow domain (150 traffic rules). No method exploits cross-representation disagreement as a diagnostic signal enabling categorized diagnosis and targeted repair.

- **Our framing (dual-track)**: We present (1) the first systematic empirical analysis of cross-representation disagreement patterns in neurosymbolic reasoning — characterizing disagreement rates, error types, localization accuracy, and failure mode boundaries across domains and models; and (2) a lightweight diagnosis-guided repair framework that operates at inference time without model modification. The analysis is the primary contribution; the repair framework demonstrates downstream utility.

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


## experiment_plan (with registry status)

- id: exp-001
  claim:
  - 1
  - 2
  - 3
  description: 'FOLIO 完整分析（MVP 数据深度挖掘）: 基于 204 样本 MVP 数据，完成统计显著性检验、错误类型详细分类、Unknown
    样本子集分析、repair 前后对比。不需要新实验运行，纯分析。'
  priority: P0
  gpu_budget_hours: 0
  deps: []
  registry_id: mvp_pipeline_004
  status: ANALYZING
  conclusion: success
  metrics:
    progress: 204/204 (deduped from 211)
    deduped: true
    dedup_original:
      all_mode:
        C1_disagree_rate: 39.6% (76/192)
        C2_diagnostic_rate: 86.8% (66/76)
        C3_error_types: 3 types
        C4_targeted_vs_blind: +6.2pp (T:60/96 B:54/96)
        C5_localization: 85.4% (35/41)
        mvp_pass: 5/5 PASS
      excl_unknown:
        C1_disagree_rate: 35.7% (45/126)
        C2_diagnostic_rate: 84.4% (38/45)
        C3_error_types: 2 types
        C4_targeted_vs_blind: -1.7pp (T:34/59 B:35/59)
        C5_localization: 89.3% (25/28)
        mvp_pass: 4/5 (C4 FAIL)
    repair_fixed:
      all_mode:
        C1_disagree_rate: 39.6% (76/192)
        C2_diagnostic_rate: 86.8% (66/76)
        C3_error_types: 3 types
        C4_targeted_vs_blind: +5.2pp (T:61/96 B:56/96)
        C5_localization: 85.4% (35/41)
        mvp_pass: 5/5 PASS
      excl_unknown:
        C1_disagree_rate: 35.7% (45/126)
        C2_diagnostic_rate: 84.4% (38/45)
        C3_error_types: 2 types
        C4_targeted_vs_blind: +0.0pp (T:38/59 B:38/59)
        C5_localization: 89.3% (25/28)
        mvp_pass: 4/5 (C4 FAIL)
    final_verdict: All-mode 5/5 PASS (both original and repair)
- id: exp-002
  claim:
  - 1
  - 2
  description: '跨模型消融（FOLIO）: DeepSeek V4 Pro 生成一种表征 + Qwen3-32B 生成另一种，测试模型多样性是否降低
    correlated failures、提升诊断覆盖率。FOLIO 204 样本。'
  priority: P0
  gpu_budget_hours: 4
  deps:
  - exp-001
  api_cost_estimate: $15-25 (DeepSeek V4 Pro promotional pricing)
  status: planned
- id: exp-003
  claim:
  - 1
  - 2
  - 3
  description: 'ProofWriter 扩展: 在 ProofWriter 数据集上运行完整 pipeline（双表征+诊断+repair），验证方法在第二个逻辑推理
    benchmark 上的泛化性。'
  priority: P0
  gpu_budget_hours: 6
  deps: []
  status: planned
- id: exp-004
  claim:
  - 1
  - 2
  - 3
  description: 'MATH Level 5 扩展: 在 MATH 难题子集上运行 pipeline（CoT vs SymPy/Python 双表征），测试跨领域泛化性。数学领域的
    FOL:Code 不对称性可能不同。'
  priority: P0
  gpu_budget_hours: 8
  deps: []
  status: planned
- id: exp-005
  claim: 3
  description: 'Repair 机制改进: 多轮 repair（max 3 rounds）、改进 repair prompt（加入错误类型特定的修复策略）、对比
    repair 前后的 C4 delta。目标：拉大 targeted vs blind 差距。'
  priority: P0
  gpu_budget_hours: 4
  deps:
  - exp-001
  status: planned
- id: exp-006
  claim: 3
  description: 'Unknown 样本深度分析: 为什么 GT=Unknown 样本驱动 C4 delta？分析 Unknown 样本的错误模式分布，是否存在
    specification-level vs formalization-specific 的系统性差异。'
  priority: P1
  gpu_budget_hours: 0
  deps:
  - exp-001
  status: planned
- id: exp-007
  claim: 3
  description: 'Selection vs Repair 消融: 当检测到分歧且定位了错误侧后，直接选择另一侧答案（selection）vs 诊断引导修复（repair）的对比。回应
    Reviewer Concern R3。'
  priority: P1
  gpu_budget_hours: 2
  deps:
  - exp-001
  status: planned
- id: exp-008
  claim: 2
  description: 'Error Taxonomy 消融: 按错误类型分派修复策略 vs 固定策略（统一重生成），验证 taxonomy 的规定性价值。'
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
    test / McNemar test，确保所有 claim 有统计支撑。'
  priority: P1
  gpu_budget_hours: 0
  deps:
  - exp-001
  - exp-003
  - exp-004
  status: planned
- id: exp-010
  claim:
  - 1
  - 2
  description: 'Qwen3-8B 消融: 低能力模型上的诊断率和分歧率是否变化？测试方法对模型能力的鲁棒性。'
  priority: P2
  gpu_budget_hours: 4
  deps: []
  status: planned
- id: exp-011
  claim:
  - 1
  - 2
  description: 'GPQA Diamond 扩展: 科学知识推理领域，CoT vs Python 验证代码。'
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
    dedup_original:
      all_mode:
        C1_disagree_rate: 39.6% (76/192)
        C2_diagnostic_rate: 86.8% (66/76)
        C3_error_types: 3 types
        C4_targeted_vs_blind: +6.2pp (T:60/96 B:54/96)
        C5_localization: 85.4% (35/41)
        mvp_pass: 5/5 PASS
      excl_unknown:
        C1_disagree_rate: 35.7% (45/126)
        C2_diagnostic_rate: 84.4% (38/45)
        C3_error_types: 2 types
        C4_targeted_vs_blind: -1.7pp (T:34/59 B:35/59)
        C5_localization: 89.3% (25/28)
        mvp_pass: 4/5 (C4 FAIL)
    repair_fixed:
      all_mode:
        C1_disagree_rate: 39.6% (76/192)
        C2_diagnostic_rate: 86.8% (66/76)
        C3_error_types: 3 types
        C4_targeted_vs_blind: +5.2pp (T:61/96 B:56/96)
        C5_localization: 85.4% (35/41)
        mvp_pass: 5/5 PASS
      excl_unknown:
        C1_disagree_rate: 35.7% (45/126)
        C2_diagnostic_rate: 84.4% (38/45)
        C3_error_types: 2 types
        C4_targeted_vs_blind: +0.0pp (T:38/59 B:38/59)
        C5_localization: 89.3% (25/28)
        mvp_pass: 4/5 (C4 FAIL)
    final_verdict: All-mode 5/5 PASS (both original and repair)

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
  "promptId": "05c35ade-570f-48a5-8513-cce3f89e5447",
  "type": "user",
  "uuid": "9b1323e4-17f4-4c0f-9a92-9a7fc700d254",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "ecc5382a-3f63-45a1-993b-0dee29c58083",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T06:14:27.861Z_

```json
{
  "parentUuid": "9b1323e4-17f4-4c0f-9a92-9a7fc700d254",
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
  "uuid": "80600ea0-70e4-4dba-adc3-5826e03bd2c6",
  "timestamp": "2026-05-15T06:14:27.861Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "ecc5382a-3f63-45a1-993b-0dee29c58083",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T06:14:27.861Z_

```json
{
  "parentUuid": "80600ea0-70e4-4dba-adc3-5826e03bd2c6",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7656fd32-2f5d-4a58-8ec2-3cbe65a83a00",
  "timestamp": "2026-05-15T06:14:27.861Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "ecc5382a-3f63-45a1-993b-0dee29c58083",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：诊断信号在 FOLIO 外不稳健——disagree rate 过低或 precision 大幅下降，repair 无正向效果，核心 framing 需重构 核心假设：['ProofWriter/MATH 上 C1 disagree rate <20% 或 C2 diagnostic precision <…",
  "leafUuid": "7656fd32-2f5d-4a58-8ec2-3cbe65a83a00",
  "sessionId": "ecc5382a-3f63-45a1-993b-0dee29c58083"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterize boundary conditions for cross-representation diagnosis",
  "sessionId": "ecc5382a-3f63-45a1-993b-0dee29c58083"
}
```

---

### Assistant

_source line 8 · 2026-05-15T06:14:53.015Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental data for the "worst" tier scenario for each planned experiment in their experiment plan. I need to provide specific metric predictions with rationales explaining why these results would occur under the worst-case scenario.

Let me carefully analyze the worst tier definition:

**Worst tier meaning**: Diagnostic signal is not robust outside FOLIO — disagree rate too low or precision drops significantly, repair has no positive effect, core framing needs restructuring.

**Key assumptions**:
1. ProofWriter/MATH: C1 disagree rate <20% or C2 diagnostic precision <65%
2. exp-005 repair improvement fails, C4 delta ≤3pp (All-mode), Excl-Unknown negative


3. MATH dual-representation disagreement patterns diverge significantly from the logic domain patterns
4. exp-002 cross-model ablation doesn't effectively reduce correlated failures
5. Statistical significance doesn't hold on new benchmarks (p>0.05 or CI crosses zero)
6. Only FOLIO single benchmark data is reliable

**Key metric ranges**:
- C1_disagree_rate_cross_bench: [0.1, 0.25]
- C2_diagnostic_precision_cross_bench: [0.55, 0.7]
- C4_targeted_vs_blind_delta_pp_all_mode: [-2.0, 3]
- C4_targeted_vs_blind_delta_pp_excl_unknown: [-4.0, 0.0]
- C5_localization_accuracy_cross_bench: [0.6, 0.75]
- cross_model_false_agreement_reduction_pp: [-1.0, 2.0]
- MATH_fol_code_error_ratio: [5.0, 9.0]
- benchmarks_with_5of5_pass: [0, 1]

**Narrative direction**: Abandon universal "general cross-representation diagnosis framework" narrative. Reframe as domain-specific deep study.

Now I'm looking at exp-002 with DeepSeek V4 Pro and Qwen3-32B on FOLIO—the cross-model ablation approach doesn't actually reduce correlated failures effectively, which puts it in the worst tier of results.

For exp-003 on ProofWriter, the simpler, more formulaic nature of the task means both models tend to produce correlated formalizations, so the disagree rate drops because they fail in the same ways rather than catching each other's errors. With exp-004 on MATH Level 5, the domain itself has fundamentally different error patterns where CoT and SymPy fail in correlated ways, keeping the disagree rate very low. The repair mechanism in exp-005 doesn't help much because the errors are specification-level rather than something multi-round fixing can address. For exp-006, I'm doing a pure analysis of the unknown samples to understand what's actually happening there.

Now looking at the remaining experiments: selection might actually outperform repair in exp-007, which would undermine the repair contribution claim. The taxonomy-guided repair in exp-008 appears to be roughly equivalent to a fixed strategy, suggesting the taxonomy itself doesn't provide prescriptive value. Statistical significance testing in exp-009 shows FOLIO is significant but ProofWriter and MATH aren't. Using a lower capability model like Qwen3-8B in exp-010 makes the disagree rate or diagnostic precision even worse. And exp-011 on GPQA Diamond suggests the science domain performs even worse than MATH. I'm now organizing all these findings into detailed YAML output.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7656fd32-2f5d-4a58-8ec2-3cbe65a83a00",
  "isSidechain": false,
  "requestId": "req_011Cb3s14WfEFdrXGedfmLty",
  "type": "assistant",
  "uuid": "40091779-888b-44da-afe5-a1ac50798c14",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "ecc5382a-3f63-45a1-993b-0dee29c58083",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016WyPXrWdkeQTcdYwJkgiCV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11059,
      "cache_read_input_tokens": 11841,
      "output_tokens": 15365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11059,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 15365,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11059,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11059
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

_source line 9 · 2026-05-15T06:19:20.180Z_

```yaml
tier: worst
narrative_guidance: >
  放弃 'general cross-representation diagnosis framework' 的普适性叙事。Reframe 为 domain-specific
  深度研究：'When and Why Cross-Representation Disagreement Works: A Case Study in Formal
  Logic Reasoning'。核心 angle 转向：(1) 深度刻画 FOL-Code 分歧在逻辑推理中的独特有效性及其认知/结构原因，
  (2) 系统性分析跨域失败的原因（correlated failures、specification-level errors 的普遍性），
  (3) 提出 cross-representation diagnosis 的 applicability conditions。用深度补广度，FOLIO 上
  的分析必须足够深。

imagined_experiments:
  - name: "Cross-Model Ablation (FOLIO)"
    plan_id: "exp-002"
    description: "DeepSeek V4 Pro 生成一种表征 + Qwen3-32B 生成另一种，测试模型多样性是否降低 correlated failures"
    expected_results:
      C1_disagree_rate_mixed: 0.42
      C1_disagree_rate_deepseek_only: 0.33
      C2_diagnostic_precision_mixed: 0.83
      C2_diagnostic_precision_deepseek_only: 0.78
      false_agreement_reduction_vs_single_model_pp: 1.5
      correlated_failure_rate_single_model: 0.18
      correlated_failure_rate_mixed_model: 0.165
      C5_localization_mixed: 0.81
      new_disagreement_type_introduced: true
      spurious_disagreement_rate_mixed: 0.09
    result_rationale: >
      混合模型配置仅将 false agreement 降低约 1.5pp（从 ~18% 到 ~16.5%），远低于预期的 5-8pp。
      原因：correlated failures 的根源不在于 "同一个模型的 shared bias"，而在于 specification-level
      ambiguity——两个不同模型面对同一道模糊 NL 问题时，犯相同的 specification error 的概率仍然很高，
      因为错误来源是 NL 本身的歧义而非模型内部表征。DeepSeek V4 Pro 单独运行时 disagree rate 更低（33%
      vs 39.6%），说明更强模型的两种表征更趋一致（能力提升同时减少了 formalization-specific errors
      和 diagnostic opportunities）。混合模型引入约 9% 的 spurious disagreements——两个模型对
      同一问题的合法但不同的形式化选择（如变量命名、逻辑等价变换），这些分歧不是 errors 而是 representation
      divergence，降低了整体 precision。结论：模型多样性不是解决 correlated failures 的有效路径，
      因为 correlation 的主要来源是 task specification 而非 model bias。
    tables:
      - table_id: "tab-exp002-1"
        caption: "Cross-Model vs Single-Model Pipeline Comparison (FOLIO, N=192)"
        columns: ["Config", "C1 Disagree%", "C2 Precision%", "Correlated Failure%", "Spurious Disagree%", "C5 Localization%"]
        rows:
          - ["Qwen3-32B (single)", "39.6%", "86.8%", "18.2%", "3.1%", "85.4%"]
          - ["DeepSeek V4 Pro (single)", "33.3%", "78.1%", "19.8%", "4.2%", "79.7%"]
          - ["Mixed (DS-FOL, Qwen-Code)", "42.2%", "83.3%", "16.5%", "9.1%", "81.3%"]
          - ["Mixed (Qwen-FOL, DS-Code)", "40.6%", "80.6%", "17.1%", "8.7%", "78.9%"]
      - table_id: "tab-exp002-2"
        caption: "False Agreement Breakdown by Error Source"
        columns: ["Error Source", "Single-Model False Agree%", "Mixed-Model False Agree%", "Δ"]
        rows:
          - ["Specification-level ambiguity", "11.5%", "10.9%", "-0.6pp"]
          - ["Shared formalization bias", "4.2%", "3.1%", "-1.1pp"]
          - ["Independent coincidental", "2.5%", "2.5%", "0.0pp"]
    figures_description:
      - "Venn diagram: Qwen-only failures vs DeepSeek-only failures vs shared failures, showing ~70% overlap in false-agreement samples across models — evidence that correlated failures are task-driven not model-driven"
      - "Bar chart: spurious disagreement rate by disagreement category (legitimate formalization choice vs actual error), showing mixed-model introduces ~3x more spurious disagreements"
    analysis: >
      核心发现是 correlated failures 的主要来源是 task specification 而非 model bias，因此
      cross-model 策略的边际收益极小。这对 general framework 叙事是重大打击——如果 false agreement
      无法通过模型多样性有效缓解，那么 diagnosis coverage 存在固有上限。但这一 negative result 本身
      具有 insight 价值：它揭示了 cross-representation diagnosis 的 fundamental limitation
      来自 NL-to-formal 的 specification gap，而非模型能力。在 reframed narrative 中，这成为
      boundary characterization 的关键 evidence。

  - name: "ProofWriter Extension"
    plan_id: "exp-003"
    description: "在 ProofWriter 上运行完整 pipeline，验证逻辑推理域内泛化性"
    expected_results:
      N_samples: 300
      C1_disagree_rate: 0.17
      C2_diagnostic_precision: 0.63
      C3_error_types: 2
      C4_targeted_vs_blind_delta_pp_all_mode: 1.8
      C4_targeted_vs_blind_delta_pp_excl_unknown: -2.1
      C5_localization_accuracy: 0.72
      fol_code_error_ratio: "7:1"
      mvp_pass_count: "2/5 (C1 borderline FAIL at <20% threshold pending, C2 FAIL, C3 PASS, C4 FAIL, C5 PASS)"
      bootstrap_C1_95CI: [0.13, 0.22]
      bootstrap_C2_95CI: [0.54, 0.71]
      fisher_exact_C4_p_value: 0.31
    result_rationale: >
      ProofWriter 的 disagree rate 仅 17%，远低于 FOLIO 的 39.6%。根本原因：ProofWriter 的问题
      结构高度规范化——前提以 "If X then Y" 的固定模板给出，推理深度可控（depth 0-5），NL 歧义极少。
      这意味着 LLM 在 FOL 和 Code 两种表征上都能较准确地捕获 specification，formalization-specific
      errors 的发生率本身就低。剩余的 17% 分歧中，diagnostic precision 降至 63%：更多分歧来自
      "两种表征对 closed-world assumption 的不同处理"——FOL/Z3 默认 CWA 而 Python 代码常遗漏
      CWA 导致的推理差异，这类分歧是 representation semantics gap 而非 formalization error。
      error types 仅 2 种（缺少 FOLIO 上的 "scope ambiguity" 类型，因为 ProofWriter 无量词
      作用域歧义）。Repair delta 仅 1.8pp（All-mode），因为可诊断的 errors 本身就少，且 CWA-related
      分歧不可通过 repair 单侧修复。Excl-Unknown 为负（-2.1pp），因为 ProofWriter 无 Unknown
      类别，所有样本都是 True/False，移除了 FOLIO 上驱动 repair delta 的主要子集。
    tables:
      - table_id: "tab-exp003-1"
        caption: "ProofWriter Full Pipeline Results (N=300, Qwen3-32B)"
        columns: ["Metric", "ProofWriter", "FOLIO (reference)", "Δ"]
        rows:
          - ["C1 Disagree Rate", "17.0% (42/247)", "39.6% (76/192)", "-22.6pp"]
          - ["C2 Diagnostic Precision", "63.2% (24/38)", "86.8% (66/76)", "-23.6pp"]
          - ["C3 Error Types", "2", "3", "-1"]
          - ["C4 Δ (All-mode)", "+1.8pp", "+5.2pp", "-3.4pp"]
          - ["C4 Δ (Excl-Unknown)", "-2.1pp", "+0.0pp", "-2.1pp"]
          - ["C5 Localization", "72.0%", "85.4%", "-13.4pp"]
      - table_id: "tab-exp003-2"
        caption: "Disagreement Source Analysis: ProofWriter vs FOLIO"
        columns: ["Disagreement Source", "ProofWriter %", "FOLIO %"]
        rows:
          - ["Formalization-specific error (one side wrong)", "63.2%", "86.8%"]
          - ["CWA/semantic gap (neither side truly wrong)", "26.3%", "5.3%"]
          - ["Both sides wrong (correlated failure)", "10.5%", "7.9%"]
      - table_id: "tab-exp003-3"
        caption: "ProofWriter Results by Reasoning Depth"
        columns: ["Depth", "N", "Disagree%", "Precision%", "Notes"]
        rows:
          - ["0", "62", "8.1%", "40.0%", "Trivial problems, few errors to detect"]
          - ["1", "68", "13.2%", "55.6%", "Simple chain, low formalization difficulty"]
          - ["2", "58", "17.2%", "66.7%", "Moderate depth"]
          - ["3", "52", "23.1%", "70.0%", "More complex chains increase error rate"]
          - ["5", "60", "26.7%", "75.0%", "Deepest reasoning shows highest signal"]
    figures_description:
      - "Line plot: disagree rate and diagnostic precision vs reasoning depth (0-5), showing monotonic increase — signal improves with task complexity but even depth-5 falls below FOLIO baseline"
      - "Confusion matrix: FOL vs Code correctness on ProofWriter, showing the 7:1 asymmetry persists but both sides are more accurate overall (fewer errors = fewer disagreements)"
    analysis: >
      ProofWriter 结果确认了 worst-case 假设：诊断信号在结构化程度更高的 benchmark 上显著退化。
      disagree rate 仅 17% 且 precision 仅 63%，均低于 FOLIO。关键 insight：cross-representation
      disagreement 的 informativeness 与 NL specification 的 ambiguity 正相关——ProofWriter
      的 "clean" NL 减少了 formalization errors，但也减少了 diagnostic opportunities。
      这不是方法的失败，而是 applicability boundary：当 NL→formal 翻译足够 straightforward
      时，cross-representation diagnosis 的附加价值有限。depth-5 子集数据（26.7% disagree,
      75% precision）暗示在更难的推理链上信号恢复，为 "complexity threshold" 的 boundary
      condition 提供了 evidence。Reframed narrative 中，ProofWriter 作为 "lower boundary"
      与 FOLIO 的 "sweet spot" 形成对照。

  - name: "MATH Level 5 Extension"
    plan_id: "exp-004"
    description: "在 MATH 难题子集运行 CoT vs SymPy/Python 双表征 pipeline"
    expected_results:
      N_samples: 200
      C1_disagree_rate: 0.14
      C2_diagnostic_precision: 0.58
      C3_error_types: 3
      C4_targeted_vs_blind_delta_pp_all_mode: -0.5
      C4_targeted_vs_blind_delta_pp_excl_unknown: -3.2
      C5_localization_accuracy: 0.63
      cot_sympy_error_ratio: "1.8:1"
      fol_code_error_ratio_equivalent: 7.2
      mvp_pass_count: "0/5 (all FAIL)"
      bootstrap_C1_95CI: [0.09, 0.19]
      bootstrap_C2_95CI: [0.47, 0.68]
      fisher_exact_C4_p_value: 0.82
      correlated_failure_rate: 0.31
      specification_error_rate: 0.24
    result_rationale: >
      MATH 域的双表征分歧模式与逻辑域本质不同，不支持统一框架叙事。核心原因有三：
      (1) 错误对称性逆转——CoT:SymPy error ratio 仅 1.8:1，远低于 FOLIO 的 9:1。数学推理中
      CoT 的自然语言链式推导和 SymPy 的符号计算犯错概率更接近，因为数学 errors 更多是 "计算错误"
      而非 "形式化翻译错误"。FOL 在逻辑域近乎 "ground truth" 的角色（因为 Z3 solver 的完备性）
      在数学域不成立——SymPy 无法解决所有数学问题类型（如几何、组合），常 fallback 到数值近似。
      (2) Correlated failure rate 高达 31%——MATH Level 5 的难度意味着模型在 CoT 和 SymPy
      两条路径上都无法正确 specify 问题（如组合恒等式、复杂积分），产生大量 false agreement（双方
      都错但碰巧同一答案或都无法执行）。
      (3) 分歧的 diagnostic content 不同——MATH 上的分歧更多反映 "能否用该表征解决此类问题"
      （capability mismatch）而非 "形式化翻译是否正确"（formalization quality）。例如
      SymPy 无法处理某些几何题，不是 formalization error 而是 tool limitation。
      这导致 C2 precision 仅 58%，C5 localization 仅 63%（因为 "错误侧" 的判定不明确——
      可能两侧都有道理但方法不同），repair delta 为负（targeted repair 反而引入 noise）。
    tables:
      - table_id: "tab-exp004-1"
        caption: "MATH Level 5 Full Pipeline Results (N=200, Qwen3-32B)"
        columns: ["Metric", "MATH", "FOLIO (ref)", "ProofWriter (ref)"]
        rows:
          - ["C1 Disagree Rate", "14.0% (24/172)", "39.6%", "17.0%"]
          - ["C2 Diagnostic Precision", "58.3% (14/24)", "86.8%", "63.2%"]
          - ["C3 Error Types", "3", "3", "2"]
          - ["C4 Δ All-mode", "-0.5pp", "+5.2pp", "+1.8pp"]
          - ["C4 Δ Excl-Unk", "-3.2pp", "+0.0pp", "-2.1pp"]
          - ["C5 Localization", "63.0%", "85.4%", "72.0%"]
          - ["Error Ratio (logic:code equiv)", "1.8:1", "9:1", "7:1"]
          - ["Correlated Failure Rate", "31.0%", "18.2%", "10.5%"]
      - table_id: "tab-exp004-2"
        caption: "MATH Disagreement Source by Problem Category"
        columns: ["MATH Category", "N", "Disagree%", "Precision%", "CoT:SymPy Error Ratio"]
        rows:
          - ["Algebra", "52", "17.3%", "71.4%", "2.5:1"]
          - ["Number Theory", "38", "15.8%", "60.0%", "2.0:1"]
          - ["Counting & Prob", "35", "11.4%", "50.0%", "1.5:1"]
          - ["Geometry", "28", "10.7%", "33.3%", "1.0:1"]
          - ["Precalculus", "25", "12.0%", "50.0%", "1.2:1"]
          - ["Intermediate Algebra", "22", "18.2%", "66.7%", "2.2:1"]
      - table_id: "tab-exp004-3"
        caption: "Error Type Distribution: MATH vs Logic Domains"
        columns: ["Error Type", "MATH %", "FOLIO %", "Interpretation"]
        rows:
          - ["Formalization-specific", "33%", "72%", "Much less dominant in MATH"]
          - ["Specification-level", "24%", "10%", "NL→formal ambiguity higher in MATH"]
          - ["Tool limitation", "28%", "0%", "SymPy can't solve certain problem types"]
          - ["Computational error", "15%", "18%", "Similar across domains"]
    figures_description:
      - "Scatter plot: CoT accuracy vs SymPy accuracy per MATH category, showing near-diagonal clustering (error ratio ~1.8:1) vs FOLIO's extreme off-diagonal (9:1) — the asymmetry that makes diagnosis work in logic does not exist in math"
      - "Stacked bar: error source distribution across three benchmarks (FOLIO/ProofWriter/MATH), showing formalization-specific errors declining from 72% to 33% while specification-level and tool-limitation errors grow"
      - "Heatmap: false agreement rate by MATH difficulty sublevel and category, showing concentrated failure in geometry and combinatorics"
    analysis: >
      MATH 结果是 worst-case 的核心 evidence。0/5 MVP pass 意味着 cross-representation
      diagnosis 在数学域基本失效。关键 insight：诊断方法的有效性依赖于两种表征之间的 "asymmetric
      reliability"——在逻辑域，Z3 的完备性保证了 FOL 侧几乎总是对的，使分歧成为高质量的 error
      detector。数学域缺少这种 asymmetry：CoT 和 SymPy 都是 "fallible solvers"，分歧不再指向
      "哪边错了"而是 "两种方法对此题的适用性不同"。Tool limitation（28%）作为新 error type
      出现，这类错误不可通过 repair 修复（SymPy 本身不支持的问题类型）。
      在 reframed narrative 中，这构成了 "applicability condition" 的核心论据：
      cross-representation diagnosis requires asymmetric reliability between representations，
      而这在 formal logic 域自然成立（Z3 completeness）但在其他域不保证。

  - name: "Repair Mechanism Improvement"
    plan_id: "exp-005"
    description: "多轮 repair + 错误类型特定修复策略，尝试拉大 targeted vs blind 差距"
    expected_results:
      C4_round1_delta_pp_all_mode: 5.2
      C4_round2_delta_pp_all_mode: 2.6
      C4_round3_delta_pp_all_mode: 2.1
      C4_improved_prompt_delta_pp_all_mode: 3.0
      C4_best_config_delta_pp_all_mode: 3.0
      C4_best_config_delta_pp_excl_unknown: -1.5
      repair_success_rate_formalization_errors: 0.22
      repair_success_rate_specification_errors: 0.04
      multi_round_diminishing_returns: true
      error_type_specific_vs_generic_delta: 0.8
    result_rationale: >
      多轮 repair 和改进 prompt 均未能突破 C4 delta 瓶颈。原因分析：
      (1) 多轮 repair 呈显著递减收益——Round 1 的 5.2pp 到 Round 2 降至 2.6pp，Round 3 仅
      2.1pp。这是因为 Round 1 已修复了 "easy fixes"（简单的语法级 formalization errors），
      剩余的 errors 是 deep semantic misunderstandings（模型对 NL 含义的理解偏差），多轮
      regeneration 不改变模型的理解。
      (2) 改进 prompt（加入 error type 信息）的 delta 反而降至 3.0pp——更详细的 diagnosis
      信息有时误导 repair：当 error type classification 本身有 ~15% 错误率时，提供错误的
      error type 信息比不提供更差。
      (3) Excl-Unknown 从 0.0pp 恶化到 -1.5pp——多轮 repair 在 True/False 样本上引入了
      regression（过度修改导致原本正确的逻辑被破坏）。
      (4) 核心瓶颈：repair 只能修复 formalization-specific errors（22% 成功率），对
      specification-level errors 几乎无效（4%），而后者占 errors 的 ~30%。targeted repair
      的上限被 error type 分布锁定。
    tables:
      - table_id: "tab-exp005-1"
        caption: "Multi-Round Repair Results (FOLIO, N=96 disagreement pairs)"
        columns: ["Config", "Targeted Acc", "Blind Acc", "Δ (pp)", "Excl-Unk Δ (pp)"]
        rows:
          - ["Baseline (Round 1, original prompt)", "63.5%", "58.3%", "+5.2", "+0.0"]
          - ["Round 2 (re-repair failures)", "64.6%", "62.0%", "+2.6", "-0.5"]
          - ["Round 3 (re-repair failures)", "65.1%", "63.0%", "+2.1", "-1.0"]
          - ["Improved prompt (error-type-specific)", "62.5%", "59.5%", "+3.0", "-1.5"]
          - ["Best combo (Round 2 + improved)", "63.8%", "60.8%", "+3.0", "-1.5"]
      - table_id: "tab-exp005-2"
        caption: "Repair Success Rate by Error Type"
        columns: ["Error Type", "N (targeted)", "Repair Success%", "Blind Success%", "Δ"]
        rows:
          - ["Variable mapping error", "18", "33.3%", "22.2%", "+11.1pp"]
          - ["Scope/quantifier error", "12", "16.7%", "16.7%", "+0.0pp"]
          - ["Logic connective error", "15", "26.7%", "20.0%", "+6.7pp"]
          - ["Specification-level error", "9", "4.4%", "6.7%", "-2.2pp"]
          - ["Unknown GT (all errors)", "42", "28.6%", "19.0%", "+9.5pp"]
    figures_description:
      - "Line plot: C4 delta (pp) across repair rounds (1-3), showing monotonic decrease — diminishing returns curve with inflection at Round 1"
      - "Grouped bar chart: repair success rate by error type for targeted vs blind, showing targeted advantage concentrates on variable-mapping and logic-connective errors while specification errors show no benefit"
    analysis: >
      Repair improvement 实验确认了 C4 delta 的 structural ceiling。最佳配置仅 3.0pp
      All-mode（低于 MVP 的 5.2pp，因为 improved prompt 有时误导），Excl-Unknown 为负。
      这是 worst-case 的关键：即使投入 3 rounds repair + error-type-specific prompts，
      targeted repair 相比 blind 的优势依然 marginal。根本原因是 diagnosis 信息对 repair
      的 actionability 有限——知道 "Code 侧有 variable mapping error" 并不能帮助 LLM 在
      重新生成时避免同样的错误，因为错误来源于 LLM 对 NL 语义的理解而非生成随机性。
      在 reframed narrative 中，这支持 "diagnosis as analysis tool, not repair tool" 的定位。

  - name: "Unknown Sample Deep Analysis"
    plan_id: "exp-006"
    description: "分析 GT=Unknown 样本为何驱动 C4 delta，探索 specification-level vs formalization-specific 差异"
    expected_results:
      unknown_sample_count: 66
      unknown_disagree_rate: 0.47
      unknown_specification_error_rate: 0.08
      unknown_formalization_error_rate: 0.39
      true_false_specification_error_rate: 0.22
      true_false_formalization_error_rate: 0.14
      unknown_fol_code_error_ratio: "12:1"
      true_false_fol_code_error_ratio: "6:1"
      unknown_repair_delta_pp: 9.5
      true_false_repair_delta_pp: -1.7
    result_rationale: >
      Unknown 样本驱动 C4 delta 的原因在 worst-case 下被揭示为一个 confound 而非 feature：
      (1) Unknown 样本的 FOL:Code asymmetry 更极端（12:1 vs 6:1）——Z3 solver 对 "信息不足"
      的判定（返回 Unknown）几乎总是正确的，而 Python 代码极难正确实现 "三值逻辑"（True/False/Unknown），
      倾向于错误地返回 True 或 False。这不是 "diagnosis 发现了 formalization error" 而是
      "Code 表征在结构上不适合处理 Unknown 类别"。
      (2) True/False 样本的 specification error rate 更高（22% vs 8%），因为需要完整的
      逻辑推理链，任何 NL 歧义都传播为 specification error。Unknown 样本通常只需检测 "信息不足"，
      specification 更简单。
      (3) 这意味着 FOLIO 上的 C4 success 本质上是 "Z3 对 Unknown 判定的优越性" 的 side effect，
      而非 cross-representation diagnosis 的 general 能力。当移除 Unknown 样本后 C4 delta 消失
      就是这个 confound 的直接证据。
    tables:
      - table_id: "tab-exp006-1"
        caption: "Error Mode Distribution: Unknown vs True/False Samples"
        columns: ["Metric", "GT=Unknown (N=66)", "GT=True/False (N=126)", "Interpretation"]
        rows:
          - ["Disagree Rate", "47.0%", "35.7%", "Unknown samples produce more disagreement"]
          - ["Specification Error Rate", "8.1%", "22.2%", "True/False problems have more NL ambiguity"]
          - ["Formalization Error Rate", "39.4%", "14.3%", "Unknown triggers Code-side errors"]
          - ["FOL:Code Error Ratio", "12:1", "6:1", "Extreme asymmetry on Unknown"]
          - ["Code 'Unknown' output rate", "12.1%", "N/A", "Code rarely outputs Unknown correctly"]
          - ["Repair Δ (targeted vs blind)", "+9.5pp", "-1.7pp", "Entire C4 signal from Unknown"]
      - table_id: "tab-exp006-2"
        caption: "Code-side Error Patterns on Unknown Samples"
        columns: ["Code Output", "Count", "%", "Is Error?"]
        rows:
          - ["True (should be Unknown)", "18", "58.1%", "Yes — most common failure"]
          - ["False (should be Unknown)", "9", "29.0%", "Yes"]
          - ["Unknown (correct)", "3", "9.7%", "No"]
          - ["Runtime Error", "1", "3.2%", "Yes"]
    figures_description:
      - "Stacked bar: error type distribution split by GT label (Unknown / True / False), showing formalization errors dominate Unknown while specification errors dominate True/False"
      - "Decision tree visualization: why Unknown samples are 'easy' for diagnosis — Z3 returns Unknown → almost certainly correct → any Code disagreement is Code-side error → repair = regenerate Code"
    analysis: >
      这个分析在 worst-case scenario 中具有双刃剑效应。一方面，它解释了 C4 delta 的来源并揭示了
      一个重要的 confound：FOLIO 上的 repair success 主要来自 Unknown 样本中 Code 表征对三值逻辑
      的结构性缺陷，而非 diagnosis 的 general 能力。另一方面，在 reframed narrative 中，这恰好
      是 "When and Why" 的深度案例：精确刻画了 WHY diagnosis works（Z3 completeness +
      representation asymmetry）和 WHEN it fails（True/False samples where specification
      errors dominate）。这个 confound 的发现本身是 contribution——它警告后续研究者
      cross-representation diagnosis 的效果可能被特定 GT label 分布所夸大。

  - name: "Selection vs Repair Ablation"
    plan_id: "exp-007"
    description: "检测到分歧后，直接选择另一侧 vs 诊断引导修复的对比"
    expected_results:
      selection_accuracy_all_mode: 0.68
      repair_accuracy_all_mode: 0.635
      selection_vs_repair_delta_pp: 4.5
      selection_accuracy_excl_unknown: 0.61
      repair_accuracy_excl_unknown: 0.59
      selection_accuracy_when_localization_correct: 0.80
      selection_accuracy_when_localization_wrong: 0.31
      oracle_selection_accuracy: 0.88
    result_rationale: >
      Selection（直接选正确侧）在 All-mode 上以 4.5pp 优于 Repair（68% vs 63.5%），这对 repair
      contribution 是直接打击。原因：
      (1) 在 9:1 的 FOL:Code asymmetry 下，"永远选 FOL" 这个 naive 策略本身就有 ~90% 的
      accuracy on disagreement samples。Selection with localization（选 localization 判定的
      正确侧）达到 68%（受限于 localization 的 85% accuracy——当 localization 错误时 selection
      反而选了错误侧，降至 31%）。
      (2) Repair 的 63.5% 低于 selection 的 68%，因为 repair 引入了 regeneration noise——
      即使 diagnosis 正确指出了错误侧和错误类型，LLM 的重新生成不保证修复该错误，有时甚至引入新错误。
      (3) Oracle selection（假设 perfect localization）达到 88%，说明 localization accuracy
      是 selection 策略的主要瓶颈。这暗示 "提升 localization" 比 "提升 repair" 更有杠杆。
      在 worst-case 下，这意味着 repair 作为 downstream application 不仅 marginal 而且
      不如更简单的 selection baseline。
    tables:
      - table_id: "tab-exp007-1"
        caption: "Selection vs Repair Comparison (FOLIO disagreement samples)"
        columns: ["Strategy", "All-mode Acc", "Excl-Unk Acc", "Compute Cost (relative)"]
        rows:
          - ["Always-FOL baseline", "65.8%", "57.8%", "0x (no extra)"]
          - ["Selection (w/ localization)", "68.0%", "61.0%", "0x (no extra)"]
          - ["Repair (targeted, 1 round)", "63.5%", "59.3%", "1x (regeneration)"]
          - ["Repair (targeted, 3 rounds)", "65.1%", "57.6%", "3x"]
          - ["Oracle Selection", "88.0%", "82.0%", "0x (hypothetical)"]
          - ["Blind Repair (1 round)", "58.3%", "59.3%", "1x"]
      - table_id: "tab-exp007-2"
        caption: "Selection Accuracy Conditioned on Localization Correctness"
        columns: ["Localization", "N", "Selection Acc", "Repair Acc"]
        rows:
          - ["Correct (85.4%)", "35", "80.0%", "68.6%"]
          - ["Incorrect (14.6%)", "6", "31.3%", "50.0%"]
    figures_description:
      - "Bar chart with error bars: accuracy comparison across 5 strategies (always-FOL, selection, repair-1, repair-3, oracle-selection), showing selection > repair and oracle-selection sets the ceiling"
      - "Scatter: per-sample selection outcome vs repair outcome, showing weak correlation (r=0.32) — selection and repair succeed on different subsets"
    analysis: >
      Selection > Repair 的结果在 worst-case 中直接质疑了 repair 作为 downstream application
      的价值。一个更简单、零额外计算成本的策略（selection）beats 更复杂、需要额外 LLM call 的策略
      （repair），这在 reviewer 眼中是 fatal weakness for the repair narrative。然而在 reframed
      narrative 中，这反而支持 "diagnosis as analysis, not repair" 的定位：cross-representation
      disagreement 的价值在于 detection 和 localization，不在于 repair。Selection 的成功
      恰好证明 diagnosis 的上游价值（localization accuracy 直接决定 selection quality）。
      Oracle selection 88% 的上限暗示未来方向：提升 localization 精度是 highest-leverage
      improvement。

  - name: "Error Taxonomy Ablation"
    plan_id: "exp-008"
    description: "按错误类型分派修复策略 vs 固定策略的对比"
    expected_results:
      taxonomy_guided_repair_acc: 0.625
      fixed_strategy_repair_acc: 0.615
      taxonomy_vs_fixed_delta_pp: 1.0
      taxonomy_guided_by_error_type:
        variable_mapping: 0.333
        scope_quantifier: 0.167
        logic_connective: 0.267
      fixed_strategy_by_error_type:
        variable_mapping: 0.278
        scope_quantifier: 0.167
        logic_connective: 0.200
      taxonomy_misclassification_rate: 0.15
      taxonomy_misclassification_repair_success: 0.07
    result_rationale: >
      Taxonomy-guided repair 仅比 fixed strategy 高 1.0pp（62.5% vs 61.5%），在 worst-case
      下这个差异统计不显著（p=0.68, Fisher exact test）。原因：
      (1) Error taxonomy 的分类准确率约 85%，那 15% 的 misclassification 会导致错误的修复策略
      被应用，反而降低 repair 效果——misclassified samples 的 repair 成功率仅 7%（vs correctly
      classified 的 ~25%）。
      (2) 不同 error type 的最优修复策略差异不大——无论是 variable mapping error 还是 logic
      connective error，LLM 的 repair 本质上都是 "重新生成并希望这次不犯同样的错"。Error type
      信息对 repair prompt 的 marginal guidance 有限，因为 LLM 不能精确执行 "只修改变量映射
      而保持其他逻辑不变" 这样的指令。
      (3) Scope/quantifier errors 在两种策略下 repair 成功率相同（16.7%），说明这类 deep
      semantic errors 超出了 prompt-level repair 的能力边界。
    tables:
      - table_id: "tab-exp008-1"
        caption: "Taxonomy-Guided vs Fixed Strategy Repair (FOLIO)"
        columns: ["Strategy", "Overall Acc", "Variable Map", "Scope/Quant", "Logic Conn", "p-value"]
        rows:
          - ["Taxonomy-guided", "62.5%", "33.3%", "16.7%", "26.7%", ""]
          - ["Fixed (generic regen)", "61.5%", "27.8%", "16.7%", "20.0%", "0.68"]
          - ["Δ", "+1.0pp", "+5.5pp", "+0.0pp", "+6.7pp", "n.s."]
      - table_id: "tab-exp008-2"
        caption: "Impact of Taxonomy Misclassification on Repair"
        columns: ["Classification", "N", "Repair Success%", "Notes"]
        rows:
          - ["Correctly classified", "36", "25.0%", "Taxonomy info slightly helps"]
          - ["Misclassified", "5", "7.1%", "Wrong repair strategy applied"]
          - ["All targeted", "41", "22.0%", "Weighted average"]
    figures_description:
      - "Grouped bar: repair success rate per error type, taxonomy-guided vs fixed, with 95% CI error bars overlapping on all types"
      - "Sankey diagram: error type classification → repair strategy → outcome, showing misclassification paths leading to failures"
    analysis: >
      Taxonomy 的规定性价值在 worst-case 下几乎不存在。1.0pp 的差异在 N=41 的样本量下统计不显著，
      无法 claim taxonomy-guided repair is better than generic repair。这对论文的 error
      taxonomy contribution 有影响——如果 taxonomy 只有 descriptive value（帮助理解 errors）
      而无 prescriptive value（指导 repair），reviewer 可能质疑 taxonomy 的实用性。
      在 reframed narrative 中，taxonomy 的价值重新定位为 analytical tool：它帮助解释 WHY
      某些 errors 可修复而某些不可修复（scope errors 的 0% Δ），贡献于 boundary characterization
      而非 repair improvement。

  - name: "Statistical Significance Testing"
    plan_id: "exp-009"
    description: "对所有 benchmark 做 bootstrap 95% CI + Fisher exact test"
    expected_results:
      folio_C1_bootstrap_95CI: [0.333, 0.461]
      folio_C2_bootstrap_95CI: [0.782, 0.934]
      folio_C4_bootstrap_95CI_all_mode: [-0.8, 11.2]
      folio_C4_fisher_p_all_mode: 0.078
      folio_C4_bootstrap_95CI_excl_unknown: [-7.5, 7.5]
      folio_C4_fisher_p_excl_unknown: 1.0
      folio_C5_bootstrap_95CI: [0.735, 0.939]
      proofwriter_C1_bootstrap_95CI: [0.128, 0.218]
      proofwriter_C2_bootstrap_95CI: [0.472, 0.771]
      proofwriter_C4_fisher_p: 0.31
      math_C1_bootstrap_95CI: [0.093, 0.194]
      math_C2_bootstrap_95CI: [0.385, 0.762]
      math_C4_fisher_p: 0.82
      benchmarks_with_C4_significant: 0
      benchmarks_with_C1C2_significant: 1
    result_rationale: >
      统计显著性结果在 worst-case 下呈现清晰的 "FOLIO-only" 格局：
      (1) FOLIO 的 C1（39.6%）和 C2（86.8%）CI 不跨零，统计显著。但 C4 All-mode（+5.2pp）
      的 Fisher exact p=0.078，未达 0.05 阈值——这是因为 C4 的 base rate 比较（targeted vs blind）
      在 N=96 paired samples 上 power 不足。Bootstrap CI [-0.8, 11.2] 跨零。Excl-Unknown
      的 C4 delta=0.0pp 显然不显著。
      (2) ProofWriter 的 C2 CI [0.472, 0.771] 跨 65% threshold——无法 claim "high precision"。
      C4 p=0.31，far from significant。
      (3) MATH 更差：C2 CI [0.385, 0.762] 极宽（N=24 disagreement samples），C4 p=0.82。
      (4) 没有任何 benchmark 的 C4 达到统计显著性。只有 FOLIO 的 C1 和 C2 显著。
      这意味着论文能统计支撑的 claim 仅限于 "FOLIO 上 disagree rate substantial 且 diagnostically
      precise"，repair 和跨域泛化均无统计支撑。
    tables:
      - table_id: "tab-exp009-1"
        caption: "Statistical Significance Summary Across Benchmarks"
        columns: ["Metric", "FOLIO", "ProofWriter", "MATH"]
        rows:
          - ["C1 Disagree Rate", "39.6% [33.3, 46.1]**", "17.0% [12.8, 21.8]*", "14.0% [9.3, 19.4]*"]
          - ["C2 Precision", "86.8% [78.2, 93.4]**", "63.2% [47.2, 77.1]", "58.3% [38.5, 76.2]"]
          - ["C4 Δ All-mode", "+5.2pp [-0.8, 11.2]", "+1.8pp [-4.2, 7.8]", "-0.5pp [-9.1, 8.1]"]
          - ["C4 Fisher p (All)", "0.078", "0.31", "0.82"]
          - ["C4 Δ Excl-Unk", "+0.0pp [-7.5, 7.5]", "-2.1pp [-9.8, 5.6]", "-3.2pp [-14.1, 7.7]"]
          - ["C5 Localization", "85.4% [73.5, 93.9]**", "72.0% [58.1, 83.5]*", "63.0% [44.7, 79.0]"]
      - table_id: "tab-exp009-2"
        caption: "Statistical Power Analysis"
        columns: ["Test", "N (effective)", "Observed Effect", "Power at α=0.05", "N needed for 80% power"]
        rows:
          - ["FOLIO C4 Fisher", "96 pairs", "+5.2pp", "0.42", "~280"]
          - ["ProofWriter C4 Fisher", "~120 pairs", "+1.8pp", "0.12", "~2400"]
          - ["MATH C4 Fisher", "~86 pairs", "-0.5pp", "0.05", "N/A (null effect)"]
    figures_description:
      - "Forest plot: C4 delta with 95% CI across three benchmarks, showing all CIs crossing zero — no benchmark achieves statistical significance for repair"
      - "Forest plot: C2 precision with 95% CI, showing FOLIO clearly above 65% threshold while ProofWriter and MATH CIs cross it"
      - "Power curve: statistical power vs sample size for C4 Fisher test at observed effect sizes, showing FOLIO needs ~280 samples for 80% power"
    analysis: >
      统计检验结果是 worst-case 的 "nail in the coffin" for the general framework narrative。
      C4（repair）在任何 benchmark 上都不显著，C2（precision）仅在 FOLIO 上显著。
      这直接支持核心假设 "仅 FOLIO 单 benchmark 数据可靠"。
      在 reframed narrative 中，这驱动两个调整：(1) 诚实报告 all CIs，不 overclaim；
      (2) 将 FOLIO 的 power analysis 作为 future work 的 guide（需要 ~280 samples 才能
      confirm C4 effect），承认当前 sample size 是 limitation。
      注意 FOLIO C4 的 p=0.078 是 borderline——在 reframed 的 "case study" narrative 下，
      可以 report 为 "marginally significant trend" 而非 hard claim，这在 EMNLP 可接受。

  - name: "Qwen3-8B Ablation"
    plan_id: "exp-010"
    description: "低能力模型上的诊断率和分歧率测试"
    expected_results:
      C1_disagree_rate: 0.52
      C2_diagnostic_precision: 0.61
      C3_error_types: 3
      C4_targeted_vs_blind_delta_pp: 1.5
      C5_localization_accuracy: 0.68
      fol_code_error_ratio: "4:1"
      fol_crash_rate: 0.12
      code_crash_rate: 0.08
      both_wrong_rate: 0.28
    result_rationale: >
      Qwen3-8B 的 disagree rate 上升到 52%（vs 32B 的 39.6%），表面上看更多分歧。但 diagnostic
      precision 降至 61%——更多分歧是 "noise" 而非 "signal"。原因：
      (1) 8B 模型在两种表征上都犯更多错误，both-wrong rate 从 ~10% 飙升到 28%。大量 disagreements
      来自 "两侧都错但错误方式不同"，这类分歧无 diagnostic value。
      (2) FOL:Code asymmetry 减弱（4:1 vs 9:1）——8B 的 FOL 生成能力退化明显（Z3 crash rate
      12%，因为生成的 FOL 语法更常出错），削弱了 "FOL 作为 reliable reference" 的前提。
      (3) C4 delta 仅 1.5pp——更多错误不等于更多可修复的错误。低能力模型的 errors 更 fundamental
      （理解错误而非形式化错误），repair 更难。
      (4) C5 localization 降至 68%——当 both-wrong rate 高时，"哪侧错了" 的判定本身就更模糊。
    tables:
      - table_id: "tab-exp010-1"
        caption: "Model Capability Ablation: Qwen3-8B vs Qwen3-32B (FOLIO)"
        columns: ["Metric", "Qwen3-8B", "Qwen3-32B", "Δ"]
        rows:
          - ["C1 Disagree Rate", "52.0%", "39.6%", "+12.4pp"]
          - ["C2 Precision", "61.0%", "86.8%", "-25.8pp"]
          - ["C4 Δ All-mode", "+1.5pp", "+5.2pp", "-3.7pp"]
          - ["C5 Localization", "68.0%", "85.4%", "-17.4pp"]
          - ["FOL:Code Error Ratio", "4:1", "9:1", "Asymmetry reduced"]
          - ["Both-Wrong Rate", "28.0%", "~10%", "+18pp"]
          - ["FOL Crash Rate", "12.0%", "~2%", "+10pp"]
    figures_description:
      - "Scatter: model capability (8B vs 32B) on x-axis, disagree rate vs diagnostic precision on y-axis, showing inverse relationship — more disagreement but less informative"
    analysis: >
      8B 结果揭示了 cross-representation diagnosis 的另一个 applicability condition：
      模型能力需要足够高，使得至少一种表征是 reliable 的。当模型能力不足时，both-wrong rate
      上升，分歧变成噪声。这支持 "asymmetric reliability" 作为 necessary condition 的论点。
      在 reframed narrative 中，这与 MATH 的 failure mode 形成呼应——无论是因为 domain
      （MATH 中 CoT 和 SymPy 都 fallible）还是因为 model capability（8B 中 FOL 也不可靠），
      一旦 asymmetric reliability 被打破，diagnosis 就失效。

  - name: "GPQA Diamond Extension"
    plan_id: "exp-011"
    description: "科学知识推理领域，CoT vs Python 验证代码"
    expected_results:
      N_samples: 150
      C1_disagree_rate: 0.11
      C2_diagnostic_precision: 0.56
      C4_delta_pp: -1.8
      C5_localization_accuracy: 0.60
      cot_code_error_ratio: "1.3:1"
      correlated_failure_rate: 0.38
      code_not_applicable_rate: 0.35
      mvp_pass_count: "0/5"
    result_rationale: >
      GPQA Diamond 是 worst-case 的极端表现。disagree rate 仅 11%，precision 56%（接近随机）。
      核心原因：科学推理（物理/化学/生物）中 Python 代码的角色与逻辑域完全不同——大部分 GPQA 问题
      需要 domain knowledge 和 conceptual reasoning，Python 只能验证计算步骤但无法验证
      conceptual correctness。35% 的问题 Code 表征 "不适用"（无法有意义地用代码验证）。
      CoT:Code error ratio 几乎对称（1.3:1），完全丧失了逻辑域的 asymmetric reliability。
      Correlated failure rate 高达 38%——模型在科学知识上的盲点在两种表征上都表现出来。
      C4 为负——targeted repair 不如 blind，因为 "diagnosis" 信息在科学域几乎没有 actionability。
    tables:
      - table_id: "tab-exp011-1"
        caption: "GPQA Diamond Results (N=150, Qwen3-32B)"
        columns: ["Metric", "GPQA", "MATH", "FOLIO"]
        rows:
          - ["C1 Disagree Rate", "11.0%", "14.0%", "39.6%"]
          - ["C2 Precision", "56.0%", "58.3%", "86.8%"]
          - ["C4 Δ", "-1.8pp", "-0.5pp", "+5.2pp"]
          - ["C5 Localization", "60.0%", "63.0%", "85.4%"]
          - ["Error Ratio", "1.3:1", "1.8:1", "9:1"]
          - ["Correlated Failure%", "38.0%", "31.0%", "18.2%"]
          - ["Code N/A Rate", "35.0%", "8.0%", "0%"]
    figures_description:
      - "Gradient heatmap: 4 benchmarks (FOLIO → ProofWriter → MATH → GPQA) showing monotonic degradation of all metrics, establishing the applicability spectrum"
    analysis: >
      GPQA 完成了 "applicability spectrum" 的构建：FOLIO（强信号）→ ProofWriter（弱信号）→
      MATH（噪声）→ GPQA（失效）。关键维度是 representation asymmetry 和 formalization-vs-knowledge
      error ratio。GPQA 的 35% code-not-applicable rate 揭示了一个 fundamental limitation：
      cross-representation diagnosis 要求两种表征都能 meaningfully encode the reasoning，
      而科学推理中 Code 常常只能部分覆盖推理过程。
      这在 reframed narrative 中作为 applicability conditions 的最外层边界。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40091779-888b-44da-afe5-a1ac50798c14",
  "isSidechain": false,
  "requestId": "req_011Cb3s14WfEFdrXGedfmLty",
  "type": "assistant",
  "uuid": "818c37a9-8161-4e60-805c-747e4c4c9c3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "ecc5382a-3f63-45a1-993b-0dee29c58083",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016WyPXrWdkeQTcdYwJkgiCV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11059,
      "cache_read_input_tokens": 11841,
      "output_tokens": 15365,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11059,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 15365,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11059,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11059
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：诊断信号在 FOLIO 外不稳健——disagree rate 过低或 precision 大幅下降，repair 无正向效果，核心 framing 需重构 核心假设：['ProofWriter/MATH 上 C1 disagree rate <20% 或 C2 diagnostic precision <…",
  "leafUuid": "818c37a9-8161-4e60-805c-747e4c4c9c3e",
  "sessionId": "ecc5382a-3f63-45a1-993b-0dee29c58083"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterize boundary conditions for cross-representation diagnosis",
  "sessionId": "ecc5382a-3f63-45a1-993b-0dee29c58083"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：诊断信号在 FOLIO 外不稳健——disagree rate 过低或 precision 大幅下降，repair 无正向效果，核心 framing 需重构 核心假设：['ProofWriter/MATH 上 C1 disagree rate <20% 或 C2 diagnostic precision <…",
  "leafUuid": "818c37a9-8161-4e60-805c-747e4c4c9c3e",
  "sessionId": "ecc5382a-3f63-45a1-993b-0dee29c58083"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterize boundary conditions for cross-representation diagnosis",
  "sessionId": "ecc5382a-3f63-45a1-993b-0dee29c58083"
}
```

---
