# Server Recovery Plan (2026-05-29)

## Pre-flight (MANDATORY before ANY experiment submission)

```bash
# On EACH server, BEFORE submitting:
ssh_read_only: nvidia-smi -L
# Expect: "GPU 0: NVIDIA RTX PRO 6000 ..." (exactly 1 GPU)
# If 0 GPUs or different count → STOP and report to Director
```

---

## Phase 1: Resume Interrupted Experiments

### 1A. random_occ_v2_s0_r4 @westd-10894

Last known state: step ~39620/50005, save_freq=10000 → likely has step 40000 checkpoint.

```bash
# Step 1: Check what checkpoints exist
ssh_read_only:
ls -lt /root/autodl-tmp/checkpoints/random_occ_v2_s0_r4/
# Look for directories matching *--{step}_chkpt pattern
# Expected: 10000, 20000, 30000, 40000

# Step 2: Check if training actually completed (step 50005)
ssh_read_only:
tail -5 /root/runs/occsafe_vla/random_occ_v2_s0_r4.log
# If last line shows step 50000+ → training DONE, skip to eval
# If shows step < 50000 → need resume

# Step 3a: If DONE → run eval
ssh_execute:
CKPT_DIR=$(ls -d /root/autodl-tmp/checkpoints/random_occ_v2_s0_r4/*50000_chkpt 2>/dev/null | head -1)
echo "Eval checkpoint: $CKPT_DIR"

bash -c "export CUDA_VISIBLE_DEVICES=0 && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/occsafe_vla/openvla-oft && \
MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint $CKPT_DIR \
  --task_suite_name libero_spatial \
  --num_rollouts 50 \
  --seed 42"

# Step 3b: If NOT DONE → resume from latest checkpoint
# Find latest checkpoint step:
ssh_read_only:
ls /root/autodl-tmp/checkpoints/random_occ_v2_s0_r4/ | grep chkpt | sort -t- -k1 -n | tail -1

# Resume command (adjust LATEST_STEP from above):
bash -c "export WANDB_MODE=disabled && export CUDA_VISIBLE_DEVICES=0 && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/occsafe_vla/openvla-oft && \
torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py \
  --vla_path /root/autodl-tmp/models/openvla-7b \
  --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ \
  --dataset_name libero_spatial_no_noops \
  --use_l1_regression True --num_images_in_input 2 --use_proprio True \
  --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 \
  --image_aug True --lora_rank 32 \
  --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data \
  --occ_detach false --random_occ True \
  --run_root_dir /root/autodl-tmp/checkpoints/random_occ_v2_s0_r4 \
  --seed 42 --run_id_note random_occ_v2_s0_r4 \
  --resume true"
```

### 1B. full_occ_bn_v2_s2_r5 @westd-34685

Last known state: step ~39287/50005, save_freq=10000 → likely has step 40000 checkpoint.

```bash
# Step 1: Check checkpoints
ssh_read_only:
ls -lt /root/autodl-tmp/checkpoints/full_occ_bn_v2_s2_r5/

# Step 2: Check completion
ssh_read_only:
tail -5 /root/runs/occsafe_vla/full_occ_bn_v2_s2_r5.log

# Step 3a: If DONE → eval
ssh_execute:
CKPT_DIR=$(ls -d /root/autodl-tmp/checkpoints/full_occ_bn_v2_s2_r5/*50000_chkpt 2>/dev/null | head -1)

bash -c "export CUDA_VISIBLE_DEVICES=0 && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/openvla-oft && \
MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=0 python vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint $CKPT_DIR \
  --task_suite_name libero_spatial \
  --num_rollouts 50 \
  --seed 42"

# Step 3b: If NOT DONE → resume
bash -c "export WANDB_MODE=disabled && export CUDA_VISIBLE_DEVICES=0 && \
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/openvla-oft && \
torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py \
  --vla_path /root/autodl-tmp/models/openvla-7b \
  --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ \
  --dataset_name libero_spatial_no_noops \
  --use_l1_regression True --num_images_in_input 2 --use_proprio True \
  --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 \
  --image_aug True --lora_rank 32 \
  --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data \
  --occ_detach false \
  --run_root_dir /root/autodl-tmp/checkpoints/full_occ_bn_v2_s2_r5 \
  --seed 44 --run_id_note full_occ_bn_v2_s2_r5 \
  --resume true"
```

**NOTE**: westd-34685 code path is `/root/openvla-oft/` (NOT `/root/occsafe_vla/openvla-oft/`).

---

## Phase 2: Queue Experiments (after Phase 1 eval completes)

Base env setup per server:
- westd-10894: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/occsafe_vla/openvla-oft`
- westd-34685: `source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && cd /root/openvla-oft`

Common flags (all experiments):
```
--vla_path /root/autodl-tmp/models/openvla-7b
--data_root_dir /root/autodl-tmp/data/modified_libero_rlds/
--dataset_name libero_spatial_no_noops
--use_l1_regression True --num_images_in_input 2 --use_proprio True
--batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000
--image_aug True --lora_rank 32
--use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data
```

### westd-10894 Queue

#### Q1: full_occ_bn_eval_v2_s0_r2 (BN eval mode ablation)
```
CONDITION_FLAGS: --occ_detach false --occ_bn_eval true
SEED: 42
RUN_ID: full_occ_bn_eval_v2_s0_r2
```

#### Q2: full_occ_bn_lambda001_v2_s0_r2 (λ₀=0.001)
```
CONDITION_FLAGS: --occ_detach false --occ_loss_weight 0.001
SEED: 42
RUN_ID: full_occ_bn_lambda001_v2_s0_r2
```

#### Q3: full_occ_bn_lambda01_v2_s0_r2 (λ₀=0.1)
```
CONDITION_FLAGS: --occ_detach false --occ_loss_weight 0.1
SEED: 42
RUN_ID: full_occ_bn_lambda01_v2_s0_r2
```

### westd-34685 Queue

#### Q4: vanilla_v2_s3_r2 (Vanilla baseline seed expansion)
```
CONDITION_FLAGS: (no --use_occ_head, remove occ flags entirely)
NOTE: Vanilla = no auxiliary head. Remove --use_occ_head True --occ_data_dir --occ_detach etc.
SEED: 45
RUN_ID: vanilla_v2_s3_r2
```

#### Q5: full_occ_bn_v2_s4_r2 (Cell 1 seed expansion)
```
CONDITION_FLAGS: --occ_detach false
SEED: 45
RUN_ID: full_occ_bn_v2_s4_r2
```

#### Q6: detach_bn_v2_s3_r2 (Cell 3 seed expansion)
```
CONDITION_FLAGS: --occ_detach true
SEED: 47
RUN_ID: detach_bn_v2_s3_r2
```

---

## Checklist Before Each Submission

- [ ] `nvidia-smi -L` → exactly 1 GPU visible
- [ ] `CUDA_VISIBLE_DEVICES=0` in command
- [ ] `WANDB_MODE=disabled` set
- [ ] `--occ_data_dir /root/occsafe_vla/occ_data` included (for OCC experiments)
- [ ] `MUJOCO_EGL_DEVICE_ID=0` for eval
- [ ] Correct code path (10894: `/root/occsafe_vla/openvla-oft/`, 34685: `/root/openvla-oft/`)
- [ ] Correct conda env: `occsafe`
