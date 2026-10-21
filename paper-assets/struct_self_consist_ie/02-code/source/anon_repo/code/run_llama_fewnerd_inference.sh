#!/bin/bash
set -e
cd /root/autodl-tmp/struct_self_consist_ie

eval "$(/root/miniconda3/bin/conda shell.bash hook)"
conda activate base

MODEL=checkpoints/llama3.1-8b-fewnerd-merged
DATA=data/fewnerd
DATASET=fewnerd

echo "=== Step 1: Merge LoRA adapter ==="
python code/merge_llama_fewnerd.py

echo "=== Step 2: Launch 3-seed inference ==="

CUDA_VISIBLE_DEVICES=0 python code/run_mvp_pilot.py \
    --model_path $MODEL \
    --data_dir $DATA \
    --dataset $DATASET \
    --subtask ner \
    --n_samples 8 \
    --temperature 1.0 \
    --seed 42 \
    --output_dir output/llama_fewnerd_s42 \
    --collect_logprobs &
PID0=$!

CUDA_VISIBLE_DEVICES=2 python code/run_mvp_pilot.py \
    --model_path $MODEL \
    --data_dir $DATA \
    --dataset $DATASET \
    --subtask ner \
    --n_samples 8 \
    --temperature 1.0 \
    --seed 123 \
    --output_dir output/llama_fewnerd_s123 \
    --collect_logprobs &
PID2=$!

CUDA_VISIBLE_DEVICES=3 python code/run_mvp_pilot.py \
    --model_path $MODEL \
    --data_dir $DATA \
    --dataset $DATASET \
    --subtask ner \
    --n_samples 8 \
    --temperature 1.0 \
    --seed 456 \
    --output_dir output/llama_fewnerd_s456 \
    --collect_logprobs &
PID3=$!

echo "PIDs: s42=$PID0, s123=$PID2, s456=$PID3"
echo "Waiting for all 3 to finish..."
wait $PID0 $PID2 $PID3
echo "=== All 3-seed inference complete ==="

echo "=== Step 3: Run analysis ==="
python code/analyze_llama_fewnerd_3seed.py

echo "=== Step 4: Cleanup merged model (save disk) ==="
rm -rf checkpoints/llama3.1-8b-fewnerd-merged
echo "Cleaned up merged model"

echo "=== ALL DONE ==="
