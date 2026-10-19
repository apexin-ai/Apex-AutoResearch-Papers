#!/usr/bin/env bash
set -euo pipefail

cd .

if [[ ! -d repositories/semi-supervised-regression ]]; then
  mkdir -p newrepo
  tar -xzf data/downloads/rankup/rankup_repo.tar.gz -C newrepo
  mv repositories/rankup repositories/semi-supervised-regression
fi

DATA_DIR="data/formal/rankup_utkface/utkface"
mkdir -p "$DATA_DIR"
if [[ ! -d "$DATA_DIR/UTKFace" ]]; then
  tar -xzf data/downloads/rankup/UTKFace.tar.gz -C "$DATA_DIR"
fi
if [[ ! -d "$DATA_DIR/meta" ]]; then
  unzip -q data/downloads/rankup/meta.zip -d "$DATA_DIR"
fi

source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda run -n autorep-vlm2vec python -c '
import json
from pathlib import Path
import pandas as pd

root = Path(".")
data_dir = root / "data/formal/rankup_utkface/utkface"
train = pd.read_csv(data_dir / "meta/train.csv")
test = pd.read_csv(data_dir / "meta/test.csv")
payload = {
    "dataset": "UTKFace",
    "train_rows": int(len(train)),
    "test_rows": int(len(test)),
    "image_dir_exists": (data_dir / "UTKFace").is_dir(),
    "official_anchor_MAE": 4.851,
    "official_anchor_source": "semi-supervised-regression/results/classic_cv_average_log.csv fullysupervised_utkface",
}
(data_dir / "dataset_info.json").write_text(json.dumps(payload, indent=2))
print(json.dumps(payload, indent=2))
'
