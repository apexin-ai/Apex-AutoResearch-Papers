#!/bin/bash
# d066: Beam Width Sweep - SciERC (westd-21461)
# GPU0: Llama-3.1-8B LoRA SciERC, beam k=1,2,4,8, unconstrained + constrained
# GPU1: Qwen3-8B LoRA SciERC, beam k=1,2,4,8, unconstrained + constrained
# Usage: bash scripts/d066_beam_sweep_scierc.sh
set -euo pipefail

source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/schema_semantic_constrained_ie

OUTDIR="/root/autodl-tmp/schema_outputs/d066_beam_sweep"
VIOL_DIR="${OUTDIR}/violations"
mkdir -p "$OUTDIR" "$VIOL_DIR"

LLAMA_MODEL="/root/autodl-tmp/checkpoints/llama_lora_scierc_merged"
QWEN_MODEL="/root/autodl-tmp/checkpoints/qwen3_8b_lora_scierc_merged"
DATA_PATH="data/processed_data/test.json"
CONSTRAINTS_PATH="ontology_constraints.json"
MAX_NEW_TOKENS=2048
BEAMS=(1 2 4 8)

run_inference() {
    local gpu=$1 model_path=$2 model_name=$3 beam=$4 mode=$5
    local out_name="${model_name}_scierc_beam${beam}_${mode}"
    local out_file="${OUTDIR}/${out_name}.jsonl"

    if [ -f "$out_file" ]; then
        local n_lines=$(wc -l < "$out_file")
        if [ "$n_lines" -ge 100 ]; then
            echo "$(date): SKIP ${out_name} (already complete: ${n_lines} lines)"
            return 0
        fi
    fi

    echo "$(date): START ${out_name} on GPU${gpu}"
    CUDA_VISIBLE_DEVICES=$gpu python run_constrained_extraction.py \
        --mode "$mode" \
        --dataset scierc \
        --model_path "$model_path" \
        --data_path "$DATA_PATH" \
        --constraints_path "$CONSTRAINTS_PATH" \
        --output_path "$out_file" \
        --device cuda:0 \
        --max_new_tokens $MAX_NEW_TOKENS \
        --seed 42 \
        --decoding_strategy beam \
        --num_beams "$beam" \
        --skip_on_error
    echo "$(date): DONE ${out_name}"
}

run_violation_check() {
    local model_name=$1 beam=$2 mode=$3
    local out_name="${model_name}_scierc_beam${beam}_${mode}"
    local in_file="${OUTDIR}/${out_name}.jsonl"
    local viol_file="${VIOL_DIR}/${out_name}_violations.json"

    if [ ! -f "$in_file" ]; then
        echo "WARN: ${in_file} not found, skipping violation check"
        return 0
    fi

    python violation_checker.py \
        --input_path "$in_file" \
        --constraints_path "$CONSTRAINTS_PATH" \
        --output_path "$viol_file"
}

run_gpu0() {
    echo "=== GPU0: Llama SciERC Beam Sweep ==="
    for beam in "${BEAMS[@]}"; do
        run_inference 0 "$LLAMA_MODEL" llama "$beam" unconstrained
        run_inference 0 "$LLAMA_MODEL" llama "$beam" full_s1
    done
    echo "=== GPU0: Llama violation checks ==="
    for beam in "${BEAMS[@]}"; do
        run_violation_check llama "$beam" unconstrained
        run_violation_check llama "$beam" full_s1
    done
    echo "=== GPU0: ALL DONE ==="
}

run_gpu1() {
    echo "=== GPU1: Qwen SciERC Beam Sweep ==="
    for beam in "${BEAMS[@]}"; do
        run_inference 1 "$QWEN_MODEL" qwen "$beam" unconstrained
        run_inference 1 "$QWEN_MODEL" qwen "$beam" full_s1
    done
    echo "=== GPU1: Qwen violation checks ==="
    for beam in "${BEAMS[@]}"; do
        run_violation_check qwen "$beam" unconstrained
        run_violation_check qwen "$beam" full_s1
    done
    echo "=== GPU1: ALL DONE ==="
}

# Run both GPUs in parallel
run_gpu0 > >(tee "${OUTDIR}/d066_scierc_gpu0.log") 2>&1 &
PID_GPU0=$!

run_gpu1 > >(tee "${OUTDIR}/d066_scierc_gpu1.log") 2>&1 &
PID_GPU1=$!

echo "GPU0 PID=$PID_GPU0, GPU1 PID=$PID_GPU1"
echo "Waiting for both GPUs..."
wait $PID_GPU0 && echo "GPU0 finished OK" || echo "GPU0 FAILED"
wait $PID_GPU1 && echo "GPU1 finished OK" || echo "GPU1 FAILED"

echo "$(date): === d066 SciERC beam sweep COMPLETE ==="
