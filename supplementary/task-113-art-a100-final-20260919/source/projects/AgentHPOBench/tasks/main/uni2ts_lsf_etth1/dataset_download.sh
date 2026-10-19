#!/usr/bin/env bash
set -euo pipefail

ROOT=${AUTOREP_ROOT:-.}
DATA_DIR="$ROOT/data/formal/uni2ts_lsf/ETT-small"
MODEL_DIR="$ROOT/models/uni2ts/moirai-1.0-R-small"

mkdir -p "$DATA_DIR" "$MODEL_DIR"

if [[ ! -s "$DATA_DIR/ETTh1.csv" ]]; then
  curl -L --retry 3 \
    -o "$DATA_DIR/ETTh1.csv" \
    https://raw.githubusercontent.com/zhouhaoyi/ETDataset/main/ETT-small/ETTh1.csv
fi

if [[ ! -s "$MODEL_DIR/model.safetensors" ]]; then
  export HF_ENDPOINT="${HF_ENDPOINT:-https://hf-mirror.com}"
  export HF_HOME="${HF_HOME:-$ROOT/external/hf_cache}"
  source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
  conda activate autorep-vlm2vec
  python - <<'PY'
from pathlib import Path
from huggingface_hub import snapshot_download

root = Path(".")
snapshot_download(
    repo_id="Salesforce/moirai-1.0-R-small",
    local_dir=str(root / "models/uni2ts/moirai-1.0-R-small"),
)
PY
fi

test -s "$DATA_DIR/ETTh1.csv"
test -s "$MODEL_DIR/config.json"
test -s "$MODEL_DIR/model.safetensors"
echo "Uni2TS ETTh1 data and MOIRAI-small checkpoint are available."
