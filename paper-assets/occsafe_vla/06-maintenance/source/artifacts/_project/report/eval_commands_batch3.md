# Eval Commands — Batch 3 (8 experiments, 50r SafeLIBERO)

Generated: 2026-05-26. All from scratch (no resume), checkpoint = `--50000_chkpt`.

Checkpoint path pattern:
```
/root/autodl-tmp/checkpoints/{exp_id}/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--{exp_id}--50000_chkpt
```

---

## westd-10894

### 1. reverse_cutoff_s2_v2_eval
- GPU: cuda:0（训练完成后同卡 eval）
- ETA: ~23:00
- Checkpoint: `/root/autodl-tmp/checkpoints/reverse_cutoff_s2_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--reverse_cutoff_s2_v2--50000_chkpt`
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/reverse_cutoff_s2_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--reverse_cutoff_s2_v2--50000_chkpt --task_suite_name libero_spatial --num_rollouts 50 --seed 42
```

### 6. full_occ_ln_v2_s0_eval
- GPU: cuda:1（训练完成后同卡 eval）
- ETA: ~01:15
- Checkpoint: `/root/autodl-tmp/checkpoints/full_occ_ln_v2_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s0--50000_chkpt`
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/full_occ_ln_v2_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s0--50000_chkpt --task_suite_name libero_spatial --num_rollouts 50 --seed 42
```

### 7. full_occ_ln_v2_s1_eval
- GPU: cuda:2（训练完成后同卡 eval）
- ETA: ~01:15
- Checkpoint: `/root/autodl-tmp/checkpoints/full_occ_ln_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s1--50000_chkpt`
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=2 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/full_occ_ln_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s1--50000_chkpt --task_suite_name libero_spatial --num_rollouts 50 --seed 42
```

### 8. detach_ln_v2_s0_eval
- GPU: cuda:3（训练完成后同卡 eval）
- ETA: ~01:15
- Checkpoint: `/root/autodl-tmp/checkpoints/detach_ln_v2_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_v2_s0--50000_chkpt`
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=3 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_ln_v2_s0/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_v2_s0--50000_chkpt --task_suite_name libero_spatial --num_rollouts 50 --seed 42
```

---

## westd-34685

### 2. vanilla_v2_s1_eval
- GPU: cuda:0（训练完成后同卡 eval）
- ETA: ~23:30
- Checkpoint: `/root/autodl-tmp/checkpoints/vanilla_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--vanilla_v2_s1--50000_chkpt`
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/vanilla_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--vanilla_v2_s1--50000_chkpt --task_suite_name libero_spatial --num_rollouts 50 --seed 42
```

### 3. vanilla_v2_s2_eval
- GPU: cuda:1（训练完成后同卡 eval）
- ETA: ~23:30
- Checkpoint: `/root/autodl-tmp/checkpoints/vanilla_v2_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--vanilla_v2_s2--50000_chkpt`
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/vanilla_v2_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--vanilla_v2_s2--50000_chkpt --task_suite_name libero_spatial --num_rollouts 50 --seed 42
```

### 4. detach_ln_s3_eval
- GPU: cuda:2（训练完成后同卡 eval）
- ETA: ~23:30
- Checkpoint: `/root/autodl-tmp/checkpoints/detach_ln_s3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_s3--50000_chkpt`
- 注意: 已确认用 v2 代码训练
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=2 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_ln_s3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_s3--50000_chkpt --task_suite_name libero_spatial --num_rollouts 50 --seed 42
```

### 5. cutoff_25k_s1_v2_eval
- GPU: cuda:3（训练完成后同卡 eval）
- ETA: ~00:00
- Checkpoint: `/root/autodl-tmp/checkpoints/cutoff_25k_s1_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--cutoff_25k_s1_v2--50000_chkpt`
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=3 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/cutoff_25k_s1_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--cutoff_25k_s1_v2--50000_chkpt --task_suite_name libero_spatial --num_rollouts 50 --seed 42
```

---

## 启动顺序建议

按 ETA 排序，训练完成后立即在同卡启动 eval：

| 序号 | ETA | 实验 | 服务器 | GPU |
|------|-----|------|--------|-----|
| 1 | ~23:00 | reverse_cutoff_s2_v2 | westd-10894 | cuda:0 |
| 2 | ~23:30 | vanilla_v2_s1 | westd-34685 | cuda:0 |
| 3 | ~23:30 | vanilla_v2_s2 | westd-34685 | cuda:1 |
| 4 | ~23:30 | detach_ln_s3 | westd-34685 | cuda:2 |
| 5 | ~00:00 | cutoff_25k_s1_v2 | westd-34685 | cuda:3 |
| 6 | ~01:15 | full_occ_ln_v2_s0 | westd-10894 | cuda:1 |
| 7 | ~01:15 | full_occ_ln_v2_s1 | westd-10894 | cuda:2 |
| 8 | ~01:15 | detach_ln_v2_s0 | westd-10894 | cuda:3 |

## 注意事项
- 启动 eval 前先确认 checkpoint `--50000_chkpt` 目录已存在
- 所有实验均从 pretrained 从头训练（非 resume），checkpoint 命名统一
- Eval 约需 ~50 分钟/实验（基于历史数据 2900-3500s）
