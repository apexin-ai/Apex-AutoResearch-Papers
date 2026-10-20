# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：诊断信号跨 benchmark/模型稳健泛化，repair 改进经 exp-005 提升至可独立 claim 水平，MATH 域展现不同不对称模式丰富叙

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/607eee2a-7f6d-409d-b311-c0419e42790d.jsonl`
- **Structured JSON:** [`12bca5dea8eefec4a434.json`](../../sessions/12/12bca5dea8eefec4a434.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-15T06:05:23.292Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T06:05:23.292Z",
  "sessionId": "607eee2a-7f6d-409d-b311-c0419e42790d",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：诊断信号跨 benchmark/模型稳健泛化，repair 改进经 exp-005 提升至可独立 claim 水平，MATH 域展现不同不对称模式丰富叙事\n核心假设：['C1 disagree rate 在 ProofWriter/MATH 上保持 30%+ (方法非 FOLIO 特异)', 'C2 diagnostic precision 跨 benchmark 均 ≥80%', 'exp-005 多轮+类型特定 repair 将 C4 delta 拉至 ≥8pp (All-mode)，Excl-Unknown 也转正 (≥3pp)', 'exp-002 跨模型消融降低 correlated failures，false agreement rate 下降 ≥5pp', 'MATH 域 FOL:Code 不对称性显著不同 (≤3:1)，提供跨域对比叙事', '所有 C1-C5 主指标 bootstrap 95% CI 不跨零，p<0.05']\n关键指标范围：{'C1_disagree_rate_cross_bench': [0.3, 0.5], 'C2_diagnostic_precision_cross_bench': [0.8, 0.92], 'C4_targeted_vs_blind_delta_pp_all_mode': [8.0, 15.0], 'C4_targeted_vs_blind_delta_pp_excl_unknown': [3.0, 8.0], 'C5_localization_accuracy_cross_bench': [0.82, 0.92], 'cross_model_false_agreement_reduction_pp': [5.0, 12.0], 'MATH_fol_code_error_ratio': [1.5, 3.0], 'benchmarks_with_5of5_pass': [3, 3]}\n叙事方向：原始 dual-track framing 完全成立。三 benchmark 一致验证诊断信号的高精度和跨域泛化性；repair 改进足以作为独立贡献而非仅 downstream utility 展示；MATH 域不对称性差异深化 'LLM 对不同形式化范式的系统性差异' 叙事。Claims 1-3 均无需降级，直投 EMNLP Main。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: cross_representation_disagreement_diagno\nfocus: C4 repair improvement is the main weakness (0.2pp margin). Key questions: (1) Is the dual-track framing (systematic analysis + lightweight repair) strong enough for EMNLP Main? (2) Does the boundary characterization (Claim 3) compensate for weak repair results? (3) Is 3 benchmarks (FOLIO + ProofWriter + MATH) sufficient or do we need more? (4) The 9:1 FOL:Code asymmetry — strength or weakness for the story?\n\n## paper_framing.md\n\n# Paper Framing — cross_representation_disagreement_diagno\n\n## Target Venue\n- Primary: EMNLP 2026 Main (ARR submission)\n- Fallback: EMNLP 2026 Findings\n- Deadline: ARR May 25, 2026 (10 days)\n- Secondary: AAAI 2027 (abstract July 25, full August 1) — extended version with full benchmark coverage\n\n## Core Insight\nCross-representation disagreement (FOL/Z3 vs Python Code) produced by the same LLM for the same reasoning problem is an underexploited diagnostic signal that detects formalization errors, enables error localization and classification, and guides targeted repair — going beyond existing approaches that only filter or verify within a single representation.\n\n## Core Claims (3 条)\n\n### Claim 1: Disagreement as High-Precision Diagnostic Signal\nWhen the same LLM formalizes a reasoning problem into two distinct representations (FOL/Z3 and executable Python), disagreements occur at a substantial rate (~40%) and are diagnostically informative with high precision (~87%). This cross-representation signal detects formalization-specific errors invisible to within-representation verification.\n\n**MVP evidence**: C1=39.6% disagree rate, C2=86.8% diagnostic rate on FOLIO (204 samples, Qwen3-32B).\n\n### Claim 2: Accurate Error Localization and Classification\nDisagreement patterns enable automatic error localization (identifying which representation contains the error) with high accuracy (~85%), and error type classification into a structured taxonomy (≥3 distinct types). The 9:1 asymmetry (FOL almost always correct, Code almost always erroneous) itself reveals fundamental differences in how LLMs handle formal logic vs. imperative code generation.\n\n**MVP evidence**: C5=85.4% localization accuracy, C3=3 error types. FOL:Code error ratio 9:1.\n\n### Claim 3: Characterizing the Boundary of Diagnosis-Guided Repair\nWe systematically characterize when cross-representation diagnosis enables effective targeted repair vs. when correlated failures limit repair gains. Targeted repair shows modest improvement over blind regeneration in All-mode (+5.2pp), but the advantage concentrates on specific sample subsets (GT=Unknown). This boundary characterization — distinguishing formalization-specific errors (catchable) from specification-level errors (producing false agreement) — is itself a contribution to understanding neurosymbolic failure modes.\n\n**MVP evidence**: C4 All-mode +5.2pp, Excl-Unknown +0.0pp. Unknown samples drive the repair delta.\n\n## Story Spine\n\n- **Problem**: Neurosymbolic reasoning pipelines suffer from formalization errors as their dominant failure mode. The LLM's translation from natural language to formal representation introduces subtle corruptions. Current approaches either select one representation (HybridMind, Adaptive Selection), verify within one representation (VeriCoT, VERGE, Roundtrip Verification), or filter disagreeing solutions without diagnosis (Liang et al. 2024, Prove 2024). The gap: nobody uses cross-representation disagreement patterns for error CATEGORIZATION and TARGETED REPAIR.\n\n- **Existing approaches & gaps**: Liang et al. (2024) proved CoT-PoT disagreement is informative for filtering but stopped at discarding disagreements — no error categorization, no repair. Roundtrip Verification (2026) showed diagnosis-guided repair works within a single representation on a narrow domain (150 traffic rules). No method exploits cross-representation disagreement as a diagnostic signal enabling categorized diagnosis and targeted repair.\n\n- **Our framing (dual-track)**: We present (1) the first systematic empirical analysis of cross-representation disagreement patterns in neurosymbolic reasoning — characterizing disagreement rates, error types, localization accuracy, and failure mode boundaries across domains and models; and (2) a lightweight diagnosis-guided repair framework that operates at inference time without model modification. The analysis is the primary contribution; the repair framework demonstrates downstream utility.\n\n- **Headline result template**: \"On [benchmarks], cross-representation disagreement detects [X]% of samples as potentially erroneous with [Y]% diagnostic precision and [Z]% error localization accuracy. We characterize a fundamental asymmetry: [logic representation] exhibits [N]x lower formalization error rate than [code representation], revealing systematic differences in how LLMs handle formal logic vs. imperative code generation.\"\n\n## Venue Fit\n\n- **EMNLP fit (strong)**: NLP + symbolic reasoning is a core track. Dual-track framing (systematic analysis + method) aligns with EMNLP's tradition of accepting empirical analyses. The correlated failure / boundary characterization angle fits EMNLP's emphasis on rigorous evaluation.\n- **Risk**: modest repair improvement → mitigate by framing analysis as primary contribution, repair as secondary.\n- **Risk**: single model+dataset insufficient → extend to ≥2 models and ≥3 benchmarks in research phase.\n\n## Anticipated Reviewer Concerns & Responses\n\n| # | Concern | Response Strategy | Required Experiment |\n|---|---------|-------------------|---------------------|\n| R1 | Single model/dataset — generalization? | Cross-model ablation + multi-benchmark | exp-002, exp-003, exp-004 |\n| R2 | C4 repair improvement marginal | Honest framing + boundary characterization as contribution | exp-005, exp-006 |\n| R3 | Why repair, not just select correct side? | Selection vs repair ablation | exp-007 |\n| R4 | Error taxonomy rule-based, not learned | Deliberate choice for interpretability; taxonomy-guided vs fixed strategy ablation | exp-008 |\n| R5 | FOL 9:1 asymmetry — just FOL-as-verifier? | Test on math domain where asymmetry may differ | exp-004 |\n| R6 | Statistical significance? | Bootstrap CI + Fisher exact test on all metrics | exp-009 |\n| R7 | Correlated failures (Denisov-Blanch 2026) | Explicit quantification + cross-model ablation reduces correlation | exp-002, exp-006 |\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'FOLIO 完整分析（MVP 数据深度挖掘）: 基于 204 样本 MVP 数据，完成统计显著性检验、错误类型详细分类、Unknown\n    样本子集分析、repair 前后对比。不需要新实验运行，纯分析。'\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: mvp_pipeline_004\n  status: ANALYZING\n  conclusion: success\n  metrics:\n    progress: 204/204 (deduped from 211)\n    deduped: true\n    dedup_original:\n      all_mode:\n        C1_disagree_rate: 39.6% (76/192)\n        C2_diagnostic_rate: 86.8% (66/76)\n        C3_error_types: 3 types\n        C4_targeted_vs_blind: +6.2pp (T:60/96 B:54/96)\n        C5_localization: 85.4% (35/41)\n        mvp_pass: 5/5 PASS\n      excl_unknown:\n        C1_disagree_rate: 35.7% (45/126)\n        C2_diagnostic_rate: 84.4% (38/45)\n        C3_error_types: 2 types\n        C4_targeted_vs_blind: -1.7pp (T:34/59 B:35/59)\n        C5_localization: 89.3% (25/28)\n        mvp_pass: 4/5 (C4 FAIL)\n    repair_fixed:\n      all_mode:\n        C1_disagree_rate: 39.6% (76/192)\n        C2_diagnostic_rate: 86.8% (66/76)\n        C3_error_types: 3 types\n        C4_targeted_vs_blind: +5.2pp (T:61/96 B:56/96)\n        C5_localization: 85.4% (35/41)\n        mvp_pass: 5/5 PASS\n      excl_unknown:\n        C1_disagree_rate: 35.7% (45/126)\n        C2_diagnostic_rate: 84.4% (38/45)\n        C3_error_types: 2 types\n        C4_targeted_vs_blind: +0.0pp (T:38/59 B:38/59)\n        C5_localization: 89.3% (25/28)\n        mvp_pass: 4/5 (C4 FAIL)\n    final_verdict: All-mode 5/5 PASS (both original and repair)\n- id: exp-002\n  claim:\n  - 1\n  - 2\n  description: '跨模型消融（FOLIO）: DeepSeek V4 Pro 生成一种表征 + Qwen3-32B 生成另一种，测试模型多样性是否降低\n    correlated failures、提升诊断覆盖率。FOLIO 204 样本。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  api_cost_estimate: $15-25 (DeepSeek V4 Pro promotional pricing)\n  status: planned\n- id: exp-003\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'ProofWriter 扩展: 在 ProofWriter 数据集上运行完整 pipeline（双表征+诊断+repair），验证方法在第二个逻辑推理\n    benchmark 上的泛化性。'\n  priority: P0\n  gpu_budget_hours: 6\n  deps: []\n  status: planned\n- id: exp-004\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'MATH Level 5 扩展: 在 MATH 难题子集上运行 pipeline（CoT vs SymPy/Python 双表征），测试跨领域泛化性。数学领域的\n    FOL:Code 不对称性可能不同。'\n  priority: P0\n  gpu_budget_hours: 8\n  deps: []\n  status: planned\n- id: exp-005\n  claim: 3\n  description: 'Repair 机制改进: 多轮 repair（max 3 rounds）、改进 repair prompt（加入错误类型特定的修复策略）、对比\n    repair 前后的 C4 delta。目标：拉大 targeted vs blind 差距。'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  status: planned\n- id: exp-006\n  claim: 3\n  description: 'Unknown 样本深度分析: 为什么 GT=Unknown 样本驱动 C4 delta？分析 Unknown 样本的错误模式分布，是否存在\n    specification-level vs formalization-specific 的系统性差异。'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  status: planned\n- id: exp-007\n  claim: 3\n  description: 'Selection vs Repair 消融: 当检测到分歧且定位了错误侧后，直接选择另一侧答案（selection）vs 诊断引导修复（repair）的对比。回应\n    Reviewer Concern R3。'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  claim: 2\n  description: 'Error Taxonomy 消融: 按错误类型分派修复策略 vs 固定策略（统一重生成），验证 taxonomy 的规定性价值。'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-005\n  status: planned\n- id: exp-009\n  claim:\n  - 1\n  - 2\n  - 3\n  description: '统计显著性全面检验: 对所有 benchmark 的 C1-C5 指标做 bootstrap 95% CI + Fisher exact\n    test / McNemar test，确保所有 claim 有统计支撑。'\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - exp-001\n  - exp-003\n  - exp-004\n  status: planned\n- id: exp-010\n  claim:\n  - 1\n  - 2\n  description: 'Qwen3-8B 消融: 低能力模型上的诊断率和分歧率是否变化？测试方法对模型能力的鲁棒性。'\n  priority: P2\n  gpu_budget_hours: 4\n  deps: []\n  status: planned\n- id: exp-011\n  claim:\n  - 1\n  - 2\n  description: 'GPQA Diamond 扩展: 科学知识推理领域，CoT vs Python 验证代码。'\n  priority: P2\n  gpu_budget_hours: 6\n  deps:\n  - exp-004\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_baseline_001\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    accuracy: 0.74\n    correct: 37\n    total: 50\n    gate: PASS_FOLIO\n- exp_id: mvp_pipeline_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    disagree_rate: 0.04\n    diagnostic_rate: 1\n    error_types: 4\n    targeted_repair: 0.1875\n    blind_repair: 0.4688\n    delta_pp: -28.12\n    localization: 0.4186\n    fol_accuracy: 0.14\n    code_accuracy: 0.52\n    C1: false\n    C2: true\n    C3: true\n    C4: false\n    C5: false\n- exp_id: mvp_pipeline_002\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    fol_crash_rate_v2: 0.1\n    code_crash_rate_v2: 0.4\n    fol_crash_rate_v3: 0.8\n    code_crash_rate_v3: 0\n    fol_accuracy_v3: 0.2\n    code_accuracy_v3: 0.6\n    oracle_accuracy_v3: 0.6\n    disagree_rate_v3: 0\n    effective_disagree_rate_v3: 0\n    diagnostic_rate_v3: null\n    targeted_rate_v3: 0.5\n    blind_rate_v3: 0.625\n    delta_pp_v3: -12.5\n    localization_accuracy_v3: 0.5\n    error_types_v3: 3\n    C1_v3: false\n    C2_v3: false\n    C3_v3: true\n    C4_v3: false\n    C5_v3: false\n    avg_time_per_sample_s_v3: 218.5\n    total_api_calls_v3: 48\n    input_tokens_v3: 50558\n    output_tokens_v3: 139706\n    samples_v3: 10\n    v3_changes: enable_thinking=False for Code generation, _strip_thinking unclosed\n      tag handling\n- exp_id: mvp_pipeline_003\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_003b\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: mvp_pipeline_004\n  name: ''\n  status: ANALYZING\n  conclusion: success\n  metrics:\n    progress: 204/204 (deduped from 211)\n    deduped: true\n    dedup_original:\n      all_mode:\n        C1_disagree_rate: 39.6% (76/192)\n        C2_diagnostic_rate: 86.8% (66/76)\n        C3_error_types: 3 types\n        C4_targeted_vs_blind: +6.2pp (T:60/96 B:54/96)\n        C5_localization: 85.4% (35/41)\n        mvp_pass: 5/5 PASS\n      excl_unknown:\n        C1_disagree_rate: 35.7% (45/126)\n        C2_diagnostic_rate: 84.4% (38/45)\n        C3_error_types: 2 types\n        C4_targeted_vs_blind: -1.7pp (T:34/59 B:35/59)\n        C5_localization: 89.3% (25/28)\n        mvp_pass: 4/5 (C4 FAIL)\n    repair_fixed:\n      all_mode:\n        C1_disagree_rate: 39.6% (76/192)\n        C2_diagnostic_rate: 86.8% (66/76)\n        C3_error_types: 3 types\n        C4_targeted_vs_blind: +5.2pp (T:61/96 B:56/96)\n        C5_localization: 85.4% (35/41)\n        mvp_pass: 5/5 PASS\n      excl_unknown:\n        C1_disagree_rate: 35.7% (45/126)\n        C2_diagnostic_rate: 84.4% (38/45)\n        C3_error_types: 2 types\n        C4_targeted_vs_blind: +0.0pp (T:38/59 B:38/59)\n        C5_localization: 89.3% (25/28)\n        mvp_pass: 4/5 (C4 FAIL)\n    final_verdict: All-mode 5/5 PASS (both original and repair)\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-15T06:05:23.299Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T06:05:23.299Z",
  "sessionId": "607eee2a-7f6d-409d-b311-c0419e42790d"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-15T06:05:23.326Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：诊断信号跨 benchmark/模型稳健泛化，repair 改进经 exp-005 提升至可独立 claim 水平，MATH 域展现不同不对称模式丰富叙事
核心假设：['C1 disagree rate 在 ProofWriter/MATH 上保持 30%+ (方法非 FOLIO 特异)', 'C2 diagnostic precision 跨 benchmark 均 ≥80%', 'exp-005 多轮+类型特定 repair 将 C4 delta 拉至 ≥8pp (All-mode)，Excl-Unknown 也转正 (≥3pp)', 'exp-002 跨模型消融降低 correlated failures，false agreement rate 下降 ≥5pp', 'MATH 域 FOL:Code 不对称性显著不同 (≤3:1)，提供跨域对比叙事', '所有 C1-C5 主指标 bootstrap 95% CI 不跨零，p<0.05']
关键指标范围：{'C1_disagree_rate_cross_bench': [0.3, 0.5], 'C2_diagnostic_precision_cross_bench': [0.8, 0.92], 'C4_targeted_vs_blind_delta_pp_all_mode': [8.0, 15.0], 'C4_targeted_vs_blind_delta_pp_excl_unknown': [3.0, 8.0], 'C5_localization_accuracy_cross_bench': [0.82, 0.92], 'cross_model_false_agreement_reduction_pp': [5.0, 12.0], 'MATH_fol_code_error_ratio': [1.5, 3.0], 'benchmarks_with_5of5_pass': [3, 3]}
叙事方向：原始 dual-track framing 完全成立。三 benchmark 一致验证诊断信号的高精度和跨域泛化性；repair 改进足以作为独立贡献而非仅 downstream utility 展示；MATH 域不对称性差异深化 'LLM 对不同形式化范式的系统性差异' 叙事。Claims 1-3 均无需降级，直投 EMNLP Main。

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
  "promptId": "4a68d131-ac32-430b-b30d-18dfb652377a",
  "type": "user",
  "uuid": "05e3f611-f214-4350-9551-bf47fb3b8b04",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "607eee2a-7f6d-409d-b311-c0419e42790d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-15T06:05:23.325Z_

```json
{
  "parentUuid": "05e3f611-f214-4350-9551-bf47fb3b8b04",
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
  "uuid": "961daa79-d64f-4c89-8d30-a39689476dae",
  "timestamp": "2026-05-15T06:05:23.325Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "607eee2a-7f6d-409d-b311-c0419e42790d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-15T06:05:23.325Z_

```json
{
  "parentUuid": "961daa79-d64f-4c89-8d30-a39689476dae",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b8ac40c7-133b-43b3-9951-93591b8e0b79",
  "timestamp": "2026-05-15T06:05:23.325Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "607eee2a-7f6d-409d-b311-c0419e42790d",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：诊断信号跨 benchmark/模型稳健泛化，repair 改进经 exp-005 提升至可独立 claim 水平，MATH 域展现不同不对称模式丰富叙事 核心假设：['C1 disagree rate 在 ProofWriter/MATH 上保持 30%+ (方法非 FOLIO 特异)', 'C2 diag…",
  "leafUuid": "b8ac40c7-133b-43b3-9951-93591b8e0b79",
  "sessionId": "607eee2a-7f6d-409d-b311-c0419e42790d"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-representation disagreement diagnosis and repair",
  "sessionId": "607eee2a-7f6d-409d-b311-c0419e42790d"
}
```

---

### Assistant

_source line 8 · 2026-05-15T06:05:41.470Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each planned experiment in the experiment plan, under the "best" tier assumptions. I need to produce a YAML block with the specified format.

Let me carefully review:

1. The "best" tier definition with its key metric ranges and narrative
2. Each planned experiment (exp-001 through exp-011)
3. exp-001 is already completed with actual data

Let me think through each experiment's predicted results under the "best" tier:

**exp-001**: Already done. Actual data available.

**exp-002** (Cross-model ablation on FOLIO): DeepSeek V4 Pro + Qwen3-32B. 
Under "best", cross-model should reduce correlated failures, false agreement rate drops ≥5pp. Disagree rate might increase slightly (different models disagree more), diagnostic precision stays high.

**exp-003** (ProofWriter): Full pipeline on ProofWriter. Under "best", disagree rate 30%+, diagnostic precision ≥80%, repair delta should be positive.

**exp-004** (MATH Level 5): Different domain. FOL:Code asymmetry should be notably different (≤3:1 ratio instead of 9:1). Disagree rate 30%+.

**exp-005** (Repair improvement): Multi-round repair cycles should compound gains, repair delta ≥15pp, disagree rate stays around 25-30%.

**exp-006** (Unknown sample analysis): Pure analysis to distinguish specification-level failures from formalization-specific issues.

**exp-007** (Selection vs Repair ablation): Repair should outperform pure selection by a meaningful margin.

**exp-008** (Error taxonomy ablation): Taxonomy-guided approach beats fixed strategy.

**exp-009** (Statistical significance): All confidence intervals exclude zero with p<0.05.

**exp-010** (Qwen3-8B): Method generalizes to lower-capability models, though with different performance characteristics.

**exp-011** (GPQA Diamond): Testing whether the approach extends to science domains.

Now I'm laying out detailed predictions for each experiment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b8ac40c7-133b-43b3-9951-93591b8e0b79",
  "isSidechain": false,
  "requestId": "req_011Cb3rJvVqSve3GQKqhhGVa",
  "type": "assistant",
  "uuid": "47b46840-fe32-4e11-91a4-90aae5d76dec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "607eee2a-7f6d-409d-b311-c0419e42790d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AQUHLVLbs2YoTcUDrAfoXw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10950,
      "cache_read_input_tokens": 11841,
      "output_tokens": 12606,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10950,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 12606,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10950,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10950
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

_source line 9 · 2026-05-15T06:09:22.022Z_

```yaml
tier: best
narrative_guidance: >
  原始 dual-track framing 完全成立。三 benchmark 一致验证诊断信号的高精度和跨域泛化性；
  exp-005 多轮+类型特定 repair 将 C4 delta 拉至可独立 claim 水平；
  MATH 域 FOL:Code 不对称性显著不同于 FOLIO/ProofWriter，深化"LLM 对不同形式化范式的系统性差异"叙事。
  Claims 1-3 均无需降级，直投 EMNLP Main。

imagined_experiments:
  - name: "FOLIO 完整分析（MVP 深度挖掘）"
    plan_id: "exp-001"
    description: "基于 204 样本 MVP 数据的统计分析、错误分类、Unknown 子集分析。已完成。"
    expected_results:
      C1_disagree_rate_all: "39.6% (76/192)"
      C2_diagnostic_rate_all: "86.8% (66/76)"
      C3_error_types: 3
      C4_targeted_vs_blind_all: "+5.2pp (T:61/96 B:56/96)"
      C4_targeted_vs_blind_excl_unknown: "+0.0pp (T:38/59 B:38/59)"
      C5_localization: "85.4% (35/41)"
      FOL_Code_error_ratio: "9:1"
      mvp_pass_all: "5/5 PASS"
      mvp_pass_excl_unknown: "4/5 (C4 FAIL)"
    result_rationale: >
      实际已完成实验。数据直接取自 mvp_pipeline_004 registry。All-mode 全部通过；
      Excl-Unknown 的 C4 failure 是已知弱点，将由 exp-005 repair 改进和 exp-006 深度分析共同解决。
      9:1 FOL:Code 不对称反映 Qwen3-32B 在 FOLIO 逻辑域的 FOL 生成能力远强于 Code 生成能力。
    tables:
      - name: "Table 1: FOLIO Diagnostic Pipeline Results (Qwen3-32B, N=192)"
        columns: ["Metric", "All-mode", "Excl-Unknown"]
        rows:
          - ["C1 Disagree Rate", "39.6% (76/192)", "35.7% (45/126)"]
          - ["C2 Diagnostic Precision", "86.8% (66/76)", "84.4% (38/45)"]
          - ["C3 Error Types", "3", "2"]
          - ["C4 Targeted vs Blind Δ", "+5.2pp", "+0.0pp"]
          - ["C5 Localization Acc", "85.4% (35/41)", "89.3% (25/28)"]
      - name: "Table 2: FOLIO Error Type Distribution"
        columns: ["Error Type", "Count", "Proportion", "Description"]
        rows:
          - ["Predicate Mapping Error", "~28", "~42%", "NL概念到谓词的映射错误"]
          - ["Quantifier Scope Error", "~22", "~33%", "全称/存在量词作用域错误"]
          - ["Negation Handling Error", "~16", "~24%", "否定逻辑处理不当"]
    figures_description:
      - "Fig 1: FOLIO 分歧样本的错误类型分布饼图 + 各类型的 repair 成功率条形图"
      - "Fig 2: GT=Unknown vs GT={True,False} 样本的 diagnostic/repair 指标对比"
    analysis: >
      FOLIO 基线建立完毕。关键发现：(1) ~40% 分歧率说明双表征分歧不是 corner case 而是系统性现象；
      (2) 87% 诊断精度说明分歧具有高信噪比；(3) 9:1 FOL:Code 不对称说明 LLM 在逻辑域的 FOL 能力远超 Code；
      (4) C4 Excl-Unknown 弱点需要 exp-005 解决。Unknown 样本驱动 repair delta 的原因将由 exp-006 解释。

  - name: "跨模型消融（FOLIO）"
    plan_id: "exp-002"
    description: "DeepSeek V4 Pro 生成一种表征 + Qwen3-32B 另一种，测试模型多样性降低 correlated failures。"
    expected_results:
      C1_disagree_rate_cross_model: "44.3% (85/192)"
      C2_diagnostic_precision_cross_model: "83.5% (71/85)"
      false_agreement_rate_single_model: "18.2%"
      false_agreement_rate_cross_model: "11.5%"
      false_agreement_reduction: "6.7pp"
      correlated_failure_rate_reduction: "~35%"
      C5_localization_cross_model: "81.2%"
      oracle_accuracy_cross_model: "82.8%"
    result_rationale: >
      两个不同模型对同一问题的形式化倾向不同，systematic bias 方向不重叠，
      因此 false agreement（双方都错但碰巧一致）的概率显著下降。分歧率从 39.6% 升至 ~44%
      因为跨模型本身引入更多"合理分歧"；诊断精度略降至 83.5% 因为部分新增分歧来自模型风格差异
      而非真实错误；但 false agreement reduction ≥5pp（从 18.2% 降至 11.5%）是核心收益。
      定位准确率略降因为跨模型时难以归因"哪个模型错了"需要不同的归因策略。
      整体：模型多样性是有效的去相关手段，但单模型方案的简洁性仍有实用价值——
      这为论文提供"推荐的部署配置"讨论。
    tables:
      - name: "Table 3: Single-Model vs Cross-Model Disagreement (FOLIO, N=192)"
        columns: ["Metric", "Single-Model (Qwen3)", "Cross-Model (Qwen3+DSV4)", "Δ"]
        rows:
          - ["Disagree Rate", "39.6%", "44.3%", "+4.7pp"]
          - ["Diagnostic Precision", "86.8%", "83.5%", "-3.3pp"]
          - ["False Agreement Rate", "18.2%", "11.5%", "-6.7pp"]
          - ["Localization Accuracy", "85.4%", "81.2%", "-4.2pp"]
          - ["Oracle Accuracy", "79.2%", "82.8%", "+3.6pp"]
      - name: "Table 4: Correlated Failure Analysis"
        columns: ["Failure Mode", "Single-Model", "Cross-Model"]
        rows:
          - ["Both wrong, same answer (false agree)", "35 samples", "22 samples"]
          - ["Both wrong, different answer (detected)", "8 samples", "18 samples"]
          - ["One correct, one wrong (diagnosed)", "66 samples", "71 samples"]
    figures_description:
      - "Fig 3: Venn diagram — Qwen3 errors vs DeepSeek V4 Pro errors，展示错误重叠度"
      - "Fig 4: False agreement rate 随模型对组合变化的条形图"
    analysis: >
      跨模型消融的核心贡献是量化 correlated failure 的降低。6.7pp false agreement reduction
      直接回应 Reviewer Concern R7（Denisov-Blanch 2026）。诊断精度和定位精度的小幅下降
      是预期内的 trade-off：跨模型引入的一些分歧是"模型风格差异"而非"真实错误"。
      论文叙事：单模型方案已足够强（87% precision），跨模型是进一步去相关的可选增强。

  - name: "ProofWriter 扩展"
    plan_id: "exp-003"
    description: "ProofWriter 数据集完整 pipeline，验证逻辑推理域泛化性。"
    expected_results:
      sample_size: 200
      C1_disagree_rate: "36.8% (71/193)"
      C2_diagnostic_precision: "84.5% (60/71)"
      C3_error_types: 3
      C4_targeted_vs_blind_all: "+6.8pp"
      C4_targeted_vs_blind_excl_unknown: "+2.1pp"
      C5_localization: "83.7%"
      FOL_Code_error_ratio: "7:1"
      mvp_pass: "5/5 PASS"
    result_rationale: >
      ProofWriter 是规则式逻辑推理，问题结构比 FOLIO 更规整（明确的 facts/rules/query），
      FOL 形式化对 LLM 相对更容易，因此分歧率略低于 FOLIO（36.8% vs 39.6%），
      但仍然稳健地保持在 30%+ 阈值以上。诊断精度 84.5% 略低于 FOLIO 的 86.8%，
      因为 ProofWriter 的推理链更长（depth 3-5），部分分歧涉及推理步骤差异而非纯粹的形式化错误。
      FOL:Code 不对称降至 7:1（从 FOLIO 的 9:1），因为 ProofWriter 的规则结构更适合
      Code 的 if-then 表达。C4 All-mode +6.8pp 略好于 FOLIO 因为 ProofWriter
      的错误模式更可预测，repair prompt 更有效。Excl-Unknown +2.1pp 因为 ProofWriter
      的 Unknown 样本比例低于 FOLIO，更多 repair delta 分散到非 Unknown 样本。
    tables:
      - name: "Table 5: ProofWriter Diagnostic Pipeline Results (Qwen3-32B, N~193)"
        columns: ["Metric", "All-mode", "Excl-Unknown"]
        rows:
          - ["C1 Disagree Rate", "36.8% (71/193)", "33.2% (52/157)"]
          - ["C2 Diagnostic Precision", "84.5% (60/71)", "82.7% (43/52)"]
          - ["C3 Error Types", "3", "3"]
          - ["C4 Targeted vs Blind Δ", "+6.8pp", "+2.1pp"]
          - ["C5 Localization Acc", "83.7%", "85.9%"]
      - name: "Table 6: Cross-Benchmark Comparison (FOLIO vs ProofWriter)"
        columns: ["Metric", "FOLIO", "ProofWriter", "Trend"]
        rows:
          - ["C1 Disagree Rate", "39.6%", "36.8%", "Consistent (30%+)"]
          - ["C2 Diagnostic Precision", "86.8%", "84.5%", "Consistent (80%+)"]
          - ["C5 Localization", "85.4%", "83.7%", "Consistent (80%+)"]
          - ["FOL:Code Error Ratio", "9:1", "7:1", "Slight convergence"]
    figures_description:
      - "Fig 5: ProofWriter 错误类型分布 vs FOLIO 错误类型分布并排对比"
      - "Fig 6: ProofWriter depth-wise disagree rate（推理深度与分歧率关系）"
    analysis: >
      ProofWriter 结果确认诊断信号在第二个逻辑推理 benchmark 上稳健泛化。
      所有核心指标（C1≥30%, C2≥80%, C5≥80%）均保持在 best 档范围内。
      FOL:Code 不对称从 9:1 降至 7:1 是合理的渐变——ProofWriter 的规则结构
      对 Code 表征更友好。C4 略优于 FOLIO 且 Excl-Unknown 转正（+2.1pp），
      预示 exp-005 的改进方向是可行的。

  - name: "MATH Level 5 扩展"
    plan_id: "exp-004"
    description: "MATH 难题子集，CoT vs SymPy/Python 双表征，测试跨域泛化和不对称模式差异。"
    expected_results:
      sample_size: 200
      C1_disagree_rate: "42.1% (80/190)"
      C2_diagnostic_precision: "81.3% (65/80)"
      C3_error_types: 4
      C4_targeted_vs_blind_all: "+7.5pp"
      C4_targeted_vs_blind_excl_unknown: "+5.2pp"
      C5_localization: "82.4%"
      FOL_Code_error_ratio: "2.3:1"
      CoT_accuracy: "58.4%"
      SymPy_accuracy: "67.2%"
      oracle_accuracy: "78.9%"
      mvp_pass: "5/5 PASS"
    result_rationale: >
      MATH 域是最关键的跨域验证。核心差异在于 FOL:Code 不对称性：MATH 中 SymPy/Python
      不再是"弱侧"，数值计算恰恰是 Code 的强项（SymPy 67.2% vs CoT 58.4%），
      因此不对称降至 2.3:1（Code 侧偶尔犯符号操作错误，但远少于 FOLIO 域的逻辑表达错误）。
      分歧率 42.1% 甚至略高于 FOLIO，因为 MATH Level 5 的复杂推理链在 CoT 和 Code
      之间产生更多 divergence。诊断精度降至 81.3% 因为 MATH 的部分分歧来自
      不同但等价的求解路径（如化简程度不同），这些是"假分歧"。新增第 4 种错误类型
      "Computation Error"（CoT 中的计算失误），丰富了 taxonomy。
      C4 Excl-Unknown 表现显著好于 FOLIO（+5.2pp vs +0.0pp），因为 MATH 没有
      Unknown 类别，repair 效果均匀分布。这为"MATH 域更适合 repair"的叙事提供证据。
    tables:
      - name: "Table 7: MATH Level 5 Diagnostic Pipeline Results (Qwen3-32B, N~190)"
        columns: ["Metric", "Value"]
        rows:
          - ["C1 Disagree Rate", "42.1% (80/190)"]
          - ["C2 Diagnostic Precision", "81.3% (65/80)"]
          - ["C3 Error Types", "4 (incl. Computation Error)"]
          - ["C4 Targeted vs Blind Δ", "+7.5pp"]
          - ["C5 Localization Acc", "82.4%"]
          - ["CoT:Code Error Ratio", "2.3:1"]
      - name: "Table 8: Cross-Domain Asymmetry Comparison"
        columns: ["Domain", "Logic-side Acc", "Code-side Acc", "Ratio", "Dominant Side"]
        rows:
          - ["FOLIO (logic)", "FOL 82.3%", "Code 48.7%", "9:1", "FOL dominates"]
          - ["ProofWriter (logic)", "FOL 80.1%", "Code 51.2%", "7:1", "FOL dominates"]
          - ["MATH (math)", "CoT 58.4%", "SymPy 67.2%", "2.3:1 (inverted)", "Code dominates"]
      - name: "Table 9: MATH Error Type Taxonomy"
        columns: ["Error Type", "Count", "Proportion", "Example"]
        rows:
          - ["Variable Mapping Error", "~20", "~31%", "变量符号与问题中概念对应错误"]
          - ["Computation Error", "~18", "~28%", "CoT 中间步骤算术错误"]
          - ["Constraint Omission", "~15", "~23%", "遗漏边界条件或约束"]
          - ["Type Mismatch", "~12", "~18%", "整数/实数域混淆"]
    figures_description:
      - "Fig 7: 三域 FOL:Code 不对称性雷达图，展示不同域中两种表征的相对优势"
      - "Fig 8: MATH 错误类型分布 vs FOLIO/ProofWriter 错误类型分布（Sankey 图或堆叠条形图）"
      - "Fig 9: 分歧率 vs 问题难度（MATH Level 子集按难度分组）"
    analysis: >
      MATH 结果是 best 档叙事的关键支柱。2.3:1 的 CoT:Code 不对称（与 FOLIO 的 9:1 形成鲜明对比）
      证明不对称性不是方法的 artifact 而是反映 LLM 对不同形式化范式的真实能力差异：
      逻辑域中 FOL 远强于 Code，数学域中 Code（SymPy）反而更强。
      这为论文提供核心叙事："不对称模式随域变化，揭示 LLM 形式化能力的系统性结构"。
      诊断指标（C1≥30%, C2≥80%, C5≥80%）跨域一致，确认方法泛化性。
      C4 在 MATH 上表现更好（+7.5pp），部分因为无 Unknown 类别，部分因为
      MATH 的错误更 localized（计算错误比逻辑语义错误更容易修复）。

  - name: "Repair 机制改进"
    plan_id: "exp-005"
    description: "多轮 repair（max 3 rounds）+ 错误类型特定修复策略，目标拉大 C4 delta。"
    expected_results:
      C4_targeted_vs_blind_all_mode_round1: "+5.2pp"
      C4_targeted_vs_blind_all_mode_round2: "+9.4pp"
      C4_targeted_vs_blind_all_mode_round3: "+10.8pp"
      C4_targeted_vs_blind_all_mode_final: "+10.8pp"
      C4_targeted_vs_blind_excl_unknown_round1: "+0.0pp"
      C4_targeted_vs_blind_excl_unknown_round2: "+3.2pp"
      C4_targeted_vs_blind_excl_unknown_round3: "+4.1pp"
      C4_targeted_vs_blind_excl_unknown_final: "+4.1pp"
      type_specific_vs_generic_repair_delta: "+3.6pp"
      repair_convergence_round: 2.3
      targeted_accuracy_all_final: "73.4%"
      blind_accuracy_all_final: "62.6%"
    result_rationale: >
      多轮 repair 的核心逻辑：第 1 轮已有的 +5.2pp baseline 来自"容易修复"的形式化错误；
      第 2 轮加入错误类型特定策略（如 Predicate Mapping Error 用不同 prompt 模板
      vs Quantifier Scope Error），catch 了第 1 轮遗漏的较难错误，delta 跃升至 +9.4pp；
      第 3 轮收益递减（+10.8pp），因为剩余未修复的分歧多为 correlated failure
      或 specification-level 错误，已接近方法天花板。Excl-Unknown 从 +0.0pp
      拉至 +4.1pp 的关键机制：类型特定策略让 repair prompt 更精准地指向错误根因，
      即使在非 Unknown 样本上也能产生有效修复。blind repair 也在多轮中提升（因为多次重试），
      但 targeted 的提升更快，拉大了差距。blind round 3 约 62.6%，targeted 73.4%。
      这满足 best 档的 C4 ≥8pp All-mode 和 ≥3pp Excl-Unknown 要求。
    tables:
      - name: "Table 10: Multi-Round Repair Progression (FOLIO, N=96 disagree pairs)"
        columns: ["Round", "Targeted Acc", "Blind Acc", "Δ (pp)", "Excl-Unk Δ (pp)"]
        rows:
          - ["0 (no repair)", "63.5%", "63.5%", "0", "0"]
          - ["1 (generic)", "66.7%", "61.5%", "+5.2", "+0.0"]
          - ["2 (type-specific)", "71.9%", "62.5%", "+9.4", "+3.2"]
          - ["3 (type-specific)", "73.4%", "62.6%", "+10.8", "+4.1"]
      - name: "Table 11: Repair Success Rate by Error Type"
        columns: ["Error Type", "Generic Repair Rate", "Type-Specific Rate", "Δ"]
        rows:
          - ["Predicate Mapping", "34%", "52%", "+18pp"]
          - ["Quantifier Scope", "28%", "41%", "+13pp"]
          - ["Negation Handling", "22%", "33%", "+11pp"]
    figures_description:
      - "Fig 10: Repair delta vs round 数的折线图（targeted vs blind 两条线，All-mode 和 Excl-Unknown 各一组）"
      - "Fig 11: 各错误类型的 repair 成功率条形图（generic vs type-specific）"
    analysis: >
      exp-005 是将 C4 从"勉强通过"拉至"可独立 claim"的关键实验。多轮+类型特定策略的组合
      将 All-mode delta 从 5.2pp 提升至 10.8pp（best 档要求 ≥8pp），Excl-Unknown 从 0.0pp
      提升至 4.1pp（要求 ≥3pp）。收益主要来自类型特定策略（贡献约 +3.6pp），
      多轮机制贡献约 +2pp。第 3 轮后收益趋平，说明方法在 correlated failure 边界处饱和——
      这与 Claim 3 的"boundary characterization"叙事一致。

  - name: "Unknown 样本深度分析"
    plan_id: "exp-006"
    description: "分析 GT=Unknown 样本驱动 C4 delta 的原因，区分 specification-level vs formalization-specific 错误。"
    expected_results:
      unknown_sample_count: 66
      unknown_disagree_rate: "47.0% (31/66)"
      unknown_diagnostic_rate: "90.3% (28/31)"
      unknown_C4_delta: "+9.7pp"
      non_unknown_C4_delta: "+0.0pp (pre-exp-005)"
      specification_level_error_rate_unknown: "12.1%"
      specification_level_error_rate_non_unknown: "31.7%"
      formalization_specific_rate_unknown: "87.9%"
      formalization_specific_rate_non_unknown: "68.3%"
      false_agreement_rate_unknown: "8.2%"
      false_agreement_rate_non_unknown: "22.4%"
    result_rationale: >
      GT=Unknown 样本驱动 C4 delta 的根本原因是双重的：
      (1) Unknown 的正确答案不依赖精确推理链——只需证明"信息不足"即可，因此
      formalization-specific error 更容易修复（repair 只需纠正形式化而非推理逻辑）；
      (2) Unknown 样本的 false agreement rate 极低（8.2% vs non-Unknown 22.4%），
      因为两种表征很难在"信息不足"这个结论上碰巧一致地犯错——要么双方都正确返回 Unknown，
      要么至少一方给出了具体答案从而暴露分歧。
      相比之下，non-Unknown 样本的 specification-level error 占比高达 31.7%——
      即问题理解本身就有偏差，导致两种表征犯同一方向的错误，repair 无效。
      这个分析直接支撑 Claim 3 的 boundary characterization：
      方法的天花板由 specification-level error（correlated failure 的根源）决定。
    tables:
      - name: "Table 12: Unknown vs Non-Unknown Error Mode Distribution"
        columns: ["Error Mode", "Unknown (N=66)", "Non-Unknown (N=126)"]
        rows:
          - ["Formalization-specific", "87.9%", "68.3%"]
          - ["Specification-level", "12.1%", "31.7%"]
          - ["False Agreement Rate", "8.2%", "22.4%"]
          - ["Disagree Rate", "47.0%", "35.7%"]
          - ["C4 Repair Δ", "+9.7pp", "+0.0pp (pre-005)"]
      - name: "Table 13: Why Unknown Samples Are More Repairable"
        columns: ["Factor", "Explanation", "Evidence"]
        rows:
          - ["Lower spec-level errors", "Unknown 答案不需精确推理链", "Spec-error 12.1% vs 31.7%"]
          - ["Lower false agreement", "难以在 'Unknown' 上碰巧一致犯错", "FA rate 8.2% vs 22.4%"]
          - ["Higher disagree rate", "更多样本进入诊断流水线", "47.0% vs 35.7%"]
    figures_description:
      - "Fig 12: Error mode 分布对比（Unknown vs Non-Unknown 堆叠条形图）"
      - "Fig 13: False agreement 产生机制的流程图/决策树"
    analysis: >
      此分析解答了 MVP 阶段最关键的未解问题。结论清晰：Unknown 样本的高可修复性源于
      低 specification-level error rate 和低 false agreement rate 的双重优势。
      这不是方法的缺陷而是其边界条件的特征——specification-level error 是方法天花板。
      此发现为 Claim 3 提供了因果解释，比单纯报告"Unknown 驱动 delta"更有说服力。

  - name: "Selection vs Repair 消融"
    plan_id: "exp-007"
    description: "检测分歧+定位错误侧后，直接选择另一侧 vs 诊断引导修复的对比。"
    expected_results:
      selection_accuracy_all: "71.9%"
      repair_accuracy_all: "73.4%"
      repair_vs_selection_delta: "+1.5pp"
      selection_accuracy_localization_correct: "85.4%"
      selection_accuracy_localization_wrong: "14.6%"
      repair_accuracy_localization_wrong: "38.5%"
      oracle_selection_accuracy: "86.8%"
    result_rationale: >
      Selection 策略在定位正确时等价于 oracle selection（直接选对的那一侧），
      因此其准确率上限由 C5 定位精度（85.4%）决定。当定位正确时 selection 直接得到正确答案（85.4%）；
      当定位错误时 selection 选了错的一侧（14.6% 情况下反而更差）。
      Repair 策略的优势在于：即使定位错误（选了"正确侧"去修，实际它也有问题），
      repair 过程仍有概率改善该侧的答案（38.5% 的错误定位案例中 repair 仍有效）。
      因此 repair 以 +1.5pp 小幅胜出 selection。但更重要的定性结论是：
      repair 提供了诊断信息（错误类型、修复建议），这些信息本身有独立价值
      （可用于模型改进、数据增强），而 selection 只是黑箱选择。
      论文叙事：repair 不仅在准确率上略优，更提供了 selection 无法给出的可解释性。
    tables:
      - name: "Table 14: Selection vs Repair Comparison (FOLIO, post-exp-005)"
        columns: ["Strategy", "All-mode Acc", "When Loc Correct", "When Loc Wrong"]
        rows:
          - ["Baseline (no action)", "63.5%", "-", "-"]
          - ["Selection (pick other side)", "71.9%", "85.4%", "14.6%"]
          - ["Repair (diagnose+fix)", "73.4%", "84.1%", "38.5%"]
          - ["Oracle Selection", "86.8%", "100%", "-"]
    figures_description:
      - "Fig 14: Selection vs Repair 在不同定位准确率区间的表现对比"
    analysis: >
      Selection 是一个强 baseline——当定位准确时直接选择更简单且几乎等效。
      Repair 的优势在两处：(1) 定位错误时 repair 仍可能修复（+1.5pp 整体优势的来源）；
      (2) repair 过程产出的诊断报告（错误类型、位置、建议）有可解释性价值。
      回应 R3：repair 不仅是"为何不直接选？"的答案，更是连接 Claim 2（分类）和
      Claim 3（修复）的桥梁——分类信息只有通过 repair prompt 才能转化为行动。

  - name: "Error Taxonomy 消融"
    plan_id: "exp-008"
    description: "按错误类型分派修复策略 vs 固定策略（统一重生成），验证 taxonomy 的规定性价值。"
    expected_results:
      taxonomy_guided_repair_accuracy: "73.4%"
      fixed_strategy_repair_accuracy: "69.8%"
      taxonomy_vs_fixed_delta: "+3.6pp"
      taxonomy_guided_per_type:
        predicate_mapping: "52%"
        quantifier_scope: "41%"
        negation_handling: "33%"
      fixed_strategy_per_type:
        predicate_mapping: "36%"
        quantifier_scope: "30%"
        negation_handling: "24%"
    result_rationale: >
      不同错误类型有不同的最佳修复策略：Predicate Mapping Error 需要重新对齐 NL 概念
      与谓词名称（提供 NL-to-predicate 对照表更有效），Quantifier Scope Error 需要
      显式列出量词作用域（提供 scope disambiguation prompt），Negation Handling 需要
      逐步展开否定逻辑（chain-of-negation prompt）。固定策略（统一"请修复这个表达式"）
      无法利用这些类型特定信息，因此在每种类型上都表现更差。
      +3.6pp 的总体提升证明 taxonomy 不仅是描述性的分类工具，更具有规定性价值——
      错误分类直接指导修复策略选择。这回应了 R4 关于 rule-based taxonomy 的质疑。
    tables:
      - name: "Table 15: Taxonomy-Guided vs Fixed Strategy Repair"
        columns: ["Error Type", "Taxonomy-Guided", "Fixed Strategy", "Δ"]
        rows:
          - ["Predicate Mapping", "52%", "36%", "+16pp"]
          - ["Quantifier Scope", "41%", "30%", "+11pp"]
          - ["Negation Handling", "33%", "24%", "+9pp"]
          - ["Overall", "73.4%", "69.8%", "+3.6pp"]
    figures_description:
      - "Fig 15: 各错误类型下 taxonomy-guided vs fixed 的 repair 成功率对比"
    analysis: >
      Taxonomy 的规定性价值通过每种错误类型 +9~16pp 的提升得到验证。
      Predicate Mapping Error 受益最大（+16pp），因为该类型的修复最依赖
      精确的 NL-to-predicate 对齐信息。这支撑论文的 Claim 2：
      错误分类不仅用于理解，更直接赋能修复。

  - name: "统计显著性全面检验"
    plan_id: "exp-009"
    description: "所有 benchmark 的 C1-C5 指标做 bootstrap 95% CI + 假设检验。"
    expected_results:
      FOLIO_C1_CI: "[33.2%, 46.1%]"
      FOLIO_C2_CI: "[78.4%, 93.1%]"
      FOLIO_C4_CI_all: "[4.2pp, 17.4pp]"
      FOLIO_C5_CI: "[73.1%, 93.8%]"
      ProofWriter_C1_CI: "[30.1%, 43.5%]"
      ProofWriter_C2_CI: "[75.2%, 91.6%]"
      ProofWriter_C5_CI: "[75.8%, 90.1%]"
      MATH_C1_CI: "[35.4%, 48.9%]"
      MATH_C2_CI: "[72.1%, 88.7%]"
      MATH_C5_CI: "[74.2%, 89.1%]"
      all_CIs_exclude_zero: true
      all_p_values_below_05: true
      C4_McNemar_p_all: 0.008
      C4_McNemar_p_excl_unknown: 0.031
      cross_bench_heterogeneity_I2: "18.3%"
    result_rationale: >
      样本量 ~200 per benchmark 在二项比例估计下提供足够的统计功效。
      以 C1 disagree rate 39.6% 为例，N=192 的 95% Wilson CI 约为 [33%, 46%]，
      下界远高于零（30% 阈值也在 CI 内）。C2 86.8% 的 CI 约为 [78%, 93%]，
      下界高于 80% 阈值。C4 all-mode post-exp-005 的 10.8pp delta 对应
      McNemar p≈0.008，Excl-Unknown 4.1pp 对应 p≈0.031——均显著。
      跨 benchmark 的 I² 异质性统计量 18.3% 表明低异质性，
      即三个 benchmark 上的效应量一致。所有指标的 bootstrap 95% CI 不跨零，
      p<0.05——满足 best 档的统计显著性要求。
    tables:
      - name: "Table 16: Bootstrap 95% CI Summary (All Benchmarks)"
        columns: ["Metric", "FOLIO", "ProofWriter", "MATH", "Cross-Bench"]
        rows:
          - ["C1 Disagree Rate", "[33.2, 46.1]%", "[30.1, 43.5]%", "[35.4, 48.9]%", "All >30%"]
          - ["C2 Diagnostic Prec", "[78.4, 93.1]%", "[75.2, 91.6]%", "[72.1, 88.7]%", "All >70%"]
          - ["C4 Δ (All, post-005)", "[4.2, 17.4]pp", "[2.8, 11.2]pp", "[3.1, 12.3]pp", "All >0"]
          - ["C5 Localization", "[73.1, 93.8]%", "[75.8, 90.1]%", "[74.2, 89.1]%", "All >70%"]
      - name: "Table 17: Hypothesis Tests"
        columns: ["Test", "Statistic", "p-value", "Significant?"]
        rows:
          - ["C4 All-mode McNemar (FOLIO)", "χ²=7.04", "p=0.008", "Yes"]
          - ["C4 Excl-Unknown McNemar (FOLIO)", "χ²=4.65", "p=0.031", "Yes"]
          - ["C1 cross-bench Cochran Q", "Q=1.82", "p=0.402", "No (homogeneous)"]
          - ["Cross-bench heterogeneity I²", "18.3%", "-", "Low heterogeneity"]
    figures_description:
      - "Fig 16: 所有指标的 bootstrap CI forest plot（三 benchmark 并排）"
      - "Fig 17: C4 delta 的 bootstrap 分布直方图（标注零线）"
    analysis: >
      统计显著性检验确认所有核心 claim 在 p<0.05 水平成立。CI 不跨零，
      跨 benchmark 异质性低（I²=18.3%），说明效应在三个域上一致。
      C4 Excl-Unknown 的 p=0.031 是最接近阈值的指标，但仍然显著。

  - name: "Qwen3-8B 消融"
    plan_id: "exp-010"
    description: "低能力模型 Qwen3-8B 上测试诊断方法的鲁棒性。"
    expected_results:
      C1_disagree_rate: "48.2%"
      C2_diagnostic_precision: "79.3%"
      C5_localization: "78.8%"
      FOL_Code_error_ratio: "5:1"
      FOL_accuracy: "71.4%"
      Code_accuracy: "39.2%"
      oracle_accuracy: "74.1%"
    result_rationale: >
      低能力模型（8B vs 32B）的形式化质量整体下降，但影响不对称：Code 生成受影响更大
      （39.2% vs 32B 的 ~49%），FOL 生成也下降但较少（71.4% vs ~82%）。
      因此分歧率升高至 48.2%——更多样本出现双方不一致。诊断精度略降至 79.3%
      因为 8B 模型产出的噪声更多，部分分歧来自随机错误而非系统性形式化偏差。
      这个结果对论文叙事是积极的：方法在低能力模型上仍然有效（诊断精度 ~79%），
      且分歧率更高意味着诊断机会更多——方法对更弱模型的"需要修复的空间"更大。
    tables:
      - name: "Table 18: Model Capability Ablation (FOLIO)"
        columns: ["Metric", "Qwen3-32B", "Qwen3-8B", "Trend"]
        rows:
          - ["C1 Disagree Rate", "39.6%", "48.2%", "↑ (more errors)"]
          - ["C2 Diagnostic Precision", "86.8%", "79.3%", "↓ (more noise)"]
          - ["C5 Localization", "85.4%", "78.8%", "↓ (harder to localize)"]
          - ["FOL Accuracy", "~82%", "71.4%", "↓"]
          - ["Code Accuracy", "~49%", "39.2%", "↓↓"]
          - ["FOL:Code Ratio", "9:1", "5:1", "↓ (both degrade)"]
    figures_description:
      - "Fig 18: 模型能力 vs 诊断指标的散点图（8B vs 32B 两点，可扩展为趋势线）"
    analysis: >
      8B 消融确认方法对模型能力有合理的 graceful degradation。核心指标不跌破实用阈值。
      FOL:Code 不对称从 9:1 降至 5:1 说明弱模型的 FOL 优势缩小但仍存在。
      此结果放入 appendix 或 analysis section，支撑"方法不过度依赖特定模型能力"的论述。

  - name: "GPQA Diamond 扩展"
    plan_id: "exp-011"
    description: "科学知识推理域（GPQA Diamond），CoT vs Python 验证代码。"
    expected_results:
      sample_size: 150
      C1_disagree_rate: "38.5%"
      C2_diagnostic_precision: "76.2%"
      C5_localization: "74.8%"
      CoT_accuracy: "42.1%"
      Code_accuracy: "35.8%"
      FOL_Code_error_ratio: "1.5:1"
    result_rationale: >
      GPQA Diamond 是最难的 benchmark（人类专家 ~65%），两种表征的准确率都较低。
      分歧率 38.5% 与其他域一致（方法域无关性的进一步证据）。
      诊断精度降至 76.2%——低于 80% 阈值——因为 GPQA 的科学推理错误
      更多来自知识缺失而非形式化偏差，双方的错误模式更相关。
      FOL:Code 不对称降至 1.5:1，接近对称——CoT 和 Code 在科学域的能力差距最小。
      此实验作为 P2 优先级，主要放在 appendix 或 AAAI 扩展版。
      诊断精度未达 80% 不影响核心三 benchmark 的结论，
      反而提供了方法局限性的诚实讨论素材。
    tables:
      - name: "Table 19: GPQA Diamond Results (Qwen3-32B, N~150)"
        columns: ["Metric", "Value", "vs Other Benchmarks"]
        rows:
          - ["C1 Disagree Rate", "38.5%", "Consistent"]
          - ["C2 Diagnostic Precision", "76.2%", "Below threshold (knowledge-limited)"]
          - ["C5 Localization", "74.8%", "Below threshold"]
          - ["CoT:Code Ratio", "1.5:1", "Most symmetric"]
    figures_description:
      - "Fig 19: 四域诊断指标雷达图（FOLIO/ProofWriter/MATH/GPQA）"
    analysis: >
      GPQA 结果诚实地展示方法边界：当错误来源从"形式化偏差"转向"知识缺失"时，
      诊断精度下降。这与 Claim 3 的 boundary characterization 一致——
      方法在 formalization-specific error 占主导的域（逻辑、数学）最有效，
      在 knowledge-level error 占主导的域（科学 QA）效果减弱。
      对核心 EMNLP 投稿：三 benchmark 足以支撑 claims，GPQA 作为 limitation 讨论或 AAAI 扩展材料。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47b46840-fe32-4e11-91a4-90aae5d76dec",
  "isSidechain": false,
  "requestId": "req_011Cb3rJvVqSve3GQKqhhGVa",
  "type": "assistant",
  "uuid": "a086b4bb-2b8a-4c88-aede-34118908ad0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3",
  "sessionId": "607eee2a-7f6d-409d-b311-c0419e42790d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AQUHLVLbs2YoTcUDrAfoXw",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10950,
      "cache_read_input_tokens": 11841,
      "output_tokens": 12606,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10950,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 12606,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10950,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10950
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：诊断信号跨 benchmark/模型稳健泛化，repair 改进经 exp-005 提升至可独立 claim 水平，MATH 域展现不同不对称模式丰富叙事 核心假设：['C1 disagree rate 在 ProofWriter/MATH 上保持 30%+ (方法非 FOLIO 特异)', 'C2 diag…",
  "leafUuid": "a086b4bb-2b8a-4c88-aede-34118908ad0d",
  "sessionId": "607eee2a-7f6d-409d-b311-c0419e42790d"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-representation disagreement diagnosis and repair",
  "sessionId": "607eee2a-7f6d-409d-b311-c0419e42790d"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：诊断信号跨 benchmark/模型稳健泛化，repair 改进经 exp-005 提升至可独立 claim 水平，MATH 域展现不同不对称模式丰富叙事 核心假设：['C1 disagree rate 在 ProofWriter/MATH 上保持 30%+ (方法非 FOLIO 特异)', 'C2 diag…",
  "leafUuid": "a086b4bb-2b8a-4c88-aede-34118908ad0d",
  "sessionId": "607eee2a-7f6d-409d-b311-c0419e42790d"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Cross-representation disagreement diagnosis and repair",
  "sessionId": "607eee2a-7f6d-409d-b311-c0419e42790d"
}
```

---
