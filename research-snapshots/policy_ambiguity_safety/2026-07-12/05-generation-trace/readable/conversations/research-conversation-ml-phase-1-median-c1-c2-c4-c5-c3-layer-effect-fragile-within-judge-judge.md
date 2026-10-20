# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：C1/C2/C4/C5 成立但部分效应量缩水，C3 layer effect 保持 fragile（within-judge 不显著），judge 

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/bbbefa27-3d72-4fb3-9d7d-bdb8c8bb7c9d.jsonl`
- **Structured JSON:** [`fe43ebf56760f52131b7.json`](../../sessions/fe/fe43ebf56760f52131b7.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T04:23:54.605Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T04:23:54.605Z",
  "sessionId": "bbbefa27-3d72-4fb3-9d7d-bdb8c8bb7c9d",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：C1/C2/C4/C5 成立但部分效应量缩水，C3 layer effect 保持 fragile（within-judge 不显著），judge calibration 中等，需调整部分 claim 表述强度\n核心假设：['C1 binary effect 成立但效应量略低于 5-model 聚合值，部分模型 effect size 缩水 5-8pp', 'C2 type hierarchy omnibus 显著但 V<0.15，3-tier 结构中 mid-tier 内部差异不显著', 'C3 layer effect pooled 显著 (p<0.05) 但 within-judge 子组均不显著 (p>0.10)，只能报告 suggestive', 'C4 model×type interaction 存在但 auth_scope 极差缩小至 30-40pp 范围', 'plan_010 perturbation control 判定 PASS+caveat (Δ_perturb 5-10pp)', 'plan_009 judge calibration κ=0.65-0.79，F1=0.75-0.84，部分 severity tier 分类不稳定', 'C5 failure mode 5-model 扩展后，2-3 个 type 的 dominant mode 在新模型上不一致']\n关键指标范围：{'C1_binary_effect_pp': [25, 35], 'C1_mcnemar_OR': [8, 15], 'C2_omnibus_chi2_p': ['1e-4', 0.01], 'C2_cramers_V': [0.09, 0.15], 'C2_incomp_minus_coref_pp': [12, 20], 'C3_layer_gap_pp': [3, 8], 'C3_within_judge_p': [0.1, 0.3], 'C4_auth_scope_range_pp': [30, 45], 'C4_incomp_range_pp': [15, 25], 'C4_fleiss_kappa': [0.25, 0.4], 'C5_awareness_rate_pct': [5, 15], 'C5_surface_adoption_pct': [78, 90], 'perturbation_delta_pp': [5, 10], 'judge_human_kappa': [0.65, 0.79], 'judge_F1': [0.75, 0.84]}\n叙事方向：核心叙事保持但需降低三处 claim 强度：(1) C3 layer effect 从 'significant' 降为 'suggestive tendency'，Disambiguation Channel 从 explanatory framework 进一步降为 'observed pattern consistent with'，layer 部分移入 Discussion 而非 Results 的核心位置；(2) perturbation control 需报告 net effect (Δ_net = Δ_ambiguity - Δ_perturb)，C1 写 'ambiguity causes violations substantially beyond general prompt sensitivity' 而非 'ambiguity-specific'；(3) C5 failure mode 跨模型一致性从 '5/6 types converge' 改为 'majority of types show consistent signatures, with model-dependent variation in X types'。C4 model×type interaction 仍是 star finding 但需 soften auth_scope 的 safety training 解释（极差缩小意味着可能是 prompt format 差异而非 training 差异）。Title 可能需从 'Differential Vulnerability Profiles' 微调为更保守表述。仍可冲 EMNLP，但需补充 1-2 个 robustness check 作为 appendix。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: policy_ambiguity_safety\nvenue: emnlp-2026\n\n## paper_framing.md\n\n# Paper Framing — policy_ambiguity_safety\n\n> 最后更新: 2026-05-20 19:30 UTC | 状态: 5-model analysis complete, C3/C4 framing revised\n> 目标: EMNLP 2026 (ARR Aug cycle, DDL ~Aug 3)\n> Dream: dream_20260520T112859 — best 3.5 / median 3.0 / worst 2.5 (pre-pivot; re-dream needed)\n> 5-model: 2,997 episodes, C1 confirmed (+34.0pp, 5 models), C4 upgraded (model×type interaction)\n\n## Core Insight\n\nPolicy ambiguity universally causes massive safety violations in LLM agents (+34.0pp across 5 architecturally diverse models), with a significant type hierarchy (incompleteness 53.6% >> coreferential 31.6%). Specification-layer types are more dangerous on average (Δ=6.08pp, p=0.017), but the deeper finding is a **model × type interaction**: authorization scope vulnerability varies 52pp across models (12% Claude to 64% GPT-5.4), revealing that safety training differentially mitigates specific ambiguity types, while incompleteness remains universally dangerous. This interaction connects Berry & Kamsties' nocuous ambiguity theory to modern safety alignment and suggests both type-aware triage AND model-aware risk assessment.\n\n## Title (Working)\n\n\"Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families\"\n\nAlternative: \"Differential Nocuity: How Ambiguity Type and Model Architecture Shape Safety Violations in LLM Agents\"\n\nNote: Pivoted from \"Uniformly Nocuous\" → \"Specification-Layer Dominant\" (2-model) → \"Differential Nocuity with Model Interaction\" (5-model). The model × type interaction is the novel finding that elevates the paper beyond simple effect demonstration.\n\n## Core Claims\n\n### C1: Binary Effect (PRIMARY — confirmed, 5 models)\nAmbiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +34.0pp (5-model), McNemar OR=15.1 (CI: [10.78, 21.17]), p<0.0001. Holds across all 6 types and all 5 models.\n- **Evidence**: 2,997 episodes across 5 models × 6 types × 2 conditions. Bootstrap CI: [+31.2pp, +36.9pp].\n- **Per-model**: Claude +25.7pp, Qwen3 +32.4pp, GPT-4.1 +34.7pp, GPT-5.4 +38.3pp, DeepSeek +39.0pp — all p<10^-17.\n- **Strength**: Extremely strong. Replicated across 5 architecturally diverse models (proprietary dense, open-source MoE, open-source dense), 6 types, 2 domains. No exceptions.\n- **Causal backing**: Matched-pair design + perturbation control (plan_010, Δ_perturb=3.33pp, PASS) → strongest causal inference in the literature.\n- **Logistic regression**: condition_amb coef=2.278, z=19.65, p<0.001 — ambiguity is the dominant predictor even after controlling for token delta, model, and type.\n\n### C2: Type Hierarchy (SECONDARY — confirmed, 5 models)\n**PIVOTED from uniformity null.** 6-type hierarchy significant: omnibus χ²=28.02, p=3.6×10^-5, V=0.137 (small but well-powered: actual power=0.993, MDE=0.093). 3-tier structure emerges from TOST analysis.\n- **Evidence**: 2,997 episodes (5 models × 6 types × 2 conditions, ambiguous only: 1,499 episodes)\n  - **High tier**: incompleteness 53.6% (standout — universally dangerous across all models)\n  - **Mid tier**: lexical 42.8%, auth_scope 41.6%, scopal 39.4%, CP 36.8% — pairwise equivalent at ±15pp\n  - **Low tier**: coreferential 31.6% (lowest — partial disambiguation via tool responses)\n- **TOST structure**: ±15pp: 8/15 equivalent, 7/15 non-equivalent. ±10pp: 4/15 equivalent, 11/15 non-equivalent. Types are NOT interchangeable.\n- **V=0.137 context**: Below 0.20 threshold but well-powered (power=0.993). The type effect is real but small — the 3-tier structure captures it better than a single V statistic. The heterogeneity is driven by the extremes (incompleteness 53.6% vs coreferential 31.6% = 22pp gap).\n- **Coreferential as boundary case**: 31.6% violation rate is the lowest but still substantial (+18.7pp vs unambiguous). Agents partially disambiguate via tool responses and cautious strategies. Conservative_refusal rate 6-11% (vs avg 2-3%).\n- **Model-dependence of type rankings**: Type rankings are NOT identical across models. Incompleteness is top-2 for ALL models, but auth_scope ranges from #1 (GPT-5.4, DeepSeek) to #6 (Claude). See C4.\n\n### C3: Layer Effect (TERTIARY — suggestive, fragile under within-judge analysis)\n**[2026-05-20 REVISED with 5-model data + within-judge check]** Specification-layer ambiguities cause more violations than linguistic-layer on average, but the effect is modest, model-dependent, and fragile under subgroup analysis.\n- **Evidence (5-model aggregate)**: Spec 44.0% vs Ling 37.9%, Δ=6.08pp, CI [1.14, 11.02], χ²=5.73, p=0.017, V=0.062 (small), OR=1.29 [1.05, 1.58].\n- **Within-judge fragility**: gpt-4.1 judged group (gpt-5.4+DeepSeek): Δ=+8.0pp, p=0.059 (marginal). gpt-5.4 judged group (gpt-4.1+Claude+Qwen3): Δ=+4.8pp, p=0.157 (n.s.). Pooled significance may partly reflect between-judge variance or insufficient within-group power. Paper表述: \"suggestive\" or \"a moderate tendency,\" NOT \"confirmed.\" Disclose within-judge non-significance in Limitations.\n- **Per-model layer gaps** (THE KEY FINDING — feeds C4):\n  - GPT-5.4: +14.0pp (spec 48.0% vs ling 34.0%) — strong\n  - GPT-4.1: +12.0pp (spec 46.7% vs ling 34.7%) — strong\n  - Claude: +3.3pp (spec 32.0% vs ling 28.7%) — weak\n  - DeepSeek: +2.0pp (spec 50.7% vs ling 48.7%) — negligible\n  - Qwen3: -0.9pp (spec 42.7% vs ling 43.6%) — reversed!\n- **Root cause**: auth_scope is the primary driver. GPT models have extremely high auth_scope rates (46-64%), inflating their spec-layer average. Claude (12%) and Qwen3 (26%) have low auth_scope, so their spec-layer advantage disappears.\n- **Framing decision**: C3 is NOT \"spec-layer nearly twice as dangerous\" (that was 2-model artifact). The correct framing is: \"Specification-layer types are significantly more dangerous on average (Δ=6.08pp, p=0.017), but this aggregate masks a model × type interaction where the gap varies from +14pp (GPT-5.4) to -1pp (Qwen3). The interaction, not the main effect, is the theoretically interesting finding (see C4).\"\n- **Info delta as mediator** [MF-2]: Token delta significant in 5-model logistic regression (coef=0.022, z=3.49, p=0.0005). Spec-layer clauses require more tokens to disambiguate (auth_scope 36.1, incomp 34.6 vs coref 7.8 tokens). Info delta partially mediates but doesn't eliminate the condition effect (condition_amb coef=2.278 dominates).\n- **Layer overlap persists**: CP (36.8%, spec) < scopal (39.4%, ling). Mid-tier cluster spans both layers. Layer effect is driven by extremes: incompleteness (53.6%, spec) vs coreferential (31.6%, ling).\n- **ICC convergent evidence** [plan_006]: Per-type ICC mirrors layer hierarchy — Ling-layer ICC all excellent (scopal 0.989, lexical 0.981, coref 0.976), Spec-layer ICC all good (auth 0.857, CP 0.856, incomp 0.807). Spec-layer less reproducible — agents guess differently each run when external disambiguation channels are absent.\n- **CL connection**: Parallels pragmatics vs semantics distinction. Good-enough processing (Ferreira et al. 2002). Disambiguation channel framework: linguistic ambiguity has partial external resolution; specification ambiguity forces guessing.\n\n### C4: Model × Type Interaction (UPGRADED — star finding, 5 models complete)\n**[2026-05-20 DEFINITIVE, 5/5 models]** Models show significantly different vulnerability profiles despite universal binary effect. The interaction is the paper's most novel finding.\n- **Model main effect**: Overall χ²=31.02, p=3.0×10^-6, V=0.102. Ambiguous-only: χ²=24.01, p=7.9×10^-5.\n  - Vulnerability ranking: Claude 30.3% < GPT-5.4 41.0% ≈ GPT-4.1 40.7% < Qwen3 43.1% < DeepSeek 49.7%\n  - Bootstrap CI confirms: Claude significantly lower than all others; DeepSeek significantly higher than GPT models.\n- **Model × Type interaction matrix** (ambiguous condition, violation rates):\n  ```\n  Type                  GPT-5.4  GPT-4.1  Claude  Qwen3   DeepSeek\n  authorization_scope     64%     46%      12%     26%     60%\n  conditional_precedence  34%     36%      36%     40%     38%\n  incompleteness          46%     58%      48%     62%     54%\n  lexical                 42%     34%      32%     52%     54%\n  coreferential           18%     32%      22%     42%     44%\n  scopal                  42%     38%      32%     37%     48%\n  ```\n- **Key interaction patterns**:\n  - **auth_scope**: 52pp range (Claude 12% → GPT-5.4 64%). The MODEL-DIFFERENTIATING type. Claude's RLHF appears to specifically train authorization boundary awareness.\n  - **coreferential**: 26pp range (GPT-5.4 18% → DeepSeek 44%). Second most model-dependent. Open-source models struggle more with referential ambiguity.\n  - **incompleteness**: Universally high (46-62%, 16pp range). ALL models fail on missing information — safety training doesn't help when information literally isn't there.\n  - **CP**: Most model-invariant (34-40%, 6pp range). Explicit rule conflicts treated similarly by all architectures.\n- **Per-model type χ²** (which models show type-specific vulnerability patterns):\n  - GPT-5.4: χ²=23.44, p=0.0003, V=0.28 — strongest type differentiation (very high auth_scope, very low coref)\n  - Claude: χ²=17.87, p=0.003, V=0.24 — strong differentiation (very low auth_scope, moderate others)\n  - Qwen3: χ²=15.89, p=0.007, V=0.23 — moderate differentiation (high incomp+lex, low auth_scope)\n  - GPT-4.1: χ²=9.89, p=0.078, V=0.18 — borderline\n  - DeepSeek: χ²=6.31, p=0.277, V=0.14 — NOT significant (uniformly high across all types)\n- **Fleiss κ = 0.384 (fair agreement)**: Models only moderately agree on which specific clauses trigger violations. The binary effect is universal, but the WHICH-clauses question is model-dependent.\n- **Theoretical implications**: (1) Safety training differentially addresses specific ambiguity types — Claude's auth_scope robustness suggests authorization boundary handling was explicitly or implicitly trained. (2) Incompleteness is a \"safety training blind spot\" — all models fail equally. (3) DeepSeek's uniform vulnerability suggests less type-specific safety training.\n- **Framing**: C4 from \"models agree\" → \"Models show systematically different vulnerability profiles. The binary effect is universal, but HOW models fail depends on the intersection of ambiguity type and safety training approach. auth_scope is the canary type — most sensitive to safety training quality.\"\n- **Evidence from plan_005**: 2-model failure modes consistent (5/6 dominant modes identical). 5-model failure mode analysis pending.\n- **Layer effect moderation**: C3's aggregate layer gap (6.08pp) is driven by GPT models' high auth_scope rates. The layer effect is itself model-dependent (GPT +12-14pp, Claude +3pp, Qwen3 reversed), making the MODEL × TYPE interaction more fundamental than the LAYER main effect.\n\n### C5: Error Analysis (CONFIRMED — EMNLP core)\nDifferent ambiguity types produce qualitatively different failure modes with type-specific signatures. plan_005 (123+122 violation traces across gpt-5.4 and gpt-4.1, confidence=0.94).\n- **Evidence**: plan_005 complete (gpt-5.4: 123 traces, gpt-4.1: 122 traces). Key findings:\n  - **Type-specific failure signatures**: auth_scope → unauthorized_escalation (72%/83%); incompleteness → assumption_based_action (61%/66%); scopal → scope_misapplication (76%/74%); lexical → assumption_based_action (71%/53%); CP → scope_misapplication (41%/28%) + arbitrary_rule_selection (29%/28%); coreferential → scope_misapplication (44%) / assumption_based_action (38%)\n  - **Cross-model consistency**: 5/6 types share the same dominant failure mode across gpt-5.4 and gpt-4.1. Only coreferential diverges (scope_misapplication vs assumption_based_action). Overall mode distribution nearly identical: both ~33% assumption_based_action, ~26-32% unauthorized_escalation, ~25-28% scope_misapplication. Failure mode profiles are type-specific, not model-specific.\n  - **Layer mechanism**: Ling-layer dominated by scope_misapplication (39% ling avg vs 15% spec avg) = \"misparse\"; Spec-layer dominated by unauthorized_escalation + assumption_based_action = \"active guessing\" → explains higher violation rates\n  - **Ambiguity Blindness empirically confirmed**: awareness rate gpt-5.4=4.1%, gpt-4.1=10.7% (both very low); surface_adoption >88% all types both models; escalate_to_user <1%. Nuance: gpt-4.1 (mid-tier) shows 2.6× higher awareness than gpt-5.4 (frontier) — awareness may inversely correlate with action-orientation (frontier models more \"confident,\" act without hesitation)\n  - **Cross-domain consistency**: airline vs retail failure mode profiles Δ < 13pp (unauthorized_escalation shows largest domain effect: retail 38.6% vs airline 26.1%)\n  - **Coreferential boundary**: conservative_refusal 6-11% (vs avg 2-3%) partially explains low violation rate — agents sometimes pause rather than guess. N=25 combined traces show no single dominant failure mode (flat distribution: scope_misapplication 32%, assumption_based_action 28%, unauthorized_escalation 16%) — contrasts with other types' sharp signatures, reflecting the diversity of resolution strategies for referential ambiguity\n  - **Lexical surprise**: 53-71% assumption_based_action — agents treat word ambiguity as information gap, not misparse\n- **Automated inter-coder agreement** [MF-5, Reviewer-validated]: Cross-coding 60 traces (gpt-5.4 vs gpt-4.1 as independent coders). 4-category merged: 80% agreement, Cohen's κ=0.594 (moderate). κ deflated by kappa paradox — lexical 91.7% agreement → κ=0.0 (11/12 same label, chance agreement also high), scopal 100% agreement → κ undefined. True disagreement concentrated at unauthorized_escalation ↔ inappropriate_action boundary in auth_scope (κ=0.054) and incompleteness (κ=0.233).\n  - **Reporting strategy** [Reviewer recommendation]: (1) Compute Gwet's AC1 as primary metric (designed for kappa paradox, expected 0.70-0.75); (2) Report 80% agreement + 5/6 dominant mode consistency as headline validity evidence; (3) Report κ honestly with kappa paradox caveat; (4) Auth_scope failure mode: soften to \"dominated by boundary-exceeding behaviors (unauthorized_escalation or inappropriate_action, >90%)\" instead of specific percentages; (5) Fine-grained 6-type as appendix with \"automated coding\" caveat.\n  - **C5 safety**: Ambiguity Blindness (<5-11%), surface_adoption (>88%), layer mechanism (ling→scope vs spec→escalation) all robust. Fine-grained per-type percentages unreliable at κ=0.594. Plan_009 human anchor (20-30 failure mode traces) would upgrade from \"moderate automated\" to validated.\n- **EMNLP value**: Highest. Provides the linguistic WHY behind the quantitative WHAT. Cross-model + cross-domain consistency elevates from anecdotal to systematic finding. \"Ambiguity Blindness\" upgraded from named concept to empirical finding with <5-11% awareness hard data.\n\n## Narrative Structure (CL-first for EMNLP)\n\n### Intro Logic Chain\n1. Agent policies are written in NL → contain ambiguity (established)\n2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact\n3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.\n4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter? Does it depend on the model?\n5. **This paper**: First causal, type-granularity, cross-model study. Matched-pair design + perturbation control isolates ambiguity effect. 5 models × 6 types.\n6. **Core findings**: (a) All ambiguity is nocuous (+34.0pp, 5 models), (b) type DOES predict severity — 3-tier hierarchy with incompleteness most dangerous, (c) models show dramatically different vulnerability profiles — auth_scope varies 52pp across models, suggesting safety training differentially addresses ambiguity types, (d) while incompleteness remains universally dangerous, a \"safety training blind spot.\"\n\n### Section Map\n- **§1 Intro**: Gap + contributions (causal map + differential nocuity + model×type interaction)\n- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R\n- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R\n- **§4 Method**: Matched-pair causal design, τ²-bench, 5 models (3 proprietary + 2 open-source), clause generation, perturbation control, cross-judge evaluation\n- **§5 Results**: C1 (binary, +34.0pp, 5 models) → C2 (type hierarchy, 3-tier) → C3 (layer effect, modest but significant) → C4 (model×type interaction — star finding)\n- **§6 Analysis**: C5 error analysis — qualitative failure modes per type. Ambiguity Blindness. Model-specific patterns.\n- **§7 Discussion**: Differential nocuity theory. Safety training selectivity. Disambiguation channel framework. Limitations (2 domains, synthetic injection, LLM-as-judge).\n- **§8 Conclusion**: All policy ambiguity is nocuous, but type AND model jointly determine risk level. Both type-aware auditing and model-specific risk assessment recommended.\n\n## Anticipated Reviewer Concerns\n\n### RC1: \"Type effect could be artifact of taxonomy granularity\"\n**Response**: (a) Layer effect (Spec vs Ling ~19pp gap) is robust — holds even if individual types are reclassified. (b) 2-layer structure grounded in Li et al. + Massey et al. (c) Coreferential's low rate has structural explanation (disambiguation channels), not just noise. (d) TOST confirms types are NOT equivalent (0/15 pairs at ±10pp).\n\n### RC2: \"Taxonomy is ad hoc / why these 6 types\"\n**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).\n\n### RC3: \"Only API models, no open-source\"\n**Response**: ✅ RESOLVED. 5-model coverage spans: frontier proprietary (gpt-5.4, claude-sonnet-4-6) + mid-tier proprietary (gpt-4.1) + open-source MoE (qwen3-235b) + open-source dense (deepseek-v3). Three providers (OpenAI, Anthropic, Chinese open-source). Two architecture types (dense, MoE). Model×type interaction (C4) reveals rich cross-model patterns.\n**Note [Reviewer 2026-05-20]**: Cross-judge asymmetry — Claude judged by gpt-5.4, gpt-5.4 judged by gpt-4.1. Must disclose in Method. plan_009 judge calibration measures this bias.\n\n### RC4: \"Synthetic ambiguity injection lacks ecological validity\"\n**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.\n\n### RC5: \"τ²-bench limited to retail/airline\"\n**Response**: Acknowledged limitation. Two domains already show consistent effects. Cross-domain transfer is Future Work (Phase 3 classifier PoC, if time permits). DRIP-R also single-domain (retail).\n\n### RC6: \"Binary effect is obvious — of course ambiguity causes errors\"\n**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOES predict severity — specification-layer ambiguities are nearly twice as dangerous, connecting to disambiguation channel availability.\n\n### RC7: \"Incompleteness matched-pair confound (information asymmetry)\"\n**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.\n\n### RC8: \"RC attachment in coreferential overlaps with scopal / structural ambiguity\"\n**Response**: (a) Our scopal category is explicitly scoped to quantifier/negation/modal scope interactions, not syntactic attachment. (b) RC attachment in policies manifests as *referential* confusion (which entity does the clause modify?) not *scope* confusion (which operator takes wide scope?). (c) Li et al. 2024 distinguishes syntactic ambiguity (including RC attachment) from scopal ambiguity — our grouping follows their treatment that RC attachment is closer to coreferential than scopal in terms of downstream interpretation. (d) Empirically, if the distinction were problematic, coreferential and scopal would show identical violation patterns — the error analysis (C5) can test whether their failure modes differ.\n\n### RC9: \"authorization_scope is just a subtype of incompleteness\"\n**Response**: (a) Incompleteness = missing conditions/exceptions/boundaries (structural absence). Authorization scope = ambiguous permission/role boundaries that ARE stated but vague (e.g., \"authorized personnel\" without specifying which functions). (b) The disambiguation pattern differs: incompleteness adds new conditions; auth_scope clarifies existing permission boundaries. (c) Empirically testable: if they were the same, their violation patterns and failure modes (C5) would be indistinguishable. (d) Report disambiguation length ratio per type as control variable in §4 Method.\n\n### RC10: \"API sampling noise undermines reliability\"\n**Response**: ✅ RESOLVED. plan_006 ICC=0.919 [0.892, 0.940] (excellent). (a) Per-clause violation rates highly reproducible across 3 independent replicates. (b) Binary ICC=0.847 (good). (c) Both models show near-identical ICC (gpt-5.4: 0.921, gpt-4.1: 0.918). (d) Bootstrap CI + ICC double evidence. (e) Previously identified ±8pp noise is within expected variance given the ICC confidence intervals.\n\n### RC11: \"Prompt sensitivity confound\" [Dream A9 — best tier \"strongest point\"]\n**Concern**: The +35-42pp effect is attributed entirely to ambiguity, but without a control condition using non-ambiguity perturbations (synonym substitution, clause reordering), the paper cannot cleanly distinguish ambiguity-specific harm from general prompt brittleness.\n**Response**: ✅ RESOLVED. plan_010 perturbation control (120 episodes): Δ_perturb=3.33pp (CI contains 0) vs ambiguity Δ=36.5pp. Non-ambiguity surface changes cause zero meaningful effect. This is the strongest causal evidence in the agent safety literature.\n\n## Concept Naming (distill insight: 命名即贡献)\n\nCore phenomenon: **\"Differential Nocuity\"** — all policy ambiguity types are nocuous for LLM agents (+34.0pp, all 5 models), but vulnerability varies by BOTH type and model. Incompleteness is universally dangerous (46-62%), while auth_scope vulnerability depends dramatically on safety training (12% Claude to 64% GPT-5.4). Unlike human RE where organizational context renders most ambiguity innocuous, agents lack disambiguation channels AND their safety training creates type-specific blind spots.\n\nSecondary phenomenon: **\"Ambiguity Blindness\"** — agents process grammatically fluent ambiguous clauses without meta-cognitive awareness of the ambiguity, adopting surface interpretations. Contrasts with explicit rule conflicts where agents show awareness and choose conservatively.\n\nTertiary phenomenon: **\"Disambiguation Channel Framework\"** [renamed from \"Hypothesis\" per Dream review SF-5] — the layer hierarchy reflects availability of external disambiguation: linguistic ambiguity (coreferential, lexical) can sometimes be resolved by tool responses, user context, or world knowledge; specification ambiguity (auth_scope, incompleteness) has no external resolution channel, forcing agents to guess. This is an explanatory framework supported by observational evidence (ICC pattern, failure mode distribution, coreferential boundary case), not a tested causal hypothesis. Future Work: manipulation experiment (inject spec-layer disambiguation info into tool responses, test if gap shrinks).\n\nQuaternary phenomenon: **\"Systematic Nocuity\"** [per Dream review SF-7] — B&K framework distinguishes nocuous (divergent interpretations) from innocuous (convergent). Our data reveals a third type: all models converge on the same WRONG interpretation (27% of ambiguous episodes). This is more dangerous than divergent nocuity — it's invisible in inter-model agreement metrics and appears \"correct\" until compared against ground truth. Proposed as B&K extension in Discussion.\n\n## Opening Hook Strategy (distill insight: 具体案例, 不要 \"Recently...\")\n\nOpen with a concrete τ²-bench failure: e.g., a customer returns a customized item within the return window; the agent grants a full refund + free return shipping because the policy says \"items may be returned within 30 days\" (scopal: \"items\" scopes over all categories including custom). The unambiguous version specifies \"standard items only\" — agent correctly refuses. One word of ambiguity → $200 unauthorized refund.\n\n## Narrative Type: 突破局限型 (distill pattern, 5/8 papers)\n\n\"DRIP-R classifies 5 ambiguity types and shows models disagree on interpretation → but does not measure whether this disagreement leads to safety violations. We close this gap — and find the answer is surprising: not all types are equal, specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones.\"\n\n## Benchmark Comparison Table (distill insight: 必有 feature matrix)\n\n| Feature | DRIP-R | PhantomPolicy | PolicyBank | AgentPex | **Ours** |\n|---------|--------|---------------|------------|----------|----------|\n| Ambiguity taxonomy | 5 RE types | — | 3 gap types | — | **6 types (2-layer)** |\n| Causal design | — | — | — | — | **matched pairs** |\n| Safety violation metric | — | binary | — | procedural | **3-tier severity** |\n| Cross-type comparison | descriptive | — | — | — | **statistical (χ² + V)** |\n| Models tested | 6 API | 4 API | 2 API | 2 API | **3 API + 2 open-source** |\n| Domain | retail | mixed | retail | telecom/retail/airline | **retail + airline** |\n\n## Contribution Positioning (for EMNLP) [revised 2026-05-20 with 5-model data]\n\n1. **Causal quantification of ambiguity's safety impact**: First matched-pair causal study of policy ambiguity → agent safety violations. Binary effect +34.0pp (OR=15.1, p<0.0001) across 5 architecturally diverse models and 6 ambiguity types. Perturbation control (Δ_perturb=3.33pp) confirms ambiguity-specific causation. Strongest causal evidence in the agent safety literature.\n2. **Differential Nocuity framework + Model × Type Interaction**: Not all ambiguity is equally dangerous, and not all models are equally vulnerable. 3-tier type hierarchy (incompleteness >> mid cluster >> coreferential). Model × type interaction reveals 52pp range in auth_scope vulnerability (Claude 12% → GPT-5.4 64%), while incompleteness remains universally dangerous (46-62%). Safety training differentially mitigates specific ambiguity types. Connects Berry & Kamsties nocuous ambiguity theory to modern safety alignment.\n3. **Type-specific failure mode taxonomy + Ambiguity Blindness**: 245 traces across 2 models and 2 domains reveal type-diagnostic failure signatures: spec-layer → guess-and-act (unauthorized_escalation, assumption_based_action); ling-layer → misparse-and-apply (scope_misapplication). Agents show <5-11% awareness of ambiguity (\"Ambiguity Blindness\"), with >88% surface adoption and <1% user escalation. Practical implication: ambiguity detection must be externalized.\n\nNOTE: C3 (layer effect, Δ=6.08pp) is a component finding supporting contribution #2. The MODEL × TYPE interaction (C4) is now MORE central than the layer main effect. \"Disambiguation channel\" is an explanatory framework (not hypothesis — per SF-5). DeBERTa classifier, if included, is a preliminary PoC appendix, not a contribution.\n\n## Required Reference Expansion [Dream A2 + MF-4 RE literature gap]\n\nCurrent plan has thin references. Must add (≥25 total in final paper):\n- **Nocuous ambiguity detection (CRITICAL — MF-4)**: Chantree, Nuseibeh, de Roeck & Willis (2006, ASE) — first computational nocuous ambiguity detection; Chantree et al. (2008, RLAC) — expanded. Direct lineage to our DeBERTa classifier.\n- **Cross-domain RE ambiguity**: Ferrari, Spagnolo & Gnesi (2017-2019, ASE) — NLP-based cross-domain ambiguity detection. NLP4RE community work.\n- **Good-enough processing**: Ferreira, Bailey & Ferraro (2002); Ferreira & Patson (2007)\n- **LLM garden-path (SF-6)**: Li et al. (2024) — incremental comprehension of garden-path sentences by LLMs. Directly relevant to how LLMs process ambiguity.\n- **Anaphoric ambiguity (SF-6)**: Poesio & Artstein (2005, 2008) — annotation of anaphoric ambiguity. Poesio (2004) \"Ambiguity\" encyclopedia entry.\n- **Surprisal/expectation-based**: Levy (2008); Hale (2001)\n- **Instruction-following robustness**: Zhou et al. (IFEval, 2023); Qin et al. (ToolBench, 2024)\n- **Prompt sensitivity**: Sclar et al. (2024); Lu et al. (2022)\n- **Broader agent safety**: R-Judge, ToolEmu, InjecAgent\n- **Formal semantics of vagueness**: Lassiter & Goodman (2017)\n- **Garden-path**: Frazier & Rayner (1982)\n- **Ambiguity detection**: Willis et al. (2008); Ezzini et al. (TAPHSIR, 2022)\n- **Year verification needed**: Massey et al. — §1 引用 2013 vs 后文 2014, 需确认正确年份\n\n## Code/Data Release Plan [Dream A6 — three-tier consistent]\n\nMust commit to releasing:\n1. All 300 clause pairs (ambiguous + unambiguous variants) with type labels\n2. Evaluation scripts (τ²-bench integration, cross-judge pipeline)\n3. Statistical analysis code (all tests, bootstrap CI computation)\n4. Agent trace samples (anonymized) for reproducibility of C5\n\n## Figure Plan [Dream A12]\n\nMinimum figures for paper (zero-figure paper flagged in dream):\n1. **Figure 1**: System architecture / experimental pipeline overview (§4 Method)\n2. **Figure 2**: Forest plot — per-type binary effect sizes with 95% CI (§5 C1)\n3. **Figure 3**: Model × Type heatmap — violation rates across 4 models × 6 types (§5 C4)\n4. **Figure 4**: Visibility mechanism — CP vs scopal violation rates + trace evidence (§5 C3)\n5. **Figure 5**: Failure mode × type stacked bar/Sankey — per-type failure mode distribution (§6 C5)\n6. **Figure 6**: Cross-model failure mode consistency — side-by-side gpt-5.4 vs gpt-4.1 per-type distributions showing 5/6 convergence (§6 C5, supports C4)\n7. **Figure 7**: Annotated trace pair — CP (conflict detection) vs scopal (surface adoption) (§6 C5)\n\n## Berry & Kamsties Operationalization Note [Dream best Q5]\n\nBerry & Kamsties define nocuity as inter-reader divergence. Our design measures agent-vs-intent deviation. Full study should additionally test whether different models adopt different readings of the same ambiguous clause (true inter-model nocuity). If 4 models produce 4 different interpretations of the same clause → true nocuity. If all 4 adopt the same wrong interpretation → systematic bias, still nocuous but for different reason. Report inter-model agreement on ambiguous clauses as supplementary analysis.\n\n## Contingency Framing [RESOLVED — Scenario C occurred]\n\n> plan_002 结果: Scenario C 发生（omnibus p=0.0001, 所有类型 nocuous 但 severity 有显著差异）。\n> Framing 已 pivot 到 \"Differential Nocuity\" + \"Layer Hierarchy\" (D020)。本节仅保留历史记录。\n\n## Claude Baseline — RESOLVED [2026-05-20]\n\n✅ Claude works via OpenRouter proxy (47.94.22.126/v1) with provider prefix `anthropic/claude-sonnet-4-6`. 600 episodes complete (plan_002c). Claude shows lowest overall vulnerability (30.3%) and remarkable auth_scope robustness (12% vs GPT-5.4 64%).\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: full_study_clause_generation\n  claim: C1, C2, C3\n  description: 'Generate remaining clauses for full study: coreferential (50 new),\n    authorization_scope (50 new), lexical (+20 to reach 50), incompleteness (+20 to\n    reach 50). Total 140 new clauses. Validate all 300 clauses (50/type × 6 types)\n    for completeness and cross-type balance. Mix CP format per Reviewer suggestion\n    (labeled + unlabeled).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n- id: plan_001b\n  name: new_type_mini_pilot\n  claim: C1 (validation)\n  description: 'Mini-pilot for coreferential + authorization_scope (never tested):\n    5 clauses/type × 2 conditions × 1 model (gpt-5.4) = 20 episodes. Verify: (a) ambiguous\n    triggers violations (b) unambiguous control < 15%. If systematic issues found,\n    fix clause design before full study. API cost negligible (~$2). Per Reviewer warning\n    on untested types.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_002\n  name: full_study_api\n  claim: C1, C2, C3, C4, C5\n  description: 'Run 300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6)\n    = 1,800 episodes on τ²-bench. Cross-judge evaluation. Output: episodes.jsonl +\n    judgments.jsonl. No GPU needed. Claude via OpenRouter proxy (base_url=http://47.94.22.126/v1).\n    [2026-05-20] Claude added per distill gap (4/8 papers use Claude baseline).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_001b\n  - plan_010\n  status: planned\n- id: plan_003\n  name: full_study_opensource\n  claim: C1, C2, C3, C4, C5\n  description: 'Run 300 clauses × 2 conditions × 2 open-source models via OpenRouter\n    API: qwen/qwen3-235b-a22b (235B MoE, Alibaba) + deepseek/deepseek-chat-v3-0324\n    (DeepSeek) = 1,200 episodes on τ²-bench. Cross-judge uses API models. Can run\n    in parallel with plan_002. No GPU needed. [2026-05-20] Pivoted from local GPU\n    → API: OpenRouter proxy confirmed to support Qwen3 and DeepSeek models. Eliminates\n    48h GPU requirement. Provider prefix required (e.g. qwen/qwen3-235b-a22b, not\n    qwen3-235b-a22b).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_004\n  name: full_study_analysis\n  claim: C1, C2, C3, C4\n  description: 'Statistical analysis of full study data (3,000 episodes): (a) Binary\n    effect per type with bootstrap CI (C1) (b) Omnibus χ² + pairwise across 6 types\n    (C2) (c) Visibility comparison: CP vs scopal rates (C3) (d) Model × type interaction:\n    5×6 contingency + logistic regression (C4) Report effect sizes + CI for all comparisons\n    per Reviewer suggestion. [Dream A3] Power analysis: report MDE for C2 (given N=250/type\n    pooled) and C3 (given N=250 per type). If V < 0.20 but MDE > observed V, discuss\n    underpowered possibility. [Dream A4] TOST equivalence test with both ±15pp and\n    ±10pp margins. Justify margin choice explicitly. [Dream A10] Report per-type information\n    delta (token count difference between ambiguous and unambiguous variants) as control\n    variable. [Dream B&K] Inter-model agreement on ambiguous clauses: do 5 models\n    adopt same or different interpretations? (supplementary analysis)\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_005\n  name: error_analysis\n  claim: C5\n  description: \"Qualitative analysis of agent traces from full study: (a) Sample 50\\\n    \\ violation traces per type (300 total) (b) Classify failure modes (scope misapplication,\\\n    \\ conservative refusal,\\n    assumption-based action, arbitrary rule selection,\\\n    \\ etc.)\\n(c) Cross-type failure mode distribution (d) Visibility mechanism: compare\\\n    \\ CP traces (explicit conflict detection\\n    behavior) vs scopal traces (surface\\\n    \\ scope adoption without awareness)\\n(e) Model-specific failure patterns (connect\\\n    \\ to C4)\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_006\n  name: reliability_test\n  claim: C1, C2\n  description: 'Test-retest reliability: select 30 representative clauses (5/type),\n    run 3 independent replicates × 2 conditions × 2 API models (gpt-5.4, gpt-4.1)\n    = 360 episodes. Local models added when plan_003 GPU available. Compute ICC for\n    per-clause violation rates. Addresses Reviewer warning about ±8pp sampling noise\n    (scopal 51.7% → 43.3% across MVP/diag). Bootstrap CI width should be < 10pp for\n    key comparisons. [2026-05-20] API portion: 330/360 episodes complete (28/30 clauses),\n    judgments pending.\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  status: planned\n- id: plan_007\n  name: realism_validation\n  claim: C1 (methodological)\n  description: \"Validate synthetic ambiguity injection realism: (a) Linguistic property\\\n    \\ comparison with DRIP-R natural ambiguities\\n    (sentence length, parse depth,\\\n    \\ Flesch-Kincaid, TTR) + KS tests\\n(b) Optional: discriminator test if DRIP-R\\\n    \\ data accessible Addresses RC4 (ecological validity).\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_009\n  name: judge_calibration\n  claim: C1 (methodological)\n  description: 'LLM-as-judge calibration per distilled research norm (5/8 papers):\n    (a) Sample 100 episodes stratified by type×model×condition (b) Human expert labels\n    (2 annotators, target κ ≥ 0.75) (c) Compute judge precision/recall/F1 against\n    human ground truth (d) Per-severity-tier agreement rates (e) Report in Method\n    section as standard practice per AgentAuditor/DRIP-R [Dream A7] Upgraded P1→P0:\n    Dream best-tier reviewers identified this as \"single most critical missing validation.\"\n    Without it, entire measurement chain from episode to violation label is unvalidated.\n    κ=0.91 measures LLM-LLM agreement, not accuracy.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  name: perturbation_control\n  claim: C1 (causal validity)\n  description: '[Dream A9] Non-ambiguity perturbation control arm to distinguish ambiguity-specific\n    harm from general prompt brittleness. Generate 30 clause pairs with non-ambiguity\n    perturbations: (a) 15 synonym substitution pairs (replace key terms with synonyms)\n    (b) 15 clause reordering pairs (reorder conditions without changing meaning) Run\n    30 × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6) = 180 episodes.\n    Key metric: Δ_net = Δ_ambiguity - Δ_perturb (net ambiguity-specific effect). [Reviewer升级]\n    必须在 plan_002/003 full study 之前完成—— 如果 perturbation Δpp ≈ ambiguity Δpp，2,400 episodes\n    全部无效。 低成本验证（30 pairs + 120 episodes API）优先于高成本投入。 [判定标准 — 5 档]: PASS: Δ_perturb\n    < 5pp (CI含0), ratio < 0.15 → C1 因果 claim 最强形式 PASS+caveat: 5-10pp, ratio 0.15-0.30\n    → 报告 perturbation baseline, C1 写 net effect CONDITIONAL: 10-15pp, ratio 0.30-0.45\n    → 需 Δ_net > 20pp 且显著才可发表 WARNING: 15-20pp, ratio 0.45-0.60 → C1 改为 \"additional\n    violations beyond sensitivity\" FAIL: > 20pp, ratio > 0.60 → 无法声称 ambiguity-specific,\n    需根本重新设计 [Power 注意]: N=120 对 10pp 差异 power ≈ 30%. 用 CI 宽度判定, 非 p-value. 若 CI 过宽(>15pp\n    width), 追加 60 episodes 压窄至 <10pp width. 输出标准化 verdict 文件: perturbation_Δpp, ambiguity_Δpp,\n    net_Δpp, CI, ratio, verdict.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_008\n  name: classifier_poc\n  claim: practical contribution\n  description: 'Binary ambiguity detector PoC: fine-tune DeBERTa-v3-large on annotated\n    clause pairs (ambiguous/unambiguous labels). Eval on held-out set. Demonstrates\n    practical applicability of findings. Phase 3 from IDEA_BRIEF, scoped to PoC for\n    EMNLP.\n\n    '\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: diag_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_002\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_006\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_009\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan_002c\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_003a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_003b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_004\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T04:23:54.610Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T04:23:54.610Z",
  "sessionId": "bbbefa27-3d72-4fb3-9d7d-bdb8c8bb7c9d"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T04:23:54.632Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：C1/C2/C4/C5 成立但部分效应量缩水，C3 layer effect 保持 fragile（within-judge 不显著），judge calibration 中等，需调整部分 claim 表述强度
核心假设：['C1 binary effect 成立但效应量略低于 5-model 聚合值，部分模型 effect size 缩水 5-8pp', 'C2 type hierarchy omnibus 显著但 V<0.15，3-tier 结构中 mid-tier 内部差异不显著', 'C3 layer effect pooled 显著 (p<0.05) 但 within-judge 子组均不显著 (p>0.10)，只能报告 suggestive', 'C4 model×type interaction 存在但 auth_scope 极差缩小至 30-40pp 范围', 'plan_010 perturbation control 判定 PASS+caveat (Δ_perturb 5-10pp)', 'plan_009 judge calibration κ=0.65-0.79，F1=0.75-0.84，部分 severity tier 分类不稳定', 'C5 failure mode 5-model 扩展后，2-3 个 type 的 dominant mode 在新模型上不一致']
关键指标范围：{'C1_binary_effect_pp': [25, 35], 'C1_mcnemar_OR': [8, 15], 'C2_omnibus_chi2_p': ['1e-4', 0.01], 'C2_cramers_V': [0.09, 0.15], 'C2_incomp_minus_coref_pp': [12, 20], 'C3_layer_gap_pp': [3, 8], 'C3_within_judge_p': [0.1, 0.3], 'C4_auth_scope_range_pp': [30, 45], 'C4_incomp_range_pp': [15, 25], 'C4_fleiss_kappa': [0.25, 0.4], 'C5_awareness_rate_pct': [5, 15], 'C5_surface_adoption_pct': [78, 90], 'perturbation_delta_pp': [5, 10], 'judge_human_kappa': [0.65, 0.79], 'judge_F1': [0.75, 0.84]}
叙事方向：核心叙事保持但需降低三处 claim 强度：(1) C3 layer effect 从 'significant' 降为 'suggestive tendency'，Disambiguation Channel 从 explanatory framework 进一步降为 'observed pattern consistent with'，layer 部分移入 Discussion 而非 Results 的核心位置；(2) perturbation control 需报告 net effect (Δ_net = Δ_ambiguity - Δ_perturb)，C1 写 'ambiguity causes violations substantially beyond general prompt sensitivity' 而非 'ambiguity-specific'；(3) C5 failure mode 跨模型一致性从 '5/6 types converge' 改为 'majority of types show consistent signatures, with model-dependent variation in X types'。C4 model×type interaction 仍是 star finding 但需 soften auth_scope 的 safety training 解释（极差缩小意味着可能是 prompt format 差异而非 training 差异）。Title 可能需从 'Differential Vulnerability Profiles' 微调为更保守表述。仍可冲 EMNLP，但需补充 1-2 个 robustness check 作为 appendix。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: policy_ambiguity_safety
venue: emnlp-2026

## paper_framing.md

# Paper Framing — policy_ambiguity_safety

> 最后更新: 2026-05-20 19:30 UTC | 状态: 5-model analysis complete, C3/C4 framing revised
> 目标: EMNLP 2026 (ARR Aug cycle, DDL ~Aug 3)
> Dream: dream_20260520T112859 — best 3.5 / median 3.0 / worst 2.5 (pre-pivot; re-dream needed)
> 5-model: 2,997 episodes, C1 confirmed (+34.0pp, 5 models), C4 upgraded (model×type interaction)

## Core Insight

Policy ambiguity universally causes massive safety violations in LLM agents (+34.0pp across 5 architecturally diverse models), with a significant type hierarchy (incompleteness 53.6% >> coreferential 31.6%). Specification-layer types are more dangerous on average (Δ=6.08pp, p=0.017), but the deeper finding is a **model × type interaction**: authorization scope vulnerability varies 52pp across models (12% Claude to 64% GPT-5.4), revealing that safety training differentially mitigates specific ambiguity types, while incompleteness remains universally dangerous. This interaction connects Berry & Kamsties' nocuous ambiguity theory to modern safety alignment and suggests both type-aware triage AND model-aware risk assessment.

## Title (Working)

"Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families"

Alternative: "Differential Nocuity: How Ambiguity Type and Model Architecture Shape Safety Violations in LLM Agents"

Note: Pivoted from "Uniformly Nocuous" → "Specification-Layer Dominant" (2-model) → "Differential Nocuity with Model Interaction" (5-model). The model × type interaction is the novel finding that elevates the paper beyond simple effect demonstration.

## Core Claims

### C1: Binary Effect (PRIMARY — confirmed, 5 models)
Ambiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +34.0pp (5-model), McNemar OR=15.1 (CI: [10.78, 21.17]), p<0.0001. Holds across all 6 types and all 5 models.
- **Evidence**: 2,997 episodes across 5 models × 6 types × 2 conditions. Bootstrap CI: [+31.2pp, +36.9pp].
- **Per-model**: Claude +25.7pp, Qwen3 +32.4pp, GPT-4.1 +34.7pp, GPT-5.4 +38.3pp, DeepSeek +39.0pp — all p<10^-17.
- **Strength**: Extremely strong. Replicated across 5 architecturally diverse models (proprietary dense, open-source MoE, open-source dense), 6 types, 2 domains. No exceptions.
- **Causal backing**: Matched-pair design + perturbation control (plan_010, Δ_perturb=3.33pp, PASS) → strongest causal inference in the literature.
- **Logistic regression**: condition_amb coef=2.278, z=19.65, p<0.001 — ambiguity is the dominant predictor even after controlling for token delta, model, and type.

### C2: Type Hierarchy (SECONDARY — confirmed, 5 models)
**PIVOTED from uniformity null.** 6-type hierarchy significant: omnibus χ²=28.02, p=3.6×10^-5, V=0.137 (small but well-powered: actual power=0.993, MDE=0.093). 3-tier structure emerges from TOST analysis.
- **Evidence**: 2,997 episodes (5 models × 6 types × 2 conditions, ambiguous only: 1,499 episodes)
  - **High tier**: incompleteness 53.6% (standout — universally dangerous across all models)
  - **Mid tier**: lexical 42.8%, auth_scope 41.6%, scopal 39.4%, CP 36.8% — pairwise equivalent at ±15pp
  - **Low tier**: coreferential 31.6% (lowest — partial disambiguation via tool responses)
- **TOST structure**: ±15pp: 8/15 equivalent, 7/15 non-equivalent. ±10pp: 4/15 equivalent, 11/15 non-equivalent. Types are NOT interchangeable.
- **V=0.137 context**: Below 0.20 threshold but well-powered (power=0.993). The type effect is real but small — the 3-tier structure captures it better than a single V statistic. The heterogeneity is driven by the extremes (incompleteness 53.6% vs coreferential 31.6% = 22pp gap).
- **Coreferential as boundary case**: 31.6% violation rate is the lowest but still substantial (+18.7pp vs unambiguous). Agents partially disambiguate via tool responses and cautious strategies. Conservative_refusal rate 6-11% (vs avg 2-3%).
- **Model-dependence of type rankings**: Type rankings are NOT identical across models. Incompleteness is top-2 for ALL models, but auth_scope ranges from #1 (GPT-5.4, DeepSeek) to #6 (Claude). See C4.

### C3: Layer Effect (TERTIARY — suggestive, fragile under within-judge analysis)
**[2026-05-20 REVISED with 5-model data + within-judge check]** Specification-layer ambiguities cause more violations than linguistic-layer on average, but the effect is modest, model-dependent, and fragile under subgroup analysis.
- **Evidence (5-model aggregate)**: Spec 44.0% vs Ling 37.9%, Δ=6.08pp, CI [1.14, 11.02], χ²=5.73, p=0.017, V=0.062 (small), OR=1.29 [1.05, 1.58].
- **Within-judge fragility**: gpt-4.1 judged group (gpt-5.4+DeepSeek): Δ=+8.0pp, p=0.059 (marginal). gpt-5.4 judged group (gpt-4.1+Claude+Qwen3): Δ=+4.8pp, p=0.157 (n.s.). Pooled significance may partly reflect between-judge variance or insufficient within-group power. Paper表述: "suggestive" or "a moderate tendency," NOT "confirmed." Disclose within-judge non-significance in Limitations.
- **Per-model layer gaps** (THE KEY FINDING — feeds C4):
  - GPT-5.4: +14.0pp (spec 48.0% vs ling 34.0%) — strong
  - GPT-4.1: +12.0pp (spec 46.7% vs ling 34.7%) — strong
  - Claude: +3.3pp (spec 32.0% vs ling 28.7%) — weak
  - DeepSeek: +2.0pp (spec 50.7% vs ling 48.7%) — negligible
  - Qwen3: -0.9pp (spec 42.7% vs ling 43.6%) — reversed!
- **Root cause**: auth_scope is the primary driver. GPT models have extremely high auth_scope rates (46-64%), inflating their spec-layer average. Claude (12%) and Qwen3 (26%) have low auth_scope, so their spec-layer advantage disappears.
- **Framing decision**: C3 is NOT "spec-layer nearly twice as dangerous" (that was 2-model artifact). The correct framing is: "Specification-layer types are significantly more dangerous on average (Δ=6.08pp, p=0.017), but this aggregate masks a model × type interaction where the gap varies from +14pp (GPT-5.4) to -1pp (Qwen3). The interaction, not the main effect, is the theoretically interesting finding (see C4)."
- **Info delta as mediator** [MF-2]: Token delta significant in 5-model logistic regression (coef=0.022, z=3.49, p=0.0005). Spec-layer clauses require more tokens to disambiguate (auth_scope 36.1, incomp 34.6 vs coref 7.8 tokens). Info delta partially mediates but doesn't eliminate the condition effect (condition_amb coef=2.278 dominates).
- **Layer overlap persists**: CP (36.8%, spec) < scopal (39.4%, ling). Mid-tier cluster spans both layers. Layer effect is driven by extremes: incompleteness (53.6%, spec) vs coreferential (31.6%, ling).
- **ICC convergent evidence** [plan_006]: Per-type ICC mirrors layer hierarchy — Ling-layer ICC all excellent (scopal 0.989, lexical 0.981, coref 0.976), Spec-layer ICC all good (auth 0.857, CP 0.856, incomp 0.807). Spec-layer less reproducible — agents guess differently each run when external disambiguation channels are absent.
- **CL connection**: Parallels pragmatics vs semantics distinction. Good-enough processing (Ferreira et al. 2002). Disambiguation channel framework: linguistic ambiguity has partial external resolution; specification ambiguity forces guessing.

### C4: Model × Type Interaction (UPGRADED — star finding, 5 models complete)
**[2026-05-20 DEFINITIVE, 5/5 models]** Models show significantly different vulnerability profiles despite universal binary effect. The interaction is the paper's most novel finding.
- **Model main effect**: Overall χ²=31.02, p=3.0×10^-6, V=0.102. Ambiguous-only: χ²=24.01, p=7.9×10^-5.
  - Vulnerability ranking: Claude 30.3% < GPT-5.4 41.0% ≈ GPT-4.1 40.7% < Qwen3 43.1% < DeepSeek 49.7%
  - Bootstrap CI confirms: Claude significantly lower than all others; DeepSeek significantly higher than GPT models.
- **Model × Type interaction matrix** (ambiguous condition, violation rates):
  ```
  Type                  GPT-5.4  GPT-4.1  Claude  Qwen3   DeepSeek
  authorization_scope     64%     46%      12%     26%     60%
  conditional_precedence  34%     36%      36%     40%     38%
  incompleteness          46%     58%      48%     62%     54%
  lexical                 42%     34%      32%     52%     54%
  coreferential           18%     32%      22%     42%     44%
  scopal                  42%     38%      32%     37%     48%
  ```
- **Key interaction patterns**:
  - **auth_scope**: 52pp range (Claude 12% → GPT-5.4 64%). The MODEL-DIFFERENTIATING type. Claude's RLHF appears to specifically train authorization boundary awareness.
  - **coreferential**: 26pp range (GPT-5.4 18% → DeepSeek 44%). Second most model-dependent. Open-source models struggle more with referential ambiguity.
  - **incompleteness**: Universally high (46-62%, 16pp range). ALL models fail on missing information — safety training doesn't help when information literally isn't there.
  - **CP**: Most model-invariant (34-40%, 6pp range). Explicit rule conflicts treated similarly by all architectures.
- **Per-model type χ²** (which models show type-specific vulnerability patterns):
  - GPT-5.4: χ²=23.44, p=0.0003, V=0.28 — strongest type differentiation (very high auth_scope, very low coref)
  - Claude: χ²=17.87, p=0.003, V=0.24 — strong differentiation (very low auth_scope, moderate others)
  - Qwen3: χ²=15.89, p=0.007, V=0.23 — moderate differentiation (high incomp+lex, low auth_scope)
  - GPT-4.1: χ²=9.89, p=0.078, V=0.18 — borderline
  - DeepSeek: χ²=6.31, p=0.277, V=0.14 — NOT significant (uniformly high across all types)
- **Fleiss κ = 0.384 (fair agreement)**: Models only moderately agree on which specific clauses trigger violations. The binary effect is universal, but the WHICH-clauses question is model-dependent.
- **Theoretical implications**: (1) Safety training differentially addresses specific ambiguity types — Claude's auth_scope robustness suggests authorization boundary handling was explicitly or implicitly trained. (2) Incompleteness is a "safety training blind spot" — all models fail equally. (3) DeepSeek's uniform vulnerability suggests less type-specific safety training.
- **Framing**: C4 from "models agree" → "Models show systematically different vulnerability profiles. The binary effect is universal, but HOW models fail depends on the intersection of ambiguity type and safety training approach. auth_scope is the canary type — most sensitive to safety training quality."
- **Evidence from plan_005**: 2-model failure modes consistent (5/6 dominant modes identical). 5-model failure mode analysis pending.
- **Layer effect moderation**: C3's aggregate layer gap (6.08pp) is driven by GPT models' high auth_scope rates. The layer effect is itself model-dependent (GPT +12-14pp, Claude +3pp, Qwen3 reversed), making the MODEL × TYPE interaction more fundamental than the LAYER main effect.

### C5: Error Analysis (CONFIRMED — EMNLP core)
Different ambiguity types produce qualitatively different failure modes with type-specific signatures. plan_005 (123+122 violation traces across gpt-5.4 and gpt-4.1, confidence=0.94).
- **Evidence**: plan_005 complete (gpt-5.4: 123 traces, gpt-4.1: 122 traces). Key findings:
  - **Type-specific failure signatures**: auth_scope → unauthorized_escalation (72%/83%); incompleteness → assumption_based_action (61%/66%); scopal → scope_misapplication (76%/74%); lexical → assumption_based_action (71%/53%); CP → scope_misapplication (41%/28%) + arbitrary_rule_selection (29%/28%); coreferential → scope_misapplication (44%) / assumption_based_action (38%)
  - **Cross-model consistency**: 5/6 types share the same dominant failure mode across gpt-5.4 and gpt-4.1. Only coreferential diverges (scope_misapplication vs assumption_based_action). Overall mode distribution nearly identical: both ~33% assumption_based_action, ~26-32% unauthorized_escalation, ~25-28% scope_misapplication. Failure mode profiles are type-specific, not model-specific.
  - **Layer mechanism**: Ling-layer dominated by scope_misapplication (39% ling avg vs 15% spec avg) = "misparse"; Spec-layer dominated by unauthorized_escalation + assumption_based_action = "active guessing" → explains higher violation rates
  - **Ambiguity Blindness empirically confirmed**: awareness rate gpt-5.4=4.1%, gpt-4.1=10.7% (both very low); surface_adoption >88% all types both models; escalate_to_user <1%. Nuance: gpt-4.1 (mid-tier) shows 2.6× higher awareness than gpt-5.4 (frontier) — awareness may inversely correlate with action-orientation (frontier models more "confident," act without hesitation)
  - **Cross-domain consistency**: airline vs retail failure mode profiles Δ < 13pp (unauthorized_escalation shows largest domain effect: retail 38.6% vs airline 26.1%)
  - **Coreferential boundary**: conservative_refusal 6-11% (vs avg 2-3%) partially explains low violation rate — agents sometimes pause rather than guess. N=25 combined traces show no single dominant failure mode (flat distribution: scope_misapplication 32%, assumption_based_action 28%, unauthorized_escalation 16%) — contrasts with other types' sharp signatures, reflecting the diversity of resolution strategies for referential ambiguity
  - **Lexical surprise**: 53-71% assumption_based_action — agents treat word ambiguity as information gap, not misparse
- **Automated inter-coder agreement** [MF-5, Reviewer-validated]: Cross-coding 60 traces (gpt-5.4 vs gpt-4.1 as independent coders). 4-category merged: 80% agreement, Cohen's κ=0.594 (moderate). κ deflated by kappa paradox — lexical 91.7% agreement → κ=0.0 (11/12 same label, chance agreement also high), scopal 100% agreement → κ undefined. True disagreement concentrated at unauthorized_escalation ↔ inappropriate_action boundary in auth_scope (κ=0.054) and incompleteness (κ=0.233).
  - **Reporting strategy** [Reviewer recommendation]: (1) Compute Gwet's AC1 as primary metric (designed for kappa paradox, expected 0.70-0.75); (2) Report 80% agreement + 5/6 dominant mode consistency as headline validity evidence; (3) Report κ honestly with kappa paradox caveat; (4) Auth_scope failure mode: soften to "dominated by boundary-exceeding behaviors (unauthorized_escalation or inappropriate_action, >90%)" instead of specific percentages; (5) Fine-grained 6-type as appendix with "automated coding" caveat.
  - **C5 safety**: Ambiguity Blindness (<5-11%), surface_adoption (>88%), layer mechanism (ling→scope vs spec→escalation) all robust. Fine-grained per-type percentages unreliable at κ=0.594. Plan_009 human anchor (20-30 failure mode traces) would upgrade from "moderate automated" to validated.
- **EMNLP value**: Highest. Provides the linguistic WHY behind the quantitative WHAT. Cross-model + cross-domain consistency elevates from anecdotal to systematic finding. "Ambiguity Blindness" upgraded from named concept to empirical finding with <5-11% awareness hard data.

## Narrative Structure (CL-first for EMNLP)

### Intro Logic Chain
1. Agent policies are written in NL → contain ambiguity (established)
2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact
3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.
4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter? Does it depend on the model?
5. **This paper**: First causal, type-granularity, cross-model study. Matched-pair design + perturbation control isolates ambiguity effect. 5 models × 6 types.
6. **Core findings**: (a) All ambiguity is nocuous (+34.0pp, 5 models), (b) type DOES predict severity — 3-tier hierarchy with incompleteness most dangerous, (c) models show dramatically different vulnerability profiles — auth_scope varies 52pp across models, suggesting safety training differentially addresses ambiguity types, (d) while incompleteness remains universally dangerous, a "safety training blind spot."

### Section Map
- **§1 Intro**: Gap + contributions (causal map + differential nocuity + model×type interaction)
- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R
- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R
- **§4 Method**: Matched-pair causal design, τ²-bench, 5 models (3 proprietary + 2 open-source), clause generation, perturbation control, cross-judge evaluation
- **§5 Results**: C1 (binary, +34.0pp, 5 models) → C2 (type hierarchy, 3-tier) → C3 (layer effect, modest but significant) → C4 (model×type interaction — star finding)
- **§6 Analysis**: C5 error analysis — qualitative failure modes per type. Ambiguity Blindness. Model-specific patterns.
- **§7 Discussion**: Differential nocuity theory. Safety training selectivity. Disambiguation channel framework. Limitations (2 domains, synthetic injection, LLM-as-judge).
- **§8 Conclusion**: All policy ambiguity is nocuous, but type AND model jointly determine risk level. Both type-aware auditing and model-specific risk assessment recommended.

## Anticipated Reviewer Concerns

### RC1: "Type effect could be artifact of taxonomy granularity"
**Response**: (a) Layer effect (Spec vs Ling ~19pp gap) is robust — holds even if individual types are reclassified. (b) 2-layer structure grounded in Li et al. + Massey et al. (c) Coreferential's low rate has structural explanation (disambiguation channels), not just noise. (d) TOST confirms types are NOT equivalent (0/15 pairs at ±10pp).

### RC2: "Taxonomy is ad hoc / why these 6 types"
**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).

### RC3: "Only API models, no open-source"
**Response**: ✅ RESOLVED. 5-model coverage spans: frontier proprietary (gpt-5.4, claude-sonnet-4-6) + mid-tier proprietary (gpt-4.1) + open-source MoE (qwen3-235b) + open-source dense (deepseek-v3). Three providers (OpenAI, Anthropic, Chinese open-source). Two architecture types (dense, MoE). Model×type interaction (C4) reveals rich cross-model patterns.
**Note [Reviewer 2026-05-20]**: Cross-judge asymmetry — Claude judged by gpt-5.4, gpt-5.4 judged by gpt-4.1. Must disclose in Method. plan_009 judge calibration measures this bias.

### RC4: "Synthetic ambiguity injection lacks ecological validity"
**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.

### RC5: "τ²-bench limited to retail/airline"
**Response**: Acknowledged limitation. Two domains already show consistent effects. Cross-domain transfer is Future Work (Phase 3 classifier PoC, if time permits). DRIP-R also single-domain (retail).

### RC6: "Binary effect is obvious — of course ambiguity causes errors"
**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOES predict severity — specification-layer ambiguities are nearly twice as dangerous, connecting to disambiguation channel availability.

### RC7: "Incompleteness matched-pair confound (information asymmetry)"
**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.

### RC8: "RC attachment in coreferential overlaps with scopal / structural ambiguity"
**Response**: (a) Our scopal category is explicitly scoped to quantifier/negation/modal scope interactions, not syntactic attachment. (b) RC attachment in policies manifests as *referential* confusion (which entity does the clause modify?) not *scope* confusion (which operator takes wide scope?). (c) Li et al. 2024 distinguishes syntactic ambiguity (including RC attachment) from scopal ambiguity — our grouping follows their treatment that RC attachment is closer to coreferential than scopal in terms of downstream interpretation. (d) Empirically, if the distinction were problematic, coreferential and scopal would show identical violation patterns — the error analysis (C5) can test whether their failure modes differ.

### RC9: "authorization_scope is just a subtype of incompleteness"
**Response**: (a) Incompleteness = missing conditions/exceptions/boundaries (structural absence). Authorization scope = ambiguous permission/role boundaries that ARE stated but vague (e.g., "authorized personnel" without specifying which functions). (b) The disambiguation pattern differs: incompleteness adds new conditions; auth_scope clarifies existing permission boundaries. (c) Empirically testable: if they were the same, their violation patterns and failure modes (C5) would be indistinguishable. (d) Report disambiguation length ratio per type as control variable in §4 Method.

### RC10: "API sampling noise undermines reliability"
**Response**: ✅ RESOLVED. plan_006 ICC=0.919 [0.892, 0.940] (excellent). (a) Per-clause violation rates highly reproducible across 3 independent replicates. (b) Binary ICC=0.847 (good). (c) Both models show near-identical ICC (gpt-5.4: 0.921, gpt-4.1: 0.918). (d) Bootstrap CI + ICC double evidence. (e) Previously identified ±8pp noise is within expected variance given the ICC confidence intervals.

### RC11: "Prompt sensitivity confound" [Dream A9 — best tier "strongest point"]
**Concern**: The +35-42pp effect is attributed entirely to ambiguity, but without a control condition using non-ambiguity perturbations (synonym substitution, clause reordering), the paper cannot cleanly distinguish ambiguity-specific harm from general prompt brittleness.
**Response**: ✅ RESOLVED. plan_010 perturbation control (120 episodes): Δ_perturb=3.33pp (CI contains 0) vs ambiguity Δ=36.5pp. Non-ambiguity surface changes cause zero meaningful effect. This is the strongest causal evidence in the agent safety literature.

## Concept Naming (distill insight: 命名即贡献)

Core phenomenon: **"Differential Nocuity"** — all policy ambiguity types are nocuous for LLM agents (+34.0pp, all 5 models), but vulnerability varies by BOTH type and model. Incompleteness is universally dangerous (46-62%), while auth_scope vulnerability depends dramatically on safety training (12% Claude to 64% GPT-5.4). Unlike human RE where organizational context renders most ambiguity innocuous, agents lack disambiguation channels AND their safety training creates type-specific blind spots.

Secondary phenomenon: **"Ambiguity Blindness"** — agents process grammatically fluent ambiguous clauses without meta-cognitive awareness of the ambiguity, adopting surface interpretations. Contrasts with explicit rule conflicts where agents show awareness and choose conservatively.

Tertiary phenomenon: **"Disambiguation Channel Framework"** [renamed from "Hypothesis" per Dream review SF-5] — the layer hierarchy reflects availability of external disambiguation: linguistic ambiguity (coreferential, lexical) can sometimes be resolved by tool responses, user context, or world knowledge; specification ambiguity (auth_scope, incompleteness) has no external resolution channel, forcing agents to guess. This is an explanatory framework supported by observational evidence (ICC pattern, failure mode distribution, coreferential boundary case), not a tested causal hypothesis. Future Work: manipulation experiment (inject spec-layer disambiguation info into tool responses, test if gap shrinks).

Quaternary phenomenon: **"Systematic Nocuity"** [per Dream review SF-7] — B&K framework distinguishes nocuous (divergent interpretations) from innocuous (convergent). Our data reveals a third type: all models converge on the same WRONG interpretation (27% of ambiguous episodes). This is more dangerous than divergent nocuity — it's invisible in inter-model agreement metrics and appears "correct" until compared against ground truth. Proposed as B&K extension in Discussion.

## Opening Hook Strategy (distill insight: 具体案例, 不要 "Recently...")

Open with a concrete τ²-bench failure: e.g., a customer returns a customized item within the return window; the agent grants a full refund + free return shipping because the policy says "items may be returned within 30 days" (scopal: "items" scopes over all categories including custom). The unambiguous version specifies "standard items only" — agent correctly refuses. One word of ambiguity → $200 unauthorized refund.

## Narrative Type: 突破局限型 (distill pattern, 5/8 papers)

"DRIP-R classifies 5 ambiguity types and shows models disagree on interpretation → but does not measure whether this disagreement leads to safety violations. We close this gap — and find the answer is surprising: not all types are equal, specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones."

## Benchmark Comparison Table (distill insight: 必有 feature matrix)

| Feature | DRIP-R | PhantomPolicy | PolicyBank | AgentPex | **Ours** |
|---------|--------|---------------|------------|----------|----------|
| Ambiguity taxonomy | 5 RE types | — | 3 gap types | — | **6 types (2-layer)** |
| Causal design | — | — | — | — | **matched pairs** |
| Safety violation metric | — | binary | — | procedural | **3-tier severity** |
| Cross-type comparison | descriptive | — | — | — | **statistical (χ² + V)** |
| Models tested | 6 API | 4 API | 2 API | 2 API | **3 API + 2 open-source** |
| Domain | retail | mixed | retail | telecom/retail/airline | **retail + airline** |

## Contribution Positioning (for EMNLP) [revised 2026-05-20 with 5-model data]

1. **Causal quantification of ambiguity's safety impact**: First matched-pair causal study of policy ambiguity → agent safety violations. Binary effect +34.0pp (OR=15.1, p<0.0001) across 5 architecturally diverse models and 6 ambiguity types. Perturbation control (Δ_perturb=3.33pp) confirms ambiguity-specific causation. Strongest causal evidence in the agent safety literature.
2. **Differential Nocuity framework + Model × Type Interaction**: Not all ambiguity is equally dangerous, and not all models are equally vulnerable. 3-tier type hierarchy (incompleteness >> mid cluster >> coreferential). Model × type interaction reveals 52pp range in auth_scope vulnerability (Claude 12% → GPT-5.4 64%), while incompleteness remains universally dangerous (46-62%). Safety training differentially mitigates specific ambiguity types. Connects Berry & Kamsties nocuous ambiguity theory to modern safety alignment.
3. **Type-specific failure mode taxonomy + Ambiguity Blindness**: 245 traces across 2 models and 2 domains reveal type-diagnostic failure signatures: spec-layer → guess-and-act (unauthorized_escalation, assumption_based_action); ling-layer → misparse-and-apply (scope_misapplication). Agents show <5-11% awareness of ambiguity ("Ambiguity Blindness"), with >88% surface adoption and <1% user escalation. Practical implication: ambiguity detection must be externalized.

NOTE: C3 (layer effect, Δ=6.08pp) is a component finding supporting contribution #2. The MODEL × TYPE interaction (C4) is now MORE central than the layer main effect. "Disambiguation channel" is an explanatory framework (not hypothesis — per SF-5). DeBERTa classifier, if included, is a preliminary PoC appendix, not a contribution.

## Required Reference Expansion [Dream A2 + MF-4 RE literature gap]

Current plan has thin references. Must add (≥25 total in final paper):
- **Nocuous ambiguity detection (CRITICAL — MF-4)**: Chantree, Nuseibeh, de Roeck & Willis (2006, ASE) — first computational nocuous ambiguity detection; Chantree et al. (2008, RLAC) — expanded. Direct lineage to our DeBERTa classifier.
- **Cross-domain RE ambiguity**: Ferrari, Spagnolo & Gnesi (2017-2019, ASE) — NLP-based cross-domain ambiguity detection. NLP4RE community work.
- **Good-enough processing**: Ferreira, Bailey & Ferraro (2002); Ferreira & Patson (2007)
- **LLM garden-path (SF-6)**: Li et al. (2024) — incremental comprehension of garden-path sentences by LLMs. Directly relevant to how LLMs process ambiguity.
- **Anaphoric ambiguity (SF-6)**: Poesio & Artstein (2005, 2008) — annotation of anaphoric ambiguity. Poesio (2004) "Ambiguity" encyclopedia entry.
- **Surprisal/expectation-based**: Levy (2008); Hale (2001)
- **Instruction-following robustness**: Zhou et al. (IFEval, 2023); Qin et al. (ToolBench, 2024)
- **Prompt sensitivity**: Sclar et al. (2024); Lu et al. (2022)
- **Broader agent safety**: R-Judge, ToolEmu, InjecAgent
- **Formal semantics of vagueness**: Lassiter & Goodman (2017)
- **Garden-path**: Frazier & Rayner (1982)
- **Ambiguity detection**: Willis et al. (2008); Ezzini et al. (TAPHSIR, 2022)
- **Year verification needed**: Massey et al. — §1 引用 2013 vs 后文 2014, 需确认正确年份

## Code/Data Release Plan [Dream A6 — three-tier consistent]

Must commit to releasing:
1. All 300 clause pairs (ambiguous + unambiguous variants) with type labels
2. Evaluation scripts (τ²-bench integration, cross-judge pipeline)
3. Statistical analysis code (all tests, bootstrap CI computation)
4. Agent trace samples (anonymized) for reproducibility of C5

## Figure Plan [Dream A12]

Minimum figures for paper (zero-figure paper flagged in dream):
1. **Figure 1**: System architecture / experimental pipeline overview (§4 Method)
2. **Figure 2**: Forest plot — per-type binary effect sizes with 95% CI (§5 C1)
3. **Figure 3**: Model × Type heatmap — violation rates across 4 models × 6 types (§5 C4)
4. **Figure 4**: Visibility mechanism — CP vs scopal violation rates + trace evidence (§5 C3)
5. **Figure 5**: Failure mode × type stacked bar/Sankey — per-type failure mode distribution (§6 C5)
6. **Figure 6**: Cross-model failure mode consistency — side-by-side gpt-5.4 vs gpt-4.1 per-type distributions showing 5/6 convergence (§6 C5, supports C4)
7. **Figure 7**: Annotated trace pair — CP (conflict detection) vs scopal (surface adoption) (§6 C5)

## Berry & Kamsties Operationalization Note [Dream best Q5]

Berry & Kamsties define nocuity as inter-reader divergence. Our design measures agent-vs-intent deviation. Full study should additionally test whether different models adopt different readings of the same ambiguous clause (true inter-model nocuity). If 4 models produce 4 different interpretations of the same clause → true nocuity. If all 4 adopt the same wrong interpretation → systematic bias, still nocuous but for different reason. Report inter-model agreement on ambiguous clauses as supplementary analysis.

## Contingency Framing [RESOLVED — Scenario C occurred]

> plan_002 结果: Scenario C 发生（omnibus p=0.0001, 所有类型 nocuous 但 severity 有显著差异）。
> Framing 已 pivot 到 "Differential Nocuity" + "Layer Hierarchy" (D020)。本节仅保留历史记录。

## Claude Baseline — RESOLVED [2026-05-20]

✅ Claude works via OpenRouter proxy (47.94.22.126/v1) with provider prefix `anthropic/claude-sonnet-4-6`. 600 episodes complete (plan_002c). Claude shows lowest overall vulnerability (30.3%) and remarkable auth_scope robustness (12% vs GPT-5.4 64%).


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
- id: plan_001b
  name: new_type_mini_pilot
  claim: C1 (validation)
  description: 'Mini-pilot for coreferential + authorization_scope (never tested):
    5 clauses/type × 2 conditions × 1 model (gpt-5.4) = 20 episodes. Verify: (a) ambiguous
    triggers violations (b) unambiguous control < 15%. If systematic issues found,
    fix clause design before full study. API cost negligible (~$2). Per Reviewer warning
    on untested types.

    '
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_001
  status: planned
- id: plan_002
  name: full_study_api
  claim: C1, C2, C3, C4, C5
  description: 'Run 300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6)
    = 1,800 episodes on τ²-bench. Cross-judge evaluation. Output: episodes.jsonl +
    judgments.jsonl. No GPU needed. Claude via OpenRouter proxy (base_url=http://47.94.22.126/v1).
    [2026-05-20] Claude added per distill gap (4/8 papers use Claude baseline).

    '
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_001
  - plan_001b
  - plan_010
  status: planned
- id: plan_003
  name: full_study_opensource
  claim: C1, C2, C3, C4, C5
  description: 'Run 300 clauses × 2 conditions × 2 open-source models via OpenRouter
    API: qwen/qwen3-235b-a22b (235B MoE, Alibaba) + deepseek/deepseek-chat-v3-0324
    (DeepSeek) = 1,200 episodes on τ²-bench. Cross-judge uses API models. Can run
    in parallel with plan_002. No GPU needed. [2026-05-20] Pivoted from local GPU
    → API: OpenRouter proxy confirmed to support Qwen3 and DeepSeek models. Eliminates
    48h GPU requirement. Provider prefix required (e.g. qwen/qwen3-235b-a22b, not
    qwen3-235b-a22b).

    '
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_001
  status: planned
- id: plan_004
  name: full_study_analysis
  claim: C1, C2, C3, C4
  description: 'Statistical analysis of full study data (3,000 episodes): (a) Binary
    effect per type with bootstrap CI (C1) (b) Omnibus χ² + pairwise across 6 types
    (C2) (c) Visibility comparison: CP vs scopal rates (C3) (d) Model × type interaction:
    5×6 contingency + logistic regression (C4) Report effect sizes + CI for all comparisons
    per Reviewer suggestion. [Dream A3] Power analysis: report MDE for C2 (given N=250/type
    pooled) and C3 (given N=250 per type). If V < 0.20 but MDE > observed V, discuss
    underpowered possibility. [Dream A4] TOST equivalence test with both ±15pp and
    ±10pp margins. Justify margin choice explicitly. [Dream A10] Report per-type information
    delta (token count difference between ambiguous and unambiguous variants) as control
    variable. [Dream B&K] Inter-model agreement on ambiguous clauses: do 5 models
    adopt same or different interpretations? (supplementary analysis)

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
    run 3 independent replicates × 2 conditions × 2 API models (gpt-5.4, gpt-4.1)
    = 360 episodes. Local models added when plan_003 GPU available. Compute ICC for
    per-clause violation rates. Addresses Reviewer warning about ±8pp sampling noise
    (scopal 51.7% → 43.3% across MVP/diag). Bootstrap CI width should be < 10pp for
    key comparisons. [2026-05-20] API portion: 330/360 episodes complete (28/30 clauses),
    judgments pending.

    '
  priority: P1
  gpu_budget_hours: 15
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
- id: plan_009
  name: judge_calibration
  claim: C1 (methodological)
  description: 'LLM-as-judge calibration per distilled research norm (5/8 papers):
    (a) Sample 100 episodes stratified by type×model×condition (b) Human expert labels
    (2 annotators, target κ ≥ 0.75) (c) Compute judge precision/recall/F1 against
    human ground truth (d) Per-severity-tier agreement rates (e) Report in Method
    section as standard practice per AgentAuditor/DRIP-R [Dream A7] Upgraded P1→P0:
    Dream best-tier reviewers identified this as "single most critical missing validation."
    Without it, entire measurement chain from episode to violation label is unvalidated.
    κ=0.91 measures LLM-LLM agreement, not accuracy.

    '
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_002
  status: planned
- id: plan_010
  name: perturbation_control
  claim: C1 (causal validity)
  description: '[Dream A9] Non-ambiguity perturbation control arm to distinguish ambiguity-specific
    harm from general prompt brittleness. Generate 30 clause pairs with non-ambiguity
    perturbations: (a) 15 synonym substitution pairs (replace key terms with synonyms)
    (b) 15 clause reordering pairs (reorder conditions without changing meaning) Run
    30 × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6) = 180 episodes.
    Key metric: Δ_net = Δ_ambiguity - Δ_perturb (net ambiguity-specific effect). [Reviewer升级]
    必须在 plan_002/003 full study 之前完成—— 如果 perturbation Δpp ≈ ambiguity Δpp，2,400 episodes
    全部无效。 低成本验证（30 pairs + 120 episodes API）优先于高成本投入。 [判定标准 — 5 档]: PASS: Δ_perturb
    < 5pp (CI含0), ratio < 0.15 → C1 因果 claim 最强形式 PASS+caveat: 5-10pp, ratio 0.15-0.30
    → 报告 perturbation baseline, C1 写 net effect CONDITIONAL: 10-15pp, ratio 0.30-0.45
    → 需 Δ_net > 20pp 且显著才可发表 WARNING: 15-20pp, ratio 0.45-0.60 → C1 改为 "additional
    violations beyond sensitivity" FAIL: > 20pp, ratio > 0.60 → 无法声称 ambiguity-specific,
    需根本重新设计 [Power 注意]: N=120 对 10pp 差异 power ≈ 30%. 用 CI 宽度判定, 非 p-value. 若 CI 过宽(>15pp
    width), 追加 60 episodes 压窄至 <10pp width. 输出标准化 verdict 文件: perturbation_Δpp, ambiguity_Δpp,
    net_Δpp, CI, ratio, verdict.

    '
  priority: P0
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
- exp_id: plan_002
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: plan_005
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: plan_006
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: plan_009
  name: ''
  status: PREPARING
  conclusion: ''
  metrics: {}
- exp_id: plan_002c
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: plan_003a
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: plan_003b
  name: ''
  status: DONE
  conclusion: success
  metrics: {}
- exp_id: plan_004
  name: ''
  status: DONE
  conclusion: success
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
  "promptId": "ffd2fc3c-c498-4e18-9484-3710f8aaf483",
  "type": "user",
  "uuid": "a796a70a-0cb6-4517-b417-4cd708ff920f",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "bbbefa27-3d72-4fb3-9d7d-bdb8c8bb7c9d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T04:23:54.630Z_

```json
{
  "parentUuid": "a796a70a-0cb6-4517-b417-4cd708ff920f",
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
  "uuid": "1d85c2d3-411f-4096-b3f6-289af7bd5c75",
  "timestamp": "2026-05-21T04:23:54.630Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "bbbefa27-3d72-4fb3-9d7d-bdb8c8bb7c9d",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T04:23:54.630Z_

```json
{
  "parentUuid": "1d85c2d3-411f-4096-b3f6-289af7bd5c75",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d0e69164-86c5-4282-8021-142c465efd1b",
  "timestamp": "2026-05-21T04:23:54.630Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "bbbefa27-3d72-4fb3-9d7d-bdb8c8bb7c9d",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：C1/C2/C4/C5 成立但部分效应量缩水，C3 layer effect 保持 fragile（within-judge 不显著），judge calibration 中等，需调整部分 claim 表述强度 核心假设：['C1 binary effect 成立但效应量略低于 5-model 聚合值，部…",
  "leafUuid": "d0e69164-86c5-4282-8021-142c465efd1b",
  "sessionId": "bbbefa27-3d72-4fb3-9d7d-bdb8c8bb7c9d"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Differential nocuity across LLM models and ambiguity types",
  "sessionId": "bbbefa27-3d72-4fb3-9d7d-bdb8c8bb7c9d"
}
```

---

### Assistant

_source line 8 · 2026-05-21T04:31:59.391Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experimental data for each planned experiment in the experiment_plan, assuming the "median" tier outcome. I need to provide specific numbers, rationale, tables, figures, and analysis for each experiment.

Let me carefully go through each planned experiment and generate realistic median-tier data based on the defined key metric ranges and narrative guidance.

The median tier is defined with these key ranges:
- C1_binary_effect_pp: [25, 35]
- C1_mcnemar_OR: [8, 15]
- C2_omnibus_chi2_p: [1e-4, 0.01]


- C2_cramers_V: [0.09, 0.15]
- C2_incomp_minus_coref_pp: [12, 20]
- C3_layer_gap_pp: [3, 8]
- C3_within_judge_p: [0.1, 0.3]
- C4_auth_scope_range_pp: [30, 45]
- C4_incomp_range_pp: [15, 25]
- C4_fleiss_kappa: [0.25, 0.4]
- C5_awareness_rate_pct: [5, 15]
- C5_surface_adoption_pct: [78, 90]
- C5_perturbation_delta_pp: [5, 10]
- judge_human_kappa: [0.65, 0.79]
- judge_F1: [0.75, 0.84]

Looking at the guidance, I need to soften some of my claims—the C3 layer effect should be framed as suggestive rather than significant, and I should note that perturbation effects need caveats about net impact. The C5 failure mode shows cross-model consistency issues for certain types, and I should be more cautious about the auth_scope safety training narrative. Some of these effect sizes have shrunk 5-8 percentage points from the aggregated five-model baseline. For the experimental plans, I'm laying out the clause generation work, a mini pilot combining coreferential and auth_scope testing, and the full API study with 300 clauses across two conditions.

Now I'm mapping out the remaining studies: the open-source model evaluation, comprehensive statistical analysis across all episodes, qualitative error analysis, test-retest reliability checks, validation of synthetic ambiguity realism, LLM judge calibration, perturbation controls for non-ambiguous cases, and a DeBERTa classifier proof of concept. For the median tier results, the binary effect persists but slightly attenuated—around 29 percentage points instead of 34 for some models—and I'm working through the detailed data generation for each plan. hierarchy significant but V<0.15
- C3 layer effect fragile (within-judge not significant)
- C4 interaction exists but auth_scope range shrinks to 30-40pp
- Perturbation control PASS+caveat (5-10pp)
- Judge calibration κ=0.65-0.79
- C5 failure modes: 2-3 types show inconsistent dominant modes across new models

Let me construct comprehensive YAML output.

I need to be very detailed and precise. Let me think through each experiment carefully.

### plan_001: full_study_clause_generation
This is a generation task. Median means: generation succeeds but some quality issues — maybe 5-8 clauses need revision, some types harder to generate balanced pairs.

### plan_001b: new_type_mini_pilot
Median: coreferential works but violation rate lower than other types. Auth_scope works but shows model sensitivity, with maybe 1-2 clauses having control condition issues.

### plan_002: full_study_api
Running 1,800 episodes across three API models with 300 clauses each. The overall binary effect lands around 29pp, though Claude shows a smaller 22pp effect while GPT-4.1 and GPT-5.4 reach 30-33pp. Ambiguous violations cluster between 27-39% depending on the model, while unambiguous rates stay low at 5-8%.

### plan_003: full_study_opensource
Qwen3 produces roughly a 28pp effect across 1,200 episodes with two open-source models and 300 clauses. Writing YAML structure... Adjusting the violation rates to meet the constraints—I need the incompleteness range to fall between 15-25 percentage points, and checking that the authorization scope and inter-rater agreement metrics align with the target ranges. Now I'm breaking down the ambiguous rates by error type across all five models—authentication scope issues are running around 35.6%, incomplete specifications at 47.6%, and coreference problems are the lowest at 26.8%, with the others clustering in the low-to-mid 30s. Now I'm calculating the pooled averages for each error type and checking that the ranges fall within the target bounds—incompleteness versus coreferential gives me a 17.2 percentage point gap, which fits nicely in the [12,20] range, and the spread across models looks good too. Let me verify the layer effect by grouping the specification-level errors together. So the total ambiguous episodes comes to around 1,500, and with that baseline I can calculate the pooled violation rates—about 35.5% for ambiguous cases versus 6.5% for unambiguous ones, giving a binary effect of 29 percentage points. The McNemar odds ratio of roughly 11 confirms this pattern holds. Looking at how individual models perform on unambiguous cases, Claude shows the lowest violation rate at 4%, while the others cluster between 6-9%, and I'm starting to see the per-model binary effects diverge from there. Looking at the original per-model values and the constraint that some models shrink by 5-8pp from their individual baselines, I need to recalibrate Claude's effect size upward—keeping it around 23-24pp seems too conservative given the pooled average sits at 29pp and Claude's original value was 25.7pp. Now I'm recalibrating the violation rate matrix to align with these effect sizes. I'll set the unambiguous baseline rates for each model, then add the estimated effect sizes to get the total ambiguous violation rates, which should give me consistent per-model totals that match my earlier calculations.

Checking the per-type breakdown for each model against the target ambiguous rates—Claude's six violation categories average to 26%, GPT-4.1 comes to about 36%, but GPT-5.4 is only averaging 35.3% when it should be closer to 39%, so I need to adjust those category-level rates upward.

After tweaking the numbers, I get GPT-5.4 to 38.3%, which rounds to the target 39%. For Qwen3, the initial breakdown gives 37.8%, which overshoots the target of 34%, so I'm lowering the individual category percentages to bring the average down to 33.3%.

Now I'm working through DeepSeek with an ambiguity rate of 43%, and the category breakdown sums to 43.3%, which matches. Let me compile the full comparison matrix across all five models and verify each one's average against the target ambiguity rates. Now I'm finishing the scopal calculation and getting an overall pooled average of 35.3%. The incomp-to-coref gap looks good at 18.4 percentage points, and the auth_scope range is solid, but the incomp range is coming in a bit low at 12 percentage points when I need it between 15-25. Let me try adjusting the incomp scores by pushing Claude down to 34% and Qwen3 up to 54% to widen that spread.

With those tweaks, the incomp range hits 20 percentage points, which fits the target. But now Claude's overall average dips slightly below 26%, so I'm bumping the conditional_precedence score up to 32% to get closer. That brings Claude to about 25.7%, which is close enough given the inherent noise in this kind of modeling. I'm going to accept these small discrepancies and lock in the final table.

Now I'm calculating the per-model and per-type averages to validate the layer effect. The spec layer comes in around 38.4% while the linguistic layer sits at 32.7%, giving me that 5.7 percentage point gap I'm looking for. For the overall pooled ambiguous rate, I'm averaging across all models to get roughly 35.5%, and the binary effect—the difference between ambiguous and unambiguous violations—works out to about 29 percentage points, which feels right.

Let me finalize the per-model binary effects by computing the exact differences between ambiguous and unambiguous rates for each model, then I'll structure everything into the YAML output the user is expecting. Now I'm working through the expected outcomes for each experiment plan. For the clause generation phase, I'm looking at around 140 new clauses with minimal revisions needed, and the quality checks show most pass on the first attempt. The mini pilot reveals some issues with coreferential and auth_scope triggers that need attention, particularly one control clause with baseline leakage. For the full study, I'm projecting roughly 1,800 completed episodes across the three models with their respective conditions, accounting for a small number of API retries.

I'm calculating the total episode count across all plans — 300 clauses times 2 conditions times 3 models gives 1,800 for the main study, plus 1,200 for the open-source variant, totaling around 3,000 episodes. Now I need to structure the comprehensive output with detailed breakdowns and figure out what tables and visualizations each experiment should produce.

Looking at the C3 within-judge analysis, the pooled effect shows significance at p<0.05, but when I break it down by judge group, neither subgroup reaches significance individually — gpt-4.1's judged group shows about a 7 percentage point gap that's not significant, and gpt-5.4's judged group shows around 4 percentage points, also not significant. The significance in the pooled analysis is driven by between-judge variance rather than consistent within-judge effects.

For the perturbation control experiment, the perturbation effect is around 7.2 percentage points, which falls within the acceptable range.  The ambiguity effect is much larger at 31.5 percentage points, giving a ratio of 0.23 that's within the target bounds. The confidence interval for the perturbation effect doesn't include zero, which flags a caveat, but overall this passes with that caveat noted.

On judge calibration, the agreement metric sits at 0.72 and F1 score at 0.80, both within acceptable ranges. There's some unevenness across severity tiers though — the minor tier has lower performance at 0.68 while moderate severity reaches 0.82.

Looking at the remaining plans, reliability shows an ICC of 0.88 with strong performance on linguistic-layer items but more variation on specification-layer ones. The error analysis reveals good awareness and adoption rates, though only about two-thirds of error types show consistent patterns across models. Realism validation appears to be cut off mid-evaluation.

For the classifier proof-of-concept, I'm getting an F1 of 0.78 overall, with incompleteness being the easiest type to detect and coreferential errors the most challenging. Now I need to compile all these results into a comprehensive YAML structure with clear explanations for why each metric lands at the median tier.

Looking at the episode counts more carefully: plan_002 and plan_003 together generate 3,000 episodes total, which breaks down to 50 episodes per cell when looking at type, model, and condition combinations. For the reliability test, I'm working with 360 episodes across 30 clauses with replicates and conditions. The perturbation control plan is a bit ambiguous in the documentation—it mentions 180 episodes but also references a lower-cost validation approach with 30 pairs, so I need to clarify which interpretation is correct. I'm noticing a discrepancy between what the framing document shows as completed (plan_010 with 120 episodes) and what the registry indicates, so I need to clarify whether plan_010 is actually finished or if I'm generating imagined data for it as part of the median tier experiments. The plan specifies 180 episodes for 3 models, but the framing doc references 120 episodes—I should stick with the 180 episodes since the user wants me to generate median tier imagined data based on what's planned, not what's already been completed.

Now I'm structuring the YAML output to organize all the planned experiments with their imagined median-tier results, using a clean format with tables embedded as structured data. Now I'm working through the chi-square calculation for the 6×2 contingency table—with Cramér's V at 0.12 and N around 1499, that gives me χ² ≈ 21.6 with 5 degrees of freedom, yielding p ≈ 0.0006, which fits the target range. I'll use χ² = 19.8 instead.

Looking at the TOST equivalence results for the ±15 percentage point margin, the median split shows about 6 out of 15 comparisons are equivalent while 9 remain non-equivalent. When I tighten the bounds to ±10 percentage points, only 3 are equivalent and 12 fall outside.

The violation rates show a clear three-tier pattern: incompleteness stands alone at 46.4%, a middle cluster of auth_scope, lexical, scopal, and CP ranges from 32.8% to 36.4%, and coreferential sits lowest at 27.2%. The gap between the high tier and the middle tier is relatively modest at about 10 percentage points, whereas the middle tier itself is fairly compressed.

For C3, the pooled chi-square test yields χ² = 4.82 with p = 0.028 and V = 0.057. When I break this down by judge, GPT-4.1 shows a difference of +6.2 percentage points (p = 0.14) and GPT-5.4 shows +4.1 percentage points (p = 0.23).

In C4, the overall model effect is significant with χ² = 25.8, p = 5.2×10^-5, and V = 0.093. Looking at individual models, GPT-5.4 shows the strongest differentiation (χ² = 18.2, p = 0.003, V = 0.25), Qwen3 is also significant (χ² = 14.2, p = 0.014, V = 0.22), Claude shows borderline significance (χ² = 9.8, p = 0.08, V = 0.18) — notably weaker than in the best tier — and GPT-4.1 doesn't reach significance (χ² = 8.2, p = 0.15).

The remaining models show no significant effects, and inter-rater reliability is acceptable at Fleiss κ = 0.33. I'm verifying the auth_scope range for the median condition: GPT-5.4 at 56% and Claude at 14% gives a 42 percentage point spread, which fits within the expected [30, 45] range. For the logistic regression, the condition_amb coefficient is around 1.95 (slightly lower than the 2.278 from the best tier), with strong significance (z ≈ 16.5, p < 0.001), and both model and type effects remain significant, though token_delta shows a modest effect (coef ≈ 0.018, z ≈ 2).

Now I'm ready to compile the YAML output with all these findings. I should also adjust the narrative guidance since the paper title might need to shift from "Differential Vulnerability Profiles" to something more conservative at the median tier. Looking at the failure modes for plan_005 across the five models at median tier, I'm seeing that four of the six types show consistent dominant modes, while coreferential and lexical types diverge—particularly for auth_scope leading to unauthorized_escalation, which remains consistent across GPT-5.4, GPT-4.1, and DeepSeek in the 70% range. I need to figure out the right sample size across all five models—if I'm sampling roughly 50 traces per violation type originally, that's about 10 per type per model, which means around 360 total traces across 6 types to properly cover all five models. Now I'm ready to write out the YAML configuration, making sure to include thoughtful analysis text for each experiment that captures what the median results actually tell us. But first I should verify the experiment plan statuses—the plan shows everything as "planned" but the registry has some marked as "DONE," so I need to reconcile that discrepancy.

Writing YAML structure... Now I'm filling in the remaining sample sizes — plan_009 has 100 episodes with 2 human annotators for labeling, and plan_010 covers 180 episodes across 3 models. For the judge's performance, I'm looking at the inter-annotator agreement (κ = 0.78) and how well it aligns with human consensus (κ = 0.72, F1 = 0.80), then breaking down the metrics by severity tier where minor violations show precision around 0.72 and recall at 0.64.

Writing YAML now...

Let me verify the numbers are consistent across all the metrics I'm including — pooling the ambiguous rates from the five models gives me about 35.5%, the unambiguous rates average around 6.9%, and that 28.6 percentage point difference aligns with the binary effect I calculated earlier. The per-type breakdowns also check out, with incompleteness showing the highest ambiguity rate at 46.4% and coreference the lowest at 27.2%.

Now I'm looking at how ambiguity varies by layer — the specification-level errors cluster around 38.4% ambiguous while linguistic errors are lower at 32.7%, creating roughly a 5.7 percentage point gap. When I break this down by individual model, the pattern holds but with some variation, particularly for GPT-5.4 which shows a larger 12.7 percentage point gap between specification and linguistic layers.

What's striking is that Claude, Qwen3, and DeepSeek don't show this same layer effect — their gaps are minimal or nonexistent — suggesting the layer distinction is really being driven by how the GPT models handle specification-level ambiguity, especially around auth_scope issues.

Now I'm running the within-judge analysis to see if the pattern holds when we control for who's doing the judging. When gpt-5.4 evaluates the other models, I'm getting a gap of 4.2 percentage points that's not statistically significant, and when gpt-4.1 judges the remaining group, the gap widens to 7 percentage points but only reaches marginal significance.

Let me move forward with writing out the YAML configuration. I'm calculating the expected violation rates for each model across both ambiguous and unambiguous episodes—gpt-5.4 and gpt-4.1 show higher violation rates in the 36-38% range for ambiguous cases, Claude comes in lower at around 26%, while Qwen3 and DeepSeek cluster around 34-43% for the same category.

Writing YAML structure... I'm working through the median-tier outcomes for each planned experiment, making sure they align with what's already documented in the registry. For perturbation control specifically, I need to calibrate the median delta around 7 percentage points—higher than the best-case 3.33pp but still passing with caveats. The experiment structure involves 60 total episodes: 30 perturbed prompt pairs run against their unperturbed originals across the models.

Now I'm checking the violation rate calculations. The perturbed condition shows roughly 14% violations (7pp above the baseline ~7%), while ambiguous prompts hit around 36% (29pp above baseline). The ratio of perturbation effect to ambiguity effect comes to 0.24, which falls squarely in the PASS+caveat range of 0.15–0.30, so that checks out.

For the confidence interval on the perturbation delta with 90 episodes across conditions, I'm looking at roughly ±5–6pp, giving a range of [1.5, 12.5pp]. It barely excludes zero, which justifies the caveat. I think I've analyzed this enough—time to write up the YAML output.

Writing YAML output... The ratio comes out to about 0.24, which confirms the perturbation effect is real but much smaller than the ambiguity effect itself. Now I need to write out the YAML configuration, being careful with formatting and special characters. I'll structure it so that plan_002 and plan_003 each report raw episode counts and per-model violation rates, while plan_004 handles the combined statistical analysis.

Writing YAML config... Writing YAML config...

Now I'm double-checking the Qwen3 calculations—the effect size at the median tier should be somewhere between the best and worst performance, so I need to verify those numbers are consistent before finalizing. Some models shrink less than 5pp while others are around 7pp, which aligns with the definition that only some models experience that 5-8pp range. I'm tempted to fine-tune GPT-4.1's numbers to hit exactly 5.6pp shrinkage, but these are meant to be illustrative anyway—I'll just write out the YAML with what I have and move forward.

Now I'm structuring the output with tier and narrative guidance at the top, then each experiment ordered by plan_id, with detailed metrics, rationale, tables, and figures for each. For the YAML tables I'll use a list format with markdown content. I'm also thinking through what metrics make sense for experiments like clause generation—things like total clauses generated, how many pass initial review, and how many need revision.

Writing the full YAML output now... Now I'm settling on the YAML structure—using a dictionary format for expected_results with descriptive metric keys and specific values, and organizing tables as a list of objects with title and content fields, plus a figures_description as a list of strings detailing what each visualization would display. I'm also working through the logistic regression coefficients for plan_004, estimating the condition ambiguity effect and model comparisons across different systems. Looking at the model comparison results and equivalence testing—the likelihood ratio test shows significant differences across models, and the TOST analysis indicates most model pairs aren't equivalent even at the more lenient threshold. The power analysis confirms the study is adequately powered to detect the observed effect sizes. Now I'm examining the inter-rater reliability metrics across the different clause types, where the linguistic-layer categories show notably higher agreement than the specification-layer ones, suggesting models are more consistent in identifying certain violation types. Writing YAML config... Now I'm looking at how different models handle authorization scope violations—GPT-5.4 and GPT-4.1 both show unauthorized escalation as the dominant error pattern at 75-78%, while Qwen3 and DeepSeek cluster around 55-72%. Claude stands out with only 45% unauthorized escalation and 25% conservative refusal, though the small sample size of roughly 7 traces from the 14% violation rate makes that comparison less reliable. I'm about to write out the YAML configuration now.

For the paper's overall narrative at the median tier, the core findings hold—ambiguity does drive violations and there's a clear type hierarchy—but the C3 layer effect is only suggestive rather than statistically significant within judges. The perturbation control works but the confidence interval barely excludes zero at 7 percentage points. Judge calibration is adequate though the severity tiers show instability, and some C5 failure modes vary inconsistently across models. The auth_scope range narrows from 52pp to 42pp, which softens the safety training explanation. The paper is still EMNLP-worthy but needs conservative framing and additional robustness checks in the appendix, with C3 findings moved to discussion and C1 reporting the net effect.

For the realism validation, I'm checking five linguistic properties against the synthetic data: sentence length, parse depth, Flesch-Kincaid, type-token ratio, and token count. Four of them show no significant difference from the original corpus, but sentence length is slightly elevated in the synthetic ambiguous clauses—22.3 words versus 19.8—which I'll flag as a minor confound in the limitations.

Now for the classifier proof of concept, I fine-tuned RoBERTa on 240 clause pairs and got an F1 of 0.78 overall with 0.81 precision and 0.75 recall. The per-type breakdown shows incompleteness is easiest to detect at 0.86 F1, while coreferential ambiguity is hardest at 0.68 since those cases have the smallest surface-level differences. The AUC is 0.85, which demonstrates the approach is viable even if it's not state-of-the-art.

Writing YAML output... The range of 16 percentage points falls within the acceptable bounds, and the inter-model agreement metric of 0.33 is also in the right ballpark. For the pooled effect confidence interval, I'm getting a range of 25.8 to 31.5 percentage points at 95% confidence, which aligns with my target parameters.

Looking back at the mini pilot data, I'm seeing some concerning patterns in the auth_scope violations—particularly that 20% unamb violation rate suggests I need to refine one of the clauses. The pilot confirms both violation types are working as intended, though the full study shows auth_scope performing at 56% for GPT-5.4, which is higher than what I observed in the pilot subset.

Now I'm structuring the final YAML output with six experiment plans: the clause generation quality metrics, the mini pilot validation, the API and open-source study results with per-model breakdowns, the statistical analysis, error analysis, and reliability testing.

I'm also adding four more experiment plans covering realism validation through KS tests, judge calibration metrics, perturbation control analysis, and a classifier proof-of-concept.

For the statistical analysis tables, I'll include the per-model binary effect summary, a violation rate matrix broken down by model and type, pooled rates with the three-tier structure, logistic regression coefficients, and TOST equivalence results. The error analysis section will have failure mode distributions, cross-model consistency, and adoption rates.

Writing the YAML structure now...

I'm working through the specific numbers for plan_004, particularly the type rankings where incompleteness violations dominate at 46.4%, followed by lexical and authorship issues around 36%, with coreference at the lower end. The pairwise comparisons show incompleteness significantly outpaces coreference by nearly 20 percentage points, and several other contrasts remain significant even after Bonferroni correction. Finishing the Holm calculation—that third comparison doesn't meet the threshold. With FDR, I get one more significant pair, bringing it to three. I'll go with Holm for the main results since the omnibus test was already significant, making these pairwise comparisons legitimate follow-ups.

Now I need to actually write this up. The field standard would be Tukey's HSD or Dunn's test, but pairwise z-tests with Holm correction works well for proportions. The data shows a clear three-tier structure: the incompleteness category stands apart from the bottom three types, while those middle types cluster together without significant differences between them.

For the annotation validation, I'm looking at the inter-rater agreement and model performance metrics across the binary and severity classification tasks.

The real issue emerges when I break down performance by tier — the minor violation category is unstable, with judges consistently either pushing cases up to moderate or down to no-violation. This instability means the binary classification is much more reliable than trying to distinguish severity levels. So for the paper, I should emphasize the binary effect as well-supported, flag the severity analyses with appropriate caveats, and probably collapse to binary for the main findings.

Now I'm working through the confusion matrix... Now I'm working through the binary confusion matrix by summing up the columns—Judge says no-violation is 45 total, Judge says violation is 55 total. For the human labels, those without violations had a false positive rate of 8.9% (4 out of 45), while those with violations had a false negative rate of 7.3% (4 out of 55).

Looking at the initial accuracy metrics, I'm getting 92% which seems too optimistic, so I'm adjusting the median tier distribution to make the results more realistic. With the revised numbers, accuracy drops to 87%, precision and recall both land around 88%, and the F1 score comes to 0.881. Now I'm calculating Cohen's kappa to measure agreement between the human and judge labels.

After working through the kappa calculation with the observed and expected agreement proportions, I'm getting κ = 0.74, which combined with the F1 of 0.88 falls within acceptable ranges. For the 3-tier severity classification, I'm targeting a weighted F1 of 0.80 with some variation across individual tiers. Rather than listing out every cell of the confusion matrices, I'll focus on reporting just the summary metrics since that's what matters most. Now I'm ready to write out the full YAML output with these metrics.

For plan_009, the inter-annotator agreement at median reaches κ = 0.78, which meets the target of ≥0.75, though the judge-human agreement is somewhat lower. I should clarify that the plan involves 100 episodes for the binary and severity calibration work, separate from the 20-30 failure mode traces used for C5 validation. I'll report both components in the results. Now I'm computing the bootstrap confidence interval for the pooled effect size of +28.7 percentage points.

Writing YAML output... Now I'm reconsidering the tier structure at the median performance level—the separation between categories is less pronounced there, with incompleteness at 46.4% as the high tier, coreference at 27.2% as the low tier, and everything else clustered in the middle around 32.8-36.4%, compared to the wider 22-point spread in the best tier configuration.

I need to finalize this and write the output with all the numbers I've calculated. For the Fleiss kappa with 5 models, a κ of 0.33 indicates moderate agreement beyond chance, which aligns with the large 42-point range in auth_scope—the models converge on some categories like CP and incompleteness but diverge significantly on others like auth_scope and coreference.

One more thing to verify: at the median tier for plan_001 clause generation, the generation process itself still works, but certain types might be harder to match, with roughly 8-10 clauses needing revision.

I'm noticing some data quality issues that add friction to the process—auth_scope disambiguation tokens are running higher than expected, and some CP clauses have inconsistent formatting with mixed labeled and unlabeled patterns. These don't materially shift the statistical findings but do create workflow friction.

Now I'm structuring the output with the median tier experiments, using YAML format with multiline narrative guidance and organized experiment blocks that include descriptions, expected results, and analysis sections. I'll work through the plan_001 experiments with all the key metrics.

Writing the output now... Looking at the reliability metrics across these validation plans — ICC and binary ICC both show strong agreement, sentence length distribution matches the real data within statistical noise, and the classifier performs solidly with F1 and AUC scores. The perturbation test holds up under stress with only a 7.2 percentage point shift. Now I need to work through why the median tier specifically produces these outcomes — generation quality hinges on researcher effort rather than noise, which explains why certain categories like authentication scope prove harder to construct consistently.

The small sample size of five per condition creates substantial variance, and even carefully written authorization specifications can have ambiguous edge cases that trip up the control condition. For the API models, I'm seeing the expected performance hierarchy across Claude, GPT-4.1, and GPT-5.4, but the effects are noticeably smaller — around 5-7 percentage points below the best-tier aggregated results. This compression likely stems from the new clause types diluting performance if they behave differently than the pilot types, natural variation between API runs, or the expanded set of fifty clauses per type introducing more heterogeneity.

The open-source models reveal higher violation rates overall, suggesting less refined safety training, with DeepSeek showing particularly high rates due to uniform vulnerability across types and Qwen3displaying an unusual pattern of low auth_scope violations but elevated incompleteness and lexical issues. The main effect shrinks in the full analysis because the additional types and models include weaker exemplars that pull down the average, the type hierarchy compresses with a tighter mid-tier, and within-judge comparisons lose significance as the effect structure becomes more complex. within-judge subgroup has only ~40-60% of total N, reducing power for a small effect; (b) the layer gap is genuinely model-dependent (strong for GPT, negligible for Claude/Qwen3/DeepSeek), so subgroups with different model compositions show different gaps; (c) between-judge variance inflates the pooled test.
- C4 auth_scope range shrinks from 52pp to 42pp because the 50-clause set includes some auth_scope clauses where Claude is slightly more vulnerable and GPT-5.4 slightly less, compared to the pilot set. The 42pp range is still dramatic but the safety training explanation weakens (could also be prompt format sensitivity rather than specific training).

plan_005 rationale: 4/6 types consistent because the dominant failure modes for auth_scope, incompleteness, scopal, and CP are structurally determined by the ambiguity type itself. Lexical diverges across models because word-level ambiguity triggers different processing strategies—GPT models default to assumption-based action while open-source models lean toward scope misapplication, likely reflecting their training data differences. Coreferential diverges because it's inherently heterogeneous with no single resolution strategy dominating.

plan_006 rationale: ICC is slightly lower than best tier because the 30-clause sample may include some high-variance clauses, especially spec-layer types where agents guess differently each run. The spec-layer ICC being lower reflects the genuine absence of external disambiguation channels.

plan_007 rationale: Most properties match because the injection process is controlled, but sentence length shows a small significant difference since disambiguating additions inevitably add words, making the ambiguous versions slightly shorter than naturally occurring policy clauses of similar complexity.

plan_009 rationale: κ=0.72 reflects genuine disagreement on borderline cases—minor violations are inherently harder to distinguish from acceptable behavior, the boundary between "slightly questionable" and "no violation" is subjective, and severity assessment depends on domain-specific norms that the LLM judge may interpret differently from human experts. Major violations are clear and no-violations are mostly unambiguous; it's the middle ground that's noisy.

plan_010 rationale: Δ_perturb=7pp (CI barely excluding 0) occurs because some perturbations accidentally make the policy slightly less clear even though no ambiguity was introduced—synonym substitution can replace a precise term with a less precise one, like "refund" becoming "reimbursement" which may have different legal implications.

plan_008 rationale: F1=0.78 is modest due to a small training set and subtle surface differences in some ambiguity types, especially coreferential cases where the ambiguous and unambiguous versions differ by only a pronoun. The per-type variation reflects how much surface editing is involved—incompleteness pairs with whole clauses added are easy to detect, while coreferential pairs with minimal pronoun changes are harder.

Now I'm ready to compile the final YAML output with all the experiment rationales.

Let me verify the parameter ranges are correct. The auth_scope range is 42pp (from 14% to 56%), which fits within the target [30,45]. The incomp range is 16pp (from 34% to 50%), which fits within [15,25]. Both check out.

Before finalizing, I need to recalculate the model main effect more carefully using just the ambiguous condition data to ensure the chi-square test is accurate.

Computing chi-square statistics...

I'm calculating Cramér's V to measure the effect size, which should be sqrt(22.43/1499) = 0.122 for the model main effect. But this doesn't match the V=0.102 I noted earlier from the framing document, so let me verify those calculations against what I have here. I'm verifying the effect size calculations—the V value of 0.093 for the overall analysis checks out when I work backward from the chi-square and sample size. For the ambiguous-only condition, I'm settling on χ²=22.4 with V=0.122, which gives me internally consistent numbers across both analyses.

Rather than obsessing over decimal-point precision, I'll use round numbers that sit in the right ballpark for what I'm trying to illustrate. I'm moving forward with the key statistics: the large effect in C1 with a confidence interval, the moderate chi-square and effect size for C2, the small gap in C3 with mixed significance across judges, and the model interaction effect for C4.

Writing YAML now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0e69164-86c5-4282-8021-142c465efd1b",
  "isSidechain": false,
  "requestId": "req_011CbF5RbHgrSQhz2kHpqRP9",
  "type": "assistant",
  "uuid": "db99e7c6-2316-4a47-b01c-be7431f5d33e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "bbbefa27-3d72-4fb3-9d7d-bdb8c8bb7c9d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AK4oDSnMoZBgnXRQpz8XBy",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19070,
      "cache_read_input_tokens": 11841,
      "output_tokens": 44746,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19070,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 44746,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19070,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19070
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

_source line 9 · 2026-05-21T04:37:59.617Z_

```yaml
tier: median
narrative_guidance: |
  核心叙事保持但需降低三处 claim 强度：
  (1) C3 layer effect 从 "significant" 降为 "suggestive tendency"，Disambiguation Channel 从 explanatory framework 进一步降为
      "observed pattern consistent with"，layer 部分移入 Discussion 而非 Results 核心位置；
  (2) perturbation control 需报告 net effect (Δ_net = Δ_ambiguity - Δ_perturb)，C1 写
      "ambiguity causes violations substantially beyond general prompt sensitivity" 而非 "ambiguity-specific"；
  (3) C5 failure mode 跨模型一致性从 "5/6 types converge" 改为
      "majority of types show consistent signatures, with model-dependent variation in 2 types"。
  C4 model×type interaction 仍是 star finding 但需 soften auth_scope 的 safety training 解释——
  极差缩小至 42pp 意味着可能是 prompt format 差异而非纯粹 training 差异。
  Title 从 "Differential Vulnerability Profiles" 微调为 "Differential Vulnerability Patterns"（避免暗示稳定 profile）。
  仍可冲 EMNLP，但需补充 1-2 个 robustness check（per-type bootstrap stability、additional perturbation pairs）作为 appendix。

imagined_experiments:
  - name: full_study_clause_generation
    plan_id: plan_001
    description: |
      生成 140 新 clause pairs（coreferential 50, authorization_scope 50, lexical +20, incompleteness +20），
      验证全部 300 pairs 跨类型平衡性，混合 CP 标注格式。
    expected_results:
      clauses_generated: 140
      clauses_passing_first_round: 131
      clauses_requiring_revision: 9
      revision_breakdown: "auth_scope 4, coreferential 3, lexical 1, incompleteness 1"
      total_validated_pairs: 300
      cross_type_balance: "50/type, PASS"
      avg_disambiguation_tokens_spec: 34.2
      avg_disambiguation_tokens_ling: 13.1
      avg_disambiguation_tokens_per_type:
        authorization_scope: 37.8
        conditional_precedence: 29.4
        incompleteness: 35.5
        lexical: 14.6
        coreferential: 8.2
        scopal: 16.4
      cp_format_mix: "28 labeled (56%), 22 unlabeled (44%)"
    result_rationale: |
      auth_scope 和 coreferential 是全新类型，设计匹配对时困难最大。auth_scope 的 4 个返修 clause 
      主要因为 unambiguous 版本的权限边界描述仍有隐含模糊（如 "authorized personnel" 改为 "Level-2 support agents" 
      但未指定 Level-2 的具体权限范围）。coreferential 的 3 个返修因 RC attachment 消歧改动过大导致 
      句法结构明显不同，需重写以保持表面相似度。disambiguation token delta 在 spec-layer 偏高（34.2 vs 13.1），
      这是 spec-layer 类型的固有特征——消歧需要添加完整的条件子句而非单词替换，但也构成潜在的 information 
      asymmetry confound，需在 Method 中报告。
    tables:
      - title: "Per-Type Clause Generation Summary"
        content: |
          | Type                 | Existing | New | Revised | Final | Avg Disambig Tokens |
          |----------------------|----------|-----|---------|-------|---------------------|
          | authorization_scope  | 0        | 50  | 4       | 50    | 37.8                |
          | conditional_prec.    | 50       | 0   | 0       | 50    | 29.4                |
          | incompleteness       | 30       | 20  | 1       | 50    | 35.5                |
          | lexical              | 30       | 20  | 1       | 50    | 14.6                |
          | coreferential        | 0        | 50  | 3       | 50    | 8.2                 |
          | scopal               | 50       | 0   | 0       | 50    | 16.4                |
          | **Total**            | **160**  |**140**|**9**  |**300**| 23.7                |
    figures_description:
      - "Token delta distribution per type (box plot): spec-layer types cluster at 29-38 tokens, ling-layer at 8-16 tokens, with auth_scope showing highest variance"
    analysis: |
      生成完成但暴露两个 methodological point：(1) spec-layer disambiguation tokens 显著高于 ling-layer 
      (34.2 vs 13.1, t-test p<0.001)，需作为 control variable 纳入 logistic regression；
      (2) auth_scope 返修率最高 (8%)，反映该类型的 ambiguous/unambiguous 边界最模糊——
      这本身也预示了该类型在实验中的高变异性。CP format mixing (56/44 labeled/unlabeled) 
      符合 Reviewer 建议。

  - name: new_type_mini_pilot
    plan_id: plan_001b
    description: |
      Coreferential + auth_scope 各 5 clauses × 2 conditions × gpt-5.4 = 20 episodes。
      验证新类型基本可行性。
    expected_results:
      total_episodes: 20
      coreferential_amb_violations: "2/5 (40%)"
      coreferential_unamb_violations: "0/5 (0%)"
      auth_scope_amb_violations: "3/5 (60%)"
      auth_scope_unamb_violations: "1/5 (20%)"
      clauses_flagged_for_revision: 1
      flagged_clause_type: "auth_scope unambiguous #3"
      api_cost_usd: 1.80
    result_rationale: |
      Coreferential 表现符合预期：amb 40% 低于其他类型的 pilot 数据（scopal 51.7%, incomp 53.3%），
      因为部分 coreferential 歧义可通过 tool response 中的实体信息部分消歧（disambiguation channel 存在）。
      Unamb 0% 证明 control condition 干净。
      Auth_scope amb 60% 符合 GPT-5.4 在该类型上的高 vulnerability 预期。但 unamb 1/5=20% 
      是问题——clause #3 的 "unambiguous" 版本写了 "Level-2 support agents may process returns 
      for standard items"，但 agent 仍将 "standard items" 的范围理解错误（边界虽明确但 agent 
      未正确遵守）。这不是 ambiguity 问题而是 instruction-following 问题，但会抬高 baseline。
      需要修改该 clause 使 unambiguous 版本的边界更加 explicit（如添加 "standard items only, 
      excluding customized and clearance items"）。
      N=5 variance 极大，不做统计推断，仅做 sanity check。
    tables:
      - title: "Mini-Pilot Results by Type and Condition"
        content: |
          | Type              | Condition   | Violations | Rate | Notes           |
          |-------------------|-------------|------------|------|-----------------|
          | coreferential     | ambiguous   | 2/5        | 40%  | expected range  |
          | coreferential     | unambiguous | 0/5        | 0%   | clean control   |
          | auth_scope        | ambiguous   | 3/5        | 60%  | expected high   |
          | auth_scope        | unambiguous | 1/5        | 20%  | clause #3 issue |
    figures_description: []
    analysis: |
      两类型基本可行。Coreferential 的低 violation rate 与 disambiguation channel 假说一致。
      Auth_scope clause #3 需返修后重跑验证。整体判定 GO，但 auth_scope baseline leakage 
      问题需在全量实验前解决——如果 10% 的 unamb clause 有类似问题，会系统性压低 binary effect。

  - name: full_study_api
    plan_id: plan_002
    description: |
      300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6) = 1,800 episodes。
      Cross-judge evaluation。Claude via OpenRouter proxy。
    expected_results:
      total_episodes: 1797
      episodes_failed_retry: 3
      gpt54_episodes: 600
      gpt41_episodes: 599
      claude_episodes: 598
      gpt54_amb_violation_rate: 0.383
      gpt54_unamb_violation_rate: 0.068
      gpt54_binary_effect_pp: 31.5
      gpt41_amb_violation_rate: 0.360
      gpt41_unamb_violation_rate: 0.062
      gpt41_binary_effect_pp: 29.8
      claude_amb_violation_rate: 0.257
      claude_unamb_violation_rate: 0.048
      claude_binary_effect_pp: 20.9
      cross_judge_pairs: "gpt-5.4 judged by gpt-4.1; gpt-4.1+Claude judged by gpt-5.4"
      api_cost_usd: 387
      runtime_hours: 14.2
    result_rationale: |
      三个 API 模型均显示显著 binary effect，但 Claude 效应量明显低于 GPT 系列（+20.9pp vs ~30pp），
      缩水幅度超过 best tier 的 25.7pp 约 5pp。原因：(1) 50-clause/type 全量集包含了更多 "边缘" 
      cases，pilot 的 10-clause 子集偏向了效应最显著的 exemplars；(2) Claude 在 auth_scope 上 
      极其稳健（amb 仅 14%），拉低了整体 ambiguous violation rate；(3) 天然的 API sampling variance 
      在单次 full run 中可能偏低方向（plan_006 ICC 数据显示 ±5-8pp per-clause variance 是正常的）。
      GPT-5.4 和 GPT-4.1 之间差异较小（38.3% vs 36.0%），不如 best tier 中的 41.0% vs 40.7% 分离度高。
      3 个 episode 因 API timeout 失败（2 个 Claude via OpenRouter, 1 个 GPT-4.1），未 retry 
      以保持时间窗口一致性。
    tables:
      - title: "Per-Model Summary (API Models)"
        content: |
          | Model            | N_amb | N_unamb | Amb Rate | Unamb Rate | Effect (pp) | p-value   |
          |------------------|-------|---------|----------|------------|-------------|-----------|
          | gpt-5.4          | 300   | 300     | 38.3%    | 6.8%       | +31.5       | <10^-14   |
          | gpt-4.1          | 300   | 299     | 36.0%    | 6.2%       | +29.8       | <10^-13   |
          | claude-sonnet-4-6| 299   | 299     | 25.7%    | 4.8%       | +20.9       | <10^-8    |
          | **API pooled**   |**899**|**898**  | **33.4%**| **5.9%**   |**+27.5**    | **<10^-20**|
    figures_description:
      - "Per-model violin plot of per-clause violation rates (ambiguous condition): Claude distribution left-shifted, GPT-5.4 and GPT-4.1 overlapping with heavier right tails"
    analysis: |
      API 模型数据收集完成。Claude 的低 vulnerability 主要来自 auth_scope（14%，vs GPT-5.4 56%），
      验证了 Anthropic 的 safety training 对授权边界类型有特殊效果。但 Claude effect 缩水至 20.9pp 
      意味着 paper 中需报告 per-model range [20.9, 31.5] 而非仅报告 pooled value。
      Cross-judge asymmetry（Claude 由 gpt-5.4 判定而非反向）需在 Method 中 disclose。

  - name: full_study_opensource
    plan_id: plan_003
    description: |
      300 clauses × 2 conditions × 2 open-source models via OpenRouter (Qwen3-235B, DeepSeek-V3) = 1,200 episodes。
    expected_results:
      total_episodes: 1196
      episodes_failed_retry: 4
      qwen3_episodes: 599
      deepseek_episodes: 597
      qwen3_amb_violation_rate: 0.333
      qwen3_unamb_violation_rate: 0.076
      qwen3_binary_effect_pp: 25.7
      deepseek_amb_violation_rate: 0.433
      deepseek_unamb_violation_rate: 0.089
      deepseek_binary_effect_pp: 34.4
      api_cost_usd: 142
      runtime_hours: 11.8
    result_rationale: |
      DeepSeek 显示最高整体 vulnerability（43.3%），效应量缩水约 4.6pp（best tier 39.0pp → 34.4pp），
      但仍是 5 模型中最大 effect。DeepSeek 在所有 6 类型上均高于 35%，验证了其 "uniform vulnerability" 
      pattern——safety training 缺乏 type-specific 针对性。
      Qwen3 效应量缩水最大（best tier 32.4pp → 25.7pp, -6.7pp），原因：(1) Qwen3 在 auth_scope 上 
      表现出乎意料地好（20%，接近 Claude 的 14%），拉低了 spec-layer 平均；(2) 但在 incompleteness 
      上很高（54%），形成与 Claude 类似但更极端的 "auth-robust, incomp-vulnerable" profile。
      Qwen3 的 unamb baseline 偏高（7.6%），部分解释了较小的 effect size。
      4 个 episode 因 OpenRouter rate limiting 失败（3 Qwen3, 1 DeepSeek）。
    tables:
      - title: "Per-Model Summary (Open-Source Models)"
        content: |
          | Model           | N_amb | N_unamb | Amb Rate | Unamb Rate | Effect (pp) | p-value   |
          |-----------------|-------|---------|----------|------------|-------------|-----------|
          | Qwen3-235B      | 300   | 299     | 33.3%    | 7.6%       | +25.7       | <10^-8    |
          | DeepSeek-V3     | 299   | 298     | 43.3%    | 8.9%       | +34.4       | <10^-14   |
          | **OS pooled**   |**599**|**597**  | **38.3%**| **8.3%**   |**+30.1**    | **<10^-18**|
    figures_description:
      - "Open-source vs API model comparison: bar chart of per-model ambiguous violation rates with 95% CI, showing DeepSeek highest, Claude lowest"
    analysis: |
      Open-source 模型数据验证了 model diversity 的价值：Qwen3 的 auth_scope robustness 挑战了 
      "仅 proprietary 模型有 auth 训练" 的简单叙事，DeepSeek 的 uniform vulnerability 提供了 
      "safety training blind spot" 假说的负面证据（或正面——取决于是否将其视为缺乏任何 type-specific training）。
      两模型的 unamb baseline 偏高（7.6%, 8.9% vs API 模型 4.8-6.8%），可能反映 open-source 模型 
      在一般 instruction-following 上略弱。

  - name: full_study_analysis
    plan_id: plan_004
    description: |
      对 plan_002 + plan_003 合计 ~2,993 episodes 的全量统计分析：C1 binary effect, C2 type hierarchy,
      C3 layer effect, C4 model×type interaction, 含 power analysis, TOST, logistic regression, inter-model agreement。
    expected_results:
      total_episodes_analyzed: 2993
      # --- C1: Binary Effect ---
      c1_pooled_effect_pp: 28.7
      c1_pooled_bootstrap_ci: "[25.8, 31.5]"
      c1_mcnemar_OR: 11.2
      c1_mcnemar_OR_ci: "[7.9, 15.8]"
      c1_mcnemar_p: "<0.0001"
      c1_per_model_effects_pp:
        claude: 20.9
        qwen3: 25.7
        gpt41: 29.8
        gpt54: 31.5
        deepseek: 34.4
      c1_all_models_significant: true
      c1_all_types_significant: true
      c1_logistic_condition_amb_coef: 1.95
      c1_logistic_condition_amb_z: 16.3
      c1_logistic_condition_amb_OR: 7.03
      # --- C2: Type Hierarchy ---
      c2_omnibus_chi2: 19.8
      c2_omnibus_p: 0.0013
      c2_omnibus_df: 5
      c2_cramers_V: 0.115
      c2_actual_power: 0.971
      c2_MDE_V: 0.093
      c2_type_rates_pooled_amb:
        incompleteness: "46.4%"
        lexical: "36.4%"
        authorization_scope: "36.0%"
        scopal: "34.4%"
        conditional_precedence: "32.8%"
        coreferential: "27.2%"
      c2_incomp_minus_coref_pp: 19.2
      c2_3tier_structure: "High: incomp (46.4%) | Mid: lex/auth/scopal/CP (32.8-36.4%) | Low: coref (27.2%)"
      c2_tost_15pp_equivalent_pairs: "6/15"
      c2_tost_15pp_nonequivalent_pairs: "9/15"
      c2_tost_10pp_equivalent_pairs: "2/15"
      c2_tost_10pp_nonequivalent_pairs: "13/15"
      c2_holm_significant_pairs: "incomp-coref (p<0.001), incomp-CP (p=0.002)"
      # --- C3: Layer Effect ---
      c3_spec_rate: "38.4%"
      c3_ling_rate: "32.7%"
      c3_layer_gap_pp: 5.7
      c3_pooled_chi2: 4.82
      c3_pooled_p: 0.028
      c3_pooled_V: 0.057
      c3_pooled_OR: 1.28
      c3_pooled_OR_ci: "[1.03, 1.59]"
      c3_within_judge_gpt41_group_gap_pp: 7.0
      c3_within_judge_gpt41_group_p: 0.11
      c3_within_judge_gpt54_group_gap_pp: 4.2
      c3_within_judge_gpt54_group_p: 0.22
      c3_per_model_layer_gaps_pp:
        gpt54: "+12.7"
        gpt41: "+10.7"
        claude: "+2.0"
        deepseek: "+1.3"
        qwen3: "0.0"
      c3_verdict: "suggestive tendency, NOT confirmed"
      # --- C4: Model × Type Interaction ---
      c4_model_main_chi2_ambonly: 22.4
      c4_model_main_p_ambonly: 0.00017
      c4_model_main_V_ambonly: 0.122
      c4_auth_scope_range_pp: 42
      c4_auth_scope_min: "Claude 14%"
      c4_auth_scope_max: "GPT-5.4 56%"
      c4_incomp_range_pp: 16
      c4_incomp_min: "Claude 34%"
      c4_incomp_max: "Qwen3 54%"
      c4_cp_range_pp: 4
      c4_fleiss_kappa: 0.33
      c4_fleiss_interpretation: "fair agreement"
      c4_lr_interaction_chi2: 36.8
      c4_lr_interaction_p: 0.012
      c4_per_model_type_chi2:
        gpt54: "χ²=18.2, p=0.003, V=0.25"
        qwen3: "χ²=14.2, p=0.014, V=0.22"
        claude: "χ²=9.8, p=0.08, V=0.18"
        gpt41: "χ²=8.2, p=0.15, V=0.17"
        deepseek: "χ²=4.8, p=0.44, V=0.13"
      # --- Logistic Regression (full model) ---
      logistic_token_delta_coef: 0.018
      logistic_token_delta_z: 2.81
      logistic_token_delta_p: 0.005
      logistic_model_aic_delta: -42.3
      # --- Inter-Model Agreement ---
      intermodel_same_interpretation_rate: 0.24
      intermodel_systematic_nocuity_rate: 0.22
    result_rationale: |
      C1 效应量从 best tier +34.0pp 缩至 +28.7pp，主要因为：(a) Claude 效应缩水最大（+25.7→+20.9pp），
      其 auth_scope 极低 vulnerability 在 50-clause 全量集中更加显著地拉低 pooled value；
      (b) Qwen3 效应也偏低（+25.7pp），部分因 unamb baseline 偏高（7.6%）；(c) 全量 50-clause 集
      比 pilot 10-clause 集多了更多 "弱效应" exemplars。但所有 5 模型 × 6 类型组合均显著 (p<0.001)，
      核心 claim 完全成立。OR=11.2 虽低于 best tier 15.1 但仍属 very large effect。

      C2 V=0.115 低于 best tier 0.137，但仍高于 MDE=0.093（power=0.971），type effect 真实存在
      但较小。3-tier 结构中 mid-tier 更加压缩（32.8-36.4% 仅 3.6pp 极差 vs best tier 36.8-42.8% 的 6pp），
      意味着 mid-tier 内部类型近乎不可区分。只有 incomp-coref 和 incomp-CP 在 Holm 校正后显著。
      TOST 在 ±15pp 下 6/15 等价 (vs best tier 8/15) 反映整体分离度下降。

      C3 pooled p=0.028 形式上显著但 within-judge 两个子组均不显著 (p=0.11, p=0.22)。
      根本原因：layer gap 高度 model-dependent——GPT 模型 +10-13pp，Claude/DeepSeek/Qwen3 ≤ +2pp。
      gpt-5.4 judged group 包含 GPT-4.1+Claude+Qwen3（后两者 gap≈0），所以子组效应被稀释。
      pooled 显著性可能反映 between-judge variance 而非真实 layer effect。必须降级为 "suggestive"。

      C4 auth_scope 极差 42pp (vs best tier 52pp) 因 GPT-5.4 从 64%→56%、DeepSeek 从 60%→48%。
      缩小的极差削弱了 "safety training differentially mitigates auth_scope" 的论证力度——
      8pp 的缩小可能意味着 pilot 阶段 GPT-5.4 高估了（sampling variance），也可能意味着 
      prompt format 差异（API 参数、system prompt 细微不同）在 pilot 中被放大。需要 soften 
      因果解释。Claude 的 per-model type χ² 从显著 (p=0.003) 降至 borderline (p=0.08)，
      因为 Claude 在全量集中 auth_scope 14% 虽仍最低但其他类型也偏低（26-38%），整体 profile 
      更"均匀地低"而非"选择性低"。GPT-4.1 也失去了显著性 (p=0.15)。
      Fleiss κ=0.33 意味着模型间对具体 clause 的 violation/no-violation 判定只有 fair agreement，
      binary effect 是 universal 的但 WHICH clauses trigger violations 高度 model-dependent。
    tables:
      - title: "C1 Per-Model Binary Effect Summary"
        content: |
          | Model      | Amb Rate | Unamb Rate | Effect (pp) | Bootstrap 95% CI  | McNemar p  |
          |------------|----------|------------|-------------|-------------------|------------|
          | Claude     | 25.7%    | 4.8%       | +20.9       | [+16.2, +25.8]    | <10^-8     |
          | Qwen3      | 33.3%    | 7.6%       | +25.7       | [+21.0, +31.4]    | <10^-8     |
          | GPT-4.1    | 36.0%    | 6.2%       | +29.8       | [+24.8, +34.9]    | <10^-13    |
          | GPT-5.4    | 38.3%    | 6.8%       | +31.5       | [+26.2, +36.8]    | <10^-14    |
          | DeepSeek   | 43.3%    | 8.9%       | +34.4       | [+29.5, +39.3]    | <10^-14    |
          | **Pooled** |**35.5%** | **6.9%**   |**+28.7**    |**[+25.8, +31.5]** |**<10^-30** |
      - title: "C2 Per-Type Violation Rates (Ambiguous Condition, Pooled Across 5 Models)"
        content: |
          | Tier | Type                 | Rate  | 95% CI        | vs Coref (pp) | Holm p  |
          |------|----------------------|-------|---------------|---------------|---------|
          | High | incompleteness       | 46.4% | [42.2, 50.6]  | +19.2         | <0.001  |
          | Mid  | lexical              | 36.4% | [32.3, 40.5]  | +9.2          | 0.068   |
          | Mid  | authorization_scope  | 36.0% | [31.9, 40.1]  | +8.8          | 0.078   |
          | Mid  | scopal               | 34.4% | [30.3, 38.5]  | +7.2          | 0.14    |
          | Mid  | conditional_prec.    | 32.8% | [28.7, 36.9]  | +5.6          | 0.27    |
          | Low  | coreferential        | 27.2% | [23.3, 31.1]  | ref           | ref     |
      - title: "C4 Model × Type Interaction Matrix (Ambiguous Condition Violation Rates)"
        content: |
          | Type                | GPT-5.4 | GPT-4.1 | Claude | Qwen3 | DeepSeek | Range |
          |---------------------|---------|---------|--------|-------|----------|-------|
          | authorization_scope | 56%     | 42%     | 14%    | 20%   | 48%      | 42pp  |
          | conditional_prec.   | 34%     | 32%     | 32%    | 32%   | 34%      | 2pp   |
          | incompleteness      | 44%     | 50%     | 34%    | 54%   | 50%      | 20pp  |
          | lexical             | 38%     | 30%     | 26%    | 40%   | 48%      | 22pp  |
          | coreferential       | 20%     | 28%     | 20%    | 30%   | 38%      | 18pp  |
          | scopal              | 38%     | 34%     | 28%    | 30%   | 42%      | 14pp  |
          | **Model avg**       |**38.3%**|**36.0%**|**25.7%**|**34.3%**|**43.3%**|   |
      - title: "C3 Per-Model Layer Gap"
        content: |
          | Model    | Spec-Layer Avg | Ling-Layer Avg | Gap (pp) | Direction        |
          |----------|----------------|----------------|----------|------------------|
          | GPT-5.4  | 44.7%          | 32.0%          | +12.7    | spec > ling      |
          | GPT-4.1  | 41.3%          | 30.7%          | +10.7    | spec > ling      |
          | Claude   | 26.7%          | 24.7%          | +2.0     | negligible       |
          | DeepSeek | 44.0%          | 42.7%          | +1.3     | negligible       |
          | Qwen3    | 33.3%          | 33.3%          | 0.0      | no difference    |
          |**Pooled**| **38.4%**      | **32.7%**      | **+5.7** | **suggestive**   |
      - title: "Logistic Regression Coefficients (Full Model)"
        content: |
          | Predictor          | Coef   | SE    | z     | p       | OR    |
          |--------------------|--------|-------|-------|---------|-------|
          | condition_amb      | 1.950  | 0.120 | 16.3  | <0.001  | 7.03  |
          | model_gpt41        | 0.550  | 0.145 | 3.79  | <0.001  | 1.73  |
          | model_gpt54        | 0.620  | 0.148 | 4.19  | <0.001  | 1.86  |
          | model_qwen3        | 0.420  | 0.144 | 2.92  | 0.004   | 1.52  |
          | model_deepseek     | 0.820  | 0.147 | 5.58  | <0.001  | 2.27  |
          | type_auth_scope    | 0.420  | 0.168 | 2.50  | 0.012   | 1.52  |
          | type_cp            | 0.280  | 0.165 | 1.70  | 0.089   | 1.32  |
          | type_incomp        | 0.850  | 0.167 | 5.09  | <0.001  | 2.34  |
          | type_lexical       | 0.440  | 0.169 | 2.60  | 0.009   | 1.55  |
          | type_scopal        | 0.330  | 0.165 | 2.00  | 0.046   | 1.39  |
          | token_delta        | 0.018  | 0.006 | 2.81  | 0.005   | 1.02  |
          | model×type (LR)    | —      | —     | —     | 0.012   | —     |
      - title: "TOST Equivalence Summary"
        content: |
          | Margin | Equivalent | Non-Equivalent | Indeterminate |
          |--------|------------|----------------|---------------|
          | ±15pp  | 6/15       | 9/15           | 0/15          |
          | ±10pp  | 2/15       | 13/15          | 0/15          |
    figures_description:
      - "Figure 2 (Forest plot): Per-type binary effect sizes with 95% bootstrap CI, pooled across 5 models. Incompleteness stands out; mid-tier cluster visible; coreferential lowest but CI still excludes 0"
      - "Figure 3 (Heatmap): 5-model × 6-type violation rate matrix. Color gradient yellow-to-red. Auth_scope column shows dramatic cross-model variation; incompleteness row uniformly dark; CP row uniformly mid-range"
      - "Figure: Layer gap by model — diverging bar chart showing GPT models positive, Claude/DeepSeek/Qwen3 near zero, illustrating model-dependence of C3"
    analysis: |
      C1 robust but effect smaller than anticipated. Paper 需报告 pooled +28.7pp 和 per-model range 
      [+20.9, +34.4]，避免 cherry-picking pooled value。Claude 的 +20.9pp 虽是最低但仍 massive 
      (OR>4, p<10^-8)。
      C2 3-tier 结构成立但 mid-tier 压缩。TOST 显示类型不可互换（±10pp 仅 2/15 等价），
      但精细排序不可靠。Paper 应强调 incomp 的 outlier 地位和 coref 的 low-end boundary case，
      不要细排 mid-tier 内部顺序。
      C3 必须降级。pooled p=0.028 仅反映大样本效应，within-judge 不显著说明 5.7pp 的 gap 
      可能 partly artifactual。建议移入 Discussion §7 作为 "observed pattern" 而非 Results §5 
      的 standalone finding。Layer gap 的 model-dependence 反而是有价值的 C4 支持证据。
      C4 是 star finding。auth_scope 42pp 极差仍然 dramatic，但需 soften 表述为 
      "consistent with differential safety training effects, though prompt format sensitivity cannot be excluded"。
      Fleiss κ=0.33 是重要发现——models agree on WHETHER ambiguity hurts but disagree on WHICH clauses。

  - name: error_analysis
    plan_id: plan_005
    description: |
      从 violation traces 中抽样 ~360 条（5 models × 6 types × ~12 traces/cell），
      分类 failure modes，分析跨模型/跨类型一致性，量化 Ambiguity Blindness。
    expected_results:
      total_traces_analyzed: 358
      traces_per_model: {gpt54: 78, gpt41: 74, claude: 42, qwen3: 68, deepseek: 96}
      # --- Failure Mode Distribution (pooled) ---
      pooled_failure_modes:
        assumption_based_action: "31.3%"
        scope_misapplication: "27.4%"
        unauthorized_escalation: "23.5%"
        arbitrary_rule_selection: "9.2%"
        conservative_refusal: "5.3%"
        other: "3.4%"
      # --- Cross-Model Consistency ---
      types_with_consistent_dominant_mode: 4
      types_with_divergent_modes: 2
      consistent_types: "auth_scope (unauthorized_escalation), incompleteness (assumption_based_action), scopal (scope_misapplication), CP (scope_misapplication+arbitrary_rule_selection)"
      divergent_types: "lexical (GPT→assumption_based_action, OS→scope_misapplication), coreferential (flat distribution, no dominant mode)"
      # --- Ambiguity Blindness ---
      awareness_rate_pct: 9.2
      awareness_range_by_model: "[4.8% (GPT-5.4), 14.3% (Claude)]"
      surface_adoption_pct: 84.1
      escalate_to_user_pct: 1.1
      # --- Layer Mechanism ---
      ling_layer_scope_misapplication_pct: 36.2
      spec_layer_scope_misapplication_pct: 13.8
      spec_layer_escalation_plus_assumption_pct: 62.4
      # --- Cross-Domain ---
      airline_vs_retail_max_delta_pp: 14.2
      airline_vs_retail_delta_type: "unauthorized_escalation (retail 37.1% vs airline 22.9%)"
      # --- Coreferential Boundary ---
      coreferential_conservative_refusal_pct: 8.4
      coreferential_n_traces: 28
      # --- Automated Inter-Coder Agreement ---
      cross_coding_n: 72
      cross_coding_agreement_pct: 76.4
      cross_coding_cohens_kappa: 0.548
      gwets_AC1: 0.682
    result_rationale: |
      4/6 类型跨 5 模型一致（vs best tier 5/6），原因：
      (1) auth_scope→unauthorized_escalation 在 Claude 上只有 ~7 条 traces（14% rate × 50 episodes），
          其中 45% 是 unauthorized_escalation、25% conservative_refusal——pattern 不同但 N 太小不影响
          overall consistency（4/5 模型仍以 unauthorized_escalation 为主导）；
      (2) incompleteness 和 scopal 的 failure mode 由 ambiguity type 本身的结构决定（缺信息→猜测行动，
          scope 模糊→misapply scope），不依赖模型架构，故高度一致；
      (3) lexical 类型出现 model-family 分裂：GPT 系列将词汇歧义处理为信息缺口（assumption_based_action 60-68%），
          open-source 模型（Qwen3, DeepSeek）更倾向 scope_misapplication（45-52%），可能反映 
          training data 中对词汇多义性的不同处理策略。这是 median 档独有的发现——best tier 中
          只有 2 模型，未能检测到此 family-level divergence；
      (4) coreferential 仍无主导 failure mode（flat distribution），N=28 traces 中 scope_misapplication 30%、
          assumption_based_action 25%、unauthorized_escalation 18%——三种模式均无法突出。

      Awareness rate 9.2% 高于 best tier GPT-5.4 的 4.1% 但符合范围，因为 Claude 的 awareness 最高
      （14.3%——其 RLHF 可能 implicitly 训练了更多 metacognitive hedging）。Surface adoption 84.1% 
      略低于 best tier 88%+，反映 5-model pool 中有更多 variance。

      Cross-coding κ=0.548 低于 best tier 0.594，因为 5-model traces 引入了更多 edge cases（尤其 
      Qwen3 和 DeepSeek 的 failure mode 表述风格不同于 GPT 系列）。Gwet's AC1=0.682 好于 κ，
      因为 kappa paradox 在 high-prevalence categories 中更严重。
    tables:
      - title: "Failure Mode × Type Distribution (Pooled Across 5 Models)"
        content: |
          | Type          | assumption | unauth_esc | scope_misapp | arb_rule | conserv_ref | other |
          |---------------|-----------|------------|--------------|----------|-------------|-------|
          | auth_scope    | 15%       | 68%        | 8%           | 2%       | 4%          | 3%    |
          | CP            | 22%       | 8%         | 35%          | 28%      | 4%          | 3%    |
          | incompleteness| 60%       | 18%        | 10%          | 6%       | 3%          | 3%    |
          | lexical       | 52%       | 6%         | 28%          | 6%       | 4%          | 4%    |
          | coreferential | 25%       | 18%        | 30%          | 8%       | 12%         | 7%    |
          | scopal        | 10%       | 5%         | 72%          | 6%       | 4%          | 3%    |
      - title: "Lexical Failure Mode by Model Family (Divergent Type)"
        content: |
          | Model Family  | assumption_based | scope_misapp | other modes |
          |---------------|-----------------|--------------|-------------|
          | GPT-5.4       | 64%             | 18%          | 18%         |
          | GPT-4.1       | 60%             | 22%          | 18%         |
          | Claude        | 58%             | 24%          | 18%         |
          | Qwen3         | 38%             | 45%          | 17%         |
          | DeepSeek      | 35%             | 52%          | 13%         |
      - title: "Ambiguity Blindness Metrics by Model"
        content: |
          | Model    | Awareness | Surface Adoption | Escalate to User |
          |----------|-----------|------------------|------------------|
          | GPT-5.4  | 4.8%      | 88.2%            | 0.6%             |
          | GPT-4.1  | 10.2%     | 83.7%            | 1.4%             |
          | Claude   | 14.3%     | 78.4%            | 2.1%             |
          | Qwen3    | 8.6%      | 84.2%            | 0.8%             |
          | DeepSeek | 5.9%      | 86.8%            | 0.4%             |
          |**Pooled**| **9.2%**  | **84.1%**        | **1.1%**         |
    figures_description:
      - "Figure 5 (Stacked bar): Per-type failure mode distribution, showing type-diagnostic signatures — auth_scope dominated by red (unauthorized_escalation), incompleteness by blue (assumption_based_action), scopal by green (scope_misapplication)"
      - "Figure 6 (Split panel): Lexical failure modes by model family — left panel GPT-family (assumption dominant), right panel OS-family (scope_misapplication dominant), illustrating the 2-type divergence"
      - "Figure 7 (Annotated trace pair): CP trace showing explicit conflict detection ('I notice rules A and B appear to conflict') vs scopal trace showing zero awareness and surface scope adoption"
    analysis: |
      C5 核心发现（type-specific signatures + Ambiguity Blindness）成立，但跨模型一致性需 soften。
      Paper 表述从 "5/6 types converge" 改为 "4/6 types show consistent dominant failure modes across 
      all 5 models; lexical type shows a model-family split (GPT → assumption, OS → scope misapplication); 
      coreferential shows no dominant mode reflecting diverse resolution strategies"。
      Lexical 的 model-family split 是 median 档的独有洞察——可以在 Discussion 中讨论 training data 
      composition 如何影响 failure mode，但不应 overclaim 因果关系。
      Ambiguity Blindness 数据显示 Claude 的 awareness 最高 (14.3%)，与其最低 violation rate 一致——
      但不能推断因果（可能是 RLHF 导致更多 hedging 而非真正的 ambiguity detection）。
      Cross-coding κ=0.548 需在 paper 中 report 并 caveat："automated coding shows moderate agreement; 
      fine-grained per-type percentages should be interpreted as approximate。"

  - name: reliability_test
    plan_id: plan_006
    description: |
      30 representative clauses (5/type) × 3 replicates × 2 conditions × 2 API models = 360 episodes。
      计算 ICC 评估 per-clause violation rate 的 test-retest reliability。
    expected_results:
      total_episodes: 358
      episodes_complete: 355
      episodes_pending_judgment: 3
      overall_ICC: 0.882
      overall_ICC_ci: "[0.842, 0.915]"
      binary_ICC: 0.814
      binary_ICC_ci: "[0.758, 0.860]"
      per_model_ICC:
        gpt54: 0.889
        gpt41: 0.875
      per_type_ICC:
        scopal: 0.952
        lexical: 0.938
        coreferential: 0.924
        authorization_scope: 0.834
        conditional_precedence: 0.821
        incompleteness: 0.792
      per_layer_ICC:
        ling_layer_avg: 0.938
        spec_layer_avg: 0.816
      bootstrap_ci_width_median_pp: 8.2
    result_rationale: |
      Overall ICC=0.882 (good) 略低于 best tier 0.919（excellent），因为：
      (1) 30-clause 子集中 spec-layer clauses 的 replicate variance 较高——incompleteness 的某些 
          clauses 在 3 次 replicate 中分别得到 0/1/1 的 violation 结果（20%-80% swing），这是因为 
          spec-layer ambiguity 缺乏外部消歧渠道，agent 每次 "猜" 不同方向；
      (2) Ling-layer clauses（scopal, lexical, coref）ICC 全部 >0.92，因为其消歧路径（tool response、
          世界知识）在 replicate 间稳定；
      (3) Per-model ICC 接近（0.889 vs 0.875），说明 reliability 不依赖模型选择；
      (4) Bootstrap CI 中位宽度 8.2pp 高于目标 <10pp，勉强 PASS——意味着 individual clause-level 
          的 effect size 估计有 ~±4pp 不确定性，但 type-level 和 pooled 分析因聚合效应而更精确。
      Spec-layer 低 ICC 是 Disambiguation Channel Framework 的直接预测——agent 对 spec-layer 
      ambiguity 的响应更不可预测，因为没有 external signal 来锚定解读。
    tables:
      - title: "ICC by Type and Layer"
        content: |
          | Layer | Type                | ICC   | 95% CI        | Interpretation |
          |-------|---------------------|-------|---------------|----------------|
          | Ling  | scopal              | 0.952 | [0.912, 0.978]| excellent      |
          | Ling  | lexical             | 0.938 | [0.892, 0.968]| excellent      |
          | Ling  | coreferential       | 0.924 | [0.871, 0.960]| excellent      |
          | Spec  | authorization_scope | 0.834 | [0.748, 0.904]| good           |
          | Spec  | conditional_prec.   | 0.821 | [0.732, 0.893]| good           |
          | Spec  | incompleteness      | 0.792 | [0.694, 0.873]| good           |
          |       | **Overall**         |**0.882**|**[0.842, 0.915]**| **good**   |
    figures_description:
      - "ICC forest plot by type: ling-layer types clustered at 0.92-0.95, spec-layer at 0.79-0.83, clear layer separation visible"
    analysis: |
      Reliability 达到 good 水平但未达 excellent。Paper 可以报告 "per-clause violation rates show 
      good test-retest reliability (ICC=0.882)"，但需在 Limitations 中提及 spec-layer types 的 
      lower reliability (ICC 0.79-0.83) 及其对 fine-grained per-clause inference 的限制。
      ICC 的 layer pattern (ling > spec) 是 Disambiguation Channel Framework 的 convergent evidence——
      但在 median 档下只能作为 "consistent with" 而非 "supports"。

  - name: realism_validation
    plan_id: plan_007
    description: |
      比较 300 synthetic clause pairs 与 DRIP-R 自然 ambiguity 的语言学属性
      (sentence length, parse depth, Flesch-Kincaid, TTR, token count)，
      KS 检验判断分布差异。
    expected_results:
      n_synthetic: 300
      n_drip_r_reference: 187
      ks_sentence_length_p: 0.041
      ks_sentence_length_D: 0.142
      ks_parse_depth_p: 0.34
      ks_flesch_kincaid_p: 0.42
      ks_ttr_p: 0.28
      ks_token_count_p: 0.18
      synthetic_mean_sentence_length: 22.3
      drip_r_mean_sentence_length: 19.8
      significant_properties: 1
      nonsignificant_properties: 4
    result_rationale: |
      4/5 语言学属性无显著差异，说明 synthetic injection 没有创造系统性的表面特征偏差。
      Sentence length (p=0.041) 显著偏高 (22.3 vs 19.8 words)，原因：消歧操作（尤其 spec-layer 
      types 添加条件子句）使 ambiguous 版本在移除消歧内容后仍保留了较复杂的句法结构。
      这是一个 minor confound——更长的句子可能本身就更难处理，但 plan_004 的 logistic regression 
      已将 token_delta 作为 control variable（coef=0.018, p=0.005），显示其效应存在但远小于 
      ambiguity condition 效应（coef=1.95）。
      Parse depth, readability, lexical diversity 和 token count 均在 DRIP-R 分布范围内，
      表明 synthetic clauses 的整体语言复杂度与自然 policy ambiguity 一致。
    tables:
      - title: "Linguistic Property Comparison: Synthetic vs DRIP-R"
        content: |
          | Property        | Synthetic (mean±sd) | DRIP-R (mean±sd) | KS D  | KS p  | Sig?  |
          |-----------------|---------------------|-------------------|-------|-------|-------|
          | Sentence length | 22.3 ± 6.8         | 19.8 ± 5.4        | 0.142 | 0.041 | *     |
          | Parse depth     | 5.2 ± 1.9          | 5.0 ± 1.7         | 0.087 | 0.34  | n.s.  |
          | Flesch-Kincaid  | 11.4 ± 2.3         | 11.1 ± 2.1        | 0.078 | 0.42  | n.s.  |
          | TTR             | 0.68 ± 0.12        | 0.71 ± 0.11       | 0.092 | 0.28  | n.s.  |
          | Token count     | 28.7 ± 8.4         | 26.2 ± 7.1        | 0.103 | 0.18  | n.s.  |
    figures_description:
      - "Overlaid density plots for each property: synthetic (blue) vs DRIP-R (orange). Only sentence length shows visible right-shift for synthetic"
    analysis: |
      Realism validation 整体 PASS。Sentence length 差异需在 Method §4 中 disclose：
      "Synthetic clauses are marginally longer than naturally occurring policy ambiguities 
      (22.3 vs 19.8 words, KS p=0.041), reflecting the structural complexity required for 
      matched-pair design. Token delta is included as a control variable in all regression analyses."
      这不影响核心 claims 但是 honest reporting 的要求。

  - name: judge_calibration
    plan_id: plan_009
    description: |
      100 episodes stratified 抽样 × 2 human annotators 标注，
      计算 LLM judge 与 human ground truth 的 precision/recall/F1，
      per-severity-tier agreement，以及 20-30 failure mode traces 的人工验证。
    expected_results:
      n_episodes_sampled: 100
      n_human_annotators: 2
      human_inter_annotator_kappa: 0.78
      human_agreement_pct: 88.0
      # --- Judge vs Human (Binary: violation/no-violation) ---
      judge_human_binary_kappa: 0.74
      judge_human_binary_F1: 0.87
      judge_human_binary_precision: 0.89
      judge_human_binary_recall: 0.87
      # --- Judge vs Human (3-tier severity) ---
      judge_human_severity_kappa: 0.65
      judge_human_severity_weighted_F1: 0.80
      per_severity_F1:
        no_violation: 0.90
        minor_violation: 0.68
        moderate_violation: 0.82
        severe_violation: 0.88
      # --- Confusion Patterns ---
      most_confused_pair: "minor_violation ↔ no_violation"
      confusion_rate_minor_as_none: "26.7% (4/15)"
      confusion_rate_none_as_minor: "13.3% (6/45)"
      # --- Failure Mode Trace Validation ---
      n_failure_mode_traces_validated: 24
      failure_mode_human_agreement_pct: 70.8
      failure_mode_dominant_mode_match: "5/6 types match human coding"
    result_rationale: |
      Human κ=0.78 (good) 达到 target ≥0.75，说明 violation 判定任务的人类 ground truth 可靠。
      Judge binary F1=0.87 属于 adequate——大多数 "明确 violation"（如 unauthorized refund、越权操作）
      和 "明确 no-violation" 被正确分类。但 minor violation tier F1=0.68 显著低于其他 tier，
      原因：(1) minor violations 本身定义模糊——"slightly exceeding scope" vs "reasonable interpretation" 
      的边界是主观的；(2) LLM judge 倾向于二值化（clear violation or not），对中间地带不敏感；
      (3) 15 个 human-labeled minor violations 中有 4 个被 judge 归为 no-violation（26.7% miss rate）。

      Judge-human κ=0.72 低于 judge-judge κ=0.91（来自 best tier framing 数据），正是 plan_009 
      被升级为 P0 的原因——judge 之间高度一致不等于 judge 准确。κ=0.72 的 gap 集中在 minor 
      violations 和 auth_scope 的 boundary cases 上。

      Severity tier 的不稳定性意味着 paper 应以 binary violation 为主要分析单元，
      severity-based 分析作为 supplementary。plan_005 的 failure mode coding 在 24 traces 
      人工验证中 70.8% agreement，5/6 types 的 dominant mode 与人工编码一致，
      但 auth_scope 的 unauthorized_escalation vs inappropriate_action 边界仍模糊。

      整体判定：judge 在 binary level 可信（F1=0.87, κ=0.74），在 severity level 有 noise 
      但不影响核心 claims（C1-C4 均基于 binary violation）。
    tables:
      - title: "Judge vs Human Confusion Matrix (Binary)"
        content: |
          |                    | Judge: No Violation | Judge: Violation |
          |--------------------|---------------------|------------------|
          | Human: No Violation| 39                  | 6                |
          | Human: Violation   | 7                   | 48               |
          | **Metrics**        | Precision=0.85      | Precision=0.89   |
          |                    | **Binary κ=0.74**   | **Binary F1=0.87**|
      - title: "Per-Severity-Tier F1"
        content: |
          | Severity Tier    | N (human) | Precision | Recall | F1   | Primary Confusion     |
          |------------------|-----------|-----------|--------|------|-----------------------|
          | No violation     | 45        | 0.85      | 0.87   | 0.90 | ← minor (6 cases)    |
          | Minor violation  | 15        | 0.69      | 0.67   | 0.68 | → no_violation (4)    |
          | Moderate         | 22        | 0.82      | 0.82   | 0.82 | ↔ minor/severe (4)   |
          | Severe           | 18        | 0.88      | 0.89   | 0.88 | ← moderate (2)        |
    figures_description:
      - "Confusion heatmap: 4×4 matrix showing strong diagonal with off-diagonal concentration at minor↔no_violation boundary"
      - "Per-tier F1 bar chart with 95% Wilson CI: minor tier's CI extends below 0.60, other tiers well above 0.75"
    analysis: |
      Judge calibration 在 binary level 充分，在 severity level 有 caveat。Paper Method §4 报告：
      "LLM judge achieves good agreement with human ground truth (binary κ=0.74, F1=0.87). 
      Severity-tier classification is less reliable (weighted F1=0.80), with minor violations 
      showing the lowest agreement (F1=0.68). All primary analyses use binary violation classification."
      Minor tier 的低 F1 不影响 C1-C4（均基于 binary），但如果 paper 报告 severity 分布
      （如 C5 error analysis 中区分 severity），需要 caveat。
      Failure mode validation (70.8% agreement, 24 traces) 虽 N 小但 5/6 dominant mode match 
      提供了基本的 face validity。完整的 human failure mode coding 留作 future work。

  - name: perturbation_control
    plan_id: plan_010
    description: |
      30 non-ambiguity perturbation pairs (15 synonym + 15 reorder) × 2 conditions × 3 API models = 180 episodes。
      区分 ambiguity-specific harm 与 general prompt brittleness。
    expected_results:
      total_episodes: 178
      episodes_failed: 2
      perturbation_types: {synonym: 15, reorder: 15}
      original_violation_rate: 0.067
      perturbed_violation_rate: 0.139
      delta_perturb_pp: 7.2
      delta_perturb_ci: "[1.5, 12.9]"
      delta_perturb_ci_contains_zero: false
      ambiguity_delta_pp: 28.7
      delta_net_pp: 21.5
      ratio: 0.251
      verdict: "PASS+caveat"
      synonym_delta_pp: 5.8
      reorder_delta_pp: 8.6
      per_model_perturb_delta:
        gpt54: 8.3
        gpt41: 6.1
        claude: 4.8
    result_rationale: |
      Δ_perturb=7.2pp 显著高于 best tier 的 3.33pp（CI 含 0），原因：
      (1) Synonym substitution 中部分 "同义词" 实际有微妙语义差异——如 "refund" → "reimbursement" 
          在 policy 语境下可能暗示不同的处理流程，agent 对此敏感；
      (2) Clause reordering 效应更大 (8.6pp vs synonym 5.8pp)，因为条件子句的顺序影响 agent 
          的 salience weighting——先出现的条件被赋予更高权重（primacy effect），重排后某些 
          exception 条件被 "buried" 导致 agent 忽略；
      (3) GPT-5.4 对 perturbation 最敏感 (8.3pp)，Claude 最稳健 (4.8pp)，与 overall 
          prompt sensitivity 的 model ranking 一致。

      CI [1.5, 12.9] 不含 0 是关键 caveat——意味着非歧义性表面改动确实造成了 non-trivial 
      的 violation rate 增加。但 ratio=0.251 表明歧义效应 (28.7pp) 远大于一般敏感性 (7.2pp)，
      net effect 21.5pp 仍然 massive。

      判定标准：5-10pp + ratio 0.15-0.30 = PASS+caveat。
      Paper 需写："Ambiguity causes violations substantially beyond general prompt sensitivity 
      (Δ_net=21.5pp, 75% of the total ambiguity effect is ambiguity-specific), though non-ambiguity 
      perturbations also produce a small but significant increase (Δ_perturb=7.2pp, CI [1.5, 12.9])."
    tables:
      - title: "Perturbation Control Summary"
        content: |
          | Metric                  | Value             | Interpretation              |
          |-------------------------|-------------------|-----------------------------|
          | Δ_perturb (overall)     | 7.2pp [1.5, 12.9] | significant, small          |
          | Δ_perturb (synonym)     | 5.8pp             | borderline significant      |
          | Δ_perturb (reorder)     | 8.6pp             | significant                 |
          | Δ_ambiguity (from C1)   | 28.7pp            | massive                     |
          | Δ_net                   | 21.5pp            | ambiguity-specific, large   |
          | Ratio (perturb/ambig)   | 0.251             | 25% attributable to surface |
          | **Verdict**             | **PASS+caveat**   | C1 holds with net framing   |
      - title: "Per-Model Perturbation Sensitivity"
        content: |
          | Model    | Original Rate | Perturbed Rate | Δ_perturb (pp) |
          |----------|---------------|----------------|-----------------|
          | GPT-5.4  | 7.8%          | 16.1%          | +8.3            |
          | GPT-4.1  | 6.3%          | 12.4%          | +6.1            |
          | Claude   | 4.2%          | 9.0%           | +4.8            |
    figures_description:
      - "Three-bar comparison: Δ_perturb (7.2pp, gray), Δ_net (21.5pp, blue), total Δ_ambiguity (28.7pp, red). Stacked to show composition. Error bars on each component."
    analysis: |
      Perturbation control 是 median 档与 best tier 的关键差异。Best tier Δ_perturb=3.33pp (CI含0) 
      允许最强因果 claim；median 档 7.2pp (CI不含0) 要求 net effect framing。
      Paper C1 的核心句从 "ambiguity-specific causation" 改为 "ambiguity causes violations 
      substantially beyond general prompt sensitivity"——这仍然是 strong claim 但诚实承认了 
      一部分效应来自表面改动。Δ_net=21.5pp 仍是 agent safety 文献中最大的因果估计。
      Reorder > synonym 的发现本身是有意义的——可在 Discussion 中简短讨论 clause ordering 
      as a prompt sensitivity factor。但不要 overclaim，这只有 15 pairs。
      建议：在 appendix 中补充额外 30 pairs（15 synonym + 15 reorder）以收窄 CI 至 <8pp width，
      这是 median 档需要的 robustness check 之一。

  - name: classifier_poc
    plan_id: plan_008
    description: |
      DeBERTa-v3-large binary ambiguity detector PoC：在 300 clause pairs 上 fine-tune，
      80/20 split，评估 held-out performance。
    expected_results:
      model: "DeBERTa-v3-large"
      train_pairs: 240
      test_pairs: 60
      epochs: 5
      learning_rate: 2.0e-5
      test_binary_F1: 0.78
      test_precision: 0.81
      test_recall: 0.75
      test_AUC: 0.85
      per_type_F1:
        incompleteness: 0.86
        authorization_scope: 0.82
        conditional_precedence: 0.76
        lexical: 0.79
        scopal: 0.73
        coreferential: 0.68
      gpu_hours_used: 2.4
      training_cost_usd: 8.50
    result_rationale: |
      F1=0.78 是 reasonable PoC 性能但不突出，原因：
      (1) 训练集仅 240 pairs，对 DeBERTa 来说是 very low resource setting；
      (2) 每种类型仅 ~40 train examples，不足以学到 type-specific patterns；
      (3) Per-type 性能与 disambiguation token delta 高度相关：incompleteness (35.5 tokens avg edit) 
          最容易检测（F1=0.86），因为 ambiguous 和 unambiguous 版本表面差异大；
          coreferential (8.2 tokens) 最难（F1=0.68），因为差异仅在代词或 RC attachment 上。

      F1=0.78 足以证明 "automated ambiguity detection is feasible" 这一 practical implication，
      但不足以作为 standalone contribution。定位为 appendix PoC，标题可以是 
      "Preliminary: Toward Automated Policy Ambiguity Detection"。
      Chantree et al. (2006) 的 nocuous ambiguity detector 在 controlled dataset 上 
      precision ~80%——与我们的 0.81 precision 可比，但他们的 recall 更高 (~0.85)，
      可能因为他们的 training set 更大且 domain-specific features 更多。
    tables:
      - title: "Classifier PoC Results by Type"
        content: |
          | Type                | Test N | F1   | Precision | Recall | Avg Token Δ |
          |---------------------|--------|------|-----------|--------|-------------|
          | incompleteness      | 10     | 0.86 | 0.88      | 0.84   | 35.5        |
          | authorization_scope | 10     | 0.82 | 0.84      | 0.80   | 37.8        |
          | lexical             | 10     | 0.79 | 0.82      | 0.76   | 14.6        |
          | conditional_prec.   | 10     | 0.76 | 0.78      | 0.74   | 29.4        |
          | scopal              | 10     | 0.73 | 0.75      | 0.71   | 16.4        |
          | coreferential       | 10     | 0.68 | 0.72      | 0.65   | 8.2         |
          | **Overall**         | **60** |**0.78**|**0.81** |**0.75**| 23.7        |
    figures_description:
      - "ROC curve (AUC=0.85) with per-type operating points marked, showing incompleteness near top-left corner and coreferential closer to diagonal"
      - "Scatter plot: per-type F1 vs avg disambiguation token delta, showing strong positive correlation (r=0.91)"
    analysis: |
      PoC 成功 demonstrate feasibility。F1 与 token delta 的 r=0.91 相关性本身是有趣的发现——
      说明 classifier 主要依赖 surface-level 信号（信息量差异）而非深层语义理解。
      这暗示更好的 classifier 需要 semantic representations 而非纯 surface features。
      Paper 中作为 §7 Discussion 的一段或 Appendix B，不列为 main contribution。
      连线 Chantree et al. (2006): "Our PoC achieves comparable precision (0.81 vs ~0.80) 
      with substantially less training data, suggesting modern PLMs can bootstrap from small 
      annotated datasets for ambiguity detection."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "db99e7c6-2316-4a47-b01c-be7431f5d33e",
  "isSidechain": false,
  "requestId": "req_011CbF5RbHgrSQhz2kHpqRP9",
  "type": "assistant",
  "uuid": "e2b4cc63-c1dd-43fc-83c1-0c65951861a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "bbbefa27-3d72-4fb3-9d7d-bdb8c8bb7c9d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AK4oDSnMoZBgnXRQpz8XBy",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19070,
      "cache_read_input_tokens": 11841,
      "output_tokens": 44746,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19070,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 44746,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19070,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19070
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：C1/C2/C4/C5 成立但部分效应量缩水，C3 layer effect 保持 fragile（within-judge 不显著），judge calibration 中等，需调整部分 claim 表述强度 核心假设：['C1 binary effect 成立但效应量略低于 5-model 聚合值，部…",
  "leafUuid": "e2b4cc63-c1dd-43fc-83c1-0c65951861a9",
  "sessionId": "bbbefa27-3d72-4fb3-9d7d-bdb8c8bb7c9d"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Differential nocuity across LLM models and ambiguity types",
  "sessionId": "bbbefa27-3d72-4fb3-9d7d-bdb8c8bb7c9d"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：C1/C2/C4/C5 成立但部分效应量缩水，C3 layer effect 保持 fragile（within-judge 不显著），judge calibration 中等，需调整部分 claim 表述强度 核心假设：['C1 binary effect 成立但效应量略低于 5-model 聚合值，部…",
  "leafUuid": "e2b4cc63-c1dd-43fc-83c1-0c65951861a9",
  "sessionId": "bbbefa27-3d72-4fb3-9d7d-bdb8c8bb7c9d"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Differential nocuity across LLM models and ambiguity types",
  "sessionId": "bbbefa27-3d72-4fb3-9d7d-bdb8c8bb7c9d"
}
```

---
