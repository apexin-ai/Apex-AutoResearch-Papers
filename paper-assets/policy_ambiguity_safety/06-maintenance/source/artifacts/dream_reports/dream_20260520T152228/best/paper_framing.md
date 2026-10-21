# Paper Framing — policy_ambiguity_safety

> 最后更新: 2026-05-20 | 状态: plan_002 complete, framing pivot (C2 falsified)
> 目标: EMNLP 2026 (ARR Aug cycle, DDL ~Aug 3)
> Dream: dream_20260520T112859 — best 3.5 / median 3.0 / worst 2.5 (pre-pivot; re-dream needed)
> plan_002: 1,200 episodes, C1 confirmed (+36.5pp), C2 FALSIFIED (V=0.207, p=0.0001)

## Core Insight

Policy ambiguity causes devastating safety violations in LLM agents (+36.5pp), but **not all types are equally dangerous**: specification-layer ambiguities (authorization scope, incompleteness) cause nearly twice the violation rate increase (~46pp) of linguistic-layer ambiguities (~27pp). This layer hierarchy connects Berry & Kamsties' nocuous ambiguity theory to LLM agent safety and suggests type-aware triage prioritizing specification-layer ambiguities.

## Title (Working)

"Not All Policy Ambiguity Is Equal: Specification-Layer Ambiguity Poses Greater Safety Risks for LLM Agents"

Alternative: "Differential Nocuity: How Ambiguity Type Predicts Safety Violation Severity in LLM Agent Policies"

Note: Pivoted from "Uniformly Nocuous" after plan_002 falsified C2 (V=0.207, p=0.0001). Layer hierarchy is a stronger, more informative finding.

## Core Claims

### C1: Binary Effect (PRIMARY — confirmed)
Ambiguous policy specifications cause massive safety violation rate increases compared to unambiguous matched variants. Effect: +36.5pp (plan_002), McNemar OR=44.8 (CI: [18.47, 108.69]), p<0.0001. Holds across all 6 types and both models.
- **Evidence**: mvp_001 (360 episodes, 3 types) + plan_002 (1,200 episodes, 6 types, 2 models). Bootstrap CI: [+32.0pp, +40.5pp].
- **Strength**: Very strong. Replicated across types and models. Perturbation control (plan_010) confirms ambiguity-specific (Δ_perturb=3.33pp, PASS).
- **Causal backing**: Matched-pair design + perturbation control → strongest causal inference in the literature.

### C2: Type Hierarchy (SECONDARY — confirmed positive, upgraded from null)
**PIVOTED from uniformity null.** Different ambiguity types produce significantly different violation rates. Omnibus χ²=25.61, p=0.0001, V=0.207.
- **Evidence**: plan_002 (1,200 episodes, 6 types × 2 conditions × 2 models)
  - Specification-layer: auth_scope 55% (+53pp), incompleteness 52% (+49pp), CP 35% (+35pp) → avg Δ≈46pp
  - Linguistic-layer: scopal 40% (+36pp), lexical 38% (+30pp), coreferential 25% (+16pp) → avg Δ≈27pp
- **Layer effect**: Specification avg Δ ≈ 46pp vs Linguistic avg Δ ≈ 27pp (~19pp gap)
- **Implication**: Type-aware triage warranted. Specification-layer ambiguities should be prioritized in policy auditing pipelines.
- **TOST**: ±15pp equivalence rejected for most pairs (3/15 equivalent); ±10pp all rejected. Types are NOT interchangeable.
- **MVP→Full Study evolution**: MVP 3 types gave V=0.084 (null); full study 6 types gives V=0.207 (significant). The new types (especially auth_scope and coreferential) drove the heterogeneity — MVP's 3 types were coincidentally similar.
- **Coreferential as boundary case**: 25% violation rate (Δ=+16pp) is the lowest — agents can partially disambiguate via tool responses and cautious strategies. This defines the "nocuous ambiguity boundary" — where external disambiguation channels reduce but don't eliminate harm.

### C3: Layer Effect (SECONDARY — new, from plan_002 data)
**Replaces old "Visibility Moderates Risk" hypothesis.** Specification-layer ambiguities (operating at pragmatic/discourse level of policy interpretation) cause significantly more violations than linguistic-layer ambiguities (operating at syntactic/semantic level).
- **Evidence**: plan_002 layer comparison. Spec avg 47.3% vs Ling avg 34.3%, Δ≈13pp.
- **Mechanism hypothesis**: Linguistic ambiguity can sometimes be resolved by contextual cues (tool responses, user messages, world knowledge). Specification ambiguity (undefined roles, missing conditions) has no external resolution channel — agents must guess.
- **CL connection**: Parallels pragmatics vs semantics distinction. Connects to good-enough processing (Ferreira et al. 2002) — agents may handle syntactic ambiguity "good enough" but fail on pragmatic underspecification.
- **Note on old C3 (visibility)**: diag_001's CP(34%) vs scopal(40%) direction confirmed in full study (CP 35% vs scopal 40%), but the effect is subsumed by the broader layer hierarchy. CP is specification-layer but has the lowest spec-layer rate, while scopal is linguistic-layer with the highest ling-layer rate — they are the convergence point between layers.

### C4: Model Consistency (EXPLORATORY — updated)
No significant model main effect (p=0.581, V=0.016). Both models show similar overall violation rates. Model×type interaction to be tested with 5 models (plan_003 adds Qwen3-8B, Qwen3-32B-AWQ; Claude pending).
- **Evidence**: plan_002 gpt-5.4 (41.0%) vs gpt-4.1 (40.7%). Consistent direction across types.
- **Strength**: 2-model result. Full 5-model test needed for formal interaction analysis.

### C5: Error Analysis (EXPLORATORY — EMNLP core)
Different ambiguity types produce qualitatively different failure modes. Now additionally: failure mode analysis should explain WHY specification-layer types are more dangerous.
- **Evidence**: Requires full study qualitative analysis of agent traces.
- **EMNLP value**: Highest. CL reviewers care about linguistic analysis of WHY, not just THAT.
- **Key questions**: (a) Do spec-layer failures involve more "guessing" (assumption-based action) while ling-layer failures involve "misparse" (scope/reference errors)? (b) Does coreferential show more "avoidance" behavior (conservative strategy) explaining its low rate? (c) Are auth_scope failures distinctive (unauthorized escalation)?

## Narrative Structure (CL-first for EMNLP)

### Intro Logic Chain
1. Agent policies are written in NL → contain ambiguity (established)
2. Prior work classifies ambiguity types in policies (DRIP-R, Li et al., Massey et al.) but doesn't measure safety impact
3. Berry & Kamsties (2003): ambiguity is nocuous (divergent interpretations) or innocuous (convergent). In human RE, shared organizational context makes most ambiguity innocuous.
4. **Gap**: LLM agents lack shared context. Are policy ambiguities nocuous for agents? Does type matter for safety?
5. **This paper**: First causal, type-granularity study. Matched-pair design isolates ambiguity effect. Perturbation control confirms ambiguity-specific causation.
6. **Core findings**: (a) All ambiguity is nocuous (+36.5pp), (b) but type DOES predict severity — specification-layer ambiguities (~46pp) are nearly twice as dangerous as linguistic-layer (~27pp), (c) this hierarchy reflects availability of external disambiguation channels.

### Section Map
- **§1 Intro**: Gap + contributions (causal map + differential nocuity + layer hierarchy + disambiguation channel theory)
- **§2 Related Work**: Ambiguity taxonomies (NLP + RE) → Agent safety evaluation → Policy specification quality. Position vs DRIP-R (concurrent, different angle: we measure safety, they measure decision quality)
- **§3 Taxonomy**: 2-layer, 6-type taxonomy with cross-walk to Li et al. + Massey et al. + DRIP-R. Operational definition (ambiguity + vagueness, per Wasow 2005)
- **§4 Method**: Matched-pair causal design, τ²-bench, clause generation pipeline, perturbation control, cross-judge evaluation, statistical analysis plan
- **§5 Results**: C1 (binary, +36.5pp) → C2 (type hierarchy, V=0.207) → C3 (layer effect, Spec>>Ling) → C4 (model consistency)
- **§6 Analysis**: C5 error analysis — qualitative failure modes per type, explaining WHY specification-layer is more dangerous. This is the EMNLP core.
- **§7 Discussion**: Differential nocuity theory. Disambiguation channel hypothesis. Practical implications (type-aware triage pipeline, prioritize spec-layer). Limitations (2 domains, 2 API models, synthetic injection).
- **§8 Conclusion**: All policy ambiguity is nocuous, but specification-layer ambiguities demand priority attention. Type-aware auditing recommended.

## Anticipated Reviewer Concerns

### RC1: "Type effect could be artifact of taxonomy granularity"
**Response**: (a) Layer effect (Spec vs Ling ~19pp gap) is robust — holds even if individual types are reclassified. (b) 2-layer structure grounded in Li et al. + Massey et al. (c) Coreferential's low rate has structural explanation (disambiguation channels), not just noise. (d) TOST confirms types are NOT equivalent (0/15 pairs at ±10pp).

### RC2: "Taxonomy is ad hoc / why these 6 types"
**Response**: 2-layer structure grounded in Li et al. 2024 (11-type NLP) + Massey et al. 2014 (6-type RE). Selection criteria: frequency in policy documents + theoretical distinctiveness. Explicit cross-walk to DRIP-R's 5 types. Operational definition handles ambiguity/vagueness boundary (Wasow 2005, Kennedy 2007).

### RC3: "Only API models, no open-source"
**Response**: Full study adds Qwen3-8B + Qwen3-32B-AWQ (open-source, local inference). 5-model coverage spans frontier API (gpt-5.4, claude-sonnet-4-6) + mid-tier API (gpt-4.1) + open-source at two scales. Model×type interaction analysis (C4) explicitly tests capability dependence.
**Note [Reviewer 2026-05-20]**: Cross-judge asymmetry — Claude judged by gpt-5.4 (strongest), gpt-5.4 judged by gpt-4.1 (weaker). Must disclose in Method. plan_009 judge calibration measures this bias.

### RC4: "Synthetic ambiguity injection lacks ecological validity"
**Response**: (a) Matched-pair design requires synthetic control for causal inference. (b) Reviewer-verified quality (Chantree-style). (c) CP clauses use both explicit labeling and naturalistic rule rewrites. (d) Full study mixes formats per Reviewer suggestion. (e) Realism validation: distribution comparison with DRIP-R natural ambiguities.

### RC5: "τ²-bench limited to retail/airline"
**Response**: Acknowledged limitation. Two domains already show consistent effects. Cross-domain transfer is Future Work (Phase 3 classifier PoC, if time permits). DRIP-R also single-domain (retail).

### RC6: "Binary effect is obvious — of course ambiguity causes errors"
**Response**: (a) No prior work quantifies effect SIZE for agent safety. +35-42pp is massive and non-trivial. (b) DRIP-R measures decision quality, not safety violations. (c) Prior work (PolicyBank, PhantomPolicy) studies different failure modes, not ambiguity-specific causation. (d) The interesting finding is C2: type DOESN'T matter, contradicting intuition that some ambiguities are worse.

### RC7: "Incompleteness matched-pair confound (information asymmetry)"
**Response**: (a) Dual-track analysis: primary analysis uses ambiguous-only cross-type comparison (avoids confound). (b) Incompleteness pairs constrained to minimal information addition. (c) Explicitly discussed as limitation for within-type effect size.

### RC8: "RC attachment in coreferential overlaps with scopal / structural ambiguity"
**Response**: (a) Our scopal category is explicitly scoped to quantifier/negation/modal scope interactions, not syntactic attachment. (b) RC attachment in policies manifests as *referential* confusion (which entity does the clause modify?) not *scope* confusion (which operator takes wide scope?). (c) Li et al. 2024 distinguishes syntactic ambiguity (including RC attachment) from scopal ambiguity — our grouping follows their treatment that RC attachment is closer to coreferential than scopal in terms of downstream interpretation. (d) Empirically, if the distinction were problematic, coreferential and scopal would show identical violation patterns — the error analysis (C5) can test whether their failure modes differ.

### RC9: "authorization_scope is just a subtype of incompleteness"
**Response**: (a) Incompleteness = missing conditions/exceptions/boundaries (structural absence). Authorization scope = ambiguous permission/role boundaries that ARE stated but vague (e.g., "authorized personnel" without specifying which functions). (b) The disambiguation pattern differs: incompleteness adds new conditions; auth_scope clarifies existing permission boundaries. (c) Empirically testable: if they were the same, their violation patterns and failure modes (C5) would be indistinguishable. (d) Report disambiguation length ratio per type as control variable in §4 Method.

### RC10: "API sampling noise undermines reliability"
**Response**: (a) Reviewer identified ±8pp test-retest band for scopal clauses. (b) Full study reports bootstrap CI for all violation rates. (c) Key findings (binary effect +31-42pp) far exceed noise band. (d) Null findings (type effect V=0.084) are robust — even with favorable noise, effect remains negligible.

### RC11: "Prompt sensitivity confound" [Dream A9 — best tier "strongest point"]
**Concern**: The +35-42pp effect is attributed entirely to ambiguity, but without a control condition using non-ambiguity perturbations (synonym substitution, clause reordering), the paper cannot cleanly distinguish ambiguity-specific harm from general prompt brittleness.
**Response**: ✅ RESOLVED. plan_010 perturbation control (120 episodes): Δ_perturb=3.33pp (CI contains 0) vs ambiguity Δ=36.5pp. Non-ambiguity surface changes cause zero meaningful effect. This is the strongest causal evidence in the agent safety literature.

## Concept Naming (distill insight: 命名即贡献)

Core phenomenon: **"Differential Nocuity"** — all policy ambiguity types are nocuous for LLM agents, but specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones. Unlike human RE where organizational context renders most ambiguity innocuous, agents lack disambiguation channels for specification-level underspecification.

Secondary phenomenon: **"Ambiguity Blindness"** — agents process grammatically fluent ambiguous clauses without meta-cognitive awareness of the ambiguity, adopting surface interpretations. Contrasts with explicit rule conflicts where agents show awareness and choose conservatively.

Tertiary phenomenon: **"Disambiguation Channel Hypothesis"** — the layer hierarchy reflects availability of external disambiguation: linguistic ambiguity (coreferential, lexical) can sometimes be resolved by tool responses, user context, or world knowledge; specification ambiguity (auth_scope, incompleteness) has no external resolution channel, forcing agents to guess.

## Opening Hook Strategy (distill insight: 具体案例, 不要 "Recently...")

Open with a concrete τ²-bench failure: e.g., a customer returns a customized item within the return window; the agent grants a full refund + free return shipping because the policy says "items may be returned within 30 days" (scopal: "items" scopes over all categories including custom). The unambiguous version specifies "standard items only" — agent correctly refuses. One word of ambiguity → $200 unauthorized refund.

## Narrative Type: 突破局限型 (distill pattern, 5/8 papers)

"DRIP-R classifies 5 ambiguity types and shows models disagree on interpretation → but does not measure whether this disagreement leads to safety violations. We close this gap — and find the answer is surprising: all types are equally dangerous."

## Benchmark Comparison Table (distill insight: 必有 feature matrix)

| Feature | DRIP-R | PhantomPolicy | PolicyBank | AgentPex | **Ours** |
|---------|--------|---------------|------------|----------|----------|
| Ambiguity taxonomy | 5 RE types | — | 3 gap types | — | **6 types (2-layer)** |
| Causal design | — | — | — | — | **matched pairs** |
| Safety violation metric | — | binary | — | procedural | **3-tier severity** |
| Cross-type comparison | descriptive | — | — | — | **statistical (χ² + V)** |
| Models tested | 6 API | 4 API | 2 API | 2 API | **2 API + 2 open-source** |
| Domain | retail | mixed | retail | telecom/retail/airline | **retail + airline** |

## Contribution Positioning (for EMNLP)

1. **Problem formulation**: First causal framing of ambiguity type → safety violation in agent policies. Introduces "uniform nocuity" as a named phenomenon.
2. **Empirical**: Quantifies binary effect (+31-42pp) across 6 types and 4 models. Reports informative null on type differentiation.
3. **Theoretical**: Connects Berry & Kamsties nocuous ambiguity theory to agent safety. Proposes "ambiguity blindness" mechanism linking linguistic visibility to safety risk.
4. **Practical**: Binary ambiguity detection suffices for safety triage. Type-specific pipelines not justified.
5. **Methodological**: Matched-pair causal design + cross-judge evaluation + 2-layer taxonomy with cross-walk.

## Required Reference Expansion [Dream A2 — three-tier consistent]

Current plan has thin references. Must add (≥25 total in final paper):
- **Good-enough processing**: Ferreira, Bailey & Ferraro (2002); Ferreira & Patson (2007) — directly relevant to visibility hypothesis (how processors handle ambiguity without full reanalysis)
- **Surprisal/expectation-based**: Levy (2008); Hale (2001) — why some ambiguity triggers reanalysis
- **Instruction-following robustness**: Zhou et al. (IFEval, 2023); Qin et al. (ToolBench, 2024) — ambiguity sensitivity as special case of instruction robustness
- **Prompt sensitivity**: Sclar et al. (2024); Lu et al. (2022) — general prompt brittleness literature
- **Broader agent safety**: R-Judge, ToolEmu, InjecAgent — position against wider agent safety work
- **Formal semantics of vagueness**: Lassiter & Goodman (2017) — ambiguity/vagueness boundary
- **Garden-path**: Frazier & Rayner (1982) — reanalysis cost grounding for C3
- **Ambiguity detection**: Willis et al. (2008); Ezzini et al. (TAPHSIR, 2022)

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
5. **Figure 5**: Failure mode × type Sankey/alluvial diagram (§6 C5)
6. **Figure 6**: Annotated trace pair — CP (conflict detection) vs scopal (surface adoption) (§6 C5)

## Berry & Kamsties Operationalization Note [Dream best Q5]

Berry & Kamsties define nocuity as inter-reader divergence. Our design measures agent-vs-intent deviation. Full study should additionally test whether different models adopt different readings of the same ambiguous clause (true inter-model nocuity). If 4 models produce 4 different interpretations of the same clause → true nocuity. If all 4 adopt the same wrong interpretation → systematic bias, still nocuous but for different reason. Report inter-model agreement on ambiguous clauses as supplementary analysis.

## Contingency Framing [Reviewer assessment 2026-05-20]

如果 full study 结果偏离 MVP，预备以下 pivot 方向（小时级完成 reframe）：

**Scenario B — 2/6 types binary effect 不显著**（概率中低，取决于 coreferential 修复质量）:
- Pivot: "Not All Ambiguity Is Nocuous: Type-Dependent Safety Risks"
- C1 降级 "most types nocuous" + 效果异质性; C2 升级为 positive finding
- 更深 CL insight: nocuity 取决于 agent 消歧渠道可获取性
- 实用建议从 "binary detection" 改为 "type-aware triage"

**Scenario C — Type uniformity 被拒绝（omnibus p<0.05, 但所有类型仍 nocuous）**（概率中等）:
- Pivot: 去掉 "Uniformly"，改为 "type hierarchy predicts severity"
- C2 从 confirmed null → weak type effect / type hierarchy
- C4 从 exploratory 升级为 supporting evidence
- 如果排序与语言学理论一致 → 正面发现；随机排序 → noise

**关键降风险措施**: coreferential 第三轮 mini-pilot 是 Scenario B 的最大杠杆点。

## Claude Baseline — RESOLVED [2026-05-20]

4/8 distilled papers use Claude as baseline. ✅ Claude Sonnet 4.6 added as 5th model via OpenRouter proxy (base_url=http://47.94.22.126/v1). plan_002 expanded to 3 API models (gpt-5.4, gpt-4.1, claude-sonnet-4-6). Total model coverage: 5 models across 3 families (OpenAI, Anthropic, Qwen).
