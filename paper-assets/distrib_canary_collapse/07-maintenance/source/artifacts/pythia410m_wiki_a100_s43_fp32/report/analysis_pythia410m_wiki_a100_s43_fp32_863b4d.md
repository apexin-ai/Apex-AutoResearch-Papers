# Analysis: pythia410m_wiki_a100_s43_fp32

## 1. Config

| Key | Value |
|-----|-------|
| model | EleutherAI/pythia-410m |
| dataset | WikiText-103 (5k subset) |
| α (synthetic_ratio) | 1.0 |
| seed | 43 |
| precision | fp32 |
| generations | 11 (gen_0–gen_10) |
| steps_per_gen | 5000 |
| batch_size | 4 |
| lr | 5e-05 |
| server | westd-17855 |
| parent | generalize_pythia410m_wiki_a100_s42 |

## 2. Hypothesis

Pythia-410M s43 cross-seed 验证：410M 是 dose-response 全部实验的 base model，但 Table 7 α=1.0 仅有 s42 单 seed（PermG=6/8, K≥3=6/8）。5/8 架构单 seed 是审稿攻击面。s43 验证 core model 的跨 seed 稳健性。Claim 1/3。

## 3. Result Summary

**Cross-seed 验证通过。** s43 的 PermG=6/8、K≥3=6/8 与 s42 完全一致，threshold_onset=8/8，TY=6/8。两个 mauve pair 在两个 seed 上均不显著，是 mauve 本身在 T=11 下信号弱的稳健特征，非随机波动。K≥4 从 s42 的 1/8 降至 0/8，差异来源于 naive/diff xcorr 的 D111 direction filtering（所有 pair peak_lag≤0）。

## 4. Training Completion

- EXIT_CODE=0，正常完成
- gen_0–gen_10 所有 metrics.json 完整
- all_metrics.json 已生成
- 最终 gen_10: ppl=960.41, entropy=1.1639, eff_rank=109.5, mauve=0.0322

## 5. Per-Generation Metrics

| Gen | token_entropy | ece | distinct_1 | distinct_2 | distinct_3 | perplexity | effective_rank | mauve |
|-----|--------------|-----|-----------|-----------|-----------|-----------|---------------|-------|
| 0 | 3.2342 | 0.0108 | 0.0983 | 0.5146 | 0.8140 | 26.95 | 46.61 | 0.0315 |
| 1 | 1.7930 | 0.2187 | 0.0966 | 0.5112 | 0.8110 | 55.59 | 77.45 | 0.0313 |
| 2 | 1.4034 | 0.3293 | 0.0827 | 0.4321 | 0.7167 | 158.22 | 95.34 | 0.0329 |
| 3 | 1.2791 | 0.3655 | 0.0795 | 0.4074 | 0.6752 | 266.83 | 100.48 | 0.0318 |
| 4 | 1.2208 | 0.3846 | 0.0792 | 0.4036 | 0.6684 | 368.24 | 103.66 | 0.0314 |
| 5 | 1.1747 | 0.3977 | 0.0790 | 0.4024 | 0.6663 | 464.70 | 105.89 | 0.0313 |
| 6 | 1.1694 | 0.4060 | 0.0789 | 0.4014 | 0.6647 | 553.71 | 105.04 | 0.0306 |
| 7 | 1.1579 | 0.4121 | 0.0789 | 0.4012 | 0.6639 | 650.35 | 94.58 | 0.0321 |
| 8 | 1.1688 | 0.4169 | 0.0789 | 0.4008 | 0.6634 | 742.62 | 105.70 | 0.0325 |
| 9 | 1.1581 | 0.4215 | 0.0788 | 0.4006 | 0.6632 | 846.16 | 108.41 | 0.0322 |
| 10 | 1.1639 | 0.4260 | 0.0788 | 0.4004 | 0.6629 | 960.41 | 109.54 | 0.0322 |

## 6. Drift (gen_0 → gen_10)

| Metric | gen_0 | gen_10 | Δ% |
|--------|-------|--------|-----|
| token_entropy | 3.2342 | 1.1639 | **-64.01%** |
| ece | 0.0108 | 0.4260 | **+3842.72%** |
| perplexity | 26.95 | 960.41 | **+3463.79%** |
| distinct_1 | 0.0983 | 0.0788 | **-19.78%** |
| distinct_2 | 0.5146 | 0.4004 | **-22.20%** |
| distinct_3 | 0.8140 | 0.6629 | **-18.56%** |
| effective_rank | 46.61 | 109.54 | **+134.99%** |
| mauve | 0.0315 | 0.0322 | +2.15% |

## 7. 5-Method Lead-Lag Summary

| Method | Forward sig / 8 |
|--------|-----------------|
| naive_xcorr (D111) | **0/8** |
| diff_xcorr (D111 FDR) | **0/8** |
| threshold_onset (3σ) | **8/8** |
| PermG fwd (FDR) | **6/8** |
| PermG rev (FDR) | 0/8 |
| TY Granger | **6/8** |
| **K≥3 (3σ)** | **6/8** |
| **K≥4** | **0/8** |

D111 note: All naive_xcorr and diff_xcorr peak lags are ≤0 (reverse direction), excluded from forward count. This is consistent across both seeds — xcorr methods detect strong contemporaneous/reverse correlation in the co-trending entropy/diversity series, but cannot isolate a forward lead at T=11 resolution.

## 8. Per-Pair Detail

### token_entropy → distinct_1
| Method | Result | Detail |
|--------|--------|--------|
| naive_xcorr | lag=-1 (excluded D111) | r=0.994, p<0.001 |
| diff_xcorr | lag=-1 (excluded D111) | r=0.9975, p_fdr<0.001 |
| threshold_onset | **fwd lead=1** | onset_c=1, onset_d=2 |
| PermG fwd | **sig** (FDR) | F=1714.76, p_fdr=0.0028 |
| PermG rev | NS | p_fdr=0.473 |
| TY Granger | **sig** | χ²=562.0, p<0.001, d_max=0 |
| **Votes: 3/5** | [thresh, pg, ty] | |

### token_entropy → distinct_2
| Method | Result | Detail |
|--------|--------|--------|
| naive_xcorr | lag=-1 (excluded D111) | r=0.9982 |
| diff_xcorr | lag=-1 (excluded D111) | r=0.9977 |
| threshold_onset | **fwd lead=1** | onset_c=1, onset_d=2 |
| PermG fwd | **sig** (FDR) | F=1851.44, p_fdr=0.0028 |
| PermG rev | NS | p_fdr=0.419 |
| TY Granger | **sig** | χ²=903.55, p<0.001, d_max=0 |
| **Votes: 3/5** | [thresh, pg, ty] | |

### token_entropy → distinct_3
| Method | Result | Detail |
|--------|--------|--------|
| naive_xcorr | lag=-1 (excluded D111) | |
| diff_xcorr | lag=-2 (excluded D111) | |
| threshold_onset | **fwd lead=1** | onset_c=1, onset_d=2 |
| PermG fwd | **sig** (FDR) | F=791.53, p_fdr=0.0072 |
| PermG rev | NS | p_fdr=0.399 |
| TY Granger | **sig** | χ²=750.10, p<0.001, d_max=0 |
| **Votes: 3/5** | [thresh, pg, ty] | |

### token_entropy → mauve
| Method | Result | Detail |
|--------|--------|--------|
| naive_xcorr | lag=-5 (excluded D111) | NS |
| diff_xcorr | lag=5 | r weak, NS |
| threshold_onset | **fwd lead=10** | onset_c=1, onset_d=None (never crossed) |
| PermG fwd | NS | F=1.99, p_fdr=0.242 |
| PermG rev | NS | p_fdr=0.473 |
| TY Granger | NS | χ²=2.35, p=0.126, d_max=1 |
| **Votes: 1/5** | [thresh] | |

### ece → distinct_1
| Method | Result | Detail |
|--------|--------|--------|
| naive_xcorr | lag=-3 (excluded D111) | |
| diff_xcorr | lag=-1 (excluded D111) | |
| threshold_onset | **fwd lead=1** | onset_c=1, onset_d=2 |
| PermG fwd | **sig** (FDR) | F=963.61, p_fdr=0.00288 |
| PermG rev | NS | p_fdr=0.106 |
| TY Granger | **sig** | χ²=56.96, p<0.001, d_max=0 |
| **Votes: 3/5** | [thresh, pg, ty] | |

### ece → distinct_2
| Method | Result | Detail |
|--------|--------|--------|
| naive_xcorr | lag=-3 (excluded D111) | |
| diff_xcorr | lag=-1 (excluded D111) | |
| threshold_onset | **fwd lead=1** | onset_c=1, onset_d=2 |
| PermG fwd | **sig** (FDR) | F=1731.36, p_fdr=0.0008 |
| PermG rev | NS | p_fdr=0.156 |
| TY Granger | **sig** | χ²=96.90, p<0.001, d_max=0 |
| **Votes: 3/5** | [thresh, pg, ty] | |

### ece → distinct_3
| Method | Result | Detail |
|--------|--------|--------|
| naive_xcorr | lag=-3 (excluded D111) | |
| diff_xcorr | lag=-1 (excluded D111) | |
| threshold_onset | **fwd lead=1** | onset_c=1, onset_d=2 |
| PermG fwd | **sig** (FDR) | F=1799.84, p_fdr=0.0008 |
| PermG rev | NS | p_fdr=0.156 |
| TY Granger | **sig** | χ²=130.41, p<0.001, d_max=0 |
| **Votes: 3/5** | [thresh, pg, ty] | |

### ece → mauve
| Method | Result | Detail |
|--------|--------|--------|
| naive_xcorr | lag=-5 (excluded D111) | NS |
| diff_xcorr | lag=-2 (excluded D111) | NS |
| threshold_onset | **fwd lead=10** | onset_c=1, onset_d=None |
| PermG fwd | NS | F=1.02, p_fdr=0.391 |
| PermG rev | NS | p_fdr=0.259 |
| TY Granger | NS | χ²=1.97, p=0.160, d_max=1 |
| **Votes: 1/5** | [thresh] | |

## 9. Cross-Seed Comparison (s42 vs s43)

| Metric | s42 | s43 | Match? |
|--------|-----|-----|--------|
| PermG fwd (FDR) | 6/8 | 6/8 | ✓ |
| K≥3 (3σ) | 6/8 | 6/8 | ✓ |
| K≥4 | 1/8 | 0/8 | ~close |
| threshold_onset | 8/8 | 8/8 | ✓ |
| TY Granger | 6/8 | 6/8 | ✓ |
| naive_xcorr (D111) | — | 0/8 | — |
| diff_xcorr (D111) | — | 0/8 | — |
| PermG rev (FDR) | — | 0/8 | — |
| Non-significant pairs | mauve×2 | mauve×2 | ✓ |

**Conclusion**: PermG 和 K≥3 在两个 seed 上完全一致（6/8）。失败的 pair 都是 mauve 对（entropy→mauve, ece→mauve），这是 mauve 在 T=11 短序列下信号本身弱的系统性特征，跨 seed 稳健复现。K≥4 的 1 pair 差异（s42=1/8 vs s43=0/8）处于方法噪声范围内，不影响 cross-seed 稳健性判定。

## 10. Notes

- D105: 3σ threshold applied to threshold_onset
- D111: naive_xcorr and diff_xcorr lag≤0 excluded from forward count; all 8 pairs had peak_lag≤0
- D086: per-alpha BH FDR correction, n_perm=5000
- D102: 8 pairs = {entropy, ece} × {d1, d2, d3, mauve}
- TY Granger d_max=0 for all 6 significant pairs (series appear stationary); d_max=1 for 2 mauve pairs
- PermG rev uniformly NS (0/8), confirming directionality: canary → downstream, not reverse
- Mauve drift only +2.15% (essentially flat), explaining why all methods fail on mauve pairs
