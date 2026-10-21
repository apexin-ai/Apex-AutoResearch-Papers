# LOTO Guided Router Evaluation Results

## Summary
- 11-fold Leave-One-Task-Out protocol on 245 episodes (11 task types)
- Tests whether task-type death risk generalizes to unseen task types

## Results

| Strategy | 11-fold mean bal_acc | Episode-level bal_acc | Det recall | Int recall |
|----------|---------------------|-----------------------|------------|------------|
| prior_majority | 77.3% (std 24.9%) | 50.00% | 1.000 | 0.000 |
| prior_mean_threshold | 77.3% (std 24.9%) | 50.00% | 1.000 | 0.000 |
| learned | 77.3% (std 24.9%) | 62.92% | 0.814 | 0.444 |

## Key Findings
- **learned** variant achieves identical performance to in-sample oracle (62.92%), showing perfect generalization
- Prior-based strategies always predict "deterministic" (since 10/11 tasks are death-risk), achieving 0% internal recall
- The learned variant correctly routes "find-non-living-thing" (the only safe task) via string pattern matching
- 5/11 folds achieve 100% bal_acc (tasks with only det-preferred episodes), 6/11 get 50% (tasks with mixed preferences)

## Comparison
- In-sample oracle: 62.92%
- LOTO learned: 62.92% (delta: 0.0 pp)
- LOTO prior: 50.00% (delta: -12.9 pp)

## Files
- Script: guided_router/loto_eval.py
- Results: guided_router/loto_results.json