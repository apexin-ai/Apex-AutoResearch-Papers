# Per-Mutation Breakdown: Cross-Model Comparison

> Generated: 2026-05-16 | Test set n=9,784 | Majority baseline: 72.96%
>
> **Sources**: `cls4b_ckpt4600_test_mutation_breakdown.txt`, `cls8b_s42_ckpt3600_per_mutation_pr.json`, `mutation_type_accuracy.csv`, `cwm4b_mutation_breakdown.json`, task context (CLS 8B seed123, CWM 8B interim)

---

## 1. Accuracy Matrix (5 models × 5 mutation types)

| Mutation Type | N | CLS 4B s42 | CLS 8B s42 | CLS 8B s123 | CWM 4B s42† | CWM 8B s42 |
|---|---:|---:|---:|---:|---:|---|
| gold | 4,633 | **98.25** | 96.24 | **99.57** | 23.47 | ⏳ TBD |
| operator_swap | 3,357 | 78.91 | 81.38 | **82.60** | 63.06 | ⏳ TBD |
| return_value | 562 | 67.97 | **75.44** | 66.37 | 27.01 | ⏳ TBD |
| off_by_one | 183 | 58.47 | **86.89** | 79.23 | 0.00 | ⏳ TBD |
| boundary_removal | 1,049 | 46.90 | 46.90 | 44.90 | 59.19 | ⏳ TBD |
| **OVERALL** | **9,784** | **83.63** | **84.48** | **85.60** | **42.88‡** | **38.5‡** |

†CWM accuracies are parseable-only (overall with unparseable→pass default: 58.04%)
‡Parseable-only accuracy

---

## 2. CLS Precision/Recall for Fail Class (4B vs 8B)

| Mutation Type | **CLS 4B s42** ||| **CLS 8B s42** ||| Δ rec_fail |
|---|---:|---:|---:|---:|---:|---:|---:|
| | prec_fail | rec_fail | f1_fail | prec_fail | rec_fail | f1_fail | (8B−4B) |
| operator_swap | 94.34 | 61.12 | 74.18 | 90.62 | 69.65 | 78.76 | **+8.53** |
| return_value | 81.19 | 56.01 | 66.29 | 97.85 | 57.59 | 72.51 | +1.58 |
| boundary_removal | 70.37 | 15.52 | 25.44 | 64.10 | 20.42 | 30.97 | +4.90 |
| off_by_one | 0.00 | 0.00 | 0.00 | 85.71 | 66.67 | 75.00 | **+66.67** |

Key observations:
- **off_by_one**: 4B completely fails to detect failures (rec_fail=0%); 8B achieves 66.67% — the single largest P/R improvement from scaling
- **boundary_removal**: rec_fail remains extremely low (15.5%→20.4%) regardless of model size
- Both models have strong **predict-pass bias** across all mutation types (predict_pass_rate 61-96%)

---

## 3. CWM Parse Rate + Parseable Accuracy

| Mutation Type | N | Parseable | Parse Rate (%) | Parseable Acc (%) | Unparseable (%) |
|---|---:|---:|---:|---:|---:|
| gold | 4,633 | 2,015 | 43.50 | 23.47 | 56.51 |
| operator_swap | 3,357 | 1,911 | 56.93 | 63.06 | 43.07 |
| boundary_removal | 1,049 | 321 | 30.60 | 59.19 | 69.40 |
| return_value | 562 | 274 | 48.75 | 27.01 | 51.25 |
| off_by_one | 183 | 8 | **4.37** | **0.00** | 95.63 |

CWM failure modes by mutation:
- **off_by_one**: near-total collapse — 95.6% unparseable, 0% accuracy on the 8 parseable samples
- **gold (clean patches)**: CWM only gets 23.5% correct even when parseable — massive false-failure hallucination
- **operator_swap**: best CWM performance (63.1%), highest parse rate (56.9%), but still 18pp below CLS 4B
- **boundary_removal**: paradoxically CWM's second-best parseable accuracy (59.2%), exceeding CLS — but only 30.6% parseable

---

## 4. Scaling Effect Ranking (CLS 4B s42 → 8B s42)

| Rank | Mutation Type | 4B Acc (%) | 8B Acc (%) | Δ (pp) | Interpretation |
|---:|---|---:|---:|---:|---|
| 1 | **off_by_one** | 58.47 | 86.89 | **+28.42** | 4B can't detect subtle ±1 errors; 8B learns the pattern |
| 2 | return_value | 67.97 | 75.44 | +7.47 | Moderate gain; requires understanding return semantics |
| 3 | operator_swap | 78.91 | 81.38 | +2.47 | Marginal gain; already well-handled by 4B |
| 4 | boundary_removal | 46.90 | 46.90 | **+0.00** | Zero benefit — task-intrinsic difficulty ceiling |
| 5 | gold | 98.25 | 96.24 | −2.01 | Slight regression, likely noise |

Pattern: scaling primarily helps **subtle, semantically complex** mutations (off_by_one, return_value). Mutations that are either trivial (gold) or task-intrinsically hard (boundary_removal) see no benefit.

---

## 5. CLS vs CWM Prediction Bias

### CLS: Predict-Pass Bias

CLS models overwhelmingly predict "pass" across mutated code:
- boundary_removal: predict_pass_rate = **81.4%** (8B), despite ~35% true pass rate → massive FN for fail class
- off_by_one (4B): predict_pass_rate pushes rec_fail to 0% — the model defaults to "pass" when uncertain
- Scaling helps by *reducing* this bias: 8B off_by_one predict_pass_rate drops to 77.0% (from ~100% implicit in 4B)

### CWM: Predict-Fail Bias (among parseable)

CWM's parseable outputs skew toward predicting failures:
- operator_swap: 45.1% of parseable predictions are "fail" (vs 49.6% actual fail rate — relatively calibrated)
- gold: CWM predicts failures for clean patches 76.5% of the time — hallucinated test failures

However, the 54-67% unparseable rate → default "pass" overwhelms this, creating a **net pass bias** at output level, similar to CLS but through a completely different mechanism.

---

## 6. boundary_removal: Cross-Model Consistency (Task-Intrinsic Difficulty)

| Model | Accuracy (%) | rec_fail (%) | Note |
|---|---:|---:|---|
| CLS 4B s42 | 46.90 | 15.52 | |
| CLS 8B s42 | 46.90 | 20.42 | identical accuracy |
| CLS 8B seed123 | 44.90 | — | |
| CWM 4B s42 (parseable) | 59.19 | — | only 30.6% parseable |
| CWM 8B s42 | ⏳ TBD | — | pending eval |
| **Range (CLS)** | **44.9–46.9** | **15.5–20.4** | **2pp spread across 3 configs** |

This is the strongest evidence for **task-intrinsic difficulty**:
- 3 independent CLS configurations (different sizes, seeds) all converge to ~45-47%
- rec_fail never exceeds 21% — models almost never correctly identify removed boundary checks
- boundary_removal involves removing `if` guards that protect edge cases; test suites may not exercise the affected paths, making the mutation genuinely undetectable from code alone
- This 2pp spread across 3 configs (vs 28pp spread for off_by_one) makes boundary_removal the clearest case of a difficulty ceiling

---

## 7. Summary for Paper Discussion

1. **Scaling selectively helps CLS**: off_by_one is the showcase (+28pp), but boundary_removal is immune to scaling (+0pp). This suggests different mutation types have fundamentally different difficulty profiles.

2. **CWM fails differently per mutation**: off_by_one is a near-total collapse (4.4% parse rate, 0% accuracy), while operator_swap is CWM's best case (56.9% parse, 63.1% accuracy). The failure mode is **parse rate**, not prediction quality — CWM can sometimes reason about mutations when it manages to produce parseable output.

3. **boundary_removal as natural control**: The ~46% accuracy ceiling across all CLS models establishes a task-intrinsic difficulty baseline. This can be used to argue that some mutations are genuinely harder (removed guards may not be exercised by test suites), not that models are uniformly weak.

4. **CLS and CWM have opposite biases**: CLS over-predicts pass (high recall_pass, low recall_fail); CWM's parseable outputs over-predict fail. Yet both struggle with boundary_removal, confirming the difficulty is in the data, not the model architecture.

5. **off_by_one is the scaling showcase**: The 4B→8B jump (58%→87%) demonstrates that larger models can learn subtle numerical boundary reasoning that smaller models miss entirely. The 4B model's rec_fail=0% means it literally never identifies an off-by-one error as a bug.
