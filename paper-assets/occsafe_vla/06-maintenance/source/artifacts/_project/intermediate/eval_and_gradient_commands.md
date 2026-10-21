# Post-Training Execution Commands

## Eval Pipeline (8 experiments, ~50 min each)

### westd-34685 (4 evals)

**GPU 0 — detach_ln_v2_s1 (Cell 4 v2, seed 43)**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 CUDA_VISIBLE_DEVICES=0 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_ln_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_v2_s1 --num_rollouts 50 --seed 42
```

**GPU 1 — detach_ln_s4 (Cell 4 n=5, seed 46)**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 CUDA_VISIBLE_DEVICES=1 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_ln_s4/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_s4 --num_rollouts 50 --seed 42
```

**GPU 2 — ablation_occ_detach_s4 (Cell 3 n=5, seed 46)**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=2 CUDA_VISIBLE_DEVICES=2 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/ablation_occ_detach_s4/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--ablation_occ_detach_s4 --num_rollouts 50 --seed 42
```

**GPU 3 — mvp_occ_s4 (Cell 1 n=5, seed 46)**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=3 CUDA_VISIBLE_DEVICES=3 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/mvp_occ_s4/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--mvp_occ_s4 --num_rollouts 50 --seed 42
```

### westd-10894 (4 evals)

**GPU 0 — full_occ_ln_v2_s1c (Cell 2 v2, seed 43)**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 CUDA_VISIBLE_DEVICES=0 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/full_occ_ln_v2_s1c/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s1c --num_rollouts 50 --seed 42
```

**GPU 1 — full_occ_ln_v2_s2 (Cell 2 v2, seed 44)**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 CUDA_VISIBLE_DEVICES=1 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/full_occ_ln_v2_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s2 --num_rollouts 50 --seed 42
```

**GPU 2 — detach_ln_v2_s0c (Cell 4 v2, seed 42)**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=2 CUDA_VISIBLE_DEVICES=2 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_ln_v2_s0c/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_v2_s0c --num_rollouts 50 --seed 42
```

**GPU 3 — full_occ_ln_v2_s0d (Cell 2 v2, seed 42)**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=3 CUDA_VISIBLE_DEVICES=3 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/full_occ_ln_v2_s0d/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s0d --num_rollouts 50 --seed 42
```

## Gradient Analysis (5 conditions, ~15-30 min each)

### westd-10894 (2 conditions, GPU 0+1)

**Cell 1: Full OCC + LN (gradient ON)**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && CUDA_VISIBLE_DEVICES=0 python3 /root/occsafe_vla/scripts/run_gradient_analysis_v2.py --checkpoint_dir /root/autodl-tmp/checkpoints/full_occ_ln_s3_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_s3_v2--50000_chkpt --condition_name "Full_OCC_LN_v2" --seed 42 --output_dir /root/occsafe_vla/artifacts/gradient_v2/ --gpu 0
```

**Cell 3: Detach + BN (gradient OFF)**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && CUDA_VISIBLE_DEVICES=1 python3 /root/occsafe_vla/scripts/run_gradient_analysis_v2.py --checkpoint_dir /root/autodl-tmp/checkpoints/ablation_occ_detach_s3_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--ablation_occ_detach_s3_v2--50000_chkpt --condition_name "Detach_BN_v2" --seed 42 --occ_norm bn --output_dir /root/occsafe_vla/artifacts/gradient_v2/ --gpu 0
```

### westd-34685 (3 conditions, GPU 0/1/2)

**Vanilla**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && CUDA_VISIBLE_DEVICES=0 python3 /root/occsafe_vla/scripts/run_gradient_analysis_v2.py --checkpoint_dir /root/autodl-tmp/checkpoints/vanilla_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--vanilla_v2_s1--50000_chkpt --condition_name "Vanilla_v2" --seed 42 --output_dir /root/occsafe_vla/artifacts/gradient_v2/ --gpu 0
```

**Cell 2: Full OCC + BN (gradient ON)**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && CUDA_VISIBLE_DEVICES=1 python3 /root/occsafe_vla/scripts/run_gradient_analysis_v2.py --checkpoint_dir /root/autodl-tmp/checkpoints/full_occ_bn_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_bn_v2_s1--50000_chkpt --condition_name "Full_OCC_BN_v2" --seed 42 --occ_norm bn --output_dir /root/occsafe_vla/artifacts/gradient_v2/ --gpu 0
```

**Cell 4: Detach + BN (gradient OFF)**
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && CUDA_VISIBLE_DEVICES=2 python3 /root/occsafe_vla/scripts/run_gradient_analysis_v2.py --checkpoint_dir /root/autodl-tmp/checkpoints/detach_bn_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_bn_v2_s1--50000_chkpt --condition_name "Detach_BN_v2" --seed 42 --occ_norm bn --output_dir /root/occsafe_vla/artifacts/gradient_v2/ --gpu 0
```

## Execution Order

1. **34685 训练完成 (~12:27-13:21 UTC)** → 立即 4 GPU 并行 eval（~50 min）+ 3 GPU 并行梯度分析（~30 min）
   - 梯度分析用已有的 50K checkpoint（不需等当前训练完成）
   - eval 用当前训练产出的 checkpoint
2. **10894 训练完成 (~13:39-14:21 UTC)** → 立即 4 GPU 并行 eval + 2 GPU 梯度分析
3. **合并梯度分析结果** → scp JSON 到一台机器 → plot_gradient_analysis_v2.py 出图

## Notes
- 梯度分析 checkpoint 已经存在（50K 已完成的旧实验），可以在训练完成前就跑
- ablation_occ_detach_s3_v2 已确认是 BN（Director 确认），命令已加 --occ_norm bn
- 两台服务器 gradient 结果需 scp 合并后出图
