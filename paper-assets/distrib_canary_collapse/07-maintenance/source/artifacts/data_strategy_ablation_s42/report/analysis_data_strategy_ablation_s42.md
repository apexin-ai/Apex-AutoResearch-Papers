# Analysis: data_strategy_ablation_s42

**Experiment**: accumulate mode (每代叠加所有前几代生成文本) vs replace mode (每代只用上一代输出)
**Model**: Pythia-410m, α=0.50, seed=42, 10 generations, wikitext103_5k
**Baseline**: alpha_sweep_a050_s42_fp32 (replace mode)

## 5-Method Lead-Lag Scores

| Method | accumulate | replace (baseline) | Δ |
|--------|-----------|-------------------|---|
| naive_xcorr_fwd | 0/8 | — | — |
| diff_xcorr_fwd | 0/8 | — | — |
| threshold_onset_3σ | 0/8 | — | — |
| PermG_fwd | **0/8** | **6/8** | **-6** |
| PermG_rev | 0/8 | 0/8 | 0 |
| TY Granger | 4/8 | 4/8 | 0 |
| K≥3 | **0/8** | **6/8** | **-6** |
| K≥4 | 0/8 | — | — |
| MMCT | 0.0 | 6/8 | -6 |

Note: TY 4/8 仅在 α≤0.50 下种子不稳定（C003），不作为支撑证据。

## Consensus Detail (per pair)

| Pair | K | Methods |
|------|---|---------|
| entropy→distinct_1 | 1 | ty |
| entropy→distinct_2 | 1 | ty |
| entropy→distinct_3 | 0 | — |
| entropy→mauve | 0 | — |
| ece→distinct_1 | 1 | ty |
| ece→distinct_2 | 1 | ty |
| ece→distinct_3 | 0 | — |
| ece→mauve | 0 | — |

## Collapse Metrics

| Metric | gen0 | gen10 | drift_pct |
|--------|------|-------|-----------|
| token_entropy | 3.2342 | 3.1556 | -2.43% |
| ece | 0.0108 | 0.0204 | +88.73% |
| perplexity | 26.949 | 23.702 | -12.05% |
| distinct_1 | 0.0980 | 0.0712 | -27.31% |
| distinct_2 | 0.5141 | 0.3483 | -32.25% |
| distinct_3 | 0.8127 | 0.5799 | -28.65% |
| effective_rank | 46.613 | 45.849 | -1.64% |
| mauve | 0.0311 | 0.0287 | -7.75% |

## vs Baseline Drift Comparison

| Metric | accumulate | replace | 解读 |
|--------|-----------|---------|------|
| token_entropy | **-2.4%** | -16.3% | accumulate 大幅减缓 canary 退化 |
| ece | **+88.7%** | +703.4% | ECE 退化量级差 8x |
| perplexity | **-12.1%** | +16.8% | 方向相反：accumulate 下 ppl 降低 |
| distinct_1 | -27.3% | -29.2% | 多样性退化速率相近 |

## 核心发现

**Conclusion: success** — 数据策略是 canary early-warning 检测能力的关键设计选择。

1. **accumulate 压平 canary 信号**：token_entropy drift 从 -16.3% 缩至 -2.4%，ECE drift 从 +703% 缩至 +89%。历代数据叠加稀释了每代合成文本的污染信号。

2. **diversity 退化不受影响**：distinct_1/2/3 在两种模式下退化幅度相近（-27~32%），说明 downstream collapse 与数据策略关系不大，主要由合成比例 α 驱动。

3. **时序耦合断裂**：canary 几乎不动但 downstream 继续退化，导致 canary→downstream 的 temporal lead 消失。PermG_fwd 从 6/8 降至 0/8，K≥3 从 6/8 降至 0/8。

4. **机制解释**：replace 模式下每代只看上一代输出，形成 Markov chain 式信号放大——每一步退化直接传递给下一步。accumulate 模式混入所有历史数据，相当于对退化信号做时间平均，canary 被平滑掉但 diversity 的累积退化仍在。

5. **实践意义**：若目标是用 canary 做早期预警，必须用 replace（或类似的 memoryless）数据策略。accumulate 虽减缓表观 canary 退化，实际掩盖了预警信号。
