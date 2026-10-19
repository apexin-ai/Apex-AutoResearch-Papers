#!/usr/bin/env bash
set -euo pipefail

cd .
OUT="results/formal_baselines/forest_diffusion_iris_f1fake/baseline_nt10_dup5_flow"
mkdir -p "$OUT"
export PYTHONPATH="$PWD:$PWD/repositories/ForestDiffusion:$PWD/repositories/ForestDiffusion/Python-Package/base-ForestDiffusion:${PYTHONPATH:-}"
python tasks/main/forest_diffusion_iris_f1fake/eval_forest_diffusion_iris.py \
  --results-dir "$OUT" \
  --n-t 10 \
  --n-t-sampling 10 \
  --duplicate-k 5 \
  --max-depth 7 \
  --n-estimators 50 \
  --eta 0.3 \
  --diffusion-type flow \
  --ycond false \
  --n-batch 1 \
  --n-jobs 8 \
  --nexp 1 \
  --ngen 2 \
  --n-tries 2 \
  --seed 0
