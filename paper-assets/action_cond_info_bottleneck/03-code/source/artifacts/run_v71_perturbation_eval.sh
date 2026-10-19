#!/bin/bash
# v7.1 perturbation eval: 4 perturbation types × scored/unscored = 8 runs
# Designed for dual GPU parallel: GPU 0 runs scored (alpha=1.0), GPU 1 runs unscored (alpha=0.0)
#
# Usage:
#   GPU 0 (scored):   CUDA_VISIBLE_DEVICES=0 bash run_v71_perturbation_eval.sh scored <seed_dir>
#   GPU 1 (unscored): CUDA_VISIBLE_DEVICES=1 bash run_v71_perturbation_eval.sh unscored <seed_dir>

MODE=${1:-scored}  # "scored" or "unscored"
SEED_DIR=${2:-acib_v7.1_scorer_only_seed1}
CKPT_DIR="/root/autodl-tmp/${SEED_DIR}"
BASE_OUT="/root/autodl-tmp/v71_perturbation_eval"

if [ "$MODE" = "scored" ]; then
    ALPHA=1.0
elif [ "$MODE" = "unscored" ]; then
    ALPHA=0.0
else
    echo "Usage: $0 <scored|unscored> <seed_dir>"
    exit 1
fi

PERTURBATIONS="gaussian_noise color_jitter spatial_jitter sensor_noise"

cd /root/acib
for pert in $PERTURBATIONS; do
    OUT_DIR="${BASE_OUT}/${MODE}/${pert}"
    echo "=== Running ${MODE} (alpha=${ALPHA}) ${pert} ==="
    python3 -u scripts/eval_acib_perturbed.py \
      --checkpoint_dir "${CKPT_DIR}" \
      --checkpoint_step 20000 \
      --base_model lerobot/smolvla_libero \
      --suites libero_spatial libero_object libero_goal libero_10 \
      --perturbation "${pert}" \
      --n_episodes 50 \
      --gpu 0 --seed 42 \
      --scoring_alpha "${ALPHA}" \
      --out_dir "${OUT_DIR}"
    echo "=== Done ${pert} ==="
    echo ""
done

echo "All ${MODE} perturbation evals complete."
