#!/usr/bin/env bash
set -euo pipefail

ROOT=.
OUT=${OPENR1_BASELINE_OUT:-$ROOT/results/formal_baselines/open_r1_math500/qwen1p5b_budget_512}
LIMIT=${OPENR1_BASELINE_LIMIT:-0}

cd "$ROOT"
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-open-r1

CUDA_VISIBLE_DEVICES="${OPENR1_CUDA_VISIBLE_DEVICES:-1}" \
python baselines/bohb/open_r1_math500/openr1_math500_eval.py \
  --model "$ROOT/models/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B" \
  --data "$ROOT/data/paper_exact/open_r1_math500/math_500/test.jsonl" \
  --output "$OUT/metrics.json" \
  --predictions "$OUT/predictions.jsonl" \
  --limit "$LIMIT" \
  --max-new-tokens 512 \
  --temperature 0.0 \
  --top-p 1.0 \
  --max-model-len 4096 \
  --gpu-memory-utilization 0.72 \
  --dtype bfloat16
