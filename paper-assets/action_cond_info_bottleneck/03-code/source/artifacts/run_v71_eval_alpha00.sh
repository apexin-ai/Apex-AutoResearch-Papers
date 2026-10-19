#!/bin/bash
# v7.1 eval: alpha=0.0 passthrough (should = baseline ~66%)
# Usage: CUDA_VISIBLE_DEVICES=X bash run_v71_eval_alpha00.sh <seed_dir> <out_suffix>
# Example: CUDA_VISIBLE_DEVICES=0 bash run_v71_eval_alpha00.sh acib_v7.1_scorer_only_seed1 seed1

SEED_DIR=${1:-acib_v7.1_scorer_only_seed1}
OUT_SUFFIX=${2:-seed1}
CKPT_DIR="/root/autodl-tmp/${SEED_DIR}"
OUT_DIR="/root/autodl-tmp/v71_eval/alpha_0.0_${OUT_SUFFIX}"

cd /root/acib
python3 -u scripts/eval_acib.py \
  --checkpoint_dir "${CKPT_DIR}" \
  --checkpoint_step 20000 \
  --base_model lerobot/smolvla_libero \
  --suites libero_spatial libero_object libero_goal libero_10 \
  --n_episodes 50 \
  --gpu 0 --seed 42 \
  --out_dir "${OUT_DIR}" \
  --scoring_alpha 0.0
