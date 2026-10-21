import json, os, numpy as np, torch
from transformers import AutoTokenizer
from fla.models.gated_deltanet import GatedDeltaNetForCausalLM

MODEL_DIR = '/root/autodl-tmp/models_1.3b'
DATA_DIR = '/root/entrainment_gated_ft/lm_eval_clean'
DEVICE = 'cuda:0'

with open(os.path.join(DATA_DIR, '1.3B-100B-GatedDeltaNet-pure.json')) as f:
    d = json.load(f)
samples = sorted(d['samples']['lambada_openai'], key=lambda x: x['doc_id'])[:8]
texts = [s['doc']['text'] for s in samples]
print(f"Loaded {len(texts)} samples")

model_path = os.path.join(MODEL_DIR, '1.3B-100B-GatedDeltaNet-pure')
tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = GatedDeltaNetForCausalLM.from_pretrained(model_path, torch_dtype=torch.float16).to(DEVICE)
model.eval()
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

encodings = tokenizer(texts[:4], return_tensors='pt', padding=True, truncation=True, max_length=512)
input_ids = encodings['input_ids'].to(DEVICE)
attention_mask = encodings['attention_mask'].to(DEVICE)
print(f"Input shape: {input_ids.shape}")

with torch.no_grad():
    outputs = model(input_ids=input_ids, attention_mask=attention_mask)
    logits = outputs.logits
print(f"Logits shape: {logits.shape}")

shift_logits = logits[:, :-1, :].contiguous()
shift_labels = input_ids[:, 1:].contiguous()
shift_mask = attention_mask[:, 1:].contiguous()

loss_fct = torch.nn.CrossEntropyLoss(reduction='none')
token_losses = loss_fct(shift_logits.view(-1, shift_logits.size(-1)), shift_labels.view(-1)).view(shift_labels.shape)
masked = token_losses * shift_mask.float()
lengths = shift_mask.sum(dim=1).float()
sample_losses = (masked.sum(dim=1) / lengths.clamp(min=1)).cpu().numpy()

for i, loss in enumerate(sample_losses):
    print(f"  Sample {i}: loss={loss:.4f}, ppl={np.exp(loss):.2f}, len={int(lengths[i])}")

print(f"\nGPU memory: {torch.cuda.max_memory_allocated()/1024**3:.2f} GB")
del model; torch.cuda.empty_cache()
print("Dry-run OK.")
