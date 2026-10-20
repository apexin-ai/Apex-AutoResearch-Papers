# research cmd format

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_cmd_format_20260528T192647_result.json`
- **Structured JSON:** [`ec5b836b6f494ad629fa.json`](../../sessions/ec/ec5b836b6f494ad629fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the full picture. Here's the complete summary:

---

## 完整训练命令格式

### 基础模板（来自 `scripts/run_occ_detach.sh` + `cutoff_experiments.sh`）

```bash
CUDA_VISIBLE_DEVICES={GPU} bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && \
WANDB_MODE=disabled MUJOCO_GL=egl torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py \
  --vla_path /root/autodl-tmp/models/openvla-7b \
  --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ \
  --dataset_name libero_spatial_no_noops \
  --use_l1_regression True --use_diffusion False --use_film False \
  --num_images_in_input 2 --use_proprio True --batch_size 8 \
  --learning_rate 5e-4 --num_steps_before_decay 100000 --max_steps 50005 \
  --save_freq 10000 --image_aug True --lora_rank 32 \
  --run_root_dir /root/autodl-tmp/checkpoints/{EXP_NAME} --seed {SEED}"
```

### 所有 CLI 参数（来自 `FinetuneConfig` dataclass）

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| **必需/常用** | | | |
| `--vla_path` | str | `openvla/openvla-7b` | 模型路径 |
| `--data_root_dir` | Path | `datasets/rlds` | RLDS 数据集根目录 |
| `--dataset_name` | str | `aloha_scoop_x_into_bowl` | 数据集名（`libero_spatial_no_noops` / `libero_object_no_noops`） |
| `--run_root_dir` | Path | `runs` | 输出目录 |
| `--seed` | int | 7 | 随机种子 |
| **算法/架构** | | | |
| `--use_l1_regression` | bool | True | L1 回归 action head |
| `--use_diffusion` | bool | False | 扩散 action head |
| `--use_film` | bool | False | FiLM 语言→视觉注入 |
| `--num_images_in_input` | int | 1 | 输入图片数 |
| `--use_proprio` | bool | False | 包含 proprio state |
| **OCC Head** | | | |
| `--use_occ_head` | bool | False | 启用 BEV occ head |
| `--occ_data_dir` | str | `""` | occ 标签 HDF5 路径 |
| `--occ_loss_weight` | float | 0.01 | occ loss 初始权重 |
| `--occ_loss_decay_steps` | float | 50000 | 指数衰减步数 |
| `--occ_loss_cutoff_step` | int | 0 | cutoff 步数（0=不截断） |
| `--occ_loss_cutoff_mode` | str | `"after"` | `"after"` / `"before"` |
| `--clean_cutoff` | bool | False | cutoff 后跳过 aux forward |
| `--occ_detach` | bool | False | 是否 detach 视觉特征 |
| `--occ_norm_type` | str | `"bn"` | `"bn"` (BatchNorm) / `"ln"` (LayerNorm) |
| `--occ_resolution` | int | 64 | BEV 网格分辨率 |
| `--random_occ` | bool | False | 随机打乱 occ 标签 |
| `--occ_bn_eval` | bool | False | BN 保持 eval 模式 |
| **Depth Head** | | | |
| `--use_depth_head` | bool | False | 启用 depth head |
| `--depth_data_dir` | str | `""` | depth GT 路径 |
| `--depth_loss_weight` | float | 0.01 | depth loss 权重 |
| `--depth_loss_decay_steps` | float | 20000 | |
| `--depth_loss_cutoff_step` | int | 0 | |
| `--depth_detach` | bool | False | |
| `--depth_resolution` | int | 64 | |
| **训练配置** | | | |
| `--batch_size` | int | 8 | per-GPU batch size |
| `--learning_rate` | float | 5e-4 | |
| `--lr_warmup_steps` | int | 0 | |
| `--num_steps_before_decay` | int | 100000 | LR 衰减前步数 |
| `--grad_accumulation_steps` | int | 1 | |
| `--max_steps` | int | 200000 | |
| `--save_freq` | int | 10000 | checkpoint 保存频率 |
| `--save_latest_checkpoint_only` | bool | False | |
| `--resume` | bool | False | 从 checkpoint 恢复 |
| `--resume_step` | int | None | 恢复的步数 |
| `--image_aug` | bool | True | 图像增广 |
| **LoRA** | | | |
| `--use_lora` | bool | True | |
| `--lora_rank` | int | 32 | |
| `--lora_dropout` | float | 0.0 | |
| `--merge_lora_during_training` | bool | True | |
| **Logging** | | | |
| `--wandb_entity` | str | | |
| `--wandb_project` | str | | |
| `--wandb_log_freq` | int | 10 | |

### 各实验变体的关键差异参数

| 实验类型 | 关键参数 |
|----------|----------|
| **vanilla** | 不加 `--use_occ_head`（默认 False） |
| **full_occ_bn** | `--use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach false --occ_norm_type bn` |
| **full_occ_ln** | `--use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach false --occ_norm_type ln` |
| **detach_bn** | `--use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach true --occ_norm_type bn` |
| **detach_ln** | `--use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach true --occ_norm_type ln` |
| **cutoff_25K** | full_occ + `--occ_loss_cutoff_step 25000` |
| **random_occ** | full_occ + `--random_occ True` |
| **_object** 变体 | `--dataset_name libero_object_no_noops` |

### 固定路径

- 模型: `/root/autodl-tmp/models/openvla-7b`
- 数据集: `/root/autodl-tmp/data/modified_libero_rlds/`
- OCC 标签: `/root/occsafe_vla/occ_data`
- 输出: `/root/autodl-tmp/checkpoints/{exp_name}`

### 环境变量

- `WANDB_MODE=disabled` — 禁用 W&B
- `MUJOCO_GL=egl` — MuJoCo 渲染后端
- `CUDA_VISIBLE_DEVICES={GPU}` — GPU 选择

### 磁盘状态 (westd-34685)

350G 总量, 257G 已用, **94G 可用** (74%)

---
