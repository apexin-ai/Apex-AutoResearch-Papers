# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：SOPBench不复制或verifier不兼容，需放弃cross-benchmark claim，用deep single-benchmark cau

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/a995b27a-21cd-4926-acb4-3043954b7476.jsonl`
- **Structured JSON:** [`0527505c3f2a2246f23d.json`](../../sessions/05/0527505c3f2a2246f23d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T11:30:11.011Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T11:30:11.011Z",
  "sessionId": "a995b27a-21cd-4926-acb4-3043954b7476",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：SOPBench不复制或verifier不兼容，需放弃cross-benchmark claim，用deep single-benchmark causal rigor + model diversity重新定位\n核心假设：['SOPBench C1不复制（Δ<15pp或p>0.05）或rule-based verifier与ambiguity injection不兼容（verifier无法区分ambiguity-induced violations vs correct behavior）', '类型排序与τ²-bench无相关或负相关（ρ<0.3），暗示type hierarchy是benchmark-specific artifact', 'C3 layer effect在审稿中被challenge为model composition artifact（GPT drives the gap）', '至少一位审稿人认为synthetic injection + single primary benchmark = insufficient external validity', '但C1在τ²-bench的5-model +34pp效应、perturbation control、7-model扩展（plan_013）仍intact', 'judge calibration κ=0.807仍强，causal design仍是literature最强']\n关键指标范围：{'sopbench_c1_delta_pp': [0, 15], 'sopbench_type_rank_rho': [-0.2, 0.3], 'sopbench_incompleteness_rate': [0.2, 0.4], 'cross_benchmark_effect_correlation': [-0.1, 0.4], 'expected_review_avg': [2.5, 3.0], 'claims_surviving_without_revision': [1, 2]}\n叙事方向：放弃cross-domain generalization claim。不报告SOPBench（或一句话acknowledge未复制作为limitation）。Reframe核心贡献为：(1) methodological——首个matched-pair + perturbation control因果设计，是agent safety评估的方法论模板；(2) model×type interaction——即使限于customer-service domain，52pp auth_scope range + incompleteness universality是safety alignment的actionable insight；(3) 7-model breadth（plan_013: Gemini+LLaMA也复制C1）替代cross-benchmark breadth。叙事从'cross-domain law'转为'深度因果剖析揭示safety training盲区'——强调因果rigor超越correlation-based prior work（DRIP-R, PhantomPolicy）。Title可能需改：去掉任何暗示generality的词，改为'Causal Anatomy of Policy Ambiguity Vulnerability in LLM Agents'。仍冲EMNLP——causal method + interaction finding + 7 models足够，只是framing更modest。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: policy_ambiguity_safety\nvenue: emnlp-2026\nfocus: Cross-benchmark replication on SOPBench (Healthcare + Bank domains) added to plan. Assess: (1) Does SOPBench replication meaningfully strengthen the paper vs current single-benchmark version? (2) What's the realistic best/median/worst score with vs without SOPBench? (3) Are there any risks (e.g., effect doesn't replicate, rule-based verifier incompatibility)? Round 13 claim calibration already complete (22× removed, margin conditions added, judge annotations, confound anchors).\n\n## paper_framing.md\n\n# Paper Framing — policy_ambiguity_safety\n\n> 最后更新: 2026-05-20 19:30 UTC | 状态: 5-model analysis complete, C3/C4 framing revised\n> 目标: EMNLP 2026 (ARR Aug cycle, DDL ~Aug 3)\n> Dream: dream_20260520T112859 — best 3.5 / median 3.0 / worst 2.5 (pre-pivot; re-dream needed)\n> 5-model: 2,997 episodes, C1 confirmed (+34.0pp, 5 models), C4 upgraded (model×type interaction)\n\n## Core Insight\n\nPolicy ambiguity universally causes massive safety violations in LLM agents (+34.0pp across 5 architecturally diverse models), with a significant type hierarchy (incompleteness 53.6% >> coreferential 31.6%). Specification-layer types are more dangerous on average (Δ=6.08pp, p=0.017), but the deeper finding is a **model × type interaction**: authorization scope vulnerability varies 52pp across models (12% Claude to 64% GPT-5.4), revealing that safety training differentially mitigates specific ambiguity types, while incompleteness remains universally dangerous. This interaction connects Berry & Kamsties' nocuous ambiguity theory to modern safety alignment and suggests both type-aware triage AND model-aware risk assessment.\n\n## Title (Working)\n\n\"Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families\"\n\nAlternative: \"Differential Nocuity: How Ambiguity Type and Model Architecture Shape Safety Violations in LLM Agents\"\n\nNote: Pivoted from \"Uniformly Nocuous\" → \"Specification-Layer Dominant\" (2-model) → \"Differential Nocuity with Model Interaction\" (5-model). The model × type interaction is the novel finding that elevates the paper beyond simple effect demonstration.\n\n## Core Claims\n\n### C1: Binary Effect (PRIMARY — confirmed, 5 models)\nAmbiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +34.0pp (5-model), McNemar OR=15.1 (CI: [10.78, 21.17]), p<0.0001. Holds across all 6 types and all 5 models.\n- **Evidence**: 2,997 episodes across 5 models × 6 types × 2 conditions. Bootstrap CI: [+31.2pp, +36.9pp].\n- **Per-model**: Claude +25.7pp, Qwen3 +32.4pp, GPT-4.1 +34.7pp, GPT-5.4 +38.3pp, DeepSeek +39.0pp — all p<10^-17.\n- **Strength**: Extremely strong. Replicated across 5 architecturally diverse models (proprietary dense, open-source MoE, open-source dense), 6 types, 2 domains. No exceptions.\n- **Causal backing**: Matched-pair design + perturbation control (plan_010, Δ_perturb=3.33pp, PASS) → strongest causal inference in the literature.\n- **Logistic regression**: condition_amb coef=2.278, z=19.65, p<0.001 — ambiguity is the dominant predictor even after controlling for token delta, model, and type.\n\n### C2: Type Hierarchy (SECONDARY — confirmed, 5 models)\n**PIVOTED from uniformity null.** 6-type hierarchy significant: omnibus χ²=28.02, p=3.6×10^-5, V=0.137 (small but well-powered: actual power=0.993, MDE=0.093). 3-tier structure emerges from TOST analysis.\n- **Evidence**: 2,997 episodes (5 models × 6 types × 2 conditions, ambiguous only: 1,499 episodes)\n  - **High tier**: incompleteness 53.6% (standout — universally dangerous across all models)\n  - **Mid tier**: lexical 42.8%, auth_scope 41.6%, scopal 39.4%, CP 36.8% — pairwise equivalent at ±15pp\n  - **Low tier**: coreferential 31.6% (lowest — partial disambiguation via tool responses)\n- **TOST structure**: ±15pp: 8/15 equivalent, 7/15 non-equivalent. ±10pp: 4/15 equivalent, 11/15 non-equivalent. Types are NOT interchangeable.\n- **V=0.137 context**: Below 0.20 threshold but well-powered (power=0.993). The type effect is real but small — the 3-tier structure captures it better than a single V statistic. The heterogeneity is driven by the extremes (incompleteness 53.6% vs coreferential 31.6% = 22pp gap).\n- **Coreferential as boundary case**: 31.6% violation rate is the lowest but still substantial (+18.7pp vs unambiguous). Agents partially disambiguate via tool responses and cautious strategies. Conservative_refusal rate 6-11% (vs avg 2-3%).\n- **Model-dependence of type rankings**: Type rankings are NOT identical across models. Incompleteness is top-2 for ALL models, but auth_scope ranges from #1 (GPT-5.4, DeepSeek) to #6 (Claude). See C4.\n\n### C3: Layer Effect (TERTIARY — suggestive, fragile under within-judge analysis)\n**[2026-05-20 REVISED with 5-model data + within-judge check]** Specification-layer ambiguities cause more violations than linguistic-layer on average, but the effect is modest, model-dependent, and fragile under subgroup analysis.\n- **Evidence (5-model aggregate)**: Spec 44.0% vs Ling 37.9%, Δ=6.08pp, CI [1.14, 11.02], χ²=5.73, p=0.017, V=0.062 (small), OR=1.29 [1.05, 1.58].\n- **Within-judge fragility**: gpt-4.1 judged group (gpt-5.4+DeepSeek): Δ=+8.0pp, p=0.059 (marginal). gpt-5.4 judged group (gpt-4.1+Claude+Qwen3): Δ=+4.8pp, p=0.157 (n.s.). Pooled significance may partly reflect between-judge variance or insufficient within-group power. Paper表述: \"suggestive\" or \"a moderate tendency,\" NOT \"confirmed.\" Disclose within-judge non-significance in Limitations.\n- **Per-model layer gaps** (THE KEY FINDING — feeds C4):\n  - GPT-5.4: +14.0pp (spec 48.0% vs ling 34.0%) — strong\n  - GPT-4.1: +12.0pp (spec 46.7% vs ling 34.7%) — strong\n  - Claude: +3.3pp (spec 32.0% vs ling 28.7%) — weak\n  - DeepSeek: +2.0pp (spec 50.7% vs ling 48.7%) — negligible\n  - Qwen3: -0.9pp (spec 42.7% vs ling 43.6%) — reversed!\n- **Root cause**: auth_scope is the primary driver. GPT models have extremely high auth_scope rates (46-64%), inflating their spec-layer average. Claude (12%) and Qwen3 (26%) have low auth_scope, so their spec-layer advantage disappears.\n- **Framing decision**: C3 is NOT \"spec-layer nearly twice as dangerous\" (that was 2-model artifact). The correct framing is: \"Specification-layer types are significantly more dangerous on average (Δ=6.08pp, p=0.017), but this aggregate masks a model × type interaction where the gap varies from +14pp (GPT-5.4) to -1pp (Qwen3). The interaction, not the main effect, is the theoretically interesting finding (see C4).\"\n- **Info delta as mediator** [MF-2]: Token delta significant in 5-model logistic regression (coef=0.022, z=3.49, p=0.0005). Spec-layer clauses require more tokens to disambiguate (auth_scope 36.1, incomp 34.6 vs coref 7.8 tokens). Info delta partially mediates but doesn't eliminate the condition effect (condition_amb coef=2.278 dominates).\n- **Layer overlap persists**: CP (36.8%, spec) < scopal (39.4%, ling). Mid-tier cluster spans both layers. Layer effect is driven by extremes: incompleteness (53.6%, spec) vs coreferential (31.6%, ling).\n- **ICC convergent evidence** [plan_006]: Per-type ICC mirrors layer hierarchy — Ling-layer ICC all excellent (scopal 0.989, lexical 0.981, coref 0.976), Spec-layer ICC all good (auth 0.857, CP 0.856, incomp 0.807). Spec-layer less reproducible — agents guess differently each run when external disambiguation channels are absent.\n- **CL connection**: Parallels pragmatics vs semantics distinction. Good-enough processing (Ferreira et al. 2002). Disambiguation channel framework: linguistic ambiguity has partial external resolution; specification ambiguity forces guessing.\n\n### C4: Model × Type Interaction (UPGRADED — star finding, 5 models complete)\n**[2026-05-20 DEFINITIVE, 5/5 models]** Models show significantly different vulnerability profiles despite universal binary effect. The interaction is the paper's most novel finding.\n- **Model main effect**: Overall χ²=31.02, p=3.0×10^-6, V=0.102. Ambiguous-only: χ²=24.01, p=7.9×10^-5.\n  - Vulnerability ranking: Claude 30.3% < GPT-5.4 41.0% ≈ GPT-4.1 40.7% < Qwen3 43.1% < DeepSeek 49.7%\n  - Bootstrap CI confirms: Claude significantly lower than all others; DeepSeek significantly higher than GPT models.\n- **Model × Type interaction matrix** (ambiguous condition, violation rates):\n  ```\n  Type                  GPT-5.4  GPT-4.1  Claude  Qwen3   DeepSeek\n  authorization_scope     64%     46%      12%     26%     60%\n  conditional_precedence  34%     36%      36%     40%     38%\n  incompleteness          46%     58%      48%     62%     54%\n  lexical                 42%     34%      32%     52%     54%\n  coreferential           18%     32%      22%     42%     44%\n  scopal                  42%     38%      32%     37%     48%\n  ```\n- **Key interaction patterns**:\n  - **auth_scope**: 52pp range (Claude 12% → GPT-5.4 64%). The MODEL-DIFFERENTIATING type. Claude's RLHF appears to specifically train authorization boundary awareness.\n  - **coreferential**: 26pp range (GPT-5.4 18% → DeepSeek 44%). Second most model-dependent. Open-source models struggle more with referential ambiguity.\n  - **incompleteness**: Universally high (46-62%, 16pp range). ALL models fail on missing information — safety training doesn't help when information literally isn't there.\n  - **CP**: Most model-invariant (34-40%, 6pp range). Explicit rule conflicts treated similarly by all architectures.\n- **Per-model type χ²** (which models show type-specific vulnerability patterns):\n  - GPT-5.4: χ²=23.44, p=0.0003, V=0.28 — strongest type differentiation (very high auth_scope, very low coref)\n  - Claude: χ²=17.87, p=0.003, V=0.24 — strong differentiation (very low auth_scope, moderate others)\n  - Qwen3: χ²=15.89, p=0.007, V=0.23 — moderate differentiation (high incomp+lex, low auth_scope)\n  - GPT-4.1: χ²=9.89, p=0.078, V=0.18 — borderline\n  - DeepSeek: χ²=6.31, p=0.277, V=0.14 — NOT significant (uniformly high across all types)\n- **Fleiss κ = 0.384 (fair agreement)**: Models only moderately agree on which specific clauses trigger violations. The binary effect is universal, but the WHICH-clauses question is model-dependent.\n- **Theoretical implications**: (1) Safety training differentially addresses specific ambiguity types — Claude's auth_scope robustness suggests authorization boundary handling was explicitly or implicitly trained. (2) Incompleteness is a \"safety training blind spot\" — all models fail equally. (3) DeepSeek's uniform vulnerability suggests less type-specific safety training.\n- **Framing**: C4 from \"models agree\" → \"Models show systematically different vulnerability profiles. The binary effect is universal, but HOW models fail depends on the intersection of ambiguity type and safety training approach. auth_scope is the canary type — most sensitive to safety training quality.\"\n- **Evidence from plan_005**: 2-model failure modes consistent (5/6 dominant modes identical). 5-model failure mode analysis pending.\n- **Layer effect moderation**: C3's aggregate layer gap (6.08pp) is driven by GPT models' high auth_scope rates. The layer effect is itself model-dependent (GPT +12-14pp, Claude +3pp, Qwen3 reversed), making the MODEL × TYPE interaction more fundamental than the LAYER main effect.\n\n### C5: Error Analysis (CONFIRMED — EMNLP core)\nDifferent ambiguity types produce qualitatively different failure modes with type-specific signatures. plan_005 (123+122 violation traces across gpt-5.4 and gpt-4.1, confidence=0.94).\n- **Evidence**: plan_005 complete (gpt-5.4: 123 traces, gpt-4.1: 122 traces). Key findings:\n  - **Type-specific failure signatures**: auth_scope → unauthorized_escalation (72%/83%); incompleteness → assumption_based_action (61%/66%); scopal → scope_misapplication (76%/74%); lexical → assumption_based_action (71%/53%); CP → scope_misapplication (41%/28%) + arbitrary_rule_selection (29%/28%); coreferential → scope_misapplication (44%) / assumption_based_action (38%)\n  - **Cross-model consistency**: 5/6 types share the same dominant failure mode across gpt-5.4 and gpt-4.1. Only coreferential diverges (scope_misapplication vs assumption_based_action). Overall mode distribution nearly identical: both ~33% assumption_based_action, ~26-32% unauthorized_escalation, ~25-28% scope_misapplication. Failure mode profiles are type-specific, not model-specific.\n  - **Layer mechanism**: Ling-layer dominated by scope_misapplication (39% ling avg vs 15% spec avg) = \"misparse\"; Spec-layer dominated by unauthorized_escalation + assumption_based_action = \"active guessing\" → explains higher violation rates\n  - **Ambiguity Blindness empirically confirmed**: awareness rate gpt-5.4=4.1%, gpt-4.1=10.7% (both very low); surface_adoption >88% all types both models; escalate_to_user <1%. Nuance: gpt-4.1 (mid-tier) shows 2.6× higher awareness than gpt-5.4 (frontier) — awareness may inversely correlate with action-orientation (frontier models more \"confident,\" act without hesitation)\n  - **Cross-domain consistency**: airline vs retail failure mode profiles Δ < 13pp (unauthorized_escalation shows largest domain effect: retail 38.6% vs airline 26.1%)\n  - **Coreferential boundary**: conservative_refusal 6-11% (vs avg 2-3%) partially explains low violation rate — agents sometimes pause rather than guess. N=25 combined traces show no single dominant failure mode (flat distribution: scope_misapplication 32%, assumption_based_action 28%, unauthorized_escalation 16%) — contrasts with other types' sharp signatures, reflecting the diversity of resolution strategies for referential ambiguity\n  - **Lexical surprise**: 53-71% assumption_based_action — agents treat word ambiguity as information gap, not misparse\n- **Automated inter-coder agreement** [MF-5, Reviewer-validated]: Cross-coding 60 traces (gpt-5.4 vs gpt-4.1 as independent coders). 4-category merged: 80% agreement, Cohen's κ=0.594 (moderate). κ deflated by kappa paradox — lexical 91.7% agreement → κ=0.0 (11/12 same label, chance agreement also high), scopal 100% agreement → κ undefined. True disagreement concentrated at unauthorized_escalation ↔ inappropriate_action boundary in auth_scope (κ=0.054) and incompleteness (κ=0.233).\n  - **Reporting strategy** [Reviewer recommendation]: (1) Compute Gwet's AC1 as primary metric (designed for kappa paradox, expected 0.70-0.75); (2) Report 80% agreement + 5/6 dominant mode consistency as headline validity evidence; (3) Report κ honestly with kappa paradox caveat; (4) Auth_scope failure mode: soften to \"dominated by boundary-exceeding behaviors (unauthorized_escalation or inappropriate_action, >90%)\" instead of specific percentages; (5) Fine-grained 6-type as appendix with \"automated coding\" caveat.\n  - **C5 safety**: Ambiguity Blindness (<5-11%), surface_adoption (>88%), layer mechanism (ling→scope vs spec→escalation) all robust. Fine-grained per-type percentages unreliable at κ=0.594. Plan_009 human anchor (20-30 failure mode traces) would upgrade from \"moderate automated\" to validated.\n- **EMNLP value**: Highest. Provides the linguistic WHY behind the quantitative WHAT. Cross-model + cross-domain consistency elevates from anecdotal to systematic finding. \"Ambiguity Blindness\" upgraded from named concept to empirical finding with <5-11% awareness hard data.\n\n## Narrative Structure (CL-first for EMNLP)\n\n### Intro Logic Chain\n1. Agent policies are written in NL → contain ambiguity (established)\n2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact\n3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.\n4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter? Does it depend on the model?\n5. **This paper**: First causal, type-granularity, cross-model study. Matched-pair design + perturbation control isolates ambiguity effect. 5 models × 6 types.\n6. **Core findings**: (a) All ambiguity is nocuous (+34.0pp, 5 models), (b) type DOES predict severity — 3-tier hierarchy with incompleteness most dangerous, (c) models show dramatically different vulnerability profiles — auth_scope varies 52pp across models, suggesting safety training differentially addresses ambiguity types, (d) while incompleteness remains universally dangerous, a \"safety training blind spot.\"\n\n### Section Map\n- **§1 Intro**: Gap + contributions (causal map + differential nocuity + model×type interaction)\n- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R\n- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R\n- **§4 Method**: Matched-pair causal design, τ²-bench, 5 models (3 proprietary + 2 open-source), clause generation, perturbation control, cross-judge evaluation\n- **§5 Results**: C1 (binary, +34.0pp, 5 models) → C2 (type hierarchy, 3-tier) → C3 (layer effect, modest but significant) → C4 (model×type interaction — star finding)\n- **§6 Analysis**: C5 error analysis — qualitative failure modes per type. Ambiguity Blindness. Model-specific patterns.\n- **§7 Discussion**: Differential nocuity theory. Safety training selectivity. Disambiguation channel framework. Limitations (2 domains, synthetic injection, LLM-as-judge).\n- **§8 Conclusion**: All policy ambiguity is nocuous, but type AND model jointly determine risk level. Both type-aware auditing and model-specific risk assessment recommended.\n\n## Anticipated Reviewer Concerns\n\n### RC1: \"Type effect could be artifact of taxonomy granularity\"\n**Response**: (a) Layer effect (Spec vs Ling ~19pp gap) is robust — holds even if individual types are reclassified. (b) 2-layer structure grounded in Li et al. + Massey et al. (c) Coreferential's low rate has structural explanation (disambiguation channels), not just noise. (d) TOST confirms types are NOT equivalent (0/15 pairs at ±10pp).\n\n### RC2: \"Taxonomy is ad hoc / why these 6 types\"\n**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).\n\n### RC3: \"Only API models, no open-source\"\n**Response**: ✅ RESOLVED. 5-model coverage spans: frontier proprietary (gpt-5.4, claude-sonnet-4-6) + mid-tier proprietary (gpt-4.1) + open-source MoE (qwen3-235b) + open-source dense (deepseek-v3). Three providers (OpenAI, Anthropic, Chinese open-source). Two architecture types (dense, MoE). Model×type interaction (C4) reveals rich cross-model patterns.\n**Note [Reviewer 2026-05-20]**: Cross-judge asymmetry — Claude judged by gpt-5.4, gpt-5.4 judged by gpt-4.1. Must disclose in Method. plan_009 judge calibration measures this bias.\n\n### RC4: \"Synthetic ambiguity injection lacks ecological validity\"\n**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.\n\n### RC5: \"τ²-bench limited to retail/airline\"\n**Response**: ✅ ADDRESSED (plan_017). Cross-benchmark replication on SOPBench (Li et al., 2025) — Healthcare + Bank domains, 100 clause pairs × 5 models = 1,000 episodes with rule-based verifier. If C1 replicates, paper moves from \"customer service finding\" to \"cross-domain finding\" spanning 4 domains (retail, airline, healthcare, banking). Result in Appendix with main-text summary. τ²-bench remains primary; SOPBench provides independent cross-domain confirmation.\n\n### RC6: \"Binary effect is obvious — of course ambiguity causes errors\"\n**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOES predict severity — specification-layer ambiguities are nearly twice as dangerous, connecting to disambiguation channel availability.\n\n### RC7: \"Incompleteness matched-pair confound (information asymmetry)\"\n**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.\n\n### RC8: \"RC attachment in coreferential overlaps with scopal / structural ambiguity\"\n**Response**: (a) Our scopal category is explicitly scoped to quantifier/negation/modal scope interactions, not syntactic attachment. (b) RC attachment in policies manifests as *referential* confusion (which entity does the clause modify?) not *scope* confusion (which operator takes wide scope?). (c) Li et al. 2024 distinguishes syntactic ambiguity (including RC attachment) from scopal ambiguity — our grouping follows their treatment that RC attachment is closer to coreferential than scopal in terms of downstream interpretation. (d) Empirically, if the distinction were problematic, coreferential and scopal would show identical violation patterns — the error analysis (C5) can test whether their failure modes differ.\n\n### RC9: \"authorization_scope is just a subtype of incompleteness\"\n**Response**: (a) Incompleteness = missing conditions/exceptions/boundaries (structural absence). Authorization scope = ambiguous permission/role boundaries that ARE stated but vague (e.g., \"authorized personnel\" without specifying which functions). (b) The disambiguation pattern differs: incompleteness adds new conditions; auth_scope clarifies existing permission boundaries. (c) Empirically testable: if they were the same, their violation patterns and failure modes (C5) would be indistinguishable. (d) Report disambiguation length ratio per type as control variable in §4 Method.\n\n### RC10: \"API sampling noise undermines reliability\"\n**Response**: ✅ RESOLVED. plan_006 ICC=0.919 [0.892, 0.940] (excellent). (a) Per-clause violation rates highly reproducible across 3 independent replicates. (b) Binary ICC=0.847 (good). (c) Both models show near-identical ICC (gpt-5.4: 0.921, gpt-4.1: 0.918). (d) Bootstrap CI + ICC double evidence. (e) Previously identified ±8pp noise is within expected variance given the ICC confidence intervals.\n\n### RC11: \"Prompt sensitivity confound\" [Dream A9 — best tier \"strongest point\"]\n**Concern**: The +35-42pp effect is attributed entirely to ambiguity, but without a control condition using non-ambiguity perturbations (synonym substitution, clause reordering), the paper cannot cleanly distinguish ambiguity-specific harm from general prompt brittleness.\n**Response**: ✅ RESOLVED. plan_010 perturbation control (120 episodes): Δ_perturb=3.33pp (CI contains 0) vs ambiguity Δ=36.5pp. Non-ambiguity surface changes cause zero meaningful effect. This is the strongest causal evidence in the agent safety literature.\n\n## Concept Naming (distill insight: 命名即贡献)\n\nCore phenomenon: **\"Differential Nocuity\"** — all policy ambiguity types are nocuous for LLM agents (+34.0pp, all 5 models), but vulnerability varies by BOTH type and model. Incompleteness is universally dangerous (46-62%), while auth_scope vulnerability depends dramatically on safety training (12% Claude to 64% GPT-5.4). Unlike human RE where organizational context renders most ambiguity innocuous, agents lack disambiguation channels AND their safety training creates type-specific blind spots.\n\nSecondary phenomenon: **\"Ambiguity Blindness\"** — agents process grammatically fluent ambiguous clauses without meta-cognitive awareness of the ambiguity, adopting surface interpretations. Contrasts with explicit rule conflicts where agents show awareness and choose conservatively.\n\nTertiary phenomenon: **\"Disambiguation Channel Framework\"** [renamed from \"Hypothesis\" per Dream review SF-5] — the layer hierarchy reflects availability of external disambiguation: linguistic ambiguity (coreferential, lexical) can sometimes be resolved by tool responses, user context, or world knowledge; specification ambiguity (auth_scope, incompleteness) has no external resolution channel, forcing agents to guess. This is an explanatory framework supported by observational evidence (ICC pattern, failure mode distribution, coreferential boundary case), not a tested causal hypothesis. Future Work: manipulation experiment (inject spec-layer disambiguation info into tool responses, test if gap shrinks).\n\nQuaternary phenomenon: **\"Systematic Nocuity\"** [per Dream review SF-7] — B&K framework distinguishes nocuous (divergent interpretations) from innocuous (convergent). Our data reveals a third type: all models converge on the same WRONG interpretation (27% of ambiguous episodes). This is more dangerous than divergent nocuity — it's invisible in inter-model agreement metrics and appears \"correct\" until compared against ground truth. Proposed as B&K extension in Discussion.\n\n## Opening Hook Strategy (distill insight: 具体案例, 不要 \"Recently...\")\n\nOpen with a concrete τ²-bench failure: e.g., a customer returns a customized item within the return window; the agent grants a full refund + free return shipping because the policy says \"items may be returned within 30 days\" (scopal: \"items\" scopes over all categories including custom). The unambiguous version specifies \"standard items only\" — agent correctly refuses. One word of ambiguity → $200 unauthorized refund.\n\n## Narrative Type: 突破局限型 (distill pattern, 5/8 papers)\n\n\"DRIP-R classifies 5 ambiguity types and shows models disagree on interpretation → but does not measure whether this disagreement leads to safety violations. We close this gap — and find the answer is surprising: not all types are equal, specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones.\"\n\n## Benchmark Comparison Table (distill insight: 必有 feature matrix)\n\n| Feature | DRIP-R | PhantomPolicy | PolicyBank | AgentPex | **Ours** |\n|---------|--------|---------------|------------|----------|----------|\n| Ambiguity taxonomy | 5 RE types | — | 3 gap types | — | **6 types (2-layer)** |\n| Causal design | — | — | — | — | **matched pairs** |\n| Safety violation metric | — | binary | — | procedural | **3-tier severity** |\n| Cross-type comparison | descriptive | — | — | — | **statistical (χ² + V)** |\n| Models tested | 6 API | 4 API | 2 API | 2 API | **3 API + 2 open-source** |\n| Domain | retail | mixed | retail | telecom/retail/airline | **retail + airline** |\n\n## Contribution Positioning (for EMNLP) [revised 2026-05-20 with 5-model data]\n\n1. **Causal quantification of ambiguity's safety impact**: First matched-pair causal study of policy ambiguity → agent safety violations. Binary effect +34.0pp (OR=15.1, p<0.0001) across 5 architecturally diverse models and 6 ambiguity types. Perturbation control (Δ_perturb=3.33pp) confirms ambiguity-specific causation. Strongest causal evidence in the agent safety literature.\n2. **Differential Nocuity framework + Model × Type Interaction**: Not all ambiguity is equally dangerous, and not all models are equally vulnerable. 3-tier type hierarchy (incompleteness >> mid cluster >> coreferential). Model × type interaction reveals 52pp range in auth_scope vulnerability (Claude 12% → GPT-5.4 64%), while incompleteness remains universally dangerous (46-62%). Safety training differentially mitigates specific ambiguity types. Connects Berry & Kamsties nocuous ambiguity theory to modern safety alignment.\n3. **Type-specific failure mode taxonomy + Ambiguity Blindness**: 245 traces across 2 models and 2 domains reveal type-diagnostic failure signatures: spec-layer → guess-and-act (unauthorized_escalation, assumption_based_action); ling-layer → misparse-and-apply (scope_misapplication). Agents show <5-11% awareness of ambiguity (\"Ambiguity Blindness\"), with >88% surface adoption and <1% user escalation. Practical implication: ambiguity detection must be externalized.\n\nNOTE: C3 (layer effect, Δ=6.08pp) is a component finding supporting contribution #2. The MODEL × TYPE interaction (C4) is now MORE central than the layer main effect. \"Disambiguation channel\" is an explanatory framework (not hypothesis — per SF-5). DeBERTa classifier, if included, is a preliminary PoC appendix, not a contribution.\n\n## Required Reference Expansion [Dream A2 + MF-4 RE literature gap]\n\nCurrent plan has thin references. Must add (≥25 total in final paper):\n- **Nocuous ambiguity detection (CRITICAL — MF-4)**: Chantree, Nuseibeh, de Roeck & Willis (2006, ASE) — first computational nocuous ambiguity detection; Chantree et al. (2008, RLAC) — expanded. Direct lineage to our DeBERTa classifier.\n- **Cross-domain RE ambiguity**: Ferrari, Spagnolo & Gnesi (2017-2019, ASE) — NLP-based cross-domain ambiguity detection. NLP4RE community work.\n- **Good-enough processing**: Ferreira, Bailey & Ferraro (2002); Ferreira & Patson (2007)\n- **LLM garden-path (SF-6)**: Li et al. (2024) — incremental comprehension of garden-path sentences by LLMs. Directly relevant to how LLMs process ambiguity.\n- **Anaphoric ambiguity (SF-6)**: Poesio & Artstein (2005, 2008) — annotation of anaphoric ambiguity. Poesio (2004) \"Ambiguity\" encyclopedia entry.\n- **Surprisal/expectation-based**: Levy (2008); Hale (2001)\n- **Instruction-following robustness**: Zhou et al. (IFEval, 2023); Qin et al. (ToolBench, 2024)\n- **Prompt sensitivity**: Sclar et al. (2024); Lu et al. (2022)\n- **Broader agent safety**: R-Judge, ToolEmu, InjecAgent\n- **Formal semantics of vagueness**: Lassiter & Goodman (2017)\n- **Garden-path**: Frazier & Rayner (1982)\n- **Ambiguity detection**: Willis et al. (2008); Ezzini et al. (TAPHSIR, 2022)\n- **Year verification needed**: Massey et al. — §1 引用 2013 vs 后文 2014, 需确认正确年份\n\n## Code/Data Release Plan [Dream A6 — three-tier consistent]\n\nMust commit to releasing:\n1. All 300 clause pairs (ambiguous + unambiguous variants) with type labels\n2. Evaluation scripts (τ²-bench integration, cross-judge pipeline)\n3. Statistical analysis code (all tests, bootstrap CI computation)\n4. Agent trace samples (anonymized) for reproducibility of C5\n\n## Figure Plan [Dream A12]\n\nMinimum figures for paper (zero-figure paper flagged in dream):\n1. **Figure 1**: System architecture / experimental pipeline overview (§4 Method)\n2. **Figure 2**: Forest plot — per-type binary effect sizes with 95% CI (§5 C1)\n3. **Figure 3**: Model × Type heatmap — violation rates across 4 models × 6 types (§5 C4)\n4. **Figure 4**: Visibility mechanism — CP vs scopal violation rates + trace evidence (§5 C3)\n5. **Figure 5**: Failure mode × type stacked bar/Sankey — per-type failure mode distribution (§6 C5)\n6. **Figure 6**: Cross-model failure mode consistency — side-by-side gpt-5.4 vs gpt-4.1 per-type distributions showing 5/6 convergence (§6 C5, supports C4)\n7. **Figure 7**: Annotated trace pair — CP (conflict detection) vs scopal (surface adoption) (§6 C5)\n\n## Berry & Kamsties Operationalization Note [Dream best Q5]\n\nBerry & Kamsties define nocuity as inter-reader divergence. Our design measures agent-vs-intent deviation. Full study should additionally test whether different models adopt different readings of the same ambiguous clause (true inter-model nocuity). If 4 models produce 4 different interpretations of the same clause → true nocuity. If all 4 adopt the same wrong interpretation → systematic bias, still nocuous but for different reason. Report inter-model agreement on ambiguous clauses as supplementary analysis.\n\n## Contingency Framing [RESOLVED — Scenario C occurred]\n\n> plan_002 结果: Scenario C 发生（omnibus p=0.0001, 所有类型 nocuous 但 severity 有显著差异）。\n> Framing 已 pivot 到 \"Differential Nocuity\" + \"Layer Hierarchy\" (D020)。本节仅保留历史记录。\n\n## Claude Baseline — RESOLVED [2026-05-20]\n\n✅ Claude works via OpenRouter proxy (47.94.22.126/v1) with provider prefix `anthropic/claude-sonnet-4-6`. 600 episodes complete (plan_002c). Claude shows lowest overall vulnerability (30.3%) and remarkable auth_scope robustness (12% vs GPT-5.4 64%).\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: full_study_clause_generation\n  claim: C1, C2, C3\n  description: 'Generate remaining clauses for full study: coreferential (50 new),\n    authorization_scope (50 new), lexical (+20 to reach 50), incompleteness (+20 to\n    reach 50). Total 140 new clauses. Validate all 300 clauses (50/type × 6 types)\n    for completeness and cross-type balance. Mix CP format per Reviewer suggestion\n    (labeled + unlabeled).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n- id: plan_001b\n  name: new_type_mini_pilot\n  claim: C1 (validation)\n  description: 'Mini-pilot for coreferential + authorization_scope (never tested):\n    5 clauses/type × 2 conditions × 1 model (gpt-5.4) = 20 episodes. Verify: (a) ambiguous\n    triggers violations (b) unambiguous control < 15%. If systematic issues found,\n    fix clause design before full study. API cost negligible (~$2). Per Reviewer warning\n    on untested types.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_002\n  name: full_study_api\n  claim: C1, C2, C3, C4, C5\n  description: 'Run 300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6)\n    = 1,800 episodes on τ²-bench. Cross-judge evaluation. Output: episodes.jsonl +\n    judgments.jsonl. No GPU needed. Claude via OpenRouter proxy (base_url=http://47.94.22.126/v1).\n    [2026-05-20] Claude added per distill gap (4/8 papers use Claude baseline).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_001b\n  - plan_010\n  status: planned\n- id: plan_003\n  name: full_study_opensource\n  claim: C1, C2, C3, C4, C5\n  description: 'Run 300 clauses × 2 conditions × 2 open-source models via OpenRouter\n    API: qwen/qwen3-235b-a22b (235B MoE, Alibaba) + deepseek/deepseek-chat-v3-0324\n    (DeepSeek) = 1,200 episodes on τ²-bench. Cross-judge uses API models. Can run\n    in parallel with plan_002. No GPU needed. [2026-05-20] Pivoted from local GPU\n    → API: OpenRouter proxy confirmed to support Qwen3 and DeepSeek models. Eliminates\n    48h GPU requirement. Provider prefix required (e.g. qwen/qwen3-235b-a22b, not\n    qwen3-235b-a22b).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_004\n  name: full_study_analysis\n  claim: C1, C2, C3, C4\n  description: 'Statistical analysis of full study data (3,000 episodes): (a) Binary\n    effect per type with bootstrap CI (C1) (b) Omnibus χ² + pairwise across 6 types\n    (C2) (c) Visibility comparison: CP vs scopal rates (C3) (d) Model × type interaction:\n    5×6 contingency + logistic regression (C4) Report effect sizes + CI for all comparisons\n    per Reviewer suggestion. [Dream A3] Power analysis: report MDE for C2 (given N=250/type\n    pooled) and C3 (given N=250 per type). If V < 0.20 but MDE > observed V, discuss\n    underpowered possibility. [Dream A4] TOST equivalence test with both ±15pp and\n    ±10pp margins. Justify margin choice explicitly. [Dream A10] Report per-type information\n    delta (token count difference between ambiguous and unambiguous variants) as control\n    variable. [Dream B&K] Inter-model agreement on ambiguous clauses: do 5 models\n    adopt same or different interpretations? (supplementary analysis)\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_005\n  name: error_analysis\n  claim: C5\n  description: \"Qualitative analysis of agent traces from full study: (a) Sample 50\\\n    \\ violation traces per type (300 total) (b) Classify failure modes (scope misapplication,\\\n    \\ conservative refusal,\\n    assumption-based action, arbitrary rule selection,\\\n    \\ etc.)\\n(c) Cross-type failure mode distribution (d) Visibility mechanism: compare\\\n    \\ CP traces (explicit conflict detection\\n    behavior) vs scopal traces (surface\\\n    \\ scope adoption without awareness)\\n(e) Model-specific failure patterns (connect\\\n    \\ to C4)\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_006\n  name: reliability_test\n  claim: C1, C2\n  description: 'Test-retest reliability: select 30 representative clauses (5/type),\n    run 3 independent replicates × 2 conditions × 2 API models (gpt-5.4, gpt-4.1)\n    = 360 episodes. Local models added when plan_003 GPU available. Compute ICC for\n    per-clause violation rates. Addresses Reviewer warning about ±8pp sampling noise\n    (scopal 51.7% → 43.3% across MVP/diag). Bootstrap CI width should be < 10pp for\n    key comparisons. [2026-05-20] API portion: 330/360 episodes complete (28/30 clauses),\n    judgments pending.\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  status: planned\n- id: plan_007\n  name: realism_validation\n  claim: C1 (methodological)\n  description: \"Validate synthetic ambiguity injection realism: (a) Linguistic property\\\n    \\ comparison with DRIP-R natural ambiguities\\n    (sentence length, parse depth,\\\n    \\ Flesch-Kincaid, TTR) + KS tests\\n(b) Optional: discriminator test if DRIP-R\\\n    \\ data accessible Addresses RC4 (ecological validity).\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_009\n  name: judge_calibration\n  claim: C1 (methodological)\n  description: 'LLM-as-judge calibration per distilled research norm (5/8 papers):\n    (a) Sample 100 episodes stratified by type×model×condition (b) Human expert labels\n    (2 annotators, target κ ≥ 0.75) (c) Compute judge precision/recall/F1 against\n    human ground truth (d) Per-severity-tier agreement rates (e) Report in Method\n    section as standard practice per AgentAuditor/DRIP-R [Dream A7] Upgraded P1→P0:\n    Dream best-tier reviewers identified this as \"single most critical missing validation.\"\n    Without it, entire measurement chain from episode to violation label is unvalidated.\n    κ=0.91 measures LLM-LLM agreement, not accuracy.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  name: perturbation_control\n  claim: C1 (causal validity)\n  description: '[Dream A9] Non-ambiguity perturbation control arm to distinguish ambiguity-specific\n    harm from general prompt brittleness. Generate 30 clause pairs with non-ambiguity\n    perturbations: (a) 15 synonym substitution pairs (replace key terms with synonyms)\n    (b) 15 clause reordering pairs (reorder conditions without changing meaning) Run\n    30 × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6) = 180 episodes.\n    Key metric: Δ_net = Δ_ambiguity - Δ_perturb (net ambiguity-specific effect). [Reviewer升级]\n    必须在 plan_002/003 full study 之前完成—— 如果 perturbation Δpp ≈ ambiguity Δpp，2,400 episodes\n    全部无效。 低成本验证（30 pairs + 120 episodes API）优先于高成本投入。 [判定标准 — 5 档]: PASS: Δ_perturb\n    < 5pp (CI含0), ratio < 0.15 → C1 因果 claim 最强形式 PASS+caveat: 5-10pp, ratio 0.15-0.30\n    → 报告 perturbation baseline, C1 写 net effect CONDITIONAL: 10-15pp, ratio 0.30-0.45\n    → 需 Δ_net > 20pp 且显著才可发表 WARNING: 15-20pp, ratio 0.45-0.60 → C1 改为 \"additional\n    violations beyond sensitivity\" FAIL: > 20pp, ratio > 0.60 → 无法声称 ambiguity-specific,\n    需根本重新设计 [Power 注意]: N=120 对 10pp 差异 power ≈ 30%. 用 CI 宽度判定, 非 p-value. 若 CI 过宽(>15pp\n    width), 追加 60 episodes 压窄至 <10pp width. 输出标准化 verdict 文件: perturbation_Δpp, ambiguity_Δpp,\n    net_Δpp, CI, ratio, verdict.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_017\n  name: sopbench_cross_benchmark\n  claim: C1 (generalizability), C2 (partial)\n  description: 'Cross-benchmark C1 replication on SOPBench (Li et al., 2025). 7 domains\n    (Bank, DMV, Healthcare, Hotel, Library, University, Online Market) all different\n    from τ²-bench (retail + airline). Select 2 domains (Healthcare + Bank) for maximum\n    domain diversity. Construct 100 clause pairs (50/domain) covering 3-4 ambiguity\n    types (incompleteness, auth_scope, lexical, conditional_precedence) from SOPBench''s\n    NL SOP constraints. Run 100 pairs × 2 conditions × 5 models = 1,000 episodes.\n    SOPBench has rule-based verifier — no LLM judge needed. Key metrics: (a) Does\n    C1 binary effect replicate? (b) Is incompleteness still highest-risk type? (c)\n    Cross-benchmark effect size correlation. Addresses SF-8 (single benchmark external\n    validity). Result goes in Appendix with 1-sentence summary in main text. [2026-05-22]\n    Approved by user. Estimated 1 day including clause construction.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n- id: plan_008\n  name: classifier_poc\n  claim: practical contribution\n  description: 'Binary ambiguity detector PoC: fine-tune DeBERTa-v3-large on annotated\n    clause pairs (ambiguous/unambiguous labels). Eval on held-out set. Demonstrates\n    practical applicability of findings. Phase 3 from IDEA_BRIEF, scoped to PoC for\n    EMNLP.\n\n    '\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: diag_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_002\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_006\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_009\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cross_judge_kappa_weighted: 0.685\n    cross_judge_exact_agreement: 0.76\n    cross_judge_binary_kappa: 0.74\n    human_llm_pooled_kappa_weighted: 0.807\n    human_inter_annotator_kappa_weighted: 0.762\n    n_episodes: 100\n- exp_id: plan_002c\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_003a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_003b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_004\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_010\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_violations_coded: 614\n    types_unanimous_dominant_fm: 3/6\n    types_majority_dominant_fm: 6/6\n    inter_coder_kappa: 0.5173\n    percent_agreement: 0.656\n    disambiguation_awareness_overall: 0.046\n    elapsed_seconds: 98.5\n- exp_id: plan_011\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_delta_pp: -6.6\n    overall_baseline: 0.41\n    overall_mitigated: 0.343\n    auth_scope_delta_pp: -18\n    incompleteness_delta_pp: -3.4\n    lexical_delta_pp: -8.9\n    cond_prec_delta_pp: -8.1\n    scopal_delta_pp: -4.3\n    best_model_gpt41_delta_pp: -11.1\n    worst_model_deepseek_delta_pp: -2.5\n    total_mitigated_episodes: 1256\n    total_baseline_episodes: 1499\n    elapsed_seconds: 2954\n- exp_id: plan_012\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1: 0.6322\n    binary_f1: 0.8055\n    binary_fpr: 0.044\n    best_type_f1:\n      conditional_precedence: 0.94\n    worst_type_f1:\n      incompleteness: 0.34\n    per_type_f1:\n      conditional_precedence: 0.94\n      scopal: 0.75\n      coreferential: 0.7\n      authorization_scope: 0.58\n      lexical: 0.39\n      incompleteness: 0.34\n    total_clauses: 500\n    folds: 5\n- exp_id: plan_013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gemini_2.5_flash:\n      amb_rate: 0.376\n      unamb_rate: 0.04\n      delta_pp: 33.6\n      or: 14.46\n      p_value: 4.0e-22\n      c1_replicates: true\n      c2_rank_corr: 0.6\n      c2_rank_p: 0.285\n      type_ranking:\n      - lexical\n      - incompleteness\n      - scopal\n      - cond_prec\n      - auth_scope\n    llama_4_scout:\n      amb_rate: 0.376\n      unamb_rate: 0.176\n      delta_pp: 20\n      or: 2.82\n      p_value: 7.7e-07\n      c1_replicates: true\n      c2_rank_corr: 0.9\n      c2_rank_p: 0.037\n      type_ranking:\n      - incompleteness\n      - auth_scope\n      - lexical\n      - scopal\n      - cond_prec\n    summary:\n      c1_replicated: 7/7\n      c2_replicated: 2/2 positive (LLaMA ρ=0.90 p=0.037, Gemini ρ=0.60 p=0.285)\n      incompleteness_universal: 7/7 (≥46%)\n      total_episodes: 1000\n    bugfix: reference_rank corrected from arbitrary order to main-study pooled descending;\n      OR inverted\n- exp_id: plan_014\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_episodes: 300\n    delta_perturb_pp: -0.67\n    ci_95_bootstrap:\n    - -8\n    - 6.67\n    ci_upper_bound: 6.67\n    ci_width: 14.67\n    mcnemar_p: 1\n    verdict: PASS\n    plan_010_ci_upper: 13.33\n    ci_upper_reduction: 6.66\n- exp_id: plan_015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pooled_escalation_rate: 0.692\n    pooled_restriction_rate: 0\n    binomial_p: 5.5e-05\n    models_majority_escalation: 4/5\n    n_total: 104\n    n_escalation: 72\n- exp_id: plan_016\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    generic_awareness_overall_delta_pp: 1.33\n    type_specific_auth_scope_delta_pp: -12\n    type_specific_auth_scope_p: 0.07\n    type_specific_incompleteness_delta_pp: 14\n    type_specific_incompleteness_p: 0.118\n    type_specific_lexical_delta_pp: -2\n    type_specific_lexical_p: 1\n    total_new_episodes: 450\n    total_judge_calls: 450\n    model: gpt-5.4\n    all_mcnemar_p_gt_005: true\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n\n重要：tables 中使用 YAML flow sequence 时，所有字符串必须加双引号（如 `columns: [\"Judge\", \"Biased?\"]`），否则 `?` `:` 等字符会导致解析失败。\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-22T11:30:11.015Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T11:30:11.015Z",
  "sessionId": "a995b27a-21cd-4926-acb4-3043954b7476"
}
```

---

## Round 1

12 recorded events

### User

_source line 3 · 2026-05-22T11:30:11.036Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：SOPBench不复制或verifier不兼容，需放弃cross-benchmark claim，用deep single-benchmark causal rigor + model diversity重新定位
核心假设：['SOPBench C1不复制（Δ<15pp或p>0.05）或rule-based verifier与ambiguity injection不兼容（verifier无法区分ambiguity-induced violations vs correct behavior）', '类型排序与τ²-bench无相关或负相关（ρ<0.3），暗示type hierarchy是benchmark-specific artifact', 'C3 layer effect在审稿中被challenge为model composition artifact（GPT drives the gap）', '至少一位审稿人认为synthetic injection + single primary benchmark = insufficient external validity', '但C1在τ²-bench的5-model +34pp效应、perturbation control、7-model扩展（plan_013）仍intact', 'judge calibration κ=0.807仍强，causal design仍是literature最强']
关键指标范围：{'sopbench_c1_delta_pp': [0, 15], 'sopbench_type_rank_rho': [-0.2, 0.3], 'sopbench_incompleteness_rate': [0.2, 0.4], 'cross_benchmark_effect_correlation': [-0.1, 0.4], 'expected_review_avg': [2.5, 3.0], 'claims_surviving_without_revision': [1, 2]}
叙事方向：放弃cross-domain generalization claim。不报告SOPBench（或一句话acknowledge未复制作为limitation）。Reframe核心贡献为：(1) methodological——首个matched-pair + perturbation control因果设计，是agent safety评估的方法论模板；(2) model×type interaction——即使限于customer-service domain，52pp auth_scope range + incompleteness universality是safety alignment的actionable insight；(3) 7-model breadth（plan_013: Gemini+LLaMA也复制C1）替代cross-benchmark breadth。叙事从'cross-domain law'转为'深度因果剖析揭示safety training盲区'——强调因果rigor超越correlation-based prior work（DRIP-R, PhantomPolicy）。Title可能需改：去掉任何暗示generality的词，改为'Causal Anatomy of Policy Ambiguity Vulnerability in LLM Agents'。仍冲EMNLP——causal method + interaction finding + 7 models足够，只是framing更modest。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

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

重要：tables 中使用 YAML flow sequence 时，所有字符串必须加双引号（如 `columns: ["Judge", "Biased?"]`），否则 `?` `:` 等字符会导致解析失败。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "eaff2207-4775-4863-9dc3-77a86a3667bd",
  "type": "user",
  "uuid": "ce6fc3a0-f552-4304-917c-d39fa00e5dab",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "a995b27a-21cd-4926-acb4-3043954b7476",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T11:30:11.034Z_

```json
{
  "parentUuid": "ce6fc3a0-f552-4304-917c-d39fa00e5dab",
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
  "uuid": "2dd3f69e-095f-4579-b904-ae21429441ce",
  "timestamp": "2026-05-22T11:30:11.034Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "a995b27a-21cd-4926-acb4-3043954b7476",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T11:30:11.034Z_

```json
{
  "parentUuid": "2dd3f69e-095f-4579-b904-ae21429441ce",
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
  "uuid": "c2d009e1-15d4-491c-9223-7cc9bf2154af",
  "timestamp": "2026-05-22T11:30:11.034Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "a995b27a-21cd-4926-acb4-3043954b7476",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-22T11:30:11.034Z_

```json
{
  "parentUuid": "c2d009e1-15d4-491c-9223-7cc9bf2154af",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "7a0fc428-23d9-441b-913c-a915ed35cedc",
  "timestamp": "2026-05-22T11:30:11.034Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "a995b27a-21cd-4926-acb4-3043954b7476",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：SOPBench不复制或verifier不兼容，需放弃cross-benchmark claim，用deep single-benchmark causal rigor + model diversity重新定位 核心假设：['SOPBench C1不复制（Δ<15pp或p>0.05）或rule-based…",
  "leafUuid": "7a0fc428-23d9-441b-913c-a915ed35cedc",
  "sessionId": "a995b27a-21cd-4926-acb4-3043954b7476"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Causal anatomy of policy ambiguity under worst-case replication",
  "sessionId": "a995b27a-21cd-4926-acb4-3043954b7476"
}
```

---

### Assistant

_source line 9 · 2026-05-22T11:30:49.939Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for all "planned" experiments in the experiment_plan, under the "worst" tier scenario. Let me identify all planned experiments:

1. plan_001 - full_study_clause_generation
2. plan_001b - new_type_mini_pilot
3. plan_002 - full_study_api (but wait, registry shows plan_002 as DONE... let me check)

Actually, looking more carefully at the registry vs experiment_plan:


- Registry shows plan_002, plan_005, plan_006, plan_009, plan_002c, plan_003a, plan_003b, plan_004, plan_010, plan_011, plan_012, plan_013, plan_014, plan_015, plan_016 as DONE

But the experiment_plan still lists many as "planned". Let me look at which ones have status: planned in the experiment_plan:
- plan_001: planned
- plan_001b: planned
- plan_002: planned
- plan_003: planned
- plan_004: planned
- plan_005: planned
- plan_006: planned
- plan_007: planned
- plan_009: planned
- plan_010: planned
- plan_017: planned

So there's a discrepancy between what the registry marks as DONE and what the experiment_plan still lists as planned. I need to focus on the experiment_plan's status field and generate worst-case predictions for all those marked as planned. I need to figure out which experiments are actually still planned versus already completed. Looking at the registry, I can see that several experiments have been executed—mvp_001, diag_001, plan_002, plan_005, plan_006, plan_009—so I should focus on predicting worst-tier results only for the ones that haven't been done yet. The user wants detailed data for the planned experiments under that worst-case scenario narrative. Looking at the experiment plan, I need to generate worst-tier predictions for all the experiments marked as "planned" — which appears to be all of them. The worst-tier scenario has specific constraints: SOPBench fails to replicate, type ranking shows no correlation with τ²-bench, the C3 layer effect gets challenged as a model composition artifact, and at least one reviewer questions external validity. However, the C1 performance on τ²-bench with five models still shows that +34pp improvement, and judge calibration remains strong at κ=0.807. Now I'm working through what these worst-case metrics would look like across the key measurement ranges. Looking at how each experiment holds up under worst-case conditions: the core clause generation and API studies still succeed since C1 remains robust, the open-source replication works, and the statistical analysis confirms C1 and C2 while C3 becomes fragile. The qualitative and reliability work proceed as planned, though I need to assess what happens with the remaining validation experiments.

The critical failure point is the cross-benchmark validation against SopBench—under worst tier, C1 either doesn't replicate with meaningful effect size or the rule-based verifier becomes incompatible with the synthetic data. The classifier proof-of-concept still functions but becomes less central to the narrative. Now I'm working through detailed predictions for each plan under this worst-case scenario.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7a0fc428-23d9-441b-913c-a915ed35cedc",
  "isSidechain": false,
  "requestId": "req_011CbHXjrYkKaJPidQq6srDt",
  "type": "assistant",
  "uuid": "26ce57da-2726-4eac-84c9-3fcaba0d1c77",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "a995b27a-21cd-4926-acb4-3043954b7476",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GmcBMk82b51xBBVXDY2rnA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21210,
      "cache_read_input_tokens": 11447,
      "output_tokens": 13566,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21210,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 13566,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 21210,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21210
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

_source line 10 · 2026-05-22T11:34:40.874Z_

```yaml
tier: worst
narrative_guidance: "放弃cross-domain generalization claim。SOPBench未复制或verifier不兼容，一句话acknowledge作为limitation。核心贡献重新定位为：(1) 方法论模板——首个matched-pair + perturbation control因果设计；(2) model×type interaction——52pp auth_scope range + incompleteness universality；(3) 7-model breadth（plan_013 Gemini+LLaMA复制C1）替代cross-benchmark breadth。Title改为'Causal Anatomy of Policy Ambiguity Vulnerability in LLM Agents'。仍冲EMNLP但framing更modest。"
imagined_experiments:
  - name: full_study_clause_generation
    plan_id: plan_001
    description: "生成140新clause pairs（coreferential 50, auth_scope 50, lexical +20, incompleteness +20），总计300 pairs validated"
    expected_results:
      total_clauses_generated: 300
      per_type_count: 50
      cross_type_balance_pass: true
      format_mix_cp_labeled_ratio: 0.5
      avg_token_delta_spec_layer: 34.2
      avg_token_delta_ling_layer: 12.8
      quality_review_pass_rate: 0.92
      revision_needed_clauses: 24
    result_rationale: "Clause generation是upstream工序，不受worst tier影响。质量审查会发现~8%需修订（auth_scope边界case和incompleteness minimal-info约束难满足）。Token delta的layer差异（spec 34 vs ling 13）是固有结构——specification层歧义消解需要更多信息量，这在后续分析中成为confound讨论点但不改变因果结论。"
    tables:
      - title: "Clause Generation Summary by Type"
        columns: ["Type", "Layer", "N Generated", "N Passed QA", "Avg Token Delta", "Revision Rate"]
        rows:
          - ["incompleteness", "spec", "50", "46", "34.6", "0.08"]
          - ["authorization_scope", "spec", "50", "44", "36.1", "0.12"]
          - ["conditional_precedence", "spec", "50", "48", "31.9", "0.04"]
          - ["scopal", "ling", "50", "47", "14.2", "0.06"]
          - ["lexical", "ling", "50", "47", "16.3", "0.06"]
          - ["coreferential", "ling", "50", "45", "7.8", "0.10"]
    figures_description:
      - "Token delta distribution boxplot by type — spec-layer clauses显示更长的disambiguation tokens (median 34 vs 13), 支持info delta as mediator但不消除condition effect"
    analysis: "Clause generation成功完成。Auth_scope和coreferential作为首次生成的类型，revision rate略高（10-12%），主要问题是auth_scope边界条件过于subtle（unambiguous版本仍可能被误读）和coreferential的RC attachment需确保不与scopal overlap。生成质量不影响worst tier结论——downstream SOPBench失败是verifier/domain层面的问题，非clause质量问题。"

  - name: new_type_mini_pilot
    plan_id: plan_001b
    description: "Coreferential + auth_scope mini-pilot: 5 clauses/type × 2 conditions × 1 model (gpt-5.4) = 20 episodes"
    expected_results:
      coreferential_amb_violation_rate: 0.40
      coreferential_unamb_violation_rate: 0.08
      auth_scope_amb_violation_rate: 0.60
      auth_scope_unamb_violation_rate: 0.04
      systematic_issues_found: 0
      proceed_to_full_study: true
      total_episodes: 20
      api_cost_usd: 1.8
    result_rationale: "Mini-pilot在τ²-bench上验证新类型，C1效应在τ²-bench上intact（worst tier核心假设）。GPT-5.4对auth_scope高度脆弱（main study 64%），mini-pilot sample虽小但会观察到强效应。Coreferential是最低violation type但仍显著高于baseline。N=5太小无法精确估计，但足以确认方向正确（>15pp gap）和unambiguous control < 15%。这些结果不受SOPBench失败影响。"
    tables:
      - title: "Mini-Pilot Results"
        columns: ["Type", "Condition", "N", "Violations", "Rate", "Pass Criteria"]
        rows:
          - ["auth_scope", "ambiguous", "5", "3", "0.60", "triggers violations: YES"]
          - ["auth_scope", "unambiguous", "5", "0", "0.00", "control < 15%: YES"]
          - ["coreferential", "ambiguous", "5", "2", "0.40", "triggers violations: YES"]
          - ["coreferential", "unambiguous", "5", "0", "0.00", "control < 15%: YES"]
    figures_description: []
    analysis: "两个新类型均通过验证——ambiguous条件触发violations且unambiguous control干净。Auth_scope的60%与main study gpt-5.4的64%一致。可进入full study。"

  - name: full_study_api
    plan_id: plan_002
    description: "300 clauses × 2 conditions × 3 API models = 1,800 episodes on τ²-bench"
    expected_results:
      total_episodes: 1800
      overall_amb_violation_rate: 0.387
      overall_unamb_violation_rate: 0.047
      overall_delta_pp: 34.0
      mcnemar_or: 15.1
      mcnemar_p: "<0.0001"
      gpt54_delta_pp: 38.3
      gpt41_delta_pp: 34.7
      claude_delta_pp: 25.7
      per_type_incompleteness_rate: 0.536
      per_type_auth_scope_rate: 0.416
      per_type_coreferential_rate: 0.316
      bootstrap_ci_overall: [31.2, 36.9]
      cross_judge_agreement: 0.76
    result_rationale: "Worst tier明确保留τ²-bench C1效应（+34pp, 5 models intact）。三个API模型的效应与已完成registry数据一致。Claude最低（25.7pp）因其auth_scope robustness，GPT-5.4最高（38.3pp）因auth_scope极度脆弱。这些结果是paper的核心evidence base，不受SOPBench cross-benchmark失败影响。worst tier的损失在于这些强结果无法被cross-domain claim放大。"
    tables:
      - title: "Full Study API Results by Model"
        columns: ["Model", "Amb Rate", "Unamb Rate", "Delta pp", "OR", "p-value", "Bootstrap CI"]
        rows:
          - ["gpt-5.4", "0.443", "0.060", "+38.3", "12.4", "<10^-20", "[34.1, 42.5]"]
          - ["gpt-4.1", "0.407", "0.060", "+34.7", "10.8", "<10^-18", "[30.2, 39.2]"]
          - ["claude-sonnet-4-6", "0.303", "0.047", "+25.7", "8.9", "<10^-15", "[21.0, 30.3]"]
          - ["Pooled", "0.384", "0.056", "+32.9", "10.5", "<10^-40", "[30.2, 35.6]"]
      - title: "Per-Type Violation Rates (Ambiguous Only, 3 API Models Pooled)"
        columns: ["Type", "Violation Rate", "95% CI", "N"]
        rows:
          - ["incompleteness", "0.507", "[0.44, 0.57]", "150"]
          - ["authorization_scope", "0.407", "[0.34, 0.47]", "150"]
          - ["lexical", "0.427", "[0.36, 0.49]", "150"]
          - ["scopal", "0.373", "[0.31, 0.44]", "150"]
          - ["conditional_precedence", "0.367", "[0.30, 0.43]", "150"]
          - ["coreferential", "0.240", "[0.18, 0.30]", "150"]
    figures_description:
      - "Forest plot showing per-model per-type effect sizes with 95% CI — all positive, no overlap with zero"
    analysis: "τ²-bench full study完整复制pilot结果。C1 binary effect +34pp across 3 API models robust。但在worst tier下，这些结果局限于retail+airline两个domain，无法通过SOPBench扩展到healthcare/bank。paper必须明确scope limitation。"

  - name: full_study_opensource
    plan_id: plan_003
    description: "300 clauses × 2 conditions × 2 open-source models (Qwen3-235B, DeepSeek-V3) = 1,200 episodes via OpenRouter"
    expected_results:
      total_episodes: 1200
      qwen3_amb_rate: 0.431
      qwen3_unamb_rate: 0.100
      qwen3_delta_pp: 33.1
      qwen3_or: 6.9
      qwen3_p: "<10^-17"
      deepseek_amb_rate: 0.497
      deepseek_unamb_rate: 0.107
      deepseek_delta_pp: 39.0
      deepseek_or: 8.3
      deepseek_p: "<10^-20"
      qwen3_auth_scope_rate: 0.26
      deepseek_auth_scope_rate: 0.60
      qwen3_incompleteness_rate: 0.62
      deepseek_incompleteness_rate: 0.54
    result_rationale: "Open-source模型在τ²-bench上复制C1（worst tier假设C1 intact）。DeepSeek表现为最脆弱模型（49.7% overall），因其safety training对所有type均匀不足（χ²=6.31, p=0.277, non-significant type differentiation）。Qwen3 incompleteness异常高（62%）但auth_scope相对低（26%），显示不同于GPT的vulnerability profile。这些结果支撑C4 model×type interaction——worst tier的核心可保留贡献。"
    tables:
      - title: "Open-Source Model Results"
        columns: ["Model", "Architecture", "Amb Rate", "Unamb Rate", "Delta pp", "OR", "Type χ²", "Type p"]
        rows:
          - ["Qwen3-235B", "MoE", "0.431", "0.100", "+33.1", "6.9", "15.89", "0.007"]
          - ["DeepSeek-V3", "Dense", "0.497", "0.107", "+39.0", "8.3", "6.31", "0.277"]
      - title: "Model × Type Interaction Matrix (Open-Source, Ambiguous Only)"
        columns: ["Type", "Qwen3", "DeepSeek"]
        rows:
          - ["incompleteness", "62%", "54%"]
          - ["lexical", "52%", "54%"]
          - ["auth_scope", "26%", "60%"]
          - ["scopal", "37%", "48%"]
          - ["cond_prec", "40%", "38%"]
          - ["coreferential", "42%", "44%"]
    figures_description:
      - "Model vulnerability profile radar chart — DeepSeek近圆形（uniform vulnerability），Qwen3 shows spikes at incompleteness/lexical"
    analysis: "Open-source模型确认C1 universality和C4 differential profiles。DeepSeek的uniform high vulnerability（6pp range across types）与Claude的strong differentiation（52pp range）形成对比，支撑safety training selectivity论点。在worst tier叙事下，5-model breadth（加上plan_013的Gemini+LLaMA = 7 models）替代cross-benchmark breadth作为generalizability evidence。"

  - name: full_study_analysis
    plan_id: plan_004
    description: "3,000 episodes统计分析: C1 binary effect, C2 type hierarchy, C3 layer effect, C4 model×type interaction"
    expected_results:
      c1_pooled_delta_pp: 34.0
      c1_pooled_or: 15.1
      c1_ci: [10.78, 21.17]
      c1_p: "<0.0001"
      c2_omnibus_chi2: 28.02
      c2_omnibus_p: 0.000036
      c2_cramer_v: 0.137
      c2_power: 0.993
      c2_mde: 0.093
      c2_tost_equiv_15pp: "8/15 equivalent"
      c2_tost_equiv_10pp: "4/15 equivalent"
      c3_spec_vs_ling_delta_pp: 6.08
      c3_p: 0.017
      c3_within_judge_gpt54_p: 0.059
      c3_within_judge_gpt41_p: 0.157
      c4_model_main_chi2: 31.02
      c4_model_main_p: 0.000003
      c4_model_v: 0.102
      c4_auth_scope_range_pp: 52
      c4_incompleteness_range_pp: 16
      c4_fleiss_kappa: 0.384
      logistic_condition_coef: 2.278
      logistic_condition_z: 19.65
      logistic_token_delta_coef: 0.022
      logistic_token_delta_z: 3.49
      info_delta_mediates: "partial (does not eliminate condition effect)"
      inter_model_agreement_amb: "models partially converge — 27% systematic nocuity (same wrong answer)"
    result_rationale: "统计分析确认C1-C4在τ²-bench上的full results。C3 within-judge fragility（p=0.059和0.157）在worst tier下被reviewer challenge为model composition artifact——GPT models drive the gap通过high auth_scope。但C4 interaction（52pp range）is the star finding且不需C3 main effect支撑。V=0.137 for C2 below 0.20 threshold但well-powered（MDE=0.093 < observed 0.137），3-tier structure defensible。Worst tier的关键问题不在这些内部统计——而是这些结果无法推广到τ²-bench之外（SOPBench失败）。"
    tables:
      - title: "C1-C4 Summary Statistics"
        columns: ["Claim", "Test", "Statistic", "p-value", "Effect Size", "Verdict"]
        rows:
          - ["C1 Binary", "McNemar", "OR=15.1", "<0.0001", "+34.0pp", "CONFIRMED"]
          - ["C2 Type", "Omnibus χ²", "28.02", "3.6e-5", "V=0.137", "CONFIRMED (small)"]
          - ["C3 Layer", "χ²", "5.73", "0.017", "Δ=6.08pp", "SUGGESTIVE (fragile within-judge)"]
          - ["C4 Model×Type", "χ²", "31.02", "3.0e-6", "V=0.102", "CONFIRMED (star finding)"]
      - title: "TOST Equivalence Results (±15pp margin)"
        columns: ["Pair", "Observed Δ", "TOST p", "Verdict"]
        rows:
          - ["incomp vs coref", "22.0pp", ">0.05", "NON-EQUIVALENT"]
          - ["incomp vs cond_prec", "16.8pp", ">0.05", "NON-EQUIVALENT"]
          - ["incomp vs scopal", "14.2pp", "0.048", "BORDERLINE"]
          - ["lexical vs scopal", "3.4pp", "<0.001", "EQUIVALENT"]
          - ["auth_scope vs cond_prec", "4.8pp", "0.003", "EQUIVALENT"]
          - ["lexical vs auth_scope", "1.2pp", "<0.001", "EQUIVALENT"]
          - ["scopal vs cond_prec", "2.6pp", "<0.001", "EQUIVALENT"]
          - ["coreferential vs any mid", ">5pp", "varies", "NON-EQUIVALENT at ±10pp"]
      - title: "Power Analysis"
        columns: ["Comparison", "N per group", "MDE (V)", "Observed V", "Power", "Assessment"]
        rows:
          - ["C2 6-type omnibus", "250/type pooled", "0.093", "0.137", "0.993", "Well-powered"]
          - ["C3 2-layer", "750/layer", "0.072", "0.062", "0.68", "Underpowered for observed effect"]
          - ["C4 5-model", "600/model", "0.081", "0.102", "0.95", "Adequate"]
    figures_description:
      - "Heatmap: 5 models × 6 types violation rates, with auth_scope column showing dramatic gradient (12% blue to 64% red)"
      - "Forest plot: per-type binary effect with 95% CI, ordered by magnitude"
    analysis: "τ²-bench内部分析全部intact。C3 fragility在worst tier被reviewer攻击但不致命——paper已将C3降为'suggestive'且C4 interaction supersedes it。核心问题：reviewer指出single benchmark + synthetic injection = insufficient external validity，而SOPBench本该解决这个问题却失败了。Paper必须承认scope limitation并用7-model breadth + perturbation control的methodological rigor来compensate。"

  - name: error_analysis
    plan_id: plan_005
    description: "300 violation traces qualitative analysis: failure mode classification, Ambiguity Blindness, cross-type/cross-model patterns"
    expected_results:
      total_traces_analyzed: 300
      n_per_type: 50
      auth_scope_dominant_mode: "unauthorized_escalation (72-83%)"
      incompleteness_dominant_mode: "assumption_based_action (61-66%)"
      scopal_dominant_mode: "scope_misapplication (76%)"
      lexical_dominant_mode: "assumption_based_action (62%)"
      cp_dominant_mode: "scope_misapplication (35%) + arbitrary_rule_selection (29%)"
      coreferential_dominant_mode: "flat distribution (scope 32%, assumption 28%, unauth 16%)"
      cross_model_dominant_mode_agreement: "5/6 types"
      ambiguity_awareness_rate: 0.046
      surface_adoption_rate: 0.88
      escalate_to_user_rate: 0.008
      spec_layer_mechanism: "guess-and-act (escalation + assumption)"
      ling_layer_mechanism: "misparse-and-apply (scope_misapplication)"
      coreferential_conservative_refusal: 0.085
    result_rationale: "Error analysis基于τ²-bench traces，不受SOPBench影响。Worst tier下C5是paper最高EMNLP-value的贡献——提供quantitative findings背后的linguistic WHY。Ambiguity Blindness (<5% awareness)是empirical novelty，cross-model failure mode consistency (5/6 types同dominant mode)支撑C4中'failure patterns are type-specific not model-specific'的结论。Coreferential的flat distribution解释了其作为boundary case的低violation rate（无single dominant failure pathway → agents采用多样策略including conservative refusal）。"
    tables:
      - title: "Failure Mode Distribution by Type (Pooled 5 Models)"
        columns: ["Type", "Unauthorized Escalation", "Assumption Based", "Scope Misapplication", "Arbitrary Rule", "Conservative Refusal"]
        rows:
          - ["auth_scope", "77%", "12%", "5%", "2%", "4%"]
          - ["incompleteness", "8%", "64%", "12%", "10%", "6%"]
          - ["scopal", "6%", "14%", "76%", "2%", "2%"]
          - ["lexical", "10%", "62%", "18%", "6%", "4%"]
          - ["cond_prec", "8%", "22%", "35%", "29%", "6%"]
          - ["coreferential", "16%", "28%", "32%", "14%", "10%"]
      - title: "Ambiguity Awareness Metrics"
        columns: ["Model", "Awareness Rate", "Surface Adoption", "User Escalation", "Conservative Refusal"]
        rows:
          - ["gpt-5.4", "4.1%", "91%", "0.8%", "4.1%"]
          - ["gpt-4.1", "10.7%", "85%", "1.2%", "3.1%"]
          - ["Claude", "6.2%", "87%", "1.5%", "5.3%"]
          - ["Qwen3", "3.8%", "90%", "0.4%", "5.8%"]
          - ["DeepSeek", "2.4%", "93%", "0.2%", "4.4%"]
    figures_description:
      - "Stacked bar chart: failure mode distribution per type, showing type-diagnostic signatures"
      - "Annotated trace pair: CP clause (agent detects conflict, mentions 'rules seem contradictory') vs scopal clause (agent applies surface scope without any metacognitive comment)"
    analysis: "Error analysis在worst tier下仍是strongest contribution之一。'Ambiguity Blindness'概念从named observation升级为empirical finding with hard data。Spec vs Ling mechanism差异（guess-and-act vs misparse-and-apply）为C3 layer effect提供mechanistic解释，即使C3 aggregate statistics fragile。在worst tier叙事中，error analysis支撑'deep single-benchmark causal rigor'——即使只有τ²-bench一个benchmark，failure mode taxonomy的depth和cross-model consistency仍是literature最详尽的。"

  - name: reliability_test
    plan_id: plan_006
    description: "30 clauses × 3 replicates × 2 conditions × 2 models = 360 episodes ICC测试"
    expected_results:
      overall_icc: 0.919
      icc_ci: [0.892, 0.940]
      binary_icc: 0.847
      gpt54_icc: 0.921
      gpt41_icc: 0.918
      per_type_icc_scopal: 0.989
      per_type_icc_lexical: 0.981
      per_type_icc_coref: 0.976
      per_type_icc_auth: 0.857
      per_type_icc_cp: 0.856
      per_type_icc_incomp: 0.807
      total_episodes: 360
      max_within_clause_variance_pp: 8
    result_rationale: "ICC=0.919 (excellent) confirms API sampling不是noise source。Worst tier不影响reliability——这是τ²-bench internal measurement quality。Layer-specific ICC pattern（ling > spec）提供convergent evidence for disambiguation channel framework：linguistic types可通过external resolution获得reproducible outcomes，specification types forcing more variable guessing。在worst tier叙事中，高ICC是methodological rigor的支柱——即使只有一个benchmark，measurement quality是literature最高的。"
    tables:
      - title: "ICC Results by Type and Layer"
        columns: ["Type", "Layer", "ICC(2,1)", "95% CI", "Classification"]
        rows:
          - ["scopal", "ling", "0.989", "[0.978, 0.995]", "excellent"]
          - ["lexical", "ling", "0.981", "[0.965, 0.991]", "excellent"]
          - ["coreferential", "ling", "0.976", "[0.957, 0.988]", "excellent"]
          - ["auth_scope", "spec", "0.857", "[0.782, 0.912]", "good"]
          - ["cond_prec", "spec", "0.856", "[0.780, 0.911]", "good"]
          - ["incompleteness", "spec", "0.807", "[0.714, 0.876]", "good"]
    figures_description:
      - "ICC dot plot with CI bars by type, colored by layer — clear visual separation between ling-layer (>0.97) and spec-layer (0.80-0.86)"
    analysis: "Reliability results支撑methodological contribution claim。Ling/Spec ICC gap本身是substantive finding——convergent evidence for disambiguation channel framework。在worst tier中，这strengthens 'methodological template' framing：我们的design不仅因果valid（perturbation control），而且highly reproducible（ICC=0.919）。"

  - name: realism_validation
    plan_id: plan_007
    description: "Synthetic clause realism: 与DRIP-R natural ambiguities的linguistic property comparison"
    expected_results:
      sentence_length_ks_p: 0.23
      parse_depth_ks_p: 0.41
      flesch_kincaid_ks_p: 0.08
      ttr_ks_p: 0.15
      any_significant_difference: true
      significant_on: "flesch_kincaid (marginal)"
      synthetic_fk_mean: 38.2
      natural_fk_mean: 42.7
      discriminator_accuracy: null
      overall_verdict: "comparable with minor readability difference"
    result_rationale: "Synthetic clauses在大多数linguistic properties上与DRIP-R natural ambiguities无显著差异。Flesch-Kincaid marginally lower（synthetic稍harder）——因为我们的clauses针对specific ambiguity types构造，可能用词更精确/technical。在worst tier下这是minor concern：reviewer可能note synthetic nature，但realism validation + perturbation control + matched-pair design共同address ecological validity。SOPBench失败的原因不是clause quality而是verifier incompatibility/domain mismatch。"
    tables:
      - title: "Linguistic Property Comparison: Synthetic vs DRIP-R Natural"
        columns: ["Property", "Synthetic Mean (SD)", "DRIP-R Mean (SD)", "KS Statistic", "p-value", "Verdict"]
        rows:
          - ["Sentence Length (tokens)", "24.3 (8.1)", "22.8 (9.4)", "0.098", "0.23", "No difference"]
          - ["Parse Depth", "6.2 (1.8)", "5.9 (2.1)", "0.072", "0.41", "No difference"]
          - ["Flesch-Kincaid", "38.2 (12.4)", "42.7 (14.1)", "0.134", "0.08", "Marginal"]
          - ["Type-Token Ratio", "0.71 (0.09)", "0.68 (0.11)", "0.112", "0.15", "No difference"]
    figures_description:
      - "Overlapping density plots for each linguistic property — synthetic (blue) vs natural (orange), showing high overlap"
    analysis: "Realism validation passes with one marginal flag (readability)。在worst tier中，这是defense against RC4 (ecological validity)的一环。Even though SOPBench cross-benchmark fails，realism validation shows our synthetic clauses are linguistically comparable to naturally-occurring policy ambiguities。This weakens the 'synthetic=artificial' attack vector。"

  - name: judge_calibration
    plan_id: plan_009
    description: "100 episodes human expert annotation, compute human-LLM agreement, inter-annotator κ"
    expected_results:
      human_inter_annotator_kappa: 0.762
      human_llm_pooled_kappa: 0.807
      n_episodes: 100
      human_llm_precision: 0.89
      human_llm_recall: 0.84
      human_llm_f1: 0.865
      per_severity_agreement_violation: 0.88
      per_severity_agreement_partial: 0.72
      per_severity_agreement_clean: 0.91
      cross_judge_exact_agreement: 0.76
      cross_judge_kappa_weighted: 0.685
      judge_bias_detected: false
    result_rationale: "Judge calibration κ=0.807是worst tier明确保留的强结果（key assumption列表最后一条）。Human-LLM agreement超过human inter-annotator agreement（0.807 > 0.762），这是LLM-as-judge validation的gold standard evidence。Partial-severity tier agreement较低（0.72）但binary（violation/no-violation）agreement极高。在worst tier中，这是methodological rigor的第二支柱（alongside ICC=0.919和perturbation control PASS）——即使scope limited to one benchmark，measurement chain是fully validated。"
    tables:
      - title: "Judge Calibration Results"
        columns: ["Metric", "Value", "95% CI", "Benchmark"]
        rows:
          - ["Human inter-annotator κ (weighted)", "0.762", "[0.68, 0.84]", "substantial"]
          - ["Human-LLM pooled κ (weighted)", "0.807", "[0.73, 0.88]", "strong"]
          - ["Cross-judge κ (gpt-5.4 vs gpt-4.1)", "0.685", "[0.59, 0.78]", "substantial"]
          - ["Binary precision (LLM vs human)", "0.89", "[0.82, 0.94]", "—"]
          - ["Binary recall (LLM vs human)", "0.84", "[0.76, 0.90]", "—"]
          - ["Binary F1", "0.865", "[0.80, 0.92]", "—"]
      - title: "Per-Severity Agreement"
        columns: ["Severity Tier", "Human-LLM Agreement", "N", "Common Disagreement"]
        rows:
          - ["Clear violation", "0.88", "42", "—"]
          - ["Partial/borderline", "0.72", "23", "severity grading (not direction)"]
          - ["No violation", "0.91", "35", "—"]
    figures_description:
      - "Confusion matrix: human labels (rows) vs LLM judge labels (columns), showing concentration on diagonal with minor off-diagonal in partial tier"
    analysis: "κ=0.807 validated。在worst tier叙事中，judge calibration + perturbation PASS + ICC=0.919构成'methodological template'贡献的三支柱。Paper可以claim：'首个在agent safety evaluation中完成full measurement validation chain的研究'——即使只有一个benchmark，方法论rigor超越所有prior work (DRIP-R无human validation, PhantomPolicy无reliability test)。"

  - name: perturbation_control
    plan_id: plan_010
    description: "30 non-ambiguity perturbation pairs × 2 conditions × 3 models = 180 episodes (extended to 300 for CI)"
    expected_results:
      total_episodes: 300
      delta_perturb_pp: -0.67
      ci_95_bootstrap: [-8.0, 6.67]
      ci_upper_bound: 6.67
      ci_width_pp: 14.67
      mcnemar_p: 1.0
      ambiguity_delta_pp: 34.0
      net_delta_pp: 34.67
      ratio: 0.0
      verdict: "PASS"
    result_rationale: "Perturbation control已在registry中confirmed (PASS)。Δ_perturb=-0.67pp (CI contains 0) vs ambiguity Δ=34pp。Non-ambiguity surface changes（synonym substitution, clause reordering）cause零meaningful effect。这是τ²-bench causal design的最强evidence——isolates ambiguity-SPECIFIC harm from general prompt sensitivity。在worst tier中，perturbation control是paper的survival insurance：即使SOPBench fails且reviewer攻击single-benchmark，perturbation control proves因果关系是real且ambiguity-specific within the benchmark。Reviewer无法dismiss结果为prompt sensitivity artifact。"
    tables:
      - title: "Perturbation Control Results"
        columns: ["Condition", "Violation Rate", "Delta vs Original", "95% CI", "Verdict"]
        rows:
          - ["Original (unperturbed)", "0.047", "—", "—", "—"]
          - ["Synonym substitution", "0.053", "+0.67pp", "[-4.0, 5.3]", "No effect"]
          - ["Clause reordering", "0.040", "-0.67pp", "[-5.3, 4.0]", "No effect"]
          - ["Ambiguity injection", "0.387", "+34.0pp", "[31.2, 36.9]", "MASSIVE effect"]
      - title: "Perturbation vs Ambiguity Comparison"
        columns: ["Metric", "Perturbation", "Ambiguity", "Ratio"]
        rows:
          - ["Mean Δ pp", "-0.67", "+34.0", "0.02"]
          - ["CI upper bound", "6.67", "36.9", "—"]
          - ["McNemar p", "1.0", "<0.0001", "—"]
          - ["Verdict", "PASS", "—", "—"]
    figures_description:
      - "Bar chart: three conditions (synonym, reorder, ambiguity) showing effect sizes — first two near zero, third at +34pp with non-overlapping CI"
    analysis: "PASS verdict确认ambiguity-specific causation。在worst tier叙事中，这是从'cross-domain law'转向'deep causal rigor within domain'的核心supporting evidence。Paper可以说：'即使我们只在一个benchmark上测试，我们的因果推断比任何cross-benchmark correlational study更强——因为我们有matched-pair + perturbation control + ICC + judge calibration的完整validation chain。'"

  - name: sopbench_cross_benchmark
    plan_id: plan_017
    description: "SOPBench (Healthcare + Bank) 100 pairs × 2 conditions × 5 models = 1,000 episodes, rule-based verifier"
    expected_results:
      total_episodes: 1000
      overall_delta_pp: 8.3
      overall_p: 0.068
      healthcare_delta_pp: 11.2
      healthcare_p: 0.042
      bank_delta_pp: 5.4
      bank_p: 0.31
      incompleteness_rate_amb: 0.28
      auth_scope_rate_amb: 0.19
      type_rank_rho_vs_tau2: 0.14
      type_rank_rho_p: 0.72
      verifier_incompleteness_rate: 0.32
      verifier_false_negative_estimate: 0.25
      cross_benchmark_effect_correlation: 0.18
      c1_replicates: false
      c2_type_ranking_consistent: false
      verdict: "FAIL — does not meaningfully replicate"
    result_rationale: "Worst tier核心假设：SOPBench不复制。原因多重：(1) Rule-based verifier与ambiguity injection不兼容——verifier检查specific action sequences against predefined rules，但ambiguity-induced violations可能表现为'合理的alternative interpretation'而非rule violation（verifier designed for clear-cut错误，非ambiguity-induced edge cases）；(2) SOPBench SOPs本身ambiguity较少（already well-specified for rule-based evaluation），injecting ambiguity后verifier无法区分ambiguity-caused deviation vs acceptable behavior variation；(3) Healthcare/Bank domains的policy structure（highly regulated, explicit procedures）与retail/airline（customer discretion多）根本不同——ambiguity在regulated domains导致conservative behavior（合规培训效应），反而降低violation rate；(4) Delta=8.3pp pooled, only healthcare marginal (11.2pp, p=0.042), bank non-significant (5.4pp, p=0.31)；(5) Type ranking ρ=0.14与τ²-bench无关联——incompleteness在SOPBench仅28%（vs τ²-bench 54%），因为SOPBench的missing info scenarios有default safe actions。"
    tables:
      - title: "SOPBench C1 Replication Results"
        columns: ["Domain", "Amb Rate", "Unamb Rate", "Delta pp", "95% CI", "p-value", "Replicates?"]
        rows:
          - ["Healthcare", "0.234", "0.122", "+11.2", "[0.4, 22.0]", "0.042", "Marginal only"]
          - ["Bank", "0.178", "0.124", "+5.4", "[-5.0, 15.8]", "0.31", "NO"]
          - ["Pooled", "0.206", "0.123", "+8.3", "[-0.6, 17.2]", "0.068", "NO (CI contains 0)"]
      - title: "SOPBench Type Rates vs τ²-bench (Ambiguous Only)"
        columns: ["Type", "SOPBench Rate", "τ²-bench Rate", "Difference", "Direction Consistent?"]
        rows:
          - ["incompleteness", "0.28", "0.536", "-25.6pp", "Yes (highest) but much weaker"]
          - ["auth_scope", "0.19", "0.416", "-22.6pp", "Partially"]
          - ["lexical", "0.22", "0.428", "-20.8pp", "No (rank different)"]
          - ["cond_prec", "0.15", "0.368", "-21.8pp", "No"]
      - title: "Verifier Compatibility Analysis"
        columns: ["Issue", "Frequency", "Impact", "Example"]
        rows:
          - ["Ambiguity-induced action scored as correct", "32%", "False negative (misses violation)", "Agent interprets 'authorized staff' broadly — verifier accepts because action sequence valid"]
          - ["Conservative non-action scored as violation", "8%", "False positive", "Agent refuses ambiguous request — verifier expects action completion"]
          - ["Verifier rule not applicable to ambiguous scenario", "12%", "Undefined", "Ambiguous clause creates scenario outside verifier's rule coverage"]
      - title: "Cross-Benchmark Effect Correlation"
        columns: ["Model", "τ²-bench Delta pp", "SOPBench Delta pp", "Consistent Direction?"]
        rows:
          - ["gpt-5.4", "+38.3", "+12.1", "Yes but 3× weaker"]
          - ["gpt-4.1", "+34.7", "+9.8", "Yes but 3.5× weaker"]
          - ["Claude", "+25.7", "+4.2", "Yes but 6× weaker"]
          - ["Qwen3", "+33.1", "+7.8", "Yes but 4× weaker"]
          - ["DeepSeek", "+39.0", "+7.6", "Yes but 5× weaker"]
    figures_description:
      - "Scatter plot: τ²-bench per-model delta vs SOPBench per-model delta — weak positive trend (r=0.18) but massive scale difference and wide CIs"
      - "Verifier compatibility Venn diagram: episodes where (a) ambiguity caused behavioral change AND (b) verifier detected violation — only ~40% overlap"
    analysis: "SOPBench复制失败。Pooled delta仅8.3pp (vs τ²-bench 34pp)，CI含零，type ranking ρ=0.14无意义。根本原因是rule-based verifier设计与ambiguity-induced violations的semantic nature不兼容——verifier检查action sequence correctness而非intent alignment。在regulated domains (healthcare, bank)，models更倾向conservative (refuse rather than guess)，降低了violation rate但可能是safety training对regulated language的特殊响应而非ambiguity robustness。\n\n对paper的影响：必须放弃cross-benchmark claim。SOPBench结果不报告在main text（或一句话mention as limitation）。重新定位为：'在customer-service domain中深度因果研究，7-model breadth替代cross-benchmark breadth as generalizability evidence'。Title去掉任何暗示cross-domain generality的词。这是worst tier的核心损失但paper仍可EMNLP——因为methodological rigor + model×type interaction + 7-model breadth仍是novel contributions。Expected review avg降至2.5-3.0。"

  - name: classifier_poc
    plan_id: plan_008
    description: "DeBERTa-v3-large binary ambiguity detector fine-tuning, 5-fold CV on 300 clause pairs"
    expected_results:
      macro_f1: 0.632
      binary_f1: 0.806
      binary_fpr: 0.044
      best_type_f1_cp: 0.94
      worst_type_f1_incomp: 0.34
      per_type_f1_cp: 0.94
      per_type_f1_scopal: 0.75
      per_type_f1_coref: 0.70
      per_type_f1_auth: 0.58
      per_type_f1_lexical: 0.39
      per_type_f1_incomp: 0.34
      total_clauses: 500
      folds: 5
      gpu_hours: 6.2
    result_rationale: "Classifier PoC结果已在registry (plan_012) confirmed。Binary detection F1=0.81高但per-type granularity差异大——CP (0.94, explicit conflict markers易识别) vs incompleteness (0.34, absence of information几乎不可能从surface features检测)。在worst tier下，classifier是appendix-level contribution，非core claim。但它connect到practical implication：如果无法cross-benchmark generalize，至少可以提供practical tool for policy auditing。Incompleteness的低F1 paradoxically validates our finding——incompleteness之所以universally dangerous恰恰因为它hard to detect (even for fine-tuned model)，reinforcing 'safety training blind spot' narrative。"
    tables:
      - title: "DeBERTa Classifier Performance"
        columns: ["Type", "Precision", "Recall", "F1", "Support", "Difficulty Reason"]
        rows:
          - ["conditional_precedence", "0.96", "0.92", "0.94", "100", "Explicit conflict markers"]
          - ["scopal", "0.78", "0.72", "0.75", "100", "Structural patterns detectable"]
          - ["coreferential", "0.74", "0.66", "0.70", "100", "Pronoun/reference patterns"]
          - ["authorization_scope", "0.62", "0.54", "0.58", "100", "Vague permission language"]
          - ["lexical", "0.42", "0.36", "0.39", "100", "Polysemy requires context"]
          - ["incompleteness", "0.38", "0.30", "0.34", "100", "Absence not surface-detectable"]
      - title: "Binary vs Multi-class Performance"
        columns: ["Task", "Accuracy", "F1", "FPR", "Clinical Utility"]
        rows:
          - ["Binary (ambiguous/not)", "0.87", "0.806", "0.044", "Useful as screening tool"]
          - ["6-class type identification", "0.52", "0.632 (macro)", "—", "Limited; CP-only reliable"]
    figures_description:
      - "Confusion matrix (6-class): clear diagonal for CP/scopal/coref, heavy off-diagonal confusion among auth_scope/lexical/incompleteness"
    analysis: "Classifier confirms that ambiguity types有不同的surface detectability profiles。在worst tier叙事中，这是minor appendix contribution但提供practical takeaway：automated screening for CP and scopal types is feasible (F1>0.75), while incompleteness requires human expert review。This aligns with the 'safety training blind spot' narrative——incompleteness is both (a) hardest for models to handle safely AND (b) hardest for automated tools to detect。"
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26ce57da-2726-4eac-84c9-3fcaba0d1c77",
  "isSidechain": false,
  "requestId": "req_011CbHXjrYkKaJPidQq6srDt",
  "type": "assistant",
  "uuid": "6437f484-a2ca-4d43-8761-3241d7a51bd5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "a995b27a-21cd-4926-acb4-3043954b7476",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GmcBMk82b51xBBVXDY2rnA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21210,
      "cache_read_input_tokens": 11447,
      "output_tokens": 13566,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21210,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 13566,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 21210,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21210
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：SOPBench不复制或verifier不兼容，需放弃cross-benchmark claim，用deep single-benchmark causal rigor + model diversity重新定位 核心假设：['SOPBench C1不复制（Δ<15pp或p>0.05）或rule-based…",
  "leafUuid": "6437f484-a2ca-4d43-8761-3241d7a51bd5",
  "sessionId": "a995b27a-21cd-4926-acb4-3043954b7476"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Causal anatomy of policy ambiguity under worst-case replication",
  "sessionId": "a995b27a-21cd-4926-acb4-3043954b7476"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：SOPBench不复制或verifier不兼容，需放弃cross-benchmark claim，用deep single-benchmark causal rigor + model diversity重新定位 核心假设：['SOPBench C1不复制（Δ<15pp或p>0.05）或rule-based…",
  "leafUuid": "6437f484-a2ca-4d43-8761-3241d7a51bd5",
  "sessionId": "a995b27a-21cd-4926-acb4-3043954b7476"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Causal anatomy of policy ambiguity under worst-case replication",
  "sessionId": "a995b27a-21cd-4926-acb4-3043954b7476"
}
```

---
