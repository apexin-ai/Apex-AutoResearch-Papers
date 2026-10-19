#!/usr/bin/env bash
set -euo pipefail

BASE=.
DATA=$BASE/data/paper_exact/vbll_yacht/yacht_hydrodynamics.data
test -f "$DATA"
python - <<'PY'
import numpy as np
from pathlib import Path

data = Path("./data/paper_exact/vbll_yacht/yacht_hydrodynamics.data")
arr = np.loadtxt(data)
print({
    "dataset": "UCI Yacht Hydrodynamics",
    "source_file": str(data),
    "rows": int(arr.shape[0]),
    "columns": int(arr.shape[1]),
    "paper_anchor_rmse": 0.86,
    "paper_anchor_nll": 1.29,
    "source": "UCI archive static public dataset 243; original six attributes plus residuary resistance target."
})
PY
