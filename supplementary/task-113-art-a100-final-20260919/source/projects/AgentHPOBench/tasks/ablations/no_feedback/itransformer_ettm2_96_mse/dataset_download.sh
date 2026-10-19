#!/usr/bin/env bash
set -euo pipefail

BASE="."
DATA="$BASE/data/formal/ett_diverse/ETT-small/ETTm2.csv"
REPO="$BASE/repositories/iTransformer/run.py"

test -f "$DATA"
test -f "$REPO"
python -c "import pandas as pd; p='$DATA'; df=pd.read_csv(p); assert df.shape[1] == 8, df.shape; print({'dataset':'ETTm2','shape':df.shape,'path':p})"
