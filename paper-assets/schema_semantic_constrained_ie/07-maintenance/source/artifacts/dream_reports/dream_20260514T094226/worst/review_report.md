---
dream_id: dream_20260514T094226
tier: worst
overall_score: Weak Reject (3/6)
timestamp: 2026-05-14T11:04:54.261725+00:00
---

# Dream Review Report — Full Roundtable

**Paper**: "How LLMs Violate Ontology Constraints: A Landscape Study and Grammar-Based Mitigation"  
**Review Mode**: Full (2 Reviewers, 4-Step Roundtable)  
**Venue Standard**: Top ML venue, ~25% acceptance, 6-point scale

---

## Step 1: Independent Reviews

### Reviewer R1 — Methods & Experiments

**Score: 4 (Weak Accept) | Confidence: 4**

**Strengths:**
- S1. Well-defined four-level violation taxonomy with clear decidability classification (ET/RV as CFG-expressible vs DR/CF as stateful/global). This is a genuine conceptual contribution.
- S2. Grammar layer achieves perfect ET/RV elimination (0%) across both datasets and both models — the cleanest result in the paper. Zero F1 degradation and only 14% latency overhead make this immediately actionable.
- S3. Proper ablation design on SciERC with enabling dependency quantification (12.5× ratio). The semantic-only vs full comparison isolates the grammar layer's prerequisite role convincingly.
- S4. Honest treatment of negative results: DocRED's 35.5% DR reduction (vs SciERC's 94%), tightness-DR null result (ρ=0.14, p=0.18), and CF side effects are reported transparently rather than buried.
- S5. The "grammar-only DR increase" on DocRED (15.8%→26.17%) is correctly identified as a measurement artifact (RV violations masking true DR) — this is a subtle insight that strengthens the paper's analytical credibility.

**Weaknesses:**
- W1. **CF trade-off unquantified in downstream terms.** Grammar+Semantic introduces 9.9% CF on SciERC and 2.99% on DocRED. The paper argues these are less severe than DR violations but provides no downstream evaluation (KG quality, QA accuracy, etc.) to validate this claim. A reviewer could argue the method trades one violation type for another.
- W2. **No post-hoc filtering baseline.** The paper argues against post-hoc filtering ("cannot redirect probability mass, wastes compute on rejected outputs") but never runs a post-hoc baseline. At ~0% latency overhead, post-hoc filtering achieving even 50% DR reduction would undermine the constrained decoding justification. This is a gap in the experimental design.
- W3. **Single seed, single prompt, no variance estimates.** All results are single-run. No confidence intervals, bootstrap estimates, or multi-seed experiments. The F1 difference between unconstrained (8.23%) and Grammar+Semantic (8.36%) is called "not statistically significant" but no test is reported.
- W4. **Only two 8B-class models tested.** No larger models (70B), no base-vs-instruct comparison, no closed-source models. The violation landscape could look very different at larger scales or with stronger instruction-following.
- W5. **Very low absolute F1 (~8%).** Both R-F1 values hover around 8%, far below practical utility thresholds. This raises the question: are we measuring constraint violations on a system that is too weak for real deployment? The violation landscape study would be more convincing on a system with competitive extraction quality.
- W6. **DocRED unconstrained baseline fairness.** The paper uses a Phase 2 pipeline for DocRED unconstrained (DR=15.8%) but the comparison to grammar+semantic (DR=10.19%) yields only 35.5% reduction. It is unclear whether the unconstrained baseline uses exactly the same prompt template, generation config, and post-processing as the constrained runs. Any pipeline differences could inflate or deflate the reduction percentage.
- W7. **Enabling dependency analysis is post-hoc.** The enabling ratio (semantic-only DR / full DR) is presented as a discovered mechanism, but the definition was likely crafted after observing the SciERC results. The DocRED enabling ratio=1.1 then becomes a "the mechanism doesn't generalize" finding rather than a clean null result from a pre-registered hypothesis.

**Questions for Authors:**
1. What happens if you combine schema-informed prompting (providing ontology constraints in the prompt) with grammar-constrained decoding? This is the natural practical configuration but is not tested.
2. Can you provide the per-relation breakdown of the grammar-only DR increase on DocRED? Which relations contribute most, and does the RV→DR transfer hypothesis hold uniformly?
3. What are the CF rates for Llama-3.1-8B? Cross-model CF consistency would strengthen the analysis.
4. Have you computed bootstrap confidence intervals for any of the F1 or violation rate comparisons?
5. How does the semantic layer's graceful degradation fallback (empty intersection → grammar-only) trigger rate vary across datasets?

---

### Reviewer R2 — Novelty & Related Work

**Score: 3 (Weak Reject) | Confidence: 4**

**Strengths:**
- S1. The paper addresses a genuine practical problem — LLM-generated IE output violating ontology constraints — that is underexplored in the literature.
- S2. The honest reporting of negative results (DocRED degradation, CF trade-offs, tightness null result) is commendable and raises the paper's credibility.
- S3. The grammar layer finding is clean and actionable: a practitioner reading this paper could immediately add XGrammar-based decoding to their IE pipeline.
- S4. The pivot from "method paper" to "empirical study + targeted solution" is a reasonable framing given the mixed results.

**Weaknesses:**
- W1. **Thin novelty across all three contributions.** (a) The grammar layer is a straightforward application of XGrammar to IE ontologies — the technical contribution is writing the schema-to-grammar compiler, which is engineering rather than research. (b) The semantic layer transfers type-constrained logit masking from code generation (Synchromesh, MGD) to IE with modest technical novelty — the core idea of dynamic logit masking conditioned on partial output is well-established. (c) The violation landscape study is descriptive, covering only 2 datasets and 1–2 models, which is narrow for an empirical contribution.
- W2. **Sparse related work — only 7 references.** Major gaps include:
  - Structured prediction for IE (joint entity-relation models that inherently enforce type constraints via architecture)
  - Alternative constrained decoding methods: PICARD (Scholak et al., 2021), Synchromesh (Poesia et al., 2022), Guidance (Microsoft), SGLang
  - Schema-guided dialogue/generation (SGD, Rastogi et al., 2020)
  - Broader type-constrained KG completion beyond Krompass (TransE/RotatE with type constraints)
  - Error analysis in IE (prior work characterizing extraction errors, even if not framed as "violations")
  - Commercial structured output features (OpenAI function calling, Anthropic tool use) that partially solve the same problem
  - This level of citation sparsity would be flagged at any top venue.
- W3. **No downstream task evaluation.** The paper motivates constraint enforcement with KG quality, downstream reasoning, and regulatory compliance but never evaluates whether reducing violations improves any downstream metric. Without this, the practical significance remains theoretical.
- W4. **Semantic layer effectiveness does not justify its complexity.** On DocRED (the more realistic/complex dataset), the semantic layer achieves only 35.5% DR reduction while introducing 2.99% CF violations and 39% latency overhead. The cost-benefit ratio is unfavorable. On SciERC (7 relations), the strong result is on a toy-scale ontology that does not represent real-world complexity.
- W5. **Cross-model analysis is incomplete and confounded.** Llama-3.1-8B is tested only on SciERC unconstrained — no constrained decoding results for Llama, no DocRED results. The 92% parse rate introduces survivorship bias that the paper acknowledges but does not resolve. With only 2 models from different families, the cross-model "consistency" claim (ρ=0.82) is statistically weak.
- W6. **Positioning ambiguity.** The paper oscillates between three identities: (a) empirical study of violations, (b) method paper for constrained decoding, (c) proof-of-concept for semantic constraints. Each individually is thin — the landscape study needs more models/datasets, the method needs stronger results, the proof-of-concept needs a path forward. The combination doesn't compound into a strong paper; it fragments into three incomplete contributions.
- W7. **Title overclaims.** "How LLMs Violate Ontology Constraints" implies a general investigation, but the study covers only 2 datasets and 2 models in the narrow setting of zero-shot IE. The title should be scoped more precisely.

**Questions for Authors:**
1. How do you position this work against joint entity-relation extraction models (SpERT, PFN, etc.) that enforce type constraints by architectural design? These achieve much higher F1 while inherently avoiding many violation types.
2. Have you considered testing with larger models (70B+) or API-based models where instruction-following is stronger? The violation landscape at 8B may not generalize.
3. What is the technical novelty of the semantic layer beyond applying Synchromesh-style dynamic masking to IE ontology constraints?
4. Can you estimate the practical impact of the grammar layer by measuring what fraction of downstream errors (in a KG or QA pipeline) are attributable to ET/RV violations?
5. Why not include a simple prompt-engineering baseline (providing the full ontology with domain/range constraints in the prompt)?

**Minor Issues:**
- Discussion (§6) placed before Related Work (§7) — unconventional ordering.
- Table 6 omits DR for SciERC grammar-only (shown as "—"). Should be reported for completeness.
- "Constraint tightness" defined informally in §3.2 — needs a formal equation.
- Appendix A (S1 vs S2) feels like padding — could be cut or summarized in one paragraph.

---

## Step 2: Cross-Sharing

**R1→R2**: R1's core concern is experimental rigor — missing variance estimates, no post-hoc baseline, single-seed results, and the unquantified CF trade-off. R1 is more charitable toward the honest negative results framing but flags that low F1 (~8%) undermines practical relevance.

**R2→R1**: R2's core concern is novelty and scope — the grammar layer is engineering (XGrammar application), the semantic layer is a known technique applied to a new domain, and the landscape study is too narrow (2 datasets, 2 models) for a standalone empirical contribution. The 7-reference related work section is a significant gap.

**Shared concerns (both reviewers):**
1. CF trade-off unresolved — no downstream validation of the claim that DR reduction outweighs CF introduction
2. No post-hoc filtering baseline
3. Cross-model analysis incomplete and confounded (Llama parse rate, SciERC only)
4. DocRED semantic layer results are weak — 35.5% reduction at 39% overhead is questionable value

---

## Step 3: Convergence

### Points of Agreement
1. **Grammar layer is a clean, actionable result** — both reviewers agree this is the strongest finding, though R2 questions its novelty (engineering vs research).
2. **Honest negative results reporting is a strength** — both credit the transparent handling of DocRED limitations.
3. **CF trade-off is a genuine concern** — introducing new violations (up to 9.9%) while reducing others, without downstream validation, weakens the contribution.
4. **Experimental scope is narrow** — 2 datasets, 2 models (with Llama only partially tested), zero-shot only, single seed.
5. **Missing baselines** — post-hoc filtering and prompt-engineering with full ontology are natural baselines that should be included.

### Points of Disagreement
1. **Overall assessment**: R1 leans Weak Accept (the empirical findings + grammar layer are sufficient for a venue like EMNLP findings), R2 leans Weak Reject (each contribution individually is thin, and combined they don't reach the bar).
2. **Novelty threshold**: R1 views the violation taxonomy and tightness-DR analysis as genuine conceptual contributions; R2 views them as descriptive and shallow.
3. **Practical relevance of low F1**: R1 notes it as a weakness but accepts zero-shot as a valid experimental setting; R2 sees it as fundamentally undermining the paper's motivation.

### Consensus Position
Both reviewers agree the paper is **borderline** — below a strong accept threshold but not without merit. The grammar layer finding is clean and useful. The violation landscape analysis provides some value. The semantic layer is the weakest contribution (limited novelty, limited effectiveness on DocRED, introduces CF). The paper's main liabilities are: (1) narrow experimental scope with no variance estimates, (2) sparse related work, (3) no downstream evaluation, (4) thin novelty per contribution.

---

## Step 4: Consolidated Assessment

### Overall Score: 3 (Weak Reject)

### Justification

The paper addresses a relevant problem — ontology constraint violations in LLM-based IE — and does so with commendable transparency about negative results. The grammar-constrained decoding layer is a clean, actionable finding (ET→0%, RV→0%, 14% overhead, zero F1 cost) that any practitioner could adopt. The violation landscape analysis (tightness-DR correlation breakdown across ontology complexity) is a useful empirical observation.

However, the paper falls short of the acceptance bar for a top ML venue on multiple dimensions:

**1. Novelty is thin across all three contributions.** The grammar layer is a direct application of XGrammar with an ontology-to-grammar compiler — useful but engineering-level. The semantic layer applies known dynamic logit masking techniques to a new domain with limited effectiveness (35.5% on DocRED). The violation landscape study covers only 2 datasets and 1–2 models, which is narrow for a primary empirical contribution.

**2. Experimental rigor has significant gaps.** No variance estimates or confidence intervals on any metric. No post-hoc filtering baseline despite arguing against it theoretically. Cross-model analysis is incomplete (Llama tested only on SciERC unconstrained, with 92% parse rate confound). Single-seed, single-prompt results.

**3. The semantic layer introduces unvalidated trade-offs.** The 9.9% CF violation rate on SciERC and 2.99% on DocRED represent new errors introduced by the method. Without downstream evaluation (KG quality, QA accuracy), the claim that DR reduction outweighs CF introduction is unsupported. Entity duplication (85 instances on DocRED) is a newly identified side effect that further complicates the value proposition.

**4. Related work is insufficient.** Seven references is far below the standard for a top venue. Major omissions include structured prediction for IE, alternative constrained decoding methods (PICARD, Synchromesh, Guidance), schema-guided generation, and prior error analysis work in IE.

**5. Low absolute F1 (~8%) raises practical utility concerns.** The systems being analyzed are too weak for real deployment. The violation landscape and constraint effectiveness could look very different on a competitive extraction system (fine-tuned or few-shot).

**6. Positioning fragmentation.** The paper tries to be three things (empirical study, method paper, proof-of-concept) but none reaches sufficient depth individually. The landscape study needs more models/datasets/settings. The grammar method needs novelty beyond XGrammar application. The semantic proof-of-concept needs a clearer path forward.

### Recommendation

The paper would benefit from:
- Expanding to 3+ datasets and 3+ models (including larger models) for the landscape study
- Adding post-hoc filtering and prompt-engineering baselines
- Including variance estimates (multi-seed or bootstrap)
- Substantially expanding related work (20+ references minimum)
- Adding downstream evaluation (even a simple KG quality or QA accuracy measurement)
- Focusing the contribution: either commit to the landscape study (with much broader coverage) or commit to the grammar layer method (with stronger baselines and ablations)

The grammar layer finding alone, if better positioned with proper baselines and broader validation, could be a solid contribution to a workshop or findings track. The current manuscript's attempt to combine three partial contributions does not reach the threshold for a main conference paper.

### Scores Summary

| Criterion | Score |
|---|---|
| Novelty | 2.5/6 |
| Soundness | 3.5/6 |
| Significance | 3/6 |
| Clarity | 4/6 |
| Overall | 3/6 (Weak Reject) |

### Key Strengths (Final)
1. Grammar layer achieves universal ET/RV elimination with zero F1 cost — clean, actionable
2. Transparent reporting of negative results (DocRED degradation, tightness null result)
3. Well-defined violation taxonomy with decidability classification
4. The "grammar-only DR increase" insight (RV masking true DR) is analytically valuable

### Key Weaknesses (Final)
1. Thin novelty: XGrammar application + known masking technique + narrow landscape study
2. Missing baselines: no post-hoc filtering, no prompt-engineering with full ontology
3. No variance estimates on any metric
4. CF trade-off unvalidated downstream — method may trade one violation type for another
5. 7 references — far below venue standards; major related work gaps
6. Low F1 (~8%) undermines practical motivation
7. Incomplete cross-model analysis (Llama only partially tested, parse rate confound)
