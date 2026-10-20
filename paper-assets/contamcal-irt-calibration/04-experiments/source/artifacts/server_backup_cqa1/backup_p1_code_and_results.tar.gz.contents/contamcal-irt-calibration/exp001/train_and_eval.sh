#!/bin/bash
# Single-job chain: SFT train → eval (original + paraphrased).
#
# Usage:
#   bash train_and_eval.sh \
#     --model Qwen/Qwen2.5-0.5B --dosage 5 --seed 42 --gpu 0
#
#   # Eval-only (skip training, just run eval on existing checkpoint):
#   bash train_and_eval.sh \
#     --model Qwen/Qwen2.5-0.5B --dosage 5 --seed 42 --gpu 0 --eval-only

set -euo pipefail

# ── Defaults ──
MODEL=""
DOSAGE=""
SEED=42
GPU="0"
EVAL_ONLY=false
MAX_SAMPLES=""
BASE_DIR="/root/autodl-tmp/exp001"
CACHE_DIR="/root/autodl-tmp/.hf_cache"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BENCHMARK_LIST="mmlu gsm8k arc_challenge humaneval"

export HF_HOME="$CACHE_DIR"

# ── Parse args ──
while [[ $# -gt 0 ]]; do
    case $1 in
        --model)        MODEL="$2";         shift 2 ;;
        --dosage)       DOSAGE="$2";        shift 2 ;;
        --seed)         SEED="$2";          shift 2 ;;
        --gpu)          GPU="$2";           shift 2 ;;
        --eval-only)    EVAL_ONLY=true;     shift ;;
        --max-samples)  MAX_SAMPLES="$2";   shift 2 ;;
        --base-dir)     BASE_DIR="$2";      shift 2 ;;
        --benchmarks)   BENCHMARK_LIST="$2"; shift 2 ;;
        -h|--help)
            echo "Usage: $0 --model MODEL --dosage DOSAGE [--seed 42] [--gpu 0] [--eval-only] [--max-samples N]"
            exit 0 ;;
        *) echo "Unknown arg: $1"; exit 1 ;;
    esac
done

if [[ -z "$MODEL" || -z "$DOSAGE" ]]; then
    echo "ERROR: --model and --dosage are required"
    exit 1
fi

MODEL_SHORT=$(echo "$MODEL" | sed 's|.*/||')
DOSAGE_PAD=$(printf "d%03d" "$DOSAGE")
RUN_TAG="${MODEL_SHORT}_${DOSAGE_PAD}_s${SEED}"

CKPT_DIR="$BASE_DIR/checkpoints/$RUN_TAG"
DATA_DIR="$BASE_DIR/sft_data"
PARA_DIR="$BASE_DIR/paraphrases"
EVAL_DIR="$BASE_DIR/eval_results/$RUN_TAG"
EVAL_DIR_PARA="$BASE_DIR/eval_results/${RUN_TAG}_para"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"; }

# ── Step 1: Training ──
if [[ "$EVAL_ONLY" == false ]]; then
    DATA_FILE="$DATA_DIR/sft_d${DOSAGE}.jsonl"
    if [[ ! -f "$DATA_FILE" ]]; then
        echo "ERROR: training data not found: $DATA_FILE"
        exit 1
    fi

    if [[ -f "$CKPT_DIR/train_config.json" ]]; then
        log "SKIP training: $CKPT_DIR already exists"
    else
        log "Starting SFT training: $RUN_TAG (GPU=$GPU)"
        python3 "$SCRIPT_DIR/train_sft.py" \
            --model-name "$MODEL" \
            --data-path "$DATA_FILE" \
            --output-dir "$CKPT_DIR" \
            --seed "$SEED" \
            --gpu "$GPU" \
            --cache-dir "$CACHE_DIR"
        log "Training complete: $CKPT_DIR"
    fi
fi

# ── Step 2: Eval (original benchmarks) ──
ADAPTER_PATH="$CKPT_DIR/lora_adapter"
if [[ ! -d "$ADAPTER_PATH" ]]; then
    echo "ERROR: adapter not found: $ADAPTER_PATH"
    exit 1
fi

MAX_SAMPLES_FLAG=""
if [[ -n "$MAX_SAMPLES" ]]; then
    MAX_SAMPLES_FLAG="--max-samples $MAX_SAMPLES"
fi

if [[ -f "$EVAL_DIR/eval_results.json" ]]; then
    log "SKIP original eval: $EVAL_DIR already exists"
else
    log "Starting eval (original): $RUN_TAG (GPU=$GPU)"
    mkdir -p "$EVAL_DIR"
    CUDA_VISIBLE_DEVICES="$GPU" python3 "$SCRIPT_DIR/evaluate.py" \
        --model-path "$MODEL" \
        --adapter-path "$ADAPTER_PATH" \
        --benchmarks $BENCHMARK_LIST \
        --output-dir "$EVAL_DIR" \
        --cache-dir "$CACHE_DIR" \
        $MAX_SAMPLES_FLAG
    log "Eval (original) complete: $EVAL_DIR"
fi

# ── Step 3: Eval (paraphrased benchmarks) ──
if [[ -d "$PARA_DIR" ]]; then
    if [[ -f "$EVAL_DIR_PARA/eval_results.json" ]]; then
        log "SKIP paraphrased eval: $EVAL_DIR_PARA already exists"
    else
        log "Starting eval (paraphrased): $RUN_TAG (GPU=$GPU)"
        mkdir -p "$EVAL_DIR_PARA"
        CUDA_VISIBLE_DEVICES="$GPU" python3 "$SCRIPT_DIR/evaluate.py" \
            --model-path "$MODEL" \
            --adapter-path "$ADAPTER_PATH" \
            --benchmarks $BENCHMARK_LIST \
            --output-dir "$EVAL_DIR_PARA" \
            --paraphrase-dir "$PARA_DIR" \
            --cache-dir "$CACHE_DIR" \
            $MAX_SAMPLES_FLAG
        log "Eval (paraphrased) complete: $EVAL_DIR_PARA"
    fi
else
    log "SKIP paraphrased eval: paraphrase dir not found"
fi

log "=== $RUN_TAG pipeline complete ==="
log "Results:"
log "  Original:    $EVAL_DIR/"
log "  Paraphrased: $EVAL_DIR_PARA/"
