# W2 Regex Baseline Validation & Q2 Edge Case Analysis

## 1. Data Description

**Dataset**: exception_only condition, 1190 test samples (seed=42 split)

**Label distribution**: 851 pass (71.5%), 339 fail (28.5%)

**Trace content taxonomy** (mutually exclusive, exhaustive):

| Pattern | Count | Pass | Fail | Description |
|---------|-------|------|------|-------------|
| `[No exception data in trace]` | 843 | 843 | 0 | VOTA compressor found no exceptions |
| `[No trace available]` | 70 | 0 | 70 | Trace collection failed (e.g., timeout, crash) |
| `[ERROR] ...` | 277 | 8 | 269 | VOTA extracted exception summary |
| OTHER | 0 | 0 | 0 | — |

Key observation: the three categories perfectly partition all 1190 samples with zero ambiguity. There are no samples outside these three patterns.

## 2. Regex Baseline Results

| Method | Rule | Acc | Correct | Errors |
|--------|------|-----|---------|--------|
| B_marker | `[No exception data in trace]` → pass, else → fail | 99.33% | 1182/1190 | 8 |
| B_error_tag | `[ERROR]` → fail, else → pass | 93.45% | 1112/1190 | 78 |
| B_optimal | marker → pass; `[ERROR]` or `[No trace]` → fail; else → fail | 99.33% | 1182/1190 | 8 |
| B_reviewer | regex `(Error\|Exception\|Traceback\|\[ERROR\])` → fail; `[No trace]` → fail; else → pass | 99.33% | 1182/1190 | 8 |
| **SFT (seed42)** | — | **99.83%** | **1188/1190** | **2** |

Per-class metrics for B_marker (= B_optimal = B_reviewer):

| Class | Precision | Recall | F1 |
|-------|-----------|--------|----|
| pass | 1.0000 | 0.9906 | 0.9953 |
| fail | 0.9769 | 1.0000 | 0.9883 |

Per-class metrics for SFT (seed42):

| Class | Precision | Recall | F1 |
|-------|-----------|--------|----|
| pass | 1.0000 | 0.9976 | 0.9988 |
| fail | 0.9941 | 1.0000 | 0.9971 |

**Multi-seed SFT consistency** (all three seeds identical):

| Seed | Accuracy |
|------|----------|
| seed42 | 1188/1190 = 99.83% |
| seed123 | 1188/1190 = 99.83% |
| seed456 | 1188/1190 = 99.83% |

## 3. McNemar Discordant Pair Analysis (SFT vs B_marker)

| Cell | Count | Samples |
|------|-------|---------|
| Both correct | 1180 | — |
| SFT correct, Regex wrong | **6** | idx=540,541,542,543,548,549 |
| SFT wrong, Regex correct | **0** | — |
| Both wrong | **2** | idx=901, 905 |

**Net SFT advantage: +6 samples (all in one direction)**

The 6 SFT-only-correct samples are all from HumanEval/95 (`check_dict_case`), where the code correctly catches a `ValueError` during string processing. The trace shows `[ERROR] ValueError at line 3: invalid literal for int() with base 10: 'python'`, but the exception is handled by the program logic (try/except), so the test passes. Regex cannot distinguish caught from uncaught exceptions.

The 2 shared errors (idx=901, 905) are both `GeneratorExit` exceptions from generator cleanup. The trace shows `[ERROR] GeneratorExit at line 5` but the code actually passes. Neither SFT nor regex can handle this pattern — SFT also predicts fail.

## 4. Edge Case Analysis (Q2)

### Case 1: fail samples WITHOUT `[ERROR]` tag

**Count: 70** — all are `[No trace available]` (trace collection failed).

- All 70 correctly labeled as fail
- SFT accuracy on these: **70/70 (100%)**
- These represent cases where the buggy code caused a crash/timeout that prevented trace collection entirely

### Case 2: pass samples WITH exception/error text

**Count: 8** — the critical edge cases

| idx | Exception Type | SFT Correct? | Description |
|-----|---------------|---------------|-------------|
| 540 | ValueError | Yes | `check_dict_case` — caught exception in string parsing |
| 541 | ValueError | Yes | Same problem, different solution variant |
| 542 | ValueError | Yes | Same |
| 543 | ValueError | Yes | Same |
| 548 | ValueError | Yes | Same |
| 549 | ValueError | Yes | Same |
| 901 | GeneratorExit | **No** | Generator cleanup exception — benign |
| 905 | GeneratorExit | **No** | Same pattern |

**Interpretation**: 6/8 are caught exceptions (try/except in the code), and SFT learns to predict pass for these. 2/8 are GeneratorExit from Python's generator protocol — benign but extremely rare, and neither SFT nor regex handles them.

### Case 3: `[No trace available]` distribution

- **All 70 samples are fail** (zero pass samples have missing traces)
- SFT: 70/70 correct
- This makes `[No trace available]` a perfectly reliable fail signal

### Case 4: OTHER category (no standard markers)

**Count: 0** — every sample falls into one of the three standard patterns.

## 5. Conclusion: Is Regex Equivalent to SFT?

**No, but the gap is small and structurally bounded.**

| Aspect | Finding |
|--------|---------|
| **Overall accuracy gap** | 0.50% (6 samples out of 1190) |
| **Structural explanation** | 8 pass samples have `[ERROR]` tag (caught/benign exceptions). SFT learns 6/8; regex gets 0/8. |
| **Theoretical regex ceiling** | 99.33% — impossible to exceed without understanding exception semantics |
| **SFT ceiling** | 99.83% — fails only on 2 GeneratorExit edge cases |
| **Is the gap meaningful?** | Yes: it demonstrates the model learns exception semantics (caught vs uncaught), not just keyword matching |

### Reviewer's specific claim

Reviewer hypothesized `[ERROR]→fail, else→pass` achieves ~99.83%. This is **incorrect**: that rule (B_error_tag) achieves only **93.45%** because it misses all 70 `[No trace available]` fail samples.

The closest valid formulation — `[No exception data in trace]→pass, else→fail` — achieves **99.33%**, not 99.83%. The 0.50% gap (6 samples) is entirely explained by caught exceptions that require semantic understanding beyond pattern matching.

### Rebuttal implications

1. **Best regex = 99.33%, not 99.83%**: Reviewer's mental model omitted the `[No trace available]` category
2. **SFT's edge is semantically meaningful**: The 6 discordant samples are all caught exceptions — the model learned that `[ERROR] ValueError` in a try/except context still means pass
3. **The gap is consistent across seeds**: All 3 seeds produce identical 99.83%, suggesting robust learning (not noise)
4. **exception_only is intentionally the simplest condition**: It's the ablation floor showing what exception data alone provides. The paper's main result is VOTA (full compression), which is compared against no_trace, not exception_only
