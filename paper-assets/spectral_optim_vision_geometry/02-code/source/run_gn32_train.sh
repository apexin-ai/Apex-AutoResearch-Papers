#!/bin/bash
set -e
cd /root/spectral_optim_vision_geometry
source /root/miniconda3/bin/activate
export CUDA_VISIBLE_DEVICES=1

echo "=== [1/5] Training muon GN(32) ==="
python -u muon_train.py --model resnet50 --norm-type gn32 --gpu 0 --seed 42 --epochs 20 2>&1 | tee /root/runs/spectral_optim_vision_geometry/muon_r50_gn32_retrain.log

echo "=== [2/5] Training adamw GN(32) ==="
python -u baseline_train.py --model resnet50 --optimizer adamw --norm-type gn32 --gpu 0 --seed 42 --epochs 20 2>&1 | tee /root/runs/spectral_optim_vision_geometry/adamw_r50_gn32_retrain.log

echo "=== [3/5] Training sgd GN(32) ==="
python -u baseline_train.py --model resnet50 --optimizer sgd --norm-type gn32 --gpu 0 --seed 42 --epochs 20 2>&1 | tee /root/runs/spectral_optim_vision_geometry/sgd_r50_gn32_retrain.log

echo "=== [4/5] Training soap GN(32) ==="
python -u baseline_train.py --model resnet50 --optimizer soap --norm-type gn32 --gpu 0 --seed 42 --epochs 20 --lr 1e-3 2>&1 | tee /root/runs/spectral_optim_vision_geometry/soap_r50_gn32_retrain.log

echo "=== [5/5] Training shampoo GN(32) ==="
python -u baseline_train.py --model resnet50 --optimizer shampoo --norm-type gn32 --gpu 0 --seed 42 --epochs 20 --lr 7e-3 2>&1 | tee /root/runs/spectral_optim_vision_geometry/shampoo_r50_gn32_retrain.log

echo "=== ALL GN(32) TRAINING COMPLETE ==="
ls -la /root/autodl-tmp/checkpoints/spectral_optim/*gn32* 2>/dev/null
