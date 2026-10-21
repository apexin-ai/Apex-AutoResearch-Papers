from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch, os

base_path = '/root/autodl-tmp/.hf_cache/LLM-Research/Meta-Llama-3___1-8B-Instruct'
lora_path = '/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-scierc-lora'
out_path = '/root/autodl-tmp/struct_self_consist_ie/checkpoints/llama3.1-8b-scierc-merged'

print('Loading base model...')
model = AutoModelForCausalLM.from_pretrained(base_path, torch_dtype=torch.bfloat16, device_map='cpu')
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
print('DONE')
