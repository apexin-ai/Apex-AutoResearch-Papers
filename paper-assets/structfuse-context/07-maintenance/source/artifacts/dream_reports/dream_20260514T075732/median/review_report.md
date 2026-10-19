---
dream_id: dream_20260514T075732
tier: median
overall_score: weak reject
timestamp: 2026-05-14T08:36:30.193110+00:00
---

# Dream Review Report: "What Makes Hard Negatives Work for Code Retrieval?"

**Dream ID:** 20260514T075732 | **Review Mode:** full | **Date:** 2026-05-14

---

## Paper Summary

This paper presents a controlled comparison of three hard negative mining strategies for contrastive code retrieval—random, embedding-distance, and dataflow-aware (via CodeQL inter-procedural analysis)—across two code encoders (Qwen2.5-Coder-3B, StarCoder2-3B) with distinct representation geometries. The main findings are: (1) embedding-distance mining provides directional improvement over random (+0.5–1.3pp R@1 on RepoBench-R), (2) dataflow-grounded negatives yield inconsistent effects across encoders, and (3) no strategy achieves significant downstream gains on SWE-bench Lite (all p > 0.3). The paper positions itself as an EMNLP analysis paper with methodology contributions: a controlled comparison framework, representation geometry analysis, and a CodeQL extraction pipeline.

---

## Reviewer Panel

| Reviewer | Focus | Score | Confidence |
|----------|-------|-------|------------|
| R1 | Methods + Experiments | 4/6 (Weak Accept) | 4/5 |
| R2 | Novelty + Related Work | 3/6 (Weak Reject) | 4/5 |

---

## R1 Review: Methods and Experiments

### Strengths

- **Rigorous experimental protocol.** ~54 training runs with paired bootstrap CIs on SWE-bench is commendable. The controlled comparison genuinely isolates the negative selection variable while holding all other training details constant.
- **Comprehensive ablation suite.** Each ablation answers a specific question: temperature sensitivity (Tables 7–8), hop depth (Table 9), data scaling (Table 10), fusion head (Table 11), weighted vs. binary dataflow (Table 12), static vs. dynamic mining (Table 13). The ablation coverage is thorough for this subfield.
- **Honest reporting of null and conditional results.** The paper openly reports that SWE-bench shows no significant differences, that dataflow negatives are inconsistent, and that effect sizes diminish with data scale. This is appropriate for an analysis paper.
- **Failure analysis (§4.3) provides genuine insight.** The decomposition showing 44% generation failures vs. 36% retrieval misses cleanly explains the downstream null result and provides useful signal for the community.
- **Temperature robustness.** The finding that embedding > random direction is consistent across all τ values (Tables 7–8) strengthens the directional claim beyond a single hyperparameter setting.

### Weaknesses

1. **N=2 encoders fundamentally limits the representation geometry claim.** The paper's central analytical contribution—linking encoder-strategy interaction to representation saturation—rests on exactly two data points. The pos_sim values (0.9855 vs. 0.7985) are an observation, not a validated mechanism. Any two encoders will differ in some metric; without testing whether pos_sim is predictive across 4–5 additional encoders, the "representation geometry" framing overpromises.

2. **Missing BM25 negative baseline—the single most important omitted experiment.** The paper's narrative begins with correcting CoCoHaNeRe's conflation of BM25 and embedding-distance negatives. Yet the paper never runs BM25 negatives in its own framework. This experiment would (a) verify that BM25 negatives indeed harm performance, (b) quantify the gap between BM25-proxy and true embedding-distance mining, and (c) close the paper's own argument loop. Without it, the correction claim is asserted but unverified.

3. **No error bars or confidence intervals on RepoBench-R results (Table 1).** The main retrieval results lack any statistical significance testing—no seeds, no CIs, no p-values. For an analysis paper emphasizing statistical rigor (bootstrap CIs on SWE-bench), this inconsistency is glaring. The +0.5pp StarCoder improvement could easily be within noise.

4. **Pool size of 50 candidates per query is unrealistically small.** Real repositories have hundreds to thousands of files. A pool of 50 inflates absolute R@1 values and may not preserve strategy ranking at realistic pool sizes. No sensitivity analysis on pool size is provided.

5. **StarCoder2-3B is mischaracterized as "encoder-decoder" (§3.5).** StarCoder2-3B is a decoder-only model, same architectural class as Qwen2.5-Coder-3B. The actual difference is in pretraining data/procedure, not architecture. This factual error undermines the "architecturally distinct" framing.

6. **Table 6 repo-complexity analysis has N=1 in the smallest tier.** The "<50 instances" tier contains a single repository, making the +2.1pp data point anecdotal. This tier should be excluded or merged, and the correlation analysis (r=−0.41, p=0.08) should be recomputed without it.

7. **SWE-smith validation results are referenced but never shown.** The paper mentions "consistent with SWE-smith validation results" (§4.1) but the SWE-smith validation table is absent. These are presumably the primary evaluation results—their omission is surprising.

8. **34% structural data coverage is underreported as a limitation.** Only 34% of training instances actually receive dataflow-mined negatives; the rest fall back to alternative selection. The reported effects average over both populations, diluting the true signal. A stratified analysis (structured vs. fallback instances) is needed.

9. **Checkpoint selection criterion is unspecified.** With documented overfitting after step 1000, the choice of "best checkpoint" could reverse strategy rankings. The criterion (validation metric, early stopping patience) should be explicitly stated.

### Questions for Authors

1. What is the per-instance effect of dataflow negatives stratified by whether structural data was available (34%) vs. not?
2. Why were SWE-smith validation results omitted from the paper despite being referenced?
3. Have you tested sensitivity to pool size (e.g., pool=100, 200, 500)?
4. What is the checkpoint selection criterion, and how sensitive are strategy rankings to this choice?
5. Can you run a BM25 negative baseline to close the CoCoHaNeRe correction argument?

---

## R2 Review: Novelty and Related Work

### Strengths

- **CoCoHaNeRe correction has community value.** If BM25-proxy negatives were indeed mislabeled as embedding-distance, clarifying this matters for practitioners and could redirect research effort.
- **Honest reporting of null results.** The paper does not hide that dataflow negatives are inconsistent, SWE-bench shows no significant differences, and CIs include zero for StarCoder. This candor is increasingly valuable in ML research.
- **Potentially actionable pos_sim diagnostic.** If validated on more encoders, the observation that pos_sim correlates with mining strategy effectiveness could become a cheap pre-training diagnostic for practitioners.
- **Clean separation of training-time vs. inference-time value.** The fusion head ablation (Table 11) demonstrates that structural information's value is in negative selection, not inference-time scoring—a crisp methodological insight.
- **"Directional evidence" framing is appropriately calibrated** for the evidence strength. The paper does not overclaim given the data.

### Weaknesses

1. **"First controlled comparison" novelty claim is overstated.** The paper claims to be the "first controlled comparison using true embedding-distance negatives for code retrieval." ANCE-style mining (using actual embedding distance) has existed since 2021 and has been applied broadly. The claim that nobody has done this for code requires more thorough documentation than critiquing a single paper.

2. **CoCoHaNeRe critique is the paper's central motivation but remains unverified.** The entire narrative depends on CoCoHaNeRe using BM25-proxy negatives mislabeled as embedding-distance. Yet the paper never: (a) provides specific textual evidence from CoCoHaNeRe showing the mislabeling, (b) reproduces the CoCoHaNeRe setup with BM25 negatives, or (c) runs BM25 negatives in its own framework. Without a BM25 baseline experiment, the "correcting a misconception" claim is speculative.

3. **Representation geometry analysis is shallow despite impressive terminology.** The substance is: one encoder has pos_sim=0.99 and the other has pos_sim=0.80, and they respond differently. With n=2, this is anecdotal. The paper does not connect to existing contrastive learning theory on negative difficulty (Robinson et al. 2021, Kalantidis et al. 2020) or provide any formal relationship between pos_sim and expected mining benefit.

4. **Significant related work gaps for a "systematic study":**
   - Hard negative theory: Robinson et al. 2021, Kalantidis et al. 2020
   - Contrastive learning foundations: SimCLR, MoCo
   - Code representation baselines: CodeBERT, UniXcoder, CodeT5+
   - Structural code methods: CodeGRAG, GraphCoder, RepoGraph
   - Curriculum-based mining: mentioned but never cited or compared

5. **CodeQL pipeline is an engineering artifact, not a research contribution.** "123 repos processed with zero timeouts" is a reliability metric for a tool. The 34% instance-level coverage is the scientifically relevant number, and it is a significant limitation that makes Contribution (3) underwhelming.

6. **Dataflow method is introduced and shown not to work, but still framed as a contribution.** The dataflow strategy is +0.6pp on Qwen RepoBench-R but −0.6pp on StarCoder, and −0.3pp on SWE-bench Lite. The "conditional benefit mediated by representation saturation" framing repackages a negative result. The honest conclusion is that dataflow negatives failed to demonstrate consistent value.

7. **Effect sizes are too small for practical relevance.** +0.5–1.3pp R@1 with CIs including zero on half the setups. Table 14 is self-damaging: StructFuse gets +0.5–1.5pp while CodexGraph gets +5.2pp. The cost-benefit of a CodeQL extraction pipeline for +0.5pp is hard to justify.

8. **No comparison with other training-time hard negative mining approaches.** The paper compares random, static embedding, and dataflow but omits ANCE-style dynamic mining as a proper baseline, in-batch negatives (DPR-style), and curriculum-based approaches. For a paper titled "systematic study," the strategy space is narrow.

9. **Broken bibliography.** All references appear as [?], making it impossible to verify the claims about prior work. This is a serious presentation issue.

### Questions for Authors

1. Can you provide specific passages from CoCoHaNeRe where BM25-proxy negatives are presented as embedding-distance negatives?
2. Have you measured pos_sim for any encoders beyond Qwen and StarCoder?
3. Why were ANCE-style dynamic mining, in-batch negatives, and curriculum-based mining excluded from the comparison?
4. The data scaling ablation (Table 10) shows benefit diminishing from +1.8pp to +0.9pp as data grows. What is your estimate at 50K+ instances?
5. Why is "StructFuse" used as a system name when the paper is positioned as an analysis? Does the name set incorrect expectations?

---

## Roundtable: Cross-Reviewer Discussion

### Points of Agreement (Both Reviewers)

1. **Missing BM25 baseline is the most critical gap.** Both reviewers independently identify this as the experiment most needed to substantiate the paper's central narrative. Without it, the CoCoHaNeRe correction claim—which motivates the entire paper—is unverified.

2. **N=2 encoders is insufficient for the representation geometry claim.** Both reviewers agree this limits the contribution from a "validated mechanism" to an "anecdotal observation." The framing should be significantly downgraded.

3. **StarCoder2-3B architecture is mischaracterized.** Both flag that calling it "encoder-decoder" is factually incorrect (it is decoder-only), which weakens the "architecturally distinct" narrative.

4. **Ablation breadth is a genuine strength.** Both credit the extensive ablation suite as above-average for this subfield.

5. **Honest reporting is commendable.** Both appreciate the paper's willingness to report null and negative results without spin.

6. **Effect sizes are too small for practical impact.** Both note that +0.5–1.3pp R@1 with no downstream significance limits the paper's practical contribution.

7. **Missing error bars on RepoBench-R** is inconsistent with the statistical rigor shown on SWE-bench.

### Points of Disagreement → Resolution

- **R1 (4/6) vs. R2 (3/6) on overall score.** R1 is more generous toward the methodology framework as a standalone contribution; R2 argues the novelty is thin and the central narrative is unsubstantiated. After cross-sharing, both agree the missing BM25 baseline is disqualifying for the "correcting CoCoHaNeRe" framing, which is the paper's primary motivation. R1 adjusts downward; the consensus trends toward **3/6 (Weak Reject)** with a path to revision.

- **Is the "analysis paper" positioning sufficient?** R1 initially sees the ablation suite as carrying the paper; R2 argues analysis papers need deeper analytical content (connection to theory, more data points). Consensus: the ablations are thorough but the analysis layer (representation geometry) is too shallow to stand as a primary contribution.

---

## Consolidated Assessment

### Summary Judgment

The paper tackles a relevant question—what hard negative mining strategies work for code retrieval—with above-average experimental discipline. The ablation breadth, honest null-result reporting, and controlled comparison design are genuine strengths. However, the paper has several critical gaps that prevent acceptance at a top venue:

1. **The central narrative is unsubstantiated.** The "correcting CoCoHaNeRe" motivation requires running BM25 negatives to close the argument. Without this, the paper's raison d'être is speculative.

2. **The analytical contribution is too shallow.** "Representation geometry" with n=2 encoders is an observation. Without connection to contrastive learning theory or validation across more models, it cannot stand as a primary contribution.

3. **Effect sizes are marginal.** +0.5–1.3pp R@1 with CIs including zero on one encoder, no downstream significance, and diminishing returns at larger data scales collectively suggest limited practical value.

4. **Presentation issues.** Broken bibliography ([?] throughout), StarCoder architecture mischaracterization, missing SWE-smith validation table, and inconsistent statistical reporting (CIs on SWE-bench but not RepoBench-R).

### What Would Improve the Paper

- Run a BM25 negative baseline to close the CoCoHaNeRe argument
- Add 2–3 more encoders with varying pos_sim to validate the saturation hypothesis
- Provide error bars/CIs on RepoBench-R results across multiple seeds
- Fix the bibliography and the StarCoder architecture description
- Add pool-size sensitivity analysis
- Connect to hard negative theory literature (Robinson et al., Kalantidis et al.)
- Stratify dataflow results by structural data availability (34% with data vs. 66% fallback)

### Experiment Coverage vs. Design

All 13 imagined experiments are reflected in the paper: SWE-bench Lite (Tables 2–3), RepoBench-R (Table 1), repo complexity (Table 6), hop depth (Table 9), data scaling (Table 10), fusion head (Table 11), weighted vs. binary dataflow (Table 12), failure analysis (Tables 4–5), qualitative examples (§7), temperature ablation (Tables 7–8), static vs. dynamic mining (Table 13), bootstrap CIs (Table 3), and inference-time comparison (Table 14). Coverage is complete. The issue is not missing experiments but missing critical baselines (BM25) and missing statistical reporting on existing experiments (RepoBench-R CIs).

---

## Final Scores

| | Score | Confidence |
|---|---|---|
| R1 (Methods + Experiments) | 4/6 → 3/6 after roundtable | 4/5 |
| R2 (Novelty + Related Work) | 3/6 | 4/5 |
| **Consolidated** | **3/6 (Weak Reject)** | **4/5** |

### Decision Rationale

The paper demonstrates solid experimental practice but fails to substantiate its central narrative (CoCoHaNeRe correction without BM25 baseline), offers insufficient analytical depth for an analysis paper (representation geometry on n=2), and reports effect sizes too small for practical significance. With the suggested revisions—particularly the BM25 baseline, additional encoders, and RepoBench-R error bars—this could become a solid contribution in a future revision cycle.
