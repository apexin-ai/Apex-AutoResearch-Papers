#!/bin/bash
set -e

cd /root/spectral_optim_vision_geometry
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

DATA_DIR="/root/autodl-tmp/imagenet100_deduped"
LOG_DIR="$HOME/runs/spectral_optim_vision_geometry/lr_sweep_imagenet100"
CKPT_DIR="/root/autodl-tmp/checkpoints/spectral_optim/lr_sweep_imagenet100"
EPOCHS=5
SEED=42
BATCH_SIZE=128
NUM_WORKERS=4

mkdir -p "$LOG_DIR" "$CKPT_DIR"

run_one() {
    local gpu=$1 arch=$2 opt=$3 lr=$4
    local tag="${arch}_${opt}_lr${lr}"
    local log="${LOG_DIR}/${tag}.log"

    echo "[$(date '+%H:%M:%S')] START ${tag} on GPU ${gpu}"

    if [ "$opt" = "muon" ]; then
        lr_flag="--muon-lr $lr"
    else
        lr_flag="--lr $lr"
    fi

    CUDA_VISIBLE_DEVICES=$gpu python3 imagenet100_train.py \
        --arch $arch --optimizer $opt $lr_flag \
        --epochs $EPOCHS --seed $SEED --batch-size $BATCH_SIZE \
        --num-workers $NUM_WORKERS \
        --data-dir "$DATA_DIR" --gpu 0 \
        --output-dir "$CKPT_DIR" \
        > "$log" 2>&1

    local best=$(grep -oP 'TRAINING_COMPLETE val_acc=\K[\d.]+' "$log" 2>/dev/null || echo "N/A")
    echo "[$(date '+%H:%M:%S')] DONE ${tag} -> best_val_acc=${best}%"
}

gpu0_sweep() {
    run_one 0 resnet50 muon 0.005
    run_one 0 resnet50 muon 0.02
    run_one 0 resnet50 muon 0.05
    run_one 0 resnet50 adamw 3e-4
    run_one 0 resnet50 adamw 1e-3
    run_one 0 resnet50 adamw 3e-3
    run_one 0 resnet50 sgd 0.03
    run_one 0 resnet50 sgd 0.1
    run_one 0 resnet50 sgd 0.3
    echo "[GPU0] ALL 9 RUNS COMPLETE"
}

gpu1_sweep() {
    run_one 1 deit_small muon 0.005
    run_one 1 deit_small muon 0.02
    run_one 1 deit_small muon 0.05
    run_one 1 deit_small adamw 3e-5
    run_one 1 deit_small adamw 1e-4
    run_one 1 deit_small adamw 3e-4
    run_one 1 deit_small sgd 0.01
    run_one 1 deit_small sgd 0.05
    run_one 1 deit_small sgd 0.1
    echo "[GPU1] ALL 9 RUNS COMPLETE"
}

gpu0_sweep &
GPU0_PID=$!
gpu1_sweep &
GPU1_PID=$!

echo "GPU0 PID=$GPU0_PID, GPU1 PID=$GPU1_PID"
echo "Started at $(date)"

wait $GPU0_PID
GPU0_EXIT=$?
wait $GPU1_PID
GPU1_EXIT=$?

echo ""
echo "=== LR SWEEP COMPLETE ==="
echo "GPU0 exit: $GPU0_EXIT, GPU1 exit: $GPU1_EXIT"
echo "Finished at $(date)"

echo ""
echo "=== RESULTS SUMMARY ==="
printf "%-35s %s\n" "CONFIG" "BEST_VAL_ACC"
printf "%-35s %s\n" "-----------------------------------" "-----------"
for log in $LOG_DIR/*.log; do
    tag=$(basename "$log" .log)
    best=$(grep -oP 'TRAINING_COMPLETE val_acc=\K[\d.]+' "$log" 2>/dev/null || echo "FAILED")
    printf "%-35s %s%%\n" "$tag" "$best"
done
echo ""
echo "EXIT_CODE=0"
