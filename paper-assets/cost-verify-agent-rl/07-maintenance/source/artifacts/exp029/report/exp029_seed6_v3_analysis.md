## exp029_seed6_v3 结果分析

**conclusion**: success
**最终指标**:
- global_step: 15
- val_success_rate: 28.125%
- train_reward_mean: 7.11 (final step), peak 8.91 (step 14)
- kl_divergence: 0.0019 (final step)
- actor/entropy: 0.037 (final step)
- response_length: 5097 tokens (final), 从 14910 (step 1) 持续下降

**训练曲线概述**:

Val success rate 单调上升：9.375% (step 0) → 21.875% (step 5) → 28.125% (step 10) → 28.125% (step 15)。Step 10-15 之间 val 持平。

Train success rate 整体上升但有波动：7.0% (step 1) → 50.8% (step 5) → 78.1% (step 10) → 89.1% (step 14)。Pass@8 从 93.75% 升到 100%。

Reward 持续增长：0.70 → 5.08 → 7.81 → 8.91，无 collapse 迹象。

Response length 持续缩短（14910 → 3329），agent 学会了更高效的行动策略。

KL 保持在低位（< 0.008），actor entropy 在 0.03-0.08 范围内波动，训练稳定。

**checkpoint 路径**: `/root/autodl-tmp/checkpoints/exp029-seed6/global_step_15/actor/` (仅保留最终 checkpoint)
**log 路径**: `~/runs/cost-verify-agent-rl/exp029_seed6_v3.log`
**W&B run**: https://wandb.ai/xiaoyucorynne-/cost-verify-agent-rl/runs/2bbyvsdr

**Per-step 训练指标 (W&B)**:

| Step | Train Success | Reward Mean | PPO KL | Entropy | Resp Length |
|------|-------------|-------------|--------|---------|-------------|
| 1 | 7.0% | 0.70 | 0.0003 | 0.028 | 14910 |
| 2 | 40.6% | 4.06 | -0.0004 | 0.070 | 8192 |
| 3 | 35.2% | 3.52 | 0.0003 | 0.032 | 10179 |
| 4 | 34.4% | 3.44 | 0.0004 | 0.063 | 9297 |
| 5 | 50.8% | 5.08 | 0.0017 | 0.039 | 8419 |
| 6 | 42.2% | 4.22 | 0.0076 | 0.068 | 9604 |
| 7 | 71.1% | 7.11 | -0.0031 | 0.077 | 5508 |
| 8 | 57.0% | 5.70 | 0.0047 | 0.069 | 7092 |
| 9 | 67.2% | 6.72 | 0.0012 | 0.079 | 6835 |
| 10 | 78.1% | 7.81 | 0.0019 | 0.070 | 4865 |
| 11 | 82.0% | 8.20 | 0.0007 | 0.067 | 4175 |
| 12 | 80.5% | 8.05 | 0.0019 | 0.052 | 4454 |
| 13 | 67.9% | 6.80 | 0.0024 | 0.031 | 6660 |
| 14 | 89.1% | 8.91 | 0.0008 | 0.036 | 3329 |

Val 评估点 (32 episodes each):
| Step | Val Success | Val Reward Mean@32 |
|------|-----------|-------------------|
| 0 | 9.375% | 0.9375 |
| 5 | 21.875% | 2.1875 |
| 10 | 28.125% | 2.8125 |
| 15 | 28.125% | 2.8125 |

**与其他 seed 对比**:
- vs Seed 1 (val ~43%, OOD 23.88%): Seed 6 val 28.1% 明显低于 Seed 1，差距 ~15pp
- vs Seed 3 (val ~40.6%, OOD 10.45%): Seed 6 val 28.1% 低于 Seed 3，差距 ~12.5pp
- Seed 6 是已完成三个 seed 中 val 最低的，但仍满足 ≥20% 成功标准

**下一步建议**:
1. 对 global_step_15 checkpoint 运行 OOD eval（ScienceWorld），与 Seed 1/3 对比泛化能力
2. Seed 6 val 在 step 10-15 持平（28.1%），可能已接近该 seed 的收敛上限
3. 等 Seed 4/5 结束后汇总全部 5 seeds，分析 seed 间方差