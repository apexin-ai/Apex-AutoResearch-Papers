#!/usr/bin/env bash
set -euo pipefail

BASE=.
DATA="$BASE/data/formal/ett_diverse/ETT-small/ETTm1.csv"
REPO="$BASE/repositories/SparseTSF"

if [[ ! -s "$DATA" ]]; then
  echo "Missing ETTm1 data at $DATA" >&2
  exit 1
fi

if [[ ! -f "$REPO/models/SparseTSF.py" ]]; then
  echo "Missing SparseTSF repo at $REPO" >&2
  exit 1
fi

python - <<'PY'
from pathlib import Path
import pandas as pd

path = Path("./data/formal/ett_diverse/ETT-small/ETTm1.csv")
df = pd.read_csv(path)
print({
    "path": str(path),
    "rows": len(df),
    "columns": list(df.columns),
})
PY
