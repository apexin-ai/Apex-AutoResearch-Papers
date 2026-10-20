#!/bin/bash
set -e
cd /root/autodl-tmp/struct_self_consist_ie
source /root/miniconda3/bin/activate
export CUDA_VISIBLE_DEVICES=3

echo "=== Step 1: Merge LoRA adapter ==="
python3 -c "
import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

base = '/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B'
adapter = 'checkpoints/qwen3-8b-conll2003-lora/checkpoint-400'
out = 'checkpoints/qwen3-8b-conll2003-merged'

print('Loading base model...')
model = AutoModelForCausalLM.from_pretrained(base, torch_dtype=torch.bfloat16)
print('Loading adapter...')
model = PeftModel.from_pretrained(model, adapter)
print('Merging...')
model = model.merge_and_unload()
print('Saving merged model...')
model.save_pretrained(out)
tokenizer = AutoTokenizer.from_pretrained(base, trust_remote_code=True)
tokenizer.save_pretrained(out)
print('Merge complete')
"

echo "=== Step 2: Run inference seed=456 ==="
python code/run_mvp_pilot.py \
  --model_path checkpoints/qwen3-8b-conll2003-merged \
  --data_dir data/conll2003 \
  --dataset conll2003 \
  --subtask ner \
  --n_samples 8 \
  --temperature 1.0 \
  --seed 456 \
  --collect_logprobs \
  --output_dir output/exp_002_conll_n8_seed456

echo "=== Step 3: Verify output ==="
LINES=$(wc -l < output/exp_002_conll_n8_seed456/samples.jsonl)
echo "Output lines: $LINES (expected ~3453)"
if [ "$LINES" -lt 3400 ]; then
  echo "ERROR: Output incomplete! Only $LINES lines."
  exit 1
fi

echo "=== Step 4: Run analysis ==="
python code/conll_seed456_analysis.py

echo "=== Step 5: Cleanup merged model (save disk) ==="
rm -rf checkpoints/qwen3-8b-conll2003-merged
echo "Cleaned up merged model"

echo "=== ALL DONE ==="
