#!/bin/bash
# Download Qwen3 models for policy_ambiguity_safety experiments
# Run on AutoDL server before serving

set -euo pipefail

# AutoDL proxy setup
source /etc/network_turbo 2>/dev/null || true
export HF_HUB_DISABLE_XET=1
export HF_HOME=/root/autodl-tmp/.hf_cache
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt

MODEL_DIR="/root/autodl-tmp/models"
mkdir -p "$MODEL_DIR"

download_hf() {
    local model=$1
    local dest=$2
    echo "=== Downloading $model via HuggingFace CLI ==="

    local start_time=$SECONDS
    huggingface-cli download "$model" --local-dir "$dest" &
    local pid=$!

    sleep 60
    if kill -0 "$pid" 2>/dev/null; then
        local size_now
        size_now=$(du -sb "$dest" 2>/dev/null | awk '{print $1}')
        size_now=${size_now:-0}
        local speed=$((size_now / 60))
        if [ "$speed" -lt 512000 ]; then
            echo "WARNING: HF download speed ~$((speed / 1024))KB/s, falling back to ModelScope"
            kill "$pid" 2>/dev/null || true
            wait "$pid" 2>/dev/null || true
            return 1
        fi
    fi

    wait "$pid"
}

download_modelscope() {
    local model=$1
    local dest=$2
    echo "=== Downloading $model via ModelScope ==="
    pip install modelscope -q 2>/dev/null
    python3 -c "
from modelscope import snapshot_download
snapshot_download('$model', cache_dir='$dest')
"
}

download_model() {
    local model=$1
    local dirname=$2
    local dest="$MODEL_DIR/$dirname"

    if [ -d "$dest" ] && [ "$(ls -A "$dest" 2>/dev/null)" ]; then
        echo "=== $model already exists at $dest, skipping ==="
        return 0
    fi

    download_hf "$model" "$dest" || download_modelscope "$model" "$MODEL_DIR"
}

download_model "Qwen/Qwen3-8B" "Qwen3-8B"
download_model "Qwen/Qwen3-32B-AWQ" "Qwen3-32B-AWQ"

echo ""
echo "=== Download complete ==="
ls -lh "$MODEL_DIR"
