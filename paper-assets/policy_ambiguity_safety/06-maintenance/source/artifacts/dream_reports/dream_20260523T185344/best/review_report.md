---
dream_id: dream_20260523T185344
tier: best
overall_score: 3.5 — Borderline Conference
timestamp: 2026-05-23T19:52:19.881721+00:00
---

# Dream Review Report: "Not All Policy Ambiguity Is Equal"

**Dream ID**: 20260523T185344  
**Review Mode**: Full (2-Reviewer Roundtable)  
**Target Venue**: EMNLP 2026 (ARR)

---

## Consolidated Scores

| Dimension | R1 (Method) | R2 (Novelty) | Converged |
|-----------|-------------|--------------|-----------|
| Soundness | 4.0 | 3.5 | 4.0 |
| Excitement | 3.5 | 4.0 | 4.0 |
| Reproducibility | 3.5 | 3.0 | 3.0 |
| **Overall Assessment** | **3.5** | **4.0** | **3.5** |

**Overall Assessment: 3.5 — Borderline Conference**

Confidence: 4.0 (high — both reviewers aligned after cross-sharing)

---

## Summary of Paper

The paper investigates how policy ambiguity in natural language specifications causally affects safety violations in LLM agents. Using a matched-pair design (300 clause pairs × 6 ambiguity types × 5 models = 2,997 episodes), it establishes: (C1) ambiguity causes +34.0pp increase in violations; (C2) a three-tier type hierarchy; (C3) suggestive spec-vs-ling layer effect; (C4) model×type interaction with 52pp auth_scope range; (C5) validated failure mode taxonomy with "Ambiguity Blindness" (<5% awareness). Perturbation controls and cross-benchmark replication (SOPBench) strengthen the causal claims.

---

## Strengths

### S1: Genuinely Novel Research Question (R2, confirmed by R1)
No prior work has causally measured the effect of policy ambiguity on LLM agent safety violations. DRIP-R (Li et al. 2024) showed interpretation divergence but not consequential safety outcomes. The matched-pair design with perturbation controls is the first to establish ambiguity-specific causation in agent safety, moving the field beyond correlational claims.

### S2: Perturbation Control Is Methodologically Innovative (R1, endorsed by R2)
The perturbation control experiment (§4.5) is unprecedented in agent safety literature. The extended N=300 version with Δ=-0.67pp (CI upper 6.67pp) vs. Δ_ambiguity=+34.0pp, ratio=0.020, decisively rules out the prompt sensitivity alternative explanation (Sclar et al. 2024). This alone elevates the paper's causal rigor above comparable work.

### S3: Model×Type Interaction Is the Star Finding (Both reviewers)
The 52pp range for authorization scope (Claude 12% → GPT-5.4 64%) is a striking, actionable result. It reveals that safety training differentially mitigates specific ambiguity types — Claude's RLHF appears to specifically address authorization boundaries while leaving incompleteness equally vulnerable (48% vs. 46-62% for other models). The contrast between auth_scope (high model variance, 52pp range) and incompleteness (low model variance, 16pp range) is the most scientifically interesting finding. DeepSeek's uniform vulnerability (χ²=n.s.) vs. Claude's strong type differentiation (V=0.24) provides a clean natural experiment on the effect of type-specific safety training.

### S4: Honest Reporting of C3 Fragility (Both reviewers)
Characterizing the layer effect as "suggestive" when within-judge subgroup analysis shows p=0.059 and p=0.157 demonstrates scientific maturity. Many papers would bury this fragility. The paper correctly argues that the model×type interaction (C4) is more fundamental than the layer main effect.

### S5: Comprehensive Validation Chain (R1)
The paper builds a thorough evidence chain: ecological validity (KS tests + discriminator), judge calibration (human κ=0.807, cross-judge κ=0.685, no same-family bias), test-retest reliability (ICC=0.919), human re-annotation of failure modes (κ=0.52, 5/6 types consistent), and cross-benchmark replication (SOPBench, rule-based verification). Each link addresses a specific methodological threat.

### S6: Named Phenomena Are Citable (R2)
"Differential Nocuity," "Ambiguity Blindness," and "Convergent Nocuity" are well-defined, precisely quantified, and grounded in established theory (Berry & Kamsties 2003). The convergent nocuity concept (27% of ambiguous episodes: all 5 models converge on the same wrong answer) is genuinely concerning for practice — it's invisible to inter-model agreement checks.

### S7: Cross-Benchmark Replication Provides Measurement Independence (R1)
SOPBench uses rule-based verification (no LLM judge), different domains (healthcare + banking vs. retail + airline), and still replicates C1 (Δ=29.8pp, p<0.001) with consistent type ranking (ρ=0.77, p=0.038). This is the strongest form of independent replication available.

---

## Weaknesses

### W1: Multiple Comparison Correction Missing for C2 Pairwise Claims (R1, acknowledged by R2)
**Severity: Minor but should be addressed.**
The omnibus χ² for C2 (p=3.6×10⁻⁵) is fine, but the paper makes specific pairwise claims about the three-tier structure without formal correction. With 15 pairwise comparisons, Bonferroni or Holm correction should be applied. The TOST analysis partially addresses this by testing equivalence rather than difference, but the tier boundaries still rely on uncorrected pairwise contrasts.

*Recommendation*: Apply Holm-Bonferroni to the 15 pairwise comparisons and report adjusted p-values. The three-tier structure will likely survive given the effect sizes, but this needs to be shown explicitly.

### W2: Reproducibility Details Insufficient (R1, confirmed by R2)
**Severity: Moderate — addressable in revision.**
The paper lacks:
- Temperature settings for all models (critical for reproducibility of stochastic effects)
- Exact prompt templates used for agent instructions and judge evaluations
- API version dates (model behaviors change across versions)
- Seed/sampling parameters
- Cost information

The promise to "release all 300 clause pairs, evaluation scripts, and analysis code" is good but doesn't substitute for methodological details in the paper itself. Reviewers should be able to assess the methodology without running the code.

*Recommendation*: Add a methodology details subsection (can go in appendix) with temperature, prompt templates, API versions, and random seeds.

### W3: Moderate κ for Failure Mode Taxonomy (Both reviewers)
**Severity: Moderate — honestly reported but limits C5 claim strength.**
κ=0.52 (Gwet's AC1=0.68) for human re-annotation is moderate. While the paper correctly reports this with the kappa paradox caveat and notes 5/6 types have consistent dominant modes, the taxonomy's reliability is the weakest evidence link. Only 2 annotators on 100 traces is a small-scale validation. The coreferential type's genuine disagreement (human vs. automated coders on dominant mode) is informative but also means the taxonomy doesn't fully generalize.

*Recommendation*: Acknowledge more explicitly that C5 findings should be considered preliminary. Consider whether "validated" (used in abstract) overstates the evidence — "supported by human re-annotation" might be more precise given κ=0.52.

### W4: Per-Cell Sample Size for C4 Interaction Is Small (R1)
**Severity: Minor for the main claim, moderate for finer-grained interpretation.**
Each cell in the 5×6 model×type matrix contains only N=50 observations. The headline finding (auth_scope 52pp range) is large enough to be robust, but finer-grained interpretations (e.g., cond_prec's 6pp range being "model-invariant") may be underpowered. A 6pp range across 5 models with N=50/cell could easily arise by chance. The paper should be more careful about distinguishing "no significant difference" from "proven invariance."

*Recommendation*: Add CIs for per-cell rates or per-type ranges. Interpret the 6pp cond_prec range more cautiously — absence of evidence ≠ evidence of absence.

### W5: Disambiguation Channel Framework Is Observational (R2, confirmed by R1)
**Severity: Minor — the paper acknowledges this.**
The disambiguation channel explanation (ling ambiguity has external resolution channels → higher ICC, lower violation rates; spec ambiguity has no channels → lower ICC, forced guessing) is compelling as a framework but not causally tested. The convergent evidence (ICC pattern + failure mode dissociation + violation rates) is suggestive but could be circular: all three measures are derived from the same episodes. The paper correctly notes "a manipulation experiment...would test the causal mechanism."

*Recommendation*: No change needed — the paper handles this well. The framework's value is in generating testable predictions for future work.

### W6: Missing Related Work (R2)
**Severity: Minor.**
- No citation of Poesio (2004) or other computational/formal ambiguity work from the NLP side
- The connection to constitutional AI / RLHF could be developed more (the paper mentions RLHF for Claude but doesn't engage with the RLHF literature)
- Recent work on LLM robustness to specification underspecification could be cited
- Wasow et al. (2005) on ambiguity avoidance in production could contextualize the Ambiguity Blindness finding

### W7: SOPBench Replication Is Incomplete (R1)
**Severity: Minor.**
The SOPBench replication tests only 4 types (incompleteness, auth_scope, lexical, cond_prec) — scopal and coreferential appear excluded. Individual domain correlations (ρ=0.80, p=0.200) are non-significant due to N=4 types, making the per-domain evidence weaker than it appears. The pooled ρ=0.77 (p=0.038) is significant but with only 4 data points, individual outliers could drive the correlation.

---

## Questions for Authors

1. What temperature settings were used across all 5 models? Were they consistent?
2. The logistic regression controls for token_delta but not for domain (retail vs. airline). Could domain-specific effects confound the type hierarchy?
3. For the perturbation control, were the same clauses used for both perturbation and ambiguity conditions, or different subsets?
4. The paper mentions 5 × 300 × 2 = 3,000 expected episodes but reports 2,997. What happened to the missing 3 episodes?
5. How were the "expert annotators" for judge calibration selected? Were they aware of the study hypotheses?
6. The classifier PoC (Appendix A) uses 500 clauses but the main study has 300 pairs = 600 clauses. Where do the extra/missing clauses come from?

---

## Roundtable Convergence Notes

**R1 and R2 agreed on:**
- C1 is unassailable (both: this is the paper's strongest claim)
- C4 is the most exciting finding (both: actionable, surprising, well-supported)
- C3 honesty is commendable (both: correct decision to hedge)
- The paper is well-written and well-structured
- Missing reproducibility details are the most actionable weakness

**R1 and R2 diverged on:**
- **Overall score**: R1 at 3.5, R2 at 4.0. R1's lower score reflects concern about reproducibility details and moderate κ. R2's higher score reflects excitement about novelty and practical impact. After cross-sharing, R1 acknowledged the novelty strengthens the case but maintained that reproducibility gaps should be addressed before conference acceptance. R2 acknowledged the methodological concerns but argued they're all addressable in revision and don't undermine the core contributions.
- **Converged at 3.5** — borderline conference. The paper is above Findings threshold and could reach Conference with specific revisions (reproducibility details, multiple comparison corrections, tighter C5 hedging).

---

## Verdict

**ARR Overall Assessment: 3.5 (Borderline Conference)**

This paper makes a genuinely novel and practically important contribution — the first causal measurement of ambiguity→safety violations in LLM agents, with the perturbation control being unprecedented methodological rigor for this subfield. The model×type interaction (C4) is the star finding and would change how practitioners think about agent safety. The honest reporting of C3 fragility demonstrates scientific integrity.

The paper falls short of a clean 4.0 (Conference) primarily due to: (1) insufficient reproducibility details (temperature, prompts, API versions), (2) missing multiple comparison corrections for C2 pairwise claims, and (3) moderate κ=0.52 for failure mode validation with only 2 annotators on 100 traces, while the abstract uses "validated." These are all addressable in a revision cycle.

**Pathway to 4.0**: Add reproducibility details to appendix, apply Holm-Bonferroni to C2 pairwise comparisons, soften "validated" to "supported by human re-annotation" in abstract, add CIs for per-cell C4 rates.

**Pathway to 4.5**: Additionally, conduct the manipulation experiment for disambiguation channels (inject disambiguation info into tool responses), increase human annotation scale (more annotators, more traces), and develop the RLHF connection more deeply.

**Risk of desk reject**: Low. The paper has a Limitations section, anonymous submission, appears within 8-page limit, and has a proper reference list. No obvious compliance issues with EMNLP 2026 formatting requirements.

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