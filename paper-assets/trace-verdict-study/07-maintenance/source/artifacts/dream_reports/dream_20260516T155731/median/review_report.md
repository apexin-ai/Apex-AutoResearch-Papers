---
dream_id: dream_20260516T155731
tier: median
overall_score: weak reject
timestamp: 2026-05-16T16:31:53.242502+00:00
---


# Review Report: "Exception Events with Structured Formatting: The Most Effective Trace Representation for Verdict Prediction"

## Summary

This paper studies which execution trace components are most effective for verdict prediction (binary pass/fail classification of code solutions) when used for SFT of decoder LLMs. Through systematic ablation across four models (Qwen-2.5-Coder-1.5B/7B, DeepSeek-Coder-6.7B, CodeLlama-13B-Instruct), the authors find that: (1) exception events with structured format markers achieve 99.83% accuracy and outperform all alternatives; (2) information density, not gradient dilution, is the primary bottleneck of full traces (74% vs 26%); (3) trace components form a two-tier diagnostic hierarchy; and (4) format markers contribute ~37% of SFT advantage over simple pattern matching.

---

## Strengths

**S1. Systematic experimental design.** The paper's ablation structure is well-conceived. The component isolation (exception_only, ae_only, loop_only), the label-only loss decomposition, the nomarker ablation, and cross-model testing form a logically coherent experimental pipeline. Each experiment addresses a specific sub-question and the results compose into a clear narrative.

**S2. Information density decomposition is a genuine contribution.** The label-only loss ablation that decomposes the full-trace gap into gradient dilution (26%) and information overload (74%) is a clean causal analysis. This is the paper's strongest methodological contribution — it provides an actionable insight for anyone working with execution traces for SFT.

**S3. Honest treatment of format marker contribution.** Many papers would downplay or omit the nomarker ablation. The authors transparently report that format markers contribute ~37% of SFT advantage and that Regex B5 (99.33%) exceeds nomarker SFT (97.45%). This intellectual honesty strengthens the paper.

**S4. Multi-seed robustness analysis.** Testing key conditions across 3 seeds and reporting variance is good practice. The Qwen zero-variance result (99.83% ± 0.00) and the DeepSeek seed sensitivity finding (σ=4.76pp) add real value.

**S5. Calibration analysis.** Going beyond accuracy to report ECE and Brier scores provides an independent evidence dimension. The 63x ECE ratio between no-trace and exception-only is striking.

---

## Weaknesses

**W1. [Major] The core finding is near-tautological.** Verdict prediction for failing test cases overwhelmingly involves exceptions being thrown. The finding that "exception events predict test verdicts" is dangerously close to "the presence of errors predicts failure." The Regex B5 result (99.33% via format marker alone) confirms this concern: a trivial string-matching rule achieves near-identical performance to the SFT model. The marginal gain of SFT over Regex B5 is only **0.50pp** (99.83% vs 99.33%). The paper needs to more seriously engage with the question: what, precisely, does the 7B SFT model learn beyond what a regex captures? The 63% "semantic learning" decomposition is computed relative to Regex B1 (a weaker baseline), not Regex B5 — a framing choice that inflates the apparent contribution of semantic learning.

**W2. [Major] Small, narrow dataset with ceiling effects.** The dataset comprises only 591 problems from HumanEval and MBPP — small competitive-programming-style problems. The test set is 1,190 samples. At 99.83% accuracy, there are exactly **2 errors** in the entire test set. Drawing fine-grained conclusions about method differences from 2–7 error count differences is statistically fragile regardless of what McNemar's test says. The DebugBench evaluation (96.71% no-trace baseline) suffers even more severe ceiling effects. The paper needs evaluation on harder, more realistic codebases where verdict prediction is actually challenging — e.g., real-world software with complex test suites, non-exception failures (wrong output, timeout, resource exhaustion), or multi-file projects.

**W3. [Major] Limited generalizability and overclaiming.** The title claims to identify "the most effective trace representation" — full stop — but all evidence is from a single narrow task (binary verdict prediction) on simple competitive programming problems. The abstract and conclusion assert "implications for trace representation engineering" and "practical implications for trace design," but these findings may not transfer to:
- More complex codebases with subtle bugs
- Tasks beyond binary classification (debugging, repair, generation)
- Non-exception failures (logic errors producing wrong output without exceptions)
- Real-world test suites where pass/fail semantics differ from HumanEval

The paper should scope its claims to the specific setting studied.

**W4. [Major] Missing critical baselines.** The paper lacks several baselines that would contextualize the contribution:
- **Zero-shot / few-shot prompting** of instruction-tuned models (e.g., GPT-4, Claude, or even the base models themselves with prompting). If prompting a large model with exception traces achieves similar accuracy without SFT, the SFT contribution is diminished.
- **Simple ML classifiers** (logistic regression, random forest) on trace features. If a bag-of-words model on exception text matches SFT, the claimed "semantic learning" is questionable.
- **Regex baselines in Table 1.** The regex results (B1=93.45%, B5=99.33%) are buried in Section 4.7. They should appear in the main results table since Regex B5 is competitive with or superior to most SFT conditions.

**W5. [Moderate] Nomarker ablation details are thin.** Section 4.7, which presents a core novel contribution (format vs. semantics decomposition), provides surprisingly little methodological detail. There are no training curves for nomarker conditions, no per-sample error analysis, no examination of what types of exceptions are hardest without markers. Given that this section supports one of the four stated contributions, it deserves deeper treatment. Additionally, the specific nomarker accuracy numbers (97.45% ± 0.63) and the CodeLlama-13B VOTA result (99.50%) appear without sufficient supporting detail to fully verify them.

**W6. [Moderate] The two-tier hierarchy is descriptively useful but mechanistically shallow.** The tier designation is post-hoc labeling based on observed accuracy clustering. The paper doesn't provide a mechanistic explanation for why the hierarchy exists beyond "diagnostic moment signals are more specific." Why exactly does loop compression achieve ~86% — what specific failure modes does it miss? Why does combining Tier 1 and Tier 2 introduce noise — what is the interference mechanism? Without mechanistic understanding, the "hierarchy" is a description of results, not an explanatory framework.

**W7. [Minor] Thin related work and limited references.** Only 5 references are cited. The paper misses substantial relevant work on:
- Fault localization in software engineering
- Execution-guided code reasoning (SWE-bench, related tasks)
- Trace abstraction and program analysis
- Curriculum learning and data filtering for SFT (relevant to the information density finding)

**W8. [Minor] Class imbalance not adequately addressed.** The 71.5/28.5 pass/fail split means a majority-class classifier achieves 71.51%. While the paper reports this baseline, it doesn't discuss whether the class imbalance affects different conditions differently. Per-class F1 scores are mentioned in passing but not systematically reported in tables.

---

## Experiment Coverage Assessment

Compared against the experimental design document, the paper covers all planned experiments:
- Main conditions (no_trace, full_trace, VOTA, exception_only) across 4 models: ✓
- Component ablation (exception/ae/loop individually): ✓
- Label-only loss ablation: ✓
- Trace length ablation: ✓
- Calibration analysis: ✓
- Seed robustness (Qwen 3-seed, DeepSeek 3-seed): ✓
- Cross-scale (Qwen-1.5B): ✓
- CodeLlama-13B conditions: ✓
- Nomarker ablation (3 seeds): ✓
- DebugBench generalization: ✓
- Multi-seed expansion (ae_only, label_only, loop_only): ✓

Coverage is comprehensive. However, several experiments from the design (CodeLlama-13B VOTA, all nomarker conditions) are flagged as predictions in the design doc rather than actual runs. If the paper presents predicted results as empirical findings, this is a significant concern.

---

## Questions for Authors

1. What fraction of failing test cases in your dataset fail due to exceptions vs. producing incorrect output without exceptions? If nearly all failures involve exceptions, the finding that "exception events predict failure" is circular.

2. Why not include Regex B5 in Table 1? Given that it outperforms full_trace, VOTA (on DeepSeek), and nomarker SFT, it seems like a critical baseline for the main comparison.

3. The nomarker SFT (97.45%) underperforms Regex B5 (99.33%). Does this mean that without format markers, SFT is strictly worse than pattern matching for this task? How do you reconcile this with the claim of "semantic learning"?

4. Have you verified that the 2 irreducible errors (GeneratorExit) are truly irreducible, or could a modified trace representation (e.g., filtering BaseException subclasses) resolve them?

5. How does the exception-only representation handle cases where code produces wrong output without raising any exception? What is the accuracy breakdown for exception-failure vs. wrong-output-failure samples?

---

## Minor Issues

- Table 2: The "¿" symbol appears to be a rendering artifact (should be ">")
- The paper would benefit from a figure showing the trace representation formats (VOTA vs full trace vs exception only) with concrete examples
- Section 3.2: "10 LLM-generated solutions" — which LLM? This affects reproducibility
- The DeepSeek full_trace footnote "†Label-preserving truncation fix (v3)" is unexplained — what were v1/v2 and why did they need fixing?

---

## Overall Assessment

The paper presents a competently executed ablation study with clear writing and honest reporting. The information density decomposition (W: gradient dilution vs. information overload) and the format marker analysis are genuine contributions to understanding trace SFT dynamics.

However, the core finding — that exception events predict test verdicts — borders on tautological for the task studied (W1). The dataset is small and limited to simple competitive programming problems (W2), making it unclear whether findings generalize beyond this narrow setting (W3). The absence of critical baselines (W4), particularly zero-shot prompting and the omission of regex from the main results table, makes it difficult to assess the practical significance of the SFT approach. The fact that Regex B5 achieves 99.33% — only 0.50pp below the best SFT model — substantially undermines the motivation for training a 7B parameter model for this task.

For a top ML venue (acceptance rate ~25%), the contribution bar requires either surprising findings or broad impact. The findings here, while solid, are largely expected (exceptions predict failures) and narrow in scope (one binary classification task, simple code benchmarks). The information density decomposition and format marker analysis add value but may be better suited for a workshop or Findings track.

**Overall Score: 3 — Weak Reject**

**Confidence: 4/5** — I am confident in my assessment. The experimental methodology is clear enough to evaluate, and my concerns about task triviality, dataset limitations, and missing baselines are substantive.

### Score Justification
- **Soundness: 3/5** — Methodology is generally sound, but near-ceiling accuracy makes statistical comparisons fragile, and some experimental conditions lack sufficient detail.
- **Novelty: 2/5** — Core finding is expected; information density decomposition and format marker analysis add modest novelty.
- **Significance: 2/5** — Narrow task, small dataset, minimal practical impact given regex performance.
- **Clarity: 4/5** — Well-written, clear tables, logical structure. Thin related work section.
