#!/usr/bin/env bash
set -euo pipefail

BASE=.
source ${CONDA_ROOT:-/opt/miniconda3}/etc/profile.d/conda.sh
conda activate autorep-vlm2vec
python - <<'PY'
from pathlib import Path
from torchvision import datasets, transforms

root = Path("./data")
expected = root / "cifar-100-python"
if not expected.exists():
    raise SystemExit(f"missing CIFAR-100 at {expected}; GPU environment has no internet, stage it before running")
train = datasets.CIFAR100(root, train=True, download=False, transform=transforms.ToTensor())
test = datasets.CIFAR100(root, train=False, download=False, transform=transforms.ToTensor())
print({
    "dataset": "CIFAR-100",
    "root": str(root),
    "train": len(train),
    "test": len(test),
    "paper_anchor_accuracy_percent": 78.07,
    "paper_anchor_source": "HyperbolicCV README Table 1",
})
PY
