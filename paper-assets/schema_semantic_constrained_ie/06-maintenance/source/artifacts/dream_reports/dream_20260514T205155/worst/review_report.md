---
dream_id: dream_20260514T205155
tier: worst
overall_score: borderline reject
timestamp: 2026-05-14T21:49:47.974901+00:00
---

# Dream Review Report: OntoCoDec

**Paper:** "OntoCoDec: Near-Complete Type-Valid Information Extraction via Compiled Ontology Constraints"
**Venue:** EMNLP 2026 (ACL Rolling Review)
**Review Mode:** Full (2 Reviewers + Roundtable)
**Date:** 2026-05-14

---

## Venue Calibration

EMNLP 2026 submissions go through ACL Rolling Review. Scoring uses a 1–5 scale with half-point increments:
- 5 = Award-worthy (top 2.5%)
- 4 = Largely complete, minor revisions
- 3 = Major revisions needed
- 2 = Significant revisions / resubmit next cycle
- 1.5 = Resubmit after next cycle
- 1 = Not publishable at *ACL

Three dimensions scored: Soundness, Excitement, Overall Assessment. EMNLP 2025 acceptance rate was ~26% for main conference.

---

## Paper Summary

The paper addresses ontology constraint violations in LLM-based zero-shot information extraction. It makes two main contributions: (1) a **violation landscape study** measuring domain/range (DR), relation vocabulary (RV), entity type (ET), and cross-field consistency (CF) violations on SciERC (7 relations) and DocRED (96 relations); (2) **OntoCoDec**, a framework that compiles IE ontology schemas into two composable constrained-decoding layers — a grammar layer (XGrammar CFG for JSON/vocabulary enforcement) and a semantic layer (stateful entity registry + dynamic logit masking for domain/range constraints). On SciERC, DR violations drop 94% (15.4%→0.93%) with neutral F1; on DocRED, 45% (Qwen) to 90% (Llama). The method introduces cross-field consistency violations (2.6–12.0%) as a trade-off.

---

## Experiment Coverage Assessment

The paper covers experiments P001–P016 and P018–P019 from the full experiment plan. P017 (50-doc pilot) was superseded by the full S2 evaluation. P020 was killed/superseded. All major planned experiments are reported. The paper's experimental matrix (2 models × 2 datasets × 5 configurations + post-hoc baseline + bootstrap CI) is comprehensive for the claims made.

---

## Reviewer 1 (R1): Methods and Experiments

### Strengths

**S1: Violation landscape study is a genuine empirical contribution.** No prior work systematically quantifies per-relation ontology constraint violation distributions in LLM-based IE. The finding that SciERC (7 relations, DR=15.4%) and DocRED (96 relations, DR=18.7%) show comparable violation rates despite 14× ontology size difference — with constraint tightness as the predictor — is non-obvious. The Evaluate-for regression (+5.8pp under schema-informed prompting) concretely demonstrates prompt-level unreliability.

**S2: Clean and informative ablation design.** The 5-way ablation (unconstrained / grammar-only / semantic-only / full S1 / full S2) cleanly isolates each layer's contribution. The enabling dependency finding — grammar-only barely changes DR (15.4%→14.8%), semantic-only achieves 24% reduction, but the combination reaches 94% — is well-demonstrated with sound mechanistic explanation. Grammar-only DR *increase* on DocRED (18.5%→26.2%) is a particularly informative result.

**S3: Commendable transparency.** The paper honestly reports: CF elevation to 9.9–12.0%, S2 failing to solve CF, post-hoc filtering achieving higher F1, DocRED scalability gap, and parse failure increases. This disclosure level is rare.

**S4: Cross-model validation with mechanistic explanation.** The 2×2 matrix (2 models × 2 datasets) with the dual-factor model (tightness × RV baseline) explaining Qwen DR↓45% vs Llama DR↓90% on the same ontology is analytically insightful.

**S5: Bootstrap significance testing with honest framing.** Per-dataset significance reporting (SciERC: +0.13pp, p=0.58; DocRED: +0.50pp, p<0.001) with mechanistic attribution is methodologically correct.

**S6: Post-hoc baseline comparison is multi-dimensional.** The comparison across recall, information coverage, and entity-type residuals is legitimate, not just F1.

### Weaknesses

**W1 [Major]: "Near-complete" title claim not supported by DocRED results.** Qwen DocRED retains 10.2% residual DR — more than 1 in 10 triples still violates domain/range constraints. Combined with CF=2.6%, ~13% of triples have some violation. The title is defensible for SciERC (0.93% residual) and Llama-DocRED (2.55%), but misleading for Qwen-DocRED. The paper's own dual-factor explanation makes clear effectiveness is highly contingent on model-specific vocabulary compliance.

**W2 [Major]: CF trade-off is substantial and severity distinction lacks empirical validation.** CF rises from 0.08% to 9.9% on SciERC (Qwen) and to 12.0% on DocRED (Llama). The paper frames DR as "hard" and CF as "soft," but this distinction is entirely unvalidated — no downstream experiment demonstrates CF violations are less harmful. The monotonic increase across enforcement aggressiveness (unconstrained 0.08% → semantic-only 2.71% → full S1 9.90%) suggests this is a systematic consequence that will worsen with more constraints.

**W3 [Major]: Evaluation operates at ~8% R-F1 — practical value unclear.** At ~8% R-F1, ~92% of extracted triples are incorrect. Constraints primarily operate on *wrong* triples — ensuring ontological well-formedness of factually incorrect extractions. No experiment validates whether violation rates transfer to the higher-F1 regime (fine-tuned models), or whether the dual-factor model's predictions hold there.

**W4 [Moderate]: Fallback rate / residual DR near-identity may be tautological.** The near-identity between fallback rate (10.2%) and residual DR (10.21%) on DocRED may be a mathematical consequence of system design rather than an empirical finding — if every fallback event implies a DR violation, the relationship is definitional.

**W5 [Moderate]: Limited technical novelty — domain transfer of code-generation constrained decoding.** The core mechanism (compiling type constraints into token-level logit masks with a stateful processor) transfers techniques from code generation (PICARD, Synchromesh). IE ontology constraints (flat domain/range sets over 6 entity types) are structurally simpler than what prior systems handle. The entity registry is a dictionary; mask composition is bitwise AND.

**W6 [Moderate]: Semantic-only worsens ET violations on DocRED (2.5%→4.2%).** This negative interaction — partial constraint application increasing a different violation type — is reported but underexplored. Practitioners cannot safely deploy the semantic layer alone.

**W7 [Minor]: Tightness-violation correlation on SciERC rests on 7 data points.** DocRED's 96 relations would provide far stronger evidence; the full tightness-DR scatter for DocRED is not reported.

**W8 [Minor]: Parse failure increase not well-analyzed.** Llama-DocRED parse failures increase 6.8%→9.1% under constraints. Since failures are excluded from F1/violation calculations, this creates potential selection bias.

### R1 Questions for Authors

1. Is the fallback→DR relationship definitional or empirical? What fraction of fallback events do NOT produce DR violations?
2. Have you estimated violation rates for fine-tuned IE systems? If fine-tuned models already have low DR, the practical motivation narrows.
3. What mechanism causes semantic-only to increase ET violations on DocRED?
4. Have you checked gold-standard type consistency for the dominant CF conflict patterns (Generic↔OtherScientificTerm)?
5. Why not evaluate a combined OntoCoDec + post-hoc approach?

### R1 Scores

| Dimension | Score |
|-----------|-------|
| Soundness | 3.5 |
| Excitement | 2.5 |
| Overall | 3.0 |
| Confidence | 4 |

---

## Reviewer 2 (R2): Novelty and Related Work

### Strengths

**S1: Problem identification is well-motivated and concrete.** The four-category violation taxonomy (DR, RV, ET, CF) is clear and actionable. Per-relation breakdown (Compare at 42.4% vs. Used-for at 0.8%) makes a compelling case that violations are non-uniform.

**S2: Paper is honest about limitations.** Proactive reporting of CF trade-off, post-hoc outperformance, S2 failure, and qualification of title as "Near-Complete" rather than "Guaranteed."

**S3: Cross-model validation is genuine positive.** Zero code modification across Qwen and Llama with consistent structural guarantees (RV/ET→0%).

**S4: Constraint tightness formalization is useful.** τ(r) = 1 − |dom(r)|·|rng(r)|/|E|² predicting fallback frequency and residual DR is a clean analytical insight.

**S5: Related work coverage is extensive** (in appendix, ~25+ references covering 5 paradigms).

### Weaknesses

**W1 [Major]: Grammar layer is not novel — it is an application of XGrammar.** Compiling a JSON schema with enum constraints into an XGrammar CFG is exactly what XGrammar, Outlines, and LMQL were designed for. Any practitioner using XGrammar with a properly specified JSON schema would achieve RV=0% and ET=0%. Framing this as a "contribution layer" overstates novelty.

**W2 [Major]: Semantic layer is a lookup table with logit masking — novelty is narrow.** Core mechanism: parse prefix to detect JSON field, look up relation in constraint table, mask disallowed entity-type logits to -inf. Each component is individually straightforward. The first-token masking approach works only because type vocabularies are very small (6 types); scalability to hundreds of types is undiscussed.

**W3 [Major]: "Near-complete" in title not justified.** DocRED Qwen: DR drops from 18.5% to only 10.2% — 45% reduction, 10.2% residual. One in ten triples still violates constraints. The headline 94% comes from SciERC (7 relations, loose constraints). The more realistic benchmark directly contradicts the "near-complete" framing.

**W4 [Major]: Violation landscape study is an incremental observation.** Running an LLM on IE benchmarks and counting schema violations is a straightforward measurement. The tightness correlation is intuitive (tighter constraints are harder to satisfy by chance). This motivates the method but does not constitute a standalone contribution.

**W5 [Major]: CF trade-off undermines core value proposition.** Net effect on SciERC: −14.4pp DR, +9.8pp CF. The paper argues DR is "harder" than CF, but provides no empirical evidence (e.g., downstream task impact). For KG construction, cross-field inconsistency can be equally problematic.

**W6 [Moderate]: Post-hoc filtering outperforms on F1.** SciERC: 8.63 vs 8.36; DocRED: 9.61 vs 8.23. A simple generate-then-filter baseline outperforms the proposed method on the standard metric. The rebuttal relies on recall/coverage arguments that are marginal in a ~8% F1 regime.

**W7 [Moderate]: Missing related work and insufficient differentiation.** Key gaps:
- **Guidance library** (Microsoft): Supports stateful token masking conditioned on generation history — functionally similar to OntoCoDec's semantic layer.
- **InstructUIE** (Wang et al., 2023): Instruction-tuned universal IE combinable with constrained decoding.
- **DeepKE** (Zhang et al., 2022): Schema-guided extraction toolkit.
- **Type-constrained KG completion** (Krompass et al., 2015; Jain et al., 2018): Domain/range type restriction during KG operations — conceptually identical mechanism.
- **NeuroLogic Decoding** (Lu et al., 2021): Predicate logic constraints during beam search; semantic layer's masking is a special case.

**W8 [Minor]: Decidability taxonomy is relabeling.** "Local / prefix-decidable / non-local" restates standard formal language theory (regular / context-free / context-sensitive) applied to IE constraints. Not a novel taxonomy.

**W9 [Minor]: Experimental scope narrow.** 2 models (both 8B), zero-shot only, 2 datasets. No biomedical IE (where ontology compliance is most critical), no models >8B, no fine-tuned evaluation.

### R2 Questions for Authors

1. How does first-token masking scale to ontologies with hundreds of entity types? At what point does first-token uniqueness break down?
2. What does OntoCoDec provide beyond what a skilled engineer could build using Guidance/Outlines in an afternoon?
3. Have you measured downstream impact of DR reduction + CF increase on question answering or reasoning?
4. Grammar-only on DocRED increases DR from 18.5% to 26.2% — grammar makes things worse without semantic. How is grammar an "enabling prerequisite" when it is actively harmful alone?
5. Why lead with SciERC (easy, 7 relations) rather than DocRED (realistic, 96 relations)?

### R2 Scores

| Dimension | Score |
|-----------|-------|
| Soundness | 3.0 |
| Excitement | 2.5 |
| Overall | 2.5 |
| Confidence | 4 |

---

## Roundtable Discussion

### Step 2: Cross-Sharing

**R1 responding to R2:**

*Agreements:* Title overclaim (R2-W3 = R1-W1), CF trade-off severity (R2-W5 = R1-W2), experimental scope partially (R2-W9).

*Disagreements:*
- R2-W1/W2 (novelty of individual layers): R1 finds this "overly reductive." The contribution is the *compilation pipeline* — automatically translating IE ontology axioms into composable decoder constraints — not the masking primitives. The enabling dependency between layers is a non-trivial design insight.
- R2-W4 (violation landscape as incremental): R1 "strongly disagrees." No prior work measured this; the SciERC-DocRED comparability despite 14× ontology size difference is genuinely informative.
- R2-W6 (post-hoc outperforms): R1 gives more credit to the multi-dimensional comparison; post-hoc discards 48.1% of triples including 127 true positives.
- R2-W8 (decidability taxonomy): R1 finds it "lightweight but not vacuous" — provides practitioners clear guidance.

*New insight adopted:* R2-W7 (missing related work) is well-taken, especially Guidance, NeuroLogic, and type-constrained KG completion.

**R1 final scores: Soundness 3.5, Excitement 2.5, Overall 3.0 (unchanged).**

---

**R2 responding to R1:**

*Agreements:* Title framing (R1-W1), CF severity (R1-W2), limited novelty (R1-W5), tightness on 7 points (R1-W7).

*Disagreements:*
- R1-S1 (violation landscape as short-paper-worthy): R2 remains skeptical — "tighter constraints produce more violations" is close to tautological without a predictive model.
- R1-S4 (dual-factor model as insightful): R2 questions whether fallback→DR relationship is definitional rather than empirical.
- Soundness gap (R1: 3.5 vs R2: 3.0): R2's lower score reflects unvalidated CF severity distinction and potential fallback/DR tautology.

*New insights adopted:*
- R1-W6 (semantic-only worsening ET on DocRED) — a fragility R2 had underweighted.
- R1-Q6 (combined OntoCoDec + post-hoc) — a natural untested combination.

**R2 final scores: Soundness 3.0, Excitement 2.5 (↑ from 2.0), Overall 2.5 (unchanged).**

### Step 3: Convergence Summary

| Dimension | R1 | R2 | Mean | Consensus |
|-----------|----|----|------|-----------|
| Soundness | 3.5 | 3.0 | 3.25 | Methodology is strong; deductions for unvalidated CF severity distinction and low-F1 regime |
| Excitement | 2.5 | 2.5 | 2.5 | Empirical contributions have value; technical novelty is moderate at best |
| Overall | 3.0 | 2.5 | 2.75 | Borderline — strong Findings candidate, below main conference threshold |
| Confidence | 4 | 4 | 4 | Both reviewers are domain-knowledgeable |

**Converged points (both reviewers agree):**
1. "Near-complete" title is not supported by DocRED results — **must be revised**
2. CF trade-off (up to 12%) is the paper's central unresolved weakness — severity distinction requires empirical validation
3. Zero-shot ~8% F1 regime limits practical impact claims
4. Cross-model validation and honest reporting are clear strengths
5. Post-hoc filtering outperforming on F1 is a presentational challenge, though multi-dimensional comparison has merit
6. Missing related work (Guidance, type-constrained KG completion, NeuroLogic) is addressable

**Remaining divergences:**
1. Violation landscape as contribution: R1 sees it as potentially short-paper-worthy; R2 sees it as incremental. *AC note: The truth is between — it is a useful empirical contribution but not sufficient as a standalone claim.*
2. Dual-factor model: R1 finds it analytically insightful; R2 suspects it may be partially tautological. *AC note: The relationship between fallback rate and residual DR needs decomposition to resolve this.*
3. Technical novelty of the compilation pipeline: R1 gives moderate credit to the systems contribution; R2 sees it as engineering combination. *AC note: The novelty is real but narrow — the IE-specific insight (enabling dependency between grammar and semantic layers) is sound but the individual mechanisms are established.*

---

## Step 4: AC Synthesis and Recommendation

### Overall Assessment: **2.75 → Borderline Reject / Strong Findings Candidate**

This paper makes a genuine empirical contribution to an understudied problem (ontology constraint violations in LLM-based IE) and proposes a technically sound solution with thorough evaluation. The violation landscape study, cross-model validation, and honest reporting of negative results are commendable. However, multiple major issues prevent recommendation for the main conference:

**Critical Issues:**
1. **Title overclaim.** "Near-Complete Type-Valid IE" is contradicted by Qwen-DocRED retaining 10.2% residual DR + 2.6% CF. The title must be qualified or the contribution reframed.
2. **CF as net-neutral trade-off.** On SciERC: −14.4pp DR, +9.8pp CF. The paper argues these are different severity levels but provides no downstream evidence. A reviewer who doesn't accept the severity distinction sees the method as redistributing violations rather than eliminating them.
3. **Low-F1 regime.** At ~8% R-F1, constraints primarily operate on incorrect triples. Without validation on fine-tuned models or downstream tasks, practical significance is unclear.
4. **Limited technical novelty.** The grammar layer is an XGrammar application; the semantic layer is a constraint lookup table with logit masking. The compilation pipeline and enabling dependency are sound engineering contributions but not conceptually novel relative to code-generation constrained decoding (PICARD, Synchromesh).
5. **Post-hoc baseline outperforms on F1.** A trivial baseline achieves higher F1 on both datasets.

**Strengths That Support Findings:**
1. First systematic violation measurement with actionable tightness analysis
2. Thorough ablation isolating each layer's contribution
3. Cross-model generalization without code modification
4. Honest, transparent reporting of limitations

### Actionable Revision Recommendations

1. **Revise title** to remove "Near-Complete" or scope it to specific configurations
2. **Add downstream task evaluation** (e.g., KG-based QA) to validate that DR reduction + CF increase yields net benefit
3. **Evaluate on at least one fine-tuned model** to demonstrate practical relevance beyond zero-shot
4. **Decompose fallback-DR relationship** to confirm it is empirical rather than definitional
5. **Add missing related work** (Guidance, NeuroLogic, type-constrained KG completion, InstructUIE)
6. **Test combined OntoCoDec + post-hoc** pipeline to address residual violations
7. **Report full tightness-DR scatter** on DocRED's 96 relations to strengthen the tightness hypothesis
8. **Reframe contributions**: position grammar layer as off-the-shelf application, center novelty on semantic layer + compilation pipeline + empirical analysis

### Final Scores

| Dimension | R1 | R2 | AC Consensus |
|-----------|----|----|-------------|
| Soundness | 3.5 | 3.0 | **3.0** |
| Excitement | 2.5 | 2.5 | **2.5** |
| Overall | 3.0 | 2.5 | **2.5** |
| Confidence | 4 | 4 | **4** |

**Recommendation:** Reject for main conference. The paper is a strong candidate for **Findings of EMNLP 2026** if the title is corrected and the CF severity distinction is supported with evidence. In its current form, the combination of limited novelty, CF trade-off, low-F1 evaluation regime, and post-hoc baseline outperformance places it below the acceptance threshold for the main conference (~top 26%).
