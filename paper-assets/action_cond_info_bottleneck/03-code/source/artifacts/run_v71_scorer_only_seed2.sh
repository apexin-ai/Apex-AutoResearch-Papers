#!/bin/bash
# v7.1 scorer-only training - Seed 2
# Freeze action expert, only train scorer (123K params)
# Base model: original lerobot/smolvla_libero (not v7 trained)

python3 -u scripts/train_acib.py \
  --model_id lerobot/smolvla_libero \
  --dataset_id lerobot/libero \
  --data_root /root/autodl-tmp/libero_dataset \
  --hidden_dim 64 \
  --alpha 0.01 --beta 0.01 --beta_warmup_steps 1000 \
  --mode soft --condition_source language --conditioning_mode concat \
  --lambda_contrastive 0.1 --diversity_lambda 0.1 --lambda_ent 0.0 \
  --steps 20000 --batch_size 64 --lr 1e-4 --warmup_steps 1000 --grad_clip 1.0 \
  --save_freq 5000 --dtype bfloat16 \
  --gpu 0 --seed 123 \
  --train_scorer_only \
  --freeze_action_expert \
  --output_dir /root/autodl-tmp/acib_v7.1_scorer_only_seed2
