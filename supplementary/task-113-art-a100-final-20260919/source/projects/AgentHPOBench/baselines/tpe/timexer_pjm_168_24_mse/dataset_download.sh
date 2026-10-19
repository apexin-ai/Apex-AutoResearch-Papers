#!/usr/bin/env bash
set -euo pipefail

BASE="."
DATA="$BASE/repositories/TimeXer/dataset/EPF/PJM.csv"
test -f "$DATA"
python -c "import pandas as pd; p='$DATA'; df=pd.read_csv(p); assert df.shape[1] == 4 and 'OT' in df.columns, df.shape; print({'dataset':'EPF/PJM','shape':df.shape,'path':p})"
