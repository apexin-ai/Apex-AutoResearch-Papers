# data_strategy_ablation_s43 Analysis Report

**Experiment**: accumulate data strategy, cross-seed (s43) validation
**Model**: Pythia-410M | **Seed**: 43 | **Alpha**: 0.50 | **Precision**: fp32
**Server**: westd-19828
**Analysis standards**: D105 3sigma + D086 BH FDR + D102 8-pair + D111 peak_lag<0 + n_perm=5000

## Training Status

Completed normally. EXIT_CODE=0, 11 generations (gen_0 through gen_10).

## Metric Trajectories (gen_0 -> gen_10)

| Metric | gen_0 | gen_10 | Drift % |
|--------|-------|--------|---------|
| token_entropy | 3.2342 | 3.1427 | **-2.83%** |
| ece | 0.0108 | 0.0181 | **+67.8%** |
| distinct_1 | 0.0983 | 0.0704 | **-28.4%** |
| distinct_2 | 0.5146 | 0.3415 | **-33.6%** |
| distinct_3 | 0.8140 | 0.5671 | **-30.3%** |
| mauve | 0.0315 | 0.0307 | **-2.5%** |
| perplexity | 26.95 | 23.50 | -12.8% |
| effective_rank | 46.61 | 44.95 | -3.6% |

## Lead-Lag Analysis (5-method, 8-pair)

| Method | Forward sig | Reverse sig | Notes |
|--------|-----------|-----------|-------|
| PermG FDR | **0/8** | 0/8 | All p_fdr=0.94 |
| DiffXCorr FDR | 2/8 raw | 2/8 raw | D111: 0/8 (sig pairs have DLag=0) |
| Threshold onset (D105 3sigma) | **0/8** | 0/8 | downstream onset=null on 7/8 pairs |
| TY Granger | 3/8 | - | C003: unreliable at alpha<=0.50 |
| Naive XCorr | 6/8 | 6/8 | Non-directional, not used for consensus |

### Consensus (K votes)

| Pair | K (votes/5) | Methods |
|------|------------|---------|
| token_entropy -> distinct_1 | 0/5 | - |
| token_entropy -> distinct_2 | 0/5 | - |
| token_entropy -> distinct_3 | 0/5 | - |
| token_entropy -> mauve | 0/5 | - |
| ece -> distinct_1 | 1/5 | ty |
| ece -> distinct_2 | 1/5 | ty |
| ece -> distinct_3 | 1/5 | ty |
| ece -> mauve | 0/5 | - |

- **K>=3**: 0/8
- **K>=4**: 0/8

## Cross-seed Comparison: accumulate strategy

| Metric | s42 accumulate | s43 accumulate |
|--------|---------------|----------------|
| PermG FDR fwd | 0/8 | 0/8 |
| K>=3 consensus | 0/8 | 0/8 |
| entropy_drift | -2.4% | -2.83% |
| ece_drift | +89% | +67.8% |
| distinct_1_drift | -27% | -28.4% |

## Comparison with replace baseline (alpha_sweep_a050_s43_fp32)

| Metric | accumulate s43 | replace s43 |
|--------|---------------|-------------|
| PermG FDR fwd | **0/8** | **6/8** |
| K>=3 consensus | **0/8** | **6/8** |
| TY fwd | 3/8 | 5/8 |
| entropy_drift | -2.83% | -15.81% |
| ece_drift | +67.8% | +679.56% |
| distinct_1_drift | -28.4% | -29% |

## Conclusion

**accumulate 策略在 s43 完全复现 s42 的 lead-lag 抑制效应**:

1. **Lead-lag 完全被抑制**: PermG=0/8, K>=3=0/8，与 s42 accumulate 一致。Replace 基线同种子下 PermG=6/8, K>=3=6/8。
2. **Canary drift 被大幅抑制**: entropy_drift 仅 -2.83%（replace: -15.81%），ece_drift +67.8%（replace: +679.56%）。accumulate 通过保留原始数据稀释了合成数据的 distributional shift，canary 信号太弱无法建立统计显著的 lead-lag 关系。
3. **Downstream 退化仍然发生**: distinct_1 drift -28.4% 与 replace (-29%) 几乎一致。说明 accumulate 虽然抑制了 canary-level 信号，但多样性退化仍在发生，只是因为 canary 变化被平滑化导致 lead-lag 无法检测。
4. **Seed robustness 确认**: 两个种子（s42, s43）结果高度一致，accumulate 策略对 lead-lag 的抑制效应是 robust 的，非随机 artifact。
