#!/usr/bin/env bash
# One-click server setup for Schema-Conformance IE training.
# Usage: bash scripts/setup_server.sh [--data_dir /path/to/ace2005]
# Requires: NVIDIA GPU with CUDA, git, Python 3.10+.
# Steps: detect env -> install deps -> download model -> prep data -> dry-run.
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
DATA_DIR=""
MODEL_NAME="Qwen/Qwen3.5-9B"
MODEL_CACHE="/root/autodl-tmp/.hf_cache"

# ---- Parse args ----
while [[ $# -gt 0 ]]; do
    case $1 in
        --data_dir) DATA_DIR="$2"; shift 2;;
        --model_cache) MODEL_CACHE="$2"; shift 2;;
        *) shift;;
    esac
done

echo "========================================="
echo "Schema-Conformance IE — Server Setup"
echo "========================================="
echo "Repo:        ${REPO_DIR}"
echo "Data dir:    ${DATA_DIR:-<not set>}"
echo "Model cache: ${MODEL_CACHE}"
echo ""

# ---- Phase 1: Environment detection ----
echo "[1/6] Detecting environment..."
python3 --version || { echo "ERROR: Python3 not found"; exit 1; }
nvidia-smi --query-gpu=name,memory.total --format=csv,noheader 2>/dev/null || echo "WARNING: No GPU detected"
CUDA_VERSION=$(nvcc --version 2>/dev/null | grep -oP 'release \K[0-9]+\.[0-9]+' || echo "unknown")
echo "CUDA version: ${CUDA_VERSION}"

# ---- Phase 2: Python environment ----
echo ""
echo "[2/6] Setting up Python environment..."

VENV_DIR="${REPO_DIR}/.venv"

if [ -f /root/miniconda3/etc/profile.d/conda.sh ]; then
    echo "Found conda environment (aml-train image)"
    source /root/miniconda3/etc/profile.d/conda.sh
    conda activate base
    PIP="pip"
    PYTHON="python"
elif [ -d "${VENV_DIR}" ]; then
    echo "Found existing venv at ${VENV_DIR}"
    source "${VENV_DIR}/bin/activate"
    PIP="pip"
    PYTHON="python"
else
    echo "Creating venv at ${VENV_DIR}"
    python3 -m venv "${VENV_DIR}"
    source "${VENV_DIR}/bin/activate"
    PIP="pip"
    PYTHON="python"
fi

# ---- Phase 3: Install dependencies ----
echo ""
echo "[3/6] Installing dependencies..."

case "${CUDA_VERSION}" in
    11.8*) TORCH_INDEX="https://download.pytorch.org/whl/cu118";;
    12.1*) TORCH_INDEX="https://download.pytorch.org/whl/cu121";;
    12.4*) TORCH_INDEX="https://download.pytorch.org/whl/cu124";;
    12.6*) TORCH_INDEX="https://download.pytorch.org/whl/cu126";;
    *)     TORCH_INDEX="https://download.pytorch.org/whl/cu124"; echo "WARNING: Unknown CUDA ${CUDA_VERSION}, defaulting to cu124";;
esac

if ${PYTHON} -c "import torch; assert torch.cuda.is_available()" 2>/dev/null; then
    echo "PyTorch with CUDA already installed, skipping"
else
    echo "Installing PyTorch from ${TORCH_INDEX}..."
    ${PIP} install --timeout 300 torch torchvision torchaudio --index-url "${TORCH_INDEX}"
fi

echo "Installing project dependencies..."
${PIP} install --timeout 300 -r "${REPO_DIR}/requirements.txt"

if ${PYTHON} -c "import flash_attn" 2>/dev/null; then
    echo "flash-attn already installed"
else
    echo "Attempting flash-attn install (optional, may take 10+ min)..."
    ${PIP} install flash-attn --no-build-isolation 2>/dev/null || echo "WARNING: flash-attn install failed, will use default attention"
fi

# ---- Phase 4: Verify GPU ----
echo ""
echo "[4/6] Verifying GPU setup..."
${PYTHON} -c "
import torch
print(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')
for i in range(torch.cuda.device_count()):
    props = torch.cuda.get_device_properties(i)
    print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({props.total_mem // 1024**3}GB)')
"

# ---- Phase 5: Download model ----
echo ""
echo "[5/6] Downloading model ${MODEL_NAME}..."
export HF_HOME="${MODEL_CACHE}"
export HF_HUB_DISABLE_XET=1

if [ -d "${MODEL_CACHE}/models--Qwen--Qwen3.5-9B" ] || [ -d "${MODEL_CACHE}/Qwen/Qwen3.5-9B" ]; then
    echo "Model cache found, skipping download"
else
    ${PYTHON} -c "
from transformers import AutoModelForCausalLM, AutoTokenizer
print('Downloading tokenizer...')
AutoTokenizer.from_pretrained('${MODEL_NAME}', trust_remote_code=True)
print('Downloading model...')
AutoModelForCausalLM.from_pretrained('${MODEL_NAME}', trust_remote_code=True)
print('Download complete.')
"
fi

# ---- Phase 6: Data + dry-run ----
echo ""
echo "[6/6] Data check and dry-run..."

if [ -z "${DATA_DIR}" ] || [ ! -d "${DATA_DIR}" ]; then
    echo ""
    echo "================================================================"
    echo "  ACE2005 data not found."
    echo "  ACE2005 requires an LDC license (LDC2006T06)."
    echo "  After obtaining the data, preprocess with DyGIE++ format:"
    echo "    https://github.com/dwadden/dygiepp"
    echo "  Then re-run:"
    echo "    bash scripts/setup_server.sh --data_dir /path/to/ace2005"
    echo ""
    echo "  Alternatively, provide pre-converted JSON:"
    echo "    python -m src.train_grpo --config configs/grpo_baseline.yaml \\"
    echo "        --data_path /path/to/train.json --dry_run"
    echo "================================================================"
    echo ""
    echo "Skipping dry-run (no data). Environment setup complete."
    exit 0
fi

echo "Running dry-run (5 steps) with baseline config..."
cd "${REPO_DIR}"
CUDA_VISIBLE_DEVICES=0 ${PYTHON} -m src.train_grpo \
    --config configs/grpo_baseline.yaml \
    --data_dir "${DATA_DIR}" \
    --output_dir ./output/dry_run \
    --dry_run

echo ""
echo "========================================="
echo "  Setup complete! Dry-run passed."
echo "  To start training:"
echo "    # Group A (F1 only):"
echo "    CUDA_VISIBLE_DEVICES=0 python -m src.train_grpo \\"
echo "        --config configs/grpo_baseline.yaml \\"
echo "        --data_dir ${DATA_DIR}"
echo ""
echo "    # Group B (conformance + GDPO):"
echo "    CUDA_VISIBLE_DEVICES=1 python -m src.train_grpo \\"
echo "        --config configs/grpo_conformance.yaml \\"
echo "        --data_dir ${DATA_DIR}"
echo "========================================="
