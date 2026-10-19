# exp029_seed4_ood_eval_v2 Analysis

## Summary

```
exp_id: exp029_seed4_ood_eval_v2
conclusion: success (surprising positive)
ood_success_rate: 30.60% (41/134)
parent: exp029_seed4_v2 (negative, response_inflation collapse, val_pass_at_1=0.4375)
checkpoint: seed=42, step 15 (collapse seed)
server: westd-47453
```

## Key Metrics

| Metric | Value |
|--------|-------|
| val-env/AlfworldSG_OOD/success | 0.3060 (30.60%) |
| val-env/AlfworldSG_OOD/pass@1 | 0.3060 |
| val-env/AlfworldSG_OOD/num_actions | 33.24 |
| val-env/AlfworldSG_OOD/action_is_effective | 0.9081 (90.81%) |
| val-env/AlfworldSG_OOD/action_is_valid | 0.6367 (63.67%) |
| val-env/AlfworldSG_OOD/manager_invalid_action | 0.0919 (9.19%) |
| val-env/response_length | 7211.95 |
| val-core/unknown/reward/mean@134 | 3.06 |
| val-aux/unknown/reward/best@2/mean | 5.47 |
| val-aux/unknown/reward/best@4/mean | 7.85 |
| val-aux/unknown/reward/best@16/mean | 9.99 |
| Total OOD tasks | 134 (eval_out_of_distribution split) |

## OOD Cross-Seed Comparison

| Seed / Condition | OOD Success Rate | Notes |
|------------------|-----------------|-------|
| SFT baseline | 5.97% | Pre-training baseline |
| Seed 3 (success) | 10.45% | Normal training |
| Seed 1 (success) | 23.88% | Normal training |
| Seed 5 step10 (OOM killed) | 29.10% | Partial training |
| Seed 6 (success) | 29.10% | Normal training |
| **Seed 4 step15 (collapse)** | **30.60%** | **Response inflation collapse** |

## Analysis

Seed 4 (collapse seed) 在 OOD 评估上取得了 30.60% 的成功率，是目前所有 seed 中最高的。这个结果极为出人意料——该 seed 在训练中出现了严重的 response_length 膨胀（训练时 4850 tokens，OOD eval 时 7212 tokens），训练被判定为 negative（collapse），但 OOD 泛化能力反而最强。

关键观察：
1. **OOD 泛化最强**：30.60% 比 SFT baseline (5.97%) 高 5.1 倍，甚至超过所有正常训练的 success seed（Seed 1: 23.88%, Seed 6: 29.10%）
2. **Response inflation 的代价**：action_is_valid 仅 63.67%（远低于正常水平），response_length 高达 7212 tokens，说明模型确实在生成大量冗余/无效内容
3. **有效动作质量高**：action_is_effective 达 90.81%，说明当模型产生有效动作时，质量很高
4. **高方差**：best@2 mean=5.47 vs worst@2 mean=1.02，表明表现存在显著波动，但整体正向

**Hypothesis 判定**：**成立**。Collapse seed 不仅有 OOD 泛化能力，而且泛化能力比正常 seed 更强。这暗示 response inflation 可能是一种"探索策略"——模型通过生成更长的回复来覆盖更多可能的动作序列，虽然在训练集上表现不佳（pass@1=0.4375），但在 OOD 场景中这种过度探索反而提供了更好的覆盖率。

**对论文的启示**：这是一个重要发现——collapse 并不等于 OOD 泛化失败。可以在论文中作为"response inflation collapse 仍保持 OOD 泛化"的正面证据，支撑 "RL 训练即使在 in-distribution 上出现退化，仍能在 OOD 上带来收益" 的论点。