# eval-obs-only-object-norm01-seed45-r2 分析

## 实验配置
- Mode: crm_obs_only, Benchmark: object, ε=0.1 (max_correction_norm)
- Seed: 45, n_rollouts: 10, K: 10
- CRM checkpoint: crm_v3_norm/obs_only/crm_best.pt
- 目的: 标准化 seed45 到 n_rollouts=10（原始 seed45 用 n_rollouts=20, SR=14%）

## 结果

**Overall success rate: 17% (17/100)**

### Per-task breakdown

| Task | SR | Successes/Total |
|------|-----|-----------------|
| alphabet_soup | 0% | 0/10 |
| cream_cheese | 10% | 1/10 |
| salad_dressing | 10% | 1/10 |
| bbq_sauce | **40%** | 4/10 |
| ketchup | 10% | 1/10 |
| tomato_sauce | 10% | 1/10 |
| butter | 10% | 1/10 |
| milk | 20% | 2/10 |
| chocolate_pudding | 30% | 3/10 |
| orange_juice | 30% | 3/10 |

## 与其他 seed 对比

| Seed | SR | 备注 |
|------|-----|------|
| seed42 | 19% | |
| seed44 | 16% | |
| **seed45-r2** | **17%** | 本次（标准化 n_rollouts=10）|
| seed45 原始 | 14% | n_rollouts=20，已废弃 |
| seed46-r3 | 18% | |
| seed48 | 18% | |

### 统计汇总（5 seeds, 标准化后）

- Mean: 17.6%
- Range: 16%~19%
- Std: ~1.1%
- 原始含 seed45(14%) 的均值: 17.0%

## 结论

1. 标准化后 seed45 从 14% 升至 17%，与其他 seed (16%~19%) 一致。原始 14% 的偏低可能是 n_rollouts=20 带来的采样差异。
2. 5 seeds 均值从 17.0% 微升至 17.6%，不改变 ε=0.1 配置的统计结论。
3. obs_only CRM ε=0.1 在 object benchmark 上的表现稳定在 ~17-18%，各 seed 方差小。