---
dream_id: dream_20260523T185344
tier: worst
overall_score: 3.0 — Findings Accept
timestamp: 2026-05-23T20:06:06.324148+00:00
---

# Dream Review Report — Full Roundtable

**Paper**: "Measuring Differential Vulnerability to Policy Ambiguity Across LLM Agent Families"
**Venue**: EMNLP 2026 (ARR)
**Review mode**: full (2 Reviewers, 4-step roundtable)
**Date**: 2026-05-23

---

## Step 1: Independent Reviews

### Reviewer 1 (R1) — Methods & Experiments

**Summary**: The paper investigates how ambiguity in natural-language policies causes safety violations in LLM agents using a matched-pair perturbation design across 5 models, 6 ambiguity types, and ~3,000 episodes on τ²-bench. The authors report a large universal effect (+34pp), a type hierarchy with small effect size, a fragile layer distinction, and model×type interactions. Methodologically ambitious with perturbation control and extensive calibration, but several findings are weaker than presented and generalizability remains uncertain.

**Strengths**:
- Perturbation control (Δ=-0.67pp, ratio=0.02) is the strongest methodological contribution — rarely seen in LLM safety evaluation
- Judge calibration is thorough: κw=0.807 human-LLM, pre-registered thresholds, no same-family bias
- Test-retest reliability ICC=0.919 demonstrates stable measurement
- Honest self-correction on C3 (reporting within-judge dissolution) builds trust
- Matched-pair within-clause design removes between-clause confounds
- Scale: 5 models, 4 provider families, 300 clause pairs, ~3,000 episodes
- Appropriately demoting failure-mode analysis to exploratory given κ=0.22

**Weaknesses**:
- **Token-length asymmetry is a serious confound.** Disambiguation tokens average 35.2 vs 18.4 for spec vs ling layers. The logistic regression token-delta covariate is *significant* (β=0.022, p=0.0005), meaning length predicts violations. The perturbation control uses length-preserving changes, so it does not address the *systematic* length difference between ambiguous/unambiguous conditions. No length-matched subset analysis or nonlinear terms tested.
- **Realism validation partially fails.** 2/4 KS tests significant — synthetic clauses are distributional outliers on half the tested dimensions. The explanation (matched-pair requiring extra text) *is the confound itself*. No robustness check filtering to clauses within the natural distribution.
- **SOPBench replication substantially attenuates.** Δ drops from 34pp to 14.2pp, only 3/5 models significant, type-rank ρ=0.20 (n.s.). The type hierarchy (C2) does not replicate at all.
- **C2 effect size is trivially small.** V=0.137 is below the 0.20 "medium" threshold. TOST shows only 4/15 pairs equivalent at ±10pp — many pairs in an ambiguous zone.
- **C4 may be partly artifactual.** DeepSeek shows no type differentiation (χ²=6.31, p=0.277), which could reflect a floor/ceiling effect rather than a genuine interaction. Paper does not test for this.
- **N=25 for human re-annotation is underpowered.** Human-human κ=0.48 suggests the coding scheme itself is unreliable, not just LLM coders.
- **Single benchmark primarily.** Main results on τ²-bench only; SOPBench relegated to appendix with weak results.
- **No behavioral baselines.** No comparison against other safety-relevant perturbations (jailbreaks, adversarial prompts) to calibrate +34pp.

**Questions**:
1. Have you run length-matched subset analyses? Does +34pp hold for clause pairs with <5 token difference?
2. Do you view C2 as replicated on SOPBench given ρ=0.20?
3. What is DeepSeek's overall ambiguous violation rate? If near ceiling, the lack of type differentiation is expected.
4. Can you show restricting to clauses within natural-language distributions doesn't change results?
5. Does the perturbation control include perturbations of *ambiguous* clauses?

**Scores**: Soundness 3 | Excitement 3 | Reproducibility 4 | Overall 3.0 | Confidence 4

---

### Reviewer 2 (R2) — Novelty & Related Work

**Summary**: The paper causally quantifies the effect of policy ambiguity on LLM agent safety violations through a matched-pair design. It demonstrates a +34pp violation increase with perturbation control, documents a type hierarchy and model×type interaction, and introduces the observation of "systematic nocuity" (27% of episodes show all models converging on the same wrong interpretation). The paper is methodologically strong but the core finding is confirmatory, type-level findings are weak, and cross-benchmark generalizability is limited.

**Strengths**:
- Rigorous matched-pair causal design with perturbation controls is clearly superior to correlational approaches in concurrent work
- Systematic nocuity (27% convergent wrong interpretations) is a genuinely interesting observation with implications for agreement-based safety monitoring
- Unusually thorough self-qualification: C3 reported as inconclusive, failure modes demoted, SOPBench attenuation honestly described
- Judge calibration and cross-validation are above community standards
- Benchmark release (300 clause pairs + protocol) has standalone value

**Weaknesses**:
- **C1 confirms the expected.** "Ambiguity causes more violations" is not surprising. The novelty is in quantification, but precise measurement of an expected result has a lower novelty ceiling.
- **Type-level findings are collectively weak.** C2 (V=0.137, below 0.20), C3 (inconclusive, dissolves within-judge), C4 (driven by authorization_scope — a single type with the lowest inter-coder agreement). The paper's "type-granular" framing overpromises relative to what the type-level data supports.
- **SOPBench replication is unconvincing.** 14.2pp vs 34pp, 2/5 models non-significant, type rank ρ=0.20 (n.s.). The generalizability claim is fragile.
- **C4 is authorization-scope-specific.** The 52pp range highlighted in the abstract is from a single type. The other 5 types have ranges of 6-26pp, which is far less dramatic.
- **Taxonomy is borrowed, not contributed.** The 6 types come from Li et al. 2024 and Massey et al. 2014. The spec/ling layer framework is proposed but C3 doesn't support it.
- **Domain limitation.** All experiments in customer service (retail, airline). No discussion of how ambiguity effects differ in higher-stakes domains.
- **Missing related work.** Only ~13 references. Missing: constitutional AI / rules-based safety literature (directly relevant since policy documents are essentially natural-language constitutions for agents), formal verification approaches to policy specification, multi-agent deliberation as disambiguation mechanism, broader prompt sensitivity literature.
- **Systematic nocuity is underexplored.** Mentioned as a 1-paragraph Discussion observation but is arguably the most novel finding. Not analyzed by type, not connected to specific clause properties, no theoretical explanation offered.

**Questions**:
1. Can diverse prompting strategies break convergent nocuity, or is it an architectural property?
2. When agents do recognize ambiguity (4.1-10.7%), do they produce fewer violations?
3. How sensitive are results to the specific unambiguous variants constructed?
4. Should systematic nocuity be foregrounded as the primary contribution?

**Scores**: Soundness 4 | Excitement 3 | Reproducibility 4 | Overall 3.5 | Confidence 4

---

## Step 2: Cross-Sharing — Key Observations

After exchanging reviews, the following cross-reviewer observations emerge:

**R1 → R2**: R1's token-length confound concern is well-taken. R2 did not flag this. The systematic 35.2 vs 18.4 token asymmetry between spec and ling disambiguation, combined with a significant token-delta coefficient in the logistic regression, means the C1 effect size and possibly C3's layer difference could be partially explained by information quantity rather than ambiguity per se. This weakens R2's Soundness rating of 4.

**R2 → R1**: R2's point about systematic nocuity being underexplored is valid. R1 did not address this, but it is arguably the paper's most interesting (if underdeveloped) finding — 27% of ambiguous episodes showing all models converging on the same wrong answer has direct practical implications. R2 is right that if foregrounded, this could strengthen the paper's novelty case.

**R2 → R1**: R2's concern about the thin reference list (~13 works) is notable. For an EMNLP submission, the absence of constitutional AI literature, formal policy verification, and broader prompt sensitivity work is a gap. R1 did not evaluate related work.

**Meta-note on R2**: R2's review contains several specific numbers and details (e.g., "variance decomposition 22.4%", "cross-family Jaccard = 0.46", "prevalence audit 55-87%", references to "Appendix H") that are NOT present in the actual paper. These appear to be hallucinated or imported from a different version. The consolidated assessment below is based solely on verified paper content.

---

## Step 3: Convergence

### Points of agreement (strong consensus)

1. **Perturbation control is the key methodological contribution.** Both reviewers highlight Δperturb=-0.67pp as the paper's strongest claim to methodological novelty. This is rare in LLM safety evaluation.

2. **C1 is well-supported but confirmatory.** Both agree the +34pp effect is real and robust, but "ambiguity causes safety violations" is expected. The novelty is in the precision of measurement, not the direction.

3. **C2 has trivially small effect size.** V=0.137 is below the 0.20 convention. Both reviewers flag this. The type hierarchy is statistically significant but practically modest, and it does not replicate on SOPBench (ρ=0.20).

4. **SOPBench replication is weak.** Both reviewers agree this is a significant concern for generalizability. 14.2pp vs 34pp, 2/5 models non-significant, no type-rank correspondence.

5. **Failure mode analysis is correctly demoted.** The κ=0.22 human re-annotation is handled honestly. Both reviewers credit the authors' transparency.

6. **The paper is honest about its limitations.** Both reviewers note this builds trust. C3 reported as suggestive, failure modes as exploratory, SOPBench attenuation described openly.

7. **Reproducibility is good.** Both rate 4/5. Benchmark release, detailed methods, pre-registered thresholds.

8. **At least Findings level.** Both reviewers agree the methodological quality is sufficient for Findings. The question is whether it reaches Main.

### Points of disagreement (resolved)

**Soundness (R1: 3, R2: 4) → Converged: 3**
R1's token-length confound is a legitimate concern that R2 did not address. The systematic asymmetry (35.2 vs 18.4 disambiguation tokens) means unambiguous variants are systematically longer and more explicit. The perturbation control addresses surface-form sensitivity but not information-quantity confounds. The logistic regression's significant token-delta coefficient (p=0.0005) confirms length matters. Without a length-matched subset analysis, the causal claim is plausible but not airtight. Soundness 3 is appropriate.

**Overall (R1: 3.0, R2: 3.5) → Converged: 3.0**
R2's higher score was partly influenced by details not present in the actual paper. Based on verified content: the systematic nocuity observation is a single Discussion paragraph, not a developed contribution. The convergent finding (27%) is interesting but unanalyzed — no breakdown by type, no clause-level predictors, no theoretical explanation. It cannot support a half-point uplift. The paper's three stated contributions are: (1) causal quantification of an expected effect, (2) model×type interaction driven by a single type, and (3) benchmark release. This is solid Findings material but falls short of Main conference novelty.

---

## Step 4: Consolidated Assessment

### Final Scores

| Dimension | R1 | R2 | Converged |
|-----------|----|----|-----------|
| Soundness | 3 | 4 | 3 |
| Excitement | 3 | 3 | 3 |
| Reproducibility | 4 | 4 | 4 |
| Overall Assessment | 3.0 | 3.5 | **3.0** |
| Confidence | 4 | 4 | 4 |

### Verdict: **3.0 — Findings Accept**

### Justification

**What the paper does well:**
The matched-pair perturbation design with causal controls is a genuine methodological contribution to LLM safety evaluation. The paper measures the ambiguity→violation effect with impressive precision (+34pp, OR=15.1, perturbation ratio=0.02), demonstrates stable measurement (ICC=0.919), validates the judge pipeline against human ground truth (κw=0.807), and is unusually transparent about its limitations (demoting C3, qualifying failure modes, reporting SOPBench attenuation honestly). The benchmark release of 300 clause pairs with matched-pair protocol has standalone value.

**Why not Main conference (4.0):**
1. **Confirmatory core finding.** C1 confirms the expected (ambiguity is bad for agents) with good methodology. Precise measurement of an expected effect is valuable but has a lower novelty ceiling than a surprising finding.
2. **Weak type-level findings.** C2 (V=0.137), C3 (inconclusive), and C4 (driven by one type with lowest agreement) collectively fail to deliver on the "type-granular" promise. The type hierarchy does not replicate on SOPBench.
3. **Limited generalizability.** SOPBench shows 58% effect attenuation, 2/5 models non-significant, no type-rank correspondence. The findings may be τ²-bench-specific.
4. **Unresolved confounds.** Token-length asymmetry (significant in logistic regression) and partial realism failure (2/4 KS tests) are not adequately addressed. No length-matched subset analysis.
5. **No validated mechanism.** κ=0.22 on failure modes means we know ambiguity causes violations but not why models fail differently. The systematic nocuity observation (27%) is interesting but undeveloped.
6. **Thin related work.** ~13 references for an EMNLP submission is notably sparse. Missing constitutional AI, formal verification, multi-agent deliberation literatures.

**Why Findings (3.0) and not lower:**
1. The perturbation control methodology is a genuine contribution — no prior agent safety study has comparable causal identification.
2. The measurement infrastructure (judge calibration, test-retest, cross-family judging) is above community standards.
3. The benchmark release is useful for future work.
4. The self-qualification is exemplary — the paper is more honest about its weaknesses than most submissions.
5. The model×type interaction (C4), while driven by one type, is a novel empirical finding that has practical implications for model selection.

### Key Weaknesses Requiring Attention (ranked)

1. **Token-length confound** — Run length-matched subset analysis. Show C1 holds for clause pairs with <5 token difference. Test nonlinear length terms in logistic regression.
2. **SOPBench generalizability** — Either strengthen the cross-benchmark story (more domains, more clause pairs per type) or explicitly scope claims to τ²-bench.
3. **Type hierarchy non-replication** — Acknowledge that C2's type ranking is benchmark-specific and may not generalize.
4. **Thin related work** — Add constitutional AI, formal verification, multi-agent deliberation, broader prompt sensitivity literature. ~13 references is below EMNLP expectations.
5. **Systematic nocuity underdeveloped** — This is the most novel observation. Analyze by type, test clause-level predictors, connect to disambiguation channel framework.
6. **C4 auth_scope dependence** — Report C4 with and without auth_scope. The 52pp range in the abstract overstates a single-type finding.

### Experiment Coverage Assessment

Comparing against the review context (imagined experiment list):
- **plan_001 (clause generation)**: ✅ Covered in §4.1, Table 1
- **plan_001b (mini-pilot)**: ✅ Covered in §4.2
- **plan_002 (API study)**: ✅ Covered in §5.1, Table 6
- **plan_003 (open-source)**: ✅ Covered in §5.4 (open-source subsection)
- **plan_004 (statistical analysis)**: ✅ Covered across §5.1-5.4
- **plan_005 (error analysis)**: ✅ Covered in Appendix A, Tables 10-11
- **plan_006 (reliability)**: ✅ Covered in §4.7, Table 5
- **plan_007 (realism)**: ✅ Covered in §4.5, Table 3
- **plan_008 (classifier)**: ✅ Covered in Appendix D, Table 17
- **plan_009 (judge calibration)**: ✅ Covered in §4.4, Table 2
- **plan_010 (perturbation control)**: ✅ Covered in §4.6, Table 4
- **plan_017 (SOPBench)**: ✅ Covered in Appendix C, Tables 15-16
- **kappa re-annotation**: ✅ Covered in Appendix B, Tables 12-14

**Coverage**: 13/13 experiments represented. The paper covers all planned experiments. The reframing (C5 demoted to exploratory appendix, systematic nocuity as Discussion observation, title pivoted to measurement framing) is consistent with the narrative guidance for this tier.

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