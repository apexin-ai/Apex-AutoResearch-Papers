#!/bin/bash
# Phase 2 deployment script for cqa1-21977
# Syncs Phase 2 code to server and runs dry-run validation

set -e

SERVER="connect.cqa1.seetacloud.com"
REMOTE_DIR="/root/structfuse-context"
LOCAL_ARTIFACTS="/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/min_necessary_circuit_css/artifacts"

# 1. 文件清单 — 需要传到服务器的文件
FILES=(
    "ifr_scoring.py"
    "eap_ig_scoring.py"
    "edge_pruning_scoring.py"
    "css.py"
    "model_adapter.py"
    "run_circus.py"
)

echo "=== Phase 2 Deployment ==="
echo "Server: $SERVER"
echo "Remote dir: $REMOTE_DIR"
echo ""

# 2. SCP 传输
echo "--- Uploading files ---"
for f in "${FILES[@]}"; do
    if [ -f "$LOCAL_ARTIFACTS/$f" ]; then
        echo "  Uploading $f ..."
        scp "$LOCAL_ARTIFACTS/$f" "root@$SERVER:$REMOTE_DIR/$f"
    else
        echo "  WARNING: $LOCAL_ARTIFACTS/$f not found, skipping"
    fi
done
echo ""

# 3. 依赖检查（远程执行）
echo "--- Dependency check ---"
ssh root@$SERVER 'bash -c '\''
    source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
    echo "=== Python packages ==="
    pip list 2>/dev/null | grep -iE "torch|transformers|einops|accelerate|numpy|scipy"
    echo ""
    echo "=== Qwen model check ==="
    if [ -d /root/autodl-tmp/.hf_cache/models--Qwen--Qwen2.5-0.5B ]; then
        echo "QWEN_CACHED"
        ls -lh /root/autodl-tmp/.hf_cache/models--Qwen--Qwen2.5-0.5B/snapshots/*/model.safetensors 2>/dev/null || echo "  (safetensors not found in snapshot)"
    else
        find /root/autodl-tmp/ -maxdepth 3 -name "*Qwen2.5-0.5B*" -type d 2>/dev/null | head -5
        if [ $? -ne 0 ] || [ -z "$(find /root/autodl-tmp/ -maxdepth 3 -name "*Qwen2.5-0.5B*" -type d 2>/dev/null)" ]; then
            echo "QWEN_NOT_CACHED"
        fi
    fi
'\'''
echo ""

# 4. Dry-run（不用 GPU，验证 import + config + edge 枚举）
echo "--- Dry-run import test ---"
ssh root@$SERVER 'bash -c '\''
    source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
    cd /root/structfuse-context
    CUDA_VISIBLE_DEVICES="" python3 -c "
from run_circus import *
from css import binarize_scores, compute_css_matrix
from model_adapter import ModelAdapter
from ifr_scoring import compute_ifr_edges
from eap_ig_scoring import compute_eap_ig_edges
from edge_pruning_scoring import compute_edge_pruning_scores
print(\"IMPORT OK\")
"
'\'''

echo ""
echo "=== Deployment complete ==="
