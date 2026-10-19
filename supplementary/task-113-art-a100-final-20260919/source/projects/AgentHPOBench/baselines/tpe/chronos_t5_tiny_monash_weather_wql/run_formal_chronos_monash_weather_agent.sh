#!/usr/bin/env bash
set -euo pipefail

cd .
export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-1}"
export QWEN_CUDA_VISIBLE_DEVICES="${QWEN_CUDA_VISIBLE_DEVICES:-1}"
export PYTHONPATH="$PWD/.python_deps:$PWD/repositories/chronos-forecasting/src:$PWD:${PYTHONPATH:-}"
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda run -n autorep-vlm2vec python baselines/tpe/chronos_t5_tiny_monash_weather_wql/run_formal_chronos_monash_weather_agent.py
