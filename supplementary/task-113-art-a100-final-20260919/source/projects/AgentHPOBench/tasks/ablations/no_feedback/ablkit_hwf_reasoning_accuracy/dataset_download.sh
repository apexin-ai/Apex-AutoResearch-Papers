#!/usr/bin/env bash
set -euo pipefail

BASE="${AUTOREP_BASE:-.}"
HWF_DATA_DIR="$BASE/repositories/ABLkit/examples/hwf/datasets/data"
ZIP_SRC="${HWF_ZIP_SRC:-$BASE/data/paper_exact/ablkit_hwf/HWF.zip}"

if [[ -f "$HWF_DATA_DIR/expr_train.json" && -f "$HWF_DATA_DIR/expr_test.json" ]]; then
  echo "Using existing HWF data under $HWF_DATA_DIR"
  exit 0
fi

if [[ ! -f "$ZIP_SRC" ]]; then
  cat >&2 <<EOF
Missing HWF.zip at $ZIP_SRC.
The original ABLkit HWF example downloads this file from Google Drive:
https://drive.google.com/u/0/uc?id=1t52OE2Wdm5GdShX1jD2Wy8phCllk0r8I&export=download
EOF
  exit 2
fi

mkdir -p "$BASE/repositories/ABLkit/examples/hwf/datasets"
python - "$ZIP_SRC" "$BASE/repositories/ABLkit/examples/hwf/datasets" <<'PY'
from pathlib import Path
import sys
import zipfile

zip_src = Path(sys.argv[1])
out_dir = Path(sys.argv[2])
with zipfile.ZipFile(zip_src, "r") as zip_ref:
    zip_ref.extractall(out_dir)
print({"zip": str(zip_src), "out": str(out_dir)})
PY

test -f "$HWF_DATA_DIR/expr_train.json"
test -f "$HWF_DATA_DIR/expr_test.json"
echo "HWF data ready under $HWF_DATA_DIR"
