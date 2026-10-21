#!/bin/bash
source /root/miniconda3/etc/profile.d/conda.sh
conda activate base
cd /root/spectral_optim_vision_geometry
python deit_weight_swap.py \
  --muon-ckpt checkpoints/deit_small_muon_lr0003_s42_ep20.pt \
  --adamw-ckpt checkpoints/deit_small_adamw_lr0.0001_wd0.05_s42_ep20.pt \
  --gpu 1 \
  --output results/fairlr/deit_weight_swap.csv \
  --seed 42 \
  2>&1 | tee logs/deit_weight_swap_fairlr.log
echo "DEIT_SWAP_DONE" >> logs/deit_weight_swap_fairlr.log
