#!/usr/bin/env bash
set -euo pipefail

BASE="${AUTOREP_BASE:-.}"
DATA_DIR="$BASE/data/paper_exact/modernbert_mnli/glue_mnli"
MODEL_DIR="$BASE/models/modernbert/ModernBERT-base"

source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec

if [[ ! -d "$MODEL_DIR" ]]; then
  echo "Missing ModernBERT model dir: $MODEL_DIR" >&2
  exit 2
fi

if [[ -f "$DATA_DIR/dataset_dict.json" ]]; then
  echo "Using existing GLUE MNLI save_to_disk dataset at $DATA_DIR"
else
  mkdir -p "$(dirname "$DATA_DIR")"
  export HF_DATASETS_OFFLINE="${HF_DATASETS_OFFLINE:-1}"
  python - "$DATA_DIR" "$BASE/cache" <<'PY'
from pathlib import Path
import sys
from datasets import load_dataset

out = Path(sys.argv[1])
cache = Path(sys.argv[2])
ds = load_dataset("glue", "mnli", cache_dir=str(cache))
ds.save_to_disk(str(out))
print({"dataset": "glue/mnli", "splits": {k: len(v) for k, v in ds.items()}, "out": str(out)})
PY
fi

python - "$DATA_DIR" <<'PY'
import sys
from datasets import load_from_disk

ds = load_from_disk(sys.argv[1])
print({"dataset": "glue/mnli", "splits": {k: len(v) for k, v in ds.items()}})
PY
