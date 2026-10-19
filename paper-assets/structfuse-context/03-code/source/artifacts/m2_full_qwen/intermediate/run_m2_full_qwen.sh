#!/bin/bash
set -eo pipefail

export CUDA_VISIBLE_DEVICES=0
export PYTHONUNBUFFERED=1
export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True
export WANDB_MODE=offline
export WANDB_CONSOLE=off
export WANDB_DIR=/root/autodl-tmp/structfuse/wandb_logs/
export HF_HOME=/root/autodl-tmp/.hf_cache
export TRANSFORMERS_OFFLINE=1
export HF_HUB_OFFLINE=1

trap 'echo "INTERRUPTED at $(date), cleaning up..."; kill 0; exit 1' INT TERM

DATA_DIR="/root/autodl-tmp/structfuse/full_m2_training_data"
OUT_BASE="/root/autodl-tmp/structfuse/checkpoints/m2_full_qwen"
LOG_DIR="/root/runs/m2_full_qwen"
MODEL="/root/autodl-tmp/structfuse/models/Qwen/Qwen2.5-Coder-3B"
TRAIN_SCRIPT="/root/structfuse/training/train.py"

STRATEGIES=("random" "embedding_distance" "dataflow_aware")
SEEDS=(42 43 44)

mkdir -p "${LOG_DIR}" "${OUT_BASE}"

TOTAL_RUNS=9
RUN_NUM=0

for STRATEGY in "${STRATEGIES[@]}"; do
    for SEED in "${SEEDS[@]}"; do
        RUN_NUM=$((RUN_NUM + 1))
        TAG="${STRATEGY}_s${SEED}"
        LOG_FILE="${LOG_DIR}/${TAG}.log"

        echo "=========================================="
        echo "[${RUN_NUM}/${TOTAL_RUNS}] Starting: ${TAG} at $(date)"
        echo "=========================================="

        TRAIN_FILE="${DATA_DIR}/train_${STRATEGY}_s${SEED}.jsonl"
        VAL_FILE="${DATA_DIR}/val_${STRATEGY}_s${SEED}.jsonl"
        OUT_DIR="${OUT_BASE}/${TAG}"

        if [ ! -f "${TRAIN_FILE}" ]; then
            echo "ERROR: Train file not found: ${TRAIN_FILE}"
            exit 1
        fi
        if [ ! -f "${VAL_FILE}" ]; then
            echo "ERROR: Val file not found: ${VAL_FILE}"
            exit 1
        fi

        EXTRA_ARGS=""
        if [ "${STRATEGY}" = "dataflow_aware" ]; then
            EXTRA_ARGS="--dataflow-graph-file ${DATA_DIR}/dataflow_graph.json"
        fi

        python "${TRAIN_SCRIPT}" \
            --model-name "${MODEL}" \
            --train-file "${TRAIN_FILE}" \
            --val-file "${VAL_FILE}" \
            --output-dir "${OUT_DIR}" \
            --hard-negative-strategy "${STRATEGY}" \
            --learning-rate 2e-5 \
            --temperature 0.07 \
            --batch-size 8 \
            --num-epochs 3 \
            --num-negatives 7 \
            --hard-negative-ratio 0.5 \
            --use-lora \
            --gradient-checkpointing \
            --max-seq-length 2048 \
            --seed "${SEED}" \
            --eval-steps 500 \
            --save-steps 1000 \
            --wandb-project structfuse \
            --wandb-run-name "m2_full_${TAG}" \
            ${EXTRA_ARGS} \
            > "${LOG_FILE}" 2>&1

        TRAIN_EXIT=$?
        if [ ${TRAIN_EXIT} -ne 0 ]; then
            echo "ERROR: ${TAG} failed with exit code ${TRAIN_EXIT}"
            echo "Last 20 lines of log:"
            tail -20 "${LOG_FILE}"
            exit ${TRAIN_EXIT}
        fi

        echo "[${RUN_NUM}/${TOTAL_RUNS}] Completed: ${TAG} at $(date)"

        grep -E "\[Final eval\]|\[eval@" "${LOG_FILE}" | tail -3

        if [ -f "${OUT_DIR}/best_by_val_loss/training_config.json" ]; then
            echo "  best_by_val_loss checkpoint saved"
        fi
        if [ -f "${OUT_DIR}/best_by_recall_at_1/training_config.json" ]; then
            echo "  best_by_recall_at_1 checkpoint saved"
        fi

        find "${OUT_DIR}" -maxdepth 1 -name "checkpoint-*" -type d -exec rm -rf {} + 2>/dev/null || true

        echo ""
    done
done

echo "=========================================="
echo "ALL 9 RUNS COMPLETED at $(date)"
echo "=========================================="