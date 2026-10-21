---
dream_id: dream_20260522T111643
tier: best
overall_score: 3.5 — Borderline Conference
timestamp: 2026-05-22T11:58:39.286422+00:00
---

# Dream Review Report: "Not All Policy Ambiguity Is Equal"

**dream_id:** 20260522T111643 | **review_mode:** full | **venue:** EMNLP 2026 (ARR)

---

## 1. Paper Summary

This paper presents the first causal, type-granular, cross-model study of how policy ambiguity drives safety violations in LLM agents. Using a matched-pair design with 300 clause pairs spanning six ambiguity types (two-layer taxonomy: specification vs. linguistic), five architecturally diverse models are evaluated across 2,997 episodes on τ²-bench. Key findings:

- **C1 (Binary effect):** +34.0pp violation increase (OR=15.1, p<10⁻¹⁰⁰), replicated across all 5 models
- **C2 (Type hierarchy):** Three-tier structure — incompleteness (53.6%) > mid-cluster (36.8–42.8%) > coreferential (31.6%); V=0.137, power=0.993
- **C3 (Layer effect):** Specification > linguistic (+6.08pp, p=0.017), but within-judge fragile; honestly reported as "suggestive"
- **C4 (Model × type interaction):** Authorization scope range 52pp across models (Claude 12% → GPT-5.4 64%); χ²=31.02, p=3e-6
- **C5 (Failure modes):** Type-specific signatures; <5% ambiguity awareness ("ambiguity blindness")
- **Perturbation control:** Δ_perturb = −0.67pp (CI contains 0), confirming ambiguity-specific causation
- **Cross-benchmark:** SOPBench replication Δ=31.2pp across healthcare/banking with rule-based verifier
- **Reliability:** ICC=0.919; Judge calibration κ=0.87 (exceeds human inter-annotator κ=0.762)

---

## 2. Reviewer Scores Summary

| Dimension | R1 (Methods) | R2 (Novelty) | Consensus |
|-----------|:---:|:---:|:---:|
| Soundness | 3.5 | 4.0 | 3.5 |
| Excitement | 3.5 | 3.0 | 3.5 |
| Reproducibility | 3.0 | 4.0 | 3.5 |
| **Overall** | **3.5** | **3.5** | **3.5** |
| Confidence | 4 | 4 | — |

---

## 3. Step 1: Independent Reviews

### R1 (Methods + Experiments) — Score: 3.5

**Top strengths:** (1) Well-executed matched-pair design with strong internal validity. (2) Comprehensive perturbation control arm (Δ=−0.67pp vs. +34pp for ambiguity) — rarely done in agent safety evaluations. (3) Transparent handling of the incompleteness confound (logistic regression controlling for token delta, confound-free lower bound reported). (4) Multi-level reliability evidence (ICC=0.919, human-LLM κ=0.87, cross-judge McNemar calibration). (5) Appropriate claim calibration — C3 honestly downgraded to "suggestive" despite nominal significance. (6) TOST equivalence testing with multi-margin sensitivity analysis.

**Top concerns:** (1) [Major] Cross-judge design confounds judge identity with model identity — GPT-5.4 judges Claude/GPT-4.1/Qwen3 while GPT-4.1 judges GPT-5.4/DeepSeek. For C4's 52pp auth_scope range, genuine model differences are mixed with judge differences. Both judges are from OpenAI. (2) [Major — partially retracted, see §4] R1 claimed several experiments were missing from the paper (SOPBench, ecological validity KS tests, DeBERTa classifier); cross-checking confirms these ARE present in the paper. (3) [Minor] Single-day data collection raises temporal confound concern. (4) [Minor] Pre-registration referenced but no protocol URL provided.

**R1-unique finding from code inspection:** R1 examined the experimental codebase and found that tool execution in the harness appears simulated (`{"status": "simulated"}`). If confirmed, this is a significant undisclosed limitation — real tool responses could provide disambiguating information. However, this finding comes from development code, not the paper, and may reflect the τ²-bench framework's standard evaluation setup.

### R2 (Novelty + Related Work) — Score: 3.5

**Top strengths:** (1) Genuinely novel research question — no prior work provides causal, type-granular mapping from policy ambiguity to agent safety violations. The "first matched-pair causal study" claim appears justified. (2) Self-critical statistical treatment — C3 labeled inconclusive, incompleteness confound acknowledged, TOST sensitivity reported. (3) Strong replication evidence across 5 models, 2 benchmarks, 4 domains. (4) Ambiguity blindness (<5% awareness) is a meaningful empirical contribution extending psycholinguistic work to agentic settings. (5) Systematic nocuity (27% convergent wrong interpretation) is a useful conceptual extension of Berry & Kamsties. (6) Well-situated in literature with clear differentiation from DRIP-R, PolicyBank, and τ²-bench.

**Top concerns:** (1) [Major] Taxonomy conflates genuinely different phenomena under "ambiguity" — incompleteness is information absence, conditional precedence is normative conflict, authorization scope overlaps with vagueness. None are ambiguity in the strict linguistic sense. This theoretical muddiness propagates to the "differential nocuity" and "disambiguation channel" frameworks. (2) [Major] "Differential nocuity" may be more rebranding than conceptual advance — Willis et al. (2008) already showed different ambiguity types have different nocuity profiles. The paper's contribution is the empirical demonstration for LLM agents, which is valuable but calling it a "framework" overstates novelty. (3) [Major] Type hierarchy (C2) is the paper's central claim but V=0.137 is small. The 22pp gap between extremes is practically meaningful, but the mid-tier cluster (4 types within ~6pp) shows limited differentiation. The title "Not All Policy Ambiguity Is Equal" overclaims relative to the evidence that primarily shows incompleteness ≫ rest ≈ each other. (4) [Minor] Authorization scope results are prominently featured (52pp range, abstract, discussion) despite being the type with lowest judge reliability. (5) [Minor] Disambiguation channel framework is theoretically interesting but receives only cursory development.

**R2-unique observation:** R2 found variance decomposition data in the repository (clause 22.4% vs. type 0.4% of variance). If accurate, this substantially reframes the story: individual clause wording dominates type membership by 56×. This analysis does not appear in the paper PDF and should either be included with discussion or its implications addressed.

---

## 4. Step 2: Cross-Sharing Corrections

Several factual errors emerged when cross-checking reviewer claims against the paper PDF:

| Claim | Reviewer | Verdict | Evidence |
|---|---|---|---|
| SOPBench absent from paper | R1, R2 | **WRONG** | Section 5.6 + Table 8 report full SOPBench results |
| No KS test results reported | R1 | **WRONG** | Table 2 shows all 4 KS p-values |
| DeBERTa replaced by GPT-4.1 | R1 | **WRONG** | Appendix C + Table 12 report DeBERTa-v3-large 5-fold CV |
| "Seven models" tested | R2 | **WRONG** | Paper has 5 models; R2 found 2 additional in repo files |
| 41.3% systematic nocuity | R2 | **WRONG** | Paper says 27% (Section 7) |
| Variance decomposition (type=0.4%) | R2 | Not in paper | Found in repo experiments.tex, not submitted PDF |
| Mitigation experiment results | R2 | Not in paper | Found in repo, not submitted PDF |
| Simulated tool execution | R1 | Unconfirmed | Found in harness.py code, not disclosed in paper |

**Impact on scores:** R1's "missing experiments" concern (which was one of its major weaknesses) is invalidated. The paper actually includes SOPBench replication, ecological validity validation, and the DeBERTa classifier — all experiments R1 claimed were absent. This removes a significant negative and would raise R1's reproducibility score. R2's factual errors (model count, systematic nocuity rate) are minor and don't affect the core assessment.

---

## 5. Step 3: Convergence — Agreements and Disagreements

### Points of Strong Agreement

1. **C1 is convincingly established.** Both reviewers agree the +34.0pp binary effect with perturbation control (Δ_perturb=−0.67pp) constitutes strong causal evidence. The matched-pair design is sound, the effect replicates across all 5 models, and the SOPBench cross-benchmark replication (Δ=31.2pp, rule-based verifier) strengthens generalizability. This is the paper's strongest contribution.

2. **Claim calibration is commendable.** Both reviewers independently praised the honest downgrading of C3 to "suggestive" and the transparent reporting of within-judge fragility. This builds scientific credibility.

3. **Type hierarchy (C2) is real but small.** Both agree V=0.137 is a small effect size. The incompleteness > rest > coreferential structure is supported, but the mid-tier differentiation is weak. The paper's statistical sophistication (power=0.993, TOST analysis) is appreciated but the practical significance of type distinctions (beyond incompleteness being worst) is limited.

4. **Cross-judge confound is the primary methodological concern.** R1 raised this explicitly; R2's concern about auth_scope reliability (lowest judge agreement) is the same issue from a different angle. The 52pp auth_scope range — the paper's "star statistic" — is the claim most vulnerable to judge artifacts because (a) auth_scope has the lowest cross-judge agreement, (b) the judges are both OpenAI models, and (c) the paper does not report auth_scope-specific within-judge analysis.

5. **Ecological validity of synthetic clauses is a concern.** Both reviewers note this, though the paper's Table 2 (KS tests, discriminator at chance) partially addresses it. The concern is legitimate but mitigated.

### Points of Divergence

1. **Theoretical novelty.** R2 views "differential nocuity" as rebranding (Willis et al. 2008 precedent) while R1 sees the conceptual framing as a genuine contribution. **Resolution:** The empirical demonstration is novel; the theoretical framework is incremental. The paper should more carefully cite Willis et al. and position differential nocuity as an empirical validation in a new domain (LLM agents) rather than a new theoretical framework.

2. **Taxonomy validity.** R2 raises the fundamental concern that the taxonomy conflates ambiguity (multiple readings), vagueness (authorization scope), information absence (incompleteness), and normative conflict (conditional precedence). R1 does not raise this concern. **Resolution:** This is a legitimate theoretical weakness. The paper's pragmatic grouping under "policy ambiguity" is defensible for the applied safety audience, but the conflation limits the theoretical claims. The paper should acknowledge this more explicitly.

3. **Excitement.** R1 rates 3.5 (timely question, striking effect size), R2 rates 3.0 (empirical characterization without new methods). **Resolution:** Split the difference at 3.5. The combination of causal design + type granularity + cross-model interaction IS novel for the agent safety literature, even if the individual methods are standard.

### Adjusted Consensus Scores (Post-Roundtable)

After correcting R1's factual errors (missing experiments are actually present) and weighing the cross-sharing discussion:

- **Soundness: 3.5/5** — Strong matched-pair design and perturbation control, but cross-judge confound on C4 and taxonomy conflation are real concerns.
- **Excitement: 3.5/5** — Novel research question with practical importance; theoretical contributions are incremental rather than transformative.
- **Reproducibility: 3.5/5** — Model versions, temperature, clause counts, and statistical tests well-specified. Code and data promised for release. The ?? citation placeholders and blank references page are formatting issues for the submission.
- **Overall: 3.5 (Borderline Conference)**

---

## 6. Step 4: Consolidated Assessment

### Overall Assessment: 3.5 (Borderline Conference)

This paper addresses a genuinely novel and practically important question — how different types of policy ambiguity cause safety violations in LLM agents, and how this varies across model families. The matched-pair design with perturbation control is methodologically strong, and the +34.0pp binary effect (OR=15.1) is convincingly established as the strongest causal evidence for ambiguity-specific harm in the agent safety literature. The SOPBench cross-benchmark replication across 4 domains with an independent rule-based verifier, the ICC=0.919 test-retest reliability, and the human-validated judge calibration (κ=0.87) collectively provide unusually thorough validation for an agent evaluation paper.

### What Keeps It From 4.0 (Main Conference)

1. **Cross-judge confound on C4.** The paper's most novel finding — the 52pp authorization scope interaction — is also its most methodologically vulnerable. Each model is judged by exactly one LLM judge (both from OpenAI). The auth_scope type has the lowest cross-judge agreement, and the paper does not report auth_scope-specific within-judge-group analysis. Adding a third judge from a non-OpenAI family, or reporting within-judge-group C4 results, would substantially strengthen this claim.

2. **Theoretical framework is underdeveloped.** "Differential nocuity" is presented as a framework but receives minimal theoretical development beyond the empirical results. Willis et al. (2008) is not adequately distinguished. The "disambiguation channel framework" is interesting but presented as speculation with only observational support. The taxonomy conflates linguistically distinct phenomena (ambiguity, vagueness, incompleteness, normative conflict) under one umbrella, which limits the depth of theoretical analysis.

3. **Type hierarchy practical significance.** The V=0.137 for C2 is small. The story is essentially "incompleteness is worst, coreferential is least bad, the other four are similar." The title overclaims relative to this finding. The variance decomposition in the authors' own analysis (found in supplementary materials) shows clause-level wording explains 56× more variance than type — this should be reported and discussed, as it reframes the practical recommendation from "type-level triage" to "clause-level auditing."

4. **Formatting issues.** All in-text citations render as ?? or ?. The references page is blank. This is clearly a LaTeX compilation issue but must be fixed before submission.

### What Makes It Strong for Findings (3.0+)

1. **C1 is rock-solid.** Triple causal evidence chain: matched-pair + perturbation control + cross-benchmark replication. No prior agent safety work has this level of causal rigor.

2. **Cross-benchmark replication is rare and valuable.** SOPBench across healthcare/banking with rule-based verifier (91% agreement with LLM judge), 4-domain coverage, and preserved model ranking (r=0.89) goes well beyond what reviewers typically expect.

3. **Honest claim calibration.** C3 downgraded to "suggestive," incompleteness confound transparently handled, within-judge fragility disclosed. This builds trust in all other claims.

4. **Ambiguity blindness is empirically striking.** <5% awareness, 89% surface adoption, <1% escalation across 5 models. This quantification of a previously anecdotal concern is a genuine contribution.

5. **Model × type interaction (despite caveats).** Even with the cross-judge confound, the qualitative pattern — Claude robust to auth_scope, DeepSeek uniformly vulnerable, incompleteness universally dangerous — is informative for the safety alignment community.

### Actionable Recommendations for Revision

**High priority (would move toward 4.0):**
- Add a non-OpenAI judge (e.g., Claude as judge) for at least a subset of episodes to address the cross-judge confound on C4
- Report within-judge-group C4 analysis explicitly (does the 52pp auth_scope range hold within each judge group?)
- Include variance decomposition in the paper with discussion of what clause-level vs. type-level variance means for practical recommendations
- Fix all ?? citations and compile the full bibliography
- Acknowledge the taxonomy conflation more explicitly in Section 3 (ambiguity vs. vagueness vs. incompleteness)

**Medium priority:**
- Develop the disambiguation channel framework beyond speculation — even a single paragraph connecting to formal disambiguation theory would help
- More carefully position "differential nocuity" relative to Willis et al. (2008)
- Report auth_scope-specific judge calibration statistics prominently given its role as the "star" finding
- Address R1's concern about whether tool execution is simulated — if τ²-bench uses simulated tools, disclose this and discuss implications

**Low priority:**
- Consider whether the title overclaims given V=0.137
- Add missing related work: AmbigQA (Min et al. 2020), formal policy specification literature
- Disclose whether test families for Holm-Bonferroni were pre-specified or post-hoc

### Venue Recommendation

**3.5 — Borderline Conference.** The paper is a strong candidate for Findings and a borderline candidate for main conference. The C1 causal evidence is main-conference caliber. The C4 interaction finding, if the cross-judge confound is addressed, would push this solidly to 4.0. In its current form, the theoretical contributions are not sufficiently developed for main, but the empirical rigor and practical importance make it clearly above the Findings threshold.

---

*Review conducted by two independent reviewers (R1: Methods/Experiments, R2: Novelty/Related Work) with full roundtable cross-sharing and convergence. Factual errors in individual reviews were identified and corrected during cross-checking.*

---

## 引用验证结果

**统计**: 43 篇文献 / 62 处引用 / 在线验证 43/43 篇

### 问题 (11)

- ❌ `berry_kamsties_2004` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.37 below threshold 0.82
- ⚠️ `ferrari_defects_2018` — 元数据不匹配: first_author: bib=rosadini vs api=ferrari
- ⚠️ `zheng_llm_judge_2024` — 元数据不匹配: first_author: bib=zheng vs api=chiang
- ❌ `tau_bench_2024` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.37 below threshold 0.82
- ❌ `tau2_bench_2025` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.32 below threshold 0.82
- ❌ `hu_ambiguity_2025` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.39 below threshold 0.82
- ⚠️ `lakens_2017` — 元数据不匹配: title: similarity=0.34 (possible wrong DOI)
- ⚠️ `lin_ask_to_clarify_2025` — 元数据不匹配: first_author: bib=lin vs api=xingyao
- ⚠️ `yu_causal_2026` — 在 .bib 中但正文未引用
- ⚠️ `lin_ask_to_clarify_2025` — 在 .bib 中但正文未引用
- ⚠️ `mu_can_llms_2023` — 在 .bib 中但正文未引用

### ✅ 通过 (35)