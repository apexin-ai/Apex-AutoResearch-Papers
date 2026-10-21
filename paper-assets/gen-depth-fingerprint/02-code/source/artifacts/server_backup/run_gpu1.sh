#!/bin/bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/gen-depth-fingerprint
export HF_HOME=/root/autodl-tmp/.hf_cache

MODEL=/root/autodl-tmp/models/olmo-2-1b-hf/allenai/OLMo-2-0425-1B
EVAL=data/downstream/test.jsonl
OUTBASE=experiments/downstream

for SEED in 42 123 456; do
  echo "=== depth0_only seed=$SEED ==="
  python finetune_downstream.py --model-path $MODEL --train-data data/downstream/train_depth0_only.jsonl --eval-data $EVAL --output-dir $OUTBASE/depth0_only_seed${SEED} --seed $SEED --bf16 --batch-size 4 --grad-accum 4 --epochs 3
done

for SEED in 42 123; do
  echo "=== depth01 seed=$SEED ==="
  python finetune_downstream.py --model-path $MODEL --train-data data/downstream/train_depth01.jsonl --eval-data $EVAL --output-dir $OUTBASE/depth01_seed${SEED} --seed $SEED --bf16 --batch-size 4 --grad-accum 4 --epochs 3
done

echo "GPU1 ALL DONE"
