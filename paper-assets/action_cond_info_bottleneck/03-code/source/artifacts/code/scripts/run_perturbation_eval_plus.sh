#!/bin/bash
# LIBERO-Plus perturbation eval for data-aug baseline (lerobot/smolvla_libero_plus)
# Run AFTER standard LIBERO eval completes to establish robustness gap.
# GPU 0 (CUDA_VISIBLE_DEVICES=0)
set -e

source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
source /etc/network_turbo
export HF_HOME=/root/autodl-tmp/.hf_cache
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
export HF_HUB_DISABLE_XET=1
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl
export CUDA_VISIBLE_DEVICES=0

cd /root/acib
echo "$(date '+%Y-%m-%d %H:%M:%S') Starting LIBERO-Plus perturbation eval (baseline_plus)"

for suite in libero_spatial libero_object libero_goal libero_10; do
    echo "$(date '+%Y-%m-%d %H:%M:%S') === Perturbation eval suite: $suite ==="
    python3 -u -m lerobot.scripts.eval \
        --policy.path=lerobot/smolvla_libero_plus \
        --env.type=libero_plus \
        --env.task=$suite \
        --eval.n_episodes=50 \
        --eval.batch_size=1 \
        --output_dir=/root/acib/outputs/perturbation_plus/$suite
    echo "$(date '+%Y-%m-%d %H:%M:%S') === Done: $suite ==="
done

echo "$(date '+%Y-%m-%d %H:%M:%S') ALL PERTURBATION EVAL (PLUS) COMPLETE"
