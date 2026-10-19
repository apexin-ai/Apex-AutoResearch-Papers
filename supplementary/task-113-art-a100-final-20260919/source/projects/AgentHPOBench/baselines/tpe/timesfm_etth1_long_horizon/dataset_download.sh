#!/usr/bin/env bash
set -euo pipefail

ROOT="${AUTOREP_ROOT:-.}"
OUT_DIR="$ROOT/data/formal/timesfm_long_horizon/ETT-small"
SRC="$ROOT/data/formal/uni2ts_lsf/ETT-small/ETTh1.csv"
mkdir -p "$OUT_DIR"

if [[ -f "$SRC" ]]; then
  cp "$SRC" "$OUT_DIR/ETTh1.csv"
else
  curl -L --fail --retry 5 \
    -o "$OUT_DIR/ETTh1.csv" \
    "https://raw.githubusercontent.com/zhouhaoyi/ETDataset/main/ETT-small/ETTh1.csv"
fi

python - <<'PY'
from pathlib import Path
root = Path(".")
p = root / "data/formal/timesfm_long_horizon/ETT-small/ETTh1.csv"
print(p, p.exists(), sum(1 for _ in p.open()))
PY
