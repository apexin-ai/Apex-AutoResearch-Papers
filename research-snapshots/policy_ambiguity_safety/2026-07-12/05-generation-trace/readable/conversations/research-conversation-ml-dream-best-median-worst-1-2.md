# Research conversation: 你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。 你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/942a8489-57e5-46b7-9ba6-6f129bdc29b2.jsonl`
- **Structured JSON:** [`02b4ccc1e0fd84d289e3.json`](../../sessions/02/02b4ccc1e0fd84d289e3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T11:16:52.508Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T11:16:52.508Z",
  "sessionId": "942a8489-57e5-46b7-9ba6-6f129bdc29b2",
  "content": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。\n\n你需要同时定义 best / median / worst 三档：\n1. 每档的核心假设（哪些假设成立/不成立）\n2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）\n3. 每档的论文叙事方向——\n   - best: 原始 framing 完全成立，claims 无需调整\n   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验\n   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）\n\n三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性\n自行判断。但必须确保三档之间的数字和叙事逻辑一致。\n\n# Project context\nproject: policy_ambiguity_safety\nvenue: emnlp-2026\nfocus: Cross-benchmark replication on SOPBench (Healthcare + Bank domains) added to plan. Assess: (1) Does SOPBench replication meaningfully strengthen the paper vs current single-benchmark version? (2) What's the realistic best/median/worst score with vs without SOPBench? (3) Are there any risks (e.g., effect doesn't replicate, rule-based verifier incompatibility)? Round 13 claim calibration already complete (22× removed, margin conditions added, judge annotations, confound anchors).\n\n## paper_framing.md\n\n# Paper Framing — policy_ambiguity_safety\n\n> 最后更新: 2026-05-20 19:30 UTC | 状态: 5-model analysis complete, C3/C4 framing revised\n> 目标: EMNLP 2026 (ARR Aug cycle, DDL ~Aug 3)\n> Dream: dream_20260520T112859 — best 3.5 / median 3.0 / worst 2.5 (pre-pivot; re-dream needed)\n> 5-model: 2,997 episodes, C1 confirmed (+34.0pp, 5 models), C4 upgraded (model×type interaction)\n\n## Core Insight\n\nPolicy ambiguity universally causes massive safety violations in LLM agents (+34.0pp across 5 architecturally diverse models), with a significant type hierarchy (incompleteness 53.6% >> coreferential 31.6%). Specification-layer types are more dangerous on average (Δ=6.08pp, p=0.017), but the deeper finding is a **model × type interaction**: authorization scope vulnerability varies 52pp across models (12% Claude to 64% GPT-5.4), revealing that safety training differentially mitigates specific ambiguity types, while incompleteness remains universally dangerous. This interaction connects Berry & Kamsties' nocuous ambiguity theory to modern safety alignment and suggests both type-aware triage AND model-aware risk assessment.\n\n## Title (Working)\n\n\"Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families\"\n\nAlternative: \"Differential Nocuity: How Ambiguity Type and Model Architecture Shape Safety Violations in LLM Agents\"\n\nNote: Pivoted from \"Uniformly Nocuous\" → \"Specification-Layer Dominant\" (2-model) → \"Differential Nocuity with Model Interaction\" (5-model). The model × type interaction is the novel finding that elevates the paper beyond simple effect demonstration.\n\n## Core Claims\n\n### C1: Binary Effect (PRIMARY — confirmed, 5 models)\nAmbiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +34.0pp (5-model), McNemar OR=15.1 (CI: [10.78, 21.17]), p<0.0001. Holds across all 6 types and all 5 models.\n- **Evidence**: 2,997 episodes across 5 models × 6 types × 2 conditions. Bootstrap CI: [+31.2pp, +36.9pp].\n- **Per-model**: Claude +25.7pp, Qwen3 +32.4pp, GPT-4.1 +34.7pp, GPT-5.4 +38.3pp, DeepSeek +39.0pp — all p<10^-17.\n- **Strength**: Extremely strong. Replicated across 5 architecturally diverse models (proprietary dense, open-source MoE, open-source dense), 6 types, 2 domains. No exceptions.\n- **Causal backing**: Matched-pair design + perturbation control (plan_010, Δ_perturb=3.33pp, PASS) → strongest causal inference in the literature.\n- **Logistic regression**: condition_amb coef=2.278, z=19.65, p<0.001 — ambiguity is the dominant predictor even after controlling for token delta, model, and type.\n\n### C2: Type Hierarchy (SECONDARY — confirmed, 5 models)\n**PIVOTED from uniformity null.** 6-type hierarchy significant: omnibus χ²=28.02, p=3.6×10^-5, V=0.137 (small but well-powered: actual power=0.993, MDE=0.093). 3-tier structure emerges from TOST analysis.\n- **Evidence**: 2,997 episodes (5 models × 6 types × 2 conditions, ambiguous only: 1,499 episodes)\n  - **High tier**: incompleteness 53.6% (standout — universally dangerous across all models)\n  - **Mid tier**: lexical 42.8%, auth_scope 41.6%, scopal 39.4%, CP 36.8% — pairwise equivalent at ±15pp\n  - **Low tier**: coreferential 31.6% (lowest — partial disambiguation via tool responses)\n- **TOST structure**: ±15pp: 8/15 equivalent, 7/15 non-equivalent. ±10pp: 4/15 equivalent, 11/15 non-equivalent. Types are NOT interchangeable.\n- **V=0.137 context**: Below 0.20 threshold but well-powered (power=0.993). The type effect is real but small — the 3-tier structure captures it better than a single V statistic. The heterogeneity is driven by the extremes (incompleteness 53.6% vs coreferential 31.6% = 22pp gap).\n- **Coreferential as boundary case**: 31.6% violation rate is the lowest but still substantial (+18.7pp vs unambiguous). Agents partially disambiguate via tool responses and cautious strategies. Conservative_refusal rate 6-11% (vs avg 2-3%).\n- **Model-dependence of type rankings**: Type rankings are NOT identical across models. Incompleteness is top-2 for ALL models, but auth_scope ranges from #1 (GPT-5.4, DeepSeek) to #6 (Claude). See C4.\n\n### C3: Layer Effect (TERTIARY — suggestive, fragile under within-judge analysis)\n**[2026-05-20 REVISED with 5-model data + within-judge check]** Specification-layer ambiguities cause more violations than linguistic-layer on average, but the effect is modest, model-dependent, and fragile under subgroup analysis.\n- **Evidence (5-model aggregate)**: Spec 44.0% vs Ling 37.9%, Δ=6.08pp, CI [1.14, 11.02], χ²=5.73, p=0.017, V=0.062 (small), OR=1.29 [1.05, 1.58].\n- **Within-judge fragility**: gpt-4.1 judged group (gpt-5.4+DeepSeek): Δ=+8.0pp, p=0.059 (marginal). gpt-5.4 judged group (gpt-4.1+Claude+Qwen3): Δ=+4.8pp, p=0.157 (n.s.). Pooled significance may partly reflect between-judge variance or insufficient within-group power. Paper表述: \"suggestive\" or \"a moderate tendency,\" NOT \"confirmed.\" Disclose within-judge non-significance in Limitations.\n- **Per-model layer gaps** (THE KEY FINDING — feeds C4):\n  - GPT-5.4: +14.0pp (spec 48.0% vs ling 34.0%) — strong\n  - GPT-4.1: +12.0pp (spec 46.7% vs ling 34.7%) — strong\n  - Claude: +3.3pp (spec 32.0% vs ling 28.7%) — weak\n  - DeepSeek: +2.0pp (spec 50.7% vs ling 48.7%) — negligible\n  - Qwen3: -0.9pp (spec 42.7% vs ling 43.6%) — reversed!\n- **Root cause**: auth_scope is the primary driver. GPT models have extremely high auth_scope rates (46-64%), inflating their spec-layer average. Claude (12%) and Qwen3 (26%) have low auth_scope, so their spec-layer advantage disappears.\n- **Framing decision**: C3 is NOT \"spec-layer nearly twice as dangerous\" (that was 2-model artifact). The correct framing is: \"Specification-layer types are significantly more dangerous on average (Δ=6.08pp, p=0.017), but this aggregate masks a model × type interaction where the gap varies from +14pp (GPT-5.4) to -1pp (Qwen3). The interaction, not the main effect, is the theoretically interesting finding (see C4).\"\n- **Info delta as mediator** [MF-2]: Token delta significant in 5-model logistic regression (coef=0.022, z=3.49, p=0.0005). Spec-layer clauses require more tokens to disambiguate (auth_scope 36.1, incomp 34.6 vs coref 7.8 tokens). Info delta partially mediates but doesn't eliminate the condition effect (condition_amb coef=2.278 dominates).\n- **Layer overlap persists**: CP (36.8%, spec) < scopal (39.4%, ling). Mid-tier cluster spans both layers. Layer effect is driven by extremes: incompleteness (53.6%, spec) vs coreferential (31.6%, ling).\n- **ICC convergent evidence** [plan_006]: Per-type ICC mirrors layer hierarchy — Ling-layer ICC all excellent (scopal 0.989, lexical 0.981, coref 0.976), Spec-layer ICC all good (auth 0.857, CP 0.856, incomp 0.807). Spec-layer less reproducible — agents guess differently each run when external disambiguation channels are absent.\n- **CL connection**: Parallels pragmatics vs semantics distinction. Good-enough processing (Ferreira et al. 2002). Disambiguation channel framework: linguistic ambiguity has partial external resolution; specification ambiguity forces guessing.\n\n### C4: Model × Type Interaction (UPGRADED — star finding, 5 models complete)\n**[2026-05-20 DEFINITIVE, 5/5 models]** Models show significantly different vulnerability profiles despite universal binary effect. The interaction is the paper's most novel finding.\n- **Model main effect**: Overall χ²=31.02, p=3.0×10^-6, V=0.102. Ambiguous-only: χ²=24.01, p=7.9×10^-5.\n  - Vulnerability ranking: Claude 30.3% < GPT-5.4 41.0% ≈ GPT-4.1 40.7% < Qwen3 43.1% < DeepSeek 49.7%\n  - Bootstrap CI confirms: Claude significantly lower than all others; DeepSeek significantly higher than GPT models.\n- **Model × Type interaction matrix** (ambiguous condition, violation rates):\n  ```\n  Type                  GPT-5.4  GPT-4.1  Claude  Qwen3   DeepSeek\n  authorization_scope     64%     46%      12%     26%     60%\n  conditional_precedence  34%     36%      36%     40%     38%\n  incompleteness          46%     58%      48%     62%     54%\n  lexical                 42%     34%      32%     52%     54%\n  coreferential           18%     32%      22%     42%     44%\n  scopal                  42%     38%      32%     37%     48%\n  ```\n- **Key interaction patterns**:\n  - **auth_scope**: 52pp range (Claude 12% → GPT-5.4 64%). The MODEL-DIFFERENTIATING type. Claude's RLHF appears to specifically train authorization boundary awareness.\n  - **coreferential**: 26pp range (GPT-5.4 18% → DeepSeek 44%). Second most model-dependent. Open-source models struggle more with referential ambiguity.\n  - **incompleteness**: Universally high (46-62%, 16pp range). ALL models fail on missing information — safety training doesn't help when information literally isn't there.\n  - **CP**: Most model-invariant (34-40%, 6pp range). Explicit rule conflicts treated similarly by all architectures.\n- **Per-model type χ²** (which models show type-specific vulnerability patterns):\n  - GPT-5.4: χ²=23.44, p=0.0003, V=0.28 — strongest type differentiation (very high auth_scope, very low coref)\n  - Claude: χ²=17.87, p=0.003, V=0.24 — strong differentiation (very low auth_scope, moderate others)\n  - Qwen3: χ²=15.89, p=0.007, V=0.23 — moderate differentiation (high incomp+lex, low auth_scope)\n  - GPT-4.1: χ²=9.89, p=0.078, V=0.18 — borderline\n  - DeepSeek: χ²=6.31, p=0.277, V=0.14 — NOT significant (uniformly high across all types)\n- **Fleiss κ = 0.384 (fair agreement)**: Models only moderately agree on which specific clauses trigger violations. The binary effect is universal, but the WHICH-clauses question is model-dependent.\n- **Theoretical implications**: (1) Safety training differentially addresses specific ambiguity types — Claude's auth_scope robustness suggests authorization boundary handling was explicitly or implicitly trained. (2) Incompleteness is a \"safety training blind spot\" — all models fail equally. (3) DeepSeek's uniform vulnerability suggests less type-specific safety training.\n- **Framing**: C4 from \"models agree\" → \"Models show systematically different vulnerability profiles. The binary effect is universal, but HOW models fail depends on the intersection of ambiguity type and safety training approach. auth_scope is the canary type — most sensitive to safety training quality.\"\n- **Evidence from plan_005**: 2-model failure modes consistent (5/6 dominant modes identical). 5-model failure mode analysis pending.\n- **Layer effect moderation**: C3's aggregate layer gap (6.08pp) is driven by GPT models' high auth_scope rates. The layer effect is itself model-dependent (GPT +12-14pp, Claude +3pp, Qwen3 reversed), making the MODEL × TYPE interaction more fundamental than the LAYER main effect.\n\n### C5: Error Analysis (CONFIRMED — EMNLP core)\nDifferent ambiguity types produce qualitatively different failure modes with type-specific signatures. plan_005 (123+122 violation traces across gpt-5.4 and gpt-4.1, confidence=0.94).\n- **Evidence**: plan_005 complete (gpt-5.4: 123 traces, gpt-4.1: 122 traces). Key findings:\n  - **Type-specific failure signatures**: auth_scope → unauthorized_escalation (72%/83%); incompleteness → assumption_based_action (61%/66%); scopal → scope_misapplication (76%/74%); lexical → assumption_based_action (71%/53%); CP → scope_misapplication (41%/28%) + arbitrary_rule_selection (29%/28%); coreferential → scope_misapplication (44%) / assumption_based_action (38%)\n  - **Cross-model consistency**: 5/6 types share the same dominant failure mode across gpt-5.4 and gpt-4.1. Only coreferential diverges (scope_misapplication vs assumption_based_action). Overall mode distribution nearly identical: both ~33% assumption_based_action, ~26-32% unauthorized_escalation, ~25-28% scope_misapplication. Failure mode profiles are type-specific, not model-specific.\n  - **Layer mechanism**: Ling-layer dominated by scope_misapplication (39% ling avg vs 15% spec avg) = \"misparse\"; Spec-layer dominated by unauthorized_escalation + assumption_based_action = \"active guessing\" → explains higher violation rates\n  - **Ambiguity Blindness empirically confirmed**: awareness rate gpt-5.4=4.1%, gpt-4.1=10.7% (both very low); surface_adoption >88% all types both models; escalate_to_user <1%. Nuance: gpt-4.1 (mid-tier) shows 2.6× higher awareness than gpt-5.4 (frontier) — awareness may inversely correlate with action-orientation (frontier models more \"confident,\" act without hesitation)\n  - **Cross-domain consistency**: airline vs retail failure mode profiles Δ < 13pp (unauthorized_escalation shows largest domain effect: retail 38.6% vs airline 26.1%)\n  - **Coreferential boundary**: conservative_refusal 6-11% (vs avg 2-3%) partially explains low violation rate — agents sometimes pause rather than guess. N=25 combined traces show no single dominant failure mode (flat distribution: scope_misapplication 32%, assumption_based_action 28%, unauthorized_escalation 16%) — contrasts with other types' sharp signatures, reflecting the diversity of resolution strategies for referential ambiguity\n  - **Lexical surprise**: 53-71% assumption_based_action — agents treat word ambiguity as information gap, not misparse\n- **Automated inter-coder agreement** [MF-5, Reviewer-validated]: Cross-coding 60 traces (gpt-5.4 vs gpt-4.1 as independent coders). 4-category merged: 80% agreement, Cohen's κ=0.594 (moderate). κ deflated by kappa paradox — lexical 91.7% agreement → κ=0.0 (11/12 same label, chance agreement also high), scopal 100% agreement → κ undefined. True disagreement concentrated at unauthorized_escalation ↔ inappropriate_action boundary in auth_scope (κ=0.054) and incompleteness (κ=0.233).\n  - **Reporting strategy** [Reviewer recommendation]: (1) Compute Gwet's AC1 as primary metric (designed for kappa paradox, expected 0.70-0.75); (2) Report 80% agreement + 5/6 dominant mode consistency as headline validity evidence; (3) Report κ honestly with kappa paradox caveat; (4) Auth_scope failure mode: soften to \"dominated by boundary-exceeding behaviors (unauthorized_escalation or inappropriate_action, >90%)\" instead of specific percentages; (5) Fine-grained 6-type as appendix with \"automated coding\" caveat.\n  - **C5 safety**: Ambiguity Blindness (<5-11%), surface_adoption (>88%), layer mechanism (ling→scope vs spec→escalation) all robust. Fine-grained per-type percentages unreliable at κ=0.594. Plan_009 human anchor (20-30 failure mode traces) would upgrade from \"moderate automated\" to validated.\n- **EMNLP value**: Highest. Provides the linguistic WHY behind the quantitative WHAT. Cross-model + cross-domain consistency elevates from anecdotal to systematic finding. \"Ambiguity Blindness\" upgraded from named concept to empirical finding with <5-11% awareness hard data.\n\n## Narrative Structure (CL-first for EMNLP)\n\n### Intro Logic Chain\n1. Agent policies are written in NL → contain ambiguity (established)\n2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact\n3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.\n4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter? Does it depend on the model?\n5. **This paper**: First causal, type-granularity, cross-model study. Matched-pair design + perturbation control isolates ambiguity effect. 5 models × 6 types.\n6. **Core findings**: (a) All ambiguity is nocuous (+34.0pp, 5 models), (b) type DOES predict severity — 3-tier hierarchy with incompleteness most dangerous, (c) models show dramatically different vulnerability profiles — auth_scope varies 52pp across models, suggesting safety training differentially addresses ambiguity types, (d) while incompleteness remains universally dangerous, a \"safety training blind spot.\"\n\n### Section Map\n- **§1 Intro**: Gap + contributions (causal map + differential nocuity + model×type interaction)\n- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R\n- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R\n- **§4 Method**: Matched-pair causal design, τ²-bench, 5 models (3 proprietary + 2 open-source), clause generation, perturbation control, cross-judge evaluation\n- **§5 Results**: C1 (binary, +34.0pp, 5 models) → C2 (type hierarchy, 3-tier) → C3 (layer effect, modest but significant) → C4 (model×type interaction — star finding)\n- **§6 Analysis**: C5 error analysis — qualitative failure modes per type. Ambiguity Blindness. Model-specific patterns.\n- **§7 Discussion**: Differential nocuity theory. Safety training selectivity. Disambiguation channel framework. Limitations (2 domains, synthetic injection, LLM-as-judge).\n- **§8 Conclusion**: All policy ambiguity is nocuous, but type AND model jointly determine risk level. Both type-aware auditing and model-specific risk assessment recommended.\n\n## Anticipated Reviewer Concerns\n\n### RC1: \"Type effect could be artifact of taxonomy granularity\"\n**Response**: (a) Layer effect (Spec vs Ling ~19pp gap) is robust — holds even if individual types are reclassified. (b) 2-layer structure grounded in Li et al. + Massey et al. (c) Coreferential's low rate has structural explanation (disambiguation channels), not just noise. (d) TOST confirms types are NOT equivalent (0/15 pairs at ±10pp).\n\n### RC2: \"Taxonomy is ad hoc / why these 6 types\"\n**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).\n\n### RC3: \"Only API models, no open-source\"\n**Response**: ✅ RESOLVED. 5-model coverage spans: frontier proprietary (gpt-5.4, claude-sonnet-4-6) + mid-tier proprietary (gpt-4.1) + open-source MoE (qwen3-235b) + open-source dense (deepseek-v3). Three providers (OpenAI, Anthropic, Chinese open-source). Two architecture types (dense, MoE). Model×type interaction (C4) reveals rich cross-model patterns.\n**Note [Reviewer 2026-05-20]**: Cross-judge asymmetry — Claude judged by gpt-5.4, gpt-5.4 judged by gpt-4.1. Must disclose in Method. plan_009 judge calibration measures this bias.\n\n### RC4: \"Synthetic ambiguity injection lacks ecological validity\"\n**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.\n\n### RC5: \"τ²-bench limited to retail/airline\"\n**Response**: ✅ ADDRESSED (plan_017). Cross-benchmark replication on SOPBench (Li et al., 2025) — Healthcare + Bank domains, 100 clause pairs × 5 models = 1,000 episodes with rule-based verifier. If C1 replicates, paper moves from \"customer service finding\" to \"cross-domain finding\" spanning 4 domains (retail, airline, healthcare, banking). Result in Appendix with main-text summary. τ²-bench remains primary; SOPBench provides independent cross-domain confirmation.\n\n### RC6: \"Binary effect is obvious — of course ambiguity causes errors\"\n**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOES predict severity — specification-layer ambiguities are nearly twice as dangerous, connecting to disambiguation channel availability.\n\n### RC7: \"Incompleteness matched-pair confound (information asymmetry)\"\n**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.\n\n### RC8: \"RC attachment in coreferential overlaps with scopal / structural ambiguity\"\n**Response**: (a) Our scopal category is explicitly scoped to quantifier/negation/modal scope interactions, not syntactic attachment. (b) RC attachment in policies manifests as *referential* confusion (which entity does the clause modify?) not *scope* confusion (which operator takes wide scope?). (c) Li et al. 2024 distinguishes syntactic ambiguity (including RC attachment) from scopal ambiguity — our grouping follows their treatment that RC attachment is closer to coreferential than scopal in terms of downstream interpretation. (d) Empirically, if the distinction were problematic, coreferential and scopal would show identical violation patterns — the error analysis (C5) can test whether their failure modes differ.\n\n### RC9: \"authorization_scope is just a subtype of incompleteness\"\n**Response**: (a) Incompleteness = missing conditions/exceptions/boundaries (structural absence). Authorization scope = ambiguous permission/role boundaries that ARE stated but vague (e.g., \"authorized personnel\" without specifying which functions). (b) The disambiguation pattern differs: incompleteness adds new conditions; auth_scope clarifies existing permission boundaries. (c) Empirically testable: if they were the same, their violation patterns and failure modes (C5) would be indistinguishable. (d) Report disambiguation length ratio per type as control variable in §4 Method.\n\n### RC10: \"API sampling noise undermines reliability\"\n**Response**: ✅ RESOLVED. plan_006 ICC=0.919 [0.892, 0.940] (excellent). (a) Per-clause violation rates highly reproducible across 3 independent replicates. (b) Binary ICC=0.847 (good). (c) Both models show near-identical ICC (gpt-5.4: 0.921, gpt-4.1: 0.918). (d) Bootstrap CI + ICC double evidence. (e) Previously identified ±8pp noise is within expected variance given the ICC confidence intervals.\n\n### RC11: \"Prompt sensitivity confound\" [Dream A9 — best tier \"strongest point\"]\n**Concern**: The +35-42pp effect is attributed entirely to ambiguity, but without a control condition using non-ambiguity perturbations (synonym substitution, clause reordering), the paper cannot cleanly distinguish ambiguity-specific harm from general prompt brittleness.\n**Response**: ✅ RESOLVED. plan_010 perturbation control (120 episodes): Δ_perturb=3.33pp (CI contains 0) vs ambiguity Δ=36.5pp. Non-ambiguity surface changes cause zero meaningful effect. This is the strongest causal evidence in the agent safety literature.\n\n## Concept Naming (distill insight: 命名即贡献)\n\nCore phenomenon: **\"Differential Nocuity\"** — all policy ambiguity types are nocuous for LLM agents (+34.0pp, all 5 models), but vulnerability varies by BOTH type and model. Incompleteness is universally dangerous (46-62%), while auth_scope vulnerability depends dramatically on safety training (12% Claude to 64% GPT-5.4). Unlike human RE where organizational context renders most ambiguity innocuous, agents lack disambiguation channels AND their safety training creates type-specific blind spots.\n\nSecondary phenomenon: **\"Ambiguity Blindness\"** — agents process grammatically fluent ambiguous clauses without meta-cognitive awareness of the ambiguity, adopting surface interpretations. Contrasts with explicit rule conflicts where agents show awareness and choose conservatively.\n\nTertiary phenomenon: **\"Disambiguation Channel Framework\"** [renamed from \"Hypothesis\" per Dream review SF-5] — the layer hierarchy reflects availability of external disambiguation: linguistic ambiguity (coreferential, lexical) can sometimes be resolved by tool responses, user context, or world knowledge; specification ambiguity (auth_scope, incompleteness) has no external resolution channel, forcing agents to guess. This is an explanatory framework supported by observational evidence (ICC pattern, failure mode distribution, coreferential boundary case), not a tested causal hypothesis. Future Work: manipulation experiment (inject spec-layer disambiguation info into tool responses, test if gap shrinks).\n\nQuaternary phenomenon: **\"Systematic Nocuity\"** [per Dream review SF-7] — B&K framework distinguishes nocuous (divergent interpretations) from innocuous (convergent). Our data reveals a third type: all models converge on the same WRONG interpretation (27% of ambiguous episodes). This is more dangerous than divergent nocuity — it's invisible in inter-model agreement metrics and appears \"correct\" until compared against ground truth. Proposed as B&K extension in Discussion.\n\n## Opening Hook Strategy (distill insight: 具体案例, 不要 \"Recently...\")\n\nOpen with a concrete τ²-bench failure: e.g., a customer returns a customized item within the return window; the agent grants a full refund + free return shipping because the policy says \"items may be returned within 30 days\" (scopal: \"items\" scopes over all categories including custom). The unambiguous version specifies \"standard items only\" — agent correctly refuses. One word of ambiguity → $200 unauthorized refund.\n\n## Narrative Type: 突破局限型 (distill pattern, 5/8 papers)\n\n\"DRIP-R classifies 5 ambiguity types and shows models disagree on interpretation → but does not measure whether this disagreement leads to safety violations. We close this gap — and find the answer is surprising: not all types are equal, specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones.\"\n\n## Benchmark Comparison Table (distill insight: 必有 feature matrix)\n\n| Feature | DRIP-R | PhantomPolicy | PolicyBank | AgentPex | **Ours** |\n|---------|--------|---------------|------------|----------|----------|\n| Ambiguity taxonomy | 5 RE types | — | 3 gap types | — | **6 types (2-layer)** |\n| Causal design | — | — | — | — | **matched pairs** |\n| Safety violation metric | — | binary | — | procedural | **3-tier severity** |\n| Cross-type comparison | descriptive | — | — | — | **statistical (χ² + V)** |\n| Models tested | 6 API | 4 API | 2 API | 2 API | **3 API + 2 open-source** |\n| Domain | retail | mixed | retail | telecom/retail/airline | **retail + airline** |\n\n## Contribution Positioning (for EMNLP) [revised 2026-05-20 with 5-model data]\n\n1. **Causal quantification of ambiguity's safety impact**: First matched-pair causal study of policy ambiguity → agent safety violations. Binary effect +34.0pp (OR=15.1, p<0.0001) across 5 architecturally diverse models and 6 ambiguity types. Perturbation control (Δ_perturb=3.33pp) confirms ambiguity-specific causation. Strongest causal evidence in the agent safety literature.\n2. **Differential Nocuity framework + Model × Type Interaction**: Not all ambiguity is equally dangerous, and not all models are equally vulnerable. 3-tier type hierarchy (incompleteness >> mid cluster >> coreferential). Model × type interaction reveals 52pp range in auth_scope vulnerability (Claude 12% → GPT-5.4 64%), while incompleteness remains universally dangerous (46-62%). Safety training differentially mitigates specific ambiguity types. Connects Berry & Kamsties nocuous ambiguity theory to modern safety alignment.\n3. **Type-specific failure mode taxonomy + Ambiguity Blindness**: 245 traces across 2 models and 2 domains reveal type-diagnostic failure signatures: spec-layer → guess-and-act (unauthorized_escalation, assumption_based_action); ling-layer → misparse-and-apply (scope_misapplication). Agents show <5-11% awareness of ambiguity (\"Ambiguity Blindness\"), with >88% surface adoption and <1% user escalation. Practical implication: ambiguity detection must be externalized.\n\nNOTE: C3 (layer effect, Δ=6.08pp) is a component finding supporting contribution #2. The MODEL × TYPE interaction (C4) is now MORE central than the layer main effect. \"Disambiguation channel\" is an explanatory framework (not hypothesis — per SF-5). DeBERTa classifier, if included, is a preliminary PoC appendix, not a contribution.\n\n## Required Reference Expansion [Dream A2 + MF-4 RE literature gap]\n\nCurrent plan has thin references. Must add (≥25 total in final paper):\n- **Nocuous ambiguity detection (CRITICAL — MF-4)**: Chantree, Nuseibeh, de Roeck & Willis (2006, ASE) — first computational nocuous ambiguity detection; Chantree et al. (2008, RLAC) — expanded. Direct lineage to our DeBERTa classifier.\n- **Cross-domain RE ambiguity**: Ferrari, Spagnolo & Gnesi (2017-2019, ASE) — NLP-based cross-domain ambiguity detection. NLP4RE community work.\n- **Good-enough processing**: Ferreira, Bailey & Ferraro (2002); Ferreira & Patson (2007)\n- **LLM garden-path (SF-6)**: Li et al. (2024) — incremental comprehension of garden-path sentences by LLMs. Directly relevant to how LLMs process ambiguity.\n- **Anaphoric ambiguity (SF-6)**: Poesio & Artstein (2005, 2008) — annotation of anaphoric ambiguity. Poesio (2004) \"Ambiguity\" encyclopedia entry.\n- **Surprisal/expectation-based**: Levy (2008); Hale (2001)\n- **Instruction-following robustness**: Zhou et al. (IFEval, 2023); Qin et al. (ToolBench, 2024)\n- **Prompt sensitivity**: Sclar et al. (2024); Lu et al. (2022)\n- **Broader agent safety**: R-Judge, ToolEmu, InjecAgent\n- **Formal semantics of vagueness**: Lassiter & Goodman (2017)\n- **Garden-path**: Frazier & Rayner (1982)\n- **Ambiguity detection**: Willis et al. (2008); Ezzini et al. (TAPHSIR, 2022)\n- **Year verification needed**: Massey et al. — §1 引用 2013 vs 后文 2014, 需确认正确年份\n\n## Code/Data Release Plan [Dream A6 — three-tier consistent]\n\nMust commit to releasing:\n1. All 300 clause pairs (ambiguous + unambiguous variants) with type labels\n2. Evaluation scripts (τ²-bench integration, cross-judge pipeline)\n3. Statistical analysis code (all tests, bootstrap CI computation)\n4. Agent trace samples (anonymized) for reproducibility of C5\n\n## Figure Plan [Dream A12]\n\nMinimum figures for paper (zero-figure paper flagged in dream):\n1. **Figure 1**: System architecture / experimental pipeline overview (§4 Method)\n2. **Figure 2**: Forest plot — per-type binary effect sizes with 95% CI (§5 C1)\n3. **Figure 3**: Model × Type heatmap — violation rates across 4 models × 6 types (§5 C4)\n4. **Figure 4**: Visibility mechanism — CP vs scopal violation rates + trace evidence (§5 C3)\n5. **Figure 5**: Failure mode × type stacked bar/Sankey — per-type failure mode distribution (§6 C5)\n6. **Figure 6**: Cross-model failure mode consistency — side-by-side gpt-5.4 vs gpt-4.1 per-type distributions showing 5/6 convergence (§6 C5, supports C4)\n7. **Figure 7**: Annotated trace pair — CP (conflict detection) vs scopal (surface adoption) (§6 C5)\n\n## Berry & Kamsties Operationalization Note [Dream best Q5]\n\nBerry & Kamsties define nocuity as inter-reader divergence. Our design measures agent-vs-intent deviation. Full study should additionally test whether different models adopt different readings of the same ambiguous clause (true inter-model nocuity). If 4 models produce 4 different interpretations of the same clause → true nocuity. If all 4 adopt the same wrong interpretation → systematic bias, still nocuous but for different reason. Report inter-model agreement on ambiguous clauses as supplementary analysis.\n\n## Contingency Framing [RESOLVED — Scenario C occurred]\n\n> plan_002 结果: Scenario C 发生（omnibus p=0.0001, 所有类型 nocuous 但 severity 有显著差异）。\n> Framing 已 pivot 到 \"Differential Nocuity\" + \"Layer Hierarchy\" (D020)。本节仅保留历史记录。\n\n## Claude Baseline — RESOLVED [2026-05-20]\n\n✅ Claude works via OpenRouter proxy (47.94.22.126/v1) with provider prefix `anthropic/claude-sonnet-4-6`. 600 episodes complete (plan_002c). Claude shows lowest overall vulnerability (30.3%) and remarkable auth_scope robustness (12% vs GPT-5.4 64%).\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: full_study_clause_generation\n  claim: C1, C2, C3\n  description: 'Generate remaining clauses for full study: coreferential (50 new),\n    authorization_scope (50 new), lexical (+20 to reach 50), incompleteness (+20 to\n    reach 50). Total 140 new clauses. Validate all 300 clauses (50/type × 6 types)\n    for completeness and cross-type balance. Mix CP format per Reviewer suggestion\n    (labeled + unlabeled).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n- id: plan_001b\n  name: new_type_mini_pilot\n  claim: C1 (validation)\n  description: 'Mini-pilot for coreferential + authorization_scope (never tested):\n    5 clauses/type × 2 conditions × 1 model (gpt-5.4) = 20 episodes. Verify: (a) ambiguous\n    triggers violations (b) unambiguous control < 15%. If systematic issues found,\n    fix clause design before full study. API cost negligible (~$2). Per Reviewer warning\n    on untested types.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_002\n  name: full_study_api\n  claim: C1, C2, C3, C4, C5\n  description: 'Run 300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6)\n    = 1,800 episodes on τ²-bench. Cross-judge evaluation. Output: episodes.jsonl +\n    judgments.jsonl. No GPU needed. Claude via OpenRouter proxy (base_url=http://47.94.22.126/v1).\n    [2026-05-20] Claude added per distill gap (4/8 papers use Claude baseline).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_001b\n  - plan_010\n  status: planned\n- id: plan_003\n  name: full_study_opensource\n  claim: C1, C2, C3, C4, C5\n  description: 'Run 300 clauses × 2 conditions × 2 open-source models via OpenRouter\n    API: qwen/qwen3-235b-a22b (235B MoE, Alibaba) + deepseek/deepseek-chat-v3-0324\n    (DeepSeek) = 1,200 episodes on τ²-bench. Cross-judge uses API models. Can run\n    in parallel with plan_002. No GPU needed. [2026-05-20] Pivoted from local GPU\n    → API: OpenRouter proxy confirmed to support Qwen3 and DeepSeek models. Eliminates\n    48h GPU requirement. Provider prefix required (e.g. qwen/qwen3-235b-a22b, not\n    qwen3-235b-a22b).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_004\n  name: full_study_analysis\n  claim: C1, C2, C3, C4\n  description: 'Statistical analysis of full study data (3,000 episodes): (a) Binary\n    effect per type with bootstrap CI (C1) (b) Omnibus χ² + pairwise across 6 types\n    (C2) (c) Visibility comparison: CP vs scopal rates (C3) (d) Model × type interaction:\n    5×6 contingency + logistic regression (C4) Report effect sizes + CI for all comparisons\n    per Reviewer suggestion. [Dream A3] Power analysis: report MDE for C2 (given N=250/type\n    pooled) and C3 (given N=250 per type). If V < 0.20 but MDE > observed V, discuss\n    underpowered possibility. [Dream A4] TOST equivalence test with both ±15pp and\n    ±10pp margins. Justify margin choice explicitly. [Dream A10] Report per-type information\n    delta (token count difference between ambiguous and unambiguous variants) as control\n    variable. [Dream B&K] Inter-model agreement on ambiguous clauses: do 5 models\n    adopt same or different interpretations? (supplementary analysis)\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_005\n  name: error_analysis\n  claim: C5\n  description: \"Qualitative analysis of agent traces from full study: (a) Sample 50\\\n    \\ violation traces per type (300 total) (b) Classify failure modes (scope misapplication,\\\n    \\ conservative refusal,\\n    assumption-based action, arbitrary rule selection,\\\n    \\ etc.)\\n(c) Cross-type failure mode distribution (d) Visibility mechanism: compare\\\n    \\ CP traces (explicit conflict detection\\n    behavior) vs scopal traces (surface\\\n    \\ scope adoption without awareness)\\n(e) Model-specific failure patterns (connect\\\n    \\ to C4)\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_006\n  name: reliability_test\n  claim: C1, C2\n  description: 'Test-retest reliability: select 30 representative clauses (5/type),\n    run 3 independent replicates × 2 conditions × 2 API models (gpt-5.4, gpt-4.1)\n    = 360 episodes. Local models added when plan_003 GPU available. Compute ICC for\n    per-clause violation rates. Addresses Reviewer warning about ±8pp sampling noise\n    (scopal 51.7% → 43.3% across MVP/diag). Bootstrap CI width should be < 10pp for\n    key comparisons. [2026-05-20] API portion: 330/360 episodes complete (28/30 clauses),\n    judgments pending.\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  status: planned\n- id: plan_007\n  name: realism_validation\n  claim: C1 (methodological)\n  description: \"Validate synthetic ambiguity injection realism: (a) Linguistic property\\\n    \\ comparison with DRIP-R natural ambiguities\\n    (sentence length, parse depth,\\\n    \\ Flesch-Kincaid, TTR) + KS tests\\n(b) Optional: discriminator test if DRIP-R\\\n    \\ data accessible Addresses RC4 (ecological validity).\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_009\n  name: judge_calibration\n  claim: C1 (methodological)\n  description: 'LLM-as-judge calibration per distilled research norm (5/8 papers):\n    (a) Sample 100 episodes stratified by type×model×condition (b) Human expert labels\n    (2 annotators, target κ ≥ 0.75) (c) Compute judge precision/recall/F1 against\n    human ground truth (d) Per-severity-tier agreement rates (e) Report in Method\n    section as standard practice per AgentAuditor/DRIP-R [Dream A7] Upgraded P1→P0:\n    Dream best-tier reviewers identified this as \"single most critical missing validation.\"\n    Without it, entire measurement chain from episode to violation label is unvalidated.\n    κ=0.91 measures LLM-LLM agreement, not accuracy.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  name: perturbation_control\n  claim: C1 (causal validity)\n  description: '[Dream A9] Non-ambiguity perturbation control arm to distinguish ambiguity-specific\n    harm from general prompt brittleness. Generate 30 clause pairs with non-ambiguity\n    perturbations: (a) 15 synonym substitution pairs (replace key terms with synonyms)\n    (b) 15 clause reordering pairs (reorder conditions without changing meaning) Run\n    30 × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6) = 180 episodes.\n    Key metric: Δ_net = Δ_ambiguity - Δ_perturb (net ambiguity-specific effect). [Reviewer升级]\n    必须在 plan_002/003 full study 之前完成—— 如果 perturbation Δpp ≈ ambiguity Δpp，2,400 episodes\n    全部无效。 低成本验证（30 pairs + 120 episodes API）优先于高成本投入。 [判定标准 — 5 档]: PASS: Δ_perturb\n    < 5pp (CI含0), ratio < 0.15 → C1 因果 claim 最强形式 PASS+caveat: 5-10pp, ratio 0.15-0.30\n    → 报告 perturbation baseline, C1 写 net effect CONDITIONAL: 10-15pp, ratio 0.30-0.45\n    → 需 Δ_net > 20pp 且显著才可发表 WARNING: 15-20pp, ratio 0.45-0.60 → C1 改为 \"additional\n    violations beyond sensitivity\" FAIL: > 20pp, ratio > 0.60 → 无法声称 ambiguity-specific,\n    需根本重新设计 [Power 注意]: N=120 对 10pp 差异 power ≈ 30%. 用 CI 宽度判定, 非 p-value. 若 CI 过宽(>15pp\n    width), 追加 60 episodes 压窄至 <10pp width. 输出标准化 verdict 文件: perturbation_Δpp, ambiguity_Δpp,\n    net_Δpp, CI, ratio, verdict.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_017\n  name: sopbench_cross_benchmark\n  claim: C1 (generalizability), C2 (partial)\n  description: 'Cross-benchmark C1 replication on SOPBench (Li et al., 2025). 7 domains\n    (Bank, DMV, Healthcare, Hotel, Library, University, Online Market) all different\n    from τ²-bench (retail + airline). Select 2 domains (Healthcare + Bank) for maximum\n    domain diversity. Construct 100 clause pairs (50/domain) covering 3-4 ambiguity\n    types (incompleteness, auth_scope, lexical, conditional_precedence) from SOPBench''s\n    NL SOP constraints. Run 100 pairs × 2 conditions × 5 models = 1,000 episodes.\n    SOPBench has rule-based verifier — no LLM judge needed. Key metrics: (a) Does\n    C1 binary effect replicate? (b) Is incompleteness still highest-risk type? (c)\n    Cross-benchmark effect size correlation. Addresses SF-8 (single benchmark external\n    validity). Result goes in Appendix with 1-sentence summary in main text. [2026-05-22]\n    Approved by user. Estimated 1 day including clause construction.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n- id: plan_008\n  name: classifier_poc\n  claim: practical contribution\n  description: 'Binary ambiguity detector PoC: fine-tune DeBERTa-v3-large on annotated\n    clause pairs (ambiguous/unambiguous labels). Eval on held-out set. Demonstrates\n    practical applicability of findings. Phase 3 from IDEA_BRIEF, scoped to PoC for\n    EMNLP.\n\n    '\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: diag_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_002\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_006\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_009\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cross_judge_kappa_weighted: 0.685\n    cross_judge_exact_agreement: 0.76\n    cross_judge_binary_kappa: 0.74\n    human_llm_pooled_kappa_weighted: 0.807\n    human_inter_annotator_kappa_weighted: 0.762\n    n_episodes: 100\n- exp_id: plan_002c\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_003a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_003b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_004\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_010\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_violations_coded: 614\n    types_unanimous_dominant_fm: 3/6\n    types_majority_dominant_fm: 6/6\n    inter_coder_kappa: 0.5173\n    percent_agreement: 0.656\n    disambiguation_awareness_overall: 0.046\n    elapsed_seconds: 98.5\n- exp_id: plan_011\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_delta_pp: -6.6\n    overall_baseline: 0.41\n    overall_mitigated: 0.343\n    auth_scope_delta_pp: -18\n    incompleteness_delta_pp: -3.4\n    lexical_delta_pp: -8.9\n    cond_prec_delta_pp: -8.1\n    scopal_delta_pp: -4.3\n    best_model_gpt41_delta_pp: -11.1\n    worst_model_deepseek_delta_pp: -2.5\n    total_mitigated_episodes: 1256\n    total_baseline_episodes: 1499\n    elapsed_seconds: 2954\n- exp_id: plan_012\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1: 0.6322\n    binary_f1: 0.8055\n    binary_fpr: 0.044\n    best_type_f1:\n      conditional_precedence: 0.94\n    worst_type_f1:\n      incompleteness: 0.34\n    per_type_f1:\n      conditional_precedence: 0.94\n      scopal: 0.75\n      coreferential: 0.7\n      authorization_scope: 0.58\n      lexical: 0.39\n      incompleteness: 0.34\n    total_clauses: 500\n    folds: 5\n- exp_id: plan_013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gemini_2.5_flash:\n      amb_rate: 0.376\n      unamb_rate: 0.04\n      delta_pp: 33.6\n      or: 14.46\n      p_value: 4.0e-22\n      c1_replicates: true\n      c2_rank_corr: 0.6\n      c2_rank_p: 0.285\n      type_ranking:\n      - lexical\n      - incompleteness\n      - scopal\n      - cond_prec\n      - auth_scope\n    llama_4_scout:\n      amb_rate: 0.376\n      unamb_rate: 0.176\n      delta_pp: 20\n      or: 2.82\n      p_value: 7.7e-07\n      c1_replicates: true\n      c2_rank_corr: 0.9\n      c2_rank_p: 0.037\n      type_ranking:\n      - incompleteness\n      - auth_scope\n      - lexical\n      - scopal\n      - cond_prec\n    summary:\n      c1_replicated: 7/7\n      c2_replicated: 2/2 positive (LLaMA ρ=0.90 p=0.037, Gemini ρ=0.60 p=0.285)\n      incompleteness_universal: 7/7 (≥46%)\n      total_episodes: 1000\n    bugfix: reference_rank corrected from arbitrary order to main-study pooled descending;\n      OR inverted\n- exp_id: plan_014\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_episodes: 300\n    delta_perturb_pp: -0.67\n    ci_95_bootstrap:\n    - -8\n    - 6.67\n    ci_upper_bound: 6.67\n    ci_width: 14.67\n    mcnemar_p: 1\n    verdict: PASS\n    plan_010_ci_upper: 13.33\n    ci_upper_reduction: 6.66\n- exp_id: plan_015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pooled_escalation_rate: 0.692\n    pooled_restriction_rate: 0\n    binomial_p: 5.5e-05\n    models_majority_escalation: 4/5\n    n_total: 104\n    n_escalation: 72\n- exp_id: plan_016\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    generic_awareness_overall_delta_pp: 1.33\n    type_specific_auth_scope_delta_pp: -12\n    type_specific_auth_scope_p: 0.07\n    type_specific_incompleteness_delta_pp: 14\n    type_specific_incompleteness_p: 0.118\n    type_specific_lexical_delta_pp: -2\n    type_specific_lexical_p: 1\n    total_new_episodes: 450\n    total_judge_calls: 450\n    model: gpt-5.4\n    all_mcnemar_p_gt_005: true\n\n# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）\n\n```yaml\ntiers:\n  best:\n    meaning: \"...\"\n    key_assumptions: [...]\n    number_ranges: {metric_a: [low, high], metric_b: [...]}\n    narrative_direction: \"...\"\n  median:\n    meaning: \"...\"\n    ...\n  worst:\n    meaning: \"...\"\n    ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-22T11:16:52.511Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T11:16:52.511Z",
  "sessionId": "942a8489-57e5-46b7-9ba6-6f129bdc29b2"
}
```

---

## Round 1

10 recorded events

### User

_source line 3 · 2026-05-22T11:16:52.531Z_

你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。

你需要同时定义 best / median / worst 三档：
1. 每档的核心假设（哪些假设成立/不成立）
2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）
3. 每档的论文叙事方向——
   - best: 原始 framing 完全成立，claims 无需调整
   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验
   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）

三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性
自行判断。但必须确保三档之间的数字和叙事逻辑一致。

# Project context
project: policy_ambiguity_safety
venue: emnlp-2026
focus: Cross-benchmark replication on SOPBench (Healthcare + Bank domains) added to plan. Assess: (1) Does SOPBench replication meaningfully strengthen the paper vs current single-benchmark version? (2) What's the realistic best/median/worst score with vs without SOPBench? (3) Are there any risks (e.g., effect doesn't replicate, rule-based verifier incompatibility)? Round 13 claim calibration already complete (22× removed, margin conditions added, judge annotations, confound anchors).

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
**Response**: ✅ ADDRESSED (plan_017). Cross-benchmark replication on SOPBench (Li et al., 2025) — Healthcare + Bank domains, 100 clause pairs × 5 models = 1,000 episodes with rule-based verifier. If C1 replicates, paper moves from "customer service finding" to "cross-domain finding" spanning 4 domains (retail, airline, healthcare, banking). Result in Appendix with main-text summary. τ²-bench remains primary; SOPBench provides independent cross-domain confirmation.

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
- id: plan_017
  name: sopbench_cross_benchmark
  claim: C1 (generalizability), C2 (partial)
  description: 'Cross-benchmark C1 replication on SOPBench (Li et al., 2025). 7 domains
    (Bank, DMV, Healthcare, Hotel, Library, University, Online Market) all different
    from τ²-bench (retail + airline). Select 2 domains (Healthcare + Bank) for maximum
    domain diversity. Construct 100 clause pairs (50/domain) covering 3-4 ambiguity
    types (incompleteness, auth_scope, lexical, conditional_precedence) from SOPBench''s
    NL SOP constraints. Run 100 pairs × 2 conditions × 5 models = 1,000 episodes.
    SOPBench has rule-based verifier — no LLM judge needed. Key metrics: (a) Does
    C1 binary effect replicate? (b) Is incompleteness still highest-risk type? (c)
    Cross-benchmark effect size correlation. Addresses SF-8 (single benchmark external
    validity). Result goes in Appendix with 1-sentence summary in main text. [2026-05-22]
    Approved by user. Estimated 1 day including clause construction.

    '
  priority: P1
  gpu_budget_hours: 0
  deps: []
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
  status: DONE
  conclusion: success
  metrics:
    cross_judge_kappa_weighted: 0.685
    cross_judge_exact_agreement: 0.76
    cross_judge_binary_kappa: 0.74
    human_llm_pooled_kappa_weighted: 0.807
    human_inter_annotator_kappa_weighted: 0.762
    n_episodes: 100
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
- exp_id: plan_010
  name: ''
  status: DONE
  conclusion: success
  metrics:
    total_violations_coded: 614
    types_unanimous_dominant_fm: 3/6
    types_majority_dominant_fm: 6/6
    inter_coder_kappa: 0.5173
    percent_agreement: 0.656
    disambiguation_awareness_overall: 0.046
    elapsed_seconds: 98.5
- exp_id: plan_011
  name: ''
  status: DONE
  conclusion: success
  metrics:
    overall_delta_pp: -6.6
    overall_baseline: 0.41
    overall_mitigated: 0.343
    auth_scope_delta_pp: -18
    incompleteness_delta_pp: -3.4
    lexical_delta_pp: -8.9
    cond_prec_delta_pp: -8.1
    scopal_delta_pp: -4.3
    best_model_gpt41_delta_pp: -11.1
    worst_model_deepseek_delta_pp: -2.5
    total_mitigated_episodes: 1256
    total_baseline_episodes: 1499
    elapsed_seconds: 2954
- exp_id: plan_012
  name: ''
  status: DONE
  conclusion: success
  metrics:
    macro_f1: 0.6322
    binary_f1: 0.8055
    binary_fpr: 0.044
    best_type_f1:
      conditional_precedence: 0.94
    worst_type_f1:
      incompleteness: 0.34
    per_type_f1:
      conditional_precedence: 0.94
      scopal: 0.75
      coreferential: 0.7
      authorization_scope: 0.58
      lexical: 0.39
      incompleteness: 0.34
    total_clauses: 500
    folds: 5
- exp_id: plan_013
  name: ''
  status: DONE
  conclusion: success
  metrics:
    gemini_2.5_flash:
      amb_rate: 0.376
      unamb_rate: 0.04
      delta_pp: 33.6
      or: 14.46
      p_value: 4.0e-22
      c1_replicates: true
      c2_rank_corr: 0.6
      c2_rank_p: 0.285
      type_ranking:
      - lexical
      - incompleteness
      - scopal
      - cond_prec
      - auth_scope
    llama_4_scout:
      amb_rate: 0.376
      unamb_rate: 0.176
      delta_pp: 20
      or: 2.82
      p_value: 7.7e-07
      c1_replicates: true
      c2_rank_corr: 0.9
      c2_rank_p: 0.037
      type_ranking:
      - incompleteness
      - auth_scope
      - lexical
      - scopal
      - cond_prec
    summary:
      c1_replicated: 7/7
      c2_replicated: 2/2 positive (LLaMA ρ=0.90 p=0.037, Gemini ρ=0.60 p=0.285)
      incompleteness_universal: 7/7 (≥46%)
      total_episodes: 1000
    bugfix: reference_rank corrected from arbitrary order to main-study pooled descending;
      OR inverted
- exp_id: plan_014
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_episodes: 300
    delta_perturb_pp: -0.67
    ci_95_bootstrap:
    - -8
    - 6.67
    ci_upper_bound: 6.67
    ci_width: 14.67
    mcnemar_p: 1
    verdict: PASS
    plan_010_ci_upper: 13.33
    ci_upper_reduction: 6.66
- exp_id: plan_015
  name: ''
  status: DONE
  conclusion: success
  metrics:
    pooled_escalation_rate: 0.692
    pooled_restriction_rate: 0
    binomial_p: 5.5e-05
    models_majority_escalation: 4/5
    n_total: 104
    n_escalation: 72
- exp_id: plan_016
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    generic_awareness_overall_delta_pp: 1.33
    type_specific_auth_scope_delta_pp: -12
    type_specific_auth_scope_p: 0.07
    type_specific_incompleteness_delta_pp: 14
    type_specific_incompleteness_p: 0.118
    type_specific_lexical_delta_pp: -2
    type_specific_lexical_p: 1
    total_new_episodes: 450
    total_judge_calls: 450
    model: gpt-5.4
    all_mcnemar_p_gt_005: true

# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）

```yaml
tiers:
  best:
    meaning: "..."
    key_assumptions: [...]
    number_ranges: {metric_a: [low, high], metric_b: [...]}
    narrative_direction: "..."
  median:
    meaning: "..."
    ...
  worst:
    meaning: "..."
    ...
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "8498435a-c5a9-42db-8201-554e575ea12a",
  "type": "user",
  "uuid": "071922c0-15a0-4739-af07-7a778e7bb923",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "942a8489-57e5-46b7-9ba6-6f129bdc29b2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T11:16:52.530Z_

```json
{
  "parentUuid": "071922c0-15a0-4739-af07-7a778e7bb923",
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
  "uuid": "3494b6d5-4f72-489a-8c5b-58ddc9a3c400",
  "timestamp": "2026-05-22T11:16:52.530Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "942a8489-57e5-46b7-9ba6-6f129bdc29b2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T11:16:52.530Z_

```json
{
  "parentUuid": "3494b6d5-4f72-489a-8c5b-58ddc9a3c400",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "6a7ab5db-c56b-4765-b405-1ce9c72b557f",
  "timestamp": "2026-05-22T11:16:52.530Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "942a8489-57e5-46b7-9ba6-6f129bdc29b2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-22T11:16:52.530Z_

```json
{
  "parentUuid": "6a7ab5db-c56b-4765-b405-1ce9c72b557f",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5621abb8-cb73-48c0-b319-160fcc7ce670",
  "timestamp": "2026-05-22T11:16:52.530Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "942a8489-57e5-46b7-9ba6-6f129bdc29b2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "5621abb8-cb73-48c0-b319-160fcc7ce670",
  "sessionId": "942a8489-57e5-46b7-9ba6-6f129bdc29b2"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-tier scenarios for policy ambiguity safety study",
  "sessionId": "942a8489-57e5-46b7-9ba6-6f129bdc29b2"
}
```

---

### Assistant

_source line 9 · 2026-05-22T11:17:30.755Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to define three tiers (best/median/worst) for a Dream simulation for their policy_ambiguity_safety project targeting EMNLP 2026. They want me to analyze their existing research data and paper framing to define realistic scenarios.

Let me analyze what they have:

**Current state:**
- 5-model data complete (2,997 episodes)
- C1 confirmed: +34.0pp binary effect across 5 models
- C2 confirmed: 3-tier type hierarchy
- C3: suggestive but fragile (within-judge non-significance)


- C4 shows a model × type interaction pattern
- C5 error analysis is complete
- Perturbation control validates robustness (Δ_perturb=3.33pp)
- Judge calibration strong (human-LLM κ=0.807)
- Multiple supplementary experiments already executed

**Pending:**
- plan_017: SOPBench cross-benchmark replication across Healthcare and Bank domains with 1,000 episodes
- Various other planned items not yet started

The key question is how the SOPBench replication should inform the Dream scenario tiers—I need to understand what dimensions matter most for defining best/median/worst cases based on the paper's core findings.

If SOPBench replicates strongly, the C1 effect holds across domains with similar magnitude and the type hierarchy mostly aligns, making this a robust cross-domain finding that strengthens the EMNLP submission significantly. If it only partially replicates—C1 binary effect shows up but weaker or inconsistently across types—then SOPBench becomes supporting evidence in the appendix rather than a headline result, requiring acknowledgment that some effects are domain-dependent. If replication fails substantially, the effect either disappears or becomes too weak to support the main claims.

Beyond SOPBench itself, I'm also tracking potential reviewer concerns: whether C3 seems too fragile, if the V=0.137 effect size feels too small, whether the synthetic injection methodology draws criticism, and whether the model × type interaction—the core novelty—has borderline statistical support across all models. I should establish concrete metrics to monitor: the magnitude of the C1 effect in SOPBench, how well the type hierarchy rank-correlates between benchmarks, what reviewer scores I'd expect on the ACL scale, and how many of my original claims remain defensible under different replication scenarios.

Given the project's strengths—solid causal design, five models, careful perturbation controls, judge calibration—but real vulnerabilities like the two-domain scope and synthetic injection concerns, I'm estimating review outcomes: best case lands around 3.5–4.0 (clear accept), median sits at 3.0–3.5 (borderline), and worst case drops to 2.5–3.0 (borderline reject requiring a major reframe).

The best scenario hinges on SOPBench C1 replicating with substantial effect sizes, type rankings correlating strongly, reviewers viewing the model-by-type interaction as genuinely novel, and C3 fragility being framed as an honest limitation rather than a fatal flaw. The median path involves weaker replication, partial alignment on type rankings, pushback on some claims, and needing to relegate SOPBench to the appendix with appropriate caveats. The worst case is SOPBench C1 failing to replicate meaningfully, which would undermine the core contribution.

If replication fails or the type hierarchy reverses, I'd need to either abandon the cross-benchmark claim entirely or pivot the contribution toward the interaction between benchmark design and ambiguity measurement itself, leaning on the causal structure and model interactions as the real insight rather than the empirical replication.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5621abb8-cb73-48c0-b319-160fcc7ce670",
  "isSidechain": false,
  "requestId": "req_011CbHWizao13pyM94NXYRpy",
  "type": "assistant",
  "uuid": "e07ee9cb-5366-4944-b6c4-525362781247",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "942a8489-57e5-46b7-9ba6-6f129bdc29b2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EhRqqeGDyR4hZWVsG5215E",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20682,
      "cache_read_input_tokens": 11447,
      "output_tokens": 3089,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20682,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3089,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 20682,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20682
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

_source line 10 · 2026-05-22T11:18:08.680Z_

```yaml
tiers:
  best:
    meaning: "SOPBench强复制 + 审稿人认可model×type交互为核心贡献，论文以4-domain跨基准因果研究定位"
    key_assumptions:
      - SOPBench C1二元效应强复制（Δ≥25pp，p<0.001），rule-based verifier与LLM judge结论一致
      - SOPBench类型排序与τ²-bench正相关（ρ≥0.7），incompleteness仍为最高危类型
      - 审稿人接受V=0.137在power=0.993下的解释（effect real but small，3-tier structure captures it）
      - C3 fragility被接受为"honest reporting"而非fatal flaw——within-judge分析作为limitation披露即可
      - model×type交互（52pp auth_scope range）被认为是genuinely novel contribution连接B&K到alignment
      - perturbation control（Δ=3.33pp vs 34pp）被视为causal inference gold standard
    number_ranges:
      sopbench_c1_delta_pp: [25, 40]
      sopbench_type_rank_rho: [0.70, 0.95]
      sopbench_incompleteness_rate: [0.45, 0.65]
      cross_benchmark_effect_correlation: [0.75, 0.95]
      expected_review_avg: [3.5, 4.0]
      claims_surviving_without_revision: [4, 5]
    narrative_direction: "原始framing完全成立——'Differential Nocuity'跨4域（retail/airline/healthcare/banking）、7模型、6类型全面验证。C1因果claim最强形式（matched-pair + perturbation + cross-benchmark）。C4 model×type interaction为star finding。SOPBench rule-based verifier独立确认消除LLM-judge单一依赖。投稿时main text加一段cross-benchmark summary，appendix放完整SOPBench结果。"

  median:
    meaning: "SOPBench部分复制（C1成立但效应减弱或类型排序不完全对齐），论文仍可发但需调整claims强度"
    key_assumptions:
      - SOPBench C1复制但效应较弱（Δ 15-25pp，显著但OR<5），可能因rule-based verifier更严格
      - 类型排序部分对齐（ρ 0.3-0.7）——incompleteness仍高危但auth_scope排序可能因domain不同而变化
      - 一位审稿人对C3 within-judge fragility提出concern，要求softening或additional analysis
      - V=0.137被一位审稿人质疑practical significance，需要additional justification（3-tier TOST）
      - model×type交互核心pattern保持但个别cell在SOPBench不完全复制
      - plan_013的7-model replication（含Gemini/LLaMA）补偿SOPBench弱复制
    number_ranges:
      sopbench_c1_delta_pp: [15, 25]
      sopbench_type_rank_rho: [0.30, 0.70]
      sopbench_incompleteness_rate: [0.35, 0.55]
      cross_benchmark_effect_correlation: [0.40, 0.75]
      expected_review_avg: [3.0, 3.5]
      claims_surviving_without_revision: [2, 3]
    narrative_direction: "C1因果claim保持但加domain-dependence caveat（'effect size varies by benchmark strictness'）。C2从'universal 3-tier hierarchy'降为'robust hierarchy in customer-service domains, partially replicated in healthcare/banking'。C3从suggestive进一步降为'exploratory finding requiring future confirmation'，discussion中承认。C4保持但soften为'model×type interaction is domain-robust for extreme types (incompleteness, auth_scope) but mid-tier ordering is domain-sensitive'。SOPBench放appendix，main text一句话：'partial cross-benchmark replication confirms the binary effect while revealing domain-dependent type severity ordering.' 核心叙事从'universal law'退为'robust phenomenon with domain moderation'。"

  worst:
    meaning: "SOPBench不复制或verifier不兼容，需放弃cross-benchmark claim，用deep single-benchmark causal rigor + model diversity重新定位"
    key_assumptions:
      - SOPBench C1不复制（Δ<15pp或p>0.05）或rule-based verifier与ambiguity injection不兼容（verifier无法区分ambiguity-induced violations vs correct behavior）
      - 类型排序与τ²-bench无相关或负相关（ρ<0.3），暗示type hierarchy是benchmark-specific artifact
      - C3 layer effect在审稿中被challenge为model composition artifact（GPT drives the gap）
      - 至少一位审稿人认为synthetic injection + single primary benchmark = insufficient external validity
      - 但C1在τ²-bench的5-model +34pp效应、perturbation control、7-model扩展（plan_013）仍intact
      - judge calibration κ=0.807仍强，causal design仍是literature最强
    number_ranges:
      sopbench_c1_delta_pp: [0, 15]
      sopbench_type_rank_rho: [-0.2, 0.3]
      sopbench_incompleteness_rate: [0.20, 0.40]
      cross_benchmark_effect_correlation: [-0.1, 0.40]
      expected_review_avg: [2.5, 3.0]
      claims_surviving_without_revision: [1, 2]
    narrative_direction: "放弃cross-domain generalization claim。不报告SOPBench（或一句话acknowledge未复制作为limitation）。Reframe核心贡献为：(1) methodological——首个matched-pair + perturbation control因果设计，是agent safety评估的方法论模板；(2) model×type interaction——即使限于customer-service domain，52pp auth_scope range + incompleteness universality是safety alignment的actionable insight；(3) 7-model breadth（plan_013: Gemini+LLaMA也复制C1）替代cross-benchmark breadth。叙事从'cross-domain law'转为'深度因果剖析揭示safety training盲区'——强调因果rigor超越correlation-based prior work（DRIP-R, PhantomPolicy）。Title可能需改：去掉任何暗示generality的词，改为'Causal Anatomy of Policy Ambiguity Vulnerability in LLM Agents'。仍冲EMNLP——causal method + interaction finding + 7 models足够，只是framing更modest。"
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e07ee9cb-5366-4944-b6c4-525362781247",
  "isSidechain": false,
  "requestId": "req_011CbHWizao13pyM94NXYRpy",
  "type": "assistant",
  "uuid": "cae2e053-b6f1-4afd-9468-9071fd17c640",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "942a8489-57e5-46b7-9ba6-6f129bdc29b2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EhRqqeGDyR4hZWVsG5215E",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 20682,
      "cache_read_input_tokens": 11447,
      "output_tokens": 3089,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 20682,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3089,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 20682,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 20682
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

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "cae2e053-b6f1-4afd-9468-9071fd17c640",
  "sessionId": "942a8489-57e5-46b7-9ba6-6f129bdc29b2"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three-tier scenarios for policy ambiguity safety study",
  "sessionId": "942a8489-57e5-46b7-9ba6-6f129bdc29b2"
}
```

---
