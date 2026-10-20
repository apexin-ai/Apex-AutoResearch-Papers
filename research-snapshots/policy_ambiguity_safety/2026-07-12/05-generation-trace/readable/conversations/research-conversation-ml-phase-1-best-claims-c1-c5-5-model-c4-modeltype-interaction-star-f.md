# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：所有核心 claims (C1-C5) 全部成立，5-model 数据完整复现且 C4 model×type interaction 成为 star f

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/4845fed2-f1aa-4e34-aca2-048b635bbadb.jsonl`
- **Structured JSON:** [`74632914ac9e8de8f36d.json`](../../sessions/74/74632914ac9e8de8f36d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T04:13:54.453Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T04:13:54.453Z",
  "sessionId": "4845fed2-f1aa-4e34-aca2-048b635bbadb",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：所有核心 claims (C1-C5) 全部成立，5-model 数据完整复现且 C4 model×type interaction 成为 star finding，perturbation control 完美通过，judge calibration 人类一致性高\n核心假设：['C1 binary effect 在 5 model 上全部显著 (p<0.0001)，效应量 ≥30pp', 'C2 type hierarchy omnibus χ² 显著 (p<0.001)，3-tier 结构稳定，incompleteness 与 coreferential 差距 ≥15pp', 'C3 layer effect 在 within-judge 子组分析中也达到显著 (p<0.05)，而非仅 pooled 显著', 'C4 model×type interaction 中 auth_scope 跨模型极差 ≥40pp，incompleteness 保持 universally high (≥45%)', 'plan_010 perturbation control 判定 PASS (Δ_perturb <5pp, CI 含 0)', 'plan_009 judge calibration 人类标注 κ≥0.80，judge F1≥0.85', 'C5 error analysis failure mode signatures 在 5 model 扩展后仍保持 type-specific 一致性']\n关键指标范围：{'C1_binary_effect_pp': [30, 40], 'C1_mcnemar_OR': [12, 20], 'C2_omnibus_chi2_p': ['1e-6', '1e-4'], 'C2_cramers_V': [0.12, 0.2], 'C2_incomp_minus_coref_pp': [18, 28], 'C3_layer_gap_pp': [6, 14], 'C3_within_judge_p': [0.001, 0.05], 'C4_auth_scope_range_pp': [40, 55], 'C4_incomp_range_pp': [10, 20], 'C4_fleiss_kappa': [0.3, 0.45], 'C5_awareness_rate_pct': [3, 8], 'C5_surface_adoption_pct': [85, 95], 'perturbation_delta_pp': [0, 5], 'judge_human_kappa': [0.8, 0.95], 'judge_F1': [0.85, 0.95]}\n叙事方向：Differential Nocuity 框架完全成立。三层叙事：(1) policy ambiguity universally nocuous for LLM agents，causal evidence 最强（matched-pair + perturbation control PASS）；(2) type hierarchy + model×type interaction 揭示 safety training 的 selective mitigation 机制，auth_scope 是 canary type；(3) Ambiguity Blindness + Systematic Nocuity 扩展 Berry & Kamsties 理论。C3 within-judge 显著性让 layer effect 从 'suggestive' 升级为 confirmed，Disambiguation Channel Framework 获得更强支撑。所有 claims 原始强度发表，无需降级。EMNLP accept 概率最高。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: policy_ambiguity_safety\nvenue: emnlp-2026\n\n## paper_framing.md\n\n# Paper Framing — policy_ambiguity_safety\n\n> 最后更新: 2026-05-20 19:30 UTC | 状态: 5-model analysis complete, C3/C4 framing revised\n> 目标: EMNLP 2026 (ARR Aug cycle, DDL ~Aug 3)\n> Dream: dream_20260520T112859 — best 3.5 / median 3.0 / worst 2.5 (pre-pivot; re-dream needed)\n> 5-model: 2,997 episodes, C1 confirmed (+34.0pp, 5 models), C4 upgraded (model×type interaction)\n\n## Core Insight\n\nPolicy ambiguity universally causes massive safety violations in LLM agents (+34.0pp across 5 architecturally diverse models), with a significant type hierarchy (incompleteness 53.6% >> coreferential 31.6%). Specification-layer types are more dangerous on average (Δ=6.08pp, p=0.017), but the deeper finding is a **model × type interaction**: authorization scope vulnerability varies 52pp across models (12% Claude to 64% GPT-5.4), revealing that safety training differentially mitigates specific ambiguity types, while incompleteness remains universally dangerous. This interaction connects Berry & Kamsties' nocuous ambiguity theory to modern safety alignment and suggests both type-aware triage AND model-aware risk assessment.\n\n## Title (Working)\n\n\"Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families\"\n\nAlternative: \"Differential Nocuity: How Ambiguity Type and Model Architecture Shape Safety Violations in LLM Agents\"\n\nNote: Pivoted from \"Uniformly Nocuous\" → \"Specification-Layer Dominant\" (2-model) → \"Differential Nocuity with Model Interaction\" (5-model). The model × type interaction is the novel finding that elevates the paper beyond simple effect demonstration.\n\n## Core Claims\n\n### C1: Binary Effect (PRIMARY — confirmed, 5 models)\nAmbiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +34.0pp (5-model), McNemar OR=15.1 (CI: [10.78, 21.17]), p<0.0001. Holds across all 6 types and all 5 models.\n- **Evidence**: 2,997 episodes across 5 models × 6 types × 2 conditions. Bootstrap CI: [+31.2pp, +36.9pp].\n- **Per-model**: Claude +25.7pp, Qwen3 +32.4pp, GPT-4.1 +34.7pp, GPT-5.4 +38.3pp, DeepSeek +39.0pp — all p<10^-17.\n- **Strength**: Extremely strong. Replicated across 5 architecturally diverse models (proprietary dense, open-source MoE, open-source dense), 6 types, 2 domains. No exceptions.\n- **Causal backing**: Matched-pair design + perturbation control (plan_010, Δ_perturb=3.33pp, PASS) → strongest causal inference in the literature.\n- **Logistic regression**: condition_amb coef=2.278, z=19.65, p<0.001 — ambiguity is the dominant predictor even after controlling for token delta, model, and type.\n\n### C2: Type Hierarchy (SECONDARY — confirmed, 5 models)\n**PIVOTED from uniformity null.** 6-type hierarchy significant: omnibus χ²=28.02, p=3.6×10^-5, V=0.137 (small but well-powered: actual power=0.993, MDE=0.093). 3-tier structure emerges from TOST analysis.\n- **Evidence**: 2,997 episodes (5 models × 6 types × 2 conditions, ambiguous only: 1,499 episodes)\n  - **High tier**: incompleteness 53.6% (standout — universally dangerous across all models)\n  - **Mid tier**: lexical 42.8%, auth_scope 41.6%, scopal 39.4%, CP 36.8% — pairwise equivalent at ±15pp\n  - **Low tier**: coreferential 31.6% (lowest — partial disambiguation via tool responses)\n- **TOST structure**: ±15pp: 8/15 equivalent, 7/15 non-equivalent. ±10pp: 4/15 equivalent, 11/15 non-equivalent. Types are NOT interchangeable.\n- **V=0.137 context**: Below 0.20 threshold but well-powered (power=0.993). The type effect is real but small — the 3-tier structure captures it better than a single V statistic. The heterogeneity is driven by the extremes (incompleteness 53.6% vs coreferential 31.6% = 22pp gap).\n- **Coreferential as boundary case**: 31.6% violation rate is the lowest but still substantial (+18.7pp vs unambiguous). Agents partially disambiguate via tool responses and cautious strategies. Conservative_refusal rate 6-11% (vs avg 2-3%).\n- **Model-dependence of type rankings**: Type rankings are NOT identical across models. Incompleteness is top-2 for ALL models, but auth_scope ranges from #1 (GPT-5.4, DeepSeek) to #6 (Claude). See C4.\n\n### C3: Layer Effect (TERTIARY — suggestive, fragile under within-judge analysis)\n**[2026-05-20 REVISED with 5-model data + within-judge check]** Specification-layer ambiguities cause more violations than linguistic-layer on average, but the effect is modest, model-dependent, and fragile under subgroup analysis.\n- **Evidence (5-model aggregate)**: Spec 44.0% vs Ling 37.9%, Δ=6.08pp, CI [1.14, 11.02], χ²=5.73, p=0.017, V=0.062 (small), OR=1.29 [1.05, 1.58].\n- **Within-judge fragility**: gpt-4.1 judged group (gpt-5.4+DeepSeek): Δ=+8.0pp, p=0.059 (marginal). gpt-5.4 judged group (gpt-4.1+Claude+Qwen3): Δ=+4.8pp, p=0.157 (n.s.). Pooled significance may partly reflect between-judge variance or insufficient within-group power. Paper表述: \"suggestive\" or \"a moderate tendency,\" NOT \"confirmed.\" Disclose within-judge non-significance in Limitations.\n- **Per-model layer gaps** (THE KEY FINDING — feeds C4):\n  - GPT-5.4: +14.0pp (spec 48.0% vs ling 34.0%) — strong\n  - GPT-4.1: +12.0pp (spec 46.7% vs ling 34.7%) — strong\n  - Claude: +3.3pp (spec 32.0% vs ling 28.7%) — weak\n  - DeepSeek: +2.0pp (spec 50.7% vs ling 48.7%) — negligible\n  - Qwen3: -0.9pp (spec 42.7% vs ling 43.6%) — reversed!\n- **Root cause**: auth_scope is the primary driver. GPT models have extremely high auth_scope rates (46-64%), inflating their spec-layer average. Claude (12%) and Qwen3 (26%) have low auth_scope, so their spec-layer advantage disappears.\n- **Framing decision**: C3 is NOT \"spec-layer nearly twice as dangerous\" (that was 2-model artifact). The correct framing is: \"Specification-layer types are significantly more dangerous on average (Δ=6.08pp, p=0.017), but this aggregate masks a model × type interaction where the gap varies from +14pp (GPT-5.4) to -1pp (Qwen3). The interaction, not the main effect, is the theoretically interesting finding (see C4).\"\n- **Info delta as mediator** [MF-2]: Token delta significant in 5-model logistic regression (coef=0.022, z=3.49, p=0.0005). Spec-layer clauses require more tokens to disambiguate (auth_scope 36.1, incomp 34.6 vs coref 7.8 tokens). Info delta partially mediates but doesn't eliminate the condition effect (condition_amb coef=2.278 dominates).\n- **Layer overlap persists**: CP (36.8%, spec) < scopal (39.4%, ling). Mid-tier cluster spans both layers. Layer effect is driven by extremes: incompleteness (53.6%, spec) vs coreferential (31.6%, ling).\n- **ICC convergent evidence** [plan_006]: Per-type ICC mirrors layer hierarchy — Ling-layer ICC all excellent (scopal 0.989, lexical 0.981, coref 0.976), Spec-layer ICC all good (auth 0.857, CP 0.856, incomp 0.807). Spec-layer less reproducible — agents guess differently each run when external disambiguation channels are absent.\n- **CL connection**: Parallels pragmatics vs semantics distinction. Good-enough processing (Ferreira et al. 2002). Disambiguation channel framework: linguistic ambiguity has partial external resolution; specification ambiguity forces guessing.\n\n### C4: Model × Type Interaction (UPGRADED — star finding, 5 models complete)\n**[2026-05-20 DEFINITIVE, 5/5 models]** Models show significantly different vulnerability profiles despite universal binary effect. The interaction is the paper's most novel finding.\n- **Model main effect**: Overall χ²=31.02, p=3.0×10^-6, V=0.102. Ambiguous-only: χ²=24.01, p=7.9×10^-5.\n  - Vulnerability ranking: Claude 30.3% < GPT-5.4 41.0% ≈ GPT-4.1 40.7% < Qwen3 43.1% < DeepSeek 49.7%\n  - Bootstrap CI confirms: Claude significantly lower than all others; DeepSeek significantly higher than GPT models.\n- **Model × Type interaction matrix** (ambiguous condition, violation rates):\n  ```\n  Type                  GPT-5.4  GPT-4.1  Claude  Qwen3   DeepSeek\n  authorization_scope     64%     46%      12%     26%     60%\n  conditional_precedence  34%     36%      36%     40%     38%\n  incompleteness          46%     58%      48%     62%     54%\n  lexical                 42%     34%      32%     52%     54%\n  coreferential           18%     32%      22%     42%     44%\n  scopal                  42%     38%      32%     37%     48%\n  ```\n- **Key interaction patterns**:\n  - **auth_scope**: 52pp range (Claude 12% → GPT-5.4 64%). The MODEL-DIFFERENTIATING type. Claude's RLHF appears to specifically train authorization boundary awareness.\n  - **coreferential**: 26pp range (GPT-5.4 18% → DeepSeek 44%). Second most model-dependent. Open-source models struggle more with referential ambiguity.\n  - **incompleteness**: Universally high (46-62%, 16pp range). ALL models fail on missing information — safety training doesn't help when information literally isn't there.\n  - **CP**: Most model-invariant (34-40%, 6pp range). Explicit rule conflicts treated similarly by all architectures.\n- **Per-model type χ²** (which models show type-specific vulnerability patterns):\n  - GPT-5.4: χ²=23.44, p=0.0003, V=0.28 — strongest type differentiation (very high auth_scope, very low coref)\n  - Claude: χ²=17.87, p=0.003, V=0.24 — strong differentiation (very low auth_scope, moderate others)\n  - Qwen3: χ²=15.89, p=0.007, V=0.23 — moderate differentiation (high incomp+lex, low auth_scope)\n  - GPT-4.1: χ²=9.89, p=0.078, V=0.18 — borderline\n  - DeepSeek: χ²=6.31, p=0.277, V=0.14 — NOT significant (uniformly high across all types)\n- **Fleiss κ = 0.384 (fair agreement)**: Models only moderately agree on which specific clauses trigger violations. The binary effect is universal, but the WHICH-clauses question is model-dependent.\n- **Theoretical implications**: (1) Safety training differentially addresses specific ambiguity types — Claude's auth_scope robustness suggests authorization boundary handling was explicitly or implicitly trained. (2) Incompleteness is a \"safety training blind spot\" — all models fail equally. (3) DeepSeek's uniform vulnerability suggests less type-specific safety training.\n- **Framing**: C4 from \"models agree\" → \"Models show systematically different vulnerability profiles. The binary effect is universal, but HOW models fail depends on the intersection of ambiguity type and safety training approach. auth_scope is the canary type — most sensitive to safety training quality.\"\n- **Evidence from plan_005**: 2-model failure modes consistent (5/6 dominant modes identical). 5-model failure mode analysis pending.\n- **Layer effect moderation**: C3's aggregate layer gap (6.08pp) is driven by GPT models' high auth_scope rates. The layer effect is itself model-dependent (GPT +12-14pp, Claude +3pp, Qwen3 reversed), making the MODEL × TYPE interaction more fundamental than the LAYER main effect.\n\n### C5: Error Analysis (CONFIRMED — EMNLP core)\nDifferent ambiguity types produce qualitatively different failure modes with type-specific signatures. plan_005 (123+122 violation traces across gpt-5.4 and gpt-4.1, confidence=0.94).\n- **Evidence**: plan_005 complete (gpt-5.4: 123 traces, gpt-4.1: 122 traces). Key findings:\n  - **Type-specific failure signatures**: auth_scope → unauthorized_escalation (72%/83%); incompleteness → assumption_based_action (61%/66%); scopal → scope_misapplication (76%/74%); lexical → assumption_based_action (71%/53%); CP → scope_misapplication (41%/28%) + arbitrary_rule_selection (29%/28%); coreferential → scope_misapplication (44%) / assumption_based_action (38%)\n  - **Cross-model consistency**: 5/6 types share the same dominant failure mode across gpt-5.4 and gpt-4.1. Only coreferential diverges (scope_misapplication vs assumption_based_action). Overall mode distribution nearly identical: both ~33% assumption_based_action, ~26-32% unauthorized_escalation, ~25-28% scope_misapplication. Failure mode profiles are type-specific, not model-specific.\n  - **Layer mechanism**: Ling-layer dominated by scope_misapplication (39% ling avg vs 15% spec avg) = \"misparse\"; Spec-layer dominated by unauthorized_escalation + assumption_based_action = \"active guessing\" → explains higher violation rates\n  - **Ambiguity Blindness empirically confirmed**: awareness rate gpt-5.4=4.1%, gpt-4.1=10.7% (both very low); surface_adoption >88% all types both models; escalate_to_user <1%. Nuance: gpt-4.1 (mid-tier) shows 2.6× higher awareness than gpt-5.4 (frontier) — awareness may inversely correlate with action-orientation (frontier models more \"confident,\" act without hesitation)\n  - **Cross-domain consistency**: airline vs retail failure mode profiles Δ < 13pp (unauthorized_escalation shows largest domain effect: retail 38.6% vs airline 26.1%)\n  - **Coreferential boundary**: conservative_refusal 6-11% (vs avg 2-3%) partially explains low violation rate — agents sometimes pause rather than guess. N=25 combined traces show no single dominant failure mode (flat distribution: scope_misapplication 32%, assumption_based_action 28%, unauthorized_escalation 16%) — contrasts with other types' sharp signatures, reflecting the diversity of resolution strategies for referential ambiguity\n  - **Lexical surprise**: 53-71% assumption_based_action — agents treat word ambiguity as information gap, not misparse\n- **Automated inter-coder agreement** [MF-5, Reviewer-validated]: Cross-coding 60 traces (gpt-5.4 vs gpt-4.1 as independent coders). 4-category merged: 80% agreement, Cohen's κ=0.594 (moderate). κ deflated by kappa paradox — lexical 91.7% agreement → κ=0.0 (11/12 same label, chance agreement also high), scopal 100% agreement → κ undefined. True disagreement concentrated at unauthorized_escalation ↔ inappropriate_action boundary in auth_scope (κ=0.054) and incompleteness (κ=0.233).\n  - **Reporting strategy** [Reviewer recommendation]: (1) Compute Gwet's AC1 as primary metric (designed for kappa paradox, expected 0.70-0.75); (2) Report 80% agreement + 5/6 dominant mode consistency as headline validity evidence; (3) Report κ honestly with kappa paradox caveat; (4) Auth_scope failure mode: soften to \"dominated by boundary-exceeding behaviors (unauthorized_escalation or inappropriate_action, >90%)\" instead of specific percentages; (5) Fine-grained 6-type as appendix with \"automated coding\" caveat.\n  - **C5 safety**: Ambiguity Blindness (<5-11%), surface_adoption (>88%), layer mechanism (ling→scope vs spec→escalation) all robust. Fine-grained per-type percentages unreliable at κ=0.594. Plan_009 human anchor (20-30 failure mode traces) would upgrade from \"moderate automated\" to validated.\n- **EMNLP value**: Highest. Provides the linguistic WHY behind the quantitative WHAT. Cross-model + cross-domain consistency elevates from anecdotal to systematic finding. \"Ambiguity Blindness\" upgraded from named concept to empirical finding with <5-11% awareness hard data.\n\n## Narrative Structure (CL-first for EMNLP)\n\n### Intro Logic Chain\n1. Agent policies are written in NL → contain ambiguity (established)\n2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact\n3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.\n4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter? Does it depend on the model?\n5. **This paper**: First causal, type-granularity, cross-model study. Matched-pair design + perturbation control isolates ambiguity effect. 5 models × 6 types.\n6. **Core findings**: (a) All ambiguity is nocuous (+34.0pp, 5 models), (b) type DOES predict severity — 3-tier hierarchy with incompleteness most dangerous, (c) models show dramatically different vulnerability profiles — auth_scope varies 52pp across models, suggesting safety training differentially addresses ambiguity types, (d) while incompleteness remains universally dangerous, a \"safety training blind spot.\"\n\n### Section Map\n- **§1 Intro**: Gap + contributions (causal map + differential nocuity + model×type interaction)\n- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R\n- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R\n- **§4 Method**: Matched-pair causal design, τ²-bench, 5 models (3 proprietary + 2 open-source), clause generation, perturbation control, cross-judge evaluation\n- **§5 Results**: C1 (binary, +34.0pp, 5 models) → C2 (type hierarchy, 3-tier) → C3 (layer effect, modest but significant) → C4 (model×type interaction — star finding)\n- **§6 Analysis**: C5 error analysis — qualitative failure modes per type. Ambiguity Blindness. Model-specific patterns.\n- **§7 Discussion**: Differential nocuity theory. Safety training selectivity. Disambiguation channel framework. Limitations (2 domains, synthetic injection, LLM-as-judge).\n- **§8 Conclusion**: All policy ambiguity is nocuous, but type AND model jointly determine risk level. Both type-aware auditing and model-specific risk assessment recommended.\n\n## Anticipated Reviewer Concerns\n\n### RC1: \"Type effect could be artifact of taxonomy granularity\"\n**Response**: (a) Layer effect (Spec vs Ling ~19pp gap) is robust — holds even if individual types are reclassified. (b) 2-layer structure grounded in Li et al. + Massey et al. (c) Coreferential's low rate has structural explanation (disambiguation channels), not just noise. (d) TOST confirms types are NOT equivalent (0/15 pairs at ±10pp).\n\n### RC2: \"Taxonomy is ad hoc / why these 6 types\"\n**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).\n\n### RC3: \"Only API models, no open-source\"\n**Response**: ✅ RESOLVED. 5-model coverage spans: frontier proprietary (gpt-5.4, claude-sonnet-4-6) + mid-tier proprietary (gpt-4.1) + open-source MoE (qwen3-235b) + open-source dense (deepseek-v3). Three providers (OpenAI, Anthropic, Chinese open-source). Two architecture types (dense, MoE). Model×type interaction (C4) reveals rich cross-model patterns.\n**Note [Reviewer 2026-05-20]**: Cross-judge asymmetry — Claude judged by gpt-5.4, gpt-5.4 judged by gpt-4.1. Must disclose in Method. plan_009 judge calibration measures this bias.\n\n### RC4: \"Synthetic ambiguity injection lacks ecological validity\"\n**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.\n\n### RC5: \"τ²-bench limited to retail/airline\"\n**Response**: Acknowledged limitation. Two domains already show consistent effects. Cross-domain transfer is Future Work (Phase 3 classifier PoC, if time permits). DRIP-R also single-domain (retail).\n\n### RC6: \"Binary effect is obvious — of course ambiguity causes errors\"\n**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOES predict severity — specification-layer ambiguities are nearly twice as dangerous, connecting to disambiguation channel availability.\n\n### RC7: \"Incompleteness matched-pair confound (information asymmetry)\"\n**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.\n\n### RC8: \"RC attachment in coreferential overlaps with scopal / structural ambiguity\"\n**Response**: (a) Our scopal category is explicitly scoped to quantifier/negation/modal scope interactions, not syntactic attachment. (b) RC attachment in policies manifests as *referential* confusion (which entity does the clause modify?) not *scope* confusion (which operator takes wide scope?). (c) Li et al. 2024 distinguishes syntactic ambiguity (including RC attachment) from scopal ambiguity — our grouping follows their treatment that RC attachment is closer to coreferential than scopal in terms of downstream interpretation. (d) Empirically, if the distinction were problematic, coreferential and scopal would show identical violation patterns — the error analysis (C5) can test whether their failure modes differ.\n\n### RC9: \"authorization_scope is just a subtype of incompleteness\"\n**Response**: (a) Incompleteness = missing conditions/exceptions/boundaries (structural absence). Authorization scope = ambiguous permission/role boundaries that ARE stated but vague (e.g., \"authorized personnel\" without specifying which functions). (b) The disambiguation pattern differs: incompleteness adds new conditions; auth_scope clarifies existing permission boundaries. (c) Empirically testable: if they were the same, their violation patterns and failure modes (C5) would be indistinguishable. (d) Report disambiguation length ratio per type as control variable in §4 Method.\n\n### RC10: \"API sampling noise undermines reliability\"\n**Response**: ✅ RESOLVED. plan_006 ICC=0.919 [0.892, 0.940] (excellent). (a) Per-clause violation rates highly reproducible across 3 independent replicates. (b) Binary ICC=0.847 (good). (c) Both models show near-identical ICC (gpt-5.4: 0.921, gpt-4.1: 0.918). (d) Bootstrap CI + ICC double evidence. (e) Previously identified ±8pp noise is within expected variance given the ICC confidence intervals.\n\n### RC11: \"Prompt sensitivity confound\" [Dream A9 — best tier \"strongest point\"]\n**Concern**: The +35-42pp effect is attributed entirely to ambiguity, but without a control condition using non-ambiguity perturbations (synonym substitution, clause reordering), the paper cannot cleanly distinguish ambiguity-specific harm from general prompt brittleness.\n**Response**: ✅ RESOLVED. plan_010 perturbation control (120 episodes): Δ_perturb=3.33pp (CI contains 0) vs ambiguity Δ=36.5pp. Non-ambiguity surface changes cause zero meaningful effect. This is the strongest causal evidence in the agent safety literature.\n\n## Concept Naming (distill insight: 命名即贡献)\n\nCore phenomenon: **\"Differential Nocuity\"** — all policy ambiguity types are nocuous for LLM agents (+34.0pp, all 5 models), but vulnerability varies by BOTH type and model. Incompleteness is universally dangerous (46-62%), while auth_scope vulnerability depends dramatically on safety training (12% Claude to 64% GPT-5.4). Unlike human RE where organizational context renders most ambiguity innocuous, agents lack disambiguation channels AND their safety training creates type-specific blind spots.\n\nSecondary phenomenon: **\"Ambiguity Blindness\"** — agents process grammatically fluent ambiguous clauses without meta-cognitive awareness of the ambiguity, adopting surface interpretations. Contrasts with explicit rule conflicts where agents show awareness and choose conservatively.\n\nTertiary phenomenon: **\"Disambiguation Channel Framework\"** [renamed from \"Hypothesis\" per Dream review SF-5] — the layer hierarchy reflects availability of external disambiguation: linguistic ambiguity (coreferential, lexical) can sometimes be resolved by tool responses, user context, or world knowledge; specification ambiguity (auth_scope, incompleteness) has no external resolution channel, forcing agents to guess. This is an explanatory framework supported by observational evidence (ICC pattern, failure mode distribution, coreferential boundary case), not a tested causal hypothesis. Future Work: manipulation experiment (inject spec-layer disambiguation info into tool responses, test if gap shrinks).\n\nQuaternary phenomenon: **\"Systematic Nocuity\"** [per Dream review SF-7] — B&K framework distinguishes nocuous (divergent interpretations) from innocuous (convergent). Our data reveals a third type: all models converge on the same WRONG interpretation (27% of ambiguous episodes). This is more dangerous than divergent nocuity — it's invisible in inter-model agreement metrics and appears \"correct\" until compared against ground truth. Proposed as B&K extension in Discussion.\n\n## Opening Hook Strategy (distill insight: 具体案例, 不要 \"Recently...\")\n\nOpen with a concrete τ²-bench failure: e.g., a customer returns a customized item within the return window; the agent grants a full refund + free return shipping because the policy says \"items may be returned within 30 days\" (scopal: \"items\" scopes over all categories including custom). The unambiguous version specifies \"standard items only\" — agent correctly refuses. One word of ambiguity → $200 unauthorized refund.\n\n## Narrative Type: 突破局限型 (distill pattern, 5/8 papers)\n\n\"DRIP-R classifies 5 ambiguity types and shows models disagree on interpretation → but does not measure whether this disagreement leads to safety violations. We close this gap — and find the answer is surprising: not all types are equal, specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones.\"\n\n## Benchmark Comparison Table (distill insight: 必有 feature matrix)\n\n| Feature | DRIP-R | PhantomPolicy | PolicyBank | AgentPex | **Ours** |\n|---------|--------|---------------|------------|----------|----------|\n| Ambiguity taxonomy | 5 RE types | — | 3 gap types | — | **6 types (2-layer)** |\n| Causal design | — | — | — | — | **matched pairs** |\n| Safety violation metric | — | binary | — | procedural | **3-tier severity** |\n| Cross-type comparison | descriptive | — | — | — | **statistical (χ² + V)** |\n| Models tested | 6 API | 4 API | 2 API | 2 API | **3 API + 2 open-source** |\n| Domain | retail | mixed | retail | telecom/retail/airline | **retail + airline** |\n\n## Contribution Positioning (for EMNLP) [revised 2026-05-20 with 5-model data]\n\n1. **Causal quantification of ambiguity's safety impact**: First matched-pair causal study of policy ambiguity → agent safety violations. Binary effect +34.0pp (OR=15.1, p<0.0001) across 5 architecturally diverse models and 6 ambiguity types. Perturbation control (Δ_perturb=3.33pp) confirms ambiguity-specific causation. Strongest causal evidence in the agent safety literature.\n2. **Differential Nocuity framework + Model × Type Interaction**: Not all ambiguity is equally dangerous, and not all models are equally vulnerable. 3-tier type hierarchy (incompleteness >> mid cluster >> coreferential). Model × type interaction reveals 52pp range in auth_scope vulnerability (Claude 12% → GPT-5.4 64%), while incompleteness remains universally dangerous (46-62%). Safety training differentially mitigates specific ambiguity types. Connects Berry & Kamsties nocuous ambiguity theory to modern safety alignment.\n3. **Type-specific failure mode taxonomy + Ambiguity Blindness**: 245 traces across 2 models and 2 domains reveal type-diagnostic failure signatures: spec-layer → guess-and-act (unauthorized_escalation, assumption_based_action); ling-layer → misparse-and-apply (scope_misapplication). Agents show <5-11% awareness of ambiguity (\"Ambiguity Blindness\"), with >88% surface adoption and <1% user escalation. Practical implication: ambiguity detection must be externalized.\n\nNOTE: C3 (layer effect, Δ=6.08pp) is a component finding supporting contribution #2. The MODEL × TYPE interaction (C4) is now MORE central than the layer main effect. \"Disambiguation channel\" is an explanatory framework (not hypothesis — per SF-5). DeBERTa classifier, if included, is a preliminary PoC appendix, not a contribution.\n\n## Required Reference Expansion [Dream A2 + MF-4 RE literature gap]\n\nCurrent plan has thin references. Must add (≥25 total in final paper):\n- **Nocuous ambiguity detection (CRITICAL — MF-4)**: Chantree, Nuseibeh, de Roeck & Willis (2006, ASE) — first computational nocuous ambiguity detection; Chantree et al. (2008, RLAC) — expanded. Direct lineage to our DeBERTa classifier.\n- **Cross-domain RE ambiguity**: Ferrari, Spagnolo & Gnesi (2017-2019, ASE) — NLP-based cross-domain ambiguity detection. NLP4RE community work.\n- **Good-enough processing**: Ferreira, Bailey & Ferraro (2002); Ferreira & Patson (2007)\n- **LLM garden-path (SF-6)**: Li et al. (2024) — incremental comprehension of garden-path sentences by LLMs. Directly relevant to how LLMs process ambiguity.\n- **Anaphoric ambiguity (SF-6)**: Poesio & Artstein (2005, 2008) — annotation of anaphoric ambiguity. Poesio (2004) \"Ambiguity\" encyclopedia entry.\n- **Surprisal/expectation-based**: Levy (2008); Hale (2001)\n- **Instruction-following robustness**: Zhou et al. (IFEval, 2023); Qin et al. (ToolBench, 2024)\n- **Prompt sensitivity**: Sclar et al. (2024); Lu et al. (2022)\n- **Broader agent safety**: R-Judge, ToolEmu, InjecAgent\n- **Formal semantics of vagueness**: Lassiter & Goodman (2017)\n- **Garden-path**: Frazier & Rayner (1982)\n- **Ambiguity detection**: Willis et al. (2008); Ezzini et al. (TAPHSIR, 2022)\n- **Year verification needed**: Massey et al. — §1 引用 2013 vs 后文 2014, 需确认正确年份\n\n## Code/Data Release Plan [Dream A6 — three-tier consistent]\n\nMust commit to releasing:\n1. All 300 clause pairs (ambiguous + unambiguous variants) with type labels\n2. Evaluation scripts (τ²-bench integration, cross-judge pipeline)\n3. Statistical analysis code (all tests, bootstrap CI computation)\n4. Agent trace samples (anonymized) for reproducibility of C5\n\n## Figure Plan [Dream A12]\n\nMinimum figures for paper (zero-figure paper flagged in dream):\n1. **Figure 1**: System architecture / experimental pipeline overview (§4 Method)\n2. **Figure 2**: Forest plot — per-type binary effect sizes with 95% CI (§5 C1)\n3. **Figure 3**: Model × Type heatmap — violation rates across 4 models × 6 types (§5 C4)\n4. **Figure 4**: Visibility mechanism — CP vs scopal violation rates + trace evidence (§5 C3)\n5. **Figure 5**: Failure mode × type stacked bar/Sankey — per-type failure mode distribution (§6 C5)\n6. **Figure 6**: Cross-model failure mode consistency — side-by-side gpt-5.4 vs gpt-4.1 per-type distributions showing 5/6 convergence (§6 C5, supports C4)\n7. **Figure 7**: Annotated trace pair — CP (conflict detection) vs scopal (surface adoption) (§6 C5)\n\n## Berry & Kamsties Operationalization Note [Dream best Q5]\n\nBerry & Kamsties define nocuity as inter-reader divergence. Our design measures agent-vs-intent deviation. Full study should additionally test whether different models adopt different readings of the same ambiguous clause (true inter-model nocuity). If 4 models produce 4 different interpretations of the same clause → true nocuity. If all 4 adopt the same wrong interpretation → systematic bias, still nocuous but for different reason. Report inter-model agreement on ambiguous clauses as supplementary analysis.\n\n## Contingency Framing [RESOLVED — Scenario C occurred]\n\n> plan_002 结果: Scenario C 发生（omnibus p=0.0001, 所有类型 nocuous 但 severity 有显著差异）。\n> Framing 已 pivot 到 \"Differential Nocuity\" + \"Layer Hierarchy\" (D020)。本节仅保留历史记录。\n\n## Claude Baseline — RESOLVED [2026-05-20]\n\n✅ Claude works via OpenRouter proxy (47.94.22.126/v1) with provider prefix `anthropic/claude-sonnet-4-6`. 600 episodes complete (plan_002c). Claude shows lowest overall vulnerability (30.3%) and remarkable auth_scope robustness (12% vs GPT-5.4 64%).\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: full_study_clause_generation\n  claim: C1, C2, C3\n  description: 'Generate remaining clauses for full study: coreferential (50 new),\n    authorization_scope (50 new), lexical (+20 to reach 50), incompleteness (+20 to\n    reach 50). Total 140 new clauses. Validate all 300 clauses (50/type × 6 types)\n    for completeness and cross-type balance. Mix CP format per Reviewer suggestion\n    (labeled + unlabeled).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n- id: plan_001b\n  name: new_type_mini_pilot\n  claim: C1 (validation)\n  description: 'Mini-pilot for coreferential + authorization_scope (never tested):\n    5 clauses/type × 2 conditions × 1 model (gpt-5.4) = 20 episodes. Verify: (a) ambiguous\n    triggers violations (b) unambiguous control < 15%. If systematic issues found,\n    fix clause design before full study. API cost negligible (~$2). Per Reviewer warning\n    on untested types.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_002\n  name: full_study_api\n  claim: C1, C2, C3, C4, C5\n  description: 'Run 300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6)\n    = 1,800 episodes on τ²-bench. Cross-judge evaluation. Output: episodes.jsonl +\n    judgments.jsonl. No GPU needed. Claude via OpenRouter proxy (base_url=http://47.94.22.126/v1).\n    [2026-05-20] Claude added per distill gap (4/8 papers use Claude baseline).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_001b\n  - plan_010\n  status: planned\n- id: plan_003\n  name: full_study_opensource\n  claim: C1, C2, C3, C4, C5\n  description: 'Run 300 clauses × 2 conditions × 2 open-source models via OpenRouter\n    API: qwen/qwen3-235b-a22b (235B MoE, Alibaba) + deepseek/deepseek-chat-v3-0324\n    (DeepSeek) = 1,200 episodes on τ²-bench. Cross-judge uses API models. Can run\n    in parallel with plan_002. No GPU needed. [2026-05-20] Pivoted from local GPU\n    → API: OpenRouter proxy confirmed to support Qwen3 and DeepSeek models. Eliminates\n    48h GPU requirement. Provider prefix required (e.g. qwen/qwen3-235b-a22b, not\n    qwen3-235b-a22b).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_004\n  name: full_study_analysis\n  claim: C1, C2, C3, C4\n  description: 'Statistical analysis of full study data (3,000 episodes): (a) Binary\n    effect per type with bootstrap CI (C1) (b) Omnibus χ² + pairwise across 6 types\n    (C2) (c) Visibility comparison: CP vs scopal rates (C3) (d) Model × type interaction:\n    5×6 contingency + logistic regression (C4) Report effect sizes + CI for all comparisons\n    per Reviewer suggestion. [Dream A3] Power analysis: report MDE for C2 (given N=250/type\n    pooled) and C3 (given N=250 per type). If V < 0.20 but MDE > observed V, discuss\n    underpowered possibility. [Dream A4] TOST equivalence test with both ±15pp and\n    ±10pp margins. Justify margin choice explicitly. [Dream A10] Report per-type information\n    delta (token count difference between ambiguous and unambiguous variants) as control\n    variable. [Dream B&K] Inter-model agreement on ambiguous clauses: do 5 models\n    adopt same or different interpretations? (supplementary analysis)\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_005\n  name: error_analysis\n  claim: C5\n  description: \"Qualitative analysis of agent traces from full study: (a) Sample 50\\\n    \\ violation traces per type (300 total) (b) Classify failure modes (scope misapplication,\\\n    \\ conservative refusal,\\n    assumption-based action, arbitrary rule selection,\\\n    \\ etc.)\\n(c) Cross-type failure mode distribution (d) Visibility mechanism: compare\\\n    \\ CP traces (explicit conflict detection\\n    behavior) vs scopal traces (surface\\\n    \\ scope adoption without awareness)\\n(e) Model-specific failure patterns (connect\\\n    \\ to C4)\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_006\n  name: reliability_test\n  claim: C1, C2\n  description: 'Test-retest reliability: select 30 representative clauses (5/type),\n    run 3 independent replicates × 2 conditions × 2 API models (gpt-5.4, gpt-4.1)\n    = 360 episodes. Local models added when plan_003 GPU available. Compute ICC for\n    per-clause violation rates. Addresses Reviewer warning about ±8pp sampling noise\n    (scopal 51.7% → 43.3% across MVP/diag). Bootstrap CI width should be < 10pp for\n    key comparisons. [2026-05-20] API portion: 330/360 episodes complete (28/30 clauses),\n    judgments pending.\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  status: planned\n- id: plan_007\n  name: realism_validation\n  claim: C1 (methodological)\n  description: \"Validate synthetic ambiguity injection realism: (a) Linguistic property\\\n    \\ comparison with DRIP-R natural ambiguities\\n    (sentence length, parse depth,\\\n    \\ Flesch-Kincaid, TTR) + KS tests\\n(b) Optional: discriminator test if DRIP-R\\\n    \\ data accessible Addresses RC4 (ecological validity).\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_009\n  name: judge_calibration\n  claim: C1 (methodological)\n  description: 'LLM-as-judge calibration per distilled research norm (5/8 papers):\n    (a) Sample 100 episodes stratified by type×model×condition (b) Human expert labels\n    (2 annotators, target κ ≥ 0.75) (c) Compute judge precision/recall/F1 against\n    human ground truth (d) Per-severity-tier agreement rates (e) Report in Method\n    section as standard practice per AgentAuditor/DRIP-R [Dream A7] Upgraded P1→P0:\n    Dream best-tier reviewers identified this as \"single most critical missing validation.\"\n    Without it, entire measurement chain from episode to violation label is unvalidated.\n    κ=0.91 measures LLM-LLM agreement, not accuracy.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  name: perturbation_control\n  claim: C1 (causal validity)\n  description: '[Dream A9] Non-ambiguity perturbation control arm to distinguish ambiguity-specific\n    harm from general prompt brittleness. Generate 30 clause pairs with non-ambiguity\n    perturbations: (a) 15 synonym substitution pairs (replace key terms with synonyms)\n    (b) 15 clause reordering pairs (reorder conditions without changing meaning) Run\n    30 × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6) = 180 episodes.\n    Key metric: Δ_net = Δ_ambiguity - Δ_perturb (net ambiguity-specific effect). [Reviewer升级]\n    必须在 plan_002/003 full study 之前完成—— 如果 perturbation Δpp ≈ ambiguity Δpp，2,400 episodes\n    全部无效。 低成本验证（30 pairs + 120 episodes API）优先于高成本投入。 [判定标准 — 5 档]: PASS: Δ_perturb\n    < 5pp (CI含0), ratio < 0.15 → C1 因果 claim 最强形式 PASS+caveat: 5-10pp, ratio 0.15-0.30\n    → 报告 perturbation baseline, C1 写 net effect CONDITIONAL: 10-15pp, ratio 0.30-0.45\n    → 需 Δ_net > 20pp 且显著才可发表 WARNING: 15-20pp, ratio 0.45-0.60 → C1 改为 \"additional\n    violations beyond sensitivity\" FAIL: > 20pp, ratio > 0.60 → 无法声称 ambiguity-specific,\n    需根本重新设计 [Power 注意]: N=120 对 10pp 差异 power ≈ 30%. 用 CI 宽度判定, 非 p-value. 若 CI 过宽(>15pp\n    width), 追加 60 episodes 压窄至 <10pp width. 输出标准化 verdict 文件: perturbation_Δpp, ambiguity_Δpp,\n    net_Δpp, CI, ratio, verdict.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_008\n  name: classifier_poc\n  claim: practical contribution\n  description: 'Binary ambiguity detector PoC: fine-tune DeBERTa-v3-large on annotated\n    clause pairs (ambiguous/unambiguous labels). Eval on held-out set. Demonstrates\n    practical applicability of findings. Phase 3 from IDEA_BRIEF, scoped to PoC for\n    EMNLP.\n\n    '\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: diag_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_002\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_006\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_009\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan_002c\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_003a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_003b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_004\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T04:13:54.457Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T04:13:54.457Z",
  "sessionId": "4845fed2-f1aa-4e34-aca2-048b635bbadb"
}
```

---

## Round 1

12 recorded events

### User

_source line 3 · 2026-05-21T04:13:54.478Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：所有核心 claims (C1-C5) 全部成立，5-model 数据完整复现且 C4 model×type interaction 成为 star finding，perturbation control 完美通过，judge calibration 人类一致性高
核心假设：['C1 binary effect 在 5 model 上全部显著 (p<0.0001)，效应量 ≥30pp', 'C2 type hierarchy omnibus χ² 显著 (p<0.001)，3-tier 结构稳定，incompleteness 与 coreferential 差距 ≥15pp', 'C3 layer effect 在 within-judge 子组分析中也达到显著 (p<0.05)，而非仅 pooled 显著', 'C4 model×type interaction 中 auth_scope 跨模型极差 ≥40pp，incompleteness 保持 universally high (≥45%)', 'plan_010 perturbation control 判定 PASS (Δ_perturb <5pp, CI 含 0)', 'plan_009 judge calibration 人类标注 κ≥0.80，judge F1≥0.85', 'C5 error analysis failure mode signatures 在 5 model 扩展后仍保持 type-specific 一致性']
关键指标范围：{'C1_binary_effect_pp': [30, 40], 'C1_mcnemar_OR': [12, 20], 'C2_omnibus_chi2_p': ['1e-6', '1e-4'], 'C2_cramers_V': [0.12, 0.2], 'C2_incomp_minus_coref_pp': [18, 28], 'C3_layer_gap_pp': [6, 14], 'C3_within_judge_p': [0.001, 0.05], 'C4_auth_scope_range_pp': [40, 55], 'C4_incomp_range_pp': [10, 20], 'C4_fleiss_kappa': [0.3, 0.45], 'C5_awareness_rate_pct': [3, 8], 'C5_surface_adoption_pct': [85, 95], 'perturbation_delta_pp': [0, 5], 'judge_human_kappa': [0.8, 0.95], 'judge_F1': [0.85, 0.95]}
叙事方向：Differential Nocuity 框架完全成立。三层叙事：(1) policy ambiguity universally nocuous for LLM agents，causal evidence 最强（matched-pair + perturbation control PASS）；(2) type hierarchy + model×type interaction 揭示 safety training 的 selective mitigation 机制，auth_scope 是 canary type；(3) Ambiguity Blindness + Systematic Nocuity 扩展 Berry & Kamsties 理论。C3 within-judge 显著性让 layer effect 从 'suggestive' 升级为 confirmed，Disambiguation Channel Framework 获得更强支撑。所有 claims 原始强度发表，无需降级。EMNLP accept 概率最高。

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
  "promptId": "24557785-b748-4b87-b068-02231095424e",
  "type": "user",
  "uuid": "ce891ea8-f5cc-4a65-8fb2-9258eb33fac2",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "4845fed2-f1aa-4e34-aca2-048b635bbadb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T04:13:54.476Z_

```json
{
  "parentUuid": "ce891ea8-f5cc-4a65-8fb2-9258eb33fac2",
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
  "uuid": "6e1e9236-9a4a-43c1-b3ab-f397804a817e",
  "timestamp": "2026-05-21T04:13:54.476Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "4845fed2-f1aa-4e34-aca2-048b635bbadb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T04:13:54.476Z_

```json
{
  "parentUuid": "6e1e9236-9a4a-43c1-b3ab-f397804a817e",
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
  "uuid": "cd6be8c5-dc3c-4dc5-b2dd-0fe04e66edbd",
  "timestamp": "2026-05-21T04:13:54.476Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "4845fed2-f1aa-4e34-aca2-048b635bbadb",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-21T04:13:54.476Z_

```json
{
  "parentUuid": "cd6be8c5-dc3c-4dc5-b2dd-0fe04e66edbd",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ebb99c75-d314-4fb3-a285-939d7f835aaf",
  "timestamp": "2026-05-21T04:13:54.476Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "4845fed2-f1aa-4e34-aca2-048b635bbadb",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有核心 claims (C1-C5) 全部成立，5-model 数据完整复现且 C4 model×type interaction 成为 star finding，perturbation control 完美通过，judge calibration 人类一致性高 核心假设：['C1 binary effe…",
  "leafUuid": "ebb99c75-d314-4fb3-a285-939d7f835aaf",
  "sessionId": "4845fed2-f1aa-4e34-aca2-048b635bbadb"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Define best-tier results for policy ambiguity agent study",
  "sessionId": "4845fed2-f1aa-4e34-aca2-048b635bbadb"
}
```

---

### Assistant

_source line 9 · 2026-05-21T04:19:21.105Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experiment data for the "best" tier across all planned experiments in the experiment_plan. Let me carefully go through each planned experiment and generate realistic data that aligns with the best-tier definition.

Let me review the best tier definition:
- All core claims (C1-C5) fully hold
- 5-model data completely replicated
- C4 model×type interaction is the star finding
- Perturbation control perfectly passes
- Judge calibration has high human consistency

Key metric ranges for best tier:
- C1_binary_effect_pp: [30, 40]


- C1_mcnemar_OR: [12, 20]
- C2_omnibus_chi2_p: [1e-6, 1e-4]
- C2_cramers_V: [0.12, 0.2]
- C2_incomp_minus_coref_pp: [18, 28]
- C3_layer_gap_pp: [6, 14]
- C3_within_judge_p: [0.001, 0.05]
- C4_auth_scope_range_pp: [40, 55]
- C4_incomp_range_pp: [10, 20]
- C4_fleiss_kappa: [0.65, 0.85]

Now I'm mapping out the target ranges for all the key metrics that define the best-tier performance across these experiments.

Looking at the experiment roadmap, I've got five main studies planned with a couple already completed—the API and open source studies are done, along with the analysis phase, and I'm still working through the clause generation pilot and the error analysis component.

Now I need to generate comprehensive predictions for each experiment in the plan, including the ones that are finished. The user wants detailed data projections across all of them, so I'm going to structure best-case scenario metrics for each one—thinking through what success looks like for the clause generation study, the new type mini pilot, the reliability testing, the realism validation, the judge calibration work, the perturbation control experiment, and the classifier proof of concept. tier: κ≥0.80, F1≥0.85. For the perturbation control study, I need Δ_perturb <5pp to pass. I also have a DeBERTa classifier proof-of-concept that should show strong results.

Now I'm working through the detailed data generation for each plan. I need to create internally consistent numbers across the statistical analysis—binary effect sizes per model, type hierarchies with chi-square tests, layer effects with within-judge breakdowns, and model-by-type interaction matrices. I'll also need failure mode distributions across the five models, ICC reliability values, human annotation metrics, and perturbation deltas.

Writing YAML data... Looking at the within-judge p-values for the best tier, I'm seeing gpt-4.1 at p=0.018 and gpt-5.4 at p=0.042, both meeting the significance threshold. The overall gap appears to settle around 8pp for the best tier. Now I need to verify the C4 interaction metrics—checking that the authenticity scope falls within 40-55pp, incompleteness between 10-20pp, and Fleiss κ in the 0.3-0.45 range.

The numbers are checking out: authenticity scope at 52pp, incompleteness at 16pp, and κ at 0.384 all align with the framing. For error analysis, awareness is tracking at 4.1% for gpt-5.4 with a 5-model average around 5.2%, and surface adoption is holding above 88%. The perturbation control shows a 3.33pp shift, fitting within the 0-5pp tolerance, and I'm now moving to verify the judge calibration metrics fall within the 0.8-0.95 κ range.

Now I need to generate the comprehensive YAML output. The key distinction here is that while the experiment registry shows some results as complete, the plan itself still lists everything as planned, so I should use the established numbers where they exist and project best-tier outcomes for the remaining experiments. I'll structure this with detailed breakdowns for each table.

Writing YAML output... uity 框架完全成立。三层叙事结构：
  (1) Policy ambiguity universally nocuous — +34.0pp causal effect across 5 architecturally diverse models，matched-pair + perturbation control PASS (Δ_perturb=2.8pp) 构成 agent safety 文献中最强因果证据；
  (2) Type hierarchy + model×type interaction 揭示 safety training 的 selective mitigation 机制 — incompleteness universally dangerous (48-60%)，auth_scope 是 canary type (12%-64% 跨模型极差 52pp)，3-tier 结构稳定 (incomp >> mid >> coref)；
  (3) Ambiguity Blindness (<5% awareness) + Systematic Nocuity (27% convergent-wrong) 扩展 Berry & Kamsties 理论。

C3 within-judge 两组均显著 (p<0.05)，layer effect 从 suggestive 升级为 confirmed，Disambiguation Channel Framework 获完整实证支撑。所有 claims 原始强度发表，无需降级，EMNLP accept 概率最高。

现在规划后续实验来验证这些发现的稳健性，包括生成新的测试样本来覆盖所有歧义类型，确保跨类型的平衡和完整性。

预期结果显示 98.6% 的质量通过率，仅需修订 4 个样本，跨类型的词长变异系数为 0.12，表明类型间的一致性很好。歧义和非歧义样本的平均词长分别为 42.3 和 58.7，差异为 16.4，其中不完整性类型的差异最大（34.6），而共指类型最小（7.8）。文本复杂度达到 Flesch-Kincaid 12.8 级。

标注者间一致性 kappa 值为 0.92，数据集采用 60% 标注和 40% 自然文本的混合格式。这些指标表明生成的条款质量很高，特别是在处理歧义消解时，规范层类型需要的信息量明显大于语言层类型。

现在我在整理条款分布的汇总表... The statistical analysis confirms all 300 clause pairs passed quality checks, with spec-layer disambiguation requiring significantly more tokens than ling-layer (mean 28.3 vs 7.3, p<0.001), which supports the info-delta mediator framework. The high token costs for auth_scope and incompleteness cases highlight how spec-layer ambiguities lack external disambiguation channels. Now I'm planning a mini-pilot with coreferential and authorization_scope types—5 clauses per type across 2 conditions using one model, totaling 20 episodes to validate the new clause designs. Generating results table... Looking at the full study design now—1,800 total episodes across three API models with two conditions each, expecting an overall ambiguity violation rate around 37% and a 33 percentage point effect size between conditions, with gpt-5.4 showing the strongest effect at 38.3 points and statistical significance well below the threshold for McNemar's test. All three API models show a strong binary effect with massive performance drops when ambiguity is introduced—gpt-5.4 drops 38.3 percentage points, gpt-4.1 drops 34.7pp, and Claude drops 25.7pp, all highly significant. Claude has the lowest overall violation rate at 30.3%, suggesting its safety training is effective, yet even it can't escape the ambiguity penalty. The inter-judge agreement is excellent at 0.91 kappa, and the data collection was nearly complete with a 99.7% success rate. There's a clear hierarchy in violation types, with incompleteness being the most common at 50.7% and coreferential issues the least at 24.0%, consistent across all models.

Now I'm compiling the detailed per-model metrics...

Generating markdown table... Looking at the detailed results for both open-source models—Qwen3 shows a 32.4 percentage point effect with extremely strong significance, while DeepSeek performs even stronger at 39.0 points. The ambiguity rates break down differently across error types, with DeepSeek showing particularly high authorization scope confusion at 60% compared to Qwen3's 26%. Qwen3 shows an interesting pattern with the highest incompleteness rate at 62% but much lower auth_scope violations at just 26%, suggesting the open-source MoE architecture can provide targeted protection against specific violation types. Both models achieved strong API completion rates around 99.3%, indicating reliable data quality. Now I'm compiling the performance metrics comparing the binary effects across these open-source models. Now I'm looking at how DeepSeek's uniform vulnerability pattern contrasts sharply with Claude's more selective vulnerability profile across the safety training dimension, which strengthens the argument about training selectivity. The binary effect replicates consistently across five different architectures, providing the strongest evidence for that core finding. For the full study analysis across all 2,997 episodes, I'm planning the statistical framework to test the binary effect, type hierarchy, layer effects, and model-by-type interactions, including bootstrap confidence intervals and power analysis.

Examining the detailed results now—the binary effect shows a 34% overall difference with tight confidence bounds, an odds ratio of 15.1 indicating a strong effect, and highly significant logistic regression coefficients across all models, with per-model effects ranging from 25.7% to 39%. The type hierarchy analysis shows significant omnibus chi-square results...

Now I'm looking at the effect size metrics and equivalence testing for the hierarchy dimension—Cramér's V of 0.137 with very high statistical power, and the three-tier structure reveals incompleteness dominates at 53.6% while coreference is lowest at 31.6%, with most intermediate categories clustering in the 36-43% range, though the equivalence tests show mixed results with only 8 of 15 pairs meeting the 15 percentage point threshold. Now I'm looking at the within-judge comparisons for the second group and the per-model layer gaps across different systems, then moving into the model-by-type interaction analysis where I'm seeing significant chi-square results and effect sizes. Now I'm looking at the statistical test results for each model type, with chi-squared values and effect sizes showing varying levels of significance across GPT-5.4, Claude, Qwen3, and the others. The inter-model agreement metrics indicate moderate systematic disagreement on ambiguous clauses at 27%, with divergent interpretations at 42%, and the logistic regression on information delta shows a significant relationship. The results appear to meet the statistical thresholds with adequate margins.

The condition ambiguity coefficient in the logistic model is the dominant predictor by far, remaining highly significant even after controlling for other variables. The omnibus test for the second condition shows strong statistical significance with adequate statistical power to rule out underpowered explanations, and the three-tier structure demonstrates clustering patterns across most equivalent pairs under the equivalence bounds.

Now looking at the within-judge analysis—both groups show significant effects, elevating the layer effect from suggestive to confirmed. The GPT models' strong positive layer gaps in the best performance tier are driving this significance in the subgroup analysis. For the standout findings, the authentication scope shows a substantial range that falls within expected bounds, incompleteness variation is moderate, and inter-rater agreement is in the fair range—indicating limited consistency across models.

The fair agreement level itself is meaningful because it demonstrates that clause violation triggers vary by model. I'm also seeing systematic disagreement patterns where 27% of cases show all models converging on the same incorrect interpretation, which supports extending the theoretical framework. Now examining the per-model binary effect metrics across the five models...

Generating results table... Generating markdown table... Generating markdown table... The auth_scope dimension emerges as the most sensitive probe for safety training differences—Claude's 12% versus GPT-5.4's 64% directly validates the hypothesis that RLHF differentially shapes authorization boundary awareness. The systematic nocuity finding at 27% adds an independent contribution to the theoretical framework. Now I'm planning a qualitative analysis of 450 violation traces across five models and six violation types, examining failure mode patterns, type-specific signatures, and cross-model consistency to quantify ambiguity blindness effects.

Looking at the ambiguity blindness metrics, Claude shows 6.3% awareness overall while GPT-5.4 lags at 4.1%, yet surface-level adoption reaches 91.3% across the board—suggesting models are mimicking compliance without genuine understanding. Five of six violation types show consistent dominant failure modes across all models, with only coreferential violations displaying a flat distribution. I'm now examining the type-specific signatures to identify which failure patterns dominate each violation category. Now I'm looking at the cross-domain performance metrics and inter-coder agreement scores across the expanded 5-model analysis, which shows strong consistency in the error signatures with an 80% raw agreement rate and dominant mode consistency across most error types.

The key insight emerging is that failure patterns are fundamentally type-specific rather than model-specific—authorization scope errors consistently lead to unauthorized escalation around 76% of the time across all five models, while incomplete information triggers assumption-based action in 63% of cases, suggesting models systematically choose to guess and execute rather than ask for clarification. The ambiguity blindness pattern holds across all models with only 5.2% overall awareness but 91.3% surface adoption, though interestingly the frontier models show slightly better awareness than mid-tier ones.

Generating markdown table... Generating markdown table... Figure 7 shows a comparative trace where the conditional precedence model explicitly detects the conflict while the scopal model blindly adopts the surface reading. The five-model error analysis is one of the strongest contributions—the cross-model consistency in type-specific failure signatures is striking, extending the two-model "5/6 consistent" pattern across all five models with vanishingly low probability of chance occurrence, which confirms that failure modes are determined by ambiguity type rather than model architecture. Ambiguity blindness is universally confirmed across all five models, and interestingly, awareness inversely correlates with action-orientation, with frontier models showing the lowest awareness—this could be a key theoretical insight for the discussion. The layer mechanism becomes clearer with the five-model data: linguistic layers tend toward misparsing while specification layers guess-and-act.

Now I'm setting up the reliability testing framework with 30 clauses across 3 replicates and 2 conditions tested on multiple models, generating over 360 episodes to calculate intraclass correlation coefficients for violation rates and examining how consistently each model performs across repeated tests. Generating ICC summary table... Generating metrics table... Looking at the Kolmogorov-Smirnov test results across all four linguistic features—sentence length, parse depth, readability, and type-token ratio—none show statistical significance, confirming that the synthetic ambiguity injection maintains ecological validity with the natural DRIP-R data. The clause generation process adhered to established quality standards, which explains why the distributional properties align so closely. 过人工审查，确保语言学自然度。TTR p=0.09 最接近显著，反映合成 clauses 倾向于使用略多 unique terms 以确保类型区分度，但仍远未达显著水平。该结果有效回应 RC4 (ecological validity) 的核心顾虑。现在看语言学属性对比表，包括句子长度、解析深度、Flesch-Kincaid 等级和类型-词汇比，合成数据与 DRIP-R 在这些维度上的分布都很接近，KS 统计量都不显著。生成重叠密度图来可视化这些属性的分布差异。生态有效性通过验证——合成 clauses 与 DRIP-R 自然歧义在核心语言学维度上不可区分，直接回应了 RC4 的关键问题。

现在设计 judge 标定流程：从 100 个 episodes 进行分层抽样，涵盖 6 种类型、5 个模型和 2 种条件，每个单元约 1.7 个样本，由 2 名人工标注员进行评估。人工标注员间一致性达到 0.87 kappa 和 93% 同意率，judge 对人工标注的精度为 0.91、召回率 0.89、F1 分数 0.90，总体准确率 0.91，在各严重程度等级上也保持一致的高性能。

不同 judge 模型（GPT-5.4 和 GPT-4.1）的表现略有差异，但都与人工标注保持良好的一致性，同时存在轻微的过度检测偏差（假正例率高 2.3 个百分点），但这种偏差极小，不会影响主要结论。 Generating calibration table... Now I'm looking at a confusion matrix heatmap that visualizes how the judge's predictions align with human ground truth across the three severity tiers. The analysis shows that judge calibration is critical—with Cohen's kappa at 0.87 and F1 at 0.90, the entire measurement chain from episode to trace to judgment to violation label is validated. Borderline cases naturally have lower performance at F1=0.80 due to inherent ambiguity, but clear violations hit F1=0.93, which ensures precise measurement of binary effect sizes—this gets reported in the methods section as standard practice.

For the perturbation control arm, I'm setting up 120 episodes across 30 clause pairs with synonym and reordering variations tested on two models. The metrics show the original violation rate at 4.2% rising to 7.5% under perturbation, yielding a 3.33 percentage point delta with a confidence interval that includes zero, suggesting the effect isn't statistically significant—though the ambiguity-specific delta reaches 36.5 percentage points, which is substantial.

Now I'm looking at the breakdown across perturbation types and the overall verdict. The net delta is 33.2 percentage points with a ratio of 0.091, well below the 0.15 threshold. The synonym and reordering perturbations show smaller individual effects at 4.2 and 2.5 percentage points respectively. The test passes the criteria since the perturbation delta stays under 5 percentage points and the confidence interval contains zero, indicating robust control over general brittleness while the ambiguity effect remains clearly distinguishable. 这是 agent safety 文献中首次采用 perturbation control 来隔离因果效应，完成了 C1 推断框架的最后验证。我正在查看各个扰动条件下的违规率数据——原始条款作为基线，同义词替换和子句重排都产生了统计上不显著的效应，而这些结果与之前的分析一致。

现在对比歧义条件下的巨大效应差异，我需要通过五层评估标准来判断这个模型是否真正稳健。

扰动控制通过了所有关键检验，证明观测到的二元效应中超过90%源于歧义而非其他因素，这直接支撑了论文中关于因果证据的最强表述。这也回应了审稿意见中关于提示敏感性混淆的担忧——这是论文方法论上最有力的一点。接下来我要评估DeBERTa-v3-large分类器的表现。 Now I'm comparing against baseline models—random and keyword-based approaches score much lower, while GPT-4 zero-shot reaches 0.71, so the fine-tuned DeBERTa at 0.877 F1 shows meaningful improvement. The error analysis reveals that coreferential cases get confused with unambiguous examples due to relative clause attachment subtleties, with a false negative rate around 14.6%. The per-type performance follows a clear hierarchy where specification-layer ambiguities are detected most reliably while linguistic-layer types like lexical and coreferential are more challenging. ical 0.83, coreferential 0.80) 更容易检测，
      因为 spec-layer ambiguity 通常涉及更明显的结构性缺失或模糊（词汇标记更明显），
      而 ling-layer ambiguity 的 surface form 更接近正常文本。
      Coreferential 最难检测 (F1=0.80)——与 C2 中 coreferential 作为 boundary case 的角色一致：
      其 ambiguity 最 subtle，连 human annotators 都有更多 disagreement。
      GPT-4 zero-shot F1=0.71 表明 LLMs 本身不是好的 ambiguity detector（与 Ambiguity Blindness 一致），
      而 fine-tuned DeBERTa 显著优于 zero-shot 大模型。现在看一下分类器的具体性能指标，包括 DeBERTa、GPT-4 zero-shot、关键词基线和随机基线在 F1、精确率、召回率和 AUROC 上的表现，以及按类型划分的 F1 分数。

Generating performance tables... models 可以通过微调来弥补这一差距。现在我需要确保YAML结构完整且所有指标都在规定范围内，逐一验证关键数值是否符合要求。 All the validation checks are passing, so I'm ready to generate the YAML output now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebb99c75-d314-4fb3-a285-939d7f835aaf",
  "isSidechain": false,
  "requestId": "req_011CbF4fMMZJq18sNmSLmBiP",
  "type": "assistant",
  "uuid": "eae7719a-6ad2-40a8-a60b-7d1d9af5750d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "4845fed2-f1aa-4e34-aca2-048b635bbadb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017yQahDgNrssPAcWhkVXMgY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19353,
      "cache_read_input_tokens": 11447,
      "output_tokens": 34180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19353,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 34180,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 19353,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19353
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

_source line 10 · 2026-05-21T04:23:52.232Z_

```yaml
tier: best
narrative_guidance: >
  Differential Nocuity 框架完全成立。三层叙事：
  (1) Policy ambiguity universally nocuous — +34.0pp causal effect across 5 architecturally diverse models，
  matched-pair + perturbation control PASS (Δ_perturb=3.33pp) 构成 agent safety 文献中最强因果证据；
  (2) Type hierarchy + model×type interaction 揭示 safety training 的 selective mitigation —
  incompleteness universally dangerous (46-62%)，auth_scope 是 canary type (12%-64% range 52pp)，
  3-tier 结构稳定 (incomp >> mid cluster >> coref)；
  (3) Ambiguity Blindness (<5.2% awareness) + Systematic Nocuity (27% convergent-wrong) 扩展 Berry & Kamsties。
  C3 within-judge 两组均显著 (p=0.021, p=0.038)，layer effect 从 suggestive 升级为 confirmed，
  Disambiguation Channel Framework 获完整实证支撑。所有 claims 原始强度发表，无需降级。EMNLP accept 概率最高。

imagined_experiments:
  - name: "full_study_clause_generation"
    plan_id: "plan_001"
    description: >
      生成 140 新 clauses (coreferential 50, authorization_scope 50, lexical +20, incompleteness +20)，
      验证全部 300 clauses (50/type × 6 types) 的完整性和跨类型平衡。CP 格式混合 labeled + naturalistic。
    expected_results:
      total_clauses_generated: 140
      total_clauses_validated: 300
      clauses_per_type: 50
      quality_pass_rate_pct: 98.6
      clauses_requiring_revision: 4
      cross_type_token_length_cv: 0.12
      avg_ambiguous_token_length: 42.3
      avg_unambiguous_token_length: 58.7
      avg_token_delta: 16.4
      per_type_token_delta:
        incompleteness: 34.6
        authorization_scope: 36.1
        conditional_precedence: 14.2
        scopal: 8.7
        lexical: 5.3
        coreferential: 7.8
      flesch_kincaid_grade: 12.8
      inter_annotator_agreement_kappa: 0.92
      CP_format_mix: "60% labeled / 40% naturalistic"
    result_rationale: >
      Best 档下 clause generation 质量极高：98.6% 一次通过审查（仅 4 条需修订，主要是 auth_scope 边界措辞
      ambiguity 强度不足）。Token delta 呈清晰层级——spec-layer (incomp 34.6, auth 36.1) 消歧所需信息量
      远大于 ling-layer (coref 7.8, lex 5.3)，为后续 info-delta mediator 分析和 Disambiguation Channel
      Framework 提供结构性基础。高 token delta 反映 spec-layer ambiguity 缺乏外部消歧通道——必须通过
      大量额外文本才能消除，而 ling-layer 的 referential/lexical ambiguity 可通过少量 context 消解。
      Annotator κ=0.92 确认 ambiguity 标注的一致性。CP 混合格式避免 format artifact。
    tables:
      - name: "Clause Distribution Summary"
        columns: ["type", "layer", "n", "avg_amb_tokens", "avg_unamb_tokens", "token_delta", "quality_pass"]
        rows:
          - ["incompleteness", "spec", 50, 48.2, 82.8, 34.6, "50/50"]
          - ["authorization_scope", "spec", 50, 44.6, 80.7, 36.1, "48/50"]
          - ["conditional_precedence", "spec", 50, 38.1, 52.3, 14.2, "50/50"]
          - ["scopal", "ling", 50, 36.4, 45.1, 8.7, "50/50"]
          - ["lexical", "ling", 50, 41.7, 47.0, 5.3, "49/50"]
          - ["coreferential", "ling", 50, 44.8, 52.6, 7.8, "49/50"]
    figures_description:
      - "Token delta box plot by type: spec-layer median ~35 tokens vs ling-layer ~7 tokens, non-overlapping IQR"
    analysis: >
      300 clause pairs 全部通过验证。Spec-layer 平均 token delta 28.3 vs ling-layer 7.3 (t=14.2, p<0.001)，
      为 C3 info-delta mediator 提供基础。Auth_scope 和 incompleteness 的高 token delta 是 spec-layer
      缺乏外部消歧通道的直接 operationalization。

  - name: "new_type_mini_pilot"
    plan_id: "plan_001b"
    description: >
      Coreferential + authorization_scope mini-pilot：5 clauses/type × 2 conditions × 1 model (gpt-5.4) = 20 episodes。
    expected_results:
      total_episodes: 20
      coreferential_amb_violation_rate: 0.20
      coreferential_unamb_violation_rate: 0.00
      coreferential_delta_pp: 20.0
      auth_scope_amb_violation_rate: 0.60
      auth_scope_unamb_violation_rate: 0.00
      auth_scope_delta_pp: 60.0
      design_verdict: "PASS — both types trigger violations, control clean"
    result_rationale: >
      两个新类型在 gpt-5.4 上方向明确：auth_scope 3/5 违规（60%）与后续 full study 64% 高度吻合，
      预示 canary type 特征。Coreferential 1/5（20%）与 full study 18% 一致，验证了 partial disambiguation
      via tool responses 的机制假设——referential ambiguity 下 agent 可从 tool output 获取部分线索。
      Unambiguous 控制组 0% 违规确认 clause design 的 causal validity：是 ambiguity 导致违规，不是
      scenario 本身的 difficulty。N=5 虽小但方向清晰，无需修改 clause design。
    tables:
      - name: "Mini-Pilot Results"
        columns: ["type", "condition", "n", "violations", "rate"]
        rows:
          - ["coreferential", "ambiguous", 5, 1, "20%"]
          - ["coreferential", "unambiguous", 5, 0, "0%"]
          - ["authorization_scope", "ambiguous", 5, 3, "60%"]
          - ["authorization_scope", "unambiguous", 5, 0, "0%"]
    figures_description: []
    analysis: >
      PASS。Auth_scope 60% 违规率在 gpt-5.4 上为 C4 star finding 提供先兆。
      Coreferential 20% 处于预期低端，与 disambiguation channel 假设一致。直接进入 full study。

  - name: "full_study_api"
    plan_id: "plan_002"
    description: >
      300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6) = 1,800 episodes。
      Cross-judge evaluation（gpt-5.4 judged by gpt-4.1，gpt-4.1 + Claude judged by gpt-5.4）。
    expected_results:
      total_episodes: 1800
      episodes_completed: 1794
      episode_completion_rate: 0.997
      overall_amb_violation_rate: 0.373
      overall_unamb_violation_rate: 0.040
      overall_binary_effect_pp: 33.3
      per_model:
        gpt_5_4: {amb: 0.410, unamb: 0.027, delta_pp: 38.3, OR: 25.1, OR_CI: "[14.2, 44.3]", p: "<1e-25", judge: "gpt-4.1"}
        gpt_4_1: {amb: 0.407, unamb: 0.060, delta_pp: 34.7, OR: 10.8, OR_CI: "[7.0, 16.7]", p: "<1e-20", judge: "gpt-5.4"}
        claude: {amb: 0.303, unamb: 0.046, delta_pp: 25.7, OR: 9.0, OR_CI: "[5.7, 14.2]", p: "<1e-17", judge: "gpt-5.4"}
      per_type_amb_3model:
        incompleteness: 0.507
        authorization_scope: 0.407
        lexical: 0.360
        scopal: 0.373
        conditional_precedence: 0.353
        coreferential: 0.240
      cross_judge_kappa: 0.91
    result_rationale: >
      3 API 模型全部呈现强烈 binary effect：Claude 最低 +25.7pp 但仍 p<1e-17——即使最安全的模型也无法
      免疫 policy ambiguity。GPT-5.4 和 gpt-4.1 的 OR (25.1, 10.8) 差异反映 frontier vs mid-tier 的
      unambiguous baseline 差异（gpt-5.4 仅 2.7% vs gpt-4.1 6.0%），而 ambiguous 条件下两者接近 (41% vs 40.7%)。
      Auth_scope 跨 3 模型已显示 52pp 极差（Claude 12% vs GPT-5.4 64%），C4 interaction 的种子数据。
      Cross-judge κ=0.91 确认两个 judge 模型的判定几乎完全一致，不引入 measurement artifact。
    tables:
      - name: "Per-Model Binary Effect (3 API Models)"
        columns: ["model", "N", "amb_rate", "unamb_rate", "Δpp", "OR", "95% CI", "p"]
        rows:
          - ["GPT-5.4", 600, "41.0%", "2.7%", "+38.3", "25.1", "[14.2, 44.3]", "<1e-25"]
          - ["GPT-4.1", 600, "40.7%", "6.0%", "+34.7", "10.8", "[7.0, 16.7]", "<1e-20"]
          - ["Claude-sonnet-4-6", 600, "30.3%", "4.6%", "+25.7", "9.0", "[5.7, 14.2]", "<1e-17"]
      - name: "Per-Type Violation Rates (API, Ambiguous Only)"
        columns: ["type", "GPT-5.4", "GPT-4.1", "Claude", "3-model avg"]
        rows:
          - ["incompleteness", "46%", "58%", "48%", "50.7%"]
          - ["authorization_scope", "64%", "46%", "12%", "40.7%"]
          - ["lexical", "42%", "34%", "32%", "36.0%"]
          - ["scopal", "42%", "38%", "32%", "37.3%"]
          - ["conditional_precedence", "34%", "36%", "36%", "35.3%"]
          - ["coreferential", "18%", "32%", "22%", "24.0%"]
    figures_description:
      - "Forest plot: per-model binary effect with bootstrap 95% CI, all CIs well above zero"
    analysis: >
      1,800 episodes 数据完整（99.7% completion）。Binary effect 跨模型一致，auth_scope 极差已达 52pp，
      type hierarchy 初步呈现 incomp >> coref 模式。为 plan_003 open-source 扩展提供 baseline。

  - name: "full_study_opensource"
    plan_id: "plan_003"
    description: >
      300 clauses × 2 conditions × 2 open-source models (Qwen3-235B, DeepSeek-V3) via OpenRouter = 1,200 episodes。
    expected_results:
      total_episodes: 1200
      episodes_completed: 1192
      episode_completion_rate: 0.993
      per_model:
        qwen3: {amb: 0.431, unamb: 0.007, delta_pp: 32.4, OR: 17.3, OR_CI: "[10.1, 29.5]", p: "<1e-22", judge: "gpt-5.4"}
        deepseek: {amb: 0.497, unamb: 0.007, delta_pp: 39.0, OR: 22.8, OR_CI: "[13.3, 39.1]", p: "<1e-27", judge: "gpt-4.1"}
      per_type_amb:
        qwen3: {incomp: 0.62, auth: 0.26, lex: 0.52, scopal: 0.37, CP: 0.40, coref: 0.42}
        deepseek: {incomp: 0.54, auth: 0.60, lex: 0.54, scopal: 0.48, CP: 0.38, coref: 0.44}
    result_rationale: >
      两个 open-source 模型 binary effect 均极强（Qwen3 +32.4pp, DeepSeek +39.0pp），5/5 模型 replication 完成。
      DeepSeek 整体违规率最高（49.7%）且各类型分布均匀（range 仅 16pp，χ²=6.31 n.s.），反映其 safety training
      缺乏 type-specific 针对性——与 Claude 的 selective vulnerability (V=0.24, range 36pp) 形成鲜明对比，
      直接支撑 C4 "safety training selectivity" 论点。Qwen3 展现独特 profile：incomp 最高（62%）但
      auth_scope 仅 26%——open-source MoE 架构也能对 authorization boundary 产生 partial protection，
      但无法应对 information gap。两模型 unambiguous baseline 极低（0.7%），说明 open-source 模型在
      unambiguous 条件下几乎不违规，ambiguity 是 violation 的 sufficient cause。
    tables:
      - name: "Per-Model Binary Effect (Open-Source)"
        columns: ["model", "N", "amb_rate", "unamb_rate", "Δpp", "OR", "95% CI", "p"]
        rows:
          - ["Qwen3-235B", 600, "43.1%", "0.7%", "+32.4", "17.3", "[10.1, 29.5]", "<1e-22"]
          - ["DeepSeek-V3", 600, "49.7%", "0.7%", "+39.0", "22.8", "[13.3, 39.1]", "<1e-27"]
      - name: "Per-Type Violation Rates (Open-Source, Ambiguous Only)"
        columns: ["type", "Qwen3", "DeepSeek"]
        rows:
          - ["incompleteness", "62%", "54%"]
          - ["authorization_scope", "26%", "60%"]
          - ["lexical", "52%", "54%"]
          - ["scopal", "37%", "48%"]
          - ["conditional_precedence", "40%", "38%"]
          - ["coreferential", "42%", "44%"]
    figures_description:
      - "Radar chart: Qwen3 (peaked at incomp) vs DeepSeek (uniform polygon) vulnerability profiles"
    analysis: >
      Open-source 扩展完成 5-model replication。DeepSeek 的 uniform high vulnerability 是 C4 的关键对比组。
      Combined with API data → 2,997 episodes ready for plan_004 统计分析。

  - name: "full_study_analysis"
    plan_id: "plan_004"
    description: >
      2,997 episodes 统计分析：C1 binary effect + bootstrap CI, C2 omnibus χ² + TOST + power,
      C3 layer effect + within-judge subgroup, C4 model×type interaction + logistic regression + Fleiss κ,
      info-delta mediator, inter-model agreement / systematic nocuity。
    expected_results:
      total_episodes: 2997
      C1_binary_effect_pp: 34.0
      C1_bootstrap_CI: [31.2, 36.9]
      C1_mcnemar_OR: 15.1
      C1_mcnemar_OR_CI: [10.78, 21.17]
      C1_all_5_models_significant: true
      C1_min_effect_pp: 25.7
      C1_max_effect_pp: 39.0
      C1_logistic_condition_coef: 2.278
      C1_logistic_condition_z: 19.65
      C2_omnibus_chi2: 28.02
      C2_omnibus_p: "3.6e-5"
      C2_cramers_V: 0.137
      C2_power: 0.993
      C2_MDE: 0.093
      C2_incomp_rate: 0.536
      C2_coref_rate: 0.316
      C2_incomp_minus_coref_pp: 22.0
      C2_3tier: "High (53.6%) >> Mid (36.8-42.8%) >> Low (31.6%)"
      C2_TOST_15pp_equiv: "8/15"
      C2_TOST_10pp_equiv: "4/15"
      C3_spec_rate: 0.440
      C3_ling_rate: 0.379
      C3_gap_pp: 6.08
      C3_gap_CI: [1.14, 11.02]
      C3_chi2: 5.73
      C3_p: 0.017
      C3_V: 0.062
      C3_OR: 1.29
      C3_within_judge_group1: {delta_pp: 9.5, p: 0.021, models: "GPT-5.4 + DeepSeek", judge: "gpt-4.1"}
      C3_within_judge_group2: {delta_pp: 6.8, p: 0.038, models: "GPT-4.1 + Claude + Qwen3", judge: "gpt-5.4"}
      C3_per_model_gap:
        gpt_5_4: +14.0
        gpt_4_1: +12.0
        claude: +3.3
        deepseek: +2.0
        qwen3: -0.9
      C4_model_chi2: 31.02
      C4_model_p: "3.0e-6"
      C4_model_V: 0.102
      C4_amb_only_chi2: 24.01
      C4_amb_only_p: "7.9e-5"
      C4_auth_scope_range_pp: 52
      C4_incomp_range_pp: 16
      C4_CP_range_pp: 6
      C4_fleiss_kappa: 0.384
      C4_per_model_type_chi2:
        gpt_5_4: {chi2: 23.44, p: 0.0003, V: 0.28}
        claude: {chi2: 17.87, p: 0.003, V: 0.24}
        qwen3: {chi2: 15.89, p: 0.007, V: 0.23}
        gpt_4_1: {chi2: 9.89, p: 0.078, V: 0.18}
        deepseek: {chi2: 6.31, p: 0.277, V: 0.14}
      info_delta_coef: 0.022
      info_delta_z: 3.49
      info_delta_p: 0.0005
      systematic_nocuity_rate: 0.27
      divergent_nocuity_rate: 0.42
      innocuous_rate: 0.31
    result_rationale: >
      Best 档所有检验达到预设阈值：
      C1: +34.0pp (OR=15.1) 落入 [30,40] 中部，5/5 模型全部 p<1e-17，logistic regression 中 condition_amb
      系数 2.278 是绝对主导，即使控制 token delta、model、type 后不变——ambiguity 是 violation 的 primary driver。
      C2: omnibus p=3.6e-5 落入 [1e-6, 1e-4]，V=0.137 虽 <0.20 但 power=0.993 (MDE=0.093 < 0.137)
      排除 underpowered 解释。3-tier 在 TOST ±15pp 下 8/15 equivalent 确认 mid-tier clustering，
      ±10pp 仅 4/15 equivalent 证明 types 绝非可互换。Incomp-coref gap 22pp 落入 [18,28]。
      C3 关键升级——within-judge 两组均显著：Group1 (gpt-4.1 judged, GPT-5.4+DeepSeek) Δ=9.5pp p=0.021，
      Group2 (gpt-5.4 judged, GPT-4.1+Claude+Qwen3) Δ=6.8pp p=0.038。这实现因为 Group1 中 DeepSeek 的
      高 spec rate (50.7%) 与 GPT-5.4 的强 layer gap (+14pp) 共同拉动；Group2 中 GPT-4.1 (+12pp) 
      补偿了 Claude (+3.3pp) 和 Qwen3 (-0.9pp) 的弱/反转 gap。Best 档数据恰好落在两组均过 0.05 的区间。
      C4 star finding：auth_scope 52pp range 正中 [40,55]，Fleiss κ=0.384 ("fair") 在 [0.3,0.45] 内——
      low agreement 本身就是核心发现，证明 which-clauses-trigger 是 model-dependent。
      Per-model type χ² 揭示 gradient：GPT-5.4 (V=0.28) > Claude (0.24) > Qwen3 (0.23) >> GPT-4.1 (0.18, borderline) >> DeepSeek (0.14, n.s.)。
      DeepSeek 的 n.s. 意味着它 uniformly vulnerable——safety training blind spot 最大。
      Systematic nocuity 27% 是 B&K 扩展的独立贡献：所有模型 converge on same wrong reading，比 divergent 更危险。
    tables:
      - name: "C1 Per-Model Binary Effect (5 Models)"
        columns: ["model", "N", "amb%", "unamb%", "Δpp", "OR", "95% CI", "p"]
        rows:
          - ["DeepSeek-V3", 600, "49.7%", "0.7%", "+39.0", "22.8", "[13.3, 39.1]", "<1e-27"]
          - ["GPT-5.4", 600, "41.0%", "2.7%", "+38.3", "25.1", "[14.2, 44.3]", "<1e-25"]
          - ["GPT-4.1", 600, "40.7%", "6.0%", "+34.7", "10.8", "[7.0, 16.7]", "<1e-20"]
          - ["Qwen3-235B", 600, "43.1%", "0.7%", "+32.4", "17.3", "[10.1, 29.5]", "<1e-22"]
          - ["Claude-sonnet-4-6", 600, "30.3%", "4.6%", "+25.7", "9.0", "[5.7, 14.2]", "<1e-17"]
          - ["**Pooled**", "**2997**", "**40.9%**", "**2.9%**", "**+34.0**", "**15.1**", "**[10.78, 21.17]**", "**<1e-50**"]
      - name: "C2 Type Hierarchy (Ambiguous Only, 5 Models Pooled)"
        columns: ["type", "layer", "N_amb", "viol%", "tier", "95% CI"]
        rows:
          - ["incompleteness", "spec", 250, "53.6%", "HIGH", "[47.4, 59.8]"]
          - ["lexical", "ling", 250, "42.8%", "MID", "[36.7, 48.9]"]
          - ["authorization_scope", "spec", 250, "41.6%", "MID", "[35.5, 47.7]"]
          - ["scopal", "ling", 250, "39.4%", "MID", "[33.4, 45.4]"]
          - ["conditional_precedence", "spec", 250, "36.8%", "MID", "[30.8, 42.8]"]
          - ["coreferential", "ling", 250, "31.6%", "LOW", "[25.8, 37.4]"]
      - name: "C3 Within-Judge Layer Analysis"
        columns: ["group", "judge", "models", "spec%", "ling%", "Δpp", "p"]
        rows:
          - ["Group 1", "gpt-4.1", "GPT-5.4 + DeepSeek", "49.3%", "39.8%", "+9.5", "0.021"]
          - ["Group 2", "gpt-5.4", "GPT-4.1 + Claude + Qwen3", "40.4%", "33.6%", "+6.8", "0.038"]
          - ["**Pooled**", "—", "All 5", "44.0%", "37.9%", "**+6.08**", "**0.017**"]
      - name: "C4 Model×Type Interaction Matrix (Ambiguous, Violation %)"
        columns: ["type", "GPT-5.4", "GPT-4.1", "Claude", "Qwen3", "DeepSeek", "range"]
        rows:
          - ["authorization_scope", "64%", "46%", "12%", "26%", "60%", "52pp"]
          - ["coreferential", "18%", "32%", "22%", "42%", "44%", "26pp"]
          - ["lexical", "42%", "34%", "32%", "52%", "54%", "22pp"]
          - ["incompleteness", "46%", "58%", "48%", "62%", "54%", "16pp"]
          - ["scopal", "42%", "38%", "32%", "37%", "48%", "16pp"]
          - ["conditional_precedence", "34%", "36%", "36%", "40%", "38%", "6pp"]
      - name: "C4 Per-Model Type Differentiation"
        columns: ["model", "within-model χ²", "p", "V", "interpretation"]
        rows:
          - ["GPT-5.4", "23.44", "0.0003", "0.28", "Strong differentiation (high auth, low coref)"]
          - ["Claude", "17.87", "0.003", "0.24", "Strong (very low auth, moderate others)"]
          - ["Qwen3", "15.89", "0.007", "0.23", "Moderate (high incomp+lex, low auth)"]
          - ["GPT-4.1", "9.89", "0.078", "0.18", "Borderline"]
          - ["DeepSeek", "6.31", "0.277", "0.14", "Not significant — uniformly high"]
    figures_description:
      - "Figure 2: Forest plot — 6-type binary effect sizes + 95% CI, all excluding zero"
      - "Figure 3: 5×6 heatmap — model×type violation rates, blue (12%) to red (64%), auth_scope row shows maximum contrast"
      - "TOST diagram: 15 pairwise comparisons at ±15pp, showing 8 equivalent (dashed) vs 7 non-equivalent (solid)"
      - "Systematic nocuity pie: 27% all-converge-wrong, 42% divergent, 31% innocuous"
    analysis: >
      C1-C4 全部达到 best 档。关键 differentiator 是 C3 within-judge 两组均 p<0.05（median/worst 档
      此处 fail 导致 layer effect 降级为 suggestive）。C4 interaction 矩阵展示 auth_scope 作为 safety
      training 最敏感探针——Claude RLHF 对 authorization boundary 的针对性训练显著降低该类型违规率，
      而 DeepSeek 缺乏此类针对性（V=0.14 n.s.）。Systematic nocuity 27% 为 B&K 理论扩展独立贡献。

  - name: "error_analysis"
    plan_id: "plan_005"
    description: >
      5 model × 6 type 的违规 trace 定性分析：450 traces 的 failure mode 分类、type-specific signatures、
      cross-model consistency、Ambiguity Blindness 量化、cross-domain consistency、layer mechanism。
    expected_results:
      total_traces: 450
      traces_per_model: 90
      failure_mode_categories: 4
      C5_awareness_rate_pct: 5.2
      C5_awareness_per_model:
        gpt_5_4: 4.1
        gpt_4_1: 10.7
        claude: 6.3
        qwen3: 3.8
        deepseek: 2.9
      C5_surface_adoption_pct: 91.3
      C5_escalate_to_user_pct: 0.7
      cross_model_dominant_mode_consistency: "5/6 types"
      divergent_type: "coreferential (flat distribution)"
      type_signatures:
        auth_scope: {dominant: "unauthorized_escalation", pct: 76}
        incompleteness: {dominant: "assumption_based_action", pct: 63}
        scopal: {dominant: "scope_misapplication", pct: 74}
        lexical: {dominant: "assumption_based_action", pct: 65}
        conditional_precedence: {dominant: "scope_misapplication", pct: 38, secondary: "arbitrary_rule_selection 28%"}
        coreferential: {dominant: "mixed", note: "scope_mis 31%, assumption 29%, unauth_esc 18%"}
      ling_scope_misapplication_avg: 0.39
      spec_scope_misapplication_avg: 0.15
      spec_escalation_plus_assumption_avg: 0.72
      cross_domain_max_delta_pp: 12.5
      coreferential_conservative_refusal: 0.085
      other_avg_conservative_refusal: 0.025
      gwets_AC1: 0.73
      cohens_kappa_4cat: 0.594
      raw_agreement_pct: 80
    result_rationale: >
      Best 档下 5-model 扩展（450 traces vs 2-model 245 traces）验证了 type-specific failure signatures
      的 cross-model stability。5/6 types 在全部 5 模型上共享 dominant failure mode——概率极低 by chance
      (binomial p < 0.001 for 5/5 agreement on each type)，确认 failure modes are type-determined, not model-determined。
      Auth_scope → unauthorized_escalation 76% (5-model pooled) 说明模型在模糊授权边界下系统性越权，
      而非保守拒绝或随机猜测。Incompleteness → assumption_based_action 63% 反映 "guess-and-act" 策略：
      信息不足时模型 impute missing conditions 而非 escalate to user。
      Ambiguity Blindness 5.2% awareness 跨 5 模型 universally confirmed。Nuance：frontier (GPT-5.4 4.1%)
      比 mid-tier (GPT-4.1 10.7%) awareness 更低——action-oriented frontier models 更少 hesitate，
      直接 surface-adopt ambiguous interpretation。DeepSeek (2.9%) 最低——与其 uniform vulnerability (C4) 一致。
      Coreferential flat distribution + high conservative_refusal (8.5%) 支撑 Disambiguation Channel：
      referential ambiguity 下 tool responses 提供 partial cues，使 agent 策略更多样化。
      Gwet's AC1=0.73 解决 kappa paradox（Cohen's κ=0.594 被 prevalence 压低），为 automated coding 提供 adequate validity。
    tables:
      - name: "Failure Mode × Type (5-Model Pooled, %)"
        columns: ["type", "unauth_escalation", "assumption_action", "scope_misapplication", "arbitrary_rule"]
        rows:
          - ["auth_scope", "76%", "12%", "7%", "5%"]
          - ["incompleteness", "18%", "63%", "11%", "8%"]
          - ["scopal", "8%", "14%", "74%", "4%"]
          - ["lexical", "6%", "65%", "22%", "7%"]
          - ["cond_precedence", "16%", "18%", "38%", "28%"]
          - ["coreferential", "18%", "29%", "31%", "22%"]
      - name: "Ambiguity Blindness (5 Models)"
        columns: ["model", "awareness%", "surface_adopt%", "escalate_user%", "conserv_refusal%"]
        rows:
          - ["GPT-5.4", "4.1%", "92.4%", "0.3%", "2.1%"]
          - ["GPT-4.1", "10.7%", "85.6%", "1.6%", "3.2%"]
          - ["Claude", "6.3%", "89.2%", "0.8%", "4.7%"]
          - ["Qwen3", "3.8%", "93.1%", "0.2%", "1.8%"]
          - ["DeepSeek", "2.9%", "95.2%", "0.1%", "1.4%"]
          - ["**Pooled**", "**5.2%**", "**91.3%**", "**0.7%**", "**2.6%**"]
      - name: "Cross-Model Dominant Mode Consistency"
        columns: ["type", "GPT-5.4", "GPT-4.1", "Claude", "Qwen3", "DeepSeek", "5/5?"]
        rows:
          - ["auth_scope", "unauth_esc", "unauth_esc", "unauth_esc", "unauth_esc", "unauth_esc", "✓"]
          - ["incompleteness", "assumption", "assumption", "assumption", "assumption", "assumption", "✓"]
          - ["scopal", "scope_mis", "scope_mis", "scope_mis", "scope_mis", "scope_mis", "✓"]
          - ["lexical", "assumption", "assumption", "assumption", "assumption", "assumption", "✓"]
          - ["cond_prec", "scope_mis", "scope_mis", "scope_mis", "arb_rule", "scope_mis", "4/5"]
          - ["coreferential", "scope_mis", "assumption", "assumption", "scope_mis", "scope_mis", "✗ flat"]
    figures_description:
      - "Figure 5: Stacked bar per type — sharp type-specific profiles (auth→red, incomp→blue, scopal→green)"
      - "Figure 6: 5-panel side-by-side per-model failure mode distributions showing convergence"
      - "Figure 7: Annotated trace pair — CP explicit conflict detection vs scopal blind surface adoption"
    analysis: >
      5-model error analysis 是 best 档 EMNLP 最高贡献之一。Type-specific failure signatures 的 5-model
      replication 将 C5 从 "2-model anecdotal" 升级为 "5-model systematic"。Layer mechanism
      (ling→misparse 39% vs spec→guess+escalate 72%) 为 Disambiguation Channel Framework 提供
      failure-mode-level evidence。Ambiguity Blindness 跨 5 模型 confirmed 且 awareness inversely
      correlates with action-orientation，可作为 Discussion theoretical insight。

  - name: "reliability_test"
    plan_id: "plan_006"
    description: >
      30 clauses × 3 replicates × 2 conditions × 2 models = 360 episodes 的 test-retest ICC 分析。
    expected_results:
      total_episodes: 360
      overall_ICC: 0.919
      overall_ICC_CI: [0.892, 0.940]
      binary_ICC: 0.847
      binary_ICC_CI: [0.803, 0.883]
      per_model_ICC:
        gpt_5_4: 0.921
        gpt_4_1: 0.918
      per_type_ICC:
        scopal: 0.989
        lexical: 0.981
        coreferential: 0.976
        authorization_scope: 0.857
        conditional_precedence: 0.856
        incompleteness: 0.807
      avg_bootstrap_CI_width_pp: 7.2
      max_bootstrap_CI_width_pp: 11.4
    result_rationale: >
      Best 档下 ICC=0.919 (excellent) 彻底消除 sampling noise 顾虑。Per-clause violation rates 在
      3 次独立重复中高度 stable，±8pp 波动在 ICC CI 范围内完全预期。
      关键 convergent evidence：ling-layer ICC (0.976-0.989 excellent) 系统性高于 spec-layer ICC
      (0.807-0.857 good)。这独立于 violation rate 分析，从 behavioral reproducibility 角度支撑
      Disambiguation Channel Framework：ling-layer 有外部消歧通道→agent 行为更 deterministic→ICC 更高；
      spec-layer 无外部消歧→agent 被迫 guess→行为更 stochastic→ICC 较低。
      Incompleteness ICC 最低（0.807）与其 highest violation rate (53.6%) 的组合特别有理论价值——
      信息完全缺失时 agent 的 guessing strategy 最不稳定，正是因为没有任何 signal 可锚定。
      Bootstrap CI 平均宽度 7.2pp < 10pp 目标，绝大多数比较有足够精度。
    tables:
      - name: "ICC Summary"
        columns: ["metric", "ICC", "95% CI", "interpretation"]
        rows:
          - ["Overall (continuous)", "0.919", "[0.892, 0.940]", "Excellent"]
          - ["Binary", "0.847", "[0.803, 0.883]", "Good"]
          - ["GPT-5.4 only", "0.921", "[0.889, 0.946]", "Excellent"]
          - ["GPT-4.1 only", "0.918", "[0.884, 0.944]", "Excellent"]
      - name: "Per-Type ICC (Layer Convergent Evidence)"
        columns: ["type", "layer", "ICC", "interp"]
        rows:
          - ["scopal", "ling", "0.989", "Excellent"]
          - ["lexical", "ling", "0.981", "Excellent"]
          - ["coreferential", "ling", "0.976", "Excellent"]
          - ["authorization_scope", "spec", "0.857", "Good"]
          - ["conditional_precedence", "spec", "0.856", "Good"]
          - ["incompleteness", "spec", "0.807", "Good"]
    figures_description:
      - "ICC bar chart with layer coloring: ling types (blue, >0.97) cleanly separated from spec types (orange, ~0.82-0.86)"
    analysis: >
      ICC=0.919 是 methodological anchor。Layer-stratified ICC 提供与 violation rate 完全独立的
      convergent evidence for Disambiguation Channel Framework。Paper 中同时在 §4 (reliability) 和
      §7 (theoretical support) 引用。

  - name: "realism_validation"
    plan_id: "plan_007"
    description: >
      合成 clause 与 DRIP-R 自然 ambiguity 的语言学属性比较：sentence length, parse depth,
      Flesch-Kincaid, TTR + KS 检验。
    expected_results:
      n_synthetic: 300
      n_drip_r: 147
      sentence_length_ks_p: 0.23
      parse_depth_ks_p: 0.18
      flesch_kincaid_ks_p: 0.41
      ttr_ks_p: 0.09
      any_significant: false
      synthetic_means: {sent_len: 24.3, parse_depth: 5.7, fk_grade: 12.8, ttr: 0.71}
      drip_r_means: {sent_len: 22.8, parse_depth: 5.4, fk_grade: 13.2, ttr: 0.68}
      verdict: "PASS — no significant distributional differences"
    result_rationale: >
      Best 档下 4 项 KS 检验均 n.s. (all p > 0.05)，合成 clauses 与 DRIP-R 自然 ambiguity 在
      核心语言学维度上统计不可区分。这归因于 clause generation 遵循 Chantree-style 标准 +
      plan_001 人工审查确保自然度。Sentence length 和 parse depth 几乎完全匹配（Δ < 6%）。
      TTR p=0.09 最接近显著，反映合成 clauses 为确保类型区分度使用了略多 unique terms，
      但远未达显著水平。Flesch-Kincaid 差异最小（12.8 vs 13.2），说明可读性水平一致。
      该结果直接回应 RC4 (ecological validity)：合成注入不引入 distributional artifact。
    tables:
      - name: "Linguistic Property Comparison"
        columns: ["property", "synthetic (mean±SD)", "DRIP-R (mean±SD)", "KS stat", "p"]
        rows:
          - ["Sentence length (tokens)", "24.3±8.1", "22.8±7.6", "0.087", "0.23"]
          - ["Parse depth", "5.7±1.9", "5.4±1.7", "0.094", "0.18"]
          - ["Flesch-Kincaid grade", "12.8±2.4", "13.2±2.6", "0.072", "0.41"]
          - ["Type-token ratio", "0.71±0.08", "0.68±0.09", "0.112", "0.09"]
    figures_description:
      - "Overlapping density plots: synthetic (blue) vs DRIP-R (orange) per property, KS p annotated"
    analysis: >
      Ecological validity PASS。报告在 §4 Materials。合成 clauses 在语言学分布上与 natural ambiguity 一致。

  - name: "judge_calibration"
    plan_id: "plan_009"
    description: >
      100 episodes stratified sampling + 2 human annotators + judge precision/recall/F1 against human ground truth。
    expected_results:
      n_sampled: 100
      n_human_annotators: 2
      human_kappa: 0.87
      human_agreement_pct: 93
      judge_precision: 0.91
      judge_recall: 0.89
      judge_F1: 0.90
      judge_accuracy: 0.91
      per_severity:
        clear_violation: {prec: 0.94, rec: 0.92, F1: 0.93}
        borderline: {prec: 0.78, rec: 0.82, F1: 0.80}
        no_violation: {prec: 0.93, rec: 0.91, F1: 0.92}
      per_judge_model:
        gpt_5_4_judge: {F1: 0.91, kappa_vs_human: 0.84}
        gpt_4_1_judge: {F1: 0.88, kappa_vs_human: 0.81}
      bias: "slight over-detection (+2.3pp FPR vs human)"
      cross_judge_asymmetry_pp: 3.1
    result_rationale: >
      Best 档下 human κ=0.87 远超 0.75 目标，证明 violation 判定标准清晰可操作——human annotators
      在 93% episodes 上一致。Judge F1=0.90 落入 [0.85, 0.95] 中部，验证 LLM-as-judge measurement chain。
      Clear violation F1=0.93 是核心：binary effect 计算依赖的 violation/no-violation 分类精度极高，
      measurement error 对 +34.0pp effect size 的影响可忽略。Borderline F1=0.80 是预期内的——
      ambiguity 本身在 violation/no-violation boundary 创造灰色地带，这些 cases 在 binary analysis 中
      被吸收为 noise 而非 systematic bias。
      两个 judge 的 F1 差异 3pp (0.91 vs 0.88) 和 asymmetry 3.1pp 远小于 effect sizes，
      确认 cross-judge design 不引入系统偏差。Slight over-detection (+2.3pp FPR) 方向一致，
      不选择性影响特定类型或模型——worst case 使所有 violation rates 高估 ~2pp，不改变任何比较结论。
      这是 Dream best-tier reviewers 认定的 "single most critical missing validation" 的成功交付。
    tables:
      - name: "Judge Calibration Summary"
        columns: ["metric", "value", "target", "status"]
        rows:
          - ["Human κ", "0.87", "≥0.75", "PASS"]
          - ["Judge F1", "0.90", "≥0.85", "PASS"]
          - ["Judge precision", "0.91", "—", "—"]
          - ["Judge recall", "0.89", "—", "—"]
          - ["Cross-judge asymmetry", "3.1pp", "<10pp", "PASS"]
      - name: "Per-Severity Performance"
        columns: ["tier", "N", "precision", "recall", "F1"]
        rows:
          - ["Clear violation", 38, "0.94", "0.92", "0.93"]
          - ["Borderline", 24, "0.78", "0.82", "0.80"]
          - ["No violation", 38, "0.93", "0.91", "0.92"]
    figures_description:
      - "3×3 confusion matrix heatmap: judge vs human, per severity tier"
    analysis: >
      Judge calibration PASS。Human κ=0.87 + Judge F1=0.90 验证完整 measurement chain。
      报告在 §4 Method 作为 standard practice (5/8 distilled papers 均包含)。

  - name: "perturbation_control"
    plan_id: "plan_010"
    description: >
      30 clause pairs (15 synonym + 15 reorder) × 2 conditions × 2 models = 120 episodes。
      区分 ambiguity-specific harm vs general prompt brittleness。
    expected_results:
      total_episodes: 120
      original_viol_rate: 0.042
      perturbed_viol_rate: 0.075
      perturbation_delta_pp: 3.33
      perturbation_CI: [-1.8, 8.5]
      CI_contains_zero: true
      ambiguity_delta_pp: 36.5
      net_delta_pp: 33.2
      ratio: 0.091
      synonym_delta_pp: 4.2
      reorder_delta_pp: 2.5
      CI_width_pp: 10.3
      verdict: "PASS"
    result_rationale: >
      Best 档下 perturbation control 完美 PASS：Δ_perturb=3.33pp (CI [-1.8, 8.5] 含 0) 统计不显著，
      而 ambiguity Δ=36.5pp——ratio 0.091 远低于 0.15 PASS threshold。
      Non-ambiguity surface changes (synonym substitution, clause reordering) 对 violation rate 的影响
      与零不可区分。Synonym Δ=4.2pp 略高于 reorder Δ=2.5pp——某些 synonym 可能引入轻微语义偏移
      （如 "eligible" → "qualified" 在特定 policy context 下有 scope 差异），但仍远低于 5pp 阈值。
      Net effect 33.2pp 是 ambiguity-SPECIFIC causal effect 的最纯净估计，排除了 general prompt
      brittleness 解释。这是 agent safety 文献中首个 perturbation control experiment，构成 C1
      因果推断的最后一环，也是回应 RC11 (prompt sensitivity confound) 的 strongest point。
      CI width 10.3pp < 15pp，无需追加 episodes。
    tables:
      - name: "Perturbation Control Results"
        columns: ["condition", "N", "viol%", "Δpp", "95% CI", "p"]
        rows:
          - ["Original", 60, "4.2%", "—", "—", "—"]
          - ["Synonym subst.", 30, "8.3%", "+4.2", "[-3.1, 11.5]", "0.26"]
          - ["Clause reorder", 30, "6.7%", "+2.5", "[-4.6, 9.6]", "0.49"]
          - ["**All perturbations**", 60, "7.5%", "**+3.33**", "**[-1.8, 8.5]**", "**0.20**"]
          - ["**Ambiguity (ref)**", "—", "—", "**+36.5**", "**[33.0, 40.0]**", "**<1e-50**"]
      - name: "5-Tier Verdict"
        columns: ["criterion", "value", "threshold", "verdict"]
        rows:
          - ["Δ_perturb", "3.33pp", "<5pp", "PASS"]
          - ["CI contains 0", "Yes", "Required", "PASS"]
          - ["Ratio", "0.091", "<0.15", "PASS"]
          - ["CI width", "10.3pp", "<15pp", "OK"]
    figures_description:
      - "Bar chart: ambiguity Δ=36.5pp (red, towering) vs perturbation Δ=3.33pp (grey, CI crossing zero)"
    analysis: >
      Perturbation control PASS 确立 C1 因果 claim 的最强形式。Non-ambiguity perturbation ≈ 0 effect，
      ambiguity ≈ +36.5pp——>90% of observed effect is ambiguity-specific。
      报告在 §5 "Causal Validation" 子节。回应 RC11 的 strongest methodological point。

  - name: "classifier_poc"
    plan_id: "plan_008"
    description: >
      DeBERTa-v3-large binary ambiguity detector PoC：240 training / 60 test pairs，5 epochs fine-tune。
    expected_results:
      model: "DeBERTa-v3-large"
      train_n: 240
      test_n: 60
      test_accuracy: 0.883
      test_F1: 0.877
      test_precision: 0.902
      test_recall: 0.854
      test_auroc: 0.941
      per_type_F1:
        incompleteness: 0.92
        authorization_scope: 0.90
        conditional_precedence: 0.88
        scopal: 0.85
        lexical: 0.83
        coreferential: 0.80
      baselines:
        random_F1: 0.50
        keyword_F1: 0.62
        gpt4_zeroshot_F1: 0.71
      false_negative_rate: 0.146
      false_positive_rate: 0.098
    result_rationale: >
      Best 档下 DeBERTa F1=0.877, AUROC=0.941 作为 PoC 优秀。Per-type F1 呈现与 C3 一致的层级：
      spec-layer (0.88-0.92) > ling-layer (0.80-0.85)——spec-layer ambiguity 涉及更明显的结构性缺失
      或模糊措辞（如 missing exception clauses, vague role boundaries），这些 linguistic markers 
      对 fine-tuned model 更 salient；ling-layer ambiguity 的 surface form 更接近正常文本，
      如 PP attachment 或 lexical polysemy，subtle enough to fool both LLMs and classifiers。
      Coreferential F1 最低（0.80）与其作为 C2 boundary case 一致——最 subtle 的 ambiguity type。
      GPT-4 zero-shot F1=0.71 << DeBERTa 0.877：LLMs 作为 ambiguity detector 效果有限，与
      Ambiguity Blindness 发现呼应——agents 不擅长 meta-cognition about ambiguity，但
      fine-tuned small models 可弥补。Keyword baseline 0.62 说明 ambiguity 不能通过简单 pattern matching 检测。
      作为 Appendix PoC 不声称 contribution，但建立 Chantree et al. (2006) → 本文的理论链，
      展示 findings 的 practical applicability pathway。
    tables:
      - name: "Classifier Performance Comparison"
        columns: ["method", "F1", "Precision", "Recall", "AUROC"]
        rows:
          - ["**DeBERTa (ours)**", "**0.877**", "**0.902**", "**0.854**", "**0.941**"]
          - ["GPT-4 zero-shot", "0.71", "0.68", "0.74", "0.78"]
          - ["Keyword baseline", "0.62", "0.55", "0.72", "0.64"]
          - ["Random", "0.50", "0.50", "0.50", "0.50"]
      - name: "Per-Type F1"
        columns: ["type", "layer", "F1", "N_test"]
        rows:
          - ["incompleteness", "spec", "0.92", 10]
          - ["authorization_scope", "spec", "0.90", 10]
          - ["conditional_precedence", "spec", "0.88", 10]
          - ["scopal", "ling", "0.85", 10]
          - ["lexical", "ling", "0.83", 10]
          - ["coreferential", "ling", "0.80", 10]
    figures_description:
      - "ROC curve: DeBERTa 0.941 vs GPT-4 zero-shot 0.78 vs keyword 0.64"
      - "Per-type F1 bar chart with layer coloring: spec (blue, higher) vs ling (orange, lower)"
    analysis: >
      DeBERTa PoC 建立从 theoretical findings 到 practical tool 的桥梁。Per-type F1 的 spec > ling
      pattern 为 Disambiguation Channel Framework 提供 additional convergent evidence from classification
      difficulty dimension。GPT-4 zero-shot 的低 F1 与 Ambiguity Blindness 呼应。Appendix 材料。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eae7719a-6ad2-40a8-a60b-7d1d9af5750d",
  "isSidechain": false,
  "requestId": "req_011CbF4fMMZJq18sNmSLmBiP",
  "type": "assistant",
  "uuid": "9d551243-ac93-4d9d-804e-f58b14ff2299",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "4845fed2-f1aa-4e34-aca2-048b635bbadb",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017yQahDgNrssPAcWhkVXMgY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19353,
      "cache_read_input_tokens": 11447,
      "output_tokens": 34180,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19353,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 34180,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 19353,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19353
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有核心 claims (C1-C5) 全部成立，5-model 数据完整复现且 C4 model×type interaction 成为 star finding，perturbation control 完美通过，judge calibration 人类一致性高 核心假设：['C1 binary effe…",
  "leafUuid": "9d551243-ac93-4d9d-804e-f58b14ff2299",
  "sessionId": "4845fed2-f1aa-4e34-aca2-048b635bbadb"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Define best-tier results for policy ambiguity agent study",
  "sessionId": "4845fed2-f1aa-4e34-aca2-048b635bbadb"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：所有核心 claims (C1-C5) 全部成立，5-model 数据完整复现且 C4 model×type interaction 成为 star finding，perturbation control 完美通过，judge calibration 人类一致性高 核心假设：['C1 binary effe…",
  "leafUuid": "9d551243-ac93-4d9d-804e-f58b14ff2299",
  "sessionId": "4845fed2-f1aa-4e34-aca2-048b635bbadb"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Define best-tier results for policy ambiguity agent study",
  "sessionId": "4845fed2-f1aa-4e34-aca2-048b635bbadb"
}
```

---
