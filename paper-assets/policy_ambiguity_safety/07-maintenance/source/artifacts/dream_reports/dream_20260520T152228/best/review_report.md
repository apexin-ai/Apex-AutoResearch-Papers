---
dream_id: dream_20260520T152228
tier: best
overall_score: 3/6 — Borderline Findings
timestamp: 2026-05-20T16:55:30.271057+00:00
---

# R2 Review: Novelty, Contributions, and Related Work

**Paper**: "Not All Policy Ambiguity Is Equal: Specification-Layer Ambiguity Poses Greater Safety Risks for LLM Agents"
**Reviewer**: R2 (Novelty + Contributions + Related Work)
**Score**: 3/6 (Borderline Findings)
**Confidence**: 4/5

---

## Summary

This paper presents a matched-pair causal study of how six types of policy ambiguity affect safety violation rates in LLM agents, testing five models across 3,000 agentic episodes on τ²-bench. The core claim — "Differential Nocuity" — is that specification-layer ambiguities (+43.6pp) are nearly twice as dangerous as linguistic-layer ones (+26.2pp). The paper includes a perturbation control, error analysis with six failure modes, inter-model nocuity measurement via Fleiss κ, and a DeBERTa classifier proof-of-concept. The experimental design is rigorous, but the novelty is primarily empirical rather than conceptual, the layer dichotomy is undermined by its own data, the related work is thin and missing critical connections, and the contribution framing is overclaimed relative to evidence.

---

## Strengths

- **The matched-pair design combined with a perturbation control is genuinely novel in the agent safety literature.** Table 12's feature comparison correctly shows no prior work achieves this combination. The perturbation arm (Δ=3.3pp vs. ambiguity Δ=36.5pp, ratio=0.09) provides convincing causal evidence that the observed effects are ambiguity-specific, not general prompt brittleness. This is the paper's single strongest methodological contribution.

- **The error analysis (Section 6) is the paper's most valuable section.** The 300-trace qualitative analysis revealing mechanistically distinct failure modes per type — unauthorized assumption for auth_scope (72%), scope escalation for incompleteness (65%), misparse scope for scopal (58%), surface adoption for lexical (62%) — provides genuine explanatory depth. The 82% failure-mode-to-layer consistency is informative. The coreferential avoidance finding (44% vs. 8% for other types) is a genuinely novel behavioral observation.

- **The Berry & Kamsties operationalization via Fleiss κ is well-executed.** Measuring inter-model agreement on ambiguous clauses (κ=0.33) vs. unambiguous ones (κ=0.82) provides a clean operationalization of nocuity as divergent interpretation. The Δκ=−0.49 and the 58% vs. 12% divergent clause rates strengthen the theoretical connection.

- **The Disambiguation Channel Hypothesis has genuine explanatory power.** The gradient from scopal (Δ=34.8pp, low external resolution) to coreferential (Δ=16.2pp, 23% tool-based disambiguation) aligns with the hypothesis that external information channels partially mitigate linguistic-layer ambiguity but not specification-layer ambiguity.

- **The binary effect (C1) is robust and well-quantified.** +35.8pp with CI [33.1, 38.5], OR=42.1, holding across all six types and five models. This is a useful quantification for the community even if the directional finding is unsurprising.

---

## Weaknesses

### W1 (MAJOR): CP undermines the clean layer dichotomy, invalidating the headline claim.

The paper's title and abstract frame the core finding as "specification-layer ambiguities are nearly twice as dangerous as linguistic-layer ones." However, the paper's own data shows CP (specification-layer, Δ=31.0pp) falls *below* scopal (linguistic-layer, Δ=34.8pp). The actual type ranking is:

auth_scope (52.0) > incompleteness (47.8) > **scopal (34.8) > CP (31.0)** > lexical (28.6) > coreferential (16.2)

The spec/ling boundary is crossed. The "nearly twice as dangerous" framing (43.6pp vs. 26.2pp) is an artifact of averaging: it is driven by the extremes (auth_scope+incompleteness vs. coreferential), not a consistent layer effect. The paper acknowledges this in Section 6 via the "visibility" argument (CP has detectable conflicts, making it behaviorally distinct), but this explanation actually *undermines* the two-layer taxonomy — if CP behaves more like a linguistic-layer type because its conflicts are "visible," then the spec/ling distinction is not the right organizing principle.

A more honest framing would be: "authorization scope and incompleteness ambiguities are substantially more dangerous than other types, and coreferential ambiguity is least dangerous, with the middle four types (CP, scopal, lexical, and their neighbors) forming a less differentiated cluster." This is a weaker but more accurate claim.

### W2 (MAJOR): "Differential Nocuity" is overclaimed as a theoretical framework.

The observation that different ambiguity types cause different violation rates is an expected finding from any taxonomy study with sufficient power. The real value lies in (a) the causal quantification, (b) the error analysis showing mechanistically distinct failure modes, and (c) the disambiguation channel observation. Packaging these as a named "framework" — "Differential Nocuity" — adds branding without proportional conceptual substance. The paper would be stronger presenting these as empirical findings with mechanistic grounding rather than elevating them to a theoretical framework.

The term also creates confusion: Berry & Kamsties' original "nocuity" refers to whether an ambiguity produces divergent interpretations (nocuous) vs. convergent ones (innocuous). "Differential Nocuity" suggests different *degrees* of interpretive divergence, which is a different concept from different *rates of safety violation*. The paper conflates these two meanings.

### W3 (MAJOR): Related work has significant gaps for a paper making theoretical claims.

The paper cites only 16 references. For a paper that positions itself at the intersection of computational linguistics, requirements engineering, and agent safety — and that proposes a named theoretical framework — this is thin. Specific gaps:

**Pragmatics literature (entirely missing):** The Disambiguation Channel Hypothesis is fundamentally about pragmatic inference — agents lack shared context and cooperative norms that humans use for disambiguation. Yet there is no engagement with Grice (cooperative principle, implicature), Clark (common ground theory), or Sperber & Wilson (relevance theory). The specification/linguistic layer distinction maps naturally onto pragmatics/semantics, but this connection is never made explicit.

**RLHF/alignment effects (undiscussed):** The paper notes Claude shows the highest avoidance rate and GPT-5.4 shows the most aggressive execution, but attributes these only to vague "model differences." The alignment training literature (Constitutional AI, RLHF) directly explains why different models handle ambiguity differently. This is not just a missing citation — it's a missed analytical opportunity.

**Legal NLP / contract ambiguity (missing):** Specification-layer ambiguity in policies is directly analogous to contract ambiguity in legal documents. The growing legal NLP literature on contract analysis, ambiguity detection in legal text, and formal specification of legal provisions is highly relevant and entirely absent.

**Formal policy verification (missing):** ShieldAgent (ICML 2025), MANTRA (2026), AgentSpec (ICSE 2026), and Policy Compiler (2026) all address formal approaches to policy specification. The paper's practical recommendation (type-aware triage) would be substantially strengthened by positioning it as the diagnostic front-end to these formalization pipelines.

**Broader agent safety benchmarks (sparse):** ATBench, OpenAgentSafety, SafetyDrift, PolicyGuard, CRAFT are all relevant but uncited. The comparison table (Table 12) includes only four baselines.

**Requirements engineering beyond Berry & Kamsties:** Chantree et al. (2006) on nocuous ambiguity detection, Ezzini et al. (2022) TAPHSIR system, Willis et al. (2008) on automated ambiguity detection — the RE literature is richer than the paper acknowledges.

### W4 (MAJOR): Five contributions in 8 pages stretches the paper thin.

The paper claims five findings: (C1) binary effect, (C2) type hierarchy, (C3) layer effect, (C4) architecture-universality, and (C5) inter-model nocuity. This is overambitious:

- C1 is a prerequisite for the other claims, not an independent contribution. The direction (ambiguity causes violations) is unsurprising; the magnitude quantification is useful but not standalone-contribution-level.
- C2 and C3 are deeply related (C3 is an aggregation of C2). Presenting them as separate contributions inflates the contribution count.
- C4 (Model×Type interaction p=0.34) is essentially a non-finding presented as a contribution. A non-significant interaction in a 5-model × 6-type design with the observed sample sizes has limited inferential value — it could reflect true universality or insufficient power.
- C5 (inter-model nocuity, Fleiss κ) is interesting but gets only one page of development.

The paper would be stronger consolidating to three claims: (1) causal binary effect with perturbation control, (2) type hierarchy with layer-level tendency and mechanistic grounding via error analysis, and (3) inter-model nocuity operationalizing Berry & Kamsties.

### W5 (MAJOR): The psycholinguistic grounding is asserted rather than argued.

Section 2 invokes good-enough processing (Ferreira et al., 2002) and garden-path effects (Frazier & Rayner, 1982) as explanatory frameworks for why agents adopt surface readings of ambiguous clauses. But the paper never argues *why* these human processing models should apply to autoregressive language models. LLM generation is fundamentally different from human incremental comprehension — there is no eye-movement regression, no reanalysis cost, no working memory bottleneck. The behavioral analogy may hold, but the mechanistic basis is unexamined. Four sentences of assertion (Section 2, paragraph 4) is insufficient grounding for what becomes a recurring explanatory motif.

### W6 (MINOR): The DeBERTa classifier PoC (Section 7) is tangential.

F1=0.89 on 60 test examples from the same synthetic distribution as training is expected for a fine-tuned model. The zero-shot GPT-4.1 baseline (F1=0.64) is the more interesting data point — suggesting that LLMs are poor at detecting the very ambiguities that cause their failures. But this receives one sentence. The classifier consumes valuable page budget without advancing the core narrative. Move to appendix.

### W7 (MINOR): The taxonomy cross-walk is mentioned but not shown.

Section 3 claims a cross-walk to DRIP-R's five types and Massey et al.'s six-type scheme, but no table or explicit mapping is provided. For a paper whose taxonomy is the structural backbone, this is an oversight. A mapping table would also help readers assess whether the six selected types adequately cover the policy ambiguity space.

### W8 (MINOR): Conflation of ambiguity and vagueness is acknowledged but underdefended.

The paper follows Wasow et al. (2015) in operationally including vagueness under ambiguity "when the effect on agent behavior is indistinguishable." But authorization scope (e.g., "authorized personnel may access customer records") is paradigmatic vagueness — a continuous spectrum of interpretation, not discrete alternative readings. This is a contested choice in linguistics. The one-sentence defense (Section 3, citing Wasow et al.) is insufficient. Some reviewers will object that the entire specification layer is studying vagueness/underspecification, not ambiguity, which would undermine the unified taxonomy.

### W9 (MINOR): Architecture-universality claim is strong given non-significant interaction.

The non-significant Model×Type interaction (p=0.34) is presented as evidence for "architecture-universal hierarchy." But non-significance does not equal equivalence. With 5 models and 6 types, the interaction test may lack power. The paper does not report an equivalence test (TOST) for the interaction, only for pairwise type comparisons. "Consistent across tested models" would be more calibrated than "architecture-universal."

---

## Questions for Authors

1. **CP anomaly**: How do you reconcile the headline "specification nearly twice as dangerous as linguistic" with CP (spec, 31.0pp) < scopal (ling, 34.8pp)? Is the two-layer taxonomy the right organizing principle, or would a three-group structure (high: auth_scope+incompleteness; medium: scopal+CP+lexical; low: coreferential) be more faithful to the data?

2. **Disambiguation Channel — causal test**: The Disambiguation Channel Hypothesis is correlational. Have you considered manipulating channel availability (e.g., withholding tool access, or providing explicit "if ambiguous, ask for clarification" instructions) to test it causally?

3. **Convergent-but-wrong**: What proportion of ambiguous clauses produce unanimous wrong interpretations across all five models (i.e., all models converge on the same incorrect reading)? This would distinguish true nocuity (divergent interpretations) from systematic bias (convergent-but-wrong), which has different practical implications.

4. **Psycholinguistic mechanism**: Beyond behavioral analogy, what evidence suggests autoregressive LLMs exhibit processing patterns analogous to good-enough comprehension? Could the surface adoption finding be explained more parsimoniously by training data distribution (high-frequency readings dominate)?

5. **Ambiguity vs. vagueness**: For authorization scope, can you provide examples where the policy admits discrete alternative readings (true ambiguity) rather than a continuous spectrum of interpretation (vagueness)? If not, should this type be relabeled?

6. **RLHF interaction**: Claude shows the highest avoidance rate across all types (Section 6). Does this reflect Constitutional AI training specifically targeting cautious behavior under uncertainty? If so, this suggests alignment methods are a direct mitigation for ambiguity-driven violations — a finding worth developing.

---

## Minor Issues

- Table 5 caption says "Type ranking auth_scope > incompleteness > scopal > lexical > CP > coreferential is preserved across all five models" — but this ranking has CP below scopal, crossing the layer boundary. The caption should acknowledge this.
- The paper claims to release "all clause pairs, evaluation code, and annotated traces" (abstract) but no URL, repository, or supplementary materials are provided.
- "Conflicting provisions" is abbreviated as "CP" without definition at first use in the abstract.
- The perturbation control (Section 4.3) uses only 30 pairs and 3 API models (180 episodes). Extending to open-source models (especially Qwen3-8B, which shows different behavioral patterns) would strengthen the causal claim.
- The logistic regression (Table 6) reports "Model (5 levels)" as a single coefficient — this should be a set of 4 indicator coefficients or an omnibus test, not a single z-value. The reporting format is unclear.
- Section 5.4 reports Model×Type interaction p=0.34, but Section 5.5 (inter-model nocuity) reports κ=0.33 on ambiguous clauses. These are related but distinct analyses — the paper should clarify how interaction non-significance relates to low inter-model agreement.
- The paper uses "3-tier severity" in Table 12 but the main text only reports binary (violation/no-violation) outcomes. Where is the severity analysis?

---

## Overall Assessment

**Score: 3/6 (Borderline Findings)**

**EMNLP equivalent: 2.5–3.0 (between Borderline Findings and Findings)**

**Justification:**

The paper addresses a timely and genuinely novel research question — no prior work causally links ambiguity type to safety violation severity in LLM agents. The matched-pair design with perturbation control is the strongest causal framework in this literature, and the error analysis provides genuine mechanistic insight into why different ambiguity types produce different failure modes.

However, I have serious concerns about the paper's current form:

(1) The headline claim — "specification nearly twice as dangerous as linguistic" — is undermined by the paper's own data (CP < scopal), making the two-layer taxonomy a leaky abstraction rather than a clean organizing principle. The paper needs to either qualify the layer claim substantially or restructure around the type ranking directly.

(2) "Differential Nocuity" is overclaimed as a theoretical framework. The novelty is empirical (quantification + mechanism), not conceptual (the idea that different ambiguity types have different effects is not surprising).

(3) The related work is too thin (16 references) for a paper making theoretical claims at the CL/RE/safety intersection. Missing pragmatics, alignment/RLHF, legal NLP, and formal verification connections weaken both the theoretical grounding and the practical positioning.

(4) Five contributions in 8 pages is overambitious. Several (C1 as standalone, C4 as non-finding-as-contribution) are inflated.

(5) The psycholinguistic grounding is asserted without mechanistic argument.

The paper has strong experimental bones. With restructured framing (lead with type ranking + error analysis, present layer as secondary observation with CP caveat), expanded related work (25+ references with pragmatics and alignment connections), and toned-down theoretical claims, this could reach Conference level. In its current form, the overclaiming and thin related work keep it at the Findings boundary.

**Confidence: 4/5** — I have read the paper carefully and have domain expertise in both computational linguistics and agent safety evaluation. My main uncertainty is whether the five-model results are fully completed or partially projected; if projected, the universality claims would need further downgrading.
