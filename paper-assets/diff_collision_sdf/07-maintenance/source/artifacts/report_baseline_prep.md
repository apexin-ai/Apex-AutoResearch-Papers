# Baseline Training & Evaluation Script Preparation Report

## 产出文件

| 文件 | 服务器路径 | 状态 |
|------|-----------|------|
| 训练脚本 | `/root/colliforce-vla/scripts/train_baseline.py` | ✅ 已部署 |
| 评估脚本 | `/root/colliforce-vla/scripts/eval_safelibero.py` | ✅ 已部署 |

## openpi Fine-tune 配置摘要

基于 `pi0_libero_low_mem_finetune` 配置，关键参数：

| 参数 | 值 | 说明 |
|------|------|------|
| Model | Pi0Config | LoRA fine-tune |
| paligemma_variant | gemma_2b_lora | VLM backbone, LoRA |
| action_expert_variant | gemma_300m_lora | Action expert, LoRA (rank=32) |
| action_dim | 7 | LIBERO: 6 joints + 1 gripper |
| action_horizon | 50 | Action chunk length |
| Base weights | pi0_base | `gs://openpi-assets/checkpoints/pi0_base/params` |
| Optimizer | AdamW | b1=0.9, b2=0.95, grad_clip=1.0 |
| LR schedule | CosineDecay | peak=2.5e-5, warmup=1000, decay=30000 |
| batch_size | 32 | 可根据 VRAM 调整 |
| num_train_steps | 30,000 | 约 ~1000 epochs (取决于数据量) |
| freeze_filter | LoRA freeze | 冻结非 LoRA 参数 |
| ema_decay | None | LoRA 不用 EMA |
| extra_delta_transform | True | LIBERO 专用 delta action 转换 |

## 训练脚本功能 (train_baseline.py)

- 支持单 GPU 和多 GPU (torchrun DDP)
- `--scene` 选择 MVP 场景 (spatial_bowl / object_pudding)
- `--dry_run` 快速 2-step 验证（无 wandb）
- `--resume` 从上次 checkpoint 恢复
- Checkpoint 保存到 `/root/autodl-tmp/checkpoints/baseline_{scene}_{seed}/`
- WandB logging（project: colliforce-vla）
- 自动检查数据和权重路径，缺失时报错退出

## 评估脚本功能 (eval_safelibero.py)

- 支持所有 4 个 SafeLIBERO suite (spatial/object/goal/long)
- 支持 Safety Level I 和 II
- 碰撞检测: 6 个 obstacle 位移 > 0.001m 阈值
  - moka_pot_obstacle, white_storage_box_obstacle, milk_obstacle
  - wine_bottle_obstacle, red_coffee_mug_obstacle, yellow_book_obstacle
- 输出指标:
  - **CAR** (Collision Avoidance Rate): 无碰撞 episodes / 总 episodes
  - **TSR** (Task Success Rate): 成功完成 / 总 episodes
  - **Trajectory Smoothness**: mean jerk (三阶导数)
  - **Max Displacement**: 最大障碍物位移
- 结果保存为 JSON: `/root/autodl-tmp/eval_results/eval_{suite}_{task}_level{level}_{ckpt}_seed{seed}.json`
- `MUJOCO_GL=egl` 环境变量自动设置

## 前置条件状态

| 前置条件 | 状态 | 说明 |
|----------|------|------|
| openpi 代码 | ✅ 就绪 | `/root/colliforce-vla/openpi/` |
| openpi import | ✅ 就绪 | 已修复 datetime.UTC 兼容性, 安装缺失依赖 |
| SafeLIBERO 环境 | ✅ 就绪 | benchmark import 和 init_states 文件正常 |
| SafeLIBERO init_states | ✅ 就绪 | Level I 和 II 都有 |
| 训练数据 | ❌ 未就绪 | `/root/autodl-tmp/colliforce_data/` 不存在 (Worker 2) |
| Base weights | ❌ 未就绪 | `/root/autodl-tmp/openpi_weights/` 不存在 (Worker 1) |
| Checkpoint 目录 | ❌ 未就绪 | 需要先完成训练 |

## Dry-run 状态

**无法执行 dry-run**：训练数据和 pi0_base 权重均未就绪。

训练 dry-run 需要：
1. Worker 1 下载 pi0_base 权重到 `/root/autodl-tmp/openpi_weights/pi0_base/params`
2. Worker 2 生成训练数据到 `/root/autodl-tmp/colliforce_data/safelibero_spatial/`

评估 dry-run 需要：
1. 训练完成后的 checkpoint，或 default openpi LIBERO policy

## 环境修复记录

以下依赖在 conda env `libero` (Python 3.10) 中补装：
- augmax, docstring_parser, typeguard, toolz, tqdm-loggable, polars, openpi-client
- 修复 `openpi/src/openpi/shared/download.py`: `datetime.UTC` → `datetime.timezone.utc`
- numpy 重装 (版本检测异常修复)
- 创建 `~/.safelibero/config.yaml` 配置 SafeLIBERO 路径

## 预估训练时间和显存

| 配置 | 显存 (估算) | 训练时间 (估算) |
|------|-----------|---------------|
| LoRA bs=32, 单卡 RTX PRO 6000 (94GB) | ~30-40 GB | ~2-3h (30k steps) |
| LoRA bs=32, 4卡 DDP | ~30-40 GB/卡 | ~40-60min |
| Full finetune bs=32, 单卡 | ~70-80 GB | ~3-4h |

## 后续步骤

1. 等 Worker 1 完成权重下载和 openpi 环境配置
2. 等 Worker 2 完成训练数据生成
3. 运行 dry-run 验证: `python scripts/train_baseline.py --scene spatial_bowl --dry_run`
4. 启动正式训练: `torchrun --standalone --nnodes=1 --nproc_per_node=4 scripts/train_baseline.py --scene spatial_bowl --seed 0`
5. 训练完成后运行评估: `MUJOCO_GL=egl python scripts/eval_safelibero.py --checkpoint <ckpt_path> --config_name baseline_spatial_bowl --suite safelibero_spatial --task_id 0 --safety_level II`
