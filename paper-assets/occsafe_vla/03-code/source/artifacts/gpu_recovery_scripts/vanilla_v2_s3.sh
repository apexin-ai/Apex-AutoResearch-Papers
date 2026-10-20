#!/bin/bash
set -euo pipefail

# === RD2-N1: Vanilla seed 45 ===
# Experiment: vanilla_v2_s3
# Condition:  Vanilla baseline (no auxiliary head)
# Seed:       45
# Group:      RD2-N1 seed expansion

GPU_ID=${1:-0}  # Physical GPU ID, default 0

echo "================================================================"
echo " Experiment: vanilla_v2_s3"
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
EXP_NAME="vanilla_v2_s3"
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
echo "[START] Training vanilla_v2_s3 at $(date '+%H:%M:%S')"
echo ""

MUJOCO_EGL_DEVICE_ID=$GPU_ID WANDB_MODE=disabled torchrun --standalone --nnodes 1 --nproc-per-node 1 vla-scripts/finetune.py --vla_path /root/autodl-tmp/models/openvla-7b --data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ --dataset_name libero_spatial_no_noops --use_l1_regression True --num_images_in_input 2 --use_proprio True --batch_size 8 --learning_rate 5e-4 --max_steps 50005 --save_freq 10000 --image_aug True --lora_rank 32 --use_diffusion False --use_film False --num_steps_before_decay 100000 --run_root_dir /root/autodl-tmp/checkpoints/vanilla_v2_s3 --seed 45 --run_id_note vanilla_v2_s3 $RESUME_FLAGS \
    2>&1 | tee /root/autodl-tmp/occsafe_vla/runs/vanilla_v2_s3.log

echo ""
echo "[DONE] vanilla_v2_s3 finished at $(date '+%H:%M:%S')"
