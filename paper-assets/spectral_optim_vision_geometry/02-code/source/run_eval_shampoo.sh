#!/bin/bash
cd /root/spectral_optim_vision_geometry
source /root/miniconda3/bin/activate
CUDA_VISIBLE_DEVICES=0 python eval_cifar100c.py \
  --model convnext_tiny \
  --checkpoint /root/autodl-tmp/checkpoints/spectral_optim/convnext_tiny_shampoo_s42_lr7e-3_best.pt \
  --data-dir /root/autodl-tmp/data/CIFAR-100-C \
  --output-csv results/convnext_tiny_shampoo_baseline_s42.csv \
  --optimizer shampoo \
  --device cuda:0 \
  > /tmp/eval_shampoo2.log 2>&1
echo "EXIT_CODE=$?" >> /tmp/eval_shampoo2.log
