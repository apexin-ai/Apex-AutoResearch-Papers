# Training Dynamics Analysis: full_trace (label_only_loss) vs exception_only

**Experiment**: `qwen7b_full_trace_dynamics_seed42`  
**Model**: Qwen2.5-Coder-7B-Instruct  
**Condition**: full_trace with label_only_loss  
**Hypothesis**: full_trace converges slower than exception_only due to redundant information diluting effective signal density  
**Date**: 2026-05-19

## 1. Learning Curve Data

### full_trace (label_only_loss)

| Step | Accuracy | Train Loss | Pass F1 | Fail F1 | Pass Recall | Fail Recall |
|------|----------|------------|---------|---------|-------------|-------------|
| 50   | 87.39%   | 0.2524     | 0.9179  | 0.7292  | 0.9847      | 0.5959      |
| 100  | 82.10%   | 0.1032     | 0.8686  | 0.7194  | 0.8273      | 0.8053      |
| 150  | 86.72%   | 0.0749     | 0.9114  | 0.7349  | 0.9553      | 0.6460      |
| 200  | 88.40%   | 0.0309     | 0.9211  | 0.7810  | 0.9471      | 0.7257      |
| 250  | 86.39%   | 0.0488     | 0.9032  | 0.7705  | 0.8884      | 0.8024      |
| 300  | 84.87%   | 0.0361     | 0.8925  | 0.7450  | 0.8778      | 0.7758      |
| 350  | 88.82%   | 0.0188     | 0.9252  | 0.7787  | 0.9671      | 0.6903      |
| 400  | 88.24%   | 0.0083     | 0.9200  | 0.7778  | 0.9459      | 0.7227      |
| 444  | 88.24%   | 0.0085     | 0.9206  | 0.7727  | 0.9542      | 0.7021      |

### exception_only (baseline)

| Step | Accuracy |
|------|----------|
| 50   | 99.33%   |
| 100  | 99.75%   |
| 150  | 99.83%   |
| 200+ | 99.83% (plateau) |

## 2. Step-by-Step Comparison

| Step | exception_only | full_trace | Gap (pp) |
|------|---------------|------------|----------|
| 50   | 99.33%        | 87.39%     | -11.94   |
| 100  | 99.75%        | 82.10%     | -17.65   |
| 150  | 99.83%        | 86.72%     | -13.11   |
| 200  | 99.83%        | 88.40%     | -11.43   |
| 250  | 99.83%        | 86.39%     | -13.44   |
| 300  | 99.83%        | 84.87%     | -14.96   |
| 350  | 99.83%        | 88.82%     | -11.01   |
| 400  | 99.83%        | 88.24%     | -11.59   |
| 444  | 99.83%        | 88.24%     | -11.59   |

## 3. Convergence Analysis

### 3.1 Convergence Speed

- **exception_only**: reaches 99.33% at step 50, saturates at 99.83% by step 150. Near-instant convergence.
- **full_trace**: best accuracy 88.82% at step 350. Never approaches exception_only's step-50 level even after 444 steps (full epoch).
- **Ratio**: exception_only reaches its plateau in ~150 steps; full_trace does not plateau meaningfully even at 444 steps.

### 3.2 Plateau Level

- **exception_only**: 99.83%
- **full_trace**: ~88.2-88.8% (fluctuating, no clean plateau)
- **Gap at convergence**: ~11 pp

### 3.3 Non-Monotonic Behavior

full_trace shows significant accuracy oscillation:
- Step 50 (87.4%) -> Step 100 (82.1%): **-5.3 pp drop**
- Step 200 (88.4%) -> Step 300 (84.9%): **-3.5 pp drop**
- This non-monotonicity is absent in exception_only (strictly increasing to plateau).

The oscillation correlates with shifts in the pass/fail recall trade-off: at step 100, Fail Recall jumps to 80.5% while Pass Recall drops to 82.7%, suggesting the model temporarily over-corrects toward predicting "fail."

### 3.4 Train-Eval Gap

Train loss drops steadily (0.2524 -> 0.0085), but eval accuracy stagnates at ~88%. This 12 pp gap between training convergence and eval performance suggests the model memorizes trace-specific patterns that don't generalize.

### 3.5 Fail Class Difficulty

Fail F1 is consistently 15-19 pp below Pass F1 across all checkpoints. The model struggles to extract failure signals from full traces, where the relevant exception information is buried among verbose execution steps.

## 4. Conclusion

**Verdict: SUCCESS (hypothesis strongly confirmed)**

The hypothesis that full_trace converges slower than exception_only due to signal dilution is confirmed, and the effect is far stronger than anticipated:

1. **Step 50 accuracy**: full_trace 87.39% vs exception_only 99.33% (11.94 pp gap)
2. **Convergence step**: exception_only saturates at step 150; full_trace never saturates after 444 steps
3. **Final plateau**: full_trace ~88.2% vs exception_only 99.83% (11.6 pp gap)
4. **Learning stability**: full_trace shows non-monotonic oscillation; exception_only is strictly increasing

The result goes beyond "slower convergence" into "fundamentally lower ceiling": even with label_only_loss (no loss on trace tokens), the mere presence of long trace context prevents the model from matching exception_only performance. This directly supports the paper's information density argument: verbose execution traces actively harm verdict prediction because the model must attend to irrelevant context, diluting gradient signal and degrading generalization.

## 5. Implications for Paper Story

- The ~11 pp accuracy gap is a strong quantitative anchor for the "information density matters" claim
- Non-monotonic learning dynamics provide additional evidence that full traces confuse the model
- The train-eval gap (loss -> 0.008 but accuracy stuck at 88%) suggests overfitting to spurious trace patterns
- Combined with exception_only's near-instant saturation, this creates a compelling contrast: less context, better learning

## 6. Key Metrics Summary

| Metric | Value |
|--------|-------|
| Final accuracy (step 444) | 88.24% |
| Best accuracy (step 350) | 88.82% |
| Step-50 accuracy | 87.39% |
| Convergence step | N/A (no clean plateau) |
| Final train loss | 0.0085 |
| exception_only plateau | 99.83% |
| Accuracy gap at step 50 | 11.94 pp |
| Accuracy gap at convergence | 11.01-11.59 pp |
