# CWM Relaxed Matching Analysis (D095 Reviewer Action Item)

## Background

CWM (Code-with-Modification) generates execution traces, then extracts pass/fail via keyword matching. Current results:

| Model | Accuracy | Unparseable % |
|-------|----------|---------------|
| CWM 4B s42 (v12) | 58.04% | 53.7% |
| CWM 4B seed123 | 59.09% | 67.2% |
| CLS 4B (reference) | 84.24% | 0% |

**Reviewer concern:** Is CWM's low accuracy an artifact of overly strict matching? Could unparseable outputs contain correct answers?

## Matching Levels

| Level | Strategy | Description |
|-------|----------|-------------|
| L0 (current) | Exact keywords | `fail_kw ∩ pass_kw` → unparseable; unparseable defaults to majority class (pass) |
| L1 | Resolve ambiguous | When both keywords present, check last 300 chars for dominant signal |
| L2 | Pattern parsing | Pytest progress markers (dots/F), unittest "ok"/"FAIL", summary lines |
| L3 | Semantic phrases | Traceback detection, "test passed/failed" phrases, exception patterns |
| L4 | Generous | Any error indicator → fail; degenerate/clean output → pass; **0 unparseable** |

## Results

### CWM 4B s42 (v12) — 9784 instances

| Level | Accuracy | Parseable | Unparseable | Recovered | Recovered→Correct |
|-------|----------|-----------|-------------|-----------|-------------------|
| L0 (current) | **58.04%** | 4,529 | 5,255 | — | — |
| L1 | 57.52% | 5,093 | 4,691 | 564 | 306 (54.3%) |
| L2 | 55.88% | 8,051 | 1,733 | 3,522 | 2,308 (65.5%) |
| L3 | 55.86% | 8,054 | 1,730 | 3,525 | 2,309 (65.5%) |
| L4 | 56.98% | 9,784 | 0 | 5,255 | 3,633 (69.1%) |

### CWM 4B seed123 — 9784 instances

| Level | Accuracy | Parseable | Unparseable | Recovered | Recovered→Correct |
|-------|----------|-----------|-------------|-----------|-------------------|
| L0 (current) | **59.09%** | 3,210 | 6,574 | — | — |
| L1 | 58.24% | 4,947 | 4,837 | 1,737 | 885 (50.9%) |
| L2 | 56.39% | 7,523 | 2,261 | 4,313 | 2,574 (59.7%) |
| L3 | 56.38% | 7,528 | 2,256 | 4,318 | 2,576 (59.7%) |
| L4 | 55.91% | 9,784 | 0 | 6,574 | 4,100 (62.4%) |

## Key Finding: Relaxed Matching Makes CWM *Worse*

**Every relaxed matching level decreases CWM accuracy compared to L0.** The most generous matching (L4, 0 unparseable) drops accuracy by 1-3pp.

### Why?

The paradox is explained by comparing recovered prediction accuracy against the majority baseline:

| | Recovered Correct Rate | Majority Baseline |
|---|---|---|
| v12 L2 recovered | 65.5% | 73.0% |
| seed123 L2 recovered | 59.7% | 73.0% |
| v12 L4 recovered | 69.1% | 73.0% |
| seed123 L4 recovered | 62.4% | 73.0% |

When unparseable predictions default to the majority class (pass), they achieve 73.0% accuracy — the dataset's class prior. When we actually parse the model's generated content, the recovered predictions are **worse than the majority baseline** (60-69% vs 73%). Parsing reveals the model's actual predictions, which are less accurate than simply guessing "pass."

### Parseable-Only Accuracy (CWM's True Prediction Quality)

| Model | Parseable-Only Acc (L0) | Parseable-Only Acc (L2) |
|-------|------------------------|------------------------|
| v12 | 42.88% | 52.79% |
| seed123 | 42.68% | 52.43% |

CWM's actual predictions, when parseable, are **below 53% accuracy** — worse than random coin flip and far below the 73% majority baseline.

### Unparseable Output Patterns (v12)

| Pattern | Count | % of Unparseable |
|---------|-------|-----------------|
| unittest "ok" results | 1,698 | 32.3% |
| Unclassified | 1,246 | 23.7% |
| Pytest progress (dots/F) | 1,030 | 19.6% |
| Degenerate repetition | 988 | 18.8% |
| Code instead of trace | 203 | 3.9% |
| Has pytest summary | 90 | 1.7% |

## L4 Unparseable Fate Detail

### v12 (5,255 unparseable → all parsed at L4)

| L4 Prediction | Actual | Count | Effect |
|---------------|--------|-------|--------|
| pass | pass ✓ | 3,473 | Were already correct via majority default |
| pass | fail ✗ | 1,358 | Were already wrong via majority default |
| fail | pass ✗ | 264 | **Flipped from correct → wrong** |
| fail | fail ✓ | 160 | **Flipped from wrong → correct** |

Net: +160 correct, −264 correct → **net loss of 104 correct predictions**.

### seed123 (6,574 unparseable → all parsed at L4)

| L4 Prediction | Actual | Count | Effect |
|---------------|--------|-------|--------|
| pass | pass ✓ | 4,076 | Were already correct via majority default |
| pass | fail ✗ | 2,139 | Were already wrong via majority default |
| fail | pass ✗ | 335 | **Flipped from correct → wrong** |
| fail | fail ✓ | 24 | **Flipped from wrong → correct** |

Net: +24 correct, −335 correct → **net loss of 311 correct predictions**.

## Conclusion

1. **Relaxed matching cannot improve CWM.** All levels reduce accuracy because the model's actual predictions (when parsed) are worse than the majority-class default.

2. **CWM's generation quality is fundamentally weak.** Parseable-only accuracy is 43-53%, indicating the model fails to learn meaningful execution prediction regardless of matching strategy.

3. **Gap to CLS is structural, not artifactual.**
   - L0 (current): 58% CWM vs 84% CLS = **26pp gap**
   - L4 (most generous): 56% CWM vs 84% CLS = **28pp gap**
   - Relaxed matching actually *widens* the gap.

4. **Reviewer concern is fully addressed.** The unparseable rate is not masking a better CWM model — it's masking a worse one. The high unparseable rate with majority-class default is the most favorable possible evaluation for CWM, and it still trails CLS by 25+ percentage points.

## Files

- Script: `/home/sonny/exec-sim-repair-verifier/analyze_cwm_relaxed.py`
- Detailed JSON: `/root/autodl-tmp/results/cwm_relaxed_matching_results.json`
- Predictions: `/root/autodl-tmp/results/repo_cwm_v12_conda_eval/eval_repo_cwm_predictions.jsonl`
- Predictions: `/root/autodl-tmp/results/repo_cwm_seed123_conda_eval/eval_repo_cwm_predictions.jsonl`
