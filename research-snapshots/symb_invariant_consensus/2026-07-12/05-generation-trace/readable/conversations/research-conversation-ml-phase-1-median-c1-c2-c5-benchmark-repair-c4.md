# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：诊断信号 (C1/C2/C5) 跨 benchmark 基本成立但有波动，repair (C4) 经改进仍边际，需将分析权重进一步向诊断倾斜 核心假

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/b514574f-8acf-405c-a805-45a06a49658a.jsonl`
- **Structured JSON:** [`3c55262e32e26e86941a.json`](../../sessions/3c/3c55262e32e26e86941a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T06:09:25.743Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T06:09:25.743Z",
  "sessionId": "b514574f-8acf-405c-a805-45a06a49658a",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：诊断信号 (C1/C2/C5) 跨 benchmark 基本成立但有波动，repair (C4) 经改进仍边际，需将分析权重进一步向诊断倾斜\n核心假设：['C1 disagree rate 在 ProofWriter 保持 25%+，MATH 可能偏低 (20-30%) 因数学问题形式化模式不同', 'C2 diagnostic precision 跨 benchmark 在 70-85% 区间，个别 benchmark 低于 80%', 'exp-005 repair 改进有限，C4 delta All-mode 4-7pp，Excl-Unknown 仍 ≤2pp', 'exp-002 跨模型有改善但 correlated failures 仍显著 (false agreement 仅降 2-4pp)', 'MATH 域表现弱于逻辑域 (diagnostic precision 下降 5-10pp)', '部分指标 CI 较宽或 p 值边缘 (0.01<p<0.05)']\n关键指标范围：{'C1_disagree_rate_cross_bench': [0.2, 0.4], 'C2_diagnostic_precision_cross_bench': [0.7, 0.85], 'C4_targeted_vs_blind_delta_pp_all_mode': [4.0, 7.0], 'C4_targeted_vs_blind_delta_pp_excl_unknown': [-1.0, 2.0], 'C5_localization_accuracy_cross_bench': [0.75, 0.85], 'cross_model_false_agreement_reduction_pp': [2.0, 4.0], 'MATH_fol_code_error_ratio': [3.0, 7.0], 'benchmarks_with_5of5_pass': [1, 2]}\n叙事方向：调整 claims 强度分配：Claim 1+2 (诊断信号+定位分类) 升格为唯一核心贡献，Claim 3 从 'repair framework' 降级为 'boundary characterization of when diagnosis translates to repair gains'。论文叙事重心从 'diagnosis + repair' 转向 'systematic empirical analysis of cross-representation disagreement patterns'，repair 仅作为一个 application case study。需补充 failure mode 分析（为什么 correlated failures 限制 repair）作为 negative-but-informative result。MATH 域若弱，诚实报告并讨论 domain-dependent effectiveness。仍可投 EMNLP Main，但需准备 Findings 作为 fallback。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: cross_representation_disagreement_diagno\nfocus: C4 repair improvement is the main weakness (0.2pp margin). Key questions: (1) Is the dual-track framing (systematic analysis + lightweight repair) strong enough for EMNLP Main? (2) Does the boundary characterization (Claim 3) compensate for weak repair results? (3) Is 3 benchmarks (FOLIO + ProofWriter + MATH) sufficient or do we need more? (4) The 9:1 FOL:Code asymmetry — strength or weakness for the story?\n\n## paper_framing.md\n\n# Paper Framing — cross_representation_disagreement_diagno\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026 (10 days)\n- Secondary: AAAI 2027 (abstract July 25, full August 1) — extended version with full benchmark coverage\n\n## Core Insight\nCross-representation disagreement (FOL/Z3 vs Python Code) produced by the same LLM for the same reasoning problem is an underexploited diagnostic signal that detects formalization errors, enables error localization and classification, and guides targeted repair — going beyond existing approaches that only filter or verify within a single representation.\n\n## Core Claims (3 条)\n\n### Claim 1: Disagreement as High-Precision Diagnostic Signal\nWhen the same LLM formalizes a reasoning problem into two distinct representations (FOL/Z3 and executable Python), disagreements occur at a substantial rate (~40%) and are diagnostically informative with high precision (~87%). This cross-representation signal detects formalization-specific errors invisible to within-representation verification.\n\n**MVP evidence**: C1=39.6% disagree rate, C2=86.8% diagnostic rate on FOLIO (204 samples, Qwen3-32B).\n\n### Claim 2: Accurate Error Localization and Classification\nDisagreement patterns enable automatic error localization (identifying which representation contains the error) with high accuracy (~85%), and error type classification into a structured taxonomy (≥3 distinct types). The 9:1 asymmetry (FOL almost always correct, Code almost always erroneous) itself reveals fundamental differences in how LLMs handle formal logic vs. imperative code generation.\n\n**MVP evidence**: C5=85.4% localization accuracy, C3=3 error types. FOL:Code error ratio 9:1.\n\n### Claim 3: Characterizing the Boundary of Diagnosis-Guided Repair\nWe systematically characterize when cross-representation diagnosis enables effective targeted repair vs. when correlated failures limit repair gains. Targeted repair shows modest improvement over blind regeneration in All-mode (+5.2pp), but the advantage concentrates on specific sample subsets (GT=Unknown). This boundary characterization — distinguishing formalization-specific errors (catchable) from specification-level errors (producing false agreement) — is itself a contribution to understanding neurosymbolic failure modes.\n\n**MVP evidence**: C4 All-mode +5.2pp, Excl-Unknown +0.0pp. Unknown samples drive the repair delta.\n\n## Story Spine\n\n- **Problem**: Neurosymbolic reasoning pipelines suffer from formalization errors as their dominant failure mode. The LLM's translation from natural language to formal representation introduces subtle corruptions. Current approaches either select one representation (HybridMind, Adaptive Selection), verify within one representation (VeriCoT, VERGE, Roundtrip Verification), or filter disagreeing solutions without diagnosis (Liang et al. 2024, Prove 2024). The gap: nobody uses cross-representation disagreement patterns for error CATEGORIZATION and TARGETED REPAIR.\n\n- **Existing approaches & gaps**: Liang et al. (2024) proved CoT-PoT disagreement is informative for filtering but stopped at discarding disagreements — no error categorization, no repair. Roundtrip Verification (2026) showed diagnosis-guided repair works within a single representation on a narrow domain (150 traffic rules). No method exploits cross-representation disagreement as a diagnostic signal enabling categorized diagnosis and targeted repair.\n\n- **Our framing (dual-track)**: We present (1) the first systematic empirical analysis of cross-representation disagreement patterns in neurosymbolic reasoning — characterizing disagreement rates, error types, localization accuracy, and failure mode boundaries across domains and models; and (2) a lightweight diagnosis-guided repair framework that operates at inference time without model modification. The analysis is the primary contribution; the repair framework demonstrates downstream utility.\n\n- **Headline result template**: \"On [benchmarks], cross-representation disagreement detects [X]% of samples as potentially erroneous with [Y]% diagnostic precision and [Z]% error localization accuracy. We characterize a fundamental asymmetry: [logic representation] exhibits [N]x lower formalization error rate than [code representation], revealing systematic differences in how LLMs handle formal logic vs. imperative code generation.\"\n\n## Venue Fit\n\n- **EMNLP fit (strong)**: NLP + symbolic reasoning is a core track. Dual-track framing (systematic analysis + method) aligns with EMNLP's tradition of accepting empirical analyses. The correlated failure / boundary characterization angle fits EMNLP's emphasis on rigorous evaluation.\n- **Risk**: modest repair improvement → mitigate by framing analysis as primary contribution, repair as secondary.\n- **Risk**: single model+dataset insufficient → extend to ≥2 models and ≥3 benchmarks in research phase.\n\n## Anticipated Reviewer Concerns & Responses\n\n| # | Concern | Response Strategy | Required Experiment |\n|---|---------|-------------------|---------------------|\n| R1 | Single model/dataset — generalization? | Cross-model ablation + multi-benchmark | exp-002, exp-003, exp-004 |\n| R2 | C4 repair improvement marginal | Honest framing + boundary characterization as contribution | exp-005, exp-006 |\n| R3 | Why repair, not just select correct side? | Selection vs repair ablation | exp-007 |\n| R4 | Error taxonomy rule-based, not learned | Deliberate choice for interpretability; taxonomy-guided vs fixed strategy ablation | exp-008 |\n| R5 | FOL 9:1 asymmetry — just FOL-as-verifier? | Test on math domain where asymmetry may differ | exp-004 |\n| R6 | Statistical significance? | Bootstrap CI + Fisher exact test on all metrics | exp-009 |\n| R7 | Correlated failures (Denisov-Blanch 2026) | Explicit quantification + cross-model ablation reduces correlation | exp-002, exp-006 |\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'FOLIO 完整分析（MVP 数据深度挖掘）: 基于 204 样本 MVP 数据，完成统计显著性检验、错误类型详细分类、Unknown\n    样本子集分析、repair 前后对比。不需要新实验运行，纯分析。'\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: mvp_pipeline_004\n  status: ANALYZING\n  conclusion: success\n  metrics:\n    progress: 204/204 (deduped from 211)\n    deduped: true\n    dedup_original:\n      all_mode:\n        C1_disagree_rate: 39.6% (76/192)\n        C2_diagnostic_rate: 86.8% (66/76)\n        C3_error_types: 3 types\n        C4_targeted_vs_blind: +6.2pp (T:60/96 B:54/96)\n        C5_localization: 85.4% (35/41)\n        mvp_pass: 5/5 PASS\n      excl_unknown:\n        C1_disagree_rate: 35.7% (45/126)\n        C2_diagnostic_rate: 84.4% (38/45)\n        C3_error_types: 2 types\n        C4_targeted_vs_blind: -1.7pp (T:34/59 B:35/59)\n        C5_localization: 89.3% (25/28)\n        mvp_pass: 4/5 (C4 FAIL)\n    repair_fixed:\n      all_mode:\n        C1_disagree_rate: 39.6% (76/192)\n        C2_diagnostic_rate: 86.8% (66/76)\n        C3_error_types: 3 types\n        C4_targeted_vs_blind: +5.2pp (T:61/96 B:56/96)\n        C5_localization: 85.4% (35/41)\n        mvp_pass: 5/5 PASS\n      excl_unknown:\n        C1_disagree_rate: 35.7% (45/126)\n        C2_diagnostic_rate: 84.4% (38/45)\n        C3_error_types: 2 types\n        C4_targeted_vs_blind: +0.0pp (T:38/59 B:38/59)\n        C5_localization: 89.3% (25/28)\n        mvp_pass: 4/5 (C4 FAIL)\n    final_verdict: All-mode 5/5 PASS (both original and repair)\n- id: exp-002\n  claim:\n  - 1\n  - 2\n  description: '跨模型消融（FOLIO）: DeepSeek V4 Pro 生成一种表征 + Qwen3-32B 生成另一种，测试模型多样性是否降低\n    correlated failures、提升诊断覆盖率。FOLIO 204 样本。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  api_cost_estimate: $15-25 (DeepSeek V4 Pro promotional pricing)\n  status: planned\n- id: exp-003\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'ProofWriter 扩展: 在 ProofWriter 数据集上运行完整 pipeline（双表征+诊断+repair），验证方法在第二个逻辑推理\n    benchmark 上的泛化性。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  status: planned\n- id: exp-004\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'MATH Level 5 扩展: 在 MATH 难题子集上运行 pipeline（CoT vs SymPy/Python 双表征），测试跨领域泛化性。数学领域的\n    FOL:Code 不对称性可能不同。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  status: planned\n- id: exp-005\n  claim: 3\n  description: 'Repair 机制改进: 多轮 repair（max 3 rounds）、改进 repair prompt（加入错误类型特定的修复策略）、对比\n    repair 前后的 C4 delta。目标：拉大 targeted vs blind 差距。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  status: planned\n- id: exp-006\n  claim: 3\n  description: 'Unknown 样本深度分析: 为什么 GT=Unknown 样本驱动 C4 delta？分析 Unknown 样本的错误模式分布，是否存在\n    specification-level vs formalization-specific 的系统性差异。'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n- id: exp-007\n  claim: 3\n  description: 'Selection vs Repair 消融: 当检测到分歧且定位了错误侧后，直接选择另一侧答案（selection）vs 诊断引导修复（repair）的对比。回应\n    Reviewer Concern R3。'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  claim: 2\n  description: 'Error Taxonomy 消融: 按错误类型分派修复策略 vs 固定策略（统一重生成），验证 taxonomy 的规定性价值。'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-005\n  status: planned\n- id: exp-009\n  claim:\n  - 1\n  - 2\n  - 3\n  description: '统计显著性全面检验: 对所有 benchmark 的 C1-C5 指标做 bootstrap 95% CI + Fisher exact\n    test / McNemar test，确保所有 claim 有统计支撑。'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-003\n  - exp-004\n  status: planned\n- id: exp-010\n  claim:\n  - 1\n  - 2\n  description: 'Qwen3-8B 消融: 低能力模型上的诊断率和分歧率是否变化？测试方法对模型能力的鲁棒性。'\n  priority: P2\n  gpu_budget_hours: 4\n  deps: []\n  status: planned\n- id: exp-011\n  claim:\n  - 1\n  - 2\n  description: 'GPQA Diamond 扩展: 科学知识推理领域，CoT vs Python 验证代码。'\n  priority: P2\n  gpu_budget_hours: 6\n  deps:\n  - exp-004\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_baseline_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.74\n    correct: 37\n    total: 50\n    gate: PASS_FOLIO\n- exp_id: mvp_pipeline_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    disagree_rate: 0.04\n    diagnostic_rate: 1\n    error_types: 4\n    targeted_repair: 0.1875\n    blind_repair: 0.4688\n    delta_pp: -28.12\n    localization: 0.4186\n    fol_accuracy: 0.14\n    code_accuracy: 0.52\n    C1: false\n    C2: true\n    C3: true\n    C4: false\n    C5: false\n- exp_id: mvp_pipeline_002\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    fol_crash_rate_v2: 0.1\n    code_crash_rate_v2: 0.4\n    fol_crash_rate_v3: 0.8\n    code_crash_rate_v3: 0\n    fol_accuracy_v3: 0.2\n    code_accuracy_v3: 0.6\n    oracle_accuracy_v3: 0.6\n    disagree_rate_v3: 0\n    effective_disagree_rate_v3: 0\n    diagnostic_rate_v3: null\n    targeted_rate_v3: 0.5\n    blind_rate_v3: 0.625\n    delta_pp_v3: -12.5\n    localization_accuracy_v3: 0.5\n    error_types_v3: 3\n    C1_v3: false\n    C2_v3: false\n    C3_v3: true\n    C4_v3: false\n    C5_v3: false\n    avg_time_per_sample_s_v3: 218.5\n    total_api_calls_v3: 48\n    input_tokens_v3: 50558\n    output_tokens_v3: 139706\n    samples_v3: 10\n    v3_changes: enable_thinking=False for Code generation, _strip_thinking unclosed\n      tag handling\n- exp_id: mvp_pipeline_003\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_003b\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_004\n  name: ''\n  status: ANALYZING\n  conclusion: success\n  metrics:\n    progress: 204/204 (deduped from 211)\n    deduped: true\n    dedup_original:\n      all_mode:\n        C1_disagree_rate: 39.6% (76/192)\n        C2_diagnostic_rate: 86.8% (66/76)\n        C3_error_types: 3 types\n        C4_targeted_vs_blind: +6.2pp (T:60/96 B:54/96)\n        C5_localization: 85.4% (35/41)\n        mvp_pass: 5/5 PASS\n      excl_unknown:\n        C1_disagree_rate: 35.7% (45/126)\n        C2_diagnostic_rate: 84.4% (38/45)\n        C3_error_types: 2 types\n        C4_targeted_vs_blind: -1.7pp (T:34/59 B:35/59)\n        C5_localization: 89.3% (25/28)\n        mvp_pass: 4/5 (C4 FAIL)\n    repair_fixed:\n      all_mode:\n        C1_disagree_rate: 39.6% (76/192)\n        C2_diagnostic_rate: 86.8% (66/76)\n        C3_error_types: 3 types\n        C4_targeted_vs_blind: +5.2pp (T:61/96 B:56/96)\n        C5_localization: 85.4% (35/41)\n        mvp_pass: 5/5 PASS\n      excl_unknown:\n        C1_disagree_rate: 35.7% (45/126)\n        C2_diagnostic_rate: 84.4% (38/45)\n        C3_error_types: 2 types\n        C4_targeted_vs_blind: +0.0pp (T:38/59 B:38/59)\n        C5_localization: 89.3% (25/28)\n        mvp_pass: 4/5 (C4 FAIL)\n    final_verdict: All-mode 5/5 PASS (both original and repair)\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-15T06:09:25.748Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T06:09:25.748Z",
  "sessionId": "b514574f-8acf-405c-a805-45a06a49658a"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-15T06:09:25.788Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：诊断信号 (C1/C2/C5) 跨 benchmark 基本成立但有波动，repair (C4) 经改进仍边际，需将分析权重进一步向诊断倾斜
核心假设：['C1 disagree rate 在 ProofWriter 保持 25%+，MATH 可能偏低 (20-30%) 因数学问题形式化模式不同', 'C2 diagnostic precision 跨 benchmark 在 70-85% 区间，个别 benchmark 低于 80%', 'exp-005 repair 改进有限，C4 delta All-mode 4-7pp，Excl-Unknown 仍 ≤2pp', 'exp-002 跨模型有改善但 correlated failures 仍显著 (false agreement 仅降 2-4pp)', 'MATH 域表现弱于逻辑域 (diagnostic precision 下降 5-10pp)', '部分指标 CI 较宽或 p 值边缘 (0.01<p<0.05)']
关键指标范围：{'C1_disagree_rate_cross_bench': [0.2, 0.4], 'C2_diagnostic_precision_cross_bench': [0.7, 0.85], 'C4_targeted_vs_blind_delta_pp_all_mode': [4.0, 7.0], 'C4_targeted_vs_blind_delta_pp_excl_unknown': [-1.0, 2.0], 'C5_localization_accuracy_cross_bench': [0.75, 0.85], 'cross_model_false_agreement_reduction_pp': [2.0, 4.0], 'MATH_fol_code_error_ratio': [3.0, 7.0], 'benchmarks_with_5of5_pass': [1, 2]}
叙事方向：调整 claims 强度分配：Claim 1+2 (诊断信号+定位分类) 升格为唯一核心贡献，Claim 3 从 'repair framework' 降级为 'boundary characterization of when diagnosis translates to repair gains'。论文叙事重心从 'diagnosis + repair' 转向 'systematic empirical analysis of cross-representation disagreement patterns'，repair 仅作为一个 application case study。需补充 failure mode 分析（为什么 correlated failures 限制 repair）作为 negative-but-informative result。MATH 域若弱，诚实报告并讨论 domain-dependent effectiveness。仍可投 EMNLP Main，但需准备 Findings 作为 fallback。

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
tier: median
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
  "promptId": "b5c99332-5b6c-47f4-91b5-800f6919595b",
  "type": "user",
  "uuid": "63047589-af13-43e9-804e-7f619f2ace97",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "b514574f-8acf-405c-a805-45a06a49658a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T06:09:25.787Z_

```json
{
  "parentUuid": "63047589-af13-43e9-804e-7f619f2ace97",
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
  "uuid": "0f70527a-1be0-4fe7-a627-d56c0aa350cc",
  "timestamp": "2026-05-15T06:09:25.787Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "b514574f-8acf-405c-a805-45a06a49658a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T06:09:25.787Z_

```json
{
  "parentUuid": "0f70527a-1be0-4fe7-a627-d56c0aa350cc",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "29ffbdfe-7b3b-4d55-b049-35993ed93346",
  "timestamp": "2026-05-15T06:09:25.787Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "b514574f-8acf-405c-a805-45a06a49658a",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：诊断信号 (C1/C2/C5) 跨 benchmark 基本成立但有波动，repair (C4) 经改进仍边际，需将分析权重进一步向诊断倾斜 核心假设：['C1 disagree rate 在 ProofWriter 保持 25%+，MATH 可能偏低 (20-30%) 因数学问题形式化模式不同', 'C…",
  "leafUuid": "29ffbdfe-7b3b-4d55-b049-35993ed93346",
  "sessionId": "b514574f-8acf-405c-a805-45a06a49658a"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Detailed median tier experiment predictions with rationales",
  "sessionId": "b514574f-8acf-405c-a805-45a06a49658a"
}
```

---

### Assistant

_source line 8 · 2026-05-15T06:09:47.730Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for all planned experiments in the experiment plan, under the "median" tier definition they've provided. Each prediction needs a `result_rationale` explaining why this tier would produce these specific results.

Let me carefully go through each planned experiment and generate predictions consistent with the median tier definition:

**Median tier key characteristics:**
- Diagnostic signals (C1/C2/C5) mostly hold across benchmarks but with variance
- Repair (C4) still marginal even after improvement
- C1 disagree rate: 20-40% cross-bench


- C2 diagnostic precision: 70-85% cross-bench
- C4 delta All-mode: 4-7pp, Excl-Unknown: -1 to 2pp
- C5 localization accuracy: 75-85% cross-bench
- Cross-model false agreement reduction: 2-4pp
- MATH FOL:Code error ratio: 3-7 (less asymmetric than logic domain)
- Benchmarks with 5/5 pass: 1-2 (out of 3)
- MATH domain weaker than logic domain
- Some CIs wide, some p-values marginal

Now I'm working through each experiment systematically, starting with exp-001 and generating specific predicted results that align with these median tier parameters. done (ANALYZING status), data exists. I should still include it with actual results.

**exp-002**: Cross-model ablation on FOLIO with DeepSeek V4 Pro + Qwen3-32B shows modest reductions in correlated failures, with false agreement dropping 2-4 percentage points, while disagreement rates might increase slightly and C2 stays relatively stable.

**exp-003**: ProofWriter extension yields a disagreement rate around 25-30% matching the hypothesis, diagnostic precision around 78-82%, with C4 showing modest gains and C5 in the 78-83% range.

**exp-004**: MATH Level 5 performs weaker as a domain, with disagreement rates around 22-28% due to different formalization patterns, diagnostic precision dropping 5-10 percentage points compared to logic tasks, and a less asymmetric FOL-to-code ratio of 3-7.

**exp-005**: Repair improvements show C4 delta gains of 4-7 percentage points in all-mode but only up to 2 percentage points when excluding unknowns, with multi-round approaches providing marginal benefits.

**exp-006** through **exp-011** cover pure analysis of unknown samples, selection versus repair baselines, error taxonomy ablation, statistical significance testing, Qwen3-8B ablation, and GPQA Diamond results.

Now I'm organizing these findings into a comprehensive YAML structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29ffbdfe-7b3b-4d55-b049-35993ed93346",
  "isSidechain": false,
  "requestId": "req_011Cb3rcnzeU8DMh9jx8bM8V",
  "type": "assistant",
  "uuid": "59c8e9bd-9aa2-414d-9c77-797bdd010023",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "b514574f-8acf-405c-a805-45a06a49658a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011nBXZ6njw9FLojZvMTSy3o",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11034,
      "cache_read_input_tokens": 11841,
      "output_tokens": 16817,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11034,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 16817,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11034,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11034
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

_source line 9 · 2026-05-15T06:14:23.961Z_

```yaml
tier: median
narrative_guidance: >
  调整 claims 强度分配：Claim 1+2 (诊断信号+定位分类) 升格为唯一核心贡献，
  Claim 3 从 'repair framework' 降级为 'boundary characterization of when diagnosis translates to repair gains'。
  论文叙事重心从 'diagnosis + repair' 转向 'systematic empirical analysis of cross-representation disagreement patterns'，
  repair 仅作为一个 application case study。需补充 failure mode 分析（为什么 correlated failures 限制 repair）
  作为 negative-but-informative result。MATH 域若弱，诚实报告并讨论 domain-dependent effectiveness。
  仍可投 EMNLP Main，但需准备 Findings 作为 fallback。

imagined_experiments:
  - name: "FOLIO 完整分析（MVP 数据深度挖掘）"
    plan_id: "exp-001"
    description: "基于 204 样本 MVP 数据，完成统计显著性检验、错误类型详细分类、Unknown 样本子集分析、repair 前后对比。"
    expected_results:
      C1_disagree_rate_all: "39.6% (76/192)"
      C2_diagnostic_rate_all: "86.8% (66/76)"
      C3_error_types: 3
      C4_targeted_vs_blind_all: "+5.2pp (T:61/96 B:56/96)"
      C4_targeted_vs_blind_excl_unknown: "+0.0pp (T:38/59 B:38/59)"
      C5_localization_accuracy: "85.4% (35/41)"
      FOL_Code_error_ratio: "9:1"
      bootstrap_CI_C1: "[32.8%, 46.5%]"
      bootstrap_CI_C2: "[78.2%, 93.1%]"
      bootstrap_CI_C4_all: "[-1.8pp, +12.2pp]"
      bootstrap_CI_C5: "[73.4%, 93.5%]"
      fisher_exact_C4_all_p: 0.038
      fisher_exact_C4_excl_unknown_p: 0.91
      mcnemar_C4_all_p: 0.042
      unknown_sample_count: 66
      unknown_disagree_rate: "47.0% (31/66)"
      unknown_diagnostic_rate: "90.3% (28/31)"
      error_type_distribution:
        wrong_operator_or_quantifier: "46%"
        missing_or_extra_premise: "32%"
        type_mismatch_or_structural: "22%"
    result_rationale: >
      这是已有 MVP 数据的深度分析，数值已锁定。median 档的关键体现在统计检验结果上：
      C1/C2/C5 的 bootstrap CI 虽宽（样本量仅 204），但不跨零/不跨阈值，p 值显著。
      C4 All-mode 的 Fisher exact p=0.038 处于边缘显著（0.01&lt;p<0.05），CI 跨零 [-1.8, +12.2]，
      这正是 median 档 "部分指标 CI 较宽或 p 值边缘" 的典型表现。
      Excl-Unknown 的 C4 delta=0.0pp 完全不显著，确认 repair 效果集中在 Unknown 子集。
      错误类型分布中 wrong_operator_or_quantifier 占主导，说明 FOL 翻译的准确性优势
      来自 Z3 对逻辑算子的严格约束，而 Python 代码缺乏这种结构约束。
    tables:
      - table_id: "tab-001-1"
        caption: "FOLIO 全指标摘要 (Qwen3-32B, N=204, deduped from 211)"
        rows:
          - metric: "C1 Disagree Rate"
            all_mode: "39.6%"
            excl_unknown: "35.7%"
            bootstrap_95CI_all: "[32.8%, 46.5%]"
          - metric: "C2 Diagnostic Precision"
            all_mode: "86.8%"
            excl_unknown: "84.4%"
            bootstrap_95CI_all: "[78.2%, 93.1%]"
          - metric: "C3 Error Types"
            all_mode: "3"
            excl_unknown: "2"
            note: "Unknown 子集引入第3类错误"
          - metric: "C4 Δ(Targeted−Blind)"
            all_mode: "+5.2pp"
            excl_unknown: "+0.0pp"
            bootstrap_95CI_all: "[-1.8pp, +12.2pp]"
          - metric: "C5 Localization Acc"
            all_mode: "85.4%"
            excl_unknown: "89.3%"
            bootstrap_95CI_all: "[73.4%, 93.5%]"
          - metric: "FOL:Code Error Ratio"
            all_mode: "9:1"
            excl_unknown: "9:1"
            note: ""
      - table_id: "tab-001-2"
        caption: "FOLIO 错误类型分布 (N=66 diagnostic disagreements)"
        rows:
          - error_type: "Wrong Operator / Quantifier"
            count: 30
            pct: "46%"
            example: "∀→∃ 混淆，negation 遗漏"
          - error_type: "Missing / Extra Premise"
            count: 21
            pct: "32%"
            example: "多步推理中丢失中间条件"
          - error_type: "Type Mismatch / Structural"
            count: 15
            pct: "22%"
            example: "谓词参数顺序错误，嵌套结构错误"
    figures_description:
      - "fig-001-1: 分歧类型 Sankey 图 — Agree-Correct / Agree-Wrong / Disagree-FOL-Right / Disagree-Code-Right / Disagree-Both-Wrong 五流。突出 Disagree-FOL-Right (9:1 asymmetry) 的粗线条。"
      - "fig-001-2: Unknown vs non-Unknown 子集的 C4 delta 分组条形图，视觉化 repair 效果的子集依赖性。"
    analysis: >
      FOLIO 数据确认诊断信号强劲（C1~40%, C2~87%, C5~85%），但 repair 效果脆弱——
      All-mode +5.2pp 的 CI 跨零，Excl-Unknown 完全平坦。Unknown 样本驱动 repair delta
      的原因可能是：Unknown GT 意味着问题本身存在歧义，blind repair 倾向保持原答案，
      而 targeted repair 利用诊断信息打破僵局。这个发现本身有论文价值，但需要在 exp-006 深挖。

  - name: "跨模型消融（FOLIO）"
    plan_id: "exp-002"
    description: "DeepSeek V4 Pro 生成一种表征 + Qwen3-32B 生成另一种，测试模型多样性是否降低 correlated failures、提升诊断覆盖率。"
    expected_results:
      # 配置 A: DeepSeek-FOL + Qwen-Code
      config_A_C1_disagree_rate: "44.3% (85/192)"
      config_A_C2_diagnostic_precision: "82.4% (70/85)"
      config_A_false_agreement_rate: "18.2%"
      # 配置 B: Qwen-FOL + DeepSeek-Code
      config_B_C1_disagree_rate: "42.7% (82/192)"
      config_B_C2_diagnostic_precision: "80.5% (66/82)"
      config_B_false_agreement_rate: "19.5%"
      # 与 baseline (single-model) 对比
      baseline_false_agreement_rate: "21.8%"
      false_agreement_reduction_config_A: "3.6pp"
      false_agreement_reduction_config_B: "2.3pp"
      cross_model_C5_localization: "81.2%"
      cross_model_FOL_Code_ratio: "7:1"
      correlated_failure_overlap_jaccard: 0.62
    result_rationale: >
      median 档预测跨模型仅能小幅降低 false agreement（2-4pp 区间）。理由：
      (1) 两个模型共享训练数据的大量重叠（都在大规模数学/逻辑语料上训练），导致
      对同一问题的 formalization 错误存在 systematic bias overlap——例如对自然语言中
      歧义量词的处理，两个模型可能犯相同方向的错误。
      (2) Jaccard overlap 0.62 意味着 62% 的 correlated failures 在换模型后仍然 correlate，
      只有约 38% 被打破。这比 optimistic 档（Jaccard<0.5）悲观，但仍有改善。
      (3) disagree rate 上升 3-5pp（从 39.6% 到 ~43%），因为不同模型的 formalization
      偏好差异制造了额外分歧，但其中一部分是 "噪声分歧"（两侧都对但形式不同），
      导致 C2 diagnostic precision 从 86.8% 轻微下降到 ~81%。
      (4) FOL:Code ratio 从 9:1 降到 ~7:1，因为 DeepSeek 的 Code 生成能力可能略优于 Qwen，
      稀释了不对称性。C5 localization 也因此下降约 4pp。
      总体结论：跨模型可以作为 "有改善但不改变故事" 的消融实验，支撑 claims 但不改变 narrative。
    tables:
      - table_id: "tab-002-1"
        caption: "Cross-Model Ablation on FOLIO (N=192 effective samples)"
        rows:
          - config: "Single-Model (Qwen3-32B)"
            C1: "39.6%"
            C2: "86.8%"
            false_agree: "21.8%"
            C5: "85.4%"
          - config: "Cross-Model A (DS-FOL + Qwen-Code)"
            C1: "44.3%"
            C2: "82.4%"
            false_agree: "18.2%"
            C5: "81.2%"
          - config: "Cross-Model B (Qwen-FOL + DS-Code)"
            C1: "42.7%"
            C2: "80.5%"
            false_agree: "19.5%"
            C5: "79.8%"
    figures_description:
      - "fig-002-1: Venn 图 — single-model correlated failures vs cross-model correlated failures 的重叠。标注 Jaccard=0.62，说明大部分 correlation 源于 task-level difficulty 而非 model-specific bias。"
      - "fig-002-2: False agreement rate 的 bar chart，三个配置并排，附 bootstrap 95% CI error bars。"
    analysis: >
      跨模型消融的核心发现：false agreement reduction 仅 2-4pp，说明 correlated failures
      的主要来源是 task-level specification ambiguity（问题本身难以无歧义形式化）而非
      model-specific formalization bias。这是一个 negative-but-informative result：
      它直接解释了为什么 repair 效果有限——如果两个不同模型都无法正确形式化同一个问题，
      targeted repair（基于诊断信息修复）也无法突破 specification-level 的瓶颈。
      论文中应将此作为 "correlated failure 来源分析" 的关键证据。

  - name: "ProofWriter 扩展"
    plan_id: "exp-003"
    description: "在 ProofWriter 数据集上运行完整 pipeline（双表征+诊断+repair），验证方法在第二个逻辑推理 benchmark 上的泛化性。"
    expected_results:
      sample_size: 300
      C1_disagree_rate: "28.3% (85/300)"
      C2_diagnostic_precision: "81.2% (69/85)"
      C3_error_types: 3
      C4_targeted_vs_blind_all: "+5.8pp"
      C4_targeted_vs_blind_excl_unknown: "+1.2pp"
      C5_localization_accuracy: "82.0%"
      FOL_Code_error_ratio: "8:1"
      mvp_pass_all_mode: "5/5"
      mvp_pass_excl_unknown: "4/5 (C4 marginal)"
      bootstrap_CI_C1: "[23.2%, 33.8%]"
      bootstrap_CI_C2: "[72.5%, 88.1%]"
      fisher_exact_C4_all_p: 0.027
      fisher_exact_C4_excl_unknown_p: 0.34
    result_rationale: >
      ProofWriter 的 C1 disagree rate 预测为 ~28%，低于 FOLIO 的 40%。原因：
      (1) ProofWriter 的问题结构更规范——基于封闭世界假设的确定性推理，前提和规则
      以模板化自然语言给出，LLM 的 FOL 翻译任务更简单，因此翻译错误率更低。
      (2) 但仍保持 25%+ 是因为多步推理链（depth 3-5）引入的组合复杂度使得 Code 表征
      仍容易出错（循环逻辑、条件遗漏），只是单步翻译错误减少了。
      C2 diagnostic precision 降至 ~81%（FOLIO 87%），因为 ProofWriter 的 false disagreement
      比例略高——规范化的问题格式使两种表征更可能在语义等价但形式不同时被误判为分歧。
      C4 All-mode +5.8pp 与 FOLIO 一致，Excl-Unknown +1.2pp 略高于 FOLIO 的 0.0pp，
      因为 ProofWriter 的 Unknown 比例更低（封闭世界假设下更少歧义样本），
      non-Unknown repair delta 被稀释得更少。但 p=0.34 仍不显著。
      FOL:Code ratio 保持 ~8:1，略低于 FOLIO 的 9:1，验证了 "FOL 表征系统性更准确" 的跨 benchmark 结论。
      总体：ProofWriter 是 median 档中 "跨 benchmark 基本成立但有波动" 的主要支撑——
      诊断指标全部通过，repair 仍然边际。
    tables:
      - table_id: "tab-003-1"
        caption: "ProofWriter Full Pipeline Results (Qwen3-32B, N=300)"
        rows:
          - metric: "C1 Disagree Rate"
            all_mode: "28.3%"
            excl_unknown: "26.1%"
            FOLIO_comparison: "39.6% / 35.7%"
          - metric: "C2 Diagnostic Precision"
            all_mode: "81.2%"
            excl_unknown: "79.8%"
            FOLIO_comparison: "86.8% / 84.4%"
          - metric: "C4 Δ(T−B)"
            all_mode: "+5.8pp"
            excl_unknown: "+1.2pp"
            FOLIO_comparison: "+5.2pp / +0.0pp"
          - metric: "C5 Localization"
            all_mode: "82.0%"
            excl_unknown: "84.1%"
            FOLIO_comparison: "85.4% / 89.3%"
          - metric: "FOL:Code Ratio"
            all_mode: "8:1"
            excl_unknown: "8:1"
            FOLIO_comparison: "9:1"
      - table_id: "tab-003-2"
        caption: "ProofWriter 按推理深度分层的 C1 分歧率"
        rows:
          - depth: "0-1"
            disagree_rate: "18.5%"
            n: 92
          - depth: "2-3"
            disagree_rate: "29.7%"
            n: 118
          - depth: "4-5"
            disagree_rate: "38.9%"
            n: 90
    figures_description:
      - "fig-003-1: FOLIO vs ProofWriter 的 C1-C5 雷达图对比。ProofWriter 各轴略内缩但形状一致，视觉传达 '泛化成立但有波动'。"
      - "fig-003-2: 推理深度 vs disagree rate 的折线图，展示深度增加时分歧率单调递增——支持 '组合复杂度驱动 formalization 错误' 的机制解释。"
    analysis: >
      ProofWriter 验证了诊断信号的跨 benchmark 泛化性。C1 disagree rate 下降 (~28% vs ~40%)
      符合预期——更规范的输入减少了翻译错误。关键发现是推理深度与分歧率的正相关
      （depth 0-1: 18.5%, depth 4-5: 38.9%），为 "formalization 错误与组合复杂度相关"
      提供了直接证据。C4 仍然边际（Excl-Unknown +1.2pp, p=0.34），强化了 median 档
      "repair 需降级为 boundary characterization" 的叙事方向。
      ProofWriter 是 benchmarks_with_5of5_pass 的候选之一（All-mode 5/5），
      但 Excl-Unknown 仍 4/5。

  - name: "MATH Level 5 扩展"
    plan_id: "exp-004"
    description: "在 MATH 难题子集上运行 pipeline（CoT vs SymPy/Python 双表征），测试跨领域泛化性。"
    expected_results:
      sample_size: 250
      C1_disagree_rate: "24.0% (60/250)"
      C2_diagnostic_precision: "72.0% (43/60)"
      C3_error_types: 4
      C4_targeted_vs_blind_all: "+4.2pp"
      C4_targeted_vs_blind_excl_unknown: "-0.5pp"
      C5_localization_accuracy: "76.0%"
      FOL_Code_error_ratio: "4:1"
      mvp_pass_all_mode: "4/5 (C2 borderline)"
      mvp_pass_excl_unknown: "3/5 (C2 FAIL, C4 FAIL)"
      bootstrap_CI_C1: "[18.8%, 29.9%]"
      bootstrap_CI_C2: "[60.2%, 82.1%]"
      fisher_exact_C4_all_p: 0.068
      CoT_accuracy: "61.2%"
      SymPy_accuracy: "53.6%"
      oracle_accuracy: "68.8%"
      MATH_fol_code_error_ratio: "4:1"
      error_type_new: "computation_error"
      crash_rate_sympy: "12%"
    result_rationale: >
      MATH 域预测显著弱于逻辑域，原因有三层：
      (1) FOL:Code 不对称性大幅减弱（4:1 vs 9:1）。数学领域中 CoT（对应逻辑域的 FOL）
      并不像 FOL/Z3 那样有严格的形式约束——CoT 是自然语言推理链，容易出现计算错误
      和推理跳跃。而 SymPy/Python 在数值计算上反而更可靠。因此两侧的错误率差距缩小。
      (2) C2 diagnostic precision 降至 ~72%（逻辑域 ~84-87%），因为数学问题中 "分歧但
      两侧都错" 的比例更高——难题（Level 5）常导致 CoT 和 SymPy 都犯不同类型的错误
      （CoT 计算错误 vs SymPy 建模错误），分歧并不指向一侧正确。
      (3) C1 disagree rate ~24%，处于 median 档下限（假设区间 20-30%），因为数学问题
      的答案空间更确定（数值答案），两侧即使推理过程不同，更容易碰巧得到相同答案
      （false agreement 更高）。
      新增第4种错误类型 computation_error（CoT 中的算术错误），这在逻辑域不存在。
      C4 All-mode +4.2pp 的 p=0.068 不显著，MATH 将是 "5/5 pass" 失败的 benchmark。
      SymPy crash rate 12% 引入额外噪声——部分 SymPy 代码因库限制无法执行。
    tables:
      - table_id: "tab-004-1"
        caption: "MATH Level 5 Full Pipeline Results (Qwen3-32B, N=250)"
        rows:
          - metric: "C1 Disagree Rate"
            value: "24.0%"
            vs_FOLIO: "39.6%"
            vs_ProofWriter: "28.3%"
          - metric: "C2 Diagnostic Precision"
            value: "72.0%"
            vs_FOLIO: "86.8%"
            vs_ProofWriter: "81.2%"
          - metric: "C4 Δ(T−B) All"
            value: "+4.2pp"
            vs_FOLIO: "+5.2pp"
            vs_ProofWriter: "+5.8pp"
          - metric: "C5 Localization"
            value: "76.0%"
            vs_FOLIO: "85.4%"
            vs_ProofWriter: "82.0%"
          - metric: "Representation Error Ratio"
            value: "4:1 (CoT:SymPy)"
            vs_FOLIO: "9:1 (FOL:Code)"
            vs_ProofWriter: "8:1"
      - table_id: "tab-004-2"
        caption: "MATH 错误类型分布 (N=43 diagnostic disagreements)"
        rows:
          - error_type: "Computation Error (CoT arithmetic)"
            count: 14
            pct: "33%"
          - error_type: "Wrong Setup / Equation"
            count: 12
            pct: "28%"
          - error_type: "Missing Case / Edge Condition"
            count: 10
            pct: "23%"
          - error_type: "SymPy Modeling Error"
            count: 7
            pct: "16%"
      - table_id: "tab-004-3"
        caption: "MATH 按子领域分层分歧率"
        rows:
          - subdomain: "Algebra"
            disagree_rate: "20.3%"
            C2: "68.4%"
            n: 74
          - subdomain: "Number Theory"
            disagree_rate: "22.1%"
            C2: "70.0%"
            n: 52
          - subdomain: "Geometry"
            disagree_rate: "31.4%"
            C2: "76.9%"
            n: 51
          - subdomain: "Counting & Probability"
            disagree_rate: "25.8%"
            C2: "75.0%"
            n: 42
          - subdomain: "Precalculus"
            disagree_rate: "22.6%"
            C2: "71.4%"
            n: 31
    figures_description:
      - "fig-004-1: 三个 benchmark 的 C1-C5 雷达图叠加。MATH 的五角形面积明显小于 FOLIO/ProofWriter，特别在 C2 和 C5 轴收缩显著。"
      - "fig-004-2: FOL:Code (CoT:SymPy) error ratio 的 benchmark 对比柱状图。从 9:1 → 8:1 → 4:1 的递减趋势，讨论 domain-dependent asymmetry。"
      - "fig-004-3: MATH 子领域热力图，行=子领域，列=C1/C2/C4/C5，颜色深浅表示指标值。Geometry 是相对亮点（最高分歧率和诊断率）。"
    analysis: >
      MATH 是 median 档的 "弱域" 体现。diagnostic precision 72% 仍高于随机，说明
      cross-representation disagreement 作为诊断信号在数学域仍有价值，但效力明显衰减。
      核心原因是不对称性坍塌：数学域中 CoT 不像 FOL 那样受形式系统约束，
      两种表征的 "可靠性差" 更接近，导致分歧的诊断价值下降。
      Geometry 子领域表现最好（C1=31.4%, C2=76.9%），因为几何问题的 SymPy 建模困难
      恢复了一定的不对称性。论文应诚实报告 MATH 的衰减，将其定位为 "domain boundary"——
      方法在逻辑域强效，数学域有效但减弱，揭示了 "representation asymmetry 是方法
      有效性的前提条件" 这一理论洞察。

  - name: "Repair 机制改进"
    plan_id: "exp-005"
    description: "多轮 repair（max 3 rounds）、改进 repair prompt（加入错误类型特定的修复策略）、对比 repair 前后的 C4 delta。"
    expected_results:
      # FOLIO repair 改进结果
      FOLIO_C4_delta_all_v1_baseline: "+5.2pp"
      FOLIO_C4_delta_all_v2_multiround: "+6.8pp"
      FOLIO_C4_delta_all_v3_type_specific: "+7.1pp"
      FOLIO_C4_delta_all_v4_combined: "+6.5pp"
      FOLIO_C4_delta_excl_unknown_v1: "+0.0pp"
      FOLIO_C4_delta_excl_unknown_v2: "+1.4pp"
      FOLIO_C4_delta_excl_unknown_v3: "+1.8pp"
      FOLIO_C4_delta_excl_unknown_v4: "+1.5pp"
      round_2_additional_fixes: 4
      round_3_additional_fixes: 1
      diminishing_returns_evident: true
      type_specific_vs_generic_delta: "+1.9pp"
    result_rationale: >
      median 档预测 repair 改进有限（C4 delta All-mode 升至 4-7pp 区间上段，Excl-Unknown ≤2pp）。
      原因分析：
      (1) 多轮 repair 的收益递减极快：第2轮额外修复 4 个样本，第3轮仅 1 个。
      因为 repair 失败的主要原因不是 "修复信息不够"，而是 "底层 specification-level 错误
      无法通过 prompt 层面解决"——模型对问题本身的理解有误，无论 repair 多少轮都不会改。
      (2) 错误类型特定修复策略（如 "检查量词" / "验证前提完整性"）在 wrong_operator 类型上
      确实更有效（该类型 repair 成功率从 ~35% 升至 ~50%），但对 missing_premise 类型
      几乎无效（信息缺失无法从诊断中恢复）。
      (3) combined (v4) 反而略低于分别最优 (v3)，因为多轮+类型特定组合时 prompt 过长
      导致模型 "迷失"，指令遵从度下降。
      (4) Excl-Unknown 从 0.0pp 升至约 1.5pp，进步微小且不显著——这正是 median 档
      "repair 经改进仍边际" 的核心含义。repair 的天花板由 correlated failures 决定，
      不是 prompt 工程能突破的。
    tables:
      - table_id: "tab-005-1"
        caption: "Repair Strategy Comparison on FOLIO (N=96 disagree-targeted pairs)"
        rows:
          - strategy: "v1: Baseline (single round, generic prompt)"
            C4_all: "+5.2pp"
            C4_excl_unk: "+0.0pp"
            repair_success_rate: "31.6%"
          - strategy: "v2: Multi-round (max 3)"
            C4_all: "+6.8pp"
            C4_excl_unk: "+1.4pp"
            repair_success_rate: "36.8%"
          - strategy: "v3: Type-specific prompt"
            C4_all: "+7.1pp"
            C4_excl_unk: "+1.8pp"
            repair_success_rate: "38.2%"
          - strategy: "v4: Combined (multi-round + type-specific)"
            C4_all: "+6.5pp"
            C4_excl_unk: "+1.5pp"
            repair_success_rate: "35.5%"
      - table_id: "tab-005-2"
        caption: "Repair Success Rate by Error Type (v3 type-specific)"
        rows:
          - error_type: "Wrong Operator/Quantifier"
            baseline_repair_rate: "35.0%"
            v3_repair_rate: "50.0%"
            delta: "+15.0pp"
          - error_type: "Missing/Extra Premise"
            baseline_repair_rate: "19.0%"
            v3_repair_rate: "21.4%"
            delta: "+2.4pp"
          - error_type: "Type Mismatch/Structural"
            baseline_repair_rate: "26.7%"
            v3_repair_rate: "33.3%"
            delta: "+6.7pp"
    figures_description:
      - "fig-005-1: 多轮 repair 的累计修复曲线 — x 轴为 round (1,2,3)，y 轴为累计修复样本数。曲线快速平坦化，视觉化 diminishing returns。"
      - "fig-005-2: 按错误类型分组的 repair 成功率对比（baseline vs v3），stacked bar chart。Wrong Operator 改善最大，Missing Premise 几乎不变。"
    analysis: >
      repair 改进实验确认了 median 档的核心判断：即使用最优策略（v3 type-specific），
      C4 delta All-mode 仅从 +5.2 升至 +7.1pp，Excl-Unknown 从 0.0 升至 1.8pp。
      错误类型分层揭示了 repair 的 "可修复边界"——operator/quantifier 错误因为信息
      完整（诊断能指出具体哪个算子错了）而可修复；premise-level 错误因为信息缺失
      而不可修复。这就是 Claim 3 "boundary characterization" 的实证基础。
      建议论文采用 v3 作为报告结果（最优单策略），v4 的退化作为 "prompt complexity
      ceiling" 的 negative result 放在 appendix。

  - name: "Unknown 样本深度分析"
    plan_id: "exp-006"
    description: "为什么 GT=Unknown 样本驱动 C4 delta？分析 Unknown 样本的错误模式分布，是否存在 specification-level vs formalization-specific 的系统性差异。"
    expected_results:
      unknown_sample_count: 66
      unknown_disagree_count: 31
      unknown_error_distribution:
        ambiguous_specification: "48.4% (15/31)"
        formalization_specific: "35.5% (11/31)"
        both: "16.1% (5/31)"
      non_unknown_error_distribution:
        ambiguous_specification: "17.8% (8/45)"
        formalization_specific: "66.7% (30/45)"
        both: "15.6% (7/45)"
      chi_squared_p: 0.003
      repair_success_by_error_source:
        spec_ambiguity_repair_rate: "40.0%"
        formalization_specific_repair_rate: "27.3%"
        both_repair_rate: "20.0%"
      blind_repair_by_error_source:
        spec_ambiguity_blind_rate: "20.0%"
        formalization_specific_blind_rate: "26.7%"
        both_blind_rate: "14.3%"
    result_rationale: >
      Unknown 样本驱动 repair delta 的机制假说：Unknown GT 意味着在封闭世界假设下
      信息不足以判定 True/False，问题本身具有 "规格歧义"。在这类样本上：
      (1) ambiguous_specification 错误占 48.4%（vs non-Unknown 的 17.8%），因为问题
      本身的歧义传导到 formalization——两种表征对歧义的处理方式不同，产生分歧。
      (2) targeted repair 在 spec-ambiguity 样本上成功率 40%（vs blind 20%），差距 20pp，
      因为诊断信息帮助 repair 选择了 "更保守的解读"（倾向输出 Unknown），而 blind
      repair 无此引导，倾向输出确定性答案（True/False）。
      (3) 在 formalization-specific 错误上，targeted 和 blind repair 成功率几乎相同
      （27.3% vs 26.7%），因为这类错误在 non-Unknown 样本中也大量存在，且 repair
      策略对两组样本的处理方式无差异。
      (4) chi_squared_p=0.003 确认 Unknown vs non-Unknown 的错误来源分布有显著差异。
      结论：C4 delta 由 Unknown 驱动不是 "方法只对简单问题有效"，而是 "方法对
      specification-ambiguity 类问题特别有效"——这是一个有意义的 positive finding。
    tables:
      - table_id: "tab-006-1"
        caption: "Error Source Distribution: Unknown vs Non-Unknown Subsets"
        rows:
          - subset: "GT=Unknown (N=31 disagree)"
            spec_ambiguity: "48.4%"
            formalization_specific: "35.5%"
            both: "16.1%"
          - subset: "GT≠Unknown (N=45 disagree)"
            spec_ambiguity: "17.8%"
            formalization_specific: "66.7%"
            both: "15.6%"
          - subset: "χ² test"
            spec_ambiguity: "p=0.003"
            formalization_specific: ""
            both: ""
      - table_id: "tab-006-2"
        caption: "Targeted vs Blind Repair Rate by Error Source"
        rows:
          - error_source: "Specification Ambiguity"
            targeted: "40.0%"
            blind: "20.0%"
            delta: "+20.0pp"
          - error_source: "Formalization-Specific"
            targeted: "27.3%"
            blind: "26.7%"
            delta: "+0.6pp"
          - error_source: "Both"
            targeted: "20.0%"
            blind: "14.3%"
            delta: "+5.7pp"
    figures_description:
      - "fig-006-1: 2x2 热力图 — 行=Unknown/non-Unknown，列=Spec-Ambiguity/Formalization-Specific，颜色=比例。视觉化两个子集的错误来源分布差异。"
      - "fig-006-2: Repair delta (targeted−blind) 按 error source 分组的 bar chart。Spec-Ambiguity 的 +20pp 柱子突出，Formalization-Specific 接近零。"
    analysis: >
      此分析提供了 Unknown-driven delta 的因果解释：诊断引导的 repair 对 specification-
      ambiguity 类错误特别有效（+20pp），但对 pure formalization errors 无额外优势。
      Unknown 样本恰好富含 spec-ambiguity 错误，因此 C4 delta 集中在此子集。
      这不是方法的缺陷，而是方法的 "有效域刻画"——论文应将其定位为 boundary
      characterization 的核心证据：cross-representation diagnosis 最有价值的场景
      是 "问题规格本身有歧义" 的情况，此时不同表征对歧义的不同处理为 repair 提供了
      disambiguation signal。

  - name: "Selection vs Repair 消融"
    plan_id: "exp-007"
    description: "当检测到分歧且定位了错误侧后，直接选择另一侧答案（selection）vs 诊断引导修复（repair）的对比。"
    expected_results:
      # FOLIO 数据
      selection_accuracy_all: "78.9% (60/76)"
      repair_accuracy_all: "80.3% (61/76)"
      selection_accuracy_excl_unknown: "82.2% (37/45)"
      repair_accuracy_excl_unknown: "84.4% (38/45)"
      baseline_no_intervention: "63.2% (48/76)"
      selection_vs_repair_delta_all: "-1.3pp"
      selection_vs_repair_delta_excl_unknown: "-2.2pp"
      selection_limited_by_localization_error: "14.6% (C5 错误导致选错侧)"
      oracle_selection_accuracy: "93.4% (71/76)"
    result_rationale: >
      Selection 和 Repair 的差距预测很小（~1-2pp），原因：
      (1) 当 C5 localization 正确时（85.4% 情况），selection 直接选对侧就是最优策略，
      repair 不可能做得更好（除非 repair 把两侧都修对了，概率极低）。
      (2) 当 C5 localization 错误时（14.6% 情况），selection 选错侧，repair 也很可能
      基于错误诊断修错侧，两者都失败。
      (3) Repair 略优于 selection 的 ~1-2pp 来自少数 "两侧都错但 repair 修对了一侧" 的样本。
      (4) oracle selection（假设完美 localization）的 93.4% 展示了诊断信号的真正上限，
      暗示 C5 localization accuracy 是整个方法的关键瓶颈。
      回应 R3：selection 确实是 repair 的 strong baseline，但 repair 的额外价值在于
      它不需要完美 localization——即使定位错误，repair 仍有概率修复。这种鲁棒性
      在 localization 不确定时有价值。
    tables:
      - table_id: "tab-007-1"
        caption: "Selection vs Repair vs No Intervention (FOLIO, disagree subset N=76)"
        rows:
          - strategy: "No Intervention (keep both, majority)"
            acc_all: "63.2%"
            acc_excl_unk: "62.2%"
          - strategy: "Selection (choose localized-correct side)"
            acc_all: "78.9%"
            acc_excl_unk: "82.2%"
          - strategy: "Repair (diagnosis-guided fix)"
            acc_all: "80.3%"
            acc_excl_unk: "84.4%"
          - strategy: "Oracle Selection (perfect localization)"
            acc_all: "93.4%"
            acc_excl_unk: "95.6%"
    figures_description:
      - "fig-007-1: 四种策略的 accuracy bar chart，附 oracle 上界虚线。No Intervention → Selection 的跳跃远大于 Selection → Repair 的跳跃。"
    analysis: >
      Selection vs Repair 的小差距确认了 repair 的边际价值。但更重要的发现是
      oracle selection 的 93.4% 上界——这说明诊断信号本身价值巨大（+30pp over no intervention），
      方法的瓶颈在 localization accuracy 而非 repair strategy。
      论文应论证：(1) 诊断+定位是核心贡献；(2) 下游应用（selection 或 repair）
      是次要的；(3) localization accuracy 的提升是最有价值的未来方向。

  - name: "Error Taxonomy 消融"
    plan_id: "exp-008"
    description: "按错误类型分派修复策略 vs 固定策略（统一重生成），验证 taxonomy 的规定性价值。"
    expected_results:
      # 基于 exp-005 的 v3 结果
      taxonomy_guided_repair_rate: "38.2%"
      fixed_strategy_repair_rate: "31.6%"
      taxonomy_delta: "+6.6pp"
      per_type_improvement:
        wrong_operator: "+15.0pp (50% vs 35%)"
        missing_premise: "+2.4pp (21.4% vs 19.0%)"
        type_mismatch: "+6.7pp (33.3% vs 26.7%)"
      fisher_exact_p: 0.089
    result_rationale: >
      Taxonomy-guided 比 fixed strategy 高 ~6.6pp repair 成功率，但 p=0.089 不显著。
      原因：(1) taxonomy 对 wrong_operator 类错误确实有效（+15pp），因为该类型的修复
      指令明确（"检查量词和算子"），模型能很好地遵从。(2) 但 missing_premise 类型
      几乎无提升，因为 "补充缺失前提" 需要回到原始自然语言重新理解，taxonomy 标签
      本身不提供足够信息。(3) 样本量（76 disagree samples）对于按类型分层后各 cell 仅
      ~20-30 个样本，统计功效不足以检测中等效应量。
      论文应报告 taxonomy 有方向性改善但统计不显著，符合 "taxonomy 提供可解释性
      和方向性指导，但不是 repair 的 silver bullet" 的 median 档叙事。
    tables:
      - table_id: "tab-008-1"
        caption: "Taxonomy-Guided vs Fixed Strategy Repair (FOLIO, N=76)"
        rows:
          - strategy: "Fixed (uniform regeneration)"
            overall: "31.6%"
            wrong_op: "35.0%"
            missing: "19.0%"
            structural: "26.7%"
          - strategy: "Taxonomy-Guided"
            overall: "38.2%"
            wrong_op: "50.0%"
            missing: "21.4%"
            structural: "33.3%"
          - strategy: "Delta"
            overall: "+6.6pp"
            wrong_op: "+15.0pp"
            missing: "+2.4pp"
            structural: "+6.7pp"
    figures_description:
      - "fig-008-1: 按错误类型的 repair 成功率分组对比图。Wrong Operator 的改善柱突出，其余两类几乎平齐。"
    analysis: >
      Taxonomy 消融支持了 Claim 2 的 "错误分类有规定性价值" 但力度有限。
      建议论文表述为 "error classification enables type-specific repair strategies
      with directional improvement, particularly for operator-level errors"，
      避免过度宣称。p=0.089 放在 table 中如实报告，在讨论中承认 power limitation。

  - name: "统计显著性全面检验"
    plan_id: "exp-009"
    description: "对所有 benchmark 的 C1-C5 指标做 bootstrap 95% CI + Fisher exact test / McNemar test。"
    expected_results:
      FOLIO:
        C1_bootstrap_CI: "[32.8%, 46.5%]"
        C1_vs_chance_p: "<0.001"
        C2_bootstrap_CI: "[78.2%, 93.1%]"
        C2_vs_50pct_p: "<0.001"
        C4_fisher_all_p: 0.038
        C4_fisher_excl_unk_p: 0.91
        C4_mcnemar_all_p: 0.042
        C5_bootstrap_CI: "[73.4%, 93.5%]"
        C5_vs_50pct_p: "<0.001"
      ProofWriter:
        C1_bootstrap_CI: "[23.2%, 33.8%]"
        C1_vs_chance_p: "<0.001"
        C2_bootstrap_CI: "[72.5%, 88.1%]"
        C2_vs_50pct_p: "<0.001"
        C4_fisher_all_p: 0.027
        C4_fisher_excl_unk_p: 0.34
        C5_bootstrap_CI: "[75.3%, 87.9%]"
        C5_vs_50pct_p: "<0.001"
      MATH:
        C1_bootstrap_CI: "[18.8%, 29.9%]"
        C1_vs_chance_p: "<0.001"
        C2_bootstrap_CI: "[60.2%, 82.1%]"
        C2_vs_50pct_p: 0.004
        C4_fisher_all_p: 0.068
        C4_fisher_excl_unk_p: 0.62
        C5_bootstrap_CI: "[65.8%, 84.4%]"
        C5_vs_50pct_p: "<0.001"
      cross_benchmark_summary:
        all_C1_significant: true
        all_C2_significant: true
        C4_significant_count: "1/3 (FOLIO marginal, ProofWriter marginal, MATH not sig)"
        all_C5_significant: true
        metrics_with_marginal_p: ["FOLIO C4 (p=0.038)", "ProofWriter C4 (p=0.027)", "MATH C2 (p=0.004)", "MATH C4 (p=0.068)"]
    result_rationale: >
      median 档的统计检验呈现清晰的两级分化：
      (1) 诊断指标（C1/C2/C5）在所有 benchmark 上均显著（p<0.005），CI 不跨关键阈值。
      这是因为 disagree rate、diagnostic precision、localization accuracy 的效应量大
      （均远离 chance level），即使中等样本量也足以检测。
      (2) repair 指标（C4）在所有 benchmark 上均边缘或不显著。FOLIO p=0.038、
      ProofWriter p=0.027 在传统 α=0.05 下刚刚通过，但若做多重比较校正（Bonferroni
      对 3 个 benchmark）则不再显著。MATH p=0.068 直接不显著。
      (3) MATH C2 的 CI 特别宽 [60.2%, 82.1%]，下限接近 "marginally informative" 区域，
      反映了数学域诊断信号更嘈杂的现实。
      这个两级分化模式完美支撑 median 档的叙事策略：诊断贡献有坚实统计支撑，
      repair 贡献诚实报告为 "方向性但统计不robust"。
    tables:
      - table_id: "tab-009-1"
        caption: "Statistical Significance Summary Across All Benchmarks"
        rows:
          - metric: "C1 Disagree Rate"
            FOLIO_p: "<0.001 ✓"
            ProofWriter_p: "<0.001 ✓"
            MATH_p: "<0.001 ✓"
            verdict: "3/3 significant"
          - metric: "C2 Diagnostic Precision"
            FOLIO_p: "<0.001 ✓"
            ProofWriter_p: "<0.001 ✓"
            MATH_p: "0.004 ✓"
            verdict: "3/3 significant"
          - metric: "C4 Δ(T−B) All-mode"
            FOLIO_p: "0.038 ○"
            ProofWriter_p: "0.027 ○"
            MATH_p: "0.068 ✗"
            verdict: "0/3 after Bonferroni"
          - metric: "C5 Localization"
            FOLIO_p: "<0.001 ✓"
            ProofWriter_p: "<0.001 ✓"
            MATH_p: "<0.001 ✓"
            verdict: "3/3 significant"
    figures_description:
      - "fig-009-1: Forest plot — 所有 benchmark × 所有 metric 的 bootstrap CI，按 metric 分组。C4 的 CI 条跨零，其余不跨。一图总结全部统计结果。"
    analysis: >
      统计检验结果为论文的 claim 强度分配提供了硬约束：
      C1/C2/C5 全部 3/3 显著 → Claim 1+2 可自信宣称。
      C4 0/3 Bonferroni-corrected 显著 → Claim 3 必须降级为 "directional evidence"。
      建议论文正文报告未校正 p 值（FOLIO 0.038, ProofWriter 0.027），appendix 报告
      Bonferroni 校正后结果，讨论中承认 repair 效果的统计证据不够 robust。

  - name: "Qwen3-8B 消融"
    plan_id: "exp-010"
    description: "低能力模型上的诊断率和分歧率是否变化？测试方法对模型能力的鲁棒性。"
    expected_results:
      sample_size: 204
      benchmark: "FOLIO"
      C1_disagree_rate: "52.1% (100/192)"
      C2_diagnostic_precision: "74.0% (74/100)"
      C5_localization_accuracy: "72.5%"
      FOL_Code_error_ratio: "5:1"
      FOL_accuracy_8B: "58.3%"
      Code_accuracy_8B: "41.7%"
      Qwen32B_FOL_accuracy: "74.0%"
      Qwen32B_Code_accuracy: "52.1%"
    result_rationale: >
      低能力模型（8B）预测 C1 disagree rate 上升至 ~52%（32B 为 40%），因为模型
      能力下降导致两种表征的 formalization 质量同时下降，但 Code 表征下降更快
      （从 52.1% → 41.7%），产生更多分歧。C2 diagnostic precision 下降至 ~74%，
      因为 8B 模型更容易在两侧同时犯错（both-wrong disagreement 增加），这些
      分歧不具有诊断价值。FOL:Code ratio 从 9:1 降至 5:1，因为 8B 的 FOL 能力
      也显著退化。C5 localization 降至 ~72.5%，因为 FOL 不再那么可靠，
      "FOL 侧通常正确" 的启发式准确率下降。
      结论：方法对模型能力有一定鲁棒性（指标方向一致），但效力随能力下降。
      这支持 "representation asymmetry 是方法有效性前提" 的论点——更强的模型
      有更大的 asymmetry，诊断信号更强。
    tables:
      - table_id: "tab-010-1"
        caption: "Model Capability Ablation: Qwen3-8B vs Qwen3-32B on FOLIO"
        rows:
          - metric: "FOL Accuracy"
            Qwen3_32B: "74.0%"
            Qwen3_8B: "58.3%"
            delta: "-15.7pp"
          - metric: "Code Accuracy"
            Qwen3_32B: "52.1%"
            Qwen3_8B: "41.7%"
            delta: "-10.4pp"
          - metric: "C1 Disagree Rate"
            Qwen3_32B: "39.6%"
            Qwen3_8B: "52.1%"
            delta: "+12.5pp"
          - metric: "C2 Diagnostic Precision"
            Qwen3_32B: "86.8%"
            Qwen3_8B: "74.0%"
            delta: "-12.8pp"
          - metric: "C5 Localization"
            Qwen3_32B: "85.4%"
            Qwen3_8B: "72.5%"
            delta: "-12.9pp"
          - metric: "FOL:Code Error Ratio"
            Qwen3_32B: "9:1"
            Qwen3_8B: "5:1"
            delta: "asymmetry reduced"
    figures_description:
      - "fig-010-1: 双 Y 轴图 — 左轴 FOL/Code accuracy（随模型能力变化），右轴 C2 diagnostic precision。展示三者的协同变化关系。"
    analysis: >
      8B 消融的核心发现是 representation asymmetry 与 diagnostic precision 的耦合：
      当模型能力下降使 FOL:Code ratio 从 9:1 缩至 5:1 时，C2 从 87% 降至 74%。
      这量化了 "asymmetry 是方法前提" 的关系。论文可据此提出 "方法最适合
      FOL:Code ratio ≥ 7:1 的场景" 的实用指南。

  - name: "GPQA Diamond 扩展"
    plan_id: "exp-011"
    description: "科学知识推理领域，CoT vs Python 验证代码，测试第四个域的泛化性。"
    expected_results:
      sample_size: 198
      C1_disagree_rate: "33.8% (67/198)"
      C2_diagnostic_precision: "68.7% (46/67)"
      C5_localization_accuracy: "71.7%"
      CoT_accuracy: "42.4%"
      Code_accuracy: "35.9%"
      CoT_Code_error_ratio: "3:1"
      C4_delta_all: "+2.8pp"
      mvp_pass_all: "3/5 (C2 FAIL, C4 FAIL)"
    result_rationale: >
      GPQA Diamond（研究生级科学问题）预测为最弱 benchmark，原因：
      (1) 科学问题需要大量 domain knowledge，Code 表征很难编码领域知识（如化学反应
      机理、量子力学原理），CoT:Code ratio 进一步降至 ~3:1。
      (2) C2 降至 ~69%，接近 "marginally useful" 边界，因为科学问题的分歧更多源于
      两侧都不懂（知识缺失）而非 formalization 错误。
      (3) GPQA 整体准确率低（CoT ~42%, Code ~36%），基础能力不足限制了诊断上限。
      结论：GPQA 结果进一步支持 "方法效力依赖于 representation asymmetry" 的论点，
      在科学域不推荐使用。如果时间不够（P2 priority），可以省略此实验，
      3 benchmarks (FOLIO + ProofWriter + MATH) 已足够支撑论文。
    tables:
      - table_id: "tab-011-1"
        caption: "GPQA Diamond Results (Qwen3-32B, N=198)"
        rows:
          - metric: "C1"
            value: "33.8%"
            pass: "✓"
          - metric: "C2"
            value: "68.7%"
            pass: "✗ (<70%)"
          - metric: "C4 Δ"
            value: "+2.8pp"
            pass: "✗"
          - metric: "C5"
            value: "71.7%"
            pass: "✗ (<75%)"
    figures_description:
      - "fig-011-1: 四 benchmark 的 C1-C5 雷达图叠加（若包含 GPQA）。GPQA 的五角形最小，视觉化 domain boundary。"
    analysis: >
      GPQA 作为 P2 实验，如果做了可以放在 appendix 作为 "domain boundary" 的额外证据。
      如果 deadline 紧张（ARR May 25 仅剩 10 天），建议跳过。3 benchmarks 已能
      支撑 "逻辑域强、数学域中等" 的 domain-dependent effectiveness 叙事。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59c8e9bd-9aa2-414d-9c77-797bdd010023",
  "isSidechain": false,
  "requestId": "req_011Cb3rcnzeU8DMh9jx8bM8V",
  "type": "assistant",
  "uuid": "fdb9204e-a3d8-4f21-8233-a90c0caec535",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "b514574f-8acf-405c-a805-45a06a49658a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011nBXZ6njw9FLojZvMTSy3o",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11034,
      "cache_read_input_tokens": 11841,
      "output_tokens": 16817,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11034,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 16817,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11034,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11034
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：诊断信号 (C1/C2/C5) 跨 benchmark 基本成立但有波动，repair (C4) 经改进仍边际，需将分析权重进一步向诊断倾斜 核心假设：['C1 disagree rate 在 ProofWriter 保持 25%+，MATH 可能偏低 (20-30%) 因数学问题形式化模式不同', 'C…",
  "leafUuid": "fdb9204e-a3d8-4f21-8233-a90c0caec535",
  "sessionId": "b514574f-8acf-405c-a805-45a06a49658a"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Detailed median tier experiment predictions with rationales",
  "sessionId": "b514574f-8acf-405c-a805-45a06a49658a"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：诊断信号 (C1/C2/C5) 跨 benchmark 基本成立但有波动，repair (C4) 经改进仍边际，需将分析权重进一步向诊断倾斜 核心假设：['C1 disagree rate 在 ProofWriter 保持 25%+，MATH 可能偏低 (20-30%) 因数学问题形式化模式不同', 'C…",
  "leafUuid": "fdb9204e-a3d8-4f21-8233-a90c0caec535",
  "sessionId": "b514574f-8acf-405c-a805-45a06a49658a"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Detailed median tier experiment predictions with rationales",
  "sessionId": "b514574f-8acf-405c-a805-45a06a49658a"
}
```

---
