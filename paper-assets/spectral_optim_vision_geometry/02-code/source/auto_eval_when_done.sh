#!/bin/bash
# Wait for training to complete, then auto-start eval
while true; do
    if grep -q "ALL GN(32) TRAINING COMPLETE" /root/runs/spectral_optim_vision_geometry/gn32_train_all.log 2>/dev/null; then
        echo "Training complete, starting eval..."
        cd /root/spectral_optim_vision_geometry
        source /root/miniconda3/bin/activate
        export CUDA_VISIBLE_DEVICES=1
        bash run_gn32_eval.sh > /root/runs/spectral_optim_vision_geometry/gn32_eval_all.log 2>&1
        echo "EVAL DONE" >> /root/runs/spectral_optim_vision_geometry/gn32_eval_all.log
        exit 0
    fi
    sleep 60
done
