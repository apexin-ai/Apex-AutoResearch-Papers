#!/usr/bin/env python3
"""Generate GPU recovery launch scripts for all 14 experiments."""

import os
import stat

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

COMMON_HEADER = '''#!/bin/bash
set -euo pipefail

# === {title} ===
# Experiment: {exp_name}
# Condition:  {condition}
# Seed:       {seed}
# Group:      {group}

GPU_ID=${{1:-0}}  # Physical GPU ID, default 0

echo "================================================================"
echo " Experiment: {exp_name}"
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
EXP_NAME="{exp_name}"
CHECKPOINT_DIR="/root/autodl-tmp/checkpoints/$EXP_NAME"
RESUME_FLAGS=""

if [ -d "$CHECKPOINT_DIR" ]; then
    LATEST_STEP=$(ls -d ${{CHECKPOINT_DIR}}/*_chkpt 2>/dev/null \\
        | grep -oP '\\d+(?=_chkpt)' | sort -n | tail -1)
    if [ -n "$LATEST_STEP" ] && [ "$LATEST_STEP" -ge 40000 ]; then
        echo "[RESUME] Found checkpoint at step $LATEST_STEP in $CHECKPOINT_DIR"
        RESUME_FLAGS="--resume True --resume_step $LATEST_STEP"
    else
        echo "[FROM SCRATCH] No checkpoint >= 40000 found (latest: ${{LATEST_STEP:-none}})"
    fi
else
    echo "[FROM SCRATCH] No checkpoint directory: $CHECKPOINT_DIR"
fi

# Create log directory
mkdir -p /root/autodl-tmp/occsafe_vla/runs

echo ""
echo "[START] Training {exp_name} at $(date '+%H:%M:%S')"
echo ""

'''

COMMON_BASE_FLAGS = (
    'MUJOCO_EGL_DEVICE_ID=$GPU_ID WANDB_MODE=disabled '
    'torchrun --standalone --nnodes 1 --nproc-per-node 1 '
    'vla-scripts/finetune.py '
    '--vla_path /root/autodl-tmp/models/openvla-7b '
    '--data_root_dir /root/autodl-tmp/data/modified_libero_rlds/ '
    '--dataset_name libero_spatial_no_noops '
    '--use_l1_regression True '
    '--num_images_in_input 2 '
    '--use_proprio True '
    '--batch_size 8 '
    '--learning_rate 5e-4 '
    '--max_steps 50005 '
    '--save_freq 10000 '
    '--image_aug True '
    '--lora_rank 32'
)

VANILLA_EXTRA = (
    ' --use_diffusion False --use_film False'
    ' --num_steps_before_decay 100000'
)

OCC_BASE = (
    ' --use_occ_head True'
    ' --occ_data_dir /root/occsafe_vla/occ_data'
)

experiments = [
    # RD2-N1: Seed expansion (8 runs)
    {
        'exp_name': 'full_occ_bn_v2_s3',
        'condition': 'Cell 1: Full OCC BN (gradient ON, BatchNorm)',
        'seed': 45,
        'group': 'RD2-N1 seed expansion',
        'title': 'RD2-N1: Full OCC BN seed 45',
        'occ_flags': ' --occ_detach false --occ_norm_type bn',
    },
    {
        'exp_name': 'full_occ_bn_v2_s4',
        'condition': 'Cell 1: Full OCC BN (gradient ON, BatchNorm)',
        'seed': 46,
        'group': 'RD2-N1 seed expansion',
        'title': 'RD2-N1: Full OCC BN seed 46',
        'occ_flags': ' --occ_detach false --occ_norm_type bn',
    },
    {
        'exp_name': 'full_occ_ln_v2_s3',
        'condition': 'Cell 2: Full OCC LN (gradient ON, LayerNorm)',
        'seed': 46,
        'group': 'RD2-N1 seed expansion',
        'title': 'RD2-N1: Full OCC LN seed 46',
        'occ_flags': ' --occ_detach false --occ_norm_type ln',
    },
    {
        'exp_name': 'detach_bn_v2_s3',
        'condition': 'Cell 3: Detach BN (gradient OFF, BatchNorm)',
        'seed': 46,
        'group': 'RD2-N1 seed expansion',
        'title': 'RD2-N1: Detach BN seed 46',
        'occ_flags': ' --occ_detach true --occ_norm_type bn',
    },
    {
        'exp_name': 'detach_ln_v2_s3',
        'condition': 'Cell 4: Detach LN (gradient OFF, LayerNorm)',
        'seed': 45,
        'group': 'RD2-N1 seed expansion',
        'title': 'RD2-N1: Detach LN seed 45',
        'occ_flags': ' --occ_detach true --occ_norm_type ln',
    },
    {
        'exp_name': 'detach_ln_v2_s4',
        'condition': 'Cell 4: Detach LN (gradient OFF, LayerNorm)',
        'seed': 46,
        'group': 'RD2-N1 seed expansion',
        'title': 'RD2-N1: Detach LN seed 46',
        'occ_flags': ' --occ_detach true --occ_norm_type ln',
    },
    {
        'exp_name': 'vanilla_v2_s3',
        'condition': 'Vanilla baseline (no auxiliary head)',
        'seed': 45,
        'group': 'RD2-N1 seed expansion',
        'title': 'RD2-N1: Vanilla seed 45',
        'occ_flags': None,  # vanilla
    },
    {
        'exp_name': 'vanilla_v2_s4',
        'condition': 'Vanilla baseline (no auxiliary head)',
        'seed': 46,
        'group': 'RD2-N1 seed expansion',
        'title': 'RD2-N1: Vanilla seed 46',
        'occ_flags': None,  # vanilla
    },
    # RD2-N2: Random OCC v2 (3 runs)
    {
        'exp_name': 'random_occ_v2_s0',
        'condition': 'Random OCC (content irrelevance control)',
        'seed': 42,
        'group': 'RD2-N2 Random OCC v2',
        'title': 'RD2-N2: Random OCC seed 42',
        'occ_flags': ' --occ_detach false --occ_norm_type bn --random_occ True',
    },
    {
        'exp_name': 'random_occ_v2_s1',
        'condition': 'Random OCC (content irrelevance control)',
        'seed': 43,
        'group': 'RD2-N2 Random OCC v2',
        'title': 'RD2-N2: Random OCC seed 43',
        'occ_flags': ' --occ_detach false --occ_norm_type bn --random_occ True',
    },
    {
        'exp_name': 'random_occ_v2_s2',
        'condition': 'Random OCC (content irrelevance control)',
        'seed': 44,
        'group': 'RD2-N2 Random OCC v2',
        'title': 'RD2-N2: Random OCC seed 44',
        'occ_flags': ' --occ_detach false --occ_norm_type bn --random_occ True',
    },
    # RD2-W4: BN eval mode (1 run)
    {
        'exp_name': 'full_occ_bn_eval_v2_s0',
        'condition': 'Full OCC BN with eval-mode BN (frozen running stats)',
        'seed': 42,
        'group': 'RD2-W4 BN eval mode',
        'title': 'RD2-W4: BN eval mode seed 42',
        'occ_flags': ' --occ_detach false --occ_norm_type bn --occ_bn_eval True',
    },
    # RD3-W3: Lambda sweep (2 runs)
    {
        'exp_name': 'full_occ_bn_lambda001_s0',
        'condition': 'Full OCC BN with lambda_0=0.001 (10x lower)',
        'seed': 42,
        'group': 'RD3-W3 lambda sweep',
        'title': 'RD3-W3: lambda=0.001 seed 42',
        'occ_flags': ' --occ_detach false --occ_norm_type bn --occ_loss_weight 0.001',
    },
    {
        'exp_name': 'full_occ_bn_lambda01_s0',
        'condition': 'Full OCC BN with lambda_0=0.1 (10x higher)',
        'seed': 42,
        'group': 'RD3-W3 lambda sweep',
        'title': 'RD3-W3: lambda=0.1 seed 42',
        'occ_flags': ' --occ_detach false --occ_norm_type bn --occ_loss_weight 0.1',
    },
]

for exp in experiments:
    header = COMMON_HEADER.format(**exp)

    if exp['occ_flags'] is None:
        # Vanilla: no OCC head
        cmd = COMMON_BASE_FLAGS + VANILLA_EXTRA
    else:
        # OCC experiment
        cmd = COMMON_BASE_FLAGS + OCC_BASE + exp['occ_flags']

    cmd += (
        f" --run_root_dir /root/autodl-tmp/checkpoints/{exp['exp_name']}"
        f" --seed {exp['seed']}"
        f" --run_id_note {exp['exp_name']}"
        ' $RESUME_FLAGS'
    )

    log_path = f"/root/autodl-tmp/occsafe_vla/runs/{exp['exp_name']}.log"

    script = header
    script += f'{cmd} \\\n    2>&1 | tee {log_path}\n'
    script += f'\necho ""\necho "[DONE] {exp["exp_name"]} finished at $(date \'+%H:%M:%S\')"\n'

    path = os.path.join(SCRIPT_DIR, f"{exp['exp_name']}.sh")
    with open(path, 'w') as f:
        f.write(script)
    os.chmod(path, os.stat(path).st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    print(f"  Created: {exp['exp_name']}.sh")

print(f"\nTotal: {len(experiments)} scripts generated.")
