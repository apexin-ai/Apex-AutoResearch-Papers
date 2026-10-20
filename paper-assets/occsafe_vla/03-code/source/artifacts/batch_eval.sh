#!/bin/bash
set -euo pipefail

CKPT_BASE="/root/autodl-tmp/checkpoints"
LOG_DIR="/root/occsafe_vla/logs"
TASK_SUITE="libero_spatial"
NUM_ROLLOUTS=50
SEED=42

usage() {
    echo "Usage: $0 <exp_id:gpu_id> [exp_id:gpu_id ...]"
    echo ""
    echo "Example:"
    echo "  $0 vanilla_v2_s1:0 vanilla_v2_s2:1 detach_ln_s3:2 cutoff_25k_s1_v2:3"
    echo ""
    echo "Each argument is exp_id:gpu_id pair."
    echo "Checkpoint path: ${CKPT_BASE}/{exp_id}/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--{exp_id}--50000_chkpt"
    exit 1
}

if [ $# -eq 0 ]; then
    usage
fi

declare -a EXP_IDS
declare -a GPU_IDS
declare -a CKPT_PATHS

for arg in "$@"; do
    if [[ "$arg" != *:* ]]; then
        echo "ERROR: Invalid format '$arg'. Expected exp_id:gpu_id"
        exit 1
    fi
    exp_id="${arg%%:*}"
    gpu_id="${arg##*:}"
    ckpt_path="${CKPT_BASE}/${exp_id}/openvla-7b+libero_spatial_no_noops+b8+lr-0.0005+lora-r32+dropout-0.0--image_aug--${exp_id}--50000_chkpt"

    EXP_IDS+=("$exp_id")
    GPU_IDS+=("$gpu_id")
    CKPT_PATHS+=("$ckpt_path")
done

echo "=== Pre-flight: checking checkpoints ==="
all_ok=true
for i in "${!EXP_IDS[@]}"; do
    if [ -d "${CKPT_PATHS[$i]}" ]; then
        echo "  [OK] ${EXP_IDS[$i]} -> ${CKPT_PATHS[$i]}"
    else
        echo "  [MISSING] ${EXP_IDS[$i]} -> ${CKPT_PATHS[$i]}"
        all_ok=false
    fi
done

if [ "$all_ok" = false ]; then
    echo ""
    echo "ERROR: Some checkpoints are missing. Aborting (no evals started)."
    exit 1
fi

mkdir -p "$LOG_DIR"

echo ""
echo "=== Launching evals ==="
for i in "${!EXP_IDS[@]}"; do
    exp_id="${EXP_IDS[$i]}"
    gpu_id="${GPU_IDS[$i]}"
    ckpt_path="${CKPT_PATHS[$i]}"
    session_name="${exp_id}_eval"
    log_file="${LOG_DIR}/${exp_id}_eval.log"

    # Kill existing session if any
    tmux kill-session -t "$session_name" 2>/dev/null || true

    tmux new-session -d -s "$session_name" bash -c "
source /root/miniconda3/etc/profile.d/conda.sh && conda activate occsafe && \
cd /root/occsafe_vla/openvla-oft && \
CUDA_VISIBLE_DEVICES=${gpu_id} MUJOCO_GL=egl MUJOCO_EGL_DEVICE_ID=${gpu_id} \
python3 vla-scripts/evaluate_safelibero.py \
  --pretrained_checkpoint ${ckpt_path} \
  --task_suite_name ${TASK_SUITE} \
  --num_rollouts ${NUM_ROLLOUTS} \
  --seed ${SEED} \
  2>&1 | tee ${log_file}
"
    echo "  [LAUNCHED] ${exp_id} on GPU ${gpu_id} -> tmux: ${session_name}, log: ${log_file}"
done

echo ""
echo "=== Active tmux sessions ==="
tmux list-sessions 2>/dev/null || echo "  (no tmux sessions found)"
echo ""
echo "Done. Use 'tmux attach -t <session_name>' to monitor, or 'tail -f ${LOG_DIR}/<exp_id>_eval.log' for logs."
