---
dream_id: dream_20260515T060408
tier: worst
overall_score: borderline reject
timestamp: 2026-05-15T06:56:05.479961+00:00
---

# Dream Review Report: "When and Why Cross-Representation Disagreement Works"

**Dream ID**: 20260515T060408
**Review Mode**: Full (2 Reviewers + Roundtable)
**Date**: 2026-05-15

---

## Roundtable Process Summary

- **R1** (Methods + Experiments): Evaluated experimental design, statistical rigor, reproducibility
- **R2** (Novelty + Related Work): Evaluated contribution novelty, positioning, related work coverage
- **Step 1**: Independent reviews completed
- **Step 2**: Cross-sharing of findings — identified 6 consensus points and 2 divergence areas
- **Step 3**: Convergence on Borderline Reject; both reviewers agree contribution volume is below top-venue main track threshold despite genuine analytical insights
- **Step 4**: Synthesized report below

---

## Paper Summary

The paper investigates when and why cross-representation disagreement (CRD) — comparing FOL/Z3 outputs with Python code outputs for the same NL problem — provides effective diagnostic signal for LLM formalization errors. Rather than proposing CRD as a general framework, it characterizes applicability boundaries across four benchmarks (FOLIO, ProofWriter, MATH Level 5, GPQA Diamond), two model families, and multiple ablations. Key findings: CRD works well only on FOLIO (86.8% diagnostic precision, 9:1 error asymmetry) and degrades sharply elsewhere. Two necessary conditions are identified: asymmetric reliability between representations, and formalization-dominated errors. The repair mechanism is shown to be marginal (+5.2pp, p=0.078) and confounded by GT=Unknown samples.

---

## R1: Methods and Experiments

### Strengths

- **S1: Well-structured evaluation framework.** The five criteria (C1–C5) provide a clean, modular evaluation protocol. The separation of All-mode vs. Excl-Unknown for C4 is honest and analytically important — it directly reveals the Unknown confound rather than hiding it.

- **S2: Comprehensive ablation coverage.** The paper tests four benchmarks spanning formal logic to scientific reasoning, two model sizes (8B vs 32B), cross-model pipelines (Qwen + DeepSeek), multi-round repair, taxonomy-guided repair, and selection vs repair. This breadth is unusual for a paper of this scope.

- **S3: Statistical honesty.** The paper reports bootstrap CIs and Fisher's exact test for all key metrics, transparently shows that C4 is not significant (p=0.078, CI crosses zero), and includes a power analysis (Table 16) acknowledging ~280 samples needed for 80% power. This level of statistical candor is commendable.

- **S4: The Unknown confound analysis (§5.2.1) is the strongest methodological contribution.** Decomposing the C4 signal by GT label reveals that the entire repair advantage comes from Python's structural inability to implement three-valued logic — a representation limitation, not a diagnosis capability. Table 3 (Code-side error patterns on Unknown samples: 58.1% output True, 29.0% output False) makes this mechanism concrete and falsifiable.

- **S5: ProofWriter depth analysis (Table 5).** The monotonic relationship between reasoning depth and diagnostic signal quality (8.1% disagree at depth-0 → 26.7% at depth-5) provides empirical grounding for the "sufficient task complexity" condition and is a clean, interpretable result.

### Weaknesses

- **W1: Repair contribution fails to reach significance on any benchmark.** C4 All-mode is +5.2pp on FOLIO (p=0.078), +1.8pp on ProofWriter (p=0.31), −0.5pp on MATH (p=0.82). C4 Excl-Unknown is 0.0pp / −2.1pp / −3.2pp respectively. The paper acknowledges this but still dedicates substantial space (§5.7, Tables 12–14) to analyzing repair mechanisms that demonstrably don't work. This creates a tension: the paper spends ~2 pages analyzing a non-effect.

- **W2: CoT+SymPy on MATH is a fundamentally different "cross-representation" than FOL+Code.** FOL verified by Z3 has formal completeness guarantees for decidable fragments; CoT is informal natural language reasoning. Treating CoT–Code disagreement as the same phenomenon as FOL–Code disagreement conflates verified formal specification with unverified textual reasoning. The paper's "applicability spectrum" implicitly assumes these are the same mechanism applied in different domains, but they may be categorically different phenomena.

- **W3: Error taxonomy lacks validation.** The three-way classification (variable mapping / scope-quantifier / logic connective) is presented without inter-annotator agreement, without describing the classification procedure (manual? LLM-based? rule-based?), and with only descriptive value (taxonomy-guided repair: +1.0pp, p=0.68). For a contribution claimed in the abstract, this is underspecified.

- **W4: Prompt sensitivity is unexamined.** CRD performance depends heavily on formalization prompt quality — the paper notes this as a limitation (§6.3) but provides no analysis. Given that FOL/Code generation quality is prompt-dependent, a prompt sensitivity ablation (e.g., zero-shot vs. few-shot, different instruction styles) would substantially strengthen the claims about when CRD works.

- **W5: Sample sizes are modest for the claims made.** FOLIO (N=192), MATH (N=200), GPQA (N=150) yield small effective samples for disagree-conditional analyses. On FOLIO, only ~76 samples disagree; on MATH, ~24. The per-error-type analyses in Tables 13–14 have N=9–42 per cell. Power analysis (Table 16) confirms this but the paper still draws strong conclusions from underpowered comparisons.

- **W6: Reproducibility gaps.** The paper does not report: (a) exact prompts used for FOL/Code generation, (b) few-shot examples, (c) Z3 timeout settings, (d) Python execution sandboxing details, (e) model serving configuration (quantization, temperature, etc.). These are essential for reproduction given the prompt sensitivity acknowledged in §6.3.

### Questions for Authors

- Q1: How was the error taxonomy operationalized? Manual annotation, LLM-based, or rule-based? What is the inter-annotator agreement?
- Q2: For MATH, what justifies treating CoT–Code disagreement as the same phenomenon as FOL–Code disagreement, given that FOL has formal verification guarantees and CoT does not?
- Q3: Have you tested with different formalization prompts? How sensitive are C1/C2 to prompt design?
- Q4: The 9:1 FOL:Code error ratio is central to the asymmetric reliability argument. How is this computed? Is it the ratio of "Code-only errors" to "FOL-only errors" among disagreeing samples?

### R1 Scores

- Soundness: 3/5
- Contribution: 2/5
- Presentation: 4/5
- Overall: 3/6
- Confidence: 4/5

---

## R2: Novelty and Related Work

### Strengths

- **S1: Honest boundary characterization is rare and valuable.** Most papers in this space propose a method and show it works. This paper systematically shows where its method fails and why, which is more informative for the field. The "applicability spectrum" (FOLIO → ProofWriter → MATH → GPQA) with monotonically degrading metrics is a clean empirical contribution.

- **S2: The Unknown confound is a genuinely novel finding.** The discovery that FOLIO's C4 repair signal is entirely driven by GT=Unknown samples — where Z3 correctly returns Unknown but Python code structurally cannot implement three-valued logic — is a non-obvious insight. It warns future researchers against overgeneralizing from benchmarks with specific label distributions.

- **S3: The "diagnosis as analysis, not repair" reframing (§6.2) is well-supported.** The combination of evidence — selection > repair by 4.5pp, diminishing multi-round returns, taxonomy lacking prescriptive value, repair confounded by Unknown — converges on a coherent thesis that CRD's value is in detection and localization, not in guiding repair. This is a useful conceptual contribution.

- **S4: Cross-model ablation yields a non-obvious negative result.** The finding that model diversity reduces correlated failures by only 1.5pp (because the root cause is specification-level ambiguity in the NL, not shared model bias) challenges a natural assumption and has implications beyond this paper.

### Weaknesses

- **W1: Incremental over Liang et al. (2024).** The core insight that cross-representation disagreement is informative for error detection already exists. Liang et al. demonstrated CoT–PoT disagreement for filtering; this paper extends from "filtering" to "diagnosis" (identifying which side is wrong and what type of error) and adds boundary characterization. While the extension is real, the conceptual gap is modest — diagnosis via an LLM prompt that receives both outputs is a natural next step. The paper's primary novelty resides in the negative/boundary results, which are valuable but may not constitute sufficient contribution for a main track paper.

- **W2: Related work is severely under-cited.** Only 7 references for a 12-page paper at the intersection of neurosymbolic reasoning, LLM self-correction, and cross-representation methods. Major omissions include:
  - **Self-consistency** (Wang et al., 2023): samples multiple reasoning paths and takes majority vote — a cross-sample disagreement method directly relevant to the "agreement/disagreement as signal" theme
  - **LEVER** (Ni et al., 2023): uses verification to re-rank code generations — relevant to the selection vs. repair comparison
  - **Faithful CoT** (Lyu et al., 2023): generates both NL reasoning and symbolic code — closely related dual-representation approach
  - **Self-Debug / Self-Refine** (Chen et al., 2024; Madaan et al., 2023): LLM-driven code repair using execution feedback — directly relevant to the repair mechanism analysis
  - **Multi-agent debate** literature: conceptually related to using disagreement for error detection
  - **Ensemble/diverse verifier** literature in code generation

- **W3: Several bibliography entries appear incomplete.** "HybridMind," "Adaptive Selection," "VeriCoT," "VERGE," "Prove," and "Roundtrip Verification Authors" lack proper author names. This raises concerns about citation quality and whether all cited works have been carefully consulted.

- **W4: The two "necessary conditions" are descriptive, not predictive.** Asymmetric reliability and formalization-dominated errors are identified post-hoc from the observed pattern across benchmarks. They explain the results but do not predict — given a new task domain, the paper provides no method to assess whether these conditions hold without running the full CRD pipeline. A truly predictive framework would estimate asymmetry and error mode distribution before running the expensive pipeline.

- **W5: Contribution balance skews heavily toward negative results.** The paper's constructive contributions (the diagnostic pipeline, error taxonomy, applicability conditions) are modest individually. The pipeline is straightforward (generate two representations, compare outputs, prompt LLM to diagnose); the taxonomy has no prescriptive value; the conditions are descriptive. The bulk of the paper's value is in showing what doesn't work (repair, cross-domain transfer, cross-model diversity) — which is informative but may not meet the constructive contribution bar for a top venue.

- **W6: The paper does not engage with the broader question of why formal verification matters.** The entire asymmetric reliability argument rests on Z3's completeness guarantees, but FOL is decidable only for specific fragments. The paper does not discuss which FOL fragments FOLIO problems actually use, whether Z3 timeouts occur, or how often the FOL encoding falls outside decidable fragments. This weakens the theoretical grounding of Condition 1.

### Questions for Authors

- Q1: How do you position this work relative to self-consistency (Wang et al., 2023)? Both use disagreement as a signal, but self-consistency operates within a single representation — does your cross-representation analysis add insights beyond what within-representation disagreement provides?
- Q2: Can the applicability conditions be assessed a priori for a new domain, or must one run the full pipeline first? If the latter, the conditions have limited practical value.
- Q3: What FOL fragments does FOLIO actually use? Are there Z3 timeout or undecidability issues that compromise the asymmetric reliability assumption?
- Q4: Would you characterize the paper's contribution as primarily a "negative result" paper? If so, how do you address the concern that negative results require stronger evidence (larger scale, more domains, more models) to be convincing?

### R2 Scores

- Soundness: 3/5
- Contribution: 2/5
- Presentation: 3/5
- Overall: 3/6
- Confidence: 4/5

---

## Step 4: Consolidated Assessment

### Consensus Strengths

1. **Boundary characterization framing is the paper's defining strength.** The systematic degradation across FOLIO → ProofWriter → MATH → GPQA, supported by consistent metrics, is a clean and informative empirical contribution.
2. **Unknown confound analysis is genuinely insightful.** The decomposition by GT label revealing Python's structural three-valued logic limitation as the driver of C4 signal is the paper's strongest finding.
3. **Statistical honesty.** Transparent reporting of CIs, p-values, and power analysis sets a good example. The paper does not overclaim.
4. **Ablation breadth.** Four benchmarks, two model sizes, cross-model pipelines, multiple repair strategies, and selection vs repair — the experimental coverage is thorough.
5. **"Diagnosis as analysis, not repair" is a well-supported reframing** backed by converging evidence from multiple experiments.

### Consensus Weaknesses

1. **Insufficient novelty for a main track top-venue paper.** The core diagnostic mechanism (compare two LLM formalizations, use disagreement to detect errors) is straightforward and incremental over Liang et al. (2024). The boundary characterization and negative results are valuable but may be better suited for a Findings track.
2. **Related work coverage is inadequate.** Seven references for a paper at this intersection is far too few. Self-consistency, LEVER, Faithful CoT, self-debug/self-refine, and multi-agent debate are all directly relevant and uncited.
3. **Repair analysis is extensive but concerns a non-effect.** ~2 pages of the paper analyze repair mechanisms that never reach statistical significance. This space could be better used to deepen the diagnostic analysis or broaden related work.
4. **Error taxonomy is underspecified and unvalidated.** No classification procedure details, no inter-annotator agreement, no prescriptive value — this weakens a claimed contribution.
5. **Cross-domain comparisons conflate different phenomena.** FOL+Z3 (formal verification) vs. CoT+SymPy (informal reasoning + symbolic computation) are categorically different; treating them as points on a single "applicability spectrum" is an imperfect abstraction.
6. **Missing prompt sensitivity analysis.** The paper acknowledges prompt dependence but provides no ablation, leaving it unclear whether findings are properties of CRD or of specific prompt designs.
7. **Modest sample sizes.** Disagree-conditional analyses operate on N=24–76, too small for the fine-grained claims about error types and repair mechanisms.

### Experiment Coverage Assessment

All 10 planned experiments from the experimental design are reflected in the paper:
- exp-002 (Cross-Model Ablation): §5.4, Table 8-9 ✓
- exp-003 (ProofWriter): §5.2.2–5.2.3, Tables 4-5 ✓
- exp-004 (MATH Level 5): §5.3.1, Tables 6-7 ✓
- exp-005 (Repair Mechanism): §5.7.1, Table 12 ✓
- exp-006 (Unknown Deep Analysis): §5.2.1, Tables 2-3 ✓
- exp-007 (Selection vs Repair): §5.6, Table 11 ✓
- exp-008 (Error Taxonomy Ablation): §5.7.3, Table 14 ✓
- exp-009 (Statistical Significance): §5.8, Tables 15-16 ✓
- exp-010 (Qwen3-8B Ablation): §5.5, Table 10 ✓
- exp-011 (GPQA Diamond): §5.3.2, Table 1 (row) ✓

Coverage is complete. The paper faithfully reflects the full experimental design.

### Missing Elements

- GPQA results lack C3/C4 detail in the main table (marked "—")
- No per-category breakdown for GPQA (physics/chemistry/biology) analogous to MATH Table 6
- Cross-model ablation (§5.4) does not report statistical significance for the 1.5pp difference
- No prompt examples or generation details in appendix

### Overall Scores (Consolidated)

| Dimension | R1 | R2 | Consensus |
|-----------|----|----|-----------|
| Soundness | 3/5 | 3/5 | **3/5** |
| Contribution | 2/5 | 2/5 | **2/5** |
| Presentation | 4/5 | 3/5 | **3.5/5** |
| Overall | 3/6 | 3/6 | **3/6** |
| Confidence | 4/5 | 4/5 | **4/5** |

### Final Recommendation: **3/6 (Borderline Reject)**

The paper asks a good question ("when and why does CRD work?") and provides honest, well-structured answers. The Unknown confound analysis and the applicability spectrum are genuine contributions. However, the core diagnostic mechanism is incremental, the repair analysis concerns a non-effect, the related work coverage is inadequate, the error taxonomy is unvalidated, and the cross-domain comparisons conflate categorically different phenomena. The contribution volume — primarily negative/boundary results with modest constructive additions — falls below the threshold for a top-venue main track paper.

**Recommended venue**: Findings track (EMNLP/ACL Findings) or a workshop paper, where boundary characterization and negative results are more naturally valued.

### Actionable Revision Suggestions

1. **Expand related work substantially.** Add self-consistency, LEVER, Faithful CoT, self-debug, multi-agent debate. Fix incomplete bibliography entries.
2. **Cut or compress repair analysis (§5.7).** The non-significant C4 results don't warrant 2 pages. Summarize in one paragraph + one table.
3. **Validate the error taxonomy.** Add human annotation agreement, describe the classification procedure, or downgrade the taxonomy from a claimed contribution to an analytical tool.
4. **Add prompt sensitivity analysis.** Even a small ablation (2-3 prompt variants) would strengthen the claims about when CRD works.
5. **Separate FOL+Z3 analysis from CoT+SymPy analysis.** Frame MATH/GPQA as "related but distinct phenomena" rather than points on the same spectrum, or provide a theoretical argument for why they're commensurable.
6. **Increase FOLIO sample size.** Power analysis shows ~280 samples needed for C4; running on the full FOLIO dataset or augmenting with additional FOL reasoning benchmarks would strengthen the core results.
7. **Discuss FOL decidability fragments.** Address which FOL fragments FOLIO uses and whether Z3 completeness actually holds for all test cases.
