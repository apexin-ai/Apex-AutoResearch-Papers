# Research conversation: You are a senior ML/NLP reviewer conducting a review of a paper submitted to AAAI. I have already read the paper and con

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 3
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-aa4042c4117489a97.jsonl`
- **Structured JSON:** [`cdc7fb65b6b757236a4b.json`](../../sessions/cd/cdc7fb65b6b757236a4b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

3 recorded events

### User

_source line 1 · 2026-05-21T13:40:20.013Z_

You are a senior ML/NLP reviewer conducting a review of a paper submitted to AAAI. I have already read the paper and context thoroughly and will provide you with all necessary information. Your job is to write the review report in the exact format I specify below.

## Paper Summary

**Title**: Reproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics

**Core idea**: The paper applies Generalizability Theory (G-theory) to LLM evaluation across 5 benchmarks (MMLU, ARC, HellaSwag, GSM8K, MATH), 7 open-weight models (7-9B), crossing numerical precision (BF16/FP16), prompt templates (6), random seeds (6), temperature ({0.0, 0.7}), and option orderings (4), yielding ~2M binary records. 

**Three main claims**:
1. **Cross-benchmark variance gradient**: item_id% drops monotonically from 42.1% (MMLU) to 14.2% (MATH) while model×item rises from 33.6% to 53.7%. Permutation test p=0.008. Knowledge-retrieval benchmarks are item-dominated; reasoning benchmarks are model×item-dominated.
2. **Precision separability**: precision×methodology interactions < 0.8% under binary scoring — infrastructure (limited to numerical precision on a single GPU) is separable from methodology.
3. **IRT vs G-theory**: G-theory requires 3.6–14.4× more items than IRT for G≥0.80, because IRT ignores prompt×item, seed×item, ordering×item, and model×item dimensions. At IRT-recommended item counts, G-theory reliability is only 0.312–0.529.

**Additional contributions**: D-study benchmark-specific reproducibility budget tables; open-source G-theory pipeline; 17 robustness analyses (REML cross-validation, bootstrap CIs, null simulation, logprob gradient preservation, GLMM complementary analysis, power analysis, design reduction sensitivity, etc.).

## Experiment Coverage Assessment (from review_context.yaml)

The planned experiment design includes 7 experiments (exp-002 through exp-008). Coverage in the paper:

| Experiment | Status | Paper treatment |
|---|---|---|
| exp-002: Multi-benchmark replication | Phase 1-3 complete, Phase 4 partial (InternLM 3/5 benchmarks, DeepSeek not started) | Core results — Tables 1-5 |
| exp-003: Multi-hardware G-study | NOT executed | Scoped out; "infrastructure" narrowed to "numerical precision" |
| exp-004: Comprehensive analysis package | Complete (17/17 sub-analyses) | Section 5 + appendices |
| exp-005: 14B model scale extension | NOT executed | Listed as future work |
| exp-006: Fine-tuning G-study (RoBERTa) | NOT executed | One sentence in Discussion |
| exp-007: LayerCast precision mitigation | NOT executed | Not mentioned |
| exp-008: MATH benchmark | Merged into exp-002 Phase 2 | Included as 5th benchmark |

Key observation: Only exp-002 (mostly) and exp-004 (fully) were executed. Three experiments (003, 005, 006) that would have significantly broadened the paper's scope were not run.

## Paper Structure (12 pages)

- Pages 1-2: Abstract, Introduction, Related Work
- Page 3: Method (G-theory background, experimental design)
- Page 4: Experimental design continued, Results begin (Section 4)
- Pages 5-7: Results (cross-benchmark decomposition, gradient monotonicity, precision separability, IRT vs G-theory, bootstrap CIs, D-study budgets)
- Pages 8-9: Methodological Robustness (Section 5), Discussion (Section 6)
- Page 9-10: Limitations and Future Work, Conclusion
- Pages 10-11: References
- Pages 11-12: Appendices (A: full D-study tables, B: model accuracy, C: three-way interactions, D: logprob analysis)

## Detailed Analysis for Your Review

### Strengths to note:

**S1 - Novel multi-benchmark G-theory application**: First study to cross benchmarks with G-theory in LLM evaluation, extending Mesting (2026) which was single-benchmark.

**S2 - The cross-benchmark gradient is genuinely interesting**: The monotonic shift from item-dominated (knowledge) to model×item-dominated (reasoning) variance has clear theoretical grounding in task structure — knowledge-retrieval items have stable difficulty rankings across models, while reasoning items elicit model-specific solution strategies. This is well-argued.

**S3 - Massive robustness analysis**: 17 sensitivity checks covering estimation method (REML), binary data concern (null simulation, GLMM, Bernoulli adjustment, logprob), CI method (bootstrap vs jackknife), design sensitivity (3×3→2×2 reduction), and power analysis. This is unusually thorough for a conference paper.

**S4 - Actionable practical output**: D-study budget lookup tables (Table 5) give practitioners immediate guidance. The IRT comparison (Table 3) is highly citable — showing that at IRT-recommended item counts, G-theory reliability is only 0.312-0.529.

**S5 - Model as crossed quasi-random facet**: Treating model as crossed rather than fixed reveals 34% model×item interaction invisible in single-model G-studies. The 19pp drop from single-model to cross-model item_id on MMLU is a strong empirical finding.

**S6 - Excellent writing quality**: Clear, well-structured, honest about limitations. The Discussion section's positioning relative to Sclar et al. (2024) and Mesting (2026) is nuanced.

**S7 - Format confound analysis**: Within-format gradient tests (MMLU→ARC within MC: Δ=-6.3pp, p=0.023; GSM8K→MATH within free-form: Δ=-5.4pp, p=0.031) effectively rule out answer format as the primary driver.

### Weaknesses to note:

**W1 - "Infrastructure" claim is overclaimed then narrowed**: The abstract says "crossing infrastructure (numerical precision) with methodology" but the actual infrastructure variation is only BF16 vs FP16 on a single GPU type. The paper transparently acknowledges this in Section 6.1, but the framing in the abstract and contributions still oversells. Mesting (2026) varied judge choice; this paper fixed it. The result is that Claim 2 (precision separability) is a narrow and somewhat unsurprising finding — BF16 and FP16 differ by at most 0.23pp.

**W2 - 200-item samples raise sampling bias concerns**: Each benchmark contributes only 200 randomly sampled items from much larger pools (MMLU has ~14K). The paper does not discuss potential sampling bias — what if the 200 items are not representative of the full difficulty distribution? No stability analysis across different 200-item samples is reported. The D-study recommendations (e.g., 340 items for MMLU at G≥0.80) are calibrated to this specific 200-item subsample.

**W3 - Model scale limited to 7-9B**: All 7 models are in the 7-9B range. Larger models (14B+, 70B) may show qualitatively different variance structures — higher accuracy could compress item_id while specialized reasoning could amplify model×item. The gradient direction might be preserved but the magnitudes could shift substantially. The paper acknowledges this but the generalizability claim is weakened.

**W4 - Incomplete factorial design**: InternLM2.5-7B covers only 3/5 benchmarks, DeepSeek-7B was not run at all. The paper claims 7 models but the design is unbalanced. Henderson Method I assumes balanced designs — while REML cross-validation shows concordance (Δ<0.47pp), the bias properties of Henderson I on unbalanced designs are not fully characterized.

**W5 - Judge facet is fixed**: Mesting (2026) found judge choice accounts for 43.8% of variance. By fixing the judge to generation-based evaluation, this paper excludes a potentially dominant variance source. The paper justifies this choice (Section 6.1) but it means the variance decomposition is conditional on a specific evaluation paradigm.

**W6 - Binary data and G-theory**: G-theory assumes continuous, normally distributed data. Binary (correct/incorrect) data fundamentally violates this. The four-part defense (Section 3.1) is commendable but each defense has limitations: (a) matched-design simulation on a subsample isn't the same as proving unbiasedness; (b) the 25-item GLMM subsample is tiny; (c) Bernoulli normalization is heuristic; (d) logprob analysis changes the measurement model. The paper is transparent, but this remains a methodological tension.

**W7 - Permutation test on 5 benchmarks**: The monotonicity test uses Kendall's τ on only 5 data points (benchmarks). While τ=-1.0 with p=0.008 is statistically significant, the test has extremely low resolution — any non-perfect monotonicity would fail to achieve significance. The apparent strength (τ=-1.0) partly reflects the small sample size.

**W8 - Temperature only 2 levels**: Temperature is measured at only {0.0, 0.7}, which is insufficient to characterize temperature effects. Temperature 0.0 is deterministic, so the "temperature" facet is really a binary deterministic/stochastic toggle rather than a meaningful range.

**W9 - No uncertainty on D-study budgets**: Table 5 gives point estimates (e.g., 340 items, 780 items) without confidence intervals. Given that the variance components have bootstrap CIs of ±8-10pp (Table 4), the D-study projections should also carry substantial uncertainty. Practitioners might over-rely on precise-looking but uncertain numbers.

**W10 - Residual variance interpretation is hand-wavy**: Residual increases from 19.5% (MMLU) to 27.4% (MATH) but the explanation (chain-of-thought path dependence, format variability, cumulative temperature effects) is speculative and not empirically validated.

### Minor issues:

- Table 7 (Appendix A) has missing entries for ARC, HellaSwag, GSM8K in the "All random" column — unexplained.
- The paper mentions releasing an open-source G-theory pipeline but provides no link or repository.
- Some references are to "Preprint" without venue — may not be verifiable.
- The leave-one-model-out analysis mentioned in the review_context.yaml is not reported in the paper itself.

## Scoring

Use AAAI 1-10 scale for Overall Recommendation:
- 10: Top 5% of accepted papers, seminal
- 8-9: Clear accept, strong contribution
- 7: Good paper, accept
- 6: Marginally above threshold
- 5: Marginally below threshold
- 4: Clear reject
- 1-3: Strong reject

My assessment: **Overall: 7** (Good paper, weak accept). The cross-benchmark gradient finding is novel and well-supported, the robustness analysis is thorough, and the practical output (D-study budgets, IRT comparison) is immediately useful. However, the narrow infrastructure scope, 200-item sampling concern, limited model scale, and incomplete factorial design are substantive weaknesses. The paper is clearly above average for AAAI but does not reach the level of a strong accept.

**Soundness: 3/4** — Methodology grounded in G-theory with extensive robustness checks, but binary data assumption violation and unbalanced design are concerns.
**Significance: 3/4** — Practical reproducibility budgets fill a gap; cross-benchmark insight is valuable; limited by narrow scope.
**Novelty: 3/4** — First multi-benchmark G-theory study; meaningful extension of Mesting (2026); but incremental in framework (G-theory is established).
**Clarity: 4/4** — Excellently written, well-structured, transparent about limitations.
**Confidence: 4/5** — High confidence; familiar with G-theory, LLM evaluation, and related work.

## Output Format

Write the review in the following EXACT markdown format. Be thorough and specific. Cite specific table/section numbers. The total report should be 1500-2500 words.

```markdown
# Dream Review Report

**Paper**: Reproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics
**Venue**: AAAI (1-10 scale; exact rubric not publicly available for AAAI-26, using standard AAAI conventions)
**Review mode**: simple (single reviewer, full coverage)
**Date**: 2026-05-21

---

## Summary

[2-3 paragraph summary of what the paper does, its main contributions, and its approach]

## Strengths

[S1 through S7, each a paragraph with specific references to tables/sections]

## Weaknesses

[W1 through W9+, each a paragraph with specific references and constructive suggestions]

## Minor Issues

[Bullet list of minor issues]

## Questions for Authors

[3-5 specific questions that would help clarify concerns]

## Experiment Coverage Assessment

[Assessment of which planned experiments were executed vs. not, and impact on claims]

## Scores

| Dimension | Score |
|---|---|
| Soundness | X/4 |
| Significance | X/4 |
| Novelty | X/4 |
| Clarity | X/4 |
| Overall Recommendation | X/10 |
| Confidence | X/5 |

## Overall Assessment

[2-3 paragraph final judgment: what makes this paper worth accepting or not, key risk, and recommendation]
```

Write the complete review now. Be fair, specific, and constructive.


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "56436a2c-adbd-4565-b64a-15f85dbb167e",
  "agentId": "aa4042c4117489a97",
  "type": "user",
  "uuid": "7abd5f7f-c369-4a10-aecf-48f1ae3ffef7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "44955cf6-fbf6-481a-ac64-bdae83b1911e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-21T13:40:20.018Z_

```json
{
  "parentUuid": "7abd5f7f-c369-4a10-aecf-48f1ae3ffef7",
  "isSidechain": true,
  "agentId": "aa4042c4117489a97",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "b0995159-e48c-40e2-98ac-293286377668",
  "timestamp": "2026-05-21T13:40:20.018Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "44955cf6-fbf6-481a-ac64-bdae83b1911e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-21T13:41:39.521Z_



# Dream Review Report

**Paper**: Reproducibility Budgets for LLM Evaluation: A Generalizability Theory Analysis of Variance Sources Across Benchmarks, Models, and Evaluation Metrics
**Venue**: AAAI (1-10 scale; exact rubric not publicly available for AAAI-26, using standard AAAI conventions)
**Review mode**: simple (single reviewer, full coverage)
**Date**: 2026-05-21

---

## Summary

This paper applies Generalizability Theory (G-theory) to decompose variance in LLM evaluation across five benchmarks (MMLU, ARC, HellaSwag, GSM8K, MATH), seven open-weight models in the 7–9B parameter range, and multiple methodological facets: prompt templates (6), random seeds (6), numerical precision (BF16/FP16), temperature ({0.0, 0.7}), and option orderings (4). The resulting ~2M binary item-level records are analyzed via Henderson Method I variance decomposition, yielding a fully crossed G-study design. The paper advances three central claims: a monotonic cross-benchmark variance gradient from item-dominated (knowledge-retrieval) to model×item-dominated (reasoning) benchmarks; separability of numerical precision from methodology; and a quantified gap between IRT and G-theory reliability estimates due to IRT's inability to capture prompt×item, seed×item, and ordering×item interactions.

The practical contribution is a set of Decision-study (D-study) budget tables specifying the number of items, prompts, seeds, and orderings needed to achieve target generalizability coefficients (G ≥ 0.80) for each benchmark. The paper also reports 17 robustness analyses addressing the known tension between G-theory's normality assumptions and binary response data, including REML cross-validation, null simulation, GLMM on a subsample, Bernoulli-adjusted coefficients, logprob gradient analysis, bootstrap and jackknife confidence intervals, and design reduction sensitivity tests.

The work positions itself as extending Mesting (2026), which applied G-theory to a single benchmark with LLM-as-judge evaluation, by crossing benchmarks, fixing the judge to generation-based scoring, and introducing the cross-benchmark gradient as a new theoretical lens for understanding how task structure shapes evaluation reliability.

## Strengths

**S1 — Novel multi-benchmark G-theory application.** This is, to my knowledge, the first study to apply G-theory across multiple LLM benchmarks in a single crossed design. Prior work (Mesting, 2026) demonstrated G-theory's utility on a single benchmark with judge-based evaluation. By crossing five benchmarks, this paper reveals structural differences in variance composition that are invisible in single-benchmark analyses. The conceptual contribution — that the *type* of benchmark fundamentally shapes which variance sources dominate — is well-motivated and extends the literature meaningfully.

**S2 — The cross-benchmark gradient is the paper's strongest finding.** The monotonic drop in item_id variance from 42.1% (MMLU) to 14.2% (MATH), with a corresponding rise in model×item from 33.6% to 53.7% (Table 1), is theoretically grounded and empirically robust. The explanation is compelling: knowledge-retrieval items have stable difficulty rankings across models (high item_id%), while reasoning items elicit model-specific solution strategies (high model×item%). The within-format gradient tests (Section 4.1) — MMLU→ARC within multiple-choice (Δ=−6.3pp, p=0.023) and GSM8K→MATH within free-form (Δ=−5.4pp, p=0.031) — effectively rule out answer format as the primary driver, strengthening the cognitive-structure interpretation.

**S3 — Unusually thorough robustness analysis.** The 17-analysis robustness package (Section 5) is exceptional for a conference paper. The binary data concern — a legitimate methodological tension — is addressed from four complementary angles: matched-design simulation, GLMM comparison, Bernoulli normalization, and logprob gradient analysis. The REML cross-validation (Δ<0.47pp from Henderson I), bootstrap CIs (Table 4), null simulation, and 3×3→2×2 design reduction sensitivity test collectively provide strong evidence that the main findings are not artifacts of estimation choices. This level of self-scrutiny is commendable.

**S4 — Actionable practical output.** The D-study budget tables (Table 5) translate abstract variance components into concrete guidance: practitioners can look up how many items, prompts, seeds, and orderings are needed for a target reliability on each benchmark. The IRT comparison (Table 3) is particularly impactful — showing that at IRT-recommended item counts, G-theory reliability is only 0.312–0.529 because IRT ignores prompt×item, seed×item, ordering×item, and model×item interaction dimensions. This 3.6–14.4× gap is a quantified, citable result that challenges current evaluation practice.

**S5 — Model as crossed quasi-random facet.** Treating model as a crossed rather than fixed facet is methodologically important. The resulting 34% model×item interaction — invisible in single-model G-studies — reveals that item difficulty rankings are substantially model-dependent. The 19pp drop in item_id% from single-model to cross-model analysis on MMLU (Section 4.1) is a strong empirical demonstration of why single-model reliability estimates are inflated.

**S6 — Writing quality.** The paper is clearly written, well-structured, and transparent about its limitations. The Discussion section's nuanced positioning relative to Sclar et al. (2024) and Mesting (2026) avoids both overclaiming and excessive hedging. Limitations are stated plainly in Section 6.1 rather than buried.

**S7 — Format confound controls.** The within-format gradient tests are a methodologically clean way to address the obvious confound that answer format (multiple-choice vs. free-form) varies across benchmarks. Demonstrating the gradient within format categories substantially strengthens the cognitive-structure interpretation.

## Weaknesses

**W1 — "Infrastructure" is overclaimed then narrowed.** The abstract frames the study as "crossing infrastructure (numerical precision) with methodology," but the actual infrastructure variation is limited to BF16 vs. FP16 on a single GPU type. This is acknowledged in Section 6.1, but the abstract and contribution list still frame Claim 2 (precision separability, <0.8% variance) as a major finding. In practice, BF16 and FP16 differ by at most 0.23pp — a result that is unsurprising given the minimal numerical difference between these formats. Meaningful infrastructure variation would include GPU architecture, quantization levels (INT8, INT4), batching strategies, or multi-GPU parallelism. The planned exp-003 (multi-hardware G-study) was not executed. I recommend the authors either reframe Claim 2 as a narrow negative result or explicitly state in the abstract that "infrastructure" refers only to numerical precision on a single GPU.

**W2 — 200-item subsamples raise representativeness concerns.** Each benchmark contributes only 200 randomly sampled items from pools ranging up to ~14K (MMLU). No analysis of sampling variability is reported — the paper does not show how variance component estimates change across different 200-item draws. This is consequential because the D-study budgets (Table 5) are calibrated to these specific subsamples. If item difficulty distributions in the 200-item samples are not representative, the budget recommendations may be systematically biased. A split-half or repeated-subsampling stability analysis would address this directly and should be feasible given the available data.

**W3 — Model scale is narrow.** All seven models fall in the 7–9B parameter range. Larger models (14B, 70B) may exhibit qualitatively different variance structures: higher accuracy could compress item_id% (ceiling effects), while specialized reasoning capabilities could amplify or dampen model×item%. The planned exp-005 (14B scale extension) was not executed. While the paper acknowledges this limitation, it weakens the generalizability of the gradient claim — the monotonic pattern may hold only within a specific scale regime. I encourage the authors to include at least one model outside the 7–9B range in a revision.

**W4 — Unbalanced factorial design.** InternLM2.5-7B covers only 3 of 5 benchmarks, and DeepSeek-7B was not run. Henderson Method I assumes balanced designs; while REML cross-validation shows small discrepancies (Δ<0.47pp), the bias properties of Henderson I on unbalanced data are not fully characterized in the paper. The authors should either complete the design or provide a more thorough analysis of the impact of imbalance — for example, by re-running the main analyses on the balanced subset (excluding InternLM) and comparing results.

**W5 — Judge facet is absent.** Mesting (2026) found judge choice accounts for 43.8% of variance. By fixing the evaluation paradigm to generation-based scoring, this paper's variance decomposition is conditional on that choice. The judge facet is not merely a limitation — it may be the *dominant* variance source in real-world LLM evaluation. The paper's framing as providing "comprehensive" variance decomposition is therefore misleading in settings where LLM-as-judge evaluation is used. This should be stated more prominently.

**W6 — Binary data remains a methodological tension.** Despite four complementary defenses (Section 3.1/Section 5), G-theory's assumption of continuous, normally distributed data is fundamentally violated by binary item scores. The matched-design simulation uses a subsample; the GLMM comparison covers only 25 items; Bernoulli normalization is heuristic; and logprob analysis changes the measurement model from binary to continuous. Each defense is individually reasonable but none is definitive. The paper is admirably transparent, but this remains the core methodological risk. A full-scale GLMM analysis on all 200 items (computationally expensive but feasible) would substantially strengthen the paper.

**W7 — Permutation test resolution is very low.** The monotonicity test (Kendall's τ on 5 benchmarks) achieves τ=−1.0, p=0.008. However, with only 5 data points, this test cannot detect non-trivial departures from monotonicity — any single violation would push τ to −0.6 with p>0.05. The statistical significance partly reflects the small sample size rather than strong evidence. The authors should acknowledge this limitation more explicitly and consider whether the within-format gradient tests (which are more targeted) are actually the stronger evidence.

**W8 — Temperature as a two-level factor.** Temperature is varied at only {0.0, 0.7}. Since 0.0 is deterministic, this is really a binary deterministic/stochastic toggle rather than a characterization of temperature's role. Values like 0.3, 0.5, and 1.0 would provide meaningful interpolation. The paper's claim about temperature variance contributions is based on an impoverished sampling of this facet.

**W9 — D-study budgets lack uncertainty quantification.** Table 5 reports point estimates (e.g., 340 items for MMLU at G≥0.80) without confidence intervals, even though the underlying variance components have bootstrap CIs of ±8–10pp (Table 4). Propagating this uncertainty to D-study projections would likely yield wide ranges, which practitioners need to make informed decisions. Presenting precise-looking numbers without uncertainty risks overreliance on potentially unstable estimates.

## Minor Issues

- Table 7 (Appendix A) has missing entries for ARC, HellaSwag, and GSM8K in the "All random" column, without explanation.
- The paper claims an open-source G-theory pipeline will be released but provides no repository link or anonymized reference.
- Several references cite "Preprint" without venue, making verification difficult.
- The leave-one-model-out sensitivity analysis mentioned in planning documents does not appear in the paper.
- Residual variance interpretation (Section 4.1, increasing from 19.5% to 27.4%) invokes chain-of-thought path dependence and cumulative temperature effects without empirical support — this should be flagged as speculative.

## Questions for Authors

1. **Sampling stability**: Have you examined how the variance component estimates change across different random 200-item draws from each benchmark? If the item_id% for MMLU shifts by, say, ±5pp across draws, the gradient claim becomes less robust.

2. **Unbalanced design impact**: If you restrict the analysis to the 5 models × 5 benchmarks that are fully balanced (excluding InternLM), do the main findings — particularly the gradient monotonicity and the magnitude of model×item — change meaningfully?

3. **D-study uncertainty**: Could you propagate the bootstrap CIs on variance components into uncertainty ranges for the D-study budget recommendations? This seems feasible given your existing bootstrap infrastructure.

4. **Scale sensitivity**: The gradient claim is tested on 7–9B models only. Do you have any theoretical argument or preliminary evidence for whether the gradient direction would be preserved at 70B scale, where accuracy distributions are substantially different?

5. **Full GLMM**: The GLMM analysis in Section 5 covers only 25 items due to computational cost. Have you considered running this on a larger subset (e.g., 100 items) to provide a more definitive comparison with Henderson I estimates on binary data?

## Experiment Coverage Assessment

Of the seven planned experiments (exp-002 through exp-008), only two were substantively executed: exp-002 (multi-benchmark replication, mostly complete but with gaps for InternLM and DeepSeek) and exp-004 (comprehensive analysis package, fully complete with 17/17 sub-analyses). Three experiments that would have broadened the paper's scope were not run: exp-003 (multi-hardware G-study, which would have supported a genuine infrastructure claim), exp-005 (14B model scale extension, which would have tested scale generalizability), and exp-006 (fine-tuning G-study, which would have introduced a qualitatively different evaluation context).

The impact on claims is asymmetric. Claim 1 (cross-benchmark gradient) is well-supported by the executed experiments, modulo the model-scale concern. Claim 2 (precision separability) is technically supported but the "infrastructure" framing is undermined by exp-003's absence. Claim 3 (IRT vs. G-theory gap) is well-supported. The robustness of the overall contribution would have been substantially enhanced by exp-003 and exp-005.

## Scores

| Dimension | Score |
|---|---|
| Soundness | 3/4 |
| Significance | 3/4 |
| Novelty | 3/4 |
| Clarity | 4/4 |
| Overall Recommendation | 7/10 |
| Confidence | 4/5 |

## Overall Assessment

This is a well-executed study that makes a genuinely novel contribution: the cross-benchmark variance gradient from item-dominated to model×item-dominated structure is theoretically grounded, empirically supported by within-format controls, and practically useful for understanding why different benchmarks have different reliability properties. The D-study budget tables and the quantified IRT–G-theory gap provide immediately actionable outputs for the evaluation community. The 17-analysis robustness package demonstrates unusual methodological rigor for a conference paper, and the writing is exemplary in its clarity and transparency.

The weaknesses are real but bounded. The "infrastructure" claim (Claim 2) is overclaimed given the narrow BF16/FP16 variation and should be reframed. The 200-item subsampling, 7–9B model scale restriction, and unbalanced design introduce uncertainty about the generalizability of the specific numbers reported, though the directional findings (gradient, IRT gap) are likely robust. The binary data tension is the deepest methodological concern — it is well-defended but not fully resolved, and a full-scale GLMM comparison would strengthen the paper.

My recommendation is weak accept. The paper is clearly above the AAAI acceptance threshold: it introduces a novel analytical lens, reports a well-supported primary finding, provides practical tools, and is transparent about limitations. It does not reach strong accept because the scope narrowing (from the planned seven experiments to effectively two) leaves several natural extensions unaddressed, and the infrastructure and scale claims are weaker than framed. A revision that completes the factorial design, adds a split-half subsampling analysis, and reframes Claim 2 would make this a strong accept.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b0995159-e48c-40e2-98ac-293286377668",
  "isSidechain": true,
  "agentId": "aa4042c4117489a97",
  "requestId": "req_011CbForaHVtVg9Le59eSN86",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8a6b9f7-8ff9-4b8b-abd6-a6f0f60138a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory",
  "sessionId": "44955cf6-fbf6-481a-ac64-bdae83b1911e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cd2yMWRS8GWC1XQx7988SA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17765,
      "cache_read_input_tokens": 0,
      "output_tokens": 3924,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 17765
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3924,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 17765,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 17765,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
