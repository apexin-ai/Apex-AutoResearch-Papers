---
dream_id: dream_20260514T205155
tier: median
overall_score: borderline — Findings acceptance (3.0/5)
timestamp: 2026-05-14T21:41:12.367118+00:00
---

# Dream Review Report: OntoCoDec

**Paper**: OntoCoDec: Near-Complete Type-Valid Information Extraction under Single-Relation Scope via Compiled Ontology Constraints
**Venue**: EMNLP 2026 (ARR scoring)
**Review Mode**: Full (2 Reviewers, 4-step roundtable)
**Dream ID**: 20260514T205155

---

## Roundtable Process

- **R1** (Methods + Experiments focus): Soundness 3.5, Excitement 3.0, Overall 3.5, Confidence 4
- **R2** (Novelty + Related Work focus): Soundness 3.5, Excitement 2.5, Overall 3.0, Confidence 4
- **Cross-examination**: Conducted in Steps 2-3. Key agreements and divergences documented below.

---

## Consolidated Scores (ARR 1–5 scale, half-point increments)

| Dimension | R1 | R2 | Consensus |
|-----------|----|----|-----------|
| Soundness | 3.5 | 3.5 | **3.5** |
| Excitement | 3.0 | 2.5 | **2.5** |
| Overall | 3.5 | 3.0 | **3.0** |
| Confidence | 4 | 4 | **4** |

**Headline**: Borderline — suitable for **Findings** track. The violation landscape study (§3) is a genuine empirical contribution; the OntoCoDec framework is technically sound but limited in novelty. The CF trade-off and DocRED weakness prevent main conference recommendation.

---

## Summary of the Paper

This paper presents the first systematic per-relation measurement of ontology constraint violations in LLM-based zero-shot information extraction, finding that domain/range (DR) violations affect 15–26% of generated triples and correlate with per-relation constraint tightness rather than ontology size. The authors propose OntoCoDec, which compiles IE ontology schemas into two composable constrained-decoding layers — a grammar layer (XGrammar CFG) eliminating vocabulary violations and a semantic layer (stateful entity registry + dynamic logit masking) enforcing domain/range constraints. On SciERC, DR drops from 15.4% to 0.93% (↓94%) with no F1 degradation; on DocRED, reduction ranges from 45–90% depending on model, with cross-field consistency (CF) violations of 9.9–12.0% identified as an inherent limitation.

---

## Consensus Strengths

### S1: Violation Landscape Study Is a Genuine Empirical Contribution (R1+R2 agree)
The per-relation violation analysis in §3 is novel and informative. The finding that DR violations concentrate on high-tightness relations (Compare 42.4% vs. Conjunction 0.0%, a 56× spread on SciERC) and that violation rates are comparable across SciERC (7 relations) and DocRED (96 relations) despite 14× ontology size difference provides actionable insight for the IE community. The schema-informed prompting experiment (Table 3) revealing that one relation type (Evaluate-for) *increases* violations under prompting (+5.8pp) is a striking negative result. Both reviewers agree this landscape study stands as an independent contribution regardless of OntoCoDec's merits.

### S2: Thorough and Transparent Ablation Design (R1+R2 agree)
The 4-way ablation (unconstrained / grammar-only / semantic-only / full S1) on two datasets with a cross-model validation (Llama-3.1-8B) is well-structured. The ablation cleanly demonstrates the enabling dependency: grammar-only DR barely changes (15.37%→14.84%), semantic-only achieves ↓24%, but full S1 achieves ↓94% — proving grammar is a prerequisite, not a redundancy. The S2 two-pass variant is honestly positioned as an ablation rather than over-sold as a CF solution. Document-level bootstrap CIs (10,000 iterations) provide appropriate statistical rigor.

### S3: Honest Negative Result Reporting (R1+R2 agree)
The paper is commendably transparent about its limitations: CF trade-off (9.9–12.0%), DocRED's weaker results (45% vs. 94% DR reduction for Qwen), the low-F1 regime caveat, grammar-only DR *increase* on DocRED (latent violations exposed), and the admission that post-hoc filtering achieves higher F1 in precision-focused scenarios. This intellectual honesty strengthens the paper's credibility.

### S4: Dual-Factor Model and Constraint Coverage Metric (R1+R2 agree)
The dual-factor analysis — DR reduction ceiling determined jointly by constraint tightness and model vocabulary compliance (RV baseline) — is analytically stronger than a naive single-factor story. The Constraint Coverage metric (SciERC CC≈89% vs. DocRED CC≈43%) successfully reframes the DocRED weakness from "the method doesn't work on complex ontologies" to "DR reduction scales predictably with coverage, which is determined by tightness × vocabulary compliance." This is a useful practitioner-facing diagnostic.

---

## Consensus Weaknesses

### W1 [Major]: CF Trade-Off Is Severe and Inadequately Resolved
**R1 position**: CF reaches 9.90% on SciERC and 12.02% on Llama-DocRED — the method trades one class of violations for another. The claim of "near-complete type-valid IE" is undermined when 1 in 10 entities has inconsistent typing. The §5.8 sub-type analysis (>90% EVR, root cause: type-system ambiguity) is a good start but insufficient: (a) no quantitative breakdown of ambiguity-driven CF vs. erroneous CF; (b) the severity distinction ("CF is softer than DR") is asserted but not empirically validated (e.g., what fraction of CF triples are actually usable in a downstream KG?); (c) the progression unconstrained 0.08% → semantic-only 2.71% → full S1 9.90% shows CF scales with constraint enforcement aggressiveness.

**R2 position**: Agrees. Additionally notes that CF=12.02% on Llama-DocRED suggests CF worsens with constraint complexity, raising concerns about applicability to real-world ontologies with hundreds of types.

**Consensus**: Major weakness. The paper needs either (a) a net violation analysis (DR eliminated vs. CF introduced, with severity weighting), or (b) a downstream evaluation showing CF triples remain usable, or at minimum (c) a rigorous breakdown of ambiguity-driven vs. erroneous CF with per-type-pair analysis.

### W2 [Major]: DocRED DR Reduction (45% for Qwen) Undermines Generality Claims
**R1 position**: The 2× variation between models on the same ontology (Qwen ↓45% vs. Llama ↓90%) contradicts model-agnostic framing. Residual DR=10.21% is substantial.

**R2 position**: Agrees. Notes that 10.21% residual DR combined with 2.57% CF means ~13% of triples still have some violation, which strains the "Near-Complete" title framing.

**Consensus**: Major weakness. The Constraint Coverage explanation is *plausible* but would benefit from direct evidence (e.g., tracing specific triples before/after grammar correction to verify the latent violation hypothesis). The title qualifier "under Single-Relation Scope" does not adequately communicate that effectiveness is also model-dependent and ontology-dependent.

### W3 [Moderate]: Limited Technical Novelty in the Framework
**R1 position**: The two-layer architecture is well-motivated and the enabling dependency insight is non-trivial, but the decidability taxonomy is a straightforward classification of three obvious cases rather than a deep formalism.

**R2 position**: Stronger critique — the core mechanism is domain transfer of code-generation constrained decoding (PICARD for SQL, Syncode/PLDI'25 for code) to a structurally simpler constraint system. The entity registry is a dictionary lookup; mask composition is standard bitwise AND. The novelty lies in the *problem identification* (violation landscape) more than the *solution*.

**Consensus**: Moderate weakness. The enabling dependency insight and the problem identification are the genuine intellectual contributions. The implementation, while clean and effective, is engineering-level novelty rather than algorithmic novelty. This is acceptable for Findings but limits main conference competitiveness.

### W4 [Moderate]: Narrow Evaluation Scope
- **Two models only** (Qwen3-8B, Llama-3.1-8B) — both 8B parameter, open-weight. No proprietary models, no larger models, no fine-tuned models.
- **Two datasets only** (SciERC, DocRED) — one small/simple, one large/complex. No mid-range ontology.
- **Zero-shot only** — the interaction between constraint enforcement and few-shot/fine-tuned extraction quality is an open question explicitly acknowledged but not explored.
- **Low-F1 regime** (R-F1 ≈ 2–8%) — constraint violations may matter less when extraction quality is already very low. The §5.6 discussion ("even small absolute F1 changes are non-trivial relative effects") is fair but does not resolve whether the method remains useful at higher F1 levels.

### W5 [Minor]: Thin Related Work / Missing References
**R2 identified gaps**:
- **Constrained decoding**: PICARD (Scholak et al., 2021) for SQL, Synchromesh (Poesia et al., 2022), SynCode (Ugare et al., 2024) — already cited but differentiation with PICARD/Synchromesh could be sharper.
- **LLM-based IE (2024–2025)**: TANL, REBEL, GoLLIE, and more recent zero-shot IE papers are missing.
- **Neuro-symbolic constraint literature**: DeepProbLog, Semantic Loss Functions, posterior regularization — these enforce semantic constraints during neural generation and are conceptually related.
- **KG embedding type constraints**: TransE/DistMult with type constraints (Krompass et al., 2015; Jain et al., 2018) address the same problem from an embedding perspective.
- **Schema-guided dialogue**: SGD (Rastogi et al., 2020) and related work on schema-conditioned generation.

**R1 concurs** that 9 references is unusually thin for EMNLP. Even accounting for page limits, the related work section should engage with at least 15–20 references.

---

## Points of Reviewer Divergence

### D1: Overall Recommendation
- **R1** (3.5): Leans toward borderline accept based on the strong ablation design, the violation landscape contribution, and the transparent analysis. Views the framework as a solid engineering contribution with the enabling dependency as a non-trivial insight.
- **R2** (3.0): Leans toward Findings based on limited technical novelty. Views the primary contribution as the empirical landscape study, with the framework as enabling infrastructure.
- **Resolution**: Consensus at **3.0 (Findings)**. The empirical contributions are solid but the novelty profile fits Findings better than main conference. With a stronger related work section and CF resolution, the paper could move to 3.5.

### D2: Decidability Taxonomy
- **R1**: Useful organizational framework, slightly overstated as a "contribution."
- **R2**: Restates obvious properties of autoregressive generation; not a standalone contribution.
- **Resolution**: The taxonomy is *useful exposition* but should not be framed as a primary contribution. It provides a principled boundary for what constrained decoding can and cannot enforce, which has pedagogical value.

---

## Questions for Authors

1. **CF severity validation**: Can you provide evidence that CF-violating triples are actually usable in downstream KG population? What fraction of CF instances represent genuine type ambiguity (where both types are defensible) vs. clear errors?

2. **Latent DR hypothesis**: For the DocRED grammar-only DR *increase* (18.46%→26.17%), can you trace a sample of grammar-corrected triples to show that OOV relation names were indeed hiding DR violations? This would strengthen the dual-factor claim considerably.

3. **Constraint Coverage predictive power**: You report CC≈89% (SciERC) and CC≈43% (DocRED). Can CC be computed *before* running the full pipeline (from the grammar alone + a small calibration set)? If so, this becomes a genuinely useful pre-deployment diagnostic.

4. **F1 regime sensitivity**: Have you considered running OntoCoDec on a few-shot or instruction-tuned model to test whether constraint enforcement effects persist at higher F1 levels? Even a small experiment (e.g., 5-shot on SciERC) would significantly strengthen the paper.

5. **Post-hoc F1 advantage**: Post-hoc filtering achieves higher F1 than OntoCoDec (Table 8). Can you clarify why — is it because post-hoc also removes CF-violating triples that happen to be false positives, giving it a precision advantage that OntoCoDec's streaming approach cannot match?

6. **Tightness-violation correlation**: The correlation between tightness and DR rate on SciERC is based on only 5–7 data points (relations). Have you tested whether this holds on DocRED's 96 relations? A scatter plot with 96 points would be far more convincing than one with 7.

---

## Recommendations for Revision

1. **Title**: "Near-Complete" is misleading given DocRED results (10.21% residual DR, Qwen) and CF rates (up to 12%). Consider: "Toward Type-Valid Information Extraction via Compiled Ontology Constraints" or keep "under Single-Relation Scope" but add "with Model-Dependent Effectiveness."

2. **CF analysis**: Add a net violation analysis — total violations before (DR+RV+ET) vs. after (residual DR + CF). Show that the net violation count decreases even accounting for CF. Validate the severity distinction with a downstream evaluation or at least a manual annotation of CF instances.

3. **Related work**: Expand to at least 15–20 references. Add PICARD, Synchromesh, TANL/REBEL, recent 2024–2025 zero-shot IE papers, and neuro-symbolic constraint enforcement literature. Sharpen differentiation: what makes IE ontology constraints harder than SQL/code constraints?

4. **DocRED evidence**: Add a triple-level tracing analysis for the latent DR hypothesis (sample 50–100 grammar-corrected triples, show before/after). This would convert the dual-factor explanation from "plausible" to "empirically validated."

5. **Tightness correlation**: Show the scatter plot on DocRED (96 relations) in addition to SciERC. If the correlation holds at scale, this substantially strengthens the landscape study. If it doesn't hold, discuss why (confounds: relation frequency, entity type distribution).

6. **Reframe contributions**: Position the violation landscape study as the primary novel contribution, with OntoCoDec as a demonstration that these violations are addressable via constrained decoding. This framing better matches the actual novelty profile.

---

## Experiment Coverage Assessment

Comparing the paper against the experiment design (review_context.yaml, 20 planned experiments):

| Experiment | Status in Paper | Notes |
|---|---|---|
| P001 (SciERC minimal) | ✅ Table 1, §3 | Complete |
| P002 (SciERC schema-informed) | ✅ Table 3, §3 | Complete |
| P003 (DocRED minimal) | ✅ Table 1, §3 | Complete |
| P004 (DocRED schema-informed) | ✅ Table 3, §3 | Complete |
| P005a (SciERC unconstrained baseline) | ✅ Table 4, §5.2 | Complete |
| P005 (SciERC grammar-only) | ✅ Table 4, §5.2 | Complete |
| P006 (SciERC semantic-only) | ✅ Table 4, §5.2 | Complete |
| P007 (SciERC full S1) | ✅ Table 4, §5.2 | Complete |
| P008 (SciERC full S2) | ✅ Table 4, §5.2 | Complete |
| P009 (DocRED unconstrained) | ✅ Table 5, §5.3 | Complete |
| P010 (DocRED grammar-only) | ✅ Table 5, §5.3 | Complete |
| P011 (DocRED semantic-only) | ✅ Table 5, §5.3 | Complete |
| P012 (DocRED full S1) | ✅ Table 5, §5.3 | Complete |
| P013 (Llama SciERC uncon) | ✅ Table 6, §5.4 | Complete |
| P014 (Llama SciERC S1) | ✅ Table 6, §5.4 | Complete |
| P015 (Llama DocRED uncon) | ✅ Table 6, §5.4 | Complete |
| P016 (Llama DocRED S1) | ✅ Table 6, §5.4 | Complete |
| P017 (S2 pilot) | ✅ Not in paper | Correct — superseded by full run |
| P018 (Post-hoc filtering) | ✅ Table 8, §5.5 | Complete |
| P019 (Bootstrap CI) | ✅ Table 9, §5.6 | Complete |
| P020 (DocRED Phase 0 R2) | ✅ Not in paper | Correct — killed experiment |

**Coverage**: 18/18 live experiments are in the paper. 2 correctly excluded (pilot, killed). Coverage is **complete**.

---

## Final Assessment

This paper makes a genuine empirical contribution through its violation landscape study, demonstrating that ontology constraint violations in LLM-based IE are systematic, tightness-driven, and not reliably addressable via prompting alone. The OntoCoDec framework is technically sound and the ablation design is exemplary in its thoroughness and honesty. However, the framework's technical novelty is moderate (domain transfer of constrained decoding), the CF trade-off (up to 12%) is a significant unresolved limitation, and the DocRED results show model-dependent effectiveness that complicates generality claims. The paper is below the threshold for EMNLP main conference but is a solid candidate for the **Findings** track, contingent on addressing the thin related work section and providing stronger CF analysis.

**Consensus recommendation: Overall 3.0 — Findings acceptance.**