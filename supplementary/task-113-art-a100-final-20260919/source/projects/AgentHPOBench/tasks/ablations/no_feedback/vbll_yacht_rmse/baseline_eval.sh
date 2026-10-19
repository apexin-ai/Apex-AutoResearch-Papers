#!/usr/bin/env bash
set -euo pipefail

BASE=.
FORMAL=$BASE/tasks/ablations/no_feedback/vbll_yacht_rmse
OUT=$BASE/results/formal_baselines/vbll_yacht_rmse/baseline_diag_80ep
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
export CUDA_VISIBLE_DEVICES="${CUDA_VISIBLE_DEVICES:-1}"
export PYTHONPATH="$BASE/repositories/vbll:$BASE/.python_deps:${PYTHONPATH:-}"
python "$FORMAL/eval_vbll_yacht.py" \
  --results-dir "$OUT" \
  --hidden-features 64 \
  --num-layers 2 \
  --parameterization diagonal \
  --lr 1e-3 \
  --weight-decay 1e-4 \
  --batch-size 32 \
  --epochs "${VBLL_EPOCHS:-80}" \
  --reg-weight-scale 1.0 \
  --prior-scale 1.0 \
  --wishart-scale 0.1 \
  --dropout 0.0 \
  --no-use-scheduler \
  --select-best-val \
  --device cuda:0 \
  --seed 1
