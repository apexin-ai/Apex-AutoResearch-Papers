#!/bin/bash
set -euo pipefail

# === RD2-N1: Detach LN seed 46 ===
# Experiment: detach_ln_v2_s4
# Condition:  Cell 4: Detach LN (gradient OFF, LayerNorm)
# Seed:       46
# Group:      RD2-N1 seed expansion

GPU_ID=${1:-0}  # Physical GPU ID, default 0

echo "================================================================"
echo " Experiment: detach_ln_v2_s4"
echo " GPU:        cuda:$GPU_ID"
echo " Timestamp:  $(date '+%Y-%m-%d %H:%M:%S')"
echo "================================================================"

# GPU verification
echo ""
echo "[CHECK] nvidia-smi output:"
nvidia-smi --query-gpu=index,name,memory.total,driver_version --format=csv,noheader
echo ""

export CUDA_VISIBLE_DEVICES=$GPU_ID

# Environment setup
source /root/miniconda3/etc/profile.d/conda.sh
conda activate occsafe
cd /root/occsafe_vla/openvla-oft

# Checkpoint resume logic
EXP_NAME="detach_ln_v2_s4"
CHECKPOINT_DIR="/root/autodl-tmp/checkpoints/$EXP_NAME"
RESUME_FLAGS=""

if [ -d "$CHECKPOINT_DIR" ]; then
    LATEST_STEP=$(ls -d ${CHECKPOINT_DIR}/*_chkpt 2>/dev/null \
        | grep -oP '\d+(?=_chkpt)' | sort -n | tail -1)
    if [ -n "$LATEST_STEP" ] && [ "$LATEST_STEP" -ge 40000 ]; then
        echo "[RESUME] Found checkpoint at step $LATEST_STEP in $CHECKPOINT_DIR"
        RESUME_FLAGS="--resume True --resume_step $LATEST_STEP"
    else
        echo "[FROM SCRATCH] No checkpoint >= 40000 found (latest: ${LATEST_STEP:-none})"
    fi
else
    echo "[FROM SCRATCH] No checkpoint directory: $CHECKPOINT_DIR"
fi

# Create log directory
mkdir -p /root/autodl-tmp/occsafe_vla/runs

echo ""
echo "[START] Training detach_ln_v2_s4 at $(date '+%H:%M:%S')"
echo ""

MUJOCO_EGL_DEVICE_ID=$GPU_ID WANDB_MODE=disabled torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_occ_head True --occ_data_dir /root/occsafe_vla/occ_data --occ_detach true --occ_norm_type ln --run_root_dir /root/autodl-tmp/checkpoints/detach_ln_v2_s4 --seed 46 --run_id_note detach_ln_v2_s4 $RESUME_FLAGS \
    2>&1 | tee /root/autodl-tmp/occsafe_vla/runs/detach_ln_v2_s4.log

echo ""
echo "[DONE] detach_ln_v2_s4 finished at $(date '+%H:%M:%S')"
