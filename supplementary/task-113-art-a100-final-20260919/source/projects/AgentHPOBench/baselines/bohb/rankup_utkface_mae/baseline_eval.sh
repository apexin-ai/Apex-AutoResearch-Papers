#!/usr/bin/env bash
set -euo pipefail

cd .
OUT="${OUT_DIR:-results/formal_baselines/rankup_utkface_mae/baseline}"
mkdir -p "$OUT"
export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-1}"
export PYTHONPATH="$PWD/repositories/semi-supervised-regression:$PWD/.python_deps:$PWD:${PYTHONPATH:-}"
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda run -n autorep-vlm2vec python baselines/bohb/rankup_utkface_mae/eval_rankup_utkface.py \
  --results-dir "$OUT" \
  --lr "${RANKUP_LR:-0.01}" \
  --weight-decay "${RANKUP_WEIGHT_DECAY:-0.001}" \
  --batch-size "${RANKUP_BATCH_SIZE:-32}" \
  --train-steps "${RANKUP_TRAIN_STEPS:-400}" \
  --eval-examples "${RANKUP_EVAL_EXAMPLES:-0}" \
  ${RANKUP_NO_AUGMENT:+--no-augment} \
  --seed 0
