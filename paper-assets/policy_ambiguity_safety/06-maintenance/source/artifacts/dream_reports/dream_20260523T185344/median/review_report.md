---
dream_id: dream_20260523T185344
tier: median
overall_score: 3.5 — Borderline Conference / Strong Findings
timestamp: 2026-05-23T19:59:41.641617+00:00
---

# Dream Review Report: "Not All Policy Ambiguity Is Equal"

**Dream ID:** 20260523T185344
**Review Mode:** Full (2-Reviewer Roundtable)
**Target Venue:** EMNLP 2026 (ARR)

---

## Roundtable Summary

Two reviewers conducted independent reviews (R1: Methods & Experiments; R2: Novelty & Related Work), followed by cross-sharing and convergence discussion. Both converged on **Overall 3.5** (Borderline Conference / strong Findings).

---

## Consolidated Scores

| Dimension | R1 | R2 | Consensus |
|---|---|---|---|
| Soundness | 3.5 | 4 | 3.5 |
| Excitement | 3.5 | 3 | 3 |
| Reproducibility | 3.5 | 4 | 3.5 |
| **Overall** | **3.5** | **3.5** | **3.5** |
| Confidence | 4 | 4 | 4 |

**Verdict:** Borderline Conference — competitive for Findings, could reach Main with targeted revisions.

---

## Strengths (Consensus)

**S1. Rigorous matched-pair causal design (R1, R2 concur).** The minimal-edit clause pair construction with perturbation controls (Δ_perturb = −0.67pp, CI contains zero) is methodologically exemplary. No prior work in the agent safety space provides matched-pair causal evidence isolating ambiguity type as the independent variable. The perturbation control definitively rules out surface-level prompt sensitivity as a confound.

**S2. Large, robust primary effect (R1).** The +34.0pp binary effect (OR=15.1, p<0.0001) survives every robustness check: exclusion of any single type, cross-model replication across 5 models, cross-benchmark replication on SOPBench, and logistic regression controlling for token delta. This is among the largest causally-established effects in the agent safety literature.

**S3. Comprehensive validity infrastructure (R1).** ICC test-retest reliability (0.919), cross-judge validation (Fleiss' κ=0.717), human-LLM judge calibration (pooled κ=0.807, F1=0.89), and realism validation (3/4 KS tests pass) collectively address most threats to internal and external validity. This level of methodological care exceeds typical agent safety benchmarking papers.

**S4. Genuinely novel research question (R2).** No prior work causally quantifies the impact of specific ambiguity types on agent safety violations or examines how this impact varies across model families. The paper sits at an underexplored intersection of requirements engineering, psycholinguistics, and agent safety.

**S5. Convergent nocuity concept (R2).** The inversion of Berry-Kamsties' framework — showing agents converge on the *same wrong* interpretation rather than diverging — is a significant conceptual contribution with practical implications for agreement-based safety monitoring.

**S6. Honest reporting of negative/inconclusive results (R1, R2 concur).** C3 (layer effect) is transparently labeled inconclusive. Within-judge analyses (p=0.059, p=0.157) are reported without spin. Failure-mode human validation κ=0.39 is disclosed prominently. This scientific maturity strengthens the paper's credibility.

**S7. Cross-benchmark replication (R1).** SOPBench replication across 2 additional domains (Healthcare, Banking) with a rule-based verifier (eliminating LLM-judge confound) confirms the binary effect in 4/5 models (Δ=19.4pp), strengthening external validity.

---

## Weaknesses (Consensus)

**W1. Authorization scope undermines multiple claims [Major] (R1 raised, R2 concurs).** Authorization scope has the lowest inter-judge agreement, the largest cross-model range (52pp), borderline/contaminated pairs (8/50 borderline + 3/50 cross-type), and drives the entire C4 interaction (excluding it renders the interaction non-significant). The cumulative effect is underappreciated — one of six types has compromised construct validity, affecting C2 omnibus test, TOST equivalence structure, and the model×type interaction. The paper should present a complete re-analysis excluding authorization scope as a primary robustness check, or more prominently qualify all claims involving this type.

**W2. Failure mechanism analysis relies on LLM coders with large human-LLM gap [Major] (R1 raised, R2 concurs).** The type-mechanism dissociation (V=0.45) is a central contribution, but it rests on LLM-coded traces. Human mechanism coding yields κ=0.39 (5-category) / κ=0.51 (3-category collapsed), and there is a concerning gap between LLM agreement and human agreement. The paper's own acknowledgment that LLM agreement "may partly reflect shared classification conventions" creates an uncomfortable circularity with the convergent nocuity phenomenon the paper documents. The fine-grained type-mechanism structure may be partially an annotation artifact rather than a genuine behavioral pattern.

**W3. Disambiguation Channel Framework is underspecified and unsupported by data [Moderate] (R2 raised, R1 partially concurs).** The framework posits that linguistic ambiguities have partial external disambiguation channels while specification ambiguities don't. C3 (the direct test of this hypothesis) fails Holm-Bonferroni correction, and within-judge analyses are fragile. Presenting this as a named framework contribution is premature. R1 notes the per-type labels retain diagnostic utility, but the layer-level grouping is not empirically supported. Recommended: downgrade framing from "framework" to "design hypothesis" or "organizing observation."

**W4. Incompleteness information-addition confound weakens narrative prominence [Moderate] (R2 raised, R1 concurs).** When the unambiguous variant necessarily adds policy content, the treatment is not purely ambiguity resolution. The paper handles this transparently (marking as upper bound, reporting +31.0pp excluding incompleteness, controlling token delta as covariate), but incompleteness remains the most narratively prominent finding — it drives the "safety training blind spot" framing, tops the hierarchy, and features in the practical implications. The coreferential lower bound (+18.7pp at minimal token delta) is the cleaner causal estimate but receives less emphasis.

**W5. Convergent nocuity claims outrun statistical evidence [Moderate] (R1 raised, R2 concurs).** With only 1 within-family pair (Jaccard=0.54) vs. 9 cross-family pairs (0.46), there is no statistical power to conclude that cross-family convergence "approaches" within-family levels. The 0.08 difference could be noise. The permissive attractor finding (77%) is striking but not connected to the well-studied RLHF sycophancy literature (Perez et al. 2023, Sharma et al. 2024), which is a missed opportunity.

**W6. Realism validation mentioned but not fully presented [Minor] (R1 raised).** The method section references KS tests comparing synthetic clauses to DRIP-R natural ambiguities (3/4 pass, parse depth fails at p=0.041), but the full analysis is not presented in the main text or appendix. This is a significant omission for evaluating ecological validity. The parse depth failure (synthetic clauses simpler than natural) is argued to be conservative bias, which is plausible but should be shown, not just asserted.

**W7. Disambiguation neglect / Ambiguity Blindness is incremental [Minor] (R2 raised, R1 partially disagrees).** R2 argues the gap between "LLMs collapse ambiguous representations" (Liu et al. 2023) and "LLM agents act on collapsed interpretations without flagging uncertainty" is narrow. R1 defends the behavioral extension as meaningful (the 4.6% awareness rate with cross-model variation is a genuine empirical contribution). Consensus: the concept is not highly novel but the quantification is valuable.

**W8. Temperature=0 limits ecological validity [Minor] (R1 raised, R2 disagrees).** R1 notes production systems often use temperature 0.3-0.7, and no pilot data exists for temperature>0. R2 argues temperature=0 is standard for policy-governed deployment. Consensus: minor concern, appropriately handled in Limitations.

---

## Key Questions for Authors

1. **Authorization scope robustness:** What happens to C2 and C4 when the 11 problematic auth_scope pairs (8 borderline + 3 cross-type contaminated) are excluded? Does the model×type interaction survive without authorization scope entirely?

2. **Realism validation:** Where is the full KS test analysis comparing synthetic vs. DRIP-R clauses? The parse depth failure (p=0.041) deserves explicit presentation and discussion.

3. **LLM-coded failure mechanisms:** Given that human κ=0.39 and LLM-LLM agreement may reflect shared classification conventions, how confident are you that V=0.45 represents genuine type-mechanism structure rather than annotation artifact? Would a different LLM family (e.g., Gemini) as coder produce similar structure?

4. **Convergent nocuity statistics:** With only one within-family pair, the Jaccard comparison lacks power. Would a permutation test comparing within- vs. cross-family distributions be feasible?

5. **Disambiguation Channel Framework:** Given that C3 fails Holm-Bonferroni and within-judge analyses are fragile, should this be downgraded from "framework" to "design hypothesis" or "organizing observation"?

6. **Permissive attractor and sycophancy:** The 77% permissive bias finding would benefit from engagement with the RLHF sycophancy literature. Is convergent nocuity a special case of specification gaming?

---

## Experiment Coverage Assessment

All imagined experiments from the design document appear covered in the paper:
- ✅ Clause generation (plan_001) — 300 pairs, 6 types
- ✅ Mini-pilot (plan_001b) — 20 episodes for new types
- ✅ Full study API (plan_002) — 1,800 episodes, 3 API models
- ✅ Full study open-source (plan_003) — 1,197 episodes, 2 open-source models
- ✅ Full analysis (plan_004) — C1-C4 statistical analysis
- ✅ Error analysis (plan_005) — 614 traces, 5 failure modes
- ✅ Reliability (plan_006) — ICC=0.919
- ✅ Realism validation (plan_007) — mentioned but details sparse
- ✅ Classifier PoC (plan_008) — DeBERTa binary F1=0.805
- ✅ Judge calibration (plan_009) — human-LLM κ=0.807
- ✅ Perturbation control (plan_010) — Δ=-0.67pp, PASS
- ✅ SOPBench (plan_017) — 982 episodes, 4/5 replicate
- ✅ Human re-annotation (what_if) — κ=0.39

---

## Actionable Revision Recommendations

1. **High priority:** Present authorization scope robustness analysis (exclude problematic pairs, show C2/C4 with and without auth_scope) as a primary table or paragraph in Results.

2. **High priority:** Present the realism validation KS test results explicitly (currently referenced but not shown).

3. **Medium priority:** Downgrade "Disambiguation Channel Framework" to "design hypothesis" or "organizing observation" given C3 failure. Remove from named contributions.

4. **Medium priority:** Add formal statistical test for convergent nocuity (permutation test for Jaccard within- vs. cross-family). Connect permissive attractor to RLHF sycophancy literature.

5. **Medium priority:** Qualify type-mechanism dissociation claims more prominently given human-LLM agreement gap. Consider presenting collapsed 3-category results (κ=0.51) as primary and 5-category as supplementary.

6. **Low priority:** Rebalance incompleteness narrative emphasis — present coreferential lower bound more prominently as the cleaner causal estimate.

---

## Final Assessment

**Overall: 3.5 (Borderline Conference / Strong Findings)**

The paper makes a genuine contribution to agent safety research through its rigorous causal design and large, robust primary effect (+34.0pp). The matched-pair methodology, perturbation controls, and cross-benchmark replication establish C1 at a standard exceeding most agent safety evaluation papers. The model×type interaction (C4) is a genuinely novel finding, though its reliance on authorization scope — the type with weakest construct validity — is concerning.

The paper's main limitations are: (a) two of six ambiguity types have significant validity concerns (authorization scope: construct validity; incompleteness: information-addition confound), meaning four types carry the core claims; (b) the failure mechanism analysis rests on LLM coding with only fair human agreement; (c) several named conceptual contributions (Disambiguation Channel Framework, Convergent Nocuity) outrun their statistical evidence.

The paper demonstrates unusual scientific maturity in its transparent handling of negative results and limitations. With the recommended revisions — particularly authorization scope robustness analysis, realism validation presentation, and Disambiguation Channel Framework downgrade — this could reach a clear Conference-level recommendation. As submitted, it is competitive for Findings and borderline for Main.

**Expected ARR range:** 3.25–3.75, central estimate 3.5.


---

## 引用验证结果

**统计**: 63 篇文献 / 86 处引用 / 在线验证 63/63 篇

### 问题 (16)

- ❌ `berry_kamsties_2004` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.37 below threshold 0.82
- ⚠️ `ferrari_defects_2018` — 元数据不匹配: first_author: bib=rosadini vs api=ferrari
- ⚠️ `zheng_llm_judge_2024` — 元数据不匹配: first_author: bib=zheng vs api=chiang
- ❌ `tau_bench_2024` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.37 below threshold 0.82
- ❌ `tau2_bench_2025` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.32 below threshold 0.82
- ❌ `hu_ambiguity_2025` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.39 below threshold 0.82
- ⚠️ `lakens_2017` — 元数据不匹配: title: similarity=0.34 (possible wrong DOI)
- ⚠️ `lin_ask_to_clarify_2025` — 元数据不匹配: first_author: bib=lin vs api=xingyao
- ⚠️ `ruis_goldilocks_2023` — 元数据不匹配: first_author: bib=ruis vs api=biderman
- ❌ `li_sopbench_2025` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.33 below threshold 0.82
- ❌ `krakovna2020specification` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.30 below threshold 0.82
- ❌ `poesio_artstein_2005` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.40 below threshold 0.82
- ❌ `wang_agentspec_2026` — 在线验证未找到匹配（疑似虚假引用）: best match similarity 0.33 below threshold 0.82
- ⚠️ `lin_ask_to_clarify_2025` — 在 .bib 中但正文未引用
- ⚠️ `rosenbaum_observational_2002` — 在 .bib 中但正文未引用
- ⚠️ `wang_agentspec_2026` — 在 .bib 中但正文未引用

### ✅ 通过 (50)