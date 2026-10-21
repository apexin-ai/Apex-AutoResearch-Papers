## alpha_sweep_a010_s43 分析结果

### 训练状态
完成状态: 正常 (EXIT_CODE=0)
Generations: 11 (gen0-gen10, 全部完成)
服务器: westd-17855
精度: bf16
结果路径: /root/autodl-tmp/distrib_canary_collapse/results/alpha_sweep/a010_s43_bf16/

### Per-Generation Metrics

| Gen | token_entropy | ece | perplexity | distinct_1 | distinct_2 | distinct_3 | eff_rank | mauve |
|-----|--------------|--------|-----------|------------|------------|------------|----------|--------|
| 0 | 3.2574 | 0.01230 | 27.681 | 0.09168 | 0.5037 | 0.8341 | 48.33 | 0.02971 |
| 1 | 2.8816 | 0.00325 | 17.184 | 0.08966 | 0.4955 | 0.8242 | 48.03 | 0.03005 |
| 2 | 2.8580 | 0.00461 | 16.950 | 0.07679 | 0.4180 | 0.7476 | 50.44 | 0.02424 |
| 3 | 2.8500 | 0.00384 | 16.714 | 0.07156 | 0.3800 | 0.7051 | 52.17 | 0.02454 |
| 4 | 2.8562 | 0.00459 | 17.162 | 0.06980 | 0.3622 | 0.6782 | 54.92 | 0.02063 |
| 5 | 2.8456 | 0.00545 | 16.914 | 0.06818 | 0.3399 | 0.6403 | 56.18 | 0.02030 |
| 6 | 2.8514 | 0.00518 | 16.988 | 0.06664 | 0.3239 | 0.6139 | 56.77 | 0.01839 |
| 7 | 2.8628 | 0.00457 | 17.127 | 0.06575 | 0.3148 | 0.5937 | 57.75 | 0.01538 |
| 8 | 2.8477 | 0.00613 | 17.183 | 0.06534 | 0.3096 | 0.5832 | 58.94 | 0.01571 |
| 9 | 2.8243 | 0.00614 | 16.955 | 0.06458 | 0.3024 | 0.5729 | 58.93 | 0.01510 |
| 10 | 2.8304 | 0.00478 | 16.920 | 0.06496 | 0.3009 | 0.5681 | 59.69 | 0.01596 |

### Drift (gen0 → gen10)

| Metric | gen0 | gen10 | Drift% |
|--------|------|-------|--------|
| token_entropy | 3.2574 | 2.8304 | -13.1% |
| ece | 0.01230 | 0.00478 | -61.1% |
| perplexity | 27.681 | 16.920 | -38.9% |
| distinct_1 | 0.09168 | 0.06496 | -29.1% |
| distinct_2 | 0.5037 | 0.3009 | -40.3% |
| distinct_3 | 0.8341 | 0.5681 | -31.9% |
| effective_rank | 48.33 | 59.69 | +23.5% |
| mauve | 0.02971 | 0.01596 | -46.3% |

### 5-Method Lead-Lag (n_perm=5000, xcorr_lag=5)

| Method | Score |
|--------|-------|
| naive_xcorr_fwd | 7/8 |
| diff_xcorr_fwd (BH-FDR) | 8/8 |
| threshold_onset_fwd | 3/8 |
| perm_granger_fwd (BH-FDR) | 0/8 |
| perm_granger_rev (BH-FDR) | 0/8 |
| ty_granger_fwd | 0/8 |
| K>=4/5 | 0/8 |

Consensus detail:
- token_entropy->distinct_1: 3/5 [naive, diff, thresh]
- token_entropy->distinct_2: 3/5 [naive, diff, thresh]
- token_entropy->distinct_3: 3/5 [naive, diff, thresh]
- token_entropy->perplexity: 2/5 [naive, diff]
- ece->distinct_1: 1/5 [diff]
- ece->distinct_2: 2/5 [naive, diff]
- ece->distinct_3: 2/5 [naive, diff]
- ece->perplexity: 2/5 [naive, diff]

### 对比

#### vs fp32 s42 (a010_s42, westd-19828)

| Metric | bf16 s43 drift | fp32 s42 drift | Delta |
|--------|---------------|---------------|-------|
| token_entropy | -13.1% | -5.3% | bf16 2.5x larger drop |
| ece | -61.1% | +57.4% | 方向相反 |
| perplexity | -38.9% | -21.0% | bf16 1.9x larger drop |
| distinct_1 | -29.1% | -39.7% | bf16 27% less collapse |
| distinct_2 | -40.3% | -56.4% | bf16 29% less collapse |
| distinct_3 | -31.9% | -58.9% | bf16 46% less collapse |
| effective_rank | +23.5% | -3.1% | 方向相反 |
| mauve | -46.3% | -54.6% | bf16 15% less drop |

D079 confirmed: bf16 显著抑制 diversity collapse (d1/d2/d3 均明显缓解)。
ECE 方向逆转: bf16 校准误差下降, fp32 上升。
Effective rank 方向逆转: bf16 rank 上升(+23.5%), fp32 下降(-3.1%)。

#### vs null a000_s43 (fp32, westd-19828)

| Metric | a010 s43 bf16 | null a000 s43 | 可区分? |
|--------|--------------|--------------|--------|
| token_entropy | -13.1% | -4.4% | 是 (3.0x) |
| ece | -61.1% | +37.2% | 是 (方向相反) |
| perplexity | -38.9% | -20.3% | 是 (1.9x) |
| distinct_1 | -29.1% | -13.9% | 是 (2.1x) |
| distinct_2 | -40.3% | -9.8% | 是 (4.1x) |
| distinct_3 | -31.9% | -4.8% | 是 (6.7x) |

Magnitude 层面: a010 所有 metric drift 均明显大于 null, 可区分。
Causal 层面: 5-method 中 PermG (0/8), TY (0/8), K>=4 (0/8) 均未检出 canary->downstream 因果先导, 盲区复现。

注意: null a000_s43 为 fp32, a010_s43 为 bf16, 精度差异可能影响直接比较。

#### D078 精度桥梁评估

bf16 对 α=0.10 regime 影响:
1. Diversity collapse 显著缓解: d1 从 -39.7% → -29.1%, d3 从 -58.9% → -31.9%
2. Entropy canary 反而 drift 更大: -13.1% (bf16) vs -5.3% (fp32)
3. ECE 行为彻底改变: bf16 降低 ECE (改善校准), fp32 升高 ECE (恶化校准)
4. Causal signal 未改变: 两者 PermG/TY 均为 0/8
5. 盲区本质不变: bf16 缓解了 collapse 程度但未改变 canary 缺乏因果先导的核心问题

### Conclusion

**success** - validates D075 canary blind zone

理由:
1. D075 盲区复现: α=0.10 bf16 s43 存在实质性 diversity collapse (d1=-29.1%, d2=-40.3%, d3=-31.9%) 但 5-method 因果检验全部失败 (PermG 0/8, TY 0/8, K>=4 0/8)
2. D079 confirmed: bf16 系统性抑制 diversity collapse (d1/d2/d3 collapse 分别减少 27%/29%/46%)
3. D078 新发现: bf16 不消除盲区, 只是缓解 collapse 幅度; ECE 和 effective_rank 在 bf16 下行为模式与 fp32 完全不同 (方向逆转)
4. Correlation vs causation 分离: naive (7/8) 和 diff_xcorr (8/8) 检出强相关, 但 PermG/TY 无因果信号, 说明 canary 与 downstream 存在 co-movement 但无 temporal precedence
