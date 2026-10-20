#!/bin/bash
set -e
source /etc/network_turbo 2>/dev/null || true

BASE_DIR="${MODEL_DIR:-./models}"
MIRROR="https://hf-mirror.com"

MODELS=(
    "m-a-p/340M-20B-GatedDeltaNet-pure-baseline"
    "m-a-p/340M-20B-GatedDeltaNet-New-hybrid-24-1"
    "m-a-p/340M-20B-GatedDeltaNet-hybrid-12-1"
    "m-a-p/340M-20B-GatedDeltaNet-hybrid-6-1"
    "m-a-p/340M-20B-GatedDeltaNet-hybrid-3-1"
    "m-a-p/340M-20B-HGRN2-pure-baseline"
    "m-a-p/340M-20B-HGRN2-hybrid-24-1"
    "m-a-p/340M-20B-HGRN2-hybrid-12-1"
    "m-a-p/340M-20B-HGRN2-hybrid-6-1"
    "m-a-p/340M-20B-HGRN2-hybrid-3-1"
    "m-a-p/340M-20B-RetNet-pure"
    "m-a-p/340M-20B-RetNet-hybrid-24-1"
    "m-a-p/340M-20B-RetNet-hybrid-12-1"
    "m-a-p/340M-20B-RetNet-hybrid-6-1"
    "m-a-p/340M-20B-RetNet-hybrid-3-1"
    "m-a-p/transformer_340M_baseline"
)

# Files to download for each model
FILES="config.json generation_config.json model.safetensors special_tokens_map.json tokenizer.json tokenizer_config.json"

total=${#MODELS[@]}
ok=0
fail=0

for i in "${!MODELS[@]}"; do
    repo="${MODELS[$i]}"
    model_name="${repo#*/}"
    dir="$BASE_DIR/$model_name"
    idx=$((i+1))
    
    # Skip if already complete
    if [ -f "$dir/config.json" ] && ls "$dir"/*.safetensors 1>/dev/null 2>&1; then
        echo "[$idx/$total] SKIP (exists): $model_name"
        ok=$((ok+1))
        continue
    fi
    
    mkdir -p "$dir"
    echo "[$idx/$total] Downloading: $model_name"
    t_start=$(date +%s)
    model_ok=true
    
    for fname in $FILES; do
        url="$MIRROR/$repo/resolve/main/$fname"
        dest="$dir/$fname"
        if [ -f "$dest" ] && [ -s "$dest" ]; then
            continue
        fi
        # Try wget with resume support
        if ! wget -q --timeout=120 --tries=3 -O "$dest" "$url" 2>/dev/null; then
            # Some models might not have generation_config.json
            if [ "$fname" = "generation_config.json" ]; then
                rm -f "$dest"
                continue
            fi
            echo "  WARN: failed to download $fname"
            rm -f "$dest"
            model_ok=false
        fi
    done
    
    t_end=$(date +%s)
    elapsed=$((t_end - t_start))
    
    if $model_ok && [ -f "$dir/config.json" ] && ls "$dir"/*.safetensors 1>/dev/null 2>&1; then
        echo "  OK (${elapsed}s)"
        ok=$((ok+1))
    else
        echo "  FAILED (${elapsed}s)"
        fail=$((fail+1))
    fi
done

echo ""
echo "============================================================"
echo "SUMMARY: $ok OK, $fail failed out of $total"
echo "============================================================"
echo "DONE"
