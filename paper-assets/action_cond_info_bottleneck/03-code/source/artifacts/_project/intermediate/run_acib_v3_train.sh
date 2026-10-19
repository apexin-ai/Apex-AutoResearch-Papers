#!/bin/bash
# ACIB v3 training: SmolVLA + ACIB-S with β warmup fix
# Uses lerobot/smolvla_libero (fine-tuned) as base, NOT smolvla_base
# β warmup: 0→0.01 over steps 1000-2000, batch_size=64
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
echo "$(date '+%Y-%m-%d %H:%M:%S') Starting ACIB v3 training (seed ${SEED:-42})"

python3 -u scripts/train_acib.py \
    --model_id lerobot/smolvla_libero \
    --dataset_id lerobot/libero \
    --hidden_dim 64 \
    --alpha 0.01 \
    --beta 0.01 \
    --beta_warmup_steps 1000 \
    --mode soft \
    --steps 20000 \
    --batch_size 64 \
    --lr 1e-4 \
    --warmup_steps 1000 \
    --grad_clip 1.0 \
    --gpu 0 \
    --output_dir /root/acib/outputs/acib_v3_s_h64_s${SEED:-42} \
    --seed ${SEED:-42} \
    --wandb_project acib \
    --wandb_run_name acib-v3-s-h64-b001-warmup-s${SEED:-42}

echo "$(date '+%Y-%m-%d %H:%M:%S') ACIB v3 training COMPLETE"
