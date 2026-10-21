#!/bin/bash
set -e
source /root/miniconda3/bin/activate
cd /root/autodl-tmp/struct_self_consist_ie

export CUDA_VISIBLE_DEVICES=0

echo "=== $(date) === Step 1: Merging LoRA adapter ==="
python -c "
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch, os

base_path = '/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B'
adapter_path = 'output/exp_021_fewnerd_full'
merged_path = 'checkpoints/qwen3-8b-fewnerd-exp021-merged'

if os.path.exists(os.path.join(merged_path, 'config.json')):
    print(f'Merged model already exists at {merged_path}, skipping...')
else:
    print('Loading base model...')
    model = AutoModelForCausalLM.from_pretrained(base_path, torch_dtype=torch.bfloat16, device_map='cpu')
    print('Loading adapter...')
    model = PeftModel.from_pretrained(model, adapter_path)
    print('Merging...')
    model = model.merge_and_unload()
    print(f'Saving to {merged_path}...')
    os.makedirs(merged_path, exist_ok=True)
    model.save_pretrained(merged_path)
    print('Saving tokenizer...')
    tokenizer = AutoTokenizer.from_pretrained(adapter_path)
    tokenizer.save_pretrained(merged_path)
    print('Merge complete!')
"

echo "=== $(date) === Step 2: Running inference seed=123 ==="
python code/run_mvp_pilot.py \
    --model_path checkpoints/qwen3-8b-fewnerd-exp021-merged \
    --data_dir data/fewnerd \
    --dataset fewnerd \
    --subtask ner \
    --n_samples 8 \
    --temperature 1.0 \
    --seed 123 \
    --collect_logprobs \
    --output_dir output/exp_021_fewnerd_n8_seed123

echo "=== $(date) === Step 3: Running analysis ==="
python code/analyze_fewnerd_results.py \
    --input_dir output/exp_021_fewnerd_n8_seed123 \
    --output_dir output/exp_021_fewnerd_n8_seed123

echo "=== $(date) === All done ==="
