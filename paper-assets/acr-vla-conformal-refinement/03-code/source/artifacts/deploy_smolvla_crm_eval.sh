#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════
# SmolVLA CRM 3-Suite Eval Deployment Script
# ═══════════════════════════════════════════════════════════════════════
#
# After train-crm-smolvla-3suite-v1 completes on bjb2-28827 cuda:0.
#
# 18 evals total:
#   - 9 ACR-VLA (crm_obs_only): 3 suites × 3 seeds
#   - 9 VLA-only baseline:      3 suites × 3 seeds
#
# CRM checkpoint: obs_only architecture (unc_dim=0, obs_dim=960)
#   → eval mode must be crm_obs_only (NOT acr_vla which expects unc_dim=40)
#
# GPU allocation (9 GPUs, 1 spare):
#   bjb2-28827: cuda:1,2,3,4,5        (5 GPUs)
#   bjb1-32546: cuda:0,1,2,4          (4 GPUs, skip cuda:3 = π0.5 CRM)
#   bjb1-32546: cuda:5                 (spare / re-run failures)
#
# Each GPU runs ACR-VLA first, then VLA-only (same suite+seed), chained.
# ═══════════════════════════════════════════════════════════════════════

set -euo pipefail

CRM_CKPT="/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt"
PROJECT="/root/acr-vla-conformal-refinement"
ACTIVATE="source /root/miniconda3/etc/profile.d/conda.sh && conda activate base"

# ─── STEP 0: Prerequisites ──────────────────────────────────────────
# Run these BEFORE launching evals.

prerequisite_copy_checkpoint() {
    echo "=== Copying CRM checkpoint to bjb1-32546 ==="
    echo "Run on bjb1-32546:"
    echo "  mkdir -p /root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/"
    echo ""
    echo "Then from a machine that can reach both servers:"
    echo "  scp bjb2-28827:/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt \\"
    echo "      bjb1-32546:/root/autodl-tmp/checkpoints/crm_smolvla_3suite_v1/crm_best.pt"
    echo ""
    echo "Checkpoint is only 1.3MB — should take <1s."
}

# ─── STEP 1: bjb2-28827 sessions (5 GPUs: cuda:1-5) ─────────────────
# Chained: ACR-VLA eval → VLA-only baseline on same GPU

launch_bjb2_28827() {
    local SERVER="bjb2-28827"
    echo "=== Launching on ${SERVER} ==="

    # cuda:1 — object/seed42
    ssh connect.bjb2.seetacloud.com tmux new-session -d -s sv_obj42 \
        "${ACTIVATE} && cd ${PROJECT} && \
        CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py \
            --mode crm_obs_only --model smolvla \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark object --seed 42 \
            --n_rollouts 20 --K 10 --obs_dim 960 \
            --max_steps 280 \
        && \
        CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py \
            --mode vla_only --model smolvla \
            --benchmark object --seed 42 \
            --n_rollouts 20 \
            --max_steps 280"

    # cuda:2 — object/seed43
    ssh connect.bjb2.seetacloud.com tmux new-session -d -s sv_obj43 \
        "${ACTIVATE} && cd ${PROJECT} && \
        CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py \
            --mode crm_obs_only --model smolvla \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark object --seed 43 \
            --n_rollouts 20 --K 10 --obs_dim 960 \
            --max_steps 280 \
        && \
        CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py \
            --mode vla_only --model smolvla \
            --benchmark object --seed 43 \
            --n_rollouts 20 \
            --max_steps 280"

    # cuda:3 — object/seed44
    ssh connect.bjb2.seetacloud.com tmux new-session -d -s sv_obj44 \
        "${ACTIVATE} && cd ${PROJECT} && \
        CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py \
            --mode crm_obs_only --model smolvla \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark object --seed 44 \
            --n_rollouts 20 --K 10 --obs_dim 960 \
            --max_steps 280 \
        && \
        CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py \
            --mode vla_only --model smolvla \
            --benchmark object --seed 44 \
            --n_rollouts 20 \
            --max_steps 280"

    # cuda:4 — spatial/seed42
    ssh connect.bjb2.seetacloud.com tmux new-session -d -s sv_spa42 \
        "${ACTIVATE} && cd ${PROJECT} && \
        CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py \
            --mode crm_obs_only --model smolvla \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark spatial --seed 42 \
            --n_rollouts 20 --K 10 --obs_dim 960 \
            --max_steps 280 \
        && \
        CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py \
            --mode vla_only --model smolvla \
            --benchmark spatial --seed 42 \
            --n_rollouts 20 \
            --max_steps 280"

    # cuda:5 — spatial/seed43
    ssh connect.bjb2.seetacloud.com tmux new-session -d -s sv_spa43 \
        "${ACTIVATE} && cd ${PROJECT} && \
        CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py \
            --mode crm_obs_only --model smolvla \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark spatial --seed 43 \
            --n_rollouts 20 --K 10 --obs_dim 960 \
            --max_steps 280 \
        && \
        CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py \
            --mode vla_only --model smolvla \
            --benchmark spatial --seed 43 \
            --n_rollouts 20 \
            --max_steps 280"

    echo "  ${SERVER}: 5 sessions launched (sv_obj42..44, sv_spa42..43)"
}

# ─── STEP 2: bjb1-32546 sessions (4 GPUs: cuda:0,1,2,4) ─────────────
# cuda:3 occupied by π0.5 CRM training — DO NOT USE

launch_bjb1_32546() {
    local SERVER="bjb1-32546"
    echo "=== Launching on ${SERVER} ==="

    # cuda:0 — spatial/seed44
    ssh connect.bjb1.seetacloud.com tmux new-session -d -s sv_spa44 \
        "${ACTIVATE} && cd ${PROJECT} && \
        CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py \
            --mode crm_obs_only --model smolvla \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark spatial --seed 44 \
            --n_rollouts 20 --K 10 --obs_dim 960 \
            --max_steps 280 \
        && \
        CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py \
            --mode vla_only --model smolvla \
            --benchmark spatial --seed 44 \
            --n_rollouts 20 \
            --max_steps 280"

    # cuda:1 — goal/seed42
    ssh connect.bjb1.seetacloud.com tmux new-session -d -s sv_goal42 \
        "${ACTIVATE} && cd ${PROJECT} && \
        CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py \
            --mode crm_obs_only --model smolvla \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark goal --seed 42 \
            --n_rollouts 20 --K 10 --obs_dim 960 \
            --max_steps 300 \
        && \
        CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py \
            --mode vla_only --model smolvla \
            --benchmark goal --seed 42 \
            --n_rollouts 20 \
            --max_steps 300"

    # cuda:2 — goal/seed43
    ssh connect.bjb1.seetacloud.com tmux new-session -d -s sv_goal43 \
        "${ACTIVATE} && cd ${PROJECT} && \
        CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py \
            --mode crm_obs_only --model smolvla \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark goal --seed 43 \
            --n_rollouts 20 --K 10 --obs_dim 960 \
            --max_steps 300 \
        && \
        CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py \
            --mode vla_only --model smolvla \
            --benchmark goal --seed 43 \
            --n_rollouts 20 \
            --max_steps 300"

    # cuda:4 — goal/seed44
    ssh connect.bjb1.seetacloud.com tmux new-session -d -s sv_goal44 \
        "${ACTIVATE} && cd ${PROJECT} && \
        CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py \
            --mode crm_obs_only --model smolvla \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark goal --seed 44 \
            --n_rollouts 20 --K 10 --obs_dim 960 \
            --max_steps 300 \
        && \
        CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py \
            --mode vla_only --model smolvla \
            --benchmark goal --seed 44 \
            --n_rollouts 20 \
            --max_steps 300"

    echo "  ${SERVER}: 4 sessions launched (sv_spa44, sv_goal42..44)"
}

# ─── STEP 3: Status check commands ───────────────────────────────────

check_status() {
    echo "=== bjb2-28827 ==="
    ssh connect.bjb2.seetacloud.com tmux list-sessions 2>/dev/null
    echo ""
    echo "=== bjb1-32546 ==="
    ssh connect.bjb1.seetacloud.com tmux list-sessions 2>/dev/null
}

# ─── STEP 4: Harvest results ─────────────────────────────────────────

harvest_results() {
    echo "=== Collecting eval results ==="
    echo ""
    echo "bjb2-28827 (object + spatial/42,43):"
    ssh connect.bjb2.seetacloud.com \
        "cat ${PROJECT}/logs/eval_object_crm_obs_only_seed4*.json ${PROJECT}/logs/eval_spatial_crm_obs_only_seed42.json ${PROJECT}/logs/eval_spatial_crm_obs_only_seed43.json 2>/dev/null | grep success_rate"
    ssh connect.bjb2.seetacloud.com \
        "cat ${PROJECT}/logs/eval_object_vla_only_seed4*.json ${PROJECT}/logs/eval_spatial_vla_only_seed42.json ${PROJECT}/logs/eval_spatial_vla_only_seed43.json 2>/dev/null | grep success_rate"
    echo ""
    echo "bjb1-32546 (spatial/44 + goal):"
    ssh connect.bjb1.seetacloud.com \
        "cat ${PROJECT}/logs/eval_spatial_crm_obs_only_seed44.json ${PROJECT}/logs/eval_goal_crm_obs_only_seed4*.json 2>/dev/null | grep success_rate"
    ssh connect.bjb1.seetacloud.com \
        "cat ${PROJECT}/logs/eval_spatial_vla_only_seed44.json ${PROJECT}/logs/eval_goal_vla_only_seed4*.json 2>/dev/null | grep success_rate"
}

# ─── Expected output files ───────────────────────────────────────────
#
# ACR-VLA (crm_obs_only):
#   logs/eval_object_crm_obs_only_seed42.json   (bjb2-28827)
#   logs/eval_object_crm_obs_only_seed43.json   (bjb2-28827)
#   logs/eval_object_crm_obs_only_seed44.json   (bjb2-28827)
#   logs/eval_spatial_crm_obs_only_seed42.json  (bjb2-28827)
#   logs/eval_spatial_crm_obs_only_seed43.json  (bjb2-28827)
#   logs/eval_spatial_crm_obs_only_seed44.json  (bjb1-32546)
#   logs/eval_goal_crm_obs_only_seed42.json     (bjb1-32546)
#   logs/eval_goal_crm_obs_only_seed43.json     (bjb1-32546)
#   logs/eval_goal_crm_obs_only_seed44.json     (bjb1-32546)
#
# VLA-only baseline:
#   logs/eval_object_vla_only_seed42.json       (bjb2-28827)
#   logs/eval_object_vla_only_seed43.json       (bjb2-28827)
#   logs/eval_object_vla_only_seed44.json       (bjb2-28827)
#   logs/eval_spatial_vla_only_seed42.json      (bjb2-28827)
#   logs/eval_spatial_vla_only_seed43.json      (bjb2-28827)
#   logs/eval_spatial_vla_only_seed44.json      (bjb1-32546)
#   logs/eval_goal_vla_only_seed42.json         (bjb1-32546)
#   logs/eval_goal_vla_only_seed43.json         (bjb1-32546)
#   logs/eval_goal_vla_only_seed44.json         (bjb1-32546)

# ─── GPU Assignment Summary ──────────────────────────────────────────
#
# bjb2-28827:
#   cuda:0  — CRM training (DO NOT USE until training completes)
#   cuda:1  — object/seed42 (ACR → VLA)
#   cuda:2  — object/seed43 (ACR → VLA)
#   cuda:3  — object/seed44 (ACR → VLA)
#   cuda:4  — spatial/seed42 (ACR → VLA)
#   cuda:5  — spatial/seed43 (ACR → VLA)
#
# bjb1-32546:
#   cuda:0  — spatial/seed44 (ACR → VLA)
#   cuda:1  — goal/seed42 (ACR → VLA)
#   cuda:2  — goal/seed43 (ACR → VLA)
#   cuda:3  — π0.5 CRM training (DO NOT USE)
#   cuda:4  — goal/seed44 (ACR → VLA)
#   cuda:5  — spare (re-run failures)

# ─── Execution ────────────────────────────────────────────────────────
case "${1:-}" in
    prereq)   prerequisite_copy_checkpoint ;;
    bjb2)     launch_bjb2_28827 ;;
    bjb1)     launch_bjb1_32546 ;;
    all)
        prerequisite_copy_checkpoint
        echo ""
        echo "Press Enter after checkpoint is copied to continue..."
        read -r
        launch_bjb2_28827
        launch_bjb1_32546
        echo ""
        echo "=== All 9 sessions launched (18 evals chained) ==="
        echo "Monitor: bash $0 status"
        ;;
    status)   check_status ;;
    harvest)  harvest_results ;;
    *)
        echo "Usage: $0 {prereq|bjb2|bjb1|all|status|harvest}"
        echo ""
        echo "  prereq  — Print checkpoint copy instructions"
        echo "  bjb2    — Launch 5 sessions on bjb2-28827 (cuda:1-5)"
        echo "  bjb1    — Launch 4 sessions on bjb1-32546 (cuda:0,1,2,4)"
        echo "  all     — Copy checkpoint, then launch all 9 sessions"
        echo "  status  — Check tmux sessions on both servers"
        echo "  harvest — Grep success_rate from result JSONs"
        ;;
esac
