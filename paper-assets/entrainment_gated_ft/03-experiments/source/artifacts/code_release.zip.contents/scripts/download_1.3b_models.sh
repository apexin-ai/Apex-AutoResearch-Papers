#!/bin/bash
unset http_proxy https_proxy HTTP_PROXY HTTPS_PROXY REQUESTS_CA_BUNDLE SSL_CERT_FILE

MIRROR="https://hf-mirror.com"
SAVE_DIR="${MODEL_DIR:-./models_1.3b}"
mkdir -p "$SAVE_DIR"

MODELS=(
    "m-a-p/1.3B-100B-GatedDeltaNet-pure"
    "m-a-p/1.3B-100B-GatedDeltaNet-hybrid-24-1"
    "m-a-p/1.3B-100B-GatedDeltaNet-hybrid-12-1"
    "m-a-p/1.3B-100B-GatedDeltaNet-hybrid-6-1"
    "m-a-p/1.3B-100B-GatedDeltaNet-hybrid-3-1"
    "m-a-p/1.3B-100B-HGRN2-pure"
    "m-a-p/1.3B-100B-HGRN2-hybrid-24-1"
    "m-a-p/1.3B-100B-HGRN2-hybrid-12-1"
    "m-a-p/1.3B-100B-HGRN2-hybrid-6-1"
    "m-a-p/1.3B-100B-HGRN2-hybrid-3-1"
    "m-a-p/1.3B-100B-RetNet-pure"
    "m-a-p/1.3B-100B-RetNet-hybrid-24-1"
    "m-a-p/1.3B-100B-RetNet-hybrid-12-1"
    "m-a-p/1.3B-100B-RetNet-hybrid-6-1"
    "m-a-p/1.3B-100B-RetNet-hybrid-3-1"
    "m-a-p/transformer_1.3B_baseline"
)

download_file() {
    local url="$1"
    local dest="$2"
    local max_retries=5
    local retry=0
    
    while [ $retry -lt $max_retries ]; do
        curl -s -f -L -C - -o "$dest" --connect-timeout 30 --max-time 1800 "$url"
        if [ $? -eq 0 ] && [ -f "$dest" ] && [ -s "$dest" ]; then
            return 0
        fi
        retry=$((retry+1))
        echo "      Retry $retry/$max_retries for $(basename $dest)" >&2
        sleep 5
    done
    return 1
}

TOTAL=${#MODELS[@]}
OK=0
SKIP=0
FAIL=0

for i in "${!MODELS[@]}"; do
    idx=$((i+1))
    model="${MODELS[$i]}"
    local_name="${model#*/}"
    local_dir="$SAVE_DIR/$local_name"
    
    if [ -f "$local_dir/config.json" ] && ls "$local_dir"/model*.safetensors >/dev/null 2>&1; then
        # Verify file sizes are reasonable (>100MB for safetensors)
        min_size=$(find "$local_dir" -name "*.safetensors" -size +100M 2>/dev/null | wc -l)
        if [ "$min_size" -gt 0 ]; then
            echo "[$idx/$TOTAL] SKIP (exists): $local_name"
            SKIP=$((SKIP+1))
            continue
        fi
    fi
    
    echo "[$idx/$TOTAL] Downloading: $model"
    START=$(date +%s)
    mkdir -p "$local_dir"
    
    # Get file list from API
    files=$(curl -s -f "$MIRROR/api/models/$model" | python3 -c "
import sys, json
data = json.load(sys.stdin)
for s in data.get('siblings', []):
    f = s['rfilename']
    if f != '.gitattributes':
        print(f)
")
    
    all_ok=true
    for fname in $files; do
        dest="$local_dir/$fname"
        if [ -f "$dest" ]; then
            continue
        fi
        url="$MIRROR/$model/resolve/main/$fname"
        
        fstart=$(date +%s)
        if download_file "$url" "$dest"; then
            fend=$(date +%s)
            fsize=$(stat -c%s "$dest" 2>/dev/null || echo 0)
            fsize_mb=$((fsize / 1048576))
            ftime=$((fend - fstart))
            if [ $ftime -gt 0 ]; then
                speed=$((fsize_mb / ftime))
            else
                speed=$fsize_mb
            fi
            echo "    $fname: ${fsize_mb}MB in ${ftime}s (${speed} MB/s)"
        else
            echo "    FAILED: $fname"
            all_ok=false
            break
        fi
    done
    
    END=$(date +%s)
    DT=$((END-START))
    
    if $all_ok; then
        SIZE=$(du -sh "$local_dir" | cut -f1)
        echo "[$idx/$TOTAL] OK: $local_name ($SIZE in ${DT}s)"
        OK=$((OK+1))
    else
        echo "[$idx/$TOTAL] FAILED: $local_name"
        FAIL=$((FAIL+1))
    fi
done

echo ""
echo "Summary: $OK downloaded, $SKIP skipped, $FAIL failed"
echo "Done."
