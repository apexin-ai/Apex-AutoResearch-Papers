#!/bin/bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base
cd /root/gen-depth-fingerprint
export HF_HOME=/root/autodl-tmp/.hf_cache

# Wait for current size_matched_seed42 (PID 142680) to finish
echo "Waiting for PID 142680 to finish..."
while kill -0 142680 2>/dev/null; do sleep 30; done
echo "PID 142680 done, starting remaining runs"

MODEL=/root/autodl-tmp/models/olmo-2-1b-hf/allenai/OLMo-2-0425-1B
EVAL=data/downstream/test.jsonl
OUTBASE=experiments/downstream

echo "=== depth01 seed=456 ==="
python finetune_downstream.py --model-path $MODEL --train-data data/downstream/train_depth01.jsonl --eval-data $EVAL --output-dir $OUTBASE/depth01_seed456 --seed 456 --bf16 --batch-size 4 --grad-accum 4 --epochs 3

for SEED in 42 123 456; do
  echo "=== all seed=$SEED ==="
  python finetune_downstream.py --model-path $MODEL --train-data data/downstream/train_all.jsonl --eval-data $EVAL --output-dir $OUTBASE/all_seed${SEED} --seed $SEED --bf16 --batch-size 4 --grad-accum 4 --epochs 3
done

echo "GPU2 ALL DONE"
