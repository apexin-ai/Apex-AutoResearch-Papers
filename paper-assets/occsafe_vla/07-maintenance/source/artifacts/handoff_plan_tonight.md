# 今晚接力计划 — May 26 22:30 - May 27 02:00 UTC

## 阶段 1: 34685 训练完成 (~22:30 UTC)

### GPU 分配 (4 GPU, 5 任务 → 3 eval + 1 training 先行, 1 eval 排队)
| cuda | 任务 | 类型 | 优先级 |
|------|------|------|--------|
| 0 | vanilla_v2_s1 eval | eval | P0 (Vanilla baseline) |
| 1 | vanilla_v2_s2 eval | eval | P0 (Vanilla baseline) |
| 2 | detach_ln_s3 eval | eval | P0 (Cell 4 v2) |
| 3 | detach_ln_v2_s1 training | train | P0 (Cell 4 关键路径) |

### 排队: cutoff_25k_s1_v2 eval
- 等任一 eval 完成后 (~23:20) 在释放的 GPU 上启动
- 优先级 P1 (dose-response, 非 factorial 核心)

### detach_ln_v2_s1 训练命令 (34685 cuda:3)
```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach true --occ_norm_type ln --run_root_dir /root/autodl-tmp/checkpoints/detach_ln_v2_s1 --seed 43 --run_id_note detach_ln_v2_s1"
```

### 3 eval 命令 (34685)
```bash
# vanilla_v2_s1 eval → cuda:0
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python3 vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/vanilla_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--vanilla_v2_s1--50000_chkpt --task_suite_name libero_spatial --num_rollouts 50 --seed 42

# vanilla_v2_s2 eval → cuda:1
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python3 vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/vanilla_v2_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--vanilla_v2_s2--50000_chkpt --task_suite_name libero_spatial --num_rollouts 50 --seed 42

# detach_ln_s3 eval → cuda:2
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=2 python3 vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_ln_s3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_s3--50000_chkpt --task_suite_name libero_spatial --num_rollouts 50 --seed 42
```

### cutoff_25k_s1_v2 eval (排队, ~23:20 启动)
```bash
# cutoff_25k_s1_v2 eval → 等 eval 释放的 GPU (0/1/2 之一)
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES={freed_gpu} MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID={freed_gpu} python3 vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/cutoff_25k_s1_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--cutoff_25k_s1_v2--50000_chkpt --task_suite_name libero_spatial --num_rollouts 50 --seed 42
```

## 阶段 2: 10894 完成

### reverse_cutoff_s2_v2 完成 (~22:54 UTC) → eval on cuda:0
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python3 vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/reverse_cutoff_s2_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--reverse_cutoff_s2_v2--50000_chkpt --task_suite_name libero_spatial --num_rollouts 50 --seed 42
```

### full_occ_ln_v2_s0/s1, detach_ln_v2_s0 完成 (~01:50 UTC) → 3 eval
使用 batch_eval.sh:
```bash
bash /root/occsafe_vla/scripts/batch_eval.sh full_occ_ln_v2_s0:1 full_occ_ln_v2_s1:2 detach_ln_v2_s0:3
```

## 阶段 3: 34685 eval 全部完成 (~23:20 UTC) → n=5 expansion
cutoff eval 完成后 (~00:10 UTC)，3 个空闲 GPU 可启动 n=5 expansion（cuda:3 被 detach_ln_v2_s1 占用）:
- cuda:0: mvp_occ_s4
- cuda:1: full_occ_ln_s4
- cuda:2: ablation_occ_detach_s4
- detach_ln_s4 等 detach_ln_v2_s1 完成后启动
