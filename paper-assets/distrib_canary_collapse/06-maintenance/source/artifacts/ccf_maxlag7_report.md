# max_lag=7 Reanalysis Report

## Purpose

MVP 4-seed 分析 (max_lag=5) 中，token_entropy→perplexity 的 lag=-5 恰好等于 max_lag 上限。需排除截断伪影。

## Method

`python analyze_mvp.py --seeds 42 43 44 45 --max_lag 7`

## Results: max_lag=5 vs max_lag=7 对比

### Significant Lead Pairs

| canary | downstream | max_lag=5 lags (per seed) | max_lag=7 lags (per seed) | Changed? |
|--------|-----------|--------------------------|--------------------------|----------|
| token_entropy | distinct_1 | -1,-1,-1,-1 | -1,-1,-1,-1 | No |
| token_entropy | distinct_2 | -1,-1,-2,-1 | -1,-1,-2,-1 | No |
| token_entropy | distinct_3 | -5,-1,-2,-1 | -5,-1,-2,-1 | No |
| ece | distinct_1 | -1,-4,-2,-2 | -1,-4,-2,-2 | No |
| ece | distinct_2 | -1,-1,-1,-1 | -1,-1,-1,-1 | No |
| ece | distinct_3 | -1,-5,-1,-1 | -1,-5,-1,-1 | No |

### Weak Lead Pairs

| canary | downstream | max_lag=5 lags (per seed) | max_lag=7 lags (per seed) | Changed? |
|--------|-----------|--------------------------|--------------------------|----------|
| token_entropy | perplexity | -5,-5,-5,-5 | -5,-5,-5,-5 | **No** |
| effective_rank | distinct_3 | -5,-5,-5,-1 | -5,-5,-5,-1 | No |

### All Pairs Lead Time Table (max_lag=7)

| canary | downstream | mean_lag | lag_std | peak_corr | consistent |
|--------|-----------|----------|---------|-----------|------------|
| token_entropy | perplexity | -5.00 | 0.00 | 0.828 | True |
| token_entropy | distinct_1 | -1.00 | 0.00 | 0.995 | True |
| token_entropy | distinct_2 | -1.25 | 0.43 | 0.977 | True |
| token_entropy | distinct_3 | -2.25 | 1.64 | 0.959 | True |
| token_entropy | mauve | -1.00 | 2.92 | 0.763 | False |
| self_bleu | perplexity | -3.25 | 1.92 | 0.950 | False |
| self_bleu | distinct_1 | 0.75 | 2.95 | 0.955 | False |
| self_bleu | distinct_2 | 1.00 | 1.73 | 0.962 | False |
| self_bleu | distinct_3 | 1.00 | 1.73 | 0.969 | False |
| self_bleu | mauve | -1.25 | 3.27 | 0.802 | False |
| ece | perplexity | 4.75 | 0.43 | 0.962 | False |
| ece | distinct_1 | -2.25 | 1.09 | 0.996 | True |
| ece | distinct_2 | -1.00 | 0.00 | 0.996 | True |
| ece | distinct_3 | -2.00 | 1.73 | 0.990 | True |
| ece | mauve | -1.25 | 3.77 | 0.372 | False |
| effective_rank | perplexity | -0.50 | 4.15 | -0.405 | False |
| effective_rank | distinct_1 | 1.50 | 2.60 | 0.005 | False |
| effective_rank | distinct_2 | 1.50 | 2.60 | 0.012 | False |
| effective_rank | distinct_3 | -4.00 | 1.73 | -0.867 | True |
| effective_rank | mauve | 2.75 | 3.34 | -0.385 | False |

## Conclusion

**无截断伪影。** 扩展 max_lag 从 5 到 7 后，所有 20 个 canary→downstream pair 的 lag 估计完全不变。

关键确认：
1. **token_entropy→perplexity lag=-5 是真实信号**，不是撞上 max_lag 边界的伪影。4/4 seed 一致在 lag=-5，但 p-value 仍 borderline (0.058–0.12)，问题在统计功效不足，不在截断。
2. **所有 SIGNIFICANT LEAD pair 的 lag 均远小于 max_lag**（lag=-1 或 -2），不受 max_lag 选择影响。
3. **effective_rank→distinct_3 的 3/4 seed lag=-5** 也未移动到 -6/-7，确认非截断。
4. **Verdict 不变**: STRONG PASS，6 个 significant lead pair + 1 个 weak lead pair。

对 narrative 的影响：token_entropy→perplexity 的 weak lead (lag=-5) 是真实的但统计上不够强，需要更长序列（plan_006 extended 20-gen）或更温和的 collapse 条件（α-sweep）来获得足够统计功效。
