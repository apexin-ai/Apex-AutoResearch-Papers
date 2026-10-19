#!/bin/bash
# ACIB v5_div_reg seed1 eval commands
# Generated: 2026-05-16
#
# Prerequisites:
#   - seed1 training (acib_v5_div_reg) must be finished (20000 steps)
#   - Final checkpoint at /root/acib/outputs/acib_v5_div_reg/checkpoint-20000/checkpoint.pt
#   - GPU 0 free (kill training process first if still running)
#
# C001 safety check: ALWAYS run before launching eval:
#   ps aux | grep acib_v5_div_reg | grep -v grep
#   # Kill any leftover training processes writing to the same output_dir

# =============================================================================
# Option A: All 4 suites in one command (recommended — caches policy across suites)
# =============================================================================
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/acib && \
CUDA_VISIBLE_DEVICES=0 python3 -u scripts/eval_acib.py \
    --checkpoint_dir /root/acib/outputs/acib_v5_div_reg \
    --base_model lerobot/smolvla_libero \
    --suites libero_spatial libero_object libero_goal libero_10 \
    --n_episodes 50 \
    --gpu 0 \
    --seed 42 \
    --out_dir /root/acib/outputs/acib_v5_div_reg_eval

# =============================================================================
# Option B: Individual suite commands (if you need to run selectively)
# =============================================================================

# Suite: libero_spatial
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/acib && \
CUDA_VISIBLE_DEVICES=0 python3 -u scripts/eval_acib.py \
    --checkpoint_dir /root/acib/outputs/acib_v5_div_reg \
    --base_model lerobot/smolvla_libero \
    --suites libero_spatial \
    --n_episodes 50 \
    --gpu 0 \
    --seed 42 \
    --out_dir /root/acib/outputs/acib_v5_div_reg_eval

# Suite: libero_object
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/acib && \
CUDA_VISIBLE_DEVICES=0 python3 -u scripts/eval_acib.py \
    --checkpoint_dir /root/acib/outputs/acib_v5_div_reg \
    --base_model lerobot/smolvla_libero \
    --suites libero_object \
    --n_episodes 50 \
    --gpu 0 \
    --seed 42 \
    --out_dir /root/acib/outputs/acib_v5_div_reg_eval

# Suite: libero_goal
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/acib && \
CUDA_VISIBLE_DEVICES=0 python3 -u scripts/eval_acib.py \
    --checkpoint_dir /root/acib/outputs/acib_v5_div_reg \
    --base_model lerobot/smolvla_libero \
    --suites libero_goal \
    --n_episodes 50 \
    --gpu 0 \
    --seed 42 \
    --out_dir /root/acib/outputs/acib_v5_div_reg_eval

# Suite: libero_10
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/acib && \
CUDA_VISIBLE_DEVICES=0 python3 -u scripts/eval_acib.py \
    --checkpoint_dir /root/acib/outputs/acib_v5_div_reg \
    --base_model lerobot/smolvla_libero \
    --suites libero_10 \
    --n_episodes 50 \
    --gpu 0 \
    --seed 42 \
    --out_dir /root/acib/outputs/acib_v5_div_reg_eval

# =============================================================================
# Option C: nohup wrapper (for long-running eval, avoids SSH timeout)
# =============================================================================
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/acib && \
nohup bash -c 'CUDA_VISIBLE_DEVICES=0 python3 -u scripts/eval_acib.py \
    --checkpoint_dir /root/acib/outputs/acib_v5_div_reg \
    --base_model lerobot/smolvla_libero \
    --suites libero_spatial libero_object libero_goal libero_10 \
    --n_episodes 50 \
    --gpu 0 \
    --seed 42 \
    --out_dir /root/acib/outputs/acib_v5_div_reg_eval' \
    > /root/acib/outputs/acib_v5_div_reg_eval/eval.log 2>&1 &
echo "PID=$!"

# Monitor:
#   tail -f /root/acib/outputs/acib_v5_div_reg_eval/eval.log
#   ps -p <PID> -o pid= && echo RUNNING || echo DONE

# =============================================================================
# ⚠️ CRITICAL: Post-launch verification (Reviewer mandate)
# =============================================================================
# After launching eval, IMMEDIATELY check log for monkey-patch confirmation:
#   grep -i "ACIB.*loading\|loading.*checkpoint\|monkey.patch" /root/acib/outputs/acib_v5_div_reg_eval/eval.log
#
# MUST see "[ACIB] loading checkpoint" or similar. If ABSENT:
#   → monkey-patch failed, eval is running base model = results = baseline = WASTED HOURS
#   → Kill immediately and debug eval_acib.py
#
# ⚠️ DO NOT use run_acib_eval.sh — it calls lerobot-eval which expects HuggingFace
#    format, but ACIB checkpoint is custom PyTorch format (checkpoint.pt).
#    from_pretrained() will crash. ONLY use eval_acib.py (monkey-patch approach).
#
# ⚠️ --seed 42 is mandatory (matches baseline eval seed for fair comparison)
