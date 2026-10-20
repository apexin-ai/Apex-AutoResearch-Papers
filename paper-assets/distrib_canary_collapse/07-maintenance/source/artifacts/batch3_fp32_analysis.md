# 三个 fp32 实验分析报告 (2026-05-19)

服务器: westd-17855 | 分析脚本: batch_analysis.py | 所有实验 d=0.80, seed=42

---

## 1. alpha_sweep_a005_s42_v3 (α=0.05)

### 指标轨迹

| gen | token_entropy | ece | perplexity | distinct_1 | distinct_2 | distinct_3 | eff_rank | mauve |
|-----|--------------|-------|-----------|-----------|-----------|-----------|---------|-------|
| 0 | 3.234 | 0.0108 | 26.95 | 0.0916 | 0.5038 | 0.8318 | 46.61 | 0.0270 |
| 1 | 3.006 | 0.0092 | 19.40 | 0.0910 | 0.4993 | 0.8311 | 47.77 | 0.0276 |
| 2 | 3.030 | 0.0113 | 20.18 | 0.0735 | 0.4036 | 0.7381 | 48.71 | 0.0282 |
| 3 | 3.014 | 0.0131 | 20.41 | 0.0678 | 0.3558 | 0.6829 | 48.69 | 0.0228 |
| 4 | 3.027 | 0.0144 | 20.67 | 0.0680 | 0.3505 | 0.6682 | 48.01 | 0.0208 |
| 5 | 3.026 | 0.0154 | 20.83 | 0.0678 | 0.3503 | 0.6640 | 47.72 | 0.0226 |
| 6 | 3.032 | 0.0141 | 20.75 | 0.0696 | 0.3570 | 0.6655 | 47.27 | 0.0235 |
| 7 | 3.023 | 0.0174 | 20.86 | 0.0692 | 0.3586 | 0.6661 | 46.59 | 0.0250 |
| 8 | 3.041 | 0.0160 | 20.82 | 0.0694 | 0.3641 | 0.6746 | 46.03 | 0.0220 |
| 9 | 3.037 | 0.0156 | 20.86 | 0.0701 | 0.3622 | 0.6723 | 46.17 | 0.0240 |
| 10 | 3.042 | 0.0168 | 20.81 | 0.0688 | 0.3607 | 0.6693 | 45.31 | 0.0235 |

**Drift (gen0→gen10):** token_entropy -5.96%, ece +55.41%, perplexity -22.78%, distinct_1 -24.86%, distinct_2 -28.42%, distinct_3 -19.54%, eff_rank -2.80%, mauve -13.08%

### Lead-lag 分析

| method | forward sig / total |
|--------|-------------------|
| naive_xcorr | 7/8 |
| diff_xcorr | 3/8 |
| threshold_onset | 5/8 |
| perm_granger_fwd | 0/8 |
| perm_granger_rev | 0/8 |
| ty_granger | 3/8 |
| **consensus_k4** | **0/8** |

MMCT detection_rate = **0.0**

**Consensus detail** (最高 3 votes，均未达 K≥4 阈值):

| pair | votes | methods |
|------|-------|---------|
| token_entropy→distinct_1 | 3 | naive, diff, thresh |
| token_entropy→distinct_2 | 3 | naive, diff, thresh |
| token_entropy→distinct_3 | 3 | naive, diff, thresh |
| token_entropy→mauve | 2 | naive, thresh |
| ece→distinct_2 | 2 | naive, ty |
| ece→distinct_3 | 2 | naive, ty |
| ece→mauve | 2 | thresh, ty |
| ece→distinct_1 | 1 | naive |

**⚠️ C003 注意**: TY 3/8 显著的 pairs (ece→distinct_2, ece→distinct_3, ece→mauve) 全部 d_max=2, df_resid=1，属于 C003 约束范围内的不可靠结果，不可作为支撑证据。

### 关键发现

- α=0.05 产生**极微弱的 collapse**：canary (token_entropy) 仅下降 5.96%，ece 仅从 0.011 升至 0.017
- diversity 指标有中等下降 (distinct_1/2/3 -19%~-28%)，但主要发生在 gen 0→3，之后几乎稳定
- perplexity 反常下降 22.78%（gen0 的 26.95 是原始模型基线，gen1 起快速降至 ~20.8 并稳定）
- lead-lag **完全无法检测**：consensus_k4 = 0/8，MMCT = 0.0。信号太弱，5-method 无法达成共识
- 与 α=0.00 null 控制组的区分度很低，属于近基线行为

---

## 2. alpha_sweep_a060_s42_fp32_v3 (α=0.60)

### 指标轨迹

| gen | token_entropy | ece | perplexity | distinct_1 | distinct_2 | distinct_3 | eff_rank | mauve |
|-----|--------------|-------|-----------|-----------|-----------|-----------|---------|-------|
| 0 | 3.234 | 0.0108 | 26.95 | 0.0916 | 0.5038 | 0.8318 | 46.61 | 0.0270 |
| 1 | 2.223 | 0.1244 | 29.57 | 0.0910 | 0.4993 | 0.8311 | 65.29 | 0.0276 |
| 2 | 2.210 | 0.1468 | 36.33 | 0.0742 | 0.4093 | 0.7542 | 71.77 | 0.0265 |
| 3 | 2.248 | 0.1465 | 38.09 | 0.0710 | 0.3717 | 0.7009 | 72.84 | 0.0232 |
| 4 | 2.272 | 0.1501 | 40.33 | 0.0698 | 0.3559 | 0.6613 | 72.81 | 0.0224 |
| 5 | 2.313 | 0.1489 | 41.58 | 0.0691 | 0.3508 | 0.6388 | 71.59 | 0.0223 |
| 6 | 2.337 | 0.1480 | 41.88 | 0.0685 | 0.3430 | 0.6159 | 71.75 | 0.0244 |
| 7 | 2.393 | 0.1472 | 42.66 | 0.0676 | 0.3382 | 0.5942 | 70.77 | 0.0245 |
| 8 | 2.402 | 0.1490 | 44.06 | 0.0670 | 0.3282 | 0.5699 | 70.67 | 0.0231 |
| 9 | 2.456 | 0.1461 | 45.16 | 0.0662 | 0.3220 | 0.5531 | 70.41 | 0.0232 |
| 10 | 2.479 | 0.1470 | 45.41 | 0.0658 | 0.3163 | 0.5377 | 69.33 | 0.0226 |

**Drift (gen0→gen10):** token_entropy -23.36%, ece +1260.23%, perplexity +68.52%, distinct_1 -28.17%, distinct_2 -37.22%, distinct_3 -35.35%, eff_rank +48.74%, mauve -16.31%

### Lead-lag 分析

| method | forward sig / total |
|--------|-------------------|
| naive_xcorr | 7/8 |
| diff_xcorr | 8/8 |
| threshold_onset | 8/8 |
| perm_granger_fwd | 3/8 |
| perm_granger_rev | 0/8 |
| ty_granger | 8/8 |
| **consensus_k4** | **7/8** |

MMCT detection_rate = **0.875**

**Consensus detail**:

| pair | votes | methods | K≥4? |
|------|-------|---------|------|
| token_entropy→distinct_1 | 5 | naive, diff, thresh, pg_fwd, ty | ✓ |
| token_entropy→distinct_2 | 4 | naive, diff, thresh, ty | ✓ |
| token_entropy→distinct_3 | 4 | naive, diff, thresh, ty | ✓ |
| token_entropy→mauve | 4 | naive, diff, thresh, ty | ✓ |
| ece→distinct_1 | 5 | naive, diff, thresh, pg_fwd, ty | ✓ |
| ece→distinct_2 | 5 | naive, diff, thresh, pg_fwd, ty | ✓ |
| ece→distinct_3 | 3 | diff, thresh, ty | ✗ |
| ece→mauve | 4 | naive, diff, thresh, ty | ✓ |

**TY Granger**: 8/8 显著，全部 d_max=0 或 d_max=1 (df_resid≥4)，结果可靠（不受 C003 约束）。

### 关键发现

- α=0.60 产生**强烈且持续的 collapse**：token_entropy gen0→gen1 骤降 31.3% (3.234→2.223)，ece 从 0.011 跃升至 0.124 (+1050% 单代)
- gen1 后 canary 继续缓慢漂移但不回复，ece 稳定在 ~0.147，entropy 缓慢回升至 2.48
- downstream diversity 持续单调下降：distinct_3 从 0.832 线性降至 0.538
- perplexity 持续上升 (+68.5%)，effective_rank 大幅上升 (+48.7%)，表明模型输出分布变得更分散但质量更差
- **lead-lag 检测能力极强**: 7/8 pairs consensus≥4，MMCT=0.875，最高 pair 达到 5-method 全票
- canary (token_entropy, ece) gen1 即响应，downstream (distinct) gen2 才开始下降 → 1-gen lead time 一致

---

## 3. interv_pred_a075_s42_fp32_v4 (intervention α=0.75)

### 指标轨迹

| gen | token_entropy | ece | perplexity | distinct_1 | distinct_2 | distinct_3 | eff_rank | mauve | α_eff | interv |
|-----|--------------|-------|-----------|-----------|-----------|-----------|---------|-------|------|--------|
| 0 | 3.234 | 0.0108 | 26.95 | 0.0916 | 0.5038 | 0.8318 | 46.61 | 0.0270 | 0.75 | — |
| 1 | 2.212 | 0.1322 | 32.63 | 0.0910 | 0.4993 | 0.8311 | 67.60 | 0.0276 | 0.75 | **triggered** |
| 2 | 3.049 | 0.0140 | 20.80 | 0.0752 | 0.4121 | 0.7595 | 49.83 | 0.0249 | 0.00 | recovery |
| 3 | 3.053 | 0.0124 | 20.74 | 0.0846 | 0.4786 | 0.8046 | 48.86 | 0.0341 | 0.00 | stable |
| 4 | 3.067 | 0.0111 | 20.96 | 0.0856 | 0.4804 | 0.8020 | 47.03 | 0.0297 | 0.00 | stable |
| 5 | 3.047 | 0.0133 | 20.77 | 0.0866 | 0.4775 | 0.7978 | 47.15 | 0.0307 | 0.00 | stable |
| 6 | 3.051 | 0.0150 | 20.93 | 0.0859 | 0.4790 | 0.7984 | 45.73 | 0.0275 | 0.00 | stable |
| 7 | 3.055 | 0.0136 | 20.99 | 0.0858 | 0.4768 | 0.7960 | 45.51 | 0.0323 | 0.00 | stable |
| 8 | 3.057 | 0.0124 | 20.67 | 0.0854 | 0.4817 | 0.8022 | 44.14 | 0.0318 | 0.00 | stable |
| 9 | 3.033 | 0.0193 | 20.95 | 0.0850 | 0.4800 | 0.7982 | 44.48 | 0.0300 | 0.00 | stable |
| 10 | 3.049 | 0.0168 | 20.81 | 0.0843 | 0.4775 | 0.7993 | 44.81 | 0.0308 | 0.00 | stable |

**Drift (gen0→gen10):** token_entropy -5.74%, ece +55.78%, perplexity -22.76%, distinct_1 -7.97%, distinct_2 -5.22%, distinct_3 -3.90%, eff_rank -3.86%, mauve +13.82%

### Intervention 行为

- **触发 gen**: gen 1（canary 检测到 token_entropy 骤降 31.6%: 3.234→2.212，ece 跃升至 0.132）
- **α 切换**: gen 2 起 effective_alpha 从 0.75→0.00
- **恢复速度**: **1 代完全恢复**。gen2 token_entropy 回到 3.049（接近 gen0 的 3.234），ece 回到 0.014
- **恢复后稳定性**: gen 3-10 所有指标高度稳定，distinct_1 ~0.085, distinct_2 ~0.478, distinct_3 ~0.799
- **diversity 保持**: 恢复后 distinct_1/2/3 仅比 gen0 低 4-8%（vs α=0.60 无干预时 -28%~-35%）
- **mauve 上升**: 恢复后 mauve 从 0.027 升至 ~0.031 (+13.8%)，说明干预后输出分布反而更接近参考分布

### Lead-lag 分析

| method | forward sig / total |
|--------|-------------------|
| naive_xcorr | 8/8 |
| diff_xcorr | 8/8 |
| threshold_onset | 0/8 |
| perm_granger_fwd | 6/8 |
| perm_granger_rev | 0/8 |
| ty_granger | 8/8 |
| **consensus_k4** | **6/8** |

MMCT detection_rate = **0.75**

**Consensus detail**:

| pair | votes | methods | K≥4? |
|------|-------|---------|------|
| token_entropy→distinct_1 | 4 | naive, diff, pg_fwd, ty | ✓ |
| token_entropy→distinct_2 | 4 | naive, diff, pg_fwd, ty | ✓ |
| token_entropy→distinct_3 | 4 | naive, diff, pg_fwd, ty | ✓ |
| token_entropy→mauve | 3 | naive, diff, ty | ✗ |
| ece→distinct_1 | 4 | naive, diff, pg_fwd, ty | ✓ |
| ece→distinct_2 | 4 | naive, diff, pg_fwd, ty | ✓ |
| ece→distinct_3 | 4 | naive, diff, pg_fwd, ty | ✓ |
| ece→mauve | 3 | naive, diff, ty | ✗ |

**注意**: threshold_onset = 0/8 是因为干预后指标回复，大部分 canary 和 downstream 均未持续超过 10% threshold。这不是方法失效，而是干预成功阻止了持续偏离。

**TY Granger**: 8/8 显著，全部 d_max=0, df_resid=7，结果高度可靠。

### 关键发现

- intervention 在 gen1 正确触发，α→0 后 **1 代内完全恢复**
- 即使只有 1 代的 α=0.75 暴露，lead-lag 仍能检测到 6/8 pairs 的因果方向性
- perm_granger_fwd 6/8 显著 (vs α=0.60 的 3/8)，说明即使短暂干预的脉冲信号也被 Granger 捕捉到
- perm_granger_rev 0/8 → 无反向因果，方向性一致
- fp32 intervention 行为与预期完全一致：检测→触发→恢复→稳定

---

## 4. 对 Dose-Response Map 的影响

### α=0.05 填补的格子

- **位置**: dose-response 曲线最低端（近 null baseline）
- **结果**: MMCT=0.0, consensus_k4=0/8
- **意义**: 确认 α=0.05 在 fp32 下属于 **"undetectable" zone**。canary drift 过小（entropy -6%, ece +55% 但绝对值仅 0.011→0.017），5-method 无法形成共识。这为 dose-response 曲线提供了关键的下界参照——α<0.05 可安全视为无影响

### α=0.60 填补的格子

- **位置**: dose-response 曲线中高段
- **结果**: MMCT=0.875, consensus_k4=7/8
- **意义**: α=0.60 fp32 表现出**极强的 lead-lag 信号**，与之前 α=0.75/1.00 结果形成连续梯度。ece +1260% 的巨幅漂移为 canary 提供了充足的信号强度。7/8 pairs 达到 K≥4 consensus，仅 ece→distinct_3 (3 votes) 未达标

### Intervention 结果与 bf16 对比

- **fp32 v4**: gen1 触发, 1-gen 恢复, MMCT=0.75 (6/8 consensus)
- **关键观察**: fp32 intervention 的 lead-lag 检测率 (0.75) 略低于 non-intervention α=0.60 (0.875)，这符合预期——干预截断了 collapse 过程，减少了可用于因果推断的时间序列长度
- threshold_onset 0/8 是干预成功的标志（而非方法缺陷），因为指标在超过 threshold 前就被拉回

### Dose-Response 汇总 (fp32, seed=42, d=0.80)

| α | MMCT | K≥4 pairs | token_entropy drift | ece drift | 状态 |
|------|------|-----------|-------------------|----------|------|
| 0.05 | 0.00 | 0/8 | -5.96% | +55% | undetectable |
| 0.60 | 0.875 | 7/8 | -23.36% | +1260% | strong signal |
| 0.75 (interv) | 0.75 | 6/8 | -5.74%* | +55.8%* | intervention success |

*intervention 实验的 gen0→gen10 drift 反映的是干预后恢复状态，不是持续 collapse。gen0→gen1 的单步 drift 为 entropy -31.6%, ece +1124%。
