# Binary Reward Credit Agreement Experiment — Interim Results

**Date**: 2026-05-23  
**Server**: bjb1-17606  
**Status**: Training still running (1/3 iterations complete, ~2h more estimated)  
**W&B Run**: `binary-credit-agreement` (ID: `5rqm7ofr`)  
**Config**: Cell A (h=2, step-independent GRPO), penalty=0 (pure binary reward), 3 iterations

## Key Finding

**Credit agreement = 100% (157/157)** among non-zero advantage windows.

With binary reward (penalty=0), sign(advantage) perfectly matches sign(step_return > 0). This confirms the theoretical prediction: binary reward + GRPO normalization produces perfect credit agreement because the only signal is episode success/failure, and GRPO normalization assigns positive advantage to success windows and negative to failure windows within the same group.

## Summary Statistics (Iteration 0)

| Metric | Value |
|--------|-------|
| Total advantage records | 400 |
| Unique episodes with windows | 72 / 128 |
| Episode success rate | 12/72 = 16.67% |
| Zero advantage (all-fail groups) | 243/400 = 60.75% |
| Non-zero agreement | 157/157 = 100.00% |
| Positive advantages | 38 (mean=0.0651) |
| Negative advantages | 119 (mean=-0.0127) |

## Per-Group (UID) Breakdown

| UID | Records | Episodes | Success Eps | Success Rate | Zero Adv | Agreement |
|-----|---------|----------|-------------|--------------|----------|-----------|
| 0 | 32 | 8 | 0 | 0.00% | 32 | N/A (all-fail) |
| 1 | 32 | 8 | 1 | 12.50% | 6 | 26/26 = 100% |
| 2 | 25 | 8 | 4 | 50.00% | 7 | 18/18 = 100% |
| 3 | 78 | 8 | 4 | 50.00% | 17 | 61/61 = 100% |
| 4 | 67 | 8 | 3 | 37.50% | 15 | 52/52 = 100% |
| 7 | 41 | 8 | 0 | 0.00% | 41 | N/A (all-fail) |
| 8 | 41 | 7 | 0 | 0.00% | 41 | N/A (all-fail) |
| 9 | 57 | 8 | 0 | 0.00% | 57 | N/A (all-fail) |
| 14 | 12 | 4 | 0 | 0.00% | 12 | N/A (all-fail) |
| 15 | 15 | 5 | 0 | 0.00% | 15 | N/A (all-fail) |

**6/10 groups (UIDs 0,7,8,9,14,15) had all-fail episodes → all zero advantage → no gradient signal.**

## Advantage Asymmetry

- Positive advantages (success windows): mean = 0.0651, max = 0.1396
- Negative advantages (failure windows in mixed groups): mean = -0.0127, min = -0.0210
- **Ratio**: positive magnitude ~5× larger than negative magnitude

This asymmetry is expected: with low success rate (~16.7%), there are few successes per group, so the group mean is pulled toward 0. Successes deviate far above the mean (large positive advantage), while failures cluster near the mean (small negative advantage).

## Window Position Analysis

| Position | Records | Success | Success Rate |
|----------|---------|---------|--------------|
| 0 | 105 | 12 | 11.43% |
| 1 | 83 | 10 | 12.05% |
| 2 | 66 | 6 | 9.09% |
| 3 | 43 | 4 | 9.30% |
| 4 | 35 | 3 | 8.57% |
| 5 | 26 | 2 | 7.69% |
| 6 | 18 | 1 | 5.56% |
| 7+ | 24 | 0 | 0.00% |

Success rate slightly decreases at later window positions — episodes reaching later steps (more actions taken) without succeeding are less likely to eventually succeed.

## Step Return Distribution

Success windows: n=38, mean=5.71, min=1.75, max=10.00

## Implications for Paper

1. **Binary reward guarantees 100% credit agreement** — this is the trivial baseline that confirms our metric definition is correct.
2. **The cost**: 60.75% zero-advantage windows = wasted compute with no gradient signal. This is the "no learning from failure" problem.
3. **The paper's argument**: step-level reward (with format_penalty ≠ 0) can achieve high credit agreement (<100% but close) while providing gradient signal from ALL windows, including all-fail groups. This trades perfect agreement for training efficiency.
4. **Advantage asymmetry** (5× positive/negative) creates imbalanced gradient updates — mostly pushing down failure actions, less reinforcement of success.

## Outstanding

- Iterations 1 and 2 still running (estimated completion ~21:45 CST)
- W&B training metrics (loss, KL, reward) available at run `5rqm7ofr`
- After completion: check if success rate changes across iterations (collapse risk)
- Full 3-iteration analysis will show whether 100% agreement holds consistently
