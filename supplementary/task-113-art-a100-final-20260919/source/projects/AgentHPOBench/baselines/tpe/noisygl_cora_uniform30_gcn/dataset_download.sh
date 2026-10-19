#!/usr/bin/env bash
set -euo pipefail

BASE=.
DATA_DIR="$BASE/data/paper_exact/noisygl_cora"
mkdir -p "$DATA_DIR"
missing=0
for f in x tx allx y ty ally graph test.index; do
  if [[ ! -s "$DATA_DIR/ind.cora.$f" ]]; then
    missing=1
  fi
done
if [[ "$missing" -ne 0 ]]; then
  echo "Cora Planetoid files are missing in $DATA_DIR. Upload data/paper_exact/noisygl_cora before running on the network-restricted GPU node." >&2
  exit 2
fi
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
python "$BASE/baselines/tpe/noisygl_cora_uniform30_gcn/eval_noisygl_cora_gcn.py" \
  --results-dir "$BASE/results/formal_baselines/noisygl_cora_uniform30_gcn/smoke_5ep" \
  --epochs 5 \
  --hidden-dim 32 \
  --dropout 0.5 \
  --lr 0.01 \
  --weight-decay 0.0005 \
  --noise-rate 0.3 \
  --seed 3000 \
  --noise-seed 3000 \
  --cpu
