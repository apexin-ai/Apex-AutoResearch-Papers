#!/bin/bash
# Deploy Adaptive Conformal CRM evals: 3 suites × 3 seeds = 9 jobs
# Usage: bash deploy_adaptive_k_eval.sh [GPU_LIST]
#   GPU_LIST: comma-separated GPU indices (default: "0")
#   Example: bash deploy_adaptive_k_eval.sh 0,1,2,3,4,5

set -euo pipefail

GPU_LIST="${1:-0}"
IFS=',' read -ra GPUS <<< "$GPU_LIST"
NUM_GPUS=${#GPUS[@]}

PROJECT_DIR="/root/acr-vla-conformal-refinement"
CRM_CKPT="/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt"
CONFORMAL_TAU=0.074855
N_ROLLOUTS=20

SUITES=("object" "spatial" "goal")
SEEDS=(42 43 44)

# Verify checkpoint exists
if [ ! -f "$CRM_CKPT" ]; then
    echo "ERROR: CRM checkpoint not found: $CRM_CKPT"
    exit 1
fi

cd "$PROJECT_DIR"
mkdir -p logs

job_idx=0
for suite in "${SUITES[@]}"; do
    for seed in "${SEEDS[@]}"; do
        gpu_idx=$((job_idx % NUM_GPUS))
        gpu="${GPUS[$gpu_idx]}"
        session="acr-${suite}-s${seed}"
        logfile="logs/eval-acr-${suite}-tau${CONFORMAL_TAU}-seed${seed}.log"

        cmd="cd ${PROJECT_DIR} && CUDA_VISIBLE_DEVICES=${gpu} python -u src/evaluate.py \
    --mode adaptive_conformal_crm \
    --model smolvla \
    --crm_checkpoint ${CRM_CKPT} \
    --benchmark ${suite} \
    --seed ${seed} \
    --n_rollouts ${N_ROLLOUTS} \
    --conformal_threshold ${CONFORMAL_TAU} \
    2>&1 | tee ${logfile}; exit \${PIPESTATUS[0]}"

        echo "[deploy] GPU=${gpu} suite=${suite} seed=${seed} → tmux:${session}"
        tmux new-session -d -s "$session" "$cmd" 2>/dev/null || {
            echo "WARN: session ${session} already exists, killing and recreating"
            tmux kill-session -t "$session" 2>/dev/null || true
            tmux new-session -d -s "$session" "$cmd"
        }

        job_idx=$((job_idx + 1))

        # If we've filled all GPUs, wait before next batch
        if [ $((job_idx % NUM_GPUS)) -eq 0 ] && [ $job_idx -lt 9 ]; then
            echo "[deploy] Batch of ${NUM_GPUS} launched. Next batch will share GPUs (tmux handles scheduling)."
        fi
    done
done

echo ""
echo "[deploy] All ${job_idx} jobs launched."
echo "[deploy] Monitor: tmux ls"
echo "[deploy] Attach:  tmux a -t acr-object-s42"
echo "[deploy] Results: ls -la ${PROJECT_DIR}/logs/eval_*adaptive_conformal_crm*"
echo ""
echo "Expected output files:"
for suite in "${SUITES[@]}"; do
    for seed in "${SEEDS[@]}"; do
        echo "  logs/eval_${suite}_adaptive_conformal_crm_tau${CONFORMAL_TAU}_seed${seed}.json"
    done
done
