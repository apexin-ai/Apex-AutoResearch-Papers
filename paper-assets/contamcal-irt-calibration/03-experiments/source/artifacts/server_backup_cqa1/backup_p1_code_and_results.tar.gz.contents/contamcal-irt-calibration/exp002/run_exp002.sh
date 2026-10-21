#!/bin/bash
# exp-002 Stage 1 Signal Pipeline — orchestration script.
#
# Computes 4 contamination detection signals for all exp-001 checkpoints,
# then aggregates via RRF into per-model-item exposure scores.
#
# Usage:
#   bash run_exp002.sh --phase all --gpu-ids 0,1
#   bash run_exp002.sh --phase signals --gpu-ids 0 --benchmarks "mmlu gsm8k"
#   bash run_exp002.sh --phase aggregate

set -euo pipefail

# ── Defaults ──
PHASE="all"
GPU_IDS="0"
EXP001_DIR="/root/autodl-tmp/exp001"
OUTPUT_DIR="/root/autodl-tmp/exp002"
MODEL_LIST="Qwen2.5-0.5B Qwen2.5-1.5B Qwen2.5-3B"
DOSAGE_LIST="0 5 25 50 100"
SEED_LIST="42 123 456"
BENCHMARK_LIST="mmlu gsm8k arc_challenge humaneval"
CACHE_DIR="/root/autodl-tmp/.hf_cache"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
K_PERCENT=20
BATCH_SIZE=64

export HF_HOME="$CACHE_DIR"

# ── Parse args ──
while [[ $# -gt 0 ]]; do
    case $1 in
        --phase)        PHASE="$2";         shift 2 ;;
        --gpu-ids)      GPU_IDS="$2";       shift 2 ;;
        --exp001-dir)   EXP001_DIR="$2";    shift 2 ;;
        --output-dir)   OUTPUT_DIR="$2";    shift 2 ;;
        --models)       MODEL_LIST="$2";    shift 2 ;;
        --dosages)      DOSAGE_LIST="$2";   shift 2 ;;
        --seeds)        SEED_LIST="$2";     shift 2 ;;
        --benchmarks)   BENCHMARK_LIST="$2"; shift 2 ;;
        --cache-dir)    CACHE_DIR="$2";     shift 2 ;;
        --k-percent)    K_PERCENT="$2";     shift 2 ;;
        --batch-size)   BATCH_SIZE="$2";    shift 2 ;;
        -h|--help)
            echo "Usage: $0 [--phase signals|aggregate|all] [--gpu-ids 0,1] ..."
            exit 0 ;;
        *) echo "Unknown arg: $1"; exit 1 ;;
    esac
done

CKPT_DIR="$EXP001_DIR/checkpoints"
EVAL_DIR="$EXP001_DIR/eval_results"
DATA_DIR="$EXP001_DIR/sft_data"
PARA_DIR="$EXP001_DIR/paraphrases"
SIGNAL_DIR="$OUTPUT_DIR/signals"
RRF_DIR="$OUTPUT_DIR/rrf"

mkdir -p "$SIGNAL_DIR" "$RRF_DIR"

IFS=',' read -ra GPU_ARRAY <<< "$GPU_IDS"
NUM_GPUS=${#GPU_ARRAY[@]}

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*"; }

# ── Phase 1: Compute signals for each model-benchmark pair ──
run_signals() {
    log "=== Phase 1: Signal Computation ==="

    for model_short in $MODEL_LIST; do
        for dosage in $DOSAGE_LIST; do
            for seed in $SEED_LIST; do
                run_id="${model_short}_d${dosage}_s${seed}"
                model_path="$CKPT_DIR/${run_id}/lora_adapter"
                signal_out="$SIGNAL_DIR/${run_id}"

                if [[ ! -d "$model_path" ]]; then
                    log "SKIP: model not found at $model_path"
                    continue
                fi

                # Reference model = 0% dosage, same model, same seed
                ref_run_id="${model_short}_d0_s${seed}"
                ref_model_path="$CKPT_DIR/${ref_run_id}/lora_adapter"
                if [[ ! -d "$ref_model_path" ]]; then
                    log "WARN: reference model not found at $ref_model_path, using model itself"
                    ref_model_path="$model_path"
                fi

                # SFT data for this dosage
                sft_data_file="$DATA_DIR/sft_dosage_$(printf '%03d' "$dosage").jsonl"

                gpu_id=${GPU_ARRAY[$((RANDOM % NUM_GPUS))]}

                for bench in $BENCHMARK_LIST; do
                    merged_file="$signal_out/signals_merged_${bench}.json"
                    if [[ -f "$merged_file" ]]; then
                        log "SKIP: $merged_file exists"
                        continue
                    fi

                    # Collect original + paraphrase eval paths across seeds
                    orig_paths=()
                    para_paths=()
                    for s in $SEED_LIST; do
                        orig_eval="$EVAL_DIR/${model_short}_d${dosage}_s${s}/eval_results.json"
                        para_eval="$EVAL_DIR/${model_short}_d${dosage}_s${s}_para/eval_results.json"
                        if [[ -f "$orig_eval" ]]; then
                            orig_paths+=("$orig_eval")
                        fi
                        if [[ -f "$para_eval" ]]; then
                            para_paths+=("$para_eval")
                        fi
                    done

                    constat_args=""
                    if [[ ${#orig_paths[@]} -gt 0 && ${#para_paths[@]} -gt 0 ]]; then
                        constat_args="--original-eval-paths ${orig_paths[*]} --paraphrase-eval-paths ${para_paths[*]}"
                    fi

                    log "Computing signals: $run_id / $bench (GPU=$gpu_id)"
                    python3 "$SCRIPT_DIR/compute_signals.py" \
                        --model-path "$model_path" \
                        --benchmark "$bench" \
                        --ref-model-path "$ref_model_path" \
                        --sft-data-path "$sft_data_file" \
                        $constat_args \
                        --output-dir "$signal_out" \
                        --gpu "$gpu_id" \
                        --batch-size "$BATCH_SIZE" \
                        --k-percent "$K_PERCENT" \
                        --cache-dir "$CACHE_DIR"
                done
            done
        done
    done
    log "Phase 1 complete."
}

# ── Phase 2: RRF aggregation ──
run_aggregate() {
    log "=== Phase 2: RRF Aggregation ==="

    for model_short in $MODEL_LIST; do
        for dosage in $DOSAGE_LIST; do
            for seed in $SEED_LIST; do
                run_id="${model_short}_d${dosage}_s${seed}"
                signal_out="$SIGNAL_DIR/${run_id}"
                rrf_out="$RRF_DIR/${run_id}"

                if [[ ! -d "$signal_out" ]]; then
                    log "SKIP: signals not found at $signal_out"
                    continue
                fi

                if [[ -f "$rrf_out/rrf_scores_${run_id}.json" ]]; then
                    log "SKIP: $rrf_out already aggregated"
                    continue
                fi

                mkdir -p "$rrf_out"

                for bench in $BENCHMARK_LIST; do
                    merged_file="$signal_out/signals_merged_${bench}.json"
                    if [[ ! -f "$merged_file" ]]; then
                        log "SKIP: merged signals not found: $merged_file"
                        continue
                    fi

                    log "Aggregating: $run_id / $bench"
                    python3 "$SCRIPT_DIR/aggregate_rrf.py" \
                        --signal-files "$merged_file" \
                        --output-dir "$rrf_out" \
                        --model-name "${run_id}_${bench}" \
                        --benchmark "$bench"
                done
            done
        done
    done
    log "Phase 2 complete."
}

# ── Dispatch ──
case $PHASE in
    signals)   run_signals ;;
    aggregate) run_aggregate ;;
    all)
        run_signals
        run_aggregate
        ;;
    *) echo "Unknown phase: $PHASE"; exit 1 ;;
esac

log "=== exp-002 done ==="
