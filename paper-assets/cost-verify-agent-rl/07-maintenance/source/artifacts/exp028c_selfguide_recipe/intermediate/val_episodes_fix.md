# exp028c Val Episodes: 16 → 140

## 修改

文件: `RAGEN/config/_alfworld_exp028c_selfguide_recipe.yaml`

- `es_manager.val.env_groups`: 16 → 140
- `es_manager.val.env_configs.n_groups`: [16] → [140]
- `group_size` 和 `validation_steps` 不变（均为 1）
- 总 val episodes: 16 → 140，分辨率 6.25% → 0.71%，对齐 Self-Guide 论文

## 对当前训练的影响

**无影响。** Hydra 启动时一次性加载配置到内存，运行中不重新读取 YAML。PID 824675 继续以 16 episodes 评估。

## 生效方式

下次重启实验时自动生效。

## 注意

eval 耗时约增加 ~9x（16→140 episodes）。
