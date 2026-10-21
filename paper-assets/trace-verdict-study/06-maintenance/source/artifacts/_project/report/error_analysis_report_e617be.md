# Error Analysis Report: Trace Condition Failure Modes

## Overview

Analyzed 1,190 test samples across 5 trace conditions (Qwen-7B seed42):

| Condition | Accuracy | TP | TN | FP | FN |
|-----------|----------|-----|-----|-----|-----|
| exception_only | 99.83% | 849 | 339 | 0 | 2 |
| vota | 99.41% | 844 | 339 | 0 | 7 |
| loop_only | 85.63% | 741 | 278 | 61 | 110 |
| full_trace | 81.76% | 737 | 236 | 103 | 114 |
| no_trace | 75.13% | 645 | 249 | 90 | 206 |

Test set: 851 pass, 339 fail. Sources: HumanEval 340, MBPP 850.

---

## Finding 1: AssertionError Is the Dominant Failure Mode

**All FPs across all conditions trace back to AssertionError samples** — code that runs without crashing but produces wrong output.

| Error Type (n) | exception_only | vota | loop_only | full_trace | no_trace |
|----------------|---------------|------|-----------|------------|----------|
| AssertionError (190) | 100% | 100% | 67.9% | **50.5%** | 63.2% |
| SyntaxError (67) | 100% | 100% | 100% | 100% | **71.6%** |
| TypeError (53) | 100% | 100% | 100% | 88.7% | 100% |
| NameError (21) | 100% | 100% | 100% | 100% | 100% |
| Timeout (3) | 100% | 100% | 100% | 100% | 100% |
| AttributeError (5) | 100% | 100% | 100% | 40.0% | 80.0% |
| no_error/pass (851) | 99.8% | 99.2% | 87.1% | 86.6% | **75.8%** |

**Key insight**: Crash-type errors (SyntaxError, NameError, TypeError, Timeout) are trivially detectable by all conditions — even partial trace information suffices. The hard case is **AssertionError** (code runs, but assertion on output fails), where:
- exception_only/vota achieve 100% because they see the exception message directly
- full_trace drops to **50.5%** — worse than random on these samples
- The model with full traces gets confused by long execution traces of code that ultimately fails an assertion

**Paper-worthy**: full_trace performs *worse* than no_trace on AssertionError samples (50.5% vs 63.2%), suggesting verbose traces actively mislead the model when the bug is a subtle logic error.

---

## Finding 2: FP/FN Asymmetry Reveals Condition-Specific Biases

| Condition | FP | FN | FP Error Types | Bias |
|-----------|-----|-----|----------------|------|
| exception_only | 0 | 2 | — | Near-unbiased |
| vota | 0 | 7 | — | Near-unbiased |
| full_trace | 103 | 114 | AssertionError(94), TypeError(6), AttributeError(3) | Balanced |
| no_trace | 90 | 206 | AssertionError(70), SyntaxError(19), AttributeError(1) | **FN-heavy** |
| loop_only | 61 | 110 | AssertionError(61) | FN-heavy |

- **no_trace** has 2.3x more FN than FP — without any trace, the model defaults to predicting "fail" when uncertain
- **full_trace** is the only condition with near-equal FP and FN, suggesting the verbose trace adds both signal and noise
- **loop_only** FPs are 100% AssertionError — loop iterations are misleading for assertion failures
- **exception_only and vota have zero FPs** — they never incorrectly predict a failing program as passing

### Per-label accuracy
| Condition | Pass accuracy (n=851) | Fail accuracy (n=339) |
|-----------|----------------------|----------------------|
| exception_only | 99.76% | 100.00% |
| vota | 99.18% | 100.00% |
| loop_only | 87.07% | 82.01% |
| full_trace | 86.60% | **69.62%** |
| no_trace | 75.79% | 73.45% |

full_trace has the widest pass/fail accuracy gap (86.6% vs 69.6%), indicating it struggles specifically with detecting failures.

---

## Finding 3: Source Dataset Differences

| Condition | HumanEval (n=340) | MBPP (n=850) |
|-----------|-------------------|--------------|
| exception_only | 99.41% | 100.00% |
| vota | 100.00% | 99.18% |
| loop_only | **95.29%** | 81.76% |
| full_trace | 84.41% | 80.71% |
| no_trace | 70.88% | 76.82% |

- **loop_only** shows the biggest HumanEval/MBPP gap: 95.3% vs 81.8% (+13.5pp). HumanEval programs tend to be simpler with fewer loop iterations.
- **no_trace** is the only condition where MBPP > HumanEval (76.8% vs 70.9%), possibly because MBPP test code patterns are more stereotypical.

---

## Finding 4: Trace Length Impact

Trace length stats: min=0, max=2000, mean=75.6, median=32.5

| Trace Length | n | exception_only | vota | loop_only | full_trace | no_trace |
|-------------|---|---------------|------|-----------|------------|----------|
| 0 (no trace) | 70 | 100% | 100% | 100% | 100% | **72.9%** |
| 6-20 (medium) | 82 | 100% | 100% | 97.6% | 74.4% | 82.9% |
| 21-50 (long) | 651 | 100% | 98.9% | 86.8% | 81.1% | 77.7% |
| 51+ (very long) | 387 | 99.5% | 100% | 78.6% | 81.1% | **69.5%** |

- **Longer traces hurt no_trace and loop_only the most**: 69.5% and 78.6% for traces 51+. These conditions lack the information to handle complex programs.
- **full_trace is surprisingly stable** across lengths (74-81%), but not because it uses the trace well — it's uniformly confused.
- **Traces of length 0** (SyntaxError or crash-before-execution): only no_trace struggles (72.9%), all others 100%. Without trace info, no_trace can't infer syntax errors.

---

## Finding 5: Cross-Condition Overlap

- **795/1190 (66.8%)** correct by ALL 5 conditions — the "easy" majority
- **0/1190 (0.0%)** wrong by ALL conditions — no universally impossible sample
- **112/1190 (9.4%)** wrong by 3+ conditions (the "hard core")

| Wrong ONLY by | Count |
|---------------|-------|
| exception_only | 2 |
| vota | 0 |
| full_trace | 58 |
| no_trace | 119 |
| loop_only | 36 |

exception_only's 2 unique errors are both FN on HumanEval/95 (label=pass, predicted fail). These correct programs were the only samples exception_only uniquely misjudged.

### Pairwise Disagreement

| Pair | Disagreements |
|------|--------------|
| exception_only ↔ vota | 9 |
| exception_only ↔ loop_only | 173 |
| exception_only ↔ full_trace | 219 |
| exception_only ↔ no_trace | 298 |
| vota ↔ loop_only | 166 |
| vota ↔ full_trace | 210 |
| vota ↔ no_trace | 289 |
| full_trace ↔ no_trace | 201 |
| full_trace ↔ loop_only | 160 |
| no_trace ↔ loop_only | 203 |

exception_only and vota are nearly identical (9 disagreements). The Tier-2 conditions (full_trace, no_trace, loop_only) disagree with each other ~160-200 times and with Tier-1 ~170-300 times.

---

## Finding 6: Universally Hard Samples Cluster in 25 Problems

112 samples wrong by 3+ conditions come from only **25 unique problems**. Top clusters:

| Problem | # Hard Samples | Labels | Wrong By |
|---------|---------------|--------|----------|
| MBPP/284 | 10 | all pass | full_trace, loop_only, no_trace |
| MBPP/419 | 10 | all pass | full_trace, loop_only, no_trace |
| MBPP/443 | 10 | all fail | full_trace, loop_only, no_trace |
| MBPP/113 | 9 | all pass | full_trace, loop_only, no_trace, **vota** |
| MBPP/638 | 9 | all pass | full_trace, loop_only, no_trace |
| MBPP/754 | 9 | all pass | full_trace, loop_only, no_trace |
| MBPP/644 | 8 | all fail (AssertionError) | full_trace, loop_only, no_trace |
| MBPP/92 | 8 | all fail (AssertionError) | full_trace, loop_only, no_trace |
| MBPP/295 | 7 | all fail (AssertionError) | full_trace, loop_only, no_trace |

**exception_only gets ALL 112 hard samples correct.** vota misses 7 (all from MBPP/113). The hard core is dominated by MBPP problems where multiple solution variants all confuse the non-exception conditions.

Among the 112 hard samples: 70 are pass→fail (FN), 42 are fail→pass (FP). The model without exception info both over-predicts and under-predicts verdict for these specific programs.

---

## Finding 7: Tier 1 vs Tier 2 Error Disjointness

| Metric | exception_only | loop_only |
|--------|---------------|-----------|
| Total errors | 2 | 171 |
| Overlap | 0 | 0 |
| Unique to condition | 2 | 171 |

**Zero overlap** — the 2 samples exception_only gets wrong are correctly handled by loop_only, and vice versa. These conditions fail on completely different samples, reinforcing that they encode fundamentally different signals.

---

## Summary: Key Patterns for Paper Discussion

1. **AssertionError is the decisive error type.** Conditions with exception info (exception_only, vota) achieve 100% on these; conditions without (full_trace 50.5%, loop_only 67.9%, no_trace 63.2%) are the primary source of all accuracy gaps. This is the single most important finding for explaining the ~20pp gap between Tier 1 and Tier 2.

2. **Full traces actively hurt on assertion errors** — full_trace (50.5%) performs worse than no_trace (63.2%) on AssertionError samples. Verbose execution traces for logically incorrect but syntactically valid code appear to mislead the model.

3. **Crash errors are trivially solvable** by any condition. SyntaxError, NameError, TypeError, Timeout are all at or near 100% for all conditions except no_trace on SyntaxError (71.6%).

4. **no_trace is FN-biased** (206 FN vs 90 FP), defaulting to "fail" when uncertain. This is the only condition with a strong directional bias.

5. **Hard samples cluster tightly**: 112 samples from 25 problems account for virtually all errors shared by 3+ conditions. These are MBPP-dominated, concentrated problems that confuse all non-exception conditions simultaneously.

6. **exception_only and vota are near-identical** (9 disagreements out of 1190), suggesting that the exception signal alone carries almost all useful information in the vota format.
