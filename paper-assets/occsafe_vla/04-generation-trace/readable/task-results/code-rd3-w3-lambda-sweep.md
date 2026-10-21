# code rd3 w3 lambda sweep

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_rd3-w3-lambda-sweep_20260528T223746_result.json`
- **Structured JSON:** [`4558b59cea436db18945.json`](../../sessions/45/4558b59cea436db18945.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有信息已收集完毕。

---

## RD3-W3 λ₀ Sweep 实验配置

### 1. 当前默认值

`occ_loss_weight: float = 0.01` （finetune.py line 92）

### 2. Loss 计算公式

```
occ_weight_now = λ₀ × exp(-batch_idx / occ_loss_decay_steps)
total_loss = action_loss + occ_weight_now × occ_loss
```

其中 `occ_loss_decay_steps=50000`（默认值）。即 λ₀ 是 **初始权重**，实际权重随训练步数指数衰减。

注意：当前 sweep 中不使用 cutoff（`occ_loss_cutoff_step=0`），所以走纯指数衰减分支（line 1182）。

### 3. 实验矩阵

| Run | λ₀ | 条件 | Seed | GPU 分配 |
|-----|-----|------|------|----------|
| lambda_001 | 0.001 | Full OCC BN, no detach | 42 | westd-10894 cuda:0 |
| lambda_01 | 0.01 | Full OCC BN, no detach | 42 | westd-10894 cuda:1 |
| lambda_1 | 0.1 | Full OCC BN, no detach | 42 | westd-10894 cuda:2 |

λ₀=0.01 就是当前默认值（作为 baseline 对照），3 runs 可并行在不同 GPU 上跑。

### 4. 训练命令

```bash
# --- λ₀ = 0.001 ---
CUDA_VISIBLE_DEVICES=0 bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && \
WANDB_MODE=disabled MUJOCO_GL=egl torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py \
  --vla_path /root/autodl-tmp/models/openvla-7b \
  --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ \
  --dataset_name libero_spatial_no_noops \
  --use_l1_regression True --use_diffusion False --use_film False \
  --num_images_in_input 2 --use_proprio True --batch_size 8 \
  --learning_rate 5e-4 --num_steps_before_decay 100000 --max_steps 50005 \
  --save_freq 10000 --image_aug True --lora_rank 32 \
  --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach false --occ_norm_type bn \
  --occ_loss_weight 0.001 \
  --run_root_dir /root/autodl-tmp/checkpoints/lambda_001_s0 --seed 42"

# --- λ₀ = 0.01 (default baseline) ---
CUDA_VISIBLE_DEVICES=1 bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && \
WANDB_MODE=disabled MUJOCO_GL=egl torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py \
  --vla_path /root/autodl-tmp/models/openvla-7b \
  --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ \
  --dataset_name libero_spatial_no_noops \
  --use_l1_regression True --use_diffusion False --use_film False \
  --num_images_in_input 2 --use_proprio True --batch_size 8 \
  --learning_rate 5e-4 --num_steps_before_decay 100000 --max_steps 50005 \
  --save_freq 10000 --image_aug True --lora_rank 32 \
  --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach false --occ_norm_type bn \
  --occ_loss_weight 0.01 \
  --run_root_dir /root/autodl-tmp/checkpoints/lambda_01_s0 --seed 42"

# --- λ₀ = 0.1 ---
CUDA_VISIBLE_DEVICES=2 bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && \
WANDB_MODE=disabled MUJOCO_GL=egl torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py \
  --vla_path /root/autodl-tmp/models/openvla-7b \
  --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ \
  --dataset_name libero_spatial_no_noops \
  --use_l1_regression True --use_diffusion False --use_film False \
  --num_images_in_input 2 --use_proprio True --batch_size 8 \
  --learning_rate 5e-4 --num_steps_before_decay 100000 --max_steps 50005 \
  --save_freq 10000 --image_aug True --lora_rank 32 \
  --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach false --occ_norm_type bn \
  --occ_loss_weight 0.1 \
  --run_root_dir /root/autodl-tmp/checkpoints/lambda_1_s0 --seed 42"
```

### 5. 预期时长

~13h/run × 3 runs **并行** = **~13h 总墙钟时间**（westd-10894 cuda:0/1/2 各跑一个）。

### 6. 代码修改

**不需要任何代码修改。** `occ_loss_weight` 已经是 draccus CLI 参数（line 92），直接通过命令行传不同值即可。没有范围验证限制。

### 7. 注意事项

- λ₀=0.01 run 严格来说和之前的 Full OCC BN 实验是同条件（如果之前有 seed=42 的 50K run，可以直接复用结果，省掉这一个 run）
- 指数衰减意味着实际权重在训练后期很小：λ₀=0.1 在 step 50K 时衰减到 0.1×exp(-50000/50000) ≈ 0.037，λ₀=0.001 衰减到 ~0.00037
- DDL 约束（C003: 今天 20:00 北京时间）下，13h 的训练无法在 DDL 前完成——需要确认是否 DDL 后可以继续

---
