# DeepSeek TRAJ Repo-Level: Per-Seed Analysis

## 1. Per-Seed Results

All 6 seeds trained on DeepSeek-Coder 7B with LoRA, repo-level trajectory data, max_seq_length=8192, 3 epochs. Test set: 48 SWE-bench variants (26 resolved, 22 unresolved).

| Seed | Acc (%) | Correct/48 | Resolved F1 | Unresolved F1 | F1 Macro | Best Eval Loss |
|------|---------|-----------|-------------|--------------|----------|---------------|
| s42  | 81.25   | 39        | 84.21       | 76.92        | 80.57    | 0.1216        |
| s999 | 79.17   | 38        | 82.14       | 75.00        | 78.57    | 0.1565        |
| s123 | 75.00   | 36        | 76.92       | 72.73        | 74.83    | 0.1182        |
| s0   | 75.00   | 36        | 80.65       | 64.71        | 72.68    | 0.1013        |
| s456 | 75.00   | 36        | 75.00       | 75.00        | 75.00    | 0.1547        |
| s789 | 66.67   | 32        | 75.00       | 50.00        | 62.50    | 0.1295        |

### Confusion Matrices (available for 5/6 seeds)

| Seed | TN  | FP  | FN  | TP  |
|------|-----|-----|-----|-----|
| s42  | 15  | 7   | 2   | 24  |
| s999 | 15  | 7   | 3   | 23  |
| s123 | 16  | 6   | 6   | 20  |
| s0   | 11  | 11  | 1   | 25  |
| s789 | 8   | 14  | 2   | 24  |

(s456 confusion matrix not saved in eval JSON; only registry metrics available.)

## 2. Summary Statistics

| Metric        | Value    |
|---------------|----------|
| Mean Acc      | 75.35%   |
| SD            | 5.00 pp  |
| Min           | 66.67% (s789) |
| Max           | 81.25% (s42)  |
| Range         | 14.58 pp |
| Median        | 75.00%   |

Mean correct: 36.17/48.

## 3. Binomial CI Analysis

With n=48 and p=0.7535, the expected sampling distribution of accuracy under a binomial model:

- **SE_binomial** = sqrt(p(1-p)/n) = sqrt(0.7535 * 0.2465 / 48) = **6.22 pp**
- **95% CI for single seed** = 75.35% +/- 1.96 * 6.22 = **[63.16%, 87.54%]**
- **CI half-width** = 12.19 pp

### Key comparison

| Quantity | Value |
|----------|-------|
| Observed between-seed SD | 5.00 pp |
| Expected binomial SD (n=48) | 6.22 pp |
| Ratio (observed/expected) | 0.80 |

**The observed SD (5.00 pp) is *smaller* than the expected binomial SD (6.22 pp).** This means the seed-to-seed variation is fully explained by statistical noise from the small test set (n=48). There is no evidence of meaningful model instability beyond what binomial sampling variance would produce.

All 6 seeds fall within the 95% binomial CI [63.16%, 87.54%], including the outlier s789 (66.67%).

### Interpretation

- With n=48 binary outcomes, any single accuracy measurement has inherent uncertainty of ~12 pp (95% CI half-width).
- The +/-5 pp SD across seeds is actually *less* than the 6.22 pp expected from pure binomial noise, suggesting the 6 models are performing very similarly and the apparent spread is just sampling variance.
- Even s789 (66.67%, the worst seed) is only 1.39 SD below the mean in binomial terms, well within normal fluctuation.

## 4. Data Sources

- s42: `/root/autodl-tmp/checkpoints_deepseek_traj_repo_8k/eval_test_s42.json`
- s123: `/root/autodl-tmp/checkpoints_deepseek_traj_repo_8k_s123/eval_test_s123.json`
- s0: `/home/sonny/exec-sim-repair-verifier/eval_traj_results_s0.json`
- s789: `/home/sonny/exec-sim-repair-verifier/eval_traj_results_s789.json`
- s999: `/home/sonny/exec-sim-repair-verifier/eval_traj_results.json`
- s456: Registry metrics only (no eval JSON file found on server)
