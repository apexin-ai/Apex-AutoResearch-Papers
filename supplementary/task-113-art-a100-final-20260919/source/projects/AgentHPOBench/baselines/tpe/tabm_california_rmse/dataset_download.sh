#!/usr/bin/env bash
set -euo pipefail

BASE="."
DATA_DIR="$BASE/data/paper_exact/tabm_california"
REPO_DIR="$BASE/repositories/tabm"

test -f "$DATA_DIR/cal_housing.data"
test -f "$DATA_DIR/cal_housing.domain"
test -f "$REPO_DIR/tabm.py"

python - <<'PY'
from pathlib import Path
import numpy as np

base = Path(".")
data = base / "data/paper_exact/tabm_california/cal_housing.data"
arr = np.loadtxt(data, delimiter=",", dtype=np.float32)
assert arr.shape == (20640, 9), arr.shape
print({"dataset": "California Housing", "shape": arr.shape, "path": str(data)})
PY
