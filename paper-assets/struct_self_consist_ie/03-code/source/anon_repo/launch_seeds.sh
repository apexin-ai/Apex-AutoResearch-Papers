#!/bin/bash
cd /root/autodl-tmp/struct_self_consist_ie
PYTHON=/root/miniconda3/bin/python
LOGDIR=output/review_round9_experiments/freeform_conll

for SEED_GPU in "123 1" "456 2" "789 3"; do
    SEED=$(echo $SEED_GPU | cut -d' ' -f1)
    GPU=$(echo $SEED_GPU | cut -d' ' -f2)
    nohup $PYTHON run_freeform_conll.py --seed $SEED --gpu $GPU > ${LOGDIR}/seed_${SEED}.log 2>&1 &
    echo "Launched seed=$SEED gpu=$GPU pid=$!"
done
