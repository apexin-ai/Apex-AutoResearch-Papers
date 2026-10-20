#!/bin/bash
# 3B s42 para_aligned eval — one function per dose, call with GPU index as $1

BASE_MODEL="/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-3B"
EVAL_SCRIPT="/root/contamcal-irt-calibration/exp001/evaluate.py"
PARA_DIR="/root/autodl-tmp/exp001/paraphrases"
CACHE_DIR="/root/autodl-tmp/.hf_cache"
EVAL_OUT="/root/autodl-tmp/exp001/eval_results"
CONDA_ACTIVATE="source /root/miniconda3/etc/profile.d/conda.sh && conda activate base"

run_d000() {
    local GPU=${1:?Usage: run_d000 <GPU_ID>}
    eval "$CONDA_ACTIVATE"
    CUDA_VISIBLE_DEVICES=$GPU python $EVAL_SCRIPT \
        --model-path $BASE_MODEL \
        --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d000_a32_s42/lora_adapter \
        --output-dir $EVAL_OUT/Qwen2.5-3B_d000_s42_a32_para_aligned \
        --benchmarks mmlu gsm8k arc_challenge humaneval \
        --mc-format aligned \
        --paraphrase-dir $PARA_DIR \
        --cache-dir $CACHE_DIR
}

run_d005() {
    local GPU=${1:?Usage: run_d005 <GPU_ID>}
    eval "$CONDA_ACTIVATE"
    CUDA_VISIBLE_DEVICES=$GPU python $EVAL_SCRIPT \
        --model-path $BASE_MODEL \
        --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d005_s42/lora_adapter \
        --output-dir $EVAL_OUT/Qwen2.5-3B_d005_s42_a32_para_aligned \
        --benchmarks mmlu gsm8k arc_challenge humaneval \
        --mc-format aligned \
        --paraphrase-dir $PARA_DIR \
        --cache-dir $CACHE_DIR
}

run_d100() {
    local GPU=${1:?Usage: run_d100 <GPU_ID>}
    eval "$CONDA_ACTIVATE"
    CUDA_VISIBLE_DEVICES=$GPU python $EVAL_SCRIPT \
        --model-path $BASE_MODEL \
        --adapter-path /root/autodl-tmp/exp001/checkpoints/Qwen2.5-3B_d100_a32_s42_v3/lora_adapter \
        --output-dir $EVAL_OUT/Qwen2.5-3B_d100_s42_a32_para_aligned \
        --benchmarks mmlu gsm8k arc_challenge humaneval \
        --mc-format aligned \
        --paraphrase-dir $PARA_DIR \
        --cache-dir $CACHE_DIR
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo "Usage: source this script, then call run_d000/run_d005/run_d100 <GPU_ID>"
    echo "  e.g.: source run_3B_s42_para_aligned.sh && run_d000 2"
    echo ""
    echo "Or run directly: bash run_3B_s42_para_aligned.sh <d000|d005|d100> <GPU_ID>"
    DOSE=${1:-}
    GPU=${2:-}
    if [[ -n "$DOSE" && -n "$GPU" ]]; then
        run_${DOSE} $GPU
    fi
fi
