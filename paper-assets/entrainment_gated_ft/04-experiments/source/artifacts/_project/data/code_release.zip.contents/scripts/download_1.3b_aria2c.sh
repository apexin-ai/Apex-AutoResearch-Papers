#!/bin/bash
set -e
source ${CONDA_SH:-$HOME/miniconda3/etc/profile.d/conda.sh} && conda activate base
source /etc/network_turbo 2>/dev/null || true

HF_MIRROR="https://hf-mirror.com"
BASE_DIR="${MODEL_DIR:-./models_1.3b}"
PYTHON="${PYTHON:-python3}"

MODELS=(
  "1.3B-100B-GatedDeltaNet-pure"
  "1.3B-100B-GatedDeltaNet-hybrid-24-1"
  "1.3B-100B-GatedDeltaNet-hybrid-12-1"
  "1.3B-100B-GatedDeltaNet-hybrid-6-1"
  "1.3B-100B-HGRN2-pure"
  "1.3B-100B-HGRN2-hybrid-24-1"
  "1.3B-100B-HGRN2-hybrid-12-1"
  "1.3B-100B-HGRN2-hybrid-6-1"
  "1.3B-100B-HGRN2-hybrid-3-1"
  "1.3B-100B-RetNet-hybrid-24-1"
  "1.3B-100B-RetNet-hybrid-12-1"
  "1.3B-100B-RetNet-hybrid-6-1"
  "1.3B-100B-RetNet-hybrid-3-1"
)

download_model() {
  local model_name="$1"
  local repo="m-a-p/$model_name"
  local target="$BASE_DIR/$model_name"

  if [ -f "$target/config.json" ] && find "$target" -name "*.safetensors" -size +100M 2>/dev/null | grep -q .; then
    echo "=== SKIP $model_name (already complete: $(du -sh "$target" | cut -f1)) ==="
    return 0
  fi

  echo "=== DOWNLOADING $model_name ==="
  mkdir -p "$target"

  local files
  files=$(curl -sf "$HF_MIRROR/api/models/$repo" | $PYTHON -c "
import sys, json
data = json.load(sys.stdin)
for s in data.get('siblings', []):
    print(s['rfilename'])
" 2>/dev/null)

  if [ -z "$files" ]; then
    echo "WARN: API failed for $model_name, trying common file list..."
    files="config.json
model.safetensors
tokenizer.json
tokenizer_config.json
special_tokens_map.json
generation_config.json"
  fi

  local fail=0
  while IFS= read -r fname; do
    [ -z "$fname" ] && continue
    local url="$HF_MIRROR/$repo/resolve/main/$fname"
    local out_dir="$target/$(dirname "$fname")"
    local out_name="$(basename "$fname")"
    mkdir -p "$out_dir"

    if echo "$fname" | grep -qE '\.safetensors$|\.bin$'; then
      echo "  aria2c (16x): $fname"
      if ! aria2c -x16 -s16 -k1M --allow-overwrite=true --file-allocation=none --console-log-level=error -d "$out_dir" -o "$out_name" "$url"; then
        echo "  FAILED: $fname"
        fail=1
      fi
    else
      echo "  wget: $fname"
      if ! wget -q -O "$out_dir/$out_name" "$url"; then
        echo "  FAILED: $fname (wget)"
        fail=1
      fi
    fi
  done <<< "$files"

  if [ -f "$target/config.json" ] && find "$target" -name "*.safetensors" -size +100M 2>/dev/null | grep -q .; then
    echo "=== OK: $model_name ($(du -sh "$target" | cut -f1)) ==="
    return 0
  else
    echo "=== FAILED: $model_name ==="
    return 1
  fi
}

echo "Starting batch download at $(date)"
completed=0
failed=0
failed_list=""

for model in "${MODELS[@]}"; do
  if download_model "$model"; then
    completed=$((completed + 1))
  else
    failed=$((failed + 1))
    failed_list="$failed_list $model"
  fi
done

echo ""
echo "========================================="
echo "DONE: $completed completed, $failed failed"
if [ -n "$failed_list" ]; then
  echo "FAILED:$failed_list"
fi
echo "Finished at $(date)"
echo "========================================="
du -sh "$BASE_DIR"/*/
df -h ${DATA_DIR:-./data}/
