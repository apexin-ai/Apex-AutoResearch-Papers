---
dream_id: dream_20260520T112859
tier: worst
overall_score: 2.5 — Borderline Findings
timestamp: 2026-05-20T12:24:30.243274+00:00
---

# Dream Review Report — Full Roundtable

**Paper**: "Not All Ambiguity Is Equal: Type-Specific Safety Vulnerabilities in LLM Agent Policies"
**Venue**: EMNLP 2026 (ARR)
**Review Mode**: Full (2 Reviewers + Roundtable)
**Date**: 2026-05-20

---

## Panel

| Role | Focus |
|------|-------|
| R1 | Methods, Experiments, Statistical Rigor |
| R2 | Novelty, Related Work, Excitement |

---

## Step 1 — Independent Reviews

### R1: Methods & Experiments

**Strengths**

1. **Appropriate causal design.** The matched-pair injection paradigm correctly isolates ambiguity as the causal variable. Each clause pair controls for semantic content, making the Δpp interpretable as an ambiguity effect. This is a genuine methodological advance over observational studies (DRIP-R, PolicyBank).

2. **Scale.** 2,400 episodes across 4 models and 6 types is a substantial experimental effort. The 300-pair stimulus set is large enough to support the pooled binary effect claim (+19.3pp, p < 1e-12) with confidence.

3. **Statistical toolkit is generally appropriate.** McNemar for within-pair binary comparisons, omnibus χ² with Cramér's V for type uniformity, Holm–Bonferroni for pairwise corrections, logistic regression with interaction terms — these are standard and correctly applied.

4. **Commendable transparency.** The paper honestly reports that 2/6 types fail Holm–Bonferroni, that ICC = 0.55 is moderate, that κ = 0.38 is fair, and that coreferential effects fall within the noise band. This candor is rare and appreciated.

**Weaknesses**

1. **Error analysis inter-annotator agreement (κ = 0.38) is below conventional thresholds.** Landis & Koch classify this as "fair" agreement, below the 0.67 threshold for reliable qualitative coding. The "arbitrary resolution" category (κ = 0.22) is barely above chance. Yet the failure mode taxonomy is claimed as Contribution #4. The paper's defense ("error analysis provides explanatory depth for patterns established by statistical analysis") is partially valid, but the taxonomy should be explicitly labeled as preliminary/exploratory, not as a standalone contribution.

2. **Two of six types fail Holm–Bonferroni correction.** Lexical (+11.0pp) and coreferential (+8.0pp) do not survive correction, yet the paper presents a "three-tier hierarchy" that includes them. The hierarchy is partially supported: the top tier ({auth_scope, scopal}) is robust, but the bottom tier is not statistically distinguishable from no effect after correction. The paper should frame the hierarchy as {reliably demonstrated: auth_scope, scopal, incompleteness, CP} vs. {tentative: lexical, coreferential}.

3. **Visibility effect is a null result presented misleadingly.** The pooled Δ = −4.5pp with p = 0.47 is not significant. The Qwen3-8B reversal makes it worse. Presenting this as a "capability-dependent" finding is post-hoc rationalization of a failed hypothesis. The paper should state clearly: "The visibility hypothesis was not supported."

4. **Moderate test-retest reliability (ICC = 0.55).** Coreferential ICC = 0.38 means its +8.0pp effect (CI [1.9, 14.1]) is within the noise band (mean |Δ| across replicates = 9.8pp). The effect may be real but cannot be reliably measured with this design.

5. **Realism validation is partial.** 2 of 5 KS tests fail: synthetic clauses are significantly longer (+4.8 tokens) and more deeply nested (+1.4 parse depth) than DRIP-R naturals. The argument that "longer context helps disambiguation, making estimates conservative" is speculative and untested. A length-matched subset analysis would strengthen this claim but is absent.

6. **Clause generation pipeline under-described.** "Multi-round pipeline with human validation" lacks critical details: how many annotators? What qualifications? Was generation manual or LLM-assisted? What revision criteria? The 36% revision rate for coreferential raises ecological validity concerns for that type — heavily revised stimuli may not represent natural coreferential ambiguity.

7. **Missing controls and baselines:**
   - No human baseline: How do human agents perform on the same ambiguous clauses?
   - No within-domain breakdown: Are effects consistent across retail vs. airline, or does one domain drive results?
   - No severity weighting: All violations treated as binary (a refund error = a data access violation).
   - No ablation on clause length: Critical given the realism validation failure on length/depth.
   - Temperature/sampling parameters for models not specified.
   - No power analysis for the visibility comparison or interaction tests.

8. **Incompleteness type confound.** Disambiguating incompleteness clauses necessarily adds information (filling what was absent). This creates a content confound absent from purely structural disambiguations (scopal, lexical). The Δpp for incompleteness (+20.0pp) conflates ambiguity removal with information addition. This is not addressed.

**R1 Scores:**
- Soundness: 3.0 / 5
- Reproducibility: 2.5 / 5

---

### R2: Novelty & Related Work

**Strengths**

1. **Timely research question.** With LLM agents increasingly deployed under natural language policies, understanding how specification quality affects safety is practically important. The question is well-motivated.

2. **Genuine conceptual bridge.** Connecting Berry & Kamsties' nocuous/innocuous distinction from requirements engineering to LLM agent contexts is a nice cross-disciplinary contribution. The argument that LLM agents lack shared organizational context (making all ambiguity nocuous) is sound.

3. **Actionable type hierarchy.** The top-tier finding — that authorization scope (+33.5pp) and scopal (+24.0pp) ambiguity are significantly more dangerous — provides concrete prioritization guidance for practitioners. This is the paper's most valuable contribution.

**Weaknesses**

1. **Critically thin related work (10 references).** This is far below EMNLP standards. Major missing lines of work include:
   - **Instruction-following robustness**: Zhou et al. 2023 (IFEval), Qin et al. 2024 (ToolBench). Ambiguity sensitivity is a special case of instruction robustness — the paper fails to position against this broader phenomenon.
   - **Prompt sensitivity**: Sclar et al. 2024, Lu et al. 2022. The documented prompt sensitivity of LLMs is directly relevant.
   - **Formal policy specification**: Work on structured policy languages (SEAL, constitutional AI constraints) that could bypass the ambiguity problem entirely.
   - **Broader agent safety benchmarks**: R-Judge, ToolEmu, InjecAgent. The paper cites only 4 agent safety works.
   - **Psycholinguistic processing in LLMs**: Futrell et al., Hu et al. on surprisal-based ambiguity resolution — relevant to the mechanistic claims.
   - **Vagueness in formal semantics**: Lassiter & Goodman 2017. The paper invokes Wasow et al. 2005 but does not engage with the ambiguity/vagueness distinction substantively.

2. **Low technical novelty.** The method is standard experimental design (matched-pair injection + standard statistical tests). No new model, algorithm, or evaluation framework. The taxonomy recombines prior categories from Li et al. [2024] and Massey et al. [2014]. The DeBERTa classifier PoC (F1 = 0.76) is minimal and would not stand alone.

3. **Overclaimed contributions:**
   - C3 (model×type interaction, r_s = 0.97): A Spearman correlation of 0.97 computed on n = 4 data points is statistically meaningless — almost any monotonic trend across 4 points produces r_s ≥ 0.80. This should not be presented as a finding.
   - C4 (failure mode taxonomy): κ = 0.38 makes this unreliable as a standalone contribution. The highest-κ modes (conflict paralysis 0.55, scope misapplication 0.52) are only "moderate."
   - C5 (detection-risk alignment): An observation on 6 data points (types), not a validated contribution. F1 = 0.76 is not deployable.

4. **Positioning issues.** The paper claims to be the "first causal, type-granularity study" but DRIP-R already examines type-specific effects of policy ambiguity on agent behavior. The distinction (decision quality vs. safety violations) is real but narrower than implied. The causal matched-pair design is a genuine advantage over DRIP-R, but the conceptual territory is shared.

5. **"Not All X Is Equal" is a familiar finding pattern** in NLP (not all attention heads, not all layers, not all data points). The application to agent safety ambiguity is new, but the intellectual template is well-worn.

**R2 Scores:**
- Excitement: 2.5 / 5
- Assessment: Borderline Findings (2.5)

---

## Step 2 — Cross-Sharing

**R1 → R2**: The core methodology is appropriate and the binary effect is solid, but execution weaknesses accumulate: low IAA, moderate reliability, partial realism validation, under-described generation pipeline, missing controls (human baseline, within-domain breakdown, severity weighting). The visibility hypothesis is a null result dressed up as a capability-dependent finding.

**R2 → R1**: The novelty is in the application domain, not the method. Ten references is unacceptable for EMNLP. The r_s = 0.97 on n = 4 claim is statistically vacuous. The paper overclaims on 3 of 5 contributions (C3, C4, C5). The related work misses several important connections that would better position the work.

---

## Step 3 — Convergence

### Areas of Agreement (both reviewers)

1. **Binary effect (+19.3pp) is the paper's strongest, most reliable finding.** The matched-pair design, large N, and highly significant p-value make this robust.
2. **Top-tier type hierarchy is supported.** Authorization scope (+33.5pp) and scopal (+24.0pp) surviving Holm–Bonferroni and showing high ICC (0.67, 0.58) is a credible empirical finding with practical value.
3. **κ = 0.38 for error analysis is a major weakness.** This undermines Contribution #4. The taxonomy should be explicitly exploratory.
4. **2/6 types failing Holm–Bonferroni weakens the hierarchy claim.** The "three-tier" framing overclaims — the bottom tier is not reliably distinguished from noise.
5. **Visibility effect is a null result (p = 0.47).** Reframing as "capability-dependent" is post-hoc.
6. **10 references is far too thin** for an EMNLP submission. Multiple important lines of work are missing.
7. **ICC = 0.55 is moderate.** Coreferential (ICC = 0.38) effects are within the noise band.
8. **Only 2 domains (retail, airline)** limits generalizability claims.
9. **Honest limitations section** is appreciated.

### Areas of Divergence

- **R2 is harsher on novelty** (low technical novelty, familiar finding pattern) while **R1 gives more credit** to the causal design as a methodological contribution.
- **R1 identifies the incompleteness confound** (disambiguating adds information) which R2 did not flag; both agree it's a real concern.
- **R2 is harsher on overall assessment** (2.5 Borderline Findings) while R1's scores are marginally more generous (Soundness 3.0).

### Resolution

Both reviewers agree the paper falls in the **Borderline Findings** to **Findings** range. The binary effect and top-tier type hierarchy are genuine contributions, but the accumulation of weaknesses (thin references, overclaimed contributions, low IAA, moderate reliability, null visibility result, 2-domain limitation, partial realism validation) prevents a Main conference recommendation. The consensus converges at **2.5–3.0**.

---

## Step 4 — Consolidated Assessment

### Summary
The paper presents the first causal study of how different ambiguity types in LLM agent policy specifications differentially affect safety violation rates. Using a matched-pair design with 300 clause pairs across 6 types, 4 models, and 2,400 episodes, it demonstrates a significant overall binary effect (+19.3pp) and a partially supported type hierarchy where authorization scope and scopal ambiguity are reliably the most dangerous.

### Consolidated Strengths

1. **Sound causal design.** The matched-pair paradigm correctly isolates ambiguity as the causal variable. This is a clear advance over the observational approaches in DRIP-R and PolicyBank.
2. **Robust top-tier findings.** Authorization scope (+33.5pp, ICC = 0.67) and scopal (+24.0pp, ICC = 0.58) effects are statistically significant, survive multiple comparison correction, and show acceptable test-retest reliability. These provide actionable guidance.
3. **Substantial experimental scale.** 2,400 episodes across 4 models spanning API and open-source is thorough.
4. **Transparent reporting.** The paper honestly discloses weaknesses (Holm–Bonferroni failures, moderate ICC, low κ, coreferential noise band). This candor is commendable.

### Consolidated Weaknesses

1. **[Critical] Error analysis reliability (κ = 0.38) undermines Contribution #4.** "Arbitrary resolution" (κ = 0.22) is essentially unreliable. The failure mode taxonomy is claimed as a core contribution but does not meet conventional reliability thresholds. Should be reframed as exploratory.

2. **[Major] 2 of 6 types fail Holm–Bonferroni.** Lexical (+11.0pp) and coreferential (+8.0pp) are not individually significant after correction. The "three-tier hierarchy" overclaims: the bottom tier is indistinguishable from noise. The hierarchy should be presented as {reliably dangerous: auth_scope, scopal} > {moderately dangerous: incompleteness, CP} > {tentative/unresolved: lexical, coreferential}.

3. **[Major] Critically thin related work (10 references).** Missing instruction-following robustness, prompt sensitivity, formal policy specification, broader agent safety benchmarks, psycholinguistic ambiguity processing, and formal semantics of vagueness. This is well below EMNLP standards and weakens the paper's positioning.

4. **[Major] Visibility hypothesis is a null result.** Pooled Δ = −4.5pp, p = 0.47 is non-significant. Qwen3-8B reverses the direction. The paper reframes this as "capability-dependent" but this is post-hoc rationalization. Should be stated plainly as: "The visibility hypothesis was not supported in pooled analysis."

5. **[Moderate] r_s = 0.97 on n = 4 is statistically meaningless.** The model×type interaction χ² test (p = 0.001) is valid, but the Spearman correlation presented as headline evidence for Contribution #3 is computed on 4 data points. Almost any monotonic trend across 4 points yields high r_s.

6. **[Moderate] Moderate reliability (ICC = 0.55).** Coreferential ICC = 0.38 means its +8.0pp effect falls within the noise band (mean |Δ| across replicates = 9.8pp). Lexical ICC = 0.44 is also concerning.

7. **[Moderate] Ecological validity partially validated.** Synthetic clauses are significantly longer and more deeply nested than DRIP-R naturals (2/5 KS tests fail). No length-matched robustness check is provided.

8. **[Minor] Clause generation under-described.** Number of annotators, qualifications, generation method (manual vs. LLM-assisted), and revision criteria are missing. Coreferential's 36% revision rate raises ecological validity concerns specific to that type.

9. **[Minor] Missing controls.** No human baseline, no within-domain breakdown (retail vs. airline), no severity weighting, no power analysis for secondary hypotheses.

### Questions for Authors

1. How were clauses generated? Manual, LLM-assisted, or hybrid? How many validators and what were their qualifications?
2. Can you provide a length-matched subset analysis to address the ecological validity concern?
3. For the incompleteness type, what is the mean token-count delta between ambiguous and unambiguous variants? Does disambiguating incompleteness clauses add substantially more information than disambiguating other types?
4. Are the binary effects consistent across retail vs. airline domains, or does one domain drive results?
5. What temperature/sampling parameters were used for each model?

### Scores

| Dimension | Score | Justification |
|-----------|-------|---------------|
| Soundness | 3.0 | Core matched-pair design is sound; undermined by low IAA (κ=0.38), moderate ICC (0.55), overclaimed hierarchy (2/6 fail correction), null visibility result framed misleadingly |
| Excitement | 2.5 | Timely question with practical value; top-tier type hierarchy is useful; but "not all X is equal" pattern is familiar, technical novelty is low, and key findings are partially supported |
| Reproducibility | 2.5 | Clause generation pipeline under-described; temperature parameters missing; ICC=0.55 raises concerns; no dataset release commitment |
| Overall | 2.5 | Borderline Findings |

### Overall Assessment: 2.5 — Borderline Findings

**Rationale**: The paper addresses a timely question with an appropriate causal design and finds a robust binary effect (+19.3pp) with a partially supported type hierarchy. Authorization scope and scopal ambiguity are reliably identified as the most dangerous types — this is a genuine empirical contribution with practical value. However, the paper is weakened by: (a) overclaiming on 3 of 5 contributions (C3 r_s on n=4, C4 at κ=0.38, C5 as PoC); (b) critically thin related work (10 references); (c) a null visibility result presented as a capability-dependent finding; (d) 2 of 6 types not surviving multiple comparison correction; and (e) moderate reliability undermining per-type claims. With substantially expanded related work, honest reframing of the hierarchy and visibility claims, and improved or downgraded error analysis, this could reach Findings quality in a revision cycle.

### Actionable Revision Recommendations (Priority Order)

1. **Expand references to ≥25.** Add instruction-following robustness, prompt sensitivity, formal policy specification, broader agent safety benchmarks, and psycholinguistic ambiguity processing literature.
2. **Reframe type hierarchy honestly.** Present as {reliably demonstrated: auth_scope, scopal, incompleteness, CP} vs. {tentative: lexical, coreferential}. Remove the three-tier framing or clearly caveat the bottom tier.
3. **Reframe visibility as null result.** State plainly that the hypothesis was not supported. The capability-dependent observation can be noted as an exploratory post-hoc finding.
4. **Downgrade failure mode taxonomy from contribution to supplementary analysis.** At κ = 0.38, this cannot be a headline finding. Focus on high-κ modes (conflict paralysis, scope misapplication) as reliable observations.
5. **Remove r_s = 0.97 from headline claims.** The interaction χ² (p = 0.001) is valid evidence; the rank correlation on n = 4 is not.
6. **Add length-matched subset analysis** for realism validation.
7. **Provide clause generation details.** Annotator count, qualifications, generation method, revision criteria.
8. **Report within-domain breakdown** (retail vs. airline) to assess generalizability within the available data.
9. **Check page limit.** Main text (§1–§10) appears to extend to ~9 pages, exceeding the 8-page limit for EMNLP 2026 long papers.
