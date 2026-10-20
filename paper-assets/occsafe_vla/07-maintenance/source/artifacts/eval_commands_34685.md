# Eval Commands for westd-34685 (4 experiments)

Generated: 2026-05-26

## Checkpoint naming pattern

Confirmed from westd-10894 existing checkpoints:
- Checkpoint dirs are siblings of run dir under `run_root_dir/`
- Format: `{base_config}--{run_id_note}--{step}_chkpt`
- Base config: `openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug`

## 1. vanilla_v2_s1 (cuda:0)

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/vanilla_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--vanilla_v2_s1--50000_chkpt --task_suite_name libero_spatial --num_rollouts 50 --seed 42"
```

## 2. vanilla_v2_s2 (cuda:1)

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/vanilla_v2_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--vanilla_v2_s2--50000_chkpt --task_suite_name libero_spatial --num_rollouts 50 --seed 42"
```

## 3. detach_ln_s3 (cuda:2)

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=2 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_ln_s3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_s3--50000_chkpt --task_suite_name libero_spatial --num_rollouts 50 --seed 42"
```

## 4. cutoff_25k_s1_v2 (cuda:3)

```bash
bash -c "source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft && MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=3 python vla-scripts/evaluate_safelibero.py --pretrained_checkpoint /root/autodl-tmp/checkpoints/cutoff_25k_s1_v2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--cutoff_25k_s1_v2--50000_chkpt --task_suite_name libero_spatial --num_rollouts 50 --seed 42"
```

## Notes

- All 4 experiments currently at ~14%, ETA ~21:30 UTC. No checkpoints saved yet (only `dataset_statistics.json` exists).
- cutoff_25k_s1_v2 confirmed via `/proc/453581/cmdline`: `--run_root_dir /root/autodl-tmp/checkpoints/cutoff_25k_s1_v2 --run_id_note cutoff_25k_s1_v2`
- Checkpoint path pattern verified against completed experiments on westd-10894 (e.g., `cutoff_15k_s1--50000_chkpt`, `cutoff_45k_s2_v2--50000_chkpt`).
