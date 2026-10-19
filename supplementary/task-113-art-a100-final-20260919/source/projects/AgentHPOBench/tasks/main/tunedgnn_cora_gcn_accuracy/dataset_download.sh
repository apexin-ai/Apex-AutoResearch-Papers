#!/usr/bin/env bash
set -euo pipefail

BASE="${AUTOREP_ROOT:-.}"
DATA_DIR="$BASE/data/paper_exact/noisygl_cora"

required=(
  ind.cora.x
  ind.cora.y
  ind.cora.tx
  ind.cora.ty
  ind.cora.allx
  ind.cora.ally
  ind.cora.graph
  ind.cora.test.index
)

missing=0
for file in "${required[@]}"; do
  if [[ ! -f "$DATA_DIR/$file" ]]; then
    echo "Missing $DATA_DIR/$file" >&2
    missing=1
  fi
done

if [[ "$missing" != "0" ]]; then
  echo "Cora Planetoid files are expected from the existing NoisyGL Cora staging directory." >&2
  exit 2
fi

echo "Cora Planetoid files ready: $DATA_DIR"
