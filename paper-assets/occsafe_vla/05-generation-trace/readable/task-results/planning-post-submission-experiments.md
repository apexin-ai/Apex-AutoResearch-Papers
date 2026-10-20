# planning post submission experiments

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_planning_post-submission-experiments_20260528T175139_result.json`
- **Structured JSON:** [`c744ef266c94aa97e9c1.json`](../../sessions/c7/c744ef266c94aa97e9c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I now have all the information needed. Here's the complete plan.

---

## 实验 1: RD2-N1 — 每个 cell 扩充到 n≥5

**代码修改**: 不需要

**已用 seeds（v1+v2 合计）**:
| Cell | 已用 seeds |
|------|-----------|
| Cell 1 (Full OCC BN) | 42, 43, 44, 45, 46 |
| Cell 2 (Full OCC LN) | 42, 43, 44, 45, 46, 47 |
| Cell 3 (Detach BN) | 42, 43, 44, 45, 46 |
| Cell 4 (Detach LN) | 42, 43, 44, 45, 46 |

**新 seeds**: 从 48 起分配，避免任何已用值。

**训练命令**:

**Cell 1 — Full OCC BN, +2 seeds (48, 49)**:
```bash
# seed 48
CUDA_VISIBLE_DEVICES=0 bash -c "export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach false --occ_norm_type bn --seed 48 --run_root_dir /root/autodl-tmp/checkpoints/full_occ_bn_v2_s48 --run_id_note full_occ_bn_v2_s48"

# seed 49
CUDA_VISIBLE_DEVICES=1 bash -c "export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach false --occ_norm_type bn --seed 49 --run_root_dir /root/autodl-tmp/checkpoints/full_occ_bn_v2_s49 --run_id_note full_occ_bn_v2_s49"
```

**Cell 2 — Full OCC LN, +1 seed (48)**:
```bash
CUDA_VISIBLE_DEVICES=2 bash -c "export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach false --occ_norm_type ln --seed 48 --run_root_dir /root/autodl-tmp/checkpoints/full_occ_ln_v2_s48 --run_id_note full_occ_ln_v2_s48"
```

**Cell 3 — Detach BN, +1 seed (48)**:
```bash
CUDA_VISIBLE_DEVICES=3 bash -c "export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach true --occ_norm_type bn --seed 48 --run_root_dir /root/autodl-tmp/checkpoints/detach_bn_v2_s48 --run_id_note detach_bn_v2_s48"
```

**Cell 4 — Detach LN, +2 seeds (48, 49)**:
```bash
# seed 48
CUDA_VISIBLE_DEVICES=0 bash -c "export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach true --occ_norm_type ln --seed 48 --run_root_dir /root/autodl-tmp/checkpoints/detach_ln_v2_s48 --run_id_note detach_ln_v2_s48"

# seed 49
CUDA_VISIBLE_DEVICES=1 bash -c "export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach true --occ_norm_type ln --seed 49 --run_root_dir /root/autodl-tmp/checkpoints/detach_ln_v2_s49 --run_id_note detach_ln_v2_s49"
```

**GPU 时间**: 每个 run ~14.5h, 共 6 runs = ~87h 单卡时间。8 卡并行可在 ~2 波完成（波1: 6 runs 占 6 卡，~15h; 评估 ~40min/run 串行在同卡）。  
**前置条件**: 无。可直接启动。

---

## 实验 2: RD2-N2 — v2 Random OCC (3 seeds)

**代码修改**: **需要**

v2 codebase 没有 `random_occ` flag（v1 有但已移除）。需修改两个文件：

**文件 1: `vla-scripts/finetune.py`**

(a) FinetuneConfig 添加 flag（~line 99 后）:
```python
random_occ: bool = False                         # If True, randomly permute OCC labels (content irrelevance ablation)
```

(b) 训练循环中，在 OCC loss 计算前 shuffle label（~line 1206 附近，调用 `compute_loss` 时已传入 batch）。最简方案：在 `compute_loss` 函数内部修改。在 `vla-scripts/finetune.py` line 481-490 区域：

```python
# 现有代码 (line 481-489):
if occ_head is not None and "occ_labels" in batch:
    ...
    occ_targets = batch["occ_labels"].to(device_id).float()

# 改为:
if occ_head is not None and "occ_labels" in batch:
    ...
    occ_targets = batch["occ_labels"].to(device_id).float()
    if random_occ:
        # Randomly permute OCC labels across batch (break scene-label correspondence)
        perm = torch.randperm(occ_targets.shape[0])
        occ_targets = occ_targets[perm]
```

需要同步修改 `compute_loss` 函数签名，添加 `random_occ=False` 参数，以及调用处（~line 1208）传入 `random_occ=cfg.random_occ`。

**完整修改清单**:
1. `FinetuneConfig` 加 `random_occ: bool = False` (line ~99)
2. `compute_loss()` 签名加 `random_occ=False` (line ~312)
3. `compute_loss()` 中 OCC loss 部分加 batch permutation (line ~487)
4. 训练循环调用 `compute_loss` 时传入 `random_occ=cfg.random_occ` (line ~1209)

**训练命令** (3 seeds: 48, 49, 50):
```bash
# seed 48
CUDA_VISIBLE_DEVICES=2 bash -c "export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach false --occ_norm_type bn --random_occ True --seed 48 --run_root_dir /root/autodl-tmp/checkpoints/random_occ_v2_s48 --run_id_note random_occ_v2_s48"

# seed 49
CUDA_VISIBLE_DEVICES=3 bash -c "export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach false --occ_norm_type bn --random_occ True --seed 49 --run_root_dir /root/autodl-tmp/checkpoints/random_occ_v2_s49 --run_id_note random_occ_v2_s49"

# seed 50
CUDA_VISIBLE_DEVICES=0 bash -c "export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach false --occ_norm_type bn --random_occ True --seed 50 --run_root_dir /root/autodl-tmp/checkpoints/random_occ_v2_s50 --run_id_note random_occ_v2_s50"
```

**GPU 时间**: 每个 run ~14.5h, 共 3 runs = ~43.5h 单卡时间。  
**前置条件**: 先部署上述 4 处代码修改到两台服务器的 `/root/occsafe_vla/openvla-oft/vla-scripts/finetune.py`。

---

## 实验 3: RD2-W4 — BN eval mode 消融

**关键发现**:

经过代码审查，这个实验存在设计问题：

1. **eval 脚本 (`evaluate_safelibero.py`) 不加载 OCC head** — grep 确认无 `occ_head` 引用
2. **backbone 模型 (ViT + Llama) 没有 BatchNorm 层** — 仅使用 LayerNorm / RMSNorm
3. **BN 只存在于 OCC head 的 decoder** (`occ_head.py` line 23: `nn.BatchNorm2d`)
4. eval 时 `openvla_utils.py` line 299 已调用 `vla.eval()`

**结论**: 在推理时切换 BN eval/train mode 不会改变 CAR，因为 OCC head 根本不参与推理。

**有意义的替代方案 — 训练时 BN eval mode**:

假设: Full OCC BN (CAR=0.725) 低于 Full OCC LN (0.773) 的原因是 batch_size=8 时 BN 的 batch statistics 噪声通过梯度反传污染了 backbone。若训练时冻结 BN 为 eval mode（使用 running stats），梯度信号更稳定，CAR 可能恢复。

**代码修改**: 需要

**文件: `vla-scripts/finetune.py`**

(a) FinetuneConfig 添加（~line 99 后）:
```python
occ_bn_eval: bool = False                        # If True, keep OCC head BN in eval mode during training (use running stats)
```

(b) 训练循环中，每次 forward 前冻结 BN（~line 1200 附近，在 `compute_loss` 调用前）:
```python
if cfg.occ_bn_eval and occ_head is not None:
    for m in occ_head.modules():
        if isinstance(m, torch.nn.BatchNorm2d):
            m.eval()
```

**训练命令** (用 Cell 1 现有 3 个 seed 值对应训练):
```bash
# seed 48 (与 RD2-N1 Cell 1 seed 48 对比)
CUDA_VISIBLE_DEVICES=X bash -c "export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach false --occ_norm_type bn --occ_bn_eval True --seed 48 --run_root_dir /root/autodl-tmp/checkpoints/full_occ_bn_eval_v2_s48 --run_id_note full_occ_bn_eval_v2_s48"
```

**或者（零代码版本）**: 如果不想改代码，可以对已有 Full OCC BN checkpoints 做纯 eval 对比 — 但由于 OCC head 不参与 eval，结果会与已有 eval 完全一致，没有新信息。

**推荐方案**: 将此实验改为 **训练时 BN eval mode 消融**，需 2-3 seeds 的全新训练。若资源紧张可降到 2 seeds。

**GPU 时间**: 2 seeds × ~14.5h = ~29h 单卡时间（如做 3 seeds 则 43.5h）  
**前置条件**: 代码修改部署。如果沿用原始 eval-time 方案，则无需训练，但结果无信息量。

---

## 实验 4: RD3-W3 — λ₀ sweep

**代码修改**: 不需要

`occ_loss_weight` 已是 FinetuneConfig 的命令行参数（`finetune.py` line 92），默认值 0.01。直接通过 `--occ_loss_weight` 传入即可。

衰减公式: `occ_weight(t) = occ_loss_weight × exp(-batch_idx / occ_loss_decay_steps)`, 其中 `occ_loss_decay_steps=50000`（默认值）。

| λ₀ | 配置 | 备注 |
|----|------|------|
| 0.01 | 已有 (Cell 1 Full OCC BN 默认) | 无需额外实验 |
| 0.001 | `--occ_loss_weight 0.001` | 弱 OCC 信号 |
| 0.1 | `--occ_loss_weight 0.1` | 强 OCC 信号 |

**训练命令** (Full OCC BN, 每个 λ₀ 各 2 seeds):

**λ₀=0.001, seeds 48, 49**:
```bash
# λ₀=0.001, seed 48
CUDA_VISIBLE_DEVICES=0 bash -c "export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach false --occ_norm_type bn --occ_loss_weight 0.001 --seed 48 --run_root_dir /root/autodl-tmp/checkpoints/lambda001_bn_v2_s48 --run_id_note lambda001_bn_v2_s48"

# λ₀=0.001, seed 49
CUDA_VISIBLE_DEVICES=1 bash -c "export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach false --occ_norm_type bn --occ_loss_weight 0.001 --seed 49 --run_root_dir /root/autodl-tmp/checkpoints/lambda001_bn_v2_s49 --run_id_note lambda001_bn_v2_s49"
```

**λ₀=0.1, seeds 48, 49**:
```bash
# λ₀=0.1, seed 48
CUDA_VISIBLE_DEVICES=2 bash -c "export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach false --occ_norm_type bn --occ_loss_weight 0.1 --seed 48 --run_root_dir /root/autodl-tmp/checkpoints/lambda01_bn_v2_s48 --run_id_note lambda01_bn_v2_s48"

# λ₀=0.1, seed 49
CUDA_VISIBLE_DEVICES=3 bash -c "export WANDB_MODE=disabled && source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach false --occ_norm_type bn --occ_loss_weight 0.1 --seed 49 --run_root_dir /root/autodl-tmp/checkpoints/lambda01_bn_v2_s49 --run_id_note lambda01_bn_v2_s49"
```

**GPU 时间**: 每个 run ~14.5h, 共 4 runs = ~58h 单卡时间。  
**前置条件**: 无。可直接启动。

---

## 汇总

| 实验 | 训练 runs | Eval runs | 代码改动 | 单卡 GPU 时间 |
|------|-----------|-----------|----------|--------------|
| RD2-N1 (扩充 n≥5) | 6 | 6 | 无 | ~87h |
| RD2-N2 (Random OCC) | 3 | 3 | 需要 (4 处) | ~43.5h |
| RD2-W4 (BN eval mode) | 2-3 | 2-3 | 需要 (2 处) | ~29-43.5h |
| RD3-W3 (λ₀ sweep) | 4 | 4 | 无 | ~58h |
| **合计** | **15-16** | **15-16** | — | **~217-232h** |

**8 卡并行调度方案** (westd-10894 cuda:0-3 + westd-34685 cuda:0-3):

| 波次 | 时长 | westd-34685 (4 卡) | westd-10894 (4 卡) |
|------|------|-------------------|-------------------|
| 波1 | ~15h | RD2-N1 Cell1 s48, Cell1 s49, Cell2 s48, Cell3 s48 | RD2-N1 Cell4 s48, Cell4 s49, RD3-W3 λ001 s48, RD3-W3 λ001 s49 |
| 波2 | ~15h | RD3-W3 λ01 s48, RD3-W3 λ01 s49, RD2-N2 s48, RD2-N2 s49 | RD2-N2 s50, RD2-W4 s48, RD2-W4 s49, (空闲或备用) |

总挂钟时间: ~30h (2 波 × 15h) + eval 时间 (~40min/run × 16 runs ≈ 11h, 可 8 卡并行降到 ~1.5h)。

**注意事项**:
- Full OCC BN 在 westd-10894 历史上有 RAM OOM 问题 (v2_s3 被 OOM kill)，建议 Cell 1 的新 runs 优先放 westd-34685
- RD2-N2 和 RD2-W4 需要先部署代码修改再启动
- 每个 run 完成后需串行跑 eval：`MUJOCO_GL=egl python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint {50000_chkpt_path} --task_suite_name libero_spatial --num_rollouts 50`

---
