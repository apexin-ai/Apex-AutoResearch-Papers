#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════
# π0.5 CRM 4-Suite Eval Deployment Script
# ═══════════════════════════════════════════════════════════════════════
#
# After crm_unified_4suite_r4 training completes on bjb1-32546 cuda:3.
#
# 36 evals total (3 rounds × 4 suites × 3 seeds):
#   Round 1: crm_obs_only          — always-apply CRM (upper bound)
#   Round 2: adaptive_conformal_crm — Adaptive Conformal (core contribution)
#   Round 3: vla_only              — π0.5 baseline (no CRM)
#
# Each GPU chains all 3 modes for the same suite+seed combo.
#
# ─── KNOWN ISSUE ────────────────────────────────────────────────────
# The CRM checkpoint (crm_unified_4suite_r4) was trained with SmolVLA
# features (obs_dim=960). π0.5 produces 2048D features. evaluate.py
# raises ValueError if --model pi05 --obs_dim 960 with CRM.
#
# Resolution options (pick one before deploying):
#   A) Retrain CRM with π0.5 caches (obs_dim=2048)
#   B) Add obs projection (2048→960) in evaluate.py
#   C) Use --unified_obs_dim 2048 + update the pi05 obs_dim check
#
# The script uses obs_dim=960 as specified. Adjust OBS_DIM below if
# the CRM is retrained with a different obs_dim.
# ────────────────────────────────────────────────────────────────────
#
# GPU allocation (11 GPUs):
#   bjb1-32546: cuda:0,1,2,4,5      (5 GPUs, skip cuda:3 = training)
#   bjb2-28827: cuda:0,1,2,3,4,5    (6 GPUs)
#
# Long suite MUST run on bjb1-32546 (bjb2-28827 has 36min SSH timeout).
# ═══════════════════════════════════════════════════════════════════════

set -euo pipefail

CRM_CKPT="/root/autodl-tmp/checkpoints/crm_unified_4suite_r4/crm_best.pt"
PROJECT="/root/acr-vla-conformal-refinement"
ACTIVATE="source /root/miniconda3/etc/profile.d/conda.sh && conda activate base"

MODEL="pi05"
N_ACTION_STEPS=10
OBS_DIM=960
K=10
N_ROLLOUTS=20
CONFORMAL_TAU=0.074855

# ─── STEP 0: Prerequisites ──────────────────────────────────────────

prerequisite_checks() {
    echo "=== Pre-flight checks ==="
    echo ""
    echo "1. Verify CRM training completed:"
    echo "   ssh connect.bjb1.seetacloud.com tail -5 /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/train.log"
    echo ""
    echo "2. Verify CRM checkpoint:"
    echo "   ssh connect.bjb1.seetacloud.com ls -la ${CRM_CKPT}"
    echo ""
    echo "3. Copy CRM checkpoint to bjb2-28827 (~1.3MB):"
    echo "   ssh connect.bjb2.seetacloud.com mkdir -p /root/autodl-tmp/checkpoints/crm_unified_4suite_r4/"
    echo "   scp bjb1-32546:${CRM_CKPT} bjb2-28827:${CRM_CKPT}"
    echo ""
    echo "4. Verify π0.5 model on both servers:"
    echo "   ssh connect.bjb1.seetacloud.com ls /root/autodl-tmp/models/pi05_libero_finetuned/"
    echo "   ssh connect.bjb2.seetacloud.com ls /root/autodl-tmp/models/pi05_libero_finetuned/"
    echo ""
    echo "5. Sync code on both servers:"
    echo "   ssh connect.bjb1.seetacloud.com 'cd ${PROJECT} && git pull'"
    echo "   ssh connect.bjb2.seetacloud.com 'cd ${PROJECT} && git pull'"
}

# ─── STEP 1: bjb1-32546 sessions (5 GPUs: cuda:0,1,2,4,5) ─────────
# Long suite MUST run here. cuda:3 occupied by CRM training.

launch_bjb1_32546() {
    local SERVER="bjb1-32546"
    echo "=== Launching on ${SERVER} ==="

    # cuda:0 — long/seed42: crm_obs_only → adaptive_conformal_crm → vla_only
    ssh connect.bjb1.seetacloud.com tmux new-session -d -s pi05_long42 \
        "${ACTIVATE} && cd ${PROJECT} && \
        CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py \
            --mode crm_obs_only --model ${MODEL} \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark long --seed 42 \
            --n_rollouts ${N_ROLLOUTS} --K ${K} --obs_dim ${OBS_DIM} \
            --n_action_steps ${N_ACTION_STEPS} \
            --max_steps 520 \
        && \
        CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py \
            --mode adaptive_conformal_crm --model ${MODEL} \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark long --seed 42 \
            --n_rollouts ${N_ROLLOUTS} --K ${K} --obs_dim ${OBS_DIM} \
            --n_action_steps ${N_ACTION_STEPS} \
            --conformal_threshold ${CONFORMAL_TAU} \
            --max_steps 520 \
        && \
        CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py \
            --mode vla_only --model ${MODEL} \
            --benchmark long --seed 42 \
            --n_rollouts ${N_ROLLOUTS} \
            --n_action_steps ${N_ACTION_STEPS} \
            --max_steps 520"

    # cuda:1 — long/seed43
    ssh connect.bjb1.seetacloud.com tmux new-session -d -s pi05_long43 \
        "${ACTIVATE} && cd ${PROJECT} && \
        CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py \
            --mode crm_obs_only --model ${MODEL} \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark long --seed 43 \
            --n_rollouts ${N_ROLLOUTS} --K ${K} --obs_dim ${OBS_DIM} \
            --n_action_steps ${N_ACTION_STEPS} \
            --max_steps 520 \
        && \
        CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py \
            --mode adaptive_conformal_crm --model ${MODEL} \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark long --seed 43 \
            --n_rollouts ${N_ROLLOUTS} --K ${K} --obs_dim ${OBS_DIM} \
            --n_action_steps ${N_ACTION_STEPS} \
            --conformal_threshold ${CONFORMAL_TAU} \
            --max_steps 520 \
        && \
        CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py \
            --mode vla_only --model ${MODEL} \
            --benchmark long --seed 43 \
            --n_rollouts ${N_ROLLOUTS} \
            --n_action_steps ${N_ACTION_STEPS} \
            --max_steps 520"

    # cuda:2 — long/seed44
    ssh connect.bjb1.seetacloud.com tmux new-session -d -s pi05_long44 \
        "${ACTIVATE} && cd ${PROJECT} && \
        CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py \
            --mode crm_obs_only --model ${MODEL} \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark long --seed 44 \
            --n_rollouts ${N_ROLLOUTS} --K ${K} --obs_dim ${OBS_DIM} \
            --n_action_steps ${N_ACTION_STEPS} \
            --max_steps 520 \
        && \
        CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py \
            --mode adaptive_conformal_crm --model ${MODEL} \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark long --seed 44 \
            --n_rollouts ${N_ROLLOUTS} --K ${K} --obs_dim ${OBS_DIM} \
            --n_action_steps ${N_ACTION_STEPS} \
            --conformal_threshold ${CONFORMAL_TAU} \
            --max_steps 520 \
        && \
        CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py \
            --mode vla_only --model ${MODEL} \
            --benchmark long --seed 44 \
            --n_rollouts ${N_ROLLOUTS} \
            --n_action_steps ${N_ACTION_STEPS} \
            --max_steps 520"

    # cuda:4 — object/seed42
    ssh connect.bjb1.seetacloud.com tmux new-session -d -s pi05_obj42 \
        "${ACTIVATE} && cd ${PROJECT} && \
        CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py \
            --mode crm_obs_only --model ${MODEL} \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark object --seed 42 \
            --n_rollouts ${N_ROLLOUTS} --K ${K} --obs_dim ${OBS_DIM} \
            --n_action_steps ${N_ACTION_STEPS} \
            --max_steps 280 \
        && \
        CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py \
            --mode adaptive_conformal_crm --model ${MODEL} \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark object --seed 42 \
            --n_rollouts ${N_ROLLOUTS} --K ${K} --obs_dim ${OBS_DIM} \
            --n_action_steps ${N_ACTION_STEPS} \
            --conformal_threshold ${CONFORMAL_TAU} \
            --max_steps 280 \
        && \
        CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py \
            --mode vla_only --model ${MODEL} \
            --benchmark object --seed 42 \
            --n_rollouts ${N_ROLLOUTS} \
            --n_action_steps ${N_ACTION_STEPS} \
            --max_steps 280"

    # cuda:5 — object/seed43
    ssh connect.bjb1.seetacloud.com tmux new-session -d -s pi05_obj43 \
        "${ACTIVATE} && cd ${PROJECT} && \
        CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py \
            --mode crm_obs_only --model ${MODEL} \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark object --seed 43 \
            --n_rollouts ${N_ROLLOUTS} --K ${K} --obs_dim ${OBS_DIM} \
            --n_action_steps ${N_ACTION_STEPS} \
            --max_steps 280 \
        && \
        CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py \
            --mode adaptive_conformal_crm --model ${MODEL} \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark object --seed 43 \
            --n_rollouts ${N_ROLLOUTS} --K ${K} --obs_dim ${OBS_DIM} \
            --n_action_steps ${N_ACTION_STEPS} \
            --conformal_threshold ${CONFORMAL_TAU} \
            --max_steps 280 \
        && \
        CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py \
            --mode vla_only --model ${MODEL} \
            --benchmark object --seed 43 \
            --n_rollouts ${N_ROLLOUTS} \
            --n_action_steps ${N_ACTION_STEPS} \
            --max_steps 280"

    echo "  ${SERVER}: 5 sessions launched (pi05_long42..44, pi05_obj42..43)"
}

# ─── STEP 2: bjb2-28827 sessions (6 GPUs: cuda:0-5) ────────────────
# No long suite here (36min SSH timeout).
# cuda:5 double-chains goal/43 then goal/44.

launch_bjb2_28827() {
    local SERVER="bjb2-28827"
    echo "=== Launching on ${SERVER} ==="

    # cuda:0 — object/seed44
    ssh connect.bjb2.seetacloud.com tmux new-session -d -s pi05_obj44 \
        "${ACTIVATE} && cd ${PROJECT} && \
        CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py \
            --mode crm_obs_only --model ${MODEL} \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark object --seed 44 \
            --n_rollouts ${N_ROLLOUTS} --K ${K} --obs_dim ${OBS_DIM} \
            --n_action_steps ${N_ACTION_STEPS} \
            --max_steps 280 \
        && \
        CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py \
            --mode adaptive_conformal_crm --model ${MODEL} \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark object --seed 44 \
            --n_rollouts ${N_ROLLOUTS} --K ${K} --obs_dim ${OBS_DIM} \
            --n_action_steps ${N_ACTION_STEPS} \
            --conformal_threshold ${CONFORMAL_TAU} \
            --max_steps 280 \
        && \
        CUDA_VISIBLE_DEVICES=0 python -u src/evaluate.py \
            --mode vla_only --model ${MODEL} \
            --benchmark object --seed 44 \
            --n_rollouts ${N_ROLLOUTS} \
            --n_action_steps ${N_ACTION_STEPS} \
            --max_steps 280"

    # cuda:1 — spatial/seed42
    ssh connect.bjb2.seetacloud.com tmux new-session -d -s pi05_spa42 \
        "${ACTIVATE} && cd ${PROJECT} && \
        CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py \
            --mode crm_obs_only --model ${MODEL} \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark spatial --seed 42 \
            --n_rollouts ${N_ROLLOUTS} --K ${K} --obs_dim ${OBS_DIM} \
            --n_action_steps ${N_ACTION_STEPS} \
            --max_steps 280 \
        && \
        CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py \
            --mode adaptive_conformal_crm --model ${MODEL} \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark spatial --seed 42 \
            --n_rollouts ${N_ROLLOUTS} --K ${K} --obs_dim ${OBS_DIM} \
            --n_action_steps ${N_ACTION_STEPS} \
            --conformal_threshold ${CONFORMAL_TAU} \
            --max_steps 280 \
        && \
        CUDA_VISIBLE_DEVICES=1 python -u src/evaluate.py \
            --mode vla_only --model ${MODEL} \
            --benchmark spatial --seed 42 \
            --n_rollouts ${N_ROLLOUTS} \
            --n_action_steps ${N_ACTION_STEPS} \
            --max_steps 280"

    # cuda:2 — spatial/seed43
    ssh connect.bjb2.seetacloud.com tmux new-session -d -s pi05_spa43 \
        "${ACTIVATE} && cd ${PROJECT} && \
        CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py \
            --mode crm_obs_only --model ${MODEL} \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark spatial --seed 43 \
            --n_rollouts ${N_ROLLOUTS} --K ${K} --obs_dim ${OBS_DIM} \
            --n_action_steps ${N_ACTION_STEPS} \
            --max_steps 280 \
        && \
        CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py \
            --mode adaptive_conformal_crm --model ${MODEL} \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark spatial --seed 43 \
            --n_rollouts ${N_ROLLOUTS} --K ${K} --obs_dim ${OBS_DIM} \
            --n_action_steps ${N_ACTION_STEPS} \
            --conformal_threshold ${CONFORMAL_TAU} \
            --max_steps 280 \
        && \
        CUDA_VISIBLE_DEVICES=2 python -u src/evaluate.py \
            --mode vla_only --model ${MODEL} \
            --benchmark spatial --seed 43 \
            --n_rollouts ${N_ROLLOUTS} \
            --n_action_steps ${N_ACTION_STEPS} \
            --max_steps 280"

    # cuda:3 — spatial/seed44
    ssh connect.bjb2.seetacloud.com tmux new-session -d -s pi05_spa44 \
        "${ACTIVATE} && cd ${PROJECT} && \
        CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py \
            --mode crm_obs_only --model ${MODEL} \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark spatial --seed 44 \
            --n_rollouts ${N_ROLLOUTS} --K ${K} --obs_dim ${OBS_DIM} \
            --n_action_steps ${N_ACTION_STEPS} \
            --max_steps 280 \
        && \
        CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py \
            --mode adaptive_conformal_crm --model ${MODEL} \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark spatial --seed 44 \
            --n_rollouts ${N_ROLLOUTS} --K ${K} --obs_dim ${OBS_DIM} \
            --n_action_steps ${N_ACTION_STEPS} \
            --conformal_threshold ${CONFORMAL_TAU} \
            --max_steps 280 \
        && \
        CUDA_VISIBLE_DEVICES=3 python -u src/evaluate.py \
            --mode vla_only --model ${MODEL} \
            --benchmark spatial --seed 44 \
            --n_rollouts ${N_ROLLOUTS} \
            --n_action_steps ${N_ACTION_STEPS} \
            --max_steps 280"

    # cuda:4 — goal/seed42
    ssh connect.bjb2.seetacloud.com tmux new-session -d -s pi05_goal42 \
        "${ACTIVATE} && cd ${PROJECT} && \
        CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py \
            --mode crm_obs_only --model ${MODEL} \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark goal --seed 42 \
            --n_rollouts ${N_ROLLOUTS} --K ${K} --obs_dim ${OBS_DIM} \
            --n_action_steps ${N_ACTION_STEPS} \
            --max_steps 300 \
        && \
        CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py \
            --mode adaptive_conformal_crm --model ${MODEL} \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark goal --seed 42 \
            --n_rollouts ${N_ROLLOUTS} --K ${K} --obs_dim ${OBS_DIM} \
            --n_action_steps ${N_ACTION_STEPS} \
            --conformal_threshold ${CONFORMAL_TAU} \
            --max_steps 300 \
        && \
        CUDA_VISIBLE_DEVICES=4 python -u src/evaluate.py \
            --mode vla_only --model ${MODEL} \
            --benchmark goal --seed 42 \
            --n_rollouts ${N_ROLLOUTS} \
            --n_action_steps ${N_ACTION_STEPS} \
            --max_steps 300"

    # cuda:5 — goal/seed43 → goal/seed44 (6 evals, bottleneck GPU)
    ssh connect.bjb2.seetacloud.com tmux new-session -d -s pi05_goal43_44 \
        "${ACTIVATE} && cd ${PROJECT} && \
        CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py \
            --mode crm_obs_only --model ${MODEL} \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark goal --seed 43 \
            --n_rollouts ${N_ROLLOUTS} --K ${K} --obs_dim ${OBS_DIM} \
            --n_action_steps ${N_ACTION_STEPS} \
            --max_steps 300 \
        && \
        CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py \
            --mode adaptive_conformal_crm --model ${MODEL} \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark goal --seed 43 \
            --n_rollouts ${N_ROLLOUTS} --K ${K} --obs_dim ${OBS_DIM} \
            --n_action_steps ${N_ACTION_STEPS} \
            --conformal_threshold ${CONFORMAL_TAU} \
            --max_steps 300 \
        && \
        CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py \
            --mode vla_only --model ${MODEL} \
            --benchmark goal --seed 43 \
            --n_rollouts ${N_ROLLOUTS} \
            --n_action_steps ${N_ACTION_STEPS} \
            --max_steps 300 \
        && \
        CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py \
            --mode crm_obs_only --model ${MODEL} \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark goal --seed 44 \
            --n_rollouts ${N_ROLLOUTS} --K ${K} --obs_dim ${OBS_DIM} \
            --n_action_steps ${N_ACTION_STEPS} \
            --max_steps 300 \
        && \
        CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py \
            --mode adaptive_conformal_crm --model ${MODEL} \
            --crm_checkpoint ${CRM_CKPT} \
            --benchmark goal --seed 44 \
            --n_rollouts ${N_ROLLOUTS} --K ${K} --obs_dim ${OBS_DIM} \
            --n_action_steps ${N_ACTION_STEPS} \
            --conformal_threshold ${CONFORMAL_TAU} \
            --max_steps 300 \
        && \
        CUDA_VISIBLE_DEVICES=5 python -u src/evaluate.py \
            --mode vla_only --model ${MODEL} \
            --benchmark goal --seed 44 \
            --n_rollouts ${N_ROLLOUTS} \
            --n_action_steps ${N_ACTION_STEPS} \
            --max_steps 300"

    echo "  ${SERVER}: 6 sessions launched (pi05_obj44, pi05_spa42..44, pi05_goal42, pi05_goal43_44)"
}

# ─── STEP 3: Status check ───────────────────────────────────────────

check_status() {
    echo "=== bjb1-32546 ==="
    ssh connect.bjb1.seetacloud.com tmux list-sessions 2>/dev/null
    echo ""
    echo "=== bjb2-28827 ==="
    ssh connect.bjb2.seetacloud.com tmux list-sessions 2>/dev/null
}

# ─── STEP 4: Harvest results ────────────────────────────────────────

harvest_results() {
    echo "=== π0.5 CRM Eval Results ==="
    echo ""

    echo "--- crm_obs_only (always-apply CRM) ---"
    ssh connect.bjb1.seetacloud.com \
        "grep -h success_rate ${PROJECT}/logs/eval_*_crm_obs_only_pi05_seed4*.json 2>/dev/null"
    ssh connect.bjb2.seetacloud.com \
        "grep -h success_rate ${PROJECT}/logs/eval_*_crm_obs_only_pi05_seed4*.json 2>/dev/null"
    echo ""

    echo "--- adaptive_conformal_crm (Adaptive Conformal) ---"
    ssh connect.bjb1.seetacloud.com \
        "grep -h success_rate ${PROJECT}/logs/eval_*_adaptive_conformal_crm_pi05_tau*_seed4*.json 2>/dev/null"
    ssh connect.bjb2.seetacloud.com \
        "grep -h success_rate ${PROJECT}/logs/eval_*_adaptive_conformal_crm_pi05_tau*_seed4*.json 2>/dev/null"
    echo ""

    echo "--- vla_only (π0.5 baseline) ---"
    ssh connect.bjb1.seetacloud.com \
        "grep -h success_rate ${PROJECT}/logs/eval_*_vla_only_pi05_seed4*.json 2>/dev/null"
    ssh connect.bjb2.seetacloud.com \
        "grep -h success_rate ${PROJECT}/logs/eval_*_vla_only_pi05_seed4*.json 2>/dev/null"
}

# ─── Expected output files ───────────────────────────────────────────
#
# crm_obs_only (12 files):
#   logs/eval_{object,spatial,goal,long}_crm_obs_only_pi05_seed{42,43,44}.json
#
# adaptive_conformal_crm (12 files):
#   logs/eval_{object,spatial,goal,long}_adaptive_conformal_crm_pi05_tau0.074855_seed{42,43,44}.json
#
# vla_only (12 files):
#   logs/eval_{object,spatial,goal,long}_vla_only_pi05_seed{42,43,44}.json

# ─── GPU Assignment Summary ──────────────────────────────────────────
#
# bjb1-32546:
#   cuda:0  — long/seed42   (crm_obs_only → adaptive_conformal → vla_only)
#   cuda:1  — long/seed43   (crm_obs_only → adaptive_conformal → vla_only)
#   cuda:2  — long/seed44   (crm_obs_only → adaptive_conformal → vla_only)
#   cuda:3  — CRM training (DO NOT USE)
#   cuda:4  — object/seed42 (crm_obs_only → adaptive_conformal → vla_only)
#   cuda:5  — object/seed43 (crm_obs_only → adaptive_conformal → vla_only)
#
# bjb2-28827:
#   cuda:0  — object/seed44  (crm_obs_only → adaptive_conformal → vla_only)
#   cuda:1  — spatial/seed42 (crm_obs_only → adaptive_conformal → vla_only)
#   cuda:2  — spatial/seed43 (crm_obs_only → adaptive_conformal → vla_only)
#   cuda:3  — spatial/seed44 (crm_obs_only → adaptive_conformal → vla_only)
#   cuda:4  — goal/seed42    (crm_obs_only → adaptive_conformal → vla_only)
#   cuda:5  — goal/seed43    (3 modes) → goal/seed44 (3 modes) [bottleneck]

# ─── Execution ────────────────────────────────────────────────────────
case "${1:-}" in
    prereq)   prerequisite_checks ;;
    bjb1)     launch_bjb1_32546 ;;
    bjb2)     launch_bjb2_28827 ;;
    all)
        prerequisite_checks
        echo ""
        echo "Press Enter after pre-flight checks pass..."
        read -r
        launch_bjb1_32546
        launch_bjb2_28827
        echo ""
        echo "=== All 11 sessions launched (36 evals chained) ==="
        echo "Monitor: bash $0 status"
        ;;
    status)   check_status ;;
    harvest)  harvest_results ;;
    *)
        echo "Usage: $0 {prereq|bjb1|bjb2|all|status|harvest}"
        echo ""
        echo "  prereq  — Print pre-flight check instructions"
        echo "  bjb1    — Launch 5 sessions on bjb1-32546 (long×3 + object×2)"
        echo "  bjb2    — Launch 6 sessions on bjb2-28827 (object×1 + spatial×3 + goal×3)"
        echo "  all     — Run prereq, then launch all 11 sessions (36 evals)"
        echo "  status  — Check tmux sessions on both servers"
        echo "  harvest — Grep success_rate from result JSONs"
        ;;
esac
