---
dream_id: dream_20260516T155731
tier: worst
overall_score: Weak Reject (3/6)
timestamp: 2026-05-16T16:38:12.625857+00:00
---

# Review Report: "Trace Formatting as Implicit Task Specification: Format Markers Dominate SFT Verdict Prediction"

## 1. Summary

This paper investigates SFT on execution traces for verdict prediction (binary pass/fail classification of code solutions) and discovers that format markers in the VOTA trace representation—specifically `[No exception data in trace]` and `[ERROR]`—account for 41.3% of the total accuracy lift, reducing SFT to near-regex-level pattern matching. The authors design a format marker removal experiment (nomarker) showing a 10.2pp accuracy drop, and demonstrate scale invariance (1.5B=7B=13B) as further evidence of trivial task complexity. The paper reframes trace SFT as a study in implicit task specification, connecting to NLI shortcut learning literature.

## 2. Strengths

- **Well-structured ablation suite.** The paper covers an impressive range of experimental conditions: 6 trace conditions, 4 models across 3 families and scales, 3 seeds, label-only loss ablation, trace length ablation, calibration analysis, and cross-dataset validation. The experimental matrix is thorough for a short paper.

- **Compelling core observation.** The comparison between SFT (99.83%) and Regex B5 (99.33%) is striking and immediately intuitive. The Δ=0.50pp gap is the paper's most effective rhetorical device, clearly communicating that SFT adds negligible value over a trivial string match.

- **Good use of converging evidence.** The paper marshals multiple independent lines of evidence—scale invariance, DeepSeek seeds matching regex exactly, seed variance shift (0→2.5pp), asymmetric pass/fail recall degradation—that individually are suggestive and collectively are persuasive.

- **Practical value.** The recommendation for format ablation as a mandatory control in trace SFT studies is actionable and genuinely useful for the community. The observation that a regex may be preferable to an SFT model at 99.33% vs 99.83% is a pragmatically important point.

- **Honest limitations.** Section 5.7 acknowledges dataset scope, model coverage, residual formatting cues in the nomarker condition, and DebugBench ceiling effects. The DebugBench section (4.11) explicitly declines to draw mechanistic conclusions from it.

- **Interesting secondary findings.** The gradient dilution decomposition (26% vs 74%), exception dominance being model-specific on CodeLlama-13B, token-level loss vs verdict accuracy disconnect, and irreducible error analysis (GeneratorExit) are all individually interesting observations.

## 3. Weaknesses

### W1: The core finding is more predictable than presented (Significance)

The format markers `[No exception data in trace]` and `[ERROR]` **explicitly encode the pass/fail label** by design. They are deterministic functions of the verdict: every passing trace gets `[No exception data in trace]`, every failing trace gets `[ERROR] type: message`. A model learning to use these markers is not "shortcut learning" in the sense of Gururangan et al. (2018)—it is learning the most informative feature in the input. The NLI annotation artifact analogy is strained:

- In NLI, hypothesis-only artifacts are **unintended byproducts** of the annotation process that happen to correlate with labels.
- In VOTA, format markers are **deterministic encodings** of the target label that were intentionally placed in the input by the trace representation design.

A model exploiting a feature that perfectly encodes the label is doing exactly what we'd expect a well-trained classifier to do. The paper frames this as surprising ("a troubling picture"), but it is more accurately described as a trace representation design flaw being diagnosed. This weakens the novelty claim.

**Suggestion:** Reframe from "shortcut learning" to "label leakage through trace formatting." This is a more accurate characterization and still carries significant practical implications without the strained analogy to annotation artifacts.

### W2: Confounded nomarker experiment (Soundness)

The nomarker experiment is the paper's central contribution, but it has a significant confound. After marker removal:
- **Pass samples** become empty or near-empty (the marker *was* the entire content for passing traces).
- **Fail samples** retain substantial exception content (type, message, stack trace elements), just without the `[ERROR]` prefix.

This creates a **content asymmetry confound**: the accuracy drop may not measure "format marker contribution" but rather "what happens when pass samples lose all informative content while fail samples retain theirs." The asymmetric recall degradation (pass recall drops 0.139, fail recall drops only 0.008) is consistent with this confound—it's not that format markers helped pass detection, it's that pass samples *have nothing left* without the marker.

A cleaner experiment would replace `[No exception data in trace]` with a **neutral placeholder** of similar length (e.g., "Execution completed normally") and replace `[ERROR]` with a neutral prefix (e.g., "Exception occurred:"). This preserves content structure while removing the deterministic label encoding.

**Impact:** The 10.2pp number and the 41.3% decomposition are likely overestimates of the format marker's independent contribution, since they conflate marker removal with content destruction.

### W3: Narrow task and dataset scope with broad framing (Generalizability)

- **One dataset:** 591 problems from HumanEval + MBPP-sanitized. These are relatively simple competitive programming problems. Real-world verdict prediction involves more complex codebases, diverse test frameworks, and richer trace semantics.
- **One trace format:** All findings are specific to VOTA's particular design choices. The title ("Format Markers Dominate SFT Verdict Prediction") implies generality beyond VOTA, but no other trace format is tested.
- **Class imbalance:** 71.5% pass / 28.5% fail. The high pass rate means the format marker `[No exception data in trace]` appears in 71.5% of samples, making it a strong majority-class indicator. Would the findings hold with balanced classes?
- **Binary task:** Verdict prediction is binary. The findings may not extend to multi-class trace tasks (e.g., error type classification, fault localization).

### W4: Missing mechanistic evidence (Depth)

The paper relies entirely on accuracy-based ablations to infer the shortcut mechanism. No mechanistic analysis is provided:
- **No attention analysis:** Do models actually attend to format markers? Attention maps over `[No exception data in trace]` tokens would directly confirm the hypothesized mechanism.
- **No probing experiments:** Linear probes on intermediate representations could show when/where the format marker signal is captured.
- **No token attribution:** Gradient-based or perturbation-based attribution methods could quantify each token's contribution to the prediction.
- **No embedding analysis:** Are exception_only representations clustering by marker presence rather than by fault type?

Without mechanistic evidence, the "shortcut learning" claim remains an inference from behavioral data, not a demonstrated mechanism.

### W5: Incomplete related work and missing baselines (Completeness)

- **No comparison to encoder-based models.** TRACED (Chen et al. 2024) uses encoder-based classification on traces. How does an encoder model handle format markers vs content?
- **No prompting baselines.** How do zero-shot or few-shot LLM predictions compare? If a prompted LLM achieves >90% without any SFT, the entire SFT investigation is less interesting.
- **Limited shortcut learning literature.** The paper cites Gururangan (2018), McCoy (2019), Gardner (2020), and Niven & Kao (2019), but misses more recent and directly relevant work on shortcut learning in code models and diagnostic evaluation.
- **No discussion of data augmentation or debiasing.** The shortcut learning literature offers mitigation strategies (e.g., product-of-experts, learned-mixin, confidence regularization). The paper identifies the problem but only suggests "remove markers" as a solution.

### W6: Writing and presentation issues (Clarity)

- **No figures at all.** The paper has 13 tables but zero figures. A single waterfall/decomposition figure would dramatically improve readability. The narrative arc (from initial positive results → troubling regex comparison → nomarker diagnosis → converging evidence) is compelling but would benefit from visual support.
- **Too many subsections.** Sections 4 and 5 have 11 and 7 subsections respectively, many containing only 1-2 paragraphs. This fragments the narrative. Several subsections (4.5 trace length, 4.9 multi-seed, 4.11 DebugBench) could be consolidated.
- **Repetitive argumentation.** The same shortcut interpretation is restated for nearly every experiment. By Section 4.8, the reader has seen the same argument applied to 6+ different results.
- **Table-heavy presentation.** Tables 5-12 could be consolidated into 3-4 tables without information loss.

## 4. Questions for Authors

Q1. In the nomarker condition, what is the average token length of pass vs. fail samples? If pass samples are near-empty while fail samples retain hundreds of tokens, how do you rule out length as a confound?

Q2. Have you tried a **controlled replacement** experiment (replacing markers with neutral text of similar length) rather than simple removal?

Q3. The paper claims scale invariance as evidence of trivial task complexity. But format markers are explicitly present across all scales—couldn't a 1.5B model learn "if string X present, predict pass" just as easily as a 7B model? Scale invariance is expected for any sufficiently simple input-output mapping, shortcut or not.

Q4. What is the performance of zero-shot or few-shot prompting on this task? If Qwen-7B can achieve >90% without SFT, it would change the interpretation significantly.

Q5. The nomarker experiment trains new models from scratch on marker-free traces. But LoRA fine-tuning starts from a pretrained model that has seen code and traces. Could the base model's prior knowledge of exception patterns partially substitute for the removed markers?

Q6. Why not include a "random marker" control where markers are randomly assigned to pass/fail samples (breaking the label correlation)? This would directly test whether the marker's role is as a classification feature vs. a structural/formatting aid.

## 5. Minor Issues

- Table 1: DeepSeek exception_only reports "99.33†" with footnote about median of 3 seeds. The outlier seed (91.09%) is a 8.24pp gap from the other two—this deserves more than a footnote.
- Table 2: Pass F1 and Fail F1 are only reported for vota_no_ae. Why are they missing for other components?
- Table 11: nomarker ECE and Brier are "estimated" (~0.065, ~0.085). Why estimated? These should be exact if the nomarker models were trained and evaluated.
- Section 5.4: The DeepSeek VOTA truncation analysis is interesting but feels like a post-hoc explanation for a negative result. Was truncation rate analyzed before training?
- Section 5.5: The irreducible error analysis (GeneratorExit) is a nice detail but could be a footnote.
- The paper uses "format marker" and "format shortcut" somewhat interchangeably. Defining and consistently using one term would improve clarity.
- Reference formatting: "Gu et al. [2025]" and "Wang et al. [2025]" appear as hyperlinks in the PDF but the underlying citation format is inconsistent.

## 6. Missing Experiments or Analyses

1. **Controlled marker replacement** (neutral placeholder instead of removal) — most critical missing experiment.
2. **Attention/attribution analysis** on format marker tokens to confirm the hypothesized mechanism.
3. **Zero-shot / few-shot prompting baselines** to contextualize SFT value.
4. **Class-balanced evaluation** or stratified analysis to check if findings hold under balanced pass/fail distribution.
5. **Nomarker experiment on ae_only** — ae_only (99.92%) also has strong markers per the paper's analysis. Does removing ae markers produce a similar drop?
6. **Fine-grained error analysis** — what types of problems/bugs does the nomarker model get wrong? Are they systematically different?
7. **Learning dynamics** — does the model learn the format marker early in training (as expected for shortcuts)? Training curves by epoch with marker vs. nomarker would be informative.

## 7. Overall Assessment

**Score: 3 — Weak Reject**

The paper identifies a real and practically important issue—format markers in VOTA traces dominate SFT verdict prediction—and supports it with an admirably thorough experimental suite. The practical recommendation (format ablation as mandatory control) is valuable.

However, the contribution falls short of a top venue for several reasons:

1. **Limited novelty.** The core finding—that a deterministic label encoding in the input is used by the model—is more expected than surprising. The paper's framing as "shortcut learning" overstates the connection to annotation artifacts in NLI, where the artifacts are unintentional.

2. **Methodological concern.** The nomarker experiment, which is the central contribution, has a content-asymmetry confound that undermines the quantitative claims (10.2pp, 41.3%). The paper needs a controlled replacement experiment to make the decomposition credible.

3. **Narrow scope.** One trace format, one dataset, binary task. The broad title and framing don't match the evidence scope.

4. **Missing depth.** No mechanistic analysis beyond accuracy ablations. The paper diagnoses a symptom (accuracy drops) but doesn't confirm the mechanism (attention to markers vs. other explanations).

The paper would be strengthened significantly by: (a) a controlled marker replacement experiment, (b) any form of mechanistic analysis, (c) reframing from "shortcut learning" to "label leakage in trace design," and (d) adding at least one figure. In its current form, it reads as a thorough empirical analysis of a trace representation design flaw, which is useful but incremental.

## 8. Confidence

**4/5** — I am confident in this assessment. I have expertise in NLP evaluation methodology, shortcut learning literature, and SFT for code models. The main area of uncertainty is whether the community would find the "trace format as implicit task specification" framing more novel than I do—it's possible this perspective is less obvious to researchers focused on code/trace domains than to NLP evaluation specialists.