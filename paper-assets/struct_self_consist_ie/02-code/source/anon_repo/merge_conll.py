from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch, os

base_path = '/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B'
lora_path = 'checkpoints/qwen3-8b-conll2003-lora/checkpoint-400'
out_path = 'checkpoints/qwen3-8b-conll2003-merged'

print('Loading base model...')
model = AutoModelForCausalLM.from_pretrained(base_path, dtype=torch.bfloat16, device_map='cpu')
print('Loading LoRA adapter...')
model = PeftModel.from_pretrained(model, lora_path)
print('Merging...')
model = model.merge_and_unload()
print(f'Saving merged model to {out_path}...')
os.makedirs(out_path, exist_ok=True)
model.save_pretrained(out_path, safe_serialization=True)
print('Saving tokenizer...')
tokenizer = AutoTokenizer.from_pretrained(lora_path, trust_remote_code=True)
tokenizer.save_pretrained(out_path)
print('DONE - merge complete')
