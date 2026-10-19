# Spatial Bowl A1 SDF 训练准备验证报告

**日期**: 2026-05-23

## 1. 脚本支持状态：已支持

`scripts/train_a1_sdf_aux_pi05.py` 的 `SCENE_CONFIG` 已包含 `spatial_bowl`：

```python
"spatial_bowl": {
    "description": "SafeLIBERO Spatial: bowl between plate and ramekin",
    "data_subdir": "safelibero_spatial",
    "sdf_gt": "/root/colliforce-vla/data/sdf_gt_spatial_bowl.npz",
    "assets_dir": "/root/colliforce-vla/assets/baseline_spatial_bowl",
}
```

无需修改脚本。

## 2. SDF GT 数据：两台服务器均就绪

| 服务器 | 路径 | 大小 | 日期 |
|--------|------|------|------|
| westd-45947 | `/root/colliforce-vla/data/sdf_gt_spatial_bowl.npz` | 114,658 bytes | May 20 |
| westd-35807 | `/root/colliforce-vla/data/sdf_gt_spatial_bowl.npz` | 114,658 bytes | May 20 |

数据内容：`query_points=(4076, 3)`, `sdf_values=(4076,)` — 4076 个查询点的 SDF 值。

## 3. 训练数据：两台服务器均就绪

| 服务器 | 路径 | 大小 | Episodes |
|--------|------|------|----------|
| westd-45947 | `/root/autodl-tmp/colliforce_data/safelibero_spatial/` | 434MB | 50 (episode_000000–000049) |
| westd-35807 | `/root/autodl-tmp/colliforce_data/safelibero_spatial/` | 433MB | 50 |

Meta 文件完整：info.json, stats.json, tasks.parquet, tasks.jsonl, episodes.jsonl, episodes_stats.jsonl

## 4. Eval Assets：就绪

- `assets/baseline_spatial_bowl/safelibero_spatial/norm_stats.json` (两台服务器均有)
- 还存在 `assets/a1_sdf_spatial_bowl/` 和 `assets/a3_grad_refine_spatial_bowl/`（历史实验资产）

## 5. 启动命令模板

```bash
# Seed 0
WANDB_MODE=offline python scripts/train_a1_sdf_aux_pi05.py \
  --scene spatial_bowl --seed 0 --gpu {GPU} --batch_size 32 \
  --num_train_steps 30000 --lambda_sdf {LAMBDA} --lambda_ee 0.01 \
  --lr 2.5e-5 --save_interval 2000

# Seed 42
WANDB_MODE=offline python scripts/train_a1_sdf_aux_pi05.py \
  --scene spatial_bowl --seed 42 --gpu {GPU} --batch_size 32 \
  --num_train_steps 30000 --lambda_sdf {LAMBDA} --lambda_ee 0.01 \
  --lr 2.5e-5 --save_interval 2000
```

- `{LAMBDA}`: 待 object_pudding 结果确定后填入
- `{GPU}`: 待 GPU 空闲后分配（白名单：westd-35807:cuda:0-3, westd-45947:cuda:0-1）
- 约束 C002：预估训练 <24h，可用 submit_training_job；若超 24h 需用 tmux

## 6. 缺失项

无。代码、SDF GT、训练数据、eval assets 全部就绪，等 GPU 释放即可启动。
