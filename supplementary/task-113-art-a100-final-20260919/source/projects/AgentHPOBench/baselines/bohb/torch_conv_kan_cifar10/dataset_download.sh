#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AUTOREP_ROOT="${AUTOREP_ROOT:-$(cd "$SCRIPT_DIR/../../.." && pwd)}"
DATA_ROOT="${DATA_ROOT:-$AUTOREP_ROOT/data/paper_exact/torch_conv_kan_cifar10}"

mkdir -p "$DATA_ROOT"

if [[ "${DRY_RUN:-0}" == "1" ]]; then
  echo "Would download CIFAR-10 with torchvision into: $DATA_ROOT"
  exit 0
fi

CIFAR_ROOT="$DATA_ROOT" python3 - <<'PY'
import os
from torchvision.datasets import CIFAR10

root = os.environ["CIFAR_ROOT"]
CIFAR10(root=root, train=True, download=True)
CIFAR10(root=root, train=False, download=True)
print(f"CIFAR-10 is ready at {root}")
PY
