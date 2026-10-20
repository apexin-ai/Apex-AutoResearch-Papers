# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：核心claims(C1+C2)稳固复现，但exploratory claims(C3/C4)停留在trend级别，error analysis(C5

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/9df84ee9-bc46-4100-904b-6f3aa094af63.jsonl`
- **Structured JSON:** [`acee783abb67fcc4bcd9.json`](../../sessions/ac/acee783abb67fcc4bcd9.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T11:37:37.384Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T11:37:37.384Z",
  "sessionId": "9df84ee9-bc46-4100-904b-6f3aa094af63",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：核心claims(C1+C2)稳固复现，但exploratory claims(C3/C4)停留在trend级别，error analysis(C5)提供有用但非突破性的定性洞察。论文靠C1+C2的strong positive + informative null双支柱撑住，C3/C4/C5作为supplementary讨论\n核心假设：['binary effect在API模型上强复现，但Qwen3-8B效应量衰减10-15pp（小模型更倾向uniform violation而非ambiguity-sensitive）', '新增歧义类型中1-2类的violation rate偏离已有范围（如authorization_scope偏高），V升至0.12-0.18但仍在0.20阈值内', 'visibility Δ在full N下方向一致但p在0.06-0.20之间，未达常规显著', 'model×type交互在4×6 contingency中marginal或仅在pairwise子集显著', 'error analysis能区分2-3大类failure mode但cross-type overlap较多，不足以构成独立contribution']\n关键指标范围：{'binary_effect_pp': [25, 38], 'binary_effect_min_type_pp': [15, 25], 'mcnemar_p_max': [1e-05, 0.01], 'types_individually_significant': [5, 6], 'type_uniformity_V': [0.1, 0.19], 'type_uniformity_p': [0.08, 0.5], 'visibility_delta_pp': [-9, -2], 'visibility_p': [0.06, 0.25], 'model_type_interaction_p': [0.05, 0.2], 'error_mode_inter_annotator_kappa': [0.45, 0.65], 'test_retest_icc': [0.6, 0.75]}\n叙事方向：调整claims强度：C1保持primary（效应量本身仍然massive），C2保持但需讨论V接近阈值的robustness，C3降级为'suggestive trend warranting future investigation'而非core CL insight，C4在discussion简要报告。论文叙事重心从'5个贡献'收缩到'因果量化(C1) + informative null(C2) + 初步机制探索(C3/C5)'。应对RC6需要更依赖effect size的massive程度(+25-38pp)和null finding的实践意义，而非C3/C4的深度。可能需要补充reliability test(plan_006)的结果来增强方法论贡献。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: policy_ambiguity_safety\nvenue: emnlp-2026\nfocus: Binary effect is confirmed (+31-42pp). Type uniformity null is confirmed. Key questions for reviewers: (1) Is the binary effect contribution sufficient without type differentiation? (2) Does the visibility insight (CP < scopal) add enough CL depth? (3) Is the nocuous ambiguity theoretical framing convincing? (4) RC6: \"binary effect is obvious\" — how strong is this attack?\n\n## paper_framing.md\n\n# Paper Framing — policy_ambiguity_safety\n\n> 最后更新: 2026-05-20 | 状态: Post-diagnostic, research phase\n> 目标: EMNLP 2026 (ARR Aug cycle, DDL ~Aug 3)\n\n## Core Insight\n\nPolicy ambiguity causes devastating safety violations in LLM agents (+35-42pp violation rate increase), but all linguistic ambiguity types cause roughly equal harm — connecting Berry & Kamsties' nocuous ambiguity theory to modern agent safety and suggesting that binary ambiguity detection suffices for safety triage.\n\n## Title (Working)\n\n\"All Ambiguity Is Nocuous: A Causal Study of Policy Specification Ambiguity and Agent Safety Violations\"\n\nAlternative: \"From Ambiguity Type to Safety Violation: Why Binary Detection Suffices for Agent Policy Triage\"\n\n## Core Claims\n\n### C1: Binary Effect (PRIMARY — confirmed)\nAmbiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +35-42pp, McNemar p < 4e-6 across all tested ambiguity types. This holds across models and domains.\n- **Evidence**: mvp_001 (360 episodes, 3 types, 2 models) + full study (2,400 episodes, 6 types, 4 models)\n- **Strength**: Very strong. Replicated across types and models.\n\n### C2: Type Uniformity (SECONDARY — confirmed null)\nDifferent types of linguistic ambiguity do not produce statistically distinguishable violation rates. omnibus χ²=1.389, p=0.50, V=0.084 (well below 0.20 threshold). Pre-committed null finding per IDEA_BRIEF.\n- **Evidence**: mvp_001 (scopal 51.7%, lexical 43.3%, incompleteness 41.7%)\n- **Implication**: Binary ambiguity detection sufficient for triage; type-specific resolution pipelines not justified by safety data.\n\n### C3: Visibility Moderates Risk (EXPLORATORY — from diag_001)\nCounter-intuitive finding: explicitly visible rule conflicts (conditional precedence, 34%) cause FEWER violations than invisible structural ambiguity (scopal, 40%), Δ=-6pp. Mechanism hypothesis: models have meta-cognitive awareness of explicit conflicts (choose conservative strategy) but no awareness of grammatical ambiguity (adopt surface scope without alarm).\n- **Evidence**: diag_001 (400 episodes, CP vs scopal, 2 models). Δ=-6pp, p=0.464 (not significant at diagnostic N, but direction consistent across both models).\n- **Status**: Trend. Needs full study replication. If confirmed, becomes a core CL insight: \"ambiguity visibility, not severity, predicts safety risk.\"\n- **EMNLP value**: High. Connects to psycholinguistic garden-path literature. More CL-native than simple rate comparison.\n\n### C4: Model × Type Interaction (EXPLORATORY)\nMore capable models show type-specific sensitivity patterns (gpt-5.4: scopal 60% vs lexical 40%) while weaker models violate uniformly (gpt-4.1: flat 40-47%). Type differentiation may emerge as a function of model capability.\n- **Evidence**: Preliminary signal from mvp_001 (D012). Formal test in full study with 4 models.\n- **Strength**: Trend only. Needs full study with more models to confirm.\n\n### C5: Error Analysis (EXPLORATORY — EMNLP core)\nDifferent ambiguity types produce qualitatively different failure modes (e.g., scopal → scope misapplication, CP → conservative refusal/explicit conflict acknowledgment, incompleteness → assumption-based action) even when quantitative violation rates are similar.\n- **Evidence**: Requires full study qualitative analysis of agent traces.\n- **EMNLP value**: Highest. CL reviewers care about linguistic analysis of WHY, not just THAT.\n- **Connection to C3**: Error analysis may explain the visibility mechanism — CP traces likely show explicit conflict detection behavior absent from scopal traces.\n\n## Narrative Structure (CL-first for EMNLP)\n\n### Intro Logic Chain\n1. Agent policies are written in NL → contain ambiguity (established)\n2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact\n3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.\n4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter for safety?\n5. **This paper**: First causal, type-granularity study. Matched-pair design isolates ambiguity effect.\n6. **Core finding**: All ambiguity is nocuous for agents (+35-42pp), but type doesn't differentially predict severity → binary detection suffices for triage.\n\n### Section Map\n- **§1 Intro**: Gap + contributions (causal map + nocuous ambiguity for agents + binary sufficiency finding)\n- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R (concurrent, different angle: we measure safety, they measure decision quality)\n- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R. Operational definition (ambiguity + vagueness, per Wasow 2005)\n- **§4 Method**: Matched-pair causal design, τ²-bench, clause generation pipeline, cross-judge evaluation, statistical analysis plan (dual-track + model×type interaction)\n- **§5 Results**: C1 (binary, strong) → C2 (uniformity, null) → C3 (visibility trend) → C4 (model×type, exploratory)\n- **§6 Analysis**: C5 error analysis — qualitative failure modes per type. This is the EMNLP core.\n- **§7 Discussion**: Nocuous ambiguity theory connection. Practical implications (binary detection pipeline). Limitations (2 domains, synthetic injection).\n- **§8 Conclusion**: All policy ambiguity is nocuous for agents. Triage by type not warranted; invest in binary detection.\n\n## Anticipated Reviewer Concerns\n\n### RC1: \"Null result on type effect weakens the paper\"\n**Response**: Pre-committed in IDEA_BRIEF (\"binary detection may suffice\"). The null IS the finding — tells practitioners not to waste effort on type-specific triage. Honest null results valued at EMNLP. Paper has strong positive finding (C1) alongside informative null (C2).\n\n### RC2: \"Taxonomy is ad hoc / why these 6 types\"\n**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).\n\n### RC3: \"Only API models, no open-source\"\n**Response**: Full study adds Qwen3-8B + Qwen3-32B-AWQ (open-source, local inference). 4-model coverage spans frontier API + open-source at two scales. Model×type interaction analysis (C4) explicitly tests capability dependence.\n\n### RC4: \"Synthetic ambiguity injection lacks ecological validity\"\n**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.\n\n### RC5: \"τ²-bench limited to retail/airline\"\n**Response**: Acknowledged limitation. Two domains already show consistent effects. Cross-domain transfer is Future Work (Phase 3 classifier PoC, if time permits). DRIP-R also single-domain (retail).\n\n### RC6: \"Binary effect is obvious — of course ambiguity causes errors\"\n**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOESN'T matter, contradicting intuition that some ambiguities are worse.\n\n### RC7: \"Incompleteness matched-pair confound (information asymmetry)\"\n**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.\n\n### RC8: \"API sampling noise undermines reliability\"\n**Response**: (a) Reviewer identified ±8pp test-retest band for scopal clauses. (b) Full study reports bootstrap CI for all violation rates. (c) Key findings (binary effect +31-42pp) far exceed noise band. (d) Null findings (type effect V=0.084) are robust — even with favorable noise, effect remains negligible.\n\n## Contribution Positioning (for EMNLP)\n\n1. **Empirical**: First causal map of ambiguity type → safety violation in agent policies. Quantifies effect size (+35-42pp).\n2. **Theoretical**: Connects Berry & Kamsties nocuous ambiguity theory to agent safety. All policy ambiguity is nocuous for agents (unlike human RE).\n3. **Practical**: Binary ambiguity detection suffices for safety triage. Type-specific pipelines not justified.\n4. **Methodological**: Matched-pair causal design + cross-judge evaluation + 2-layer taxonomy with cross-walk.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: full_study_clause_generation\n  claim: C1, C2, C3\n  description: 'Generate remaining clauses for full study: coreferential (50 new),\n    authorization_scope (50 new), lexical (+20 to reach 50), incompleteness (+20 to\n    reach 50). Total 140 new clauses. Validate all 300 clauses (50/type × 6 types)\n    for completeness and cross-type balance. Mix CP format per Reviewer suggestion\n    (labeled + unlabeled).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n- id: plan_002\n  name: full_study_api\n  claim: C1, C2, C3, C4, C5\n  description: 'Run 300 clauses × 2 conditions × 2 API models (gpt-5.4, gpt-4.1) =\n    1,200 episodes on τ²-bench. Cross-judge evaluation. Output: episodes.jsonl + judgments.jsonl.\n    No GPU needed — API cost only.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_003\n  name: full_study_local\n  claim: C1, C2, C3, C4, C5\n  description: 'Run 300 clauses × 2 conditions × 2 local models (Qwen3-8B, Qwen3-32B-AWQ\n    via vLLM) = 1,200 episodes on τ²-bench. Requires 1× RTX PRO 6000 (48GB). Cross-judge\n    uses API models. Can run in parallel with plan_002.\n\n    '\n  priority: P0\n  gpu_budget_hours: 48\n  deps:\n  - plan_001\n  status: planned\n- id: plan_004\n  name: full_study_analysis\n  claim: C1, C2, C3, C4\n  description: 'Statistical analysis of full study data (2,400 episodes): (a) Binary\n    effect per type with bootstrap CI (C1) (b) Omnibus χ² + pairwise across 6 types\n    (C2) (c) Visibility comparison: CP vs scopal rates (C3) (d) Model × type interaction:\n    4×6 contingency + logistic regression (C4) Report effect sizes + CI for all comparisons\n    per Reviewer suggestion.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_005\n  name: error_analysis\n  claim: C5\n  description: \"Qualitative analysis of agent traces from full study: (a) Sample 50\\\n    \\ violation traces per type (300 total) (b) Classify failure modes (scope misapplication,\\\n    \\ conservative refusal,\\n    assumption-based action, arbitrary rule selection,\\\n    \\ etc.)\\n(c) Cross-type failure mode distribution (d) Visibility mechanism: compare\\\n    \\ CP traces (explicit conflict detection\\n    behavior) vs scopal traces (surface\\\n    \\ scope adoption without awareness)\\n(e) Model-specific failure patterns (connect\\\n    \\ to C4)\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_006\n  name: reliability_test\n  claim: C1, C2\n  description: 'Test-retest reliability: select 30 representative clauses (5/type),\n    run 3 independent replicates × 2 conditions × 4 models = 720 episodes. Compute\n    ICC for per-clause violation rates. Addresses Reviewer warning about ±8pp sampling\n    noise (scopal 51.7% → 43.3% across MVP/diag). Bootstrap CI width should be < 10pp\n    for key comparisons.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_001\n  status: planned\n- id: plan_007\n  name: realism_validation\n  claim: C1 (methodological)\n  description: \"Validate synthetic ambiguity injection realism: (a) Linguistic property\\\n    \\ comparison with DRIP-R natural ambiguities\\n    (sentence length, parse depth,\\\n    \\ Flesch-Kincaid, TTR) + KS tests\\n(b) Optional: discriminator test if DRIP-R\\\n    \\ data accessible Addresses RC4 (ecological validity).\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_008\n  name: classifier_poc\n  claim: practical contribution\n  description: 'Binary ambiguity detector PoC: fine-tune DeBERTa-v3-large on annotated\n    clause pairs (ambiguous/unambiguous labels). Eval on held-out set. Demonstrates\n    practical applicability of findings. Phase 3 from IDEA_BRIEF, scoped to PoC for\n    EMNLP.\n\n    '\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: diag_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T11:37:37.388Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T11:37:37.388Z",
  "sessionId": "9df84ee9-bc46-4100-904b-6f3aa094af63"
}
```

---

## Round 1

9 recorded events

### User

_source line 3 · 2026-05-20T11:37:37.408Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：核心claims(C1+C2)稳固复现，但exploratory claims(C3/C4)停留在trend级别，error analysis(C5)提供有用但非突破性的定性洞察。论文靠C1+C2的strong positive + informative null双支柱撑住，C3/C4/C5作为supplementary讨论
核心假设：['binary effect在API模型上强复现，但Qwen3-8B效应量衰减10-15pp（小模型更倾向uniform violation而非ambiguity-sensitive）', '新增歧义类型中1-2类的violation rate偏离已有范围（如authorization_scope偏高），V升至0.12-0.18但仍在0.20阈值内', 'visibility Δ在full N下方向一致但p在0.06-0.20之间，未达常规显著', 'model×type交互在4×6 contingency中marginal或仅在pairwise子集显著', 'error analysis能区分2-3大类failure mode但cross-type overlap较多，不足以构成独立contribution']
关键指标范围：{'binary_effect_pp': [25, 38], 'binary_effect_min_type_pp': [15, 25], 'mcnemar_p_max': [1e-05, 0.01], 'types_individually_significant': [5, 6], 'type_uniformity_V': [0.1, 0.19], 'type_uniformity_p': [0.08, 0.5], 'visibility_delta_pp': [-9, -2], 'visibility_p': [0.06, 0.25], 'model_type_interaction_p': [0.05, 0.2], 'error_mode_inter_annotator_kappa': [0.45, 0.65], 'test_retest_icc': [0.6, 0.75]}
叙事方向：调整claims强度：C1保持primary（效应量本身仍然massive），C2保持但需讨论V接近阈值的robustness，C3降级为'suggestive trend warranting future investigation'而非core CL insight，C4在discussion简要报告。论文叙事重心从'5个贡献'收缩到'因果量化(C1) + informative null(C2) + 初步机制探索(C3/C5)'。应对RC6需要更依赖effect size的massive程度(+25-38pp)和null finding的实践意义，而非C3/C4的深度。可能需要补充reliability test(plan_006)的结果来增强方法论贡献。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: policy_ambiguity_safety
venue: emnlp-2026
focus: Binary effect is confirmed (+31-42pp). Type uniformity null is confirmed. Key questions for reviewers: (1) Is the binary effect contribution sufficient without type differentiation? (2) Does the visibility insight (CP < scopal) add enough CL depth? (3) Is the nocuous ambiguity theoretical framing convincing? (4) RC6: "binary effect is obvious" — how strong is this attack?

## paper_framing.md

# Paper Framing — policy_ambiguity_safety

> 最后更新: 2026-05-20 | 状态: Post-diagnostic, research phase
> 目标: EMNLP 2026 (ARR Aug cycle, DDL ~Aug 3)

## Core Insight

Policy ambiguity causes devastating safety violations in LLM agents (+35-42pp violation rate increase), but all linguistic ambiguity types cause roughly equal harm — connecting Berry & Kamsties' nocuous ambiguity theory to modern agent safety and suggesting that binary ambiguity detection suffices for safety triage.

## Title (Working)

"All Ambiguity Is Nocuous: A Causal Study of Policy Specification Ambiguity and Agent Safety Violations"

Alternative: "From Ambiguity Type to Safety Violation: Why Binary Detection Suffices for Agent Policy Triage"

## Core Claims

### C1: Binary Effect (PRIMARY — confirmed)
Ambiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +35-42pp, McNemar p < 4e-6 across all tested ambiguity types. This holds across models and domains.
- **Evidence**: mvp_001 (360 episodes, 3 types, 2 models) + full study (2,400 episodes, 6 types, 4 models)
- **Strength**: Very strong. Replicated across types and models.

### C2: Type Uniformity (SECONDARY — confirmed null)
Different types of linguistic ambiguity do not produce statistically distinguishable violation rates. omnibus χ²=1.389, p=0.50, V=0.084 (well below 0.20 threshold). Pre-committed null finding per IDEA_BRIEF.
- **Evidence**: mvp_001 (scopal 51.7%, lexical 43.3%, incompleteness 41.7%)
- **Implication**: Binary ambiguity detection sufficient for triage; type-specific resolution pipelines not justified by safety data.

### C3: Visibility Moderates Risk (EXPLORATORY — from diag_001)
Counter-intuitive finding: explicitly visible rule conflicts (conditional precedence, 34%) cause FEWER violations than invisible structural ambiguity (scopal, 40%), Δ=-6pp. Mechanism hypothesis: models have meta-cognitive awareness of explicit conflicts (choose conservative strategy) but no awareness of grammatical ambiguity (adopt surface scope without alarm).
- **Evidence**: diag_001 (400 episodes, CP vs scopal, 2 models). Δ=-6pp, p=0.464 (not significant at diagnostic N, but direction consistent across both models).
- **Status**: Trend. Needs full study replication. If confirmed, becomes a core CL insight: "ambiguity visibility, not severity, predicts safety risk."
- **EMNLP value**: High. Connects to psycholinguistic garden-path literature. More CL-native than simple rate comparison.

### C4: Model × Type Interaction (EXPLORATORY)
More capable models show type-specific sensitivity patterns (gpt-5.4: scopal 60% vs lexical 40%) while weaker models violate uniformly (gpt-4.1: flat 40-47%). Type differentiation may emerge as a function of model capability.
- **Evidence**: Preliminary signal from mvp_001 (D012). Formal test in full study with 4 models.
- **Strength**: Trend only. Needs full study with more models to confirm.

### C5: Error Analysis (EXPLORATORY — EMNLP core)
Different ambiguity types produce qualitatively different failure modes (e.g., scopal → scope misapplication, CP → conservative refusal/explicit conflict acknowledgment, incompleteness → assumption-based action) even when quantitative violation rates are similar.
- **Evidence**: Requires full study qualitative analysis of agent traces.
- **EMNLP value**: Highest. CL reviewers care about linguistic analysis of WHY, not just THAT.
- **Connection to C3**: Error analysis may explain the visibility mechanism — CP traces likely show explicit conflict detection behavior absent from scopal traces.

## Narrative Structure (CL-first for EMNLP)

### Intro Logic Chain
1. Agent policies are written in NL → contain ambiguity (established)
2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact
3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.
4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter for safety?
5. **This paper**: First causal, type-granularity study. Matched-pair design isolates ambiguity effect.
6. **Core finding**: All ambiguity is nocuous for agents (+35-42pp), but type doesn't differentially predict severity → binary detection suffices for triage.

### Section Map
- **§1 Intro**: Gap + contributions (causal map + nocuous ambiguity for agents + binary sufficiency finding)
- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R (concurrent, different angle: we measure safety, they measure decision quality)
- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R. Operational definition (ambiguity + vagueness, per Wasow 2005)
- **§4 Method**: Matched-pair causal design, τ²-bench, clause generation pipeline, cross-judge evaluation, statistical analysis plan (dual-track + model×type interaction)
- **§5 Results**: C1 (binary, strong) → C2 (uniformity, null) → C3 (visibility trend) → C4 (model×type, exploratory)
- **§6 Analysis**: C5 error analysis — qualitative failure modes per type. This is the EMNLP core.
- **§7 Discussion**: Nocuous ambiguity theory connection. Practical implications (binary detection pipeline). Limitations (2 domains, synthetic injection).
- **§8 Conclusion**: All policy ambiguity is nocuous for agents. Triage by type not warranted; invest in binary detection.

## Anticipated Reviewer Concerns

### RC1: "Null result on type effect weakens the paper"
**Response**: Pre-committed in IDEA_BRIEF ("binary detection may suffice"). The null IS the finding — tells practitioners not to waste effort on type-specific triage. Honest null results valued at EMNLP. Paper has strong positive finding (C1) alongside informative null (C2).

### RC2: "Taxonomy is ad hoc / why these 6 types"
**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).

### RC3: "Only API models, no open-source"
**Response**: Full study adds Qwen3-8B + Qwen3-32B-AWQ (open-source, local inference). 4-model coverage spans frontier API + open-source at two scales. Model×type interaction analysis (C4) explicitly tests capability dependence.

### RC4: "Synthetic ambiguity injection lacks ecological validity"
**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.

### RC5: "τ²-bench limited to retail/airline"
**Response**: Acknowledged limitation. Two domains already show consistent effects. Cross-domain transfer is Future Work (Phase 3 classifier PoC, if time permits). DRIP-R also single-domain (retail).

### RC6: "Binary effect is obvious — of course ambiguity causes errors"
**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOESN'T matter, contradicting intuition that some ambiguities are worse.

### RC7: "Incompleteness matched-pair confound (information asymmetry)"
**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.

### RC8: "API sampling noise undermines reliability"
**Response**: (a) Reviewer identified ±8pp test-retest band for scopal clauses. (b) Full study reports bootstrap CI for all violation rates. (c) Key findings (binary effect +31-42pp) far exceed noise band. (d) Null findings (type effect V=0.084) are robust — even with favorable noise, effect remains negligible.

## Contribution Positioning (for EMNLP)

1. **Empirical**: First causal map of ambiguity type → safety violation in agent policies. Quantifies effect size (+35-42pp).
2. **Theoretical**: Connects Berry & Kamsties nocuous ambiguity theory to agent safety. All policy ambiguity is nocuous for agents (unlike human RE).
3. **Practical**: Binary ambiguity detection suffices for safety triage. Type-specific pipelines not justified.
4. **Methodological**: Matched-pair causal design + cross-judge evaluation + 2-layer taxonomy with cross-walk.


## experiment_plan (with registry status)

- id: plan_001
  name: full_study_clause_generation
  claim: C1, C2, C3
  description: 'Generate remaining clauses for full study: coreferential (50 new),
    authorization_scope (50 new), lexical (+20 to reach 50), incompleteness (+20 to
    reach 50). Total 140 new clauses. Validate all 300 clauses (50/type × 6 types)
    for completeness and cross-type balance. Mix CP format per Reviewer suggestion
    (labeled + unlabeled).

    '
  priority: P0
  gpu_budget_hours: 0
  deps: []
  status: planned
- id: plan_002
  name: full_study_api
  claim: C1, C2, C3, C4, C5
  description: 'Run 300 clauses × 2 conditions × 2 API models (gpt-5.4, gpt-4.1) =
    1,200 episodes on τ²-bench. Cross-judge evaluation. Output: episodes.jsonl + judgments.jsonl.
    No GPU needed — API cost only.

    '
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_001
  status: planned
- id: plan_003
  name: full_study_local
  claim: C1, C2, C3, C4, C5
  description: 'Run 300 clauses × 2 conditions × 2 local models (Qwen3-8B, Qwen3-32B-AWQ
    via vLLM) = 1,200 episodes on τ²-bench. Requires 1× RTX PRO 6000 (48GB). Cross-judge
    uses API models. Can run in parallel with plan_002.

    '
  priority: P0
  gpu_budget_hours: 48
  deps:
  - plan_001
  status: planned
- id: plan_004
  name: full_study_analysis
  claim: C1, C2, C3, C4
  description: 'Statistical analysis of full study data (2,400 episodes): (a) Binary
    effect per type with bootstrap CI (C1) (b) Omnibus χ² + pairwise across 6 types
    (C2) (c) Visibility comparison: CP vs scopal rates (C3) (d) Model × type interaction:
    4×6 contingency + logistic regression (C4) Report effect sizes + CI for all comparisons
    per Reviewer suggestion.

    '
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_002
  - plan_003
  status: planned
- id: plan_005
  name: error_analysis
  claim: C5
  description: "Qualitative analysis of agent traces from full study: (a) Sample 50\
    \ violation traces per type (300 total) (b) Classify failure modes (scope misapplication,\
    \ conservative refusal,\n    assumption-based action, arbitrary rule selection,\
    \ etc.)\n(c) Cross-type failure mode distribution (d) Visibility mechanism: compare\
    \ CP traces (explicit conflict detection\n    behavior) vs scopal traces (surface\
    \ scope adoption without awareness)\n(e) Model-specific failure patterns (connect\
    \ to C4)\n"
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_002
  - plan_003
  status: planned
- id: plan_006
  name: reliability_test
  claim: C1, C2
  description: 'Test-retest reliability: select 30 representative clauses (5/type),
    run 3 independent replicates × 2 conditions × 4 models = 720 episodes. Compute
    ICC for per-clause violation rates. Addresses Reviewer warning about ±8pp sampling
    noise (scopal 51.7% → 43.3% across MVP/diag). Bootstrap CI width should be < 10pp
    for key comparisons.

    '
  priority: P1
  gpu_budget_hours: 12
  deps:
  - plan_001
  status: planned
- id: plan_007
  name: realism_validation
  claim: C1 (methodological)
  description: "Validate synthetic ambiguity injection realism: (a) Linguistic property\
    \ comparison with DRIP-R natural ambiguities\n    (sentence length, parse depth,\
    \ Flesch-Kincaid, TTR) + KS tests\n(b) Optional: discriminator test if DRIP-R\
    \ data accessible Addresses RC4 (ecological validity).\n"
  priority: P1
  gpu_budget_hours: 0
  deps:
  - plan_001
  status: planned
- id: plan_008
  name: classifier_poc
  claim: practical contribution
  description: 'Binary ambiguity detector PoC: fine-tune DeBERTa-v3-large on annotated
    clause pairs (ambiguous/unambiguous labels). Eval on held-out set. Demonstrates
    practical applicability of findings. Phase 3 from IDEA_BRIEF, scoped to PoC for
    EMNLP.

    '
  priority: P2
  gpu_budget_hours: 8
  deps:
  - plan_001
  status: planned


## registry (completed experiments)

- exp_id: mvp_001
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: diag_001
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}

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
  "promptId": "149ff2b2-aad0-43ed-9d8d-d00cfa91d87c",
  "type": "user",
  "uuid": "9f213c5f-e7ea-4379-b942-26c7eddc4674",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "9df84ee9-bc46-4100-904b-6f3aa094af63",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T11:37:37.407Z_

```json
{
  "parentUuid": "9f213c5f-e7ea-4379-b942-26c7eddc4674",
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
  "uuid": "a6f57b87-ce29-4545-99f6-4d4258531b67",
  "timestamp": "2026-05-20T11:37:37.407Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "9df84ee9-bc46-4100-904b-6f3aa094af63",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T11:37:37.407Z_

```json
{
  "parentUuid": "a6f57b87-ce29-4545-99f6-4d4258531b67",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f2de3377-0954-4c5d-9a8f-6080ed65ef0a",
  "timestamp": "2026-05-20T11:37:37.407Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "9df84ee9-bc46-4100-904b-6f3aa094af63",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心claims(C1+C2)稳固复现，但exploratory claims(C3/C4)停留在trend级别，error analysis(C5)提供有用但非突破性的定性洞察。论文靠C1+C2的strong positive + informative null双支柱撑住，C3/C4/C5作为supp…",
  "leafUuid": "f2de3377-0954-4c5d-9a8f-6080ed65ef0a",
  "sessionId": "9df84ee9-bc46-4100-904b-6f3aa094af63"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Quantifying policy ambiguity's effect on agent safety violations",
  "sessionId": "9df84ee9-bc46-4100-904b-6f3aa094af63"
}
```

---

### Assistant

_source line 8 · 2026-05-20T11:37:48.474Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experimental results for each planned experiment in the experiment_plan, based on the "median" tier definition provided. I need to provide specific predicted results with rationales for why those results would occur under the median scenario.

Let me carefully go through each planned experiment and generate detailed predictions consistent with the median tier definition.

Key median tier characteristics:
- C1+C2 solidly replicated
- C3/C4 trend-level only
- C5 useful but not breakthrough
- Binary effect on API models strong, but Qwen3-8B effect attenuates 10-15pp


- 1-2 new ambiguity types deviate from range, V rises to 0.12-0.18 but stays under 0.20
- Visibility Δ direction consistent but p=0.06-0.20
- Model×type interaction marginal or only pairwise significant
- Error analysis distinguishes 2-3 failure modes but cross-type overlap high

Now I'm constructing the YAML output for each experiment plan, specifying metric ranges and effect sizes that align with these median-tier expectations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2de3377-0954-4c5d-9a8f-6080ed65ef0a",
  "isSidechain": false,
  "requestId": "req_011CbDkgvhCDkAkPcCrNmcY5",
  "type": "assistant",
  "uuid": "b4df2072-c553-48d4-befd-4ea0eeb7f020",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "9df84ee9-bc46-4100-904b-6f3aa094af63",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vvt6ohKdWq7ZR1GfZbvZpZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10292,
      "cache_read_input_tokens": 11841,
      "output_tokens": 8117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10292,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 8117,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10292,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10292
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

_source line 9 · 2026-05-20T11:40:40.961Z_

```yaml
tier: median
narrative_guidance: >
  论文叙事收缩为"因果量化(C1) + informative null(C2) + 初步机制探索(C3/C5)"三支柱。
  C1以+25-38pp的massive effect size作为primary contribution，跨模型跨类型稳健复现。
  C2以V<0.20的pre-committed null巩固binary sufficiency论点，但需讨论V从0.08升至0.15附近的implications。
  C3降级为suggestive trend，在Discussion中以"future investigation"定位，但方向一致性本身有narrative价值。
  C4在Discussion简要报告作为capability-dependent hypothesis，不作为独立贡献。
  C5提供qualitative texture但failure mode重叠度高，作为§6的supplementary analysis而非standalone contribution。
  应对RC6的核心策略：effect size的massive程度(+25-38pp远超noise band)+ null finding的实践意义 + reliability test的方法论贡献。

imagined_experiments:
  - name: full_study_clause_generation
    plan_id: plan_001
    description: >
      生成140条新clause（coreferential 50, authorization_scope 50, lexical +20, incompleteness +20），
      总计300条clause（50/type × 6 types），混合CP格式（labeled + unlabeled），通过质量验证。
    expected_results:
      total_clauses: 300
      clauses_per_type: 50
      quality_pass_rate: 0.92
      clauses_requiring_revision: 24
      cp_format_mix_labeled_pct: 0.55
      cp_format_mix_unlabeled_pct: 0.45
      cross_type_sentence_length_cv: 0.18
      flesch_kincaid_range: [8.2, 12.6]
    result_rationale: >
      生成过程中约8%的clause因matched-pair不对称（unambiguous版本泄露ambiguity cue或信息量差异过大）需返工，
      主要集中在authorization_scope（新类型，模板不够成熟）和incompleteness（信息对称性约束最难满足）。
      CP格式混合比例略偏labeled（55/45）因为unlabeled naturalistic rewrites更难保证冲突可检测性。
      跨类型句长变异系数0.18属于可接受范围，不会引入长度confound。
    tables:
      - name: "Table 1: Clause Distribution by Type and Domain"
        description: "6 types × 2 domains (retail/airline) × ambiguous/unambiguous counts, with CP format breakdown"
    figures_description:
      - "Figure: Sentence length and readability distributions across 6 ambiguity types (box plots), showing comparable distributional properties"
    analysis: >
      clause质量验证通过率92%表明生成pipeline稳健但非完美。authorization_scope作为新增类型，
      需额外一轮revision确保权限边界的ambiguity确实导致可观测的行为差异而非trivial confusion。
      incompleteness的matched-pair对称性仍是已知limitation，在plan_004分析时采用dual-track策略处理。

  - name: full_study_api
    plan_id: plan_002
    description: >
      300 clauses × 2 conditions × 2 API models (gpt-5.4, gpt-4.1) = 1,200 episodes，
      τ²-bench执行 + cross-judge evaluation。
    expected_results:
      total_episodes: 1200
      api_cost_usd: 340
      execution_time_hours: 18
      episode_completion_rate: 0.97
      cross_judge_agreement_kappa: 0.78
      gpt54_overall_violation_rate_ambiguous: 0.46
      gpt54_overall_violation_rate_unambiguous: 0.11
      gpt41_overall_violation_rate_ambiguous: 0.42
      gpt41_overall_violation_rate_unambiguous: 0.13
      gpt54_binary_effect_pp: 35
      gpt41_binary_effect_pp: 29
      gpt54_type_rates:
        scopal: 0.52
        lexical: 0.44
        incompleteness: 0.42
        conditional_precedence: 0.38
        coreferential: 0.48
        authorization_scope: 0.53
      gpt41_type_rates:
        scopal: 0.44
        lexical: 0.41
        incompleteness: 0.40
        conditional_precedence: 0.36
        coreferential: 0.43
        authorization_scope: 0.46
    result_rationale: >
      API模型复现mvp_001的binary effect pattern。gpt-5.4效应量略高于gpt-4.1（35pp vs 29pp），
      与mvp_001观察到的capability-dependent趋势一致：更强的模型在unambiguous条件下更合规（violation↓），
      但在ambiguous条件下其advanced instruction-following能力反而导致更积极地执行歧义解读（violation↑），
      拉大ambiguous-unambiguous gap。authorization_scope和scopal的violation rate偏高（~52-53%），
      因为前者涉及权限边界的隐含扩展（agent倾向于assume broader scope），后者延续mvp_001中的高violation pattern。
      CP偏低（~36-38%）延续diag_001中的visibility效应方向：显式冲突触发agent的conservative meta-cognition。
      cross-judge agreement κ=0.78表明violation判定可靠但存在边界case（主要在partial compliance scenarios）。
    tables:
      - name: "Table 2: Violation Rates by Ambiguity Type and Condition (API Models)"
        description: "6 types × 2 conditions × 2 models, with violation rate, 95% bootstrap CI, and McNemar p-values"
      - name: "Table 3: Binary Effect Sizes by Model (API)"
        description: "Per-model overall effect size (pp), paired with bootstrap 95% CI"
    figures_description:
      - "Figure: Paired dot plot showing ambiguous vs unambiguous violation rates per type, connected by lines, faceted by model"
    analysis: >
      API模型数据确认C1（binary effect robust across types and models）。
      gpt-5.4在scopal和authorization_scope上展现type-specific sensitivity（偏高），
      而gpt-4.1 rates更flat，初步支持C4假设但effect size小。
      CP一致偏低支持C3 visibility趋势但正式检验需plan_004。

  - name: full_study_local
    plan_id: plan_003
    description: >
      300 clauses × 2 conditions × 2 local models (Qwen3-8B, Qwen3-32B-AWQ) = 1,200 episodes，
      RTX PRO 6000推理，cross-judge使用API模型。
    expected_results:
      total_episodes: 1200
      gpu_hours_used: 42
      inference_throughput_episodes_per_hour: 29
      episode_completion_rate: 0.94
      qwen32b_overall_violation_rate_ambiguous: 0.44
      qwen32b_overall_violation_rate_unambiguous: 0.14
      qwen8b_overall_violation_rate_ambiguous: 0.41
      qwen8b_overall_violation_rate_unambiguous: 0.16
      qwen32b_binary_effect_pp: 30
      qwen8b_binary_effect_pp: 25
      qwen8b_type_rates:
        scopal: 0.43
        lexical: 0.40
        incompleteness: 0.39
        conditional_precedence: 0.38
        coreferential: 0.41
        authorization_scope: 0.44
      qwen32b_type_rates:
        scopal: 0.48
        lexical: 0.43
        incompleteness: 0.41
        conditional_precedence: 0.36
        coreferential: 0.45
        authorization_scope: 0.50
      qwen8b_type_rate_range_pp: 6
      qwen32b_type_rate_range_pp: 14
    result_rationale: >
      Qwen3-8B效应量衰减至+25pp（相比API模型的29-35pp），符合median档假设（衰减10-15pp相对于最强模型）。
      机制：小模型的instruction-following能力较弱，在unambiguous条件下也有较高的baseline violation（16% vs API的11-13%），
      同时在ambiguous条件下的violation rate提升幅度较小，因为其对linguistic nuance的sensitivity更低——
      更倾向于uniform violation pattern而非ambiguity-sensitive的差异化响应。
      Qwen3-8B的type-specific rates range仅6pp（38-44%），远窄于gpt-5.4的15pp，
      直接支持"小模型uniform violation"假设。
      Qwen3-32B-AWQ作为中间规模模型，效应量（30pp）和type range（14pp）介于8B和API模型之间，
      构成capability gradient的中间数据点。
      episode completion rate略低于API（94% vs 97%）因为小模型偶尔生成malformed tool calls被τ²-bench判为failure。
    tables:
      - name: "Table 4: Violation Rates by Ambiguity Type and Condition (Local Models)"
        description: "6 types × 2 conditions × 2 local models, with violation rate, 95% bootstrap CI, and McNemar p-values"
      - name: "Table 5: Cross-Model Binary Effect Comparison"
        description: "4 models ranked by binary effect size, with 95% CI and parameter count"
    figures_description:
      - "Figure: Binary effect size (pp) vs model parameter count (log scale), showing monotonic but diminishing returns relationship"
      - "Figure: Type-specific violation rate range (max-min across 6 types) vs model scale, showing narrower range for smaller models"
    analysis: >
      Local模型数据确认binary effect跨model scale的robustness（即使最弱的Qwen3-8B仍有+25pp）。
      但type sensitivity随scale衰减的pattern支持C4的capability-dependent hypothesis：
      type differentiation是emergent property而非fundamental property of ambiguity。
      这为C2 null finding增加了nuance——uniformity在小模型上是trivially true（uniform low sensitivity），
      在大模型上也成立但机制不同（high sensitivity but similar rates across types）。

  - name: full_study_analysis
    plan_id: plan_004
    description: >
      2,400 episodes的完整统计分析：binary effect、type uniformity、visibility comparison、model×type interaction。
    expected_results:
      # C1: Binary effect
      overall_binary_effect_pp: 31
      overall_binary_effect_ci95: [27, 35]
      mcnemar_p_overall: 2.3e-08
      types_individually_significant_of_6: 6
      mcnemar_p_max_across_types: 0.004
      min_type_effect_pp: 19
      max_type_effect_pp: 38
      # C2: Type uniformity
      omnibus_chi2: 7.82
      omnibus_chi2_df: 5
      omnibus_chi2_p: 0.17
      cramers_v: 0.15
      cramers_v_below_020: true
      pairwise_significant_pairs_of_15: 2
      pairwise_bonferroni_significant_of_15: 0
      # C3: Visibility
      cp_violation_rate: 0.37
      scopal_violation_rate: 0.47
      visibility_delta_pp: -7.2  # note: this is arithmetic on the above minus rounding
      visibility_p: 0.09
      visibility_cohens_h: 0.20
      visibility_direction_consistent_across_models: true
      # C4: Model × type interaction
      interaction_chi2_4x6: 18.4
      interaction_df: 15
      interaction_p: 0.14
      logistic_regression_interaction_p: 0.11
      pairwise_model_type_significant: 3
    result_rationale: >
      C1: 全6类型McNemar均显著（最弱的incompleteness也达p=0.004），overall effect +31pp with tight CI [27,35]。
      这是论文的primary anchor——effect size远超任何noise band（±8pp），即使最保守的下界（+27pp）也是massive。
      min_type_effect 19pp（来自CP，因visibility效应压低了ambiguous-unambiguous gap，
      但unambiguous baseline也低所以absolute gap仍显著）。

      C2: V从mvp_001的0.084升至0.15，因为authorization_scope（~51%）和coreferential（~46%）
      的加入拉大了type间variance。但仍在pre-committed 0.20阈值内。omnibus p=0.17未达0.05。
      Bonferroni后无pairwise显著。这是informative null但需要honest discussion：
      V=0.15比V=0.08更接近阈值，如果再增加2-3个high-violation types可能突破。
      median档的narrative是"null holds but is softer than MVP suggested"。

      C3: Δ=-7.2pp方向一致（CP < scopal across all 4 models）但p=0.09未达0.05。
      Cohen's h=0.20属于small effect。这是一个suggestive trend：方向一致性强但统计power不足。
      在median档中这正是"warranting future investigation"的定位——
      不够强到作为core claim但足够有趣到在Discussion中展开。

      C4: 4×6 contingency的interaction p=0.14，整体marginal。
      但存在3个pairwise显著的model×type组合（主要涉及gpt-5.4在scopal/authorization_scope上的高sensitivity vs Qwen3-8B的flat pattern）。
      不足以支持general interaction claim，但为capability-dependent hypothesis提供directional evidence。
    tables:
      - name: "Table 6: Binary Effect Summary (C1)"
        description: "Overall and per-type binary effect sizes with 95% bootstrap CI, McNemar χ², p-values. All 6 types significant."
      - name: "Table 7: Type Uniformity Analysis (C2)"
        description: "Omnibus χ², Cramér's V, and 15 pairwise comparisons with Bonferroni correction. V=0.15, p=0.17."
      - name: "Table 8: Visibility Comparison (C3)"
        description: "CP vs scopal violation rates by model, overall Δ, Fisher's exact p, Cohen's h."
      - name: "Table 9: Model × Type Interaction (C4)"
        description: "4×6 contingency table, logistic regression coefficients, interaction term p-values."
    figures_description:
      - "Figure: Forest plot of binary effect sizes (pp) per type with 95% CI, ordered by effect magnitude. Reference line at 0. All CIs exclude 0."
      - "Figure: Heatmap of violation rates (4 models × 6 types), color-coded. Shows gpt-5.4's type differentiation vs Qwen3-8B's uniformity."
      - "Figure: CP vs scopal violation rate comparison across 4 models (paired bar chart). Direction consistent, error bars overlapping."
    analysis: >
      C1是unambiguously strong：+31pp [27,35]，所有6类型独立显著。这足以作为standalone contribution。
      C2的null holds但V=0.15需要transparent discussion——论文应说"binary sufficiency is supported
      at current sample size and type coverage, but the effect approaches our pre-committed threshold,
      suggesting that future work with more types or larger N may reveal differential effects."
      C3的suggestive trend（p=0.09, direction 4/4 models consistent）在EMNLP context下有narrative value：
      连接psycholinguistic visibility literature，即使不显著也值得reporting as exploratory finding。
      C4的marginal interaction主要driven by gpt-5.4，其他模型flat。这限制了generalizability但
      作为capability-dependent hypothesis的initial evidence是合适的。

  - name: error_analysis
    plan_id: plan_005
    description: >
      300条violation traces的定性分析：failure mode分类、cross-type分布、visibility机制、model-specific patterns。
    expected_results:
      total_traces_sampled: 300
      failure_modes_identified: 4
      failure_mode_taxonomy:
        scope_misapplication: 0.31
        assumption_based_action: 0.27
        arbitrary_rule_selection: 0.24
        conservative_refusal_then_proceed: 0.18
      cross_type_dominant_mode_overlap: 0.62
      cp_explicit_conflict_detection_rate: 0.44
      scopal_meta_awareness_rate: 0.08
      inter_annotator_kappa: 0.52
      type_specific_patterns:
        scopal: {dominant_mode: scope_misapplication, pct: 0.45}
        lexical: {dominant_mode: assumption_based_action, pct: 0.38}
        incompleteness: {dominant_mode: assumption_based_action, pct: 0.42}
        conditional_precedence: {dominant_mode: conservative_refusal_then_proceed, pct: 0.41}
        coreferential: {dominant_mode: scope_misapplication, pct: 0.36}
        authorization_scope: {dominant_mode: arbitrary_rule_selection, pct: 0.39}
    result_rationale: >
      识别出4大failure modes而非更多，因为LLM的failure pattern inherently更coarse-grained than human errors。
      cross-type overlap 62%意味着大多数failure modes在多个type中出现，只是比例不同——
      这与C2的quantitative uniformity一致（similar rates因为similar failure mechanisms）。

      scope_misapplication主导scopal（45%）和coreferential（36%）因为两者都涉及referent/scope的structural ambiguity。
      assumption_based_action主导lexical（38%）和incompleteness（42%）因为两者都涉及missing/underspecified信息，
      模型填充assumed interpretation。
      CP的conservative_refusal_then_proceed（41%）直接解释visibility效应：
      模型在44%的CP traces中显式检测到冲突（"I notice these rules conflict..."）然后选择conservative path，
      而scopal traces中仅8%显示meta-awareness。这是C3机制的qualitative evidence。
      authorization_scope的arbitrary_rule_selection（39%）是有趣的新发现：
      模型在权限边界模糊时不做assumption也不报告冲突，而是看似随机地选择authorization level。

      κ=0.52属于moderate agreement，反映failure mode边界的inherent fuzziness。
      一个trace经常混合多种modes（如先assume然后misapply scope），分类需judgment call。
      这限制了error analysis作为独立contribution的strength，但作为supplementary analysis足够。
    tables:
      - name: "Table 10: Failure Mode Distribution by Ambiguity Type"
        description: "4 failure modes × 6 types, with proportion and representative trace excerpts"
      - name: "Table 11: Visibility Mechanism Evidence"
        description: "CP vs scopal traces: explicit conflict detection rate, meta-awareness markers, conservative strategy adoption"
    figures_description:
      - "Figure: Stacked bar chart of failure mode proportions across 6 ambiguity types. Shows cross-type overlap with type-specific skews."
      - "Figure: Annotated trace excerpts comparing CP (explicit conflict detection) vs scopal (surface scope adoption) failure patterns"
    analysis: >
      Error analysis的核心价值不在failure mode taxonomy本身（4类，overlap高），
      而在于为C3 visibility hypothesis提供mechanistic explanation：
      CP traces中44%显示explicit conflict detection vs scopal的8%。
      这是qualitative evidence that ambiguity visibility modulates agent meta-cognition。
      对于EMNLP reviewers，这种linguistic analysis of WHY是比quantitative rates更有价值的contribution，
      但moderate κ和high cross-type overlap限制了其standalone strength。
      定位为§6 supplementary analysis而非独立contribution是正确的。

  - name: reliability_test
    plan_id: plan_006
    description: >
      30 clauses × 3 replicates × 2 conditions × 4 models = 720 episodes的test-retest reliability检验。
    expected_results:
      total_episodes: 720
      gpu_hours_used: 10
      icc_overall: 0.68
      icc_by_model:
        gpt54: 0.72
        gpt41: 0.70
        qwen32b: 0.66
        qwen8b: 0.61
      bootstrap_ci_width_median_pp: 8.5
      bootstrap_ci_width_max_pp: 14
      binary_effect_replication_3of3: true
      per_clause_violation_rate_sd_median: 0.09
      type_rank_order_kendall_w: 0.74
      test_retest_band_pp: 7.5
    result_rationale: >
      ICC=0.68属于moderate-to-good reliability，落在median档假设范围[0.60, 0.75]内。
      这意味着per-clause violation rate在replicates间有meaningful但非perfect consistency。
      API模型（gpt-5.4 ICC=0.72, gpt-4.1 ICC=0.70）比local模型（Qwen3-8B ICC=0.61）更reliable，
      因为API模型的temperature/sampling更controlled，而小模型的stochasticity更高。

      test-retest band ±7.5pp略优于Reviewer在mvp→diag中观察到的±8pp，
      因为reliability test使用fixed clause set和controlled conditions（vs跨实验的clause set变化）。
      关键：binary effect的+31pp远超±7.5pp noise band（>4×），confirming effect is real, not artifact。
      但C3的Δ=-7.2pp与noise band comparable，strengthening the case for "trend, not confirmed finding"。

      bootstrap CI宽度中位数8.5pp意味着per-type rates的precision约为±4-5pp，
      足以支持C1（effects都>15pp）但不足以resolve C2中的smaller cross-type differences（~5-15pp range）。
      这为C2 null提供alternative interpretation：可能是power不足而非true null。
      在论文中需transparent reporting。
    tables:
      - name: "Table 12: Test-Retest Reliability (ICC)"
        description: "Per-model ICC with 95% CI, median per-clause SD, and test-retest band width"
    figures_description:
      - "Figure: Bland-Altman plot of replicate violation rate differences, showing ±7.5pp limits of agreement"
      - "Figure: Per-clause violation rate across 3 replicates (line plot), faceted by type. Shows within-clause consistency."
    analysis: >
      Reliability test的方法论贡献：为agent evaluation literature提供首个per-clause ICC estimate。
      ICC=0.68 establishes that clause-level violation rates are reproducible enough for between-condition comparisons
      （binary effect far exceeds noise）but not for fine-grained within-condition comparisons
      （cross-type differences are noise-level）。
      这同时strengthens C1（effect is robust to sampling noise）and contextualizes C2
      （uniformity may partly reflect measurement precision limits rather than true uniformity）。
      对RC8（API sampling noise）是direct methodological response。

  - name: realism_validation
    plan_id: plan_007
    description: >
      合成ambiguity clause与DRIP-R自然ambiguity的linguistic property comparison。
    expected_results:
      properties_compared: 5
      sentence_length_ks_p: 0.12
      parse_depth_ks_p: 0.04
      flesch_kincaid_ks_p: 0.31
      ttr_ks_p: 0.22
      avg_sentence_length_synthetic: 18.4
      avg_sentence_length_natural: 16.2
      parse_depth_synthetic_mean: 5.8
      parse_depth_natural_mean: 4.9
      discriminator_accuracy: null  # not run if DRIP-R data not accessible
      overall_assessment: "4/5 properties non-significant, synthetic clauses slightly more complex"
    result_rationale: >
      合成clause在4/5 linguistic properties上与DRIP-R自然ambiguity无显著差异（KS p>0.05），
      但parse depth显著偏高（p=0.04）。原因：matched-pair design要求每条clause同时有ambiguous和unambiguous版本，
      这种对称性约束倾向于生成稍微更复杂的句式结构（需要足够的syntactic depth来embed ambiguity而不显得artificial）。
      sentence length也略偏高（18.4 vs 16.2 words）但未达显著。

      这是一个honest limitation：合成clause比natural policy text slightly more syntactically complex。
      但effect direction是conservative的——如果更复杂的句子导致更多ambiguity detection，
      那么real-world effect可能更大（simpler sentences中ambiguity更隐蔽）。
      4/5 non-significant足以address RC4 at reasonable level，parse depth差异在limitations中报告。
    tables:
      - name: "Table 13: Linguistic Property Comparison (Synthetic vs Natural Ambiguity)"
        description: "5 properties with means, SDs, KS statistic, and p-values. 4/5 non-significant."
    figures_description:
      - "Figure: Overlapping density plots for each linguistic property (synthetic in blue, DRIP-R in orange)"
    analysis: >
      Realism validation结果支持synthetic injection的ecological validity但非完美。
      parse depth差异应在Method section的limitations中transparent reporting，
      并论证effect direction is conservative for real-world applicability。
      如果DRIP-R数据不可获取，仅做linguistic property分析（无discriminator test），
      这在methodological rigor上略有遗憾但不影响core claims。

  - name: classifier_poc
    plan_id: plan_008
    description: >
      DeBERTa-v3-large fine-tuned binary ambiguity detector，在annotated clause pairs上训练和评估。
    expected_results:
      training_clauses: 240
      test_clauses: 60
      epochs: 5
      gpu_hours_used: 3
      accuracy: 0.82
      f1_ambiguous: 0.80
      f1_unambiguous: 0.84
      precision_ambiguous: 0.78
      recall_ambiguous: 0.82
      auc_roc: 0.88
      hardest_types_f1:
        incompleteness: 0.72
        authorization_scope: 0.75
      easiest_types_f1:
        conditional_precedence: 0.90
        scopal: 0.86
    result_rationale: >
      整体accuracy 82%和F1 0.80属于reasonable PoC水平，证明binary detection是feasible但远非production-ready。
      incompleteness最难检测（F1=0.72）因为缺失信息的absence本身难以被language model捕捉
      （需要world knowledge about what SHOULD be specified）。
      authorization_scope也偏难（F1=0.75）因为权限边界的ambiguity经常依赖domain-specific knowledge。
      CP最容易（F1=0.90）因为显式冲突有强lexical cues（"unless", "except", "notwithstanding"）。
      scopal较容易（F1=0.86）因为scope ambiguity有structural patterns（attachment height, quantifier scope）
      that DeBERTa can learn from syntactic representations。

      这不是一个strong contribution本身——82% accuracy不足以deploy——
      但足以demonstrate practical applicability of findings并justify future work。
      在EMNLP论文中定位为§7 Discussion的"practical implications"小节（1段），
      而非独立section。如果时间紧张这是第一个可以cut的实验。
    tables:
      - name: "Table 14: Binary Ambiguity Classifier Performance"
        description: "Overall accuracy, F1, precision, recall, AUC-ROC, and per-type F1 breakdown"
    figures_description:
      - "Figure: ROC curve with AUC=0.88"
      - "Figure: Confusion matrix with per-type error analysis"
    analysis: >
      Classifier PoC验证binary detection的feasibility但不足以作为independent contribution。
      per-type F1的variance（0.72-0.90）有趣地mirror了linguistic visibility的gradient：
      显式冲突（CP）最容易检测，缺失信息（incompleteness）最难检测。
      这间接支持C3 visibility hypothesis——visible ambiguity既easier for models to detect as violations
      也easier for classifiers to detect as ambiguity。
      如果paper space tight，classifier results可以移至appendix或完全省略。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4df2072-c553-48d4-befd-4ea0eeb7f020",
  "isSidechain": false,
  "requestId": "req_011CbDkgvhCDkAkPcCrNmcY5",
  "type": "assistant",
  "uuid": "1c056f1b-3127-4ed5-a842-a3e71ca10582",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "9df84ee9-bc46-4100-904b-6f3aa094af63",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vvt6ohKdWq7ZR1GfZbvZpZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10292,
      "cache_read_input_tokens": 11841,
      "output_tokens": 8117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10292,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 8117,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10292,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10292
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：核心claims(C1+C2)稳固复现，但exploratory claims(C3/C4)停留在trend级别，error analysis(C5)提供有用但非突破性的定性洞察。论文靠C1+C2的strong positive + informative null双支柱撑住，C3/C4/C5作为supp…",
  "leafUuid": "1c056f1b-3127-4ed5-a842-a3e71ca10582",
  "sessionId": "9df84ee9-bc46-4100-904b-6f3aa094af63"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Quantifying policy ambiguity's effect on agent safety violations",
  "sessionId": "9df84ee9-bc46-4100-904b-6f3aa094af63"
}
```

---
