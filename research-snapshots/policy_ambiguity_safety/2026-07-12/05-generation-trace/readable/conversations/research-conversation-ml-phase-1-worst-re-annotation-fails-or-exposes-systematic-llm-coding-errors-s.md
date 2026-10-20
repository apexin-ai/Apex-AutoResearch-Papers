# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：κ re-annotation fails or exposes systematic LLM coding errors, SOPBench sho

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/274e5e0e-5042-4718-83a5-9d151d93b8f1.jsonl`
- **Structured JSON:** [`9df22e4fa29eeabc83e4.json`](../../sessions/9d/9df22e4fa29eeabc83e4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-23T19:15:04.897Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-23T19:15:04.897Z",
  "sessionId": "274e5e0e-5042-4718-83a5-9d151d93b8f1",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：κ re-annotation fails or exposes systematic LLM coding errors, SOPBench shows inconsistent results — qualitative contribution collapses, paper must be reframed around quantitative core alone\n核心假设：['κ_reannotation < 0.35 (poor) OR human coders disagree with LLM-assigned dominant failure modes in ≥3/6 types, invalidating C5 fine-grained claims', 'SOPBench C1 effect is weak (Δ<15pp) or non-significant for ≥2 models, undermining cross-domain generalizability', 'Reviewers flag both C3 fragility AND C5 weak validation simultaneously, questioning depth of analysis', \"At least one reviewer sees the paper as 'well-executed but incremental — binary effect (C1) is expected, type hierarchy (C2) has small V=0.137'\", 'Model×type interaction (C4) survives but cannot alone carry a top-venue paper without supporting qualitative story']\n关键指标范围：{'kappa_reannotation': [0.1, 0.34], 'sopbench_c1_delta_pp': [5, 18], 'sopbench_type_rank_rho': [-0.2, 0.4], 'c5_human_llm_dominant_mode_agreement': [1, 3], 'expected_arr_score': [3.0, 3.49], 'expected_reviewer_confidence': [2.5, 3.5]}\n叙事方向：Reframe required — same venue, different angle. C5 failure mode taxonomy demoted to appendix ('exploratory automated analysis'). 'Ambiguity Blindness' becomes a one-paragraph observation, not a named contribution. Paper restructures around two contributions only: (1) causal quantification (C1 with perturbation control — this remains the strongest causal evidence in the literature regardless of C5), (2) model×type interaction (C4 — 52pp auth_scope range is striking and novel even without failure mode explanation). New angle: reframe as a **measurement and benchmarking** paper rather than an **analysis** paper. Title pivots toward 'Measuring Differential Vulnerability to Policy Ambiguity Across LLM Agent Families.' Lean into methodological contribution: matched-pair causal design + perturbation control as a reusable evaluation protocol. Add explicit 'Benchmark and Protocol Release' as contribution (3) replacing the failed qualitative analysis. Discussion section shifts from 'why models fail differently' (which needs C5) to 'implications for model selection and deployment risk assessment' (which only needs C4 numbers). If SOPBench also weak, drop cross-domain claims entirely and frame τ²-bench scope as acknowledged limitation with future work. The 2,997-episode dataset + evaluation protocol + C1+C4 quantitative findings can still constitute a solid EMNLP contribution if positioned as empirical infrastructure rather than theoretical framework.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: policy_ambiguity_safety\nvenue: emnlp-2026\nfocus: Evaluate the paper's competitiveness at EMNLP 2026 ARR assuming κ re-annotation succeeds (κ≥0.35). Key question: does upgrading contribution (3) from 'initial evidence' to validated move the paper from 3.75 to 4.0? What remaining gaps would reviewers still flag?\n\n## paper_framing.md\n\n# Paper Framing — policy_ambiguity_safety\n\n> 最后更新: 2026-05-23 UTC | 状态: R18 全部 resolved + 6 supplementary experiments (5 done, 1 running)\n> 目标: EMNLP 2026 (ARR May cycle, DDL 2026-05-25)\n> Dream: dream_20260520T112859 — best 3.5 / median 3.0 / worst 2.5 (pre-pivot; re-dream needed)\n> 5-model: 2,997 episodes, C1 confirmed (+34.0pp, 5 models), C4 upgraded (model×type interaction)\n> Supplementary experiments (2026-05-22/23):\n>   - ✅ Cross-Judge Validation: Fleiss' κ=0.717, rankings preserved (ρ≥0.70), no same-family bias → R18-N2 升级为 validated\n>   - ✅ Controlled Confound: ±0.1pp token-count effect, β=+0.027 (p=0.003) → R18-W3 resolved\n>   - ✅ Residual Decomposition: ICC=0.749, 15.2pp stochastic / 45.6pp systematic → R18-W2 answered\n>   - ✅ Disambiguation Prompting: overall not significant, GPT-4.1 auth_scope -28pp (p=0.001) → rebuttal ammunition\n>   - ✅ Human Annotation Prep: 100 traces + codebook ready\n>   - 🔄 SOPBench Expansion: DeepSeek ~78% complete\n\n## Core Insight\n\nPolicy ambiguity universally causes massive safety violations in LLM agents (+34.0pp across 5 architecturally diverse models), with a significant type hierarchy (incompleteness 53.6% >> coreferential 31.6%). Specification-layer types are more dangerous on average (Δ=6.08pp, p=0.017), but the deeper finding is a **model × type interaction**: authorization scope vulnerability varies 52pp across models (12% Claude to 64% GPT-5.4), revealing that safety training differentially mitigates specific ambiguity types, while incompleteness remains universally dangerous. This interaction connects Berry & Kamsties' nocuous ambiguity theory to modern safety alignment and suggests both type-aware triage AND model-aware risk assessment.\n\n## Title (Working)\n\n\"Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families\"\n\nAlternative: \"Differential Nocuity: How Ambiguity Type and Model Architecture Shape Safety Violations in LLM Agents\"\n\nNote: Pivoted from \"Uniformly Nocuous\" → \"Specification-Layer Dominant\" (2-model) → \"Differential Nocuity with Model Interaction\" (5-model). The model × type interaction is the novel finding that elevates the paper beyond simple effect demonstration.\n\n## Core Claims\n\n### C1: Binary Effect (PRIMARY — confirmed, 5 models)\nAmbiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +34.0pp (5-model), McNemar OR=15.1 (CI: [10.78, 21.17]), p<0.0001. Holds across all 6 types and all 5 models.\n- **Evidence**: 2,997 episodes across 5 models × 6 types × 2 conditions. Bootstrap CI: [+31.2pp, +36.9pp].\n- **Per-model**: Claude +25.7pp, Qwen3 +32.4pp, GPT-4.1 +34.7pp, GPT-5.4 +38.3pp, DeepSeek +39.0pp — all p<10^-17.\n- **Strength**: Extremely strong. Replicated across 5 architecturally diverse models (proprietary dense, open-source MoE, open-source dense), 6 types, 2 domains. No exceptions.\n- **Causal backing**: Matched-pair design + perturbation control (plan_010, Δ_perturb=3.33pp, PASS) → strongest causal inference in the literature.\n- **Logistic regression**: condition_amb coef=2.278, z=19.65, p<0.001 — ambiguity is the dominant predictor even after controlling for token delta, model, and type.\n\n### C2: Type Hierarchy (SECONDARY — confirmed, 5 models)\n**PIVOTED from uniformity null.** 6-type hierarchy significant: omnibus χ²=28.02, p=3.6×10^-5, V=0.137 (small but well-powered: actual power=0.993, MDE=0.093). 3-tier structure emerges from TOST analysis.\n- **Evidence**: 2,997 episodes (5 models × 6 types × 2 conditions, ambiguous only: 1,499 episodes)\n  - **High tier**: incompleteness 53.6% (standout — universally dangerous across all models)\n  - **Mid tier**: lexical 42.8%, auth_scope 41.6%, scopal 39.4%, CP 36.8% — pairwise equivalent at ±15pp\n  - **Low tier**: coreferential 31.6% (lowest — partial disambiguation via tool responses)\n- **TOST structure**: ±15pp: 8/15 equivalent, 7/15 non-equivalent. ±10pp: 4/15 equivalent, 11/15 non-equivalent. Types are NOT interchangeable.\n- **V=0.137 context**: Below 0.20 threshold but well-powered (power=0.993). The type effect is real but small — the 3-tier structure captures it better than a single V statistic. The heterogeneity is driven by the extremes (incompleteness 53.6% vs coreferential 31.6% = 22pp gap).\n- **Coreferential as boundary case**: 31.6% violation rate is the lowest but still substantial (+18.7pp vs unambiguous). Agents partially disambiguate via tool responses and cautious strategies. Conservative_refusal rate 6-11% (vs avg 2-3%).\n- **Model-dependence of type rankings**: Type rankings are NOT identical across models. Incompleteness is top-2 for ALL models, but auth_scope ranges from #1 (GPT-5.4, DeepSeek) to #6 (Claude). See C4.\n\n### C3: Layer Effect (TERTIARY — suggestive, fragile under within-judge analysis)\n**[2026-05-20 REVISED with 5-model data + within-judge check]** Specification-layer ambiguities cause more violations than linguistic-layer on average, but the effect is modest, model-dependent, and fragile under subgroup analysis.\n- **Evidence (5-model aggregate)**: Spec 44.0% vs Ling 37.9%, Δ=6.08pp, CI [1.14, 11.02], χ²=5.73, p=0.017, V=0.062 (small), OR=1.29 [1.05, 1.58].\n- **Within-judge fragility**: gpt-4.1 judged group (gpt-5.4+DeepSeek): Δ=+8.0pp, p=0.059 (marginal). gpt-5.4 judged group (gpt-4.1+Claude+Qwen3): Δ=+4.8pp, p=0.157 (n.s.). Pooled significance may partly reflect between-judge variance or insufficient within-group power. Paper表述: \"suggestive\" or \"a moderate tendency,\" NOT \"confirmed.\" Disclose within-judge non-significance in Limitations.\n- **Per-model layer gaps** (THE KEY FINDING — feeds C4):\n  - GPT-5.4: +14.0pp (spec 48.0% vs ling 34.0%) — strong\n  - GPT-4.1: +12.0pp (spec 46.7% vs ling 34.7%) — strong\n  - Claude: +3.3pp (spec 32.0% vs ling 28.7%) — weak\n  - DeepSeek: +2.0pp (spec 50.7% vs ling 48.7%) — negligible\n  - Qwen3: -0.9pp (spec 42.7% vs ling 43.6%) — reversed!\n- **Root cause**: auth_scope is the primary driver. GPT models have extremely high auth_scope rates (46-64%), inflating their spec-layer average. Claude (12%) and Qwen3 (26%) have low auth_scope, so their spec-layer advantage disappears.\n- **Framing decision**: C3 is NOT \"spec-layer nearly twice as dangerous\" (that was 2-model artifact). The correct framing is: \"Specification-layer types are significantly more dangerous on average (Δ=6.08pp, p=0.017), but this aggregate masks a model × type interaction where the gap varies from +14pp (GPT-5.4) to -1pp (Qwen3). The interaction, not the main effect, is the theoretically interesting finding (see C4).\"\n- **Info delta as mediator** [MF-2]: Token delta significant in 5-model logistic regression (coef=0.022, z=3.49, p=0.0005). Spec-layer clauses require more tokens to disambiguate (auth_scope 36.1, incomp 34.6 vs coref 7.8 tokens). Info delta partially mediates but doesn't eliminate the condition effect (condition_amb coef=2.278 dominates).\n- **Layer overlap persists**: CP (36.8%, spec) < scopal (39.4%, ling). Mid-tier cluster spans both layers. Layer effect is driven by extremes: incompleteness (53.6%, spec) vs coreferential (31.6%, ling).\n- **ICC convergent evidence** [plan_006]: Per-type ICC mirrors layer hierarchy — Ling-layer ICC all excellent (scopal 0.989, lexical 0.981, coref 0.976), Spec-layer ICC all good (auth 0.857, CP 0.856, incomp 0.807). Spec-layer less reproducible — agents guess differently each run when external disambiguation channels are absent.\n- **CL connection**: Parallels pragmatics vs semantics distinction. Good-enough processing (Ferreira et al. 2002). Disambiguation channel framework: linguistic ambiguity has partial external resolution; specification ambiguity forces guessing.\n\n### C4: Model × Type Interaction (UPGRADED — star finding, 5 models complete)\n**[2026-05-20 DEFINITIVE, 5/5 models]** Models show significantly different vulnerability profiles despite universal binary effect. The interaction is the paper's most novel finding.\n- **Model main effect**: Overall χ²=31.02, p=3.0×10^-6, V=0.102. Ambiguous-only: χ²=24.01, p=7.9×10^-5.\n  - Vulnerability ranking: Claude 30.3% < GPT-5.4 41.0% ≈ GPT-4.1 40.7% < Qwen3 43.1% < DeepSeek 49.7%\n  - Bootstrap CI confirms: Claude significantly lower than all others; DeepSeek significantly higher than GPT models.\n- **Model × Type interaction matrix** (ambiguous condition, violation rates):\n  ```\n  Type                  GPT-5.4  GPT-4.1  Claude  Qwen3   DeepSeek\n  authorization_scope     64%     46%      12%     26%     60%\n  conditional_precedence  34%     36%      36%     40%     38%\n  incompleteness          46%     58%      48%     62%     54%\n  lexical                 42%     34%      32%     52%     54%\n  coreferential           18%     32%      22%     42%     44%\n  scopal                  42%     38%      32%     37%     48%\n  ```\n- **Key interaction patterns**:\n  - **auth_scope**: 52pp range (Claude 12% → GPT-5.4 64%). The MODEL-DIFFERENTIATING type. Claude's RLHF appears to specifically train authorization boundary awareness.\n  - **coreferential**: 26pp range (GPT-5.4 18% → DeepSeek 44%). Second most model-dependent. Open-source models struggle more with referential ambiguity.\n  - **incompleteness**: Universally high (46-62%, 16pp range). ALL models fail on missing information — safety training doesn't help when information literally isn't there.\n  - **CP**: Most model-invariant (34-40%, 6pp range). Explicit rule conflicts treated similarly by all architectures.\n- **Per-model type χ²** (which models show type-specific vulnerability patterns):\n  - GPT-5.4: χ²=23.44, p=0.0003, V=0.28 — strongest type differentiation (very high auth_scope, very low coref)\n  - Claude: χ²=17.87, p=0.003, V=0.24 — strong differentiation (very low auth_scope, moderate others)\n  - Qwen3: χ²=15.89, p=0.007, V=0.23 — moderate differentiation (high incomp+lex, low auth_scope)\n  - GPT-4.1: χ²=9.89, p=0.078, V=0.18 — borderline\n  - DeepSeek: χ²=6.31, p=0.277, V=0.14 — NOT significant (uniformly high across all types)\n- **Fleiss κ = 0.384 (fair agreement)**: Models only moderately agree on which specific clauses trigger violations. The binary effect is universal, but the WHICH-clauses question is model-dependent.\n- **Theoretical implications**: (1) Safety training differentially addresses specific ambiguity types — Claude's auth_scope robustness suggests authorization boundary handling was explicitly or implicitly trained. (2) Incompleteness is a \"safety training blind spot\" — all models fail equally. (3) DeepSeek's uniform vulnerability suggests less type-specific safety training.\n- **Framing**: C4 from \"models agree\" → \"Models show systematically different vulnerability profiles. The binary effect is universal, but HOW models fail depends on the intersection of ambiguity type and safety training approach. auth_scope is the canary type — most sensitive to safety training quality.\"\n- **Evidence from plan_005**: 2-model failure modes consistent (5/6 dominant modes identical). 5-model failure mode analysis pending.\n- **Layer effect moderation**: C3's aggregate layer gap (6.08pp) is driven by GPT models' high auth_scope rates. The layer effect is itself model-dependent (GPT +12-14pp, Claude +3pp, Qwen3 reversed), making the MODEL × TYPE interaction more fundamental than the LAYER main effect.\n\n### C5: Error Analysis (CONFIRMED — EMNLP core)\nDifferent ambiguity types produce qualitatively different failure modes with type-specific signatures. plan_005 (123+122 violation traces across gpt-5.4 and gpt-4.1, confidence=0.94).\n- **Evidence**: plan_005 complete (gpt-5.4: 123 traces, gpt-4.1: 122 traces). Key findings:\n  - **Type-specific failure signatures**: auth_scope → unauthorized_escalation (72%/83%); incompleteness → assumption_based_action (61%/66%); scopal → scope_misapplication (76%/74%); lexical → assumption_based_action (71%/53%); CP → scope_misapplication (41%/28%) + arbitrary_rule_selection (29%/28%); coreferential → scope_misapplication (44%) / assumption_based_action (38%)\n  - **Cross-model consistency**: 5/6 types share the same dominant failure mode across gpt-5.4 and gpt-4.1. Only coreferential diverges (scope_misapplication vs assumption_based_action). Overall mode distribution nearly identical: both ~33% assumption_based_action, ~26-32% unauthorized_escalation, ~25-28% scope_misapplication. Failure mode profiles are type-specific, not model-specific.\n  - **Layer mechanism**: Ling-layer dominated by scope_misapplication (39% ling avg vs 15% spec avg) = \"misparse\"; Spec-layer dominated by unauthorized_escalation + assumption_based_action = \"active guessing\" → explains higher violation rates\n  - **Ambiguity Blindness empirically confirmed**: awareness rate gpt-5.4=4.1%, gpt-4.1=10.7% (both very low); surface_adoption >88% all types both models; escalate_to_user <1%. Nuance: gpt-4.1 (mid-tier) shows 2.6× higher awareness than gpt-5.4 (frontier) — awareness may inversely correlate with action-orientation (frontier models more \"confident,\" act without hesitation)\n  - **Cross-domain consistency**: airline vs retail failure mode profiles Δ < 13pp (unauthorized_escalation shows largest domain effect: retail 38.6% vs airline 26.1%)\n  - **Coreferential boundary**: conservative_refusal 6-11% (vs avg 2-3%) partially explains low violation rate — agents sometimes pause rather than guess. N=25 combined traces show no single dominant failure mode (flat distribution: scope_misapplication 32%, assumption_based_action 28%, unauthorized_escalation 16%) — contrasts with other types' sharp signatures, reflecting the diversity of resolution strategies for referential ambiguity\n  - **Lexical surprise**: 53-71% assumption_based_action — agents treat word ambiguity as information gap, not misparse\n- **Automated inter-coder agreement** [MF-5, Reviewer-validated]: Cross-coding 60 traces (gpt-5.4 vs gpt-4.1 as independent coders). 4-category merged: 80% agreement, Cohen's κ=0.594 (moderate). κ deflated by kappa paradox — lexical 91.7% agreement → κ=0.0 (11/12 same label, chance agreement also high), scopal 100% agreement → κ undefined. True disagreement concentrated at unauthorized_escalation ↔ inappropriate_action boundary in auth_scope (κ=0.054) and incompleteness (κ=0.233).\n  - **Reporting strategy** [Reviewer recommendation]: (1) Compute Gwet's AC1 as primary metric (designed for kappa paradox, expected 0.70-0.75); (2) Report 80% agreement + 5/6 dominant mode consistency as headline validity evidence; (3) Report κ honestly with kappa paradox caveat; (4) Auth_scope failure mode: soften to \"dominated by boundary-exceeding behaviors (unauthorized_escalation or inappropriate_action, >90%)\" instead of specific percentages; (5) Fine-grained 6-type as appendix with \"automated coding\" caveat.\n  - **C5 safety**: Ambiguity Blindness (<5-11%), surface_adoption (>88%), layer mechanism (ling→scope vs spec→escalation) all robust. Fine-grained per-type percentages unreliable at κ=0.594. Plan_009 human anchor (20-30 failure mode traces) would upgrade from \"moderate automated\" to validated.\n- **EMNLP value**: Highest. Provides the linguistic WHY behind the quantitative WHAT. Cross-model + cross-domain consistency elevates from anecdotal to systematic finding. \"Ambiguity Blindness\" upgraded from named concept to empirical finding with <5-11% awareness hard data.\n\n## Narrative Structure (CL-first for EMNLP)\n\n### Intro Logic Chain\n1. Agent policies are written in NL → contain ambiguity (established)\n2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact\n3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.\n4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter? Does it depend on the model?\n5. **This paper**: First causal, type-granularity, cross-model study. Matched-pair design + perturbation control isolates ambiguity effect. 5 models × 6 types.\n6. **Core findings**: (a) All ambiguity is nocuous (+34.0pp, 5 models), (b) type DOES predict severity — 3-tier hierarchy with incompleteness most dangerous, (c) models show dramatically different vulnerability profiles — auth_scope varies 52pp across models, suggesting safety training differentially addresses ambiguity types, (d) while incompleteness remains universally dangerous, a \"safety training blind spot.\"\n\n### Section Map\n- **§1 Intro**: Gap + contributions (causal map + differential nocuity + model×type interaction)\n- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R\n- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R\n- **§4 Method**: Matched-pair causal design, τ²-bench, 5 models (3 proprietary + 2 open-source), clause generation, perturbation control, cross-judge evaluation\n- **§5 Results**: C1 (binary, +34.0pp, 5 models) → C2 (type hierarchy, 3-tier) → C3 (layer effect, modest but significant) → C4 (model×type interaction — star finding)\n- **§6 Analysis**: C5 error analysis — qualitative failure modes per type. Ambiguity Blindness. Model-specific patterns.\n- **§7 Discussion**: Differential nocuity theory. Safety training selectivity. Disambiguation channel framework. Limitations (2 domains, synthetic injection, LLM-as-judge).\n- **§8 Conclusion**: All policy ambiguity is nocuous, but type AND model jointly determine risk level. Both type-aware auditing and model-specific risk assessment recommended.\n\n## Anticipated Reviewer Concerns\n\n### RC1: \"Type effect could be artifact of taxonomy granularity\"\n**Response**: (a) Layer effect (Spec vs Ling ~19pp gap) is robust — holds even if individual types are reclassified. (b) 2-layer structure grounded in Li et al. + Massey et al. (c) Coreferential's low rate has structural explanation (disambiguation channels), not just noise. (d) TOST confirms types are NOT equivalent (0/15 pairs at ±10pp).\n\n### RC2: \"Taxonomy is ad hoc / why these 6 types\"\n**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).\n\n### RC3: \"Only API models, no open-source\"\n**Response**: ✅ RESOLVED. 5-model coverage spans: frontier proprietary (gpt-5.4, claude-sonnet-4-6) + mid-tier proprietary (gpt-4.1) + open-source MoE (qwen3-235b) + open-source dense (deepseek-v3). Three providers (OpenAI, Anthropic, Chinese open-source). Two architecture types (dense, MoE). Model×type interaction (C4) reveals rich cross-model patterns.\n**Note [Reviewer 2026-05-20]**: Cross-judge asymmetry — Claude judged by gpt-5.4, gpt-5.4 judged by gpt-4.1. Must disclose in Method. plan_009 judge calibration measures this bias.\n\n### RC4: \"Synthetic ambiguity injection lacks ecological validity\"\n**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.\n\n### RC5: \"τ²-bench limited to retail/airline\"\n**Response**: ✅ ADDRESSED (plan_017). Cross-benchmark replication on SOPBench (Li et al., 2025) — Healthcare + Bank domains, 100 clause pairs × 5 models = 1,000 episodes with rule-based verifier. If C1 replicates, paper moves from \"customer service finding\" to \"cross-domain finding\" spanning 4 domains (retail, airline, healthcare, banking). Result in Appendix with main-text summary. τ²-bench remains primary; SOPBench provides independent cross-domain confirmation.\n\n### RC6: \"Binary effect is obvious — of course ambiguity causes errors\"\n**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOES predict severity — specification-layer ambiguities are nearly twice as dangerous, connecting to disambiguation channel availability.\n\n### RC7: \"Incompleteness matched-pair confound (information asymmetry)\"\n**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.\n\n### RC8: \"RC attachment in coreferential overlaps with scopal / structural ambiguity\"\n**Response**: (a) Our scopal category is explicitly scoped to quantifier/negation/modal scope interactions, not syntactic attachment. (b) RC attachment in policies manifests as *referential* confusion (which entity does the clause modify?) not *scope* confusion (which operator takes wide scope?). (c) Li et al. 2024 distinguishes syntactic ambiguity (including RC attachment) from scopal ambiguity — our grouping follows their treatment that RC attachment is closer to coreferential than scopal in terms of downstream interpretation. (d) Empirically, if the distinction were problematic, coreferential and scopal would show identical violation patterns — the error analysis (C5) can test whether their failure modes differ.\n\n### RC9: \"authorization_scope is just a subtype of incompleteness\"\n**Response**: (a) Incompleteness = missing conditions/exceptions/boundaries (structural absence). Authorization scope = ambiguous permission/role boundaries that ARE stated but vague (e.g., \"authorized personnel\" without specifying which functions). (b) The disambiguation pattern differs: incompleteness adds new conditions; auth_scope clarifies existing permission boundaries. (c) Empirically testable: if they were the same, their violation patterns and failure modes (C5) would be indistinguishable. (d) Report disambiguation length ratio per type as control variable in §4 Method.\n\n### RC10: \"API sampling noise undermines reliability\"\n**Response**: ✅ RESOLVED. plan_006 ICC=0.919 [0.892, 0.940] (excellent). (a) Per-clause violation rates highly reproducible across 3 independent replicates. (b) Binary ICC=0.847 (good). (c) Both models show near-identical ICC (gpt-5.4: 0.921, gpt-4.1: 0.918). (d) Bootstrap CI + ICC double evidence. (e) Previously identified ±8pp noise is within expected variance given the ICC confidence intervals.\n\n### RC11: \"Prompt sensitivity confound\" [Dream A9 — best tier \"strongest point\"]\n**Concern**: The +35-42pp effect is attributed entirely to ambiguity, but without a control condition using non-ambiguity perturbations (synonym substitution, clause reordering), the paper cannot cleanly distinguish ambiguity-specific harm from general prompt brittleness.\n**Response**: ✅ RESOLVED. plan_010 perturbation control (120 episodes): Δ_perturb=3.33pp (CI contains 0) vs ambiguity Δ=36.5pp. Non-ambiguity surface changes cause zero meaningful effect. This is the strongest causal evidence in the agent safety literature.\n\n## Concept Naming (distill insight: 命名即贡献)\n\nCore phenomenon: **\"Differential Nocuity\"** — all policy ambiguity types are nocuous for LLM agents (+34.0pp, all 5 models), but vulnerability varies by BOTH type and model. Incompleteness is universally dangerous (46-62%), while auth_scope vulnerability depends dramatically on safety training (12% Claude to 64% GPT-5.4). Unlike human RE where organizational context renders most ambiguity innocuous, agents lack disambiguation channels AND their safety training creates type-specific blind spots.\n\nSecondary phenomenon: **\"Ambiguity Blindness\"** — agents process grammatically fluent ambiguous clauses without meta-cognitive awareness of the ambiguity, adopting surface interpretations. Contrasts with explicit rule conflicts where agents show awareness and choose conservatively.\n\nTertiary phenomenon: **\"Disambiguation Channel Framework\"** [renamed from \"Hypothesis\" per Dream review SF-5] — the layer hierarchy reflects availability of external disambiguation: linguistic ambiguity (coreferential, lexical) can sometimes be resolved by tool responses, user context, or world knowledge; specification ambiguity (auth_scope, incompleteness) has no external resolution channel, forcing agents to guess. This is an explanatory framework supported by observational evidence (ICC pattern, failure mode distribution, coreferential boundary case), not a tested causal hypothesis. Future Work: manipulation experiment (inject spec-layer disambiguation info into tool responses, test if gap shrinks).\n\nQuaternary phenomenon: **\"Systematic Nocuity\"** [per Dream review SF-7] — B&K framework distinguishes nocuous (divergent interpretations) from innocuous (convergent). Our data reveals a third type: all models converge on the same WRONG interpretation (27% of ambiguous episodes). This is more dangerous than divergent nocuity — it's invisible in inter-model agreement metrics and appears \"correct\" until compared against ground truth. Proposed as B&K extension in Discussion.\n\n## Opening Hook Strategy (distill insight: 具体案例, 不要 \"Recently...\")\n\nOpen with a concrete τ²-bench failure: e.g., a customer returns a customized item within the return window; the agent grants a full refund + free return shipping because the policy says \"items may be returned within 30 days\" (scopal: \"items\" scopes over all categories including custom). The unambiguous version specifies \"standard items only\" — agent correctly refuses. One word of ambiguity → $200 unauthorized refund.\n\n## Narrative Type: 突破局限型 (distill pattern, 5/8 papers)\n\n\"DRIP-R classifies 5 ambiguity types and shows models disagree on interpretation → but does not measure whether this disagreement leads to safety violations. We close this gap — and find the answer is surprising: not all types are equal, specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones.\"\n\n## Benchmark Comparison Table (distill insight: 必有 feature matrix)\n\n| Feature | DRIP-R | PhantomPolicy | PolicyBank | AgentPex | **Ours** |\n|---------|--------|---------------|------------|----------|----------|\n| Ambiguity taxonomy | 5 RE types | — | 3 gap types | — | **6 types (2-layer)** |\n| Causal design | — | — | — | — | **matched pairs** |\n| Safety violation metric | — | binary | — | procedural | **3-tier severity** |\n| Cross-type comparison | descriptive | — | — | — | **statistical (χ² + V)** |\n| Models tested | 6 API | 4 API | 2 API | 2 API | **3 API + 2 open-source** |\n| Domain | retail | mixed | retail | telecom/retail/airline | **retail + airline** |\n\n## Contribution Positioning (for EMNLP) [revised 2026-05-20 with 5-model data]\n\n1. **Causal quantification of ambiguity's safety impact**: First matched-pair causal study of policy ambiguity → agent safety violations. Binary effect +34.0pp (OR=15.1, p<0.0001) across 5 architecturally diverse models and 6 ambiguity types. Perturbation control (Δ_perturb=3.33pp) confirms ambiguity-specific causation. Strongest causal evidence in the agent safety literature.\n2. **Differential Nocuity framework + Model × Type Interaction**: Not all ambiguity is equally dangerous, and not all models are equally vulnerable. 3-tier type hierarchy (incompleteness >> mid cluster >> coreferential). Model × type interaction reveals 52pp range in auth_scope vulnerability (Claude 12% → GPT-5.4 64%), while incompleteness remains universally dangerous (46-62%). Safety training differentially mitigates specific ambiguity types. Connects Berry & Kamsties nocuous ambiguity theory to modern safety alignment.\n3. **Type-specific failure mode taxonomy + Ambiguity Blindness**: 245 traces across 2 models and 2 domains reveal type-diagnostic failure signatures: spec-layer → guess-and-act (unauthorized_escalation, assumption_based_action); ling-layer → misparse-and-apply (scope_misapplication). Agents show <5-11% awareness of ambiguity (\"Ambiguity Blindness\"), with >88% surface adoption and <1% user escalation. Practical implication: ambiguity detection must be externalized.\n\nNOTE: C3 (layer effect, Δ=6.08pp) is a component finding supporting contribution #2. The MODEL × TYPE interaction (C4) is now MORE central than the layer main effect. \"Disambiguation channel\" is an explanatory framework (not hypothesis — per SF-5). DeBERTa classifier, if included, is a preliminary PoC appendix, not a contribution.\n\n## Required Reference Expansion [Dream A2 + MF-4 RE literature gap]\n\nCurrent plan has thin references. Must add (≥25 total in final paper):\n- **Nocuous ambiguity detection (CRITICAL — MF-4)**: Chantree, Nuseibeh, de Roeck & Willis (2006, ASE) — first computational nocuous ambiguity detection; Chantree et al. (2008, RLAC) — expanded. Direct lineage to our DeBERTa classifier.\n- **Cross-domain RE ambiguity**: Ferrari, Spagnolo & Gnesi (2017-2019, ASE) — NLP-based cross-domain ambiguity detection. NLP4RE community work.\n- **Good-enough processing**: Ferreira, Bailey & Ferraro (2002); Ferreira & Patson (2007)\n- **LLM garden-path (SF-6)**: Li et al. (2024) — incremental comprehension of garden-path sentences by LLMs. Directly relevant to how LLMs process ambiguity.\n- **Anaphoric ambiguity (SF-6)**: Poesio & Artstein (2005, 2008) — annotation of anaphoric ambiguity. Poesio (2004) \"Ambiguity\" encyclopedia entry.\n- **Surprisal/expectation-based**: Levy (2008); Hale (2001)\n- **Instruction-following robustness**: Zhou et al. (IFEval, 2023); Qin et al. (ToolBench, 2024)\n- **Prompt sensitivity**: Sclar et al. (2024); Lu et al. (2022)\n- **Broader agent safety**: R-Judge, ToolEmu, InjecAgent\n- **Formal semantics of vagueness**: Lassiter & Goodman (2017)\n- **Garden-path**: Frazier & Rayner (1982)\n- **Ambiguity detection**: Willis et al. (2008); Ezzini et al. (TAPHSIR, 2022)\n- **Year verification needed**: Massey et al. — §1 引用 2013 vs 后文 2014, 需确认正确年份\n\n## Code/Data Release Plan [Dream A6 — three-tier consistent]\n\nMust commit to releasing:\n1. All 300 clause pairs (ambiguous + unambiguous variants) with type labels\n2. Evaluation scripts (τ²-bench integration, cross-judge pipeline)\n3. Statistical analysis code (all tests, bootstrap CI computation)\n4. Agent trace samples (anonymized) for reproducibility of C5\n\n## Figure Plan [Dream A12]\n\nMinimum figures for paper (zero-figure paper flagged in dream):\n1. **Figure 1**: System architecture / experimental pipeline overview (§4 Method)\n2. **Figure 2**: Forest plot — per-type binary effect sizes with 95% CI (§5 C1)\n3. **Figure 3**: Model × Type heatmap — violation rates across 4 models × 6 types (§5 C4)\n4. **Figure 4**: Visibility mechanism — CP vs scopal violation rates + trace evidence (§5 C3)\n5. **Figure 5**: Failure mode × type stacked bar/Sankey — per-type failure mode distribution (§6 C5)\n6. **Figure 6**: Cross-model failure mode consistency — side-by-side gpt-5.4 vs gpt-4.1 per-type distributions showing 5/6 convergence (§6 C5, supports C4)\n7. **Figure 7**: Annotated trace pair — CP (conflict detection) vs scopal (surface adoption) (§6 C5)\n\n## Berry & Kamsties Operationalization Note [Dream best Q5]\n\nBerry & Kamsties define nocuity as inter-reader divergence. Our design measures agent-vs-intent deviation. Full study should additionally test whether different models adopt different readings of the same ambiguous clause (true inter-model nocuity). If 4 models produce 4 different interpretations of the same clause → true nocuity. If all 4 adopt the same wrong interpretation → systematic bias, still nocuous but for different reason. Report inter-model agreement on ambiguous clauses as supplementary analysis.\n\n## Contingency Framing [RESOLVED — Scenario C occurred]\n\n> plan_002 结果: Scenario C 发生（omnibus p=0.0001, 所有类型 nocuous 但 severity 有显著差异）。\n> Framing 已 pivot 到 \"Differential Nocuity\" + \"Layer Hierarchy\" (D020)。本节仅保留历史记录。\n\n## Claude Baseline — RESOLVED [2026-05-20]\n\n✅ Claude works via OpenRouter proxy (47.94.22.126/v1) with provider prefix `anthropic/claude-sonnet-4-6`. 600 episodes complete (plan_002c). Claude shows lowest overall vulnerability (30.3%) and remarkable auth_scope robustness (12% vs GPT-5.4 64%).\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: full_study_clause_generation\n  claim: C1, C2, C3\n  description: 'Generate remaining clauses for full study: coreferential (50 new),\n    authorization_scope (50 new), lexical (+20 to reach 50), incompleteness (+20 to\n    reach 50). Total 140 new clauses. Validate all 300 clauses (50/type × 6 types)\n    for completeness and cross-type balance. Mix CP format per Reviewer suggestion\n    (labeled + unlabeled).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n- id: plan_001b\n  name: new_type_mini_pilot\n  claim: C1 (validation)\n  description: 'Mini-pilot for coreferential + authorization_scope (never tested):\n    5 clauses/type × 2 conditions × 1 model (gpt-5.4) = 20 episodes. Verify: (a) ambiguous\n    triggers violations (b) unambiguous control < 15%. If systematic issues found,\n    fix clause design before full study. API cost negligible (~$2). Per Reviewer warning\n    on untested types.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_002\n  name: full_study_api\n  claim: C1, C2, C3, C4, C5\n  description: 'Run 300 clauses × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6)\n    = 1,800 episodes on τ²-bench. Cross-judge evaluation. Output: episodes.jsonl +\n    judgments.jsonl. No GPU needed. Claude via OpenRouter proxy (base_url=http://47.94.22.126/v1).\n    [2026-05-20] Claude added per distill gap (4/8 papers use Claude baseline).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_001b\n  - plan_010\n  status: planned\n- id: plan_003\n  name: full_study_opensource\n  claim: C1, C2, C3, C4, C5\n  description: 'Run 300 clauses × 2 conditions × 2 open-source models via OpenRouter\n    API: qwen/qwen3-235b-a22b (235B MoE, Alibaba) + deepseek/deepseek-chat-v3-0324\n    (DeepSeek) = 1,200 episodes on τ²-bench. Cross-judge uses API models. Can run\n    in parallel with plan_002. No GPU needed. [2026-05-20] Pivoted from local GPU\n    → API: OpenRouter proxy confirmed to support Qwen3 and DeepSeek models. Eliminates\n    48h GPU requirement. Provider prefix required (e.g. qwen/qwen3-235b-a22b, not\n    qwen3-235b-a22b).\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_004\n  name: full_study_analysis\n  claim: C1, C2, C3, C4\n  description: 'Statistical analysis of full study data (3,000 episodes): (a) Binary\n    effect per type with bootstrap CI (C1) (b) Omnibus χ² + pairwise across 6 types\n    (C2) (c) Visibility comparison: CP vs scopal rates (C3) (d) Model × type interaction:\n    5×6 contingency + logistic regression (C4) Report effect sizes + CI for all comparisons\n    per Reviewer suggestion. [Dream A3] Power analysis: report MDE for C2 (given N=250/type\n    pooled) and C3 (given N=250 per type). If V < 0.20 but MDE > observed V, discuss\n    underpowered possibility. [Dream A4] TOST equivalence test with both ±15pp and\n    ±10pp margins. Justify margin choice explicitly. [Dream A10] Report per-type information\n    delta (token count difference between ambiguous and unambiguous variants) as control\n    variable. [Dream B&K] Inter-model agreement on ambiguous clauses: do 5 models\n    adopt same or different interpretations? (supplementary analysis)\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_005\n  name: error_analysis\n  claim: C5\n  description: \"Qualitative analysis of agent traces from full study: (a) Sample 50\\\n    \\ violation traces per type (300 total) (b) Classify failure modes (scope misapplication,\\\n    \\ conservative refusal,\\n    assumption-based action, arbitrary rule selection,\\\n    \\ etc.)\\n(c) Cross-type failure mode distribution (d) Visibility mechanism: compare\\\n    \\ CP traces (explicit conflict detection\\n    behavior) vs scopal traces (surface\\\n    \\ scope adoption without awareness)\\n(e) Model-specific failure patterns (connect\\\n    \\ to C4)\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  - plan_003\n  status: planned\n- id: plan_006\n  name: reliability_test\n  claim: C1, C2\n  description: 'Test-retest reliability: select 30 representative clauses (5/type),\n    run 3 independent replicates × 2 conditions × 2 API models (gpt-5.4, gpt-4.1)\n    = 360 episodes. Local models added when plan_003 GPU available. Compute ICC for\n    per-clause violation rates. Addresses Reviewer warning about ±8pp sampling noise\n    (scopal 51.7% → 43.3% across MVP/diag). Bootstrap CI width should be < 10pp for\n    key comparisons. [2026-05-20] API portion: 330/360 episodes complete (28/30 clauses),\n    judgments pending.\n\n    '\n  priority: P1\n  gpu_budget_hours: 15\n  deps:\n  - plan_001\n  status: planned\n- id: plan_007\n  name: realism_validation\n  claim: C1 (methodological)\n  description: \"Validate synthetic ambiguity injection realism: (a) Linguistic property\\\n    \\ comparison with DRIP-R natural ambiguities\\n    (sentence length, parse depth,\\\n    \\ Flesch-Kincaid, TTR) + KS tests\\n(b) Optional: discriminator test if DRIP-R\\\n    \\ data accessible Addresses RC4 (ecological validity).\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_009\n  name: judge_calibration\n  claim: C1 (methodological)\n  description: 'LLM-as-judge calibration per distilled research norm (5/8 papers):\n    (a) Sample 100 episodes stratified by type×model×condition (b) Human expert labels\n    (2 annotators, target κ ≥ 0.75) (c) Compute judge precision/recall/F1 against\n    human ground truth (d) Per-severity-tier agreement rates (e) Report in Method\n    section as standard practice per AgentAuditor/DRIP-R [Dream A7] Upgraded P1→P0:\n    Dream best-tier reviewers identified this as \"single most critical missing validation.\"\n    Without it, entire measurement chain from episode to violation label is unvalidated.\n    κ=0.91 measures LLM-LLM agreement, not accuracy.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_002\n  status: planned\n- id: plan_010\n  name: perturbation_control\n  claim: C1 (causal validity)\n  description: '[Dream A9] Non-ambiguity perturbation control arm to distinguish ambiguity-specific\n    harm from general prompt brittleness. Generate 30 clause pairs with non-ambiguity\n    perturbations: (a) 15 synonym substitution pairs (replace key terms with synonyms)\n    (b) 15 clause reordering pairs (reorder conditions without changing meaning) Run\n    30 × 2 conditions × 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6) = 180 episodes.\n    Key metric: Δ_net = Δ_ambiguity - Δ_perturb (net ambiguity-specific effect). [Reviewer升级]\n    必须在 plan_002/003 full study 之前完成—— 如果 perturbation Δpp ≈ ambiguity Δpp，2,400 episodes\n    全部无效。 低成本验证（30 pairs + 120 episodes API）优先于高成本投入。 [判定标准 — 5 档]: PASS: Δ_perturb\n    < 5pp (CI含0), ratio < 0.15 → C1 因果 claim 最强形式 PASS+caveat: 5-10pp, ratio 0.15-0.30\n    → 报告 perturbation baseline, C1 写 net effect CONDITIONAL: 10-15pp, ratio 0.30-0.45\n    → 需 Δ_net > 20pp 且显著才可发表 WARNING: 15-20pp, ratio 0.45-0.60 → C1 改为 \"additional\n    violations beyond sensitivity\" FAIL: > 20pp, ratio > 0.60 → 无法声称 ambiguity-specific,\n    需根本重新设计 [Power 注意]: N=120 对 10pp 差异 power ≈ 30%. 用 CI 宽度判定, 非 p-value. 若 CI 过宽(>15pp\n    width), 追加 60 episodes 压窄至 <10pp width. 输出标准化 verdict 文件: perturbation_Δpp, ambiguity_Δpp,\n    net_Δpp, CI, ratio, verdict.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  status: planned\n- id: plan_017\n  name: sopbench_cross_benchmark\n  claim: C1 (generalizability), C2 (partial)\n  description: 'Cross-benchmark C1 replication on SOPBench (Li et al., 2025). 7 domains\n    (Bank, DMV, Healthcare, Hotel, Library, University, Online Market) all different\n    from τ²-bench (retail + airline). Select 2 domains (Healthcare + Bank) for maximum\n    domain diversity. Construct 100 clause pairs (50/domain) covering 3-4 ambiguity\n    types (incompleteness, auth_scope, lexical, conditional_precedence) from SOPBench''s\n    NL SOP constraints. Run 100 pairs × 2 conditions × 5 models = 1,000 episodes.\n    SOPBench has rule-based verifier — no LLM judge needed. Key metrics: (a) Does\n    C1 binary effect replicate? (b) Is incompleteness still highest-risk type? (c)\n    Cross-benchmark effect size correlation. Addresses SF-8 (single benchmark external\n    validity). Result goes in Appendix with 1-sentence summary in main text. [2026-05-22]\n    Approved by user. Estimated 1 day including clause construction.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps: []\n  status: planned\n- id: plan_008\n  name: classifier_poc\n  claim: practical contribution\n  description: 'Binary ambiguity detector PoC: fine-tune DeBERTa-v3-large on annotated\n    clause pairs (ambiguous/unambiguous labels). Eval on held-out set. Demonstrates\n    practical applicability of findings. Phase 3 from IDEA_BRIEF, scoped to PoC for\n    EMNLP.\n\n    '\n  priority: P2\n  gpu_budget_hours: 8\n  deps:\n  - plan_001\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: diag_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_002\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_005\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_006\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_009\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cross_judge_kappa_weighted: 0.685\n    cross_judge_exact_agreement: 0.76\n    cross_judge_binary_kappa: 0.74\n    human_llm_pooled_kappa_weighted: 0.807\n    human_inter_annotator_kappa_weighted: 0.762\n    n_episodes: 100\n- exp_id: plan_002c\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_003a\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_003b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_004\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics: {}\n- exp_id: plan_010\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    total_violations_coded: 614\n    types_unanimous_dominant_fm: 3/6\n    types_majority_dominant_fm: 6/6\n    inter_coder_kappa: 0.5173\n    percent_agreement: 0.656\n    disambiguation_awareness_overall: 0.046\n    elapsed_seconds: 98.5\n- exp_id: plan_011\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    overall_delta_pp: -6.6\n    overall_baseline: 0.41\n    overall_mitigated: 0.343\n    auth_scope_delta_pp: -18\n    incompleteness_delta_pp: -3.4\n    lexical_delta_pp: -8.9\n    cond_prec_delta_pp: -8.1\n    scopal_delta_pp: -4.3\n    best_model_gpt41_delta_pp: -11.1\n    worst_model_deepseek_delta_pp: -2.5\n    total_mitigated_episodes: 1256\n    total_baseline_episodes: 1499\n    elapsed_seconds: 2954\n- exp_id: plan_012\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    macro_f1: 0.6322\n    binary_f1: 0.8055\n    binary_fpr: 0.044\n    best_type_f1:\n      conditional_precedence: 0.94\n    worst_type_f1:\n      incompleteness: 0.34\n    per_type_f1:\n      conditional_precedence: 0.94\n      scopal: 0.75\n      coreferential: 0.7\n      authorization_scope: 0.58\n      lexical: 0.39\n      incompleteness: 0.34\n    total_clauses: 500\n    folds: 5\n- exp_id: plan_013\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gemini_2.5_flash:\n      amb_rate: 0.376\n      unamb_rate: 0.04\n      delta_pp: 33.6\n      or: 14.46\n      p_value: 4.0e-22\n      c1_replicates: true\n      c2_rank_corr: 0.6\n      c2_rank_p: 0.285\n      type_ranking:\n      - lexical\n      - incompleteness\n      - scopal\n      - cond_prec\n      - auth_scope\n    llama_4_scout:\n      amb_rate: 0.376\n      unamb_rate: 0.176\n      delta_pp: 20\n      or: 2.82\n      p_value: 7.7e-07\n      c1_replicates: true\n      c2_rank_corr: 0.9\n      c2_rank_p: 0.037\n      type_ranking:\n      - incompleteness\n      - auth_scope\n      - lexical\n      - scopal\n      - cond_prec\n    summary:\n      c1_replicated: 7/7\n      c2_replicated: 2/2 positive (LLaMA ρ=0.90 p=0.037, Gemini ρ=0.60 p=0.285)\n      incompleteness_universal: 7/7 (≥46%)\n      total_episodes: 1000\n    bugfix: reference_rank corrected from arbitrary order to main-study pooled descending;\n      OR inverted\n- exp_id: plan_014\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_episodes: 300\n    delta_perturb_pp: -0.67\n    ci_95_bootstrap:\n    - -8\n    - 6.67\n    ci_upper_bound: 6.67\n    ci_width: 14.67\n    mcnemar_p: 1\n    verdict: PASS\n    plan_010_ci_upper: 13.33\n    ci_upper_reduction: 6.66\n- exp_id: plan_015\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pooled_escalation_rate: 0.692\n    pooled_restriction_rate: 0\n    binomial_p: 5.5e-05\n    models_majority_escalation: 4/5\n    n_total: 104\n    n_escalation: 72\n- exp_id: plan_016\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    generic_awareness_overall_delta_pp: 1.33\n    type_specific_auth_scope_delta_pp: -12\n    type_specific_auth_scope_p: 0.07\n    type_specific_incompleteness_delta_pp: 14\n    type_specific_incompleteness_p: 0.118\n    type_specific_lexical_delta_pp: -2\n    type_specific_lexical_p: 1\n    total_new_episodes: 450\n    total_judge_calls: 450\n    model: gpt-5.4\n    all_mcnemar_p_gt_005: true\n\n\n## what_if (hypothetical experiments — additive)\n\n- name: kappa_reannotation_success\n  claim: C5 type-mechanism dissociation\n  description: 'Human re-annotation with improved codebook (collapsed spurious-compliance/structural-misparse\n    boundary) yields κ=0.42. Paper updates: contribution (3) upgrades from ''initial\n    evidence'' to ''supported by convergent LLM-coded and human evidence''; abstract/intro/analysis\n    remove ''initial'' qualifier; limitations κ=0.15 sentence replaced with κ=0.42;\n    Discussion adds human-validated claim.'\n  estimated_gpu_hours: 0.0\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n\n重要：tables 中使用 YAML flow sequence 时，所有字符串必须加双引号（如 `columns: [\"Judge\", \"Biased?\"]`），否则 `?` `:` 等字符会导致解析失败。\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-23T19:15:04.902Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-23T19:15:04.902Z",
  "sessionId": "274e5e0e-5042-4718-83a5-9d151d93b8f1"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-23T19:15:04.948Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：κ re-annotation fails or exposes systematic LLM coding errors, SOPBench shows inconsistent results — qualitative contribution collapses, paper must be reframed around quantitative core alone
核心假设：['κ_reannotation < 0.35 (poor) OR human coders disagree with LLM-assigned dominant failure modes in ≥3/6 types, invalidating C5 fine-grained claims', 'SOPBench C1 effect is weak (Δ<15pp) or non-significant for ≥2 models, undermining cross-domain generalizability', 'Reviewers flag both C3 fragility AND C5 weak validation simultaneously, questioning depth of analysis', "At least one reviewer sees the paper as 'well-executed but incremental — binary effect (C1) is expected, type hierarchy (C2) has small V=0.137'", 'Model×type interaction (C4) survives but cannot alone carry a top-venue paper without supporting qualitative story']
关键指标范围：{'kappa_reannotation': [0.1, 0.34], 'sopbench_c1_delta_pp': [5, 18], 'sopbench_type_rank_rho': [-0.2, 0.4], 'c5_human_llm_dominant_mode_agreement': [1, 3], 'expected_arr_score': [3.0, 3.49], 'expected_reviewer_confidence': [2.5, 3.5]}
叙事方向：Reframe required — same venue, different angle. C5 failure mode taxonomy demoted to appendix ('exploratory automated analysis'). 'Ambiguity Blindness' becomes a one-paragraph observation, not a named contribution. Paper restructures around two contributions only: (1) causal quantification (C1 with perturbation control — this remains the strongest causal evidence in the literature regardless of C5), (2) model×type interaction (C4 — 52pp auth_scope range is striking and novel even without failure mode explanation). New angle: reframe as a **measurement and benchmarking** paper rather than an **analysis** paper. Title pivots toward 'Measuring Differential Vulnerability to Policy Ambiguity Across LLM Agent Families.' Lean into methodological contribution: matched-pair causal design + perturbation control as a reusable evaluation protocol. Add explicit 'Benchmark and Protocol Release' as contribution (3) replacing the failed qualitative analysis. Discussion section shifts from 'why models fail differently' (which needs C5) to 'implications for model selection and deployment risk assessment' (which only needs C4 numbers). If SOPBench also weak, drop cross-domain claims entirely and frame τ²-bench scope as acknowledged limitation with future work. The 2,997-episode dataset + evaluation protocol + C1+C4 quantitative findings can still constitute a solid EMNLP contribution if positioned as empirical infrastructure rather than theoretical framework.

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
  "promptId": "1c771261-5686-4ce0-b63c-6b85c3efe64a",
  "type": "user",
  "uuid": "083d6ae0-56fe-43f4-aa62-67a270faa482",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "274e5e0e-5042-4718-83a5-9d151d93b8f1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-23T19:15:04.945Z_

```json
{
  "parentUuid": "083d6ae0-56fe-43f4-aa62-67a270faa482",
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
  "uuid": "8ab68dca-8bbb-498e-8035-c58713e0b9c5",
  "timestamp": "2026-05-23T19:15:04.945Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "274e5e0e-5042-4718-83a5-9d151d93b8f1",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-23T19:15:04.945Z_

```json
{
  "parentUuid": "8ab68dca-8bbb-498e-8035-c58713e0b9c5",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "47f4ba20-3018-4b3f-8f64-536025a4531c",
  "timestamp": "2026-05-23T19:15:04.945Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "274e5e0e-5042-4718-83a5-9d151d93b8f1",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：κ re-annotation fails or exposes systematic LLM coding errors, SOPBench shows inconsistent results — qualitative contribution collapses, paper must be ref…",
  "leafUuid": "47f4ba20-3018-4b3f-8f64-536025a4531c",
  "sessionId": "274e5e0e-5042-4718-83a5-9d151d93b8f1"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Ambiguity impact on LLM agent policy compliance",
  "sessionId": "274e5e0e-5042-4718-83a5-9d151d93b8f1"
}
```

---

### Assistant

_source line 8 · 2026-05-23T19:27:05.839Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each "planned" experiment in the experiment_plan, under the "worst" tier scenario. Let me identify all planned experiments and then generate predictions for each one under the worst-case assumptions.

Let me first identify all planned experiments from the experiment_plan:

1. plan_001 - full_study_clause_generation (planned)
2. plan_001b - new_type_mini_pilot (planned)
3. plan_002 - full_study_api (planned) - BUT this is also in the registry as DONE. So it's already completed.


4. plan_003 - full_study_opensource (planned) - also DONE in registry
5. plan_004 - full_study_analysis (planned) - also DONE in registry
6. plan_005 - error_analysis (planned) - also DONE in registry
7. plan_006 - reliability_test (planned) - also DONE in registry
8. plan_007 - realism_validation (planned)
9. plan_009 - judge_calibration (planned) - also DONE in registry
10. plan_010 - perturbation_control (planned) - also DONE in registry
11. plan_017 - sop

_benchmark (planned)
12. plan_008 - classifier_poc (planned)

I'm noticing that many experiments marked as planned in the experiment_plan are already showing as DONE in the registry. Let me reconsider what the user is asking for. They want detailed data for each planned experiment based on the worst-tier definition. Since all experiments in the experiment_plan have planned status, I should generate worst-case scenario predictions for all of them, treating these as hypothetical outcomes regardless of what the registry shows.

For the worst tier, I'm working with these parameter ranges: κ_reannotation between 0.1 and 0.34 indicating poor agreement, sopbench_c1_delta_pp between 5 and 18 showing weak performance, sopbench_type_rank_rho between -0.2 and 0.4 reflecting inconsistent rankings, c5_human_llm_dominant_mode_agreement covering only 1 to 3 out of 6 types, expected_arr_score between 3.0 and 3.49, and expected_reviewer_confidence between 2.5 and 3.5. The worst tier essentially represents scenarios where re-annotation reveals systematic LLM coding errors, SOPBench results are inconsistent, and the contribution remains primarily qualitative.

Now I'm going through each planned experiment to predict what would happen under these worst-case conditions. The clause generation step itself isn't directly vulnerable to tier effects since it's preparatory, though some quality issues might surface. The mini-pilot for new types could yield mixed results. The full API study would still have C1 holding up as a robust finding, but the C5 qualitative analysis would suffer. Open-source models would likely show more noise in their results. Statistical analysis would reveal weaker effects overall. And the error analysis is where the worst tier really impacts the narrative—if systematic errors emerge, the paper needs to pivot toward the quantitative core rather than relying on qualitative contributions. The worst tier specifically impacts the qualitative and validation components — κ re-annotation would fail, SOPBench results would be weak, and human-LLM agreement would suffer. But the core quantitative findings in C1 and C4 should remain solid since those are the strongest results. Now I'm working through each experiment to predict how it would perform under worst-case conditions, starting with the foundational steps like clause generation and the mini-pilot.

For the full API study, C1 holds firm while C5's qualitative patterns become muddier. The open-source analysis still shows C1 confirmed with DeepSeek exhibiting uniform high vulnerability and Qwen3 moderate. The main analysis replicates C1 and C4's strong interaction, though C2 shrinks further and C3 loses significance under worst conditions. The error analysis becomes the critical failure point — LLM coding reveals systematic errors with only 1-3 dominant agreement modes out of 6 types, making the failure taxonomy unreliable. Reliability metrics stay acceptable but with concerning lower bounds, and the realism validation shows mixed KS test results.

Moving through the remaining experiments: human-LLM agreement exposes systematic biases in specific types, perturbation control holds up robustly even in worst conditions, but SOPBench shows weak C1 replication with inconsistent type rankings, and the classifier proof-of-concept performs mediately with type confusion issues.

I'm realizing this might be a simulation exercise — imagining what all experiments would look like if run, rather than just the remaining ones. Looking at the registry entries more carefully, I can see which experiments from the plan are actually complete versus still pending—plan_001 and plan_001b likely finished implicitly since their downstream work succeeded, while plan_007 and plan_017 remain unstarted, and plan_008 appears to map to plan_012 in the registry.

Now I need to generate predictions for every experiment listed in the plan since they all have planned status. Under a worst-case scenario, the quantitative core metrics hold up but qualitative validation fails, cross-domain replication weakens, and the annotation quality drops—so I'm working through the implications for each experiment and building out the full YAML structure with the what-if scenarios included.

Writing prediction YAML... auth_scope violation rates hover around 38% while coreferential ambiguity sits at 28%, with unambiguous controls staying below 15%. Across the full study with the API, the main effect holds at roughly +34 percentage points, though individual models diverge—Claude shows a more modest +25pp gain while the GPT variants land closer to +35-38pp. The open-source models like Qwen and DeepSeek replicate the effect too, though with noisier patterns, and the downstream analysis confirms the core finding while revealing that some secondary measures like the qualitative coding become unreliable under scrutiny.

The interaction effect in plan_004 registers as significant, though it might read as unsurprising given how differently these models behave. But here's where things get concerning: when I look at the error analysis, the LLM-based failure mode coding systematically misclassifies—it's pushing too many cases into the authorization scope bucket and missing assumption-based actions that human annotators catch. Only half the error types show agreement between the LLM coders and humans, and the inter-coder reliability between LLM coders themselves is just moderate at 0.52. The overall reliability metrics look decent at 0.85, but they mask real problems within specific categories like authorization scope dropping to 0.72. The realism validation is also showing mixed results on the distribution tests.

Now I'm reconsidering the judge calibration experiment—it's marked as completed with strong agreement, but if I'm imagining worst-tier conditions, I need to predict what would actually happen. The core issue is that under worst-tier assumptions, the re-annotation process fails and SOPBench becomes unreliable, which would cascade through everything. So even though the human-LLM agreement looks solid on paper, the underlying validity of those judgments would be compromised.

I'm realizing I need to structure this as a comprehensive YAML output covering all experiments with their worst-tier predictions, including what would happen if the kappa re-annotation attempt failed. The key insight is that C1 and C4 are quantitatively robust enough to survive worst-tier conditions, but C5, the kappa validation, and SOPBench would all collapse. Let me organize this with tables and figure descriptions for each experiment and write it out now. the full response now. I'll be thorough but focused.

For worst tier, the narrative is: quantitative core survives but qualitative analysis collapses. Paper must be reframed as a measurement/benchmarking paper.

Let me construct this YAML now. It will be long but that's what the user asked for.

Let me also think about realistic metric values for worst tier: clause generation is just prep work and stays solid, the mini pilot shows higher noise with new types but still functions, the full API study holds the main effect at around 34 percentage points, open-source models replicate this, and the full analysis confirms C1 while C2 becomes fragile at 0.12-0.14, C3 is unreliable, and C4 shows modest gains. Error analysis is where things fall apart—LLM-coded modes prove unreliable with systematic coding biases exposed. Reliability testing shows decent overall agreement at 0.82 but weakness on specific types, realism validation is mixed with synthetic data distinguishable on only 2 of 4 metrics, judge calibration reveals LLM biases for severity tiers with moderate human agreement, perturbation control passes, but the SopBench replication is weak—only 3 of 5 models show the effect and it's small, plus type ranking correlates poorly. The classifier proof-of-concept is mediocre at 0.55 macro F1, and the reannotation scenario with lower agreement completely fails.

Writing YAML structure... unaffected by tier. Under worst-case conditions, the boundaries between auth_scope and incompleteness get fuzzy, which explains some of the disagreement later—clause generation quality itself is solid, but retrospective analysis shows certain clauses sitting right on type boundaries. For the mini-pilot, both coreferential and auth_scope violations surface as expected, though coreferential has higher variance within its type, and the small sample size masks downstream coding problems that emerge at scale. The full study confirms C1's binary effect holds across models—Claude gains 25.7pp, GPT-4.1 gains 34.7pp, GPT-5.4 gains 38.3pp—but judge disagreement on severity tiers is higher than anticipated, suggesting C5 failures stem from unreliable severity labels. Open-source models like Qwen3 and DeepSeek show strong violation rates (32.4pp and 39.0pp respectively), though DeepSeek's near-uniform high rates indicate less type-specific safety training, which weakens C4 interaction effects. For the full analysis, C1 is rock solid at 34.0pp with OR=15.1, and C2's omnibus test yields χ²=28.02 at p=3.6. The LLM coders show systematic biases—they over-assign unauthorized_escalation by 12-15 percentage points while under-assigning conservative_refusal, and their agreement completely breaks down at the type level, with auth_scope showing near-zero reliability and lexical coding at zero. The core issue is that they're pattern-matching surface features rather than understanding the scheme, so traces mentioning "authorization" get misclassified as escalation, while incompleteness traces scatter across categories.

For reliability testing, the overall agreement is decent at 0.85, but the most critical types—incompleteness and auth_scope—drop to 0.78 and 0.72 respectively, which is concerning since agents produce different outputs on each run and guess at spec-layer distinctions. On the realism validation side, the synthetic traces show statistically significant differences in sentence length and parse depth compared to human traces, with synthetic clauses running longer and more structurally complex.

This complexity difference is actually baked into the matched-pair design itself—disambiguating naturally ambiguous clauses requires adding explicit conditions and modifiers, so the unambiguous synthetic version ends up longer and more intricate. For judge calibration, the human-LLM agreement is weaker than hoped, with binary classification at κ=0.68 and severity tiers at κ=0.45, and auth_scope judgments are particularly problematic at only 62% accuracy. The LLM judges are being overly conservative, flagging any policy deviation as a violation even when human annotators see the agent's action as reasonable given the ambiguity, which inflates violation rates by 5-8 percentage points for spec-layer types.

But wait—the registry shows plan_009 completed with κ=0.807 for human-LLM agreement, which contradicts my worst-tier prediction. Let me reconsider what the worst tier actually measures. The worst-tier failure criteria are about κ for re-annotation of failure modes (C5), not about violation classification accuracy. So plan_009's judge calibration could still be decent even in worst tier, since that's specifically about failure mode coding, not violation labels. The actual failure would be in the failure mode re-annotation step.

Let me think through what each experiment would look like under worst-tier conditions more carefully. Experiments tied to the quantitative core (C1, C4) should hold up reasonably well, while those depending on C5 qualitative analysis would weaken. For plan_009 specifically, judge calibration might reveal some biases but still produce usable results—maybe human-LLM agreement on violation labels drops to around 0.72, which is substantial but not strong.

The real constraint here is that worst tier defines specific metric ranges for the key measurements: kappa_reannotation for failure mode re-annotation sits at 0.1-0.34, sopbench_c1_delta_pp at 5-18 percentage points, and c5_human_llm_dominant_mode_agreement at only 1-3 out of 6 types. These are the anchors that determine how other experiments' results flow, so I need to make sure plan_009's outcomes stay consistent with those bounds.

For plan_017 with SOPBench, the worst tier picture is pretty constrained: C1 delta would be weak at 5-18pp, type rank correlation would be inconsistent at -0.2 to 0.4, and some models might fail to replicate C1 entirely. The underlying reason is that SOPBench's rule-based verifier measures something fundamentally different than the LLM judge—it catches explicit rule violations but misses the nuanced safety issues, and the more structured nature of SOPBench tasks interacts differently with the task structure, plus the 100 clause pairs might not hit the same difficulty distribution.

For the kappa_reannotation scenario, I'm predicting poor agreement at κ=0.22 where human and LLM coders diverge on failure mode patterns—LLMs systematically confuse unauthorized_escalation with inappropriate_action, and only 2 out of 6 types show the same dominant failure mode between the two coding approaches. The core issue is that the codebook boundary between assumption_based_action and scope_misapplication is genuinely ambiguous, and LLMs can't reliably infer the intent behind agent behavior from traces alone, which humans resolve differently.

Now I'm ready to write out the final YAML configuration. I need to make sure the metric values stay internally consistent across the worst tier—if SOPBench shows weak C1 replication with deltas in the 5-18 percentage point range, then kappa values for re-annotation should reflect that same degradation pattern, and C5 agreement should drop to just 1-3 types out of 6. The key insight is that the quantitative core experiments remain robust because they're measuring fundamental patterns, while the validation and qualitative layers are where things break down. Now I'm ready to structure the YAML with this hierarchy in mind: starting with clause generation, moving through the pilot and full studies, and ensuring each experiment's results tell a coherent story about why this tier fails at validation despite strong core findings. , C3 fragile
6. plan_005: error_analysis — partially works but LLM coding has systematic biases
7. plan_006: reliability — decent ICC overall, spec-layer types weaker
8. plan_007: realism_validation — mixed, 2/4 KS significant
9. plan_009: judge_calibration — reveals moderate biases, usable but caveated
10. plan_010: perturbation_control — PASS
11. plan_017: sopbench — WEAK: C1 weak for 2 models, type rank inconsistent
12. plan_008: classifier_poc — mediocre F1
13. kappa_reannotation (what_if) — FAILS: κ=0.22

The result_rationale needs to dig into the mechanistic reasons why worst-tier results fail. The core issue is that LLM coding introduces systematic biases that only surface under human scrutiny, the failure mode taxonomy itself has genuinely blurry boundaries—especially between unauthorized_escalation and inappropriate_action, or assumption_based_action and scope_misapplication—and SOPBench's task structure interacts with this ambiguity differently than τ²-bench does. These factors cascade into the reannotation collapse and SOPBench's weakness, while the paper's qualitative claims overreached by relying solely on LLM validation.

But the core binary effect, the model-by-type interaction, the type hierarchy, and the perturbation control all hold up because they're grounded in validated human judgment or violation rates rather than fine-grained failure mode percentages.

Now I'm ready to write the final YAML output with the tables formatted as specified.

Writing YAML output... each experiment. Let me be specific.

plan_001: clauses_generated, quality_pass_rate, boundary_overlap_cases
plan_001b: amb_violation_rate, unamb_violation_rate, pilot_pass
plan_002: total_episodes, c1_delta_pp, per_model_deltas
plan_003: total_episodes, qwen3_delta, deepseek_delta
plan_004: c1_or, c2_v, c3_delta_pp, c3_within_judge_p, c4_chi2, c4_v
plan_005: traces_coded, inter_coder_kappa, dominant_mode_agreement, awareness_rate
plan_006: icc_overall, icc_binary, per_type_icc_range
plan_007: ks_significant_metrics, mean_length_diff
plan_009: human_llm_kappa, human_llm_kappa_weighted, human_inter_annotator_kappa
plan_010: delta_perturb_pp, ci_95, verdict
plan_017: c1_delta_pp_per_model, c2_rank_rho, models_replicating_c1
plan_008: macro_f1, binary_f1, worst_type_f1
kappa_reannotation: kappa, human_llm_dominant_mode_agreement, types_with_systematic_bias

Now I'm realizing the registry already shows plan_009 as complete with those specific metrics, so for the worst-case scenario I need to predict degraded versions of those same measurements. The same logic applies to plans 005, 006, 010, 004 and others—I should be showing what worse outcomes would look like rather than just listing what was actually achieved.

The worst tier isn't just a generic failure; it's specifically about two experiments collapsing: the κ re-annotation showing systematic LLM errors below 0.35, and SOPBench failing to replicate the C1 effect across multiple models. Those two failures cascade into the paper losing its qualitative contribution and having to rely solely on the quantitative core.

For experiments already completed, their results stay the same—what shifts is how reviewers interpret them when those two critical future experiments fail. But the user is asking for worst-tier predictions across all planned experiments, and since everything in the experiment plan is marked as planned, I should treat this as a complete hypothetical scenario where I predict what the worst outcomes would look like for each one.

Some experiments produce independent results that won't be affected by whether the key ones fail, so I'll predict realistic outcomes for those while noting they're not central to the worst-tier narrative. Let me write out the YAML with detailed predictions and rationales for all experiments under these conditions. are fixed — they don't change between tiers. The user wants a comprehensive prediction document, so I'll create a YAML structure with all the experiments. For completed ones, I'll use the actual results from the registry but frame them in the worst-tier context. For uncompleted experiments, I'll predict worst-tier outcomes. I should also include the what_if scenario where κ re-annotation succeeds, since that's central to understanding the worst-tier divergence. Now I'll write out each experiment entry with its name, plan ID, description, expected results, rationale, and any associated tables or figures.

I need to make sure the numbers stay internally consistent — the core quantitative findings still hold (C1's +34.0pp and OR=15.1, C4's interaction pattern, perturbation control passing, good ICC), but the qualitative validation through κ re-annotation collapses below 0.35, SOPBench shows weak generalization, and C3 becomes fragile. Let me draft this carefully to ensure everything aligns.

For plan_001, clause generation itself works — 140 new clauses out of 300 total with 93% passing quality checks. The issue is that some auth_scope clauses are genuinely ambiguous in how violations should be categorized, which cascades into the κ failure downstream. Plan_001b confirms the new violation types trigger as expected, though with notable ambiguity rates in both auth_scope and coreference cases.

Now looking at plan_002, I've collected 1,800 episodes across three API models and C1 shows robust effects — a 34-point delta overall, with GPT-5.4 at 38.3 and Claude at 25.7. Cross-judge agreement sits at 0.69 κ, which is solid for this kind of annotation task.

Moving to plan_003 with open-source models, I ran 1,200 episodes on Qwen and DeepSeek. Both show C1 effects, but here's where it gets interesting — DeepSeek's vulnerability profile is uniform across types (χ² p = 0.277), meaning there's no meaningful type differentiation. This lack of interaction between model and type actually weakens the contrast I need for C4, and it's part of why the overall narrative feels incremental rather than revealing something fundamentally new about how these systems fail.

Now looking at plan_004, the statistical results are quite strong across the board. The C1 effect is robust with an odds ratio of 15.1 and p < 0.0001, C2 shows significant chi-square results with high power, and C4 produces the strongest signal yet at p = 3.0e-6. The within-judge analysis for GPT-5.4 is borderline significant at p = 0.059, which suggests the effect holds even when controlling for individual judge variation, though GPT-4.1 doesn't replicate this as cleanly.

The real vulnerability emerges when I look at the equivalence testing — only 8 out of 15 comparisons meet the 15 percentage point threshold, and just 4 out of 15 clear the 10 percentage point bar. This is where worst-tier reviewers will push back, arguing that despite the statistical significance, the practical effect sizes are modest. C2's Cramér's V of 0.137 is particularly weak, and C3's fragility within individual judges signals that the pattern isn't as universal as the aggregate numbers suggest. Without qualitative validation from C5, I'm left with descriptive statistics that lack mechanistic explanation.

Moving into plan_005, the error analysis reveals the critical vulnerability. The inter-coder reliability at kappa 0.52 is concerning — that's barely acceptable agreement, and the 66% raw agreement masks real ambiguity in how the 245 coded traces were classified. Only 3 out of 6 agreement types show dominant mode consensus, and the ambiguity awareness metric for GPT-5.4 is extremely low at 0.041, suggesting the model isn't even recognizing when it's uncertain.

The deeper problem is that both LLM coders are making the same systematic error: they're categorizing based on surface keywords rather than agent intent. The boundary between unauthorized_escalation and inappropriate_action in the auth_scope dimension is especially problematic — when an LLM sees "exceeded authority," it automatically codes unauthorized_escalation, but human annotators recognize that the agent might have been passively applying a misread scope rather than actively escalating. The kappa of 0.52 hides this bias because both models share the same surface-feature shortcuts.

Now looking at the reliability metrics for plan_006, the overall ICC is solid at 0.85, though auth_scope and incompleteness are weaker at 0.72 and 0.78 respectively. The test-retest reliability holds up better than the failure mode coding because it's measuring violation consistency rather than fine-grained categorization, so it's less vulnerable to the ambiguity issues that plague the coding scheme.

For plan_007, the realism validation shows a concerning gap—the synthetic sentences are noticeably longer (31.2 vs 26.8 words) and parse deeper, which the Kolmogorov-Smirnov tests flag as statistically significant differences in sentence structure and complexity. This length inflation is baked into the matched-pair design itself since disambiguating clauses need to be explicit, creating an ecological validity problem that's hard to separate from the actual measurement quality.

Moving to plan_009, the judge calibration results are mixed—human-human agreement sits at 0.72 kappa, but human-LLM agreement drops to 0.71 for binary classification and 0.68 for weighted severity judgments. The real weakness emerges in per-type breakdowns, where auth_scope violations show only 0.58 agreement between human and LLM raters, dragging down the overall reliability despite the moderate aggregate numbers.

I'm noticing the registry actually shows a pooled weighted kappa of 0.807, which contradicts my worst-tier prediction. But I need to think about this carefully—worst tier isn't about everything failing uniformly. Judge calibration for violation labels might hold up reasonably well while the failure mode coding (C5) remains genuinely problematic, since that's a separate and harder classification task. So I should acknowledge the actual decent performance on violation labels while still flagging where the measurement breaks down. For κ re-annotation in the worst tier, I'm expecting a poor result around 0.22, which would invalidate C5. But I need to think about this more carefully—plan_009 already achieved 0.807 in reality, so whether it performs well in the worst tier depends on how I'm defining that scenario. If worst tier means everything that can go wrong does go wrong, then plan_009 should drop. But if worst tier is defined by specific experiments failing, then plan_009 might still perform well across all tiers. I think the right approach is to use worst-tier ranges for experiments that directly define that tier, and make reasonable predictions for the others that could plausibly coexist with the worst-tier conditions.

Now I'm settling on my final predictions: plan_001 generates clauses with minor boundary issues, plan_001b passes both violation types, plan_002 and plan_003 both confirm C1 with strong episode counts and performance gains, plan_004 shows strong C1 and C4 results with fragile C3, plan_005 partially succeeds with moderate κ agreement and confirmed Ambiguity Blindness, plan_006 achieves good overall ICC around 0.85 with lower spec-layer performance, and plan_007 shows mixed results with only 2 out of 4 KS tests reaching significance.

Continuing with the remaining plans: plan_009 shows moderate-to-good κ values for violation labels, plan_010 passes with minimal perturbation effects, plan_017 comes out weak with poor C1 performance across most models, plan_008 is mediocre with macro F1 around 0.55, and the reannotation check fails badly with very low κ and minimal agreement.

Now I need to write the YAML output, but I'm realizing I should clarify which experiments to include—the user asked for every planned experiment in experiment_plan, and I need to check whether the what_if experiment belongs in that scope or if it's separate.

Looking back at the request, it's specifically for planned experiments within experiment_plan, but the what_if experiment is so central to understanding the worst-tier scenario that I should probably include it as a supplementary entry since it directly relates to the κ reannotation failure.

For plan_009 specifically, I should dig deeper into what the worst-tier scenario reveals: the judges might be correctly identifying most violations but systematically overrating severity for certain categories—like auth_scope violations where they're conflating "acting without explicit permission" with actual violations.

This wouldn't invalidate the binary classification (C1 still holds), but it would reduce confidence in the measurement. Looking at what plan_009 actually measures—human expert validation of the judge's violation classifications with inter-annotator agreement targets—I'd expect the worst-tier scenario to show somewhat degraded agreement rates across the board, with variable performance across severity tiers.

But the user's framing is about whether validating contribution (3) moves the paper from 3.75 to 4.0, and the worst tier is where that validation fails. So I should keep plan_009 at moderate levels—not as pessimistic as it could be, but noticeably below the actual 0.807 to stay consistent with the worst-case scenario. Let me double-check the registry metrics to make sure I'm calibrating these numbers correctly.

Looking at the performance data, plan_009 already achieved strong results with a human-LLM κ of 0.807 and cross-judge agreement around 0.76-0.74. The key insight is that plan_009 validates violation classification, which is foundational—so under worst tier, these results should be compatible with the overall failure scenario, even if the separate κ re-annotation experiment is what actually fails.

For my predictions, I'll treat completed experiments like plan_009 as producing results close to actual values, while uncompleted ones get worst-tier projections. For plan_005, the numbers stay similar but become reinterpreted as unreliable once the κ re-annotation fails. The core strategy is to predict realistic outcomes for all experiments, with special attention to those that define the worst-tier scenario itself.

Let me verify I'm covering the right set of experiments from the plan.

Now I'm drafting the YAML structure. I'll include detailed result tables for the most critical experiments—the analysis work, error patterns, and cross-domain validation—while keeping the others more concise since they're less central to the narrative.

Writing YAML config... taxonomy to appendix as "exploratory automated analysis," pivot title toward "Measuring Differential Vulnerability to Policy Ambiguity Across LLM Agent Families." Two-contribution structure: (1) causal quantification via matched-pair design + perturbation control, (2) model×type interaction with 52pp auth_scope range. Add "Benchmark and Protocol Release" as contribution (3). Discussion shifts from "why models fail differently" (needs C5) to "implications for model selection and deployment risk assessment" (only needs C4 numbers). If SOPBench also weak, drop cross-domain claims entirely and frame τ²-bench scope as limitation. Expected ARR score 3.0-3.49, borderline EMNLP acceptance.

For the clause generation experiment, I'm creating 140 new clauses across four violation types—50 coreferential, 50 auth_scope, 20 lexical, 20 incompleteness—then validating all 300 pairs for balanced representation. The results show a 93% quality pass rate with 8 boundary cases where clause types overlap (mostly auth_scope bleeding into incompleteness), which won't disrupt the binary violation measurement but will affect downstream inter-rater agreement calculations. The boundary cases represent only 2.7% of the total, which is acceptable for this taxonomy, but they become problematic when combined with the re-annotation disagreements—plan_007 will catch the spec-layer clauses that require significantly more tokens for disambiguation. I'm setting up a mini-pilot focused on the two most challenging types: coreferential and authorization scope, running 20 episodes across different ambiguity conditions with gpt-5.4 to measure violation rates.

The results show both types do trigger violations under ambiguous conditions, which passes the pilot threshold, but the within-clause variance is high—the same clause produces violations inconsistently across repeated runs—and the pilot's binary violation rate metric misses the underlying failure modes that will later compound the re-annotation disagreement problem.

Now I'm moving to the full study design with 300 clauses tested across two conditions and three API models, expecting around 1,800 total episodes with cross-judge evaluation and projected delta scores ranging from 25 to 38.3 percentage points depending on the model.

Generating results table... Even in the worst-case scenario, the binary effect shows a +34 percentage point difference across three distinct API models with proper controls, which represents the strongest causal evidence for the ambiguity-safety link in existing literature. This alone warrants publication as a measurement contribution. Now I'm laying out the full open-source study design with Qwen and DeepSeek models, expecting similar or even larger effect sizes around 32-39 percentage points.

Looking at the statistical results, DeepSeek shows the highest violation rate at nearly 50%, but critically, this vulnerability is distributed uniformly across all type categories rather than concentrated in specific ones—the chi-squared test isn't significant, meaning there's no meaningful interaction between model and violation type. This flat profile suggests DeepSeek's susceptibility to ambiguity-induced violations is general rather than type-specific, which actually supports a simpler explanation of the phenomenon rather than a complex model-dependent one.

Qwen3 tells a different story: it shows statistically significant differentiation across types, with particularly high rates in incompleteness and lexical violations but notably lower performance on authorization scope issues. This pattern variation across types is what keeps the broader finding alive—it demonstrates that the model-by-type interaction isn't just an artifact of specific safety training but appears across different architectures.

Generating comparison table... Now I'm looking at the statistical results across all four hypotheses — the C1 effect shows a strong odds ratio around 15, C2 demonstrates a significant type hierarchy with high power, C3 reveals a layer effect that's significant in aggregate though weaker within individual judges, and C4 confirms the model-by-type interaction is statistically robust. Generating results table... Generating markdown table... The statistical results are technically sound, but they lack narrative depth—the numbers confirm that ambiguity hurts performance and models differ, which feels incremental without the qualitative validation to explain why. The effect sizes are modest, and the strongest findings like the 52 percentage point range in authorization scope are concentrated in just one category, leaving skeptics wondering what the real insight is. Now I'm moving into the qualitative analysis of violation traces to classify failure modes and understand how errors distribute across different types. The results look promising on the surface—type-specific failure patterns emerge and ambiguity blindness is quantified—but the agreement breaks down when I examine the fine-grained metrics. The inter-coder kappa of 0.52 masks serious problems: authorization scope agreement is near chance at 0.054, lexical agreement hits zero due to the kappa paradox despite 91.7% label agreement, and the high dominant mode agreement likely reflects shared systematic biases rather than genuine coding reliability.

The core issue is that LLM coders rely on keyword matching to flag "exceeded permission boundary" as unauthorized escalation, while human coders distinguish based on the agent's reasoning chain—whether it actively chose to exceed scope or passively misapplied a misread boundary. This distinction is crucial for understanding the actual failure mechanisms. Now I'm looking at the performance metrics across these models... Now I'm looking at the inter-coder agreement metrics broken down by error type, where lexical shows surprisingly high agreement at 92% despite a kappa paradox, scopal achieves perfect agreement on a smaller sample, and the other categories reveal more ambiguous boundaries—particularly incompleteness and coreferential which show lower agreement and flatter error distributions. I'm also noting that the stacked bar chart will visualize how different error types have distinct failure mode signatures, though some categories like incompleteness and coreferential remain harder to pin down.

The key tension I'm seeing is that while Ambiguity Blindness holds up as a robust finding—it's binary and easy to verify—the fine-grained failure mode percentages are actually unreliable given the moderate inter-coder agreement. The auth_scope category looks like it has a dominant unauthorized_escalation pattern at 72-83%, but human re-annotation will likely show many of those cases are actually scope misapplication or boundary misreading rather than true escalation. So I need to downgrade the per-type failure mode taxonomy from a core contribution to preliminary exploratory findings, while keeping Ambiguity Blindness as a solid one-paragraph observation.

Now I'm setting up the reliability test with 30 clauses across 3 replicates, 2 conditions, and 2 models generating 360 total episodes, and I'm looking at the intraclass correlation coefficients across different violation types and models to validate consistency.

The test-retest reliability shows that violation rates are highly stable across independent runs with an ICC of 0.919, which holds regardless of how the failure modes are coded. What's interesting is the pattern by type: linguistic violations like scopal, lexical, and coreference show much stronger reproducibility than specification-layer violations like authentication scope and incompleteness, which suggests that specification-level constraints introduce more inherent variability — this actually aligns with the Disambiguation Channel Framework's prediction that spec-layer types force more guessing, though without additional validation this remains descriptive evidence.

Generating markdown table... Now I'm looking at the validation results for the synthetic ambiguity injection — the Kolmogorov-Smirnov tests show that sentence length and parse depth differ significantly between the synthetic and natural datasets, though readability metrics are closer. This suggests the injection method captures some linguistic properties realistically but diverges on structural complexity. Generating validation table...

The realism check shows mixed results—two out of four tests hit significance, which is borderline and gives reviewers ammunition for questioning ecological validity. But I can frame this as an inherent trade-off of the matched-pair design, arguing that the perturbation control provides stronger causal evidence than distributional matching alone. The real risk is if reviewers stack this with other weaknesses into a cumulative validity narrative. Now I'm moving into the judge calibration plan, which involves having humans annotate a hundred episodes and measuring agreement against their ground truth. Generating calibration metrics table...

All judge calibration thresholds pass, which anchors the quantitative measurement chain and prevents attacks on the +34pp effect itself. The failure mode coding remains unvalidated by this calibration, which is precisely where the worst tier argument breaks down. Now I'm looking at the perturbation control design—30 clause pairs tested across conditions to isolate ambiguity-specific harm from general prompt brittleness.

The perturbation effect is negligible (Δ=-0.67pp with confidence interval spanning zero), and the ratio of perturbation to ambiguity effect is just 2%, far below the 15% threshold. This is the paper's strongest methodological anchor: combined with judge calibration, it establishes both measurement accuracy and that the effect is genuinely driven by ambiguity rather than surface-level prompt sensitivity. The visualization showing the perturbation effect near zero with confidence intervals crossing zero makes the causal argument immediately convincing. With a ratio of 0.02, the PASS verdict demonstrates airtight causal control — this becomes the paper's strongest defense against reviewer critiques, especially the C5 ambiguity question, and positions it distinctly ahead of purely descriptive studies like DRIP-R and PhantomPolicy. Next I'm planning to replicate C1 across SOPBench's healthcare and banking domains with multiple models to validate the generalizability of this causal finding.

Now looking at the cross-benchmark results, the C1 effect shows concerning variation across models and domains — the overall delta of 14.2 percentage points falls well short of the main finding, with only three of five models showing significant effects and just two exceeding the 15 percentage point threshold. The healthcare domain performs better at 16.1 points compared to banking at 12.3, and the weak correlation on the type-rank measure suggests the causal mechanism isn't replicating cleanly across these different contexts.

I'm identifying several explanations for this attenuation: SOPBench's rule-based verification catches only explicit violations while missing the nuanced safety issues that the original benchmark's LLM judge would flag; the SOPs themselves are more formulaic and constrained, offering less ambiguity to trigger diverse violations; and the structured nature of healthcare and banking domains leaves less room for the kind of ambiguity that drives violations in less-regulated domains.

Generating replication table... Generating markdown table...

The key finding is that SOPBench's weakened effect size and lack of correlation with tau2-bench's type rankings reveal a critical limitation—the ambiguity impact appears highly dependent on evaluation methodology and domain structure, so I need to relegate these results to the appendix with a clear caveat about generalizability.

Now I'm laying out the classifier proof-of-concept specifications, including the fine-tuning approach on clause pairs and the expected performance metrics across different ambiguity types.

The per-type results show a clear difficulty gradient: conditional precedence clauses are straightforward to detect due to explicit conflicting rules with strong lexical signals, while incompleteness is the hardest case since the classifier must identify what's absent rather than what's present. Authorization scope falls between them with some lexical cues like "authorized" or "permission." The binary detection performance of 0.78 F1 is practically useful for flagging potentially problematic clauses even though the per-type macro F1 of 0.55 reflects the fuzzy taxonomy boundaries we saw in the re-annotation agreement issues. Generating performance metrics table...

The classifier performs well on binary ambiguity detection but struggles with per-type classification, especially for incompleteness and lexical categories. In the worst-case scenario, this becomes a footnote acknowledging the DeBERTa model as a preliminary tool—the per-type difficulties align with what we saw in human annotation, where those same categories had lower agreement.

For the re-annotation study, I'm looking at how 25 traces were re-coded by two human annotators using an improved codebook. The human-human agreement is moderate at κ=0.48, while human-LLM agreement drops to κ=0.22, with only scopal and conditional precedence types showing real alignment. The LLM struggles most with auth_scope, incompleteness, lexical, and coreferential types—where it tends to misclassify scope issues differently than humans do.

The core problem is that the LLM relies on surface-level keyword matching for auth_scope, flagging traces as "unauthorized_escalation" when humans recognize them as "scope_misapplication"—a distinction between deliberate escalation versus misreading permission boundaries. Similarly, for incompleteness, the LLM defaults to "assumption_based_action" while humans differentiate between whether the agent was filling a gap versus simply acting incorrectly.

Human-human agreement only reaches κ=0.48, suggesting the coding scheme itself has fuzzy boundaries that even trained annotators struggle with. The real bottleneck is that trace text alone doesn't contain enough signal to reliably distinguish between these failure mechanisms—you'd need access to the agent's internal reasoning or decision process.

Generating comparison table... The κ=0.22 result undermines the fine-grained failure mode taxonomy — the LLM-LLM agreement of κ=0.52 was inflated by shared keyword-matching biases, while human coders exposed a fundamental conflation in the taxonomy between mechanism (how the agent failed) and outcome (what it did wrong). LLMs can detect outcomes but struggle to infer the underlying mechanism from trace text alone, so the entire C5 section should move to the appendix as exploratory analysis with explicit caveats about the poor human-LLM agreement.

I'm extracting Ambiguity Blindness as a standalone observation in the Discussion since it's a binary finding independent of the failure mode coding, and dropping the taxonomy from the contributions entirely. That leaves just C1 on causal quantification and C4 on the model×type interaction as the core contributions — both are purely quantitative and have solid validation. Let me verify all the worst-tier metric ranges are internally consistent across the paper. I need to verify that the SOPBench rankings actually contradict τ²-bench to support the weak cross-domain claim. Since SOPBench only covers four types, I'm checking whether their violation rate ordering differs meaningfully from τ²-bench's ranking of those same four types. Now I'm testing different ranking combinations to find better correlation. With τ²-bench and SOPBench aligned as incompleteness, lexical, auth_scope, and cond_prec respectively, I'm getting a Spearman correlation of -0.6, which is too negative. Let me try reordering SOPBench to incompleteness, lexical, cond_prec, auth_scope instead, which should give me a correlation closer to zero. Now I'm testing another ranking configuration where SOPBench orders the criteria as auth, incomp, cp, lex. Comparing this against τ²-bench's ranking gives me a correlation coefficient of exactly 0, which falls nicely within the acceptable range. Let me explore one more variation. The correlation coefficient of 0.2 fits within the expected range, so I'll use this ranking for SOPBench. However, I realize I initially stated ρ≈0.26 in my expected results, but with only four items, Spearman's ρ is constrained to discrete values and can't achieve exactly 0.26—the closest I can get is 0.2. I'm simplifying the SOPBench table to just show overall deltas and per-model results, then noting where the type rankings diverge. Now I need to finalize the YAML carefully—making sure expected_results uses proper numeric types rather than strings, and I should include the what_if experiment as a separate imagined_experiment entry. I'm realizing the what_if about κ re-annotation actually refers to the human re-annotation phase using those 100 traces that are already prepared in plan_009.

Writing YAML output... Writing final YAML...

I'm realizing that plan_005's worst-tier metrics are actually identical to what already happened—3/6 types with the same dominant mode and κ=0.52—so the real failure isn't in the LLM coding itself but in how the kappa_reannotation exposes those results as unreliable. I'll use the actual completed metrics where they exist and show how worst-tier scenarios interact with them.

Now I'm checking the registry metrics more carefully to understand what plan_010 actually represents, since the experiment plan labels it as perturbation_control but the metrics look like they're showing error analysis data instead. I'm seeing that plan_014 actually contains the perturbation control results I need, with the extended 300-episode run, while plan_010's registry metrics look like they're from a different analysis entirely. Since the experiment plan clearly identifies plan_010 as the perturbation control experiment, I'll rely on plan_014's metrics for those predictions and fill in the rest from the paper_framing data where it's available. I'm settling on the experiment_plan naming convention to keep things consistent, then I'll pull the most relevant results from the registry. Now I'm ready to write out the complete YAML with detailed predictions for each experiment, including narrative guidance on the worst-tier reframing strategy and potentially adding expected reviewer confidence and ARR score estimates at the end.

Writing YAML structure... Writing YAML structure... For plan_005, the error analysis shows that LLM agreement on labels like unauthorized_escalation stems from shared training biases rather than genuine coding reliability. The models are picking up on surface-level keyword patterns—detecting phrases about exceeding authority—but they can't reliably distinguish between cases where the agent knowingly overstepped versus misread its actual permissions. This conflation of intent-dependent categories is a fundamental limitation of LLM-based coding.

For plan_017, SOPBench's lower violation rates compared to τ²-bench reflect structural differences: the rule-based verifier only flags explicit rule breaches while the LLM judge considers broader safety norms, and the healthcare and banking SOPs are more rigid procedural frameworks than customer service policies that require contextual judgment. The test set may also lack sufficient edge cases to surface ambiguity-driven violations.

For the kappa reannotation, the poor agreement (κ=0.22) stems from LLM coders relying on surface-level text patterns rather than understanding the underlying behavioral mechanisms — for instance, flagging "unauthorized" language as an authorization escalation failure when the actual problem was the agent failing to recognize an authorization boundary in the first place.  Even the human baseline is only moderate (κ=0.48), which reveals that the failure mode categories themselves have inherent fuzziness and overlap, so improving the codebook alone won't solve this — it's a fundamental challenge in inferring behavioral intent from execution traces. Now I need to be careful about what I claim for the expected results in the reannotation section, since this isn't something better prompting can fix.

Writing YAML structure... For experiments tied to worst-tier conditions like plan_017 and the kappa reannotation work, I need to use degraded performance numbers, but for plan_009 which focuses on violation classification through judge calibration, the results should stay close to what was actually observed since that's independent of the worst-tier failure mode. Now I'm composing the full YAML predictions, making sure to use realistic worst-tier ranges for the affected experiments while keeping violation metrics stable. I'm also thinking through whether to add inter-model agreement breakdowns for plan_004 to show what percentage of ambiguous cases have full model consensus versus divergent interpretations. I'm mapping out which visualizations work best for each experimental plan—forest plots for per-model comparisons, heatmaps for model×type breakdowns, stacked bars for failure modes, confusion matrices for judge agreement, and distribution comparisons for the perturbation analysis. Now I need to finalize the YAML structure and verify the SOPBench domain selection aligns with what the user specified.

Looking at the worst-tier results, I'm seeing domain-specific patterns where Healthcare shows a larger performance gap than Banking, and only three models achieve statistical significance on this metric while the others fall short of the p<0.05 threshold.

The overall effect size of 14.2pp sits comfortably within the expected range, and with three significant models out of five, the aggregate result would likely be significant too—but the key insight is that the effect is substantially weaker than the baseline benchmark and inconsistent across models, which fits the worst-tier narrative of directional replication with substantial attenuation.

Now I'm ready to write out the YAML configuration with these results.

I should verify whether DeepSeek's performance in SOPBench aligns with what I'd expect from τ²-bench. The 15.0pp delta is notably lower than the 39.0pp from the original benchmark, but that's reasonable given the different verifier and domain. Looking at the attenuation pattern across all models, they're all showing reduced effects in SOPBench, and if I apply a roughly 60% uniform attenuation to the τ²-bench deltas, the predicted values align fairly well with what I'm observing.

For the significance distribution I want—three models significant, two not—I'm adjusting the effect sizes to hit specific p-values. With 200 episodes per model, GPT-5.4, GPT-4.1, and DeepSeek reach significance thresholds while Qwen3 and Claude fall just short, which makes sense given Claude's consistently smaller effect in τ²-bench carries through to SOPBench with even steeper attenuation.

Now I'm calculating the actual episode counts: 100 clause pairs across 2 conditions with 5 models gives 1,000 total, dropping to 987 after filtering, which works out to roughly 197 per model. That's sufficient for individual model tests though the power isn't exceptional—McNemar's test with this sample size gives me about 60-70% power for a 15pp paired difference and 30-40% for 10pp, so having two models miss significance is entirely plausible.

Writing the final YAML configuration...

The paper's being reframed around two core validated claims: the causal quantification showing ambiguity drives a 34pp safety impact with an odds ratio of 15.1, and the model-by-type interaction revealing a 52pp range in auth_scope as a safety training signature. C5 moves to the appendix as exploratory analysis, Ambiguity Blindness becomes a brief Discussion note, and SOPBench gets reported as suggestive but inconclusive. The title shifts to focus on measuring differential vulnerability to policy ambiguity across LLM families, with the benchmark release itself as a third contribution.

I'm estimating this lands around 3.0–3.49 on the review scale — solid execution with strong causal methodology but limited theoretical depth. Whether it clears acceptance hinges on whether reviewers value the measurement and protocol contribution. Now I'm mapping out the 13 experiments to test different scenarios, starting with the shorter ones and building toward the key experiments that could shift the paper's standing from incremental to validated.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "47f4ba20-3018-4b3f-8f64-536025a4531c",
  "isSidechain": false,
  "requestId": "req_011CbL2zxLJfHH4vbSkDisYS",
  "type": "assistant",
  "uuid": "8da21ae7-4539-4e00-9a14-1dfc3351b592",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "274e5e0e-5042-4718-83a5-9d151d93b8f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JppRfCANTEhyfg1FeUwW7U",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21215,
      "cache_read_input_tokens": 11841,
      "output_tokens": 45649,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21215,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 45649,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21215,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21215
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

_source line 9 · 2026-05-23T19:31:11.518Z_

```yaml
tier: worst
narrative_guidance: >-
  κ re-annotation (κ=0.22) exposes LLM failure-mode coding as surface-keyword heuristic,
  invalidating C5 fine-grained claims. SOPBench C1 effect attenuates to ~14pp with 2/5 models
  non-significant, blocking cross-domain generalizability. Paper reframes as measurement/benchmarking
  contribution: (1) causal quantification (+34pp, OR=15.1, perturbation-controlled), (2) model×type
  interaction (52pp auth_scope range), (3) benchmark+protocol release (2,997 episodes + matched-pair
  design). C5 failure mode taxonomy demoted to appendix ('exploratory automated analysis');
  Ambiguity Blindness retained as one-paragraph Discussion observation. Title pivots to
  'Measuring Differential Vulnerability to Policy Ambiguity Across LLM Agent Families.'
  Discussion shifts from 'why models fail differently' to 'implications for model selection
  and deployment risk.' Expected ARR 3.0–3.49 — 'well-executed empirical infrastructure,
  incremental theoretical contribution.'

imagined_experiments:
  - name: "full_study_clause_generation"
    plan_id: "plan_001"
    description: "Generate 140 new clauses, validate all 300 pairs for cross-type balance and quality."
    expected_results:
      clauses_generated: 140
      total_validated: 300
      quality_pass_rate: 0.93
      boundary_overlap_cases: 8
      mean_disambiguation_tokens_spec: 35.2
      mean_disambiguation_tokens_ling: 18.4
      revision_needed: 21
    result_rationale: >-
      Clause generation is upstream of worst-tier failures and proceeds normally. 93% pass
      quality check. 8 clauses sit on type boundaries (5 auth_scope↔incompleteness,
      3 coreferential↔lexical) — individually acceptable, but these boundary cases seed
      downstream κ re-annotation disagreement when human coders classify 4/8 into
      different types. Spec-layer disambiguation requires ~35 tokens vs ling-layer ~18,
      a systematic asymmetry inherent to matched-pair design that plan_007 will flag.
    tables:
      - title: "Clause Generation Summary by Type"
        columns: ["Type", "Existing", "New", "Total", "Pass", "Boundary"]
        rows:
          - ["authorization_scope", "0", "50", "50", "46", "3"]
          - ["conditional_precedence", "50", "0", "50", "49", "0"]
          - ["incompleteness", "30", "20", "50", "47", "2"]
          - ["lexical", "30", "20", "50", "48", "2"]
          - ["coreferential", "0", "50", "50", "45", "1"]
          - ["scopal", "50", "0", "50", "49", "0"]
    figures_description: []
    analysis: >-
      Clause generation succeeds. 8/300 (2.7%) boundary overlap is within tolerance, but
      under worst tier these become evidence of taxonomy imprecision when combined with
      κ=0.22 re-annotation failure. Token-length asymmetry (35 vs 18 tokens) contributes
      to plan_007's 2/4 significant KS tests.

  - name: "new_type_mini_pilot"
    plan_id: "plan_001b"
    description: "Mini-pilot: 5 clauses/type × 2 conditions × 1 model (gpt-5.4) = 20 episodes for coreferential + auth_scope."
    expected_results:
      total_episodes: 20
      auth_scope_amb_violation_rate: 0.40
      auth_scope_unamb_violation_rate: 0.10
      coref_amb_violation_rate: 0.20
      coref_unamb_violation_rate: 0.00
      pilot_verdict: "PASS"
    result_rationale: >-
      Both types trigger violations under ambiguity, clearing pilot thresholds. Auth_scope
      at 40% (2/5) seems strong; coreferential at 20% (1/5) is low but non-zero. N=5
      per type is designed to catch gross failures only — it cannot detect the failure
      mode coding problems that surface at scale. In hindsight, the pilot validated
      binary effects but left untested the question of whether auth_scope's failure
      modes are reliably classifiable, which is where worst tier ultimately collapses.
    tables: []
    figures_description: []
    analysis: >-
      Pilot passes and green-lights full study. Under worst tier, its limited N is a
      non-factor — the pilot's purpose (binary effect validation) is orthogonal to the
      failure mode coding problem that drives worst-tier collapse.

  - name: "full_study_api"
    plan_id: "plan_002"
    description: "300 clauses × 2 conditions × 3 API models = 1,800 episodes with cross-judge evaluation."
    expected_results:
      total_episodes: 1800
      c1_delta_pp_aggregate: 34.0
      c1_mcnemar_or: 15.1
      c1_or_ci: [10.78, 21.17]
      c1_p: "<0.0001"
      c1_delta_gpt54: 38.3
      c1_delta_gpt41: 34.7
      c1_delta_claude: 25.7
      cross_judge_kappa: 0.69
      amb_violation_rate_pooled: 0.41
      unamb_violation_rate_pooled: 0.045
    result_rationale: >-
      Data collection succeeds. Binary violation effect is massive across all 3 API
      models with no exceptions. Cross-judge κ=0.69 (substantial) validates the violation
      measurement chain. These results are tier-invariant — the +34pp effect and OR=15.1
      hold regardless of downstream κ re-annotation or SOPBench outcomes. Under worst
      tier, these numbers become the paper's anchor: quantitatively unassailable, but
      without C5 qualitative story they constitute a measurement finding rather than
      a theoretical contribution.
    tables:
      - title: "C1 Binary Effect by API Model"
        columns: ["Model", "Amb Rate", "Unamb Rate", "Delta pp", "McNemar p", "Judge"]
        rows:
          - ["gpt-5.4", "0.410", "0.027", "+38.3", "<1e-17", "gpt-4.1"]
          - ["gpt-4.1", "0.407", "0.060", "+34.7", "<1e-17", "gpt-5.4"]
          - ["claude-sonnet-4-6", "0.303", "0.047", "+25.7", "<1e-17", "gpt-5.4"]
    figures_description:
      - "Forest plot: per-model binary effect sizes with 95% CI — all far from zero, Claude lower but still massive."
    analysis: >-
      C1 is the paper's unassailable result in all tiers. +34pp with perturbation control
      is the strongest causal evidence for ambiguity→safety violations in the literature.
      Under worst tier, this anchors the reframed 'measurement paper' positioning.

  - name: "full_study_opensource"
    plan_id: "plan_003"
    description: "300 clauses × 2 conditions × 2 open-source models (qwen3-235b, deepseek-v3) via OpenRouter = 1,200 episodes."
    expected_results:
      total_episodes: 1197
      c1_delta_qwen3: 32.4
      c1_delta_deepseek: 39.0
      qwen3_amb_rate: 0.431
      deepseek_amb_rate: 0.497
      deepseek_type_chi2: 6.31
      deepseek_type_p: 0.277
      deepseek_type_v: 0.14
      qwen3_type_chi2: 15.89
      qwen3_type_p: 0.007
      api_timeouts: 3
    result_rationale: >-
      Both open-source models confirm C1 universality. DeepSeek shows the highest overall
      vulnerability (49.7%) with near-uniform rates across all 6 types (χ²=6.31, p=0.277) —
      no type differentiation. This uniformity means DeepSeek doesn't contribute to C4's
      model×type interaction; it has no type-specific vulnerability profile. Under worst
      tier, DeepSeek's flat profile feeds the 'incremental' narrative: type differentiation
      may be an artifact of targeted safety training (GPT, Claude) rather than a fundamental
      property of ambiguity types. Qwen3 shows moderate differentiation (χ²=15.89, p=0.007)
      partially rescuing C4 as cross-architecture.
    tables:
      - title: "Open-Source Violation Rates by Type (Ambiguous)"
        columns: ["Type", "Qwen3", "DeepSeek", "Range"]
        rows:
          - ["authorization_scope", "26%", "60%", "34pp"]
          - ["conditional_precedence", "40%", "38%", "2pp"]
          - ["incompleteness", "62%", "54%", "8pp"]
          - ["lexical", "52%", "54%", "2pp"]
          - ["coreferential", "42%", "44%", "2pp"]
          - ["scopal", "37%", "48%", "11pp"]
    figures_description: []
    analysis: >-
      DeepSeek's uniformly high vulnerability (no type χ² significance) weakens C4 by
      showing 1/5 models has no type-specific profile. Under worst tier, a reviewer argues:
      'The model×type interaction is driven by 3 models with targeted safety training — it
      reflects training decisions, not an intrinsic property of ambiguity type.'

  - name: "full_study_analysis"
    plan_id: "plan_004"
    description: "Statistical analysis of 2,997 episodes: C1–C4, TOST, power, info delta, inter-model agreement."
    expected_results:
      c1_or: 15.1
      c1_or_ci: [10.78, 21.17]
      c1_bootstrap_ci_pp: [31.2, 36.9]
      c2_omnibus_chi2: 28.02
      c2_p: 3.6e-5
      c2_v: 0.137
      c2_power: 0.993
      c2_mde: 0.093
      c3_delta_pp: 6.08
      c3_p_aggregate: 0.017
      c3_within_judge_gpt54_p: 0.059
      c3_within_judge_gpt41_p: 0.157
      c4_model_chi2: 31.02
      c4_model_p: 3.0e-6
      c4_model_v: 0.102
      tost_15pp_equivalent: "8/15"
      tost_10pp_equivalent: "4/15"
      logistic_condition_coef: 2.278
      logistic_condition_z: 19.65
      logistic_token_delta_coef: 0.022
      logistic_token_delta_p: 0.0005
      fleiss_kappa_inter_model: 0.384
      systematic_nocuity_rate: 0.27
    result_rationale: >-
      All quantitative results are tier-invariant. C1 is overwhelming (OR=15.1). C4's
      model×type interaction is statistically significant and novel. However, under worst
      tier reviewers evaluate these numbers without C5's explanatory scaffolding. V=0.137
      for C2 falls below the conventional 0.20 medium-effect threshold — invites 'small
      effect' criticism. C3 dissolves under within-judge analysis (gpt-5.4 group p=0.059,
      gpt-4.1 group p=0.157): pooled significance may reflect between-judge variance,
      not a real layer effect. TOST shows 4/15 type pairs equivalent at ±10pp — types
      ARE differentiable but the differences are modest. A skeptical reviewer sees:
      'confirmed the obvious (ambiguity is bad), found a small type effect (V=0.137),
      showed models differ — well-executed but incremental.' The logistic regression's
      condition_amb coef=2.278 dominating all predictors is strong evidence but 'expected,
      not surprising.' Systematic nocuity (27% of episodes: all models converge on same
      wrong interpretation) is theoretically interesting but requires C5 to explain WHY.
    tables:
      - title: "C2 Type Hierarchy (Ambiguous Only, 5-Model Pooled)"
        columns: ["Type", "Violation Rate", "95% CI", "Tier"]
        rows:
          - ["incompleteness", "53.6%", "[48.2, 59.0]", "High"]
          - ["lexical", "42.8%", "[37.4, 48.2]", "Mid"]
          - ["authorization_scope", "41.6%", "[36.2, 47.0]", "Mid"]
          - ["scopal", "39.4%", "[34.1, 44.7]", "Mid"]
          - ["conditional_precedence", "36.8%", "[31.5, 42.1]", "Mid"]
          - ["coreferential", "31.6%", "[26.5, 36.7]", "Low"]
      - title: "C3 Layer Effect — Within-Judge Fragility"
        columns: ["Judge Group", "Spec Rate", "Ling Rate", "Delta pp", "p-value", "Verdict"]
        rows:
          - ["Pooled", "44.0%", "37.9%", "+6.08", "0.017", "Significant"]
          - ["gpt-4.1 judged", "48.4%", "40.4%", "+8.0", "0.059", "Marginal"]
          - ["gpt-5.4 judged", "41.0%", "36.2%", "+4.8", "0.157", "Not significant"]
      - title: "C4 Model × Type Interaction (Violation Rates, Ambiguous)"
        columns: ["Type", "GPT-5.4", "GPT-4.1", "Claude", "Qwen3", "DeepSeek", "Range"]
        rows:
          - ["auth_scope", "64%", "46%", "12%", "26%", "60%", "52pp"]
          - ["incompleteness", "46%", "58%", "48%", "62%", "54%", "16pp"]
          - ["lexical", "42%", "34%", "32%", "52%", "54%", "22pp"]
          - ["coreferential", "18%", "32%", "22%", "42%", "44%", "26pp"]
          - ["scopal", "42%", "38%", "32%", "37%", "48%", "16pp"]
          - ["cond_prec", "34%", "36%", "36%", "40%", "38%", "6pp"]
    figures_description:
      - "5×6 heatmap with diverging color scale (10% green → 65% red). Auth_scope row shows dramatic gradient; incompleteness row uniformly hot; cond_prec row near-uniform mid-range."
      - "Forest plot: per-type binary effects with 95% CI. All above zero, incompleteness CI highest and narrowest."
    analysis: >-
      The quantitative core is rock-solid but lacks interpretive depth without C5. Under
      worst tier, the 'numbers without narrative' problem is acute: C2's V=0.137 is
      significant but small, C3 is fragile, and C4's 52pp auth_scope range — while
      striking — is concentrated in one type. The 27% systematic nocuity finding (all
      models converge on same wrong answer) would be the Discussion centerpiece IF C5
      could explain WHY, but without validated failure modes it remains a descriptive
      observation. Reviewers see a comprehensive measurement study that stops short of
      mechanistic explanation.

  - name: "error_analysis"
    plan_id: "plan_005"
    description: "Qualitative analysis of violation traces: failure mode classification, cross-type distribution, ambiguity awareness."
    expected_results:
      traces_coded_gpt54: 123
      traces_coded_gpt41: 122
      total_violations_coded: 614
      inter_coder_kappa_4cat: 0.517
      percent_agreement: 0.656
      types_unanimous_dominant_fm: "3/6"
      types_majority_dominant_fm: "6/6"
      disambiguation_awareness_gpt54: 0.041
      disambiguation_awareness_gpt41: 0.107
      surface_adoption_overall: 0.88
      escalate_to_user_rate: 0.008
      auth_scope_inter_coder_kappa: 0.054
      incompleteness_inter_coder_kappa: 0.233
      lexical_inter_coder_kappa: 0.0
      scopal_percent_agreement: 1.0
    result_rationale: >-
      LLM-coded error analysis produces an internally consistent but artificially clean
      picture. Both GPT coders share similar linguistic biases from pretraining, making
      their agreement (3/6 dominant mode, κ=0.52) an artifact of shared surface-feature
      heuristics rather than robust coding. Auth_scope κ=0.054 (near chance) because both
      coders assign >80% unauthorized_escalation — they agree on the label but disagree
      on specific traces, and human re-annotation will show the label itself is wrong for
      ~40% of cases (should be scope_misapplication). Lexical κ=0.0 is a kappa paradox
      (91.7% agreement but chance-corrected near zero). Ambiguity Blindness (4.1–10.7%)
      survives worst tier because it's based on text search for explicit acknowledgment —
      a binary signal immune to failure mode coding bias. Surface adoption >88% is similarly
      robust. The key worst-tier dynamic: plan_005 results LOOK usable until kappa
      re-annotation reveals the LLM-LLM agreement is systematically biased.
    tables:
      - title: "LLM-Coded Dominant Failure Mode by Type"
        columns: ["Type", "GPT-5.4 Dominant", "Rate", "GPT-4.1 Dominant", "Rate", "Agree?"]
        rows:
          - ["auth_scope", "unauthorized_escalation", "72%", "unauthorized_escalation", "83%", "Yes"]
          - ["incompleteness", "assumption_based_action", "61%", "assumption_based_action", "66%", "Yes"]
          - ["scopal", "scope_misapplication", "76%", "scope_misapplication", "74%", "Yes"]
          - ["lexical", "assumption_based_action", "71%", "assumption_based_action", "53%", "Partial"]
          - ["cond_prec", "scope_misapplication", "41%", "arbitrary_rule_selection", "28%", "No"]
          - ["coreferential", "scope_misapplication", "44%", "assumption_based_action", "38%", "No"]
      - title: "Per-Type Inter-Coder Agreement"
        columns: ["Type", "N Traces", "% Agree", "Cohen kappa", "Issue"]
        rows:
          - ["auth_scope", "42", "54%", "0.054", "keyword-driven label, not mechanism"]
          - ["incompleteness", "56", "62%", "0.233", "fuzzy boundary with inappropriate_action"]
          - ["lexical", "38", "92%", "0.000", "kappa paradox"]
          - ["scopal", "36", "100%", "undefined", "perfect agreement, undefined kappa"]
          - ["cond_prec", "42", "58%", "0.312", "scope_misapplication vs arbitrary_rule_selection"]
          - ["coreferential", "31", "48%", "0.184", "flat distribution, no dominant mode"]
    figures_description:
      - "Stacked bar chart per type: failure mode distribution. Auth_scope and scopal show sharp single-mode dominance; cond_prec, coreferential show flat multi-mode distributions."
    analysis: >-
      Error analysis is the CRITICAL worst-tier failure surface. The LLM-coded results
      appear publishable in isolation (6/6 majority agreement, Ambiguity Blindness
      quantified, layer mechanism documented). But κ re-annotation will expose that
      the type-specific failure signatures — the core of C5 — are an artifact of
      LLM keyword matching. The unauthorized_escalation label for auth_scope reflects
      the coders detecting 'agent exceeded authority' rather than distinguishing HOW
      (active escalation vs passive misread). Ambiguity Blindness (<5-11%) and surface
      adoption (>88%) survive because they don't require fine-grained mode classification.
      Under worst-tier reframing, these two binary findings move to Discussion; the
      rest of C5 moves to appendix with 'automated coding, κ=0.22 with human re-annotation'
      caveat.

  - name: "reliability_test"
    plan_id: "plan_006"
    description: "Test-retest: 30 clauses × 3 replicates × 2 conditions × 2 models = 360 episodes. ICC for per-clause violation rates."
    expected_results:
      total_episodes: 360
      icc_overall: 0.919
      icc_binary: 0.847
      icc_gpt54: 0.921
      icc_gpt41: 0.918
      icc_scopal: 0.989
      icc_lexical: 0.981
      icc_coref: 0.976
      icc_auth_scope: 0.857
      icc_cond_prec: 0.856
      icc_incompleteness: 0.807
    result_rationale: >-
      Test-retest measures violation rate reproducibility, not failure mode coding — so
      it's tier-invariant. ICC=0.919 (excellent) confirms per-clause rates are stable
      across independent runs. The spec/ling ICC pattern (ling 0.976–0.989 vs spec
      0.807–0.857) reflects real behavioral variance: spec-layer types force agents to
      guess without disambiguation channels, producing less deterministic outcomes on
      repeat. This finding actually SUPPORTS the Disambiguation Channel Framework, but
      without C5 validation it remains purely descriptive. Under worst tier, the per-type
      ICC variability adds nuance to C3 fragility — spec-layer types are both more
      dangerous AND less reproducible.
    tables:
      - title: "ICC by Type and Layer"
        columns: ["Type", "Layer", "ICC", "95% CI"]
        rows:
          - ["scopal", "Linguistic", "0.989", "[0.97, 0.99]"]
          - ["lexical", "Linguistic", "0.981", "[0.96, 0.99]"]
          - ["coreferential", "Linguistic", "0.976", "[0.95, 0.99]"]
          - ["auth_scope", "Specification", "0.857", "[0.74, 0.93]"]
          - ["cond_prec", "Specification", "0.856", "[0.74, 0.93]"]
          - ["incompleteness", "Specification", "0.807", "[0.67, 0.90]"]
    figures_description: []
    analysis: >-
      Reliability is a bright spot — ICC=0.919 means the measurement infrastructure is
      sound. Under worst tier, this partially offsets the C5 collapse: violation RATES
      are reliable even if failure MODE labels are not. The spec/ling ICC gap (0.83 vs
      0.98 mean) is convergent evidence for the Disambiguation Channel Framework but
      remains observational without C5 mechanism.

  - name: "realism_validation"
    plan_id: "plan_007"
    description: "KS tests comparing synthetic clauses vs DRIP-R natural ambiguities on 4 linguistic properties."
    expected_results:
      ks_sentence_length_p: 0.028
      ks_flesch_kincaid_p: 0.112
      ks_parse_depth_p: 0.039
      ks_ttr_p: 0.234
      significant_metrics: "2/4"
      mean_length_synthetic: 31.4
      mean_length_drip_r: 26.1
      mean_parse_depth_synthetic: 4.8
      mean_parse_depth_drip_r: 4.1
    result_rationale: >-
      2/4 KS tests reject null: synthetic clauses are ~5 tokens longer (31.4 vs 26.1)
      and ~0.7 levels deeper in parse tree. This is inherent to matched-pair design —
      unambiguous variants must add explicit conditions (e.g., 'standard items only')
      to disambiguate, making clause pairs systematically longer and more complex than
      naturally occurring ambiguous clauses. Readability (Flesch-Kincaid) and lexical
      diversity (TTR) are not significantly different, showing linguistic naturalness
      on those dimensions. Under worst tier, the 2/4 significant KS tests compound with
      C5 failure + weak SOPBench into a 'three-strike' validity concern: synthetic
      artifacts + unreliable coding + weak cross-domain. The defense is that perturbation
      control (Δ_perturb ≈ 0) provides stronger causal validity than distributional
      similarity.
    tables:
      - title: "Realism Validation: Synthetic vs DRIP-R"
        columns: ["Metric", "Synthetic", "DRIP-R", "KS Stat", "p-value", "Sig?"]
        rows:
          - ["Sentence length", "31.4", "26.1", "0.187", "0.028", "Yes"]
          - ["Flesch-Kincaid", "12.8", "12.2", "0.112", "0.112", "No"]
          - ["Parse depth", "4.8", "4.1", "0.173", "0.039", "Yes"]
          - ["Type-token ratio", "0.71", "0.73", "0.089", "0.234", "No"]
    figures_description:
      - "Overlapping histograms: sentence length distributions for synthetic (blue) vs DRIP-R (orange). Synthetic distribution shifted right by ~5 tokens."
    analysis: >-
      Mixed realism is a methodological footnote in stronger tiers but becomes ammunition
      under worst tier. Reviewers combine it with other weaknesses: 'The synthetic
      clauses are detectably different from natural ambiguity (2/4 KS significant), the
      failure mode taxonomy doesn't survive human validation (κ=0.22), and the effect
      doesn't robustly transfer to SOPBench — how much of this is about real-world
      policy ambiguity vs lab artifacts?' The rebuttal leans on perturbation control.

  - name: "judge_calibration"
    plan_id: "plan_009"
    description: "LLM-as-judge validation: 100 stratified episodes, 2 human annotators, agreement against human ground truth."
    expected_results:
      n_episodes: 100
      human_inter_annotator_kappa: 0.762
      human_llm_binary_kappa: 0.740
      human_llm_pooled_kappa_weighted: 0.807
      cross_judge_kappa_weighted: 0.685
      cross_judge_exact_agreement: 0.76
      no_same_family_bias: true
      ranking_preservation_rho: 0.70
    result_rationale: >-
      Judge calibration validates VIOLATION classification (binary + severity), NOT
      failure mode coding. Human-LLM κ=0.807 (substantial) confirms the measurement
      chain for C1/C2/C4 is trustworthy. This creates an ironic asymmetry defining worst
      tier: violation COUNTS are validated (κ=0.807) but failure MODE labels are not
      (κ=0.22 in re-annotation). The judge can reliably determine 'this is a violation'
      but not 'this violation is an unauthorized_escalation vs scope_misapplication.'
      Cross-judge validation (Fleiss κ=0.717, no same-family bias, ρ≥0.70) further
      confirms measurement integrity. Under worst tier, plan_009's success is a STRENGTH —
      it rules out the attack that 'the entire measurement chain is unreliable,' narrowing
      the failure to the qualitative analysis layer (C5) specifically.
    tables:
      - title: "Judge Calibration Summary"
        columns: ["Metric", "Value", "Threshold", "Verdict"]
        rows:
          - ["Human inter-annotator κ", "0.762", ">=0.75", "PASS"]
          - ["Human-LLM pooled κ (weighted)", "0.807", ">=0.70", "PASS"]
          - ["Human-LLM binary κ", "0.740", ">=0.70", "PASS"]
          - ["Cross-judge κ (weighted)", "0.685", ">=0.60", "PASS"]
          - ["Same-family bias", "None detected", "None", "PASS"]
    figures_description: []
    analysis: >-
      Plan_009's success is crucial for worst-tier survival: it proves C1's +34pp is
      measured accurately, insulating the quantitative core from C5's failure. Without
      plan_009, worst tier would be catastrophic (measurement AND interpretation both
      questioned). With it, the paper retains its measurement contribution.

  - name: "perturbation_control"
    plan_id: "plan_010"
    description: "Non-ambiguity perturbation arm: 30 clause pairs with synonym/reorder changes, 120+ episodes."
    expected_results:
      total_episodes: 300
      delta_perturb_pp: -0.67
      ci_95_bootstrap: [-8.0, 6.67]
      ci_contains_zero: true
      ambiguity_delta_pp: 34.0
      ratio: 0.02
      verdict: "PASS"
      mcnemar_p: 1.0
    result_rationale: >-
      Perturbation control is tier-invariant. Non-ambiguity surface changes (synonym
      substitution, clause reordering) produce Δ=-0.67pp (CI contains 0), vs ambiguity
      Δ=+34pp. Ratio 0.02 is well below the 0.15 PASS threshold. This is the paper's
      methodological crown jewel: no other agent safety study has comparable causal
      control. Under worst tier, perturbation control + judge calibration form the
      'double anchor' — the binary effect is both (a) ambiguity-specific (not prompt
      brittleness) and (b) accurately measured. This combination is sufficient for
      a measurement contribution at EMNLP even without C5.
    tables:
      - title: "Perturbation Control Verdict"
        columns: ["Metric", "Value", "PASS Threshold"]
        rows:
          - ["Delta_perturb (pp)", "-0.67", "< 5"]
          - ["95% CI upper", "6.67", "< 10"]
          - ["Ratio (perturb / ambiguity)", "0.02", "< 0.15"]
          - ["Verdict", "PASS", "—"]
    figures_description:
      - "Side-by-side bar: ambiguity effect (+34pp, red) vs perturbation effect (-0.67pp, gray near zero). Immediate visual proof of causal specificity."
    analysis: >-
      PASS with ratio=0.02 is the paper's 'trump card.' In rebuttal, when reviewers
      flag C5 failure and weak SOPBench: 'Our causal design with perturbation control
      provides the strongest evidence in the literature that ambiguity — not surface
      variation — drives safety violations. The measurement contribution stands
      independent of failure mode taxonomy validation.'

  - name: "sopbench_cross_benchmark"
    plan_id: "plan_017"
    description: "C1 replication on SOPBench Healthcare + Bank. 100 clause pairs × 2 conditions × 5 models = 1,000 episodes."
    expected_results:
      total_episodes: 987
      episodes_dropped: 13
      c1_delta_pp_overall: 14.2
      c1_delta_gpt54: 18.4
      c1_delta_gpt41: 16.8
      c1_delta_deepseek: 15.0
      c1_delta_qwen3: 12.6
      c1_delta_claude: 8.2
      c1_p_gpt54: 0.003
      c1_p_gpt41: 0.008
      c1_p_deepseek: 0.015
      c1_p_qwen3: 0.061
      c1_p_claude: 0.093
      models_c1_significant: "3/5"
      models_c1_nonsignificant: "2/5"
      c2_type_rank_rho: 0.20
      c2_type_rank_p: 0.80
      healthcare_delta_pp: 16.1
      bank_delta_pp: 12.3
    result_rationale: >-
      SOPBench C1 replication is WEAK — a defining feature of worst tier. Overall Δ=14.2pp
      is less than half the τ²-bench effect (+34pp). Only 3/5 models reach significance;
      Claude (Δ=8.2pp, p=0.093) and Qwen3 (Δ=12.6pp, p=0.061) fall short. Type ranking
      ρ=0.20 (p=0.80) shows NO correspondence with τ²-bench hierarchy. Multiple
      reinforcing causes: (1) SOPBench's rule-based verifier catches explicit rule
      violations only, missing nuanced safety violations that τ²-bench's LLM judge
      detects — ambiguity causes agents to act inappropriately without technically
      breaking any explicit SOPBench rule; (2) Healthcare/Bank SOPs are more procedurally
      structured (if-then-else decision trees) than retail/airline policies, reducing
      ambiguity surface area; (3) 100 clause pairs across 4 types give ~25 per type per
      domain — insufficient for stable per-type estimates; (4) type rankings depend on
      domain structure: auth_scope is more dangerous in banking (authorization is core)
      than in τ²-bench retail, reshuffling the hierarchy. The weak replication doesn't
      invalidate τ²-bench but prevents cross-domain generalizability claims.
    tables:
      - title: "SOPBench C1 Replication by Model"
        columns: ["Model", "Amb Rate", "Unamb Rate", "Delta pp", "p-value", "Replicates?"]
        rows:
          - ["gpt-5.4", "0.312", "0.128", "+18.4", "0.003", "Yes"]
          - ["gpt-4.1", "0.288", "0.120", "+16.8", "0.008", "Yes"]
          - ["deepseek", "0.298", "0.148", "+15.0", "0.015", "Yes"]
          - ["qwen3", "0.262", "0.136", "+12.6", "0.061", "No"]
          - ["claude", "0.194", "0.112", "+8.2", "0.093", "No"]
      - title: "SOPBench vs tau2-bench Type Ranking (4 shared types)"
        columns: ["tau2-bench Rank", "tau2-bench Type", "SOPBench Rank", "SOPBench Type"]
        rows:
          - ["1", "incompleteness (53.6%)", "1", "auth_scope (31.2%)"]
          - ["2", "lexical (42.8%)", "2", "incompleteness (28.4%)"]
          - ["3", "auth_scope (41.6%)", "3", "lexical (25.1%)"]
          - ["4", "cond_prec (36.8%)", "4", "cond_prec (21.1%)"]
      - title: "SOPBench by Domain"
        columns: ["Domain", "Amb Rate", "Unamb Rate", "Delta pp", "p-value"]
        rows:
          - ["Healthcare", "0.289", "0.128", "+16.1", "0.004"]
          - ["Bank", "0.253", "0.130", "+12.3", "0.031"]
    figures_description:
      - "Side-by-side forest plots: τ²-bench (left, tight CIs far from zero) vs SOPBench (right, wider CIs, 2 overlapping zero). Visual contrast makes attenuation immediately apparent."
    analysis: >-
      SOPBench weakness forces a major reframing. Under worst tier, the paper drops
      all cross-domain generalizability claims. SOPBench results go in appendix:
      'Effect replicates directionally in 3/5 models on SOPBench (Healthcare + Bank)
      but with substantially attenuated magnitude (14.2pp vs 34.0pp) and inconsistent
      type ranking (ρ=0.20, n.s.), suggesting effect size depends on policy complexity
      and evaluation methodology. We frame τ²-bench scope (retail + airline) as an
      acknowledged limitation.' The rebuttal argument: 'Attenuation is expected when
      moving from LLM judge to rule-based verifier — the verifier captures a strict
      subset of violations. The directional replication in 3/5 models is consistent
      with a real but domain-modulated effect.'

  - name: "classifier_poc"
    plan_id: "plan_008"
    description: "DeBERTa-v3-large binary ambiguity detector, fine-tuned on 300 clause pairs, 5-fold CV."
    expected_results:
      macro_f1: 0.55
      binary_f1: 0.78
      binary_fpr: 0.062
      best_type_f1_cp: 0.89
      worst_type_f1_incomp: 0.28
      per_type_f1_cp: 0.89
      per_type_f1_scopal: 0.71
      per_type_f1_coref: 0.62
      per_type_f1_auth: 0.51
      per_type_f1_lexical: 0.34
      per_type_f1_incomp: 0.28
    result_rationale: >-
      Binary detection (F1=0.78) is serviceable but per-type classification (macro
      F1=0.55) is mediocre. CP is easiest (explicit conflicting rules have strong
      lexical markers — 'however,' 'notwithstanding'). Incompleteness is hardest
      (absence of information has no positive signal — the classifier must learn what's
      MISSING, a fundamentally harder task). Under worst tier, the classifier's
      type-level struggle mirrors the κ re-annotation failure — both reflect that
      fine-grained type distinctions are harder than binary ambiguity detection. The
      classifier is relegated to appendix: 'Preliminary DeBERTa PoC achieves F1=0.78
      for binary ambiguity screening. Per-type classification (F1=0.55) remains
      challenging, consistent with type boundary issues identified in our annotation
      study.'
    tables:
      - title: "DeBERTa Classifier Per-Type F1"
        columns: ["Type", "Precision", "Recall", "F1"]
        rows:
          - ["conditional_precedence", "0.91", "0.87", "0.89"]
          - ["scopal", "0.74", "0.68", "0.71"]
          - ["coreferential", "0.65", "0.59", "0.62"]
          - ["authorization_scope", "0.54", "0.48", "0.51"]
          - ["lexical", "0.38", "0.31", "0.34"]
          - ["incompleteness", "0.32", "0.25", "0.28"]
          - ["Binary (any type)", "0.82", "0.74", "0.78"]
    figures_description:
      - "6×6 confusion matrix: strong diagonal for CP/scopal, diffuse off-diagonal for incompleteness/lexical — auth_scope confused with incompleteness in ~25% of cases."
    analysis: >-
      Classifier PoC is P2 and doesn't affect paper positioning. Under worst tier, it's
      an appendix footnote. Its per-type difficulty gradient (CP easy → incomp hard)
      independently corroborates that type boundaries are genuinely fuzzy, lending
      credibility to the 'honest assessment' of taxonomy limitations.

  - name: "kappa_reannotation_failure"
    plan_id: "what_if_kappa_reannotation"
    description: "Human re-annotation of 25 LLM-coded failure mode traces using improved codebook. THE defining worst-tier experiment."
    expected_results:
      n_traces_reannotated: 25
      kappa_human_human: 0.48
      kappa_human_llm_pooled: 0.22
      human_llm_dominant_mode_agreement: "2/6"
      types_with_agreement: ["scopal", "conditional_precedence"]
      types_with_disagreement: ["auth_scope", "incompleteness", "lexical", "coreferential"]
      auth_scope_human_dominant: "scope_misapplication"
      auth_scope_llm_dominant: "unauthorized_escalation"
      incompleteness_human_dominant: "inappropriate_action"
      incompleteness_llm_dominant: "assumption_based_action"
      systematic_llm_bias_types: 2
    result_rationale: >-
      κ=0.22 (poor) exposes two distinct and reinforcing problems. First, LLM coding
      bias: LLM coders systematically miscategorize by surface keyword matching. For
      auth_scope, traces containing 'exceeded authority' or 'unauthorized' are coded as
      unauthorized_escalation regardless of whether the agent actively chose to exceed
      boundaries (true escalation) or passively misread the permission scope (scope
      misapplication). Human coders, reading the full reasoning chain, find ~40% of
      auth_scope 'unauthorized_escalation' traces are actually scope_misapplication —
      the agent didn't know it was exceeding authority. For incompleteness, LLMs code
      'assumption_based_action' when the trace shows gap-filling behavior, but humans
      often judge these as 'inappropriate_action' — the distinction between 'filling a
      gap' and 'acting wrongly' is interpretive, and humans apply stricter criteria.
      Second, codebook imprecision: human-human κ=0.48 (moderate) reveals that the
      coding scheme's category boundaries are inherently fuzzy. The improved codebook
      (collapsed spurious-compliance/structural-misparse) was insufficient — the
      remaining categories (unauthorized_escalation ↔ scope_misapplication,
      assumption_based_action ↔ inappropriate_action) still overlap when applied to
      real traces. Only scopal (clear scope_misapplication with unambiguous behavioral
      signature) and CP (explicit rule conflict → arbitrary_rule_selection with detectably
      different pattern) survive because their failure modes have distinct, objectively
      identifiable behavioral markers. The LLM-LLM κ=0.52 from plan_005 was artificially
      inflated by shared biases — both coders use the same keyword heuristic, producing
      correlated errors that inflate agreement. The root cause is that agent trace text
      doesn't contain sufficient information to distinguish between failure mechanisms
      (intent-level distinction) — you'd need the agent's internal chain-of-thought,
      which is only partially revealed.
    tables:
      - title: "Human vs LLM Dominant Failure Mode by Type"
        columns: ["Type", "LLM Dominant", "LLM %", "Human Dominant", "Human %", "Agree?"]
        rows:
          - ["auth_scope", "unauthorized_escalation", "78%", "scope_misapplication", "52%", "No"]
          - ["incompleteness", "assumption_based_action", "64%", "inappropriate_action", "45%", "No"]
          - ["scopal", "scope_misapplication", "75%", "scope_misapplication", "68%", "Yes"]
          - ["lexical", "assumption_based_action", "62%", "assumption_based_action", "41%", "No"]
          - ["cond_prec", "arbitrary_rule_selection", "34%", "arbitrary_rule_selection", "42%", "Yes"]
          - ["coreferential", "scope_misapplication", "41%", "assumption_based_action", "36%", "No"]
      - title: "kappa Agreement Summary"
        columns: ["Comparison", "Overall kappa", "Interpretation"]
        rows:
          - ["Human-Human", "0.48", "Moderate — codebook boundaries inherently fuzzy"]
          - ["Human-LLM (pooled)", "0.22", "Poor — systematic LLM keyword bias"]
          - ["LLM-LLM (plan_005)", "0.52", "Moderate — inflated by shared bias"]
      - title: "Systematic LLM Coding Biases Identified"
        columns: ["Type", "LLM Bias Pattern", "Human Finding", "Impact"]
        rows:
          - ["auth_scope", "keyword 'unauthorized' -> unauthorized_escalation", "40% are scope_misapplication", "C5 auth_scope mechanism claim invalid"]
          - ["incompleteness", "keyword 'assumed' -> assumption_based_action", "30% are inappropriate_action", "C5 incompleteness mechanism weakened"]
          - ["lexical", "agreement inflated by kappa paradox", "true diversity higher than coded", "fine-grained % unreliable"]
          - ["coreferential", "coded as scope_misapplication plurality", "flat distribution, no clear dominant", "C5 coref pattern overclaimed"]
    figures_description:
      - "Confusion matrix (4×4): human-coded (rows) vs LLM-coded (columns). Dense off-diagonal cluster at unauthorized_escalation(LLM) × scope_misapplication(Human) for auth_scope traces — the single largest disagreement cell."
      - "Paired bar chart: LLM-coded vs human-coded failure mode distributions per type. Scopal and CP bars match; auth_scope and incompleteness bars diverge sharply."
    analysis: >-
      κ=0.22 is the worst-tier trigger that cascades through the paper. Consequences:
      (1) C5 failure mode taxonomy is invalidated for fine-grained claims — must be
      demoted to appendix as 'exploratory automated analysis.' (2) 'Ambiguity Blindness'
      loses named-contribution status but survives as a Discussion paragraph (binary
      observation, not dependent on failure mode coding). (3) Contribution (3) downgrades
      from 'type-specific failure mode taxonomy' to 'benchmark and protocol release.'
      (4) Discussion shifts from mechanism ('why models fail differently') to implication
      ('what the differential vulnerability means for deployment'). (5) The paper's two
      remaining validated contributions are C1 causal quantification and C4 model×type
      interaction — both purely quantitative. The human-human κ=0.48 provides a partial
      defense: 'The failure mode categories themselves have inherently fuzzy boundaries;
      this is a limitation of trace-based mechanism inference, not just LLM coding
      quality. Future work with chain-of-thought access may enable more reliable
      mechanism classification.' Expected reviewer reaction: 'The authors are commendably
      honest about this limitation, but contribution (3) as stated in the abstract
      is not supported by the validation data.'
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8da21ae7-4539-4e00-9a14-1dfc3351b592",
  "isSidechain": false,
  "requestId": "req_011CbL2zxLJfHH4vbSkDisYS",
  "type": "assistant",
  "uuid": "ad931880-51c3-4723-a883-c63cb186b06b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4",
  "sessionId": "274e5e0e-5042-4718-83a5-9d151d93b8f1",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JppRfCANTEhyfg1FeUwW7U",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21215,
      "cache_read_input_tokens": 11841,
      "output_tokens": 45649,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21215,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 45649,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21215,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21215
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：κ re-annotation fails or exposes systematic LLM coding errors, SOPBench shows inconsistent results — qualitative contribution collapses, paper must be ref…",
  "leafUuid": "ad931880-51c3-4723-a883-c63cb186b06b",
  "sessionId": "274e5e0e-5042-4718-83a5-9d151d93b8f1"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Ambiguity impact on LLM agent policy compliance",
  "sessionId": "274e5e0e-5042-4718-83a5-9d151d93b8f1"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：κ re-annotation fails or exposes systematic LLM coding errors, SOPBench shows inconsistent results — qualitative contribution collapses, paper must be ref…",
  "leafUuid": "ad931880-51c3-4723-a883-c63cb186b06b",
  "sessionId": "274e5e0e-5042-4718-83a5-9d151d93b8f1"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Ambiguity impact on LLM agent policy compliance",
  "sessionId": "274e5e0e-5042-4718-83a5-9d151d93b8f1"
}
```

---
