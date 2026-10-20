from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch, os

base_path = '/root/autodl-tmp/models/Qwen3-4B/Qwen/Qwen3-4B'
lora_path = 'checkpoints/qwen3-4b-conll2003-lora/checkpoint-4200'
out_path = 'checkpoints/qwen3-4b-conll2003-merged-ckpt4200'

print('Loading base model...')
model = AutoModelForCausalLM.from_pretrained(base_path, torch_dtype=torch.bfloat16, device_map='cpu')
print('Loading LoRA adapter from checkpoint-4200...')
model = PeftModel.from_pretrained(model, lora_path)
print('Merging...')
model = model.merge_and_unload()
os.makedirs(out_path, exist_ok=True)
print(f'Saving merged model to {out_path}...')
model.save_pretrained(out_path, safe_serialization=True)
print('Saving tokenizer...')
tokenizer = AutoTokenizer.from_pretrained(base_path)
tokenizer.save_pretrained(out_path)
print('MERGE_DONE')
