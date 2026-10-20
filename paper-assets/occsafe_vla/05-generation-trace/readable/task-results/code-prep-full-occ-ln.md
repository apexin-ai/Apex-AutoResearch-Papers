# code prep full occ ln

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep_full_occ_ln_20260524T083855_result.json`
- **Structured JSON:** [`498ecbf3c00f1b02f0aa.json`](../../sessions/49/498ecbf3c00f1b02f0aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### 代码确认

- **LN 控制参数**: `--occ_norm_type ln`（finetune.py:98，默认 `"bn"`）
- **实现方式**: `nn.GroupNorm(1, channels)`（occ_head.py:23），等价于 LayerNorm
- **与 detach 独立**: `occ_norm_type` 和 `occ_detach` 是完全独立的参数，在代码中无任何耦合

### Dry-run 验证（`--occ_detach false --occ_norm_type ln`）

| 指标 | 结果 |
|------|------|
| trainable params | **279,977,608** ✅（与 detach_ln 一致）|
| occ_head params | 1,213,313 |
| 初始 occ_loss | 0.1192 |
| 训练速度 | ~1.2-1.6 s/it |
| 梯度流 | 正常（无 detach）|
| 状态 | 5 步完成，无错误 |

### 3 个训练命令

**Seed 42 → westd-10894 cuda:1**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES=1 MASTER_PORT=29506 WANDB_MODE=disabled torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach false --occ_norm_type ln --run_root_dir /root/autodl-tmp/checkpoints/full_occ_ln_s0 --seed 42
```

**Seed 43 → westd-10894 cuda:2**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES=2 MASTER_PORT=29507 WANDB_MODE=disabled torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach false --occ_norm_type ln --run_root_dir /root/autodl-tmp/checkpoints/full_occ_ln_s1 --seed 43
```

**Seed 44 → westd-10894 cuda:3**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES=3 MASTER_PORT=29508 WANDB_MODE=disabled torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach false --occ_norm_type ln --run_root_dir /root/autodl-tmp/checkpoints/full_occ_ln_s2 --seed 44
```

与 detach_ln 命令的唯一差异：`--occ_detach false`（detach_ln 用 `true`）+ checkpoint 目录名 `full_occ_ln_s{N}`。

---
