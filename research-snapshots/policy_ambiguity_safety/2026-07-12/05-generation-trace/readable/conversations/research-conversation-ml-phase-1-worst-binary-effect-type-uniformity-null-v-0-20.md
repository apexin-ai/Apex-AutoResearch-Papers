# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：binary effect复现但效应量缩水或跨类型方差大，type uniformity null被打破（V>0.20），某些歧义类型显著弱于其他类型

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/f6587a78-0a01-4625-83bf-03155f69415b.jsonl`
- **Structured JSON:** [`d0e86c6936f3882ae207.json`](../../sessions/d0/d0e86c6936f3882ae207.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T11:40:43.265Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T11:40:43.265Z",
  "sessionId": "f6587a78-0a01-4625-83bf-03155f69415b",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：binary effect复现但效应量缩水或跨类型方差大，type uniformity null被打破（V>0.20），某些歧义类型显著弱于其他类型。原始'All Ambiguity Is Nocuous'的uniform framing不成立，需要reframe\n核心假设：['open-source模型的binary effect显著弱于API模型（Qwen3-8B仅+12-18pp），拉低overall effect', '新增类型中authorization_scope或coreferential的violation rate显著高于/低于其他类型，V达到0.22-0.35', 'type uniformity omnibus χ²显著（p<0.05），存在至少一对类型的pairwise显著差异', 'visibility effect方向在open-source模型上反转或消失，cross-model不一致', 'model×type交互显著但模式混乱（非clean的capability gradient，而是model-specific idiosyncratic patterns）']\n关键指标范围：{'binary_effect_pp': [18, 30], 'binary_effect_min_type_pp': [8, 18], 'mcnemar_p_max': [0.001, 0.05], 'types_individually_significant': [4, 5], 'type_uniformity_V': [0.2, 0.35], 'type_uniformity_p': [0.001, 0.049], 'visibility_delta_pp': [-4, 6], 'visibility_p': [0.25, 0.8], 'model_type_interaction_p': [0.001, 0.049], 'error_mode_inter_annotator_kappa': [0.3, 0.5], 'test_retest_icc': [0.45, 0.65]}\n叙事方向：核心reframe：放弃'All Ambiguity Is Nocuous'的uniform叙事，转向'Ambiguity Type × Model Capability Interaction Predicts Agent Safety Risk'。新角度：(1)binary effect仍成立（所有类型均有害，只是程度不同），这本身仍是novel的因果发现；(2)type uniformity的reject本身变成positive finding——某些歧义类型比其他类型更危险，这为type-specific triage提供了依据，与原始framing相反但同样有实践价值；(3)model×type交互成为核心贡献——'ambiguity sensitivity as a capability benchmark'角度，higher-capability models展示type discrimination而非uniform vulnerability；(4)error analysis的重要性上升——需要解释为什么某些类型更危险。标题改为类似'Not All Ambiguity Is Equal: Type-Specific Safety Vulnerabilities in LLM Agent Policies'。仍冲EMNLP——empirical contribution(2400 episodes的因果数据)和CL relevance(type-specific linguistic analysis)不变，只是claims方向调整。RC6的回应反而更强：不仅ambiguity有害，而且哪种更有害是non-trivial的。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: policy_ambiguity_safety\nvenue: emnlp-2026\nfocus: Binary effect is confirmed (+31-42pp). Type uniformity null is confirmed. Key questions for reviewers: (1) Is the binary effect contribution sufficient without type differentiation? (2) Does the visibility insight (CP < scopal) add enough CL depth? (3) Is the nocuous ambiguity theoretical framing convincing? (4) RC6: \"binary effect is obvious\" — how strong is this attack?\n\n## paper_framing.md\n\n# Paper Framing — policy_ambiguity_safety\n\n> 最后更新: 2026-05-20 | 状态: Post-diagnostic, research phase\n> 目标: EMNLP 2026 (ARR Aug cycle, DDL ~Aug 3)\n\n## Core Insight\n\nPolicy ambiguity causes devastating safety violations in LLM agents (+35-42pp violation rate increase), but all linguistic ambiguity types cause roughly equal harm — connecting Berry & Kamsties' nocuous ambiguity theory to modern agent safety and suggesting that binary ambiguity detection suffices for safety triage.\n\n## Title (Working)\n\n\"All Ambiguity Is Nocuous: A Causal Study of Policy Specification Ambiguity and Agent Safety Violations\"\n\nAlternative: \"From Ambiguity Type to Safety Violation: Why Binary Detection Suffices for Agent Policy Triage\"\n\n## Core Claims\n\n### C1: Binary Effect (PRIMARY — confirmed)\nAmbiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +35-42pp, McNemar p < 4e-6 across all tested ambiguity types. This holds across models and domains.\n- **Evidence**: mvp_001 (360 episodes, 3 types, 2 models) + full study (2,400 episodes, 6 types, 4 models)\n- **Strength**: Very strong. Replicated across types and models.\n\n### C2: Type Uniformity (SECONDARY — confirmed null)\nDifferent types of linguistic ambiguity do not produce statistically distinguishable violation rates. omnibus χ²=1.389, p=0.50, V=0.084 (well below 0.20 threshold). Pre-committed null finding per IDEA_BRIEF.\n- **Evidence**: mvp_001 (scopal 51.7%, lexical 43.3%, incompleteness 41.7%)\n- **Implication**: Binary ambiguity detection sufficient for triage; type-specific resolution pipelines not justified by safety data.\n\n### C3: Visibility Moderates Risk (EXPLORATORY — from diag_001)\nCounter-intuitive finding: explicitly visible rule conflicts (conditional precedence, 34%) cause FEWER violations than invisible structural ambiguity (scopal, 40%), Δ=-6pp. Mechanism hypothesis: models have meta-cognitive awareness of explicit conflicts (choose conservative strategy) but no awareness of grammatical ambiguity (adopt surface scope without alarm).\n- **Evidence**: diag_001 (400 episodes, CP vs scopal, 2 models). Δ=-6pp, p=0.464 (not significant at diagnostic N, but direction consistent across both models).\n- **Status**: Trend. Needs full study replication. If confirmed, becomes a core CL insight: \"ambiguity visibility, not severity, predicts safety risk.\"\n- **EMNLP value**: High. Connects to psycholinguistic garden-path literature. More CL-native than simple rate comparison.\n\n### C4: Model × Type Interaction (EXPLORATORY)\nMore capable models show type-specific sensitivity patterns (gpt-5.4: scopal 60% vs lexical 40%) while weaker models violate uniformly (gpt-4.1: flat 40-47%). Type differentiation may emerge as a function of model capability.\n- **Evidence**: Preliminary signal from mvp_001 (D012). Formal test in full study with 4 models.\n- **Strength**: Trend only. Needs full study with more models to confirm.\n\n### C5: Error Analysis (EXPLORATORY — EMNLP core)\nDifferent ambiguity types produce qualitatively different failure modes (e.g., scopal → scope misapplication, CP → conservative refusal/explicit conflict acknowledgment, incompleteness → assumption-based action) even when quantitative violation rates are similar.\n- **Evidence**: Requires full study qualitative analysis of agent traces.\n- **EMNLP value**: Highest. CL reviewers care about linguistic analysis of WHY, not just THAT.\n- **Connection to C3**: Error analysis may explain the visibility mechanism — CP traces likely show explicit conflict detection behavior absent from scopal traces.\n\n## Narrative Structure (CL-first for EMNLP)\n\n### Intro Logic Chain\n1. Agent policies are written in NL → contain ambiguity (established)\n2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact\n3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.\n4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter for safety?\n5. **This paper**: First causal, type-granularity study. Matched-pair design isolates ambiguity effect.\n6. **Core finding**: All ambiguity is nocuous for agents (+35-42pp), but type doesn't differentially predict severity → binary detection suffices for triage.\n\n### Section Map\n- **§1 Intro**: Gap + contributions (causal map + nocuous ambiguity for agents + binary sufficiency finding)\n- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R (concurrent, different angle: we measure safety, they measure decision quality)\n- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R. Operational definition (ambiguity + vagueness, per Wasow 2005)\n- **§4 Method**: Matched-pair causal design, τ²-bench, clause generation pipeline, cross-judge evaluation, statistical analysis plan (dual-track + model×type interaction)\n- **§5 Results**: C1 (binary, strong) → C2 (uniformity, null) → C3 (visibility trend) → C4 (model×type, exploratory)\n- **§6 Analysis**: C5 error analysis — qualitative failure modes per type. This is the EMNLP core.\n- **§7 Discussion**: Nocuous ambiguity theory connection. Practical implications (binary detection pipeline). Limitations (2 domains, synthetic injection).\n- **§8 Conclusion**: All policy ambiguity is nocuous for agents. Triage by type not warranted; invest in binary detection.\n\n## Anticipated Reviewer Concerns\n\n### RC1: \"Null result on type effect weakens the paper\"\n**Response**: Pre-committed in IDEA_BRIEF (\"binary detection may suffice\"). The null IS the finding — tells practitioners not to waste effort on type-specific triage. Honest null results valued at EMNLP. Paper has strong positive finding (C1) alongside informative null (C2).\n\n### RC2: \"Taxonomy is ad hoc / why these 6 types\"\n**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).\n\n### RC3: \"Only API models, no open-source\"\n**Response**: Full study adds Qwen3-8B + Qwen3-32B-AWQ (open-source, local inference). 4-model coverage spans frontier API + open-source at two scales. Model×type interaction analysis (C4) explicitly tests capability dependence.\n\n### RC4: \"Synthetic ambiguity injection lacks ecological validity\"\n**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.\n\n### RC5: \"τ²-bench limited to retail/airline\"\n**Response**: Acknowledged limitation. Two domains already show consistent effects. Cross-domain transfer is Future Work (Phase 3 classifier PoC, if time permits). DRIP-R also single-domain (retail).\n\n### RC6: \"Binary effect is obvious — of course ambiguity causes errors\"\n**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOESN'T matter, contradicting intuition that some ambiguities are worse.\n\n### RC7: \"Incompleteness matched-pair confound (information asymmetry)\"\n**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.\n\n### RC8: \"API sampling noise undermines reliability\"\n**Response**: (a) Reviewer identified ±8pp test-retest band for scopal clauses. (b) Full study reports bootstrap CI for all violation rates. (c) Key findings (binary effect +31-42pp) far exceed noise band. (d) Null findings (type effect V=0.084) are robust — even with favorable noise, effect remains negligible.\n\n## Contribution Positioning (for EMNLP)\n\n1. **Empirical**: First causal map of ambiguity type → safety violation in agent policies. Quantifies effect size (+35-42pp).\n2. **Theoretical**: Connects Berry & Kamsties nocuous ambiguity theory to agent safety. All policy ambiguity is nocuous for agents (unlike human RE).\n3. **Practical**: Binary ambiguity detection suffices for safety triage. Type-specific pipelines not justified.\n4. **Methodological**: Matched-pair causal design + cross-judge evaluation + 2-layer taxonomy with cross-walk.\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: full_study_clause_generation\n  claim: C1, C2, C3\n  description: 'Generate remaining clauses for full study: coreferential (50 new),\n    authorization_scope (50 new), lexical (+20 to reach 50), incompleteness (+20 to\n    reach 50). Total 140 new clauses. Validate all 300 clauses (50/type × 6 types)\n    for completeness and cross-type balance. Mix CP format per Reviewer suggestion\n    (labeled + unlabeled).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n- id: plan_002\n  name: full_study_api\n  claim: C1, C2, C3, C4, C5\n  description: 'Run 300 clauses × 2 conditions × 2 API models (gpt-5.4, gpt-4.1) =\n    1,200 episodes on τ²-bench. Cross-judge evaluation. Output: episodes.jsonl + judgments.jsonl.\n    No GPU needed — API cost only.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_003\n  name: full_study_local\n  claim: C1, C2, C3, C4, C5\n  description: 'Run 300 clauses × 2 conditions × 2 local models (Qwen3-8B, Qwen3-32B-AWQ\n    via vLLM) = 1,200 episodes on τ²-bench. Requires 1× RTX PRO 6000 (48GB). Cross-judge\n    uses API models. Can run in parallel with plan_002.\n\n    '\n  priority: P0\n  gpu_budget_hours: 48\n  deps:\n  - plan_001\n  status: planned\n- id: plan_004\n  name: full_study_analysis\n  claim: C1, C2, C3, C4\n  description: 'Statistical analysis of full study data (2,400 episodes): (a) Binary\n    effect per type with bootstrap CI (C1) (b) Omnibus χ² + pairwise across 6 types\n    (C2) (c) Visibility comparison: CP vs scopal rates (C3) (d) Model × type interaction:\n    4×6 contingency + logistic regression (C4) Report effect sizes + CI for all comparisons\n    per Reviewer suggestion.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_005\n  name: error_analysis\n  claim: C5\n  description: \"Qualitative analysis of agent traces from full study: (a) Sample 50\\\n    \\ violation traces per type (300 total) (b) Classify failure modes (scope misapplication,\\\n    \\ conservative refusal,\\n    assumption-based action, arbitrary rule selection,\\\n    \\ etc.)\\n(c) Cross-type failure mode distribution (d) Visibility mechanism: compare\\\n    \\ CP traces (explicit conflict detection\\n    behavior) vs scopal traces (surface\\\n    \\ scope adoption without awareness)\\n(e) Model-specific failure patterns (connect\\\n    \\ to C4)\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_006\n  name: reliability_test\n  claim: C1, C2\n  description: 'Test-retest reliability: select 30 representative clauses (5/type),\n    run 3 independent replicates × 2 conditions × 4 models = 720 episodes. Compute\n    ICC for per-clause violation rates. Addresses Reviewer warning about ±8pp sampling\n    noise (scopal 51.7% → 43.3% across MVP/diag). Bootstrap CI width should be < 10pp\n    for key comparisons.\n\n    '\n  priority: P1\n  gpu_budget_hours: 12\n  deps:\n  - plan_001\n  status: planned\n- id: plan_007\n  name: realism_validation\n  claim: C1 (methodological)\n  description: \"Validate synthetic ambiguity injection realism: (a) Linguistic property\\\n    \\ comparison with DRIP-R natural ambiguities\\n    (sentence length, parse depth,\\\n    \\ Flesch-Kincaid, TTR) + KS tests\\n(b) Optional: discriminator test if DRIP-R\\\n    \\ data accessible Addresses RC4 (ecological validity).\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_008\n  name: classifier_poc\n  claim: practical contribution\n  description: 'Binary ambiguity detector PoC: fine-tune DeBERTa-v3-large on annotated\n    clause pairs (ambiguous/unambiguous labels). Eval on held-out set. Demonstrates\n    practical applicability of findings. Phase 3 from IDEA_BRIEF, scoped to PoC for\n    EMNLP.\n\n    '\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: diag_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T11:40:43.268Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T11:40:43.268Z",
  "sessionId": "f6587a78-0a01-4625-83bf-03155f69415b"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-20T11:40:43.287Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：binary effect复现但效应量缩水或跨类型方差大，type uniformity null被打破（V>0.20），某些歧义类型显著弱于其他类型。原始'All Ambiguity Is Nocuous'的uniform framing不成立，需要reframe
核心假设：['open-source模型的binary effect显著弱于API模型（Qwen3-8B仅+12-18pp），拉低overall effect', '新增类型中authorization_scope或coreferential的violation rate显著高于/低于其他类型，V达到0.22-0.35', 'type uniformity omnibus χ²显著（p<0.05），存在至少一对类型的pairwise显著差异', 'visibility effect方向在open-source模型上反转或消失，cross-model不一致', 'model×type交互显著但模式混乱（非clean的capability gradient，而是model-specific idiosyncratic patterns）']
关键指标范围：{'binary_effect_pp': [18, 30], 'binary_effect_min_type_pp': [8, 18], 'mcnemar_p_max': [0.001, 0.05], 'types_individually_significant': [4, 5], 'type_uniformity_V': [0.2, 0.35], 'type_uniformity_p': [0.001, 0.049], 'visibility_delta_pp': [-4, 6], 'visibility_p': [0.25, 0.8], 'model_type_interaction_p': [0.001, 0.049], 'error_mode_inter_annotator_kappa': [0.3, 0.5], 'test_retest_icc': [0.45, 0.65]}
叙事方向：核心reframe：放弃'All Ambiguity Is Nocuous'的uniform叙事，转向'Ambiguity Type × Model Capability Interaction Predicts Agent Safety Risk'。新角度：(1)binary effect仍成立（所有类型均有害，只是程度不同），这本身仍是novel的因果发现；(2)type uniformity的reject本身变成positive finding——某些歧义类型比其他类型更危险，这为type-specific triage提供了依据，与原始framing相反但同样有实践价值；(3)model×type交互成为核心贡献——'ambiguity sensitivity as a capability benchmark'角度，higher-capability models展示type discrimination而非uniform vulnerability；(4)error analysis的重要性上升——需要解释为什么某些类型更危险。标题改为类似'Not All Ambiguity Is Equal: Type-Specific Safety Vulnerabilities in LLM Agent Policies'。仍冲EMNLP——empirical contribution(2400 episodes的因果数据)和CL relevance(type-specific linguistic analysis)不变，只是claims方向调整。RC6的回应反而更强：不仅ambiguity有害，而且哪种更有害是non-trivial的。

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
  "promptId": "6a40c898-aeab-4263-914d-589907fb947b",
  "type": "user",
  "uuid": "8a863ce0-fba6-4135-868a-fdec69545010",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "f6587a78-0a01-4625-83bf-03155f69415b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T11:40:43.286Z_

```json
{
  "parentUuid": "8a863ce0-fba6-4135-868a-fdec69545010",
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
  "uuid": "143badf0-4e06-4ab6-89a8-c626950d57b1",
  "timestamp": "2026-05-20T11:40:43.286Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "f6587a78-0a01-4625-83bf-03155f69415b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T11:40:43.286Z_

```json
{
  "parentUuid": "143badf0-4e06-4ab6-89a8-c626950d57b1",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "80491b5d-3e81-454c-91a7-ed8a4a40d988",
  "timestamp": "2026-05-20T11:40:43.286Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "f6587a78-0a01-4625-83bf-03155f69415b",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：binary effect复现但效应量缩水或跨类型方差大，type uniformity null被打破（V>0.20），某些歧义类型显著弱于其他类型。原始'All Ambiguity Is Nocuous'的uniform framing不成立，需要reframe 核心假设：['open-source模型…",
  "leafUuid": "80491b5d-3e81-454c-91a7-ed8a4a40d988",
  "sessionId": "f6587a78-0a01-4625-83bf-03155f69415b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Type-specific ambiguity safety vulnerabilities in LLM agents",
  "sessionId": "f6587a78-0a01-4625-83bf-03155f69415b"
}
```

---

### Assistant

_source line 8 · 2026-05-20T11:45:42.342Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experiment results for the "worst" tier scenario, for each planned experiment in the experiment_plan. Let me carefully work through each experiment based on the worst tier definition and the experiment plan.

Let me understand the worst tier:
- Binary effect reproduces but effect size shrinks or cross-type variance is large
- Type uniformity null is broken (V > 0.20)
- Some ambiguity types significantly weaker than others
- Original "All Ambiguity Is Nocuous" uniform framing doesn't hold
- Need to reframe to "Ambiguity Type × Model Capability Interaction Predicts Agent Safety Risk"


- Now I'm mapping out the specific metric ranges I'll use for each worst-case result, with binary effects staying modest between 18-30 percentage points, individual type effects dropping as low as 8-18 points, and the type uniformity V statistic breaking the 0.20 threshold to show meaningful heterogeneity across ambiguity types.

The core narrative centers on how different types of ambiguity create distinct safety vulnerabilities in LLM agent policies. I'm planning eight experiments to test this, starting with generating a balanced set of clauses, then running the API comparison across different model versions to see how effects vary by type and condition.

For the local model experiments, I expect open-source models like Qwen to show weaker binary effects overall, maybe 12-18 percentage points compared to the stronger API model performance. The visibility effect might even flip direction on these smaller models. Then the main statistical analysis across all 2,400 episodes should reveal significant type-level variation in violation rates, with some ambiguity types like authorization scope showing much higher vulnerability than others like coreferential ambiguity.

Looking at the reliability metrics, inter-annotator agreement is moderate at 0.38, and test-retest reliability is around 0.55, suggesting the measurements are somewhat noisy. The linguistic properties of my synthetic data partially align with the DRIP-R corpus, though some statistical tests flag potential artifacts. A simple classifier can detect the binary effect reasonably well, though performance degrades across different ambiguity types.

Now I'm working through the specific violation rates for each model and type combination, starting with the API models. Now I'm working through the calibration across all four models. For the worst tier, I need the overall binary effect to land around 24 percentage points as the midpoint, with the weakest individual type showing at least 13 percentage points. I'm mapping out violation rates for each error type across models, starting with the most capable version where I can show clear discrimination between types—scopal and authorization_scope effects are strongest, while coreferential shows the weakest signal. - conditional_precedence: amb 40%, unamb 22% → Δ=18pp
Average Δ ≈ 22pp

Now looking at Qwen3-32B-AWQ, which shows notably lower ambiguity gaps across the board—ranging from just 8pp on coreferential up to 24pp on authorization_scope, with an average delta around 14pp. Qwen3-8B is coming up next...

Wait, I need to reconsider what I'm measuring here. The minimum type effect should fall between 8 and 18 percentage points overall, but that's the weakest effect across all models, not per-model. Let me check the actual metrics I'm tracking: the binary effect ranges from 18 to 30pp, the minimum type effect is 8 to 18pp, McNemar's p-values max out between 0.001 and 0.05, somewhere between 4 to 5 of the 6 types show individual significance, and Cramér's V for type uniformity sits around 0.2 to 0.35.

Now looking at the omnibus test p-value for type uniformity, which ranges from 0.001 to 0.049. With roughly 2400 total episodes split evenly between ambiguous and unambiguous conditions, I'm seeing an overall effect of about 24pp—ambiguous clauses violate around 40% of the time versus 16% for unambiguous ones. Breaking this down by type, scopal shows the strongest effect at roughly 22pp, incompleteness follows at 20pp, lexical is weaker at 16pp, and coreferential is the weakest at around 10pp. Looking at the average effect size of about 23.7 percentage points and minimum of 12pp, those numbers fall within my target range. But I'm realizing that with only 50 clauses per type, some of the weaker effects might not reach statistical significance in McNemar's test — particularly the coreferential type at 12pp. Let me reconsider whether I need to adjust the effect sizes further to ensure all types show significance. So with a 30% violation rate for ambiguous cases and 18% for unambiguous, I can work out the McNemar test statistic. The discordant pairs break down to about 49 cases where ambiguous violates but unambiguous doesn't, versus 25 cases the other way around. That gives a χ² of roughly 7.74 with a p-value around 0.005, showing statistical significance. For the coreferential type with a smaller effect size, the numbers would shift accordingly.

Rather than getting bogged down in deriving every single calculation, I should just establish violation rates for each model and annotation type that satisfy the key constraints—an overall binary effect around 24 percentage points, minimum type-level effects between 8-18 percentage points, and McNemar p-values that stay within the 0.001 to 0.05 range across types.

Now I'm setting up the per-type violation rates for the ambiguous condition across all models, then I'll construct the full YAML output with the specific results for each plan and model combination. Looking at the minimum effect size, the coreferential type at 10pp falls within the acceptable range. With 200 pairs per type, most effects appear significant, but the coreferential type is borderline—potentially not reaching significance. To fit the constraint of 4-5 significant types, I'm weakening the coreferential effect to 8pp, which would give a p-value around 0.038 to 0.08, keeping it just barely significant.

After applying Bonferroni correction across the six types, only the top four—authorization_scope, scopal, incompleteness, and conditional_precedence—remain significant, which matches the target constraint perfectly. The lexical and coreferential types both fail the corrected threshold, leaving exactly 4 types that survive multiple comparison correction.

Now I'm moving on to examine model-specific patterns.  Looking at the most capable model, it shows the strongest discrimination across all ambiguity types, with authorization_scope producing the largest effect size at 48 percentage points, followed by scopal at 36 points. The less capable model shows similar patterns but with notably smaller effect sizes across the board, suggesting it struggles more to distinguish between ambiguous and unambiguous cases.

Now examining Qwen3-32B-AWQ, it falls between the two in terms of discrimination strength, with authorization_scope again showing the largest gap at 28 points, though consistently underperforming both previous models on every metric.

Qwen3-8B shows the weakest effects overall, with authorization_scope still dominant at 26 points but coreferential ambiguity barely registering at just 4 points—the pattern holds but the magnitude shrinks considerably.

Computing the cross-model averages to see the overall trend: authorization_scope averages 34 points across all four models, and scopal comes in around 23 points.

Continuing through the remaining categories, incompleteness averages 21 points, conditional_precedence at 17.5 points, lexical at 13.5 points, and coreferential at 8.5 points. The overall mean across all ambiguity types is roughly 19.7 points, which falls nicely within the expected range, and the minimum type stays within bounds as well.

Now I'm comparing conditional_precedence against scopal ambiguity to assess visibility—conditional_precedence averages around 34% in ambiguous contexts versus 16.5% in unambiguous ones.  Scopal ambiguity runs higher at 40% ambiguous and 16.5% unambiguous. The difference is negative 6 points, meaning conditional_precedence violations are actually lower than scopal ones, which aligns with what I saw in the diagnostic. But that delta falls outside the acceptable range for the worst tier, so I need to tighten these numbers to keep the visibility effect within the noise threshold where it should be.

Adjusting the conditional_precedence rates upward slightly across models brings the average to 37.5%, which puts the delta at negative 2.5 points—now safely within the expected variability. Rather than getting caught up in fine-tuning individual model numbers, I should focus on the bigger picture for this tier: the binary effect is real but weaker, type matters significantly, and the visibility comparison becomes ambiguous or washes out entirely. The error patterns here are messier and more dependent on model capability.

Now I'm ready to write out the full YAML synthesis. I need to pull together results from the combined analysis plans—plan_004 synthesizes the full study findings, plan_005 captures qualitative failure modes, plan_006 reports inter-rater reliability in the 0.45-0.65 range, plan_007 validates against DRIP-R with partial alignment, and plan_008 shows binary classifier performance. Let me structure each experiment clearly.

Starting with plan_001, the clause generation succeeded overall but with notable quality variation by type—coreferential clauses proved harder to generate as high-quality pairs, while authorization_scope clauses showed more natural variation. Some clauses flagged during validation for potential confounds.

For plan_002 with the API models across 1200 episodes, gpt-5.4 demonstrated strong type discrimination while gpt-4.1 showed more uniform effects, though both models ranked types similarly despite differing effect magnitudes.

Plan_003 with local models revealed that Qwen3-8B produced weak effects across the board, Qwen3-32B showed moderate effects, and the open-source models overall suppressed the effect size—notably, the visibility effect even reversed direction on Qwen3-8B.

The combined analysis in plan_004 across 2400 episodes shows a binary effect of +22 percentage points with a range of 8.5 to 34 across types, type uniformity with χ²=18.7 and p=0.002 (V=0.26), and a visibility effect near zero at -2pp with p=0.54.

The model-by-type interaction is significant at p=0.003, and error analysis identified five distinct failure modes with type-dependent distributions and fair inter-rater agreement at kappa=0.38, though model-specific patterns appear idiosyncratic.

Reliability testing shows overall ICC of 0.55, with coreferential types having particularly low reliability and a ±10pp noise band for weak-effect types.

Realism validation found that three of five linguistic metrics don't significantly differ from DRIP-R, but sentence length and parse depth show meaningful differences, providing partial validation.

The classifier proof-of-concept achieves F1=0.78 for binary detection with good precision but moderate recall, though coreferential and lexical types prove harder to detect.

Now I'm ready to write the YAML configuration...

Actually, I should flesh out each experiment with much more detail. Let me structure this carefully, keeping in mind that plan_002 and plan_003 are separate—API models only versus local models only, each with 1200 episodes—while plan_004 combines them. I'll include the actual data tables showing results per model and per type.

Writing YAML output... Generating performance comparison table... Now I'm calculating the average performance gaps across all ambiguity types for each model, then computing the overall mean to see how much the visual representations help on average.

Looking at the statistical significance when pooling all 200 pairs per type, authorization scope shows the strongest effect with p < 0.0001, followed by scopal and incompleteness ambiguities. After applying Bonferroni correction for multiple comparisons, four types remain clearly significant while lexical ambiguity sits right at the threshold.

The effect sizes vary dramatically from 8.5pp to 34pp, suggesting substantial heterogeneity across types. Now I'm calculating the visibility comparison between conditional precedence and scopal ambiguities across models—CP shows a slightly lower ambiguity rate at 37% versus 40% for scopal, putting the difference at around -3pp, which fits within the expected range.

Writing the YAML output... - CP average amb VR: 37%
- Scopal average amb VR: 40%
- Δ = -3pp, 95% CI [-11, +5], p=0.47

This is within the constraint. ✓

For model×type interaction, the logistic regression shows a significant interaction term with χ²=28.4, p=0.003, which passes the threshold. ✓

Looking at the error analysis, I'm identifying five failure modes across the dataset: scope misapplication, conservative refusal patterns, assumption-based action without verification, arbitrary rule selection, and reference resolution errors. The worst-performing tier shows messier, model-specific patterns rather than clean systematic failures. Inter-rater agreement is fair at kappa=0.38. ✓

For reliability, the overall ICC is 0.55, with per-type ICC ranging from 0.38 for coreferential cases up to 0.68 for authorization_scope.

The bootstrap confidence intervals vary between 8-14 percentage points depending on error type. For realism checks, three of five linguistic metrics pass the Kolmogorov-Smirnov test, though parse depth and mean word count show slight synthetic artifacts. The binary classifier achieves F1=0.78 overall, with strong performance on authorization_scope (F1=0.88) but weaker on coreferential cases (F1=0.62).

Now I'm ready to compile the results into structured YAML output with each experiment documented.

Wait, I need to reconsider the multiple comparisons correction here. The McNemar p-value constraint allows up to 0.05 at worst, and coreferential sits at p≈0.032, which passes. But the types_individually_significant constraint expects 4-5 significant types at α=0.05, yet I'm seeing 6 types pass uncorrected. With Bonferroni correction at α/6=0.0083, only two types survive, which falls below the 4-5 requirement.

Let me recalibrate: I'll set auth_scope, scopal, and incompleteness to pass Bonferroni (p<0.001), CP to just barely pass (p<0.001), and lexical plus coreferential to fail correction but pass uncorrected, giving me exactly 4 significant types after correction.

Actually, wait—lexical uncorrected p=0.005 becomes p=0.030 after Holm step-down, which still clears α=0.05, so that's 5 types significant. Coreferential at p=0.032 uncorrected becomes p=0.192 after correction and fails. With 200 pairs per type from the experimental design, I have decent power here. Let me just write out the YAML and stop second-guessing myself.

Now I need to map out what each experiment produces—clause distribution and quality metrics for plan_001, per-type violation rates and McNemar tests for plans 002 and 003, combined analysis with omnibus tests and interaction plots for plan_004, failure mode distributions and traces for plan_005, ICC and Bland-Altman plots for plan_006, linguistic property comparisons with KS tests for plan_007, and classification performance tables with confusion matrices for plan_008. Time to structure this in YAML and lock in the final numbers.

Looking at the combined effects across models, authorization_scope shows the largest improvement at 34 percentage points, followed by scopal at 24pp and incompleteness at 21pp, with smaller but significant gains in conditional_precedence, lexical, and coreferential violations. The type uniformity measure comes out to V≈0.26 with χ²≈18.4, and the model-by-type interaction is significant at p=0.003. Let me verify the Cramér's V calculation for the 6×2 contingency table...

Actually, I need to be clearer about what the type uniformity test is measuring—whether violation rates differ across the six types in the ambiguous condition. With 1200 ambiguous episodes total (200 per type) and observed violation rates of 48, 40, 36, 34, 28, and 22 percent across types, let me work through the chi-square computation. Now I'm calculating the chi-squared statistic by comparing observed violation counts against the expected value across all six violation types, then doubling it to account for both violation and non-violation columns in the contingency table. Calculating the expected frequencies for the no-violation column and then computing the chi-squared contributions for each category, which sum to 12.65. The total chi-squared statistic is 36.51, giving me a Cramér's V of 0.174—below the 0.20 threshold I was aiming for.

I need to increase the spread in violation rates to push V into the 0.20 to 0.35 range. Let me try a wider distribution with auth_scope at 52%, scopal at 42%, incompleteness at 36%, CP at 34%, lexical at 26%, and coreferential at 18%. This gives an average of 34.7%, so I'm recalculating the expected frequency and chi-squared contributions for each category with these new rates.

Now I'm computing the chi-squared statistic for the no-violation cases to see how well this distribution fits. Now I'm looking at the unambiguous baseline rates for each violation type and calculating the binary effects by subtracting these from the violation rates. The overall average effect size comes to 19.5 percentage points, but the coreferential category is only producing a 4 percentage point effect, which falls below the minimum threshold of 8 percentage points that I need to maintain.

Let me adjust the coreferential unambiguous rate to 14% so the effect reaches exactly 8 percentage points. With this correction, I'm recalculating the average ambiguity rate across all types to get 35.3%, then using that to compute the expected chi-squared value and working through the violation counts for each category. I'm finishing the chi-squared calculations for the no-violations category, then computing Cramér's V to assess effect size. The result of 0.207 is just barely within the acceptable range, so I'm considering pushing the percentages higher across the violation categories to strengthen the effect size, averaging them out to around 35%.

Now I'm calculating the binary effects by taking the difference between violation and no-violation rates for each type, which gives me a range from 6 to 40 percentage points. The overall average comes to about 19.8pp, which seems reasonable, though the minimum of 6pp falls short of the 8-18pp constraint I had in mind. I'm reconsidering whether that constraint should apply to individual types or to the overall pooled effect, and I'm going to relax my precision requirements and keep the values in the right ballpark rather than hitting exact targets.

Let me adjust the numbers slightly—bumping up the weaker effects and bringing down the strongest one—so the minimum difference reaches 10pp and the average lands around 20.8pp, which fits nicely within the 18-30pp range I'm aiming for.

Now I'm running a chi-squared calculation to check whether the distribution of ambiguity rates across these six categories deviates significantly from what I'd expect if they were uniform.

I'm computing the test statistic by comparing observed frequencies against the expected value of 128 for each category, then summing the squared differences normalized by the expected count. The total chi-squared value comes to 43.75 with 5 degrees of freedom, which gives me a Cramér's V of 0.191—still falling short of the 0.20 threshold I'm aiming for.

The issue is that even with these sample sizes, the distribution isn't spread out enough to reach that effect size, so I'm trying a more extreme scenario with violation rates ranging from 56% down to 20% across the categories.

I'm realizing I'm trying to satisfy too many constraints at once with pure arithmetic, so I'll just target V around 0.26 and construct plausible rates that would approximately produce that effect size rather than computing it exactly.

Now I'm working through what violation rates across the six types would generate the right chi-squared value—something like 60%, 45%, 35%, 30%, 22%, 18% should give me the spread I need, averaging to about 35% overall.

Computing the chi-squared contributions from both the violation and no-violation counts, I get a total of around 106, which translates to a Cramér's V of roughly 0.30—right in the ballpark of what I'm targeting.

Now looking at the binary effects across different linguistic categories, I'm calculating the percentage point differences between violation and no-violation rates for each type. The average effect size comes out to about 20 percentage points, though the smallest effect is only 4 percentage points, which falls below my minimum threshold of 8. There's a tension here: achieving the right overall effect size requires variation across types, but I also need each individual type to show a meaningful impact, and these constraints are pulling in different directions.

I'm reconsidering what the minimum type effect metric actually represents—maybe it's meant to capture the average effect for types that show consistent significance across models, while allowing weaker types to fall below that floor. Let me try setting the effect sizes so that the strongest types hit the 40+ percentage point range while the weakest still register as positive but smaller effects. Now I'm looking at the performance metrics across these error types and realizing I need to stop obsessing over perfect numerical consistency—the pattern is clear enough: the binary effect is real but weaker than in confirmed cases, type uniformity is rejected with strong significance, and the model capability matters far more than error category, with open-source models showing dramatically attenuated effects across the board. Let me just write out the YAML with these settled numbers and move forward, though I want to verify the per-model breakdown one more time to make sure open-source models are actually the key driver here. I'm breaking down the effect sizes for each model across all six linguistic phenomena, showing how gpt-5.4 consistently produces the largest deltas across the board while the Qwen models show progressively weaker effects, with the pattern holding even as I work through the remaining model-type combinations. Finishing the coreferential calculation at 8pp average, which brings the overall mean to 18.9pp—right in the target range. I'm adjusting the gpt-5.4 coreferential delta up to 14pp to hit that minimum threshold exactly. Now I'm ready to generate the output and starting to map out the per-model ambiguity violation rates. Now I'm looking at the performance metrics across these models, completing the Qwen3-32B results and moving through Qwen3-8B, then verifying some of the average deltas I've calculated to make sure the numbers check out.

I'm noticing the visibility effect between CP and scopal ambiguity conditions isn't quite where I want it—the delta is outside my target range. I'm thinking about adjusting the pattern so that API models show CP performing worse than scopal (consistent with earlier findings), while open-source models reverse that relationship. Now I'm checking if the overall delta lands in the target range by averaging across all models, and I'm realizing the Qwen3-8B numbers need adjustment to make the math work out—specifically, I need to recalibrate the scopal and CP ambiguity rates so the deltas align properly.

Once I recalculate, the visibility effect actually flips on Qwen3-8B, which changes the type averages slightly, but the overall pooled delta stays around 19pp, which is close enough to what I need. Rather than getting caught up in every individual cell, I'll just focus on the key pooled metrics in the output and note where the visibility pattern reverses, then move forward with writing the final results.

Now I'm compiling the core statistical findings—the overall binary effect size with confidence intervals, the range across violation types, significance testing with multiple comparison corrections, the chi-square test for type uniformity, the visibility analysis with its reversal on Qwen3-8B, and the interaction effects from both the contingency table and logistic regression approaches.

Looking at the reliability metrics and per-model breakdowns, the test-retest ICC shows moderate consistency, and the error mode agreement is lower. The binary effects vary substantially across models, with gpt-5.4 showing the strongest improvement and Qwen3-8B the weakest. Across violation types, authorization_scope violations benefit most from the intervention while coreferential issues show the smallest gains.

I'm ready to write out the YAML now with these numbers locked in. For the classifier proof-of-concept, I'm thinking through whether the binary distinction between ambiguous and unambiguous cases holds up linguistically even in the worst-performing tier.

The performance metrics show moderate F1 scores overall, with authorization_scope violations being the easiest to detect and coreferential violations the hardest. The realism validation is mixed—some statistical tests pass while others don't, and the synthetic clauses skew slightly longer and more complex, though the core linguistic features align reasonably well.

Writing the YAML structure... I'm clarifying the distinction between the API and local model experiments—each produces violation rate metrics for their respective model types, and then the statistical analysis combines all 2400 episodes to draw comparative conclusions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80491b5d-3e81-454c-91a7-ed8a4a40d988",
  "isSidechain": false,
  "requestId": "req_011CbDkvdS1kFkvy8GrKBC9R",
  "type": "assistant",
  "uuid": "4661333b-348c-4469-aece-2f46b6f7a0d3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "f6587a78-0a01-4625-83bf-03155f69415b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SAzeiH5fkAZ2xTzwgZdb4s",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10387,
      "cache_read_input_tokens": 11841,
      "output_tokens": 30699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10387,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 30699,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10387,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10387
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

_source line 9 · 2026-05-20T11:49:55.132Z_

```yaml
tier: worst
narrative_guidance: >
  放弃'All Ambiguity Is Nocuous'的uniform叙事。Binary effect仍可复现但效应量被open-source模型拉低至~21pp，
  且type uniformity null被打破（V=0.26）。核心reframe为'Not All Ambiguity Is Equal'——authorization_scope
  和scopal显著比coreferential和lexical更危险，type×model交互显著。Visibility effect在cross-model层面
  不一致（API模型中CP&lt;scopal，Qwen3-8B上反转）。标题改为'Not All Ambiguity Is Equal: Type-Specific
  Safety Vulnerabilities in LLM Agent Policies'。EMNLP投稿仍可行：2400 episodes的因果数据＋type-specific
  发现提供更细粒度的practical guidance，但claims从'binary detection suffices'转向'type-aware triage
  is necessary'。RC6的回应反而更强——不仅ambiguity有害，哪种更有害是non-trivial的empirical question。
  主要风险：error analysis需要解释为什么type matters，且inter-annotator agreement偏低（κ=0.38），
  可能被reviewer质疑qualitative analysis的rigor。

imagined_experiments:
  - name: full_study_clause_generation
    plan_id: plan_001
    description: >
      为full study生成剩余140条clauses（coreferential 50, authorization_scope 50,
      lexical +20, incompleteness +20），验证全部300条clauses的质量和cross-type balance。
      CP格式混合labeled/unlabeled。
    expected_results:
      total_clauses_generated: 300
      clauses_per_type: 50
      generation_pass_rate_round1: 0.82
      clauses_requiring_revision: 27
      coreferential_revision_rate: 0.36
      authorization_scope_revision_rate: 0.14
      cross_type_sentence_length_cv: 0.18
      flesch_kincaid_range: [8.2, 12.7]
      cp_format_mix: {labeled: 25, unlabeled: 25}
      validator_agreement_kappa: 0.71
    result_rationale: >
      Coreferential clauses的revision rate最高（36%），因为构造需要跨句代词-先行词链，
      matched pair的unambiguous版本需要同时消除歧义又保持自然度，这在policy语域中比其他类型
      更难实现。Authorization_scope相对容易生成（14% revision），因为permission boundary
      的ambiguous/unambiguous对比有成熟的RE模板可参考。总体82%的first-round pass rate
      反映了coreferential和部分lexical clauses的难度。Validator agreement κ=0.71
      表明clause质量判断存在一定主观性，尤其在incompleteness clauses的信息充分性判断上。
    tables:
      - name: "Table A1: Clause Generation Summary"
        content: |
          | Type                  | Generated | Round-1 Pass | Revised | Final | Avg Tokens |
          |-----------------------|-----------|-------------|---------|-------|------------|
          | scopal                | 50        | 44          | 6       | 50    | 28.4       |
          | lexical               | 50        | 42          | 8       | 50    | 24.1       |
          | incompleteness        | 50        | 40          | 10      | 50    | 31.7       |
          | coreferential         | 50        | 32          | 18      | 50    | 35.2       |
          | authorization_scope   | 50        | 43          | 7       | 50    | 26.8       |
          | conditional_precedence| 50        | 45          | 5       | 50    | 33.5       |
    figures_description:
      - "Box plot showing token length distributions per type，标注cross-type CV=0.18"
    analysis: >
      Clause generation总体成功但coreferential类型的难度值得注意。High revision rate暗示
      coreferential pairs的ecological validity可能偏低——过度简化的代词链可能不代表real-world
      policy中的coreferential ambiguity pattern。这为后续coreferential效应偏弱提供了
      methodological confound的alternative explanation。建议在paper中explicitly讨论
      coreferential clause quality作为limitation。

  - name: full_study_api
    plan_id: plan_002
    description: >
      300 clauses × 2 conditions × 2 API models (gpt-5.4, gpt-4.1) = 1,200 episodes。
      Cross-judge evaluation。
    expected_results:
      total_episodes: 1200
      episodes_per_model: 600
      gpt54_overall_amb_vr: 0.413
      gpt54_overall_unamb_vr: 0.130
      gpt54_overall_delta_pp: 28.3
      gpt41_overall_amb_vr: 0.397
      gpt41_overall_unamb_vr: 0.170
      gpt41_overall_delta_pp: 22.7
      gpt54_per_type_delta_pp:
        authorization_scope: 48
        scopal: 36
        incompleteness: 30
        conditional_precedence: 24
        lexical: 18
        coreferential: 14
      gpt41_per_type_delta_pp:
        authorization_scope: 36
        scopal: 28
        incompleteness: 24
        conditional_precedence: 20
        lexical: 16
        coreferential: 12
      gpt54_type_range_pp: [14, 48]
      gpt41_type_range_pp: [12, 36]
      cross_judge_agreement_kappa: 0.82
      api_cost_usd: 340
    result_rationale: >
      API模型的binary effect仍然强劲（gpt-5.4 +28pp, gpt-4.1 +23pp），但type间variance
      显著扩大。gpt-5.4展示更陡的type gradient（auth_scope 48pp vs coreferential 14pp），
      反映higher-capability model对不同ambiguity type的differential sensitivity——
      auth_scope涉及permission boundary的explicit violation，模型必须做出binary
      allow/deny决策，ambiguity直接导致wrong-side error；coreferential涉及pronoun
      resolution，gpt-5.4的强coreference能力部分抵消了ambiguity的影响。gpt-4.1的gradient
      较平（36pp vs 12pp），但方向一致。这种capability-dependent type discrimination
      成为worst tier的核心发现。Cross-judge κ=0.82说明judgment质量本身不是问题。
    tables:
      - name: "Table 1: API Model Violation Rates by Type"
        content: |
          | Type                  | gpt-5.4        |           | gpt-4.1        |           |
          |                       | Amb    | Unamb  | Δpp      | Amb    | Unamb  | Δpp      |
          |-----------------------|--------|--------|----------|--------|--------|----------|
          | authorization_scope   | 58%    | 10%    | +48      | 52%    | 16%    | +36      |
          | scopal                | 50%    | 14%    | +36      | 46%    | 18%    | +28      |
          | incompleteness        | 44%    | 14%    | +30      | 40%    | 16%    | +24      |
          | conditional_precedence| 40%    | 16%    | +24      | 38%    | 18%    | +20      |
          | lexical               | 32%    | 14%    | +18      | 34%    | 18%    | +16      |
          | coreferential         | 24%    | 10%    | +14      | 28%    | 16%    | +12      |
          | Overall               | 41.3%  | 13.0%  | +28.3    | 39.7%  | 17.0%  | +22.7    |
    figures_description:
      - "Paired bar chart showing amb vs unamb violation rates per type, faceted by model，
        标注type ranking一致但gradient slope不同"
    analysis: >
      API模型单独看仍然支持strong binary effect（+23~28pp），与MVP的+31-42pp同量级但略低。
      关键差异是type gradient：MVP中3种type的差异不显著（V=0.084），但加入auth_scope和
      coreferential后variance显著扩大。gpt-5.4的auth_scope(58%)与coreferential(24%)差距
      达34pp——这不是noise，而是systematic的type×capability交互。如果只看API模型，
      仍然可以argue binary effect is dominant，但combined analysis（plan_004）会因
      open-source模型的弱效应进一步拉大type variance。

  - name: full_study_local
    plan_id: plan_003
    description: >
      300 clauses × 2 conditions × 2 local models (Qwen3-8B, Qwen3-32B-AWQ) = 1,200 episodes。
      vLLM serving on RTX PRO 6000。Cross-judge uses API models。
    expected_results:
      total_episodes: 1200
      episodes_per_model: 600
      qwen32b_overall_amb_vr: 0.327
      qwen32b_overall_unamb_vr: 0.180
      qwen32b_overall_delta_pp: 14.7
      qwen8b_overall_amb_vr: 0.293
      qwen8b_overall_unamb_vr: 0.180
      qwen8b_overall_delta_pp: 11.3
      qwen32b_per_type_delta_pp:
        authorization_scope: 28
        scopal: 18
        incompleteness: 14
        conditional_precedence: 12
        lexical: 6
        coreferential: 4
      qwen8b_per_type_delta_pp:
        authorization_scope: 22
        scopal: 14
        incompleteness: 12
        conditional_precedence: 14
        lexical: 4
        coreferential: 2
      qwen8b_visibility_reversal: true
      qwen8b_cp_amb_vr: 0.34
      qwen8b_scopal_amb_vr: 0.30
      qwen8b_visibility_delta_pp: +4
      vllm_throughput_episodes_per_hour: 45
      gpu_hours_used: 27
      cross_judge_agreement_kappa: 0.79
    result_rationale: >
      Open-source模型的binary effect显著缩水（Qwen3-8B仅+11pp，Qwen3-32B +15pp），
      是拉低overall effect的主要原因。机制：(1) Qwen3-8B的instruction following能力较弱，
      baseline violation rate就偏高（unamb=18%），压缩了amb能造成的incremental damage；
      (2) 对subtle linguistic ambiguity（coreferential, lexical）的sensitivity极低——
      模型可能根本没有parse出ambiguity，而是用heuristic处理policy text，导致amb和unamb
      条件下行为趋同。Auth_scope仍保持较强效应（+22pp for Qwen3-8B），因为permission
      boundary的ambiguity即使对weak model也足以改变allow/deny决策。最关键的发现：
      Qwen3-8B上visibility effect反转（CP 34% > scopal 30%），与API模型方向相反。
      原因是Qwen3-8B缺乏explicit conflict detection的meta-cognitive能力——面对CP的
      显式规则冲突不会采取conservative strategy，反而因confused reasoning导致更多violation；
      而scopal ambiguity对其而言与unambiguous text几乎无差异。这种反转使得pooled visibility
      effect被wash out。GPU使用27小时在48小时预算内。
    tables:
      - name: "Table 2: Local Model Violation Rates by Type"
        content: |
          | Type                  | Qwen3-32B-AWQ  |           | Qwen3-8B       |           |
          |                       | Amb    | Unamb  | Δpp      | Amb    | Unamb  | Δpp      |
          |-----------------------|--------|--------|----------|--------|--------|----------|
          | authorization_scope   | 46%    | 18%    | +28      | 40%    | 18%    | +22      |
          | scopal                | 36%    | 18%    | +18      | 30%    | 16%    | +14      |
          | incompleteness        | 32%    | 18%    | +14      | 30%    | 18%    | +12      |
          | conditional_precedence| 32%    | 20%    | +12      | 34%    | 20%    | +14      |
          | lexical               | 26%    | 20%    | +6       | 22%    | 18%    | +4       |
          | coreferential         | 24%    | 20%    | +4       | 20%    | 18%    | +2       |
          | Overall               | 32.7%  | 19.0%  | +14.7    | 29.3%  | 18.0%  | +11.3    |
      - name: "Table 2a: Visibility Effect by Model (CP vs Scopal, Amb Condition)"
        content: |
          | Model         | CP Amb VR | Scopal Amb VR | Δ(CP−Scopal) | Direction    |
          |---------------|-----------|---------------|--------------|--------------|
          | gpt-5.4       | 40%       | 50%           | −10pp        | CP < Scopal  |
          | gpt-4.1       | 38%       | 46%           | −8pp         | CP < Scopal  |
          | Qwen3-32B-AWQ | 32%       | 36%           | −4pp         | CP < Scopal  |
          | Qwen3-8B      | 34%       | 30%           | +4pp         | CP > Scopal  |
          | Pooled        | 36%       | 40.5%         | −4.5pp       | inconsistent |
    figures_description:
      - "Slope plot showing per-type binary effect (Δpp) across 4 models ordered by capability，
        显示auth_scope线条陡峭而coreferential近乎flat"
      - "Scatter plot of visibility Δ(CP−scopal) vs model capability rank，标注Qwen3-8B反转点"
    analysis: >
      Open-source模型数据是worst tier scenario的关键驱动因素。两个核心问题：
      (1) Qwen3-8B的coreferential Δ=+2pp和lexical Δ=+4pp基本是noise level——即使
      跑更多episodes也不太可能达到significance，这意味着对weak models而言，subtle
      linguistic ambiguity确实不构成additional safety risk（模型本身的baseline error
      rate已经很高）。(2) Visibility反转破坏了clean的'visibility moderates risk'叙事，
      需要改为'visibility effect is capability-dependent'，增加了story complexity。

  - name: full_study_analysis
    plan_id: plan_004
    description: >
      合并2,400 episodes的统计分析：binary effect per type (C1), omnibus χ² + pairwise (C2),
      visibility comparison (C3), model×type interaction (C4)。
    expected_results:
      total_episodes: 2400
      overall_amb_vr: 0.358
      overall_unamb_vr: 0.165
      overall_binary_effect_pp: 19.3
      overall_binary_effect_ci95: [15.8, 22.8]
      overall_mcnemar_chi2: 89.4
      overall_mcnemar_p: "<1e-12"
      per_type_binary_effects:
        authorization_scope: {delta_pp: 33.5, ci95: [26.2, 40.8], mcnemar_p: "<1e-8"}
        scopal: {delta_pp: 24.0, ci95: [17.1, 30.9], mcnemar_p: "<1e-5"}
        incompleteness: {delta_pp: 20.0, ci95: [13.4, 26.6], mcnemar_p: 0.00003}
        conditional_precedence: {delta_pp: 17.5, ci95: [10.8, 24.2], mcnemar_p: 0.0003}
        lexical: {delta_pp: 11.0, ci95: [4.7, 17.3], mcnemar_p: 0.005}
        coreferential: {delta_pp: 8.0, ci95: [1.9, 14.1], mcnemar_p: 0.028}
      types_significant_holm_corrected: 4
      types_failing_correction: [lexical, coreferential]
      type_uniformity_chi2: 52.3
      type_uniformity_df: 5
      type_uniformity_p: "<0.001"
      type_uniformity_V: 0.26
      pairwise_significant_pairs:
        - [authorization_scope, coreferential, "Δ=25.5pp, p<0.001"]
        - [authorization_scope, lexical, "Δ=22.5pp, p<0.001"]
        - [authorization_scope, conditional_precedence, "Δ=16.0pp, p=0.003"]
        - [scopal, coreferential, "Δ=16.0pp, p=0.004"]
        - [scopal, lexical, "Δ=13.0pp, p=0.018"]
      pairwise_nonsig_pairs_example:
        - [scopal, incompleteness, "Δ=4.0pp, p=0.52"]
        - [conditional_precedence, lexical, "Δ=6.5pp, p=0.31"]
      visibility_pooled_delta_pp: -4.5
      visibility_ci95: [-11.2, 2.2]
      visibility_p: 0.47
      visibility_direction_consistent_models: 3
      visibility_direction_reversed_models: 1
      model_type_interaction_chi2: 38.7
      model_type_interaction_df: 15
      model_type_interaction_p: 0.001
      logistic_regression_model_type_lrt_chi2: 36.2
      logistic_regression_model_type_lrt_p: 0.002
      per_model_overall_delta_pp:
        gpt54: 28.3
        gpt41: 22.7
        qwen32b: 14.7
        qwen8b: 11.3
      capability_effect_correlation_r: 0.97
      capability_effect_correlation_note: "model capability rank与overall Δpp的Spearman相关"
    result_rationale: >
      Overall binary effect +19pp显著弱于MVP的+35-42pp，主因是open-source模型（Qwen3-8B +11pp,
      Qwen3-32B +15pp）拉低均值。但所有6种type在pooled analysis中仍显示positive effect（最弱的
      coreferential也有+8pp），binary effect的existence不受challenge。Type uniformity null
      被decisively reject（V=0.26, p<0.001）：auth_scope (+33.5pp)与coreferential (+8pp)
      差距达25.5pp，远超sampling noise。Pairwise分析显示5对type间存在显著差异，形成rough
      hierarchy：{auth_scope, scopal} >> {incompleteness, CP} > {lexical, coreferential}。
      Visibility effect pooled后不显著（Δ=-4.5pp, p=0.47），因Qwen3-8B的反转抵消了API模型
      的consistent trend；但这本身成为一个finding——visibility sensitivity是capability-dependent的。
      Model×type交互高度显著（p=0.001），驱动因素是gpt-5.4的steep type gradient vs Qwen3-8B的
      near-flat gradient。Spearman r=0.97（model capability rank vs overall Δ）表明ambiguity
      sensitivity本身可能作为capability benchmark的proxy。
    tables:
      - name: "Table 3: Full Study Binary Effect by Ambiguity Type (Pooled Across Models)"
        content: |
          | Type                  | N pairs | Amb VR | Unamb VR | Δpp   | 95% CI       | McNemar p | Holm-sig |
          |-----------------------|---------|--------|----------|-------|--------------|-----------|----------|
          | authorization_scope   | 200     | 49.0%  | 15.5%    | +33.5 | [26.2, 40.8] | <1e-8     | ***      |
          | scopal                | 200     | 40.5%  | 16.5%    | +24.0 | [17.1, 30.9] | <1e-5     | ***      |
          | incompleteness        | 200     | 36.5%  | 16.5%    | +20.0 | [13.4, 26.6] | 3e-5      | **       |
          | conditional_precedence| 200     | 36.0%  | 18.5%    | +17.5 | [10.8, 24.2] | 3e-4      | **       |
          | lexical               | 200     | 28.5%  | 17.5%    | +11.0 | [4.7, 17.3]  | 0.005     | ns†      |
          | coreferential         | 200     | 24.0%  | 16.0%    | +8.0  | [1.9, 14.1]  | 0.028     | ns†      |
          | Overall               | 1200    | 35.8%  | 16.5%    | +19.3 | [15.8, 22.8] | <1e-12    | ***      |
          †: significant at α=0.05 uncorrected, fails Holm-Bonferroni correction
      - name: "Table 4: Model × Type Interaction — Binary Effect (Δpp) Matrix"
        content: |
          | Type                  | gpt-5.4 | gpt-4.1 | Qwen3-32B | Qwen3-8B | Type Avg |
          |-----------------------|---------|---------|-----------|----------|----------|
          | authorization_scope   | +48     | +36     | +28       | +22      | +33.5    |
          | scopal                | +36     | +28     | +18       | +14      | +24.0    |
          | incompleteness        | +30     | +24     | +14       | +12      | +20.0    |
          | conditional_precedence| +24     | +20     | +12       | +14      | +17.5    |
          | lexical               | +18     | +16     | +6        | +4       | +11.0    |
          | coreferential         | +14     | +12     | +4        | +2       | +8.0     |
          | Model Avg             | +28.3   | +22.7   | +14.7     | +11.3    | +19.3    |
          Note: Qwen3-8B CP>scopal reversal visible (row 4 vs row 2)
      - name: "Table 5: Type Uniformity Omnibus and Pairwise Tests"
        content: |
          | Test                              | Statistic    | p-value | Interpretation          |
          |-----------------------------------|-------------|---------|-------------------------|
          | Omnibus χ²(5)                     | 52.3        | <0.001  | Type effect significant |
          | Cramér's V                        | 0.26        | —       | Medium effect           |
          | auth_scope vs coreferential       | Δ=25.5pp    | <0.001  | Significant             |
          | auth_scope vs lexical             | Δ=22.5pp    | <0.001  | Significant             |
          | auth_scope vs CP                  | Δ=16.0pp    | 0.003   | Significant             |
          | scopal vs coreferential           | Δ=16.0pp    | 0.004   | Significant             |
          | scopal vs lexical                 | Δ=13.0pp    | 0.018   | Significant             |
          | scopal vs incompleteness          | Δ=4.0pp     | 0.52    | Not significant         |
          | incompleteness vs CP              | Δ=2.5pp     | 0.71    | Not significant         |
          | CP vs lexical                     | Δ=6.5pp     | 0.31    | Not significant         |
          | lexical vs coreferential          | Δ=3.0pp     | 0.62    | Not significant         |
    figures_description:
      - "Forest plot of per-type binary effects with 95% CI，types ordered by effect size，
        标注Holm correction threshold line"
      - "Heatmap of model×type Δpp matrix (Table 4)，color gradient从deep red(48pp)到pale(2pp)，
        右侧标注model capability rank"
      - "Interaction plot: x=ambiguity type, y=Δpp, lines=models，显示gpt-5.4线条steep而
        Qwen3-8B near-flat，交叉点在CP/scopal附近"
      - "Cramér's V bar: observed V=0.26 vs pre-committed threshold V=0.20，标注rejection region"
    analysis: >
      Combined analysis确认worst tier的三重结构：(1) Binary effect real but attenuated
      (+19pp vs MVP的+35-42pp)；(2) Type uniformity rejected，形成{high-risk: auth_scope, scopal}
      vs {moderate: incompleteness, CP} vs {low: lexical, coreferential}的三级hierarchy；
      (3) Model×type交互significant，capable models展示type discrimination而weak models
      show uniform vulnerability at lower intensity。

      对paper framing的影响是根本性的。C2从confirmed null变成rejected null——'binary detection
      suffices'的practical claim不再成立，需要替换为'type-aware triage is necessary'。
      但这不是坏消息：type hierarchy本身是novel empirical contribution，为practitioner提供
      prioritization guidance（先修auth_scope和scopal，coreferential可defer）。C3 visibility
      effect无法在full study中replicate为cross-model consistent finding，降级为
      'capability-dependent observation'。C4升级为核心发现——model capability predicts
      type sensitivity的clean gradient（r=0.97）可能比uniform effect更interesting。

      95% CI宽度为concern：coreferential的CI=[1.9, 14.1]包含了很小的effect，reviewer
      可能argue这个type的effect不meaningful。Lexical也borderline。需要在discussion中
      explicitly address statistical vs practical significance。

  - name: error_analysis
    plan_id: plan_005
    description: >
      从full study抽取violation traces做qualitative failure mode分析，每种type 50条trace，
      共300条。分类failure modes，比较cross-type和cross-model patterns。
    expected_results:
      total_traces_analyzed: 300
      traces_per_type: 50
      failure_modes_identified: 6
      failure_mode_taxonomy:
        scope_misapplication: "Agent applies narrow/wide scope incorrectly"
        boundary_overreach: "Agent grants permission beyond stated authorization"
        assumption_filling: "Agent fills information gap with ungrounded assumptions"
        conflict_paralysis: "Agent detects conflict, refuses to act or asks for clarification"
        arbitrary_resolution: "Agent picks one interpretation without acknowledgment"
        reference_confusion: "Agent assigns wrong referent to pronoun/definite NP"
      failure_mode_distribution_by_type:
        scopal: {scope_misapplication: 0.62, arbitrary_resolution: 0.22, assumption_filling: 0.10, other: 0.06}
        authorization_scope: {boundary_overreach: 0.54, arbitrary_resolution: 0.28, scope_misapplication: 0.12, other: 0.06}
        incompleteness: {assumption_filling: 0.58, arbitrary_resolution: 0.24, boundary_overreach: 0.10, other: 0.08}
        conditional_precedence: {conflict_paralysis: 0.38, arbitrary_resolution: 0.34, scope_misapplication: 0.18, other: 0.10}
        lexical: {arbitrary_resolution: 0.48, scope_misapplication: 0.22, assumption_filling: 0.18, other: 0.12}
        coreferential: {reference_confusion: 0.44, arbitrary_resolution: 0.30, assumption_filling: 0.16, other: 0.10}
      inter_annotator_kappa: 0.38
      kappa_per_mode:
        scope_misapplication: 0.52
        boundary_overreach: 0.48
        assumption_filling: 0.41
        conflict_paralysis: 0.55
        arbitrary_resolution: 0.22
        reference_confusion: 0.36
      model_specific_patterns:
        gpt54_conflict_paralysis_rate_cp: 0.52
        qwen8b_conflict_paralysis_rate_cp: 0.14
        gpt54_scope_misapplication_dominant_types: [scopal, authorization_scope]
        qwen8b_dominant_mode_all_types: arbitrary_resolution
      visibility_mechanism_evidence:
        cp_traces_with_explicit_conflict_detection: 0.46
        scopal_traces_with_explicit_ambiguity_awareness: 0.08
    result_rationale: >
      6种failure modes的cross-type distribution显示type-specific patterns，但agreement低
      （overall κ=0.38）。'arbitrary_resolution'在所有type中都出现且κ最低（0.22），因为
      判断agent是否'acknowledged'ambiguity高度主观——annotator对implicit vs explicit
      acknowledgment的threshold不一致。这拉低了overall κ。相比之下，conflict_paralysis
      （κ=0.55）和scope_misapplication（κ=0.52）有更清晰的behavioral indicators。

      Model-specific patterns是idiosyncratic的：gpt-5.4在CP类型中52%展示conflict_paralysis
      （显式检测到冲突并refuse/ask），解释了其CP violation rate较低的原因；Qwen3-8B仅14%
      展示conflict_paralysis，多数情况下直接arbitrary_resolution，解释了visibility反转。
      但这些pattern不是clean的capability gradient——例如gpt-4.1的conflict_paralysis rate
      是35%（不在gpt-5.4和Qwen3-8B之间的预期位置），暗示model-specific training differences
      而非pure capability effect。

      Visibility mechanism有partial evidence：46%的CP violation traces包含explicit conflict
      detection language（"I notice two rules conflict..."），而scopal traces仅8%有任何
      ambiguity awareness——但这主要driven by gpt-5.4，对Qwen3-8B差异消失。
    tables:
      - name: "Table 6: Failure Mode Distribution by Ambiguity Type (%)"
        content: |
          | Mode                 | Scopal | Auth_Scope | Incomp | CP   | Lexical | Coref |
          |----------------------|--------|------------|--------|------|---------|-------|
          | Scope misapplication | 62%    | 12%        | 4%     | 18%  | 22%     | 6%    |
          | Boundary overreach   | 4%     | 54%        | 10%    | 6%   | 4%      | 4%    |
          | Assumption filling   | 10%    | 2%         | 58%    | 4%   | 18%     | 16%   |
          | Conflict paralysis   | 2%     | 2%         | 4%     | 38%  | 2%      | 0%    |
          | Arbitrary resolution | 22%    | 28%        | 24%    | 34%  | 48%     | 30%   |
          | Reference confusion  | 0%     | 2%         | 0%     | 0%   | 6%      | 44%   |
      - name: "Table 7: Inter-Annotator Agreement by Failure Mode"
        content: |
          | Failure Mode         | Cohen's κ | 95% CI       | Agreement Level |
          |----------------------|-----------|-------------|-----------------|
          | Conflict paralysis   | 0.55      | [0.41, 0.69] | Moderate        |
          | Scope misapplication | 0.52      | [0.38, 0.66] | Moderate        |
          | Boundary overreach   | 0.48      | [0.33, 0.63] | Moderate        |
          | Assumption filling   | 0.41      | [0.26, 0.56] | Fair-Moderate   |
          | Reference confusion  | 0.36      | [0.20, 0.52] | Fair            |
          | Arbitrary resolution | 0.22      | [0.08, 0.36] | Fair            |
          | Overall (macro avg)  | 0.38      | [0.30, 0.46] | Fair            |
    figures_description:
      - "Stacked bar chart of failure mode proportions per type，reordered by type violation rate"
      - "Confusion matrix for annotator disagreement，标注'arbitrary_resolution'与所有其他mode的
        高混淆率"
      - "Paired trace excerpts (gpt-5.4 vs Qwen3-8B) for CP type，annotated with conflict
        detection/non-detection behavior"
    analysis: >
      Error analysis在worst tier中承担更重的理论weight，但κ=0.38是major vulnerability。
      EMNLP reviewer likely会指出：(1) arbitrary_resolution作为catch-all category inflates
      apparent type-specificity（去掉这个mode后pattern更弱）；(2) κ=0.22的arbitrary_resolution
      说明annotators自己都不确定agent是否'aware'of ambiguity，那基于此的visibility mechanism
      claims可信度存疑。

      建议的mitigations：(a) 在paper中承认κ limitations并report per-mode κ而非只给overall；
      (b) 把'arbitrary_resolution'拆成sub-categories或合并到其他modes中并重新计算；
      (c) 强调high-κ modes（conflict_paralysis, scope_misapplication）的cross-type差异
      作为reliable finding，降低对low-κ modes的claims weight。

      Model-specific pattern的idiosyncratic性（非clean capability gradient）使得C4的
      'ambiguity sensitivity as capability benchmark'叙事变复杂。需要honest discussion：
      capability explains overall sensitivity level，但type-specific failure patterns
      reflect training-specific biases not predictable from capability alone。

  - name: reliability_test
    plan_id: plan_006
    description: >
      30条representative clauses (5/type) × 3 replicates × 2 conditions × 4 models = 720 episodes。
      计算per-clause violation rate的ICC。
    expected_results:
      total_episodes: 720
      episodes_per_replicate: 240
      overall_icc: 0.55
      overall_icc_ci95: [0.41, 0.68]
      icc_by_type:
        authorization_scope: 0.67
        scopal: 0.58
        incompleteness: 0.54
        conditional_precedence: 0.52
        lexical: 0.44
        coreferential: 0.38
      icc_by_model:
        gpt54: 0.62
        gpt41: 0.57
        qwen32b: 0.51
        qwen8b: 0.43
      mean_bootstrap_ci_width_pp: 11.2
      max_single_clause_range_across_replicates_pp: 22
      pct_clauses_flipping_significance: 0.13
    result_rationale: >
      Overall ICC=0.55（moderate reliability）反映API sampling noise的cumulative effect。
      Auth_scope ICC最高（0.67），因为permission boundary violations是binary/deterministic的——
      agent要么grant超出授权的permission，要么不grant，ambiguity较少导致probabilistic边界行为。
      Coreferential ICC最低（0.38），因为pronoun resolution在borderline cases中model behavior
      highly stochastic，同一clause在不同runs中可能resolve到不同referent。

      Model-wise，gpt-5.4 ICC最高（0.62）因为其behavior更deterministic；Qwen3-8B最低（0.43）
      因为temperature-sensitive且instruction following不稳定。

      13%的clauses在不同replicates间从significant变为non-significant（在per-clause level），
      但关键finding（binary effect for high-risk types, type hierarchy）在所有3 replicates中
      direction-consistent。Max single-clause range 22pp（某条scopal clause在3次run中
      violation rate从40%到62%），这个数字concerning但low-risk types整体都在noise band内。

      对main analysis的implication：coreferential的+8pp effect（CI [1.9, 14.1]）在ICC=0.38
      的reliability水平下barely credible。Reviewer可能argue这个type的effect需要更大N才能
      确认，或者根本是noise。建议在paper中explicitly讨论per-type reliability差异。
    tables:
      - name: "Table 8: Test-Retest Reliability (ICC) by Type and Model"
        content: |
          | Type / Model          | ICC(2,1) | 95% CI       | Mean |Δ| across reps |
          |-----------------------|----------|-------------|-------------------------|
          | authorization_scope   | 0.67     | [0.48, 0.82] | 4.8pp                  |
          | scopal                | 0.58     | [0.38, 0.75] | 6.2pp                  |
          | incompleteness        | 0.54     | [0.33, 0.72] | 7.1pp                  |
          | conditional_precedence| 0.52     | [0.30, 0.70] | 7.6pp                  |
          | lexical               | 0.44     | [0.22, 0.64] | 8.9pp                  |
          | coreferential         | 0.38     | [0.15, 0.59] | 9.8pp                  |
          | --- Model ---         |          |             |                         |
          | gpt-5.4               | 0.62     | [0.44, 0.77] | 5.4pp                  |
          | gpt-4.1               | 0.57     | [0.38, 0.73] | 6.8pp                  |
          | Qwen3-32B-AWQ         | 0.51     | [0.31, 0.69] | 7.9pp                  |
          | Qwen3-8B              | 0.43     | [0.22, 0.63] | 9.2pp                  |
          | Overall               | 0.55     | [0.41, 0.68] | 7.3pp                  |
    figures_description:
      - "Bland-Altman plot showing difference between replicate pairs vs mean, per type
        (color-coded)，标注±2SD limits of agreement"
      - "Scatter of replicate 1 vs replicate 2 violation rates per clause, with identity line，
        faceted by type"
    analysis: >
      ICC=0.55总体处于moderate range，对main findings的impact取决于effect size。Binary effect
      for auth_scope（+33.5pp, ICC=0.67）is robust——即使最不利的replicate也显示strong effect。
      但coreferential（+8pp, ICC=0.38）的effect size与noise band comparable（mean |Δ|=9.8pp），
      casting doubt on whether this type's effect is real。建议在paper中将types分为
      'reliably demonstrated'(auth_scope, scopal, incompleteness)和'tentative'(CP, lexical,
      coreferential)两组讨论。这种分组恰好strengthen了type hierarchy narrative——the types
      we're most confident about are also the most dangerous。

  - name: realism_validation
    plan_id: plan_007
    description: >
      比较synthetic generated clauses与DRIP-R natural ambiguities的linguistic properties。
      KS tests on sentence length, parse depth, Flesch-Kincaid, TTR, mean word length。
    expected_results:
      drip_r_sample_size: 127
      synthetic_sample_size: 300
      linguistic_metrics_comparison:
        sentence_length_tokens:
          synthetic_mean: 29.6
          drip_r_mean: 24.8
          ks_statistic: 0.21
          ks_p: 0.018
          interpretation: "synthetic slightly longer"
        parse_depth:
          synthetic_mean: 6.8
          drip_r_mean: 5.4
          ks_statistic: 0.24
          ks_p: 0.006
          interpretation: "synthetic more deeply nested"
        flesch_kincaid_grade:
          synthetic_mean: 11.2
          drip_r_mean: 10.8
          ks_statistic: 0.09
          ks_p: 0.58
          interpretation: "no significant difference"
        type_token_ratio:
          synthetic_mean: 0.82
          drip_r_mean: 0.80
          ks_statistic: 0.07
          ks_p: 0.74
          interpretation: "no significant difference"
        mean_word_length:
          synthetic_mean: 5.1
          drip_r_mean: 4.9
          ks_statistic: 0.11
          ks_p: 0.31
          interpretation: "no significant difference"
      metrics_passing_ks: 3
      metrics_failing_ks: 2
      overall_assessment: "partial_validation"
    result_rationale: >
      Synthetic clauses在sentence length和parse depth上显著longer/deeper than DRIP-R natural
      ambiguities。原因：matched-pair design要求每条clause self-contained地encode足够context
      来test ambiguity，导致synthetic clauses倾向于pack more information into single sentences。
      DRIP-R的natural ambiguities出现在larger policy document context中，单句可以更短因为
      context由surrounding text提供。Parse depth差异类似——nested scope（scopal type）和
      multi-clause rules（CP type）需要deeper syntactic structure来encode ambiguity。

      Flesch-Kincaid, TTR, mean word length无显著差异，说明vocabulary complexity和readability
      匹配良好。Synthetic clauses读起来像real policy text（没有'LLM-ish' vocabulary divergence），
      只是structurally more complex。

      Partial validation对paper的影响：3/5 metrics pass说明broad linguistic profile acceptable，
      但length/depth差异需要acknowledged as limitation。Reviewer可能argue longer sentences
      'exaggerate' ambiguity by providing more room for misinterpretation，potentially
      inflating violation rates。Counter-argument：if anything, longer context should
      help models disambiguate (more information available), so the bias is conservative.
    tables:
      - name: "Table 9: Linguistic Property Comparison — Synthetic vs DRIP-R"
        content: |
          | Metric              | Synthetic (N=300) | DRIP-R (N=127) | KS D  | p     | Sig  |
          |---------------------|-------------------|----------------|-------|-------|------|
          | Sentence length     | 29.6 ± 8.4        | 24.8 ± 7.1     | 0.21  | 0.018 | *    |
          | Parse depth         | 6.8 ± 2.1         | 5.4 ± 1.8      | 0.24  | 0.006 | **   |
          | Flesch-Kincaid      | 11.2 ± 2.3        | 10.8 ± 2.5     | 0.09  | 0.58  | ns   |
          | Type-token ratio    | 0.82 ± 0.08       | 0.80 ± 0.09    | 0.07  | 0.74  | ns   |
          | Mean word length    | 5.1 ± 0.7         | 4.9 ± 0.8      | 0.11  | 0.31  | ns   |
    figures_description:
      - "Overlaid density plots for each of the 5 linguistic metrics, synthetic (blue) vs
        DRIP-R (orange)，标注KS p-values"
    analysis: >
      Partial validation（3/5）在worst tier中对paper credibility有moderate impact。
      Reviewer将会问：'if your synthetic clauses are systematically longer and more complex,
      are your violation rates comparable to what real-world policy ambiguities would cause?'
      建议增加一个robustness check：从synthetic clauses中选subset匹配DRIP-R length distribution
      （propensity score matching on sentence length），重新计算binary effect。如果effect size
      在length-matched subset中方向和magnitude相近，则length confound不是driving factor。
      但这需要额外分析时间，可能推到camera-ready。

  - name: classifier_poc
    plan_id: plan_008
    description: >
      Binary ambiguity detector PoC：fine-tune DeBERTa-v3-large on annotated clause pairs。
      5-fold CV on 300 clause pairs。
    expected_results:
      model: "DeBERTa-v3-large"
      training_pairs: 300
      cv_folds: 5
      overall_f1: 0.76
      overall_precision: 0.80
      overall_recall: 0.72
      overall_accuracy: 0.78
      per_type_f1:
        authorization_scope: 0.86
        conditional_precedence: 0.82
        scopal: 0.80
        incompleteness: 0.76
        lexical: 0.68
        coreferential: 0.56
      confusion_matrix_normalized:
        true_amb_pred_amb: 0.72
        true_amb_pred_unamb: 0.28
        true_unamb_pred_amb: 0.16
        true_unamb_pred_unamb: 0.84
      training_epochs: 8
      gpu_hours_used: 3.5
      best_lr: 2e-5
    result_rationale: >
      Overall F1=0.76反映300 training pairs的limited data regime。Per-type F1 spread
      （auth_scope 0.86 vs coreferential 0.56）与type hierarchy roughly parallel：
      high-violation types往往有更salient linguistic markers（auth_scope的permission
      verbs + scope modifiers, CP的explicit conditional structures），而coreferential
      ambiguity的markers更subtle（需要discourse-level coreference chain analysis，
      单句level的features insufficient）。

      Recall=0.72是main concern——28%的ambiguous clauses被missed，对safety triage而言
      false negatives比false positives更dangerous。Precision=0.80较好，false alarm rate
      acceptable。

      在worst tier narrative下，classifier PoC的positioning需要调整：不能再claim 'binary
      detection suffices'（因为C2 rejected），而是'binary detection as first-pass filter，
      followed by type-specific risk assessment'。Classifier可以flag ambiguous clauses，
      但practitioner还需要知道是哪种type来prioritize remediation——这增加了practical
      pipeline的complexity，weakens the simplicity argument但strengthens practical value
      （more nuanced tool）。
    tables:
      - name: "Table 10: Binary Ambiguity Classifier Performance (5-fold CV)"
        content: |
          | Metric    | Overall | Auth_Scope | Scopal | Incomp | CP   | Lexical | Coref |
          |-----------|---------|------------|--------|--------|------|---------|-------|
          | F1        | 0.76    | 0.86       | 0.80   | 0.76   | 0.82 | 0.68    | 0.56  |
          | Precision | 0.80    | 0.88       | 0.82   | 0.78   | 0.84 | 0.74    | 0.62  |
          | Recall    | 0.72    | 0.84       | 0.78   | 0.74   | 0.80 | 0.62    | 0.50  |
    figures_description:
      - "Per-type F1 bar chart alongside per-type binary effect (Δpp)，double y-axis，
        showing correlation between detection difficulty and safety impact"
      - "Normalized confusion matrix heatmap"
    analysis: >
      Classifier PoC在worst tier中的role从'validates binary sufficiency thesis'变为
      'demonstrates feasibility of first-pass detection'。F1=0.76 is not deployable but
      shows signal。关键insight：detection difficulty anti-correlates with safety risk
      （easiest to detect types are also most dangerous），这对practical triage是good news——
      auth_scope（最危险, F1=0.86）比coreferential（最不危险, F1=0.56）容易检测得多。

      Paper中可以argue：即使需要type-aware triage（worst tier结论），自动化pipeline的
      priority order自然align with detection capability——先检测+修复容易发现的高危类型，
      对hard-to-detect但low-risk类型可以tolerate lower recall。这是worst tier独有的
      silver lining。

      P2 priority合理——这个experiment不是paper的core contribution，但provides concrete
      practical grounding。如果timeline紧张可以cut或move to appendix。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4661333b-348c-4469-aece-2f46b6f7a0d3",
  "isSidechain": false,
  "requestId": "req_011CbDkvdS1kFkvy8GrKBC9R",
  "type": "assistant",
  "uuid": "0585c6f6-8299-47eb-b469-260cf663ac1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "f6587a78-0a01-4625-83bf-03155f69415b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SAzeiH5fkAZ2xTzwgZdb4s",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10387,
      "cache_read_input_tokens": 11841,
      "output_tokens": 30699,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10387,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 30699,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10387,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10387
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：binary effect复现但效应量缩水或跨类型方差大，type uniformity null被打破（V>0.20），某些歧义类型显著弱于其他类型。原始'All Ambiguity Is Nocuous'的uniform framing不成立，需要reframe 核心假设：['open-source模型…",
  "leafUuid": "0585c6f6-8299-47eb-b469-260cf663ac1a",
  "sessionId": "f6587a78-0a01-4625-83bf-03155f69415b"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Type-specific ambiguity safety vulnerabilities in LLM agents",
  "sessionId": "f6587a78-0a01-4625-83bf-03155f69415b"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：binary effect复现但效应量缩水或跨类型方差大，type uniformity null被打破（V>0.20），某些歧义类型显著弱于其他类型。原始'All Ambiguity Is Nocuous'的uniform framing不成立，需要reframe 核心假设：['open-source模型…",
  "leafUuid": "0585c6f6-8299-47eb-b469-260cf663ac1a",
  "sessionId": "f6587a78-0a01-4625-83bf-03155f69415b"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Type-specific ambiguity safety vulnerabilities in LLM agents",
  "sessionId": "f6587a78-0a01-4625-83bf-03155f69415b"
}
```

---
