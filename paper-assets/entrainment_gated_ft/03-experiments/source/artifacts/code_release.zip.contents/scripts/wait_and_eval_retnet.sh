#!/bin/bash
set -e
source ${CONDA_SH:-$HOME/miniconda3/etc/profile.d/conda.sh} && conda activate base

MODEL_DIR="${MODEL_DIR:-./models_1.3b}/1.3B-100B-RetNet-pure"
SHARD1="$MODEL_DIR/model-00001-of-00002.safetensors"
ARIA2="$SHARD1.aria2"
LOG="${PROJECT_ROOT:-.}/lm_eval_clean/retnet_reeval.log"

echo "Waiting for RetNet-pure shard 1 download to complete..." | tee "$LOG"

# Wait for the file to exist and aria2 control file to be gone
while true; do
    if [ -f "$SHARD1" ] && [ ! -f "$ARIA2" ]; then
        SIZE=$(stat -c%s "$SHARD1" 2>/dev/null || echo 0)
        if [ "$SIZE" -gt 1000000000 ]; then
            echo "$(date): Shard 1 found, size=$SIZE bytes. Starting eval." | tee -a "$LOG"
            break
        fi
    fi
    # Also check if HF download completed (file appears without aria2)
    if [ -f "$SHARD1" ] && [ ! -f "$ARIA2" ]; then
        SIZE=$(stat -c%s "$SHARD1" 2>/dev/null || echo 0)
        if [ "$SIZE" -gt 1000000000 ]; then
            echo "$(date): File ready. Starting eval." | tee -a "$LOG"
            break
        fi
    fi
    # Check modelscope cache too
    MS_FILE=$(find ${MODEL_DIR:-./models_1.3b}/retnet_ms_cache -name "model-00001-of-00002.safetensors" -size +1G 2>/dev/null | head -1)
    if [ -n "$MS_FILE" ]; then
        echo "$(date): Found completed ModelScope download at $MS_FILE, copying..." | tee -a "$LOG"
        cp "$MS_FILE" "$SHARD1"
        rm -f "$ARIA2"
        echo "$(date): Copied. Starting eval." | tee -a "$LOG"
        break
    fi
    echo "$(date): Still waiting... shard1 exists=$([ -f "$SHARD1" ] && echo yes || echo no), aria2=$([ -f "$ARIA2" ] && echo yes || echo no)" >> "$LOG"
    sleep 60
done

echo "$(date): Verifying model can load..." | tee -a "$LOG"
python3 -c "
from safetensors.torch import load_file
import os
path = '$MODEL_DIR'
for fn in ['model-00001-of-00002.safetensors', 'model-00002-of-00002.safetensors']:
    fp = os.path.join(path, fn)
    sd = load_file(fp)
    print(f'{fn}: {len(sd)} keys')
print('Model shards OK')
" 2>&1 | tee -a "$LOG"

echo "$(date): Running lm-eval for RetNet-pure..." | tee -a "$LOG"
export CUDA_VISIBLE_DEVICES=0
python3 ${PROJECT_ROOT:-.}/scripts/run_lmeval_clean.py \
  --model_path "$MODEL_DIR" \
  --tasks lambada_openai,hellaswag,winogrande,arc_easy,arc_challenge,mmlu \
  --output_dir ${PROJECT_ROOT:-.}/lm_eval_clean \
  --batch_size 8 \
  2>&1 | tee -a "$LOG"

echo "$(date): RetNet-pure eval COMPLETE" | tee -a "$LOG"
