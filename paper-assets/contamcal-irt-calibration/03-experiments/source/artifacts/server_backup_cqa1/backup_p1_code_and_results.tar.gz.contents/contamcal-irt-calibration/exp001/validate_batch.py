"""Quick validation: compare single-item vs batch GSM8K inference."""
import os, sys, re, json, torch
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
sys.path.insert(0, "/root/contamcal-irt-calibration/exp001")

from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from tqdm import tqdm

MODEL = "Qwen/Qwen2.5-3B"
CACHE = "/root/autodl-tmp/.hf_cache"
N = 50
BATCH_SIZE = 8
MAX_NEW_TOKENS = 256

def extract_gsm8k_answer(text):
    match = re.search(r'####\s*(.+?)(?:\n|$)', text)
    if match:
        answer = match.group(1).strip().replace(",", "")
        return re.sub(r'[^-\d.]', '', answer)
    numbers = re.findall(r'-?\d+(?:,\d{3})*(?:\.\d+)?', text)
    if numbers:
        return numbers[-1].replace(",", "")
    return None

print("Loading model...")
tokenizer = AutoTokenizer.from_pretrained(MODEL, cache_dir=CACHE, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(MODEL, cache_dir=CACHE, torch_dtype=torch.bfloat16,
                                              trust_remote_code=True, device_map="auto")
model.eval()
if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

ds = load_dataset("openai/gsm8k", "main", split="test", cache_dir=CACHE)
ds = ds.select(range(N))
train_ds = load_dataset("openai/gsm8k", "main", split="train", cache_dir=CACHE)

fewshot_examples = []
for idx in range(8):
    row = train_ds[idx]
    fewshot_examples.append(f"Question: {row['question']}\nAnswer: {row['answer']}")
fewshot_prefix = "\n\n".join(fewshot_examples) + "\n\n"

def format_chat(text):
    messages = [{"role": "user", "content": text}]
    return tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

# Prepare prompts and golds
prompts = []
golds = []
for row in ds:
    gold = row["answer"].split("####")[-1].strip().replace(",", "")
    gold = re.sub(r'[^-\d.]', '', gold)
    golds.append(gold)
    raw = fewshot_prefix + f"Question: {row['question']}\nAnswer: Let's think step by step.\n"
    prompts.append(format_chat(raw))

# --- Single-item inference ---
print(f"\n=== Single-item inference ({N} samples) ===")
single_preds = []
for i, prompt in enumerate(tqdm(prompts, desc="Single")):
    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=2048).to(model.device)
    with torch.no_grad():
        output_ids = model.generate(**inputs, max_new_tokens=MAX_NEW_TOKENS, do_sample=False,
                                     pad_token_id=tokenizer.pad_token_id)
    generated = tokenizer.decode(output_ids[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
    single_preds.append(extract_gsm8k_answer(generated))

# --- Batch inference ---
print(f"\n=== Batch inference ({N} samples, bs={BATCH_SIZE}) ===")
batch_preds = []
orig_side = tokenizer.padding_side
tokenizer.padding_side = "left"
for i in tqdm(range(0, N, BATCH_SIZE), desc="Batch"):
    batch = prompts[i:i+BATCH_SIZE]
    inputs = tokenizer(batch, return_tensors="pt", padding=True, truncation=True, max_length=2048).to(model.device)
    with torch.no_grad():
        output_ids = model.generate(**inputs, max_new_tokens=MAX_NEW_TOKENS, do_sample=False,
                                     pad_token_id=tokenizer.pad_token_id)
    input_len = inputs["input_ids"].shape[1]
    for j in range(len(batch)):
        generated = tokenizer.decode(output_ids[j][input_len:], skip_special_tokens=True)
        batch_preds.append(extract_gsm8k_answer(generated))
tokenizer.padding_side = orig_side

# --- Compare ---
print(f"\n=== Results ===")
match = 0
diffs = []
for i in range(N):
    if single_preds[i] == batch_preds[i]:
        match += 1
    else:
        diffs.append({"idx": i, "gold": golds[i], "single": single_preds[i], "batch": batch_preds[i]})

print(f"Match: {match}/{N} ({100*match/N:.1f}%)")
single_correct = sum(1 for s, g in zip(single_preds, golds) if s is not None and s == g)
batch_correct = sum(1 for b, g in zip(batch_preds, golds) if b is not None and b == g)
print(f"Single accuracy: {single_correct}/{N} ({100*single_correct/N:.1f}%)")
print(f"Batch  accuracy: {batch_correct}/{N} ({100*batch_correct/N:.1f}%)")
if diffs:
    print(f"\nDifferences ({len(diffs)}):")
    for d in diffs[:10]:
        print(f"  idx={d['idx']}: gold={d['gold']}, single={d['single']}, batch={d['batch']}")
