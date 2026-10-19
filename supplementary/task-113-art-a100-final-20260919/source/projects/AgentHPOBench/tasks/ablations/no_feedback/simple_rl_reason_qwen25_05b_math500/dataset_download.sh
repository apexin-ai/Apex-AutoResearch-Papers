#!/usr/bin/env bash
set -euo pipefail

ROOT="${AUTOREP_ROOT:-.}"
DATA_DIR="$ROOT/data/formal/simple_rl_reason_qwen25_05b_math500/simplelr_qwen_level3to5"
mkdir -p "$DATA_DIR"

BASE_URL="https://huggingface.co/datasets/hkust-nlp/SimpleRL-Zoo-Data/resolve/main/simplelr_qwen_level3to5"
for name in train.parquet test.parquet; do
  if [ ! -s "$DATA_DIR/$name" ]; then
    wget -O "$DATA_DIR/$name" "$BASE_URL/$name"
  fi
done

python - <<'PY'
from pathlib import Path
import pandas as pd

root = Path(__import__("os").environ.get("AUTOREP_ROOT", "."))
data_dir = root / "data/formal/simple_rl_reason_qwen25_05b_math500/simplelr_qwen_level3to5"
for path in sorted(data_dir.glob("*.parquet")):
    df = pd.read_parquet(path)
    print(f"{path.name}: shape={df.shape}")
PY
