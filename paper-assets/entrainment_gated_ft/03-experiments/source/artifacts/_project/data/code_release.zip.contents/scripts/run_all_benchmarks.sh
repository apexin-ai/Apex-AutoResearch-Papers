#!/bin/bash
set -e
source ${CONDA_SH:-$HOME/miniconda3/etc/profile.d/conda.sh} && conda activate base
source /etc/network_turbo
export HF_ENDPOINT=https://hf-mirror.com
export CUDA_VISIBLE_DEVICES=0

SCRIPT=${PROJECT_ROOT:-.}/scripts/run_lmeval_fla.py
TASKS="lambada_openai,hellaswag,arc_easy,arc_challenge,winogrande"

# Model 1: Transformer baseline
echo "=== Starting Transformer baseline ==="
MODEL_PATH="${MODEL_DIR:-./models_1.3b}/transformer_1.3B_baseline"
OUTPUT_DIR="${PROJECT_ROOT:-.}/results_1.3b/lm_eval/transformer_baseline_v2"
mkdir -p "$OUTPUT_DIR"
python3 $SCRIPT --model hf --model_args pretrained=$MODEL_PATH,trust_remote_code=True,dtype=bfloat16 --tasks $TASKS --batch_size auto --output_path "$OUTPUT_DIR" --log_samples 2>&1 | tee "$OUTPUT_DIR/run.log"
echo "=== Transformer baseline DONE ==="

# Model 2: GatedDeltaNet hybrid 3:1
echo "=== Starting GatedDeltaNet hybrid ==="
MODEL_PATH="${MODEL_DIR:-./models_1.3b}/1.3B-100B-GatedDeltaNet-hybrid-3-1"
OUTPUT_DIR="${PROJECT_ROOT:-.}/results_1.3b/lm_eval/gated_deltanet_hybrid"
mkdir -p "$OUTPUT_DIR"
python3 $SCRIPT --model hf --model_args pretrained=$MODEL_PATH,trust_remote_code=True,dtype=bfloat16 --tasks $TASKS --batch_size auto --output_path "$OUTPUT_DIR" --log_samples 2>&1 | tee "$OUTPUT_DIR/run.log"
echo "=== GatedDeltaNet hybrid DONE ==="

# Model 3: RetNet pure
echo "=== Starting RetNet pure ==="
MODEL_PATH="${MODEL_DIR:-./models_1.3b}/1.3B-100B-RetNet-pure"
OUTPUT_DIR="${PROJECT_ROOT:-.}/results_1.3b/lm_eval/retnet_pure"
mkdir -p "$OUTPUT_DIR"
python3 $SCRIPT --model hf --model_args pretrained=$MODEL_PATH,trust_remote_code=True,dtype=bfloat16 --tasks $TASKS --batch_size auto --output_path "$OUTPUT_DIR" --log_samples 2>&1 | tee "$OUTPUT_DIR/run.log"
echo "=== RetNet pure DONE ==="

# MMLU 5-shot for all three
echo "=== Starting MMLU 5-shot runs ==="

echo "--- Transformer MMLU ---"
MODEL_PATH="${MODEL_DIR:-./models_1.3b}/transformer_1.3B_baseline"
OUTPUT_DIR="${PROJECT_ROOT:-.}/results_1.3b/lm_eval/transformer_baseline_v2"
python3 $SCRIPT --model hf --model_args pretrained=$MODEL_PATH,trust_remote_code=True,dtype=bfloat16 --tasks mmlu --num_fewshot 5 --batch_size auto --output_path "$OUTPUT_DIR" --log_samples 2>&1 | tee -a "$OUTPUT_DIR/run.log"

echo "--- GatedDeltaNet MMLU ---"
MODEL_PATH="${MODEL_DIR:-./models_1.3b}/1.3B-100B-GatedDeltaNet-hybrid-3-1"
OUTPUT_DIR="${PROJECT_ROOT:-.}/results_1.3b/lm_eval/gated_deltanet_hybrid"
python3 $SCRIPT --model hf --model_args pretrained=$MODEL_PATH,trust_remote_code=True,dtype=bfloat16 --tasks mmlu --num_fewshot 5 --batch_size auto --output_path "$OUTPUT_DIR" --log_samples 2>&1 | tee -a "$OUTPUT_DIR/run.log"

echo "--- RetNet MMLU ---"
MODEL_PATH="${MODEL_DIR:-./models_1.3b}/1.3B-100B-RetNet-pure"
OUTPUT_DIR="${PROJECT_ROOT:-.}/results_1.3b/lm_eval/retnet_pure"
python3 $SCRIPT --model hf --model_args pretrained=$MODEL_PATH,trust_remote_code=True,dtype=bfloat16 --tasks mmlu --num_fewshot 5 --batch_size auto --output_path "$OUTPUT_DIR" --log_samples 2>&1 | tee -a "$OUTPUT_DIR/run.log"

echo "=== ALL BENCHMARKS COMPLETE ==="
