# Experiment Analysis: full_trace_seed123

## Experiment Info

| Field | Value |
|-------|-------|
| exp_id | full_trace_seed123 |
| condition | full_trace |
| model | Qwen2.5-Coder-7B-Instruct |
| seed | 123 |
| parent | full_trace_seed42_v5 (accuracy=0.8176, fail_f1=0.6851) |
| status | DONE |
| conclusion | **success** |

## Core Metrics

| Metric | seed123 | seed42 (parent) | Delta |
|--------|---------|-----------------|-------|
| Accuracy | 0.7958 | 0.8176 | -2.18pp |
| Majority Baseline | 0.7151 | 0.7151 | 0.00pp |
| Lift over majority | +8.07pp | +10.25pp | -2.18pp |
| Pass Precision | 0.8753 | — | — |
| Pass Recall | 0.8331 | — | — |
| Pass F1 | 0.8537 | — | — |
| Fail Precision | 0.6263 | — | — |
| Fail Recall | 0.7021 | — | — |
| Fail F1 | 0.6620 | 0.6851 | -0.0231 |
| n | 1190 | 1190 | — |

## Confidence Intervals (95%, 1000 bootstrap resamples)

| Metric | Lower | Upper |
|--------|-------|-------|
| Accuracy | 0.7714 | 0.8202 |
| Lift | +5.04pp | +11.43pp |

## Training Metrics

| Metric | Value |
|--------|-------|
| train_loss | 0.0416 |
| eval_loss (epoch 2) | 0.0761 |
| eval_loss (epoch 3) | 0.0842 |
| wall_clock | 7844s (~2h 10m) |
| GPU hours | 2.42 |

## 3-Seed Summary (full_trace, Qwen2.5-Coder-7B-Instruct)

| Seed | Accuracy | Fail F1 | Status |
|------|----------|---------|--------|
| 42 | 0.8176 | 0.6851 | DONE |
| 123 | 0.7958 | 0.6620 | DONE |
| 456 | — | — | pending |

**2-seed mean accuracy**: 0.8067 (std=0.0154)
**2-seed mean fail_f1**: 0.6736 (std=0.0163)

## Conclusion Rationale

Hypothesis: seed123 accuracy is within ±3pp of seed42 (81.76%).

Result: seed123 accuracy = 79.58%, delta = -2.18pp. This is within the ±3pp threshold.

The 95% CI for seed123 accuracy [77.1%, 82.0%] overlaps with seed42's accuracy (81.76%), confirming the two seeds are statistically consistent.

**Conclusion: SUCCESS** — full_trace condition shows reasonable cross-seed stability. The ~2pp variance is typical for SFT with different random initialization.

## Checkpoint

`/root/autodl-tmp/trace-verdict-study-checkpoints/full_trace_seed123/final`
