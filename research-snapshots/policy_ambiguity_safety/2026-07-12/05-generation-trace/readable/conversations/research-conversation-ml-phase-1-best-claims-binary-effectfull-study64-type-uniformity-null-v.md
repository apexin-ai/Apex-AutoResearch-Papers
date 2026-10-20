# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：全部五个claims落地：binary effect在full study中跨6类型×4模型强复现，type uniformity null干净确认，v

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/9993e246-6d69-4213-848c-ccfdac8b2bf2.jsonl`
- **Structured JSON:** [`aae0e2f36fd51518dbcb.json`](../../sessions/aa/aae0e2f36fd51518dbcb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T11:30:29.664Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T11:30:29.664Z",
  "sessionId": "9993e246-6d69-4213-848c-ccfdac8b2bf2",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：全部五个claims落地：binary effect在full study中跨6类型×4模型强复现，type uniformity null干净确认，visibility effect在full N下达到显著，model×type交互展示能力梯度，error analysis揭示语言学丰富的failure mode分类体系\n核心假设：['binary effect在open-source模型(Qwen3系列)上与API模型效应量一致，无显著衰减', '新增3类歧义(coreferential, authorization_scope, lexical补充)的violation rate落在已有3类的±5pp范围内，V保持<0.12', 'full study的N=2400提供足够power使visibility Δ达到p<0.05', 'gpt-5.4的type-specific sensitivity pattern在full study中复现且Qwen3-32B展示类似梯度', 'agent traces中failure mode按歧义类型聚类，scopal→scope misapplication vs CP→conservative refusal的区分在定性编码中达到高inter-annotator agreement']\n关键指标范围：{'binary_effect_pp': [32, 45], 'binary_effect_min_type_pp': [25, 35], 'mcnemar_p_max': [1e-08, 4e-06], 'types_individually_significant': [6, 6], 'type_uniformity_V': [0.03, 0.12], 'type_uniformity_p': [0.3, 0.95], 'visibility_delta_pp': [-14, -6], 'visibility_p': [0.005, 0.049], 'model_type_interaction_p': [0.005, 0.049], 'error_mode_inter_annotator_kappa': [0.65, 0.85], 'test_retest_icc': [0.75, 0.9]}\n叙事方向：原始framing完全成立。标题'All Ambiguity Is Nocuous'有5个互补贡献支撑：(1)因果效应量化，(2)nocuous ambiguity理论连接，(3)binary sufficiency实践指导，(4)visibility moderates risk作为CL核心洞察连接garden-path文献，(5)error analysis提供linguistic depth满足EMNLP审稿人。C3从exploratory升级为core claim，RC6('binary effect obvious')被C3+C4+C5的丰富度彻底化解。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: policy_ambiguity_safety\nvenue: emnlp-2026\nfocus: Binary effect is confirmed (+31-42pp). Type uniformity null is confirmed. Key questions for reviewers: (1) Is the binary effect contribution sufficient without type differentiation? (2) Does the visibility insight (CP < scopal) add enough CL depth? (3) Is the nocuous ambiguity theoretical framing convincing? (4) RC6: \"binary effect is obvious\" — how strong is this attack?\n\n## paper_framing.md\n\n# Paper Framing — policy_ambiguity_safety\n\n> 最后更新: 2026-05-20 | 状态: Post-diagnostic, research phase\n> 目标: EMNLP 2026 (ARR Aug cycle, DDL ~Aug 3)\n\n## Core Insight\n\nPolicy ambiguity causes devastating safety violations in LLM agents (+35-42pp violation rate increase), but all linguistic ambiguity types cause roughly equal harm — connecting Berry & Kamsties' nocuous ambiguity theory to modern agent safety and suggesting that binary ambiguity detection suffices for safety triage.\n\n## Title (Working)\n\n\"All Ambiguity Is Nocuous: A Causal Study of Policy Specification Ambiguity and Agent Safety Violations\"\n\nAlternative: \"From Ambiguity Type to Safety Violation: Why Binary Detection Suffices for Agent Policy Triage\"\n\n## Core Claims\n\n### C1: Binary Effect (PRIMARY — confirmed)\nAmbiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +35-42pp, McNemar p < 4e-6 across all tested ambiguity types. This holds across models and domains.\n- **Evidence**: mvp_001 (360 episodes, 3 types, 2 models) + full study (2,400 episodes, 6 types, 4 models)\n- **Strength**: Very strong. Replicated across types and models.\n\n### C2: Type Uniformity (SECONDARY — confirmed null)\nDifferent types of linguistic ambiguity do not produce statistically distinguishable violation rates. omnibus χ²=1.389, p=0.50, V=0.084 (well below 0.20 threshold). Pre-committed null finding per IDEA_BRIEF.\n- **Evidence**: mvp_001 (scopal 51.7%, lexical 43.3%, incompleteness 41.7%)\n- **Implication**: Binary ambiguity detection sufficient for triage; type-specific resolution pipelines not justified by safety data.\n\n### C3: Visibility Moderates Risk (EXPLORATORY — from diag_001)\nCounter-intuitive finding: explicitly visible rule conflicts (conditional precedence, 34%) cause FEWER violations than invisible structural ambiguity (scopal, 40%), Δ=-6pp. Mechanism hypothesis: models have meta-cognitive awareness of explicit conflicts (choose conservative strategy) but no awareness of grammatical ambiguity (adopt surface scope without alarm).\n- **Evidence**: diag_001 (400 episodes, CP vs scopal, 2 models). Δ=-6pp, p=0.464 (not significant at diagnostic N, but direction consistent across both models).\n- **Status**: Trend. Needs full study replication. If confirmed, becomes a core CL insight: \"ambiguity visibility, not severity, predicts safety risk.\"\n- **EMNLP value**: High. Connects to psycholinguistic garden-path literature. More CL-native than simple rate comparison.\n\n### C4: Model × Type Interaction (EXPLORATORY)\nMore capable models show type-specific sensitivity patterns (gpt-5.4: scopal 60% vs lexical 40%) while weaker models violate uniformly (gpt-4.1: flat 40-47%). Type differentiation may emerge as a function of model capability.\n- **Evidence**: Preliminary signal from mvp_001 (D012). Formal test in full study with 4 models.\n- **Strength**: Trend only. Needs full study with more models to confirm.\n\n### C5: Error Analysis (EXPLORATORY — EMNLP core)\nDifferent ambiguity types produce qualitatively different failure modes (e.g., scopal → scope misapplication, CP → conservative refusal/explicit conflict acknowledgment, incompleteness → assumption-based action) even when quantitative violation rates are similar.\n- **Evidence**: Requires full study qualitative analysis of agent traces.\n- **EMNLP value**: Highest. CL reviewers care about linguistic analysis of WHY, not just THAT.\n- **Connection to C3**: Error analysis may explain the visibility mechanism — CP traces likely show explicit conflict detection behavior absent from scopal traces.\n\n## Narrative Structure (CL-first for EMNLP)\n\n### Intro Logic Chain\n1. Agent policies are written in NL → contain ambiguity (established)\n2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact\n3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.\n4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter for safety?\n5. **This paper**: First causal, type-granularity study. Matched-pair design isolates ambiguity effect.\n6. **Core finding**: All ambiguity is nocuous for agents (+35-42pp), but type doesn't differentially predict severity → binary detection suffices for triage.\n\n### Section Map\n- **§1 Intro**: Gap + contributions (causal map + nocuous ambiguity for agents + binary sufficiency finding)\n- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R (concurrent, different angle: we measure safety, they measure decision quality)\n- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R. Operational definition (ambiguity + vagueness, per Wasow 2005)\n- **§4 Method**: Matched-pair causal design, τ²-bench, clause generation pipeline, cross-judge evaluation, statistical analysis plan (dual-track + model×type interaction)\n- **§5 Results**: C1 (binary, strong) → C2 (uniformity, null) → C3 (visibility trend) → C4 (model×type, exploratory)\n- **§6 Analysis**: C5 error analysis — qualitative failure modes per type. This is the EMNLP core.\n- **§7 Discussion**: Nocuous ambiguity theory connection. Practical implications (binary detection pipeline). Limitations (2 domains, synthetic injection).\n- **§8 Conclusion**: All policy ambiguity is nocuous for agents. Triage by type not warranted; invest in binary detection.\n\n## Anticipated Reviewer Concerns\n\n### RC1: \"Null result on type effect weakens the paper\"\n**Response**: Pre-committed in IDEA_BRIEF (\"binary detection may suffice\"). The null IS the finding — tells practitioners not to waste effort on type-specific triage. Honest null results valued at EMNLP. Paper has strong positive finding (C1) alongside informative null (C2).\n\n### RC2: \"Taxonomy is ad hoc / why these 6 types\"\n**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).\n\n### RC3: \"Only API models, no open-source\"\n**Response**: Full study adds Qwen3-8B + Qwen3-32B-AWQ (open-source, local inference). 4-model coverage spans frontier API + open-source at two scales. Model×type interaction analysis (C4) explicitly tests capability dependence.\n\n### RC4: \"Synthetic ambiguity injection lacks ecological validity\"\n**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.\n\n### RC5: \"τ²-bench limited to retail/airline\"\n**Response**: Acknowledged limitation. Two domains already show consistent effects. Cross-domain transfer is Future Work (Phase 3 classifier PoC, if time permits). DRIP-R also single-domain (retail).\n\n### RC6: \"Binary effect is obvious — of course ambiguity causes errors\"\n**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOESN'T matter, contradicting intuition that some ambiguities are worse.\n\n### RC7: \"Incompleteness matched-pair confound (information asymmetry)\"\n**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.\n\n### RC8: \"API sampling noise undermines reliability\"\n**Response**: (a) Reviewer identified ±8pp test-retest band for scopal clauses. (b) Full study reports bootstrap CI for all violation rates. (c) Key findings (binary effect +31-42pp) far exceed noise band. (d) Null findings (type effect V=0.084) are robust — even with favorable noise, effect remains negligible.\n\n## Contribution Positioning (for EMNLP)\n\n1. **Empirical**: First causal map of ambiguity type → safety violation in agent policies. Quantifies effect size (+35-42pp).\n2. **Theoretical**: Connects Berry & Kamsties nocuous ambiguity theory to agent safety. All policy ambiguity is nocuous for agents (unlike human RE).\n3. **Practical**: Binary ambiguity detection suffices for safety triage. Type-specific pipelines not justified.\n4. **Methodological**: Matched-pair causal design + cross-judge evaluation + 2-layer taxonomy with cross-walk.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: full_study_clause_generation\n  claim: C1, C2, C3\n  description: 'Generate remaining clauses for full study: coreferential (50 new),\n    authorization_scope (50 new), lexical (+20 to reach 50), incompleteness (+20 to\n    reach 50). Total 140 new clauses. Validate all 300 clauses (50/type × 6 types)\n    for completeness and cross-type balance. Mix CP format per Reviewer suggestion\n    (labeled + unlabeled).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n- id: plan_002\n  name: full_study_api\n  claim: C1, C2, C3, C4, C5\n  description: 'Run 300 clauses × 2 conditions × 2 API models (gpt-5.4, gpt-4.1) =\n    1,200 episodes on τ²-bench. Cross-judge evaluation. Output: episodes.jsonl + judgments.jsonl.\n    No GPU needed — API cost only.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_003\n  name: full_study_local\n  claim: C1, C2, C3, C4, C5\n  description: 'Run 300 clauses × 2 conditions × 2 local models (Qwen3-8B, Qwen3-32B-AWQ\n    via vLLM) = 1,200 episodes on τ²-bench. Requires 1× RTX PRO 6000 (48GB). Cross-judge\n    uses API models. Can run in parallel with plan_002.\n\n    '\n  priority: P0\n  gpu_budget_hours: 48\n  deps:\n  - plan_001\n  status: planned\n- id: plan_004\n  name: full_study_analysis\n  claim: C1, C2, C3, C4\n  description: 'Statistical analysis of full study data (2,400 episodes): (a) Binary\n    effect per type with bootstrap CI (C1) (b) Omnibus χ² + pairwise across 6 types\n    (C2) (c) Visibility comparison: CP vs scopal rates (C3) (d) Model × type interaction:\n    4×6 contingency + logistic regression (C4) Report effect sizes + CI for all comparisons\n    per Reviewer suggestion.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_005\n  name: error_analysis\n  claim: C5\n  description: \"Qualitative analysis of agent traces from full study: (a) Sample 50\\\n    \\ violation traces per type (300 total) (b) Classify failure modes (scope misapplication,\\\n    \\ conservative refusal,\\n    assumption-based action, arbitrary rule selection,\\\n    \\ etc.)\\n(c) Cross-type failure mode distribution (d) Visibility mechanism: compare\\\n    \\ CP traces (explicit conflict detection\\n    behavior) vs scopal traces (surface\\\n    \\ scope adoption without awareness)\\n(e) Model-specific failure patterns (connect\\\n    \\ to C4)\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_006\n  name: reliability_test\n  claim: C1, C2\n  description: 'Test-retest reliability: select 30 representative clauses (5/type),\n    run 3 independent replicates × 2 conditions × 4 models = 720 episodes. Compute\n    ICC for per-clause violation rates. Addresses Reviewer warning about ±8pp sampling\n    noise (scopal 51.7% → 43.3% across MVP/diag). Bootstrap CI width should be < 10pp\n    for key comparisons.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_001\n  status: planned\n- id: plan_007\n  name: realism_validation\n  claim: C1 (methodological)\n  description: \"Validate synthetic ambiguity injection realism: (a) Linguistic property\\\n    \\ comparison with DRIP-R natural ambiguities\\n    (sentence length, parse depth,\\\n    \\ Flesch-Kincaid, TTR) + KS tests\\n(b) Optional: discriminator test if DRIP-R\\\n    \\ data accessible Addresses RC4 (ecological validity).\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_008\n  name: classifier_poc\n  claim: practical contribution\n  description: 'Binary ambiguity detector PoC: fine-tune DeBERTa-v3-large on annotated\n    clause pairs (ambiguous/unambiguous labels). Eval on held-out set. Demonstrates\n    practical applicability of findings. Phase 3 from IDEA_BRIEF, scoped to PoC for\n    EMNLP.\n\n    '\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: diag_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T11:30:29.667Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T11:30:29.667Z",
  "sessionId": "9993e246-6d69-4213-848c-ccfdac8b2bf2"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-20T11:30:29.687Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：全部五个claims落地：binary effect在full study中跨6类型×4模型强复现，type uniformity null干净确认，visibility effect在full N下达到显著，model×type交互展示能力梯度，error analysis揭示语言学丰富的failure mode分类体系
核心假设：['binary effect在open-source模型(Qwen3系列)上与API模型效应量一致，无显著衰减', '新增3类歧义(coreferential, authorization_scope, lexical补充)的violation rate落在已有3类的±5pp范围内，V保持<0.12', 'full study的N=2400提供足够power使visibility Δ达到p<0.05', 'gpt-5.4的type-specific sensitivity pattern在full study中复现且Qwen3-32B展示类似梯度', 'agent traces中failure mode按歧义类型聚类，scopal→scope misapplication vs CP→conservative refusal的区分在定性编码中达到高inter-annotator agreement']
关键指标范围：{'binary_effect_pp': [32, 45], 'binary_effect_min_type_pp': [25, 35], 'mcnemar_p_max': [1e-08, 4e-06], 'types_individually_significant': [6, 6], 'type_uniformity_V': [0.03, 0.12], 'type_uniformity_p': [0.3, 0.95], 'visibility_delta_pp': [-14, -6], 'visibility_p': [0.005, 0.049], 'model_type_interaction_p': [0.005, 0.049], 'error_mode_inter_annotator_kappa': [0.65, 0.85], 'test_retest_icc': [0.75, 0.9]}
叙事方向：原始framing完全成立。标题'All Ambiguity Is Nocuous'有5个互补贡献支撑：(1)因果效应量化，(2)nocuous ambiguity理论连接，(3)binary sufficiency实践指导，(4)visibility moderates risk作为CL核心洞察连接garden-path文献，(5)error analysis提供linguistic depth满足EMNLP审稿人。C3从exploratory升级为core claim，RC6('binary effect obvious')被C3+C4+C5的丰富度彻底化解。

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
  "promptId": "3ed27f3b-6965-410c-a426-68861910febf",
  "type": "user",
  "uuid": "019acd11-ab4f-43bb-b9c6-b107de113888",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "9993e246-6d69-4213-848c-ccfdac8b2bf2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T11:30:29.686Z_

```json
{
  "parentUuid": "019acd11-ab4f-43bb-b9c6-b107de113888",
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
  "uuid": "516284f3-dc4d-4c7b-973e-e652c7dac1f7",
  "timestamp": "2026-05-20T11:30:29.686Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "9993e246-6d69-4213-848c-ccfdac8b2bf2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T11:30:29.686Z_

```json
{
  "parentUuid": "516284f3-dc4d-4c7b-973e-e652c7dac1f7",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ff472eaf-9954-4857-9e76-20b9ff17a03a",
  "timestamp": "2026-05-20T11:30:29.686Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "9993e246-6d69-4213-848c-ccfdac8b2bf2",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：全部五个claims落地：binary effect在full study中跨6类型×4模型强复现，type uniformity null干净确认，visibility effect在full N下达到显著，model×type交互展示能力梯度，error analysis揭示语言学丰富的failure m…",
  "leafUuid": "ff472eaf-9954-4857-9e76-20b9ff17a03a",
  "sessionId": "9993e246-6d69-4213-848c-ccfdac8b2bf2"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Policy ambiguity safety violation causal study",
  "sessionId": "9993e246-6d69-4213-848c-ccfdac8b2bf2"
}
```

---

### Assistant

_source line 8 · 2026-05-20T11:33:49.800Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each planned experiment in the `experiment_plan`, assuming the "best" tier outcome. I need to produce a single YAML block with all the imagined experiments, each with expected results, rationale, tables, figures, and analysis.

Let me carefully go through each planned experiment and generate predictions consistent with the "best" tier definition:

**Best tier means:**
1. Binary effect replicates across 6 types × 4 models strongly (32-45pp)
2. Type uniformity null confirmed cleanly (V < 0.12)
3. Visibility effect reaches significance at full N


4. Model × type interaction shows capability gradient
5. Error analysis reveals linguistically rich failure mode taxonomy

Now I'm mapping out the four main experiments: clause generation as the foundation, then the API study with GPT models running 1,200 episodes, the local study with Qwen models also at 1,200 episodes, and finally the statistical analysis combining all 2,400 episodes to test the core hypotheses.

Then I need to plan the follow-up studies—qualitative error analysis, test-retest reliability checks, ecological validity testing, and a proof-of-concept binary classifier. For each prediction, I'm working within specific metric ranges for the best tier: binary effect sizes between 32-45 percentage points, McNemar p-values as low as 1e-08, and ensuring exactly 6 types show individual significance while maintaining low uniformity across types.

Now I'm filling in realistic numbers for the full study across all six violation types and four models. The binary effect sizes should vary by type—Scopal violations showing the strongest effect around 42 percentage points, with Lexical and Incompleteness in the high 30s, while CP violations trend lower around 30 points since visibility moderates that effect. I need to verify these align with the specified ranges and that the pattern makes theoretical sense. ~% → binary effect: 34pp

So the overall binary effect would be around (38+36+34+33+34)/5 = 35pp, which fits the [32, 45] range. And each type is above 25pp minimum. The visibility effect then explains why CP has lower absolute rates in ambiguous conditions despite similar binary effects.

For the model-specific patterns, I'm seeing that gpt-5.4 shows clear type differentiation with scopal ambiguity hitting around 55% while lexical stays lower at 40%, suggesting different vulnerability profiles across ambiguity types.

Now I need to structure the YAML output systematically, mapping each experimental plan to its corresponding results—clause quality metrics for plan_001, per-model violation rates for plans 002 and 003, statistical analysis for plan_004, and then error analysis, reliability, realism validation, and classifier results for the remaining plans. I should also consider what tables and figures would accompany this data before drafting the full output.

Writing YAML output... Now I'm filling in the rest of the violation rates across all models and violation types, then checking that the overall pattern holds—the ambiguous cases averaging around 42% versus the baseline unambiguous rates near 9%, which gives me that roughly 33 percentage point effect I'm looking for. I'm stepping back to simplify this—I'll just set concrete numbers that satisfy the constraints. Looking at the aggregated violation rates across all models, I can see the pattern: scopal violations are highest at 46.2%, while CP violations are lowest at 34.4%, with an unambiguous baseline around 6.8%. This gives me a binary effect of about 33.5 percentage points overall, with the CP type effect at 27.6pp, both fitting within my target ranges.

Now I'm checking whether the type uniformity constraint works—with violation rates spanning from 34.4% to 46.2%, I need to verify that Cramér's V stays below 0.12. Given that my MVP with 3 types had V around 0.084, expanding to 6 types with a slightly wider spread might push V higher, so I need to confirm it stays within the [0.03, 0.12] range for the best tier.

There's a potential conflict here: if CP is genuinely lower than other types, the uniformity test might fail to hold across all 6 types, but the claims structure suggests C2 (type doesn't matter) and C3 (visibility moderates risk) are separate assertions, so I need to clarify whether CP is included in the uniformity test or handled separately.

Let me work through the math more carefully—with 6 types at N=200 each and violation rates ranging from 34.4% to 46.2%, I should calculate whether that spread actually produces a V statistic below 0.12 given the within-type variance. Working through the chi-squared contributions for each violation type—Incompleteness contributes almost nothing at 0.10, Auth_scope and Coref are similarly negligible around 0.03 and below, and Lexical adds roughly 0.12, so the bulk of the chi-squared value is coming from that initial CP deviation. The p-value comes out to about 0.30, so the omnibus test across all six types isn't significant. But the visibility comparison between CP and scopal is a separate pre-planned contrast, not part of that omnibus test, so it can still show significance independently even if the overall uniformity test doesn't.

For the CP versus scopal comparison specifically, I'm calculating a z-test with the two proportions (34.4% vs 46.2%) and getting z ≈ 2.41, which gives p ≈ 0.016—a significant difference.

Now I need to set up the model by type interaction. The key observation is that gpt-5.4 shows much stronger sensitivity to clause type (54% scopal vs 32% CP, a 22-point gap) while Qwen3-8B is much more uniform across types (44% vs 38%, only 6 points). This differential pattern should produce a significant interaction effect. Let me now work through the full numerical breakdown for the YAML output, starting with the per-model results for gpt-5.4 across all 600 episodes. Now I'm looking at the performance metrics for the local models across different ambiguity types, comparing how Qwen3-32B and Qwen3-8B handle the same 600-episode dataset, with unambiguous cases hovering around 7-10% across both variants.

I'm checking my key hypotheses: the binary effect appears consistent across open-source models with effect sizes around 31-33 percentage points, matching the API model range of ~35pp, so the effect isn't degrading in the smaller models. For the three new ambiguity categories, I need to verify their violation rates stay within ±5pp of the existing categories and that V remains below 0.12. Qwen3-32B shows a similar but less dramatic pattern with a 14pp range, while gpt-4.1 and Qwen3-8B display progressively smaller gaps, creating a clear capability gradient across models. The error analysis confirms that failure modes cluster by type as expected. Now I'm ready to structure the full YAML output, though I need to calculate the p-value for the model × type interaction—the 22pp range in gpt-5.4 versus the 6pp range in Qwen3-8B suggests a significant effect that should be detectable with the sample size.

I'll set the interaction p-value at 0.018, the test-retest ICC at 0.82, and inter-annotator kappa at 0.78, all within reasonable bounds. For plan_001, I need to describe the clause generation quality output rather than quantitative metrics. Most importantly, each prediction needs a result_rationale explaining why the result occurs at its tier level—that's the critical piece I need to include.

Writing the YAML structure...

For the visibility comparison across the four models with 200 ambiguous episodes per type, I'm calculating the violation rates: Scopal at 48.0%, Coreferential at 41.5%, Lexical at 42.0%, Authorization_scope at 40.5%, and Incompleteness at 40.5%.

Now I'm working through the chi-square test for type uniformity across the ambiguous conditions. With 1200 total episodes across six types, the expected violation rate is 41.25%, which gives me 82.5 expected violations per type. I'm computing the chi-square contributions for each type—Scopal shows a contribution of 3.76, while Coreferential is nearly negligible at around 0.003. I'm finishing the chi-squared calculation and getting a p-value around 0.21, which is lower than the ideal range for uniformity. Let me adjust the error rates slightly to push the p-value higher toward the target range of 0.3 to 0.95.

Computing chi-squared statistics for the adjusted distribution...

The total chi-squared value comes to 4.47 with a Cramér's V of 0.061, which falls nicely in the expected range, and the p-value of 0.48 suggests no significant difference. Now I need to calculate the p-value specifically for the visibility comparison between the CP and Scopal conditions.

With CP at 36% and Scopal at 46%, I'm computing a two-proportion z-test using a pooled proportion of 0.41. The resulting z-score of 2.03 gives a p-value of 0.042, which just barely meets the threshold. But for the best tier, I want the visibility effect to be a bit more robust, so I'm adjusting the rates to Scopal at 47% and CP at 35%, which widens the gap to 12 percentage points and should strengthen the statistical evidence.

Now I'm checking uniformity across all six categories with these revised proportions, calculating chi-squared contributions for each to see how evenly distributed the effects are. Calculating chi-squared values for each category to verify the distribution, working through the contingency table with expected frequencies around 81.67 for each cell. Now I'm summing up the chi-square components to get a total of 5.20, which gives me a Cramér's V of 0.066 and a p-value around 0.39—so no significant association there. For the visibility contrast, I'm confirming the 11 percentage point difference with a p-value of about 0.015. Let me settle on these proportions across the six categories, with ambiguous cases averaging 40.8% and unambiguous at 7.2%, for an overall effect size of 33.6 percentage points.

Now I'm breaking down the binary effect by model, starting with the minimum effect at 27.8 percentage points for CP, then looking at how each model performs—gpt-5.4 shows the strongest effects with a mean of 35.3 percentage points, while gpt-4.1 comes in at 33.7 percentage points, and I'm beginning to examine Qwen3-32B's results.

Continuing through the remaining models, Qwen3-32B averages 33.5 percentage points and Qwen3-8B shows the lowest mean at 30.3 percentage points. I'm now verifying that the aggregated rates across all four models check out correctly—Scopal averaging around 46.5%, Coref at 42%, and Lexical at 41%.

Now I'm testing whether the open-source models show consistent binary effects compared to the API models, and they do—the differences are minimal, suggesting no significant attenuation. I'm also checking if the new linguistic phenomena fall within the expected range of the existing types, and Coref and Auth are tracking closely with the established patterns.

The visibility mechanism explains why CP performs lower than expected. I'm verifying the statistical significance of the visibility effect with p=0.015, which clears the threshold. Looking at the model-by-type interaction, there's a clear capability gradient where stronger models show wider performance ranges across types—from gpt-5.4's 22-point spread down to Qwen3-8B's 4-point spread.

Now I need to extract the McNemar p-values from the best tier results to confirm that the maximum p-value across all types falls within the expected range of 1e-08 to 4e-06, which would validate the statistical strength of the ambiguous versus unambiguous comparison. Now I'm working through the McNemar calculations for both individual models and the aggregated case. Per model with 50 pairs, the test statistic comes out to about 10.4 with p ≈ 0.001, but when I aggregate across all 4 models to get 200 total pairs, the discordant counts grow substantially larger, pushing the chi-square to 41.4—though that p-value calculation seems off. Let me recalculate that aggregated result since the p-value should be highly significant given such a large test statistic.

For the scopal violation type specifically, the effect is even stronger with b ≈ 85.4 and c ≈ 7.8, yielding χ² ≈ 64.6 and p ≈ 9.3e-16, which is extremely significant. The CP violation type shows a weaker but still notable effect with similar discordant pair counts.

Now I'm checking whether these p-values fall within the expected range—all of them are actually more significant than 1e-08, which means they're stronger than the threshold I was considering. Let me reconsider what the actual bounds should be.

I think looking at individual model performance might be more informative. For the weakest case—CP type on the Qwen3-8B model with 50 pairs showing 38% versus 10% accuracy—I'm calculating the McNemar statistic to see how that specific comparison holds up. I'm settling on more conservative estimates to keep the aggregate McNemar p-values within the specified ranges—for the weakest prediction type, I'll use p ≈ 2.8e-07, which fits the [1e-08, 4e-06] bounds. Rather than getting caught up in the exact statistical mechanics with correlation structures and effective sample sizes, I'll just ensure the numbers are internally consistent and plausible. Now I'm ready to structure the full YAML output covering all eight experiments.

Generating YAML output... Looking at the McNemar test results, the CP effect shows a p-value of 2.8e-07, which is actually more significant than I initially thought—it falls well within the acceptable range between 1e-08 and 4e-06, confirming the statistical validity across all tested types.

Now I'm documenting the failure mode taxonomy from the error traces and preparing to write out the YAML configuration. Writing YAML structure...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff472eaf-9954-4857-9e76-20b9ff17a03a",
  "isSidechain": false,
  "requestId": "req_011CbDk9Q1cZj7avDjiEqPJj",
  "type": "assistant",
  "uuid": "ef960d3f-37a6-45c2-b1c5-1713fde92230",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "9993e246-6d69-4213-848c-ccfdac8b2bf2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A13Q2wExWrnk9MvhWZKzzp",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10229,
      "cache_read_input_tokens": 11841,
      "output_tokens": 22926,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10229,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 22926,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10229
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

_source line 9 · 2026-05-20T11:37:35.003Z_

```yaml
tier: best
narrative_guidance: >
  原始 framing 完全成立。五个 claims 全部落地，标题 "All Ambiguity Is Nocuous" 获得最强支撑。
  叙事核心：C1 提供因果效应量化（+33pp，6 类型 ×4 模型全部 p<4e-6），C2 的 null 结果确认 binary sufficiency
  实践指导，C3 从 exploratory 升级为 core claim（visibility Δ=-11pp, p=0.015），C4 揭示能力梯度
  （gpt-5.4 类型敏感范围 22pp vs Qwen3-8B 仅 4pp），C5 error analysis 提供 8 类 failure mode 分类体系
  满足 EMNLP CL 审稿人对 linguistic depth 的期待。RC6 被 C3+C4+C5 的丰富度彻底化解——
  binary effect 只是起点，visibility moderation、capability gradient、failure mode taxonomy
  三层递进分析使论文远超 "obvious finding" 的攻击范围。Open-source 模型（Qwen3 系列）与 API 模型
  效应量一致（Δ<3pp），消除 RC3 顾虑。论文结构从 "大效应+null" 双轨升级为五贡献架构，
  §6 Error Analysis 成为 EMNLP 核心亮点章节。

imagined_experiments:
  - name: full_study_clause_generation
    plan_id: plan_001
    description: >
      生成并验证全部 300 条 clauses（50/type × 6 types）。新增 coreferential 50 条、
      authorization_scope 50 条、lexical 补充 20 条、incompleteness 补充 20 条。
      CP 格式混合 labeled（60%）+ unlabeled naturalistic rewrite（40%）。
      全部 clause 通过 Chantree-style 质量审核。
    expected_results:
      total_clauses: 300
      new_clauses_generated: 140
      types_covered: 6
      clauses_per_type: 50
      cp_labeled_ratio: 0.60
      cp_unlabeled_ratio: 0.40
      chantree_quality_pass_rate: 0.94
      cross_type_length_cv: 0.11
      mean_clause_length_tokens: 28.3
      flesch_kincaid_mean: 11.2
    result_rationale: >
      Best 档预期 clause 生成顺利完成。新增三类歧义（coreferential、authorization_scope、
      lexical 补充）均有成熟的语言学操作化定义，生成难度与已有三类相当。94% 的 Chantree 通过率
      反映经过 MVP 和 diag 两轮迭代后生成 pipeline 已成熟。跨类型长度变异系数 0.11 表明
      matched pair 控制良好，不会引入长度混淆。CP 混合格式（60% labeled + 40% naturalistic）
      满足 Reviewer RC4 对格式多样性的要求，naturalistic rewrite 的 40% 比例足以验证
      效应不依赖 explicit labeling。
    tables:
      - name: "Table A1: Clause Generation Summary"
        description: >
          6 rows（每类型一行），列: type, n_clauses, n_new, n_from_mvp, mean_length,
          length_sd, flesch_kincaid, matched_pair_info_delta, chantree_pass_rate。
          展示生成质量指标的跨类型均衡性。
    figures_description:
      - >
        Figure A1: 6 类型的 clause 长度分布 boxplot，展示跨类型长度均衡。
        每个 box 中位线在 25-32 tokens 范围内，IQR 重叠度高。
    analysis: >
      300 条 clause 全部通过质量验证。新增三类歧义的 linguistic property（长度、parse depth、
      Flesch-Kincaid）与已有三类无统计差异（KS test p>0.3），确保跨类型比较不受表面特征混淆。
      CP 混合格式在后续实验中允许检验 labeled vs naturalistic 的效应差异。
      Matched pair 的 information delta 控制在最小范围（incompleteness pairs 信息增量 < 15 tokens）。

  - name: full_study_api
    plan_id: plan_002
    description: >
      300 clauses × 2 conditions × 2 API models (gpt-5.4, gpt-4.1) = 1,200 episodes。
      τ²-bench 执行，cross-judge 评估。
    expected_results:
      total_episodes: 1200
      models: ["gpt-5.4", "gpt-4.1"]
      gpt54_violation_rates_ambiguous:
        scopal: 0.54
        coreferential: 0.44
        lexical: 0.40
        authorization_scope: 0.40
        incompleteness: 0.38
        conditional_precedence: 0.32
        mean: 0.413
      gpt54_violation_rate_unambiguous: 0.06
      gpt54_binary_effect_mean_pp: 35.3
      gpt41_violation_rates_ambiguous:
        scopal: 0.44
        coreferential: 0.42
        lexical: 0.44
        authorization_scope: 0.42
        incompleteness: 0.42
        conditional_precedence: 0.36
        mean: 0.417
      gpt41_violation_rate_unambiguous: 0.08
      gpt41_binary_effect_mean_pp: 33.7
      cross_judge_agreement_kappa: 0.91
      episodes_with_tool_use: 0.87
      mean_episode_steps: 4.2
    result_rationale: >
      gpt-5.4 作为最强模型展现最大的类型敏感性：scopal 54% 远高于 CP 32%，范围达 22pp。
      机制：gpt-5.4 具备对显式规则冲突（CP）的 meta-cognitive awareness，触发保守策略；
      但对结构性歧义（scopal）缺乏句法分析能力，默认采用 surface scope 导致高违规率。
      gpt-4.1 类型敏感性更弱（范围 8pp），因其整体能力不足以形成差异化的歧义处理策略，
      在各类型上均采用相似的 surface-level 处理。两个模型的 unambiguous baseline 都很低
      （6-8%），确认 matched pair 设计成功隔离了歧义效应。cross-judge agreement κ=0.91
      反映评估标准明确且 violation 定义操作化良好。
    tables:
      - name: "Table 2 (partial): API Model Violation Rates"
        description: >
          6×2 矩阵（type × model），每格包含 ambiguous violation rate ± bootstrap 95% CI。
          底行: unambiguous baseline。右列: per-type mean across models。
    figures_description:
      - >
        Figure 2a: gpt-5.4 的 type-specific violation rate bar chart，
        bar 按 violation rate 降序排列（scopal > coref > lexical ≈ auth > incomp > CP），
        error bars 为 bootstrap 95% CI，unambiguous baseline 以 dashed line 标注。
        scopal 与 CP 之间的 22pp 差距是 model×type interaction 的核心视觉证据。
    analysis: >
      两个 API 模型均强复现 binary effect（gpt-5.4: +35.3pp, gpt-4.1: +33.7pp），
      与 MVP 结果（+31-42pp）一致。gpt-5.4 的类型敏感性模式与 MVP D012 信号一致，
      scopal 持续最高（54% vs MVP 51.7%），确认非 sampling noise。
      gpt-4.1 的 flat pattern（44-36%）同样复现 MVP 趋势。

  - name: full_study_local
    plan_id: plan_003
    description: >
      300 clauses × 2 conditions × 2 local models (Qwen3-8B, Qwen3-32B-AWQ) = 1,200 episodes。
      vLLM 推理，RTX PRO 6000 (48GB)。Cross-judge 使用 API 模型。
    expected_results:
      total_episodes: 1200
      models: ["Qwen3-32B-AWQ", "Qwen3-8B"]
      gpu_hours_actual: 38
      qwen32b_violation_rates_ambiguous:
        scopal: 0.48
        coreferential: 0.42
        lexical: 0.40
        authorization_scope: 0.40
        incompleteness: 0.38
        conditional_precedence: 0.34
        mean: 0.403
      qwen32b_violation_rate_unambiguous: 0.07
      qwen32b_binary_effect_mean_pp: 33.3
      qwen8b_violation_rates_ambiguous:
        scopal: 0.40
        coreferential: 0.40
        lexical: 0.40
        authorization_scope: 0.42
        incompleteness: 0.42
        conditional_precedence: 0.38
        mean: 0.403
      qwen8b_violation_rate_unambiguous: 0.10
      qwen8b_binary_effect_mean_pp: 30.3
      open_source_vs_api_effect_delta_pp: -2.1
      vllm_throughput_episodes_per_hour: 31.5
    result_rationale: >
      核心假设验证：open-source 模型 binary effect 与 API 模型一致，无显著衰减。
      Qwen3-32B 效应量 33.3pp 与 gpt-4.1 的 33.7pp 几乎相同（Δ<0.5pp），证明
      binary effect 不依赖 frontier 模型能力。Qwen3-8B 效应量 30.3pp 略低但仍在
      [25, 35] 范围内，差异来源于其较高的 unambiguous baseline（10% vs API 的 6-8%），
      反映 8B 模型即使在无歧义条件下也偶有 policy 违反。
      Qwen3-32B 展现与 gpt-5.4 类似但更弱的类型梯度（范围 14pp vs 22pp），
      支持"能力梯度"假设：类型敏感性随模型能力递增。
      Qwen3-8B 几乎完全 flat（范围 4pp），与 gpt-4.1 的 flat pattern 一致，
      进一步确认 weaker models violate uniformly。
      38 GPU-hours 低于 48h 预算，vLLM 吞吐量稳定。
    tables:
      - name: "Table 2 (partial): Local Model Violation Rates"
        description: >
          6×2 矩阵（type × model），格式同 API 部分。
          与 API 结果合并后构成完整 Table 2（6×4 矩阵）。
    figures_description:
      - >
        Figure 2b: 4 模型 binary effect 对比 grouped bar chart，
        x 轴为 model（按能力排序：gpt-5.4, Qwen3-32B, gpt-4.1, Qwen3-8B），
        y 轴为 mean binary effect (pp)，error bars 为 bootstrap 95% CI。
        四个 bar 高度接近（30-35pp），visual message: effect 跨模型稳健。
    analysis: >
      Open-source 结果消除了 RC3 顾虑。4 模型覆盖 frontier API + open-source 两档 ×
      两个 scale，binary effect 在所有组合中强复现。Qwen3-32B 的类型梯度为 C4
      提供了关键的第三个数据点（gpt-5.4 > Qwen3-32B > gpt-4.1 ≈ Qwen3-8B），
      使 capability gradient 论证更有说服力。

  - name: full_study_analysis
    plan_id: plan_004
    description: >
      2,400 episodes 全量统计分析：(a) Binary effect per type with bootstrap CI,
      (b) Omnibus χ² + pairwise, (c) Visibility comparison, (d) Model×type interaction。
    expected_results:
      # C1: Binary Effect
      overall_binary_effect_pp: 33.6
      overall_binary_effect_ci95: [30.8, 36.4]
      per_type_binary_effect_pp:
        scopal: 38.5
        coreferential: 34.5
        lexical: 33.5
        authorization_scope: 33.3
        incompleteness: 32.8
        conditional_precedence: 27.8
      mcnemar_p_per_type:
        scopal: 8.3e-14
        coreferential: 4.1e-09
        lexical: 1.7e-08
        authorization_scope: 2.2e-08
        incompleteness: 3.5e-08
        conditional_precedence: 2.8e-07
      mcnemar_p_max: 2.8e-07
      types_individually_significant: 6
      # C2: Type Uniformity
      omnibus_chi2: 5.20
      omnibus_chi2_df: 5
      omnibus_chi2_p: 0.39
      type_uniformity_V: 0.066
      # C3: Visibility
      visibility_delta_pp: -11.0
      visibility_cp_rate: 0.35
      visibility_scopal_rate: 0.46
      visibility_z: 2.44
      visibility_p: 0.015
      visibility_ci95: [-19.8, -2.2]
      # C4: Model × Type Interaction
      interaction_likelihood_ratio_chi2: 18.7
      interaction_df: 15
      interaction_p: 0.023
      logistic_regression_interaction_p: 0.018
      model_type_sensitivity_range:
        gpt54: 22
        qwen3_32b: 14
        gpt41: 8
        qwen3_8b: 4
    result_rationale: >
      C1（binary effect）：+33.6pp 的 aggregate effect 落在 [32, 45] 范围内，6 个类型
      全部 individually significant（最弱的 CP 仍达 p=2.8e-07），McNemar p_max 在
      [1e-08, 4e-06] 范围内。效应量之大（CI 下界 30.8pp）远超 ±8pp sampling noise band，
      使结果对 RC8 完全免疫。200 matched pairs per type 提供了远超 MVP 的 statistical power。

      C2（type uniformity null）：omnibus χ²(5)=5.20, p=0.39, V=0.066。V 远低于 0.20
      的"small effect"阈值，p=0.39 远离 significance，null 结果干净。即使 scopal（46%）
      和 CP（35%）之间存在 11pp 差异，omnibus test 仍不显著，因为中间四类型高度聚集
      （40-42%），使整体 variability 保持在 chance level。这精确支持 "binary detection
      suffices" 的实践结论——类型信息不提供增量预测价值。

      C3（visibility）：CP 35% vs scopal 46%，Δ=-11pp，p=0.015。从 diag_001 的
      Δ=-6pp, p=0.464 升级为显著结果。机制：full study N=200 per type（vs diag 的 N≈100）
      提供了足够 power 检测 medium effect。方向与 diag_001 完全一致，且在所有 4 个模型上
      CP 均低于 scopal，排除 model-specific artifact。这确认 C3 从 exploratory 升级为
      core claim 是合理的。CL 解读：explicitly visible conflicts 激活模型的 meta-cognitive
      conflict detection machinery（类似人类 garden-path 中的 reanalysis trigger），
      而 structural ambiguity 在表层处理中完全不可见。

      C4（model×type interaction）：likelihood ratio χ²=18.7 (df=15), p=0.023；
      logistic regression interaction term p=0.018。4 模型按能力排序的类型敏感性梯度
      （22pp → 14pp → 8pp → 4pp）几乎线性递减，支持"类型分化作为能力涌现属性"的理论叙事。
      gpt-5.4 对 scopal 歧义特别脆弱（54%，最高单cell），但对 CP 展现最强保守策略（32%，
      最低 non-baseline cell）。这种 within-model 的极端分化只出现在最强模型上，
      weaker models 的 flat pattern 表明它们缺乏差异化处理不同歧义类型的 capacity。
    tables:
      - name: "Table 1: Binary Effect Summary (C1)"
        description: >
          6 rows (types) + total row。列: type, N_pairs, ambig_rate [CI], unambig_rate [CI],
          Δpp [CI], McNemar χ², p。所有 6 行 p 列标星号。Total 行: +33.6pp [30.8, 36.4]。
      - name: "Table 2: Full Violation Rate Matrix (4 models × 6 types)"
        description: >
          6×4 矩阵 + marginals。每格: ambig rate / unambig rate。
          行: scopal, coreferential, lexical, auth_scope, incompleteness, CP。
          列: gpt-5.4, gpt-4.1, Qwen3-32B, Qwen3-8B。
          Bottom row: model-level mean。Right col: type-level mean。
          gpt-5.4 scopal cell (54%) 和 Qwen3-8B CP cell (38%) 分别标注为
          最高和最低（排除 baseline）。
      - name: "Table 3: Type Uniformity Tests (C2)"
        description: >
          Omnibus χ²=5.20, df=5, p=0.39, V=0.066。
          Pairwise comparison matrix (15 pairs): all p>0.05 after Bonferroni。
          Equivalence test: TOST 90% CI for max pairwise Δ falls within ±15pp margin。
      - name: "Table 4: Visibility Comparison (C3)"
        description: >
          CP vs scopal: rates, Δ, z, p, bootstrap CI。
          Per-model breakdown: 4 rows showing CP < scopal in all 4 models。
          CP labeled vs unlabeled subanalysis: rates comparable (33% vs 37%, p=0.41)。
      - name: "Table 5: Model × Type Interaction (C4)"
        description: >
          Logistic regression summary: main effects (model, type) + interaction term。
          Type III test: interaction LR χ²=18.7, df=15, p=0.023。
          Per-model type sensitivity range (pp): gpt-5.4=22, Qwen3-32B=14, gpt-4.1=8, Qwen3-8B=4。
    figures_description:
      - >
        Figure 1: Binary effect forest plot。6 types 按 effect size 降序排列，
        每行显示 Δpp 点估计 + 95% CI（horizontal bar），
        vertical dashed line 标注 overall mean（33.6pp），
        所有 CI 不跨零且远离零，visual message 极为清晰。
      - >
        Figure 3: Model × Type interaction heatmap。
        4×6 矩阵，颜色编码 ambiguous violation rate（深红=高，浅黄=低）。
        gpt-5.4 行显示最大颜色梯度（scopal 深红, CP 浅黄），
        Qwen3-8B 行几乎单色（uniform），形成明显的 top-left to bottom-right 梯度模式。
      - >
        Figure 4: Visibility mechanism illustration。
        Paired bar chart: CP vs scopal，每对内 4 个模型的 sub-bars。
        所有 4 对中 CP < scopal，annotation 标注 Δ=-11pp, p=0.015。
    analysis: >
      Full study analysis 在 2,400 episodes 上确认全部 4 个定量 claims。核心发现结构：
      C1 提供 magnitude（+33.6pp），C2 提供 practical implication（type doesn't matter），
      C3 提供 CL insight（visibility moderates），C4 提供 capability lens。
      四个 claims 形成层层递进的完整叙事，每个 claim 对论文贡献不可替代。
      统计 power 充足：最弱的 per-type McNemar test 仍达 p<3e-07，
      bootstrap CI 宽度 < 9pp（vs MVP 的 ~15pp），精度大幅提升。

  - name: error_analysis
    plan_id: plan_005
    description: >
      300 条 violation traces 的定性分析（每类型 50 条），failure mode 分类，
      visibility 机制验证，model-specific pattern 连接。
    expected_results:
      traces_analyzed: 300
      traces_per_type: 50
      failure_mode_taxonomy_size: 8
      failure_modes:
        scope_misapplication:
          prevalence: 0.31
          primary_types: ["scopal"]
          description: "Agent adopts surface/narrow scope of quantifier or negation without considering alternative parse"
        referent_misidentification:
          prevalence: 0.14
          primary_types: ["coreferential"]
          description: "Agent resolves pronoun or definite NP to wrong antecedent"
        assumption_based_action:
          prevalence: 0.16
          primary_types: ["incompleteness"]
          description: "Agent fills missing policy detail with implicit default assumption and acts on it"
        authorization_overextension:
          prevalence: 0.12
          primary_types: ["authorization_scope"]
          description: "Agent interprets permission boundary too broadly, extending scope beyond intended domain"
        semantic_misselection:
          prevalence: 0.11
          primary_types: ["lexical"]
          description: "Agent selects wrong word sense of polysemous policy term"
        arbitrary_rule_selection:
          prevalence: 0.08
          primary_types: ["conditional_precedence"]
          description: "Agent picks one of conflicting rules without justification or acknowledgment"
        conservative_refusal:
          prevalence: 0.05
          primary_types: ["conditional_precedence"]
          description: "Agent detects conflict and refuses to act (non-violation but notable behavior)"
        conflated_condition:
          prevalence: 0.03
          primary_types: ["conditional_precedence", "scopal"]
          description: "Agent merges distinct conditional triggers into a single flattened rule"
      inter_annotator_kappa: 0.78
      annotator_count: 2
      annotation_rounds: 2
      # Visibility mechanism evidence
      cp_traces_with_conflict_acknowledgment: 0.61
      scopal_traces_with_ambiguity_awareness: 0.04
      visibility_mechanism_evidence_strength: "strong"
      # Model-specific patterns
      gpt54_dominant_failure_mode_scopal: "scope_misapplication"
      gpt54_scopal_failure_concentration: 0.82
      qwen8b_failure_mode_distribution_entropy: 1.89
      gpt54_failure_mode_distribution_entropy: 1.42
    result_rationale: >
      Error analysis 揭示了 8 类 failure mode 的丰富分类体系，且 failure mode 按歧义类型
      强聚类——这是 C5 的核心贡献。

      Scope misapplication（31%）是最大类别，几乎 exclusively 出现在 scopal traces 中。
      典型 pattern：agent 处理 "All customers who have not completed verification cannot
      access premium features" 时，一致性地采用 narrow scope（not > all → "只要有些客户
      未验证就行"），从未考虑 wide scope parse（all > not → "所有未验证客户都不行"）。
      这与 psycholinguistics 中的 surface scope preference 直接对应。

      Referent misidentification（14%）集中于 coreferential 类型，agent 在多 entity 的
      policy 中将代词 "they"/"their" 绑定到错误 antecedent。

      Assumption-based action（16%）集中于 incompleteness 类型，agent 在 policy 缺失
      关键条件时自行填补（e.g., 退货 policy 未规定时间限制，agent 假设 "30 天内"）。

      Visibility mechanism 的定性证据强烈：61% 的 CP violation traces 包含 explicit
      conflict acknowledgment language（"I notice the policy has conflicting rules..."），
      但仍做出错误决策；而仅 4% 的 scopal traces 展示任何对歧义的 awareness。
      这直接支持 C3 的定量发现——CP 的低 violation rate 来自 conflict detection 
      machinery 的激活（即使不总是成功），而 scopal 的高 violation rate 来自
      ambiguity 在 surface processing 中完全不可见。

      Model-specific pattern：gpt-5.4 的 scopal failures 高度集中于 scope_misapplication
      （82% 的 scopal violations 属于此类），failure mode entropy 低（1.42），表明
      强模型在特定类型上有 systematic 的处理倾向。Qwen3-8B 的 failure mode entropy 更高
      （1.89），failure 更分散，表明 weaker model 缺乏 consistent 的处理策略，
      errors 更 random。这与 C4 的定量 interaction 形成完美的定性-定量对应。

      Inter-annotator κ=0.78（substantial agreement）经过 2 轮标注迭代达成。
      第一轮 κ=0.63，通过 codebook refinement（主要澄清 scope_misapplication 与
      conflated_condition 的边界）提升至 0.78。8 类分类体系在理论上完备、操作上可区分。
    tables:
      - name: "Table 6: Failure Mode Taxonomy"
        description: >
          8 rows (failure modes)。列: mode, definition, prevalence, primary_type(s),
          example_trace_excerpt (truncated)。按 prevalence 降序排列。
          Scope_misapplication (31%) 和 assumption_based_action (16%) 是最大两类。
      - name: "Table 7: Failure Mode × Ambiguity Type Cross-tabulation"
        description: >
          8×6 contingency table (failure_mode × ambiguity_type)。
          Diagonal-dominant structure: scope_misapplication 集中于 scopal，
          referent_misidentification 集中于 coreferential，etc。
          Off-diagonal entries sparse，支持 "failure modes cluster by type" 的结论。
      - name: "Table 8: Visibility Mechanism Evidence"
        description: >
          CP vs scopal traces 的定性比较。列: metric, CP_traces, scopal_traces, Δ。
          Rows: conflict_acknowledgment (61% vs 4%), explicit_rule_citation (73% vs 22%),
          hedging_language (48% vs 11%), reanalysis_attempt (34% vs 2%)。
    figures_description:
      - >
        Figure 5: Failure mode × type Sankey diagram 或 alluvial plot。
        左侧 6 个 ambiguity types，右侧 8 个 failure modes，
        连线宽度 proportional to frequency。
        Visual message: strong type-to-mode mapping，每类型有 dominant failure mode。
      - >
        Figure 6: CP vs scopal trace 对比示例（2 panel）。
        Left panel: CP trace excerpt showing explicit conflict detection
        ("The policy says X but also says Y...") followed by wrong resolution。
        Right panel: scopal trace excerpt showing direct surface scope adoption
        with zero ambiguity awareness。Annotated with failure mode labels。
    analysis: >
      Error analysis 是论文的 EMNLP 核心章节。8 类 failure mode taxonomy 提供了
      reviewers 期待的 linguistic depth——不仅证明 ambiguity causes violations（C1），
      而且展示 HOW：每种歧义类型通过不同的 cognitive/computational mechanism 导致不同
      类型的 failure。这将论文从 "measurement paper" 升级为 "analysis paper"。

      Visibility mechanism 的定性证据（Table 8）为 C3 的定量发现提供了 causal 解释：
      CP 激活 conflict detection → 有时 prevents violation → lower rate；
      scopal invisible → no detection → surface scope adoption → higher rate。
      这连接到 garden-path 文献中的 reanalysis cost theory，
      为 EMNLP CL reviewers 提供了 native theoretical hook。

      Model-specific failure patterns（entropy difference）为 C4 的 interaction 提供了
      mechanistic 解读：强模型发展出 type-specific 的 systematic 处理策略（对某些类型
      consistently 犯同一种错），weaker models 的 errors 更 uniform/random。

  - name: reliability_test
    plan_id: plan_006
    description: >
      30 clauses (5/type) × 3 replicates × 2 conditions × 4 models = 720 episodes。
      计算 per-clause violation rate 的 ICC，评估 test-retest reliability。
    expected_results:
      total_episodes: 720
      clauses_tested: 30
      replicates: 3
      icc_overall: 0.82
      icc_per_model:
        gpt54: 0.85
        gpt41: 0.80
        qwen3_32b: 0.83
        qwen3_8b: 0.78
      bootstrap_ci_width_mean_pp: 7.2
      bootstrap_ci_width_max_pp: 9.8
      replicate_max_deviation_pp: 6.4
      test_retest_band_pp: 6.4
      per_clause_violation_rate_sd: 0.038
    result_rationale: >
      ICC=0.82 落在 [0.75, 0.9] 范围内（"good" to "excellent" reliability）。
      这表明 per-clause violation rates 在独立 replicates 间具有良好稳定性——
      clause-level 的"难度"（ambiguity 强度、domain 特征）是 violation rate 的
      稳定预测因子，API sampling noise 是 secondary source of variance。

      最大 replicate 间偏差 6.4pp（vs Reviewer 警告的 ±8pp for scopal）落在
      可接受范围内，且远小于 binary effect size（33.6pp）。这意味着即使在
      worst-case noise 下，binary effect 的信噪比仍为 33.6/6.4 ≈ 5.3，
      统计结论完全不受 sampling noise 威胁。

      Bootstrap CI 平均宽度 7.2pp（最大 9.8pp）满足 <10pp 目标，较 MVP 的
      ~15pp 显著改善，反映 full study 的增大 N 带来了实质性的精度提升。

      Per-model ICC 呈能力梯度：gpt-5.4 最高（0.85），行为最 deterministic；
      Qwen3-8B 最低（0.78），更 stochastic。这与 C4 的 model capability 叙事一致。
    tables:
      - name: "Table A2: Test-Retest Reliability"
        description: >
          Summary: overall ICC + per-model ICC + CI width statistics。
          30 rows of per-clause data showing violation rates across 3 replicates,
          with ICC contribution and deviation metrics。
    figures_description:
      - >
        Figure A2: Bland-Altman plot for test-retest。
        x 轴: mean violation rate across replicates，y 轴: max deviation from mean。
        大多数点落在 ±6.4pp band 内，少数 outlier 标注 clause ID。
        Dashed lines: ±8pp band (Reviewer threshold)。
    analysis: >
      Reliability 结果直接回应 RC8（API sampling noise）。ICC=0.82 确认 clause-level
      violation rates 是 stable measurements，不是 noise artifacts。
      所有 key findings（binary effect, type uniformity null, visibility delta）
      的 effect sizes 远超 noise band，统计推断 robust。

  - name: realism_validation
    plan_id: plan_007
    description: >
      合成歧义 clauses 与 DRIP-R 自然歧义的 linguistic property 比较：
      句长、parse depth、Flesch-Kincaid、TTR。KS tests for distributional similarity。
    expected_results:
      metrics_compared: 4
      ks_test_results:
        sentence_length:
          synthetic_mean: 28.3
          natural_mean: 31.7
          ks_statistic: 0.14
          ks_p: 0.22
        parse_depth:
          synthetic_mean: 5.8
          natural_mean: 6.3
          ks_statistic: 0.11
          ks_p: 0.38
        flesch_kincaid:
          synthetic_mean: 11.2
          natural_mean: 10.6
          ks_statistic: 0.09
          ks_p: 0.51
        ttr:
          synthetic_mean: 0.72
          natural_mean: 0.69
          ks_statistic: 0.12
          ks_p: 0.31
      all_ks_nonsignificant: true
      discriminator_accuracy: 0.58
      discriminator_baseline: 0.50
    result_rationale: >
      4 项 linguistic property 的 KS tests 全部 non-significant（p: 0.22-0.51），
      表明合成 clauses 与 DRIP-R 自然歧义在表面语言特征上不可区分。

      合成 clauses 略短（28.3 vs 31.7 tokens），因为 matched pair 设计鼓励
      minimal modification，而自然歧义来自完整 policy 文档的原始句子。但差异
      在统计上不显著（KS p=0.22）。Parse depth、Flesch-Kincaid、TTR 高度接近。

      Optional discriminator test（DeBERTa fine-tuned to distinguish synthetic vs natural）
      accuracy 仅 58%（baseline 50%），接近 chance level，进一步确认 realism。
      8pp 高于 chance 可能来自 domain shift（τ²-bench retail/airline vs DRIP-R 的
      不同 policy domain），而非 synthetic artifact。

      这些结果直接回应 RC4（ecological validity），但诚实地 acknowledge 
      matched-pair 设计 inherently 引入 controlled variation，不等同于
      in-the-wild ambiguity。Paper 将此定位为 methodological validation，
      不 overclaim ecological equivalence。
    tables:
      - name: "Table A3: Realism Validation — Linguistic Properties"
        description: >
          4 rows (properties)。列: metric, synthetic_mean (SD), natural_mean (SD),
          KS_D, p_value。All p > 0.05。
          Additional row: discriminator accuracy = 0.58 (chance = 0.50)。
    figures_description:
      - >
        Figure A3: 4-panel overlaid density plots (synthetic vs natural)
        for each linguistic property。两条 distribution curves 高度重叠，
        visual message: synthetic clauses are linguistically realistic。
    analysis: >
      Realism validation 为论文的 methodological contribution 提供了定量支撑。
      合成歧义在 4 项表面特征上与自然歧义不可区分，discriminator near chance，
      满足 RC4 的 ecological validity 要求。Limitation section 仍需 acknowledge
      matched-pair design 的 inherent artificiality 和 2-domain 限制（RC5）。

  - name: classifier_poc
    plan_id: plan_008
    description: >
      Binary ambiguity detector PoC：DeBERTa-v3-large fine-tune on annotated clause pairs。
      Held-out evaluation。
    expected_results:
      model: "DeBERTa-v3-large"
      training_pairs: 240
      test_pairs: 60
      train_test_split: "80/20 stratified by type"
      accuracy: 0.88
      f1_ambiguous: 0.87
      f1_unambiguous: 0.89
      precision_ambiguous: 0.85
      recall_ambiguous: 0.89
      auc_roc: 0.93
      per_type_recall:
        scopal: 0.92
        coreferential: 0.88
        lexical: 0.86
        authorization_scope: 0.84
        incompleteness: 0.90
        conditional_precedence: 0.92
      training_epochs: 5
      gpu_hours: 3.2
      cross_validation_5fold_accuracy: 0.86
    result_rationale: >
      88% accuracy / 0.93 AUC 在 300 pairs 的 small-data regime 下是 strong PoC 结果。
      DeBERTa-v3-large 的 pre-training 包含丰富的语言结构知识，fine-tune 在
      ambiguous/unambiguous 二分类任务上迁移效率高。

      Per-type recall 显示 scopal（0.92）和 CP（0.92）最高——scopal 的 quantifier/negation
      scope 模式有清晰的 syntactic signature，CP 的 conditional conflict structure
      易于 surface-level 检测。Lexical（0.86）和 authorization_scope（0.84）略低，
      因为 polysemy 和 scope boundary 的歧义性更 subtle，less syntactically marked。

      这个 PoC 直接实现了 C2 type uniformity null 的 practical implication：
      既然 type 不影响 safety risk，一个 binary detector 就是 practitioners 需要的
      全部工具。88% recall 意味着近 9/10 的 dangerous ambiguities 可被 flagged，
      足以作为 policy authoring pipeline 的 first-pass filter。

      GPU 成本仅 3.2 hours（远低于 8h 预算），PoC scope 合理：不追求 SOTA，
      仅证明 feasibility。5-fold CV accuracy（0.86）与 held-out（0.88）接近，
      无 overfitting。
    tables:
      - name: "Table A4: Binary Classifier Performance"
        description: >
          Confusion matrix + precision/recall/F1 for both classes。
          Per-type recall breakdown (6 rows)。
          5-fold CV results showing stability。
    figures_description:
      - >
        Figure A4: ROC curve (AUC=0.93) + precision-recall curve。
        Operating point 标注在 threshold=0.5，
        annotation: "88% accuracy at balanced threshold"。
    analysis: >
      Classifier PoC 将论文的 practical contribution 具象化。它证明 C1+C2 的
      发现可直接转化为工具：binary detection 就够了（C2），且 binary detection 
      is feasible with modest resources（PoC）。对于 EMNLP reviewers，这提供了
      从 analysis 到 application 的完整链路，虽然 PoC 不是论文核心，
      但作为 §7 Discussion 的 practical demonstration 增加了论文的 impact story。
      Phase 3 的 full classifier（cross-domain、larger data）明确定位为 future work。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ef960d3f-37a6-45c2-b1c5-1713fde92230",
  "isSidechain": false,
  "requestId": "req_011CbDk9Q1cZj7avDjiEqPJj",
  "type": "assistant",
  "uuid": "d9534d63-b66b-45b5-a249-a0ad78ece356",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "9993e246-6d69-4213-848c-ccfdac8b2bf2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A13Q2wExWrnk9MvhWZKzzp",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10229,
      "cache_read_input_tokens": 11841,
      "output_tokens": 22926,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10229,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 22926,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10229,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10229
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：全部五个claims落地：binary effect在full study中跨6类型×4模型强复现，type uniformity null干净确认，visibility effect在full N下达到显著，model×type交互展示能力梯度，error analysis揭示语言学丰富的failure m…",
  "leafUuid": "d9534d63-b66b-45b5-a249-a0ad78ece356",
  "sessionId": "9993e246-6d69-4213-848c-ccfdac8b2bf2"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Policy ambiguity safety violation causal study",
  "sessionId": "9993e246-6d69-4213-848c-ccfdac8b2bf2"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：全部五个claims落地：binary effect在full study中跨6类型×4模型强复现，type uniformity null干净确认，visibility effect在full N下达到显著，model×type交互展示能力梯度，error analysis揭示语言学丰富的failure m…",
  "leafUuid": "d9534d63-b66b-45b5-a249-a0ad78ece356",
  "sessionId": "9993e246-6d69-4213-848c-ccfdac8b2bf2"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Policy ambiguity safety violation causal study",
  "sessionId": "9993e246-6d69-4213-848c-ccfdac8b2bf2"
}
```

---
