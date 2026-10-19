#!/usr/bin/env bash
set -euo pipefail

ROOT=${AUTOREP_ROOT:-.}
REPO_DIR="$ROOT/repositories/uni2ts"
MODEL_DIR="$ROOT/models/uni2ts/moirai-1.0-R-small"
LSF_PATH="${LSF_PATH:-$ROOT/data/formal/uni2ts_lsf}"
OUT_DIR="${UNI2TS_OUT_DIR:-$ROOT/results/formal_baselines/uni2ts_lsf_etth1}"
LOG_FILE="${UNI2TS_LOG_FILE:-$ROOT/logs/formal_baselines/uni2ts_lsf_etth1_moirai_small_pl96.log}"
NUM_SAMPLES="${UNI2TS_NUM_SAMPLES:-100}"
BATCH_SIZE="${UNI2TS_BATCH_SIZE:-512}"
PATCH_SIZE="${UNI2TS_PATCH_SIZE:-64}"
CONTEXT_LENGTH="${UNI2TS_CONTEXT_LENGTH:-5000}"
CUDA_VISIBLE_DEVICES="${UNI2TS_CUDA_VISIBLE_DEVICES:-0}"

mkdir -p "$OUT_DIR" "$(dirname "$LOG_FILE")"
cd "$REPO_DIR"

source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec

export LSF_PATH
export PYTHONPATH="$REPO_DIR/src:${PYTHONPATH:-}"
export CUDA_VISIBLE_DEVICES

python -m cli.eval \
  run_name=autorep_formal_moirai_small_pl96 \
  model=moirai_1.0_R_small \
  model.module.pretrained_model_name_or_path="$MODEL_DIR" \
  model.patch_size="$PATCH_SIZE" \
  model.context_length="$CONTEXT_LENGTH" \
  model.num_samples="$NUM_SAMPLES" \
  data=lsf_test \
  data.dataset_name=ETTh1 \
  data.mode=M \
  data.prediction_length=96 \
  batch_size="$BATCH_SIZE" \
  device=cuda \
  2>&1 | tee "$LOG_FILE"
