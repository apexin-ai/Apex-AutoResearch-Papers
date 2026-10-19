#!/usr/bin/env bash
set -euo pipefail
BASE=.
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
python "$BASE/tasks/main/binary_diffusion_adult_rf/eval_binary_diffusion_adult_rf.py" --results-dir "$BASE/results/formal_baselines/binary_diffusion_adult_rf/baseline_rf"
