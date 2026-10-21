# 实验 8b_v9d_ood_eval 失败诊断

## Traceback

```
File "/root/autodl-tmp/cost-verify-agent-rl/RAGEN/train.py", line 178, in main
    config = add_dependency_and_validate_config(config)
File "/root/autodl-tmp/cost-verify-agent-rl/RAGEN/train.py", line 163, in add_dependency_and_validate_config
    assert config.es_manager.train.env_groups * config.es_manager.train.group_size * effective_ratio >= config.ppo_mini_batch_size
AssertionError: env_groups * group_size * effective_ratio (2.0) must be greater than or equal to ppo_mini_batch_size (4).
```

## 根因分析

**类型**: 配置问题（train batch size 约束与 val-only 模式冲突）

OOD eval 配置 (`_alfworld_8b_v9d_ood_eval.yaml`) 中：
- `es_manager.train.env_groups = 1`
- `es_manager.train.group_size = 2`
- `ppo_mini_batch_size = 4`

`base.yaml` 中 `rollout_filter_strategy = "top_p"`, `rollout_filter_value = 1.0`，OOD eval config 未覆盖。

代码计算 `effective_ratio`:
```python
# train.py line 155-156
rollout_filter_strategy = getattr(..., "rollout_filter_strategy", "top_p")
rollout_filter_value = getattr(..., "rollout_filter_value", 0.25)
# 但 base.yaml 设了 1.0，所以实际 effective_ratio = 1.0
```

最终: `1 * 2 * 1.0 = 2.0 < 4` → assertion 失败。

**本质问题**: 这是 val-only 评估（`val_only: True`），train 参数不参与实际计算。但 `add_dependency_and_validate_config()` 不区分 val-only 模式，仍然校验 train batch size 约束。

## 修复方案

### 方案 A: 改配置（最快，推荐用于本次重跑）

在 `_alfworld_8b_v9d_ood_eval.yaml` 中将 `ppo_mini_batch_size` 降到 ≤ 2:

```yaml
ppo_mini_batch_size: 2
```

或增大 train env_groups 使乘积 ≥ 4:

```yaml
es_manager:
  train:
    env_groups: 2
    group_size: 2
```

### 方案 B: 改代码（更彻底）

在 `train.py` 的 `add_dependency_and_validate_config()` 中，当 `config.trainer.val_only == True` 时跳过 train batch size 相关 assertion。

## 推荐

方案 A（`ppo_mini_batch_size: 2`）改动最小且 val-only 模式下该值无实际影响。后续可考虑方案 B 避免类似问题复现。
