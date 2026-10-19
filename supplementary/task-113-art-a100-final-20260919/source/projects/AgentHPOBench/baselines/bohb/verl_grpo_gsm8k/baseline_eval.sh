#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AUTOREP_ROOT="${AUTOREP_ROOT:-$(cd "$SCRIPT_DIR/../../.." && pwd)}"
REPO_DIR="${REPO_DIR:-$AUTOREP_ROOT/repositories/verl}"
DATA_ROOT="${DATA_ROOT:-$AUTOREP_ROOT/data/paper_exact/verl_grpo_gsm8k/gsm8k}"
BASELINE_SCRIPT="${BASELINE_SCRIPT:-examples/grpo_trainer/run_qwen2_5-3b_gsm8k_grpo_lora.sh}"

if [[ ! -d "$REPO_DIR" ]]; then
  echo "Missing repo: $REPO_DIR" >&2
  exit 2
fi

if [[ ! -f "$REPO_DIR/$BASELINE_SCRIPT" ]]; then
  echo "Missing baseline script: $REPO_DIR/$BASELINE_SCRIPT" >&2
  exit 2
fi

export GSM8K_DATA_DIR="${GSM8K_DATA_DIR:-$DATA_ROOT}"
TRAIN_FILE="${TRAIN_FILE:-$GSM8K_DATA_DIR/train.parquet}"
VAL_FILE="${VAL_FILE:-$GSM8K_DATA_DIR/test.parquet}"

if [[ ! -f "$TRAIN_FILE" || ! -f "$VAL_FILE" ]]; then
  echo "Missing GSM8K parquet files under: $GSM8K_DATA_DIR" >&2
  exit 2
fi

cmd=(
  bash "$BASELINE_SCRIPT"
  "data.train_files=$TRAIN_FILE"
  "data.val_files=$VAL_FILE"
  "$@"
)
echo "Repo: $REPO_DIR"
echo "GSM8K_DATA_DIR=$GSM8K_DATA_DIR"
echo "TRAIN_FILE=$TRAIN_FILE"
echo "VAL_FILE=$VAL_FILE"
printf 'Command:'
printf ' %q' "${cmd[@]}"
printf '\n'

if [[ "${DRY_RUN:-0}" == "1" ]]; then
  exit 0
fi

cd "$REPO_DIR"
"${cmd[@]}"
