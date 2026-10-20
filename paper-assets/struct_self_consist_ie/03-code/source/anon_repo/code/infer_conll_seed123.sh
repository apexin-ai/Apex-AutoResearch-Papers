#!/bin/bash
set -e
cd /root/autodl-tmp/struct_self_consist_ie

echo "=== Step 1: Merge LoRA adapter ==="
python3 -c "
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch, os

base_path = '/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B'
adapter_path = 'checkpoints/qwen3-8b-conll2003-lora/checkpoint-400'
merged_path = 'checkpoints/qwen3-8b-conll2003-merged'

if os.path.exists(merged_path + '/config.json'):
    print('Merged model already exists, skip merge')
else:
    print('Loading base model...')
    base = AutoModelForCausalLM.from_pretrained(base_path, dtype=torch.bfloat16, device_map='cpu')
    print('Loading adapter...')
    model = PeftModel.from_pretrained(base, adapter_path)
    print('Merging...')
    model = model.merge_and_unload()
    print('Saving merged model...')
    model.save_pretrained(merged_path)
    tokenizer = AutoTokenizer.from_pretrained(base_path)
    tokenizer.save_pretrained(merged_path)
    print('Merge complete')
"

echo "=== Step 2: Run inference seed=123 ==="
python3 code/run_mvp_pilot.py \
    --model_path checkpoints/qwen3-8b-conll2003-merged \
    --data_dir data/conll2003 \
    --dataset conll2003 \
    --subtask ner \
    --n_samples 8 \
    --temperature 1.0 \
    --max_tokens 1024 \
    --seed 123 \
    --output_dir output/exp_002_conll_n8_seed123 \
    --collect_logprobs

echo "=== Step 3: Verify output ==="
LINES=$(wc -l < output/exp_002_conll_n8_seed123/samples.jsonl)
echo "samples.jsonl lines: $LINES"
if [ "$LINES" -ne 3453 ]; then
    echo "WARNING: Expected 3453 lines, got $LINES"
fi

echo "=== Step 4: Full signal analysis ==="
python3 code/conll_seed123_analysis.py

echo "=== Step 5: Cleanup merged model (save disk) ==="
rm -rf checkpoints/qwen3-8b-conll2003-merged
echo "Cleaned up merged model"

echo "=== ALL DONE ==="
