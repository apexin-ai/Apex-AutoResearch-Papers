#!/bin/bash
# D063 Val Set Checkpoint Sweep
cd /home/sonny/exec-sim-repair-verifier
source .venv/bin/activate 2>/dev/null

export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True

RESULTS_DIR="val_eval_results"
mkdir -p "$RESULTS_DIR"

CHECKPOINTS=(
    "checkpoints_repo_cls_seed123_home/checkpoint-200"
    "checkpoints_repo_cls_seed123_home/checkpoint-400"
    "checkpoints_repo_cls_seed123_home/checkpoint-600"
    "checkpoints_repo_cls_seed123_home/checkpoint-800"
    "checkpoints_repo_cls_seed123_home/checkpoint-1000"
    "checkpoints_repo_cls_v5/checkpoint-600"
    "checkpoints_repo_cls_v5/checkpoint-4000"
    "checkpoints_repo_cls_v5/checkpoint-4200"
    "checkpoints_repo_cls_v5/checkpoint-4400"
    "checkpoints_repo_cls_v5/checkpoint-4600"
    "checkpoints_repo_cls_home/checkpoint-200"
    "checkpoints_repo_cls_home/checkpoint-2400"
    "checkpoints_repo_cls_home/checkpoint-2600"
)

for ckpt in "${CHECKPOINTS[@]}"; do
    tag=$(echo "$ckpt" | tr '/' '_')
    out_json="$RESULTS_DIR/${tag}.json"
    out_pred="$RESULTS_DIR/${tag}_predictions.jsonl"

    if [ -f "$out_json" ]; then
        echo "SKIP $ckpt (already done)"
        continue
    fi

    echo "=========================================="
    echo "EVAL: $ckpt"
    echo "START: $(date)"
    echo "=========================================="

    python3 eval_repo_cls.py \
        --checkpoint_dir "$ckpt" \
        --split val \
        --output "$out_json" \
        --pred_output "$out_pred" \
        --batch_size 8 \
        --device cuda:0

    rc=$?
    if [ $rc -ne 0 ]; then
        echo "ERROR: $ckpt exited with code $rc"
        rm -f "$out_json" "$out_pred"
    fi

    echo "DONE: $ckpt at $(date) (exit=$rc)"
    echo ""
    sleep 3
done

echo "ALL DONE at $(date)"
echo ""
echo "=== SUMMARY ==="
for f in "$RESULTS_DIR"/*.json; do
    [ -f "$f" ] || continue
    echo "--- $(basename $f) ---"
    python3 -c "import json; d=json.load(open('$f')); m=d['metrics']; print(f\"acc={m['accuracy']:.4f} f1_macro={m['f1_macro']:.4f} fail_f1={m['f1_fail']:.4f} pass_f1={m['f1_pass']:.4f}\")"
done
