#!/usr/bin/env bash
set -euo pipefail

cd .
export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-1}"
export QWEN_CUDA_VISIBLE_DEVICES="${QWEN_CUDA_VISIBLE_DEVICES:-1}"
export PYTHONPATH="$PWD:$PWD/.python_deps:$PWD/repositories/ForestDiffusion:$PWD/repositories/ForestDiffusion/Python-Package/base-ForestDiffusion:${PYTHONPATH:-}"
python baselines/bohb/forest_diffusion_iris_f1fake/run_formal_forest_diffusion_iris_agent.py
