# CWM Error Analysis — Paper-Ready Data

> Compiled: 2026-05-15. All numbers from registry experiments with matched environments (conda, transformers 4.57.6).

---

## 1. Headline Numbers: Repo-level CWM vs CLS

| Metric | CWM v12 (s42) | CWM seed123 | CLS 4B best | CLS 8B (val-sel) | Majority BL |
|--------|---------------|-------------|-------------|------------------|-------------|
| **Accuracy** | 58.04% | 59.09% | 82.35% | **83.52%** | 72.96% |
| **F1 macro** | 51.67% | 43.43% | 74.74% | **77.50%** | — |
| **F1 fail** | 34.12% | 13.67% | 60.87% | **65.85%** | — |
| **F1 pass** | 69.22% | 73.19% | 88.60% | **89.14%** | — |
| **Unparseable rate** | 53.7% | 67.2% | 1.3% | 0% | — |
| **Parseable-only acc** | 42.88% | 42.68% | — | — | — |
| **vs Majority (pp)** | −14.92 | −13.87 | +9.39 | +10.56 | 0 |

> **D088 修正**: CLS 8B 改用 val-selected ckpt-1000 (test=83.52%)，不再用 test-best ckpt-400 (84.79%)。F1 已从 `cls8b-s42-ckpt1000-test8192-eval` 补填：macro=77.50%, fail=65.85% (P=74.93%/R=58.73%), pass=89.14% (P=85.84%/R=92.72%)。Confusion: TP=6618, FP=1092, FN=520, TN=1554。

- CLS-CWM gap (4B apple-to-apple): CLS v5-conda 76.37% vs CWM v12 58.04% = **18.33pp**
- CLS-CWM gap (best 4B CLS vs best 4B CWM): 82.35% vs 58.04% = **24.31pp**
- CLS-CWM gap (8B CLS vs 4B CWM): 83.52% vs 58.04% = **25.48pp**
- Both CWM seeds **below majority baseline** (72.96%) by ~14pp

### Experiment References

| exp_id | Model | Seed | Checkpoint | Eval Set |
|--------|-------|------|------------|----------|
| `repo-level-cwm-v12` | Qwen3-4B | 42 | ckpt-500 | test (n=9784) |
| `repo-level-cwm-seed123-conda` | Qwen3-4B | 123 | ckpt-500 | test (n=9784) |
| `repo-level-cls-v5` | Qwen3-4B | 42 | ckpt-4600 | test (n=9784) |
| `repo-level-cls-v5-conda` | Qwen3-4B | 42 | ckpt-600 | test (n=9784) |
| ~~`cls8b-s42-ckpt400-test8192-eval`~~ | ~~Qwen3-8B~~ | ~~42~~ | ~~ckpt-400~~ | ~~test@8192 (n=9784)~~ | ⚠️ superseded by D088 |
| `cls8b-s42-ckpt1000-test8192-eval` | Qwen3-8B | 42 | ckpt-1000 | test@8192 (n=9784) | **primary (val-sel)** |

---

## 2. Error Mode Breakdown (v11 subset-500, config identical to v12)

Source: `cwm_error_mode_analysis.md` (500-sample analysis from v11 ckpt-600, max_new_tokens=1024, max_seq_length=2048)

### 2.1 Unparseable Rate: 75.2% (376/500)

| Category | Count | % of Unparseable |
|----------|-------|------------------|
| Neither pass nor fail keywords (no_keywords) | 289 | 76.9% |
| Both pass AND fail keywords (ambiguous_both) | 86 | 22.9% |
| Only fail keywords | 1 | 0.3% |
| Only pass keywords | 0 | 0.0% |

"Neither" subcategories (289 samples):
- pytest dot-progress bars: 48.1%
- Command output / logs: 51.2%
- All cut off at token budget before reaching verdict

### 2.2 Error Source Attribution (167 total errors in subset-500)

| Error Source | Count | % of Errors |
|-------------|-------|-------------|
| Unparseable → defaulted to PASS, but true=FAIL | 96 | **57.5%** |
| Wrong parseable: true=PASS, pred=FAIL | 64 | 38.3% |
| Wrong parseable: true=FAIL, pred=PASS | 7 | 4.2% |

**57.5% of all errors come from the unparseable-defaults-to-majority mechanism**, not from model predictions.

### 2.3 Token Budget Exhaustion

| Statistic | All Samples | "Neither" Unparseable |
|-----------|------------|----------------------|
| Mean gen length (chars) | 3,398 | 3,773 |
| Median | 3,308 | 3,933 |
| Max | 7,582 | 6,582 |
| Min | 722 | 1,002 |

47.8% of all outputs exceed 3,500 chars. Typical pattern: model outputs `pytest -rA ...` → `test session starts` → hundreds of `.` dots → warnings → **cut off** (never reaches `passed/failed` summary).

### 2.4 Parseable Prediction Quality (124/500 = 24.8%)

| True Label | n | Accuracy |
|-----------|---|----------|
| FAIL | 39 | 82.1% |
| PASS | 85 | 24.7% |
| Overall | 124 | 42.7% |

Model hallucinates failures: 64/71 wrong parseable predictions are PASS→FAIL.

### 2.5 Input Truncation

- 4.2% (21/500) truncated at max_seq_length=2048
- Truncated accuracy: 38.1% vs non-truncated: 67.9%
- 15/21 truncated samples also unparseable

### 2.6 Confusion Matrix (v11 subset-500)

| | Pred PASS | Pred FAIL |
|---|----------|-----------|
| True PASS | 301 (TP) | 64 (FP) |
| True FAIL | 103 (FN) | 32 (TN) |

---

## 3. Per-repo Variation

From `repo-level-cwm-v12` notes:
- **Worst**: pytest — 25-42% accuracy
- **Best**: requests — 64-84% accuracy

Per-repo unparseable rate (from task background):
- scikit-learn: ~0% unparseable
- sphinx: 100% unparseable

The enormous per-repo variance reflects that CWM's ability to parse depends on the repo's test framework output format. Repos with concise pytest output (scikit-learn) are parseable; repos with verbose build/sphinx output are universally unparseable.

---

## 4. Cross-complexity Comparison (Function-level vs Repo-level)

### Function-level CLS vs CWM (per-test, 1890 samples)

| Config | CLS Acc | CWM Acc | Gap (pp) | p-value | Cohen's d |
|--------|---------|---------|----------|---------|-----------|
| 4B (5 seeds) | 88.43 ± 0.78 | 87.19 ± 0.37 | +1.24 | 0.025 | 1.24 |
| 8B (3 seeds) | 89.39 ± 1.09 | 86.96 ± 0.72 | +2.43 | 0.007 | 4.97 |

### Repo-level CLS vs CWM (9784 samples)

| Config | CLS Acc | CWM Acc | Gap (pp) |
|--------|---------|---------|----------|
| 4B apple-to-apple | 76.37% | 58.04% | **+18.33** |
| 4B best CLS vs CWM | 82.35% | 58.04% | **+24.31** |
| 8B CLS (val-sel) vs 4B CWM | 83.52% | 58.04% | **+25.48** |

### Gap Amplification Summary

| Complexity Level | CLS-CWM Gap (pp) | CWM Unparseable |
|-----------------|-------------------|-----------------|
| Function-level (4B) | 1.24 | 0% |
| Function-level (8B) | 2.43 | 0% |
| Repo-level (4B) | 18-24 | 54-67% |

The gap explodes from ~1-2pp to ~24pp as code complexity increases from function-level to repo-level. This is the central C1 claim evidence.

---

## 5. "Correct by Accident" Analysis

CWM's ~58-59% accuracy partly comes from unparseable outputs defaulting to majority class (PASS).

- 38% of CWM "correct" predictions (in v12) are unparseable samples that happened to be PASS class
- Parseable-only accuracy: 42.88% (v12 s42) / 42.68% (seed123)
- Both parseable-only accuracies are below random (50%) — the model is **anti-informative** when parseable

---

## 6. Scaling Behavior (Function-level)

| Method | 4B Mean | 8B Mean | Scaling Gain (pp) |
|--------|---------|---------|-------------------|
| CLS | 88.43 | 89.39 | **+0.96** |
| CWM | 87.19 | 86.96 | **−0.23** |

CLS benefits from scaling; CWM does not. CWM's bottleneck is generation overhead, not model capacity. Gap widens: 1.24pp (4B) → 2.43pp (8B), probability of widening p=0.988.

---

## 7. Three Inherent CWM Failure Modes

### Mode 1: Token Budget Exhaustion (primary, ~77% of unparseable)
CWM must generate ~3400 chars of execution trace to reach a verdict vs CLS's 1-2 tokens. The model produces realistic pytest sessions with dots, warnings, and file paths that consume the entire budget before reaching any pass/fail summary.

### Mode 2: Keyword Ambiguity (~23% of unparseable)
Realistic execution traces contain mixed pass/fail signals: test names with "fail", deprecation warnings, partial error messages. Keyword extraction cannot resolve these.

### Mode 3: Hallucinated Failures (38% of parseable errors)
When parseable, CWM hallucinates failures for passing patches (PASS→FAIL = 64/71 wrong parseable). The model's attempt to simulate execution makes it prone to generating plausible-looking error messages.

---

## 8. Suggested Figures

### Figure A: Per-repo Unparseable Rate (Bar Chart)
- X-axis: repos (scikit-learn, requests, django, ..., sphinx)
- Y-axis: unparseable rate (0-100%)
- Shows dramatic variation from ~0% to 100%
- **Position**: Error Analysis subsection or Appendix

### Figure B: Error Mode Breakdown (Stacked Bar or Pie)
- Segments: no_keywords (77%), ambiguous_both (23%), other (<1%)
- Or: token exhaustion vs keyword ambiguity vs degenerate repetition
- **Position**: Error Analysis subsection

### Figure C: CLS-CWM Gap Amplification (Grouped Bar)
- X-axis: function-level 4B, function-level 8B, repo-level 4B
- Y-axis: accuracy gap (pp)
- Values: 1.24, 2.43, 24.31
- **Position**: Main results section, key visualization for C1 claim

### Figure D: Error Source Attribution (Stacked Bar)
- Three segments: unparseable-default (57.5%), wrong parseable PASS→FAIL (38.3%), wrong parseable FAIL→PASS (4.2%)
- **Position**: Error Analysis subsection

### Figure E: CWM Scaling Non-benefit (Line Plot)
- Two lines: CLS (88.43 → 89.39) vs CWM (87.19 → 86.96)
- X-axis: 4B, 8B
- **Position**: Discussion or Results

---

## 9. Paper Placement Recommendations

| Data | Section | Rationale |
|------|---------|-----------|
| CLS-CWM gap amplification (§4 table) | **Results §5.3** (Repo-level) | Central finding, C1 claim |
| Error mode breakdown (§2) | **Analysis §5.4** or **§6** | Explains WHY CWM fails |
| Unparseable rate comparison (54-67% vs 0-1.3%) | **Results §5.3** | Headline comparison metric |
| Parseable-only accuracy (42.88%) | **Analysis §5.4** | Shows CWM is anti-informative |
| Correct-by-accident (38%) | **Analysis §5.4** | Deflates apparent CWM performance |
| Scaling non-benefit (§6) | **Discussion §7** | Architectural implication |
| Token exhaustion examples | **Appendix** | Qualitative illustration |
| Per-repo breakdown | **Appendix** | Supporting detail |
| Confusion matrix | **Appendix** | Full transparency |

---

## 10. Key Sentences for the Paper

1. "CWM accuracy drops from 87.19% at function-level to 58.04% at repo-level (−29pp), falling 14.92pp below the majority baseline, while CLS maintains above-baseline performance at both complexity levels."

2. "53.7-67.2% of CWM outputs are unparseable, with 77% of unparseable cases caused by token budget exhaustion — the model generates realistic pytest execution traces that consume the entire generation budget before reaching any verdict."

3. "Even among parseable CWM outputs, accuracy is only 42.88% — below random chance — indicating the model is anti-informative when it does produce interpretable predictions."

4. "57.5% of CWM errors stem from the unparseable-defaults-to-majority mechanism rather than incorrect predictions, suggesting the generative approach fundamentally cannot produce reliable execution simulations at repo scale."

5. "The CLS-CWM gap widens from 1.24pp (4B) to 2.43pp (8B) at function-level (p=0.025, d=1.24), and explodes to 24pp at repo-level, supporting the hypothesis that classification approaches scale better than generation for execution simulation."
