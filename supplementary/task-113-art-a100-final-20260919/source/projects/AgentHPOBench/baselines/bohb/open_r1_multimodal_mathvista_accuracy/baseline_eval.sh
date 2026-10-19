#!/usr/bin/env bash
set -euo pipefail

cd .
OUT="${OUT_DIR:-results/formal_baselines/open_r1_multimodal_mathvista_accuracy/baseline_direct}"
mkdir -p "$OUT"
export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-0}"
export PYTHONPATH="$PWD/.python_deps:$PWD:${PYTHONPATH:-}"
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda run -n autorep-vlm2vec python baselines/bohb/open_r1_multimodal_mathvista_accuracy/eval_open_r1_multimodal_mathvista.py \
  --results-dir "$OUT" \
  --prompt-style "${MATHVISTA_PROMPT_STYLE:-direct}" \
  --max-new-tokens "${MATHVISTA_MAX_NEW_TOKENS:-32}" \
  --temperature "${MATHVISTA_TEMPERATURE:-0.0}" \
  --top-p "${MATHVISTA_TOP_P:-1.0}" \
  --max-examples "${MATHVISTA_MAX_EXAMPLES:-0}" \
  --seed 0
