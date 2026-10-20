---
dream_id: dream_20260522T111643
tier: median
overall_score: 3.5 — Borderline Conference / Strong Findings
timestamp: 2026-05-22T12:07:33.945843+00:00
---

# Dream Review Report: "Not All Policy Ambiguity Is Equal"

**dream_id**: 20260522T111643  
**Venue**: EMNLP 2026 (ARR)  
**Review mode**: full (2 reviewers, 4-step roundtable)

---

## Step 1: Independent Reviews

### R1 (Methods + Experiments) — Independent Score: 3.5/5

**Strengths:**
1. Matched-pair design with perturbation control is a genuine methodological contribution to agent safety evaluation. The within-clause comparison (amb vs. unamb as minimal edit) is a strong causal design; the perturbation control arm (Δ=−0.67pp, CI containing zero) effectively rules out general prompt brittleness.
2. Thorough measurement validation chain: cross-judge design to avoid self-evaluation bias, human calibration (κ_w=0.807 exceeding human-human κ_w=0.762), ICC=0.919 for test-retest reliability. This level of measurement transparency is rare in agent safety papers.
3. Confound handling for incompleteness is exemplary: logistic regression controlling token delta, coreferential as confound-free lower bound, authorization scope counter-evidence, and explicit statement that C1 holds even excluding incompleteness.
4. Statistical methodology is mostly appropriate: McNemar's for paired binary, TOST equivalence testing with multi-margin sensitivity, bootstrap CIs, Holm-Bonferroni correction. Post-hoc power >0.99 for C1 and C2.
5. Honest epistemic calibration: C3 moved to appendix as exploratory, C4 interaction labeled appropriately, variance decomposition presented despite potentially undercutting narrative.

**Weaknesses:**
1. Cross-judge design confounds judge identity with model identity. GPT-5.4 judges three models; GPT-4.1 judges two. The 52pp authorization scope range (Claude 12% to GPT-5.4 64%) spans judge groups. A judge-bias sensitivity analysis using the 100 dual-judged episodes is needed to bound this confound for C4.
2. Authorization scope has the weakest measurement properties (cross-judge κ=0.385 per review context) but receives outsized narrative weight. Excluding auth_scope would collapse the C4 interaction (estimated p=0.97 without it).
3. Perturbation control is underpowered: CI [−8.0, 6.67] cannot distinguish 0pp from 6.67pp perturbation effect. While the residual ambiguity effect (27.3pp worst-case) is still large, a tighter bound would strengthen the causal claim.
4. Error analysis inter-coder κ=0.517 (moderate). Fine-grained failure mode proportions carry substantial uncertainty. The paper handles this by using qualitative descriptors (majority/plurality), but CIs for proportions are missing.
5. Token delta as confound proxy is coarse — semantic information density may differ from raw token count.
6. Coreferential excluded from multiple secondary analyses without consolidated justification.

**R1 Scores:** Soundness 4/5, Excitement 3.5/5, Reproducibility 4/5, Overall 3.5/5

---

### R2 (Novelty + Related Work) — Independent Score: 3.5/5

**Strengths:**
1. Genuine conceptual novelty in the research question: first causal, type-granular mapping from ambiguity to safety violations in agentic settings. No prior work isolates ambiguity type as a causal variable with matched-pair controls.
2. Well-grounded theoretical framing via Berry & Kamsties' nocuous/innocuous distinction. The argument that LLM agents lack disambiguation channels (colleague consultation, shared context) that make most ambiguity innocuous in human RE is compelling.
3. "Ambiguity Blindness" (or "Disambiguation Neglect") finding is impactful: <5% meta-cognitive awareness, >88% surface adoption, <1% user escalation. This extends ambiguity-collapse findings to consequential agentic settings.
4. Systematic nocuity (27% of ambiguous episodes → all models converge on same wrong interpretation) is a novel concept with practical implications for inter-model agreement-based evaluation.
5. Exceptional statistical discipline for the subfield.
6. Disambiguation channel framework provides useful organizing principle beyond mere enumeration.

**Weaknesses:**
1. Taxonomy is synthesized from Li et al. (2024) and Massey et al. (2014), not genuinely novel. The main conceptual addition is the disambiguation channel principle.
2. "Differential nocuity" term may overstate contribution — Willis et al. (2008) already studied differential nocuity detection. The empirical demonstration in LLM agent context is the contribution, not the concept.
3. Missing important related work: ClarEval (Mar 2026), Ambig-SWE (ICLR 2026), LHAW (Feb 2026), ATBench (Apr 2026), OpenAgentSafety (ICLR 2026). These are directly relevant to disambiguation channels and agent clarification-seeking.
4. "Ambiguity" label is stretched for incompleteness (absent information) and conditional precedence (normative conflict). The paper should engage with Dalpiaz et al. (2018) on the distinction between ambiguity, incompleteness, and inconsistency.
5. Variance decomposition shows type explains only 0.4% of variance vs. clause identity at 22.4% — this fundamentally undermines the "not all ambiguity is equal" framing. Clause-level wording dominates; the type taxonomy may be less useful than individual clause auditing.
6. DRIP-R comparison should be deeper (do their type rankings correlate? does their agreement rate map to systematic nocuity?).
7. The 7-model claim mixes full-design evaluation (5 models) with reduced-scope replication (2 models) without sufficient clarity.

**R2 Scores:** Soundness 4/5, Excitement 3.5/5, Reproducibility 4/5, Overall 3.5/5

---

## Step 2: Cross-Sharing — Key Observations

### Correction: SOPBench IS in the Paper
Both reviewers flagged SOPBench as missing. This is incorrect: the paper includes SOPBench results in §5.1 (one paragraph + cross-reference) and Appendix A (full section with Table 8: τ²-bench vs. SOPBench comparison, per-model SOPBench results, type ranking comparison). The SOPBench replication covers 982 valid episodes across healthcare and banking domains with all 5 models. This partially addresses the single-domain concern, though the weaker effect (Δ=18.3pp vs. 34.0pp) and non-significant type ranking correlation (ρ=0.40, p=0.60) raise questions about cross-domain generalizability of fine-grained findings.

### Points of Agreement
1. Both converge at 3.5 overall — strong Findings, borderline conference
2. Both praise the matched-pair + perturbation control design as the core methodological contribution
3. Both note honest epistemic calibration as a strength
4. Both flag C4 (model×type interaction) as the most interesting but empirically weakest claim
5. Both identify the 7-model framing as potentially misleading
6. Both score Soundness 4/5 and Reproducibility 4/5

### Points of Divergence
- R2's variance decomposition challenge (type = 0.4% of variance) is potentially devastating to the paper's central thesis. R1 noted this was honestly presented but didn't flag it as undermining the core framing. **Assessment**: R2's point is valid — the paper's title and framing emphasize type-level differences, but clause-level wording explains 56× more variance than type. However, the type hierarchy is still statistically significant (χ²=28.02, p=3.6e-5) and the 22pp incompleteness-coreferential gap is practically meaningful even if type is a coarse predictor. The tension is real but not fatal — it suggests the paper should frame types as "risk categories for triage" rather than "deterministic predictors."
- R1's cross-judge confound concern is more technically detailed than R2's treatment of C4. This is a genuine methodological limitation that could explain some of the 52pp range.
- R2 identifies more missing related work (5+ papers), reflecting the novelty-focused lens. These are legitimate gaps.

---

## Step 3: Convergence

### Consensus Assessment

**C1 (Binary Effect)**: Both reviewers agree this is solid and the paper's strongest contribution. The +34.0pp effect with perturbation control, replicated across 5 models and partially on SOPBench (Δ=18.3pp), is convincing. The perturbation control CI width (up to 6.67pp) is a minor concern but doesn't threaten the main finding. **Verdict: Strong.**

**C2 (Type Hierarchy)**: The three-tier structure is statistically significant and TOST-validated, but R2's variance decomposition challenge (type = 0.4% of variance) is a serious concern for the paper's framing. The hierarchy is real at the extremes (incompleteness >> coreferential) but the mid-tier clustering and small V=0.137 limit practical utility. SOPBench partial replication (incompleteness still #1, but ρ=0.40 n.s.) adds domain-moderation caveats. **Verdict: Moderate — findings-level contribution.**

**C4 (Model×Type Interaction)**: The most interesting finding but methodologically the weakest. Authorization scope drives the entire interaction; cross-judge confounding and low per-type judge agreement (κ=0.385) create interpretability concerns. Claude's 12% vs GPT-5.4's 64% is striking but may partly reflect judge bias. **Verdict: Suggestive — needs judge-bias sensitivity analysis.**

**Error Analysis (Ambiguity Blindness)**: <5% awareness is a robust binary metric unaffected by the moderate inter-coder κ. The systematic permissiveness bias (69.2% escalation, 0% restriction for auth_scope) is striking. Inter-coder κ=0.517 limits fine-grained failure mode claims. **Verdict: Moderate — the blindness finding is solid; failure mode taxonomy is exploratory.**

**SOPBench Replication**: Present in the paper (§5.1 + Appendix A), confirming binary effect cross-domain (Δ=18.3pp, p<0.0001). Weaker effect size is explained by three factors (rule-based verifier, domain moderation, higher baselines). Type ranking partial alignment (ρ=0.40, n.s.) adds important domain-moderation caveats. **Verdict: Useful but raises as many questions as it answers.**

### Formatting Issue
All bibliography citations render as "(?)". This is a LaTeX compilation error (.bbl not generated or bibliographystyle mismatch). If submitted in this state, reviewers would be severely hindered and the paper could face desk-reject risk. **Must fix before submission.**

### Agreed Weaknesses (Priority Order)
1. **Bibliography not rendering** — critical formatting issue
2. **Cross-judge confound on C4** — limits interpretability of the headline auth_scope finding
3. **Type explains 0.4% of variance** — tension with paper's central "not all ambiguity is equal" framing
4. **Missing related work** — ClarEval, Ambig-SWE, LHAW, OpenAgentSafety at minimum
5. **"Ambiguity" label stretch** — incompleteness and cond_prec are not ambiguity in the linguistic sense
6. **Perturbation control CI width** — minor but should be discussed
7. **Error analysis inter-coder reliability** — moderate κ limits failure mode claims

### Agreed Strengths (Priority Order)
1. Matched-pair causal design with perturbation control — methodological contribution
2. C1 binary effect is massive and replicates across all models and benchmarks
3. Honest epistemic calibration — C3 to appendix, variance decomposition disclosed
4. Thorough measurement validation (ICC, judge calibration, human annotation)
5. Ambiguity Blindness finding (<5% awareness) is robust and practically important
6. SOPBench cross-benchmark replication adds domain breadth
7. Five architecturally diverse models across three providers

---

## Step 4: Final Synthesis

### Meta-Review

This paper makes a genuine contribution to agent safety evaluation by introducing a matched-pair causal design that cleanly isolates the effect of policy ambiguity on safety violations. The core finding — that ambiguous policy clauses increase violation rates by +34.0pp across five models, while non-ambiguity perturbations produce near-zero effect — is convincing and replicates on a second benchmark (SOPBench, Δ=18.3pp). The Ambiguity Blindness finding (<5% meta-cognitive awareness) has clear practical implications.

The paper's main limitation is a tension between its framing and its evidence. The title promises that "not all policy ambiguity is equal," but type explains only 0.4% of violation variance — clause-level wording explains 56× more. The type hierarchy is statistically significant but driven by the extremes (incompleteness vs. coreferential), with a small effect size (V=0.137). The model×type interaction (C4) is the most interesting finding but rests on authorization scope, which has the weakest measurement properties and is confounded with judge identity.

The paper exhibits exceptional statistical discipline and honest epistemic calibration — unusual strengths for this subfield. C3 is correctly moved to an exploratory appendix, variance decomposition is reported despite undercutting the narrative, and the error analysis honestly discloses moderate inter-coder agreement.

Several important concurrent works are missing from the related work section (ClarEval, Ambig-SWE, LHAW, OpenAgentSafety). The "ambiguity" framing for incompleteness and conditional precedence is pragmatically justified but conceptually stretched.

The bibliography rendering failure (all citations as "?") is a critical formatting issue that must be resolved.

### Final Scores

| Dimension | R1 | R2 | Converged |
|-----------|----|----|-----------|
| Soundness | 4/5 | 4/5 | **4/5** |
| Excitement | 3.5/5 | 3.5/5 | **3.5/5** |
| Reproducibility | 4/5 | 4/5 | **4/5** |
| Overall | 3.5/5 | 3.5/5 | **3.5/5** |
| Confidence | 4/5 | 4/5 | **4/5** |

### Overall Assessment: 3.5 — Borderline Conference / Strong Findings

**Calibration**: At 3.5 on the ARR scale, this paper falls between Findings-accept (3.0) and Conference-accept (4.0). The methodological contribution (matched-pair + perturbation control) and C1 binary effect are conference-quality. However, the type-level framing is weakened by low explained variance, the C4 interaction has measurement concerns, and the missing related work creates positioning gaps. With revisions (judge-bias sensitivity for C4, related work additions, variance decomposition reframing, bibliography fix), this could reach 4.0.

### Actionable Revision Priorities

1. **Fix bibliography rendering** — all citations show as "(?)", critical for review
2. **Add judge-bias sensitivity analysis for C4** — use 100 dual-judged episodes to estimate per-type judge correction; bound how much of the 52pp auth_scope range could be judge artifact
3. **Reframe type contribution given variance decomposition** — acknowledge that clause-level wording dominates; position types as "risk categories for prioritized auditing" rather than deterministic predictors
4. **Add missing related work** — ClarEval, Ambig-SWE, LHAW, OpenAgentSafety; engage with Dalpiaz et al. on ambiguity vs. incompleteness distinction
5. **Discuss TOST margin justification** — ground the ±15pp margin in deployment evidence or domain expert consultation
6. **Consolidate coreferential exclusions** — explain in one place why it's excluded from multiple secondary analyses
7. **Tighten perturbation control** — either expand to more clause pairs or explicitly discuss CI upper bound (6.67pp) tolerability


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