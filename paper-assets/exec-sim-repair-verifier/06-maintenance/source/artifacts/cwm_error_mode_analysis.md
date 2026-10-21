# CWM Error Mode Analysis

**Date**: 2026-05-14
**Data source**: CWM v11 ckpt600 subset500 (config identical to v12: max_new_tokens=1024, max_seq_length=2048)
**Running v12**: 4952/9784 (50.6%), running_acc=57.8%
**Running seed123**: 4888/9784 (50.0%), running_acc=58.2%

## Summary

| Metric | CWM v11 (n=500) | CWM v12 (running) | CLS 8B ckpt400 |
|--------|------------------|--------------------|-----------------|
| Accuracy | 66.6% | ~57.8% | **84.5%** |
| vs Majority | -6.4pp | -15.2pp | +11.6pp |
| F1_macro | 53.0 | TBD | **80.9** |
| Unparseable | **75.2%** | TBD | 1.4% |

## 1. Unparseable Rate: 75.2% (376/500)

The dominant failure mode. CWM generates verbose execution traces that `parse_cwm_prediction()` cannot resolve to PASS/FAIL.

**Why unparseable (among 376):**
| Category | Count | % |
|----------|-------|---|
| Neither pass nor fail keywords | 289 | 76.9% |
| Both pass AND fail keywords | 86 | 22.9% |
| Only fail keywords | 1 | 0.3% |
| Only pass keywords | 0 | 0.0% |

The "neither" category (289 samples) generates execution traces containing:
- pytest output with dot-progress bars (48.1%)
- Command output / logs (51.2%)
- Traces get cut off at token budget before reaching the final verdict line

## 2. Error Source Attribution (167 total errors)

| Error Source | Count | % of errors |
|-------------|-------|-------------|
| Unparseable → defaulted to PASS, but true=FAIL | 96 | **57.5%** |
| Wrong parseable: true=PASS, pred=FAIL | 64 | 38.3% |
| Wrong parseable: true=FAIL, pred=PASS | 7 | 4.2% |

**57.5% of all errors come from the unparseable-defaults-to-majority mechanism**, not from wrong predictions.

## 3. Token Budget Exhaustion

Config: `max_new_tokens=1024` (~3000-4000 chars)

| Gen text length | Mean | Median | Max | Min |
|----------------|------|--------|-----|-----|
| All samples | 3398 | 3308 | 7582 | 722 |
| "Neither" unparseable | 3773 | 3933 | 6582 | 1002 |

The model generates realistic execution traces (pytest sessions with dots, warnings, file paths) that consume the entire token budget before reaching any verdict. 47.8% of all outputs exceed 3500 chars.

Typical pattern: the model outputs `pytest -rA ...` → `test session starts` → hundreds of `.` dots → warnings → **gets cut off here** (never reaches `passed/failed` summary).

## 4. Input Truncation

- 4.2% (21/500) have input truncated to max_seq_length=2048
- Truncated accuracy: 38.1% vs non-truncated: 67.9%
- 15/21 truncated samples are also unparseable

## 5. Parseable Prediction Quality

When the model produces parseable output (only 124/500 = 24.8%):

| True label | Accuracy |
|-----------|----------|
| FAIL (n=39) | **82.1%** |
| PASS (n=85) | 24.7% |
| Overall | 42.7% |

The model hallucinates failures: when it generates clear text, it tends to predict FAIL even for PASS patches (64/71 wrong parseable = PASS→FAIL).

## 6. Typical Error Examples

**Type A: Token exhaustion (no verdict)**
```
+ pytest -rA xarray/tests/test_dataset.py
============================= test session starts =====...
........................................ [  2%]
........................................ [  6%]
... [thousands of dots and warnings] ...
-- Ignored: /opt/miniconda3/envs/testbed/lib/python3.10/_thread  ← CUT OFF
```

**Type B: Mixed keywords (ambiguous)**
```
test_create_engine (dbshell.test_postgresql...) ... ok    ← "pass"-like
...
Importing application dbshell
Testing complete. Django test client exited successfully.  ← but also "error" in trace
```

**Type C: Degenerate repetition**
```
from _pytest.config import _parse_pytest_args
from _pytest.config import _parse_pytest_args
from _pytest.config import _parse_pytest_args
... [repeated 40+ times until token limit]
```

## 7. C1 Claim Support Assessment

**Strong support.** The data shows three inherent difficulties of the generative (CWM) approach:

1. **Generation overhead**: CWM must produce ~3400 chars of execution trace to reach a verdict vs CLS's 1-2 tokens. This creates a fundamental token-budget vs fidelity trade-off that CLS avoids entirely.

2. **Parsing fragility**: Realistic execution traces naturally contain mixed pass/fail signals (test names with "fail", deprecation warnings, partial error messages), making keyword extraction unreliable. 75% of outputs are unparseable.

3. **Hallucination bias**: Even when parseable, CWM hallucinates failures for passing patches (PASS→FAIL = 38% of all errors). The model's attempt to simulate execution makes it prone to generating plausible-looking error messages.

**Quantitative gap**: CLS 8B = 84.5% acc / 80.9 F1_macro vs CWM ≈ 58% acc — a **~26pp accuracy gap** driven primarily by the 75% unparseable rate.
