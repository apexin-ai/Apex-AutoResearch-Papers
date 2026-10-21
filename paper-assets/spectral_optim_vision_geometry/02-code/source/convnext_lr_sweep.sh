#!/bin/bash
set -e
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/spectral_optim_vision_geometry

GPU=0
SEED=42
EPOCHS=5
LOG_DIR=/root/autodl-tmp/tmp
mkdir -p $LOG_DIR

echo "============================================================"
echo "ConvNeXt-T Combined LR Sweep: Muon (3 pts) + AdamW (3 pts)"
echo "GPU=$GPU  SEED=$SEED  EPOCHS=$EPOCHS"
echo "Start: $(date)"
echo "============================================================"

# --- Muon lr sweep ---
echo ""
echo ">>> PHASE 1: Muon lr sweep <<<"
for LR in 0.003 0.01 0.02; do
    echo "--- [Muon] lr=$LR starting at $(date) ---"
    python3 scripts/p1_new_arch/convnext_t_muon_train.py \
        --muon-lr $LR --gpu $GPU --seed $SEED --epochs $EPOCHS \
        2>&1 | tee ${LOG_DIR}/convnext_muon_lr${LR}.log
    echo "--- [Muon] lr=$LR done ---"
    echo ""
done

# --- AdamW lr sweep ---
echo ""
echo ">>> PHASE 2: AdamW lr sweep <<<"
for LR in 0.0001 0.0003 0.001; do
    echo "--- [AdamW] lr=$LR starting at $(date) ---"
    python3 scripts/p1_new_arch/convnext_t_adamw_train.py \
        --lr $LR --gpu $GPU --seed $SEED --epochs $EPOCHS \
        2>&1 | tee ${LOG_DIR}/convnext_adamw_lr${LR}.log
    echo "--- [AdamW] lr=$LR done ---"
    echo ""
done

echo "============================================================"
echo "SWEEP_COMPLETE at $(date)"
echo "============================================================"
