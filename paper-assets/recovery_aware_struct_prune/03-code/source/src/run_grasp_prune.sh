#!/bin/bash
# End-to-end GraSP baseline: scoring + pruning + optional GRPO recovery.
# Usage: bash src/run_grasp_prune.sh <sparsity_pct> <gpu_id>
# Example: bash src/run_grasp_prune.sh 20 0

set -euo pipefail

SPARSITY_PCT=${1:?Usage: run_grasp_prune.sh <sparsity_pct> <gpu_id>}
GPU=${2:?Usage: run_grasp_prune.sh <sparsity_pct> <gpu_id>}

cd /root/recovery_aware_struct_prune

MODEL_PATH="/root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B"
SPARSITY_FRAC=$(python3 -c "print(${SPARSITY_PCT}/100)")
SCORES_PATH="/root/autodl-tmp/recovery_aware_struct_prune/scores/grasp_scores.pt"
OUTPUT_PATH="/root/autodl-tmp/pruned_grasp_${SPARSITY_PCT}"
LOG_DIR="/root/recovery_aware_struct_prune/logs"

mkdir -p "$LOG_DIR"
mkdir -p "$(dirname "$SCORES_PATH")"

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base

echo "=== GraSP Baseline Pruning ==="
echo "Sparsity: ${SPARSITY_PCT}%"
echo "GPU:      $GPU"
echo "Model:    $MODEL_PATH"
echo "Output:   $OUTPUT_PATH"
echo "=============================="

# Phase 1: Compute GraSP scores
if [ ! -f "$SCORES_PATH" ]; then
    echo "--- Phase 1: Computing GraSP scores ---"
    CUDA_VISIBLE_DEVICES=$GPU python src/grasp_scoring.py \
        --model_path "$MODEL_PATH" \
        --output_path "$SCORES_PATH" \
        --n_samples 64 \
        --seed 42 \
        2>&1 | tee "${LOG_DIR}/grasp_scoring.log"
else
    echo "--- Phase 1: GraSP scores already exist at $SCORES_PATH, skipping ---"
fi

# Phase 2: Prune with GraSP scores (uses standard mode — no recoverability penalty)
echo "--- Phase 2: Pruning with GraSP scores ---"
CUDA_VISIBLE_DEVICES=$GPU python src/prune.py \
    --model_path "$MODEL_PATH" \
    --importance_path "$SCORES_PATH" \
    --mode standard \
    --sparsity "$SPARSITY_FRAC" \
    --output_path "$OUTPUT_PATH" \
    --seed 42 \
    2>&1 | tee "${LOG_DIR}/grasp_prune_${SPARSITY_PCT}.log"

echo ""
echo "=== Done ==="
echo "Pruned model: $OUTPUT_PATH"
echo "To recover with GRPO:"
echo "  bash src/run_grpo_multiseed.sh grasp ${SPARSITY_PCT} ${GPU} 42"
