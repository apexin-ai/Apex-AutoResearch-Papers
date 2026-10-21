#!/bin/bash
# run_pending_experiments.sh
# Master launch script for pending supplementary experiments.
# Usage: bash run_pending_experiments.sh [group] [experiment_id]
#   group: "long-n5" | "adaptive-eps" | "all" (default: all)
#   experiment_id: run a single experiment by ID (optional)
#
# Prerequisites:
#   - Conda env activated: source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
#   - CRM checkpoints present at /root/autodl-tmp/checkpoints/
#   - Project code at /root/acr-vla-conformal-refinement/
#   - For adaptive-eps group: run patch_adaptive_epsilon.py first

set -euo pipefail

PROJECT_DIR="/root/acr-vla-conformal-refinement"
EVAL_SCRIPT="${PROJECT_DIR}/src/evaluate.py"
LOG_DIR="${PROJECT_DIR}/logs/pending_experiments"
mkdir -p "${LOG_DIR}"

CRM_SMOLVLA="/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt"

GROUP="${1:-all}"
SINGLE_ID="${2:-}"

run_experiment() {
    local exp_id="$1"
    local log_file="${LOG_DIR}/${exp_id}.log"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Starting ${exp_id} ..."
    shift
    python "${EVAL_SCRIPT}" "$@" 2>&1 | tee "${log_file}"
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] Finished ${exp_id}"
}

# ============================================================
# Group 1: SmolVLA Long n=5 extension (4 experiments)
# Extends Table 1 Long from n=3 (s42/s43/s44) to n=5
# Note: Adaptive Long s45/s46 already completed in registry
# ============================================================

run_smolvla_vla_only_long_s45() {
    run_experiment "smolvla-vla-only-long-s45" \
        --mode vla_only \
        --model smolvla \
        --benchmark long \
        --seed 45 \
        --max_steps 520 \
        --n_rollouts 20
}

run_smolvla_vla_only_long_s46() {
    run_experiment "smolvla-vla-only-long-s46" \
        --mode vla_only \
        --model smolvla \
        --benchmark long \
        --seed 46 \
        --max_steps 520 \
        --n_rollouts 20
}

run_smolvla_crm_long_s45() {
    run_experiment "smolvla-crm-long-s45" \
        --mode crm_obs_only \
        --model smolvla \
        --benchmark long \
        --seed 45 \
        --K 2 \
        --obs_dim 960 \
        --max_steps 520 \
        --n_rollouts 20 \
        --conformal_threshold 0.001 \
        --crm_checkpoint "${CRM_SMOLVLA}" \
        --max_correction_norm 0.2
}

run_smolvla_crm_long_s46() {
    run_experiment "smolvla-crm-long-s46" \
        --mode crm_obs_only \
        --model smolvla \
        --benchmark long \
        --seed 46 \
        --K 2 \
        --obs_dim 960 \
        --max_steps 520 \
        --n_rollouts 20 \
        --conformal_threshold 0.001 \
        --crm_checkpoint "${CRM_SMOLVLA}" \
        --max_correction_norm 0.2
}

# ============================================================
# Group 2: Adaptive Epsilon validation (2 experiments)
# Requires: patch_adaptive_epsilon.py applied first
# ============================================================

run_smolvla_adaptive_eps_spatial_s42() {
    run_experiment "smolvla-adaptive-eps-spatial-s42" \
        --mode adaptive_conformal_crm \
        --adaptive_epsilon \
        --model smolvla \
        --benchmark spatial \
        --seed 42 \
        --K 2 \
        --obs_dim 960 \
        --max_steps 280 \
        --n_rollouts 20 \
        --conformal_threshold 0.25 \
        --crm_checkpoint "${CRM_SMOLVLA}" \
        --max_correction_norm 0.2
}

run_smolvla_adaptive_eps_object_s42() {
    run_experiment "smolvla-adaptive-eps-object-s42" \
        --mode adaptive_conformal_crm \
        --adaptive_epsilon \
        --model smolvla \
        --benchmark object \
        --seed 42 \
        --K 2 \
        --obs_dim 960 \
        --max_steps 280 \
        --n_rollouts 20 \
        --conformal_threshold 0.25 \
        --crm_checkpoint "${CRM_SMOLVLA}" \
        --max_correction_norm 0.2
}

# ============================================================
# Dispatch
# ============================================================

if [[ -n "${SINGLE_ID}" ]]; then
    case "${SINGLE_ID}" in
        smolvla-vla-only-long-s45)         run_smolvla_vla_only_long_s45 ;;
        smolvla-vla-only-long-s46)         run_smolvla_vla_only_long_s46 ;;
        smolvla-crm-long-s45)             run_smolvla_crm_long_s45 ;;
        smolvla-crm-long-s46)             run_smolvla_crm_long_s46 ;;
        smolvla-adaptive-eps-spatial-s42)   run_smolvla_adaptive_eps_spatial_s42 ;;
        smolvla-adaptive-eps-object-s42)   run_smolvla_adaptive_eps_object_s42 ;;
        *) echo "Unknown experiment: ${SINGLE_ID}"; exit 1 ;;
    esac
    exit 0
fi

if [[ "${GROUP}" == "long-n5" || "${GROUP}" == "all" ]]; then
    echo "=== Group 1: SmolVLA Long n=5 extension ==="
    run_smolvla_vla_only_long_s45
    run_smolvla_vla_only_long_s46
    run_smolvla_crm_long_s45
    run_smolvla_crm_long_s46
fi

if [[ "${GROUP}" == "adaptive-eps" || "${GROUP}" == "all" ]]; then
    echo "=== Group 2: Adaptive Epsilon validation ==="
    echo "NOTE: Ensure patch_adaptive_epsilon.py has been applied first!"
    run_smolvla_adaptive_eps_spatial_s42
    run_smolvla_adaptive_eps_object_s42
fi

echo "All experiments complete."
