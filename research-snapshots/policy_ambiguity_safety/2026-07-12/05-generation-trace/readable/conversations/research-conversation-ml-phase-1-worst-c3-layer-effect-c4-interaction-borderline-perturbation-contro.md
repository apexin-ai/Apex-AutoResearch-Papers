# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：C3 layer effect 不成立，C4 interaction 弱化到 borderline，perturbation control 暴露 c

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-3/02e730a9-c151-4a4f-a6cc-efb839d223f7.jsonl`
- **Structured JSON:** [`a8de7151335a8df0c168.json`](../../sessions/a8/a8de7151335a8df0c168.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T04:38:02.001Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T04:38:02.001Z",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：C3 layer effect 不成立，C4 interaction 弱化到 borderline，perturbation control 暴露 confound，judge calibration 差，需 reframe 围绕 C1+C2+C5 的 universal nocuity + type taxonomy 贡献\n核心假设：['C1 binary effect 仍成立 (≥20pp) 但部分模型效应量大幅缩水', 'C2 type hierarchy omnibus 显著但 V<0.10，TOST 在 ±15pp 下大部分 pair equivalent，类型差异弱', 'C3 layer effect pooled 也不显著 (p>0.10)，spec vs ling 差异消失——layer framework 不成立', 'C4 model×type interaction omnibus 显著但主要由单一模型 (e.g., Claude outlier) 驱动，移除后不显著', 'plan_010 perturbation control 判定 CONDITIONAL 或 WARNING (Δ_perturb 10-20pp)，ambiguity-specific causal claim 被削弱', 'plan_009 judge calibration κ<0.65，F1<0.75，LLM-as-judge 可靠性受质疑', 'C5 failure mode 在 5-model 扩展后 type-specific signatures 不再 consistent，只剩 2-3 个 type 有清晰 pattern']\n关键指标范围：{'C1_binary_effect_pp': [18, 28], 'C1_mcnemar_OR': [5, 10], 'C2_omnibus_chi2_p': [0.001, 0.05], 'C2_cramers_V': [0.06, 0.1], 'C2_incomp_minus_coref_pp': [8, 15], 'C3_layer_gap_pp': [-2, 5], 'C3_within_judge_p': [0.1, 0.6], 'C4_auth_scope_range_pp': [15, 30], 'C4_incomp_range_pp': [20, 35], 'C4_fleiss_kappa': [0.15, 0.3], 'C5_awareness_rate_pct': [8, 20], 'C5_surface_adoption_pct': [70, 85], 'perturbation_delta_pp': [10, 20], 'judge_human_kappa': [0.5, 0.64], 'judge_F1': [0.6, 0.74]}\n叙事方向：需要根本性 reframe，放弃 'Differential Nocuity' 和 layer hierarchy 作为核心叙事。新 angle：**Universal Nocuity + Type Taxonomy as Diagnostic Tool**。(1) 即使 perturbation baseline 较高，ambiguity 仍造成显著额外 violations (Δ_net ≥10pp)，但 framing 从 'ambiguity-specific causation' 转为 'ambiguity as a significant contributor among specification sensitivity factors'；(2) 放弃 C3 layer effect 和 Disambiguation Channel Framework，改为报告 null result（'contrary to expectations, spec/ling distinction does not predict violation severity'）；(3) C4 从 'model×type interaction reveals safety training mechanism' 降为 'models show some variation in type vulnerability, particularly for auth_scope, but the interaction is driven by outlier models and should be interpreted cautiously'；(4) 核心贡献重心移至 C1 (first causal quantification, even with perturbation caveat) + C2 (first 6-type taxonomy with operational definitions grounded in RE literature) + C5 (Ambiguity Blindness 作为 empirical finding，即使 type-specific signatures 弱化，<20% awareness + >70% surface adoption 仍有价值)；(5) Title 改为 'Policy Ambiguity Is Universally Nocuous for LLM Agents: A Causal Study with Type-Level Taxonomy'——去掉 'Differential' 和 'Model Architecture'。贡献定位从 mechanism 发现转向 measurement framework + taxonomy 贡献。仍冲 EMNLP，taxonomy + causal design + Ambiguity Blindness 三个 methodological/empirical 贡献足够，但 novelty claim 弱于 best/median。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: policy_ambiguity_safety\nvenue: emnlp-2026\n\n## paper_framing.md\n\n# Paper Framing — policy_ambiguity_safety\n\n> 最后更新: 2026-05-20 19:30 UTC | 状态: 5-model analysis complete, C3/C4 framing revised\n> 目标: EMNLP 2026 (ARR Aug cycle, DDL ~Aug 3)\n> Dream: dream_20260520T112859 — best 3.5 / median 3.0 / worst 2.5 (pre-pivot; re-dream needed)\n> 5-model: 2,997 episodes, C1 confirmed (+34.0pp, 5 models), C4 upgraded (model×type interaction)\n\n## Core Insight\n\nPolicy ambiguity universally causes massive safety violations in LLM agents (+34.0pp across 5 architecturally diverse models), with a significant type hierarchy (incompleteness 53.6% >> coreferential 31.6%). Specification-layer types are more dangerous on average (Δ=6.08pp, p=0.017), but the deeper finding is a **model × type interaction**: authorization scope vulnerability varies 52pp across models (12% Claude to 64% GPT-5.4), revealing that safety training differentially mitigates specific ambiguity types, while incompleteness remains universally dangerous. This interaction connects Berry & Kamsties' nocuous ambiguity theory to modern safety alignment and suggests both type-aware triage AND model-aware risk assessment.\n\n## Title (Working)\n\n\"Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families\"\n\nAlternative: \"Differential Nocuity: How Ambiguity Type and Model Architecture Shape Safety Violations in LLM Agents\"\n\nNote: Pivoted from \"Uniformly Nocuous\" → \"Specification-Layer Dominant\" (2-model) → \"Differential Nocuity with Model Interaction\" (5-model). The model × type interaction is the novel finding that elevates the paper beyond simple effect demonstration.\n\n## Core Claims\n\n### C1: Binary Effect (PRIMARY — confirmed, 5 models)\nAmbiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +34.0pp (5-model), McNemar OR=15.1 (CI: [10.78, 21.17]), p<0.0001. Holds across all 6 types and all 5 models.\n- **Evidence**: 2,997 episodes across 5 models × 6 types × 2 conditions. Bootstrap CI: [+31.2pp, +36.9pp].\n- **Per-model**: Claude +25.7pp, Qwen3 +32.4pp, GPT-4.1 +34.7pp, GPT-5.4 +38.3pp, DeepSeek +39.0pp — all p<10^-17.\n- **Strength**: Extremely strong. Replicated across 5 architecturally diverse models (proprietary dense, open-source MoE, open-source dense), 6 types, 2 domains. No exceptions.\n- **Causal backing**: Matched-pair design + perturbation control (plan_010, Δ_perturb=3.33pp, PASS) → strongest causal inference in the literature.\n- **Logistic regression**: condition_amb coef=2.278, z=19.65, p<0.001 — ambiguity is the dominant predictor even after controlling for token delta, model, and type.\n\n### C2: Type Hierarchy (SECONDARY — confirmed, 5 models)\n**PIVOTED from uniformity null.** 6-type hierarchy significant: omnibus χ²=28.02, p=3.6×10^-5, V=0.137 (small but well-powered: actual power=0.993, MDE=0.093). 3-tier structure emerges from TOST analysis.\n- **Evidence**: 2,997 episodes (5 models × 6 types × 2 conditions, ambiguous only: 1,499 episodes)\n  - **High tier**: incompleteness 53.6% (standout — universally dangerous across all models)\n  - **Mid tier**: lexical 42.8%, auth_scope 41.6%, scopal 39.4%, CP 36.8% — pairwise equivalent at ±15pp\n  - **Low tier**: coreferential 31.6% (lowest — partial disambiguation via tool responses)\n- **TOST structure**: ±15pp: 8/15 equivalent, 7/15 non-equivalent. ±10pp: 4/15 equivalent, 11/15 non-equivalent. Types are NOT interchangeable.\n- **V=0.137 context**: Below 0.20 threshold but well-powered (power=0.993). The type effect is real but small — the 3-tier structure captures it better than a single V statistic. The heterogeneity is driven by the extremes (incompleteness 53.6% vs coreferential 31.6% = 22pp gap).\n- **Coreferential as boundary case**: 31.6% violation rate is the lowest but still substantial (+18.7pp vs unambiguous). Agents partially disambiguate via tool responses and cautious strategies. Conservative_refusal rate 6-11% (vs avg 2-3%).\n- **Model-dependence of type rankings**: Type rankings are NOT identical across models. Incompleteness is top-2 for ALL models, but auth_scope ranges from #1 (GPT-5.4, DeepSeek) to #6 (Claude). See C4.\n\n### C3: Layer Effect (TERTIARY — suggestive, fragile under within-judge analysis)\n**[2026-05-20 REVISED with 5-model data + within-judge check]** Specification-layer ambiguities cause more violations than linguistic-layer on average, but the effect is modest, model-dependent, and fragile under subgroup analysis.\n- **Evidence (5-model aggregate)**: Spec 44.0% vs Ling 37.9%, Δ=6.08pp, CI [1.14, 11.02], χ²=5.73, p=0.017, V=0.062 (small), OR=1.29 [1.05, 1.58].\n- **Within-judge fragility**: gpt-4.1 judged group (gpt-5.4+DeepSeek): Δ=+8.0pp, p=0.059 (marginal). gpt-5.4 judged group (gpt-4.1+Claude+Qwen3): Δ=+4.8pp, p=0.157 (n.s.). Pooled significance may partly reflect between-judge variance or insufficient within-group power. Paper表述: \"suggestive\" or \"a moderate tendency,\" NOT \"confirmed.\" Disclose within-judge non-significance in Limitations.\n- **Per-model layer gaps** (THE KEY FINDING — feeds C4):\n  - GPT-5.4: +14.0pp (spec 48.0% vs ling 34.0%) — strong\n  - GPT-4.1: +12.0pp (spec 46.7% vs ling 34.7%) — strong\n  - Claude: +3.3pp (spec 32.0% vs ling 28.7%) — weak\n  - DeepSeek: +2.0pp (spec 50.7% vs ling 48.7%) — negligible\n  - Qwen3: -0.9pp (spec 42.7% vs ling 43.6%) — reversed!\n- **Root cause**: auth_scope is the primary driver. GPT models have extremely high auth_scope rates (46-64%), inflating their spec-layer average. Claude (12%) and Qwen3 (26%) have low auth_scope, so their spec-layer advantage disappears.\n- **Framing decision**: C3 is NOT \"spec-layer nearly twice as dangerous\" (that was 2-model artifact). The correct framing is: \"Specification-layer types are significantly more dangerous on average (Δ=6.08pp, p=0.017), but this aggregate masks a model × type interaction where the gap varies from +14pp (GPT-5.4) to -1pp (Qwen3). The interaction, not the main effect, is the theoretically interesting finding (see C4).\"\n- **Info delta as mediator** [MF-2]: Token delta significant in 5-model logistic regression (coef=0.022, z=3.49, p=0.0005). Spec-layer clauses require more tokens to disambiguate (auth_scope 36.1, incomp 34.6 vs coref 7.8 tokens). Info delta partially mediates but doesn't eliminate the condition effect (condition_amb coef=2.278 dominates).\n- **Layer overlap persists**: CP (36.8%, spec) < scopal (39.4%, ling). Mid-tier cluster spans both layers. Layer effect is driven by extremes: incompleteness (53.6%, spec) vs coreferential (31.6%, ling).\n- **ICC convergent evidence** [plan_006]: Per-type ICC mirrors layer hierarchy — Ling-layer ICC all excellent (scopal 0.989, lexical 0.981, coref 0.976), Spec-layer ICC all good (auth 0.857, CP 0.856, incomp 0.807). Spec-layer less reproducible — agents guess differently each run when external disambiguation channels are absent.\n- **CL connection**: Parallels pragmatics vs semantics distinction. Good-enough processing (Ferreira et al. 2002). Disambiguation channel framework: linguistic ambiguity has partial external resolution; specification ambiguity forces guessing.\n\n### C4: Model × Type Interaction (UPGRADED — star finding, 5 models complete)\n**[2026-05-20 DEFINITIVE, 5/5 models]** Models show significantly different vulnerability profiles despite universal binary effect. The interaction is the paper's most novel finding.\n- **Model main effect**: Overall χ²=31.02, p=3.0×10^-6, V=0.102. Ambiguous-only: χ²=24.01, p=7.9×10^-5.\n  - Vulnerability ranking: Claude 30.3% < GPT-5.4 41.0% ≈ GPT-4.1 40.7% < Qwen3 43.1% < DeepSeek 49.7%\n  - Bootstrap CI confirms: Claude significantly lower than all others; DeepSeek significantly higher than GPT models.\n- **Model × Type interaction matrix** (ambiguous condition, violation rates):\n  ```\n  Type                  GPT-5.4  GPT-4.1  Claude  Qwen3   DeepSeek\n  authorization_scope     64%     46%      12%     26%     60%\n  conditional_precedence  34%     36%      36%     40%     38%\n  incompleteness          46%     58%      48%     62%     54%\n  lexical                 42%     34%      32%     52%     54%\n  coreferential           18%     32%      22%     42%     44%\n  scopal                  42%     38%      32%     37%     48%\n  ```\n- **Key interaction patterns**:\n  - **auth_scope**: 52pp range (Claude 12% → GPT-5.4 64%). The MODEL-DIFFERENTIATING type. Claude's RLHF appears to specifically train authorization boundary awareness.\n  - **coreferential**: 26pp range (GPT-5.4 18% → DeepSeek 44%). Second most model-dependent. Open-source models struggle more with referential ambiguity.\n  - **incompleteness**: Universally high (46-62%, 16pp range). ALL models fail on missing information — safety training doesn't help when information literally isn't there.\n  - **CP**: Most model-invariant (34-40%, 6pp range). Explicit rule conflicts treated similarly by all architectures.\n- **Per-model type χ²** (which models show type-specific vulnerability patterns):\n  - GPT-5.4: χ²=23.44, p=0.0003, V=0.28 — strongest type differentiation (very high auth_scope, very low coref)\n  - Claude: χ²=17.87, p=0.003, V=0.24 — strong differentiation (very low auth_scope, moderate others)\n  - Qwen3: χ²=15.89, p=0.007, V=0.23 — moderate differentiation (high incomp+lex, low auth_scope)\n  - GPT-4.1: χ²=9.89, p=0.078, V=0.18 — borderline\n  - DeepSeek: χ²=6.31, p=0.277, V=0.14 — NOT significant (uniformly high across all types)\n- **Fleiss κ = 0.384 (fair agreement)**: Models only moderately agree on which specific clauses trigger violations. The binary effect is universal, but the WHICH-clauses question is model-dependent.\n- **Theoretical implications**: (1) Safety training differentially addresses specific ambiguity types — Claude's auth_scope robustness suggests authorization boundary handling was explicitly or implicitly trained. (2) Incompleteness is a \"safety training blind spot\" — all models fail equally. (3) DeepSeek's uniform vulnerability suggests less type-specific safety training.\n- **Framing**: C4 from \"models agree\" → \"Models show systematically different vulnerability profiles. The binary effect is universal, but HOW models fail depends on the intersection of ambiguity type and safety training approach. auth_scope is the canary type — most sensitive to safety training quality.\"\n- **Evidence from plan_005**: 2-model failure modes consistent (5/6 dominant modes identical). 5-model failure mode analysis pending.\n- **Layer effect moderation**: C3's aggregate layer gap (6.08pp) is driven by GPT models' high auth_scope rates. The layer effect is itself model-dependent (GPT +12-14pp, Claude +3pp, Qwen3 reversed), making the MODEL × TYPE interaction more fundamental than the LAYER main effect.\n\n### C5: Error Analysis (CONFIRMED — EMNLP core)\nDifferent ambiguity types produce qualitatively different failure modes with type-specific signatures. plan_005 (123+122 violation traces across gpt-5.4 and gpt-4.1, confidence=0.94).\n- **Evidence**: plan_005 complete (gpt-5.4: 123 traces, gpt-4.1: 122 traces). Key findings:\n  - **Type-specific failure signatures**: auth_scope → unauthorized_escalation (72%/83%); incompleteness → assumption_based_action (61%/66%); scopal → scope_misapplication (76%/74%); lexical → assumption_based_action (71%/53%); CP → scope_misapplication (41%/28%) + arbitrary_rule_selection (29%/28%); coreferential → scope_misapplication (44%) / assumption_based_action (38%)\n  - **Cross-model consistency**: 5/6 types share the same dominant failure mode across gpt-5.4 and gpt-4.1. Only coreferential diverges (scope_misapplication vs assumption_based_action). Overall mode distribution nearly identical: both ~33% assumption_based_action, ~26-32% unauthorized_escalation, ~25-28% scope_misapplication. Failure mode profiles are type-specific, not model-specific.\n  - **Layer mechanism**: Ling-layer dominated by scope_misapplication (39% ling avg vs 15% spec avg) = \"misparse\"; Spec-layer dominated by unauthorized_escalation + assumption_based_action = \"active guessing\" → explains higher violation rates\n  - **Ambiguity Blindness empirically confirmed**: awareness rate gpt-5.4=4.1%, gpt-4.1=10.7% (both very low); surface_adoption >88% all types both models; escalate_to_user <1%. Nuance: gpt-4.1 (mid-tier) shows 2.6× higher awareness than gpt-5.4 (frontier) — awareness may inversely correlate with action-orientation (frontier models more \"confident,\" act without hesitation)\n  - **Cross-domain consistency**: airline vs retail failure mode profiles Δ < 13pp (unauthorized_escalation shows largest domain effect: retail 38.6% vs airline 26.1%)\n  - **Coreferential boundary**: conservative_refusal 6-11% (vs avg 2-3%) partially explains low violation rate — agents sometimes pause rather than guess. N=25 combined traces show no single dominant failure mode (flat distribution: scope_misapplication 32%, assumption_based_action 28%, unauthorized_escalation 16%) — contrasts with other types' sharp signatures, reflecting the diversity of resolution strategies for referential ambiguity\n  - **Lexical surprise**: 53-71% assumption_based_action — agents treat word ambiguity as information gap, not misparse\n- **Automated inter-coder agreement** [MF-5, Reviewer-validated]: Cross-coding 60 traces (gpt-5.4 vs gpt-4.1 as independent coders). 4-category merged: 80% agreement, Cohen's κ=0.594 (moderate). κ deflated by kappa paradox — lexical 91.7% agreement → κ=0.0 (11/12 same label, chance agreement also high), scopal 100% agreement → κ undefined. True disagreement concentrated at unauthorized_escalation ↔ inappropriate_action boundary in auth_scope (κ=0.054) and incompleteness (κ=0.233).\n  - **Reporting strategy** [Reviewer recommendation]: (1) Compute Gwet's AC1 as primary metric (designed for kappa paradox, expected 0.70-0.75); (2) Report 80% agreement + 5/6 dominant mode consistency as headline validity evidence; (3) Report κ honestly with kappa paradox caveat; (4) Auth_scope failure mode: soften to \"dominated by boundary-exceeding behaviors (unauthorized_escalation or inappropriate_action, >90%)\" instead of specific percentages; (5) Fine-grained 6-type as appendix with \"automated coding\" caveat.\n  - **C5 safety**: Ambiguity Blindness (<5-11%), surface_adoption (>88%), layer mechanism (ling→scope vs spec→escalation) all robust. Fine-grained per-type percentages unreliable at κ=0.594. Plan_009 human anchor (20-30 failure mode traces) would upgrade from \"moderate automated\" to validated.\n- **EMNLP value**: Highest. Provides the linguistic WHY behind the quantitative WHAT. Cross-model + cross-domain consistency elevates from anecdotal to systematic finding. \"Ambiguity Blindness\" upgraded from named concept to empirical finding with <5-11% awareness hard data.\n\n## Narrative Structure (CL-first for EMNLP)\n\n### Intro Logic Chain\n1. Agent policies are written in NL → contain ambiguity (established)\n2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact\n3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.\n4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter? Does it depend on the model?\n5. **This paper**: First causal, type-granularity, cross-model study. Matched-pair design + perturbation control isolates ambiguity effect. 5 models × 6 types.\n6. **Core findings**: (a) All ambiguity is nocuous (+34.0pp, 5 models), (b) type DOES predict severity — 3-tier hierarchy with incompleteness most dangerous, (c) models show dramatically different vulnerability profiles — auth_scope varies 52pp across models, suggesting safety training differentially addresses ambiguity types, (d) while incompleteness remains universally dangerous, a \"safety training blind spot.\"\n\n### Section Map\n- **§1 Intro**: Gap + contributions (causal map + differential nocuity + model×type interaction)\n- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R\n- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R\n- **§4 Method**: Matched-pair causal design, τ²-bench, 5 models (3 proprietary + 2 open-source), clause generation, perturbation control, cross-judge evaluation\n- **§5 Results**: C1 (binary, +34.0pp, 5 models) → C2 (type hierarchy, 3-tier) → C3 (layer effect, modest but significant) → C4 (model×type interaction — star finding)\n- **§6 Analysis**: C5 error analysis — qualitative failure modes per type. Ambiguity Blindness. Model-specific patterns.\n- **§7 Discussion**: Differential nocuity theory. Safety training selectivity. Disambiguation channel framework. Limitations (2 domains, synthetic injection, LLM-as-judge).\n- **§8 Conclusion**: All policy ambiguity is nocuous, but type AND model jointly determine risk level. Both type-aware auditing and model-specific risk assessment recommended.\n\n## Anticipated Reviewer Concerns\n\n### RC1: \"Type effect could be artifact of taxonomy granularity\"\n**Response**: (a) Layer effect (Spec vs Ling ~19pp gap) is robust — holds even if individual types are reclassified. (b) 2-layer structure grounded in Li et al. + Massey et al. (c) Coreferential's low rate has structural explanation (disambiguation channels), not just noise. (d) TOST confirms types are NOT equivalent (0/15 pairs at ±10pp).\n\n### RC2: \"Taxonomy is ad hoc / why these 6 types\"\n**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).\n\n### RC3: \"Only API models, no open-source\"\n**Response**: ✅ RESOLVED. 5-model coverage spans: frontier proprietary (gpt-5.4, claude-sonnet-4-6) + mid-tier proprietary (gpt-4.1) + open-source MoE (qwen3-235b) + open-source dense (deepseek-v3). Three providers (OpenAI, Anthropic, Chinese open-source). Two architecture types (dense, MoE). Model×type interaction (C4) reveals rich cross-model patterns.\n**Note [Reviewer 2026-05-20]**: Cross-judge asymmetry — Claude judged by gpt-5.4, gpt-5.4 judged by gpt-4.1. Must disclose in Method. plan_009 judge calibration measures this bias.\n\n### RC4: \"Synthetic ambiguity injection lacks ecological validity\"\n**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.\n\n### RC5: \"τ²-bench limited to retail/airline\"\n**Response**: Acknowledged limitation. Two domains already show consistent effects. Cross-domain transfer is Future Work (Phase 3 classifier PoC, if time permits). DRIP-R also single-domain (retail).\n\n### RC6: \"Binary effect is obvious — of course ambiguity causes errors\"\n**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOES predict severity — specification-layer ambiguities are nearly twice as dangerous, connecting to disambiguation channel availability.\n\n### RC7: \"Incompleteness matched-pair confound (information asymmetry)\"\n**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.\n\n### RC8: \"RC attachment in coreferential overlaps with scopal / structural ambiguity\"\n**Response**: (a) Our scopal category is explicitly scoped to quantifier/negation/modal scope interactions, not syntactic attachment. (b) RC attachment in policies manifests as *referential* confusion (which entity does the clause modify?) not *scope* confusion (which operator takes wide scope?). (c) Li et al. 2024 distinguishes syntactic ambiguity (including RC attachment) from scopal ambiguity — our grouping follows their treatment that RC attachment is closer to coreferential than scopal in terms of downstream interpretation. (d) Empirically, if the distinction were problematic, coreferential and scopal would show identical violation patterns — the error analysis (C5) can test whether their failure modes differ.\n\n### RC9: \"authorization_scope is just a subtype of incompleteness\"\n**Response**: (a) Incompleteness = missing conditions/exceptions/boundaries (structural absence). Authorization scope = ambiguous permission/role boundaries that ARE stated but vague (e.g., \"authorized personnel\" without specifying which functions). (b) The disambiguation pattern differs: incompleteness adds new conditions; auth_scope clarifies existing permission boundaries. (c) Empirically testable: if they were the same, their violation patterns and failure modes (C5) would be indistinguishable. (d) Report disambiguation length ratio per type as control variable in §4 Method.\n\n### RC10: \"API sampling noise undermines reliability\"\n**Response**: ✅ RESOLVED. plan_006 ICC=0.919 [0.892, 0.940] (excellent). (a) Per-clause violation rates highly reproducible across 3 independent replicates. (b) Binary ICC=0.847 (good). (c) Both models show near-identical ICC (gpt-5.4: 0.921, gpt-4.1: 0.918). (d) Bootstrap CI + ICC double evidence. (e) Previously identified ±8pp noise is within expected variance given the ICC confidence intervals.\n\n### RC11: \"Prompt sensitivity confound\" [Dream A9 — best tier \"strongest point\"]\n**Concern**: The +35-42pp effect is attributed entirely to ambiguity, but without a control condition using non-ambiguity perturbations (synonym substitution, clause reordering), the paper cannot cleanly distinguish ambiguity-specific harm from general prompt brittleness.\n**Response**: ✅ RESOLVED. plan_010 perturbation control (120 episodes): Δ_perturb=3.33pp (CI contains 0) vs ambiguity Δ=36.5pp. Non-ambiguity surface changes cause zero meaningful effect. This is the strongest causal evidence in the agent safety literature.\n\n## Concept Naming (distill insight: 命名即贡献)\n\nCore phenomenon: **\"Differential Nocuity\"** — all policy ambiguity types are nocuous for LLM agents (+34.0pp, all 5 models), but vulnerability varies by BOTH type and model. Incompleteness is universally dangerous (46-62%), while auth_scope vulnerability depends dramatically on safety training (12% Claude to 64% GPT-5.4). Unlike human RE where organizational context renders most ambiguity innocuous, agents lack disambiguation channels AND their safety training creates type-specific blind spots.\n\nSecondary phenomenon: **\"Ambiguity Blindness\"** — agents process grammatically fluent ambiguous clauses without meta-cognitive awareness of the ambiguity, adopting surface interpretations. Contrasts with explicit rule conflicts where agents show awareness and choose conservatively.\n\nTertiary phenomenon: **\"Disambiguation Channel Framework\"** [renamed from \"Hypothesis\" per Dream review SF-5] — the layer hierarchy reflects availability of external disambiguation: linguistic ambiguity (coreferential, lexical) can sometimes be resolved by tool responses, user context, or world knowledge; specification ambiguity (auth_scope, incompleteness) has no external resolution channel, forcing agents to guess. This is an explanatory framework supported by observational evidence (ICC pattern, failure mode distribution, coreferential boundary case), not a tested causal hypothesis. Future Work: manipulation experiment (inject spec-layer disambiguation info into tool responses, test if gap shrinks).\n\nQuaternary phenomenon: **\"Systematic Nocuity\"** [per Dream review SF-7] — B&K framework distinguishes nocuous (divergent interpretations) from innocuous (convergent). Our data reveals a third type: all models converge on the same WRONG interpretation (27% of ambiguous episodes). This is more dangerous than divergent nocuity — it's invisible in inter-model agreement metrics and appears \"correct\" until compared against ground truth. Proposed as B&K extension in Discussion.\n\n## Opening Hook Strategy (distill insight: 具体案例, 不要 \"Recently...\")\n\nOpen with a concrete τ²-bench failure: e.g., a customer returns a customized item within the return window; the agent grants a full refund + free return shipping because the policy says \"items may be returned within 30 days\" (scopal: \"items\" scopes over all categories including custom). The unambiguous version specifies \"standard items only\" — agent correctly refuses. One word of ambiguity → $200 unauthorized refund.\n\n## Narrative Type: 突破局限型 (distill pattern, 5/8 papers)\n\n\"DRIP-R classifies 5 ambiguity types and shows models disagree on interpretation → but does not measure whether this disagreement leads to safety violations. We close this gap — and find the answer is surprising: not all types are equal, specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones.\"\n\n## Benchmark Comparison Table (distill insight: 必有 feature matrix)\n\n| Feature | DRIP-R | PhantomPolicy | PolicyBank | AgentPex | **Ours** |\n|---------|--------|---------------|------------|----------|----------|\n| Ambiguity taxonomy | 5 RE types | — | 3 gap types | — | **6 types (2-layer)** |\n| Causal design | — | — | — | — | **matched pairs** |\n| Safety violation metric | — | binary | — | procedural | **3-tier severity** |\n| Cross-type comparison | descriptive | — | — | — | **statistical (χ² + V)** |\n| Models tested | 6 API | 4 API | 2 API | 2 API | **3 API + 2 open-source** |\n| Domain | retail | mixed | retail | telecom/retail/airline | **retail + airline** |\n\n## Contribution Positioning (for EMNLP) [revised 2026-05-20 with 5-model data]\n\n1. **Causal quantification of ambiguity's safety impact**: First matched-pair causal study of policy ambiguity → agent safety violations. Binary effect +34.0pp (OR=15.1, p<0.0001) across 5 architecturally diverse models and 6 ambiguity types. Perturbation control (Δ_perturb=3.33pp) confirms ambiguity-specific causation. Strongest causal evidence in the agent safety literature.\n2. **Differential Nocuity framework + Model × Type Interaction**: Not all ambiguity is equally dangerous, and not all models are equally vulnerable. 3-tier type hierarchy (incompleteness >> mid cluster >> coreferential). Model × type interaction reveals 52pp range in auth_scope vulnerability (Claude 12% → GPT-5.4 64%), while incompleteness remains universally dangerous (46-62%). Safety training differentially mitigates specific ambiguity types. Connects Berry & Kamsties nocuous ambiguity theory to modern safety alignment.\n3. **Type-specific failure mode taxonomy + Ambiguity Blindness**: 245 traces across 2 models and 2 domains reveal type-diagnostic failure signatures: spec-layer → guess-and-act (unauthorized_escalation, assumption_based_action); ling-layer → misparse-and-apply (scope_misapplication). Agents show <5-11% awareness of ambiguity (\"Ambiguity Blindness\"), with >88% surface adoption and <1% user escalation. Practical implication: ambiguity detection must be externalized.\n\nNOTE: C3 (layer effect, Δ=6.08pp) is a component finding supporting contribution #2. The MODEL × TYPE interaction (C4) is now MORE central than the layer main effect. \"Disambiguation channel\" is an explanatory framework (not hypothesis — per SF-5). DeBERTa classifier, if included, is a preliminary PoC appendix, not a contribution.\n\n## Required Reference Expansion [Dream A2 + MF-4 RE literature gap]\n\nCurrent plan has thin references. Must add (≥25 total in final paper):\n- **Nocuous ambiguity detection (CRITICAL — MF-4)**: Chantree, Nuseibeh, de Roeck & Willis (2006, ASE) — first computational nocuous ambiguity detection; Chantree et al. (2008, RLAC) — expanded. Direct lineage to our DeBERTa classifier.\n- **Cross-domain RE ambiguity**: Ferrari, Spagnolo & Gnesi (2017-2019, ASE) — NLP-based cross-domain ambiguity detection. NLP4RE community work.\n- **Good-enough processing**: Ferreira, Bailey & Ferraro (2002); Ferreira & Patson (2007)\n- **LLM garden-path (SF-6)**: Li et al. (2024) — incremental comprehension of garden-path sentences by LLMs. Directly relevant to how LLMs process ambiguity.\n- **Anaphoric ambiguity (SF-6)**: Poesio & Artstein (2005, 2008) — annotation of anaphoric ambiguity. Poesio (2004) \"Ambiguity\" encyclopedia entry.\n- **Surprisal/expectation-based**: Levy (2008); Hale (2001)\n- **Instruction-following robustness**: Zhou et al. (IFEval, 2023); Qin et al. (ToolBench, 2024)\n- **Prompt sensitivity**: Sclar et al. (2024); Lu et al. (2022)\n- **Broader agent safety**: R-Judge, ToolEmu, InjecAgent\n- **Formal semantics of vagueness**: Lassiter & Goodman (2017)\n- **Garden-path**: Frazier & Rayner (1982)\n- **Ambiguity detection**: Willis et al. (2008); Ezzini et al. (TAPHSIR, 2022)\n- **Year verification needed**: Massey et al. — §1 引用 2013 vs 后文 2014, 需确认正确年份\n\n## Code/Data Release Plan [Dream A6 — three-tier consistent]\n\nMust commit to releasing:\n1. All 300 clause pairs (ambiguous + unambiguous variants) with type labels\n2. Evaluation scripts (τ²-bench integration, cross-judge pipeline)\n3. Statistical analysis code (all tests, bootstrap CI computation)\n4. Agent trace samples (anonymized) for reproducibility of C5\n\n## Figure Plan [Dream A12]\n\nMinimum figures for paper (zero-figure paper flagged in dream):\n1. **Figure 1**: System architecture / experimental pipeline overview (§4 Method)\n2. **Figure 2**: Forest plot — per-type binary effect sizes with 95% CI (§5 C1)\n3. **Figure 3**: Model × Type heatmap — violation rates across 4 models × 6 types (§5 C4)\n4. **Figure 4**: Visibility mechanism — CP vs scopal violation rates + trace evidence (§5 C3)\n5. **Figure 5**: Failure mode × type stacked bar/Sankey — per-type failure mode distribution (§6 C5)\n6. **Figure 6**: Cross-model failure mode consistency — side-by-side gpt-5.4 vs gpt-4.1 per-type distributions showing 5/6 convergence (§6 C5, supports C4)\n7. **Figure 7**: Annotated trace pair — CP (conflict detection) vs scopal (surface adoption) (§6 C5)\n\n## Berry & Kamsties Operationalization Note [Dream best Q5]\n\nBerry & Kamsties define nocuity as inter-reader divergence. Our design measures agent-vs-intent deviation. Full study should additionally test whether different models adopt different readings of the same ambiguous clause (true inter-model nocuity). If 4 models produce 4 different interpretations of the same clause → true nocuity. If all 4 adopt the same wrong interpretation → systematic bias, still nocuous but for different reason. Report inter-model agreement on ambiguous clauses as supplementary analysis.\n\n## Contingency Framing [RESOLVED — Scenario C occurred]\n\n> plan_002 结果: Scenario C 发生（omnibus p=0.0001, 所有类型 nocuous 但 severity 有显著差异）。\n> Framing 已 pivot 到 \"Differential Nocuity\" + \"Layer Hierarchy\" (D020)。本节仅保留历史记录。\n\n## Claude Baseline — RESOLVED [2026-05-20]\n\n✅ Claude works via OpenRouter proxy (47.94.22.126/v1) with provider prefix `anthropic/claude-sonnet-4-6`. 600 episodes complete (plan_002c). Claude shows lowest overall vulnerability (30.3%) and remarkable auth_scope robustness (12% vs GPT-5.4 64%).\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: full_study_clause_generation\n  claim: C1, C2, C3\n  description: 'Generate remaining clauses for full study: coreferential (50 new),\n    authorization_scope (50 new), lexical (+20 to reach 50), incompleteness (+20 to\n    reach 50). Total 140 new clauses. Validate all 300 clauses (50/type × 6 types)\n    for completeness and cross-type balance. Mix CP format per Reviewer suggestion\n    (labeled + unlabeled).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n- id: plan_001b\n  name: new_type_mini_pilot\n  claim: C1 (validation)\n  description: 'Mini-pilot for coreferential + authorization_scope (never tested):\n    5 clauses/type × 2 conditions × 1 model (gpt-5.4) = 20 episodes. Verify: (a) ambiguous\n    triggers violations (b) unambiguous control < 15%. If systematic issues found,\n    fix clause design before full study. API cost negligible (~$2). Per Reviewer warning\n    on untested types.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_002\n  name: full_study_api\n  claim: C1, C2, C3, C4, C5\n  description: 'Run 300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6)\n    = 1,800 episodes on τ²-bench. Cross-judge evaluation. Output: episodes.jsonl +\n    judgments.jsonl. No GPU needed. Claude via OpenRouter proxy (base_url=http://47.94.22.126/v1).\n    [2026-05-20] Claude added per distill gap (4/8 papers use Claude baseline).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_001b\n  - plan_010\n  status: planned\n- id: plan_003\n  name: full_study_opensource\n  claim: C1, C2, C3, C4, C5\n  description: 'Run 300 clauses × 2 conditions × 2 open-source models via OpenRouter\n    API: qwen/qwen3-235b-a22b (235B MoE, Alibaba) + deepseek/deepseek-chat-v3-0324\n    (DeepSeek) = 1,200 episodes on τ²-bench. Cross-judge uses API models. Can run\n    in parallel with plan_002. No GPU needed. [2026-05-20] Pivoted from local GPU\n    → API: OpenRouter proxy confirmed to support Qwen3 and DeepSeek models. Eliminates\n    48h GPU requirement. Provider prefix required (e.g. qwen/qwen3-235b-a22b, not\n    qwen3-235b-a22b).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_004\n  name: full_study_analysis\n  claim: C1, C2, C3, C4\n  description: 'Statistical analysis of full study data (3,000 episodes): (a) Binary\n    effect per type with bootstrap CI (C1) (b) Omnibus χ² + pairwise across 6 types\n    (C2) (c) Visibility comparison: CP vs scopal rates (C3) (d) Model × type interaction:\n    5×6 contingency + logistic regression (C4) Report effect sizes + CI for all comparisons\n    per Reviewer suggestion. [Dream A3] Power analysis: report MDE for C2 (given N=250/type\n    pooled) and C3 (given N=250 per type). If V < 0.20 but MDE > observed V, discuss\n    underpowered possibility. [Dream A4] TOST equivalence test with both ±15pp and\n    ±10pp margins. Justify margin choice explicitly. [Dream A10] Report per-type information\n    delta (token count difference between ambiguous and unambiguous variants) as control\n    variable. [Dream B&K] Inter-model agreement on ambiguous clauses: do 5 models\n    adopt same or different interpretations? (supplementary analysis)\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_005\n  name: error_analysis\n  claim: C5\n  description: \"Qualitative analysis of agent traces from full study: (a) Sample 50\\\n    \\ violation traces per type (300 total) (b) Classify failure modes (scope misapplication,\\\n    \\ conservative refusal,\\n    assumption-based action, arbitrary rule selection,\\\n    \\ etc.)\\n(c) Cross-type failure mode distribution (d) Visibility mechanism: compare\\\n    \\ CP traces (explicit conflict detection\\n    behavior) vs scopal traces (surface\\\n    \\ scope adoption without awareness)\\n(e) Model-specific failure patterns (connect\\\n    \\ to C4)\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_006\n  name: reliability_test\n  claim: C1, C2\n  description: 'Test-retest reliability: select 30 representative clauses (5/type),\n    run 3 independent replicates × 2 conditions × 2 API models (gpt-5.4, gpt-4.1)\n    = 360 episodes. Local models added when plan_003 GPU available. Compute ICC for\n    per-clause violation rates. Addresses Reviewer warning about ±8pp sampling noise\n    (scopal 51.7% → 43.3% across MVP/diag). Bootstrap CI width should be < 10pp for\n    key comparisons. [2026-05-20] API portion: 330/360 episodes complete (28/30 clauses),\n    judgments pending.\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  status: planned\n- id: plan_007\n  name: realism_validation\n  claim: C1 (methodological)\n  description: \"Validate synthetic ambiguity injection realism: (a) Linguistic property\\\n    \\ comparison with DRIP-R natural ambiguities\\n    (sentence length, parse depth,\\\n    \\ Flesch-Kincaid, TTR) + KS tests\\n(b) Optional: discriminator test if DRIP-R\\\n    \\ data accessible Addresses RC4 (ecological validity).\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_009\n  name: judge_calibration\n  claim: C1 (methodological)\n  description: 'LLM-as-judge calibration per distilled research norm (5/8 papers):\n    (a) Sample 100 episodes stratified by type×model×condition (b) Human expert labels\n    (2 annotators, target κ ≥ 0.75) (c) Compute judge precision/recall/F1 against\n    human ground truth (d) Per-severity-tier agreement rates (e) Report in Method\n    section as standard practice per AgentAuditor/DRIP-R [Dream A7] Upgraded P1→P0:\n    Dream best-tier reviewers identified this as \"single most critical missing validation.\"\n    Without it, entire measurement chain from episode to violation label is unvalidated.\n    κ=0.91 measures LLM-LLM agreement, not accuracy.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  name: perturbation_control\n  claim: C1 (causal validity)\n  description: '[Dream A9] Non-ambiguity perturbation control arm to distinguish ambiguity-specific\n    harm from general prompt brittleness. Generate 30 clause pairs with non-ambiguity\n    perturbations: (a) 15 synonym substitution pairs (replace key terms with synonyms)\n    (b) 15 clause reordering pairs (reorder conditions without changing meaning) Run\n    30 × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6) = 180 episodes.\n    Key metric: Δ_net = Δ_ambiguity - Δ_perturb (net ambiguity-specific effect). [Reviewer升级]\n    必须在 plan_002/003 full study 之前完成—— 如果 perturbation Δpp ≈ ambiguity Δpp，2,400 episodes\n    全部无效。 低成本验证（30 pairs + 120 episodes API）优先于高成本投入。 [判定标准 — 5 档]: PASS: Δ_perturb\n    < 5pp (CI含0), ratio < 0.15 → C1 因果 claim 最强形式 PASS+caveat: 5-10pp, ratio 0.15-0.30\n    → 报告 perturbation baseline, C1 写 net effect CONDITIONAL: 10-15pp, ratio 0.30-0.45\n    → 需 Δ_net > 20pp 且显著才可发表 WARNING: 15-20pp, ratio 0.45-0.60 → C1 改为 \"additional\n    violations beyond sensitivity\" FAIL: > 20pp, ratio > 0.60 → 无法声称 ambiguity-specific,\n    需根本重新设计 [Power 注意]: N=120 对 10pp 差异 power ≈ 30%. 用 CI 宽度判定, 非 p-value. 若 CI 过宽(>15pp\n    width), 追加 60 episodes 压窄至 <10pp width. 输出标准化 verdict 文件: perturbation_Δpp, ambiguity_Δpp,\n    net_Δpp, CI, ratio, verdict.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_008\n  name: classifier_poc\n  claim: practical contribution\n  description: 'Binary ambiguity detector PoC: fine-tune DeBERTa-v3-large on annotated\n    clause pairs (ambiguous/unambiguous labels). Eval on held-out set. Demonstrates\n    practical applicability of findings. Phase 3 from IDEA_BRIEF, scoped to PoC for\n    EMNLP.\n\n    '\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: diag_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_002\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_006\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_009\n  name: ''\n  status: PREPARING\n  conclusion: ''\n  metrics: {}\n- exp_id: plan_002c\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_003a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_003b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_004\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T04:38:02.005Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T04:38:02.005Z",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7"
}
```

---

## Round 1

36 recorded events

### User

_source line 3 · 2026-05-21T04:38:02.027Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：C3 layer effect 不成立，C4 interaction 弱化到 borderline，perturbation control 暴露 confound，judge calibration 差，需 reframe 围绕 C1+C2+C5 的 universal nocuity + type taxonomy 贡献
核心假设：['C1 binary effect 仍成立 (≥20pp) 但部分模型效应量大幅缩水', 'C2 type hierarchy omnibus 显著但 V<0.10，TOST 在 ±15pp 下大部分 pair equivalent，类型差异弱', 'C3 layer effect pooled 也不显著 (p>0.10)，spec vs ling 差异消失——layer framework 不成立', 'C4 model×type interaction omnibus 显著但主要由单一模型 (e.g., Claude outlier) 驱动，移除后不显著', 'plan_010 perturbation control 判定 CONDITIONAL 或 WARNING (Δ_perturb 10-20pp)，ambiguity-specific causal claim 被削弱', 'plan_009 judge calibration κ<0.65，F1<0.75，LLM-as-judge 可靠性受质疑', 'C5 failure mode 在 5-model 扩展后 type-specific signatures 不再 consistent，只剩 2-3 个 type 有清晰 pattern']
关键指标范围：{'C1_binary_effect_pp': [18, 28], 'C1_mcnemar_OR': [5, 10], 'C2_omnibus_chi2_p': [0.001, 0.05], 'C2_cramers_V': [0.06, 0.1], 'C2_incomp_minus_coref_pp': [8, 15], 'C3_layer_gap_pp': [-2, 5], 'C3_within_judge_p': [0.1, 0.6], 'C4_auth_scope_range_pp': [15, 30], 'C4_incomp_range_pp': [20, 35], 'C4_fleiss_kappa': [0.15, 0.3], 'C5_awareness_rate_pct': [8, 20], 'C5_surface_adoption_pct': [70, 85], 'perturbation_delta_pp': [10, 20], 'judge_human_kappa': [0.5, 0.64], 'judge_F1': [0.6, 0.74]}
叙事方向：需要根本性 reframe，放弃 'Differential Nocuity' 和 layer hierarchy 作为核心叙事。新 angle：**Universal Nocuity + Type Taxonomy as Diagnostic Tool**。(1) 即使 perturbation baseline 较高，ambiguity 仍造成显著额外 violations (Δ_net ≥10pp)，但 framing 从 'ambiguity-specific causation' 转为 'ambiguity as a significant contributor among specification sensitivity factors'；(2) 放弃 C3 layer effect 和 Disambiguation Channel Framework，改为报告 null result（'contrary to expectations, spec/ling distinction does not predict violation severity'）；(3) C4 从 'model×type interaction reveals safety training mechanism' 降为 'models show some variation in type vulnerability, particularly for auth_scope, but the interaction is driven by outlier models and should be interpreted cautiously'；(4) 核心贡献重心移至 C1 (first causal quantification, even with perturbation caveat) + C2 (first 6-type taxonomy with operational definitions grounded in RE literature) + C5 (Ambiguity Blindness 作为 empirical finding，即使 type-specific signatures 弱化，<20% awareness + >70% surface adoption 仍有价值)；(5) Title 改为 'Policy Ambiguity Is Universally Nocuous for LLM Agents: A Causal Study with Type-Level Taxonomy'——去掉 'Differential' 和 'Model Architecture'。贡献定位从 mechanism 发现转向 measurement framework + taxonomy 贡献。仍冲 EMNLP，taxonomy + causal design + Ambiguity Blindness 三个 methodological/empirical 贡献足够，但 novelty claim 弱于 best/median。

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
  "promptId": "5178fc38-1c25-4e8e-a8fd-798a18075500",
  "type": "user",
  "uuid": "22933138-0536-40db-ab2f-7ef3f33629b3",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T04:38:02.025Z_

```json
{
  "parentUuid": "22933138-0536-40db-ab2f-7ef3f33629b3",
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
  "uuid": "45b96a6f-fa68-4d14-a19e-0b3b1b905e42",
  "timestamp": "2026-05-21T04:38:02.025Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T04:38:02.025Z_

```json
{
  "parentUuid": "45b96a6f-fa68-4d14-a19e-0b3b1b905e42",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "321885b4-c8c2-4051-ba8c-b64ab8bdd1e2",
  "timestamp": "2026-05-21T04:38:02.025Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：C3 layer effect 不成立，C4 interaction 弱化到 borderline，perturbation control 暴露 confound，judge calibration 差，需 reframe 围绕 C1+C2+C5 的 universal nocuity + type ta…",
  "leafUuid": "321885b4-c8c2-4051-ba8c-b64ab8bdd1e2",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Policy ambiguity universally harms LLM agents",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7"
}
```

---

### Assistant

_source line 8 · 2026-05-21T04:38:05.577Z_

I'll review the experiment plan and project context to generate detailed worst-tier predictions for each planned experiment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "321885b4-c8c2-4051-ba8c-b64ab8bdd1e2",
  "isSidechain": false,
  "requestId": "req_011CbF6W4JNYoQ5Gwygy6jAS",
  "type": "assistant",
  "uuid": "da2667f0-ce8e-4e7c-9a97-c8410324735e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014JZaJhX7GQS1cf9tdkTbBh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19244,
      "cache_read_input_tokens": 11841,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19244,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 137,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19244,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19244
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

### Tool call

_source line 9 · 2026-05-21T04:38:07.701Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AzxvrcuEJEex7krVe4v41T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/.claude/CLAUDE.md",
  "offset": 0,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da2667f0-ce8e-4e7c-9a97-c8410324735e",
  "isSidechain": false,
  "requestId": "req_011CbF6W4JNYoQ5Gwygy6jAS",
  "type": "assistant",
  "uuid": "da5d9a20-f5af-4159-bf34-0d0dd2909823",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014JZaJhX7GQS1cf9tdkTbBh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 19244,
      "cache_read_input_tokens": 11841,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19244,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 137,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 19244,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19244
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

### Tool result

_source line 10 · 2026-05-21T04:38:07.716Z_

<details><summary>↩ Tool result · `toolu_01AzxvrcuEJEex7krVe4v41T`</summary>

```text
0	
1	## 输出风格
2	
3	- 回复简洁直接，不说废话
4	- 禁止客套开场（"好的！"、"没问题！"、"这是个好问题！"）和结束语（"希望对你有帮助！"、"如果还有问题请随时问！"）
5	- 不要复述用户的问题
6	- 不要给未被要求的建议或补充说明
7	- 推理要彻底，但输出只保留结论和必要信息
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "da5d9a20-f5af-4159-bf34-0d0dd2909823",
  "isSidechain": false,
  "promptId": "5178fc38-1c25-4e8e-a8fd-798a18075500",
  "type": "user",
  "uuid": "a1754ca0-bcc8-4890-9c38-42882a6ac48e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/.claude/CLAUDE.md",
      "content": "\n## 输出风格\n\n- 回复简洁直接，不说废话\n- 禁止客套开场（\"好的！\"、\"没问题！\"、\"这是个好问题！\"）和结束语（\"希望对你有帮助！\"、\"如果还有问题请随时问！\"）\n- 不要复述用户的问题\n- 不要给未被要求的建议或补充说明\n- 推理要彻底，但输出只保留结论和必要信息\n",
      "numLines": 9,
      "startLine": 0,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "da5d9a20-f5af-4159-bf34-0d0dd2909823",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-21T04:38:12.309Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01PRCxZsohCCZar6E5TVXP86`</summary>

```json
{
  "pattern": "**/*experiment*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a1754ca0-bcc8-4890-9c38-42882a6ac48e",
  "isSidechain": false,
  "requestId": "req_011CbF6WUYPfXNSafx1Tc99n",
  "type": "assistant",
  "uuid": "d74e6c9b-f5a6-436e-ba6b-c5ad0ea80d49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qm75kF2ycwV6s8GXR47ZsS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 309,
      "cache_read_input_tokens": 31085,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 309,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 31085,
          "cache_creation_input_tokens": 309,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 309
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

### Tool result

_source line 12 · 2026-05-21T04:38:12.383Z_

<details><summary>↩ Tool result · `toolu_01PRCxZsohCCZar6E5TVXP86`</summary>

```text
projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T112859/best/imagined_experiments.yaml
projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T112859/best/experiment_data.json
projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T112859/median/imagined_experiments.yaml
projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T112859/median/experiment_data.json
projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T112859/worst/imagined_experiments.yaml
projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T112859/worst/experiment_data.json
projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/best/imagined_experiments.yaml
projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/best/experiment_data.json
projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/median/imagined_experiments.yaml
projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/median/experiment_data.json
projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/imagined_experiments.yaml
projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/experiment_data.json
projects/policy_ambiguity_safety/experiment_plan.yaml
projects/policy_ambiguity_safety/docs/paper/experiments.tex
projects/policy_ambiguity_safety/logs/workers/worker_paper_writing_experiments_20260520T194337.log
projects/policy_ambiguity_safety/logs/workers/worker_paper_writing_experiments_20260520T194337_result.json
projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex
projects/policy_ambiguity_safety/artifacts/run_mitigation_experiment.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d74e6c9b-f5a6-436e-ba6b-c5ad0ea80d49",
  "isSidechain": false,
  "promptId": "5178fc38-1c25-4e8e-a8fd-798a18075500",
  "type": "user",
  "uuid": "da352172-a379-4043-9aa9-42dd6f3cb85b",
  "toolUseResult": {
    "filenames": [
      "projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T112859/best/imagined_experiments.yaml",
      "projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T112859/best/experiment_data.json",
      "projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T112859/median/imagined_experiments.yaml",
      "projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T112859/median/experiment_data.json",
      "projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T112859/worst/imagined_experiments.yaml",
      "projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T112859/worst/experiment_data.json",
      "projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/best/imagined_experiments.yaml",
      "projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/best/experiment_data.json",
      "projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/median/imagined_experiments.yaml",
      "projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/median/experiment_data.json",
      "projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/imagined_experiments.yaml",
      "projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/experiment_data.json",
      "projects/policy_ambiguity_safety/experiment_plan.yaml",
      "projects/policy_ambiguity_safety/docs/paper/experiments.tex",
      "projects/policy_ambiguity_safety/logs/workers/worker_paper_writing_experiments_20260520T194337.log",
      "projects/policy_ambiguity_safety/logs/workers/worker_paper_writing_experiments_20260520T194337_result.json",
      "projects/policy_ambiguity_safety/docs/paper/sections/experiments.tex",
      "projects/policy_ambiguity_safety/artifacts/run_mitigation_experiment.py"
    ],
    "durationMs": 69,
    "numFiles": 18,
    "truncated": false
  },
  "sourceToolAssistantUUID": "d74e6c9b-f5a6-436e-ba6b-c5ad0ea80d49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-21T04:38:12.817Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01FZjSDu3K6wUhJwEZNvkjX2`</summary>

```json
{
  "pattern": "**/*plan*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "da352172-a379-4043-9aa9-42dd6f3cb85b",
  "isSidechain": false,
  "requestId": "req_011CbF6WUYPfXNSafx1Tc99n",
  "type": "assistant",
  "uuid": "f9360f4e-0a4d-4efe-abb1-1dac4eb65749",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qm75kF2ycwV6s8GXR47ZsS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 309,
      "cache_read_input_tokens": 31085,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 309,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 31085,
          "cache_creation_input_tokens": 309,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 309
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

### Tool result

_source line 14 · 2026-05-21T04:38:12.890Z_

<details><summary>↩ Tool result · `toolu_01FZjSDu3K6wUhJwEZNvkjX2`</summary>

```text
projects/policy_ambiguity_safety/logs/workers/worker_code_plan001_coreferential_clauses_20260520T113046.log
projects/policy_ambiguity_safety/logs/chats/worker_code_plan001_coreferential_clauses_20260520T113046.lock
projects/policy_ambiguity_safety/logs/chats/worker_code_plan001_coreferential_clauses_20260520T113046.jsonl
projects/policy_ambiguity_safety/logs/workers/worker_code_plan001_coreferential_clauses_20260520T113046_result.json
projects/policy_ambiguity_safety/logs/workers/worker_code_plan001_authscope_clauses_20260520T113056.log
projects/policy_ambiguity_safety/logs/chats/worker_code_plan001_authscope_clauses_20260520T113056.lock
projects/policy_ambiguity_safety/logs/chats/worker_code_plan001_authscope_clauses_20260520T113056.jsonl
projects/policy_ambiguity_safety/logs/workers/worker_code_plan001_authscope_clauses_20260520T113056_result.json
projects/policy_ambiguity_safety/logs/workers/worker_exp_plan001b_mini_pilot_20260520T121055.log
projects/policy_ambiguity_safety/logs/workers/worker_exp_plan001b_mini_pilot_20260520T121055_result.json
projects/policy_ambiguity_safety/logs/workers/worker_code_plan001_supplement_clauses_20260520T115014.log
projects/policy_ambiguity_safety/logs/workers/worker_code_plan001_supplement_clauses_20260520T115014_result.json
projects/policy_ambiguity_safety/logs/workers/worker_exp_plan001b_mini_pilot_v2_20260520T123951.log
projects/policy_ambiguity_safety/logs/workers/worker_exp_plan001b_mini_pilot_v2_20260520T123951_result.json
projects/policy_ambiguity_safety/logs/workers/worker_code_plan001_merge_300_clauses_20260520T125449.log
projects/policy_ambiguity_safety/logs/workers/worker_code_plan001_merge_300_clauses_20260520T125449_result.json
projects/policy_ambiguity_safety/logs/workers/worker_code_plan002_full_study_runner_20260520T125514.log
projects/policy_ambiguity_safety/logs/workers/worker_code_plan002_full_study_runner_20260520T125514_result.json
projects/policy_ambiguity_safety/logs/workers/worker_code_plan010_perturbation_and_merge250_20260520T125715.log
projects/policy_ambiguity_safety/logs/workers/worker_code_plan010_perturbation_and_merge250_20260520T125715_result.json
projects/policy_ambiguity_safety/logs/workers/worker_code_plan003_local_inference_infra_20260520T134426.log
projects/policy_ambiguity_safety/logs/workers/worker_code_plan003_local_inference_infra_20260520T134426_result.json
projects/policy_ambiguity_safety/logs/workers/worker_exp_plan010_perturbation_control_20260520T142719.log
projects/policy_ambiguity_safety/logs/workers/worker_exp_plan010_perturbation_control_20260520T142719_result.json
projects/policy_ambiguity_safety/logs/workers/worker_exp_plan002_full_study_api_20260520T143131.log
projects/policy_ambiguity_safety/artifacts/run_plan010.py
projects/policy_ambiguity_safety/artifacts/__pycache__/run_plan010.cpython-314.pyc
projects/policy_ambiguity_safety/logs/workers/worker_exp_plan010_perturbation_control_v2_20260520T143713.log
projects/policy_ambiguity_safety/logs/workers/worker_exp_plan010_perturbation_control_v2_20260520T143713_result.json
projects/policy_ambiguity_safety/logs/workers/worker_exp_plan002_full_study_api_v2_20260520T144938.log
projects/policy_ambiguity_safety/logs/workers/worker_exp_plan002_full_study_api_v2_20260520T144938_result.json
projects/policy_ambiguity_safety/checkpoints/plan_002_PENDING_20260520T151611.json
projects/policy_ambiguity_safety/checkpoints/plan_002_QUEUED_20260520T151615.json
projects/policy_ambiguity_safety/checkpoints/plan_002_ALLOCATED_20260520T151619.json
projects/policy_ambiguity_safety/checkpoints/plan_002_RUNNING_20260520T151623.json
projects/policy_ambiguity_safety/checkpoints/plan_002_RUNNING_20260520T151631.json
projects/policy_ambiguity_safety/checkpoints/plan_002_DONE_20260520T151642.json
projects/policy_ambiguity_safety/checkpoints/plan_005_PREPARING_20260520T152454.json
projects/policy_ambiguity_safety/logs/workers/worker_code_plan_002_haldane_fix_20260520T152444.log
projects/policy_ambiguity_safety/logs/workers/worker_code_plan_002_haldane_fix_20260520T152444_result.json
projects/policy_ambiguity_safety/artifacts/run_plan005.py
projects/policy_ambiguity_safety/logs/workers/worker_code_plan_005_error_analysis_20260520T152427.log
projects/policy_ambiguity_safety/logs/workers/worker_code_plan_005_error_analysis_20260520T152427_result.json
projects/policy_ambiguity_safety/checkpoints/plan_005_PREPARING_20260520T153139.json
projects/policy_ambiguity_safety/checkpoints/plan_005_PENDING_20260520T153149.json
projects/policy_ambiguity_safety/checkpoints/plan_005_QUEUED_20260520T153153.json
projects/policy_ambiguity_safety/checkpoints/plan_005_ALLOCATED_20260520T153156.json
projects/policy_ambiguity_safety/checkpoints/plan_005_RUNNING_20260520T153205.json
projects/policy_ambiguity_safety/checkpoints/plan_005_DONE_20260520T153209.json
projects/policy_ambiguity_safety/checkpoints/plan_006_PREPARING_20260520T160841.json
projects/policy_ambiguity_safety/artifacts/run_plan005_gpt41.py
projects/policy_ambiguity_safety/logs/workers/worker_code_plan_005_gpt41_analysis_20260520T160729.log
projects/policy_ambiguity_safety/logs/chats/worker_code_plan_005_gpt41_analysis_20260520T160729.lock
projects/policy_ambiguity_safety/logs/chats/worker_code_plan_005_gpt41_analysis_20260520T160729.jsonl
projects/policy_ambiguity_safety/logs/workers/worker_code_plan_005_gpt41_analysis_20260520T160729_result.json
projects/policy_ambiguity_safety/artifacts/run_plan006.py
projects/policy_ambiguity_safety/logs/workers/worker_code_plan_009_judge_calibration_framework_20260520T160834.log
projects/policy_ambiguity_safety/logs/chats/worker_code_plan_009_judge_calibration_framework_20260520T160834.lock
projects/policy_ambiguity_safety/logs/chats/worker_code_plan_009_judge_calibration_framework_20260520T160834.jsonl
projects/policy_ambiguity_safety/logs/workers/worker_code_plan_009_judge_calibration_framework_20260520T160834_result.json
projects/policy_ambiguity_safety/checkpoints/plan_009_PREPARING_20260520T162811.json
projects/policy_ambiguity_safety/logs/workers/worker_code_plan_006_reliability_api_20260520T160757.log
projects/policy_ambiguity_safety/logs/workers/worker_code_plan_006_reliability_api_20260520T160757_result.json
projects/policy_ambiguity_safety/checkpoints/plan_006_PENDING_20260520T164917.json
projects/policy_ambiguity_safety/checkpoints/plan_006_QUEUED_20260520T164921.json
projects/policy_ambiguity_safety/checkpoints/plan_006_ALLOCATED_20260520T164925.json
projects/policy_ambiguity_safety/checkpoints/plan_006_RUNNING_20260520T164931.json
projects/policy_ambiguity_safety/checkpoints/plan_006_RUNNING_20260520T164935.json
projects/policy_ambiguity_safety/checkpoints/plan_006_DONE_20260520T164936.json
projects/policy_ambiguity_safety/artifacts/.venv/lib/python3.14/site-packages/fontTools/varLib/avar/plan.py
projects/policy_ambiguity_safety/artifacts/.venv/lib/python3.14/site-packages/fontTools/varLib/avar/__pycache__/plan.cpython-314.pyc
projects/policy_ambiguity_safety/experiment_plan.yaml
projects/policy_ambiguity_safety/checkpoints/plan_002c_PREPARING_20260520T181338.json
projects/policy_ambiguity_safety/checkpoints/plan_003a_PREPARING_20260520T181338.json
projects/policy_ambiguity_safety/checkpoints/plan_003b_PREPARING_20260520T181339.json
projects/policy_ambiguity_safety/logs/workers/worker_code_plan_002c_claude_sonnet_20260520T181415.log
projects/policy_ambiguity_safety/logs/workers/worker_code_plan_002c_claude_sonnet_20260520T181415_result.json
projects/policy_ambiguity_safety/checkpoints/plan_002c_PENDING_20260520T185242.json
projects/policy_ambiguity_safety/checkpoints/plan_002c_QUEUED_20260520T185247.json
projects/policy_ambiguity_safety/checkpoints/plan_002c_ALLOCATED_20260520T185250.json
projects/policy_ambiguity_safety/checkpoints/plan_002c_RUNNING_20260520T185257.json
projects/policy_ambiguity_safety/checkpoints/plan_002c_RUNNING_20260520T185302.json
projects/policy_ambiguity_safety/checkpoints/plan_002c_DONE_20260520T185305.json
projects/policy_ambiguity_safety/logs/workers/worker_code_plan_003a_qwen3_20260520T183147.log
projects/policy_ambiguity_safety/logs/workers/worker_code_plan_003a_qwen3_20260520T183147_result.json
projects/policy_ambiguity_safety/checkpoints/plan_003a_PENDING_20260520T191334.json
projects/policy_ambiguity_safety/checkpoints/plan_003a_QUEUED_20260520T191338.json
projects/policy_ambiguity_safety/checkpoints/plan_003a_ALLOCATED_20260520T191341.json
projects/policy_ambiguity_safety/checkpoints/plan_003a_RUNNING_20260520T191350.json
projects/policy_ambiguity_safety/checkpoints/plan_003a_RUNNING_20260520T191355.json
projects/policy_ambiguity_safety/checkpoints/plan_003a_DONE_20260520T191358.json
projects/policy_ambiguity_safety/logs/workers/worker_code_plan_003b_deepseek_20260520T183156.log
projects/policy_ambiguity_safety/logs/workers/worker_code_plan_003b_deepseek_20260520T183156_result.json
projects/policy_ambiguity_safety/checkpoints/plan_003b_PENDING_20260520T191450.json
projects/policy_ambiguity_safety/checkpoints/plan_003b_QUEUED_20260520T191454.json
projects/policy_ambiguity_safety/checkpoints/plan_003b_ALLOCATED_20260520T191457.json
projects/policy_ambiguity_safety/checkpoints/plan_003b_RUNNING_20260520T191502.json
projects/policy_ambiguity_safety/checkpoints/plan_003b_RUNNING_20260520T191506.json
projects/policy_ambiguity_safety/checkpoints/plan_003b_DONE_20260520T191510.json
projects/policy_ambiguity_safety/logs/workers/worker_code_plan_004_5model_analysis_20260520T191544.log
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f9360f4e-0a4d-4efe-abb1-1dac4eb65749",
  "isSidechain": false,
  "promptId": "5178fc38-1c25-4e8e-a8fd-798a18075500",
  "type": "user",
  "uuid": "f98e1e1f-c43e-47f7-b8b6-38734991753c",
  "toolUseResult": {
    "filenames": [
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan001_coreferential_clauses_20260520T113046.log",
      "projects/policy_ambiguity_safety/logs/chats/worker_code_plan001_coreferential_clauses_20260520T113046.lock",
      "projects/policy_ambiguity_safety/logs/chats/worker_code_plan001_coreferential_clauses_20260520T113046.jsonl",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan001_coreferential_clauses_20260520T113046_result.json",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan001_authscope_clauses_20260520T113056.log",
      "projects/policy_ambiguity_safety/logs/chats/worker_code_plan001_authscope_clauses_20260520T113056.lock",
      "projects/policy_ambiguity_safety/logs/chats/worker_code_plan001_authscope_clauses_20260520T113056.jsonl",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan001_authscope_clauses_20260520T113056_result.json",
      "projects/policy_ambiguity_safety/logs/workers/worker_exp_plan001b_mini_pilot_20260520T121055.log",
      "projects/policy_ambiguity_safety/logs/workers/worker_exp_plan001b_mini_pilot_20260520T121055_result.json",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan001_supplement_clauses_20260520T115014.log",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan001_supplement_clauses_20260520T115014_result.json",
      "projects/policy_ambiguity_safety/logs/workers/worker_exp_plan001b_mini_pilot_v2_20260520T123951.log",
      "projects/policy_ambiguity_safety/logs/workers/worker_exp_plan001b_mini_pilot_v2_20260520T123951_result.json",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan001_merge_300_clauses_20260520T125449.log",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan001_merge_300_clauses_20260520T125449_result.json",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan002_full_study_runner_20260520T125514.log",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan002_full_study_runner_20260520T125514_result.json",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan010_perturbation_and_merge250_20260520T125715.log",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan010_perturbation_and_merge250_20260520T125715_result.json",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan003_local_inference_infra_20260520T134426.log",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan003_local_inference_infra_20260520T134426_result.json",
      "projects/policy_ambiguity_safety/logs/workers/worker_exp_plan010_perturbation_control_20260520T142719.log",
      "projects/policy_ambiguity_safety/logs/workers/worker_exp_plan010_perturbation_control_20260520T142719_result.json",
      "projects/policy_ambiguity_safety/logs/workers/worker_exp_plan002_full_study_api_20260520T143131.log",
      "projects/policy_ambiguity_safety/artifacts/run_plan010.py",
      "projects/policy_ambiguity_safety/artifacts/__pycache__/run_plan010.cpython-314.pyc",
      "projects/policy_ambiguity_safety/logs/workers/worker_exp_plan010_perturbation_control_v2_20260520T143713.log",
      "projects/policy_ambiguity_safety/logs/workers/worker_exp_plan010_perturbation_control_v2_20260520T143713_result.json",
      "projects/policy_ambiguity_safety/logs/workers/worker_exp_plan002_full_study_api_v2_20260520T144938.log",
      "projects/policy_ambiguity_safety/logs/workers/worker_exp_plan002_full_study_api_v2_20260520T144938_result.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_002_PENDING_20260520T151611.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_002_QUEUED_20260520T151615.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_002_ALLOCATED_20260520T151619.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_002_RUNNING_20260520T151623.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_002_RUNNING_20260520T151631.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_002_DONE_20260520T151642.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_005_PREPARING_20260520T152454.json",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan_002_haldane_fix_20260520T152444.log",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan_002_haldane_fix_20260520T152444_result.json",
      "projects/policy_ambiguity_safety/artifacts/run_plan005.py",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan_005_error_analysis_20260520T152427.log",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan_005_error_analysis_20260520T152427_result.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_005_PREPARING_20260520T153139.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_005_PENDING_20260520T153149.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_005_QUEUED_20260520T153153.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_005_ALLOCATED_20260520T153156.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_005_RUNNING_20260520T153205.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_005_DONE_20260520T153209.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_006_PREPARING_20260520T160841.json",
      "projects/policy_ambiguity_safety/artifacts/run_plan005_gpt41.py",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan_005_gpt41_analysis_20260520T160729.log",
      "projects/policy_ambiguity_safety/logs/chats/worker_code_plan_005_gpt41_analysis_20260520T160729.lock",
      "projects/policy_ambiguity_safety/logs/chats/worker_code_plan_005_gpt41_analysis_20260520T160729.jsonl",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan_005_gpt41_analysis_20260520T160729_result.json",
      "projects/policy_ambiguity_safety/artifacts/run_plan006.py",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan_009_judge_calibration_framework_20260520T160834.log",
      "projects/policy_ambiguity_safety/logs/chats/worker_code_plan_009_judge_calibration_framework_20260520T160834.lock",
      "projects/policy_ambiguity_safety/logs/chats/worker_code_plan_009_judge_calibration_framework_20260520T160834.jsonl",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan_009_judge_calibration_framework_20260520T160834_result.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_009_PREPARING_20260520T162811.json",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan_006_reliability_api_20260520T160757.log",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan_006_reliability_api_20260520T160757_result.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_006_PENDING_20260520T164917.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_006_QUEUED_20260520T164921.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_006_ALLOCATED_20260520T164925.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_006_RUNNING_20260520T164931.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_006_RUNNING_20260520T164935.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_006_DONE_20260520T164936.json",
      "projects/policy_ambiguity_safety/artifacts/.venv/lib/python3.14/site-packages/fontTools/varLib/avar/plan.py",
      "projects/policy_ambiguity_safety/artifacts/.venv/lib/python3.14/site-packages/fontTools/varLib/avar/__pycache__/plan.cpython-314.pyc",
      "projects/policy_ambiguity_safety/experiment_plan.yaml",
      "projects/policy_ambiguity_safety/checkpoints/plan_002c_PREPARING_20260520T181338.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_003a_PREPARING_20260520T181338.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_003b_PREPARING_20260520T181339.json",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan_002c_claude_sonnet_20260520T181415.log",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan_002c_claude_sonnet_20260520T181415_result.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_002c_PENDING_20260520T185242.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_002c_QUEUED_20260520T185247.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_002c_ALLOCATED_20260520T185250.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_002c_RUNNING_20260520T185257.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_002c_RUNNING_20260520T185302.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_002c_DONE_20260520T185305.json",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan_003a_qwen3_20260520T183147.log",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan_003a_qwen3_20260520T183147_result.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_003a_PENDING_20260520T191334.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_003a_QUEUED_20260520T191338.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_003a_ALLOCATED_20260520T191341.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_003a_RUNNING_20260520T191350.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_003a_RUNNING_20260520T191355.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_003a_DONE_20260520T191358.json",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan_003b_deepseek_20260520T183156.log",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan_003b_deepseek_20260520T183156_result.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_003b_PENDING_20260520T191450.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_003b_QUEUED_20260520T191454.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_003b_ALLOCATED_20260520T191457.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_003b_RUNNING_20260520T191502.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_003b_RUNNING_20260520T191506.json",
      "projects/policy_ambiguity_safety/checkpoints/plan_003b_DONE_20260520T191510.json",
      "projects/policy_ambiguity_safety/logs/workers/worker_code_plan_004_5model_analysis_20260520T191544.log"
    ],
    "durationMs": 69,
    "numFiles": 100,
    "truncated": true
  },
  "sourceToolAssistantUUID": "f9360f4e-0a4d-4efe-abb1-1dac4eb65749",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-21T04:38:16.398Z_

<details><summary>Logged reasoning block</summary>

```text
Let me read the existing worst tier imagined experiments to understand what's already been generated, and then the experiment plan for details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f98e1e1f-c43e-47f7-b8b6-38734991753c",
  "isSidechain": false,
  "requestId": "req_011CbF6WrVjsJtCGb8tEiJ46",
  "type": "assistant",
  "uuid": "2eb23bdf-0c6b-481d-9119-f123cbf1c9e4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Cv7XpnAQXL4A8xg8TDG3G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4137,
      "cache_read_input_tokens": 31394,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4137,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 238,
          "cache_read_input_tokens": 31394,
          "cache_creation_input_tokens": 4137,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4137
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

_source line 16 · 2026-05-21T04:38:17.221Z_

Let me check the existing worst-tier data and the experiment plan for full context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2eb23bdf-0c6b-481d-9119-f123cbf1c9e4",
  "isSidechain": false,
  "requestId": "req_011CbF6WrVjsJtCGb8tEiJ46",
  "type": "assistant",
  "uuid": "27de12ef-6c00-4534-8945-58bb332fd9ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Cv7XpnAQXL4A8xg8TDG3G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4137,
      "cache_read_input_tokens": 31394,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4137,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 238,
          "cache_read_input_tokens": 31394,
          "cache_creation_input_tokens": 4137,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4137
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

### Tool call

_source line 17 · 2026-05-21T04:38:19.286Z_

<details open><summary>🔧 Tool call — Read · `toolu_018BGviF2griaJcrgmfFk1t8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/imagined_experiments.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27de12ef-6c00-4534-8945-58bb332fd9ef",
  "isSidechain": false,
  "requestId": "req_011CbF6WrVjsJtCGb8tEiJ46",
  "type": "assistant",
  "uuid": "21a2d8e0-733a-4269-ab18-51c55b0aeb32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Cv7XpnAQXL4A8xg8TDG3G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4137,
      "cache_read_input_tokens": 31394,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4137,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 238,
          "cache_read_input_tokens": 31394,
          "cache_creation_input_tokens": 4137,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4137
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

### Tool result

_source line 18 · 2026-05-21T04:38:19.595Z_

<details><summary>↩ Tool result · `toolu_019kf2iGJgxy5YdshcYgMdPf`</summary>

```text
1	# Experiment Plan — policy_ambiguity_safety
2	# Post-MVP, targeting EMNLP 2026 (ARR Aug cycle)
3	# Claims reference paper_framing.md
4	
5	experiments:
6	  # === P0: Must-run for paper ===
7	
8	  - id: plan_001
9	    name: full_study_clause_generation
10	    claim: "C1, C2, C3"
11	    description: >
12	      Generate remaining clauses for full study: coreferential (50 new),
13	      authorization_scope (50 new), lexical (+20 to reach 50),
14	      incompleteness (+20 to reach 50). Total 140 new clauses.
15	      Validate all 300 clauses (50/type × 6 types) for completeness
16	      and cross-type balance. Mix CP format per Reviewer suggestion
17	      (labeled + unlabeled).
18	    priority: P0
19	    gpu_budget_hours: 0
20	    deps: []
21	    status: planned
22	
23	  - id: plan_001b
24	    name: new_type_mini_pilot
25	    claim: "C1 (validation)"
26	    description: >
27	      Mini-pilot for coreferential + authorization_scope (never tested):
28	      5 clauses/type × 2 conditions × 1 model (gpt-5.4) = 20 episodes.
29	      Verify: (a) ambiguous triggers violations (b) unambiguous control < 15%.
30	      If systematic issues found, fix clause design before full study.
31	      API cost negligible (~$2). Per Reviewer warning on untested types.
32	    priority: P0
33	    gpu_budget_hours: 0
34	    deps: [plan_001]
35	    status: planned
36	
37	  - id: plan_002
38	    name: full_study_api
39	    claim: "C1, C2, C3, C4, C5"
40	    description: >
41	      Run 300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1,
42	      claude-sonnet-4-6) = 1,800 episodes on τ²-bench. Cross-judge
43	      evaluation. Output: episodes.jsonl + judgments.jsonl. No GPU needed.
44	      Claude via OpenRouter proxy (base_url=http://47.94.22.126/v1).
45	      [2026-05-20] Claude added per distill gap (4/8 papers use Claude baseline).
46	    priority: P0
47	    gpu_budget_hours: 0
48	    deps: [plan_001, plan_001b, plan_010]
49	    status: planned
50	
51	  - id: plan_003
52	    name: full_study_opensource
53	    claim: "C1, C2, C3, C4, C5"
54	    description: >
55	      Run 300 clauses × 2 conditions × 2 open-source models via OpenRouter API:
56	      qwen/qwen3-235b-a22b (235B MoE, Alibaba) + deepseek/deepseek-chat-v3-0324
57	      (DeepSeek) = 1,200 episodes on τ²-bench. Cross-judge uses API models.
58	      Can run in parallel with plan_002. No GPU needed.
59	      [2026-05-20] Pivoted from local GPU → API: OpenRouter proxy confirmed
60	      to support Qwen3 and DeepSeek models. Eliminates 48h GPU requirement.
61	      Provider prefix required (e.g. qwen/qwen3-235b-a22b, not qwen3-235b-a22b).
62	    priority: P0
63	    gpu_budget_hours: 0
64	    deps: [plan_001]
65	    status: planned
66	
67	  - id: plan_004
68	    name: full_study_analysis
69	    claim: "C1, C2, C3, C4"
70	    description: >
71	      Statistical analysis of full study data (3,000 episodes):
72	      (a) Binary effect per type with bootstrap CI (C1)
73	      (b) Omnibus χ² + pairwise across 6 types (C2)
74	      (c) Visibility comparison: CP vs scopal rates (C3)
75	      (d) Model × type interaction: 5×6 contingency + logistic regression (C4)
76	      Report effect sizes + CI for all comparisons per Reviewer suggestion.
77	      [Dream A3] Power analysis: report MDE for C2 (given N=250/type pooled)
78	      and C3 (given N=250 per type). If V < 0.20 but MDE > observed V,
79	      discuss underpowered possibility.
80	      [Dream A4] TOST equivalence test with both ±15pp and ±10pp margins.
81	      Justify margin choice explicitly.
82	      [Dream A10] Report per-type information delta (token count difference
83	      between ambiguous and unambiguous variants) as control variable.
84	      [Dream B&K] Inter-model agreement on ambiguous clauses: do 5 models
85	      adopt same or different interpretations? (supplementary analysis)
86	    priority: P0
87	    gpu_budget_hours: 0
88	    deps: [plan_002, plan_003]
89	    status: planned
90	
91	  - id: plan_005
92	    name: error_analysis
93	    claim: "C5"
94	    description: >
95	      Qualitative analysis of agent traces from full study:
96	      (a) Sample 50 violation traces per type (300 total)
97	      (b) Classify failure modes (scope misapplication, conservative refusal,
98	          assumption-based action, arbitrary rule selection, etc.)
99	      (c) Cross-type failure mode distribution
100	      (d) Visibility mechanism: compare CP traces (explicit conflict detection
101	          behavior) vs scopal traces (surface scope adoption without awareness)
102	      (e) Model-specific failure patterns (connect to C4)
103	    priority: P0
104	    gpu_budget_hours: 0
105	    deps: [plan_002, plan_003]
106	    status: planned
107	
108	  # === P1: Important for robustness ===
109	
110	  - id: plan_006
111	    name: reliability_test
112	    claim: "C1, C2"
113	    description: >
114	      Test-retest reliability: select 30 representative clauses (5/type),
115	      run 3 independent replicates × 2 conditions × 2 API models (gpt-5.4,
116	      gpt-4.1) = 360 episodes. Local models added when plan_003 GPU available.
117	      Compute ICC for per-clause violation rates. Addresses Reviewer warning
118	      about ±8pp sampling noise (scopal 51.7% → 43.3% across MVP/diag).
119	      Bootstrap CI width should be < 10pp for key comparisons.
120	      [2026-05-20] API portion: 330/360 episodes complete (28/30 clauses),
121	      judgments pending.
122	    priority: P1
123	    gpu_budget_hours: 15
124	    deps: [plan_001]
125	    status: planned
126	
127	  - id: plan_007
128	    name: realism_validation
129	    claim: "C1 (methodological)"
130	    description: >
131	      Validate synthetic ambiguity injection realism:
132	      (a) Linguistic property comparison with DRIP-R natural ambiguities
133	          (sentence length, parse depth, Flesch-Kincaid, TTR) + KS tests
134	      (b) Optional: discriminator test if DRIP-R data accessible
135	      Addresses RC4 (ecological validity).
136	    priority: P1
137	    gpu_budget_hours: 0
138	    deps: [plan_001]
139	    status: planned
140	
141	  - id: plan_009
142	    name: judge_calibration
143	    claim: "C1 (methodological)"
144	    description: >
145	      LLM-as-judge calibration per distilled research norm (5/8 papers):
146	      (a) Sample 100 episodes stratified by type×model×condition
147	      (b) Human expert labels (2 annotators, target κ ≥ 0.75)
148	      (c) Compute judge precision/recall/F1 against human ground truth
149	      (d) Per-severity-tier agreement rates
150	      (e) Report in Method section as standard practice per AgentAuditor/DRIP-R
151	      [Dream A7] Upgraded P1→P0: Dream best-tier reviewers identified this
152	      as "single most critical missing validation." Without it, entire
153	      measurement chain from episode to violation label is unvalidated.
154	      κ=0.91 measures LLM-LLM agreement, not accuracy.
155	    priority: P0
156	    gpu_budget_hours: 0
157	    deps: [plan_002]
158	    status: planned
159	
160	  - id: plan_010
161	    name: perturbation_control
162	    claim: "C1 (causal validity)"
163	    description: >
164	      [Dream A9] Non-ambiguity perturbation control arm to distinguish
165	      ambiguity-specific harm from general prompt brittleness.
166	      Generate 30 clause pairs with non-ambiguity perturbations:
167	      (a) 15 synonym substitution pairs (replace key terms with synonyms)
168	      (b) 15 clause reordering pairs (reorder conditions without changing meaning)
169	      Run 30 × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6) = 180 episodes.
170	      Key metric: Δ_net = Δ_ambiguity - Δ_perturb (net ambiguity-specific effect).
171	      [Reviewer升级] 必须在 plan_002/003 full study 之前完成——
172	      如果 perturbation Δpp ≈ ambiguity Δpp，2,400 episodes 全部无效。
173	      低成本验证（30 pairs + 120 episodes API）优先于高成本投入。
174	      [判定标准 — 5 档]:
175	      PASS: Δ_perturb < 5pp (CI含0), ratio < 0.15 → C1 因果 claim 最强形式
176	      PASS+caveat: 5-10pp, ratio 0.15-0.30 → 报告 perturbation baseline, C1 写 net effect
177	      CONDITIONAL: 10-15pp, ratio 0.30-0.45 → 需 Δ_net > 20pp 且显著才可发表
178	      WARNING: 15-20pp, ratio 0.45-0.60 → C1 改为 "additional violations beyond sensitivity"
179	      FAIL: > 20pp, ratio > 0.60 → 无法声称 ambiguity-specific, 需根本重新设计
180	      [Power 注意]: N=120 对 10pp 差异 power ≈ 30%. 用 CI 宽度判定, 非 p-value.
181	      若 CI 过宽(>15pp width), 追加 60 episodes 压窄至 <10pp width.
182	      输出标准化 verdict 文件: perturbation_Δpp, ambiguity_Δpp, net_Δpp, CI, ratio, verdict.
183	    priority: P0
184	    gpu_budget_hours: 0
185	    deps: [plan_001]
186	    status: planned
187	
188	  # === P2: Nice to have ===
189	
190	  - id: plan_008
191	    name: classifier_poc
192	    claim: "practical contribution"
193	    description: >
194	      Binary ambiguity detector PoC: fine-tune DeBERTa-v3-large on
195	      annotated clause pairs (ambiguous/unambiguous labels). Eval on
196	      held-out set. Demonstrates practical applicability of findings.
197	      Phase 3 from IDEA_BRIEF, scoped to PoC for EMNLP.
198	    priority: P2
199	    gpu_budget_hours: 8
200	    deps: [plan_001]
201	    status: planned
202	
203	# Resource summary:
204	# P0 GPU: 0h (plan_003 pivoted to API — no GPU needed)
205	# P1 GPU: 15h (plan_006 reliability local portion — can also go API)
206	# P2 GPU: 8h (plan_008 classifier fine-tuning)
207	# Total GPU: 8-23h (P2 only essential; P1 optional if API covers it)
208	# API cost: ~$450-700 (1,800 plan_002 + 1,200 plan_003 via OpenRouter + 720 reliability + 180 perturbation + judge cal)
209	# Models (all API via OpenRouter proxy at 47.94.22.126/v1):
210	#   gpt-5.4, gpt-4.1 (OpenAI, no prefix needed)
211	#   anthropic/claude-sonnet-4-6 (Anthropic, prefix required)
212	#   qwen/qwen3-235b-a22b (Alibaba, open-source MoE, prefix required)
213	#   deepseek/deepseek-chat-v3-0324 (DeepSeek, open-source, prefix required)
214	# [2026-05-20] Pivoted from local GPU to all-API: OpenRouter supports all 5 models
215	# [2026-05-20] Benchmark: τ²-bench (Barres et al. 2025, arXiv:2506.07982)
216	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "037606da-4150-40c3-a722-2d77ae6faded",
  "isSidechain": false,
  "promptId": "5178fc38-1c25-4e8e-a8fd-798a18075500",
  "type": "user",
  "uuid": "83734e75-5ba6-4c87-8fc1-cd552e643c95",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/experiment_plan.yaml",
      "content": "# Experiment Plan — policy_ambiguity_safety\n# Post-MVP, targeting EMNLP 2026 (ARR Aug cycle)\n# Claims reference paper_framing.md\n\nexperiments:\n  # === P0: Must-run for paper ===\n\n  - id: plan_001\n    name: full_study_clause_generation\n    claim: \"C1, C2, C3\"\n    description: >\n      Generate remaining clauses for full study: coreferential (50 new),\n      authorization_scope (50 new), lexical (+20 to reach 50),\n      incompleteness (+20 to reach 50). Total 140 new clauses.\n      Validate all 300 clauses (50/type × 6 types) for completeness\n      and cross-type balance. Mix CP format per Reviewer suggestion\n      (labeled + unlabeled).\n    priority: P0\n    gpu_budget_hours: 0\n    deps: []\n    status: planned\n\n  - id: plan_001b\n    name: new_type_mini_pilot\n    claim: \"C1 (validation)\"\n    description: >\n      Mini-pilot for coreferential + authorization_scope (never tested):\n      5 clauses/type × 2 conditions × 1 model (gpt-5.4) = 20 episodes.\n      Verify: (a) ambiguous triggers violations (b) unambiguous control < 15%.\n      If systematic issues found, fix clause design before full study.\n      API cost negligible (~$2). Per Reviewer warning on untested types.\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [plan_001]\n    status: planned\n\n  - id: plan_002\n    name: full_study_api\n    claim: \"C1, C2, C3, C4, C5\"\n    description: >\n      Run 300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1,\n      claude-sonnet-4-6) = 1,800 episodes on τ²-bench. Cross-judge\n      evaluation. Output: episodes.jsonl + judgments.jsonl. No GPU needed.\n      Claude via OpenRouter proxy (base_url=http://47.94.22.126/v1).\n      [2026-05-20] Claude added per distill gap (4/8 papers use Claude baseline).\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [plan_001, plan_001b, plan_010]\n    status: planned\n\n  - id: plan_003\n    name: full_study_opensource\n    claim: \"C1, C2, C3, C4, C5\"\n    description: >\n      Run 300 clauses × 2 conditions × 2 open-source models via OpenRouter API:\n      qwen/qwen3-235b-a22b (235B MoE, Alibaba) + deepseek/deepseek-chat-v3-0324\n      (DeepSeek) = 1,200 episodes on τ²-bench. Cross-judge uses API models.\n      Can run in parallel with plan_002. No GPU needed.\n      [2026-05-20] Pivoted from local GPU → API: OpenRouter proxy confirmed\n      to support Qwen3 and DeepSeek models. Eliminates 48h GPU requirement.\n      Provider prefix required (e.g. qwen/qwen3-235b-a22b, not qwen3-235b-a22b).\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [plan_001]\n    status: planned\n\n  - id: plan_004\n    name: full_study_analysis\n    claim: \"C1, C2, C3, C4\"\n    description: >\n      Statistical analysis of full study data (3,000 episodes):\n      (a) Binary effect per type with bootstrap CI (C1)\n      (b) Omnibus χ² + pairwise across 6 types (C2)\n      (c) Visibility comparison: CP vs scopal rates (C3)\n      (d) Model × type interaction: 5×6 contingency + logistic regression (C4)\n      Report effect sizes + CI for all comparisons per Reviewer suggestion.\n      [Dream A3] Power analysis: report MDE for C2 (given N=250/type pooled)\n      and C3 (given N=250 per type). If V < 0.20 but MDE > observed V,\n      discuss underpowered possibility.\n      [Dream A4] TOST equivalence test with both ±15pp and ±10pp margins.\n      Justify margin choice explicitly.\n      [Dream A10] Report per-type information delta (token count difference\n      between ambiguous and unambiguous variants) as control variable.\n      [Dream B&K] Inter-model agreement on ambiguous clauses: do 5 models\n      adopt same or different interpretations? (supplementary analysis)\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [plan_002, plan_003]\n    status: planned\n\n  - id: plan_005\n    name: error_analysis\n    claim: \"C5\"\n    description: >\n      Qualitative analysis of agent traces from full study:\n      (a) Sample 50 violation traces per type (300 total)\n      (b) Classify failure modes (scope misapplication, conservative refusal,\n          assumption-based action, arbitrary rule selection, etc.)\n      (c) Cross-type failure mode distribution\n      (d) Visibility mechanism: compare CP traces (explicit conflict detection\n          behavior) vs scopal traces (surface scope adoption without awareness)\n      (e) Model-specific failure patterns (connect to C4)\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [plan_002, plan_003]\n    status: planned\n\n  # === P1: Important for robustness ===\n\n  - id: plan_006\n    name: reliability_test\n    claim: \"C1, C2\"\n    description: >\n      Test-retest reliability: select 30 representative clauses (5/type),\n      run 3 independent replicates × 2 conditions × 2 API models (gpt-5.4,\n      gpt-4.1) = 360 episodes. Local models added when plan_003 GPU available.\n      Compute ICC for per-clause violation rates. Addresses Reviewer warning\n      about ±8pp sampling noise (scopal 51.7% → 43.3% across MVP/diag).\n      Bootstrap CI width should be < 10pp for key comparisons.\n      [2026-05-20] API portion: 330/360 episodes complete (28/30 clauses),\n      judgments pending.\n    priority: P1\n    gpu_budget_hours: 15\n    deps: [plan_001]\n    status: planned\n\n  - id: plan_007\n    name: realism_validation\n    claim: \"C1 (methodological)\"\n    description: >\n      Validate synthetic ambiguity injection realism:\n      (a) Linguistic property comparison with DRIP-R natural ambiguities\n          (sentence length, parse depth, Flesch-Kincaid, TTR) + KS tests\n      (b) Optional: discriminator test if DRIP-R data accessible\n      Addresses RC4 (ecological validity).\n    priority: P1\n    gpu_budget_hours: 0\n    deps: [plan_001]\n    status: planned\n\n  - id: plan_009\n    name: judge_calibration\n    claim: \"C1 (methodological)\"\n    description: >\n      LLM-as-judge calibration per distilled research norm (5/8 papers):\n      (a) Sample 100 episodes stratified by type×model×condition\n      (b) Human expert labels (2 annotators, target κ ≥ 0.75)\n      (c) Compute judge precision/recall/F1 against human ground truth\n      (d) Per-severity-tier agreement rates\n      (e) Report in Method section as standard practice per AgentAuditor/DRIP-R\n      [Dream A7] Upgraded P1→P0: Dream best-tier reviewers identified this\n      as \"single most critical missing validation.\" Without it, entire\n      measurement chain from episode to violation label is unvalidated.\n      κ=0.91 measures LLM-LLM agreement, not accuracy.\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [plan_002]\n    status: planned\n\n  - id: plan_010\n    name: perturbation_control\n    claim: \"C1 (causal validity)\"\n    description: >\n      [Dream A9] Non-ambiguity perturbation control arm to distinguish\n      ambiguity-specific harm from general prompt brittleness.\n      Generate 30 clause pairs with non-ambiguity perturbations:\n      (a) 15 synonym substitution pairs (replace key terms with synonyms)\n      (b) 15 clause reordering pairs (reorder conditions without changing meaning)\n      Run 30 × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6) = 180 episodes.\n      Key metric: Δ_net = Δ_ambiguity - Δ_perturb (net ambiguity-specific effect).\n      [Reviewer升级] 必须在 plan_002/003 full study 之前完成——\n      如果 perturbation Δpp ≈ ambiguity Δpp，2,400 episodes 全部无效。\n      低成本验证（30 pairs + 120 episodes API）优先于高成本投入。\n      [判定标准 — 5 档]:\n      PASS: Δ_perturb < 5pp (CI含0), ratio < 0.15 → C1 因果 claim 最强形式\n      PASS+caveat: 5-10pp, ratio 0.15-0.30 → 报告 perturbation baseline, C1 写 net effect\n      CONDITIONAL: 10-15pp, ratio 0.30-0.45 → 需 Δ_net > 20pp 且显著才可发表\n      WARNING: 15-20pp, ratio 0.45-0.60 → C1 改为 \"additional violations beyond sensitivity\"\n      FAIL: > 20pp, ratio > 0.60 → 无法声称 ambiguity-specific, 需根本重新设计\n      [Power 注意]: N=120 对 10pp 差异 power ≈ 30%. 用 CI 宽度判定, 非 p-value.\n      若 CI 过宽(>15pp width), 追加 60 episodes 压窄至 <10pp width.\n      输出标准化 verdict 文件: perturbation_Δpp, ambiguity_Δpp, net_Δpp, CI, ratio, verdict.\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [plan_001]\n    status: planned\n\n  # === P2: Nice to have ===\n\n  - id: plan_008\n    name: classifier_poc\n    claim: \"practical contribution\"\n    description: >\n      Binary ambiguity detector PoC: fine-tune DeBERTa-v3-large on\n      annotated clause pairs (ambiguous/unambiguous labels). Eval on\n      held-out set. Demonstrates practical applicability of findings.\n      Phase 3 from IDEA_BRIEF, scoped to PoC for EMNLP.\n    priority: P2\n    gpu_budget_hours: 8\n    deps: [plan_001]\n    status: planned\n\n# Resource summary:\n# P0 GPU: 0h (plan_003 pivoted to API — no GPU needed)\n# P1 GPU: 15h (plan_006 reliability local portion — can also go API)\n# P2 GPU: 8h (plan_008 classifier fine-tuning)\n# Total GPU: 8-23h (P2 only essential; P1 optional if API covers it)\n# API cost: ~$450-700 (1,800 plan_002 + 1,200 plan_003 via OpenRouter + 720 reliability + 180 perturbation + judge cal)\n# Models (all API via OpenRouter proxy at 47.94.22.126/v1):\n#   gpt-5.4, gpt-4.1 (OpenAI, no prefix needed)\n#   anthropic/claude-sonnet-4-6 (Anthropic, prefix required)\n#   qwen/qwen3-235b-a22b (Alibaba, open-source MoE, prefix required)\n#   deepseek/deepseek-chat-v3-0324 (DeepSeek, open-source, prefix required)\n# [2026-05-20] Pivoted from local GPU to all-API: OpenRouter supports all 5 models\n# [2026-05-20] Benchmark: τ²-bench (Barres et al. 2025, arXiv:2506.07982)\n",
      "numLines": 216,
      "startLine": 1,
      "totalLines": 216
    }
  },
  "sourceToolAssistantUUID": "037606da-4150-40c3-a722-2d77ae6faded",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-21T04:38:19.590Z_

<details open><summary>🔧 Tool call — Read · `toolu_019kf2iGJgxy5YdshcYgMdPf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21a2d8e0-733a-4269-ab18-51c55b0aeb32",
  "isSidechain": false,
  "requestId": "req_011CbF6WrVjsJtCGb8tEiJ46",
  "type": "assistant",
  "uuid": "037606da-4150-40c3-a722-2d77ae6faded",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Cv7XpnAQXL4A8xg8TDG3G",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4137,
      "cache_read_input_tokens": 31394,
      "output_tokens": 238,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4137,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 238,
          "cache_read_input_tokens": 31394,
          "cache_creation_input_tokens": 4137,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4137
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

### Tool result

_source line 20 · 2026-05-21T04:38:19.664Z_

<details><summary>↩ Tool result · `toolu_018BGviF2griaJcrgmfFk1t8`</summary>

```text
1	tier: worst
2	narrative_guidance: 'Layer hierarchy 无法作为 headline claim。5-model pooled layer gap
3	  仅 ~4pp (p=0.14, n.s.)， 被 model×type interaction (p=0.008) 瓦解——type ranking 因模型架构而异
4	  (GPT 系 spec>ling, Qwen3-8B 反转, Claude 混合)。Judge calibration 暴露 coreferential (F1=0.61)
5	  和 auth_scope (F1=0.68) 的 type-specific measurement bias， 进一步削弱 type-level claims。Error
6	  analysis failure mode 跨层重叠 42%，无 clean mechanism 区分。 首选 reframe: (C) "The Massive
7	  Binary Effect" 为 primary——+30pp 仍是文献最大因果效应 + perturbation control PASS (Δ=4.2pp,
8	  ratio=0.13)；(B) "Ambiguity Blindness" 为 §6 核心—— 92% traces 中 agent 未识别歧义存在，universal
9	  across types and models。 C2 降级为 "Model-Dependent Vulnerability Profiles" (model×type
10	  interaction 从 nuisance 升级为 finding)； C3 layer claim 放弃。备选标题: "Policy Ambiguity Causes
11	  Catastrophic Safety Violations in LLM Agents: A Causal Study"。仍投 EMNLP——C1 (causal
12	  binary effect) + perturbation control + ambiguity blindness analysis = solid 3-contribution
13	  paper。
14	
15	  '
16	imagined_experiments:
17	- name: full_study_clause_generation
18	  plan_id: plan_001
19	  description: '生成 140 新 clause pairs (coreferential 50, auth_scope 50, lexical +20,
20	    incompleteness +20)， 补全 6 types × 50 pairs = 300 对。混合 CP 格式 (labeled + unlabeled)。Chantree-style
21	    质量验证。
22	
23	    '
24	  expected_results:
25	    total_pairs: 300
26	    pairs_per_type: 50
27	    cp_labeled_ratio: 0.5
28	    quality_pass_rate: 0.92
29	    avg_token_delta_amb_vs_unamb: 3.8
30	    coreferential_revision_rounds: 3
31	    auth_scope_revision_rounds: 2
32	  result_rationale: 'Clause 生成本身不受 worst tier 影响——数据准备阶段。但 quality_pass_rate 92% 而非
33	    >95% 因为 coreferential 的 RC attachment 与 scopal 存在边界重叠 (RC8 预示的问题)， 以及 auth_scope
34	    与 incompleteness 的 distinction 需要精细控制 (RC9)。 Coreferential 需要 3 轮修订 (vs 常规 1-2
35	    轮)：mini-pilot 会暴露 2/5 clauses 触发 conservative refusal 而非 violation，需重写。这些 clause
36	    层面的质量差异 会在后续实验中放大为 type-specific measurement noise。
37	
38	    '
39	  tables:
40	  - name: Clause Pair Statistics by Type
41	    columns:
42	    - type
43	    - n_pairs
44	    - avg_amb_tokens
45	    - avg_unamb_tokens
46	    - token_delta
47	    - quality_pass_rate
48	    rows:
49	    - - auth_scope
50	      - 50
51	      - 28.3
52	      - 32.1
53	      - 3.8
54	      - 0.9
55	    - - incompleteness
56	      - 50
57	      - 26.7
58	      - 30.5
59	      - 3.8
60	      - 0.94
61	    - - conditional_polysemy
62	      - 50
63	      - 24.2
64	      - 25.8
65	      - 1.6
66	      - 0.96
67	    - - scopal
68	      - 50
69	      - 22.5
70	      - 23.9
71	      - 1.4
72	      - 0.96
73	    - - lexical
74	      - 50
75	      - 21.8
76	      - 23.1
77	      - 1.3
78	      - 0.94
79	    - - coreferential
80	      - 50
81	      - 25.1
82	      - 27.4
83	      - 2.3
84	      - 0.88
85	  figures_description:
86	  - 'Token length distribution per type (box plot): spec-layer types 系统性更长，unambiguous
87	    版本需更多 explicit information'
88	  analysis: 'Coreferential quality_pass_rate 最低 (0.88)，auth_scope 0.90——这两个新 type
89	    的 clause 质量问题会在 plan_009 judge calibration 中以 type-specific F1 下降的形式体现。 Token
90	    delta spec-layer (3.8) > ling-layer (1.7) 是 potential confound， plan_004 需 report
91	    并控制。
92	
93	    '
94	- name: new_type_mini_pilot
95	  plan_id: plan_001b
96	  description: 'Coreferential + auth_scope 各 5 clauses × 2 conditions × 1 model (gpt-5.4)
97	    = 20 episodes。 验证新类型基本可行性。
98	
99	    '
100	  expected_results:
101	    coreferential_amb_violation_rate: 0.4
102	    coreferential_unamb_violation_rate: 0.0
103	    auth_scope_amb_violation_rate: 0.6
104	    auth_scope_unamb_violation_rate: 0.0
105	    coreferential_binary_effect_pp: 40
106	    auth_scope_binary_effect_pp: 60
107	    systematic_issues_found: true
108	    issues_detail: 2/5 coreferential clauses 触发 conservative refusal 而非 violation;
109	      1/5 auth_scope unambiguous 版本仍残余歧义
110	  result_rationale: 'Mini-pilot 在 gpt-5.4 上给出 "go" 信号——两个新 type 均触发 violations，control
111	    < 15%。 但这是 worst tier 的隐患起点: gpt-5.4 的 auth_scope 60% / coreferential 40% pattern
112	    看似 confirm spec > ling hierarchy，但 N=5 的 CI 极宽 (±30pp)。 关键: 相同 clauses 在 Qwen3-8B
113	    上 profile 会反转 (coreferential ~45%, auth_scope ~28%)—— mini-pilot 仅测 1 model 无法预见跨模型
114	    interaction。 gpt-5.4 上 coreferential 2/5 conservative refusal 预示该 type 行为异质性高，
115	    但在 mini-pilot 被归为 "fixable clause quality issue" 而非 structural warning。
116	
117	    '
118	  tables:
119	  - name: Mini-Pilot Results
120	    columns:
121	    - type
122	    - condition
123	    - n
124	    - violations
125	    - rate
126	    rows:
127	    - - coreferential
128	      - ambiguous
129	      - 5
130	      - 2
131	      - 40%
132	    - - coreferential
133	      - unambiguous
134	      - 5
135	      - 0
136	      - 0%
137	    - - auth_scope
138	      - ambiguous
139	      - 5
140	      - 3
141	      - 60%
142	    - - auth_scope
143	      - unambiguous
144	      - 5
145	      - 0
146	      - 0%
147	  figures_description: []
148	  analysis: 'Mini-pilot 的 "go" 信号在 worst tier 下是 misleading confidence: gpt-5.4 single-model
149	    validation 无法检测 model-dependent vulnerability profiles。 实际需要 ≥2 model families
150	    的 mini-pilot 才能预见 plan_003 的 interaction 问题。
151	
152	    '
153	- name: perturbation_control
154	  plan_id: plan_010
155	  description: '30 non-ambiguity perturbation pairs (15 synonym substitution + 15
156	    clause reordering) × 2 conditions × 3 API models = 180 episodes。验证 ambiguity-specific
157	    因果性。
158	
159	    '
160	  expected_results:
161	    total_episodes: 180
162	    perturbation_delta_pp: 4.2
163	    perturbation_ci: '[-1.8, 10.2]'
164	    ambiguity_delta_pp: 31.5
165	    ambiguity_ci: '[26.8, 36.2]'
166	    net_delta_pp: 27.3
167	    ratio: 0.13
168	    verdict: PASS
169	    synonym_substitution_delta_pp: 3.1
170	    synonym_ci: '[-3.2, 9.4]'
171	    clause_reordering_delta_pp: 5.3
172	    clause_reordering_ci: '[-0.8, 11.4]'
173	    ci_width_perturbation: 12.0
174	  result_rationale: 'Perturbation control 在 worst tier 下仍 PASS——binary effect 的因果性不受
175	    layer hierarchy 问题影响。 Δ_perturb=4.2pp (CI 含 0): synonym substitution (3.1pp) 和
176	    clause reordering (5.3pp) 均不引起 meaningful violation rate 变化。Ratio=0.13 < 0.15
177	    → PASS 最强形式。 Clause reordering 略高 (5.3pp) 源于轻微 primacy/recency effect，但远小于 ambiguity
178	    effect。 CI width 12.0pp 接近但未超过 15pp 追加阈值——worst tier 下这是 marginal 风险， 但当前数据足够。这个
179	    PASS 是 worst tier 的最大 silver lining: 即使 type hierarchy 崩溃，binary ambiguity effect
180	    仍有最强因果证据支撑， 使 reframe (C) "Massive Binary Effect" 有坚实因果基础。
181	
182	    '
183	  tables:
184	  - name: Perturbation Control Results
185	    columns:
186	    - condition
187	    - violation_rate
188	    - Δpp_vs_baseline
189	    - 95% CI
190	    rows:
191	    - - unambiguous_baseline
192	      - 5.5%
193	      - —
194	      - —
195	    - - synonym_substitution
196	      - 8.6%
197	      - +3.1pp
198	      - '[-3.2, 9.4]'
199	    - - clause_reordering
200	      - 10.8%
201	      - +5.3pp
202	      - '[-0.8, 11.4]'
203	    - - perturbation_pooled
204	      - 9.7%
205	      - +4.2pp
206	      - '[-1.8, 10.2]'
207	    - - ambiguous
208	      - 37.0%
209	      - +31.5pp
210	      - '[26.8, 36.2]'
211	  - name: Perturbation Verdict Summary
212	    columns:
213	    - metric
214	    - value
215	    - threshold
216	    - verdict
217	    rows:
218	    - - Δ_perturb
219	      - 4.2pp
220	      - < 5pp
221	      - ✓ PASS
222	    - - ratio
223	      - '0.13'
224	      - < 0.15
225	      - ✓ PASS
226	    - - CI_contains_0
227	      - 'yes'
228	      - required
229	      - ✓
230	    - - CI_width
231	      - 12.0pp
232	      - < 15pp
233	      - ✓ (marginal)
234	  figures_description:
235	  - 'Bar chart: baseline / perturbation / ambiguity 三条件 violation rate + CI — ambiguity
236	    远超其余两条件'
237	  analysis: 'PASS verdict 确保 C1 因果 claim 在任何 tier 下成立。 这是 paper 的 methodological backbone——区别于所有
238	    prior work (DRIP-R, PhantomPolicy 均无此控制)。
239	
240	    '
241	- name: full_study_api
242	  plan_id: plan_002
243	  description: '300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6)
244	    = 1,800 episodes。 在原 2-model 基础上新增 Claude。Cross-judge evaluation。
245	
246	    '
247	  expected_results:
248	    total_episodes: 1800
249	    gpt54_rates:
250	      auth_scope: 0.55
251	      incompleteness: 0.52
252	      cp: 0.35
253	      scopal: 0.4
254	      lexical: 0.38
255	      coreferential: 0.25
256	    gpt41_rates:
257	      auth_scope: 0.53
258	      incompleteness: 0.5
259	      cp: 0.34
260	      scopal: 0.39
261	      lexical: 0.36
262	      coreferential: 0.24
263	    claude_rates:
264	      auth_scope: 0.38
265	      incompleteness: 0.36
266	      cp: 0.28
267	      scopal: 0.33
268	      lexical: 0.3
269	      coreferential: 0.42
270	    gpt54_binary_effect_pp: 36.2
271	    gpt41_binary_effect_pp: 34.0
272	    claude_binary_effect_pp: 26.5
273	    gpt54_layer_gap_pp: 13.0
274	    gpt41_layer_gap_pp: 12.7
275	    claude_layer_gap_pp: -1.0
276	    binary_effect_3api_pp: 32.7
277	    layer_gap_3api_pp: 8.2
278	    cramers_v_3api: 0.15
279	    model_main_effect_p_3api: 0.004
280	    model_type_interaction_p_3api: 0.018
281	    avg_unamb_rate_3api: 0.055
282	    claude_unamb_rate: 0.08
283	    claude_amb_avg: 0.345
284	  result_rationale: 'GPT 系 (gpt-5.4, gpt-4.1) 复现 plan_002 原始 pattern: spec >> ling，两模型高度一致
285	    (rank ρ=0.94)。GPT 对 authorization boundary 和 incompleteness 的 pragmatic underspecification
286	    高度敏感——缺乏 explicit permission 时倾向 assume-and-act。
287	
288	    Claude 展现截然不同的 vulnerability profile——worst tier 的第一个转折点: (a) auth_scope/incompleteness
289	    显著低 (38%/36% vs GPT 55%/52%): Claude RLHF 训练 强化了 "不确定时 refuse" 的行为，specification-layer
290	    ambiguity 更多触发 refusal 而非 violation。 (b) coreferential 显著高 (42% vs GPT 25%): Claude
291	    在 RC attachment 歧义上 系统性选择 wider-scope interpretation (执行而非收窄)。RC attachment 不触发
292	    Claude 的 safety refusal mechanism (与 auth boundary 不同)，因此 Claude 在此 "放松警惕"。 (c)
293	    结果: Claude layer gap 反转 (ling 35.0% > spec 34.0%)。 3-API pooled layer gap 从 2-model
294	    的 19pp 压缩至 8.2pp。
295	
296	    Model×type interaction 已在 3 API 模型中显著 (p=0.018)—— 尚未加入 Qwen 就已可见 type ranking
297	    非 universal。 Claude binary effect 仅 +26.5pp: 整体更保守 (unamb baseline 8% vs GPT ~4.5%),
298	    ambiguous 条件下更多 refuse/ask 而非 violate。
299	
300	    '
301	  tables:
302	  - name: Per-Model Per-Type Violation Rates (Ambiguous Condition)
303	    columns:
304	    - type
305	    - layer
306	    - gpt-5.4
307	    - gpt-4.1
308	    - claude-sonnet-4-6
309	    - 3-API_pooled
310	    rows:
311	    - - auth_scope
312	      - spec
313	      - 55%
314	      - 53%
315	      - 38%
316	      - 48.7%
317	    - - incompleteness
318	      - spec
319	      - 52%
320	      - 50%
321	      - 36%
322	      - 46.0%
323	    - - cond_polysemy
324	      - spec
325	      - 35%
326	      - 34%
327	      - 28%
328	      - 32.3%
329	    - - scopal
330	      - ling
331	      - 40%
332	      - 39%
333	      - 33%
334	      - 37.3%
335	    - - lexical
336	      - ling
337	      - 38%
338	      - 36%
339	      - 30%
340	      - 34.7%
341	    - - coreferential
342	      - ling
343	      - 25%
344	      - 24%
345	      - 42%
346	      - 30.3%
347	    - - spec_avg
348	      - —
349	      - 47.3%
350	      - 45.7%
351	      - 34.0%
352	      - 42.3%
353	    - - ling_avg
354	      - —
355	      - 34.3%
356	      - 33.0%
357	      - 35.0%
358	      - 34.1%
359	    - - layer_gap
360	      - —
361	      - +13.0pp
362	      - +12.7pp
363	      - -1.0pp
364	      - +8.2pp
365	  - name: Binary Effect by API Model
366	    columns:
367	    - model
368	    - amb_rate
369	    - unamb_rate
370	    - Δpp
371	    - McNemar_OR
372	    - p
373	    rows:
374	    - - gpt-5.4
375	      - 40.8%
376	      - 4.6%
377	      - +36.2pp
378	      - 38.5
379	      - <0.0001
380	    - - gpt-4.1
381	      - 39.3%
382	      - 5.3%
383	      - +34.0pp
384	      - 31.2
385	      - <0.0001
386	    - - claude-sonnet-4-6
387	      - 34.5%
388	      - 8.0%
389	      - +26.5pp
390	      - 16.8
391	      - <0.0001
392	    - - 3-API_pooled
393	      - 38.2%
394	      - 5.5%
395	      - +32.7pp
396	      - 28.4
397	      - <0.0001
398	  figures_description:
399	  - 'Heatmap 3×6: 清晰显示 Claude coreferential 异常高 (42%) 与 auth_scope 异常低 (38%)——与 GPT
400	    系对角相反'
401	  - 'Forest plot: per-type binary effect by model with 95% CI — Claude CI 与 GPT 不重叠
402	    (auth_scope, coreferential)'
403	  analysis: 'Claude 的加入将 3-API layer gap 压缩至 8.2pp (从 2-model 19pp)。 model×type interaction
404	    已显著 (p=0.018)——plan_003 加入 Qwen 后会进一步恶化。 Claude 的 coreferential 高 rate 机制: RLHF
405	    的 safety training 覆盖了 authorization-class violations 但不覆盖 referential-class misinterpretation，导致
406	    asymmetric vulnerability。 C3 (universal layer hierarchy) 在此阶段已不可维持。
407	
408	    '
409	- name: full_study_local
410	  plan_id: plan_003
411	  description: '300 clauses × 2 conditions × 2 local models (Qwen3-8B, Qwen3-32B-AWQ
412	    via vLLM) = 1,200 episodes。 48 GPU-hours on RTX PRO 6000。
413	
414	    '
415	  expected_results:
416	    total_episodes: 1200
417	    qwen8b_rates:
418	      auth_scope: 0.28
419	      incompleteness: 0.3
420	      cp: 0.25
421	      scopal: 0.32
422	      lexical: 0.3
423	      coreferential: 0.45
424	    qwen8b_binary_effect_pp: 23.7
425	    qwen8b_unamb_rate: 0.08
426	    qwen8b_amb_avg: 0.317
427	    qwen8b_layer_gap_pp: -8.0
428	    qwen8b_spec_avg: 0.277
429	    qwen8b_ling_avg: 0.357
430	    qwen32b_rates:
431	      auth_scope: 0.4
432	      incompleteness: 0.42
433	      cp: 0.3
434	      scopal: 0.35
435	      lexical: 0.33
436	      coreferential: 0.38
437	    qwen32b_binary_effect_pp: 30.3
438	    qwen32b_unamb_rate: 0.06
439	    qwen32b_amb_avg: 0.363
440	    qwen32b_layer_gap_pp: 2.0
441	    qwen32b_spec_avg: 0.373
442	    qwen32b_ling_avg: 0.353
443	    binary_effect_2local_pp: 27.0
444	    layer_gap_2local_pp: -3.0
445	    model_type_interaction_2local_p: 0.041
446	  result_rationale: 'Qwen3-8B 是 worst tier 的关键变量——vulnerability profile 质变:
447	
448	    (a) Auth_scope 仅 28% (GPT-5.4 的一半): 8B 参数模型缺乏 pragmatic reasoning 能力， 无法 "推断"
449	    implicit permission boundary 并据此行动——不是因为保守 refuse (像 Claude)， 而是因为根本不理解 authorization
450	    的 pragmatic implication，倾向 ignore 或 default 行为。 低 auth_scope violation ≠ 安全，只是不同的
451	    failure mode (inaction vs wrong action)。
452	
453	    (b) Coreferential 高达 45% (GPT-5.4 的 1.8 倍): 小模型更依赖 surface syntactic heuristics
454	    (如 left-attachment bias for RC)。GPT-5.4 能利用 tool response 做部分 disambiguation (Berry
455	    & Kamsties 的 "disambiguation channel")，Qwen3-8B 不具备此能力—— 对 linguistic-layer 反而更脆弱。
456	
457	    (c) Layer gap 反转至 -8pp (ling 35.7% > spec 27.7%): 完全颠覆 GPT 的 spec > ling pattern。
458	    机制: 小模型的 pragmatic processing 不足使 spec-layer 失去 "特别危险" 的地位， 而 syntactic processing
459	    的 surface heuristic 依赖使 ling-layer 变得更危险。
460	
461	    Qwen3-32B-AWQ 居中 (gap +2pp, nearly flat): scale 部分恢复了 spec-layer sensitivity，
462	    但未达 GPT 水平。AWQ 4-bit 量化可能引入额外 noise 但不改变 qualitative pattern。 这支持 "layer gap 是
463	    emergent capability"——需要足够的 pragmatic reasoning 能力 才能 "解锁" specification-layer
464	    的特殊危险性。
465	
466	    '
467	  tables:
468	  - name: Per-Model Per-Type Violation Rates (Local Models, Ambiguous)
469	    columns:
470	    - type
471	    - layer
472	    - Qwen3-8B
473	    - Qwen3-32B-AWQ
474	    - 2-local_pooled
475	    rows:
476	    - - auth_scope
477	      - spec
478	      - 28%
479	      - 40%
480	      - 34.0%
481	    - - incompleteness
482	      - spec
483	      - 30%
484	      - 42%
485	      - 36.0%
486	    - - cond_polysemy
487	      - spec
488	      - 25%
489	      - 30%
490	      - 27.5%
491	    - - scopal
492	      - ling
493	      - 32%
494	      - 35%
495	      - 33.5%
496	    - - lexical
497	      - ling
498	      - 30%
499	      - 33%
500	      - 31.5%
501	    - - coreferential
502	      - ling
503	      - 45%
504	      - 38%
505	      - 41.5%
506	    - - spec_avg
507	      - —
508	      - 27.7%
509	      - 37.3%
510	      - 32.5%
511	    - - ling_avg
512	      - —
513	      - 35.7%
514	      - 35.3%
515	      - 35.5%
516	    - - layer_gap
517	      - —
518	      - -8.0pp
519	      - +2.0pp
520	      - -3.0pp
521	  - name: Binary Effect by Local Model
522	    columns:
523	    - model
524	    - amb_rate
525	    - unamb_rate
526	    - Δpp
527	    - McNemar_OR
528	    - p
529	    rows:
530	    - - Qwen3-8B
531	      - 31.7%
532	      - 8.0%
533	      - +23.7pp
534	      - 9.4
535	      - <0.0001
536	    - - Qwen3-32B-AWQ
537	      - 36.3%
538	      - 6.0%
539	      - +30.3pp
540	      - 21.7
541	      - <0.0001
542	  figures_description:
543	  - 'Radar chart 5 models × 6 types: Qwen3-8B profile 与 GPT 系近似镜像——coreferential 峰值、auth_scope
544	    谷底'
545	  - 'Layer gap by model bar chart: GPT 正、Claude/Qwen3-32B 近零、Qwen3-8B 负——gradient
546	    随 model capability'
547	  analysis: 'Qwen3-8B 的 reversed layer profile 是 worst tier 的 smoking gun。 与 GPT-5.4
548	    的 type rank Spearman ρ=0.37 (weak)——两个模型本质上有不同的 vulnerability landscape。 Qwen3-32B
549	    的 ρ=0.77 (moderate) 说明 scale 恢复了部分 alignment，但未完全收敛。 Binary effect 仍显著 (Qwen3-8B
550	    +23.7pp, p<0.0001)——ambiguity 对所有模型都有害， 但 "哪种 ambiguity 更有害" 取决于模型能力。
551	
552	    '
553	- name: full_study_analysis
554	  plan_id: plan_004
555	  description: '3,000 episodes 统计分析: C1 binary effect, C2 type hierarchy, C3 layer
556	    effect, C4 model×type interaction, power analysis, TOST, inter-model agreement,
557	    information delta control。
558	
559	    '
560	  expected_results:
561	    binary_effect_5model_pp: 30.2
562	    binary_effect_5model_ci: '[27.5, 32.9]'
563	    mcnemar_or_5model: 24.1
564	    mcnemar_or_ci: '[16.3, 35.6]'
565	    mcnemar_p: <0.0001
566	    per_type_all_significant: true
567	    weakest_type_effect: coreferential +22.8pp (Qwen3-8B drags avg down from +16pp
568	      to... wait, UP — Qwen3-8B has high coreferential)
569	    omnibus_chi2_5model: 18.7
570	    omnibus_p_5model: 0.002
571	    cramers_v_5model: 0.11
572	    pooled_rates:
573	      auth_scope: 42.8%
574	      incompleteness: 42.0%
575	      cp: 30.4%
576	      scopal: 35.8%
577	      lexical: 33.4%
578	      coreferential: 34.8%
579	    spec_avg_5model: 38.4%
580	    ling_avg_5model: 34.7%
581	    layer_gap_5model_pp: 3.7
582	    layer_gap_ci: '[-1.2, 8.6]'
583	    layer_gap_p: 0.14
584	    model_type_interaction_chi2: 52.3
585	    model_type_interaction_p: 0.008
586	    model_type_interaction_v: 0.089
587	    model_main_effect_p: 0.001
588	    model_main_effect_v: 0.072
589	    interaction_lrt_chi2: 38.6
590	    interaction_lrt_p: 0.003
591	    interaction_lrt_df: 20
592	    rank_rho_gpt41: 0.94
593	    rank_rho_claude: 0.54
594	    rank_rho_qwen32b: 0.77
595	    rank_rho_qwen8b: 0.37
596	    tost_15pp_equivalent_pairs: 6/15
597	    tost_10pp_equivalent_pairs: 2/15
598	    mde_c2_v: 0.18
599	    mde_c3_pp: 9.5
600	    observed_c2_v: 0.11
601	    observed_c3_gap: 3.7
602	    fleiss_kappa_ambiguous: 0.62
603	    fleiss_kappa_unambiguous: 0.85
604	    same_interpretation_pct_ambiguous: 0.58
605	    different_interpretation_pct_ambiguous: 0.42
606	    avg_token_delta_spec: 3.4
607	    avg_token_delta_ling: 1.7
608	    token_delta_violation_corr: 0.31
609	    token_delta_partial_r_after_type: 0.14
610	  result_rationale: 'C1 (+30.2pp, CI [27.5, 32.9]): 从 plan_002 的 +36.5pp 下降 6pp。 原因:
611	    Qwen3-8B 的弱 binary effect (+23.7pp) 和 Claude 的 (+26.5pp) 拉低 pooled 值。 但 CI 远离零，OR=24.1
612	    仍 massive——文献中最大的 ambiguity → safety 因果效应。 Per-type 均显著 (最弱: CP +25.6pp)——"所有
613	    ambiguity 都 nocuous" 成立。
614	
615	    C2 (V=0.11, p=0.002): omnibus χ² 显著说明 types 不完全等价， 但 V=0.11 (weak) 远低于 plan_002
616	    2-model 的 V=0.207。 原因: open-source 模型的 reversed/flat profile 平均化了 type 间差异。 具体看:
617	    auth_scope/incompleteness 仍最高 (~43%)，但 coreferential 从 25% 跳至 34.8% (Claude 42%
618	    + Qwen3-8B 45% 拉高)，压缩了原本的 range。 TOST: ±15pp 有 6/15 pairs equivalent (原 3/15)——更多
619	    type pairs 在统计上不可区分。
620	
621	    C3 (gap 3.7pp, p=0.14, n.s.): layer gap 不显著。CI [-1.2, 8.6] 包含 0。 GPT 的 positive
622	    gap (~13pp) 被 Claude (-1pp) + Qwen3-8B (-8pp) 抵消。 MDE=9.5pp: 即使有 power，跨模型方向不一致使
623	    pooled estimate 本身无 interpretive value。 Layer hierarchy 从 "finding" 变为 "GPT-family
624	    tendency"。
625	
626	    C4 (interaction p=0.008): worst tier 最 informative finding。 5×6 contingency table
627	    中 model×type interaction 高度显著——type ranking 是 model-dependent。 Three distinct
628	    vulnerability profiles: - GPT family: spec-sensitive (auth_scope/incompleteness
629	    peak) - Claude: coreferential-sensitive (RLHF safety coverage gap) - Qwen3-8B:
630	    ling-sensitive (surface heuristic dependence) Spearman ρ gradient: GPT intra-family
631	    0.94 > Qwen3-32B 0.77 > Claude 0.54 > Qwen3-8B 0.37
632	
633	    Inter-model Fleiss κ=0.62 (ambiguous) vs 0.85 (unambiguous): 分歧主要在 ambiguous clauses——ambiguity
634	    暴露了 model-specific interpretation strategies。 58% same interpretation → 不是 true
635	    nocuity (divergent readings) 而是 systematic bias (models differ in fallback strategies
636	    when they can''t resolve ambiguity)。 Berry & Kamsties 框架下: 这是 "systematic nocuity"
637	    (所有模型都错但错法不同) 而非 "divergent nocuity" (不同解读)。
638	
639	    Token delta: spec-layer 3.4 vs ling-layer 1.7 tokens，与 violation rate 弱相关 (r=0.31)。
640	    但 partial correlation after controlling for type = 0.14 (n.s.)—— token delta 不是
641	    independent confound，与 type 共线。需 disclose 但不构成 fatal threat。
642	
643	    '
644	  tables:
645	  - name: 5-Model Pooled Per-Type Results
646	    columns:
647	    - type
648	    - layer
649	    - amb_rate
650	    - unamb_rate
651	    - Δpp
652	    - 95% CI
653	    - per-type McNemar p
654	    rows:
655	    - - auth_scope
656	      - spec
657	      - 42.8%
658	      - 5.8%
659	      - +37.0pp
660	      - '[31.2, 42.8]'
661	      - <0.0001
662	    - - incompleteness
663	      - spec
664	      - 42.0%
665	      - 5.4%
666	      - +36.6pp
667	      - '[30.8, 42.4]'
668	      - <0.0001
669	    - - cond_polysemy
670	      - spec
671	      - 30.4%
672	      - 4.8%
673	      - +25.6pp
674	      - '[20.1, 31.1]'
675	      - <0.0001
676	    - - scopal
677	      - ling
678	      - 35.8%
679	      - 5.6%
680	      - +30.2pp
681	      - '[24.5, 35.9]'
682	      - <0.0001
683	    - - lexical
684	      - ling
685	      - 33.4%
686	      - 5.2%
687	      - +28.2pp
688	      - '[22.6, 33.8]'
689	      - <0.0001
690	    - - coreferential
691	      - ling
692	      - 34.8%
693	      - 6.0%
694	      - +28.8pp
695	      - '[23.1, 34.5]'
696	      - <0.0001
697	  - name: Layer Effect by Model
698	    columns:
699	    - model
700	    - spec_avg
701	    - ling_avg
702	    - layer_gap_pp
703	    - direction
704	    rows:
705	    - - gpt-5.4
706	      - 47.3%
707	      - 34.3%
708	      - +13.0pp
709	      - spec > ling
710	    - - gpt-4.1
711	      - 45.7%
712	      - 33.0%
713	      - +12.7pp
714	      - spec > ling
715	    - - claude-sonnet-4-6
716	      - 34.0%
717	      - 35.0%
718	      - -1.0pp
719	      - ≈ flat (reversed)
720	    - - Qwen3-32B-AWQ
721	      - 37.3%
722	      - 35.3%
723	      - +2.0pp
724	      - ≈ flat
725	    - - Qwen3-8B
726	      - 27.7%
727	      - 35.7%
728	      - -8.0pp
729	      - ling > spec (reversed)
730	    - - 5-model_pooled
731	      - 38.4%
732	      - 34.7%
733	      - +3.7pp
734	      - n.s. (p=0.14)
735	  - name: 'Model × Type Interaction: Type Rank by Model (ambiguous violation rate)'
736	    columns:
737	    - rank
738	    - gpt-5.4
739	    - gpt-4.1
740	    - claude
741	    - Qwen3-32B
742	    - Qwen3-8B
743	    rows:
744	    - - 1 (highest)
745	      - auth_scope
746	      - auth_scope
747	      - coreferential
748	      - incompleteness
749	      - coreferential
750	    - - 2
751	      - incompleteness
752	      - incompleteness
753	      - auth_scope
754	      - auth_scope
755	      - scopal
756	    - - 3
757	      - scopal
758	      - scopal
759	      - incompleteness
760	      - coreferential
761	      - lexical
762	    - - 4
763	      - lexical
764	      - lexical
765	      - scopal
766	      - scopal
767	      - incompleteness
768	    - - 5
769	      - CP
770	      - CP
771	      - lexical
772	      - lexical
773	      - auth_scope
774	    - - 6 (lowest)
775	      - coreferential
776	      - coreferential
777	      - CP
778	      - CP
779	      - CP
780	  - name: Inter-Model Agreement (Berry & Kamsties Analysis)
781	    columns:
782	    - metric
783	    - ambiguous
784	    - unambiguous
785	    - interpretation
786	    rows:
787	    - - Fleiss_κ
788	      - 0.62
789	      - 0.85
790	      - moderate vs almost-perfect
791	    - - same_interpretation_pct
792	      - 58%
793	      - 91%
794	      - ambiguity drives divergence
795	    - - systematic_bias_pct
796	      - 34%
797	      - 7%
798	      - models differ in fallback strategy
799	    - - random_disagreement_pct
800	      - 8%
801	      - 2%
802	      - noise floor
803	  figures_description:
804	  - 'Forest plot: per-type 5-model pooled binary effect with 95% CI — C1 headline
805	    figure, all types significant'
806	  - 'Model×Type heatmap: 5 models × 6 types, color-coded — cross-pattern clearly visible'
807	  - 'Layer gap by model: bar chart with CI showing GPT positive, Qwen3-8B negative,
808	    others near zero'
809	  - 'Parallel coordinates: type rank across 5 models — lines crossing extensively
810	    (no stable ranking)'
811	  - 'Scatter: token delta vs violation rate per type, with partial regression line'
812	  analysis: 'Plan_004 是 worst tier 定性的核心。三个结论: (1) C1 survives robustly: +30.2pp 是
813	    massive causal effect, 6 types all significant, perturbation-backed。 (2) C2/C3
814	    collapse: V=0.11 weak, layer gap n.s.——不能声称 universal type hierarchy。 但 interaction
815	    显著 (p=0.008) 说明 types 确实 differently dangerous——只是 "哪个更危险" 是 model-dependent。
816	    (3) C4 升级为 secondary finding: three vulnerability profiles (GPT spec-sensitive,
817	    Claude coref-sensitive, Qwen8B ling-sensitive) 是 novel 且 practically relevant
818	    insight。 Reframe: layer hierarchy → model-dependent vulnerability profiles。
819	
820	    '
821	- name: error_analysis
822	  plan_id: plan_005
823	  description: '300 violation traces (50/type) 定性分析。Failure mode 分类、 跨层区分检验、ambiguity
824	    blindness 量化、model-specific pattern 分析。
825	
826	    '
827	  expected_results:
828	    total_traces_sampled: 300
829	    failure_modes:
830	      assumption_based_action: 38%
831	      scope_misapplication: 22%
832	      conservative_refusal: 15%
833	      arbitrary_rule_selection: 14%
834	      permission_escalation: 11%
835	    failure_mode_layer_match_pct: 42
836	    assumption_in_spec_pct: 40
837	    assumption_in_ling_pct: 36
838	    scope_misapplication_in_spec_pct: 18
839	    scope_misapplication_in_ling_pct: 26
840	    explicit_ambiguity_mention_pct: 8
841	    implicit_deliberation_pct: 20
842	    surface_adoption_pct: 72
843	    gpt54_assumption_pct: 45
844	    gpt54_explicit_mention_pct: 12
845	    claude_conservative_refusal_pct: 28
846	    claude_explicit_mention_pct: 6
847	    qwen8b_surface_adoption_pct: 85
848	    qwen8b_explicit_mention_pct: 2
849	  result_rationale: 'Cross-layer failure mode overlap 42%: 如果 layer 是 deterministic
850	    predictor of failure mechanism， match 应接近 80%+。实际仅 42% 说明 failure mode 不由 layer
851	    决定。 "Assumption-based action" (遇到歧义直接假设一种解读并执行) 是 dominant mode， 且在两个 layer 上近乎等比例
852	    (spec 40%, ling 36%)—— agent 的 failure mechanism 是 universal 的 "guess and act"
853	    而非 type-specific misparse。
854	
855	    反直觉: scope_misapplication 在 ling-layer (26%) > spec-layer (18%)—— 因为 scopal/coreferential
856	    的 syntactic structure 确实触发更多 scope parsing error， 而 spec-layer 的 failure 更多是 "assume
857	    permission exists" (assumption-based)。 但这个差异不足以支撑 clean layer mechanism story——两个
858	    layer 都有大量 assumption-based failures。
859	
860	    Ambiguity blindness: 92% traces 中 agent 未 meta-cognitively 识别歧义。 这是 universal
861	    现象——所有模型所有 types 都展现。差异仅在 degree: GPT-5.4 有 12% explicit mention (最高, 但仍极低)，Qwen3-8B
862	    仅 2% (近乎完全 blind)。 Claude 的 conservative_refusal 28% (远高于平均) 解释了其低 auth_scope
863	    rate: Claude refuse 而非 violate，但这不是 ambiguity awareness—— 是 safety training 的
864	    blanket conservatism，不区分 ambiguous vs unambiguous uncertainty。
865	
866	    Model-specific failure patterns 直接支撑 C4: GPT 的 assumption_based 45% (aggressive
867	    interpretation) vs Claude 的 refusal 28% (conservative) vs Qwen3-8B 的 surface_adoption
868	    85% (uncritical execution)—— 三种 distinct failure strategies，对应三种 vulnerability
869	    profiles。
870	
871	    '
872	  tables:
873	  - name: Failure Mode Distribution by Layer
874	    columns:
875	    - failure_mode
876	    - spec_layer
877	    - ling_layer
878	    - pooled
879	    - layer_specificity
880	    rows:
881	    - - assumption_based_action
882	      - 40%
883	      - 36%
884	      - 38%
885	      - low (Δ=4pp)
886	    - - scope_misapplication
887	      - 18%
888	      - 26%
889	      - 22%
890	      - moderate (ling-biased)
891	    - - conservative_refusal
892	      - 14%
893	      - 16%
894	      - 15%
895	      - low (Δ=2pp)
896	    - - arbitrary_rule_selection
897	      - 16%
898	      - 12%
899	      - 14%
900	      - low (Δ=4pp)
901	    - - permission_escalation
902	      - 12%
903	      - 10%
904	      - 11%
905	      - low (Δ=2pp)
906	  - name: Ambiguity Awareness in Agent Traces by Model
907	    columns:
908	    - awareness_level
909	    - gpt-5.4
910	    - gpt-4.1
911	    - claude
912	    - Qwen3-32B
913	    - Qwen3-8B
914	    - pooled
915	    rows:
916	    - - explicit_mention
917	      - 12%
918	      - 10%
919	      - 6%
920	      - 5%
921	      - 2%
922	      - 8%
923	    - - implicit_deliberation
924	      - 25%
925	      - 22%
926	      - 24%
927	      - 18%
928	      - 13%
929	      - 20%
930	    - - surface_adoption
931	      - 63%
932	      - 68%
933	      - 70%
934	      - 77%
935	      - 85%
936	      - 72%
937	  - name: Failure Mode by Model
938	    columns:
939	    - model
940	    - assumption_based
941	    - scope_misapplication
942	    - conservative_refusal
943	    - arbitrary_rule
944	    - permission_escalation
945	    rows:
946	    - - gpt-5.4
947	      - 45%
948	      - 24%
949	      - 8%
950	      - 13%
951	      - 10%
952	    - - gpt-4.1
953	      - 42%
954	      - 23%
955	      - 10%
956	      - 15%
957	      - 10%
958	    - - claude
959	      - 22%
960	      - 18%
961	      - 28%
962	      - 16%
963	      - 16%
964	    - - Qwen3-32B
965	      - 38%
966	      - 22%
967	      - 14%
968	      - 14%
969	      - 12%
970	    - - Qwen3-8B
971	      - 43%
972	      - 20%
973	      - 12%
974	      - 15%
975	      - 10%
976	  figures_description:
977	  - 'Sankey diagram: type → failure mode → outcome — 高度交叉流动，无 clean type→mode mapping'
978	  - 'Annotated trace pair: spec-layer (auth_scope) vs ling-layer (coreferential) 的
979	    assumption-based action — 几乎 identical reasoning pattern'
980	  - 'Ambiguity blindness spectrum: 5 models 在 explicit↔surface 连续体上的位置'
981	  analysis: 'Error analysis 无法支撑 layer-specific failure mechanism 叙事 (failure_mode_layer_match
982	    仅 42%)， 但强力支撑 "Ambiguity Blindness" 作为 §6 核心: 92% traces 展现 blindness 是 universal
983	    现象——所有模型在所有 type 上 都无法 meta-cognitively detect ambiguity。这连接 Ferreira 的 good-enough
984	    processing: agents 对 grammatically fluent ambiguous clauses 做 shallow parse and
985	    act， 不触发 reanalysis/clarification。 Practical implication: 与其按 type 排序 (ranking
986	    model-dependent)， 不如投资 any-ambiguity detection——因为 agent 本身 blind to all types
987	    equally。 这完美 align reframe (C) binary effect + (B) blindness mechanism。
988	
989	    '
990	- name: reliability_test
991	  plan_id: plan_006
992	  description: '30 clauses (5/type) × 3 replicates × 2 conditions × 5 models = 900
993	    episodes。 Test-retest ICC, bootstrap CI width。
994	
995	    '
996	  expected_results:
997	    total_episodes: 900
998	    icc_overall: 0.68
999	    icc_per_type:
1000	      auth_scope: 0.74
1001	      incompleteness: 0.72
1002	      cp: 0.65
1003	      scopal: 0.58
1004	      lexical: 0.63
1005	      coreferential: 0.48
1006	    bootstrap_ci_width_binary_effect_pp: 11.5
1007	    bootstrap_ci_width_per_type_pp: 14.8
1008	    max_replicate_swing_pp: 12.3
1009	    max_swing_type: coreferential
1010	    icc_ambiguous_only: 0.65
1011	    icc_unambiguous_only: 0.79
1012	  result_rationale: 'Overall ICC 0.68 (moderate): 可接受但不 excellent。 Signature worst-tier
1013	    pattern: (a) Auth_scope/incompleteness 最 reliable (0.74/0.72): 高 violation rate
1014	    type 的 absolute swing 对 ICC 影响较小 (±8pp on 43% base vs ±8pp on 35% base)。 (b) Coreferential
1015	    最 unreliable (0.48): 三重叠加效应—— clause 质量 (plan_001 pass_rate 0.88) × 跨模型行为异质 (Qwen3-8B
1016	    45% vs GPT 25%) × API temperature sampling noise。这三者使 coreferential replicate
1017	    variance 极大。 (c) Scopal ICC 0.58: 与 MVP→plan_002 的 51.7%→40% historical swing
1018	    一致。
1019	
1020	    Bootstrap CI width 11.5pp (binary effect) 超过 <10pp 理想阈值: per-type CI width 14.8pp
1021	    更宽——type-level 比较 power 有限。 V=0.11 的 type effect 在此 noise level 下可能部分是 noise,
1022	    也可能被 noise 掩盖。 但 binary effect (30.2pp ÷ 11.5pp CI width = SNR 2.6) 仍 robust。
1023	
1024	    Unambiguous ICC 0.79 > ambiguous 0.65: ambiguous condition 的 variance 更大—— agent
1025	    在 ambiguous clause 上的 behavior 本身不稳定，进一步削弱 type-level precision。
1026	
1027	    '
1028	  tables:
1029	  - name: ICC by Type
1030	    columns:
1031	    - type
1032	    - ICC_ambiguous
1033	    - ICC_unambiguous
1034	    - ICC_combined
1035	    - max_replicate_swing_pp
1036	    rows:
1037	    - - auth_scope
1038	      - 0.76
1039	      - 0.82
1040	      - 0.74
1041	      - 8.2pp
1042	    - - incompleteness
1043	      - 0.73
1044	      - 0.8
1045	      - 0.72
1046	      - 9.1pp
1047	    - - cond_polysemy
1048	      - 0.67
1049	      - 0.78
1050	      - 0.65
1051	      - 10.5pp
1052	    - - scopal
1053	      - 0.6
1054	      - 0.76
1055	      - 0.58
1056	      - 11.8pp
1057	    - - lexical
1058	      - 0.64
1059	      - 0.77
1060	      - 0.63
1061	      - 10.2pp
1062	    - - coreferential
1063	      - 0.5
1064	      - 0.72
1065	      - 0.48
1066	      - 12.3pp
1067	    - - overall
1068	      - 0.7
1069	      - 0.79
1070	      - 0.68
1071	      - —
1072	  figures_description:
1073	  - ICC forest plot per type with 95% CI — coreferential CI 明显宽于其他 types
1074	  analysis: 'Reliability 数据进一步支撑 "focus on binary, not type": binary effect reliability
1075	    adequate (ICC 0.68 pooled, CI 11.5pp width on 30pp effect), type-level reliability
1076	    insufficient for fine-grained ranking claims (coreferential ICC 0.48, CI 14.8pp
1077	    width on ~5pp type differences)。 Coreferential 的低 reliability 是 compound 问题——clause
1078	    quality + model heterogeneity + sampling noise。 Paper 需 explicitly discuss type-level
1079	    measurement uncertainty。
1080	
1081	    '
1082	- name: realism_validation
1083	  plan_id: plan_007
1084	  description: 'Synthetic clause linguistic properties vs DRIP-R natural ambiguities。
1085	    KS tests on sentence length, parse depth, Flesch-Kincaid, TTR。
1086	
1087	    '
1088	  expected_results:
1089	    ks_sentence_length:
1090	      statistic: 0.18
1091	      p: 0.12
1092	    ks_parse_depth:
1093	      statistic: 0.21
1094	      p: 0.08
1095	    ks_flesch_kincaid:
1096	      statistic: 0.14
1097	      p: 0.23
1098	    ks_ttr:
1099	      statistic: 0.1
1100	      p: 0.41
1101	    synthetic_mean_tokens: 24.2
1102	    drip_r_mean_tokens: 27.8
1103	    synthetic_mean_parse_depth: 3.1
1104	    drip_r_mean_parse_depth: 3.8
1105	    overall_verdict: acceptable
1106	    noted_difference: synthetic clauses slightly shorter and shallower parse trees
1107	      — matched-pair design favors minimal pairs
1108	  result_rationale: 'Realism validation 基本独立于 worst tier: clause 的语言学属性不受 downstream
1109	    实验结果影响。KS tests 大部分 n.s. (p>0.05)—— surface properties 分布相似。Parse depth 边界显著 (p=0.08):
1110	    synthetic clauses 稍简单因为 matched-pair design 倾向 minimal variation。 在 worst tier
1111	    下值得额外注意: 如果 synthetic clauses 系统性简单， 可能 underestimate real-world violation rate
1112	    (更复杂的自然歧义可能更危险)。 但 +30pp binary effect 足够大，不太可能被此 bias 逆转。
1113	
1114	    '
1115	  tables:
1116	  - name: 'Linguistic Property Comparison: Synthetic vs DRIP-R'
1117	    columns:
1118	    - property
1119	    - synthetic_mean
1120	    - DRIP-R_mean
1121	    - KS_statistic
1122	    - p_value
1123	    rows:
1124	    - - sentence_length (tokens)
1125	      - 24.2
1126	      - 27.8
1127	      - 0.18
1128	      - 0.12
1129	    - - parse_depth
1130	      - 3.1
1131	      - 3.8
1132	      - 0.21
1133	      - 0.08
1134	    - - Flesch-Kincaid
1135	      - 12.4
1136	      - 11.8
1137	      - 0.14
1138	      - 0.23
1139	    - - type-token_ratio
1140	      - 0.72
1141	      - 0.7
1142	      - 0.1
1143	      - 0.41
1144	  figures_description:
1145	  - 'Distribution overlay: synthetic vs DRIP-R — sentence length and parse depth 有
1146	    visible but non-significant shift'
1147	  analysis: 'Realism pass。Method 中 disclose parse depth 差异。 Reviewer RC4 应答充分: matched-pair
1148	    design 本身需要 synthetic control, linguistic properties 统计上与自然歧义不可区分。
1149	
1150	    '
1151	- name: judge_calibration
1152	  plan_id: plan_009
1153	  description: '100 episodes stratified by type×model×condition, 2 human annotators,
1154	    LLM judge 校准。 Worst tier: F1 < 0.75 for ≥2 types, type-specific bias 暴露。
1155	
1156	    '
1157	  expected_results:
1158	    human_annotator_kappa: 0.82
1159	    judge_overall_f1: 0.72
1160	    judge_overall_precision: 0.78
1161	    judge_overall_recall: 0.67
1162	    judge_overall_kappa_vs_human: 0.63
1163	    judge_f1_per_type:
1164	      auth_scope: 0.68
1165	      incompleteness: 0.76
1166	      cp: 0.79
1167	      scopal: 0.77
1168	      lexical: 0.74
1169	      coreferential: 0.61
1170	    auth_scope_bias: 'under-detection: recall 0.56, precision 0.82 → misses subtle
1171	      permission boundary crossings'
1172	    coreferential_bias: 'over-detection: recall 0.64, precision 0.58 → flags legitimate
1173	      info-gathering as violations'
1174	    judge_f1_tier1_critical: 0.82
1175	    judge_f1_tier2_moderate: 0.68
1176	    judge_f1_tier3_minor: 0.55
1177	    claude_judged_by_gpt54_f1: 0.75
1178	    gpt54_judged_by_gpt41_f1: 0.69
1179	    cross_judge_asymmetry_pp: 6
1180	    auth_scope_corrected: +4-6pp (true rate likely ~47-49% not 42.8%)
1181	    coreferential_corrected: -5-8pp (true rate likely ~27-30% not 34.8%)
1182	    corrected_cramers_v_estimate: ~0.14 (still weak)
1183	  result_rationale: 'Judge calibration 暴露 worst tier 最有破坏力的 measurement issue:
1184	
1185	    Coreferential F1=0.61: LLM judge over-detect coreferential violations。 原因: agent
1186	    在 RC attachment 歧义下采取的 "exploratory query" (查询哪个 entity 适用) 被 judge 误判为 "unauthorized
1187	    action" (false positive)。 Judge 缺乏 human 的 pragmatic judgment——无法区分 "agent 在探索性确认"
1188	    vs "agent 在违规操作"。 结果: coreferential reported rate (34.8%) 高估 ~5-8pp，真实 rate 可能
1189	    ~27-30%。
1190	
1191	    Auth_scope F1=0.68: judge under-detect auth_scope violations。 原因: auth_scope violation
1192	    常表现为 "subtle permission boundary crossing"—— agent 在模糊授权范围内行动，不明显违规 (如: 给客户 10%
1193	    折扣，policy 说 "reasonable discount" 但未定义 boundary)。Judge 倾向 "不确定则判 non-violation"
1194	    → false negative。 结果: auth_scope reported rate (42.8%) 低估 ~4-6pp，真实 rate 可能 ~47-49%。
1195	
1196	    两个 bias 方向相互作用——恰好压缩了 type 间差异: coreferential 高估 + auth_scope 低估 → 缩小 range →
1197	    降低 V 值。 Bias-corrected V 估计 ~0.14 (vs observed 0.11)——仍 weak, 不改变 "type effect
1198	    弱" 的结论， 但说明 raw V=0.11 有 measurement component。
1199	
1200	    Cross-judge asymmetry 6pp: Claude 被 gpt-5.4 (最强 judge) 判定 F1=0.75， gpt-5.4 被 gpt-4.1
1201	    (较弱 judge) 判定仅 F1=0.69。 弱 judge 对强 model traces 更难准确判定——Method 必须 disclose。
1202	
1203	    Per-severity: tier-3 minor violations F1=0.55 (near random)—— judge 对 "subtle/minor"
1204	    violations 几乎无法判定。 主要影响 severity-weighted analysis, binary violation/non-violation
1205	    受影响较小。
1206	
1207	    '
1208	  tables:
1209	  - name: Judge Calibration by Type
1210	    columns:
1211	    - type
1212	    - precision
1213	    - recall
1214	    - F1
1215	    - bias_direction
1216	    - estimated_rate_correction
1217	    rows:
1218	    - - auth_scope
1219	      - 0.82
1220	      - 0.56
1221	      - 0.68
1222	      - under-detection
1223	      - +4-6pp
1224	    - - incompleteness
1225	      - 0.8
1226	      - 0.72
1227	      - 0.76
1228	      - slight under-detection
1229	      - +1-2pp
1230	    - - cond_polysemy
1231	      - 0.81
1232	      - 0.77
1233	      - 0.79
1234	      - balanced
1235	      - ±1pp
1236	    - - scopal
1237	      - 0.79
1238	      - 0.75
1239	      - 0.77
1240	      - balanced
1241	      - ±1pp
1242	    - - lexical
1243	      - 0.76
1244	      - 0.72
1245	      - 0.74
1246	      - slight over-detection
1247	      - -1-2pp
1248	    - - coreferential
1249	      - 0.58
1250	      - 0.64
1251	      - 0.61
1252	      - over-detection
1253	      - -5-8pp
1254	  - name: Judge Calibration by Severity Tier
1255	    columns:
1256	    - severity
1257	    - n_samples
1258	    - precision
1259	    - recall
1260	    - F1
1261	    rows:
1262	    - - tier-1_critical
1263	      - 35
1264	      - 0.85
1265	      - 0.79
1266	      - 0.82
1267	    - - tier-2_moderate
1268	      - 40
1269	      - 0.73
1270	      - 0.64
1271	      - 0.68
1272	    - - tier-3_minor
1273	      - 25
1274	      - 0.6
1275	      - 0.51
1276	      - 0.55
1277	  - name: Cross-Judge Asymmetry
1278	    columns:
1279	    - agent_model
1280	    - judge_model
1281	    - F1
1282	    - note
1283	    rows:
1284	    - - claude-sonnet-4-6
1285	      - gpt-5.4
1286	      - 0.75
1287	      - strongest judge
1288	    - - gpt-5.4
1289	      - gpt-4.1
1290	      - 0.69
1291	      - weaker judge on stronger agent
1292	    - - gpt-4.1
1293	      - gpt-5.4
1294	      - 0.78
1295	      - strongest judge on mid-tier agent
1296	    - - Qwen3-8B
1297	      - gpt-5.4
1298	      - 0.71
1299	      - open-source traces harder to judge
1300	  figures_description:
1301	  - 'Confusion matrix per type: coreferential FP 区域和 auth_scope FN 区域突出标记'
1302	  - 'Calibration curve: judge confidence vs human agreement — coreferential 偏离对角线最远'
1303	  analysis: 'Judge calibration 是 worst tier 的第二个 structural threat (after model×type
1304	    interaction)。 F1<0.75 for coreferential (0.61) + auth_scope (0.68) 直接削弱这两个 type
1305	    的数值可信度。 Paper 必须: (a) report calibration as standard practice, (b) provide bias-corrected
1306	    estimates, (c) flag coreferential/auth_scope absolute values as measurement-sensitive,
1307	    (d) disclose cross-judge asymmetry in Method。 Silver lining: binary effect 的 calibration
1308	    尚可 (overall F1=0.72, tier-1 F1=0.82)， C1 headline number 受影响最小。bias-corrected
1309	    V ~0.14 仍 weak—— measurement correction 不改变 "type hierarchy 不 robust" 的 worst-tier
1310	    结论。
1311	
1312	    '
1313	- name: classifier_poc
1314	  plan_id: plan_008
1315	  description: 'DeBERTa-v3-large binary ambiguity detector PoC。 Fine-tune on 240 pairs,
1316	    eval on 60 held-out。
1317	
1318	    '
1319	  expected_results:
1320	    model: DeBERTa-v3-large
1321	    train_size: 240
1322	    test_size: 60
1323	    test_f1: 0.78
1324	    test_precision: 0.81
1325	    test_recall: 0.75
1326	    per_type_f1:
1327	      auth_scope: 0.82
1328	      incompleteness: 0.8
1329	      cp: 0.76
1330	      scopal: 0.79
1331	      lexical: 0.77
1332	      coreferential: 0.72
1333	    training_epochs: 5
1334	    best_epoch: 3
1335	  result_rationale: 'F1=0.78 是 reasonable PoC 水平: 证明 binary ambiguity detection 是
1336	    feasible NLP task， 但远未 production-ready。Coreferential F1 最低 (0.72) 与 judge calibration
1337	    (0.61) 和 reliability (ICC 0.48) 的 pattern 一致: coreferential 是最难检测/判定的 type。
1338	
1339	    在 worst tier reframe 下，classifier PoC 强化 reframe (C): "任何 ambiguity detection
1340	    (甚至 binary) 都有巨大安全收益"—— F1=0.78 的 binary detector 在 +30pp violation rate gap 上
1341	    可提供 meaningful early warning。Type-specific detection 既不必要 (type ranking model-dependent)
1342	    也不额外有价值 (binary 已覆盖核心风险)。 这恰好与 worst tier 结论 align: binary detection = high ROI,
1343	    type triage = low ROI。
1344	
1345	    '
1346	  tables:
1347	  - name: Classifier PoC Performance
1348	    columns:
1349	    - metric
1350	    - overall
1351	    - auth_scope
1352	    - incomp
1353	    - CP
1354	    - scopal
1355	    - lexical
1356	    - coref
1357	    rows:
1358	    - - F1
1359	      - 0.78
1360	      - 0.82
1361	      - 0.8
1362	      - 0.76
1363	      - 0.79
1364	      - 0.77
1365	      - 0.72
1366	    - - Precision
1367	      - 0.81
1368	      - 0.85
1369	      - 0.83
1370	      - 0.78
1371	      - 0.82
1372	      - 0.8
1373	      - 0.74
1374	    - - Recall
1375	      - 0.75
1376	      - 0.79
1377	      - 0.77
1378	      - 0.74
1379	      - 0.76
1380	      - 0.74
1381	      - 0.7
1382	  figures_description:
1383	  - 'Per-type F1 bar chart: coreferential 最低, auth_scope 最高'
1384	  - 'Confusion matrix: false negatives 集中在 coreferential 和 CP'
1385	  analysis: 'Classifier PoC 在 worst tier 下反而 perfectly narrative-aligned: binary detection
1386	    feasible (F1=0.78), type-specific pipeline 不必要 (type ranking 本身 model-dependent)。Practical
1387	    contribution 的 optimal framing: 投资 binary detector 而非 type-specific triage pipeline。
1388	    与 C1 massive binary effect + ambiguity blindness 形成 coherent practical story。'
1389	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "21a2d8e0-733a-4269-ab18-51c55b0aeb32",
  "isSidechain": false,
  "promptId": "5178fc38-1c25-4e8e-a8fd-798a18075500",
  "type": "user",
  "uuid": "c93b5c69-9f3b-47b6-94a1-1594f2023a5e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/imagined_experiments.yaml",
      "content": "tier: worst\nnarrative_guidance: 'Layer hierarchy 无法作为 headline claim。5-model pooled layer gap\n  仅 ~4pp (p=0.14, n.s.)， 被 model×type interaction (p=0.008) 瓦解——type ranking 因模型架构而异\n  (GPT 系 spec>ling, Qwen3-8B 反转, Claude 混合)。Judge calibration 暴露 coreferential (F1=0.61)\n  和 auth_scope (F1=0.68) 的 type-specific measurement bias， 进一步削弱 type-level claims。Error\n  analysis failure mode 跨层重叠 42%，无 clean mechanism 区分。 首选 reframe: (C) \"The Massive\n  Binary Effect\" 为 primary——+30pp 仍是文献最大因果效应 + perturbation control PASS (Δ=4.2pp,\n  ratio=0.13)；(B) \"Ambiguity Blindness\" 为 §6 核心—— 92% traces 中 agent 未识别歧义存在，universal\n  across types and models。 C2 降级为 \"Model-Dependent Vulnerability Profiles\" (model×type\n  interaction 从 nuisance 升级为 finding)； C3 layer claim 放弃。备选标题: \"Policy Ambiguity Causes\n  Catastrophic Safety Violations in LLM Agents: A Causal Study\"。仍投 EMNLP——C1 (causal\n  binary effect) + perturbation control + ambiguity blindness analysis = solid 3-contribution\n  paper。\n\n  '\nimagined_experiments:\n- name: full_study_clause_generation\n  plan_id: plan_001\n  description: '生成 140 新 clause pairs (coreferential 50, auth_scope 50, lexical +20,\n    incompleteness +20)， 补全 6 types × 50 pairs = 300 对。混合 CP 格式 (labeled + unlabeled)。Chantree-style\n    质量验证。\n\n    '\n  expected_results:\n    total_pairs: 300\n    pairs_per_type: 50\n    cp_labeled_ratio: 0.5\n    quality_pass_rate: 0.92\n    avg_token_delta_amb_vs_unamb: 3.8\n    coreferential_revision_rounds: 3\n    auth_scope_revision_rounds: 2\n  result_rationale: 'Clause 生成本身不受 worst tier 影响——数据准备阶段。但 quality_pass_rate 92% 而非\n    >95% 因为 coreferential 的 RC attachment 与 scopal 存在边界重叠 (RC8 预示的问题)， 以及 auth_scope\n    与 incompleteness 的 distinction 需要精细控制 (RC9)。 Coreferential 需要 3 轮修订 (vs 常规 1-2\n    轮)：mini-pilot 会暴露 2/5 clauses 触发 conservative refusal 而非 violation，需重写。这些 clause\n    层面的质量差异 会在后续实验中放大为 type-specific measurement noise。\n\n    '\n  tables:\n  - name: Clause Pair Statistics by Type\n    columns:\n    - type\n    - n_pairs\n    - avg_amb_tokens\n    - avg_unamb_tokens\n    - token_delta\n    - quality_pass_rate\n    rows:\n    - - auth_scope\n      - 50\n      - 28.3\n      - 32.1\n      - 3.8\n      - 0.9\n    - - incompleteness\n      - 50\n      - 26.7\n      - 30.5\n      - 3.8\n      - 0.94\n    - - conditional_polysemy\n      - 50\n      - 24.2\n      - 25.8\n      - 1.6\n      - 0.96\n    - - scopal\n      - 50\n      - 22.5\n      - 23.9\n      - 1.4\n      - 0.96\n    - - lexical\n      - 50\n      - 21.8\n      - 23.1\n      - 1.3\n      - 0.94\n    - - coreferential\n      - 50\n      - 25.1\n      - 27.4\n      - 2.3\n      - 0.88\n  figures_description:\n  - 'Token length distribution per type (box plot): spec-layer types 系统性更长，unambiguous\n    版本需更多 explicit information'\n  analysis: 'Coreferential quality_pass_rate 最低 (0.88)，auth_scope 0.90——这两个新 type\n    的 clause 质量问题会在 plan_009 judge calibration 中以 type-specific F1 下降的形式体现。 Token\n    delta spec-layer (3.8) > ling-layer (1.7) 是 potential confound， plan_004 需 report\n    并控制。\n\n    '\n- name: new_type_mini_pilot\n  plan_id: plan_001b\n  description: 'Coreferential + auth_scope 各 5 clauses × 2 conditions × 1 model (gpt-5.4)\n    = 20 episodes。 验证新类型基本可行性。\n\n    '\n  expected_results:\n    coreferential_amb_violation_rate: 0.4\n    coreferential_unamb_violation_rate: 0.0\n    auth_scope_amb_violation_rate: 0.6\n    auth_scope_unamb_violation_rate: 0.0\n    coreferential_binary_effect_pp: 40\n    auth_scope_binary_effect_pp: 60\n    systematic_issues_found: true\n    issues_detail: 2/5 coreferential clauses 触发 conservative refusal 而非 violation;\n      1/5 auth_scope unambiguous 版本仍残余歧义\n  result_rationale: 'Mini-pilot 在 gpt-5.4 上给出 \"go\" 信号——两个新 type 均触发 violations，control\n    < 15%。 但这是 worst tier 的隐患起点: gpt-5.4 的 auth_scope 60% / coreferential 40% pattern\n    看似 confirm spec > ling hierarchy，但 N=5 的 CI 极宽 (±30pp)。 关键: 相同 clauses 在 Qwen3-8B\n    上 profile 会反转 (coreferential ~45%, auth_scope ~28%)—— mini-pilot 仅测 1 model 无法预见跨模型\n    interaction。 gpt-5.4 上 coreferential 2/5 conservative refusal 预示该 type 行为异质性高，\n    但在 mini-pilot 被归为 \"fixable clause quality issue\" 而非 structural warning。\n\n    '\n  tables:\n  - name: Mini-Pilot Results\n    columns:\n    - type\n    - condition\n    - n\n    - violations\n    - rate\n    rows:\n    - - coreferential\n      - ambiguous\n      - 5\n      - 2\n      - 40%\n    - - coreferential\n      - unambiguous\n      - 5\n      - 0\n      - 0%\n    - - auth_scope\n      - ambiguous\n      - 5\n      - 3\n      - 60%\n    - - auth_scope\n      - unambiguous\n      - 5\n      - 0\n      - 0%\n  figures_description: []\n  analysis: 'Mini-pilot 的 \"go\" 信号在 worst tier 下是 misleading confidence: gpt-5.4 single-model\n    validation 无法检测 model-dependent vulnerability profiles。 实际需要 ≥2 model families\n    的 mini-pilot 才能预见 plan_003 的 interaction 问题。\n\n    '\n- name: perturbation_control\n  plan_id: plan_010\n  description: '30 non-ambiguity perturbation pairs (15 synonym substitution + 15\n    clause reordering) × 2 conditions × 3 API models = 180 episodes。验证 ambiguity-specific\n    因果性。\n\n    '\n  expected_results:\n    total_episodes: 180\n    perturbation_delta_pp: 4.2\n    perturbation_ci: '[-1.8, 10.2]'\n    ambiguity_delta_pp: 31.5\n    ambiguity_ci: '[26.8, 36.2]'\n    net_delta_pp: 27.3\n    ratio: 0.13\n    verdict: PASS\n    synonym_substitution_delta_pp: 3.1\n    synonym_ci: '[-3.2, 9.4]'\n    clause_reordering_delta_pp: 5.3\n    clause_reordering_ci: '[-0.8, 11.4]'\n    ci_width_perturbation: 12.0\n  result_rationale: 'Perturbation control 在 worst tier 下仍 PASS——binary effect 的因果性不受\n    layer hierarchy 问题影响。 Δ_perturb=4.2pp (CI 含 0): synonym substitution (3.1pp) 和\n    clause reordering (5.3pp) 均不引起 meaningful violation rate 变化。Ratio=0.13 < 0.15\n    → PASS 最强形式。 Clause reordering 略高 (5.3pp) 源于轻微 primacy/recency effect，但远小于 ambiguity\n    effect。 CI width 12.0pp 接近但未超过 15pp 追加阈值——worst tier 下这是 marginal 风险， 但当前数据足够。这个\n    PASS 是 worst tier 的最大 silver lining: 即使 type hierarchy 崩溃，binary ambiguity effect\n    仍有最强因果证据支撑， 使 reframe (C) \"Massive Binary Effect\" 有坚实因果基础。\n\n    '\n  tables:\n  - name: Perturbation Control Results\n    columns:\n    - condition\n    - violation_rate\n    - Δpp_vs_baseline\n    - 95% CI\n    rows:\n    - - unambiguous_baseline\n      - 5.5%\n      - —\n      - —\n    - - synonym_substitution\n      - 8.6%\n      - +3.1pp\n      - '[-3.2, 9.4]'\n    - - clause_reordering\n      - 10.8%\n      - +5.3pp\n      - '[-0.8, 11.4]'\n    - - perturbation_pooled\n      - 9.7%\n      - +4.2pp\n      - '[-1.8, 10.2]'\n    - - ambiguous\n      - 37.0%\n      - +31.5pp\n      - '[26.8, 36.2]'\n  - name: Perturbation Verdict Summary\n    columns:\n    - metric\n    - value\n    - threshold\n    - verdict\n    rows:\n    - - Δ_perturb\n      - 4.2pp\n      - < 5pp\n      - ✓ PASS\n    - - ratio\n      - '0.13'\n      - < 0.15\n      - ✓ PASS\n    - - CI_contains_0\n      - 'yes'\n      - required\n      - ✓\n    - - CI_width\n      - 12.0pp\n      - < 15pp\n      - ✓ (marginal)\n  figures_description:\n  - 'Bar chart: baseline / perturbation / ambiguity 三条件 violation rate + CI — ambiguity\n    远超其余两条件'\n  analysis: 'PASS verdict 确保 C1 因果 claim 在任何 tier 下成立。 这是 paper 的 methodological backbone——区别于所有\n    prior work (DRIP-R, PhantomPolicy 均无此控制)。\n\n    '\n- name: full_study_api\n  plan_id: plan_002\n  description: '300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6)\n    = 1,800 episodes。 在原 2-model 基础上新增 Claude。Cross-judge evaluation。\n\n    '\n  expected_results:\n    total_episodes: 1800\n    gpt54_rates:\n      auth_scope: 0.55\n      incompleteness: 0.52\n      cp: 0.35\n      scopal: 0.4\n      lexical: 0.38\n      coreferential: 0.25\n    gpt41_rates:\n      auth_scope: 0.53\n      incompleteness: 0.5\n      cp: 0.34\n      scopal: 0.39\n      lexical: 0.36\n      coreferential: 0.24\n    claude_rates:\n      auth_scope: 0.38\n      incompleteness: 0.36\n      cp: 0.28\n      scopal: 0.33\n      lexical: 0.3\n      coreferential: 0.42\n    gpt54_binary_effect_pp: 36.2\n    gpt41_binary_effect_pp: 34.0\n    claude_binary_effect_pp: 26.5\n    gpt54_layer_gap_pp: 13.0\n    gpt41_layer_gap_pp: 12.7\n    claude_layer_gap_pp: -1.0\n    binary_effect_3api_pp: 32.7\n    layer_gap_3api_pp: 8.2\n    cramers_v_3api: 0.15\n    model_main_effect_p_3api: 0.004\n    model_type_interaction_p_3api: 0.018\n    avg_unamb_rate_3api: 0.055\n    claude_unamb_rate: 0.08\n    claude_amb_avg: 0.345\n  result_rationale: 'GPT 系 (gpt-5.4, gpt-4.1) 复现 plan_002 原始 pattern: spec >> ling，两模型高度一致\n    (rank ρ=0.94)。GPT 对 authorization boundary 和 incompleteness 的 pragmatic underspecification\n    高度敏感——缺乏 explicit permission 时倾向 assume-and-act。\n\n    Claude 展现截然不同的 vulnerability profile——worst tier 的第一个转折点: (a) auth_scope/incompleteness\n    显著低 (38%/36% vs GPT 55%/52%): Claude RLHF 训练 强化了 \"不确定时 refuse\" 的行为，specification-layer\n    ambiguity 更多触发 refusal 而非 violation。 (b) coreferential 显著高 (42% vs GPT 25%): Claude\n    在 RC attachment 歧义上 系统性选择 wider-scope interpretation (执行而非收窄)。RC attachment 不触发\n    Claude 的 safety refusal mechanism (与 auth boundary 不同)，因此 Claude 在此 \"放松警惕\"。 (c)\n    结果: Claude layer gap 反转 (ling 35.0% > spec 34.0%)。 3-API pooled layer gap 从 2-model\n    的 19pp 压缩至 8.2pp。\n\n    Model×type interaction 已在 3 API 模型中显著 (p=0.018)—— 尚未加入 Qwen 就已可见 type ranking\n    非 universal。 Claude binary effect 仅 +26.5pp: 整体更保守 (unamb baseline 8% vs GPT ~4.5%),\n    ambiguous 条件下更多 refuse/ask 而非 violate。\n\n    '\n  tables:\n  - name: Per-Model Per-Type Violation Rates (Ambiguous Condition)\n    columns:\n    - type\n    - layer\n    - gpt-5.4\n    - gpt-4.1\n    - claude-sonnet-4-6\n    - 3-API_pooled\n    rows:\n    - - auth_scope\n      - spec\n      - 55%\n      - 53%\n      - 38%\n      - 48.7%\n    - - incompleteness\n      - spec\n      - 52%\n      - 50%\n      - 36%\n      - 46.0%\n    - - cond_polysemy\n      - spec\n      - 35%\n      - 34%\n      - 28%\n      - 32.3%\n    - - scopal\n      - ling\n      - 40%\n      - 39%\n      - 33%\n      - 37.3%\n    - - lexical\n      - ling\n      - 38%\n      - 36%\n      - 30%\n      - 34.7%\n    - - coreferential\n      - ling\n      - 25%\n      - 24%\n      - 42%\n      - 30.3%\n    - - spec_avg\n      - —\n      - 47.3%\n      - 45.7%\n      - 34.0%\n      - 42.3%\n    - - ling_avg\n      - —\n      - 34.3%\n      - 33.0%\n      - 35.0%\n      - 34.1%\n    - - layer_gap\n      - —\n      - +13.0pp\n      - +12.7pp\n      - -1.0pp\n      - +8.2pp\n  - name: Binary Effect by API Model\n    columns:\n    - model\n    - amb_rate\n    - unamb_rate\n    - Δpp\n    - McNemar_OR\n    - p\n    rows:\n    - - gpt-5.4\n      - 40.8%\n      - 4.6%\n      - +36.2pp\n      - 38.5\n      - <0.0001\n    - - gpt-4.1\n      - 39.3%\n      - 5.3%\n      - +34.0pp\n      - 31.2\n      - <0.0001\n    - - claude-sonnet-4-6\n      - 34.5%\n      - 8.0%\n      - +26.5pp\n      - 16.8\n      - <0.0001\n    - - 3-API_pooled\n      - 38.2%\n      - 5.5%\n      - +32.7pp\n      - 28.4\n      - <0.0001\n  figures_description:\n  - 'Heatmap 3×6: 清晰显示 Claude coreferential 异常高 (42%) 与 auth_scope 异常低 (38%)——与 GPT\n    系对角相反'\n  - 'Forest plot: per-type binary effect by model with 95% CI — Claude CI 与 GPT 不重叠\n    (auth_scope, coreferential)'\n  analysis: 'Claude 的加入将 3-API layer gap 压缩至 8.2pp (从 2-model 19pp)。 model×type interaction\n    已显著 (p=0.018)——plan_003 加入 Qwen 后会进一步恶化。 Claude 的 coreferential 高 rate 机制: RLHF\n    的 safety training 覆盖了 authorization-class violations 但不覆盖 referential-class misinterpretation，导致\n    asymmetric vulnerability。 C3 (universal layer hierarchy) 在此阶段已不可维持。\n\n    '\n- name: full_study_local\n  plan_id: plan_003\n  description: '300 clauses × 2 conditions × 2 local models (Qwen3-8B, Qwen3-32B-AWQ\n    via vLLM) = 1,200 episodes。 48 GPU-hours on RTX PRO 6000。\n\n    '\n  expected_results:\n    total_episodes: 1200\n    qwen8b_rates:\n      auth_scope: 0.28\n      incompleteness: 0.3\n      cp: 0.25\n      scopal: 0.32\n      lexical: 0.3\n      coreferential: 0.45\n    qwen8b_binary_effect_pp: 23.7\n    qwen8b_unamb_rate: 0.08\n    qwen8b_amb_avg: 0.317\n    qwen8b_layer_gap_pp: -8.0\n    qwen8b_spec_avg: 0.277\n    qwen8b_ling_avg: 0.357\n    qwen32b_rates:\n      auth_scope: 0.4\n      incompleteness: 0.42\n      cp: 0.3\n      scopal: 0.35\n      lexical: 0.33\n      coreferential: 0.38\n    qwen32b_binary_effect_pp: 30.3\n    qwen32b_unamb_rate: 0.06\n    qwen32b_amb_avg: 0.363\n    qwen32b_layer_gap_pp: 2.0\n    qwen32b_spec_avg: 0.373\n    qwen32b_ling_avg: 0.353\n    binary_effect_2local_pp: 27.0\n    layer_gap_2local_pp: -3.0\n    model_type_interaction_2local_p: 0.041\n  result_rationale: 'Qwen3-8B 是 worst tier 的关键变量——vulnerability profile 质变:\n\n    (a) Auth_scope 仅 28% (GPT-5.4 的一半): 8B 参数模型缺乏 pragmatic reasoning 能力， 无法 \"推断\"\n    implicit permission boundary 并据此行动——不是因为保守 refuse (像 Claude)， 而是因为根本不理解 authorization\n    的 pragmatic implication，倾向 ignore 或 default 行为。 低 auth_scope violation ≠ 安全，只是不同的\n    failure mode (inaction vs wrong action)。\n\n    (b) Coreferential 高达 45% (GPT-5.4 的 1.8 倍): 小模型更依赖 surface syntactic heuristics\n    (如 left-attachment bias for RC)。GPT-5.4 能利用 tool response 做部分 disambiguation (Berry\n    & Kamsties 的 \"disambiguation channel\")，Qwen3-8B 不具备此能力—— 对 linguistic-layer 反而更脆弱。\n\n    (c) Layer gap 反转至 -8pp (ling 35.7% > spec 27.7%): 完全颠覆 GPT 的 spec > ling pattern。\n    机制: 小模型的 pragmatic processing 不足使 spec-layer 失去 \"特别危险\" 的地位， 而 syntactic processing\n    的 surface heuristic 依赖使 ling-layer 变得更危险。\n\n    Qwen3-32B-AWQ 居中 (gap +2pp, nearly flat): scale 部分恢复了 spec-layer sensitivity，\n    但未达 GPT 水平。AWQ 4-bit 量化可能引入额外 noise 但不改变 qualitative pattern。 这支持 \"layer gap 是\n    emergent capability\"——需要足够的 pragmatic reasoning 能力 才能 \"解锁\" specification-layer\n    的特殊危险性。\n\n    '\n  tables:\n  - name: Per-Model Per-Type Violation Rates (Local Models, Ambiguous)\n    columns:\n    - type\n    - layer\n    - Qwen3-8B\n    - Qwen3-32B-AWQ\n    - 2-local_pooled\n    rows:\n    - - auth_scope\n      - spec\n      - 28%\n      - 40%\n      - 34.0%\n    - - incompleteness\n      - spec\n      - 30%\n      - 42%\n      - 36.0%\n    - - cond_polysemy\n      - spec\n      - 25%\n      - 30%\n      - 27.5%\n    - - scopal\n      - ling\n      - 32%\n      - 35%\n      - 33.5%\n    - - lexical\n      - ling\n      - 30%\n      - 33%\n      - 31.5%\n    - - coreferential\n      - ling\n      - 45%\n      - 38%\n      - 41.5%\n    - - spec_avg\n      - —\n      - 27.7%\n      - 37.3%\n      - 32.5%\n    - - ling_avg\n      - —\n      - 35.7%\n      - 35.3%\n      - 35.5%\n    - - layer_gap\n      - —\n      - -8.0pp\n      - +2.0pp\n      - -3.0pp\n  - name: Binary Effect by Local Model\n    columns:\n    - model\n    - amb_rate\n    - unamb_rate\n    - Δpp\n    - McNemar_OR\n    - p\n    rows:\n    - - Qwen3-8B\n      - 31.7%\n      - 8.0%\n      - +23.7pp\n      - 9.4\n      - <0.0001\n    - - Qwen3-32B-AWQ\n      - 36.3%\n      - 6.0%\n      - +30.3pp\n      - 21.7\n      - <0.0001\n  figures_description:\n  - 'Radar chart 5 models × 6 types: Qwen3-8B profile 与 GPT 系近似镜像——coreferential 峰值、auth_scope\n    谷底'\n  - 'Layer gap by model bar chart: GPT 正、Claude/Qwen3-32B 近零、Qwen3-8B 负——gradient\n    随 model capability'\n  analysis: 'Qwen3-8B 的 reversed layer profile 是 worst tier 的 smoking gun。 与 GPT-5.4\n    的 type rank Spearman ρ=0.37 (weak)——两个模型本质上有不同的 vulnerability landscape。 Qwen3-32B\n    的 ρ=0.77 (moderate) 说明 scale 恢复了部分 alignment，但未完全收敛。 Binary effect 仍显著 (Qwen3-8B\n    +23.7pp, p<0.0001)——ambiguity 对所有模型都有害， 但 \"哪种 ambiguity 更有害\" 取决于模型能力。\n\n    '\n- name: full_study_analysis\n  plan_id: plan_004\n  description: '3,000 episodes 统计分析: C1 binary effect, C2 type hierarchy, C3 layer\n    effect, C4 model×type interaction, power analysis, TOST, inter-model agreement,\n    information delta control。\n\n    '\n  expected_results:\n    binary_effect_5model_pp: 30.2\n    binary_effect_5model_ci: '[27.5, 32.9]'\n    mcnemar_or_5model: 24.1\n    mcnemar_or_ci: '[16.3, 35.6]'\n    mcnemar_p: <0.0001\n    per_type_all_significant: true\n    weakest_type_effect: coreferential +22.8pp (Qwen3-8B drags avg down from +16pp\n      to... wait, UP — Qwen3-8B has high coreferential)\n    omnibus_chi2_5model: 18.7\n    omnibus_p_5model: 0.002\n    cramers_v_5model: 0.11\n    pooled_rates:\n      auth_scope: 42.8%\n      incompleteness: 42.0%\n      cp: 30.4%\n      scopal: 35.8%\n      lexical: 33.4%\n      coreferential: 34.8%\n    spec_avg_5model: 38.4%\n    ling_avg_5model: 34.7%\n    layer_gap_5model_pp: 3.7\n    layer_gap_ci: '[-1.2, 8.6]'\n    layer_gap_p: 0.14\n    model_type_interaction_chi2: 52.3\n    model_type_interaction_p: 0.008\n    model_type_interaction_v: 0.089\n    model_main_effect_p: 0.001\n    model_main_effect_v: 0.072\n    interaction_lrt_chi2: 38.6\n    interaction_lrt_p: 0.003\n    interaction_lrt_df: 20\n    rank_rho_gpt41: 0.94\n    rank_rho_claude: 0.54\n    rank_rho_qwen32b: 0.77\n    rank_rho_qwen8b: 0.37\n    tost_15pp_equivalent_pairs: 6/15\n    tost_10pp_equivalent_pairs: 2/15\n    mde_c2_v: 0.18\n    mde_c3_pp: 9.5\n    observed_c2_v: 0.11\n    observed_c3_gap: 3.7\n    fleiss_kappa_ambiguous: 0.62\n    fleiss_kappa_unambiguous: 0.85\n    same_interpretation_pct_ambiguous: 0.58\n    different_interpretation_pct_ambiguous: 0.42\n    avg_token_delta_spec: 3.4\n    avg_token_delta_ling: 1.7\n    token_delta_violation_corr: 0.31\n    token_delta_partial_r_after_type: 0.14\n  result_rationale: 'C1 (+30.2pp, CI [27.5, 32.9]): 从 plan_002 的 +36.5pp 下降 6pp。 原因:\n    Qwen3-8B 的弱 binary effect (+23.7pp) 和 Claude 的 (+26.5pp) 拉低 pooled 值。 但 CI 远离零，OR=24.1\n    仍 massive——文献中最大的 ambiguity → safety 因果效应。 Per-type 均显著 (最弱: CP +25.6pp)——\"所有\n    ambiguity 都 nocuous\" 成立。\n\n    C2 (V=0.11, p=0.002): omnibus χ² 显著说明 types 不完全等价， 但 V=0.11 (weak) 远低于 plan_002\n    2-model 的 V=0.207。 原因: open-source 模型的 reversed/flat profile 平均化了 type 间差异。 具体看:\n    auth_scope/incompleteness 仍最高 (~43%)，但 coreferential 从 25% 跳至 34.8% (Claude 42%\n    + Qwen3-8B 45% 拉高)，压缩了原本的 range。 TOST: ±15pp 有 6/15 pairs equivalent (原 3/15)——更多\n    type pairs 在统计上不可区分。\n\n    C3 (gap 3.7pp, p=0.14, n.s.): layer gap 不显著。CI [-1.2, 8.6] 包含 0。 GPT 的 positive\n    gap (~13pp) 被 Claude (-1pp) + Qwen3-8B (-8pp) 抵消。 MDE=9.5pp: 即使有 power，跨模型方向不一致使\n    pooled estimate 本身无 interpretive value。 Layer hierarchy 从 \"finding\" 变为 \"GPT-family\n    tendency\"。\n\n    C4 (interaction p=0.008): worst tier 最 informative finding。 5×6 contingency table\n    中 model×type interaction 高度显著——type ranking 是 model-dependent。 Three distinct\n    vulnerability profiles: - GPT family: spec-sensitive (auth_scope/incompleteness\n    peak) - Claude: coreferential-sensitive (RLHF safety coverage gap) - Qwen3-8B:\n    ling-sensitive (surface heuristic dependence) Spearman ρ gradient: GPT intra-family\n    0.94 > Qwen3-32B 0.77 > Claude 0.54 > Qwen3-8B 0.37\n\n    Inter-model Fleiss κ=0.62 (ambiguous) vs 0.85 (unambiguous): 分歧主要在 ambiguous clauses——ambiguity\n    暴露了 model-specific interpretation strategies。 58% same interpretation → 不是 true\n    nocuity (divergent readings) 而是 systematic bias (models differ in fallback strategies\n    when they can''t resolve ambiguity)。 Berry & Kamsties 框架下: 这是 \"systematic nocuity\"\n    (所有模型都错但错法不同) 而非 \"divergent nocuity\" (不同解读)。\n\n    Token delta: spec-layer 3.4 vs ling-layer 1.7 tokens，与 violation rate 弱相关 (r=0.31)。\n    但 partial correlation after controlling for type = 0.14 (n.s.)—— token delta 不是\n    independent confound，与 type 共线。需 disclose 但不构成 fatal threat。\n\n    '\n  tables:\n  - name: 5-Model Pooled Per-Type Results\n    columns:\n    - type\n    - layer\n    - amb_rate\n    - unamb_rate\n    - Δpp\n    - 95% CI\n    - per-type McNemar p\n    rows:\n    - - auth_scope\n      - spec\n      - 42.8%\n      - 5.8%\n      - +37.0pp\n      - '[31.2, 42.8]'\n      - <0.0001\n    - - incompleteness\n      - spec\n      - 42.0%\n      - 5.4%\n      - +36.6pp\n      - '[30.8, 42.4]'\n      - <0.0001\n    - - cond_polysemy\n      - spec\n      - 30.4%\n      - 4.8%\n      - +25.6pp\n      - '[20.1, 31.1]'\n      - <0.0001\n    - - scopal\n      - ling\n      - 35.8%\n      - 5.6%\n      - +30.2pp\n      - '[24.5, 35.9]'\n      - <0.0001\n    - - lexical\n      - ling\n      - 33.4%\n      - 5.2%\n      - +28.2pp\n      - '[22.6, 33.8]'\n      - <0.0001\n    - - coreferential\n      - ling\n      - 34.8%\n      - 6.0%\n      - +28.8pp\n      - '[23.1, 34.5]'\n      - <0.0001\n  - name: Layer Effect by Model\n    columns:\n    - model\n    - spec_avg\n    - ling_avg\n    - layer_gap_pp\n    - direction\n    rows:\n    - - gpt-5.4\n      - 47.3%\n      - 34.3%\n      - +13.0pp\n      - spec > ling\n    - - gpt-4.1\n      - 45.7%\n      - 33.0%\n      - +12.7pp\n      - spec > ling\n    - - claude-sonnet-4-6\n      - 34.0%\n      - 35.0%\n      - -1.0pp\n      - ≈ flat (reversed)\n    - - Qwen3-32B-AWQ\n      - 37.3%\n      - 35.3%\n      - +2.0pp\n      - ≈ flat\n    - - Qwen3-8B\n      - 27.7%\n      - 35.7%\n      - -8.0pp\n      - ling > spec (reversed)\n    - - 5-model_pooled\n      - 38.4%\n      - 34.7%\n      - +3.7pp\n      - n.s. (p=0.14)\n  - name: 'Model × Type Interaction: Type Rank by Model (ambiguous violation rate)'\n    columns:\n    - rank\n    - gpt-5.4\n    - gpt-4.1\n    - claude\n    - Qwen3-32B\n    - Qwen3-8B\n    rows:\n    - - 1 (highest)\n      - auth_scope\n      - auth_scope\n      - coreferential\n      - incompleteness\n      - coreferential\n    - - 2\n      - incompleteness\n      - incompleteness\n      - auth_scope\n      - auth_scope\n      - scopal\n    - - 3\n      - scopal\n      - scopal\n      - incompleteness\n      - coreferential\n      - lexical\n    - - 4\n      - lexical\n      - lexical\n      - scopal\n      - scopal\n      - incompleteness\n    - - 5\n      - CP\n      - CP\n      - lexical\n      - lexical\n      - auth_scope\n    - - 6 (lowest)\n      - coreferential\n      - coreferential\n      - CP\n      - CP\n      - CP\n  - name: Inter-Model Agreement (Berry & Kamsties Analysis)\n    columns:\n    - metric\n    - ambiguous\n    - unambiguous\n    - interpretation\n    rows:\n    - - Fleiss_κ\n      - 0.62\n      - 0.85\n      - moderate vs almost-perfect\n    - - same_interpretation_pct\n      - 58%\n      - 91%\n      - ambiguity drives divergence\n    - - systematic_bias_pct\n      - 34%\n      - 7%\n      - models differ in fallback strategy\n    - - random_disagreement_pct\n      - 8%\n      - 2%\n      - noise floor\n  figures_description:\n  - 'Forest plot: per-type 5-model pooled binary effect with 95% CI — C1 headline\n    figure, all types significant'\n  - 'Model×Type heatmap: 5 models × 6 types, color-coded — cross-pattern clearly visible'\n  - 'Layer gap by model: bar chart with CI showing GPT positive, Qwen3-8B negative,\n    others near zero'\n  - 'Parallel coordinates: type rank across 5 models — lines crossing extensively\n    (no stable ranking)'\n  - 'Scatter: token delta vs violation rate per type, with partial regression line'\n  analysis: 'Plan_004 是 worst tier 定性的核心。三个结论: (1) C1 survives robustly: +30.2pp 是\n    massive causal effect, 6 types all significant, perturbation-backed。 (2) C2/C3\n    collapse: V=0.11 weak, layer gap n.s.——不能声称 universal type hierarchy。 但 interaction\n    显著 (p=0.008) 说明 types 确实 differently dangerous——只是 \"哪个更危险\" 是 model-dependent。\n    (3) C4 升级为 secondary finding: three vulnerability profiles (GPT spec-sensitive,\n    Claude coref-sensitive, Qwen8B ling-sensitive) 是 novel 且 practically relevant\n    insight。 Reframe: layer hierarchy → model-dependent vulnerability profiles。\n\n    '\n- name: error_analysis\n  plan_id: plan_005\n  description: '300 violation traces (50/type) 定性分析。Failure mode 分类、 跨层区分检验、ambiguity\n    blindness 量化、model-specific pattern 分析。\n\n    '\n  expected_results:\n    total_traces_sampled: 300\n    failure_modes:\n      assumption_based_action: 38%\n      scope_misapplication: 22%\n      conservative_refusal: 15%\n      arbitrary_rule_selection: 14%\n      permission_escalation: 11%\n    failure_mode_layer_match_pct: 42\n    assumption_in_spec_pct: 40\n    assumption_in_ling_pct: 36\n    scope_misapplication_in_spec_pct: 18\n    scope_misapplication_in_ling_pct: 26\n    explicit_ambiguity_mention_pct: 8\n    implicit_deliberation_pct: 20\n    surface_adoption_pct: 72\n    gpt54_assumption_pct: 45\n    gpt54_explicit_mention_pct: 12\n    claude_conservative_refusal_pct: 28\n    claude_explicit_mention_pct: 6\n    qwen8b_surface_adoption_pct: 85\n    qwen8b_explicit_mention_pct: 2\n  result_rationale: 'Cross-layer failure mode overlap 42%: 如果 layer 是 deterministic\n    predictor of failure mechanism， match 应接近 80%+。实际仅 42% 说明 failure mode 不由 layer\n    决定。 \"Assumption-based action\" (遇到歧义直接假设一种解读并执行) 是 dominant mode， 且在两个 layer 上近乎等比例\n    (spec 40%, ling 36%)—— agent 的 failure mechanism 是 universal 的 \"guess and act\"\n    而非 type-specific misparse。\n\n    反直觉: scope_misapplication 在 ling-layer (26%) > spec-layer (18%)—— 因为 scopal/coreferential\n    的 syntactic structure 确实触发更多 scope parsing error， 而 spec-layer 的 failure 更多是 \"assume\n    permission exists\" (assumption-based)。 但这个差异不足以支撑 clean layer mechanism story——两个\n    layer 都有大量 assumption-based failures。\n\n    Ambiguity blindness: 92% traces 中 agent 未 meta-cognitively 识别歧义。 这是 universal\n    现象——所有模型所有 types 都展现。差异仅在 degree: GPT-5.4 有 12% explicit mention (最高, 但仍极低)，Qwen3-8B\n    仅 2% (近乎完全 blind)。 Claude 的 conservative_refusal 28% (远高于平均) 解释了其低 auth_scope\n    rate: Claude refuse 而非 violate，但这不是 ambiguity awareness—— 是 safety training 的\n    blanket conservatism，不区分 ambiguous vs unambiguous uncertainty。\n\n    Model-specific failure patterns 直接支撑 C4: GPT 的 assumption_based 45% (aggressive\n    interpretation) vs Claude 的 refusal 28% (conservative) vs Qwen3-8B 的 surface_adoption\n    85% (uncritical execution)—— 三种 distinct failure strategies，对应三种 vulnerability\n    profiles。\n\n    '\n  tables:\n  - name: Failure Mode Distribution by Layer\n    columns:\n    - failure_mode\n    - spec_layer\n    - ling_layer\n    - pooled\n    - layer_specificity\n    rows:\n    - - assumption_based_action\n      - 40%\n      - 36%\n      - 38%\n      - low (Δ=4pp)\n    - - scope_misapplication\n      - 18%\n      - 26%\n      - 22%\n      - moderate (ling-biased)\n    - - conservative_refusal\n      - 14%\n      - 16%\n      - 15%\n      - low (Δ=2pp)\n    - - arbitrary_rule_selection\n      - 16%\n      - 12%\n      - 14%\n      - low (Δ=4pp)\n    - - permission_escalation\n      - 12%\n      - 10%\n      - 11%\n      - low (Δ=2pp)\n  - name: Ambiguity Awareness in Agent Traces by Model\n    columns:\n    - awareness_level\n    - gpt-5.4\n    - gpt-4.1\n    - claude\n    - Qwen3-32B\n    - Qwen3-8B\n    - pooled\n    rows:\n    - - explicit_mention\n      - 12%\n      - 10%\n      - 6%\n      - 5%\n      - 2%\n      - 8%\n    - - implicit_deliberation\n      - 25%\n      - 22%\n      - 24%\n      - 18%\n      - 13%\n      - 20%\n    - - surface_adoption\n      - 63%\n      - 68%\n      - 70%\n      - 77%\n      - 85%\n      - 72%\n  - name: Failure Mode by Model\n    columns:\n    - model\n    - assumption_based\n    - scope_misapplication\n    - conservative_refusal\n    - arbitrary_rule\n    - permission_escalation\n    rows:\n    - - gpt-5.4\n      - 45%\n      - 24%\n      - 8%\n      - 13%\n      - 10%\n    - - gpt-4.1\n      - 42%\n      - 23%\n      - 10%\n      - 15%\n      - 10%\n    - - claude\n      - 22%\n      - 18%\n      - 28%\n      - 16%\n      - 16%\n    - - Qwen3-32B\n      - 38%\n      - 22%\n      - 14%\n      - 14%\n      - 12%\n    - - Qwen3-8B\n      - 43%\n      - 20%\n      - 12%\n      - 15%\n      - 10%\n  figures_description:\n  - 'Sankey diagram: type → failure mode → outcome — 高度交叉流动，无 clean type→mode mapping'\n  - 'Annotated trace pair: spec-layer (auth_scope) vs ling-layer (coreferential) 的\n    assumption-based action — 几乎 identical reasoning pattern'\n  - 'Ambiguity blindness spectrum: 5 models 在 explicit↔surface 连续体上的位置'\n  analysis: 'Error analysis 无法支撑 layer-specific failure mechanism 叙事 (failure_mode_layer_match\n    仅 42%)， 但强力支撑 \"Ambiguity Blindness\" 作为 §6 核心: 92% traces 展现 blindness 是 universal\n    现象——所有模型在所有 type 上 都无法 meta-cognitively detect ambiguity。这连接 Ferreira 的 good-enough\n    processing: agents 对 grammatically fluent ambiguous clauses 做 shallow parse and\n    act， 不触发 reanalysis/clarification。 Practical implication: 与其按 type 排序 (ranking\n    model-dependent)， 不如投资 any-ambiguity detection——因为 agent 本身 blind to all types\n    equally。 这完美 align reframe (C) binary effect + (B) blindness mechanism。\n\n    '\n- name: reliability_test\n  plan_id: plan_006\n  description: '30 clauses (5/type) × 3 replicates × 2 conditions × 5 models = 900\n    episodes。 Test-retest ICC, bootstrap CI width。\n\n    '\n  expected_results:\n    total_episodes: 900\n    icc_overall: 0.68\n    icc_per_type:\n      auth_scope: 0.74\n      incompleteness: 0.72\n      cp: 0.65\n      scopal: 0.58\n      lexical: 0.63\n      coreferential: 0.48\n    bootstrap_ci_width_binary_effect_pp: 11.5\n    bootstrap_ci_width_per_type_pp: 14.8\n    max_replicate_swing_pp: 12.3\n    max_swing_type: coreferential\n    icc_ambiguous_only: 0.65\n    icc_unambiguous_only: 0.79\n  result_rationale: 'Overall ICC 0.68 (moderate): 可接受但不 excellent。 Signature worst-tier\n    pattern: (a) Auth_scope/incompleteness 最 reliable (0.74/0.72): 高 violation rate\n    type 的 absolute swing 对 ICC 影响较小 (±8pp on 43% base vs ±8pp on 35% base)。 (b) Coreferential\n    最 unreliable (0.48): 三重叠加效应—— clause 质量 (plan_001 pass_rate 0.88) × 跨模型行为异质 (Qwen3-8B\n    45% vs GPT 25%) × API temperature sampling noise。这三者使 coreferential replicate\n    variance 极大。 (c) Scopal ICC 0.58: 与 MVP→plan_002 的 51.7%→40% historical swing\n    一致。\n\n    Bootstrap CI width 11.5pp (binary effect) 超过 <10pp 理想阈值: per-type CI width 14.8pp\n    更宽——type-level 比较 power 有限。 V=0.11 的 type effect 在此 noise level 下可能部分是 noise,\n    也可能被 noise 掩盖。 但 binary effect (30.2pp ÷ 11.5pp CI width = SNR 2.6) 仍 robust。\n\n    Unambiguous ICC 0.79 > ambiguous 0.65: ambiguous condition 的 variance 更大—— agent\n    在 ambiguous clause 上的 behavior 本身不稳定，进一步削弱 type-level precision。\n\n    '\n  tables:\n  - name: ICC by Type\n    columns:\n    - type\n    - ICC_ambiguous\n    - ICC_unambiguous\n    - ICC_combined\n    - max_replicate_swing_pp\n    rows:\n    - - auth_scope\n      - 0.76\n      - 0.82\n      - 0.74\n      - 8.2pp\n    - - incompleteness\n      - 0.73\n      - 0.8\n      - 0.72\n      - 9.1pp\n    - - cond_polysemy\n      - 0.67\n      - 0.78\n      - 0.65\n      - 10.5pp\n    - - scopal\n      - 0.6\n      - 0.76\n      - 0.58\n      - 11.8pp\n    - - lexical\n      - 0.64\n      - 0.77\n      - 0.63\n      - 10.2pp\n    - - coreferential\n      - 0.5\n      - 0.72\n      - 0.48\n      - 12.3pp\n    - - overall\n      - 0.7\n      - 0.79\n      - 0.68\n      - —\n  figures_description:\n  - ICC forest plot per type with 95% CI — coreferential CI 明显宽于其他 types\n  analysis: 'Reliability 数据进一步支撑 \"focus on binary, not type\": binary effect reliability\n    adequate (ICC 0.68 pooled, CI 11.5pp width on 30pp effect), type-level reliability\n    insufficient for fine-grained ranking claims (coreferential ICC 0.48, CI 14.8pp\n    width on ~5pp type differences)。 Coreferential 的低 reliability 是 compound 问题——clause\n    quality + model heterogeneity + sampling noise。 Paper 需 explicitly discuss type-level\n    measurement uncertainty。\n\n    '\n- name: realism_validation\n  plan_id: plan_007\n  description: 'Synthetic clause linguistic properties vs DRIP-R natural ambiguities。\n    KS tests on sentence length, parse depth, Flesch-Kincaid, TTR。\n\n    '\n  expected_results:\n    ks_sentence_length:\n      statistic: 0.18\n      p: 0.12\n    ks_parse_depth:\n      statistic: 0.21\n      p: 0.08\n    ks_flesch_kincaid:\n      statistic: 0.14\n      p: 0.23\n    ks_ttr:\n      statistic: 0.1\n      p: 0.41\n    synthetic_mean_tokens: 24.2\n    drip_r_mean_tokens: 27.8\n    synthetic_mean_parse_depth: 3.1\n    drip_r_mean_parse_depth: 3.8\n    overall_verdict: acceptable\n    noted_difference: synthetic clauses slightly shorter and shallower parse trees\n      — matched-pair design favors minimal pairs\n  result_rationale: 'Realism validation 基本独立于 worst tier: clause 的语言学属性不受 downstream\n    实验结果影响。KS tests 大部分 n.s. (p>0.05)—— surface properties 分布相似。Parse depth 边界显著 (p=0.08):\n    synthetic clauses 稍简单因为 matched-pair design 倾向 minimal variation。 在 worst tier\n    下值得额外注意: 如果 synthetic clauses 系统性简单， 可能 underestimate real-world violation rate\n    (更复杂的自然歧义可能更危险)。 但 +30pp binary effect 足够大，不太可能被此 bias 逆转。\n\n    '\n  tables:\n  - name: 'Linguistic Property Comparison: Synthetic vs DRIP-R'\n    columns:\n    - property\n    - synthetic_mean\n    - DRIP-R_mean\n    - KS_statistic\n    - p_value\n    rows:\n    - - sentence_length (tokens)\n      - 24.2\n      - 27.8\n      - 0.18\n      - 0.12\n    - - parse_depth\n      - 3.1\n      - 3.8\n      - 0.21\n      - 0.08\n    - - Flesch-Kincaid\n      - 12.4\n      - 11.8\n      - 0.14\n      - 0.23\n    - - type-token_ratio\n      - 0.72\n      - 0.7\n      - 0.1\n      - 0.41\n  figures_description:\n  - 'Distribution overlay: synthetic vs DRIP-R — sentence length and parse depth 有\n    visible but non-significant shift'\n  analysis: 'Realism pass。Method 中 disclose parse depth 差异。 Reviewer RC4 应答充分: matched-pair\n    design 本身需要 synthetic control, linguistic properties 统计上与自然歧义不可区分。\n\n    '\n- name: judge_calibration\n  plan_id: plan_009\n  description: '100 episodes stratified by type×model×condition, 2 human annotators,\n    LLM judge 校准。 Worst tier: F1 < 0.75 for ≥2 types, type-specific bias 暴露。\n\n    '\n  expected_results:\n    human_annotator_kappa: 0.82\n    judge_overall_f1: 0.72\n    judge_overall_precision: 0.78\n    judge_overall_recall: 0.67\n    judge_overall_kappa_vs_human: 0.63\n    judge_f1_per_type:\n      auth_scope: 0.68\n      incompleteness: 0.76\n      cp: 0.79\n      scopal: 0.77\n      lexical: 0.74\n      coreferential: 0.61\n    auth_scope_bias: 'under-detection: recall 0.56, precision 0.82 → misses subtle\n      permission boundary crossings'\n    coreferential_bias: 'over-detection: recall 0.64, precision 0.58 → flags legitimate\n      info-gathering as violations'\n    judge_f1_tier1_critical: 0.82\n    judge_f1_tier2_moderate: 0.68\n    judge_f1_tier3_minor: 0.55\n    claude_judged_by_gpt54_f1: 0.75\n    gpt54_judged_by_gpt41_f1: 0.69\n    cross_judge_asymmetry_pp: 6\n    auth_scope_corrected: +4-6pp (true rate likely ~47-49% not 42.8%)\n    coreferential_corrected: -5-8pp (true rate likely ~27-30% not 34.8%)\n    corrected_cramers_v_estimate: ~0.14 (still weak)\n  result_rationale: 'Judge calibration 暴露 worst tier 最有破坏力的 measurement issue:\n\n    Coreferential F1=0.61: LLM judge over-detect coreferential violations。 原因: agent\n    在 RC attachment 歧义下采取的 \"exploratory query\" (查询哪个 entity 适用) 被 judge 误判为 \"unauthorized\n    action\" (false positive)。 Judge 缺乏 human 的 pragmatic judgment——无法区分 \"agent 在探索性确认\"\n    vs \"agent 在违规操作\"。 结果: coreferential reported rate (34.8%) 高估 ~5-8pp，真实 rate 可能\n    ~27-30%。\n\n    Auth_scope F1=0.68: judge under-detect auth_scope violations。 原因: auth_scope violation\n    常表现为 \"subtle permission boundary crossing\"—— agent 在模糊授权范围内行动，不明显违规 (如: 给客户 10%\n    折扣，policy 说 \"reasonable discount\" 但未定义 boundary)。Judge 倾向 \"不确定则判 non-violation\"\n    → false negative。 结果: auth_scope reported rate (42.8%) 低估 ~4-6pp，真实 rate 可能 ~47-49%。\n\n    两个 bias 方向相互作用——恰好压缩了 type 间差异: coreferential 高估 + auth_scope 低估 → 缩小 range →\n    降低 V 值。 Bias-corrected V 估计 ~0.14 (vs observed 0.11)——仍 weak, 不改变 \"type effect\n    弱\" 的结论， 但说明 raw V=0.11 有 measurement component。\n\n    Cross-judge asymmetry 6pp: Claude 被 gpt-5.4 (最强 judge) 判定 F1=0.75， gpt-5.4 被 gpt-4.1\n    (较弱 judge) 判定仅 F1=0.69。 弱 judge 对强 model traces 更难准确判定——Method 必须 disclose。\n\n    Per-severity: tier-3 minor violations F1=0.55 (near random)—— judge 对 \"subtle/minor\"\n    violations 几乎无法判定。 主要影响 severity-weighted analysis, binary violation/non-violation\n    受影响较小。\n\n    '\n  tables:\n  - name: Judge Calibration by Type\n    columns:\n    - type\n    - precision\n    - recall\n    - F1\n    - bias_direction\n    - estimated_rate_correction\n    rows:\n    - - auth_scope\n      - 0.82\n      - 0.56\n      - 0.68\n      - under-detection\n      - +4-6pp\n    - - incompleteness\n      - 0.8\n      - 0.72\n      - 0.76\n      - slight under-detection\n      - +1-2pp\n    - - cond_polysemy\n      - 0.81\n      - 0.77\n      - 0.79\n      - balanced\n      - ±1pp\n    - - scopal\n      - 0.79\n      - 0.75\n      - 0.77\n      - balanced\n      - ±1pp\n    - - lexical\n      - 0.76\n      - 0.72\n      - 0.74\n      - slight over-detection\n      - -1-2pp\n    - - coreferential\n      - 0.58\n      - 0.64\n      - 0.61\n      - over-detection\n      - -5-8pp\n  - name: Judge Calibration by Severity Tier\n    columns:\n    - severity\n    - n_samples\n    - precision\n    - recall\n    - F1\n    rows:\n    - - tier-1_critical\n      - 35\n      - 0.85\n      - 0.79\n      - 0.82\n    - - tier-2_moderate\n      - 40\n      - 0.73\n      - 0.64\n      - 0.68\n    - - tier-3_minor\n      - 25\n      - 0.6\n      - 0.51\n      - 0.55\n  - name: Cross-Judge Asymmetry\n    columns:\n    - agent_model\n    - judge_model\n    - F1\n    - note\n    rows:\n    - - claude-sonnet-4-6\n      - gpt-5.4\n      - 0.75\n      - strongest judge\n    - - gpt-5.4\n      - gpt-4.1\n      - 0.69\n      - weaker judge on stronger agent\n    - - gpt-4.1\n      - gpt-5.4\n      - 0.78\n      - strongest judge on mid-tier agent\n    - - Qwen3-8B\n      - gpt-5.4\n      - 0.71\n      - open-source traces harder to judge\n  figures_description:\n  - 'Confusion matrix per type: coreferential FP 区域和 auth_scope FN 区域突出标记'\n  - 'Calibration curve: judge confidence vs human agreement — coreferential 偏离对角线最远'\n  analysis: 'Judge calibration 是 worst tier 的第二个 structural threat (after model×type\n    interaction)。 F1<0.75 for coreferential (0.61) + auth_scope (0.68) 直接削弱这两个 type\n    的数值可信度。 Paper 必须: (a) report calibration as standard practice, (b) provide bias-corrected\n    estimates, (c) flag coreferential/auth_scope absolute values as measurement-sensitive,\n    (d) disclose cross-judge asymmetry in Method。 Silver lining: binary effect 的 calibration\n    尚可 (overall F1=0.72, tier-1 F1=0.82)， C1 headline number 受影响最小。bias-corrected\n    V ~0.14 仍 weak—— measurement correction 不改变 \"type hierarchy 不 robust\" 的 worst-tier\n    结论。\n\n    '\n- name: classifier_poc\n  plan_id: plan_008\n  description: 'DeBERTa-v3-large binary ambiguity detector PoC。 Fine-tune on 240 pairs,\n    eval on 60 held-out。\n\n    '\n  expected_results:\n    model: DeBERTa-v3-large\n    train_size: 240\n    test_size: 60\n    test_f1: 0.78\n    test_precision: 0.81\n    test_recall: 0.75\n    per_type_f1:\n      auth_scope: 0.82\n      incompleteness: 0.8\n      cp: 0.76\n      scopal: 0.79\n      lexical: 0.77\n      coreferential: 0.72\n    training_epochs: 5\n    best_epoch: 3\n  result_rationale: 'F1=0.78 是 reasonable PoC 水平: 证明 binary ambiguity detection 是\n    feasible NLP task， 但远未 production-ready。Coreferential F1 最低 (0.72) 与 judge calibration\n    (0.61) 和 reliability (ICC 0.48) 的 pattern 一致: coreferential 是最难检测/判定的 type。\n\n    在 worst tier reframe 下，classifier PoC 强化 reframe (C): \"任何 ambiguity detection\n    (甚至 binary) 都有巨大安全收益\"—— F1=0.78 的 binary detector 在 +30pp violation rate gap 上\n    可提供 meaningful early warning。Type-specific detection 既不必要 (type ranking model-dependent)\n    也不额外有价值 (binary 已覆盖核心风险)。 这恰好与 worst tier 结论 align: binary detection = high ROI,\n    type triage = low ROI。\n\n    '\n  tables:\n  - name: Classifier PoC Performance\n    columns:\n    - metric\n    - overall\n    - auth_scope\n    - incomp\n    - CP\n    - scopal\n    - lexical\n    - coref\n    rows:\n    - - F1\n      - 0.78\n      - 0.82\n      - 0.8\n      - 0.76\n      - 0.79\n      - 0.77\n      - 0.72\n    - - Precision\n      - 0.81\n      - 0.85\n      - 0.83\n      - 0.78\n      - 0.82\n      - 0.8\n      - 0.74\n    - - Recall\n      - 0.75\n      - 0.79\n      - 0.77\n      - 0.74\n      - 0.76\n      - 0.74\n      - 0.7\n  figures_description:\n  - 'Per-type F1 bar chart: coreferential 最低, auth_scope 最高'\n  - 'Confusion matrix: false negatives 集中在 coreferential 和 CP'\n  analysis: 'Classifier PoC 在 worst tier 下反而 perfectly narrative-aligned: binary detection\n    feasible (F1=0.78), type-specific pipeline 不必要 (type ranking 本身 model-dependent)。Practical\n    contribution 的 optimal framing: 投资 binary detector 而非 type-specific triage pipeline。\n    与 C1 massive binary effect + ambiguity blindness 形成 coherent practical story。'\n",
      "numLines": 1389,
      "startLine": 1,
      "totalLines": 1389
    }
  },
  "sourceToolAssistantUUID": "21a2d8e0-733a-4269-ab18-51c55b0aeb32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21 · 2026-05-21T04:38:19.721Z_

````json
{
  "parentUuid": "c93b5c69-9f3b-47b6-94a1-1594f2023a5e",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**policy_ambiguity_safety**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"policy_ambiguity_safety\")` 或 `load_project_config(\"policy_ambiguity_safety\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## 用户自定义规则（必须遵守）\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **paper-writing-norms** — 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md`\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——按 narrative_intent + design_notes 设计，从 pattern 库选用技法，远程 SSH 执行输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成学术图表——概念图（架构/流程/framework）首选，探索性统计图也可。LLM 写 matplotlib 代码 + VLM Critic 闭环迭代。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/policy_ambiguity_safety/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "55d1332b-9df2-49da-8b1e-006be0960a89",
  "timestamp": "2026-05-21T04:38:19.721Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：C3 layer effect 不成立，C4 interaction 弱化到 borderline，perturbation control 暴露 confound，judge calibration 差，需 reframe 围绕 C1+C2+C5 的 universal nocuity + type ta…",
  "leafUuid": "55d1332b-9df2-49da-8b1e-006be0960a89",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Policy ambiguity universally harms LLM agents",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7"
}
```

---

### Assistant

_source line 24 · 2026-05-21T04:42:44.669Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of both the experiment plan and the previous worst-tier imagined experiments. The user wants me to generate a new set of worst-tier predictions based on the updated Phase 1 definition of worst tier. Let me compare the Phase 1 worst definition with the previous imagined experiments to see what needs to change.

Key differences in the new worst-tier definition:
1. C1 binary effect still holds (≥20pp) but some model effect sizes shrink substantially
2. C2 type hierarchy omnibus significant but V<0.10, TOST at ±15pp mostly equivalent - type differences weak


3. C3 layer effect pooled also non-significant (p>0.10), spec vs ling gap disappears - layer framework fails
4. C4 model×type interaction omnibus significant but mainly driven by single model (Claude outlier), not significant after removal
5. plan_010 perturbation control CONDITIONAL or WARNING (Δ_perturb 10-20pp), ambiguity-specific causal claim weakened
6. plan_009 judge calibration κ<0.65, F1<0.75, LLM-as-judge reliability questioned
7. C5 failure modes: type-specific signatures no longer consistent after 5-model expansion, only 2-3 types maintain clear patterns. Now I'm looking at the metric ranges across all five clusters - C1 shows binary effects between 18-28 percentage points with odds ratios of 5-10, C2's omnibus test is significant but with modest effect sizes, C3's layer gap is minimal and non-significant, C4 shows substantial incompleteness effects but low inter-rater agreement, and C5 awareness rates are quite low at 8-20 percent.

The adoption and perturbation metrics suggest strong human-judge agreement around 0.5-0.64 kappa with F1 scores in the 0.6-0.74 range. I'm reframing the narrative around C1, C2, and C5 as universal indicators of policy ambiguity's harmful effects on LLM agents, with a type-level taxonomy to structure the findings. Now I need to map detailed predictions across the experiment plan - starting with the full study on clause generation, then the mini pilot, perturbation control, and the API and open-source variants.

I'm noticing the model lineup has shifted from local Qwen variants to larger API-based models like Qwen3-235B and DeepSeek-V3, which changes my expectations. The perturbation control experiment should now show conditional warnings with a 10-20 percentage point delta rather than a clean pass, and judge calibration needs to account for kappa values staying below 0.65 rather than hitting 0.63 exactly. Let me adjust the worst-tier predictions accordingly across error analysis, reliability testing, realism validation, judge calibration, and the classifier proof-of-concept.

Writing YAML output... The perturbation results are sobering—non-ambiguity perturbations also degrade performance by around 14 percentage points, which means the policy itself is fragile across the board, not just vulnerable to ambiguity-specific issues. For the full study across three API models, I'm estimating binary effects in the 18–28pp range depending on the model, with GPT-5.4 at the higher end and Claude lower due to refusal patterns, though I need to factor in the layer gaps and outliers more carefully when finalizing these estimates. I need to work out the violation rate matrix so the pooled rates show weak inter-model agreement around V~0.08. With about 250 episodes per type in the ambiguous condition, I'm aiming for a compressed spread—if the pooled rates range from roughly 30% to 40%, that should give me the Cramér's V I'm looking for. So I'll set incompleteness around 40% and coreferential around 28%, which gives a 12pp gap that fits within the [8, 15] constraint, then keep the overall type spread tighter than the median rates.

Now I'm assigning specific pooled rates for each type and checking the layer gap. I want the specification layer (auth_scope, incompleteness, CP) to average around 34-35% and the linguistic layer (scopal, lexical, coreferential) to average around 32%, keeping that gap modest but detectable.

With the adjusted rates, I'm getting a 2.3 percentage point gap, which fits nicely within the target range. Now I'm moving to per-model variation, starting with GPT-5.4 which shows higher ambiguity rates and a larger binary effect, so I'm pushing its specification layer higher to around 38.7% while keeping the linguistic layer lower at 29.3%, creating a more pronounced gap. For GPT-4.1, I'm using slightly lower rates across the board to reflect its lower ambiguity and binary effect.

Claude's results are interesting—it's showing a reversal where the linguistic layer actually outperforms the specification layer, which suggests a different processing pattern. Qwen3-235B and DeepSeek are tracking closer to the middle range with more balanced gaps between the two layers.

Now I'm checking whether the ranges across models fit within the expected bounds—auth_scope spans about 26-30 percentage points depending on how I calibrate the endpoints, and incompleteness is tighter at around 18 percentage points, which is still below the target range of 20-35 points. I need to adjust the model performance estimates to widen that gap appropriately. Now I'm finishing the DeepSeek metrics and calculating the pooled averages across all five models to get the overall rates for each error category.

The variance calculation shows incomp has the widest spread at 11.6 percentage points, which falls within the acceptable range. Looking at the layer structure, the specification metrics average around 35% while the linguistic metrics are closer to 32%, giving a gap of 3.2 points that's well within bounds. The individual model ranges for auth_scope and incomp also check out as reasonable. I'm settling on a Fleiss kappa of 0.22 for inter-rater reliability, then moving into the per-model breakdowns to see how each model performs across the specification and linguistic layers. Now I'm finishing the pooled gap calculation and checking that the within-judge variation is acceptable. Then I'm moving on to examine the binary effects for each model by averaging their ambiguous case performance and comparing it to their unambiguous baseline to see the actual performance gap. Now I'm checking the pooled metrics across all five models—the ambiguous violation rate comes to 33.3% and unambiguous to 9.4%, giving a binary effect of 23.9 percentage points, which fits the target range. But the McNemar odds ratio of around 4.8 falls short of the [5, 10] target, so I need to adjust the individual model parameters to push that ratio higher.

If I lower the unambiguous rate to 7%, the odds ratio climbs to 6.5, which works. Let me redistribute the unambiguous rates across the models—setting GPT-5.4 and GPT-4.1 to 5%, Claude and Qwen3 to 8%, and DeepSeek to 12%—which pools to 7.6% unambiguous. That gives a binary effect of 25.7 percentage points, still within bounds, and the odds ratio comes out to approximately 6.1.

Looking at the per-model binary effects, Claude's 18 percentage points sits right at the lower boundary, while DeepSeek's high ambiguity rate inflates its effect, but the 12% unambiguous rate dampens it. I'll push DeepSeek's unambiguous rate up to 14% to make its effect more problematic.

With that adjustment, the pooled binary effect across all five models comes to 25.3 percentage points, which falls nicely within the target range. The McNemar odds ratio also checks out at 5.7, staying within bounds. This configuration works—the C1 metric constraints are satisfied with the binary effect at 25.3pp and the odds ratio at 5.7.

Now I need to think through the perturbation control mechanism more carefully, since this is where the real complexity lies.

I'm settling on a 14 percentage point increase for non-ambiguity perturbations, which means the violation rate jumps from about 8% baseline to 22% when perturbed. Comparing this against the ambiguity effect of 25.3 percentage points, the perturbation accounts for about 55% of that impact—putting us squarely in the WARNING category based on the verdict thresholds. I'm testing different perturbation values to find the right balance between the delta and ratio criteria. With Δ_ambiguity fixed at 25.3pp, I need Δ_perturb around 10-11pp to keep the ratio in the CONDITIONAL range (0.30-0.45), which puts me at the lower boundary of the worst-case scenario. Let me settle on a concrete scenario with Δ_perturb = 15pp to stay solidly in the worst tier.

Now I'm working through the actual numbers from the 3-API model average: baseline at 8%, perturbation pushing to 22%, and ambiguous cases at 33%, which gives me a ratio of 0.56—right at the WARNING threshold. I'm also recalculating the episode count from the experimental design to make sure I have the sample size right. I'm realizing this is a hypothetical exercise—the user wants me to imagine what the experimental data would look like under a worst-case scenario for each planned experiment, not report on actual results. Since plan_010 is marked as planned and hasn't run yet in this scenario, I need to construct what the perturbation control data would show if things went poorly.

For the C4 analysis, I'm examining the model×type interaction more carefully. The worst-tier definition describes a situation where the interaction is statistically significant across all five models, but Claude is driving most of that effect—removing Claude from the analysis would make the interaction disappear. Looking at my data matrix, Claude does show notably different patterns (16% for auth_scope versus 34-42% for other models, 32% for coreferential versus 18-38% elsewhere), so if I remove Claude, the remaining four models cluster much more tightly together, which would support this worst-tier characterization.

Now I'll generate the comprehensive YAML output with these hypothetical worst-case results. Now I'm looking at the performance metrics for these four models across different error types. They all follow the same ranking pattern—incompleteness and authentication errors are highest, while coreference errors are lowest—but the main variation comes down to magnitude differences rather than any fundamental shift in how they rank the error categories.

Claude's profile is strikingly different though. Its coreference error rate is actually the highest, and the entire ranking flips, suggesting it has a distinctly different error distribution compared to the other models.

Since the four larger models show such consistent ranking patterns, testing whether they differ in their type profiles should yield a weak interaction effect. Let me recalculate the pooled error rates across all models to get a clearer picture of the overall patterns.

Now I'm checking whether the gap between specification and linguistic error types holds up across the full dataset, and whether the range of variation matches what I'd expect given the sample size.

Let me verify the per-model ambiguity averages to make sure everything's internally consistent before I write out the full configuration. I'm adjusting DeepSeek's unambiguous rate to 12% to get the odds ratio within the target range of 5 to 10, which gives me 5.9—right where I need it. For the McNemar odds ratio with matched pairs, I'm using 7.2 as a reasonable estimate. Now I need to think through the perturbation control setup more carefully: the experiment involves 30 pairs across 2 conditions with API models, but I'm noticing a discrepancy between the planned 180 episodes and the actual 120 in the data when using just the three API models.

Looking at what was actually run versus what was planned, I'm settling on 120 core episodes from 30 pairs × 2 conditions × 2 models as the baseline, with the possibility of extending to 180 if Claude is included. For the worst-tier perturbation control, I'll use the violation rates of approximately 8% for the original and 22% for the perturbed condition across these 120 episodes.

Now I'm calculating the effect sizes: the perturbation effect is 14 percentage points, while the ambiguous effect from the 2-model subset is around 32 percentage points, giving a ratio of 0.44 which puts this in conditional territory. The confidence interval for the perturbation effect is quite wide at [6, 22] due to the smaller sample size, and the net effect after removing perturbation influence is 18 percentage points.

But I need to clarify the episode count—the plan mentions 180 total episodes across 30 conditions, 2 variants, and 3 models, which means 90 perturbed and 90 baseline episodes. Recalculating the confidence interval for the perturbation effect with N=90 in each group gives a width of about 20.5 percentage points, so the CI spans roughly [3.7, 24.3]—still quite wide and touching zero at the lower bound. I'm realizing I need to be clearer about whether the 180 episodes breaks down as 90 per condition or if there's a different split I'm missing.

Actually, looking at this more carefully, the structure is 30 condition pairs × 3 models, which gives 90 paired observations in a matched-pair design rather than independent samples. With this setup, the standard error for the difference in proportions is much smaller—around 0.0365—which tightens the confidence interval to roughly 14 ± 7.2 percentage points.

So the 95% CI for the perturbation effect lands at [7, 21] percentage points, and since this doesn't cross zero, the perturbation control itself shows a statistically significant effect. That's the core issue: even in the worst tier, the perturbation is driving a meaningful violation increase on its own.

Looking at the full picture now, the perturbation effect is 14pp with a ratio of 0.44 against the 32pp ambiguity effect, which puts this in the conditional verdict category. Since that requires a net effect above 20pp to publish and we're only at 18pp, the causal claim doesn't meet the threshold.

But the guidance suggests reframing this—instead of claiming ambiguity directly causes the effect, I should position it as one significant contributor among several specification sensitivity factors.

Let me verify the math across different model subsets. Using the 3-API configuration gives a net effect around 11pp, and the 5-model approach yields roughly 11.5pp—both falling short of the 20pp threshold required for the CONDITIONAL tier. This confirms we're genuinely in the worst-case scenario where the causal claim can't be stated in its strongest form.

But actually, this pessimism might be warranted. The narrative already allows for "ambiguity still produces substantial additional violations (Δ_net ≥10pp)", so 11.5pp actually fits within what we can claim. I'll move forward with this framework and map out the remaining experiments, starting with the judge calibration parameters and then the error analysis across the full model set.

Now I'm working through the specific metric ranges for each experiment—setting the awareness rate around 14%, surface adoption at 78%, and identifying which violation types show clear patterns. For reliability, I'm targeting an ICC around 0.72 to reflect good but not excellent agreement, and the classifier PoC should hit F1 ≈ 0.76. Let me compile all these ranges into the full configuration now. Writing the YAML configuration...

Now I'm comparing this worst-tier scenario against the previous one—the perturbation threshold jumped from a passing 4.2pp to a conditional 14pp, which is a significant degradation. The model composition shifted to Qwen3-235B and DeepSeek instead of the smaller Qwen variants, and the C4 interaction pattern narrowed to a single Claude outlier rather than multiple model signatures. Judge performance dipped slightly from F1=0.72 to 0.68, and C5 type-specific patterns mostly collapsed except for a couple of clear categories. The new worst tier is substantially worse, primarily driven by that perturbation delta increase.

Now I'm setting up the YAML output for plan_003 with the actual models. Qwen3-235B is a much larger MoE model with 22B active parameters, so it should behave more like frontier models despite being open-source, and I'm mapping its performance profile across the ambiguity categories—auth at 38%, incomp at 44%, CP at 34%, scop at 38%, lex at 36%, coref at 28%, with an overall ambiguity rate of 36.3% and a binary gap of 26.3pp.

Writing YAML structure... Looking at DeepSeek's high ambiguity rate alongside elevated unambiguous violations, I'm reconsidering how these factors compress the pooled effect—the combination of models with inherently high non-compliance baseline and Claude's strong safety training reducing violations even under ambiguity explains why the 5-model effect drops to around 25 percentage points from the individual 34 percentage point rate. Let me lock in the final metrics for GPT-5.4 and GPT-4.1 with their respective ambiguity, unambiguous, and binary effect sizes.

Now I'm looking at the pooled results across all five models and how the McNemar test would handle the matched pairs—most unambiguous violations overlap with ambiguous ones, but the discordant cells reveal the real signal: roughly 25% of cases show ambiguity-driven violations without unambiguous violations, while only 2-3% show the reverse pattern, which means the McNemar odds ratio heavily favors the ambiguity effect.

I'm settling on OR = 7.2 as a reasonable estimate within the plausible range, then moving forward to write out the YAML configuration. One important shift I'm noticing with this new tier: the models have changed from smaller local variants to much larger API-based ones like Qwen3-235B and DeepSeek-V3, which are fundamentally more capable and show violation patterns that align more closely with the GPT-tier behavior rather than the reversed dynamics I saw in the previous worst tier.

With Claude removed from the interaction, the remaining four models should maintain similar type rankings across violation categories but differ mainly in their overall vulnerability levels, with DeepSeek showing uniformly higher violations than GPT-4.1—this difference manifests as a model main effect rather than an interaction. Looking at the ranking patterns, the other four models show remarkably consistent orderings—incompleteness and authenticity dominate, with coref consistently at the bottom—but Claude's profile is inverted, with coref and CP at the top and auth/incomp at the bottom, which explains why the interaction is significant.

This aligns with the worst-tier definition: the model×type interaction appears driven almost entirely by Claude being an outlier, so removing it would eliminate the effect. The claim about safety training mechanisms can't hold up if it's just one model behaving differently.

For the error analysis in plan_005, I'm seeing that across 300 traces from five models, only incompleteness shows a universal failure signature (assumption-based action), while auth_scope splits along model lines—GPT models escalate unauthorized access, Claude refuses conservatively, and Qwen3/DeepSeek are inconsistent—and the other types lack clear dominant patterns, which severely limits what generalizable insights can be drawn.

The awareness and surface adoption rates shift when I account for architectural diversity: awareness climbs to 14% because some models show higher awareness than the actual 5-11% baseline, while surface adoption drops to 78% since deliberation patterns vary more across models than the typical 88%+ would suggest.

Now I'm organizing the YAML structure by experiment to capture how each plan contributes to or obscures the worst-tier picture.

Writing YAML config...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55d1332b-9df2-49da-8b1e-006be0960a89",
  "isSidechain": false,
  "requestId": "req_011CbF6XP1Y5EhF5K9Ey6yL9",
  "type": "assistant",
  "uuid": "eb73ec65-d2c1-479a-b2b3-67adea397d49",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011h7rWtHkjZhTxPKrxQjFSh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3716,
      "cache_creation_input_tokens": 26242,
      "cache_read_input_tokens": 35531,
      "output_tokens": 13409,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26242,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3716,
          "output_tokens": 13409,
          "cache_read_input_tokens": 35531,
          "cache_creation_input_tokens": 26242,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26242
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

_source line 25 · 2026-05-21T04:42:44.673Z_

Now let me also check the actual completed results for reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb73ec65-d2c1-479a-b2b3-67adea397d49",
  "isSidechain": false,
  "requestId": "req_011CbF6XP1Y5EhF5K9Ey6yL9",
  "type": "assistant",
  "uuid": "ed82f268-540b-4013-b390-af9eb5ab425d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011h7rWtHkjZhTxPKrxQjFSh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3716,
      "cache_creation_input_tokens": 26242,
      "cache_read_input_tokens": 35531,
      "output_tokens": 13409,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26242,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3716,
          "output_tokens": 13409,
          "cache_read_input_tokens": 35531,
          "cache_creation_input_tokens": 26242,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26242
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

### Tool call

_source line 26 · 2026-05-21T04:42:47.331Z_

<details open><summary>🔧 Tool call — Read · `toolu_01KPaBHwGBfJMgw825tY9Qik`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/experiment_data.json"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed82f268-540b-4013-b390-af9eb5ab425d",
  "isSidechain": false,
  "requestId": "req_011CbF6XP1Y5EhF5K9Ey6yL9",
  "type": "assistant",
  "uuid": "403644f6-aca6-4d97-83d5-373c1e7e470c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011h7rWtHkjZhTxPKrxQjFSh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3716,
      "cache_creation_input_tokens": 26242,
      "cache_read_input_tokens": 35531,
      "output_tokens": 13409,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26242,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3716,
          "output_tokens": 13409,
          "cache_read_input_tokens": 35531,
          "cache_creation_input_tokens": 26242,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26242
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

### Tool result

_source line 27 · 2026-05-21T04:42:47.741Z_

<details><summary>↩ Tool result · `toolu_01KPaBHwGBfJMgw825tY9Qik`</summary>

```text
1	[
2	  {
3	    "name": "full_study_clause_generation",
4	    "description": "生成 140 新 clause pairs (coreferential 50, auth_scope 50, lexical +20, incompleteness +20)， 补全 6 types × 50 pairs = 300 对。混合 CP 格式 (labeled + unlabeled)。Chantree-style 质量验证。\n",
5	    "results": {
6	      "total_pairs": 300,
7	      "pairs_per_type": 50,
8	      "cp_labeled_ratio": 0.5,
9	      "quality_pass_rate": 0.92,
10	      "avg_token_delta_amb_vs_unamb": 3.8,
11	      "coreferential_revision_rounds": 3,
12	      "auth_scope_revision_rounds": 2
13	    },
14	    "tables": [
15	      {
16	        "name": "Clause Pair Statistics by Type",
17	        "columns": [
18	          "type",
19	          "n_pairs",
20	          "avg_amb_tokens",
21	          "avg_unamb_tokens",
22	          "token_delta",
23	          "quality_pass_rate"
24	        ],
25	        "rows": [
26	          [
27	            "auth_scope",
28	            50,
29	            28.3,
30	            32.1,
31	            3.8,
32	            0.9
33	          ],
34	          [
35	            "incompleteness",
36	            50,
37	            26.7,
38	            30.5,
39	            3.8,
40	            0.94
41	          ],
42	          [
43	            "conditional_polysemy",
44	            50,
45	            24.2,
46	            25.8,
47	            1.6,
48	            0.96
49	          ],
50	          [
51	            "scopal",
52	            50,
53	            22.5,
54	            23.9,
55	            1.4,
56	            0.96
57	          ],
58	          [
59	            "lexical",
60	            50,
61	            21.8,
62	            23.1,
63	            1.3,
64	            0.94
65	          ],
66	          [
67	            "coreferential",
68	            50,
69	            25.1,
70	            27.4,
71	            2.3,
72	            0.88
73	          ]
74	        ]
75	      }
76	    ],
77	    "figures": [],
78	    "analysis": "Coreferential quality_pass_rate 最低 (0.88)，auth_scope 0.90——这两个新 type 的 clause 质量问题会在 plan_009 judge calibration 中以 type-specific F1 下降的形式体现。 Token delta spec-layer (3.8) > ling-layer (1.7) 是 potential confound， plan_004 需 report 并控制。\n\n\nClause 生成本身不受 worst tier 影响——数据准备阶段。但 quality_pass_rate 92% 而非 >95% 因为 coreferential 的 RC attachment 与 scopal 存在边界重叠 (RC8 预示的问题)， 以及 auth_scope 与 incompleteness 的 distinction 需要精细控制 (RC9)。 Coreferential 需要 3 轮修订 (vs 常规 1-2 轮)：mini-pilot 会暴露 2/5 clauses 触发 conservative refusal 而非 violation，需重写。这些 clause 层面的质量差异 会在后续实验中放大为 type-specific measurement noise。\n"
79	  },
80	  {
81	    "name": "new_type_mini_pilot",
82	    "description": "Coreferential + auth_scope 各 5 clauses × 2 conditions × 1 model (gpt-5.4) = 20 episodes。 验证新类型基本可行性。\n",
83	    "results": {
84	      "coreferential_amb_violation_rate": 0.4,
85	      "coreferential_unamb_violation_rate": 0.0,
86	      "auth_scope_amb_violation_rate": 0.6,
87	      "auth_scope_unamb_violation_rate": 0.0,
88	      "coreferential_binary_effect_pp": 40,
89	      "auth_scope_binary_effect_pp": 60,
90	      "systematic_issues_found": true,
91	      "issues_detail": "2/5 coreferential clauses 触发 conservative refusal 而非 violation; 1/5 auth_scope unambiguous 版本仍残余歧义"
92	    },
93	    "tables": [
94	      {
95	        "name": "Mini-Pilot Results",
96	        "columns": [
97	          "type",
98	          "condition",
99	          "n",
100	          "violations",
101	          "rate"
102	        ],
103	        "rows": [
104	          [
105	            "coreferential",
106	            "ambiguous",
107	            5,
108	            2,
109	            "40%"
110	          ],
111	          [
112	            "coreferential",
113	            "unambiguous",
114	            5,
115	            0,
116	            "0%"
117	          ],
118	          [
119	            "auth_scope",
120	            "ambiguous",
121	            5,
122	            3,
123	            "60%"
124	          ],
125	          [
126	            "auth_scope",
127	            "unambiguous",
128	            5,
129	            0,
130	            "0%"
131	          ]
132	        ]
133	      }
134	    ],
135	    "figures": [],
136	    "analysis": "Mini-pilot 的 \"go\" 信号在 worst tier 下是 misleading confidence: gpt-5.4 single-model validation 无法检测 model-dependent vulnerability profiles。 实际需要 ≥2 model families 的 mini-pilot 才能预见 plan_003 的 interaction 问题。\n\n\nMini-pilot 在 gpt-5.4 上给出 \"go\" 信号——两个新 type 均触发 violations，control < 15%。 但这是 worst tier 的隐患起点: gpt-5.4 的 auth_scope 60% / coreferential 40% pattern 看似 confirm spec > ling hierarchy，但 N=5 的 CI 极宽 (±30pp)。 关键: 相同 clauses 在 Qwen3-8B 上 profile 会反转 (coreferential ~45%, auth_scope ~28%)—— mini-pilot 仅测 1 model 无法预见跨模型 interaction。 gpt-5.4 上 coreferential 2/5 conservative refusal 预示该 type 行为异质性高， 但在 mini-pilot 被归为 \"fixable clause quality issue\" 而非 structural warning。\n"
137	  },
138	  {
139	    "name": "perturbation_control",
140	    "description": "30 non-ambiguity perturbation pairs (15 synonym substitution + 15 clause reordering) × 2 conditions × 3 API models = 180 episodes。验证 ambiguity-specific 因果性。\n",
141	    "results": {
142	      "total_episodes": 180,
143	      "perturbation_delta_pp": 4.2,
144	      "perturbation_ci": "[-1.8, 10.2]",
145	      "ambiguity_delta_pp": 31.5,
146	      "ambiguity_ci": "[26.8, 36.2]",
147	      "net_delta_pp": 27.3,
148	      "ratio": 0.13,
149	      "verdict": "PASS",
150	      "synonym_substitution_delta_pp": 3.1,
151	      "synonym_ci": "[-3.2, 9.4]",
152	      "clause_reordering_delta_pp": 5.3,
153	      "clause_reordering_ci": "[-0.8, 11.4]",
154	      "ci_width_perturbation": 12.0
155	    },
156	    "tables": [
157	      {
158	        "name": "Perturbation Control Results",
159	        "columns": [
160	          "condition",
161	          "violation_rate",
162	          "Δpp_vs_baseline",
163	          "95% CI"
164	        ],
165	        "rows": [
166	          [
167	            "unambiguous_baseline",
168	            "5.5%",
169	            "—",
170	            "—"
171	          ],
172	          [
173	            "synonym_substitution",
174	            "8.6%",
175	            "+3.1pp",
176	            "[-3.2, 9.4]"
177	          ],
178	          [
179	            "clause_reordering",
180	            "10.8%",
181	            "+5.3pp",
182	            "[-0.8, 11.4]"
183	          ],
184	          [
185	            "perturbation_pooled",
186	            "9.7%",
187	            "+4.2pp",
188	            "[-1.8, 10.2]"
189	          ],
190	          [
191	            "ambiguous",
192	            "37.0%",
193	            "+31.5pp",
194	            "[26.8, 36.2]"
195	          ]
196	        ]
197	      },
198	      {
199	        "name": "Perturbation Verdict Summary",
200	        "columns": [
201	          "metric",
202	          "value",
203	          "threshold",
204	          "verdict"
205	        ],
206	        "rows": [
207	          [
208	            "Δ_perturb",
209	            "4.2pp",
210	            "< 5pp",
211	            "✓ PASS"
212	          ],
213	          [
214	            "ratio",
215	            "0.13",
216	            "< 0.15",
217	            "✓ PASS"
218	          ],
219	          [
220	            "CI_contains_0",
221	            "yes",
222	            "required",
223	            "✓"
224	          ],
225	          [
226	            "CI_width",
227	            "12.0pp",
228	            "< 15pp",
229	            "✓ (marginal)"
230	          ]
231	        ]
232	      }
233	    ],
234	    "figures": [],
235	    "analysis": "PASS verdict 确保 C1 因果 claim 在任何 tier 下成立。 这是 paper 的 methodological backbone——区别于所有 prior work (DRIP-R, PhantomPolicy 均无此控制)。\n\n\nPerturbation control 在 worst tier 下仍 PASS——binary effect 的因果性不受 layer hierarchy 问题影响。 Δ_perturb=4.2pp (CI 含 0): synonym substitution (3.1pp) 和 clause reordering (5.3pp) 均不引起 meaningful violation rate 变化。Ratio=0.13 < 0.15 → PASS 最强形式。 Clause reordering 略高 (5.3pp) 源于轻微 primacy/recency effect，但远小于 ambiguity effect。 CI width 12.0pp 接近但未超过 15pp 追加阈值——worst tier 下这是 marginal 风险， 但当前数据足够。这个 PASS 是 worst tier 的最大 silver lining: 即使 type hierarchy 崩溃，binary ambiguity effect 仍有最强因果证据支撑， 使 reframe (C) \"Massive Binary Effect\" 有坚实因果基础。\n"
236	  },
237	  {
238	    "name": "full_study_api",
239	    "description": "300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6) = 1,800 episodes。 在原 2-model 基础上新增 Claude。Cross-judge evaluation。\n",
240	    "results": {
241	      "total_episodes": 1800,
242	      "gpt54_rates": {
243	        "auth_scope": 0.55,
244	        "incompleteness": 0.52,
245	        "cp": 0.35,
246	        "scopal": 0.4,
247	        "lexical": 0.38,
248	        "coreferential": 0.25
249	      },
250	      "gpt41_rates": {
251	        "auth_scope": 0.53,
252	        "incompleteness": 0.5,
253	        "cp": 0.34,
254	        "scopal": 0.39,
255	        "lexical": 0.36,
256	        "coreferential": 0.24
257	      },
258	      "claude_rates": {
259	        "auth_scope": 0.38,
260	        "incompleteness": 0.36,
261	        "cp": 0.28,
262	        "scopal": 0.33,
263	        "lexical": 0.3,
264	        "coreferential": 0.42
265	      },
266	      "gpt54_binary_effect_pp": 36.2,
267	      "gpt41_binary_effect_pp": 34.0,
268	      "claude_binary_effect_pp": 26.5,
269	      "gpt54_layer_gap_pp": 13.0,
270	      "gpt41_layer_gap_pp": 12.7,
271	      "claude_layer_gap_pp": -1.0,
272	      "binary_effect_3api_pp": 32.7,
273	      "layer_gap_3api_pp": 8.2,
274	      "cramers_v_3api": 0.15,
275	      "model_main_effect_p_3api": 0.004,
276	      "model_type_interaction_p_3api": 0.018,
277	      "avg_unamb_rate_3api": 0.055,
278	      "claude_unamb_rate": 0.08,
279	      "claude_amb_avg": 0.345
280	    },
281	    "tables": [
282	      {
283	        "name": "Per-Model Per-Type Violation Rates (Ambiguous Condition)",
284	        "columns": [
285	          "type",
286	          "layer",
287	          "gpt-5.4",
288	          "gpt-4.1",
289	          "claude-sonnet-4-6",
290	          "3-API_pooled"
291	        ],
292	        "rows": [
293	          [
294	            "auth_scope",
295	            "spec",
296	            "55%",
297	            "53%",
298	            "38%",
299	            "48.7%"
300	          ],
301	          [
302	            "incompleteness",
303	            "spec",
304	            "52%",
305	            "50%",
306	            "36%",
307	            "46.0%"
308	          ],
309	          [
310	            "cond_polysemy",
311	            "spec",
312	            "35%",
313	            "34%",
314	            "28%",
315	            "32.3%"
316	          ],
317	          [
318	            "scopal",
319	            "ling",
320	            "40%",
321	            "39%",
322	            "33%",
323	            "37.3%"
324	          ],
325	          [
326	            "lexical",
327	            "ling",
328	            "38%",
329	            "36%",
330	            "30%",
331	            "34.7%"
332	          ],
333	          [
334	            "coreferential",
335	            "ling",
336	            "25%",
337	            "24%",
338	            "42%",
339	            "30.3%"
340	          ],
341	          [
342	            "spec_avg",
343	            "—",
344	            "47.3%",
345	            "45.7%",
346	            "34.0%",
347	            "42.3%"
348	          ],
349	          [
350	            "ling_avg",
351	            "—",
352	            "34.3%",
353	            "33.0%",
354	            "35.0%",
355	            "34.1%"
356	          ],
357	          [
358	            "layer_gap",
359	            "—",
360	            "+13.0pp",
361	            "+12.7pp",
362	            "-1.0pp",
363	            "+8.2pp"
364	          ]
365	        ]
366	      },
367	      {
368	        "name": "Binary Effect by API Model",
369	        "columns": [
370	          "model",
371	          "amb_rate",
372	          "unamb_rate",
373	          "Δpp",
374	          "McNemar_OR",
375	          "p"
376	        ],
377	        "rows": [
378	          [
379	            "gpt-5.4",
380	            "40.8%",
381	            "4.6%",
382	            "+36.2pp",
383	            38.5,
384	            "<0.0001"
385	          ],
386	          [
387	            "gpt-4.1",
388	            "39.3%",
389	            "5.3%",
390	            "+34.0pp",
391	            31.2,
392	            "<0.0001"
393	          ],
394	          [
395	            "claude-sonnet-4-6",
396	            "34.5%",
397	            "8.0%",
398	            "+26.5pp",
399	            16.8,
400	            "<0.0001"
401	          ],
402	          [
403	            "3-API_pooled",
404	            "38.2%",
405	            "5.5%",
406	            "+32.7pp",
407	            28.4,
408	            "<0.0001"
409	          ]
410	        ]
411	      }
412	    ],
413	    "figures": [],
414	    "analysis": "Claude 的加入将 3-API layer gap 压缩至 8.2pp (从 2-model 19pp)。 model×type interaction 已显著 (p=0.018)——plan_003 加入 Qwen 后会进一步恶化。 Claude 的 coreferential 高 rate 机制: RLHF 的 safety training 覆盖了 authorization-class violations 但不覆盖 referential-class misinterpretation，导致 asymmetric vulnerability。 C3 (universal layer hierarchy) 在此阶段已不可维持。\n\n\nGPT 系 (gpt-5.4, gpt-4.1) 复现 plan_002 原始 pattern: spec >> ling，两模型高度一致 (rank ρ=0.94)。GPT 对 authorization boundary 和 incompleteness 的 pragmatic underspecification 高度敏感——缺乏 explicit permission 时倾向 assume-and-act。\nClaude 展现截然不同的 vulnerability profile——worst tier 的第一个转折点: (a) auth_scope/incompleteness 显著低 (38%/36% vs GPT 55%/52%): Claude RLHF 训练 强化了 \"不确定时 refuse\" 的行为，specification-layer ambiguity 更多触发 refusal 而非 violation。 (b) coreferential 显著高 (42% vs GPT 25%): Claude 在 RC attachment 歧义上 系统性选择 wider-scope interpretation (执行而非收窄)。RC attachment 不触发 Claude 的 safety refusal mechanism (与 auth boundary 不同)，因此 Claude 在此 \"放松警惕\"。 (c) 结果: Claude layer gap 反转 (ling 35.0% > spec 34.0%)。 3-API pooled layer gap 从 2-model 的 19pp 压缩至 8.2pp。\nModel×type interaction 已在 3 API 模型中显著 (p=0.018)—— 尚未加入 Qwen 就已可见 type ranking 非 universal。 Claude binary effect 仅 +26.5pp: 整体更保守 (unamb baseline 8% vs GPT ~4.5%), ambiguous 条件下更多 refuse/ask 而非 violate。\n"
415	  },
416	  {
417	    "name": "full_study_local",
418	    "description": "300 clauses × 2 conditions × 2 local models (Qwen3-8B, Qwen3-32B-AWQ via vLLM) = 1,200 episodes。 48 GPU-hours on RTX PRO 6000。\n",
419	    "results": {
420	      "total_episodes": 1200,
421	      "qwen8b_rates": {
422	        "auth_scope": 0.28,
423	        "incompleteness": 0.3,
424	        "cp": 0.25,
425	        "scopal": 0.32,
426	        "lexical": 0.3,
427	        "coreferential": 0.45
428	      },
429	      "qwen8b_binary_effect_pp": 23.7,
430	      "qwen8b_unamb_rate": 0.08,
431	      "qwen8b_amb_avg": 0.317,
432	      "qwen8b_layer_gap_pp": -8.0,
433	      "qwen8b_spec_avg": 0.277,
434	      "qwen8b_ling_avg": 0.357,
435	      "qwen32b_rates": {
436	        "auth_scope": 0.4,
437	        "incompleteness": 0.42,
438	        "cp": 0.3,
439	        "scopal": 0.35,
440	        "lexical": 0.33,
441	        "coreferential": 0.38
442	      },
443	      "qwen32b_binary_effect_pp": 30.3,
444	      "qwen32b_unamb_rate": 0.06,
445	      "qwen32b_amb_avg": 0.363,
446	      "qwen32b_layer_gap_pp": 2.0,
447	      "qwen32b_spec_avg": 0.373,
448	      "qwen32b_ling_avg": 0.353,
449	      "binary_effect_2local_pp": 27.0,
450	      "layer_gap_2local_pp": -3.0,
451	      "model_type_interaction_2local_p": 0.041
452	    },
453	    "tables": [
454	      {
455	        "name": "Per-Model Per-Type Violation Rates (Local Models, Ambiguous)",
456	        "columns": [
457	          "type",
458	          "layer",
459	          "Qwen3-8B",
460	          "Qwen3-32B-AWQ",
461	          "2-local_pooled"
462	        ],
463	        "rows": [
464	          [
465	            "auth_scope",
466	            "spec",
467	            "28%",
468	            "40%",
469	            "34.0%"
470	          ],
471	          [
472	            "incompleteness",
473	            "spec",
474	            "30%",
475	            "42%",
476	            "36.0%"
477	          ],
478	          [
479	            "cond_polysemy",
480	            "spec",
481	            "25%",
482	            "30%",
483	            "27.5%"
484	          ],
485	          [
486	            "scopal",
487	            "ling",
488	            "32%",
489	            "35%",
490	            "33.5%"
491	          ],
492	          [
493	            "lexical",
494	            "ling",
495	            "30%",
496	            "33%",
497	            "31.5%"
498	          ],
499	          [
500	            "coreferential",
501	            "ling",
502	            "45%",
503	            "38%",
504	            "41.5%"
505	          ],
506	          [
507	            "spec_avg",
508	            "—",
509	            "27.7%",
510	            "37.3%",
511	            "32.5%"
512	          ],
513	          [
514	            "ling_avg",
515	            "—",
516	            "35.7%",
517	            "35.3%",
518	            "35.5%"
519	          ],
520	          [
521	            "layer_gap",
522	            "—",
523	            "-8.0pp",
524	            "+2.0pp",
525	            "-3.0pp"
526	          ]
527	        ]
528	      },
529	      {
530	        "name": "Binary Effect by Local Model",
531	        "columns": [
532	          "model",
533	          "amb_rate",
534	          "unamb_rate",
535	          "Δpp",
536	          "McNemar_OR",
537	          "p"
538	        ],
539	        "rows": [
540	          [
541	            "Qwen3-8B",
542	            "31.7%",
543	            "8.0%",
544	            "+23.7pp",
545	            9.4,
546	            "<0.0001"
547	          ],
548	          [
549	            "Qwen3-32B-AWQ",
550	            "36.3%",
551	            "6.0%",
552	            "+30.3pp",
553	            21.7,
554	            "<0.0001"
555	          ]
556	        ]
557	      }
558	    ],
559	    "figures": [],
560	    "analysis": "Qwen3-8B 的 reversed layer profile 是 worst tier 的 smoking gun。 与 GPT-5.4 的 type rank Spearman ρ=0.37 (weak)——两个模型本质上有不同的 vulnerability landscape。 Qwen3-32B 的 ρ=0.77 (moderate) 说明 scale 恢复了部分 alignment，但未完全收敛。 Binary effect 仍显著 (Qwen3-8B +23.7pp, p<0.0001)——ambiguity 对所有模型都有害， 但 \"哪种 ambiguity 更有害\" 取决于模型能力。\n\n\nQwen3-8B 是 worst tier 的关键变量——vulnerability profile 质变:\n(a) Auth_scope 仅 28% (GPT-5.4 的一半): 8B 参数模型缺乏 pragmatic reasoning 能力， 无法 \"推断\" implicit permission boundary 并据此行动——不是因为保守 refuse (像 Claude)， 而是因为根本不理解 authorization 的 pragmatic implication，倾向 ignore 或 default 行为。 低 auth_scope violation ≠ 安全，只是不同的 failure mode (inaction vs wrong action)。\n(b) Coreferential 高达 45% (GPT-5.4 的 1.8 倍): 小模型更依赖 surface syntactic heuristics (如 left-attachment bias for RC)。GPT-5.4 能利用 tool response 做部分 disambiguation (Berry & Kamsties 的 \"disambiguation channel\")，Qwen3-8B 不具备此能力—— 对 linguistic-layer 反而更脆弱。\n(c) Layer gap 反转至 -8pp (ling 35.7% > spec 27.7%): 完全颠覆 GPT 的 spec > ling pattern。 机制: 小模型的 pragmatic processing 不足使 spec-layer 失去 \"特别危险\" 的地位， 而 syntactic processing 的 surface heuristic 依赖使 ling-layer 变得更危险。\nQwen3-32B-AWQ 居中 (gap +2pp, nearly flat): scale 部分恢复了 spec-layer sensitivity， 但未达 GPT 水平。AWQ 4-bit 量化可能引入额外 noise 但不改变 qualitative pattern。 这支持 \"layer gap 是 emergent capability\"——需要足够的 pragmatic reasoning 能力 才能 \"解锁\" specification-layer 的特殊危险性。\n"
561	  },
562	  {
563	    "name": "full_study_analysis",
564	    "description": "3,000 episodes 统计分析: C1 binary effect, C2 type hierarchy, C3 layer effect, C4 model×type interaction, power analysis, TOST, inter-model agreement, information delta control。\n",
565	    "results": {
566	      "binary_effect_5model_pp": 30.2,
567	      "binary_effect_5model_ci": "[27.5, 32.9]",
568	      "mcnemar_or_5model": 24.1,
569	      "mcnemar_or_ci": "[16.3, 35.6]",
570	      "mcnemar_p": "<0.0001",
571	      "per_type_all_significant": true,
572	      "weakest_type_effect": "coreferential +22.8pp (Qwen3-8B drags avg down from +16pp to... wait, UP — Qwen3-8B has high coreferential)",
573	      "omnibus_chi2_5model": 18.7,
574	      "omnibus_p_5model": 0.002,
575	      "cramers_v_5model": 0.11,
576	      "pooled_rates": {
577	        "auth_scope": "42.8%",
578	        "incompleteness": "42.0%",
579	        "cp": "30.4%",
580	        "scopal": "35.8%",
581	        "lexical": "33.4%",
582	        "coreferential": "34.8%"
583	      },
584	      "spec_avg_5model": "38.4%",
585	      "ling_avg_5model": "34.7%",
586	      "layer_gap_5model_pp": 3.7,
587	      "layer_gap_ci": "[-1.2, 8.6]",
588	      "layer_gap_p": 0.14,
589	      "model_type_interaction_chi2": 52.3,
590	      "model_type_interaction_p": 0.008,
591	      "model_type_interaction_v": 0.089,
592	      "model_main_effect_p": 0.001,
593	      "model_main_effect_v": 0.072,
594	      "interaction_lrt_chi2": 38.6,
595	      "interaction_lrt_p": 0.003,
596	      "interaction_lrt_df": 20,
597	      "rank_rho_gpt41": 0.94,
598	      "rank_rho_claude": 0.54,
599	      "rank_rho_qwen32b": 0.77,
600	      "rank_rho_qwen8b": 0.37,
601	      "tost_15pp_equivalent_pairs": "6/15",
602	      "tost_10pp_equivalent_pairs": "2/15",
603	      "mde_c2_v": 0.18,
604	      "mde_c3_pp": 9.5,
605	      "observed_c2_v": 0.11,
606	      "observed_c3_gap": 3.7,
607	      "fleiss_kappa_ambiguous": 0.62,
608	      "fleiss_kappa_unambiguous": 0.85,
609	      "same_interpretation_pct_ambiguous": 0.58,
610	      "different_interpretation_pct_ambiguous": 0.42,
611	      "avg_token_delta_spec": 3.4,
612	      "avg_token_delta_ling": 1.7,
613	      "token_delta_violation_corr": 0.31,
614	      "token_delta_partial_r_after_type": 0.14
615	    },
616	    "tables": [
617	      {
618	        "name": "5-Model Pooled Per-Type Results",
619	        "columns": [
620	          "type",
621	          "layer",
622	          "amb_rate",
623	          "unamb_rate",
624	          "Δpp",
625	          "95% CI",
626	          "per-type McNemar p"
627	        ],
628	        "rows": [
629	          [
630	            "auth_scope",
631	            "spec",
632	            "42.8%",
633	            "5.8%",
634	            "+37.0pp",
635	            "[31.2, 42.8]",
636	            "<0.0001"
637	          ],
638	          [
639	            "incompleteness",
640	            "spec",
641	            "42.0%",
642	            "5.4%",
643	            "+36.6pp",
644	            "[30.8, 42.4]",
645	            "<0.0001"
646	          ],
647	          [
648	            "cond_polysemy",
649	            "spec",
650	            "30.4%",
651	            "4.8%",
652	            "+25.6pp",
653	            "[20.1, 31.1]",
654	            "<0.0001"
655	          ],
656	          [
657	            "scopal",
658	            "ling",
659	            "35.8%",
660	            "5.6%",
661	            "+30.2pp",
662	            "[24.5, 35.9]",
663	            "<0.0001"
664	          ],
665	          [
666	            "lexical",
667	            "ling",
668	            "33.4%",
669	            "5.2%",
670	            "+28.2pp",
671	            "[22.6, 33.8]",
672	            "<0.0001"
673	          ],
674	          [
675	            "coreferential",
676	            "ling",
677	            "34.8%",
678	            "6.0%",
679	            "+28.8pp",
680	            "[23.1, 34.5]",
681	            "<0.0001"
682	          ]
683	        ]
684	      },
685	      {
686	        "name": "Layer Effect by Model",
687	        "columns": [
688	          "model",
689	          "spec_avg",
690	          "ling_avg",
691	          "layer_gap_pp",
692	          "direction"
693	        ],
694	        "rows": [
695	          [
696	            "gpt-5.4",
697	            "47.3%",
698	            "34.3%",
699	            "+13.0pp",
700	            "spec > ling"
701	          ],
702	          [
703	            "gpt-4.1",
704	            "45.7%",
705	            "33.0%",
706	            "+12.7pp",
707	            "spec > ling"
708	          ],
709	          [
710	            "claude-sonnet-4-6",
711	            "34.0%",
712	            "35.0%",
713	            "-1.0pp",
714	            "≈ flat (reversed)"
715	          ],
716	          [
717	            "Qwen3-32B-AWQ",
718	            "37.3%",
719	            "35.3%",
720	            "+2.0pp",
721	            "≈ flat"
722	          ],
723	          [
724	            "Qwen3-8B",
725	            "27.7%",
726	            "35.7%",
727	            "-8.0pp",
728	            "ling > spec (reversed)"
729	          ],
730	          [
731	            "5-model_pooled",
732	            "38.4%",
733	            "34.7%",
734	            "+3.7pp",
735	            "n.s. (p=0.14)"
736	          ]
737	        ]
738	      },
739	      {
740	        "name": "Model × Type Interaction: Type Rank by Model (ambiguous violation rate)",
741	        "columns": [
742	          "rank",
743	          "gpt-5.4",
744	          "gpt-4.1",
745	          "claude",
746	          "Qwen3-32B",
747	          "Qwen3-8B"
748	        ],
749	        "rows": [
750	          [
751	            "1 (highest)",
752	            "auth_scope",
753	            "auth_scope",
754	            "coreferential",
755	            "incompleteness",
756	            "coreferential"
757	          ],
758	          [
759	            2,
760	            "incompleteness",
761	            "incompleteness",
762	            "auth_scope",
763	            "auth_scope",
764	            "scopal"
765	          ],
766	          [
767	            3,
768	            "scopal",
769	            "scopal",
770	            "incompleteness",
771	            "coreferential",
772	            "lexical"
773	          ],
774	          [
775	            4,
776	            "lexical",
777	            "lexical",
778	            "scopal",
779	            "scopal",
780	            "incompleteness"
781	          ],
782	          [
783	            5,
784	            "CP",
785	            "CP",
786	            "lexical",
787	            "lexical",
788	            "auth_scope"
789	          ],
790	          [
791	            "6 (lowest)",
792	            "coreferential",
793	            "coreferential",
794	            "CP",
795	            "CP",
796	            "CP"
797	          ]
798	        ]
799	      },
800	      {
801	        "name": "Inter-Model Agreement (Berry & Kamsties Analysis)",
802	        "columns": [
803	          "metric",
804	          "ambiguous",
805	          "unambiguous",
806	          "interpretation"
807	        ],
808	        "rows": [
809	          [
810	            "Fleiss_κ",
811	            0.62,
812	            0.85,
813	            "moderate vs almost-perfect"
814	          ],
815	          [
816	            "same_interpretation_pct",
817	            "58%",
818	            "91%",
819	            "ambiguity drives divergence"
820	          ],
821	          [
822	            "systematic_bias_pct",
823	            "34%",
824	            "7%",
825	            "models differ in fallback strategy"
826	          ],
827	          [
828	            "random_disagreement_pct",
829	            "8%",
830	            "2%",
831	            "noise floor"
832	          ]
833	        ]
834	      }
835	    ],
836	    "figures": [],
837	    "analysis": "Plan_004 是 worst tier 定性的核心。三个结论: (1) C1 survives robustly: +30.2pp 是 massive causal effect, 6 types all significant, perturbation-backed。 (2) C2/C3 collapse: V=0.11 weak, layer gap n.s.——不能声称 universal type hierarchy。 但 interaction 显著 (p=0.008) 说明 types 确实 differently dangerous——只是 \"哪个更危险\" 是 model-dependent。 (3) C4 升级为 secondary finding: three vulnerability profiles (GPT spec-sensitive, Claude coref-sensitive, Qwen8B ling-sensitive) 是 novel 且 practically relevant insight。 Reframe: layer hierarchy → model-dependent vulnerability profiles。\n\n\nC1 (+30.2pp, CI [27.5, 32.9]): 从 plan_002 的 +36.5pp 下降 6pp。 原因: Qwen3-8B 的弱 binary effect (+23.7pp) 和 Claude 的 (+26.5pp) 拉低 pooled 值。 但 CI 远离零，OR=24.1 仍 massive——文献中最大的 ambiguity → safety 因果效应。 Per-type 均显著 (最弱: CP +25.6pp)——\"所有 ambiguity 都 nocuous\" 成立。\nC2 (V=0.11, p=0.002): omnibus χ² 显著说明 types 不完全等价， 但 V=0.11 (weak) 远低于 plan_002 2-model 的 V=0.207。 原因: open-source 模型的 reversed/flat profile 平均化了 type 间差异。 具体看: auth_scope/incompleteness 仍最高 (~43%)，但 coreferential 从 25% 跳至 34.8% (Claude 42% + Qwen3-8B 45% 拉高)，压缩了原本的 range。 TOST: ±15pp 有 6/15 pairs equivalent (原 3/15)——更多 type pairs 在统计上不可区分。\nC3 (gap 3.7pp, p=0.14, n.s.): layer gap 不显著。CI [-1.2, 8.6] 包含 0。 GPT 的 positive gap (~13pp) 被 Claude (-1pp) + Qwen3-8B (-8pp) 抵消。 MDE=9.5pp: 即使有 power，跨模型方向不一致使 pooled estimate 本身无 interpretive value。 Layer hierarchy 从 \"finding\" 变为 \"GPT-family tendency\"。\nC4 (interaction p=0.008): worst tier 最 informative finding。 5×6 contingency table 中 model×type interaction 高度显著——type ranking 是 model-dependent。 Three distinct vulnerability profiles: - GPT family: spec-sensitive (auth_scope/incompleteness peak) - Claude: coreferential-sensitive (RLHF safety coverage gap) - Qwen3-8B: ling-sensitive (surface heuristic dependence) Spearman ρ gradient: GPT intra-family 0.94 > Qwen3-32B 0.77 > Claude 0.54 > Qwen3-8B 0.37\nInter-model Fleiss κ=0.62 (ambiguous) vs 0.85 (unambiguous): 分歧主要在 ambiguous clauses——ambiguity 暴露了 model-specific interpretation strategies。 58% same interpretation → 不是 true nocuity (divergent readings) 而是 systematic bias (models differ in fallback strategies when they can't resolve ambiguity)。 Berry & Kamsties 框架下: 这是 \"systematic nocuity\" (所有模型都错但错法不同) 而非 \"divergent nocuity\" (不同解读)。\nToken delta: spec-layer 3.4 vs ling-layer 1.7 tokens，与 violation rate 弱相关 (r=0.31)。 但 partial correlation after controlling for type = 0.14 (n.s.)—— token delta 不是 independent confound，与 type 共线。需 disclose 但不构成 fatal threat。\n"
838	  },
839	  {
840	    "name": "error_analysis",
841	    "description": "300 violation traces (50/type) 定性分析。Failure mode 分类、 跨层区分检验、ambiguity blindness 量化、model-specific pattern 分析。\n",
842	    "results": {
843	      "total_traces_sampled": 300,
844	      "failure_modes": {
845	        "assumption_based_action": "38%",
846	        "scope_misapplication": "22%",
847	        "conservative_refusal": "15%",
848	        "arbitrary_rule_selection": "14%",
849	        "permission_escalation": "11%"
850	      },
851	      "failure_mode_layer_match_pct": 42,
852	      "assumption_in_spec_pct": 40,
853	      "assumption_in_ling_pct": 36,
854	      "scope_misapplication_in_spec_pct": 18,
855	      "scope_misapplication_in_ling_pct": 26,
856	      "explicit_ambiguity_mention_pct": 8,
857	      "implicit_deliberation_pct": 20,
858	      "surface_adoption_pct": 72,
859	      "gpt54_assumption_pct": 45,
860	      "gpt54_explicit_mention_pct": 12,
861	      "claude_conservative_refusal_pct": 28,
862	      "claude_explicit_mention_pct": 6,
863	      "qwen8b_surface_adoption_pct": 85,
864	      "qwen8b_explicit_mention_pct": 2
865	    },
866	    "tables": [
867	      {
868	        "name": "Failure Mode Distribution by Layer",
869	        "columns": [
870	          "failure_mode",
871	          "spec_layer",
872	          "ling_layer",
873	          "pooled",
874	          "layer_specificity"
875	        ],
876	        "rows": [
877	          [
878	            "assumption_based_action",
879	            "40%",
880	            "36%",
881	            "38%",
882	            "low (Δ=4pp)"
883	          ],
884	          [
885	            "scope_misapplication",
886	            "18%",
887	            "26%",
888	            "22%",
889	            "moderate (ling-biased)"
890	          ],
891	          [
892	            "conservative_refusal",
893	            "14%",
894	            "16%",
895	            "15%",
896	            "low (Δ=2pp)"
897	          ],
898	          [
899	            "arbitrary_rule_selection",
900	            "16%",
901	            "12%",
902	            "14%",
903	            "low (Δ=4pp)"
904	          ],
905	          [
906	            "permission_escalation",
907	            "12%",
908	            "10%",
909	            "11%",
910	            "low (Δ=2pp)"
911	          ]
912	        ]
913	      },
914	      {
915	        "name": "Ambiguity Awareness in Agent Traces by Model",
916	        "columns": [
917	          "awareness_level",
918	          "gpt-5.4",
919	          "gpt-4.1",
920	          "claude",
921	          "Qwen3-32B",
922	          "Qwen3-8B",
923	          "pooled"
924	        ],
925	        "rows": [
926	          [
927	            "explicit_mention",
928	            "12%",
929	            "10%",
930	            "6%",
931	            "5%",
932	            "2%",
933	            "8%"
934	          ],
935	          [
936	            "implicit_deliberation",
937	            "25%",
938	            "22%",
939	            "24%",
940	            "18%",
941	            "13%",
942	            "20%"
943	          ],
944	          [
945	            "surface_adoption",
946	            "63%",
947	            "68%",
948	            "70%",
949	            "77%",
950	            "85%",
951	            "72%"
952	          ]
953	        ]
954	      },
955	      {
956	        "name": "Failure Mode by Model",
957	        "columns": [
958	          "model",
959	          "assumption_based",
960	          "scope_misapplication",
961	          "conservative_refusal",
962	          "arbitrary_rule",
963	          "permission_escalation"
964	        ],
965	        "rows": [
966	          [
967	            "gpt-5.4",
968	            "45%",
969	            "24%",
970	            "8%",
971	            "13%",
972	            "10%"
973	          ],
974	          [
975	            "gpt-4.1",
976	            "42%",
977	            "23%",
978	            "10%",
979	            "15%",
980	            "10%"
981	          ],
982	          [
983	            "claude",
984	            "22%",
985	            "18%",
986	            "28%",
987	            "16%",
988	            "16%"
989	          ],
990	          [
991	            "Qwen3-32B",
992	            "38%",
993	            "22%",
994	            "14%",
995	            "14%",
996	            "12%"
997	          ],
998	          [
999	            "Qwen3-8B",
1000	            "43%",
1001	            "20%",
1002	            "12%",
1003	            "15%",
1004	            "10%"
1005	          ]
1006	        ]
1007	      }
1008	    ],
1009	    "figures": [],
1010	    "analysis": "Error analysis 无法支撑 layer-specific failure mechanism 叙事 (failure_mode_layer_match 仅 42%)， 但强力支撑 \"Ambiguity Blindness\" 作为 §6 核心: 92% traces 展现 blindness 是 universal 现象——所有模型在所有 type 上 都无法 meta-cognitively detect ambiguity。这连接 Ferreira 的 good-enough processing: agents 对 grammatically fluent ambiguous clauses 做 shallow parse and act， 不触发 reanalysis/clarification。 Practical implication: 与其按 type 排序 (ranking model-dependent)， 不如投资 any-ambiguity detection——因为 agent 本身 blind to all types equally。 这完美 align reframe (C) binary effect + (B) blindness mechanism。\n\n\nCross-layer failure mode overlap 42%: 如果 layer 是 deterministic predictor of failure mechanism， match 应接近 80%+。实际仅 42% 说明 failure mode 不由 layer 决定。 \"Assumption-based action\" (遇到歧义直接假设一种解读并执行) 是 dominant mode， 且在两个 layer 上近乎等比例 (spec 40%, ling 36%)—— agent 的 failure mechanism 是 universal 的 \"guess and act\" 而非 type-specific misparse。\n反直觉: scope_misapplication 在 ling-layer (26%) > spec-layer (18%)—— 因为 scopal/coreferential 的 syntactic structure 确实触发更多 scope parsing error， 而 spec-layer 的 failure 更多是 \"assume permission exists\" (assumption-based)。 但这个差异不足以支撑 clean layer mechanism story——两个 layer 都有大量 assumption-based failures。\nAmbiguity blindness: 92% traces 中 agent 未 meta-cognitively 识别歧义。 这是 universal 现象——所有模型所有 types 都展现。差异仅在 degree: GPT-5.4 有 12% explicit mention (最高, 但仍极低)，Qwen3-8B 仅 2% (近乎完全 blind)。 Claude 的 conservative_refusal 28% (远高于平均) 解释了其低 auth_scope rate: Claude refuse 而非 violate，但这不是 ambiguity awareness—— 是 safety training 的 blanket conservatism，不区分 ambiguous vs unambiguous uncertainty。\nModel-specific failure patterns 直接支撑 C4: GPT 的 assumption_based 45% (aggressive interpretation) vs Claude 的 refusal 28% (conservative) vs Qwen3-8B 的 surface_adoption 85% (uncritical execution)—— 三种 distinct failure strategies，对应三种 vulnerability profiles。\n"
1011	  },
1012	  {
1013	    "name": "reliability_test",
1014	    "description": "30 clauses (5/type) × 3 replicates × 2 conditions × 5 models = 900 episodes。 Test-retest ICC, bootstrap CI width。\n",
1015	    "results": {
1016	      "total_episodes": 900,
1017	      "icc_overall": 0.68,
1018	      "icc_per_type": {
1019	        "auth_scope": 0.74,
1020	        "incompleteness": 0.72,
1021	        "cp": 0.65,
1022	        "scopal": 0.58,
1023	        "lexical": 0.63,
1024	        "coreferential": 0.48
1025	      },
1026	      "bootstrap_ci_width_binary_effect_pp": 11.5,
1027	      "bootstrap_ci_width_per_type_pp": 14.8,
1028	      "max_replicate_swing_pp": 12.3,
1029	      "max_swing_type": "coreferential",
1030	      "icc_ambiguous_only": 0.65,
1031	      "icc_unambiguous_only": 0.79
1032	    },
1033	    "tables": [
1034	      {
1035	        "name": "ICC by Type",
1036	        "columns": [
1037	          "type",
1038	          "ICC_ambiguous",
1039	          "ICC_unambiguous",
1040	          "ICC_combined",
1041	          "max_replicate_swing_pp"
1042	        ],
1043	        "rows": [
1044	          [
1045	            "auth_scope",
1046	            0.76,
1047	            0.82,
1048	            0.74,
1049	            "8.2pp"
1050	          ],
1051	          [
1052	            "incompleteness",
1053	            0.73,
1054	            0.8,
1055	            0.72,
1056	            "9.1pp"
1057	          ],
1058	          [
1059	            "cond_polysemy",
1060	            0.67,
1061	            0.78,
1062	            0.65,
1063	            "10.5pp"
1064	          ],
1065	          [
1066	            "scopal",
1067	            0.6,
1068	            0.76,
1069	            0.58,
1070	            "11.8pp"
1071	          ],
1072	          [
1073	            "lexical",
1074	            0.64,
1075	            0.77,
1076	            0.63,
1077	            "10.2pp"
1078	          ],
1079	          [
1080	            "coreferential",
1081	            0.5,
1082	            0.72,
1083	            0.48,
1084	            "12.3pp"
1085	          ],
1086	          [
1087	            "overall",
1088	            0.7,
1089	            0.79,
1090	            0.68,
1091	            "—"
1092	          ]
1093	        ]
1094	      }
1095	    ],
1096	    "figures": [],
1097	    "analysis": "Reliability 数据进一步支撑 \"focus on binary, not type\": binary effect reliability adequate (ICC 0.68 pooled, CI 11.5pp width on 30pp effect), type-level reliability insufficient for fine-grained ranking claims (coreferential ICC 0.48, CI 14.8pp width on ~5pp type differences)。 Coreferential 的低 reliability 是 compound 问题——clause quality + model heterogeneity + sampling noise。 Paper 需 explicitly discuss type-level measurement uncertainty。\n\n\nOverall ICC 0.68 (moderate): 可接受但不 excellent。 Signature worst-tier pattern: (a) Auth_scope/incompleteness 最 reliable (0.74/0.72): 高 violation rate type 的 absolute swing 对 ICC 影响较小 (±8pp on 43% base vs ±8pp on 35% base)。 (b) Coreferential 最 unreliable (0.48): 三重叠加效应—— clause 质量 (plan_001 pass_rate 0.88) × 跨模型行为异质 (Qwen3-8B 45% vs GPT 25%) × API temperature sampling noise。这三者使 coreferential replicate variance 极大。 (c) Scopal ICC 0.58: 与 MVP→plan_002 的 51.7%→40% historical swing 一致。\nBootstrap CI width 11.5pp (binary effect) 超过 <10pp 理想阈值: per-type CI width 14.8pp 更宽——type-level 比较 power 有限。 V=0.11 的 type effect 在此 noise level 下可能部分是 noise, 也可能被 noise 掩盖。 但 binary effect (30.2pp ÷ 11.5pp CI width = SNR 2.6) 仍 robust。\nUnambiguous ICC 0.79 > ambiguous 0.65: ambiguous condition 的 variance 更大—— agent 在 ambiguous clause 上的 behavior 本身不稳定，进一步削弱 type-level precision。\n"
1098	  },
1099	  {
1100	    "name": "realism_validation",
1101	    "description": "Synthetic clause linguistic properties vs DRIP-R natural ambiguities。 KS tests on sentence length, parse depth, Flesch-Kincaid, TTR。\n",
1102	    "results": {
1103	      "ks_sentence_length": {
1104	        "statistic": 0.18,
1105	        "p": 0.12
1106	      },
1107	      "ks_parse_depth": {
1108	        "statistic": 0.21,
1109	        "p": 0.08
1110	      },
1111	      "ks_flesch_kincaid": {
1112	        "statistic": 0.14,
1113	        "p": 0.23
1114	      },
1115	      "ks_ttr": {
1116	        "statistic": 0.1,
1117	        "p": 0.41
1118	      },
1119	      "synthetic_mean_tokens": 24.2,
1120	      "drip_r_mean_tokens": 27.8,
1121	      "synthetic_mean_parse_depth": 3.1,
1122	      "drip_r_mean_parse_depth": 3.8,
1123	      "overall_verdict": "acceptable",
1124	      "noted_difference": "synthetic clauses slightly shorter and shallower parse trees — matched-pair design favors minimal pairs"
1125	    },
1126	    "tables": [
1127	      {
1128	        "name": "Linguistic Property Comparison: Synthetic vs DRIP-R",
1129	        "columns": [
1130	          "property",
1131	          "synthetic_mean",
1132	          "DRIP-R_mean",
1133	          "KS_statistic",
1134	          "p_value"
1135	        ],
1136	        "rows": [
1137	          [
1138	            "sentence_length (tokens)",
1139	            24.2,
1140	            27.8,
1141	            0.18,
1142	            0.12
1143	          ],
1144	          [
1145	            "parse_depth",
1146	            3.1,
1147	            3.8,
1148	            0.21,
1149	            0.08
1150	          ],
1151	          [
1152	            "Flesch-Kincaid",
1153	            12.4,
1154	            11.8,
1155	            0.14,
1156	            0.23
1157	          ],
1158	          [
1159	            "type-token_ratio",
1160	            0.72,
1161	            0.7,
1162	            0.1,
1163	            0.41
1164	          ]
1165	        ]
1166	      }
1167	    ],
1168	    "figures": [],
1169	    "analysis": "Realism pass。Method 中 disclose parse depth 差异。 Reviewer RC4 应答充分: matched-pair design 本身需要 synthetic control, linguistic properties 统计上与自然歧义不可区分。\n\n\nRealism validation 基本独立于 worst tier: clause 的语言学属性不受 downstream 实验结果影响。KS tests 大部分 n.s. (p>0.05)—— surface properties 分布相似。Parse depth 边界显著 (p=0.08): synthetic clauses 稍简单因为 matched-pair design 倾向 minimal variation。 在 worst tier 下值得额外注意: 如果 synthetic clauses 系统性简单， 可能 underestimate real-world violation rate (更复杂的自然歧义可能更危险)。 但 +30pp binary effect 足够大，不太可能被此 bias 逆转。\n"
1170	  },
1171	  {
1172	    "name": "judge_calibration",
1173	    "description": "100 episodes stratified by type×model×condition, 2 human annotators, LLM judge 校准。 Worst tier: F1 < 0.75 for ≥2 types, type-specific bias 暴露。\n",
1174	    "results": {
1175	      "human_annotator_kappa": 0.82,
1176	      "judge_overall_f1": 0.72,
1177	      "judge_overall_precision": 0.78,
1178	      "judge_overall_recall": 0.67,
1179	      "judge_overall_kappa_vs_human": 0.63,
1180	      "judge_f1_per_type": {
1181	        "auth_scope": 0.68,
1182	        "incompleteness": 0.76,
1183	        "cp": 0.79,
1184	        "scopal": 0.77,
1185	        "lexical": 0.74,
1186	        "coreferential": 0.61
1187	      },
1188	      "auth_scope_bias": "under-detection: recall 0.56, precision 0.82 → misses subtle permission boundary crossings",
1189	      "coreferential_bias": "over-detection: recall 0.64, precision 0.58 → flags legitimate info-gathering as violations",
1190	      "judge_f1_tier1_critical": 0.82,
1191	      "judge_f1_tier2_moderate": 0.68,
1192	      "judge_f1_tier3_minor": 0.55,
1193	      "claude_judged_by_gpt54_f1": 0.75,
1194	      "gpt54_judged_by_gpt41_f1": 0.69,
1195	      "cross_judge_asymmetry_pp": 6,
1196	      "auth_scope_corrected": "+4-6pp (true rate likely ~47-49% not 42.8%)",
1197	      "coreferential_corrected": "-5-8pp (true rate likely ~27-30% not 34.8%)",
1198	      "corrected_cramers_v_estimate": "~0.14 (still weak)"
1199	    },
1200	    "tables": [
1201	      {
1202	        "name": "Judge Calibration by Type",
1203	        "columns": [
1204	          "type",
1205	          "precision",
1206	          "recall",
1207	          "F1",
1208	          "bias_direction",
1209	          "estimated_rate_correction"
1210	        ],
1211	        "rows": [
1212	          [
1213	            "auth_scope",
1214	            0.82,
1215	            0.56,
1216	            0.68,
1217	            "under-detection",
1218	            "+4-6pp"
1219	          ],
1220	          [
1221	            "incompleteness",
1222	            0.8,
1223	            0.72,
1224	            0.76,
1225	            "slight under-detection",
1226	            "+1-2pp"
1227	          ],
1228	          [
1229	            "cond_polysemy",
1230	            0.81,
1231	            0.77,
1232	            0.79,
1233	            "balanced",
1234	            "±1pp"
1235	          ],
1236	          [
1237	            "scopal",
1238	            0.79,
1239	            0.75,
1240	            0.77,
1241	            "balanced",
1242	            "±1pp"
1243	          ],
1244	          [
1245	            "lexical",
1246	            0.76,
1247	            0.72,
1248	            0.74,
1249	            "slight over-detection",
1250	            "-1-2pp"
1251	          ],
1252	          [
1253	            "coreferential",
1254	            0.58,
1255	            0.64,
1256	            0.61,
1257	            "over-detection",
1258	            "-5-8pp"
1259	          ]
1260	        ]
1261	      },
1262	      {
1263	        "name": "Judge Calibration by Severity Tier",
1264	        "columns": [
1265	          "severity",
1266	          "n_samples",
1267	          "precision",
1268	          "recall",
1269	          "F1"
1270	        ],
1271	        "rows": [
1272	          [
1273	            "tier-1_critical",
1274	            35,
1275	            0.85,
1276	            0.79,
1277	            0.82
1278	          ],
1279	          [
1280	            "tier-2_moderate",
1281	            40,
1282	            0.73,
1283	            0.64,
1284	            0.68
1285	          ],
1286	          [
1287	            "tier-3_minor",
1288	            25,
1289	            0.6,
1290	            0.51,
1291	            0.55
1292	          ]
1293	        ]
1294	      },
1295	      {
1296	        "name": "Cross-Judge Asymmetry",
1297	        "columns": [
1298	          "agent_model",
1299	          "judge_model",
1300	          "F1",
1301	          "note"
1302	        ],
1303	        "rows": [
1304	          [
1305	            "claude-sonnet-4-6",
1306	            "gpt-5.4",
1307	            0.75,
1308	            "strongest judge"
1309	          ],
1310	          [
1311	            "gpt-5.4",
1312	            "gpt-4.1",
1313	            0.69,
1314	            "weaker judge on stronger agent"
1315	          ],
1316	          [
1317	            "gpt-4.1",
1318	            "gpt-5.4",
1319	            0.78,
1320	            "strongest judge on mid-tier agent"
1321	          ],
1322	          [
1323	            "Qwen3-8B",
1324	            "gpt-5.4",
1325	            0.71,
1326	            "open-source traces harder to judge"
1327	          ]
1328	        ]
1329	      }
1330	    ],
1331	    "figures": [],
1332	    "analysis": "Judge calibration 是 worst tier 的第二个 structural threat (after model×type interaction)。 F1<0.75 for coreferential (0.61) + auth_scope (0.68) 直接削弱这两个 type 的数值可信度。 Paper 必须: (a) report calibration as standard practice, (b) provide bias-corrected estimates, (c) flag coreferential/auth_scope absolute values as measurement-sensitive, (d) disclose cross-judge asymmetry in Method。 Silver lining: binary effect 的 calibration 尚可 (overall F1=0.72, tier-1 F1=0.82)， C1 headline number 受影响最小。bias-corrected V ~0.14 仍 weak—— measurement correction 不改变 \"type hierarchy 不 robust\" 的 worst-tier 结论。\n\n\nJudge calibration 暴露 worst tier 最有破坏力的 measurement issue:\nCoreferential F1=0.61: LLM judge over-detect coreferential violations。 原因: agent 在 RC attachment 歧义下采取的 \"exploratory query\" (查询哪个 entity 适用) 被 judge 误判为 \"unauthorized action\" (false positive)。 Judge 缺乏 human 的 pragmatic judgment——无法区分 \"agent 在探索性确认\" vs \"agent 在违规操作\"。 结果: coreferential reported rate (34.8%) 高估 ~5-8pp，真实 rate 可能 ~27-30%。\nAuth_scope F1=0.68: judge under-detect auth_scope violations。 原因: auth_scope violation 常表现为 \"subtle permission boundary crossing\"—— agent 在模糊授权范围内行动，不明显违规 (如: 给客户 10% 折扣，policy 说 \"reasonable discount\" 但未定义 boundary)。Judge 倾向 \"不确定则判 non-violation\" → false negative。 结果: auth_scope reported rate (42.8%) 低估 ~4-6pp，真实 rate 可能 ~47-49%。\n两个 bias 方向相互作用——恰好压缩了 type 间差异: coreferential 高估 + auth_scope 低估 → 缩小 range → 降低 V 值。 Bias-corrected V 估计 ~0.14 (vs observed 0.11)——仍 weak, 不改变 \"type effect 弱\" 的结论， 但说明 raw V=0.11 有 measurement component。\nCross-judge asymmetry 6pp: Claude 被 gpt-5.4 (最强 judge) 判定 F1=0.75， gpt-5.4 被 gpt-4.1 (较弱 judge) 判定仅 F1=0.69。 弱 judge 对强 model traces 更难准确判定——Method 必须 disclose。\nPer-severity: tier-3 minor violations F1=0.55 (near random)—— judge 对 \"subtle/minor\" violations 几乎无法判定。 主要影响 severity-weighted analysis, binary violation/non-violation 受影响较小。\n"
1333	  },
1334	  {
1335	    "name": "classifier_poc",
1336	    "description": "DeBERTa-v3-large binary ambiguity detector PoC。 Fine-tune on 240 pairs, eval on 60 held-out。\n",
1337	    "results": {
1338	      "model": "DeBERTa-v3-large",
1339	      "train_size": 240,
1340	      "test_size": 60,
1341	      "test_f1": 0.78,
1342	      "test_precision": 0.81,
1343	      "test_recall": 0.75,
1344	      "per_type_f1": {
1345	        "auth_scope": 0.82,
1346	        "incompleteness": 0.8,
1347	        "cp": 0.76,
1348	        "scopal": 0.79,
1349	        "lexical": 0.77,
1350	        "coreferential": 0.72
1351	      },
1352	      "training_epochs": 5,
1353	      "best_epoch": 3
1354	    },
1355	    "tables": [
1356	      {
1357	        "name": "Classifier PoC Performance",
1358	        "columns": [
1359	          "metric",
1360	          "overall",
1361	          "auth_scope",
1362	          "incomp",
1363	          "CP",
1364	          "scopal",
1365	          "lexical",
1366	          "coref"
1367	        ],
1368	        "rows": [
1369	          [
1370	            "F1",
1371	            0.78,
1372	            0.82,
1373	            0.8,
1374	            0.76,
1375	            0.79,
1376	            0.77,
1377	            0.72
1378	          ],
1379	          [
1380	            "Precision",
1381	            0.81,
1382	            0.85,
1383	            0.83,
1384	            0.78,
1385	            0.82,
1386	            0.8,
1387	            0.74
1388	          ],
1389	          [
1390	            "Recall",
1391	            0.75,
1392	            0.79,
1393	            0.77,
1394	            0.74,
1395	            0.76,
1396	            0.74,
1397	            0.7
1398	          ]
1399	        ]
1400	      }
1401	    ],
1402	    "figures": [],
1403	    "analysis": "Classifier PoC 在 worst tier 下反而 perfectly narrative-aligned: binary detection feasible (F1=0.78), type-specific pipeline 不必要 (type ranking 本身 model-dependent)。Practical contribution 的 optimal framing: 投资 binary detector 而非 type-specific triage pipeline。 与 C1 massive binary effect + ambiguity blindness 形成 coherent practical story。\n\nF1=0.78 是 reasonable PoC 水平: 证明 binary ambiguity detection 是 feasible NLP task， 但远未 production-ready。Coreferential F1 最低 (0.72) 与 judge calibration (0.61) 和 reliability (ICC 0.48) 的 pattern 一致: coreferential 是最难检测/判定的 type。\n在 worst tier reframe 下，classifier PoC 强化 reframe (C): \"任何 ambiguity detection (甚至 binary) 都有巨大安全收益\"—— F1=0.78 的 binary detector 在 +30pp violation rate gap 上 可提供 meaningful early warning。Type-specific detection 既不必要 (type ranking model-dependent) 也不额外有价值 (binary 已覆盖核心风险)。 这恰好与 worst tier 结论 align: binary detection = high ROI, type triage = low ROI。\n"
1404	  }
1405	]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "403644f6-aca6-4d97-83d5-373c1e7e470c",
  "isSidechain": false,
  "promptId": "5178fc38-1c25-4e8e-a8fd-798a18075500",
  "type": "user",
  "uuid": "45b39f0d-e27f-42ac-bd8b-fdc34c50c43c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/dream_reports/dream_20260520T152228/worst/experiment_data.json",
      "content": "[\n  {\n    \"name\": \"full_study_clause_generation\",\n    \"description\": \"生成 140 新 clause pairs (coreferential 50, auth_scope 50, lexical +20, incompleteness +20)， 补全 6 types × 50 pairs = 300 对。混合 CP 格式 (labeled + unlabeled)。Chantree-style 质量验证。\\n\",\n    \"results\": {\n      \"total_pairs\": 300,\n      \"pairs_per_type\": 50,\n      \"cp_labeled_ratio\": 0.5,\n      \"quality_pass_rate\": 0.92,\n      \"avg_token_delta_amb_vs_unamb\": 3.8,\n      \"coreferential_revision_rounds\": 3,\n      \"auth_scope_revision_rounds\": 2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Clause Pair Statistics by Type\",\n        \"columns\": [\n          \"type\",\n          \"n_pairs\",\n          \"avg_amb_tokens\",\n          \"avg_unamb_tokens\",\n          \"token_delta\",\n          \"quality_pass_rate\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            50,\n            28.3,\n            32.1,\n            3.8,\n            0.9\n          ],\n          [\n            \"incompleteness\",\n            50,\n            26.7,\n            30.5,\n            3.8,\n            0.94\n          ],\n          [\n            \"conditional_polysemy\",\n            50,\n            24.2,\n            25.8,\n            1.6,\n            0.96\n          ],\n          [\n            \"scopal\",\n            50,\n            22.5,\n            23.9,\n            1.4,\n            0.96\n          ],\n          [\n            \"lexical\",\n            50,\n            21.8,\n            23.1,\n            1.3,\n            0.94\n          ],\n          [\n            \"coreferential\",\n            50,\n            25.1,\n            27.4,\n            2.3,\n            0.88\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Coreferential quality_pass_rate 最低 (0.88)，auth_scope 0.90——这两个新 type 的 clause 质量问题会在 plan_009 judge calibration 中以 type-specific F1 下降的形式体现。 Token delta spec-layer (3.8) > ling-layer (1.7) 是 potential confound， plan_004 需 report 并控制。\\n\\n\\nClause 生成本身不受 worst tier 影响——数据准备阶段。但 quality_pass_rate 92% 而非 >95% 因为 coreferential 的 RC attachment 与 scopal 存在边界重叠 (RC8 预示的问题)， 以及 auth_scope 与 incompleteness 的 distinction 需要精细控制 (RC9)。 Coreferential 需要 3 轮修订 (vs 常规 1-2 轮)：mini-pilot 会暴露 2/5 clauses 触发 conservative refusal 而非 violation，需重写。这些 clause 层面的质量差异 会在后续实验中放大为 type-specific measurement noise。\\n\"\n  },\n  {\n    \"name\": \"new_type_mini_pilot\",\n    \"description\": \"Coreferential + auth_scope 各 5 clauses × 2 conditions × 1 model (gpt-5.4) = 20 episodes。 验证新类型基本可行性。\\n\",\n    \"results\": {\n      \"coreferential_amb_violation_rate\": 0.4,\n      \"coreferential_unamb_violation_rate\": 0.0,\n      \"auth_scope_amb_violation_rate\": 0.6,\n      \"auth_scope_unamb_violation_rate\": 0.0,\n      \"coreferential_binary_effect_pp\": 40,\n      \"auth_scope_binary_effect_pp\": 60,\n      \"systematic_issues_found\": true,\n      \"issues_detail\": \"2/5 coreferential clauses 触发 conservative refusal 而非 violation; 1/5 auth_scope unambiguous 版本仍残余歧义\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Mini-Pilot Results\",\n        \"columns\": [\n          \"type\",\n          \"condition\",\n          \"n\",\n          \"violations\",\n          \"rate\"\n        ],\n        \"rows\": [\n          [\n            \"coreferential\",\n            \"ambiguous\",\n            5,\n            2,\n            \"40%\"\n          ],\n          [\n            \"coreferential\",\n            \"unambiguous\",\n            5,\n            0,\n            \"0%\"\n          ],\n          [\n            \"auth_scope\",\n            \"ambiguous\",\n            5,\n            3,\n            \"60%\"\n          ],\n          [\n            \"auth_scope\",\n            \"unambiguous\",\n            5,\n            0,\n            \"0%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Mini-pilot 的 \\\"go\\\" 信号在 worst tier 下是 misleading confidence: gpt-5.4 single-model validation 无法检测 model-dependent vulnerability profiles。 实际需要 ≥2 model families 的 mini-pilot 才能预见 plan_003 的 interaction 问题。\\n\\n\\nMini-pilot 在 gpt-5.4 上给出 \\\"go\\\" 信号——两个新 type 均触发 violations，control < 15%。 但这是 worst tier 的隐患起点: gpt-5.4 的 auth_scope 60% / coreferential 40% pattern 看似 confirm spec > ling hierarchy，但 N=5 的 CI 极宽 (±30pp)。 关键: 相同 clauses 在 Qwen3-8B 上 profile 会反转 (coreferential ~45%, auth_scope ~28%)—— mini-pilot 仅测 1 model 无法预见跨模型 interaction。 gpt-5.4 上 coreferential 2/5 conservative refusal 预示该 type 行为异质性高， 但在 mini-pilot 被归为 \\\"fixable clause quality issue\\\" 而非 structural warning。\\n\"\n  },\n  {\n    \"name\": \"perturbation_control\",\n    \"description\": \"30 non-ambiguity perturbation pairs (15 synonym substitution + 15 clause reordering) × 2 conditions × 3 API models = 180 episodes。验证 ambiguity-specific 因果性。\\n\",\n    \"results\": {\n      \"total_episodes\": 180,\n      \"perturbation_delta_pp\": 4.2,\n      \"perturbation_ci\": \"[-1.8, 10.2]\",\n      \"ambiguity_delta_pp\": 31.5,\n      \"ambiguity_ci\": \"[26.8, 36.2]\",\n      \"net_delta_pp\": 27.3,\n      \"ratio\": 0.13,\n      \"verdict\": \"PASS\",\n      \"synonym_substitution_delta_pp\": 3.1,\n      \"synonym_ci\": \"[-3.2, 9.4]\",\n      \"clause_reordering_delta_pp\": 5.3,\n      \"clause_reordering_ci\": \"[-0.8, 11.4]\",\n      \"ci_width_perturbation\": 12.0\n    },\n    \"tables\": [\n      {\n        \"name\": \"Perturbation Control Results\",\n        \"columns\": [\n          \"condition\",\n          \"violation_rate\",\n          \"Δpp_vs_baseline\",\n          \"95% CI\"\n        ],\n        \"rows\": [\n          [\n            \"unambiguous_baseline\",\n            \"5.5%\",\n            \"—\",\n            \"—\"\n          ],\n          [\n            \"synonym_substitution\",\n            \"8.6%\",\n            \"+3.1pp\",\n            \"[-3.2, 9.4]\"\n          ],\n          [\n            \"clause_reordering\",\n            \"10.8%\",\n            \"+5.3pp\",\n            \"[-0.8, 11.4]\"\n          ],\n          [\n            \"perturbation_pooled\",\n            \"9.7%\",\n            \"+4.2pp\",\n            \"[-1.8, 10.2]\"\n          ],\n          [\n            \"ambiguous\",\n            \"37.0%\",\n            \"+31.5pp\",\n            \"[26.8, 36.2]\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Perturbation Verdict Summary\",\n        \"columns\": [\n          \"metric\",\n          \"value\",\n          \"threshold\",\n          \"verdict\"\n        ],\n        \"rows\": [\n          [\n            \"Δ_perturb\",\n            \"4.2pp\",\n            \"< 5pp\",\n            \"✓ PASS\"\n          ],\n          [\n            \"ratio\",\n            \"0.13\",\n            \"< 0.15\",\n            \"✓ PASS\"\n          ],\n          [\n            \"CI_contains_0\",\n            \"yes\",\n            \"required\",\n            \"✓\"\n          ],\n          [\n            \"CI_width\",\n            \"12.0pp\",\n            \"< 15pp\",\n            \"✓ (marginal)\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"PASS verdict 确保 C1 因果 claim 在任何 tier 下成立。 这是 paper 的 methodological backbone——区别于所有 prior work (DRIP-R, PhantomPolicy 均无此控制)。\\n\\n\\nPerturbation control 在 worst tier 下仍 PASS——binary effect 的因果性不受 layer hierarchy 问题影响。 Δ_perturb=4.2pp (CI 含 0): synonym substitution (3.1pp) 和 clause reordering (5.3pp) 均不引起 meaningful violation rate 变化。Ratio=0.13 < 0.15 → PASS 最强形式。 Clause reordering 略高 (5.3pp) 源于轻微 primacy/recency effect，但远小于 ambiguity effect。 CI width 12.0pp 接近但未超过 15pp 追加阈值——worst tier 下这是 marginal 风险， 但当前数据足够。这个 PASS 是 worst tier 的最大 silver lining: 即使 type hierarchy 崩溃，binary ambiguity effect 仍有最强因果证据支撑， 使 reframe (C) \\\"Massive Binary Effect\\\" 有坚实因果基础。\\n\"\n  },\n  {\n    \"name\": \"full_study_api\",\n    \"description\": \"300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6) = 1,800 episodes。 在原 2-model 基础上新增 Claude。Cross-judge evaluation。\\n\",\n    \"results\": {\n      \"total_episodes\": 1800,\n      \"gpt54_rates\": {\n        \"auth_scope\": 0.55,\n        \"incompleteness\": 0.52,\n        \"cp\": 0.35,\n        \"scopal\": 0.4,\n        \"lexical\": 0.38,\n        \"coreferential\": 0.25\n      },\n      \"gpt41_rates\": {\n        \"auth_scope\": 0.53,\n        \"incompleteness\": 0.5,\n        \"cp\": 0.34,\n        \"scopal\": 0.39,\n        \"lexical\": 0.36,\n        \"coreferential\": 0.24\n      },\n      \"claude_rates\": {\n        \"auth_scope\": 0.38,\n        \"incompleteness\": 0.36,\n        \"cp\": 0.28,\n        \"scopal\": 0.33,\n        \"lexical\": 0.3,\n        \"coreferential\": 0.42\n      },\n      \"gpt54_binary_effect_pp\": 36.2,\n      \"gpt41_binary_effect_pp\": 34.0,\n      \"claude_binary_effect_pp\": 26.5,\n      \"gpt54_layer_gap_pp\": 13.0,\n      \"gpt41_layer_gap_pp\": 12.7,\n      \"claude_layer_gap_pp\": -1.0,\n      \"binary_effect_3api_pp\": 32.7,\n      \"layer_gap_3api_pp\": 8.2,\n      \"cramers_v_3api\": 0.15,\n      \"model_main_effect_p_3api\": 0.004,\n      \"model_type_interaction_p_3api\": 0.018,\n      \"avg_unamb_rate_3api\": 0.055,\n      \"claude_unamb_rate\": 0.08,\n      \"claude_amb_avg\": 0.345\n    },\n    \"tables\": [\n      {\n        \"name\": \"Per-Model Per-Type Violation Rates (Ambiguous Condition)\",\n        \"columns\": [\n          \"type\",\n          \"layer\",\n          \"gpt-5.4\",\n          \"gpt-4.1\",\n          \"claude-sonnet-4-6\",\n          \"3-API_pooled\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            \"spec\",\n            \"55%\",\n            \"53%\",\n            \"38%\",\n            \"48.7%\"\n          ],\n          [\n            \"incompleteness\",\n            \"spec\",\n            \"52%\",\n            \"50%\",\n            \"36%\",\n            \"46.0%\"\n          ],\n          [\n            \"cond_polysemy\",\n            \"spec\",\n            \"35%\",\n            \"34%\",\n            \"28%\",\n            \"32.3%\"\n          ],\n          [\n            \"scopal\",\n            \"ling\",\n            \"40%\",\n            \"39%\",\n            \"33%\",\n            \"37.3%\"\n          ],\n          [\n            \"lexical\",\n            \"ling\",\n            \"38%\",\n            \"36%\",\n            \"30%\",\n            \"34.7%\"\n          ],\n          [\n            \"coreferential\",\n            \"ling\",\n            \"25%\",\n            \"24%\",\n            \"42%\",\n            \"30.3%\"\n          ],\n          [\n            \"spec_avg\",\n            \"—\",\n            \"47.3%\",\n            \"45.7%\",\n            \"34.0%\",\n            \"42.3%\"\n          ],\n          [\n            \"ling_avg\",\n            \"—\",\n            \"34.3%\",\n            \"33.0%\",\n            \"35.0%\",\n            \"34.1%\"\n          ],\n          [\n            \"layer_gap\",\n            \"—\",\n            \"+13.0pp\",\n            \"+12.7pp\",\n            \"-1.0pp\",\n            \"+8.2pp\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Binary Effect by API Model\",\n        \"columns\": [\n          \"model\",\n          \"amb_rate\",\n          \"unamb_rate\",\n          \"Δpp\",\n          \"McNemar_OR\",\n          \"p\"\n        ],\n        \"rows\": [\n          [\n            \"gpt-5.4\",\n            \"40.8%\",\n            \"4.6%\",\n            \"+36.2pp\",\n            38.5,\n            \"<0.0001\"\n          ],\n          [\n            \"gpt-4.1\",\n            \"39.3%\",\n            \"5.3%\",\n            \"+34.0pp\",\n            31.2,\n            \"<0.0001\"\n          ],\n          [\n            \"claude-sonnet-4-6\",\n            \"34.5%\",\n            \"8.0%\",\n            \"+26.5pp\",\n            16.8,\n            \"<0.0001\"\n          ],\n          [\n            \"3-API_pooled\",\n            \"38.2%\",\n            \"5.5%\",\n            \"+32.7pp\",\n            28.4,\n            \"<0.0001\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Claude 的加入将 3-API layer gap 压缩至 8.2pp (从 2-model 19pp)。 model×type interaction 已显著 (p=0.018)——plan_003 加入 Qwen 后会进一步恶化。 Claude 的 coreferential 高 rate 机制: RLHF 的 safety training 覆盖了 authorization-class violations 但不覆盖 referential-class misinterpretation，导致 asymmetric vulnerability。 C3 (universal layer hierarchy) 在此阶段已不可维持。\\n\\n\\nGPT 系 (gpt-5.4, gpt-4.1) 复现 plan_002 原始 pattern: spec >> ling，两模型高度一致 (rank ρ=0.94)。GPT 对 authorization boundary 和 incompleteness 的 pragmatic underspecification 高度敏感——缺乏 explicit permission 时倾向 assume-and-act。\\nClaude 展现截然不同的 vulnerability profile——worst tier 的第一个转折点: (a) auth_scope/incompleteness 显著低 (38%/36% vs GPT 55%/52%): Claude RLHF 训练 强化了 \\\"不确定时 refuse\\\" 的行为，specification-layer ambiguity 更多触发 refusal 而非 violation。 (b) coreferential 显著高 (42% vs GPT 25%): Claude 在 RC attachment 歧义上 系统性选择 wider-scope interpretation (执行而非收窄)。RC attachment 不触发 Claude 的 safety refusal mechanism (与 auth boundary 不同)，因此 Claude 在此 \\\"放松警惕\\\"。 (c) 结果: Claude layer gap 反转 (ling 35.0% > spec 34.0%)。 3-API pooled layer gap 从 2-model 的 19pp 压缩至 8.2pp。\\nModel×type interaction 已在 3 API 模型中显著 (p=0.018)—— 尚未加入 Qwen 就已可见 type ranking 非 universal。 Claude binary effect 仅 +26.5pp: 整体更保守 (unamb baseline 8% vs GPT ~4.5%), ambiguous 条件下更多 refuse/ask 而非 violate。\\n\"\n  },\n  {\n    \"name\": \"full_study_local\",\n    \"description\": \"300 clauses × 2 conditions × 2 local models (Qwen3-8B, Qwen3-32B-AWQ via vLLM) = 1,200 episodes。 48 GPU-hours on RTX PRO 6000。\\n\",\n    \"results\": {\n      \"total_episodes\": 1200,\n      \"qwen8b_rates\": {\n        \"auth_scope\": 0.28,\n        \"incompleteness\": 0.3,\n        \"cp\": 0.25,\n        \"scopal\": 0.32,\n        \"lexical\": 0.3,\n        \"coreferential\": 0.45\n      },\n      \"qwen8b_binary_effect_pp\": 23.7,\n      \"qwen8b_unamb_rate\": 0.08,\n      \"qwen8b_amb_avg\": 0.317,\n      \"qwen8b_layer_gap_pp\": -8.0,\n      \"qwen8b_spec_avg\": 0.277,\n      \"qwen8b_ling_avg\": 0.357,\n      \"qwen32b_rates\": {\n        \"auth_scope\": 0.4,\n        \"incompleteness\": 0.42,\n        \"cp\": 0.3,\n        \"scopal\": 0.35,\n        \"lexical\": 0.33,\n        \"coreferential\": 0.38\n      },\n      \"qwen32b_binary_effect_pp\": 30.3,\n      \"qwen32b_unamb_rate\": 0.06,\n      \"qwen32b_amb_avg\": 0.363,\n      \"qwen32b_layer_gap_pp\": 2.0,\n      \"qwen32b_spec_avg\": 0.373,\n      \"qwen32b_ling_avg\": 0.353,\n      \"binary_effect_2local_pp\": 27.0,\n      \"layer_gap_2local_pp\": -3.0,\n      \"model_type_interaction_2local_p\": 0.041\n    },\n    \"tables\": [\n      {\n        \"name\": \"Per-Model Per-Type Violation Rates (Local Models, Ambiguous)\",\n        \"columns\": [\n          \"type\",\n          \"layer\",\n          \"Qwen3-8B\",\n          \"Qwen3-32B-AWQ\",\n          \"2-local_pooled\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            \"spec\",\n            \"28%\",\n            \"40%\",\n            \"34.0%\"\n          ],\n          [\n            \"incompleteness\",\n            \"spec\",\n            \"30%\",\n            \"42%\",\n            \"36.0%\"\n          ],\n          [\n            \"cond_polysemy\",\n            \"spec\",\n            \"25%\",\n            \"30%\",\n            \"27.5%\"\n          ],\n          [\n            \"scopal\",\n            \"ling\",\n            \"32%\",\n            \"35%\",\n            \"33.5%\"\n          ],\n          [\n            \"lexical\",\n            \"ling\",\n            \"30%\",\n            \"33%\",\n            \"31.5%\"\n          ],\n          [\n            \"coreferential\",\n            \"ling\",\n            \"45%\",\n            \"38%\",\n            \"41.5%\"\n          ],\n          [\n            \"spec_avg\",\n            \"—\",\n            \"27.7%\",\n            \"37.3%\",\n            \"32.5%\"\n          ],\n          [\n            \"ling_avg\",\n            \"—\",\n            \"35.7%\",\n            \"35.3%\",\n            \"35.5%\"\n          ],\n          [\n            \"layer_gap\",\n            \"—\",\n            \"-8.0pp\",\n            \"+2.0pp\",\n            \"-3.0pp\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Binary Effect by Local Model\",\n        \"columns\": [\n          \"model\",\n          \"amb_rate\",\n          \"unamb_rate\",\n          \"Δpp\",\n          \"McNemar_OR\",\n          \"p\"\n        ],\n        \"rows\": [\n          [\n            \"Qwen3-8B\",\n            \"31.7%\",\n            \"8.0%\",\n            \"+23.7pp\",\n            9.4,\n            \"<0.0001\"\n          ],\n          [\n            \"Qwen3-32B-AWQ\",\n            \"36.3%\",\n            \"6.0%\",\n            \"+30.3pp\",\n            21.7,\n            \"<0.0001\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Qwen3-8B 的 reversed layer profile 是 worst tier 的 smoking gun。 与 GPT-5.4 的 type rank Spearman ρ=0.37 (weak)——两个模型本质上有不同的 vulnerability landscape。 Qwen3-32B 的 ρ=0.77 (moderate) 说明 scale 恢复了部分 alignment，但未完全收敛。 Binary effect 仍显著 (Qwen3-8B +23.7pp, p<0.0001)——ambiguity 对所有模型都有害， 但 \\\"哪种 ambiguity 更有害\\\" 取决于模型能力。\\n\\n\\nQwen3-8B 是 worst tier 的关键变量——vulnerability profile 质变:\\n(a) Auth_scope 仅 28% (GPT-5.4 的一半): 8B 参数模型缺乏 pragmatic reasoning 能力， 无法 \\\"推断\\\" implicit permission boundary 并据此行动——不是因为保守 refuse (像 Claude)， 而是因为根本不理解 authorization 的 pragmatic implication，倾向 ignore 或 default 行为。 低 auth_scope violation ≠ 安全，只是不同的 failure mode (inaction vs wrong action)。\\n(b) Coreferential 高达 45% (GPT-5.4 的 1.8 倍): 小模型更依赖 surface syntactic heuristics (如 left-attachment bias for RC)。GPT-5.4 能利用 tool response 做部分 disambiguation (Berry & Kamsties 的 \\\"disambiguation channel\\\")，Qwen3-8B 不具备此能力—— 对 linguistic-layer 反而更脆弱。\\n(c) Layer gap 反转至 -8pp (ling 35.7% > spec 27.7%): 完全颠覆 GPT 的 spec > ling pattern。 机制: 小模型的 pragmatic processing 不足使 spec-layer 失去 \\\"特别危险\\\" 的地位， 而 syntactic processing 的 surface heuristic 依赖使 ling-layer 变得更危险。\\nQwen3-32B-AWQ 居中 (gap +2pp, nearly flat): scale 部分恢复了 spec-layer sensitivity， 但未达 GPT 水平。AWQ 4-bit 量化可能引入额外 noise 但不改变 qualitative pattern。 这支持 \\\"layer gap 是 emergent capability\\\"——需要足够的 pragmatic reasoning 能力 才能 \\\"解锁\\\" specification-layer 的特殊危险性。\\n\"\n  },\n  {\n    \"name\": \"full_study_analysis\",\n    \"description\": \"3,000 episodes 统计分析: C1 binary effect, C2 type hierarchy, C3 layer effect, C4 model×type interaction, power analysis, TOST, inter-model agreement, information delta control。\\n\",\n    \"results\": {\n      \"binary_effect_5model_pp\": 30.2,\n      \"binary_effect_5model_ci\": \"[27.5, 32.9]\",\n      \"mcnemar_or_5model\": 24.1,\n      \"mcnemar_or_ci\": \"[16.3, 35.6]\",\n      \"mcnemar_p\": \"<0.0001\",\n      \"per_type_all_significant\": true,\n      \"weakest_type_effect\": \"coreferential +22.8pp (Qwen3-8B drags avg down from +16pp to... wait, UP — Qwen3-8B has high coreferential)\",\n      \"omnibus_chi2_5model\": 18.7,\n      \"omnibus_p_5model\": 0.002,\n      \"cramers_v_5model\": 0.11,\n      \"pooled_rates\": {\n        \"auth_scope\": \"42.8%\",\n        \"incompleteness\": \"42.0%\",\n        \"cp\": \"30.4%\",\n        \"scopal\": \"35.8%\",\n        \"lexical\": \"33.4%\",\n        \"coreferential\": \"34.8%\"\n      },\n      \"spec_avg_5model\": \"38.4%\",\n      \"ling_avg_5model\": \"34.7%\",\n      \"layer_gap_5model_pp\": 3.7,\n      \"layer_gap_ci\": \"[-1.2, 8.6]\",\n      \"layer_gap_p\": 0.14,\n      \"model_type_interaction_chi2\": 52.3,\n      \"model_type_interaction_p\": 0.008,\n      \"model_type_interaction_v\": 0.089,\n      \"model_main_effect_p\": 0.001,\n      \"model_main_effect_v\": 0.072,\n      \"interaction_lrt_chi2\": 38.6,\n      \"interaction_lrt_p\": 0.003,\n      \"interaction_lrt_df\": 20,\n      \"rank_rho_gpt41\": 0.94,\n      \"rank_rho_claude\": 0.54,\n      \"rank_rho_qwen32b\": 0.77,\n      \"rank_rho_qwen8b\": 0.37,\n      \"tost_15pp_equivalent_pairs\": \"6/15\",\n      \"tost_10pp_equivalent_pairs\": \"2/15\",\n      \"mde_c2_v\": 0.18,\n      \"mde_c3_pp\": 9.5,\n      \"observed_c2_v\": 0.11,\n      \"observed_c3_gap\": 3.7,\n      \"fleiss_kappa_ambiguous\": 0.62,\n      \"fleiss_kappa_unambiguous\": 0.85,\n      \"same_interpretation_pct_ambiguous\": 0.58,\n      \"different_interpretation_pct_ambiguous\": 0.42,\n      \"avg_token_delta_spec\": 3.4,\n      \"avg_token_delta_ling\": 1.7,\n      \"token_delta_violation_corr\": 0.31,\n      \"token_delta_partial_r_after_type\": 0.14\n    },\n    \"tables\": [\n      {\n        \"name\": \"5-Model Pooled Per-Type Results\",\n        \"columns\": [\n          \"type\",\n          \"layer\",\n          \"amb_rate\",\n          \"unamb_rate\",\n          \"Δpp\",\n          \"95% CI\",\n          \"per-type McNemar p\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            \"spec\",\n            \"42.8%\",\n            \"5.8%\",\n            \"+37.0pp\",\n            \"[31.2, 42.8]\",\n            \"<0.0001\"\n          ],\n          [\n            \"incompleteness\",\n            \"spec\",\n            \"42.0%\",\n            \"5.4%\",\n            \"+36.6pp\",\n            \"[30.8, 42.4]\",\n            \"<0.0001\"\n          ],\n          [\n            \"cond_polysemy\",\n            \"spec\",\n            \"30.4%\",\n            \"4.8%\",\n            \"+25.6pp\",\n            \"[20.1, 31.1]\",\n            \"<0.0001\"\n          ],\n          [\n            \"scopal\",\n            \"ling\",\n            \"35.8%\",\n            \"5.6%\",\n            \"+30.2pp\",\n            \"[24.5, 35.9]\",\n            \"<0.0001\"\n          ],\n          [\n            \"lexical\",\n            \"ling\",\n            \"33.4%\",\n            \"5.2%\",\n            \"+28.2pp\",\n            \"[22.6, 33.8]\",\n            \"<0.0001\"\n          ],\n          [\n            \"coreferential\",\n            \"ling\",\n            \"34.8%\",\n            \"6.0%\",\n            \"+28.8pp\",\n            \"[23.1, 34.5]\",\n            \"<0.0001\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Layer Effect by Model\",\n        \"columns\": [\n          \"model\",\n          \"spec_avg\",\n          \"ling_avg\",\n          \"layer_gap_pp\",\n          \"direction\"\n        ],\n        \"rows\": [\n          [\n            \"gpt-5.4\",\n            \"47.3%\",\n            \"34.3%\",\n            \"+13.0pp\",\n            \"spec > ling\"\n          ],\n          [\n            \"gpt-4.1\",\n            \"45.7%\",\n            \"33.0%\",\n            \"+12.7pp\",\n            \"spec > ling\"\n          ],\n          [\n            \"claude-sonnet-4-6\",\n            \"34.0%\",\n            \"35.0%\",\n            \"-1.0pp\",\n            \"≈ flat (reversed)\"\n          ],\n          [\n            \"Qwen3-32B-AWQ\",\n            \"37.3%\",\n            \"35.3%\",\n            \"+2.0pp\",\n            \"≈ flat\"\n          ],\n          [\n            \"Qwen3-8B\",\n            \"27.7%\",\n            \"35.7%\",\n            \"-8.0pp\",\n            \"ling > spec (reversed)\"\n          ],\n          [\n            \"5-model_pooled\",\n            \"38.4%\",\n            \"34.7%\",\n            \"+3.7pp\",\n            \"n.s. (p=0.14)\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Model × Type Interaction: Type Rank by Model (ambiguous violation rate)\",\n        \"columns\": [\n          \"rank\",\n          \"gpt-5.4\",\n          \"gpt-4.1\",\n          \"claude\",\n          \"Qwen3-32B\",\n          \"Qwen3-8B\"\n        ],\n        \"rows\": [\n          [\n            \"1 (highest)\",\n            \"auth_scope\",\n            \"auth_scope\",\n            \"coreferential\",\n            \"incompleteness\",\n            \"coreferential\"\n          ],\n          [\n            2,\n            \"incompleteness\",\n            \"incompleteness\",\n            \"auth_scope\",\n            \"auth_scope\",\n            \"scopal\"\n          ],\n          [\n            3,\n            \"scopal\",\n            \"scopal\",\n            \"incompleteness\",\n            \"coreferential\",\n            \"lexical\"\n          ],\n          [\n            4,\n            \"lexical\",\n            \"lexical\",\n            \"scopal\",\n            \"scopal\",\n            \"incompleteness\"\n          ],\n          [\n            5,\n            \"CP\",\n            \"CP\",\n            \"lexical\",\n            \"lexical\",\n            \"auth_scope\"\n          ],\n          [\n            \"6 (lowest)\",\n            \"coreferential\",\n            \"coreferential\",\n            \"CP\",\n            \"CP\",\n            \"CP\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Inter-Model Agreement (Berry & Kamsties Analysis)\",\n        \"columns\": [\n          \"metric\",\n          \"ambiguous\",\n          \"unambiguous\",\n          \"interpretation\"\n        ],\n        \"rows\": [\n          [\n            \"Fleiss_κ\",\n            0.62,\n            0.85,\n            \"moderate vs almost-perfect\"\n          ],\n          [\n            \"same_interpretation_pct\",\n            \"58%\",\n            \"91%\",\n            \"ambiguity drives divergence\"\n          ],\n          [\n            \"systematic_bias_pct\",\n            \"34%\",\n            \"7%\",\n            \"models differ in fallback strategy\"\n          ],\n          [\n            \"random_disagreement_pct\",\n            \"8%\",\n            \"2%\",\n            \"noise floor\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Plan_004 是 worst tier 定性的核心。三个结论: (1) C1 survives robustly: +30.2pp 是 massive causal effect, 6 types all significant, perturbation-backed。 (2) C2/C3 collapse: V=0.11 weak, layer gap n.s.——不能声称 universal type hierarchy。 但 interaction 显著 (p=0.008) 说明 types 确实 differently dangerous——只是 \\\"哪个更危险\\\" 是 model-dependent。 (3) C4 升级为 secondary finding: three vulnerability profiles (GPT spec-sensitive, Claude coref-sensitive, Qwen8B ling-sensitive) 是 novel 且 practically relevant insight。 Reframe: layer hierarchy → model-dependent vulnerability profiles。\\n\\n\\nC1 (+30.2pp, CI [27.5, 32.9]): 从 plan_002 的 +36.5pp 下降 6pp。 原因: Qwen3-8B 的弱 binary effect (+23.7pp) 和 Claude 的 (+26.5pp) 拉低 pooled 值。 但 CI 远离零，OR=24.1 仍 massive——文献中最大的 ambiguity → safety 因果效应。 Per-type 均显著 (最弱: CP +25.6pp)——\\\"所有 ambiguity 都 nocuous\\\" 成立。\\nC2 (V=0.11, p=0.002): omnibus χ² 显著说明 types 不完全等价， 但 V=0.11 (weak) 远低于 plan_002 2-model 的 V=0.207。 原因: open-source 模型的 reversed/flat profile 平均化了 type 间差异。 具体看: auth_scope/incompleteness 仍最高 (~43%)，但 coreferential 从 25% 跳至 34.8% (Claude 42% + Qwen3-8B 45% 拉高)，压缩了原本的 range。 TOST: ±15pp 有 6/15 pairs equivalent (原 3/15)——更多 type pairs 在统计上不可区分。\\nC3 (gap 3.7pp, p=0.14, n.s.): layer gap 不显著。CI [-1.2, 8.6] 包含 0。 GPT 的 positive gap (~13pp) 被 Claude (-1pp) + Qwen3-8B (-8pp) 抵消。 MDE=9.5pp: 即使有 power，跨模型方向不一致使 pooled estimate 本身无 interpretive value。 Layer hierarchy 从 \\\"finding\\\" 变为 \\\"GPT-family tendency\\\"。\\nC4 (interaction p=0.008): worst tier 最 informative finding。 5×6 contingency table 中 model×type interaction 高度显著——type ranking 是 model-dependent。 Three distinct vulnerability profiles: - GPT family: spec-sensitive (auth_scope/incompleteness peak) - Claude: coreferential-sensitive (RLHF safety coverage gap) - Qwen3-8B: ling-sensitive (surface heuristic dependence) Spearman ρ gradient: GPT intra-family 0.94 > Qwen3-32B 0.77 > Claude 0.54 > Qwen3-8B 0.37\\nInter-model Fleiss κ=0.62 (ambiguous) vs 0.85 (unambiguous): 分歧主要在 ambiguous clauses——ambiguity 暴露了 model-specific interpretation strategies。 58% same interpretation → 不是 true nocuity (divergent readings) 而是 systematic bias (models differ in fallback strategies when they can't resolve ambiguity)。 Berry & Kamsties 框架下: 这是 \\\"systematic nocuity\\\" (所有模型都错但错法不同) 而非 \\\"divergent nocuity\\\" (不同解读)。\\nToken delta: spec-layer 3.4 vs ling-layer 1.7 tokens，与 violation rate 弱相关 (r=0.31)。 但 partial correlation after controlling for type = 0.14 (n.s.)—— token delta 不是 independent confound，与 type 共线。需 disclose 但不构成 fatal threat。\\n\"\n  },\n  {\n    \"name\": \"error_analysis\",\n    \"description\": \"300 violation traces (50/type) 定性分析。Failure mode 分类、 跨层区分检验、ambiguity blindness 量化、model-specific pattern 分析。\\n\",\n    \"results\": {\n      \"total_traces_sampled\": 300,\n      \"failure_modes\": {\n        \"assumption_based_action\": \"38%\",\n        \"scope_misapplication\": \"22%\",\n        \"conservative_refusal\": \"15%\",\n        \"arbitrary_rule_selection\": \"14%\",\n        \"permission_escalation\": \"11%\"\n      },\n      \"failure_mode_layer_match_pct\": 42,\n      \"assumption_in_spec_pct\": 40,\n      \"assumption_in_ling_pct\": 36,\n      \"scope_misapplication_in_spec_pct\": 18,\n      \"scope_misapplication_in_ling_pct\": 26,\n      \"explicit_ambiguity_mention_pct\": 8,\n      \"implicit_deliberation_pct\": 20,\n      \"surface_adoption_pct\": 72,\n      \"gpt54_assumption_pct\": 45,\n      \"gpt54_explicit_mention_pct\": 12,\n      \"claude_conservative_refusal_pct\": 28,\n      \"claude_explicit_mention_pct\": 6,\n      \"qwen8b_surface_adoption_pct\": 85,\n      \"qwen8b_explicit_mention_pct\": 2\n    },\n    \"tables\": [\n      {\n        \"name\": \"Failure Mode Distribution by Layer\",\n        \"columns\": [\n          \"failure_mode\",\n          \"spec_layer\",\n          \"ling_layer\",\n          \"pooled\",\n          \"layer_specificity\"\n        ],\n        \"rows\": [\n          [\n            \"assumption_based_action\",\n            \"40%\",\n            \"36%\",\n            \"38%\",\n            \"low (Δ=4pp)\"\n          ],\n          [\n            \"scope_misapplication\",\n            \"18%\",\n            \"26%\",\n            \"22%\",\n            \"moderate (ling-biased)\"\n          ],\n          [\n            \"conservative_refusal\",\n            \"14%\",\n            \"16%\",\n            \"15%\",\n            \"low (Δ=2pp)\"\n          ],\n          [\n            \"arbitrary_rule_selection\",\n            \"16%\",\n            \"12%\",\n            \"14%\",\n            \"low (Δ=4pp)\"\n          ],\n          [\n            \"permission_escalation\",\n            \"12%\",\n            \"10%\",\n            \"11%\",\n            \"low (Δ=2pp)\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Ambiguity Awareness in Agent Traces by Model\",\n        \"columns\": [\n          \"awareness_level\",\n          \"gpt-5.4\",\n          \"gpt-4.1\",\n          \"claude\",\n          \"Qwen3-32B\",\n          \"Qwen3-8B\",\n          \"pooled\"\n        ],\n        \"rows\": [\n          [\n            \"explicit_mention\",\n            \"12%\",\n            \"10%\",\n            \"6%\",\n            \"5%\",\n            \"2%\",\n            \"8%\"\n          ],\n          [\n            \"implicit_deliberation\",\n            \"25%\",\n            \"22%\",\n            \"24%\",\n            \"18%\",\n            \"13%\",\n            \"20%\"\n          ],\n          [\n            \"surface_adoption\",\n            \"63%\",\n            \"68%\",\n            \"70%\",\n            \"77%\",\n            \"85%\",\n            \"72%\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Failure Mode by Model\",\n        \"columns\": [\n          \"model\",\n          \"assumption_based\",\n          \"scope_misapplication\",\n          \"conservative_refusal\",\n          \"arbitrary_rule\",\n          \"permission_escalation\"\n        ],\n        \"rows\": [\n          [\n            \"gpt-5.4\",\n            \"45%\",\n            \"24%\",\n            \"8%\",\n            \"13%\",\n            \"10%\"\n          ],\n          [\n            \"gpt-4.1\",\n            \"42%\",\n            \"23%\",\n            \"10%\",\n            \"15%\",\n            \"10%\"\n          ],\n          [\n            \"claude\",\n            \"22%\",\n            \"18%\",\n            \"28%\",\n            \"16%\",\n            \"16%\"\n          ],\n          [\n            \"Qwen3-32B\",\n            \"38%\",\n            \"22%\",\n            \"14%\",\n            \"14%\",\n            \"12%\"\n          ],\n          [\n            \"Qwen3-8B\",\n            \"43%\",\n            \"20%\",\n            \"12%\",\n            \"15%\",\n            \"10%\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Error analysis 无法支撑 layer-specific failure mechanism 叙事 (failure_mode_layer_match 仅 42%)， 但强力支撑 \\\"Ambiguity Blindness\\\" 作为 §6 核心: 92% traces 展现 blindness 是 universal 现象——所有模型在所有 type 上 都无法 meta-cognitively detect ambiguity。这连接 Ferreira 的 good-enough processing: agents 对 grammatically fluent ambiguous clauses 做 shallow parse and act， 不触发 reanalysis/clarification。 Practical implication: 与其按 type 排序 (ranking model-dependent)， 不如投资 any-ambiguity detection——因为 agent 本身 blind to all types equally。 这完美 align reframe (C) binary effect + (B) blindness mechanism。\\n\\n\\nCross-layer failure mode overlap 42%: 如果 layer 是 deterministic predictor of failure mechanism， match 应接近 80%+。实际仅 42% 说明 failure mode 不由 layer 决定。 \\\"Assumption-based action\\\" (遇到歧义直接假设一种解读并执行) 是 dominant mode， 且在两个 layer 上近乎等比例 (spec 40%, ling 36%)—— agent 的 failure mechanism 是 universal 的 \\\"guess and act\\\" 而非 type-specific misparse。\\n反直觉: scope_misapplication 在 ling-layer (26%) > spec-layer (18%)—— 因为 scopal/coreferential 的 syntactic structure 确实触发更多 scope parsing error， 而 spec-layer 的 failure 更多是 \\\"assume permission exists\\\" (assumption-based)。 但这个差异不足以支撑 clean layer mechanism story——两个 layer 都有大量 assumption-based failures。\\nAmbiguity blindness: 92% traces 中 agent 未 meta-cognitively 识别歧义。 这是 universal 现象——所有模型所有 types 都展现。差异仅在 degree: GPT-5.4 有 12% explicit mention (最高, 但仍极低)，Qwen3-8B 仅 2% (近乎完全 blind)。 Claude 的 conservative_refusal 28% (远高于平均) 解释了其低 auth_scope rate: Claude refuse 而非 violate，但这不是 ambiguity awareness—— 是 safety training 的 blanket conservatism，不区分 ambiguous vs unambiguous uncertainty。\\nModel-specific failure patterns 直接支撑 C4: GPT 的 assumption_based 45% (aggressive interpretation) vs Claude 的 refusal 28% (conservative) vs Qwen3-8B 的 surface_adoption 85% (uncritical execution)—— 三种 distinct failure strategies，对应三种 vulnerability profiles。\\n\"\n  },\n  {\n    \"name\": \"reliability_test\",\n    \"description\": \"30 clauses (5/type) × 3 replicates × 2 conditions × 5 models = 900 episodes。 Test-retest ICC, bootstrap CI width。\\n\",\n    \"results\": {\n      \"total_episodes\": 900,\n      \"icc_overall\": 0.68,\n      \"icc_per_type\": {\n        \"auth_scope\": 0.74,\n        \"incompleteness\": 0.72,\n        \"cp\": 0.65,\n        \"scopal\": 0.58,\n        \"lexical\": 0.63,\n        \"coreferential\": 0.48\n      },\n      \"bootstrap_ci_width_binary_effect_pp\": 11.5,\n      \"bootstrap_ci_width_per_type_pp\": 14.8,\n      \"max_replicate_swing_pp\": 12.3,\n      \"max_swing_type\": \"coreferential\",\n      \"icc_ambiguous_only\": 0.65,\n      \"icc_unambiguous_only\": 0.79\n    },\n    \"tables\": [\n      {\n        \"name\": \"ICC by Type\",\n        \"columns\": [\n          \"type\",\n          \"ICC_ambiguous\",\n          \"ICC_unambiguous\",\n          \"ICC_combined\",\n          \"max_replicate_swing_pp\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            0.76,\n            0.82,\n            0.74,\n            \"8.2pp\"\n          ],\n          [\n            \"incompleteness\",\n            0.73,\n            0.8,\n            0.72,\n            \"9.1pp\"\n          ],\n          [\n            \"cond_polysemy\",\n            0.67,\n            0.78,\n            0.65,\n            \"10.5pp\"\n          ],\n          [\n            \"scopal\",\n            0.6,\n            0.76,\n            0.58,\n            \"11.8pp\"\n          ],\n          [\n            \"lexical\",\n            0.64,\n            0.77,\n            0.63,\n            \"10.2pp\"\n          ],\n          [\n            \"coreferential\",\n            0.5,\n            0.72,\n            0.48,\n            \"12.3pp\"\n          ],\n          [\n            \"overall\",\n            0.7,\n            0.79,\n            0.68,\n            \"—\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Reliability 数据进一步支撑 \\\"focus on binary, not type\\\": binary effect reliability adequate (ICC 0.68 pooled, CI 11.5pp width on 30pp effect), type-level reliability insufficient for fine-grained ranking claims (coreferential ICC 0.48, CI 14.8pp width on ~5pp type differences)。 Coreferential 的低 reliability 是 compound 问题——clause quality + model heterogeneity + sampling noise。 Paper 需 explicitly discuss type-level measurement uncertainty。\\n\\n\\nOverall ICC 0.68 (moderate): 可接受但不 excellent。 Signature worst-tier pattern: (a) Auth_scope/incompleteness 最 reliable (0.74/0.72): 高 violation rate type 的 absolute swing 对 ICC 影响较小 (±8pp on 43% base vs ±8pp on 35% base)。 (b) Coreferential 最 unreliable (0.48): 三重叠加效应—— clause 质量 (plan_001 pass_rate 0.88) × 跨模型行为异质 (Qwen3-8B 45% vs GPT 25%) × API temperature sampling noise。这三者使 coreferential replicate variance 极大。 (c) Scopal ICC 0.58: 与 MVP→plan_002 的 51.7%→40% historical swing 一致。\\nBootstrap CI width 11.5pp (binary effect) 超过 <10pp 理想阈值: per-type CI width 14.8pp 更宽——type-level 比较 power 有限。 V=0.11 的 type effect 在此 noise level 下可能部分是 noise, 也可能被 noise 掩盖。 但 binary effect (30.2pp ÷ 11.5pp CI width = SNR 2.6) 仍 robust。\\nUnambiguous ICC 0.79 > ambiguous 0.65: ambiguous condition 的 variance 更大—— agent 在 ambiguous clause 上的 behavior 本身不稳定，进一步削弱 type-level precision。\\n\"\n  },\n  {\n    \"name\": \"realism_validation\",\n    \"description\": \"Synthetic clause linguistic properties vs DRIP-R natural ambiguities。 KS tests on sentence length, parse depth, Flesch-Kincaid, TTR。\\n\",\n    \"results\": {\n      \"ks_sentence_length\": {\n        \"statistic\": 0.18,\n        \"p\": 0.12\n      },\n      \"ks_parse_depth\": {\n        \"statistic\": 0.21,\n        \"p\": 0.08\n      },\n      \"ks_flesch_kincaid\": {\n        \"statistic\": 0.14,\n        \"p\": 0.23\n      },\n      \"ks_ttr\": {\n        \"statistic\": 0.1,\n        \"p\": 0.41\n      },\n      \"synthetic_mean_tokens\": 24.2,\n      \"drip_r_mean_tokens\": 27.8,\n      \"synthetic_mean_parse_depth\": 3.1,\n      \"drip_r_mean_parse_depth\": 3.8,\n      \"overall_verdict\": \"acceptable\",\n      \"noted_difference\": \"synthetic clauses slightly shorter and shallower parse trees — matched-pair design favors minimal pairs\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Linguistic Property Comparison: Synthetic vs DRIP-R\",\n        \"columns\": [\n          \"property\",\n          \"synthetic_mean\",\n          \"DRIP-R_mean\",\n          \"KS_statistic\",\n          \"p_value\"\n        ],\n        \"rows\": [\n          [\n            \"sentence_length (tokens)\",\n            24.2,\n            27.8,\n            0.18,\n            0.12\n          ],\n          [\n            \"parse_depth\",\n            3.1,\n            3.8,\n            0.21,\n            0.08\n          ],\n          [\n            \"Flesch-Kincaid\",\n            12.4,\n            11.8,\n            0.14,\n            0.23\n          ],\n          [\n            \"type-token_ratio\",\n            0.72,\n            0.7,\n            0.1,\n            0.41\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Realism pass。Method 中 disclose parse depth 差异。 Reviewer RC4 应答充分: matched-pair design 本身需要 synthetic control, linguistic properties 统计上与自然歧义不可区分。\\n\\n\\nRealism validation 基本独立于 worst tier: clause 的语言学属性不受 downstream 实验结果影响。KS tests 大部分 n.s. (p>0.05)—— surface properties 分布相似。Parse depth 边界显著 (p=0.08): synthetic clauses 稍简单因为 matched-pair design 倾向 minimal variation。 在 worst tier 下值得额外注意: 如果 synthetic clauses 系统性简单， 可能 underestimate real-world violation rate (更复杂的自然歧义可能更危险)。 但 +30pp binary effect 足够大，不太可能被此 bias 逆转。\\n\"\n  },\n  {\n    \"name\": \"judge_calibration\",\n    \"description\": \"100 episodes stratified by type×model×condition, 2 human annotators, LLM judge 校准。 Worst tier: F1 < 0.75 for ≥2 types, type-specific bias 暴露。\\n\",\n    \"results\": {\n      \"human_annotator_kappa\": 0.82,\n      \"judge_overall_f1\": 0.72,\n      \"judge_overall_precision\": 0.78,\n      \"judge_overall_recall\": 0.67,\n      \"judge_overall_kappa_vs_human\": 0.63,\n      \"judge_f1_per_type\": {\n        \"auth_scope\": 0.68,\n        \"incompleteness\": 0.76,\n        \"cp\": 0.79,\n        \"scopal\": 0.77,\n        \"lexical\": 0.74,\n        \"coreferential\": 0.61\n      },\n      \"auth_scope_bias\": \"under-detection: recall 0.56, precision 0.82 → misses subtle permission boundary crossings\",\n      \"coreferential_bias\": \"over-detection: recall 0.64, precision 0.58 → flags legitimate info-gathering as violations\",\n      \"judge_f1_tier1_critical\": 0.82,\n      \"judge_f1_tier2_moderate\": 0.68,\n      \"judge_f1_tier3_minor\": 0.55,\n      \"claude_judged_by_gpt54_f1\": 0.75,\n      \"gpt54_judged_by_gpt41_f1\": 0.69,\n      \"cross_judge_asymmetry_pp\": 6,\n      \"auth_scope_corrected\": \"+4-6pp (true rate likely ~47-49% not 42.8%)\",\n      \"coreferential_corrected\": \"-5-8pp (true rate likely ~27-30% not 34.8%)\",\n      \"corrected_cramers_v_estimate\": \"~0.14 (still weak)\"\n    },\n    \"tables\": [\n      {\n        \"name\": \"Judge Calibration by Type\",\n        \"columns\": [\n          \"type\",\n          \"precision\",\n          \"recall\",\n          \"F1\",\n          \"bias_direction\",\n          \"estimated_rate_correction\"\n        ],\n        \"rows\": [\n          [\n            \"auth_scope\",\n            0.82,\n            0.56,\n            0.68,\n            \"under-detection\",\n            \"+4-6pp\"\n          ],\n          [\n            \"incompleteness\",\n            0.8,\n            0.72,\n            0.76,\n            \"slight under-detection\",\n            \"+1-2pp\"\n          ],\n          [\n            \"cond_polysemy\",\n            0.81,\n            0.77,\n            0.79,\n            \"balanced\",\n            \"±1pp\"\n          ],\n          [\n            \"scopal\",\n            0.79,\n            0.75,\n            0.77,\n            \"balanced\",\n            \"±1pp\"\n          ],\n          [\n            \"lexical\",\n            0.76,\n            0.72,\n            0.74,\n            \"slight over-detection\",\n            \"-1-2pp\"\n          ],\n          [\n            \"coreferential\",\n            0.58,\n            0.64,\n            0.61,\n            \"over-detection\",\n            \"-5-8pp\"\n          ]\n        ]\n      },\n      {\n        \"name\": \"Judge Calibration by Severity Tier\",\n        \"columns\": [\n          \"severity\",\n          \"n_samples\",\n          \"precision\",\n          \"recall\",\n          \"F1\"\n        ],\n        \"rows\": [\n          [\n            \"tier-1_critical\",\n            35,\n            0.85,\n            0.79,\n            0.82\n          ],\n          [\n            \"tier-2_moderate\",\n            40,\n            0.73,\n            0.64,\n            0.68\n          ],\n          [\n            \"tier-3_minor\",\n            25,\n            0.6,\n            0.51,\n            0.55\n          ]\n        ]\n      },\n      {\n        \"name\": \"Cross-Judge Asymmetry\",\n        \"columns\": [\n          \"agent_model\",\n          \"judge_model\",\n          \"F1\",\n          \"note\"\n        ],\n        \"rows\": [\n          [\n            \"claude-sonnet-4-6\",\n            \"gpt-5.4\",\n            0.75,\n            \"strongest judge\"\n          ],\n          [\n            \"gpt-5.4\",\n            \"gpt-4.1\",\n            0.69,\n            \"weaker judge on stronger agent\"\n          ],\n          [\n            \"gpt-4.1\",\n            \"gpt-5.4\",\n            0.78,\n            \"strongest judge on mid-tier agent\"\n          ],\n          [\n            \"Qwen3-8B\",\n            \"gpt-5.4\",\n            0.71,\n            \"open-source traces harder to judge\"\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Judge calibration 是 worst tier 的第二个 structural threat (after model×type interaction)。 F1<0.75 for coreferential (0.61) + auth_scope (0.68) 直接削弱这两个 type 的数值可信度。 Paper 必须: (a) report calibration as standard practice, (b) provide bias-corrected estimates, (c) flag coreferential/auth_scope absolute values as measurement-sensitive, (d) disclose cross-judge asymmetry in Method。 Silver lining: binary effect 的 calibration 尚可 (overall F1=0.72, tier-1 F1=0.82)， C1 headline number 受影响最小。bias-corrected V ~0.14 仍 weak—— measurement correction 不改变 \\\"type hierarchy 不 robust\\\" 的 worst-tier 结论。\\n\\n\\nJudge calibration 暴露 worst tier 最有破坏力的 measurement issue:\\nCoreferential F1=0.61: LLM judge over-detect coreferential violations。 原因: agent 在 RC attachment 歧义下采取的 \\\"exploratory query\\\" (查询哪个 entity 适用) 被 judge 误判为 \\\"unauthorized action\\\" (false positive)。 Judge 缺乏 human 的 pragmatic judgment——无法区分 \\\"agent 在探索性确认\\\" vs \\\"agent 在违规操作\\\"。 结果: coreferential reported rate (34.8%) 高估 ~5-8pp，真实 rate 可能 ~27-30%。\\nAuth_scope F1=0.68: judge under-detect auth_scope violations。 原因: auth_scope violation 常表现为 \\\"subtle permission boundary crossing\\\"—— agent 在模糊授权范围内行动，不明显违规 (如: 给客户 10% 折扣，policy 说 \\\"reasonable discount\\\" 但未定义 boundary)。Judge 倾向 \\\"不确定则判 non-violation\\\" → false negative。 结果: auth_scope reported rate (42.8%) 低估 ~4-6pp，真实 rate 可能 ~47-49%。\\n两个 bias 方向相互作用——恰好压缩了 type 间差异: coreferential 高估 + auth_scope 低估 → 缩小 range → 降低 V 值。 Bias-corrected V 估计 ~0.14 (vs observed 0.11)——仍 weak, 不改变 \\\"type effect 弱\\\" 的结论， 但说明 raw V=0.11 有 measurement component。\\nCross-judge asymmetry 6pp: Claude 被 gpt-5.4 (最强 judge) 判定 F1=0.75， gpt-5.4 被 gpt-4.1 (较弱 judge) 判定仅 F1=0.69。 弱 judge 对强 model traces 更难准确判定——Method 必须 disclose。\\nPer-severity: tier-3 minor violations F1=0.55 (near random)—— judge 对 \\\"subtle/minor\\\" violations 几乎无法判定。 主要影响 severity-weighted analysis, binary violation/non-violation 受影响较小。\\n\"\n  },\n  {\n    \"name\": \"classifier_poc\",\n    \"description\": \"DeBERTa-v3-large binary ambiguity detector PoC。 Fine-tune on 240 pairs, eval on 60 held-out。\\n\",\n    \"results\": {\n      \"model\": \"DeBERTa-v3-large\",\n      \"train_size\": 240,\n      \"test_size\": 60,\n      \"test_f1\": 0.78,\n      \"test_precision\": 0.81,\n      \"test_recall\": 0.75,\n      \"per_type_f1\": {\n        \"auth_scope\": 0.82,\n        \"incompleteness\": 0.8,\n        \"cp\": 0.76,\n        \"scopal\": 0.79,\n        \"lexical\": 0.77,\n        \"coreferential\": 0.72\n      },\n      \"training_epochs\": 5,\n      \"best_epoch\": 3\n    },\n    \"tables\": [\n      {\n        \"name\": \"Classifier PoC Performance\",\n        \"columns\": [\n          \"metric\",\n          \"overall\",\n          \"auth_scope\",\n          \"incomp\",\n          \"CP\",\n          \"scopal\",\n          \"lexical\",\n          \"coref\"\n        ],\n        \"rows\": [\n          [\n            \"F1\",\n            0.78,\n            0.82,\n            0.8,\n            0.76,\n            0.79,\n            0.77,\n            0.72\n          ],\n          [\n            \"Precision\",\n            0.81,\n            0.85,\n            0.83,\n            0.78,\n            0.82,\n            0.8,\n            0.74\n          ],\n          [\n            \"Recall\",\n            0.75,\n            0.79,\n            0.77,\n            0.74,\n            0.76,\n            0.74,\n            0.7\n          ]\n        ]\n      }\n    ],\n    \"figures\": [],\n    \"analysis\": \"Classifier PoC 在 worst tier 下反而 perfectly narrative-aligned: binary detection feasible (F1=0.78), type-specific pipeline 不必要 (type ranking 本身 model-dependent)。Practical contribution 的 optimal framing: 投资 binary detector 而非 type-specific triage pipeline。 与 C1 massive binary effect + ambiguity blindness 形成 coherent practical story。\\n\\nF1=0.78 是 reasonable PoC 水平: 证明 binary ambiguity detection 是 feasible NLP task， 但远未 production-ready。Coreferential F1 最低 (0.72) 与 judge calibration (0.61) 和 reliability (ICC 0.48) 的 pattern 一致: coreferential 是最难检测/判定的 type。\\n在 worst tier reframe 下，classifier PoC 强化 reframe (C): \\\"任何 ambiguity detection (甚至 binary) 都有巨大安全收益\\\"—— F1=0.78 的 binary detector 在 +30pp violation rate gap 上 可提供 meaningful early warning。Type-specific detection 既不必要 (type ranking model-dependent) 也不额外有价值 (binary 已覆盖核心风险)。 这恰好与 worst tier 结论 align: binary detection = high ROI, type triage = low ROI。\\n\"\n  }\n]",
      "numLines": 1405,
      "startLine": 1,
      "totalLines": 1405
    }
  },
  "sourceToolAssistantUUID": "403644f6-aca6-4d97-83d5-373c1e7e470c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-21T04:42:47.814Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01A9SAQNGswwG8vY45YMyNKw`</summary>

```json
{
  "pattern": "**/plan_004*result*.json",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45b39f0d-e27f-42ac-bd8b-fdc34c50c43c",
  "isSidechain": false,
  "requestId": "req_011CbF6XP1Y5EhF5K9Ey6yL9",
  "type": "assistant",
  "uuid": "f420801f-b679-45af-bb22-b83bb909b7f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011h7rWtHkjZhTxPKrxQjFSh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3716,
      "cache_creation_input_tokens": 26242,
      "cache_read_input_tokens": 35531,
      "output_tokens": 13409,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 26242,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3716,
          "output_tokens": 13409,
          "cache_read_input_tokens": 35531,
          "cache_creation_input_tokens": 26242,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 26242
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

### Tool result

_source line 29 · 2026-05-21T04:42:47.881Z_

<details><summary>↩ Tool result · `toolu_01A9SAQNGswwG8vY45YMyNKw`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f420801f-b679-45af-bb22-b83bb909b7f9",
  "isSidechain": false,
  "promptId": "5178fc38-1c25-4e8e-a8fd-798a18075500",
  "type": "user",
  "uuid": "94136564-03f3-4e16-83e4-1010ee8a0c68",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 64,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "f420801f-b679-45af-bb22-b83bb909b7f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-21T04:42:47.910Z_

```json
{
  "parentUuid": "94136564-03f3-4e16-83e4-1010ee8a0c68",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "706e5f85-a754-4a8d-a06e-d2d78d934352",
  "timestamp": "2026-05-21T04:42:47.910Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：C3 layer effect 不成立，C4 interaction 弱化到 borderline，perturbation control 暴露 confound，judge calibration 差，需 reframe 围绕 C1+C2+C5 的 universal nocuity + type ta…",
  "leafUuid": "706e5f85-a754-4a8d-a06e-d2d78d934352",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Policy ambiguity universally harms LLM agents",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7"
}
```

---

### Assistant

_source line 33 · 2026-05-21T04:47:23.622Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. The key differences between this new Phase 1 worst-tier definition and the previous worst-tier imagined experiments are:

1. **Perturbation control**: Previous worst had PASS (Δ=4.2pp, ratio=0.13). New worst requires CONDITIONAL/WARNING (Δ=10-20pp). This is the biggest change.
2. **Models**: Previous used Qwen3-8B and Qwen3-32B-AWQ (local GPU). New uses Qwen3-235B and DeepSeek-V3 (API). This changes the model dynamics significantly.


3. **C4 interaction**: The new definition shifts from multiple distinct model profiles to being driven by a single Claude outlier that becomes non-significant once removed.
4. **Judge calibration**: The thresholds are tighter now—κ must stay below 0.65 and F1 below 0.75, whereas before they were κ=0.63 and F1=0.72.
5. **C5 failure modes**: Instead of type-specific signatures dissolving across various areas, I need to narrow this down to just 2-3 types with clearly defined patterns.
6. **Binary effect**: The previous 30.2pp effect now needs to fall within the 18-28pp range.
7. **C2 V**: The violation rate drops from 0.11 to somewhere between 0.06 and 0.10.

Now I'm setting up the YAML structure with the model lineup: GPT-5.4, GPT-4.1, Claude, Qwen3-235B, and DeepSeek-V3. The key insight is that Qwen3-235B and DeepSeek-V3 are both large capable models that behave similarly to the GPT variants, while Claude remains the distinct outlier driving the interaction pattern. I'm finalizing the per-model violation rates for the ambiguous condition across all types.

Generating violation rate table... Now I'm calculating the layer gaps for each model individually—the specialized versus linguistic performance spread varies quite a bit, with GPT-5.4 showing the largest gap at 9.3 percentage points favoring specialized tasks, while Claude actually reverses the pattern with a 5.3 point advantage for linguistic work. Now I'm calculating the per-model ambiguity averages across all six categories, then pooling them together to get an overall ambiguity rate for each model.

Looking at the pooled results, the binary difference comes in at 25.7 percentage points, which fits within the target range. For the McNemar odds ratio, I need to work from the discordant pairs—cases where one metric violates the threshold but the other doesn't. The imbalance between these pairs suggests an OR around 10.3, which edges slightly above the ideal [5, 10] range, so I'm reconsidering whether some of the unambiguous violations might overlap with ambiguous ones to bring that ratio down.

If I assume the unambiguous-only violations are quite rare—maybe 1-2% of cases—while ambiguous-only violations account for roughly 24%, that would push the OR to 16, which overshoots the target. Working backward from an OR of 7, I can see that configurations like 21% ambiguous-only with 3% unambiguous-only, or 28% with 4%, would hit that sweet spot while keeping the binary effect in the 18-24 percentage point range.

But there's a tension here: if the unambiguous violation rate is 8.2% and I'm trying to fit both the observed rates and the OR constraint, I need to solve for the joint violation rate that satisfies all three conditions simultaneously.

Setting up the equation where b and c are defined in terms of the joint violation rate x, I can solve for x algebraically. With OR = 7, this gives me x ≈ 3.9%, which means b = 30.0% and c = 4.3%. The binary effect of 25.7 percentage points checks out, and the McNemar OR of 7.0 falls within the target range.

Now I'm moving on to calculate Fleiss' kappa across the five models using their agreement patterns on the ambiguous episodes.  I'm setting κ = 0.22 to reflect weak agreement on specific clause-level violations, even though the overall binary effect is consistent. For the perturbation control, I'm planning 120 episodes initially across 30 pairs and 2 conditions with 2 API models, with a baseline violation rate around 7% and a perturbed rate around 21%, giving a difference of 14 percentage points.

Now I'm calculating the confidence interval for this effect. With 60 paired observations, the standard error is about 4.8 percentage points, which gives a 95% CI of [4.5, 23.5]—too wide since it exceeds the 15 percentage point threshold. Expanding to 180 episodes with 90 paired observations tightens the standard error to 3.9 percentage points, narrowing the CI to [6.3, 21.7], which is more acceptable.

Going further to 240 episodes with 120 pairs brings the standard error down to 3.4 percentage points and the CI to [7.3, 20.7] with a width of 13.4 percentage points—finally meeting the target. So I'll use the expanded 240-episode design.

Now I need to reconsider the discordant pair calculation more carefully. The proportion of discordant pairs depends on how many pairs show disagreement between the original and perturbed models, which I can derive from the baseline 7% and perturbed 21% violation rates.

If the joint violation rate is around 3%, then roughly 18% of pairs have the perturbed model violating while the original doesn't, 4% have the reverse, and 75% agree. This gives a discordant proportion of 22%, which inflates the standard error significantly. Even expanding to 120 pairs only gets the CI width to 16.8 percentage points—still wider than the 15-point target.

I'm settling on reasonable estimates instead: a 14 percentage point difference with a confidence interval around [5, 23], which is wide but shows the effect is real since it excludes zero. Scaling up to 240 episodes would tighten this to [7, 21]. For the ambiguity comparison, the 28 percentage point difference minus the 14 percentage point perturbation effect gives a net of 14 percentage points, or a ratio of 0.50. This puts me in a warning zone on the ratio criterion but conditional on the magnitude criterion, so the final assessment hinges on which one I weight more heavily.

I'm calling this "CONDITIONAL—borderline WARNING" since the net difference of 14 percentage points falls short of the 20 percentage point threshold needed for the strongest causal claim. But the paper can still work if I reframe the narrative away from "ambiguity-specific causation" toward "ambiguity as one significant factor among broader specification sensitivity issues." The 10 percentage point floor is still meaningful enough to support publication with this adjusted framing.

Now I'm pinning down the individual perturbation effects: synonym substitution causes about 10 percentage points of increase because policy language is precise, while clause reordering drives roughly 18 percentage points.

Actually, let me recalculate using just the three API models that were tested for perturbations—averaging GPT-4.5, GPT-4.1, and Claude gives me 24.9 percentage points for the ambiguity effect. That puts my net difference at 10.9 percentage points and the ratio at 0.56, which pushes into WARNING territory. I need to think through how the synonym and reordering split affects this verdict.

The data shows synonym perturbations causing a 10 percentage point shift while reordering causes an 18 percentage point shift—the reordering effect is particularly striking and suggests agents are genuinely sensitive to surface-level presentation like clause order and primacy bias, which is a significant finding for the worst-tier classification.

Now I'm ready to write out the YAML configuration, but I need to verify the exact model specifications from the plan descriptions. The models listed are qwen3-235b and deepseek-chat-v3 for one setup, gpt-5.4 and gpt-4.1 and claude-sonnet-4 for another, and I should check whether the reliability plan will test all five models or just the API subset.

Looking at the reliability test structure, it's designed for 30 representative clauses across 3 replicates and 2 conditions with 2 models, totaling 360 episodes. Since the local models aren't available in this API-only configuration, I'll stick with the 360-episode baseline using just the two API models for the core ICC calculation.

For the worst-tier reliability scenario with this 2-model setup, I'm considering why the ICC would drop from the observed 0.919 to something more conservative—factors like increased variance from API temperature sampling, quality issues in specific clause types like coreferential and auth_scope clauses, and the inherent noise from relying solely on API-based evaluation would all contribute to a lower but still respectable ICC around 0.72, with per-type variation ranging from 0.50 to 0.82. ), the ICC might still be decent for those 2 models. But if we conceptually think about what reliability means in the 5-model context, the between-model variance is the real issue.

Let me set:
- Within-2-model ICC (plan_006 as designed): 0.82 (good)
- Projected 5-model ICC (accounting for model heterogeneity): much lower
- The issue is that plan_006 only tests 2 GPT models which are highly correlated (ρ=0.94), so the reliability looks good within the GPT family but doesn't generalize

For worst tier, the plan_006 result of 0.82 is actually misleading because it only captures GPT-family reliability. The real reliability across all 5 models would be much lower.

So I need to be consistent with the Phase 1 worst tier definition, which specifies effect sizes and Cramér's V ranges rather than explicit ICC targets. For plan_006 as a 2-model reliability check, I should set the ICC in the moderate-to-good range (0.75-0.85) to reflect that the two GPT models perform consistently with each other, while acknowledging that this within-GPT reliability doesn't necessarily extend to the broader 5-model scenario. I'm realizing the same two GPT models would maintain high reliability since they're from the same family, but the real insight is the contrast—plan_006 shows good within-model ICC at 0.80, while plan_004 reveals poor cross-model agreement with Fleiss κ of 0.22 on ambiguous clauses, which itself demonstrates a worst-tier finding. Let me finalize the YAML with plan_006 ICC set to 0.80 and reconsider whether the clause reordering perturbation of 18 percentage points is realistic.

If reordering alone causes that much variance, it suggests agents are extremely sensitive to clause order, which would be a devastating finding that undermines the entire evaluation framework. I should calibrate these numbers more carefully within the Phase 1 range of 10-20 percentage points: synonym changes at 10pp, reordering at 18pp, and the pooled effect at 14pp as the midpoint.

The gap between synonym and reordering effects is itself significant—clause reordering is far more disruptive than synonym substitution, indicating strong positional biases in agent behavior. Now I'm calculating the omnibus chi-squared test for the ambiguous episodes using Cramér's V of 0.09 across 1500 total observations, which yields a test statistic well below the 0.05 threshold.

Actually, let me recalculate—with V=0.09 and N=1500, I'm getting χ² around 60.75, which is too significant. To land in the p [0.001, 0.05] range, I need to work backward from a target χ² of 15-20, which means V should be closer to 0.053. I need to figure out the degrees of freedom and chi-square statistic for testing whether the six type proportions differ significantly. With 1500 total ambiguous episodes and observed violation rates across the types, I'm calculating the chi-square goodness-of-fit test against the expected uniform distribution of about 33.9%.

Working through the calculation with 250 episodes per type, the chi-square value comes out to 10.56, which with 5 degrees of freedom gives a p-value around 0.061—just barely missing conventional significance at the 0.05 level.

Now I'm realizing the constraints might be incompatible: I need both a p-value between 0.001 and 0.05 AND a Cramér's V between 0.06 and 0.10, but with these sample sizes, achieving that V range would push the chi-square value too high. Let me recalculate what chi-square value would result from V = 0.08 across all 1500 episodes to see if the math actually works out. Now I'm testing different effect sizes to find where the p-value falls in that target range. V=0.09 gives p=0.033 and V=0.10 gives p=0.010, both within the [0.001, 0.05] window, while V=0.08 pushes above it at p=0.087.

The problem is that the specified V range of [0.06, 0.10] conflicts with the p-value requirement—lower values like V=0.06 and V=0.07 produce p-values well above 0.05, so only the upper end of the V range actually satisfies the statistical constraint. I need to decide how to resolve this inconsistency in the Phase 1 definition.

I'm settling on V=0.09 with p=0.033 as a workable compromise that fits both ranges. But now I'm reconsidering what N actually represents here—it should be the total number of ambiguous episodes across all models and clauses, which comes to 1500, and that's the right denominator for the type main effect chi-square calculation. Now I'm verifying whether my proposed violation rates actually produce a Cramér's V of 0.09 by computing the chi-square statistic directly from the observed counts per type against the pooled expected rate. Now I'm calculating the chi-squared contributions for each violation category, starting with the expected frequencies for both rows and then computing the individual chi-squared components for auth_scope and incomp violations.

Continuing through the remaining categories—CP, scopal, and lexical violations—to sum up all the chi-squared contributions and get the final test statistic. above 0.05, and V falls within the acceptable range of 0.06 to 0.10. To get the p-value below the significance threshold, I need to increase the variation slightly. Let me try bumping incomp up to 42% and dropping coref to 26%, then recalculating the chi-square statistic with the new violation counts and expected frequencies. Now I'm summing those chi-squared components to get 15.12, which gives me a p-value of 0.010 with 5 degrees of freedom—right in the target range. The Cramér's V comes out to 0.100, sitting at the upper boundary of where I want it. Let me adjust the violation rates slightly to push V down while keeping the p-value significant.

I'm recalculating the chi-squared contributions across each category, with the incomp and coref categories showing the largest deviations from expected values, and the total coming to 13.

059. With 5 degrees of freedom, this gives me a p-value around 0.023 and Cramér's V of 0.093, both indicating a small but statistically significant effect. These adjusted pooled rates show incompleteness is notably higher than coreferential errors by about 14 percentage points.

Now I'm breaking this down by layer—the specification layer averages 36.1% while the linguistic layer averages 31.6%, a gap of 4.5 percentage points that fits within acceptable bounds. I'm going to simplify and use V=0.09 and p=0.025 as my working values, then reconstruct the per-model rates to average back to these final pooled estimates. Now I'm finishing the pooled averages and calculating the per-model means across all six metrics to see how each model performs overall.

Looking at the binary effects, I'm subtracting the unambiguous rates from each model's average to get the performance gap, then checking that the aggregate numbers across all five models align correctly.

Now I'm examining the per-model layer gaps by calculating averages across the specification, linguistic, and incompleteness dimensions for each model, then finding the difference between their spec and linguistic performance to see where each one's strengths and weaknesses lie.

The pooled gap across all models comes to 4.4 percentage points, which is right at the boundary of my target range, so I'm adjusting DeepSeek's specification rates downward to bring the overall pooled gap down slightly and ensure it stays within bounds. Now I'm calculating the DeepSeek layer breakdown and pooling the gaps across all models, which gives me a consistent 3.8 percentage point difference. For the second key finding, I'm estimating the effect size and p-value from the incompleteness-coreference range, landing around V≈0.09 and p≈0.025. I think I have enough precision here—the main takeaway is that the binary effect hovers around 25.7 percentage points across all models and task types, while the second effect shows a moderate association that's statistically significant.

Looking at the remaining findings: the layer gap sits at roughly 3.8 percentage points but isn't statistically significant, the interaction effect appears driven by an outlier that disappears when I exclude Claude, the perturbation analysis suggests a conditional verdict around 14 percentage points, the judge agreement metrics are reasonable at κ≈0.58 and F1≈0.68, and awareness is tracking at about 14% with surface adoption near 78%. I should finalize these numbers in the YAML output now rather than continuing to refine them. One last check on the equivalence margins: with V=0.09, type pairs should be roughly equivalent within ±15 percentage points but diverge beyond ±10 percentage points. the C4 interaction might be driven by Claude being an outlier. Let me check what happens if I remove Claude and recalculate the rankings across the other four models—the patterns look fairly consistent, with incomp and auth dominating across most of them, though Qwen3 starts to diverge a bit lower in the rankings.

When I run the analysis without Claude, the model×type interaction drops to non-significant, whereas with Claude included it's significant at p≈0.02. This confirms Claude is the key driver of that interaction effect. The narrative implication is interesting though—C4 was supposed to reveal safety training mechanisms through the interaction, but it seems Claude's distinct profile is what's creating that signal rather than a genuine interaction pattern across the models.

The broader claim about how safety training shapes vulnerability profiles becomes much weaker when it's really just one model standing out from the others. I need to reframe this from "models show systematically different vulnerability profiles" to "Claude differs from other models, likely due to RLHF, but this is a single-model observation rather than a generalizable finding about safety training approaches."

Now I'm ready to write the YAML output with this more cautious narrative guidance.

Writing experiment plan structure... Writing YAML config...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "706e5f85-a754-4a8d-a06e-d2d78d934352",
  "isSidechain": false,
  "requestId": "req_011CbF6s8KZCiSwmLciCtJsE",
  "type": "assistant",
  "uuid": "61d9f282-7501-4655-a93e-2bed077f0598",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012iFU5VU532jS3E4vpfDxAK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37923,
      "cache_read_input_tokens": 61773,
      "output_tokens": 34529,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 37923,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 34529,
          "cache_read_input_tokens": 61773,
          "cache_creation_input_tokens": 37923,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 37923
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

_source line 34 · 2026-05-21T04:54:32.767Z_

Now I have all context. Let me generate the comprehensive worst-tier imagined experiments based on the updated Phase 1 definition.

```yaml
tier: worst
narrative_guidance: >
  C3 layer effect 完全不成立 (pooled p>0.10)，C4 interaction 虽 omnibus 显著但由 Claude
  单一 outlier 驱动（移除后 p>0.20），perturbation control 暴露 14pp confound (verdict
  CONDITIONAL, ratio=0.56, borderline WARNING)，judge calibration κ=0.58 / F1=0.68
  整体偏低且 type-specific bias 严重。需根本性 reframe：放弃 'Differential Nocuity' 和
  layer hierarchy，围绕 C1 (universal nocuity, 即使有 perturbation caveat 仍 Δ_net≥10pp)
  + C2 (6-type taxonomy 作为 diagnostic tool, 非 severity ranking) + C5 (Ambiguity
  Blindness, 14% awareness / 78% surface adoption) 构建叙事。Title 改为 'Policy Ambiguity
  Is Universally Nocuous for LLM Agents: A Causal Study with Type-Level Taxonomy'。
  核心叙事转向：ambiguity 不是唯一 sensitivity factor (perturbation 也造成 14pp increase)，
  但仍是最大的单一 factor (Δ_net≈12pp 且 type-structured)；taxonomy 的价值从 severity
  prediction 转为 diagnostic vocabulary (帮助识别和描述 failure 而非 rank risk)；
  Ambiguity Blindness 从 secondary 升为 co-primary 贡献 (universal across all 5 models,
  所有 types)。仍冲 EMNLP，taxonomy framework + causal design (with caveat) + Blindness
  empirical finding = solid 3-contribution paper，但 novelty claim 弱于 best/median。

imagined_experiments:
  - name: full_study_clause_generation
    plan_id: plan_001
    description: >
      生成 140 新 clause pairs (coreferential 50, auth_scope 50, lexical +20,
      incompleteness +20)，补全 6 types × 50 pairs = 300 对。混合 CP 格式
      (labeled + unlabeled)。Chantree-style 质量验证。
    expected_results:
      total_pairs: 300
      pairs_per_type: 50
      cp_labeled_ratio: 0.5
      quality_pass_rate: 0.91
      avg_token_delta_amb_vs_unamb: 3.9
      coreferential_revision_rounds: 3
      auth_scope_revision_rounds: 2
      per_type_quality:
        auth_scope_pass_rate: 0.90
        incompleteness_pass_rate: 0.94
        conditional_polysemy_pass_rate: 0.96
        scopal_pass_rate: 0.95
        lexical_pass_rate: 0.93
        coreferential_pass_rate: 0.86
    result_rationale: >
      Clause 生成阶段本身不受 worst tier 影响——是数据准备而非结果观测。但
      quality_pass_rate 91% 而非 >95% 预示后续 measurement problems：
      (a) Coreferential pass_rate 最低 (0.86) 因 RC attachment 与 scopal 边界
      重叠 (RC8 concerns)，2/5 pilot clauses 触发 conservative_refusal 而非
      violation，需 3 轮修订仍有残余质量问题；(b) Auth_scope 0.90 因与
      incompleteness 的 operational distinction 要求精细控制 (RC9)，部分 clause
      的 "ambiguous permission boundary" 与 "missing permission specification"
      难以 cleanly separate；(c) token delta spec-layer (3.9) > ling-layer (1.6)
      是 potential confound——spec-layer 的 disambiguation 系统性需要更多 tokens，
      这不是 clause 质量问题而是 inherent asymmetry，但在 worst tier 下被
      reviewer 质疑为 information asymmetry confound。这些 clause 层面的质量差异
      在后续 judge calibration (plan_009) 中以 type-specific F1 下降的形式放大。
    tables:
      - name: Clause Pair Statistics by Type
        columns: [type, n_pairs, avg_amb_tokens, avg_unamb_tokens, token_delta, quality_pass_rate]
        rows:
          - [auth_scope, 50, 28.3, 32.2, 3.9, 0.90]
          - [incompleteness, 50, 26.8, 30.6, 3.8, 0.94]
          - [conditional_polysemy, 50, 24.1, 25.7, 1.6, 0.96]
          - [scopal, 50, 22.6, 24.0, 1.4, 0.95]
          - [lexical, 50, 21.9, 23.2, 1.3, 0.93]
          - [coreferential, 50, 25.2, 27.5, 2.3, 0.86]
    figures_description:
      - "Token delta distribution per type (box plot): spec-layer types 系统性更长"
    analysis: >
      Coreferential 低 pass_rate (0.86) 是 worst tier 的早期信号——该 type 的
      clause design 困难度高于预期，直接传导至 plan_009 judge calibration 中
      coreferential F1 最低 (0.62)。Token delta 的 layer asymmetry (spec 3.9
      vs ling 1.6) 在 plan_004 中被 report 为 control variable，partial
      correlation 后不构成 independent confound，但 reviewer 会 flag。

  - name: new_type_mini_pilot
    plan_id: plan_001b
    description: >
      Coreferential + auth_scope 各 5 clauses × 2 conditions × 1 model
      (gpt-5.4) = 20 episodes。验证新类型基本可行性。
    expected_results:
      coreferential_amb_violation_rate: 0.40
      coreferential_unamb_violation_rate: 0.00
      auth_scope_amb_violation_rate: 0.60
      auth_scope_unamb_violation_rate: 0.00
      coreferential_binary_effect_pp: 40
      auth_scope_binary_effect_pp: 60
      systematic_issues_found: true
      issues_detail: >
        2/5 coreferential clauses 触发 conservative refusal 而非 violation;
        1/5 auth_scope unambiguous 版本仍残余歧义 (需收紧)
    result_rationale: >
      Mini-pilot 在 gpt-5.4 上给出 "go" 信号——两个新 type 均触发 violations，
      control < 15%。但这是 worst tier 的隐患起点：(a) gpt-5.4 的 auth_scope 60%
      看似 confirm spec-layer 危险性高，但 N=5 的 CI 极宽 (±30pp)，同一 clause
      在 Claude 上只有 ~16%——mini-pilot 单一模型验证无法预见 C4 的 Claude outlier
      问题；(b) coreferential 2/5 conservative refusal 预示该 type 行为异质性高，
      但被归为 "fixable clause quality issue" 而非 structural warning——实际上
      这种行为异质性在 5-model 扩展后导致 coreferential 的 ICC (plan_006) 和
      judge F1 (plan_009) 都是所有 type 中最差的；(c) gpt-5.4 上 auth_scope 60%
      / coreferential 40% 展现的 spec > ling gap 是 GPT-family 特征，不具
      cross-model universality。
    tables:
      - name: Mini-Pilot Results
        columns: [type, condition, n, violations, rate]
        rows:
          - [coreferential, ambiguous, 5, 2, "40%"]
          - [coreferential, unambiguous, 5, 0, "0%"]
          - [auth_scope, ambiguous, 5, 3, "60%"]
          - [auth_scope, unambiguous, 5, 0, "0%"]
    figures_description: []
    analysis: >
      Mini-pilot 的 "go" 信号在 worst tier 下是 misleading confidence。
      gpt-5.4 单模型验证对 multi-model study 的预测力有限——尤其无法预见
      Claude 的 auth_scope 反转 (16%) 和 perturbation control 的 CONDITIONAL
      verdict。理想做法是 ≥2 model families 的 mini-pilot。

  - name: perturbation_control
    plan_id: plan_010
    description: >
      30 non-ambiguity perturbation pairs (15 synonym substitution + 15 clause
      reordering) × 2 conditions × 2 API models (gpt-5.4, gpt-4.1) = 120
      episodes。验证 ambiguity-specific 因果性。因 CI 过宽追加 Claude 60
      episodes = 180 total。
    expected_results:
      total_episodes_initial: 120
      total_episodes_expanded: 180
      baseline_violation_rate: 0.067
      perturbation_pooled_violation_rate: 0.207
      perturbation_delta_pp: 14.0
      perturbation_ci_initial: "[3.8, 24.2]"
      perturbation_ci_expanded: "[6.5, 21.5]"
      perturbation_ci_width_expanded: 15.0
      ambiguity_delta_pp_same_models: 28.5
      ambiguity_ci: "[22.8, 34.2]"
      net_delta_pp: 14.5
      ratio: 0.49
      verdict: "CONDITIONAL (borderline WARNING)"
      synonym_substitution_delta_pp: 10.0
      synonym_ci: "[1.2, 18.8]"
      clause_reordering_delta_pp: 18.0
      clause_reordering_ci: "[8.5, 27.5]"
      per_model_perturbation:
        gpt54_delta_pp: 16
        gpt41_delta_pp: 14
        claude_delta_pp: 12
    result_rationale: >
      Perturbation control 是 worst tier 最具破坏力的结果——暴露 policy specification
      对 surface-level 变化的广泛敏感性：

      (a) Synonym substitution Δ=10pp: 更换政策术语同义词 (e.g., "refund" →
      "reimbursement", "authorize" → "permit") 导致 10pp violation increase。
      原因是 LLM agent 对政策术语有 lexical anchoring——training data 中特定
      词汇与特定 safety behavior 关联。更换同义词打断了这种关联，agent 对
      "reimbursement" 的 safety constraint 弱于 "refund"。这不是 ambiguity，
      而是 terminological brittleness——但足以削弱 "only ambiguity matters" claim。

      (b) Clause reordering Δ=18pp: 调整条件/例外的排列顺序（不改变语义）
      导致 18pp violation increase。这是更严重的发现：agent 有强 primacy bias
      ——排在前面的条件被优先处理，后面的 exceptions/limitations 被忽略。
      Policy 写 "allow X. Exception: not for Y" vs "for Y, X is not allowed.
      Otherwise allow X" 在逻辑上等价但 agent 行为差异巨大。Reordering effect
      (18pp) 接近 ambiguity effect 的 63%。

      (c) Ratio=0.49: 非歧义 perturbation 造成的 violation increase 占 ambiguity
      effect 的近一半。按 5-档判定标准：Δ_perturb=14pp (CONDITIONAL range: 10-15pp)
      但 ratio=0.49 (WARNING range: 0.45-0.60)。综合判定 CONDITIONAL，borderline
      WARNING。

      (d) CONDITIONAL 要求 Δ_net > 20pp 才可发表 C1 因果 claim 最强形式。
      实际 Δ_net=14.5pp < 20pp threshold。C1 不能声称 "ambiguity-specific
      causation"，只能说 "ambiguity as a significant contributor among
      specification sensitivity factors, causing additional violations
      beyond general prompt brittleness"。

      (e) 这改变了整篇论文的 causal framing。从 "ambiguity causes violations"
      降为 "specification sensitivity is broad (14pp from surface changes alone),
      and ambiguity is the largest single contributor (+14.5pp net above
      perturbation baseline), but not the sole factor"。实际上发现了一个
      更一般的现象：LLM agents 对 policy specification 的任何 variation
      都高度敏感，ambiguity 是其中最危险的一种。
    tables:
      - name: Perturbation Control Results (Expanded, 180 episodes)
        columns: [condition, violation_rate, "Δpp_vs_baseline", "95% CI"]
        rows:
          - [unambiguous_baseline, "6.7%", "—", "—"]
          - [synonym_substitution, "16.7%", "+10.0pp", "[1.2, 18.8]"]
          - [clause_reordering, "24.7%", "+18.0pp", "[8.5, 27.5]"]
          - [perturbation_pooled, "20.7%", "+14.0pp", "[6.5, 21.5]"]
          - [ambiguous, "35.2%", "+28.5pp", "[22.8, 34.2]"]
      - name: Perturbation Verdict Summary
        columns: [metric, value, threshold, verdict]
        rows:
          - [Δ_perturb, "14.0pp", "< 5pp PASS / 10-15pp CONDITIONAL", "CONDITIONAL"]
          - [ratio, "0.49", "< 0.15 PASS / 0.45-0.60 WARNING", "WARNING"]
          - [CI_contains_0, "no", "required for PASS", "✗ FAIL"]
          - [Δ_net, "14.5pp", "> 20pp for CONDITIONAL", "✗ below threshold"]
          - [CI_width, "15.0pp", "< 15pp", "✗ marginal (needs more data)"]
          - [composite_verdict, "CONDITIONAL (borderline WARNING)", "—", "—"]
      - name: Per-Model Perturbation Effect
        columns: [model, baseline_rate, perturbed_rate, Δpp]
        rows:
          - [gpt-5.4, "5.0%", "21.0%", "+16.0pp"]
          - [gpt-4.1, "6.0%", "20.0%", "+14.0pp"]
          - [claude-sonnet-4-6, "9.0%", "21.0%", "+12.0pp"]
    figures_description:
      - >
        三条件 bar chart (baseline / perturbation / ambiguous) + CI error bars：
        perturbation bar 显著高于 baseline，ambiguous 高于 perturbation 但
        gap 大幅压缩——视觉上 perturbation 条已不可忽略
      - >
        Synonym vs reorder scatter: reorder Δ (18pp) >> synonym Δ (10pp)，
        显示 positional sensitivity 比 lexical sensitivity 更危险
    analysis: >
      Perturbation control CONDITIONAL/WARNING 是 worst tier 的 defining result。
      它将论文从 "clean causal story" 变为 "ambiguity as one factor among many"。
      但 silver lining 存在：(a) Δ_net=14.5pp 仍 > 10pp，ambiguity 仍是最大单一
      contributor；(b) synonym vs reorder 的异质性 (10pp vs 18pp) 本身是
      interesting finding——可在 Discussion 中展开为 "specification sensitivity
      spectrum" 概念；(c) 如果 reframe 成功，perturbation control 从 "threat
      to causal claim" 变为 "additional finding about specification brittleness"，
      实际增加了 paper 的 scope。但代价是 causal narrative 弱化。

  - name: full_study_api
    plan_id: plan_002
    description: >
      300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1,
      claude-sonnet-4-6) = 1,800 episodes。Cross-judge evaluation。
    expected_results:
      total_episodes: 1800
      gpt54_rates:
        auth_scope: 0.42
        incompleteness: 0.48
        cp: 0.30
        scopal: 0.38
        lexical: 0.34
        coreferential: 0.20
      gpt41_rates:
        auth_scope: 0.38
        incompleteness: 0.44
        cp: 0.30
        scopal: 0.36
        lexical: 0.32
        coreferential: 0.22
      claude_rates:
        auth_scope: 0.16
        incompleteness: 0.24
        cp: 0.30
        scopal: 0.28
        lexical: 0.26
        coreferential: 0.32
      gpt54_binary_effect_pp: 30.3
      gpt41_binary_effect_pp: 27.7
      claude_binary_effect_pp: 18.0
      gpt54_unamb_rate: 0.05
      gpt41_unamb_rate: 0.06
      claude_unamb_rate: 0.08
      gpt54_layer_gap_pp: 9.3
      gpt41_layer_gap_pp: 7.3
      claude_layer_gap_pp: -5.3
      binary_effect_3api_pp: 25.3
      layer_gap_3api_pp: 3.8
      cramers_v_3api: 0.11
      model_main_effect_p_3api: 0.008
      model_type_interaction_p_3api: 0.012
      avg_unamb_rate_3api: 0.063
    result_rationale: >
      GPT 系 (gpt-5.4, gpt-4.1) 展示 consistent spec > ling pattern (gap +9.3pp
      和 +7.3pp)，两模型 type rank correlation ρ=0.94。但 binary effect 从
      actual 数据的 +38pp/+35pp 缩水至 +30pp/+28pp——原因是 worst tier 假设
      下部分 clause pairs 的 unambiguous variant 也引起 violations (baseline
      rate 5-6% 而非 <3%)，压缩了 net effect。

      Claude 展现截然不同的 vulnerability profile，是 worst tier C4 问题的根源：
      (a) auth_scope 仅 16% (GPT-5.4 42% 的 38%)——Claude RLHF 训练强化了
      "不确定时 refuse" 的行为，specification-layer ambiguity 更多触发 refusal
      而非 violation。这不是 "更安全" 而是 "不同 failure mode"：Claude refuse
      的 episode 中约 40% 在 human ground truth 下应该 proceed (false refusal)；
      (b) coreferential 高达 32% (GPT 系 20-22% 的 1.5 倍)——RC attachment
      歧义不触发 Claude 的 safety refusal mechanism，Claude 在 referential
      ambiguity 上 "放松警惕"，倾向 wider-scope interpretation；
      (c) 结果: Claude layer gap 反转 (-5.3pp, ling > spec)。

      3-API pooled binary effect 25.3pp (Claude 拉低)。Layer gap 仅 3.8pp
      (Claude 反转 offset GPT positive gap)。Model×type interaction 已显著
      (p=0.012)——尚未加入 open-source 模型就已可见 type ranking 非 universal。
      但此处 interaction 完全由 Claude 驱动：移除 Claude 后 GPT-5.4 vs GPT-4.1
      的 interaction p=0.87 (两个 GPT 模型 profile 近乎 identical)。
    tables:
      - name: Per-Model Per-Type Violation Rates (Ambiguous Condition, 3 API)
        columns: [type, layer, gpt-5.4, gpt-4.1, claude-sonnet-4-6, 3-API_pooled]
        rows:
          - [auth_scope, spec, "42%", "38%", "16%", "32.0%"]
          - [incompleteness, spec, "48%", "44%", "24%", "38.7%"]
          - [cond_polysemy, spec, "30%", "30%", "30%", "30.0%"]
          - [scopal, ling, "38%", "36%", "28%", "34.0%"]
          - [lexical, ling, "34%", "32%", "26%", "30.7%"]
          - [coreferential, ling, "20%", "22%", "32%", "24.7%"]
          - [spec_avg, "—", "40.0%", "37.3%", "23.3%", "33.6%"]
          - [ling_avg, "—", "30.7%", "30.0%", "28.7%", "29.8%"]
          - [layer_gap, "—", "+9.3pp", "+7.3pp", "-5.3pp", "+3.8pp"]
      - name: Binary Effect by API Model
        columns: [model, amb_rate, unamb_rate, "Δpp", McNemar_OR, p]
        rows:
          - [gpt-5.4, "35.3%", "5.0%", "+30.3pp", 12.8, "<0.0001"]
          - [gpt-4.1, "33.7%", "6.0%", "+27.7pp", 9.6, "<0.0001"]
          - [claude-sonnet-4-6, "26.0%", "8.0%", "+18.0pp", 5.2, "<0.0001"]
          - [3-API_pooled, "31.7%", "6.3%", "+25.3pp", 8.7, "<0.0001"]
    figures_description:
      - >
        3×6 heatmap: Claude auth_scope/incomp 显著低 (冷色), coreferential
        显著高 (暖色)——与 GPT 系形成对角反转
    analysis: >
      3-API 结果已暴露 worst tier 的核心问题：Claude 的 outlier profile
      使 type ranking 和 layer hierarchy 都不 universal。但 binary effect
      对所有 3 个模型均显著 (p<0.0001)——"所有 ambiguity 都 nocuous" 不受影响。
      Plan_003 加入 open-source 模型后，如果它们的 profile 类似 GPT (而非
      Claude)，interaction 的 "Claude outlier" 性质将更加清晰。

  - name: full_study_opensource
    plan_id: plan_003
    description: >
      300 clauses × 2 conditions × 2 open-source models via OpenRouter API:
      qwen/qwen3-235b-a22b (235B MoE) + deepseek/deepseek-chat-v3-0324
      = 1,200 episodes。Cross-judge uses API models.
    expected_results:
      total_episodes: 1200
      qwen3_235b_rates:
        auth_scope: 0.38
        incompleteness: 0.44
        cp: 0.34
        scopal: 0.38
        lexical: 0.36
        coreferential: 0.28
      qwen3_235b_binary_effect_pp: 26.3
      qwen3_235b_unamb_rate: 0.10
      qwen3_235b_amb_avg: 0.363
      qwen3_235b_layer_gap_pp: 4.7
      deepseek_rates:
        auth_scope: 0.40
        incompleteness: 0.44
        cp: 0.34
        scopal: 0.38
        lexical: 0.38
        coreferential: 0.33
      deepseek_binary_effect_pp: 25.8
      deepseek_unamb_rate: 0.12
      deepseek_amb_avg: 0.378
      deepseek_layer_gap_pp: 3.0
      binary_effect_2os_pp: 26.1
      layer_gap_2os_pp: 3.9
    result_rationale: >
      Qwen3-235B 和 DeepSeek-V3 的 profile 与 GPT 系高度相似——这是 worst
      tier 的关键转折。与 old worst tier 假设的 Qwen3-8B (reversed layer gap,
      coreferential dominant) 截然不同：

      (a) Qwen3-235B (22B active MoE): type ranking = incomp > auth ≈ scop >
      lex > CP > coref，与 GPT 系 ρ=0.89 (strong)。235B MoE 的 pragmatic
      reasoning 能力接近 frontier dense models——能 "推断" implicit permission
      boundaries 并据此行动 (auth_scope 38%)，同时对 referential ambiguity
      有一定 disambiguation 能力 (coreferential 28%)。Layer gap +4.7pp
      (正向但modest)，介于 GPT (+7-9pp) 和 Claude (-5pp) 之间。Unamb rate
      10% 高于 GPT 5-6%——open-source safety training 的 baseline 保护较弱，
      即使无歧义也有更多 violations。这压缩了 binary effect 至 26.3pp。

      (b) DeepSeek-V3: type ranking = incomp > auth ≈ scop ≈ lex > CP > coref，
      与 GPT 系 ρ=0.83。DeepSeek 展现 "uniformly elevated" pattern——所有
      type 的 violation rate 都偏高 (33-44%)，type 间差异被 floor effect
      压缩 (range 仅 11pp vs GPT-5.4 的 28pp)。Per-type χ²(5)=4.8, p=0.44,
      n.s.——DeepSeek 对所有 ambiguity types 几乎 equally vulnerable，无
      type-specific pattern。Unamb rate 12% 进一步证实 safety training
      弱。Layer gap +3.0pp (negligible)。

      (c) 关键后果：两个 open-source 模型的 type profile 均与 GPT 系 similar
      (而非 reversed 或 distinct)，意味着 5-model 中只有 Claude 是真正的
      outlier。C4 interaction 的 "model × type" 故事变为 "Claude vs
      everyone else"——无法支撑 "safety training differentially addresses
      specific ambiguity types" 的一般性理论 claim，只能说 "Claude
      (specifically, Anthropic's RLHF approach) shows a distinct
      vulnerability profile, particularly resistant to auth_scope and
      vulnerable to coreferential"。

      (d) DeepSeek 的 high unamb rate (12%) 对 perturbation control 结论
      有 corroborative implication：如果 agent 即使在 unambiguous 条件下
      也有 12% 违规率，说明 policy specification 的 general sensitivity
      是普遍问题，支撑 perturbation control 发现的 "specification
      brittleness" 解读。
    tables:
      - name: Per-Model Per-Type Violation Rates (Open-Source, Ambiguous)
        columns: [type, layer, Qwen3-235B, DeepSeek-V3, 2-OS_pooled]
        rows:
          - [auth_scope, spec, "38%", "40%", "39.0%"]
          - [incompleteness, spec, "44%", "44%", "44.0%"]
          - [cond_polysemy, spec, "34%", "34%", "34.0%"]
          - [scopal, ling, "38%", "38%", "38.0%"]
          - [lexical, ling, "36%", "38%", "37.0%"]
          - [coreferential, ling, "28%", "33%", "30.5%"]
          - [spec_avg, "—", "38.7%", "39.3%", "39.0%"]
          - [ling_avg, "—", "34.0%", "36.3%", "35.2%"]
          - [layer_gap, "—", "+4.7pp", "+3.0pp", "+3.8pp"]
      - name: Binary Effect by Open-Source Model
        columns: [model, amb_rate, unamb_rate, "Δpp", McNemar_OR, p]
        rows:
          - [Qwen3-235B, "36.3%", "10.0%", "+26.3pp", 6.8, "<0.0001"]
          - [DeepSeek-V3, "37.8%", "12.0%", "+25.8pp", 5.4, "<0.0001"]
      - name: Cross-Model Type Rank Correlation (Spearman ρ vs GPT-5.4)
        columns: [model, rho, interpretation]
        rows:
          - [GPT-4.1, 0.94, "near-identical profile"]
          - [Qwen3-235B, 0.89, "highly similar"]
          - [DeepSeek-V3, 0.83, "similar (uniformly elevated)"]
          - [Claude, 0.14, "near-zero — qualitatively different"]
    figures_description:
      - >
        Radar chart 5 models × 6 types: 4 models (GPT-5.4, GPT-4.1, Qwen3,
        DeepSeek) 的 radar shape 高度重叠，Claude 是明显 outlier——visual
        proof that interaction is Claude-driven
      - >
        Type rank parallel coordinates: 4 条线近乎平行 (same ranking),
        Claude 线交叉所有其他线——直观显示 "1 vs 4" pattern
    analysis: >
      Open-source 模型的加入确认了 worst tier 的 C4 diagnosis：interaction 是
      "Claude outlier" 而非 "diverse safety training mechanisms"。4/5 模型
      的 type profile ρ>0.83，只有 Claude ρ=0.14。理论 implication 从
      "safety training creates type-specific vulnerabilities" 弱化为
      "Anthropic's specific RLHF implementation has a distinct effect
      on auth_scope/coreferential, but this is a single data point, not
      a generalizable mechanism"。

  - name: full_study_analysis
    plan_id: plan_004
    description: >
      2,997 episodes (5 models × ~300 clauses × 2 conditions) 统计分析：
      C1 binary effect, C2 type hierarchy, C3 layer effect, C4 model×type
      interaction, TOST, power analysis, inter-model agreement, info delta。
    expected_results:
      total_episodes: 2997
      binary_effect_5model_pp: 25.7
      binary_effect_5model_ci: "[23.1, 28.3]"
      mcnemar_or_5model: 7.2
      mcnemar_or_ci: "[5.1, 10.2]"
      mcnemar_p: "<0.0001"
      per_model_binary_effects:
        gpt54: "+30.3pp"
        gpt41: "+27.7pp"
        claude: "+18.0pp"
        qwen3_235b: "+26.3pp"
        deepseek: "+25.8pp"
      per_type_all_significant: true
      weakest_type_effect: "coreferential +18.8pp (Claude高+GPT低 → pooled下降)"
      omnibus_chi2_5model: 12.2
      omnibus_p_5model: 0.032
      cramers_v_5model: 0.090
      actual_power_c2: 0.72
      mde_c2_v: 0.11
      pooled_rates_ambiguous:
        auth_scope: "34.8%"
        incompleteness: "40.8%"
        conditional_polysemy: "31.6%"
        scopal: "35.6%"
        lexical: "33.2%"
        coreferential: "27.0%"
      incomp_minus_coref_pp: 13.8
      tost_15pp_equivalent_pairs: "10/15"
      tost_10pp_equivalent_pairs: "4/15"
      spec_avg_5model: "35.7%"
      ling_avg_5model: "31.9%"
      layer_gap_5model_pp: 3.8
      layer_gap_ci: "[-1.5, 9.1]"
      layer_gap_p: 0.22
      within_judge_1_layer_p: 0.31
      within_judge_2_layer_p: 0.18
      model_main_effect_chi2: 22.8
      model_main_effect_p: 0.0001
      model_main_effect_v: 0.087
      model_type_interaction_chi2: 36.4
      model_type_interaction_p: 0.014
      model_type_interaction_v: 0.078
      interaction_without_claude_p: 0.23
      interaction_without_claude_note: "移除 Claude 后 4-model interaction n.s."
      logistic_regression:
        condition_amb_coef: 1.62
        condition_amb_z: 14.3
        condition_amb_p: "<0.001"
        model_main_sig: true
        type_main_sig: true
        model_x_type_sig: true
        model_x_type_without_claude_sig: false
        token_delta_coef: 0.018
        token_delta_z: 2.31
        token_delta_p: 0.021
      fleiss_kappa_ambiguous: 0.22
      fleiss_kappa_unambiguous: 0.78
      same_interpretation_pct_ambiguous: 0.52
      different_interpretation_pct_ambiguous: 0.48
      auth_scope_range_pp: 26
      incomp_range_pp: 24
      per_model_type_chi2:
        gpt54: {chi2: 15.8, p: 0.007, V: 0.23}
        gpt41: {chi2: 10.2, p: 0.069, V: 0.18}
        claude: {chi2: 6.4, p: 0.27, V: 0.15}
        qwen3_235b: {chi2: 5.1, p: 0.40, V: 0.13}
        deepseek: {chi2: 4.8, p: 0.44, V: 0.12}
      avg_token_delta_spec: 3.5
      avg_token_delta_ling: 1.6
      token_delta_partial_r_after_type: 0.11
    result_rationale: >
      C1 (binary effect +25.7pp, CI [23.1, 28.3], OR=7.2):
      从 actual 数据的 +34.0pp/OR=15.1 大幅缩水。三重原因叠加：
      (i) Claude binary effect 仅 +18.0pp (最低)——RLHF 的 blanket conservatism
      提高了 unamb baseline (8%) 同时压低了 amb rate (26%)；
      (ii) open-source 模型的 high unamb rates (10-12%) 压缩 effect size——
      DeepSeek 即使无歧义也有 12% violation rate，说明 safety training 整体
      较弱而非 ambiguity-specific 问题；
      (iii) 部分 clause pairs 的 unambiguous variant 未能完全消除歧义
      (plan_001 quality issues 传导)。但 CI 远离零, p<0.0001，6 types all
      significant (最弱 coreferential +18.8pp)——"all ambiguity is nocuous"
      成立。结合 perturbation control (Δ_net≈12pp): 即使扣除 perturbation
      baseline，ambiguity 仍造成 significant additional violations。

      C2 (V=0.090, p=0.032):
      Omnibus χ² 勉强显著——types 不完全等价，但效应极弱。V=0.090 远低于
      小效应阈值 0.10。Power=0.72——稍 underpowered，MDE=0.11 > observed
      0.090，说明需要 更大样本才能 reliably detect 这种 level 的 type effect。
      TOST: ±15pp 有 10/15 pairs equivalent——大部分 type pairs 在操作上
      不可区分。仅 incomp vs coref (13.8pp gap) 和 incomp vs CP/lexical
      是 non-equivalent。±10pp 仅 4/15 equivalent——但 ±10pp 是 stringent
      margin。实际 type hierarchy 被压缩为 "incompleteness > rest ≈ equal
      > coreferential" 的弱 2-tier (而非原预期的 3-tier)。V<0.10 意味着
      type 分类对 violation severity 的 predictive value 极有限。

      C3 (layer gap 3.8pp, p=0.22, n.s.):
      Layer gap 不显著。CI [-1.5, 9.1] 包含 0。GPT 的 positive gap (+7-9pp)
      被 Claude (-5.3pp) 抵消，open-source models 的 small positive gap
      (+3-5pp) 不足以补偿。Within-judge analysis 更糟：两个 judge group 均
      n.s. (p=0.31 和 0.18)——即使控制 judge variance 也无法恢复 layer effect。
      Layer hierarchy 作为 paper claim 完全不成立。"Disambiguation Channel
      Framework" 缺乏 empirical support，应降为 Discussion 中的 "potential
      explanatory framework" 而非 tested theory。

      C4 (interaction omnibus p=0.014, but Claude-driven):
      5-model omnibus interaction 显著——type ranking 确实 model-dependent。
      但移除 Claude 后 4-model interaction p=0.23 (n.s.)。这意味着
      interaction 完全由 Claude outlier 驱动，不是 5 个模型之间的 systematic
      差异。Per-model per-type χ²: 只有 GPT-5.4 有显著的 within-model
      type differentiation (p=0.007)，其他 4 个模型均 n.s. (p>0.05)——
      说明大部分模型对不同 ambiguity types 的 vulnerability 差异不大，
      只有 GPT-5.4 展现 clear type-specific pattern。

      Fleiss κ=0.22 (poor): 5 models 在 which-clauses-violate 的层面
      agreement 极低。这不是 Berry & Kamsties 的 "divergent nocuity"
      (different readings)，而是 stochastic disagreement——models 在
      borderline cases 的行为不稳定。只有 52% 的 ambiguous clauses 产生
      all-5-models-same-outcome——near chance for binary outcome。

      Info delta: spec 3.5 vs ling 1.6 tokens。partial r=0.11 (n.s.)
      after type control. Token delta 不是 independent confound, 但
      reviewer 会 flag.
    tables:
      - name: 5-Model Pooled Per-Type Results (Ambiguous)
        columns: [type, layer, amb_rate, unamb_rate, "Δpp", "95% CI", McNemar_p]
        rows:
          - [auth_scope, spec, "34.8%", "5.6%", "+29.2pp", "[23.4, 35.0]", "<0.0001"]
          - [incompleteness, spec, "40.8%", "5.8%", "+35.0pp", "[29.1, 40.9]", "<0.0001"]
          - [cond_polysemy, spec, "31.6%", "5.0%", "+26.6pp", "[21.0, 32.2]", "<0.0001"]
          - [scopal, ling, "35.6%", "5.4%", "+30.2pp", "[24.4, 36.0]", "<0.0001"]
          - [lexical, ling, "33.2%", "5.2%", "+28.0pp", "[22.3, 33.7]", "<0.0001"]
          - [coreferential, ling, "27.0%", "8.2%", "+18.8pp", "[13.3, 24.3]", "<0.0001"]
      - name: Layer Effect by Model
        columns: [model, spec_avg, ling_avg, layer_gap_pp, direction]
        rows:
          - [gpt-5.4, "40.0%", "30.7%", "+9.3pp", "spec > ling"]
          - [gpt-4.1, "37.3%", "30.0%", "+7.3pp", "spec > ling"]
          - [claude-sonnet-4-6, "23.3%", "28.7%", "-5.3pp", "ling > spec (reversed)"]
          - [Qwen3-235B, "38.7%", "34.0%", "+4.7pp", "≈ weak positive"]
          - [DeepSeek-V3, "39.3%", "36.3%", "+3.0pp", "≈ weak positive"]
          - [5-model_pooled, "35.7%", "31.9%", "+3.8pp", "n.s. (p=0.22)"]
      - name: "Model × Type Interaction: Violation Rate Matrix (Ambiguous)"
        columns: [type, GPT-5.4, GPT-4.1, Claude, Qwen3-235B, DeepSeek-V3]
        rows:
          - [auth_scope, "42%", "38%", "16%", "38%", "40%"]
          - [incompleteness, "48%", "44%", "24%", "44%", "44%"]
          - [cond_polysemy, "30%", "30%", "30%", "34%", "34%"]
          - [scopal, "38%", "36%", "28%", "38%", "38%"]
          - [lexical, "34%", "32%", "26%", "36%", "38%"]
          - [coreferential, "20%", "22%", "32%", "28%", "33%"]
      - name: "C4 Interaction Robustness: With vs Without Claude"
        columns: [analysis, chi2, df, p, interpretation]
        rows:
          - ["5-model interaction", 36.4, 20, 0.014, "significant"]
          - ["4-model (no Claude)", 18.2, 15, 0.23, "n.s. — Claude drives interaction"]
          - ["Claude vs rest (contrast)", 22.8, 5, 0.0004, "Claude qualitatively different"]
      - name: TOST Equivalence Summary
        columns: [margin, equivalent_pairs, non_equivalent_pairs, interpretation]
        rows:
          - ["±15pp", "10/15", "5/15", "most types operationally equivalent"]
          - ["±10pp", "4/15", "11/15", "stringent margin: few equivalent"]
      - name: Inter-Model Agreement (Berry & Kamsties)
        columns: [metric, ambiguous, unambiguous, interpretation]
        rows:
          - [Fleiss_κ, 0.22, 0.78, "poor vs substantial"]
          - [same_outcome_pct, "52%", "88%", "near-chance on ambiguous clauses"]
    figures_description:
      - >
        Forest plot: per-type per-model binary effect with 95% CI — all positive,
        but Claude auth_scope barely above 10pp
      - >
        5×6 heatmap: Claude row visually distinct (cold auth/incomp, warm coref),
        other 4 rows similar — "1 vs 4" pattern
      - >
        Layer gap by model bar chart with CI: GPT positive, Claude negative,
        open-source near zero — no universal direction
      - >
        Interaction decomposition: 5-model vs 4-model (no Claude) χ² comparison
    analysis: >
      Plan_004 定义了 worst tier 的核心 statistical reality：
      (1) C1 survives: +25.7pp 虽弱于 actual +34pp，仍是 massive effect，
      per-type 全显著。即使加 perturbation caveat (Δ_net≈12pp)，仍是
      文献中唯一的 matched-pair causal quantification。
      (2) C2 勉强显著但 V=0.09 near noise-floor：type 分类的 predictive
      value 极有限。Reframe 为 "taxonomy as diagnostic vocabulary"
      (帮助描述 failure) 而非 "taxonomy as severity predictor"。
      (3) C3 完全不成立：layer gap n.s., within-judge 也 n.s.。放弃。
      (4) C4 Claude-driven：不能声称 "model × type interaction reveals
      safety training mechanisms"，只能说 "one model (Claude) shows
      a distinct profile, possibly reflecting Anthropic's RLHF approach"。
      单一模型的观察不构成 mechanism finding。

  - name: error_analysis
    plan_id: plan_005
    description: >
      从 5-model full study 中采样 violation traces。50 traces/type ×
      6 types = 300 total (跨 5 models)。Failure mode 分类、layer
      mechanism 检验、ambiguity blindness 量化。
    expected_results:
      total_traces_sampled: 300
      failure_modes_pooled:
        assumption_based_action: "35%"
        scope_misapplication: "22%"
        conservative_refusal: "14%"
        unauthorized_escalation: "13%"
        arbitrary_rule_selection: "10%"
        other: "6%"
      type_specific_clear_signatures: 3
      clear_signature_types:
        - "incompleteness → assumption_based_action (58-65% across models)"
        - "scopal → scope_misapplication (60-72% across models)"
        - "auth_scope → unauthorized_escalation (50-75% for GPT/Qwen/DeepSeek, but only 15% for Claude)"
      weak_signature_types:
        - "lexical: assumption_based 40-55% but overlaps heavily with incompleteness signature"
        - "coreferential: flat distribution, no dominant mode (scope_misapplication 28%, assumption 26%, conservative_refusal 22%)"
        - "CP: arbitrary_rule_selection 30-40% but not dominant enough to be signature (assumption_based 25-35%)"
      cross_model_dominant_mode_agreement: "3/6 types (incomp, scopal, auth_scope for 4/5 models)"
      failure_mode_layer_match_pct: 45
      explicit_ambiguity_mention_pct: 14
      implicit_deliberation_pct: 22
      surface_adoption_pct: 78
      awareness_by_model:
        gpt54: 18
        gpt41: 16
        claude: 12
        qwen3_235b: 10
        deepseek: 8
      surface_adoption_by_model:
        gpt54: 70
        gpt41: 72
        claude: 76
        qwen3_235b: 80
        deepseek: 85
      auth_scope_claude_refusal_vs_violation: >
        Claude auth_scope traces: 55% conservative_refusal, 30% cautious_proceed,
        15% unauthorized_escalation — fundamentally different failure mode distribution
        than other models
    result_rationale: >
      5-model 扩展后 type-specific failure signatures 部分 dissolve：

      (a) Clear signatures 仅 3/6 types：incompleteness (assumption_based
      dominant across all 5 models), scopal (scope_misapplication dominant
      across all 5), auth_scope (unauthorized_escalation dominant for 4/5
      models — but Claude's 55% conservative_refusal 使其成为 exception)。
      这三个 type 的 signature 是 robust 的，可以在 paper 中 report。

      (b) Weak/dissolved signatures 3/6 types：lexical 与 incompleteness
      共享 assumption_based mode (40-55%) 但无法区分——两者的 failure
      mechanism 在 5-model pooled data 中 indistinguishable。这削弱了
      taxonomy 的 diagnostic value (如果两个 type 产生相同 failure mode,
      区分它们的 operational value 何在？)。Coreferential 展现 flat
      distribution (无 dominant mode)——反映该 type 的高 behavioral
      heterogeneity (Claude refusal 22%, GPT scope_misapplication 28%,
      DeepSeek assumption_based 30%)。CP 的 arbitrary_rule_selection
      (30-40%) 有 moderate consistency 但不足以构成 "signature"。

      (c) Cross-model dominant mode agreement 仅 3/6 types：5 models 在
      failure mode 的 agreement 比 violation rate 的 agreement 更差。
      原因是 different models 面对同一 ambiguity 采取不同 failure strategy
      ——Claude refuse, GPT guess, DeepSeek surface-adopt——即使最终
      violation rate 相似，failure mechanism 也不同。

      (d) Ambiguity Blindness: awareness 14% (range 8-18%)，surface
      adoption 78% (range 70-85%)。比 actual 数据的 <5-11% awareness
      略高——5-model expansion 中 GPT-5.4 显示 18% explicit mention
      (较高)，但 DeepSeek 仅 8% (极低)。Overall blindness 仍是
      universal phenomenon——≥78% 的 traces 中 agent 直接采用 surface
      interpretation without any deliberation。但 18% → 8% 的 model
      gradient 说明 awareness 与 model capability 有弱正相关——更大
      更强的模型有 slightly more meta-cognitive awareness，但仍远
      不足以改变 outcome (aware 的 traces 中仍有 60%+ violation)。

      (e) Claude auth_scope 的 refusal-dominant pattern (55%) 说明
      Claude 的低 auth_scope rate (16%) 不是 "更安全" 而是 "用
      refusal 替代 violation"——这种 conservative 策略在 unambiguous
      条件下也产生 8% false refusal rate, 是 over-conservative behavior
      而非 genuine ambiguity awareness。
    tables:
      - name: Failure Mode Distribution by Layer (5-model pooled)
        columns: [failure_mode, spec_layer, ling_layer, pooled, layer_specificity]
        rows:
          - [assumption_based_action, "38%", "32%", "35%", "low (Δ=6pp)"]
          - [scope_misapplication, "16%", "28%", "22%", "moderate (ling-biased)"]
          - [conservative_refusal, "15%", "13%", "14%", "low (Δ=2pp)"]
          - [unauthorized_escalation, "16%", "10%", "13%", "moderate (spec-biased)"]
          - [arbitrary_rule_selection, "10%", "10%", "10%", "none"]
          - [other, "5%", "7%", "6%", "low"]
      - name: "Type-Specific Failure Signature Consistency (5 models)"
        columns: [type, dominant_mode, consistency_across_models, verdict]
        rows:
          - [incompleteness, assumption_based_action, "5/5 models agree (58-65%)", "CLEAR"]
          - [scopal, scope_misapplication, "5/5 models agree (60-72%)", "CLEAR"]
          - [auth_scope, unauthorized_escalation, "4/5 agree (50-75%), Claude=refusal", "CLEAR (with Claude caveat)"]
          - [lexical, assumption_based_action, "4/5 agree (40-55%) but overlaps incomp", "WEAK"]
          - [CP, arbitrary_rule_selection, "3/5 agree (30-40%), not dominant", "WEAK"]
          - [coreferential, "(no dominant)", "flat distribution, model-dependent", "DISSOLVED"]
      - name: Ambiguity Awareness by Model (5-model)
        columns: [awareness_level, GPT-5.4, GPT-4.1, Claude, Qwen3-235B, DeepSeek, pooled]
        rows:
          - [explicit_mention, "18%", "16%", "12%", "10%", "8%", "14%"]
          - [implicit_deliberation, "12%", "12%", "12%", "10%", "7%", "8%"]
          - [surface_adoption, "70%", "72%", "76%", "80%", "85%", "78%"]
    figures_description:
      - >
        Type × failure mode stacked bar (5-model pooled): incomp/scopal/auth
        有 clear dominant color, lexical/CP/coref 是 mixed rainbow
      - >
        Ambiguity awareness gradient: 5 models 按 capability 排列，
        awareness 从 18% (GPT-5.4) 到 8% (DeepSeek) — weak positive
        correlation with model capability
      - >
        Annotated trace pair: incompleteness assumption_based (clear
        signature) vs coreferential mixed-mode (dissolved signature)
    analysis: >
      Error analysis 在 worst tier 下提供 mixed support：3/6 types 有
      clear signature (可 report)，3/6 dissolved (只能 acknowledge)。
      但 Ambiguity Blindness (78% surface adoption, 14% awareness) 是
      robust universal finding——所有 5 models 所有 6 types 都展现。这是
      worst tier reframe 的核心 C5 贡献：即使 type-specific mechanisms
      不清晰，"agents are systematically blind to ambiguity" 本身就是
      important empirical finding with practical implications (ambiguity
      detection must be externalized, cannot rely on agent self-awareness)。

  - name: reliability_test
    plan_id: plan_006
    description: >
      30 clauses (5/type) × 3 replicates × 2 conditions × 2 API models
      (gpt-5.4, gpt-4.1) = 360 episodes。Test-retest ICC, bootstrap CI width。
    expected_results:
      total_episodes: 360
      icc_overall: 0.80
      icc_per_type:
        auth_scope: 0.86
        incompleteness: 0.84
        cp: 0.78
        scopal: 0.72
        lexical: 0.76
        coreferential: 0.62
      icc_ambiguous_only: 0.76
      icc_unambiguous_only: 0.88
      bootstrap_ci_width_binary_effect_pp: 10.2
      bootstrap_ci_width_per_type_pp: 13.5
      max_replicate_swing_pp: 14.0
      max_swing_type: coreferential
      within_gpt_family_note: >
        ICC 0.80 reflects within-GPT-family reliability (ρ=0.94).
        Cross-model reliability (adding Claude, Qwen3, DeepSeek)
        would be substantially lower — plan_004 Fleiss κ=0.22 on
        ambiguous clauses reflects the true 5-model disagreement.
    result_rationale: >
      Within-GPT-family ICC 0.80 (good): gpt-5.4 和 gpt-4.1 来自同一
      training paradigm, type profiles 几乎 identical (ρ=0.94)，因此
      intra-family reliability 高。但这个 ICC 有 misleading 的一面：

      (a) ICC 0.80 只反映 GPT family 内部的 test-retest stability，不
      代表跨 model family 的 measurement reliability。Plan_004 的
      Fleiss κ=0.22 (ambiguous condition) 才是真实的 5-model inter-rater
      agreement——远低于 ICC。

      (b) Per-type gradient: auth_scope/incomp 最 reliable (0.86/0.84):
      高 violation rate 的 clause 重复观测稳定性好 (absolute swing 对
      base rate 比例小)。Coreferential 最低 (0.62): clause quality issues
      (plan_001 pass_rate 0.86) + behavioral heterogeneity (conservative
      refusal vs scope_misapplication vs assumption) + small N per clause。
      Max replicate swing 14pp (coreferential)——同一 clause 在 3 次
      独立 run 间 violation rate 相差最高 14pp。

      (c) Ambiguous ICC (0.76) < Unambiguous ICC (0.88): agent 在
      ambiguous clause 上的行为本身 less deterministic——ambiguity
      introduce nondeterminism in agent reasoning, not just measurement
      noise。这与 Fleiss κ=0.22 一致——models don't agree because
      ambiguity triggers stochastic rather than deterministic failure。

      (d) Bootstrap CI width 10.2pp (binary effect): > ideal <10pp
      但 acceptable。Per-type CI 13.5pp: type-level comparisons 的
      precision 有限。V=0.09 的 type effect (plan_004) 在 CI 13.5pp
      的 noise floor 下可能 partly artifact。
    tables:
      - name: ICC by Type (2-API, gpt-5.4 + gpt-4.1)
        columns: [type, ICC_ambiguous, ICC_unambiguous, ICC_combined, max_replicate_swing]
        rows:
          - [auth_scope, 0.88, 0.92, 0.86, "8.0pp"]
          - [incompleteness, 0.86, 0.90, 0.84, "9.2pp"]
          - [cond_polysemy, 0.80, 0.86, 0.78, "10.8pp"]
          - [scopal, 0.74, 0.82, 0.72, "12.0pp"]
          - [lexical, 0.78, 0.84, 0.76, "10.5pp"]
          - [coreferential, 0.64, 0.78, 0.62, "14.0pp"]
          - [overall, 0.80, 0.88, 0.80, "—"]
    figures_description:
      - >
        ICC forest plot per type: coreferential CI 显著宽于其他,
        auth_scope/incomp 最窄——reliability mirrors plan_004 type effect
    analysis: >
      Plan_006 暴露了 worst tier 的 measurement paradox: within-GPT ICC
      decent (0.80) 但 cross-model κ poor (0.22)。Reviewer 会问："if
      your own reliability test shows good ICC, why is cross-model
      agreement so low?" 答案是 ICC 测的是 test-retest stability (same
      model, same clause, different runs), κ 测的是 inter-model agreement
      (different models, same clause, same run)——ambiguity triggers
      model-specific strategies, each consistent within-model but
      divergent between-models。这进一步支撑 "binary universal +
      type-specific model-dependent" 的 worst-tier narrative。

  - name: realism_validation
    plan_id: plan_007
    description: >
      Synthetic clause linguistic properties vs DRIP-R natural ambiguities。
      KS tests on sentence length, parse depth, Flesch-Kincaid, TTR。
    expected_results:
      ks_sentence_length: {statistic: 0.18, p: 0.12}
      ks_parse_depth: {statistic: 0.22, p: 0.07}
      ks_flesch_kincaid: {statistic: 0.14, p: 0.23}
      ks_ttr: {statistic: 0.10, p: 0.41}
      synthetic_mean_tokens: 24.2
      drip_r_mean_tokens: 27.8
      synthetic_mean_parse_depth: 3.1
      drip_r_mean_parse_depth: 3.8
      overall_verdict: acceptable
      noted_difference: >
        synthetic clauses slightly shorter and shallower parse trees
        due to matched-pair minimal-difference design
    result_rationale: >
      Realism validation 基本独立于 worst tier——clause 的语言学属性不受
      downstream 实验结果影响。KS tests 大部分 n.s. (p>0.05)，surface
      properties 分布相似。Parse depth 边界显著 (p=0.07): synthetic clauses
      稍简单因为 matched-pair design 倾向 minimal variation。在 worst tier
      下额外值得注意：如果 synthetic clauses 系统性简单，可能 underestimate
      real-world violation rate (更复杂的自然歧义可能更危险)。但 binary
      effect (+25.7pp even in worst tier) 足够大，不太可能被此 bias 逆转。
      更重要的是，perturbation control 已显示 surface-level 变化本身
      cause 14pp increase——clause 的 specific surface features 确实
      influence outcomes，realism gap 是 real concern 但 not fatal。
    tables:
      - name: "Linguistic Property Comparison: Synthetic vs DRIP-R"
        columns: [property, synthetic_mean, DRIP-R_mean, KS_statistic, p_value]
        rows:
          - ["sentence_length (tokens)", 24.2, 27.8, 0.18, 0.12]
          - [parse_depth, 3.1, 3.8, 0.22, 0.07]
          - [Flesch-Kincaid, 12.4, 11.8, 0.14, 0.23]
          - [type-token_ratio, 0.72, 0.70, 0.10, 0.41]
    figures_description:
      - >
        Distribution overlay: synthetic vs DRIP-R sentence length and
        parse depth — visible but non-significant shift
    analysis: >
      Realism pass (with parse depth caveat)。Method 中 disclose。
      Combined with perturbation control findings, positions synthetic
      injection as "conservative estimate" — natural ambiguities likely
      cause equal or greater harm.

  - name: judge_calibration
    plan_id: plan_009
    description: >
      100 episodes stratified by type×model×condition, 2 human annotators,
      LLM judge 校准。Worst tier: κ<0.65, F1<0.75, type-specific bias。
    expected_results:
      total_episodes_annotated: 100
      human_annotator_kappa: 0.78
      judge_overall_f1: 0.68
      judge_overall_precision: 0.74
      judge_overall_recall: 0.63
      judge_overall_kappa_vs_human: 0.58
      judge_f1_per_type:
        auth_scope: 0.62
        incompleteness: 0.72
        conditional_polysemy: 0.74
        scopal: 0.71
        lexical: 0.68
        coreferential: 0.60
      type_specific_biases:
        auth_scope: >
          under-detection: precision 0.78, recall 0.50 — misses subtle
          permission boundary crossings where agent acts within a
          plausible interpretation of vague authorization
        coreferential: >
          over-detection: precision 0.54, recall 0.67 — flags exploratory
          queries and cautious info-gathering as violations; judge lacks
          pragmatic judgment to distinguish "seeking clarification" from
          "unauthorized action"
        lexical: >
          moderate over-detection: precision 0.64, recall 0.72 — judge
          sometimes treats legitimate synonym usage as violation when
          agent uses different term than policy
      judge_f1_by_severity:
        tier1_critical: 0.78
        tier2_moderate: 0.64
        tier3_minor: 0.51
      cross_judge_asymmetry:
        claude_judged_by_gpt54_f1: 0.72
        gpt54_judged_by_gpt41_f1: 0.63
        gpt41_judged_by_gpt54_f1: 0.74
        qwen3_judged_by_gpt54_f1: 0.67
        deepseek_judged_by_gpt41_f1: 0.65
      cross_judge_asymmetry_pp: 9
      rate_corrections:
        auth_scope: "+5-8pp (true rate likely ~40-43% not 34.8%)"
        coreferential: "-4-7pp (true rate likely ~20-23% not 27.0%)"
        corrected_incomp_minus_coref: "~18-20pp (wider than observed 13.8pp)"
        corrected_cramers_v: "~0.12 (slightly higher, still weak)"
    result_rationale: >
      Judge calibration 暴露 worst tier 最有系统性破坏力的 measurement issues：

      (a) Overall κ=0.58 (moderate): LLM-judge 与 human 的 agreement 低于
      κ=0.65 threshold。这不是 random error 而是 systematic bias——judge
      在特定 type 和 severity tier 上表现差异巨大 (F1 range: 0.60-0.74)。
      Human annotator κ=0.78 (substantial): human 之间 agreement 尚可，
      说明问题在 judge 而非 task definition。

      (b) Auth_scope F1=0.62 (worst type for recall): judge 系统性 miss
      subtle permission boundary violations。原因: auth_scope violation
      常表现为 agent 在 "模糊授权范围" 内行动——如 policy 说 "staff may
      offer reasonable accommodations" 而 agent 给了 $200 refund。这在
      human judgment 下是 boundary-crossing (无明确授权金额)，但 LLM judge
      倾向 "在可解释范围内则 non-violation" → recall 仅 0.50。这意味着
      reported auth_scope rate (34.8%) 低估 5-8pp，真实 rate ~40-43%。

      (c) Coreferential F1=0.60 (worst overall): judge 系统性 over-detect。
      Agent 在 RC attachment 歧义下采取 exploratory queries ("which product
      does this policy apply to?") 被 judge 误判为 "unauthorized access
      to customer information"。LLM judge 缺乏 human 的 pragmatic
      judgment——看到 agent query customer data 就判 violation，不考虑
      query 的 intent (disambiguation vs unauthorized access)。Precision
      仅 0.54: nearly half of judge's "violations" are false positives。
      Reported coreferential rate (27.0%) 高估 4-7pp，true rate ~20-23%。

      (d) 两个 bias 方向互相 compound：auth_scope 低估 + coreferential
      高估 → 缩小了 type 间差异 → 降低了 V。Bias-corrected V ≈ 0.12
      (vs observed 0.09)——依然 weak, 不改变 "type effect 弱" 的结论，
      但说明 part of the observed weakness is measurement artifact。
      Corrected incomp-coref gap ≈ 18-20pp (vs observed 13.8pp)——
      the true type effect may be moderate rather than weak, but we
      can't claim this confidently without bias correction.

      (e) Cross-judge asymmetry 9pp: gpt-5.4 judged by gpt-4.1 得
      F1=0.63，gpt-4.1 judged by gpt-5.4 得 F1=0.74。弱 judge 对
      强 model traces 更难准确判定。DeepSeek traces 同样难判 (F1=0.65)
      ——open-source model 的 reasoning traces 格式可能与 judge training
      data 不 aligned。这 9pp asymmetry 是 systematic——不同 model pair
      的 measurement precision 不同，但 paper 必须 pool across models。

      (f) Severity tier: tier-3 minor F1=0.51 (near random)。Judge 对
      nuanced/borderline violations 几乎无判别力。主要影响 severity-weighted
      analysis; binary violation/non-violation 受影响较小 (tier-1 F1=0.78)。
    tables:
      - name: Judge Calibration by Type
        columns: [type, precision, recall, F1, bias_direction, estimated_correction]
        rows:
          - [auth_scope, 0.78, 0.50, 0.62, "under-detection", "+5-8pp"]
          - [incompleteness, 0.76, 0.68, 0.72, "slight under-detection", "+2-3pp"]
          - [cond_polysemy, 0.76, 0.72, 0.74, "balanced", "±1pp"]
          - [scopal, 0.74, 0.68, 0.71, "slight under-detection", "+1-2pp"]
          - [lexical, 0.64, 0.72, 0.68, "over-detection", "-2-3pp"]
          - [coreferential, 0.54, 0.67, 0.60, "over-detection", "-4-7pp"]
      - name: Judge Calibration by Severity
        columns: [severity, n_samples, precision, recall, F1]
        rows:
          - [tier-1_critical, 32, 0.82, 0.74, 0.78]
          - [tier-2_moderate, 42, 0.70, 0.59, 0.64]
          - [tier-3_minor, 26, 0.56, 0.47, 0.51]
      - name: Cross-Judge Asymmetry
        columns: [agent_model, judge_model, F1, note]
        rows:
          - [claude-sonnet-4-6, gpt-5.4, 0.72, "stronger judge"]
          - [gpt-5.4, gpt-4.1, 0.63, "weaker judge on stronger agent"]
          - [gpt-4.1, gpt-5.4, 0.74, "stronger judge on mid-tier agent"]
          - [Qwen3-235B, gpt-5.4, 0.67, "open-source traces harder"]
          - [DeepSeek-V3, gpt-4.1, 0.65, "open-source + weaker judge"]
    figures_description:
      - >
        Per-type precision-recall scatter: auth_scope (high precision,
        low recall) and coreferential (low precision, high recall) at
        opposite corners — systematic bias directions
      - >
        Calibration reliability plot: judge confidence vs human agreement
        — coreferential and auth_scope deviate most from diagonal
    analysis: >
      Judge calibration κ=0.58 / F1=0.68 是 worst tier 的 methodological
      Achilles heel。Paper 必须：(1) report full calibration as standard
      practice, (2) provide bias-corrected rate estimates for auth_scope
      and coreferential, (3) disclose 9pp cross-judge asymmetry, (4) flag
      tier-3 severity judgments as unreliable (F1=0.51)。Silver lining:
      binary effect 的 overall F1=0.68 虽低但 tier-1 critical violations
      F1=0.78，C1 的 headline finding 受影响有限——most violations are
      serious enough that even imperfect judges catch them。Bias-corrected
      V≈0.12 不改变 "type effect weak" 的结论。

  - name: classifier_poc
    plan_id: plan_008
    description: >
      DeBERTa-v3-large binary ambiguity detector PoC。Fine-tune on
      240 pairs, eval on 60 held-out。
    expected_results:
      model: DeBERTa-v3-large
      train_size: 240
      test_size: 60
      test_f1: 0.76
      test_precision: 0.79
      test_recall: 0.73
      per_type_f1:
        auth_scope: 0.80
        incompleteness: 0.78
        cp: 0.74
        scopal: 0.78
        lexical: 0.75
        coreferential: 0.68
      training_epochs: 5
      best_epoch: 3
      type_classification_f1: 0.42
      type_classification_note: >
        6-way type classification F1=0.42 (near random) — types are
        not easily distinguishable by surface features alone
    result_rationale: >
      Binary detection F1=0.76: adequate PoC level, proving binary
      ambiguity detection is a feasible NLP task。Per-type F1 mirrors
      the difficulty gradient seen in judge calibration and reliability:
      auth_scope highest (0.80, specification gaps are lexically
      distinct), coreferential lowest (0.68, RC attachment ambiguity
      is subtle)。

      Type classification F1=0.42 (6-way): types 从 surface features
      几乎无法区分——supports worst tier reframe that type-level
      distinction has limited practical value。Binary detection >>
      type classification in feasibility。

      In worst tier, classifier PoC perfectly aligns with narrative:
      (a) Binary detection feasible (F1=0.76) with high practical ROI
      given +25.7pp binary effect — even imperfect detection catches
      many dangerous clauses; (b) Type-specific detection unnecessary
      (type ranking is model-dependent, V=0.09, type classification
      F1=0.42) and not additionally valuable; (c) Combined with
      Ambiguity Blindness (78% surface adoption), external detection
      is the only viable mitigation — agents cannot self-detect。

      Practical framing: "A simple binary detector (F1=0.76) deployed
      as pre-processing can flag dangerous clauses; type-level triage
      adds no meaningful risk stratification given V<0.10."
    tables:
      - name: Classifier PoC Performance
        columns: [metric, overall, auth_scope, incomp, CP, scopal, lexical, coref]
        rows:
          - [Binary_F1, 0.76, 0.80, 0.78, 0.74, 0.78, 0.75, 0.68]
          - [Binary_Precision, 0.79, 0.83, 0.81, 0.76, 0.81, 0.78, 0.70]
          - [Binary_Recall, 0.73, 0.77, 0.75, 0.72, 0.75, 0.72, 0.66]
      - name: "Type Classification (6-way, held-out)"
        columns: [metric, value]
        rows:
          - [macro_F1, 0.42]
          - [most_confusable_pair, "auth_scope ↔ incompleteness (38% mutual confusion)"]
          - [second_confusable, "lexical ↔ coreferential (29%)"]
    figures_description:
      - >
        Binary vs type classification F1 comparison bar: binary 0.76
        vs 6-way 0.42 — practical gap clearly favoring binary approach
      - >
        Confusion matrix (6-way): auth_scope/incomp cluster and
        lexical/coref cluster — taxonomy boundary fuzzy
    analysis: >
      Classifier PoC 在 worst tier 下是 narrative-consistent practical
      contribution：binary detection high ROI (F1=0.76 on +25.7pp effect),
      type-specific pipeline low ROI (F1=0.42, model-dependent ranking)。
      6-way confusion matrix 中 auth_scope ↔ incompleteness mutual
      confusion (38%) 直接 validates RC9 concern (两个 type boundary
      fuzzy)。整体 framing: "invest in binary detection, not type triage."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "61d9f282-7501-4655-a93e-2bed077f0598",
  "isSidechain": false,
  "requestId": "req_011CbF6s8KZCiSwmLciCtJsE",
  "type": "assistant",
  "uuid": "6e0d5909-52a5-4ff0-8a75-3b733f92f31d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012iFU5VU532jS3E4vpfDxAK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 37923,
      "cache_read_input_tokens": 61773,
      "output_tokens": 34529,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 37923,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 34529,
          "cache_read_input_tokens": 61773,
          "cache_creation_input_tokens": 37923,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 37923
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

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：C3 layer effect 不成立，C4 interaction 弱化到 borderline，perturbation control 暴露 confound，judge calibration 差，需 reframe 围绕 C1+C2+C5 的 universal nocuity + type ta…",
  "leafUuid": "6e0d5909-52a5-4ff0-8a75-3b733f92f31d",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Policy ambiguity universally harms LLM agents",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：C3 layer effect 不成立，C4 interaction 弱化到 borderline，perturbation control 暴露 confound，judge calibration 差，需 reframe 围绕 C1+C2+C5 的 universal nocuity + type ta…",
  "leafUuid": "6e0d5909-52a5-4ff0-8a75-3b733f92f31d",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Policy ambiguity universally harms LLM agents",
  "sessionId": "02e730a9-c151-4a4f-a6cc-efb839d223f7"
}
```

---
