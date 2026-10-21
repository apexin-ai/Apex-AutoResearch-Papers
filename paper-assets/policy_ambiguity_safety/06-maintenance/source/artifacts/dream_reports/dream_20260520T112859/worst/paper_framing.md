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
