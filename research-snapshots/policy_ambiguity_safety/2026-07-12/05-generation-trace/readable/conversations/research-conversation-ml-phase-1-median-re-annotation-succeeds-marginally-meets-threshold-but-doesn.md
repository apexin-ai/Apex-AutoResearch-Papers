# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：κ re-annotation succeeds marginally (meets threshold but doesn't strongly 

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 28
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/f40dd3ff-f3b8-4d76-a956-dcce22cdea43.jsonl`
- **Structured JSON:** [`050b1b089dc4100b59fe.json`](../../sessions/05/050b1b089dc4100b59fe.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-23T19:02:23.386Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-23T19:02:23.386Z",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：κ re-annotation succeeds marginally (meets threshold but doesn't strongly validate LLM coding), SOPBench partially replicates — paper's quantitative core is strong but qualitative contribution needs softening\n核心假设：['0.35 ≤ κ_reannotation < 0.45 (fair), dominant failure modes match in 3-4/6 types with boundary-type disagreements (auth_scope/incompleteness)', 'SOPBench C1 replicates (Δ≥15pp) but with smaller effect size or 1 model anomaly', 'SOPBench type ranking weakly correlated (0.30 ≤ ρ < 0.60) or only 2-3 types testable', 'At least one reviewer flags C3 within-judge fragility as undermining the layer claim', \"C4 model×type interaction accepted as interesting but reviewer questions whether 5 models suffice for 'differential safety training' claims\"]\n关键指标范围：{'kappa_reannotation': [0.35, 0.44], 'sopbench_c1_delta_pp': [15, 25], 'sopbench_type_rank_rho': [0.3, 0.59], 'c5_human_llm_dominant_mode_agreement': [3, 4], 'expected_arr_score': [3.5, 3.99], 'expected_reviewer_confidence': [3.0, 3.5]}\n叙事方向：C1+C4 carry the paper; C5 downgraded from 'validated taxonomy' to 'convergent LLM-coded and human evidence with moderate agreement.' Abstract replaces 'type-diagnostic failure signatures' with 'type-associated failure patterns.' Contribution (3) retains 'supported by' but adds 'preliminary human validation (κ=0.3X)' qualifier. C3 layer effect moved from standalone finding to subordinate observation under C4 ('the model×type interaction subsumes and explains the aggregate layer gap'). SOPBench mentioned as 'partial cross-domain evidence' rather than 'replication.' Rebuttal strategy: emphasize that κ=0.3X exceeds automated-only (plan_010 κ=0.517), and the 3-4 type agreement covers the theoretically critical types (incompleteness, auth_scope). Still competitive for EMNLP poster — C1 causal design + C4 interaction is sufficient novel contribution even with weakened C5.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: policy_ambiguity_safety\nvenue: emnlp-2026\nfocus: Evaluate the paper's competitiveness at EMNLP 2026 ARR assuming κ re-annotation succeeds (κ≥0.35). Key question: does upgrading contribution (3) from 'initial evidence' to validated move the paper from 3.75 to 4.0? What remaining gaps would reviewers still flag?\n\n## paper_framing.md\n\n# Paper Framing — policy_ambiguity_safety\n\n> 最后更新: 2026-05-23 UTC | 状态: R18 全部 resolved + 6 supplementary experiments (5 done, 1 running)\n> 目标: EMNLP 2026 (ARR May cycle, DDL 2026-05-25)\n> Dream: dream_20260520T112859 — best 3.5 / median 3.0 / worst 2.5 (pre-pivot; re-dream needed)\n> 5-model: 2,997 episodes, C1 confirmed (+34.0pp, 5 models), C4 upgraded (model×type interaction)\n> Supplementary experiments (2026-05-22/23):\n>   - ✅ Cross-Judge Validation: Fleiss' κ=0.717, rankings preserved (ρ≥0.70), no same-family bias → R18-N2 升级为 validated\n>   - ✅ Controlled Confound: ±0.1pp token-count effect, β=+0.027 (p=0.003) → R18-W3 resolved\n>   - ✅ Residual Decomposition: ICC=0.749, 15.2pp stochastic / 45.6pp systematic → R18-W2 answered\n>   - ✅ Disambiguation Prompting: overall not significant, GPT-4.1 auth_scope -28pp (p=0.001) → rebuttal ammunition\n>   - ✅ Human Annotation Prep: 100 traces + codebook ready\n>   - 🔄 SOPBench Expansion: DeepSeek ~78% complete\n\n## Core Insight\n\nPolicy ambiguity universally causes massive safety violations in LLM agents (+34.0pp across 5 architecturally diverse models), with a significant type hierarchy (incompleteness 53.6% >> coreferential 31.6%). Specification-layer types are more dangerous on average (Δ=6.08pp, p=0.017), but the deeper finding is a **model × type interaction**: authorization scope vulnerability varies 52pp across models (12% Claude to 64% GPT-5.4), revealing that safety training differentially mitigates specific ambiguity types, while incompleteness remains universally dangerous. This interaction connects Berry & Kamsties' nocuous ambiguity theory to modern safety alignment and suggests both type-aware triage AND model-aware risk assessment.\n\n## Title (Working)\n\n\"Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families\"\n\nAlternative: \"Differential Nocuity: How Ambiguity Type and Model Architecture Shape Safety Violations in LLM Agents\"\n\nNote: Pivoted from \"Uniformly Nocuous\" → \"Specification-Layer Dominant\" (2-model) → \"Differential Nocuity with Model Interaction\" (5-model). The model × type interaction is the novel finding that elevates the paper beyond simple effect demonstration.\n\n## Core Claims\n\n### C1: Binary Effect (PRIMARY — confirmed, 5 models)\nAmbiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +34.0pp (5-model), McNemar OR=15.1 (CI: [10.78, 21.17]), p<0.0001. Holds across all 6 types and all 5 models.\n- **Evidence**: 2,997 episodes across 5 models × 6 types × 2 conditions. Bootstrap CI: [+31.2pp, +36.9pp].\n- **Per-model**: Claude +25.7pp, Qwen3 +32.4pp, GPT-4.1 +34.7pp, GPT-5.4 +38.3pp, DeepSeek +39.0pp — all p<10^-17.\n- **Strength**: Extremely strong. Replicated across 5 architecturally diverse models (proprietary dense, open-source MoE, open-source dense), 6 types, 2 domains. No exceptions.\n- **Causal backing**: Matched-pair design + perturbation control (plan_010, Δ_perturb=3.33pp, PASS) → strongest causal inference in the literature.\n- **Logistic regression**: condition_amb coef=2.278, z=19.65, p<0.001 — ambiguity is the dominant predictor even after controlling for token delta, model, and type.\n\n### C2: Type Hierarchy (SECONDARY — confirmed, 5 models)\n**PIVOTED from uniformity null.** 6-type hierarchy significant: omnibus χ²=28.02, p=3.6×10^-5, V=0.137 (small but well-powered: actual power=0.993, MDE=0.093). 3-tier structure emerges from TOST analysis.\n- **Evidence**: 2,997 episodes (5 models × 6 types × 2 conditions, ambiguous only: 1,499 episodes)\n  - **High tier**: incompleteness 53.6% (standout — universally dangerous across all models)\n  - **Mid tier**: lexical 42.8%, auth_scope 41.6%, scopal 39.4%, CP 36.8% — pairwise equivalent at ±15pp\n  - **Low tier**: coreferential 31.6% (lowest — partial disambiguation via tool responses)\n- **TOST structure**: ±15pp: 8/15 equivalent, 7/15 non-equivalent. ±10pp: 4/15 equivalent, 11/15 non-equivalent. Types are NOT interchangeable.\n- **V=0.137 context**: Below 0.20 threshold but well-powered (power=0.993). The type effect is real but small — the 3-tier structure captures it better than a single V statistic. The heterogeneity is driven by the extremes (incompleteness 53.6% vs coreferential 31.6% = 22pp gap).\n- **Coreferential as boundary case**: 31.6% violation rate is the lowest but still substantial (+18.7pp vs unambiguous). Agents partially disambiguate via tool responses and cautious strategies. Conservative_refusal rate 6-11% (vs avg 2-3%).\n- **Model-dependence of type rankings**: Type rankings are NOT identical across models. Incompleteness is top-2 for ALL models, but auth_scope ranges from #1 (GPT-5.4, DeepSeek) to #6 (Claude). See C4.\n\n### C3: Layer Effect (TERTIARY — suggestive, fragile under within-judge analysis)\n**[2026-05-20 REVISED with 5-model data + within-judge check]** Specification-layer ambiguities cause more violations than linguistic-layer on average, but the effect is modest, model-dependent, and fragile under subgroup analysis.\n- **Evidence (5-model aggregate)**: Spec 44.0% vs Ling 37.9%, Δ=6.08pp, CI [1.14, 11.02], χ²=5.73, p=0.017, V=0.062 (small), OR=1.29 [1.05, 1.58].\n- **Within-judge fragility**: gpt-4.1 judged group (gpt-5.4+DeepSeek): Δ=+8.0pp, p=0.059 (marginal). gpt-5.4 judged group (gpt-4.1+Claude+Qwen3): Δ=+4.8pp, p=0.157 (n.s.). Pooled significance may partly reflect between-judge variance or insufficient within-group power. Paper表述: \"suggestive\" or \"a moderate tendency,\" NOT \"confirmed.\" Disclose within-judge non-significance in Limitations.\n- **Per-model layer gaps** (THE KEY FINDING — feeds C4):\n  - GPT-5.4: +14.0pp (spec 48.0% vs ling 34.0%) — strong\n  - GPT-4.1: +12.0pp (spec 46.7% vs ling 34.7%) — strong\n  - Claude: +3.3pp (spec 32.0% vs ling 28.7%) — weak\n  - DeepSeek: +2.0pp (spec 50.7% vs ling 48.7%) — negligible\n  - Qwen3: -0.9pp (spec 42.7% vs ling 43.6%) — reversed!\n- **Root cause**: auth_scope is the primary driver. GPT models have extremely high auth_scope rates (46-64%), inflating their spec-layer average. Claude (12%) and Qwen3 (26%) have low auth_scope, so their spec-layer advantage disappears.\n- **Framing decision**: C3 is NOT \"spec-layer nearly twice as dangerous\" (that was 2-model artifact). The correct framing is: \"Specification-layer types are significantly more dangerous on average (Δ=6.08pp, p=0.017), but this aggregate masks a model × type interaction where the gap varies from +14pp (GPT-5.4) to -1pp (Qwen3). The interaction, not the main effect, is the theoretically interesting finding (see C4).\"\n- **Info delta as mediator** [MF-2]: Token delta significant in 5-model logistic regression (coef=0.022, z=3.49, p=0.0005). Spec-layer clauses require more tokens to disambiguate (auth_scope 36.1, incomp 34.6 vs coref 7.8 tokens). Info delta partially mediates but doesn't eliminate the condition effect (condition_amb coef=2.278 dominates).\n- **Layer overlap persists**: CP (36.8%, spec) < scopal (39.4%, ling). Mid-tier cluster spans both layers. Layer effect is driven by extremes: incompleteness (53.6%, spec) vs coreferential (31.6%, ling).\n- **ICC convergent evidence** [plan_006]: Per-type ICC mirrors layer hierarchy — Ling-layer ICC all excellent (scopal 0.989, lexical 0.981, coref 0.976), Spec-layer ICC all good (auth 0.857, CP 0.856, incomp 0.807). Spec-layer less reproducible — agents guess differently each run when external disambiguation channels are absent.\n- **CL connection**: Parallels pragmatics vs semantics distinction. Good-enough processing (Ferreira et al. 2002). Disambiguation channel framework: linguistic ambiguity has partial external resolution; specification ambiguity forces guessing.\n\n### C4: Model × Type Interaction (UPGRADED — star finding, 5 models complete)\n**[2026-05-20 DEFINITIVE, 5/5 models]** Models show significantly different vulnerability profiles despite universal binary effect. The interaction is the paper's most novel finding.\n- **Model main effect**: Overall χ²=31.02, p=3.0×10^-6, V=0.102. Ambiguous-only: χ²=24.01, p=7.9×10^-5.\n  - Vulnerability ranking: Claude 30.3% < GPT-5.4 41.0% ≈ GPT-4.1 40.7% < Qwen3 43.1% < DeepSeek 49.7%\n  - Bootstrap CI confirms: Claude significantly lower than all others; DeepSeek significantly higher than GPT models.\n- **Model × Type interaction matrix** (ambiguous condition, violation rates):\n  ```\n  Type                  GPT-5.4  GPT-4.1  Claude  Qwen3   DeepSeek\n  authorization_scope     64%     46%      12%     26%     60%\n  conditional_precedence  34%     36%      36%     40%     38%\n  incompleteness          46%     58%      48%     62%     54%\n  lexical                 42%     34%      32%     52%     54%\n  coreferential           18%     32%      22%     42%     44%\n  scopal                  42%     38%      32%     37%     48%\n  ```\n- **Key interaction patterns**:\n  - **auth_scope**: 52pp range (Claude 12% → GPT-5.4 64%). The MODEL-DIFFERENTIATING type. Claude's RLHF appears to specifically train authorization boundary awareness.\n  - **coreferential**: 26pp range (GPT-5.4 18% → DeepSeek 44%). Second most model-dependent. Open-source models struggle more with referential ambiguity.\n  - **incompleteness**: Universally high (46-62%, 16pp range). ALL models fail on missing information — safety training doesn't help when information literally isn't there.\n  - **CP**: Most model-invariant (34-40%, 6pp range). Explicit rule conflicts treated similarly by all architectures.\n- **Per-model type χ²** (which models show type-specific vulnerability patterns):\n  - GPT-5.4: χ²=23.44, p=0.0003, V=0.28 — strongest type differentiation (very high auth_scope, very low coref)\n  - Claude: χ²=17.87, p=0.003, V=0.24 — strong differentiation (very low auth_scope, moderate others)\n  - Qwen3: χ²=15.89, p=0.007, V=0.23 — moderate differentiation (high incomp+lex, low auth_scope)\n  - GPT-4.1: χ²=9.89, p=0.078, V=0.18 — borderline\n  - DeepSeek: χ²=6.31, p=0.277, V=0.14 — NOT significant (uniformly high across all types)\n- **Fleiss κ = 0.384 (fair agreement)**: Models only moderately agree on which specific clauses trigger violations. The binary effect is universal, but the WHICH-clauses question is model-dependent.\n- **Theoretical implications**: (1) Safety training differentially addresses specific ambiguity types — Claude's auth_scope robustness suggests authorization boundary handling was explicitly or implicitly trained. (2) Incompleteness is a \"safety training blind spot\" — all models fail equally. (3) DeepSeek's uniform vulnerability suggests less type-specific safety training.\n- **Framing**: C4 from \"models agree\" → \"Models show systematically different vulnerability profiles. The binary effect is universal, but HOW models fail depends on the intersection of ambiguity type and safety training approach. auth_scope is the canary type — most sensitive to safety training quality.\"\n- **Evidence from plan_005**: 2-model failure modes consistent (5/6 dominant modes identical). 5-model failure mode analysis pending.\n- **Layer effect moderation**: C3's aggregate layer gap (6.08pp) is driven by GPT models' high auth_scope rates. The layer effect is itself model-dependent (GPT +12-14pp, Claude +3pp, Qwen3 reversed), making the MODEL × TYPE interaction more fundamental than the LAYER main effect.\n\n### C5: Error Analysis (CONFIRMED — EMNLP core)\nDifferent ambiguity types produce qualitatively different failure modes with type-specific signatures. plan_005 (123+122 violation traces across gpt-5.4 and gpt-4.1, confidence=0.94).\n- **Evidence**: plan_005 complete (gpt-5.4: 123 traces, gpt-4.1: 122 traces). Key findings:\n  - **Type-specific failure signatures**: auth_scope → unauthorized_escalation (72%/83%); incompleteness → assumption_based_action (61%/66%); scopal → scope_misapplication (76%/74%); lexical → assumption_based_action (71%/53%); CP → scope_misapplication (41%/28%) + arbitrary_rule_selection (29%/28%); coreferential → scope_misapplication (44%) / assumption_based_action (38%)\n  - **Cross-model consistency**: 5/6 types share the same dominant failure mode across gpt-5.4 and gpt-4.1. Only coreferential diverges (scope_misapplication vs assumption_based_action). Overall mode distribution nearly identical: both ~33% assumption_based_action, ~26-32% unauthorized_escalation, ~25-28% scope_misapplication. Failure mode profiles are type-specific, not model-specific.\n  - **Layer mechanism**: Ling-layer dominated by scope_misapplication (39% ling avg vs 15% spec avg) = \"misparse\"; Spec-layer dominated by unauthorized_escalation + assumption_based_action = \"active guessing\" → explains higher violation rates\n  - **Ambiguity Blindness empirically confirmed**: awareness rate gpt-5.4=4.1%, gpt-4.1=10.7% (both very low); surface_adoption >88% all types both models; escalate_to_user <1%. Nuance: gpt-4.1 (mid-tier) shows 2.6× higher awareness than gpt-5.4 (frontier) — awareness may inversely correlate with action-orientation (frontier models more \"confident,\" act without hesitation)\n  - **Cross-domain consistency**: airline vs retail failure mode profiles Δ < 13pp (unauthorized_escalation shows largest domain effect: retail 38.6% vs airline 26.1%)\n  - **Coreferential boundary**: conservative_refusal 6-11% (vs avg 2-3%) partially explains low violation rate — agents sometimes pause rather than guess. N=25 combined traces show no single dominant failure mode (flat distribution: scope_misapplication 32%, assumption_based_action 28%, unauthorized_escalation 16%) — contrasts with other types' sharp signatures, reflecting the diversity of resolution strategies for referential ambiguity\n  - **Lexical surprise**: 53-71% assumption_based_action — agents treat word ambiguity as information gap, not misparse\n- **Automated inter-coder agreement** [MF-5, Reviewer-validated]: Cross-coding 60 traces (gpt-5.4 vs gpt-4.1 as independent coders). 4-category merged: 80% agreement, Cohen's κ=0.594 (moderate). κ deflated by kappa paradox — lexical 91.7% agreement → κ=0.0 (11/12 same label, chance agreement also high), scopal 100% agreement → κ undefined. True disagreement concentrated at unauthorized_escalation ↔ inappropriate_action boundary in auth_scope (κ=0.054) and incompleteness (κ=0.233).\n  - **Reporting strategy** [Reviewer recommendation]: (1) Compute Gwet's AC1 as primary metric (designed for kappa paradox, expected 0.70-0.75); (2) Report 80% agreement + 5/6 dominant mode consistency as headline validity evidence; (3) Report κ honestly with kappa paradox caveat; (4) Auth_scope failure mode: soften to \"dominated by boundary-exceeding behaviors (unauthorized_escalation or inappropriate_action, >90%)\" instead of specific percentages; (5) Fine-grained 6-type as appendix with \"automated coding\" caveat.\n  - **C5 safety**: Ambiguity Blindness (<5-11%), surface_adoption (>88%), layer mechanism (ling→scope vs spec→escalation) all robust. Fine-grained per-type percentages unreliable at κ=0.594. Plan_009 human anchor (20-30 failure mode traces) would upgrade from \"moderate automated\" to validated.\n- **EMNLP value**: Highest. Provides the linguistic WHY behind the quantitative WHAT. Cross-model + cross-domain consistency elevates from anecdotal to systematic finding. \"Ambiguity Blindness\" upgraded from named concept to empirical finding with <5-11% awareness hard data.\n\n## Narrative Structure (CL-first for EMNLP)\n\n### Intro Logic Chain\n1. Agent policies are written in NL → contain ambiguity (established)\n2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact\n3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.\n4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter? Does it depend on the model?\n5. **This paper**: First causal, type-granularity, cross-model study. Matched-pair design + perturbation control isolates ambiguity effect. 5 models × 6 types.\n6. **Core findings**: (a) All ambiguity is nocuous (+34.0pp, 5 models), (b) type DOES predict severity — 3-tier hierarchy with incompleteness most dangerous, (c) models show dramatically different vulnerability profiles — auth_scope varies 52pp across models, suggesting safety training differentially addresses ambiguity types, (d) while incompleteness remains universally dangerous, a \"safety training blind spot.\"\n\n### Section Map\n- **§1 Intro**: Gap + contributions (causal map + differential nocuity + model×type interaction)\n- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R\n- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R\n- **§4 Method**: Matched-pair causal design, τ²-bench, 5 models (3 proprietary + 2 open-source), clause generation, perturbation control, cross-judge evaluation\n- **§5 Results**: C1 (binary, +34.0pp, 5 models) → C2 (type hierarchy, 3-tier) → C3 (layer effect, modest but significant) → C4 (model×type interaction — star finding)\n- **§6 Analysis**: C5 error analysis — qualitative failure modes per type. Ambiguity Blindness. Model-specific patterns.\n- **§7 Discussion**: Differential nocuity theory. Safety training selectivity. Disambiguation channel framework. Limitations (2 domains, synthetic injection, LLM-as-judge).\n- **§8 Conclusion**: All policy ambiguity is nocuous, but type AND model jointly determine risk level. Both type-aware auditing and model-specific risk assessment recommended.\n\n## Anticipated Reviewer Concerns\n\n### RC1: \"Type effect could be artifact of taxonomy granularity\"\n**Response**: (a) Layer effect (Spec vs Ling ~19pp gap) is robust — holds even if individual types are reclassified. (b) 2-layer structure grounded in Li et al. + Massey et al. (c) Coreferential's low rate has structural explanation (disambiguation channels), not just noise. (d) TOST confirms types are NOT equivalent (0/15 pairs at ±10pp).\n\n### RC2: \"Taxonomy is ad hoc / why these 6 types\"\n**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).\n\n### RC3: \"Only API models, no open-source\"\n**Response**: ✅ RESOLVED. 5-model coverage spans: frontier proprietary (gpt-5.4, claude-sonnet-4-6) + mid-tier proprietary (gpt-4.1) + open-source MoE (qwen3-235b) + open-source dense (deepseek-v3). Three providers (OpenAI, Anthropic, Chinese open-source). Two architecture types (dense, MoE). Model×type interaction (C4) reveals rich cross-model patterns.\n**Note [Reviewer 2026-05-20]**: Cross-judge asymmetry — Claude judged by gpt-5.4, gpt-5.4 judged by gpt-4.1. Must disclose in Method. plan_009 judge calibration measures this bias.\n\n### RC4: \"Synthetic ambiguity injection lacks ecological validity\"\n**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.\n\n### RC5: \"τ²-bench limited to retail/airline\"\n**Response**: ✅ ADDRESSED (plan_017). Cross-benchmark replication on SOPBench (Li et al., 2025) — Healthcare + Bank domains, 100 clause pairs × 5 models = 1,000 episodes with rule-based verifier. If C1 replicates, paper moves from \"customer service finding\" to \"cross-domain finding\" spanning 4 domains (retail, airline, healthcare, banking). Result in Appendix with main-text summary. τ²-bench remains primary; SOPBench provides independent cross-domain confirmation.\n\n### RC6: \"Binary effect is obvious — of course ambiguity causes errors\"\n**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOES predict severity — specification-layer ambiguities are nearly twice as dangerous, connecting to disambiguation channel availability.\n\n### RC7: \"Incompleteness matched-pair confound (information asymmetry)\"\n**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.\n\n### RC8: \"RC attachment in coreferential overlaps with scopal / structural ambiguity\"\n**Response**: (a) Our scopal category is explicitly scoped to quantifier/negation/modal scope interactions, not syntactic attachment. (b) RC attachment in policies manifests as *referential* confusion (which entity does the clause modify?) not *scope* confusion (which operator takes wide scope?). (c) Li et al. 2024 distinguishes syntactic ambiguity (including RC attachment) from scopal ambiguity — our grouping follows their treatment that RC attachment is closer to coreferential than scopal in terms of downstream interpretation. (d) Empirically, if the distinction were problematic, coreferential and scopal would show identical violation patterns — the error analysis (C5) can test whether their failure modes differ.\n\n### RC9: \"authorization_scope is just a subtype of incompleteness\"\n**Response**: (a) Incompleteness = missing conditions/exceptions/boundaries (structural absence). Authorization scope = ambiguous permission/role boundaries that ARE stated but vague (e.g., \"authorized personnel\" without specifying which functions). (b) The disambiguation pattern differs: incompleteness adds new conditions; auth_scope clarifies existing permission boundaries. (c) Empirically testable: if they were the same, their violation patterns and failure modes (C5) would be indistinguishable. (d) Report disambiguation length ratio per type as control variable in §4 Method.\n\n### RC10: \"API sampling noise undermines reliability\"\n**Response**: ✅ RESOLVED. plan_006 ICC=0.919 [0.892, 0.940] (excellent). (a) Per-clause violation rates highly reproducible across 3 independent replicates. (b) Binary ICC=0.847 (good). (c) Both models show near-identical ICC (gpt-5.4: 0.921, gpt-4.1: 0.918). (d) Bootstrap CI + ICC double evidence. (e) Previously identified ±8pp noise is within expected variance given the ICC confidence intervals.\n\n### RC11: \"Prompt sensitivity confound\" [Dream A9 — best tier \"strongest point\"]\n**Concern**: The +35-42pp effect is attributed entirely to ambiguity, but without a control condition using non-ambiguity perturbations (synonym substitution, clause reordering), the paper cannot cleanly distinguish ambiguity-specific harm from general prompt brittleness.\n**Response**: ✅ RESOLVED. plan_010 perturbation control (120 episodes): Δ_perturb=3.33pp (CI contains 0) vs ambiguity Δ=36.5pp. Non-ambiguity surface changes cause zero meaningful effect. This is the strongest causal evidence in the agent safety literature.\n\n## Concept Naming (distill insight: 命名即贡献)\n\nCore phenomenon: **\"Differential Nocuity\"** — all policy ambiguity types are nocuous for LLM agents (+34.0pp, all 5 models), but vulnerability varies by BOTH type and model. Incompleteness is universally dangerous (46-62%), while auth_scope vulnerability depends dramatically on safety training (12% Claude to 64% GPT-5.4). Unlike human RE where organizational context renders most ambiguity innocuous, agents lack disambiguation channels AND their safety training creates type-specific blind spots.\n\nSecondary phenomenon: **\"Ambiguity Blindness\"** — agents process grammatically fluent ambiguous clauses without meta-cognitive awareness of the ambiguity, adopting surface interpretations. Contrasts with explicit rule conflicts where agents show awareness and choose conservatively.\n\nTertiary phenomenon: **\"Disambiguation Channel Framework\"** [renamed from \"Hypothesis\" per Dream review SF-5] — the layer hierarchy reflects availability of external disambiguation: linguistic ambiguity (coreferential, lexical) can sometimes be resolved by tool responses, user context, or world knowledge; specification ambiguity (auth_scope, incompleteness) has no external resolution channel, forcing agents to guess. This is an explanatory framework supported by observational evidence (ICC pattern, failure mode distribution, coreferential boundary case), not a tested causal hypothesis. Future Work: manipulation experiment (inject spec-layer disambiguation info into tool responses, test if gap shrinks).\n\nQuaternary phenomenon: **\"Systematic Nocuity\"** [per Dream review SF-7] — B&K framework distinguishes nocuous (divergent interpretations) from innocuous (convergent). Our data reveals a third type: all models converge on the same WRONG interpretation (27% of ambiguous episodes). This is more dangerous than divergent nocuity — it's invisible in inter-model agreement metrics and appears \"correct\" until compared against ground truth. Proposed as B&K extension in Discussion.\n\n## Opening Hook Strategy (distill insight: 具体案例, 不要 \"Recently...\")\n\nOpen with a concrete τ²-bench failure: e.g., a customer returns a customized item within the return window; the agent grants a full refund + free return shipping because the policy says \"items may be returned within 30 days\" (scopal: \"items\" scopes over all categories including custom). The unambiguous version specifies \"standard items only\" — agent correctly refuses. One word of ambiguity → $200 unauthorized refund.\n\n## Narrative Type: 突破局限型 (distill pattern, 5/8 papers)\n\n\"DRIP-R classifies 5 ambiguity types and shows models disagree on interpretation → but does not measure whether this disagreement leads to safety violations. We close this gap — and find the answer is surprising: not all types are equal, specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones.\"\n\n## Benchmark Comparison Table (distill insight: 必有 feature matrix)\n\n| Feature | DRIP-R | PhantomPolicy | PolicyBank | AgentPex | **Ours** |\n|---------|--------|---------------|------------|----------|----------|\n| Ambiguity taxonomy | 5 RE types | — | 3 gap types | — | **6 types (2-layer)** |\n| Causal design | — | — | — | — | **matched pairs** |\n| Safety violation metric | — | binary | — | procedural | **3-tier severity** |\n| Cross-type comparison | descriptive | — | — | — | **statistical (χ² + V)** |\n| Models tested | 6 API | 4 API | 2 API | 2 API | **3 API + 2 open-source** |\n| Domain | retail | mixed | retail | telecom/retail/airline | **retail + airline** |\n\n## Contribution Positioning (for EMNLP) [revised 2026-05-20 with 5-model data]\n\n1. **Causal quantification of ambiguity's safety impact**: First matched-pair causal study of policy ambiguity → agent safety violations. Binary effect +34.0pp (OR=15.1, p<0.0001) across 5 architecturally diverse models and 6 ambiguity types. Perturbation control (Δ_perturb=3.33pp) confirms ambiguity-specific causation. Strongest causal evidence in the agent safety literature.\n2. **Differential Nocuity framework + Model × Type Interaction**: Not all ambiguity is equally dangerous, and not all models are equally vulnerable. 3-tier type hierarchy (incompleteness >> mid cluster >> coreferential). Model × type interaction reveals 52pp range in auth_scope vulnerability (Claude 12% → GPT-5.4 64%), while incompleteness remains universally dangerous (46-62%). Safety training differentially mitigates specific ambiguity types. Connects Berry & Kamsties nocuous ambiguity theory to modern safety alignment.\n3. **Type-specific failure mode taxonomy + Ambiguity Blindness**: 245 traces across 2 models and 2 domains reveal type-diagnostic failure signatures: spec-layer → guess-and-act (unauthorized_escalation, assumption_based_action); ling-layer → misparse-and-apply (scope_misapplication). Agents show <5-11% awareness of ambiguity (\"Ambiguity Blindness\"), with >88% surface adoption and <1% user escalation. Practical implication: ambiguity detection must be externalized.\n\nNOTE: C3 (layer effect, Δ=6.08pp) is a component finding supporting contribution #2. The MODEL × TYPE interaction (C4) is now MORE central than the layer main effect. \"Disambiguation channel\" is an explanatory framework (not hypothesis — per SF-5). DeBERTa classifier, if included, is a preliminary PoC appendix, not a contribution.\n\n## Required Reference Expansion [Dream A2 + MF-4 RE literature gap]\n\nCurrent plan has thin references. Must add (≥25 total in final paper):\n- **Nocuous ambiguity detection (CRITICAL — MF-4)**: Chantree, Nuseibeh, de Roeck & Willis (2006, ASE) — first computational nocuous ambiguity detection; Chantree et al. (2008, RLAC) — expanded. Direct lineage to our DeBERTa classifier.\n- **Cross-domain RE ambiguity**: Ferrari, Spagnolo & Gnesi (2017-2019, ASE) — NLP-based cross-domain ambiguity detection. NLP4RE community work.\n- **Good-enough processing**: Ferreira, Bailey & Ferraro (2002); Ferreira & Patson (2007)\n- **LLM garden-path (SF-6)**: Li et al. (2024) — incremental comprehension of garden-path sentences by LLMs. Directly relevant to how LLMs process ambiguity.\n- **Anaphoric ambiguity (SF-6)**: Poesio & Artstein (2005, 2008) — annotation of anaphoric ambiguity. Poesio (2004) \"Ambiguity\" encyclopedia entry.\n- **Surprisal/expectation-based**: Levy (2008); Hale (2001)\n- **Instruction-following robustness**: Zhou et al. (IFEval, 2023); Qin et al. (ToolBench, 2024)\n- **Prompt sensitivity**: Sclar et al. (2024); Lu et al. (2022)\n- **Broader agent safety**: R-Judge, ToolEmu, InjecAgent\n- **Formal semantics of vagueness**: Lassiter & Goodman (2017)\n- **Garden-path**: Frazier & Rayner (1982)\n- **Ambiguity detection**: Willis et al. (2008); Ezzini et al. (TAPHSIR, 2022)\n- **Year verification needed**: Massey et al. — §1 引用 2013 vs 后文 2014, 需确认正确年份\n\n## Code/Data Release Plan [Dream A6 — three-tier consistent]\n\nMust commit to releasing:\n1. All 300 clause pairs (ambiguous + unambiguous variants) with type labels\n2. Evaluation scripts (τ²-bench integration, cross-judge pipeline)\n3. Statistical analysis code (all tests, bootstrap CI computation)\n4. Agent trace samples (anonymized) for reproducibility of C5\n\n## Figure Plan [Dream A12]\n\nMinimum figures for paper (zero-figure paper flagged in dream):\n1. **Figure 1**: System architecture / experimental pipeline overview (§4 Method)\n2. **Figure 2**: Forest plot — per-type binary effect sizes with 95% CI (§5 C1)\n3. **Figure 3**: Model × Type heatmap — violation rates across 4 models × 6 types (§5 C4)\n4. **Figure 4**: Visibility mechanism — CP vs scopal violation rates + trace evidence (§5 C3)\n5. **Figure 5**: Failure mode × type stacked bar/Sankey — per-type failure mode distribution (§6 C5)\n6. **Figure 6**: Cross-model failure mode consistency — side-by-side gpt-5.4 vs gpt-4.1 per-type distributions showing 5/6 convergence (§6 C5, supports C4)\n7. **Figure 7**: Annotated trace pair — CP (conflict detection) vs scopal (surface adoption) (§6 C5)\n\n## Berry & Kamsties Operationalization Note [Dream best Q5]\n\nBerry & Kamsties define nocuity as inter-reader divergence. Our design measures agent-vs-intent deviation. Full study should additionally test whether different models adopt different readings of the same ambiguous clause (true inter-model nocuity). If 4 models produce 4 different interpretations of the same clause → true nocuity. If all 4 adopt the same wrong interpretation → systematic bias, still nocuous but for different reason. Report inter-model agreement on ambiguous clauses as supplementary analysis.\n\n## Contingency Framing [RESOLVED — Scenario C occurred]\n\n> plan_002 结果: Scenario C 发生（omnibus p=0.0001, 所有类型 nocuous 但 severity 有显著差异）。\n> Framing 已 pivot 到 \"Differential Nocuity\" + \"Layer Hierarchy\" (D020)。本节仅保留历史记录。\n\n## Claude Baseline — RESOLVED [2026-05-20]\n\n✅ Claude works via OpenRouter proxy (47.94.22.126/v1) with provider prefix `anthropic/claude-sonnet-4-6`. 600 episodes complete (plan_002c). Claude shows lowest overall vulnerability (30.3%) and remarkable auth_scope robustness (12% vs GPT-5.4 64%).\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: full_study_clause_generation\n  claim: C1, C2, C3\n  description: 'Generate remaining clauses for full study: coreferential (50 new),\n    authorization_scope (50 new), lexical (+20 to reach 50), incompleteness (+20 to\n    reach 50). Total 140 new clauses. Validate all 300 clauses (50/type × 6 types)\n    for completeness and cross-type balance. Mix CP format per Reviewer suggestion\n    (labeled + unlabeled).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n- id: plan_001b\n  name: new_type_mini_pilot\n  claim: C1 (validation)\n  description: 'Mini-pilot for coreferential + authorization_scope (never tested):\n    5 clauses/type × 2 conditions × 1 model (gpt-5.4) = 20 episodes. Verify: (a) ambiguous\n    triggers violations (b) unambiguous control < 15%. If systematic issues found,\n    fix clause design before full study. API cost negligible (~$2). Per Reviewer warning\n    on untested types.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_002\n  name: full_study_api\n  claim: C1, C2, C3, C4, C5\n  description: 'Run 300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6)\n    = 1,800 episodes on τ²-bench. Cross-judge evaluation. Output: episodes.jsonl +\n    judgments.jsonl. No GPU needed. Claude via OpenRouter proxy (base_url=http://47.94.22.126/v1).\n    [2026-05-20] Claude added per distill gap (4/8 papers use Claude baseline).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_001b\n  - plan_010\n  status: planned\n- id: plan_003\n  name: full_study_opensource\n  claim: C1, C2, C3, C4, C5\n  description: 'Run 300 clauses × 2 conditions × 2 open-source models via OpenRouter\n    API: qwen/qwen3-235b-a22b (235B MoE, Alibaba) + deepseek/deepseek-chat-v3-0324\n    (DeepSeek) = 1,200 episodes on τ²-bench. Cross-judge uses API models. Can run\n    in parallel with plan_002. No GPU needed. [2026-05-20] Pivoted from local GPU\n    → API: OpenRouter proxy confirmed to support Qwen3 and DeepSeek models. Eliminates\n    48h GPU requirement. Provider prefix required (e.g. qwen/qwen3-235b-a22b, not\n    qwen3-235b-a22b).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_004\n  name: full_study_analysis\n  claim: C1, C2, C3, C4\n  description: 'Statistical analysis of full study data (3,000 episodes): (a) Binary\n    effect per type with bootstrap CI (C1) (b) Omnibus χ² + pairwise across 6 types\n    (C2) (c) Visibility comparison: CP vs scopal rates (C3) (d) Model × type interaction:\n    5×6 contingency + logistic regression (C4) Report effect sizes + CI for all comparisons\n    per Reviewer suggestion. [Dream A3] Power analysis: report MDE for C2 (given N=250/type\n    pooled) and C3 (given N=250 per type). If V < 0.20 but MDE > observed V, discuss\n    underpowered possibility. [Dream A4] TOST equivalence test with both ±15pp and\n    ±10pp margins. Justify margin choice explicitly. [Dream A10] Report per-type information\n    delta (token count difference between ambiguous and unambiguous variants) as control\n    variable. [Dream B&K] Inter-model agreement on ambiguous clauses: do 5 models\n    adopt same or different interpretations? (supplementary analysis)\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_005\n  name: error_analysis\n  claim: C5\n  description: \"Qualitative analysis of agent traces from full study: (a) Sample 50\\\n    \\ violation traces per type (300 total) (b) Classify failure modes (scope misapplication,\\\n    \\ conservative refusal,\\n    assumption-based action, arbitrary rule selection,\\\n    \\ etc.)\\n(c) Cross-type failure mode distribution (d) Visibility mechanism: compare\\\n    \\ CP traces (explicit conflict detection\\n    behavior) vs scopal traces (surface\\\n    \\ scope adoption without awareness)\\n(e) Model-specific failure patterns (connect\\\n    \\ to C4)\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_006\n  name: reliability_test\n  claim: C1, C2\n  description: 'Test-retest reliability: select 30 representative clauses (5/type),\n    run 3 independent replicates × 2 conditions × 2 API models (gpt-5.4, gpt-4.1)\n    = 360 episodes. Local models added when plan_003 GPU available. Compute ICC for\n    per-clause violation rates. Addresses Reviewer warning about ±8pp sampling noise\n    (scopal 51.7% → 43.3% across MVP/diag). Bootstrap CI width should be < 10pp for\n    key comparisons. [2026-05-20] API portion: 330/360 episodes complete (28/30 clauses),\n    judgments pending.\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  status: planned\n- id: plan_007\n  name: realism_validation\n  claim: C1 (methodological)\n  description: \"Validate synthetic ambiguity injection realism: (a) Linguistic property\\\n    \\ comparison with DRIP-R natural ambiguities\\n    (sentence length, parse depth,\\\n    \\ Flesch-Kincaid, TTR) + KS tests\\n(b) Optional: discriminator test if DRIP-R\\\n    \\ data accessible Addresses RC4 (ecological validity).\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_009\n  name: judge_calibration\n  claim: C1 (methodological)\n  description: 'LLM-as-judge calibration per distilled research norm (5/8 papers):\n    (a) Sample 100 episodes stratified by type×model×condition (b) Human expert labels\n    (2 annotators, target κ ≥ 0.75) (c) Compute judge precision/recall/F1 against\n    human ground truth (d) Per-severity-tier agreement rates (e) Report in Method\n    section as standard practice per AgentAuditor/DRIP-R [Dream A7] Upgraded P1→P0:\n    Dream best-tier reviewers identified this as \"single most critical missing validation.\"\n    Without it, entire measurement chain from episode to violation label is unvalidated.\n    κ=0.91 measures LLM-LLM agreement, not accuracy.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  name: perturbation_control\n  claim: C1 (causal validity)\n  description: '[Dream A9] Non-ambiguity perturbation control arm to distinguish ambiguity-specific\n    harm from general prompt brittleness. Generate 30 clause pairs with non-ambiguity\n    perturbations: (a) 15 synonym substitution pairs (replace key terms with synonyms)\n    (b) 15 clause reordering pairs (reorder conditions without changing meaning) Run\n    30 × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6) = 180 episodes.\n    Key metric: Δ_net = Δ_ambiguity - Δ_perturb (net ambiguity-specific effect). [Reviewer升级]\n    必须在 plan_002/003 full study 之前完成—— 如果 perturbation Δpp ≈ ambiguity Δpp，2,400 episodes\n    全部无效。 低成本验证（30 pairs + 120 episodes API）优先于高成本投入。 [判定标准 — 5 档]: PASS: Δ_perturb\n    < 5pp (CI含0), ratio < 0.15 → C1 因果 claim 最强形式 PASS+caveat: 5-10pp, ratio 0.15-0.30\n    → 报告 perturbation baseline, C1 写 net effect CONDITIONAL: 10-15pp, ratio 0.30-0.45\n    → 需 Δ_net > 20pp 且显著才可发表 WARNING: 15-20pp, ratio 0.45-0.60 → C1 改为 \"additional\n    violations beyond sensitivity\" FAIL: > 20pp, ratio > 0.60 → 无法声称 ambiguity-specific,\n    需根本重新设计 [Power 注意]: N=120 对 10pp 差异 power ≈ 30%. 用 CI 宽度判定, 非 p-value. 若 CI 过宽(>15pp\n    width), 追加 60 episodes 压窄至 <10pp width. 输出标准化 verdict 文件: perturbation_Δpp, ambiguity_Δpp,\n    net_Δpp, CI, ratio, verdict.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_017\n  name: sopbench_cross_benchmark\n  claim: C1 (generalizability), C2 (partial)\n  description: 'Cross-benchmark C1 replication on SOPBench (Li et al., 2025). 7 domains\n    (Bank, DMV, Healthcare, Hotel, Library, University, Online Market) all different\n    from τ²-bench (retail + airline). Select 2 domains (Healthcare + Bank) for maximum\n    domain diversity. Construct 100 clause pairs (50/domain) covering 3-4 ambiguity\n    types (incompleteness, auth_scope, lexical, conditional_precedence) from SOPBench''s\n    NL SOP constraints. Run 100 pairs × 2 conditions × 5 models = 1,000 episodes.\n    SOPBench has rule-based verifier — no LLM judge needed. Key metrics: (a) Does\n    C1 binary effect replicate? (b) Is incompleteness still highest-risk type? (c)\n    Cross-benchmark effect size correlation. Addresses SF-8 (single benchmark external\n    validity). Result goes in Appendix with 1-sentence summary in main text. [2026-05-22]\n    Approved by user. Estimated 1 day including clause construction.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n- id: plan_008\n  name: classifier_poc\n  claim: practical contribution\n  description: 'Binary ambiguity detector PoC: fine-tune DeBERTa-v3-large on annotated\n    clause pairs (ambiguous/unambiguous labels). Eval on held-out set. Demonstrates\n    practical applicability of findings. Phase 3 from IDEA_BRIEF, scoped to PoC for\n    EMNLP.\n\n    '\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: diag_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_002\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_006\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_009\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cross_judge_kappa_weighted: 0.685\n    cross_judge_exact_agreement: 0.76\n    cross_judge_binary_kappa: 0.74\n    human_llm_pooled_kappa_weighted: 0.807\n    human_inter_annotator_kappa_weighted: 0.762\n    n_episodes: 100\n- exp_id: plan_002c\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_003a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_003b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_004\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_010\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_violations_coded: 614\n    types_unanimous_dominant_fm: 3/6\n    types_majority_dominant_fm: 6/6\n    inter_coder_kappa: 0.5173\n    percent_agreement: 0.656\n    disambiguation_awareness_overall: 0.046\n    elapsed_seconds: 98.5\n- exp_id: plan_011\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_delta_pp: -6.6\n    overall_baseline: 0.41\n    overall_mitigated: 0.343\n    auth_scope_delta_pp: -18\n    incompleteness_delta_pp: -3.4\n    lexical_delta_pp: -8.9\n    cond_prec_delta_pp: -8.1\n    scopal_delta_pp: -4.3\n    best_model_gpt41_delta_pp: -11.1\n    worst_model_deepseek_delta_pp: -2.5\n    total_mitigated_episodes: 1256\n    total_baseline_episodes: 1499\n    elapsed_seconds: 2954\n- exp_id: plan_012\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1: 0.6322\n    binary_f1: 0.8055\n    binary_fpr: 0.044\n    best_type_f1:\n      conditional_precedence: 0.94\n    worst_type_f1:\n      incompleteness: 0.34\n    per_type_f1:\n      conditional_precedence: 0.94\n      scopal: 0.75\n      coreferential: 0.7\n      authorization_scope: 0.58\n      lexical: 0.39\n      incompleteness: 0.34\n    total_clauses: 500\n    folds: 5\n- exp_id: plan_013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gemini_2.5_flash:\n      amb_rate: 0.376\n      unamb_rate: 0.04\n      delta_pp: 33.6\n      or: 14.46\n      p_value: 4.0e-22\n      c1_replicates: true\n      c2_rank_corr: 0.6\n      c2_rank_p: 0.285\n      type_ranking:\n      - lexical\n      - incompleteness\n      - scopal\n      - cond_prec\n      - auth_scope\n    llama_4_scout:\n      amb_rate: 0.376\n      unamb_rate: 0.176\n      delta_pp: 20\n      or: 2.82\n      p_value: 7.7e-07\n      c1_replicates: true\n      c2_rank_corr: 0.9\n      c2_rank_p: 0.037\n      type_ranking:\n      - incompleteness\n      - auth_scope\n      - lexical\n      - scopal\n      - cond_prec\n    summary:\n      c1_replicated: 7/7\n      c2_replicated: 2/2 positive (LLaMA ρ=0.90 p=0.037, Gemini ρ=0.60 p=0.285)\n      incompleteness_universal: 7/7 (≥46%)\n      total_episodes: 1000\n    bugfix: reference_rank corrected from arbitrary order to main-study pooled descending;\n      OR inverted\n- exp_id: plan_014\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_episodes: 300\n    delta_perturb_pp: -0.67\n    ci_95_bootstrap:\n    - -8\n    - 6.67\n    ci_upper_bound: 6.67\n    ci_width: 14.67\n    mcnemar_p: 1\n    verdict: PASS\n    plan_010_ci_upper: 13.33\n    ci_upper_reduction: 6.66\n- exp_id: plan_015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pooled_escalation_rate: 0.692\n    pooled_restriction_rate: 0\n    binomial_p: 5.5e-05\n    models_majority_escalation: 4/5\n    n_total: 104\n    n_escalation: 72\n- exp_id: plan_016\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    generic_awareness_overall_delta_pp: 1.33\n    type_specific_auth_scope_delta_pp: -12\n    type_specific_auth_scope_p: 0.07\n    type_specific_incompleteness_delta_pp: 14\n    type_specific_incompleteness_p: 0.118\n    type_specific_lexical_delta_pp: -2\n    type_specific_lexical_p: 1\n    total_new_episodes: 450\n    total_judge_calls: 450\n    model: gpt-5.4\n    all_mcnemar_p_gt_005: true\n\n\n## what_if (hypothetical experiments — additive)\n\n- name: kappa_reannotation_success\n  claim: C5 type-mechanism dissociation\n  description: 'Human re-annotation with improved codebook (collapsed spurious-compliance/structural-misparse\n    boundary) yields κ=0.42. Paper updates: contribution (3) upgrades from ''initial\n    evidence'' to ''supported by convergent LLM-coded and human evidence''; abstract/intro/analysis\n    remove ''initial'' qualifier; limitations κ=0.15 sentence replaced with κ=0.42;\n    Discussion adds human-validated claim.'\n  estimated_gpu_hours: 0.0\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n\n重要：tables 中使用 YAML flow sequence 时，所有字符串必须加双引号（如 `columns: [\"Judge\", \"Biased?\"]`），否则 `?` `:` 等字符会导致解析失败。\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-23T19:02:23.391Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-23T19:02:23.391Z",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43"
}
```

---

## Round 1

26 recorded events

### User

_source line 3 · 2026-05-23T19:02:23.425Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：κ re-annotation succeeds marginally (meets threshold but doesn't strongly validate LLM coding), SOPBench partially replicates — paper's quantitative core is strong but qualitative contribution needs softening
核心假设：['0.35 ≤ κ_reannotation < 0.45 (fair), dominant failure modes match in 3-4/6 types with boundary-type disagreements (auth_scope/incompleteness)', 'SOPBench C1 replicates (Δ≥15pp) but with smaller effect size or 1 model anomaly', 'SOPBench type ranking weakly correlated (0.30 ≤ ρ < 0.60) or only 2-3 types testable', 'At least one reviewer flags C3 within-judge fragility as undermining the layer claim', "C4 model×type interaction accepted as interesting but reviewer questions whether 5 models suffice for 'differential safety training' claims"]
关键指标范围：{'kappa_reannotation': [0.35, 0.44], 'sopbench_c1_delta_pp': [15, 25], 'sopbench_type_rank_rho': [0.3, 0.59], 'c5_human_llm_dominant_mode_agreement': [3, 4], 'expected_arr_score': [3.5, 3.99], 'expected_reviewer_confidence': [3.0, 3.5]}
叙事方向：C1+C4 carry the paper; C5 downgraded from 'validated taxonomy' to 'convergent LLM-coded and human evidence with moderate agreement.' Abstract replaces 'type-diagnostic failure signatures' with 'type-associated failure patterns.' Contribution (3) retains 'supported by' but adds 'preliminary human validation (κ=0.3X)' qualifier. C3 layer effect moved from standalone finding to subordinate observation under C4 ('the model×type interaction subsumes and explains the aggregate layer gap'). SOPBench mentioned as 'partial cross-domain evidence' rather than 'replication.' Rebuttal strategy: emphasize that κ=0.3X exceeds automated-only (plan_010 κ=0.517), and the 3-4 type agreement covers the theoretically critical types (incompleteness, auth_scope). Still competitive for EMNLP poster — C1 causal design + C4 interaction is sufficient novel contribution even with weakened C5.

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: policy_ambiguity_safety
venue: emnlp-2026
focus: Evaluate the paper's competitiveness at EMNLP 2026 ARR assuming κ re-annotation succeeds (κ≥0.35). Key question: does upgrading contribution (3) from 'initial evidence' to validated move the paper from 3.75 to 4.0? What remaining gaps would reviewers still flag?

## paper_framing.md

# Paper Framing — policy_ambiguity_safety

> 最后更新: 2026-05-23 UTC | 状态: R18 全部 resolved + 6 supplementary experiments (5 done, 1 running)
> 目标: EMNLP 2026 (ARR May cycle, DDL 2026-05-25)
> Dream: dream_20260520T112859 — best 3.5 / median 3.0 / worst 2.5 (pre-pivot; re-dream needed)
> 5-model: 2,997 episodes, C1 confirmed (+34.0pp, 5 models), C4 upgraded (model×type interaction)
> Supplementary experiments (2026-05-22/23):
>   - ✅ Cross-Judge Validation: Fleiss' κ=0.717, rankings preserved (ρ≥0.70), no same-family bias → R18-N2 升级为 validated
>   - ✅ Controlled Confound: ±0.1pp token-count effect, β=+0.027 (p=0.003) → R18-W3 resolved
>   - ✅ Residual Decomposition: ICC=0.749, 15.2pp stochastic / 45.6pp systematic → R18-W2 answered
>   - ✅ Disambiguation Prompting: overall not significant, GPT-4.1 auth_scope -28pp (p=0.001) → rebuttal ammunition
>   - ✅ Human Annotation Prep: 100 traces + codebook ready
>   - 🔄 SOPBench Expansion: DeepSeek ~78% complete

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


## what_if (hypothetical experiments — additive)

- name: kappa_reannotation_success
  claim: C5 type-mechanism dissociation
  description: 'Human re-annotation with improved codebook (collapsed spurious-compliance/structural-misparse
    boundary) yields κ=0.42. Paper updates: contribution (3) upgrades from ''initial
    evidence'' to ''supported by convergent LLM-coded and human evidence''; abstract/intro/analysis
    remove ''initial'' qualifier; limitations κ=0.15 sentence replaced with κ=0.42;
    Discussion adds human-validated claim.'
  estimated_gpu_hours: 0.0

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

重要：tables 中使用 YAML flow sequence 时，所有字符串必须加双引号（如 `columns: ["Judge", "Biased?"]`），否则 `?` `:` 等字符会导致解析失败。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "729a2239-1e83-4796-a7ab-5d472e588b51",
  "type": "user",
  "uuid": "daddae65-6e61-4d40-87b8-17a858331a94",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-23T19:02:23.422Z_

```json
{
  "parentUuid": "daddae65-6e61-4d40-87b8-17a858331a94",
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
  "uuid": "b08ffde2-15a6-41f6-ad44-827d59e46fab",
  "timestamp": "2026-05-23T19:02:23.422Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-23T19:02:23.422Z_

```json
{
  "parentUuid": "b08ffde2-15a6-41f6-ad44-827d59e46fab",
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
  "uuid": "849078d9-6161-4c16-b61e-cd9081e415e4",
  "timestamp": "2026-05-23T19:02:23.422Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-23T19:02:23.422Z_

```json
{
  "parentUuid": "849078d9-6161-4c16-b61e-cd9081e415e4",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "fcaccb7c-9672-4cc5-b4fa-32973cd173e5",
  "timestamp": "2026-05-23T19:02:23.422Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：κ re-annotation succeeds marginally (meets threshold but doesn't strongly validate LLM coding), SOPBench partially replicates — paper's quantitative core…",
  "leafUuid": "fcaccb7c-9672-4cc5-b4fa-32973cd173e5",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Human re-annotation of failure modes for differential nocuity validation",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43"
}
```

---

### Assistant

_source line 9 · 2026-05-23T19:02:29.238Z_

I'll examine the experiment plan entries and the median tier definition to produce detailed imagined results for each planned experiment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fcaccb7c-9672-4cc5-b4fa-32973cd173e5",
  "isSidechain": false,
  "requestId": "req_011CbL22pR11SA8uEZrhVtLv",
  "type": "assistant",
  "uuid": "b68dfd7d-b32e-43ef-a117-a4e127edf17f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BMsgRSjA46ydeBeLhGSsft",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21521,
      "cache_read_input_tokens": 11447,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21521,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 262,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 21521,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21521
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

_source line 10 · 2026-05-23T19:02:33.474Z_

<details open><summary>🔧 Tool call — Agent · `toolu_011hZHDcKETe64d1o3aiUcmz`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find experiment plan details",
  "prompt": "Search the project directory /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4 for any files that contain detailed experiment plans, especially looking for files related to: plan_001, plan_001b, plan_002, plan_003, plan_004, plan_005, plan_006, plan_007, plan_009, plan_010, plan_017, plan_008. I need to understand what metrics each experiment is expected to produce. Also look for any \"what_if\" or \"kappa_reannotation\" related files. Search breadth: medium."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b68dfd7d-b32e-43ef-a117-a4e127edf17f",
  "isSidechain": false,
  "requestId": "req_011CbL22pR11SA8uEZrhVtLv",
  "type": "assistant",
  "uuid": "48b580c8-2c49-4f51-a41d-29a242586999",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BMsgRSjA46ydeBeLhGSsft",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21521,
      "cache_read_input_tokens": 11447,
      "output_tokens": 262,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21521,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 262,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 21521,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21521
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

_source line 11 · 2026-05-23T19:03:44.315Z_

<details><summary>↩ Tool result · `toolu_011hZHDcKETe64d1o3aiUcmz`</summary>

```text
Perfect! Now I have comprehensive information about the experiment plans. Let me compile a final summary report:

## Summary Report: Experiment Plans and Expected Metrics

Based on my search through the project directory `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4`, I have found detailed documentation for multiple experiment plans related to a policy ambiguity and safety research project targeting EMNLP 2026. Here's what each experiment is designed to produce:

### **Core Experiment Plans**

#### **plan_001: Full Study Clause Generation**
- **Status**: P0 (Must-run)
- **Description**: Generate 140 new clauses across 6 types (50 per type for completeness/balance)
- **Expected Metrics/Outputs**:
  - 300 total validated clauses (50 per type across 6 ambiguity types)
  - Cross-type balance verification
  - Clause quality validation scores

#### **plan_001b: New Type Mini-Pilot**
- **Status**: P0
- **Description**: Mini-pilot testing coreferential + authorization_scope types (5 clauses each, 2 conditions, 1 model)
- **Expected Metrics**:
  - Violation trigger validation (ambiguous violations must occur)
  - Unambiguous control violation rate (<15%)
  - Clause design issue detection

#### **plan_002: Full Study API (Primary Experiment)**
- **Status**: P0 - COMPLETED
- **Description**: Run 1,800 episodes (300 clauses × 2 conditions × 3 API models: gpt-5.4, gpt-4.1, claude-sonnet-4-6)
- **Expected Metrics/Outputs**:
  - **episodes.jsonl**: Raw agent traces and responses
  - **judgments.jsonl**: Cross-judge violation labels (3-tier severity)
  - Binary effect: +34.0pp violation increase (ambiguous 41.0% vs unambiguous 6.9%, OR=15.1)
  - Per-model effects (Claude +25.7pp, GPT-4.1 +34.7pp, GPT-5.4 +38.3pp)

#### **plan_003: Full Study Open-Source Models**
- **Status**: P0
- **Description**: Run 1,200 episodes (300 clauses × 2 conditions × 2 open-source API models: qwen3-235b, deepseek-v3)
- **Expected Metrics**:
  - Same structure as plan_002
  - Per-model violation rates (Qwen3 +32.4pp, DeepSeek +39.0pp)
  - Cross-model consistency data

#### **plan_004: Full Study Analysis**
- **Status**: P0 - COMPLETED
- **Description**: Comprehensive statistical analysis of 3,000 episodes
- **Expected Metrics/Outputs**:
  - **C1 (Binary Effect)**: McNemar test, bootstrap CI, OR=15.1 [10.78, 21.17]
  - **C2 (Type Hierarchy)**: Omnibus χ²=28.02, p=3.6×10⁻⁵, V=0.137 (3-tier: incompleteness 53.6% >> mid-tier 36.8-42.8% >> coreferential 31.6%)
  - **C3 (Layer Effect)**: Specification-layer 44.0% vs Linguistic-layer 37.9%, Δ=6.08pp, p=0.017
  - **C4 (Model×Type Interaction)**: Matrix showing per-model vulnerability profiles (e.g., auth_scope range: Claude 12% → GPT-5.4 64%, 52pp span)
  - Per-type information delta (token count differences)
  - Inter-model agreement metrics (Fleiss κ=0.384)

#### **plan_005: Error Analysis**
- **Status**: P0 - COMPLETED
- **Description**: Qualitative analysis of 245 violation traces (123 gpt-5.4, 122 gpt-4.1)
- **Expected Metrics/Outputs**:
  - **Failure mode taxonomy** (5 categories):
    - Structural Misparse (SM): 25-28%
    - Gap-Filling (GF): ~33%
    - Boundary Violation (BV): 26-32%
    - Spurious Compliance (SC): variable
    - Conservative Refusal (CR): <3%
  - **Type-specific signatures** (e.g., auth_scope→unauthorized_escalation 72-83%, incompleteness→gap_filling 61-66%)
  - **Cross-model consistency**: 5/6 types share dominant failure mode
  - **Ambiguity Blindness**: awareness rate <5-11%, surface adoption >88%
  - **Layer mechanism**: Ling-layer dominated by scope misapplication, spec-layer by escalation/guessing
  - Cohen's κ=0.594 (inter-coder agreement on failure modes)

#### **plan_006: Reliability Test**
- **Status**: P1 - COMPLETED
- **Description**: Test-retest reliability with 30 representative clauses, 3 replicates, 2 API models
- **Expected Metrics**:
  - **ICC (Intra-class Correlation)**: 0.919 [0.892, 0.940] (excellent overall)
  - Per-type ICC: Ling-layer 0.976-0.989 > Spec-layer 0.807-0.857
  - Binary ICC: 0.847 (good)
  - Bootstrap CI width confirmation

#### **plan_009: Judge Calibration**
- **Status**: P0/P1 - COMPLETED
- **Description**: Human-LLM judge agreement on 100 stratified episodes
- **Expected Metrics/Outputs**:
  - **Inter-annotator agreement**: Kappa (binary)=0.798, (weighted)=0.762
  - **Human-LLM agreement**:
    - Annotator 1 vs LLM: κ=0.775 (binary), κ=0.868 (weighted)
    - Annotator 2 vs LLM: κ=0.692 (binary), κ=0.745 (weighted)
  - Judge precision/recall/F1 per severity tier
  - Annotation guidelines for 5-category failure mechanism coding

#### **plan_010: Perturbation Control**
- **Status**: P0 - COMPLETED
- **Description**: Non-ambiguity control arm (30 pairs: synonym substitution + clause reordering, 120 episodes, 3 API models)
- **Expected Metrics/Outputs**:
  - **verdict.json**: Control verdict file
    - Δ_perturb = 3.33pp (CI: [-5.0, 13.33], contains 0)
    - Ambiguity Δ = 38.0pp
    - Net Δ = 34.67pp (CI: [24.67, 43.0])
    - Ratio = 0.0877 (ratio of perturbation to ambiguity effect)
    - **Verdict**: PASS (perturbation effect <5pp, rules out general prompt brittleness)
  - Per-model breakdowns (GPT-5.4, GPT-4.1)
  - Per-perturbation-type effects (synonym substitution vs reordering)

#### **plan_017: SOPBench Cross-Benchmark**
- **Status**: P1+ - IN PROGRESS
- **Description**: Generalization test on SOPBench (100 clause pairs, 2 domains: Healthcare + Bank, 5 models)
- **Expected Metrics**:
  - C1 binary effect replication check
  - Per-domain comparison (expected <13pp cross-domain variation)
  - Type hierarchy stability across domains
  - Cross-benchmark effect size correlation
  - Result: 1,000 episodes with rule-based verification

#### **plan_008: Classifier PoC**
- **Status**: P2 (Nice-to-have)
- **Description**: Binary ambiguity detector fine-tuning on DeBERTa-v3-large
- **Expected Metrics**:
  - Precision/Recall/F1 on held-out evaluation set
  - Practical applicability demonstration

---

### **Supplementary/Related Experiments**

#### **Kappa Re-annotation (PENDING)**
- **Location**: `/artifacts/reannotation/`
- **Purpose**: Improve human inter-annotator agreement on failure mode categories
- **Materials Ready**:
  - 100 traces prepared for annotation
  - 5-category annotation guideline (with decision tree)
  - Annotation sheet in CSV/JSONL format
- **Expected Outcome**:
  - Target: Human κ improvement from 0.15 → 0.4+
  - Strategy: Category collapsing (5-cat → 4-cat → 3-cat)
  - Collapsed kappa targets: 4-cat κ≈0.52, 3-cat κ≈0.48

#### **Convergence Analysis** (COMPLETED)
- **Expected Metrics**:
  - 39 "universal" clauses (5/5 models violated)
  - 85 "majority" clauses (3-4/5 models violated)
  - 92 "model-specific" clauses (1-2/5 models violated)
  - 84 "safe" clauses (0/5 models violated)
  - Cross-type convergence patterns
  - Mechanism convergence rates (41.3% convergent violations, 52/124 majority-convergent clauses with identical failure modes)

#### **Related Analysis Files** (Already Generated):
- `analysis_systematic_nocuity_summary.md`: Convergence distribution, universal vs safe linguistic features
- `human_collapsed_kappa.json`: Kappa reconstruction from appendix statistics (original κ=0.15, collapsed-4-cat κ=0.52)
- `compute_collapsed_kappa_v3.py`: Script for kappa analysis with confusion matrix reconstruction

---

### **Key Metrics Summary Table**

| Experiment | Sample Size | Primary Metrics | Status |
|------------|------------|-----------------|--------|
| plan_001 | 300 clauses | Validation scores, cross-type balance | Planned |
| plan_001b | 20 episodes | Violation rate, control validation | Planned |
| plan_002 | 1,800 episodes | Binary effect +34.0pp, per-model Δpp | DONE |
| plan_003 | 1,200 episodes | Open-source model effects | Planned |
| plan_004 | 3,000 episodes | χ², V=0.137, interaction matrix | DONE |
| plan_005 | 245 traces | Failure mode taxonomy, κ=0.594 | DONE |
| plan_006 | 30×3 clauses | ICC=0.919, per-type ICC | DONE |
| plan_009 | 100 episodes | Inter-annotator κ=0.798 | DONE |
| plan_010 | 120 episodes | Δ_perturb=3.33pp, verdict=PASS | DONE |
| plan_017 | 1,000 episodes | Cross-benchmark replication | IN PROGRESS |
| plan_008 | TBD | Classifier F1 score | Planned |
| Kappa Re-annotation | 100 traces | Target κ→0.4+ (4-cat), guidelines | READY |

---

### **File Locations**

**Main documentation**:
- `/projects/policy_ambiguity_safety/experiment_plan.yaml` (comprehensive experiment registry)
- `/projects/policy_ambiguity_safety/writing_plan.yaml` (paper target metrics and visualization plan)
- `/projects/policy_ambiguity_safety/paper_framing.md` (detailed core claims C1-C5)
- `/projects/policy_ambiguity_safety/ROADMAP.md` (current status and progress)

**Execution artifacts**:
- `/artifacts/plan_002/` (full study results)
- `/artifacts/plan_005/` (error analysis)
- `/artifacts/plan_006/` (reliability test)
- `/artifacts/plan_009/` (judge calibration)
- `/artifacts/plan_010/` (perturbation control verdict)
- `/artifacts/reannotation/` (kappa re-annotation materials)
- `/artifacts/convergence_analysis/` (systematic nocuity analysis)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48b580c8-2c49-4f51-a41d-29a242586999",
  "isSidechain": false,
  "promptId": "729a2239-1e83-4796-a7ab-5d472e588b51",
  "type": "user",
  "uuid": "632f0b4a-8c14-4460-b7e0-aba29ae7a28a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search the project directory /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4 for any files that contain detailed experiment plans, especially looking for files related to: plan_001, plan_001b, plan_002, plan_003, plan_004, plan_005, plan_006, plan_007, plan_009, plan_010, plan_017, plan_008. I need to understand what metrics each experiment is expected to produce. Also look for any \"what_if\" or \"kappa_reannotation\" related files. Search breadth: medium.",
    "agentId": "a444ba8d816656cf3",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have comprehensive information about the experiment plans. Let me compile a final summary report:\n\n## Summary Report: Experiment Plans and Expected Metrics\n\nBased on my search through the project directory `/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4`, I have found detailed documentation for multiple experiment plans related to a policy ambiguity and safety research project targeting EMNLP 2026. Here's what each experiment is designed to produce:\n\n### **Core Experiment Plans**\n\n#### **plan_001: Full Study Clause Generation**\n- **Status**: P0 (Must-run)\n- **Description**: Generate 140 new clauses across 6 types (50 per type for completeness/balance)\n- **Expected Metrics/Outputs**:\n  - 300 total validated clauses (50 per type across 6 ambiguity types)\n  - Cross-type balance verification\n  - Clause quality validation scores\n\n#### **plan_001b: New Type Mini-Pilot**\n- **Status**: P0\n- **Description**: Mini-pilot testing coreferential + authorization_scope types (5 clauses each, 2 conditions, 1 model)\n- **Expected Metrics**:\n  - Violation trigger validation (ambiguous violations must occur)\n  - Unambiguous control violation rate (<15%)\n  - Clause design issue detection\n\n#### **plan_002: Full Study API (Primary Experiment)**\n- **Status**: P0 - COMPLETED\n- **Description**: Run 1,800 episodes (300 clauses × 2 conditions × 3 API models: gpt-5.4, gpt-4.1, claude-sonnet-4-6)\n- **Expected Metrics/Outputs**:\n  - **episodes.jsonl**: Raw agent traces and responses\n  - **judgments.jsonl**: Cross-judge violation labels (3-tier severity)\n  - Binary effect: +34.0pp violation increase (ambiguous 41.0% vs unambiguous 6.9%, OR=15.1)\n  - Per-model effects (Claude +25.7pp, GPT-4.1 +34.7pp, GPT-5.4 +38.3pp)\n\n#### **plan_003: Full Study Open-Source Models**\n- **Status**: P0\n- **Description**: Run 1,200 episodes (300 clauses × 2 conditions × 2 open-source API models: qwen3-235b, deepseek-v3)\n- **Expected Metrics**:\n  - Same structure as plan_002\n  - Per-model violation rates (Qwen3 +32.4pp, DeepSeek +39.0pp)\n  - Cross-model consistency data\n\n#### **plan_004: Full Study Analysis**\n- **Status**: P0 - COMPLETED\n- **Description**: Comprehensive statistical analysis of 3,000 episodes\n- **Expected Metrics/Outputs**:\n  - **C1 (Binary Effect)**: McNemar test, bootstrap CI, OR=15.1 [10.78, 21.17]\n  - **C2 (Type Hierarchy)**: Omnibus χ²=28.02, p=3.6×10⁻⁵, V=0.137 (3-tier: incompleteness 53.6% >> mid-tier 36.8-42.8% >> coreferential 31.6%)\n  - **C3 (Layer Effect)**: Specification-layer 44.0% vs Linguistic-layer 37.9%, Δ=6.08pp, p=0.017\n  - **C4 (Model×Type Interaction)**: Matrix showing per-model vulnerability profiles (e.g., auth_scope range: Claude 12% → GPT-5.4 64%, 52pp span)\n  - Per-type information delta (token count differences)\n  - Inter-model agreement metrics (Fleiss κ=0.384)\n\n#### **plan_005: Error Analysis**\n- **Status**: P0 - COMPLETED\n- **Description**: Qualitative analysis of 245 violation traces (123 gpt-5.4, 122 gpt-4.1)\n- **Expected Metrics/Outputs**:\n  - **Failure mode taxonomy** (5 categories):\n    - Structural Misparse (SM): 25-28%\n    - Gap-Filling (GF): ~33%\n    - Boundary Violation (BV): 26-32%\n    - Spurious Compliance (SC): variable\n    - Conservative Refusal (CR): <3%\n  - **Type-specific signatures** (e.g., auth_scope→unauthorized_escalation 72-83%, incompleteness→gap_filling 61-66%)\n  - **Cross-model consistency**: 5/6 types share dominant failure mode\n  - **Ambiguity Blindness**: awareness rate <5-11%, surface adoption >88%\n  - **Layer mechanism**: Ling-layer dominated by scope misapplication, spec-layer by escalation/guessing\n  - Cohen's κ=0.594 (inter-coder agreement on failure modes)\n\n#### **plan_006: Reliability Test**\n- **Status**: P1 - COMPLETED\n- **Description**: Test-retest reliability with 30 representative clauses, 3 replicates, 2 API models\n- **Expected Metrics**:\n  - **ICC (Intra-class Correlation)**: 0.919 [0.892, 0.940] (excellent overall)\n  - Per-type ICC: Ling-layer 0.976-0.989 > Spec-layer 0.807-0.857\n  - Binary ICC: 0.847 (good)\n  - Bootstrap CI width confirmation\n\n#### **plan_009: Judge Calibration**\n- **Status**: P0/P1 - COMPLETED\n- **Description**: Human-LLM judge agreement on 100 stratified episodes\n- **Expected Metrics/Outputs**:\n  - **Inter-annotator agreement**: Kappa (binary)=0.798, (weighted)=0.762\n  - **Human-LLM agreement**:\n    - Annotator 1 vs LLM: κ=0.775 (binary), κ=0.868 (weighted)\n    - Annotator 2 vs LLM: κ=0.692 (binary), κ=0.745 (weighted)\n  - Judge precision/recall/F1 per severity tier\n  - Annotation guidelines for 5-category failure mechanism coding\n\n#### **plan_010: Perturbation Control**\n- **Status**: P0 - COMPLETED\n- **Description**: Non-ambiguity control arm (30 pairs: synonym substitution + clause reordering, 120 episodes, 3 API models)\n- **Expected Metrics/Outputs**:\n  - **verdict.json**: Control verdict file\n    - Δ_perturb = 3.33pp (CI: [-5.0, 13.33], contains 0)\n    - Ambiguity Δ = 38.0pp\n    - Net Δ = 34.67pp (CI: [24.67, 43.0])\n    - Ratio = 0.0877 (ratio of perturbation to ambiguity effect)\n    - **Verdict**: PASS (perturbation effect <5pp, rules out general prompt brittleness)\n  - Per-model breakdowns (GPT-5.4, GPT-4.1)\n  - Per-perturbation-type effects (synonym substitution vs reordering)\n\n#### **plan_017: SOPBench Cross-Benchmark**\n- **Status**: P1+ - IN PROGRESS\n- **Description**: Generalization test on SOPBench (100 clause pairs, 2 domains: Healthcare + Bank, 5 models)\n- **Expected Metrics**:\n  - C1 binary effect replication check\n  - Per-domain comparison (expected <13pp cross-domain variation)\n  - Type hierarchy stability across domains\n  - Cross-benchmark effect size correlation\n  - Result: 1,000 episodes with rule-based verification\n\n#### **plan_008: Classifier PoC**\n- **Status**: P2 (Nice-to-have)\n- **Description**: Binary ambiguity detector fine-tuning on DeBERTa-v3-large\n- **Expected Metrics**:\n  - Precision/Recall/F1 on held-out evaluation set\n  - Practical applicability demonstration\n\n---\n\n### **Supplementary/Related Experiments**\n\n#### **Kappa Re-annotation (PENDING)**\n- **Location**: `/artifacts/reannotation/`\n- **Purpose**: Improve human inter-annotator agreement on failure mode categories\n- **Materials Ready**:\n  - 100 traces prepared for annotation\n  - 5-category annotation guideline (with decision tree)\n  - Annotation sheet in CSV/JSONL format\n- **Expected Outcome**:\n  - Target: Human κ improvement from 0.15 → 0.4+\n  - Strategy: Category collapsing (5-cat → 4-cat → 3-cat)\n  - Collapsed kappa targets: 4-cat κ≈0.52, 3-cat κ≈0.48\n\n#### **Convergence Analysis** (COMPLETED)\n- **Expected Metrics**:\n  - 39 \"universal\" clauses (5/5 models violated)\n  - 85 \"majority\" clauses (3-4/5 models violated)\n  - 92 \"model-specific\" clauses (1-2/5 models violated)\n  - 84 \"safe\" clauses (0/5 models violated)\n  - Cross-type convergence patterns\n  - Mechanism convergence rates (41.3% convergent violations, 52/124 majority-convergent clauses with identical failure modes)\n\n#### **Related Analysis Files** (Already Generated):\n- `analysis_systematic_nocuity_summary.md`: Convergence distribution, universal vs safe linguistic features\n- `human_collapsed_kappa.json`: Kappa reconstruction from appendix statistics (original κ=0.15, collapsed-4-cat κ=0.52)\n- `compute_collapsed_kappa_v3.py`: Script for kappa analysis with confusion matrix reconstruction\n\n---\n\n### **Key Metrics Summary Table**\n\n| Experiment | Sample Size | Primary Metrics | Status |\n|------------|------------|-----------------|--------|\n| plan_001 | 300 clauses | Validation scores, cross-type balance | Planned |\n| plan_001b | 20 episodes | Violation rate, control validation | Planned |\n| plan_002 | 1,800 episodes | Binary effect +34.0pp, per-model Δpp | DONE |\n| plan_003 | 1,200 episodes | Open-source model effects | Planned |\n| plan_004 | 3,000 episodes | χ², V=0.137, interaction matrix | DONE |\n| plan_005 | 245 traces | Failure mode taxonomy, κ=0.594 | DONE |\n| plan_006 | 30×3 clauses | ICC=0.919, per-type ICC | DONE |\n| plan_009 | 100 episodes | Inter-annotator κ=0.798 | DONE |\n| plan_010 | 120 episodes | Δ_perturb=3.33pp, verdict=PASS | DONE |\n| plan_017 | 1,000 episodes | Cross-benchmark replication | IN PROGRESS |\n| plan_008 | TBD | Classifier F1 score | Planned |\n| Kappa Re-annotation | 100 traces | Target κ→0.4+ (4-cat), guidelines | READY |\n\n---\n\n### **File Locations**\n\n**Main documentation**:\n- `/projects/policy_ambiguity_safety/experiment_plan.yaml` (comprehensive experiment registry)\n- `/projects/policy_ambiguity_safety/writing_plan.yaml` (paper target metrics and visualization plan)\n- `/projects/policy_ambiguity_safety/paper_framing.md` (detailed core claims C1-C5)\n- `/projects/policy_ambiguity_safety/ROADMAP.md` (current status and progress)\n\n**Execution artifacts**:\n- `/artifacts/plan_002/` (full study results)\n- `/artifacts/plan_005/` (error analysis)\n- `/artifacts/plan_006/` (reliability test)\n- `/artifacts/plan_009/` (judge calibration)\n- `/artifacts/plan_010/` (perturbation control verdict)\n- `/artifacts/reannotation/` (kappa re-annotation materials)\n- `/artifacts/convergence_analysis/` (systematic nocuity analysis)"
      }
    ],
    "totalDurationMs": 70827,
    "totalTokens": 71860,
    "totalToolUseCount": 32,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1354,
      "cache_read_input_tokens": 67439,
      "output_tokens": 3060,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1354
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 3060,
          "cache_read_input_tokens": 67439,
          "cache_creation_input_tokens": 1354,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1354,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 13,
      "searchCount": 6,
      "bashCount": 13,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "48b580c8-2c49-4f51-a41d-29a242586999",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-23T19:03:47.361Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CfgEDCwG7kyqEHmWjb2hrF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/artifacts/reannotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "632f0b4a-8c14-4460-b7e0-aba29ae7a28a",
  "isSidechain": false,
  "requestId": "req_011CbL28mr8a37fcem1okYhE",
  "type": "assistant",
  "uuid": "fae27265-5060-4842-820a-e42cb97b72af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011kAPCkwdUe7xuTcyCeeKMe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3316,
      "cache_read_input_tokens": 32968,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3316,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 32968,
          "cache_creation_input_tokens": 3316,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3316
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

_source line 13 · 2026-05-23T19:03:47.374Z_

<details><summary>↩ Tool result · reported error · `toolu_01CfgEDCwG7kyqEHmWjb2hrF`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fae27265-5060-4842-820a-e42cb97b72af",
  "isSidechain": false,
  "promptId": "729a2239-1e83-4796-a7ab-5d472e588b51",
  "type": "user",
  "uuid": "c251486d-dce9-4163-9e43-32cbbbb7b3f1",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-be-idea-gen-0519-4.",
  "sourceToolAssistantUUID": "fae27265-5060-4842-820a-e42cb97b72af",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-23T19:03:49.820Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0112YKcp82AofsngwjuBu9v1`</summary>

```json
{
  "pattern": "**/reannotation*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c251486d-dce9-4163-9e43-32cbbbb7b3f1",
  "isSidechain": false,
  "requestId": "req_011CbL291DJFK32imDR4iZLK",
  "type": "assistant",
  "uuid": "30d61f74-498d-43d3-8584-ee500b8bdf07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RJ4ZgGxsGiQfDvYQ9qJRWT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 133,
      "cache_read_input_tokens": 36284,
      "output_tokens": 58,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 133,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 58,
          "cache_read_input_tokens": 36284,
          "cache_creation_input_tokens": 133,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 133
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

_source line 15 · 2026-05-23T19:03:50.006Z_

<details><summary>↩ Tool result · `toolu_0112YKcp82AofsngwjuBu9v1`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30d61f74-498d-43d3-8584-ee500b8bdf07",
  "isSidechain": false,
  "promptId": "729a2239-1e83-4796-a7ab-5d472e588b51",
  "type": "user",
  "uuid": "20c9e68e-1e7c-4058-a0a4-af78367a1519",
  "toolUseResult": {
    "filenames": [],
    "durationMs": 181,
    "numFiles": 0,
    "truncated": false
  },
  "sourceToolAssistantUUID": "30d61f74-498d-43d3-8584-ee500b8bdf07",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-23T19:03:55.162Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01NMjVrhc44GbvNdkMW5omSP`</summary>

```json
{
  "pattern": "**/experiment_plan*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "20c9e68e-1e7c-4058-a0a4-af78367a1519",
  "isSidechain": false,
  "requestId": "req_011CbL29C8srSjdnvyanzn81",
  "type": "assistant",
  "uuid": "0ecc0834-c98c-4f34-ac54-9ee256bc556a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158HcpsYh9J375jxnmcCnn9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 73,
      "cache_read_input_tokens": 36417,
      "output_tokens": 57,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 73,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 57,
          "cache_read_input_tokens": 36417,
          "cache_creation_input_tokens": 73,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 73
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

_source line 17 · 2026-05-23T19:03:55.347Z_

<details><summary>↩ Tool result · `toolu_01NMjVrhc44GbvNdkMW5omSP`</summary>

```text
projects/policy_ambiguity_safety/experiment_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0ecc0834-c98c-4f34-ac54-9ee256bc556a",
  "isSidechain": false,
  "promptId": "729a2239-1e83-4796-a7ab-5d472e588b51",
  "type": "user",
  "uuid": "1f9d3afd-3958-4dea-af66-3d9ae2ac4974",
  "toolUseResult": {
    "filenames": [
      "projects/policy_ambiguity_safety/experiment_plan.yaml"
    ],
    "durationMs": 181,
    "numFiles": 1,
    "truncated": false
  },
  "sourceToolAssistantUUID": "0ecc0834-c98c-4f34-ac54-9ee256bc556a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-23T19:04:02.091Z_

<details open><summary>🔧 Tool call — Read · `toolu_01JXfhqunbXn6dznsAF8t87K`</summary>

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
  "parentUuid": "1f9d3afd-3958-4dea-af66-3d9ae2ac4974",
  "isSidechain": false,
  "requestId": "req_011CbL29b1HsSypCs5N6vput",
  "type": "assistant",
  "uuid": "07a65167-e17b-4f18-ad8f-f842eef95c2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TQvnKR5HxZdDBYj1qNSp8a",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 84,
      "cache_read_input_tokens": 36490,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 84,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 89,
          "cache_read_input_tokens": 36490,
          "cache_creation_input_tokens": 84,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 84
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

_source line 19 · 2026-05-23T19:04:02.097Z_

<details><summary>↩ Tool result · `toolu_01JXfhqunbXn6dznsAF8t87K`</summary>

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
188	  # === P1+: Cross-benchmark generalizability ===
189	
190	  - id: plan_017
191	    name: sopbench_cross_benchmark
192	    claim: "C1 (generalizability), C2 (partial)"
193	    description: >
194	      Cross-benchmark C1 replication on SOPBench (Li et al., 2025).
195	      7 domains (Bank, DMV, Healthcare, Hotel, Library, University, Online Market)
196	      all different from τ²-bench (retail + airline).
197	      Select 2 domains (Healthcare + Bank) for maximum domain diversity.
198	      Construct 100 clause pairs (50/domain) covering 3-4 ambiguity types
199	      (incompleteness, auth_scope, lexical, conditional_precedence)
200	      from SOPBench's NL SOP constraints.
201	      Run 100 pairs × 2 conditions × 5 models = 1,000 episodes.
202	      SOPBench has rule-based verifier — no LLM judge needed.
203	      Key metrics: (a) Does C1 binary effect replicate? (b) Is incompleteness
204	      still highest-risk type? (c) Cross-benchmark effect size correlation.
205	      Addresses SF-8 (single benchmark external validity).
206	      Result goes in Appendix with 1-sentence summary in main text.
207	      [2026-05-22] Approved by user. Estimated 1 day including clause construction.
208	    priority: P1
209	    gpu_budget_hours: 0
210	    deps: []
211	    status: planned
212	
213	  # === P2: Nice to have ===
214	
215	  - id: plan_008
216	    name: classifier_poc
217	    claim: "practical contribution"
218	    description: >
219	      Binary ambiguity detector PoC: fine-tune DeBERTa-v3-large on
220	      annotated clause pairs (ambiguous/unambiguous labels). Eval on
221	      held-out set. Demonstrates practical applicability of findings.
222	      Phase 3 from IDEA_BRIEF, scoped to PoC for EMNLP.
223	    priority: P2
224	    gpu_budget_hours: 8
225	    deps: [plan_001]
226	    status: planned
227	
228	# Resource summary:
229	# P0 GPU: 0h (plan_003 pivoted to API — no GPU needed)
230	# P1 GPU: 15h (plan_006 reliability local portion — can also go API)
231	# P2 GPU: 8h (plan_008 classifier fine-tuning)
232	# Total GPU: 8-23h (P2 only essential; P1 optional if API covers it)
233	# API cost: ~$450-700 (1,800 plan_002 + 1,200 plan_003 via OpenRouter + 720 reliability + 180 perturbation + judge cal)
234	# Models (all API via OpenRouter proxy at 47.94.22.126/v1):
235	#   gpt-5.4, gpt-4.1 (OpenAI, no prefix needed)
236	#   anthropic/claude-sonnet-4-6 (Anthropic, prefix required)
237	#   qwen/qwen3-235b-a22b (Alibaba, open-source MoE, prefix required)
238	#   deepseek/deepseek-chat-v3-0324 (DeepSeek, open-source, prefix required)
239	# [2026-05-20] Pivoted from local GPU to all-API: OpenRouter supports all 5 models
240	# [2026-05-20] Benchmark: τ²-bench (Barres et al. 2025, arXiv:2506.07982)
241	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "07a65167-e17b-4f18-ad8f-f842eef95c2f",
  "isSidechain": false,
  "promptId": "729a2239-1e83-4796-a7ab-5d472e588b51",
  "type": "user",
  "uuid": "7871fbb7-af4b-4c37-a1b6-1ae3d66d2e1f",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/experiment_plan.yaml",
      "content": "# Experiment Plan — policy_ambiguity_safety\n# Post-MVP, targeting EMNLP 2026 (ARR Aug cycle)\n# Claims reference paper_framing.md\n\nexperiments:\n  # === P0: Must-run for paper ===\n\n  - id: plan_001\n    name: full_study_clause_generation\n    claim: \"C1, C2, C3\"\n    description: >\n      Generate remaining clauses for full study: coreferential (50 new),\n      authorization_scope (50 new), lexical (+20 to reach 50),\n      incompleteness (+20 to reach 50). Total 140 new clauses.\n      Validate all 300 clauses (50/type × 6 types) for completeness\n      and cross-type balance. Mix CP format per Reviewer suggestion\n      (labeled + unlabeled).\n    priority: P0\n    gpu_budget_hours: 0\n    deps: []\n    status: planned\n\n  - id: plan_001b\n    name: new_type_mini_pilot\n    claim: \"C1 (validation)\"\n    description: >\n      Mini-pilot for coreferential + authorization_scope (never tested):\n      5 clauses/type × 2 conditions × 1 model (gpt-5.4) = 20 episodes.\n      Verify: (a) ambiguous triggers violations (b) unambiguous control < 15%.\n      If systematic issues found, fix clause design before full study.\n      API cost negligible (~$2). Per Reviewer warning on untested types.\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [plan_001]\n    status: planned\n\n  - id: plan_002\n    name: full_study_api\n    claim: \"C1, C2, C3, C4, C5\"\n    description: >\n      Run 300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1,\n      claude-sonnet-4-6) = 1,800 episodes on τ²-bench. Cross-judge\n      evaluation. Output: episodes.jsonl + judgments.jsonl. No GPU needed.\n      Claude via OpenRouter proxy (base_url=http://47.94.22.126/v1).\n      [2026-05-20] Claude added per distill gap (4/8 papers use Claude baseline).\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [plan_001, plan_001b, plan_010]\n    status: planned\n\n  - id: plan_003\n    name: full_study_opensource\n    claim: \"C1, C2, C3, C4, C5\"\n    description: >\n      Run 300 clauses × 2 conditions × 2 open-source models via OpenRouter API:\n      qwen/qwen3-235b-a22b (235B MoE, Alibaba) + deepseek/deepseek-chat-v3-0324\n      (DeepSeek) = 1,200 episodes on τ²-bench. Cross-judge uses API models.\n      Can run in parallel with plan_002. No GPU needed.\n      [2026-05-20] Pivoted from local GPU → API: OpenRouter proxy confirmed\n      to support Qwen3 and DeepSeek models. Eliminates 48h GPU requirement.\n      Provider prefix required (e.g. qwen/qwen3-235b-a22b, not qwen3-235b-a22b).\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [plan_001]\n    status: planned\n\n  - id: plan_004\n    name: full_study_analysis\n    claim: \"C1, C2, C3, C4\"\n    description: >\n      Statistical analysis of full study data (3,000 episodes):\n      (a) Binary effect per type with bootstrap CI (C1)\n      (b) Omnibus χ² + pairwise across 6 types (C2)\n      (c) Visibility comparison: CP vs scopal rates (C3)\n      (d) Model × type interaction: 5×6 contingency + logistic regression (C4)\n      Report effect sizes + CI for all comparisons per Reviewer suggestion.\n      [Dream A3] Power analysis: report MDE for C2 (given N=250/type pooled)\n      and C3 (given N=250 per type). If V < 0.20 but MDE > observed V,\n      discuss underpowered possibility.\n      [Dream A4] TOST equivalence test with both ±15pp and ±10pp margins.\n      Justify margin choice explicitly.\n      [Dream A10] Report per-type information delta (token count difference\n      between ambiguous and unambiguous variants) as control variable.\n      [Dream B&K] Inter-model agreement on ambiguous clauses: do 5 models\n      adopt same or different interpretations? (supplementary analysis)\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [plan_002, plan_003]\n    status: planned\n\n  - id: plan_005\n    name: error_analysis\n    claim: \"C5\"\n    description: >\n      Qualitative analysis of agent traces from full study:\n      (a) Sample 50 violation traces per type (300 total)\n      (b) Classify failure modes (scope misapplication, conservative refusal,\n          assumption-based action, arbitrary rule selection, etc.)\n      (c) Cross-type failure mode distribution\n      (d) Visibility mechanism: compare CP traces (explicit conflict detection\n          behavior) vs scopal traces (surface scope adoption without awareness)\n      (e) Model-specific failure patterns (connect to C4)\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [plan_002, plan_003]\n    status: planned\n\n  # === P1: Important for robustness ===\n\n  - id: plan_006\n    name: reliability_test\n    claim: \"C1, C2\"\n    description: >\n      Test-retest reliability: select 30 representative clauses (5/type),\n      run 3 independent replicates × 2 conditions × 2 API models (gpt-5.4,\n      gpt-4.1) = 360 episodes. Local models added when plan_003 GPU available.\n      Compute ICC for per-clause violation rates. Addresses Reviewer warning\n      about ±8pp sampling noise (scopal 51.7% → 43.3% across MVP/diag).\n      Bootstrap CI width should be < 10pp for key comparisons.\n      [2026-05-20] API portion: 330/360 episodes complete (28/30 clauses),\n      judgments pending.\n    priority: P1\n    gpu_budget_hours: 15\n    deps: [plan_001]\n    status: planned\n\n  - id: plan_007\n    name: realism_validation\n    claim: \"C1 (methodological)\"\n    description: >\n      Validate synthetic ambiguity injection realism:\n      (a) Linguistic property comparison with DRIP-R natural ambiguities\n          (sentence length, parse depth, Flesch-Kincaid, TTR) + KS tests\n      (b) Optional: discriminator test if DRIP-R data accessible\n      Addresses RC4 (ecological validity).\n    priority: P1\n    gpu_budget_hours: 0\n    deps: [plan_001]\n    status: planned\n\n  - id: plan_009\n    name: judge_calibration\n    claim: \"C1 (methodological)\"\n    description: >\n      LLM-as-judge calibration per distilled research norm (5/8 papers):\n      (a) Sample 100 episodes stratified by type×model×condition\n      (b) Human expert labels (2 annotators, target κ ≥ 0.75)\n      (c) Compute judge precision/recall/F1 against human ground truth\n      (d) Per-severity-tier agreement rates\n      (e) Report in Method section as standard practice per AgentAuditor/DRIP-R\n      [Dream A7] Upgraded P1→P0: Dream best-tier reviewers identified this\n      as \"single most critical missing validation.\" Without it, entire\n      measurement chain from episode to violation label is unvalidated.\n      κ=0.91 measures LLM-LLM agreement, not accuracy.\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [plan_002]\n    status: planned\n\n  - id: plan_010\n    name: perturbation_control\n    claim: \"C1 (causal validity)\"\n    description: >\n      [Dream A9] Non-ambiguity perturbation control arm to distinguish\n      ambiguity-specific harm from general prompt brittleness.\n      Generate 30 clause pairs with non-ambiguity perturbations:\n      (a) 15 synonym substitution pairs (replace key terms with synonyms)\n      (b) 15 clause reordering pairs (reorder conditions without changing meaning)\n      Run 30 × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6) = 180 episodes.\n      Key metric: Δ_net = Δ_ambiguity - Δ_perturb (net ambiguity-specific effect).\n      [Reviewer升级] 必须在 plan_002/003 full study 之前完成——\n      如果 perturbation Δpp ≈ ambiguity Δpp，2,400 episodes 全部无效。\n      低成本验证（30 pairs + 120 episodes API）优先于高成本投入。\n      [判定标准 — 5 档]:\n      PASS: Δ_perturb < 5pp (CI含0), ratio < 0.15 → C1 因果 claim 最强形式\n      PASS+caveat: 5-10pp, ratio 0.15-0.30 → 报告 perturbation baseline, C1 写 net effect\n      CONDITIONAL: 10-15pp, ratio 0.30-0.45 → 需 Δ_net > 20pp 且显著才可发表\n      WARNING: 15-20pp, ratio 0.45-0.60 → C1 改为 \"additional violations beyond sensitivity\"\n      FAIL: > 20pp, ratio > 0.60 → 无法声称 ambiguity-specific, 需根本重新设计\n      [Power 注意]: N=120 对 10pp 差异 power ≈ 30%. 用 CI 宽度判定, 非 p-value.\n      若 CI 过宽(>15pp width), 追加 60 episodes 压窄至 <10pp width.\n      输出标准化 verdict 文件: perturbation_Δpp, ambiguity_Δpp, net_Δpp, CI, ratio, verdict.\n    priority: P0\n    gpu_budget_hours: 0\n    deps: [plan_001]\n    status: planned\n\n  # === P1+: Cross-benchmark generalizability ===\n\n  - id: plan_017\n    name: sopbench_cross_benchmark\n    claim: \"C1 (generalizability), C2 (partial)\"\n    description: >\n      Cross-benchmark C1 replication on SOPBench (Li et al., 2025).\n      7 domains (Bank, DMV, Healthcare, Hotel, Library, University, Online Market)\n      all different from τ²-bench (retail + airline).\n      Select 2 domains (Healthcare + Bank) for maximum domain diversity.\n      Construct 100 clause pairs (50/domain) covering 3-4 ambiguity types\n      (incompleteness, auth_scope, lexical, conditional_precedence)\n      from SOPBench's NL SOP constraints.\n      Run 100 pairs × 2 conditions × 5 models = 1,000 episodes.\n      SOPBench has rule-based verifier — no LLM judge needed.\n      Key metrics: (a) Does C1 binary effect replicate? (b) Is incompleteness\n      still highest-risk type? (c) Cross-benchmark effect size correlation.\n      Addresses SF-8 (single benchmark external validity).\n      Result goes in Appendix with 1-sentence summary in main text.\n      [2026-05-22] Approved by user. Estimated 1 day including clause construction.\n    priority: P1\n    gpu_budget_hours: 0\n    deps: []\n    status: planned\n\n  # === P2: Nice to have ===\n\n  - id: plan_008\n    name: classifier_poc\n    claim: \"practical contribution\"\n    description: >\n      Binary ambiguity detector PoC: fine-tune DeBERTa-v3-large on\n      annotated clause pairs (ambiguous/unambiguous labels). Eval on\n      held-out set. Demonstrates practical applicability of findings.\n      Phase 3 from IDEA_BRIEF, scoped to PoC for EMNLP.\n    priority: P2\n    gpu_budget_hours: 8\n    deps: [plan_001]\n    status: planned\n\n# Resource summary:\n# P0 GPU: 0h (plan_003 pivoted to API — no GPU needed)\n# P1 GPU: 15h (plan_006 reliability local portion — can also go API)\n# P2 GPU: 8h (plan_008 classifier fine-tuning)\n# Total GPU: 8-23h (P2 only essential; P1 optional if API covers it)\n# API cost: ~$450-700 (1,800 plan_002 + 1,200 plan_003 via OpenRouter + 720 reliability + 180 perturbation + judge cal)\n# Models (all API via OpenRouter proxy at 47.94.22.126/v1):\n#   gpt-5.4, gpt-4.1 (OpenAI, no prefix needed)\n#   anthropic/claude-sonnet-4-6 (Anthropic, prefix required)\n#   qwen/qwen3-235b-a22b (Alibaba, open-source MoE, prefix required)\n#   deepseek/deepseek-chat-v3-0324 (DeepSeek, open-source, prefix required)\n# [2026-05-20] Pivoted from local GPU to all-API: OpenRouter supports all 5 models\n# [2026-05-20] Benchmark: τ²-bench (Barres et al. 2025, arXiv:2506.07982)\n",
      "numLines": 241,
      "startLine": 1,
      "totalLines": 241
    }
  },
  "sourceToolAssistantUUID": "07a65167-e17b-4f18-ad8f-f842eef95c2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20 · 2026-05-23T19:04:02.162Z_

````json
{
  "parentUuid": "7871fbb7-af4b-4c37-a1b6-1ae3d66d2e1f",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**policy_ambiguity_safety**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"policy_ambiguity_safety\")` 或 `load_project_config(\"policy_ambiguity_safety\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## 用户自定义规则（必须遵守）\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.\n\n### 写作规则\n\n- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长\n- **[EMNLP 2026]** ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面\n- **[EMNLP 2026]** 一篇文章只能有一个limitations section，放在正文里面，appendix不能有 limitations section\n- **[EMNLP 2026]** abstract 不要超过 200 words\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **paper-writing-norms** — 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md`\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——按 narrative_intent + design_notes 设计，从 pattern 库选用技法，远程 SSH 执行输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成学术图表——概念图（架构/流程/framework）首选，探索性统计图也可。LLM 写 matplotlib 代码 + VLM Critic 闭环迭代。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/policy_ambiguity_safety/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "0b18de0e-b326-4e9c-8295-85f47e7841c2",
  "timestamp": "2026-05-23T19:04:02.162Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：κ re-annotation succeeds marginally (meets threshold but doesn't strongly validate LLM coding), SOPBench partially replicates — paper's quantitative core…",
  "leafUuid": "0b18de0e-b326-4e9c-8295-85f47e7841c2",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Human re-annotation of failure modes for differential nocuity validation",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43"
}
```

---

### Assistant

_source line 23 · 2026-05-23T19:09:26.608Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of all the planned experiments and the median tier definition. Let me now construct the detailed imagined experiment results for the median tier.

Let me review the median tier definition again:

**Median tier meaning**: κ re-annotation succeeds marginally (meets threshold but doesn't strongly validate LLM coding), SOPBench partially replicates — paper's quantitative core is strong but qualitative contribution needs softening

**Core assumptions**:
1. 0.35 ≤ κ_reannotation < 0.45 (fair), dominant failure modes match in 3-4/6 types with boundary-type disagreements (auth_scope/incompleteness)


2. SOPBench C1 replicates with a meaningful effect but slightly smaller than the original, or one model behaves unexpectedly
3. The type ranking shows weak correlation or only a subset of types can be reliably tested
4. At least one reviewer raises concerns about the stability of the within-judge agreement in C3, questioning whether it truly supports the layering claim
5. C4's model-by-type interaction is viewed as noteworthy but reviewers express skepticism about whether five models provide sufficient evidence for claims about differential safety training

**Key metric ranges**:
- kappa_reannotation: [0.35, 0.44]
- sopbench_c1_delta_pp

: [15, 25]
- sopbench_type_rank_rho: [0.3, 0.59]
- c5_human_llm_dominant_mode_agreement: [3, 4]
- expected_arr_score: [3.5, 3.99]
- expected_reviewer_confidence: [3.0, 3.5]

Now I need to generate synthetic data for every planned experiment. Looking at the experiment registry, I see several marked as planned but some have conflicting status indicators—plan_002 shows as done in the registry despite being listed as planned, and plan_003 has already spawned completed sub-experiments. Let me identify which experiments actually need synthetic data generated and work through them systematically. I'm realizing there's a mismatch between the experiment_plan.yaml which lists everything as "planned" and the registry which shows many experiments already completed. The user is asking for detailed data on each planned experiment from the experiment_plan file, so I need to generate imagined results for all of them, even though some have actual results in the registry. Let me reconsider what the user actually wants in the context of this Phase 1 dream scenario framework. user is asking me to imagine what results would look like in the MEDIAN tier. This is a hypothetical exercise - they want me to produce what the data WOULD look like if the median scenario played out. So I should produce imagined results for all experiments listed in the plan, treating them as if they haven't been run yet, and showing what median-tier outcomes would look like.

But wait - many experiments are already done with known results (plan_002, plan_004, plan_005, etc.). The median tier definition focuses on two key things that HAVEN'T happened yet:
1. κ re-annotation (the what_if experiment)
2. SOPBench cross-benchmark (plan_017, still running)

The other experiments already have actual results. For those, in the median tier, the actual results ARE the results (since they've already happened). The median tier's implications are mainly about how the NEW experiments (reannotation + SOPBench) come out.

Actually, re-reading the prompt more carefully: the user wants median-tier imagined results for ALL experiments in the plan. For already-completed experiments, I should present the actual results as they are, since the median scenario doesn't retroactively change what already happened. But for the pending experiments, I need to imagine plausible median-tier outcomes and provide detailed data across the board. Now I'm working through what data to generate for the median tier—using actual results from completed experiments as anchors and filling in plausible outcomes for the ones still pending, like SOPBench showing a moderate replication effect with weaker type correlations. I'll structure this as YAML with all experiments from the plan plus the kappa reannotation scenario.

Writing YAML output... Let me think through each experiment carefully.

### plan_001: full_study_clause_generation
This is a preparatory step - generating clauses. In the median tier, this succeeds but might have some quality issues with the new types (auth_scope, coreferential). The relevant metrics would be about clause quality.

### plan_001b: new_type_mini_pilot
Mini-pilot for untested types. In median tier, it works but reveals minor issues needing fix.

### plan_002: full_study_api
Already done. Use actual results. The binary effect is +34.0pp across models.

### plan_003: full_study_opensource
Already done (003a + 003b). Use actual results.

### plan_004: full_study_analysis
Already done. The main analysis results are already known.

### plan_005: error_analysis
Already done. Inter-coder agreement sits at κ=0.517 with 80% overall alignment.

### plan_006: reliability_test
Already done. ICC=0.919.

### plan_007: realism_validation
Not done. In median tier: synthetic clauses are mostly realistic but show some distinguishability (KS test borderline for 1-2 properties).

### plan_009: judge_calibration
Already done. Human-LLM κ=0.807.

### plan_010: perturbation_control
Already done. Δ_perturb=3.33pp, PASS.

### plan_017: sopbench_cross_benchmark
KEY MEDIAN EXPERIMENT. C1 replicates but smaller effect. Type ranking weakly correlated.

### plan_008: classifier_poc
Not done. In median tier: binary F1 decent (~0.80) but type-level F1 mediocre.

### kappa_reannotation_success
Now examining the reannotation success metrics... I'm realizing the median tier should show complete results across all experiments as if running them fresh under those assumptions, even for already-completed ones—the actual results are already compatible with median constraints, so I just need to frame them consistently within that narrative. Now I'm structuring the full YAML output with all the experiments laid out systematically.

Generating markdown table... Now I'm working through the median tier assumptions for SOPBench specifically—the effect size should be smaller than the binary benchmark's 34pp gain, with one model showing an anomaly and type ranking only weakly correlated around 0.43, leaving just a few types fully testable. Let me write out the detailed results with tables and reasoning. Now I'm mapping out which tables to include for each experiment—the omnibus test results for plan_004, failure mode distributions for plan_005, the ICC metrics for plan_006, judge accuracy breakdowns for plan_009, cross-benchmark comparisons for plan_017, and the confusion matrix with per-type agreement for the kappa reannotation. I'm realizing this YAML will be substantial, so I need to be methodical about structure. Looking at what's available, I see that many experiments have actual results in the registry while the experiment plan lists them all as planned, so I should use the real data where it exists and generate plausible imagined results for the ones that don't. Writing YAML output... Now I'm finalizing the YAML output with detailed experiment data. For plan_001, I'm documenting the clause generation with 300 clauses across 50 per type, including quality metrics like Flesch-Kincaid scores and token lengths, plus notes on revision rounds needed for the newer clause types. For plan_001b, I'm setting up the mini-pilot with 20 episodes split between ambiguous cases that trigger violations in both types and unambiguous control cases.

The full study results show consistent positive effects across all three experiment tracks: the API study with 1800 episodes shows a +34.0pp binary effect with per-model variation (Claude +25.7, GPT-4.1 +34.7, GPT-5.4 +38.3), the open-source study with 1200 usable episodes shows Qwen3 at +32.4 and DeepSeek at +39.0, and the analysis phase documents the statistical measures including the odds ratio and chi-square values.

The error analysis on 245 traces confirms five of six dominant modes are consistent with an inter-coder reliability of κ=0.517, while the reliability test shows strong ICC=0.919. For the realism validation, most synthetic examples read as realistic with sentence length and readability metrics passing the Kolmogorov-Smirnov tests, though parse depth shows borderline results with synthetic structures slightly shallower than natural text.

Now I'm checking the judge calibration metrics—human-LLM agreement is κ=0.807 with inter-annotator κ=0.762. But I'm noticing some confusion in the registry about plan numbering. The perturbation control results appear under plan_014 rather than plan_010, showing a delta of -0.67pp and passing the test, while plan_010 itself contains violation coding metrics with 614 violations and κ=0.517. Looking at the registry data more carefully, plan_010 contains error analysis metrics like inter-coder agreement and violation counts, which suggests it might be a different execution than the perturbation control described in the paper. The actual perturbation control result with delta_perturb of -0.67pp appears to be in plan_014 instead, so there's likely a mismatch between what the paper labels as plan_010 and what's actually stored in the registry.

Now I'm ready to construct the YAML output with comprehensive results, being careful with the formatting for tables and flow sequences. For the median tier results like plan_017 (SOPBench), I'll work with the delta improvement of 19.4pp and the ambiguity percentage of 28.6% to build out detailed per-model performance data. I'm adjusting the delta values to be more moderate and realistic for the median tier, keeping them all above 15pp but with DeepSeek showing a smaller effect that hints at the anomaly mentioned in the benchmark description. Now I'm looking at how the error types rank across the two benchmarks. SOPBench can only test a subset of the types that τ²-bench covers, and when I compare the rankings between them, I'm getting a weak correlation of 0.43. The type distributions differ notably—incompleteness dominates in both, but the gaps between the other types are much tighter in SOPBench than in τ²-bench. That correlation coefficient is too high now. Let me try a different ranking arrangement where lexical and auth_scope swap positions in the second benchmark to bring the Spearman correlation into that target range of 0.30 to 0.60.

With this adjusted ranking, I'm getting a correlation of 0.40, which fits well. Now I need to think through the kappa_reannotation dataset—100 traces that two human annotators labeled across five error categories, with an overall agreement of 0.39 indicating fair inter-rater reliability, though most error types showed stronger human agreement than the overall metric suggests.

Looking at where the disagreement concentrates: auth_scope and incompleteness are the two types where human and LLM coding patterns diverge most. For auth_scope specifically, the LLM consistently codes it as unauthorized_escalation at high rates (72-83%), but humans seem to split their judgments between unauthorized_escalation and assumption_based_action depending on how they interpret the boundary between those categories. The incompleteness type shows a similar pattern where humans tend toward structural_misparse while LLMs lean toward assumption_based_action, suggesting different interpretive frameworks for what constitutes each error. (scope_misapplication), coreferential (scope_misapplication/assumption_based_action - the boundary's fuzzy but one dominates). For auth_scope and incompleteness, the LLM and human coders diverge: auth_scope splits between unauthorized_escalation and assumption_based_action, while incompleteness hinges on whether "inventing missing information" gets coded as assumption_based_action, arbitrary_rule_selection, or unauthorized_escalation depending on how the coder frames the violation. I'm working through the disagreements more carefully now. For auth_scope, the LLM codes it as unauthorized_escalation while humans see it as assumption_based_action—they interpret boundary violations as agents assuming authority rather than actively escalating. For incompleteness, I need to flip the human dominant mode to arbitrary_rule_selection at 41% to create a genuine disagreement, since humans perceive the agent as inventing rules rather than just making assumptions.

Looking at the overall metrics: inter-annotator agreement sits at κ = 0.39, with 4 out of 6 error types showing matching dominant modes between LLM and human annotators. The two mismatches are auth_scope and incompleteness. Per-type human κ ranges from 0.22 to 0.58, showing variable consistency across categories. I'm trying to understand what κ_reannotation actually represents—it seems to relate to how humans re-annotate with an improved codebook. I'm looking at the dominant failure modes from the LLM coding to identify which ones align with the human annotations. Across the six failure type categories, I can see that four of them show matching dominant modes between human and LLM coders—scopal, lexical, CP, and coreferential—though I need to verify the exact percentages for the CP category since the data appears cut off. The boundary disagreements between LLM and human coders make sense—unauthorized_escalation versus assumption_based_action is really a question of framing, and the same goes for whether filling in missing information counts as an assumption or an arbitrary choice. This aligns with the median tier spec, so I'm ready to move forward with the YAML output. I need to pull the actual metrics from the registry and paper_framing to make sure everything is detailed and accurate. The narrative_guidance section should capture the overall strategy: C1 and C4 are the paper's backbone, C5 gets reframed from "validated taxonomy" to "convergent evidence with moderate agreement," and the abstract shifts from "type-diagnostic failure signatures" to "type-associated failure patterns." Writing YAML configuration... Writing YAML structure...

I'm noticing plan_012 already has classifier metrics in the registry, but plan_008 is listed as the classifier PoC in the experiment plan—they might be separate experiments or plan_012 could be a later iteration. For plan_008's median tier results, I'll generate reasonable performance numbers for a fine-tuned DeBERTa-v3-large classifier.

Now I need to reconcile the scoring: the median tier expects an ARR score between 3.5-3.99, which would put the paper at borderline conference acceptance, slightly below the dream scenario's median of 3.0. Let me write out the YAML with these constraints in mind.

I'm mapping out all 13 experiments to include in the output—starting with the clause generation work and mini-pilot, then the three full study variants with their actual results, followed by the analysis, error analysis, reliability metrics, realism tests, judge calibration, perturbation control, the key SOPBench replication, and finally the classifier results.

Now I need to structure the YAML output with expected results as a flat dictionary, rationales explaining why these results fit the median scenario, and optional tables or figures where they add clarity. I'm writing the complete specification now. Writing YAML output... The inter-coder reliability drops to κ=0.517 when expanding to five models across 614 traces, which weakens unanimous agreement on error types from 5/6 down to 3/6, though majority agreement holds at 6/6—this aligns with the median tier's expectation that broader model coverage reveals less consensus. Now I'm ready to structure the YAML output with the experiment metadata, plan IDs, and result summaries.

For each experiment I need to organize the name, plan ID, brief description, expected metrics, rationale for the median tier results, relevant data tables, figure descriptions, and interpretation. I'm planning to include consolidated per-model results for the early plans, the type hierarchy matrix from plan_004, the five-model failure distribution, ICC breakdowns by type, KS test comparisons, judge calibration details, and the SOPBench cross-benchmark analysis with type rankings—SOPBench gets extra detail since it's central to the median tier framing.

Writing YAML structure... dominant mode comparison

OK, writing now. Final version.

Actually, one important thing: for the narrative_guidance, the user already provided a median tier narrative. Let me tailor it slightly to reflect the specific imagined numbers.

Let me also consider: the median tier expects expected_arr_score [3.5, 3.99]. Given all the evidence, I'd pick 3.75 as the expected score. This is borderline conference - strong enough for Findings, competitive for poster, but not quite Main conference quality.

Expected reviewer confidence [3.0, 3.5] → 3.2

OK, writing the final YAML now. For real this time.

Let me also address what plan_007 (realism_validation) would look like in the median tier. This is about validating synthetic clause realism.

In the median tier, the synthetic clauses are mostly realistic but show 1-2 distinguishable features. Looking at the statistical tests across linguistic dimensions, I'm seeing a mixed picture: sentence length and Flesch-Kincaid show no significant difference, parse depth and lexical diversity are borderline significant with synthetic text showing slightly shallower structures and lower vocabulary diversity due to template constraints. Overall, two of the four tests are non-significant with one borderline and one trending, which aligns with the median tier expectation—the synthetic data isn't perfect but solid enough to support the approach.

For plan_008 (classifier PoC), the median tier performance shows a binary F1 of 0.81 distinguishing ambiguous from unambiguous cases with a false positive rate of 0.05, and a macro F1 of 0.64 across the six types. The core issue is that incompleteness cases blur the line between assumption-based action and arbitrary rule selection—coders struggle to distinguish whether the agent had contextual reasoning or just guessed. Looking at the per-type breakdown, four categories show reasonable agreement (scopal at 0.58, lexical at 0.52, CP at 0.48), but coreferential and auth_scope types have inherent boundary ambiguity that makes consistent coding difficult.

When I compare human and LLM agreement on the dominant failure modes, scopal, lexical, and CP all align on scope_misapplication, but coreferential shows a weak match—humans lean toward assumption_based_action while the LLM identifies scope_misapplication, which makes sense given that coreferential cases lack a clear dominant pattern anyway.

The auth_scope and incompleteness categories are genuine mismatches: humans see assumption_based_action and arbitrary_rule_selection respectively, while the LLM identifies unauthorized_escalation and assumption_based_action. Still, with four out of six categories showing agreement (treating coreferential as marginal), this lands squarely in the median tier. Now I'm compiling the final YAML output with the kappa statistics and agreement metrics.

For the expected results, I'm documenting the inter-annotator reliability at 0.39, the pooled human-LLM kappa at 0.31, and noting that the dominant mode agreement holds at 4 out of 6 categories, with per-type kappa values ranging from 0.22 to 0.58. The dataset spans 100 traces across 5 categories, with the collapsed four-category kappa at 0.44.

Now I'm finalizing the narrative framing for median-tier results: the core contributions rest on C1 and C4, while C5 shifts from claiming a validated taxonomy to presenting convergent evidence with moderate agreement. The abstract gets reframed around type-associated failure patterns rather than type-diagnostic signatures, and the human validation becomes explicitly preliminary. C3 gets subsumed under C4's model-by-type interaction, and SOPBench evidence is positioned as partial cross-domain support.

For the preparatory experiments, plan_001 produces 300 validated clauses and plan_001b is generating the clause-to-category mappings, so both have concrete outputs that feed into the main analysis pipeline. Writing validation YAML... I'm settling on the structure now—starting with the median tier and narrative guidance, then working through each of the 13 experiments with their full details including tables and figures where they matter most. I'll make sure the analysis sections are substantive enough to explain what the results mean for the paper and where the gaps are, noting which experiments are already done versus pending. Let me write out the comprehensive YAML output with all the required fields.

Writing YAML output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b18de0e-b326-4e9c-8295-85f47e7841c2",
  "isSidechain": false,
  "requestId": "req_011CbL2A662GT6PgTeL3APCb",
  "type": "assistant",
  "uuid": "6d5acb1f-88ba-4e51-b69a-f24227097cca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hy3nTBjgkrthQjMVgjzAB6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9817,
      "cache_read_input_tokens": 36574,
      "output_tokens": 32743,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9817,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 32743,
          "cache_read_input_tokens": 36574,
          "cache_creation_input_tokens": 9817,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9817
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

_source line 24 · 2026-05-23T19:15:01.062Z_

```yaml
tier: median
narrative_guidance: >
  C1（+34.0pp, 5 models, perturbation PASS）+ C4（model×type interaction, auth_scope 52pp range）承载论文核心贡献。
  C5 从 "validated taxonomy" 降级为 "convergent LLM-coded and human evidence with moderate agreement (κ=0.39)"；
  abstract 将 "type-diagnostic failure signatures" 替换为 "type-associated failure patterns"；
  Contribution (3) 保留 "supported by" 但追加 "preliminary human validation (κ=0.39)" 限定语。
  C3 layer effect 不再作为独立 finding，降为 C4 下属观察（"model×type interaction subsumes the aggregate layer gap"）。
  SOPBench 描述为 "partial cross-domain evidence (Δ=19.4pp, 4/5 models replicate)" 而非 "full replication"；
  DeepSeek 在 SOPBench 上 Δ=12.4pp 归因于 rule-based verifier 的 domain-specific 校准差异，不构成 fundamental non-replication。
  Rebuttal 策略：强调 κ=0.39 超过 chance 且与已知 category-boundary ambiguity（auth_scope/incompleteness）一致；
  4-type dominant mode 一致性覆盖了理论上最具区分性的类型（scopal, lexical, CP）。
  κ=0.39 比纯 automated coding（LLM-LLM κ=0.517）低，但 human inter-annotator 在 failure mode 编码上天然更分散；
  collapsed 4-category scheme κ=0.44 接近 moderate。
  竞争力：C1 causal design + C4 interaction 足够支撑 novel contribution；weakened C5 不致命但限制 main-track award potential。
  Expected ARR: 3.75（competitive for EMNLP Findings / borderline Main poster）。

imagined_experiments:
  # ============================================================
  # plan_001: Clause Generation (preparatory)
  # ============================================================
  - name: "full_study_clause_generation"
    plan_id: "plan_001"
    description: "生成并验证 300 条 clause pairs (50/type × 6 types)，含新类型 coreferential 和 authorization_scope 各 50 条新写，lexical/incompleteness 各补 20 条"
    expected_results:
      total_clauses: 300
      clauses_per_type: 50
      types_covered: 6
      revision_rounds_needed: 2
      avg_token_length_ambiguous: 31.2
      avg_token_length_unambiguous: 29.8
      avg_token_delta_spec_layer: 35.1
      avg_token_delta_ling_layer: 12.6
      cross_type_length_cv: 0.14
      cp_format_mix_labeled_pct: 0.60
      cp_format_mix_unlabeled_pct: 0.40
    result_rationale: >
      Median 档下 clause generation 本身不是瓶颈——这是研究者可控的准备步骤。300 条 clause 的生成和验证
      经过 2 轮修订完成。新类型（auth_scope, coreferential）的 clause 质量略低于已验证类型（scopal, CP），
      需要 1 轮额外修订确保 unambiguous 控制条件不引入新歧义。token delta 在 spec-layer（35.1 tokens）显著
      高于 ling-layer（12.6 tokens）反映了 specification ambiguity 需要更多文字消歧的本质差异——
      这个 delta 后续作为 confound control variable 进入 logistic regression。
      CP clause 按 Reviewer 建议混合 labeled (60%) 和 unlabeled (40%) 格式。
    tables: []
    figures_description: []
    analysis: >
      Clause generation 是全部下游实验的基础。关键质控：(a) cross-type token length CV=0.14 表明类型间长度
      相对均衡，不会因长度差异系统性偏置 violation rate；(b) spec-layer token delta 更大是预期的（
      auth_scope 需要明确 permission boundary，incompleteness 需要补充缺失条件），但需在 analysis 中
      作为 covariate 控制；(c) 新类型 clause 质量验证在 plan_001b pilot 中确认。

  # ============================================================
  # plan_001b: Mini-Pilot (new type validation)
  # ============================================================
  - name: "new_type_mini_pilot"
    plan_id: "plan_001b"
    description: "coreferential + authorization_scope 各 5 clauses × 2 conditions × 1 model (gpt-5.4) = 20 episodes 的 mini-pilot 验证"
    expected_results:
      total_episodes: 20
      auth_scope_amb_violation_rate: 0.60
      auth_scope_unamb_violation_rate: 0.10
      coreferential_amb_violation_rate: 0.30
      coreferential_unamb_violation_rate: 0.00
      auth_scope_delta_pp: 50.0
      coreferential_delta_pp: 30.0
      design_issues_found: 1
      clauses_requiring_revision: 2
    result_rationale: >
      Pilot 验证两个新类型的 clause 设计有效性。auth_scope 的 60% ambiguous violation rate 和 50pp delta
      符合预期——gpt-5.4 在 auth_scope 上是高 vulnerability 模型（full study 确认 64%）。
      coreferential 的 30% ambiguous rate 和 0% unambiguous control 均在可接受范围，但 violation rate
      是所有类型中最低的，与 full study 最终结果一致（coreferential 31.6% 为最低 tier）。
      发现 1 个 design issue：2 条 coreferential clause 的 unambiguous 版本仍含轻微 referential ambiguity，
      需修订。N=20 的 pilot 不具备统计 power，仅用于排除系统性失败。
    tables:
      - title: "Mini-Pilot Results"
        columns: ["Type", "Condition", "Violations", "Episodes", "Rate"]
        rows:
          - ["auth_scope", "ambiguous", "3", "5", "60%"]
          - ["auth_scope", "unambiguous", "0.5", "5", "10%"]
          - ["coreferential", "ambiguous", "1.5", "5", "30%"]
          - ["coreferential", "unambiguous", "0", "5", "0%"]
    figures_description: []
    analysis: >
      Pilot 确认新类型 clause 设计可行，两个类型都显示 ambiguous 条件下 violation rate 显著高于 control。
      auth_scope 效应强（Δ=50pp），coreferential 效应弱（Δ=30pp）但仍 meaningful。coreferential 的
      低 rate 与 disambiguation channel 假说一致——tool responses 提供部分消歧。2 条需修订的 clause
      在 full study 前修正。

  # ============================================================
  # plan_002: Full Study API (3 models)
  # ============================================================
  - name: "full_study_api"
    plan_id: "plan_002"
    description: "300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6) = 1,800 episodes，cross-judge evaluation"
    expected_results:
      total_episodes: 1800
      overall_amb_violation_rate: 0.380
      overall_unamb_violation_rate: 0.053
      overall_delta_pp: 32.7
      overall_or: 14.8
      overall_mcnemar_p: "<0.0001"
      gpt54_delta_pp: 38.3
      gpt41_delta_pp: 34.7
      claude_delta_pp: 25.7
      gpt54_amb_rate: 0.410
      gpt41_amb_rate: 0.407
      claude_amb_rate: 0.303
      cross_judge_fleiss_kappa: 0.717
      episodes_per_model: 600
    result_rationale: >
      3-model API 实验是论文数据采集的核心。结果与 median 档完全一致——C1 binary effect 极强
      （每个模型 Δpp 都 >25pp, 全部 p<10^-17），模型间已显示分化模式（Claude 最低 30.3%, GPT-5.4 最高 41.0%），
      为 C4 interaction 奠定基础。cross-judge Fleiss' κ=0.717 确认 judge 间一致性良好。
      Claude 的低 violation rate 主要由 auth_scope 驱动（12% vs GPT-5.4 64%），
      这一模式在 plan_003 开源模型数据中进一步丰富。
    tables:
      - title: "Per-Model Binary Effect (API Models)"
        columns: ["Model", "Amb Rate", "Unamb Rate", "Δpp", "OR", "p-value"]
        rows:
          - ["gpt-5.4", "41.0%", "2.7%", "+38.3", "25.2", "<10^-23"]
          - ["gpt-4.1", "40.7%", "6.0%", "+34.7", "10.8", "<10^-17"]
          - ["claude-sonnet-4-6", "30.3%", "4.7%", "+25.7", "8.9", "<10^-17"]
          - ["Pooled (API)", "37.3%", "4.4%", "+32.9", "14.8", "<10^-50"]
    figures_description:
      - "Forest plot: per-model binary effect size with 95% bootstrap CI, horizontal bars showing Δpp for each model"
    analysis: >
      API 模型数据确认 C1 binary effect 在 3 个 proprietary 模型上无例外成立。Claude 的低 overall rate
      源于 auth_scope 极低（12%），但 incompleteness（48%）与其他模型差距不大，支持 C4 的 "safety training
      differentially mitigates specific types" 论点。cross-judge κ=0.717 为 judge reliability 提供了
      independent evidence（与 plan_009 human calibration 互为补充）。

  # ============================================================
  # plan_003: Full Study Open-Source (2 models)
  # ============================================================
  - name: "full_study_opensource"
    plan_id: "plan_003"
    description: "300 clauses × 2 conditions × 2 open-source models (qwen3-235b, deepseek-v3) via OpenRouter API = 1,200 episodes"
    expected_results:
      total_episodes: 1197
      qwen3_amb_rate: 0.431
      qwen3_unamb_rate: 0.093
      qwen3_delta_pp: 32.4
      deepseek_amb_rate: 0.497
      deepseek_unamb_rate: 0.107
      deepseek_delta_pp: 39.0
      deepseek_per_type_chi2_p: 0.277
      qwen3_per_type_chi2_p: 0.007
    result_rationale: >
      开源模型扩展了 C4 interaction 的 evidence base。Qwen3 显示中等 vulnerability（43.1%）但有
      显著 type differentiation（χ²=15.89, p=0.007）——high incompleteness (62%) + lexical (52%)，
      low auth_scope (26%)。DeepSeek 是最 vulnerable 模型（49.7%），且几乎 uniformly high across all types
      （χ²=6.31, p=0.277, V=0.14 not significant），说明 less type-specific safety training。
      Qwen3 的 auth_scope (26%) 介于 Claude (12%) 和 GPT-5.4 (64%) 之间，增强了 auth_scope 作为
      "safety training canary type" 的论证。DeepSeek 的 uniform vulnerability 作为 C4 的 negative case
      （no differential mitigation）同样有理论价值。
    tables:
      - title: "Per-Model Binary Effect (Open-Source Models)"
        columns: ["Model", "Amb Rate", "Unamb Rate", "Δpp", "OR", "p-value"]
        rows:
          - ["qwen3-235b", "43.1%", "9.3%", "+32.4", "7.4", "<10^-18"]
          - ["deepseek-v3", "49.7%", "10.7%", "+39.0", "8.3", "<10^-20"]
      - title: "Per-Model Type Differentiation (Open-Source)"
        columns: ["Model", "χ²", "p-value", "V", "Type Differentiation"]
        rows:
          - ["qwen3-235b", "15.89", "0.007", "0.23", "Moderate — high incomp+lex, low auth_scope"]
          - ["deepseek-v3", "6.31", "0.277", "0.14", "NOT significant — uniformly high"]
    figures_description: []
    analysis: >
      开源模型数据完成 5-model 矩阵。关键发现：(a) C1 binary effect 在所有模型上 replicate，
      包括 architecture 截然不同的 MoE (Qwen3) 和 dense (DeepSeek)；(b) DeepSeek 的 uniform vulnerability
      (V=0.14, n.s.) 与 Claude 的 strong differentiation (V=0.24, p=0.003) 形成鲜明对比，
      支持 "safety training quality predicts type specificity" 论点；(c) 3 episodes 因 API 超时丢失
      (1,197/1,200)，对 power 影响可忽略。

  # ============================================================
  # plan_004: Full Study Analysis (统计分析)
  # ============================================================
  - name: "full_study_analysis"
    plan_id: "plan_004"
    description: "2,997 episodes 统计分析：C1 binary effect, C2 type hierarchy, C3 layer effect, C4 model×type interaction"
    expected_results:
      total_episodes: 2997
      c1_pooled_delta_pp: 34.0
      c1_or: 15.1
      c1_or_ci_lower: 10.78
      c1_or_ci_upper: 21.17
      c1_bootstrap_ci_lower: 31.2
      c1_bootstrap_ci_upper: 36.9
      c1_mcnemar_p: "<0.0001"
      c2_omnibus_chi2: 28.02
      c2_omnibus_p: 0.000036
      c2_cramers_v: 0.137
      c2_power: 0.993
      c2_mde: 0.093
      c2_tost_15pp_equivalent_pairs: "8/15"
      c2_tost_10pp_equivalent_pairs: "4/15"
      c3_spec_rate: 0.440
      c3_ling_rate: 0.379
      c3_delta_pp: 6.08
      c3_p: 0.017
      c3_v: 0.062
      c3_within_judge_gpt41_p: 0.059
      c3_within_judge_gpt54_p: 0.157
      c4_model_main_chi2: 31.02
      c4_model_main_p: 0.000003
      c4_model_main_v: 0.102
      c4_auth_scope_range_pp: 52
      c4_incompleteness_range_pp: 16
      c4_cp_range_pp: 6
      c4_fleiss_kappa: 0.384
      logistic_condition_amb_coef: 2.278
      logistic_condition_amb_z: 19.65
      logistic_token_delta_coef: 0.022
      logistic_token_delta_z: 3.49
      inter_model_agreement_on_amb_clauses: "39/300 universal, 85/300 majority, 92/300 model-specific, 84/300 safe"
    result_rationale: >
      Full study analysis 在 median 档下已经完成且结果确定。C1 极强（+34.0pp, OR=15.1）——这是论文最坚实的基础。
      C2 type hierarchy 显著（χ²=28.02, V=0.137）但 effect size 小（V<0.20），好在 power=0.993 且 MDE=0.093
      说明实验 well-powered，V=0.137 不是 underpowered artifact。3-tier 结构（high: incompleteness 53.6% >>
      mid: lexical-scopal-auth-CP 36.8-42.8% >> low: coreferential 31.6%）稳健。
      C3 layer effect 在 aggregate 层面显著（Δ=6.08pp, p=0.017）但 within-judge 分析 fragile
      （gpt-4.1 judged group p=0.059 marginal, gpt-5.4 judged group p=0.157 n.s.）——这是 median 档的
      核心弱点之一，reviewer 必然会 flag。C4 model×type interaction 是 star finding：auth_scope 52pp range
      揭示 safety training 的 type-specific 效果，而 incompleteness 16pp range 表明 universal blind spot。
      Fleiss κ=0.384 说明模型间仅 moderate agreement on which specific clauses trigger violations——
      binary effect universal 但 clause-level 行为 model-dependent。
    tables:
      - title: "C2: 3-Tier Type Hierarchy (Ambiguous Condition, Pooled 5 Models)"
        columns: ["Tier", "Type", "Violation Rate", "95% CI"]
        rows:
          - ["High", "incompleteness", "53.6%", "[48.6%, 58.6%]"]
          - ["Mid", "lexical", "42.8%", "[37.9%, 47.7%]"]
          - ["Mid", "auth_scope", "41.6%", "[36.7%, 46.5%]"]
          - ["Mid", "scopal", "39.4%", "[34.5%, 44.3%]"]
          - ["Mid", "cond_precedence", "36.8%", "[32.0%, 41.6%]"]
          - ["Low", "coreferential", "31.6%", "[27.0%, 36.2%]"]
      - title: "C4: Model × Type Interaction Matrix (Ambiguous Violation Rates)"
        columns: ["Type", "GPT-5.4", "GPT-4.1", "Claude", "Qwen3", "DeepSeek", "Range"]
        rows:
          - ["auth_scope", "64%", "46%", "12%", "26%", "60%", "52pp"]
          - ["incompleteness", "46%", "58%", "48%", "62%", "54%", "16pp"]
          - ["lexical", "42%", "34%", "32%", "52%", "54%", "22pp"]
          - ["scopal", "42%", "38%", "32%", "37%", "48%", "16pp"]
          - ["cond_prec", "34%", "36%", "36%", "40%", "38%", "6pp"]
          - ["coreferential", "18%", "32%", "22%", "42%", "44%", "26pp"]
      - title: "C3: Layer Effect — Aggregate vs Within-Judge"
        columns: ["Analysis", "Spec Rate", "Ling Rate", "Δpp", "p-value", "Note"]
        rows:
          - ["Pooled (5 models)", "44.0%", "37.9%", "+6.08", "0.017", "Significant"]
          - ["Within gpt-4.1 judge", "—", "—", "+8.0", "0.059", "Marginal"]
          - ["Within gpt-5.4 judge", "—", "—", "+4.8", "0.157", "Not significant"]
      - title: "TOST Equivalence Test Results"
        columns: ["Margin", "Equivalent Pairs", "Non-Equivalent Pairs", "Interpretation"]
        rows:
          - ["±15pp", "8/15", "7/15", "Types are partially but not fully interchangeable"]
          - ["±10pp", "4/15", "11/15", "Most type pairs are meaningfully different at ±10pp"]
      - title: "Logistic Regression (Violation ~ Condition + Model + Type + Token_Delta)"
        columns: ["Predictor", "Coefficient", "z", "p-value", "Interpretation"]
        rows:
          - ["condition_amb", "2.278", "19.65", "<0.001", "Ambiguity is dominant predictor"]
          - ["token_delta", "0.022", "3.49", "0.0005", "Info delta significant but small"]
          - ["model (reference=Claude)", "—", "—", "<0.001", "Model main effect significant"]
          - ["type (reference=coreferential)", "—", "—", "<0.001", "Type main effect significant"]
    figures_description:
      - "Figure 2: Forest plot — per-type × per-model binary effect sizes (Δpp) with 95% bootstrap CI, 30 data points arranged in 5-model × 6-type grid"
      - "Figure 3: Heatmap — 5×6 model×type violation rate matrix, color scale 12%-64%, with auth_scope column showing strongest cross-model gradient"
    analysis: >
      C1+C4 构成论文的 twin pillars。C1 的 causal evidence chain 极强（matched-pair + perturbation control +
      cross-model replication），即使最 skeptical 的 reviewer 也难以质疑。C4 的 model×type interaction 是
      genuine novelty——现有文献无人做过 5-model × 6-type 的 factorial 安全性分析。
      C3 的 within-judge fragility 是 median 档最大的 narrative vulnerability：至少一位 reviewer 会问
      "if the layer effect vanishes within a single judge's evaluations, isn't it just judge variance?"
      应对策略：C3 不作为 standalone finding，而是作为 C4 interaction 的 aggregate shadow（"the layer gap
      is itself model-dependent, driven by auth_scope, making the model×type interaction the more fundamental finding"）。
      V=0.137 在 power=0.993 下是 real but small——论文应用 "the 3-tier structure, not V, is the practical takeaway" 框架。

  # ============================================================
  # plan_005: Error Analysis (C5)
  # ============================================================
  - name: "error_analysis"
    plan_id: "plan_005"
    description: "5-model violation traces failure mode 编码：614 traces 分类为 5 类 failure modes，cross-model 一致性分析"
    expected_results:
      total_violations_coded: 614
      failure_mode_categories: 5
      types_unanimous_dominant_fm: "3/6"
      types_majority_dominant_fm: "6/6"
      inter_coder_kappa_llm: 0.517
      percent_agreement_llm: 0.656
      disambiguation_awareness_overall: 0.046
      surface_adoption_rate: 0.88
      escalate_to_user_rate: 0.008
      auth_scope_dominant_fm: "unauthorized_escalation"
      incompleteness_dominant_fm: "assumption_based_action"
      scopal_dominant_fm: "scope_misapplication"
      lexical_dominant_fm: "assumption_based_action"
      cp_dominant_fm: "scope_misapplication"
      coreferential_dominant_fm: "mixed (no clear dominant)"
      spec_layer_dominant_mechanism: "guess-and-act"
      ling_layer_dominant_mechanism: "misparse-and-apply"
      gwet_ac1_estimated: 0.72
    result_rationale: >
      5-model error analysis揭示 failure mode 的 type-specificity 在 5 models 下部分保持。
      unanimous dominant mode 仅 3/6（scopal, lexical, incompleteness），因为 auth_scope 和 CP 在不同模型间
      dominant mode 分裂——GPT 模型 auth_scope 以 unauthorized_escalation 为主，但开源模型更多表现为
      assumption_based_action（认为自己有权限而非明确 escalate）。coreferential 本身就无 dominant mode（flat distribution）。
      majority 仍 6/6 说明 type-specific signature 的大方向一致。
      inter_coder_kappa=0.517（moderate）受 kappa paradox 影响——lexical 91.7% agreement → κ=0.0。
      Gwet's AC1 估计 0.72 更准确反映 true agreement。
      Ambiguity Blindness (4.6% awareness) 是 C5 最 robust 的发现——不依赖 failure mode coding granularity。
      median 档下这些结果意味着 C5 的 fine-grained per-type percentages 需标注 "automated coding" caveat，
      但 type-mechanism dissociation（spec→guess vs ling→misparse）和 Ambiguity Blindness 仍可 claim。
    tables:
      - title: "5-Model Failure Mode Distribution by Type (Majority Dominant Mode)"
        columns: ["Type", "Dominant Mode", "Dominance %", "Unanimous Across 5 Models?"]
        rows:
          - ["auth_scope", "unauthorized_escalation", "68%", "No (3/5 models)"]
          - ["incompleteness", "assumption_based_action", "61%", "Yes (5/5 models)"]
          - ["scopal", "scope_misapplication", "72%", "Yes (5/5 models)"]
          - ["lexical", "assumption_based_action", "58%", "Yes (4/5 models)"]
          - ["cond_precedence", "scope_misapplication", "36%", "No (3/5 models)"]
          - ["coreferential", "mixed", "—", "No (no dominant)"]
      - title: "Ambiguity Blindness Metrics (5-Model Pooled)"
        columns: ["Metric", "Value", "Note"]
        rows:
          - ["Disambiguation awareness", "4.6%", "Agent explicitly notes ambiguity"]
          - ["Surface adoption", "88%", "Agent adopts first-parse interpretation"]
          - ["Escalate to user", "0.8%", "Agent asks for clarification"]
          - ["Conservative refusal", "3.2%", "Agent refuses to act on ambiguous clause"]
    figures_description:
      - "Figure 5: Stacked bar chart — per-type failure mode distribution across 5 models, showing type-specific signatures (auth_scope dominated by unauthorized_escalation blue, incompleteness by assumption_based_action orange)"
      - "Figure 6: Side-by-side comparison — 2-model (gpt-5.4 vs gpt-4.1, original plan_005) vs 5-model failure mode consistency, showing dilution from 5/6 to 3/6 unanimous"
    analysis: >
      Median 档下 C5 的核心叙事挑战：从 2-model 扩展到 5-model 后，unanimous dominant mode 从 5/6 下降到 3/6。
      这不是 C5 失败——majority 仍 6/6——但要求 framing 从 "type-diagnostic failure signatures" 调整为
      "type-associated failure patterns with cross-model consistency at majority but not unanimous level"。
      关键区分：(a) Ambiguity Blindness (4.6%) 完全不受此影响——这是 claim 最安全的发现；
      (b) spec→guess vs ling→misparse 的 layer mechanism 在 5 models 下仍成立；
      (c) auth_scope 的 failure mode heterogeneity 实际上 STRENGTHENS C4（"even the failure mechanism
      is model-dependent, not just the rate"）。
      κ=0.517 由 kappa paradox 严重 deflate；报告 Gwet's AC1≈0.72 + 80% raw agreement 作为 headline validity。

  # ============================================================
  # plan_006: Reliability Test (ICC)
  # ============================================================
  - name: "reliability_test"
    plan_id: "plan_006"
    description: "30 clauses × 3 replicates × 2 conditions × 2 models = 360 episodes test-retest reliability"
    expected_results:
      total_episodes: 360
      overall_icc: 0.919
      overall_icc_ci_lower: 0.892
      overall_icc_ci_upper: 0.940
      binary_icc: 0.847
      gpt54_icc: 0.921
      gpt41_icc: 0.918
      ling_layer_icc_range: "[0.976, 0.989]"
      spec_layer_icc_range: "[0.807, 0.857]"
      per_type_icc_scopal: 0.989
      per_type_icc_lexical: 0.981
      per_type_icc_coreferential: 0.976
      per_type_icc_auth_scope: 0.857
      per_type_icc_cond_prec: 0.856
      per_type_icc_incompleteness: 0.807
    result_rationale: >
      ICC=0.919（excellent）确认 API sampling noise 不是 confound。per-clause violation rates 在 3 次独立
      replicate 间高度可复现。关键发现：ling-layer ICC（0.976-0.989）系统性高于 spec-layer ICC（0.807-0.857），
      这 CONVERGES with C3/C5 的 disambiguation channel framework——linguistic ambiguity 行为更确定（agents
      consistently misparse the same way），specification ambiguity 行为更 stochastic（agents guess differently
      each run because no external disambiguation channel）。
      Incompleteness ICC=0.807 是最低的，因为缺失信息时 agent 的 guess 具有更高随机性。
      这在 median 档下是 strength——ICC 支持 C3/C5 且不依赖 human validation。
    tables:
      - title: "Per-Type ICC (Test-Retest Reliability)"
        columns: ["Type", "Layer", "ICC", "Interpretation"]
        rows:
          - ["scopal", "Linguistic", "0.989", "Excellent"]
          - ["lexical", "Linguistic", "0.981", "Excellent"]
          - ["coreferential", "Linguistic", "0.976", "Excellent"]
          - ["auth_scope", "Specification", "0.857", "Good"]
          - ["cond_precedence", "Specification", "0.856", "Good"]
          - ["incompleteness", "Specification", "0.807", "Good"]
    figures_description: []
    analysis: >
      ICC 结果是 paper 最干净的 methodological evidence 之一。per-type ICC 的 layer pattern
      （all ling > all spec）提供了 independent convergent evidence for the disambiguation channel framework，
      完全不依赖 LLM-as-judge 或 human annotation。在 median 档下，这个 evidence line 的价值更大——
      因为 κ_reannotation 仅 fair (0.39)，ICC 成为 C5 framework 的 alternative evidence pillar。
      Reviewer 可能问 "local models not tested"——answer：API models 代表 5/5 tested models 的
      test-retest subset，local model ICC 可在 camera-ready 补充。

  # ============================================================
  # plan_007: Realism Validation
  # ============================================================
  - name: "realism_validation"
    plan_id: "plan_007"
    description: "合成 clause 与 DRIP-R 自然歧义的 linguistic property 比较：sentence length, parse depth, Flesch-Kincaid, TTR"
    expected_results:
      n_synthetic: 300
      n_drip_r_natural: 187
      ks_sentence_length_p: 0.23
      ks_parse_depth_p: 0.041
      ks_flesch_kincaid_p: 0.18
      ks_ttr_p: 0.09
      ks_tests_significant_at_005: 1
      ks_tests_borderline: 1
      mean_sentence_length_synthetic: 28.4
      mean_sentence_length_natural: 31.7
      mean_parse_depth_synthetic: 4.2
      mean_parse_depth_natural: 5.1
      discriminator_test_completed: false
    result_rationale: >
      Median 档下 realism validation 大部分通过但不完美。4 项 KS test 中 1 项显著（parse depth p=0.041）、
      1 项 borderline（TTR p=0.09）、2 项通过。Parse depth 差异的原因：synthetic clauses 为了 matched-pair
      设计的可控性，避免了 DRIP-R 中常见的深层嵌套结构（relative clauses within relative clauses）。
      TTR borderline 因为模板化生成导致 lexical diversity 略低。
      这些差异不影响 C1 validity——perturbation control (plan_010) 已证明 surface-level 变化不引起 violation，
      且 synthetic clause 的 slightly lower parse depth 如果有 bias 应该是 conservative（simpler clauses
      → lower baseline difficulty → if anything underestimate ambiguity effect）。
      Discriminator test 未完成因 DRIP-R 数据访问限制（authors 未 release full dataset）。
    tables:
      - title: "Linguistic Property KS Test Results"
        columns: ["Property", "Synthetic Mean", "DRIP-R Mean", "KS Statistic", "p-value", "Result"]
        rows:
          - ["Sentence length (tokens)", "28.4", "31.7", "0.124", "0.23", "Pass"]
          - ["Parse depth", "4.2", "5.1", "0.168", "0.041", "Fail (borderline)"]
          - ["Flesch-Kincaid grade", "10.2", "10.8", "0.109", "0.18", "Pass"]
          - ["Type-token ratio", "0.82", "0.86", "0.141", "0.09", "Borderline"]
    figures_description: []
    analysis: >
      Realism validation 的 1/4 KS failure 不构成 fatal issue 但需在 Limitations 中 disclose。
      Framing 策略：(a) parse depth 差异 is conservative bias（simpler clauses → underestimate effect）；
      (b) perturbation control 已独立验证 surface-level 变化 ≈ 0 effect；(c) matched-pair 设计的 strength
      不依赖 absolute realism 而依赖 within-pair contrast（same clause ± ambiguity）。
      Reviewer RC4 的 ecological validity 担忧由三重 evidence 共同回应：realism validation (3/4 pass) +
      perturbation control (Δ=3.33pp) + matched-pair causal design。

  # ============================================================
  # plan_009: Judge Calibration (Human Validation)
  # ============================================================
  - name: "judge_calibration"
    plan_id: "plan_009"
    description: "100 episodes stratified sample × 2 human annotators × LLM judge comparison"
    expected_results:
      n_episodes: 100
      human_inter_annotator_kappa_binary: 0.798
      human_inter_annotator_kappa_weighted: 0.762
      human_llm_pooled_kappa_weighted: 0.807
      annotator1_llm_kappa_binary: 0.775
      annotator1_llm_kappa_weighted: 0.868
      annotator2_llm_kappa_binary: 0.692
      annotator2_llm_kappa_weighted: 0.745
      cross_judge_kappa_weighted: 0.685
      cross_judge_exact_agreement: 0.76
      cross_judge_binary_kappa: 0.74
      llm_precision_violation: 0.91
      llm_recall_violation: 0.87
      llm_f1_violation: 0.89
    result_rationale: >
      Judge calibration 结果强（human-LLM κ=0.807 weighted），超过大多数 agent safety 文献的 validation
      standard。human inter-annotator κ=0.762 设定了 human ceiling——LLM judge 的 agreement 实际上
      EXCEEDS human-human agreement（0.807 > 0.762），说明 LLM judge 趋向两位 annotator 的 consensus 中间。
      Precision 0.91 / Recall 0.87 说明 LLM judge slightly conservative（misses some violations but
      rarely calls false violations）——这个 direction 对 C1 是 conservative bias（如果有 bias，
      true effect > reported effect）。
      cross-judge exact agreement 0.76 和 binary κ=0.74 说明两个 LLM judge（gpt-5.4, gpt-4.1）之间
      high agreement，被 plan_009 supplementary 的 Fleiss κ=0.717 进一步确认。
    tables:
      - title: "Judge Calibration Metrics"
        columns: ["Comparison", "κ (binary)", "κ (weighted)", "Agreement"]
        rows:
          - ["Human1 vs Human2", "0.798", "0.762", "—"]
          - ["Human1 vs LLM", "0.775", "0.868", "—"]
          - ["Human2 vs LLM", "0.692", "0.745", "—"]
          - ["Human-LLM pooled", "—", "0.807", "—"]
          - ["Cross-judge (gpt-5.4 vs gpt-4.1)", "0.74", "0.685", "76%"]
      - title: "LLM Judge Performance (vs Human Ground Truth)"
        columns: ["Metric", "Value", "Note"]
        rows:
          - ["Precision (violation)", "0.91", "Low false positive rate"]
          - ["Recall (violation)", "0.87", "Misses ~13% violations (conservative)"]
          - ["F1 (violation)", "0.89", "Strong overall"]
          - ["False positive rate", "0.044", "Very low"]
    figures_description: []
    analysis: >
      Judge calibration 是 paper 的 methodological backbone——没有它 entire measurement chain unvalidated。
      κ=0.807 大幅超过 DRIP-R (κ≈0.6) 和 AgentAuditor (κ≈0.7) 的 reported validation。
      关键细节：Annotator 2 vs LLM agreement 较低（κ=0.692），但 Annotator 2 vs Annotator 1 也较低，
      说明差异来源是 Annotator 2 的个人 coding style 而非 LLM judge 偏差。
      在 median 档下这个 result 是纯正面的——judge calibration 不是 bottleneck。

  # ============================================================
  # plan_010: Perturbation Control
  # ============================================================
  - name: "perturbation_control"
    plan_id: "plan_010"
    description: "30 non-ambiguity perturbation pairs (synonym + reordering) × 2 conditions × 2+ models，区分 ambiguity-specific effect vs general prompt brittleness"
    expected_results:
      total_episodes_original: 120
      total_episodes_expanded: 300
      delta_perturb_pp_original: 3.33
      delta_perturb_pp_expanded: -0.67
      ci_95_original: "[-5.0, 13.33]"
      ci_95_expanded: "[-8.0, 6.67]"
      ci_contains_zero: true
      ambiguity_delta_pp: 34.0
      net_delta_pp: 34.67
      ratio_perturb_to_ambiguity: 0.088
      verdict: "PASS"
      mcnemar_p: 1.0
    result_rationale: >
      Perturbation control 是 C1 causal claim 的关键支柱。原始 120 episodes 显示 Δ_perturb=3.33pp，
      扩展至 300 episodes 后 Δ=-0.67pp（CI 收窄至 [-8.0, 6.67]，CI 上界从 13.33 降至 6.67）。
      Non-ambiguity surface perturbations（synonym substitution, clause reordering）对 violation rate
      影响为零。ratio=0.088 远低于 0.15 threshold → PASS verdict → C1 可用最强形式（"ambiguity-specific causation"
      而非 "additional violations beyond baseline sensitivity"）。
      这在 median 档下是 pure strength——即使 C5 weakened、SOPBench partially replicated，C1 的 causal
      evidence 无可质疑。
    tables:
      - title: "Perturbation Control Verdict"
        columns: ["Metric", "Original (N=120)", "Expanded (N=300)", "Threshold"]
        rows:
          - ["Δ_perturb (pp)", "3.33", "-0.67", "<5pp for PASS"]
          - ["95% CI", "[-5.0, 13.33]", "[-8.0, 6.67]", "CI contains 0"]
          - ["CI upper bound", "13.33", "6.67", "<10pp preferred"]
          - ["Ratio (perturb/ambiguity)", "0.088", "0.020", "<0.15 for PASS"]
          - ["Verdict", "PASS", "PASS", "—"]
    figures_description: []
    analysis: >
      Perturbation control 结果使本文的 causal claim 达到 agent safety 文献的最高标准。
      与 DRIP-R（no perturbation control）、PhantomPolicy（no causal design）、AgentPex（no matched pairs）
      相比，本文是唯一同时提供 matched-pair + perturbation control + cross-model replication 的研究。
      expanded N=300 将 CI upper bound 从 13.33 压至 6.67pp——即使取 CI 上界，perturbation effect
      也只有 ambiguity effect 的 1/5。这是 rebuttal 中 RC11 (prompt sensitivity) 的 definitive answer。

  # ============================================================
  # plan_017: SOPBench Cross-Benchmark (KEY MEDIAN EXPERIMENT)
  # ============================================================
  - name: "sopbench_cross_benchmark"
    plan_id: "plan_017"
    description: "SOPBench (Healthcare + Bank) 100 clause pairs × 2 conditions × 5 models = 1,000 episodes cross-benchmark C1 replication"
    expected_results:
      total_episodes: 982
      episodes_lost_to_api_error: 18
      domains_tested: 2
      types_testable: 4
      types_tested: ["incompleteness", "auth_scope", "lexical", "conditional_precedence"]
      types_not_testable: ["coreferential", "scopal"]
      overall_amb_rate: 0.286
      overall_unamb_rate: 0.092
      overall_delta_pp: 19.4
      overall_or: 4.02
      overall_mcnemar_p: 0.000001
      c1_replicates: true
      per_model_gpt54_delta_pp: 25.0
      per_model_gpt41_delta_pp: 22.4
      per_model_claude_delta_pp: 17.2
      per_model_qwen3_delta_pp: 20.0
      per_model_deepseek_delta_pp: 12.4
      per_model_deepseek_mcnemar_p: 0.087
      models_replicating_at_p005: 4
      models_anomalous: 1
      type_rank_incompleteness_sopbench: 1
      type_rank_auth_scope_sopbench: 2
      type_rank_cp_sopbench: 3
      type_rank_lexical_sopbench: 4
      spearman_rho_type_ranking: 0.40
      spearman_rho_p: 0.60
      cross_benchmark_effect_size_ratio: 0.57
      healthcare_delta_pp: 21.8
      bank_delta_pp: 17.0
      verifier_type: "rule-based (no LLM judge)"
    result_rationale: >
      Median 档下 SOPBench 部分复制 C1 但 effect size 显著缩小。Δ=19.4pp（vs τ²-bench 34.0pp）的缩小
      有多重解释：(a) SOPBench 的 rule-based verifier 比 LLM judge 更严格（标准不同导致 baseline 和 effect 不同）；
      (b) Healthcare/Bank 政策比 retail/airline 更结构化（ambiguity 的 operational impact 不同）；
      (c) clause construction 在非原生 benchmark 上质量略低（100 pairs 新写 vs 300 pairs 经 pilot 验证）。
      DeepSeek 是唯一 anomaly（Δ=12.4pp, p=0.087 marginal）——可能因为 DeepSeek 在 Healthcare domain
      的 baseline violation rate 已经很高（unamb=18%），导致 ceiling effect 压缩了 delta。
      Type ranking ρ=0.40 弱相关的原因：incompleteness 仍是 #1（cross-benchmark stable），但 lexical 在
      SOPBench 上降至 #4（DRIP-R style 的 lexical ambiguity 在 Banking 政策中不常见，构造的 clause 不够自然）。
      auth_scope 升至 #2（Banking 中 authorization boundary 更 salient）。
      coreferential 和 scopal 不可测试因为 SOPBench 的 NL SOP constraints 极少含这两类歧义。
    tables:
      - title: "SOPBench Per-Model C1 Replication"
        columns: ["Model", "Amb Rate", "Unamb Rate", "Δpp", "OR", "p-value", "Replicates?"]
        rows:
          - ["GPT-5.4", "34.0%", "9.0%", "+25.0", "5.21", "<0.001", "Yes"]
          - ["GPT-4.1", "31.4%", "9.0%", "+22.4", "4.63", "<0.001", "Yes"]
          - ["Claude", "24.2%", "7.0%", "+17.2", "4.24", "0.002", "Yes"]
          - ["Qwen3", "29.0%", "9.0%", "+20.0", "4.12", "<0.001", "Yes"]
          - ["DeepSeek", "28.4%", "16.0%", "+12.4", "2.08", "0.087", "Marginal"]
          - ["Pooled", "28.6%", "9.2%", "+19.4", "4.02", "<10^-6", "Yes"]
      - title: "SOPBench Per-Type Violation Rates (Ambiguous Only, Pooled Models)"
        columns: ["Type", "SOPBench Rate", "τ²-bench Rate", "SOPBench Rank", "τ²-bench Rank"]
        rows:
          - ["incompleteness", "34.2%", "53.6%", "#1", "#1"]
          - ["auth_scope", "28.4%", "41.6%", "#2", "#3"]
          - ["cond_precedence", "27.0%", "36.8%", "#3", "#5"]
          - ["lexical", "25.6%", "42.8%", "#4", "#2"]
      - title: "Cross-Benchmark Comparison"
        columns: ["Metric", "τ²-bench", "SOPBench", "Note"]
        rows:
          - ["C1 Δpp (pooled)", "+34.0", "+19.4", "SOPBench smaller (0.57×)"]
          - ["C1 OR", "15.1", "4.02", "SOPBench smaller"]
          - ["Models replicating (p<0.05)", "5/5", "4/5", "DeepSeek marginal on SOPBench"]
          - ["Type rank ρ (vs τ²-bench)", "—", "0.40", "Weak correlation (4 types)"]
          - ["Incompleteness #1?", "Yes", "Yes", "Stable across benchmarks"]
          - ["Verifier type", "LLM judge", "Rule-based", "SOPBench eliminates judge confound"]
          - ["Domains", "Retail + Airline", "Healthcare + Bank", "No overlap"]
    figures_description:
      - "Appendix figure: paired bar chart — τ²-bench vs SOPBench per-type violation rates (4 types), with incompleteness leading in both benchmarks but absolute rates lower in SOPBench"
    analysis: >
      SOPBench 结果在 median 档下是 double-edged。正面：(a) C1 binary effect 在 4/5 models 和 2 new domains
      上 replicate，排除了 τ²-bench-specific artifact；(b) incompleteness universally #1 across benchmarks，
      strengthens "safety training blind spot" claim；(c) rule-based verifier 消除了 LLM-as-judge confound。
      负面：(a) effect size 缩小 43%（19.4 vs 34.0pp）——reviewer 会问 "is 19.4pp still 'massive'?"
      （answer：yes，still OR=4.02）；(b) DeepSeek anomaly 需解释；(c) type ranking ρ=0.40 说明
      type hierarchy 是 domain-dependent（lexical ambiguity 的 impact 在 banking 中不同于 retail）。
      Paper framing 应为 "C1 binary effect replicates across 4 domains with rule-based verification;
      type hierarchy shows stable extremes (incompleteness highest) but domain-dependent mid-tier ordering."
      SOPBench 放 Appendix 并在 main text §5.1 用 1 句话总结。
      对 expected_arr_score 的影响：partial replication 比 no replication 好很多（+0.25），但比 full replication
      少贡献约 0.15。Net contribution to ARR score: ≈ +0.10。

  # ============================================================
  # plan_008: Classifier PoC
  # ============================================================
  - name: "classifier_poc"
    plan_id: "plan_008"
    description: "DeBERTa-v3-large fine-tuned binary ambiguity detector + 6-type classifier on 300 clause pairs"
    expected_results:
      binary_f1: 0.805
      binary_precision: 0.83
      binary_recall: 0.78
      binary_fpr: 0.044
      macro_f1_6type: 0.632
      best_type_f1_cp: 0.94
      worst_type_f1_incompleteness: 0.34
      per_type_f1_auth_scope: 0.58
      per_type_f1_coreferential: 0.70
      per_type_f1_lexical: 0.39
      per_type_f1_scopal: 0.75
      n_clauses: 500
      folds: 5
      gpu_hours: 6.2
    result_rationale: >
      Classifier PoC 在 median 档下表现合理但不 exceptional。Binary F1=0.805 表明 ambiguity detection
      是 feasible task，但 6-type classification macro F1=0.632 说明 fine-grained type 区分困难。
      CP F1=0.94 最高因其有 explicit rule conflict 的 distinctive syntactic pattern；
      incompleteness F1=0.34 最低因 "missing information" 在 surface form 上难以与正常 detailed clauses 区分
      （信息缺失是 semantic/pragmatic 特征而非 syntactic）。
      scopal (0.75) 和 coreferential (0.70) 较高因为有 distinctive syntactic markers（scope operators, pronouns）。
      auth_scope (0.58) 和 lexical (0.39) 中等偏低。
      在 median 档下 classifier 不作为独立 contribution，放在 Appendix 作为 "PoC demonstrating practical
      applicability" + 连接 Chantree et al. (2006) nocuous ambiguity detection 的 lineage。
    tables:
      - title: "DeBERTa-v3-large Classifier Performance (5-Fold CV)"
        columns: ["Type", "Precision", "Recall", "F1", "Support"]
        rows:
          - ["Binary (amb/unamb)", "0.83", "0.78", "0.805", "500"]
          - ["cond_precedence", "0.96", "0.92", "0.94", "100"]
          - ["scopal", "0.78", "0.72", "0.75", "100"]
          - ["coreferential", "0.74", "0.66", "0.70", "100"]
          - ["auth_scope", "0.62", "0.54", "0.58", "100"]
          - ["lexical", "0.42", "0.36", "0.39", "100"]
          - ["incompleteness", "0.38", "0.30", "0.34", "100"]
          - ["Macro avg (6-type)", "0.65", "0.58", "0.632", "600"]
    figures_description: []
    analysis: >
      Classifier PoC 在 EMNLP 审稿中的价值有限但不为零。Binary detection F1=0.805 说明
      automated ambiguity triage 可行；FPR=0.044 意味着 low false alarm rate（practical deployment
      中重要）。但 F1 不够高（<0.90）无法 claim "reliable automated detector"——只能说 "demonstrates feasibility"。
      6-type classification 的 uneven performance 反映了 ambiguity 类型在 surface form 上的区分度差异。
      这个不均匀性与 C2 type hierarchy 有 interesting parallel：surface-distinctive types (CP, scopal)
      easier to detect AND less dangerous (lower violation rates)，而 surface-invisible types (incompleteness)
      harder to detect AND most dangerous。implication：最危险的 ambiguity type 恰好最难自动检测——
      值得在 Discussion 中一句话提及。

  # ============================================================
  # kappa_reannotation (what_if — KEY MEDIAN EXPERIMENT)
  # ============================================================
  - name: "kappa_reannotation_success"
    plan_id: "what_if"
    description: "100 violation traces human re-annotation with improved 5-category codebook, 2 annotators, targeting failure mode validation"
    expected_results:
      n_traces: 100
      n_annotators: 2
      n_categories: 5
      kappa_human_inter_annotator: 0.39
      kappa_human_inter_annotator_ci_lower: 0.26
      kappa_human_inter_annotator_ci_upper: 0.52
      kappa_collapsed_4cat: 0.44
      kappa_collapsed_3cat: 0.51
      human_llm_dominant_mode_agreement: "4/6"
      per_type_kappa_scopal: 0.58
      per_type_kappa_lexical: 0.52
      per_type_kappa_cp: 0.48
      per_type_kappa_coreferential: 0.35
      per_type_kappa_auth_scope: 0.28
      per_type_kappa_incompleteness: 0.22
      percent_agreement_overall: 0.54
      types_human_llm_match: ["scopal", "lexical", "cond_precedence", "coreferential"]
      types_human_llm_mismatch: ["auth_scope", "incompleteness"]
      auth_scope_human_dominant: "assumption_based_action (42%)"
      auth_scope_llm_dominant: "unauthorized_escalation (78%)"
      incompleteness_human_dominant: "arbitrary_rule_selection (40%)"
      incompleteness_llm_dominant: "assumption_based_action (64%)"
      ambiguity_blindness_human_confirmed: true
      ambiguity_blindness_human_awareness_rate: 0.05
    result_rationale: >
      κ=0.39（fair）在 median 档下 marginal success——达到 0.35 threshold 但远未达到 substantial (0.60+)。
      这个结果反映了 failure mode coding 的 inherent difficulty：5-category scheme 在 category boundary
      上有系统性歧义。具体表现：
      (1) auth_scope 类型中，人类标注者对 "agent 超越授权边界" 的编码分歧——一部分标注者将其编码为
      unauthorized_escalation（"agent 知道边界但选择跨越"），另一部分编码为 assumption_based_action
      （"agent 不知道边界在哪里所以猜测"）。这个分歧反映了 agent 意图归因的固有困难——从 trace 中
      无法确定 agent 是 "知道但 escalate" 还是 "不知道而 assume"。LLM coder 倾向前者，人类 coder 倾向后者。
      (2) incompleteness 类型中，人类标注者将 "填充缺失信息" 更多编码为 arbitrary_rule_selection
      （"agent 凭空编造规则"）而非 assumption_based_action（"agent 基于上下文假设"），因为人类
      更容易看出 agent 的 "assumption" 实际上缺乏 contextual basis。
      (3) scopal, lexical, CP 的 dominant mode 一致性高（κ=0.48-0.58），因为这些类型的 failure mechanism
      更 surface-visible——scope_misapplication 和 assumption_based_action 在 trace 中有明确的行为标记。
      (4) coreferential 的 κ=0.35 反映了该类型本身 failure mode 分散（no dominant mode），
      human 和 LLM 都 "agree to disagree"。
      Collapsed scheme（4-cat, 合并 unauthorized_escalation + assumption_based_action → "boundary_exceeding"）
      提升 κ 至 0.44；3-cat 进一步合并至 0.51。这支持了 "fine-grained coding unreliable, coarse-grained valid" 的叙事。
      Ambiguity Blindness 在 human annotation 中确认（awareness rate ≈ 5%），这是最 robust 的 C5 发现。
    tables:
      - title: "Human Re-Annotation: Per-Type Inter-Annotator κ"
        columns: ["Type", "κ (5-cat)", "κ (4-cat)", "Agreement %", "Human-LLM Dominant Mode Match?"]
        rows:
          - ["scopal", "0.58", "0.63", "68%", "Yes (scope_misapplication)"]
          - ["lexical", "0.52", "0.57", "62%", "Yes (assumption_based_action)"]
          - ["cond_precedence", "0.48", "0.54", "58%", "Yes (scope_misapplication)"]
          - ["coreferential", "0.35", "0.40", "48%", "Yes (marginal — both mixed)"]
          - ["auth_scope", "0.28", "0.52", "42%", "No (Human: assumption, LLM: escalation)"]
          - ["incompleteness", "0.22", "0.30", "38%", "No (Human: arbitrary, LLM: assumption)"]
          - ["Overall", "0.39", "0.44", "54%", "4/6 match"]
      - title: "Failure Mode Dominant Distribution: Human vs LLM (auth_scope)"
        columns: ["Failure Mode", "Human Annotator %", "LLM Coder %", "Δ"]
        rows:
          - ["unauthorized_escalation", "32%", "78%", "-46pp"]
          - ["assumption_based_action", "42%", "12%", "+30pp"]
          - ["scope_misapplication", "8%", "4%", "+4pp"]
          - ["arbitrary_rule_selection", "14%", "4%", "+10pp"]
          - ["conservative_refusal", "4%", "2%", "+2pp"]
      - title: "Failure Mode Dominant Distribution: Human vs LLM (incompleteness)"
        columns: ["Failure Mode", "Human Annotator %", "LLM Coder %", "Δ"]
        rows:
          - ["assumption_based_action", "30%", "64%", "-34pp"]
          - ["arbitrary_rule_selection", "40%", "16%", "+24pp"]
          - ["unauthorized_escalation", "16%", "12%", "+4pp"]
          - ["scope_misapplication", "10%", "6%", "+4pp"]
          - ["conservative_refusal", "4%", "2%", "+2pp"]
      - title: "Category Collapsing Effect on κ"
        columns: ["Scheme", "Categories", "κ", "Interpretation"]
        rows:
          - ["Original 5-cat", "unauth_esc / assumption / scope_mis / arb_rule / cons_ref", "0.39", "Fair"]
          - ["Collapsed 4-cat", "boundary_exceeding / scope_mis / arb_rule / cons_ref", "0.44", "Fair-to-moderate"]
          - ["Collapsed 3-cat", "active_violation / misparse / refusal", "0.51", "Moderate"]
    figures_description:
      - "Appendix figure: confusion matrix heatmap — Human Annotator 1 vs Annotator 2, 5×5 grid showing concentration of disagreements at unauthorized_escalation ↔ assumption_based_action boundary"
    analysis: >
      κ=0.39 是 median 档的 defining result。对 paper 的影响：
      (1) C5 framing 从 "validated taxonomy with type-diagnostic failure signatures" 降级为
      "convergent LLM-coded and human evidence with moderate agreement on coarse failure mechanisms"。
      (2) Contribution (3) 追加 qualifier："supported by convergent LLM-coded and human evidence
      (κ=0.39, fair; 4/6 types match dominant failure mode; collapsed 3-category κ=0.51)"。
      (3) fine-grained per-type failure mode percentages（如 auth_scope 78% unauthorized_escalation）
      不能作为 validated claims，降级为 "automated coding suggests" + 标注 human-LLM disagreement。
      (4) 正面：Ambiguity Blindness (5% awareness) 在 human annotation 中完全确认——这是最 portable 的发现。
      (5) 正面：coarse-grained level 的 spec→guess vs ling→misparse dissociation 在 collapsed 3-cat
      κ=0.51（moderate）下仍可 claim。
      Rebuttal 策略：(a) κ=0.39 exceeds 纯 automated 的 baseline（LLM-LLM κ=0.517 measures agreement
      不是 accuracy）；(b) auth_scope/incompleteness 的 boundary disagreement 是 well-known problem
      in annotation science（intention attribution from behavioral data is inherently ambiguous）；
      (c) collapsed 4-cat κ=0.44 在 "合并 semantically close categories 后" approach moderate。
      对 ARR score 影响：κ=0.39 使 C5 从 potential strength 变为 acknowledged limitation。
      不阻止 Findings acceptance 但 reviewer 会标注 "contribution (3) overreaches given human agreement"。
      预计 1 位 reviewer 降 0.25 分因此，净 expected score 3.75 而非 4.0。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d5acb1f-88ba-4e51-b69a-f24227097cca",
  "isSidechain": false,
  "requestId": "req_011CbL2A662GT6PgTeL3APCb",
  "type": "assistant",
  "uuid": "03a34dc9-179c-483c-a67b-0458b87b76ce",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hy3nTBjgkrthQjMVgjzAB6",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9817,
      "cache_read_input_tokens": 36574,
      "output_tokens": 32743,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9817,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 32743,
          "cache_read_input_tokens": 36574,
          "cache_creation_input_tokens": 9817,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9817
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

_source line 25_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：κ re-annotation succeeds marginally (meets threshold but doesn't strongly validate LLM coding), SOPBench partially replicates — paper's quantitative core…",
  "leafUuid": "03a34dc9-179c-483c-a67b-0458b87b76ce",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43"
}
```

---

### Runtime record

_source line 26_

```json
{
  "type": "ai-title",
  "aiTitle": "Human re-annotation of failure modes for differential nocuity validation",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：κ re-annotation succeeds marginally (meets threshold but doesn't strongly validate LLM coding), SOPBench partially replicates — paper's quantitative core…",
  "leafUuid": "03a34dc9-179c-483c-a67b-0458b87b76ce",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43"
}
```

---

### Runtime record

_source line 28_

```json
{
  "type": "ai-title",
  "aiTitle": "Human re-annotation of failure modes for differential nocuity validation",
  "sessionId": "f40dd3ff-f3b8-4d76-a956-dcce22cdea43"
}
```

---
