#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AUTOREP_ROOT="${AUTOREP_ROOT:-$(cd "$SCRIPT_DIR/../../.." && pwd)}"
REPO_DIR="${REPO_DIR:-$AUTOREP_ROOT/repositories/torch-conv-kan}"
DATA_ROOT="${DATA_ROOT:-$AUTOREP_ROOT/data/paper_exact/torch_conv_kan_cifar10}"
OUTPUT_DIR="${OUTPUT_DIR:-$AUTOREP_ROOT/results/formal_baselines/torch_conv_kan_cifar10}"
EPOCHS="${EPOCHS:-250}"
NUM_WORKERS="${NUM_WORKERS:-22}"

mkdir -p "$DATA_ROOT" "$OUTPUT_DIR"

if [[ ! -d "$REPO_DIR" ]]; then
  echo "Missing repo: $REPO_DIR" >&2
  exit 2
fi

if [[ ! -e "$REPO_DIR/data/cifar-10-batches-py" ]]; then
  if [[ -d "$REPO_DIR/data" && ! -L "$REPO_DIR/data" ]] && find "$REPO_DIR/data" -mindepth 1 -maxdepth 1 | grep -q .; then
    echo "Existing non-empty data dir is not CIFAR-10: $REPO_DIR/data" >&2
    exit 2
  fi
  rm -rf "$REPO_DIR/data"
  ln -s "$DATA_ROOT" "$REPO_DIR/data"
fi

cmd=(
  accelerate launch cifar.py
  "output_dir=$OUTPUT_DIR/runs"
  "logging_dir=$OUTPUT_DIR/train_logs"
  "epochs=$EPOCHS"
  "dataloader_num_workers=$NUM_WORKERS"
  "$@"
)

echo "Repo: $REPO_DIR"
printf 'Command:'
printf ' %q' "${cmd[@]}"
printf '\n'

if [[ "${DRY_RUN:-0}" == "1" ]]; then
  exit 0
fi

cd "$REPO_DIR"
"${cmd[@]}"
