#!/bin/bash
# B6 Phase 1: Supplementary LR sweep + DeiT confirmed 20ep
set -e

cd /root/spectral_optim_vision_geometry
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

DATA_DIR="/root/autodl-tmp/imagenet100_deduped"
SWEEP_LOG_DIR="$HOME/runs/spectral_optim_vision_geometry/lr_sweep_imagenet100_supp"
TRAIN_LOG_DIR="$HOME/runs/spectral_optim_vision_geometry/b6_imagenet100_20ep"
CKPT_DIR="/root/autodl-tmp/checkpoints/spectral_optim/b6_imagenet100"
SEED=42
BATCH_SIZE=128
NUM_WORKERS=4

mkdir -p "$SWEEP_LOG_DIR" "$TRAIN_LOG_DIR" "$CKPT_DIR"

run_one() {
    local gpu=$1 arch=$2 opt=$3 lr=$4 epochs=$5 log_dir=$6
    local tag="${arch}_${opt}_lr${lr}"
    [ "$epochs" -gt 5 ] && tag="${arch}_${opt}_${epochs}ep"
    local log="${log_dir}/${tag}.log"

    echo "[$(date '+%H:%M:%S')] START ${tag} on GPU ${gpu} (${epochs}ep)"

    if [ "$opt" = "muon" ]; then
        lr_flag="--muon-lr $lr"
    else
        lr_flag="--lr $lr"
    fi

    CUDA_VISIBLE_DEVICES=$gpu python3 imagenet100_train.py \
        --arch $arch --optimizer $opt $lr_flag \
        --epochs $epochs --seed $SEED --batch-size $BATCH_SIZE \
        --num-workers $NUM_WORKERS \
        --data-dir "$DATA_DIR" --gpu 0 \
        --output-dir "$CKPT_DIR" \
        > "$log" 2>&1

    local best=$(grep -oP 'TRAINING_COMPLETE val_acc=\K[\d.]+' "$log" 2>/dev/null || echo "N/A")
    echo "[$(date '+%H:%M:%S')] DONE ${tag} -> best_val_acc=${best}%"
}

# GPU 0: ResNet-50 supplementary sweep (4 runs, 5ep each)
gpu0_work() {
    run_one 0 resnet50 muon 0.08 5 "$SWEEP_LOG_DIR"
    run_one 0 resnet50 muon 0.1 5 "$SWEEP_LOG_DIR"
    run_one 0 resnet50 adamw 5e-3 5 "$SWEEP_LOG_DIR"
    run_one 0 resnet50 adamw 0.01 5 "$SWEEP_LOG_DIR"
    echo "[GPU0] ALL SUPPLEMENTARY SWEEP COMPLETE"
}

# GPU 1: DeiT-S supplementary sweep (2 runs) + 20ep confirmed (2 runs)
gpu1_work() {
    run_one 1 deit_small muon 0.002 5 "$SWEEP_LOG_DIR"
    run_one 1 deit_small muon 0.003 5 "$SWEEP_LOG_DIR"
    echo "[GPU1] SUPPLEMENTARY SWEEP COMPLETE, STARTING 20EP"
    run_one 1 deit_small sgd 0.01 20 "$TRAIN_LOG_DIR"
    run_one 1 deit_small adamw 1e-4 20 "$TRAIN_LOG_DIR"
    echo "[GPU1] ALL 20EP COMPLETE"
}

# Launch both in parallel
gpu0_work &
GPU0_PID=$!
gpu1_work &
GPU1_PID=$!

echo "GPU0 PID=$GPU0_PID, GPU1 PID=$GPU1_PID"
echo "Started at $(date)"

wait $GPU0_PID
GPU0_EXIT=$?
wait $GPU1_PID
GPU1_EXIT=$?

echo ""
echo "=== PHASE 1 COMPLETE ==="
echo "GPU0 exit: $GPU0_EXIT, GPU1 exit: $GPU1_EXIT"
echo "Finished at $(date)"

echo ""
echo "=== SUPPLEMENTARY SWEEP RESULTS ==="
printf "%-35s %s\n" "CONFIG" "BEST_VAL_ACC"
printf "%-35s %s\n" "-----------------------------------" "-----------"
for log in $SWEEP_LOG_DIR/*.log; do
    tag=$(basename "$log" .log)
    best=$(grep -oP 'TRAINING_COMPLETE val_acc=\K[\d.]+' "$log" 2>/dev/null || echo "FAILED")
    printf "%-35s %s%%\n" "$tag" "$best"
done

echo ""
echo "=== 20EP RESULTS ==="
printf "%-35s %s\n" "CONFIG" "BEST_VAL_ACC"
printf "%-35s %s\n" "-----------------------------------" "-----------"
for log in $TRAIN_LOG_DIR/*.log; do
    tag=$(basename "$log" .log)
    best=$(grep -oP 'TRAINING_COMPLETE val_acc=\K[\d.]+' "$log" 2>/dev/null || echo "FAILED")
    printf "%-35s %s%%\n" "$tag" "$best"
done

echo ""
echo "EXIT_CODE=0"
