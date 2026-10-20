# Eval Commands — Factorial n=5 Expansion (2026-05-27)

8 experiments across 4 batches. Each: 50-rollout SafeLIBERO eval.

## Common Setup

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe
cd /root/occsafe_vla/openvla-oft
```

CKPT prefix: `/root/autodl-tmp/checkpoints/`
Run ID pattern: `openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--{RUN_ID}`

---

## Batch ① — westd-34685 cuda:0-1 (ETA ~12:58-12:59 UTC May 27)

### detach_ln_v2_s1_35 → Cell 4 (Detach LN), seed 43

```bash
CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 WANDB_MODE=disabled \
python vla-scripts/evaluate_safelibero.py \
  --model_family openvla \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_ln_v2_s1/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_v2_s1 \
  --task_suite_name libero_spatial \
  --num_rollouts 50 \
  --center_crop True \
  --num_images_in_input 2 \
  --use_proprio True \
  --run_id_note detach_ln_v2_s1_35_eval \
  --seed 42
```

> **Note**: run_root_dir = `detach_ln_v2_s1` (not `detach_ln_v2_s1_35`). Checkpoint verified on 34685.

### detach_ln_s4 → Cell 4 (Detach LN, v1 code), seed 46

```bash
CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 WANDB_MODE=disabled \
python vla-scripts/evaluate_safelibero.py \
  --model_family openvla \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_ln_s4/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_s4 \
  --task_suite_name libero_spatial \
  --num_rollouts 50 \
  --center_crop True \
  --num_images_in_input 2 \
  --use_proprio True \
  --run_id_note detach_ln_s4_eval \
  --seed 42
```

> **Note**: v1 code, seed 46. Checkpoint verified on 34685.

---

## Batch ② — westd-34685 cuda:2-3 (ETA ~13:46-13:52 UTC May 27)

### ablation_occ_detach_s4 → Cell 3 (Detach BN), seed 46

```bash
CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=2 WANDB_MODE=disabled \
python vla-scripts/evaluate_safelibero.py \
  --model_family openvla \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/ablation_occ_detach_s4/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--ablation_occ_detach_s4 \
  --task_suite_name libero_spatial \
  --num_rollouts 50 \
  --center_crop True \
  --num_images_in_input 2 \
  --use_proprio True \
  --run_id_note ablation_occ_detach_s4_eval \
  --seed 42
```

> Checkpoint verified on 34685.

### mvp_occ_s4 → Cell 1 (Full OCC BN), seed 46

```bash
CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=3 WANDB_MODE=disabled \
python vla-scripts/evaluate_safelibero.py \
  --model_family openvla \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/mvp_occ_s4/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--mvp_occ_s4 \
  --task_suite_name libero_spatial \
  --num_rollouts 50 \
  --center_crop True \
  --num_images_in_input 2 \
  --use_proprio True \
  --run_id_note mvp_occ_s4_eval \
  --seed 42
```

> Checkpoint verified on 34685.

---

## Batch ③ — westd-10894 cuda:0-1 (ETA ~22:40-22:50 UTC May 27)

### full_occ_ln_v2_s1c_r2 → Cell 2 (Full OCC LN), seed 43

```bash
CUDA_VISIBLE_DEVICES=0 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 WANDB_MODE=disabled \
python vla-scripts/evaluate_safelibero.py \
  --model_family openvla \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/full_occ_ln_v2_s1c/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s1c \
  --task_suite_name libero_spatial \
  --num_rollouts 50 \
  --center_crop True \
  --num_images_in_input 2 \
  --use_proprio True \
  --run_id_note full_occ_ln_v2_s1c_r2_eval \
  --seed 42
```

> **Note**: Checkpoint dir = `full_occ_ln_v2_s1c` (not `full_occ_ln_v2_s1c_r2`). r2 overwrites into same dir. Verified on 10894: has final + 20k + 30k checkpoints.

### full_occ_ln_v2_s2_r2 → Cell 2 (Full OCC LN), seed 44

```bash
CUDA_VISIBLE_DEVICES=1 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=1 WANDB_MODE=disabled \
python vla-scripts/evaluate_safelibero.py \
  --model_family openvla \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/full_occ_ln_v2_s2/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_v2_s2 \
  --task_suite_name libero_spatial \
  --num_rollouts 50 \
  --center_crop True \
  --num_images_in_input 2 \
  --use_proprio True \
  --run_id_note full_occ_ln_v2_s2_r2_eval \
  --seed 42
```

> **Note**: Checkpoint dir = `full_occ_ln_v2_s2` (not `full_occ_ln_v2_s2_r2`). Verified on 10894: has final + 20k + 30k checkpoints.

---

## Batch ④ — westd-10894 cuda:2-3 (ETA ~06:20-06:50 UTC May 28)

### detach_ln_v2_s0c_r3 → Cell 4 (Detach LN), seed 42

```bash
CUDA_VISIBLE_DEVICES=2 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=2 WANDB_MODE=disabled \
python vla-scripts/evaluate_safelibero.py \
  --model_family openvla \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/detach_ln_v2_s0c_r3/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--detach_ln_v2_s0c_r3 \
  --task_suite_name libero_spatial \
  --num_rollouts 50 \
  --center_crop True \
  --num_images_in_input 2 \
  --use_proprio True \
  --run_id_note detach_ln_v2_s0c_r3_eval \
  --seed 42
```

> Checkpoint dir verified on 10894. Currently has final + 10k checkpoint (training in progress).

### full_occ_ln_s4 → Cell 2 (Full OCC LN), seed 46

```bash
CUDA_VISIBLE_DEVICES=3 MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=3 WANDB_MODE=disabled \
python vla-scripts/evaluate_safelibero.py \
  --model_family openvla \
  --pretrained_checkpoint /root/autodl-tmp/checkpoints/full_occ_ln_s4/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--full_occ_ln_s4 \
  --task_suite_name libero_spatial \
  --num_rollouts 50 \
  --center_crop True \
  --num_images_in_input 2 \
  --use_proprio True \
  --run_id_note full_occ_ln_s4_eval \
  --seed 42
```

> Checkpoint dir verified on 10894. Only final dir present (training early stage).

---

## Post-Eval: Update ANOVA Data

After each eval completes, extract CAR and update the ANOVA script:

```bash
cd /root/occsafe_vla/analysis
python factorial_anova.py --update-cell {CELL_ID} --car {CAR_VALUE} --exp-id {EXP_ID}
```

Cell mapping:
| Experiment | Cell | Update Command |
|---|---|---|
| detach_ln_v2_s1_35 | 4 | `--update-cell 4 --car X --exp-id detach_ln_v2_s1_35` |
| detach_ln_s4 | 4 | `--update-cell 4 --car X --exp-id detach_ln_s4` |
| ablation_occ_detach_s4 | 3 | `--update-cell 3 --car X --exp-id ablation_occ_detach_s4` |
| mvp_occ_s4 | 1 | `--update-cell 1 --car X --exp-id mvp_occ_s4` |
| full_occ_ln_v2_s1c_r2 | 2 | `--update-cell 2 --car X --exp-id full_occ_ln_v2_s1c_r2` |
| full_occ_ln_v2_s2_r2 | 2 | `--update-cell 2 --car X --exp-id full_occ_ln_v2_s2_r2` |
| detach_ln_v2_s0c_r3 | 4 | `--update-cell 4 --car X --exp-id detach_ln_v2_s0c_r3` |
| full_occ_ln_s4 | 2 | `--update-cell 2 --car X --exp-id full_occ_ln_s4` |

## Expected Final Sample Sizes (after all evals)

| Cell | Current n | +Pending | Final n |
|---|---|---|---|
| 1 (Full OCC BN) | 3 | +1 (mvp_occ_s4) | 4 |
| 2 (Full OCC LN) | 1 | +3 (s1c_r2, s2_r2, s4) | 4 |
| 3 (Detach BN) | 4 | +1 (detach_s4) | 5 |
| 4 (Detach LN) | 1 | +3 (s1_35, s0c_r3, s4†) | 4 (3 v2 + 1 v1†) |

†detach_ln_s4 is v1 code — flag in analysis if needed.
