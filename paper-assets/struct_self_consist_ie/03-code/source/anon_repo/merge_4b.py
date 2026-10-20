from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

print('Loading base model...')
model = AutoModelForCausalLM.from_pretrained(
    '/root/autodl-tmp/models/Qwen3-4B/Qwen/Qwen3-4B',
    dtype=torch.bfloat16,
    device_map='cpu'
)
print('Loading LoRA adapter...')
model = PeftModel.from_pretrained(model, 'checkpoints/qwen3-4b-conll2003-lora')
print('Merging...')
model = model.merge_and_unload()
print('Saving merged model...')
model.save_pretrained('checkpoints/qwen3-4b-conll2003-merged')
tokenizer = AutoTokenizer.from_pretrained('/root/autodl-tmp/models/Qwen3-4B/Qwen/Qwen3-4B')
tokenizer.save_pretrained('checkpoints/qwen3-4b-conll2003-merged')
print('MERGE_DONE')
