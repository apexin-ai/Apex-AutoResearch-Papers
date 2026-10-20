# n=5 Expansion — Eval + Launch Commands (westd-34685)

## Phase 1: Eval (4 finishing experiments)

Pre-condition: vanilla_v2_s1, vanilla_v2_s2, detach_ln_s3, cutoff_25k_s1_v2 训练完成 (~May 27 06:20 UTC)

### Eval 1: vanilla_v2_s1 (cuda:0)
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python vla-scripts/safelibero_eval.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/vanilla_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--vanilla_v2_s1--50000_chkpt --num_rollouts 50 --seed 42 --task_suite_name libero_spatial"
```

### Eval 2: vanilla_v2_s2 (cuda:1)
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python vla-scripts/safelibero_eval.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/vanilla_v2_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--vanilla_v2_s2--50000_chkpt --num_rollouts 50 --seed 42 --task_suite_name libero_spatial"
```

### Eval 3: detach_ln_s3 (cuda:2)
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=2 python vla-scripts/safelibero_eval.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_ln_s3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_s3--50000_chkpt --num_rollouts 50 --seed 42 --task_suite_name libero_spatial"
```

### Eval 4: cutoff_25k_s1_v2 (cuda:3)
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=3 python vla-scripts/safelibero_eval.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/cutoff_25k_s1_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--cutoff_25k_s1_v2--50000_chkpt --num_rollouts 50 --seed 42 --task_suite_name libero_spatial"
```

---

## Phase 2: n=5 Training (seed=46, 2×2 factorial expansion)

Pre-condition: Phase 1 eval 全部完成, GPU 空闲

### Hypothesis
n=5 统计扩展：每个 2×2 factorial cell 增加第 5 个种子 (seed=46)，增强效应量估计的可靠性，使 gradient_flow × norm_type 交互效应的统计检验具备更高检验力 (power)。

### Training 1: detach_ln_s4 → cuda:0 (Cell 4: Grad OFF + LN)
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES=0 torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach true --occ_norm_type ln --run_root_dir /root/autodl-tmp/checkpoints/detach_ln_s4 --seed 46 --run_id_note detach_ln_s4"
```

### Training 2: ablation_occ_detach_s4 → cuda:1 (Cell 3: Grad OFF + BN)
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES=1 torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach true --run_root_dir /root/autodl-tmp/checkpoints/ablation_occ_detach_s4 --seed 46 --run_id_note ablation_occ_detach_s4"
```

### Training 3: full_occ_ln_s4 → cuda:2 (Cell 2: Grad ON + LN)
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES=2 torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach false --occ_norm_type ln --run_root_dir /root/autodl-tmp/checkpoints/full_occ_ln_s4 --seed 46 --run_id_note full_occ_ln_s4"
```

### Training 4: mvp_occ_s4 → cuda:3 (Cell 1: Grad ON + BN)
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES=3 torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach false --run_root_dir /root/autodl-tmp/checkpoints/mvp_occ_s4 --seed 46 --run_id_note mvp_occ_s4"
```

---

## GPU 分配表

### Phase 1: Eval
| cuda | exp_id | 类型 | MUJOCO_EGL_DEVICE_ID |
|------|--------|------|---------------------|
| 0 | vanilla_v2_s1 | Vanilla (seed=43) | 0 |
| 1 | vanilla_v2_s2 | Vanilla (seed=44) | 1 |
| 2 | detach_ln_s3 | Detach LN (seed=45) | 2 |
| 3 | cutoff_25k_s1_v2 | Cutoff 25k (seed=43) | 3 |

### Phase 2: Training
| cuda | exp_id | Cell | occ_detach | occ_norm_type | seed |
|------|--------|------|------------|---------------|------|
| 0 | detach_ln_s4 | 4 (Grad OFF + LN) | true | ln | 46 |
| 1 | ablation_occ_detach_s4 | 3 (Grad OFF + BN) | true | (default BN) | 46 |
| 2 | full_occ_ln_s4 | 2 (Grad ON + LN) | false | ln | 46 |
| 3 | mvp_occ_s4 | 1 (Grad ON + BN) | false | (default BN) | 46 |

---

## 前置条件检查清单

### Phase 1 启动前
- [ ] 确认 4 个训练实验全部完成（检查进程状态 + 日志中出现 step 50005）
- [ ] 确认 50000_chkpt 目录存在于各 checkpoint_path
- [ ] 确认 GPU 空闲（`nvidia-smi` 无训练进程）

### Phase 2 启动前
- [ ] Phase 1 eval 全部完成（每个 ~45-50min）
- [ ] 确认 GPU 空闲
- [ ] 磁盘空间检查：`df -h /root/autodl-tmp/`（每个实验 ~15GB checkpoint，共需 ~60GB）
- [ ] 确认 `/root/autodl-tmp/data/modified_libero_rlds/` 数据目录存在
- [ ] 确认 `/root/occsafe_vla/occ_data` 目录存在

### 时间估算
- Eval: 4 并行, ~50min/each → Phase 1 ~50min
- Training: 4 并行, ~11h/each → Phase 2 完成 ~May 27 17:30 UTC
- DDL: 2026-05-28 12:00 UTC — 留有 ~18.5h buffer

## 注意事项
- eval 脚本路径请实际确认：任务指定 `safelibero_eval.py`，但 registry 历史记录显示 `evaluate_safelibero.py`，以实际存在的为准
- 34685 环境需 `conda activate occsafe`，不是 base
- 训练命令已包含 `CUDA_VISIBLE_DEVICES` 确保 GPU 绑定
