#!/usr/bin/env bash
set -euo pipefail

cd .
DATA_DIR="data/formal/chronos_monash_weather/monash_weather"
PARQUET="$DATA_DIR/train-00000-of-00001.parquet"
mkdir -p "$DATA_DIR"

if [[ ! -f "$PARQUET" ]]; then
  UPLOAD="data/downloads/chronos_monash_weather/monash_weather/train-00000-of-00001.parquet"
  if [[ -f "$UPLOAD" ]]; then
    cp "$UPLOAD" "$PARQUET"
  else
    echo "Missing $PARQUET. Download on a networked node from hf-mirror/autogluon/chronos_datasets and stage it via autorep_uploads." >&2
    exit 2
  fi
fi

cp repositories/chronos-forecasting/scripts/evaluation/results/chronos-t5-tiny-zero-shot.csv "$DATA_DIR/chronos-t5-tiny-zero-shot.csv"
cp repositories/chronos-forecasting/scripts/evaluation/configs/zero-shot.yaml "$DATA_DIR/zero-shot.yaml"

source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda run -n autorep-vlm2vec python - <<'PY'
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

root = Path(".")
data_dir = root / "data/formal/chronos_monash_weather/monash_weather"
df = pd.read_parquet(data_dir / "train-00000-of-00001.parquet")
lengths = df["target"].map(len)
payload = {
    "dataset": "monash_weather",
    "source": "autogluon/chronos_datasets/monash_weather",
    "rows": int(len(df)),
    "subsets": {str(k): int(v) for k, v in df["subset"].value_counts().sort_index().items()},
    "target_length_min": int(lengths.min()),
    "target_length_max": int(lengths.max()),
    "official_anchor_WQL": 0.14787595319625085,
    "official_anchor_source": "chronos-t5-tiny-zero-shot.csv monash_weather row",
}
(data_dir / "dataset_info.json").write_text(json.dumps(payload, indent=2))
print(json.dumps(payload, indent=2))
PY
