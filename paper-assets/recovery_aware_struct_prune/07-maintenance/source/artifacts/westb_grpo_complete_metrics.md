# westb GRPO Training Complete Metrics

Updated: 2026-05-18

## SSH 修复状态
- 公钥添加: 不需要（SSH 免密已正常）
- 免密测试: 成功（hostname: autodl-container-16vw4zvw9r-b25fad2c）

## grpo_cka_only_20 (CKA-only 20% pruned)
- 训练状态: 进行中 at step 94/100
- 总步数: 94/100（预计剩余 ~40min）
- GPU: cuda:0
- 配置: beta=0.01, loss_type=dapo, format_reward=0.1, lr=1e-6, optim=adamw_bnb_8bit, temperature=0.4, repetition_penalty=1.15, max_completion_length=1024

| Step | Reward | frac_zero_std | grad_norm | 备注 |
|------|--------|---------------|-----------|------|
| 10   | 0.2531 | 0.175         | 1.891     |      |
| 20   | 0.2181 | 0.200         | 1.250     |      |
| 30   | 0.2500 | 0.200         | 1.102     |      |
| 40   | 0.2344 | 0.350         | 0.984     |      |
| 50   | 0.3544 | 0.150         | 1.977     | peak reward |
| 60   | 0.2994 | 0.200         | 3.750     |      |
| 70   | 0.3075 | 0.125         | 1.164     | lowest frac_zero_std |
| 80   | 0.3419 | 0.250         | 2.672     | second peak reward |
| 90   | 0.2419 | 0.300         | 1.219     | reward drops, frac_zero rises |

### 趋势分析 (step 70-90)
- Step 70: reward=0.3075, frac_zero_std=0.125 (peak diversity, low zero-std)
- Step 80: reward=0.3419, frac_zero_std=0.25 (reward peaks but frac_zero starts rising)
- Step 90: reward=0.2419, frac_zero_std=0.3 (明显下降，collapse 风险信号)
- reward 从 step 80 的 0.3419 下降至 step 90 的 0.2419 (下降 29.3%)
- frac_zero_std 从 step 70 的 0.125 升至 step 90 的 0.3 (上升 140%)

## grpo_random_20 (Random 20% pruned)
- 训练状态: 进行中 at step 97/100
- 总步数: 97/100（预计剩余 ~20min）
- GPU: cuda:1
- 配置: 同上

| Step | Reward | frac_zero_std | grad_norm | 备注 |
|------|--------|---------------|-----------|------|
| 10   | 0.1606 | 0.300         | 3.750     |      |
| 20   | 0.1419 | 0.325         | 8.625     | grad_norm spike |
| 30   | 0.1663 | 0.325         | 3.672     |      |
| 40   | 0.1450 | 0.400         | 4.188     | highest frac_zero_std |
| 50   | 0.1750 | 0.300         | 4.750     |      |
| 60   | 0.1844 | 0.350         | 3.594     |      |
| 70   | 0.1900 | 0.300         | 7.094     | grad_norm spike |
| 80   | 0.1419 | 0.375         | 3.688     | reward dip |
| 90   | 0.1725 | 0.325         | 7.531     | grad_norm spike |

### 趋势分析
- Reward 全程在 0.14-0.19 区间波动，无明显上升趋势
- frac_zero_std 始终在 0.30-0.40，显著高于 CKA 实验（CKA: 0.125-0.35）
- grad_norm 不稳定（频繁出现 7-8 的 spike），表明优化困难
- 整体表现远低于 CKA-pruned 模型

## 对比总结

| 指标 | CKA-only 20% | Random 20% | 差异 |
|------|--------------|------------|------|
| Best Reward | 0.3544 (step 50) | 0.1900 (step 70) | CKA +86.5% |
| Mean Reward (10-90) | 0.2834 | 0.1653 | CKA +71.4% |
| Best frac_zero_std | 0.125 (step 70) | 0.300 (step 50/70) | CKA 更低=更好 |
| Mean grad_norm | 1.779 | 5.227 | CKA 训练更稳定 |

**结论**: CKA-guided pruning 产生的模型在 GRPO 训练中表现显著优于 random pruning:
1. 更高的 reward（平均+71%）
2. 更低的 frac_zero_std（更少的 collapse）
3. 更稳定的 grad_norm（训练更平稳）

但 CKA 实验 step 80->90 的 reward 下降和 frac_zero_std 上升值得关注，可能是 late-stage collapse 的信号。
