#!/bin/bash
# DeiT 50ep relay script — run after ResNet 50ep finishes
# Usage: bash launch_deit_50ep.sh

set -e
cd /root/spectral_optim_vision_geometry
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base

LOGDIR=~/runs/spectral_optim_vision_geometry
mkdir -p "$LOGDIR"

echo "=== Launching DeiT 50ep experiments ==="
echo "Time: $(date)"

# cuda:0 — DeiT Muon 50ep (lr=0.003, cosine T_max=50, seed=42)
CUDA_VISIBLE_DEVICES=0 nohup python deit_muon_full_train.py \
    --epochs 50 --muon-lr 0.003 --seed 42 --gpu 0 \
    > "$LOGDIR/research_deit_muon_50ep.log" 2>&1 &
PID_MUON=$!
echo "DeiT Muon 50ep started on cuda:0, PID=$PID_MUON"

# cuda:1 — DeiT AdamW 50ep (lr=1e-4, warmup=2ep + cosine, seed=42)
CUDA_VISIBLE_DEVICES=1 nohup python deit_adamw_mild_aug_train.py \
    --epochs 50 --lr 1e-4 --seed 42 --gpu 0 \
    > "$LOGDIR/research_deit_adamw_50ep.log" 2>&1 &
PID_ADAMW=$!
echo "DeiT AdamW 50ep started on cuda:1, PID=$PID_ADAMW"

echo ""
echo "Log files:"
echo "  Muon:  $LOGDIR/research_deit_muon_50ep.log"
echo "  AdamW: $LOGDIR/research_deit_adamw_50ep.log"
echo ""
echo "Monitor: tail -f $LOGDIR/research_deit_muon_50ep.log"
