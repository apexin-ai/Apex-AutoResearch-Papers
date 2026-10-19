#!/usr/bin/env bash
set -euo pipefail

cd .
OUT="${OUT_DIR:-results/formal_baselines/chronos_t5_tiny_monash_weather_wql/baseline_ctx512_s20}"
mkdir -p "$OUT"
export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-1}"
export PYTHONPATH="$PWD/.python_deps:$PWD/repositories/chronos-forecasting/src:$PWD:${PYTHONPATH:-}"
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda run -n autorep-vlm2vec python baselines/bohb/chronos_t5_tiny_monash_weather_wql/eval_chronos_monash_weather.py \
  --results-dir "$OUT" \
  --method chronos \
  --prediction-length 30 \
  --context-length "${CHRONOS_CONTEXT_LENGTH:-512}" \
  --num-samples "${CHRONOS_NUM_SAMPLES:-20}" \
  --temperature "${CHRONOS_TEMPERATURE:-1.0}" \
  --top-k "${CHRONOS_TOP_K:-50}" \
  --top-p "${CHRONOS_TOP_P:-1.0}" \
  --max-series "${CHRONOS_MAX_SERIES:-0}" \
  --chunk-size "${CHRONOS_CHUNK_SIZE:-64}" \
  --device cuda \
  --seed 0
