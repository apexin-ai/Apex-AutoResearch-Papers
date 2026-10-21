#!/bin/bash
# exp-001 Controlled SFT Injection — main orchestration script.
#
# Runs 4 phases: paraphrase generation → data mixing → LoRA SFT → evaluation.
# Supports resumption (skips existing outputs) and phase selection.
#
# Usage:
#   bash run_exp001.sh --phase all --gpu-ids 0,1 --parallel 2
#   bash run_exp001.sh --phase train --gpu-ids 0,1,2,3 --parallel 4

set -euo pipefail

# ── Defaults ──
PHASE="all"
GPU_IDS="0"
PARALLEL=1
BASE_DIR="/root/autodl-tmp/exp001"
PARAPHRASE_MODEL="Qwen/Qwen2.5-7B-Instruct"
API_URL=""
BASE_SFT_DATA="Open-Orca/SlimOrca"
SEED_LIST="42 123 456"
MODEL_LIST="Qwen/Qwen2.5-0.5B Qwen/Qwen2.5-1.5B Qwen/Qwen2.5-3B"
DOSAGE_LIST="0 5 25 50 100"
BENCHMARK_LIST="mmlu gsm8k arc_challenge humaneval"
CACHE_DIR="/root/autodl-tmp/.hf_cache"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

export HF_HOME="$CACHE_DIR"

# ── Parse args ──
while [[ $# -gt 0 ]]; do
    case $1 in
        --phase)       PHASE="$2";             shift 2 ;;
        --gpu-ids)     GPU_IDS="$2";           shift 2 ;;
        --parallel)    PARALLEL="$2";          shift 2 ;;
        --base-dir)    BASE_DIR="$2";          shift 2 ;;
        --para-model)  PARAPHRASE_MODEL="$2";  shift 2 ;;
        --api-url)     API_URL="$2";           shift 2 ;;
        --base-sft)    BASE_SFT_DATA="$2";     shift 2 ;;
        --seeds)       SEED_LIST="$2";         shift 2 ;;
        --models)      MODEL_LIST="$2";        shift 2 ;;
        --dosages)     DOSAGE_LIST="$2";       shift 2 ;;
        --benchmarks)  BENCHMARK_LIST="$2";    shift 2 ;;
        --cache-dir)   CACHE_DIR="$2";         shift 2 ;;
        -h|--help)
            echo "Usage: $0 [--phase paraphrase|data|train|eval|all] [--gpu-ids 0,1] [--parallel N] ..."
            exit 0 ;;
        *) echo "Unknown arg: $1"; exit 1 ;;
    esac
done

PARA_DIR="$BASE_DIR/paraphrases"
DATA_DIR="$BASE_DIR/sft_data"
CKPT_DIR="$BASE_DIR/checkpoints"
EVAL_DIR="$BASE_DIR/eval_results"

mkdir -p "$PARA_DIR" "$DATA_DIR" "$CKPT_DIR" "$EVAL_DIR"

IFS=',' read -ra GPU_ARRAY <<< "$GPU_IDS"
NUM_GPUS=${#GPU_ARRAY[@]}

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"; }

# ── Phase 1: Paraphrase generation ──
run_paraphrase() {
    log "=== Phase 1: Paraphrase Generation ==="
    API_FLAG=""
    if [[ -n "$API_URL" ]]; then
        API_FLAG="--api-url $API_URL"
    fi

    for bench in $BENCHMARK_LIST; do
        output_file="$PARA_DIR/${bench}_paraphrases.json"
        if [[ -f "$output_file" ]]; then
            log "SKIP: $output_file exists"
            continue
        fi
        log "Generating paraphrases for $bench..."
        python3 "$SCRIPT_DIR/paraphrase_gen.py" \
            --benchmark "$bench" \
            --model "$PARAPHRASE_MODEL" \
            --output-dir "$PARA_DIR" \
            --batch-size 32 \
            --cache-dir "$CACHE_DIR" \
            $API_FLAG
    done
    log "Phase 1 complete."
}

# ── Phase 2: Data preparation ──
run_data() {
    log "=== Phase 2: SFT Data Preparation ==="
    meta_file="$DATA_DIR/data_meta.json"
    if [[ -f "$meta_file" ]]; then
        log "SKIP: $meta_file exists"
    else
        python3 "$SCRIPT_DIR/prepare_sft_data.py" \
            --paraphrase-dir "$PARA_DIR" \
            --base-sft-data "$BASE_SFT_DATA" \
            --dosage $DOSAGE_LIST \
            --output-dir "$DATA_DIR" \
            --seed 42 \
            --cache-dir "$CACHE_DIR"
    fi
    log "Phase 2 complete."
}

# ── Phase 3: Training ──
run_train() {
    log "=== Phase 3: LoRA SFT Training ==="
    log "Models: $MODEL_LIST"
    log "Dosages: $DOSAGE_LIST"
    log "Seeds: $SEED_LIST"
    log "GPUs: $GPU_IDS (parallel=$PARALLEL)"

    # Build job list
    JOBS=()
    for model in $MODEL_LIST; do
        model_short=$(echo "$model" | sed 's|.*/||')
        for dosage in $DOSAGE_LIST; do
            for seed in $SEED_LIST; do
                run_dir="$CKPT_DIR/${model_short}_d${dosage}_s${seed}"
                if [[ -f "$run_dir/train_config.json" ]]; then
                    log "SKIP: $run_dir exists"
                    continue
                fi
                data_file="$DATA_DIR/sft_dosage_$(printf '%03d' "$dosage").jsonl"
                JOBS+=("$model|$data_file|$run_dir|$seed")
            done
        done
    done

    log "Total jobs: ${#JOBS[@]}"

    # Run jobs with GPU parallelism
    job_idx=0
    while [[ $job_idx -lt ${#JOBS[@]} ]]; do
        pids=()
        for ((slot=0; slot<PARALLEL && job_idx<${#JOBS[@]}; slot++, job_idx++)); do
            gpu_id=${GPU_ARRAY[$((slot % NUM_GPUS))]}
            IFS='|' read -r model data_file run_dir seed <<< "${JOBS[$job_idx]}"
            log "Starting: $run_dir (GPU=$gpu_id)"
            python3 "$SCRIPT_DIR/train_sft.py" \
                --model-name "$model" \
                --data-path "$data_file" \
                --output-dir "$run_dir" \
                --seed "$seed" \
                --gpu "$gpu_id" \
                --cache-dir "$CACHE_DIR" \
                > "$run_dir.log" 2>&1 &
            pids+=($!)
        done
        # Wait for batch
        for pid in "${pids[@]}"; do
            wait "$pid" || log "WARNING: job PID $pid failed"
        done
    done
    log "Phase 3 complete."
}

# ── Phase 4: Evaluation (GPU-parallel, original + paraphrased) ──
run_eval() {
    log "=== Phase 4: Evaluation (original + paraphrased) ==="
    log "GPUs: $GPU_IDS (parallel=$PARALLEL)"

    EVAL_JOBS=()
    for model in $MODEL_LIST; do
        model_short=$(echo "$model" | sed 's|.*/||')
        for dosage in $DOSAGE_LIST; do
            for seed in $SEED_LIST; do
                run_dir="$CKPT_DIR/${model_short}_d${dosage}_s${seed}"
                adapter_path="$run_dir/lora_adapter"

                if [[ ! -d "$adapter_path" ]]; then
                    log "SKIP: adapter not found at $adapter_path"
                    continue
                fi

                # Original benchmark eval
                eval_out="$EVAL_DIR/${model_short}_d${dosage}_s${seed}"
                if [[ -f "$eval_out/eval_results.json" ]]; then
                    log "SKIP: $eval_out exists"
                else
                    EVAL_JOBS+=("$model|$adapter_path|$eval_out|original")
                fi

                # Paraphrased benchmark eval (for ConStat signal)
                eval_out_para="$EVAL_DIR/${model_short}_d${dosage}_s${seed}_para"
                if [[ -f "$eval_out_para/eval_results.json" ]]; then
                    log "SKIP: $eval_out_para exists"
                else
                    EVAL_JOBS+=("$model|$adapter_path|$eval_out_para|paraphrased")
                fi
            done
        done
    done

    log "Total eval jobs: ${#EVAL_JOBS[@]} (original + paraphrased)"

    job_idx=0
    while [[ $job_idx -lt ${#EVAL_JOBS[@]} ]]; do
        pids=()
        for ((slot=0; slot<PARALLEL && job_idx<${#EVAL_JOBS[@]}; slot++, job_idx++)); do
            gpu_id=${GPU_ARRAY[$((slot % NUM_GPUS))]}
            IFS='|' read -r base_model adapter_path eval_out eval_type <<< "${EVAL_JOBS[$job_idx]}"
            mkdir -p "$eval_out"

            PARA_FLAG=""
            if [[ "$eval_type" == "paraphrased" ]]; then
                PARA_FLAG="--paraphrase-dir $PARA_DIR"
            fi

            log "Starting eval ($eval_type): $eval_out (GPU=$gpu_id)"
            CUDA_VISIBLE_DEVICES="$gpu_id" python3 "$SCRIPT_DIR/evaluate.py" \
                --model-path "$base_model" \
                --adapter-path "$adapter_path" \
                --benchmarks $BENCHMARK_LIST \
                --output-dir "$eval_out" \
                --cache-dir "$CACHE_DIR" \
                $PARA_FLAG \
                > "$eval_out.log" 2>&1 &
            pids+=($!)
        done
        for pid in "${pids[@]}"; do
            wait "$pid" || log "WARNING: eval job PID $pid failed"
        done
    done
    log "Phase 4 complete."
}

# ── Dispatch ──
case $PHASE in
    paraphrase) run_paraphrase ;;
    data)       run_data ;;
    train)      run_train ;;
    eval)       run_eval ;;
    all)
        run_paraphrase
        run_data
        run_train
        run_eval
        ;;
    *) echo "Unknown phase: $PHASE"; exit 1 ;;
esac

log "=== exp-001 done ==="
