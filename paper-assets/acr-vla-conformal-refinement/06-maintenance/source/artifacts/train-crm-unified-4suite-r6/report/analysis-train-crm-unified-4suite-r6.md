# Analysis: train-crm-unified-4suite-r6

## Status: SUCCESS

训练正常完成，50 epoch 全部跑完，EXIT_CODE=0。

## 训练配置

| 项目 | 值 |
|------|-----|
| 模型 | crm_obs_only_4suite (327,198 params) |
| Input mode | obs_only |
| Loss | MSE + λ_conf=0.1 |
| 数据量 | 224,555 samples (object: 14,570, spatial: 12,167, goal: 61,728, long: 136,090) |
| Batch size | 32 |
| LR | 0.001 (cosine decay) |
| K | 10 |
| obs_dim | 960, hidden_dim=256 |
| Val split | 0.1 |
| Resume | 从 epoch 38 (val_loss=0.005965) 继续 |

## Loss 收敛

| Epoch | Train Loss | Val Loss | LR |
|-------|-----------|----------|-----|
| 1 | 0.019415 | 0.010801 | 9.99e-04 |
| 10 | 0.014236 | 0.008281 | 9.05e-04 |
| 20 | 0.012215 | 0.007255 | 6.55e-04 |
| 30 | 0.010743 | 0.006270 | 3.45e-04 |
| 38 | 0.010174 | 0.005965 | 2.77e-04 |
| 40 | 0.010075 | 0.005864 | 2.76e-04 |
| 45 | 0.009903 | 0.005784 | 2.64e-04 |
| 50 | 0.009731 | 0.005669 | 2.39e-04 |

- Train loss: 0.019415 → 0.009731 (↓49.9%)
- Val loss: 0.010801 → 0.005669 (↓47.5%)
- Best val_loss = **0.005669** (epoch 50，最后一个 epoch 仍在刷新 best)
- 无过拟合迹象，loss 单调下降
- 注意：val_loss 到最后仍在改善，可能还有继续训练的空间

## Per-suite Loss

日志未记录分 suite 的 val_loss，只有总体 loss。

## Checkpoint

| 文件 | 大小 | 时间 |
|------|------|------|
| `/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt` | 1.3M | May 23 17:05 |
| `checkpoint_epoch0050.pt` | 3.8M | May 23 17:05 |
| `checkpoint_epoch0049.pt` | 3.8M | May 23 16:40 |
| `checkpoint_epoch0048.pt` | 3.8M | May 23 16:16 |
| `checkpoint_epoch0047.pt` | 3.8M | May 23 15:52 |
| `checkpoint_epoch0046.pt` | 3.8M | May 23 15:27 |

**最终 checkpoint 路径**: `/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt`

## W&B

无 W&B 集成（日志中无 wandb 相关输出）。

## Conclusion: **SUCCESS**

- 训练正常完成 50 epoch，loss 持续收敛，无异常
- Val loss 最后几个 epoch 仍在改善（0.005781 → 0.005669），模型未饱和
- 单一统一模型覆盖 4 个 LIBERO suite (object/spatial/goal/long)

## 建议下一步

1. **用 crm_best.pt 在 4 个 suite 上分别跑 eval**，评估各 suite 的 conformal prediction 质量（coverage、set size）
2. **对比 per-suite 独立训练的 CRM**，验证 unified 模型是否在各 suite 上都达到可比性能
3. 可选：由于 val_loss 仍在下降，可以考虑继续训练到 60-80 epoch 看是否进一步改善
