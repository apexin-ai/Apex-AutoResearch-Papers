#!/usr/bin/env bash
set -euo pipefail

cd .
DATA_DIR="data/paper_exact/forest_diffusion_iris"
mkdir -p "$DATA_DIR"
cp "repositories/ForestDiffusion/Results/Results_tabular - ablation_iris.csv" "$DATA_DIR/official_ablation_iris.csv"
python - <<'PY'
import json
from pathlib import Path
from sklearn.datasets import load_iris

root = Path(".")
out = root / "data/paper_exact/forest_diffusion_iris"
data = load_iris()
payload = {
    "dataset": "sklearn Iris",
    "n_samples": int(data["data"].shape[0]),
    "n_features": int(data["data"].shape[1]),
    "n_classes": int(len(set(data["target"].tolist()))),
    "official_result_csv": str(out / "official_ablation_iris.csv"),
}
(out / "dataset_info.json").write_text(json.dumps(payload, indent=2))
print(json.dumps(payload, indent=2))
PY
