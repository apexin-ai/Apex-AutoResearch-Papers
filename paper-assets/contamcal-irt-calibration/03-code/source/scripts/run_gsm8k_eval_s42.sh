#!/bin/bash
set -euo pipefail

export HF_DATASETS_OFFLINE=1
export HF_HUB_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
export HF_HOME=/root/autodl-tmp/.hf_cache

GPU=${1:-0}
export CUDA_VISIBLE_DEVICES=$GPU

PYTHON=/root/miniconda3/bin/python
EVAL_SCRIPT=/root/contamcal-irt-calibration/exp001/evaluate.py
CKPT_DIR=/root/autodl-tmp/exp001/checkpoints
OUT_DIR=/root/autodl-tmp/exp001/eval_results_gsm8k

mkdir -p "$OUT_DIR"

echo "============================================"
echo "GSM8K evaluation (seed=42, all models x dosages)"
echo "GPU: $GPU (CUDA_VISIBLE_DEVICES=$CUDA_VISIBLE_DEVICES)"
echo "Start: $(date)"
echo "============================================"

run_eval() {
    local family="$1"
    local base_model="$2"
    local dosage="$3"
    local ckpt_name="${family}_${dosage}_s42"
    local adapter_path="${CKPT_DIR}/${ckpt_name}/lora_adapter"
    local output_dir="${OUT_DIR}/${ckpt_name}"

    if [ ! -f "${adapter_path}/adapter_model.safetensors" ]; then
        echo ">>> SKIP ${ckpt_name}: adapter not found at ${adapter_path}"
        return 0
    fi

    if [ -f "${output_dir}/.done" ]; then
        echo ">>> SKIP ${ckpt_name}: already evaluated (found .done)"
        return 0
    fi

    echo ""
    echo "=== START: ${ckpt_name} (gsm8k) ==="
    echo "Base model: ${base_model}"
    echo "Adapter: ${adapter_path}"
    echo "Output: ${output_dir}"
    date

    $PYTHON "$EVAL_SCRIPT" \
        --model-path "$base_model" \
        --adapter-path "$adapter_path" \
        --benchmarks gsm8k \
        --output-dir "$output_dir" \
        --batch-size 8

    echo "=== DONE: ${ckpt_name} gsm8k ==="
    date
    echo ""
}

# ── Priority 1: d000 + d100 (boundary dosages) ──

# Qwen2.5-7B
run_eval "Qwen2.5-7B" "/root/autodl-tmp/models/Qwen2.5-7B" "d000"
run_eval "Qwen2.5-7B" "/root/autodl-tmp/models/Qwen2.5-7B" "d100"

# Qwen2.5-14B
run_eval "Qwen2.5-14B" "/root/autodl-tmp/models/Qwen2.5-14B" "d000"
run_eval "Qwen2.5-14B" "/root/autodl-tmp/models/Qwen2.5-14B" "d100"

# gemma-2-9b
run_eval "gemma-2-9b" "/root/autodl-tmp/models/gemma-2-9b" "d000"
run_eval "gemma-2-9b" "/root/autodl-tmp/models/gemma-2-9b" "d100"

# phi-4
run_eval "phi-4" "/root/autodl-tmp/models/phi-4" "d000"
run_eval "phi-4" "/root/autodl-tmp/models/phi-4" "d100"

# OLMo-2-7B
run_eval "OLMo-2-7B" "/root/autodl-tmp/models/OLMo-2-1124-7B" "d000"
run_eval "OLMo-2-7B" "/root/autodl-tmp/models/OLMo-2-1124-7B" "d100"

echo ">>> Priority 1 (d000 + d100) complete"

# ── Priority 2: d005, d025, d050 (intermediate dosages) ──

# Qwen2.5-7B
run_eval "Qwen2.5-7B" "/root/autodl-tmp/models/Qwen2.5-7B" "d005"
run_eval "Qwen2.5-7B" "/root/autodl-tmp/models/Qwen2.5-7B" "d025"
run_eval "Qwen2.5-7B" "/root/autodl-tmp/models/Qwen2.5-7B" "d050"

# Qwen2.5-14B
run_eval "Qwen2.5-14B" "/root/autodl-tmp/models/Qwen2.5-14B" "d005"
run_eval "Qwen2.5-14B" "/root/autodl-tmp/models/Qwen2.5-14B" "d025"
run_eval "Qwen2.5-14B" "/root/autodl-tmp/models/Qwen2.5-14B" "d050"

# gemma-2-9b
run_eval "gemma-2-9b" "/root/autodl-tmp/models/gemma-2-9b" "d005"
run_eval "gemma-2-9b" "/root/autodl-tmp/models/gemma-2-9b" "d025"
run_eval "gemma-2-9b" "/root/autodl-tmp/models/gemma-2-9b" "d050"

# phi-4
run_eval "phi-4" "/root/autodl-tmp/models/phi-4" "d005"
run_eval "phi-4" "/root/autodl-tmp/models/phi-4" "d025"
run_eval "phi-4" "/root/autodl-tmp/models/phi-4" "d050"

# OLMo-2-7B
run_eval "OLMo-2-7B" "/root/autodl-tmp/models/OLMo-2-1124-7B" "d005"
run_eval "OLMo-2-7B" "/root/autodl-tmp/models/OLMo-2-1124-7B" "d025"
run_eval "OLMo-2-7B" "/root/autodl-tmp/models/OLMo-2-1124-7B" "d050"

echo "============================================"
echo "All GSM8K evaluations complete!"
echo "End: $(date)"
echo "Results in: ${OUT_DIR}"
echo "============================================"
