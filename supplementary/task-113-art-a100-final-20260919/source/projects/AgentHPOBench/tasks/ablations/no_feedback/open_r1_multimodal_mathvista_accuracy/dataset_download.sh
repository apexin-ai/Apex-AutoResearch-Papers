#!/usr/bin/env bash
set -euo pipefail

cd .
DATA_DIR="data/formal/open_r1_multimodal_mathvista"
PARQUET="$DATA_DIR/testmini.parquet"
mkdir -p "$DATA_DIR"

if [[ ! -f "$PARQUET" ]]; then
  UPLOAD="data/downloads/mathvista/testmini.parquet"
  if [[ -f "$UPLOAD" ]]; then
    cp "$UPLOAD" "$PARQUET"
  else
    echo "Missing $PARQUET. Stage AI4Math/MathVista testmini parquet via autorep_uploads/mathvista/testmini.parquet." >&2
    exit 2
  fi
fi

source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda run -n autorep-vlm2vec python - <<'PY'
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

root = Path(".")
data_dir = root / "data/formal/open_r1_multimodal_mathvista"
df = pd.read_parquet(data_dir / "testmini.parquet")
payload = {
    "dataset": "MathVista-mini",
    "rows": int(len(df)),
    "question_type_counts": {str(k): int(v) for k, v in df["question_type"].value_counts().sort_index().items()},
    "answer_type_counts": {str(k): int(v) for k, v in df["answer_type"].value_counts().sort_index().items()},
    "official_anchor_accuracy_percent": 51.6,
    "official_anchor_source": "open-r1-multimodal README Mathvista-mini Qwen2-VL-2B-Instruct(w.o reasoning)",
}
(data_dir / "dataset_info.json").write_text(json.dumps(payload, indent=2))
print(json.dumps(payload, indent=2))
PY
