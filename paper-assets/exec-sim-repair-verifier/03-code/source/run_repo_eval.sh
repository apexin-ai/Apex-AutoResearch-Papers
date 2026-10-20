#!/bin/bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

MODE=""
CHECKPOINT_DIR=""
DEVICE="cuda:0"

while [[ $# -gt 0 ]]; do
    case $1 in
        --mode) MODE="$2"; shift 2;;
        --checkpoint_dir) CHECKPOINT_DIR="$2"; shift 2;;
        --device) DEVICE="$2"; shift 2;;
        *) echo "Error: Unknown argument: $1" >&2; exit 1;;
    esac
done

if [[ -z "$MODE" || -z "$CHECKPOINT_DIR" ]]; then
    echo "Usage: ./run_repo_eval.sh --mode cls|cwm --checkpoint_dir <path> [--device cuda:0]"
    exit 1
fi

if [[ "$MODE" != "cls" && "$MODE" != "cwm" ]]; then
    echo "Error: --mode must be 'cls' or 'cwm'" >&2
    exit 1
fi

if [[ ! -d "$CHECKPOINT_DIR" ]]; then
    echo "Error: checkpoint_dir not found: $CHECKPOINT_DIR" >&2
    exit 1
fi

OUTPUT="eval_repo_${MODE}.json"
PRED_FILE="eval_repo_${MODE}_predictions.jsonl"

echo "========================================"
echo "Repo-Level Eval Pipeline"
echo "  Mode: $MODE"
echo "  Checkpoint: $CHECKPOINT_DIR"
echo "  Device: $DEVICE"
echo "  Output: $OUTPUT"
echo "========================================"

# Step 1: Run eval
echo ""
echo "[Step 1] Running $MODE evaluation..."

if [[ -f eval_repo_level.py ]]; then
    # Home server — unified script
    MAX_NEW_TOKENS=8
    [[ "$MODE" == "cwm" ]] && MAX_NEW_TOKENS=64
    python eval_repo_level.py \
        --mode "$MODE" \
        --checkpoint_dir "$CHECKPOINT_DIR" \
        --output "$OUTPUT" \
        --save_predictions \
        --device "$DEVICE" \
        --max_new_tokens "$MAX_NEW_TOKENS"

elif [[ "$MODE" == "cls" && -f eval_repo_verifier.py ]]; then
    # Seetacloud — CLS via eval_repo_verifier.py
    python eval_repo_verifier.py \
        --checkpoint_dir "$CHECKPOINT_DIR" \
        --output "$OUTPUT" \
        --save_predictions \
        --device "$DEVICE"

elif [[ "$MODE" == "cwm" && -f eval_repo_cwm.py ]]; then
    # Seetacloud — CWM via eval_repo_cwm.py
    python eval_repo_cwm.py \
        --checkpoint_dir "$CHECKPOINT_DIR" \
        --output "$OUTPUT" \
        --save_predictions \
        --device "$DEVICE"

else
    echo "Error: No eval script found for mode=$MODE" >&2
    exit 1
fi

echo ""
echo "[Step 1] Done. Results: $OUTPUT, Predictions: $PRED_FILE"

# Step 2: Paired bootstrap (if both predictions exist)
CLS_PRED="eval_repo_cls_predictions.jsonl"
CWM_PRED="eval_repo_cwm_predictions.jsonl"
BOOTSTRAP_OUTPUT="paired_bootstrap_repo_results.json"

echo ""
if [[ -f "$CLS_PRED" && -f "$CWM_PRED" ]]; then
    if [[ -f paired_bootstrap_repo.py ]]; then
        echo "[Step 2] Both CLS and CWM predictions found. Running paired bootstrap..."
        python paired_bootstrap_repo.py \
            --cls_preds "$CLS_PRED" \
            --cwm_preds "$CWM_PRED" \
            --output "$BOOTSTRAP_OUTPUT"
        echo ""
        echo "[Step 2] Done. Bootstrap results: $BOOTSTRAP_OUTPUT"
    else
        echo "[Step 2] SKIP: paired_bootstrap_repo.py not found"
    fi
else
    OTHER_MODE="cwm"
    [[ "$MODE" == "cwm" ]] && OTHER_MODE="cls"
    echo "[Step 2] SKIP: Missing ${OTHER_MODE} predictions. Run with --mode ${OTHER_MODE} first."
fi

echo ""
echo "========================================"
echo "Pipeline complete."
echo "========================================"
