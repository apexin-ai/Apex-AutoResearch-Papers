#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
AUTOREP_ROOT="${AUTOREP_ROOT:-$(cd "$SCRIPT_DIR/../../.." && pwd)}"
DATA_ROOT="${DATA_ROOT:-$AUTOREP_ROOT/data/paper_exact/var_imagenet256}"
IMAGENET_ROOT="${IMAGENET_ROOT:-}"

mkdir -p "$DATA_ROOT/checkpoints" "$DATA_ROOT/fid_refs"

cmd_weights=(python3 "$AUTOREP_ROOT/tasks/ablations/no_feedback/hf_curl_download.py" FoundationVision/var vae_ch160v4096z32.pth var_d16.pth --local-dir "$DATA_ROOT/checkpoints")
cmd_ref=(curl -L --fail --show-error --retry 100 --retry-delay 5 --retry-all-errors --retry-max-time 0 --connect-timeout 30 --speed-time 180 --speed-limit 1024 -C - -o "$DATA_ROOT/fid_refs/VIRTUAL_imagenet256_labeled.npz.part" "https://openaipublic.blob.core.windows.net/diffusion/jul-2021/ref_batches/imagenet/256/VIRTUAL_imagenet256_labeled.npz")

printf 'Weights command:'
printf ' %q' "${cmd_weights[@]}"
printf '\n'
printf 'FID ref command:'
printf ' %q' "${cmd_ref[@]}"
printf '\n'

if [[ -z "$IMAGENET_ROOT" ]]; then
  echo "IMAGENET_ROOT is not set. ImageNet is license-restricted and must be prepared manually with train/ and val/ folders." >&2
else
  echo "$IMAGENET_ROOT" > "$DATA_ROOT/IMAGENET_ROOT.txt"
fi

if [[ "${DRY_RUN:-0}" == "1" ]]; then
  exit 0
fi

"${cmd_weights[@]}"
if [[ -f "$DATA_ROOT/fid_refs/VIRTUAL_imagenet256_labeled.npz" ]]; then
  echo "FID ref exists, skipping: $DATA_ROOT/fid_refs/VIRTUAL_imagenet256_labeled.npz"
else
  for attempt in $(seq 1 "${CURL_FILE_ATTEMPTS:-50}"); do
    if "${cmd_ref[@]}"; then
      break
    fi
    if [[ "$attempt" == "${CURL_FILE_ATTEMPTS:-50}" ]]; then
      echo "FID ref failed after $attempt attempts" >&2
      exit 1
    fi
    sleep $((attempt * 10 > 300 ? 300 : attempt * 10))
  done
  mv "$DATA_ROOT/fid_refs/VIRTUAL_imagenet256_labeled.npz.part" "$DATA_ROOT/fid_refs/VIRTUAL_imagenet256_labeled.npz"
fi
