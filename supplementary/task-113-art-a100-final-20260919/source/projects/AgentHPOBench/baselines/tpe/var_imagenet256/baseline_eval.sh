#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AUTOREP_ROOT="${AUTOREP_ROOT:-$(cd "$SCRIPT_DIR/../../.." && pwd)}"
REPO_DIR="${REPO_DIR:-$AUTOREP_ROOT/repositories/VAR}"
DATA_ROOT="${DATA_ROOT:-$AUTOREP_ROOT/data/paper_exact/var_imagenet256}"
OUTPUT_DIR="${OUTPUT_DIR:-$AUTOREP_ROOT/results/formal_baselines/var_imagenet256}"
SAMPLE_NPZ="${SAMPLE_NPZ:-}"
GUIDED_DIFFUSION_EVAL_DIR="${GUIDED_DIFFUSION_EVAL_DIR:-}"
REF_NPZ="${REF_NPZ:-$DATA_ROOT/fid_refs/VIRTUAL_imagenet256_labeled.npz}"

if [[ ! -d "$REPO_DIR" ]]; then
  echo "Missing repo: $REPO_DIR" >&2
  exit 2
fi

mkdir -p "$OUTPUT_DIR"

cmd=(python "$GUIDED_DIFFUSION_EVAL_DIR/evaluator.py" "$REF_NPZ" "$SAMPLE_NPZ")

echo "Repo: $REPO_DIR"
echo "SAMPLE_NPZ=${SAMPLE_NPZ:-<required>}"
echo "GUIDED_DIFFUSION_EVAL_DIR=${GUIDED_DIFFUSION_EVAL_DIR:-<required>}"
printf 'Command:'
printf ' %q' "${cmd[@]}"
printf '\n'

if [[ "${DRY_RUN:-0}" == "1" ]]; then
  exit 0
fi

if [[ -z "$SAMPLE_NPZ" || -z "$GUIDED_DIFFUSION_EVAL_DIR" ]]; then
  echo "VAR README says sampling script was not provided. Generate 50,000 PNG samples with autoregressive_infer_cfg(cfg=1.5, top_p=0.96, top_k=900), pack them with create_npz_from_sample_folder, then set SAMPLE_NPZ and GUIDED_DIFFUSION_EVAL_DIR." >&2
  exit 2
fi

cd "$REPO_DIR"
"${cmd[@]}" | tee "$OUTPUT_DIR/fid_eval.log"
